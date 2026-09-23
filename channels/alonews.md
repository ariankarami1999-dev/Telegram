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
<img src="https://cdn4.telesco.pe/file/V06Vx_Ph5BJQfpTsFpQ0v7ibQsHa9vyUH3fIz-peco3MCJtmg48yka9YWNBke_-xPIK520J9ni9vJr_Fn2TCPS-udygPuRmnYg0s3RhI3WH8SWny_FXHWfXbX3dHugoutq4rIPR5OsvnU-xg9YgZFFGtu2wTZ6oFDM3Yk95Ip7MWRoATknTysgzzQKPq67NVpdyIrxlsF9_yN7bZ04etDVjTucwjzaPgDY9gk9i-772r-9j1nsLYsjxgpEQDYPiuz_YccWpXIerayTMXUAqpayIFAG3pwMdn0UBSCbfmsQ04MbhxWCh6ycomDaBdYRHg7kTC19vzuGye5fCbPzMsJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 22:38:16</div>
<hr>

<div class="tg-post" id="msg-149034">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دولت ترامپ: فعالیت سه رسانه تهدیدی برای امنیت ملی است
🔴
به گزارش USA Today، وکلای وزارت دادگستری آمریکا در دفاع از ممنوعیت فعالیت CNN، MS NOW و پولیتیکو در کاخ سفید استدلال کرده‌اند که نحوه گزارش‌دهی این سه رسانه می‌تواند تهدیدی برای امنیت ملی ایجاد کند.
🔴
این استدلال در جریان پرونده قضایی مربوط به تصمیم دولت ترامپ برای محدود کردن دسترسی این رسانه‌ها به کاخ سفید مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/149034" target="_blank">📅 22:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149033">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
احتمال صدای انفجار کنترل شده در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/149033" target="_blank">📅 22:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149032">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تحریم‌های جدید کانادا علیه ایران
🔴
وزیر امور خارجه کانادا: امروز کانادا تحریم‌های بیشتری را تحت مقررات اقدامات ویژه اقتصادی علیه پنج فرد و پنج نهاد ایرانی اعمال می‌کند.
🔴
دلیل  این تحریم‌ها «حقوق بشر و خشونت غیرقانونی» ذکر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/149032" target="_blank">📅 22:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149031">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
هیمتی: در حد توانمون تورم رو کنترل می‌کنیم باقیش رو هم هرچی خدا بخواد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/149031" target="_blank">📅 22:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149030">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
جزئیات مذاکرات ایران و آمریکا در سازمان ملل/ آمریکا رفع محاصره دریایی ایران را نپذیرفت
🔴
مذاکرات ایران و آمریکا در حاشیه مجمع عمومی سازمان ملل با میانجیگری قطر انجام شد. در این رایزنی‌ها، استیو ویتکاف و جرد کوشنر از طرف آمریکا و عباس عراقچی از طرف ایران حضور داشتند.
🔴
اسماعیل بقایی، سخنگوی وزارت امور خارجه، گفت هدف این تعامل، انتقال شروط ایران از جمله پایان جنگ، توقف اقدامات نظامی آمریکا، رفع محاصره دریایی، پایان فشار اقتصادی و آزادسازی دارایی‌های ایران بوده است.
🔴
با این حال، بر اساس گزارش العربیه به نقل از یک منبع آمریکایی حاضر در مذاکرات، واشنگتن درخواست ایران برای لغو محاصره دریایی را نپذیرفته و اختلافات میان دو طرف همچنان پابرجاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149030" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149029">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صید یک ماهی عجیب در دریای بالتیک  [@AloTweet]</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/149029" target="_blank">📅 21:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149028">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ5FcJI2FRSTe7e6lCiyQyYg-x7R1B_RbgrGgVbpRh9UxCnYEX2c2rGVTImVOFTZ9LwrpXhsE602CEHaQMQk08CKp1TXwCEutkxhC-jywi1knmu7C3vk2YpPaeiG8H2bZfWkEpM2Y721rnpmq7vULV0GTJ_izf7rvi8cS-2ylDLw2t1ITCBaIy7eABweyUsw0IrZS1RBkL28wYuVSvLSpn3mMAgTEpm7sPPLTwza5iumvkBABw4cnero03PBanm6Yf-4Ei0BRwvYzK_s2MKagbinNPvl4R8vJ83yFy8UUo3N9cVX1OrpzLzujseLTmTi-fFGeC1D1tUf7QoYRKem6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش روبیو به سخنرانی پزشکیان: کسانی که ده‌ها هزار معترض بی گناه را میکشند حق حرف زدن درباره منشور سازمان ملل را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/149028" target="_blank">📅 21:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149027">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
زلنسکی: امسال به طور میانگین هر ماه ۳۱ هزار تا روس رو توی جنگ کشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/149027" target="_blank">📅 21:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149026">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfa61ab86.mp4?token=j8Z4wfvlJcQBg5h2xXirhLHSNm7BwGxCk4eJVv-ermro2--WfoF2ZaECvz74GPiw9IhqXP8m-7I5fn6NVQYkFJr3fAERCMs0L8daX-pfddZ9BGFarYc0foAFKOuZ2g2YqLxrvU42DLyH5LFTfCOYaCLlla0IPNrDTF5LcqvgCscRYTRyATaW7147PCXf7iJXIWM1LuwrmlcRTU4e9heZ8kK_VWtQVaoyqXGRWWmYD4wCbuH49uSeism0Oz7_4rwBNbm-Tmqk46uHTL8zQlCjwyv17NiwkXXaf_uEnKLfEyHn5jtmnbpJDCYozNeiihSOxE5b3WOOhv2MeTR8H40w-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfa61ab86.mp4?token=j8Z4wfvlJcQBg5h2xXirhLHSNm7BwGxCk4eJVv-ermro2--WfoF2ZaECvz74GPiw9IhqXP8m-7I5fn6NVQYkFJr3fAERCMs0L8daX-pfddZ9BGFarYc0foAFKOuZ2g2YqLxrvU42DLyH5LFTfCOYaCLlla0IPNrDTF5LcqvgCscRYTRyATaW7147PCXf7iJXIWM1LuwrmlcRTU4e9heZ8kK_VWtQVaoyqXGRWWmYD4wCbuH49uSeism0Oz7_4rwBNbm-Tmqk46uHTL8zQlCjwyv17NiwkXXaf_uEnKLfEyHn5jtmnbpJDCYozNeiihSOxE5b3WOOhv2MeTR8H40w-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید حدادیان، مداح: مجتبی خامنه‌ای امام ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149026" target="_blank">📅 21:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149025">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💢
قیمت دلار و طلا منفجر شد</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/149025" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149024">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
زلنسکی: فقط یک نفر علناً طرفدار ادامه این جنگ است
🔴
من هیچ‌کس را نمی‌شناسم که علناً طرفدار این جنگ باشد، جز یک نفر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149024" target="_blank">📅 21:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149023">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6137406465.mp4?token=iJhTXbwlprWqVETWRrUBQkMKd1pThSh2iZNY1BfPodpb68fzurd_CSm3QAfdWgRkA_t_QWdmwxj0tpZ_f_ZXlnBT-FYqhhNYpnk_ECrEP9V1NyfSbCmv55lzaY9gmMKsXMf3ZgHWxSpYDvDmoQDy-sJf2sQYjGbqrZoodakJT86NEZfDWV1x6345DwK6hdylPT2AACj5AkeDVsDNyFSPMdINeNKTgsTDuc1iYPAXPCJaPdLim1EdmV_htFxYDTHzaIM2DsrpKUTCZZ2tSXqfsSFH2IrWhQmforwIMcOc6Z0USB5Vyp11QhE_F8JfKVHt-jTTpXjnP3-hbLkK0FEhFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6137406465.mp4?token=iJhTXbwlprWqVETWRrUBQkMKd1pThSh2iZNY1BfPodpb68fzurd_CSm3QAfdWgRkA_t_QWdmwxj0tpZ_f_ZXlnBT-FYqhhNYpnk_ECrEP9V1NyfSbCmv55lzaY9gmMKsXMf3ZgHWxSpYDvDmoQDy-sJf2sQYjGbqrZoodakJT86NEZfDWV1x6345DwK6hdylPT2AACj5AkeDVsDNyFSPMdINeNKTgsTDuc1iYPAXPCJaPdLim1EdmV_htFxYDTHzaIM2DsrpKUTCZZ2tSXqfsSFH2IrWhQmforwIMcOc6Z0USB5Vyp11QhE_F8JfKVHt-jTTpXjnP3-hbLkK0FEhFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشت پهپاد که امروز توسط طالبان افغانستان به سمت پاکستان پرتاب شده بودند، سرنگون شدند.
🔴
در این حمله از مهمات سرگردان، پهپادهای انتحاری و کوادکوپترها استفاده شده بود، اما هر هشت فروند سرنگون شدند.
🔴
گفته می‌شود تمامی این پهپادها در مناطق کوهستانی خارج از کوهات و در نزدیکی تورخم در ایالت خیبر پختونخوا پاکستان سرنگون شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149023" target="_blank">📅 21:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149022">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
کانال ۱۳ عبری: نتانیاهو امشب اسرائیل را ترک می‌کند و فردا صبح به نیویورک می‌رسد و فردا شب بلافاصله پس از سخنرانی در سازمان ملل به اسرائیل باز خواهد گشت.
🔴
نتانیاهو به دلایل امنیتی ویژه در خاورمیانه، حتی یک شب هم در نیویورک اقامت نخواهد کرد و فوراً به اسرائیل بازمی‌گردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149022" target="_blank">📅 21:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149021">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
محسن رضایی: هر کشوری حریم هوایی خودش رو به روی ما ببنده، فرودگاه اون کشور رو نابود می‌کنیم؛ اون‌ها هم دیگه نمی‌تونن پرواز داشته باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149021" target="_blank">📅 21:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149020">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پزشکیان امروز غیرمستقیم گفت که معترضان دی ماه، مزدور مسلح شده توسط آمریکا و اسرائیل بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149020" target="_blank">📅 21:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149019">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
👈
بقایی:
بله دیروز با آمریکا حرف زدیم و براش شرط گذاشتیم جنگو محاصره و فشار اقتصادی رو تمام کنه، پولامونم آزاد کنه، تنگه هرمز هم دست ما باشه و یه دور هم به ما بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/149019" target="_blank">📅 21:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149018">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فارس: پزشکیان در نیویورک در هتل مستقر نشده است
🔴
پزشکیان در سفر به نیویورک به‌جای هتل، در محل اقامت نماینده ایران در سازمان ملل (رزیدانس) مستقر شده است
🔴
این اقدام با هدف کاهش هزینه‌های سفر، برای اولین‌بار توسط یکی از رؤسای‌جمهور ایران انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/149018" target="_blank">📅 21:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149017">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر نفت: پول نفت‌هایی که فروخته‌ایم درحال وصول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/149017" target="_blank">📅 21:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149016">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پولیتیکو به نقل از منابع آگاه گزارش داد:
دولت ترامپ در حال آماده‌سازی طرحی برای ممنوعیت سه ماهه صادرات گازوئیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149016" target="_blank">📅 21:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149015">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU2cPHMDMdpbX1THgGVbgdSu7b337BLJtzSWKa5hxA2tP_23rzVDQmEHID-ydhZVfNq7qsMmH3Fttog3cvIQz_reDmfT4M4Uy0TQREFcX04bn3bz4tYpTwTvWuApdIncmr5tUUPI36GA8BoCCdwvTCkwj_x5Lc1-vMDUwaeVCuMXHvqpYK9ED7R-IbBdhlhiMPNCPfye4jow9nirw_k2aMgSPklU0t1hSGHu7HHRuXtbH3gNrmdqlrWFye0Aof-TKEqfr1jikC5HcDA84LKyYMKjlGIkfGBZH3b_VVIP0_ax2DsTPdlWKAvE1Mrm2xYPCtBq4t6w4Wg9ObsJAt6vJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آپدیت جدید تلگرام اینجوری که وقتی وارد پروفایل یکی میشین اون قسمت بالا شمارش میزنه بطور میانگین، چقدر سریع به پیام‌ها پاسخ میده مثلا ۱۰ دقیقه، ۱ ساعت یا ۱ روز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149015" target="_blank">📅 20:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149014">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15548e76f5.mp4?token=J435x_oMuDskV1miFiAr2K-uirnRq0uDrM2-qg7MtzW0IFL8JpLSHGUvNN3LQmzPL_qEVDsIUU6X0mhOgXATghjkcz0g_UqeT25avgloDcYJyknUR1MuM6O91msvNuuMs-eIc-IosQuvvu22pDvBXNf-57QFwoOYiT5Fyf13FToV8Ia10pHgJYnHM9j3D0DsmGJuHHacPLVuE92cyO2eH7sZyrmZgKgEK9CbLJXYD1Hgi-3WJmpbL9Xm1NJfSigg62Dp8lB03l3YMwtoJVbyH0eNa5jQS9At5kOsGCoVG5QDznL3eoqCQAtpGIIeJzPF4rTb19plPbsd0-WH5ozfDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15548e76f5.mp4?token=J435x_oMuDskV1miFiAr2K-uirnRq0uDrM2-qg7MtzW0IFL8JpLSHGUvNN3LQmzPL_qEVDsIUU6X0mhOgXATghjkcz0g_UqeT25avgloDcYJyknUR1MuM6O91msvNuuMs-eIc-IosQuvvu22pDvBXNf-57QFwoOYiT5Fyf13FToV8Ia10pHgJYnHM9j3D0DsmGJuHHacPLVuE92cyO2eH7sZyrmZgKgEK9CbLJXYD1Hgi-3WJmpbL9Xm1NJfSigg62Dp8lB03l3YMwtoJVbyH0eNa5jQS9At5kOsGCoVG5QDznL3eoqCQAtpGIIeJzPF4rTb19plPbsd0-WH5ozfDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرگئی لاوروف، وزیر خارجه روسیه:
اگر اروپایی‌ها این بازی‌ها و اقداماتشان را انجام نمی‌دادند، اوکراین مرزهای سال ۱۹۹۱ خودش را حفظ می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149014" target="_blank">📅 20:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149013">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJ8NGcOmrNYm9MNbjWzkUhiPIjUT18IYheXCByoq-e-7vz5SB0LBMwHhB5Vw2vSurLjwe5fCMI7aO9rO9vGRqWM1FaoQsXJTuVMzqfgNWaM3O31QKOtEadFvowHZ6neNPhelai30cBDdziZfgkDWKRn_UG4Y9aprBLfhHGO_XNF5voKaKGfoNydQp159YmPZARWlM2ON9eelQ8sh0U0sWVMRmAl8gkGgREaOdDHEayNcakSFOM9nDp_avr7J4Yh3pIiMvph0hINfjqvb_WEo-9L1Kpx0fqo-WjXwJ-4GDiEfaqVylx8IOCCuMwly3MX9ns-dJi03r9WElgqQa1Qjsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور دختر و داماد پزشکیان در مجمع سازمان ملل در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149013" target="_blank">📅 20:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149012">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تنگه همچنان تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149012" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149011">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
توفق فعالیت بانک ملی ایران توسط امارات: بانک مرکزی امارات فعالیت بانک ملی ایران را در این کشور ممنوع کرده و تمامی شعب آن را از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال پول، منع کرده است.
🔴
بانک مرکزی امارات دلیل این تصمیم را نقض مقررات مالی این کشور، از جمله رعایت نکردن الزامات مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/149011" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149010">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9accb50b1.mp4?token=N8sdZIwEOg4X3_b6lttVnLPFS3TciP2c2bGz4phtDebxQ8Txk2vfwOJWzrR84F3zbEL0mrcEyp7qdAOuBWLeExIOB7tGGYlgzpAej-GHR5TphVV5g28Fn5hmn3vLi5peElRrk3ZQ86Tb004VIZkx_GlEvPGz7rg1FkSl6qsBnzatUFjMwvrp7A_DuYqAvZlBNZzCHXxIR5EpEnHt-_3odD42WQbZ6y0cc_XXjqYYNMIDW_BlD1TTEEkj42ziuxOGQPQWtdK1SvF2PKNkKgzWq7-VKFssJ0bBw9UHHBvt8ooWtTHL6LDKnEazzDBWejgG1N8_cnI7F9A5tdNXT3JJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9accb50b1.mp4?token=N8sdZIwEOg4X3_b6lttVnLPFS3TciP2c2bGz4phtDebxQ8Txk2vfwOJWzrR84F3zbEL0mrcEyp7qdAOuBWLeExIOB7tGGYlgzpAej-GHR5TphVV5g28Fn5hmn3vLi5peElRrk3ZQ86Tb004VIZkx_GlEvPGz7rg1FkSl6qsBnzatUFjMwvrp7A_DuYqAvZlBNZzCHXxIR5EpEnHt-_3odD42WQbZ6y0cc_XXjqYYNMIDW_BlD1TTEEkj42ziuxOGQPQWtdK1SvF2PKNkKgzWq7-VKFssJ0bBw9UHHBvt8ooWtTHL6LDKnEazzDBWejgG1N8_cnI7F9A5tdNXT3JJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خاویر میلی، رئیس‌جمهور آرژانتین:
حملات رژیم ایران علیه اسرائیل را محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149010" target="_blank">📅 20:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149009">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP0a2kWY45kLiLmOUtaVaufqM6UYTCpaK3TBA77_iuh_2yqMsTCqPVc5FQa7OKvwS_bbS59Kg0WuHy5nZo-iJX-9ogaXPzuDaVNgKv5ONQhEgruC3C5CT1HL0MQpKAqkXQFr5jEKlL0zxInqUDLfNDD-5Uo135eVTMp018vpFhhRZVbNdgTZhkcy6AdrjJspMTFRxJ4hB1fI7MHxNoyfSqXMolQDIJU8s0nJ3r59YHu1oqh_08W1UpHqbaWktuezx2rMGtkywZGzgHcoajmdOjmzp7qYn4QSDO6PgFPmWdY1VsB10u5GlR0TS2bnq85xQpi6Zs7FD4z3WsUDPbCh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار پزشکیان با نخست وزیر عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149009" target="_blank">📅 20:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149008">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کوشنر: دستیابی به هدف رفاه در نوار غزه، مستلزم خلع سلاح کامل آن است و حماس موافقت کرده است که سلاح‌های خود را تحویل دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149008" target="_blank">📅 20:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149007">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCnPBnr8Dt-1vX9FoE2wcPlhYCJ3FHVmVwjwfqyE0AJT2W7zUrIUyj4Hh0ZJtwTqfQggP2cfX0PGLrtkz4dXid6BrwIoRlQdyDQAxpB6bQIoNP6aEvsph7Ak5D60W4jP0Rf_jzvjgbTLjvjNlWHqHKTpR_shjs817wPhBV20P11PDraodh89oHM1xPmPjFFKv-uIxnEKQRC8N7u8T2ekSg61CCfMyhs40t-WSddiD9xt1XakDaVbFOJzxGxTTHKxttg6tCL_JrbibMQpls6ebrvB29cdJp-volz7Tcp-iha-7e-IV6tzRQkf_cJEYEFI3I6W--abbvohDCxwjkb-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: رئیس‌جمهور پزشکیان نه تنها برای یک دولت، بلکه برای تمدنی ۳۰۰۰ ساله سخن گفت.
🔴
او صدای قدرتمند شجاعت، استقامت و قدرت برای جمهوری اسلامی ایران بود.
🔴
ایران سرافراز و مقاوم، به درازا زیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/149007" target="_blank">📅 20:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149006">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e39111516.mp4?token=chgKX1XfloWVakSa4iD3cz2XAAvA2NmK4xFEyY_R-2_qiDZIpjF2lBty30PRELUOtDD1hRAsxwZvNnozFsigrqa31xTcumqDHQgvaN487UsckXIjz7XUthK9tHqIF2g6GbX6df6hQFzbeQMXOoRrWphfMox1-6Bm8qWTLlFk2xdEm2fFMHDdA3b0ZgsHMK7HqJTdB4F1XqseeXYLQGM65o5P620cS08tiXp7xn51g5s6JWVTwXzJZyCcVyeRff48zQ1ItOgp1Jn-7P3fCjA83Za2uwge9fPoGbl8CZwlPgpsMK0plsThSFPHW9MC3d_G2o8QW0O7SBXFhHOWyxTmRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e39111516.mp4?token=chgKX1XfloWVakSa4iD3cz2XAAvA2NmK4xFEyY_R-2_qiDZIpjF2lBty30PRELUOtDD1hRAsxwZvNnozFsigrqa31xTcumqDHQgvaN487UsckXIjz7XUthK9tHqIF2g6GbX6df6hQFzbeQMXOoRrWphfMox1-6Bm8qWTLlFk2xdEm2fFMHDdA3b0ZgsHMK7HqJTdB4F1XqseeXYLQGM65o5P620cS08tiXp7xn51g5s6JWVTwXzJZyCcVyeRff48zQ1ItOgp1Jn-7P3fCjA83Za2uwge9fPoGbl8CZwlPgpsMK0plsThSFPHW9MC3d_G2o8QW0O7SBXFhHOWyxTmRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی که تحت عنوان خروج نماینده‌ها هنگام آمدن پزشکیان منتشر شده مربوط به پارسال و سخنرانی نتانیاهو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/149006" target="_blank">📅 19:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149005">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO1HuDiyuUU8Al_UEXHsOuKfvzbBeWsboavPS2Bz8Rwd-5ZDdtA9K2bfthjHHJ8mjuW0CkORcq2Q2qzztUEi86MQ8mqMC3Sul7pd3C7EMg7QuufCvml65h-QOLpkMMQLwty7l2-rteLjOrzxWapdwsaUowJ4I5dEbTJGywoFadHslJWm-5dF5YzACffMEXGRYoCp6q0GukVmxP8O14UU6tQ7HmT92DAWxa5tikDzF8rgsbgo_fxjkS31_Nnfyve9Pzhsa17AXCS9k1HQ9O6BR4F3HRHooJbvCfOfjyTsE34UntXhpIOmJmIEfyEzm5HaOlMwCVKPmmtLC3mnJ4lfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت برنت، ۱۰۲.۷۶ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149005" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149004">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6_qHQUgM-5yhYZ7qWt-3xkLqXEBIxLTl7jq6eCM0UVDZbfrEcfLjnuqPs8WDxY65lBSHgjo-GJMj_qRyfgojNw99KjUiy8HACDnoyTGLBOp2lHspPSP-CRmRTh6CfKs1YefLv9N-DNnZdE2vm5AAY7UMKH1ryOTUT9U2VwB00GoiLx0xzvMWKgkxNhfflOfwsnjmpv740pI9viiCLPBfpgIZsGOFBAEtGjdlcOaPoUFLh7WLy4__NGow0lKan5REDQDjlhfOdvY03v2yQ1fQvdNHmoDUB86uHFIpnBO8u2KkKLLcHHwemAMlIlMzQgdTHj-0mjjMjxYhgUTmfgP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنتاگون در میان جنگ با ایران، یک فوت نظامی آمریکایی دیگر را به پایگاه داده عمومی تلفات خود افزود و مجموع رسمی اعلام‌شده را به ۱۹ نفر رساند، هرچند مقامات آمریکایی می‌گویند تعداد واقعی بالاتر است، به گزارش واشنگتن پست.
🔴
ارتش این افسر را کاپیتان بیانکا سی. ویلسون، ۳۷ ساله، ساکن نورفولک، ویرجینیا، شناسایی کرد که در ۱۸ سپتامبر پس از یک «اورژانس پزشکی غیرنظامی» در حین پرواز به خاورمیانه جان خود را از دست داد.
🔴
او به پایگاه هوایی شو در کارولینای جنوبی منتسب شده بود و در حال حمایت از عملیات در دوحه، قطر بود.
🔴
ویلسون پس از مرگ به درجه میجر ارتقا یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/149004" target="_blank">📅 19:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149003">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / حادثه برای یک کشتی در نزدیکی ساحل عمان
🔴
مرکز امنیت دریایی عمان: ما خدمه یک کشتی تجاری را پس از هدف قرار گرفتن در فاصله ۲.۵ مایل دریایی از سواحل استان مسندم، تخلیه کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149003" target="_blank">📅 19:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149002">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2901dc9b92.mp4?token=YZOZ9esQKt3nosDtk3op3PKk4dOGDoM5i2Bc18NM-yauuEy11IgqQFQK_H0gzgkjHOTnmxYhbbSECNjsh-_SGNmsgt6w6HYeLhECZCEr1i7VRjzYFffqT1Kne5Pp9lPV23FlCdDu2M0ggXBeRIf5ApM1_K-N3Roj7smVHOBPgaulKYpR9SB_pp0_O3NqIgdna-1cC4t1yzc-rNOFiZDNIvJp8-YzgjfrPorpXl4lbGtWJ7Q_ytDyYsdE7e-yulEqdfvqfO7hntQBBS73MIjS2l-Pw3I-HmNaGiUJlgfSIhfMiDPR1cSng-stWTnXh7ukqODHt-jDbTAMPMa46a4NNL-gLevw7rea8OSAsM8glthaFb9fjXHiALGIP1_3N_wr5kBzNkPTyK_lE9w87yzE0akTqvvI3lwS3i6Y3GczCch8k8CdNOLp-E4wG6Dl5tZ2X16981dJ4q8HBahFmBlNHwWhNGjB1ABHM9Tx6HNT0t3LO1S4GxwvBlLMi3ZJ-jApCfZRp7Ye2wmYi4GCf-Azy09mIoSjn3-wGyXhWHY88MZ2YgsUExJ3ydv4zybRgLHDTi-pfUqZKfBDVKYNfm9Xw6Iz7xRaM2Y-zGdogOW8OBXLNSaVfSCSVLdpzl0iP4-CspJ2mLCaEaPKTX7f5JVgGEsy4xoru06CZwjUVh1-QXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2901dc9b92.mp4?token=YZOZ9esQKt3nosDtk3op3PKk4dOGDoM5i2Bc18NM-yauuEy11IgqQFQK_H0gzgkjHOTnmxYhbbSECNjsh-_SGNmsgt6w6HYeLhECZCEr1i7VRjzYFffqT1Kne5Pp9lPV23FlCdDu2M0ggXBeRIf5ApM1_K-N3Roj7smVHOBPgaulKYpR9SB_pp0_O3NqIgdna-1cC4t1yzc-rNOFiZDNIvJp8-YzgjfrPorpXl4lbGtWJ7Q_ytDyYsdE7e-yulEqdfvqfO7hntQBBS73MIjS2l-Pw3I-HmNaGiUJlgfSIhfMiDPR1cSng-stWTnXh7ukqODHt-jDbTAMPMa46a4NNL-gLevw7rea8OSAsM8glthaFb9fjXHiALGIP1_3N_wr5kBzNkPTyK_lE9w87yzE0akTqvvI3lwS3i6Y3GczCch8k8CdNOLp-E4wG6Dl5tZ2X16981dJ4q8HBahFmBlNHwWhNGjB1ABHM9Tx6HNT0t3LO1S4GxwvBlLMi3ZJ-jApCfZRp7Ye2wmYi4GCf-Azy09mIoSjn3-wGyXhWHY88MZ2YgsUExJ3ydv4zybRgLHDTi-pfUqZKfBDVKYNfm9Xw6Iz7xRaM2Y-zGdogOW8OBXLNSaVfSCSVLdpzl0iP4-CspJ2mLCaEaPKTX7f5JVgGEsy4xoru06CZwjUVh1-QXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو، درباره مهمات: ما مهمات کافی برای دستیابی به اهداف خودمان در صورت ایران داریم، اما تنها در ایران نیستیم.
🔴
ما تعهداتی در منطقه هند-اقیانوس آرام داریم. ما تعهدات فزاینده‌ای در فرماندهی جنوبی داریم. ما تعهدات و متعهد بودن‌هایی به ناتو و شرکایمان در آنجا داریم.
🔴
هر بخشی از جهان که بروید و به آن‌ها بگویید که پنج سرباز آمریکایی کمتر و دو هواپیما کمتر خواهد بود، همه وحشت‌زده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/149002" target="_blank">📅 19:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149001">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
روبیو: سپاه مانع مذاکرات با ایران شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149001" target="_blank">📅 19:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149000">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016da093a0.mp4?token=Q47cDijNAoLzeuNBvL_8ezkOfb3Wf1n9HH-KtrlY4t6cIj_WsmjM3YzUpqqR6UT7KH-XghzzOvexE28EBCTq8_Kv4P7Lp8KvgKScUqstQrdTzwvqE5Y7ZEwm13dnbCbnt07F0wlk_TsyAcO7HIXT6ApONONhZae--y7r6_CGu8c1Anah13PVd5YDH7lR3TfeT-GXGenCl_zwCB1ows-MsSTIOSD-mztw7n9_n-AF8MsMiYyDkO7-sQGGZqFvewemRDiGO2KWw40WXFSlUXq20RF2eyf30biMGS6R9nloYTh72t8eSGzPZiAdaT712KO-5gg0HXNYcMLX_Aq-4BBDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016da093a0.mp4?token=Q47cDijNAoLzeuNBvL_8ezkOfb3Wf1n9HH-KtrlY4t6cIj_WsmjM3YzUpqqR6UT7KH-XghzzOvexE28EBCTq8_Kv4P7Lp8KvgKScUqstQrdTzwvqE5Y7ZEwm13dnbCbnt07F0wlk_TsyAcO7HIXT6ApONONhZae--y7r6_CGu8c1Anah13PVd5YDH7lR3TfeT-GXGenCl_zwCB1ows-MsSTIOSD-mztw7n9_n-AF8MsMiYyDkO7-sQGGZqFvewemRDiGO2KWw40WXFSlUXq20RF2eyf30biMGS6R9nloYTh72t8eSGzPZiAdaT712KO-5gg0HXNYcMLX_Aq-4BBDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: به نظر من، ایرانی‌ها معتقدند که دموکرات‌ها در ماه نوامبر پیروز خواهند شد و ترامپ دیگر نخواهد توانست هیچ کاری علیه آنها انجام دهد. آنها کل امید خود را روی این بسته‌اند.فکر نمی‌کنم آنها درک خوبی از سیستم ایالات متحده آمریکا داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149000" target="_blank">📅 19:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148999">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه: دونالد ترامپ واقعاً معتقد نیست که جهان در حال حاضر به یک «بحران کرانه باختری» نیاز دارد و این موضع ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148999" target="_blank">📅 19:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148998">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مارکو روبیو، درباره چین: روابط ایالات متحده و چین سده بیست و یکم را تعریف خواهد کرد.
🔴
ایده اینکه ما در بالاترین سطوح با آن‌ها تعامل نداشته باشیم، بی‌مسئولیتانه است. این امر بی‌پایه و اساس است. ما باید این کار را انجام دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148998" target="_blank">📅 19:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148997">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25554fe971.mp4?token=kWDPVpEPv6BXEfSkPbqiIqbQXojr5DEKeN8Yz0_HrGNZo9LTt_FK3_ioCoAlO3UTiViBT2gkPTnpBI3EnTItnQ0zuSSDOLqWrmlr93w0ydR5KVvGqV1ephvB3PCA8ESP9KDox3GNLptIfCHse_m6sxQixmfHI5rzgrUpAiD4yB7VsFy1IuyqMKSRgJig9-OsX5DinZOOuqT9Kz-bFgcjIdDclmPGxEhaT6yAfKpVYYBeFXKITlY-TG_V-8m4OtLivQwtncuR8LqiiMT-LOOMP38j1ne8_AkDR326FIknMyx4L1OnPBjupIyBykaK9DZbMHr00FZsozc6oa13kJ1PLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25554fe971.mp4?token=kWDPVpEPv6BXEfSkPbqiIqbQXojr5DEKeN8Yz0_HrGNZo9LTt_FK3_ioCoAlO3UTiViBT2gkPTnpBI3EnTItnQ0zuSSDOLqWrmlr93w0ydR5KVvGqV1ephvB3PCA8ESP9KDox3GNLptIfCHse_m6sxQixmfHI5rzgrUpAiD4yB7VsFy1IuyqMKSRgJig9-OsX5DinZOOuqT9Kz-bFgcjIdDclmPGxEhaT6yAfKpVYYBeFXKITlY-TG_V-8m4OtLivQwtncuR8LqiiMT-LOOMP38j1ne8_AkDR326FIknMyx4L1OnPBjupIyBykaK9DZbMHr00FZsozc6oa13kJ1PLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: من نمی‌خواهم مذاکرات دیروز را به‌عنوان یک پیشرفت بزرگ توصیف کنم، اما در عین حال فکر می‌کنم مهم بود که دست‌کم یک گفت‌وگو صورت گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148997" target="_blank">📅 19:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148996">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpeo331KSQ9QrN80l3b8rr94uP0SwuOYeJ2g76AnUpKn1WArkhXTv6Cj670FgZnA-F68ox60rst2IMsz6mQE9BdCQQtFvFEdR6lQit4X6vx3y3J_pkLfCSn6CE6GAKYU7oe5FjNjyjBfvzHoDdD7bfSUnKO_aPxtkFcx9zYIyuxucmW-jPtxi3HG0cx-VkUm0E0OU00BKkaldrxDt_unJXVsddYGEDMwCBRNu0V89GAa81_gWFZ6I1nidp1-llAgrE4TgFXPeg_aamwDOt3AX9elPW-lms_MVsZxGiGAP3xfz1B_cENQfAkQVd9DDBhJbd7IW5pdkf4Fy-lQqgUJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شروط ایران اعلام شد
🔴
سخنگوی وزارت خارجه: توقف اقدامات تجاوزکارانه آمریکا از جمله محاصره دریایی، تروریسم اقتصادی،
خاتمه جنگ در همه جبهه‌ها، آزادی اموال مسدودشده یا محدودشده ایران، پذیرش مسیر ایمن کشتیرانی به شیوه تفاهم شده بین دو دولت ساحلی و ....
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/148996" target="_blank">📅 19:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148995">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797313ae14.mp4?token=t9gA4DR9cRUxUhInijvCDhlx4UgIxzh29c8Reb_QcTTSSWgrKSR6o5JQTM4M4BeazFiOiReznRIOiANhZs0cv-gGx8PBGaaX8CGyk2Q9EvhTnOkavfuwuRaJxxaNmLhGKaBcEvrgE8z6R3T9vMNeA0niekJYmE8eRGMhSLD80Vzh3DzMfEzcdzPT_Jzok2wb2G1LDHHRtaY_AhtqxAUIBpV-7Mjc95_TNZQ13h_wRFCoQvDnwXHcsQ6HHP5R_u_9xHHAQOy4yX5KdUmiLpAHl0Vwxbf9bcYbA-spWzJ6uS6Thz5pfADnf3eqJAFLdLiXJRc2OtfAcKBxKcaoTgr4S6s5KzkTC9lRAgQiAUYPb4DsvUleQp7GufZcIj0GtF2mjtFnUOa2vVRWyL6T2numvf8ofbSJMStjS3HoS5gnorU7jdv0p6lot0sYuIsi0mz71-ZUXQCuuIY1C89FEbTbZkmac5dfkD6Nv7YyUQUZMCsP2hJiLuCto4RE5Mj9hZkVmH2nWtpWtGiSmq0a-vJbeZfCQym84fdMD9oqLWkyfLOvTag5avaf6C8aGUmAvi2SIv6Fw3qhILgm1oH_VXgScsZJRPSevMmjWQX2r7bVnsSLCvti04jeVQVdLwAhcSNon8NvdwJTpBfyrLQ9y-Qun21nDB9PFralCisUx1g_Yiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797313ae14.mp4?token=t9gA4DR9cRUxUhInijvCDhlx4UgIxzh29c8Reb_QcTTSSWgrKSR6o5JQTM4M4BeazFiOiReznRIOiANhZs0cv-gGx8PBGaaX8CGyk2Q9EvhTnOkavfuwuRaJxxaNmLhGKaBcEvrgE8z6R3T9vMNeA0niekJYmE8eRGMhSLD80Vzh3DzMfEzcdzPT_Jzok2wb2G1LDHHRtaY_AhtqxAUIBpV-7Mjc95_TNZQ13h_wRFCoQvDnwXHcsQ6HHP5R_u_9xHHAQOy4yX5KdUmiLpAHl0Vwxbf9bcYbA-spWzJ6uS6Thz5pfADnf3eqJAFLdLiXJRc2OtfAcKBxKcaoTgr4S6s5KzkTC9lRAgQiAUYPb4DsvUleQp7GufZcIj0GtF2mjtFnUOa2vVRWyL6T2numvf8ofbSJMStjS3HoS5gnorU7jdv0p6lot0sYuIsi0mz71-ZUXQCuuIY1C89FEbTbZkmac5dfkD6Nv7YyUQUZMCsP2hJiLuCto4RE5Mj9hZkVmH2nWtpWtGiSmq0a-vJbeZfCQym84fdMD9oqLWkyfLOvTag5avaf6C8aGUmAvi2SIv6Fw3qhILgm1oH_VXgScsZJRPSevMmjWQX2r7bVnsSLCvti04jeVQVdLwAhcSNon8NvdwJTpBfyrLQ9y-Qun21nDB9PFralCisUx1g_Yiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، درباره ایران: ایرانی‌ها و نیابت‌های آن‌ها به تأسیسات دیپلماتیک حمله کردند — بی‌سابقه است. آن‌ها عمداً به سفارت ما در کویت بمباران کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/148995" target="_blank">📅 19:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198effcfec.mp4?token=rkBdIApDDznQ6WgIqWDRQsO6sYBUACJ95WlAKSDyg9bI6fMTdqZIQ1A9kP-y5tf2FGbB7x9xzAyUf9pz5Spx11PvTXg5_lLaHkbzIfpeMwDGEbOSMbdJf-1bSeGuEKl4xH9aZ8JEr2AXXfdunUG4pFU8guBsO-chMhSvprYsJPkdJETVp34yzuuY4izkQy0XwABtOFhgV-K6tm2KGDByhVXCGLpZ1fe7G7SMaKHgkW3DtqcGqUhLx18KZkG6WZSqfOCp_rD5J99hTQTGEkkxf5Aojt3Yit9oZaJHXs8aLZgp3CIz7SLYWigsfIzNPpmOFDOpY9opMMXy7osGEM4HMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198effcfec.mp4?token=rkBdIApDDznQ6WgIqWDRQsO6sYBUACJ95WlAKSDyg9bI6fMTdqZIQ1A9kP-y5tf2FGbB7x9xzAyUf9pz5Spx11PvTXg5_lLaHkbzIfpeMwDGEbOSMbdJf-1bSeGuEKl4xH9aZ8JEr2AXXfdunUG4pFU8guBsO-chMhSvprYsJPkdJETVp34yzuuY4izkQy0XwABtOFhgV-K6tm2KGDByhVXCGLpZ1fe7G7SMaKHgkW3DtqcGqUhLx18KZkG6WZSqfOCp_rD5J99hTQTGEkkxf5Aojt3Yit9oZaJHXs8aLZgp3CIz7SLYWigsfIzNPpmOFDOpY9opMMXy7osGEM4HMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: سورپرایزهایی برای سخنرانی‌ام در سازمان ملل دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/148994" target="_blank">📅 19:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148992">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام ایرانی:
بازگشایی تنگه هرمز و رفع محاصره آمریکا طی مذاکرات غیرمستقیم روز گذشته با آمریکا مورد بحث و بررسی قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148992" target="_blank">📅 19:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148991">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59943f167f.mp4?token=rE9RATC-_C6JkzUh4FXoQdXRvrq1OCRBmObj1Di92QFVLuhIeSXst3Hfz8Q9EYilqSTjfyoQM9iPrDynRG6PNQCCiB1uKL-uU6BWqzSKoOJmQDkjv-NCtFhOFkbJeVZEFRCazdaQmijYU9BK4Xzc0oP1wYXTAe6GL6GQxyH_JPnwksNZsIlJkJN63SUROADIEZhJNxN5gI2gG6x3CayBhQBP095M7vQXuY1nuktu4U9xBEmLVwKafExQoDNmHwCWJL8YGr8Ezn44VEFjUhRLESRBJWx1QK6O0ni2QifXJp2Z4tyUlC79g0zVVg4dMTH2Z_pljKboZOfdMH4izn2dJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59943f167f.mp4?token=rE9RATC-_C6JkzUh4FXoQdXRvrq1OCRBmObj1Di92QFVLuhIeSXst3Hfz8Q9EYilqSTjfyoQM9iPrDynRG6PNQCCiB1uKL-uU6BWqzSKoOJmQDkjv-NCtFhOFkbJeVZEFRCazdaQmijYU9BK4Xzc0oP1wYXTAe6GL6GQxyH_JPnwksNZsIlJkJN63SUROADIEZhJNxN5gI2gG6x3CayBhQBP095M7vQXuY1nuktu4U9xBEmLVwKafExQoDNmHwCWJL8YGr8Ezn44VEFjUhRLESRBJWx1QK6O0ni2QifXJp2Z4tyUlC79g0zVVg4dMTH2Z_pljKboZOfdMH4izn2dJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب پزشکیان تو سخنرانی سازمان ملل به جای سانتری‌فیوژ، گفت سانتیری فوژ
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148991" target="_blank">📅 18:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148990">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUo3SkR_n4jybaidqXZWy_pTAxloTcNtx25zgv3pUFn5hEOFeoi-ERxs3TFxihyMi1wbl0sd3ZV7VfvjEF11SObnfs4Wl3mC2Nik9epn2zv7SfZj_pTQh1mE5b7F7Ojr5qGIHUwUIwj0rHlylG7ASxfEQy2nTVsTTq0tawbMg8l_Qm42qnbbLgCkvL47gySj6XW75NphuKPDsBfxO-XpRQw9QZwXG0OXPo7ZFD2fI1GC_Ki5vWHq9KK29GoPWvt9P5G9DAXanjg3GKlCQXmdlIj259OltowV3chX_M_sl6kVDcijzSWwC8CYVK6o1Nmrfgxvg9f1cWhfoYRkFPfexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز جلوی سازمان ملل، سلطنت طلبان و مجاهدین درگیر شدن و این شاهکار خلق شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148990" target="_blank">📅 18:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148989">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏
👈
مارکو روبیو:
جلسه دیگری با ایرانی‌ها امشب برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148989" target="_blank">📅 18:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148988">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f769da6b36.mp4?token=QImMGZbCX5TWUxa58d0IJl6SIsJZKAdGGkoUip5dyX8cKyKWKh8adf7yQY6oKWKl5lZvsSVmLbRTuLA6EXv-LFX6xI75qYvKtDkMmpf2Q6pJhYsRKmkeQ0fBxasYpP1LaMBNgz5c-nUdIT9nsanO4r9GVYakCNd_HO5UilW4bGfWPOMEsEtK1bJajgtxE-hHzP6uCugWt1iqaGU6wvbWhPmq-QS4b5rDsLpr0zhu9DumTyAmGDjzZQpUR7TesJQVA8XlyrQGz8FJhOrhbxJkYiWZ_Gp08mYZIP_7Hn08y3EipH5hSqTCFCRLxpfN8p0UXMdsHyrFip28O1j8-VhLpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f769da6b36.mp4?token=QImMGZbCX5TWUxa58d0IJl6SIsJZKAdGGkoUip5dyX8cKyKWKh8adf7yQY6oKWKl5lZvsSVmLbRTuLA6EXv-LFX6xI75qYvKtDkMmpf2Q6pJhYsRKmkeQ0fBxasYpP1LaMBNgz5c-nUdIT9nsanO4r9GVYakCNd_HO5UilW4bGfWPOMEsEtK1bJajgtxE-hHzP6uCugWt1iqaGU6wvbWhPmq-QS4b5rDsLpr0zhu9DumTyAmGDjzZQpUR7TesJQVA8XlyrQGz8FJhOrhbxJkYiWZ_Gp08mYZIP_7Hn08y3EipH5hSqTCFCRLxpfN8p0UXMdsHyrFip28O1j8-VhLpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگاران ایران اینترنشنال در بیرون مقر سازمان ملل وایسادن تا پزشکیان بیاد بیرون
و ازش سوال کردن
:
🔴
خبرنگار : چرا اعدام هارو متوقف نمیکنید آقای پزشکیان؟
🔴
چرا کشتار مردم رو متوقف نمیکنید
🔴
دست شما هم به خون آلوده شده آقای پزشکیان
🔴
پزشکیانم هیچ کدومو جواب نداد  سرشو انداخت پایین راشو کشید رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/148988" target="_blank">📅 18:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148987">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953c03a875.mp4?token=O71WtrRhT3ZQH30GM3wWn7oxveSferQObT7pGbHzqJ05IOLKAujjDDRAKRegOuPG2Wiw6SXcXHn9ee_cNLs9FmYluFlWVA92LFbw8ysUSf7ugUDshZy4677VNCp6-z3FTBwtW_u9IPyq1_-rSXo9PeV5qSTrKagdeucspg7wwVVm-1g8TajLOC4HcQ2BAQ1x9Bs38oVbRtq_BVwFYDDQ3_SYleMBaWgpWtlMkaUD55aVZw-ClhHpC43M2FmSod7B7vkeoRmiFRvglve67MQB8pgNSXIeLalddG4g1w_VFCINDXZcQOrZYF6w7LhnujoI-R_eEZHQONw4HZ25Wm1Gnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953c03a875.mp4?token=O71WtrRhT3ZQH30GM3wWn7oxveSferQObT7pGbHzqJ05IOLKAujjDDRAKRegOuPG2Wiw6SXcXHn9ee_cNLs9FmYluFlWVA92LFbw8ysUSf7ugUDshZy4677VNCp6-z3FTBwtW_u9IPyq1_-rSXo9PeV5qSTrKagdeucspg7wwVVm-1g8TajLOC4HcQ2BAQ1x9Bs38oVbRtq_BVwFYDDQ3_SYleMBaWgpWtlMkaUD55aVZw-ClhHpC43M2FmSod7B7vkeoRmiFRvglve67MQB8pgNSXIeLalddG4g1w_VFCINDXZcQOrZYF6w7LhnujoI-R_eEZHQONw4HZ25Wm1Gnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری آمریکایی: تعحب میکنم! ترامپ جمهوری اسلامی رو تهدید به نابودی میکنه وکلی بد و بیراه میگه اما نماینده ایران خیلی ریلکس نشسته و گوش میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148987" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148986">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRvB19FeRjmM8EuGKbXXwaLwqsjmuvjnxDVBNuvu6_c8r4or9N40wDt9bapR_XYPVxGl_pQsJ9KVW2QEJHRgTWkVqVXvc7N4gGpToz-lQ_rEiZ0zjfvHtMRe6Q1mtb3VV94g3VZWbOWgsgEsBn0H7ia8hXw_WXAdBNi7iF3VCT0fXu3pxPCFALpSjs1PJBQwvXZrBoUp9aVy3nY6sVpJ_vnXMQvt_TizMF97cPZ-CYNzr2-WT1XwxCwJmSlJX3eqVK8HCF192szsX2oNRwvf3zgttewj0lPY1cMeNAykwuT4Clb1Yd7ytln9E9HjgGMbVzcqnuo7TELqRt8E6rBxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از مخاطبین سخنرانی پزشکیان در سازمان ملل
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148986" target="_blank">📅 18:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148985">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: رسیدن به توافق با ایران نیازمند کار مداوم در یک بازه زمانی طولانی است
🔴
ما به دفاع از تنگه‌های دریایی و باز نگه داشتن آنها ادامه خواهیم داد.
🔴
ترامپ گزینه‌های متعددی از جمله گزینه نظامی در اختیار دارد.
🔴
گذرگاه جنوبی تنگه هرمز باز است.
🔴
ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ قادر به انجام اقدامی علیه آن نخواهد بود.
🔴
نیروهای نیابتی ایران در منطقه، امنیت و حاکمیت کشورهای آن را تهدید می‌کنند.
🔴
ما همیشه مطابق با منافع ملی خود عمل خواهیم کرد و نظم بین‌المللی را بالاتر از منافع خود قرار نخواهیم داد.
🔴
با کشورهای خلیج فارس در مورد لزوم باز نگه داشتن تنگه‌ها و مصون ماندن از هرگونه حمله، اتفاق نظر وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148985" target="_blank">📅 18:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148984">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvGd_js5lGbDQ0M5TFp9Nvw12xHKAg9ADwUvNGERTy4MH-JTVbMrqzQD3wgcTzGGc5A2JpTcfNaT3aFPtqbtqHjzjmTsViTevU85BwlOdVQeLcmPXi6PfBEx0PB3Bf70O6gmNi54guODOT625fcZmfQHUlqKXHXwlSovQZsDdoLhMClgDL6_vTsCLQ0Dx8ZlL0wGm13nRmEP-INQBFRWfgmMgSXVYSVVSb5aH2oQ-Zmu0AVeo7jlAZI-CH8fVV0Tc1-eO3FoEGfTHeQAFd-m9dG98BM6Z0_5dw3L_xT5irwQIqtxTWa-71QwHINi30JiYGBIpOzNXovur0zTZURn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صف‌آرایی علیه وزیر اقتصاد در سازمان بورس
معاون اول پشت تحرکات در سازمان بورس است؟
🔴
با نزدیک شدن به پایان دوره ریاست حجت‌الله صیدی در سازمان بورس، تلاش‌ها برای حفظ او و مقابله با تغییرات مدیریتی، به شکل‌های مختلف شدت گرفته است؛ از مخالفت با برخی تصمیمات وزیر اقتصاد، علی مدنی‌زاده، تا تلاش برای بی‌اعتبار کردن برخی مدیران منصوب او در سازمان بورس.
🔴
در این میان، ادعاهایی درباره حمایت معاون اول رئیس‌جمهور، محمدرضا عارف، از برخی این اقدامات مطرح شده است؛ موضوعی که در صورت صحت، می‌تواند نشانه شکل‌گیری اختلافی جدی میان برخی جریان‌های مدیریتی اقتصادی دولت باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148984" target="_blank">📅 18:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148983">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخن پایانی پزشکیان: ما آماده گفتگو هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/148983" target="_blank">📅 17:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148982">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پزشکیان خطاب به کشور های منطقه:
یا امنیت را با هم می سازیم یا ناامنی را با هم تحمل می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148982" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148981">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
👈
پزشکیان: چرا برای فلسطین کاری نمیکنید؟ مگه ظلم رو نمیبینید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148981" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148980">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پزشکیان: بمب اتم و سایر سلاح های کشتار جمعی در دست اسراییل است اما از ایران می خواهند که بازرسی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148980" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148979">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پزشکیان: اسرائیل به هر کشوری که دلش می‌خواهد حمله می‌کند
🔴
عاملان ناآرامی اسرائیل و آمریکا هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148979" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148978">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پزشکیان: حمله به زیر ساخت های غیر نظامی خلاف قواعد بین المللی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148978" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سالن چه خالیه
😐</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148977" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=oeQXCPg-6hDnzJVS3B6YSm0p0ofMLcpX-6pDMUkZVvEccOI3eB_cAUcsEWQ1Aa8hA1M3PYDNZZmruLkllk2PSmQDaFgGET_G4Pw0jzel9C_tp3Xl7_Ndil7Yu40OAf_oJP0BAoVzL06o5Pf2DfaRPUZJpFnYOQ4guGv79rIM1L4rMWIn1qbqYLvDpJclwz4KcNZ5Ac5CmQyg1bTSgrluPxI_AJk6dEh83lTwiNIjdCeiWsrohqDuMi1inBIRqeni8XE38VV83jKgMrcu9n13ivkIEjsqH7dy6-FM-eTi9Cs7NopPSkLqazj_SeQOQtU-Zd1pmHZZWeHg5uPq-xTL7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=oeQXCPg-6hDnzJVS3B6YSm0p0ofMLcpX-6pDMUkZVvEccOI3eB_cAUcsEWQ1Aa8hA1M3PYDNZZmruLkllk2PSmQDaFgGET_G4Pw0jzel9C_tp3Xl7_Ndil7Yu40OAf_oJP0BAoVzL06o5Pf2DfaRPUZJpFnYOQ4guGv79rIM1L4rMWIn1qbqYLvDpJclwz4KcNZ5Ac5CmQyg1bTSgrluPxI_AJk6dEh83lTwiNIjdCeiWsrohqDuMi1inBIRqeni8XE38VV83jKgMrcu9n13ivkIEjsqH7dy6-FM-eTi9Cs7NopPSkLqazj_SeQOQtU-Zd1pmHZZWeHg5uPq-xTL7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: اسرائیل در شهرها و استان‌ها دست به ترور می‌زند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148976" target="_blank">📅 17:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148975">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان: والله دنبال سلاح اتمی نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/148975" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148974">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پزشکیان: ایران نمی‌پذیرد دانش هسته‌ای دانش انحصاری چند کشور باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148974" target="_blank">📅 17:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148973">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پزشکیان: قدرت نظامی ما برای دفاع است و از هیچکس درباره آن اجازه نخواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/148973" target="_blank">📅 17:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148972">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پزشکیان: دویست سال است که به هیچ کشوری حمله نکرده‌ایم و فقط در حال دفاع از خود هستیم؛ حال شما به ما می‌گویید تروریست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/148972" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148971">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d23473339.mp4?token=Q2JDu9zZzbkkaLYbYDwok8ouO1i1P_Oxlhxjmt_CE-w9R-h-VH_TLXjZPVoi9aD6FVrjYW4ZOBLDh2YABr8GrfJ0DN6sO9nbNS02IGeVBHyU5F1SbHY1g-1X-0ME9ZERSnonjqihKR_CF2z6SQq6iEZthwdbyfe-0O5s19Bl6OlZiK_NCqnzZN18NElzxENqFAsUTVsZvFg6zSQ0GpEfZgrdIN6Ktm4MfPu4akZYLyKJZfLvq3wDLP3FcqsHRAseB0R_sg9EgZyhSjPBzT4qdEysC-nhbiJ3A6PUkkQijZM6ZHs9qh1I4w8mzG6b-pmiy0EkMD6UogYgs448Ln-UhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d23473339.mp4?token=Q2JDu9zZzbkkaLYbYDwok8ouO1i1P_Oxlhxjmt_CE-w9R-h-VH_TLXjZPVoi9aD6FVrjYW4ZOBLDh2YABr8GrfJ0DN6sO9nbNS02IGeVBHyU5F1SbHY1g-1X-0ME9ZERSnonjqihKR_CF2z6SQq6iEZthwdbyfe-0O5s19Bl6OlZiK_NCqnzZN18NElzxENqFAsUTVsZvFg6zSQ0GpEfZgrdIN6Ktm4MfPu4akZYLyKJZfLvq3wDLP3FcqsHRAseB0R_sg9EgZyhSjPBzT4qdEysC-nhbiJ3A6PUkkQijZM6ZHs9qh1I4w8mzG6b-pmiy0EkMD6UogYgs448Ln-UhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیئت نمایندگی آمریکا در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخن می‌گفت، مجمع را ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/148971" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148970">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv2ijbW6TWDHHU8XWSq6vNLu5PKuhW1asn6qdJAKqVWfiDXTF0tbMpmceTudVo-mWlUcxVT9WHOtxlEZ_zQndetDCtGqb1Odj7ntGRd1t70sQpDPNeFQgHABH-QXeEHzC4r52-rtSwm3jZqCmTy12SMujbgLQerCCtuX3IJpJlXnm72QkTmdwMxo2G2agB7Mpr2I-Y82NTQXQme-rWDH3Dit1giFAUQM5xw9ToSpU8p5nQ6AgdfMVGbez1r1IZ8pMpzwqrZZ3jE7YjuGX4ik5Xha35MLw0Q9ihGho58mB9xvHUP2SIE2HT4mwiGMsgrwFyp51qPqnvIJJJSfVx4Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر کودکان بیگناه مدرسه میناب در دستان پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148970" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148969">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=R0Kb8ivX3jTN9Q4r4gO_uOQOeaBqTm3Bw-RyaDOpIgnULqAKwniGkLxQWC86LidWWDCkYiC81-xAuYeRkmjqchr3ugee4yY15wRQm82rlhFTdYvjPDmmItDPFawyMJCB9z8O_g2R5EXeXP7zGcTdRe3tX_IpdM5sjgwL5soOSFabs3-ORe4cEo_7Jr3TwyQSkIrHMLle-pq5Z_PNT3F-Qcm1ZwL2bESLBEqJ8KqNYwKOGybP4KYIbxBkRl26-1XpEv_Uu82cFfRnZPN02Iav7C1owfBwlVEKZeqtxVn_mSsX3FJOQGq1oYHXpoopysbLmD4INEXo5TDVFqcj_O7c2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=R0Kb8ivX3jTN9Q4r4gO_uOQOeaBqTm3Bw-RyaDOpIgnULqAKwniGkLxQWC86LidWWDCkYiC81-xAuYeRkmjqchr3ugee4yY15wRQm82rlhFTdYvjPDmmItDPFawyMJCB9z8O_g2R5EXeXP7zGcTdRe3tX_IpdM5sjgwL5soOSFabs3-ORe4cEo_7Jr3TwyQSkIrHMLle-pq5Z_PNT3F-Qcm1ZwL2bESLBEqJ8KqNYwKOGybP4KYIbxBkRl26-1XpEv_Uu82cFfRnZPN02Iav7C1owfBwlVEKZeqtxVn_mSsX3FJOQGq1oYHXpoopysbLmD4INEXo5TDVFqcj_O7c2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نشان دادن تصویر علی خامنه‌ای توسط پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/148969" target="_blank">📅 17:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148968">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
پزشکیان در سازمان ملل:
ما قربانی تروریسم هستیم من از ایرانی می‌آیم که رهبر ما را بدون هیچ دلیلی ترور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/148968" target="_blank">📅 17:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148967">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrH4EOasXBCOoCaQNfckWMrtLdEh2YxsM7GCUWWX7QvrUotgIWLL7xASXVcmt1jZCsIkjE1WOYpK8AOoCPDuvLiyqE1YtnnMAzXskJ_Za8aeatWRaMgK-_6qhEHYSM1ZcOXbePAkP-qTsaggooa4kmzy678fe5WDKAuo7dLF5nYvzCNA-7RGqXPS8616qCL9RDDbi8ihZbxPwCay-eFaSOSdFpeBgIHqfvBZXyzZ9n9CVbborsUdq-H_YMkq1n8kdOuQe1IluI4qR_RHowpo1Zsy5QoBm2f6N6GwcDU5JVwaxv951SDJd9WJFBCl9-UkDtcbCajXafsiBxFlaHZFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیس پزشکیان توی سازمان ملل قبل سخنرانیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/148967" target="_blank">📅 17:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148966">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKQDhqUxfHH_9L-9yBhJArYCwlPuGbojlFDDFBCcBx0O7AkjIq7FJk05NenEbmekUCdMJklnvQPQBVHBjCm38F4V2ubDCeu3cLbrThMCed-4uASmyGcm8qRFeLD_rm56OQzLVJO8Z00Qr8U2rVLDwe1AZaXS54bDd8qDU18cSTzOcdUfeHHjZ96DxkWAqlgpbqj_OPNbNIJ8fi67GmEsNTOUZkZ4P67IyKLfSchSOZziZUUceIUQBjzzp5hIika7yDjrcLJx2SKWCHCsCJ377AU9QPXpHZ3O6Kgf8dosBzTYHtub0UQxK3MBWlsoU0H213FKdV85k5fUPoUktZHOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی:
ممکن است ترامپ به کوهی در ایران یا سایت‌های هسته‌ای ما حمله کند؛ ما طرح پاسخ را آماده کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/148966" target="_blank">📅 17:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148965">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پزشکیان وارد سازمان ملل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148965" target="_blank">📅 17:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148964">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هشدار فیلدمارشال رضایی به ترامپ: وقت را تلف نکن و شروط ما را بپذیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/148964" target="_blank">📅 17:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148963">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d21bb84f.mp4?token=CXV2xQCsN9SWdM7kJX58VMdVt8rMkRdi01-OR8VvMa3DoMNglfpLmqKqlH0aalrHIXruK9pgTACLkUpc6FGv-MsyweWqYyKXMD9ppI0q_mPwrh59RjK4HyFvPavVRqmi6AyPrN0GMRomdt-ElLMW16itwQILQjteI9Hn0DiX5WpOVGapheLw4x74BwqiWB5czpFuZwqCAxKp3UG3sT4Vg3lmaKydpY-80TGByM1RkTQ44FmWLUM-E1JQ1rVbhLQajVo4-h5uZBEt-1C5xGNv0bAAA9LKaYu0B0q7tlJL5QLI_QBU2zFApy21JvmpklVtuKNKFP8MIMtPiTml9Ak6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d21bb84f.mp4?token=CXV2xQCsN9SWdM7kJX58VMdVt8rMkRdi01-OR8VvMa3DoMNglfpLmqKqlH0aalrHIXruK9pgTACLkUpc6FGv-MsyweWqYyKXMD9ppI0q_mPwrh59RjK4HyFvPavVRqmi6AyPrN0GMRomdt-ElLMW16itwQILQjteI9Hn0DiX5WpOVGapheLw4x74BwqiWB5czpFuZwqCAxKp3UG3sT4Vg3lmaKydpY-80TGByM1RkTQ44FmWLUM-E1JQ1rVbhLQajVo4-h5uZBEt-1C5xGNv0bAAA9LKaYu0B0q7tlJL5QLI_QBU2zFApy21JvmpklVtuKNKFP8MIMtPiTml9Ak6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دانیال عیوضی از بازداشتی های دی ماه که مجروح شده و از طریق ترکیه خودشو به فرانسه و سپس آمریکا رسوند تو صحن سازمان ملل در مقابل نماینده های جمهوری اسلامی بدین شکل سخنرانی کرد : تو دی ماه مردم خیابون‌هارو از جمعیت پر کرده بودن، اما با گلوله به مردم حمله کردن، ده‌ها هزار نفر به قتل رسیدن، مردم ایران هیچ مشکلی با بقیه کشورها و آمریکا و اسرائیل ندارن، ولی جمهوری اسلامی ایرانیارو بدبخت کرده، به محض اینکه دانیال اسم رضا پهلوی رو به عنوان رهبر دوران گذار آورد، هیئت ایرانی اعتراض کرد که خلاف قوانین جلسه هست، اما رئیس جلسه گفت حرفای دانیال هیچ مشکلی نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/148963" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148962">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
محسن رضایی: در جلسه مشترک با رئیس جمهور قرار شد آقای عراقچی طی سفر به نیویورک شروط ایران را به واسطه‌ها ابلاغ کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/148962" target="_blank">📅 17:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148961">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ادعای محسن رضایی: برای اولین بار موشک ضدناوشکن روی ناوهواپیمابر جورج واشنگتن منفجر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148961" target="_blank">📅 17:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148960">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ادعای محسن رضایی: برای اولین بار موشک ضدناوشکن روی ناوهواپیمابر جورج واشنگتن منفجر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/148960" target="_blank">📅 17:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148959">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فیلد مارشال رضایی: ترامپ ایران را به قدرت چهارم جهان تبدیل کرد
🔴
پ.ن: گویا فیلد مارشال از وضع مردم بیخبره
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/148959" target="_blank">📅 17:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148958">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ترامپ و نتانیاهو جان سالم به در نخواهند برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/148958" target="_blank">📅 17:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148957">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ترامپ و نتانیاهو جان سالم به در نخواهند برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/148957" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148956">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYl4BTcYK1a3Fv3d4fVgG-w5XXaJfHm2ROtMGbsv0Nkjx-sCoBpwAcvgqVgi77D-DVqtp5OXwNGcMy_ZA8rTOFBMm0niQaw13LyFymyA57NQDbDdsTBtxKZtN_rTGxqWu8zFboh-7TjJAQJtVxf6CGkwOxZS627Qx-g_9ilg4Oi_I5lrnJ8tKtjT5TwJpFn1wqNFUUNAmuhv-lLRMg3-5lcglFGAFrxbDgRHQkpymFS8WA4XOWZguh8lruELTkU5vYfXb_f_w_lB2pRyuYwwbI5hr1Qwh_Q1GTrOhv7l6p_GgS_4re0An52cUSjMelwfKNsq41sIh2eY_INMAlle5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای اطلاع‌رسانی دولت:
دیدار عراقچی با ویتکاف مجوز دارد
🔴
هیات ایرانی با هماهنگی نهادهای مسئول و در سازوکارهای نهادی کشور به نیویورک رفته
🔴
همه برنامه ها در چارچوب تصمیمات اتخاذ شده در تهران، صورت می گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148956" target="_blank">📅 16:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148955">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peqB4wwA0_BAK3QJGB4n4omLNKh2GRxgwe1K39lcPF_h4JwiwMl_pOVTCELUkJ2McIQAP9bRKNlf4mR11zrYI6ZfTS-ge1ZgLQtWl0m9KR4hXE4gY31X-qxNX-JPNgQaXx6ERUAUynVxhmtu1lt9a3nnCFRPPYIn8XX0ZtPVkGaTlHUso_i7f22v3H0cKaeNT3unl07Uil4MtRusQBETYFbRPmW1flaMRScKCbttPdSzBp0dRwkIsXcVbdX9oeHmZUYi9HFImb4uD2Zw62_17dZyhq3itO_Fgkyyu2qxnuxS3mWfK6iOBvTPYw3QyhsLoZCvAIBx34QagisNpWzIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی نفت برنت از ۱۰۰ دلار عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148955" target="_blank">📅 16:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G11Iqu37RrL0KwbIFde8Flt-E7UHwawKpC4tA8Gu-6gEdJd2B6RjpI8CA8ZhuXm7EN7s_5pHqPuIYvCDELnWmUospUgIXzRwZehnnhUIYEVlw5FzVkjvPySKQqrbPrQOykVfW1hpIVH4cuziJRlC8TivWqfVey9_n38bT0pwVeSO5llFqYJ5G7bZIKirvK6Vb1RpDizi07nmNledc297hzRqZIcF6Mt9taXG5auL4isM-jkUhJfdsOWenFKrxNtBsx2wIynLU-f6vNJjnWLLvOfCjGC7VhqI57vNWXPHXJFKTHG8jwLWdmh4DDbpy3gA8U6ysCCdNYmA4fqXOjQmcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ade90416.mp4?token=LaC-iFb164rGtbOWpQtsQAz_BMlEHFmtDTaUu4o5gDTpVTKXHkHMcM7xUJ4NLrrDCJ59cq2v043mpdQYZd43MWUq_iJcehKqL2tmwpQDx6arRgWts9rAOcrIxwatNvsKS2StZ75m9fjNbfXhwUME93CPXmKxwhOXEkkiZOl3QjcMWh2AGQh7ZhWqoW_ov6z45o1U5kO8OmZfbmNWf4toVXJT_aJ4y9NmAEuHo8ly96YLXPVQW_Y--4W1GH1IYvZ_lrZ6avxogaTdqFc0dJGqAcSoOGNVdL5OcpAqqRrnjuVolli2f4FRi35sfWYNLqRlAoyxrmrqIwMsO_yG2TPCqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ade90416.mp4?token=LaC-iFb164rGtbOWpQtsQAz_BMlEHFmtDTaUu4o5gDTpVTKXHkHMcM7xUJ4NLrrDCJ59cq2v043mpdQYZd43MWUq_iJcehKqL2tmwpQDx6arRgWts9rAOcrIxwatNvsKS2StZ75m9fjNbfXhwUME93CPXmKxwhOXEkkiZOl3QjcMWh2AGQh7ZhWqoW_ov6z45o1U5kO8OmZfbmNWf4toVXJT_aJ4y9NmAEuHo8ly96YLXPVQW_Y--4W1GH1IYvZ_lrZ6avxogaTdqFc0dJGqAcSoOGNVdL5OcpAqqRrnjuVolli2f4FRi35sfWYNLqRlAoyxrmrqIwMsO_yG2TPCqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک هواپیمای آموزشی مدل "هاوک تی۲" متعلق به نیروی هوایی سلطنتی بریتانیا، امروز اندکی پس از برخاستن از پایگاه هوایی "وللی" در جزیره انگلسی، سقوط کرد.
🔴
هر دو خلبان با موفقیت از هواپیما خارج شدند و جان سالم به در بردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148953" target="_blank">📅 16:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148952" target="_blank">📅 16:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148951">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
طالبان و پاکستان درگیر شدند
🔴
روزنامۀ ۸صبح افغانستان از درگیری طالبان و نیروهای پاکستانی در مرز دو کشور در ولایت پکتیا خبر داد.
🔴
این درگیری چند ساعته ادامه داشت و به‌گفتۀ منابع، شماری از گلوله‌های خمپاره به خانه‌های مردم اصابت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148951" target="_blank">📅 16:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148950">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-kgqrjrBRmkdehNnzFl2nNoM7DO1FyFQUn0pZMtQi7dBbMGmkTZ0Tg2xVbW97gjEa4lD74MH2DEylytpcQv5M5zZaUhGXcp0c-6oyWBX7YMw0ehpDPpg9k-PNiHErCaD9FWmt2dU9UEqtQcAbg0VXEJ14sifWALEpxqffanOlVa0mFIr75SOmieHKlFgdY4fD2Y-7OZ_Ex-CfMTAAK86ykyr-uKSlMpaIBiGype4JjACBtaVYkzrkRnvrwPjRGJWi3g9qKQ_aLDWTx8p8QaX7R_xjleA0Yfio2AEbdgKcptHD3G8_76O_udCaByWrDym8vY1kfRAAPd3FHv4yogQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید اسرائیل به فارسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/148950" target="_blank">📅 16:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6Jr3LPETeYApytZDxedLKFTbXJeTBqhf234tC_X2ntfPiy8tdg1EfJqnl5f9NdiNVRtpJgiUAdmMfG8X2H7_lPNVJBQIXvjkHUtiQ1_lNOIeAhiHcGYUdUAUIvDlZA_xFWTgk1sf3VVMV1JTUV9qa5CuUOZibPI3vu8U6HYCFRzVL6qgGOh3qSpTaC9iAOTC_-msIyrk-LYnaHz1wjQIkooNBQ69zJ4TEaxkb-IU3sJkYrMP2GUDJqKULf8TscsRHrduQ5seGjKXgluXy-P5OfQGhxiAvuqnJb0YFUmueqi9i2r1DoM7dkmDQD0dV4qDNcOzUQsoKXq9jNqXJ0LhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنج تانکر بزرگ حامل نفت خام در حال عبور از تنگه هرمز از طریق مسیر عمان مشاهده شدند و در نتیجه، هدف قرار گرفتن این کشتی‌ها منجر به نشت نفت در آب‌ها شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/148949" target="_blank">📅 16:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148948">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کانال 13 اسرائیل: نتانیاهو صبح امروز یک جلسه امنیتی اضطراری سطح بالا با تمام دستگاه های امنیتی و نظامی در مورد ایران برگزار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/148948" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148947">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdfbf7d1d.mp4?token=kRtZqWy0-Zj2CcmxN658JurZmvvYMYTXQzhuy8ILY5TTjve5v0qxh5hccQNGa8aJbd2xY1_g0VeG8_aQxqSQ3vdhmo7QtvP0od3mlGwsNnoxtedrIITYpJqrKjKnVzE_zYzlugoKaEwAQ_2eBesctixlX9KWlsN8C3tkgjDH-CECRzx2X7phfq0Y0skgEQChuZRdhQrf7lEk5ZbY1xrVUQlcNunD9EZv72ai6Y_XeiikT4HGkipDzVJRaHz6uiFBSxlu0HbPBH0ZpFLXixoONlzMCvCNCFZJpdCuGORcOfLVD-b42rwozBrJXKU8tqc1KvTzW4eZ35WE5AnMS6ETC4u-8d8e7A_Rh6ucHmhTJ3nmUrOHLSYI-NVFTH3zdJMq9OT6r9VhBTGXwZ9sEcS8NobxQQ9foo1JY4nhMRupAndVP6SLs3BMkRtkT_wswT-EF4UJhI7vrNdhgp9moH68hL0dlfb675PG2ym4LQ5JtttihJPUP3VfNEL6-1eiASBxOKoCKYkca5bDjBGQ3B-sQZagN2IullVaq0odtIRTf96ByKca37NP29_4MZOUwj6k-2fXdS5ZQ3hOkc518b8d6XUMB_LHnXE66kiEipjyk4jlBt7HTkkaiuoOEriY0X-KF-l1G5zr-qxqs-rsg43yx7fuuRLsY9YIJTJi3BslFKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdfbf7d1d.mp4?token=kRtZqWy0-Zj2CcmxN658JurZmvvYMYTXQzhuy8ILY5TTjve5v0qxh5hccQNGa8aJbd2xY1_g0VeG8_aQxqSQ3vdhmo7QtvP0od3mlGwsNnoxtedrIITYpJqrKjKnVzE_zYzlugoKaEwAQ_2eBesctixlX9KWlsN8C3tkgjDH-CECRzx2X7phfq0Y0skgEQChuZRdhQrf7lEk5ZbY1xrVUQlcNunD9EZv72ai6Y_XeiikT4HGkipDzVJRaHz6uiFBSxlu0HbPBH0ZpFLXixoONlzMCvCNCFZJpdCuGORcOfLVD-b42rwozBrJXKU8tqc1KvTzW4eZ35WE5AnMS6ETC4u-8d8e7A_Rh6ucHmhTJ3nmUrOHLSYI-NVFTH3zdJMq9OT6r9VhBTGXwZ9sEcS8NobxQQ9foo1JY4nhMRupAndVP6SLs3BMkRtkT_wswT-EF4UJhI7vrNdhgp9moH68hL0dlfb675PG2ym4LQ5JtttihJPUP3VfNEL6-1eiASBxOKoCKYkca5bDjBGQ3B-sQZagN2IullVaq0odtIRTf96ByKca37NP29_4MZOUwj6k-2fXdS5ZQ3hOkc518b8d6XUMB_LHnXE66kiEipjyk4jlBt7HTkkaiuoOEriY0X-KF-l1G5zr-qxqs-rsg43yx7fuuRLsY9YIJTJi3BslFKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل، درباره هوش مصنوعی: من یک هدف را تعیین می‌کنم: در عرض پنج سال، ما به سومین کشور قدرتمند در زمینه هوش مصنوعی تبدیل خواهیم شد.
🔴
ایالات متحده و چین در این زمینه پیشرو هستند – کشورهایی کوچک نیستند – اما من می‌خواهم اسرائیل نیز به این جمع بپیوندد و با کمک خداوند، این اتفاق خواهد افتاد و ما به سومین قدرت در این حوزه تبدیل خواهیم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/148947" target="_blank">📅 16:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148946">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
عمان هم به تحریم هوایی علیه ایران پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/148946" target="_blank">📅 15:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148945">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
فارس : عراقچی اجازه دیدار با ویتکاف را نداشت و باید عذرخواهی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/148945" target="_blank">📅 15:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148944">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=gyALb3-B4ZCcVCxKAcR_GxD80JipaRscK7I8npl5ZEX8yvQwQ-sObFD1u4Saro9vskjL6y2PWa8It95L1FMF_Mwb75YOJI_AN-1WzgUAFXe_fXXhVIkiB4HGeuY11xgj_DGWT33XeKA2xwqVRZtkA3om6IE4S838aCMB0SzOfgRaKzN25jz4eJcS2eab_E31gR7rlP3O3mQPSCFFeEBatz8DvQfzsTtZRtKh9i8QAFZB3ZvCJoe9fu7MVeqg88NFYPQNdrUa9orlf0qNnMX8W5N5SX3bgCnc8CmwsmB-E3GVqNdYrB29dtZFja_YwmR0KB_GbZy_Gfjzc-geZwV56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=gyALb3-B4ZCcVCxKAcR_GxD80JipaRscK7I8npl5ZEX8yvQwQ-sObFD1u4Saro9vskjL6y2PWa8It95L1FMF_Mwb75YOJI_AN-1WzgUAFXe_fXXhVIkiB4HGeuY11xgj_DGWT33XeKA2xwqVRZtkA3om6IE4S838aCMB0SzOfgRaKzN25jz4eJcS2eab_E31gR7rlP3O3mQPSCFFeEBatz8DvQfzsTtZRtKh9i8QAFZB3ZvCJoe9fu7MVeqg88NFYPQNdrUa9orlf0qNnMX8W5N5SX3bgCnc8CmwsmB-E3GVqNdYrB29dtZFja_YwmR0KB_GbZy_Gfjzc-geZwV56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمان هم به تحریم هوایی علیه ایران پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148944" target="_blank">📅 15:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148943">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی بریتانیا: گزارشی درباره یک حادثه در داخل تنگه هرمز دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148943" target="_blank">📅 15:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148942">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">چطور برای آیفون 18تحریم نیستیم اما برای واردات دارو تحریمیم؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148942" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148941">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUkQG8r-oyJObgiEcmDwlPXGyADhrIDP1qOGheAARAWaWBq24cEWgYAaC5rLI1GvJMjmmtoicaerjwwiihEyy8LVpOC2pv-J2UVs4KSMhAa_JCjSBYCF0WoffonI4BvD5wNSrwwiimZKHbZwTGjk7M5smxXS08WFbHU6bBEFi-T5gOvAb0GjSirquKELv_hEuMZvwQmDBu-aD0b6KR6rF0pTThbeh5wWH-ITDdfomocb9_mDGMsX8P2tcMDDDPXgckyfCJcjnJviw-KH-pxvUVZS27chME2gHjhRN-IYGzyL9lCvmgBhEI5jb-bhb05uNS6cmXr06mK34yzfeMLqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجتبی زارعی، عضو کمیسیون امنیت ملی مجلس: عراقچی مجوز مذاکره با ویتکاف را دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148941" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148940">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZrt_OClXP0wDGph6hfKErUV3ELVPQ94Tswq2eeVEgWN7TRAik8tO6HvVij0QLuev2wSPdCQUuyYqB8AA4VmeuVD8EWwre1LSxQhvmGSxtKX3sm5wwrPAU2AraytYQSd33c2z0htBWPCrz5muwTKhtZVXCggk5geaWZkxzE-n9n2gByb1mRop4hC2kIF4XjwJ3EcTgGRR4JAQ8AtGcfwL2ye1onEEDe06ayph9iCeFPQ06r4ooC-aXEbgQEbAJMAbnDlhtszZjnYPNw27GxQ0x8bbVHhZ-KPyPzVEDsXVMLIXR5HIYGJAZefbuUCxnyUA9UNFhtk-y3vns_V0tdimQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیفون ۱۸ تنها دقایقی بعد از موجود شدن در دو سایت بزرگ تکنولایف و دیجی کالا اتمام موجودی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148940" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148939">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی بریتانیا: گزارشی درباره یک حادثه در داخل تنگه هرمز دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148939" target="_blank">📅 15:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVpMBLNLEqVGDwjwsJtReivpGevJmCwLubUCB902N4RkuGM5xNcdRbrPzSxdDii9WO8q92-KnEPbYti9EnhhS-rJ_H7whHBQw9vE2vAXKXf6ryy4tOhgzJc4BZAGPhns8gltUbfE3bYhr5m_RpH4fDYDuyyYZfSdw71Xfeo8vbBMwBGj-_bUB122ZgfKkTKIzkv5LgYzBWzDYDozRt7LjM59TIKecT51_3Q9oF_6kLwUtkTuwC3v4pC8obvhxQ20uehTqmtf6wN0bsTRx9d6bfFxAU_gzgeMU3m0ek6KnV9dQQkCMaTFzlg3qJZEMH5_pMVgkBE5cRhBTYb1VNAqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ۲۴ ساعت گذشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148938" target="_blank">📅 15:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148937">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا، درباره ایران: «تهدید ایران یکی از بزرگ‌ترین تهدیدها در جهان و در دنیای مدرن است.
🔴
برای مثال، همچنان تهدیدی موجودیتی علیه اسرائیل از سوی ایران و متحدانش وجود دارد.
🔴
این تهدید همچنان وجود دارد؛ قابل قبول نیست و هیچ‌گاه قابل قبول نبوده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148937" target="_blank">📅 15:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148936">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e681aa54.mp4?token=Rnh3re9rioQ4weH6slL8XavzojATMZZZKuTPLpbJBfzfA1eu281E9FztDmUuC_afl4dzuJxnRU1NFOEN6hrzUuPbYuaSD1TkvpPy0X-kYJI6s6BDDk-KiVPq-RAsUUguj8uvpB7HW2vxUBdMh5VyLe7hhcCEGDjk4eWcc6vGeQELYwT6_ugQF4ewu93qpw1n8_We37lLptY6JKwo6NX_qXSbge1TmpV8b6IOpGzPLOtvEOhAS5-yk4cGGzCfteaFok_KIaywJoHscHuzPwwQmJPXZ1b-0O85Swo7q_KhwXbEyZTAiU9yFWypSWjQ4kF2QxgjwEIwo8lC8r1S2MYnCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e681aa54.mp4?token=Rnh3re9rioQ4weH6slL8XavzojATMZZZKuTPLpbJBfzfA1eu281E9FztDmUuC_afl4dzuJxnRU1NFOEN6hrzUuPbYuaSD1TkvpPy0X-kYJI6s6BDDk-KiVPq-RAsUUguj8uvpB7HW2vxUBdMh5VyLe7hhcCEGDjk4eWcc6vGeQELYwT6_ugQF4ewu93qpw1n8_We37lLptY6JKwo6NX_qXSbge1TmpV8b6IOpGzPLOtvEOhAS5-yk4cGGzCfteaFok_KIaywJoHscHuzPwwQmJPXZ1b-0O85Swo7q_KhwXbEyZTAiU9yFWypSWjQ4kF2QxgjwEIwo8lC8r1S2MYnCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا فکر می‌کنید ترامپ با بیان اینکه در حال بررسی گزینه نابودی کامل ایران است، زیاده‌روی می‌کند؟ آیا چنین اظهاراتی به روند صلح کمک می‌کند؟»
🔴
مارک کارنی: «اکنون جنگ در جریان است. او با زبان جنگ صحبت می‌کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/148936" target="_blank">📅 15:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148935">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947a8913ac.mp4?token=UoyaiwovSYFxjXcvtYvzGD3V_s2PQ46rI-CoSnvW9Hiwq3DqGQup4yLz86RWvA-HKysWv38-PmhjLOb3LjcSeIuIv0sgSjLqkwERS-wx9kF-1hJW1no9Y7lBf_Ppj7AwAsjiSISj0uvgN9dld7bGJ3XnmjZdsvpGNue5JCdo5BShSZExNnKbrybbd2HjalzafqaT2JcYqEYmlKkC4I3Wqv_vI2QWGfK4riKuKek4nhdvnnc6MoNHycQxvhe02UaHEH6w9WJ9R6xvWLKUpEtdWUDk0e3ILv_XzFNWGBEMcCRxO9mZgxJSl-pj7HdPxfi6aV4cGXN8Hcw4bAul_NWFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947a8913ac.mp4?token=UoyaiwovSYFxjXcvtYvzGD3V_s2PQ46rI-CoSnvW9Hiwq3DqGQup4yLz86RWvA-HKysWv38-PmhjLOb3LjcSeIuIv0sgSjLqkwERS-wx9kF-1hJW1no9Y7lBf_Ppj7AwAsjiSISj0uvgN9dld7bGJ3XnmjZdsvpGNue5JCdo5BShSZExNnKbrybbd2HjalzafqaT2JcYqEYmlKkC4I3Wqv_vI2QWGfK4riKuKek4nhdvnnc6MoNHycQxvhe02UaHEH6w9WJ9R6xvWLKUpEtdWUDk0e3ILv_XzFNWGBEMcCRxO9mZgxJSl-pj7HdPxfi6aV4cGXN8Hcw4bAul_NWFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا از زمان حضور در نیویورک فرصت داشته‌اید با دونالد ترامپ یا یکی از اعضای دولت آمریکا گفت‌وگو کنید؟»
🔴
مارک کارنی: «وقتی ۱۶۰ رهبر به نیویورک می‌آیند، به نظرم ارزشمندتر این است که با افرادی دیدار کنید که معمولاً فرصت دیدنشان را ندارید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148935" target="_blank">📅 14:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
اسماعیل کوثری، نماینده مجلس: شان پزشکیان خیلی بالاتر از اینه که بخواد با ترامپ روبه‌رو بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/148934" target="_blank">📅 14:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148933">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رسانه‌های پاکستانی:امروز صبح، 8 فروند پهپاد از افغانستان وارد حریم هوایی پاکستان شدند و همگی آن‌ها مورد شناسایی و واکنش قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148933" target="_blank">📅 14:39 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
