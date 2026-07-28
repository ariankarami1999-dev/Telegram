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
<img src="https://cdn4.telesco.pe/file/XE2AfZ8KAxP7vqgjTayhmFRWqLjdWD9nRNgRLwBLTBoIedyZgpvCkusoZrXF4kqInZCHa7QRI_a6nmWpwxWN8HcPti74WFRmr4BWnNzWlRsADHruuJB0DyMcpxGEukTzdODVErV88f6f9bmmeRpEJ76qru0EmsEtdyus7Ferz6LIufagy7M-wFIrAyaC7dgcP0tRM41Sauv-dTxp51XnR9v89-NxH_Bqw3Vm2lut0YY1jWYfhwjclvaCzEIU-av2UXv2WEZd8udyMSIRKR74OvNp08K6iir7DEHo9mWFWXhcQwDcDl6TbxZFtYcGTnVdPVP0I_OJQEZhFEAvvwh1Rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-19867">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر جنگ اسرائیل:ما قویاً خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
۷۰ درصد غزه را نابود کردیم و الگوی آن را به جنوب لبنان منتقل کردیم.
ایالات متحده در موضوع ایران ملاحظات و منافعی دارد که با منافع اسرائیل متفاوت و فراتر از آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/withyashar/19867" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19866">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال ۱۲ اسرائیل , وزیر دفاع کاتز فاش کرد: جنگنده‌های آمریکایی از اسرائیل برای انجام حملات به ایران به پرواز درمی‌آیند‌ و ایرانی‌ها از این موضوع آگاه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/19866" target="_blank">📅 13:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19865">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مهاجرانی: هواپیمای تازه‌خریداری‌شده در فرودگاه بوشهر بر اثر اصابت موشک منهدم شد؛ تنها بخشی از دم هواپیما باقی مانده است
@WarRoom</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/19865" target="_blank">📅 12:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19864">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام کاخ سفید: ترامپ در کاخ سفید با زلنسکی و نتانیاهو به طور جداگانه و پشت سر هم دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/19864" target="_blank">📅 11:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19863">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/19863" target="_blank">📅 11:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19862">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مدیرکل مدیریت بحران استانداری اصفهان:صداهای شبیه به انفجار در برخی مناطق جنوب و غرب اصفهان، بهارستان و حومه ارتفاعات صفه و شهر ابریشم شنیده خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/19862" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19861">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سخنگوی دولت: سهمیه بنزین ۳ هزار تومنی از ۱۰۰ لیتر به ۵۰ لیتر کاهش پیدا کرده
اما هنوز هیچ تصمیمی به صورت جمع‌بندی شده برای قیمت بنزین در جایگاه نگرفتیم
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/19861" target="_blank">📅 11:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19860">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏زلنسکی و نتانیاهو همزمان به کاخ سفید رسیدند
‏ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، و نتانیاهو، نخست‌وزیر اسرائیل، همزمان وارد کاخ سفید شدند تا در دیدارهایی جداگانه با پرزیدنت ترامپ گفت‌وگو کنند.
‏همزمانی حضور این دو رهبر در کاخ سفید، گمانه‌زنی‌ها درباره احتمال دیداری محرمانه میان آن‌ها برای جنگ همه‌جانبه با رژیم جمهوری اسلامی را افزایش داده است.
‏این دیدارها در شرایطی انجام می‌شود که پرونده‌های امنیتی مهمی از جمله جنگ اوکراین و تهدیدهای مرتبط با رژیم جمهوری اسلامی در دستور کار واشنگتن قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19860" target="_blank">📅 10:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19859">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19859" target="_blank">📅 10:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19858">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند  @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19858" target="_blank">📅 09:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19857">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جلسۀ شورای هماهنگی مجلس با حضور قالیباف
سخنگوی هیئت‌رئیسۀ مجلس: صبح امروز جلسۀ شورای هماهنگی مجلس با حضور قالیباف، اعضای هیئت‌رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19857" target="_blank">📅 09:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxHqv1fLLMlSDzTBtnVUicd9BclYBsxfhu0fD1oLN944Wj4qp4GpH2MyAJlMLSNlu6jIunKDPYsgJvMz0Gp4UxPx4ca1_WdCm31wQ3EOuRjC30ccxxscELhZHl3wASgx6FefudS4PYKCqz_1mgyOc4x8ZKSasdFpIHI9cyGq4JN5Zn3i-o_du5U7S5ekYy1ShvVEwb8j3YhpCceD6mazs2ZuUEtF5q6ddOVjnRj1CCCsBT9CD-T-KhVo_z-GmHuOm-32a7kNVcQ7XeAnSjAuTue5KjsBH4iA3RPuYfKnr34Hu4HUkonNqxHlbof_7xwaMqwRbqLuIKGmk1qHpQ_x9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویرک پست : ملانیا و بارون ترامپ در ویدئویی نگران‌کننده که ترور آنها را تشویق می‌کند
یک ویدئوی جدید از ایران، حامیان رژیم اسلامی را به ترور همسر رئیس جمهور ترامپ تشویق می‌کند.
این ویدئو با عنوان «چگونه ملانیا ترامپ را بکشیم» تصاویری از بانوی اول را در کاروان موتوری و در برخی مکان‌های اطراف شهر نیویورک نشان می‌دهد و حتی نام برخی از فروشگاه‌های طراحان مد که او از آنها خرید می‌کند را نیز ذکر می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19856" target="_blank">📅 09:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">روزنامه لبنانی "النذاع الوتان"، که با مخالفان حزب‌الله همسو است، امروز به نقل از منابع خود گزارش داد که ایالات متحده پیامی قاطع و جدی به لبنان ارسال کرده است. این پیام حاکی از آن است که هزینه دخالت حزب‌الله به نفع ایران و انجام حملات علیه اسرائیل ( در صورتی که ایالات متحده یک عملیات گسترده علیه تهران آغاز کند ) بسیار سنگین خواهد بود. منابعی که در این روزنامه ذکر شده‌اند، گفتند که این پیام به این معناست که هر راکت یا پهپادی که به سمت اسرائیل شلیک شود، در واقع دروازه‌های جهنم را برای حزب‌الله و لبنان باز خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19855" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش انفجار در اردن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19854" target="_blank">📅 08:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGy9WO7dgLpSBFCr4dO8DAA6IgEepdspATCX0UxK0KM2uWkoy65IxFkrkfGZekFWftwxgn1rPzMblgw3OZ_D7UEG_vgnXfSKOzI9m7FsB36CEyujelQKW0bWO2sm-YDuYQkootlqbwBtgQleDa8Yp-bN7xQGhwGja1xms4_APk6PhRlKnAwcw0XLtjC_DQpm6l3QTqOT2Bqen9K2PNQ2gYFHYGi60XO-apEMBWCuThv0kEHCXVC2QVU2pja-y3mSb9UjrN16B_L3dyJqz6LTojiaGxoZKRFDzF17XrIUk-vcr-2iD4yDWIWshtBK4EH0DQerTj6trmJTzIK1sBCZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار نفت سعودی شده و همکنون 89 دلار است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19853" target="_blank">📅 08:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhZU6SI0MXdvGyqEi6U_kz1THaUye0Ma6ShrshmdVFj2Ykml0BINdCpT1TBxdlL5OgvX8h2fT8MRb2wxtiG1AJ1-Nmrcew76C4d8-xLwzSUzLyNfa-2guWt3FMEF7NrxQcreomE_Szu2GbwvmFjcRTTWcJc6hXUyykcpQVh2Y0xVuM_3ihoKGLkk8SqLjGCf2CRo3Hlb4p67lqn7_9NBjiaIbjYhPX4xCwDKD_aepC3BAMNrYcIxnbfjN9WonP3cJ39KZegPsxE2FpT_-V8GVsVT8AGIZa5d-fM1y15EGd6LaeaT3UIY2p0QHXinlIB5H8uZuIbCgczztfx3LMSHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و همسرش با «اطلاعات محرمانه‌ای» درباره ایران و تأسیسات هسته‌ای کوه کلنگ وارد واشنگتن دی‌سی شدند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19852" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19851">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به گزارش وال استریت ژورنال، رئیس جمهور ترامپ پس از آنکه بیش از یک سال به مشاورانش گفته بود که کیف در حال شکست در جنگ است، به طور فزاینده‌ای نسبت به چشم‌انداز اوکراین در جنگ علیه روسیه خوش‌بین شده است.
ترامپ «برندگان را دوست دارد» و اکنون به طور فزاینده‌ای زلنسکی را یکی از آنها می‌داند. انتظار می‌رود این دو رهبر روز سه‌شنبه در جریان سفر زلنسکی به واشنگتن برای مراسم تشییع جنازه سناتور لیندسی گراهام در کاخ سفید دیدار کنند.
او تحت تأثیر صنعت پهپاد اوکراین، به ویژه توانایی آن در مقابله با پهپادهایی مشابه پهپادهایی که ایالات متحده در جریان درگیری با ایران با آنها مواجه شده است، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19851" target="_blank">📅 08:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19850">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19850" target="_blank">📅 08:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19849">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شنیده شدن صدای انفجار در اربیل در شمال عراق
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19849" target="_blank">📅 00:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19847">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=DKsneSUQvmg6iQyV4mo5au7c4aY-4CxD9l3CxP9OyrOdPk8U3RkE2koz15JWtr7nPXMLyLsW32k9v9qxbQwY0ua8L6v2gfhOjShE9JmzZujNOTJkX2aaIXl4qiMWurrmQHtRnAgvLu5FS4sG5vxMCsaVXpGIW5L1WMxo9p072s2U1oJVEpRkofwuy8EeKuk6huNmpz8R6ixuyQaAfIoFhZQ3wb6SFvWO9kB1uNopXi728R4Qmm6GQcy3qPD51CFxjK6hEGQz5F8DyUAiZc5NWsS1sSnH8oeAmTNNe4NiK_gyIK-AnbHXWiPHSP3xcMld42O3QQ70JgmsPBUbnRjyLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=DKsneSUQvmg6iQyV4mo5au7c4aY-4CxD9l3CxP9OyrOdPk8U3RkE2koz15JWtr7nPXMLyLsW32k9v9qxbQwY0ua8L6v2gfhOjShE9JmzZujNOTJkX2aaIXl4qiMWurrmQHtRnAgvLu5FS4sG5vxMCsaVXpGIW5L1WMxo9p072s2U1oJVEpRkofwuy8EeKuk6huNmpz8R6ixuyQaAfIoFhZQ3wb6SFvWO9kB1uNopXi728R4Qmm6GQcy3qPD51CFxjK6hEGQz5F8DyUAiZc5NWsS1sSnH8oeAmTNNe4NiK_gyIK-AnbHXWiPHSP3xcMld42O3QQ70JgmsPBUbnRjyLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست وزیر قطر: پول‌هایی که به حماس پرداخت می‌شد، شفاف بود و با مجوز دولت بنت انجام می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19847" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19846">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3e86fee4.mp4?token=i3ym5G07bBWWvHxr4p3p-Tp4E0AX7G1Z1lXHHenhpLECpaXLm-DSt4BGS5QUoBlew1nSvpUcYkft4EBrat0dS8239kCRfddmaIE6o244sqZk71bI_fhHnqhrjqcPQhM35_6l_Dl9qo6-uuIUz-BFRSssb6ykJ3lLPi4VoBg67DT6y8BND7036SatOmObnJtvTROJ_9NTr_Md_j1uZ7PmrF1aDp4Xp-1VhTMqpV62gG-GUIPIMftEOlYGdm5wRkg96LrIOZbZLUCMvUCxRul8ZjyevySnfJke1WYe_juIVC3l92F4XLj9Pwfp-szJbannEr5kJV4IciaHiP5zUNqeT5k_7oe7aUCl1hTwMKXrM06mM3Sp4fVfflEz5Bj79w4DEZyvcBrJn2WqrgOHK1tVbrewPzkuDyA1GIrmr5Vw-QDjxx7wtGTY2Q-Fugn0rEDu5hgX1m_T3q7tOFkO39cxjfrQksTpcVLjwETeneIid-Uzftbc91jOJa0KOMJKdh-zuVMTRBvp26BPbhmejj2EXf81cyBsZHDpYKyYsvROlF1wLYM--8RsqyCCr8YVcl525h5td4Re6y05I9lscmfa5uZt0GQT-1zNCPwGHpFaRZW5MIz9D8e0yqL0EbNi8Apd5NUKVALsr0F65nD7OiJqWwsw7dBbd9p3EHm1S0eynBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3e86fee4.mp4?token=i3ym5G07bBWWvHxr4p3p-Tp4E0AX7G1Z1lXHHenhpLECpaXLm-DSt4BGS5QUoBlew1nSvpUcYkft4EBrat0dS8239kCRfddmaIE6o244sqZk71bI_fhHnqhrjqcPQhM35_6l_Dl9qo6-uuIUz-BFRSssb6ykJ3lLPi4VoBg67DT6y8BND7036SatOmObnJtvTROJ_9NTr_Md_j1uZ7PmrF1aDp4Xp-1VhTMqpV62gG-GUIPIMftEOlYGdm5wRkg96LrIOZbZLUCMvUCxRul8ZjyevySnfJke1WYe_juIVC3l92F4XLj9Pwfp-szJbannEr5kJV4IciaHiP5zUNqeT5k_7oe7aUCl1hTwMKXrM06mM3Sp4fVfflEz5Bj79w4DEZyvcBrJn2WqrgOHK1tVbrewPzkuDyA1GIrmr5Vw-QDjxx7wtGTY2Q-Fugn0rEDu5hgX1m_T3q7tOFkO39cxjfrQksTpcVLjwETeneIid-Uzftbc91jOJa0KOMJKdh-zuVMTRBvp26BPbhmejj2EXf81cyBsZHDpYKyYsvROlF1wLYM--8RsqyCCr8YVcl525h5td4Re6y05I9lscmfa5uZt0GQT-1zNCPwGHpFaRZW5MIz9D8e0yqL0EbNi8Apd5NUKVALsr0F65nD7OiJqWwsw7dBbd9p3EHm1S0eynBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زامبی لند
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19846" target="_blank">📅 23:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19845">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c6fd33f33.mp4?token=vXSVhJ7YmAyqAzygOtfmcVFpns8XqjTZULTta1adJyNt0oKBDVTrmVmPp9T0JiGBzvPOr6nf3dF_gh0dU-LRCulhGUW_PCqnH_gAw7mT09aS7PvKGl1_8UPuWdkByV8NEm3u8Hlm_BUDLpqRBXBHTzJL4N-e44s1mSRg4tZIiX6IikukEPHwTBcJmv8b7qvJamzlXkFfY4bhpsQprmqulHU9ViZW0KnmzhRVdkrrXfS2KC0P8eZ7eilVzIA9m1s3iQDHpBaJxdlPyOwcBweJpj8hcGRmZLxKQl_56KqB7PLKc6AVtDyAnKeW_K5iAsVoPtvBGV7fP0_FOBYXqbb4Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c6fd33f33.mp4?token=vXSVhJ7YmAyqAzygOtfmcVFpns8XqjTZULTta1adJyNt0oKBDVTrmVmPp9T0JiGBzvPOr6nf3dF_gh0dU-LRCulhGUW_PCqnH_gAw7mT09aS7PvKGl1_8UPuWdkByV8NEm3u8Hlm_BUDLpqRBXBHTzJL4N-e44s1mSRg4tZIiX6IikukEPHwTBcJmv8b7qvJamzlXkFfY4bhpsQprmqulHU9ViZW0KnmzhRVdkrrXfS2KC0P8eZ7eilVzIA9m1s3iQDHpBaJxdlPyOwcBweJpj8hcGRmZLxKQl_56KqB7PLKc6AVtDyAnKeW_K5iAsVoPtvBGV7fP0_FOBYXqbb4Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برای مدتی قیمت سوخت پایین آمد. سپس آنها رفتار مناسبی نداشتند و من مجبور شدم برگردم.
حالا آنها دوباره رفتار مناسبی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19845" target="_blank">📅 23:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19844">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c208632.mp4?token=Tyxz4QUBdLTBzj1kkC2vrKkCONNKK5nbyq1X9Uh9KXLjMn67a5UwFUSOSINYlg0jcuIf7a06TwV2UEJRxfwyL2zoCDo1WmZ9vFtAyNthIK88wLowBrGviqBqIBwKA5z2sIX_NkGX42csvaFrhxxXHf9AqG1f0CywSxyny_-InRR6dnjPke0ceYCSQGr97iK8IdpHSEzULbZ-dEZOCUFsqr7xgxvxVxjL7BL8hYSAZ1ywWB1zficsspF_6KiLgqDJUdKZvzjxBMkDo2xSu668hj0kIGN2GoXUgSWWaAZvN8aBDxtzr4al6Nw99QQD689CM_BuLxFMpTs4u3BHyvn6uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c208632.mp4?token=Tyxz4QUBdLTBzj1kkC2vrKkCONNKK5nbyq1X9Uh9KXLjMn67a5UwFUSOSINYlg0jcuIf7a06TwV2UEJRxfwyL2zoCDo1WmZ9vFtAyNthIK88wLowBrGviqBqIBwKA5z2sIX_NkGX42csvaFrhxxXHf9AqG1f0CywSxyny_-InRR6dnjPke0ceYCSQGr97iK8IdpHSEzULbZ-dEZOCUFsqr7xgxvxVxjL7BL8hYSAZ1ywWB1zficsspF_6KiLgqDJUdKZvzjxBMkDo2xSu668hj0kIGN2GoXUgSWWaAZvN8aBDxtzr4al6Nw99QQD689CM_BuLxFMpTs4u3BHyvn6uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
مذاکرات دوستانه‌ای در جریان است.
ایران می‌گوید: «لطفا، لطفا، محاصره نکنید.»
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19844" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19843">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4de1bcc9.mp4?token=Jm9FB5bPXCkRjdOamfAYfxN5VW11HuDzGmF37FUJHQFNVgMxsH6TpEvXKTsCCgFuXKVFMvC2cvRnZfqMANIelmVZFKyO_kmHoD4GUVOoDJuWrvft38qMKzRbrfqX5LYDAtGKCM8DZqF0qN2oWCKHbSxqtnre5dJoISwwvQl4BfDdRoVcKmgJ8Pw52HHxFtS5MZXcwo9tQOFiiO4HGn59QvvdhSB-RBAjZEVjP8KtW4gBewnVnBHR2kRcTatuJ_63atZgT5vsce1OKZNx8PVLcLgt_r7pu4nsCjlHDNNZNorNpAYLw217BndoyaPzrmwfK2Z3UND_AY2dz_C60LBHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4de1bcc9.mp4?token=Jm9FB5bPXCkRjdOamfAYfxN5VW11HuDzGmF37FUJHQFNVgMxsH6TpEvXKTsCCgFuXKVFMvC2cvRnZfqMANIelmVZFKyO_kmHoD4GUVOoDJuWrvft38qMKzRbrfqX5LYDAtGKCM8DZqF0qN2oWCKHbSxqtnre5dJoISwwvQl4BfDdRoVcKmgJ8Pw52HHxFtS5MZXcwo9tQOFiiO4HGn59QvvdhSB-RBAjZEVjP8KtW4gBewnVnBHR2kRcTatuJ_63atZgT5vsce1OKZNx8PVLcLgt_r7pu4nsCjlHDNNZNorNpAYLw217BndoyaPzrmwfK2Z3UND_AY2dz_C60LBHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
شما نمی‌توانید به آنها رشوه بدهید. شما باید آنها را شکست دهید.
و ما داریم آنها را به شدت شکست می‌دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19843" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19842">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a198bcb3de.mp4?token=gaLwmM2nBtv-7wYpnWNVTmVpazRVnD90ap42Gi2cq4MeIWKU-sAGFEKX_Fnfb1hJ8i7zY4q8v0HXyUEfuWQEe5zzg6u91za5mKW9_liheN76OrT18Y1kofQSW-AXJ2Z9SfYkVg4t-nL4YxVHTO992dAF_luSON6C6I1YMEOZj07gaccwcgE9viXNgtHtHR9KSEj1vXreLGOyVBnV18VCz_1anO6H_iW8yPehqBJVM0LNPZUwo7J-zgBFSD2YSjYwYNw1BEAaLaLMBK24Y0HuZfb6bRqpknnissM2ynmk37MkBVqAoYwvdcL8AJKnsozWYf6bbetuhBaYSp5psVUJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a198bcb3de.mp4?token=gaLwmM2nBtv-7wYpnWNVTmVpazRVnD90ap42Gi2cq4MeIWKU-sAGFEKX_Fnfb1hJ8i7zY4q8v0HXyUEfuWQEe5zzg6u91za5mKW9_liheN76OrT18Y1kofQSW-AXJ2Z9SfYkVg4t-nL4YxVHTO992dAF_luSON6C6I1YMEOZj07gaccwcgE9viXNgtHtHR9KSEj1vXreLGOyVBnV18VCz_1anO6H_iW8yPehqBJVM0LNPZUwo7J-zgBFSD2YSjYwYNw1BEAaLaLMBK24Y0HuZfb6bRqpknnissM2ynmk37MkBVqAoYwvdcL8AJKnsozWYf6bbetuhBaYSp5psVUJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : همون اتفاقی که توی ونزوئلا افتاد، داره توی ایران هم می‌افته
فقط مردم متوجهش نمی‌شن
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19842" target="_blank">📅 23:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19841">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/506238d711.mp4?token=r9C8IdG6gnBEMu0GitMoDozRUqI_iY8jXlygSSnykXgefqCbO18aJB2j89T1zeWOLNPmbsG7oRlqkYi--VeRoe-V8oedRkF6kdQWru4ZA4sp3kpp-R3uty-ll3ffAJB-KujendG2rcSjAh8d8S2vbodkyQLw5kYlYZnXch-EEg2vP_shsYRxPtwLcYUNTTL-arnqRVXOx5HAPYfWeS3E7q83s9DjuMrUIk1ee3U6Hi5zNaTSIq4ccmajo_-xmD7L7_3Kl1jWrtYMEtQyEm8Mq3zv7YvdEL20V4-3jxCzr_AUCi_SEqYBlupZayROaDqGYswVrrH8tBWSS3ZhBZ4dCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/506238d711.mp4?token=r9C8IdG6gnBEMu0GitMoDozRUqI_iY8jXlygSSnykXgefqCbO18aJB2j89T1zeWOLNPmbsG7oRlqkYi--VeRoe-V8oedRkF6kdQWru4ZA4sp3kpp-R3uty-ll3ffAJB-KujendG2rcSjAh8d8S2vbodkyQLw5kYlYZnXch-EEg2vP_shsYRxPtwLcYUNTTL-arnqRVXOx5HAPYfWeS3E7q83s9DjuMrUIk1ee3U6Hi5zNaTSIq4ccmajo_-xmD7L7_3Kl1jWrtYMEtQyEm8Mq3zv7YvdEL20V4-3jxCzr_AUCi_SEqYBlupZayROaDqGYswVrrH8tBWSS3ZhBZ4dCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به كشاورز زمين داد، چريك شد
به زن هويت داد، آنارشيست شد
به كارگر سهام داد، كمونيست شد
به هنرمند اعتبار داد، توده اى شد
به مسلمان حرمت داد، تروريست شد
به دانشجو بورسيه داد، ماركسيست شد
به اقليت حقوق برابر داد، جدايى طلب شد
@WarRoom
نسل ۵۷</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19841" target="_blank">📅 22:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19840">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipEEDKkqBCN4Ra8ItQdhCGfejJTItAN971W8WMmIycsoCq8C0Kflwct0epZz3s3X2RZb894ku2dHXqrIHzLvYYg_7KY-78YUogOk5TSEs1A44VpAigfJfMMrFLCCv_JX2okaz70weY0eJg9axcE-ua5IuDDItoe0v1fWD5EuZJcB9SFfLtHvJxe8vw9oxhR-OzCCWKlUK1zQ37_YeuEQ7yePdW21Z3dUWkED_QV1AihwN6PPRQP4wJU0IayUEF0c08-gMVDSkQamQD4eN9YiVRGDwELJ72ru9cMPCbM_ktrzkI1KOh29hfRLfYD5bexVftiSNR19IbVuEW5okXqWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عمو لیندزی بخاطر ما تا مونیخ اومد، حالا وقتشه ما بخاطرش تا واشنگتن بریم.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19840" target="_blank">📅 22:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19839">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=rVBw_LKJfkDFqJhchYgdUlriGrMJ6zJlfOVgFMLVrr4pqf0Amk9iQyjnEBY4r4gXs2KZ0S_XbLOitxQDHrpkqEAWXLUCMvupIZWBeM0f2GiDjgNT7_qqt4SlY9XVmR-i5DummZQmeaZltllWZbe0FMcoW8HlKS0Y2i1Ao5mwTT6dFc1wsxaoO7soZtwv2G753qNFxOO3AmrmG-fc0wMcdqK_2vpsn4fKs2ZyYluz-_tboK7A4TXHFGXtap0bWs-Ozn2NoKVhW1wFlEomBhKD8_GZK0pHY_bgVUyCX6Ze0yU1TLL1CPAyhf7GMenRci6EqLB3hEVWMqzot5uA_n5LR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=rVBw_LKJfkDFqJhchYgdUlriGrMJ6zJlfOVgFMLVrr4pqf0Amk9iQyjnEBY4r4gXs2KZ0S_XbLOitxQDHrpkqEAWXLUCMvupIZWBeM0f2GiDjgNT7_qqt4SlY9XVmR-i5DummZQmeaZltllWZbe0FMcoW8HlKS0Y2i1Ao5mwTT6dFc1wsxaoO7soZtwv2G753qNFxOO3AmrmG-fc0wMcdqK_2vpsn4fKs2ZyYluz-_tboK7A4TXHFGXtap0bWs-Ozn2NoKVhW1wFlEomBhKD8_GZK0pHY_bgVUyCX6Ze0yU1TLL1CPAyhf7GMenRci6EqLB3hEVWMqzot5uA_n5LR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏در برنامه دیشب مارک لوین پیشنهاد داده شد که یک دولت قانونی در تبعید با رهبری شاهزاده رضا پهلوی تشکیل داده بشه. مارک لوین این رو یک ایده فوق‌العاده خواند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19839" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19838">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال ۱۵ عبری: نتانیاهو در دیدار خود با ترامپ، تحت فشار زیادی قرار خواهد گرفت در مورد مسائل مختلف، از جمله سوریه، غزه و لبنان. این دیدار بسیار مهم است و امیدواریم که مقدمه‌ای برای یک عملیات مشترک بین اسرائیل و آمریکا علیه ایران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19838" target="_blank">📅 21:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19837">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرنگار: آیا نتانیاهو از شما می‌خواهد که با ایران به توافق برسید، یا از شما می‌خواهد که به حملات خود ادامه دهید؟
ترامپ: عملکرد بیبی عالی بود. ما در کنار هم عالی هستیم ، نمیخوام بگم ولی ایران اکنون ۸ درصد او چیزی هست که چهار ماه پیش بوده
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19837" target="_blank">📅 20:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19836">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ: از پوتین درباره ارائه کردن تصاویر ماهواره‌ای روسیه به ایران، سؤال خواهم کرد. با اسرائیل در مورد ایران مواضع بسیار نزدیکی داریم. ذخایر مهمات زیادی داریم و مایلم که مهمات بیشتری فراهم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19836" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19835">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19835" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19834">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرنگار: آیا شما و نتانیاهو در مورد ایران با هم موافق هستید؟
ترامپ: یک اختلاف جزئی وجود دارد، اما ما بسیار به هم نزدیک هستیم، بله.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19834" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19833">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: من زمان زیادی را با ایران سپری می‌کنم و فرصتی وجود دارد که اتفاقات خوبی رخ دهد.
ایران در طول چهارده روز گذشته، ضربه بزرگی دریافت کرده است.
آنها به ما با لحنی بسیار مؤدبانه درخواست کردند: "لطفاً دست از این کارها بردارید. بیایید ملاقات کنیم."
احتمال رسیدن به توافق وجود دارد.
اگر اقداماتی که ما انجام دادیم، صورت نگرفته بود، آن‌ها اکنون آمادگی مذاکره با ما را نداشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19833" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19832">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرنگار: آیا از وزیر دفاع، پیتر هیگز، به خاطر توصیه‌هایی که در ابتدای جنگ با ایران به شما ارائه کرد و نتایجی که در پی آن حاصل شد، احساس خشم یا ناامیدی کردید؟
ترامپ: نه، ایشان وظیفه‌اش را به بهترین نحو انجام داد. ما ارتش ایران را نابود کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19832" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19831">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wm57G2puJ4T3gVWarWLF3_nh0FTydVzUH1Q6nR3FS0VMbKOfKuPHpmkHUXcVC4KBOdSTRnM1EBKUXfPME9_8_PbenLXN4b0z0fb3SbGrokhf1p8T5kgaTHR5D74PuaO2hE0tdEVzc_JXbdL660M4mopMiPSVPmNKmjTW9P6U5_7Yjj_naExcbjSRPTxbvWn6WJ0giFa8dYulqBiKbOB2TYaCrd3vjqqk8-xIN7xDFCw1toe4pgw5L2_PfP3a3PqBWhgSUoJ78JHfc8GkeasXp-fAL3iGlI6HVLr-vjWmlbIh0wlq9l_MAM_NMT6EbHQoOslV6qgOKs74clUtFax4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19831" target="_blank">📅 20:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19830">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیویورک تایمز : ترامپ در حال بررسی سه گزینه اصلی در مورد ایران است: تشدید اقدامات نظامی، تشدید تحریم‌های اقتصادی، یا اعلام پیروزی و عقب‌نشینی نیروها.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19830" target="_blank">📅 19:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19829">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند. جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند. @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19829" target="_blank">📅 19:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19828">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTC397Ms2Uukk95hOfOBwLoGaGfZj8SdCHUnOggr27tjLQavk2q2d6mq8TPdFXaZEqIaPuEBP4IFBuonMVzhvGAR8oWpW3fLiUzjsZXNVBHjR2XXIggiZHtsx7qSAgtbxZavWdkYvN8Rc20IY8wVDP7nbj_8Bf8uFfRPxTog_XepvAcZt3Et9mf59LQldKjSEdRGU2aNiqhTBAxv1RNtjd0c2Q3qdSJJ3vUzonhEWDTJCH9bsRwYg2vuOeUlZywMF8HZU0WiIuMaZhX9qto7dabp64kztGjPEUYAlUrN4urbHtNXiqJuKTDTVdupn0TVZCjurWVLEA8CZR28nEBQ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک ملوان آمریکایی در حال گشت‌زنی در دریای عرب توسط ناو هواپیمابر یو اس اس فرانک ای. پترسن جونیور (DDG 121) است که از محاصره دریایی ایران توسط آمریکا حمایت می‌کند. سنتکام ۱۷ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی دیگر را توقیف کرده است تا از رعایت این تحریم‌ها اطمینان حاصل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19828" target="_blank">📅 19:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19827">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هم اکنون
تیراندازی نزدیک کنسولگری آمریکا در تورنتوی کانادا
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19827" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19826">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تامیز اسرائیل : بنیامین نتانیاهو در دیدار پیش‌رو با دونالد ترامپ در کاخ سفید قصد دارد اطلاعاتی جدید و حساسی درباره روند بازسازی برنامه‌های نظامی و هسته‌ای ایران ارائه کند. به گفته منابع اسرائیلی، این اطلاعات شامل ارزیابی‌هایی است که نشان می‌دهد ایران تلاش‌های خود را برای بازیابی توان نظامی و پیشبرد برنامه هسته‌ای افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19826" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19825">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرنگار:علت پذیرش درخواست میانجی‌ها برای توقف آتش توسط شما چی بود؟
ترامپ:چیزی برای از دست دادن یا به دست آوردن نبود ‏
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19825" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19824">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEQVQzGNzH_8wV3m_y-cepWzHnFyYRSWOXlTv-xiS9VZe5Z8GaGkWg_Twk2T1QXZaBsBWbnNPF74olW4zUj3xH_YuMq7K5fgpRH1PgTS5KOMSkZfqF5TwpzY2WwQeLyUijxu7f9_UlxMPG3_f2C1ok3Xm1hj_MVfRAif3jP4YKWwUqeCRTFdCMM5vPhOdfkc_c7StLnj_bU0bW_KPJ4synrCsDt7HkqNk9Lfy7mlHNi8-EFthqOX_PZGOlDkNPayWkyjN_HLimeWMOU9GW47aVPiPYfzsCvUFUulCrFJvEYiLEUS570_xY26pKnCGKxoOALus6dWFsOgFItqw6CpWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند.
جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19824" target="_blank">📅 18:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19823">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: به درخواست واسطه‌ها پاسخ دادم تا فرصتی برای مذاکره با ايران فراهم شود.
"من زمان زیادی را برای مذاکرات اختصاص نخواهم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19823" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19822">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: ما در حال انجام مذاکرات عمیقی با ايران هستیم و اگر این مذاکرات موفقیت‌آمیز نباشند، به یک عملیات نظامی گسترده باز خواهیم گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19822" target="_blank">📅 18:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19821">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کاظم دست کج : در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و اصرار داشت که مسیر جنوبی تنگۀ هرمز فعال باشد و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19821" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19819">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB97uN5Y-ppXd98uEMsDru6bOOJwlooZULx_Gjb23OENw0WGvYjTlUyx6dslR99HgKHq19tWuK4RqnmBnRwrm55YQ2t56BgaV9lGyhaVnwwMFxBr6jluprUiNPG21kdYeYON8Es61KoHsxmMOKNSj0eVzVkPcECWJPrTDOJ8uBO9NZVQ-6VunnmOmKteb7PQwz6DVGWOb34K4nudT0lfd32aLb-n2uT21A-v7ZCeYEqsh40vxK-lSjgJRuedRF4mvtr2U7H6xop2NQdGV1ZfXAMvwxoHROjXDTMqV8K_9csOvjhiRuxnMUNkw07MYV9OKrK94Dqto9oRTgTu-Yk-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19819" target="_blank">📅 17:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19818">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزارت امور خارجه عربستان : ما پهپادهایی که قصد هدف قرار دادن تاسیسات نفتی در مناطق شرقی و ریاض را داشتند از بین بردیم همچنین این حملات را که توسط شبه‌نظامیان تحت کنترل ایران در عراق انجام شده است محکوم می‌کنیم و تأکید می‌کنیم که پادشاهی عربستان سعودی مصمم است جلوی متجاوزان را بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19818" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19817">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همشهری: سران قوا با بنزین ۱۰ هزار تومانی برای سهمیه سوم موافقت کرده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19817" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19816">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جی دی ونس در انتقاد از اسرائیل برای جلوگیری از مذاکرات:
من قطعاً فکر میکنم شاهد یک کارزار بسیار پنهان و با بودجه بسیار بالا بودیم که تلاش میکنه مذاکرات رو منحرف کنه و مانع رسیدن به توافق بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19816" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19815">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=Xgul2ZIcIhO0PHUSPzlQLWgNvw0Y3Z15Cox6a2aF8U0UWrW_eyXT07y7yIo54afwqrOFjJKOHOaeltFy7mwMOQJrADKaOhW_agGhAO3zE-apOt_cjGRxJ2jGCQjB8v5_8EtkDsobAkm7TukgRcPfBJZ4WdfUaBZ9_vKrjXAjd4_xPIf2FMWxCvlAEsZB_vYP-ifNvqGOeFDXrGOan7dFWoHw4TCw-DJlCt4Z7NULQmQJitOSeN6g4BDYihZnj86G3TzjQ_LBketPktyjq3m1C2K_XXc9y8HmoYQ9fSC3sVsbhfLArjIx2Ib59dR4canBSJveNk1k86pIR0mPgRhYHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=Xgul2ZIcIhO0PHUSPzlQLWgNvw0Y3Z15Cox6a2aF8U0UWrW_eyXT07y7yIo54afwqrOFjJKOHOaeltFy7mwMOQJrADKaOhW_agGhAO3zE-apOt_cjGRxJ2jGCQjB8v5_8EtkDsobAkm7TukgRcPfBJZ4WdfUaBZ9_vKrjXAjd4_xPIf2FMWxCvlAEsZB_vYP-ifNvqGOeFDXrGOan7dFWoHw4TCw-DJlCt4Z7NULQmQJitOSeN6g4BDYihZnj86G3TzjQ_LBketPktyjq3m1C2K_XXc9y8HmoYQ9fSC3sVsbhfLArjIx2Ib59dR4canBSJveNk1k86pIR0mPgRhYHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: من با رئیس جمهور ترامپ در مورد مسائل مختلف گفتگو خواهم کرد، و در صدر این مسائل، ايران قرار دارد.هدف از سفر من به واشنگتن، تضمین امنیت، قدرت و آینده اسرائیل و همچنین گسترش دامنه صلح در منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19815" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19814">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzf5NjlECguVsRC-L6f95Aqsz_OXISNaAPznZ2Cmg5loBsh4xk1_kQK_yj77gQE-v_oy11p652bVLeFxoNw4yGDUIgmbbhlZJEmvUSk8tJksjtr2s1v9MZAJUx0x_FcmcIee2nQr8XoqmWOrTWYkxMDnS_0EQnr7P5fBHnZq0IDGQHE05kl-Lzz6kvkNDPZgGyF1ODd9_KdziVIydczHKyGBlSshsxxObsA8wvKzjpILoKbM1_sRR3zEWoUQpPntjSIlmILWB3pTd7lHOcObWgEBdz246b4sDrJrov3rA3LxmduTfOrurhduueU4Th10M0MfJVtQhOUVPyTCGGDr7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون کرج سمت فرودگاه پیام
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19814" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19813">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19813" target="_blank">📅 14:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19812">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUeY12sKCbN8ZVbRHERubEmnLNjtQDq6Uzz33kPD7ka8j2UrYlvQU05UN3A3j2mL8VD-wLHfd_M3GwgWpSGyEwQ6-5bBAiGgGPOudHS1VpHW0LK7bK5q4aU_or2h9ZnY8FMOuB2UOG4pBaN8fJMD_9uRynsKQzcpjDKxGKZnwnA3vHTwlJkWPnpIKPirc3Ty4mH-auTzJGfvMoFibvB6cDEsrJs27BlmNkcuUWEqlnm0Oy6iPv0qsPz-RFVTHWowaFZaAs7lXroUcGSmwJ0WiEYSGiMkFx7nFXExfjRQ6_NyXKHxwoh1Djx7_ZRKhaHRfq9B2E6i9wYeVfAk1Ts-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دهه هفتاد میلادی، در زمانی که در منطقه کسی نمیدانست سوخترستان حتی چیست. عکس بسیار زیبا از سوختگیری دو فروند بویینگ 747 شاهنشاهی بر فراز دماوند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19812" target="_blank">📅 14:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19811">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19811" target="_blank">📅 14:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19810">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=NTIrPHaV_Fgjudw54gylfi6iK_6L_Nu1KW2QihPen6w5PpZhyqAEhIKES5eWlh6nTmxtekZgQ59CJ7_aWz548DciII3DDgtdrzZR_B9TMBg6PIiE4tCA2BJ68xJLhlAJ9SOlO5Jsr9snDrxMpubwnXWie_rAO5INBVqONdfJRA2l-wCRy7F24b5__LEuPgpOwVkKzPyASdpA7ydQ7J_EfXjP4dKlvPAGTOR4pOrGU6d-2iy0tbB9SKA5iBIy_t6eXamCn3Bxl75sbL5CTGxIOJePVeuL9_aRafkr4zDGTrPlvMDBhSHJ5N0Ydwt4MJaEAyyfg_tojkKMFLz13az-vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9ca588d.mp4?token=NTIrPHaV_Fgjudw54gylfi6iK_6L_Nu1KW2QihPen6w5PpZhyqAEhIKES5eWlh6nTmxtekZgQ59CJ7_aWz548DciII3DDgtdrzZR_B9TMBg6PIiE4tCA2BJ68xJLhlAJ9SOlO5Jsr9snDrxMpubwnXWie_rAO5INBVqONdfJRA2l-wCRy7F24b5__LEuPgpOwVkKzPyASdpA7ydQ7J_EfXjP4dKlvPAGTOR4pOrGU6d-2iy0tbB9SKA5iBIy_t6eXamCn3Bxl75sbL5CTGxIOJePVeuL9_aRafkr4zDGTrPlvMDBhSHJ5N0Ydwt4MJaEAyyfg_tojkKMFLz13az-vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19810" target="_blank">📅 13:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19809">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKRoMfBGDVV2_lfhKKxt5GM0sanOgA-6upqVCXTLJTs5pEcjwE5rWcMAzzyVL8D5YM6MKwX5V9mMOJ5_SC2wU_gFAIj6l462NOV3jRsUWyoa7kS6yGuPGawdn8m7KuSkgIVj-V8EgncLmAv6zIi9KUzthNcYwTVpuFHn8VhEiWkb98B5GIP1N1ZsCsXrSO6DCUXrs5S3cYJ1wZlkYXPsyWhpO4eT_P2Qs2-kTU8S5HvCny5dvwaFQfFuNIwF2ZZc8oUMWEq5gm_D8-4YU2-imT3uiqMXGlYy7UyQcKVr4iGWZcxW-qh4vhdSBhW3HWItFxyP6VNQGD0wkuoHIPQOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای استاد بزرگ شطرنج بی بی نتانیاهو  تیک آف کرد و پرید ! تا کور شود رسانه هایی که خبر تاخییر رو کنسلی انتشار میدهند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19809" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19808">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19808" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19807">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ایتامار بن گویر، وزیر امنیت ملی اسرائیل گفت: «باید کارهای بیشتری انجام شود. من امیدوارم که دونالد ترامپ، رئیس جمهور آمریکا، متقاعد شود که ساده‌لوحی خود را متوقف کند. او یک تاجر است و در مورد مسئله ایران بسیار ساده‌لوح است. هیچ دیپلماسی با این افراد وجود ندارد، هیچ چیزی برای صحبت با آنها وجود ندارد. باید با ایرانی‌ها از طریق دوربین صحبت کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19807" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19806">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19806" target="_blank">📅 13:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19805">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دفتر نخست‌وزیر اسراییل از به تعویق افتادن پرواز ۱۱ صبح وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19805" target="_blank">📅 13:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19804">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuctEBkh9B8_RoggRuOoulh3dtLKSFkd-7eStG3M2Yx-7l4vRnPdBPxl4je2ZhoEFW1mV7uqXOu2IPvFbXuzJCMth6fbFMMsvSAmmPj-eR-wGIW9WGGVYqyEfLgN0N0cKtpjQm7lcD1XOdW8AxgJz_wRjJskv51Q6Bed-lUQuwMUfrLA5SiVyfs-aiSnwo7gOkDw9g8aggmBb5bwhQPmngbgD73X7cnJIWIQTOfP09vfnZoGIxJKOKgNbPbT3rlQtWCFwchYDXv6vBUyl_c3139dgYm6vYRKRJ03QPzHwhEJSL9MXMDUQGRfx3YUGchG9HNTpPwGPFGm8ymsZuQayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اطلاعات ۴ مرداد ۱۳۵۶. دقیقا سال پنجاه و شش هم همین موقع ها، هتل هیلتون آتش گرفته بود.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19804" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19803">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19803" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19802">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=fOQWJ6ASb8r-r4mJNtDLCeTInb80dFMdnOHUrvkkK7ezP2U38PTjFZYjCOpkMic2vqGST2nEmGgJWIEN54BcXvJLRfzc3SbUxC-exMoLRMNvq4dpXNnjysq0o_G_aiYO6Hd3gX9ol9tviWNNddar1o4-J1Ol3j-MEmzd3uQ-EI8DRtX31E5pJIA2CZEH83VvkxJqhRb7FHJXo35UdiK11I7bMxEMC-TGo9s25vm-D3nkkBiCygDgSuYYoJHb3gmj1vcjX9mMawtgQ7S9Co5ibhv5F6SH8E-nmWL-_IXA1DgDeRKPlPZ7EAeLLwtHwpr6tSPrZNLUAM6bH5qkDsdtcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db435b3a7.mp4?token=fOQWJ6ASb8r-r4mJNtDLCeTInb80dFMdnOHUrvkkK7ezP2U38PTjFZYjCOpkMic2vqGST2nEmGgJWIEN54BcXvJLRfzc3SbUxC-exMoLRMNvq4dpXNnjysq0o_G_aiYO6Hd3gX9ol9tviWNNddar1o4-J1Ol3j-MEmzd3uQ-EI8DRtX31E5pJIA2CZEH83VvkxJqhRb7FHJXo35UdiK11I7bMxEMC-TGo9s25vm-D3nkkBiCygDgSuYYoJHb3gmj1vcjX9mMawtgQ7S9Co5ibhv5F6SH8E-nmWL-_IXA1DgDeRKPlPZ7EAeLLwtHwpr6tSPrZNLUAM6bH5qkDsdtcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هتل در حال تخلیه است
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19802" target="_blank">📅 13:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19801">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArC4lx1piSfMQ8kD5aYTxzWtAibDkaKkXuoetoHpKkP60_ELK2dW6B0APpmlRvKF7iugz55v0GH8_jXFfL6LE8O72GUSIrDapxRKfUMJA4KnYpBQ_KDHZ6T_rWa1GQLh6lpuZbiGOkiTCzyJEF8BXdTPTivDKRmtk5hT3sHfBtAoFQWmH0MbI0lxVLPbS69IKQoI78Irr4DWmpwTRHwR5xCUMeLfWVSgHztlLCeSQkrPm1gcPzu6tSYBALcK9QLao5YixgN4vH3hqZ1_BdDyO84Q_txOVcs8ztR640pMH7hScwntigHMhD18TEIe_OjS6FFgUUg7E_r8pIidy2PWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی ساختمان هتل هیلتون
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19801" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جمهوری اسلامی  : تنگه بسته است
سخنگوی وزارت امور خارجه ایران گفت تهران به واشنگتن اجازه نخواهد داد شرایط پایان جنگ را دیکته کند و هشدار داد که تنگه هرمز همچنان بسته است. او همچنین اوکراین را به دلیل حمله ادعایی به یک کشتی ایرانی تهدید به تلافی کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19800" target="_blank">📅 12:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=cdfDXw-qByR9bBE6W1qhp-PJvFVGaEo_SztcwniT-ddczNX7eVK-Q8fL4W2GNONIh_E38cW3W-ihS2MSb9H64U99T7mxeNrXZP463K1-DOh59gvXSnWiT1C_lqYBxcxKuO1u4vDGTgUPuIuwRHGck_3tKgaCshN4W4kC9fDMM4u1AdzEoU0QgCbWCUbKEkdlyL2TjCA9mXxdakqd7zGXSMZdPdzZbdsPK3lVv2pzk2dP5Iz7dbj1MUgd2KwM4uALimWBT-HW1ZrvlcO0OFDFImOIrmUBxqykmWXenkW3X8okx0d9d6xF9PkzKMS7ToVzpMc33sy9Mf8hg4EKgPOUWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b0896ed8.mp4?token=cdfDXw-qByR9bBE6W1qhp-PJvFVGaEo_SztcwniT-ddczNX7eVK-Q8fL4W2GNONIh_E38cW3W-ihS2MSb9H64U99T7mxeNrXZP463K1-DOh59gvXSnWiT1C_lqYBxcxKuO1u4vDGTgUPuIuwRHGck_3tKgaCshN4W4kC9fDMM4u1AdzEoU0QgCbWCUbKEkdlyL2TjCA9mXxdakqd7zGXSMZdPdzZbdsPK3lVv2pzk2dP5Iz7dbj1MUgd2KwM4uALimWBT-HW1ZrvlcO0OFDFImOIrmUBxqykmWXenkW3X8okx0d9d6xF9PkzKMS7ToVzpMc33sy9Mf8hg4EKgPOUWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در
۲۰ و ۲۱ بهمن ۱۳۵۷
در پادگان‌هایی مانند
دوشان‌تپه، عشرت‌آباد، حشمتیه، لویزان و مراکز دیگر
مردم برای تصرف اسلحه وارد پادگان‌ها شدند و تعدادی افسر، درجه‌دار و سرباز را کشتند !
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19799" target="_blank">📅 12:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دیدار نتانیاهو و زلنسکی با ترامپ
گزارش ها از سفر قریب‌الوقوع و ناگهانی زلنسکی، رئیس جمهور اوکراین به آمریکا همزمان با سفر نتانیاهو به آمریکا
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19798" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست. @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19797" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد
بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19796" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Duizry8m6qgIgD8LTqVxOu2LjTSxgbCoRPXpGpkw9j_d-DpqHEz2UMJv63nh6aw6HMPG_rSziQxXxq2hCCrE3WtCLmo0CgLyy08WA08KhRCOSOraaVTFQYxk55be282nTx62L72yTKNfLSKN_ptsS2U7HDDdNQtRdS8SFKw1OZbwXvxTNdxvdnD0-zhZOGA2Fd2-CvYFWbYA9miuky3-Y9BkeF46n47_L7Et_KnN7rvNXbonFcGEiOVZ_XnpKlugkAhwLmRGQ7eS3uYd77BBnsAh54U5qQOCcHx-CJ1SW_GtXB_zuxGbYi4GdgLccI8G0UoEh49bjy9n6rQtmxdUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از «نیما مرادی» که در حمله اوکراین به کشتی ایرانی کشته شد. کشتی آنا از بندر آستاراخان عازم بندر انزلی بود.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19795" target="_blank">📅 11:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پوتین: شناورهای تندروی ایران در درگیری با آمریکا عملکردی موثر داشتند
رئیس‌جمهور روسیه در دیدار با فرماندهان و نظامیان ناوگان دریایی این کشور اعلام کرد که ایران در جریان درگیری نظامی با آمریکا با موفقیت از به‌اصطلاح «ناوگان پشه‌ای» (شناورهای کوچک و تندرو) استفاده کرده و این نیروها عملکردی کاملاً مؤثر از خود نشان داده‌اند
، توسعه چنین نیروهایی برای ناوگان دریایی روسیه نیز ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19794" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هواپیماهای تهاجمی A-10 Warthog برای عملیات احتمالی علیه ایران در خاورمیانه اعزام شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19793" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19792">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=G5xCRrML0OAV3fbDdltLNGOOvHjCmY-zenBpGNJU8kZYIP4ouWFrBKJpDYEAO5ydJGufEDeAobWYs5IjCeiyBuJO6sfITYb8g1AoQeCsUrHh_I03dIMo1-H5cA2KNgvxQ5S9wCTuqur-XbpJxGtevRinWvkfP5oKusgiFxdZpCzUfqLpAz-xkCJ4e8nDxRnYRhHQ05CDxHghOR40EgI-9Ejrv805H08xtbQu0khXH4Ec5grl3M_HKBWFz-YWD7qtXidU1qCRLydcxo0N2XkEzXTuDgQVK70o-VcmqAarBM_nbfE-FUgfY2HiWN1-j8LkDMijHh76ZfPv0hEVpw79SlOjBpYyCX1dRAtpeaxqH6ZxTQ09v0xJQlSzwW2VDuFR4uqbuvJfprIrNor4eiDJvLwXUgLZs9RM3SmXrklfmDBULY9Ha8Fns06tIPvQ2stYgY5H9pC-NI37XkR2sNZpvw6fIu2j-sNXTP9ROQvaLs7jMcQouFHcPazMIQ-naK3LHL1kEIJ13rhBsjSAaGiGeR9JScc9kf9rJtyZmRYi_lcqDOlOqD8lio7lb20S-lnHXzB16YDdLTHWXcfHp2m_LknYSyagZIm63pHaStJnkUQ4yKesRxK6d6xV08r2qFot9F2NAfKMsnF1DVrG3YEOcvBgvUaFiWeg1twxxm15cRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=G5xCRrML0OAV3fbDdltLNGOOvHjCmY-zenBpGNJU8kZYIP4ouWFrBKJpDYEAO5ydJGufEDeAobWYs5IjCeiyBuJO6sfITYb8g1AoQeCsUrHh_I03dIMo1-H5cA2KNgvxQ5S9wCTuqur-XbpJxGtevRinWvkfP5oKusgiFxdZpCzUfqLpAz-xkCJ4e8nDxRnYRhHQ05CDxHghOR40EgI-9Ejrv805H08xtbQu0khXH4Ec5grl3M_HKBWFz-YWD7qtXidU1qCRLydcxo0N2XkEzXTuDgQVK70o-VcmqAarBM_nbfE-FUgfY2HiWN1-j8LkDMijHh76ZfPv0hEVpw79SlOjBpYyCX1dRAtpeaxqH6ZxTQ09v0xJQlSzwW2VDuFR4uqbuvJfprIrNor4eiDJvLwXUgLZs9RM3SmXrklfmDBULY9Ha8Fns06tIPvQ2stYgY5H9pC-NI37XkR2sNZpvw6fIu2j-sNXTP9ROQvaLs7jMcQouFHcPazMIQ-naK3LHL1kEIJ13rhBsjSAaGiGeR9JScc9kf9rJtyZmRYi_lcqDOlOqD8lio7lb20S-lnHXzB16YDdLTHWXcfHp2m_LknYSyagZIm63pHaStJnkUQ4yKesRxK6d6xV08r2qFot9F2NAfKMsnF1DVrG3YEOcvBgvUaFiWeg1twxxm15cRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتهای زیبای ریچارد نیکسون در مورد شاه و اتفاقات آن روز.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19792" target="_blank">📅 10:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19791">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=H0A-Y8RWVgmfRVvLKTNU8EXJ0NdZ-xG-SenwEszIHePBULeuIrRAfVAQG5XjL3UVXXc8l6ivB0uubbE_I-XqBDJyI7Hm7UJ2bd4DGK7hmP9-kuiEEFJ8MzwolrP8R7lDMiWsREUiNb1eKzYyiNP3xw6S6_iaYQffH7yHH3ChYzxXUHaKimhPxuIPus7Z0awRWbP8vH8Xnx4tKoXNQIV-4PuZSrX3l86qFjMpM3D4IamZ4NBBgHH3JjCI-kEnnAo3sTSasd4Y6PYbcUoTsURmLwVrTNwEjQDZlykdKCPdGVf-vME73n8_dx6JXVrUS3hXJjRM-mbUK7AS0KOfPdqH1GW79mXFEDjOkNQp2_2j5dqDTZtnrPaxhQ26SWlrTbQTHR34Q2p5J65FM8Ayhpg_CZwlYd-CplbqIIgacEgxX4DDAaz_sfIsg3DQJvWs6lef2x2b93d9XeFN5CVjBLHFJ5xQn5QdCPYb_3Ct9q9KqUQtAoYHD0iJdHRcVQrcSlC2qEaQI7s0bkyPBj94WnZ6cU8BPih0756NJez0nl8cUGY9Ai8mYErqSRa5QYS6xgkLDau82LOvJJntIsUZM2RYqVjUhklv8ocl5K5Qvx1f0R72kT1dZZhifYCmA-jfbVh8CKV1EfDuJzohAORu734JHXfbaYHc3idABzXa8S_p6AU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=H0A-Y8RWVgmfRVvLKTNU8EXJ0NdZ-xG-SenwEszIHePBULeuIrRAfVAQG5XjL3UVXXc8l6ivB0uubbE_I-XqBDJyI7Hm7UJ2bd4DGK7hmP9-kuiEEFJ8MzwolrP8R7lDMiWsREUiNb1eKzYyiNP3xw6S6_iaYQffH7yHH3ChYzxXUHaKimhPxuIPus7Z0awRWbP8vH8Xnx4tKoXNQIV-4PuZSrX3l86qFjMpM3D4IamZ4NBBgHH3JjCI-kEnnAo3sTSasd4Y6PYbcUoTsURmLwVrTNwEjQDZlykdKCPdGVf-vME73n8_dx6JXVrUS3hXJjRM-mbUK7AS0KOfPdqH1GW79mXFEDjOkNQp2_2j5dqDTZtnrPaxhQ26SWlrTbQTHR34Q2p5J65FM8Ayhpg_CZwlYd-CplbqIIgacEgxX4DDAaz_sfIsg3DQJvWs6lef2x2b93d9XeFN5CVjBLHFJ5xQn5QdCPYb_3Ct9q9KqUQtAoYHD0iJdHRcVQrcSlC2qEaQI7s0bkyPBj94WnZ6cU8BPih0756NJez0nl8cUGY9Ai8mYErqSRa5QYS6xgkLDau82LOvJJntIsUZM2RYqVjUhklv8ocl5K5Qvx1f0R72kT1dZZhifYCmA-jfbVh8CKV1EfDuJzohAORu734JHXfbaYHc3idABzXa8S_p6AU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دیده نشده از مراسم محمدرضا شاه
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19791" target="_blank">📅 10:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19790">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏ساعت ۲۵ ایران ‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.» ‏انورسادات با لباس نظامى آمد،  ‏مستقيم به اتاق شاه رفت. ‏دستش را روى قلب شاه گذاشت،  ‏به انگليسی گفت: ‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»…</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19790" target="_blank">📅 10:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19789">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صداوسیما: در ساعات اولیه بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن موقعیت‌یاب خود قصد عبور از مسیر جنوب تنگه هرمز را داشتند که یکی از آنها دچار حادثه شده و بقیه تحت مدیریت ایران به خلیج فارس برگردانده شدند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19789" target="_blank">📅 10:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرنگار الجزیره: نیروهاى ارتش اسرائیل، به همراه بولدوزرهاى نظامی، وارد شهر عرابه، واقع در نزدیکی جنین، در کرانه باختری شدند
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19788" target="_blank">📅 09:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19787">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پنتاگن : از زمان شروع درگیری‌ها در ۹ اسفند، ۱۸ نظامی ایالات متحده کشته و ۶۲۴ تن زخمی شده‌اند
سی‌ان‌ان ‌: بر اساس اعلام پنتاگون، بیش از ۱۴۰ نظامی آمریکایی جدید به مجروحان جنگ علیه ایران، اضافه شدند
نام چهار سرباز آمریکایی کشته‌ شده در حملات ایران که از پایگاه داده‌های پنتاگون حذف شده بود نیز بازگردانده شد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19787" target="_blank">📅 09:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19786">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
ساعت ۲۵ ایران
‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.»
‏انورسادات با لباس نظامى آمد،
‏مستقيم به اتاق شاه رفت.
‏دستش را روى قلب شاه گذاشت،
‏به انگليسی گفت:
‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»
اما ‏آن روز كسی نفهميد معنی ساعت ۲۵ چيست؟
‏او در يک مصاحبه با خبرنگاران خارجى و داخلى ‏گفت: جهان عزادار شد.
‏امروز مردى از ميان ما رفت كه خواهان صلح بود، ‏بعد از او خاورميانه رنگ آرامش و آسايش به خود نخواهد ديد.
‏او فقط پادشاه ايران نبود.
‏پدرِ بزرگى براى منطقه خاورميانه بود و ‏روزهاى سختی را پشت سر گذاشت،
‏او براى دفاع از كشورش در مقابل دنيا ايستاد ، ‏او امروز صبح مُرد اما ايران در ساعت ۲۵ از حركت ايستاد.
‏اين خبر به ايران رسيد، روزنامه كيهان و اطلاعات با خط درشت نوشتند: «شاه مُرد.»‏
‏فرانسوى‌ها ضرب‌المثلى دارند كه حركت روز و شب ۲۴ ساعت است و ساعت ۲۵، ‏ساعت مرگ است.
‏به واقع ساعتِ مرگ محمد رضا شاه پهلوی ساعت ۲۵ ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19786" target="_blank">📅 09:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19785">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش صدای انفجار‌بندر عباس ، ممکنه خنثی سازی باشه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19785" target="_blank">📅 09:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19784">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19784" target="_blank">📅 02:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19783">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیغام های زیاد گزارش انفجار در‌ اهواز
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19783" target="_blank">📅 02:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19782">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=AxXYyyXKgMmv24y5nvXSny1Rsr9216Sya-cHE5THcsgWdGeJ3bF2GXHJimFtMVO6cWuhvEjgsntf5LPBp7w5cx_hKGg7Eh7MOxHUT7bqYfcahoAoCNV2TzjeibJMDOd7N-WKV3j_QHnpvFr7fQxId3OzsGJ7UgCIfBumPOMWneXf4-9_heTP508YDQbJ_5EVo0CAdzaBKQVCi0N2HSbd_TP6DDVsgGQ-cKph5ijGgD7lJC_bwGnniR7nIwWedPVOBEvx4gKavnGsipI9pvD7YSBEADc27WPRS5v-FCks77lIaq6VEdN4uquhaAIR0s246clBJzJCJRJ3JLD0sjYJwEjgH0fc5Ck8-F-bdhGmjoquBhFKMxOungYfaGME8Np9igOa6J4OlRE72_uCUxD6ZZPMVYB5rZ0ChXOJ2q_ix2a8EBIZZQHXrmkOYCJ1lWVdPNnk8wqu7DEDcBUYFD8_ILGoKXmY9D9Ku5kYEBIxatVXPcWyk4L35lnfWwwIeYlIZ4BRgKSNqA5siDMbfpid7FM6um5fEz3vwCAFUFh0hU9SG1BXMkC9DlolZnvBDp1S7p3roGqZa4Zk9rszrxivOu9MUx9rs8DVFVS0aZ6sN7UuZMwubkrAZnWzqauhOj1_kd6ZXyj17uDCo0TzKQx1Xj_IsNhaJxltGEF61P3f-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=AxXYyyXKgMmv24y5nvXSny1Rsr9216Sya-cHE5THcsgWdGeJ3bF2GXHJimFtMVO6cWuhvEjgsntf5LPBp7w5cx_hKGg7Eh7MOxHUT7bqYfcahoAoCNV2TzjeibJMDOd7N-WKV3j_QHnpvFr7fQxId3OzsGJ7UgCIfBumPOMWneXf4-9_heTP508YDQbJ_5EVo0CAdzaBKQVCi0N2HSbd_TP6DDVsgGQ-cKph5ijGgD7lJC_bwGnniR7nIwWedPVOBEvx4gKavnGsipI9pvD7YSBEADc27WPRS5v-FCks77lIaq6VEdN4uquhaAIR0s246clBJzJCJRJ3JLD0sjYJwEjgH0fc5Ck8-F-bdhGmjoquBhFKMxOungYfaGME8Np9igOa6J4OlRE72_uCUxD6ZZPMVYB5rZ0ChXOJ2q_ix2a8EBIZZQHXrmkOYCJ1lWVdPNnk8wqu7DEDcBUYFD8_ILGoKXmY9D9Ku5kYEBIxatVXPcWyk4L35lnfWwwIeYlIZ4BRgKSNqA5siDMbfpid7FM6um5fEz3vwCAFUFh0hU9SG1BXMkC9DlolZnvBDp1S7p3roGqZa4Zk9rszrxivOu9MUx9rs8DVFVS0aZ6sN7UuZMwubkrAZnWzqauhOj1_kd6ZXyj17uDCo0TzKQx1Xj_IsNhaJxltGEF61P3f-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز : در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19782" target="_blank">📅 01:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19781">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EesamDWIgRSaG4IcYHcyax8aXDFCKXLfujiyztfDhKeeZx84LdnMZvX85E1Im1Ro9jwXjYznue8NKrXoVj7RpOZY12hoLDDCK2R9_1mQl6gPM9RpVnf5DSeBv5dqL8SzMgMnqsJy1X6ecoG1DbLp5QSf1f04Aiwk0Hzo7SBHWhX1kaY3sspepSYkTpjzbjKgPUMbJAgN-wPZU4BxaNOViZvmasr_iVKWlO-0hps6gb1rI4IOn940DFoIIK-S54xDjCRMRgWUtghNES8NJ-eK4CB_W5t3qRij1PeSN9dvnXEwjbVVkA6zfgYNik2159fBpqhmhBVRQH1xPF3507MlCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری یک سایت خبری روسی مبنی بر کنترل مافیای لوازم آرایشی توسط حسن روحانی
رسانه‌های روسی در چند ساعت گذشته با انتشار خبری جنجالی از یکی از بزرگ‌ترین پرونده های قاچاق سازمان‌یافته آرایشی-بهداشتی در غرب آسیا پرده برداشتند.  طبق ادعای این سایت، حلقه اصلی این مافیا حسن روحانی؛ دیپلمات‌ سفارت فرانسه و فردی به نام مهدی‌زاده بوده‌ است.   طبق گفته این سایت اخیرا و در طول جنگ ایران و آمریکا دو کشتی محصولات قاچاق آرایشی تولید کره جنوبی، متعلق به وی توسط دستگاه های امنیتی ایران کشف شده است. این در حالی است که چند کشتی تجاری نیز در سال گذشته توسط دستگاه های امنیتی جمهوری اسلامی کشف شده که با دخالت سفارت کره جنوبی و پیگیری وزیرخارجه کره، این موضوع رها شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19781" target="_blank">📅 01:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19780">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رسانه های نظامی اوکراینی ادعا کردند: در صورت پاسخ نظامی ایران به اوکراین،ارتش اوکراین حملات پهپادی دور برد به شهر های ایران انجام خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19780" target="_blank">📅 01:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19779">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19779" target="_blank">📅 00:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19778">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جولانی: حزب‌الله به مدت 14 سال، رژیم سرکوبگر سابق را در جنگ وحشیانه‌اش علیه مردم سوریه همراهی کرد و باعث آوارگی و کشته شدن تعداد زیادی از افراد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19778" target="_blank">📅 00:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19777">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پوتین : شرق اوکراین برای ماست و غرب آن برای لهستان، مجارستان و رومانی است و به زودی به آن ها برگردانده خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19777" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19776">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فاکس نیوز:حمله گسترده به ایران هر لحظه ممکن است رخ دهد
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19776" target="_blank">📅 00:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19775">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8pymNs28eOULbYr82iyUZk1rFylpry2mfxE2HBFGbLcQto56YncieAHTpt7zkHmd3tcTtDQEb4JYgiK3wqWbBwMnDo1UaGkXmi46cDuJYE_kotPKBHm-VGPRO6-nlUmfhm5hJlSicgxf7igDh57Z3jgX0WK6JTu41qsBRYJWMJuM0oHEbeG0VMT2p4Jivp194XPX9amVp2X4SqB5pSNNL0-VyLI5koJx-dnHqPhgbIaSudhOUJBPEzUdh1pUdKLFJ1BFnxbl0icpY6DjfQWYSvKyD2FAWtXvNjC7rdsSPp1RSs04nV3q0ulj3ilSYBb1OqiGvriiv6RgcMuccc0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19775" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19774">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlOZw4YoJ_J99mrB7hPRia8qFzUEGEdTw5xE6Yq3Ks8FSD4zT5hPR7sY4O07MgF3V5SXpxZkJnRSLi-UCGPXp-USj6E-l8ywc7ujlsI_sEu9NFTlmgk3Y3gebTyy2Ast5WN4q_sk-H3tRcpPaFU7lUAhkDowchJPnca1wXAj4IWyCrtWsG5ra7E5p8YiIODG64LPBl2aEi6gfZA_Br_ub25Smt8wKFK6KN_nBzP0y3OJXSi--0Tn64Yyo5-hVfrZlYvFfI1P-0Cw7ZQgxR_d_OQVL6qwXJNLnq0Z7eN3L8lHHmjTc9_n0hB-DBXKdarLrR3Kt2mCfrjb0iUOqOzroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ موتورخانه
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19774" target="_blank">📅 00:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19773">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3anaF0PubvBNN-BK6wjiYJabAZxm30q7mOuQbPUPt_i1O_cCZ_po0c41JVxOdH_SLS9aGIghYViit9oXmy0Z2jleib0iD6uk3jY7g3HobVKmwf604RJGOltsMUXDMdP5uvmWgxqGqWtkL6sGuzJWD8S2zyKvNWm3wUkfcq5kLVAB7I4koH_LpVts1upY1KBN9kdSPT3UEMvELZSfOatAm_QJJlrm8lBYxkgrPSutmFb4rbGGKVGONvW9JDekV7DScW2unWnPLGQ7DzbNKCTBsAlsZp14lH06ldKEHN9wO93K8_aB3gyWEQHXfAiZgkIpQ8fpiysAHSEZfQgQiMksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : فرشتگان نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19773" target="_blank">📅 00:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19772">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=fplC2v2gjhbS4Aob_OSDyluRHkpMEZBhZDgzXHz9JQobIRmJaZUyoLl8voOX_-McsaNFqqRzArZLoByiMQRu3POizua_NMhcwdCAqGCZKHgFN_VMSuwEGuO2wHv5ZF6_0FkF6GRNUM1e6-HRisepbBzB3EeGBI4M2UnqP1WIznP25z5jlLSzW1VPjCppm5nK2lswA_qh8459jUfnGncL3O-2FdwJIROB09HMXqCM69VAhjAj0lCsOaoxZKRowhQnI2cPwyoKCYytfg8XP3VNLrA6ZdAIBQmeTJkQaRi1UjkoqLlSrQIfW4777dXD3X0IE8AB7JhzuHSe1kR9mJ9WJGnVEdRpkw8qMVeObPgdqVHjdsBNzgRHYijkRJLG_sAMuMmWqqMmbs6zMlHopffdUWywlvZAPEsldhrvEWTEh4dVl2r7tr5LQT8qRwAe2k3rQbxaErq_5ntYhAKROlmse4A4zAdiDG9V8F_XmXTOlBCgXPJFMF1qBvjwm-F8WSFOgchD5QhYi-pZtgFSLK1trvYS7nhgWh177pT6hDOhSp0M0etfq52OSxRKXM4Z1EADSR0bEec7MN8FOwAfNae8MJZ-m4WwbaHTskOGpu7rcEshIPtqBLpqjfHHmtQvsuzzp-LWVkA944ISi8AU62NZeP4KUuLrz4kpEj0agyN-cHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=fplC2v2gjhbS4Aob_OSDyluRHkpMEZBhZDgzXHz9JQobIRmJaZUyoLl8voOX_-McsaNFqqRzArZLoByiMQRu3POizua_NMhcwdCAqGCZKHgFN_VMSuwEGuO2wHv5ZF6_0FkF6GRNUM1e6-HRisepbBzB3EeGBI4M2UnqP1WIznP25z5jlLSzW1VPjCppm5nK2lswA_qh8459jUfnGncL3O-2FdwJIROB09HMXqCM69VAhjAj0lCsOaoxZKRowhQnI2cPwyoKCYytfg8XP3VNLrA6ZdAIBQmeTJkQaRi1UjkoqLlSrQIfW4777dXD3X0IE8AB7JhzuHSe1kR9mJ9WJGnVEdRpkw8qMVeObPgdqVHjdsBNzgRHYijkRJLG_sAMuMmWqqMmbs6zMlHopffdUWywlvZAPEsldhrvEWTEh4dVl2r7tr5LQT8qRwAe2k3rQbxaErq_5ntYhAKROlmse4A4zAdiDG9V8F_XmXTOlBCgXPJFMF1qBvjwm-F8WSFOgchD5QhYi-pZtgFSLK1trvYS7nhgWh177pT6hDOhSp0M0etfq52OSxRKXM4Z1EADSR0bEec7MN8FOwAfNae8MJZ-m4WwbaHTskOGpu7rcEshIPtqBLpqjfHHmtQvsuzzp-LWVkA944ISi8AU62NZeP4KUuLrz4kpEj0agyN-cHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش دیگری از‌مستند او قصد داشته در اوایل ماه مارس به فلوریدا سفر کند تا از دونالد ترامپ، رئیس جمهور آمریکا، بخواهد در بمباران حزب الله لبنان به اسرائیل بپیوندد.با این حال، بنیامین نتانیاهو، نخست وزیر اسرائیل، قبل از این سفر، توصیه کرد که درگیری گسترش نیابد و گفت که اسرائیل باید بر ایران متمرکز بماند و هشدار داد که حمله به حزب الله می‌تواند باعث یک جنگ منطقه‌ای گسترده‌تر شود.
نتانیاهو در این تماس تلفنی به گراهام گفت: «ما در حال حاضر بر ایران تمرکز داریم.» گراهام موافقت کرد و پاسخ داد: «این واقعاً توصیه خوبی است.»
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19772" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19771">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=vJc2KFjaRzJ3PH4NQI8kTgz9oq1yWzcy3QZ8HmxH7xvkfdN0d1aqEApkP55n_2z5XFefubq7jt-jcMjS6aLgToznzPQFBVJo5M6KCefYBBLTj7kddHWIUp16_PORYN-HFXRS6UKrl5mUWY0gmfpJcF9SCxvf1Ewh0J__K57OawDh8uNp-UoIO9j8gCxMIuSq-IOhlwBCzqoLQOceWFbFO8l-h05UGdP1LUJqzkdj6cNXiErUH1N3VSL5dd9XM8oMcgorW8XGSS1ctDNLyzZr5vo7oyuW0FcJ0QpxuSrBYZ-dHY36hpAfYIETZDFMSXjSTb8etGfdnS37Yq4o_pkPfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=vJc2KFjaRzJ3PH4NQI8kTgz9oq1yWzcy3QZ8HmxH7xvkfdN0d1aqEApkP55n_2z5XFefubq7jt-jcMjS6aLgToznzPQFBVJo5M6KCefYBBLTj7kddHWIUp16_PORYN-HFXRS6UKrl5mUWY0gmfpJcF9SCxvf1Ewh0J__K57OawDh8uNp-UoIO9j8gCxMIuSq-IOhlwBCzqoLQOceWFbFO8l-h05UGdP1LUJqzkdj6cNXiErUH1N3VSL5dd9XM8oMcgorW8XGSS1ctDNLyzZr5vo7oyuW0FcJ0QpxuSrBYZ-dHY36hpAfYIETZDFMSXjSTb8etGfdnS37Yq4o_pkPfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر مستند منتشر نشده نشان می‌دهد که سناتور فقید لیندسی گراهام در اوایل ماه مارس پیش‌بینی کرده بود که دولت ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «حرکتی تقریباً برگشت‌ناپذیر» ایجاد خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19771" target="_blank">📅 23:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19770">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وال استریت ژورنال
: ارتش آمریکا یک طرح نظامی تمام عیار برای مدت 2 هفته جنگ همه جانبه با ایران آماده کرده است که هر لحظه پس از دستور ترامپ آغاز خواهد شد.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19770" target="_blank">📅 23:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19769">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کامنت جدید زیر پست بی بی  : فقط همین کامنت رو لایک کنید و کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DbRKUnvs_mq/?comment_id=18097108343207051
ترجمه : بی‌بی، مردم ایران بسیار دلتنگ شما هستند. لطفاً به هر روشی که صلاح می‌دانید، این بار پس از وحیدی، کاری کنید که روحانیون تندرو نیز یکی‌یکی از این دنیا بروند و ریشه کن شوند . هدف قرار دادن زیرساخت‌ها و سربازان وظیفهٔ عادی، که خودشان نیز قربانی این حکومت هستند، فقط رنج و درد مردم ایران را بیشتر می‌کند.
ما شما را بسیار دوست داریم و از همه تلاش‌ها و زحمات شما صمیمانه سپاسگزاریم.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19769" target="_blank">📅 23:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19768">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کامنت جدید زیر پست ترامپ : فقط همین کامنت رو لایک کنید و کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DbRJwPPBPaP/?comment_id=18108319289002859
ترجمه : لطفاً به‌جای هدف قرار دادن زیرساخت‌ها، که تخریب آن‌ها تنها موجب رنج و سختی بیشتر مردم عادی می‌شود، و همچنین به‌جای سربازان وظیفه که بسیاری از آن‌ها خود قربانی این شرایط هستند، تمرکز خود را بر سران حکومت، به‌ویژه رهبران مذهبی تندرو، قرار دهید.
از تلاش‌های خستگی‌ناپذیر و شبانه‌روزی شما صمیمانه سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19768" target="_blank">📅 23:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19767">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyDKjDADlN0bIkSxWv7fpIYECwfs0pxUZakz6cMaSzbA56QwzivUugonaRPsAzqvlyNFM4-rFct0cjw1bFxC-yNvgFy9xPFSLJq5teXEbzX82ZRa6sJQKb7OUvYDX5aoSYKK3xENCrXhkCcNJZLalLQtnS-AjPh1UhobMSffLdEc9WiB9dXR65veB0svbkSAwhUVbZiYJ0BZzhGq2uaYUwj39d3ZF_AOJK3XVVvZRDXF1QSd_K3ZGA21Un1Biff7iQP_A8evCpr82YRizFH9FaiSXxgTKN_Kd172nfjSOJsCSfk27XOGUuC4f9aZcUDGfQEM7ZKe2m22PgRjyq266w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : الان دیگه نفتکش ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19767" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19766">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZxIwLlhgIok6UwtJp2DkLV4Ao-BLfN3zOrJXHjq_v0iy5yN-tRkdjNhMeJ2cR8K_kH5Qh5Hl5O8EApKy4EmPkO_aGCF3HubscbZhXGz44Vr03X9AFfSb1G4AhME3plowWChmcByrclRL-qeMH4V2eQU0RLS99QWBqwUP6MiMkOHDsqgZvtNyfzxe_-xhKgil8hAfpJY8_r6IhUvaAK5gUq4r8iHnP-_bnFFDPVrp1dTXrOUW2KwSEaAGCo1zme1zv_WF6hprAdclgDAYj10cJpokWndTZpKpmkbjOiChtcdnoHMHnK3SYWo5w_6RaIARDZetXmy5mVI2ROdcHwtNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حمله هوایی به جزیره خارک
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19766" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
