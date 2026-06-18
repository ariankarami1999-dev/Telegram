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
<img src="https://cdn4.telesco.pe/file/clmfUNAIiZFN6c_UxsrBsPu8z_6scjlgBKSprpmbDi5lXHyvjAu_7f8YX21QA-vU4JxtUx73OaLrF_R9cMRLZo7kKnTwDxa9ZVC9tTyV_09hgGjavAkBOAXqkZkilzlDQ-jw-8SS77noNyWNuaqQdZKFY4yI5sIAvkzQL0UF8wRckI1PHZVvNH0f75ncug-Dy10gKIir5e0EzJsiUfaV1xKNrgj_gWN2hovCK2f1yUyCQXoMN6N6qDkOP-jo4hV2L-Mal_rxmb1IHn8CKJwNNf0Pu131jfvjMdhn3Ruq03sNTyLAATLDRnK_Hzpo05TyX83MtxGq0B0XxALmtlcLAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-443010">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
رژیم صهیونیستی به حومهٔ شهرک کفرتبنیت از توابع النطبیه در جنوب لبنان حملهٔ پهپادی کرد.  @Farsna</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/443010" target="_blank">📅 09:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443009">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
رژیم صهیونیستی به حومهٔ شهرک کفرتبنیت از توابع النطبیه در جنوب لبنان حملهٔ پهپادی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/443009" target="_blank">📅 09:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443008">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd3299bc0.mp4?token=pbaOxkl4JiL0nuMnV0dSOREuDTh-S13_1wYdqR6E8L5zRGoekVhsje07FCEq2uxigJZEQwjx2Nz7faLubefFef5TC9E9AECWCjI-WJ3Cls14Zczdvzr159GZZegmw-8K8t9NjLTLoRLRj1pKWurmZsHddD_e7fd-GIkelet431bRVJyn-W_I3j59DzogyiRq1rPR7iKfPBb0D3DIslnjPJfKK43MPXXdZLYVwyGTQ6Bes_HGwxsXTgvz0m51EV0Ed-u3FCFxkZlFkUwrSeextqcE2s_ecb8TioWP5DCAmilumhKCankTPl7C2uqfckY9GkmJLkJM8eUHOEf-HJz42Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd3299bc0.mp4?token=pbaOxkl4JiL0nuMnV0dSOREuDTh-S13_1wYdqR6E8L5zRGoekVhsje07FCEq2uxigJZEQwjx2Nz7faLubefFef5TC9E9AECWCjI-WJ3Cls14Zczdvzr159GZZegmw-8K8t9NjLTLoRLRj1pKWurmZsHddD_e7fd-GIkelet431bRVJyn-W_I3j59DzogyiRq1rPR7iKfPBb0D3DIslnjPJfKK43MPXXdZLYVwyGTQ6Bes_HGwxsXTgvz0m51EV0Ed-u3FCFxkZlFkUwrSeextqcE2s_ecb8TioWP5DCAmilumhKCankTPl7C2uqfckY9GkmJLkJM8eUHOEf-HJz42Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد«فلسطین آزاد» هوادار تیم فوتبال انگلیس روی آنتن زنده بی‌بی‌سی؛ خبرنگار بی‌بی‌سی برآشفته شد!
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/443008" target="_blank">📅 09:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443007">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وام‌گرفتن گران‌تر می‌شود
🔹
بانک مرکزی قصد دارد نرخ سود سپرده و نرخ سود تسهیلات را در ۲ مرحله و در هر مرحله ۵ درصد افزایش دهد.
🔹
با این حال این امکان نیز وجود دارد به یکباره ۱۰ درصد افزایش را اعمال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/443007" target="_blank">📅 08:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443006">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUUiCStuHTDWIvKcy6EDfB-yhb0L744uFfSUP9GC6hITfzuEwZM1D4PebZw6mMl-nhlKMqYJD2tfvBUjCnkFqpoedR2ouG1b-gNVTMpBENdMEhNrbv4lJ0519jlBxX-fyqmr9QYhkOvElpCflzp9m7orNcHzS772de3NA0xj-u6bOjnpcJif6_Exse6-58ktIsDbPtNHaQIiCuXdigmZsWPrFh-U6c9JSOxZ0REG6pgIniiDw9vaxmuZjQ9EgkG0sLbnnW68ygHxbKaxaQL0e62u2Loh1oO5qxSnJ-dNvTZAPqcp08IHUm7CxnExXiprhw5oGYaV0pIvQFwee5356g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومینوی ابتذال و بی‌مایگی در بستر یک پلتفرم نمایش خانگی
🔹
جام جهانی ۲۰۲۶ زمینهٔ ساخت انبوهی از برنامه‌های ورزشی مهمل و بی‌کیفیت را در بستر فضای مجازی به‌ویژه پلتفرم‌های نمایش خانگی فراهم آورده است.
🔹
برنامه‌هایی که آشکارا نشان می‌دهند می‌توان بدون هرگونه ایده، اندیشه و خلاقیت و به صرف حرکت در مدار ابتذال و میان‌مایگی، هر محتوایی را تولید و پخش کرد و ماحصلی جز بیهودگی، هدررفت وقت و هزینه مخاطب و برآوردهای مالی میلیاردی بر جای نگذاشت.
🔹
یکی از این برنامه‌ها «جیمی‌جام» است که با اجرای ابوطالب حسینی در بستر پلتفرم نمایش خانگی فیلم‌نت پخش می‌شود.
🔹
برنامه‌ای که از همان روز نخست پخش، نشان داد که بنیان خود را به ابتذال و میانمایگی گره زده و قصد دارد بیش از پرداختن به فوتبال و جام جهانی، به حواشی زرد و بی‌اهمیت نامرتبط به آن بپردازد.
🔹
مهمان اولین قسمت «جیمی‌جام»، هواداری بود که بابت فحاشی ناموسی‌اش به علی پروین، یکی از اسطوره‌های فوتبال ایران و باشگاه پرسپولیس به شهرتی مجازی رسیده بود.
🔹
در قسمت سوم «جیمی‌جام»، بار دیگر دوز ابتذال و بی‌مایگی به اوج می‌رسد. جایی که شیث رضایی، فوتبالیست بازنشسته به‌دلیل یکی از حرکات منشوری که در دوران فوتبالی‌اش انجام داده و از نگاه مجری «صحنه‌ای ناب» محسوب می‌شود، به برنامه دعوت شده است.
🔹
در پنجمین قسمت که با حضور امیر علی‌اکبری، کشتی‌گیر سابق و رزمی‌کار سرشناس همراه شد، ابوطالب حسینی از او می‌پرسد که «حاضری کدام‌ یک از بازیکنان تیم ملی را به قصد کشت بزنی؟» علی‌اکبری در پاسخ می‌گوید که نمی‌داند چه کسانی اکنون در تیم ملی حضور دارند و مدت‌هاست که فوتبال را دنبال نکرده.
🔹
در همین حین، مجری می‌گوید که خود او هم نمی‌داند چه کسانی در جام جهانی برای تیم ملی ایران بازی می‌کنند؛ چراکه خیلی دوست‌شان ندارد!
🔹
این اظهارنظر عجیب، بیش از آنکه به یک شوخی ساده شبیه باشد، موضعی جدی است که در امتداد دوقطبی‌های کاذب و مغرضانه‌ای که این روزها توسط عده‌ای در فضای مجازی سازماندهی شده است، تعریف می‌شود.
🔸
در چنین شرایطی کارشناسان معتقدند ساترا باید نظارت جدی‌تر و بازدارنده‌تری بر پلتفرم‌ها و تولیدات نمایش خانگی داشته باشد تا از گسترش محتواهای زرد، حاشیه‌ساز و مغایر با ارزش‌های فرهنگی جلوگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443006" target="_blank">📅 07:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443005">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7NN6Gj9KLvyLA1_xUW8_lH-A9FWCkZd8wdhr0BeNiK40h9D5w9gPZRs7L3vp0Rsf1JbVSCXeMZK0QpWOYUx5TqnziKy3aRmUs_thbxxIId2Y3AdBW3eOePTZU0JZ4XjzUev6KS_SmEse3AfEZ8MxTMolvvLU-lCl-39ajB0rBfJN9b2LQTljboRFg6NuMYr9YnjdpFdAczoBp3r3xxz4uNWqCefPP4CN_JKKtrtx8pcEAimu8mVgEFJDO_ka8vhyhCG01AiNrzpBEtkTZeNTKyhtegVkexWQ7gRnT5ThcXI4MEbIErBCUTAPFoV7deQCee27vsuz9g3fyxoos7NWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محتکر ۶ هزار میلیاردی لاستیک‌سازی نقره‌داغ شد
🔹
پلیس چهارمحال‌وبختیاری: بیش از ۱۴ هزار و ۵۰۰ تن مواد اولیۀ کارخانجات تولیدی به‌ویژه صنعت لاستیک‌سازی، با ارزش ۶ هزار میلیارد تومان کشف و متهم برای سیر مراحل قانونی به دستگاه قضائی معرفی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/443005" target="_blank">📅 07:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443004">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ7X0GoHvsk9dYF5UDkR4asc5uJmiUfGgE6RFiR3-gEuG5pkxxIZS9nCz9iDV4Gxbq_jvBuTsunZCYrFQ2852tPsJ4f-dGUbHOgbcsGbjB1Wv6ZUZYguI7rvRtQgPPlaUIMNgJxnIh5Uu0aVMlfOeszDDNGdbEeUbSmrERvWhRWWRwwrxfC3cp_bQIeb_b5ZPH2VLEy-P5LKythLVTYhuGZ8Xqxzl2yj9IvMo42bqjIgaRKfBEROyIlsMmzYuJQUhcyi_6pyh64ROp0OGg5DHmoqRyElRG-6dukG23Vu6Hb337_kTqJDSoLj66kCeEhDx12--S3yxrriRmUjScvm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دژ اسرارآمیز ایران در انتظار رأی سرنوشت‌ساز
🔹
قلعۀ الموت قزوین، دژ تاریخی اسماعیلیان که به بقای حدود ۲۰۰ ساله این حکومت کمک کرد، اکنون روی میز یونسکو برای ثبت جهانی قرار گرفته است.
🔹
وزارت میراث‌فرهنگی، اعلام کرد ارزیابان یونسکو از قلعهۀالموت بازدید کرده و پاسخ‌های لازم دریافت کرده‌اند. نتیجۀ نهایی ثبت جهانی الموت در نشست کرۀ جنوبی امسال مشخص می‌شود.
🔹
پروندۀ این اثر به‌عنوان تنها پروندۀ جمهوری اسلامی ایران برای ثبت جهانی در سال ۲۰۲۵ به یونسکو ارسال شد.
🔹
در صورت ثبت جهانی، الموت سی‌امین اثر ایران در فهرست میراث جهانی یونسکو خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/443004" target="_blank">📅 07:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443003">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX4sylsr_rogiq1NQJV7EuZeb52MIBIdpG_jVmvUo93ZKOFUe5FXSzdyzsRcvjaECA7X2MOYW_hZyWpYrcVjJaqJ8Lgm7WmJDFIyzIB9ofBkfGOQkvIqgs5xPMUE-HkEprTx1kRjYByWUomypro-1QAmgr8cV7IOHN1JiYPJx-mOf4vKhReRWH1Kt7-EoiQ8toHYs6WMRSD5X47pbBVE31iXkSQzIfyxtfPbA2XpNviiY5LvLEeVHqWKtm6fjmlAksDNtYrH6aC-sd_73BRtuHhQzPfyCB5GyzPjbUf7i_maU68eaftLzbBHgYXU3AN9wAZ-RJChBfqXlnJAD0zQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمان توقف؛ کاروان در سرزمین کربلا فرود می‌آید
🔹
صبح روز دوم محرم سال ۶۱ هجری، کاروان امام حسین(ع) همچنان تحت مراقبت نیروهای حر بن یزید ریاحی در حرکت بود.
🔹
در میانهٔ راه، پیک تازه‌ای از سوی عبیدالله بن زیاد رسید. او نامه‌ای برای حر آورده بود. مضمون دستور…</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/443003" target="_blank">📅 07:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443002">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec809c01d6.mp4?token=DiJwyHr7Z6xFofpfK3LrDeSgH0S2JAhQMZLEIK4n8W6RfFmo05FjTKM6iNQtWlxK_k9-Zpn6kNm-86ioruHsyJGQjw_KV2w3cTYaVkiF6xK-t5rTaRKn9MyJglJxpeUUEvB6zS8J7sPdJzX_HlXyxgVOA5clItoRM7CTr03zbTX278_rHw6XDtbiQeFFVWtuShmooOkxBpA6iYYI5Ue1Ej6wlPxdv2gD9hr-s_RUmCLSR2ANsoysMklvHLguDbAAtCFCw7OGtfYl-cRLPHSO9wQL8T43P-g_STvAriEM6u1xWK8Y43Zbo3d2e7RFkLm3fcHpFsq-4RecyO7Mp3gPZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec809c01d6.mp4?token=DiJwyHr7Z6xFofpfK3LrDeSgH0S2JAhQMZLEIK4n8W6RfFmo05FjTKM6iNQtWlxK_k9-Zpn6kNm-86ioruHsyJGQjw_KV2w3cTYaVkiF6xK-t5rTaRKn9MyJglJxpeUUEvB6zS8J7sPdJzX_HlXyxgVOA5clItoRM7CTr03zbTX278_rHw6XDtbiQeFFVWtuShmooOkxBpA6iYYI5Ue1Ej6wlPxdv2gD9hr-s_RUmCLSR2ANsoysMklvHLguDbAAtCFCw7OGtfYl-cRLPHSO9wQL8T43P-g_STvAriEM6u1xWK8Y43Zbo3d2e7RFkLm3fcHpFsq-4RecyO7Mp3gPZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ تاریخی برای ازبک‌ها؛ فیض‌الله‌اف اولین گل تاریخ ازبکستان در جام‌جهانی را به ثمر رساند
⚽️
ازبکستان ۱ - ۱ کلمبیا
@Sportfars</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/443002" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443001">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRWIPjFxurraBoTsLlcQX6tmwXRZkvrV5J75W-f4yQkyQQb-tIfW-y7fEY5u25dWidSYDD-2Y4RBarialn2ZnbREJtUzpKo2rHb00BW3kSg-KddLWpVG2AaYwt-8kUpwfxyET8iKtZLNe_guZfxjb8WR9GWAWKqoKNmRICpP1epp08_hkhmiDbhEOkRRdJoiWGr98w8hEZ2vmnPdUu0QNMyeUSMpfWq5fyRLZF7SnGFg_a9o9_qPuHmM3FWisprbaRL1EitvPLuDPX2-HcqGwAPYhVhGAkqzdBcGlbVTsFJFRedekRZSpph_6MtN8ODTpZteQDDtTFyhH8uzWhTyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرب‌الاجل دولت به قایق‌ها برای نصب ردیاب
🔹
سازمان شیلات به صیادان یک ماه مهلت داد تا روی قایق خود ردیاب نصب کنند، در غیر این‌صورت سوخت گران‌تر دریافت می‌کنند.
🔹
این اقدام برای سنجش واقعی پیمایش و تلاش قایق‌های صیادی، انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/443001" target="_blank">📅 06:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443000">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b8fa8383.mp4?token=uG9kWoCae7On0TcfpN4d1tQvSyPjM4JPH2SP4hsUvU-JSV-gbrIx2ucdZf_G4oSWrcosmm8HsEbTfdU9mJvJf2nj_6Rzgxze-gVvsJv_BBCJ-p65Mi4VBXB9AOiOUhl6T9NINvQR7NOFAjiU7wI_XG0pEvIvZyByX_aNfH4ZotOYGx7J45sGZBGmU4CgFSJYE19yFerNrdDB1jcBqT67wzcuuBxQTZ_sxQlJhllCFa9_tlNPQ-cmNqV7bBzV6bLvARTowSI4XGXx4XbUIfx8sevC3nkhjaszgHNnv72n264TWeNKAFlKhC05h0xpeH9q99Wk9m9zb0XG0yXp1Rdumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b8fa8383.mp4?token=uG9kWoCae7On0TcfpN4d1tQvSyPjM4JPH2SP4hsUvU-JSV-gbrIx2ucdZf_G4oSWrcosmm8HsEbTfdU9mJvJf2nj_6Rzgxze-gVvsJv_BBCJ-p65Mi4VBXB9AOiOUhl6T9NINvQR7NOFAjiU7wI_XG0pEvIvZyByX_aNfH4ZotOYGx7J45sGZBGmU4CgFSJYE19yFerNrdDB1jcBqT67wzcuuBxQTZ_sxQlJhllCFa9_tlNPQ-cmNqV7bBzV6bLvARTowSI4XGXx4XbUIfx8sevC3nkhjaszgHNnv72n264TWeNKAFlKhC05h0xpeH9q99Wk9m9zb0XG0yXp1Rdumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخورد شدید بازیکن ازبکستانی به فیلمبردار مسابقات، در بازی با کلمبیا
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/443000" target="_blank">📅 06:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442998">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd9rtx6y2mO26FeS2ci2mqlyPiY6YsvijOXkZ3zkiLIILk4Yf0_gHY1l-No6dKgDiBZ9pTGJiEMgStV3HSJCh-PQQz53eMXqWWPAauU9ScuUmEp6Q_aKlisTIh2ydIRYaA82vnOsweXOfP-UU359_8zB15bzlDOOr1F68ahuWNcMuq063GhSGBQ1dNAnDBJop8ziJMQUN85V7IH_8WpVWPtTPXN1ydLuF_EB91y78YyZfYhWUBtQCwGXWsQGYJNJM-ZhxpkKn76Kh6mCirY6kH2ZuKzSPcBnfYZSMPNa0nd3Q2DgfMUv3eUqUZ9M1fr-9U4lg170MOJVw-VqVoXHqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم اشغالگر ساخت ۵۷۶ واحد صهیونیست‌نشین در کرانۀ باختری را تصویب کرد
🔹
همچنین این رژیم با ساخت یک ساختمان هزار متر مربعی در مرکز الخلیل برای استفاده به‌عنوان مؤسسه آموزش تورات موافقت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/442998" target="_blank">📅 05:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442997">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مراکز انجام یا عرضۀ داروهای غیرقانونی سقط جنین را گزارش دهید
🔹
دادستانی کل کشور از راه‌اندازی سامانۀ گزارش مردمی سقط غیرقانونی جنین خبر داد.
🔹
شهروندان می‌توانند از طریق
این سامانه
، گزارش‌های خود دربارۀ موارد مرتبط با سقط غیرقانونی جنین را به‌صورت آنلاین ثبت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/442997" target="_blank">📅 04:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQqirX36bJUXAPAQxB4rCp5xWm_-OHBPTKMwsLb_TI5CQPrTqanvy9YnBpk6aJAPHFtIipLJ1qYql8TzpoWvQecUq08Arume5zGlf4g7zHFSRcPIs_dcFuCrjLR_BcCXL-6b4QlOPbE5d9esmVcNyjlcagLgUUms2xQsoc9NjM5tAKEIa6-gB3Gl3y8JY16cAE8epylmNmZUYZ1vxF-FfcbC7Ga72WpGvohJv8OsTEjAVrbijzpHLxpjj2IWyp5FcoyCBu1yu69EUqxtqEoXF6eOgfwsuSL9r7JnbENawGFWcW8CzRjpSnAf8LMG_mJMrJ_A0pnAvFAIImQdlnc5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqRRnPD6wKTm-X13i9ySBtADZCT0hs1Fv9hrMkN_Z3FB7emPXt6XYQ0zbTsCWE0X08gSN1GrZfUHfeNKyOKnNtGbfRajn-TNbvdp9eSqXqsfAqghLS9x2qmKko_gkdLUXvApqxmSHCfIpFREW1Nd_O2ybEZdwMAXRfRQAtRh313qF2VNI4e91cAyt5-CABgjAeGdwhfHKv2qqPQM2ERsNA4zBCCUFeBG2I46YE72gVLb7UmNfy9NCB3ZSF5K8MCXmaM46eUuElRvajLze6saEZdhv0Ha1AyIZ-Dpb6TrVgS_T-HTGA7FwLb_GFoMIavA1Rvdifd1WLpJcWB71X454Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTvKOIjqJdg3b_bg-bZMCeJWF_8nd5Q_DuwSFudJqnxg9mKX5kpIq3gBaiPT12pVHrU1M2XB7L38yubDH4Iu6Qv2IbISWwb0DftbiMIOK-9qbBCdFM7uH92QJ-WX_f6Fmz6BiSdzV1MKv-OXC7KEGR8OsvnNS8g1JJ7wFFonGLXxNJ59vfc_JV-MWAXUn79QUZFVE2xMzVAfiR2PjV2dtwxJW4u5YGJFfLT0mwS56hB3B_8ReidedyYy-JKoTA6EPrys0IVVgf9pQRyiHzQ3fXlnqU0zdQTs6Xx5RQmdqwdcu2Q8AOUGkA5p0AI91A_pt6QPGjB9ok7crsMk1Z037Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaCMdxz1swiA3t6jRFoOYPX_7ViJsN10Bp5spZ14K8JlffWlnJUHrx79WbPNXmLX7YEz8B4GN26QTPS-fniGnn5oHcnvouw4amqIihpe8TNEDJYADXp18uopMhNlt9JSG3upttyDPZCN08jKzC3EyakN91s2B1o0vjC4i8KIaD-Yxn8fgWvutqg1UXSvhVZopewY8Vo6dXySwIwbJYvsyOhzMf6bCvQw66P7St0Hr1q0b0WmVRPdnkPyNbHQVAa2Uw5Pkp4nam-3BXp25LxQH52ybSZD0t-3sPfS2hrDbzZnInLoUiU-4-mGDIkGaiWxp1g4ZW5hcF2TYyNLwZi-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzfjANHVD2fevrmIWvJdLy_9juMoqr28Ff6xzQO3PbS6FPYMlsY61nE2K6hX7WSQn9g4heKXgL1BdenVMHWcfVWdP1eYjBAn98_hfUEQy9pWFc_r8jNKW-Roc5DtuKVn6_Iu9sSSzPtDt6q5NchEaoxS676Uyc5p9nEdMAY68lUZ2iTst52bMgPj4NimFh--EmLZCdTUAtH1R974Or8P_FxrDkPaM7uVH8C-Nu1DSr802QDPOzDsZ1P4cFpnPRd3b45E-9GRWYZW1EzvKy9c3eI2_n8oMvrexKWESxspDhQ6bsv4tBu7TvvsQvZZ6nsRWdPNZIkZ_8Ea3-spjWQLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aN1_Bz_jtiMAF_3Ff4yNdC0xXSpT3bQG6MNGARqzQ_ajjwXPx-JIXzz1ZyGWqGqevHpe843CwvaJk96Hb1JoiWLFpqQ8c_OHss0voZ2DFzJCY3hkx7QY5H9C5SaFkoALUDpDNIdDzGg-PHZHhWxIAzKI7GS1gtJMdQEQjWCSJeUjC0b20Vr23tCDJ-avmnRwBPooKP-KXN-PI3DgOZcY2wJGveYFviAuXnObXtQ4QfVyiagxKLckNyiDRE6F2nY_jd8KS5sCQG_uVd3g8oR5hOY8xKwXthOA6Z79bSfe6tLF0Bu3NDvZiNm8_tq2GGcH3YXsTZt2RiztgY-WvM_7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JloCw0GrIFCKSk2Sg3CxD7LQA1I1FP1tkNYowiMOY3GMeKMsjt6cM-zbu0tpxLGd7Pvfa55-mQ_M8U_t8xP4dI1hfigEl4Rt7z6tk5k-TfRPbaBKZyAoXifwHwpQSo0z0wSZLlkYJ3e2a5r_0gJuKbgYOVCghoaYSkZWTC-7ezYlgqVMSKxF9hg2eAbITnUcv9ivpnXswDkPI_gI7giZnmz0cUPUgQkAK_4lpwXhaEDQhTcBbkdyeFPq81Yv2avLOaK29sucWiCJXvBDRz5klnatb3YrxHcFFdBxmuNrkpOExcAKJK-Yphj_HE2cYJo6uPauduYFLGWHt7_6OVbNdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حسینیۀ میدان انقلاب
🔹
عزاداری شب سوم محرم ۱۴۴۸ قمری با حضور پر شور عزاداران حسینی در میدان انقلاب تهران با مداحی محمدرضا طاهری و حسین طاهری برگزار شد.
عکس:
محمد‌حسن اصلانی
@farsimages</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/442990" target="_blank">📅 04:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442988">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab312e049.mp4?token=O5mo93QtPQn-zhWeX4f4QN8vJRcJRrFDUBbPVRbamZeHrUpow9nEoGScM4ycit3uwecsdKZ7RBBOcGrFGywiQseHHHllMHPSg0DtqOOFyv2tRqUlfgqH3LA3-vGb3NbOjWUfMhq_IWEfVmGTRnD7JZ_5KgtzCoYrjaNo2A5D9yEyiJodUwM7rlR7z0rkG2H80uIVrEIfCXUcgvjU7LFUbyPHCJEMhwAaM31Xw7eGIzPDthEi4FSZZFr3en79DbSpY-N0n6zGt94aDnpyaZhQ8NVa4BrcNNi75S5t8OayX_BFqFjncUF8kIQ9IZbj3_zfpeXMmEWkcznC1rj_PFWUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab312e049.mp4?token=O5mo93QtPQn-zhWeX4f4QN8vJRcJRrFDUBbPVRbamZeHrUpow9nEoGScM4ycit3uwecsdKZ7RBBOcGrFGywiQseHHHllMHPSg0DtqOOFyv2tRqUlfgqH3LA3-vGb3NbOjWUfMhq_IWEfVmGTRnD7JZ_5KgtzCoYrjaNo2A5D9yEyiJodUwM7rlR7z0rkG2H80uIVrEIfCXUcgvjU7LFUbyPHCJEMhwAaM31Xw7eGIzPDthEi4FSZZFr3en79DbSpY-N0n6zGt94aDnpyaZhQ8NVa4BrcNNi75S5t8OayX_BFqFjncUF8kIQ9IZbj3_zfpeXMmEWkcznC1rj_PFWUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقوع انفجارهای مهیب در اوکراین
🔹
رسانه‌های اوکراینی از وقوع چندین انفجار در شهرهای مختلف این کشور از جمله پایتخت آن خبر دادند.
🔸
رسانه‌های روسیه ساعتی قبل نوشته بودند که نیروهای روسی در پاسخ به حملات اوکراین، تأسیسات نظامی و شرکت‌های صنایع نظامی آن‌را با سلاح‌های هوایی، دریایی و زمینی با دقت بالا و پهپادها مورد حمله قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/442988" target="_blank">📅 04:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442986">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jt2PUTxs4YjkPcVp_VuoTf3rFespxQ0ksTybnOs7gyJ_nxzVaFgrwD62gIAFEy1X0pD9VeAPNkUSB6lGaKR6fkgKA8s8YZLDVcgp99OgQx9Czrb_F_Tqd9DAnAXWxrWFEiG8s9DztCwGeWUnUaVpBqKNh0EpIEzizPHQBPISdUgiKs-NJQ5raLmVRgjudwueVOUyJXEAIS2L1YC6qKKHL6cARb4Pr0UopxRwjWqWi1lbrkz9GqDwUArWF49lmNdd9FS7M0wf2dDVAlsl3NTFjnqWstxbQcVG8QePEkFpjbZPRAAekyzTUQ_EBu8KNKEvKedRKS_E196pDhMN71SHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3zRHaqXMfvL3iY8ipQYT6BoqkKu8fd0I1Ck0OGEW9J7aaW6v1Dr4drITkwt4F3wLB1F1W4XF3OcEsZbhkHMELTfiojlwmDaVYRX1wY8Ye957B-MWLUt3vAjJOl5sEN8QQKoX0BQ-ydWzDojD_SW8CFHZAO11M7vLt_ZqRys5vm4Kl0Ol09j3XAD8MCw0a4q22KmsTAQlpYUBXIzeYogSrhF4nfcN1VEGHbxVTbS3tiyur9TGlQBYnbB2u_ouM_atfkJAD3y0AESp2bo-LStrivINC-sG9WVr8GAoh6xI9me-8aVcUGJiN8IFBc0B4qEwe_-bpNuOsnqqxRcgLIaug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بقائی: متن تفاهم‌نامۀ ایران و آمریکا الان رسماً نهایی شده است؛ چراکه دو طرف آن را امضا کرده‌اند.   @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442986" target="_blank">📅 03:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmCsIgHXEHoi3vC0ykbH7d-U5cxTxwkrZUAVnoEpPxgPPPYRYxI9DgModao2ZrajqxOt_aBCoMCs45dyjXflTjOV-B1ZnbYQesvCuLvSpxmcmD-7KnujOrrrhE60NXexyoFlRFTey8xRpz7VebThk68ZyghNOfZx-zT91ygZHfMq5yF27f66by3z1NcgNoiArkFABZjI1I0wVInLVwGvdcGmRH5NB9uro_zyGD3wolzR6NMyBOdFgbCH760t5KRNVmUcEqYq6VWfQfNFIrCsyFemwSZSNVPDMlFfumm0KtphcboKJTTXdWxhgRQrzpfnfU5dY8gL0esMMUdFwBgvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ آب اسرائیل علیه فلسطینی‌ها در کرانه باختری
🔹
رژیم صهیونیستی علاوه بر جنایات علیه فلسطینی‌ها در کرانۀ باختری و تشدید شهرک‌سازی‌ها، منابع آبی موجود در این منطقه را هم به‌زور تصاحب کرده است؛ امری که در چارچوب سیاست کوچاندن مردم فلسطین از اراضی‌شان انجام می‌شود.
🔹
سازمان آب رژیم اشغالگر ادعا می‌کند چاه‌های غیرقانونی رصد کرده که سالانه حدود ۵۰ میلیون مترمکعب آب تولید می‌کنند؛ و فلسطینیان حدود ۷۱ میلیون مترمکعب بیشتر از سهمیه‌ای که بر اساس توافق اسلو تعیین شده، آب برداشت و پمپاژ می‌کنند.
🔹
به‌همین بهانه دستگاه‌های امنیتی از سران سیاسی اسرائیل درخواست کرده‌اند که دامنۀ عملیات اجرایی به مناطق A و B در کرانۀ باختری را گسترش دهند.
🔹
این درخواست با این ادعا مطرح شده که در آن مناطق چاه‌های غیرقانونی حفر شده است؛ این در حالی است که تاکنون نهادهای اجرایی رژیم اشغالگر اختیار قانونی برای فعالیت در این مناطق را نداشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/442985" target="_blank">📅 03:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">انتشار فیلم لحظه امضای تفاهم‌نامه ایران توسط ترامپ
📹
رسانه‌های آمریکایی کلیپی از امضای یادداشت تفاهم ایران توسط «دونالد ترامپ» رئیس جمهور آمریکا حین ضیافت شام با همتای فرانسوی در کاخ ورسای را منتشر کردند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/442984" target="_blank">📅 03:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
رسانه‌های عبری: در دو عملیات جداگانۀ حزب‌الله در جنوب لبنان، یک صهیونیست کشته و ۱۰ صهیونیست دیگر زخمی شدند که حال برخی از آن‌ها «بسیار وخیم» گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442983" target="_blank">📅 03:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442981">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f613cd03db.mp4?token=nTcOrCI8zlKz6TJk1b6KaHey0gVrerlk4kgbJwHc_kVFNQvQoKWgv4gvpatHJ3uFC4uJuWx9ZDPEAtfMWF4daDVxAxdtuKIIFKHVVsJA9RLMeuqoekoolyhI07oFcmu2X5JPki52G36jfj4loLvPGvEL2alrPsF9BX5edq2o4631NWGTC8WKDXZkZoEkRrTmNNJ9FVMKaiPsVe5SQkAk44r0ZpwI5WkR-0-ZArkzko_YzOyL-dmDBKutu92VLSHP-a6JsV-HfA8pH7mtqMhpoR3lRd-LmjzZru4yDEQgAtAJ3fPC0_1pi_C_LKeM7B5Nxh8ig6hkNQzb6Gv8fwGyag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f613cd03db.mp4?token=nTcOrCI8zlKz6TJk1b6KaHey0gVrerlk4kgbJwHc_kVFNQvQoKWgv4gvpatHJ3uFC4uJuWx9ZDPEAtfMWF4daDVxAxdtuKIIFKHVVsJA9RLMeuqoekoolyhI07oFcmu2X5JPki52G36jfj4loLvPGvEL2alrPsF9BX5edq2o4631NWGTC8WKDXZkZoEkRrTmNNJ9FVMKaiPsVe5SQkAk44r0ZpwI5WkR-0-ZArkzko_YzOyL-dmDBKutu92VLSHP-a6JsV-HfA8pH7mtqMhpoR3lRd-LmjzZru4yDEQgAtAJ3fPC0_1pi_C_LKeM7B5Nxh8ig6hkNQzb6Gv8fwGyag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ امضای تفاهم‌نامۀ ایران را تایید کرد
🔹
رئیس جمهور آمریکا هنگام ترک کاخ ورسای بعد از ضیافت شام با همتای فرانسوی، گفت که یادداشت تفاهم با ایران، امضا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442981" target="_blank">📅 02:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442980">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آغاز ثبت‌نام زائران اربعین از ۹ تیر
🔹
ستاد مرکزی اربعین: ثبت‌نام زائران اربعین از سه‌شنبه ۹ تیر همزمان با نیمۀ محرم آغاز می‌شود.
🔹
نام‌نویسی همۀ متقاضیان تشرف زیارت اربعین در سامانۀ سماح، و داشتن گذرنامه با حداقل ۶ ماه اعتبار الزامی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442980" target="_blank">📅 02:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442979">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
روایت و روضۀ مادر مینابی برای شهادت دو فرزندش در برنامۀ حسینیۀ معلی
◾️
همه کربلا را شنیدند، اما ما کربلا را دیدیم.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/442979" target="_blank">📅 02:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442978">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
بقائی: جمهوری اسلامی پوست ایران است؛ و دشمنان می‌خواستند پوست ایران را بکنند.
🔹
هر انسان وطن دوستی فهمید که تفکیک میان ایران و جمهوری اسلامی، تفکیک موهومی است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442978" target="_blank">📅 01:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442977">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: ایران ۲ قدرت اتمی که برخی کشورهای دیگر هم همراهی‌شان می‌کردند را شکست داد.
🔹
ما شعار نمی‌دهیم بلکه واقعاً ابرقدرت هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/442977" target="_blank">📅 01:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442976">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: دشمنان به ما آزار رساندند؛ جان‌های شریفی از ما گرفتند و به ایران زخم زدند؛ اما شیر زخمی همچنان شیر است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442976" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442975">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: کار ما به عنوان دیپلمات‌ها قطعاً از کار مدافعان وطن در پشت لانچرها و پشت سنگرها ساده‌تر نیست و دشوارتر است.
🔹
چرا که باید چشم در چشم دشمنانی بدوزید که می‌دانید مرتکب چه جنایاتی شدند؛ آن‌هم برای احقاق‌حق مردم و تثبیت دستاوردها.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442975" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442974">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: مدافعان وطن در عرصۀ دیپلماسی، به اندازۀ مدافعان وطن در عرضه نظامی نیازمند حمایت و انگیزه‌بخشی از سوی مردم هستند.
🔹
بدون انسجام ملی و حمایت مردمی کار دفاع از وطن انجام نمی‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442974" target="_blank">📅 01:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442973">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: مذاکرات جمعه ایران و آمریکا در سوئیس قطعی نیست
🔹
جلسۀ جمعه تا چندساعت قبل قطعی بود ولی وقتی قرار شد روسای جمهور دو طرف تفاهم‌نامه را امضا کنند، تصمیم گرفته شد دربارۀ جلسۀ جمعه تأمل بیشتری شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442973" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442972">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
بقائی: ضمانت اجرای این توافق، قدرت ما، توانایی ما برای اقدام متقابل و اصل تناظر در تعهدات است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442972" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442971">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
بقائی: تعرضات رژیم صهیونیستی در لبنان ادامه یابد، نقض تعهدات آمریکا محسوب می‌شود.
🔹
ما آمریکا و رژیم صهیونیستی را از هم جدا نمی‌کنیم اما در شیوه‌ها و روش‌ها اختلا‌ف‌نظرهایشان کاملاً مشهود است.
🔹
این مسئولیت آمریکاست که رژیم صهیونیستی را وادار به احترام به تعهدات آمریکا به ایران در این سند کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442971" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442970">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: در سنوات گذشته تجربه‌های تلخی از بدعهدی آمریکا در زمینۀ آزادسازی اموال متعلق به ملت ایران داریم. همۀ این تجارب در مذاکرات مد نظر بود تا اطمینان حاصل کنیم این‌بار آمریکا به تعهد خودش عمل می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442970" target="_blank">📅 01:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442969">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
بقائی: باید بتوانیم هرگاه اراده می‌کنیم از اموال مسدود شده خود استفاده کنیم و برای هر خریدی از این دارایی‌ها استفاده کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/442969" target="_blank">📅 01:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442968">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: همزمان با تفاهم‌نامه، دربارۀ ۳ موضوع دیگر هم مذاکره شد
🔹
فقط دربارۀ تفاهم‌نامه مذاکره نکردیم؛ همزمان با متن، دربارۀ آزادسازی دارایی‌های مسدود شده ایران، دربارۀ بحث بازسازی خسارت و لغو تحریم‌های نفتی به صورت مجزا مذاکره کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442968" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442967">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: اسقاط تحریم نفتی ایران از امروز شروع می‌شود و در حین مذاکرات ادامه می‌یابد.
🔹
تحریم نفتی ایران باید برداشته شود؛ نه روی کاغذ. بلکه با همه ملزومات آن. ایران باید بتواند نفت خود را بفروشد، حمل‌ونقل و بیمه دچار مشکل نباشد و عواید حاصل از فروش نفت را هم باید دریافت کند.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442967" target="_blank">📅 01:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442966">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: در بازۀ ۶۰ روزه طرف مقابل نباید اقدام به تقویت حضور نظامی در منطقه یا وضع تحریم‌های جدید بکند.
🔹
چنین اقداماتی، نقض توافق محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/442966" target="_blank">📅 01:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442965">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: متن تفاهم به فارسی و انگلیسی امضا شده است
🔹
اگر فقط متن انگلیسی بود ممکن بود در ترجمه دچار مشکلات سلیقه‌ای شویم اما الان طرفین علاوه بر متن انگلیسی، متن فارسی را هم امضا کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/442965" target="_blank">📅 01:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442964">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: انتقال مواد غنی‌شدۀ هسته‌ای به خارج از کشور برای ما غیرقابل قبول است.
🔹
رقیق‌سازی مواد غنی‌شده گزینۀ جدیدی نیست. الان هم به‌عنوان یک گزینه معرفی شده تا راه را بر گزینه‌های دیگر ببندیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/442964" target="_blank">📅 01:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442963">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: تعهد در برابر تعهد؛ قرار نیست ما تعهدی انجام دهیم اما طرف مقابل از انجام تعهد طفره رود.
🔹
بدون مماشات، اجرای تعهدات طرف مقابل را رصد می‌کنیم. در صورتی تعهدات‌مان را انجام می‌دهیم که طرف مقابل به تعهدش عمل کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/442963" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۳</div>
</div>
<a href="https://t.me/farsna/442962" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۲ – کتاب آه</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/442962" target="_blank">📅 01:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: بعضی آسیب‌هایی که به ایران وارد شد با عدد و رقم حل نمی‌شود. ما برای همیشه نسبت به این جنایات مطالبه‌گر خواهیم ماند.
🔹
از هیچ فرصتی برای مستندسازی و پیگیری و تبیین جنایاتی که علیه ملت ایران اتفاق افتاد نخواهیم گذشت.
🔹
از هر سازوکار و نهاد و فرصت بین‌المللی برای احقاق حق استفاده خواهیم کرد. این‌ها خارج از یادداشت تفاهم است.
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/442961" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442960">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: موضوع تنگۀ هرمز به‌عهدۀ ایران و عمان است. فقط ایران و عمان ۲ دولت ساحلی تنگۀ هرمز هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/442960" target="_blank">📅 01:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442959">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: ایران در ازای خدمات در تنگۀ هرمز هزینه دریافت خواهد کرد.
🔹
سازوکارهای مدیریت تنگۀ هرمز تا حدود زیادی با عمان بسته شده است.
🔹
تردد ایمن با حفظ حاکمیت جمهوری اسلامی ایران بر تنگۀ هرمز خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/442959" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442958">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9D8BuIa0t_MhMEvf9kT5Fxq8s3wr35jZ33VNTYCa5PgAFjFILNaDdcZjMUAeKBNoRJzfoq0mfri_FLjVJt0gF-c6pXNQLKh_SvEV7nh43oVO5c9N-QZXoP6oK2HO3FcxaaGANKw5EmcclMtZDiHivWA3UZneZGfAPsiKhSRF34kEYGo4P1AsaBXH4gDNdRSz9l5o2Go102eVRt9euXR20wQy6TXf660bKuP-KPFuy22ZVAPpAWctauUS6YsUkDQJF7ZH_JsFidOVANJ8rRbx0ZZBrtWzBieSOcTYe4o1jSRRosGK8hXFw3X_crNab60JVXIFPacl_VYCkpSpCGOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن امضای تفاهم‌نامه با ایران را تایید کرد
🔹
دو مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفتند که واشنگتن و تهران، یادداشت تفاهم برای پایان جنگ را به‌شکل دیجیتالی امضا کرده و اکنون اجرایی شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/442958" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
بقائی: موشک‌های ما برای شلیک شدن هستند، نه برای مذاکره.
🔹
موشک‌های ما اصلاً دوست ندارند که کسی دربارۀ‌شان حرف بزند. دربارۀ توانایی دفاعی ایران در هیچ روندی و با هیچ طرفی صحبت نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/442957" target="_blank">📅 01:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
بقائی: از زمان اجرای تفاهم‌نامه که الان است، ظرف ۶۰ روز دربارۀ موضوع هسته‌ای و تحریم‌ها مذاکره می‌کنیم.
🔹
اگر زودتر مذاکره به نتیجه برسد، بهتر است. ولی با توجه به پیچیدگی موضوع، ۶۰ روز منطقی است و اگر لازم باشد، این زمان تمدید می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/442956" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442955">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: در متن تفاهم‌نامه تاکید شده است که فقط منحصراً در موضوع هسته‌ای و رفع تحریم‌ها مذاکره می‌کنیم.‌
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/442955" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: اینکه در این مرحله توافق خاتمۀ جنگ را امضا کرده‌ایم، به این معنا نیست که گذشته را فراموش کرده باشیم و درس‌هایی که به بهای گزاف آموخته‌ایم را از یاد برده باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/442954" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442952">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران نشان داد که دوستانش را در هیچ شرایطی تنها نمی‌گذارد.
🔹
برای ما آتش‌بس و خاتمۀ جنگ در لبنان به اندازۀ ایران اهمیت داشت و دارد. در بند اول یادداشت تفاهم، سه بار نام لبنان آمده؛ احترام به تمامیت سرزمینی و حاکمیت ملی لبنان آمده است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442952" target="_blank">📅 00:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442951">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
بقائی: متن تفاهم‌نامۀ ایران و آمریکا الان رسماً نهایی شده است؛ چراکه دو طرف آن را امضا کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442951" target="_blank">📅 00:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442947">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_JSiRHnOSxLY47NxTr0QnUK0Ni6kSDO6B-GJWp-fYyzcbrnxnxl5rqBRTCkFJLVdaDL-4_tK2doI3_BsczNAIqJwet5Tz9YhIcS4pfB3QC12164VRydbPFFR_NrQOOI41o224N0jIYxwQPC39URpE6-Nv4RW4AyBjEIuzdT4NPUpkuYoyvPt9RcDRWtBbo-N9xX43ysg5ZYGQB4PGWT_VTE4kdOJxGT--Z1DQv5SbVBk-6TAnFeU7Un1QC1p_vx8jd3MywtXpbbw6HlUKkfS6mgFaME06mJe-W4OjIQWM76GYxCrpAMwzRVdINGhR2tQfWR3bT78UcG0p1vTts0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8LCXNekmh_at0rQyREhv_R-XVFt11XqCV085405zaEmW0eQCh-GqeKOXy1j0LzPIxpC_gOUeKGC8ZmC9V3AgRNUglSHvYAIPyH_XNZOFUECY0loGRB8T0RuEDgtk5BLX8IrhS3ePsqtFhjDKIh-OblNErHOA-gT3cvamXjpKvqj_IEoqzFDvZaVmAVPe8KP6t4iYoROu1kRLLnjrfnON2uMlL4xCC-xAA0tcDUYy8JlMwwMfRhmba2DYqHYct8HTOCid_G3FQuQI6kVy53z5SSAyU8sRWPvJJDxxUT37Lp8noBr__1s5m3CfcUD_gie9SzNfmHsOvr4cLW8KLtVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxKjPgbU-pRp_QLdqaKu25d91ZRFI7ygOgtcJ_Jdae4c-6yCPljgl2m7d9KSW7PVPz5ONPqktCVgei-OMiU-m9OkxPVE2UP9zXFlkhx0H3Y8AJ0QYBrm4rlzcbZDr0uRzJk1OpA8UtxyI6TrTL1R9nwExgdqUHQb9inO1rIotLLkChJKWJBjXwZAIc60_zy-R52q48DA4zZPe70BoosNSjyz7IeaHXOpadmnwn2Lddmr9mzJN8GwQexNAtJbijtmtHuqt5yFED_wb-QwtL5LXI4hQ4XWA-jVoSLKWyaqi_A7wLemhZmnfHD12paSypx1cvy__WLpw-Qgxix8vQ8AiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJMQoNH-5xgYdvTQix13_uN2cYNwwGZkJ3gVNkl39sjF5481Npq4RvVF5sB9rgFlGWcha7jYl2uKgq6-mnF3KZZULQEI5e8B79cZCjRBZZtI2NZyIpo_7qjpmbcpz0tDrpE3iB-7HWl6wPb885LjRMVQvg01QyWNcw96eJtfkg9t6CgXyuVsfQpRvzI8264fEGtLVoxtFl83jzl105NY4YFPCQNDSDMSv4x7iSEdI40CMIKAiuHKDfZbBa-bOwMzHpR3wDu9JhkeH2HfD4eGDHbVjirCpUpGFyUkbuciNE0_gRBnCDxbYAJxd8jqi5Jwho2V3kLbHNbw8Av-SN_fnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۸ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442947" target="_blank">📅 00:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442937">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s4GsJaGvL_0I5tn8XWeqHQMcxI95tpUSs2vhm0qIpwswx2ZUS8EcrkptA0FRAICCSqCixdbCdnTQDtorDlKq3Ko2C8odSETC2WAHSo6b9A4lsNbU5cBBUOO1pVo2f_of5m8csk3G5Dk1NOkBoLSNlM1Po2tvv611AH45jbgTzSgxO0f7YqegQVldhtv7iwfZ1UtskoA3ZvS3YIQb7SXeFzCQH36okvYb6M16Z-yLDI46SA_YpV0FDFQIUuXyPv3BTvIPT9IDE7D5hGkCC2jVG45EFUMYjs91S_xZRfvvBBAn9BSulG5tSdTBSawOZ32hKdrJ22LJaq-qLUxR3c01Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGZMwx6Uf95rIB7as42sOzqGqksV4QCpN8kOlsEyHr-fTt4t7rvZPwt7dgpPqhOg4KIYF2SvPYk-ytloxqOANt42B66cdRHuhPTqMqGuCBX2BbU489INnhOADIheAqNgZcKlsM3fhm5_BCFwyWWhkNy-ABJbQQj8rQhGwYHrfbm1Jboj10ejZYb7X4JxuBRR7_7ipUEYGKeP_BsnTmTb9zkrhu_-s7e_PHVQ-7MKLcqNSiopiNwP8dO1dpWab-ZTaJASyAhXg_SjHV7itrUH1aR_kCEGAfW9oe73b-iJS5MIjoZ2-7GvCGhmCA3ZlU9oviOrPx1wLVwqXvD2MAMHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxBSIdb9qx3-JaruxkUmc4ZacQSsraYl6wULO07Up9S_mvN9xLu_z5nTfXf5RCUvNwR657P80q1GEIxqS6g6Q4-Una6sMThvQhu4tHzbEdF2gkH-G60oZKblknwErjh5vYH8Seqa80qKr5G2zIv6-jtbCOqbfl1z2sMJSpCUOpa9fGu6QsShhOUz9mnU1xtObYq__zIeiafVveyyO-G9X-gPnp6CX_JBZ-TUX1poocOrCntbUPK0pA3Wt38joExzbuPeIDGVOSZXvAdTEYh7-PyBGRpMpvNCjWDOrSxK70xflRN-RpkFyRzMRuMEvwQbshwclaoTqLkxyMyjOXEuzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GtayXeqs7zPYIiLNTsxWnlBdbJEGoVNJLRGGrhVtifPT_Jpcb4AqBtiICAn0X0WSkXoqAQqwd0tbLHptIXr6sB9qNCNSnM1Kc6e_1juQf02aimMzniR2BzfidMVj_XzTB2DxgAVXD6K4hSn6XkKKYU4CZIwvGFSSjrfwFcckEJHb8iy2Pf8ZNY9gwuUb2qLFe65vcgZG-49XLRt4lQYOcqq2Tz0blPL1qAOahflp4y8xCc9LRTnaD9CHutjPUNVo9jgF3fNN-ns0jOEdoBNdtLzXvXegU42hwg4Qr0bmsPK4X0C4u-fGthbFpxOqnseUhPBzOFUn9B8r3OzNXPClQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cz-AYvxZ-yoX6qNMn0_PBPJVAT_jwLDNQtbzhXdfp1_3hTjNRXAUDTNG-SsBtNaRJbQWhno1V7j1AjPpfIAXWbtlwYXSqs6oKXcAmUBnOPhY2j8vLyE780oe2cx_z1LwwzdnMlTcIp83bc8J-Ud-dhgdSTCCoC8beflo5tGN4jL-W-zdeO-AjbahvM6diXuvY1fkEF7HTzjR1t9zmdlBmpSysfYF_ilvwoPjf0i2y9PyYg-_ypZqqesnZQKbPENtPueW8OBDpBHIN4-bArvJVRG-Qkmwi_IAzyXNPrLBwxNdZV0ul5_rNZj-wdc9LYlaVoLcjsnEFm0HRwgGg2DocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaInSGQnD9zZ8UeLskf09GR-cytk4ow7Fp1fZkJQ0uo-LlV0r-C9ZscfKuYWoLvLyaw3im7JhP16_5pgCz3E4klOJjdAMLzdibVTRmW5H5521rbSN2iiUKf9hcXjCvHFnoOlEH1Bzhc3xw4ht2isGB8TLSnv0H6646YokvL_BQExaO5p_JBl-Evv6bXeWKFNuc44ikqZJXLmunB5dnnGfrJ5f4pA150UaIvji-sprSJE6x-ywXl4uFWaniHo9yzijfGlexxXX__IOQrGlozBiNftu71js36eCfH6951VLsGOu7CzQyZ3Zz4LUAZJVKCkrhd0QL6UOik_UeX5-n8Mtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opMPuq-SDHPnLIqIvGfjLqtgnRoamANx8S_8tekp1WX1S7PoDrWFXQG1TpjQ4REykt3O3KtGpIjwK69gm8gtFL5E_I4Ctp2m_B_9LYgsxo0ZXch3mD293r_LvTYTk7ZqXujhbJfl-hfb9ufQOEbEcH48YVhyeQopBFx2_JiUg6K5q8N4-2nuTlUCwE253ChuUCQvclRB0HbN8dHnK13MWLla5uLCurIa07oLYqNzncbJG4r99ElDClJKNbgJPi-w8Iy3sYGrFZuVLQxKN3BZMx26M28RxI82dWQUxFrqKQ9Jbhc_uX9p_V9WIX7lppkxIKCQIHcbBRdGK3GjHoxHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPNdzZsb7hMJt94xdpHMDo5RbyKHn1sUvgSF-bCLOFg0AWejF5byFmeSaKBzygLps7hZEnObslL0h7aXqzo0MLzK--skSDk3XeKPvni40q-r42haGfIQJOewmjKMb0S6pas7UbzOsgvtaNCu7Gh7mgOKygFFxmq8VK5NcAU5_OQ8EYtbvu2c8KezKAx9heSlV9zOSXDgTjdVXvSwxQGtehRytVc63YbYuLQflJjfZZj1Go4fHZYrgfaM52l86r_Ldz4DO32d7jf53KHsG6jgZwYK37G7GRsNASu1BMSd-015WVZ62XWYfaqwiI2PlgAAWNbNeWIlKPktf_VuvdJp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4_4UVelVMtUqNZh4LrFRboyfi_tAUYygog-xk6db689DgANB4Zdrz4a074Y6uzVIOVAt8TrxrtAOUIcVZjb0KJCzBZQ8OAKkUzQoucerD47rlSht_JrRgMtmmigNCAoJhCKKjC0j0OTRxIduLNGRYlJur3zCcTm7FF5I72BJJRPvPnqFYY3XGwRHuVuzPD3DZLtgaz0hxC4mrdXI2QPI7ofEOF4TBViSIFnz_LKmZ4VsrCZjfZ4id5OXE0OERgtoxNMVRMHF-2M8NzpBSyZbGOpJ_cazEglKQ8lY4ArTI0dTBcb-eObi8dcL5PJ-ETAB23JNhUrFvHqzKkyqzyU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncC5Sgks013cpnYMyk7lGGenwSw-Yd6bCdqmyYMJKb0L2QIl8nWHbAa_n_OQ4NSMJmN7k3UsvUYjhtH6zNl7xdHi8-iNDmo6Ohdump8y-iwtOUJzQP7iDNyCVw4Cz_sPsf3ZvlfgNKMSdUpiHCz87XMtxPHJ9K-OC9i3knEkMP9gImO_P6SyiG0ISL7RKcCsqlpA2WvERMUfNP3Dg3UZXHlregSEOXm292JoZ6HoFkqttb63qKbzqU_sDTrz9JtUMGDcs2rSO9HiVMM3S0j8GAknNuTTyzsZaWNTW9NdYYAoC-WAlzyzGZ8noqEvjCX8ni033WBmrkIVktxiI2Fq0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/442937" target="_blank">📅 00:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442936">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcvSRQeYDCljmsKSlzDJqaIZdTE23fYAE1h2kvF9PT6Jig17eBasj9e9A_a9BwmxceZGi6ogkdr8lHE1i__u3Zx7ulpWR3Oq41p7b-BlfHq9-nq8e9eKiSTYw9OKI2Uy8uUA58qHqryPoxiIIuDIUqSh4-3jZQ2dsggX2vEv5EuNPtD8hMMeDloOh3hjA7j5sYt60vCRql4ZOzf8kOStdNd9LpI135h49Eoan7YI_kNoVMhHEOIkeJn1ev-TYwkdxmIflkWVLxKW_Vmoq9xVCNCIkV1qYUD8sE7TAV1YA_2O-6rJ4EucmEH3vUxs0Qf8KQBig0YH1wAWyCqFiYpPAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ صهیونیست‌ها به جنوب لبنان با بمب‌های ممنوعۀ فسفری
🔹
رسانه‌های لبنانی: ارتش رژیم صهیونیستی ارتفاعات علی‌الطاهر مشرف به شهر النبطیه را با گلوله‌های توپخانه و بمب‌های فسفری مورد حمله قرار داد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442936" target="_blank">📅 00:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442935">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca77291ac8.mp4?token=Lk8cjTEiDn8ayWxHpxDSjp6Pj3LsbWQuOlXJcfJtLxStbcczJCReWwmsLV1eY1oOYhvkTXbT3YVPFsH271b3AlZHSfg5HnVc1PQDYHEpy8ZubzHqcYivHRrMyPEfo8WCszZon_eEuqhNY59tfRy8gSIoeGyS37DLVWPhrgqZF21fD54WHGKo7edD1pxFDQ8NB9n07-dbuUgRHLukzVH73bZgQrF2vuMS7eL9eNF1DvloiIwru7InHpIQfIJ-_KtKnatLdqzt_f_vzTZoZbFkgHrCJi1m8T63ebDbhJFtO0-NAXG9-A8bhYyxkZHfw0bChH10rqqbC7te_2j-y3pVyrZlvdQkL_wVac-mzRb6wDtirbHA4-jqoz-EKcwFfPHKvUXAHAJtUPPhoYnZjCTEsa0qTWXwUH5g4z2ybPla44lCMXNmlsWIf1mNAPxIbWsiCR1UyeAixx5f2LZX3UU9feUc_DW0zI23LfIDOJOG-EzB4CmZRq5pZVb63z4CjDrNY64bSgH_sfgV22Cn_NH9kygl4Uuo0L58sYARAWPUa_KpdtGE6Yjuf4M4Qn-s1vLcwDcxAzYQZWJy10UiFkISho4DziiKM55DTU_1dP05D-ToEPe83rZV2nRE1CBJy2orVMwCZQtVzGgO6N5oYEpj1wwlh-72_EkIuZOl_qEelDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca77291ac8.mp4?token=Lk8cjTEiDn8ayWxHpxDSjp6Pj3LsbWQuOlXJcfJtLxStbcczJCReWwmsLV1eY1oOYhvkTXbT3YVPFsH271b3AlZHSfg5HnVc1PQDYHEpy8ZubzHqcYivHRrMyPEfo8WCszZon_eEuqhNY59tfRy8gSIoeGyS37DLVWPhrgqZF21fD54WHGKo7edD1pxFDQ8NB9n07-dbuUgRHLukzVH73bZgQrF2vuMS7eL9eNF1DvloiIwru7InHpIQfIJ-_KtKnatLdqzt_f_vzTZoZbFkgHrCJi1m8T63ebDbhJFtO0-NAXG9-A8bhYyxkZHfw0bChH10rqqbC7te_2j-y3pVyrZlvdQkL_wVac-mzRb6wDtirbHA4-jqoz-EKcwFfPHKvUXAHAJtUPPhoYnZjCTEsa0qTWXwUH5g4z2ybPla44lCMXNmlsWIf1mNAPxIbWsiCR1UyeAixx5f2LZX3UU9feUc_DW0zI23LfIDOJOG-EzB4CmZRq5pZVb63z4CjDrNY64bSgH_sfgV22Cn_NH9kygl4Uuo0L58sYARAWPUa_KpdtGE6Yjuf4M4Qn-s1vLcwDcxAzYQZWJy10UiFkISho4DziiKM55DTU_1dP05D-ToEPe83rZV2nRE1CBJy2orVMwCZQtVzGgO6N5oYEpj1wwlh-72_EkIuZOl_qEelDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰۹ شب اجتماع سرخسی‌ها در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/442935" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442934">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۵ فروند بالگرد تا پایان سال به هلال‌احمر می‌پیوندد
🔹
کولیوند، رئیس جمعیت هلال‌احمر: بالگردهای هلال‌احمر از خارج از کشور خریداری می‌شود، که برای ۵ فروند قرارداد بسته شده و قبل از سال ۱۴۰۶ تحویل داده خواهد شد.
🔹
بالگردها دید در شب بوده و دارای سیستم جدید ناوبری…</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/442934" target="_blank">📅 00:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
قالیباف: پرداخت هزینه خدمات عبور از تنگه هرمز در تفاهم‌نامه تثبیت شده است
📌
کشورهای ساحلی تنگه ها در قوانین بین المللی حقوق و وظایفی دارند از جمله این که دیگران باید هزینه خدمات شان را پرداخت کنند.
📌
دشمنان ایران را خدا از احمق ها آفریده و باعث شدند ظرفیت…</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/442933" target="_blank">📅 00:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442932">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قالیباف: همه این دستاوردها و منطق قدرتی که امروز از آن سخن می‌گوییم، مرهون مجاهدت‌ها و فداکاری‌های نیروهای مسلح جمهوری اسلامی ایران است
‌
🔸
به همه فرماندهان، رزمندگان و نیروهای مسلح خدا قوت می‌گویم و از تلاش‌ها و ایستادگی آنان صمیمانه قدردانی می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/442932" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442931">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae42f790b0.mp4?token=UZMx0bfD8A5lYaAD0oPkGv-u5UMDTD3-cDxr0EYeWITp1nZ9mfICJHgW89XPQ207OtvV7aGsnLTNLgITPO2zLWqziAZqAEHw7CU9tNEoO65nPgbnUyxkobpsT3IPVuOF0U-Xifv7u0PpjxInqwe9WRrsy6Qf6xuuCMj6x8GY5Xm3_dFnvgvwboKnqSo3R6h_mIfUr8lSow_ol2A3P23MrvbYRWQgmYg9tSwfwgfN3r0gpUsFHlZG8TP0WMcxEnipTJ8zH6icKylUz7Iva6ochxDEdOroURdpVLfLRAOyUHxY8VgtoS9SRh4GEaqovyMEYiAxnu7Ktc0-3McOoTAcIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae42f790b0.mp4?token=UZMx0bfD8A5lYaAD0oPkGv-u5UMDTD3-cDxr0EYeWITp1nZ9mfICJHgW89XPQ207OtvV7aGsnLTNLgITPO2zLWqziAZqAEHw7CU9tNEoO65nPgbnUyxkobpsT3IPVuOF0U-Xifv7u0PpjxInqwe9WRrsy6Qf6xuuCMj6x8GY5Xm3_dFnvgvwboKnqSo3R6h_mIfUr8lSow_ol2A3P23MrvbYRWQgmYg9tSwfwgfN3r0gpUsFHlZG8TP0WMcxEnipTJ8zH6icKylUz7Iva6ochxDEdOroURdpVLfLRAOyUHxY8VgtoS9SRh4GEaqovyMEYiAxnu7Ktc0-3McOoTAcIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در این مدت در میادین در میان مردم عزیز حضور داشتم و در کنار شما بودم، هرچند بسیاری از شما مرا نشناختید
📌
از رهبر معظم انقلاب تشکر می‌کنم که در این مسیر ما را هدایت و رهبری کردند؛ هر جا لازم بود تذکر دادند و هر کجا نیاز به حمایت بود، پشتیبانی کردند.
📌
از مردم عزیز ایران نیز به خاطر صمیمیت، گذشت، انسجام، همراهی و حتی انتقادهای به‌جا و گاه نابه‌جا تشکر می‌کنم. همه این‌ها نشان‌دهنده حساسیت و دغدغه‌مندی مردم نسبت به سرنوشت کشور است.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/442931" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442930">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4538914626.mp4?token=Re5EPrGOAFQybeFncfKcX27mSoXjR3rlnlondtO7ozgGxRZ-oli-n363hT5jloEc_U-dNgipcWqpo5iVuu6vRQD9UR8I1-DDg7dYSQ2YZRiXtPDYndwNXy4w_-lR7QtdxJK5ZsGSE17LTvprnp9bK2GYOGS8awXyeVeZP8FcohFrVzaSx1AfEh9fv_XmSdKjee6Pj45h1gQ3jKDMFqMqJR0t27btbG9V_l4kVOrnkXfCoB_W0titkWM_m9SxrMmRh7UE3Hce25ZeJSGTWJjVTnd82-Rir5Bj5HdjnakddHeg5DD5XljKWY_5gEwAbTUx5DBcLmacEDKEDMJw65ooXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4538914626.mp4?token=Re5EPrGOAFQybeFncfKcX27mSoXjR3rlnlondtO7ozgGxRZ-oli-n363hT5jloEc_U-dNgipcWqpo5iVuu6vRQD9UR8I1-DDg7dYSQ2YZRiXtPDYndwNXy4w_-lR7QtdxJK5ZsGSE17LTvprnp9bK2GYOGS8awXyeVeZP8FcohFrVzaSx1AfEh9fv_XmSdKjee6Pj45h1gQ3jKDMFqMqJR0t27btbG9V_l4kVOrnkXfCoB_W0titkWM_m9SxrMmRh7UE3Hce25ZeJSGTWJjVTnd82-Rir5Bj5HdjnakddHeg5DD5XljKWY_5gEwAbTUx5DBcLmacEDKEDMJw65ooXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: تفاهم‌نامه براساس اصل اقدام در برابر اقدام است
🔸
هرجا آمریکا به تعهدات خود عمل نکند، محال است جمهوری اسلامی ایران به تعهداتش عمل کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/442930" target="_blank">📅 00:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442929">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c28824f9.mp4?token=EM3CYPqJjQt1YnthvrqugrhKw201LGrhNaoGdQqghnKy2J0zruG97CPhxZoDyMEOBgAw6-MP3wBbn1e5TlbZrIiYGHD7iMRtDHJbWSNu5zwzmGg5MWsMqDTgvVnWqhDG-i7-s0UyNkut2KGXhAQCPJkXCDC6l3PWscQbu44TDMXRnGLrx_luiRSVIzflxwJb0oWQwo9fuvWw9xQp-_MldOXSKDmkjhPFS5BJ4KEyPwfggUrywAzOjEXkR_wh14UYIWyO_fPalKMqVvdkm15OPCfZdl6awxlrpif9YiU9YxmjR0wC5d_S6siWKrGCN4kZhnczfXhAhFBGk0z8VDdyKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c28824f9.mp4?token=EM3CYPqJjQt1YnthvrqugrhKw201LGrhNaoGdQqghnKy2J0zruG97CPhxZoDyMEOBgAw6-MP3wBbn1e5TlbZrIiYGHD7iMRtDHJbWSNu5zwzmGg5MWsMqDTgvVnWqhDG-i7-s0UyNkut2KGXhAQCPJkXCDC6l3PWscQbu44TDMXRnGLrx_luiRSVIzflxwJb0oWQwo9fuvWw9xQp-_MldOXSKDmkjhPFS5BJ4KEyPwfggUrywAzOjEXkR_wh14UYIWyO_fPalKMqVvdkm15OPCfZdl6awxlrpif9YiU9YxmjR0wC5d_S6siWKrGCN4kZhnczfXhAhFBGk0z8VDdyKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: به‌خاطر حساسیت‌های حقوقی ساعت‌ها در مورد برخی متون تفاهم‌نامه بحث شده است
📌
برخی دوستان نگران بودند که آیا بعد از ۳۰ روز محاصره رفع خواهد شد؟ اما به لطف خدا طی ۳ روز محاصره لغو شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/442929" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442928">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎥
قالیباف: در بند ۶ تفاهم‌نامه ۳۰۰ میلیارد دلار برای موضوع بازسازی و توسعه اقتصادی در ایران تعیین شده است
🔹
سازمان ملل حتی یک بیانیه که آمریکا را متجاوز اعلام کند، منتشر نکرد و لذا نمی پذیرند که متجاوز هستند. در دنیایی که قانون جنگل حاکم است ما باید با قدرت…</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/442928" target="_blank">📅 00:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442927">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc516a2f7d.mp4?token=hC50XDp2c-Y9HR4FhfqSKJROPU3UiM4BapSKY4V65feuKS1DmqDNQ_E3xTPX7GvYIWFCJkRds_Yc1AH3lHX-3_JFpHvf36VUsKswR1ofHxm4c4w06srRlDvjETdr_lsec_3vEbJ464OJLkl4xo6Z-xeoIlc-LEhA3ZyomziBu9V0iv7ChEH-m_GNb-nixDLHLOspzDCmKKRA48_GHJsJvPfQIO599f9wCp8WugsYi7Pzre2AWxiJ18eeiNvHdgvq5AvYRVGPDpryAdMRdchjFI_7RRgziexQuACQrbb4BK5Yo2GUFFfwaa58ovOPVjYMozUrRFCoVIZ3lhWEhKkE9q-uy5qvM1DlvWG8xH2Z2KmUHS6LVbP8VyJLtzi04ZwIeATMDB_lbNbVyvL5BCjpnp7HoJF-m7tsSbhL34BpuYSOhOuXy3cSYb3DlBQ0P8fV4N_TlFxpMirygDRcBFtWUTLsJljIFYudvVBThdtJx7y0nrXyS0MUgbG3xwl65ib6yHe_wt7hwsXBBGROLmcH2Fj5ksQu2r4okwl9mYvaZ0deAIlbqgXYU_EFEsJ0Nz7OHsrDnzF09FS2_1dEUIoR20-Hnc_GtR2PAaAuJnD08z--fe3oOgem9O6OO4PvXG_ldVN13akHwf7P8Y2F6U9u2Gph6Ff0W5-O-W2nKMZFXp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc516a2f7d.mp4?token=hC50XDp2c-Y9HR4FhfqSKJROPU3UiM4BapSKY4V65feuKS1DmqDNQ_E3xTPX7GvYIWFCJkRds_Yc1AH3lHX-3_JFpHvf36VUsKswR1ofHxm4c4w06srRlDvjETdr_lsec_3vEbJ464OJLkl4xo6Z-xeoIlc-LEhA3ZyomziBu9V0iv7ChEH-m_GNb-nixDLHLOspzDCmKKRA48_GHJsJvPfQIO599f9wCp8WugsYi7Pzre2AWxiJ18eeiNvHdgvq5AvYRVGPDpryAdMRdchjFI_7RRgziexQuACQrbb4BK5Yo2GUFFfwaa58ovOPVjYMozUrRFCoVIZ3lhWEhKkE9q-uy5qvM1DlvWG8xH2Z2KmUHS6LVbP8VyJLtzi04ZwIeATMDB_lbNbVyvL5BCjpnp7HoJF-m7tsSbhL34BpuYSOhOuXy3cSYb3DlBQ0P8fV4N_TlFxpMirygDRcBFtWUTLsJljIFYudvVBThdtJx7y0nrXyS0MUgbG3xwl65ib6yHe_wt7hwsXBBGROLmcH2Fj5ksQu2r4okwl9mYvaZ0deAIlbqgXYU_EFEsJ0Nz7OHsrDnzF09FS2_1dEUIoR20-Hnc_GtR2PAaAuJnD08z--fe3oOgem9O6OO4PvXG_ldVN13akHwf7P8Y2F6U9u2Gph6Ff0W5-O-W2nKMZFXp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در بند ۶ تفاهم‌نامه ۳۰۰ میلیارد دلار برای موضوع بازسازی و توسعه اقتصادی در ایران تعیین شده است
🔹
سازمان ملل حتی یک بیانیه که آمریکا را متجاوز اعلام کند، منتشر نکرد و لذا نمی پذیرند که متجاوز هستند. در دنیایی که قانون جنگل حاکم است ما باید با قدرت خود، مسائل را دنبال کنیم.
📌
البته در تفاهم نامه بند ۶ برای این موضوع آمده که در آن از لفظ بازسازی و توسعه اقتصادی استفاده شده است.
📌
در این بند ۳۰۰ میلیارد دلار تعیین شده تا در ایران سرمایه گذاری شود که بخشی از آن صرف بازسازی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/442927" target="_blank">📅 00:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442926">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f74e37d41.mp4?token=S-MPmVdycc2qR3xisEp1Nz-4ZlYB4bwZUjUodnPb0qUYMtwmbBqtMKke7LKDs1XtwxmzpNNKMFLdXpsmmtS47idx2yVamK5oaaGpu7YrgKuH2aI3R5fX8MVNIx43g1P3CSf8O1p6lpmnzWQhHsaPySu1Qus5i_CeYZl8cd_T4aIrXJozfDqoijjTI9vGA6nsIdGwWg7MIzCSKgyZXkpJmzuMhDHtxrvK2-XDS70a9PA9RvIiXAQPmJjK3warZOmPvORNO4d8KBlhK_Xlj85p4B-UboGB_k8wvSs8hSvYGAIZqTeCjHcFdfu0nERyGvjtJu8USJ_LCg5Fd-YS0oqX3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f74e37d41.mp4?token=S-MPmVdycc2qR3xisEp1Nz-4ZlYB4bwZUjUodnPb0qUYMtwmbBqtMKke7LKDs1XtwxmzpNNKMFLdXpsmmtS47idx2yVamK5oaaGpu7YrgKuH2aI3R5fX8MVNIx43g1P3CSf8O1p6lpmnzWQhHsaPySu1Qus5i_CeYZl8cd_T4aIrXJozfDqoijjTI9vGA6nsIdGwWg7MIzCSKgyZXkpJmzuMhDHtxrvK2-XDS70a9PA9RvIiXAQPmJjK3warZOmPvORNO4d8KBlhK_Xlj85p4B-UboGB_k8wvSs8hSvYGAIZqTeCjHcFdfu0nERyGvjtJu8USJ_LCg5Fd-YS0oqX3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: پرداخت هزینه خدمات عبور از تنگه هرمز در تفاهم‌نامه تثبیت شده است
📌
کشورهای ساحلی تنگه ها در قوانین بین المللی حقوق و وظایفی دارند از جمله این که دیگران باید هزینه خدمات شان را پرداخت کنند.
📌
دشمنان ایران را خدا از احمق ها آفریده و باعث شدند ظرفیت بالقوه ایران در تنگه هرمز بالفعل شود.
📌
ایران در تنگه هرمز حق حاکمیتی دارد و طبیعتا در قبال خدمات، هزینه دریافت خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/442926" target="_blank">📅 00:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442925">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7111ac9d43.mp4?token=ILZiU7PuecHtWJXlrLY-J8qkzI1lFszPbN-wvs350hV04ACumWlOG9In3Jwmjr3VLuRkx1YqLkpdoPXauYvhWAPpshv6JODjU3A1J74ct0QddWboPFpMGPilZnM3Em4hVBL3J6YKrcWYRrWpKE_rxyySt0OP-snh9K-6UoZ4yjbroCsA9U_hbeXK1xfA2oyiD21-COzZ-vOwPQX61JKBD74VNiPaansSRpi74jnDOyLFh6OPnT-eC7nXC5j-ZRURU1uioMEV3AgG9KqKkcVXc87h2rnyL7Y-grp5EjWMEkfU1yCCngSVzt6jLxlzSoD8X1ATFzoADXgOK2QjbGWczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7111ac9d43.mp4?token=ILZiU7PuecHtWJXlrLY-J8qkzI1lFszPbN-wvs350hV04ACumWlOG9In3Jwmjr3VLuRkx1YqLkpdoPXauYvhWAPpshv6JODjU3A1J74ct0QddWboPFpMGPilZnM3Em4hVBL3J6YKrcWYRrWpKE_rxyySt0OP-snh9K-6UoZ4yjbroCsA9U_hbeXK1xfA2oyiD21-COzZ-vOwPQX61JKBD74VNiPaansSRpi74jnDOyLFh6OPnT-eC7nXC5j-ZRURU1uioMEV3AgG9KqKkcVXc87h2rnyL7Y-grp5EjWMEkfU1yCCngSVzt6jLxlzSoD8X1ATFzoADXgOK2QjbGWczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: وظیفه ما اجرای تدابیر رهبر انقلاب در مذاکرات است
📌
ما تدابیری از رهبر معظم انقلاب داریم و وظیفه داریم در این مذاکرات به آن تدابیر جامه عمل بپوشانیم.
📌
موضوعاتی که اکنون مطرح است، پایان جنگ است که اعلام شده و همچنین برداشته شدن محاصره که اتفاق افتاده است.
📌
در وسط جنگ، توییتی منتشر کردم و گفتم تنگه هرمز هرگز به شرایط قبل بازنخواهد گشت و امروز نیز همین‌گونه است.
📌
البته این به آن معنا نیست که ما در تنگه هرمز بخواهیم برخلاف قوانین بین‌المللی و مقررات دریانوردی عمل کنیم؛ هرگز. ما در چارچوب قوانین بین‌المللی عمل می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/442925" target="_blank">📅 00:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442924">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌‌ قالیباف اگر آمریکا به تعهداتش عمل نکند محال است ایران به تعهدش عمل کند
🔹
ما مرحله به مرحله و اقدام در برابر اقدام پیش می‌رویم. @Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/442924" target="_blank">📅 00:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442922">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌‌
🔴
قالیباف: ما ۳۰۰ میلیارد دلار سرمایه‌گذاری ازسوی شرکت‌های آمریکایی را در تفاهم‌نامه گذاشتیم که خود خسارات ما را جبران می‌کند  @Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/442922" target="_blank">📅 00:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442921">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
قالیباف: هرجا دشمن به تعهداتی که داده عمل نکند شمشیر ما موجود است و با منطق قدرت به او خواهیم فهماند
🔹
من دیپلمات نیستم اما خوب بلد هستم به آمریکا تفهیم کنم که باید چه کار کند. @Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/442921" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442920">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
قالیباف: خونخواهی رهبر شهید آزادی قدس است؛ ۱۰۰ نتانیاهو بند کفش امام شهید ما هم نمی‌شود  @Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/442920" target="_blank">📅 23:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442919">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48f0dcc90.mp4?token=KYQJb9Q7gUVYANtWMFvDYUkV3B8GMFbEge3T2d3x2_1DUaMlSa7PrlFKpPpthdu61-Co8tKZHiuZ6RPTJ8a_7s_iAB_5HkJWOd6RpfcyLcUye_jxcU0JNksRVMTg4GE8_9AAVnkFsZNQRQW0ndBOT7N2W3yVC-1FKftrLI5gou6Vjyid_3w5l-yo-k6G6_4DfXIoC_OYEfXpVrmhf9NSttDyWr6DNgV5rwPGLaAprrSRfOIllTczyFfOkkhOjpwkG23CGVF9Hq7t_sPdjGWsSRPP1rBdLzO09w0avrIzg4Y2qkrLJ9z0ivKU5VNBwBSKAB5LxMFtpA0VxNeMaNV_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48f0dcc90.mp4?token=KYQJb9Q7gUVYANtWMFvDYUkV3B8GMFbEge3T2d3x2_1DUaMlSa7PrlFKpPpthdu61-Co8tKZHiuZ6RPTJ8a_7s_iAB_5HkJWOd6RpfcyLcUye_jxcU0JNksRVMTg4GE8_9AAVnkFsZNQRQW0ndBOT7N2W3yVC-1FKftrLI5gou6Vjyid_3w5l-yo-k6G6_4DfXIoC_OYEfXpVrmhf9NSttDyWr6DNgV5rwPGLaAprrSRfOIllTczyFfOkkhOjpwkG23CGVF9Hq7t_sPdjGWsSRPP1rBdLzO09w0avrIzg4Y2qkrLJ9z0ivKU5VNBwBSKAB5LxMFtpA0VxNeMaNV_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
قالیباف: مدیریت تنگه هرمز را براساس قوانین بین‌المللی پیش می‌بریم
🔹
براساس این قوانین ما حق داریم هزینۀ خدمات در تنگه هرمز را دریافت کنیم. @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/442919" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442918">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
قالیباف: بازهم تاکید می‌کنم که تنگه هرمز هرگز به شرایط قبل بازنمی‌گردد.  @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/442918" target="_blank">📅 23:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442917">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
قالیباف: ما دستمان روی ماشه است و اگر دشمن زبان منطق را نفهمد دوباره با زبان قدرت وارد می‌شویم @Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/442917" target="_blank">📅 23:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442916">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8762557a67.mp4?token=YWL93IYTy6GOVILwfSQhGzetRG5P0MKXEbRGTvmTiXrBOR8GhCwmuWgsKOhJP10YYNevhLx90YBr5Wor_b_9nwbokKG0pLUakKB_urolUHu9vv6BNkXRTbgtOklADcK2PJk_VhFMN7tLtYHeVh4yNBhBmjqlF3Imzm9DkqwFtm-CjGDdwiD2e-TNKisxm4Jzlwxq4_52DTM367oB6o97ixZFxVLOK8snE_0f3Ea-2x1Lv_DTKq3EDBEVXt3Cqeqx0HtKJshJx3ECah_g_2gL4y7JHIZF0hQrERBKq3r4SeskpNjmTZZfyRVqGKPo-bKoPQdYMvJU2W6kW8NaLomvqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8762557a67.mp4?token=YWL93IYTy6GOVILwfSQhGzetRG5P0MKXEbRGTvmTiXrBOR8GhCwmuWgsKOhJP10YYNevhLx90YBr5Wor_b_9nwbokKG0pLUakKB_urolUHu9vv6BNkXRTbgtOklADcK2PJk_VhFMN7tLtYHeVh4yNBhBmjqlF3Imzm9DkqwFtm-CjGDdwiD2e-TNKisxm4Jzlwxq4_52DTM367oB6o97ixZFxVLOK8snE_0f3Ea-2x1Lv_DTKq3EDBEVXt3Cqeqx0HtKJshJx3ECah_g_2gL4y7JHIZF0hQrERBKq3r4SeskpNjmTZZfyRVqGKPo-bKoPQdYMvJU2W6kW8NaLomvqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: وقتی منطق دشمن قدرت است باید او را ادب کرد ولی وقتی پای میز مذاکره می‌آید با بی اعتمادی با او صحبت کرد
📌
گاهی قدرت ما منطق است و گاهی منطقِ دشمن، قدرت است؛ در چنین شرایطی باید او را ادب کرد. اما وقتی طرف مقابل پای میز می‌نشیند و می‌خواهد گفت‌وگو کند، باید با بی‌اعتمادی، اما با حسن نیت با او صحبت کرد.
📌
دیدید که ترامپ در حالی که طبق تفاهم‌نامه قرار بود رفع محاصره طی ۳۰ روز انجام شود، آن را یک‌شبه اجرایی کرد. همچنین آتش‌بس از ضاحیه به سراسر لبنان گسترش پیدا کرد.
📌
البته ما می‌دانیم که با دشمنی بدعهد و غیرقابل اعتماد مذاکره می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/442916" target="_blank">📅 23:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442915">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a47ff9e3.mp4?token=BT2H_vxUpFawQdaGfweG4P65idC1jwyiJKYNQ_zA9mXbSFJbBw_NZs_N3MFiHDaEp5qX0bxSc_RFkHlmRLhCH5TfVtLXJThO-45BUVBvfnea0xZdeKHvnmBP9DoGFgDKUveYXWszChHPAc9dWtdiy-RciKuZZBB7ZGjVc6zd36fa9LTluab8IOPh0ttDxr5M8wT5I5I_vAoh6J0jRg-I2dH2d1s3cWWwP62Xg8zoUa-IYNMBtuDsMPLAw3UYleUPG1MN3Wwy0Mq3yfTQ1ErzgVLEdOfBgr-zsIFwxuOqHSlMGLK2z_XpF2JiwUWYA00Mf73PGBc3gJwTlBOLhC_SM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a47ff9e3.mp4?token=BT2H_vxUpFawQdaGfweG4P65idC1jwyiJKYNQ_zA9mXbSFJbBw_NZs_N3MFiHDaEp5qX0bxSc_RFkHlmRLhCH5TfVtLXJThO-45BUVBvfnea0xZdeKHvnmBP9DoGFgDKUveYXWszChHPAc9dWtdiy-RciKuZZBB7ZGjVc6zd36fa9LTluab8IOPh0ttDxr5M8wT5I5I_vAoh6J0jRg-I2dH2d1s3cWWwP62Xg8zoUa-IYNMBtuDsMPLAw3UYleUPG1MN3Wwy0Mq3yfTQ1ErzgVLEdOfBgr-zsIFwxuOqHSlMGLK2z_XpF2JiwUWYA00Mf73PGBc3gJwTlBOLhC_SM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توضیحات جدید قالیباف در مورد فرآیند مذاکرات اسلام آباد
📌
طی ۲۴ ساعت ۳ دور مذاکرات با متن و ۳ دور مذاکرات سه جانبه با حضور میانجی برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/442915" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442914">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
قالیباف: اکنون براساس تفاهم‌نامه، باید ابتدا بندهای ۴، ۵، ۱۰ و ۱۱ و اکنون تأکید می‌کنم بند ۱ نیز در اولویت اجرا قرار گیرد تا پس از آن وارد سایر بندهای تفاهم‌نامه شویم. @Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/442914" target="_blank">📅 23:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442912">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌ قالیباف: قبل از مذاکرات اسلام آباد اعلام کردیم موضوع لبنان و آزادسازی پول های بلوکه شده باید محور مذاکرات باشد
📌
ما چیزی به عنوان پیش‌شرط نداشتیم، هرچند ممکن است خواسته‌هایی داشته باشیم. البته به میانجی گفته بودیم که بحث آتش‌بس لبنان و آزادسازی پول‌های بلوکه‌شده،…</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/442912" target="_blank">📅 23:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442911">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌ قالیباف: من برای پذیرش حضور در تیم مذاکره‌کننده کراهت داشتم
📌
من نه‌تنها داوطلب حضور در تیم مذاکره کننده نبودم بلکه کراهت هم داشتم و قبل از پذیرش مسئولیت مذاکرات من تمام تلاشم را کردم که این مسئولیت به من سپرده نشود.
📌
یکی از دلایل من برای عدم پذیرش این…</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/442911" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442910">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
قالیباف: در طول جنگ نمایندگان چند کشور اروپایی به ایران آمدند تا از ما خواهش کنند
🔹
همان کشورهای اروپایی که سپاه را در لیست تروریستی گذاشته بودند از مسیرهای زمینی به سختی به ایران آمدند تا با ما صحبت کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/442910" target="_blank">📅 23:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442909">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">روایت شب آخر مذاکرات
📌
قالیباف: هر جنگی که پیروزی داشته باشد، اگر این نهایتاً منجر به یک سند حقوقی و سیاسی نشود و آن پیروزی‌ها ثبت نشود، آن پیروزی‌ها هیچ منفعتی پیدا نخواهد کرد؛ نه در تاریخ و نه در مزایای آن.
📌
الان ما در جنگ ۴۰ روزه پیروز شدیم، خب دستاوردش…</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/442909" target="_blank">📅 23:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442908">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0785c208b9.mp4?token=lYygv87iPZq6hj9DXWZUKOOeLkXEZvl3J-vzb2oznZL-pblf0UJKuxZTWsUQWyxIjYnbtU3BHvR-eFNFDVX9Q8QFGN6VlqHPnxPtt4Tp_uCK-YvyXTTBDaw8kB-kfPYM7kwo8ATAYA-F5xBzLKvKKhM_L8Bf37iCBpe68XU50yrwqSuL1ZNqZItKHKPZTYdz4YKcjoRlRVyVAXTQtOTC70vSAcwa1gVmPzwd-QnQCdh_3grc-abJk4eOXgjed3cc6BqWRD0FdeZjafAlvH2p24uiHsQTvqVJ95dr-nCVjFwTDWSzLpLUCm7LBcs7JYTamKDy8r-ibs568MR-f1ezPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0785c208b9.mp4?token=lYygv87iPZq6hj9DXWZUKOOeLkXEZvl3J-vzb2oznZL-pblf0UJKuxZTWsUQWyxIjYnbtU3BHvR-eFNFDVX9Q8QFGN6VlqHPnxPtt4Tp_uCK-YvyXTTBDaw8kB-kfPYM7kwo8ATAYA-F5xBzLKvKKhM_L8Bf37iCBpe68XU50yrwqSuL1ZNqZItKHKPZTYdz4YKcjoRlRVyVAXTQtOTC70vSAcwa1gVmPzwd-QnQCdh_3grc-abJk4eOXgjed3cc6BqWRD0FdeZjafAlvH2p24uiHsQTvqVJ95dr-nCVjFwTDWSzLpLUCm7LBcs7JYTamKDy8r-ibs568MR-f1ezPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: مهم ترین ضمانت برای ما قدرت ایران و انسجام مردم است نه قطعنامه شورای امنیت
📌
بدبینی و بی اعتمادی من به آمریکا از همه بیشتر است. حتی اگر توافق نهایی باشد و آن به تایید قطعنامه شورای امنیت برسد بازهم اصلا قابل اعتماد نیست، تضمین ما قدرت ایران است.
📌
مهم ترین ضمانت اتکا به خداوند، فرهنگ عاشورایی، غیرت ایرانیان و انسجام مردم است.
📌
قدرت ایران باعث شده سه کشور اروپایی که در برجام بدعهدی کردند و سپاه را در فهرست تروریستی قرار دادند و دنبال براندازی نظام جمهوری اسلامی بودند به دنبال مذاکره با ایران برای برداشتن تحریم ها هستند.
📌
سیستم های امنیتی همان کشورهای که سپاه را در فهرست تروریستی گذاشتند،  با التماس خواستار گفت و گو با ما بودند و با ماشین به ایران آمدند تا گفت و گو کنند، ما هم پاسخ دادیم، شما که ما را تروریست نامیدید، اکنون با تروریست ها چه کاری دارید؟
📌
ما حتما باید با عقلانیت حرکت کنیم، شعار قدرت نیست، گرهی که با دست باز می شود را لازم نیست با دندان باز کنیم. اگر دوبار شعار بدهیم ولی قدرت نداشته باشیم یعنی بی اعتباری و کمک به دشمن.
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/442908" target="_blank">📅 23:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442907">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41398d99c5.mp4?token=RPzOQGpnKYqQei6tO7mpxXvZJi6D_EgOflsGEdRw_nYTtEF0zIMOzqaj1yGek2_aBCNZo8mTIR0dmp7xyK2inW0MLGSH3d41KBvoMlNFFUVErV4SSoeOrgTt31soRoxrEhaF-lk6J-_CMyEgrmtrxMylverbv7oBIGm5WcUjUw7_yJNfDoCfACCNNXIxX5cIQ9USFrXQ-Fkj0_YznnJP3HyxVVCinZg58KzFfs754v3NG00oZuDx1hTV0cIMdD9o6L-IlCaGtRYEY8clDPw3m45VJwu8N0YZjLKagrkJVlyCkWD-qRtfgpYYYec9_Q22hmOipx7bg5bRRqW3AG6_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41398d99c5.mp4?token=RPzOQGpnKYqQei6tO7mpxXvZJi6D_EgOflsGEdRw_nYTtEF0zIMOzqaj1yGek2_aBCNZo8mTIR0dmp7xyK2inW0MLGSH3d41KBvoMlNFFUVErV4SSoeOrgTt31soRoxrEhaF-lk6J-_CMyEgrmtrxMylverbv7oBIGm5WcUjUw7_yJNfDoCfACCNNXIxX5cIQ9USFrXQ-Fkj0_YznnJP3HyxVVCinZg58KzFfs754v3NG00oZuDx1hTV0cIMdD9o6L-IlCaGtRYEY8clDPw3m45VJwu8N0YZjLKagrkJVlyCkWD-qRtfgpYYYec9_Q22hmOipx7bg5bRRqW3AG6_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ از موضع خود درباره «نابودی برنامه هسته‌ای ایران» فاصله گرفت
🔹
دونالد ترامپ روز چهارشنبه در حاشیهٔ نشست گروه هفت در فرانسه گفت که ایران می‌تواند برنامهٔ هسته‌ای خود را داشته باشد.
🔹
او اظهار داشت: «این موضوع تا حدی دشوار است که وقتی می‌گویید کشوری خواهان انرژی هسته‌ای است، در حالی که سایر کشورهای همسایه آن را دارند، شما به آن کشور اجازه ندهید که برای مقاصدی مثل تولید برق و امثال از آن استفاده کند. این همیشه کمی سخت است. باید کمی عقل سلیم به کار ببرید.»
🔸
پایگاه یاهونیوز نوشته این اظهارات به نظر می‌رسد که چرخشی آشکار از مواضع پیشین ترامپ در طول جنگ باشد. او که ماه‌ها بر این نکته پافشاری می‌کرد که هدف از جنگ، نابودی هرگونه توان هسته‌ای ایران و حذف کامل «غنی‌سازی» است.
🔸
این رسانه نوشته است: «اکنون این پرسش مطرح می‌شود که جمهوری‌خواهان کنگره دربارهٔ این امتیازدهی تازهٔ ترامپ چه خواهند اندیشید. اگر توافق نهایی صلح بین ایران و آمریکا هیچ‌گونه محدودیتی بر برنامهٔ هسته‌ای ایران نداشته باشد، در عمل از توافق برجام (۲۰۱۵) با ایران نیز بدتر خواهد بود.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/442907" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442906">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
🔴
قالیباف: مهم‌ترین ضمانت برای تفاهم فقط قدرت ماست وگرنه دشمن قابل‌اعتماد نیست
🔹
ترامپ قطعنامه‌ رسمی سازمان ملل را جلوی چشمان همه پاره کرده پس به هیچ وجه قابل‌اعتماد نیست. @Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/442906" target="_blank">📅 23:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442905">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
🔴
قالیباف: هدف ما تحقق هدف است؛ گاهی این هدف با مذاکره اتفاق می‌افتاد و گاهی با حملهٔ نظامی‌. @Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/442905" target="_blank">📅 23:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442904">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌
🔴
قالیباف: رئیس مجلس لبنان به من می‌گفت ایران مایهٔ افتخار جهان اسلام شده است. @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/442904" target="_blank">📅 23:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442903">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
قالیباف: قرار بود آمریکا محاصره را ظرف ۳۰ روز بردارد اما ترامپ گفت همین امشب محاصره را برمی‌داریم
🔹
اگر مذاکره نبود این موضوع اتفاق نمی‌افتاد و اگر موشک نبود حرف‌های من پای میز مذاکره بلوف و خالی‌بندی تلقی می‌شد. @Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/442903" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442902">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌
🔴
قالیباف: قرار بود آمریکا محاصره را ظرف ۳۰ روز بردارد اما ترامپ گفت همین امشب محاصره را برمی‌داریم
🔹
اگر مذاکره نبود این موضوع اتفاق نمی‌افتاد و اگر موشک نبود حرف‌های من پای میز مذاکره بلوف و خالی‌بندی تلقی می‌شد. @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/442902" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442901">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌ چرا ایران در روز آخر مذاکره حمله به اراضی اشغالی را متوقف کرد؟
🔹
قالیباف: ما هر آنچه که می‌خواستیم با حمله بگیریم را چندین برابرش را با مذاکره گرفتیم. ساعت ۲ صبح ترامپ آتش‌بس را در کل لبنان داد و با آن ادبیات با نتانیاهو صحبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/442901" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442900">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
🔴
قالیباف: فرق مذاکرات الان با دوره‌های قبل در این است که امروز علمِ پیروزیِ میدان، پشتوانه مذاکرات است. @Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/442900" target="_blank">📅 23:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442898">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌
🔴
قالیباف: وقتی خواستیم در جواب حمله به ضاحیه به اراضی اشغالی موشک بزنیم طرف مقابل گفت که نزنید، ما گفتیم حتما می‌زنیم و اگر پاسخ بدهید منطقه را می‌زنیم؛ این فرهنگ غالب بر مذاکرهٔ ما بود. @Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/442898" target="_blank">📅 23:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442897">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌
🔴
قالیباف: وقتی دشمن به ضاحیه حمله کرد من بلافاصله از جلسهٔ بررسی مذاکره بیرون آمدم و توییت زدم که ما پاسخ می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/442897" target="_blank">📅 23:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442895">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌
🔴
قالیباف: اگر مردم ما در خیابان نبودند ما نمی‌توانستیم با این قدرت در مقابل دشمن حرف بزنیم. @Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/442895" target="_blank">📅 23:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442894">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌
🔴
قالیباف: وقتی حرف از مذاکره می‌زنیم شمشیرمان هم آماده است
🔹
وقتی به ضاحیه حمله شد و بلافاصله عملیات نصر را انجام دادیم و اینجا نیروی نظامی این کار را انجام داد و دشمن متوجه شد وقتی حرف از مذاکره می‌زنیم شمشیرمان هم آماده است. @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/442894" target="_blank">📅 23:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442893">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌
🔴
قالیباف: من یک رزمنده‌ام و با فرهنگ رزمندگی کار دیپلماسی را دنبال می‌کنم.  @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/442893" target="_blank">📅 23:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442892">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
قالیباف: در مذاکره وقتی به دشمن اولتیماتوم دادیم، ترامپ توییت زد و به صهیونیست‌ها گفت باید آتش را قطع کنید؛ ما با مذاکره دشمن را وادار کردیم که این اتفاق بیفتد
🔹
بدون شک این به‌خاطر قدرت نظامی ما بود‌. @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/442892" target="_blank">📅 23:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442891">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
قالیباف: آتش‌بس را دشمن درخواست کرد و دنبال کرد
🔹
بعد از آتش‌بس دیدید که دشمن اقداماتی انجام داد و ما فورا پاسخ دادیم. ۲ ناوچهٔ دشمن که خواستند عبور کنند مورد اصابت قرار گرفتند‌. @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/442891" target="_blank">📅 23:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442889">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌ قالیباف: در مذاکره‌ای که خود یک شیوه مبارزه باشد وادادگی وجود ندارد
🔹
همچنین در این شیوه «شعارزدگی» هم وجود ندارد زیرا شعارهای توخالی دشمن را جسورتر می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/442889" target="_blank">📅 23:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442888">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌ قالیباف: مذاکرۀ فعلی ما از موضع قدرت است
🔹
من در زمان برجام هم گفته بودم فقط با مذاکره‌ای موافقم که خودش نوعی مبارزه باشد. @Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/442888" target="_blank">📅 23:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442887">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
قالیباف: امروز در هر ۴ جبهه میدان مبارزه، میدان دیپلماسی، میدان خیابان و میدان خدمت هرکس دقیقا می‌داند چه کاری باید انجام دهد. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442887" target="_blank">📅 23:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442886">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
قالیباف: اجازه ندادیم آمریکا و اسرائیل به ۹ هدفی که خودشان از آغاز جنگ مطرح کردند برسند.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442886" target="_blank">📅 23:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442885">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
قالیباف: قدرت اول نظامی، سیاسی و اقتصادی دنیا در کنار رژیم صهیونیستی که یک قدرت هسته‌ای با آخرین تکنولوژی‌ها است در مقابل ما قرار گرفتند.
🔹
صحنۀ درگیری این جنگ تاثیرات جهانی داشت و یک موضوع بین‌المللی بود؛ این جنگ رویارویی حق و باطل بود. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442885" target="_blank">📅 22:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442884">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
قالیباف: قدرت اول نظامی، سیاسی و اقتصادی دنیا در کنار رژیم صهیونیستی که یک قدرت هسته‌ای با آخرین تکنولوژی‌ها است در مقابل ما قرار گرفتند.
🔹
صحنۀ درگیری این جنگ تاثیرات جهانی داشت و یک موضوع بین‌المللی بود؛ این جنگ رویارویی حق و باطل بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442884" target="_blank">📅 22:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442874">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔸
۱۰. ایالات متحده آمریکا متعهد می‌شود بلافاصله با امضای این یادداشت تفاهم و تا زمان خاتمه تحریم‌ها، اسقاطیه‌های وزارت خزانه‌داری را برای صادرات نفت خام ایران، محصولات پتروشیمی و مشتقات آنها، و تمامی خدمات مرتبط شامل تراکنش‌های بانکی، بیمه‌ها، حمل و نقل و غیره صادر کند.
🔸
۱۱. ایالات متحده آمریکا متعهد می‌شود تا وجوه و دارایی‌های محدود یا مسدود شده جمهوری اسلامی ایران را با اجرای این یادداشت تفاهم به طور کامل برای استفاده در دسترس قرار دهد. ایالات متحده آمریکا و جمهوری اسلامی ایران در مورد روال مربوط به آزادسازی این وجوه در طول مذاکرات، به صورت دوجانبه توافق می‌کنند. این وجوه، چه در حساب اصلی نگهداری شوند و چه منتقل شوند، برای پرداخت به هر ذینفع نهایی که توسط بانک مرکزی جمهوری اسلامی ایران تعیین می‌شود، باید به طور کامل قابل استفاده شوند. ایالات متحده آمریکا متعهد می‌شود که تمامی تاییدیه ها و مجوزهای لازم را در این رابطه صادر کند.
🔸
۱۲. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند تا یک سازوکار اجرایی برای نظارت بر اجرای موفق این یادداشت تفاهم و پایبندی آتی به توافق نهایی تشکیل شود.
🔸
۱۳. پس از امضای این یادداشت تفاهم و منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این یادداشت تفاهم و تداوم اجرای این اقدامات، جمهوری اسلامی ایران و ایالات متحده آمریکا مذاکرات درخصوص توافق نهایی را منحصرا در مورد بقیه بندها آغاز خواهند کرد.
🔸
۱۴. توافق نهایی با یک قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تایید خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/442874" target="_blank">📅 22:41 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
