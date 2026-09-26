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
<img src="https://cdn1.telesco.pe/file/huHc2qn_DiZxymcBZFFofOwUaXJWkrkssmXCWt-O1uEiceDEeoNgEXuFBu_qd4eUYWF0meipk_KSKar1X9lEWD9D9DPUhPmGLIK2TrQiR79i0yWhiqO4dgdhrcqfVtOQ5ttLUMdwmMNwkgvN-UdjICm4FcYy8x-zwMEaGbJhzxQJKsdjbCb_iipsPS_zTjFV1b0obK0J7ljpOijE1PSAkMkrW43adCtbxEfACQHbV3mvYS62tfR7AzsHpRImeGitvUv18T8HIkkIPdeBVUi8Wsix9oOvcuL__DfYjhiCTmq_jMcLNLHVlMdfNfeVZIISTN83d52Xilby9lMGtnxKyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YEFI1hbdfxw4-IHzaDZ4zZUowcWnC6PVVrmbefnFzSdT_YeqX_1c5xWglZaemptLGwDhcVqHSuqrD1P3YwCr37GyGTKFyghqFjSHFdb6eHVrpw-Jnt9xaCStT7c1z5El07KhbCGzNlZzxPS8_ymW52DSBTMj6n0o4O-NZLJGN2Xyf_TjZ7DoiRr-xydkeaXiKYhi3p0SafACKDQUmOwk8xUqAeOXt9SE6GAiVjc33W4yNBfbdY_kljkwSOEhvc4B8t_RHluHiqXw3BuoGbkNORq9M158I8HkDXj1-Vkwn5t_1z78i2uhX82fqR-jxZERBpMynD-efnWcgqyrRiZ6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKUPlHw1-5CCTblRxhq6uFMD7Da_bcm9dp3Vvzgf28_VoDN-5w93PWtSx4TlWcWa5QJA5M3fWSs2QNOq_3QjTF3EE8-tK7p43Xo_9FS5rpbY0tk9Vt-dozz0VKdDW7_5VkgE5H7caPPotQoJb9Ppc_aTjTsq7N2NKXhTTLKrw1WOAXWbZhwwwF5AHcRNcuq2tLfWiGkT-wVGrEKhlpQDV85DmRMjit7DKcFCzkdYEz5jWT6NQDK-ivb7t16evUZT1BzbcpkE7vk0WQr0WpPzFqmmkVfIvWeXsOAnrJKFWSExS4ax2Z-I9hp7yDmLCl4oqasTVfcaMkeNcYQvxNJowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCj3AxdYH4lGPZbs1VTrz-XKMjWyovPeOxTypdh_QuTaIfuqzKPwN9RApxUi13CHpk2r-43KQ7Jg-O2QyJH0B8ECp9VwRoiqH4tofZe1hY5fp68XOCjW7Ki87542dskV1gJvoUX9uCaVj2XTJfr0gRU76C8rrRtJGBz3uLUN_lthQTVXNPHRr1xtDaLMcbhMVKBqUP06M-YcZobH727TFvTy0B48XcIu9yHCET6naHefyqnP0adLmWr2dIYN2TuqkFOF9BIryWdjtDY9WG9lbf1hDhgLG4NkEO1w1PRn1kF2PYrqq0QwMpy6PRBlCTNoeEukWq_j0z8NuykA72hhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UogdDOYR_XzMnsXIN0hLkzMuy5E3QYN7GK61B5-T6Lki43nMN9Iy9IG37CftXcmOtKTeWfFVKqupNh1ftg0ccgldKyxqvtoG4ifKdrTn5_saybUv5D9Gse1Vd3_x5RvJ29pzpDXtIulQgHDSj17wEWmn75ewuOmBETYLCco7IgY41rm5Pn7VTmfA44p74oLZWSH9pyAJ5tfjLuYC7z94zhcnXcoSNflKMu6RmutMMTriCYWdLQop4giOxqowwUqSego9halMETMN12sDsm8geykdw0BIriQ5775aTK0-XMIP14nSG_Rqt5WvJvsh4QjVXrlif5wXa9vbomQg7be-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QppTQX70dB6992nlfgyxlon2-bZt-CD-k_Q81flDsmrjX0hz5wrQyRYAoHgk3v09nWZx6-q21Tpwwia6oYg8uEZ7Ybh9398YI7dBO3aeLQlfw0j7wyj1Ou9fUQFvwMaD74NmFlRjn6KfBwLyNtrSQtOvSJWI0dmAyVa2gH5ekfB8L2BQSUmJyLnXokwtFm1gVtH383DNXVuD72cTqpnWw7mxL3RygmmGfJLm8Wk_qXvFFqhTQvgF4M98aCg9PVTUPa34sotCbu8ZkyCALQCMBjVl2iWXrpTYDfutIdx9dwfjg2wQiyqQrx4ID_09cYaLiIEbRwDfIgN8KkHx4xy31w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PNj5QUWhosw_x2KdmZyJhZNL14WeUhP78heVmnnFQ_EQeCVIt9XLjVA4yONKWXa7juyc8INX2LwDvdYfkPb1CM9AaENZ5CXipoDMiyS9iIzx1igJycTwyZrvou3CCbBhlqbS04RNUfsN-OvjGAKW93AJ6mq8VW1ahXGfoz7NgI1E4zS_XZhdSxaqiY4C5Kagdp-BwuIEqNZlj8teYjeHOEFsfj5UKGtSon-NPfLkwybPlOjwAjjQgncAwa8pTHjFicPiXvFeZVFQhnOe4np8XI6bHulfuY_rus1qw66B_wPUTqEfw8w0dqLmT9Mo4MnsVFT2A2bYwoVgzfLdJfBMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq9_Y6kwGywKk0x74fa_SYf3tJ_kXymKH385RP-r6GGC4GcXnOEcFcpBO48k-7tP2AkWuf_1x1kJBz-3JRxu0UUAGa_tRYgKhtYdoGZbDQqb_graS9bHQEs8wnR1IcJDYsGWuQzrvKLrHHfW5laf2m9xDcxM_xN_04OOSJWOqPwiLJZJ7xxVIWONrfzBSwtE1gMRwkpnULWZKzyS2S4dp6bdoqtl1YARSyJpdHdaB_Dn0W5RvXCbF7obaR3Tfy0PmKyFIwvNbdhgjP0vMrUfjYtQdVidrijSt3AWJVXEpBlqZ5K-mVINVGkwAQa3-Ps3pVX1Jr-2csfTTK7XaLCMcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_gp7J8uMDLtw5Jg6EoalvSEA4Z4dL53W8W9-SFW6ADy0Spi1efPFs3IX60Yj9h9lS0Mw0S65cSMGMCazsDFuB56B3KpLW-53zGPXe6m0KOb2v7e1hhDDn7fU50oUTOF3vpLl88naPv-X929CMa6um21MZ-l1q0fsoZD463RhEKtFPRxtxMsfPa9P90gEQivbBIki8ryuxyGXFkLBhIb1SYnWwqFUH1_YIHNagqeApN-j_RV4oYYfz9g3u7toBbpgfZ33fYuLacjwUe_EtBRg8rC-kMEUbGS17lvaqLErECGwr1d2KIueJvUtX9ryvnQ4edeMYFTaj_ADRgqn7rG9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=oLKczy52Qx7DZESeQW4gSoVOw_Ozf3yjVmfWg-yhN9-P4kfSNKSrJB1NPFRQ7wz_x2sFoemu-nYJjc_FizaYDIAgJlzOLtiraBXr9v1jlj_fwwVej1E6aJljvnWH0JXuGDc5lNgPTwtNfPym4gvEfNpo17B4vKIV47bcjAur1UkvkphbzD5TdHtiRzQmfFYb_Iu7msEEKV1FBgpa__-Uen7J9bPcJabgVGTMSBbZY6bKl6odmEmaolK4rDs0M04SWuJBl6Kt-DTw6wHNwVD60x2mOYTGtRY6UrUC1lQbsDad7lrKaRWT7js4tO4R1qBYlOHQ4GOaTpmZTI-qUORvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=oLKczy52Qx7DZESeQW4gSoVOw_Ozf3yjVmfWg-yhN9-P4kfSNKSrJB1NPFRQ7wz_x2sFoemu-nYJjc_FizaYDIAgJlzOLtiraBXr9v1jlj_fwwVej1E6aJljvnWH0JXuGDc5lNgPTwtNfPym4gvEfNpo17B4vKIV47bcjAur1UkvkphbzD5TdHtiRzQmfFYb_Iu7msEEKV1FBgpa__-Uen7J9bPcJabgVGTMSBbZY6bKl6odmEmaolK4rDs0M04SWuJBl6Kt-DTw6wHNwVD60x2mOYTGtRY6UrUC1lQbsDad7lrKaRWT7js4tO4R1qBYlOHQ4GOaTpmZTI-qUORvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K_Vmlr_215TOiKco-nNQDhZ9Fybb71pZ82dWwVK1I9QcZTLMPLFaG23DJPK2_2LtgV7FB9hwhOFuf7nRUie_K0mLUA9tgaPTZn3kHMwOP003JSlBDplTWGMytP4oB4piyB5H5tlXs5-d_SjwloxturwhggTfo8m9uQZVkto9YMUHs8Bd_slpH5m6KAV8xH7kOy8_muprQsM49W8ZZacdLkxwr00VEob4hYuzr9TQiSN-4i98EWriG2W2sLQEeVAj8XuXW-Co2jD8WrZvWK-IyUE_nW_oInF8fdAmUFm1Q2ne3r05wfT1w3jf4tK7LAWZxLbL3jZgl_5DpmN1CrXMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaxlHHZXkmUiyCquCTG5028mHfb2FWw4XWzvHdi6g71TnNRREJNrFdn_SrfUdM6GLr82p5_dhig6E1StIbsDIZf0GScf4uGmJRQAxh-r_sehJ7gMiwf3LVEPK0_1zz-dFgyEN3LGN4D4m2Mmi5-3pY0w4_jBrRt-8GKPhT5yznbWPjpizwGkkSWwxF6Eaa4G0z3SL8_YOmcyArCOnX0YhMe5QV6jZrZTMK-2TaFVJp1mmaRNsizMs1l-viiu1grPS6N7NYmwtMZ98jGRQERjrhZ9Rj_o943untLMCIwouW-ccdYsTxi3t3AsT6uVI-5eCwkHgbO-hpisDlwjNvMugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NlZfPOrVVe4_iD9qpE9SyW0U0TO5L51DUmU7auH4VDVXIQd07OPElQP-iymZbGtMjLIbqHREUbiqdgA_-gFbWPKrq4o16ABRQaxrylI1EZ8tN3SJq9-iMMuNPluusWRPecVfYQjm5ZfGuTCuFFAdiNDg-qcyqFDOnHu3s9a9DK7vunGqz-R9Gaxeb_0KV4v2juZl6CvKwNHDHIUCdzWLFb_a7aHVjrX8pMF-u-kDNRarQeugbHY24TnFwJZnZ3uM0deDQRHwnkNuqdm5dL6bD0EIQWnsVDXOF_8cLkkqheAG5BjFcaLp8NlBnue-Nw6gZyDDHeSg1AEAIdA3jq9xsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EWY2CyEiv9WFPiaB5y0JwPt1Luzk0otAqKMjXPfgKZncukSqIJ5uZa-9rr2dcwHkAh8hsWFFo74UBRAA_gsb7IuX_cJBiPWfFLNe4nx8FGhrrI4PBfA-1789zqf2JXwme7A5zwBrxS4GR4r4IOl49zO8CRP6vy3FzWTaa9EkjzHyoV_SiXIicOIQiGR1J9cbGWNms43j7FWkbGPFhCE4G5Su3qTRPT_5_D6e_gHwVFmtV64N4gpg6N6oCeC9MKn0B54EjBlxJ24xxWpo25TE_vhqrBq9TW_p7ru0IG-3awQlzS3tIxO36o-kshvs15hp1lk2CHqaeAcUns92zdVcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=tsnNT4q042UHTn3SVlGE0bsTTtYe13Wj0PfmfbiyE8PKxHISl1UFwgJEo5092tXlFryQexI2-s3UTWCZQpsJZUwfIFE-LHk8b7x03RVoiCvkhy8f3uGRHIpfX6ixyNXtER2JXuqlJaSC3I4QF_ZPSfgRgTl4aDWVfkc-n3sS5Von98BnifcahW6tv8DIcI6i5T4Xhe08sbOi5mGISZOxMmvXB3YME0KU-9_qFLC7MkWmJy3-XEYEXmFLTm9CTG0rsZYb4t692GmJeIT2xtn2a24WHBgyTNiPzMdmx4W_2h85rarHauW7GhYKfQXyLZ1qZwnQEExKY5t1V127ee3ztA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=tsnNT4q042UHTn3SVlGE0bsTTtYe13Wj0PfmfbiyE8PKxHISl1UFwgJEo5092tXlFryQexI2-s3UTWCZQpsJZUwfIFE-LHk8b7x03RVoiCvkhy8f3uGRHIpfX6ixyNXtER2JXuqlJaSC3I4QF_ZPSfgRgTl4aDWVfkc-n3sS5Von98BnifcahW6tv8DIcI6i5T4Xhe08sbOi5mGISZOxMmvXB3YME0KU-9_qFLC7MkWmJy3-XEYEXmFLTm9CTG0rsZYb4t692GmJeIT2xtn2a24WHBgyTNiPzMdmx4W_2h85rarHauW7GhYKfQXyLZ1qZwnQEExKY5t1V127ee3ztA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsvQ-wCJdiqQPyJB0VFsyy2ULN5Y6IuhcbloxERy9SWRhpCiA4xEzJ201lAyJzEJOfEQamBvVbC7yJlGfhvMDMtX2AwAPbq0ScJJ80sZuIcyuS7AUtmY6fNtZyerEm2QxT_zXDGRPDPUY0n-3IM16PKMI_6bNaoneUfF4e4CI5XWmQ930e-52WxQOEvMBhdbfSplmcIRALT8IluJ0NPHZkbNHTKvS4OyqyOKtiMmvDahT-E_mZq4LVCb5hGQEOc2YJkNZTs4ZtHwWuedIY_sohULRL1IoNpzY21hFY5mVMobYNjXh9g9p_HjMREtE4U4iZ4DzL8A8DZ-fYXQ_8CX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=A0QXRhYqRUjit62r8CUfim2QD8aFDgnr5EDrjL3rjKZpkVjmyY8p4yQwERZToJhl1paS_yrALAAZESemS2ZOMRTH5cWOdbSZ0ek2Ui7wDG1uPZedlsVPsl3nhlqTo6Fg8XhYFvJRO8RlgpP8vgYvPyfdigzNMTHnxeRwERQ1KHzmuRlxasOVsoTPJHTlMKCj0WvdwHOlGlZgco_i8DF-DRIpIACv6B6wM9ocLzI63XZ0yoYhVRpAECWNB-MNWXEDYReYJulRd1FHvj5WzCzaiSpvBtD-0H26az1wnF7eC-jDqyFLK8Ox10-OrFWB9ndmZLlu8lGI-fS7uMgaCTJD4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=A0QXRhYqRUjit62r8CUfim2QD8aFDgnr5EDrjL3rjKZpkVjmyY8p4yQwERZToJhl1paS_yrALAAZESemS2ZOMRTH5cWOdbSZ0ek2Ui7wDG1uPZedlsVPsl3nhlqTo6Fg8XhYFvJRO8RlgpP8vgYvPyfdigzNMTHnxeRwERQ1KHzmuRlxasOVsoTPJHTlMKCj0WvdwHOlGlZgco_i8DF-DRIpIACv6B6wM9ocLzI63XZ0yoYhVRpAECWNB-MNWXEDYReYJulRd1FHvj5WzCzaiSpvBtD-0H26az1wnF7eC-jDqyFLK8Ox10-OrFWB9ndmZLlu8lGI-fS7uMgaCTJD4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a_MFcfaCSmHdGtEkWr8B0oPuCvISZfP7QnslUPs1xRUdq5gRgpt1b45SSOiOXHGjgMLwHWW16oh50IowghzWX5uvtSFM_MTV_a1NMc76codA9H3XayD7zmRGfeolwS63E-mUlw_u77GjeQ5F05ERCKh_QlWZuEQ94gRoLHhHFo0RGDqDSh0E8a1uevxosxhXgmQsg9VN5cw6IyEnpUBVSo7jcKhiZKGNmFan3wyHZJGbBAEq8zoW0nuH8cal_Pu8jus3RWIewCehzzveF1KGujdJRgOE8Dls40NCFMHaBYJXygqakBM_aVldroi_DJ7f-6tCP9jD7MFHt0h_tfswzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hAIhnUgsz-Ca7_r0Jakb_84_PKBoExBrnPM5QwdU9H6G-CRsvabu-Dfe8wTwdiVlp3mtgK-3vnRd5skZ9LMhMj8yHDkVYjOwfAoutI0UKKl9oOFwGQ_THx0IDowFe5KarndBNz2a9tjM2QREnlFu0QtuDY5BGQm00-dLFbczvJlLTxArKcBTHmEwqV4JzSopZ50wNjxYarJuJD755QRzNmnk5S1hP0y13YfH_8_-OoWMUj_20FTHaouTa4qEG_88G_E8VA3pAzkOvSMGc00rBjClp0WFw_8Awyy74uSa_56U4YFCLIpGM70xR_sJE-mL5gskr0MAVV0zeIEOGcWn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RoUDN26s1_2KwC7gTajjxLkUA4crk80RoCThTA03IogLr-N1mcWdhklLrRNqjNPhUhx4vpVVzekAYZ2crvPTUrGj0JB_quuajRUpSCZYDGcbJTBkemOsp7DqcAm_IiEL5ioIEnPDywCJ2GqcWVoVdJch3y7dgJs6MH_u92Sx4A7gn4z81ey1d3plSIPpo3sTgtqq7WbkHODtrrDt-YiX2r4Mmrzi8mUm9Rn2PkupGilzV8QRQvRX9dqg1QlpI9Ltb2d7TT6aoWt39xgEKUjVeBcvbcy_Gcu16WHLOqOs3ZMnawZj2FzDM7xnCYvCL_Z53aaQg2uZhlENUwVggAGwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uI6EtkcpRjAE1J95V3xe8NuvkwRIP2oRbJYfVu_lDxJ8aYp82dMuGlHktdX3NnACOTcMDpl_Mth0w1N9o5eBNRx8tCU-hWZdbalK8khuU9Kpv2YtTuRg1CcpBFTIOkY9uY29A77ZOJnntuANVmvAhJV0SGzH5HJzrX_B38WkxeZHZ221VT2OXnNuliQvpoF4-bHmIiOD2YM82GhLmDfeWSwWla5Tnoaj7Q_AqvL8DlgJZTTIuMjyTRzRh20zwWRoqn6tkZUr3BEZEGHIHJiXKijodEdlriMeJ8Sbe7YYMUiCLj0Bewzf64hFW8GGNeEmel4knj7A8e6w3pOD9saR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/krag1swLe2GCryq9zwslGm-LoR4cdCZaFgU7wQibaohCVRVFu2yWrNAAsFtb23fKYdC9N-ZWZFuLU9KXXCx5hnWq5-fJ4w7ocxf-rAYUjUkXWLhqdj7hTC8-qwj9YBptictENbn54JnkMllSNGMDt0wXh-7h70jCndG_ZaVmNhD8P-7F77p8hbjhUP7X46BTCFKS2uF6TRe0f1s9XZh1Sc6qjnmsGno7tUut9VlWmGbovq3yd-QX68K6JG5vZ6MSSxt_fT_9qT1lrAAnRWe4vqphYV8hMf5sGB35NRGQpBAcxFOkrALKALXXpgRPrR3SKAu-NCYlorqVBnYGleaarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mXYm_ZYNwg1l8kF_F8QXlJn_X4g48vdOEPgYZLH5G_kC4nky7M4tkDWVoHqhAiZ5g4U06jA0hTUQqd1R7PushCkuocl3oq6OO8LWVdQBqlUHMNyyzpU28cSV18EKHpahVeBOSj0mJqieMXeG1tQe-Phyi6s6D7MRV2sKD3yZ9Gfnw2V5C2zQy3kZvaOKnklKc7E_QbfNv0CbQht_YYqqhW0QFyQxuWZmX4HP3iqnwmE2qHaEfipzfq_HJttOjR7lfbsGMfeatb8xkRGJa6EPGOdVN9lWKU4R3FJnAdca_t-49bI-38miS6FnMDhyA6YzakQCXjp3HlBUngLjD6NisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cdlWqk1xj8A1bnQ7KUQEqFyurOjBbb-vxw2Oq8OdZL2ckUGJESyjI5Fhe8sHceWhmkO2Gk4NYW9aObfn16FPh-J1zoz1_NU4QGU8XiwACbZfal3Ec_kq6pqp_p1UyxXAk5ZwSdM9ffMO5zo4ReULFdZxOoRpuTy7q0sMHS4Cy9mSm_RSvWm7Vj5-p7LJ-inS2h1hTPQxPJmGWb3w5MxfTrGAQ6FXOT81LztURXv_eudakgxpPwtHduW-3Ngd4D7vg1X7xkQqt-QvbeYP7t6Mh2Txepj3o26MSUrdtXM8eN3u5UjzKA5dSeq4CKsh89mPw9rmL1SRuCE5cOgDvYYUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LN47iLt0dwx7qrkUH4R1ue1TucZ8FFx-oZ0W-4G4tc0k2jiA3dxIG6cm5PLxbc7ertmO7db8zJh2CifbhqeOcZjDyJOi9src0Zu_knZe9nCumyq9wJ_E8aij2mUlYVBkHS-XBvb5H7wlr5bYxOAsJ46vzMsdwpG8XV0xb8iv4OTbRkt2QOOiwoCSuJDUtL1sElVF_d39ZlTVLZt5Y8g93ENAi0KFo5343FG2mJu84MSgiaZxhdR2qoTsRqRtz0r4QJ3aMLzK1m3T-vrmqZ40VnpHbSPG15uMZ8e5cN_DwbyXACxHefKZI0DPIiDzAgFV-PYCoHCEX9z6HuFU3wDVaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GMgH-SUUDF7pGv9vbmVHuprV6HrAVfkRy-W8L62ZCq5f-QPwh5e-ZSwM_PCbIG5QIFvLlJNJPZBbPEOnolQnvVsoTNPXglIly6WPm_2kR9AjBvjuAZg5VZx0Jc18I6TbPvGCa5-P0IYhSrCMnZWQwR4aMIIPEM8N9pK_56ud2K8d4d31pxUXRb6Zhy4YKizl_ECFUhkjB4RN36YncaIkWMvX3-_OBpcP-ikKTcnYND8A25UPB6N29oz7FGOMHUG9qQZByXA1c5uwOBUd6PQLmUb72cDU2cwIIGBnH3c4VGpVsRX7y1BCJB8g6rr4DJ-JKBxqZHeWVH5NvfsnFEDVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dmFD-sAmtivy2XklK8hFZYaKGwebpivAvFnd_XVJTAYydzRDjOc3HDFh4Hr3xl6hYtL5F8TJVSeFyiCAdm5To_2vSnMNkgebOq15Wpuy733blix07xUHM7x3qfW9h3hMuuqUdh_qMB4KZ09t8pVwLc3WLmgpXz3d04Wki7GKdvwfCq6mvlm2-Y69PKoGmz40SwiTOnFAkUFt97AlWNrd-HjHzf-xd-w2aAWxUhK9kRcmCuniDtLnJaTQ8lxL7AzvdN33MEt517yMsydieYyrTgHgj9lenxOBIdvQwLKAm3DExLwVlUj-QjE0QkC3QJYNiS9TlkOtclpNmdCjEyw4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PWxLxPoWqz21zMcfdHNF_1zEXlONVGhnvqWc4_mnvnFEEiv7SBNQIR2eRd5bLrePb0hGx2We5csCjHrE-udXFEUJOyFF8CnfQitjfzAxwdWhnKdyDH18VG40KcPZ8WTxtcgtRXtMLWCAvaWjeBJ-kvuxMVgfh2faNjrG-nC01f5p3vz7cfh3z5ef81t17ImmbQBTT5qY7YiKVbRf18L2VKQHjSSYuDBAt6coEaxShoVxGXUqjz8EdbRAz-w1YRyoI21-bK7nGqHv4BUDweZ3jVmLKOpye2V43SiToPuwIEU1TN6Y41OCEVv8oqM20R8O4M6i32YylfNz_M1CEgItOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v4JJtgiF2tevne5G61qeG-FWdN3NO1BvsspxhGdncyuQTPcsbcMDY_m5LrxZva6OthpkS7jCR6wUec3Kfrb5BCQuNUSpgGrBe4A1V6_N8HPzCg0QitIdz_xImk0LL4FpXAMKkvk4MijlSrF5EPnuhZ-ogUGP1wZyxC7M-g5HasUc9WSN24IIYoQ4RIo9KaVisPCOS9kQMU-5acvTCKVvgFKRktCV-V05GnXxLstQgOmaoMyG4v2E__ptx05S3mXEg4nla94INvRUQO3KoGDcLohcGENmnmjSXIIzDrjNw8WypU7b6bsH1RVeZ9O0NJivbNNjGWPIKrOlnAJRt2W1xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YOgZI05GyBFAKbZ_K712y5IMgbQrTvtamNYf0KnUR3nNUQ4n6a_4t3I8Gz2DTELfEaKUTBMhEipEe7g1xhsHS6tQj28W-Ng05FOZLA15V1SDblWpI_DXwnyWAMWWEfCzuzpXpiXK1l0UbHpZDb6AJ-be2pKf4x3NOjZ-02KCaIbHn8-T889LtiRgz05FfnrUuauYK1xMh0mA7OK0845HBZvq9NK0ODK2FyhpxIt9jMDdd_JCAPKLMaHBhPBFDbRqluswynbWIHoAKkCn7Hqy2BjAFbxKSnSQ-qtryzzIQFZabKfh2XJt7Ymzo2mz5aSEOfIAdwF6pthfXCxS8PqDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WlbzVJGrJDHV0cE3kRdxdbZZ-ebDnZlJECdbTNsuHS6_VjCQIQYRRWrpMOZeZ5SDi-G_GFaIFWkOsjXPQKNtkcfe6wEdJgIdzTmJ4GtnqdslzwfybSYRAMvs_wdROVz4abP5zuSepGEbtFDAT_bYymDckeG3XV8EvyfLz0tXekAf3VxWY6KeGWtbpq_iOGnfw2_O8mkKqjz5qsRjAODrv1rIerdvbnY0F1kQ_qp6wTI-mKfywRWlIv2T1631iJY6J1tg26UH3VHTt8rQ24avDf4kjbkAu4Q6wMO7uzNGv6Uj2zg3g4080Sp7RizvwvBrKhGb1d56XVdElfOEwc4TWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jg9Mu8NNqnP_akBn-YDGyhXnybmEmPRY5q7tOFHGrqw6wvj-7GiNWcuaZ_PJno_eDpptlKHEBn3kxLKBXs1JQ_u8BAQoVudxwR6u_uneX3bqWTRt2VHps8vhS1T9md0ulBwTZp59ISQf5uExkZ6HUrP5GQBRGS3OFyU53A6Zmb02Md-ll5LT_06_ra8H4qMrzhXquT8iiV0z7PgTvgxboQwpfc3wfpQTEpjvcmrII473flHCtwGjBk25QJjwhktGEh6p7VDExqhFGHmHLmsmyE350WtF9poDaTztutpATIrdtR1zbO3TvobJlrE_PbhH4QYWybF8IdkOod7XZkbKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PxbhDQT5qVqCAV2k7KjyZfVmH4CHUsRwzof0b20emlzBrbtI3e5uEk2E7YBaKKHm4l_1Dq6Rvn5efPS9VbE-_R1cKs5IZDzvdk2A0cnUkdp-XYh3wwNwZWzHAvZnmM15r-naJbbgrLJjGdKNICzUi6WGLsmSvmeyeKxrKTCVFgB83uUQwaBj9MbilcCkC36HgSTKjKGZUffT7vvT6x7HKyR5WBcOy_zZWy11xzm5-MqrcsVTjKZ3WhY2Q1PLW0Zve29XHeyZffEDvkR3d_yP10wPFIyt0I07OBCVmK3LHktipkv5mZ-GioiXXWySG_xPST1lN0NbNxxddDwsYxTIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t0BSDdI8LmjiOu0RhinPJ1Cxjs9ba0_uZ0VWUkCwSC7TyjQePf0c3UCzwzZliN5r1LOQO_q0LSZGR94BY3QKfkgpEmhimQ8Dd-pBYLTBachCJaxuYVELXdO0i1U2EUp6HZVKfwiPDzgMzTLpERchkJvIBG8aW9ncow5a7e64ddYnSzx_U6qbkH62nj66UqZ0LPE7zv4cz9Ny3U2M8FKoyfox3LyCqn2sAgObpnQFOoXIlS8xcaRtYiZJCQqqZ_jBGc6JVEX_ufvXxz_R73NBECr__L_Aoj13TTZ_tIo5XqRSJYoxEbUiR8iZ0GFd6iu1peB99v5ngJz4LajWwgqJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/muX0u7oP_fiId2Jg-cB5WheXdN5DxWkvPLMH_sEIgxdsMkfnn6I5EPnFWdN_0c7ioeayzIAM__9JgyNQ_D8gKWNJ507GXJ6mspkBytYnUOswI7jO3mjjaz6kc7HyPEhoqZljZFXy_koixgNsKBtg7_19ZMU79nXUIo656_4rxhW-diRpd6-4H7RqXR_DttqpFPmFebsL6fE4jc_z62uZaehFU9D52bS-BmCmE6Fcyws_Y646mKnWSacCS9SvZvAHwRrFSQGNDPIT_IOSX-cz65eGBo2EAmHF4p1zZjHhoOq1WWCjBdqKq1pzM_nW7HBSVT-NkdPw7ZjtEYivqMVjvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mzAhl_GC3flCK_J7bR9ap-zkEVEOFKri0NfYWnbiRw4CNFhVM8SU9IvRG-p8JWrgaXrs-FMMyW-W8Lro0aQ2_3Cll3hXmwCzWP1dfExctmep3nCYvCxzqXslC5QJ8gFx06gywDPXbzHnZoD887ao_pUKV-EtspjPG1sJ7KLba9_Pfy7rxnRgFq21gPy1kmOYGVODXGSwSQCsiuQQ0YloysAzzdBfuCXfbW3ujS6kGTxL0kXBYr9EAW_LmFqaBhXIH8_05hL_UY1zOXjmN12cnRXN_57QM2M6nzO6yfXJSD9oaHsZIX1L8c_2GrofJhJ1Bfx5hkYyd3OyOI8FM_I07A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ixhGtGWIWLZW6wqMj4UYzbpgVUxmw3sd64EMFhc4GCv9-PVLCeBtoS5qFV4uxP6ZRhxeKqjhmnMIH3FFoZ-V61rGOMkclt3JZAI7OjoqkayTPa56H1nSM0Cbsl-bRfYSkudNuE2IlHbib7jmW-fbfvljrWNXBRNKBHwRY0oEgz6CeEqb4VooR98HoRtnOdbq5Vp8gkYF_6n-CuwB7TebIo_Z3DyzdTOj6LZ7DqL5E11mjr0MIuFAngXxgxz3YhN6mCjcbMu6i6HuLoEKlJaq85DLGAMsyYoCgmslnE635qaOL2m0vQixf7wSjjW0AHa4zm5sgQehWW7mzNHSDjxfMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NbC9BeyiD2CUhSZwF5cRPkUKYetWGsvB1i1lYbZTuHhaAQKlS6IZXjniOXCep9mt5HDHDqCV6UZrZIZ2so5R_8e2nVanTrUtdiwcbGTODyxUbkRjRMy1U1I66A2y-L97U9NaoxgtdOdmQqYYlMSyGrYNzPnoUQWfpKf3_6ZeXov4_debq8WFYHtk39gHwIbj8pd5i5cHONbjeZu1ESd29a92teRgid1DXJSJKcYnpK3MLU73x_0unxsrcVYerVVFnfG3uLjri3Z4zJmfq7Kn6-WLQjQV_p9z6Ke2l-9dJz0X3OTCiEkDieOXpVJ6YXt_nY3IUVpwxZ5n-NaKJaj5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CdHP7fBLjptkHHfU9mmt0rZEEf-z8hFt38jdiX8atszAh3b88O9n9ahMh-q4JTX11BeQ9oGGzUDNjTxW4OqJsZcrqQdMAE7ghPNKxeKsheycmZMZJ4p09NCzlNVf0DuHT4hPvill2dzxeDeL5QQu6J5QO_3VXUsjnekJrCYGcu-1E5OoaCXqXLDKKoiez8fpT6eQdaT2WXa9sorkeRnCi3EMWGN3R3JhJGNH7Aq1GI70iikP6nSejyWJBif1SuIp8lBmrMDl3NldGV_BGG0nlw_H_dBOqV1BnSMPyjqQnqvDlIKJ4yi26xwzh6QB3gyeYcPRg8Z3H8UM66W1YKKC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXnzh9JinJmPbdm9QLFhpwN6-ZLPV1FTUs1Mju49cJzDBk_2ebKcedfmr_-dZfb31L4KGp6PIUqVoP0titJuBlAYaqfa7Zk8ljynTdxbdyy_VS2LC12t1Mu5qqtBdPioOo_RC932K6_7T4wy0kyy0nV6y853xTJGznwprCA6B632s-FTk1CilLHjkTayoMczkOLo8KN7ib_e3F9JGUTqACsfhzQWC-ASIwi9SJbUl7biu_0mdU-eAMM1xSf0VucYIY-mue4is0ZggalFuLCGHT_hSZQL6N2Ur0NKpeA7j8YXubMRF-F9NohGA16i3jQaZLT5rI_ACc0m3fLz_Jyxog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7jYJTo_XtUcokNsfB8Ssas5Fd2LjCh4T9IQxHKKEH1vx07JoArwNEHJzQjsJHYRIrv9sThREeVRmcV5VgzqXyI7lZgzden7XY7VO5bOuU2n7WAj8g5ggS7y_VATLRyLWs2deubzF2Ay00fJ73I-BwpxiOi1sQsEUudKFyb5kOEgN97gSKdqp0055h66DMn3wrhuCmUAvCB3x3kZ2AJTY0kDUR3YLnCuYZDjGtrdKMESeLPWYIVQanfIy_VkWzNjLcn8TYURFvAzqMjTCpyrdUfQWsK8p4tjFt1UAIZFeDpBDjgL9cErOUYBOABQWlMKBbOkba8mj616hbY3lX27Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gmzQ36erMg8sn3ql7JYNLy03zJw5oO_U4FjYFHAeXvIQQXHlt-5Cp7P9XR3fZ0xvwdHXWHwDNgpmT0x344bTtN2NqUVnqKUgqQLEuLAIGlQTA4pVzUBdx7J9VytDD1n2v7eVf2j4kzL2spPh2F3qq8wmD5iSCs8M0Qk-bJz0ghLkE-t6A1vI52qsNfGCsxnkx_uXIuMerMRH4NQb99XI2QE4ETTsKrF6uaJfsFE3MviJ5xvQLyXiXsy_EniiGsyivRb4CjyBdgmZrXSHzmHaWul20j9U_SaNKuAbMHZ67ymkT7r6shhp7r_S4hcquSOu1NMaFwuJU36hgTP9ULnQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o42ALxxOQ1IrZHLid3OCFxpKO1m-0woIAeH24uiRcoXyDb_-0Ab5pCOsrMD2dayotTQuLP6riIzM_wb1HPIE5F8nwGxB7fHTXC-no-we5SP3lsghqBRYueqIEncwZt30sMcZs6CYwT8D69PRKsKJUCYnWT34i3HJ3A6NTvd9VVvB7TNJN20cLLK0jf1_AdBj6xuFGrbja1gp20xWhZKGp56moTbCiHu59pC7tvRVmnf-t0Kx1eGQT1yS5A2DbEE_S1oR6kVs7RLzqznTGVO_PPrSG2__ckJrEDbxP6WFI-anlLjgTYHU39_thBZYsY0ixGU-Udvxd9oBFqxElxzEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=B2jupm-rrWi6uf9d0fPsn-gEe4XYnhP6Mafipcg4eOZwMcN0H_GlgVqTnVcrt1DvUDtjDQYpKGRxEqepGCzxewmWMMSVZdJGa9xv_vliF4y6lukHVV0ffj-I4_Zj6NOfrY4SKqA4sqrzsi5ZT-RNbNll1XX7CNjrCK_ADGK6EkaQxVLPz4xEpcjrB2FGGLhfRNFqeB-1wx3uEnxxIvuhh-EbIV8XbK_K5eUdc6RVCOHgVOLt8KYSuQrUenmsQs9kxlPC8XbhzkX_NdyefeVWBcHoGCFo5e_1t7x_R0JCODUe3z05WfqIy_om5DW81MCqPL0blH14whShof7XUUMNfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=B2jupm-rrWi6uf9d0fPsn-gEe4XYnhP6Mafipcg4eOZwMcN0H_GlgVqTnVcrt1DvUDtjDQYpKGRxEqepGCzxewmWMMSVZdJGa9xv_vliF4y6lukHVV0ffj-I4_Zj6NOfrY4SKqA4sqrzsi5ZT-RNbNll1XX7CNjrCK_ADGK6EkaQxVLPz4xEpcjrB2FGGLhfRNFqeB-1wx3uEnxxIvuhh-EbIV8XbK_K5eUdc6RVCOHgVOLt8KYSuQrUenmsQs9kxlPC8XbhzkX_NdyefeVWBcHoGCFo5e_1t7x_R0JCODUe3z05WfqIy_om5DW81MCqPL0blH14whShof7XUUMNfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=pPyEHxPW8rGt_A7-FalFZoCB2_3-_Cx8wCm6pcv7Btc6fbrwKPcIdCizTUPIPx7cRUwQiXYfyCWTPDrk2BBa9c66z7Ge9iWusLVz5L42Ataqj_egj5kexafWCnbnJB1Q9gIfjeFGj3rINrR9yKc3TwkXYGWleyfPFOF_8jjJPV9QSQCR7blTiPsrOSAZgwBu-6nuDY5dk8avjCwuSiq0T7LR2nXIUS5txfB6MieSXHpZgMu91KL-yPTZFShX4fGJHiKZwtrJ3M7-cZm7t1P8jdsvm6c0jrrTexu_K2BJ0T11hLCi33jQ9Bbtq3nMitPYEOWoUvj1nokU5ve1H5kS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=pPyEHxPW8rGt_A7-FalFZoCB2_3-_Cx8wCm6pcv7Btc6fbrwKPcIdCizTUPIPx7cRUwQiXYfyCWTPDrk2BBa9c66z7Ge9iWusLVz5L42Ataqj_egj5kexafWCnbnJB1Q9gIfjeFGj3rINrR9yKc3TwkXYGWleyfPFOF_8jjJPV9QSQCR7blTiPsrOSAZgwBu-6nuDY5dk8avjCwuSiq0T7LR2nXIUS5txfB6MieSXHpZgMu91KL-yPTZFShX4fGJHiKZwtrJ3M7-cZm7t1P8jdsvm6c0jrrTexu_K2BJ0T11hLCi33jQ9Bbtq3nMitPYEOWoUvj1nokU5ve1H5kS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgxpqSYbxfaOHtGjEclJ0xtP0KvkGHNoWLGpPxngXwVjxFxzmup_bAg-2sFduMR1VtVp91yaM0Rjgy0TSgdHj0xjr2UmR8VBjLHS1GmapZaddRsPVX1rjYusSuh8I0zipe23RiafUHHYzAWLv7uqGRPhHPw9HD5AZtDKFUkgU1d2VG1ZUkUi49-ARBSf26jh__SeenHzMDfBEVln2mENtCouSu5cElb6Aos9BB3Y-zDiBCz2eMOL1PUbGsAxyy0aMHQjor3ftQRxjlOsvfpVjM6J0YA7MHcYT_-l_pqYoHI6XpeZZSvxRbXy4gssjZ7wgAA3T3WFPc9SX55bQdIL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l92u__DSG3yzHwbKW6WX0ncrd1pE9Y47i7s_Q0Htjc6CMd0CaNS2q_cKngLjS3hE6Dh3pen344obRTaHJDjATZtdP7yteDqX8Tr0jlRTZbRuVm8eQL02bdH0AvqJVTRVh60adcMNnRGHa6EiKWetxmMff-Tmxe358xjcBfRl-kO1gap2Ay-w-9JsKp_ywYwm8boVu6E69bfef9yalSGsB8QSMugeRaxLkkDto5vH5QZw5OLVjSFWMuzips009f4rdR6pehPAY9gtxXO6usPIStYjAnHRzkQgNH9k4rlNKloiT2ZMrvwmkIoION6N_Chp4U3Wqv9HuAtM2Ie65Pityg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=QAPmF5sLLhmgasBTd14AW7iScc59DVKZhJIeMUUhM5QoLm1vY2-9K6E1KoC2gtGt7Cnnh-RYOsPdrWKREt3C2vfUZ0UCKKxcU7I54Hy4kAUW4e9KGeEBJ4wm3ZeWtRpauRnvUyIqB_YFWi5-svcZ66-ena32GUJGKqhyAaAGAkGqbnyl1fRaHOMtlHCWmphIPsmMCTmx4dKf1AvDbv8fI70mdrehkw1QofzVnyXIcwKa-LYvKfbVlOE4vqPWwF3kyUt3UbeV-O9l1L1VNK2M9fcYupKw9Y-IApBWZkoGJgYVU-SsioBWzdUBMcrv5yjghvZxUppRwj8M5vyBb73T6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=QAPmF5sLLhmgasBTd14AW7iScc59DVKZhJIeMUUhM5QoLm1vY2-9K6E1KoC2gtGt7Cnnh-RYOsPdrWKREt3C2vfUZ0UCKKxcU7I54Hy4kAUW4e9KGeEBJ4wm3ZeWtRpauRnvUyIqB_YFWi5-svcZ66-ena32GUJGKqhyAaAGAkGqbnyl1fRaHOMtlHCWmphIPsmMCTmx4dKf1AvDbv8fI70mdrehkw1QofzVnyXIcwKa-LYvKfbVlOE4vqPWwF3kyUt3UbeV-O9l1L1VNK2M9fcYupKw9Y-IApBWZkoGJgYVU-SsioBWzdUBMcrv5yjghvZxUppRwj8M5vyBb73T6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=rZgocDzDhJ-lHYB5hIwk2JYxLZtUGe70JxAmWx8YsxVCPbcrSSpkEK2wvAzfi22tK5etsziGr1DNTC5rgVhVc7___hjvr-0h-GAwQnUsMpwQwEr1YXr3DdXHXSfULp0BwrEs4oOmqnMDDbbwArjLcgW2umOd89Nn7vVRG61MhEJqck9v4yiRl0WqjTsMrd6Gbo4VE4sE3XbLVV9M83935D3tgFdRZBLd8kel7uFSOQwv4m5BrOpN1k9x4E0auccrT6gs3XCfeQ-gI3DTCGXQi_uTG1wnEqvRDUS-33bSll6Ig56QATKMie-i3BM9i-vRe6c8_XTfAdC6VzOkgvOm2VEpncJcUFDZDkNH-WqMqgrSdHt1YXAO9d8dBEI1ijNNOOmINQ6mZqKkEbQBPHpbFGgNwLANrhU2GByWK724VsmP7KQYNMw1VShvajKN0X2gqALyJS8J0eSt-Oo8WaLyNM-m6X0ddNsSpwuRM7DEWT-3vFME7u0YoTzehiRfJkq_Te4kQJMGqZ1W7XhGyBD9LtLtKNQxVqaeicW4YmtUKX-KVuy2yvFT51DE9m83mL2gwyLdiA4gqwu40bzHd_11aD83s17v0b8UU_EXnDDnj7wvNvtU9dQtWr8GuN_WyaudpPVO8Df91IAw2dv9pzcp5ULZKn2MnXXyoMddBuU5_Co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=rZgocDzDhJ-lHYB5hIwk2JYxLZtUGe70JxAmWx8YsxVCPbcrSSpkEK2wvAzfi22tK5etsziGr1DNTC5rgVhVc7___hjvr-0h-GAwQnUsMpwQwEr1YXr3DdXHXSfULp0BwrEs4oOmqnMDDbbwArjLcgW2umOd89Nn7vVRG61MhEJqck9v4yiRl0WqjTsMrd6Gbo4VE4sE3XbLVV9M83935D3tgFdRZBLd8kel7uFSOQwv4m5BrOpN1k9x4E0auccrT6gs3XCfeQ-gI3DTCGXQi_uTG1wnEqvRDUS-33bSll6Ig56QATKMie-i3BM9i-vRe6c8_XTfAdC6VzOkgvOm2VEpncJcUFDZDkNH-WqMqgrSdHt1YXAO9d8dBEI1ijNNOOmINQ6mZqKkEbQBPHpbFGgNwLANrhU2GByWK724VsmP7KQYNMw1VShvajKN0X2gqALyJS8J0eSt-Oo8WaLyNM-m6X0ddNsSpwuRM7DEWT-3vFME7u0YoTzehiRfJkq_Te4kQJMGqZ1W7XhGyBD9LtLtKNQxVqaeicW4YmtUKX-KVuy2yvFT51DE9m83mL2gwyLdiA4gqwu40bzHd_11aD83s17v0b8UU_EXnDDnj7wvNvtU9dQtWr8GuN_WyaudpPVO8Df91IAw2dv9pzcp5ULZKn2MnXXyoMddBuU5_Co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/degJJUQWjeYCB6Yvk6avMqIWLKJArOW6FBbg6jbwnav8-faB8KFMOn_C9HiFoR5WUZYVZmnLMjZQG63u_Rpgnc6U4ZPsVukncnj29cLpPtZDdwcUI0_6KYWs5BhqHN8LwkY0s3X5mZE67rXPjhMaeFrc80o7_5e_YbFQVZyD5OIG5zMNpiOUXo1Ut_IrMB1Myr0ESO19xs0TwOxU-1Ih74XNRjvxVxaodbvgZPcjq7NSRCpnUxRSDEQGP7MF0WrtcwQQg_mNZHefQ92R3x96cngh_0JM6zKRI_o_LulOj-ttbWLekHxqYyEiB0fyBf_5fkkNlfro2QOA41vuTbYVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cl2OivaLZUWB8eZz3lgi7mgOhaI35M_1sU4uXyuHCZ9KRNNHSzTJSRJ6YZmjtNnShQV9UrEymMZToc0kp4zlr2ZTKggw-7OEv3y7VqyjFhDkcCqGAadzTayQnJSx_EhofrcoBjMEWGV8_bg3RUh_2KslGFE5ioOsumtmjoR_HlgLNoQGNbavKjz72BadlNknhV2DRVuP4d-Or2lySp38dbQiHhNNXeOvNmrMbfiDTlBKzcq5JBRFltPkoyZndgabXYs2DpZNMkJROT9ttQKiAjODaiCMEUitJ1kaM0FuTx80FSuD3gqQZvGoY4kV5PM5kSfdGmj4sv22KcYD5y_yxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VTCc1Vih7AMome5tW8K_Tl6OzezooQmaxIKj42BwpCfnUZAwJJqgFpp4G4pSwhZZf4WuKJ468TbCY0FWU_jDM6r5Ce1fMxDWxPQDveVM8C773G7Cx0L8oDcTmYrAVVNDBUB7_s5iEv25kY4XncEfPQuqa7B7cieIw0d7FhkDFkAwuO0S5Yh8K0z6CTIPInTVOrg2NIcQambj6YTh1KVD7VjdXfowazrsLa9qF2RlP7LFm-1qDMdV4cDGt-aPaHyYX3jaL_b33HdsIhYjpoV5QeNGGlNoBF1tpgEHcfyKj-p-b1MemQcRU-dlXfCTIW8ktYgXQMo6PD7cAWWAKJ7rhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/md8vdVU5XVxiyqYtLCzYLhPLuwMcTdr2913A12FGQLlrLO-Q1EzcZnLj1cfk4IrWAIW_RSz_ztoAYrirjRMuNFbpmE_si4C_IAjImAwvupSoasLRnjl6skCmBjzwRi-6akzKkHU27Nm55-y8JNmtTVvb5GQjSELsLumW7Wh2k-jkXiIOEIx4vCKdg6cqPFulzXOOf5EtjzRUf-l36BDA5fVleGgAcsNrBV4ZRPj44ATPBF6xOoCZaUXD5d4Pbi3L0gJwZr5Aw9-AqBBBF6TzPUfLWuFJYwiny3eiQ26TUFVAU74lUpgE2EyXM2lQPqroa-C69TWz0iTm1bQ3eeMQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ioQQrT5rSaoGKXGcMO4_A7o1tmXaVbimyNhgBbekkHG4bkex6YfrSduM7MaYTDfku3y8OC1Ezk1FH26BbLXNDj4bQ728VqBAniBq9Gs-qduNHDbPeXeeQoyw1UOEE5aD9NlNY2idp5jyAt1pOn0CUkZBInc_f1pDaEf3FHuUbo7fdtgf64zqM8oQbSMSCme-1AZ8IVWFegktHrNlEtEIM2LZHqciFqGjY4RCC7rU97XPz_GqCRo0HCmqwSaVSoLQxJ0SPymPZQNxZnISc6azigV-Zm2xI7PlgqWmMRU66zycLce7NzOpwXmuKx0eAOMEpeNgIwr-UuZOyIhujBP6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HbryptPUdRw6Jyt0fMxSEy29-345UV-OIcYV2uPOGrjx4YFl443XL6XJjjLMEH3gwXCIRIGNw1dGRO6woAhVVeNKQrhxY_ib2yfBJt-kLNGFLJYUiNR1-1IV3aSwEX3NTrythWrL2OlcDwlKPvtGXOfibHn5sSRwEUWA94tcLtYZDlk-bNxG9UmKVR6q66phNtMDQ6Vx7LB8dwyhZVJKmKgqSmmsc4pMZ14wfKB7eR9ICn37QV3P5roDC7iZEU4gfKlgZ82q5E10Xpr9Us53-4WgdCPu6iVuXjO3W-sTfFvPljnxVOh9kPEKVyii91KBFGA8NA0Hug8l63EgJle_xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TWtsoqH_IZeG0UwCsivSOe3a_cihLxmDv0yr-rxxBuxn2AdzZoYfeesGnJqPxmj-a88awwOcTQxAXuBQmrGTQn-trGqBqpIqE9TgjxIqmSS47jQCd5AaBqWirq1wtGSulJBzYck9OG2ngcP9rDJeNzEzsp1nQYsHk71dyfv-3PKKieCyPl5JlVDlurO8uAk_sr9wzkYoGDbHaDDaElLvREBNW3s3den9yaLyt5SyszJp-VNzYDr-gJt7XxeKKZHJapZLSIp9WzZWOuW8jYFxWSXJOdAIFsN0CVN1pIo0XBgOIJ0XOhtFRkloloLYpuiGrxQZnfbj97O69_Qm2c-NXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lLDEONJeJhKJWPxTaG8TJQ1rQ4OkhnHZvQThHdQudZI1Fbx01KJo5e0anG_u2fSOpUB56JEeEmqdci90omK4p1yYlUt1P5rK0-xHj9XFIcfrPGItuIHrljcV_MtLYrIXGu1IzZUVw_WILITIPgFNlaZkCLrSenyFT3fSR_v9u1dKHaSmktym5dTdXOKpGAruZvHZAhFyzdWEoAJCKx_H0td9oJKxDonAZY0yJxxq4E4KDG0j8ntaGIwOpRR8Ye4hbRrq0q48DdGUDqvuScEeHewB4LDvzfdEfqEjgytsQjs2L5JhDd6LYEKxZ2wzBLqBWRYGl6SOOr2xro9Zl-eJyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/c_FXdEcpEMIgJQ58FdPR_z9MIcTvigLv0ReZ8nA9miCwfZnH-tyAbq9ghj7Cdm6GwW5sZ_GODt_FcJkBSflC8LKXNv29KQE0vGRtl63jtodXLEgG_fK1uZEui2mtg79q2bH8zfPWs114BE6gI4h-uOA0ePqFFHGupMIcV3OrdkfmAGXv7kvutFes_FujBvGPge7t56W1v5Izm-nMBwsOYCWDwEhOZYPczG40Uc4PRZXUZM8yCirszUq-F5KT2PDvo7d5Om6nrJ6uKWSft_Lf75aZByTqoYjopAUxfikRRSma3Ol5VR9SsY5APaGNFKpsqeLBQdiuMFX6yLWUAIgDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueBZJ-o1qpbO1p8Q0sjdzq_EmUdai-y3LyGr4MkeCflWH9i2zvpNwsL47F-U30d_ts5DjF8ZMBYQXWe1DAWo5SzT6Lv7Md_xOPce0elP7FboB5MX-44x-daWnSqPaM54mJbwaAs9An9jLMpxbWNbsyrabehfEPuDbt5Li2AGu8g2Z_gt28XHo5UrApZkbIL6f60cvQmzvwSHy-XSLo3oIUNaBdxzO949ufDpOFdfsdS1ER7tXGxQb0qJoRiMsePggHBMQTa7sLj7GHyscOCKCQdwV21D9Jt_noQgKPxuMVpo5S90LF5o4yCqQRzKp_7W1ijI6DQ1cO3QKILvcWm3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAi8-shUhwcDvrsAhIwHFmDeFVtICjnn0-RNjFEzituqt5sz6-8IoKT8Vj9eAvMGbXHrqVb-7ZrxgscBAzpYZtoe4a-qH8ALZNROOZEzJjvl9UkWMDWZ2zmgnXMCCkAyZV4USXCLIyorIOd5A5xOh7YMnCUkCU_nP1xH52-z0kMHL7MK9mDGvSWKgm3-YcI0yeXe0FOfaQkK0iTIUiFI3eU7LJaMiBXdxbxQESs8IhEIxDdyORjXQzSC164fN6j7r2gcPU-tjv2O1e2bONbfHqt9u8-aumy8uGaVW1cPqVaOemMAAVZJCITn5vDXTZ8EsD8jv3FrPXcUCR6INctVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-Vcdyl2Q32b23ylr6pY4ytnTHgOLCRgvzsjela6axjb4UTVU-l2y4NGxbucVTg2v3j0Cx-S_9cgOAEKp5BEo1rqWFEkmgcNQd6IOV7V90CeXLxbOtdDJ-1Zk3PI4yLHCtxR7yIR_OiBdh1bAExPoo8jtWJdMSYj3PH5yQ85Tox_qF5-lC_hcAyREUrRUTebfVhe5zssVQ44Dd0ZZveQ7Lo2ibA5tyCNPpCTcDotA6pzU5ySg-ukaC7KqStzs3VN9_Rdu5SMPQ3CKVCIFxfZn29jahzqjFa_Kb9dZ3dXk9A7OppSXJkUY2M0id5Wjjud9vymxjkLDU0Rt6Nxpw5tjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AcBRP_dZNwiauPllszryQ0vrLVoDrYmX5ep2FDWYohmZL2JNfTJWQuz2OiEvJMhC0pgN8CkNfKHSXeW0VBjAopuy7hqnraSI4ILF1nPCvVb2jSpAzps7CJRY3a8rdwzrrKn2AACMPRAXlLjgjmeVmNapH69sMMWXhWaBYW-HMvpmUS9Y4lDOSqqMYSJ5C2jpblCNJK9Ljw-T1kX5Wk1ImtRp-uqecY6UlF3ju2hJ7dylvrGKIAOqEewoswwgB0Dr_yh2ESrO57-QOzC7wx1VFLr3X0imPgxgQc0dvZ1MMhLmE397anejEUdzLhx8XBkGo8SIRB56AXUETJPcO7dXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
