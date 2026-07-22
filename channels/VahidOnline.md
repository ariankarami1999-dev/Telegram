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
<img src="https://cdn1.telesco.pe/file/Dkp-yKMwuJ8dwfr2UK8Fp01w7uWbSnAzgswrsmm6Rx_F1UdWDoTIkowaheiKIUkD9hGQHSAiWIpLpNHLhlod2s_M767iWatK3Jyl21tOnNX2amKzYDnGESn--e0JMFdYZJDgfFwQ1dGmiMlI9tPnkK9WUtGXyN8Z3GXjofpRxiH-sTxM7g5in-swYuhLN4xBoU9QrUubmfGbYuqbOE7u58-c_oi6fUIXtUtPxrNKTWlPkU7lnNxwLN2TfO14Nmj2BflUlxEz3vp9WVKsDqOcQiRRuDLcYIfn-vhlVowmRMDZNCmyqH_QTTn-qZENowkj5vfJlMQHBy03LzuSJcbCDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 15:40:06</div>
<hr>

<div class="tg-post" id="msg-77392">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">معاون استاندار همدان اعلام کرد در ادامه حملات آمریکا، ساعتی پیش نقاطی در شهرستان کبودرآهنگ هدف حمله هوایی قرار گرفت.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
پیام ساعت ۳:۵۹
آقا پادگان نوژه همدان شخم زدن
پیام ساعت ۴:۰۸
سلام پایگاه نوژه همدان صدا انفجار پی در پی اومد
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد آمریکا ساعت ۰۲:۵۵ بامداد چهارشنبه ۳۱ تیرماه یک نقطه در خارج از محدوده شهری بانه در استان کردستان را هدف حمله قرار داد.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
وحید بانه رو زدن
صدای انفجار همین الان اومد
بیرون شهره نمیدونم کجاست
بانه صدای جنگنده اومد
بعد صدای انفجار ازدور  میاد
همین الان‌۲:۵۸ دقیقه
برای سومین شب متوالی
گردنه خان بانه رو زدن
همون تایم
پیام قبلی ایشون (شب قبلش):
رادار گردنه خان بانه رو زدن
ساعت 2.20 نصف شب
چوار، آبدانان، انارک و دینارکوه در استان ایلام نیز هدف حمله قرار گرفتند.
فرماندار آبدانان گفت این حمله‌ها هیچ تلفات جانی نداشته است، اما حمله هوایی به منطقه انارک در چوار باعث آتش‌سوزی در زمین‌های منابع طبیعی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77392" target="_blank">📅 05:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پیام‌های دریافتی:
من تهرانم دوباره صدای پدافند داره میاد
پدافند مشیریه
دوباره پدافند داره کار میکند شرق تهران
صدای پدافند شدید افسریه
فعال شدن مجدد پدافند همین الان خ پیروزی
فعالیت پدافند شرق تهران. ۴:۵۱.
ساعت 4:52 دقیقه فعالیت پدافند شرق تهران
جنوب تهران پدافند 4:51
وحید من منطقه ۱۵ ناحیه ۴ تهران هستم محله مشیریه ۶ انفجار اومد پدافند به شدت فعاله ساعت ۴ و ۵۰ دقیقه
[صدای انفجار لزوما به معنای برخورد نیست. توپ‌های ضدهوایی هم با صدای انفجار شلیک می‌کنند.]
🔄
سلام وحید جان منطقه ۱۵ تهران همین الان ساعت ۰۵/۱۵ پدافند مشغوله
ساعت 5:15 دوباره صدای پدافند در مشیریه
سلام باز مشیریه همین الان صدا اومد
😂
😐
سلام الان ساعت ۵:۱۴ دقیقه صدای توپ های ضد هوایی و پدافند از جنوب شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77391" target="_blank">📅 04:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=Az6mK8ED3k1_sCvO-PQOFz3LG14yNeeeG1ClfEoQmwpFsuwuEucJR_uKB3V4MnnFGOwaZM2jwhv0oCUsotNEuom1gRXux6TI4lcv63FQQmbPaj3uvOrodFUunFi3-6QJxx1vP2ROi4RApIZGuB3BUP287vON4Dp9NBjjHG-FY6Uj6adBnuylSw5GmZFGGXv2UzRGnr4B9zaZglAgsHvTQYXarH61rS2l8wANgqVayxv7GC6o7hCX-iwvd0XFJArLt4suK3nyfCZM3vuTrHfjIDd2fEIPHkMkYyIUs16Q1bzXvyuiEZtkQULUzjyZ3UdODpKH85EFqPwdoRYChpAzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=Az6mK8ED3k1_sCvO-PQOFz3LG14yNeeeG1ClfEoQmwpFsuwuEucJR_uKB3V4MnnFGOwaZM2jwhv0oCUsotNEuom1gRXux6TI4lcv63FQQmbPaj3uvOrodFUunFi3-6QJxx1vP2ROi4RApIZGuB3BUP287vON4Dp9NBjjHG-FY6Uj6adBnuylSw5GmZFGGXv2UzRGnr4B9zaZglAgsHvTQYXarH61rS2l8wANgqVayxv7GC6o7hCX-iwvd0XFJArLt4suK3nyfCZM3vuTrHfjIDd2fEIPHkMkYyIUs16Q1bzXvyuiEZtkQULUzjyZ3UdODpKH85EFqPwdoRYChpAzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا یازدهمین شب حملات علیه ایران را به پایان رساندند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۸:۱۵ شب ۲۱ ژوئیه به وقت شرق آمریکا [۳:۴۵ به وقت تهران]، یازدهمین شب متوالی حملات علیه ایران را با موفقیت به پایان رساند.
تجهیزات و نیروهای سنتکام مراکز عملیات نظامی ایران، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز بیش از پیش تضعیف شود.
ایران طی سه ماه گذشته به بیش از ۳۰ کشتی تجاری در حال عبور از این آبراه بین‌المللی که برای تجارت منطقه‌ای و جهانی حیاتی است، حمله کرده است. این حملات بی‌دلیل، صدها دریانورد بی‌گناه را به خطر انداخته و آزادی کشتیرانی را تضعیف کرده‌اند.
با وجود اقدامات تجاوزکارانه ایران، تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. از اوایل ماه مه تاکنون، نیروهای سنتکام به تسهیل عبور حدود ۹۰۰ کشتی تجاری و ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77390" target="_blank">📅 04:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=uNEBbmIpM035aca4yDmsY0vgCuM3mgwyXMT3tzFY52yxyj-xTw7EzbVqu6EnEUGzDs-TkhlKYDLxVBVxx32oQhy6FSmXQMHuSuivIt8axjuKYlcj9HnJtHvy1hsKkw1ncNmBGwSS7LF1nBNk4tHW3lDqJGmCvg8RddDABCKA5SqLXtevX3fDE0gYblkfmG_lgocLGa08DXUAh0C5RXv8X47OBTweH__AElCCPfg-a1-LQ_C6Q3CArz8sZG4n_4OW8Bgq5bb1NeMk3lpoH732YMJ2sTTVLSCoULpSInBZ1ds2mjYi3F4FiuUOQfr80hjSWAhfsiLAwTn_bFI49a_Dtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=uNEBbmIpM035aca4yDmsY0vgCuM3mgwyXMT3tzFY52yxyj-xTw7EzbVqu6EnEUGzDs-TkhlKYDLxVBVxx32oQhy6FSmXQMHuSuivIt8axjuKYlcj9HnJtHvy1hsKkw1ncNmBGwSS7LF1nBNk4tHW3lDqJGmCvg8RddDABCKA5SqLXtevX3fDE0gYblkfmG_lgocLGa08DXUAh0C5RXv8X47OBTweH__AElCCPfg-a1-LQ_C6Q3CArz8sZG4n_4OW8Bgq5bb1NeMk3lpoH732YMJ2sTTVLSCoULpSInBZ1ds2mjYi3F4FiuUOQfr80hjSWAhfsiLAwTn_bFI49a_Dtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی با شرح شعله‌های انفجارهای حمله به 'پادگان بخردیان در بهبهان خوزستان'
چهارشنبه ۳۱ تیر، حدود ساعت ۲:۳۰، هم‌زمان با آغاز اعلام حملات از سوی آمریکا
Vahid
📍
میگن
اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77386" target="_blank">📅 04:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیام‌های دریافتی:
سلام اصفهان صدای پدافند اومد
پدافند اصفهان فعال شد . سمت بهارستان و صفه
اصفهان صدای انفجار اومد الان چندتا پشت هم ولی از خیلی دور
ساعت ۴ صبح صدای پدافند جنوب شهر اصفهان
جنوب اصفهان شهر موشکی رو به روی بهارستان پدافند فعال شد ساعت 4:5
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77385" target="_blank">📅 04:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=rSHuRQNHqS9BdYm8I0Zv3bPVeI6BE-9bMr_aDeYPFQiBR9BrkQNL93_Kfyjst5lB5wBpY7uMW0LsiTQZQ_V-y2mdZB9yanyB0Ds0KSjHch7a3wSYH6d0-EAMCqLOc0CBqJQIe1my-gFlwpCvdiSSLttLH8DqixbbVMM-IPbxbzjA8u6QvQJwPNjh-Na-dF9OArjJcldJVLyPjEkx8v6Sn7-WIVSOvPUTmwE5FHeA_NLOt838f4bWgKD4lXpzR4cht51JssfT-jSUPfC4DJ-0Hdct9zjjtRzv3yhtO-JXyiW5MOVQ7QSlPQgNWo8faL2V3fPc7_Bs1JZYtSj3a90U5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=rSHuRQNHqS9BdYm8I0Zv3bPVeI6BE-9bMr_aDeYPFQiBR9BrkQNL93_Kfyjst5lB5wBpY7uMW0LsiTQZQ_V-y2mdZB9yanyB0Ds0KSjHch7a3wSYH6d0-EAMCqLOc0CBqJQIe1my-gFlwpCvdiSSLttLH8DqixbbVMM-IPbxbzjA8u6QvQJwPNjh-Na-dF9OArjJcldJVLyPjEkx8v6Sn7-WIVSOvPUTmwE5FHeA_NLOt838f4bWgKD4lXpzR4cht51JssfT-jSUPfC4DJ-0Hdct9zjjtRzv3yhtO-JXyiW5MOVQ7QSlPQgNWo8faL2V3fPc7_Bs1JZYtSj3a90U5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی ۳:۱۰
دوباره پدافند شمال شرق تهران فعال شد. شدیدتر از دفعه قبل
شرق تهران صدا پدافند
+ ده‌ها پیام مشابه از شهروندانی که همین صداها رو در محله‌های مختلف شرق و شمال شرق تهران شنیده‌اند.
🔄
ساعت ۳:۲۶:
ده‌ها پیام رگباری دیگر درباره صدای فعالیت پدافند
من حتی نمی‌رسم بازشون کنم فقط از پیش‌نمایش دارم آخرین پیام هر کسی رو می‌بینم باز هم کلی عقبم.
پیام‌ها رسیده به مرکز شهر و حتی مناطقی در غرب تهران
گرچه همیشه هستند کسانی که هر صدایی رو به برخورد تعبیر کنند ولی از حجم پیام‌ها واضحه که صدای پدافند شنیده میشه در مناطق مختلف تهران
آپدیت ساعت ۳:۴۰:
تا الان به طور پیوسته در هر ثانیه کلی پیام میومد. الان داره به حدود یک پیام در ثانیه کاهش پیدا می‌کنه.
همچنان درباره صدای پدافند در همه مناطق تهران
آپدیت ۳:۵۰:
سکوت نسبی برقرار شد. میزان نوتیفیکیشن‌ها هم به حالت معمول برگشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77384" target="_blank">📅 03:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77383">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای سنتکام امروز ساعت ۷ عصر به وقت شرق آمریکا [۲:۳۰ به وقت تهران]، برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند. این حملات با هدف ادامه تضعیف توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77383" target="_blank">📅 03:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فعالیت پدافند در شرق شهر و استان تهران:
پردیس صدای انفجار و پدافند
همین الان شرق تهران
پدافندداره روی شهرک خمینی اتوبان بابایی کار میکنه، فعلا انفجار بزرگی نشنیدم، ممکنه هدف خجیر یا پارچین باشه
صدا پدافند زیاد میاد
ما سمت پردیس هستیم
سلام پردیس صدای انفجار از راه دور اومد
ساعت ۲:۵۰
سلام وحید جان از پردیس چندین انفجار شنیدیم الان
وحید صدای انفجار و پدافند شرق تهران همین الان
سلام تهران حکیمیه ۲:۵۳ دقیقه صدای پدافند میاد
سلام وحید جان همین الان  ساعت ۲:۵۰پدافند پارچین فعاله از پردیس مشخصه
صدای هواپیما میاد
همین دو سه دقه پیش
بشدت پدافندا فعالیت داشتن
پنج شیشتا صدای انفجار اومد
چندبار صدای پدافند سمت شرق ته
ران ۰۲:۵۰
پردیس صدای پدافند و انفجار اومد
شهرستان پردیس فاز ۱۱ از استان تهران صدای مکرر پدافند.  ساعت ۲:۵۵ صبح
شرق تهران(لواسان) صدای پافند ۲:۵۲
پردیس شرق تهران، چهار پنج تا صدا شبیه انفجار واضح ، ولی با فاصله شنیدیم ، حدود ساعت ۲:۵۳ صبح
سلام وحید جان  ساعت ۲.۵۰ دقیقه صدای حداقل ۱۰ انفجار از خجیر  که از حکیمیه شنیدیم
درود وحید جان ساعت ۲:۲۰ دقیقه ما پردیسیم
یه صدایی اومد گفتن سایت هسته ای پارچین زدن
پدافند شرق تهران فعاله
ما پردیسیم
اطراف (احتمالا پارچین)صدای انفجار و پدافند
[+ ده‌ها پیام مشابه دیگر از مناطق مختلف شرق و شمال شرق تهران که دیگه نقل نمی‌کنم و ازشون عبور می‌کنم چون تازه رسیدم به پیام‌های ۱۰ دقیقه پیش و از پیام‌های تازه‌تر بی‌خبرم.
هم‌زمان دارم همه پست‌های قبلی مربوط به شهرهای دیگر رو هم آپدیت می‌کنم با پیام‌های تازه‌تر]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77382" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77381">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر انفجار
همین الان بوشهر صدای انفجار
بوشهر یکی سنگین
۰۲:۴۸ بوشهر صدای انفجار اومد
سلام خسته نباشید بندر گناوم چند بار موج انفجار اومد ولی نمیدونیم کجاست
بوشهر صدا و انفجار خیلی مهیب اومد
بوشهر صدا اومد ۲:۴۸ ریشهر
بوشهر صدای دو انفجار ساعت 2:48
بوشهر  انفجار فوق فوق سنگین ۲:۴۸
وحید الان ۲:۴۷ بوشهر زد زمین لرزید
وحید جان همین الان بوشهر عاشوری صدای وحشتناک بمب اومد تمام خونه لرزید
همین الان بوشهر دو انفجار بزرگ
بوشهر الآن صدای انفجار اومد، ساعت ۲:۴۷
ساعت ۲:۴۸ بوشهر صدای انفجار اومد!
انفجار وحشتناک بوشهر ۰۲:۴۸
خود شهر بوشهر صدای انفجار
۲:۴۷ بوشهر، یه انفجار خیلی وحشتناک و مهیب
سلام وحید جان همین الان بوشهر صدای انفجار ناحیه پایگاه هوایی و دریایی
سلام بوشهر ساعت دو و چهل و هشت دقیقه تک انفجار
بوشهر 2:48 یک انفجار مهیب محدوده بهمنی
ساعت ۲:۴۸ دقیقه بوشهر رو زدن صداش خیلی بلند بود
سلام آقا وحید، بوشهر ۲:۴۹ یه صدایی اومد و در های خونه کمی لرزید
بوشهرو الان ۲:۴۸‌‌بد زدن پایگاه هوایی
سلام بوشهر ساعت ۲:۴۸ دقیقه انفجار شدید
من یه سر شهرم.. دوستم یه سر دیگه شهر
جفت خونه هامون لرزید
بوشهر - چهارمین انفجار «مهیب» در ۲:۵۳
برازجان (استان بوشهر) تک صدای بلند و لرزش زمین. 2:54
وحید صدای انفجار شبیه شلیک موشک برازجان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77381" target="_blank">📅 02:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=UenKQuRa9PK3EVVtG6TylZWDwGoSIDo2jLIpDazrkGwDboWBRSIseG25npcNdiOiZoDBar5s5w-HLC45b2-6AxQumiUcXKF2GHojFo_DCOUwFIeT_6XHqGHnCSOXP0vzuh0XsHvwZbc9cYgk7QmfxdbpZULyIqH5YMIwpAZLsw7Hp0GZtcGGXSKZVj8zxA80juVLh35-4hzWqJfi8uUpsB4N_4-1uPNIudCQ1qUV0JmpMCYy_2Un91eeztOQwxpdoAQ1CRx42_lgw4-dcTNMoXDi9AtP1pSFCQdo_8lU5Id8bQavFWHXUVj2q-fN8aIJy58Hmk5lKLYMk3az0vHPBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=UenKQuRa9PK3EVVtG6TylZWDwGoSIDo2jLIpDazrkGwDboWBRSIseG25npcNdiOiZoDBar5s5w-HLC45b2-6AxQumiUcXKF2GHojFo_DCOUwFIeT_6XHqGHnCSOXP0vzuh0XsHvwZbc9cYgk7QmfxdbpZULyIqH5YMIwpAZLsw7Hp0GZtcGGXSKZVj8zxA80juVLh35-4hzWqJfi8uUpsB4N_4-1uPNIudCQ1qUV0JmpMCYy_2Un91eeztOQwxpdoAQ1CRx42_lgw4-dcTNMoXDi9AtP1pSFCQdo_8lU5Id8bQavFWHXUVj2q-fN8aIJy58Hmk5lKLYMk3az0vHPBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
تبریز ۶/۷ تا همین الان  زدن شدید
همین الان شیش تا صدای انفجار تبریز اومد
پشت سر هم
۲:۴۲ از تبریز ۴تا صدای بلند انفجار یا پرتاب موشک اومد
سلام همین الان ۸ تا انفجار تبریز
سلام 5 انفجار شدید تبریز
سلام ساعت ۲:۴۲ بمب باران تبریز بیشتر از ۱۰ تا
۷ انفجار تبریز ۲:۴۰
از تبریز فک کنم موشک زدن
صدای انفجار از تبریز ۲:۴۲
وحید جان انفجارهای خیلی شدید اطراف تبریز ۲:۴۲ دقیقه
همین الان تبریز ۶ ۷ انفجار شدید
ساعت ۰۲:۴۲
ساعت ۲.۴۰ دقیقه تبریز رو زدن،حداقل چهار پنج تا صدای انفجار اومد
تبریز صدای ۵ انفجار توسط جنگنده بود
سلام تبریز ۴.۵ تا زدن
سلام همین الان صدای ۶انفجار سهند تبریز
ساعت ۲.۴۲
۷ تا انفجار شدید تبریز
همین الان2:43 دقیقه
پنج تا بیشتر زد تبریز رو و مشخصه سنگین بود و عجیب به مرکز شهر نزدیک
صدای انفجار از تبریز
۳ یا ۴ تا با فاصله خیلی کم
سلام وحید جان تبریز 2.43 شش هفت تا انجار وحشتناک بلند خونه لرزید و از خواب بلندم کرد
وحید تبریز ۸ تا صدای انفجار اومده
شدید و مهیب
تبریز موشک نبود. رادار رو زدن
سلام همین الان ۲:۴۲ بامداد ۶ بار سنگین زدن تبریز رو احتمالا سایت موشکی باشه
🔄
وحید دوباره تبریزو زدن
تبریز دوباره دو تا شنیدم اما دور بود صداش ضعیف میومد
دوتا انفجار دیگه تبریز ولی دورتر بود
تبریز دو تا صدا اومد
ادامه انفجارها در
#تبریز
سلام. الان تبریز پدافند کار کرد.
بازم تبریز رو زد، ۵ انفجار، شدتش کمتر از قبل بود ولی؛ ساعت ۰۳:۰۴
۵ انفجار یا بیشتر تبریز ۳:۰۴، یا شاید فعالیت پدافند ،(غرب تبریز)
تبریز بازم داره می‌زنه ساعت ۳:۰۴
۵ تا انفجار پشت سر هم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77380" target="_blank">📅 02:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
چند تا صدای انفجار چابهار شنیده شد بنظر کنارک بود
چابهار صدا اومد.
سلام وحید جان چابهار صدا جنگنده و بمب اومد چند تا هم اومد از 2/5 شروع کرده
صدای انفجار در چابهار
چابهار همین الان چهارتا زد ساعت ۲:۳۸
چندددیقه قبلشم یکی زد
چابهار وحشتناک. داره میزنه
۷ انفجار رگباری پشت سر هم
ساعت 2:30 چهارشنبه چابهار یه صدای انفجار سنگین شنیده شد
الان دو سری 4، 5 تایی پشت هم زد
چابهار همین الآن صدای چند انفجار پشت سر هم
خود چابهار نبود
صداها دور بود
ولی تعدادش زیاد بود</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/77379" target="_blank">📅 02:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بندرعباس الان سه تا پشت هم زیادد زدن
بندرعباس پشت سر هم داره میزنه
بندرعباس سلام صدای چندتا انفجار ساعت ۲:۲۷.
سلام وحید جان بندرعباس صدای 3 انفجار
سلام وحید جان همین الان  بندرعباس صدایی وحشتناک از سمت اسکله باهنر اومد ۲تا صدای وحشتناک
وحید جان دوتا انفجار پشت سرهم بندرعباس 2:38 دقیقه، دور بود
بندرعباس ۲:۳۸ چند صدای انفجار شنیدم
سلام صدای انفجار بندرعباس سه تا پشت سرهم همین الان
بندرعباس ۲:۳۷
سه انفجار
بندرعباس ۳ تا انفجار پشت هم الان
سلام آقا وحید ساعت ۲:۳۷ دقیقه بندرعباس صدای ۳ تا انفجار اومد که اولی از همه بلندتر بود
سلام بندرعباس الان صدای ۳تا انفجار شدید ۲:۳۷
سلام بندرعباس 2:37 حدودا ۴ تا صدای انفجار اومد
بندر عباس صدای ۳ انفجار ۲:۳۹
بندرعباس صدای انفجار اومد الان
میگن سمت اسکله باهنر زدن</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77378" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سلام صدای انفجار یا پرتاب موشک از کنگاور
سلام ۲ و ۳۵ صدای انفجار و لرزش کنگاور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/77377" target="_blank">📅 02:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ماهشهر دو صدای انفجار از دور
همین الان یک انفجار دیگه
سه چهارتا انفجار ماهشهر همین الاننن
ماهشهر ۴تا موج از دور ولی حس شد
بندر ماهشهر ۴ انفجار
سه چهارتا انفجار ماهشهر همین الاننن
سلام ماهشهر الان ۳ انفجار
وحید خسته نباشی بندرماهشهر الان چند انفجار اومد
سلام صداها مثل ویبره هستن انگاردورازماهشهره به فاصله 2ذقیفه
ماهشهر صدای انفجار ساعت ۲:۳۱
🔄
اقا وحید ماهشهر دوتا دیگه زد همین الان 2.48 دقه
باز ماهشهر دوتا زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77376" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77375">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پیام‌های دریافتی:
سلام خسته نباشید همین الان بهبهان رو زدن
چهار بار زدن
خیلی بد زدن
خونه ها خیلی لرزیدن
وحید
بهبهان رو زدن
۴ انفجار محکم
بهبهانو چنان داره میزنه که هبچ وقت اینجوری نزده بودددد
انفجارها انقدر قوین که تا حالا همچین چیزی ندیده بودمممم
بهبهان ۳ یا ۴ تا صدا انفجار خیلی شدید
پشت سر هم
۲:۳۲ دقیقه
خیلی شدیده
🔄
سلام بهبهان همین الان ۲ و ۳۰ بامداد ۴ انفجار بسیار سنگین
شد چهار بار دوباره اومد
بازم زد
بهبهان 4 موج انفجار 2:30
4موج انفجار نزدیک تر 2:34
۷ بار زدن بهبهان رو
سلام منصوریه بهبهان هستیم
همینجور صدای انفجار میاد پشت هم
سلام توی همین ۴ دقیقه ۸ انفجار داشتیم
همینطوری داره صدا میاد
درود وحید جان ۷ تا انفجار پیاپی و سنگین بهبهان احتمالا سمت پادگان بخردیان
دود از سمت پالایشگاه بیدبلند میاد نمیدونم کجا رو زدن
حاجی ۱۰بار زدن در خدی که زمین لرزید
بهبهان وحشتناک دارن میزنن
سلام ، تا اینجا حدود ۹ صدای انفجار اومده بهبهان
از ۲:۳۲ تا ۲:۳۵
بهبهان ۲:۳۵
صدای ۶ انفجار
همین الان بههبهان زدن صداش خیلی بلند از استرس تو کوچه ایم
سلام سپاه روبروی بیدبلند بهبهان رو حدود هفت بار زد
سلام صدای های مهیب موشک در آسمان بهبهان
شایدم انفجار
بهبهان درب خونه ها از موج انفجار چند بار لرزی از خواب بیدار شدیم وحشتناک
🔄
پیام‌های حدود ساعت ۲:۵۰
بهبهان بازم صدا انفجار
قطع نمیشه
خیلی شدیده
حاجی هنوز صدای انفجار میاد
بهبهان بازم صدای انفجار میاد
۴ تا پشت هم
بهبهان دوباره داره صدا مياد، 4 بار
دوباره دارن میزنن
بهبهان دوباره زد
۴ تا انفجار
۴ بار دیگه الان بهبهان رو زدن آقا وحید
۳ انفجار بزرگ دیگه همین الان
داداش وحید سه موج بخردیان بهبهان رو زدن
۲:۳۰
۲:۳۵
۲:۵۰
همین الان بهبهان،جدای از اون ۸ تا الان ۳ تا دیگه شدیییید زد
ساعت ۲:۵۰
بهبهان دوباره دوتا انفجار شدید
ساعت ۰۲:۴۹..دوباره ۳ انفجار شدید دیگه بهبهان.
سلام رگباری دارن بهبهان رو میزنن
بهبهان تا الان 11 تا انفجار شده وحید
وحید جان از ساعت ۲:۳۲ تا ۲:۴۷ دقیقه صدای ۱۰ انفجار داخل بهبهان اومد
سلام وحید 2و50دیقه دوباره 2انفجار  بهبهان زدن انفجار خیلی مهیبه
باز هم همونجا رو حدود چهار بار دیگه زد بیست کیلومتری شهر هستش
بهبهان پونزده بار تا حالا زدن همین الان صدا ۵ انفجار دیگه اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77375" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">در بخشی از نارمک تهران صدایی شنیده شده که معلوم نیست مربوط به چی بوده.
پیام‌های دریافتی خیلی کم:
سلام شرق نارمک صدای خیلی بلند مثل انفجار
من سمت نارمکم الان یه صدایی شبیه به انفجار پهپاد شنیدم
شرق تهران نارمک شیشه ها لرزید و صدای انفجار
تهران الان صدا اومد فکر کنم زدن
ساعت 02:01
سمت نارمک ساعت ۲بامداد صدای انفجار اومد
سمت نارمک صدایی شبیه به انفجار  بود ساعت ۲:۰۰
ما هم شنیدیم ولی انفجار نبود یه صدایی مثل زمانی که پدافند می زدن
🔄
پیام‌های تازه:
انفجار گاز بوده
سلام انفجار گاز بوده میدان ۹۵
انفجار نشنیدم اما ده دقیقه پیش صدای آتش‌نشانی اومد تعداد زیاد
نزدیک نارمکیم، گلبرگ
نارمک میدان ۹۵ کوچه مهدی
ظاهرا ترکیدگی گازه
کسی صدمه ندیده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77374" target="_blank">📅 02:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi_00YA6S9tlvJyiM8PedtHllxQqDhEqS5oi6byw1DkExEzNs_FV2xPz3vOBt9Nsv66aC5r9eMltDKtwFgU9nv9JqBfFb71EriIAs8iG7smxGTpX_lgA5Na2lqQgn9i96aGRx_ApL6YnenL0h758XLvlL4VVclwVIzR2xo5OS0C56rbvzqQzMg4tfclEUXraHh-9veTcKqp3pjF-7judzeT8RwR_ap7H_3Q3ep6a9L6GXPfU3tufOe7y-jMJ2BZtCEts4PZ5ooYyukGFqrgZPrwmwG42Ubl32duyhBe9KovVamJ7m3I1RPg1oGN16NuUSMdqi1jV6qY5CiaUpJlAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد کل ارتش کویت، بامداد چهارشنبه، با صدور بیانیه‌ای اعلام کرد که پدافند هوایی این کشور در حال حاضر در حال مقابله با حملات پهپادهای متخاصم در پی «تجاوز گستاخانه ایران» است و تصریح کرد صدای انفجارهای شنیده‌شده ناشی از رهگیری این اهداف توسط سامانه‌های دفاع جوی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77373" target="_blank">📅 01:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">منابع حکومتی:
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): تعرض به مراکز هسته‌ای ایران، پاسخ گسترده نیروهای مسلح را درپی دارد
🔹
آمریکای جنایتکار مراکز هسته ای و حساس ایران اسلامی را تهدید به حمله نموده است. اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله ای بشود، آن را به‌عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77372" target="_blank">📅 00:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oe0xrVz7hNYs-aG69v2kVU2BzkT8F8MXji5ppSGXTdGhNnAn5d27SHemmCqjM6i71f8-RAkLv5GuQzAILWBk_d7UABSPldmLOxu-7ql1XZiCIYj47DCIM_k6swEkl5XvhhmDXpWdXLUH-rnjouVfnnSo5hPpB-I_P94QHpQpLOzWV6NTWiW2tsaLJfXOGtuxM-FaT4-Nmi7SKIyMsmQ88RIWU2C36xVYY0CuUDauKOrPj6PWPpPyqpYRj8SqQ3t841ZR0QSQ4ap9O_4KuDoT0VlmX903k0o5fJ60QFCCewrmd2g-pkZ1BU6n9Nog4UPP__qwJCzBHBU7h3wkaOx5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع ایالات متحده می‌گوید جنگ با ایران تاکنون ۳۷ میلیارد و پانصد میلیون دلار هزینه داشته است.
پیت هگست این موضوع را خطاب به اعضای کنگره اعلام کرد؛ آماری که از افزایش نزدیک به ۸ میلیارد دلاری هزینۀ جنگ، نسبت به ارقام قبلی که دو ماه پیش اعلام شده بود، حکایت دارد.
وزیر دفاع آمریکا البته تأکید کرد که این رقم تازه، هزینه‌های پیش‌بینی‌شده تا پایان سال مالی جاری، یعنی ۳۰ سپتامبر مطابق با ۸ مهرماه ۱۴۰۵ را هم شامل می‌شود.
از زمان آغاز مجدد درگیری‌ها بین ایران و آمریکا، این نخستین بار است که پیت هگست وزیر دفاع ایالات متحده به همراه ژنرال دن کِین رئیس ستاد مشترک نیروهای مسلح این کشور، با حضور در کمیتۀ تخصصی کنگره، ویژۀ تخصیص بودجه، به سوالات اعضا پاسخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77371" target="_blank">📅 00:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V_sdU3OLV4PXEsunX8SyK9VrLXZabsYmZEF_dZcrTtOQGFk9Oue7MatybaVyFPhpM6881i7muwZZC41TWiTxKyF4uEQvw93VOsCP5rf7MA2bEU4YOwlnv8Kf5RGCLl339ON3v4Vd3AQAbI_xYq49sZTFt4tbRM9O9ot0PkfF4rkM9Wqc1hR7SMCZGsyB2lmEoy5t7Cie0Sbd0OXrmy2Kip-dY-K1DuRBRtytyFkVkv5WBCjnhAKm5h1hOaZELqaleah5ZBaBhyiFfeqhIEITWC1gSJn4z-jzUMPCacwpUphipFE1EvpJR2Usx7LvUbvx6kOUDfWov7qt322iOdkSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
جنگ افغانستان: 20 سال، 2,000 کشته.
جنگ عراق: 9 سال، 4,600 کشته.
جنگ ویتنام: 19 سال و 5 ماه، 58,220 کشته.
جنگ کره: 3 سال و 1 ماه، 36,574 کشته.
جنگ ونزوئلا: 1 روز، بدون کشته.
درگیری نظامی با ایران: 4 ماه، 18 کشته.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77370" target="_blank">📅 23:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=qTI1C9x5T7LsvMxiE3uHKRingdOsn3xSbcmpIgvSwMPeDYBzuQnB-Ebzwl6aIUv5GYbLk0boET7vi-oIN_Ct-J1H7_1rM_4H0DFFfdIxxcIp-j2ESHvVE1WUM3Vx5EP3vOEv_kZJjEt77Jcvy75MG4O0Q6P2VHFNgnzaricHSV_n85dd9MAvY_ZKwZ7ArTdxRYlbFh4IuH2qQeqSPzkQr6ZuFr-zRJxAL_VVJ9zdKaxWjJbGSXcnhFstm9aIweYfIrVHCh6H6Uzg_8CXYZa-V7C25p0JDrYXYkdkDIqZ4P5vmpQQg9YDp2eAX2450zLVECNqxzFSHteZdnKdyBzkWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=qTI1C9x5T7LsvMxiE3uHKRingdOsn3xSbcmpIgvSwMPeDYBzuQnB-Ebzwl6aIUv5GYbLk0boET7vi-oIN_Ct-J1H7_1rM_4H0DFFfdIxxcIp-j2ESHvVE1WUM3Vx5EP3vOEv_kZJjEt77Jcvy75MG4O0Q6P2VHFNgnzaricHSV_n85dd9MAvY_ZKwZ7ArTdxRYlbFh4IuH2qQeqSPzkQr6ZuFr-zRJxAL_VVJ9zdKaxWjJbGSXcnhFstm9aIweYfIrVHCh6H6Uzg_8CXYZa-V7C25p0JDrYXYkdkDIqZ4P5vmpQQg9YDp2eAX2450zLVECNqxzFSHteZdnKdyBzkWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز، ترجمه ماشین:
خبر فوری: معترضان چندین بار جلسه ادای شهادت پیت هگست، وزیر جنگ، در برابر مجلس سنا را مختل کردند و پلاکاردهایی با نوشته «نه به جنگ با ایران» در دست گرفتند.
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
پلیس کنگره هر چهار معترض را از جلسه بیرون برد.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77369" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEr56qCAWkfT7sFKakWzyz7BY6ckCkolitdn2gH1f3P8KrCKH0p0QT8chJIkLqchzttGN-C1smzADoM9iDoHFN9c4_tAownfFG4VpFPJBWf0xwmFtxY1c16XJeENEWGWqSjmA5YAv7Ujv4DkTwnhGwWyNaUmkGk_FKVYF6H8YJEpKwuCsT_5ZWLpLNELlT0sO5CPBeZKlO1Eq5tiPSwekbK9rp7e27j5MNeWL3R9M0QJDFMqXgZASt4i875V8RUdkZFQ4VVihwkryj4OjFwNs56mJjPJCQf0J1IzX3D-PRoWLHKbdBrEngfCJxAkcFHLCenSmIOCGP5k6HhPQH0YTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز سه‌شنبه ۳۰ تیرماه گزارش داد اندی برنهام، نخست‌وزیر جدید بریتانیا، با استفاده ایالات متحده از پایگاه‌های نظامی بریتانیا برای آنچه لندن «حملات دفاعی» علیه ایران می‌نامد موافقت کرده و بدین ترتیب سیاست سلف خود، کی‌یر استارمر، را ادامه داده است.
این خبرگزاری به نقل از منابع آگاه نوشته که استارمر روز ۲۶ تیرماه نشستی با وزرا و مقام‌های ارشد برگزار کرد تا سیاست بریتانیا پس از ازسرگیری عملیات آمریکا در اوایل این ماه بررسی شود.
این منابع افزودند که در آن نشست، وزرا تصمیم گرفتند سیاست موجود ادامه یابد.
بر اساس این سیاست، پایگاه دیه‌گو گارسیا در اقیانوس هند و پایگاه هوایی «آراف فیرفورد» در گلاسترشر انگلستان می‌توانند در اختیار هواپیماهای آمریکایی قرار گیرند که مأموریت‌هایی برای مقابله با تهدید موشکی ایران و نیز اهداف مرتبط با تنگه هرمز انجام می‌دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77368" target="_blank">📅 22:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77367">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XG4Ys7jS-qYyTERcqIXWLNNi40CAkxQSTS938e8NY4RRqga8Cqh0U16RCX6mU9SgazMKThyyqsyP03c8GCeZAVET9NmroAUHyhgl_fNE1x4exHmRHBCFqKS4_wvLMAyrFd_Ay97_DbqVvjVdoFd6-zJT-jYlv_SlUGYq7pnR891VGgCReIrvTW6WLwY7jJY1iZi4nRC0bzJEeEwAqyExDtV9tWluXmdlqlyzmyffLLwwNYr8YFrDsVHqHxKJxO9SPYzf0Xh1L9fbc41TEsyxKUMRBA_dnQJFVr94_MAk1prU2A2IF8FDF8lg6iAo5JtU0ekdacMJRtMLTGn5csC27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیته دفاع پارلمان بلغارستان روز سه‌شنبه ۳۰ تیر با طرح دولت برای استقرار موقت هواپیماهای سوخت‌رسان و نیروهای نظامی آمریکا در پایگاه هوایی بزمِر موافقت کرد؛ اقدامی که با هشدار جمهوری اسلامی به صوفیه همراه شد.
بر اساس گزارش خبرگزاری رسمی بلغارستان، کمیته دفاع پارلمان از پیش‌نویس مصوبه شورای وزیران حمایت کرد که بر اساس آن، حداکثر هشت فروند هواپیمای سوخت‌رسان آمریکایی و ۲۵۰ نیروی نظامی این کشور می‌توانند به طور موقت در پایگاه هوایی بزمِر در جنوب شرقی بلغارستان مستقر شوند تا از عملیات آمریکا در خاورمیانه پشتیبانی کنند.
بر اساس این گزارش، آمریکا درخواست کرده است این استقرار از ۲۴ ژوییه تا اول اکتبر ادامه داشته باشد.
فرماندهی مرکزی آمریکا، سنتکام، در پاسخ به پرسش شبکه سی‌ان‌ان درباره این استقرار اعلام کرد: «به دلایل امنیت عملیاتی، درباره جابه‌جایی نیروها یا آرایش احتمالی نیروها در آینده اظهار نظر نمی‌کنیم.»
ساعاتی پیش، جمهوری اسلامی به دولت بلغارستان هشدار داد از خاک یا تاسیسات خود برای حمایت از عملیات نظامی آمریکا علیه ایران استفاده نکند.
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، گفت هرگونه مشارکت در برنامه‌ریزی یا اجرای چنین عملیاتی به منزله همدستی در «جنایت تجاوز و جنایت‌های جنگی» خواهد بود. او همچنین از پارلمان بلغارستان خواست با این طرح مخالفت کند.
بلغارستان که از اعضای ناتو است، بر اساس توافق‌نامه همکاری دفاعی دوجانبه با آمریکا که در سال ۲۰۰۶ امضا شد، پایگاه هوایی بزمِر را به عنوان یک تاسیسات مشترک در اختیار نیروهای مسلح دو کشور قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77367" target="_blank">📅 21:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77361">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AbGA4qVGMLaPDOBH9VTBIClh2hO_Fu52_h0G9GrPo6igdJ_hT54DU7JHBDIXpLlRVe_H-vmFsYHXDi0Mn9uVw0ZDF7iKc7GUiaXDK3MoAOqiGXPN-xbXQt4Y1Gfuci7AidOBaM96Z1wQHK6mt-2OuiWsy6ESHet_e4F4VEQqtTxAUOgbOqytS8byMZ5Xqqx5np9jF7Vh1Q7TqWUqPTbZyf9UPG9STZVKgg6lGGmrBAF4JlcGY1ef1IGVcX1Anjf4e4RM9n_wpshvrJ6cBd3dSZ3HaAe6jo8BUoxNV3rCEh-9cYN2jnpOgP0VYFUi-3ssXs5Jp18cRRCw2TOaOnAV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pYziQWMPRKH-weDSjULaOGx7JDU9JWGphS3XhKefjN90oCyJI2MYxw9cqRT4kEMCGcZAwjEbObm-oR8cWbyuC6O0s7gClKFUswATWEo81cyPIF-Uf5vPvWFzxm-gEIGpqTv8gaqUJL8fUCLtzZ52IcAF6LJsEwJo2457ovnDi3T7npDBgCXyjcdF1w8Vob604oOcFPwf8KbjiPue36isPr6ZmoYL07nSJuUiqB3eITd9tEzStGOv8ScUZ8Gy7Riy84e0TzZ-XX3N-Y8FvX3j7FciPVvgNCzHMC0x4hld9LYbfz98ABJcSRnIW8bKMItyJSs7jii2LfbEvnEGtdkX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A5O602qwbJ-inDeHIo9zGqnHAnjmk2YFufKPAk6YpkmNR_Oezn8ZB6wuqFMTmnCIlCVDxdJI27Rs9Lztsr9cT3Yc8-dxX75t0e7G4s6-XXowN35A_5DssPVhfaraPyV4kplO1oSFsVGwyArShVkspse_cFa7XA708znl-m3dimX-wPw1DfHuDQrj6sGGjjJR2u7ZWQ5vGPyJnE3Ro0nUD-poOU_9MFJEbr2pdCcsbzeYNsmV_POQywjCLzR9m6xS_F-sbecTL2HuH6YFY_cHSMRqdvYSquz9Wt4dCFkRDo7CTWH9X8rvPGX3BLWzofdddYmnKCuWra2JDPZVuiq-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uzRty62uMCr1HQkV0CJidzw2nyT_TLiduonrFLlnmnh3pCuPFG4nAAWQGuf0eLhMiX0NVwu8-ackrV3AvRpA93ZubXDI9J1stZAA2enQK39HMOmZdAzwbbE957aWV0f2Af3y9pqWmqSWlVIMet1RsRul-Yq93gpiTWtx10U4YVnqJP3MQ0fzes1xlXH8VU_RvyDxoVEqvz7gEi07rGWXsphcQGakjyej8dT9dX-bfGU5goOkL-yLRD3BwrfPtTS9hTta9wRnYKMYGP8i3xv7bqM7ikXribRY4Qx60HXbzu0p3vCFBQTDSPYVypsRslz9imaScYz56LYZw0eNhny0cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4477673f76.mp4?token=jPC8-8wwmVvU166NAoyo-DH3b3KpJVD3LWaPnVxR_h7jT6wQlvvIqkP8ab_cjsEfDCSeULxaYnXLx7hx6DptxrrLmiFu86Jlaae5Sg938RREjTKh6UVXDQRgcr2D_0wlhI6bKpp0GixYxy12-5binizIua-Vgu0KN1fxz7m867Mqmc31G2fVC9xyVj3FQ_7yjMUM8q_IP12dtUhb5B_MaSWOubcYrVDIt2mtRcUEpDbBfEq5gk6FkEBPo1SE01iVmR5_fy1tMDXmsTHjzfA3UNzOQuQEAfsQmu3nvB7DPt37LInoNnREWiReUp-5Fq7PRUx1-Z52NSgMawVZIIrERA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4477673f76.mp4?token=jPC8-8wwmVvU166NAoyo-DH3b3KpJVD3LWaPnVxR_h7jT6wQlvvIqkP8ab_cjsEfDCSeULxaYnXLx7hx6DptxrrLmiFu86Jlaae5Sg938RREjTKh6UVXDQRgcr2D_0wlhI6bKpp0GixYxy12-5binizIua-Vgu0KN1fxz7m867Mqmc31G2fVC9xyVj3FQ_7yjMUM8q_IP12dtUhb5B_MaSWOubcYrVDIt2mtRcUEpDbBfEq5gk6FkEBPo1SE01iVmR5_fy1tMDXmsTHjzfA3UNzOQuQEAfsQmu3nvB7DPt37LInoNnREWiReUp-5Fq7PRUx1-Z52NSgMawVZIIrERA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی  در شیراز
دو تصویر اول منتشر شده در سایر منابع
سایر تصاویر دریافتی از شهروندان،
سه‌شنبه ۳۰ تیر
گویا تصاویر بالا دو نقطه مختلف شیراز رو نشون میدن: کوه دراک و کوه نزدیک دروازه قرآن
آپدیت:
به گزارش رسانه‌های ایران عصر امروز سه‌شنبه(۳۰ تیرماه) آتش‌سوزی گسترده در ارتفاعات دراک شیراز رخ داده است که همچنان ادامه دارد.
خبرگزاری ایرنا گزارش داده است که شعله‌های آتش، مراتع ارتفاعات دراک در شمال‌غرب شیراز و کوه‌های نزدیک به دروازه‌ قرآن را در بر گرفته است و «زبانه‌های این آتش‌ از نقاط مختلف شهر به وضوح قابل مشاهده است.»
رئیس سازمان آتش‌نشانی شیراز گفته است: «۵۰ آتش‌نشان به همراه دو تیم تخصصی کوهستان در حال تلاش برای مهار حریق هستند.»
هادی عیدی‌پور به خبرگزاری مهر گفته است: «به دلیل صعب‌العبور بودن منطقه کوهستانی، وزش باد و وجود پوشش گیاهی خشک که موجب گسترش و شعله‌ور شدن آتش می‌شود، عملیات مهار حریق با دشواری همراه است.»
دلیل این آتش‌سوزی هنور اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77361" target="_blank">📅 21:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77360">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf4d005f22.mp4?token=Tx3pp9bRIbCmNbam6Yjc1f4IyuTi-lOFIEt8dVLxj_zjgl_VelMucCi0-lQ-mot23O7Z2tKSRi54W3kF01GHIHsr4Mf2NmyLt3xCJbi7dUkrn4T6IipO4yJK_nxaLxztXzawJXiaIIx-iHnIm3v2TcTJCdjigfrHFq_Z_f2XJbexps5BJmrS03f8Wtc1THth7PNxXxoZMVUvEPPFcDy0CADLUsZqX_vb0TTT4_dxieLZZ90CbemklVP1_I62QUzOppNH_lAKYv2GK4Euu_vOJvIdr6hCgmrGDcLP2FMcUx33gnrc3LAclnMdIEY5theljc_MieY20VJZ739bn8SCi2-BOrR9-q35EuholqjoOE-35O4BUX2Ivge-A2aJPglVnCaEMCsETKn9bKcVKe1K0NJHWegGCbLek22zX6VuBYUfohBVXh-Kj70L_KrecSwd3YSsTxmVUNDdUX5OUuggCGUG1NubVgSnWl1f8zk15y_jLPo7uD-DU3FAdxk5pdJRCbsF_vcPbRatI-ypgTgtUQOSoz2EWF9obILPyJIUlltoUGZrZV2qpJDzWbd5U5IbxbgGc2-tQ_h64OQHVORWqPKnAbGKbhUSf03qUzv7ufjlyfpDn63aNbcYmpuDrQGPIstwAY6TKdC3TZ0Jx6HFRG5cFPwwFJcEqSYa_sW-X0I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf4d005f22.mp4?token=Tx3pp9bRIbCmNbam6Yjc1f4IyuTi-lOFIEt8dVLxj_zjgl_VelMucCi0-lQ-mot23O7Z2tKSRi54W3kF01GHIHsr4Mf2NmyLt3xCJbi7dUkrn4T6IipO4yJK_nxaLxztXzawJXiaIIx-iHnIm3v2TcTJCdjigfrHFq_Z_f2XJbexps5BJmrS03f8Wtc1THth7PNxXxoZMVUvEPPFcDy0CADLUsZqX_vb0TTT4_dxieLZZ90CbemklVP1_I62QUzOppNH_lAKYv2GK4Euu_vOJvIdr6hCgmrGDcLP2FMcUx33gnrc3LAclnMdIEY5theljc_MieY20VJZ739bn8SCi2-BOrR9-q35EuholqjoOE-35O4BUX2Ivge-A2aJPglVnCaEMCsETKn9bKcVKe1K0NJHWegGCbLek22zX6VuBYUfohBVXh-Kj70L_KrecSwd3YSsTxmVUNDdUX5OUuggCGUG1NubVgSnWl1f8zk15y_jLPo7uD-DU3FAdxk5pdJRCbsF_vcPbRatI-ypgTgtUQOSoz2EWF9obILPyJIUlltoUGZrZV2qpJDzWbd5U5IbxbgGc2-tQ_h64OQHVORWqPKnAbGKbhUSf03qUzv7ufjlyfpDn63aNbcYmpuDrQGPIstwAY6TKdC3TZ0Jx6HFRG5cFPwwFJcEqSYa_sW-X0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به زودی «کوه کلنگ گزلا» در نزدیکی نطنز را هدف حمله‌ای شدید قرار خواهد داد
06:33
دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۰ تیر در دیدار با جوزف عون، رییس‌جمهوری لبنان، گفت جمهوری اسلامی با «درماندگی» به دنبال مذاکره برای پایان دادن به جنگ است و هشدار داد آمریکا به‌زودی «کوه کلنگ گزلا» در نزدیکی نطنز را هدف حمله‌ای شدید قرار خواهد داد.
@
VahidHeadline
رئیس جمهور آمریکا در پاسخ به این سوال که آیا ممکن است ایران سانتریفوژهای خود را به داخل تاسیسات کوه کلنگ منتقل کرده باشد، گفت:
«ممکن است کرده باشند ... ما اطلاعات مستندی نداریم ما فقط در اخبار جعلی این چیزها را می شنویم. اما سانتریفوژ بدون مواد هسته‌ای اهمیتی ندارد. ما مواد هسته‌ای را دنبال می‌کنیم که اصل قضیه است. آنجا را می‌زنیم، احتمالا خیلی زود. معمولا این چیزها را اعلام نمی‌کنم. اگر فکر می‌کردم می‌توانند جلویمان را بگیرند نمی‌گفتم.»
@
VahidHeadline
ویدیوی بالا: قطعات مربوط به ایران به تشخیص ماشین
متن زیرنویس ویدیوی بالا (ترجمه ماشین
)
تیترهای پیشنهادی چت جی‌پی‌تی درباره متن زیرنویس ویدیوی بالا:
▪️
ترامپ: ایران عاجزانه خواهان مذاکره است؛ هر تأسیسات هسته‌ای تازه را به‌شدت هدف قرار می‌دهیم
▪️
ترامپ: اگر امروز هم خارج شویم، بازسازی توان ایران ۲۰ تا ۲۵ سال طول می‌کشد
▪️
ترامپ: ایران هنوز چیزی ندیده؛ به هر محل فعالیت هسته‌ای حمله خواهیم کرد
▪️
ترامپ: محاصره ایران مانند دیوار فولادی است؛ هیچ‌کس عبور نمی‌کند
▪️
ترامپ: ایران سلاح هسته‌ای نخواهد داشت؛ برای حملات سنگین‌تر آماده‌ایم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77360" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77359">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5ebdb6d740.mp4?token=RtCRuHeXUM6UUf5nGEyOlPMFseTT-elffKXO5bQOvfn-n3cdP3jsC7JRStqc3d_V6HsNryAEmCLyZeT-J7sDaSbXNvyrwAlDm1xj7XO-JNf5Hu_RRRixkZzdOnLwyd30Qn3lnhJSdor964o2v-Af8dTqLTjK6V1i_RRt-zRAXZriOmr8pUL_FxLDrT13PSMq-FKKPko50rzulYb22Kyk2LDuwQHtgLSggfwrre024z3TnWInmf_XVq4W7uH7tAtbHI0kEWCMnaWy2XdZdWk46QKeUxbVBMecBiGidQqJA-2C9A8bv-1JH6zGRHCMp26ju2aTXkLzB0X3EZrtp0gpww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5ebdb6d740.mp4?token=RtCRuHeXUM6UUf5nGEyOlPMFseTT-elffKXO5bQOvfn-n3cdP3jsC7JRStqc3d_V6HsNryAEmCLyZeT-J7sDaSbXNvyrwAlDm1xj7XO-JNf5Hu_RRRixkZzdOnLwyd30Qn3lnhJSdor964o2v-Af8dTqLTjK6V1i_RRt-zRAXZriOmr8pUL_FxLDrT13PSMq-FKKPko50rzulYb22Kyk2LDuwQHtgLSggfwrre024z3TnWInmf_XVq4W7uH7tAtbHI0kEWCMnaWy2XdZdWk46QKeUxbVBMecBiGidQqJA-2C9A8bv-1JH6zGRHCMp26ju2aTXkLzB0X3EZrtp0gpww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، روز سه‌شنبه ۳۰ تیرماه در یک مراسم عمومی با بیان این‌که «سطح دسترسی» به مجتبی خامنه‌ای افزایش یافته، گفت تمام اقدامات مربوط به مذاکره «بر اساس رهنمودهای» رهبر جمهوری اسلامی انجام شده و از «اظهارنظرهای نادرست و بی‌توجه به ابعاد مختلف» در این باره انتقاد کرد.
مجتبی خامنه‌ای حدود ۱۰ روز پس از کشته شدن پدرش در نهم اسفند ۱۴۰۴ به‌عنوان رهبر جمهوری اسلامی معرفی شد، اما از آن زمان نه تنها هیچ فایل تصویری که هیچ فایل صوتی هم از او منتشر نشده است.
عباس عراقچی، وزیر خارجه ایران، به‌تازگی اعلام کرده که «هیچ‌وقت» مجتبی خامنه‌ای را از نزدیک ندیده و در دورهٔ رهبری او نیز جز معدودی او را ندیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77359" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77358">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVqVjkeSp5k6uKnI_vhbWz70BIeFlOg7D27z1TUj5_I8jOq0IAYx0qupvq9RaA-YE6kigFf1321LfSYzgkJVAHUQXV1N6NI2-un1RGrHqedkiXVdW-zqaVMQdODjKNHhHikd3DDsF6wHbAHDinwRaKlaYEPYAfXJgoRJlk-4dvtEfb0yxydtc-ppDHMXxcFXlJswS3Nww4Jn1hlx4E7FarSlGMC5tb17uaarKA-RaNg7yjgDpnLtJAGMTuTxQaZrJJ4kQfpdPqrPQQ3VLer4hY_xEq1qscNLuzq4qtYo5diAInt_aDnXBRza38SIh477dhCQXb4IYZlPeXg9S1o5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، «شیده توکلی»، شهروند بهایی ساکن تهران، را به ۱۱ سال حبس تعزیری، جریمه نقدی، محرومیت دائم از اشتغال در خدمات عمومی و دولتی و مصادره بخشی از اموالش محکوم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77358" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad05dc08a.mp4?token=I8qabsvPnId2wLi94HVYbEyYINWEq2cvyX0kGSvtTWmeltvDhtjK8NTUfkxG93fStJ4mtcyTDnRnrXMjvZDdsBSwkaQO0x1aVy0-ofsjMmHoP5QL6YzPRLPORZfhbRYoIVPG_hIwB_KcFqPhcBbgf6Ys7Bj0XaCa_CxvGFBJQSywM2ucO5gRZAgI7gqTNdMic0UQg8ceoxF1CsP-Vjf5x4GaCJHehHI2D3Xdt-XLx7GZhJUBK8B82892LlVxqFfsdrC-0167Ln99pha2vZiRyAyvJGjiT53lERqge4AhhQkd_JCtpp44RZh5TmJzgU1731sibJ2BYDcGI_Onr5BUNK7QUL2G9xxaLBt8v3B0LqVEhbsBW1p_CYsz5xhrtNHAiG2I6L3xVGZtxgB_wWg546k0MadPPe1-vAKyKymhx12PFjZT2iLBlgWIgLSja-h0a3VB3OKPtXokr8KR4ltdPBuMMcU8EmhFqR53F8lqLUxTa_DEahJacEriUQ8nHL_XZprdkQ23OiRDKA0Nchm2bXwXMSxqvvT8JDeU4DKChFdOCmhhL3ryyXlPjWC45wqyScu19sI2FBQH8XfNFZzMrA3Pux6gwMZLOImNAZvqQzYNIhr-hho159wFMLPBWQ58f7khDC9EeeuKl_XhvZcsopoZmw1mBHmPp65VWItCDr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad05dc08a.mp4?token=I8qabsvPnId2wLi94HVYbEyYINWEq2cvyX0kGSvtTWmeltvDhtjK8NTUfkxG93fStJ4mtcyTDnRnrXMjvZDdsBSwkaQO0x1aVy0-ofsjMmHoP5QL6YzPRLPORZfhbRYoIVPG_hIwB_KcFqPhcBbgf6Ys7Bj0XaCa_CxvGFBJQSywM2ucO5gRZAgI7gqTNdMic0UQg8ceoxF1CsP-Vjf5x4GaCJHehHI2D3Xdt-XLx7GZhJUBK8B82892LlVxqFfsdrC-0167Ln99pha2vZiRyAyvJGjiT53lERqge4AhhQkd_JCtpp44RZh5TmJzgU1731sibJ2BYDcGI_Onr5BUNK7QUL2G9xxaLBt8v3B0LqVEhbsBW1p_CYsz5xhrtNHAiG2I6L3xVGZtxgB_wWg546k0MadPPe1-vAKyKymhx12PFjZT2iLBlgWIgLSja-h0a3VB3OKPtXokr8KR4ltdPBuMMcU8EmhFqR53F8lqLUxTa_DEahJacEriUQ8nHL_XZprdkQ23OiRDKA0Nchm2bXwXMSxqvvT8JDeU4DKChFdOCmhhL3ryyXlPjWC45wqyScu19sI2FBQH8XfNFZzMrA3Pux6gwMZLOImNAZvqQzYNIhr-hho159wFMLPBWQ58f7khDC9EeeuKl_XhvZcsopoZmw1mBHmPp65VWItCDr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند  از ابتدای سال ۲۰۲۶ تاکنون اعدام دست‌کم ۸۵۱ نفر در ایران مستند کرده است که ۳۲ مورد آن تنها در ماه ژوئیه انجام شده است.
🔸
بر اساس قوانین بین‌المللی، مجازات اعدام تنها به «شدیدترین جرایم» — که به معنای قتل عمد تفسیر می‌شود — محدود شده است؛ با این حال در ایران، جرایم غیر خشن مرتبط با مواد مخدر، بیشترین سهم را در آمارهای اعدام با این‌گونه اتهامات دارند.
🔸
طبق داده‌های گردآوری‌شده توسط بنیاد عبدالرحمن برومند، نزدیک به ۴۵ درصد (۲,۹۴۶ مورد) از کل اعدام‌های ثبت‌شده در بازه ۱۰ ساله ۲۰۱۶ تا ۲۰۲۵، مربوط به اتهامات منتسب به مواد مخدر بوده است.
🔸
سوءاستفاده حکومت ایران از مجازات اعدام به حدی وخیم شده که زندانیان واحد دو زندان قزل‌حصار ، بزرگ‌ترین زندان دولتی ایران برای دومین بار در سال جاری دست به اعتصاب غذا زده‌اند و حتی برخی از آن‌ها لب‌های خود را دوخته‌اند. با گذشت هشت روز از آغاز این اعتصاب، هیچ‌یک از مسئولان پاسخگوی وضعیت آنان نبوده و به خواسته‌های اعتصاب آنها توجه نکرده‌اند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77357" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77353">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hx6oZ5kK3ssk5OgsTvTcM9F5s9mfwA5Mz7jvi1AazBEJkjeLPkhx3fXWTialu2QVLs91ZYSibqRvb9avGDQ6HIqqCv6-88nOZG8K2Kagkjb5j87mpGd_Apu6BB6MfLqrJkuLpZFvYLjGKcjVg7wzgZ1_3Aa6SWOsTYNzEKbmsO-l1Lh5yjRjXTqxQcQWpqJHw49bcfGBkVHGp9jrgfvjJW7T4muz5XYAAn8nHwuiHQq6RiMm5hjQuckh-MHQ7Xh8f38AynPYpB_jyUZpzmpt84ltglaeCUcBWVks72dJwTxmYR1oXZR2tXTA_a60c4ucKp9KJ9x8HcdIruwFroJ_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cK_nfhDCl2MFdxDTJNmnwMtJVG4XysEK6bzyqcEyTwEC3r1CwhpRhpzUuhJjg2urSetXULNSXyB74PHS1bSA-Xjy-ReHzTV1yg-Lxi1awcQjdGu5jPYOZyxiXpoQBI6-rcvFBxKUOH6AEZyOnqdyHSNDZ48Zr5AcC0yWNsEfNBPVfkTyQwBmdgBgdNCzIFBTm3y1L0WLF8gZJLTd_OLER-99v0GlPLSsRBA5F0W4hCGdfjVF5T13HpXHrcKNCvXrq-Bb6d0OVt_PivWW6B2xzITu1vyrtWuij5KrIafgATOPPPgwgUkLSviNclqs_DZCQuOWA0yOogzDTXl-HxPC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gi211z3Cor4O49gonLA0rs-hGsn7zbWiXqnbkheE7PYKJrmGk5757-fPfAZZtjmHABAGmxyvZ5kgPdXS-zK11Qo7jB6InFpbVu3PfdlBw-eudEl7oH5K2jGkXgju-lf79iNbaV5vmY0JbTeN7X1eGAE5NKWmwP-an3Rqb_qPD-Y1JogduZqkFBAV_THTdhc9maJy-JwpCAHN_KfWDhD_y_iuFQtg98SS4GeSKLc2F31uIQ-D0rr41QWCGC_Cal2-E0JCL-HKuRYM0qOvFMYyxo6-W-60Hmv7vpp2rudzswZPOWQ9Cb55-a5X5JFwXp4n2OzxC8MpCwxR1FS8akXtrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vbkj21KphBYtlIh7KcYodZ9d4hfD0qR8AyQeFH-wdk7McZhr8X9Rwgr7KX_RhowjXSo61lkFE8sE2xoTYIOEuHhhb495kCDGzAee4T1D2IBeuyTc_CwjjQk7lgPBTKenatfqFpMjqVbchzmqki7m0XUA9rAD2VJvZGoQIT1GWf0fWRSu1TYkkU5pI9Rwn_hOZzSZPKhclmPtTeg2BKyO1mDnh9lVXZNs6SgXLQsOGovWboq-rEyeREdHaZr4Q1sdRn6KqgqU0GVCTP6fsm4E9qKeNlIlr3QgK5g0z41cK1Qf-z_O66jEqwqko_qcbSciYQzhBF1-X0fHFE7BX-83WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز سه‌شنبه ۳۰ تیر با انتشار چند پست مختلف در شبکه اجتماعی تروث‌سوشال با بازنشر تصاویر و نوشته‌هایی از دو معترض به تازگی اعدام‌شده در ایران، مقام‌های جمهوری اسلامی را «وحشی‌» خطاب کرد.
دونالد ترامپ در یکی از پیام‌هایش با انتشار تصویری از یک پیام منتشرشده در شبکهٔ اجتماعی ایکس که به اعدام گل‌محمد محمدی، یکی از معترضان پروندهٔ موسوم به «میدان علیخانی اصفهان» اشاره کرده، نوشت: «آخرین مورد از ۵۲ هزار معترض بی‌گناه، و حتی بیشتر. وحشی‌ها!!! دموکرات‌ها کی از خواب بیدار می‌شوند؟؟؟»
رئیس‌جمهور آمریکا در پیام دیگری تصویری از یک پیام منتشرشده کاربری در شبکهٔ اجتماعی ایکس را منتشر کرد که در آن در کنار تصویری از عرفان اسفندیاری، معترض ۱۹ ساله اعدام‌شده در پرونده علیخانی اصفهان، نوشته شده که «لطفاً کمک کنید. لطفا صدایشان باشید».
آقای ترامپ در پیام دیگری، تصویری از یک زن گریان را بر حاشیه‌ای از پرچم در حال سوختن جمهوری اسلامی منتشر کرد که پلاکاری با این جمله را در دست دارد: «ما را نکشید».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77353" target="_blank">📅 18:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیام‌های زیادی از اصفهان دریافت می‌کنم درباره شنیدن شدن صدای انفجار و لرزش شیشه‌ها
پیش‌تر اعلام شده که:
صدا وسیما: صدای انفجارهای کنترل شده مرتبط با مهمات عمل‌نکرده از ساعت ۹تا ۱۶ بعدازظهر امروز در جنوب و غرب شهر اصفهان، بهارستان و محدوده‌های صفه و شهر ابریشم شنیده می شود
مردم نگران نباشند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77352" target="_blank">📅 09:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8SxEZH0RAV9TqFIVkkdBd2ed7-o7XA19B2HJ3lOzr3pYXi1X8I2ojp7ugL8ts2xAfhoEICfgtcI1dAs6wTQz9MC3mjm-zz-AZRGL9Ormf7tCLvoGMc5SfVxgfe00nGIvLUNokIaIPoV1bvdOVRNStLH02Omx584X59-6ppR39Fs3CK5NORXncBSROAB_3GGl7SpiWEZ7usW4TvPrw-w7-zqPiSGNQ92UV7LowaqY0Eop82a24FiTbbdjcop4GUabQLdw5cDNt3sFbb6cevee2AO89YsbFn_7lmX98q0mK5cZOfHFZ3Ti8IYJs-gqq7ITGPA2oXMQJJSn02lmUdRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای سپاه: سامانهٔ راداری دفاع موشکی و یک هواپیمای اف ۱۵ در آشیانه دشمن در اردن منهدم شد
خبرگزاری فارس:
🔹
روابط‌عمومی سپاه: ملت عظیم الشأن ایران اسلامی! با استعانت از خدای متعال، در ادامهٔ عملیات پاکسازی منطقه از رادارها و سامانه‌های پدافندی و هموارکردن مسیر حملات موشکی و پهپادی گسترده‌تر و تکمیل شب سیاه راداری دشمن آمریکایی، رزمندگان غیرتمند نیروی هوافضای سپاه در ادامهٔ موج ۲۴ عملیات نصر ۲ در حملهٔ موشکی به پایگاه آمریکایی در اردن یک سامانهٔ راداری دفاع موشکی را تخریب و یک فروند هواپیمای اف ۱۵ را در داخل آشیانه منهدم کردند.
🔹
این منطقه جای متجاوزان آمریکایی نیست، ارتش کودک کش آمریکا برای پیشگیری از تلفات بیشتر باید منطقه ما را ترک کنند.
📝
گزارش تکمیلی این عملیات تنبیهی به استحضار ملت شریف ایران خواهد رسید.
ادعای سپاه: زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین ویران شد
خبرگزاری فارس:
روابط عمومی سپاه: با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در پاسخ به تجاوز و تعرض روز گذشته ارتش کودک‌کش آمریکا به تاسیسات در دست احداث و غیرنظامی دارخوئین، زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون را در بحرین با چند فروند موشک کروز مورد هجوم قرار دادند و آن را ویران نمودند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77351" target="_blank">📅 09:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77350">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فرماندار آبدانان: آمریکا با موشک به نقطه‌ای در کوه‌های اطراف آبدانان حمله کرد
خبرگزاری جمهوری اسلامی، ایرنا:
🔹
به گفته فرماندار آبدانان، ساعتی پیش دشمن متجاوز آمریکایی با چند پرتابه مناطقی در بیرون از این شهر استان ایلام را هدف گرفت.
🔹
بهزاد نورمحمدی صبح سه‌شنبه در گفت‌وگو با خبرنگار ایرنا اظهار کرد: دشمن آمریکایی با پرتاب موشک، به نقطه‌ای غیرنظامی در کوه‌های اطراف آبدانان حمله کرد.
🔹
وی افزود: خوشبختانه این حادثه هیچ‌گونه تلفات جانی در پی نداشته و دستگاه‌های مسئول در حال بررسی ابعاد موضوع هستند.
🔹
نورمحمدی یادآور شد: دستگاه‌های امدادی به محل حادثه اعزام شده و مشغول بررسی دقیق ابعاد تجاوز دشمن هستند.
پیام‌هایی که من از یک شهروند دریافت کرده بودم از ساعت ۲:۴۱:
سلام وحید جان صدای دو انفجار اومد چند دقیقه پیش
ما آبدانان هستیم ولی صدا خیلی دور بود بیرون شهر بود.
ظهر هم رد موشک تو آسمون دیده میشد
الآنم یکی دیگه
2:49 دوباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/77350" target="_blank">📅 06:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=aZbxtMcUqEva1pzCd8d1Bfbok0oqalOzfN3zhu0qD3dPMGSvEil8xrG3lD3eg9b6d5dZf4_rZUMb4qxtTJoNNgDeSDppzUgQ05cb5AXbZXm7bZmNi3fGKR5xu_kLOy1dZLS4KaVwL1u2J7o318fy2cXTU5Bf9eCq_EhsIXagS7em_dj7bo4Y40fiYgUGjEBFeeR4AppRBY3sgjBldeaFVxbiP_C40wpPmi6jpuW_kmRuKOLIUhBGVXAF6M1-eKy2F_oBmECThPX4hswu6W4nXHaOnrnyqT_Ykk7YAWVBZXLmiJ1MocirnVC2jyclpgKdYrlotHgoDG2k_a16IkNo5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=aZbxtMcUqEva1pzCd8d1Bfbok0oqalOzfN3zhu0qD3dPMGSvEil8xrG3lD3eg9b6d5dZf4_rZUMb4qxtTJoNNgDeSDppzUgQ05cb5AXbZXm7bZmNi3fGKR5xu_kLOy1dZLS4KaVwL1u2J7o318fy2cXTU5Bf9eCq_EhsIXagS7em_dj7bo4Y40fiYgUGjEBFeeR4AppRBY3sgjBldeaFVxbiP_C40wpPmi6jpuW_kmRuKOLIUhBGVXAF6M1-eKy2F_oBmECThPX4hswu6W4nXHaOnrnyqT_Ykk7YAWVBZXLmiJ1MocirnVC2jyclpgKdYrlotHgoDG2k_a16IkNo5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع حکومتی با انتشار ویدیوی بالا: سه پایگاه مهم آمریکا در کویت، هدف حملات پهپادهای انهدامی ارتش قرار گرفت
مرحله نوزدهم عملیات صاعقه ارتش
روابط عمومی ارتش:
🔹
در پاسخ به شرارت‌ها و نقض عهدهای مکرر شیطان بزرگ، بامداد امروز و در مرحله نوزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، ساختمان‌های اداری  و آنتن‌های جهت‌یاب در پایگاه عریفجان، پارکینگ گروهی بالگردها در اردوگاه العدیری و ساختمان اسقرار نیروهای ارتش تروریستی در پایگاه احمدالجابر کویت را هدف حملات پهپادهای انهدامی خود قرار داد.
🔹
پایگاه عریفجان از بزرگ‌ترین مراکز استقرار نیروها و ستاد فرماندهی نیروی زمینی آمریکا در جنوب غرب آسیا و پایگاه العدیری محل استقرار بالگردهای آپاچی، شنوک و بلک هاوک نیروهای دریایی و هوایی  آمریکا است.
🔹
پایگاه احمدالجابر نیز نقش محوری در آماد و پشتیبانی ارتش متجاوز آمریکا در غرب آسیا دارد و تاثیر عمده‌ای در عملیات‌های هوایی و نظارتی این کشور ایفا کرده است.
🔹
ارتش جمهوری اسلامی ایران اعلام کرد، امنیت منطقه در پی شرارت های نیروهای تروریستی آمریکا مختل شده و  نیروهای مسلح جمهوری اسلامی تلاش می‌کنند در نبرد با آمریکا، امنیت و آرامش را به منطقه بازگردانند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/77349" target="_blank">📅 06:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/841c527612.mp4?token=RIz2guPQtw2wMFjZhTCl-AjSWLJFjn8FwMvYHz4Uww0DQHFnoxtJhhnSlOR_eHZProJofXEirV-m2lSLrejYvPbgdG_2KtoOca3Oi-tXIw9c2QU_DKq09lgt6NeaO5Jrh_vR29cyVe_E_L3hi_AAE02X3QuUAFY_OtDfIoy0mawumgpF7E3CyeOSkss3Zkm3Td_HI2vBhVWZ3t82WOzb9zO7bhCFZJLDusDGe8K2L7MEWmCzHmrxOG7OHaPDjBdFD5VtGWfnPolt9jzaEwFYXRMRSHa0vtnYZz4amgBqkaPZQKPVm_B9TBs4R_V_02ognovCmOrCIgycH5DJP8e3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/841c527612.mp4?token=RIz2guPQtw2wMFjZhTCl-AjSWLJFjn8FwMvYHz4Uww0DQHFnoxtJhhnSlOR_eHZProJofXEirV-m2lSLrejYvPbgdG_2KtoOca3Oi-tXIw9c2QU_DKq09lgt6NeaO5Jrh_vR29cyVe_E_L3hi_AAE02X3QuUAFY_OtDfIoy0mawumgpF7E3CyeOSkss3Zkm3Td_HI2vBhVWZ3t82WOzb9zO7bhCFZJLDusDGe8K2L7MEWmCzHmrxOG7OHaPDjBdFD5VtGWfnPolt9jzaEwFYXRMRSHa0vtnYZz4amgBqkaPZQKPVm_B9TBs4R_V_02ognovCmOrCIgycH5DJP8e3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند.
ترجمه ماشین:
پایان تازه‌ترین حملات آمریکا علیه ایران
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دور دیگری از حملات علیه ایران را در ساعت ۹ شب ۲۰ ژوئیه به وقت شرق آمریکا به پایان رساند.
نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز را کاهش دهند.
عبور کشتی‌های تجاری از این گذرگاه حیاتی دریایی بین‌المللی همچنان ادامه دارد. از اوایل ماه مه تاکنون، نیروهای سنتکام به تسهیل عبور حدود ۹۰۰ کشتی تجاری و ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
نیروهای آمریکایی همچنان در موقعیت و آمادگی لازم برای پاسخگو کردن ایران به‌دلیل تجاوز بی‌دلیل علیه دریانوردان غیرنظامی که در پی عبور آزادانه و بدون مانع از این تنگه هستند، قرار دارند.
CENTCOM
اطلاعیه شماره ۳۵ سپاه:
شب سیاه رادارها و سامانه های پدافند هوایی آمریکا در منطقه
روابط عمومی سپاه:
🔹
ملت عظیم الشان و مجاهد ایران اسلامی؛ حماسه حضور در میدان و ۱۴۰ شبانه روز ایستادگی بی‌نظیر و پرشور شما چنان روحیه ای به رزمندگان اسلام و مدافعان از جان گذشته وطن بخشیده است که با لطف و امداد الهی هر روز حماسه‌ای نو خلق می کنند.
🔹
ساعاتی پیش عملیات بزرگ رزمندگان اسلام برای تنبیه ارتش کودک کش آمریکا به خاطر برهم زدن امنیت تنگه هرمز و تجاوز به نقاطی از میهن عزیزمان آغاز شد.
🔹
فرزندان شما در نیروی هوا فضای سپاه شب سیاهی برای رادارها و سامانه های پدافند هوایی آمریکا در منطقه رقم زدند و در موج ۲۴ عملیات نصر۲ با رمز مبارک یا رقیه (س)، به منظور هموار کردن راه عملیات گسترده آینده و از میان برداشتن موانع اصابت دقیق اهداف یک سامانه پدافندی و یک رادار آمریکایی در المحرق بحرین به طور کامل تخریب شد و از مدار عملیاتی خارج گردید و همچنین یک سامانه پدافند هوایی پاتریوت آمریکا در اَلرفاع بحرین هدف حمله همزمان موشکی و پهپادی قرار گرفت و نابود شد.
🔹
تنبیه متجاوز ادامه دارد و گزارش آن به استحضار شما ملت عزیز و قهرمان خواهد رسید
و ماالنصر اِلا من عند الله العزیز الحکیم
اطلاعیه شماره ۳۶ سپاه:
یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی و یک سوله آشیانه پهپادهای MQ9 منهدم شدند
روابط عمومی سپاه:
🔹
ملت عظیم الشان و قهرمان ایران اسلامی؛ در ادامه عملیات تنبیهی رزمندگان هوافضای سپاه و در راستای هموارسازی مسیر، برای دفع موانع عملیات هوایی و موشکی گسترده در مرحله دوم موج ۲۴ عملیات نصر۲،  امشب یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی ارتش کودک کش آمریکا مستقر در کویت مورد اصابت موشکی و پهپادی قرار گرفت و منهدم شد.
🔹
همچنین یک سوله آشیانه پهپادهای MQ9 نیز در پایگاه علی السالم مورد اصابت واقع و تعدادی پهپاد منهدم شده یا آسیب کلی دیدند.
🔹
عملیات تنبیهی فرزندان شما ادامه دارد. التماس دعا.
و ما النصر الا من عند الله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77348" target="_blank">📅 04:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ICe2GEfg_3p-D6Lh6B8HBGZQZs_0i_qlMb6BUonCMYYzIKBWCjnRKLTww_VdXIa6KQqu1VfTdtt5q6G3zTs0zu2ErmyGOSUYNN9fHjcKMjYVY9M8ioqkhQWvdMDR-eUQRIPh8OBtHCPt-cW3_3n8QgUOHBwDJ5PM_QOX-UOzuvSOv9BdPKiqhBiwxjpW8QxUqMrPd4YZJTbFqPihEX-jLQub6FHyq-oSipMOiS_0AqGEk0R7PLbc6W177uPdYk7lkgA24cT8cmene2Za9-aU3LIiQRW3Ky8Yu05GJJk-8zVFLOuXAMSkR-aUW4qiROfjpLkf6tX9MVubt-nC63HG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
خبرنگار صداوسیما: حوالی ساعت یک بامداد در برخی نقاط شیراز صدای انفجار شنیده شد که بر اساس گزارش‌ها یک نقطه در شرق و دیگری در غرب شیراز مورد هجوم دشمن قرار گرفته است.
چند پیامی که من دریافت کرده بودم:
شیراز رو باز زدن
یجوری شیراز رو زدن که شیشه ما بدجور لرزید
سلام صدای دوباره انفجار در شیراز
شیراز دوباره زدن
خیلی بد زد
شیراز 1:21 صدای دوتا انفجار خفیف دیگه اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77347" target="_blank">📅 03:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5Px43ke5yJRD5IMqy21MWQNJy3NjLNG4ya5-1dPsAm5GmwYfkwIqiVCFfigG7le22JF3IvYKWJjqdOnPb3pmyIBXeuC4ZwhMMhoLFOjx6txp-f-X8_i5OTOmKIOcy7SBZdV-Pl5ny07Sy9xksmdACMt88N5sUDASERnRufY7HkMioXdJ9s-uOA9oT2-cAxiOxgJR3ZaaDCGcs9yvAyj2Q17IeYsyB09LU4U-GVXo5TndnTR29ztJ87EkKH7TEw-a-r4-IAxVMCPoZFO7UGEtzLNC_3qvaravZP7btZq_YujzBC0szViZbFeVfV5ZequlDRIWpajR0hoYQrr1BXh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درباره تماس با نخست‌وزیر تازه بریتانیا: درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
ترجمه ماشین:
گفت‌وگوی بسیار خوبی با نخست‌وزیر جدید بریتانیا، اندی برنهام، داشتم. درباره موضوعات بسیاری گفت‌وگو کردیم، از جمله روابط فوق‌العاده‌ای که با بریتانیا داشته‌ایم.
در آینده‌ای نه‌چندان دور برای گفت‌وگو درباره موضوعات مورد علاقه مشترک دیدار خواهیم کرد. نخست‌وزیر کار بزرگی پیش رو دارد، اما قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا نیز برای کمک در کنار او خواهد بود!
درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
این تماس جالب بود و بسیار خوب پیش رفت. برای نخست‌وزیر برنهام آرزوی موفقیت کردم: موفق باشید و خدا به همراهتان!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77346" target="_blank">📅 02:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKMYSFkgPQHdjCb6zoFPG6Xl8qFLLkMEX5LLZucbZaZz6IV7ZvyVjtOhoqNLhGIK9p7GzXkzUGKHeh6h70Sj2NurPae5k77yAabm5_5R56KIpHvd2w3XtYqMCu5L8P0pZ2f8p8NJJTgG-ry-3wiLteoCFKz6bU3vBJxEIdfUPNhmc5yArkuwS7L8ZZRbcigX6FqMGitfQqn-CHVRZBFBly1nf1Z--HbPtVBU-249P4Q61Qc-df6y2QgwA5ZjGq5OOOwheJwGiuVi5UsXpxkmcaUcKllF4K7xDgzrsARJyLGyUzviJVDyQ3iZzs4App0rRtjfMlK62YnekWaAyFDi4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی از یک حادثه در فاصله ۸ مایل دریایی شمال شرقی لیما در عمان دریافت کرده است.
این سازمان افزود گزارش‌های متعددی دریافت کرده که بر اساس آنها، یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده در تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77345" target="_blank">📅 02:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77344">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس پایگاه هوایی ۲ انفجار ۰۱:۴۷
بندر ٢ تا شنيدم ٣٠ ثانيه پيش
1:47 دو انفجار به شدت قوی در پایگاه هوایی خیلی شدتش زیاد بود بندرعباس
بندرعباس ۱:۴۷ دو صدای انفجار شنیدم
درود آقا وحید دوتا انفجار وحشتناک ساعت ۱:۴۷ دقیقه بندرعباس
همین الان ساعت ۱۱:۴۶ انفجار فوق شدید بندرعباس
۲ تا انفجار وحشتناک بندرعباس ۱:۴۷
صدای ماشین‌ها درومد
صدای دو انفجار الان بندرعباس ۱:۴۷
بندرعباس ۱:۴۷ صدای دو انفجار
تک انفجار شدید بندر
سلام الان صدای دوتا انفجار بندرعباس اومد
سلام وحید جان صدای دوتا انفجار پشت سر هم اومد بندرعباس
ساعت 1:48 بامداد
بندرعباس ۳ تا انفجار شدید
صدای ۲ تا انفجار سمت پایگاه هوایی بندرعباس
سلام صدای دو انفجار بسیار شدید بندرعباس ساعت ۱:۴۷
درود وحید جان وقتتون‌ بخیر
بندرعباس ساعت ۱:۴۸ دو صدای انفجار بلند.
بندرعباس ساعت 1:47، دو سه بار سنگین زد
سلام وحید جان الان دو تا انفجار سنگین سمت فرودگاه بندرعباس آمد که شیش ها لزیدند 1:48
سلام وحید خان بندرعباس ساعت 1:46 چندتا انفجار پشت سر هم
سلام وحید بندرعباس همین الان صدای 2 انفجار خیلی وحشتناک
اقا وحید  ۳تا انفجار شدید قشم ساعت ۱:۴۶
وحید‌ داداش
حوالی۱.۴۷ اینا دو انفجار مهیب. اومد
فک کنم پایگاه هوایی بود
ثانیه پیش هم زدن
حدودا ۴ انفجار شد
تعداشو دقیق شمردم کمی با هم فاصله داشت
در حد هر کدوم ۳۰ ثانیه
ولی همش از یه سمت بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77344" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77343">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیام‌های دریافتی:
۱:۴۵ قشم صدای انفجار همراه با لرزش
قشم من چهارتا صدا شنیدم، نمیدونم توهم زدم یا واقعی یود چون خیلی خفیف صدا اومد ۱:۴۵
چهار انفجار فعلا بندرعباس
وحید جان
قشم چهار تا انفجار ۱:۴۵ دقیقه
صدای انفجار بندرعباس ۱:۴۵
سلام وحید جان ستا انفجار همین الان بندر عباس ساعت ۱:۴۵
بندرعباس الان دو تا صدا آمد ولی صدا دور بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77343" target="_blank">📅 01:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77342">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منابع حکومتی
منابع محلی لحظاتی پیش گزارش دادند برای دومین بار طی بامداد امروز صدای انفجار در بندرلنگه شنیده شد.
چند پیامی که من دریافت کرده بودم:
سلام وحید جان بندر لنگه دو بار زدن
صدا و لرزش زیاد
ساعت ۱۲ و ۴۰ دیقه
ساعت ۰:۴۰   صدای انفجار در بندرلنگه شنیده شد
درود وحید جان
صدای انفجار در ساعت ۱۲:۴۰ بامداد از بندرلنگه اومد ۲ بار
گویا هدف، نیروی دریایی سپاه بوده
صدای انفجار ۲ بار در خونه لرزید بندر لنگه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77342" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77341">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پیام‌های دریافتی:
۳ انفجار در کنارک همین الان
۵تا انفجار سنگین چابهار ۱.۲۷
مجدد چابهار صدای چندین انفجار میاد
چابهار ۱:۲۷ دقیقه صدای ۲ تا انفجار اومد
ساعت 1:27 چهار انفجار پشت سر هم دیگه چابهار
کنارک 1:28 دو انفجار
۱:۲۸ دیقه کنارک دو بار صدای انفجار اومد
🔄
کنارک 4 انفجار دیگه
خیلی سنگین بودن این چهار تا انگار خونه رو سرمون خراب شد
۴تا دیگه چابهار همین الان ۱.۳۰
۱:۳۰دقیقه ۴ بار چابهار زد
نمیدونم کجاست اما از سمت دریا بزرگ دورتر
۱:۲۹ چابهار ۲ تا انفجار دیگه اتفاق افتاد
دوتا پشت سر هم و باز 3تا پشت سر هم 1:30 چابهار
صداهای شنیده شده در چابهار و کنارک: ۵ انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77341" target="_blank">📅 01:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77340">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GHBXus9GuRuI38p5oxUUcnTzSUtgPnTnS4UOBZl3maEsQ8_G6gbJ8uN0E4qMq6KJ1ULWgG_B3qaeawa7l8-99ebFzurAlyK4WZ9_AxJEReP2L5oFqUx3RhyQiUQPUy-Wm2DMjJgKWxrbQHUYszB8TNn86_XfTRm9napSMMmIvzduyjKe1g5jMx06BnPiG-k5dd3haq4Ix-o4GTQuGnKwNNT9RjHMSYGWSOARU5thn5W76D3CpQ05KfjfiJV5tLoXlP2sST1PAm2dNET-JCVD8glVH669bFmKYhfGvhgbfwmZkEaL0hUT-3kWC6NcFRPe5szIJO4386lzgBIZtZLU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر از شنیده شدن صدای دو انفجار در شهر اصفهان خبر داد.
دقایقی بعد، استاندار اصفهان اعلام کرد که امشب حمله‌ای به شهر اصفهان صورت نگرفته است.
@
VahidOOnLine
فارس:
استاندار اصفهان گفت: امشب حمله‌ای به اصفهان صورت نگرفته است.
وی ادامه داد: در حال بررسی علت شنیده شدن صدای انفجار اعلام شده از سوی شهروندان هستیم.
تسنیم:
معاون استانداری اصفهان: هیچ گونه تجاوز دشمن یا انفجار در سطح شهر اصفهان و سایر نقاط استان نداشته‌ایم
من هم چند پیام مردد داشتم و از این رو فکر می‌کنم صدایی شنیده شده ولی مطمئن نیستم که دلیلی نظامی داشته یا نه.
منابع زیادی هم هستند که هر روز کلی خبر دروغ تولید می‌کنند و از این رو اعتنا کردن به پیام‌هایی که بعد از چرندیات تولیدی اون کانال‌ها ارسال میشن هم خیلی سخته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77340" target="_blank">📅 01:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77335">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NqrAVnogESESYnbR0ZwZG6htgxaTSYdbQL56eT_1b_3mM0ut77HBireGXIWDc3RXcoakB_GCh0_0rxCLXYyIlkBtoTQKBepupRO4R9OTYLndHZw_Bn-7Sb5d0l6kxKQtlGJ2AngjIEKiLBvHtDjfo-Ev-uRW5q8x9xHk-f0iAcbd5VjUJbJnNS5R1GIydgp02QhoRp8csrl7xa8wJXg4c-E9GA2jt6tut0_tDrCsWugSfjszETN6ow5l0JS_69jBCXIOdLo-BbwF9gSUHMHNWmNxF-1PhNj9yb-7rPUtgpWJnqCfZDANOQpg_mDZwTiBh-GewxQ8Hn3GHy12cxk_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YZxwic6Tgcrz1J-oFnTlUNt8_dYUF3DS2pGygUDlzuAeE3eiRci43mueG2IkzI3IpYr0vUk4KqRTtYwk7righnbP6eViAlohgLWEn1CCPkHHwLJKuzofSh_TfaJA9Or2zfPvSfu2o8YG20axzWoneOuulLeExrJFl8QtCHGmwoC-OC60r3_8qHG9jC_4iEwR4TGVHH5LSF2G6r50IHrcbpA9TGHqNZYEt2eQBGSMPfeUL7eWBKDMNrZuAqySvyPvKTfEDGJwsK6-RB2Fa-Tajg9p5CXGR3E8PGZxja_1VEwfcUGKNI8d4AzkWAMcLQnet83sDMRQGGBt6tJy5PGDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eug2W9oW_FAUcNHvMxXZwoM3fqYchMlQJQ3mBrdXPUOnYfTScZUae3kCnITJr3sas5EFCOMxjeAyFTNCAEdsxdt5BBH_9_pKQXsw5HFZMJCKOt6tL2B5OZNiNbjIo3_1f8Kv99hXxK_Y3uVggRKrW4lrhpTwLtfZ0QyOFmIC1Sa_p22k78-Lo2HwuMhLajdOuo14WeDAyDE26FNdpPO_BHAeNe1Lf-FYJcgiUItqlpV2n0oDeSNy0uwGmE853rFBstOG0IdsWwUrkVGFKucOGlp3qnusL2jxDkjHkw0yApHDBY12F4Cx39cfLo-okzrZL49taVL0bxlx6-ELrCKH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z6PWA6bztI3uhfF5U2phzhcQT-6pS6nNk3Tfv9TPcANhAxh7mzSY5znxc2cdfZNNemCcaliZHV7LaWBnlH9b58a6UD6TRGuc6ppA820EgIBgLROcONItXsfzqOlOcoH0aGWrLZOR7L_4g5aE1y8JQu1Uz27jb7MLCVi5GWPdM-HsjqA3Pfz17jFuqVey0JZrDq6gBzgsMOEWSzBfnv2wbdhatKTGAxlb52eKGJv1DrbSGGQg-BIBKJ1A3j0oNUCiUmd13-wc05UYy3DybmLeZv7LuzzHDIWn0uRd6REpQJWrc-ZDDWWh_rGZLKkiKP3UPJpZQcqIMs4QsB4bfaTFzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IwswbIDZvqJe3H4WJR6YslATupmKYN3eL0VBgXfkwP3vFZzkio-o9UctW5b89WQPFE1Vm5W2sznvhE6ed8VrwzZ3T_1pdnDbFvpK-tnxQQzG83ty6j0mPIUuj2_BewixP9hyygB5JqEPsz_NTHzFOZjYw9gbdiuIrAJBQwFnbnB17RZC_X9JSDeBxWT0YJPVJ_kVPTH-hy9xOjhk8pyyn5zaXMr14kd01WULfiJakyO3ps_fqGUWoPeyTAtVlTh5ASB8WZOfIZwb86HT9YQN7OQ9iBUg5Et8Wio3ELlHFT6A8R0c7Pqaqcdid4YSkBRLo6MSefpTIMryu8JkZIxjnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Vahid
'هدف قرار گرفتن نقطه‌ای در کوه دراک شیراز'
تصاویر دریافتی از شهروندان با شرح بالا، سه‌شنبه ۳۰ تیر حدود ساعت ۰۰:۴۰ بامداد
Vahid
📍
میگن
اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77335" target="_blank">📅 01:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77329">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AyTPl2v3aVbxXfDUeVt5ayhN-hGiiuof1mn4d2ix7QHWlpapiAH_d9VXkS1MHxP_ZosQeMjnJiSdNlhh6Ms1-15w8ynSmWjcDX-93Oo5cqQUOd2YRFqDbzl7cLE-s9gfixxdnH_gFPi7UxB1d8OmTkb1LWYyuUTa4iQbi9X9yE4hDRs-0iuKjyF9z-mkD9i4ZwpOEXAPkWUXVBt0QoxguJnm0BXdfhtdhVVkpU_UF6l1YvQ4xuO6_6M5NYJF1DcUnEd2mjeO1f3r5yIphlsfzd7Idv8iGISglKRXHIoubK1gUWi3OGYIL_xNriiGX40jez__njvpXQ6i3sy788_oMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r4sQnlbe3ur-nIe2Z7c0t5fSzLrEm8oyjjcxegZ0DMbuM1tvGOVUuP8Gf3uQaalM_s-jdDDO8yyLG7Jb5Bn9db5JP78F_s2GaExJkITe2WwVC5CowzQeLXwg_TXiDcm_2hAYf-FTAPXBBkPCoDUs2fNdRlLjrvAxBNgim5Kel73BYi-PgTciu_LmWYmpU-Nv90kTEAdsjQPuBjRDGl05nuYRasOMdegZWSLFspTBvXEyjJpOBixYqWPDxct3K52zHWwDcScDHNZ9qtdGQRQMcghGdE0z2_5LWpwZbqx4B0MBvPmRFartITBZap7_4yvZeZKssr4oDgUPtwBMJWbW_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی درباره صدور هشدار در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77329" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77328">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده ده دقیقه پیش:
سلام شیراز همین الان صدای انفجار اومد12.37
شیراز همین الان صدای انفجار اومد
شیراز همین الان صدای انفجار مهیب اومد
🔄
پیام‌های رگباری الان:
همین الان شیراز و زد کلفت
همین الان صنایع صدای انفجار اومد
سلام وحید جان
شیراز سمت صنایع رو زدن ساعت 00:45
00:45 شیراز صدای انفجار
فکنم صنایع الکترونیک رو زدن
همین الان شیراز صنایع رو زدن
شیرازو زدن همین الان
سلام وقتتون بخیر
ساعت ۱۲ و ۴۵ دقیقه بامداده
شیراز همین الان صدای انفجار اومد
شیراز صدای انفجار
همین الان شیرازو زدن رکن آباد خونه لرزید
فرهنگ شهر شیراز صدای انفجار مهیب  ۰۰:۴۵
شیراز صدا اومد
سلام یدونه تک انفجار صنایع شیراز ساعت 0:45
شیشه ها لرزید
ساعت ۰۰:۴۵ صدای انفجار از شیراز
شیراز ۱۲:۴۴
احتمالا صنایع صدای انفجار
درود وحید جان
الان صنایع الکترونیک شیراز رو زدن
این دومین انفجار امروز تو صنایع هست
شیراز الان 00.46 زدن
12:45 معالی آباد صدای بلندی شنیده شد ( انفجار یا بمب نمیدونم)
چهل و شش دقیقهٔ بامداد صدای جنگنده و انفجار در شیراز
سلام وحید. ساعت 00:46 محدوده صنایع الکترونیک، صدای انفجار شنیدیم.
شیراز صدرا همین الان صدای شدید انفجار اومد
شیراز صدای جنگنده اومد روی کوه دراکو زد انفجارشو دیدم
همه فکر میکنن صنایع رو زد ولی بالای کوه دراک بود
امروز ساعت ۵ هم از بقیه شنیدم که صنایع الکترونیک شیراز رو زده بودن
سلام شنیده شدن صدای انفجار صدرا ۱۲:۴۷
همین الان صدرای شیرازو زدن
شیراز صدای وحشتناک بلند همه جای شهر شنیدن یا صنایع بوده یا کوه دراک
وحید ساعت ۱۲:۴۵ بعد نیمه شب صنایع الکترونیک شیراز رو زدند صدای انفجار اومد
۰۰:۴۵ صدای مهیبی اومد، ما ابیوردی هستیم ولی صدای انفجار تا اینجا اومد
سلام همین الان حدود ساعت ۱۲:۴۵ شیراز صدای انفجار شدید اومد
سلام الان شیراز صدرا هستم صدای انفجار اومد
شیراز  0:45 صدای انفجار اومد
سمت فرهنگ شهریم ما
سلام ۰:۴۵ شیراز سمت شهرک گلستان صدا انفجار اومد
شیراز زدن نمیدونم کجا بود ولی من از فرهنگشهر شنیدم صداشو
سلام وحید جان  دکل مخابراتی کوه دراک شیراز رو با جنگده زدن ۰۰:۴۰
من رو پشت بام بودم دکل کوه دراک رو زدن
صدای جنگده اومد بعد زدن
خونه ما معمولا وقتی صنایع رو میزنه صداش نمیاد، این انفجار مشخص بود خیلی عمیق  و بزرگ بود که انقد واضح صداشو شنیدم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77328" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77327">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیام‌های دریافتی:
چابهار صدای جنگنده سطح پایین میاد الان
سلام صدای انفجار شدید در چابهار ۰۰:۰۲
۰۰:۰۶ دیقه صدای انفجار اومد کنارک انگار دور بود
چابهار ساعت 12 شب دوتا سنگین زد
🔄
چابهار دوباره صدا جنگنده :۶
انفجار سنگین :۰۷
الان زدن چابهار 12:07
چابهار الان صدای انفجار شدید
درود چابهار الان زدن خونه لرزید 00:07
دوتا دیگه هم زد
چابهار همین الان دوباره زد
انفجار خعلی سنگین ۱۲:۰۸
وحید ۰۰:۰۷ انفجار شدیدتر
کنارک همین الان صدای سه انفجار
سلام چابهار الان ۳ تا صدای انفجار اومد۰۰:۰۸
چابهار همین الان دوباره زد
۳ بار شد
🔄
صدای ۲ انفجار دیگه در کنارک
همین الان یکی دیکه چابهار
صدای انفجار دوباره در چابهار
صدا جت امام علی زد یکی ۱۲:۱۱
باز یکی دیگه زد همین دقیقه
پشت هم داره میزنه
جنگنده ها در ارتفاع پایین در حال پرواز هستند
داداش امامعلی چابهار رو مثل اینکه زدن
سلام آقا وحید طرف های امام علی نه خود [پایگاه] امام علی رو زد
دو تا چیز شبیه فلر از سمت دریا اومد چابهار
نمی‌دونم چی بودن
منابع حکومتی:
فرماندار ویژه چابهار از حمله هوایی دشمن به شهرهای کنارک و چابهار در بامداد سه‌شنبه خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77327" target="_blank">📅 00:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77326">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z1aT3pavZV-4fSK8xWdxhi8bI2jaO5TWDtqFt3P5h8PjuGxiz954AqXv9M9rFOfWBakyzVFjUmyMs9QAbvBg2A78dZfxuToOYYg0o9eEf59Z_1INvo0jw_aVXpgIDNM1j_dpaKU3s-dL_SRFwBUAlIqLwNCpIkII1NxVYeeSCPhiYdZDRYmz_3j5Um8vAGV8f6EPQ-plcgD7ZNDZIZw4h9QU8hNzxlHnAH6Sd5Ll9ajbYBCROGt5xM7RyFb6Y4lKrmfxqtMSXstbZ8y8w5Ovp0cY37MAgdxPfQ67L1_zddtNZsJFjDvSNVFNjzIKn3yMaLZUA8OqvZkJNxccrKzikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۴ بعدازظهر به وقت شرق آمریکا [۲۳:۳۰ به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور جدیدی از حملات علیه ایران را آغاز کردند. هدف از این حملات، تضعیف بیشتر توانمندی‌های نظامی ایران است که برای حمله به کشتیرانی تجاری در تنگه هرمز به کار گرفته می‌شوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77326" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77325">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیام‌های دریافتی:
صدای یک انفجار الان بندرعباس
صدای انفجار مهیب بندرعباس ساعت 22:33
همین الان ۱۱:۳۴ بندرعباس صدای انفجار شنیدم فکر کنم
سلام وحید جان ، بندرعباس صدا اومد الان
بندرعباس انفجار همین الان
سلام ساعت یازده ۲۳:۴۳ بندرعباس موج انفجار
انفجار در بندرعباس
بندر انفجار ۱۱.۳۴
ساعت ٢٣:٣۴ صدای انفجار نسبتا شدید بندرعباس
انفجار شدید بندرعباس ۲۳:۳۴
بندرعباس الان یدونه صدای انفجار اومد
بندرعباس ساعت ۲۳:۳۴ صدای انفجار شنیده شد
۱۱:۳۴ صدای انفجار بندرعباس
وحید سلام ساعت ۱۱:۳۵ بندرعباس یه انفجار خیلی شدید امد
بندرعباس صدای شدید انفجار همین الان 11:35 الهیه جنوبی
سلام صدای انفجار بندرعباس ۲۳:۳۵
بندرعباس الان صدا اومد تقریبا شدید بود
بندرعباس صدایییی وحشتنام ۲۳:۳۴ دقیقه دو تا انفجار
بندرعباس ۲۳و۳۵صدای انفجار اومد خیلی سنگین بود
سلام آقا وحید ساعت ۲۳:۳۴ دقیقه صدای انفجار اومد بندرعباس
ساعت ۲۳:۳۷ دقیقه یه صدای انفجار دیگه از سمت دریا اومد
یک ربع پیش از پیام‌های بندرعباس خبرگزاری فارس نوشته بود:
دقایقی پیش صدای چند انفجار از حوالی سیریک در شرق استان هرمزگان شنیده شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77325" target="_blank">📅 23:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77324">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vP3059sU7bwa1JDnEJ3JAxk8J8iYSGwGj9K5uT6YwPk6LgCwAiMdSypD06AAQ4GpkKYXtk-TbXDW5fUEOw_WzFtt-MfB6ur05EFQlDlJPguskMFrpNwBwoLA7r7gH9_Y2nJs9p3u1vPYFZ-4jsBVs61jyt_0HSvqc4r4ZEBnG2e1rF2cEEoDYy9iHTrqKB45h19LRpvHenXwoA5eszrlOITAU-NbZZFE1TtJHBwyN2TCI7Xv5Fi5hqCWitpM6_N-WIYOk2APCTF2XK9blla16UXdYijB46Y4O9ovK2JfJcYvM6Lx9VjQLn8o0G6Vt4aKqmuipQLj_aDXQX3s4kLY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب فارسی وزارت خارجه آمریکا شامگاه دوشنبه ۲۹ تیر با انتشار یک هشدار امنیتی از شهروندان آمریکایی خواست در پی افزایش تنش‌ها در خاورمیانه، هرچه سریع‌تر ایران را ترک کنند.
در این هشدار آمده است که وضعیت امنیتی منطقه همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
@
VahidHeadline
خبرنگار اکسیوس، ترجمه ماشین:
یک مقام آمریکایی درباره گفت‌وگوهای احتمالی آتش‌بس با ایران به من می‌گوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را به‌دلیل نقض تفاهم‌نامه و ادامه اقدامات تروریستی‌اش در تنگه هرمز مجازات کند. علاوه بر این، رئیس‌جمهور ایران را به‌دلیل کشته‌شدن اخیر سربازان آمریکایی مجازات خواهد کرد. این ضربات ویرانگر تا زمانی که رئیس‌جمهور صلاح بداند ادامه خواهد یافت، اما گفت‌وگوها میان دو کشورمان همچنان در جریان است.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77324" target="_blank">📅 23:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b98202fb7b.mp4?token=XDR-ctaaFKIp6BMiIAktKJtKJAKWC4Wp302z7AbY_LQcBR_zYKbHFspaXEwpcpGIzdRfbbDR_Ces08uthskXcvjiruX18zC_dAulGy0TorA8_BwOkTaAAl_lPO6u5H1Q7nCELL6rQQTifMZyT47AK8cK8JcPBF9VY-xeSflX58oWVrk7qohZ0QoNe1Evc6ePMauIjn2lLCXMaSDcpA4V67IMzRH2EhSIgtuHJgV0N5LhfXvXAt1Lvb89K-A_dIS3JMJcA53EVwYG3wCN3MD4Km23Z7J_K9c2WEnmSQZOeUC85WIxIYHZxebHpY8C3XV00aFqOsZJLvrofI3i0Xy7eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b98202fb7b.mp4?token=XDR-ctaaFKIp6BMiIAktKJtKJAKWC4Wp302z7AbY_LQcBR_zYKbHFspaXEwpcpGIzdRfbbDR_Ces08uthskXcvjiruX18zC_dAulGy0TorA8_BwOkTaAAl_lPO6u5H1Q7nCELL6rQQTifMZyT47AK8cK8JcPBF9VY-xeSflX58oWVrk7qohZ0QoNe1Evc6ePMauIjn2lLCXMaSDcpA4V67IMzRH2EhSIgtuHJgV0N5LhfXvXAt1Lvb89K-A_dIS3JMJcA53EVwYG3wCN3MD4Km23Z7J_K9c2WEnmSQZOeUC85WIxIYHZxebHpY8C3XV00aFqOsZJLvrofI3i0Xy7eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهرداد گودرزوند چگینی‌، نماینده شهرستان رودبار در مجلس شورای اسلامی می‌گوید که در تحولات اخیر، این ایران بوده که ابتدا توافق آتش‌بس میان ایران و آمریکا را نقض کرده است.
او در پاسخ به سوالی درباره توقف مذاکرات به دلیل نقض آتش‌بس گفت: نمی‌دانم گفتنش درست است یا نه اما اول ما حمله کردیم و بعد آنها سیریک را هدف قراردادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77323" target="_blank">📅 21:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82071ea2df.mov?token=GeHLEVQrKuJx4fMRG6poWA4x4RLKMVGYa8vSdmhA5axYqiwntwZgwD__MRVCp0mFp9rUm6Sc-qgUayFj-6H8jHu062A15StU_GS8usqY3aGNsUTZVImdledcJ41htJTd6J5ypfE-1U8lGT2jLfS-wFvs3sSQJ64_C6OreY1LHPNVSlisGO7kM7dA5yHkh-29WHkbqTX2yWPbV2grKQ6FUHG0DbUh6OX33DbTaxOfwLVJdYAldKl-92e4sCzxPdXCGxPqKNXlP0nNNuZKT7FtMIFjAGWf1EIbaTbPoGWCzLI9hFtBCE-X5z9AVOQy6qrRlJD5eYU27ZlbG6isOkXK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82071ea2df.mov?token=GeHLEVQrKuJx4fMRG6poWA4x4RLKMVGYa8vSdmhA5axYqiwntwZgwD__MRVCp0mFp9rUm6Sc-qgUayFj-6H8jHu062A15StU_GS8usqY3aGNsUTZVImdledcJ41htJTd6J5ypfE-1U8lGT2jLfS-wFvs3sSQJ64_C6OreY1LHPNVSlisGO7kM7dA5yHkh-29WHkbqTX2yWPbV2grKQ6FUHG0DbUh6OX33DbTaxOfwLVJdYAldKl-92e4sCzxPdXCGxPqKNXlP0nNNuZKT7FtMIFjAGWf1EIbaTbPoGWCzLI9hFtBCE-X5z9AVOQy6qrRlJD5eYU27ZlbG6isOkXK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: موشک‌هایی در آسمان ارومیه
آپدیت:
ارتش اردن شامگاه دوشنبه ۲۹ تیر حمله موشکی به این کشور را تایید و از رهگیری موشک‌های شلیک شده به سوی این کشور خبر داد و اعلام کرد که سه موشک از مبدا ایران که پادشاهی اردن را هدف قرار داده بودند، سرنگون کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77322" target="_blank">📅 21:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb11afb901.mp4?token=tckhSPZbxiGwJlG7t5CTbu9mq4FWVuk5kixiq9V-DUS5v7By_cGinMoGlBJ8QfBjPhMOcrIatnJAU2Bo7T64iAVCdB3cDQjmaREq3V-FH--OV3PR1GFS1pea00YAPR7-P6ZHEYA4Q-n5oL1PYchrODK7z7U32sWrPXCxVhwRZ569xYpCoLHhTqoqfWGBiG_2GrhmNycO5DhxXzu_HEQmAnAGzrSPHyX_tC2lBTrBTW9sYpPLhn_h5astCYHlf5HEtCdvQZQXmDOAlRNaDdtnvypsnXqWxBPxQ56uGeDSoEeEn7fdKFP5rlCJ5-0H_pHz6Bboveyhp2feMxHJXlENhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb11afb901.mp4?token=tckhSPZbxiGwJlG7t5CTbu9mq4FWVuk5kixiq9V-DUS5v7By_cGinMoGlBJ8QfBjPhMOcrIatnJAU2Bo7T64iAVCdB3cDQjmaREq3V-FH--OV3PR1GFS1pea00YAPR7-P6ZHEYA4Q-n5oL1PYchrODK7z7U32sWrPXCxVhwRZ569xYpCoLHhTqoqfWGBiG_2GrhmNycO5DhxXzu_HEQmAnAGzrSPHyX_tC2lBTrBTW9sYpPLhn_h5astCYHlf5HEtCdvQZQXmDOAlRNaDdtnvypsnXqWxBPxQ56uGeDSoEeEn7fdKFP5rlCJ5-0H_pHz6Bboveyhp2feMxHJXlENhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره پرتاب موشک از تبریز
ویدیوی بالا: شلیک موشک از [...] تبریز ساعت ۲۱:۲۴
صداشنیدم تبریز موشک زدن 9:25
میگن از [...] بلند شده
همین الان از [...] تبریز ۲ تا موشک فرستادن. ۲۱.۲۵
همین الان دوتا موشک از تبریز فرستادن  21:24
از تبریز دو تا موشک شلیک شد الان
صدای شلیک موشک ساعت ۲۱:۲۵ از تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77321" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c8221ff7b.mp4?token=DruQvSgBikR814iK6gPujcy0hgyrxggXKrrI5ELIOPpgrboavFiTaHPxN06d0w_7Qxg21MlQzRhk_WnaGGRouPw8qLj_1K825scMbKphMjI5FNbCRcLH-Skiiek_XuKA7V8-LHG4XSXyo0yvnbNjSCzpwqEBXc6KABv0eqdL-CsVHB2WVW4DlVsKQNMaVzWIvozgKgGqFFcpkypxuwlfG_OjYaxg82OLipX2qAySS1vcex-DwwQ8p700KnhCpyif4YW2fkAn2QoFEey8TKNbZD3jFvquWY9wtMlBCLL530HkkvzfxyfM63g-0tLF_tm8zyxC4kl37omcb0JnXYL_FYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c8221ff7b.mp4?token=DruQvSgBikR814iK6gPujcy0hgyrxggXKrrI5ELIOPpgrboavFiTaHPxN06d0w_7Qxg21MlQzRhk_WnaGGRouPw8qLj_1K825scMbKphMjI5FNbCRcLH-Skiiek_XuKA7V8-LHG4XSXyo0yvnbNjSCzpwqEBXc6KABv0eqdL-CsVHB2WVW4DlVsKQNMaVzWIvozgKgGqFFcpkypxuwlfG_OjYaxg82OLipX2qAySS1vcex-DwwQ8p700KnhCpyif4YW2fkAn2QoFEey8TKNbZD3jFvquWY9wtMlBCLL530HkkvzfxyfM63g-0tLF_tm8zyxC4kl37omcb0JnXYL_FYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل‌ها و پل‌های تخریب شده در حملات آمریکا، روی نقشه
در جریان حملات اخیر آمریکا که عمدتا بر جنوب ایران متمرکز شده، چند پل و یک تونل و یک ایستگاه انشعاب راه‌آهن در استان هرمزگان هدف قرار گرفت که خسارات جدی وارد کرد.
این پل‌ها و تونل در مسیرهای دسترسی استان هرمزگان به استان‌های فارس و کرمان قرار دارد و تخریب آنها باعث توقف تردد در مسیرهای بندرعباس به سمت شیراز و همچنین استان کرمان شد.
تونل شهید میرزایی در محدوده گلوگاه در مسیر بندرعباس به سمت حاجی آباد یک روز بعد از تخریب هر دو دهانه رفت و برگشت باز شد. در مسیرهای دیگر که پل‌ها هدف قرار گرفت، مسیرهای جانبی پل‌ها به طور موقت مورد استفاده قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77320" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77319">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/an9BtjLouro3fQ3FLvdT9bXBHneJuKIxO74nHy1KorNEiyNih4HWezJCFQVMewazsGgC4JieD8EhF-HnDbs88IbZuen9jsbnrh72iIXylyhg5eUBx6Q7kjUbzvUPmWr-d59Q42PhtREQA7SaqOiElbf-eerGngxY4hH5YP-QSojKe9ajcMShYBJ7GhCOdMDfJY0-1H4YXSbfxv9K4QOqtX6LnBSOsFU_LpDyptbSo4sBawHKHufFDOmyEbDTNIjigw_38oxeH3u69iRLFITGySPcJGOk8hnD6qm0c0P-wecTXr_GYT_3oG8CF8DbMmxw2bL8jfrUEAm2ptzbY_xRIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین برابر خواهد پرداخت! این دستور به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک ارتش، و تمامی فرماندهان نظامی ابلاغ شده است.
رئیس‌جمهور دونالد جی. ترامپ
Every time Iran kills an American Soldier they will pay for that killing many times over! This directive has been passed on to Secretary of War, Pete Hegseth, Chairman of the Joint Chiefs of Staff, Daniel Caine, and every Leader in the Military. President DONALD J. TRUMP
realDonaldTrump
ترامپ در پستی دیگر نوشت:
بنیامین نتانیاهو تحت هیچ شرایطی، به هیچ شکل و طریقی، در ایالات متحده آمریکا بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را کشته و طی ۴۷ سال گذشته سربازان آمریکایی و دیگران را به قتل رسانده است.
تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این
چرخه بی‌سابقه مرگ و ویرانی
کشاندند؛ موضوعی که رؤسای‌جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!
رئیس‌جمهور دونالد جی. ترامپ
Benjamin Netanyahu will not be arrested, in any way, shape, or form, while in the United States of America. He is fighting against the Islamic Republic of Iran, which recently killed 52,000 innocent protestors, and has spent the last 47 years killing American Soldiers, and others. The only ones that should be arrested are the people that led Iran into this unprecedented SPIRAL OF DEATH AND DESTRUCTION, something that should have been dealt with years ago, by previous Presidents! President DONALD J. TRUMP
realDonaldTrump
پیش‌تر:
زهران ممدانی، شهردار نیویورک، اعلام کرد در حال بررسی امکان بازداشت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در صورت سفر به این شهر برای شرکت در مجمع عمومی سازمان ملل متحد در پاییز امسال است. ... @
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77319" target="_blank">📅 20:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/upvdVTwuLtErvnFqURTTxzwBrXRtI_V9NCE94mv8H4MAVQ5e2J0TCemIgO8v6Zn9ps1oswrXVY5sB4cKl81fDuZQ6796tjmQ6G1q3gJEG1Roac5pnSZOuMssbTAx5LLy4WypruxRLcHKz7wLtHymRyDdiaVObZGfnWgTXSmCLK5H_dyVaEQbUDU9pzh_BDPVex1INFD-yDSW5AU2AyKqC_XhC1EbAxYWy3phLkGhEGpovcNvUolq42bq5ZKnhgmOyEp1d5vKSzWRFFaOB7e65mjFH55IEVCCoSuVrMko70gApMOnGZ3cxmBr_2cUyAVXFP007aomT43GHaJXVwHNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند پیام دریافتی تاییدنشده با مضمون: کارخانه نخ شهرستان خمین رو هدف قرار دادند.
هم‌زمان منابع حکومتی:
یک واحد صنعتی در حومه شهر خمین هدف حمله دشمن قرار گرفت
معاون سیاسی امنیتی استانداری مرکزی در گفتگو با خبرگزاری صداوسیما: این حمله حوالی ساعت ۱۹ روی داد که تلفات جانی در پی نداشت و خسارات احتمالی در دست بررسی است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77318" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhRBC-dB6hJXgUrhaKHyiMhz7kTqFPgURJen8oT3aurO1DM9CA_2Q66CgwBYBDuxhaYlT7yBCNaNOLwe5neEmunfgINh6oEp33ZsCMM6UliX2Ou7qA8mkjatnAVnjd2L_eUMiavvEoomPF_mwbD4oKQz1yzcleWstRiSHrVefyIwxrZ9-dGCqPg6w8OT185m08j1Eu7k-OcJW9wVjezCcUrujr0QrZo8fOecfOVTfsp6a-DYluC_8gGUmmguLrkVdc97AkE-CbcZcg3RZPskUA11m6SeNOQRSEmRLyCRF2iPN686lpiHm_XzACbkoxxP40tW9Oyu3bNzS6nev76w4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژان نوئل بارو، وزیر خارجه فرانسه، در شبکه ایکس اعلام کرد که دو نفر از کارکنان سفارت این کشور یک‌شنبه از سوی نیروهای امنیتی جمهوری اسلامی مورد «تهدید و رفتار ارعاب‌آمیز شدید» قرار گرفتند.
بارو گفت این اقدام نقض آشکار مصونیت‌های دیپلماتیکی است که این افراد از آن برخوردارند.
وزیر خارجه فرانسه افزود: «آن‌ها بدون هیچ دلیلی برای چندین ساعت بازداشت بودند و مورد بازجویی قرار گرفتند و یکی از آن‌ها نیز مورد ضرب‌وشتم قرار گرفت.»
او گفت: «آنها سرانجام توانستند به سفارت برگردند و اکنون در آنجا در امنیت به سر می‌برند تا در ساعات آینده به فرانسه بازگردند.»
بارو تاکید کرد به عباس عراقچی، وزیر خارجه جمهوری اسلامی، اطلاع داده‌ که «این تعرض غیرقابل‌قبول به سلامت و امنیت کارکنان ما، بدون پیامد نخواهد ماند».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77317" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOfKCFlgPxaWWdRC0aCmn79viESxxFuTyCZMZMtUvcyGUDzVswcg42yldjwhUxOFA7MnXIuLkyuIE1LK4XgIs2EU4t3FbCJ4HzJGBlxwYBU3uOSbM1UnDsFBReXldMcY8hzpnhCRIHGHepvfD8xeLEWdQUo20DfokXTsH-WBLRlL702fLRnQwdOWvn1XVMp-5HEO02W0-MouPyyzFUY_cSQOscAmKbGoNHbpmuFdYxlH4Hbdc7-VkjCOCfsqE3Dig99IQN8u3Yw0-u9qbH_8FfwSf8JKS4KfTyncyNhGQJ1Zry0xnGKRX13iLcLT7-ZC2hwCc_IYBB3svTxoYjjDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز، ترجمه ماشین:
خبر فوری: پنتاگون تصویری از سرباز ایزابلا گونزالس، نظامی ۱۹ ساله آمریکایی اهل کارولتونِ تگزاس، منتشر کرده است که در حملات موشک‌های بالستیک و پهپادی ایران در آخر هفته کشته شد.
گونزالس در حال پشتیبانی از مأموریت آمریکا علیه گروه «دولت اسلامی» بود که هنگام کمک به دفاع در برابر حملات ورودی ایران کشته شد.
مرگ او در حالی رخ می‌دهد که درگیری‌ها در سراسر خاورمیانه همچنان شدت می‌گیرد.
نیروهای آمریکایی نهمین شب متوالی حملات تلافی‌جویانه علیه اهداف ایرانی را آغاز کردند؛ در حالی که دو کشور همچنان برای کنترل تنگه هرمز با یکدیگر می‌جنگند.
FoxNews
آپدیت:
خبر فوری: رئیس‌جمهور ترامپ در مراسم انتقال رسمی و با احترام پیکر دو سربازی که در حملات ایران در اردن کشته شدند، شرکت خواهد کرد. این مراسم فردا شب در پایگاه نیروی هوایی دوور برگزار می‌شود.
کارولین لیویت، سخنگوی کاخ سفید، در پستی در شبکه ایکس نوشت: «رئیس‌جمهور و تمامی اعضای کاخ سفید برای خانواده‌های آنان دعا می‌کنند.»
رئیس‌جمهور نیز در پستی در تروث سوشال نوشت: «هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین برابر خواهد پرداخت»؛ در حالی که آمریکا به کارزار نظامی خود در خاورمیانه ادامه می‌دهد.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77316" target="_blank">📅 19:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6cac939191.mp4?token=o_p4KYpSUr3n4hbJPSjhNKNu-3LeYWn6-dlFIMx3YhPwtNkhZgd1Stg5H-r4qhoPWWSUFwi7OhKduNSPcIPJugp-yZjUP6nUgpzwYutRdOY4jgJ-z54JkZXJsmNjj_5MnKqI9pYt9yJe82gp_enGrFdQ_C4fA8a7r8bM9AQEurjiIj7nWMF_s5B_1JC6vFAYu4eJgSxKOXWDxJpVSxbwmKadasCs6EvUAjVusfqDDfTIWAGlabZcUdo-_02ceSO2OKZ5CImnc41RBrIIxNMhICKVUTX9dbfAbLmN7_A1d8We9-YQuNampyWmDtE40ErAINajt3zt23X5-x9--qZHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6cac939191.mp4?token=o_p4KYpSUr3n4hbJPSjhNKNu-3LeYWn6-dlFIMx3YhPwtNkhZgd1Stg5H-r4qhoPWWSUFwi7OhKduNSPcIPJugp-yZjUP6nUgpzwYutRdOY4jgJ-z54JkZXJsmNjj_5MnKqI9pYt9yJe82gp_enGrFdQ_C4fA8a7r8bM9AQEurjiIj7nWMF_s5B_1JC6vFAYu4eJgSxKOXWDxJpVSxbwmKadasCs6EvUAjVusfqDDfTIWAGlabZcUdo-_02ceSO2OKZ5CImnc41RBrIIxNMhICKVUTX9dbfAbLmN7_A1d8We9-YQuNampyWmDtE40ErAINajt3zt23X5-x9--qZHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پیام‌ها و تصاویر دریافتی: پرتاب موشک از حوالی لار در استان فارس، دوشنبه ۲۹ تیر حدود ساعت ۱۹'
هم‌زمان: پیام‌های دریافتی از صدور هشدار در بحرین
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77315" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رسانه‌های داخل ایران از پلمب چند کافه و رستوران در مرکز شهر تهران خبر داده‌اند.
براساس این گزارش‌ها جو کافه، ۱۴۰۱، سام‌کافه، دو بار، نووک و تئوری در خیابان‌های سنایی و ایرانشهر پلمب‌ شده‌اند.
وبسایت امتداد نوشت که به هریک از این کافه‌ها دلیل متفاوتی ارائه شده است از جمله «حجاب، داشتن ساندویچ در منو و صندلی در پیاده‌رو».
پلمب کافه‌ها و رستوران‌ها به دلایلی مثل حجاب یا موسیقی زنده سابقه طولانی دارد.
@
VahidHeadline
پیام دریافتی به همراه تصویر یک حکم:
چهارشنبه (چندروز پیش) به ۹ تا کافه داخل اکباتان فاز یک حکم پلمب دادند بدون هیچ توجیهی (فقط گفتن حجاب رعایت نشد) و همه کافه ها رو پلمب کردن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77313" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77312">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhrTRIKOdB18-xJaEXvoJbRS2F5oQAzUaS-eNA8C9u38Vlyln_sfdJ9o5APrI2sxheV04Qr97hCAfgTZ7-wDuVYGQq8p2aF2UVRaKlqKpKQWvZC0dn8duAoJPhoSx6wLhCJ8pSBw22KQy7co9QbID1Zff5mE_vwcAXsY_dQlzNGSezvRs10c6Mc8jhSpLZBj23g5HH521Vy-_YW5a-bH0qYratM-Av4_loYEemxSVGb8E32Mh7USkdLcG3jsdufSVzuiyjwg60iWk3_FQZlmUq9_LssEA_MKjBZF0R384Xy86jByfr1ECjvU4gLVsKAly7WmeiVbvEExl342hr-Mrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسکندر مومنی»، وزیر کشور جمهوری اسلامی، در راس هیاتی از نمایندگان دستگاه‌های اجرایی، به دعوت همتای پاکستانی خود عازم اسلام‌آباد شد.
رسانه‌های ایران روز دوشنبه ۲۹تیر۱۴۰۵ گزارش دادند که هدف از این سفر، بررسی راه‌های توسعه همکاری‌های دوجانبه میان ایران و پاکستان است. جزییات بیشتری درباره برنامه دیدارها و محورهای مذاکرات وزیر کشور جمهوری اسلامی منتشر نشده است.
سفر مومنی به اسلام‌آباد در حالی انجام می‌شود که وزارت خارجه جمهوری اسلامی ساعاتی پیش دریافت پیشنهادهایی از سوی کشورهای میانجی برای توقف درگیری‌ها را تایید کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77312" target="_blank">📅 18:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To_pBb3U0E4sCwqZxtr8u0o2pIqIPYyJiwjG9qMHdI4j4WjuCbsWZychbeivIswqHdMLfUTSLlO8h-o5FhsseU2658HqJ16Dej_yN_NdDjYc-BNzesmOv5hWUfD7vF8NI_Qir2UaWHHmNa1BrcuRVh-pm4Ly_DYqmfj5isbb-SE1z6aw1pvDBV4XzKgFrxc7mswDoogKl_NAEsSNI2CUh9u-3NXZau_jfL_f5Lqo3TzY3sPfS8uFiMd579dKEYMQ37sLFP4xSeDvqeh1gFhkaHEO3XYEXTTBJqUCMTUSssYlCVcvlyouQhU0ZzsGLMECKZkjU0L-P36QHIuUcVzExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدباقر قالیباف»، رییس مجلس شورای اسلامی، با انتقاد از سیاست‌های آمریکا در منطقه، با انتشار پستی در حساب «ایکس» خود نوشته است که واشینگتن هم‌زمان با ادعای تلاش برای توقف جنگ، به انتقال تجهیزات نظامی جدید به منطقه ادامه می‌دهد.
قالیباف در پیامی که دوشنبه ۲۹تیر۱۴۰۵ منتشر کرده، نوشته است: «آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند.»
رییس مجلس شورای اسلامی همچنین با اشاره به آنچه «آمریکایی‌بازی‌ها» خواند، نوشته است: «آمریکایی‌ها روی هوش ما اندازه آی‌کیوی مختصر خودشان حساب کرده‌اند. جمهوری اسلامی در شناخت این رفتارها «به مرحله استاد تمامی رسیده و بر همین اساس برای مواجهه با آن آماده شده است.»
قالیباف در پایان نوشته که اقدامات باید موید ادعاها باشد، نه ناقض آن‌ها.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77311" target="_blank">📅 18:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77310">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKGY3E4U1wnH7_sayYx5V7AjFpzAzGyA1EVlQYkruSFAVx8EdF15ewfVu-GMD2j2a7fBaEMRMVTjhD5_PDrohgQAT6JRRw-auOJ_kGHh5W4Ik2zzNB-5LqIv39B0Sm0Yf6bmIf3e3D-MkQjee-P699SlryPQJqcKRG0Midk2LGW6FJ5rc9JJZEHwp0k609iaWuxS8lN8q9FY5tJOiKnUnUMhwdUowpnuUN_0RBAdSTCJ3-G1W9xkkceRQD5JFfUzgUDwj-4TBc6BYgvan0XM1nArzI8ggTXGbN1MyFIlwngpCHlLAfasIQ-NYNovCzZEt80oxCjwh0qSpvJan1ADyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت کشتیرانی یونانی «دایناکام تنکرز» همزمان با بالا گرفتن درگیری‌ها میان ایران و آمریکا در منطقه اعلام کرد که دو نفتکش تحت مدیریت این شرکت روز دوشنبه هنگام عبور در آب‌های ساحلی عمان، هدف پرتابه‌هایی با منشأ نامشخص قرار گرفتند.
شرکت دایناکام اعلام کرد نفتکش «کاوومیلیز» با پرچم مالت هدف دو پرتابه قرار گرفت که باعث آتش‌سوزی در اتاق موتور آن شد و خدمه را ناچار به ترک کشتی کرد.
این شرکت در بیانیه‌ای گفت: «پس از فعال شدن سامانه اطفای حریق کشتی، ناخدا تصمیم گرفت کشتی را تخلیه کند.»
دایناکام افزود که تمامی خدمه توسط مقام‌های عمانی به سلامت پیدا شده و به ساحل منتقل شدند و این شرکت در تماس نزدیک با همه مقام‌های ذی‌ربط منطقه‌ای قرار دارد.
شرکت بریتانیایی مدیریت ریسک دریایی ونگارد اعلام کرد این حادثه زمانی رخ داد که کشتی در فاصله حدود هشت مایل دریایی در شمال‌غربی کُمزار عمان در حال عبور بود.
سازمان عملیات تجارت دریایی بریتانیا که پیش‌تر گزارش داده بود این کشتی دچار آتش‌سوزی شده است، اعلام کرد هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77310" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gv1zqwQe_gthVbZpGFpiY74z42NadH9-EcL_4w-AkYWLLnsHDwz55qrqojuzqYzgx1OJIQXm2YLPhdkOv_dRnujY3T1brK2S4iLArCknfSQoEm9p0Zn4Od4xgeZK7_vFDDwNKMLO-6GS9-w1k-lDMD_zzN0e-ouWBkxquVpSRFoVPRtT7XnEmlcLkpMvDNFujw9NCGKoHbF6B9EctMiG-2uXlRu6IVhDekcAisiz416mszK-P6RKf-eR4gorahYLihb3dZsMkxRMdrXbCNhOtBlQcZQDGXwYR080sXzbW6Bh6DRMnM6hGLEt8q9e0Zt3YLVgneZurIZRXx2U6-xu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E810zijvVrWyg3rheJ37kTUtovQ6eV_YsJ1IywvZhe4UVi6SYTG35nJEgWMYhBhUZBEi9S9VyCMPRm0sHD_3AODHflLmdj8mNqc7myk1KBm3VlFD9Jln2DL7FONBsXMcl8hXlVI067vq7dR8a15_z0zj5_KjiIlG7ksTupQ-_2Bsj8hFiVE3atpykgEMwy84DF8owHu111RRaAyWNzykpWbQY6Aw3KWcC49POtF-BoW49VYvm3pBgY4sTBhz01rwkUyjWpqDjPo9X4SwhdHFTRzkvEItI_FObnpWHIm7EkAqsc_5uWp-2Yx4-_9RjDpD2Y-AEYDkzFHeXKxKa_5NMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری رویترز به نقل از یک مقام ارشد جمهوری اسلامی گزارش داد که میانجی‌ها پیشنهادی را به جمهوری اسلامی ارائه کرده‌اند که هدف آن کاهش تنش در جنگ با آمریکا است.
بر اساس این گزارش، این پیشنهاد شامل یک آتش‌بس ۱۰ روزه برای یافتن راه‌هایی جهت احیای تفاهم‌نامه میان جمهوری اسلامی و آمریکاست که ماه گذشته حاصل شده بود.
پیشتر سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد که پیشنهادهایی از طریق میانجی‌ها دریافت کرده است. این اظهارات در بحبوحه تنش‌های نظامی میان آمریکا و جمهوری اسلامی مطرح شده است.
اسماعیل بقائی روز دوشنبه در یک نشست خبری بدون ارائه جزئیات افزود: «اصل موضوع که در این روزها ایده‌هایی از سوی برخی میانجی‌ها به جمهوری اسلامی واصل شده، تأیید می‌شود.»
تنش‌های اخیر پس از حملات جمهوری اسلامی به کشتی‌های تجاری در تنگه هرمز آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77308" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چند پست بعدی مربوط به ساعت‌های گذشته هستند.</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77307" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tc9YJnoaGXgzmtI8fvkqP4eUcdr-HQ5WAU81tPJbQQN1Dr4TWL9TH_2NywWKa1g190rFxEMA9A86gTFHvaavWRYXDrDoSVbwxYzLUF8UKnGcH7Omxj2ocU_81Qfz6egu38QDKojCTUwOGw8Bgo9CZr4qn6Tf6xj8ek59BFGD5T0ambV8c8Bu6bfH6l2ThsP9jkWdkVAlz1KrMGVwB6cG8PXI0tl_OYX_TmEoGz_I2amx6DBsHZCVGeuV5wOS3Vn6KSuvreyirkWFWfSX9hRbZFd5_Ej2Xk05w3hp9wAckY6UtD2OBGRIHlSElphxCsw7CRnsnaBt9MrZB8U8D9-Ulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mLC1BEfqbYmwbwWZHENhdXRqIHYN1R9tpvkNxhFnIH5MK3V36_Vkzrgo1olOu_Ivcpxjq4AyLrIQ8DQgFSdSH-fFRDJLzjVura8NkQo2u6LHAaXBQIcpmOQ1NjP7QNLkfmx2n1Ioc-CXjWCDypoDzeGhSxrGTHmdzieUePnjGXXfuyCLN1FOtSEXIYU9z6rsjdaZ06vQqY9eWHUy_bfQLSbTNfSuMzJG80tBNz9Qv_qHMyJhwts1hX9ePU2ERFbg9Iz50CZYUMyWpGzREKOCqNDg_JBNmzTISs4vRs3K3ySrurbkyj0cTxTSB5GF7A3L6Bto0GnDicGuAlstruUC1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
اسمون شیراز الان
ساعت ۱۸:۲۵ از شیراز موشک شلیک شد
سلام وجید جان شلیک موشک از شیراز 18:17
درود وحید جان
۵دقیقه پیش از شیراز موشک زدن
[بعدش کلی تصویر مشابه دیگه اومد که دیگه پست نمی‌کنم]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77305" target="_blank">📅 18:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tuW2Coojd3C6BPANFdiwt1MtZJxZ-Ae2MQTEdbCebYxdOutflbTG0dy3sJDHXpRyRpXIA5kp-Dw9qXEmdIqGA3_iNqlF6gghL7FTlGyeEGBTyOorZQGqVP5Ujc8mF0iRrAQdegwu4U69FFUgYtHPxPeU5nrmFbsMBckayb7BoYuZpDGB46C9J9gx2Vha1_Mm7pIlxPbTNJwE2GKtOwj8vuDS681sJFuqBtHx3OBMSzyXTN-PSXS_y2EXt91uTTPoXQR7odOaaBdgGcC9Sa6ZIZVWkDBUHtl5gfpVmhZLNnoIHx6NF8mOpmTT4HWSTcf54j5hgoLnAHGkq564hYC_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KWN0fxzLu2oJlfGhRkkiQP4iGUfmSCwQKMciFgEdaVH00MHvBBsj5wEpFPQ4KkzVltfFW8Hrd18ypehHQKzR_N4xfIyjCwPYZbUxEyAi6p7dyjt-97LlqAHqEbcC9yCo6XVuKvrAxpXGEeoXlPY27aW5h1Wrxt_0bEkPGPL_M_0phUrdkgK7r3ejjRWlI_Gzh_4xfYiKF4G7WXnzTdnJyQDfZU3jKGiRegssFPGSnQ9fdzJRl6Jnhw_oObx0NVfkzadOYV1KKv9P6111NO8Vxm85zl5tkHOxphqq7PhjT9uvhs2cSY5JgQaA7O8NJaI4tG-yxBXNo4fNvFdXCmcSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FpDkXDzmtpf7-LVyajJt26Xss7jbcq9XqqBDLWOT0jqA4bq1X9s276JqyPaBX4-RTrFJYMhjPBIh3hTkEg5TQ2FgsxLcwhn9yXj5iut4-7nyHpO6ONq3bTqoYHB1Km2YvhyeHFVEX5st12Gkgq7XVqWOlDYrIf89JN5II9GeBpvFFY1Aryb2x4LXyHlHt5a8ulzL8ORkzbJ7-sXB9L6KIKXrNEvmpnmSVbWIL3jZXtH5yzk-TnvVWTZn8YKvmYZgzwgDMeCeZHeDQmFQy9WsKmMAW9Eq0lSYVLFh2qIOX9sntXqAas0feSFSV6hBcYi9jypaeOi_C_51Eyc9yRpZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EptkysY0m_uN5SecUexHNdJMUr-QEBlaircIvDzUeCb1SgiWTWLIfXxSB5TWaDF6RSS6Itz0KqX0xMkH1pRreCUCAWjAGn0VkauDRTd55u4V2cOcQVl4YChLsQk4GHQDCFYF-4ppQ_lEbEGoBsUhbYRfsNSrEV0RSzMjTlJKBVWX_S17UAAM8mBu87f4jLjnseeyFa5tJ3Qo-U_Sc8ho7pe4apMvztQq7veEcuOXycUxKQt_TDMA6vD1sjI6TOWNO4DF2AcXwT4q1l8EXUrH09MAkyJPn1lU2THp6YMWL-N41fyl7zul_jNbEOGJamosrfZwZVdF3xuhDuxRMpRz6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی از شیراز پس از دریافت پیام‌ها درباره 'شنیده شدن صدای انفجار سمت صنایع الکترونیک'
دوشنبه ۲۹ تیر حدود ساعت ۱۷:۱۰
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77301" target="_blank">📅 18:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شیراز، پیام‌های دریافتی از ساعت ۱۷:۰۶
سلام ساعت ۱۷:۰۶ شیراز ،صنایع الکترونیک زدن صدا انفجار لرزوند
صاایران شیراز رو زد پنج دقیقه پیش
صدای انفجار و دود
صنایع شیراز
ساعت پنج
سلام وحید جان من شیراز هستم همین الان سمت تاچارا و معالی اباد صدای انفجار شدید اومد فکنم صنايع الکترونیک بود
سلام وحید جان. شیراز ما خونه‌مون نزدیک محدوده صنایع هست. ساعت ۵ صدای انفجار اومد. نمی‌دونم زدن یا موشک پرتاب کردن، ولی صدای انفجار بود.
سلام وحید جان ساعت ۱۷:۰۷ شیراز سمت صنایع صدا اومد
مطمئن نیستم افنجار بود یا دقیقا از کجا بود
ولی صدای بلندی بود
شیراز صنایع رو زدن  ۱۷.۱۶ دقیقه
وحید ساعت حدودا ۵:۱۵ عصر صنایع الکتریک شیراز صدای انفجار اومد دود بلند شد
شیراز صنایع رو زدن انفجار
صنایع الکترونیک شیراز و زدن
سلام شیراز صدای انفجار حدودای ۵وربع سمت صنایع
آپدیت:‌ منابع حکومتی
شنیده‌شدن صدای انفجار در شیراز
دقایقی پیش اهالی بخش‌هایی از شهر شیراز صدای انفجار از محدوده شمال غرب این شهر شنیدند.
خبرهای اولیه از حمله به یک نقطه در شهر در جریان این حملۀ هوایی دشمن حکایت دارد.
به گفته استانداری فارس، این حادثه هیچ گونه خسارت جانی درپی نداشته و تیم‌های ارزیاب در محل حادثه حضور یافته‌اند.
📍
میگن اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77300" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BCHjSXVKtewAvbW7-iHykLgM29VdCA3D-OHtSF9CuO_Ly0QAdLurtz-P0uJqyb3Sv3QyN1m4a1QaM1PjvrF7bJg2XC4gu38WUy3yFVz2Rgzsb71HF6C8PbzuViEaJoAVBgpkPHj0MpizTARcoql_qiY8upwpQSSTX5ZpAtZ3ZL1Nw3IJkonjIGedUAgdmvJ8fdwYeZGn-Gj_vuYyolzxpfJpiM0klb-wlmRVaeRVLNFf39RHtiJsPHaKNm1dg9kIj7-0Kdkw3lq9dxRDeb8ODxJb-Ut3pIxgUPwjxQ_B-BTVX4eOq3SVgQu1sFs4jjsW2uj0aVpvSmznyefw9mGxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ها در کرمانشاه!
آپدیت: دو زلزله به بزرگی ۵٫۲ و ۵٫۷
📍
در عمق ۸ تا ۱۳ کیلومتری
کوزران
پیام‌های دریافتی:
الان کرمانشاه هستیم
کل خونه لرزید
زلزله بود
سلام وحید همین الان زلزله اومد تو ایلام
کامیاران سنندج زلزله هنوزم پس لرزه میاد
خیلی بد زلزله اومد
کرمانشاه
کل خونه لرزید
اینجا جوانرودزلزلە اومد شدید بود
سلام ایلام حدود ۱۰ ثانیه خیلی بد لرزید
سلام وحید، زلزله سنندجم حس شد
سلام وحید همین الان ایوان غرب زلزله آمد خیلی شدید بود
کرمانشاه زلزله اومد
درود کرمانشاه چند ثانیه به شدت لرزید کاملا حس شد
سلام وقتتون بخیر همین الان زلزله اومد استان همدان ملایر ۷:۱۵
زلزله نسبتاً شدیدی سمت کرمانشاه اومد
همدان هم ۳ الی ۴ ثانیه لرزید
سلام همین الان زمین لرزه اومد جوانرود استان کرمانشاه
سلام اقا وحید، ما پاوه هستیم تو کرمانشاه خیلی بد لرزیدیم معلوم نبود زلزله‌ بود یا چی. از شدت لرزش زیاد از خواب پریدیم. ساعت تقریبا ۷:۱۴ صبح
کرمانشاه اسلام اباد غرب زلزله شدید
سلام کرمانشاه خیلی شدید لرزید حدود ۶. ۷ ثانیه
سلام من کرمانشاهم حدود ۱۰ ثانیه شایدم کمی بیشتر کل خونه لرزید
آقا وحید ما مرز مهران هستیم، استان ایلام اینجا هم لرزید ساعت 7:15دقیقه
🔄
دوباره لرزیدددد
یا خداا بازم
دوباره اومد
دوباره ایوان داره می‌لرزه
وحید خیلی شدیده
وحید بازم داره زلزله میاد، ایلام
همین الان سروآباد استان کردستان لرزید
همین الان ۷:۱۹ هم پس لرزه‌ش اومد
پشت سر هم زلزله بالای 10 دیقه کامیاران داره پس لرزه
سلام وحید جان
مریوان دوبار اومد ۷:۱۴ و ۷:۱۹
وای دوباره اومد اینقد شدید بود
سلام وحید دوباره کرمانشاه لرزید خیلی شدید تر و طولانی تر
سلام ایلام دوباره لرزید
۳ ۴ دقیقه پیش پاوه لرزید
یه دقیقه پیشم لرزید و قوی‌تر بود
درود دو مرتبه پشت سر هم داره زلزله میاد هنوزم ادامه داره
خرم اباد ساعت 7/20
همدان دوباره بدتر لرزید
کرمانشاه زلزله بود
همین الان کرمانشاه زلزله خیلی قویی امد
کرمانشاه بازم زلزله شدید و طولانی
سلام آقا وحید کرمانشاه زلزله قبلی حس نکردیم الان ۷:۲۰ خیلی شدید و طولانی لرزید
ساعت ۷:۲۰ همدان لرزید
زلزله بود
اراک همین الان ۷:۲۰
چنننند ثانیه لرزید
سلام 7:20 اراک خونه لرزید در حد تکون شدید
همدان الان کاملا لرزید برای زلزله
قوی بود
وای ایلام بد لرزید
عجبيه اين زلزله خرم آباد حس شد
جالب اينه چقد ادامه داشت
سلام وحید خرم اباد لرزید خیلی کم لرزید
سلام،همین الان پشت سرهم دو بار زلزله اومد همه مون از خواب بیدار شدیم،جوانرود
نهاوندم لرزید خیلی عجیب بود
دوباره کرمانشاه زلزله،
از دفعه اول طولانی‌تر بود
۷:۱۸
زلزله شدید دوباره کرمانشاه
سلام وحیدجان همین الان اراک لرزید چهار پنج ثانیه شدید بود مثل گعواره خونه میلرزید چه خبره همه جای ایران میلرزه...
سلام وحید ..زلزله خفیف ساعت ۷:۲۰ همدان
همدان شدید لرزید چند سال بود چنین زلزله ایی نیومده بود
وحید جان سلام
اینجا الشتر، لرستان، ساعت 7:19صبح لرزید و قشنگ حس کردم لرزش زمین رو
سلام وحید جان ۷و۱۷دقیقه ب مدت۶ثانیه زلزله خیلی شدید از کرمانشاه همه رو از خواب بیدار کرد
کرمانشاه با زلزله بیدارشدیم
سلام وحید جان زلزله خیلی شدید همین الان کرمانشاه
سلام داداش کرمانشاه برای چند ثانیه وحشتناک لرزید
سلام بروجرد هفت و بیست دقیقه لرزید
سلام ساعت ۷:۲۱ همدان شهر همدان یه زلزله خفیف اومد
سلام بروجرد هم زلزله اومد
زلزله یا چیزی شبیه به آن در خرم آباد احساس شد
کرمانشاه زلزله وحشتناک اومد خیلی شدید بود
کرمانشاه زلزله آمد
منم قروه کردستانم
خونه یه ذره لرزید
آپدیت:
گزارش مقدماتی زمین‌لرزه
زلزله به بزرگی ۵.۲ در استان کرمانشاه
مرکز لرزه‌نگاری کشوری مؤسسۀ ژئوفیزیک دانشگاه تهران:
محل وقوع: استان كرمانشاه - حوالی كوزران
تاریخ و زمان وقوع به وقت محلی:
۰۷:۱۳:۱۷ ۱۴۰۵/۰۴/۲۹
طول جغرافیایی: ۴۶.۴۳
عرض جغرافیایی: ۳۴.۵۶
عمق زمین‌لرزه: ۸ کیلومتر
نزدیک‌ترین شهرها:
۱۷ کیلومتری كوزران (كرمانشاه)
۲۳ کیلومتری گهواره (كرمانشاه)
۲۶ کیلومتری روانسر (كرمانشاه)
نزدیکترین مراکز استان:
۶۵ کیلومتری كرمانشاه
۹۸ کیلومتری سنندج
كوزران کرمانشاه دوباره لرزید/ اینبار زلزله به بزرگی ۵.۷
مرکز لرزه‌نگاری کشوری مؤسسۀ ژئوفیزیک دانشگاه تهران:
محل وقوع: استان كرمانشاه - حوالی كوزران
تاریخ و زمان وقوع به وقت محلی: 1405/04/29 07:18:49
طول جغرافیایی: 46.48
عرض جغرافیایی: 34.57
عمق زمین‌لرزه: 13 کیلومتر
نزدیک‌ترین شهرها:
13 کیلومتری كوزران (كرمانشاه)
22 کیلومتری روانسر (كرمانشاه)
25 کیلومتری گهواره (كرمانشاه)
نزدیکترین مراکز استان:
61 کیلومتری كرمانشاه
94 کیلومتری سنندج
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/77299" target="_blank">📅 07:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8AJQAnMDTD6jwAReMJLfWUIv2w8BCmfvrWpRzV4CFNXhQCkHr82CJHph6pZ3IyH04jgR8ZwpLjxLYYIw43VEth1agXE6g8TaDHAJm5yxeidQAhIFizvOxKdPNFXx5Eruv39kGD0lM6S182vekGblj3x1NJDhPQB3QLvmZkFf94qTYeX9Xl3G95-p-_SP0vOlz5B7HK_xCC9_aAXNU7D8HIu13CXTSX78ESkiCF72rrZm0nSy0pmYNaYNh0TPwOQ6XuDjzZT0xgaKWfQn9DkPf1Pk8nFV5Hls8F_Jtltz6YVcat8VM_C2JQRRFKLejgRVDSSdnWS5aPbqBVM7WZd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
مارکو روبیو، وزیر خارجه آمریکا، روز یکشنبه گفت ایالات متحده آماده دیپلماسی با ایران است؛ هم‌زمان ارتش آمریکا نهمین شب پیاپی حملات خود را آغاز کرد.
روبیو پیش از عزیمت به مانیل، جایی که قرار است در اجلاس اتحادیه کشورهای جنوب شرق آسیا شرکت کند، به خبرنگاران گفت: «ایالات متحده همیشه برای رسیدن به یک راه‌حل دیپلماتیک آماده است. ما چندین بار با ایران تلاش کرده‌ایم و به تلاش خود ادامه خواهیم داد. اگر آن در باز شود، از دیدن آن خوشحال خواهیم شد.»
روبیو از ایران به‌دلیل حمله به کشتی‌ها و ایجاد مانع در تنگه هرمز انتقاد کرد. تفاهم‌نامه‌ای که آمریکا و ایران در ماه ژوئن به آن دست یافتند، با هدف گسترش آتش‌بس و ازسرگیری تردد در این آبراه کلیدی تنظیم شده بود.
روبیو گفت: «اگر آن‌ها مفاد این تفاهم‌نامه را نقض کنند، نمی‌توانند انتظار داشته باشند که این تفاهم‌نامه همچنان پابرجا بماند.» او افزود: «آن‌ها همچنان پیام می‌فرستند که می‌خواهند گفت‌وگو کنند و مذاکره کنند، اما آنچه ما به آن پاسخ می‌دهیم رفتارشان است، و رفتارشان این است که موشک‌ها و پهپادهایی را علیه کشتی‌ها، از جمله همین امشب، پرتاب می‌کنند.»
کیت ماهر، خبرنگار سی‌ان‌ان، از روبیو پرسید اگر تلاش‌های دیپلماتیک شکست بخورد چه خواهد شد. روبیو پاسخ داد: «فکر نمی‌کنم برای ایران خوب باشد. منظورم این است که اقتصاد ایران از هم پاشیده است.»
CNN
مارکو روبیو، وزیر خارجه آمریکا، گفت حادثه‌ای که روز شنبه در شمال عراق به کشته‌شدن یک نظامی آمریکایی انجامید، یک «سانحه» بود و این نظامی هنگام خنثی‌سازی یک پهپاد سرنگون‌شده ایرانی آسیب دید.
روبیو روز یکشنبه به خبرنگاران گفت: «هیچ کاری که ارتش انجام می‌دهد بی‌خطر نیست. همه این کارها ذاتاً خطرناک‌اند و ما فقط سپاسگزاریم که چنین آمریکایی‌های قهرمانی با پوشیدن یونیفرم، در خدمت کشورمان هستند.»
روبیو درباره حمله ایران در روز جمعه در اردن که به کشته‌شدن دو نظامی آمریکایی انجامید، گفت: «یک موشک عبور کرد. تقریباً همه موشک‌ها را سرنگون کردیم. یکی از آن‌ها رد شد... این دلخراش است.»
روبیو گفت که «برای خانواده‌هایشان و آمرزش روحشان دعا می‌کند.»
تعداد نظامیان آمریکایی که در جنگ نزدیک به پنج‌ماهه با ایران کشته شده‌اند، اکنون به ۱۷ نفر رسیده است.
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/77298" target="_blank">📅 07:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان چابهار 5 بار زد 5:50
باز داره چابهار رو میزنه  لرزش ها وحشتناکه
الان دوبار صدا اومد ساعت ۵:۴۸
5:49 دیقه کنارک صدای انفجار اومد
هنوزم صدای هواپیما میاد
به عنوان آخرین مقصد اینجا رو میزنه
کنارک صدای جنگنده و انفجار هم اکنون
۲انفجا کنارک نیروی هوایی ۵.۴۹
صدای هواپیما بازم شنیده میشهه چابهار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77297" target="_blank">📅 05:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ddbd450c.mp4?token=ZikASNsyK7XYhYu-10-f6sr9QMvYeq0y9SdDtx5ysLF3-LCuUVCo4gYh-Dmy-Hey9RRLSaOAI8p-7hkFZ6tyYIIt5DT6ZCg8HPR4QfVR5m8haUL0CJmlJxDrsT3WsG1PB_-Q-VWuVm5TUX6LRQTeIYo3uMoURysUdO6aPMTxLmGUV9lSDzUl3YY6xu6wrplJ7VUVnMDiGpqJFSYahXnz0FfKq6LM_kax5I80JIn6VS-vCTIXc6entLEdzRtIOl7Nl00lNrA80RzcpIsqt7ITYyuEEP5eXqLBfEWTEwgHGe2NtoTHE_BKq27cEJJXOjIP3ufp4iDGOd8B21h2zWIUjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ddbd450c.mp4?token=ZikASNsyK7XYhYu-10-f6sr9QMvYeq0y9SdDtx5ysLF3-LCuUVCo4gYh-Dmy-Hey9RRLSaOAI8p-7hkFZ6tyYIIt5DT6ZCg8HPR4QfVR5m8haUL0CJmlJxDrsT3WsG1PB_-Q-VWuVm5TUX6LRQTeIYo3uMoURysUdO6aPMTxLmGUV9lSDzUl3YY6xu6wrplJ7VUVnMDiGpqJFSYahXnz0FfKq6LM_kax5I80JIn6VS-vCTIXc6entLEdzRtIOl7Nl00lNrA80RzcpIsqt7ITYyuEEP5eXqLBfEWTEwgHGe2NtoTHE_BKq27cEJJXOjIP3ufp4iDGOd8B21h2zWIUjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام موج حملات آخر هفته علیه ایران را به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) نهمین شب پیاپی حملات علیه ایران را روز ۱۹ ژوئیه، ساعت ۱۰ شب به وقت شرق آمریکا، با موفقیت به پایان رساند.
تجهیزات و نیروهای سنتکام مراکز فرماندهی نظامی ایران، مواضع پدافند هوایی و نظارت ساحلی، توانمندی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و شبکه‌های ارتباطی را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی عبوری از تنگه هرمز بیش از پیش کاهش یابد.
ارتش آمریکا به دستور فرمانده کل قوا، ایران را پاسخ‌گو می‌کند. نیروهای سنتکام همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی می‌مانند.
CENTCOM
منابع حکومتی:
اطلاعیه شماره ۳۰/ دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
روابط عمومی سپاه:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی؛ اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک کوش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگه هرمز را داشتند منفجر شده و از حرکت باز ماندند.
🔹
اینجا سرزمین ماست و دخالت ارتش تروریستی آمریکا از هزاران کیلومتر آن طرف‌تر هیچ وجاهت قانونی ندارد و با قطعیت با آن برخورد خواهد شد و تا زمانی که شرارت های آمریکا در منطقه ادامه یابد این معبر برای عبور کود شیمیایی و حتی یک قطر نفت و گاز امنیت ندارد.
🔹
ارتش متجاوز، آماده عملیات تنبیه ما به خاطر این تخلف غیرقانونی باشد.
قدردانی سپاه از اطلاعات مردم اردن؛ هواپیماهای بزرگ ترابری C17 و هواپیماهای فرمانده کنترل P8 ارتش متجاوز امریکا در فرودگاه عقبه هدف موشک بالستیک قرار گرفتند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
إِنْ نَکَثُوا أَیْمانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَ طَعَنُوا فی دینِکُمْ فَقاتِلُوا أَئِمَّةَ الْکُفْرِ إِنَّهُمْ لا أَیْمانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ
🔺
مردم شریف و ارتشیان مجاهد اردن، با تشکر از همکاری صمیمانه و اطلاعات دقیق شما که موجب هدفگیری دقیق رزمندگان اسلام و انهدام ۲۰ سوله محل استقرار نیروهای ارتش کودک کش آمریکا در منطقه الازرق و کشته شدن ده‌ها نیروی تروریست آمریکایی شد.
🔺
رزمندگان نیروی هوافضای سپاه در موج ۲۱ عملیات نصر ۲ با رمز مبارک یا رقیه (س) و تقدیم به دختر بچه های شهید جنگ تحمیلی سوم، با کمک شما، هواپیماهای بزرگ ترابری C17 و هواپیماهای فرمانده کنترل P8 ارتش متجاوز امریکا در فرودگاه عقبه را هدف حمله موشک های بالستیک قرار داده و به تعدادی از آنهاخسارت سنگین وارد کردند.
🔺
نظامیان متجاوز آمریکا که طی چند دهه اخیر به بیش از ده کشور اسلامی حمله کرده و میلیون ها مسلمان را کشته اند و حامی اصلی رژیم کودکش صهیونیستی در کشتار عظیم مردم غزه و ویران کردن کرانه باختری هستند، از لحاظ شرعی مهدور الدم هستند و هر مسلمانی، هرجا دستش رسید باید این قاتلان وحشی را بکشد.
🔺
با تشکر مجدد از تلاش‌ها و همکاری‌های شما که با انجام تکلیف شرعی راه را برای آزادی قدس شریف هموار می‌کنید.
«إِنْ تَنْصُرُوا اللَّهَ یَنْصُرْکُمْ وَ یُثَبِّتْ أَقْدَامَکُمْ»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77296" target="_blank">📅 05:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94bb518d25.mp4?token=TgCNfsJhRFq3ScH7BPJDmu4pFLRCFVvDdAphNqi9m-q2eA7HAZ1F6ZJ7_JpDUOe21qpVRXdeMxah6Le_68rXruZ9TY5mlwSldHrJpezBDTeLeJZYFyddT04I-EqG17cYBmC_Bw37ZgrJtWE5RyZ59eZIn4pV7Zc3Ct4m0mJt6ZUkCpxL40FZ4lUf-qnusfYX_IZOpZ5cungsQl4p7p_fkb9aCOkhcSfNaF7DTPwpS05oT8Yv6dH-LXJa2E_Vm9jgpXErQbtSdQF8mVpqBnHT838kcsTG-RrF09Sj4RgW99Kmx2Zc7Gu24r-tNfHGlDyobLwwVdoSIq860W9qKyF4tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94bb518d25.mp4?token=TgCNfsJhRFq3ScH7BPJDmu4pFLRCFVvDdAphNqi9m-q2eA7HAZ1F6ZJ7_JpDUOe21qpVRXdeMxah6Le_68rXruZ9TY5mlwSldHrJpezBDTeLeJZYFyddT04I-EqG17cYBmC_Bw37ZgrJtWE5RyZ59eZIn4pV7Zc3Ct4m0mJt6ZUkCpxL40FZ4lUf-qnusfYX_IZOpZ5cungsQl4p7p_fkb9aCOkhcSfNaF7DTPwpS05oT8Yv6dH-LXJa2E_Vm9jgpXErQbtSdQF8mVpqBnHT838kcsTG-RrF09Sj4RgW99Kmx2Zc7Gu24r-tNfHGlDyobLwwVdoSIq860W9qKyF4tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کاری که اکنون می‌کنیم این است که هرگونه امکان دستیابی آن‌ها به موشک هسته‌ای را از بین می‌بریم
مصاحبه ترامپ بعد از مراسم فینال جام جهانی، ترجمه ماشین:
ترامپ:
به کشورمان افتخار می‌کنیم. به کاری که همه انجام دادند بسیار افتخار می‌کنیم. به جیانی اینفانتینو و تمام کارکنانش برای کار باورنکردنی‌شان تبریک می‌گوییم.
این یکی از بزرگ‌ترین رویدادها از هر نوعی بود که تاکنون برگزار شده است. بنابراین خیلی خوشحالیم که این‌قدر موفق بود. مردم از سراسر جهان آمدند و کشورمان را دوست داشتند.
می‌دانید، این رویداد کشورمان را از زاویه‌ای متفاوت به نمایش گذاشت.
اتفاق فوق‌العاده‌ای بود؛ یک رویداد عالی بود و خوشحالم که همه شما از آن لذت بردید.
خبرنگار:
شما گفتید آرژانتین باخت.
ترامپ:
این را شما می‌گویید؟
خبرنگار:
شما گفتید آرژانتین باخت.
ترامپ:
نه، چنین چیزی نگفتم. فکر می‌کنم هر دو خوب بازی کردند. من می‌گویم اسپانیا واقعاً بهتر بازی کرد.
هر دو خوب بازی کردند. منظورم این است که به فینال رسیدند و واقعاً بسیار هیجان‌انگیز بود. به نظر می‌رسید اسپانیا مسلط بود، اما مسابقه بسیار نزدیک بود. بنابراین عالی بود؛ یک رویداد عالی بود، بله.
خبرنگار:
[پرسش خبرنگار نامفهوم است.]
ترامپ:
خب، احساس بسیار بدی داریم. اما می‌دانید، آن افراد بزرگ، آن میهن‌پرستان بزرگ، در تمام این مدت جنگیدند تا ایران نتواند سلاح هسته‌ای داشته باشد.
ایران به‌شدت، به‌شدت آسیب دیده است. تقریباً همه توان نظامی‌اش را از دست داده است. چیز بسیار کمی برای آن‌ها باقی مانده. تعدادی موشک و پهپاد دارند. مقداری توان تولید هم دارند، اما زیاد نیست.
ما تنگه هرمز را در کنترل داریم. آن‌ها هیچ‌چیز را کنترل نمی‌کنند. پس خواهیم دید چه اتفاقی می‌افتد.
امشب دوباره ضربه بسیار سختی به آن‌ها زدیم و این کار را به احترام آن میهن‌پرستان بزرگی انجام دادیم که احتمالاً سه نفرند، نه دو نفر.
خبرنگار:
پیامدهای دخالت چین در انتخابات آمریکا چه خواهد بود؟
ترامپ:
بعداً درباره‌اش صحبت خواهیم کرد. با آن‌ها گفت‌وگو می‌کنیم، مطمئنم.
خبرنگار:
می‌توانم بپرسم آیا با کارنی، نخست‌وزیر کانادا، گفت‌وگو کردید؟
ترامپ:
بله، کردم. بله، صحبت کردم.
خبرنگار:
گفت‌وگو چطور پیش رفت؟
ترامپ:
خوب پیش رفت. اما به او گفتم باید جلوی ورود دود این آتش‌سوزی‌ها را بگیرید، چون هوای ما را مسموم می‌کند. هوای ما مسموم شده است.
من رابطه خوبی با مارک کارنی دارم. اما می‌دانید، باید آتش‌سوزی‌های آنجا را متوقف کنیم. اگر بتوانیم به آن‌ها کمک کنیم، کمک می‌کنیم. اما شاید باید بابت خسارت‌ها چیزی به ما بپردازند، یا شاید ما باید تعرفه‌ای وضع کنیم.
وضعیت وحشتناک بود. کسب‌وکارها تعطیل می‌شدند؛ به‌ویژه در میشیگان. اگر به دیترویت در میشیگان نگاه کنید، مجبور شدند همه‌چیز را تعطیل کنند. مجبور شدند کارخانه‌های خودروسازی و بسیاری مراکز دیگر را ببندند.
من هرگز به یاد ندارم چنین اتفاقی افتاده باشد. در چهار یا پنج سال گذشته این وضعیت کم‌کم آغاز شد. پیش از آن هرگز به یاد ندارم چنین اتفاقی افتاده باشد.
خبرنگار:
آیا فرصت کردید با نخست‌وزیر اسپانیا هم صحبت کنید؟
ترامپ:
بله. با مقام‌های اسپانیا صحبت کردم و بابت داشتن چنین تیم بزرگی به آن‌ها تبریک گفتم. با افراد زیادی صحبت کردم.
خبرنگار:
پیش‌تر با اسپانیا تنش داشتید.
ترامپ:
نه، هیچ تنشی ندارم. با هیچ‌کس تنشی ندارم.
خبرنگار:
[پرسش خبرنگار درباره اسپانیا نامفهوم است.]
ترامپ:
خب، [نامفهوم]. می‌دانید، توانایی زیادی دارد. اما تا جایی که می‌دانم، ظرف حدود یک ماه [نامفهوم] تا آن را به حداکثر برسانند. بنابراین قرار است آن را بفرستند و به حداکثر برسانند. فکر می‌کنم حدود یک ماه دیگر.
خبرنگار:
آقای رئیس‌جمهور، آیا با نخست‌وزیر کانادا صحبت کردید؟
ترامپ:
بله. همین حالا داشتم پاسخ می‌دادم. درباره‌اش با او صحبت کردم. گفتم: «باید جلویش را بگیرید.»
مسئله در اصل مدیریت جنگل‌هاست و آن‌ها باید بدانند چگونه این کار را انجام دهند. اگر چهار یا پنج سال به عقب برگردید، به یاد ندارم هرگز چنین مشکلی داشته باشیم. اما حالا این مشکل را داریم.
فردی در محل:
از این طرف بیایید، آقای رئیس‌جمهور.
خبرنگار:
شما گفتید جنگ را ظرف چهار یا پنج هفته پایان می‌دهید.
ترامپ:
[آغاز پاسخ نامفهوم است.] کاری که اکنون انجام می‌دهیم بسیار بزرگ‌تر است. قبلاً کار محدودتری انجام می‌دادیم؛ می‌خواستیم مانع دستیابی آن‌ها به توانایی خاصی شویم. حالا داریم کار را تمام می‌کنیم.
بنابراین واقعاً همان موضوع قبلی نیست. کاری که اکنون می‌کنیم این است که هرگونه امکان دستیابی آن‌ها به موشک هسته‌ای را از بین می‌بریم.
اگر نگاه کنید، پس از یک هفته و نیم ــ نه چهار هفته؛ یک هفته و نیم یا دو هفته ــ جلویشان را گرفتیم؛ احتمالاً... اما نمی‌خواهم از واژهٔ «احتمالاً» استفاده کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77295" target="_blank">📅 04:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iszhx07Pk7VRJTggxjcSa-c8ILyFYh9I0T118KIc6hMZ77Z2WIcVlxvyq4T_PkXLYvop54mtrVQ_3XN37VMZjNfI3JeKXmu1BluT44wp-2VU5jL6ec95u13SlhyFFtvSwW-FF7sdTllaggqaOakPHgyUU4qPwrNgd0WjGQBI4ZvItf_2A2xUJja2bTy0o4Snfdowe2JIwo6hRieYk7za8y3S8QA2vrM0d1isvSB689fRc3_nufc0PR7bWFSnIplJ8euWKie3swIRX55Oryz0O2QIN4VPcScV7HItoc6FGyoH1HUTDlMVO1m2_WjjnGObumglrvxQM8EAomj9aF5s2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت: تصویر منتشرشده با شرح کنارک
پیام‌های دریافتی:
بازم یه انفجار چابهار ۳:۵۱
کنارک صدای انفجار(دور بود)
و همینطور صدای جنگنده
نیم ساعته از بعد جام جهانی داره چابهار و کنارک رو سنگین می زنه. جاهای مختلفه و نمی دونم کجاها بوده فعلا
دوباره خیلی سنگین زد
چابهار ۳:۵۱ صدا اومد
همین الان چابهار دوبار زد 3:51
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77294" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzPYVY2bkMG12zkTiIK3_rgyiMEt-blcFB6Q5jYziR4ieP3MBm-I5aXtNExbn5QysV8JFbaIDVuP89-dBPlKon_2QNNX88QNDDOh2beMtkzxRbW2WenmMEDpfnGXwMMfxYbYxxPity6l1PMzGzf7rkDODBVU4wFX8uCT9rm0xPqgi40_IyY855VuxHTa9LhMez3w122salbgULFaiXoCBfELv5aIX9qE3iw_pxzxNswgY-bkE1LsWKm0fcay4p_2QftGu0YpXN7N_Qp9xcEg8rrHn_g2Wk8Honu36HTy66LPSkeyVlXbnYNIa_HNggt6iDRmadVpcCZURGo4BEgOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با آغاز نهمین شب حملات متوالی آمریکا به مواضع نظامی در ایران، بامداد یکشنبه، فارس از اصابت چند موشک و شنیده‌شدن صدای انفجارها در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر و بندر خمینی در خوزستان خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77293" target="_blank">📅 03:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام‌های دریافتی:
سپاه خورموج توی استان بوشهر رو زدن برق ی منطقه هم رفته
سلام وحید  ساعت ۳:۰۷ دقیقه
خورموج پنج انفجار شدید
همین الان خورموج پادگان سپاه زدن برق هم قطع شد
همین الان سپاه خورموج زدن ساختمانش کلا صااف زمین شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77292" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیام‌های دریافتی:
چندین صدای انفجار پیاپی، سیریک.
ساعت سه و پنج دقیقه بامداد شهر سیریک ده ها انفجار بسیار سنگین
سه تا آخری خیلی بد زد موجش زیاد بود
احتمالا اسکله بوده باشه
۳:۰۵ تا ۳:۱۰ چند انفجار سمت سیریک (طاهرویی) خیلی شدید
سیریک صدای انفجار پشت سرهم خیلی بلند، صدای جنگنده‌ها هم میاد
بندر عباس ساعت 3:11 دقیقه چند انفجار پشت سر هم و طولانی رخ داد و تا دو دقیقه ادامه داشت
بندر جاسک همین الان دوتا صدا اومد
بندر جاسک دوباره صدا اومد صدا خیلی وحشتناک بود
سیریک حدود ۸ انفجار شدید شایدم بیشتر  شیشه های اتاقم نزدیک بود بشکنن
جاسک جنگنده بالا سرمونه
۳تا انفجار تا الان
بیشتر از ۳تا شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77291" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fzdw2-5xREz93XQeRMYabJBxswdR7TLe_nqq3wdghXqcbA4QP_N1oJkjmjtGgN7vsHOiLC_CIDyPlqJFY6WGikh_kgth50cLdste-L7J0AFba642ZjhmV7mRvOJV2ct1H-YEk5IFldTHhaVtVLcSFgk5xAimB2fsZ_5AlC3Z63SbHefh9aBdRtuoVI-RN55rvZXvsM47piQQEz10rqfohGM7Xiubi-dznfSaWf9ec-gXuhD3PLGRJn_r88x6x3i9AGCRlsODrw_1vwpWTMmJl_1ju3wfNDlDLDVbEYH2M3oU3fTUYbatAksBAjLG9XtYLk0gzGodong83exfrImA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'سربندر ("بندر امام خمینی") ساعت ۲:۴۰ دوشنبه ۲۹ تیر'
Vahid
دوباره زد
سربندر خوزستان 3:08 دو صدای انفجار و لرزش شدید خونه
وحید جان دوباره سربندر دوبار محکم زدن
وحید سربندر رو باز هم زد
تک انفجار، ولی خیلی سنگین ۳:۰۹
۳.۰۸ دقیقه سربندرو بازم زدن
اقا وحید ماهشهر دوباره زد
شیشه اتاقم لرزید این بار
صدای انفجار قبلی رو فقط شنیدم
خود ماهشهرم، سربندر نیستم ۳:۰۹
وحید ماهشهر یکی سنگین زد
سربندر دوباره زد صداش بیشتر از قبلی بودد
ماهشهر دوباره شدید ۳:۸ دقیقه
ماهشهر رو دوباره زد ۳:۰۸
همین الان باز ماهشهر دو انفجار شدید
سربندر ساعت ٣:٠٩ دقیقه دوباره انفجار شدید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77290" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=ogBW4ZlnA6hZgKOSdYtvUb58Jplyz3PwiMQo_TgDWBQgy2WXv7oG-P64psgkEJ926DMHa3yT4pyJM6k2R5s4V8X68IKkw5eSbNSWmsbQ9CGYHL41zijDJMQxTv6kB0PAPAw-AAzniC576Tf10y4yiaapxQAgi4ijAJAjhU_bPDll7LQ2022yFaUi2LLkzbpTZQNBXqVN2jZ6MReLU6HJNbIV77XNIAEhMUxfkUIMGsVHLL5-_8aFoIfnPkuHN-ShZ3rIxvtJylDYwqq4ecy8b6N0JtSZLoBMaQTypr0R4lqo3d2Yl_PJ36-CbCJVt1jYyacyROrUULhmaIEKM4SaNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=ogBW4ZlnA6hZgKOSdYtvUb58Jplyz3PwiMQo_TgDWBQgy2WXv7oG-P64psgkEJ926DMHa3yT4pyJM6k2R5s4V8X68IKkw5eSbNSWmsbQ9CGYHL41zijDJMQxTv6kB0PAPAw-AAzniC576Tf10y4yiaapxQAgi4ijAJAjhU_bPDll7LQ2022yFaUi2LLkzbpTZQNBXqVN2jZ6MReLU6HJNbIV77XNIAEhMUxfkUIMGsVHLL5-_8aFoIfnPkuHN-ShZ3rIxvtJylDYwqq4ecy8b6N0JtSZLoBMaQTypr0R4lqo3d2Yl_PJ36-CbCJVt1jYyacyROrUULhmaIEKM4SaNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'سایت موشکی تبریز'
دوشنبه ۲۹ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77289" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/028b9087f7.mp4?token=a4MuLNUAPUi77XtsimpQRoDsMc-Lm5nv1X2xdWXncd67_qwrvadA496XjeHsILy4LW1Y2nlSOPeq7-DMD-kJ8gYjXmgIPzr140WagdSNVk5O-kc3Gyhz2E309NToMyjA891bLYlrEOZoIvNAG7M3CKfyuf3iY8iQTMN5q-VHKeWSrkD_kTr3pQynevivxx1cPw8c9f2CcQXo7toqPYD-ITpW8zl1jl9pp96DcsG3SxP3bnI-UsS8ZZlX-wW2UtJLcolzE0TO0iqwUfJ1b3rIVGW1tFTdQJ4XD8ohjQR7w4MOJ_NDNmyq-eLWbr6rMKDe3EtqHIVw7WShaYMm7BJNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/028b9087f7.mp4?token=a4MuLNUAPUi77XtsimpQRoDsMc-Lm5nv1X2xdWXncd67_qwrvadA496XjeHsILy4LW1Y2nlSOPeq7-DMD-kJ8gYjXmgIPzr140WagdSNVk5O-kc3Gyhz2E309NToMyjA891bLYlrEOZoIvNAG7M3CKfyuf3iY8iQTMN5q-VHKeWSrkD_kTr3pQynevivxx1cPw8c9f2CcQXo7toqPYD-ITpW8zl1jl9pp96DcsG3SxP3bnI-UsS8ZZlX-wW2UtJLcolzE0TO0iqwUfJ1b3rIVGW1tFTdQJ4XD8ohjQR7w4MOJ_NDNmyq-eLWbr6rMKDe3EtqHIVw7WShaYMm7BJNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'انفجار در
#تبریز
'
بنا بر پیام‌های دریافتی از شهروندان حدود ساعت ۲:۳۷ دوشنبه ۲۹ تیر صدای چند انفجار در تبریز شنیده شده.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77288" target="_blank">📅 03:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77287">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dGnB-wQjquwX1FI5cE-c8Ihqgw0qMNJ3jYbR9k45UHM04sgw0clHF1jbBhxbDuCgQzs1Lju2kOo9dwhem1cNONA8M-gV2vuDyU5JNowaTTY6JBa7TAdExiAln9bI3PiunX-2Nk2eVV4IRE_o_GYFMuJb8N2gRlVkzCnMLwb92Ohm-LDJOAENSJpZd6LPtdFLhQe4nVQbUbSH0kI9DNDcfswvdMzwJSRU8Xk0DnWbz95hUKSb5JrlmgKALTn4MCDfsG7_LPq-eB_xYscCS1yOlp46-po4CkMctXW5lYCPpQBAITk_mhZfyewNPogvssrgAM0K1WNT14loxVTBvC3YNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
سنتکام امروز ساعت ۷ عصر به وقت شرق آمریکا، برای نهمین شب متوالی موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات به تضعیف بیشتر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی در حال عبور از تنگه هرمز به کار می‌روند، ادامه خواهد داد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77287" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پیام‌های دریافتی:
۵ ۶ تا همین الان کنارک
خیلی خیلی شدید بود هنوز داریم میلرزیم
۳ تا دیگه همین الان
چابهار الان صدا انفجار پی در پی اومد
2.43
چابهار 4تا صدای انفجار شنیده شد دور بودن
چابهارو الان زدن ۲:۴۴
چابهار صدای انفجار اومد
کنارک 2:42 سه انفجار پشت سرهم
کنارک ۳ تا انفجار
سلام بازم دوتا قدای انفجار ساعت ۲.۴۵ در کنارک
خیلی بد داره میزنه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77286" target="_blank">📅 02:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیام‌های دریافتی:
ماهشهر صدای انفجار اومد میگن سربندره
سلام وحید جان
ساعت 02:40 سربندر صدای وحشتناکی اومد.
آقا وحید ماهشهر همین الان چندتا صدای مهیب و لرزش شیشه ها رو داشتیم
همین الان ماهشهر رو زدن
سربندر ۲:۴۱ انفجار شدید
سربندر دو سه تا پشت سرهم یکیش خیلی نزدیک بود یعنی پدافند رو زدن
چون تازه دود دیدم از سمت سایت پدافندی  نزدیک خونمونه
وحید جان همین الان سربندر خوزستان  شدید زد
وحید جان 2:40 سربندر انفجار بسیار قوی
بندر امام خمینی، خوزستان
من ماهشرم، هیچ صدایی نشنیدم، شاید سربندر رو زده باشن، اما ماهشهر هیچ خبری نبوده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77285" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QmKSG98Hkrr7M_wFxWW-aDzuRwGvSJOEe7U2pOSUUANwloW3IJBh2tgtdDhhLGKz0G5CCXodlwYuy0ru0wCVZEey8p2NWynHop2HUnkbELLYvpy1p_FfqwHuUFBNmom454rviv5V-tZu0N9I6fN3LzxRyayMMw7QQHOiWzl3p7wKP09kYxSFh5VIZEP7V_X909dxunx6F4bjOUsbsK3SpJj6cjQo8UpXuGEtVoHjWL-qMaFlCN4qFrbIh2prav0r6i26w6YvOiptGO7hiO1iEJMD9MxSYh0qJBNOEKY1bM_Poh4ptmwV-h-ETZOX7StBFhnxSKFlwUdu7tTWMrEufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
وحید همین الان صدا اومد از تبریز ، ۳ تا
تبریز همین الان ساعت ۲.۳۸ صدای انفجار شدید اومد
صدای چند انفجار وحشتناک از تبریز همین الان
تبریز سه چهار تا صدای انفجار ا‌مد
سلام تبریز الان صدای ۳ تا انفجار اومد
صدای چند انفجار پیاپی - تبریز ساعت ۲:۳۷ بامداد
وحید جان تبریز 3 باز زدن شدید
سلام آقا وحید 2:37 صدای ۳ انفجار اطراف تبریز
سلام وحید. ۲:۳۷ انفجار در تبریز
ساعت ۲:۳۸ تبریز
چندین صدای مهیب انفجار
وحید تبریز یه صدای مهیب اومد نمی‌دونیم چی بود ولی انفجار بزرگی بود
همین الان تبریز پشت سرهم ۴ تا صدای انفجار اومد
سلام تبریز زدن ساعت ۲.۳۷ دقیقه
مکانی که ما بودیم قشنگ لرزید صدای انفجار هم اومد اما سمتش نمیدونم دقیق کجاست
سلام آقا وحید. الان ۲:۳۸ تبریزو زدن.
سلام وحید جان چند انفجار پشت سرهم در تبریز ۲:۳۷
خیلی شدید بودن
سلام تبریز صدای ۲ تا انفجار اومد
سلام صدای ۳ ۴ تا انفجار پشت سرهم  اومد تبریز
وحید  ۴ انفجار پیاپی تبریز
همین الان صدای انفجار تبریز ۰۲/۳۷
تبریز صدای ۳ انفجار پشت سر هم،ساعت ۲:۳۷
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77284" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668363f045.mp4?token=aPMA_-y3nAFHPVBlTM2w6Dz2wn_y51pIJbjrmdJf8WpdxEX3RY4NvpcOS6RrwrYnTrdVxUTSkjyvbc5357P2UCPIdy9fXFNYRQr1lu8OTShsqV9F93gFsbkCkhWXLk3mTWs1yGOMkIdxsaesOO6hVZH802a_5EU2HXu9tYUb4ahZoaKVBh0eUOYrmDJMkKzS5T-0gg_NAuSb49tQAexn2iwdD5mdFTv6j6urLeSWWbK_KSlwxn-8rjSMBD_E9M0Yo5rZ3fuH_3k_y8ygQbtMgflUGlU0fv3MUHw_YFgZiP13ACkDJkobUJ8HcrwqpUWTBOcs26SzFR9VqKlLjYRaxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668363f045.mp4?token=aPMA_-y3nAFHPVBlTM2w6Dz2wn_y51pIJbjrmdJf8WpdxEX3RY4NvpcOS6RrwrYnTrdVxUTSkjyvbc5357P2UCPIdy9fXFNYRQr1lu8OTShsqV9F93gFsbkCkhWXLk3mTWs1yGOMkIdxsaesOO6hVZH802a_5EU2HXu9tYUb4ahZoaKVBh0eUOYrmDJMkKzS5T-0gg_NAuSb49tQAexn2iwdD5mdFTv6j6urLeSWWbK_KSlwxn-8rjSMBD_E9M0Yo5rZ3fuH_3k_y8ygQbtMgflUGlU0fv3MUHw_YFgZiP13ACkDJkobUJ8HcrwqpUWTBOcs26SzFR9VqKlLjYRaxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال اسپانیا با تک گل فران تورس در وقت‌های اضافی آرژانتین را شکست داد و قهرمان جام جهانی ۲۰۲۶ شد.
این دومین قهرمانی اسپانیا در جام جهانی است که این بار با پیروزی مقابل مدافع عنوان قهرمانی به دست آمد.
@
VahidHeadline
تلویزیون سراسری در ایران مراسم اهدای جام جهانی فوتبال رو به خاطر حضور ترامپ پخش نکرد.
ترامپی که حتی موقع ثبت لحظه تاریخی بالا بردن جام هم حاضر نشد از کادر دوربین‌ها بیرون بره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77283" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c82cf41e.mp4?token=ip7F6aUDbM945j31C1WHmnx96FADB8c3EpoxATKhaWr3wyd-ydlSoAPc1btJCZ1ocfSVEAo579-nbpLGfkj-NEAgQdhEXaKgJGSEsHTC_ux7gM2Zd5McwBqALT4bIbacpdpZhZVL9yjeIvi_HK_JKOzf80c_p0VIjQ0H7hURR8o9_w_LaRkjN1W4vqD2zy19knP3YJTasNRP6IpeASEbc_l3U03EBnXWXq5kaiC4RvYxPUHb4-EzClKfHUG9wENSNUl1g5W8MqDmQnuj-SzfNoZiCTV1vWoyswQXWDi_CHtnUYVT-EV_JSd6d2RGOWXTk3o4khHQxG69YpXYZZI_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c82cf41e.mp4?token=ip7F6aUDbM945j31C1WHmnx96FADB8c3EpoxATKhaWr3wyd-ydlSoAPc1btJCZ1ocfSVEAo579-nbpLGfkj-NEAgQdhEXaKgJGSEsHTC_ux7gM2Zd5McwBqALT4bIbacpdpZhZVL9yjeIvi_HK_JKOzf80c_p0VIjQ0H7hURR8o9_w_LaRkjN1W4vqD2zy19knP3YJTasNRP6IpeASEbc_l3U03EBnXWXq5kaiC4RvYxPUHb4-EzClKfHUG9wENSNUl1g5W8MqDmQnuj-SzfNoZiCTV1vWoyswQXWDi_CHtnUYVT-EV_JSd6d2RGOWXTk3o4khHQxG69YpXYZZI_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی از قم با شرح پرتاب موشک
سایر پیام‌های دریافتی که شاید درباره پرتاب موشک باشند:
وحید شهرستان محلات صدای انفجار مهیب اومد . همه جا لرزید
23/44 صدا انفجار از دور ساوه
ساوه ۱۱:۴۵ دقیقه
صدای انفجار
سلام وحید جان صدای انفجار ساعت ۲۳:۴۰ ساوه
نزدیک قم یه صدای انفجار اومد
سلام وحید  الان صدای جنگنده خیلی نزدیک  دلیجان
صدای دو یا سه تا انفجار شنیدم اما خیلی فاصله بود. فکر کنم خمین با اراک بود.
ما خنداب هستیم.
قزوین صدای جنگنده [که معمولا با صدای پرتاب موشک اشتباه گرفته میشه.]
از دلیجان موشک پرتاب شد
ساوه صدایی اومد. مثل انفجار. ولی انگار از دور بود
اراک هم صدای یه انفجار از دور شنیده شد
وحید جان ما اراکیم یک ربع پیش سه بار صدای انفجار اومد اما بار اول صداش خیلی خیلی بلند بود
🔄
منابع حکومتی:
فرماندار اراک اعلام کرد که صدای شنیده شده مربوط به اقدامات آفندی در یکی از استان‌های مجاور است و جای نگرانی نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77282" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP-C95jsKGI9VbD7KMEePcCGivU9ufaRXGZhQ4UzIMQLIvuQsqtX_-l603LSIxlXPfQ2aP0AjO2QLIOCtHm6XjiI-hqlJBZuuEY2TxUbJwvFRiwJCgUwo0VMnsGLcJz_HIJw-EOWSpevZrVQyc5ToHHjdTFJSvIdPtZalAcabUZl6MZ5JntJKvPeBnSCzDyUpUPJNuoTe5v-Z5gVgdpH-tHnOPCoMrW2w7hIvz-l8cfilqWNE-9XfpXRiRlQd1L_Fl7J6xfSGjOrB6f_TwVss87QPOJ846SyL3tgYLAwXtGYkG-bHMRItonlzPfCHcgXkco-nAyEdBYTwY3D_Ge0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
به‌روزرسانی سنتکام درباره نظامیان آمریکایی جان‌باخته اخیر
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دیروز اعلام کرد که در پی حمله ایران در ۱۷ ژوئیه در اردن، دو نظامی آمریکایی جان باخته‌اند و یک نفر نیز مفقود شده است. پس از جست‌وجویی گسترده، نیروهای نظامی آمریکا اوایل امروز بقایای انسانی ناشناسی را در محل پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق روز ۱۸ ژوئیه هنگام انفجار کنترل‌شده مهمات منفجرنشده متعلق به یک پهپاد انتحاری سرنگون‌شده ایرانی، در جریان عملیات کشته شد. یک نظامی دیگر نیز زخمی شد و همچنان برای جراحت جزئی خود تحت درمان پزشکی قرار دارد.
سنتکام به احترام خانواده‌ها در جریان روند اطلاع‌رسانی، از انتشار اطلاعات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77281" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhU7gWKpBcaY7qbhIxMm2RxjqzI1SQ2iMjcdmG7H3cGYAInQn1cvaSZZTbFNt5A_eMuGc8Drs1LREDXf_0OxUC3aw_2GiywJHc7CPKDAe4-fIbKuiHdS8nn3zNz3buoJnfbiS8aEtqkcExG7z9M6MWOwVItoTUgzVpOeqtbGFl_s1Jh5Nqx5uQYY4FU2i8Hk-LieAcxIj14odr6pbH-Kbb2VMZuemwt5pQomoTHRLBuhPI0FdPdqJ5KdtK2JHQVnt71uqIem3sApSqWO2UmQOBH5f_sQrpnnIGesOf5a-Sb32FG88cVUwqsXMGEwGrtaTUdQEn6RuB4gTXHi8fqAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران گفته است آمریکا بامداد یکشنبه با «تعدادی پرتابه» به سایت در حال ساخت نیروگاه دارخوین حمله کرد. دارخوین شهری در بخش دارخوین شهرستان شادگان در استان خوزستان ایران است.
آژانس بین‌المللی انرژی اتمی اعلام کرد که در حال بررسی این گزارش‌هاست و یادآور شد که این نیروگاه «در مراحل بسیار ابتدایی ساخت قرار دارد و در آخرین بازدید آژانس، هیچ ماده هسته‌ای در آن وجود نداشت.»
آژانس افزود که این حادثه «احتمالاً هیچ خطر پرتوی ایجاد نمی‌کند»، اما رافائل گروسی، مدیرکل آژانس، با انتشار پیامی در شبکه ایکس «خواستار خویشتنداری نظامی در اطراف همه سایت‌های مرتبط با فعالیت‌های هسته‌ای» شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77280" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MLaYP1lErUre0ZqW-wrykoR6NLJdDIhtTSz-jQQcztp6bt-vAFjNFe0bzynkuEkLDcOseXRcokNBSWwuxu1WavTHuYoMkEc5zvxrfyiBxwnIaICSQxrHD-F2e68DR_S8zAJF09wDQvDFuUJ31iYPmXiT7KE-0irZSpM9J6qdYbxHrTSKGLLhTpnFZf7WVpSGjpxJ-fLtHapUtcR-lBdL9zlCGYaSqeaBRwKnV8piCrSjW7nUCCm2EtaOx3ZUhDKmeokKBY4-_VIj-kZGQs-XaFePYW2V1Z3U_2yq-iV0kqbvm6czImB1GKozSylmDvkEqhAzWH6JmNwgombgYs1Nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی و انتظامی استانداری خوزستان عصر روز یکشنبه از «حمله موشکی آمریکا» به نقطه‌ای در اطراف شهر آبادان خبر داد.
ولی‌الله حیاتی اضافه کرد که این حمله کشته و مجروحی به جا نگذاشته است.
سنتکام، ستاد فرماندهی ارتش آمریکا در منطقه خاورمیانه، [هنوز] درباره این ادعا بیانیه‌ای منتشر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77279" target="_blank">📅 18:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPrgDOk9GTDVBSEt0l8_WY8y8R3P8RyXMFCk9lYLLQiH5WKt20HdVl2SoBgON5yBY_Q96o-k5oKlpLdaYunWFVfbhbUvClvBA0ekH0LglUoPvPLVj_yda-frVStUkL9NfIe2UqDNviAihF3k9-A0LqDMHAqn0Nk__2fqjVDIjOZAhkr5xZ9u1kwHAEkB9196RZyHxP8e9By37vcV_AGNr5v6v3Vfl6TVHjgzPsKcoAEO5fWBTY90GAuUjn3V9LglrsaahUiACMCSafzGtiGA8WGurnlKbEGXzzKFLCz5ij5c_lg6kVbFm1t6dN7EvLgtGDYxJvOVTTKRLNcqYB_J1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز یکشنبه اعلام کرد که نیروهای اسرائیلی و اردنی یک موشک ایرانی را که به سمت شهر عقبه در اردن شلیک شده بود، رهگیری کرده‌اند.
دقایقی پیش از این رهگیری، ارتش اسرائیل اعلام کرده بود که موشک‌هایی را که از ایران به سمت عقبه شلیک شده‌اند، شناسایی کرده و نسبت به احتمال «سرایت» حملات به خاک اسرائیل هشدار داده بود.
سخنگوی ارتش اسرائیل در پاسخ به پرسش خبرگزاری فرانسه دربارهٔ گزارش‌های مربوط به شنیده شدن صدای انفجار در نزدیکی شهر ایلات در جنوب اسرائیل گفت که نیروهای اسرائیلی و اردنی به‌طور مشترک یک پرتابه را رهگیری کرده‌اند.
در همین حال، ارتش اردن اعلام کرد که «سه موشک ایرانی را که خاک این کشور را هدف قرار داده بودند» ساقط کرده است و یک موشک دیگر نیز در منطقه‌ای بیابانی فرود آمده است، بدون آنکه محل دقیق آن را اعلام کند.
ایران در دور تازه درگیری‌ها با آمریکا که در هشت روز گذشته ادامه داشته است، اردن را در چند نوبت هدف قرار داده است. ارتش ایالات متحده اعلام کرده که در جریان حمله روز جمعه ایران به اردن، دو نیروی نظامی آمریکایی کشته شدند.
@
VahidHeadline
آپدیت:
اکانت ارتش اسرائیل، ترجمه ماشین:
⭕️
ارتش اسرائیل شلیک موشک‌هایی از ایران به سوی شهر عقبه در اردن، در مجاورت اسرائیل، را شناسایی کرد. چندین موشک رهگیر به سوی بقایای موشک‌ها شلیک شد تا از اصابت این بقایا به داخل اسرائیل جلوگیری شود.
هیچ خسارت یا جراحتی گزارش نشد. مطابق دستورالعمل‌ها، آژیرهای هشدار به صدا درنیامدند. این رویداد پایان یافته است.
آپدیت:
صفحه رسمی وزارت خارجه اردن در ایکس، از احضار کاردار سفارت جمهوری اسلامی در امان در اعتراض به حملات تهران به خاک اردن و اظهارات تحریک‌آمیز مقامات جمهوری اسلامی خبر داد.
در این بیانیه آمده سخنگوی این وزارت‌خانه به کاردار جمهوری اسلامی اعلام کرده است تا پیام روشن اردن مبنی بر توقف فوری حملات را به تهران منتقل کند. ...
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77278" target="_blank">📅 18:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/224ff6e0b2.mp4?token=OVrrJ_q1wlh9-glmbBxaaZv5F7bPbqmuRf7Sz_8wNCUT0dN5pWVy1im3VraxmfxXvVUxGMBAS96WyAvgzkSw8bdMMXvThdwRdJ7X9wNFwb5xVslNMuQRlX1hMVVEylehL9pvW67MmjUBbyjYDPR977Q_hxGar8rGXHrOhYLD7TAs5yyralb5GuhVBRbfrlcChnBIq2Le9-LOWf114PjpQn9r3oY3HEYNy3Nc-qyzSAUyQnqMnRhsFLY3AWAoZQBwXkCsDbVV_TcX9HeNhv77VDi_8KL9FPhQ0VlmaoP-GBX3iwhgqQxIZberTeBiczquN6cve-L0fKyKvRmASsU0c45eQLi41FyReV8VC8nCmPYGVkve_qIaIS568V16n20kkjN71cfSiJm_A0u4cbV2D8T0ySoVxIIpHJpAJ3RNQX2UJEKkn--8snu9duJv3v31-k1XxEYkNFCrK_mg46exprHPQQj02CoMhrfhFM871NoBWRq2LEDztwoXDRVg987a2I9ksfFcQ-wRv4wn3Aepbp88wxUTvlQ9vaeewAEgvMwW_MhvV4Cseg4ODf_AknGp7--ZOp8NYDUeu-712JT6Bq7-1VmbG5HQKVf1jIjprVIGobzsT_LbIrUO2LxWxo8XfhRES7uNEKKf4WIgKzZtJX56oPVT7t7Nr19tSB4HrZk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/224ff6e0b2.mp4?token=OVrrJ_q1wlh9-glmbBxaaZv5F7bPbqmuRf7Sz_8wNCUT0dN5pWVy1im3VraxmfxXvVUxGMBAS96WyAvgzkSw8bdMMXvThdwRdJ7X9wNFwb5xVslNMuQRlX1hMVVEylehL9pvW67MmjUBbyjYDPR977Q_hxGar8rGXHrOhYLD7TAs5yyralb5GuhVBRbfrlcChnBIq2Le9-LOWf114PjpQn9r3oY3HEYNy3Nc-qyzSAUyQnqMnRhsFLY3AWAoZQBwXkCsDbVV_TcX9HeNhv77VDi_8KL9FPhQ0VlmaoP-GBX3iwhgqQxIZberTeBiczquN6cve-L0fKyKvRmASsU0c45eQLi41FyReV8VC8nCmPYGVkve_qIaIS568V16n20kkjN71cfSiJm_A0u4cbV2D8T0ySoVxIIpHJpAJ3RNQX2UJEKkn--8snu9duJv3v31-k1XxEYkNFCrK_mg46exprHPQQj02CoMhrfhFM871NoBWRq2LEDztwoXDRVg987a2I9ksfFcQ-wRv4wn3Aepbp88wxUTvlQ9vaeewAEgvMwW_MhvV4Cseg4ODf_AknGp7--ZOp8NYDUeu-712JT6Bq7-1VmbG5HQKVf1jIjprVIGobzsT_LbIrUO2LxWxo8XfhRES7uNEKKf4WIgKzZtJX56oPVT7t7Nr19tSB4HrZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی در یک مصاحبه ویدیویی اعلام کرد که از زمان آغاز دوره جدید رهبری، شخصا با مجتبی خامنه‌ای دیدار نکرده و تنها افراد محدودی موفق به ملاقات با او شده‌اند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، با اشاره به دلیل کشته شدن رهبر سابق جمهوری اسلامی می‌گوید هنوز این احتمال هست که در رده‌های بالای حکومت «حفره امنیتی» وجود داشته باشد.
او در گفت‌‌وگو با یک مستندساز حکومتی در تهران که بخش‌هایی از آن روز یکشنبه ۲۸ تیر منتشر شده است، با اشاره به «وجود عوامل نفوذی در بالاترین سطح نظام» گفت:‌ «نفوذ فقط در گرفتن اطلاعات نیست، بلکه در تصمیم‌سازی هم هست، در جهت‌دهی به فضای روانی هم هست.»
او تأکید کرد بمباران «بیت رهبری» که در جریان آن علی خامنه‌ای و شماری از فرماندهان ارشد نظامی ایران کشته شدند، از طریق یک «حفره امنیتی» صورت گرفت و افزود که این حفره همچنان وجود دارد.
به گفته عراقچی، در روز ۹ اسفند ۱۴۰۴ که حمله مشترک اسرائیل و‌ آمریکا به ایران آغاز شد، علاوه بر دفتر علی خامنه‌ای، دفاتر علی شمخانی و محمد شیرازی، دو مقام نظامی، و علی‌اصغر حجازی، مقام امنیتی بسیار نزدیک به خامنه‌ای، هم هدف قرار گرفت. از این میان، فقط حجازی زنده ماند.
جواد موگویی که با عراقچی مصاحبه کرده است، در جریان این گفت‌وگو توضیح می‌دهد که علاوه بر جلسه خامنه‌ای با مقام‌های دفاعی کشور، در آن روز یک جلسه بسیار مهم دیگر هم برقرار بود: جلسه شورای معاونین وزارت اطلاعات در نقطه دیگری از تهران.
به نظر می‌رسد اشاره او به جلسه‌ای است که اسرائیل اعلام کرد در نخستین ساعات حملات مشترک با آمریکا، آن را هدف قرار داد و چند تن از اعضای بلندپایه وزارت اطلاعات جمهوری اسلامی را کشت.
ارتش اسرائیل روز ۱۱ اسفند پارسال اعلام کرد سید یحیی حمیدی، معاون وزیر اطلاعات در امور «اسرائیل»، که به گفته آن «فعالیت‌های تروریستی علیه یهودیان، بازیگران غربی و مخالفان رژیم در داخل ایران و خارج از کشور را هدایت می‌کرد»، جزو کشته‌شدگان است.
جلال پورحسین که از او به عنوان «رئیس بخش جاسوسی» وزارت اطلاعات نام برده شده، نیز بر اساس اطلاعیه ارتش اسرائیل ازجمله کشته‌شدگان است.
رسانه‌های ایران پیشتر خبر کشته شدن محمد باصری، از مقام‌های ارشد وزارت اطلاعات، را در حملهٔ روز ۹ اسفند اسرائیل تأیید کرده‌ بودند.
@
VahidHeadline
عراقچی همچنین ادعای منتقدان مبنی بر اینکه مذاکرات زمینه‌ساز جنگ شده است را رد کرد و گفت جمهوری اسلامی در مذاکرات بر موضع خود درباره غنی‌سازی ایستادگی کرده و پس از ناکامی مذاکرات، طرف مقابل گزینه نظامی را انتخاب کرده است.
عراقچی همچنین گفت برای احتمال کشته شدن رهبر جمهوری اسلامی نیز سناریوهایی طراحی شده بود و «این سناریوها حتی کد مشخص داشتند»، هرچند به گفته او در جلسات تصمیم‌گیری کسی تمایلی به طرح آن‌ها نداشت.
@
VahidHeadline
عباس عراقچی درباره فرایند تصمیم‌گیری درباره مذاکره با آمریکا گفت: «آن زمان [بین دو جنگ] کمیته هسته‌ای را در داخل دبیرخانه شورای عالی امنیت ملی تشکیل دادیم که اکنون به کمیته مذاکرات تبدیل شده است و به کمیته شش نفره معروف است.»
«تمام بحث‌های مربوط به مذاکرات، در این کمیته صورت می‌گرفت و مصوبات آن، عینا همان روال مصوبات شورای عالی امنیت ملی را طی می‌کرد.»
به گفته عباس عراقچی، ریاست این کمیته ابتدا بر عهده علی شمخانی و سپس علی لاریجانی بود که هر دو در حملات آمریکا و اسرائیل کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77274" target="_blank">📅 18:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77270">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3d1JMmVXUKUQj4UKMZM1gXozaIng2gt2oz-_PsY68lYSMgslkl9RatX5JePEfpzetaEFlFchfebFOwdo5MJXibP0EEX0zthJI5k8kohsTSmNpRbKDFDCUonbTCHsjAB36K9EHA3ZtWDcANED2YVVpLUC2dUK2Vom_Hl8UdP6AkBzY_3AoQLDyp0bx_DJ0Gfgmjt4s1VRHASVdHIwwkzE5m7Dj5icYBdsO82Ry9Ke7r913lZabpYz5E8p3COBHVFV0h5pbcxVw2-7ltpSc6RL74afD7BpKl7C7BWkbvhrqzI87-nBhetC2NLcDq2nEsHOemUizGXNBMlvnuR4P_8-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d80bc4cf46.mp4?token=SOOrF1t9byWHDbsb9_dksrQdCRcLuo-IZpjMmR6XfIwLGSCcWLtI5yAmosKh1D3qKFIOWLsg27rhlg4YTC9NhhzZVWfv775KKh8FOyTlvVF7LS3gL_ooqNlM6yEwTPg_DjWRQ6k6U0ZMcxnoYGZ3hPmcNgPdPaCg3Vm-7KvtkYeACrcppk2zV8RR33ixsZ0b7w9-EF2N_roKhz_NVHN3zROlQ-RszMGPrVVM7Uk8N0P1YruL4lRcn3izAgHLzzr9KzWGeKeylobGrpTL-FYFIBDcXNjQSj7Xm8WUTIHcBZSzorfCZA4rlaPZCVl0bO5ztwiigLKmv4oDpqA5XDpwww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d80bc4cf46.mp4?token=SOOrF1t9byWHDbsb9_dksrQdCRcLuo-IZpjMmR6XfIwLGSCcWLtI5yAmosKh1D3qKFIOWLsg27rhlg4YTC9NhhzZVWfv775KKh8FOyTlvVF7LS3gL_ooqNlM6yEwTPg_DjWRQ6k6U0ZMcxnoYGZ3hPmcNgPdPaCg3Vm-7KvtkYeACrcppk2zV8RR33ixsZ0b7w9-EF2N_roKhz_NVHN3zROlQ-RszMGPrVVM7Uk8N0P1YruL4lRcn3izAgHLzzr9KzWGeKeylobGrpTL-FYFIBDcXNjQSj7Xm8WUTIHcBZSzorfCZA4rlaPZCVl0bO5ztwiigLKmv4oDpqA5XDpwww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خواننده زیرزمینی زن که با نام «آنیتا پاپیست» در ایران فعالیت می‌کند روز شنبه با انتشار حکم قضایی‌اش خبر داد که در دادگاه به ۷۴ ضربه شلاق محکوم شده است.
آنیتا که ویدئوهای آوازخوانی خود را در شبکه‌های اجتماعی منتشر می‌کند، طبق آن چه در این حکم آمده، به دلیل «جریحه‌دار نمودن عفت عمومی» به این مجازات محکوم شده است.
این خواننده همچنین تصویری از رسید توقیف پاسپورتش در فرودگاه را منتشر کرده و خبر داده است که خط موبایلش هم مسدود شده است.
یک ماه پیش دادگاه کیفری استان قم پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌ طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
این خبر به‌سرعت در صدر اخبار قرار گرفت و واکنش سازمان عفو بین‌الملل را نیز به دنبال داشت، اما خبر حکم شلاق برای دو خواننده زن دیگر و اخبار این‌چنینی این روزها به دلیل اخبار جنگ و حملات بی‌وقفه به جنوب کشور مورد توجه قرار نمی‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77270" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aMgrnuoL7KyxQO2iQCUrTVa175W4wfo0d7BIKey9tANUvpwWfmvMORMTnoob-NiEM9pinc3_z1yH-Fypfv3fzX5meV0jaNd0NbAhEDyGYMQJ7w4_lxIDZoTrGbVaxDctA00t_6hQNrHoTrEd08KxUlZ3acvo6Na0nMW33ND84M7OIao88JCgmkPiCSbetjyNZS1xxVFQ2ys5b5QELbKNTzBx9YrccqSLJGrucCQWcPjMJPVKUo7jvI0Xn55DlDHkoE2p7PVJQfQedXmJvAgSUO4QK8wGRhcV0KbMNBlozvo4ccnguZI7XjqBGCOo1im_OH-9fgv_8zQDNfuSsdc0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنا کراری، شهروند دو تابعیتی ایرانی-آمریکایی که پس از حدود ۱۹ ماه ممنوع‌الخروجی و محدودیت‌های امنیتی سرانجام ایران را ترک کرده بود، به ایالات متحده رسید. هم‌زمان، مقام‌های جمهوری اسلامی همچنان روایت منتشر شده درباره آزادی او را رد می‌کنند.
جرد گنسر، وکیل دنا کراری، با اشاره به «۵۶۶ روز بازداشت ناعادلانه دنا کراری توسط حکومت ایران» از همه افرادی که در آزادی او نقش داشتند قدردانی کرد و افزود: «اکنون باید تلاش‌های خود را برای آزادی سایر شهروندان آمریکایی که همچنان در ایران هستند، دوچندان کنیم.»
خبر خروج دنا کراری از ایران نخستین بار روز ۲۴ تیر از سوی دونالد ترامپ، رییس‌جمهوری آمریکا، اعلام شد. ترامپ در شبکه اجتماعی «تروث سوشال» نوشت ایران به یک شهروند آمریکایی که به گفته او از دسامبر ۲۰۲۴ «به ناحق» بازداشت شده بود، اجازه خروج داده و این اقدام را «نشانه‌ای از حسن نیت» جمهوری اسلامی توصیف کرد.
اندکی بعد، جرد گنسر هویت این شهروند را تأیید کرد و گفت دنا کراری پس از ماه‌ها محدودیت امنیتی، در مسیر بازگشت به ایالات متحده قرار گرفته است.
با این حال، خبرگزاری میزان، وابسته به قوه قضاییه، گزارش‌های منتشر شده درباره آزادی یا مبادله یک شهروند آمریکایی را تکذیب کرد و مدعی شد هیچ «زندانی محکوم یا جاسوس آمریکایی» از زندان‌های ایران آزاد یا مبادله نشده است.
با وجود این تکذیب، میزان به اصل خروج دنا کراری از ایران یا لغو ممنوع‌الخروجی او اشاره‌ای نکرد و توضیحی درباره چگونگی ترک ایران از سوی این شهروند دوتابعیتی ارائه نداد.
دنا کراری، ۵۳ ساله و ساکن کالیفرنیا، سال ۲۰۲۴ برای دیدار با اعضای خانواده خود به شیراز سفر کرده بود. به گفته وکیلش، گذرنامه او در ایران ضبط شد و اجازه خروج از کشور را از دست داد. هرچند او هرگز به‌طور رسمی زندانی نشد، اما طی ماه‌های بعد بارها از سوی نهادهای امنیتی بازجویی شد و تحت محدودیت‌های شدید قرار داشت.
بر اساس گفته‌های وکیلش، مقام‌های جمهوری اسلامی او را با اتهام‌هایی از جمله «همکاری با دولت متخاصم» و «جاسوسی» مواجه کرده بودند؛ اتهام‌هایی که کراری و وکلایش آن‌ها را بی‌اساس دانسته‌اند.
گنسر همچنین گفته است حساسیت نهادهای امنیتی نسبت به موکلش به فعالیت او در «بنیاد کودکان مهر» بازمی‌گردد؛ یک سازمان غیرانتفاعی ثبت‌شده در آمریکا که با مجوز دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) و با کمک‌های مالی خصوصی، از کودکان کم‌برخوردار در ایران حمایت می‌کرد.
برخی رسانه‌های بین‌المللی نیز گزارش داده‌اند که کراری علاوه بر فعالیت در یک شرکت فناوری آمریکایی، مدیریت این موسسه خیریه را برعهده داشته؛ موضوعی که به گفته نزدیکانش، به افزایش حساسیت نهادهای امنیتی جمهوری اسلامی نسبت به او انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77269" target="_blank">📅 17:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lh2mOznCaBuSDIxbi4XbRNcTkGWCuqCbd2zlilDTnXmHwZtxVM0LzBiA-Kulloxnu-0W_vXSy-Dx8Y5PTtW4USWFMBxrII4-dm24LQmf_2SuPYYPyzn35NWzv5CmSlCro-HezI4swT97-LERBURfMVBnouKER269tnn5rOJIWNTB_AiHMFiFV_XCMOCmkfQc_dTJSze9EiNXQm0zXWnuJC56Wo11jyE5ni4Xg2J1oGkW_CGjE0B2NFvc_PI_YsgqViQHh06I3hI2QPg2v2gi2wJhSSetCQg5xe-hhZiIY6lL6j38pfNUAqKg6sYJB7CvMspuOFOd6NOXHau9bGp7Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه، روز یک‌شنبه خبر داد که حکم اعدام عرفان اسفندیاری و گل‌محمد محمدی، دو تن از جوانان معترض دی‌ماه ۱۴۰۴ متهم در پرونده موسوم به میدان علیخانی اصفهان، در بامداد همین روز اجرا شده است.
هفته گذشته کمیته پیگیری وضعیت بازداشت‌شدگان در ایران هشدار داده بود که حکم اعدام ۱۲ نفر از معترضان دی‌ماه در اصفهان در پرونده موسوم به «میدان علیخانی» این شهر، در دیوان عالی کشور «تأیید شده» است.
در میان این ۱۲ نفر که برخی از آن‌ها به دو، سه و حتی چهار بار اعدام محکوم شده‌اند، چندین نوجوان و یک شهروند افغانستان نیز دیده می‌شود. بنا بر گزارش‌ها، گل‌محمد محمدی شهروند افغانستان بود.
این پرونده به وقایع ۱۸ دی‌ماه ۱۴۰۴ در محدوده میدان علیخانی، بین ملک‌شهر و کاوه اصفهان بازمی‌گردد، جایی که مقام‌های جمهوری اسلامی اعلام کردند چهار نیروی بسیج و یگان ویژه به نام‌های حسین رمضانی، محمد همتی، سید علی خشوعی و ولی‌الله صفری کشته‌ شده‌اند.
در پی کشته‌ شدن آنها، ۵۹ نفر در اصفهان بازداشت شدند و برای آنها پرونده‌ای گسترده تشکیل شد.
@
VahidHeadline
این رسانه حکومتی معترضان را به «آتش زدن ساختمان‌ها، تخریب تابلوهای شهری، دوربین‌ها و چراغ‌های راهنمایی و رانندگی، تخریب پاسگاه و کلانتری، آتش زدن لاستیک، مسدود کردن خیابان، حمله به مردم در حال تردد در خیابان و تخریب مسجد» در جریان تجمعات ۱۸ دی در میدان علیخانی متهم کرد.
بر اساس این گزارش، «عوامل دشمن» در اعتراضات ۱۸ دی به «انواع سلاح گرم، چاقو، قمه، قداره و کوکتل مولوتوف» مجهز بودند و در جریان درگیری آن‌ها با نیروهای جمهوری اسلامی در میدان علیخانی، چهار مامور انتظامی کشته شدند.
در پرونده میدان علیخانی ۱۲ نفر به اعدام محکوم شده‌اند.
در زمان اجرای حکم اعدام، اسفندیاری ۱۹ سال و محمدی ۲۴ سال سن داشتند.
۱۰ متهم دیگر این پرونده که زیر حکم اعدام قرار دارند، به سلول انفرادی منتقل شده‌اند و نگرانی‌ها درباره احتمال اجرای قریب‌الوقوع حکم آن‌ها بالا گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77268" target="_blank">📅 17:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اگر صدایی شنیدید و خواستید به من هم اطلاع بدید لطفا فقط بگید صدا شنیدم. یا نور دیدم، زمین لرزید... یعنی لطفا تفسیر نکنید که: زدند!
آبادان تک صدای انفجار از دور ۱۶:۳۸
سلام همین الان ابادان رو زدن برق هم نداریم
صدای انفجار آبادان همین الان
همین الان صدای انفجار یا شلیک موشک از آبادان
نمیدونم دقیقا کجای شهر بود
سلام ابادان همین الان ۱۶:۴۰ صدا شنیدیم
سلام وحیدجان همین الان صدای مهیب انفجار از آبادان
همین الان آبادان رو زد نمیدونم کجا بود ۱۶:۴۰
آبادان صدا انفجار
صدای انفجار ۱۶:۳۹ آبادان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77267" target="_blank">📅 16:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی الان درباره شنیده شدن صدای انفجار که می‌تونه انفجار پرتاب موشک باشه، انفجار شلیک پدافند باشه و...
سلام وحید جان
الان ۴:۳۱ صدای انفجار اومد، کرمانشاهم
کرمانشاه صدای انفجار اومدددد
وحید جان (۱۶:۳۲)  کرمانشاه دو انفجار مهیب. احتمالا داخل شهر یا بسیار نزدیک به شهر
سلام وحید جان
کرمانشاه 4:31، دو تا انفجار بزرگ صدای جنگنده خیلی نزدیک و زیاد
همین الان کرمانشاه صدای وحشتناکی اومد
صدای پدافند نبود
الان 2 صدا انفجار آمد کرمانشاه
سلام همین الان کرمانشاه صدای وحشتناکی امد
ما شریعتی هستیم
وحید الان کرمانشاه ساعت ۴:۳۲ زدن
سلام وحید جان الان صدای ۱ انفجار از کرمانشاه اومد
صدای شلیک موشک آسمان کرمانشاه ساعت 16:30
دو تا موشک کرمانشاه خیلی نزدیک بود.
انگار تو شهر بود
صدای سوت موشک کامل پیچید
کرمانشاه ارسال موشک ساعت 16 و 32
دو پرتاپ موشک
[هنوز از اخبار ساعت‌های گذشته بی‌خبرم]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77266" target="_blank">📅 16:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGRYvZWRiCn_4FMiwdxcjHba-mJT7oZKFP3DE-wSOpOi-8voCF4Ce653UTuqEZPqHXmAowsrJiqEPnao9hGQZOLeh7yqFizzcTxepyiWw7hkOuvi2Xrnry2Bo0QZrqL9X_3WkOq5nz2y3Gf1pm97Wjn-a9PM3H7jLb82eIIzRKw-5FIzf-U6H2mLr_SBjECu1aKusZSnuarr80XhxNQy8Is_a2MvHyn63oSZFhuKSC7q6yBdqaQUQPOldiqFzg5pkXjlNlA16aukMT-qSDUFJre8UTZXcnW4y5xPLqHrdj6I_Vv97bwPvDncmw3Nz1Hi_4xSr0KB-z2lXKpREbgc5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار در کویت هم‌زمان با پیام‌ها درباره پرتاب موشک از خوزستان
آپدیت:
ستاد کل نیروهای مسلح کویت در بیانیه‌ای رسمی اعلام کرد پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی «متخاصم» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77265" target="_blank">📅 10:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌های دریافتی:
صدای یک انفجار چابهار اومد دور بود فقط موجش بود
09:42 بدجور زد الان چابهار رو نمیدونم کجا بود
چابهار یهو صدای انفجار اومد شیشه هامون لرزید
🥲
قبلا تو روز روشن نمیزد
چابهار یچی زدن همه ریختن بیرون ولی نه سمت اسکله نه پایگاه امام علی اصلا هیچ دودی هم نیست به شدت لرزوند
آپدیت: منابع حکومتی
فرمانداری شهرستان چابهار: صدای انفجار شنیده‌ شده در روز جاری (۲۸ تیر) در حوالی شهر چابهار، ناشی از عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77264" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BRKrFfMV7PHrIXNBv5jqnFMKebiDPCRmFpZeJIkE0hp4IebCUTudM5pdabknis1cXwqJPWA6kqu6Vc_VVya1rO-6W0DnkfpMW-MxMH_hmz9C1HWZb6IIA6fYX6T3pPSfpuDb_6Xe9VgJNkTR4OGqT7oyQNfI2kZ9jHWSfjYZqHlzZXJTtSfjzkIk_cG8E7_3cMwGcd0AbO4KQFKG7tIKRgpyMv_T4JS65_HIRaPNIh9LwB-LPl31jOwpGvweYrqh_UcfUhiyZ1cBCSMCBi3rqUwpKacwiuQbsblOvcwcmW7d-oOCm9Lt8wRZNwcuhlriVYjRqW49CnFDlahuuIBB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های ساعت ۹:۰۹
سلام وحید همین الان گرگان زلزله اومد نسبتا شدید بود
آقا وحید گرگان گلستان الان ساعت 9:09 صبح هم لرزید، زلزله بود
سلام گرگان الان زلزله اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77263" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jm_STqPAuAnxHLy1YdA5gsC0dlz8pdZ26q7jn1w4St1ZiS_ILLhLawtja4EbljgUm2sVxyT7sYTa-xRpC4jCRaFNALMED9MEy5jUCJnLZ9BwWs4YvRce9MQBrJe1juq-j3iihKRk_OAcmPJSC-8sMoQfeW0myUF_tVs9bqxmD0zyauEKjHk8gLNnhVZEHmlUWr2w5Hc9KaV0cmIjZdzHCftLazlxT6F-npV_-OTwycojMmSL0gXSCmFK1LPK-5liTyTJMYLKrFBZVVRwU6NhziUaXRsZzA4mKYY1q6EouuDT5sHLbyyHwTkf--g9W-vbCtYAst27nLIg8QJV1VmYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت: زمین‌لرزه به بزرگی ۴
دوباره
در سالند خوزستان
پیام‌های دریافتی:
۷:۵۷ اندیمشک دوباره زلزله اومد
دزفول لرزید دوباره
اهواز دوباره زلزله اومد
دزفول لرزید بازم فقط شدتش خیلی کمتر بود
زلزله ۷ و ۵۷  دقیقه باز هم دزفول با شدت کمتر از قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77262" target="_blank">📅 07:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77261">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTfwC7IYzgLSnkZ2YObSd-nRXwxCorbEMiDmsNn9a-CC4INpj7N6IFyV7fH-gJSraCxUyr41MrXJLMhPHjYBpQDvl5oNt7QI3jVD1Hz9LSOlH0g-QQR5OHAyScWhdFQAiC1P7fen26NvcNZmkmWcTcNw00Y3m5OUrKvjW3zRks00AvYvYNeD-z5dxidyAKXqpNZ_8r0pXZqjxODfMXkgqG4ECPJ4LnH-VvOEbHLye1N0wqHZggKZEE-R76ynEmX1bQs09rA3aPPf4EftjwHc2YeXWlDmivlzct4fU6_xQVqozLx4XSObE1Xrh7gnVQv3B9CBcv0keItHGxNVZTcBtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه سقوط ارزش ریال، قیمت ارز، طلا و سکه در بازار ایران به سطوح تازه‌ای رسیده است.
براساس نرخ‌های ثبت‌شده در روز ۲۷ تیر، قیمت هر دلار در بازار آزاد به حدود یک میلیون و ۹۴۵ هزار ریال، معادل ۱۹۴ هزار و ۵۰۰ تومان رسیده است. یورو نیز حدود ۲۲۳ هزار تومان و پوند بریتانیا بیش از ۲۶۲ هزار تومان قیمت‌گذاری شده‌اند.
در بازار طلا، قیمت هر گرم طلای ۱۸ عیار به حدود ۱۹ میلیون و ۱۳۸ هزار تومان و هر مثقال طلا به حدود ۸۲ میلیون و ۸۹۵ هزار تومان رسیده است.
قیمت سکه نیز یک میلیارد و ۹۰۰ میلیون و ۵۰ هزار ریال ثبت شده که معادل بیش از ۱۹۰ میلیون تومان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77261" target="_blank">📅 07:28 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
