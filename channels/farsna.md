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
<img src="https://cdn4.telesco.pe/file/fldyJwPOM5x17hiZWuEO6bH7Wq8f60iZcvc01qljUUbhex_jc_galL05S73ryRqoHxT7bGScSDtOYwttEXmiWO_-Kb82fZB1thcxRkn3Q904gzMShbMrpP_WgOVBJT-828PH716NZ9YZgDLdF2dqPaHFPjn9ffMyE4RuCaf8QY4FxOOYGRPjpyfpwuBJCbepgO4VC4RyMI4_o0XCpcx43ukyLPA36uFJHyqvH1Q8hyjFylwZ3BQn2piKf0-lGYrW4JBtrYlWD4uUEVI0KStxKv-zDJbdEV_OsOU7Xlw-4Jn9ob8u_GrU8Ci4tB1R260yF4-XfaQAf1qNMQU7hwKVxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 05:21:29</div>
<hr>

<div class="tg-post" id="msg-451549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شب سیاه رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه
🔹
سپاه: فرزندان شما در نیروی هوافضای سپاه شب سیاهی برای رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه رقم زدند، و در موج ۲۴ عملیات نصر۲ به‌منظور هموار کردن راه عملیات گستردۀ آینده و از میان برداشتن…</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/farsna/451549" target="_blank">📅 05:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf767c5293.mp4?token=W73Q1fqdHCAVRFZSQ0K8mm7p492uhkjCogEesilItK7fmedWMCfP1qv801r0jYuXfrR_RvlFOFwD66pa22aGrSmoAuyNtF6ts5Dt1LbTwwFqL1rkGmG64bDrN9AB-VnwGa1Cj5tXsfjY0sBmmNI0yiAMHjUR-z-rNj-AIEQ7G0c_BTHjiNq6tgHLY-xg4Ty4xhgODJuvtZZ6zKBU8fNVi6k0YPF8mSOHyiQQVJsDl6y7MrCHDdDouRQrRK9pBUmHgSvGikhINsBFmsx5hn5h8lArGP3bMnOuRGCCDt7GqrGzfYf9fS1qjqKjfTE8OrNV8OStp6RZGsiof55GvlwEBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf767c5293.mp4?token=W73Q1fqdHCAVRFZSQ0K8mm7p492uhkjCogEesilItK7fmedWMCfP1qv801r0jYuXfrR_RvlFOFwD66pa22aGrSmoAuyNtF6ts5Dt1LbTwwFqL1rkGmG64bDrN9AB-VnwGa1Cj5tXsfjY0sBmmNI0yiAMHjUR-z-rNj-AIEQ7G0c_BTHjiNq6tgHLY-xg4Ty4xhgODJuvtZZ6zKBU8fNVi6k0YPF8mSOHyiQQVJsDl6y7MrCHDdDouRQrRK9pBUmHgSvGikhINsBFmsx5hn5h8lArGP3bMnOuRGCCDt7GqrGzfYf9fS1qjqKjfTE8OrNV8OStp6RZGsiof55GvlwEBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای سامرا، دوهفته مانده به اربعین حسینی
@Farsna</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/farsna/451548" target="_blank">📅 05:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شب سیاه رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه
🔹
سپاه: فرزندان شما در نیروی هوافضای سپاه شب سیاهی برای رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه رقم زدند، و در موج ۲۴ عملیات نصر۲ به‌منظور هموار کردن راه عملیات گستردۀ آینده و از میان برداشتن…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/451546" target="_blank">📅 04:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شب سیاه رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه
🔹
سپاه: فرزندان شما در نیروی هوافضای سپاه شب سیاهی برای رادارها و سامانه‌های پدافند هوایی آمریکا در منطقه رقم زدند، و در موج ۲۴ عملیات نصر۲ به‌منظور هموار کردن راه عملیات گستردۀ آینده و از میان برداشتن موانع اصابت دقیق اهداف، یک سامانۀ پدافندی و یک رادار آمریکایی در المحرق بحرین به طور کامل تخریب شد و از مدار عملیاتی خارج گردید؛ و همچنین یک سامانۀ پدافند هوایی پاتریوت آمریکا در اَلرفاع بحرین هدف حملۀ همزمان موشکی و پهپادی قرار گرفت و نابود شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/451545" target="_blank">📅 04:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
سپاه: دو نفتکش متخلف با قصد عبور از مسیر ناایمن جنوب تنگۀ هرمز، بر اثر انفجار دچار حریق گسترده شده و متوقف شدند
🔹
ساعتی پیش دو نفتکش متخلف که با فریب ارتش کودک‌کش آمریکا قصد عبور از مسیر خطرناک جنوب تنگۀ هرمز را داشتند، بر اثر انفجار دچار حریق گسترده شده و متوقف شدند. واحدهای امداد و نجات در حال خارج کردن خدمۀ این شناورها از منطقه هستند.
🔹
نیروی دریایی سپاه بار دیگر به شرکت‌های کشتیرانی اخطار می‌کند، مراقب سلامت خدمه و شناورهای خود باشند و به اطلاعات غلط ارتش آمریکا اعتماد نکنند و از مسیرهای آلوده و خطرناک پرهیز کنند.
@Farsna</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/farsna/451544" target="_blank">📅 04:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b4cffa3a.mp4?token=sqfktgQlQHl3wylG-BFQKa3YTvYFvGIrFDww7SiiNWJjB9xyZwmMHtc0hscgoUzwDxepxUn3VlMMYEfbd7l0LWnnxB66URaw_X77mwFbqhjmf5vg1kKGzRMn8tnG53TktyzXmT7eV-B2rUjLSFuaMqZ6TZ49ODQJXa1f-cbN6hg1UicM8BdN5fEcNqXwHUXcNREe2Tx8vxTk8rsASzLnV1PUI4I1PQhrsNTqMZcxFU0_Ck9aUhvoSJlSwbpsUzCA6s3nJK_gBf1Y0tr1jp0DIWd6buig9MRsMAhau49-8bGJ62iaY2ay0S8UOe28WVJ8x2HMZIgpw8iNrDaew_-BOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b4cffa3a.mp4?token=sqfktgQlQHl3wylG-BFQKa3YTvYFvGIrFDww7SiiNWJjB9xyZwmMHtc0hscgoUzwDxepxUn3VlMMYEfbd7l0LWnnxB66URaw_X77mwFbqhjmf5vg1kKGzRMn8tnG53TktyzXmT7eV-B2rUjLSFuaMqZ6TZ49ODQJXa1f-cbN6hg1UicM8BdN5fEcNqXwHUXcNREe2Tx8vxTk8rsASzLnV1PUI4I1PQhrsNTqMZcxFU0_Ck9aUhvoSJlSwbpsUzCA6s3nJK_gBf1Y0tr1jp0DIWd6buig9MRsMAhau49-8bGJ62iaY2ay0S8UOe28WVJ8x2HMZIgpw8iNrDaew_-BOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر انرژی آمریکا: به حملات علیه ایران ادامه می‌دهیم
🔹
کاری که ما اکنون انجام می‌دهیم، تضمین جریان نفت، گاز و سایر محصولات از طریق تنگۀ هرمز، با یا بدون همکاری ایران است.
🔹
ما همچنان به تضعیف قابلیت‌های نظامی تهاجمی ایران ادامه می‌دهیم. ترامپ می‌خواهد با یک توافق صلح‌آمیز به این درگیری پایان دهد، اما این امر مستلزم همکاری دو طرف است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/451543" target="_blank">📅 04:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش‌ها از حادثۀ دریایی نزدیک عمان
🔹
منابع عربی از وقوع یک حادثۀ دریایی نزدیک سواحل عمان خبر دادند.
🔹
سازمان عملیات دریایی انگلیس تایید کرد که این نفتکش مورد اصابت یک پرتابۀ نامشخص قرار گرفته و دچار آتش‌سوزی شده است.  @Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/451542" target="_blank">📅 03:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOYatqRj1CHuko2XJDgFPfFNh_wPI8IPiRr4A-8lR_A7itAvIaj4ICqLJvWQCQJ1vD2szJ_l1LRq_0Y2AuTTCvcvNEeo6vhPdV1fMwBZGD5oqgOa5NWmgBmiy_lDrSEQuCbQTY_f2iSFbIdadm515YE25eseI8JKc1S9h5tBGwSqr7HFubHJndAKRZqbdtDCt1BemJW0z_jL7juPSIpFDU6mA3KMWQM-AMcNzg6cI8Rb06k7OpeG2ASHoh84UDZqpN5yd4AEgvN96V0LeCKbHNfd4yFo5gqInEnmPoWdnDT3g0YE9zaKnaWW71_FdiCUVAsq33AMMlQJBdKEhdtJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار پرسپولیسی‌ها برای معرفی دروازه‌بان جدید
اخباری باز به تارتار رسید
🗣
محمدرضا اخباری، دروازه‌بان پیشین تیم‌های سایپا، سپاهان، تراکتور و گل‌گهر در آستانه پیوستن به پرسپولیس قرار گرفته است.
🗣
پیگیری‌های خبرنگار فارس حاکی از آن است که مذاکرات میان مسئولان باشگاه پرسپولیس و اخباری طی روزهای اخیر با روندی مثبت دنبال شده و طرفین در کلیات به توافق رسیده‌اند. در حال حاضر مانع جدی بر سر راه نهایی‌شدن این انتقال وجود ندارد و اگر اتفاق خاصی رخ ندهد، این دروازه‌بان امروز به‌صورت رسمی به‌عنوان خرید جدید سرخ‌پوشان معرفی خواهد شد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/451541" target="_blank">📅 02:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هشدار یمن به عربستان دربارۀ عواقب تداوم محاصره
🔹
وزارت امور خارجۀ یمن در واکنش به بیانیۀ رژیم سعودی، دربارۀ عواقب تداوم محاصرۀ این کشور به ریاض هشدار داد.
🔹
یمن در بیانیه‌ای گفت: رژیم جنایتکار سعودی با جمهوری یمن طوری رفتار می‌کند که گویی سرزمینی تحت کنترل آن است.
🔹
این رژیم جنایتکار باید دست خود را از کشور ما بردارد و به تجاوز و محاصرۀ خود پایان دهد، وگرنه باید منتظر اتفاقات آینده باشد.
🔗
متن کامل بیانیه را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/451540" target="_blank">📅 02:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bb724c93.mp4?token=JRhbMeo79wHe1m4BZCCdC-zcIQVZqkeeOTSPqdBW9kdPx6-W7sNDwNXb42Nyc8fV8QbInf8NZrldoo4A7gAHk5BiCBB0AU_EB7UCz3ZzbiJJuoOYjVs1XguJHwDBSCGlti6IUrkWCGw8kllF4oLAIEn5ppXU_HElqxggazkLq8dmemTa4Cctovv1hbBxzBKsN1jsR4rnBP_KvA-3lInSLU-g7Ml5m7hht8sfSe6F8CxmRfZ2kQvrl07kntZ4hWO8R_Fi9HVXOZwsUz5Ttw5hdBaLlwUfKSN5aZ1hrT7dXmxMFZn5LEwNzk4_sD0NpU1jI2VaA9c6VF4GWqQPDNl1SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bb724c93.mp4?token=JRhbMeo79wHe1m4BZCCdC-zcIQVZqkeeOTSPqdBW9kdPx6-W7sNDwNXb42Nyc8fV8QbInf8NZrldoo4A7gAHk5BiCBB0AU_EB7UCz3ZzbiJJuoOYjVs1XguJHwDBSCGlti6IUrkWCGw8kllF4oLAIEn5ppXU_HElqxggazkLq8dmemTa4Cctovv1hbBxzBKsN1jsR4rnBP_KvA-3lInSLU-g7Ml5m7hht8sfSe6F8CxmRfZ2kQvrl07kntZ4hWO8R_Fi9HVXOZwsUz5Ttw5hdBaLlwUfKSN5aZ1hrT7dXmxMFZn5LEwNzk4_sD0NpU1jI2VaA9c6VF4GWqQPDNl1SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور خانوادۀ شهید جاویدالاثر ماکان نصیری از شهدای دانش‌آموز میناب، در جوار مزار رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/451539" target="_blank">📅 02:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bdda04f4.mp4?token=BFHg6sakbr5xyd73FnPU-rnrMDcO2hQTswKm8r62xQUTQfEaVp0PZt15lw3cgKDN06HzejxneQr_IQbQIbSr3c5LxvGMM1KPyxViKD-SN9QCCr-YLGegybJ8dijcNgoNrsBa6QDr8flwmr6QfJlPgIiQL96svllegvFPdQyiMDfSs516gPdZH1TDS9N4C7NRc027p2jS2WmUEcJMeR_wV7_KWvBckEPvP6rbTOXH045M4380qZ-ARyRwW2mfeVemj2B88Hl2_iEOzA2ByIrObnkTA5qXJlAOLmDrrDYJW77tUtVkSIRA5P2htl28GhscsR5GOM6cFbKAZewVus7QaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bdda04f4.mp4?token=BFHg6sakbr5xyd73FnPU-rnrMDcO2hQTswKm8r62xQUTQfEaVp0PZt15lw3cgKDN06HzejxneQr_IQbQIbSr3c5LxvGMM1KPyxViKD-SN9QCCr-YLGegybJ8dijcNgoNrsBa6QDr8flwmr6QfJlPgIiQL96svllegvFPdQyiMDfSs516gPdZH1TDS9N4C7NRc027p2jS2WmUEcJMeR_wV7_KWvBckEPvP6rbTOXH045M4380qZ-ARyRwW2mfeVemj2B88Hl2_iEOzA2ByIrObnkTA5qXJlAOLmDrrDYJW77tUtVkSIRA5P2htl28GhscsR5GOM6cFbKAZewVus7QaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سامانه‌های موشکی هیمارس در کویت هدف موشک‌های زمین‌به‌زمین ارتش قرار گرفت
🔹
ارتش: در پاسخ به حملات موشکی شیطان بزرگ به مناطقی از کشورمان، ساعتی قبل و در مرحلۀ هجدهم عملیات صاعقه، نیروی زمینی ارتش با موشک‌های زمین‌به‌زمین، سامانه‌های موشکی هیمارس ارتش تروریستی آمریکا مستقر در پایگاه عریفجان کویت را هدف قرار داد.
🔸
هیمارس یک سامانۀ موشکی متحرک با امکان جابه‌جایی سریع علیه اهداف زمینی است که هدف قرار گرفتن آن‌ها، موجب آسیب به لایه‌های آفندی و پدافندی و کاهش قدرت موشکی دشمن در جنایت‌های تجاوزکارانه می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/451538" target="_blank">📅 01:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در بندرعباس و قشم به‌گوش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/451537" target="_blank">📅 01:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkOntiD47RwnBfIZaNfewfTShx7x9wWFSILv9tvewJIkSd2Agm4FjqVnwRADHPe7fAHM22YMGlGkXg1i0LSvhNVzhXh3CXvPMe9CfOl4LsGDfah_K1Wr9hbStl595GAVBYvUqqPnNYLvdf8j917KsIhGBJ7CKLPCcIF-8fCfOrMtabTZufC2m-4zRvuX-okzGg1smidvL_5uLb761htoIrlP-xP2P_VeqLxx8c2Q1-hBNcmqJBDv7aVjN0RONu_WKoQZcFkjf3ifS3F8H0uiIhIWVgsVNPvPEF7CTaDgOsrps6YF49xwDCc7KN7_3goJ0eJRHxypdt1r4CxLYofi8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از حادثۀ دریایی نزدیک عمان
🔹
منابع عربی از وقوع یک حادثۀ دریایی نزدیک سواحل عمان خبر دادند.
🔹
سازمان عملیات دریایی انگلیس تایید کرد که این نفتکش مورد اصابت یک پرتابۀ نامشخص قرار گرفته و دچار آتش‌سوزی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451536" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f38a10e82.mp4?token=EBVnFSjwcC3P7TBaeUUCLpVCVkWQnFZDOBEdjJQFyJzRKP5DS-qW-PHEfNWpmFZtNZukS6lOVX50mOu7-iO9t7PauGGRaDHRRuh9sBKkPEpTSMD9mIA_i0QmqsxJUaNMrdov2pLlfS2xHeGL6t9aGl8XuiXLq1cb4hOF7keGWnR4r37thWvQsJKcooj0Z7tCkMGDX4GYyyKc0ldwOUmutv5S0wDT_c0zMLEbLNNgFShuaB_et387sAll-RZQt5AGNJOzSpBXX7sDwzAkk7K0BwFqeLV3vV2xZErUQmqOkGiZzsI8lg9rQgbrRXf6-WuPsc3o_AdJVSEMscpgJcvmug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f38a10e82.mp4?token=EBVnFSjwcC3P7TBaeUUCLpVCVkWQnFZDOBEdjJQFyJzRKP5DS-qW-PHEfNWpmFZtNZukS6lOVX50mOu7-iO9t7PauGGRaDHRRuh9sBKkPEpTSMD9mIA_i0QmqsxJUaNMrdov2pLlfS2xHeGL6t9aGl8XuiXLq1cb4hOF7keGWnR4r37thWvQsJKcooj0Z7tCkMGDX4GYyyKc0ldwOUmutv5S0wDT_c0zMLEbLNNgFShuaB_et387sAll-RZQt5AGNJOzSpBXX7sDwzAkk7K0BwFqeLV3vV2xZErUQmqOkGiZzsI8lg9rQgbrRXf6-WuPsc3o_AdJVSEMscpgJcvmug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، ‌تحلیلگر مسائل استراتژیک: هربار که دست ما برتر می‌شود، آمریکا به‌دنبال مذاکره می‌افتد.
🔹
این‌بار دشمن وقیحانه به‌دنبال مذاکره است؛ این‌طور احساس کرده هربار بگوید مذاکره، قبول می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/451535" target="_blank">📅 01:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451534">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fe786137.mp4?token=XeySX-7bTlWLAJzI8d5ljtBMVGna2UimTIallBcMxApvmjJg5DADb5dq9mgD5y5FiOwStBVKd7VFOovP8vZeH98JadUNpnxWvgCTUw32pW-ly7WTLZviw_5IfTvSSlpEpvkKQ4EbLn2kK7nxe5Sm48BLcRTiu46NnO1Ww79QMNxdDHZXHq7Fef8URrI4zusnofi9_L-AlPFng6hpowXeoNZD7ER2YLDJFz3GV-zIcQhMMP8YOURAfx8YClVI1bXCiV-6IkXaajJQ723ZQqMBWas4BE5d_9Z--zOLJlxtAgu7r4zgROiC-Fk8e-DYzaCo1fRaNGp4Z_R1SWo11nAoiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fe786137.mp4?token=XeySX-7bTlWLAJzI8d5ljtBMVGna2UimTIallBcMxApvmjJg5DADb5dq9mgD5y5FiOwStBVKd7VFOovP8vZeH98JadUNpnxWvgCTUw32pW-ly7WTLZviw_5IfTvSSlpEpvkKQ4EbLn2kK7nxe5Sm48BLcRTiu46NnO1Ww79QMNxdDHZXHq7Fef8URrI4zusnofi9_L-AlPFng6hpowXeoNZD7ER2YLDJFz3GV-zIcQhMMP8YOURAfx8YClVI1bXCiV-6IkXaajJQ723ZQqMBWas4BE5d_9Z--zOLJlxtAgu7r4zgROiC-Fk8e-DYzaCo1fRaNGp4Z_R1SWo11nAoiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
یمن محاصرۀ دریایی بر عربستان اعمال کرد
🔹
سخنگوی نیروهای مسلح یمن از ممنوعیت کشتی‌رانی و محاصره دریایی بر عربستان براساس معادلۀ محاصره در برابر محاصره خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/451534" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451533">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
قلعه‌نویی: بی‌وطن‌های ایران‌فروش گفته‌اند که خوب شد تیم ملی صعود نکرد وگرنه ما بیچاره می‌شدیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451533" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451532">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در شیراز
🔹
دقایقی پیش یک نقطه از ارتفاعات شهر شیراز هدف حمله دشمن آمریکایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451532" target="_blank">📅 01:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451527">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmEm22ThC7oMHAhGTLbF94vrkTzOuREwdz7i79mdortn86xL3T5-3VQOIbu-iKhODfLewPs146fBhuE9IXmP-jiscj2fI75HBsxjeWkkhjrvW4y7Y1JiTWRERh0DIce8VFRKlUKvBjxucbRluOq5DRWBDaRDJP9VQoyJwRN_fzuH2yVfCQAZIUPD6cw7ziOANdNry5zcG364UfbzAjl1eXrx9W_-jZR6DVw8vXF200Z0vUZMTtVfSWMk1DPvGxpvPGAEhD-PUX13LOSWO3YsH8PUglUNGu35b0oTETrx9PTOB2ci9O4YSQQFH8NHLU-Ad232swRbLDr9P5lu8zUf4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edO_Bz9hHs6wBXNCcmr3A90M4aK8x2mOFZiQkQREkqxY0ypT2jiI76uCLCzIebyAGRq-I9rbp_hwjPw3gpe43ww5E06OY5Kokxhy4RfGGSdnIIkcQveP4A1hbQmjmasRZZe2dHekCimfBackk0_g-j9pB2yUmWJtwyxKw6rcxL1HnabkPinKdkZDNIl7zC890kA-tZ3gLSg1jb-PzAaYzFqBl10A3ycuHCMEkFlscKBT8Zwcf5zPBPNY7pJjthFDQ7kihU6JYwnSFpG5QHrS67t9d-kBM_Qq1bkshaHbZ96jHtAEXOxsLbuakuEpJw1OqiNOAj9ueYjlDyG0mtOslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRTitjbesHvvluAM3GrBNf387Gywk8QNDB1fdlhsO4Lr9MZGrbRqjskOgC8MGaMaIv0-rw3ag7z9Z28jHZ2RcvM-JEQ4BLW1rUH3vM_JnCilECj5UcIB_Erfi3XOq8BN19amM8N8E0b8bXDv59KYn7qYf7hFEx3KdG1sSv8KY7ome1YIQyd0DIYMlQQ0zBfptzSQx41K72JgZmv3_841n3E-2lEpbSDAC8LKlcnvUlnDkAhNEt9Y-Qp1kK5HtQFOqyw-2jMlnXvsv7oQ9yEZ-M9ad8RNSFXJ7ct7ivEjDyCq__JMH5Bp4RNhCNCFvuO_s2LL0RshOJhqsZg8DW7zMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfHQ-gqRpHRqVYV4taOQnZjjahWV-eX-Bg8ewaxF-e2qb5f33FbueZkGdeciCPTC89CXpKecW3n6YE3mip6cG7G1eSMuq7gQozkHPhKU0OfN4Md1DTxPm6u7CoY-dxRVE5bLi3GqI1LjsWRPz98__2jhI7rYP1nRi5B-lUozXuuFpYzLSliF0-qpC6XsYCYwH2_BPjpmsiIXs9R-StqWV8y9cOiECgSBnESVO5w1PvnlBOx84v7tL8pkTEjkrnF3vcjSQXpnr1HiJnZGq4ZzITCAoo37Mwk_2PBvVAn62ksg0UG1lntMeAbu8Ci8Abm4bFzxzsUzZraJydcgyGKGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqVGL3GxdHHQP3dW1MowOi3TELIde3tQsBS1dylqpDcfroLbb9vyYY_znnmJNRz48eOSxy0tcuXnICDImvI81GP4RL7nV7nR9iL3m0Ph7iIsNNeDrgR2GxoqWpnLzGgG4zBc2e7qdrFi_tgMLGsProDpFJPJSM32OMhAg7n2O3DkGh3nZk7v_DLpU5bjmeKpzHIviCcnrCtURBSdmWsCNsoRUVpVT-EwqoRVb-kU0tsoP-5i3OeQeTz8L9fW-Riq8tpA8WbKKSTs3M7GKypobMjGfS1_cKPQ5HXa_BoqovYUl0gK2NhtmHCyc1Z0m4T8VUSgsu52di107itEf4CPGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۳۰ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451527" target="_blank">📅 01:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451517">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAHPBvCD0VKIRkRRV4lh4S3TZBVD7qFQuGJN4-38MhHVr0Sc-aPuojKd8JqVRwWBSwz_IKOQ449p50UpCJ6MMUuSAT_nIQtaXF6DNETqjzpManYMAAPQjr7Ub0KXg74yVLbKiJZpI1D1oO1LuRHZSSZY2IZaFQwMBg2caZHWJfCE7KEvl80asb1qGk0dU4v9Vjlw79gq7q_Ztf2Rlo6jkbRGQyjz14ZDuSgWHmwoqJPPDgbpJpFFaPs8zbR9hRhQSalzBJRDOHXGkz3yTwYbZ_s6Za4rJ1dXEVQIMRQTu8D6GoMq-Edm4p7d4Q669Lowr1pg8rcKUi5aUdHsVLIGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4klu8mjQbIPL-IVwsTQumfZi1jpIKY0yXQik1IG3k3Dahd3EG8w8kqFQr6iKUj34RmjdI_yFrAGfRCPTv8k3frevVG7otTjttMO7WsxzALSCjblszJdiXsbFahSYTlDmn57n4_W2iDwEd-DfjzfLGj0WcnAA6rJklLsUuIB6uTWlxwpf_uQ0vJW2SWrkfpj66XjvFPWi0WCwlhw1nEbWRgLR5j-qfv6WKok3iYLQaUD1mSaBqcE6OLbf6bvrOhrnNL-MIr3S8c8zpjgKlYNKX4vfi3zKHY1Vu510oF4iMzZpG9etWHRKF1iU1F9BXmCDiRWaZNRhi6o04G22uOpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lD7QtJlaUaST6BufYKyFeQlXmHfcjUrI_LXo8-2A0Hel51Blz7FLN4TrO49ec1Uxql26CDNtDiIVQiZCfY8B9MnI__pOmaawSSv12HUERmmcr1pWUb8UDNNTAIe8jfA2tufne8kE8gjygRgcROfHfd4pLTSEP_p-u1KF0WKKOItfv5Lp8NhtbiDq3UqzVmEXkWA0c1S5QLwwTzwljtrUen9dKzC5TR0jeNRrlmMlALEsxlntLlOMm8-BGWGLzG_SJGohlSFWN0J740atEaY-o5tjp1Aaze3hyNUJLMM8JuJDKI1wWQj5JD75XT0ktINfEAKf5gZBrVxteDi84F2deQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQa_bkgnw3OEjOboKrsPNW4zalmvG1UK7UmISDfkHxO7eMyNcL-OnDS6eIJFDWqN3AUPVTF7fPHM1TPjJWxUdkbUsQRmF6Bf2t4TJQxIgfChoPRPwQQo5wa2qrTcs1NmW4VVin88zFvgm_hE_OB11KeSpNDrhHZMOjXrS4VzADd9JVmKYPmIQqiNDVffASjWhxILvXKolKbPmpCAijbDmGgl1w39kuy0-mgB3H72aApQJ2fdGSBRC9knJhMJn6ugBL0Wvt-zAudXil2AucxLSYNdmad68d1DpiA2XKawr-hb0_En4o9A3Y-YdtVPQZK2Rf6yn9SxewJYcOxBM09Y0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzy2BClMEUWxV0NkuS7HMbZOxt3Ct1dBD9BAvUU18-aHG6ckdjq3gRfLjOil9V9MVQA5Uqhc0vCNPg6LoeUkS9dgILgRsBhPoxrURJZnNLiL2htyV4A9IaXTmLFIPR2qQein18JyJTOVZcQB9hZr7b-LWbcsfw4lnF194a6PeNq9R-k7QjjUFYNNqOK5tgkHciIAtolYG8yUNYf5HcBAeM9vr7noukwt5CJEuZopZacp1ZgEOtYh3M119uFagPhdqg0nR50iEkbNb92RA27j5q5_P4KmSV8K4YzE2h9-hciIvOmKOW8Z5L2wf4EGJan2XhzquNf1k1aIcKa7nFECAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9liGWnlbQQL8IS4N4OfC_FwS4cwnu_-A9i9X9UzsRsLRTpxOwMdJBbOuNtTGlQETCSn_Gnz1WEU-uJUvi1WfNrjYbZqdYW6zs8b_AOYacB8QcoRG4KoqBIj2q2n2d8kO33HR9z3ZMOCt_sjFYs5hINDQ0QbDyDaV3y4Om1r0ecrEznlK7GFt6mbJUzJZnfTPh1B_PuUvIZ8tW7o6mPaDwskA40hEUTB1WjAkYjnu6t8nuR0uzw8sjLCaX7jvCkkw-h2sLThIxjqdHVdpJ_zPUAhmrbgjC_cMnecdb95_U9R99hKOlTnR3Zx8Drb1C8xYCCPOVb4DL4vcM5N8oaY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMXDedMW2YOvySzD28OmqvfWxtRNshjsXEqxsiI-spIJQruymn8L_4Dt9eO5vSP171juQCBX-fAxeZN9zAq3YH3r5UFr0epComRQYYFL-eJOLbuJeF9jYQhHdcFc2RLeJz2OdBruQqYTFhX0ZEvYrZmjsyL_zANViXNFCTyvyHeDWx_L0o_9tP0usqcOOxT6z6ipvOATi1yTLpDImygZOpxC6GKfNzA1Q73WEu-wPWsDt0DLMqq58y16t-ul8KKMnZJLucISD0q2f1Tfe4jf6LIFjFU1Fy3nSuNecCkEFwBeMZ7SA6wgtH53zURDR9tbnWwrqMZ31vNMeeQave1GNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXWxPFYdshXk6tJs5tlKOwVW7KbCjdvSDcloIM3pHZ-jHLKOFXGM4liT2bTpoXUh4hiK-RI_wsTUaLHohs2rwhkVQIQic_EZZNnrHBoTLxXTpYff6Jc9gHW6xwUv619B0kNMu4tvNSJ8zB43SA1MwtFJud-Dg-grmnm76cvRJJAde82jt2eHSBxnA3opOpr8pTp-16-2U2Qm1l2TmFyxWtdLmXiAaLuibaUPR8EwDT2UPxwbIHujeSsOTMJsTvSNOfSkRhqy6Qc3ZWUKgEfnfHTJbFeRGrd1m8gk9ndSq7YuC_Tky0zuo-6nyCpD9MlRqJzyeBu51Xjzdud_MP0mXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mC3pHiB-YTGy3x66dZCtC44_lDIdJMZvPTUcaKXPfC789sr5_RtI8HK028Xam0_q3-qqVlGfVq2tcbkrkZMQH9K2g-0sxTm-n2BlGcxrFW5nrR5xidmSbDnUE4_C8ScRN4NCI9WGgWja_UQN70FvgU0F1zVHjiKOGRMe137bVoqZVoWKbHKq9bQbU8Agz3A1mvaD3kE_pdrx7U0dNt6FpmJoRxa0xg2C0_Qy7bWQTokM-HevQUMGAYuW8svbTGiAPfg2ESXA-Ai_GjHLd-T-8jolCI5erIaXS9KJ4peDjP_R4Rm_01h_XzmgHIhERjzgyF2_uXnQzJBfyQ3ORfae0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klInLFrTU0tfAS24AdhwUcbwEqXCuAfcfFeJ6Wtx2pQOxYpcPPGGpiKz5c5QdR656zZV_1VAJg2G-Lm2EbzTjbck8qw12l9Zz0uEuTQ5uOUShvdVGk5Azzj5oECfQfcanDTpfCwxNlnZSUpx2S3XqmkYkNHe9Y9L6l3rWXNTlu7cDC7V5vAX6gt9poDKFHHmT9HdgdWXpFoVr2qAeh8m6fwDNbC7L2P6W_5DWtjsbhrQ_bnmO1sQaRuAQMQOOqzEH3iWYLfvleOkb7-p3frWS5Rt3NDgVscdLvaR09pxbPSPFGfywonylCeJLc2B_jziN88bIe3Xn6LtzneE0dmgHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/451517" target="_blank">📅 01:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451516">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d630841d55.mp4?token=ko516qgZuRQQk9ceZL-ED82TYxMQvv0krDWpBYLmc3-da-edEq9rZ_I4xlaxRXBRqOg4pmjMHEYcAkKtcQVelLun1QSnVWWjBDknCjhsGcJ2GSsyCs8n9ceBNOc2s2nrO_5yZoWctL7BrZv3Muj7fBawrKmxBRApzRA2y8q1NyJ64DgjQv2NIo-HB6EulgpSDgZqA0TMwcIOARh9yg16tvwS95N7xlzH6YeOBgN57c--Zmc1IyIRv5_z_PzEDazHEMebv1PS-ctlEDAUcFlraA3fUN59hE2yP6J08bA4jRAQGXn3Z17L349xa93B-y4UWo-26N_-JfFywBCbBfPPxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d630841d55.mp4?token=ko516qgZuRQQk9ceZL-ED82TYxMQvv0krDWpBYLmc3-da-edEq9rZ_I4xlaxRXBRqOg4pmjMHEYcAkKtcQVelLun1QSnVWWjBDknCjhsGcJ2GSsyCs8n9ceBNOc2s2nrO_5yZoWctL7BrZv3Muj7fBawrKmxBRApzRA2y8q1NyJ64DgjQv2NIo-HB6EulgpSDgZqA0TMwcIOARh9yg16tvwS95N7xlzH6YeOBgN57c--Zmc1IyIRv5_z_PzEDazHEMebv1PS-ctlEDAUcFlraA3fUN59hE2yP6J08bA4jRAQGXn3Z17L349xa93B-y4UWo-26N_-JfFywBCbBfPPxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: چه اشکالی داشت که بی‌‌وطن‌های ایران‌فروش می‌گذاشتند جام‌جهانی تمام شود و بعد تیم ملی را نقد می‌کردند؟
🔹
قبل از بازی با بلژیک به سعید عزت‌اللهی گفتم چرا از نظر روحی به‌هم ریخته‌ای؟ او گفت که فضاسازی‌های بی‌وطن‌های ایران‌فروش روح و روانش را به‌هم…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451516" target="_blank">📅 01:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451515">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی ایران قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451515" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451514">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34e0b7a02.mp4?token=stX6RsTBBU2IKzbwcpJ0H5snxecCNxSnzKij5zJfS24iQExkQCeZm7IX0BugKtFE34TlnqBRmvka_HKCFcLPhYeX90FjL1K9ercfeqrs__Ix4Udq2WCy5heBjHTxuBGUuiwdYu1krtMGNclKNYDRyDUwCAzUjzjr6a6LJfRQiNrBPRRmimsbgH1naUVWc-jsBhZlWefsTwS-GXDfvTel2fJOWnRWyppUU4xecjAdNmqpzv-v8S7gkvacMl2ja-WZXol-yl-fb5R5brviaMYAEY2QjunWLxPiUikem-lh6-kXPdK5gGHdXGshg_RJRcK2NVVNCaIBllvtZGgMOzSrGBRqNV6mleNV-gh5NRdG-U-v-fOblRLk-i-A4yjjF4MYb48HLASXLLH65PT7U5ET6fPWASPuAYk07iZRm2Convqr0BEO2C2tN0IClug3ZT91drGhBz5RCYjRqTrL_TILINR_61mkUSjBl16fntpuU_AV0AGrh1SBe3cGNMVIT4D2XoNmRQhzmTII6L3LOdKyN_TjJR-Y2MVrYJIXmzx0J7OleXHsBJkm-CsA5dbI3wiPOznLFwJx4aXs2n9-cIW1D4kVnsSxHzsH8ApLaULx5qTCB9TMzGlxOINLuszyjRollvUp-uPLSDRHTj6MBDjqHPblzkIVJX9pkodcptL2UCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34e0b7a02.mp4?token=stX6RsTBBU2IKzbwcpJ0H5snxecCNxSnzKij5zJfS24iQExkQCeZm7IX0BugKtFE34TlnqBRmvka_HKCFcLPhYeX90FjL1K9ercfeqrs__Ix4Udq2WCy5heBjHTxuBGUuiwdYu1krtMGNclKNYDRyDUwCAzUjzjr6a6LJfRQiNrBPRRmimsbgH1naUVWc-jsBhZlWefsTwS-GXDfvTel2fJOWnRWyppUU4xecjAdNmqpzv-v8S7gkvacMl2ja-WZXol-yl-fb5R5brviaMYAEY2QjunWLxPiUikem-lh6-kXPdK5gGHdXGshg_RJRcK2NVVNCaIBllvtZGgMOzSrGBRqNV6mleNV-gh5NRdG-U-v-fOblRLk-i-A4yjjF4MYb48HLASXLLH65PT7U5ET6fPWASPuAYk07iZRm2Convqr0BEO2C2tN0IClug3ZT91drGhBz5RCYjRqTrL_TILINR_61mkUSjBl16fntpuU_AV0AGrh1SBe3cGNMVIT4D2XoNmRQhzmTII6L3LOdKyN_TjJR-Y2MVrYJIXmzx0J7OleXHsBJkm-CsA5dbI3wiPOznLFwJx4aXs2n9-cIW1D4kVnsSxHzsH8ApLaULx5qTCB9TMzGlxOINLuszyjRollvUp-uPLSDRHTj6MBDjqHPblzkIVJX9pkodcptL2UCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: یک عکس از چمدان بازیکنان تیم ملی منتشر و بی‌معرفتی کردند اما این بازیکنان آن‌قدر محبت دارند که کار تیم پشتیبانی را انجام می‌دهند
🔹
با همین عکس تبلیغ کردند که ببینید این‌ها چقدر خرید کردند. اما واقعیت این است که در این مدتی که در اردو بودیم بازیکنان…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451514" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8ebr0xkt_cynyvq0ZADTpNXEdsVKQlOEfXbiSocMtzOhq9X5oRxhKcZROsHiTDRla7DFzWsJ0IcOJxjnCfKbueBbZrD_4tK1LtfyQwmeQ72D8xGgcQ_5jn2N21mZ8vg6Y_APfTOixs46DaqCpIsWOpxgmraGcyRl8QKVcOzYJxSgeSzvia9xxuMrL-XDl-mMz0tJ9ysjjrNbxacR5pIUXJHLX99EOVblraRi6sSeIUeo0n5cyJPp8Wp1hklfABZyKi3TUXAiMx8Iw5cZRqAUzcFXdCEYPsGYrh1o9LAdIJoakdt756Ii0blJKmauECsUGlNM9BQc0ivvmQ7XbI3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزبانی فردوسی‌پور از کسی که آرزوی عصر حجر برای ایران دارد
🔹
«قرار ما با شما، نه دادگاه، نه بخشش، رقص و پایکوبی روی گور تک‌تک‌تان» این متنی است که علیرضا فغانی در دی‌ماه ۱۴۰۴ منتشر کرد؛ اما این تنها استوری‌ او در دی‌ماه و حوادث بعد آن نبود.
🔹
فغانی که پس از…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451513" target="_blank">📅 01:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فرماندار بوشهر: صداهای شنیده‌شده در بوشهر مربوط به فعالیت سامانه‌های پدافندی است.
🔹
تاکنون اصابتی در بوشهر گزارش نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451512" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی ایران قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451511" target="_blank">📅 00:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF57_iqMTz1e65bUypDLgbNEsE-xv3wAG58h7i1UoqJK-JyvAOpnuR6kGC91YWCsGo7fLMvrMuHyvYQSh2rP-KplBj3IMJdzpqnNepcWvvh69QQ44KR4dZ6f210hq66gxYXdEy_onf822jVYUABlwAc8rLVfniLHL6AFslCK2c37TTCs5mEg2v8sKSwShXMpUkz-8_GcHBX0eOSZxzJgY3PdOucudYKfuNezD1DlVX8Lu47BSIbdf8vTQRU3-MSk6Xr5OD3sIvKPL6YF4-LiByAH8OegNIhS6MSeFEGqrqIw62pnhPt-DUjZutrFpiI6vV6Ku_UcIjUTbhmpPd5V1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام ۵۰۰ تیم درمانی سیار در مسیر پیاده روی اربعین
🔹
رئیس سازمان بسیج جامعۀ پزشکی: ۵۰۰ نفر در قالب تیم‌های دو نفره با تجهیزات کامل و به صورت پیاده در مسیر راهپیمایی اربعین حضور دارند تا در صورت بروز هرگونه نیاز درمانی، اقدامات لازم را برای زائران انجام دهند.
🔹
امسال ۱۸۸ موکب درمانی با هدف ارائه خدمات سلامت به زائران در مرزها و طول مسیر نیز راه‌اندازی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451510" target="_blank">📅 00:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d151b2a3c.mp4?token=LlTBIh0UKTPKEcGIzzBNciJb6shotX9maSAZIT7CqqDGyzGg_e7aCJhDHdLsq1_sw3GAuzXNQrzJAOGOOJLbAKmos-DiKCT0W_UYeVuC1AWGomLBAzEbKDIeuxqeZWbYGOETHsENZSprVtu402xWcQjSeuQ3zuxt69FohbA0brLfWW9Yyn7UGvcTmn9yAZrG-l0Zogt4Ge-Vz7tCQt8mHC77Buz7nSbt1ANyBL7wZrDb10AbJfrF7bLTkBRFRi34KH8scH17dRVC7uzyx-fQtoecrNB4JV5CP8zslpMfZ6ShmIHwyrxHAuTjsBBt7m3bblufS8MpcFsxkAt_glxduA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d151b2a3c.mp4?token=LlTBIh0UKTPKEcGIzzBNciJb6shotX9maSAZIT7CqqDGyzGg_e7aCJhDHdLsq1_sw3GAuzXNQrzJAOGOOJLbAKmos-DiKCT0W_UYeVuC1AWGomLBAzEbKDIeuxqeZWbYGOETHsENZSprVtu402xWcQjSeuQ3zuxt69FohbA0brLfWW9Yyn7UGvcTmn9yAZrG-l0Zogt4Ge-Vz7tCQt8mHC77Buz7nSbt1ANyBL7wZrDb10AbJfrF7bLTkBRFRi34KH8scH17dRVC7uzyx-fQtoecrNB4JV5CP8zslpMfZ6ShmIHwyrxHAuTjsBBt7m3bblufS8MpcFsxkAt_glxduA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: فدراسیون فوتبال حاضر بود برای بازی دوستانه با اسپانیا ۲.۵ میلیون دلار بدهد اما آن‌ها حاضر به بازی نشدند
🔹
حتی برای بازی با پرتغال، پورتوریکو و مقدونیه هم همین موضوع تکرار شد. @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451509" target="_blank">📅 00:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار در چابهار
🔹
دقایقی پیش صدای چند انفجار از حوالی چابهار شنیده شد.
📝
اخبار تکمیلی متعاقبا اعلام خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451508" target="_blank">📅 00:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0a05251e.mp4?token=Slujzz_Tf6JMSJUSGHJzAI5khYuAdqRIEOenYyFINYPhwMuLx8Euvl-88CylTFA6qxCGBBOnq3dZDD4AkFJGJgwuiuMuFu1flBKev9dLKDEfbkSFnA8UXB_fq_JpoiyhFgBPSBtEYVQiw7ytqLb3Hh8mKzArKjwnqWo3czpPkaHdzFsFSjNKeoo7cXhM5cu4EdD2e3WXWCv9ADDiUn-y4zFcTW_9Gl2cWFZ2XZCa6U8RY74LuU8bhooThAsKOd1I5XvwzZNR7FGtuzCGZi-BcHMlX7MaWmbu0FSyRyQyMXCcxuinnotlBlOYpE72DtWtK1bQiWZ22uKAjx1MzFbDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0a05251e.mp4?token=Slujzz_Tf6JMSJUSGHJzAI5khYuAdqRIEOenYyFINYPhwMuLx8Euvl-88CylTFA6qxCGBBOnq3dZDD4AkFJGJgwuiuMuFu1flBKev9dLKDEfbkSFnA8UXB_fq_JpoiyhFgBPSBtEYVQiw7ytqLb3Hh8mKzArKjwnqWo3czpPkaHdzFsFSjNKeoo7cXhM5cu4EdD2e3WXWCv9ADDiUn-y4zFcTW_9Gl2cWFZ2XZCa6U8RY74LuU8bhooThAsKOd1I5XvwzZNR7FGtuzCGZi-BcHMlX7MaWmbu0FSyRyQyMXCcxuinnotlBlOYpE72DtWtK1bQiWZ22uKAjx1MzFbDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: بعضی‌ها بی‌‌وطنِ ایران‌فروش‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451507" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار در چابهار
🔹
دقایقی پیش صدای چند انفجار از حوالی چابهار شنیده شد.
📝
اخبار تکمیلی متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/451506" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451505">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbadd4515c.mp4?token=IcMDE9Zc0Y8pU879XoxQ92uGwh0Oyh4YMfeUvQtkgBK1XQ1jqV_eqp-S_wUdHaWCzpcREbqInizIq-M1m4l0fX6LHPoSNzTUWL6zAM57fJxZE40VDLx_T1Wv7Eo4I54A86mgFkRi0c3m5dSFMQ1MqAVhW4pBYRZ58cWZSaSYglkhry4vIgaF4I1LIGoKWqhVptrgSt4So3NViD2e2xmBL7HMJQwM8ToXVMPYnGdutnAZ597hCVzM3IwjwDP0xMkNzeHSCgKwM_B2kufHLb-oHR8Zp3Ix5iakH9d2S3310KRxeQfaSy0ARWRt7TYgFgKlarY_1-yJZrvv6WCtkvEkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbadd4515c.mp4?token=IcMDE9Zc0Y8pU879XoxQ92uGwh0Oyh4YMfeUvQtkgBK1XQ1jqV_eqp-S_wUdHaWCzpcREbqInizIq-M1m4l0fX6LHPoSNzTUWL6zAM57fJxZE40VDLx_T1Wv7Eo4I54A86mgFkRi0c3m5dSFMQ1MqAVhW4pBYRZ58cWZSaSYglkhry4vIgaF4I1LIGoKWqhVptrgSt4So3NViD2e2xmBL7HMJQwM8ToXVMPYnGdutnAZ597hCVzM3IwjwDP0xMkNzeHSCgKwM_B2kufHLb-oHR8Zp3Ix5iakH9d2S3310KRxeQfaSy0ARWRt7TYgFgKlarY_1-yJZrvv6WCtkvEkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بندرعباس و جنوب قشم
🔹
حوالی ساعت ۲۳:۳۰ صدای چند انفجار در بندرعباس به‌گوش رسید.
🔹
صداهای انفجار در جنوب قشم و دریا نیز گزارش شده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451505" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451504">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqi8ElQE4GtlCgxDoTwbZXkMshVCEdvD9zX_Vpn88zC3xp5AWscnXV0hX9eEo8UhpxYOKc7Jf5i1qSAFvoVE7fUDSMiKvjOBRmB_SVWxUf3nhiF9lFCTROs3raIlVVMGBwYZl3fcAAZlH181cLUO2xO4_ANFN8iE5AzAD4FGaTBWG90F33EVgxioJgO6572_wF2VrMfaHWW3wtG5Iwxp7pGondsszaPjE_HF9KNuBFGMCzw8YrQu0pg7EuonocjHUghBSgpw0qVZgh2DpTHRt2OskH5AHmky2rDm1mm5LeSdlGgqNjleczYxLhECCRuVeMDack1FTqPcgZeMwfJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم تشییع اعضای پیکر شهدای مدرسۀ میناب
◾️
چهارشنبه ۳۱ تیرماه - ساعت ۷:۳۰
🔹
هویت این شهدا از طریق آزمایش‌های DNA احراز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/451504" target="_blank">📅 00:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451503">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52baf9baca.mp4?token=hww83RpKNyTJAi6JQfkN112eO_Z6mb2Y5Kpiu34JSurAuuB7pADcUVYFWaeWZb3sX9TIaL7qvqkg0zEuK8GstTUwihn3tv35DQLqPkqUVEexNY8_iz-zlRQKBp3mhrvADBXgIznOh3iWFD-DZzALhMoJTcgt8nhf1rOGexGcf7KMyetMCcw6ahYeLWwZTpstu9FJFB3ClOVZksbvMvEd6DGn7iS8nlTRsSFcnZk_dzBEbf03wQZWb_TmXaeoaDi-kMWr9TpYQRxlatlN5MX0FKJlgu1-MXx7oaTKM7Jl8moXJ3x5Zt9Cq50s96PEMu0cNb6pk780eEhN23-AN_toIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52baf9baca.mp4?token=hww83RpKNyTJAi6JQfkN112eO_Z6mb2Y5Kpiu34JSurAuuB7pADcUVYFWaeWZb3sX9TIaL7qvqkg0zEuK8GstTUwihn3tv35DQLqPkqUVEexNY8_iz-zlRQKBp3mhrvADBXgIznOh3iWFD-DZzALhMoJTcgt8nhf1rOGexGcf7KMyetMCcw6ahYeLWwZTpstu9FJFB3ClOVZksbvMvEd6DGn7iS8nlTRsSFcnZk_dzBEbf03wQZWb_TmXaeoaDi-kMWr9TpYQRxlatlN5MX0FKJlgu1-MXx7oaTKM7Jl8moXJ3x5Zt9Cq50s96PEMu0cNb6pk780eEhN23-AN_toIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: شرمندهٔ مردم و بازیکنان هستم؛ ما می‌توانستیم مردم را در جام‌جهانی بیشتر خوشحال‌ کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451503" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451502">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c999740c35.mp4?token=OCLMrit14jMaLex5NOJwPYdNQUKhO3yse408Kl-RE3GJpcdUy7xPJz4bQpLgd_I-vvk-5MPpRKoOrYcePt9PVGAT0TLtBsnpQgcWfhlIVUwHMB4wZBtymgfzO4r8h2_J3IUk98LqBqkbM_E_OBXSLCyJ9L63vRHN-EjILku2YsGBRguFjj2Z-0Af7TyXuRhaoCCHLfGKTIY3DKxxeqa1IBPrg3AHtonqD0y6HXPCmb_nC93TEoTRcAWvNIgTUqeHAwaxLAQwrOkFu4OcQk_rqaKajfc4BW0Zyg5qISaIvZXtAqLjeagqS6jMyjMMbgCizgDrHc9vOPa8YSGS9KHKTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c999740c35.mp4?token=OCLMrit14jMaLex5NOJwPYdNQUKhO3yse408Kl-RE3GJpcdUy7xPJz4bQpLgd_I-vvk-5MPpRKoOrYcePt9PVGAT0TLtBsnpQgcWfhlIVUwHMB4wZBtymgfzO4r8h2_J3IUk98LqBqkbM_E_OBXSLCyJ9L63vRHN-EjILku2YsGBRguFjj2Z-0Af7TyXuRhaoCCHLfGKTIY3DKxxeqa1IBPrg3AHtonqD0y6HXPCmb_nC93TEoTRcAWvNIgTUqeHAwaxLAQwrOkFu4OcQk_rqaKajfc4BW0Zyg5qISaIvZXtAqLjeagqS6jMyjMMbgCizgDrHc9vOPa8YSGS9KHKTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: شرمندهٔ مردم و بازیکنان هستم؛ ما می‌توانستیم مردم را در جام‌جهانی بیشتر خوشحال‌ کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451502" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
تصاویری که گفته می‌شود مربوط به شلیک موشک‌های بالستیک اتکمز توسط نیروهای آمریکایی از کویت به‌سمت ایران است.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451501" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451500">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بندرعباس و جنوب قشم
🔹
حوالی ساعت ۲۳:۳۰ صدای چند انفجار در بندرعباس به‌گوش رسید.
🔹
صداهای انفجار در جنوب قشم و دریا نیز گزارش شده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/451500" target="_blank">📅 23:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451499">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAuLYew-8AcASbCpp5uI_pspgVaCEvfArb-piGNkpIbRtrtTXM7YbLY9JMyHB6z9B3BFEiAYPXK9qrPuq73hzYIvBQL-8ZAXkNGg5izlGW4kvmsJatUi_UNIg-7m0216ESRN-XbwkvAPeSAVZa7G0nlyEOuXM_wG3ndOLNJqBJOnnrMTZ3hwEb47yTYsuwQYac-bxPyc9JA-VgQaNlxSfQN03HU7YnyP7enRSXzMAeTANyFouzYXBV3gcMYmL1Qug09MoF7qcnvqt8LiUlKWm5kxckRDybVKrJN25nmGTaY6YGkFh2iS8VEEXlYm3rY-2US4kDT17wiGH4VMdz-hug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: با دستور ترامپ، دور جدید حملات به ایران را‌ آغاز کردیم
.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451499" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451498">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
خليل الحيه رئیس‌دفتر سیاسی حماس شد
🔹
جنبش مقاومت اسلامی حماس از انتخاب خلیل الحیه به‌عنوان رئیس‌دفتر سیاسی این جنبش (عالی‌ترین مقام) و جانشین شهید یحیی السنوار خبر داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451498" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امتحان نهایی یازدهم به‌جز هرمزگان در همۀ کشور طبق برنامه برگزار می‌شود؛ امتحان دوازدهم بدون تغییر
🔹
امتحانات نهایی پایۀ یازدهم تمامی رشته‌های تحصیلی، روز چهارشنبه در همه استان‌های کشور، بجز استان هرمزگان، مطابق برنامه ابلاغی برگزار خواهد شد.
🔹
امتحانات نهایی دوازدهم هم روز پنجشنبه در تمامی استان‌های کشور، از جمله در استان هرمزگان مطابق برنامه برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451497" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451495">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4d55e81f.mp4?token=MtpulGZ78r5IzXAYQFKFjzNzjCi54fVyMnbNp_hcbmQbVe8Q_5sI6l3Q8XTH_0gMoFBE5RMlIpym8GWtF-9Dp_rwZNY8q6Nn6HWQfw3Sy4WP9GmCcqtoCzlLl9e5tjNT1X4iiF5NSY40U6B_R_NZmQddC4DvD8znbrxPZ6cTsx3nnQh3lDu-TEow2Nu-F5iz8u4QYiTV4XeE0sARHnpj8wYF8I-VxWshBM5B3P8ZPoaLO_zJdaEUHjWyUW44kuP8uiHgO6aG8jTnuvfg2Mh5BGXVd031d6FnaoGtwIRpotCZ30hUgqTobdJs8pbkIZyNaA4inkMkQhORIgfrgPY4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4d55e81f.mp4?token=MtpulGZ78r5IzXAYQFKFjzNzjCi54fVyMnbNp_hcbmQbVe8Q_5sI6l3Q8XTH_0gMoFBE5RMlIpym8GWtF-9Dp_rwZNY8q6Nn6HWQfw3Sy4WP9GmCcqtoCzlLl9e5tjNT1X4iiF5NSY40U6B_R_NZmQddC4DvD8znbrxPZ6cTsx3nnQh3lDu-TEow2Nu-F5iz8u4QYiTV4XeE0sARHnpj8wYF8I-VxWshBM5B3P8ZPoaLO_zJdaEUHjWyUW44kuP8uiHgO6aG8jTnuvfg2Mh5BGXVd031d6FnaoGtwIRpotCZ30hUgqTobdJs8pbkIZyNaA4inkMkQhORIgfrgPY4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۴۳ عاشقی در گناباد؛ مردمی که پای عهد خود ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451495" target="_blank">📅 23:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451494">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
مقامات آمریکایی در گفت‌وگو با سی‌بی‌اس اعلام کردند که در حملات هوایی ایران به پایگاه‌های آمریکا در ماه اخیر، نزدیک به ۱۰۰ نظامی آمریکایی مجروح شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/451494" target="_blank">📅 23:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451493">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شنیده‌شدن صدای انفجار از حوالی سیریک
🔹
دقایقی پیش صدای چند انفجار از حوالی سیریک در شرق استان هرمزگان شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست‌.
🔹
در ساعات گذشته برخی منابع محلی از شنیده شدن انفجار از سمت دریا خبر داده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451493" target="_blank">📅 23:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTveuxNOWzWAzDt8g1kWapdhkTfQcsJMoey1RV0-RLamT4cF5lm5wU6kgAOlzXGojq8IAelcDCMdYZuiWE4HxyR6sT_edglIe7ymFrk2FgkdszErRmGp9Ivc6_FdhxguQgdQzwcX1L0lM3sQ8yMRsAK9XoZuodzMKQTX34suFmTTkmPA2yJJD0yP20v8kCaYxPnvvB2xao8xeJyqAGP74Ey6OWHga4ljwJ8sNh4gvHqPLp54jrxWuJc4SpZRPqCjQ2pGmzIaQZlML28b86wGw_Yza21OErhrFhCQ4Ql5NFPDE9dx1-PanQpgi5EVKluGjnYwzT7oclZ7Z06hu_iKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvZnerozIIqa8UA5WALnhT9e58wQ3ESkyVTyLlRKW0SHP6-H-agYv_heWvvQ0xvQr__rrtZrSeiSccIZ5c5y_IgnjTINVWied30BOwJkPFxQULXKGbdbzN7YFgIQFq2mIoX7rhhauZibmkX1CQDeNiVyNIetqKzAXunRt8PWoSUHhDjwnkGj6LuNioDTWu-tec43yiXPin_Ja937GFWbiU0MlE5kcIBaM9BMj0P3mETqsrCUogmrJHUmDPQE-OAl28_o5Grj9zxx1HQJ2Npnzw3t91BNv1e1wC0BU5YxbSMw0gS2zbYztq3yX3Yxo7M6xqfXauInztLoPBEr2fUitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQuHvHnmcSN1QL_PUoLF5FJGVZi1pKfkiw0Azg7iJRPDSnkjjSTmJSbI4WNURemE7BfNft8ndbtlpKZmPN0540xa3d_HO7osqRwDhmXGEK_LBVt2G25TvSvH3AR5IhE4Al1mDw8R6M2sdOHbcjIQVAraO_L6PVHeRrgjQn8Jsl3Z4QPidHyjTfLSlXpHKFBnudRtzBa8Da19H0Eg0RvNIr3N2zjLsGbBBjOC7jDYjk5OnI1uRsa3lfgH0efbECoeNLntXjSUPCruYHpTPQNXqtgxg9JkhT8NTO5B0fPh0_EqznCKDn-IFz7R6bucEe9KW6xynfrTceP2i5eotSwNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAmsu0AGeL3uEEHsUfzKMsWlFJtL8t7hlKHZkdi4rFArpWi_FXtlOJ-9byIWc7Xe006NwE_LAYmfrParQK1YyBRKQY5pKBvMRdKlgQff8IUdSIs1LIlOjGaDes0Smc1ZtEbYFGWBecyQpbIv3lDDfm9AQUKehn2LbazktSjYxy7Yb45UAJj_U0eknmiJmxm3AJZ-gxf7g1xw9zeJuPwvdGl1IvNYk4UFf9XWAAR5TsPb2hAzWuVRXXvcS7PNs2Brkxlp9n9KPb-GFTLK78d85v3Kmi8ypgoENCCDSwRm_Q4vurSt9WncWVX3L3CxY55KxaIvAuKdmu8NAk-crsrvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVGSS1zQPhB9FRc6BhGH0Z_wGvlZktI17yZigyvMZdrqqFCKOtFnBHYzbwznjxPGtT71PHbrcEaaxhHh5a1kPRJPMoc1MtLZpVf_iUkwqOy7ZxlF9Jec-PzmJmGpz0Ls2jAJKzwGdG5WiVE-do_TUL7S22xR1kxlAzWFRfgOJpJkYISBWr05EccXVvLTM8BgTr3tD_tzgRv5AGwWOO1JkMtZYc5YN9QJdJZrL8dz1BDp2pZD2C18wj7oC7ZW421dwKyPsLZXb3jojoYtlIhxtk66wKSpkMmNmvKk10htBqg-cgym7UXY-7z-giwhMPcoS_yxvwXCJnUkJ3Kug72ABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLFVYDWjXyZeZLUT0vtpZuyIzJJCJPefUIHd9FxavUrm8enpfd8MJyM6O9oWODLVFwSQ-MqnMIvkqwzFP-yvTAcoS2R5A6V4bonAohWsduGOw0IrVw_sJDjG34ZQhKyMO9LuTRBXHBv84-vFwcUAnyjpSl0A89Jkg_p6wjHyXh2TV5Xn9MQXfGBKly9jw7uTit1GzbPK4HOs2ay9EW6rAdBbzwO1wLT21pu0J9UjcMlTCBK8lK-SaEvgLaVw5_wmpxBr8-cG6RVXu0XH6G2uXApdOXPI95J2tVMMpgXrIoDUR9sjhLof7br0kRwHjCQBmCNLbc3OsBY-lCjUxyMmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEWs3dkdkPybUuKHLpPvJzqFI5C59a7q-kaZq39d4vcIGHg42-vg7QUmL9uYWPEYI1d9L86s0-xlBH2xYtPd2_tdI1cPEEfqmHnNf0R7FN1AIxSDBT7fcYlQjcRQAGrGa8CMgQNeU2PPtCuYKvDUODEWBl4GodixdHEfm13n_zLnODmyGZWz9zuCJIS2mJ9pWMwWSOykldMiIYT56wjQZYNfuImg3Tx2BhmoRJVpISB9C5CSGIhxQR5FFOdWRFZnZGnScpHN0VvPrACpmYr_astytucyZTYEFa31CVika0GcuvD3rwu_iypTrlZC2xIciWy6Jn_j-Wd1bHK85cd71Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرواز رنگ‌ها؛ هنرنمایی بیماران پروانه‌ای در مترو تهران
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/451486" target="_blank">📅 23:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5895b61c08.mp4?token=SHoqYaJjVJPqY1-h96W0Z1Ae7nt8QNxVfjO8U6QbFjuwUMaxmj5RMuE_fizD_MPPlTQXDDkSRdIsE6MJrV83XWAcKUm9iLHKSXviKFTFofI6RZ5H2uGyGaYK_0I2k2yu7-dETS61E960ay7JOlLY1HFCBxAm0KpszHc09vwg93j9d7ixNqBN7yZQWwFLy7nHqRuvIPw84-dXcRz8HKp1dSl5PBAjp4ORe6uDnyCQbqNuMs32N4c3oWbKNVSth_8tDd0DiaxX_aOsv2zceofOwv5xLXYK6wYvDNbTs5wfB--AKnYGW5AHDo2m_M_UfewfNNMBkPbKoxSfBGBctoSqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5895b61c08.mp4?token=SHoqYaJjVJPqY1-h96W0Z1Ae7nt8QNxVfjO8U6QbFjuwUMaxmj5RMuE_fizD_MPPlTQXDDkSRdIsE6MJrV83XWAcKUm9iLHKSXviKFTFofI6RZ5H2uGyGaYK_0I2k2yu7-dETS61E960ay7JOlLY1HFCBxAm0KpszHc09vwg93j9d7ixNqBN7yZQWwFLy7nHqRuvIPw84-dXcRz8HKp1dSl5PBAjp4ORe6uDnyCQbqNuMs32N4c3oWbKNVSth_8tDd0DiaxX_aOsv2zceofOwv5xLXYK6wYvDNbTs5wfB--AKnYGW5AHDo2m_M_UfewfNNMBkPbKoxSfBGBctoSqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهپیمایی پرشکوه مردم بجنورد در میعادگاه ۱۴۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/451485" target="_blank">📅 23:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea6b80764.mp4?token=rR_TSvfkKPBTpCrfm59fX367Xo283fjV4mylUcvqzkLsPyEdq2D4-FX2Vtsis5OGucNjN1s8RbVw3oGL1kMoAMracFMk_KuCdEXJqGpWOaX7QroNMn-yb_MPVGiQQ2xcm04i5b6DXguwJFjm8pCGPHk719P2Tcg_8Mej5GPO7EqKl9Qihew_Ps-GmDIWyJMXu_2mAOz_vW6HeuJjsT3OAo7p-j4Eo0jDcizo2Pm86l85yMrQ6PWAjuplo8lK8LyYU_jhspBbqBZvPS8_zMPDc0CrwC_fJZ5B5jIPvCB_UAN0-40rS68MKUa6GDO1V21wC7ZeD2hxspna0yi5JnD2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea6b80764.mp4?token=rR_TSvfkKPBTpCrfm59fX367Xo283fjV4mylUcvqzkLsPyEdq2D4-FX2Vtsis5OGucNjN1s8RbVw3oGL1kMoAMracFMk_KuCdEXJqGpWOaX7QroNMn-yb_MPVGiQQ2xcm04i5b6DXguwJFjm8pCGPHk719P2Tcg_8Mej5GPO7EqKl9Qihew_Ps-GmDIWyJMXu_2mAOz_vW6HeuJjsT3OAo7p-j4Eo0jDcizo2Pm86l85yMrQ6PWAjuplo8lK8LyYU_jhspBbqBZvPS8_zMPDc0CrwC_fJZ5B5jIPvCB_UAN0-40rS68MKUa6GDO1V21wC7ZeD2hxspna0yi5JnD2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ستوان‌دوم مهرداد پاشایی در حملۀ آمریکای جنایتکار به تبریز
🔹
پیکر شهید پاشایی عصر امروز با استقبال مردم وارد زادگاهش مراغه شد و فردا در این شهر تشییع و به خاک سپرده می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451484" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d61070b2f.mp4?token=A60ln6-8kgzNzhcYpdbAxa22flptUq3lbfP6b0em6z-fVL2S_QW0IheI39QleTve9Ba5oOuYH7XA2ipjEi2hcJKbzXE1xHaQZZw2PNRw6tDd57hgokbn77ktboPsfaLd81esFwdbvA8qApylHIB7eecEXK39ETv3gSg26YYhVWGmtW0-5SlTB9tE2KGDDeip5zhfBv0w_POEnbuCBEp94QnbTsn4uFBLT7z1qZwLaeLOxEiQZnbeHIzzuC6xT8EiRWtw8B_08Y6g6QfAoaGExqpG886MXzUaPXu0GHh4f6WiCpB1lzRIcb6KN5MvYkge-aTrUk4r53KJRQSRAR8WOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d61070b2f.mp4?token=A60ln6-8kgzNzhcYpdbAxa22flptUq3lbfP6b0em6z-fVL2S_QW0IheI39QleTve9Ba5oOuYH7XA2ipjEi2hcJKbzXE1xHaQZZw2PNRw6tDd57hgokbn77ktboPsfaLd81esFwdbvA8qApylHIB7eecEXK39ETv3gSg26YYhVWGmtW0-5SlTB9tE2KGDDeip5zhfBv0w_POEnbuCBEp94QnbTsn4uFBLT7z1qZwLaeLOxEiQZnbeHIzzuC6xT8EiRWtw8B_08Y6g6QfAoaGExqpG886MXzUaPXu0GHh4f6WiCpB1lzRIcb6KN5MvYkge-aTrUk4r53KJRQSRAR8WOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها دربارۀ آزادسازی دارایی‌‌های ایران هم کاری انجام ندادند
🔹
نقض تفاهم‌نامه ازسوی آمریکایی‌ها فقط دربارۀ تنگه هرمز نبود. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451483" target="_blank">📅 22:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تعطیلی ادارات منطقۀ سیستان و کاهش ساعت کاری در سایر نقاط استان
🔹
به‌دلیل تداوم گرمای شدید هوا و وقوع طوفان گرد و غبار، تمامی ادارات منطقۀ سیستان فردا تعطیل و ساعت پایان کار سایر دستگاه‌های اجرایی استان به ساعت ۱۱ محدود شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451482" target="_blank">📅 22:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pB0aIXPsU9YqnrAOvA3LwPNISgHM7DTBabu0LgHRAGWFXQMGmujgriEht8shAzAoqsmQrTJGIwiQK-0KAdZ5FpPMkwx4w_FjlnRXuIPPVN7YMMP5DpJ8J-O7f5I92q1IJP5eFKbrygyknLuSTAl2uQFUWlqaUOs4o_BuJXFiqKn3l1sfGtVUIGh7RcdoTsAAl5MPyXmGwmEDMcw4IbZEfOeSFK65IEJwPYgrS2SFkIca1FRgQeCr2NQSdYn7ecTAe9e_QEbyh1CvaBp1zvD6e93CVbFTrdwkCyGp4t3DQlbgASRfoj6mv1m0Ils1FVvddyQkCMZmOHDU9MHQyeg-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgAG2gxhKkUHwPRsbAY6u54r-6uqvkWzKFGYqNyg1GTs02BHMLf2hjjpUDOpGckOSOstHWekzP2DacoqRwxXlRBI2NSpPTkf9wHU3W8a_v40mTb8c6Nv0sjKmiUDTzXYvqjh8ThoOuZ27Ie03xQSel4k7u2eF8C64XZeuac5CEKeR8oy6lOtwjLW9B87dnqkYNBzkTAVVJgx6I4mxx8S483sd3j95jL5XAB51cvZ3XCJg9z6xrn4dn_qxuDBZxeqOZ-Ofiw5bfUjTlA_APdh3DzMqEH44fjfX_Tjy_c4CK9PaTNreiNkWNtNtdeKattIKEIAmZa97vWZ8fiouLN_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJAEsYRRnvZzz5Woyi-WqWLnW6MH3H3H7iGsAfOSujlsRmplmLLRJ36L15A67zja-A8ho0pQ0iRnewMnBgMS4ZYpXInc_Zaf8Iazazt7SF-R_ktQRddDMpKKXyQRXOUym-1maJxAaWDjW0dV5nPovVG5F-k94m_TnF3hqk2AgvX-SWs-MfnMf4oRY9jwAZdLLK8OsAnpE_vyi1smkjYKJ3wSPbHxuvBTqpNtKimGDO9dJ7TChUjO2W_-9Ds1ctfq954zTEtamV3pNBvU__Rd56k0KGhzRnD2l04gv9wR_qR75XkNFU1ymFBuIc_NEOCgyfcsYPvmPxGh8FCCJu20iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQuTtc710k0wdNLCLuCYC2Be61e9_UDQPBvyXGzSjWqYgwmDrW2jh0BR7k-voZ9Lks5vWXMC-0-Mxaj6s02LkQuqWV65URw5q3TiyODC7IZbsR00kTQSeXhXEwqN8wppFb4WTO0o0NSwhy1_NewczLTTyVxP4eE52mU5W3PZ_NEZmc2qju2R5WMsFiWRkWD_r3msb5pxwApf5XoUKaI5PQxbqpf6qoW6cYo_uEpTqMsTj--VPlNXJbQ5ViYQLT4HS4tynu0spcTm0rpHalWpUYD4Cyif2as08In4MU-scvr8DlszSTOWTVrqdBUJ9eijyEEFCozfIe3RX8EoDLXLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSmWYnIKDVtwf18Duzu-s2IJuK31SqF-t_zKzi4WNtr4MCchK4bc7XK5o5y45RYPeuvfj6F_NPFI-zcrM04sWsN3ZZneAPJCWr_OnIHDVayrIzICgamYE0LdyynWTAjPnnJG-FMgXaXnn5MMvoyH_RrUyE1vv2MMHRtw74_yO1rOULvRaF63397oACeVLu9GDwaJayjh_vwFRfsVmyrtZtOWwoN1XjsZcJlW1UhEI-Yj84_c_2Vpnj8R1BbIMTbXhke1pPmunBkQbDMSgVOqAa_EHPStnz_NsEvttANq7bzZPqRwBD14tdNb0MMlYdT5u7CG3LXg7RPO9loCREP0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mddzZFleDVPTrkBXXHxZkxN-4T8QreI7e3WN_aKIx51QqYfCVGlfbHw5lZJp3WrjN0iymWnJmip_7gNcPir39H-vZDgWDIGJpau6eBoOIZegwmN0tr8d3T362SFLwUWrnq4NiZ5HIJqx32PPz76cbgQ5P6FH3r1y0FfYnWJN5RzpGz0zSDKdJ6xtXcHo57mmD_q7c_42ImvkNb4XPWl9O_Zo0XGpRpyhUucu5soA8cPcMYYL-CMIvogp84OVyVQA4MfUTTEDXLFYYvUg1QaxjD9-tgqizBKpzjzAcCq1wiXN-3BwhWutcjKzrJ9p_SqkhOp4hKr21umEh9cLqh0lJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvJjoHsKIsd9CMt3D5OvSUo0mvuVaiFAHf8zqLGaoAw7ohMD4rJC2eX46YpnTVZJKptCByM7f-BAHs8KJHoHeM0fHeCFy7OJAuLoi0mfSVAQF-wfKcH0DeUvyKk5NlF6QtMaoulUhiP_cODp155OqtV1nPMInUgPsBKmko3nyfbxmNpQi7KvwCxO0ofgO21fmnHpyZEwx5VFFcUpM4QaLlRoOrXO0QJ1ej9fg8OBmxrAdYDpNhjRaDJyM82VxL7fXqOI9ayCj1pVc8NiiNRPxl1Zyc8DGTzVFeDc3IPRQXLAHZ67wEyi9k2kzxfc5eTWg43dkgA1TC1zzKW6WhhtTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زنجیرۀ انسانی هرمزگانی‌ها در کرانۀ خلیج همیشه فارس
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451475" target="_blank">📅 22:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcae8d7d02.mp4?token=ZMZ6fB7PAVHHjK1oXJUtmj7gqKr1v2AFaQiAhrlx5POZ0EvpeWVvtO_VDCH0bvZquhBocEOvfuA5GqYHs3nfZ8x_EgupL-_CU6TRwOM6qzprWLRITmn_EEw4fW9qpJgNXQHS7YVeZHgknrTI4YsM4ZJ0XBA_0xmplemkzuk33aUFl7DU_L4PWYioPBR8ogC7y3gcG6NQXYx_Ejh3GZ1oZ7wADMGX2p8gaxeOEl-CLH8fzNy6e4hWUv62GilI0DeYo0pxojJXuHBZOaR6at5vSx60jCw1KerIYOT-ZWMF3qdd1Am54Ot9ao9RnlKf3FenplYP_gqv5fNewY-SQueasjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcae8d7d02.mp4?token=ZMZ6fB7PAVHHjK1oXJUtmj7gqKr1v2AFaQiAhrlx5POZ0EvpeWVvtO_VDCH0bvZquhBocEOvfuA5GqYHs3nfZ8x_EgupL-_CU6TRwOM6qzprWLRITmn_EEw4fW9qpJgNXQHS7YVeZHgknrTI4YsM4ZJ0XBA_0xmplemkzuk33aUFl7DU_L4PWYioPBR8ogC7y3gcG6NQXYx_Ejh3GZ1oZ7wADMGX2p8gaxeOEl-CLH8fzNy6e4hWUv62GilI0DeYo0pxojJXuHBZOaR6at5vSx60jCw1KerIYOT-ZWMF3qdd1Am54Ot9ao9RnlKf3FenplYP_gqv5fNewY-SQueasjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باقری، معاون دبیر شورای‌عالی امنیت ملی: ترامپ بچه‌سوسول نیویورکی است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451474" target="_blank">📅 22:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6e659fab.mp4?token=W94fXHmj2o7TyD7ADB-_M8CJ9pCh-0dUWE9hdlV9BZjo1z64XtixZp2xtIEZTioccabOPFRsWPV150CK-mnfpiDy208NzyLN-SDbR8zNGvg-PTyD0X1zRWAqdzhkOm_pqqwzSddc_NE-DkQdOjix18VD4TbhvPeKvn7XRfGAO2ZgIb2l44M1nhBidb-VoObJznonlSM00sGwGskeozt3jETXs1XNIg5sUzPEpjvsJESH7lrmukSmS-rEr_CJj4dhzKkhqX4vtrtlUn5LzAi32F7zv4JkH5aVj_8vT3zsQ5MUF78nY-4fRcI_SvzXmL2VbdE_iEkfL3TXCVnShwdNgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6e659fab.mp4?token=W94fXHmj2o7TyD7ADB-_M8CJ9pCh-0dUWE9hdlV9BZjo1z64XtixZp2xtIEZTioccabOPFRsWPV150CK-mnfpiDy208NzyLN-SDbR8zNGvg-PTyD0X1zRWAqdzhkOm_pqqwzSddc_NE-DkQdOjix18VD4TbhvPeKvn7XRfGAO2ZgIb2l44M1nhBidb-VoObJznonlSM00sGwGskeozt3jETXs1XNIg5sUzPEpjvsJESH7lrmukSmS-rEr_CJj4dhzKkhqX4vtrtlUn5LzAi32F7zv4JkH5aVj_8vT3zsQ5MUF78nY-4fRcI_SvzXmL2VbdE_iEkfL3TXCVnShwdNgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهالی یافت‌آباد تهران امشب در میدان چه گفتند؟
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/451473" target="_blank">📅 22:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq99A1NduNsa-TGSGkDm7Ou75tcXODo6oW_5QVqzd7eq6QQeaNyfisRNx9MjPHSNw49mIAe6ZQTlRESyTaah-C5HESltCb58UrI99cDtHk-5sCpEs9Nr8Mj7PKQoqWDSA_u_wY7FQSgNw9zguz9xAb5Mfafj_SUWaBRN9sRCZLFspPj3OTww7Jeui1SyKh338n87BQ3AtLv50OpT6MuE5JF3UUWial_01R2bP4GjtazU7Zm12eAIC225qXnAt7HOf9txFaOdXcsUcx7yZxLl3fQqEw16PdxaxbPxQ7hWuQ4HieeLvDvUz2ljmUboX2mfAuIuYXsfBl8ALHZZ-WL4Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه استان کرمان: یک موشک کروز دشمن آمریکایی در آسمان رودبار جنوب رهگیری و منهدم شد
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451472" target="_blank">📅 22:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
منابع عربی از حملۀ پهپادی به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451471" target="_blank">📅 22:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaf299c7a5.mp4?token=iSVKVMT4MWTnwWwMKWCbNwUNvXKZPBKZ89SUQfMJREUD-BPjlitmkzIBHwXxISf7z8jeDUcutlJInJGo1rvigyHUweJ_WXkfSoWlCqrqlqcs_tmEwhMsjqVWnxNqPelOBgpP3TS_O8R1jDXSA9STZJTT6IHo3ZeP3CgFZJ-YEnG11W6jcIzrs8ZUhYnbOBftQJapBE2oAIs5qCeSF7i0IEUAkt-sD2l6fmlbTEoOSTVXRS81XGB4tARi5Gy6vUCuB7ZtBQLzArhGmBoi8JZ7F0jgScdFHTjZWsmkHVK07RGo_59YUy3ZgMiSXzAyuIqtFRUcJU2d1VS-9_Rg4nyqDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaf299c7a5.mp4?token=iSVKVMT4MWTnwWwMKWCbNwUNvXKZPBKZ89SUQfMJREUD-BPjlitmkzIBHwXxISf7z8jeDUcutlJInJGo1rvigyHUweJ_WXkfSoWlCqrqlqcs_tmEwhMsjqVWnxNqPelOBgpP3TS_O8R1jDXSA9STZJTT6IHo3ZeP3CgFZJ-YEnG11W6jcIzrs8ZUhYnbOBftQJapBE2oAIs5qCeSF7i0IEUAkt-sD2l6fmlbTEoOSTVXRS81XGB4tARi5Gy6vUCuB7ZtBQLzArhGmBoi8JZ7F0jgScdFHTjZWsmkHVK07RGo_59YUy3ZgMiSXzAyuIqtFRUcJU2d1VS-9_Rg4nyqDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری مردم تربت حیدریه در شهادت حضرت رقیه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/451470" target="_blank">📅 22:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=DnmHAf84g6Q21aXHcBkfbw_5Aa8vTsw51WU7g45aME6rllEehbUKHh7XnF2305XYFhOUtiyuf38FutiCr1PgOnq5dXqrN8G7UBdOR1UKgZGM3roU6RcWHEPbE8fpClMQ54DWEzvL01EqXpHAPe9_PK6sXizgxMYLZkAI5aI0NnGxvjJpEScUuofJ7eXkvMI1gMPlgLfc9GbnE9svGRWnLVWEOgl2nc8GqdVQoFspDzGtNFl5bWPqgZ_JFfR4I9TDExNhtEkq6nswIoMr1M_6SF9fDmgRWXm3zdsVfnv91ScnTQhjG8dxtG7Vl3aM4c9-fcSinJ4z3dy2bpHDVVaNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2ecc4084.mp4?token=DnmHAf84g6Q21aXHcBkfbw_5Aa8vTsw51WU7g45aME6rllEehbUKHh7XnF2305XYFhOUtiyuf38FutiCr1PgOnq5dXqrN8G7UBdOR1UKgZGM3roU6RcWHEPbE8fpClMQ54DWEzvL01EqXpHAPe9_PK6sXizgxMYLZkAI5aI0NnGxvjJpEScUuofJ7eXkvMI1gMPlgLfc9GbnE9svGRWnLVWEOgl2nc8GqdVQoFspDzGtNFl5bWPqgZ_JFfR4I9TDExNhtEkq6nswIoMr1M_6SF9fDmgRWXm3zdsVfnv91ScnTQhjG8dxtG7Vl3aM4c9-fcSinJ4z3dy2bpHDVVaNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باقری، معاون دبیر شورای‌عالی امنیت ملی: ترامپ بچه‌سوسول نیویورکی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451469" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451463">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-7eH-kHU0uKwfmFihi09u3HCNhQnv6o5SnScNrAJIxpiQp8qblZVfROhWbPvlvYW1cCH31KXSNb2miIBd-JKfkAKvIF5N1tp-7bdpa-XXJ4V3Jkn-8AieQo6ftG6YXQ1TF-JOxmE1t3nTTUc1rXw8k2f2NQTxcC8Hox3zetwRZ_Ro138zF_KGk2-05hJyfhhIIrwQe8zvokcgCCAIRx08sadkZSIuJUyaPvLqsCAmnRwxLg1UjsbZtYj_ylcxai1wN8chx6suLwUWPRaa_lcKi0dDQV5A6vtnL8rKC0veHbh0pG0J0Xadx0ublI3uB4ZsUFy8T_EAOi5YV3Wt5zdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFm0ZghKM5LOssKGgB8j6AmZP2L3uuHsmw1IYObwYua-XS_MQCYTeaFuHMXozSJ9mXWxZ4w6tb285YSTY-ZQ86BPVEL_Iv3Q9W7niG5RXlKVSaGdjhP7PTb_HJGVR1eBEY1xpxhTfp7o3PWxZlY1ytNvpTtyj0UOdgdpb6XVbfRq_b1g3ihHXQajp_gRCGpDa_VZDre7M-KmjzxatEu5eA1quGU5somQuG27qDuEGW4Q0arEangcm42EreGz01v2qvxVrpTkAtrP995Eo_KSH7hVzGZ_sdBMUT3obHwnRyPKeQZQ4l2FUokoRfL088VJwFWvMdXVJ-mA3llaBOZo7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFBluV5-4ytStd_cI7uMOjIn2pK6SqvYY14BeUs8L9ZAGTYokxHTcPJD2r6ZUtWX04ch99PuKOf94R5fed5imuJE0pV7pw2BOnY_ssR7ij__oTdetZ17RiSeQ5Iyw2R5BkQ-8t9BRpS6vs-VoXoCawnYKe7YFPpk8PY2FZ0KxijZhyK_YEilCsqb1cIIl3xmuYJT4SbsiKUQGt3H26n9QQWzaXXKPjuKWmNXmbrTzV6geU0gcRp4w1yMr1UZQCd3alJsR3MrUr5hFRFnnENjTqgQ8gTg0D1RtEZJOQ7gilc9SsKqMfidzfGTpg14x8ab0Fpon4H6RlXWR-ig7YWvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHQMK_BcJLHLPwR-aU8Gbw1A6HiiAZL3M04lh1zZh2Cm9mdBqGEOG4-V7ksdp-mfBc307PtZ5pMqA2jCADapb9sBxeD--u7RQe4PTnrMdOTLXZnza3bV5LKxT1jZ7j-tMTN2jSDqSDNh7rVvmW6OaS4Pf1wixmuxCxqDHxVA_Arglcc3RFyD1xXYSEAnSSWwMqiFJ5VzjPhwNSjYgb4Spf_41s5pNbMaV3LwqhDsHHSOaatUfrgbqXBSDRFyPspCeYD69w0hyeBwDiOww9iudHdnXfw_SqSG-UVPy_Y0aP2Y33_g0WXO62r3001HG5k-OiKKJwcUfyQlZQ9laAPwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-onU2O2GVCkO5gYptr0B4IWVdMhJ96JCDdcnxpM11I4ZxH1RuDg1A-BfwWED-E2A8o2Mefz_kU-LCCNI83P3Zhk9obLA3qkRC6CNtWxCkgRn0-na9jnus5Iiph77wa90kk9JHWof_y5ruQtqSoXR6huz6NTMcVv3KQVoMKKD7qzfI5CnZ6o7UWWFJo1c1cj9XCtAwnJ0kLsApc45YdSWVsPHfkgKKghpFY4s_5rOMhk4dyuSrD30jfrhA-gAy-mfKhP_QqCX3KkFQ9EUiK_781PYITmE59QcM24g9-KZvFTClDEn1SQh1thmjIYDNSmnGiSvTAGFRrg7haifT3zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ffhb8eCKLQU2GHPsa1PjSvE_QhioaHMcqmb_LiegppVFDKZPyk8LTRA5iumavd-8osX6n0jo_w8LCptbTjp4q7PxuprFp6vVRrLI1ILz9XUAAv1LJtvvgmLIQeV45vMpWeZZA9gHfiy9Wdp8TYle4HrrPrvjtzRwYra4dRvfxUVDYW26VO3ulgWy9P1EnEA8Hb4xqMqfFFn9A6TDxqwHRP6rHDUf4DBRpo_HW6FVYdkPExbCyZgfpuk1cpXqewiu8dEQ6DgZssoz7Ysu1CFurx4mU_WXuinARCLGm2JtKe4YaS54iiR4RBtrMhralG_pR83X7FL0lOefbQJPbwEBCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نصب پرچم عزای امام حسن مجتبی(ع) در ایوان طلای امیرالمؤمنین
🔹
برخی علمای شیعه هفتم ماه صفر را روز شهادت امام مجتبی(ع) می‌دانند.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/451463" target="_blank">📅 22:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451462">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgGlQjdgAUKwfXctNJPEG5RDy5BcYUIqZQS0hqMmG5U52f4Qak_vElv7niHCXH19SF7T407i9oo-4RtVJaRvzPcJBZ7aaSgak8aBJ14x_REEZN9hPJeF56B1MeON5qb77o3cVb93kWXquqB0B74dd8DP0uk26T-PwZC98bkF-hsu724QMLGoCyzl2D2ZMdcL8MnEKyIV2W4ATa_MYhkdcHJrwJfGI9g2tgVe3wHBKcdmrX1hcP_0Wud7pNhn_yi2cjUvZwcalI2Y8PFc7DwwSZ2hsmQec700xzDAN2DGJA0-UPeIN22ns9SSBlfbIBqD2FBlR90X1p9j6rdotCee5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
منابع عربی از شنیده‌شدن صدای انفجارهای پیاپی در سراسر اردن در نتیجه حملات موشکی ایران خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451462" target="_blank">📅 22:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451461">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvHJ-dV0LkppUn1WVBsNzbQKOIGpNY1QoUQIrR11eI1217nGs-Bvp4c-QF0syAt7f6eGwrVpb5DYmKmRG5rBe4XcuOhYkuZIgcWF9qH--wK-5w5Ul8tk5V_msQpuQ2kLcBM37Wg60Cq9e_ZgxdsFcaLs569-jkpyX8z7Ap27tnojSeIDmYeuPST9Bcglb6_15W1OI7ggdPY_kP9iDcg8D5KWtMpX7xPB4kkXsMdQB8-V0ANUOik2TRU0R12Lo4DKg2sbFZA2vRb1j2UiavT8k_3Vfg8QEFp5lP1StsbIN1p-i8EeVxUIkdOYg-GdPTg59H4DHBzZ2WbJWPaPx1ztgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر راه: سالن فرودگاه بوشهر در سریع‌ترین زمان بازسازی می‌شود
🔹
دیدن صحنه تخریب سالن مسافری این فرودگاه بسیار آزاردهنده است و بار دیگر نشان می‌دهد ادعای تفکیک مراکز نظامی و غیرنظامی ازسوی دشمن یک گزارۀ اشتباه بوده است.
🔹
با همکاری همه بخش‌ها، بازسازی سالن مسافری فرودگاه بوشهر در سریع‌ترین زمان ممکن آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/451461" target="_blank">📅 22:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451460">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451460" target="_blank">📅 21:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451459">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a39fa6d7.mp4?token=feZyaSrcHMIWhneDfP2dJx3NmzEwH9TBSueG-jsH7QonDKpJe4ol-w_-tbeedzqglQ8k4kQPNdu9XULTHTaau2MoTkBgInMJIUxWKKPqGkIR2fBPUruRI36wB_7VcWr3uY6IfQrNZ7A6JXx5uSWbo9yfLfuixxIp1UEvRYxhFbsYI_b96VedLrsifh90fz6ZtxXpcybzeuILO9m3ZjxdtoTRZAlwtwX6KsdIowbFPcpEKQbk4kWOrPea4bnn6Jo9aOYzpHXAtWbsu3JSM99YmMhUErAB3yVocTggnzGxf-p479B8py5n43EPKEF95kGwiOmJ1S5X18zRXUjS0qWWoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a39fa6d7.mp4?token=feZyaSrcHMIWhneDfP2dJx3NmzEwH9TBSueG-jsH7QonDKpJe4ol-w_-tbeedzqglQ8k4kQPNdu9XULTHTaau2MoTkBgInMJIUxWKKPqGkIR2fBPUruRI36wB_7VcWr3uY6IfQrNZ7A6JXx5uSWbo9yfLfuixxIp1UEvRYxhFbsYI_b96VedLrsifh90fz6ZtxXpcybzeuILO9m3ZjxdtoTRZAlwtwX6KsdIowbFPcpEKQbk4kWOrPea4bnn6Jo9aOYzpHXAtWbsu3JSM99YmMhUErAB3yVocTggnzGxf-p479B8py5n43EPKEF95kGwiOmJ1S5X18zRXUjS0qWWoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع رسانه‌ای از شنیده شدن صدای انفجارهایی در بندر عقبه اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451459" target="_blank">📅 21:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451458">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
منابع عربی از حملۀ پهپادی به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451458" target="_blank">📅 21:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451457">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850e96d1ea.mp4?token=vdKUENOBc_JUoG2Pnp8IRPUUz_OGtnEgDvraCobqlvZDuAWDhiPK-IK_rXJ8WGsYYdrwNuVsadqFqPEYBw003l4hae8a0S5sINnR77gJ-L_MjhgQNzrppvywZFDxsH63NL9RVlUr3I_XMBPFg1SAX71wBfOWYEyql4TdXOcV2jy6MSXIDv9rVIJ7ngNJ5MhxNUptRsGsIF_EAE7H60NhdYdvJlrq-3uswGCL-RR5_-l5K66ekflzOtJX6o0egRdtuhfHVL488_n2RuikTyBhhTtl_4bZtTAt7uw1AYlal7ccSCxMQwdODYDvZc4IU2bY3E7UD_znGGf1BjF0aDkKJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850e96d1ea.mp4?token=vdKUENOBc_JUoG2Pnp8IRPUUz_OGtnEgDvraCobqlvZDuAWDhiPK-IK_rXJ8WGsYYdrwNuVsadqFqPEYBw003l4hae8a0S5sINnR77gJ-L_MjhgQNzrppvywZFDxsH63NL9RVlUr3I_XMBPFg1SAX71wBfOWYEyql4TdXOcV2jy6MSXIDv9rVIJ7ngNJ5MhxNUptRsGsIF_EAE7H60NhdYdvJlrq-3uswGCL-RR5_-l5K66ekflzOtJX6o0egRdtuhfHVL488_n2RuikTyBhhTtl_4bZtTAt7uw1AYlal7ccSCxMQwdODYDvZc4IU2bY3E7UD_znGGf1BjF0aDkKJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرهنگ بازنشسته آمریکایی: اگر در کویت، بحرین، قطر، امارات یا عربستان هستید آماده [فرار] باشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451457" target="_blank">📅 21:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451456">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22b7a458.mp4?token=nP7Blj59k8S86pbh2VuyfAxYkrHnqShwV5PP_kwdnM7Lw6cqcsgSN_ZfN6D-2IRisBaow-B9Zc0aj9YtgQ3tXhSmVO0ekMft2czZ8KkomcnXLkBNSa581XLKUm6MP41738WHNPt43uhBPKUFX8B5LsiTavX8-5d66SI8z4g4tzj9LDHB3RxYivA8WaEyo6s0cIiBJqtOzdfUu446ME7oggPsca1LNGRiW-ODBDxGEf9VqQzncDHxs77ES2lCkQGv6Jq2eyjnMiwfiIOreZnHe3KnmN2x3x_XytKQbIYQgbLI9U7pB_y-An_7AfTkLfP_hbTrdSo7SmRvp99siJELMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22b7a458.mp4?token=nP7Blj59k8S86pbh2VuyfAxYkrHnqShwV5PP_kwdnM7Lw6cqcsgSN_ZfN6D-2IRisBaow-B9Zc0aj9YtgQ3tXhSmVO0ekMft2czZ8KkomcnXLkBNSa581XLKUm6MP41738WHNPt43uhBPKUFX8B5LsiTavX8-5d66SI8z4g4tzj9LDHB3RxYivA8WaEyo6s0cIiBJqtOzdfUu446ME7oggPsca1LNGRiW-ODBDxGEf9VqQzncDHxs77ES2lCkQGv6Jq2eyjnMiwfiIOreZnHe3KnmN2x3x_XytKQbIYQgbLI9U7pB_y-An_7AfTkLfP_hbTrdSo7SmRvp99siJELMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تطبیق تصاویر ماهواره‌ای سایبرالکترونیک سپاه و سایر تصاویر ماهواره‌ای
🔹
گفته می‌شود محل مورد هدف، یک مرکز داده C2 ​​و هوش مصنوعی ارتش آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/451456" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
با شنیدن نام‌های آبادان، بوشهر، چابهار، خارک و سیریک چه حسی پیدا می‌کنید؟
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/451455" target="_blank">📅 21:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJuc8aohQ7SZmRL49SJN8V_XkrJt5s4lT-WB5XhHf6Jl3f0XVp2Ndi8rZFUD7PJjEuGTS9WupkLP4EpOnHi0T3ij9M857wU8kDgx9jjY9QauroAnOipF8z8eqhnRLQQw7-cnRNj7q91EG8V-_2YZZchY7Cnp_F1VIWMwfE8mhbJYEsgf1DuXfC-mh3msjnn4ge--M8YYAifgFQ8NT3foUu6KNBQJIpN5Hh5T6pXSwdnUZ11cP6e4ZT2KkCXPDurSqQSLBWbSVJY3D3VCHxOsWdK5xVDArlzjWqLRjoJJd9yymOIB63AcRpt7Y1-csxdHbXuyvoOYapmHQDki22j2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آرزوی مرگی آرام را به‌گور خواهند برد
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451454" target="_blank">📅 21:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981a8e6dcc.mp4?token=oKbZ_x3aXg6FHEDZO8rfyaHXIZJ13YOpykbCZFT8cniASdy-PK6V7dKlkO3uw-eAMckKdSv9ip1Jqf8DAY6V38fgnWmSF1lquFf54QnqbxLvYVDF9KnhVW5hqzssNzhwxONICxCoVgy6gPUtIY2BDZ_e-f6m4upsGqjrzQbkzdwgxnM1AdCZK5Guo49d8P8UyKrRWE4QgraepVBJFGYFbtszS0uVGtzOaxW7oFoADazXTMinSzORJltEKVgtsQUlMfV-7GxhrePmQA0F96HL3sIKtcQ7lMMSbZg83vSV800eYO3AI8OB5JSFYPcI0cavDFVv-_VaqR9rfhi2YG3Bjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981a8e6dcc.mp4?token=oKbZ_x3aXg6FHEDZO8rfyaHXIZJ13YOpykbCZFT8cniASdy-PK6V7dKlkO3uw-eAMckKdSv9ip1Jqf8DAY6V38fgnWmSF1lquFf54QnqbxLvYVDF9KnhVW5hqzssNzhwxONICxCoVgy6gPUtIY2BDZ_e-f6m4upsGqjrzQbkzdwgxnM1AdCZK5Guo49d8P8UyKrRWE4QgraepVBJFGYFbtszS0uVGtzOaxW7oFoADazXTMinSzORJltEKVgtsQUlMfV-7GxhrePmQA0F96HL3sIKtcQ7lMMSbZg83vSV800eYO3AI8OB5JSFYPcI0cavDFVv-_VaqR9rfhi2YG3Bjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام‌جمعهٔ اهل‌سنت میرجاوهٔ سیستان‌وبلوچستان به شهادت رسید
🔹
سحرگاه امروز «محمد انور ریگی» امام‌جمعهٔ مسجد علی‌بن ابی‌طالب(ع) شهر میرجاوه در استان سیستان‌وبلوچستان توسط افراد ناشناس هدف سوءقصد قرار گرفت و به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/451453" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از برخورد یک پرتابۀ ناشناس به یک کشتی در نزدیکی فجیرۀ امارات خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/451452" target="_blank">📅 21:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451451">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d81f40dd.mp4?token=QnN9HbEtdSgG0kmLD9fz7k1eL6LQzQgKo8Z22WW-QosWxOxFZz0I-ClDgPzgtxJKYLXhRqOUw12G1h1jQ_GDeifcUtoYktxOtDH4zw5ERw7yP7spEVNkSXBwJRey6fznA2FYdZg0Jp27lIZXYIjICfhdiiEQqE8SA9oICT0eIGOHPCb5O-mYInHCDhbdCobyGlL1p2H6mTNgjw02Xqkz9fgWfg0MSw0Td0xpNJDHRV5319an-dc-mNaLHCu0_nNJPthuicWYKcRtz2EMYHrAbg7PAYLXqDzYMFlP0PhCs2QJCiLXFhP5KK9yIBqzPFrb_NqOZ7urHnQMvxBG6XvfDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d81f40dd.mp4?token=QnN9HbEtdSgG0kmLD9fz7k1eL6LQzQgKo8Z22WW-QosWxOxFZz0I-ClDgPzgtxJKYLXhRqOUw12G1h1jQ_GDeifcUtoYktxOtDH4zw5ERw7yP7spEVNkSXBwJRey6fznA2FYdZg0Jp27lIZXYIjICfhdiiEQqE8SA9oICT0eIGOHPCb5O-mYInHCDhbdCobyGlL1p2H6mTNgjw02Xqkz9fgWfg0MSw0Td0xpNJDHRV5319an-dc-mNaLHCu0_nNJPthuicWYKcRtz2EMYHrAbg7PAYLXqDzYMFlP0PhCs2QJCiLXFhP5KK9yIBqzPFrb_NqOZ7urHnQMvxBG6XvfDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشور وارد اسلام‌آباد شد
🔹
مومنی در رأس هیئتی متشکل از دستگاه‌های اجرایی کشور، برای تبادل نظر درباۀ راهکارهای توسعه همکاری‌های دوجانبه بین ایران و پاکستان به این کشور سفر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451451" target="_blank">📅 21:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451450">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOo-DnGDy1Dn_65UWBjpAOT3ExvwyOQBqPGQLBbx-7bfhxqAbSVA1KWOct1ezShJfNqTO52giYWqprGj0NkYtAfkb4RrMhULlEo63FhZqq3NRaULMcbIpjqCptHRDkmnyNKmZ7kllsFM8086x3788ZxwzKbkrzGQogbxKy8xnHupCG53884m3MF5pgfabN3ICYH9ZU13cFowgQ9bi5Cox06QzUR4_rIJ7EGzgO5uBUQMHEPl8a3KC3VEW9ed_wsRvHbsUrTvlFN5CHrkhTtMtcS6skQpxwSkVvPdUaNRa2MmaoURiwg8kCvlXl3JnjBlmdLaGFPjsj3aMukKR_CIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است. @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/451450" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451449">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BR_P2Be_PkGURxKTSqgC4zN74kSTfEt9k9zG9DZG1kjjbqe98gUkmHiLJcCSA4rWtv22OmVQzywJEA71WrMQynkqYJz5EBrF3rRABDZIoENYFuAG8u9YR2_likXaz9J91TDzn_wvxm7uqYoN14EAQqRR1wR0-L11oyLb_oH_2bHglbxOXR620cE1ESPM8M5e1QjZNrKN0zBp-BNZUYKNLkimFovePpAuzGNq_uut5UQe9w8rnm9W5_m2mj4nAu5H1nqCW05bycnrv8uBfNpOdEA4Qopmg-MIYpJuFGX3iZlHq3AC0Xh7a7yDEhNLkud9v6j--nMj__fgol7xalj0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت سربازان آمریکایی باعث عصبانیت ترامپ شد
🔹
ترامپ: هربار که ایران یک سرباز آمریکایی را بکشد، بهای آن را چندین برابر خواهد پرداخت. @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451449" target="_blank">📅 20:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcm49WXzAOsMTTz6IeWkBiCY6NMU1ZhNvwmluv6eObmqrvXEbQF1rSC8DAXlzaW451U39yeNqqiuTmEywLbmh9Z8nqsbM95UHepxm2UJ796GIwDzhAFS1XrPxM4bsUsX-PjPQoB4uY7YA5kdGEEM1VmnTnomX8TOIVnWnxnPTfLQVbYkhtgVMY1nJKXVcjhTDkzn10t4ohzUh3uPNjgbWfxhs2kI3zSWqOAwkwqGhDfSUt2w3Xso5PtytTEBmIY78hHxprGtgZgKyzncIimZG58fjbPHz3OdQNbvF36C9H9_FvJ4g06wRp_sZq_MSlgb9SyCiVEjF7m0eS9SwquS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام: بامداد امروز بقایای جسد ناشناسی را در محل حملهٔ موشکی ایران به اردن پیدا کردیم
🔹
در این حمله ۲ نیروهای نظامی آمریکا کشته‌ شدند و یک نفر مفقود شده است. @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/451448" target="_blank">📅 20:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451447">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VT-RmYs9sqGn3jQo42FAn-FTWZAIDMF8Hp9tP0aK-LXp1WEUJ1t_as4eLc23pmtazH2EA_h9jeoR1U_lZeAEJKG-G9Abd9wVHEx7xt3XbbRVAYXMf-8gcd8Sw8JRZ6tkhxAZ8QhtPmLA4tVOGMP3eXNrkdN38YbjTG9FDpjw759_0MnauwzHis4EHe2VFA_7OCyvbSLqnLFm0TdAwtprk3hkpdGF2N_yeuvRwsnO7i8KuNiZ4GFCS5J-iAz5VkL-ovQllIyg1J8wFX8w59a4MNQqy4l_r0uM6Nawd2OklBtXn8LuyvNhxxeKkuhSridnceXIp_1Dzkq6iID4Xgw0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از برخورد یک پرتابۀ ناشناس به یک کشتی در نزدیکی فجیرۀ امارات خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/451447" target="_blank">📅 20:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451446">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf6QGbJQ8RN-LQl_PCOwAi-49h7F5qehQ9nf62zzY4Iwc4vCmNqdVHYm3yuF_fjUyzJ59nr6-yExsc5vzLWwHz1WIu5dHDHzyUq6nCtrqdcHVib-16KDr_JRBVjpz5UfUVS43JJ4oagQdvx_DtBZyfG9WRYdHXPcbtFa9hyBGsVtxBJAQ6LjVJssHXXXunixCZPG6PrD9JnkGdMv_aFCINIFFPHWgWsyJ9Yy8WLu-VkW9cI8Q2nCuG8Odl_ZePjZ_m6zJ0J14DisCzVQvN9WkfZwOjydJnq9frw4pVEAyJiLNxrlcrwIe9_Tw8hJh2gLBaN2vFXrAki_88pMuI9mgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تیم منتخب جام‌جهانی ۲۰۲۶ از نگاه تحریریه ورزشی خبرگزاری فارس
@Sportfars</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451446" target="_blank">📅 20:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451445">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حملۀ دشمن به یک واحد صنعتی در خمین
🔹
دقایقی پیش صدای انفجار در حومۀ شهر خمین شنیده شد و گزارش‌های اولیه از هدف قرار گرفتن یک نقطه در این شهر حکایت دارد.
🔹
معاون امنیتی استانداری مرکزی اعلام کرد در این حمله، یک واحد صنعتی هدف حملۀ موشکی دشمن آمریکایی قرار گرفته است.
🔹
تاکنون گزارشی از شهادت یا مجروح‌شدن شهروندان در این حمله مخابره نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451445" target="_blank">📅 20:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451444">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd9cf5511.mp4?token=DJr4wNbuI0lHTWeLO90I0ZGonLgVgA2lUepiKoENN7yAZF-GQ4f98aZjwPuVu5ISBxHnDVYRb3iHrlzirLeFqYKPT0EyxbrEdZlETBfJ3P9kL9-o1p24UcUXNHUv6wPMZrKSVHXHSkl-1Ngg69fY0zSSxLdeilcVzNsdExrF88zUUK66VTLqZBx0nFkNGE85R9ELQjlMKoR0c8AqMPRtZbjgi1vs8IZ74RrOPb3jyGPATF1s56h2ZE507umrxE7trLPIFqUS_d7OjIcY0SQ_HdBXwG9_Hto_7ZWJPB94BFbBfrfu2GZIhaVtCbFjBTwzalDhdtLs7jNd2K7orjfwvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd9cf5511.mp4?token=DJr4wNbuI0lHTWeLO90I0ZGonLgVgA2lUepiKoENN7yAZF-GQ4f98aZjwPuVu5ISBxHnDVYRb3iHrlzirLeFqYKPT0EyxbrEdZlETBfJ3P9kL9-o1p24UcUXNHUv6wPMZrKSVHXHSkl-1Ngg69fY0zSSxLdeilcVzNsdExrF88zUUK66VTLqZBx0nFkNGE85R9ELQjlMKoR0c8AqMPRtZbjgi1vs8IZ74RrOPb3jyGPATF1s56h2ZE507umrxE7trLPIFqUS_d7OjIcY0SQ_HdBXwG9_Hto_7ZWJPB94BFbBfrfu2GZIhaVtCbFjBTwzalDhdtLs7jNd2K7orjfwvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی مرحوم مهدی آصفی در ویژه برنامۀ محرم خبرگزاری فارس
🔹
مهدی آصفی ادیب، شاعر، گردآورنده دیوان‌های شاعران قدیمی و خادم اهل‌بیت(ع) شب گذشته دار فانی را وداع گفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451444" target="_blank">📅 19:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451443">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دولت لبنان پس از چندین دور مذاکرات مستقیم با اسرائیل، ساعاتی پیش اعلام کرد که بر سر اجرای طرح «مناطق آزمایشی» و ورود ارتش لبنان به دو روستا با صهیونیست‌ها به توافق رسیده است</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451443" target="_blank">📅 19:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451442">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
آژیرهای هشدار در مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین به صدا درآمد. @farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/451442" target="_blank">📅 19:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451441">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ_hvrSzyxel4SHzkwkU3Y65iUf8ep3V6t0XeHEFtqYMd035KKOSGvjG-GOD9HfR8h3-Sh9MuDnPpmRKYBUmzTWVW-i1Qprg3HVUCDzPPCVi5LlewvsGjdhaPUAH3-EU9_UCfijUwdKY8dGogjuh2chYbAWubZICqwigqo3op9xfUXhe4T2Bt3TacZd_WHjBDqiYo_-ccLk1z8bXJNY08Q_2pL1r3LDvU8d1b222r6szQrQOGtDqCWMOd5ohawgZvCyRHmJXsSC4zcgh5Ny7Ffh-XYsaceSXAJiH_R1iKW5fbF2EbOozlCzBEMpqxKZ05ExBPbG7Wu3CVTaQiZrV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: ایران برای توسعۀ فناوری از کسی اجازه نمی‌گیرد
🔹
معاون اول رئیس‌جمهور: اقتدار دفاعی و امنیتی کشور بر پایۀ پیشرفت‌های علمی و فناوری است. ایران برای توسعۀ فناوری از کسی اجازه نمی‌گیرد اما دستاوردهای خود را در اختیار کشورهای دوست قرار می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/451441" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07e737a76.mp4?token=GIKka0v5hMwVsGYE2Fhlb0uJdYpNLsLnc24GgSXFJ0z9BvRWvIxFx8xWOsMorIi_U08hM93nnHfRhpvO_LqRxmsUuD03yLFZcGGbpCzJucw4afkFYJMwEXEFMMDdrpLKVjXBwf7oB-FYaFRkmsh3onUUJW4mBVAup6tXWmHk5MpJ7g13-Mb7t3vbAefGw9B_dRKQCu_6_GO-fpA9iijMkADuZwr7HV_fFYpLHE7gNaBLKDK1U8_J1IBQqq0-KTysJJQJ-9nOdVn7BX-B3ayTjCjz61NhQzxYFWSitkTMYkLLjbtoOsgt0YHJr3H3yR8mVWdjkEEHy7ZiqB-v9O0_cTe3-k7QWwZbwSMQnp5yj3xwuETTC0umlzOU80SG-hZdhJOYh5wwI53NA3q0JZesHmRXRu_gtHQnw92WmIOT-Nskq9Gd9X2diqt_oFMrk7sue7Ij2qtNIOciS4ryBHjOGdV9HdWViF_i4H0bgqiKyTbMQ4tc3QMpwQldxFvjOcX1vG_g6KHQc27bzfi7C941xsnJr6W7fTm_pYXLS74njdjkC1QIdmKF_wqoy8Im7KetDZLo2VRbM3ksj96ZL0-xiibiELy29u_diEfdNU38ARI82E_ae8VdhhoZphqXORBeAjVHh9DBohJEpZKj-1-TIQ47F3uM9Rvcra_x0NXAgz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07e737a76.mp4?token=GIKka0v5hMwVsGYE2Fhlb0uJdYpNLsLnc24GgSXFJ0z9BvRWvIxFx8xWOsMorIi_U08hM93nnHfRhpvO_LqRxmsUuD03yLFZcGGbpCzJucw4afkFYJMwEXEFMMDdrpLKVjXBwf7oB-FYaFRkmsh3onUUJW4mBVAup6tXWmHk5MpJ7g13-Mb7t3vbAefGw9B_dRKQCu_6_GO-fpA9iijMkADuZwr7HV_fFYpLHE7gNaBLKDK1U8_J1IBQqq0-KTysJJQJ-9nOdVn7BX-B3ayTjCjz61NhQzxYFWSitkTMYkLLjbtoOsgt0YHJr3H3yR8mVWdjkEEHy7ZiqB-v9O0_cTe3-k7QWwZbwSMQnp5yj3xwuETTC0umlzOU80SG-hZdhJOYh5wwI53NA3q0JZesHmRXRu_gtHQnw92WmIOT-Nskq9Gd9X2diqt_oFMrk7sue7Ij2qtNIOciS4ryBHjOGdV9HdWViF_i4H0bgqiKyTbMQ4tc3QMpwQldxFvjOcX1vG_g6KHQc27bzfi7C941xsnJr6W7fTm_pYXLS74njdjkC1QIdmKF_wqoy8Im7KetDZLo2VRbM3ksj96ZL0-xiibiELy29u_diEfdNU38ARI82E_ae8VdhhoZphqXORBeAjVHh9DBohJEpZKj-1-TIQ47F3uM9Rvcra_x0NXAgz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متفاوت‌ترین موتورهای مسافرکش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/451440" target="_blank">📅 18:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/451439" target="_blank">📅 18:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451438">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/451438" target="_blank">📅 18:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id90Zd-TZOg1cY_tLF7Xc0g0VIlw-gVufwTx-sMwvwvRdIbdCwYAlCyETCbiNQb251lCz02_u22NgK6YCA4MMnaCr41r5NQavGvqttMhO2o2TapINkgOnliHe_GXV7xsPHaXr1BhBSGhrwh7zCljtPPGFBvazk8OoWTTDlZVT2GybkD3NX5MDuybbscEZkANwm0Kga1YLle-Zlsk63zk8usS8QzS3bIo7K8w8a4lFS8UH_V9MFzbVurNQZT67r8VTC4D9F9ccVHpzLlaRkIkeZqnCRGN-Ey45XWG6GZsE6d9AZJkoCsLv-91RKa7EyESnPqh_NfzVCJoIbWK6VD5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرکل مدیریت بحران استانداری آذربایجان‌شرقی: در حملات بامدادی دشمن آمریکایی به اطراف تبریز یک هموطن به شهادت رسید و چند نفر دیگر هم مجروح شدند.  @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/451437" target="_blank">📅 18:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">طرح دوبارۀ آتش‌بس چه هدفی را دنبال می‌کند؟
🔹
طرح مجدد آتش‌بس از طریق واسطه‌های قطری در حالی مجددا مطرح شده است که آمریکا هم‌زمان سیاست فشار و حمله به ایران را دنبال می‌کند. همین تناقض، این سؤال را ایجاد کرده که آیا هدف واشنگتن پایان جنگ است یا ایجاد فرصتی برای اجرای مرحله بعدی نقشه خود؟
🔹
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در واکنش به این پیشنهاد نوشت: «آمریکایی‌ها روی هوش ما اندازه آی‌کیوی مختصر خودشان حساب کرده‌اند. ما در شناخت این آمریکایی‌بازی‌ها به مرحله استادی رسیده‌ایم.»
🔹
این جمله، پیام روشنی دارد؛ پس از تجربه‌های مکرر عهدشکنی آمریکا، بعید است در ایران کسی آن‌قدر ساده‌اندیش باشد که صرفاً با یک پیشنهاد آتش‌بس، دوباره به واشنگتن اعتماد کند.
آمریکا منتظر چه اتفاقی است؟
🔹
تحلیلگران معتقدند هدف اصلی این آتش‌بس، خرید زمان برای ایجاد یک فرصت داخلی است، نه پایان جنگ.
🔹
در هفته‌های اخیر، هم‌زمان با مطرح شدن برخی مباحث درباره مدیریت ناترازی سوخت و احتمال اصلاح قیمت بنزین، رسانه‌های معاند نیز تمرکز خود را بر تحریک افکار عمومی و دوقطبی‌سازی جامعه افزایش داده‌اند.
🔹
واقعیت این است که دولت با ناترازی جدی در حوزه بنزین روبه‌روست؛ ناترازی‌ای که بخشی از آن ناشی از رشد مصرف، محدودیت واردات و تغییر شرایط تأمین سوخت در پی تحولات منطقه‌ای و جنگ اوکراین است. طبیعی است که مدیریت این وضعیت نیازمند تصمیم‌های دشوار اقتصادی باشد.
🔹
تحلیل غالب این است که آمریکا امیدوار است اگر این تصمیمات به اعتراضات داخلی منجر شود، بتواند از این وضعیت به‌عنوان یک فرصت راهبردی استفاده کند؛ یعنی پس از شکل‌گیری التهاب داخلی، فشارها و حملات خود را از سر بگیرد تا ایران هم‌زمان در دو جبهه خارجی و داخلی درگیر شود.
🔹
اگر این تحلیل درست باشد، پیشنهاد آتش‌بس نه نشانۀ تغییر رفتار آمریکا، بلکه بخشی از همان «آمریکایی‌بازی» است که قالیباف از آن سخن گفت؛ تلاشی برای ایجاد اعتماد کاذب و انتظار برای مناسب‌ترین زمان جهت اعمال فشارهای بعدی.
🔹
ازاین منظر، مهم‌ترین راه خنثی کردن این سناریو، بی‌اعتمادی به وعده‌های آمریکا، مدیریت هوشمندانه مسائل اقتصادی، گفت‌وگوی شفاف دولت با مردم و ناکام گذاشتن هرگونه تلاش برای تبدیل مشکلات اقتصادی به آشوب اجتماعی است.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/451436" target="_blank">📅 18:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سخنگوی دولت: برنامه‌ای برای افزایش قیمت بنزین نداریم
🔹
مهاجرانی: دولت هنوز برنامه‌ای برای افزایش قیمت بنزین یا اجرای نرخ سوم بنزین ندارد.
🔹
در صورتی که برنامه‌ای در این زمینه وجود داشته باشد، به صورت شفاف اطلاع‌رسانی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451435" target="_blank">📅 17:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7vtZhP1NxPQtZVZPgA3myFbhuwub6cErcHIKF7Zbd-aNXZwg4Xq3bqcaEc8CgSX7TdaH5O9uNozfUIes1eeDVUN_nbvzexSXIGq8MAmdjNfIZv-a7Ypt2XviOTnXJpdw9NWOJtwNF4COLh3jEP2d1pgTUM38UemyxHro4xs94Wg01YIBbiiO8XwD6PaZDDfzRKUaSJI9O9W9gIenqbvDpjcMs1Dxy4nKt9djppouPSHf9o6HxqvjvWmDDhfh3wmeFldJMgWBaJ0xbupr8rGmMXyHWBmI37hIc1LC57Gymac7ZDh5y6Jrd7prEioKMAH5TYpsgGDVx6u_EYf3lLUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت هومن حاجی‌عبداللهی و جناب‌خان به آنتن تلویزیون
🔹
تهیه‌کنندۀ برنامه «قصه‌های هومن و جناب‌خان» در گفت‌وگو با فارس اعلام کرد این برنامه از شب اول ماه ربیع دوباره روی آنتن شبکۀ نسیم می‌رود.
🔹
این برنامه پیش از ماه محرم نیز در قالبی طنز پخش شده بود.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451434" target="_blank">📅 17:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در شیراز
🔹
دقایقی پیش اهالی بخش‌هایی از شهر شیراز صدای انفجار از محدوده شمال غرب این شهر شنیدند.
🔹
خبرهای اولیه از حمله به یک نقطه در شهر در جریان این حملۀ هوایی دشمن حکایت دارد.
🔸
به گفته استانداری فارس، این حادثه هیچ گونه خسارت جانی درپی نداشته و تیم‌های ارزیاب در محل حادثه حضور یافته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/451433" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c258107e1b.mp4?token=CL2Q_5d3FTmVzejXhyv6CXvaOZMk9HzgDHHL0O1XipVchZ8JFuFmYJgk2LXTwqNookD0xzL7IGXUtDb-SlDJWMHzf4F1CU4GQKw5ZGSQT2jgk2oOjm05i8HTt_jdgfnKDaldw_PSJmq9H37D_z6j3LJ6wn2YB-SJ8TIC3tA1uF9uiIRRBj-nQZRf33u9JpvqDVICyA4yUhjAP5_6d10dqU4fNJdnI_QxbyiqzNIY3XuwPeO-gyNcfrcs3b-U9rvd69OlPCl5qpdW_uRmXsGx8IXWpYSQHVn-DOoZT4Ja1X9XJLHqnU_VBlaZLW__6cu9lpvgmSjmc3WNIMWtHOBsXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c258107e1b.mp4?token=CL2Q_5d3FTmVzejXhyv6CXvaOZMk9HzgDHHL0O1XipVchZ8JFuFmYJgk2LXTwqNookD0xzL7IGXUtDb-SlDJWMHzf4F1CU4GQKw5ZGSQT2jgk2oOjm05i8HTt_jdgfnKDaldw_PSJmq9H37D_z6j3LJ6wn2YB-SJ8TIC3tA1uF9uiIRRBj-nQZRf33u9JpvqDVICyA4yUhjAP5_6d10dqU4fNJdnI_QxbyiqzNIY3XuwPeO-gyNcfrcs3b-U9rvd69OlPCl5qpdW_uRmXsGx8IXWpYSQHVn-DOoZT4Ja1X9XJLHqnU_VBlaZLW__6cu9lpvgmSjmc3WNIMWtHOBsXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش‌هایی از انفجار در شهر نیویورک آمریکا
🔹
رسانه‌های محلی از وقوع یک انفجار در نزدیکی یک ساختمان دولتی در شهر نیویورک آمریکا خبر می‌دهند.
🔹
طبق گزارش‌ها، صبح امروز به وقت محلی صدای تیراندازی و انفجار در شهر نیویورک آمریکا شنیده شده است. تصاویر منتشر شده از دستگیری یک مظنون حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/451432" target="_blank">📅 17:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451431">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0451456d.mp4?token=YVykqmOGxfvv6Mm3XfUgp9QSE_DvVLnMq5_Ntaxl6ZiyGfK1Rj8_v4KgbVWDqB8jecHePCHGqUrQqXX6d1jGyDg1J3M5szoxjfruw4zUSW-BIqwpBUBalzl-M_L0hnn2jfpuoAzHMEjCZiLNgOeSJCY4bjP_WICttZPA0en0LeO4LsoXDYYRXDP-Fr4Yxd4TYMP3JPcecFJzkXHXXg-z2JfpT7C4mTWg2d1tDwiQcP_46buer4hZ4DaOHfUAr6maYnAqPgiugs0MgkfetwwopSadIpp9qupyo9Fui6Xy47GlRqP_6At84bsMeGaYO0APdPTK3lPT5dcinf_PzBS1ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0451456d.mp4?token=YVykqmOGxfvv6Mm3XfUgp9QSE_DvVLnMq5_Ntaxl6ZiyGfK1Rj8_v4KgbVWDqB8jecHePCHGqUrQqXX6d1jGyDg1J3M5szoxjfruw4zUSW-BIqwpBUBalzl-M_L0hnn2jfpuoAzHMEjCZiLNgOeSJCY4bjP_WICttZPA0en0LeO4LsoXDYYRXDP-Fr4Yxd4TYMP3JPcecFJzkXHXXg-z2JfpT7C4mTWg2d1tDwiQcP_46buer4hZ4DaOHfUAr6maYnAqPgiugs0MgkfetwwopSadIpp9qupyo9Fui6Xy47GlRqP_6At84bsMeGaYO0APdPTK3lPT5dcinf_PzBS1ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی حسین طاهری برای مردم جنوب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451431" target="_blank">📅 17:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451430">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960a5e081d.mp4?token=DT8YDRxVOg21MS6pU4WhtWaW1vsD45hham32L0ZBSQkhymSBSAyQf0aWNX_120O5OAOVmfco18e3IvQnYRzct55EnMCMvvSchT9nrv6frFTZAr1dph1f97RvsiYgyFSlED-aW2jHydzyPoP5CuMBDBrV8kaoCAXxVNB-n1g44cnt3PnYuCC7KaZtZ05fwWxLKOTFlT5i1qXOLBCivnyps_saqm2xJfSg7z6zckL074JP2ivU2x0U7NC-ZGGO-SdUOrLAMqqaHsuT-R_p4ElRPes3AGxBzw_VoTpyCkjLxxmwkC1cc4kJJZGzbKnxak7Sq6CzYVFRdTAQXbnBxDXsXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960a5e081d.mp4?token=DT8YDRxVOg21MS6pU4WhtWaW1vsD45hham32L0ZBSQkhymSBSAyQf0aWNX_120O5OAOVmfco18e3IvQnYRzct55EnMCMvvSchT9nrv6frFTZAr1dph1f97RvsiYgyFSlED-aW2jHydzyPoP5CuMBDBrV8kaoCAXxVNB-n1g44cnt3PnYuCC7KaZtZ05fwWxLKOTFlT5i1qXOLBCivnyps_saqm2xJfSg7z6zckL074JP2ivU2x0U7NC-ZGGO-SdUOrLAMqqaHsuT-R_p4ElRPes3AGxBzw_VoTpyCkjLxxmwkC1cc4kJJZGzbKnxak7Sq6CzYVFRdTAQXbnBxDXsXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجات معجزه‌آسای موتورسوار نوشهری از برخورد لاستیک سرگردان تریلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451430" target="_blank">📅 17:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451429">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4ac0667a.mp4?token=d0h1JKq1AbFxbyFm-HE-fZ5cj-2A5JjQXdHnNAatTrhDRmGkqTT6Q9x10sr1egLWLEgGOTfcNxk72UE8Ffj3yqghDw0spewdsKMtcdr46CKjdCjpB6b4tmvlHSTEmOzMsDprw8HEkE8-FRyOSNvpMAIQ90lwuJlOrvVJIIYF0phiUbO33ZA4cT-wGLusgQMVI2sf3UwtNlLacdHcnM6MOrY4adn1refI-xPv2Ip7OKTUhamFNw8J9BvQD9ngMjAx96T48pKB81rSDiUsRXGEF3atwpHRDVTJs2UNvR8mf9K1765XndUWWs7HEy4-38nuEN9r-pnW4IHCPu1OAIefTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4ac0667a.mp4?token=d0h1JKq1AbFxbyFm-HE-fZ5cj-2A5JjQXdHnNAatTrhDRmGkqTT6Q9x10sr1egLWLEgGOTfcNxk72UE8Ffj3yqghDw0spewdsKMtcdr46CKjdCjpB6b4tmvlHSTEmOzMsDprw8HEkE8-FRyOSNvpMAIQ90lwuJlOrvVJIIYF0phiUbO33ZA4cT-wGLusgQMVI2sf3UwtNlLacdHcnM6MOrY4adn1refI-xPv2Ip7OKTUhamFNw8J9BvQD9ngMjAx96T48pKB81rSDiUsRXGEF3atwpHRDVTJs2UNvR8mf9K1765XndUWWs7HEy4-38nuEN9r-pnW4IHCPu1OAIefTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ضربات سنگین نیروی دریایی سپاه به ارتش کودک‌کش آمریکا با حمله همزمان در سه محور
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/451429" target="_blank">📅 17:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451428">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
وقوع چند انفجار در کویت
🔹
در حال حاضر، آژیرهای خطر در کویت فعال شده است، برخی منابع از حملات همزمان پهپادی و موشکی به مواضع آمریکا در کویت خبر می‌دهند.
🔹
ارتش کویت ضمن تأیید این حملات، ادعا کرد که موشک‌ها و پهپادهای شلیک شده را رهگیری کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/451428" target="_blank">📅 17:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av4lxxwcfxqIKlRTJqC-TaWI9OZuVo2TtE75v9p6uYW2cl-IQBcjTYqGq8laPHp7gzX_HNVB2F3jyYXh83PuY7tC6K94Tn8IdbjvRLjsRp_BghI4p8vykpFUfMhLEcj_bWGkGaEeNrF3SQvp6x_lyTDQT6IV4czTRTk8zH3NOn1EWhuLR9IUr8qCcVO4Pml3spDywSCBFBLo4taTiWMAq9PD6xlntvmmooD3HCWo09eX8Q0GZ1E7k3apHf0anyFi_eIER3647OLpZ9L0vReJuH5aQwiTDh9y2Gn4RsyKL91UmW58w5uqojtJMyU6OLoTb7Q7PUtu9A-NOoh6AHSVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07f18e551.mp4?token=e-7Ij7flrW5YmuiYxpGPj3FcQ63hqzDk0Ya-ROPBWrXNIQgzPMuqGCMqjj6vJ2ONa9-2-GKeMkspMH3lZI9UDoyka7mLWKxbzTqss63C2tf84lJ2FC4YffeXBWG1f_OYJGuH7bwU7EL5G4c8oYbwAahSVyauDwIRjDuz7_9NJih2glKLQQc7maKHYYJUMF81d-x9gDw4uuf0BVmTHJzYVY9oAjpTRuqZqOFyzRr6HygEbIsRBDnoLjPMHaPC91J8ngunC4yVQdM0K7pDG1fTeyhOty-Yri6L6S9dFXOlNOEHOnkjBNQL1f_iP8Gppk39itAgpR_bJ-KWJDE08M-qZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07f18e551.mp4?token=e-7Ij7flrW5YmuiYxpGPj3FcQ63hqzDk0Ya-ROPBWrXNIQgzPMuqGCMqjj6vJ2ONa9-2-GKeMkspMH3lZI9UDoyka7mLWKxbzTqss63C2tf84lJ2FC4YffeXBWG1f_OYJGuH7bwU7EL5G4c8oYbwAahSVyauDwIRjDuz7_9NJih2glKLQQc7maKHYYJUMF81d-x9gDw4uuf0BVmTHJzYVY9oAjpTRuqZqOFyzRr6HygEbIsRBDnoLjPMHaPC91J8ngunC4yVQdM0K7pDG1fTeyhOty-Yri6L6S9dFXOlNOEHOnkjBNQL1f_iP8Gppk39itAgpR_bJ-KWJDE08M-qZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و ۲ کشتی دیگر از ادامه مسیر ناایمن منصرف شدند
🔹
نیروی دریایی سپاه: ساعاتی پیش ۴ فروند کشتی متخلف با شیطنت و حمایت تروریست‌های امریکایی و با خاموش نمودن سامانه‌های ناوبری و بی‌توجهی به اخطارهای پایگاه کنترل تنگه…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451426" target="_blank">📅 17:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ضربات سنگین دریادلان نیروی دریایی سپاه به ارتش کودک‌کش آمریکا با حمله همزمان در سه محور
🔹
ملت به پا خاسته و حماسه آفرین ایران اسلامی، با توکل به خدای متعال و دلگرم از حضور هوشمندانه شما مردم بصیر در صحنه، دریادلان نیروی دریایی سپاه با حمله همزمان در موج ۲۳ عملیات نصر۲ در سه مرحله با رمز مبارک یارقیه (س) ضربات سنگینی به نیروهای تروریستی آمریکا در منطقه وارد کردند.
🔸
مرحله یکم: حمله به سوله‌های نگهداری و تعمیرات پهپادی واحدهای آمریکایی مستقر در فرودگاه اَلصَّخیر بحرین که منجر به انهدام آنها شد.
🔸
مرحله دوم: حمله به سوله‌های آماده سازی شناورهای تی‌اف۵۹ در بندر سلمان بحرین که منجر به تخریب آن گردید و خسارات سنگینی به شناورها وارد آمد.
🔸
مرحله سوم: به آتش کشیده شدن سوله‌های محل استقرار و پشتیبانی و تجهیز نیروهای تکاور ویژه دریایی در پایگاه عریفجان کویت و منهدم شدن آن به صورت کامل.
🔹
حملات کوبنده رزمندگان اسلام با انبوه موشک‌ها و پهپادها در مقابله به مثل و پاسخ به تجاوزات ارتش کودکش آمریکا ادامه دارد.
🔹
رئیس جمهور بی‌خرد آمریکا که بارها به ناآگاهی و بی‌خردی خود از اوضاع عالم، اعتراف کرده و می‌گوید بدون اطلاع از عمق نفوذ امام شهید ما در مردم جهان و عشق و علاقه عمیق مردم ایران و سایر کشورها، ایشان را به شهادت رسانده و اینکه می‌گوید بی‌خبر از اهمیت تنگه هرمز در اقتصاد جهان در این منطقه، جنگ به راه انداخته است، شب گذشته باز هم بی‌خردی و ناآگاهی خود را آشکار کرد و اظهار داشت تعداد موشک ها و پهپادهای کمی برای ایران باقی مانده و رو به پایان است.
🔹
رئیس‌جمهور قاتل آمریکا بداند اگر این جنگ چند سال طول بکشد به اذن الله تعالی تا آخرین روز آن موشک ها و پهپادهایمان بر سر جنایتکاران آمریکایی خواهد بارید.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451424" target="_blank">📅 16:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451423">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7Gb600dWlAN0GOWRUr3xiXsTCarpDR-t5cvdO-r7F6kJKRmTSEDPckBwVDHR72rvUMl_kpn6zFG73C1Vkakzs4Xizf8RO_Mxxr_pERQazVMdu5g-Bfm1WeX5BL1N7AFwgvXZ1pcMkLS6psSOy7ucVAbdgR1kt-i9hjVaujb4wdlDJV5b9ShgOFKMleRfgLlUSwvR9gSheDMuoJDEVdyz1Z-RwbE4Ljata9HCWAxrKOp0k0YtS81iUuZLcbs6NwY2U0YugE972pzKtHDdL7aU0aoPqG0u13Qgx0T2EIJnjtZAkRRdqUpSn304QUdok_TlJDSEurokZaSVcigksKjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور عازم پاکستان شد
🔹
وزیر کشور، در رأس هیئتی متشکل از دستگاه‌های اجرایی به دعوت همتای پاکستانی خود راهی اسلام‌آباد شد تا راهکارهای توسعه همکاری‌های دوجانبه را مورد بحث و تبادل نظر قرار دهد.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451423" target="_blank">📅 16:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451416">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tm-Aj9ZwO5M7-4F4C0BE6efvpoJkdVW6ZAKx8kLC8c-IDQQiU3VTzY4b31Vx5lDJS6R-WlFfkDhOCsZFiqmug8zfkJzFtpqRw4jXodsyd00YCtjQMDEj-FnHll-dGvqwQGjrAZALRD7ojfEhx2P7yD9z5tG1leI0b86KOtxZfuW1lCdfwvDI9O0OhMvO8yqkV1GjSUCtzU5D8BbMzEqQ6HjifXSxvHEqRUmg695470GdSIndpVpL9pWVC_3Y1PEZiMsj0mc6PBbpqTeEdhgciX3aAqXS6pkKu8fhUJL_ew_ivd_Ifw5dL3LKo9PNBOmbKNp0dZ7MF1rH7zonMfs_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzYRd35THDbE-MUi9xKBSOORpyfBynt3TyWBl4GXExAANVLB4J_AGuivHWiLqfFY70khVZvvd0EtrYR5vbyOeWY19EjOImQ1x84m8S39wN9CgAZb_LbAC3nd0N6VQPQVr-eMSScESndSHMgCj_QLtO_btnruWAnAHDxJoznP1Xr9IvumFwrcRWi0mFeg9oprv8ZxNc_7ziiRSxSTmDMJbhdLTtCrr8UBFv2cymjpFlyAoLliJIBxQfCof912WG97SzOet1YdRbJOaMr6OzA7tQqBjz6545_dabF0tedW21GIraqz8s04qTvMtOBofFKdhGZ4P1iuJljBjmrOhYICUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQeBOdugb9lW2DCX8GAe_zWOR37N8XU_G5Doj-YJOC6ZOxVo3gmIzgwlz8kf0Jl5pGO78llyAMbNPhnsB3bCBVtS5CVSaecFPuTNAytC36BxreXcI1uOj3t0GBoblZ-gKE-Az4ApBQJY6OLxgz8SLe32DOKhjP9ROLIzzDoqDenEje-H_3Q49Uhk8jgdqBih9DEBMynwtCDcEy_oB2VcdfkEfxTXjD1VbkZqPekfNAMgiMEgz7mNTK5dyTR5cj7KPdKR5Bvjzk3r3h7w0_NidLZV-4ZyCiaPi5lvL387JRI4morjIeIUvkVcsaKikoIoVIjBkgwKr3tPmV21df3uHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjJNEZm-D0KWk3QJ2q2jEXhorISeZO5BJuO8FAXtdq34CXYGfzfShyv9ssGdLOTp5uX1T6Ipt7SyUBrjcKZWH0NZw62kVciTI_PhHymfQSCep1VRY_dW9vzvmPF28rAo-Bvqml5Y54Ysa2BJ2HE9IWMvTn9dKfdKUZXjATM15Q7tLW-Ex9_C6Yv3JnXOm5kDF7xF7ir_gY6VYvvhgizg_FeOyo1Hr39PBRqqTAL37mgYAjfa6XO9yG3KWUnP_QktIRKKFHbPzwf_wyowLsRixOMjHu7E8YtaHf_NQbOsxD2SLK6h6tt7RHZu67HLVFl9e7fSZFYP9BdmS-c9t5g0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThNMnzZ2qz6sM5P19CvnfK1FMpR6QrwMMyVytvF4azk3tmqpq0Ed-i6K8JiR8daHHQ2PIYlf2ThtBTJBXgfBTzqRPcX0EyKMg2XWwOnEpmfjOQcqeD9lmufI60raRloY2zm4HsRguTDk9UdoZutnpCEeU4bU0Opbso5Z7HPiIB-6A_nSJ0mW-llt7-51RfcWg1DPf5TYlrIel4Yh9BkWsjGL8vahpKAtwBxrtGdHLvMdcE35Pe7W_HpiowFWIUJeVLzMfGj-ujWYtt4pKupAf5aa8WyemPXAmZCRLmdnGZYalT55QfxkdR1ahdx2zxZq0R5U_NOeWnCVmGcwxS2_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlI-dQmyeEnrMzJhhpflMpFT099rLwPslnD10JIcvfSFJnsqiVvQB5aW7ofG-65SD9Oclruh94KCErfwOSmXwrN3XkalhH5Z92RDeZ-X6FhW6IT4dq6d7L88idhyjtobkw1eIXVhzKkSMjqDnc9SbsagS4szrSebrp0rtMZzqimwNnQYCM9sPxOglyjpOvxazC0_WM0Y36fBLC2BW_H8Rs3K3Z559pIaG1y24sXVEkqHyJhLJ_2o3ZC0PmPxCiXT18sw-y5qwLkFaqSwscleHU1lyxacoQXoar4dYVCcH2pmVDfgp2NfIPG0d1Jr0rz23wC8elNnvCMraDA2Kh8TGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WoU80MeGVRWk5tNse731aHvQmV3G0hCg182_TFRpgCOoVoBY8cAGSpaz0SOTbbCNYvUWq_PoDmbqV9OhzYVb5i35JWwj93Rv_W6CpBgaAZfAKkBTtb6uwgCBhDx0SxjHlIx4xyivvYweU6GcPaLlDOrXovrB5-B6zgeeGDmkGyTteP4A7re9CI9u7vV4pWNRSCOL5SAZEZvDG3UMWDU8bmALqWPwVT6xS0xsTtX7YWkf0o1MQCoe8ZLlNoagBO5tz8uCnywVV3fYHqdd1-TAiE7Li3sdXMSfANua1-uDh86ms5PSID86jNftJzml4x6HJVGaoO7-SR9DohColyf8dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفر چهره‌های فرهنگی، هنری و ورزشی به جنوب کشور
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451416" target="_blank">📅 16:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451415">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
وزارت کشور بحرین: هشدارهای حملهٔ هوایی فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451415" target="_blank">📅 16:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451414">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCIlXHvzVeQYH7OAtTugd31U4Tdkf1ktEItbK12Hk6YtMKO130ZMOhCSnrN1wStdF6RiUarddmoXxgNPBeEe6IgPAWY5Khkqk0PTYGrFiJBAkPVQVIj7yyLxBHao-YE1utRF-MRr5liMNTWyyvkvEGLEOD06d52BSnPfSygpcxFqr0LUqUhL1axoXYQVNtPe8yWZDYDh5xjKaYuEaT0Fwki3skHtJVYreNbOlYZ5MN0WMIbVwRpVa0IsnZ1Qt00TYZn_iasd1VMSyRZ8UAK1IvSaHtZ3526ntyvPCIBqvcUPXLqQCBRBz7kwEUVVVdZQ9234M7Q96I_jzwUL6JZuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش دمای هوای پایتخت تا پایان هفته
🔹
هواشناسی استان تهران: کاهش دمای هوا از فردا آغاز شده و این روند تا روزهای پنج‌شنبه و جمعه در بیشتر مناطق استان ادامه خواهد داشت.
🔹
از روز جمعه به بعد، روند افزایش دما آغاز می‌شود و پیش‌بینی‌ها نشان می‌دهد این افزایش تا اواسط هفته آینده ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451414" target="_blank">📅 16:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451413">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE_3TDI05lY8Aaqc4Q_khK7QXoV-9L2XJj62spaIZMlIPSiZZ575kYN1r7vwevTuEXEpOPXVoFU9ajWjGtMMSV4GXtvG8hZOTgTN3Wv8Y9efie4_QJEwSDKwsI5j08CSEVghkTR52vJzlr9gGr6Ph7Doa-9qoR_5cgTupMNolxNnUaMfGKvRNYmCXV1hf8rBZ6U0cnn1utZ3mTpiftAGYXq1UugVPFs5Ccu58Hs3Yu66aKpLCRt561mwOKfHdwqQXFr9aUwjcpDcdlGGrlElOJ9XVAEHIXACHbeuhmA2QbIHzyNkyEqSzvJ0l_fWgIdgYNx1hChYhmrRkqW-Ge8Isg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با آغاز فروش بلیت قطارهای مرداد سامانه از دسترس خارج شد
🔹
طبق اعلام شرکت راه‌آهن پیش‌فروش بلیت در تمام مسیرهای ریلی از ساعت ۸:۳۰ امروز آغاز شده که در حال حاضر سامانهٔ فروش بلیت از دسترس خارج شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451413" target="_blank">📅 16:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451412">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4ZPJUbNI_Hl-3Ju7UaAfP8O2zrWEWD1folMUa9SGNu2r5Hp58EqPZiM-Ub02JxzOnt0JM-ClpVPL_yD7ZBs1rMyAAxnBueyJADdgf1RdUxPBJp-37RtGEdjhAoQrowseoAOkUQupKG2iZ42P8742u45MBeoQe3ktkWG__SwAnH7aRr8g0ZEZ8MC1UQSj5G9BuwV8i2VRNwZh8mBvVhQtg9O7hDLmNxjhGI1kPwnnHz_xKWGMoJeX7n3WEwDbuFlchFxjzAfN_jzYhAKGrSBGYidvqrBpmjtof2RJo9qXvqzKyBpUvPkXttwBZ3NPnQooLxXOChdizxbsj6cD7_yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
افتتاح باجه بانک شهر در زنجان؛ گامی تازه برای توسعه دسترسی شهروندان به خدمات نوین بانکی
👈
باجه بانک شهر در شهر زنجان با حضور دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر و جمعی از مسئولان استانی، به بهره‌برداری رسید تا با توسعه شبکه خدمت‌رسانی این بانک، زمینه دسترسی آسان‌تر شهروندان، فعالان اقتصادی و واحدهای تولیدی به خدمات و محصولات نوین بانکی فراهم شود.
⭐️
به گزارش روابط عمومی بانک شهر، دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر در مراسم افتتاح این باجه بر رویکرد توسعه‌ای بانک در گسترش خدمات‌رسانی به هموطنان تاکید کرد.
دکتر احمدی اظهار داشت: یکی از اولویت‌های اصلی بانک شهر در سال‌های اخیر، ارتقای کیفیت خدمت‌رسانی، افزایش رضایتمندی مشتریان و ایجاد دسترسی آسان‌تر، سریع‌تر و مطلوب‌تر مردم در سراسر کشور به خدمات متنوع بانکی بوده است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451412" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451411">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYSpMQWL-fJBOnXYBsb2IKiXQ2HzMZMOWK17g70W4wLRsnfVVBHphJLOj5HBKg-8PFnkUkoz_mwvfe3quLWc03e6eH50ip8Em2wej78j1ECqSMhGtkiwSylr1z8AkHRqjN2DNhyfh_ov8dfO4-ZLKUYJaiIKfKi52nOiR2_3u8CcT2ECuGRyH0ClNnYuGitHcrP8BlXeQnkMj4nWJlJqm4b8z5Y29jZ957Ub-jPBNSdC8J7Z9VMvFqC0eOrs9KyjUF9DodzR3DepxUFA70qHz8qLPBcq_Iw-5mJNgThvYf_KmTcKJh0e1_fsIrFq3Md899vS00ZpFQ_x0rkm9kM7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451411" target="_blank">📅 16:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451410">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/451410" target="_blank">📅 16:19 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
