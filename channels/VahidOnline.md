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
<img src="https://cdn1.telesco.pe/file/X4ZPdHU_dPERTHqyWb_lfhY_r-SMnw8OeIMoruqWpjlchOyTiZrnT1D5asZ7Nv4tzA37IqYSq24KqDFv6TiLyivtwOOfp9sTTDNbwbGI4YSVNsoZpHvE2EJjWkHA3_DEwMka7MYH7lb09CYrUzgYh4JykxrcPutuT7gMwmqDHB7loUpeak0L7AOS69G-S9Y-G2vJ48bPBH4GjkNGJuDgbqQBZC6qmXg4npow1wZJblNlCkJeOUEsPuTZX7MZLgpJj2ka3IAie_a58t8ljhZCzDnTAN9gCf0BhHk1jJ11ThHNBZZks8k-94K7Yk1_jAhceIaAUmfHm43drqQwynolsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 08:17:51</div>
<hr>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M4gG8_eLZpaX_AgRV8aLYqaA99UaiEnQP5vIaAGIdY6uXp-nhDqBgrRtTTPaY-W6tlcGDpVLs5itiutQyvtEUJ5NqfoY4UcaE_89gZr4n0M1NCZfFa60ivmxHYgfg9yltgWQbSmXgV1W4GL2n9kme4NWj2hLKUmCUzS6in2tPDmnXBjn6PLwz3LXHSss840fwt4GiI3gpFg1naolt_xHoUuaaW7nzXooP8XrKi5pjl8AKEYRTY-t-XgikH_NTkmVlu45_1TljKAv7YLR813wDBZeH2WZA14ANCPat7294bYZAHIG7iBgVqfPOfuJs03KWJqqB6-I1gH0jg4P-M92gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
ترجمه ماشین:
⚠️
هشدار: خطر قریب‌الوقوع
تهدید امنیتی
از همه خواسته می‌شود در مکان‌های امن باقی بمانند و برای حفظ ایمنی عمومی، از پنجره‌ها و فضاهای روباز و در معرض خطر دوری کنند.
دفاع مدنی – وزارت کشور
آپدیت:
کویت: ایران حمله کرده
متن پست ارتش کویت، ترجمه ماشین:
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران است.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همه خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/VahidOnline/78200" target="_blank">📅 05:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آکسیوس:
ویتکاف در بحبوحه تشدید فشارها علیه ایران با مقام قدرتمند اماراتی دیدار کرد
ترجمه ماشین:
استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته با مشاور امنیت ملی امارات متحده عربی دیدار کرد تا درباره گام‌های بعدی در قبال ایران گفت‌وگو کند؛ این را دو منبع مطلع از این دیدار گفته‌اند.
چرا مهم است:
این گفت‌وگوها که کاخ سفید آن‌ها را اعلام نکرده بود و تاکنون نیز گزارشی درباره‌شان منتشر نشده بود، در شرایطی انجام شد که دولت ترامپ در تلاش است تنگه هرمز را بازگشایی کند و هم‌زمان ایران را از نظر اقتصادی تحت فشار شدید قرار دهد. ویتکاف در جزیره ساردینیا در دریای مدیترانه با شیخ طحنون بن زاید آل نهیان (TBZ) دیدار کرد.
▪️
امارات شریک کلیدی عملیات تحت رهبری آمریکا برای بازگشایی تنگه و هدایت نفتکش‌ها در عبور از آن بوده است. این کشور همچنین برای موفقیت کارزار فشار اقتصادی آمریکا علیه ایران نقشی حیاتی دارد.
▪️
طحنون بن زاید یکی از قدرتمندترین چهره‌های امارات است: او برادر محمد بن زاید، رئیس امارات، مشاور امنیت ملی این کشور و معاون حاکم ابوظبی است و بر منافع گسترده سرمایه‌گذاری و فناوری امارات نظارت دارد.
▪️
به گفته منابع، ویتکاف و طحنون بن زاید درباره گام‌های بعدی در بحران ایران تبادل نظر کردند و درباره مسائل دیگری نیز گفت‌وگو داشتند.
▪️
کاخ سفید به درخواست برای اظهارنظر پاسخ نداد.
زمینه خبر:
این دیدار چند روز پس از آن انجام شد که اسکات بسنت، وزیر خزانه‌داری آمریکا، «عملیات طرد اقتصادی» (Operation Economic Outcast) را اعلام کرد؛ تعهدی برای اعمال تحریم‌های سنگین علیه کشورها و نهادهایی که با جمهوری اسلامی تجارت می‌کنند.
▪️
به گفته یک منبع مطلع از این تماس، بسنت پیش از اعلام این طرح با طحنون بن زاید گفت‌وگو کرده بود.
▪️
در همان روزی که ویتکاف با طحنون دیدار کرد، وزارت خزانه‌داری آمریکا برای قطع دسترسی شعب اماراتی «بانک مصر» از نظام مالی آمریکا به‌دلیل معاملات این بانک با ایران اقدام کرد. اقدام پیشنهادی، تراکنش‌های دلاری این بانک را مسدود خواهد کرد.
▪️
بانک مرکزی امارات اعلام کرد «بررسی فوری» تراکنش‌هایی را که شعب این بانک مصری با ایران داشته‌اند، انجام خواهد داد.
نگاهی دقیق‌تر:
چند روز پیش از اعلام تحریم‌های دولت ترامپ، امارات تصمیم گرفت تمام تجارت، مبادلات بازرگانی و تراکنش‌های مالی با ایران را متوقف کند.
▪️
این تصمیم اقدامی چشمگیر بود، زیرا امارات — و به‌ویژه دبی — یکی از مراکز اصلی تجارت و صادرات مجدد برای ایران محسوب می‌شد. حجم تجارت دو کشور در سال ۲۰۲۴ به ۲۸ میلیارد دلار رسیده بود.
▪️
یک منبع دیگر مطلع از موضوع گفت مقام‌های اماراتی به دولت ترامپ گفته‌اند برای آنکه هر کارزار فشار اقتصادی علیه ایران مؤثر باشد، باید همه کشورهای کلیدی که با جمهوری اسلامی تجارت می‌کنند در آن گنجانده شوند.
پشت پرده:
به گفته دو منبع مطلع، تحریم‌های ثانویه قریب‌الوقوع دولت ترامپ علیه ایران یکی از عوامل تصمیم امارات بود، اما دلیل اصلی آن نبود.
▪️
به گفته منابع، ۱۱ اوت یک هیئت ایرانی برای گفت‌وگوهای دیپلماتیک کم‌سروصدا با مقام‌های اماراتی به ابوظبی سفر کرد.
▪️
منابع گفتند ایرانی‌ها در این گفت‌وگوها اعلام کردند که خواهان کاهش تنش و بهبود روابط هستند — پس از آنکه ایران در جریان جنگ هزاران موشک و پهپاد به سوی امارات شلیک کرده بود.
▪️
به گفته منابع، ایرانی‌ها حتی از امارات برای تأمین غذا و دارو درخواست کمک کردند و از اماراتی‌ها خواستند با تحریم‌های آمریکا همکاری نکنند؛ درخواستی که بلافاصله رد شد.
▪️
اما در چند روز بعد، سپاه پاسداران حملات خود به نفتکش‌های شرکت ملی نفت امارات را که تلاش می‌کردند از تنگه هرمز عبور کنند، تشدید کرد.
▪️
منابع گفتند اماراتی‌ها خشمگین شدند و تصمیم گرفتند تمام روابط تجاری با ایران را تعلیق کنند.
موضوعی که باید زیر نظر داشت:
مقام‌های آمریکایی گفتند مارکو روبیو، وزیر خارجه آمریکا، اوایل این هفته به همه سفارتخانه‌های آمریکا در سراسر جهان دستور داد درباره «عملیات طرد اقتصادی» یک پیام رسمی دیپلماتیک به عالی‌ترین سطوح دولت‌های میزبان خود ارائه کنند.
▪️
به سفارتخانه‌های آمریکا دستور داده شد از کشورها بخواهند «فوراً و به‌صورت نظام‌مند» تمام تجارت با ایران را قطع و فعالیت‌های تجاری غیرقانونی ایران را شناسایی کنند.
▪️
مقام‌های آمریکایی گفتند در این پیام دیپلماتیک تأکید شده است که کشورها، شرکت‌ها و افرادی که به تجارت با ایران ادامه دهند، در معرض تحریم و قطع دسترسی به نظام دلاری قرار خواهند گرفت.
▪️
یکی از مقام‌ها گفت پیام ویژه‌ای برای نمایندگی‌های دیپلماتیک آمریکا در ابوظبی، مسقط، هنگ‌کنگ، دوحه، لندن، برلین و چند پایتخت آسیای مرکزی ارسال شده است. در این پیام به آن‌ها دستور داده شده از دولت‌های میزبان خود بخواهند تمام شعب بانک‌های ملی و صادرات ایران را که با سپاه پاسداران مرتبط هستند، تعطیل کنند.
گام بعدی:
یک مقام آمریکایی گفت دولت ترامپ در حال تشکیل یک کارگروه بین‌سازمانی برای هماهنگی اجرای کارزار فشار اقتصادی علیه ایران و نظارت بر اجرای آن است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/VahidOnline/78199" target="_blank">📅 03:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vmHkVhreMJ3EdwFhJ-X7jZiVfVQ6k3h57iJ6sEZFGl8nQtRm9oYW9icWy_jlmrtgjQl4PDi4uT7uWP3ZhM8viwBmBEZKOjLKTL6NsmzSe4Ds9O9Ujvb33mIjrYjiriJ9hNjD4koZxNqAyr2S_KB0SzOkyUMoifK5i6IyhGiworVtJjqTgdBIJb6lBarN9APOM24WdEfhnZ19-bonI8zoANbwXpFXZcbubEEx0N9GqRDzsIP_8NlNdpxHWjs2BI2XRu5gXWI2tVIr5myzLmKvQR7C-dg4ZYeaFKkwIWGZBgDsV6wZRLaxx4YunKtIFiJ3NC_lVB40i97Je_c4sjAcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=lTycbR1tFCdkUeqDMA_xzUlzcgJutvy35Er7A_cImVCsjNzWIJasFprrW4w2XJmWVqo7BtRZj6nKkj9-YHf79eNSydGolPCIXxcTUEGvT90N6xljfZ_6YpkhoZz3bA8tJnu1KNalwHj-4b2KVv85g0OYagGVLuMUxYeyG09HkV2BMid6byHIHT6q1OuhbG3vrl90yioQ2Mh2jPgiwqJhkZHTpL_U-7KO_s6lpzhwi2yskqEQUvlaHqu7jNT_GoEvy4v4m2Z3RPA3ZDOljG1wI3xD6tFNqSBhss_potS_REjiTcQzuSqoshh1L5zYu9OOOxb1qS4iKvHIFxWnAmZvJw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=lTycbR1tFCdkUeqDMA_xzUlzcgJutvy35Er7A_cImVCsjNzWIJasFprrW4w2XJmWVqo7BtRZj6nKkj9-YHf79eNSydGolPCIXxcTUEGvT90N6xljfZ_6YpkhoZz3bA8tJnu1KNalwHj-4b2KVv85g0OYagGVLuMUxYeyG09HkV2BMid6byHIHT6q1OuhbG3vrl90yioQ2Mh2jPgiwqJhkZHTpL_U-7KO_s6lpzhwi2yskqEQUvlaHqu7jNT_GoEvy4v4m2Z3RPA3ZDOljG1wI3xD6tFNqSBhss_potS_REjiTcQzuSqoshh1L5zYu9OOOxb1qS4iKvHIFxWnAmZvJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان حملات شب گذشته آمریکا به روستای کوهستک در سیریک، علاوه بر یک برج مخابراتی، دستکم دو خانه مسکونی هم هدف حمله قرار گرفتند.
کوهستک دیشب پنج بار هدف قرار گرفت که به نظر می‌رسد چهار موشک به یک محل اصابت کرده است.
بر اساس تصاویر دوربین مدار بسته، سه موشک اول به خانه محل عروسی اصابت می‌کند.
به نظر می‌رسد موشک چهارم به دکل مخابراتی همراه اول و موشک پنجم دوباره به محل عروسی اصابت می‌کند.
دکل مخابراتی با خانه محل عروسی حدود ۱۱۲ متر فاصله داشته است و چند خانه اطراف هم آسیب دیده است.
@
VahidHeadline
به گزارش خبرگزاری مهر، خانه مسکونی محل برگزاری عروسی ۱۳۶ متر با دکل مخابراتی که هدف حمله موشک‌های آمریکایی بود، فاصله داشت.
مقام‌های امداد و نجات جمهوری اسلامی و رسانه‌های دولتی ایران اعلام کردند بر اثر این حمله ۴ نفر کشته و ۶۸ نفر دیگر زخمی شدند.
کوچکترین قربانی این حمله، امیرعلی کریمی چهار ساله بوده است.
@
VahidOOnLine
آپدیت:
بی‌بی‌سی چند ساعت بعد خبرش رو ویرایش کرد و اسم سلاحی که نوشته بود رو عوض کرد ولی همچنان نوشتند موشک.
گویا پیش‌تر نیویورک‌تایمز هم درباره نوع پرتابه ادعای مشابهی مطرح کرده بود ولی بعدا پس گرفتند.
با جست‌وجو دیدم یکی اینجا خیلی مفصل بررسی کرده:
Mk20002000B
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/78197" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=jQRADzJymS6cav2wesN9oPel67QwoIKBJ-OOcoGW6wcbvsSYPQm1bdwRLQCbqimMCD8ZTWGnYCjoBRROcI7Kk_mDEQZC3VHiU7ihmd4wHvy8tvln9LbQlqcxiL_U4zQnYNDUOL-wHT90_qlF7JL1kcQx8aFzS8_o7zjFPboyPI9GhblZs5ZPJU7hKmNTT_pgqvlIho20B6NCsfWfS_TcdveqXezpbpb7b9BM_-ESQAbHkaHzgWQfYO1V1osZPc4Z9Tvg477ixFqpWOn-T2K69H2pm7SAGLnCSFhzpmTUhLRgzoMd4rkJcFkzDXe4CI_R8vQIDSxuK1PM8O8pHvBEtXZuQh_o8RJ6ZSq9ShYDlinyq5KK7EIMe28HFHJ1_ne-X1eh3TYq_1Wwysa7MNBzgqCA9fh9ry1yZP_V1sKwfWfqS5RqoNYLh9Axx45NUJsUFtBGk4VB__HrdPW7TkhAtm_bxa5dLCKGOQIlYFbHm1oIfv3pCC4vY3KR9yCoaczz345usWg1PJXQJNNb-t_G0eNicNr0hXfmI2P8bObVr4QtxxO-oQZzDWjD9BQ7WtFMWdEcCD-dzmEhqx1qaBQWeIxkYsx-hrgAYOOoMuSNndO-ktwQt0aLxQepCFfOU6-ABrc800Mh_2SD8mHF64C-Qc0Giak3Mzsq_zTDe0SdT-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=jQRADzJymS6cav2wesN9oPel67QwoIKBJ-OOcoGW6wcbvsSYPQm1bdwRLQCbqimMCD8ZTWGnYCjoBRROcI7Kk_mDEQZC3VHiU7ihmd4wHvy8tvln9LbQlqcxiL_U4zQnYNDUOL-wHT90_qlF7JL1kcQx8aFzS8_o7zjFPboyPI9GhblZs5ZPJU7hKmNTT_pgqvlIho20B6NCsfWfS_TcdveqXezpbpb7b9BM_-ESQAbHkaHzgWQfYO1V1osZPc4Z9Tvg477ixFqpWOn-T2K69H2pm7SAGLnCSFhzpmTUhLRgzoMd4rkJcFkzDXe4CI_R8vQIDSxuK1PM8O8pHvBEtXZuQh_o8RJ6ZSq9ShYDlinyq5KK7EIMe28HFHJ1_ne-X1eh3TYq_1Wwysa7MNBzgqCA9fh9ry1yZP_V1sKwfWfqS5RqoNYLh9Axx45NUJsUFtBGk4VB__HrdPW7TkhAtm_bxa5dLCKGOQIlYFbHm1oIfv3pCC4vY3KR9yCoaczz345usWg1PJXQJNNb-t_G0eNicNr0hXfmI2P8bObVr4QtxxO-oQZzDWjD9BQ7WtFMWdEcCD-dzmEhqx1qaBQWeIxkYsx-hrgAYOOoMuSNndO-ktwQt0aLxQepCFfOU6-ABrc800Mh_2SD8mHF64C-Qc0Giak3Mzsq_zTDe0SdT-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین
و متن زیرنویس تا اونجایی که جا می‌شد در یک پست:
🔺
خبرنگار:
ترامپ، شما امروز در تروث سوشال نوشتید: «مردم ایران چه زمانی قیام می‌کنند و می‌جنگند؟» خب، اگر این چیزی است که می‌خواهید، آیا سیا را می‌فرستید تا ایرانی‌ها را مسلح کند؟
🔻
ترامپ:
خب، نمی‌خواهم این را به تو بگویم، پیتر. خیلی دوست دارم به تو بگویم، اما گفتنش مناسب نیست. اما من... یعنی، من وضعیت دشوارشان را درک می‌کنم. همین حالا دارند به آن‌ها شلیک می‌کنند.
می‌دانید، این آقایان اینجا در ناز و نعمت نشسته‌اند و چیزهایی را می‌بینند، اما آنجا اوضاع چندان راحت و مرفه نیست. تا سه ماه پیش، ۵۲ هزار معترض کشته شده بودند. می‌توانید تصورش کنید؟ و حالا می‌شنوم که این تعداد احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم بیشتر شده. نزدیک به ۶۵ هزار معترض کشته شده‌اند.
پس وقتی آن سؤال را مطرح می‌کنم، به‌نوعی جوابش را هم می‌دانم. تنها پاسخ این است که به آن‌ها شلیک می‌شود. رژیم هر روز ضعیف‌تر و ضعیف‌تر می‌شود و در مقطعی دیگر نمی‌توانند به این راحتی شلیک کنند، چون فکر می‌کنم مردم دیگر این را تحمل نخواهند کرد.
اما من آن سؤال را مطرح کردم چون، می‌دانید، وقتش رسیده است. اما بیشترِ... بیشتر مردم نمی‌توانند مردم خودشان را این‌طور بکشند. بیشتر مردم سعی می‌کنند منطقی برخورد کنند، گفت‌وگو می‌کنند و بعد ممکن است حکومت سرنگون شود. در ایران، مردم را می‌کشند. وقتی برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند. درست بین دو چشمشان شلیک می‌کنند.
آن‌ها دو روش دارند: مسلسل و تک‌تیرانداز، و از هر دو استفاده می‌کنند؛ گاهی مسلسل‌ها و گاهی تک‌تیراندازها. تک‌تیراندازها را بیشتر دوست دارند، چون کافی است جمعیتی ۲۰۰ هزار نفری باشد و یک نفر همین‌جا با گلوله‌ای بین دو چشمش به زمین بیفتد، و سه تک‌تیرانداز این کار را انجام دهند؛ و تماشای آن وحشتناک است. واقعاً وحشتناک است.
برای همین است که این اتفاق نمی‌افتد. و چه کسی می‌تواند سرزنششان کند؟ چه کسی می‌تواند سرزنششان کند؟ اما رژیم هر روز ضعیف‌تر می‌شود.
—————-
ما  داریم تنگه هرمز را کنترل می‌کنیم. ما داریم هر روز کشتی‌های زیادی را خارج می‌کنیم که میلیون‌ها بشکه نفت حمل می‌کنند. در بیشتر موارد این کار را بدون مشکل انجام می‌دهیم. هر از گاهی آن‌ها یک پهپاد می‌فرستند و ما آن را ساقط می‌کنیم.
اما ما کنترل داریم؛ کنترل بسیار قدرتمندی. آن‌ها تلاش می‌کردند سامانه‌های راداری و یک سامانه موشکی و سامانه‌ای برای ریختن مین را بازسازی کنند. می‌دانید، ما همه مین‌ها را در تنگه هرمز از بین بردیم. آن‌ها تلاش می‌کردند موشکی بسازند که مین می‌ریزد. چه کسی چنین کاری می‌کند؟ تا حالا موشکی ساخته‌اید که مین بریزد؟ من هرگز چنین چیزی نشنیده بودم، اما این کاری بود که آن‌ها می‌کردند.
داشتند آن را می‌ساختند. تقریباً تمام شده بود، پس ما نابودش کردیم. دیدیم که داشتند آن را می‌ساختند. ما هر کاری را که می‌کنند می‌بینیم. نمی‌توانند تکان بخورند. حتی نمی‌توانند به دستشویی بروند بدون اینکه ما ببینیم. پس آن را دیدیم. نابودش کردیم.
...
بنابراین دیشب محکم به آن‌ها حمله کردیم؛ خیلی محکم. آن‌ها یک ضربه خیلی کوچک زدند، اما ما دیشب خیلی محکم به آن‌ها حمله کردیم. همه تجهیزات جدیدی را که تلاش کرده بودند در امتداد تنگه هرمز بسازند نابود کردیم؛ بعضی دفاعی و بعضی تهاجمی.
آن‌ها سعی می‌کردند کشتی‌ها را ببینند، چون نمی‌توانند کشتی‌ها را ببینند. می‌دانید، ما تعداد زیادی از کشتی‌ها را از بین برده‌ایم. آن‌ها نمی‌توانند ببینند، چون رادار ندارند، چون ما آن را منفجر کردیم، و دیشب چیزهای بسیار بیشتری از فقط رادارشان را منفجر کردیم.
دیشب حمله بسیار سنگینی بود و آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
....
بنزین با آن قیمت فروخته می‌شد؛ چون نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
...
اما مسئله خیلی ساده است. ایران نمی‌تواند سلاح هسته‌ای داشته باشد. به‌محض اینکه تمام شود، که فکر نمی‌کنم خیلی بیشتر طول بکشد، نمی‌دانم چقدر دیگر می‌توانند تحمل کنند، اما می‌دانید، هرچه باشد، اهمیتی ندارد.
و انتخابات روی من تأثیری ندارد. اول اینکه، من نامزد نیستم. اما حزب من نامزد دارد و من قرار است به حزبم کمک کنم. اما فکر می‌کنم حزب من به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران سلاح هسته‌ای داشته باشد.
————-
🔺
خبرنگار:
آقای رئیس‌جمهور، چقدر درباره تغییر نام تنگه هرمز به «تنگه ترامپ» جدی هستید؟ و اگر جدی هستید، چطور این کار را انجام می‌دهید؟ چطور این کار را می‌کنید، آقای رئیس‌جمهور؟
🔻
ترامپ:
فقط همین‌طوری مطرح شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78196" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=fynRpnf6uQ3PeEnjs_sDEV6lUUuwtCx2aRtSI85Q3qG-8x0q9XNez4ewdmZ-2oageWgXny_fMGx4Fs_1yfvF-PZezM-opHAl81Tg-pGsMHDqSJVuXaE1PqA2AXaB9jos4p_QEwZbQSi6sKgXb5LpnjyBVu_PQ-iuYPTX_jt-5y5JN_3pNQo-0Xw_okK75yKTq-WaJ06EFd7jOZNKc7oua__QGAdqV3BHrPAvmIT1d80WgJIxAa50QuOrsbUCKAtiikKlSq4N29L9155kiqsSrz1EuRNrWywpKKKxJpy7tIrP5oiD0ciX0F1sJsgSpmil_omD9xlzvrDq6g8ip2-qsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=fynRpnf6uQ3PeEnjs_sDEV6lUUuwtCx2aRtSI85Q3qG-8x0q9XNez4ewdmZ-2oageWgXny_fMGx4Fs_1yfvF-PZezM-opHAl81Tg-pGsMHDqSJVuXaE1PqA2AXaB9jos4p_QEwZbQSi6sKgXb5LpnjyBVu_PQ-iuYPTX_jt-5y5JN_3pNQo-0Xw_okK75yKTq-WaJ06EFd7jOZNKc7oua__QGAdqV3BHrPAvmIT1d80WgJIxAa50QuOrsbUCKAtiikKlSq4N29L9155kiqsSrz1EuRNrWywpKKKxJpy7tIrP5oiD0ciX0F1sJsgSpmil_omD9xlzvrDq6g8ip2-qsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، و دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، روز چهارشنبه توافقی نفتی را در کاراکاس امضا کردند که بر اساس آن ایالات متحده کنترل اکثریتی بر ۶۵ میلیارد بشکه از ذخایر نفت ونزوئلا به دست می‌آورد.
این میزان حدود یک‌پنجم ذخایر عظیم نفتی ونزوئلا را شامل می‌شود. دونالد ترامپ، رئیس‌جمهور آمریکا، این توافق را «بزرگ‌ترین معامله نفتی در تاریخ جهان» توصیف کرده است.
بر اساس این توافق، آمریکا به ۱۷ میدان نفتی ونزوئلا دسترسی ترجیحی خواهد داشت؛ تأسیساتی که برخی از آنها پیشتر در اختیار شرکت‌های روسی و چینی بوده‌اند.
همزمان، شرکت شورون نیز از توافق جداگانه‌ای به ارزش هفت میلیارد دلار برای توسعه دو میدان نفتی دیگر در کمربند اورینوکو خبر داده است. شورون می‌گوید این سرمایه‌گذاری می‌تواند تولیدش در ونزوئلا را طی پنج سال بیش از دو برابر کند.
وزیر انرژی آمریکا پیش‌بینی کرده است تولید نفت ونزوئلا تا پایان دهه جاری به بیش از دو میلیون بشکه در روز برسد؛ حدود دو برابر سطح تولید در ژانویه، زمانی که نیروهای آمریکایی نیکلاس مادورو را سرنگون کردند و دلسی رودریگز قدرت را در دست گرفت.
این توافق با انتقادهایی نیز روبه‌رو شده و منتقدان دولت رودریگز را به واگذاری حاکمیت ونزوئلا بر منابع نفتی خود متهم کرده‌اند. دولت ونزوئلا در مقابل می‌گوید این توافق به این کشور برای بهره‌برداری از ظرفیت‌های انرژی و جذب سرمایه‌گذاری کمک خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78195" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7WCnVASiIFqx9P06CYTZHBpd-zgus8IHOvRTWjYCnIvadoFPSuRYuR3yz8_xflj3wDwr6Sfe6-d0Xr8K9dKHfDwo8SFtJvrQEuIlDj_KuAvxXDGfPa8Dx8kjtRtuR8zIVPFmTHRbtqLcs5FPYeSbNaDCrKbTtdt6A-yk5MRqxPg1ZBwuVan2ZZyfCV3kyYMPgXlyBXh5F_XDPXT3TbKZLGeVvXUVWW8zPVDfFmrIf45tbwOtG6TuSWgBlqxDycyFOe9WBwXNZLBGYLEN5B9sitjH_0JVfKFhIMiyGO8g_xFHzTonVSDnOVdsuy7XdxZKWx9hvu8PoOrq3nJkKeCcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=dqEHjvp0LGkhI7SgCONdmBQ4q-4lI-YEfeF4P3cInghpC2_utdDLm0M_y3CtsI108PcMF9db7k2D5kGYPJeABSKHFizMahgbQgsfnF_9RoYz9B28fYfbLO6qnuy9asVa-kn9sPkZ0p2BiuEZAo3ABioGccPdTe_ZvDwbzjE3eRz2vV4Jxjt_0nyGLMdbLBSru2P2xdEGuuv23ewv8eRbJJBbTgmCVJR-OA84mi2TluTuIjZIjcQLMiepHxQAHvZrpvZylceIyIQw8PjgehUr15jJzyoq8q2DuRO84SQxi8_W-B8chITPomchvTTvFhtgSd034ETLE8o6RGtyW38PKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=dqEHjvp0LGkhI7SgCONdmBQ4q-4lI-YEfeF4P3cInghpC2_utdDLm0M_y3CtsI108PcMF9db7k2D5kGYPJeABSKHFizMahgbQgsfnF_9RoYz9B28fYfbLO6qnuy9asVa-kn9sPkZ0p2BiuEZAo3ABioGccPdTe_ZvDwbzjE3eRz2vV4Jxjt_0nyGLMdbLBSru2P2xdEGuuv23ewv8eRbJJBbTgmCVJR-OA84mi2TluTuIjZIjcQLMiepHxQAHvZrpvZylceIyIQw8PjgehUr15jJzyoq8q2DuRO84SQxi8_W-B8chITPomchvTTvFhtgSd034ETLE8o6RGtyW38PKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با شبکه نیوزمکس گفت که ایالات متحده لزوما به دنبال فروپاشی جمهوری اسلامی ایران نیست، هرچند تحولات درونی و قیام مردم امکان‌پذیر است.
او همچنین به مخاطرات شخصی پیش‌روی رهبران و فرماندهان نظامی ایران با افزایش فشارها اشاره کرد.
بسنت ادعاهای ایران درباره کنترل بر تنگه هرمز را رد کرد و گفت با عبور حدود ۱۷ میلیون بشکه نفت در روز گذشته، کنترل ایران بر این تنگه بی‌معناست. او همچنین گزارش‌ها درباره وجود مین یا برخورد دو کشتی با مین در تنگه هرمز را تکذیب کرد و رسانه‌ها را به بازنشر سریع ادعاهای نادرست ایران متهم ساخت.
وزیر خزانه‌داری آمریکا، با اشاره به تداوم خرید نفت ایران توسط چین تاکید کرد که تنها حدود ۳۰ میلیون بشکه نفت ایران روی آب باقی مانده و این ذخایر نیز به‌زودی به پایان خواهد رسید.
بسنت روز گذشته نیز در جریان سخنرانی در مجمع اقتصادی جی۲۰، تاکید کرده بود که فشارهای اقتصادی یا به ایجاد شکاف و دودستگی در سپاه پاسداران و احتمالا مقابله مردم با آن‌ها منجر می‌شود یا مقام‌های تهران تصمیم می‌گیرند که به میز مذاکره بازگردند.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با شبکه آی‌۲۴ درباره حکومت ایران گفت: «نیروهای ما می‌توانند هر لحظه در آنجا باشند. ما این حکومت را شکست خواهیم داد.»
نتانیاهو درباره اینکه آیا منظور او از شکست دادن، سقوط کردن حکومت است، گفت: «بله، سقوط خواهد کرد و ما آن را سرنگون می‌کنیم.»
نتانیاهو در پاسخ به این سوال که آیا رومان گوفمن، رییس موساد، برای سرنگونی جمهوری اسلامی فعالیت می‌کند، گفت: «همه دستگاه‌های ما تحت هدایت من برای سرنگونی این حکومت و شکست آن فعالیت می‌کنند.»
نتانیاهو گفت: «در نهایت با سر اختاپوس، برخورد خواهیم کرد، بازوها را قطع خواهیم کرد و محور شر ایران را هدف قرار خواهیم داد. این کار را با قدرت بسیار انجام دادیم؛ خلبانان ما آنجا بودند و هر لحظه می‌توانند آن جا باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78193" target="_blank">📅 21:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSrv0R_E_pAsd4NBKlmqnvJobGixws7SH4CWDj36JD4SFBZbQR71y_mnv298Tpvt2OmtYCV2y_J_zisWnux4pDOJg2sdwhFzLfYDrxdBGzD9s-rFta2mMVs_25ESCilckibr6keOL9W-V3TdwCCe4NejFDlPicK0lYl4hOF9rL_2dd2F1LMEfJlg4vPvpGqzEFq8L4hEO-Kd5Z8KQMsZ_wiCi5af0AZ1Y-YbUin9-dJQoM9GFgEi-Lm7bSx_Zm6yJpwPrAas0R1H5vixjNC57ZSfLPrrxFSiNEN0tBLxTwF_0KPhkrWCFgHwIwQmSFeN6P1Tw4WBl1U2mKD_11ijNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی جمهوری اسلامی، با هشدار به ایالات متحده گفت تهران در جنگ جاری از «راهبردی جدید» استفاده خواهد کرد.
رضایی، چهارشنبه ۱۱ شهریور ۱۴۰۵، در پستی در ایکس نوشت که تلاش‌های آمریکا برای خروج از شرایط کنونی نتیجه‌ای نخواهد داشت و افزود: «به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، پایه‌های شما را درهم خواهد شکست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78192" target="_blank">📅 19:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CptemAlHt3BicXrRM-FoOdZzPLHjNqX-4zcyHONfshPZMA7_aKMnmJv6XPjiODMv6arYO6Vc9BAV2FDlgyyGUE0EoWtvIIEX9J1Qvc6-oX9lKqH9e93q3xrvSOEqaQNSgQyishkHsTcOeCDf3ec5PVYq1s9-fsg3dVPEfeqKCIEa5_3nTWvS9BWVSnruhOfg0numj8nvhbBZwr-WHQ44WcLRW31IWfXYw7Bhk-nKI6Nl7w0Zr_bxiiBhyAavMkDoVJp5fVR_loQQ47KxXgOwgCGCbYdx3zCnYPNE930Ph80GWlCLj4e9_s76LLxJqmTZIfY5hBOK8nWH17yCspeIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
حالا که آن را تحت کنترل ایالات متحده آمریکا درآورده‌ایم، آیا باید نام «تنگه هرمز» را به «تنگه ترامپ» تغییر دهیم؟؟؟ درست مثل خود آمریکا، این تنگه هم «داغ‌تر» از هر زمان دیگری خواهد بود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
Now that we have it under U.S.A. control, should we change the name Hormuz Strait to TRUMP STRAIT??? Like America itself, it would be “hotter” than ever before! Thank you for your attention to this matter. President DONALD J. TRUMP
realDonaldTrump
در خبری دیگر:
ترامپ در گفت‌وگو با پادکست «دن پاتریک»، درباره حملات سه‌شنبه شب آمریکا در اطراف تنگه هرمز، گفت: «ما اکنون کنترل تنگه هرمز را در اختیار داریم. ما آن را کنترل می‌کنیم. دیشب ۲۸ کشتی را از بین بردیم. ما آن را کنترل می‌کنیم، آنها چیزی دریافت نمی‌کنند و ما کشتی‌ها را از بین بردیم.»
ترامپ همچنین درباره حکومت ایران گفت که جمهوری اسلامی دو هفته با داشتن یک سلاح هسته‌ای فاصله داشت. او افزود: «اگر آنها سلاح هسته‌ای داشتند، اسرائیل از بین می‌رفت، خاورمیانه از بین می‌رفت و آنها به شهرهای ایالات متحده حمله می‌کردند. چون آنها دیوانه هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78191" target="_blank">📅 19:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jokr8_-MUlmeq_nAkRroPLP-OCRCGMXMwpRBl6z971sgGiDMmByT_ZqUTE-bKTODM5zQwGq9F8UOjiZjmMw9oTOS91MWW57PwM0kZLvw5EvbaC-eO0t1thGUaqTn0ArDNNgcvkFEwoQPyEIVd26x-8pjhph7_AxJka5vw_lcw8fnNYi8HCH6FzOb-e5p0AHCKbIySNoSG4gYB7ShTrTMNfxbSVztezZd3eVZypZ6keFYm6sY4sXJCpm8QlDmyR0lpeC-Bt-ZP317xEU5uWp3GbN_HNglwbR7n5oajbqlBzpCKi4v5pvTV69v24f7FpxQYMlziRePiFMTSQBYplg_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی گفت: آمریکایی‌ها باید به تعهدات خود عمل کنند تا ما اقدام به بازگشایی تنگه هرمز کنیم.
محمدباقر قالیباف، در دیدار با مسئول ارتباطات اسلامی حماس گفت جمهوری اسلامی مذاکره را رد نمی‌کند، اما آن را «ابزاری برای مبارزه» می‌داند.
او گفت کنار گذاشتن مبارزه با آمریکا و اسرائیل به معنای شکست است.
او افزود جمهوری اسلامی در جریان مذاکرات، پایان جنگ علیه ایران و متحدانش در «جبهه مقاومت» را در ماده نخست تفاهم‌نامه مطرح کرد، در حالی که به گفته او، طرف مقابل در متن اولیه ۱۵ ماده‌ای خواستار توقف کامل فعالیت‌های موشکی، هسته‌ای و فعالیت‌های «جبهه مقاومت» شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78190" target="_blank">📅 19:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KY6SZYhJc3OxcItwSIH48kcg9JyEbdVOxO8tIetPI0KFTtjztN4I3gSU_QAALFp3mBGO0ljE1EkmqwDthammCOkWD3isjUD2mViqBkjdUjcXx3VSOnGWYhb4bMBfhGfljwQDDmdyt_JFDkgilrZXbnasWfJvcXjmE6A0uo09uCoheMVZbpchh5nlQ8GC5uDQiNjXv-O2UoVL-Vgc7BQDHJaG1Dz_LAR0ZiO9Fzpp8MK6lWKnBbK9Gd2blb7An3pU6AHP-bE455awnBdtYHr7-rtwz6FYkeC45EROwOluDamPHUgf2F91nKES6Wg1qbPe-jRRtBOeS8FODPGSjFX1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس آمارهای اعلام شده از سوی شرکت ملی پخش فرآورده‌های نفتی ایران، میانگین مصرف روزانۀ بنزین در نخستین هفتۀ شهریورماه از مرز ۱۴۸ میلیون لیتر گذشته است.
بر اساس این آمارها، بیشترین میزان تقاضای روزانه در ۸ روز نخست آخرین‌ماه تابستان، بیش از ۱۵۴ میلیون لیتر بوده و در این بازه در مجموع بیش از یک میلیارد و ۲۰۰ میلیون لیتر بنزین عرضه شده است.
کاهش شدید ظرفیت تولید در ماه‌های اخیر در اثر حملات آمریکا به تأسیسات نفتی ایران از یک‌سو و مشکلات دولت برای وارد کردن بنزین از سایر کشورها از سوی دیگر، باعث افزایش قیمت بنزین و حتی مطرح شدن احتمال بالاتر رفتن قیمت این فراورده و افزایش شدید تقاضا برای آن شده است.
مسعود پزشکیان رئیس‌جمهور و شماری دیگر از مقام‌ها تأکید کرده‌اند که دولت توان چندانی برای وارد کردن بنزین و بخصوص عرضۀ آن با قیمت‌های قبلی ندارد.
دولت ایران اما در عین حال ادعا می‌کند که تشکیل صف در برخی جایگاه‌های عرضۀ بنزین، ناشی از هیجان و بار روانی بوده و مشکلی در تأمین بنزین مورد نیاز کشور وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78189" target="_blank">📅 17:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kvxBNaD4W0JroiUqx2HPu69QVbxYa-uQjsxpXlTxE1uon5o52b6V-x9MHbJPeEQBQa6MeJaj-nTZs7sTVwQeVILJy4WQ4PBQrAVSjx2uSEMpYvhv1XlX_rOhNKxi6_v9IFufDmNhdujlruOBflF5AfSVzeic2brDjniGesEaHCRm8q-IH-vk4dCukjzcO0UIuoUy4Qp8R007ZzR7wPzIDf-d4vR9oqOUnRxKEWD5_OzLLvbzkEt1o2R9u3XiBhINCMRfYNez3jKAzUXNRZyCguaEGpzP_-EI0wAosEuIW4XDpbb0a3CsP38ZrJuWjlUUEIvEOGOFvh5ff5Ff2X9cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در ایران بامداد چهارشنبه ۱۱ شهریور و ساعاتی پس از دور جدید حملات آمریکا، رکورد تازه‌ای ثبت کرد و قیمت یورو، پول واحد اروپایی، برای نخستین بار از مرز ۲۵۵ هزار تومان گذشت.
وب‌سایت‌های اعلام نرخ ارز قیمت دلار از جمله «نوسان»، قیمت دلار آمریکا را حدود ۲۲۰ هزار تومان گزارش کردند. قیمت درهم امارات هم به بیش از ۶۰ هزار تومان رسیده است.
افزایش قیمت نرخ ارزهای خارجی در بازار آزاد ایران از زمان اعلام امارات در قطع روابط مالی با ایران و آغاز برنامهٔ فشار اقتصادی آمریکا موسوم به «عملیات طرد اقتصادی» شدت گرفته است.
در دو هفته اخیر پول ملی ایران در مقابل ارزهای عمده خارجی بیش از ۱۰ درصد دیگر از ارزش خود را از دست داده است.
روز چهارشنبه قیمت سکه طلای موسوم به «امامی» هم با وجود کاهش جهانی قیمت طلا، ۲۲۴ میلیون تومان گزارش شد.
عبدالناصر همتی، رئیس‌کل بانک مرکزی، روز ۱۰ شهریور ادعای کمبود منابع ارزی و احتمال فروپاشی اقتصاد ایران را رد کرد و گفت بانک مرکزی آماده است برای مهار بازار تا دو میلیارد دلار ارز عرضه کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78188" target="_blank">📅 16:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DVRQvmINoKGHN0LW0hHbNmkH4V-GkIDAJ5e3Hz4c-SI_vkH0ewkJ9Nk57JUJDvJrv2vlGOvobkW7KHOcFblmy6EAzRXW-yVfRGRZOf5971jdCe4XuAKMmhLDE40QSAVhwdgDkQT_oqr35UhIr6bS8kS9jVrrNGaoyy5b_8obzOXWFJnNxWK6GhbsaNIxWbquJQq9n2ZBtBxIyJ5-rDDpuLAy8TMmF4x-PfouvQAmnsAh_yNBLgAIMsfA-2r2kw9ApRNy-5IEHG6uAAbcmqHBCieAjheZG8RMbjRGxLGnP_VR6EOsVydg6o9CR1zoV0W2AbnlrsOFZZEOFSGqlTTMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد که ارتش ایالات متحده در جریان موج حملات شامگاه سه‌شنبه دهم شهریور به اهدافی در جنوب ایران، «دو نفتکش دولتی» این کشور را نیز هدف قرار داده است.
بر اساس این گزارش، این دو نفتکش در نزدیکی سواحل ایران و در شمال خط محاصره دریایی آمریکا لنگر انداخته بودند و پهپادهای آمریکایی با شلیک موشک موتورخانه‌های آن‌ها را هدف قرار دادند.
فرماندهی مرکزی ارتش آمریکا، سنتکام، در بیانیهٔ رسمی خود پس از حملات سه‌شنبه‌شب اشارهٔ مشخصی به حمله به نفتکش‌ها نکرد، اما در تصاویر ویدئویی که از حملات منتشر کرد، صحنه‌ای از اصابت موشک به نفتکش نیز دیده می‌شود.
اکسیوس می‌گوید این نخستین بار است که ارتش آمریکا نفتکش‌های ایرانی را نه برای جلوگیری از نقض محاصره دریایی، بلکه در واکنش به حملات ایران به کشتی‌های عبوری از تنگه هرمز هدف قرار می‌دهد.
یک مقام آمریکایی این اقدام را بخشی از سیاست تازه‌ای موسوم به «نفتکش در برابر نفتکش» توصیف کرده که به‌گفتۀ او دونالد ترامپ برای بازدارندگی از حملات بیشتر ایران به کشتی‌ها تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78187" target="_blank">📅 16:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78183">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G51fQX8R7GiQDmUJwgc_U7NQmrbEOF9Yo0z90E4gZ_6X0xCCn-doU3rylnAg3j_J-OlZWRKqin4fub2rfnN8OMcGOX-en-kwYglvpCrMUNguPWttCfwcX7WVAvF_kEXePZuU2lKcZQhHpnIeiSyJk5sEJgem5j4AUe2d5umkxiRYGuZSl1lF0CA4rCREmNiKpJAPAQfOgDXsG1iRtMk7Q-bq849SA4oLEhYCYRGcSsqZKuuinF1vy3swBaRnY_CVrAjk8-unySjsa0GKafTrvgEhyHdgtjmMKgA09IZ6SGOegsPehr4nIbUf8czvoTIs0jYi2vuCzhfyzg-z5IxAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNI2morLh_MFwcxtOpXDyINCnXNebRm19G2-xgRK43CA0_IwsrU2EyIZ4pTcYgtlYW-WirdIrTMHx2NwoxncGe-k-VXALMC5jqvRN7HSeD6g5lBb4RJVQZDN27-twbTfaRvTnlklEkvtKc2z6k0YfF_cUEo5s6C4qdL8hivP6gLkO4NF3zuLzFgDZ1czeGueuUPVeTdEmpZPB6oc2aGGkKB63f8tsTmfXnKQeJKs27HXm3037bgU2jaXRscX5om_XRaoJ9Q9AJfeBIz1SkTvVrOc9YJJoRXMKCoknPygK-Jf_5jHZ2arB_Anlq-tBl1FM6x_PIZu2Q1RXpVoscsgGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=KpXWEel4Q9yLFCWJQb3Kayv277Mc8wXVOLizRTvcGlrPomxtsi1a1SYmllinuBJMnsey_kigu6E2IROeVsQ4H0FqR3_vSxjLOPVyGC_JxqAB8KjedEsSiIRmntR45Z1ykP4UQT2fh5xGLVwwNGSURUZqVeElAYixKsCmOPOHPsysWPaqS17Sq1CWCyFlDfIhAeBcJQCS4qU2GmrFNHSq_y3v33ds1jovZAzKCcOyR0wEyqvZVaCQxfBBoSGzWE_dqdTim1m6dG-RHEHmL6D62DN-al8x_vWZ57Jp1QLNpZK3gsIlkVow1vEISbxXM40fd55TIqUR1knP2PwgUqSuaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=KpXWEel4Q9yLFCWJQb3Kayv277Mc8wXVOLizRTvcGlrPomxtsi1a1SYmllinuBJMnsey_kigu6E2IROeVsQ4H0FqR3_vSxjLOPVyGC_JxqAB8KjedEsSiIRmntR45Z1ykP4UQT2fh5xGLVwwNGSURUZqVeElAYixKsCmOPOHPsysWPaqS17Sq1CWCyFlDfIhAeBcJQCS4qU2GmrFNHSq_y3v33ds1jovZAzKCcOyR0wEyqvZVaCQxfBBoSGzWE_dqdTim1m6dG-RHEHmL6D62DN-al8x_vWZ57Jp1QLNpZK3gsIlkVow1vEISbxXM40fd55TIqUR1knP2PwgUqSuaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح چهارشنبه؛ وضعیت چند منزل مسکونی در کوهستک (هرمزگان).
@iliaen</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78183" target="_blank">📅 09:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05113c6026.mp4?token=Is5aJiA_C6KGvMo1gCymMfbyiwpJnLUkbuf5uEY0WNRL1v1pn7sRnKVxjdJo6rVK20CO4hT021QKQXfRV3NYmQYk5zRez7F4oIYgQOd7xLYDmLsXH3QzrZ-4Ef2XZrSPLHER8U7P4Oej3-VY_f-9n_R56ZeVIcXx4d_CslMcNCnCAu0qYNahUbfo_IDV5xFUVPsui_mk2DpMFmhPLptoPFPNGRK3PNZVGW3_dEhhMKvjBwZNyVOZqbCs3Y9QmJQT1zpGqdhauMxGq867vxo336sYCbWgeSBtgPwPJ4vVZIIvbURSnsueusb8fhzLe33pgERonFaBPmAsGX5d7QNA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05113c6026.mp4?token=Is5aJiA_C6KGvMo1gCymMfbyiwpJnLUkbuf5uEY0WNRL1v1pn7sRnKVxjdJo6rVK20CO4hT021QKQXfRV3NYmQYk5zRez7F4oIYgQOd7xLYDmLsXH3QzrZ-4Ef2XZrSPLHER8U7P4Oej3-VY_f-9n_R56ZeVIcXx4d_CslMcNCnCAu0qYNahUbfo_IDV5xFUVPsui_mk2DpMFmhPLptoPFPNGRK3PNZVGW3_dEhhMKvjBwZNyVOZqbCs3Y9QmJQT1zpGqdhauMxGq867vxo336sYCbWgeSBtgPwPJ4vVZIIvbURSnsueusb8fhzLe33pgERonFaBPmAsGX5d7QNA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روستای کوهستک در سیریک هرمزگان
ویدیوی منتشر شده در منابع حکومتی از مکانی که مورد حمله هوایی آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78182" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbb5MzzWJ6qEZfe_7-g-xrpAt3EOgfsL7ub-QlgjH5kgE1XzQ2R6dHi9VcBrChVPflcnZ7MvIZAF7lPRXWzUupPAwnFoo20epnx4t6Rp5vFhpRL846-viyFknAdUu7Ckz5e9lCvU077k5D-HgfvfoG7qvONT9H0DlCahRsgmoEaziLZyB9Epx0dr5hrjzd6sayJAxHxsJneyCakZCQnOURPOylnraMCnzbq8EAQ9ASrjRnMmkaF9Fvuq1oBM-sr7jBknL6nId3Q50RUTRQ0BTeL5s0IxZFFNlZXUZuJtPvH_TaNve-ug5RR2sYGQ8ncbhJ877MYSiq4e_2JdGx8hWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من تلاش نمی‌کنم ایران را، آن‌طور که ABC Fake News گزارش داده، به پای میز مذاکره بکشانم.
اصلاً برایم مهم نیست که آن‌ها توافقی امضا کنند که برای خودشان هم ارزشی ندارد.
من موقعیت فعلی‌مان را خیلی بیشتر می‌پسندم؛ با کنترل تقریباً کامل بر تنگه هرمز و اقتصادی که در ایران کاملاً در حال فروپاشی است.
آن‌ها فقط دارند روند اجتناب‌ناپذیر را طی می‌کنند.
مردم ایران چه زمانی به پا خواهند خاست و خواهند جنگید؟
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/78181" target="_blank">📅 04:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=VHr3G3e3JAyI46JG_s2otBwF9HcW06aRCg8PpRe9wXL3J-2BJZP7_iaRnp-DDVoDnMtYEWTEVyF22VKsYH8EbP2_A8zEEEYhRAZMVT2waCJ-BBWkd1HcLv83tqE1X0z4TYXEDvXwJ561WLPOC0gWVCtS2C_W8Baeo0Aobjrsew3f4-weiTK5h7u8KuuPKwbRJJXYnUEzt6l2SqN-8FG44EKkaWiGydXFdh6Jjnjkx-tNlJVRDTXP_vA5PMz-l1SJ5h6BZbXzKmjp_1EyxI5hDSwAe-jqIz4onGIY-dZj5CsHwfocFvaes0jhQ707AI6B31RXLqyAL8BA8JbISDRkqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=VHr3G3e3JAyI46JG_s2otBwF9HcW06aRCg8PpRe9wXL3J-2BJZP7_iaRnp-DDVoDnMtYEWTEVyF22VKsYH8EbP2_A8zEEEYhRAZMVT2waCJ-BBWkd1HcLv83tqE1X0z4TYXEDvXwJ561WLPOC0gWVCtS2C_W8Baeo0Aobjrsew3f4-weiTK5h7u8KuuPKwbRJJXYnUEzt6l2SqN-8FG44EKkaWiGydXFdh6Jjnjkx-tNlJVRDTXP_vA5PMz-l1SJ5h6BZbXzKmjp_1EyxI5hDSwAe-jqIz4onGIY-dZj5CsHwfocFvaes0jhQ707AI6B31RXLqyAL8BA8JbISDRkqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شروط پکن برای سفر قالیباف به چین'
حسین مرعشی، دبیرکل "حزب کارگزاران سازندگی"، گفت: خیلی روشن به ما گفته‌اند که
۱- تنگه هرمز را باز می‌کنید
۲- عوارض نمی‌گیرید
۳- با عربستان سعودی مسئله‌تان را حل می‌کنید
۴-  با آمریکا مسئله‌تان را حل می‌کنید
بعد قالیباف به چین بیاید.
قالیباف در اردیبهشت سال جاری، با پیشنهاد مسعود پزشکیان و تایید رهبر جمهوری اسلامی به عنوان «نماینده ویژه ایران در امور چین» منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/78180" target="_blank">📅 04:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">منابع حکومتی:
روابط عمومی سپاه:
🔹
مردم شریف و انقلابی اردن؛ یکبار دیگر دست شیطان از آستین ارتش کودک‌کش آمریکا به درآمد و با بمباران وحشیانه به مراسم جشن عقد یک زوج جوان اهل تسنن در منطقه سیریک هرمزگان، عمق کینه خود را به امت اسلام به نمایش گذاشت.
🔹
ارتش تروریستی شکست خورده آمریکا که از رویارویی مستقیم با رزمندگان اسلام عاجز است، با استیصال مردم مظلوم را به خاک و خون کشید و مراسم جشن عقد پاک مردم را به عزا تبدیل کرد.
🔹
ارتش جنایتکار آمریکا که در آغاز تجاوز خود به ایران اسلامی ۱۶۸ کودک دانش آموز را در مدرسه میناب و ۲۱ کودک ورزشکار را در ورزشگاه لامرد به شهادت رسانده بود، شب گذشته در این حمله ناجوانمردانه حدود ۷۰ نفر از مهمانان این مراسم را مورد اصابت قرار داد که ۴ نفر از آنان از جمله یک کودک خردسال به شهادت رسیده و حال تعدادی از مجروحان وخیم هست.
🔹
در قصاص این جنایت، رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های بالستیک، آشیانه‌های هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ را در پایگاه هوایی آمریکا در اردن موسوم به پرنس حسن مورد حمله قراردادند که تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند.
🔹
همچنین چندین زیر ساخت فنی آنها به آتش کشیده شد.
🔹
مردم شریف و پاکدل اردن، اردن قدمگاه مقدس انبیاء الهی است، نباید جایگاه ولیدهای شیطان بماند. امروز با این جنایت های سبعانه، حجت بر همگان تمام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/78179" target="_blank">📅 02:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=bR6D9plhcGx76wDE2lHaez2ub477nbtMeUZr0nYY8W7jvy8K-Ai2CxaSReG5ghGrInkoGQXROa1GlInp0TaNOsRXaDsUXTGSuJL6ZYP8QtSULBvqtD9If8AdAQS9MnbMjSgCivU9IN2I-FtCNrTcicYb0LAZOQeQx8zKdkTrI2zvHmknxMyhrPPly5MgwmPL0B_wyMWYr9JkmGj9SAprLX564EmcVaWkYOnMMxTve7ejgv-2t7tpk6u0IrQpJa5EGE_nhpNXle7EXZhTlVlCGJjB9yRi3_WICIx34i3SGjh124Z6Hwch5rqH22Fw-7fmLQ9uEQF6wfBpHbazX83BTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=bR6D9plhcGx76wDE2lHaez2ub477nbtMeUZr0nYY8W7jvy8K-Ai2CxaSReG5ghGrInkoGQXROa1GlInp0TaNOsRXaDsUXTGSuJL6ZYP8QtSULBvqtD9If8AdAQS9MnbMjSgCivU9IN2I-FtCNrTcicYb0LAZOQeQx8zKdkTrI2zvHmknxMyhrPPly5MgwmPL0B_wyMWYr9JkmGj9SAprLX564EmcVaWkYOnMMxTve7ejgv-2t7tpk6u0IrQpJa5EGE_nhpNXle7EXZhTlVlCGJjB9yRi3_WICIx34i3SGjh124Z6Hwch5rqH22Fw-7fmLQ9uEQF6wfBpHbazX83BTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متنی که اکانت سنتکام به همراه ویدیوی بالا منتشر کرده، ترجمه ماشین:
سنتکام حملات به اهداف سپاه پاسداران در ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
نیروهای آمریکایی اهداف سپاه پاسداران انقلاب اسلامی را هدف قرار دادند که شامل مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، توانمندی‌های مین‌گذاری و مراکز ارتباطی بود.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتیرانی تجاری در تنگه هرمز و نیروهای نظامی آمریکایی انجام شد.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه مشغول فعالیت هستند و همچنان هوشیار، مرگبار و آماده‌اند تا به اجرای عملیات‌هایی که فرمانده کل قوا دستور می‌دهد، ادامه دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78178" target="_blank">📅 02:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/flyU9jOxeF7PIzPfBUEht3W_4iZLP_JrFYj7C-zaVBjVKRpz9Gb9kwWC2pngbqGNg0Yql-F_4vi5TofqFpvhR6MlXvMRd9xsQXJSbVZ24_DvN2DAddq73zIfpxb3qlephHJTDKUtsBEQotyD8RwnHxheSY4r7RKyrDGUGu7AMkc-qq1ze1OnS0TfwMW8sRZx23rVmamX1uT7rx1etvZH3Z5DhR03BhcRLQrJEEkaKbZahWnrVb2b39AeLTeeinQS2c8sNEPHngUjPxQBqY0Zamh_CUZ73zx8uNa2-B69Sxh9i4nzze1e8pRtmu4Vr1f3nRtlquXCZTEPJ4jddVLACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/km-oxEsx4hRYDIzZ29bUCoTseXP0jrznYDJ8jm4UyawVvjF7MhYqyVwV3ajMRPqgu37VGUcSC1wWI8oPHsWKmibXnStXoAc91HwwbqB9ZZIalGfCCBdxf7fRMwmgjO77bMn3nwu5jeJNqqQwyk8Iptlsc4AuIx5GcFwIi6O7ouDy7fhulLRQvzHE8jmYCm2T7LDpyQm2SIpIpO8PjbzVDLWqra1eCj8CgjFdzfH5abJsXSn2HbRHABd2Vu_4tI5pWb0b4LzepmIUDuGc67zrR3OdyoGztV5wUTHxevpdXAmaqYb368oSdAutE1o2MusTYDMhJwVFAe5W4g6BF3az2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">"ستاد کل ارتش کویت" در فاصله چند دقیقه دو اطلاعیه منتشر کرد که گویا دومی فقط یک کلمه بیشتر داره. ترجمه ماشین:
اولی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات پهپادهای متخاصم است.
KuwaitArmyGHQ
دومی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم است.
KuwaitArmyGHQ
ادامه متن:
"ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، این صداها ناشی از رهگیری اهداف متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی مراجع ذی‌صلاح را رعایت کنند."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78176" target="_blank">📅 01:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78175">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=vfS7ZOrxVIMgOQGtV6MQLzhYisAPS5Jei0I3xEFf3YW4KOiht7wcwQMuZuqswFA5OXvqnie3f0vbmsWu5EzHm5MPE3nHQ6hPvvBtKd0E26Dgw5NDn-lEsTfY7A1WD2Y3Oxv7aHX8-vs1HUsN5w8iFjL2B9qXvxJ3Y-18wWOr-6gKkFw4AaJfij-r32DBraT9Xz5sXZQi_8QQWBiMYQk0IkyGr64xGI2TKK0LX0qInrCPru-3wSOa12tGPU--szP0n3aHeDMXfrcCiM8OfYB9JZ0DrE-AoxuBRyCgOf2ZhjvEnUhoI4iOTLjm4bSISyao-8mRfmGEhRa8OKUuuFraQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=vfS7ZOrxVIMgOQGtV6MQLzhYisAPS5Jei0I3xEFf3YW4KOiht7wcwQMuZuqswFA5OXvqnie3f0vbmsWu5EzHm5MPE3nHQ6hPvvBtKd0E26Dgw5NDn-lEsTfY7A1WD2Y3Oxv7aHX8-vs1HUsN5w8iFjL2B9qXvxJ3Y-18wWOr-6gKkFw4AaJfij-r32DBraT9Xz5sXZQi_8QQWBiMYQk0IkyGr64xGI2TKK0LX0qInrCPru-3wSOa12tGPU--szP0n3aHeDMXfrcCiM8OfYB9JZ0DrE-AoxuBRyCgOf2ZhjvEnUhoI4iOTLjm4bSISyao-8mRfmGEhRa8OKUuuFraQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان ویدیوی دریافتی از شهرستانی در استان ایلام
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/78175" target="_blank">📅 01:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n6e2-4Waid05ITRQl_KWx_tFvXncluglGffMlTX8m6W3bfVg78pzJ_jR_YKzO7qqyiY1jsaJCSgh_ld2dscTfsh-bSFzatbEotDwrwvprM3ZjKCug9Ho8UWUwCgWX7hzy-ZR5e4-LC-7ANBG-C95iks7H2NJ88x3vVSo6PWFeo-7XC3O3SBThYIEw46Xp-ztJc5rJkAgq6bd3Rdl8S-B8CddPDYfkVJ2IivhZORifBiEDSsi5qNIY12F1C3wberBPJliQ9C4pWpUIDeHrTMm1IZs2xkHChuvdk1N7LIZ8a2ztiMCQudAZbocbxdxPBvb36wW5P5ZdAff3pNeu86pWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: صدور هشدار در کویت
ترجمه ماشین:
هشدار: خطر قریب‌الوقوع
............. تهدید امنیتی .............
همه موظف‌اند در مکان‌های امن بمانند و برای تضمین ایمنی عمومی، از پنجره‌ها و مکان‌های روباز و در معرض خطر فاصله بگیرند.
دفاع مدنی — وزارت کشور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78174" target="_blank">📅 01:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=I9Reld0W9FdLv09Oe43MwljUQbQgA_z3-5RsbE2RMrGfD8yk2PkvXHpGS0dQKNbrru_UHmdHr8CwSCA7m92iGU3st53vX35sHbVwVYeQwADVlBnZKlpAzMlS6cWjktOMpLw7EJ-fLzz98rjfOzFsHr1oFWUd0uFo9AAol4IhiLz67MHdV6_8mBaayng71YnP8bL-YPUTK_t6dIetyOnXkLRHcp3m_o8I3XMnLEj6v501FQELF1lO7RTZQvmdxa51sf5NJ6LGy61UQFZTL4u0jQF946dSCdQzvojcd4dCKJYgmn8aXJqpw-u3cD_OH7QSHaayKXjDe9p8PsPHnqzUYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=I9Reld0W9FdLv09Oe43MwljUQbQgA_z3-5RsbE2RMrGfD8yk2PkvXHpGS0dQKNbrru_UHmdHr8CwSCA7m92iGU3st53vX35sHbVwVYeQwADVlBnZKlpAzMlS6cWjktOMpLw7EJ-fLzz98rjfOzFsHr1oFWUd0uFo9AAol4IhiLz67MHdV6_8mBaayng71YnP8bL-YPUTK_t6dIetyOnXkLRHcp3m_o8I3XMnLEj6v501FQELF1lO7RTZQvmdxa51sf5NJ6LGy61UQFZTL4u0jQF946dSCdQzvojcd4dCKJYgmn8aXJqpw-u3cD_OH7QSHaayKXjDe9p8PsPHnqzUYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس راهور جمهوری اسلامی ایران:
یک دستگاه هیوندای با سرعت بالا با یک دستگاه چانگان در مسیر موازی برخورد کرده که در پی این برخورد تعادل خودرو بر هم خورده و با جمعیتی که در حمایت از نظام و نیروهای مسلح در حاشیه خیابان حضور داشتند، برخورد می‌کند
راننده حالت عادی نداشته و پس از برخورد با بشکه‌ها و علائم ترافیکی، با جمعیت برخورد می‌کند و در نتیجه این حادثه تعدادی از شهروندان فوت می‌کنند و برخی نیز مصدوم می شوند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78173" target="_blank">📅 01:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=kwWyd3BHnSb2QhvVru5B5wsANzPGGWCADyxvNPSfGCA9DB-BYxY9xsOEtFXpdHUXE_XPS3kmWgLXPCdAeSjv6iMCs2C8sUrgQ1qiW3JCcKIm4quGrxyOJicnNgqgULgkmxLAFl1n0S00uqaAw7Gwm04tCVqtuEoSB5rhNDm9XO4PqYNeUl4v06BJfhkcMNbPZvwpxkpERYxeSb8ROnl_nZcBcTixemiqBPYsjDcTIPXXedxkmRCpyvvAMLQZnjaUOGIH5cw8x9i8uSg7pLrjPoZaTww6TyiUngrWMmgv5saKH0xq4IY8qe8VUW3NDnjK2OG1-MLKvkFF5UG3MWVt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=kwWyd3BHnSb2QhvVru5B5wsANzPGGWCADyxvNPSfGCA9DB-BYxY9xsOEtFXpdHUXE_XPS3kmWgLXPCdAeSjv6iMCs2C8sUrgQ1qiW3JCcKIm4quGrxyOJicnNgqgULgkmxLAFl1n0S00uqaAw7Gwm04tCVqtuEoSB5rhNDm9XO4PqYNeUl4v06BJfhkcMNbPZvwpxkpERYxeSb8ROnl_nZcBcTixemiqBPYsjDcTIPXXedxkmRCpyvvAMLQZnjaUOGIH5cw8x9i8uSg7pLrjPoZaTww6TyiUngrWMmgv5saKH0xq4IY8qe8VUW3NDnjK2OG1-MLKvkFF5UG3MWVt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پیکر بی‌جان
ویدیوهای منتشر شده در منابع حکومتی: یکی در
#مشهد
با خودرو کوبیده به تجمع بسیجیان
سه‌شنبه ۱۰ شهریور
Vahid
دست‌کم چهار کشته در برخورد خودرو به تجمع‌کنندگان در مشهد
دقایقی پیش خبرگزاری‌های ایران گزارش دادند که راننده خودرویی که به میان تجمع‌کنندگان در بلوار وکیل‌آباد مشهد راند، بازداشت شده است.
خبرگزاری صداوسیما گفت که در این حادثه «۴ نفر کشته و بیش از ۱۰ نفر زخمی شده‌اند.»
پلیس راهنمایی و رانندگی مشهد گفت که یک ماشین «هیوندای جنسیس با سرعت بالا منحرف شده» و پس از آن به میان جمعیت برخورد کرده است.
گفته می‌شود این خودرو به «تجمع‌ شبانه حامیان حکومت ایران» برخورد کرده است.
هنوز علت این حادثه از سوی مقام‌های مشهد اعلام نشده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 471K · <a href="https://t.me/VahidOnline/78170" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lWqpQlCk7JVBdkxejxSVBxLeG_ACbwQwpf6aAQprWfLGwFLaUr6iOw_Cpegf_Nc0RGuzF-0p4c9vSJAdZM3HF5nEm8JA6YMeYrtpCP2WFs4cWEt5drJXh9cWFYvUPfh-j5OcefcmjkxoNRBAAJlHz7Yrwei6FY4JuNawMzvdfa8k-RsZupQLpF7FAfioHMyVRLXHsCBXQ7vpxBmTttJw0yWxO-m0xMyqTYSK3zt0s7-Fg0hB_bfc5lyQInI6bbDHn_WXw0B87Pm3NCyXGedDXaY39mSOsYY2_F7MBS4zPG09lLUAnbPQhNRM36-muaRszxqLRZqEtA8uaihaisTl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pzcdkqV2ODujTypuTcgMlx0Dd3Ac0HzDjO4JvtK-othdj0enO90L0jPR4ZYHzaZm8poxwu62tqaVx58OA2ttAPBNP7VSdPimU8vwFKJfJeeqEHsdk1NhytFTjrTPVs2TEqc4k3PP9z5lsWB67Kn0hLhuViRVJFS2OPdgOFvcK5K0_aQ6zsiA--w3bNgyWPIQrEIlL3DRu7qLl1u5K_u74PPtcnxT96cJ1xiWGbNnLHfkLC3FauG9rQlEseAyUI6wHXkMzVxhjlUXezFiwwcj1J43HegeyAg-7lg69JnZ7XYp9vt6i_Jt2Q-AzefAX9w410K1RUwZYrjUH9cQMsADcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت دکل مخابراتی کوهستک که در منطقه مسکونی واقع شده بود.
@iliaen</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/78168" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=VdB0i44L5QK90IZ2OQr9ywK719R-oysaWMhBeHxNFPSYH3UiFoZTuyGt2wyrNAH1cjNamyCV0Kw0g4wp0hDW6o7oPJSsf69gmEWhDD0cF_YfbhuWPVtUkAQAYTbDQytWoQ6Wztdf2-lhuw5XPYp0sa-rxrLOvKkmtT1YLhMH-iwJJ4NYqh0QtUtZo7Jbc4kD1xj3St-qaP9FwuRAXk9ATCnY2tVVd82o_zVcFBH7cpXyXSnXNtRNQuhK7r8qYBlSLp6KZ4aFSuz57J0KLl6by2X5J7B--stVFJ7nzyZiQ79w0EKuUk2F-VCHOQq7JdN2LM_lXbXT8OQRIXHfd6fcjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=VdB0i44L5QK90IZ2OQr9ywK719R-oysaWMhBeHxNFPSYH3UiFoZTuyGt2wyrNAH1cjNamyCV0Kw0g4wp0hDW6o7oPJSsf69gmEWhDD0cF_YfbhuWPVtUkAQAYTbDQytWoQ6Wztdf2-lhuw5XPYp0sa-rxrLOvKkmtT1YLhMH-iwJJ4NYqh0QtUtZo7Jbc4kD1xj3St-qaP9FwuRAXk9ATCnY2tVVd82o_zVcFBH7cpXyXSnXNtRNQuhK7r8qYBlSLp6KZ4aFSuz57J0KLl6by2X5J7B--stVFJ7nzyZiQ79w0EKuUk2F-VCHOQq7JdN2LM_lXbXT8OQRIXHfd6fcjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: '
در حمله به سیریک ۴ شهروند کشته و ۶۵ نفر زخمی شدند
'
ایران گفته است در حملات هوایی آمریکا به بندر کوهستک شهرستان سیریک، چهار نفر از جمله یک زن و یک کودک که در مراسم عروسی شرکت داشتند کشته و ۶۵ نفر مجروح شدند.
رئیس دانشگاه علوم پزشکی هرمزگان گفت دو نفر در محل کشته شدند و دو نفر در بیمارستان جان باختند و «شش نفر از مجروحان در بخش مراقبت‌های ویژه بستری‌ شده‌اند و ۲۶ نفر هم در بخش‌های جراحی تحت درمان قرار دارند.»
@
VahidHeadline
در همین رابطه یک منبع محلی به بی‌بی‌سی فارسی گفت به گمان او هدف حمله هوایی «یک دکل مخابراتی» که در فاصله «چند متری خانه محل برگزاری عروسی و آن طرف خیابان» قرار داشته بوده است.
@
VahidHeadline
در پیام‌هایی که من دریافت کرده بودم هم نوشته بودند هدف حمله یک
دکل مخابراتی
بوده و در اون حمله شهروندانی در خانه‌های اطراف، از جمله در یک
عروسی
، کشته یا زخمی شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/78167" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=WQcdExntDuftcn0HmjsBKOO8b8G663aYG-1QnIf5tbIawYNgzvc2THFQx0_9fua6oCApHVwWCq_9DOQES2dBXFariO4FTV7f_2YdOsd8XJWBxtKE0Qagumhms95qRgzNG7m9T4WP-iyFjgh_JYbOeoEhdfAC7barnxuw9YxwYEux0uMPkGul6r4FGTqG8TZYz1mpP5uVnIobfuQXubC8sLabSgK9y1Fm3bOvLNj838es2eGfEmIXl82Iq5TRuIHj-6AF0Kr79LZuqWvovaO3jgLXIB1cy2cYWgM38kjyGABZOutIFafpv9C6sJchepG8vbeNFmVSqtmkRln7n24eXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=WQcdExntDuftcn0HmjsBKOO8b8G663aYG-1QnIf5tbIawYNgzvc2THFQx0_9fua6oCApHVwWCq_9DOQES2dBXFariO4FTV7f_2YdOsd8XJWBxtKE0Qagumhms95qRgzNG7m9T4WP-iyFjgh_JYbOeoEhdfAC7barnxuw9YxwYEux0uMPkGul6r4FGTqG8TZYz1mpP5uVnIobfuQXubC8sLabSgK9y1Fm3bOvLNj838es2eGfEmIXl82Iq5TRuIHj-6AF0Kr79LZuqWvovaO3jgLXIB1cy2cYWgM38kjyGABZOutIFafpv9C6sJchepG8vbeNFmVSqtmkRln7n24eXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از بیدگنه
سلام همین الان از بیدگنه موشک زدن
سلام از فردیس موشک فرستادن
سلام وحیدجان
ساعت ۲۳:۱۳ از سمت جنوب مهرشهر کرج صدای بلند شدن موشک میاد.
سلام الان از بیدگنه موشک زدن
از کرج موشک زدن چندتا
از بیدگنه ملارد بود احتمالا
درود همین الان صدای بلند شدن موشک از فردیس کرج اومد
همین الا از ملارد بیدگنه موشک شلیک شد
همین الان از بیدگنه چندتا موشک شلیک کرد
سلام از ملارد موشک زدن ساعت ۱۱:۱۲
+ ده‌ها پیام مشابه دیگر از این منطقه پرجمعیت که نمی‌رسم بخونم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/78166" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پیام‌های دریافتی:
سلام همین الان از کرمانشاه موشک زدن ۱۱و۰۷ دقیقه
داداش کرمانشاه پردیس دقیقا همین الان صدا اومد
همین الان از کرمانشاه موشک پرتاب کردن
صدا انفجار شدید کرمانشاه الان
وحید همین الان از کرمانشاه موشک فرستادن ۲۳:۰۸
کرمانشاه الان موشک زدن
کرمانشاه صدا جنگنده میاد وحشتناک [صدای پرتاب موشک با جنگنده زیاد اشتباه گرفته میشن.]
10:08 کرمانشاه موشک رفت
همین الان از کرمانشاه موشک فرستاد ...
سلام وقت بخیر الان هم از کرمانشاه صدای شبیه پرتاب موشک اومد ۲۳:۱۰
کرمانشاه دارن موشک میزنن، هنوز ادامه داره ۲۳:۱۱
موج دوم موشک از کرمانشاه ۲۳.۱۲
آپدیت:
پیام‌های کرمانشاه تا پنج تا موشک ادامه داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78165" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام‌های دریافتی:
الان موشک از،یزد زدن
از یزد موشک زدن الان
سلام وحید جان
همین الان از یزد موشک بلند شد
همین الان از یزد موشک زدن
وحید یزد همین الان موشک بلند شد ازش
الان از یزد موشک پرتاب شد
🔄
همین الان دوتا دیگه
دو تا دیگه از یزد زدن
۲۳:۰۸ دوباره از
#یزد
موشک زدن.
۳ تا موشک دوباره یزد بلند شد
سومین موشک هم شلیک شد
ساعت 11:08 دوتا موشک دیگه از یزد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78164" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sB19iO8jYiqgat_iWXna0eczAm6rjOktsyZoDmjjPlOYwTXzyfp65LMonT0XNVQgCxgd2H1qB9j56Nk3KgVfdIBbvl1k14dJIdzTO45dhKPHGKMg8LKHejVCNfhBnPjaBVXqT9GsEKJ2yEiBrE3MvuPXQTyGhO5gJ-_7iYptbITyrISbBcpoLCOKFpZF1BqeHiD7jyuMi-zW8uAhjR7TtSDfLjXLUEeIkm7k4Wwk33U9YkfuS38KaOiwwwB0ahOvgd15Mb8RZnvEqp2oRLuNE6Ls4JUP92eRCvd1Tl0PBSg8zGTEfod8UIATX_jQbbJkNkNw8-PttWu1nBGsvwmWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SO0l89zGrGPAMx3_ATImJZZXQ2qHMSMXeASzHMXooB08kWCch9-8WGp-l1jbB0Mv_n8y7GIzkX8IgoygL9aXGODhivvyn8eskRKp_xZc5r5q32QSgMUKyfiJzc0MmoLDPf2Ejy5xjmu6VlLaW-2aNznO6hFXStxT9uWxkUHIcD-BsXjnhRBxgjwEHHt95L02by2R40g24j9YNA2XlyfTmr5lxIRQ1ky3kt8itmhLVJdNpOG3NUoH3zpn6UeYROCgjSEoZ4cGi_QM4xMuEUlI8FIb_rCx1gvjZ361n5aOuw1VytKkR2g4XKkMAJZUpk5nu-Tv9YdnxwWtwrs5_DoKow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=dB2m1Uvt-zmoIdaEuVlx7zh43oC_Rc3iTy-No-Z8gE-KlWkN18WDPX4VG3vBzugREbjB33m7uaUbX9HlHGyNfzGdgg1pMjxWqhFNjb7h3liyLhxN9pQHBidFlTeW-vssk3kZynU7XhKaJPjI_D_JWFTz5kCF4ouSmtUD5GmeTRW4eJh6s5upgjdIG-z130G-rwhDZHWnwktAdVuqgyXijg4jL17iDSlsfF_U8vKicL6sO76eC3uzPqO_Ru845J1dVmTRaCOppuzKwKCLV9hqqV6jkiePaRw1q9h0FuSNhcd19fhXzSK8iJdxcrzrU1RwdJHV_ifNduIvm_mjE5SNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=dB2m1Uvt-zmoIdaEuVlx7zh43oC_Rc3iTy-No-Z8gE-KlWkN18WDPX4VG3vBzugREbjB33m7uaUbX9HlHGyNfzGdgg1pMjxWqhFNjb7h3liyLhxN9pQHBidFlTeW-vssk3kZynU7XhKaJPjI_D_JWFTz5kCF4ouSmtUD5GmeTRW4eJh6s5upgjdIG-z130G-rwhDZHWnwktAdVuqgyXijg4jL17iDSlsfF_U8vKicL6sO76eC3uzPqO_Ru845J1dVmTRaCOppuzKwKCLV9hqqV6jkiePaRw1q9h0FuSNhcd19fhXzSK8iJdxcrzrU1RwdJHV_ifNduIvm_mjE5SNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی: سه موشک از
#خمین
پرتاب شد
تصویر دریافتی سوم از آسمان ازنا در لرستان
سه‌شنبه ۱۰ شهریور
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78160" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=oQkiREYVBUp1nUFtGMD2lqmM9-lCl0iAP1LKElDqnuN4Y_h-SapfzR27TGmAbeHOKdYzXp0k1wLdoFU9HExVE-qNg3EByZZqChHM-Y453DPkS3BB66DsYcFLsSBYAgPNjYcNkxBmXPgT-r6Gpb1lbWjlsKkgeTcs9kMFIy_FOy5p7WZJp1kVlsQ9wZL-Gw5JLyn03lh3s2kEWHaOgF-pw2TjhM3UIGILvOGscvEvMNcY6u5KDNuMgi2v7DB5NEUptHAc5gFM8yhjI1Y7BUmIS6cMv3Nh9I-R19UGznLXcYehPHjcrWn7DfIO20FUJzqrTVUPXLZXBDgBsZ-ILh_IeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=oQkiREYVBUp1nUFtGMD2lqmM9-lCl0iAP1LKElDqnuN4Y_h-SapfzR27TGmAbeHOKdYzXp0k1wLdoFU9HExVE-qNg3EByZZqChHM-Y453DPkS3BB66DsYcFLsSBYAgPNjYcNkxBmXPgT-r6Gpb1lbWjlsKkgeTcs9kMFIy_FOy5p7WZJp1kVlsQ9wZL-Gw5JLyn03lh3s2kEWHaOgF-pw2TjhM3UIGILvOGscvEvMNcY6u5KDNuMgi2v7DB5NEUptHAc5gFM8yhjI1Y7BUmIS6cMv3Nh9I-R19UGznLXcYehPHjcrWn7DfIO20FUJzqrTVUPXLZXBDgBsZ-ILh_IeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
خمین همین الان دوتا موشک زد
سومی رو هم زد
سه تا موشک از خمین زدن
سه صدای شلیک موشک از الیگودرز - احتمالا سمت خمین باشه
شلیک مجدد موشک از خمین، بیش از 3تا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78159" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پیام‌های دریافتی:
قشم دو انفجار شدید اطراف شهر
شد ۴بار پشت سر هم و شدید
ساعت ۲۲و ۲۸ دقیقه
۲۲.۲۹
دوتا انفجار بزرگ بندرعباس
سومین و چهارمین انفجار بندرعباس  ۲۲.۳۰
سلام قشم رو الان خیلی بد زدن
بندرعباس ۱۰:۲۹ سه تا صدا
چندتا صدای دیگه هم داره میاد
بندرعباس دو صدای انفجار
بندر دوباره دوتا انفجار
وحید شد ۴ تا
وحید جان بندرعباس مجدد 22:28 صدای سه تا انفجار از سمت ساحل اومد
ما خونمون بغل فرودگاس
شهرک صنعتی طولا قشم یا ناحیه سپاه چهارتا انفجار، صدای سوت موشک قبل از انفجار هم اومد
۲۲:۲۸
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78158" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ScqVRKbpSCZ0fWRogN-CJo1V07Agth7RCEyoyVUWzAZqvKEmcGSBXAWU0iiqtTj75badDvwumVUf5YlWe1CzSxHNcuatjwEkVgOvHms3hheO1SNhWvhu6MELC1LMK2ox0QqzDfT5vLIxTbvSkIuNAC7UDchfwf5X4H4G-s_1xISHcUgJtiwsIx8NBO49vwpIZ4AGWx7oMtySVNqTDolXlIZDOo3C1ZyS70zl0QJIuPLnGMbCk615jY-RETzyV2yHhqWaT6jboHO64n50cQ4oibnjq9pHlQTY6EuhN7W1NmH9FV1hSDmEXsWJXLlK05cjQihuYUpCDugVihwt20zXeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا، روز سه‌شنبه ۱۰ شهریور در گفت‌وگو با شبکه فاکس نیوز بازگشت به «تفاهم‌نامه اسلام‌آباد» را رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد».
ترامپ درباره پاسخ جمهوری اسلامی به حملات آمریکا گفت: «اگر آنها پاسخ بدهند، با شدت بسیار بیشتری هدف قرار خواهند گرفت.»
او حملات انجام‌شده را «بسیار بزرگ» توصیف کرد و افزود اگر درگیری برای سومین بار تشدید شود، ایران «به‌عنوان یک کشور به‌طور کامل از بین خواهد رفت».
رییس‌جمهور آمریکا گفت حملات اخیر، سامانه‌های راداری در جنوب‌غرب ایران و نزدیکی تنگه هرمز را هدف قرار داده‌اند؛ سامانه‌هایی که به گفته او ایران در حال بازسازی آنها بوده است.
ترامپ گفت نیروهای آمریکایی بخش قابل‌توجهی از شبکه راداری ایران را منهدم کرده‌اند و افزود: «آنها تلاش کردند رادارهایشان را دوباره بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریبا آماده شود و بعد آن را هدف قرار دادیم.»
او همچنین گفت ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» به‌طور کامل برای ادامه عملیات در صورت نیاز آماده است.
ترامپ بازگشت به «تفاهم‌نامه اسلام‌آباد» را نیز رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد». او افزود آمریکا فرصت‌های زیادی برای دستیابی به توافق در اختیار جمهوری اسلامی قرار داده است.
رییس‌جمهور آمریکا همچنین گفت متحدان واشنگتن در منطقه خلیج فارس پیش از حملات اخیر در جریان این عملیات قرار گرفته بودند و رهبران ایران درباره عزم او دچار «اشتباه خطرناکی» شده‌اند.
ترامپ در پایان سخنان خود درباره مقام‌های جمهوری اسلامی گفت: «آنها دست‌بردار نیستند؛ آنها دیوانه و احمق‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78157" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=en-Vxi0hbYTkCyFwokrI7KPfoa6msnvsZPZ7ST-Be9YW5j5tRrCbN1DTG2J8PgvA57CpbR6roSo8W5KyZ_qc8po8qfvgDEKZUZrkCHdJfnuFnJSEcWzjgSBFV9e4Suny-FnwnAqdccxphpp27B_l6QsToDVxkWxkOPG7hNm42V4EnrpFi0pAZQUC9_XdN7lho65IOn9QhWmumocyZAcAaiq1myzthq1NUhJwuqAOVw7zEVL2aV_UnofDeVPm27eQAjSpRMOStteYVKlQn7rotTauq2LPxMzW7QxJX0HhtoGNwO8FnJruXVR2Psr0AcFCnkE4CRu-kOu4EeD7eaVpdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=en-Vxi0hbYTkCyFwokrI7KPfoa6msnvsZPZ7ST-Be9YW5j5tRrCbN1DTG2J8PgvA57CpbR6roSo8W5KyZ_qc8po8qfvgDEKZUZrkCHdJfnuFnJSEcWzjgSBFV9e4Suny-FnwnAqdccxphpp27B_l6QsToDVxkWxkOPG7hNm42V4EnrpFi0pAZQUC9_XdN7lho65IOn9QhWmumocyZAcAaiq1myzthq1NUhJwuqAOVw7zEVL2aV_UnofDeVPm27eQAjSpRMOStteYVKlQn7rotTauq2LPxMzW7QxJX0HhtoGNwO8FnJruXVR2Psr0AcFCnkE4CRu-kOu4EeD7eaVpdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
پرزیدنت ترامپ به فاکس نیوز گفت که امشب شمار زیادی از رادارهای ایران هدف قرار گرفته‌اند.
پرزیدنت ترامپ گفت: «آن‌ها تلاش کردند رادارهایشان را بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و بعد آن را هدف قرار دادیم.»
رئیس‌جمهور گفت اگر ایران پاسخ دهد، «ضربات بسیار سخت‌تری خواهند خورد... اگر کار به بار سوم برسد، آن‌ها به‌عنوان یک کشور کاملاً نابود خواهند شد.»
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78156" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رسانه‌های وابسته به سپاه از آغاز حملات موشکی و پهپادی ایران به مواضع آمریکا خبر دادند
خبرگزاری فارس، وابسته به سپاه پاسداران، شامگاه سه‌شنبه ۱۰ شهریور به نقل از مشاهدات میدانی خبرنگاران خود از شلیک موشک‌ها و پهپادهای جمهوری اسلامی به سوی مواضع آمریکا خبر داد.
همزمان، خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت «عملیات قاطع نیروهای مسلح ایران» در پاسخ به حملات آمریکا آغاز شده و «پایگاه‌ها و منافع آمریکا در منطقه زیر ضرب موشک‌ها و پهپادهای ایران قرار می‌گیرند».
تاکنون مقام‌های آمریکایی درباره این حملات جمهوری اسلامی اظهار نظر نکرده‌اند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78155" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvYRzMLEXxeIaY9rAOg_2T5puHtO2h71Zu1PFZT5aeJ3fvOvzkFdVD__KOp-ibbK7mA8ToNB8MWzBeu9V6bdgcRhCEXrvVaJYHUUCeZtlQVvJ_COMn2CnUBktgdJYeTtipvG3XypqhbBuGey5jMAJuWGV_Y2iPNhe_BmD_3Qkf8dUo8d3B0LNz0fAvJVcsHK6zRyqQPRDd8d4VA3MgoUEtTHPs5PVJfx1K0Sq6KqI1BvHkuCBXJfK_G-vI4n4-zp456jUe2VgDccRV6R8_Vep656mH16pwt0q4ZanJaoH-4LyZL8Lt8f6F6x4mJ-2S74QPJOIryggBWAMwQRhcXmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با تری ینگست، خبرنگار فاکس‌نیوز و در پی آخرین حملات آمریکا به مواضع جمهوری اسلامی، هشداری صریح خطاب به تهران صادر کرد.
ترامپ با اشاره به پاسخ احتمالی ایران گفت: «اگر دست به تلافی بزنند، بسیار سخت‌تر هدف قرار خواهند گرفت؛ و اگر دوباره چنین کاری کنند، دیگر وجود خارجی نخواهند داشت.» او با انتقاد شدید از اقدامات تهران افزود: «آن‌ها دست برنمی‌دارند؛ رفتاری دیوانه‌وار و احمقانه دارند.»
رئیس‌جمهوری آمریکا در ادامه به جزئیات حملات اخیر اشاره کرد و گفت: «آن‌ها سعی داشتند رادارهای خود را بازسازی کنند چون هیچ دیدی نداشتند؛ ما صبر کردیم تا ساخت آن تقریبا تمام شود و سپس آن را زدیم.»
ترامپ همچنین با ابراز بی‌اعتمادی کامل به مسیر دیپلماسی با حکومت ایران تاکید کرد: «معتقدم توافق با آن‌ها حتی به اندازه کاغذی که روی آن نوشته می‌شود هم ارزش ندارد. ما شانس‌های زیادی به آن‌ها دادیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78154" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صداوسیما: فرودگاه جیرفت هدف حمله آمریکا قرار گرفت
خبرگزاری صداوسیمای جمهوری اسلامی شامگاه سه‌شنبه ۱۰ شهریور گزارش داد دقایقی پیش فرودگاه غیرنظامی جیرفت هدف حمله آمریکا قرار گرفته است.
این رسانه افزود اطلاعات تکمیلی درباره این حمله منتشر خواهد شد.
@
VahidOnLive
اسکندر پاسالار، فرماندار عسلویه، به خبرگزاری فارس، وابسته به سپاه پاسداران، گفت: «حوالی ساعت ۲۰:۱۰ شامگاه سه‌شنبه، صدای یک انفجار در شهرستان عسلویه گزارش شده است.»
فرماندار عسلویه گفت که از خسارات جانی و مالی این انفجار جزئیاتی مخابره نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78153" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78152" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=Pv8sBweWcsxuYuD5p7PmKb_rxEAlYXiECqsE4GzVSX1_3ENpKWWeAlYqvqad3rJnFyn3zPfer4LRFnoP0QWTdQYZbIsb-ZzRa1vBkK04hNI_JQLwgLzi6MSfWiuuRi5w5Kd5pDcsliUKU-kxIXP5oDIyLOV1jVWS4ufPNH4nqdFDBPP96DCtxnyPuy3j0S0X1KYcJOnz0IInP4hFU87sCftM3SZFDuGFGgnXLNjygud6STSYzTKXVAzmHlyTobHi1SuZ8vEl0jiQGbkX8qbA84LbQWn2IZMIUG-SUGUEmO_yuyeZWH4RIH3hClej-7yBgcBp3DGi72oR51BG2kcM0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=Pv8sBweWcsxuYuD5p7PmKb_rxEAlYXiECqsE4GzVSX1_3ENpKWWeAlYqvqad3rJnFyn3zPfer4LRFnoP0QWTdQYZbIsb-ZzRa1vBkK04hNI_JQLwgLzi6MSfWiuuRi5w5Kd5pDcsliUKU-kxIXP5oDIyLOV1jVWS4ufPNH4nqdFDBPP96DCtxnyPuy3j0S0X1KYcJOnz0IInP4hFU87sCftM3SZFDuGFGgnXLNjygud6STSYzTKXVAzmHlyTobHi1SuZ8vEl0jiQGbkX8qbA84LbQWn2IZMIUG-SUGUEmO_yuyeZWH4RIH3hClej-7yBgcBp3DGi72oR51BG2kcM0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های زیادی دریافت کردم که نوشتند حدود ساعت ۲۱:۲۵ از
#خمین
موشک شلیک شده ولی پرتاب موفق نبوده و برگشته.
ویدیوهای دریافتی: سه‌شنبه ۱۰ شهریور
Vahid
آپدیت:
منابع جمهوری اسلامی بعدا این ویدیوهای دریافتی رو با شرح هدف قرار گرفتن پهپاد آمریکایی منتشر کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78150" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیام‌های دریافتی:
صدا ۹:۰۵ بندرعباس
وحید بندرو دوباره زدن همین الان
صدای انفجار بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78149" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JQ_BuBQk4dEDgRsj-wcfhmTfnZ95WZyTEZyr5G5PD50ZDgZarUdSHWk6I9cgWWBBZhcUXUuiiBSGj1mwn3qrgdcUC9znDh_x_DIIqmfcJbnYKIuNUdpdflq55VIfbjA2_iFerui4OZMkZRtrjK7c6bk5q4Lhonc_kl37aYs7-mmDOZfaMwQrBHG8ZM4a95QwImeFfDn2NZJkiY7_0O_sPME35eKJbPt9L_Ca2iOWElD_ne9XlUc-bqOEHu_nnhWZB3cO57bGKN2-Uyx3elXLTjPSVSILcxSKNYU9zDLJDa3H5Je7WFunotfolCWgNVh_HSY3XTITQWHiBhv6GAxQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر ایران پاسخ دهد، حملات آمریکا شدیدتر و گسترده‌تر خواهد شد
ترجمه ماشین:
ایالات متحده همین حالا، در حالی که صحبت می‌کنیم، در حال حمله به اهدافی ایرانی در نزدیکی تنگه هرمز است.
این حملات گسترده و قدرتمند هستند و در تلافی تلاش نافرجام ایرانی‌ها برای افزودن مین‌های دریایی به تنگه انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (همه آن‌ها به‌طور کامل جمع‌آوری یا منفجر شده‌اند!)، و همچنین در تلافی شلیک هشت موشک از سوی ایرانی‌ها به پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه دست به تلافی بزند، بار دیگر و در سطحی بسیار شدیدتر و بالاتر مورد حمله قرار خواهد گرفت؛ اما آن هم بزرگ‌ترین حمله از همه نخواهد بود. آن حمله هنوز در انتظار است و وقتی به پایان برسد، چیز بسیار کمی از جمهوری اسلامی ایران باقی خواهد ماند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78148" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پیام‌های دریافتی:
سلام صدای چند انفجار اومد بندرعباس ۸٫۵۰
۸:۵۲ قشم یه انفجار حس شد
بندرعباس صدای 2 انفجار دیگه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78147" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq88LOPCJHCoQzuQrqh9qTqaeELm17vEOpIBHTvwz9E7q1qWIZjsPvPTPWj3WABC4Z7L-1wHcAvqZFSKhnGYYLRkj7pVSkpFegDSf7SXmJZBDo9mxCQfBONG06enzzr9Rp_-h_ARvpMUh3nRnS3S6wNz-0B5ZtZfbzjjmQJ5582o0bwdAR80OLeJgZUQijVPW3ap3AsWwTHUeL62D-qAyzptx-_rQKXCjQ06hS0PREPXW4y59GweHbDw4ZDKd0WeXG-rwblrF_LX23nufSWzHxl62Jd2foN9DGmssgOGgNeAuxkP05Zdyp9Fm3ASU-GgknqVxkMZNgWtmRuO54KAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۱۰ شهریور، در پی شروع دور جدید حملات ارتش آمریکا به مواضع نظامی در ایران، خبرگزاری آکسیوس این اقدام را صحه‌ای بر گزارش خود مبنی بر طرح آمریکا برای حملات مداوم و دوره‌ای به مواضعی در شهرهای حاشیه تنگه هرمز دانست.
پایگاه خبری آکسیوس به نقل از مقامات آمریکایی گزارش داد که دونالد ترامپ و مقامات ارشد دولت او در حال بررسی طرح‌هایی برای انجام حملات محدود در تنگه هرمز و مناطق اطراف آن هستند. هدف اصلی این حملات، جلوگیری از بازسازی سامانه‌های راداری، پدافند هوایی و توانمندی‌های موشکی ایران اعلام شده است.
به گفته آکسیوس این طرح که توسط فرماندهی مرکزی آمریکا (سنتکام) تدوین شده و مورد حمایت پیت هگست، وزیر جنگ قرار گرفته، به دنبال مهار تلاش‌های تازه ایران برای تهدید شناورها و نفت‌کش‌هاست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78146" target="_blank">📅 20:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSQ0Vpls9Hvftw5Udo8Z8avkxVmH-a3SDh2xf-1wASS8nscbX7OJ_qoRZGTBCvOFtIu0HCjiMQu95CpbKbPwtWb9_--J_urOIqf0YDIIX8mtpVAys6ZE5Oj1p-WtGmviEwkPxsk2zrmyvalgwN2chCJqWDzAyfZj0pq8Sc4Cw_JzCpbK6W3uQTxdGBG3Ta4qkgCb9Aod4Fr_sEjY_nJmemIxtMglTo-62a2-mmwpaHt83Q8dneAUYsaxLXcLuEQ1hh--_t2IELV_T-yGSXLLQPx6tIQWW4nnQKXLEi_q148d2cSYj8dO6yeJIVEKnvcKp-_ggk2XtXFpaBoOtqIs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سنتکام در این لحظه منتشر شد. چیزی که پیش‌تر در منابع دیگر پخش شد درست نیست:
امروز ساعت ۱۲ ظهر به وقت شرق آمریکا [ساعت ۱۹:۳۰ به وقت تهران]، نیروهای ایالات متحده حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران را آغاز کردند.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و نیروهای نظامی آمریکایی مستقر در منطقه انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78145" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EUfETm12qEd9D_EO1P9GPS4su4HCvqjtrJaItvGA1XN4z6H6VWe5ClVanlfcNvCDjQP6mIZ9gQhYS-38NrLz0poGsYHvUBfqD3ldpV_oKuzRtEGFutk59dOPfXEmNaEWSgT49bUIn2ClcNkW7PVrA4iK_3hF9fwiaKsKTLjYEkkuleU9MSYdGFckZL6VCi995typS6oTEHYw04yENszNfp99-Nhem3JuM5vuLt1YbctsW0XV3pP0pTMpjm6vt1g_0IIhlEfp8MyX9asYGtkCVb8kWJbRViFEpsGVbuKBwQaRwawJgyiojsgIkUvi3kRZShsdCigsSqUyyoJQ-mz5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیمای جمهوری اسلامی از شنیده شدن صدای چند انفجار در قشم در شامگاه سه‌شنبه خبر داد و نوشت: «دقایقی قبل صدای بیش از ۵ انفجار اطراف روستای مسن قشم شنیده شد.»
این خبرگزاری نوشت: «دقایقی پیش، صدای ۴ انفجار هم از سمت تنگه هرمز در قشم شنیده شد.»
رسانه‌های ایران از شنیده شدن صدای انفجار در بندرعباس، سیریک و چابهار نیز خبر داده‌اند.
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، می‌گوید تاکنون هیچ‌گونه اصابت یا حادثه‌ای در هرمزگان گزارش نشده است.
@
VahidOOnLine
علی خلیل‌آبادی، معاون امنیتی و انتظامی استاندار سیستان و بلوچستان، در گفت‌وگو با خبرگزاری دولتی ایرنا از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78144" target="_blank">📅 20:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78143">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی:
۱۹:۵۸  چهار انفجار پشت سر هم
بندرعباس ۷ انفجار شدید ۱۹:۵۷
دوباره زدن بندرعباس
صداهای پشت سر هم ولی این بار خیلی دور
7 صدای انفجار بندرعباس سمت شرق پشت سر هم ساعت نزدیک 8
سلام بندرعباس حدود 10 انفجار
7:57
صدای ۵ انفجار  (۳ انفجار پشت سر هم و ۲ انفجار جدا ) از فاصله دور جزیره قشم شنیده شد
ساعت ١٩:٥٧ دقیقه چندتا انفجار پشت سر هم شنیدم یندرعباس
شیش انفجار مجدد بندرعباس ساعت هفت پنجاه هفت دقیقه خیلیم شدید
7:57 بندرعباس 10 شهریور بالای 10 تا انفجار
بندرعباس ۱۹:۵۷
چهار پنج تا پشت سر هم زدن
دوباره زدن ، شاید هم صدای موشک از اینطرفه، صدا اینبار کمتر بود ولی تعدادش بیشتر بود
بندرعباس انفجار های پشت هم صداش قطع نمیشه
چقد زیاد ۷ تا انفجار توی ۱۰ ثانیه ساعت ۱۹.۵۸
دور از قشم
۱۹:۵۸  ۴ انفجار پشت سر هم
احتمالا بندرعباس
ولی از قشم به خوبی احساس میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78143" target="_blank">📅 19:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیام‌های دریافتی:
دوباره زدن بندرعباس
الان یه انفجتر دیگه بندر عباس از بقه بلند تر بود ساعت ۱۹:۴۵
یک انفجار شدید الان در بندرعباس
۱۹:۴۶ دوباره بندرعباس صدای ۲ انفجار متوالی
ما شرق بندرعباسیم، صدا ضعیف بود.
سلام دوباره همین الان قشم رو زدن دو مرتبه19:47
وحید جان صدای شدیدتر همین الان بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78142" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌های کمی از سیستان و بلوچستان:
19:34 کنارک انفجار اول
19:36 کنارک انفجار دوم
سلام وحید جان صدای انفجار چابهار همین الان
چابهار داره میزنه19:33
شیش هفت تا انفجار پشت سر هم
چابهار صدای پنج انفجار پنج دقیقه پیش
سلام وحید تو خونه ۶ تا شنیدیم شاید بیشتر بود
کنارک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78141" target="_blank">📅 19:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔽
#بندرعباس
پیام‌های دریافتی:
وحید جان سلام بندرعباس همین الان ۳ انفجار شدید
بندرعباس صدای ۳ انفجار ۱۹:۲۸
بندرعباس دو صدای انفجار
بندرعباس 3 انفجار همین الان
درود چهار صدای انفجار با موج انفجار بندرعباس ساعت ۱۹:۲۸
وحید بندر سه تا صدای انفجار اومد ۱۹:۲۹
بندر عباس 19:29
صدای ۴ انفجار سنگین
سلام، هم اکنون صدای دو انفجار در بندرعباس
درود وحید جان بخدا دیگه دارن میزنن بندرعباس الان دو تا انفجار محدوده فرودگاه ساعت ۱۹:۲۹ حالا یا زدن یا خوردن
سلام
۳تا صدای انفجار مانند الان بندر عباس اومد تو خونه حس کردیم نمی‌دونم چی بود دقیق
سلام بندرعباس الان با فاصله های چند ثانیه ای صدای ۴ تا انفجار اومد
صدای دوانفجار بزرگ بندرعباس ساعت هفت وبیست وپنج دقیقه شب
۱۹/۲۹ چند انفجار پشت هم قشم حس شد
احتمالا لارک، هرمز یا بندرعباسه
احتمال بیشتر لارک صدا از سمت جنوب بود
بندرعباس الان دوتا انفجار شدید
۱۹:۲۹ زدن
منطقه بهشت بندر صدا واضح بود
وحید جان سلام بندرعباس همین الان ۳ انفجار شدید
بندر رو زدن
وحید جان صدای دو انفجار سمت اسکله رجایی العان
دوبار ۲ تا دیگه
سمت قشم درگهان بود موج
درود وحید خان صدای 4 تا انفجار پشت سر هم بندرعباس از سمت بلوار شهید رجایی
خیلی شدید
درود وقت شما بخیر
ساعت هفت و بیست هفت بندر عباس صدای انفجار
قشم خیلی صدای انفجار میاد همین الان
شروع شد ۱۹.۲۹.  صدای ۴ تا انفجار دور از قشم
یکی دیگه دقیقه ۳۱ دور بود
سلام وحید جان قشم صدا و موج انفجار میشنویم
خیلی دوره ولی بزرگ احساس میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78140" target="_blank">📅 19:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db6862775f.mp4?token=NL51-njs8ZVTgmu4miZN6aKSurcl6GpIF49PTk3ibj2gtgwSvLvZC810y9d7ELWJeyS8Wm7eH7h09Wzkx-ByXeUwaURkNklO4vCeM9yqncNWPIusVoTvnI0f4S8-f2fAM2vlSXT1XJxWc8RnW94Ou9yrwSKv1TujhQCNt47NxrHrDbFJZ8WfFNuebzKMEfKwBAj145EJ66jGQ_NTAncG8Ob5kAwKOgUumQRuo0RdPgsli_53gRhkut2QmTRHGjsnJO0c0V0QjMXIa8jmf8_zzpaL7ANfrayf9PhMjRSIRhf06EGfj7TYE7jiqJOiZrEFoNa9OqCc6PSWKY7THitTuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db6862775f.mp4?token=NL51-njs8ZVTgmu4miZN6aKSurcl6GpIF49PTk3ibj2gtgwSvLvZC810y9d7ELWJeyS8Wm7eH7h09Wzkx-ByXeUwaURkNklO4vCeM9yqncNWPIusVoTvnI0f4S8-f2fAM2vlSXT1XJxWc8RnW94Ou9yrwSKv1TujhQCNt47NxrHrDbFJZ8WfFNuebzKMEfKwBAj145EJ66jGQ_NTAncG8Ob5kAwKOgUumQRuo0RdPgsli_53gRhkut2QmTRHGjsnJO0c0V0QjMXIa8jmf8_zzpaL7ANfrayf9PhMjRSIRhf06EGfj7TYE7jiqJOiZrEFoNa9OqCc6PSWKY7THitTuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام درفشان، وکیل، روز دوشنبه خبر داد که حکم اعدام موکل او،‌ علی‌اصغر پیغمبری، از معترضان دی‌ماه ۱۴۰۴، در دیوان عالی کشور تأیید شده است.  درفشان به سایت خبری امتداد گفت: «حکم اعدام علی‌اصغر پیغمبری پیشتر از سوی دادگاه انقلاب تهران و با استناد به قانون تشدید…</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78139" target="_blank">📅 18:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y76-LwMyw07cC2LJJLMxGfV5PWUJIlJRxkRHh_cgLLo8APgIQNe25DrEr5Q-Qqfc6SSar6N96A8Oud5TwJBE2gU2QGcLUGa1iJjW1vuMquvzkBGol7nJ6gC2_TDkdZnQOKczuAhvAwL0tIMoNRewWMXUdfTQ6ow2BrM3RCBtNdALvJ_49NrCdmKzgZo-MZ42Yxm0V0HQnQgGuwOjRbRalqVozCHTmVHIi6oyLst8r7FNqhGVn_4K5rvRCJdM_niWHlCoQPQSBMf2Ey_LHDuKVAHT1Ai5vTwe72W2l4GSIf6DuYWfIC8QsivcbyjgX4SyYSWdXdGlxSOGQ03Qk7oymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a23e113ac.mp4?token=rqUWt4GS57pjkf2MhdSEfS_dm-Nlpxn0IPEpNuTE43R7wD_a8VUsTMlg18wxn_f_pBxYXs4i2H6BbZy56CWuzNr8Q2JRZFhqKek8EtgKQ4ifk4GS0z7FiCdC6O1cT_15lp8vpUWkl9OWcFQPyAfmO1B4dJg2GJ4QBLj8-CUOU61ilUwnG3ceG5ZpZ_TdXq1KWzXaWc0nyMQhPhtIPrMdj9aoJDNJBU7eSb-SpIrDUhBFbHX8_fbThuum6pmVtkt6jCnMYsgiLcyuGFn6jTanpLoIiISoGhUUJxh9Dc7WFy0BJeDxMoPAXMxPn9s32FS7rV6XxSHIvqbBCVfy6Rdn1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a23e113ac.mp4?token=rqUWt4GS57pjkf2MhdSEfS_dm-Nlpxn0IPEpNuTE43R7wD_a8VUsTMlg18wxn_f_pBxYXs4i2H6BbZy56CWuzNr8Q2JRZFhqKek8EtgKQ4ifk4GS0z7FiCdC6O1cT_15lp8vpUWkl9OWcFQPyAfmO1B4dJg2GJ4QBLj8-CUOU61ilUwnG3ceG5ZpZ_TdXq1KWzXaWc0nyMQhPhtIPrMdj9aoJDNJBU7eSb-SpIrDUhBFbHX8_fbThuum6pmVtkt6jCnMYsgiLcyuGFn6jTanpLoIiISoGhUUJxh9Dc7WFy0BJeDxMoPAXMxPn9s32FS7rV6XxSHIvqbBCVfy6Rdn1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا گفت: «جهان از رژیم مطرود و یاغی ایران خسته شده است و ترامپ به‌جای مماشات با آن‌ها می‌خواهد یک‌بار برای همیشه به آن‌ها خاتمه دهد. مردم ایران این فرصت را دارند که به نظام جهانی برگردند، به‌جای اینکه سرکوب شوند.»
IranIntl
بسنت گفت: «ما سر مار ایرانی را زیر خاک کرده‌ایم. مار هنوز نمی‌داند که مرده است و بدنش کمی حرکت می‌کند، اما با غروب آفتاب از حرکت باز خواهد ایستاد. رژیم ایران نابود شده است و به‌زودی خودش هم این را متوجه خواهد شد.» او تاکید کرد دونالد ترامپ قصد دارد این پرونده را برای همیشه ببندد.
@
VahidOOnLine
اسکات بسنت گفت: «ایرانی‌ها تلاش می‌کنند از تنگه هرمز به عنوان یک گلوگاه استفاده کنند. این تنگه برای آمریکا گلوگاه نیست، اما برای بسیاری از کشورهای دیگر هست. این وضعیت تا دو سال دیگر دور زده خواهد شد. تا دو سال دیگر، تنگه هرمز به پهنه‌ای بی‌ارزش از آب تبدیل خواهد شد.»
بسنت گفت: «نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.»
@
VahidOnLive
وزیر خزانه‌داری آمریکا: در حال شناسایی و ردیابی دارایی‌های سپاه هستیم
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز سه‌شنبه ۱۰ شهریور در حاشیه نشست وزیران و مقام‌های ارشد مالی گروه ۲۰، از تشدید فشار اقتصادی واشنگتن بر ایران خبر داد و گفت آمریکا احتمالا این هفته یک بانک و هفته آینده یک بانک دیگر را تحریم خواهد کرد.
بسنت گفت: «احتمالا این هفته تحریم یک بانک را اعلام خواهیم کرد و هفته بعد نیز یکی دیگر را اعلام می‌کنیم.»
او افزود آمریکا در این زمینه با متحدان خود در حال گفت‌وگو است و از حمایت آنها برخوردار است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال بررسی تحریم شرکت‌های لیزینگ هواپیما و دیگر نهادهایی است که با سپاه پاسداران تجارت می‌کنند.
او گفت: «ممکن است این‌ها نهادهای مختلفی باشند. ممکن است شرکت‌های لیزینگ هواپیما باشند که آنها را بررسی خواهیم کرد. ممکن است هر کسی باشد که با سپاه پاسداران تجارت می‌کند. ما در حال شناسایی و ردیابی دارایی‌های سپاه هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78137" target="_blank">📅 18:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78136">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb5fccd6a2.mp4?token=erIXyy13COaqpbDCpDrPjzdP_enGqDHJMn77SVRZkQGPs7adT0VTMqDyUvclno3xDH1hZF5uz8j8F8A6e5UuYVqPbH-fd4iZIZ_JNOwTNrLjLaUxn3_KyfloAiOg3S662OZVHGJCAstYpMWJ5sOPTVB-PVBcqY510ynHzcXxa6JfxTlymD4ylxyyL9HxOGAb_SlGmfnj_kzb7JaQkrZzP6xHXBvMI2jyYMPjanb3hfC7h-kQcSO4DE9dQHOmMg-UqsCP4DbzdzZ0QSTIwq_p0p52BAkyM5X2hQ2KDtJqLoHUFjoFvPPQpoknyggR7ZspwrCyw4PtdpACzAzKKXovkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb5fccd6a2.mp4?token=erIXyy13COaqpbDCpDrPjzdP_enGqDHJMn77SVRZkQGPs7adT0VTMqDyUvclno3xDH1hZF5uz8j8F8A6e5UuYVqPbH-fd4iZIZ_JNOwTNrLjLaUxn3_KyfloAiOg3S662OZVHGJCAstYpMWJ5sOPTVB-PVBcqY510ynHzcXxa6JfxTlymD4ylxyyL9HxOGAb_SlGmfnj_kzb7JaQkrZzP6xHXBvMI2jyYMPjanb3hfC7h-kQcSO4DE9dQHOmMg-UqsCP4DbzdzZ0QSTIwq_p0p52BAkyM5X2hQ2KDtJqLoHUFjoFvPPQpoknyggR7ZspwrCyw4PtdpACzAzKKXovkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس شورای اسلامی، سه‌شنبه در پیامی ویدیویی با تاکید بر اینکه محاصره دریایی در قوانین بین‌المللی، یک اقدام نظامی محسوب می‌شود، گفت که اگر محاصره را تشدید کنند، حتما پاسخ نظامی می‌دهیم و همه ضرر خواهند کرد.
قالیباف گفت: «اگر دشمن اراده‌اش بر این باشد که ما از خلیج فارس نفت صادر نکنیم، هیچ‌کس نخواهد توانست نفت صادر کند.»
او گفت: «آمریکا می‌خواهد برخلاف تفاهم‌نامه از مسیر جنوبی تنگه هرمز عبور کند که این اجازه را نخواهیم داد.»
رییس مجلس افزود: «دشمن در حال حاضر در جنگ اقتصادی، بر روی جنبه روانی آن متمرکز شده است.»
قالیباف گفت که دشمن پس از «شکست در عرصه نظامی و دیپلماسی» سراغ جنگ اقتصادی و شناختی رفت و آن را به جنگ نظامی خود اضافه کرد.
قالیباف افزود: «هدف دشمن از جنگ ترکیبی این است که در داخل کشور، اغتشاش را به همراه ترور و حملات نظامی کوتاه آغاز کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/78136" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q5AbOtTv5MgimWRI2lVmrQkAh6IP75GztPhUNeR1l2JilLtkIZnw4Qz-g4xRGLgQTMOuR5T1ifNBX_WsSTXZh1OicdkNriOamXYqRUHyXzWr1cHIZe7qmNIY8hODK7NiZEz0UP5olbzp80gEtoxcuh1TRKQLzLvWUWkbG3lA9XU_0mUNoEykOOfaxfp0jj7pqr9_dTZKRDgdZB7Sb6DDMN1fnS2bN197LF--D1FxvPRNNAb0ZxOsR8_-g_Zh1N_4ahyTmhGQQXaK7rkL8eOYVONUuLRXirSKmV7NqyHObEwXP1QY4kkWRxeO1I3QjyVrk99RqPdwGJmMddZMVPQvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با انتشار اخباری از حضور «حجاب‌بان‌ها» در بازار تهران و سخنان برخی از مقام‌های جمهوری اسلامی در رابطه با لزوم «اجبار حجاب»، تصاویری از نصب بنرهایی در شهرهای مختلف ایران منتشر شده که در آن‌ها زنان به مجازات قضایی در صورت رعایت نکردن حجاب مورد نظر حکومت تهدید شده‌اند.
در این بنرها، به تبصره ماده ۶۳۸ قانون مجازات اسلامی استناد شده و آمده است: «حضور بانوان بدون حجاب شرعی در معابر و انظار عمومی جرم و دارای مجازات حبس است.»
در بنر نصب‌شده همچنین به مواد ۷ و ۹ قانون موسوم به «حمایت از آمران به معروف و ناهیان از منکر» اشاره شده است. در توضیح ماده ۷ نوشته شده افرادی که در برابر «امر به معروف و نهی از منکر» مانع ایجاد کنند، مشمول تخفیف یا تعلیق مجازات نمی‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78135" target="_blank">📅 18:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HgN9qmLfRuPDmUJLMDIKvAyovsnw2jtydfG8K1-902QHiVMfdv5MMWSOFx4_umhPX-eQRgkWQxN873AAMFHx2rkFqAxo4cIdW2bYJUk6N_nVAaDMxDXRxYOm1Sxnu77pwqyHYo9FaxhXvOsnteRMFJglZ8aqLZ3MwpIEGy28mUiOkUDzpwKg_r_2VC_oxP2yEIP9pvQwzjjoi3zloaQgYjNKBstS6g8CvohOSnY4O-DWmL8mIDbUxDJf8lHiudJ1Gvi3kl-uzDkMD7x4tiyWIAxu3sADzyeu7JbE0J2W-iUxrplpVLw16DYuO1yeOt3wFd1LhnlNJhOF7vZnZOurqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران به ۲۱۳ هزار و ۷۰۰ تومان و حواله دلار به ۲۱۸ هزار تومان رسید. هر پوند بریتانیا نیز با ۲۸۹ هزار تومان معامله شد.
رقم امروز چهارمین رکورد پیاپی در چهار روز کاری است. دلار روز شنبه با ۲۰۶ هزار و ۴۰۰ تومان بسته شد، یکشنبه به ۲۰۸ هزار و دوشنبه به ۲۱۰ هزار تومان رسید.
همزمان با ثبت رکوردهای جدید در بازار ارز، رئیس کل بانک مرکزی در سی‌وششمین همایش بانکداری اسلامی گفت ایران کمبود ارز ندارد و ادعای فروپاشی اقتصادی کذب است.
همتی در پاسخ به اظهارات مقام‌های آمریکایی درباره نبود دسترسی ایران به منابع مالی گفت: «این ادعاها به‌طور کامل بی‌اساس است. ذخایر مسدودنشده، منابع پایدار و درآمدهای نفتی و غیرنفتی متعددی در دسترس بانک مرکزی قرار دارد.»
او افزود بانک مرکزی هفته گذشته ۵۰۰ میلیون دلار به بازار تخصیص داد و اکنون آمادگی دارد در صورت نیاز تا سقف دو میلیارد دلار ارز تزریق کند.
اظهارات امروز همتی با موضع پیشین او فاصله دارد. او هفته گذشته در گفت‌وگوی تلویزیونی گفته بود: «درآمد ما از فروش نفت صفر شده؛ یک واقعیتی است که نفت صادر نمی‌کنیم.»
چرخش لحن پس از پیام مجتبی خامنه‌ای، رهبر جمهوری اسلامی، به مناسبت هفته دولت رخ داد. او در آن پیام گفت گاهی بیان صادقانه ضعف‌ها کمک به دشمن است و بر ضرورت «تبیین و روایت قدرت و قوت ایران» تأکید کرد.
رهبر جمهوری اسلامی در همان پیام اعلام کرد: «قاطعانه اعلام می‌کنم که ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/78134" target="_blank">📅 18:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/scLJRgKb_JGhSYx0FR-XccRXfLPS1idVBI_XaSLmbaXzltJKJL3iu1Drxi0evsnZ4nYJK-GHG89fwekeJ6i8axsFoPeq4F5-1sKF8MoopQXvlS9HncLh9_43_CH4Vz2vaEReyD2TB1OAPszw7ERr17nUFrYe66_nHC0dCEAZziojgofoGJ__C4glAJuY3vamG9E3ye0os-DsGv3xUgLFusm9gboTW3oR8uTxA-jvFDnL1u3qAYJO9qPwCD6en6Qf_6NG8uoZ-NwnTuR3iRRxSHaE5O05D6sVpA5j7iADD0zYbQmAbaqzL7BeJIZUtwSry6nsGuw6Wim3_yp1_UIzaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت‌های‌ ناظر بر کشتیرانی جهانی می‌گویند دو ابرنفتکش حامل نفت عربستان سعودی اواخر روز دوشنبه نهم شهریور هنگام عبور از تنگه هرمز به فاصله چند دقیقه از یکدیگر هدف اصابت پرتابه‌های ناشناس قرار گرفتند.
به گزارش خبرگزاری رویترز، شرکت یونانی امنیت دریایی «ماریسکس» روز سه‌شنبه دهم شهریور اعلام کرد که ابرنفتکش «سیدر» حامل نفت خام عربستان سعودی با پرچم همین کشور حدود ۱۶ مایل دریایی در شمال شرقی خصب، عمان، ساعت ۱۹:۵۲ دوشنبه به وقت گرینویچ مورد اصابت پرتابه‌های ناشناس قرار گرفت.
شرکت امنیت دریایی وانگارد تک هم گفته است نفتکش «سنگال پراسپریتی» با پرچم لیبریا دقایقی بعد در حدود ۱۷ مایل دریایی در شرق خصب مورد اصابت سه پرتابه ناشناس قرار گرفت.
پیشتر سازمان عملیات تجارت دریایی بریتانیا از حمله به این نفتکش خبر داده و گفته بود سه پرتابه به آن هنگام خروج از تنگه هرمز برخورد کرده است.
بر اساس گزارش‌ها، خدمه این دو نفتکش سالم هستند و هر دو به فاصله کوتاهی از یکدیگر متوقف شده‌اند.
داده‌های شرکت کپلر نشان می‌دهد که هر یک از این نفتکش‌ها هفته گذشته ۲ میلیون بشکه نفت خام عربستان سعودی را از بندر جعیمه در خلیج فارس بارگیری کرده بودند.
با تشدید دوبارهٔ درگیری ایران و آمریکا، قیمت برنت روز دوشنبه نزدیک به سه درصد افزایش یافت و به ۹۰ دلار و ۴۹ سنت رسید و روز سه‌شنبه نیز با ادامه روند صعودی به حدود ۹۱ دلار و ۱۵ سنت در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/78133" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c0rgw7Fz-hkDTMdt4vQbcmRpeu-gevupruuM86N32ClbFRCE1h59N28kM_meA5oET-HevDWyMcpyhYgEsTUyOqsG1JANag4ahh6pgwOHQJpowRXHpmbkgulSyFfrAlU-C1RD-xWdlBv4Zypr_Yr8v0TrS9BVHTYeW-DJfDbyvOKPFW0X23f7XJeOTRCQxR5cUri0vZgv54Oj1cWUi03FYuLiB1JOWpdUyTjOgQ-yt7fJ7JGD6UpoLdQayriLKIR2Prq2e76Pe3BvrKoPTJW0njF6vk7Jg57kxT6w4llPbK52V8UNmzjaPsPiv8uTjiGIt-1JR380t1-mnt4yDu6fsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران، از ساکنان اسرائیل خواست به کشورهای خود بازگردند و «به‌سرعت فرار کنند». او گفت با کسانی که بمانند، مانند بنی‌قریظه رفتار خواهد شد.
نقدی گفت: «آنها باید بدانند رفتاری که نیروهای اسلام پس از رسیدن به آنجا در پیش خواهند گرفت، همان رفتاری خواهد بود که با بنی‌قریظه شد.»
او افزود: «پس باید به‌سرعت فرار کنند و هر کس بماند، بر اساس شیوه‌ای که با بنی‌قریظه رفتار شد و مطابق حکم تورات، نه بر اساس رحمت اسلامی، با او رفتار خواهد شد.»
بنی‌قریظه یکی از قبایل یهودی ساکن مدینه در دوره محمد، پیامبر مسلمانان، بود. بر اساس روایت‌های تاریخی اسلامی، پس از نبرد خندق و تسلیم بنی‌قریظه، مردان این قبیله کشته و زنان و کودکان به اسارت گرفته شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/78132" target="_blank">📅 18:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TH6l47kp9HSejLTcPhI-L_8DFc2ZjJUXgfJdkaqdgQbTfPilpjvYxCtd3ZUirdL5FsoEm0Kqmk1QpxguDhg3NnHGzv7wFoHi8o9W_6Y4YhrmvtSW10CMC_r8Hnl04VOxcAUoFi9LwJrgahLjKHV84R1Uj0TYhEUehsBTqFcwxE65278Qk_zZkdAePoOR8uD3FrLDWJ1HMX8d_ldQ3LyiqdzOpA6fmutJ6likikuITkFmiGJ5MwK43k2HpzelLQycaLyz7Qc24zHLCmR5digfiGDOvwBp3CxihIt5IU_hBCbAm8Ur1apWD5D2nxfmAtpJuHhqGQeSSVWyUg2qW8ibNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BKJGtMYfXE5BzJWtR8gFPbohDSSK339jAPs-yjfX9iJH5U9rGtww5YTqeTx1XU_5HjnCNCNdkByiA9gvGur01ga4KSjc7nuXEyyon2yIAk5x0cX_m7b2wws21zmyPjgoM_LFO1IfDrudENAZtxisqxTMrxG2ZdUVGwO3ERqJ95SlWecqf5cPe3UXvcEhUQNkOEsYqmodXOFWmfGBS5ywH9vW-8DU-nDxR8DwRiv-83KkJ3QzTOV-SdmvSjiwYbEm73t6odVgSn79KSpTru4uPFHWYd8AU_eegqB2cWbHfpP7_kPCx2Bt3MJsGIgqXG9UvcLp3JFhwMHWiR_y_p1qpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«کانون صنفی استادان دانشگاهی ایران» هشدار داده است اگر قانون ترمیم حقوق اعضای هیئت علمی تا پایان شهریور ۱۴۰۵ به‌طور کامل اجرا نشود، از استادان خواهد خواست فعالیت‌های دانشگاهی خود را از ابتدای مهر تعلیق کنند.
این کانون در بیانیه‌ای اعلام کرده است تعلیق فعالیت‌ها، حوزه‌های آموزشی، پژوهشی، اجرایی و مشاوره‌ای را شامل می‌شود و تا زمان اجرای «کامل و بی‌قیدوشرط» قانون ادامه خواهد یافت.
کانون صنفی استادان، سازمان برنامه‌وبودجه و رییس آن را به «مانع‌تراشی‌های سلیقه‌ای و خارج از عرف» متهم کرده و گفته است مکاتبه، مذاکره و رایزنی با مقام‌های مسئول نیز تاکنون به نتیجه نرسیده است.
این تشکل صنفی همچنین هشدار داده است ادامه بی‌توجهی به وضعیت معیشتی دانشگاهیان می‌تواند به افزایش مهاجرت نخبگان، کاهش بهره‌وری علمی و واردشدن آسیب‌های جبران‌ناپذیر به سرمایه انسانی کشور منجر شود.
مصوبه اصلاح حقوق اعضای هیئت علمی روز ۱۸ اسفند ۱۴۰۴ در شورای حقوق و دستمزد تصویب شد و قرار بود از ابتدای سال ۱۴۰۵ اجرا شود. این مصوبه، تغییر فرمول محاسبه حقوق و اصلاح ضر‌ایب مبنای پرداخت به اعضای هیئت علمی را در بر می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/78130" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/802f97efe1.mp4?token=YFQjiv5EscNYPLeuy856SpGam73B_mab23p4exbNKygH7ANob_41JJeH48Y6aF6Wlhs722URnnGciPHTAygxzqi__e4TR0GdVJWUveXV85QiuKX7jHxtb_d0exRdybrCRU0Tq0ieySe-k9CPEPktTe__GiEhd_cJmMO7cJJB-5NwV1ZA7E5Ird9rpJef0lbV9jYLlWVicNwGPwevZ0VYi1SrlMlHJSoUViHWOcq3tMLpqCVXmlfWkWXu54moh0Ovwz2oiZJOupthze513T6v0qFZyikDpj8H-4nOOTYVQz2aRN5gXIq1-jXNNBHIg5N_yaYUXeJcP4j3L8FHAjB36g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/802f97efe1.mp4?token=YFQjiv5EscNYPLeuy856SpGam73B_mab23p4exbNKygH7ANob_41JJeH48Y6aF6Wlhs722URnnGciPHTAygxzqi__e4TR0GdVJWUveXV85QiuKX7jHxtb_d0exRdybrCRU0Tq0ieySe-k9CPEPktTe__GiEhd_cJmMO7cJJB-5NwV1ZA7E5Ird9rpJef0lbV9jYLlWVicNwGPwevZ0VYi1SrlMlHJSoUViHWOcq3tMLpqCVXmlfWkWXu54moh0Ovwz2oiZJOupthze513T6v0qFZyikDpj8H-4nOOTYVQz2aRN5gXIq1-jXNNBHIg5N_yaYUXeJcP4j3L8FHAjB36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، روز سه‌شنبه ۱۰ شهریور در دیدار با ولادیمیر پوتین، رئیس‌جمهوری روسیه اعلام کرد که اگر ایالات متحده آمریکا به تفاهم‌نامه اسلام‌آباد برگردد، تهران نیز آماده است که به مفاد آن عمل کند.
پزشکیان، در این دیدار که در حاشیه نشست سران سازمان همکاری شانگهای برگزار شد، حضور ایران در سازمان‌هایی چون شانگهای و بریکس را تلاشی برای مقابله با «یک‌جانبه‌گرایی» آمریکا توصیف کرد.
پزشکیان در ادامه با تاکید بر تفاهم ایران و روسیه در زمینه ضرورت چندجانبه‌سازی در سیاست و اقتصاد جهانی، ابراز امیدواری کرد که این فرآیند به شکلی موفق پیش برود.
@
VahidOOnLine
مسعود پزشکیان، رییس دولت جمهوری اسلامی، در دیدار با ولادیمیر پوتین، رییس‌جمهور روسیه، گفت: «از موضع روسیه درباره جنگ و تحریم‌ها تشکر می‌کنیم. می‌توانیم در برابر یک‌جانبه‌گرایی آمریکا مقاومت کنیم. آمریکا حق ندارد تحریم اعمال کند و قوانین بین‌المللی را نقض کند.»
پزشکیان گفت: «حمله آمریکا هیچ توجیه منطقی نداشت.»
@
VahidOnLive
ولادیمیر پوتین، گفت مسکو از هر فرصتی برای دیدار، گفتگو و انجام رایزنی با تهران استفاده می‌کند.
پوتین با ابراز خرسندی از دیدار دوباره با پزشکیان گفت روابط دوستانه روسیه و ایران در همه زمینه‌ها به‌طور باثبات در حال توسعه است و این روابط مطابق با «متن و روح پیمان مشارکت جامع راهبردی» میان دو کشور پیش می‌رود.
@
VahidOOnLine
عباس عراقچی در پایان روز نخست نشست سران شانگهای در قرقیزستان گفت: «یکی از موضوعات مطرح‌شده در تمامی دیدارها، تفاهم‌نامه اسلام‌آباد بود.»
عباس عراقچی گفت «آمریکا باید به تعهدات خود بازگردد و به مفاد یادداشت تفاهم پایبند باشد؛ پس از آن می‌توانیم از این وضعیت خارج شویم چون همه کشورها دغدغه دارند که جنگ هرچه سریع‌تر خاتمه پیدا کند.»
مسعود پزشکیان امروز در حاشیه نشست شانگهای با رهبران هند، پاکستان و آذربایجان به طور جداگانه دیدار کرد.
شی جین‌پینگ، رئیس‌جمهور چین، ولادیمیر پوتین، رئیس‌جمهور روسیه، مسعود پزشکیان و بیش از ۱۲ رهبر دیگر امروز در قرقیزستان گرد هم آمده‌اند تا در نشست دو روزه سازمان همکاری شانگهای شرکت کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/78128" target="_blank">📅 18:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78127">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i1az6HltkQTtytfjFeepgJlVJyy0cawDp4w5Z_5Bzfr8E0dB_aV1RMZCnvLy3nVf5U2W7MkLE_kZtrLYJ4STjKze6fdsofalHutYUCNE6-MTg-jEbvMOFhh2P6GM8V5OwthsUgmu4YS7akOMI0qLMQcJUECiuflTK5pRGyaoNk6XhFjmjcl0j8MuAmHgLGxAhJvcyS2ZmdF1bRQLX9pqTm7mMiYfMtzm7I_d97xYivk6EP96YUoPDUbP2qvz5hUkPDCaxP--7zOcidZIivbzSMLqyEsEHdh4XBOUkeS2XZijsUc6vTN5auEsWG3zxvwhOEuKhHJ0aFNLmgAYVydH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر بختیاری، پدر پویا بختیاری از جان‌باختگان اعتراضات آبان ۱۳۹۸، از سوی شعبه اول دادگاه انقلاب بندرعباس در مجموع به ۱۰ سال حبس تعزیری دیگر محکوم شده است.
براساس حکم صادرشده، او با اتهام «فعالیت تبلیغی علیه نظام جمهوری اسلامی از طریق هم‌سویی رسانه‌ای با معاندان» به یک سال حبس، با اتهام «تحریک مردم به جنگ و کشتار با یکدیگر به قصد برهم‌زدن امنیت کشور» به چهار سال حبس و با اتهام «ارسال فیلم به شبکه‌های مجازی بیگانه برخلاف امنیت ملی» به پنج سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/78127" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78123">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OX4WgcHA19caz5Xbx66AWtIdHl6DjL_QRYsfzWR7lR9g9OWSTSpiSxUH8aoDY7gbCPjywajzhsPgn_aWZoQ1lRKC7IC-HCMN4lt8YwVHUUD7rYq9pIv1xRbUCEglEXN2_s7Ne5VDUcK4oiRdIfc5O97fGpvbU2Zbvz1BphjZCds6aLAnstXoyoj3GTHLdxBxlttI8S8BOwg_0w2urlXjAewiYOaEvwrbkuket6NKAfcdbpZrdKpBFcuuIt06rEMsEbbdUiMmpt9f47Q8fyN8Zx3TgsdzNhoLKF5xc0TxJ0Bkxokbskm_MLaEhfFhnpim0KFkt2lggVIVKzLPcni9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d499b7a4.mp4?token=fTgh98v9TfjwxCnxOVGK14OjuOF8kPrub_wmHkFpllPPX5FukcfhMflwlvG_AazTO1lQZ6a-RHtsEnvXx1EncZLycBr19NTh9pgdhfllsd62Wi1560lk3vpUKjb5M3HCp4dTqgpsJzzZp3ZxiMyo_keegp-T_BKkOjcEiCbvFCzUMb2mlaEoEiyoLK5p5R1sTQNj1s4uE3wHOE2PhfYuCfNQ6zpTJXuabycH6yEvTU1eg8VF7o9yLe4kMxy7W3U5V43xtXtrUPPFeMz_QXoMcixkcu_7sqUbG6tHPQXX-nsco2A4q_wB86yEtncx9D1QS-idSVUXSUJZ-jBLSyoS-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d499b7a4.mp4?token=fTgh98v9TfjwxCnxOVGK14OjuOF8kPrub_wmHkFpllPPX5FukcfhMflwlvG_AazTO1lQZ6a-RHtsEnvXx1EncZLycBr19NTh9pgdhfllsd62Wi1560lk3vpUKjb5M3HCp4dTqgpsJzzZp3ZxiMyo_keegp-T_BKkOjcEiCbvFCzUMb2mlaEoEiyoLK5p5R1sTQNj1s4uE3wHOE2PhfYuCfNQ6zpTJXuabycH6yEvTU1eg8VF7o9yLe4kMxy7W3U5V43xtXtrUPPFeMz_QXoMcixkcu_7sqUbG6tHPQXX-nsco2A4q_wB86yEtncx9D1QS-idSVUXSUJZ-jBLSyoS-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.
بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی از بابت اتهام «افساد فی‌الارض از طریق اقدام گسترده در انجام فعالیت‌های سیاسی، ایجاد انعکاس خسارت تصنعی، تهیه اخبار کذب، تبلیغ علیه نظام، برهم زدن امنیت و ورود و خروج غیرمجاز به کشور» صادر شده است. حکم مذکور در تاریخ 1شهریورماه ۱۴۰۵ به وی ابلاغ شده است.
آقای زارعی دوزدره‌سی که پیش از این در آلمان به سر می‌برد، در تاریخ ۸ اردیبهشت‌ماه ۱۴۰۵، پس از ورود به ایران توسط مأموران اداره اطلاعات بازداشت شد.
پرونده وی در مرحله تحقیقات مقدماتی در شعبه سوم بازپرسی دادسرای ناحیه ۳۳ تهران، موسوم به دادسرای امنیت، مورد رسیدگی قرار گرفت.
وی نهایتا در تاریخ ۹ تیرماه همان سال به زندان قزلحصار کرج منتقل شد. این زندانی در حال حاضر در واحد سه، بند ۳۷ این زندان نگهداری می‌شود.
علی زارعی دوزدره‌سی، حدودا ۲۷ ساله و ساکن تهران در جریان اعتراضات سراسری سال ۱۴۰۱ یکی از چشمانش با شلیک گلوله ساچمه ای آسیب دیده بود. وی پیش از این نیز سابقه بازداشت و برخورد قضایی را داشته است.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78123" target="_blank">📅 17:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYU1A-cvyGURTGAIwdcMPycHrkU3joPzbKi_iJxTrSR1ILpAPv3Ln0-4O5wOtCjstHzNV_XGx-X3lKpmzwD78imU3Bcv1IfacHUU3EM6Mg5QaXORTupyS6kAJCAyBQrbtOe82iZx86_WpSy5aZwT2z6kv2Nq5VLr8JjMDAZl8BXmkcnkLIZokKaYqjZ9yo62zavci4kcUTTMGgXHWQotClXs8P7RQ3NUZgL3ZCEQqy4Z1kc1xKSUl14KeEKimmCFDNlrkBL-b5dQ0TFlW_JYfc2plNv96qCkYDKmGPi_XlYo9X9v-w1Pc4_afpwvZxX4Kba0Ih9zlskdKmoIIQfqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک نفتکش در تنگه هرمز «هدف قرار گرفته است.»
براساس این گزارش، این نفتکش «هنگام عبور از تنگه هرمز و خروج از آن» هدف قرار گرفته است.
سازمان عملیات تجارت دریایی بریتانیا گفته این حادثه در فاصله ۳۱ کیلومتری شرق منطقه خصب عمان، «هدف اصابت سه پرتابه ناشناس قرار گرفته است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78122" target="_blank">📅 03:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78121">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78121" target="_blank">📅 00:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78120">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V2jYfNTx30pCgJqGeKFZN0Iv-DEIC9CHJZwSUHi4bz2_GrCqcNyjXR7jNI4QpF8BDskikQIbCPVnV7eGXzTZQyCEpxt4KEGeGYnwbp3qQmhjipNLYKojAfWmzNWTsMumxCaRs-3uJbdv5aD9QOsNUh4fKZSH9fvhlLjtx_togvDCaNxgClwUWSJ7cUEDdhiJKa4nDa0DPsbj-CiqhnJ-pn4fl3hKCUX4IkDsB3U0lNZT63Umj-sCk6H797vYOKWFCJTicS2TowdcBIHK25RJsJ2GHdo2deUcDjypaA6zHU2kyB5qjl7_Wo4klHn8NHar2SWXzUFUY_g4xEmf0oGC0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از سه مقام آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهور آمریکا، و مشاوران ارشدش در حال بررسی انجام حملات محدود در تنگه هرمز برای جلوگیری از بازسازی توانمندی‌های راداری و موشکی جمهوری اسلامی جهت حمله به کشتی‌ها هستند.
بر اساس این گزارش، این طرح که طی هفته گذشته توسط فرماندهی مرکزی آمریکا تهیه و از سوی وزیر جنگ، پیت هگست، حمایت شده بود، پیش از تبادل آتش این آخر هفته با ایران به تایید ترامپ نرسیده بود. اما او ممکن است پس از تشدید جدید تنش‌ها با آن موافقت کند.
یکی از مقامات آمریکایی گفت ایده اصلی این طرح، کاهش خطر حملات تهران به نفتکش‌ها، شناورهای نیروی دریایی آمریکا و هواپیماهای نیروی هوایی آمریکا است؛ به گفته این مقام، هدف «کوتاه کردن چمن» است.
یکی از مقامات کاخ سفید گفت: «رییس‌جمهور همه گزینه‌ها را در اختیار دارد. ایرانی‌ها می‌خواهند توافق کنند، اما همیشه یک روز دیر و یک دلار کم می‌آورند.»
ترامپ عصر دوشنبه به فاکس‌نیوز گفت که آمریکا به حملات جمهوری پاسخ خواهد داد و «آنها را به‌شدت هدف قرار خواهد داد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78120" target="_blank">📅 22:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78119">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l_wm9YvB_VognqF_ep9BxhNL7vpQNC_ZPUtehh4GyUVQOAThSARshAIGP7STsTIT2bDz8O4r73KWUo-1Pf2HRqZR3OhiroajWvp3nOu0a8NrWkYCcjcgFuflwB_fuyY-9zOtxc-3lxm99wApx-0ZC_M_1r32wapq1Y4qYDmrpuiOi7045RLvOUG9UrfRRSyHxb1ohtAKMxyCWoio3jU4VJ4a99tauieUOOQe4LVaYH7XidDfRK9Kt2dPG1O9B7bVCCgV2075BcML4TkTWBBTIRN7ObS_BxGngUAVpOTe-XmDRxMUycUZqv1W51H-n792LgFwIyR0SNGQrzx5KgQYRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستادکل نیروهای مسلح جمهوری اسلامی روز دوشنبه در بیانیه‌ای مدعی شد که ایالات متحده از آسمان یا خاک برخی کشورهای خاورمیانه برای استفاده از ایران استفاده می‌کند و هشدار داد آنها را هدف قرار خواهد داد.
این بیانیه ساعاتی بعد از آن منتشر شد که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرد ارتش این کشور به حمله شب گذشته ایران به نیروهای آمریکایی در اردن، ایران را به شدت هدف حملات انتقام‌جویانه قرار خواهد داد.
ستادکل نیروهای مسلح ایران در بیانیه خود گفته است «ضمن احترام به حاکمیت ملی همسایگان»، در صورت ادامه حملات آمریکا، نیروهای نظامی جمهوری اسلامی «پاسخی سنگین‌تر» از حملات شب گذشته خواهد داد.
ارتش آمریکا اعلام کرد شامگاه یکشنبه «نیروهای مین‌گذار سپاه» در جزیره لارک را هدف قرار داده است. در پی این حمله، سپاه پاسداران از حمله موشکی به دو پایگاه نظامی در اردن خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78119" target="_blank">📅 22:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TgzoPo2DyfSl_3tQT6d1AXMn5kd71OkqWMyWnoWM8I6IBCq9zK9MBFnw5u9Nuy-QKogARLhpidLT0P-IZzSFCIu3NRJZ27JR0vICHMOrX1K_g8z_Bdexk628MByd5rmrxooTObSrYfRIO3B-GwDL6Lt0yfaydRyt2uQ6gNMI7YTMR_V9jDtCA8eLBUrszfv9wKBmcOKFCIEXeJ2vNfZJ4jW2H_G_PTXdZ42PKd22D2qvbTO8xvk5BeJxTwE5dQfuBUy21xMqdNvlrEF0yB6Ar0ia-_0eTMlDZ4j-_QzMB6vVTqcyRJUm7aeCaW33AjT2Pk__tc6J_xabd2etTAeoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه عربستان سعودی روز دوشنبه نهم شهریور در بیانیه‌ای اعلام کرد که کشور‌های عربستان سعودی، ترکیه و پاکستان توافق کرده‌اند در قالب «پیمان دفاعی مشترک مکه»، دبیرخانه‌ای را در عربستان سعودی تاسیس کنند.
بر اساس این بیانیه، ریاست این دبیرخانه در سه سال نخست بر عهده دبیرکلی از کشور پاکستان خواهد بود.
در همین راستا، وزارت امور خارجه ترکیه نیز اعلام کرد که تنظیم سازوکارهایی برای پیوستن سایر کشورها به این پیمان، در دست بررسی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78118" target="_blank">📅 19:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=Fofos43nj8BpwCKBiRw_g9WDGssRj-GxNE7kqbKy3iAYMPBk0_EZOSngZNMaxlGHUi1oF4vpCd2wyBwgZgUFgYwhmkLTCTRxblVICfgLIDGGDL92LDbzJZElL6syt_iKNTMPC4tpAvStfES4NVqijcc0aqyPzZR6K_2AOKv4SyO0fFCSgWscZWvDhapG1gtq8AtVVtmkaBMes5h5BiVSP2RAM-SiuDYZ5Dqa0XdIakTjrLwMx_J2SxCXJrVULotQmf4TjQDCDgHe4Ul4bE_ulJNVw2lKk6v-1Bp5p1CLG9wJ83NLUPlodfIJlbtWKxhPw-D7hlTO41yBTukDGimQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=Fofos43nj8BpwCKBiRw_g9WDGssRj-GxNE7kqbKy3iAYMPBk0_EZOSngZNMaxlGHUi1oF4vpCd2wyBwgZgUFgYwhmkLTCTRxblVICfgLIDGGDL92LDbzJZElL6syt_iKNTMPC4tpAvStfES4NVqijcc0aqyPzZR6K_2AOKv4SyO0fFCSgWscZWvDhapG1gtq8AtVVtmkaBMes5h5BiVSP2RAM-SiuDYZ5Dqa0XdIakTjrLwMx_J2SxCXJrVULotQmf4TjQDCDgHe4Ul4bE_ulJNVw2lKk6v-1Bp5p1CLG9wJ83NLUPlodfIJlbtWKxhPw-D7hlTO41yBTukDGimQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا ویدیوهایی ساخته شده با هوش مصنوعی را از حمله و انفجار در جزیره خارگ ایران در تروث سوشال منتشر کرد.  ترامپ نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!»  این ویدیو ساعاتی پس از حمله سنتکام به دو پرتابگر موشک در جزیره لارک منتشر…</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78117" target="_blank">📅 19:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=VkWT1xU-Sm1MYhLlQFQ1tSyv5f4m4Q8Wv4Bv4Zf1KwTyuPnQzaZPoolu3sCUfcso3TN7Kqx3vlZXZ0mI6Z90_0Cm_UczHUnLmmbkEcO-qG1oSV9nWusYQu-lD4PIkcjY8tTGZQFYrxOb39k-PkOkVh0Vw07zgSGtT9qrKfFrXVBqQXQIzSOKMaNnNMzrgnAe3ITTd2OH39F8ROLzK-LPAORKuVUWp1IBYXMx5l9rUdCqUmQtw03m1S8UdMMCI-hac_Aa4EiVeOoezb6Hp0GvDWtgUNFq1-qMUFPjQYWMDXK_SesGJZZac4susuhhssQGFJbqrFUNx5VKIViIHc7cAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=VkWT1xU-Sm1MYhLlQFQ1tSyv5f4m4Q8Wv4Bv4Zf1KwTyuPnQzaZPoolu3sCUfcso3TN7Kqx3vlZXZ0mI6Z90_0Cm_UczHUnLmmbkEcO-qG1oSV9nWusYQu-lD4PIkcjY8tTGZQFYrxOb39k-PkOkVh0Vw07zgSGtT9qrKfFrXVBqQXQIzSOKMaNnNMzrgnAe3ITTd2OH39F8ROLzK-LPAORKuVUWp1IBYXMx5l9rUdCqUmQtw03m1S8UdMMCI-hac_Aa4EiVeOoezb6Hp0GvDWtgUNFq1-qMUFPjQYWMDXK_SesGJZZac4susuhhssQGFJbqrFUNx5VKIViIHc7cAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه نهم شهریور ماه در حاشیه نشست «جی ۲۰» در اشویل آمریکا گفت واشنگتن به اعمال فشار اقتصادی بر تهران ادامه خواهد داد و ممکن است نتایج این فشار طی هفته‌ها یا ماه‌های آینده نمایان شود.
بسنت در پاسخ به پرسشی درباره زمان احتمالی فروپاشی اقتصاد ایران گفت: « مسئله این است که ما محاصره را داریم و به اعمال فشار ادامه خواهیم داد. ما همین حالا گفتگوهای بسیار خوبی در اینجا داشته‌ایم و فکر می‌کنم این می‌تواند طی هفته‌ها یا ماه‌ها رخ دهد.»
وزیر خزانه‌داری آمریکا افزود: «اقتصاد لزوما نباید فروبپاشد؛ فقط باید حکومت ایران به خود بیاید.»
این مقام آمریکایی افزود بسنت در حاشیه نشست گروه ۲۰ با همتایان خود دیدار خواهد کرد و برای افزایش فشار اقتصادی و منزوی کردن ایران تلاش خواهد کرد.
اسکات بسنت، در ادامه با اشاره به حمله ایران به پایگاه‌های نظامی آمریکا در اردن گفت: «به نظرم آنها به‌صورت نظامی دست به واکنش می‌زنند، چون از نظر اقتصادی در حال شکست خوردن هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78116" target="_blank">📅 19:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=BGQvSBiGLuX9LrlZHAhutw9balgsQ_1e3-37UHYAtx8h--PokGnseuC1mIRXFtmhuLretVpjdGHaxD0IB4b4UCeGbddvnH3TjaIP0y_23t55mG7bPrXlnzu511Uoua7vi52uw01BJ-cQfUGxP_M_C4dfUNu1jO8xDB9UCJnEd8sWbkt6LfllrS9pdMl7Yg37D4_bXCz6kqrYI8PSsN_mOyM2eG6FACyuUBQQ1sNmsSnQf1jg-4oRv4QEmYbY5kPamiFFmWlu4qsKzc6UTbD9tv_VtjOKIQQiphx5Ac9ShtQhmzoF6h6IOG5Wva1SlZWPGLfLKSlpJfbXQ4Abybw21w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=BGQvSBiGLuX9LrlZHAhutw9balgsQ_1e3-37UHYAtx8h--PokGnseuC1mIRXFtmhuLretVpjdGHaxD0IB4b4UCeGbddvnH3TjaIP0y_23t55mG7bPrXlnzu511Uoua7vi52uw01BJ-cQfUGxP_M_C4dfUNu1jO8xDB9UCJnEd8sWbkt6LfllrS9pdMl7Yg37D4_bXCz6kqrYI8PSsN_mOyM2eG6FACyuUBQQ1sNmsSnQf1jg-4oRv4QEmYbY5kPamiFFmWlu4qsKzc6UTbD9tv_VtjOKIQQiphx5Ac9ShtQhmzoF6h6IOG5Wva1SlZWPGLfLKSlpJfbXQ4Abybw21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز دوشنبه ۹ شهریور ۱۴۰۵، شماری از شهروندان جویای کار در شهرستان گچساران در اعتراض به روند استخدام نیرو در پالایشگاه لیشتر تجمع کردند.
در ویدیوی منتشرشده از این تجمع، تیراندازی نیروهای انتظامی برای متفرق‌کردن معترضان دیده می‌شود. برخی گزارش‌ها نیز از زخمی‌شدن یک نفر در جریان این تیراندازی حکایت دارد.
این تجمع در اعتراض به نحوه جذب و استخدام نیرو در پالایشگاه لیشتر برگزار شده است؛ پالایشگاهی که به‌تازگی افتتاح شده است.
@
VahidHeadline
نیروهای امنیتی و پلیس، جوانان عرب معترض به بیکاری در مقابل شرکت نیشکر «دعبل خزاعی» در اهواز را با ضرب‌وشتم و تیراندازی متفرق کرده‌اند.
در این ویدیو، مردی که در حال فیلم‌برداری است می‌گوید: «این جوانان همه گرسنه هستند، هیچ‌کس ما را استخدام نمی‌کند. هیچ‌کس برای ما ارزش نمی‌گذارد. هر کدام از آن‌ها با اسلحه کلاشینکوف به‌دنبال جوانان افتادند. ما کار می‌خواهیم. جوانان گرسنه هستند. ما هیچ آهی در بساط نداریم. ما کار می‌خواهیم.»
سازمان حقوق‌بشر «کارون» روز دوشنبه نهم‌شهریور۱۴۰۵ در گزارشی نوشته است که «جوانان و خانواده‌های معترض که به نمایندگی از ساکنان همجوار این شرکت دست به تجمع زده بودند، با طرح مطالبات خود اعلام کرده‌اند که شرکت نیشکر دعبل خزاعی در زمینی به مساحت حدود ۱۲ هزار هکتار فعالیت می‌کند که بخش قابل‌توجهی از این اراضی متعلق به منطقه و مردم بومی آن است. با این وجود و علی‌رغم حضور جوانان بومی دارای مدارک تحصیلی و تخصص‌های مختلف، مدیریت شرکت اولویت را به جذب نیروهای غیربومی داده و باعث شده تا جوانان منطقه همچنان از فرصت‌های اولیه اشتغال محروم بمانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78114" target="_blank">📅 19:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GB3auQU2oGoYfse3hSZZ0VyniGdB42U5hEUpsFzGlTXmcuZjdvRQ7cSiuB3oOuo6X3Ks9wiPoB93ynVrH8Vs_td-Z2OI3MJmZeStz74iK30dSJmxBz9b-_1qspm6FSXmIdaixVcuUMUlO7PKHL8Lm7YCCqVX99CL0r8b2dlcfrLtX_XJc9ZTf8J2VHDBRRruCh0TKrFgoWCfvLmZJhXuxZPitnbXGhI8LLyNfkl0-6BYxFwBgbuhXPR-q3Y8StzKv89Q26YspLW0umFlM4bS9utJDonIpYBmAqwzrty6wyXasxJ9XMCKOJheybU0YxP2fLXeimYtULTHf4gd5fPZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EQWDieuOtOHgmUQovXTKid8tjO6gAxDWniBNXplK8AnFSjjOcsQnfj19LoPhKY9EtDLx9uCofct5_V0jE2H45Xrc2aLf29NYlnTd8XVspPuIQR8BVo01s6NpxzuOskqfXj16HVOTVx8y-Hx-9jL6QJ5pHxOEYxyXoEjBmmbuIrqKvSgVzAs7eX12a-3VIBqcnMQTWBkAtpJhnA2sqLjv94mm5OEuFfKuq8-KQCZkAXG4WLTWdzMxwyoKG5BRVj6kIcq6jfgeRsE0KiXjj5aTZMD0AxUAIiKTBtm77bq1CxPfnk-Nk6pgqkyGpos4MExAKtYjardzT26EVwVSfa0vNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اژه‌ای معترضان را به برخورد قاطع‌تر تهدید کرد
در پی تشدید بحران اقتصادی و رسیدن دلار آمریکا به مرز ۲۱۰ هزار تومان، رئیس قوه قضائیه جمهوری اسلامی گفت این نهاد برای مجازات «عناصری که بخواهند امنیت کشور را مخدوش کنند، قاطع‌تر از همیشه است».
این تهدید پس از آن صورت گرفته است که دستگاه‌های حکومتی بروز اعتراضات مردمی را پیش‌بینی کردند.
غلامحسین محسنی اژه‌ای افزود تحکیم امنیت و مقابله قاطع با عناصر ضدامنیتی از مقولاتی است که مردم و مسئولان درباره آن اتفاق‌نظر دارند.
این رویکرد با پیام مکتوب مجتبی خامنه‌ای در هفته دولت تشدید شده است.
خامنه‌ای در این پیام اعلام کرد: «قاطعانه اعلام می‌کنم که ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است.»
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با انتشار گزارشی به حضور «شماری از دانشجویان زن بدون حجاب اجباری» در جلسه رییس سازمان امور دانشجویان و مشاور وزیر علوم اعتراض کرد و خواستار «واکنش قاطع و فوری» وزارت علوم و واکنش نهادهای امنیتی و دستگاه‌های قضایی شد.
به نوشته فارس، انتشار تصاویر جلسه‌ای با حضور رییس سازمان امور دانشجویان، مشاور وزیر علوم و شماری از اعضای شوراهای صنفی دانشگاه‌ها که در آن تعدادی از دانشجویان زن بدون حجاب اجباری حضور داشتند، «با اعتراض گروهی از استادان و دانشجویان» مواجه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78112" target="_blank">📅 17:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78111">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bfFqkSn48km9cSPf3HVmXZ7Six9BzJ0u8JnIiilllBoinl_Rrd2JRUVAvrJOh4nTBO0fo4U8SfX3dLXZlwoh4LhhwHmWDROyJYFF1hlmZVB10QQlRmcpWmWOefU5_nbtpu5m2-1BDo9RsjM38GTy1qXzJR9h8qcECHsFrAxAtl3DEnGZWoj-UohAFJo7ABscuCeW7-afTznyCvJHJsYs6FXKXvEoMTZlXC-ZK70ikF5vLVhDYao_JFt0KVR7yF7bTSxWNHaBeJYR88Ldak99dkDzjVcXQs5W-u_2LkxIiPUS8Uf_S7v-0xQhwPgoWktLkV9M1cmfHfxkzNtPogyCtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا روز دوشنبه اعلام کرد که به همکاری با ایالات متحده و سایر شرکای بین‌المللی و گروه هفت «برای حفظ فشار بر ایران و کمک به کاهش تنش و ثبات منطقه‌ای» ادامه خواهد داد.
در این بیانیه آمده است:‌ «اتحادیه اروپا از تلاش‌ها برای اطمینان از اینکه ایران فعالیت‌های بی‌ثبات‌کننده خود را متوقف کند و با حسن نیت در مذاکرات صلح شرکت کند، از جمله از طریق فشار اقتصادی بیشتر، شامل عملیات طرد اقتصادی به رهبری ایالات متحده، استقبال می‌کند.»
«عملیات طرد اقتصادی» عنوانی است که مقام‌های دولت آمریکا بر برنامه فشار اقتصادی تازه بر جمهوری اسلامی گذاشته‌اند.
بیانیه اتحادیه اروپا در آستانه آغاز نشست گروه ۲۰ به میزبانی آمریکا صادر شده است.
اسکات بسنت، وزیر خزانه‌داری آمریکا به خبرگزاری رویترز گفته است در این نشست از وزیران دارایی و روسای بانک‌های مرکزی کشورهای جهان خواهد خواست تا روابط اقتصادی‌شان را با ایران قطع کنند؛ در غیر این صورت با تحریم‌های ثانویه آمریکا روبه‌رو خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78111" target="_blank">📅 17:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ambpTOhzMU4eQyIuJ1Rj0jyeElEZaiYzfEDFfeO49RAOfJLZ0UCpR28T8JuhJJ7VJH_zVqSQbLCuJolwbyI_KD0zMqar5oY6My0reGXgBsrqmSql6cK6xrskxewwxNGhXrYPAE7rtY-k-8gk3kN2i0joFTa2cZ8QzavjLCVz1VF-zI6Wsz9SWzHFhzmq2GnSfxiATHcBldbu4YAb9ylBlZQX5QjsFIbjx2LJHXZKiV2UJ4nW4tn-9kOMwUg8k9mSjQuNxVSVA6iUDf3mv0ZSQJNUWZoJq4SizfrWXbME9NbvbktKO-UofRWM84N5o_C9c3gK0vn7teLBk4Dchy9_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روند نزولی ارزش پول ملی در ایران، قیمت دلار آمریکا دوشنبه، نهم شهریور از ۲۱۰ هزار تومان عبور کرد.
همزمان پوند بریتانیا از ۲۸۴ هزار تومان عبور کرد و یورو نیز به مرز ۲۴۳ هزار تومان رسید. قیمت هر سکه طلای طرح جدید، موسوم به «امامی» نیز از ۲۲۳ میلیون تومان فراتر رفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78110" target="_blank">📅 17:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QYyufKkz8D1Qh1Gni-q0PoG6XUjOx9PJIXFJpGvo0fuqqWpoV6qyMkFuGWr8QcUjz-hnIdjJlF6fRGkhPas3P7UKtalreXBj67kVMd4YSUtyhCTlSfW6dxt9fNy5dRLZfUFjHAsYzfp2P2hrXIXjymJjHlMt7qwzBo03IxlVbFNi-yTYdAN1kVE54JHX77nA2iiJiy2ox5Mb53OVrjtnxSb4ggN42qZ0N2kQFIoD-k_G-1forJzpzlvknxlOsJ3w7oMMiZA0k6GXOxn1OdmiiuB5oYvNcB1ZNUiMi21iEUal4WvBsJbOPVqWYD4qAfha2PnUTLYFeSzE5WqtErC0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام:
🚫
ادعا:
سپاه پاسداران انقلاب اسلامی ایران (IRGC) ادعا می‌کند که یک ابرنفتکش هنگام عبور از مسیر جنوبی تنگه هرمز با دو مین برخورد کرده و کاملاً متوقف شده است. این ادعا
نادرست است.
✅
واقعیت:
هیچ کشتی‌ای در تنگه هرمز با مین برخورد نکرده است. این نیز یکی دیگر از تلاش‌های سپاه پاسداران برای ارعاب کشتیرانی تجاری منطقه از طریق انتشار اطلاعات نادرست است.
CENTCOM
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78109" target="_blank">📅 16:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78108" target="_blank">📅 16:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dWnh3Hsuo9xqPuUdSNSD2ArK1JBiTX-8KeB5ISZaPVCJ72goIn3ResGJ1BdoGYQtawsUD8yuD8CMYdf0w-FQF4K3ndIScLmiHQ2OV6kUXrLsqR_B924oAw9IUTHgZgt4uVfMSr7jnatKcLqa59vZ7Ams0j8SFxftRpJhXv7dqLB1QAKfQ2I1UwmZ93u1AWMrdXJzEo71p9wHBde7kYjjNs1X5TED1jgOhe9XqONJec3rhkARPrGWE-vn7aIM9OCSe-pcUspZ3xlgN1hl_n2yxwqdunwsBBrp-p7YGuxc9fPaydptbtAoUjgYu26xARGSxOJsAkeDK0Hp8r2Y9vMSRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه نهم شهریور، در شبکه اجتماعی «تروث سوشال»، جمهوری اسلامی ایران را رسما یک «کشور شکست‌خورده» خواند و خواستار محاکمه بین‌المللی رهبران آن شد.
ترامپ وضعیت ساختارهای اقتصادی و نظامی ایران را «فروپاشی کامل» توصیف کرد و نوشت: «ایران دیگر نه نیروی دریایی دارد و نه نیروی هوایی؛ ارز آن‌ها از دست رفته، حقوق سربازان و نیروهای پلیس پرداخت نمی‌شود و تورم به ۳۰۰ درصد رسیده است. رهبری آن‌ها در آشفتگی مطلق است و توانایی اداره کشور را ندارد.»
رئیس‌جمهوری آمریکا در ادامه با متهم کردن تهران به سرکوب خونین اعتراضات داخلی افزود: «تنها کاری که آن‌ها بلدند کشتار معترضان خود است که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است. مقامات تهران باید به اتهام ارتکاب جنایات جنگی علیه بشریت محاکمه شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78107" target="_blank">📅 16:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78106">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CRjzV5ebCEWOQPIDbtdoRNtTZoTjjg6YOlzbmmqWAAl6eLSA033COG7H1WAdt1TTupzol25-TNcI4T11HPIogEAwRAeoGxlGjqFFVpJ9s7_6D264xSj0_IGcNcG0aD3t8OUisqSgAdq1u3x6G9q45DuFZVSSAnp8qLA_TyGrTvwIEL_BNjjlJAsWCl-cpA2bgfM4lneAiqKDOktIvuY0vurdBk5-YuIqKYU3BAYr9jV2mCxofpw968fxNCjpBSRnLRvFEjUeD-iLeyVJy9-gaMpSFl_ZML6r5RdltY1TxgiZYbKUrbKQ4OrQefW5TA4VdDP7gUkEB-ndCvSpK0xUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی:
نتانیاهو در عبری آشکارا پُز می‌دهد که دولت آمریکا را فریب داده و به جنگ با ایران، به نیابت از اسرائیل، کشانده است.
نتانیاهو صراحتاً با خنده می‌گوید که چگونه با ۱۰۰۰ ساعت حضور در شبکه‌های تلویزیونی آمریکا، بر آمریکا «تأثیر گذاشته» است.
اما به انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78106" target="_blank">📅 16:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0006ca2103.mp4?token=h5ygv-CkCSgDXoeLX-Ml-QJ47qBL-wZmPCFZ58uzmqUe0BvRp57QWTQFj0-M3WLCpGpglpA-Ff4RLnoS2-cz653c4MbT9-daz5GHyaTKD5-36X5UC3GM6K-kY4SRgvAL1-Uqcz7ParX6EwbRUIbrK1HlnhGQ03mm7d9noB1p_br0kmdqG8fs5oFocbfImGnEhhcOoVlBGfAe7kjaQJNZGRn3Ww2ZDzVuTTCa76r6spLzwd7B5ea-H0XP-pVi4yWLJKhPoL5sZYJ-gKEWHh2BBpH19aZNU_W0w_7YU9WoWFnko6EwzsybnHS3l7eLFvuX2AeWVTXKid9LaWbMZnsFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0006ca2103.mp4?token=h5ygv-CkCSgDXoeLX-Ml-QJ47qBL-wZmPCFZ58uzmqUe0BvRp57QWTQFj0-M3WLCpGpglpA-Ff4RLnoS2-cz653c4MbT9-daz5GHyaTKD5-36X5UC3GM6K-kY4SRgvAL1-Uqcz7ParX6EwbRUIbrK1HlnhGQ03mm7d9noB1p_br0kmdqG8fs5oFocbfImGnEhhcOoVlBGfAe7kjaQJNZGRn3Ww2ZDzVuTTCa76r6spLzwd7B5ea-H0XP-pVi4yWLJKhPoL5sZYJ-gKEWHh2BBpH19aZNU_W0w_7YU9WoWFnko6EwzsybnHS3l7eLFvuX2AeWVTXKid9LaWbMZnsFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزرای خارجه و دفاع ترکیه، عربستان و پاکستان همراه با فرماندهان نظامی سه کشور روز یکشنبه نهم شهریور در استانبول اولین نشست پیمان دفاعی خود موسوم به پیمان مکه را برگزار کردند.
عربستان سعودی، پاکستان و ترکیه روز جمعه ۱۶ مرداد این توافق را در شهر مکه امضا کردند.
بر اساس بیانیه سه کشور، حمله مسلحانه به هر یک از آنها به‌منزله حمله به همه اعضا تلقی خواهد شد؛ اصلی که شباهت آشکاری با ماده ۵ پیمان آتلانتیک شمالی، ناتو، دارد.
هاکان فیدان روز شنبه ۱۷ مرداد در گفت‌وگو با خبرگزاری دولتی آناتولی توضیح داد که ائتلاف جدید علیه ایران یا هیچ کشور دیگری شکل نگرفته و هدف از آن، ارائه یک تعهد کلی برای حمایت از امنیت سه کشور عضو است.
روز یکشنبه گزارش‌هایی از احتمال پیوستن هفت کشور عربی دیگر به این پیمان منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78105" target="_blank">📅 16:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IOxmY6rKSASdQBQKq3b3gB8rxXJQSuIc6KSevFdwleYWR7FBh8G2tU-uOVCrZfLAx2QimjA-DOySv47yS_jceX37Gkk8WXHn0sQJAcsslcwgwO74Od1pkOINJmrIEQgRIQaUT4B56YLgsR8GeGXtZzreTtUxws1YImzp3yck8lnpf5cxesPtJUHgSy8oPkI1Do-OtYGkjfeBvMiyLo_HMvxu0UMe2SJibCnprF1jowxsu6Lp-dBUKmwMSzbuTzv7b8ZP7pxJ8paeKKCPCFIT1jFPUyWJR9N5NTgpHh7VtrtFBuMuoo0q_UJ9KhpfiPiW6lDGkyCOvatgW_HxBtFNPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/feZOjlC1e_HOMt2vYaktKxMUVxpp_hBDz9PuY2KKtpHQh9teCyw7pV739YQk9MoJedHsa9dhDR0lEpMWuEE6n-nBqWgJv5m66T3s-E5c3M6ix_QgyvOanINZZve0sYCLFCO9dYAavos9TT4BYsxvBNS8GqwIQgjRdC93c8u52uhIcb1Js7cT8uoFOiBWCw9jWVzFV42AM6P-p71nmm4sYdxh7Z0Cq7qdgn_uwEMYtie67yfcKrFj-2cp0w46L7_d1DQ9SW1Z1UDpblJtKn5EAYbxsYI4wZRdYdXBWW1YmV4jB2ONxEpYfXy9vgk0aEHn7-ekZ_JdaiCg45ktgu8T6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت دفاع امارات متحده عربی پیش از ظهر دوشنبه ۹ شهریورماه با صدور بیانیه‌ای گزارش‌ رسانه‌ها مبنی بر هدف قرار گرفتن پایگاه هوایی المنهاد با «موشک» را تکذیب کرد.
ارتش جمهوری اسلامی ایران ساعاتی پیش از حمله «پهپادی» به این پایگاه آمریکا در خاک امارات خبر داده بود.
در بیانیه وزارت دفاع امارات آمده است: «نیروهای مسلح همچنان در آمادگی بالایی برای پاسخ به هرگونه تهدید احتمالی هستند، به گونه‌ای که حاکمیت، امنیت و ثبات امارات متحده عربی را حفظ کند.»
@
VahidOOnLine
پیش‌تر:
روابط عمومی ارتش با انتشار ویدیویی از شلیک پهپادها نوشت که در پاسخ به کشته شدن جمعی از نیروهای سپاه و غیرنظامیان در جریان حمله نیمه‌شب آمریکا به جزیره لارک،  «محل های استقرار بالگردها و نیروهای» در پایگاه المنهاد امارات «با شلیک دهها پهپاد انهدامی، هدف قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78103" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SZWlb14IjMIA2ZvJTthI_LkCG7FYexSDlRQqG8W1yDbXRTqKJ1Ut5AzFn_fJWLmhNZbC4YkMAk1_Nb-xBqjkLayOLtNY6esMwuwxSz29s0ghscHttdPZonn7tcBCkJCnfUKKPePugFwu5tPZ9cxdvcQ-CE0wN-S4P1LSYaGgjAJlFlgfnvecaCGhgdUNzMZrRzIi8-g9XbHRF7dsXHjtR9ka1kSxRk0W5pJ7BPGAa1d9FL-KdJhQc9IorfYET4RP1dcZfR-AB8Bjiaeilk70yiT9SoeqnZl3jBsrTiHLeaMcGvTl6t2JLkhInaQ7dgq7AWEAaIeKwclqFZlmKXNYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام درفشان، وکیل، روز دوشنبه خبر داد که حکم اعدام موکل او،‌ علی‌اصغر پیغمبری، از معترضان دی‌ماه ۱۴۰۴، در دیوان عالی کشور تأیید شده است.
درفشان به سایت خبری امتداد گفت: «حکم اعدام علی‌اصغر پیغمبری پیشتر از سوی دادگاه انقلاب تهران و با استناد به قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی صادر شده بود.»
این در حالی است که به گفته این وکیل دعاوی «هیچ‌گونه ارتباط سازمانی یا ارتباط دیگری، به هیچ نحو، میان موکل و هیچ‌یک از گروه‌های متخاصم وجود نداشته» و پیغمبری تنها در اعتراضات حضور داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78102" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q5PsPP5yLNRvSj27zUlf6-HR2DicZ5-CcENe5Tol9nh8q0KC3WYl00vRbVhVjiT4yny78jgDQ1r4rqCpLQWYL2wV6V0OtQjqe3G2FNOT7vTIPq-FwsEvolAQsWMwoE6-yatVoKbZMcZMOVntJ_Pr1JRe_rIHcyihJ9XhvA2ZjlG7TlFA0PPEvS9WwGYQIwakOCy7rxtGwcpLk4VX27hQy9lwZJ4oz1G_fpVlprRygWrEi_DPcsEkDCbkNcbWEwnOBRHLaoVuucAZe9l-ZdAWmZRNoIPpUNCHFB3vVA5Ko9UIAIiJW87h1Yi6VUJiIvBcB1CZ48prsQIcRpDZ8dLwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران روز دوشنبه در بیانیه‌ای که از تلویزیون حکومتی در جمهوری اسلامی منتشر شد از برخورد یک نفتکش غول‌پیکر با دو مین دریایی در تنگه هرمز خبر داد و گفت این نفتکش آتش گرفته و کاملا متوقف شده است.
سپاه در بیانیه‌اش مدعی شد که این نفتکش قصد داشته «به طور غیرقانونی» از بخش جنوبی تنگه هرمز عبور کند.
در پی جنگ آمریکا و اسرائیل با ایران، سپاه مدعی است که عبور کشتی‌ها از بخش جنوبی تنگه هرمز یعنی نزدیک به سواحل عمان غیرقانونی است. این ادعای ایران با قوانین بین‌المللی همخوانی ندارد.
در بیانیه نیروی دریایی سپاه به نام نفتکش و خدمه و مالکیت آن و زمان وقوع حادثه برای آن اشاره‌ای نشده است.
این نهاد نظامی به سایر کشتی‌های نظامی هم هشدار داده است که در صورت پیروی نکردن از «مقررات امنیتی» تنگه هرمز، «سرنوشتی جز این نخواهند داشت.»
بیانیه سپاه پس از وقوع درگیری‌های نظامی تازه آمریکا و ایران منتشر شده است.
اما تنها گزارشی که از بروز سانحه برای یک کشتی در تنگه هرمز خبر می‌دهد مربوط به ساعت‌ها پیش از حمله آمریکا به لارک است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78101" target="_blank">📅 08:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41ed8a98ca.mp4?token=LUaoplVOKRZfIOVUHLccD2I0W9aNkfv4BX93vO9dYR6iP9P_kaA6YzLMBfTE8uP--8KSE7zwhViT_hfg5RXBG1I_ndkTpUcbRfFk2vInFLTcCKxFpR8De9_0IVnYM9nbfQge-iqMoFM79rRLfiSiIpkUdaGVT1hSCYa_S9YJZlt5g5OmykTops1dm7JPCLcIxGoY5gSzgweDqsNhr-Jhd-yU2Jrj3p-0-CtG3zMmkNgai1Upq2Oyt2lDi0E-jh_NFbnhnukkYlcxvg0G_-AtxU0sY4BHJe3RvPc2oFnee_7Bg8QvfryJkQytNxGd-kRmbZWLkXjfv0craYyhasa50w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41ed8a98ca.mp4?token=LUaoplVOKRZfIOVUHLccD2I0W9aNkfv4BX93vO9dYR6iP9P_kaA6YzLMBfTE8uP--8KSE7zwhViT_hfg5RXBG1I_ndkTpUcbRfFk2vInFLTcCKxFpR8De9_0IVnYM9nbfQge-iqMoFM79rRLfiSiIpkUdaGVT1hSCYa_S9YJZlt5g5OmykTops1dm7JPCLcIxGoY5gSzgweDqsNhr-Jhd-yU2Jrj3p-0-CtG3zMmkNgai1Upq2Oyt2lDi0E-jh_NFbnhnukkYlcxvg0G_-AtxU0sY4BHJe3RvPc2oFnee_7Bg8QvfryJkQytNxGd-kRmbZWLkXjfv0craYyhasa50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا
ویدیو
ها
یی
ساخته شده با هوش مصنوعی را از حمله و انفجار در جزیره خارگ ایران در تروث سوشال منتشر کرد.
ترامپ نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!»
این ویدیو ساعاتی پس از حمله سنتکام به دو پرتابگر موشک در جزیره لارک منتشر می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78100" target="_blank">📅 08:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p95VWEHzWDnQoBURYDgfvxxFYxSPnwGI1SAwFiLALhVCgB_ZjhiJlFS71IvGrwscVpYbDOOSNbqxMTunMqpsKsj6WdaJwxGVe6Z2SuyZiA6tTkUNWhdaf0-9K_rpW9_OFlk2C4l-wMtvfPVZms3rv_dgIJGdP8KJWKgf_jl5ZntlqZ1DwPcAEEH5uoL0cnteCI4IaLOEHxhyg8DhVuZ8IujMGStvPNq8Xo00uvxPDodKkJA1wJ9Ps4RvXy6YGxae4wKE0C3x-XaygAvNCoQBtO4GoWJHXVSVzosGKT12CNf21jz0monKHPF_8zmln4KoF8JVTlRyzSXz4XfYUQbk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین
تصویر دریافتی: اسکرین‌شاتی از وب‌سایت مرکز لرزه‌نگاری کشوری
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78099" target="_blank">📅 07:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">لرزش زمین
بنا بر پیام‌های دریافتی از شرق تهران
سلام و درود همين الان زلزله اومد ٢/٣ ثانيه طول كشيد خونه لرزيد پنجره كوبيده شد من لواسان افجه ام ٧/٢٠ صبح
شرق تهران زلزله حس کردیم
تهرانپارس تهران زلزله شدید
چند ثانیه طول کشید
انقدر قابل حس بود ک من از خواب پریدم
زلزله تهران
یه تکون ناگهانی شدید
ادامه هم نداشت
داداش تهران همین الان لرزید
نمیدونم‌زلزله بود یا چیز دیگه
سمت جنوب غرب
تهران زلزله اومد شدیدهم بود ولی کوتاه.
زلزله اومد تهرانپارس لرزید
زلزله خیلی وحشتناک همین الان حکیمیه
سلامم تهرانپارس غربی لرزید
تهران چنددقیقه پیش زمین لرزید و زلزله اومد
زلزله بود؟؟؟
تهران زلزله
خواب بودم از خواب بیدار شدم، حداقل ۴ ریشتر بود
سلام. یه لرزش شدیدی سمت تهرانپارس تهران حس شد.
اقا وحید نارمک شرق تهران زلزله شد بد لرزید الان ساعت هفت پ بیست و سه دقیقه دوشنبه
سلام تهران علم و صنعت حیدر خانی همین الان زلزله
وحید زلزله شرق تهران کوتاه بود ولی سنگین
من سمت پارچینم
لرزش شدید
یا زلزله بود یا موج انفجار
سلام پردیس لرزید چند دقیقه پیش
شرق تهران ساعت ۷:۲۱ دوتا پس لرزه شدید اومد
سلام وحید جان دو دقیقه پیش به وقت تهران من رو زمین خواب بودم ..جوری زیرم لرزید که بیدار شدم مدتش کم بود و شدتش زیاد
آره وحید زلزله اومد سمت شرق تهران خیلی حس شده
سلام، فکر کنم حدود یکی دو ثانیه زلزله اومد تهران
من غربم :) اینکه گفتی شرق هم لرزیده مطمئنم کرد
تهران  الان  زلزله اومد  شدید و کوتاه بود
زمین لرزید الان
مرکز شهر تهران
من سبلان زندگی میکنم.. متوجه شدم
ماهم تو جنوب شرق مشیریه لرزیدیم
بحدی لرزش شدید بود ک ما تهرانپارس شرقی هستیم خواهرم تهرانپارس غربی
همه از خواب پریدن
لرزش شدید
شمال شرق تهران
همه رو از خواب بیدار کرد
شرق تهران.تهرانپارس
پحید اینقدر تکونه زیاد بود که از خواب پریدیم
حدودا ساعت ۷:۱۹ ۷:۲۰
ببین صدا نداشت ولی قشنگگگ خونه لرزید عین زلزله همه پریدیم
سلام من پاسدارانم از لرزیدن خونه از خواب بیدار شدم
لواسان قشنگ لرزید
سلام من جنوب تهرانم منطقه ۱۷ طبقه پنجم زندگی میکنم کاملا لرزش حس شد و تکون خورد
ما نارمکیم خونه ی ما یجور لرزید که من با وحشت از خواب پریدم
😭
سلام وحید شرق تهرانه چیه
من مهرآباد جنوبی سمت یافت آبادم
قشنگ خونه لرزید
تکون خورد
غرب تهرانم احساس شد
سلام ما دماوند هستیم لرزش احساس شد
من یوسف ابادم
ساعت ۷.۲۰ لحظاتی کوتاه زمین لرزید
تهرانپارس چند دقیقه پیش کوتاه لرزید
سلام صبح بخیر ، ۷:۲۰ دقیقه پردیس لرزید
نارمک هستیم در حد دو سه ثانیه زلزله حس شد ولی خیلی ضعیف بود
سلام وحید جان ، من ستارخان هستم و کاملا لرزش رو حس کردم فقط شرق نیست
وحید جان ما هم مرکز تهرانیم این زلزله رو حس کردیم ساعت ۷:۲۰ بود حدودا
سلام ۷:۲۲ سهروردی خونمون قشنگ لرزید یخچال تکون خورد ولی در حد یک ثانیه بود
تا مرکز شهرم ما لرزیدیم
خیلی کوتاه بود ولی بد لرزید
زمین‌لرزه_تهران‌پارس. شدت خیلی زیاد و کل خونه لرزید
سلام من سمت جنوب غربم خونه طوری لرزید که همه بیدار شدیم
سلام وحید جان سمت مشیریه هم لرزید ولی لرزش عجیبی بود شبیه زلزله های سابق نبود
وحید بد لرزید جوری که من همه رو بیدار کردم گفتم زلزله
اینجا نزدیک دانشگاه امام حسین
قشنگ شبیه موج انفجار بود یه تک لرزه
وای خیلی وحشتناک بود خیلی بدجور لرزید هنوز دستام داره میلرزه همه از خواب پریدیم ما شریعتی معلم هستیم
ما میدون شیخ بهایی هستیم
لرزش زمین اینجا هم حس شد
همه مون فهمیدیم در جا زمین لرزید
ساعت ٧:٢٠ صدای مهیب و لرزش زمین در پردیس شنیده. و احساس شد
مردم اومدن بیرون
سلام، من مرکز تهرانم و متوجه لرزش خفیف زمین شدم.
سلام شهرری خونه شدید لرزید ۷و۲۰ دیقه ۵دیقه پیش ما طبقه ۴م فهمیدیم
ما تهرانپارس هستیم دو تا تکان شدید مثل انفجار بود دومی خیلی شدید بود ، زلزله نبود چون لوسترهامون تکان نخورد
نمی‌دونم انفجار بود یا لرزش ولی ساعت ۷:۲۰ کامل سمت نارمک لرزید
جنت آباد هم لرزید و کوتاه بود
زمین لرزه شدید  شرق تهران   تختم  بد تکون  خورد
یک ثانیه بود ولی تکون خورد
منم رو زمین خواب بودم متوجه شدم ما مرزدارانیم
زمین کامل لرزید
سمت ظفرم
ولی لوستر تکون نمیخوره
سلام وحید جان شمال طهران هستیم اینجا هم زلزله رو حس کردیم ولی خیلی ضعیف تر از شرق طهران
سلام ساعت ۷:۲۶ دقیقه سمت میدان خراسون تهران زلزله حس کردیم به حدی بود که خواب بودیم از خواب پریدیم
نارمک خونه لرزید
انگار یه موج از زیرمون رد شد
حرکتش کاملا معلوم بود
من از رسالت (شرق تهران) یه چیزی ضربه ای خیلی شدید حس کردم شبیه زلزله نبود
منم لرزش رو حس کردم کوتاه بود ولی قوی بود
منم پیروزیم ساعتای ۷:۲۰ دیقه شدید لرزید
سلام خونه ما نیرو هوایی هست چند لحظه خیلی کوتاه لرزید ولی خیلی شدت تکان زیاد بود
ما نيرو هوايي هستيم از شدت زمين لرزه از خواب بيدار شدم
من هم لرزش رو حس کردم توی نارمک
دوتا لرزش بود شدتش زیاد بود ولی زمانش کم
فکر کردم از بالا مثلا همسایه محکم پریده روی زمین تا الان اومدم پیام ها رو دیدم
رودهن هم لرزید
سلام وحید من شرقم علم و صنعت
نمیدونم بگم زلزله بود چی بود
انگار بمب افتاد
خونه ما شرق تهرانه(حکیمیه) و حدود ۷:۱۵ برای سه ثانیه لرزید، نمیدونم زلزله بود یا چی ولی هیچ صدایی هم قبلش نیومد،
خواب بودم تختم عین گهواره شد بیدار شدم. اتوبان بابایی تهران
سلام اقا وحید زلرله ساعت ۷ و بیست دقیقه بومهن و لرزوند شدتش زیاد بود
من نارمکم، زلزله اومد، یه تکون شدید خورد قشنگ، از خواب بیدارم کرد
ساعت ۷:۲۰
سلام .تهران . نارمک شمالی. با زلزله از خواب بیدار شدم. تکون و صدای شدید داشت.
سلام زلزله شدید سمت نارمک میز کامل تکون خورد و لوازم لرزیدن از شدتش بیدار شدم
میرداماد هم حس کردم
به حدی که از خواب پریدم
هروی زلزله رو‌حس کردیم ....
و از خواب پریدیممم
۷:۱۹ صبح
پاسداران زلزله درحد تکون خوردن تختم از خواب پریدم/:
از شدت لرزش از خواب پریدم
خیلی عجیب بود
ساعت ۷:۱۵ ، نارمک هفت حوض
سلام وحید جان،حکیمیه از شدت زلزله از خواب پریدم هم خودم هم خانوادم!!
فرمانیه هم من کاملا متوجه شدم
ولی بیشتر از لرزه موج شدیدی داشت
سه تا موج پشت هم که قشنگ تو پنجره و دیوار پشت سرم احساسش کردم
ما پاسداران سمت حسین آباد هستیم
قشنگ خونه لرزید
پردیس حدود ساعت ۷،۲۱ لرزید
وحید جان افسریه جنوب شرق تهران لرزش زمین بود که از خواب پریدم
سلام ما شیان هستیم خیلی بد لرزید
به خانواده ام گفتن باور نکردن تا کانال شما رو چک کردم فهمید درست بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78098" target="_blank">📅 07:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✅
واقعیت: نیروهای آمریکایی اقدامی محدود و دقیق علیه نیروهای مین‌گذار سپاه پاسداران که تهدیدی قریب‌الوقوع در تنگه هرمز ایجاد کرده بودند، انجام دادند. در اصل، ایران این تهدید را ایجاد کرد و ارتش آمریکا برای حفاظت از دریانوردان غیرنظامی، کشتیرانی تجاری و جریان آزاد تجارت جهانی، آن را از میان برد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78097" target="_blank">📅 05:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78095">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tj9Gs8VKxV1i_eak03hKKh892tAcOMfnKOf5pzgi65EZkTUssIteRMYZB-b-DSIS2k-boYAjqQBpA_frZ5l7lQhI2IGIqlNqLh6-v20gsvq2zyd1_oEPsrJHks0oAHrZfacWLwaR-FcjtH21xgcKSzHOrlbUwGrEeBHd5X4eSj6SfJgqHKf83qFRq8403VkMRM3fsTNNHCDPqL34Zu9oPWbDHo1SKdwDEBQF34KA8DxwytsmKe5LCv3Kw_7ftteIAPFxTyZVbfUfy7q6qUmKZEE_T-_WilUaFVbO_JIkIu_w5lQjIaJGwpxxgrh5mYpPMSzBgwFUOFVjpAO_CfZYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VYHt_rezgcpNKCipdX2Wvi3mnuPaowpavFh7OB0sKSZJUUPkYNXYFTHCKD8_WK5Aib0ms_H1kBaV1GVLbhX5TmtgT5ci-OGQ8ZmdOaM5RzyJ-vW4DHh3iRq_wsOiaM_eYECtCQw56_3D8uujBDsx68UuYR1LU7Q9qUQ40vMn4pxBr1dRbC2pxlzZ3FBnMQnMJX43c-gbbhyr3Rouhi_Kjde5QD_d6qIyjfX6ygTZiPfh3nXJPHSXzJriMyjuUn-MMDftsTdy6_irp2OpR8G7yNt5GPsrqy3QVbC-AsXdMNVlLxNCvKuGKF5Jmr5dlCMzxiAd0NysLXb0_HKHbkTTBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در گفتگو با «فاکس نیوز» بار دیگر حکومت ایران را حامی شماره یک تروریسم در جهان معرفی کرد و گفت هیچ کس نمی‌خواهد آنها سلاح هسته‌ای داشته باشند، حتی مخالفان عملیات نظامی آمریکا در ایران.
ترامپ همچنین گفت که حکومت ایران به سختی خسارت دیده و رهبران و تجهیزات نظامی‌اش را از دست داده و او به دنبال یک امضا روی یک تکه کاغذ نیست.
ترامپ رهبران حکومت ایران را سرسخت و در عین حال «شیطان صفت» خواند و گفت آنها همین اخیرا ۵۲ هزار معترض را کشتند و همچنان در حال کشتن معترضان هستند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه یکشنبه ۸ شهریور گفت جمهوری اسلامی به سلاح هسته‌ای دست نخواهد یافت، و تاکید کرد برای پیروزی در نبرد با رژیم ایران لزوما به امضای توافق با آن نیاز ندارد.
پرزیدنت ترامپ در گفت‌وگو با فاکس نیوز گفت محاصره دریایی و فشارهای مالی آمریکا ضربات سنگینی به جمهوری اسلامی وارد کرده‌اند و این رژیم اکنون در حال فروپاشی است.
او افزود: «در زمان مناسب، یا ما پیروز می‌شویم یا آنها کاری خواهند کرد؛ اما من با صرفا پیروز شدن مشکلی ندارم. نیازی به امضا روی یک تکه کاغذ ندارم.»
رئیس جمهوری آمریکا رژیم ایران را «بزرگ‌ترین حامی دولتی تروریسم» خواند و گفت: «نمی‌توان اجازه داد آنها سلاح هسته‌ای داشته باشند، و سلاح هسته‌ای نخواهند داشت.»
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با «فاکس‌نیوز» با دفاع از اقدامات نظامی و سیاست‌های دولتش در قبال تهران گفت: «اگر من رئیس‌جمهور نشده بودم، اسرائیلی باقی نمانده بود و به احتمال زیاد اساسا خاورمیانه‌ای هم در کار نبود.»
ترامپ با تاکید بر اینکه حکومت ایران در صورت دستیابی به سلاح اتمی از آن استفاده می‌کرد، افزود: «کشورهایی که سال‌ها در موضع بی‌طرف قرار داشتند، با آغاز درگیری‌ها بلافاصله هدف قرار گرفتند. از عربستان سعودی و قطر گرفته تا امارات، بحرین و کویت هدف گرفته شدند و همه از این اقدام شگفت‌زده شدند. همین مسئله باعث شد ایران حمایت و موضع بی‌طرفی آنان را کاملا از دست بدهد.»
رئیس‌جمهوری آمریکا در ادامه با تاکید بر جلوگیری از پیشبرد اهداف هسته‌ای تهران تصریح کرد: «اگر آنها سلاح هسته‌ای داشتند حتما شلیک می‌کردند و پس از نابودی اسرائیل و خاورمیانه، هدف بعدی ما یا اروپا بودیم. شما نمی‌توانید اجازه دهید آن‌ها به سلاح هسته‌ای برسند و هرگز سلاح هسته‌ای نخواهند داشت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78095" target="_blank">📅 05:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i7brzDyNzpctldyLb9WzatzLMgYk74oOWFJ9WUdJMYfTML6IBtH-Hd-351Fyoqo3DIIsIj9tKVkRTYC8aTny4QnH8SeviR7HhzSFEafIYbkeXkl_Pc4Th87WFSlX-YoHmWNSK88leBhR7TUHZM5dC8Y6zOJuVVRYbkP3qS6Onl2dA3D88NUA82GJtQcZoy_nWA7c1rWMGXpmhZo6f9bZvoEyxoDTN1ZP8PrX9Sr_urFldPz7xd17F-3CbtDU3S215YtljXk9L1Yq50vhECnUcihJi8p7G28VmzEhNmYFH1Ew0qpzo3VztMU0g43mY5vryjqKpi8K0SDHhIkEc9VFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JyHniwq3_6L7wLJPtCgsRCsnmcI63neVLsylSn8ENznoJ4jSqAvIgHXKQV8hubdwcIdRd8ywbGSP-vQAODMLTOSxUnmamZckqbt1RJpQ7Z9XxQUseAI__x0lFPcnOT3AepQtk2iUwhZSJuNyg1afPOOzqSIerXku1j2ehWmeKJEzYbhDWrvgrEMWRfmiaJkOsu_l8jL8swysTq4q8EFF8Stv8VMVwt6YpN9GbXb2tnHRR9ANSax_vcCQvUeFNnmDtcWTYebr57DwCSKpKW4TpVQFXH45jAuYrC-bBbxZYrcJ-J0mTf7GaFU04tlfKeb6F9ltIhjF2-ke6LXVwLHNaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با گزارش خبرگزاری فارس، مبنی بر اینکه حملات پهپادی آمریکا به جزیره لارک از «مبدا اردن و با پشتیبانی پایگاه‌های این کشور» انجام شده بود، روابط عمومی سپاه پاسداران بامداد دوشنبه با انتشار بیانیه‌ای اعلام کرد: «نیروی هوافضا در پاسخ به حمله به جزیره لارک، در یک عملیات ترکیبی موشکی-پهپادی، زیرساخت‌های فنی، تعمیراتی و محل استقرار جنگنده‌ها در دو پایگاه هوایی ملک حسین و الازرق در اردن را با شلیک موشک‌های بالستیک هدف قرار داد.» در ادامه این بیانیه آمده است: «اقدامات نظامی، تضعیف‌کننده کنترل بر تنگه هرمز نخواهد بود و هرگونه شلیک با پاسخ‌های متقابل جواب داده خواهد شد.»
@
VahidOOnLine
شبکه فاکس‌نیوز به نقل از یک منبع آمریکایی گزارش داد در پی حملات نیروهای ایالات متحده به پرتابگرهای موشکی در جزیره لارک، سپاه پاسداران مواضع نیروهای آمریکایی در اردن را هدف حملات موشکی قرار داد.
به گفته این منبع مطلع، تاکنون هیچ‌گونه خسارت قابل‌توجهی گزارش نشده و سامانه‌های پدافندی موفق شده‌اند تقریبا تمام موشک‌های شلیک‌شده را پیش از اصابت به اهداف رهگیری و منهدم کنند.
پیش از این سپاه با انتشار بیانیه‌ای از هدف قرار دادن دو پایگاه هوایی «ملک حسین» و «الازرق» در اردن خبر داد.
@
VahidOOnLine
رویترز گزارش داد قیمت نفت بیش از دو درصد افزایش یافت و بهای نفت برنت بار دیگر از ۹۰ دلار در هر بشکه فراتر رفت.
این افزایش پس از حمله نیروهای آمریکایی به دو پرتابگر متعلق به سپاه پاسداران در جزیره لارک رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/78093" target="_blank">📅 03:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پرتاب موشک از خرم‌آباد
طی ساعت گذشت پیام‌های پراکنده مختلفی دریافت می‌کردم.
ولی در این لحظه یهو کلی پیام از خرم‌آباد اومد درباره دو صدا که خیلی‌ها نوشتند مربوط به پرتاب موشک بوده ولی بعضی‌ها هم تاکید دارند که بیشتر شبیه انفجارهای برخورد یا شکست پرتاب بوده.
هم‌زمان پیام‌های مشابهی از کنگاور در کرمانشاه دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/78092" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hd0yP7OwNHI_aBR5KeTbVqgYO4M8XjQvlhTx4sHB9RlcwE9CNAgPCbQHMObGpPYMk2Z6ZeBcxZrC07Hxa700TgeWnrYoC7dOze-F5bkHJyjG5g1psKwzJmZIRfp7D60v584EPCr5nOLQKklUjcnYssEsFoqrk8kIV7kzSsqxodt6BsGXSczTKOjVvuVw9E5M_rqqn1ndNIpBKHihgTU3CqpWVPw4O84jkyJPWRQfqtVVdnmvaY7ZpvavoU_DuYPwBZ_ezbIwtoj0xqxTlC0GmpdQN2wvjQ2MqMB5q0srWXDbViOgNcJbPf2PolSU_yoW-8X_xXueRZBTAhMwDLK_pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 484K · <a href="https://t.me/VahidOnline/78091" target="_blank">📅 23:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/78089" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OeJjDAR-_579q9NDmghAF2YDT4csENCCbZCBVbbYmh4V5vChFCsQkw4OU4PLHGYP5BRTzSrKy1sWIflHWaQ0Ns0D3iWtgCBaaiLDjcv5Z4kF9bxYC0qVQPh3B5tfGY2UHw_4O36-OYk-7rb-Cadq3_IxZSenXew2mytBmGKpwwWfuYAYrxXUvHycM_B5MFLE51lR-N63h11Iu9hcDZrzLPno8ctfxc2Ym9vGSEb5paq2kvu-wy0KT9dNdtiv02rHdEhH2gpcKaVkFW5WWg-GokZxKIijIEi0mOWRR2gVOKJLAgCKgQ4RA8B08Hcz8bo1zV5Jrv7ciB_kazqGhgBAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
یکی از کارهایی که قرار است با نفت ونزوئلا انجام دهم، پر کردن ذخایر راهبردی ملی است؛ ذخایری که به‌خاطر جو بایدنِ خواب‌آلود عملاً خالی شده‌اند. روند «پر کردن تا ظرفیت کامل» به‌زودی آغاز خواهد شد و این هدیه‌ای از سوی ونزوئلا به مردم ایالات متحده است. متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/78088" target="_blank">📅 17:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fFvdtF5_p2mElGSJBylGwakIfORrxW4dJDiM6QRnzPQxWZeytcRwuegyeFDQpMmNCmTRMq5Mgh0R6ZCQhKA-QZcsn1C5yh-Y27XVpUq0AEktCGY7vYknn3wqlWTOIiSJmBi2ZVWPYKpykm-XHB2msY3Wzb8efj94UzZqDkJDrZRWqrELf0KLRDLiDwvorq-DzqFWOgpGo-8OgVz4z_Xv4NaoZkrDlQpzMJTFrfYJQF1RjZM2lSWkQ3dlUi3tCGK7VkPyA0xTJwwODCBC-Gxc1hZpHh-2Ns03fqX353QMvgceU49-jHxcNP4WCffixIYzweKANt3s4xpfB_YPVi0DDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشینگتن‌پست به نقل از افراد آگاه گزارش داد چند مقام ارشد نظامی آمریکا به پیت هگست، وزیر جنگ آمریکا، هشدار داده‌اند که ادامه عملیات نظامی گسترده علیه جمهوری اسلامی پایدار نیست و توان ارتش آمریکا را برای مقابله با تهدیدهای دیگر، از جمله دفاع از خاک آمریکا، تضعیف می‌کند.
به گفته این افراد، این هشدارها که روسای ارتش، نیروی دریایی و نیروی هوایی آمریکا، همراه با فرماندهان چهارستاره مسئول عملیات نظامی آمریکا در اروپا، آسیا و آمریکای لاتین، در نسخه ۲۳ مرداد «کتاب دستورات وزیر جنگ» به هگست ارائه کرده‌اند، بخشی از یک سند محرمانه است.
بر اساس این گزارش، با توجه به تاکید ترامپ بر اینکه گزینه نظامی همچنان روی میز است، ستاد فرماندهی مرکزی آمریکا (سنتکام)، که مسئول اداره جنگ با جمهوری اسلامی است، ماه‌هاست بیش از ۵۰ هزار نیرو را در حالت آماده‌باش نگه داشته تا در صورت صدور دستور حملات بیشتر از سوی رییس‌جمهوری وارد عمل شوند.
به گفته افراد آگاه، نسخه ۲۳ مرداد کتاب دستورات وزیر جنگ مقرر کرده است که بخشی از نیروهای مستقر در خاورمیانه تا پایان سپتامبر در منطقه باقی بمانند و ماموریت برخی دیگر تا سال ۲۰۲۷ تمدید شود. احتمال تمدید بیشتر این استقرارها باعث شد فرماندهان نظامی نگرانی‌های خود را آشکارا مطرح کنند.
به گفته این منابع، فرماندهان ارشد فرماندهی اروپا، فرماندهی اقیانوس آرام و فرماندهی جنوبی آمریکا، همراه با فرمانده ارشد نیروی دریایی، در این سند نظر «عدم موافقت» ثبت کرده‌اند؛ به این معنا که با دستور وزیر جنگ برای تمدید استقرار نیروهایشان موافق نیستند، اما آن را اجرا خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/78087" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Drxt1pTjJNqzhy--_BiBtewZifIPXhCAxPtlnODAM7QJ5DtM_LzqLm2TOEJZLR13oHc8TltUdNNjyIGgoDU7QKmxj1VA03D6xpl7e3TRyWWFFpAJbs-rzylprNUoG4ZCNc-hminq9Peib02l8hY8IOqkD1MiWOd2YNq6zO7Lfto7tvvbhuzWOndjn4U2CbgtPA4W7JSXTbtoz7dl9vstS2pNT9n2e6mLDcoIxkzEhsXuK1LLzySffP4HzrvFjs8T92fsJwNAO5BYXXmOKlIyQL6_fjIIE78jmp2PC8nu6BPREfLPOxUR5cEhA5VNvYlBu9bTXR_Sc_uu2Y336P7Uwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78086" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGYozJu10sGSxmxZPL4hGWyDYra3McqcdJ2t1f9v4N2QNE8iG4bM4RmCfghOKsudj82HX70Vo7cukZWCv3z7kVsFjtW320JiWqhcPZTgXPbtrjgrb7lMK_IaVHthNnr1pZwA9SP88thRhdHHd9YwRK2wqu9MSWlt1JH59LpUWkG213DOQq4q5zm6le_GFLa2S6E1ezqMDPxz3JRaiSw6h3yXVoyy0Jrar76cAGQmxdd7K9QElGAMCCm3Ecux-ridsFxbLYqtwByCgt_FEzXS3W3CJwS2Jxbyckmfvk5Bdk9YDZSRzn4Wv41B3YH33QTuNwmRhKjvB0n7CP6hHKOAnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78085" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B9jC4NOgEI32cpCiBk-UaDa14LH3U9LZDNTCN-_iDlMaLCphxnZGZlOmsxjkf7MA9njZ6z3TJIS0n3BxcU9I66wyhJmi14LcQFR-czNWcLo29zeubGoKeg8I6jjJCocx3L21GwsdM2f3h8Gm9-EBaITpafpmRUKcp3SyHW6MuRy3QnbH_cu6s82v7bQHjz8zWM4Ns6_aOKtVCBtdQAv19rOGjdS4x4UXx5eVcJPoXthQ1t_pfUR-dAF_9NcgCvi69idByr-OqDy4X8syh4yfIgtI59KdD3Q8Nlyvr83flciM1qk5Qlx0MQzqDsKvl-SYu3qj3K3jRqUiiqs1_jrVNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78084" target="_blank">📅 19:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ceeb0af509.mp4?token=GA2BIlKs9gCesQsUeo8YaGamE_Dn6v1zg3F7TVqIhzw3m0JYVoGdi_Yxi2SGqjJ4LZuQQB-11FOBpOemiV2m1OjSlfCQXjx2QxTLVoOG2EnTiean2Xfeu0G4BWOBs8XPlw-mO7d0WDUr_C2CJFipRF3NRTwl6jXGrDTN4zq2e16ofLuTMdFC0XQRahtf3aAXTKYfC_BbyAgYOqRd-s1tS6zewhcOTjjI_ZK84wB_IjWxXlictarkzuzLDPE9bDCkTgS6fEXAVOX3FO8371YkzYoJ2DELU4xDHgZyyTOiXowTD5TU-Atq8bo9fuEfMlrdLSRnuYMaYYaFy9pBWnxKog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ceeb0af509.mp4?token=GA2BIlKs9gCesQsUeo8YaGamE_Dn6v1zg3F7TVqIhzw3m0JYVoGdi_Yxi2SGqjJ4LZuQQB-11FOBpOemiV2m1OjSlfCQXjx2QxTLVoOG2EnTiean2Xfeu0G4BWOBs8XPlw-mO7d0WDUr_C2CJFipRF3NRTwl6jXGrDTN4zq2e16ofLuTMdFC0XQRahtf3aAXTKYfC_BbyAgYOqRd-s1tS6zewhcOTjjI_ZK84wB_IjWxXlictarkzuzLDPE9bDCkTgS6fEXAVOX3FO8371YkzYoJ2DELU4xDHgZyyTOiXowTD5TU-Atq8bo9fuEfMlrdLSRnuYMaYYaFy9pBWnxKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع حکومتی:
"اعزام نیروهای مردمی به تنگه هرمز در پاسخ به یاوه‌گویی‌های ترامپ"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78083" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZWZZN9N1aDX-6fpu2XtxySX3Nt0Qt8Z4-e9RGayubDYuav8MRpEXetz3ZrKswsdGMMlCfIMYBvFelX612JEzdzsMu9PFLC31r8HoQyqVw5FsDJsqCM9Qq04BHomoYuRUb_1NbSaOIR6hLg7bTrKjn7wp0lnBDzTZ_U-zpSYZEdl0J9IdsaEJkOdDkgujag1_FKNvz3ma3xtw9HGhOVnK3r7cqxPARu050bxtU_-N4AD3FQqKfLlQU2UXpHJQnq_YqwvDeYZm_9FyCURyxcWc8HW_NPITfmHUaiSGN2_QNSEtV9qCnIxlFsEsEm-OCDmcAWCA2Qt028pLFFoikiLSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از ابتدای سال ۲۰۲۶ تاکنون، بنیاد عبدالرحمن برومند ۹۵۰ مورد اعدام را در ایران مستند کرده است. دست‌کم ۲۰ زن و ۳۰ معترض در میان اعدام‌شدگان قرار دارند و تا این لحظه، ۴۵ مورد اعدام در ماه اوت به ثبت رسیده است.
🔸
در نظام قضایی جمهوری اسلامی که بر پایه روندهای ناعادلانه، عدم شفافیت و نفوذ انگیزه‌های سیاسی بنا شده و در آن اصول دادرسی عادلانه به‌طور سیستماتیک نقض می‌شود، استفاده از مجازات اعدام، بر اساس حقوق بین‌الملل، مصداق سلب خودسرانه حیات است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78082" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IgiiutIAx9zLX56UQJw7keFdFpO1usSvZtDejF_AJV9HwDXnViDvwvno1MUOURIHJcaK-arHlTbA76NP5ud8SgdGSfNl0oiZB8nixZvXKH5U5pLPWmh3A96xAvLzNxlvnQHVV5MtBdEEolfjukll7oZ58UTC0LAKen05cQVOeonLyA_rCTvcZ-nSjL5ZzBvbqpd33yK7shxrI-j-TrrrDeWoDbT8z93OGrFZrdUQmekZtPac-Ea1y2Tl4nco7P7nWD0vSY8Ee7fDKYfLJuW4nkONQNOnsX5dB60TuwBZAn-zWDcnZ4ZHk1fkWfWUYAXvczczYKp3fcClPDDHcAOTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YRp7owgh9qxpi5_NgCt0pJ4UzQJjIWX1BXXVlz8Ip0obGpUt4LNoysHa7w7RmXvVn5a5xtHvI81eRvpu2KDR6TVPiHovy4tSqcmoFuyv3Y5-QbhMI_y8rRrm7B6ykiGWzq93-4Rh_FvvYRHTy9e-O2wxjzvDkFP5r2ffxEmb6FpKFjUmyQ6dZGDgu689IE0gOkeCuOUcRINrdy4wwa8jD35qAzUb4YALDYY7HyQKWmSmgVl_RrlQzPKAMZDqwFIahDcbPzwFYRN34Wy1Jgg3z5ofsB1oupPbN8Gwf0MHUwULA8vlzfZAXN7dQOYE2SpL5bGYS_bQbWM-7ZO0pA6EBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78080" target="_blank">📅 04:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=VotO2dCz4b416W9a0A2uIGepyUsQz_hlEQf5tMO8uYGgYT9XTWYqoeoRqdWXBt7VdGxDsCw6Rh72MtgcBqrf_C2BPlrvizqwnyvo4nzCbSRAO2YAhSMcS_Kxv-Si9nM86K4npUqM6AFUety2W2dDB4N4tQPQ4HRvPFKhx1UNXn395MxocA0xRSfWoBwwey3LV9oxUbAxahpQNEw3s8SU-pwblwoCUn8LSCWeUB-Q2_gy1uGk2okbxu-jAFgqjU_KdeemcgsiR_vBhVupXQu7bV1sLXfNyBRS45B8Ofd8H2IdotTxf2rzwBt2E6Mvgx5bJoOrcyc6VGTngbF19bLhjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=VotO2dCz4b416W9a0A2uIGepyUsQz_hlEQf5tMO8uYGgYT9XTWYqoeoRqdWXBt7VdGxDsCw6Rh72MtgcBqrf_C2BPlrvizqwnyvo4nzCbSRAO2YAhSMcS_Kxv-Si9nM86K4npUqM6AFUety2W2dDB4N4tQPQ4HRvPFKhx1UNXn395MxocA0xRSfWoBwwey3LV9oxUbAxahpQNEw3s8SU-pwblwoCUn8LSCWeUB-Q2_gy1uGk2okbxu-jAFgqjU_KdeemcgsiR_vBhVupXQu7bV1sLXfNyBRS45B8Ofd8H2IdotTxf2rzwBt2E6Mvgx5bJoOrcyc6VGTngbF19bLhjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: نرخ سوم بنزین حدود ۱۰ هزار تومان خواهد شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78079" target="_blank">📅 22:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YW5CID3r-smc5UGtav38y7XR_JgfvpofaN_K34BUzcazDb_OLAA7onoA4I_-gkjrqFLSnuGsWCElxb_ucRm2for-MjEC6w5kEfKM0giZi9O33OBnCv2hUxLEbNXYk9yV8kMc5Iypleogvmt5ccF2bRgJp4wCheHk8Nb4v7VpPc2smcl7ghuOwUVYdGZhw7D9kLyHvMkdMzWvnz0tlbh0qmLbpEAk3bk0AYylfw63mE3n-DEEVVB6oHg3y_6IFNLHwqx20_4ruCVrYkgEhVK5mFY6na1UgxhEQsLNc0wpoBPjq5pUFF60pQu-7PYU5n1UPmWa42O5HCe4y1IjYSOWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.  به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم…</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/78078" target="_blank">📅 21:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78077" target="_blank">📅 18:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78075">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XKfCiFfoam_teyoMz8Nt4IZ3ZAEkY-HyH2OUPbKaiCsmb-rjt3YTmrXC1A776kOOlTjvp0zPaf7urhERzsk24qLO-7G_nKlkJJ0ADNTKAQnwa1Ci963N9rR-zyoREOuk2KfCY2kSHKTx14bmCvqMdxuFrvHMe66trUv_h47Y7aRhZgyV40c6Gry8gPbDS-BIvOQH3300MmDmema15gbMqdcirErQfpmGpTMnH0ZyCYxCDqnhxfu4dDcAl2Z8AkP6YagTOIRT178I215q1D6mU5qBOo5OBEiDjV63mGeJkWfCjiXKJ5R-2sGkx2bdJCHIfkBjQkzeXkaWJTZDQsr47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا نوری، امام جمعه بجنورد، در خطبه‌های نماز جمعه این شهر گفت: فشار اقتصادی کمر خود آمریکا را هم دارد می‌شکند و با فشارهای مردم در آمریکا بر علیه خود ترامپ، او که رای اول را در آمریکا داشت امروز محبوبیتش به زیر ۳۰ درصد رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78075" target="_blank">📅 16:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hlkwS3AAkR7yBBxIpyU8KZO-9ACK-Lut0tH3XuVNGpT0_ZuXDWNhGVeXHfen4L5yTkPcK3xj0o-rKOx90ZYOjREx18MGBHSfwGJPez5u3GHYjO9wt5pnEvU3df113z_qs6g-f8lF2QgvFdSXYJ6xfTICJxYoXDlC69HdYoeGCeQTAj63iU-3FX9jOPhOk6PuaHqlvc-slskdZF_gIOWRDOZACqlO6K5XF0eyEVH1MOdSZ4J5FORA_oWYEFZ3xVcxpQr4vLbRgfjIjHPJHX3zYVxL-uNCX84aotHOzFoLxRZQEY2ImumyKqiYCTx1E14yuuKmW8axBXWHNWXskRxhzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78074" target="_blank">📅 16:43 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
