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
<img src="https://cdn1.telesco.pe/file/UxSTzg0GW7OeUlzh9_9N-BkN2l5tF6pySNPVltXIR7ahEvIhh1f5O2qR3SwyoW8wZ3-SPyNYYKFf3N42MFgApop_AjvdxpBv-HmIRnLHWmEJJaUgh-72H7ji-fq4CONMSHnatdY04Tp2fpuBsRRjog4twFtEc8Hmhi12fikRwGZJTb-1t9nqbdnR2G5vAt3d0mC1C7HVtT_TW2h81PnTOGJtG83tWLzMkVQ1_W5sRgkv17Jb_Rd1gqSSO91-Xg1Wkn7FxjjjvV_KgpkfCmLOHT0DxY9b20EDlU1ONgEeq9TJQ6GgBATpEzZBWKlWVovDXSSkpDoQmXkWA_ukAk8tKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 07:40:32</div>
<hr>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZYkxKrQr0G5zd901BH_b2N1lx3vGZvBHZ6vAoC3WWCvJTKVKP8XjON2qhRcsgVnw1t5y36zV__l7ePGhFqE98QOR4EfR2yRvgKmuqxocGREzzc_GJIO3IntYRYugiTLwrmwwIWrtxiZBB4vpzVGDcT-8U5HDwqNQB4qCTCG9_rs05dAPbT-t1XyqcOCm0ewkxOUuNs2nN7xjQagonATx0YANGMbWlvdrc2I3bFNe68RTIL5R7BXGo9KmJFNEJHGaiIAVt2Kq4tl_TIhinc04ReitdLZGjyKAPs2i85t8y4dDxDzPksMyg8GWuWVmddOE4TiJ7LRMaZvcmR33Lenyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، چهارشنبه ۲۵ شهریور هنگام ورود به کارولینای شمالی برای شرکت در گردهمایی انتخاباتی مایکل واتلی، نامزد جمهوری‌خواه سنای آمریکا، درباره جنگ با ایران گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم. آن‌ها می‌خواهند توافق کنند؛ خواهیم دید چه می‌شود.»
ترامپ افزود ایران «بسیار خواهان توافق» است. او در پاسخ به این پرسش که آیا پیام‌های اخیر ایران را مستقیم دریافت کرده یا از طریق واسطه‌ها، گفت: «مستقیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I4BysKJRa3S__zqTOG1ZgTga-wmiacQtTIBXIQj3fE7giU2MPyp8sVVBr0QT114pG6NLybVMfo5_T8h1sFFXIYrXlafc34fE2ifkrvHHGN5M2ShjuDrx0v2PH13Sy75jYvUZbzs5IfcXC_uM0pfBbG4gtpvxMgX7X_b3t5SmXztZDF-IZ2NK8VDqYpRQPhROVqwG7qnaAyQnieiSDt5OzIPiRkCgGqU5nLWecpfbBz-SjGBBij7SDOrRkHBnDbUK2qge71YfX5BcJlPMRHLjLGNwS2QVh5_V37xIynQBTFJZPVNUA_l2NLQVStfP6Rc0yECEKbLqiY3wj1BkKpQv4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GtMxop5zSPdm3dFc21MEgkUmI4x6XbkRyMZFQZdrX8evW_pVL9K0sTMVQ3r_7CVPe5s_bGHORKlyM3Q0G6AAIVJIUI12Lb4J9y1kbO5p-Z5F6YTmI4QyU9i9Fs0Y_Fb5AED8W1q0hGVwjwkex-w3vHm_5AG4O16_c0-ehW0VTU1kyXrvJwCAIUEA9yvxbTZZZL9Qd_yAz2LcyCUFWpt_b84rh85PKu4qmLZXhZeVQFB8gq866lb49OM2zcTeKLK3lUyFbO6kbODBhsKE7OtkBYqlc7Th0cQa9_W5glrbf6BU0-HOHAxnsk98sgZVFO-Iy2VQ8Jlk0mGOrmDJLGY37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6439jwLg4p9A1byQPQCZXI2QCN_cLAna2GPQdeTV0HdJFsNB4swlODvzzwoxzf3p63Hod83vcdR3CuvA40V8v3rsynHDswke97KqKkEiSCpW8RHw2-zNtpsdNra3h2yClU8egg6VB39lLA-8iBwecZp3O2WxWrEJ1sBy5PK6_CNH1uTBlrdptwSHnz92_9wcQHSxmLUbYRwwTyTHRgfCJMnJJsks6DIfLopIWOBoPSjwl4X3_Cvtf97HIewuWrOdM6oKW8VZW9LlkvavttU06bcu27X568YLlza_5y0o_TLOlOUeVV9Fg9IQ7NYndSsUB-DwmC_-OtYz2Otxl_n8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hfEK_owwyCFqodSHoMj3ahobQz1eMowplYVwfcCyU6QKE4QFXta2nhUWTiaOBC-xbyJqLfUFWyeoBVynCTMigocIxG4bJPiIyM0d1G8h0AGHVicdtmr9Xa6Ko_G2ahy-FgbgafCxW9UhYVAeS8_tTwinPTYbtVioxr9yhflsM8xME4NucKG62icdpYhOk8AlZJSilVkrzz0M8sH-w7zmOYjL4Vc4sA_-LbMnbvh1IPTfXCFJK7-oworTQiGYOAyDE9xZojoh0PmOCNjtV91JAKsepdeFuRVYI7RXzrDBtCWdm4oholIU1iubkDiiM64URkXYABG3w1KZLkdxVuFYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP72fT2KRDrZiyPwFG_6nM-Ool1WNY_1nFqxEf1rqDL7p8YO8ccXbgnY9vrnBmseOHhKH-DqxgaAkNF9EPnas10Wiw5nEpoPb8_CsunQiJPtus9_ScmCI13dr61rdkyvmo_ka55Ai08TCKqFAXB9vvnykd-PwltS0xgXJxJDPoyvrE4NJVfoiPRhayXwS-iMZqRNryzkR4_QG4f0YQPaVc7TMQocjqcPwK33AyjiqrSmLX9M6BDAPEozVTggCN9YtLcPFZt3BC6vclv4olKNXKKhAO21O8NHV8NKZR_BlgaMwnszqDrAe5lBAUYSNbvreVgpUKx-Z6OFTqP_QPezGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XX2-O91z4XpXNWsHLSrONv2yUK7Gufzj_mh3cX4J3tPhz1M4MoS1WV7XR_3dW9-VIwqvVaWwlAUPfZgJAWqcUnkr7YpcIXSLUOxZUecOo2ZI1XmSn2_OO8Y4BT67AhClkJuU4bJbhglttN6ulN0VSSaGIrcKo7GNrZf4tEsFOFL5EVTRyKGsyw3l_Lgj-VIa0EFcVyIUv_v7pcKhO_OJwQWE8E4HQ2T92n5mqWIrGXce6kY2otEPPISZxfo5OrhcEPkSVMX0oLeBq8ZAsG-KbM0nEXEDt3bp5X2t-UE9EmgZEGu21mUt9cIUKWcSI1k9b0JnDJO-1yRXLcOXscK2VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=XScjw7jh2ABQpt8_V57nsITHOJ-d5msSebgewQIRF6xU8N6U1R851X9LKPP2KL9HGvcSNhEN4rlq61HiJidkWZ_Y8QHVDzjwj2X1Bk2lnPsJzl4XNIr7dj7GUmKp-XmBu5th-wI2JOzbLZlrCnE_3ALxa7prkym19cIJ3MKVgYK8a_qzHDQezbLHdBK1y2l9Cm6Hr45RTw7p8vPlbcj_HEGyfZtpB3ELWcwGGQKMJtxiLJGRbNLM3YYP2YuhC-yTW0SRjn8OB2K1KD1AsGN77gay36ek7Rtleg8xFCzw1TC4nGW8V5NnPGH6Q8ietSX8FtPVYpnALsIXK3Iv8PJdFX0kG1YbCIwhK9FfU5V1tS_xJ5p3i5F6XRX90tH0ZcIfpaAT3akdnxV7hYsb6cr_89uE9h1_8SSCNne7otrkLRUJB0FGD6et58F4M65NWJu4cZPFWQtnevPvjhin0xqk8a-OOBJzCqu3zqBfVM9uS5BcZSDywRpmGwgYmZMk7ZzsuJEvGV8j8gK_R9l-6UZhm60cVsqw85ZzUSvfEQqIDKVdaIFxbdqScMmvriE0lsj0uJmJRCmdsk0wRqnvSvRqyKor4cL6l4RWx2f35gyKgynVPnk803UVvt1b-Db0flRJkaJrXMw219T2tcUy-cp8XKEjby-YXGG7utonCrKyYlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=XScjw7jh2ABQpt8_V57nsITHOJ-d5msSebgewQIRF6xU8N6U1R851X9LKPP2KL9HGvcSNhEN4rlq61HiJidkWZ_Y8QHVDzjwj2X1Bk2lnPsJzl4XNIr7dj7GUmKp-XmBu5th-wI2JOzbLZlrCnE_3ALxa7prkym19cIJ3MKVgYK8a_qzHDQezbLHdBK1y2l9Cm6Hr45RTw7p8vPlbcj_HEGyfZtpB3ELWcwGGQKMJtxiLJGRbNLM3YYP2YuhC-yTW0SRjn8OB2K1KD1AsGN77gay36ek7Rtleg8xFCzw1TC4nGW8V5NnPGH6Q8ietSX8FtPVYpnALsIXK3Iv8PJdFX0kG1YbCIwhK9FfU5V1tS_xJ5p3i5F6XRX90tH0ZcIfpaAT3akdnxV7hYsb6cr_89uE9h1_8SSCNne7otrkLRUJB0FGD6et58F4M65NWJu4cZPFWQtnevPvjhin0xqk8a-OOBJzCqu3zqBfVM9uS5BcZSDywRpmGwgYmZMk7ZzsuJEvGV8j8gK_R9l-6UZhm60cVsqw85ZzUSvfEQqIDKVdaIFxbdqScMmvriE0lsj0uJmJRCmdsk0wRqnvSvRqyKor4cL6l4RWx2f35gyKgynVPnk803UVvt1b-Db0flRJkaJrXMw219T2tcUy-cp8XKEjby-YXGG7utonCrKyYlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NmhmiZKOEJEntBQoBYpeERyId4UcmnN_TSXtsdz6jdJmLdIAjIZJFuqwyYwL-D5acGx4ZTXpMFgkoIsauqnP1lrmWb1CL7QkIjga5kgyJUWQMMrVDzD-x4otwHM62jMjCnQzcxaomqMoe71jxCxzEsLvZcvtdfyAvUofLXlR-S8tFv-M853MsOaqXDmeeporoVC5yoUd_YaEw2DES_Y3OEEnv8J2tFLEw7mzZ31ni1TN68kR4jJ3ybLBwgnNnXylIeNC_XlqS3c87uRQev8YY6HD-VYPmZmoP1bNUqvGFiI4YWza_EolNQ7j7gwstO4nWrIA_VDKPYWW9h42StrRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NUWblWj3JtrqpPayyU3Mgln-O1gzJOo4-nf7YgIGXi5XGGAzRIYr46zvluGNBQAJejeiH3X_kYOPLFn7ubGox5CwcL_g24ThX_rIwHNrmvSBMTTZoyxa3AqN4Br_NWOwYGIcRDiZXgetgmsDPET05kALl44qGtv-N3qKGXrn7QHKZ5JQjnyYD0BGcKVxOV5qjeHBGXqWc6Ucq4P8-RSErLF2Aw-P3o3lzvpgqmOnkvrPHdkZ4s6HvGRGuhjs4MURDpvZ5CZCOgvVhEZr-FVU8bQPSVdSnF08zM8ip1Eg3p_68E8DKaQm5Oxk9MrJ6L5b5qouLuumolfyEUTkXaBXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/guR-Kg2hFufZuGqu9q_yRXRor7ntIE4ZAHWWD8czYcviYLrDuIjrxUfB6Z7mgkOiXW62SS14iBQZyQ4nSIbVb15UnuULeCMvdbMMCZib2REM1a4hv_OpN4Fm04masi5czALHiQPZqyfNOUJqiXwgTpSvH3XUaAGT2wUfsaK3NePebjwKTFlT9rBtF-w4XvOcRPlsqnRdOI9Fvjl4mliAWqcWbTVdHpgZ3r8DYW8OROiTMGQPdu2xg-SsoYMeiHr7m_JLl73wwB7LymUyGiD_pGw8VdTUP5HWzhptzbrekuP7OOSalKgD9NKjnrYaPS61VrP9-xAf1MuEFmZGnVQPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dLZt_lz5IKCGcv5_WegQF60dQCqmL20qPzQnCNbpe3lExDn6rKeRV8In0Et9JWx_DySyGXrQfrFQtGuzzC2ZkCStXev4_LCz4drAdFCZiViNOUUsk-gRGsyi4A0PoNdIdlBG1nj7ZxLEKkHo7g_qUpdDXrcq7N3YKQfsgIg7ARQTPcRVtw_xl1enSXZBaYZGiEuQhWb9sVrgthR4k04HdZEBDq4EBK1vRnRSgKk3G8nANZZcSlWWxqVni0KnXFNu9IpV9swl4KJfYnOc9bmDw9gvu2PP3MUP3afhXgMsCz_HSAwvpuvvswzJc5hf7WnxJYrRT1_egmDSprNdiS9s6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IpKYz-zB4g7R0539kHUWQNBz7uQfx28q1Kc-657R6a36Ml9R6NWlUHT7eSWViQKIvVcuVvZLNpNs4nWyLTwGaSnkUpQjOcj9e95ww5w7dVwgNXBflQAtqejo3wIXa9TxnnwYmRYwZz_VRTmE1Q3KxQ5e0p1fdUTydrcp0-rCvAIC-a8aJeXIf8Nk9UQtr_a9pvD_841blFxT5Wey-q9SMTFGpRTg1z13YE6aTelhRaqtoEdSK18CHp7TVaXeM5llY_9xT9-Jjo-EzvK7_F8S3IoRM7f0aeuEJKCX79oIlpDnny_r9rDa_-M30CFmp30ir8wOviyViGJMb-gu4DrLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P-2GZJ-fSZDQUg66LtwXPLrC99Bu3zdCHms2cbh-J5IR16AWfxj_G6doRcz7sajPadUJYxTAkdAiez3IGMw0-QYRTaVNMVzz9ZWvCH80TJc-Stx52tDAT42g-jDU-QfV0rJYG46NTLlhKRgrIVlM1bjBu7AyJ5bg1zXfqU8FfOtNsw-_ht5gDxUDoOl6SJW0_gFhwdE818tYDPP8nZrltZaCdpA0F5urbTwZd9gCc8UeII4klONFl1bUYRkw2p3fkSRY2b3J3cEHQq5McqtFLwZ9Ckp7qwtIqIsx9hOkLLWLHNx61ccGz2IImi_JA4JN4ti-lzhzZd3gH7h8bvnzlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhKJnA-r9JxrD572-G0QZImlNCpzX3AqPM_nVmIFtCUZevMs4WIKLJCGiJyKogYRdZbL0Vn7ojszMK1TvwWG2YYEUmaja9Busin4gSK4CrO72r9xeJu1T_YOCx9dZadh6yA-giNmlTQUgleF_VOfjnzrozDyHEj_K9DYq9hSJK1j5Kii6HnZOA59EaW3HmJJBmCoM5ELa6ZXuoIl7tYBHp1nRnnpKRcbyod4DIkYDsocjrsPuGWRmLKJENDOD3zKPn1ZhrJeiJUm_6HqH-WMXT4xEr5BzM75y32qaKG1rHvUD2TPITJI70QsaMh0HOO7iboljhwg5wZAt8fxrINRKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNtK8wMF7Ipz7tGqyguLV2bVx5vI5tuHOaZ8xdLCUAyH326Lv_ppm8HW-jyfuna3Rw6WBsRBZ0t5adZXnG_e_CVHKcnRKqIo1BrD7xHRxi4vvJKFEqWChQQZcIevfgpNB8VmACHMwCnUVm-KKHm-1QLZK53_o_n6NuWM4mZxVTqZVkl9FNWMwOR5dKC9Tcsn-S8DQ2dLHrxOqBI5hozYXM6LYA8Kk90mfAVQ1YS4cvkvncjE4fEzVeXS0D1wqBv7PFJPouI3gFLde1lBvhraUtjDL4VJPpc8j5jJKsaFDCq1IYvC8atvm7wI0DWkufRDFKq7zM8G6N23e4I3CeEzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=gdYa1D6sVj4Z3v_NTAiVfeAc74x7Fmsx72CqtSQxdMknDNmIAPciRtHp1wLfAqRZhgEPTUi5fGAyEFTFa4QW2z3xw92QYkqb496t1gGlFVxlb0mxjj5R0A_3iv5tNiKui7ZPIOnuPdRyrdiBXllNyjsp-OK3wwxoq0ACCNIHeNF1TmT06wpJq3AoxfztAqlS3FCRivZjdTzb-RzputdyK_TcP1ZyJxr29KKeFbXukjbiRgKoctBWyWzkNeIECK2v-mS3vOCG3RRpw8yshA2lXaERxnqop2PyA3xcISzlvZXj6kZ43zH-CFnTCxwUcSDYYjBCt3uSNls8IPx9-qSVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=gdYa1D6sVj4Z3v_NTAiVfeAc74x7Fmsx72CqtSQxdMknDNmIAPciRtHp1wLfAqRZhgEPTUi5fGAyEFTFa4QW2z3xw92QYkqb496t1gGlFVxlb0mxjj5R0A_3iv5tNiKui7ZPIOnuPdRyrdiBXllNyjsp-OK3wwxoq0ACCNIHeNF1TmT06wpJq3AoxfztAqlS3FCRivZjdTzb-RzputdyK_TcP1ZyJxr29KKeFbXukjbiRgKoctBWyWzkNeIECK2v-mS3vOCG3RRpw8yshA2lXaERxnqop2PyA3xcISzlvZXj6kZ43zH-CFnTCxwUcSDYYjBCt3uSNls8IPx9-qSVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NeBglQVxA68kDF0DlfDC_eyQcW0CErK8r72EOr0PtGCopckpbixybSWAMOSNH7C98jA-C8XBVpYrMW6iiK6KtY9evVJyGTNlM8Zn3viIMYMtdQaNrLU0wNdSRjvGMjEKoM0cSAVoTW-IsJxmmgvIgeXdpKFgW8CWq24h_sayPhzKGhF_KLMMR897-KylYQczFygaA8ZzlKlwIUZWhNTQ83EIda6b7fuuQ4BuOvia2C8ghX5fELdHZ-lcqG5VLP6-2CispqLT9WcwMENpI3GM2ot6iCJEK7bSDh7u2MmlgpbWrZNf8wsPtGlrzfhrmBEZBVAWo7gYpmyCOUXocf1AoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=rsaP9CCyeLLxiXVY4XxI1Ff0Dx9cEK_8kLBak7ccT9RxxBx9N4j0XTf-Z3NydGcYLvyiOqXQ8oRm4q2cG19INDum_AHXovCVaikwUe4aJ4EDUE7OC1tzpJQIb6ezBkv-D1a-Q3KwleWwOep9_B4lojNfcCcuh-6Z52MoJxBbbBjFfDcRjeNK0SnoqQEu9yLqqm8K5uGK9X9inEv9IBfGybHkIY_BMDwUtUzoILULMwub8QfZld8Rku912Ype7DpfHbEIm_s5bcTdyFyD8sDQ0D5Xefpmp5MI7KkqIF3ArajCVSqoKRwqoVgOUtYSCs_1h1om9k02oJOKOQ2hRm9Q3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=rsaP9CCyeLLxiXVY4XxI1Ff0Dx9cEK_8kLBak7ccT9RxxBx9N4j0XTf-Z3NydGcYLvyiOqXQ8oRm4q2cG19INDum_AHXovCVaikwUe4aJ4EDUE7OC1tzpJQIb6ezBkv-D1a-Q3KwleWwOep9_B4lojNfcCcuh-6Z52MoJxBbbBjFfDcRjeNK0SnoqQEu9yLqqm8K5uGK9X9inEv9IBfGybHkIY_BMDwUtUzoILULMwub8QfZld8Rku912Ype7DpfHbEIm_s5bcTdyFyD8sDQ0D5Xefpmp5MI7KkqIF3ArajCVSqoKRwqoVgOUtYSCs_1h1om9k02oJOKOQ2hRm9Q3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mMT7pqLGWnEabH4yPwKTP0FQpo04LcF8E3-lqA9e28ztAu6-aXDdM_IdfceECXDefAhI20MmowGvfKi7Xzh97ILH97fuJ5j_2f9xlYDjGjE1wH5EDRkilIXUH2FvHS6f9VZeoFCoCSEMK-svMq61Gx88kv1WBy4RphMniOtKiFawifBACDr199dvTnpm2U8ix8oCFo7oNG54JpsjFJ0MmlqhPKDkVVgGVJlrJmQe6T0Lv3Zuh1vutpJKojnRdC6Pxg2IebVy11Rbj9nLUsUVTbJpuLd3xqD3JTibTa19eSspaOI2stcPsgkYdi-p15Rx0BBiR78h_l05aVhEm6rFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om2i5AQiElqCUP7gmdW4o7Y_l6B8ZTXC3Txmp75dsaim16JX6KdyPcpNY0sRuqspKTNtPwdfX6w6d-dalZRBUuATzGPAxLLq3G4K62jzcBKQGaSeL0PO1eNpmglyEugrrLYSiBRm8Ff3tCkFvFNOCnrfUxhfnaJ8BQvV_-WQwPlmFgcrykvxMQoZE5zDeqOuPZOHcRS1Mr96iUpL6goNNln0N7nW9ovrlvgQ8_YHoqFKRNjxDvzH7NoWQv-jNVftvkPVee2wu7fPQRCIxIGe2KA5Vrqj6GgtU_a1-4Y7dDBiX-kvBjREk22-quo8qFuzZkgky9N-9AtoUjrLqqB_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DWDKbx7EfxgtKQfP4e4Bgwa1_R0sS7M4UYl5enL00r3gNYxUshKRxnZTGzMaLMIMG3hLZIe1vpfr5w3E0XBuxbOZNZyjcrCyRBudCe-vrpDcvr_BTZNdT4WEf3MEz5mlJkfBhmw66BKT3MkM4YrEnJ5W1xxkfd4ZRF69xVX1YFqn6TzXtmmdF2M-x4nRVpEuIDgQmxuWPKeL2ZFDYnrh-1MU9AXsWtKD9MV0QqxRAHH76awlkxJMIIvKeCBDNV0SfXxZuJSA5Ttqi9-eQNaI4W-Hr86Sl8NKWrP3qKwkKlVhyrl8Rp5FBWLK7k34xr3TNqNKSFZdo4hO4_MhWnnxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WPZBoO_T-W7UPE0dhme1wo3Zyp1UoZqNA1x0E-wO8s-rWEE3pGIlpwnZPcDjkUf_A9hVwzIm0bEubt8NFhgpBc4toWRKTFz7nbGTdT2DkI5xIjXra4k8mswOEaQME4Us_cr3gp7n6KpDf72BhpaY5G8Mrkc13V8BVBb2ua_mUm71e6a4LwN5iYzYfHEds1pVkYOVlCJKJZuqU9sPutHc2O310cj-hV5e_w62ODct1epAOBUZCtP9-gqYN1664o_cC4rpTHvBn8LcmrySXdnPh8o7cAMQD6229W3rMx11Dnn_8h0_10PlofZjhldMRA3JVE4qLM-ysnaC6UWcJAF4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNschIJKT283ulqf5md_7RD1BrcLU27-Gj1E20D-WaVbTrY9YEbFf2SDrRK3eUOQbCMfwr7ksMRgJG7qbdQ3qh6p5qGC90UJtMmUVytow7RNIG9Ef9wHHj3Mmlkdlh6tQzIoq0k6v8hi7b3kjZ0KjL5_SS37GvHDIAWVoMuixzHFDPzeSuYqTzkJWfDm7VYm9zxiRHCyVP7743FNNMsuBLuTbFbSKufNudOZQACsyGv0fESqCYy25V3YaSKaRx5EsuYrGzUAKXSXsPTNpIIQg1De-eo5cL3g7PJu1yJ41963SotmXUwrN7lk09TztG384Av31eiq7IJuRlRdUQMIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bxfVpAV_c9vW871qOs-N9VDYHRUn6E_XczMZQIHz6ZP1HMtInF6nOjKfjmpa9xXqHEWEHyTOO7ZgTd4qyc2aWVdFblwX5JMEW_Z9m8YPV97GFfd0xe2xpF8MbuMcSSw3DKvtDfHlcUVt8CFk8ydm9jIF4MSJF2zuBudWIx4Z6JwBZUExrzUhg1OLfYE-IeiGlhpDtA0XStDQEdtCWKlRbzdxZLSN_I1Fa_TvW72Z2o4Wchi8aDxe_JfzSC12zEzrl09VsfKkpDFatL2H_NwtJs2xhVXITzJkzu_Nxw2vKNPaEkVmxuDC8LsWQzLECd5-sq6An8yRghS5BORoIcLpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GVekTAe6Gp4iyiA0qLynmNpRiJC4ZfPgK2qNCH0PKvNsCmTw7hAX-gNkWX-IEYzK8i0uYXoXpIUeGLV8fRkSMrGW3HOuJyo1P5fODrcADSPRzzSOntNvQeQvYm_zA5PnvEgcGSSGU2qk9uYGYSa2fCMw5hZNTguSB81UDck5_c6zVqMHApldMm3RedGE_58d1ZILYipXn7xGBNgZsNowbVejfeL0g5NfVkG691bLu1binHgU7vDRnUW05tZh_1MbF7OHzH1ynKab-UltCvUvOs8tia2UEdqRW0C8uIswWeLXkKz-WzUSqMUIc748w-EzOUz3FJeFz_G5gzwZY2O_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IWl_dcD0-wVNHJTH3QwUQQtHK0jhD7EWNzeVTajmZl9mCQreqrsMjCl1h2vbhd7eGZjPuNRNLKZoI2QdfsCQF5RB0IHfxfiHRuY8YMzybsRmSlDuhxOPE7yW3m0CGnMm-yK7LoEOWWpCFUQevy0BM489PsTRC6jozN7xKbT6v2NxhVK4WHXMPziL85u0fpJYe2-KwmE4H2lRaNo7ycJvIQwElrCf90mAZ1atmV2a3MmW9VzjfCtRG4YL-zhG94uT-4XmohQm34Ayxac0loH8qeAVkPmIUWuWT7ri1Q2etB-ygCJiydW6_xk-QKEAS6KoYfYkeM4AW7tDxSyUIuFXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vMuiU6bmb3Qd_rStyEFRZsruqEtdt6t2cxdWpY4_TIj9ileEjrycLqDUshhhjdP03nhldXZxk5ZcTBFa6tfQ7wHuVI6taVFnbPVjpO2GXw-E5Z2ECJnYd0uke2xGKvaj-lvqbkuKwq-cSci-nJn1xWbDEIo0dh67xKgI4B3ysppVO1-Se3QhAVnlriUn8BXgIWjhRMtsrtXHzJ9hAst-rkOBELwEnGS0HvxOkeSEXtmH3KEKcf_zGASRqsVRC7jbKOCoMUt3VZib6S4WL29XjsNRWK1vcd_5a9B238KF0DOjj8S2lTm2aIaOaDnkk_dkec2Xwp1har1eXzycGo9icg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CkQRz51vNubSKxEwn3ir3dgKdgN7WdF6kK--4vFgl-jmBqlZGMvaUAVy_nf-lckwU7PwFXI8mkh18OpVkmG6jFPMLt3Fq2LmPd7zFVy9oX1H1MCs5oxIi_gh0WXUkQYH5423xYoRLPsNmCuOgA_s6yul9SSvZujRi_htjW2wyjUuNOhKWbR7YRwQijn50CEfXqnXm7YRlvJt2yhPwykcop7BwWtf1R7CaTMf7eceGvPYHXYdec9vEo9kuATda7VDV5bL-E37K9z9rYs7R7w6UBVn1UShiZUw52DNjSxBWaEkqjhZOgqhV3-17cux3vEorN48E27C_aCgXUpamxk7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vUiiq5K5f07JeCOqNi9ulB9WC4tacZX6QKMDmR6w5SrKe_DdtTmUBNxO25B4XgTOn-dfZrCu6UWTapT8LWhXi5qYg3-yJk1mxWpcNJ_dHC80mEbwJ4MnaOvUM5DPOLwwSavbtI4p7F0Nfqp3afZG3nvZwuJkFWRarxw9xMTdGCDCBum8_aGske_7C4gmyhyD9QGaCFM_OSTNKX9VW52-rNrN2PH8ChHquX9E-DIsLsB6_T0VHQlWzegsTRLddu1bMZxxbMvUUzYJYj_rXRb5TBF6Cs4YW3-ChmWIyFEMYepHw7H01XXKnaZiQDQs0DttwUujJNIm76KxNOm_0SoZbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6VEDhUTt5uJtnE2LSp3_ViKZVZH3ldTPlkfudgrOOOm7MNENhuqFhn5lC9nVdT1EEIqVprZFhbFh16Hf_AJdmm0sbvyFrj4iHJzZvfoyG6UDps1YV8PXep8DMQXZUtwc-UJMgDecxiUMAnfeGYbfPlqdqVEGXhWDdJksOYDNkBJefWgrIwgQWUAVyyJ587-ZFraQY9Lgm9BiHLAqoQcRDbITOVTr8XkZ1RtNd7QugWxwx1SGfULjd9pa-qZwdbD7LR0mkcZfsf1AJaj6vZ8rE-tQAFQoUbPcuYHK4LdNDSGnUZlGFdR0Mkt9rPEDmm9vYiqbCxc8ZcTsGwWavjkIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqCCnPha_IQi5USamVQebTvLA5Sa-tq00TFz_T-ij_5Qsfk6g0Axorkp4G9q-5reutYV_MmvtbG6InpYeqhgNCVre0dm85a9CmKhkSI1Xgj3veMmMg3U-5bGbKlemljjGng0kIItMb3222xvnaxa0Tx_oH5F2LNDWjOssliMXWg5xwsuEYU3PxTzvd6nUUur1wwbHU2F9lGl8qLrV5_zGucn8SiY0UN9k5MSrAPUVJizaafXTdxuPVi28xPHRJ8_mMZpY4EXZHSvVv5Usq32Xm5Buy7gTmW5BnGCxGHx8hWqPUlLFG_QiZ_oVHs75Mt480U71Zc6U-FvNdtBtrewtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jGjmcbFAmDIjRyW1R3DGSbAaOMJ5apk-0Yf9jNo2PL5T11JJsCVtdhb9mJEd2vItxcQ-2ge4my1OZQHDBFwd__JQXQgNKmYKM31DDuUDk1eJZL40SiM6-drJWNLpw2DCCYn3kaMqaqEvW9H9u2vfI4-DRhz3KY4ZNooZWVdUpf2ypl01iNk6siLi47PCjNPGKsesmOGXp0c9RMePVRAUS9b-s7GNEpzXJ1uGEcn2KEgmJqSvDzEsV16c3GiEaCqq-w13Jac5VbTC-4pHcnIrvy56H2-mxYmul_hbVB4LXYNa6G66F7q3jjLuxo_Tvxx-2ZWlLJiIJGzQGdhBRHulPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش الغایا پس از حمله در سواحل عمان و آتش‌سوزی در موتورخانه، به یکی از بنادر این کشور یدک‌کشی می‌شود.
بر پایه گزارش رویترز به نقل از مقام‌های عمانی، ۲۳ خدمه از شناور تخلیه شده‌اند و دو نفر همچنان مفقودند.
روایت‌ها درباره علت حادثه متناقض است.
سپاه پاسداران اعلام کرد الغایا با پرچم پاناما هنگام عبور از «منطقه ممنوعه» جنوب تنگه هرمز با مین دریایی برخورد کرده است.
فرماندهی مرکزی آمریکا ادعا را نادرست خواند و گفت شناور «ماه گذشته با موشک ایرانی زده شد و از کار افتاد».
سازمان بین‌المللی دریانوردی گزارش داده بود الغایا روز شنبه آسیب دید، بدون آنکه علت را مشخص کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gv6dblIqstjYN0mak4E-ZSiXGWfpbJikjSoz0l6FxGkXAHTrBeAsJ7N5meBtbE55rccSEjjIAaWCdl4dCSi7zXOVAc-H2P3ktY740B1j5lMKaO-cwqtpfVa0eOGBMoj7L3SojeZarIQyQcud_cFSPuMySwasFPqmNNtRQfF5s0BZ3pu-kXkltR2i-8Q38x8Tp_3d0I69990OKoLJrmgKNaL-GTrZv0HU0N-AQiaYOn6axD9zdz_mYFmFKv6LJa8pIES6dCkG6S0AdkY9YFRxYje5OOIE6lAqO9ls7GZb-JgdoRHYA8Z49iJWJm-e3TqotYyJFKrwm8b58u5w5A807w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DQ9A7ocswOlK-6dp63IPcq7Z-JHy_BSXYP_ijo5O-ovWllc4jepljYmZRncXkApSStCTo01LZdk30moXnQyiA4vAWYgOPGyH7QlO6OaaJoTyqxb8ZzAw90YiCeDzd1VpLxKy3_l-vzqVPWKF_V2OenhTu6H1UcFUo1OzuUvyPuyO5D6_Dow07Q7tVQITybCMQQFa1zzfZ84g4LAGO5zMLu7PJkYPlkz_eM7LlgJUE6lCRkKtCql2XjF0Zo4Qcu2ej1a0JYp2mQJvde73-JRjS6dMvQZ4vt8dPTO6wRAX4FY_Rq5UgD21aiF_iTyhLAuMvnymruQRVZzaYScnad96nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
آپدیت:
اکسیوس: آمریکا دو قایق سپاه پاسداران را منهدم کرد
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vYhZ49lwHqFrbgKbKX-kKszxEbbEel1vfySob3YGYgYyoYXjdahHE_FKW_WLPdkYil7JHDrYl0plFL_KvYeGXqGeUCU4c6HiCTwdg9DwTyjHQnMojH7vdU2pDV4L7LdD2uTUK9AhuuRac-0fTVgZ3n8Hk-AKU982z-YlxT2uJ4xsSf6ZSUavI_ImO_Q2cwhR3r56tqjj64slJgB5Czzbasq2jkMzcXGGB6KZ7CUw0CrlsnK-kBA2QM4HlkUMonoKQCvRD4txgZsYiQfFaRcnJr3DwnlbzlELeVHNe-x5qcDLc6pjfDOAD7JJXn5bflvJDIigiJelE26adqKJZ1BZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی نیروی دریایی سپاه می‌گوید یک ابرنفتکش که به گفتهٔ آن قصد عبور از «منطقهٔ ممنوعه در جنوب تنگهٔ هرمز» را داشت، «بر اثر برخورد با مین دریایی منفجر شد».
خبرگزاری‌های ایران شامگاه دوشنبه ۲۳ شهریور با انتشار بیانیه سپاه، نام این ابرنفتکش را «اِل گایا» به شماره دریانوردی «۹۳۲۵۳۳۶» اعلام کرده و افزودند که «تلاش برای مهار آتش بی‌نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است».
فرماندهی مرکزی آمریکا (سنتکام) این ادعا را «نادرست» خوانده و گفته که نفتکش «اِل‌ گایا» که با پرچم پاناما حرکت می‌کرد، ماه گذشته هدف موشک ایران قرار گرفت و از کار افتاد.
@
VahidHeadline
پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LEkOf4ffXV5KdR1K9xMDX4itVvIntMf3518KWqD1YVfYgl4NAynABTuOyoMVh-dAYt5XUFDdRBqsdJqRih1d_945cwtF1pa3oPY2VBiaBAuuW-NljVCeU0_jtpi1t1m3kk7pgUGx4iILfGAizOtUa5UX1o7Cbfwcb50c2nALG-U8vYU2ksGIQ_ron3EQCPIvhGlivRG1KcoT99YzGR9b3F90tSr3kvLqw0oyjbUfQGglegX137XIC3U3tIT3cjMCGDTl0MKz1qGycaOiOnLLbIydD7pM2uOu3MmxI9_-4mF2YXuesZ3geT3lgIaUYVxuBRomImh8Nty2O_K5Y3wsiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QpVAykl9-yYv-EZ2HPf41MYs4_IWOPkGaQzKiqe0UImM4WXKDlcGXA3s2enxUStNPtyWwIG9-xh3XwiDsmha7bdN8g6sGz5fReilaUgr2M6G4JYkLMWq7J0_3UOUrBsZZKkFu3OBQS0hlpjQKXR-SduItKD_BxEdy69-WpfVJ-mmZDwkoSmYIrAldWuYr1Wljcj4kR2u-BOjHd6FDFD0pj-H_lbpINK1Uco28t6GvfETA1D8PL6c1PYE2junl4YhzIYFWzuuwmv3_WJHuAmWAf46kiHNzeDxSnrXGdtvQbz_mk67ntw24SWUCMzqtRAgWPdoM4ftTJ7yo0AS9wD9Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QPsUSmpnxerCwws0iMnD1UewRXG-09yWVpmz4Ir4-WlBzTMK23cCGSgh2hJpL58srM7hz-tdXCRNvSSXuMq34XBSNY21yrnOoQxq3nV8FSy2ZJ-V2XGNpdXVkKulpC-qy3ZAFCtsADBxGgIpkTgs2fDzfLtkEZXVvUV57xbc12Z0Sli_Y__Un8LSZUVyajU7qHEIMM1RENI9HauzgMLv4gxoGRhg0BXCr976xaFnyCOmOZeFuVhrfSXK6ogd4QqvkFKT8_AjDwHQoGxGc9yL-SM8-KM38Zh4CVUiyMUEvHkI8jIycn-fCfKpsgg4qk9a_WSllpQBs4Jyp0m-Ezj-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=ODU_UINnp6SJnFvnVTXXCPOCRzDsqXwt1_Jvzae_g23XhzLHPmGegFo7V2XiNf4AB_eGBLaKYp-c0NaW4jxsPH2RI8neagCSu37U-W-Fny8Rz5EuNx555MGipbiC6uxFTNpDtR7s2Y6gNEr_0tTpX1am4wROJ6k2U9KQnKkc25QKI3kyQmRcn4N2q9DZZkL8RwyKIaWchLgdE8_1Ib4HTWF-a0V532iwszkkE4QUQif6-8ZWjEbnvc1lSVPsP7-gjRULPTOksQD2yqifpcckJyCYFTJcjmdQ_thFICSG-5XkGqtxcENiFoaRFwhB8WyUxeho2bSQ8mWzPI9wa5VW7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=ODU_UINnp6SJnFvnVTXXCPOCRzDsqXwt1_Jvzae_g23XhzLHPmGegFo7V2XiNf4AB_eGBLaKYp-c0NaW4jxsPH2RI8neagCSu37U-W-Fny8Rz5EuNx555MGipbiC6uxFTNpDtR7s2Y6gNEr_0tTpX1am4wROJ6k2U9KQnKkc25QKI3kyQmRcn4N2q9DZZkL8RwyKIaWchLgdE8_1Ib4HTWF-a0V532iwszkkE4QUQif6-8ZWjEbnvc1lSVPsP7-gjRULPTOksQD2yqifpcckJyCYFTJcjmdQ_thFICSG-5XkGqtxcENiFoaRFwhB8WyUxeho2bSQ8mWzPI9wa5VW7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQZh4PbYl9i6FZcDB0eG5vD4UkQPs2McJW-yDgxgFnAbLWhKTIPHaL8bwc5blxAOFfINflnUXyri92V0Ldr4qutfgLqh_sFXk4ruq_HtpD6mI7EKv-5qKzpMc884e-iZmHM0no_cgk5w1XxouTjUfFozAf-MsbA2UxJOO5RHMUELOlwxy1udAf7ajhccShSk434rtD-K_k_QAhf-La-x8LQHCjHh_nu0BsidHSv_KjqtTuti5cliT5qaTHAazvqXnXZ_e342JUjjHOr6jRlZW5nZmPe91BTFoIXJ2TOmpiUtp6QeRdQKQV5SENoFiT3_bgpxNSrDrHT7RonDzTILBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=k7z9O5VszYNaUzYx_YM5K4NBUiLLMSOcfRAS-H1Nb9UbHeLkpToLsPbO70KsMitq-xhj9In7y8-JbiqJ2ormhOZginyF8kjbtRfu4enjR27JJiV9Gq-uOCAgi7rMOU95D6sI9ciFOGNLuG5qcqQxsENmVUbdc4vL6QCdx-0DG9GGCiHS6QGi1gRK3nRPC_KaqSkUhnxMP_Vq-e9ecIeRxuTFA4jPNkpy7905CJDQYCSXOtZT2oZM2fNeYm6cd7aND2eBcGsMyvBi_i3CBCyT2UNY2oHZMMny0eByRvu6PUG2ou7gsm4uf5ElLqzHF73BIty0S3NDqMF5YewJKmI_2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=k7z9O5VszYNaUzYx_YM5K4NBUiLLMSOcfRAS-H1Nb9UbHeLkpToLsPbO70KsMitq-xhj9In7y8-JbiqJ2ormhOZginyF8kjbtRfu4enjR27JJiV9Gq-uOCAgi7rMOU95D6sI9ciFOGNLuG5qcqQxsENmVUbdc4vL6QCdx-0DG9GGCiHS6QGi1gRK3nRPC_KaqSkUhnxMP_Vq-e9ecIeRxuTFA4jPNkpy7905CJDQYCSXOtZT2oZM2fNeYm6cd7aND2eBcGsMyvBi_i3CBCyT2UNY2oHZMMny0eByRvu6PUG2ou7gsm4uf5ElLqzHF73BIty0S3NDqMF5YewJKmI_2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KGIwAGy6TGjgEpffXCAzQrH7zbTY5_0nHt-_j50lmoNo91Boo2zHDEmrFV47tMm6S0kDP0dGcWRuhT3bwcaa7fy-mvAX7p5dvWUsEBKOnf-bEDQ-LL5l9y6kbVMtqK_tPYT-V2OMEdKCxMhCBbWByYWZe3yuX2BMEEBlD4kp-veLGwFOxPMt4Zmr-VwqJ4d_3baaU51ozFhflu-pkxiwUEQ27k36cPeGsHTlGJ19E_vPfnl8sV0TaRMMt2Razi3QtErvvWwKkfDmj_ItJS5OUvgSV_fcXi-oQsBIRw-g5mH9MjJ6_dtc1jEEZTzk_NRox97FpXH-alphVx202iDS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aSXGDZ93XmVZvJNdL-2WsEJR8Bin-rXrnizcnWbmpCEGDzEDKbqvDKIfMHM8nST9Og5F3Mj8YLbHOqTxcwM0Bo2zgLXGF965m_viTh7yRkNee5NkhtHCZN8Ka1ievyWYAnDjFlyRp-aaHW6g8xfHhmQT9xdlVFWgPw6mn3VkRmez4Mc9rsbl_FqTxxX-t1_BrxEO3Way2RyJQi7WUnwAxoX_LiXwGa9fPu9OyLOcVd84iZs2FWG3tKwbckG10BJeXo5JBMdAoD8g-o_Xcgach9KSEl44eoBtS1rApb0a9z_-st4FFLXtC6XUzsXzyTh_s491dthbZmIUi7RKhskyDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwyZQDjqjRNA8UEw4YakgZAeXV3crZdTfqysGF4OOxSlR8duDvKYIIC3z6Rnl1OPHIvrH3el9R4sLk7FNC40DqWgbnWTlvl8zPuhU1JBC7qfyTw2ndnwmRz9rDM8if-CRcfqlBXokd5dk4m3861Vmh9UDLgup_L45MEFR2BeDsw5LNuejxR6JBe797EAba9HC5aZPO7ZnkqGSW0RG5AXQMfisopff1MnrLzXVLHO2jnSkbBZNaZ4Abk7zXKB481KBxMpOH598nXvoCTkRlPKdnN5i6SUT0kKC24wiGCTDByG5G3FFMkkFtexy2X3czdBLPzXJlfjJeEx5wPZBuG6wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/efclbdzKC9qILTvpDU275RKbrt4z0IX8ystPkYbDX9ak-kuqnQfDmwdIVPRmpj3HniQ73QJMOPcWKtOCdZvHpXPml4vOfylkeopxj_xafDhLZy_XB9C3PUxdXpxZ1JAKd7Er8dZJAkhaq8ftNUBB8JApVjuhuwsfr3RDeZ4A9aAg4cNG0Mmf1qH1wTgw5ALq3NhtpMhQ__PtaK6ki9JFhX36GoUE2HLqQ-PFp6Q3q4W2GKN8FOmFXayPEU6C89CIeOJoIPtP3Hm9My5424MdpOVpWB-7nOxQPQkr947gAWGL7xuN8Md4eJ2huS--s9SiSCKxwvqmvN7kxONEQaHIhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XZJY6DzVhYKP2exzkedK3oAHQLZrcGKkX9CxOOiQk870UCUdSuPa0H8Sm9TwNy57UVV1li0LXBjoY5TtcEOR6hw6pEEn0bd9kQTG3d43loq2GdXheg1YGtzuSooYf2qbh6sCiOLnVXjikDTmTDUEbUf6YGqucGM9qHrScwwBP28uG2hb5CouTdieKY2VQ6_houPaJXZuwfNU4r1dC3mpxj4cgbQeCJDy27q5f3OiCBAFY9OAGaaI2m8poswGtxcSUpcLx-mjmKWUu-KuztYpi7J-VRYboWIwF5K_IPPl0VEOBOqe_d9ryyfHt6PgaAiFIQNwP8Qvr3VqQtQbs4w0dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WU8ProflRP0FzK6yJu6mCrNEfEt4lenmZg1s6AQG6tKk9U66_PU9ptuu4laP8jbYBxYx7Ooq0QUECSI5UdY8yBLHD-QW7ZtTRbuN7vY_Z56i7h4hkwPVfpRLm8T8_rL_79OMEpP28CnLtLzMWOd-RqWC-oAYgO7TLTuYMcvZClSVC5rqDN3Ztgxtgid6WVV4HuFVlGKs7Fedlw8BvXM3_Q8Uymf3f7rcg8cHS3OEGn5HR1JFVXnjBKISAVcinVWjd5bEcKBgeadD7y-hcnf9MByAGuNRiAV7-3CFkRTF8OElp5f0TvD9MA6M61M7R31smfEEhuRRGAqITMtiCcgIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=BWPXmwgy7W8Le30vzDNUvoo2FzE8grTuZh9YbauChe9uuIndN6pPgp7_kSXT_sqlLMS8UhKUfHGqUk7WWn5z9-nbeFjpLt7cjsSLG3eoG-H8KC-diDeMI_JOzyt9nB7sp3niNbESrKSYEPIOQ2xuoyVl0x69hZbXY5hVpAYNCntzzu3x0SsaDooudDl2d_sFQpKRqo3zze9RET3EvbWQPzpaG-9Tu_KVWF2hTohL6YE4PAqSaK1F93rTynQSNcC21PhYP_J-Ir0GCCdWaroBrb16yBoTJC8z1OCKn4Sr9e5Hkue1QMDzbfn74v2ldi-yOQREMPIJkP2wKEJYtjEPnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=BWPXmwgy7W8Le30vzDNUvoo2FzE8grTuZh9YbauChe9uuIndN6pPgp7_kSXT_sqlLMS8UhKUfHGqUk7WWn5z9-nbeFjpLt7cjsSLG3eoG-H8KC-diDeMI_JOzyt9nB7sp3niNbESrKSYEPIOQ2xuoyVl0x69hZbXY5hVpAYNCntzzu3x0SsaDooudDl2d_sFQpKRqo3zze9RET3EvbWQPzpaG-9Tu_KVWF2hTohL6YE4PAqSaK1F93rTynQSNcC21PhYP_J-Ir0GCCdWaroBrb16yBoTJC8z1OCKn4Sr9e5Hkue1QMDzbfn74v2ldi-yOQREMPIJkP2wKEJYtjEPnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIZoSICA0LBdwA33l7GfxGoTFCp8wn1_5l-Vtnk-p56V3spfNpT6Pt1XVZfmhJYcXqjc3ujCx9spF6ifgl4QdQKLNyKD4hnb5_J4jnuz40e_fkR5lrNI0ia-CnKCOcvEA95pxyzyd8PFleF7RF4g31g7YOpuC2YtekcE8l4S7mrp-d1VKrluGfEJeEcgN32rXMLNeNwosuU8zRFqtGH4-D6_laYCDkYiPo6FqlrFKD7-CznYwoTjLANpsNJ69OEv08j-3-oessZevPm8AhQrOjQS1vp4TleJjqVuq1RMfo2t4KgFGRSWkGK6uoS9K2SZ8a1hlozPcyPPml9LpqWzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtTuUxqJ2dbPx73LqXFmd7Om3Nolg9YfjaPCb-qcSVgZQIDhx5We-ulxw_bvcm6TOh8kINY4KrqVxYzSzm82jygV6zx7Y8-sCQxCNs9icsQelRCR7fGpxuGFm-ygS1woX1mJXYt_vRDyKrsHP64YOWh3jEkIMAzycU2xdTAmfb7IL99ipfkTq0h_WhnhnmwESlzyCklGybGMTEqXDSFvLY82I2QGz3wDcqU1RKFE4FB3lkJQbX271LZexMH8jKw5wIbD4X0b_N8OnNxXwY0M4Pz5TYb0MqGSaVc60IayN4VmWkJY95Zu6nzd07IihQvRHvCN_mTKgdhFLUZLtJsUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=s8QQtOkY-Sjspl1_GF8IfEw1eUct5MIjcoTUjMz8qBoyeuNXho_ADRkF7yOUcW0aWhYYarzvvXoRS5wu_sfoaXWQ5vDE9s6v6paLEZ67XNqMES9sHLxDesfFfiMJzqcfzrUxbe8I6i3HxFkIRXXUCFDmSMRwepYIN4Oe77lzjo9oDV0wf4fon661_U--Q2_Fkd5P3FJb52zNTVvHa9c-jV1PADB65f2K-BDIt1CbHpx7MN5yAawaUYQhysRhY5K8Fg3TdeGXLl-NLqkWPUeXX-n9URyo6egeRpsQao9ecMuPDVtT6wWRQMZnd9jxXZjGFR9vhzBkdBDURvF10-y9-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=s8QQtOkY-Sjspl1_GF8IfEw1eUct5MIjcoTUjMz8qBoyeuNXho_ADRkF7yOUcW0aWhYYarzvvXoRS5wu_sfoaXWQ5vDE9s6v6paLEZ67XNqMES9sHLxDesfFfiMJzqcfzrUxbe8I6i3HxFkIRXXUCFDmSMRwepYIN4Oe77lzjo9oDV0wf4fon661_U--Q2_Fkd5P3FJb52zNTVvHa9c-jV1PADB65f2K-BDIt1CbHpx7MN5yAawaUYQhysRhY5K8Fg3TdeGXLl-NLqkWPUeXX-n9URyo6egeRpsQao9ecMuPDVtT6wWRQMZnd9jxXZjGFR9vhzBkdBDURvF10-y9-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSpu3L_AV_jwIS2xcwEdJOnZak-tgmlkqSp-0ntxh1b_p8RbSynPAQLSBRK9jITn0-l61gM2exBfLIZJfF2-FbT89a8rLSs-oqN2k0_MThPY52bGuyTUQxj1W1xw4Rc78V4zv7TuIu65TNOsnOiXFsh5H9fx97oogE31KrMi7X7haTyg-S1X4YHN1IbfQGBhjWuDDTaD-zeYFrw_PGTR7Zc_Xa-t8R5s1_CXngpgeWgbisuFtIN-I5r22AFMNxO58umjyJRDlb6zlPcGqbSjSxM2vIBcXOnCu6QRq-DXlQre5JhFufH3r9ovCdrDYEgJW5Wau0141Y4ufJ6mW8WNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r9HNcjqjWzTuVEgagrzibOf-XLFU85Ll91guOxsP7ZSO3vdRhBSHPnUg6p8iHHjLuoqufPfyDThTLwnt2zg0_YPUak3BqbrJcSpQQtootrRZjzP03KLeL-Xdx4evkggiRWfjnKRoLWTuLgwq-F6VYeK2JG2fVnGCtHH9F2uThFC7t00BKSuWQzYtyO5JzZovBmNei9zT5P5QeRTDGS8VePTgdz0nAs50z_e4uDEXrP8snChqPV9bUlXSfZzg-GaKMtzMktLVTqwyBF_nIqsuBdrqEyLB6Ypbid640DPiI3JXB_q7GRHJ15aorz9npfLOqWrgRfPIfq0bdUqYPNbGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RfhPY_HCYOLoAafTFxwbzJsLm3MQygMITsnwRjomrTVuhel8cvXRXtcsckPRNlzAJvDdIXTbKIars8SVF9SldJY-JyyHU0rusMKbrcrngzh8vqi-BHSplQQVpfCLObn-RmVSZhsUvrGt5gcycb8D8Ywp4r_BydGlCn91wcUk9GUV0v4yttkHDJT7iM61oy7LBTLOXVBGiyta2V1p83xK_KSuGh9RiQpsJ7TKFmQbsJUBnoc9nyJ0UhgHmpmnd5d9aIBg9E8NU9aJoVNGcpw03uWfUc-iParHLFKU-vVeav--iJOvgcJpVdpxB9pfPtzxo0rvYdWfH2a2VjmBfuau2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uKKKIMNd_BAvWkoOogrKzsN6eYWT9ZiOBUZ3uUSdp9x2j9fC70K2Y319B64zvkrdxfKRN3vdm4y2hHyHQlTiaVFsgqIxuUPIKIcKt7XMOeVK1WDRHCkmzjYGtIl87Oa35lH5j7nFuCOYkOcW4f5WliLqNtbYdFerwqNtv6xwsn_ou2zqq5BguurqzVSg3iDEB6e-dwIOgVJpHQGGJo4ZtH_dHAgpbsIkCCihN0yBO5Qv1rKeqA3KLtVHo-Gn6zhUQXVYk1ri4VpgQJNlNp_g2jPXcCZh9vEfv_AhvoMQXHhBfrioTutvGAjwcCuQobZJtNbCQ9GL2WLSCs5BwPZpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rWT8aBPVtxkjCK4SGiXYTzojtzCrDVBRgjvJEyma25ttWo3aqfIw9CeH-VbWiXUksv3ldWHs3gtDMVgHJqhlfFOX-2NcoKyfoXxZ11YG2PyhB4v0_N16R1-nigVuuG-7TXpIZHK3_xz_lUpBPA1SM8i2BtNcnvHhm98EmsPzTBRuahLMPmAfAeCEgLlQ5CdX4mB1Ctwu7enoUyjNsqhE4yq-jB27G9UkaE3UfQH9n8p5LRj8FfF--gcGhaqBXj4JOvEoOhv8fwfZ9bxV9PPFQmLwfsV7Hd8ryeEhzBmGtN1RX569ZdvjiGAfrSDdw1p88-5kttd7SujGpJEqI1pX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XT9lOUj4_jJggeJc1imyCmA8nJp-1ujj286hE2CXHjXaf6R2Uu-6c8y5LMMrktSudMk7llmmmVmoSAr0wjiQDNO5ajxB_ZVOIy3Ad3ukuedgqnPDTFU2sMUHSWwQHoUO1I2L7eeQbdSpd4_N3vlBvGEip4sKokmJ5LZfXQ7plDExpxh7-Qp3BQOqhFoTpN1TmmgGYDkkDe-aNglv_xSOyuNsnVy78j1duFf9zPToWCPK0DFKvLjnmTaEKs_thbtl5jwi50DlJgzBbqm48LeKN5_TiyhyLagj-3nF2suB4DBkoGlyjfn1CRpBSWIYd-CZ21lHac5qP0S_jW4Y8Jf2iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=eXMsuS5QyEx81wpE6Tr-tnhkGEz73fbxkn5oT_8LylqoSx9Jb7fDnhSK6_4YMuzXN3aXZybc9JOe2hvok3-nybFiL0SFoQWehXx9eExjE_0muLhjzM3Q-e5gt6nX9Ok5ukSD1RPg1RMyKRf93S70kJriZyFFusZvKeNOQBciKQbncHLmtYRQkv_Lp22yusab-ah_P3_yYtGCrLjQh0p9Z40Z5TOLoCKJFQSi9K2nsvSbQJKlaFo84SKc6DHyhzhiYLbBUBgmY8Dj59pCTsVZi6v_Y7dLpdNJo5pARkfALP8270UHaU2tNTDOr2JEE1zS59B-8JsaLLq9zqdlHMCUGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=eXMsuS5QyEx81wpE6Tr-tnhkGEz73fbxkn5oT_8LylqoSx9Jb7fDnhSK6_4YMuzXN3aXZybc9JOe2hvok3-nybFiL0SFoQWehXx9eExjE_0muLhjzM3Q-e5gt6nX9Ok5ukSD1RPg1RMyKRf93S70kJriZyFFusZvKeNOQBciKQbncHLmtYRQkv_Lp22yusab-ah_P3_yYtGCrLjQh0p9Z40Z5TOLoCKJFQSi9K2nsvSbQJKlaFo84SKc6DHyhzhiYLbBUBgmY8Dj59pCTsVZi6v_Y7dLpdNJo5pARkfALP8270UHaU2tNTDOr2JEE1zS59B-8JsaLLq9zqdlHMCUGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=QDEzWTL0-u8toQR-k9MQ_IVk3d5GWcExkUolQOPyepnJguPe5BHfA2Xr7havj5F880siRrbXYL5dQMo9bug1z-LaTOF7cQNAeJcr6au_xTG-qcTlEoHFmL70GfY2LHJ8XfLK8dFqcAc0ZYQt8mwnBId3WOpauxuJaq2DrZZwoU2sOa-4n6_8J4VktDJwB8bdCvBP-Sz8idvarTtbR6I362Q2Io4LSgwpwREiyOWIW_2lFQ4Y5cr-7KIbV05vh8WVjudTL3SSTieaXmT3fzyQU4Hx8Q5f6pRbuOY5P9335FALxIH3vLILld_q7mDBcZFHpGVWIDXmCCalLmY0Hcpo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=QDEzWTL0-u8toQR-k9MQ_IVk3d5GWcExkUolQOPyepnJguPe5BHfA2Xr7havj5F880siRrbXYL5dQMo9bug1z-LaTOF7cQNAeJcr6au_xTG-qcTlEoHFmL70GfY2LHJ8XfLK8dFqcAc0ZYQt8mwnBId3WOpauxuJaq2DrZZwoU2sOa-4n6_8J4VktDJwB8bdCvBP-Sz8idvarTtbR6I362Q2Io4LSgwpwREiyOWIW_2lFQ4Y5cr-7KIbV05vh8WVjudTL3SSTieaXmT3fzyQU4Hx8Q5f6pRbuOY5P9335FALxIH3vLILld_q7mDBcZFHpGVWIDXmCCalLmY0Hcpo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzyZebRm_vpwwtwUhBH8Ep5eOg_xlW8cxns8BDHQHXONaPMENcNkrkIOGvrAyp4RPQZMDGCcgssraKCcuXRFF4nPj4KypiBp8w11GntffpzEGTO5tshcdTLajVhcm2c65Uec7-hCgSMc96lCi1Ufs6lKfcUh6qOkx4QHveFEx6WcybO8q0puV_UGkg5DNk2v_u3fpOmpCAnRY3cANxGqKj6xRqlVVBkVBKKDeo1eDamtKbCd5X0GTlsBLxx99vZsYQfZRUCarKzYjId1tTlklNxJzTKaY2T1D5_4Z0o8YCDkxiGzpTFk426br_P-byoZN09WfoM4blOZMFIDJo89rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6DctAZ5s4_dz8fnJugqA6HO76x6qSx9iKuwpRhMhq1U9QGEq4eMZnyL1w8N6AjGXvapXSYvYC7P01ANdW4DvOkh6CcOvbBCyseBEgOoDFkTvvj-ttdNn285V8DB4fuhfUwdpO8R838RT0RafrHuphAW9DsLFjMp9ug285qkUyYwL5kjKfI8-hpQiLdhQJGvB51ntXqhsR5czLv3kdric1i-CRA4PdP4lmmkZ8xHfYYW4s82ab11VwUFSkpChLWzf6oCr1ZFxsyjrCxKntLpooVkrWDCEh1Jq0iw1XijuDYJAZXMw4yT3NKEJlfbfNtzkJpNORBOJlaOU1grqqfQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxmOv1_BYfZgTUEGm8eSVTQb6l9nwYHimk5XUToMDOWq-UB5k6CWBQWrqW5vh6kRvtifyj3UODf1tM-eXBmTrwDVACoVQFsx6Vcd7l9zJqXk6JIaEf3SZ8Ql6H5GIBrAhu3cEihBXG-gw02iajS9QrU0pcJ4s68HyBvDmB48U7_UwOWGDfpnPiqELADBgrTTghjeEKdXqL5naX3-ty6c_92lWc7DBJfTomTWfhh6DYd-v6SQlifI5qMIeXXdVaMEp0klHjnd56E66_GA1Kx-mMHWh6Iv4bxItmSTeVD6MxNN8cOopDjiugj7kgYZhRTkHpw8TMkuzudoO2TtzHiIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=jF4Nao-1WrFROCDqIcQK1fUVsJDI_AOpe0yKT0haFLTP89C9QKyeYG-U7mwxU-lNGBleK49LsaILDMXNVv1Fw77qpX4Mo7OYz4up59qaDn4lEkfVVdG3cRhHiu8Tfy776hC-fd7mJE5OupuTUh8QdMbmkKYBBHW43EUoS5J0caCqDaha0MFKoU_HFPt0XWTvAjIYSX9JAjNa3L2OZhzI3sNHXircYkWGuISvea8MWbBML3Ysw_Qv9C-JO7A-4zRILgGNhpv25IwxvDHHGy8rncH9kQrjJWleVfdv8v5ZK2tLlDf5k-B3LKNf1en9thJ8H4pusPYeTLlKeRrRxNDRew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=jF4Nao-1WrFROCDqIcQK1fUVsJDI_AOpe0yKT0haFLTP89C9QKyeYG-U7mwxU-lNGBleK49LsaILDMXNVv1Fw77qpX4Mo7OYz4up59qaDn4lEkfVVdG3cRhHiu8Tfy776hC-fd7mJE5OupuTUh8QdMbmkKYBBHW43EUoS5J0caCqDaha0MFKoU_HFPt0XWTvAjIYSX9JAjNa3L2OZhzI3sNHXircYkWGuISvea8MWbBML3Ysw_Qv9C-JO7A-4zRILgGNhpv25IwxvDHHGy8rncH9kQrjJWleVfdv8v5ZK2tLlDf5k-B3LKNf1en9thJ8H4pusPYeTLlKeRrRxNDRew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEEw-HwqFwbfNqZ136E2aDBJ0mGInwhdnBuMPOb4mI_lxfO_uNE-88HmUPowMfzAw9keUDYXH1DshJ5KAQf-mlALqLzDZwSphLvtdm4h1PmDaonwwYM6kdvRTwor9gO0k4pnbnwtUEL8PvAH4wl9iFNzrcHiMHPvO_eT3M7avttJ1AfQMs2u8hAOOffEzA-ifxRCnHkwU-wBaL7I5sS7x287R4iuDXJvwa6eWmLsDEYkkRgbNzLLxxDQ9S-g3dfHq1hNGiv0femnIXZRxes0LR61v6PBYBnArKy5UekWQYzpdu74jau0mocZFVBuvyGEiBRpXdkUxlvmi5CK2Wh3qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=XlRYkqqjR10EnvH-Xn-siJFnQZHpH4D47JblB-F3NaDZH5SYe5fWK-cSuDiInDqvG77_OXl948-etcFY9X2XhwNv2pgRw2AT3jD6VI-0kwi1FYwFAG9lrdbEdn61wD0-DveGyvQy5meChYW-25Stgc2X7MT5LA9fkU4gmDknTtb7q6zHxqizx2DrFlzYkqzs1uGRQUj60Taf3_nt8giXNqmOXCEGf0jYCU1YtwId4rp4C-DLtleKWQDaWW47ZCstIgK4JmQMQIkjiklqaEdg-QoXrg8TYdZRjnm56nHFNqYf0jYU_LWDbKcuaqMPmYtDxiwUrqiizpUeEBAacj7Qdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=XlRYkqqjR10EnvH-Xn-siJFnQZHpH4D47JblB-F3NaDZH5SYe5fWK-cSuDiInDqvG77_OXl948-etcFY9X2XhwNv2pgRw2AT3jD6VI-0kwi1FYwFAG9lrdbEdn61wD0-DveGyvQy5meChYW-25Stgc2X7MT5LA9fkU4gmDknTtb7q6zHxqizx2DrFlzYkqzs1uGRQUj60Taf3_nt8giXNqmOXCEGf0jYCU1YtwId4rp4C-DLtleKWQDaWW47ZCstIgK4JmQMQIkjiklqaEdg-QoXrg8TYdZRjnm56nHFNqYf0jYU_LWDbKcuaqMPmYtDxiwUrqiizpUeEBAacj7Qdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmGh8qTUrt6yvDtld4dyI0Hu1KU3Rn5OXOgPAfogStcJKEnY9g70q1FxYu1sRBrow_2OsuUBFfvbNqFoqhsCPl5itgE58_4rSx308MnJX6Ma08oyxMmm2q580Mbe7ZSxKdoLwLv-_d7VF7ufWlepoKq1c6MFqWfa2NmE06vKhYDK0AySJTXR2t6Pt36NcpltogdZDPeCHQE4xsb3NtmM4xSGUh3cP169mFm-JQC4wn_h5nKN2Wgry-SguWQE_krQCiyDygxfiGJJ4-nAXDVn4YMvUOM6gVfd4MQNZKlI1mfurBFHmOgoxSOtkciZEvadrd2zk_LlOjm2GK2Q3EUB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aAFlv6UetUWU1NvaqzKLM5avAJ4ulyqsXqA9LZQn0aExnQwv86bFpky4NW1Aay1waWzHR5ITBqcQhqKij3yRhgmNphTCmWBrsfkRDeRPFxbmT1ixBeRvajQp8loZx2cRgnILdtHU5CK1MwP8Z8F8EiSOGoyWNIcZpCQBhbRv3MRCB26f3d7nri1ANiIJUqow_GkUlQMmywFEYZqOb5CLegLJztlCI9wQezBrNZe2ocijxO4cVAnVdZz901KO2glo23m7srgDvVmhFiEOV2HrM9C_9_8qRIu925CVXWS2MtxTO6cBfhCHrfqJ9O_B-aoJO6HZjvU3XA4-jbwIKWKPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JevC4VTS60k_7G5Svab41I1QPi80pxbUm6l6rpYTpiEaJh2FkbUFUnVXZ39fuocrB1FXCi7jBiiV_S2Q9FafDeVDCwY-33EhA8gkEb5QIdV05qAdad_dRcYXYqFpr4DNR4goqsPpBEKSNWfQT86TKihDdW8cOgLLBhAVW-4NkWr6Hpz9R8d0epg_pAOmrhgqk8l6c-sxvGlAmjAM263QqwzvJJC-Jdf6ayydK3ozjdd20IlcHgzPnOQOXRpt-mY3xHgsFc7y_MAp0m4Hw53R-QO5dBKaiUcrC-zR5oX5d416A8L710sKLDt-JdyRbD8rMwJXbYyWph5FU99oxNwcug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-_Vz-AF2WisAgtQjO_c03mpGdjMD205xMhF9Av8zh6OuQhEpUXnUGRgVFyd-XCzxPUcVsLLq8-D_qQHiCB73mpthQValH3H5yDjdrDrMrxZh1VwAwz4MRLh8T0aeQsEIVWaXhMeOBxPkL6jieVDIMpLlqrUxkxMqeTztJai9RVeBVhu0gieHilz-wHX9-TSDKuZicXdJs82IfeS2N9QSiWMDMmrbX7yq4Wd9hGWKTjkInaO96imaEGMVX9tOV69my8BsDCBHTmkAyNREILs1E5O6hYr96dLhq3s6EW3FZ_i-5G6bCc_-FDFXccIzTDddcjtLLw5k7UTA6WO3lMa2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sw5p6qmKEVBpiZfk0TzPirS01CHX-QMkBiLqJjO0nnhqK_9dK7CrIzL04odjhbvGl7xXppp2STrb32ZlXoS_PQCgj_IS7JAkeNlAew3Qe0GzR7JhXfMFBY-kzaYtM6YrTP7kjcrpZPtkb3FlxyzYrMvPZ9q0bb_LXAKcU3u_Y-lkQCy1am79iYR4Ummctg9QgInx7sn3e8I2y5qVw_ZbyKpOJQpHIHvG7rJCQx6GC0yv5FwTdjnH19GpbvcAfi7dZheIuyJQp2mBGEbOTlqCKkQaWnKH4GxmX7mgs3MSIoZvnW5yxEvJe0_QXX_t9sjAgjgAczqxVp6WUd4MsqB_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NG3MmkiBz33xKgBpF3nvel4L4ZZoagVlZDjOi8oNoQkFpXtPycIQEFfIu7ZcW0lr8PpnGf3E50kXLdT47TMYeCSQ5WX2DWmNx2VaeFXUpwlihe9wSEWJuCMmauJl1hMqnb1jFcgCKFtOPiBwxqZ5iVisYpq1XnOp84sAZoPW02gt43uPYhu1juIap9Fy-QSomSC2g_f8iqEQniIs_yTphDgvTVM_OAMQvouEApW8NnlamUnNUw6BdXxLlvnqhWZbyDOapHQ9Da-OwDJZWVNyBaB-dLaVVdUro4p0t0SJQDdOZd76znHtqARpBi-k1CWJlW3EVi6BL5eE-8LuY94e4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hne8afAwO1HUrcI6X5eV3M6zJJBTYehZTasE5rNiCOXSQSKoj4HGWFDNoY2xirPMx-8VRXpqUDKLnJg1iSGPtbHd-bJGmetZLRu-TQ4U4asXLSjuVC4gI93K2PrxvMa8sKonAwUeKwaWwbcsdoXT6U4mC73A3_9fQ8IqlYQ8SDHL_4GV8SgkDffG51sqyp2jBxb1BS2KD1dCz_7DB1RsxYcTYvKRqKodA-Dc_smvMwFCtHLEAn5puJXL3UC-2rLk4XSb2I44FatylQnT6Bpp1wMgKoWZRB3n6UWBd0K5wwhHTwHbwmjVp-TufMO0H9bcT6Go_0YnZKkhM01mSgpQ8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vze3eqf7tRWB30TKPT6myDdni35WlQSLo3K3A24K95cb6DmPbYery_vPU2UUmqg0m8GUpDSm4kSdBkv-KIUmRq7Y1ado-i6H2rSgY9HUSLbfM5PO8o4x9uTuQ2YBqYJDF6fHbUQvd72qelnCqgeVAAx9Z1xasVTfF3kOQUoYOAg2n2NZ3X_UbXnJLU5TaeODDzAo2WQZHdxFxoGX7KbCRVkG39q32DWTowA5P9kotIymqH7K5NSFQsHyZoASXwabNwlOJgSvK1RMl-qgTj7SKLjmX9HxY9Kg2XG2_2L_l1hONZB_8_lxdoL2uHbG8x9e0J4qK5MbPvaOzb3GNA5kkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=BKCBSyfaCPtiAVnzBZbZYsLgUdCZC81BVEkRNlft6nPmHu4VW9BRwVOUBH1HpkSKT-T3XS-fJSjB3DvIXPt5FT2nySu_-Vtr40aUehlJfjghoTj67mOrwVHiQRWoa2SMZEP4k7z4vp9dlZXwaK5WbL8DsJFT61w3ByuXIEs7l5bZwYhbC29mxxqdOEDXBHhGN0YZ5Z3fmmWpEodZIKI0DuBYYIf7cWBbYB7eYTEx4tn5Oay2WB9TvF5ZBAnrUyxd3XL98rSTtBUXJ5YqLR2IixKs8ViTOewyp-KlkK4q3-1ySnmFDcKk-3NChSDCdMKIyNJyMEQzFn9I0FhFzeT2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=BKCBSyfaCPtiAVnzBZbZYsLgUdCZC81BVEkRNlft6nPmHu4VW9BRwVOUBH1HpkSKT-T3XS-fJSjB3DvIXPt5FT2nySu_-Vtr40aUehlJfjghoTj67mOrwVHiQRWoa2SMZEP4k7z4vp9dlZXwaK5WbL8DsJFT61w3ByuXIEs7l5bZwYhbC29mxxqdOEDXBHhGN0YZ5Z3fmmWpEodZIKI0DuBYYIf7cWBbYB7eYTEx4tn5Oay2WB9TvF5ZBAnrUyxd3XL98rSTtBUXJ5YqLR2IixKs8ViTOewyp-KlkK4q3-1ySnmFDcKk-3NChSDCdMKIyNJyMEQzFn9I0FhFzeT2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=Dtb-qjcwQy3KYgJOEsxa5Ffwk9SeIiDPLN8RrVPnQJOFLZ_OSyHF2bYi2zyVebuOOB8tG5y9FO2q1jCZyoIYjgKaWRXGieR3pZovk6ehQ_TL67Fde1wTgM8y_d0bXxOxtiHSbZcXFtmNpcg0hwjuYU2GuTIAxXRi8yQlUZvEzvqO7Pu1qIpRjOz5Z6Eu7O4erVXR5fZ0yIl9oBVN_f7IcV_qWJXWo13oi1cXGE_CzbVeGv7lPNHbKoHE9UKKZbKgWDvjYrbMmetWgqAiOFX__t8uVpuRW2nK2gYOwGAaQ3OsRBopZpkK8jSpKs1xmxGPpd12C8WasBQ0TtDtHoTuTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=Dtb-qjcwQy3KYgJOEsxa5Ffwk9SeIiDPLN8RrVPnQJOFLZ_OSyHF2bYi2zyVebuOOB8tG5y9FO2q1jCZyoIYjgKaWRXGieR3pZovk6ehQ_TL67Fde1wTgM8y_d0bXxOxtiHSbZcXFtmNpcg0hwjuYU2GuTIAxXRi8yQlUZvEzvqO7Pu1qIpRjOz5Z6Eu7O4erVXR5fZ0yIl9oBVN_f7IcV_qWJXWo13oi1cXGE_CzbVeGv7lPNHbKoHE9UKKZbKgWDvjYrbMmetWgqAiOFX__t8uVpuRW2nK2gYOwGAaQ3OsRBopZpkK8jSpKs1xmxGPpd12C8WasBQ0TtDtHoTuTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxVSzGdd3aTm3WfP9Kpt-WOVK63jB0qJs0AOjnvNK_IlR8rk4ZdAltjkCXBN-ymLhK-zCvmkkxnYV6aM-Ak0k0i_cZmtNS5TRLvK8Eji_SIyDdLw0wH82fKcCYF8da-yM0CZSFHUub0igkrQ8ZXJLusRfQ9SnxYDY2_Kt9YBCIYESb0bYLjss1bZTtCYteHZTJ5oiUbRcnRuslUtU9mYCyR_l8ofCjkXlA5h_oaizENWV21KSVOxPUXEAZdiSB9EI6vm-MUs1W7LLNHNM3WzbgQQTUx97GXuCTddLkf6pWxeGkju7Y6e_QdsOWWMz2q16JDpWcl08Tp86iRU8r1Ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I_Lgz4zQm473_aklRQhquVAN6iR3rY7aEUNMbrdnuC5EwmgAAfD8ttHvDGD8LbvjEdzJzqGnTW05hZ1DoKf2WM4XjNblqIe-MPapOeFQdy9YoATPQUy1PHLYbmFZCFA1BO9GprI0anMERrP-SBp2V71w_UfACTDeUpnz8eG8tjWDg3nyIiSBrMMIrmGoQ0c4GSfYy4-wAba_ivD5MocCVXNSDmwe2lT0xylV134kjvmnn7FrT811Q36cm9z4S7RzNbrPY_QMGqD7OSOJFXwqiH0u-0MM7lMVuzNUCJlgnGv9IWFeftTCpNhdhPL1GzBfqbIn4XC_AMwOs1-2j89njQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8m-sT4T2fm8yXpmT3nuXyI0vToKCTAj2j0wnv9ZcsNXV5uSK2b9pOzVv_fDW-GzELiKj2xYHGcfTN0pzhxuhZsdENizikiYCKT5JxNfwREA--gECjht4pNWKqg-vAziuSoKOvCOpowGNFHXIZ4op9PnRE5nLSdCNYznobRcyvW75ANnqdLjzsX5rBbBZW457XXWRvxQPjl79PhRcFQArN3SIJ3-0V_8f4nF45Z6kagtgcf9goZ2Ft8Rc5Mhzm4w7Hdpfc5GlpDSJvoqo56P7vdzS3yqxulGioKetaptYdFy86LLzo8w9bvgxpFAd77HeneAgW76JiGOXxvjv1BqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=YmL-0B_28UaMF6EMpO1fCqEaYGOuiWbrngmS19VvxIuKZtd6Jm40wB6nFRrk7SHVasShsCNBTovKCrNwzsX-hHhS8FcCaDVn1PU1Op9W92ajo-UxKrhnkrm-zcIJTbGrOergHadxGvSyivYy8xOaTwUZLRWh6drrlF2u7-_17QU3gQjrpwpUiten2x1BSvSi8JRrBZZqug1_zbw1D3Cfjr2YYKoKNiH6Bgi3yfGqqnBQmJ_z4_X1L0gPZeDsq_7DqsFzCDGdjSKxbEuJoXqwZbN1OSzccS_blhmY0gQA5SEJ4aIw0TrIv71vW5N4IOiNd5QpxsDVZ2UkGFoJK7CpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=YmL-0B_28UaMF6EMpO1fCqEaYGOuiWbrngmS19VvxIuKZtd6Jm40wB6nFRrk7SHVasShsCNBTovKCrNwzsX-hHhS8FcCaDVn1PU1Op9W92ajo-UxKrhnkrm-zcIJTbGrOergHadxGvSyivYy8xOaTwUZLRWh6drrlF2u7-_17QU3gQjrpwpUiten2x1BSvSi8JRrBZZqug1_zbw1D3Cfjr2YYKoKNiH6Bgi3yfGqqnBQmJ_z4_X1L0gPZeDsq_7DqsFzCDGdjSKxbEuJoXqwZbN1OSzccS_blhmY0gQA5SEJ4aIw0TrIv71vW5N4IOiNd5QpxsDVZ2UkGFoJK7CpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNhjfjAoD5RGIjE92HmruU65xiJ7djxzwECwgQ6rEaGFjutWcYlvXaB2tLNHid7nWvw3zogdhjFr4REXMfHZz_c2OLY5ljCY7mln8uZnP3vo_J3B0YdUapvctQPKjveaeoQ6zE2ObFkKX8iN1-19DF39E9OAVQda-INhwPddIggQcZ-Iy28VyQMh18ynZC4hUqwtuVW_xKXIsOFVOC6blrItO7d0_68alWxqJ8HmGals3Y9sWWana6_r6wds-nKCHkwzNmQV3nISyiCvqaR947JWeAGdTx4xg12oKSVOpE1CgtDY4RfawnmVrfGKj068VNowSgxOFHn1Wb4O5Dzx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0OvQcMVz5ex0UmrRJsZqMxrVkgFC88HJApRUsQ4JaHmZi3yoPDvxM67AnOlZYo9nXEkaQxgHHHFiZ9Cban2IzX-reubowIUzdoArRRDw_6BiGcZCd_JxtcyazaD8U5FZAlQPBl-N3PjXY5Zr5D7IDbxHSvubXB9D8WICxtS289mpJ5VWrHCiPvj3tyq-36gDJ5xGIZ6eUYepTZsjjxlgGKGk0j03VDZzfKIT6l17fDFIqqIdjaknOLnfgniNo76TSuB6ANz6i-KjoVz50jmmiwGXqyUQpTgBCppI4ERitnDf_B4uCb7JjjFrV3xe48t6xnKA_xQ_TTaNn2Vrhbm0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_LIczzxlVFZYrRnDGYWVlIPOS5daBW5-kuH30CwKxIY4H5MFtcPO14AwWdPOqwIPvZ8EURLo2XdVBhsurMF7Jl0rQJw_5m0NIW3b1z4sfFodjMXUhuskK48rtLfJ6zdfro0LQrpstC9fEEBdxf7qTIYupTWuzUluKWeo9zoAC9tnbjI1iL-p5VSvmIxXwsZqLvTwXkmxeBVmGgJWJnrCEj5g70kEFNw9ZmxZsdZAu74cG2tlCcLYRl8v3oTBgpf5ZQs8dyEq0HTqYEKOoNw7eQkyyF6ccqvaaY45qr8JZl8VEttV0ZED7neg_5MYGw9l854shGIx_eCQV0BuuYb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=EnDRHxBAdnjp3B-YR1j3W-uSayY7CeNXEL1d7Ft19tMzoZYS4FwBiNEs63eWZWsovFd4gAQdshREY1Mp0U9aNXmmNw_x_SfXuNaH4G9coGTKgEbxBXR0aa4t8yYARrc9Y3-AU-5jzpdgRDcegvnj54GJI5jEav4kqOhWd1QHywHXEkBk8___hAOuqR_yTVK1ETRb-GIfiZQaZkVsVwoB-qjSfOtiCHewqYCTgnNrdhOydnaWUoNV4TTwDFRU_zBTkZ1imaforqnxwTvijApQwr2MQr35u4d-I3gW2Sbed8rzxrz1ey6yWvMc36In88VT4jLVVoO3CbA2JSGUmcCj7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=EnDRHxBAdnjp3B-YR1j3W-uSayY7CeNXEL1d7Ft19tMzoZYS4FwBiNEs63eWZWsovFd4gAQdshREY1Mp0U9aNXmmNw_x_SfXuNaH4G9coGTKgEbxBXR0aa4t8yYARrc9Y3-AU-5jzpdgRDcegvnj54GJI5jEav4kqOhWd1QHywHXEkBk8___hAOuqR_yTVK1ETRb-GIfiZQaZkVsVwoB-qjSfOtiCHewqYCTgnNrdhOydnaWUoNV4TTwDFRU_zBTkZ1imaforqnxwTvijApQwr2MQr35u4d-I3gW2Sbed8rzxrz1ey6yWvMc36In88VT4jLVVoO3CbA2JSGUmcCj7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی در شبکه اجتماعی ایکس نوشت
:
امشب بزرگ‌ترین پایگاه ایران در خارج از ایران، یعنی تونل‌های علی‌الطاهر در لبنان را نابود کردیم. در حال تکمیل مأموریت هستیم. سال نو مبارک!
پیش‌تر ارتش اسرائیل اعلام کرد شبکه تونلی حزب‌الله در ارتفاعات علی‌الطاهر را با استفاده از بیش از هزار و ۱۰۰ تن مواد منفجره تخریب کرده است.
به گفته ارتش، در این تونل‌ها که طول آن‌ها بیش از دو کیلومتر اعلام شده، ده‌ها موشک، راکت، پهپاد، سلاح‌های سبک، موشک‌های ضدزره، صدها مین و مقادیر زیادی مواد منفجره کشف شده است.
بر اساس اعلام ارتش اسرائیل، با انهدام این سایت، عملیات تخریب شبکه‌ای متشکل از هشت تونل به طول مجموع ۵٫۴ کیلومتر در منطقه علی‌الطاهر و قلعه شقیف تکمیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VeMVHpvd7ZQgO3awS3lb5YBH-18nnoXwfUs4Buo3HuQ0mGxwZWZkCMLoa5nx80pVl2ciGfWVJKvr5UZ7Epz2j9VmF9FMz8BN6vRtkk9tzMdnwUMjuCuX0Gcaurx2DiKOXGfj9NZBozlddAhmilqjz0h5ifs1LnGVKVOd9W50edmUpmIxO4VariTJFuKQmqs5rb4_mZYwBUolQ_prhLWLx-EajEVeG_SlshMaXYmXY_TJd3D4NZp9Yf_cvXKgJU0nBZji3Az0ut4ypI9pH1cgcL65gFYY8WEuY-g8ysRPXRJK0k9cBuS6NFcUpRT85Libb7h5-fjYJzZ19qpoRo21Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=udYR1gBw4kpzxkubq9KGjuTQ-1XUUM_BHF5qLCeXYUaZJg22fnOdPwPsQZFG_aJp_BehK5oEMXhEec9HDnsDI-gfuurBnajmyof7XvGONECdRo_lgk43V-3vmluCpqiwlxnCO2lKI2SAAklMpvSTYkn_jbBcwd8y96SVzDu45tnFgOBnbxPyPviUBjQIsNr9gm2ip0hiE7-VuhdYvh_8ILbKMQ6vmNv4xQXL-VBJpn86FiwAM-DU_NKq1Jj7JpqgmEFksx7GK99G01A4IxJFbHxyPX-HTk1e3GUXoad5hIbdj8uQXZMJT9mxGmBN36oCjzdWP0TKoFntL3Zh7ZR1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=udYR1gBw4kpzxkubq9KGjuTQ-1XUUM_BHF5qLCeXYUaZJg22fnOdPwPsQZFG_aJp_BehK5oEMXhEec9HDnsDI-gfuurBnajmyof7XvGONECdRo_lgk43V-3vmluCpqiwlxnCO2lKI2SAAklMpvSTYkn_jbBcwd8y96SVzDu45tnFgOBnbxPyPviUBjQIsNr9gm2ip0hiE7-VuhdYvh_8ILbKMQ6vmNv4xQXL-VBJpn86FiwAM-DU_NKq1Jj7JpqgmEFksx7GK99G01A4IxJFbHxyPX-HTk1e3GUXoad5hIbdj8uQXZMJT9mxGmBN36oCjzdWP0TKoFntL3Zh7ZR1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XpaOtsMcLPNDZD2YilJS8fB0ZqJCEeRAUDtwU4Ga9naMvMbVibrTmLBQsXKUUamXPhNMGVVOJ1gEQEyRmJWDg1-7Ma0SmHnoqm_qu873BqvKgnsS3gQqzVLsSA9vdhx8w22JyfjrRNMIxeplfBcEi1nXwv-5YwJwNqRA62yvkBj5LIbjBOnGBq4z1Y_J6sChkCq4h4lXnRqkFgAA_Yo2bPgugLgV8vS81n-YQRzEJ0Nvg02ZjnxnLpdQZSxMx4EAcLaIBhJFa5sD-Lks6s9vj8rzK07TVuBl2nGO_ce-LcdTa4PAezJUdUnNS1ZLLN9SNTNdmbDOx4LARmOGnlMsKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEfsvgPNx5SBGNhzue2KXOI6doDTDxPyLjopUi5GNoXma2G2hyfWQvC1TDVbGtMvZVcI2D7BjYWWz_5Xhyib5_HVuf2NMsfeJwF2XcEWp0vZoZYQnSqImiYYzQbouJEH1uR0KYoJQAAFFpbAP5czImlgYG3aGb2aulhyW1flVOwWSHz3PfjDyXwNNwPpePRkDlQegdphy8GmJzj-NMjiiYvPbjMCNq4eUaSiTcacY2h4-ewBs4Amsa6wkYVu1R86DSUdy62ZeHmPYWkyAmBugDV0cIC7Jz3EHFkdd8GP11usrqvPcbIMNoxgi2dc7-zIBUu8Bx8JdsjwGtOxusdaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmNoVVsZZR-7ORXBcEQCNHzHxRf8UW6yukm9TOzU6z0iyjyAUnFS9aH9X2i551hYihDEiFTMyLXgbSXUY9JKpQH11CRAX54LInUFTejDRp1p9LJpFXoV8tdLmUF1OLK87z1LlB1PZ1UifB2a0ZnBGafRqdJT-hHoesoeE8RTHi6-0zs7apaouxT7r8DWBj_LydwxztnFA_xQ6hUHZGXpToZ8dTzrHhgEoYNaZNV1Tw37FjyRXOB42_3pq3giUJgcVOwEzo-VcEYF_S8xdDHcQU1hPMwwNPsr7HhbxP4AdugEw-K1Top0KVNzrzHGTR-FjKSFXQJo6yR1HwVoyKe28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fNeFVGiM_Mh2AXi4oxhcegQXQNH2Vo96bjps7ZSO4r8IYV-eEusqrR96kYwHYCNJgl7Csfdzv-9mWm1bGXWYCflALv9IkCq4oKALRsnBFU2YzOOIgUy4B7_EImvjbYfBGqTv5KqBk-P2fuJS1SRFG1a9gAq63XRqa956mweWCz9xSFaiol5jsVOfUnqbV-R1XolmL2snAtwT_RP7tU3wzUmzsI2PoA_vo3bQkYegRPlR_8RF1jwqsO1SvQoWkjo3XkGhuV5QPLmn1EaQG5iesp6J6kVKvHdHIdYoBE3nDrysKJEzYmMu4GfyMrKyDRcHmAmRC_pW1mvragDKN7aQlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HeDFXtbEFn93BNczPD3TK9WFLZ9oPnJ64AaeuND2S52HXt9gbj_Jdbahrl1EbjgeYmHChryEhKymFhIOf2eI_06BGmOJbxiPqO_vpW-q836PCJRzGF5iJvNKLTW2yZ5lsSqE2FhZpOQGqp-ff4vbeW0bnoZhzTHcuiLHVKTERcRzZiBsZUuYhaynriuGc18NQ-Zu-GS2r0Jb-89phskQTePANC6GM4uI15g3hxGRA8OYP-XH2xb99GY_qcv5Dy1iIjXWljvVZE5sraLZiHh0vileL8Fb2FsX7MBIfTYMvAB1dUZRwVbStT8ig4xYC__REw9Vuh9JyXxlzV46pFfTtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکانتش در توییتر:
MaryamAzimih
مریم عظیمی، مهندس ایرانی اپل، که پیش‌تر از بازداشت و انتقال خود با چشم‌بند در خودروی نیروهای اطلاعاتی جمهوری اسلامی در مشهد و تصور مرگ قریب‌الوقوع نوشته بود، در مراسم جهانی رونمایی اپل، یکی از فناوری‌های جدید دوربین آیفون ۱۸ پرو و پرومکس را معرفی کرد.
عظیمی در ویدیوی از پیش ضبط‌شده اپل به‌عنوان مهندس کیفیت تصویر معرفی شد.
او در بخش مربوط به دوربین آیفون ۱۸ پرو، قابلیتی به نام «تصویر مرجع اپل» را ارائه کرد.
اپل دوربین این مدل را پیشرفته‌ترین دوربین خود تا امروز توصیف کرده است.
حضور عظیمی از دو جهت در میان ایرانیان مورد توجه قرار گرفت: نقش او در توسعه فناوری تصویربرداری در یکی از بزرگ‌ترین شرکت‌های جهان و مخالفت علنی‌اش با جمهوری اسلامی، از جمله روایت شخصی او از دوران بازداشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QfZniCjJrEZmNcykQFkqyJMhaN3XNGqrHaHiuC_bSbB21LFft9oL1traQ1MBWzN4LOfJooqwbQBoeJL09734cKYYP-nACx1NAE72w_xtwj34dmG2NRYY-49SPB-L79QLPi1yMMIYwuqYq01UvUNCC-AvtKpI4pWSP1NghpzxskqOThB1cjpm5oUe4cA6H2M75nQccDFbWU9WT8LUzQR80L6uPWD4TJUI3Jq4J5raVyny1j-gdTOf4c1Z6mYxpMZp7-6LCj0rT1IzKG68tu1ymQEiDfMtSpMqXh-v112VvffeGihACTynu3ZCXTy_HqZz4GJj0FJSrAhXwV0G_3SKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uIsPFYGL03BJeE6NTrrO-mPjitTC5e3NIhC_a6LDmgDJqNl-JhyN3rTPxzbFcxd9E9YgDimfhiwDbgcOk4cyncv_Ehxg_iSzMqmn7zfx3sVTC2lak77TSCPKCYeCbu7BC8ebcPzwy0aQKru3-DUXi6koA8y6AL9xqugPf9X7TeKX2JyKxcDLofAg56uh4uxW9QUeA6uyDzeteFMM1R_bnNUeYGcYZMFOpCQuER-BvX5JPwx8cJiJFQaW-tlAZnZCF0AuKYtwY1B3xdQIvLACNj2A1AidglKdRyZKhqkdM-d0Gr0w0g0Et46XYDXdUOW9gdsDXNHrfzkJisr0AIcouA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KdgvSKdLVpuFXc4AZCAv4btYdlbvL8XFA6kNXRpsyHLJvQdD1Y_ADD2y4TsCX1twnnvCr3qnVv2W9pnvukFRgn_0Ndf_mfuo_OkvVFi8xz2ly_acP8r20KNSdKd4Ys5DLTUr9WCE2IDw0FUcJwRPjHmSkBwRCRBnXMbIdp-5kaG3PtRGOo6N8C1Ts6UDvEz5FHU6Ki-jpRlJhZShX5iLYaV-q4H8CNHt5HRMBW72u4DpIUhtAJAsSpVtkNm-Jn_1fuJ0t5_QS32SxLHZ2DqPOsfs1wP8Id2aG1S6sa3uTW5Lzf5v0VAzrxWN5x9209N_WwgRaF0MW1ZPLwa8rhXsxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoT_wzbezHANHcpw40HNLu-rhnI1jZoXRPVPvtRX9mWSsTUtkKlgi1RTQV7y5btgDTPTHrz5u3c-8vgr1A5j98Jp5IcNxR9qLZ_tHOI-0k2ELIJviEy5IdOgZAqNiC-bifvk8Acd2VuOQDNe_RMiijFVEaJ-F_CQXQS85qvabPzNF2b3CoKYeNT8a050e_Sg_NV_I3h6MTgE9mAyu8E9ELH3mRMqgaYKDY4jcWYXap6Tu39CEKCd-1_ry1FTeLF6HpUS3uhcYvFC6FwmRb73QYslMHXDWKthnAq49bVhuKKDJLnsPDH7WW2x1ALa3ECjCzBkR8t1S8BAbcIxf0CclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNsDlZWvf4HT_uVp1A6cce12T_XTp_H5TrTaoBFMwPM1lJcKGtPtr8uT3tYd9sQ0FA8rPaLHk8Xpqqo9D3U1DZUrnlf5XltA6hO754lKR4mHbGUbihoajHdpuCPE_HX7UxElMHbrCiGSvgEF95StNhGrsFyNdWRBMByWI0KXo-o0IO9beXhfXLlk4DE1YzAaQ0XcaQ4_VeDzNtpefShdFEijTdxymcSdoxPUoxC175zN5ZcFJk14pCXdyK7U7UiPsKWCQGpY46VzpKiz_mRYysHyjknxTDBqffPN3WfTS0auFtbhF5epbxeuFFYmnCvzov52OlRxl9fpNPQWL1eS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=ne69BHH4_K3t67yo6UCfLYFtTflVWw1CDDv32lY_tM4-Ls3UnX9B0WuixjcFcUmx0u9hQmQFG54wdKXf3VH6qKlEiCwH3jMBRZ_7L8fp2i0YPHrhFsXIQ3D43uQ9kygjy1rZfx7LOp-S14CZOovcjY15ig_dkPFSAZrRcIoqj2ZPMoC8UTfHQMWxJjeuF-FQQC7865ArQMV16f3qpBKwTE00bZs2LhyUbjx1uw4ra2GJ4pn0uZqTgfFmauZXae4Tg28-KPYFONhvShJDch3k-5Zm8nRg_V4UdPDf9zNnLsMCVfsMwB6idRm5ynDrXpVycQQqXxkCKt8XZRq0qtW5Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=ne69BHH4_K3t67yo6UCfLYFtTflVWw1CDDv32lY_tM4-Ls3UnX9B0WuixjcFcUmx0u9hQmQFG54wdKXf3VH6qKlEiCwH3jMBRZ_7L8fp2i0YPHrhFsXIQ3D43uQ9kygjy1rZfx7LOp-S14CZOovcjY15ig_dkPFSAZrRcIoqj2ZPMoC8UTfHQMWxJjeuF-FQQC7865ArQMV16f3qpBKwTE00bZs2LhyUbjx1uw4ra2GJ4pn0uZqTgfFmauZXae4Tg28-KPYFONhvShJDch3k-5Zm8nRg_V4UdPDf9zNnLsMCVfsMwB6idRm5ynDrXpVycQQqXxkCKt8XZRq0qtW5Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب «کاروانسرای روس‌ها» در سبزوار:
quotes
خانه واجد ارزش تاریخی «تومانیان» معروف به «پادگان روس‌ها» در سبزوار روز چهارشنبه در روز روشن با لودر تخریب شد و اعتراض گسترده فعالان میراث فرهنگی را به همراه داشت.
تصاویر منتشر شده در شبکه‌های اجتماعی نشان می‌دهد که یک دستگاه لودر روز چهارشنبه ۱۸ شهریور بخشی از یک بنای تاریخی معروف به «پادگان روس‌ها» در سبزوار را تخریب کرده است.
«پادگان روس‌ها» یا خانه «تومانیان» در سبزوار با وجود آنکه در فهرست آثار ملی ثبت نشده بود اما از سوی میراث فرهنگی به عنوان یک بنای واجد ارزش تاریخی اعلام شده بود.
معماری این بنا متعلق به دوره پهلوی اول بوده و در زمان اشغال ایران توسط روس‌ها، ارتش روسیه مدتی در این بنا مستقر شده و به همین دلیل به «پادگان روس‌ها» مشهور شده است.
مجتبی کاویان، مدیرکل میراث فرهنگی و مدیر پایگاه بافت تاریخی سبزوار در گفت‌وگو با صدای میراث گفت: این اثر بدون هماهنگی و بدون مجوز میراث فرهنگی تخریب شده و اعلام جرم علیه تخریب کنندگان این اثر واجد ارزش تاریخی قطعی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MeSK5TTEOzlJ2KiSkk_XTgUrO8Y4IXfJ2T1uBBuPkx9qUkbvP3PneZ_kerZGQk0-cJsyqe5akfl4IR2dtgQBLwFZUET5A8mugunspEWTuR7isVhrJfCmua9C03TCKRpMgt9HClNZ9Dck__Ix47ps7QFGOLDQ4K5VWycleqxXy20MQY-DLIqxADKRiQY-PXpB5fQkm-fovdQH7HBdYxNKo9x5fgGWY5diXk1bwOg5dKJNAUZ1TwJQDzqeiIHv-hV_re_vqQvwpWClcMkSrPAOAFiWVzeuKoq3kcTFerOaPsZmX9kHo4dTW-YWaUGdIoO5-WAfe_X_Ey_K95gTS1J_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/siTLh2dCYD8Zom9H43mtrAIzTEGHFlKp8yOxAB96qC5STeMjJo6kf4YlT6NZmf3N2nRBVv0XLVx8B3aovNxuB_QP2qvPozj9G1ruSoz3kgn8JZl0Wn-UTQ2Flg9NRCv-gF3Ctt-WWWX5lV3ibxPpsqp3oU59hcUPUYvXQ2D6YRAAkhZCzBFnZXJTYC8Ni1hngaRBjJbbTjfwLr-7Tt_ueWMbixoJ5SByYviOi8Jc0fIwF2eUqhzhTFDLuutoMdQ-dZ3H5pinj9IHbLPd1V_sLntbjcluHrgrfMNU4uPbZjPsQNBGIB2QMiZj9-cInptqqj6simxtaVQTpbMGBUpRUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ از مشاهده «تحرکاتی» در کوه کلنگ‌گزلا خبر داد و به جمهوری اسلامی ایران هشدار داد: «توصیه می‌کنم ایران زرنگ‌بازی درنیاورد، زیرا مجبور خواهیم شد بسیار سخت به آن حمله کنیم.»
ترامپ در ادامه از حاضران پرسید آیا ایران باید سلاح هسته‌ای داشته باشد و پس از پاسخ منفی جمعیت گفت دولت‌های پیشین دهه‌ها تلاش کرده‌اند جمهوری اسلامی را از دستیابی به سلاح هسته‌ای منصرف کنند، اما به گفته او، مقام‌های جمهوری اسلامی ایران «زبان گفتگو را نمی‌فهمند.آن‌ها فقط یک چیز را می‌فهمند و اکنون به مقدار زیادی از همان نصیبشان می‌شود».
@
VahidOOnLine
رییس‌جمهوری آمریکا، در گردهمایی جمهوری‌خواهان در دالاس گفت جنگ با جمهوری اسلامی مدت کوتاهی پس از انتخابات میان‌دوره‌ای سوم نوامبر پایان خواهد یافت و تهران خواهان توافق با دموکرات‌ها است.
ترامپ برجام را «یکی از بدترین توافق‌ها» خواند و گفت جمهوری اسلامی در مسیر دستیابی به سلاح هسته‌ای قرار داشت.
او افزود: «اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای بی-۲ آنها را هدف قرار نداده بودیم، اکنون سلاح هسته‌ای داشتند.»
ترامپ گفت در آن صورت مجبور بود با رهبر جمهوری اسلامی تماس بگیرد و بگوید: «جناب رهبر، حالتان چطور است قربان؟ کاری هست که بتوانیم برایتان انجام دهیم؟»
ترامپ در ادامه تاکید کرد: «ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. موضوع بسیار ساده است. نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=DFSQHV7wCm7uxXFLepzcLvj2bIiCulOgMOJZGKWojkituhAM4Fv_yOnx1qixMWKsCdd_UGFlG0JRcuS89AR6g2veAIeLlsvDHposO6vFaGtYQINKftthEbWJjW9z1AYB-wBiw2EHteU_4u0ag6mldJUOFW5ideehC0cU3rOtcnloxmDpYayyv-oe3iD5So-SuPexd7aynY0jVhzDJbriFEBJYm_4TRoDnSQRqvPih8KApYDniZ-DHA_E-izQ0aTStpk8j7dhQeC4w38Olt--EYrDgBD8w8hs9LX2ySP_ioiLdhQF3WjVNYVsW1RAJHUZh6bI05JugCt9cYdFQcp1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=DFSQHV7wCm7uxXFLepzcLvj2bIiCulOgMOJZGKWojkituhAM4Fv_yOnx1qixMWKsCdd_UGFlG0JRcuS89AR6g2veAIeLlsvDHposO6vFaGtYQINKftthEbWJjW9z1AYB-wBiw2EHteU_4u0ag6mldJUOFW5ideehC0cU3rOtcnloxmDpYayyv-oe3iD5So-SuPexd7aynY0jVhzDJbriFEBJYm_4TRoDnSQRqvPih8KApYDniZ-DHA_E-izQ0aTStpk8j7dhQeC4w38Olt--EYrDgBD8w8hs9LX2ySP_ioiLdhQF3WjVNYVsW1RAJHUZh6bI05JugCt9cYdFQcp1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=LzkQSYxZRixOxKBY9d4eujPiTUJqPEVO9U3ObimpLx0G9VIvewH0Vc0Q4Tk9XfSxxit9RuKcVa0jF4DW1IEo4Bit9ftkXlfHNKlDWtKjHb5lCTXTHCcud8A72cyqK7ogCSxmAAckdAOcwwpF7F5TFoRn69psuPjZMThB8eH2tw7iRW6OE-sF426k1Bc3Xbl-RUME6UdAHYxgBKTAxv5XvvGBaTQf4KhnRCB0kvUYCv5GmvabuFp8nGyKEEcwVdNi_68rtO5EzRW_45QRTVx4jwAje-EpzjQbqAxOVEPrttBQvP-Je44_mpzzKuiVw_Q1NgTfwAZmMibuL-hFMP9VRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=LzkQSYxZRixOxKBY9d4eujPiTUJqPEVO9U3ObimpLx0G9VIvewH0Vc0Q4Tk9XfSxxit9RuKcVa0jF4DW1IEo4Bit9ftkXlfHNKlDWtKjHb5lCTXTHCcud8A72cyqK7ogCSxmAAckdAOcwwpF7F5TFoRn69psuPjZMThB8eH2tw7iRW6OE-sF426k1Bc3Xbl-RUME6UdAHYxgBKTAxv5XvvGBaTQf4KhnRCB0kvUYCv5GmvabuFp8nGyKEEcwVdNi_68rtO5EzRW_45QRTVx4jwAje-EpzjQbqAxOVEPrttBQvP-Je44_mpzzKuiVw_Q1NgTfwAZmMibuL-hFMP9VRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BIMAtxHTwvSAxnFZftMLKMRt6Gdc-815i2wdlCRQMqvoYjpIQe09WuOCyXk89LYkSWTY-UlaZFssguVlaJG5e3iuzpVCn_rixm1SwYljPNH62ViFl-E3WlbEQ6j1fm1bFQo2HXZT_dAbU6q3zcWGmXu1xLQWCWLm5xsBELPkbPgimEC7tgZVPbYIS66R2CCG6e7m4Es210jCQhLuJ5as-PQQG1P8LWGvWCn8WMUFQN6O3YxAPn6eCuv4i4_JzcfDPF9eyY1LipajgTyJUYLUdE81qtrkwy_6uKfqTLy778LMSgyyw62yNCT6TZSI4UjWIsQhzt3ukAyv15GwlmVecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S6cun5Xey36wk15fe2Qx4Yufl3CsDybb8bQ4rfl8sMnbVhplmaP2p_1CLAK7Uv3ptvcUtj9_SSJKDo_SX0vi2_0X_H3vCxQhIQRFupFzWClI6WtKDUnI1sqtomWVGOc0mNgHCj36vhyk6Wquy-r8iSZOnF61vmXg850gvdJCxPxyQkQuTUQI64-ObXdmOjvtl9Y_U3Kj3dsK5poFZwOhtxDldQO9_5wd-verO3xP7d-LJflK--Cz354f3wFSwQJWev1Z2_ycuVdgFAoV-qG66QyePqUl4eXm94GZd_4eaKjKm2b_QS2Wd5jClm6YJjUrlH5R5-JY50y6ujQwnuqdjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=e8S0FwPY1U_LbzbWHGqxHoAuNoUSqa8OQoLpHiuIGTclz3LIyq4ziFw8EWlSRwIzw2BMHOCZDVz7__eCE9GHzl438kXeWhL3xPVNXPHJF-YUvm_VpRQ4SY3IyrpIvXBSXwd3rKSZOcYD5jaEMMD8_h6EeGpEjJiRnHYFefLAZhxRGr8jRTkXdbNo9X-d3z9Jz1UVv57WqoveLRbIFXr0EEU6sEAUFv9tRhQnU184-I6gQbEsWYctPAkZD95SZzqTS47zoGnKu94YQTBtZhCE8Ows4jtVBObb3KYnwVC5tBopQANPJrck64TNq2w1q2Vq3-cnnnfDTaFyK_D2OnmaPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=e8S0FwPY1U_LbzbWHGqxHoAuNoUSqa8OQoLpHiuIGTclz3LIyq4ziFw8EWlSRwIzw2BMHOCZDVz7__eCE9GHzl438kXeWhL3xPVNXPHJF-YUvm_VpRQ4SY3IyrpIvXBSXwd3rKSZOcYD5jaEMMD8_h6EeGpEjJiRnHYFefLAZhxRGr8jRTkXdbNo9X-d3z9Jz1UVv57WqoveLRbIFXr0EEU6sEAUFv9tRhQnU184-I6gQbEsWYctPAkZD95SZzqTS47zoGnKu94YQTBtZhCE8Ows4jtVBObb3KYnwVC5tBopQANPJrck64TNq2w1q2Vq3-cnnnfDTaFyK_D2OnmaPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FbrbqWuWEoJo6hJksumxaHSlbonZicriAm5yr8GoWTTZxxM3kGjhTchGXCZufLwKWBBuWacemwgkXsvyRH_9_xA3hfJG2k9SE2x0qv4uMXGmDUdMe37YEEkSKaBnxP1t8hmeBRfUBHfKvSVetFCNQocaZUmFrkgKL-BeYwKJrFXrYIeXi0obPqjBl4JIqfuyKckd2mGJXu87hN0K1qKKqA1DSl_RkAd7RydQTpYFM_8H-NVAexnpWM68gK1N8XK2YoicYUwT2R8s77H3LaI2rTh63QvTD_Ku89DakiG6m956O_GCbb6BXVkY4Ou9gVO5YLFSdJJ4WEr7kcl4YH9kRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLrIM0xXDeXj1vppixUl_J1B79wpRulDtd3tkkV933CKgWkfoGCBL15drn3EvpAfLLVnlKRrIQt81G-UVcG8mUtT9KGl91wjhJFGDTl-BWbolUuAYLgLDrJZsKTupHxEuZkr3WNxK6_R5KNz6onj9H3XVZOsHU0aevvM-sC3jPT_kQQz2QcfBKVGgMTMZiPguqBL7lY6fdBaNJm4HEjEioawhhJg3I3c6mCd8IbJNAutifCy20G2mmoJFFRVjHjJqg9tmgR0DHion_uuR3UYNwjXZkNER8m2SoLgyDv588IghV8bi941sRy38kKCQeOAEIw11XtmlER0jzOSWHtTZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWd4hCS-uzL6QRikofk0FWvzCF73L7qwOUGlaardKUR-sbhusMNsPRjVCB1DhZXDwyp_MXkoy4F04VYBFJCj9x49qXkNsGE3DLWiLD7DXvYP8ZTZNmoyzz3Tt4A9EtblUcBiI6AcFpaMtD4C8JJBFX1_GlJ3fbdYgSYtUP_jU5ylOJKmoShINOO9pSgak-gqI3q4L2Eqe56WObjaLxTymLEMCU1h42Lwe_IvAD0I8qQvxEQz6tOYoaF_R4ucEwce2l2P7_Left5RFYYOLOISTP45HV6eaX4GoudsGyhN2ndpLEL1dktU8mwORC1AYsFiiubKCjKxVu63Nu3Vylr89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vdJxdEqBpKFUgfgUCgkncXqhBvErCsdIiq_GjGtP-14zO555atsBch-8PU41Xii6XXaGQ6y6zbiEsGGjXpKEEmjjYAG4Ny93n65mHSBnpdo-a_k67gYrLnigX7HBvryyasHqlg_nlBo_eT38TNNw8cCB7-a8IbDLgaIj-W46syVft-tn0qe7x0sZURC9z4sBvxB8E6qXlvw5Clargg8_JiSJgqKA0nTuu19wgr1SLq1Zt8AIx3ckfFTBCY9RTZZBPlvghjNlXK8KxyR6e2tuSkei4DRhJysMPaeRPmf8ZT-gA228TcjZlp41b5p1Gqbx5gtf8zGDTMhtSvk3VvFj1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t3uT9AhsOrxKHFP2TnyRBKux_jBn2vc0TyUnaIYQP2ogk11V0-RoqI8ZDuRgsJ0oxmv1bEpL4vyX6XpndyyAHt_a7U9TXARLd5uY1aCkG9HOhf6t7t3mo-xIePDyCipb7-iSLvKMqLsY9dwFQuupm8Xs29RCEdf4tdfUF9twqq7tG_6GSfaeU6eyfc3_gxlr8yQ4JR5ug2qHhfFf8tEiqlB1kVS41k5W1iJw8WKgDxkKeFg9e9i7vr6AXvA58VAk39oFgsyy_LKHGDdmEuXFCu3FDFZYi_Dt9V8FVRBmyDB6Ren9QVnM4vixSJzEJ6b64Ibhb5kB0rg9bpL0E0EnsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) ظهر چهارشنبه ۱۸  شهریورماه از وقوع حادثه برای یک نفتکش در ۲۴ مایلی بندر راشد امارات متحده عربی خبر داد.
براساس این گزارش، «کاپیتان یک نفتکش گزارش داده است کشتی‌ای را مشاهده کرده که در حالت لنگراندازی کج شده است، که احتمالا نشان‌دهنده ورود آب به داخل آن پس از حمله با یک پرتابه نامشخص است.»
@
VahidOOnLine
مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در ۲۸ مایل دریایی جنوب شرقی بندر فاو عراق با یک پرتابه ناشناس هدف قرار گرفته است.
بر اساس این گزارش، ناخدای نفتکش برخورد پرتابه با شناور را گزارش کرده است.
خدمه نفتکش در سلامت هستند و تاکنون هیچ پیامد زیست‌محیطی ناشی از این حمله گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78295" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OeqjKgbLRpm12iSgNJ1zh-mDNuKoMbLfEg5rLxpchSZSyXv3AXFAOUHrZhSFeueeQIOC2rmshovhts2nXi1FHuOueVTNfXEEznFh7a5eT6Ok4s1XXYOE35X1lvpL3IcFLNBE9cijpNZPGRPnycbrx_ZTh8l2hQPIbApDKlfeagiBPGYicJNSD7-5iYLVS164UWNlTLf_5iBjHdMIFJu57VPI2LMfGEutifuFAmy3aJXE8ByUBszBvtcaKZnJP9qaHT2KrI-VBOVGpBySn1Dtx9Ozd1nJwTe7dgtu_62jqvf2htwspZGskQiLgXTujGLuantTmbSSqeohj__8kH0tAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
🚫
ادعا:
نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که دو ناوشکن نیروی دریایی آمریکا را که در خاورمیانه در حال عملیات بودند، هدف قرار داده‌اند.
این ادعا کاملاً دروغ است.
✅
واقعیت:
هیچ ناو جنگی نیروی دریایی آمریکا هدف قرار نگرفته است؛ تمام حملات مورد تلاش سپاه پاسداران شکست خورده‌اند.
در همین حال، نیروهای آمریکایی تنها طی هفته گذشته موفق شده‌اند ۱۰ نفتکش ایرانی را منهدم کنند.
این شناورها بخشی از یک شبکه سایه چندمیلیارددلاری بودند که منابع مالی سپاه پاسداران را تأمین می‌کند و ایران قادر به دفاع از آن‌ها نیست.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78294" target="_blank">📅 16:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U1V51u5V7xFBOcnry2XJvdAXJGY0n9ta5In_UNh2lBK3aPaFt2szInA_8evr3VtPlyTExBLih-DbWpbrgkA1zV1Pr6buPpDqAkobtNDHnsk9MGL6gPakWVA4rr9D7QBF_jBXuTctIZmyjBd2eTwdnLVpg_3F31_KPtJ_rrh_zSZH_lFWKMFdDuJjrEg1XB-tWuPxLj8OyTdDMllwWUhoISiTkh0deYQPmqpYGLEl4-ookv4gXUIZ3Vf72yQ4kcFLVae4jUDRzUyX4jom3ggHi-fum-gZ_bR6BpDP_eSkKoZ-4gkQFR-SpEMupsIiJMlExnTFTI5b5dk97-zESbp1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ماموستا محمد نزهتی»، روحانی اهل سنت و امام جماعت منطقه چیانه در شهرستان پیرانشهر، در یک حمله مسلحانه کشته شد.
سپاه پاسداران او را از روحانیون همکار با بسیج معرفی کرده و مسئولیت کشته‌شدن نزهتی را متوجه آنچه «گروهک‌های تجزیه‌طلب کردی» و «صهیونیستی-آمریکایی» خوانده، کرده است.
براساس این بیانیه، نزهتی سابقه «همکاری طولانی» با «بسیج اساتید، طلاب و روحانیون» داشته است.
سپاه همچنین فعالیت‌های او را در راستای حمایت از جمهوری اسلامی و آنچه «وحدت شیعه و سنی» خوانده، توصیف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78293" target="_blank">📅 16:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=Ds0w4yv8qx7t06UZbsUaWr1JxEEglUTOJm1Vd8ftHUjgTH0jYTAHQMSCjIl4lb3kAtEffoI2YM1lPZuqfbhA0gdsU4KmLyeCOgVpMm8N0nwSZnUqUZpgazJVlxmO4atGKGgQkbKEOE5PkVk2X_Wgjnry501bqls9-0vjGKaXZwoZwdu-DxzTRw1eXxbS5EUlTdLOA3hvOBLKGzzRRI48MHW6WA22i_myWw0vxoIbTz83J6KZl4kUz3Ar1URycW9FyrKLTdOrBB-uGdh6igi4opovpRm3jhBSTUbPQ8EyDuYwnr1puoLOctuyKuOfNIbvbrKqGyyYQxHmwEcDsMLB-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=Ds0w4yv8qx7t06UZbsUaWr1JxEEglUTOJm1Vd8ftHUjgTH0jYTAHQMSCjIl4lb3kAtEffoI2YM1lPZuqfbhA0gdsU4KmLyeCOgVpMm8N0nwSZnUqUZpgazJVlxmO4atGKGgQkbKEOE5PkVk2X_Wgjnry501bqls9-0vjGKaXZwoZwdu-DxzTRw1eXxbS5EUlTdLOA3hvOBLKGzzRRI48MHW6WA22i_myWw0vxoIbTz83J6KZl4kUz3Ar1URycW9FyrKLTdOrBB-uGdh6igi4opovpRm3jhBSTUbPQ8EyDuYwnr1puoLOctuyKuOfNIbvbrKqGyyYQxHmwEcDsMLB-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مادر یسنا (فروغ) اسکندری در سوگ دخترش
یسنا اسکندری، وکیل دادگستری و نقاش، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در منطقه آریاشهر تهران هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78292" target="_blank">📅 16:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fcBj9Ek3sjy5wENb8v8o4jrB4Pw5t2k080F84fl3zgyakqKd4NcOAJ7y4khu1ahZSkon4L_eUqYs8KcWDdFTrSXGUPkCfOkJ4WB1ZaV3iXjyh_gG2G2WJtfXEjm3gRPmMSf02ZZwa10o8L2mKqe0jjnPWfhTB68WW6Gc0P9bqj7PlQAgrFK2WBeNOyMXNgKB1mPu9tl6uupIOURzLM9JrguOv_A2gaH0_YF_ah2ZhnS8BF2Y2r4MB6C593EDMKdU0mzousUdL-9kfuHo5hhiaeMbr7HNcQZFKUpT0uoTDnqG09RX1p5jWI82Qd9LwqGNFH1rEztCR6q7XVoRL7KreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=KsQBF7-UNPzBLrkEvXyMoPzJEkgw4hW9SLgBa2yxd_KdtkrbezUoY9oAjQQlOrDcB4vZBJdQ43XbIgetBamdQOld1sc2voczdrBDloS1eo2HYgA1WKYlnOCWi_DdO3uQ_SAq_bzw5FNFQpXHJ9fWwSW24mCpUZn9IDhF9XUKUOxnVIfAMtuGeJOUwlRx1sYS0kojRRrwpm75_T8KvF3UauruEurIxVoN5AIvtxPJDzbAhIn07MV8xNTviMQEx8ABlMqmqHg8N0mk-px7UXXu8FcWmd9G2yVu9ttJsK7j78qrbHh3lqZ2KfAJzR2fLa-iAwQpS8pA5QiWCw6mmL0cOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=KsQBF7-UNPzBLrkEvXyMoPzJEkgw4hW9SLgBa2yxd_KdtkrbezUoY9oAjQQlOrDcB4vZBJdQ43XbIgetBamdQOld1sc2voczdrBDloS1eo2HYgA1WKYlnOCWi_DdO3uQ_SAq_bzw5FNFQpXHJ9fWwSW24mCpUZn9IDhF9XUKUOxnVIfAMtuGeJOUwlRx1sYS0kojRRrwpm75_T8KvF3UauruEurIxVoN5AIvtxPJDzbAhIn07MV8xNTviMQEx8ABlMqmqHg8N0mk-px7UXXu8FcWmd9G2yVu9ttJsK7j78qrbHh3lqZ2KfAJzR2fLa-iAwQpS8pA5QiWCw6mmL0cOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iFWFPdW8n8La-L0qDbs49Zs21iSVch9okcRqVCQ2r03mm5NsEGfplml_NlE1eMzd070OsDZ1hHMhZV5Ebwu8tjPQLueszPz-vYJimGu9j0wMmysgXYnYeiZwJ_47yv2j2NRwwt6Nuh680NALn_MnKR8ORG9uCG7J5ftmrA4cRJb4Jk9upjcJ8hOrGg2hZIdR7O_bIPE9qJOoemlrSAFNrEZbQpqDMIUhLv1doOyC2KnqWJHUcziHytOILqVLLXE3TJG2Ef5wkvIQo3EozyNgo4ip-NEyFWzOhJ9jtfSbsANrRihHNWmx9i_ahgaCIA81XaXS3yFDxtYCqpk4PlU6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای خطاب به «مردم مبعوث شده ایران اسلامی» اعلام کرد که با رمز «حیدر کرار» به پایگاه الازرق اردن حمله کرده است.
در این بیانیه آمده که به محل استقرار جنگنده‌ها حمله شده است.
پیش‌تر اسکای‌نیوز از رهگیری موشک‌ها در آسمان اردن خبر داده بود.
تلویزیون دولتی سوریه نیز گزارش داد که پدافند هوایی سوریه برخی موشک‌ها را که از ایران شلیک شده بودند بر فراز شهر مرزی اربد در اردن رهگیری کرده است.
برخی رسانه‌ها در ایران از جمله همشهری نیز گفته‌اند که سپاه با «موشک‌های خوشه‌ای» به اردن حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
