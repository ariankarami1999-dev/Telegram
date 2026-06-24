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
<img src="https://cdn1.telesco.pe/file/gddkxtyudohLP7c6QKBzZDjoTmIjIADG3JBLnIq4UKzeqMncsqI48oiYtJvMOJYyZGm-oKBvk8Hj5EHi6Z4iP8LfoGX3f7RJIQEBPPS6TmZcEySpBFKk6jPO29x9WYzPxFW8YRu_7EDlJq1BU9TaSXJbdOinkgxqXnQxmlGwrPYmisiNL9zLr9o8-NEOhW2ibc6eQrRqSr-rUrkePJWRSjvWlreQznSPUSglQvsUDBJLiaxRwZuiY8_oOTZLdHCSBTofA-oa4JAUetJ9kAYawE-BoJgtbug2bnbVTisqK5eHd-tOD9S3XCO6vs_9bA-EgFE7hj4a9_EjzfHgvvXcBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 15:47:36</div>
<hr>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=gSeh6k9Ksg98fJQXdAre3-yDH03YnbT0eIWbBoLNl0d5UOQDctFqBgSx5h1XLTDDHb4oh1_Fjl2lACIKXPvkh8tw25o4DJrqne7ScVPBlWb06iWm5SlV1LcZbYvkdzyS4W1OJtoW0AaZuN_z8B4vfwCNzUD1Xmfvr9vBsfzYa03xqvDmQtoicV4m3ZZiQMx2CJzPU6GXeOsFjJArMO2d4urbxIknVt8hHmRNAYzMvrw-Z6oqIoOsfPHPVhZfjpRRfSqTfwr4O53nG0PAiyLsJGGthW9ovi6-LuAsxz6c70aUVXLmtYg9X6hcageDHkBnveIhczekQKFLXXN9UaOO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=gSeh6k9Ksg98fJQXdAre3-yDH03YnbT0eIWbBoLNl0d5UOQDctFqBgSx5h1XLTDDHb4oh1_Fjl2lACIKXPvkh8tw25o4DJrqne7ScVPBlWb06iWm5SlV1LcZbYvkdzyS4W1OJtoW0AaZuN_z8B4vfwCNzUD1Xmfvr9vBsfzYa03xqvDmQtoicV4m3ZZiQMx2CJzPU6GXeOsFjJArMO2d4urbxIknVt8hHmRNAYzMvrw-Z6oqIoOsfPHPVhZfjpRRfSqTfwr4O53nG0PAiyLsJGGthW9ovi6-LuAsxz6c70aUVXLmtYg9X6hcageDHkBnveIhczekQKFLXXN9UaOO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uy1PRZF35la-ISWsfmOcatoS2Rpf1ZbmlPtdPtOIMl485EFQV9UjVu4-ZvKTOkfECxwun5GPfKxRgfqNmh4T_pyga05TXrM9rZCHf9hzLNPyQw4fss4488oyA3zaGh2J_0KE4bp0rhzFaaYr7HubQqZQetOL_kvLY30kNlxd1B6jZtspXVXbr6jZywquDGgkZRPjcLaO1kInfE1-3W2IVaKkmmuVj9lv59EGjKf9lA9PWhTejmEXSsvdB5_eS8oSlft52yEwEI8vJkYJ5vXSqDh5uyBLNFeKhMJl7MJgW8U9STSe_hzpvmEpJvpCIMAvwU_IIpcHnT4Tegtysm_Bng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTCJIrF9wK7X5NS8ybHCv-JLTbBhJAdwayCjaXgRn5dxGSg3n19xWrDHOM5q-yc78AFTbA7a2BLFeJLdxoPRiIROdo9fdaFS2HCIWXN5sugbqW6ttOwikLQ6B34ow6xRWISqLG9tBqbyrhV-G3Xp8Q8qzf9BsHJXaKZ18C4uni9KVEWIrosHQjUfwNZV27abC-tORZrt2G5-pgIbRZ4uxeXTNz7FTh_bEIoSO783HBTAufu5IHCTGhFhL56EW38kGz99qcwyMWNlEKRmTCFp3IjDgjdfCC7JVVYoeZHUzuFn-kJEvJzSFWxepg8cTUwhrR4B87aPyEDXjn1eA76GGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=g6_Ek09s0Y_kxfu3YiL0zpYAhEMXBW-lxong_cPM_7CLCawtQgoHI8JId57lAbJNcftEFOxEomdbnSHNx8Mgu888DOAZhUJJ4B0sCNHTCP-TXgFWIMeecMNdBfMZBUtDGM68HVY_v0v7z-gJYUIppVOUWY4OgskXsjJcbO7uVetmFP8hwe3FpFuEUHe1lI45w458jNp7RZ1GWfQ4Q5TF2b0CwchIqy2NbrrYc1Xl05Cvji2ejyYd98WUtA4Bwk0imPSqaCJOxQ9OP4PGZjpPi6YlAgdCQrm9eQCEnBZUdK5Lzq8bnTQT18E9tU1-ceyxzKQjVgO4r9d4CxSkr9Zh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=g6_Ek09s0Y_kxfu3YiL0zpYAhEMXBW-lxong_cPM_7CLCawtQgoHI8JId57lAbJNcftEFOxEomdbnSHNx8Mgu888DOAZhUJJ4B0sCNHTCP-TXgFWIMeecMNdBfMZBUtDGM68HVY_v0v7z-gJYUIppVOUWY4OgskXsjJcbO7uVetmFP8hwe3FpFuEUHe1lI45w458jNp7RZ1GWfQ4Q5TF2b0CwchIqy2NbrrYc1Xl05Cvji2ejyYd98WUtA4Bwk0imPSqaCJOxQ9OP4PGZjpPi6YlAgdCQrm9eQCEnBZUdK5Lzq8bnTQT18E9tU1-ceyxzKQjVgO4r9d4CxSkr9Zh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=ubatK5iQEQs4Xrm9bgtXZ_lCVjaoDwWUQGHx0mtmDw7NjGup56ZP7JzWWvyMCMU5cbbZZi0ZoAnPvVdBisdxQEB-e4LlqHOx7w9HOPpE-Jc4EZJZ8d2UghvST0Jl6hHBRkgC2bVtL30Nk-YXoBGc2HChBRzRhD5n-SjOM-c5MN16_yF9xKs9voZLZIhNl5Wh9UGnpMIxHgVKrzbUuT0G-j-HNXodRlFHOUw4OlonYLAzBnZgpIf2P0I3LkwgI_EVNgykeoq2LWPzWFaXWf8INJuYm3Lu_eKErLEdqkRDKePSHfrpMsRFV52DPTon24VdTqch4BYw-SJ5_MVULeeFGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=ubatK5iQEQs4Xrm9bgtXZ_lCVjaoDwWUQGHx0mtmDw7NjGup56ZP7JzWWvyMCMU5cbbZZi0ZoAnPvVdBisdxQEB-e4LlqHOx7w9HOPpE-Jc4EZJZ8d2UghvST0Jl6hHBRkgC2bVtL30Nk-YXoBGc2HChBRzRhD5n-SjOM-c5MN16_yF9xKs9voZLZIhNl5Wh9UGnpMIxHgVKrzbUuT0G-j-HNXodRlFHOUw4OlonYLAzBnZgpIf2P0I3LkwgI_EVNgykeoq2LWPzWFaXWf8INJuYm3Lu_eKErLEdqkRDKePSHfrpMsRFV52DPTon24VdTqch4BYw-SJ5_MVULeeFGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU6HGrxDmNFeRCzW6scH7xwt-g-L1wObB0TseqmFoXRP3rCQUUEgpSYfltEEoKHAR-HTrVfAr2g-3keJtkhu0pwCXFDYna5dmKBed8l_vlSr9yQxUpVlGsWY0QyKzY10CU5rN10pcnYs4T20svX0I_xtik1QxlOtTSmf_J4hThzGInQaErBHakLmMqFBP4KbZoSix726Y3tvRhw0LRMRItbONAXI3XYgdtfKWQgocva5U0LrTH41AhuX6S6Up8z0FO8cWExw6XYeuLCG4VOZzcOP28kd-ZoPeHuoAdFq_7bay1CT5WsZ0_bdd8l_pm6SE0FbAyQOioewc-8UmN-kaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=SDhNVBq-R1f8lTOYUXwN9OH3ObZEKADkwhwteUgC55bSHa0pElSvvdX9pMOhMQ2cXr-qfOkKUpdvqVlspHujCocHnj7Gg5GxYvzo9DXphuDMU5TJ7YGQ85Gsa3P5uLzmhhpxdxG3ktzclXoEFz5g19I2eSH_pijiiRqvxlaz8JS4mkUk8K8Qq4yj5K3WDD-8nKY3f4kBCmUkYRIruZZoXVCHGtjcpIydO5AFsp2LOPnnBaQMW5aIfXtJ8GZhDY0LwahqGI3xAX50qQkkRFVGBwshrT2qLD7N1wbNN0e_JrieZCaQXWa5OzQ8Oa9MSXelR1txPYr4bwEr3ViP4tGtCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=SDhNVBq-R1f8lTOYUXwN9OH3ObZEKADkwhwteUgC55bSHa0pElSvvdX9pMOhMQ2cXr-qfOkKUpdvqVlspHujCocHnj7Gg5GxYvzo9DXphuDMU5TJ7YGQ85Gsa3P5uLzmhhpxdxG3ktzclXoEFz5g19I2eSH_pijiiRqvxlaz8JS4mkUk8K8Qq4yj5K3WDD-8nKY3f4kBCmUkYRIruZZoXVCHGtjcpIydO5AFsp2LOPnnBaQMW5aIfXtJ8GZhDY0LwahqGI3xAX50qQkkRFVGBwshrT2qLD7N1wbNN0e_JrieZCaQXWa5OzQ8Oa9MSXelR1txPYr4bwEr3ViP4tGtCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT2OlF8MVZmrcAuEzUGiBam3SLzpZId0e-2Gel7cxwnCPUrpDUFlH8tTVcvPrDSMh6-KwvFw2EtZsOyKNtdxhWAoUemLCwajmxFew73xUsiCsafYMXo64NpHNz4hL6DtkzvdmHIpnTxOFZnZQHJFJHKb1HEpcbHKZ2chZpQDNjXgoBkCyx67hB3raCPr2w_a1qIycblK5Uocl0x2X8VsZ6soERsC5zaGkAwgG0AEWXDWpaTdPgf7EkcbGZN5tfF0szTxgLRpT1br9ZjJT2uBYtkw3q0F7sbcuSK013GGwb7bmHx-VU6SngWZS7aui650SJIT_RX205dD3yteXr5PQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-HsdfJkXlJ-7-9bzLHjsaixdOdtUP8VxQBDjhZRKnDFNgvPJK3oxD0QLadUlLDT_9CEuxcYUEvYlZbsH43mQCJJIj7Z9dgm2V9kY9B9dFvBeF9Re196ioh7dkt1ikselsfzdJHni3wcy6br4wYDToVFX6RT6fmkiPj47gEu94AweHLwmqzV6ZIegMmVvAA3BMM9gEfwsnlKxYnJPvIy7pGAhij4VN4ZuLIDPZuOua1lD40ebNGqtrhnkn9HiMBUQwxEmNoUjlXJTwZ9UPETYdPk8vAC7B4gKY6VJ-YReEND6hNfJKOpCjkGfbKJvKx8SOqQbTDnKDBkuQ0LPGac7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=rwlfrDZgBabz6nd_erg_M3vu7wh3jUdH7ywXPwToO78LBkGmBV3WNrJjU8-A2RBZvfAhfwQZVaIAS-yHAISDeOMUwWUO995fPzWpQdc-6cSIXJkEvHeITBbVV60viV-reYqkl8RP9qqu9btWk4GZYZIFTO15AuEKU5KpgwerRFSpLdh3VP7zAxUfisHBukFeVbB4YtxSwVHOQrlfmyCNjvOxOVxJXineaAQQWmyytJWCuFFcGKejd6BncrsFXp1zaYB_xmrtaJ2qPdU3T0ttsmuiF_1Z-8YQUJ_8hL-sk5OPi1YyQO586l4IMjVYL60lQ8H8GNyO1rM_fXQeAjCHBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=rwlfrDZgBabz6nd_erg_M3vu7wh3jUdH7ywXPwToO78LBkGmBV3WNrJjU8-A2RBZvfAhfwQZVaIAS-yHAISDeOMUwWUO995fPzWpQdc-6cSIXJkEvHeITBbVV60viV-reYqkl8RP9qqu9btWk4GZYZIFTO15AuEKU5KpgwerRFSpLdh3VP7zAxUfisHBukFeVbB4YtxSwVHOQrlfmyCNjvOxOVxJXineaAQQWmyytJWCuFFcGKejd6BncrsFXp1zaYB_xmrtaJ2qPdU3T0ttsmuiF_1Z-8YQUJ_8hL-sk5OPi1YyQO586l4IMjVYL60lQ8H8GNyO1rM_fXQeAjCHBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5_r044ELHUkDAcz2zJNWFGI7V5V_QsNL5PU-hJsK5fgA5dPoIrTgcwAUqrRbogjSXR8GOdMlNkhry4qJsbLjiwurjChblqTnn5q8OiJ7yp7aoaQeYImT3JBrnk12T9yyzSd9LyBBUyciAYvY7KcgGoDCqp5dX68eeOiDWp3fM41ZJO0AmknC_fozKptTrfO2ftrCpBqAL5xInvu7EliDxKc3nmH9gEYFLDnm5qOUyibKv6V_JTVIr92HcmG0aXYHW3QCaEIyhjXwW5TgKdSbRzuOhbGOAj89swftHk2M3oNIuKbqj1gx0b9-3r1gjaHFknkiOwotVA3ZmB26P7-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bQDskjYqEcxnk7j0qSDxOgJS1wEuXQjyB75BD0zOeYaw-UTRnvOSQNWa2aqOFet_OukPyhvZLDCCSe8eoiqdNl5ARd0NMT8HFm484G2BKJAcycNkovSn85DyeXs8BxzvvorlprWz_J2BTL33o4naMXWfEnhHFn74FxB3GH0yiuryg-e7EsBbY-8xUxvh0QJthmmPYTujwm_j29uXld-nIK1Lz3q_hHPts24QsTU0AmdOqxw6GkILWXtyIMBPKbLAbRzk_y_v6Q5kFi4UKr_2r_mpTn0NXNXaieuvxg_s-lh0h6YE4965o9eRXQSzBoCSz1yS_H_eL9NlHQSYUU0-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ja7m_jAkmLgNcoi0VpuFZAxG8JFXpI2U3TZWQEm1dRIm3tZt8ipQv3ywg8ax1NlmCGOol2FTKBtqhZ1Gv9Tq9ngD5OCDCrNPYFxilRRY9jEfL35z_7ma1a8Pfy2PRr_Jbdu_mGRESDpjhxxDzCfvlLNW3b5YtsdRYrtIl7nsEfH9ZR4AJL3ifoXcUTm_bu6Gb2crPBcxoSB-AZ0T50FnLjo0yJJra05C8JGg-Xf5xNTfQ7r2YKXZWP6cODZAyg32RsZQr_RZE8pp-Fo2ISE609MSEMxP65PBSE2ZYJkXKUDgz3hEqxN5iwQFDTImUyMN1nTKpLlwx1OB6gU6tbx_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bqS4vzAAqgxtqsWgCCxswLO6C57y5-Yq6dNsZ6Zm8hI7bamrQDnD-fbV7daEzTUQ0IkkOHnKeUhBhZ35lFkJIFXMIHLStP3LV1g0bc_22cGRkYw4Y_2ajWoXUURhM8LF7rRMCgCukFnjPZbMXiSu-uV-ZGb8bn2kT5PnBYq77yCUIOjTnzbCj983YTQjUQqI7Q4QOXjqrh-glYKphhG0GBTeGwyY6pVhxyh6bRlr93WcdwRly9MF6YrRyOLhCyBUOyU2eitjfFrGz7GOTDTafAsUU6Q11zUVjDnbl6BUrzpZgfuBO8eqbfccwOiEpw81cxbL6qDsp6tfK_ZAlJH96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JP9ih1vyD2GRQLLLwoh6w56qyUyC_czetc5bkyMDJ4In099nbpkd5_km1avUIg1ZfyZtj6Yx2UYK3V6YroAW3ZDjIbYeQCnKC0aC0w3yi6dfWVtRg-JCzzwDD3vBdHKlnEoWDATmJn07eXqXmmJjW9WQc0iDYCIzXB29W80zWVIthGA2_YIZ4sdBakLg97_vQQA19EghcLDsU1QcGI9QyRHyM2CrIW8pbG-wjt-Lv1p4B5ZiWuDaMQhGTcq5JcUFXwRyj0L77Mfz9wfwVmY9_VYm_IxCRESg4c3_Cy-9hVczo1B8qXl7526pX9y3xv9LEgCUdo39jYu_imxIywji3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PWGuGKLSZYPVx00Qk2wpfS4yw1JQvMKe2so0odBbWI1l60CFgG5q_BIqA_caM4BEy68hnvIuWW8ZAuimM9vjrDLPZwnWXZ-rmK2cFxvFKWSnsvpbpuI2-dI5cfwxULyUwLwb_B98W4I-vmCyB7rzlYeZOomKWPYk9rCAL8fZBQKib8E_VeEQ2hc6Imb4QSTX8DZhLeEUcbaJwI6Scl6A_8GZ15qBKO3P2Iq2Xu0PvDrVDPyFSj-9d5LejosJsye53IBrUSf0UDz1KGvhcg2UHD7fPnwvrP0UtpWM0-pO5JsUe0VVQ9N6sYTxNPZyf-zIGp19QrQnPI3R0p62E60n9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP-pg3NvJtBzECsN9jI2iTUiUZ1KCu--TEff-BYcK57jjpdQYy1KGCjucXhyZf0e5rGId8FK7lAPY1kIR6zBp2ze620ECSd8fauQH3dyiEoX9piaGtPe_lEtRLQNFfpKWu8jFStbCPVfhuBCdmzHjEv9bxOWIRkeeFiLgIJ1qPxuJwon6CVJNCf_hFOObBzxfGK0P2HMDK-7z9Cul9EEsg6j_SBsanF0n5ZVACZUmC6V-OHFXZ2tkBbcwb5SUaw7RsIWm8UD0c_Zv36d-xlz2pemfVZTmXQkk8Gs3OaThxgIWUb5_00GWptuYX_nZ6sbunspuvG4TsDbX-Uuo1G0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LYB3pXLkXO3ZcKd9UUDqzUprq-PJCSub0uHAXogsOBVd7UnobHyqr_gy12czqTv85agL3uj0EP6qA2ShZvD6M1gAGSA4zFql0H02PxIHNWuB1ra19Q7apWBm_kN3qt7am1aR8dG3ELWT5dcFwFqhNWPJFVU8Iteipf2j7iRJ7L-liDQe-ma6Icynud9c9FqNVyeHTL9egRkxndQnzJ0Zo1ZuAofPwd5wp4-siGJmfuXO1-a6IyA6HVZwz4-LanrEqri9rE80lL4nIlhRczEh0poquOubz3KxtjMidj_cHYSe-jeBPtJVSQkOSKxmF1MkArzfuE3DGUJ2VDeyqMLrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=gvCAQL44LR_RuU0p8EoiFSvhN2mxJyylAv0K82OATxjCTxwOMx7POsp0DRoRIL9cN56qnvlgzEucHP00IXEnuDB6KmIKgRLC6JORaxJ90G52n5pdGE2BCO5aGgOhaAHuV94AkHsvM8KNaPKj2Rb9gvhxF8dR5DwR71ygMVZkLHe9ZKpUx9O7R9zPf9dCDqi1bJY0WoRLVPrjrYh_gUWYm--X4LeKhIZsGDuMtauqlZFBAXwfxN55JCoAnX10PLBPC4-3lvy_cXZkepJrcBdGhzr0nRTmSMRLIU1nZQDcKHN-rKCQWTVkmvAUmh-YoFXtaB3ZhY9RHT-FhHEmiYRKPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=gvCAQL44LR_RuU0p8EoiFSvhN2mxJyylAv0K82OATxjCTxwOMx7POsp0DRoRIL9cN56qnvlgzEucHP00IXEnuDB6KmIKgRLC6JORaxJ90G52n5pdGE2BCO5aGgOhaAHuV94AkHsvM8KNaPKj2Rb9gvhxF8dR5DwR71ygMVZkLHe9ZKpUx9O7R9zPf9dCDqi1bJY0WoRLVPrjrYh_gUWYm--X4LeKhIZsGDuMtauqlZFBAXwfxN55JCoAnX10PLBPC4-3lvy_cXZkepJrcBdGhzr0nRTmSMRLIU1nZQDcKHN-rKCQWTVkmvAUmh-YoFXtaB3ZhY9RHT-FhHEmiYRKPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامران غضنفری، نماینده مجلس شورای اسلامی، در شبکه اجتماعی ایکس از برنامه شماری از نمایندگان برای «تحصن» مقابل ساختمان این نهاد در اعتراض به ادامه تعطیلی آن خبر داد.
او نوشت که «چنان‌چه مجلس بسته باشد، تا باز شدن مجلس، در همان‌جا تحصن خواهیم کرد.»
شماری از نمایندگان مجلس به تعطیلی این نهاد طی ماه‌های بعد از حملات اسرائیل و آمریکا به ایران در نهم اسفند ۱۴۰۴، اعتراض دارند.
حمید رسایی، یکی دیگر از نمایندگان مجلس شورای اسلامی، یکشنبه ۳۱ خرداد با انتقاد از ادامه تعطیلی مجلس گفته بود در صورت ادامه تعطیلی، همراه برخی نمایندگان مقابل ساختمان مجلس جلسه برگزار خواهد کرد.
حسین صمصامی، دیگر نماینده مجلس شورای اسلامی، نیز در پیامی جداگانه در شبکه ایکس، نسبت به ادامه تعطیلی صحن علنی اعتراض کرده و نوشته است: «بیش از ۱۰۰ روز از تعطیلی صحن مجلس می‌گذرد و نکتۀ تاسف‌بار آن است که در سامانه قانونگذاری، امکان ثبت استیضاح وزیر و صدور بیانیه مسدود شده است.»
انتقادها در این زمینه به خصوص از سوی نمایندگان نزدیک به جبهه پایداری با پررنگ‌شدن نقش محمدباقر قالیباف در مذاکرات با آمریکا، افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F17QZvxP9UgBTWo2kE_ZMu-0Tm7OYRSq7egcjXGWprmIVfX9OHvYLFfz1wtOiJ4toDuVNOLhdWg9bXlxvHiGif6juh6jD5d9NMiimY_25xXRl-AD4SGUsRgTHnYULVnb2WqkgaQMdEg-mW6KuUTdJU9sgatmCV2ajlmyzhuvkca7c3iy0AJtjQ5OO7kPgm1RfWgZ4aCU-x2ByLGIA8ptAAiYRS1DpIyiadxHC_ADg81U5HmrooTfcpu7G78-45vqOjVbEEKJ56j_fGF2VWboj4STKO5gQuX8op7mXeyxYA-_9PrjayoqBaLGmLl636Tz-78vyy6CPzgrPcTlxe0g7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IvSvj1vxa-EETvMOvCN-Mxo-Z5DahfWmGJ1r2ZnHOcbraI_130Xey8ki-g7PDAHEuDZqhPmWk5sQRe45kv5jnAJdC0deE3IPg4tNmwd6kHXZ_2iUpmG6zZLcpUDryBFiU3t1c3QD5XZsdPgX9dMHPVNX2c-PWYi0SYj_MU3AfcRJOfbQ6pxQfsqVnyLNNjP9QycUwzydbKYEwbkDmTzv4ONp40MU6sr9HW3dlR48esPX9nWdtZGZobRBwmb4aQ8ww9Xy0lyWdgf_NVH6JyCyzpj08ELE_C5aHRjQaWXU8NiXxrAEVGvwHkGXEvjLN2L1zuDfSPfhAp2sJXMCmAIvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=ngzWEpkcJJ193ucMcQK8E3aWFW2H5nbDD16-O3H8KcAESTcV8TD82DXcHfboLQr_zaFcKL7N3-5REr8oBCVN8jUaeShduzax5pXL1uJMbstjy3GRQC30NrYikIkXTimRw8Yv7cZp8TxXKNY8lBbX50JXxhJuz8g6oK7PVbBKJP4eGiqnX582Fj8N8fTKVZorGlo0ASNp7vnjqMtfBHXyYLdPOeHl5Bw3vBdUsfWlbgB7nMtXyB7cMN4S9mcPAJDKFx-tW5UI7k5GwhiS-YEVRGyDJ1NO9cMPXLaNqfhgHIVRHviT01Hc6Nc8X2q8orUnobYiDHcDWTIpEe2ZBl6nzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=ngzWEpkcJJ193ucMcQK8E3aWFW2H5nbDD16-O3H8KcAESTcV8TD82DXcHfboLQr_zaFcKL7N3-5REr8oBCVN8jUaeShduzax5pXL1uJMbstjy3GRQC30NrYikIkXTimRw8Yv7cZp8TxXKNY8lBbX50JXxhJuz8g6oK7PVbBKJP4eGiqnX582Fj8N8fTKVZorGlo0ASNp7vnjqMtfBHXyYLdPOeHl5Bw3vBdUsfWlbgB7nMtXyB7cMN4S9mcPAJDKFx-tW5UI7k5GwhiS-YEVRGyDJ1NO9cMPXLaNqfhgHIVRHviT01Hc6Nc8X2q8orUnobYiDHcDWTIpEe2ZBl6nzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه دوم تیرماه بار دیگر تکرار کرد که ایران با بالاترین سطح بازرسی‌های هسته‌ای از تأسیسات خود موافقت کرده و این بازرسی‌ها «تا ابد» است.
دونالد ترامپ در پستی در شبکهٔ اجتماعی خود، تروث سوشال، نوشت که با وجود اعتراض‌ها و «ادعاهای نادرست» ایران، و «هم‌زمان با جار و جنجال رسانه‌های جعلی که هر کاری می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند»، ایران «به‌طور کامل و تمام‌عیار با بالاترین سطح بازرسی‌های هسته‌ای برای مدت طولانی در آینده (تا ابد!!!) موافقت کرده است».
به گفتهٔ او، این امر «صداقت هسته‌ای» را تضمین خواهد کرد. «اگر با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد!»
نخستین بار، جی‌دی ونس معاون رئیس‌جمهور آمریکا بود که روز اول تیرماه خبر داد ایران با بازرسی از تأسیسات هسته‌ایش موافقت کرده و این امر ممکن است در هفته جاری رخ دهد.
با این حال، مقام‌های جمهوری اسلامی بویژه سخنگوی وزارت خارجه ایران هرگونه بازرسی آژانس از تأسیسات هسته‌ای را رد کرده‌اند.
@
VahidHeadline
پست‌های ترامپ، ترجمه ماشین:
با وجود اعتراض‌ها و اظهارات دروغین آن‌ها در خلاف این موضوع، همراه با هیاهوی مداوم اخبار جعلی، که هر کاری می‌کند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهد، ایران به‌طور کامل و تمام‌وکمال با بالاترین سطح بازرسی‌های هسته‌ای برای مدت بسیار طولانی در آینده، یعنی تا ابد، موافقت کرده است!!!
این کار «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این موضوع موافقت نکرده بودند، هیچ مذاکره بیشتری در کار نبود!
بر اساس این موضوع و سایر امتیازهای بزرگی که ایران در حال دادن آن‌هاست، من موافقت کرده‌ام اجازه بدهم تنگه هرمز باز بماند، بدون هیچ محاصره دریاییِ دیگری. با این حال، همه کشتی‌ها در جای خود باقی می‌مانند تا اگر لازم شد، محاصره دوباره برقرار شود؛ چیزی که در حال حاضر بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که وزارت خزانه‌داری آمریکا آزاد می‌کند، به حساب امانی منتقل می‌شود که تحت کنترل ایالات متحده آمریکاست و صرفاً برای خرید غذا و تجهیزات پزشکی از ایالات متحده استفاده خواهد شد، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما.
این‌ها چیزهایی هستند که ایران به‌شدت به آن‌ها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است همین حالا، پیش از آنکه خیلی دیر شود، کمک کنیم.
گفت‌وگوها به‌خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد؛ رکوردی بی‌سابقه در تمام دوران. قیمت نفت به‌شدت در حال سقوط است و جهان جای بسیار امن‌تری شده است!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ojApWp5xtJEwTsQbZH6hQMaXM2VmbZVCoGf9EXOo9DJCm815gdWmrmXWWmb5HpYy6kmf9T9ZZSI1B3k_YVInL6cFua8ZpMb3xEFIGDBGWedvYDMlCa04CzQp68dMzkJ8Cky4VEnH0GFzTFwauewjf9ZPTWDShtHlQ9jZ8fRU9RNFv-fcK0XdvUavvABFJ0hiyjxHshAliDYAUkGoD0dUGBgypdXbJ0i4bTOtgtkEndo41bkSXqaltKLJRlFSK6Li5sRifb9vTcaKjN7cUu6h-KvlOyCzXMWnQ4rZ6ZMSU7IMKioZCrxkmXpHlM6G73e0_iN8MYGZxhKl6AiXLxfWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت  [نان یارانه‌ای، نان یارانه‌دار] در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
بر اساس این گزارش، قیمت‌های جدید از سوی استانداری ابلاغ شده و از امروز روی دستگاه‌های نانینو در نانوایی‌ها اعمال شده است.
بر اساس نرخ‌های تازه، قیمت نان لواش به دو هزار و ۷۰۰ تومان، بربری به ۱۰ هزار تومان و سنگک به ۱۵ هزار و ۵۰۰ تومان رسیده است.
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران، نیز افزایش قیمت نان را تایید کرده است.
در ورامین نیز رئیس اتحادیه نانوایان از افزایش ۹۰ تا ۱۰۰ درصدی قیمت نان خبر داد.
بر این اساس، قیمت نان لواش از هزار و ۴۰۰ تومان به دو هزار و ۷۰۰ تومان، تافتون از دو هزار و ۳۰۰ تومان به چهار هزار و ۵۰۰ تومان، بربری از پنج هزار و ۳۰۰ تومان به ۱۰ هزار تومان و سنگک از هفت هزار و ۴۰۰ تومان به ۱۵ هزار و ۵۰۰ تومان افزایش یافته است.
مسئولان صنفی افزایش هزینه‌های تولید، از جمله دستمزد کارگران، خمیرمایه، حمل‌ونقل و اجاره‌بها را دلیل این افزایش قیمت عنوان کرده‌اند.
رئیس اتحادیه نانوایان ورامین نیز گفته است اصلاح قیمت‌ها با هدف ادامه فعالیت نانوایی‌ها و حفظ روند تولید و عرضه نان انجام شده است.
این افزایش قیمت در حالی اعمال شده است که نان از مهم‌ترین کالاهای مصرفی خانوارهای ایرانی محسوب می‌شود و در برخی اقلام، نرخ‌های جدید نسبت به قیمت‌های قبلی نزدیک به دو برابر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IxIMmR_6BgbUJSOaxWvZgmYsH2ZfXfs1mV8Dg46kKa1BpnQ9lI3b92zaaHh1y5ktxE7ikrQtCxvmChecjAxXQA34m7cvswd5_9ea5kxN0ZpkbLFVIOWUHtzwf9hqhqvK8iPvPRkfZprfZHGtqglzx0obxWKpC-87keTin11dJ_FsJ-ZIOcZHoTHO3W59taQSZEhwZyIwh4ecNJ9T8FB6h6wK1Uab9mylKT6ZmF3w2Q6155JMBopSWQqVd7h7INSoFqU14KShUZJgdsyVG2tuMdQOx69J3DpW3Kxril4rorPw0LbapBFgbmJlwyC88DZ4XWtSwjb1Ag-2eQo3O0Um5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HHmnG9EyDcBMApT5-3y2qMdupC6pZem4oadxmc11gWCd_fWT0jpWdXKzt9H8WfoSP3Nh0hv-6xx8qMm5EOZ63ElaJeU4-EBOTG64xzeTrH746MPm17rvWhICjCWR37KUzEucJbknzfRtUsbDDSonTnEWe0ET6-g_N6J5SGvFhGJx78gWoHAUIAjTO9aqeWs45GtU-FUppGJIeHe2X4hJ4Ccq3XqAggd4VWKcD3dbQQMZQVOa2lGM2mp8fGqCSyiqcoxGSV0atp_Z4vVgiFxT_ziVPLUZzcNHnpAbkXNDZZbqdUr8P5eg3tnLsY044GxRVl1hzxiHGoFmyd0qAHfCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TBU3tV9_K3zIgThnVZ4Dr_ThzGVZndOyWqUJyTfeqVd8cnS6pcTVFmFx2m6_XUpddc8btTHIU7TmJJoHwpfKn9XraQELCH1WV83C87OV1i1LFGqt-Dpq4Q_gI5y4KKwjlmJ1ezDisin-qlCRm3mX1gEMD5S-w4yVjXlMLLMHhPkNb_KqIQEDpQQ9hX4yS5904cm2IEN0gr6XLBC5Tuw1U6-Jt2Tp445XqRuZYPSdO5-PykeitLuzLIGI_rVlmFTt5iXQ4yIbeeCvBM4Fsc0f77UeHOZ96WXhWeofcxlXK8oK35235runOtQ5Rw5K-enWjLNMC2YeDu6djpz-Kxrq5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=aUnLwqXN25PCnHssBU_3_4kDoQlzEjnwxReYpBgkV7M__fs-WV6jyNLPlBzzJRJD0x5JU_nqYz7TB6QWUNqn7yZgrXwCt1N-ya4qUpSUpIep7ljnDGZ2KhaptGyY16yOUMtF46cqPwycgYoImcZxmwxEpx7ZsCWTXf7aygFnnxpKpaKmf3e1ptr2-zp_3qhxrc9S-JK0FUtuoifz78O2Ie7_z71D-ZHU6BUp6MytysRSVauyTEOW1VDUXlS6ugnwAiFc6giAH1WDlolHisNbEdmIMAxqojobNyIxiKIbJju608Vgv2WWDujRwr4mF7mNvpaxaiIyAFXVLltXsPXTmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=aUnLwqXN25PCnHssBU_3_4kDoQlzEjnwxReYpBgkV7M__fs-WV6jyNLPlBzzJRJD0x5JU_nqYz7TB6QWUNqn7yZgrXwCt1N-ya4qUpSUpIep7ljnDGZ2KhaptGyY16yOUMtF46cqPwycgYoImcZxmwxEpx7ZsCWTXf7aygFnnxpKpaKmf3e1ptr2-zp_3qhxrc9S-JK0FUtuoifz78O2Ie7_z71D-ZHU6BUp6MytysRSVauyTEOW1VDUXlS6ugnwAiFc6giAH1WDlolHisNbEdmIMAxqojobNyIxiKIbJju608Vgv2WWDujRwr4mF7mNvpaxaiIyAFXVLltXsPXTmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O9uAS91epL6_oQ7tIYBurBZS4n5CmK3f-4guJMmWVZC-MQT3zj5Desp2lisFBxSc59A4M_BsHTxNEg_E0x2oIiKga48A-t6-e38CjjV2X3wHXN59-ctazTr7K6SbgRw7TWzfzHFbTBkceT2vSxFt0uy7QU1HmRO-69a6vGo76lqrCm3tAm_B16QyLTG4syjOxHASC4EdSJAngkI11fsKm6xO-AjYAsdFmUsUxS6Wzt4NoMXlt-Uj_tt9cASd6iZnfW8wWa1xH5eo2SD9KgUAr5xHOnEJkE4bqTH7i-HbBI11-CoL2P40IpDKB4BP16jr7pW823S6CMGCTUEuYdPCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fLcmTCt4MqHPDyexflRrcDqblSBevFycXyuPpJv1-TMkn-WPBkYoZCCxTaRUJOAJV6MdOC0m5WRtrYJhtbLBcphc1KBp01W03BMntRU9AjoI6l6B8uLH7wa27IoVJuijp-3Y39FjqcFByxzOjppf38UqbK8wmzOOYNzFUjvnDStcJfY_s_IC5KUQ2PX0UGHHrF8snSF3qNbtW9V4dzO-M3l6XLY4DjnE5sdcvpjdDAdbbXEQenDP1MVswJiYezRPcGNE-Zx5utGU-oVazchrWHQpMhuE8DIJQv7u2MF4xN-IhZ9OI4ZdW3p3tuMTZ3LQFyf-5ZdtSO3TawPqhFnVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jwwF3ZxU63rOJfZ-gcW5kGuvDLuVCNBjzUGsq5hyNSTBoyIbsQA84ZbsM35jW5Ir6mcs7LSYAyZxWgO1WEvWGyFONBYGXQ7C1KtM6hFy2jBMpIS-e2pZaLxthx4t3YM-qopRONu08Pw3gyNgJiTk4wh2Tq6ER5sRFTM6b2yDJAOXP3im56SQ1Kk1FJ8XFlrstPi4nvHuATqw-7ZTxdx1FmnOTZQ0rhM-79l3YRnF-_VWhzX4TOsR5p4pCkItHbKwGXS6-_0meF6PgHQUS9dXVAUfU_Nn5oFlwJcf03oDgxXYA2qF07tNBT_bAF2gUGOekBbALLtAWi5BzKot457aVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RsqkTKdKpKNVkdFWZq0AhqRC2iI4pISaC5-XD2_DggeVEpIYGYT1-Ks663yC4-C331r1rA_uLvTfLLT7E-VBJCf5g0VFQRBA75nu95-x1UUvlcb9jAeJHPzCTzxZ4C6ANHRwI9WPGm4o-fFwdjSojtRmNBMXGxBH6cmwkfb8V29yuQz9tQ2z0esiEvVXOxZymh0NilOb0u9aiyy6GKlkb8XkidFa3WxxqkOJezK2W7eVrxo_XTm8ulm7oQsHYQ-s6kY_seO004q7GldB8dLF3UgLJM8s6RHdVMt43WouatJCsdkASNJCB8wr-N3UH656SwGsK-Pct0e2IHGIP6R2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/davWpWtRvtLk4zSP5Vts1KAl2YAQgm0NZYBpfUda_xryDAKwBiR7xlytmGUEh_vYhbVSPWwBU1shYSkNY2yNY3YKy_EhvKRSYagM0tzb8iMzumsIWnuKK25nUfUbe7Mf4tnHYJrt-wMjSGf-ZmZ7AaQmJKYsjNUsZ98EGOyTVaCcoEMAFLtlk3o8PLFeNtyIKzFEGcKPjKQUnW0J1tyFInCm8H1yCDhuR-Bp0IR2oONUegYafallk9x-7DsGL5PW2eEIgiN7IXywNbdxGzWKNoq3w7O2dl8PaSMmYlKlpXBngWMDsWa6VfDmjoFzkezYsNBLiKff5NGDOez8ndMQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XjUwbRmxopVkqtx2YkjfQwXgsBDQ02NEHGe_P5B2x3Jvc5d2hNjIBeG1MSQ_ktzhYZACUjjmFcJ-wkeLmdAx3Vs-GwME1XVeVZ0AnKp5LBOjsQH3IECoTVdCI8KAOUEolTiOSyf_cAr8mAXePsgg96N_Hk0j9BiaE-K4MP-0e4OhHpzzsqlh89xa9jAvCWTo6OKtBrUKc_TQmxN9Epzyb_Oltnrw6o3VgscpW-fUUDViPGtae1e-LkzoXMspeW9NJHiSuMJNSCQFez_0ULCkSVOqI2D_xMY3S-GP-qN1lD2FtJFGMfCQTtkj-wD0X3obUhNZ6qjSPEM1aj-MFk3iiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T_rDoSPM96hnqyKetFpAiEJ8qALIdHwVWRUF0HNi_nszR-CUHj3ytg9GXA06XjDmrvwaz8Iaztf4OlnsUzBavq0_qCTCICHaNSTbbjV1o4saOytzs1YINXC61dDO1RsUJU6jK_1bqD17zKO0hIzeYbAx9z9lxCYEQF35hfTDXHJ3ypTV1_cNO5Sz0bRk8nMr7IDqqQyiU8eh71VTYhFBfe-Zl0rL1NKngqMxo0j9On9rqV0B_Mj2gDsiKGjomfyY8swUBLrc4CDxbT8g7YJOeW8OghesDyeQo8m1jE84vNWbvUU-Tg1TVyn75LJkdnn0zknP-pWS05L4JEkjXd5YkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TV6oBnl-j3cxv9fNvelqZaLah6eouiPc8KbVek1F49Ux0PKNOaLmnM9jzO8Hu1-WcwpiKlvpuTXmr6mkpvcz8uu64lp9-mjZaq2Lb9rRjRs-RJ-e1ZLNv5FnQXUj2U1ZafOJQYAo6vr__hMnEqfEgHvtrXYOVpa7YogUrYe5rBkjKYA6mAdYhwlPNaEI-mXbG2JopK8f6x2xsZaJluWQ4rYlNckhCevkpru9Y8iWZYxsHAqGwbdEcN2xiT8EJPuknpUj9vBI9nnHy6PpHQamsvL-bV1cV5Xf9TFIixKxax2Z--9Hj5znH0sCamFKyEiG9zNt-C2ghJ5bAqpHojMmkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد + ترجمه ماشینی
دونالد ترامپ، رئیس جمهوری آمریکا، دوشنبه عصر نتایج چندین نظرسنجی مختلف درباره توافق با جمهوری اسلامی را منتشر کرد.
از جمله یک نظرسنجی مشترک «سی‌بی‌اس نیوز» و «شرکت یوگاو» می‌گوید که به عقیده ۸۰درصد جمهوری‌خواهان، این تفاهم‌نامه «بهتر» برای آمریکا، و یا «خوب» برای هر دو کشور، است.
در یک نظرسنجی دیگر، ۶۷ درصد می‌گویند از تفاهم‌نامه اخیر صلح میان دو دولت حمایت می‌کنند.
در نظرسنجی دیگری نیز ۴۷درصد گفته‌اند که این تفاهم‌نامه اثر مثبتی روی نرخ تورم و توانایی مالی خرید مردم آمریکا خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSn3xYE1eXCFPFUMebEP5ZKu-FYqyRGtmLj-wJcbYV6fiedmSnM0uj8SEyAD2Arj8l_fDpWGkIQX0SUIufITgnN1mRshWsHfr3i1KQZ86V24ZN0VLVXxwi_P36_6AzJ5IAf2F_LQx_lUXbLJJd5l5PthPZ1Ic1hKZCElJKnUzhuAZMQTKTJg6vB9bmwWRSWKF97Gq5u4Mvqs0iM0QtHesbjvHLHfOFmco2bWLXemf9v0HNGxETx1IbF3H_0Qc-mNejOUihXNx0_1Pcc6kXffOHPqvvdn3HzYrpZi-PGSMISBHZ1_ndt7DawmsYDufD5SX7g42F12Wasqwb54uDnnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.  ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ویدیوی بالا:
به تشخیص ماشین، حدود ۱۱ دقیقه از نشست خبری ارتباط مستقیم با ایران داشت.
متن فارسی اون دقایق
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود. 8:15
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
5:00
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=dERTlAXlRS90YEAphh7N4QUhvoRJ9YMfzuRciEHMdWhVPlsYrxtabutYsHOyPTiuqY0riMKx9-_nR4PHGo18xWzr4QF96FxTDyEXJNap_62fy9qVhOln9tMPIK_GsfjbpfTcQm62wq9f8L7G2YmAGTXpMpgPKGcQc7o_NESzwk44AZK8g_rQbWQPjx0d46YxuoHZuNad6AIBC9BUBWlALFoa1SZpuz6esomdg6NIwO_20YLU6M62IyQR9vt_tiQDquZkb7v9iYK_mew0ZTLzzxLzPFA879PYSHcOZxUt087L8G1FqNoB4E4sLWGTLPpinDRlvFTjs6B3OUmgMqurhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=dERTlAXlRS90YEAphh7N4QUhvoRJ9YMfzuRciEHMdWhVPlsYrxtabutYsHOyPTiuqY0riMKx9-_nR4PHGo18xWzr4QF96FxTDyEXJNap_62fy9qVhOln9tMPIK_GsfjbpfTcQm62wq9f8L7G2YmAGTXpMpgPKGcQc7o_NESzwk44AZK8g_rQbWQPjx0d46YxuoHZuNad6AIBC9BUBWlALFoa1SZpuz6esomdg6NIwO_20YLU6M62IyQR9vt_tiQDquZkb7v9iYK_mew0ZTLzzxLzPFA879PYSHcOZxUt087L8G1FqNoB4E4sLWGTLPpinDRlvFTjs6B3OUmgMqurhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-pf-hYx6A1tYt4xuMe3aA2h1mscXpeK_Yf9W_G9nlLdk3UGNpc69h0pjfprBj6bVgl3Qmc9a6LQaRQWckWqIHV16NUxTNUCDI_PHB5sDStJoOiFO5otyxQ7UqdaC_t9HWJAm8UmTd8gYf-jJsYZ11Otieu2IvdVUo8IIrww25s02C6CFZbeobK6mrgLfAy-KGC571SjBkj7wosaNyUMgUivZIr4UIuvSMQHE7pHfwbuVlw6BsWPLMIAUcGWFwC8dScQFVyI_0LTIuTWF5HBYc7BVrAkR1v4UG2OwYha-taebMJ7Wz-qWGKU5kCyiWXNM-CETdCbuDNalPfoA1kUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqO49Xbvs8_s4vZvhFJ1--6-2thxXDx9OKUuUCAUEG1jlUmMj2se4NzjbglFkJHJUw3HSDxHSMdOOYnwsUR61YXoa8vCh7WX9CeRUkrf2U14ac6iC2Qaaj6vjV4CbJ3Nj3BILwWftMCZilcOA10FJIQDA0DlxfKYm3ByUxXdjltDc0kLVhxqJe5s9X6H3buV_qH7y-ROzLt2RLlPjtcXYLBGOqbj-SkRA9WTEMu0yPiqpW3EOsmSuTAvAwQydyOQIQoak5apCfNXKnomZTVx4T3tBDzF9kLL5BNyn0wJG1mwpffT7wKbTzBLyh83j4qI5Mc8AuK-9oCS5Qt57RFxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l4V87FsK1vXXAfzksFMEWts2uWYNfIHa9dkUxNbwfHNGqg35Ee3YEhpTwDItzPa54NTiLLIprJsT5jrlayrqH5R-PcOmRV9pAvKuPQ18xo1TpKUqW73ub1KXqmDRgSOyYVgAcsH5srThM3aAsyZGJfA4b16CqmLdc9YY1EqeFdlJFi5vZ98p041_RS-NcJosLlp1KvOFx2jpXFmFUgawx6S9Xf0285t-b9XvXzP4aIWPgV6Tvc7VpQc2hKfbHMHPMaaQ-unZKDUoGVuUPACAGc5QCaESuBQxPfqeD72EdP_TVkZ2h5whQi8IvcaJKUWNg5LwsYyurUBytgYH8JP2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=TVAJC0K2VwqvumDVbxRdexPzpD-6WX_cSEXlQg3RI3RlKVgXTRNLX5GndUur-fQGK6DA2_3hhA1AFU4RSZaBdkonJ1qy4Bum-A-oYv1PTg130Evvh96ienVr4tGcarS5CO1dJFITrHRXrQ26fINDqwRif8iCtE5gwk4QIda2G3n6MCuJsvgwn3CRDUyq5gqYroc0BYv3YGgvFyKX3KFef-e5SbdQ1X4qpCCrZ8v6Ev6IQF2JYo-LDUerHByHQQQhTCwd4-2SDa-JOao1Vs36dCOlWPRJCO-z7imUQh2rEulXKfruoB82LvfFeQmtQq2g8YA2DffwzfHXDcSR-P1Q1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=TVAJC0K2VwqvumDVbxRdexPzpD-6WX_cSEXlQg3RI3RlKVgXTRNLX5GndUur-fQGK6DA2_3hhA1AFU4RSZaBdkonJ1qy4Bum-A-oYv1PTg130Evvh96ienVr4tGcarS5CO1dJFITrHRXrQ26fINDqwRif8iCtE5gwk4QIda2G3n6MCuJsvgwn3CRDUyq5gqYroc0BYv3YGgvFyKX3KFef-e5SbdQ1X4qpCCrZ8v6Ev6IQF2JYo-LDUerHByHQQQhTCwd4-2SDa-JOao1Vs36dCOlWPRJCO-z7imUQh2rEulXKfruoB82LvfFeQmtQq2g8YA2DffwzfHXDcSR-P1Q1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تا وقتی که لازم باشد در جنوب لبنان خواهیم ماند
بنیامین نتانیاهو اعلام کرد که موضع و دستورش به وزیر دفاع اسرائیل تغییر نکرده است.
نخست‌وزیر اسرائیل نوشت: «نیروهای ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم علیه خود یا ساکنان شمال را دارند.»
او تاکید کرد که ارتش اسرائیل «هیچ محدودیتی در این زمینه ندارد.»
نتانیاهو بار دیگر تکرار کرد که ارتش اسرائیل «تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهد ماند.»
در مذاکرات ایران و آمریکا در سوئیس، هر دو کشور تاکید کردند که حفظ آتش‌بس در لبنان از موضوعات محوری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/smt70yobdCPMKl6yhBY30ibFBr5bHoLzdHT-6xCeMxiUNFGdb4DPJkLfI3tSPLqfCAKGYQRw4f1obQzi_ZKo8BDqmUq5V3kzm8jl1rA5O2Jan7lMRAH-mTZ_FECUVI16fJv-F-5aHMIeeZYOQOhKsflZJ9W-RCm6uyOt6R3wdjTIC0h9iQJx3BxVJ5CQKf932Z1SpTwpkdbDd36-U2JLtx_8xda8Kkg3EcYlqtmxAsC2ub7_LaDaumvdFvN_R5R641mQubBl837MvMR8l0wEb3CJh375I0VXjc4YpC7Dno-4Lxo_uBVUPy1kNfJ-sKsrDSpBARjuMEUPagpAWZnMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjc_Lro62NXQhk3YCFMuMJ1D2wPtoVhOgh0ft9eJWuvfhvUWRpyT-ERfP6HUFLJiJYVlVSbatID1-Ik1zNhfPnlA-NIvz3iVIFA55_7gzNTe1uDPqhQjHApuRX5kMIIpZ-83MbHjpElgPphLOPjky-UrN2wojdWWTmANZHbboDa543A6rjCOKbb9faYyxrxYHRDv5OIVRaBVCHVLCFLijHG6wypvzDEH_zakXNB1g7PdubjOI-F4Uca8Kt4kBp4Sr4GoYRSbeQLCHrlzMdwtedE-3Wl-qbczYMp9HDxKRW_8xt6AOWchVCNigOTBenZdki3cxgT8o5Nv5MWaRnqhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jGo_4ZDuhHXQJo16XVV67qb-_noCFML7qLf3LWDUfhyU8wxQc2c6DQN6rSiMmyY1j_6X4Hd29Qclvi004UHdRkk3NhQ5CTTI0BHK_aYH0A9KUHI__DqElnHTfvF4k9mLBS_jchggUPGTO8wz2q9NbcTfrXnmm06brDmtaO1hF8vR5thUOktqJb9BusdcfLTLYNtvR1J8kiTbHDAMVU8jJsWrdsAkomD62aEN1sNkgUfK3RU2NX2Ajit8Uf6zoaIW1lA7Flp9MUyNYVJa5_rCeHwgOjtVdjpnyjG1Sxps-VG1ZeHsrw3I26Edi1Urh-Ld0DCNzWMEqou2XyahZta4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tLZRMCh2aAyKR4VBnt0UVc-_f5CFMOSvc1Y_oGMglucnBP92Nrp0J3wlDk-BH7y1sHB9r4j5HrAwsKlXbFcy1UiRRZj7h7mnPs6PVnZp3DVuoxD8gJHFwMWSDJ2mtGvS6DVQLILrz_tMnKUQAlF7tXnhu9pppeJKyFzpzpK57YYlw6o573pGwnKHJvCqb4YUaY6t0gFix1IaPlSdDzxKqRVZ4JeQoCccUuSdSvlseP3mt3eMQMuWhaz_bThlYaEdxScsMhUcucmlggRBaXkreTPev3tLzStTmUKdfJ8Po7oabZawt2OhaeoTtw5GGZUk_2uhFYSEi_81xbtntMQgfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kh4HKYpZaSGRgd44bQEGwpzHV47m3pSlS8n35BdxtYN4jquHkrb6r7B7G-_IRqF-HVyJ0BloPsy03nm644xzz8EInhL6jT3P6FimD620kGjhC-BzL4YxFLYi_Ua3eKbDifq7ZVfkYa0y3TVcteNu54S8rpSquD7VaNJOiPqf9pkQbFuyVI5J7xj3dBnIhq2czL-yJSZqNhUDmeysVyHqxPurB5GOXYQWenKHKv9jBSbi6d0NRMVoZFMFRMFTUfpBiddQ8y9fnbpFcndvEs54Y12UPsYczKY6XM9DdJEXv1zY-sMZCVvflmGT1xReJgOm6xFNTYgIR0KQqi-kcE5W4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sHg46OV9_PUuI_zLY9-iGJkcKN6ty0nLqpZzTpircTei4eyhVRPnxv0-QePkNB8dl1QXX1fT9BErwDBP4HtT9_LJV21lpqXNT-YNFVvwYyloTKa4TlIv6xj2wSW9lgLrkYDjB5h4AIvrlNfizq-IWDNwJr6DOmJqdmlO3vxfOJzWPTeJWXLiXj59MTaRD0SW3tN9dE_CjTQsqhL48cnn1MbnFa9hApfDr1jRwd2ubz04zRZrYvXqGq4-p_F7JGnP7vS7yw1k5y3e5xS9M_nQAxcSzgogZwhdVE-EDlOplW416lqBEMinCHj2dBgSJ24QMFOmDIWKp3lr6qRf2UwGug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jobra6NIZw705gXlF72CLFIYsrWNx4Nfs2TDJFwuGp94R4NVDzbHYVulqoWIHkZoJyzZwf_BQXTB5hsOv3LQSG18iwt4B_-3vFJKvIGJ10wgDYBzkraycGeMpidPBAqSeW51mz5McZzEPzpDCCKU-xuTjlgDu-5SPT9I_54yF2_Jh_lkFebROHzvOGSUHMs8qYqBILK_k0FzyFuTjjWR-9SlGUOGoox-OzEjOrA0sMFSfHxdMXcQ-r96QI8q2i22Ft2gw4SOXWco6SMgpWQzBANjrAgtMMG_AiZ0NKU7WfgDizbuOIzF2IlxRte6qdFKKDto6O3MqbzBSCazsnnA5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=ptjjtl8utP4sjj6EB2by2he25Ci-sxRDFjuefCdte9LzmpxWoUdR1aKerYeJX_MP0jqbmc6JCnM-AGvB1VfMG8X5-XCFzu_ShL06ua-byrsm2JCK7I2ogJm5RjP38e5FA5L8oc3jAmuhtarKRMuXgJHg7MCioupB7XvfMV62c-4PkZswvD3g4qpDG64ksCUlw423cZ4vZ-yQyEweCIr6L0C9hd87kNEah28Q1R6JV9zBNm3buMzup4KSfjAy93KaF5kyQSSTYFG6bQ5KT2JesGfX3gbaeTKA0UNrvm9y0L7tpZnUDwBzO1aY-7q3amfb6_MmoPL7wTo9jlrIyhAvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=ptjjtl8utP4sjj6EB2by2he25Ci-sxRDFjuefCdte9LzmpxWoUdR1aKerYeJX_MP0jqbmc6JCnM-AGvB1VfMG8X5-XCFzu_ShL06ua-byrsm2JCK7I2ogJm5RjP38e5FA5L8oc3jAmuhtarKRMuXgJHg7MCioupB7XvfMV62c-4PkZswvD3g4qpDG64ksCUlw423cZ4vZ-yQyEweCIr6L0C9hd87kNEah28Q1R6JV9zBNm3buMzup4KSfjAy93KaF5kyQSSTYFG6bQ5KT2JesGfX3gbaeTKA0UNrvm9y0L7tpZnUDwBzO1aY-7q3amfb6_MmoPL7wTo9jlrIyhAvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی گزارش داد «تحریم صادرات نفت و پتروشیمی تعلیق و محاصره دریایی برداشته شد.»
علاوه بر این، عباس عراقچی اعلام کرد برخی از دارایی‌های مسدود شده آزاد و طرح بزرگ بازسازی و پیشرفت اقتصادی ایران اجرایی شد.»
آقای عراقچی این موارد را در پستی در حساب کاربری خود در شبکه اجتماعی ایکس اعلام کرده است.
@
VahidHeadline
معاون رئیس‌جمهوری آمریکا اعلام کرد که در گفت‌وگوها با حکومت ایران پیشرفت حاصل شده و جمهوری اسلامی با ورود بازرسان هسته‌ای به این کشور موافقت کرده است.
جِی‌دی ونس، روز دوشنبه در سوئیس گفت که گفت‌وگوها درباره بازرسی‌ها ممکن است از همین هفته آغاز شود. ونس درباره زمان آغاز کار بازرسان هسته‌ای در ایران تأکید کرد: «احتمالاً همین هفته، شاید از امروز.»
معاون رئیس‌جمهوری آمریکا افزود: «ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم. گفت‌وگوهای فنی در هفته‌ها و روزهای آینده ادامه خواهد یافت».
@
VahidHeadline
معاون رییس‌جمهوری آمریکا، گفت یکی از اهداف واشینگتن در مذاکرات، ایجاد سازوکاری برای نحوه استفاده از دارایی‌های مسدودشده ایران در صورت آزادسازی آنها بوده است.
او گفت هدف این سازوکار آن است که اطمینان حاصل شود منابع مالی آزادشده به مردم ایران کمک می‌کند و صرف حمایت از فعالیت‌های «تروریستی» نمی‌شود.
ونس افزود جرد کوشنر با همکاری مقام‌های قطری طرحی را ارائه کرده است که بر اساس آن، در صورت آزادسازی دارایی‌های مسدودشده ایران، ایالات متحده و قطر بر نحوه مصرف این منابع نظارت خواهند داشت و باید آن را تایید کنند.
به گفته معاون رییس‌جمهوری آمریکا، این منابع مالی برای خرید محصولات کشاورزی آمریکایی از جمله سویا، ذرت و گندم اختصاص خواهد یافت تا در اختیار مردم ایران قرار گیرد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در پاسخ به سوالی درباره تهدید تیم مذاکره‌کننده جمهوری اسلامی به ترک میز مذاکره، گفت: «آن‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم در شبکه‌های اجتماعی چنین تهدیدهایی مطرح شد. اما ما دیروز تا مدت‌ها بعد از ساعت یک بامداد در حال مذاکره بودیم، بنابراین آن‌ها جلسه را ترک نکردند.»
@
VahidOOnLine
گزارش‌ها از سوئیس حاکی از ادامۀ مذاکرات فنی ایران و ایالات متحده، به ریاست کاظم غریب آبادی، معاون وزیر خارجه ایران، است.
رسانه‌های جمهوری اسلامی نوشته‌اند که قرار است دوطرف روز دوشنبه اول تیرماه در مورد سازوکارهای اجرای یادداشت تفاهم اسلام‌آباد و تشکیل گروه‌های فنی مربوطه با یکدیگر گفت‌و‌گو کنند.
با این حال تیم اصلی مذاکره‌کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سوئیس را به مقصد تهران ترک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MP3s8ZehjguUsLctmnc0uorL2xm0GbeFYDlWU0O1eT_EzIHqOYPWAjgO7K1xxkrHerizFLSKGvhyGU1IUJ4u7zQw5g1lCig8kVT7jg09c9tdqxwJ74m1IXzHc0mALv3c5jGEJp1BREefqbOkeqoySorRt8WjUEtZUEbaUkCTef5yFOtUcbn031vhNQgXaA4YXOjn7w5rHL08Eb2RtIVjWwy2VhMWXldfzvqxeTg403q42mlvNwZnEqSgf07JIedcoXruQNjluixas3m1Z7Tz7_jkXITfwqsuO53HbKalTlwyDCn3ziVOZT_l-FziVPQP7plsGDwmngo1DgkGrbRQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMskqICMnZNWcnplyCFadXTC-7Sqmtrq2MmdteiY6me_u9-DgOZMSFf1RhwavGxT1ft9C9SHG8m5wh9jhUnYR5lwq_WBOVHaOJHuFh27mxfb5NCq0M95Ru9CPPqEsgADd9xURx_ylZcoZB1TaH0PJE70Idt2gXSMlg8QmlTxRRVrjWnBH6-MqJ2UIU6vU7fGERQomuRBy9TsuzMEpOpIdiExRi9hUxYc1i2CoQSQNbZtXxrawqlJux6L-F5DMLM3hjcY3OcsWPM8IltMkgaFAghhOtcpj_3MRRV_MTwEzNcyXBgCbH5c39KH_pEjV1CCAXRzlIX0TGhgEnd_bzC_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین: ما این‌طور از سرزمین‌مان محافظت می‌کنیم. mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76586" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eMlTaIItTnmu7OqJELafdIc2vyMARb6G69CVGfIARbp25i1EZmBqP6Og7YbumoLweE7jmFGHNQLUwUkNVjryccsadmvwtd6s1dodeX02GAlNl80s28Ewei-8uOediAGe3X_U3a9ECkHKJoycuvkbpN87a5OCokMZ7ZpP89_4xaWc0dv0yv05M_XjQXpGfBo_fm3cZ4_vnAFOowhG_LvxRw3AArpPGEAfQS0iWz4kAKgoAx_7aKtSdL8lK5XsrJIhsleQrUcRneEwBIfDlcxIAS1MzEV12IJdeq9isi36MHCZWy2qK5FShwyORrJgplSGn3W1ADLfgykWNZ06bD2-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nmzrYkzWvG2wmZ_OhoO7P_-iwHBcdOy56LIVCRlSl9CSuFiRPe2o46V2BO91ScgXETphIotVJC2NyukL3bCfOzdAHjDGojrq4mKotjJfdPoI_LOdjOckNEy5LVinUSU9A6seP-X_0XPpBv_3hV95wWDGTgjSEoS-I5vFl2RxPpkY1ZtJTEbDx5PVaO2MbQdz1ay0KQwNxALpp2StDyS7deDn5C3lioRfTDqhD9H7gRIJXnLz_cwAAtGEhjIiLUxW83QH_zF6Rz0j-bWonsDcaSazS6kSndYq2gVRNwGjWbZPMDL-qD5fbA2SuKLYOsZr7cA9zr5fFTwqkJ-9inQLww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، اعلام کرد مذاکرات سوئیس با «پیشرفت‌های خوبی» همراه بوده و گفت‌وگوهایی درباره پایان جنگ در همه جبهه‌ها از جمله لبنان، فروش نفت ایران، آزادسازی دارایی‌های مسدودشده و سازوکار عبور کشتی‌ها از تنگه هرمز انجام شده است.
او گفت درباره صدور مجوزهای لازم برای فروش نفت و آزادسازی دارایی‌ها پیشرفت حاصل شده و قرار است سازوکاری برای موضوع تنگه هرمز نیز تدوین شود.
بقایی همچنین تایید کرد هیات جمهوری اسلامی پس از انتشار آنچه «اظهارنظر تهدیدآمیز آمریکا» خواند، از ادامه نشست چهارجانبه خودداری کرد و مذاکرات از طریق میانجی‌های قطری و پاکستانی ادامه یافت.
به گفته او، تهران بر اجرای تعهدات طرف مقابل، به‌ویژه در زمینه آتش‌بس و تعهدات اقتصادی، تاکید کرده است.
بقایی افزود گروه‌های فنی دوشنبه مذاکرات خود را برای بررسی جزییات اجرای تفاهم‌نامه ادامه می‌دهند و قطر و پاکستان نیز متنی را به‌عنوان جمع‌بندی توافقات حاصل‌شده در جریان ۱۸ ساعت مذاکره منتشر خواهند کرد.
@
VahidOOnLine
تسنیم به نقل از بیانیه مشترک قطر و پاکستان گزارش داد که نخستین جلسه مذاکرات نمایندگان جمهوری اسلامی و آمریکا در بورگن اشتوک سوئیس و با میانجی‌گری پاکستان و قطر به پایان رسیده است.
در این بیانیه فضای مذاکرات «سازنده» و روند پیشرفت «دلگرم‌کننده» عنوان شده است.
به گزارش تسنیم، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
براساس این گزارش، «مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.»
تسنیم می‌افزاید: علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@
VahidOOnLine
عباس عراقچی بامداد دوشنبه، با انتشار پیامی در اکس از پیشرفت‌های حاصل‌شده برای پایان دادن به جنگ لبنان در پی میانجی‌گری خستگی‌ناپذیر پاکستان و قطر خبر داد. وزیر خارجه جمهوری اسلامی نوشت: «صادرات نفت و پتروشیمی معاف شده، محاصره برداشته شده، برخی از دارایی‌های مسدود شده آزاد شده و طرح بزرگ بازسازی و توسعه برای ایران آغاز شده است». عراقچی با این حال تاکید کرد که اولین آزمون واقعی و جدی این دستاوردها، عملکرد «سلول مدیریت منازعه لبنان» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76584" target="_blank">📅 05:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5HfOekuIrsOn5S7NQWrKh38Zaz3frV9tB8kS_gb1xxzzB_GEhzPfh3-0fLK4qJFBvCXrtiVHoGEqWPgHBAaGpInhQpsYSJ7e33O1cvu6OvsRZDn27ieJjI-hpTj1BCCt49lvx6wdcPZ0D4Q1D2CLGxNcJuyNkiL4Lzx2V71l-gl16m5RiTB1psxngx7LJWFZ3PuTmeny7drQ6nSs0Hi4NM47VxIcOqD7rrug3o0Q67TMs4tXszS0cv6nhCrgHfyqdElzQC7GvqDNwWNv6ZB1rb6g1zv-b5X0RT-LVUF003oiTt7-0XKHGvhkG3SsMEZs3Pv0mOW_A1rlZyGSbSRgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، از دو روز دیگر، یعنی ۲۳ ژوئن (دوم تیر) در سفری دو روزه به خاورمیانه به امارات متحده عربی، کویت و بحرین سفر خواهد کرد.
در این سفر، آقای روبیو درباره مجموعه‌ای از اولویت‌های منطقه‌ای گفت‌وگو خواهد کرد؛ از جمله:
تفاهم‌نامه میان آمریکا و ایران
تلاش‌ها برای تضمین عبور کامل، آزاد و ایمن کشتی‌ها از تنگه هرمز
اهمیت حفظ صلح و ثبات در منطقه
وزیر خارجه آمریکا همچنین در بحرین با اعضای شورای همکاری خلیج فارس دیدار خواهد کرد تا درباره اولویت‌های مشترک کشورهای منطقه گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d6dbgxWQZbLPmoDQeh0n8EosBx1pK8VkexEmjhMteiI1QpSIjUa8kfa057Gskd5qFkQkcg21FSHwfW3jFqj4KdKuIZSkzaMLKkkOgmsDSJj0Xn8aS4qzBPqlAp7vCs12vCMHNuIypKYdppGTvJqqEtDsvHQdH5IVanIqHtPoY4PVnxf2eD7IHH-2xsWlRlmZZCFgRr7Q9STD75Je48yMejSkxPain_HyM64QKDmi_YKXUu_b2MDzhzFxlpe_wkvS4Cntl3ydMaFCD-8NstJaI1yff0fSNl3SCef9D17u8rPApMG9w_5Cr5OjrrQdSWHHmh_n9eLGvdyV8gBH0GGxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FSWO9pv43DxNnSwyfloUPDeiayWiSkO4_u6NSJxI5N0iDWbozY3m-j3Ge4QHOGP4iPsCVhh5Y6pLin7xEeiy2NeLxKk6GtSQ-ivAnPzimv3YTsazcVSztYxsS6hkNCBb0VGfXkmEe802QYnwJ3sxY8Qvh1YKIzvAJGlYc4eLqSTNS1RkUK2LSlaWZ7ZcsEQ7EsvMzT8uWM_uVGn_JwklEduZwIVxjch1z4vxuWrOkwfbQtBHXwSHu9ruM3HhgeUo-2S1xycrxdJha3xDcnIGLs_QTqS-daMFEJ0C3obyYcV7MyyqMQTZkf1ZHmifZrQfSVfbcwA1pOFbAE4ffLR3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست ترامپ علیه نیویورک‌تایمز درباره اخبار جنگ:
تیتر نیویورک‌تایمزِ فاسد و رو به سقوط این است: «بعد از تقریباً چهار ماه جنگ چه چیزی تغییر کرده؟ تحلیلگران می‌گویند نه چندان زیاد.»
واقعاً؟ ارتش آن‌ها از کار افتاده، نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آن‌ها تقریباً نابود شده، دو رده بالای رهبرانشان از میان رفته‌اند، تورمشان به ۲۵۰ درصد رسیده، اقتصادشان درهم شکسته، به سربازانشان حقوق پرداخت نمی‌شود، تنگه هرمز باز است، نفت با شدت در جریان است، و بازار سهام و اشتغال در آمریکا به بالاترین رکوردهای خود رسیده‌اند. این‌هاست آنچه تغییر کرده، ای ترسوهای فاسد و بی‌اخلاق، و حتی بیشتر از این‌ها!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
نحوه پوشش خبرها درباره ایرانِ بسیار ضربه‌خورده و آسیب‌دیده از سوی نیویورک‌تایمزِ فاسد و رو به افول، از طریق «واقعیت‌های» جعلی و ساختگی، به نظر من «خیانت‌آمیز» است. من همه گزارش‌های دروغین و مضحک آن‌ها را به شکایت چندمیلیارددلاری‌ام علیهشان اضافه خواهم کرد. آن‌ها مجرم‌اند!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jz-7DOT8Xmq10FJMC3UQc-2rO8vcBsNneQI9ptxfXB86RWPTyl8UauJex6rIFwqZLRxzZCJsPD6Xzhq9x4gifY5WCHmKSRT88kbMKqZQD2Kq0ZlpGETPCDrDVcVY8Ai6xaTImYUe-aBvz7i0SWY4My4KTkDRgWnuEYFHRZlUHHAjGFMWSR_b-IENK5uIbA8lwYgC9XUUje7GKkGH5lD8OPnPIXeCQFI-Eg6soy40lX_Cy4BAdSxrQ-LbtH6zTKlXbsv1I6z3mMfKY3MNeJlw_ZZ7xAFwFeLc4DmkXE0AAAERL_rv9jWpbmRRorf3zKP6q0GFMtg0xzti5QqsiAGKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XO7T9F2oNA4EAISM6t7fiwdFjZUjqI79k3joyfX5BhSHQcxfXUX_RVoy-sffRj3Vqdq24mT8M3xWq1vA_cR35R3iluBBZrQ7cs-3fJWTJDXrMW0hmZX_9m74s8a3foGQpOtyNPSE5DTB6LS8fyfv1lsY5wUachKygKcqgd33cmZ4Ee2CERWVNWI8jaHC6I7dEifCrFlpktD_w40vdORx6-pVdrFLktB0iWzV3SQNPy06pQ4CGqa9DmpsMw0mW7OU-sJX43yM7WQENsmfv91PNRzR79u4WQBiGO-SIBMYkPlZNSS0czFFGRhpG8jHXJr_Cp_aDX3_x5ssJAe9zmPPag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qAvMXGAB-dQ6jyErMTwd8MPOPGhDo4T6FwjWnGE0-1rdJMblY5X5MsW59SmXUS68H44kHeuMj53Cfq52Hes47c1nfaJ8xl4ly4BDbN9QdlH5lnMsWSDPIgkcybhS1oszguIsU7fT_kFE3tOo8qi91rQ4BX4ZCA-KIn-E41DGFfO-PwlkOZ1x71cdlMETFP_CWLr_KssM1mKc9jZc6S2pcEkNncC4C7feEbF5KvtQeDokc6gsm__78Pv9THjy90uep3ESG4TZK_grwA1wJ-klJdf4JKEFrd0TRUeigUZSnuVfmACaUE3nJ4ci8aGmzkQ787b023jTBvl17znvkeA2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M849XZMN5xJaxRA-bLp753hDuyqMszxhUQfFFei9kTZpMD8HfCHycAg7sxdJX-iJ5N5y70t2a8qhYlEMhlSzRsQ8jjxjOHf7UD5rOYp6M22WRIPdsZFTt_dCHWt6Q1euHXJuiO8_0cL8g87KETz0KevRSWLJgQGu6AbuexvyHq-Oja_1QetilUc3H-mv1ijXXQxLTOMV8A0JTqx1X7GtpGC_FxO6F3G6EC1D4dLFyDMguuR3jMJHcfTEuI-ats93JxotKFTA9_jisixXb0V133WmQoTg26O5Cgb879fJatrqDhL4sLtbKV9OlKAo4I_zhunumgtv23z_PqEPDlRUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jroKbQUfaxm8YeoMB_wND3fXMq0SrybVTOEmx_9xJU0LtyDWpScCF65yN2oogsyd4Vf1eQHKHoUWL04If4oE77r_gTPfBmmd77qhtuTkgpKf3nC4Ob4boqDuKAZmzmYc5WphaA1FKZ2kKwRnu6tcFP_9oyFmILR-H_jlf6cuAVX6xTBOdY8sw_U_HDLChZu8Be1exzJtN7Nnbma2fArGb2gc9VhdhZZLfCQQP6NKLlmW2XWsEOry4WIWvJ5TfL1nWjxvLxiyGBxxshM-3-WKk2MHagwDjdxqrVxGd8onSLz_wO8tc1pFjoSh2ZYgzykPOcQLpCmiO79YKMUM3ihOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AOb6PwwqoyTUG4kVWIauKZkU8YFkjwRUnTpT6tkb6qtUPguhrj5zAPm2oSnA02yIAC46F99VtW5FifTdgMtIQtRLsN6x-762edJsehJ7BdeyUbkVeS6-vYDBLXL5T2svd0KtxZAP02rg-T5a5L8ohQ2EN9t2AeEBcHQs2GmI2jjlZbxgpkQgRH7ghXK0hkPjoQ9Wbfd6cCQibkkhMqljXx23m2GszY1O8eM2Cr5LzeqIYG0UwP5nXG91cOE12LbwXqGRCDKY_vdLFszYMIOeiBpZFJ_cGw-NxEQ4jDgihR6Di6qUoBYTlfnLOwCCKz7VIUUUQwbVWumrA0k2NNGzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nzxKjYTkOBH6EvR_NOP_NfhJulOQZ4sx9lh0ttxjA2QdYmny2nIKB8k7EQ058s055h6FJkn7-lDt6qIh4aNG0V4BRQ-SBOj_n_nxMUEMMD3-hc5XxmSSB4bJHeoKgPakz8NHQ7RNzbSAB02OWOBumqC50WzIQehRM9oL64gJUGOdr2hM37IQynGdhOnKIFde31s_-s3sBXD1vcdBfWUbhosmPsALHSkalY0RYSgh8eVrkBXOG2JcsumT8-wGC7UXHmtvUBSsIk8p1d76dGILua103T9h3SLBe1H5v4MEaScNk88ovksmOZFy2fKlU2fHguhdYWAk-uwDYkQ5etwC6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=fkwSKhZMkcXijkWnRUDZ8FKkTvYCOyWpXxP-q8CyG1DOM7B-1N9EfGip4o8r4maRL8nzASmhlBI4A8w8P8n1HYze__oyuI3kxuNKCyvpr82hCNMgtMkAdQaIbV7_tbdVqJI-SOxLdeR1GXcmGwzsBqEkQBSWfVdVefukONCbKMa3lv7kPdoe1Gc3RdOgES8KwF7_j6UNNgrDuSm1Wwp9YbTxve-7__UmWUarWh86DqjMkCauADv44M1horg-sXcU6ZKWXNGxYEO5kWiQ1qcMF-xrBz7cT46_fX_DfnJcolxSDBhq2uk6fCERMn8NiWWl5v1A49o-NZdhRnUluPd2PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=fkwSKhZMkcXijkWnRUDZ8FKkTvYCOyWpXxP-q8CyG1DOM7B-1N9EfGip4o8r4maRL8nzASmhlBI4A8w8P8n1HYze__oyuI3kxuNKCyvpr82hCNMgtMkAdQaIbV7_tbdVqJI-SOxLdeR1GXcmGwzsBqEkQBSWfVdVefukONCbKMa3lv7kPdoe1Gc3RdOgES8KwF7_j6UNNgrDuSm1Wwp9YbTxve-7__UmWUarWh86DqjMkCauADv44M1horg-sXcU6ZKWXNGxYEO5kWiQ1qcMF-xrBz7cT46_fX_DfnJcolxSDBhq2uk6fCERMn8NiWWl5v1A49o-NZdhRnUluPd2PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_ugLxn28ogwyC5r5Af6tUtDiGf8NJbkipDxW61BjaIIqa4oQiTVDp6tlPVsar7nYuit9An8XWCZFjeNSJUbX4v-5myBvwXGpPgQa07ya2BdpvVEfkx-oAQLIkh6v9QRh6MJBQtuPN1ijQxt6v2avp0RqczlBjWRFFkB-wXMEImjFBfKCVZyslneHfKzCtHthr2YtnBdsYys5GD1DGSJbVE9pVh11lCmWabtaKCg3eMqxKkVybS20VVigBHPKTaB3HCj_WJ3tuQ4U7y-t-YxUa5CYnjc-wbdRlmxxULq5riK1Lf0qzPffGWXsFiLEq_q2W97cENex2kIYlNn98idIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDdBwJvmTup1BQgA23qnFNXladEvlCiyvw01QZe8JZMtEXtaKAvDLpf2CK9jtHlg8o0qv28rDah--n-nHLgqLQM0io4l0_5fiqoHauy5FXovfm3E-DfDeZ5eWPAV3FX26DOsdFcglM18cHMxXPzGUQuXBHU2NOSYxFOaW06Bbsby33VB9ShX54oEzoC8P4IvxqXeK28NZxYfv6iEM76p3VaSNVcw7J7S0XanTbm0BjguRTe_F3kkVkHRIDyI1SRzxTmy3F16vZI4R6JXQFidnQcRkBcz3GgNRIYUEZpSKF4om4PQsa-n6pJLvBx9qDNjiChTkVlM5SenMixmso7hGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ک مقام ایرانی یکشنبه شب ۳۱ خردادماه به خبرگزاری رویترز گفت مذاکرات میان ایران و آمریکا در بورگن‌اشتوک سوئیس متوقف شده، اما پایان نیافته است. این مقام جزئیات بیشتری درباره علت توقف گفت‌وگوها یا زمان از سرگیری آن ارائه نکرد.
این اظهارات در حالی مطرح می‌شود که گزارش‌های متناقضی درباره وضعیت مذاکرات منتشر شده است. پیش‌تر باراک داوید، خبرنگار آکسیوس و کانال ۱۲ اسرائیل، در شبکه اجتماعی اکس به نقل از یک دیپلمات حاضر در مذاکرات نوشت که هیئت ایرانی محل مذاکرات را ترک نکرده و گفت‌وگوها همچنان ادامه دارد. با این حال، خبرگزاری ایرنا دقایقی بعد به نقل از یک مقام هیئت مذاکره‌کننده جمهوری اسلامی گزارش داد که مقام‌های ایرانی پس از دومین دیدار با هیئت قطری، محل مذاکرات را ترک کرده‌اند.
@
VahidOOnLine
خبرگزاری ایرنا، رسانه دولت جمهوری اسلامی، گزارش داد هیات جمهوری اسلامی پس از دیدار با هیات قطری، ساختمان محل مذاکرات در سوئیس را ترک کرده است.
هم‌زمان، یک منبع نزدیک به هیات مذاکره‌کننده جمهوری اسلامی به شبکه سی‌ان‌ان گفت گفت‌وگوهای میان جمهوری اسلامی و آمریکا در سوئیس متوقف شده است، اما پایان نیافته است.
به گفته این منبع، گفت‌وگوهای غیرعلنی همچنان ادامه دارد تا طرف‌ها به میز گفت‌وگو بازگردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k7Gdyc9Qq_E-Mx1FBKMXrNzboVEtuPOexPHw4KftXWRVWBj8Fl39h0kxTK3ebqjyPB4xnd9IuG1qjnmGcxtNmKWPnTJq3CmYu9Ln3_HzOcUq1OdXnufrgXHbUP1iQVRn2NWYEh2OeKIuzyf3kLafk1DLEb5sbOvS8VKx5Dh2CZf2RVpsQuwC9QZExQKQPCHY6_Oy5xdFoyrOqnLcfA8a9VCDAy1s0THY76x3tPmCLcOQbn-gIgwh0Xf8vcbIBXkW63m3aYopX3UVsboKgl0RdN6-TxpxUb8cjWdZBX-a1XiH6S8m61z3mCuKhn4tSUEWIQ_q1bKncI9P54Fm36Nm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
"
ادعای فارس و تسنیم به نقل از "یک منبع نزدیک به تیم مذاکره‌کننده"
پیش‌تر در
اکانت قالیباف
همچین توییتی منتشر شده بود:
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76568" target="_blank">📅 20:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tm6smOd89REa6wXY7Eo-jQdoe9rSBFD9KoisoZpKMJ_mSm1-mAyXZKHlKFcOJX1eyoHLTJOLLG67KPD24ZPUhWkDMt0aoLcHPRh60rmMbMknUO8U8gPRUGY4utov-M3co-gJwtaZzgt7fMPGEz3G9d2W4ItJXjS043fvEa0naZAQtF-LCiNhYCXqGSVl0xMaQnrTSQdcoi0sfd6YctNJZeYK7Eu0pXeIcmchkEbVIJ2dJ26rFsTkfEoXXWymhUzmIXjPXX04kIcjK9xzpcCo-Fpw6P059Do_lowqB9lkudH8T8viVRDtJBAwCoN7Zw5L0lN0p91HfCG6DwGcuAHB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در واکنش به اظهارات مسعود پزشکیان، رییس دولت جمهوری اسلامی، درباره ناچار شدن آمریکا به پذیرش تفاهم‌نامه میان دو کشور، هشدار داد که تهران باید در مواضع و رفتار خود تجدیدنظر کند.
ترامپ در گفت‌وگو با فاکس‌نیوز گفت: بهتر است مراقب حرف زدنش باشد. بهتر است رفتارش را اصلاح کند، وگرنه ما کنترل بقیه کشور را هم به دست خواهیم گرفت.
این اظهارات پس از آن مطرح شد که مسعود پزشکیان روز یکشنبه ۳۱ خرداد گفت: آنچه مسلم است از حق غنی‌سازی اورانیوم هرگز کوتاه نخواهیم آمد و طرف مقابل نیز ناچار است آن را بپذیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76567" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JW1qdQfzj8LBV_kHB1Tw_f6jaBJZl-pw6jNaPjG7z2yPziubmxE4AAviuw3PFnJeoCgNlPuZ1_uP5oxnhtijNHVorKJnQIAdLFFUikGAkMG2lXz6O6gCKMRf1h27tfLGIuIDYscJf-dEh_d5MhkFq_Nc6JQhoh5nEux08Zy_XA9pEKGSOmLUoE-eYhZ2ZOLlG_TMQUh4bQ_SEMx_7dyDY5pveV0EXCiWO4D_VKWPJlXOkHnZI83EvAM4Yk3nTL1vFF-ZO1srfUA-MtJcOO32spMr5kahbMlP-cLdHYNnNRXWlm_99FbGVTyGC3a6pHvBeUlH6T9sUUHsn6iO9-O0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد همزمان با برگزاری مذاکرات در سوئیس، به مقام‌های جمهوری اسلامی درباره هرگونه اقدام برای بستن تنگه هرمز هشدار داده است.
او در گفتگو با شبکه فاکس‌نیوز گفت این هشدار شنبه شب به تهران منتقل شده و تاکید کرد در صورت چنین اقدامی، ایران با پیامدهای سنگینی مواجه خواهد شد.
ترامپ همچنین گفت به مقام‌های ایرانی گفته‌ام که اگر تنگه هرمز بسته شود، «دیگر کشوری نخواهند داشت و حتی امکان بازگشت به کشور خود را هم از دست خواهند داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76566" target="_blank">📅 17:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z6n-XjEmEvCWGVvSpJbkOdO-LTpEW0aLMk7kELuoqKME-uRTmptWJAA97QSsJeqjHqdSEmz4PKX7jO-bkzw_J8VuZVG8vZk3Ah3DtNbOK82A3EEjkA4s9PPceub3jLArhLc9B-EGW3yblYJeP51o3s-Tx-6o1ZCkxe0zJ_7x4ZAkL-fQ34LiAXMnII8W-1dNwQjUO6NkZpH3SNjtMukAGOLdwtY7eTeuuvc5pJRESA1mB512iRX28r1mP6XmnJtOOIug67_UIWpYHsZc6pPOmB2Zg4kUZg1CjhfXlnuGvFbtgsTm5Z4-ScArhUMfuTZZz-8t7Ijv1cipyAysI3rECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران باید فوراً جلوی نیروهای نیابتیِ بسیار پرهزینه‌اش در لبنان را بگیرد تا دیگر دردسر درست نکنند.
اگر این کار را نکنند، دوباره به ایران ضربه‌ای بسیار سنگین خواهیم زد؛ درست مثل هفته گذشته، اما این بار شدیدتر!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76565" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=M_1b1Q7Z2Piidv_vUW38ghvtDkMq8bScPuVzbaWjFzE9JzKIn3GQlI6D8LvWyNkFUBSW9ug8oaxIzgrkayiyJ3R7NQweWg-1HpbtKxQAJ6kez2zt7wh1jOtNo_F2s8Y8pcA4eoXSb4mDm8HdSVhhJ3a_GaR2U-rjpcOrfdOisJ9yQQOx8OI-qRty_2580g6NPYGKZ0vjQ97xNu325ZGvObkDfMhvpU1hl9NIkGXpm0XvuxrIH3JaBG1hEmcunJccjoBtlfuhQvkMGmIv1AsNCZ1kRT6D0N_Qow0AmdDb-V7sIUmbN0yDKBUOhGqkAhjksJl76opGp48YCMbTU7X3YA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=M_1b1Q7Z2Piidv_vUW38ghvtDkMq8bScPuVzbaWjFzE9JzKIn3GQlI6D8LvWyNkFUBSW9ug8oaxIzgrkayiyJ3R7NQweWg-1HpbtKxQAJ6kez2zt7wh1jOtNo_F2s8Y8pcA4eoXSb4mDm8HdSVhhJ3a_GaR2U-rjpcOrfdOisJ9yQQOx8OI-qRty_2580g6NPYGKZ0vjQ97xNu325ZGvObkDfMhvpU1hl9NIkGXpm0XvuxrIH3JaBG1hEmcunJccjoBtlfuhQvkMGmIv1AsNCZ1kRT6D0N_Qow0AmdDb-V7sIUmbN0yDKBUOhGqkAhjksJl76opGp48YCMbTU7X3YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس و عراقچی در یک قاب
خبرگزاری تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده جمهوری اسلامی گزارش داد که هیات آمریکایی و برگزارکنندگان نشست ژنو قصد داشتند پیش از آغاز مذاکرات چندجانبه، مراسم عکس مشترک و صحنه دست دادن میان هیات‌های جمهوری اسلامی و آمریکا برگزار شود اما محمدباقر قالیباف مخالف کرده است.
به گفته این منبع، محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، با این تشریفات مخالفت کرد و اعلام کرد اعضای هیات جمهوری اسلامی در مراسم عکس مشترک با هیات آمریکایی حضور نخواهند داشت.
این منبع افزود در پی مخالفت هیات جمهوری اسلامی و خودداری آن از حضور در این مراسم، پخش مستقیم و برنامه عکس مشترک لغو شد و پس از آن هیات جمهوری اسلامی وارد محل برگزاری مذاکرات شد.
به گفته این منبع، هیات آمریکایی از هیات جمهوری اسلامی پنج دقیقه فرصت خواست تا خبرنگاران محل مذاکرات را ترک کنند. او افزود مراسم پیش از آغاز مذاکرات، بدون حضور هیات جمهوری اسلامی برگزار شد.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز یکشنبه در آغاز مذاکرات ایالات متحده و ایران در سوئیس، این گفت‌وگوها را «تاریخی» خواند و تأکید کرد ایالات متحده آماده است روابط خود با ایران را به شکل بنیادین متحول کند.
ونس در حالی که در کنار نخست‌وزیران پاکستان و قطر ایستاده بود، در اقامتگاه بورگن‌اشتوک در کنار دریاچه لوتسرن گفت: «این یک دیدار تاریخی است. پیش از این هیچوقت رهبران ایران و آمریکا در چنین سطح بالایی با یکدیگر دیدار نکرده‌اند.»
تصاویر و ویدئوهای منتشر شده از محل نشست نشان می‌دهد هنگام حضور معاون رئیس‌جمهور آمریکا در اتاق محل مذاکرات، عباس عراقچی، وزیر خارجه ایران، نیز حضور دارد.
معاون رئیس‌جمهور آمریکا درباره اهداف مذاکره با ایران گفت: «آنچه رئیس‌جمهور از ما خواسته این است که فصل تازه‌ای را آغاز کنیم تا روابط خود با مردم ایران را متحول کنیم و دست دوستی را به سوی آن‌ها دراز کنیم. پیامی که به مردم ایران می‌گوید اگر رهبران شما حاضر باشند از نقش‌آفرینی به عنوان عامل بی‌ثباتی منطقه دست بردارند، و اگر حاضر باشند در بلندمدت از جاه‌طلبی‌های هسته‌ای خود صرف‌نظر کنند، آنگاه ایالات متحده آماده است روابط خود با آن کشور را به شکل بنیادین دگرگون کند.»
او ادامه داد: «این بدون تردید هدف ماست.»
ونس همچنین گفت: «ما تنها در چند ساعت گذشته پیشرفت‌های بزرگی داشته‌ایم و انتظار دارم در ساعت‌های پیش رو نیز پیشرفت‌های بیشتری حاصل شود.»
او با اشاره به اراده ایالات متحده برای «متحول کردن» خاورمیانه، افزود: «ایران در گذشته یکی از عوامل بی‌ثباتی منطقه بوده است. اکنون آینده‌ای را می‌بینیم که در آن همه بتوانند برای پیشبرد صلح و رفاه برای همگان با یکدیگر همکاری کنند.»
@
VahidHeadline
جی‌دی ونس پیش از آغاز مذاکرات اعلام کرد واشینگتن طی ماه‌های اخیر بیش از هر کشور دیگری برای توقف درگیری‌ها در لبنان تلاش کرده و این روند را ادامه خواهد داد.
او با تأکید بر اینکه «صلح آسان نیست» گفت رسیدن به توافق نیازمند تلاش و «بده‌بستان» میان طرف‌هاست و افزود هدف آمریکا تنها صلح با ایران نیست، بلکه دستیابی به ثبات در کل منطقه دنبال می‌شود.
ونس همچنین مذاکرات جاری را «آغاز یک گفتگوی فنی» توصیف کرد که قرار نیست همه اختلافات را یک‌باره حل کند، اما فرصتی فراهم می‌کند تا طرف‌ها برای نخستین‌بار درباره مسائل اصلی به‌صورت مستقیم گفتگو کنند.
به گفته او، حضور رهبران سیاسی برای تعیین چارچوب مذاکرات و حمایت از تیم‌های فنی است و با وجود چالش‌های پیش‌رو، طرف‌ها با انگیزه برای ادامه مسیر آماده هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76564" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=fvpGTTtHJcaJQjbnnI1qIp5ANj84raKL6xNwigbXabvOf85SuNjJ4xsEvy3n_iH_eLTWjqmjcrNgqC_T7oUkJW8vpYpyEKDwA9XV0JvoM5zZq77qPBsOhWDZpqEQqMUwwI2rZlLVHp5pdxz9AVMJx-1Bb485F3y-ZeUwSpb6Z3HAAj5cvkl7Ys06HNPw4tsg7C73fydVKpPbmh2O-ivrvPZ3pAZfaC5PKuDI5O_dM7kOWiHLtI5bPS85f7-uBdZy4bz0eR9pwrj9wx4A8Ub4b0HhPkt_Z5R6FzfWXC3DTHrrEiXQOoWupe8Cmcp0x7LVBHdgp1lYv2nftr2rg5Br2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=fvpGTTtHJcaJQjbnnI1qIp5ANj84raKL6xNwigbXabvOf85SuNjJ4xsEvy3n_iH_eLTWjqmjcrNgqC_T7oUkJW8vpYpyEKDwA9XV0JvoM5zZq77qPBsOhWDZpqEQqMUwwI2rZlLVHp5pdxz9AVMJx-1Bb485F3y-ZeUwSpb6Z3HAAj5cvkl7Ys06HNPw4tsg7C73fydVKpPbmh2O-ivrvPZ3pAZfaC5PKuDI5O_dM7kOWiHLtI5bPS85f7-uBdZy4bz0eR9pwrj9wx4A8Ub4b0HhPkt_Z5R6FzfWXC3DTHrrEiXQOoWupe8Cmcp0x7LVBHdgp1lYv2nftr2rg5Br2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، همزمان با برگزاری مذاکرات مستقیم میان ایران و آمریکا در سوئیس، گفت همه نظامیان در شورای امنیت ملی موافق مذاکره بوده‌اند.
او در جلسه‌ای به مناسبت تشکیل بسیج اساتید در دانشگاه تهران، در میان صدای اعتراض عده‌ای از حاضران گفت: «همه امضا کرده‌اند که این راه را باید برویم. حالا هر کسی می‌خواهد تفرقه ایجاد کند، این گوی و این میدان.»
او با اشاره به نظر فرماندهان نظامی در شورای امنیت ملی گفت: «فرمانده قرارگاه [خاتم الانبیاء]، فرمانده ارتش و سپاه، و نهادهای امنیتی همه بودند و همه یک حرف زدند و همه متحد بودند و همه آن چیزی را که می‌خواستیم عمل کنیم را امضا کردند.»
این سخنان پزشکیان در پی افزایش انتقاد اصولگرایان تندرو از دولت در پی انتشار نامه منسوب به مجتبی خامنه‌ای صورت می‌گیرد.
آقای پزشکیان همچنین با تاکید بر نقش دولت در حمایت از نظامیان در دوران جنگ گفت: «۲۰ میلیون بشکه نفت که مال دولت بود را به هوافضای سپاه دادیم. ارزهایی که داشتیم را به این عزیزان دادیم.»
@
VahidHeadline
مسعود پزشکیان، رییس‌ دولت جمهوری اسلامی، گفت نگرانی اصلی او این است که دولت نتواند رضایت مردم را جلب کند و نارضایتی‌ها به اعتراض‌های خیابانی منجر شود.
پزشکیان گفت: «از آنچه می‌ترسم این است که نتوانیم به مردم به درستی خدمت بدهیم، ناراضی شوند و به خیابان بیایند و اعتراض کنند. آن وقت ابهت ما فرو می‌ریزد.»
او افزود مهم‌ترین قدرت جمهوری اسلامی، وحدت مردم است و مسئولان نباید اجازه دهند کمبودها، کسری‌ها و نواقص باعث نارضایتی مردم شود. به گفته پزشکیان، بروز چنین وضعیتی موجب «خوشحالی دشمنان» خواهد شد.
@
VahidOOnLine
بعضی از جملات پزشکیان به انتخاب خبرگزاری دانشجو، وابسته بسیج:
🔸
اظهارات عجیب پزشکیان: من از این میترسم که نتوانیم مردم راضی کنیم و به خیابان بیایند اعتراض کنند
🔸
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد بود.
🔸
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔸
۶ میلیارد دلار پول ما در قطر برخواهد گشت.نتانیاهو اولین ناراضی از مذاکرات است.
🔸
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم، این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
🔸
شورای عالی امنیت ملی در وحدت و انسجام تصمیم گرفت؛ همه یک حرف زدند و متحد بودند
🔸
مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده/ آنها پذیرفتند که حق ملت ایران را نمی‌توانند نادیده بگیرند/ قاعده عوض شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76562" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDesrABdvek01id_QffamHMPzb7GG29A06dSSMEgZqzWp8R2zDgdk7ZWQdJilOLKIp9RUaZ63U2TnyeGD3FfhJTDHKGJFvQrSNJ0WBf0MVKFOqyQ959aAamUEYlJkEhUe2tc1u_z2iMedSRVQFUL7cuPxERaiLx60moLzJdIgIkNPIHl5lBVl0-fpBBcmzwDnxOfsalnqSi0-3rNmJImZmAUyuVQr_JcEtZQGaioBwrpZnWeWHCS_9jJwijNfBXJmA11KGxnF5IcvWWC5lyTSgo8LiNJwcc1yzap1kkW5wSyNOWq_hExo2dE37gzfpc6bP54Erta6yRN7yaMNAXjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو منبع منطقه‌ای آگاه گزارش داده است که آمریکا می‌خواهد نخستین دور گفت‌وگوها با ایران با دعوت تهران از بازرسان سازمان ملل برای بازدید از تاسیسات هسته‌ای ایران پایان یابد.
به گفته این منابع، این تاسیسات پیش‌تر هدف حملات آمریکا و اسرائیل قرار گرفته‌اند و آخرین بازدید بازرسان از آنها پیش از جنگ قبلی، در ژوئن ۲۰۲۵، انجام شده بود.
اکسیوس می‌گوید: «آمریکا در مقابل آماده است به ایران اجازه دهد به بخشی از دارایی‌های مسدودشده خود دسترسی پیدا کند؛ از جمله حسابی به ارزش شش میلیارد دلار در قطر.»
بر اساس این گزارش، ایران می‌تواند از این پول برای خرید کالاهای بشردوستانه استفاده کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76561" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7zP7gX3U3-ktNrBI_LPWxy4kSeWWKN8Hic3ssMExOyyOAsoIF5lNhaK2yoHilUCDi2YlRIEHcZBGjlZKrynT5jvuTazeGCjMnRgDGCGvF2N4_ozXjbWuNntLbWIhuPQFz0EHjSoSEzVmUs2_Q4RGzNKBELl_wL5mMHkoaSjTLIHH6ZdAbIlfaFxs0pds3DkucxFfD_IAv4x9sS-7VQfiGA1NTGOryi3j74jcqI6wX4BRkRZBHjE0rVAB6ARE_lvNdSOh4buav5CKYrh5oQQNit57LX3_qeD7u9WiaprbRw9FeJSEkiZD47y6VNJr_lU0rj0crEWHtn2O-oxKlxRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های بهداشتی در غزه می‌گویند که دست‌کم ۱۰ فلسطینی در حملات هوایی و تیراندازی نیروهای اسرائیلی در چند حمله جداگانه کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76560" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCEZkBnI_UD2eQzNCTgnaqnpVH8Zrzh14KloSbMuD-2B5IB3EyFKpnqC9yKiwQSx7HvaA8OiAVD8oly17OdrQ81xXfeKOePiRpZR7nsCHflGWfll0FCW_NNPiwMeiqGmsQpNmpWKNxzUiG1kZJHYLyVVaFHTzv7r7PWfecO3_BmljNX-rSDU8SnQX_L927eEDmCE6xEMff0niYIFKWIaB59LxVRJY173r-_KGm5pvB9RyHYxliq9Tg2Sl_cnYOd34PlMdAN0bStoKYYuuNM4AWishRjG1iKlVkzXO3UHa5yFHqNLs2QUroTOcmw6PGuDTBW4058lmPpS5Lu9HLWxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از هزار دانشجو و فارغ‌التحصیل دانشگاه صنعتی شریف با امضای نامه‌ای سرگشاده خطاب به محمدرضا تجریشی، رییس این دانشگاه، نسبت به آنچه «تشدید فضای امنیتی» و گسترش برخوردهای انضباطی با دانشجویان خوانده‌اند اعتراض کردند و خواستار پاسخگویی مدیریت دانشگاه شدند.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف تاکید کرد که بیش از هزار نفر این نامه را امضا کرده‌اند. انتشار این نامه یک روز پس از رسانه‌ای شدن صدور احکام اخراج برای شماری از دانشجویان شریف صورت گرفت.
امضاکنندگان در این نامه نوشته‌اند که در ماه‌های اخیر دست‌کم ۳۰ پرونده در کمیته انضباطی دانشگاه تشکیل شده و ۱۳ دانشجو با احکام بدوی تعلیق یا اخراج مواجه شده‌اند. به گفته آنان، احکام سه دانشجو نیز در مرحله تجدیدنظر تایید شده است.
نویسندگان نامه تأکید کرده‌اند که آنچه در دانشگاه می‌گذرد، ادامه «روندی نگران‌کننده» است که به دلیل نبود واکنش مؤثر از سوی مدیریت دانشگاه، هر روز ابعاد گسترده‌تری پیدا می‌کند. آنها همچنین نسبت به افزایش سرخوردگی دانشجویان، گسترش بی‌اعتمادی در فضای دانشگاه و آسیب دیدن اعتبار علمی دانشگاه صنعتی شریف هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76559" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xb6WYNHlT9qRJo9A7tjDhjOJRw6Z11TkJhiAHoiZmeaED5R5jqnH0QZrnenrK5Yi-iGmblAm1B93nA0Gd_61vIAUprujIvOKh8ziN199d6FDNJrvf5EuaviRSAf0ehLdiVF4af9TIFfAVEVxeOziJdCHBbSKH7Fd22aKWXlr3O0rV_p4ZdkfbKp8APuCMrb69M0vFMypWX6WwDZPdO6LHsXVResvhtObDPTo10OqTXFFORa4PjTFqoem2trEtl71-5_ZlVt69R9S7Hj8ZJEvdgiUhNIKn4pN1xfA-xqe8Z3WlIwUM9p8eg52iTUr0l89662sJAifoTfd0BfB_eTmyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5Ufa5v8QTs0IZ2oqM6lSt7nASaRg2II7wOm7k4O_ud40d-vZmdGeB2vCn4OCweHcph0Mf0cynvcJ1yLA6Rwlgkia5T2Gx3mBWF5tib3F6YJRBs9VjvBNEIKacTTdkAojn2SAt2_V6heIbDddgGH2Dc4SSr0sR0QkmPSrLYakowQnTcZzaKtx1t-Nh4hVqcOxrbkH2jyCmejmPFgRqBY2K4LP-64pbgIWY_JZswis8AUXuibB2HveSJcJ_dH6aEnVzpBOmHcfLjN9dFp6OHx8G4Rma6OuHiz0g6LbD9MQ5GXDxvIFalch2-fd04fQMmpQcluKEUJIEBnKo4MEPnkoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
جواد علیکردی، وکیل دادگستری زندانی، توسط شعبه اول دادگاه انقلاب مشهد به ۱۸ سال حبس، انفصال دائم از حرفه وکالت، دو سال تبعید به سراوان و دو سال منع خروج از کشور محکوم شد. جلسه رسیدگی به اتهامات او در ۲۰ خرداد ۱۴۰۵ برگزار شده بود.
🔸
به گزارش خبرگزاری هرانا، آقای علیکردی از بابت اتهام «اجتماع و تبانی برای اقدام علیه امنیت ملی» به پنج سال حبس و از بابت اتهام «فعالیت تبلیغی برخلاف امنیت ملی» به ۱۳ سال حبس محکوم شده است. پرونده او پیش‌تر در شعبه ۹۰۲ دادسرای مشهد مورد رسیدگی قرار گرفته و پس از صدور کیفرخواست به دادگاه انقلاب ارجاع شده بود.
🔸
جواد علیکردی در ۲۱ آذر ۱۴۰۴ توسط نیروهای امنیتی در مشهد بازداشت شد. او ابتدا به یکی از بازداشتگاه‌های امنیتی منتقل و سپس به زندان وکیل‌آباد مشهد انتقال یافت.
🔸
آقای علیکردی برادر خسرو علیکردی، وکیل دادگستری و مدافع حقوق بشر است که در آذر ۱۴۰۴ به شکل مشکوکی درگذشت. وی پیش‌تر نیز در پرونده‌ای جداگانه با اتهامات سیاسی و امنیتی محکوم شده بود که اجرای بخشی از احکام صادره
علیه او به حالت تعلیق درآمده بود.
@IranRights</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76556" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gDHYMMg4fp_y4nJRVC6VS4EiGsjhJQefG3VB73OOl0QLf0jNKCmo_y5eWr6k5ZloUPXNT6S7BBV4URtUqM-05ftl_ro5GEZspSL82WDjQTacTBjq5GhYhkwjPE1rV_2XZ76bHMhyo1oM5HZWI-lhwrIw_XQnyvXsOb2BCeVhW6xoBmn41Q5KnV4u7t0n8LFQJr6_sp8EmmnVq8hFgBY0KWOzdKjkqzUffqi4r3EWEOZ4BjHMh3j83zZILm6z07p_XM1qh65tDnVgxZL_ggfKtHQbldObidCFFlE7aqLT94DCqELn-B7bHZoHt0AwZNyt4gQGvAVDDO9IPtsryxGyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ‌گونه عوارضی در تنگه هرمز وجود نخواهد داشت مگر به نفع آمریکا
ترجمه ماشین:
در دوره ۶۰ روزه آتش‌بس، در تنگه هرمز
هیچ عوارضی در کار نخواهد بود
،
و پس از پایان دوره ۶۰ روزه نیز
هیچ عوارضی پرداخت نخواهد شد
؛
مگر آن‌که، در صورت تکمیل نشدن توافق، این عوارض
از سوی ایالات متحده و به نفع آمریکا
وضع شود؛
آن هم بابت خدماتی که این کشور به عنوان «فرشته نگهبان» کشورهای خاورمیانه ارائه داده، برای جبران هزینه‌های گذشته، حال و آینده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLy37MwH3Vt4iHo8trqPYuc10KgSJBq0M0oFCrxpL6c5xxLykhN1juXmUbaGZBlGGAMEeQgtr1hFDwUU8pLk2HVMnGHMRTvDk-5paDCbLCJuJBwX8jFETqNTjEP6uzZexGWDDUfm5OW8zrRQuZOkeKAs74fXgTcwPK9Py6aBv5-07o-pSwYpDq8srbzGnQ6QFTYoodEpS_wqy0ZP_e94M6WiUGxulMpBSGZyc95xtFXdwe9YW0fs9lNHFT_qCcUPdna8N8IhPSP-gGs0GErVrYKmNcKoFyGkK9Ik-84OgC83ief2tqcxoQonGLbRa0pLhp2Y73frGbpUqRclfi3InA9I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLy37MwH3Vt4iHo8trqPYuc10KgSJBq0M0oFCrxpL6c5xxLykhN1juXmUbaGZBlGGAMEeQgtr1hFDwUU8pLk2HVMnGHMRTvDk-5paDCbLCJuJBwX8jFETqNTjEP6uzZexGWDDUfm5OW8zrRQuZOkeKAs74fXgTcwPK9Py6aBv5-07o-pSwYpDq8srbzGnQ6QFTYoodEpS_wqy0ZP_e94M6WiUGxulMpBSGZyc95xtFXdwe9YW0fs9lNHFT_qCcUPdna8N8IhPSP-gGs0GErVrYKmNcKoFyGkK9Ik-84OgC83ief2tqcxoQonGLbRa0pLhp2Y73frGbpUqRclfi3InA9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبویان: مجتبی خامنه‌ای نامه داده بود که چرا شروط من رو در مذاکره رعایت نکردید؟
07:20
صدا و سیما: افشای مکاتبات مجتبی خامنه‌ای از سوی نبویان در شبکه خبر پیگرد قضایی دارد
صداوسیمای جمهوری اسلامی ایران اظهارات محمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس، در شبکه خبر پیرامون مذاکرات پیش رو بین ایران و آمریکا را «مصداق تخلف قانونی و مستوجب پیگرد قضایی» عنوان و اعلام کرد «مدیرکل مربوطهٔ این شبکه استعفا کرده است».
محمود نبویان، که به جناح تندرو موسوم به «پایداری» تعلق دارد، روز شنبه ۳۰ خرداد با خواندن بخش‌هایی از متن‌هایی که گفت مکاتبات مجتبی خامنه‌ای با هیئت مذاکره‌کننده است، مدعی شد رهبر جمهوری اسلامی در مراحل مختلف با روند مذاکرات و بندهای متن‌های گوناگون مرتبط با مذاکرات مخالف بوده است.
این گفت‌وگو پیش از آن‌که نبویان به متن نهایی تفاهم‌نامه برسد، قطع شد و موجی از واکنش‌ها را در میان دیگر چهره‌ها و فعالان رسانه‌ای جمهوری اسلامی در پی داشت.
صداوسیما در بیانیهٔ خود اعلام کرد نبویان در اظهاراتش «اشارهٔ ناقص و مخدوش به برخی اسناد دارای طبقه‌بندی» داشته و سعید آجورلو، عضو تیم رسانه‌ای هیئت مذاکره‌کننده و از چهره‌های نزدیک محمدباقر قالیباف، نیز او را به «تحریف عمدی متون» با هدف «فرار از پاسخگویی درباره ادعاهای نادرست قبلی» متهم کرد.
محمود نبویان، ۲۳ خرداد ماه، در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا، در یک برنامهٔ زنده در یک خبرگزاری نزدیک به سپاه، متنی را که مدعی بود تفاهم‌نامهٔ ایران و آمریکا است، روخوانی و از برخی بندهای آن به‌شدت انتقاد کرده بود.
نبویان یکی از اعضای گروهی بود که پس از اعلام آتش‌بس جنگ ۴۰ روزه، همراه هیئت مذاکره‌کنندهٔ با آمریکا به اسلام‌آباد رفته بود.
مجتبی خامنه‌ای، که پس از اعلام رهبری هنوز هیچ صدا و تصویری از او منتشر نشده، پس از امضای تفاهم‌نامه توسط رؤسای جمهور ایران و آمریکا در پیامی مکتوب اعلام کرد «نظر دیگری» داشته اما «با تعهدی» که پزشکیان به او داده، مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا گذاشته است.
@
VahidHeadline
حمید رسایی با انتشار ویدیوی بالا نوشت:
نبویان در آنتن زنده شبکه خبر، در حال تشریح جزئیات نامه‌های رد و بدل‌شده میان رهبر معظم انقلاب و شورای عالی امنیت ملی بود که پخش برنامه به بهانه میان‌برنامه به صورت کامل متوقف شد!
ما که از یادداشت‌های آن امام شهید در این باره اطلاع پیدا نکردیم ولی گوشه‌ای از یادداشت‌های امام حاضر توسط آقای نبویان در حال پخش از سیما بود مانع آن شدند!
صدا و سیما:
🔹
روابط عمومی معاونت سیاسی صداوسیما: به استحضار مخاطبان محترم شبکه خبر می‌رساند اظهارات یک نماینده مجلس دعوت‌شده به برنامه امروز زنده این شبکه و اشاره ناقص و مخدوش وی به برخی اسناد دارای طبقه‌بندی و مکاتبات مسئولان عالی کشور، مصداق تخلف قانونی و مستوجب پیگرد قضایی است و سازمان صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار می‌دهد.
🔹
شبکه خبر ضمن ابراز تاسف بابت بی‌توجهی مهمان مذکور به قواعد اخلاقی و الزامات آنتن زنده، به اطلاع می‌رساند مدیریت این شبکه ضمن پذیرش استعفای مدیرکل مربوطه، برخوردهای انضباطی لازم را به دلیل بی‌توجهی به الزامات برنامه‌های زنده و سهل‌انگاری در مدیریت حرفه‌ای به عمل خواهد آورد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76554" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bUQCnvy-PimIBtQps5Vyg2lv4GWJqLvH9ytrm3txg2t8oofU-JeQgQrQfIeZRq7pff4cPe-eVUwyVgDhWfBqzYQd2FBEK_tFySct_W7wufraqWEDArP5banGq_HDJNEWYoAzELrrkOeL1MA4cEGV0m4ucu_udTIFHM-AnVT94xNG5UA1Dqo0JDqc3vKzqMiKQj4LS7A9rvp3P7lCkWd3BjoZj1EFhwz7pkrN3TN8nxcHYfSSV4pqk1rJ8278F5_Xw5TPqxbDUe1kzNtbNmSrhAp6jcDWbGq9jIRLsbsa3EaIs7pQ8oUtvXb6AQTmjnfyxVG8u42tn6Z_WdGYaZ-owA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WT2UQ9CBPoelAD6zM4USxchU7l9yfwtg5_mejCiajFxi06GeBterPYBKsqH7EJQ7nfdO1XAHaaGCPyKLmG2KR2QqoQv3pchCJ0tEzvM4AxSgvR6NCZyjS2-ic0cnZLTq3_GEOBbY_si902IACVGac-qKZQr7ppLv_PmLAeyWHbfKTV8UXrBuk0mzVzvh87he9nZnpUOd024cIcPqQ4Uw6OiKmHtGlmdHy9sPd3rAlUPnqJFhMTkrNsZg_kDW2kuLzC3mGY4zdo5zDkbtusBKJZpSDKCQERnk-lQNLAIDekdJsnkFuPq-IMXsWTgp4XAwNpNLpF4n7yPBjsh5KqhREw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ در تروث سوشال نوشت: محبوبیت ملونی در ایتالیا به شدت کاهش یافته، شاید به این دلیل که او و ناتو در جریان ماموریت جلوگیری از دستیابی ایران به سلاح هسته‌ای، به ایالات متحده پشت کردند.
ایتالیا حتی اجازه استفاده از باندهای پروازی خود را به ما نداد که یک مانع لوجستیکی بزرگ بود؛ آن هم در حالی که آمریکا سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند.
رئیس‌جمهوری آمریکا در پایان با لحنی تحقیرآمیز تاکید کرد: اکنون که ایالات متحده ایران را از نظر نظامی شکست داده، او می‌خواهد برای بالا بردن آمار محبوبیتش دوباره با ما رفیق شود؛ اما نه، ممنون!
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، با انتشار بیانیه‌ای تند در صفحه اینستاگرام خود، به هجمه‌های اخیر دونالد ترامپ پاسخ داد و حملات کلامی رئیس‌جمهوری آمریکا را «بی‌دلیل و بی‌معنی» خواند.
ملونی در این پیام خطاب به ترامپ نوشت: «محبوبیت من به هیچ‌وجه به رابطه با شما بستگی ندارد و دوستی با شما نیز کمکی به آن نکرده است. محبوبیت من حاصل توانایی‌ام در دفاع از منافع ملی ایتالیاست؛ یعنی همان کاری که همواره انجام داده‌ام.»
نخست‌وزیر ایتالیا همچنین با دفاع از تصمیم خود در جریان جنگ اخیر و عدم اجازه به آمریکا برای استفاده از پایگاه‌های نظامی این کشور، افزود: «نحوه استفاده از پایگاه‌های نظامی آمریکا در خاک ما، تابع توافق‌نامه‌های متقابلی است که ما همیشه به آن‌ها احترام گذاشته‌ایم. تا زمانی که من نخست‌وزیر هستم، این توافقات نباید نقض شوند؛ چرا که ایتالیا یک کشور مستقل و دارای حق حاکمیت باقی می‌ماند.»
ملونی در پایان نوشت: «در هر صورت، میزان محبوبیت من اصلا به شما مربوط نیست. پیشنهاد می‌کنم شما روی محبوبیت خودتان تمرکز کنید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76552" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/smThNq3bFK332X38wAVRTirWYm6UQp8dM9vExyT7_Qr9OWGUScYwjPh7zhQRjQWoa3gW48dBIs2aOEEqhTR9dQl-p1dsMAk0bZXR5V-1-bVRbkN71OtEQbkovUa0NYfAkU0_3RfcY3cPghAqNSZlnHR5R-YkyXnjC7sVZomTQ_j7VGpXS9D38iCwi9ZnLMl_CvVpGioM7wF7JyaRJZFpH6Ke-YucYT3QeOJUJuRlR3uL28ocITWA8cJ8CyudYcNylDc-mhCYR45RVBGsEaPiSzfzeJeiNHaFpQvHUlf3ZZpO3-pLa9CgHiVy-hbU39mnMTlYIZHrXajcLItbbiKMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که هیات مذاکره‌کننده جمهوری اسلامی به ریاست محمدباقر قالیباف و با حضور عباس عراقچی، عازم سوئیس شده است.
بر اساس این گزارش، عبدالناصر همتی، رییس کل بانک مرکزی و علی باقری کنی، معاون بین‌الملل دبیرخانه شورای عالی امنیت ملی نیز در این سفر حضور خواهند داشت.
همچنین کاظم غریب‌آبادی، معاون و اسماعیل بقائی، سخنگوری وزارت خارجه و حمید بورد، معاون وزیر نفت نیز این افراد را همراهی می‌کنند.
پیش‌تر وزارت خارجه پاستان اعلام کرد که مذاکرات فنی میان جمهوری اسلامی و آمریکا، یکشنبه در سوئیس آغاز خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76551" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cagKKuExJ4E8sFBIptwRCJn7NePiEzPQ00OtQeuGrUWAy0P4hVNmIMsANh_yWGiM0RrwTrsJxN-Pe9GEmu4rihkxwfRpZPxNo5brqWK7Fer1sr9iCjoTt1gjOp7P66Lf9_f2cmwhFeMuFfrLuLv7QqBh1B70e2zlmrB1uJ9S9V1T-D9XwbfAyS--tWKAM205iYvwEWDHZ4qvVqoBdjoudv8fvnGbAxMe4ievpbMog6WYCd7F9Kegbl4LfI3XCUl9fR5QIlIt9J83muzxAmDFzToFaSzdrhdoizczGg1Xh6Vxwd81-syl58IFseNbHq-MYSPx5FDNkEMEXbrQWyFJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی مرکزی ایالات متحده،
ترجمه ماشین:
عبور کشتی‌های تجاری از تنگه باز هرمز
تامپا، فلوریدا — تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت؛ همزمان نیروهای آمریکایی به عملیات خود در منطقه کلی ادامه دادند تا از آزادی کشتیرانی حمایت کنند.
امروز عبور امن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری از آن عبور کردند؛ کشتی‌هایی که حجم زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل کردند.
مرکز مشترک اطلاعات دریایی این هفته اطلاعیه‌ای صادر کرد و در آن عبور امن همه کشتی‌ها را در یک مسیر تعیین‌شده تأیید کرد؛ مسیری که از ادعاهای خودسرانه درباره الزامات یا هرگونه مانع، آزاد است. جزئیات مربوط به عبور امن را می‌توان در اینجا دید:
ukmto.org
نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اجرا و به‌طور کامل برقرار و لازم‌الاجرا باقی می‌ماند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76550" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=YRMAdzYnQpsUEtzs09aHzMgkZF_x-K-kyrXOjZ9nnf6ojbUxTnrdc7l0D8NpJ4Q2jl8-Y_Lirj2O9IzlrSqJCny7TL-ELRkBRfT2JqxnZrmLHN8wT1ox99LFJUMeOrCN-q-I5Qr_AaRTos8NNRGCeJAojT7ttj11aAe1czkbCRNwbop5SCyibzsQ5rizX-MfrUrLnD7wlhIBNSzr2A_8V4xIfOVAnJA9CaW24qcrWTZ6WPM-jDuF28eD6uzJ_WD-fa2ziNBXcYFYp1fDpqIpUvAMSqMBskiA_dz5FV5_IjOKKi9Iue-jvRFEA2bRVvJN_Bj-Fs1NhLtAJfz34prgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=YRMAdzYnQpsUEtzs09aHzMgkZF_x-K-kyrXOjZ9nnf6ojbUxTnrdc7l0D8NpJ4Q2jl8-Y_Lirj2O9IzlrSqJCny7TL-ELRkBRfT2JqxnZrmLHN8wT1ox99LFJUMeOrCN-q-I5Qr_AaRTos8NNRGCeJAojT7ttj11aAe1czkbCRNwbop5SCyibzsQ5rizX-MfrUrLnD7wlhIBNSzr2A_8V4xIfOVAnJA9CaW24qcrWTZ6WPM-jDuF28eD6uzJ_WD-fa2ziNBXcYFYp1fDpqIpUvAMSqMBskiA_dz5FV5_IjOKKi9Iue-jvRFEA2bRVvJN_Bj-Fs1NhLtAJfz34prgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی پربازدید شده که مادر مانی صفرپور، جوان کشته‌شده در اعتراضات دی‌ماه، را در حال سوگواری برای فرزندش در کنار یک دستۀ عزاداری نشان می‌دهد.
عکس پسرش را بالای دست گرفته و می‌گوید «پسرم، پسرم».
مانی صفر‌پور، جوان ۱۸ سالۀ لاهیجانی، ۱۸ دی‌ماه ۱۴۰۴ با شلیک نیروهای حکومتی در محلۀ سلسبیل تهران کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76548" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76547">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQ9XqaK-zjxbbuSITouwfKH_q4ZJIZ4hI4no8xT58b6dWer57TPYilDoyxGh_Rfku8I1pMmVKGfmnMRfL5KeqjRqVb83RAnkN2k9odmu1n281GblL5zVUJybNN8sHpafOiQtcUMBpxfSLcRIOYZRxGMPOWy7qGjLNKWtXhtmUDc5_F_-cLmy7yZi2eElFC4LhRTBK-g7S0nIk2cmtnUMxnKDdJELMm6xCtLfkrTCwzVytl0xK2x672jXEzMccy5-zPOnwerb-RAJXCe9vBqdqiPRMV7IN48VMyDG1o617RZR_B8oxEulqcJ2AtxhieHkWRd7RGf_CPpqWGPvd80duQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد تنگه هرمز در واکنش به «نقض تعهدات امریکا در اجرای آتش‌بس» و «حملات اسرائیل در لبنان»، به روی همه شناورها بسته شد.
نیروی دریایی سپاه همچنین از شناورها خواست به تنگه هرمز نزدیک نشوند و هشدار داد در غیر این صورت، امنیت آن‌ها به خطر خواهد افتاد.
قرارگاه مرکزی خاتم‌الانبیا، واحدی از سپاه پاسداران هم اعلام کرد تنگه هرمز به‌دلیل «بدعهدی و پیمان‌شکنی» امریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه، به روی تردد کشتی‌ها بسته شده است.
قرارگاه مرکزی خاتم‌الانبیا روز شنبه اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.
خبرگزاری فارس، وابسته به سپاه پاسداران به نقل از یک منبع نظامی در نیروی دریایی سپاه، عصر شنبه اعلام کرد که تنگه هرمز از دقایقی پیش به‌طور کامل بسته شده است.
حملات اسرائیل به جنوب لبنان در روز شنبه دست‌کم ۱۰ کشته بر جا گذاشته است. اسرائیل اعلام کرد این حملات در واکنش به پرتاب گلوله‌هایی از سوی حزب‌الله، گروه مورد حمایت جمهوری اسلامی، انجام شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76547" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f6wVXXuAaoQj4aiL-bG8cKdJD3jx6gHDtUln-QcELsrvjTlCin9UmrA5oaqcTt-E4Kg0tF7XyelVRDBk5pup1TTkecVMSKhndyclXNBhFlxWTKwrjUAMiItuGUDWYAso5ErKqBxuwfNxB47FO4U8_g0leRrCStosK7c_wmUJG3AcxueMAcVnQzFcY79akxudAl2VFmBfmr5JeL8aCA4n0b1XdkZIfTS3XFoJiSaqXrf8Y8L2g_bHdenF0BGJfLdA0q6HftWHD1kwoTDSrdmlYknJbM1jxKzaE-f8gb8j-IR4x-RYciqvKmwQSHH7kJsMt5rvdyA2AUjlvila8EzxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، روز شنبه ۳۰ خرداد در گفتگو با فاکس‌نیوز اعلام کرد که استیو ویتکاف، فرستاده ویژه ترامپ و جرد کوشنر، داماد او، «چند ساعتی است» که در سوئیس حضور دارند و مشغول بررسی «برخی از ابعاد فنی این مذاکرات» با ایران هستند. به گفته ونس، کوشنر و ویتکاف در گزارش‌های خود تاکید کرده‌اند که «امور به خوبی پیش می‌رود.»
ونس همچنین از احتمال ورود میانجی‌های قطری و پاکستانی به سوئیس برای پیوستن به این گفتگوها خبر داد و افزود: «قطری‌ها و پاکستانی‌ها می‌خواهند مطمئن شوند که ما این کار را به شیوه درست انجام می‌دهیم، بنابراین من تلاش می‌کنم به این روند احترام بگذارم.»
معاون ترامپ که سفر خود به سوئیس را در اواخر پنج‌شنبه شب به تعویق انداخته بود، بار دیگر تاکید کرد که انتظار دارد طی دو روز آینده عازم این کشور شود. او با این حال خاطرنشان کرد که هماهنگی‌های این سفر «همواره یک رقص هماهنگی ظریف دیپلماتیک است.» این مذاکرات که پیش‌تر قرار بود روز جمعه برگزار شود، پس از وقفه‌ای کوتاه دوباره در آستانه ازسرگیری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/76546" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sY1-L86ZEfTp6Nje9SfSwqA7P8Lz145xK3iu-DKcCd_1mteseeFZ5C1tD8Xg3NYJ3EOUWiRQHtPaAESyz8u1eEGiTZ2tEN5lu4lCWm4bb1DoZ-YIDoQSkhZeEEb_9gZaDywQm2LMycpXgpVc5LS8ClSp0Vcr_LXy5j2Rd8TqTcmGc9IQx4BKKVXi097lJoal7AMw_laE-mdMnq0FyaIluN5nih8ehRI5YZhEELP4SZfENa5iJSH2GfaWrGEf-pHyghleeYQUueyGFw-ilsM6udjbop1mh7Sa0aYvd46Q2Ul9UidLeMw4L5Wcv-9u54Obwnw42HzNANpOm7MS5Fgo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«طاها نظری» معترض ۱۸ساله که پیشتر به‌دلیل حضور در اعتراضات ۱۸ و ۱۹دی۱۴۰۴ بازداشت شده بود، پس از  تشکیل جلسه رسیدگی به پرونده، به ۵سال حبس تعزیری محکوم شده است.
ماموران اطلاعات شاهرود، در فروردین ۱۴۰۵، طاها نظری را شناسایی و به صورت تلفنی احضار کردند. بعد از مراجعه به محل، این جوان ۱۸ساله به‌صورت موقت بازداشت و تحت فشار برای پذیرش اتهاماتی نظیر «ارتباط با تلویزیون‌های فارسی‌زبان و فیلم‌برداری از اعتراضات» به او نسبت داده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76545" target="_blank">📅 17:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fsERlmHkh5ObDML7LhMDgNGMRBsMwEMCjxTAeNNGfChj5T8zhfyyEclKnz1govn2VRa7qVtZPTN5A8fIfJPf8E8oLQYyrbNzrzejesInu22z8WLwF1cQvyuFBPEQ8pxOvrb67MPtnk2-Jv9ZSzOqnUrlG7Va6wPlCJfHf87BtrHAtvPFnemAsiH2uoYSbVfD1ffysvh_hL2by3-Fg6jj5XKdWH8ZW4zuWkrtA-gxz9TUFhbED-dCYJB7Z1SEccLIj4vp7iv3-FtkodiTmgVZdFlspiMmieNjOX6VkvfijndtLLvjcELF17wYqFTNGLgUXzy3ax03bWyJs-Nkvf9_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nortHowgdBxl8l0AjTrVKGvPV_pFu9kqLlD-tmhDxfbEy0BXIuTUb7lNBmwmVRocpJEpSYgaF-mwI5B6xsrbRLibYyK4dcjaGaOftZwOa9gusnITERehZxdOcOIQAC9-dRC6xNcsMlK-rYVM0JLE5zALl5G-lOAu3Hdt5SfDRlz1fj48PDYxPe9t4ZocodH41ghpUhfNlrcrYBp5hw3nnb8aL92-UQpZtXeAL6kXVF6QPM1xhVYKYMGpQSzaUgiMWWKDZ_wq1fRPaGnOMzT2oUFo9yamnpryEN1e7jhiNR7vwxireN_jC2FzRDHlDu4Qr_qLwwxE3EIu1JeYO5daJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت دلار و دیگر ارزهای خارجی که در پی نتیجه موقت مذاکرات ایران و آمریکا کاهش یافته بود بار دیگر افزایشی شد.
روز شنبه، ۳۰ خردادماه، قیمت دلار آمریکا در بازار به ۱۶۲ هزار و ۵۰۰ تومان رسید. قیمت یک یوروی اروپا نیز در این روز به ۱۸۶ هزار و ۴۰۰ تومان رسید.
این در حالی است که در طی روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسیده و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شده بود.
روزنامه هم‌میهن روز شنبه قیمت سکه امامی را در بازار طلای ایران ۱۶۹ میلیون تومان گزارش کرد.
از زمان اعلام تفاهم‌نامه ایران و آمریکا در تلاش برای پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران شاهد کاهش قابل توجهی بود.
@
VahidHeadline
حسین صمصامی، عضو کمیسیون اقتصادی مجلس شورای اسلامی، در گفت‌وگو با سایت خبری تابناک افشا کرد که در هفت سال گذشته بیش از ۱۳۰ میلیارد دلار ارز حاصل از صادرات به کشور بازنگشته است.
این در حالی است که حکومت برای بازگرداندن ۲۴ میلیارد دلار دارایی مسدودشده کشور وارد چانه‌زنی فراوان با دولت ایالات متحده شده است، امری که نشان می‌دهد تا چه حد به این پول نیاز دارد.
در این میان بیشترین میزان عدم بازگشت ارز صادرات مربوط به سال ۱۴۰۴ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/76543" target="_blank">📅 17:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WIvbfXjW-LzBaCiURfHiPPmnOgbWKt21z_1StwIDzslH_jKKNb-FWaHARTm-1jgYRNHGfcNRu1ZhWoFtnuwJD1B4dcBp9YKNqb6uSojx-DBTbTbK6bE9YkqNnW4kJwMplhpfgN9Qy2nMjjsBZom39EgiwKvUgHKIIyCdUjnd5YDk0tsooS1Vbm8PlqtVQQMR9leKoVp863Nk8ri1DLUqcP3klG4HQF4OnMOf8BOSl6Qu5fZFCEycWD33W_4VhMnK9KsPlc8EkMCMh8ap9tYnsTEbJcwSJazBCriqOmG4C_FHiS7oDsWBCpN48U0lNavnAdmsUnH4ym3O9GyN1eYKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=oM84l3vUHBD5kllv-V-W1DhGQ-grIW8pJ-ohx7wiYOAbifkKNN5Mk4mIfqP62qjlb5CFWR1jj9KRGnYIG2ZlEGzDHlcc-EzRDxv4fQGRohay3tVRiP6MDfkl6J3sSkzP_LHNDnNme0t9iee8iRLUEMZB14920hCbrbE6I8ToKn1m717hfxa1gtr6umQNA-uxhec4-2uvDZbC6a5QbwhJT8zTf9TC852rSJzdZJGvHI9GI-Xiv3LcEMe7TvcXB-1XP36I4pyK0i1KjCHfygbDBFwvaCabwQnauBlLg3gKqpH6zSPFhlBFPkTz4f4V-lSTVJCwBVyePHPYKpm7Baar1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=oM84l3vUHBD5kllv-V-W1DhGQ-grIW8pJ-ohx7wiYOAbifkKNN5Mk4mIfqP62qjlb5CFWR1jj9KRGnYIG2ZlEGzDHlcc-EzRDxv4fQGRohay3tVRiP6MDfkl6J3sSkzP_LHNDnNme0t9iee8iRLUEMZB14920hCbrbE6I8ToKn1m717hfxa1gtr6umQNA-uxhec4-2uvDZbC6a5QbwhJT8zTf9TC852rSJzdZJGvHI9GI-Xiv3LcEMe7TvcXB-1XP36I4pyK0i1KjCHfygbDBFwvaCabwQnauBlLg3gKqpH6zSPFhlBFPkTz4f4V-lSTVJCwBVyePHPYKpm7Baar1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که هاجر نادری، مادر متین پرویزی، در صفحۀ شخصی خود منتشر کرده است او را در کنار آرامگاه پسرش نشان می‌دهد که می‌گوید «من به پسرم فقط یاحسین و تشنگی را یاد ندادم، به او یاد دادم که جلوی حرف زور بایستد»
خانم نادری در ادامه با شرح کشته شدن فرزندش در اعتراضات ۱۸ دی‌ماه می‌گوید امسال محرم برای فرزندان میهن که «ناجوانمردانه کشته شدند» عزاداری خواهد کرد و ادامه می‌دهد که «می‌دانم امام حسین هم برای این جوانان عزاداری خواهد کرد»
متین پرویزی ۱۸ دی‌ماه سال گذشته در سبزه‌میدان زنجان با شلیک گلوله جنگی نیروهای حکومتی به سرش کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76541" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTl3nSQkP52QmlBRknGxwQMuiOjaISqlNqpqf2j59YHHBSWz4WY4Z2Gw5xtmYITJnYrJNwYTuHlp_Lev861BInedaBMjfRpuJJm7S0s66z4u9LMEvoDncorxsv7ObIQbAc1dNDyco_DdJ-GOyhdWxQ-09bpHpgFefabdydRhNmywAbGt0MCeyeDCJHFW9BeSS3Pw2YIOFdbCFqRVbHeSYMLfcKoOFQe67UA0Tt_Zt6eixAtB9FAWAN80fZI-As6C4R-2oX_RcsCM5jReSGrgniaN_hmvp_I8Nxs4-qVflv_hGkY8oQW8HcIwsW-g34dxMSC-64fY0wBDmjeEmimj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، صبح امروز وارد مشهد شد.
ایرنا به نقل از منابع خبری در استانداری خراسان رضوی گفته است که او سپس برای گفتگو با مقامات عازم تهران خواهد شد.
بر اساس گزارش‌ها وزیر کشور پاکستان قرار است در این سفر در مورد از سرگیری مذاکرات مستقیم بین آمریکا و ایران در سوئیس، با مقامات ایران گفتگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/76540" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATzYublnqjXOs6pqDeNdExYxqAWSJUpNrXj6SffxHYttN5Co1s69p6yN0THQ0x1yZ9G7IVQEZIWlQw6UudNEbrYUopzvZNeZS17f9fu77srdQ8jXp13wWj_lsfDBRQwzC9DgBcxiXBsgqOznEGK_rycLRe4ajLFDrojgiJqr_g6zB-BgRuoMh91Ws0BlNYGPzS5m5meNZC34nL5vCP0C6_pu0ELWG2FnUkMYbe2Lk61WzBH6Agk1BGWFGHbh84zaTtAvgfIHn-q7Zb37dtJ4kWBHjteygkTuHXoFWBJjsVPu6qR9WfjEklb5-Gxlp4EJTBlYAWNdfeAvRwDF1JXuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی پلیس استان لرستان از پلمب یک واحد صنفی و معرفی فرد متخلف به مرجع قضایی خبر داده و اعلام کرده است این اقدام پس از آن صورت گرفته که به گفته این نهاد، واحد مذکور «ضمن عدم رعایت قوانین و مقررات، اقدام به هنجارشکنی» کرده بود.
این در حالی است که تنها سه روز پیش نیز مرکز اطلاع‌رسانی پلیس لرستان از پلمپ پنج کافه‌رستوران و سفره‌خانه سنتی در سطح استان خبر داده بود. در آن گزارش، دلیل برخورد با این اماکن، اجرای طرح موسوم به «ارتقای امنیت اخلاقی و اجتماعی» و آنچه «هنجارشکنی» عنوان شده، اعلام شده بود.
در هفته‌های اخیر و هم‌زمان با فروکش کردن فضای امنیتی ناشی از تنش‌های بیرونی، گزارش‌هایی از افزایش تمرکز نهادهای انتظامی و قضایی بر حوزه‌های مرتبط با سبک زندگی شهروندان منتشر شده است؛ روندی که به نظر می‌رسد بار دیگر کسب‌وکارهایی مانند کافه‌ها، رستوران‌ها، فضاهای موسیقی، پوشش و نوع تعاملات اجتماعی را هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76539" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=iwYdftr9Qgi3m27_8GBhvq8OZ8fQhEMr41Qt5pxu_4OViK8-IPkF4YoX6AeS7cX_K7VTFM-eH7JL9z59wYWg2vuhspSQn2DwpUYGh_LO3AAn1Z2q3CAo2FN7BFMcAL0DUmyTmvpHIZrBYXMNjkgqNq9Ozr0njLjO-Q9cyLCMEkRor5RHXRJGFHdk89XcCNmWQYM4XTNbw-iZlb2Uy3aqz3x38SADqU_CdtJAIfcUlwc5_xJ7fy6jw9q0vZ9IsTrnUhnpOELFv0sXW5x0PFoGgbP3QNPf8U11C5ae-Eddw-f8uHDlt4QxMJ7zth4PU9_PCxpNSSJOGfkfcMa5csnBtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=iwYdftr9Qgi3m27_8GBhvq8OZ8fQhEMr41Qt5pxu_4OViK8-IPkF4YoX6AeS7cX_K7VTFM-eH7JL9z59wYWg2vuhspSQn2DwpUYGh_LO3AAn1Z2q3CAo2FN7BFMcAL0DUmyTmvpHIZrBYXMNjkgqNq9Ozr0njLjO-Q9cyLCMEkRor5RHXRJGFHdk89XcCNmWQYM4XTNbw-iZlb2Uy3aqz3x38SADqU_CdtJAIfcUlwc5_xJ7fy6jw9q0vZ9IsTrnUhnpOELFv0sXW5x0PFoGgbP3QNPf8U11C5ae-Eddw-f8uHDlt4QxMJ7zth4PU9_PCxpNSSJOGfkfcMa5csnBtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع‌های اعتراضی زنان به فعالیت‌های معدنی حوالی دو روستا در استان‌های کرمان و سیستان‌وبلوچستان با حضور نیروی انتظامی به خشونت کشیده شد.
بر اساس گزارش‌ها زنان روستای پشموکی از توابع فاریاب استان کرمان روز ۲۷ خرداد در ادامه اعتراضات مردمی نسبت به نحوه واگذاری و بهره‌برداری از معدن کرومیت پشموکی تجمع کرده بودند.
گفته شده که نیروی انتظامی علاوه بر ضرب‌وشتم معترضان، شماری از آن‌ها را بازداشت کرد.
هم‌چنین منابع بلوچ گزارش داده‌اند که زنان روستای سرسیاه از توابع تفتان استان سیستان‌وبلوچستان هم روز ۲۶ خرداد در اعتراض به گسترش فعالیت‌های معدن طلای تفتان و پیامدهای آن بر زندگی مردم منطقه تجمع کرده بودند.
در ویدئویی که منتشر شده شنیده می‌شود که مأموران نیروی انتظامی با خشونت، تهدید، توهین و واژه‌های تحقیرآمیز با این زنان برخورد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76537" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/egLF74GT2Etlxx2qX3nq8ws5t3G_ZMVHL3DUnZynT_VSbJQVkXLWl7ubD2BpAmV2w4-1F9fyDfvO4mOac4exki-NGXA18JrmEVQDaQI5h6gglNkmqFytWWdIW7tscytGdKA6O4hqHTYn90NcDU0QAXVQF4PeJBZwe103wVP9bJT7iUl_zEi49WFbYB4fMja87kgAWt45IEb10v3oH5Zp9FZ5qxAU1s58vrgKbX_m9L4rPE8yWt7wuS5kCRmOmmuSmLdyl7UCnjKqtxzyY4htpcZsIN9KPU34tb1QmUdA-qmTbJDyvmfIc5BMTusiGKrhcZoCeYjmpiC0xbHlM8RVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vsbtoyfZTuY79YDvWlvia1G-RaZ8KCngcjGQpCbU-wxvYYFy0B21HG8sfQ0--UY3ykxRd0ozOeSONCh08txyeIdvD08T-MZw_TeSJA__mxQ5aMRJf99fsvTKqSnKLrxkYg9UuVrvSmf7rMawDKs0kTqQyiKpwRm3NLnxJs6p1s2Euo8xC9jjK8UTXhIDpL-MZ3MkxWtjVjX1e0StRZ03RyTNNJdvqyyt4AYkMhUEydfjnw038flX6VUE_fHk1QWaYEToEzoTbCRn_ebjkmkzAflKVx55OTUPORl3F66fxs7gRx2xwams3ypE4QdURTt9j0oUQIg2Jlg8g1ozZDK1-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: استیو ویتکاف، فرستاده کاخ سفید، در حال سفر به سوئیس است، جایی که انتظار می‌رود دور اول مذاکرات با ایران در مورد توافق هسته‌ای احتمالی برگزار شود.
به نوشته اکسیوس، قرار بود مذاکرات جمعه ۲۹ خرداد آغاز شود، اما به دلیل درگیری بین اسرائیل و حزب‌الله در لبنان به تعویق افتاد.
@
VahidOOnLine
خبرنگار اکسیوس به نقل از یک منبع آگاه، روز شنبه اعلام کرد: «عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، در حال برنامه‌ریزی برای سفر به سوئیس در روز شنبه است.هرچند این برنامه همچون گذشته ممکن است تغییر کند.»
این خبرنگار به نقل از منبعی در یکی از کشورهای میانجی فاش کرد که عراقچی روز جمعه به چند تن از همتایان خود گفته است: «موضوع آتش‌بس در لبنان برای ایران یک مسئله حیاتی است و حکم برد یا باخت (تعیین‌کننده سرنوشت) را برای مذاکرات ایران و آمریکا دارد.»
خبرنگار اکسیوس همچنین به نقل از یک منبع دوم از میان کشورهای واسط افزود: «ایرانی‌ها صراحتا تأکید کرده‌اند که می‌خواهند پیش از سفر به سوئیس، شاهد برقراری و تثبیت کامل آتش‌بس باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76535" target="_blank">📅 04:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=U5UvkR2rENorgRUoPbsrxk3YCnjcnlhq8ppTaACiltvw-v77R-3RcvRSkR6RKsvAveIXZblNAiaSqJk5XOryxODyXhDDb03Mm2rOV16YScQwc2FnixZAVeibnhdi8ZrXXEf8wbsvFFsr1m6cx1BtqOupLfTCjxQIqqAgqmXQQsXNmAR7nHfLZ23B0VIGN_US5jL1SLB2WjzN5QYHPXjKNNjdl0yayg4jKA6ftFqlhW2cMHLDqNcQsG6f913C2aq7XuHPY_NA3kiDisokAQOSraTtf8YUYmxX64fPle3O6lO8gvoiMAu1DLGJVsonhKODiUGCRYOiBZFYbg9swlclOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=U5UvkR2rENorgRUoPbsrxk3YCnjcnlhq8ppTaACiltvw-v77R-3RcvRSkR6RKsvAveIXZblNAiaSqJk5XOryxODyXhDDb03Mm2rOV16YScQwc2FnixZAVeibnhdi8ZrXXEf8wbsvFFsr1m6cx1BtqOupLfTCjxQIqqAgqmXQQsXNmAR7nHfLZ23B0VIGN_US5jL1SLB2WjzN5QYHPXjKNNjdl0yayg4jKA6ftFqlhW2cMHLDqNcQsG6f913C2aq7XuHPY_NA3kiDisokAQOSraTtf8YUYmxX64fPle3O6lO8gvoiMAu1DLGJVsonhKODiUGCRYOiBZFYbg9swlclOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بخش مربوط به ایران از مصاحبه امروز ترامپ
متن کامل این بخش‌ها:
https://telegra.ph/trump-06-19
بعضی از جملات همان متن:
ترامپ: و من آیت‌الله را کشتم. یک مقام سپاه هم بود. و متأسفانه به آیت‌الله دیگر هم آسیب جدی زدم. به شما بگویم، من او را ملاقات نکردم، با او صحبت نکردم، اما دیگران درباره‌اش حرف می‌زدند. او شجاعت خاصی دارد، چون به‌شدت آسیب دیده است.
با وجود همه این‌ها، نمی‌توانید بگویید بی‌خیال. من ارتششان را نابود کردم. نمی‌خواهم این را نادیده بگیرند.
برای کسانی که می‌گویند شاید من به‌اندازه کافی سخت نگرفتم، باید بگویم من ارتششان را نابود کردم. بزرگ‌ترین پلشان را زدم، چون دیر در جلسه حاضر شدند. گفتند این کار خیلی قشنگی نبود. من گفتم پل جورج واشنگتن؟ سه دقیقه‌ای نابودش کردم. خارک را زدم، همه چیز را، جز یک چیز. گفتم به لوله‌ها دست نزنید، چون نمی‌خواهم به اقتصاد جهان آسیب بزنم.
بنابراین فکر می‌کنم خیلی سخت گرفتیم. به کسانی گوش ندهید که می‌گویند می‌توانست سخت‌تر باشد. کل ارتششان از بین رفته است.
پرسشگر: چطور تغییر رژیم است وقتی هنوز خامنه‌ای جوان‌تر و خیلی از مقام‌های سپاه آنجا هستند؟
چون افراد متفاوتی هستند. خامنه‌ای جوان‌تر با پدرش فرق دارد. افرادی هستند که بسیار کمتر از دو گروه قبلی رادیکال‌اند؛ و من هر دو گروه قبلی را می‌شناختم.
اما به این فکر کنید: همه آن‌ها رفته‌اند. بعد می‌گویند چرا سخت‌تر نگرفتی؟ تنها راهی که می‌توانم سخت‌تر بگیرم این است که دو یا سه هفته دیگر وارد شوم و آن‌ها را شدیداً بمباران کنم. اما این چه چیزی برای ما به دست می‌آورد؟ تنگه هرمز باز نخواهد ماند. فرض کنید این کار را می‌کردم. فرض کنید تصمیم می‌گرفتم این کار را بکنم. الآن بازار سهام ما فوق‌العاده بالاست. قیمت نفت در حال سقوط است. قیمت نفت تقریباً همان جایی است که قبل از شروع کار من بود. تفاوت بزرگ این است که ایران هرگز سلاح هسته‌ای نخواهد داشت. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت، روشن است؟ خیلی واضح و ساده است.
آیا می‌دانید در دو ماه گذشته، من کشتی‌های زیادی را از آنجا خارج می‌کردم و کسی خبر نداشت؟ می‌دانید چرا خبر نداشتند؟ چون ما رادارشان را از کار انداختیم. همه تجهیزات دفاعی‌شان را زدیم. آن‌ها قادر به دیدن نبودند. هفته گذشته، یک شب ۲۵ کشتی داشتیم، یک شب ۲۲ کشتی، یک شب ۱۹ کشتی، یک شب ۲۱ کشتی. هر شب، همه این کشتی‌ها بیرون می‌رفتند.
ایرانی‌ها مردم بسیار باهوشی‌اند. نوعی نبوغ ابتدایی دارند، اما باهوش‌اند. منظورم این است که باید جلوی آن‌ها را می‌گرفتم، چون اگر سلاح هسته‌ای داشتند، از آن استفاده می‌کردند. می‌خواستید ببینید؟ بگذارید چند شهر را در جایی منفجر کنند؟ مثلاً اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت. چون من توافق باراک حسین اوباما، یعنی برجام را لغو کردم؛ توافقی که مسیری به سوی سلاح هسته‌ای بود. آن‌ها پنج سال پیش به آن رسیده بودند. به نظر من، در همان هفته اول از آن استفاده می‌کردند. اسرائیل دیگر با ما نبود. اگر من آن کار را نکرده بودم، اسرائیل سال‌ها پیش از بین رفته بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76534" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfBOIjBq5sRm5gnEjQruoB2eiX-WW1HJYHEPcYNH3syyDdLdEWNqToUtWzpbHRLny_CKlFlK9UiqOgR6QOc0tIM9gllGAxJYdl9eZNn3Pn6tc76pVKOw6DxFF1bKwlJ54yRKqoAOQMuKPVBowZhbPxzi2UrFX_ABzF-D3qXM2AMK-QUQ6FfpskEXlFq01cD8jQlwYuWuJ6XkYG_fKy3onIjgJSA6Llt7C85SibLfYIj1V0GueA07mKyIPBZ2sBbuyEfoQDedfYJuzur2H-5PV1ggDU0k0v2GaCaMc9PyIH2c_cSaFLi1xyy5TXGITrccyKipNc4ftnDQQWKbgCwtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا، در مصاحبه‌ای با برنامه «آکسیوس شو» با دفاع از تصمیم خود برای شروع عملیات نظامی در ایران، مقام‌های جمهوری اسلامی را «بسیار باهوش» و «نابغه‌های بدوی» توصیف کرد و هشدار داد که آن‌ها در عین حال بسیار غیرقابل‌پیش‌بینی هستند.
ترامپ با اشاره به مداخله نظامی اخیر ایالات متحده گفت: «من مجبور به اقدام شدم تا جلوی آن‌ها را بگیرم؛ چون اگر سلاح هسته‌ای داشتند، حتما از آن استفاده می‌کردند و با منفجر کردن چند شهر، از جمله در اسرائیل، هرج‌ومرجی واقعی به راه می‌انداختند.»
او با تاکید بر اینکه اگر اقدام او در لغو برجام نبود، اسرائیل سال‌ها پیش نابود شده بود، توافق دوران اوباما را مسیری هموار برای دستیابی جمهوری اسلامی ایران به بمب اتم دانست. ترامپ همچنین با ابراز شگفتی از زمان‌بندی تقابل با ایران افزود: «چیزی که مرا غافلگیر کرد این بود که آن‌ها این‌قدر منتظر ماندند. آن‌ها صبر کردند تا من به قدرت بازگردم؛ البته این کارشان عمدی نبود. هیچ‌کس، حتی با وجود سلاح‌سازی ساختار حکومتی علیه من، فکر نمی‌کرد بازگردم، اما من با خروشی بزرگ‌تر از قبل بازگشتم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76533" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشجویان متحد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9YJdlmJu6V9fF2-29e78ImrzXbxw3WDcpsX8BRpnaquYUI5ZV07fSAVQ9AfEocmrrRZs1dpPHeEiMU154mvAzWZ5DBRSH4k-3C108dtzumAdCWPk-F4HpNHB1Cx201MxN_aODXncxasQw9G3eJkEVLox9cmJZ5f8xOTfNgwWGez52g7gokbKzufsckpLmBCN0vleSfeSd3XYib85C62EaGku-jpaLhQZmZP4Fl0zznG95_Nbpe23QLQRCANrpmRLh6EMDtBhKJWi4iKzFm7lT1ds5EmNIncel1Z9JZXuhxGPDxY8zOrJO29YvpKUEWxjMykONYmznc7f-TKQTpNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAEAel-yx1yrSXExbpDSh5REIIeWWB_Y_3NYs_cDUPRCnm-z4ODvgyF527Ntsq15tcx6_-Z_oMXxm6s7NhqS15G_1xLgAJ9PVSjBokxbz-tVMj4r_54vJBQN1OzSohA116EpiBLvo9N02mxKw8otfWW2NqSrmE_urofBZuLmnolZvrNBVC3fcr4NeyqxAble0aK_Oa4vJnfixOMcg9mZNePP19tmbpcxmWeul_BjR4VqQAskPIj5Xujgi7qAJ9IO6T8bb2tJdxbm_yd1lToy4o7oWq0ZOuX75SFrhM_dP1x9Cfd-lJjjBBfBFIZsnEWrJffxmLmzJyVHzAyBzdBB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IM9fVcpdQMFv6RtNI3xd9m-z_MglwRRhLIdjEJeQq4lxQzQPvqOH1HyPfwFOHQEATHZUv06zvoxfMuwWNeirnSoLP7x3psDH1lUL6bGUyH-U0WoIFfuUHp5Q7mw1TbBny4Gy49Res8yGTVTP4xfQ6M3dzJGlBvyE3WIsMKYNqFq4XbT1X5lFpXHr7u1Vnj1M_l3kV-f5cZ-RvhswIVRkkLLk0TmsM1-JdPhIs0sWUYDwy-liL8DdMKQRmSBoOLTlUHbV4BjnRz9dioVCcgTxIUmO-CI7AgfqyFZgw5DiRpAwsad2PkYoXdPTKIgiiKw8KK0RR8qibd-q9cdgCziIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJCyjwch0z-yVfHTBSCFiT182O5Hk2HvontHYh96jFEakAWKuHw8CKnmz7-rvAntew6Q7RsoIrNbGJrIvfxKqjF9AGNwdmxNW3uVLpEVH3zUQmzfUv8k3_uu08Wc1J7t7BDNoYlEJMx_ZXSXc0jOJcnjRHTP_ARdhK3FFcSM2KjK7Yut77CUAk3T17tHZMYhwEh0kHGEDLm8MpVshShPxl6KcxW_lLwTD5JbWMpuNOzX-kcXuqsJh5YN3k9Hl9UiRW2ztNlfKpw-CMWTN6tbKSgt2FvLmsFpzUexGlLe8TjAjtWA8ZurIlRfYkQ8-4Q6E5l8B2vtjHD-_QVfsAqctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kH9fzjYx4feKz2wucDhBFuYksFlUXLcL3jhbt8C2uIZwoI59-Azdlr15KsuwfOgL_8TsZwdqwOMZSS7LQg2mjw1zHPLO9IVa5wFVFru4tiG6TvWTikFILta1eB8dM1uPUKWzipII3RzYg4gig0CzF0xdHVNhFclrl51hH_GJ3-5OIu6tDw5LhdnHCwrzdsRyAAcZT_GmoiK8fmfzWHEDvqOQmP9to8qa2KLeiBGjzp3TlOEWIS7ZEDnz30neru5A0Rw3_mT5FeKg67iVT90Pg-ryHdWI_ULF0td5t70m7-dP3wM1Yx2kIEOcGperv7DSvcOSjWYl3-OD9S5PAxBQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTWGtwqkeQ5negeYGI67AzZHo9ddRhhm7wWvsVKzggTfaIcP1CGXuhHvfsuowO9LQSt6ccsa_f0oNWjpBCawwunG-jNM0ePfCAbfWl8KonWt3FRgbMCVxlh0jL4vy1cQMnWajE2C-vuV-D0UIBtLMrRmGYYUaKXs13sCKpRlTT8nd9Lrop154wrS6HVcfg7B__xh4QdY1l-NbYmo4f6rKg5CeBaU5tTXoxg_YjX7JexNiZVxYAe5DyfJO-4duoGdSIhxVUhfy0tnbD5Ky3kwJbGoLwg-J_4gAYGArv_4G8PtEsiND8Q21vSwXD1vr4OB6VP0AW9rqrc0ryvZxBwMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grQYNdbBJdvjQaQzHdJuf6S6GAaa1oMhMqI-rhloPGVl1aCz5W4ngv6FA9bAMOrzXaM8YTKc5jobtCft9_FOymRa3EqCP3luiYtaQuz7HwKUmxPAUtwodh5yaX4tsZUN0ffre8CpsUjDvFdFfHFQbyfvV0sI8i-3Zb5Vdm3SwqtPPrBBoGOdufdXiFLN0keqGWkfheizj1m35MVnQAFY3-tzceualLcWOHPajowjk-IYO08NfqfLLIxHEXUah7BxqNiN9qbjZxj64WjvEPaLoRXDEQ-3wczaYCrVix9D7fclkJvMkGGUDAggqo_u_NPL7wwRclscYU0yq0-f0GAa2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0owT-WRESdAG6A4dnynM1CgLtdANVLkgms0dTprbLLLir5OoV73GF3KJmRSwNcyRdhZGE9aqk9hBIXkoYvA2J9_OZD9dnu4dsasCMvjAVhXnLZMGhLbyw3F7EA-H7vHNknE4_2lYstQ9lqp5YmSBKnLf-tmMHA0_GGcOtg9uFxGPo07xBzcpOjZ3301wwlLqo2H9xbwV4BkItziPf86nqsTfMj67DgBNevMV23BZ9473cOQTwuRk7oBXbr5C6g-Ff0P42p8H0wIP0DJ20FcSqmekAhrFkOrVzqm4HLdJA-OCqkb3nZ_85AwY3NOFZgYxStGyNT-3s_gKFs44o7BJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
صدور حکم اخراج برای هفت دانشجوی دانشگاه شریف؛ صدور حکم غیابی برای یکی از دانشجویان بازداشتی؟
🔻
بر اساس گزارش‌های رسیده به دانشجویان متحد، کمیته انضباطی دانشگاه شریف، برای هفت دانشجوی این دانشگاه حکم بدوی اخراج صادر شده است. اسامی دانشجویان به شرح زیر است:
🔻
رضا دالمن، ورودی کارشناسی ارشد ۱۴۰۳ مهندسی کامپیوتر: اخراج و چهار سال محرومیت از تحصیل
🔻
فاطمه خاکپور، ورودی کارشناسی ۱۴۰۳ شیمی: اخراج
🔻
حسین شادمان، ورودی کارشناسی ارشد ۱۴۰۴ مهندسی صنایع: اخراج
🔻
سپنتا سعیدی، ورودی کارشناسی ۱۴۰۴ مهندسی کامپیوتر: اخراج و پنج سال محرومیت از تحصیل
🔻
مسیحا باقری، ورودی کارشناسی ۱۴۰۲ مهندسی کامپیوتر: اخراج
🔻
فریبرز کهن‌زاد، ورودی کارشناسی ۱۴۰۰ مهندسی برق(تغییر رشته به مهندسی صنایع): اخراج و پنج سال محرومیت از تحصیل
🔻
پرنیان خدابخشی، ورودی کارشناسی ۱۴۰۲ مهندسی و علم مواد: اخراج و پنج سال محرومیت از تحصیل
🔻
همچنین در برخی رسانه‌ها خبر صدور حکم اخراج برای «آریانا کوچکی»، ورودی کارشناسی ۱۴۰۰ مهندسی صنایع، نیز منتشر شده است. هر چند بر اساس گزارش‌هایی که به دست ما رسیده، ایشان در حال حاضر بازداشت هستند و خبری در مورد برگزاری کمیته بدوی ایشان نداریم. هر چند صدور حکم غیابی برای دانشجویان بازداشتی در جمهوری اسلامی، پدیده تازه‌ای نیست.
🔻
لازم به ذکر است از میان هفت نفر یاد شده، کمیته سه تن(سپنتا سعیدی، حسین شادمان، مسیحا باقری) با محوریت فعالیت در شبکه‌های اجتماعی و کمیته چهار تن دیگر با محوریت اعتراضات اسفندماه برگزار شده است.
ارتباط با ما:
@Public_anjmotahed
🆔
@anjmotahed</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76525" target="_blank">📅 22:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=sV1opP3FxHLIWhY7Jb__bR6hesKwCVnbwpq8ok31NfxPteKXtBmU-9qZeaon2e_GPR7EPlxUzM9LdhsNJ1Fvgz7NYE4-SuIn-44vjHhHL7YNPrgQnLMfW4mhQdSyDm4r-0X-oYCA0uiJuqX6xvTUqkRX7eDMe27LyNLwP6UIHfLX1KPSLFNjXJ9Zqjb672scDcDfCXudO3VQzt7wgcrDUFAe72Vz-7ZRW8OSRkPGYtFzcGJEIBju-x2_WR9WnX4a74QXoWfK61W110Xgfv3MEb60dTBLShKFWq0tVhMR9PHxesgByJiF0c4BZNiAMSGHhGT9jD2Hm5X8BCBgGiHchQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=sV1opP3FxHLIWhY7Jb__bR6hesKwCVnbwpq8ok31NfxPteKXtBmU-9qZeaon2e_GPR7EPlxUzM9LdhsNJ1Fvgz7NYE4-SuIn-44vjHhHL7YNPrgQnLMfW4mhQdSyDm4r-0X-oYCA0uiJuqX6xvTUqkRX7eDMe27LyNLwP6UIHfLX1KPSLFNjXJ9Zqjb672scDcDfCXudO3VQzt7wgcrDUFAe72Vz-7ZRW8OSRkPGYtFzcGJEIBju-x2_WR9WnX4a74QXoWfK61W110Xgfv3MEb60dTBLShKFWq0tVhMR9PHxesgByJiF0c4BZNiAMSGHhGT9jD2Hm5X8BCBgGiHchQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه جی‌دی ونس با زیرنویس فارسی
گفت‌وگو با:
الی بث استاکی، مجری و مفسر محافظه‌کار مسیحی آمریکایی، میزبان پادکست Relatable در شبکه BlazeTV
برنامه‌ای که در آن از زاویه‌ای مذهبی و راست‌گرایانه به سیاست، فرهنگ، خانواده و مسائل اجتماعی آمریکا می‌پردازد.
او در میان مخاطبان اوانجلیکال و محافظه‌کار آمریکا چهره‌ای شناخته‌شده است و در این گفت‌وگو با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره ایمان، خانواده، سیاست داخلی، اسرائیل و توافق با ایران صحبت می‌کند.
یک ساعت درباره مسیحی زندگی کردن
حرف زدند
و ده دقیقه درباره نقش و نفوذ اسرائیل در سیاست آمریکا و توافق با ایران برای مخاطبی از اون نوع
اینجوری می‌پرسه: می‌خواهید یک مادر معمولی چه بداند؟
متن این دقایق:
https://telegra.ph/JDVance-06-19
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76524" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ8R_05MhR0_aUtaduEdwcSkvComTQoWFa7o56yKM6rj63vLaD6jYQCZuvGmedVEFQMN-ESmgGc7U9wxYiRNSNNBdDRVwov_C2sCfay0bJ85w2cPEww2JnjVeeJc3g6dAumjpYJcCfk_lKgihgwBoCPc5-_ZniVTibH-0M5DVpKlOzZfwlAj1vaHlzk35SLY2dTpAreYKwXMb-QP4p0rau-Uh60aMBGI9vYMtNRsPqkhovKbyPa5mlgP5D6-eWWnF-OMvW11odTXmrN_-aqtcTU3nHlQFA5KyvJ-7y93xLOu1ZbPZc258bkMM-JL-zcRJiUwh4wBrIVE01RX8OdKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در یک گفت‌وگوی تلفنی با شبکه ان‌بی‌سی نیوز گفت که روز جمعه با مقام‌های اسرائیلی صحبت کرده و از آن‌ها خواسته است با گروه حزب‌الله بر سر آتش‌بس توافق کنند.
بر اساس مطلبی که خبرنگار این شبکه در شبکه ایکس منتشر کرد، ترامپ به این مقام‌ها گفته است: «بعضی وقت‌ها فقط باید آرام بگیرید و از عقلتان استفاده کنید.»
این خبرنگار همچنین افزود که ترامپ مشخص نکرد آیا مستقیماً با ‌بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفت‌وگو کرده است یا خیر.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76523" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iv_iSuuL8Drkajq7iMc-ALhTG8pTruuFq8KaSCYXVD7rs6Uf5cZE4AcKhfW23IePqEKftI3A0n9CtnTsELHHmaRCug7Kw1OPwJRdt5ZfumkZ9FT6-jhbmM9qeycFNd9gzh_rg4cxNNUizVURXsSJRmXzzgzhwSk2qkJCE7z3sra8xQuv6pavq_EyWreEabr3LjDEaOicGBBKCQ7DfSG4zywBb8qMx-_Nd9rCBhE6doUhvd1Sy81nZyA3V9W13tKDzXIqTG4V6s5tefhU_KqDSPnqJMSg1kXF5VnimOGLW7Xcu2hKeL-V8YBaKqGYzlBPRM9bzGZ07Ri9lGOo8IM5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
او تحویل سلاح‌های حزب‌الله را رد کرد و افزود این سلاح‌ها برای مقابله با اسرائیل هستند.
نعیم قاسم همچنین گفت که ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
دبیرکل حزب‌الله لبنان ادامه داد: «ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76522" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgAGrfEn76nwAZr_totZqNFmCYPgziwIELEp0VwdiotcYentaWugNriClLxWBhuXL06jrgyKFaQu-lIBsWXxMZ24tIMBbLMcgQl72bEyKXKB5iKeIcZmt7l-gQztQtdVim-gq4k-pK9xSXH5g7hhr8g2ZMi6MWo00jA2CkRtAPVA-3ujFQ3aCgNb9IZvvf9LopZnYHTHiZyKajYYj_qsuMCeKkYOo7KFyYMAQW5FYNj0tXfdq77GhRFojhhajVQ9P12QG0Cpp3TzfOuLQTUIymhtqiF_Z-x3fLAzl4KyGiM74xvLq6_SUcdADk4hAifsBxNrTEisCVbOKaBjq0AtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه ایران، روز جمعه دعوت جمهوری اسلامی از بازرسان آژانس بین‌المللی انرژی اتمی برای حضور در ایران و انجام بازرسی از تاسیسات هسته‌ای را رد کرد.
او گفت: «بازرسی از تاسیساتی که دسترسی آژانس به آنها به‌دلیل حملات نظامی متوقف گردید، منوط به روند مذاکرات و نتیجه آن خواهد بود.»
پیشتر جی‌دی ونس، معاون رئیس جمهور آمریکا پس از اعلام توافق اخیر در گفت‌وگو با شبکه ان‌بی‌سی گفته بود که بر اساس تفاهم‌نامه میان واشینگتن و تهران، بازرسان آژانس بین‌المللی انرژی اتمی «قطعاً» به ایران بازخواهند گشت.
اسماعیل بقائی همچنین گفت در حال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
نشست بین نمایندگان ایران و ایالات متحده که قرار بود جمعه در سوئیس برگزار شود، لغو شد.
سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد: «با توجه به اینکه امضای متن یادداشت تفاهم در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد.»
او همچنین گزارش‌ها درباره بسته شدن تنگه هرمز را «بی‌اساس» دانست و گفت کشتیرانی در این مسیر در حال انجام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76521" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76520">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4pDBK8RdfyHx3_qtfYzRtL3iOpYPZQQxVPLwoX5Ayx6W0F_6wAgWBpBwhluhBqOVqLsLAwiuUTAIZ6Am21eOpU7sGOVPyeqwKeqOPH1LiVjnVpjkZPhFqoJToES3i1yDshbvGfnQjCVidDBYdG1jv2M-5xlHtrKqPJRnJ10onNebBJjuu4ihSSs2kXeh85M2SrgeNckCXM9fjdRrasW7lCMusfrWUwiXJDFXFcapd5osg8vXHevFMQntM-TNWEBQFKuPBPbRByV9pWsE88lAbJp3id1_J-nMkKW5CVVHZ3hNNxmd4WoI1p7T37S74Ampsro3Fn7daAB4R6qTAesrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز گفت که اسرائیل و حزب‌الله بر سر یک آتش‌بس توافق کرده‌اند که قرار است از ساعت چهار بعدازظهر روز جمعه به وقت محلی آغاز شود.
این مقام که نخواست نامش فاش شود، افزود که مذاکره‌کنندگان آمریکایی و قطری با کمک ایران این توافق را نهایی کرده‌اند.
این مقام همچنین گفت: «درک ما این است که پس از تبادل آتش امروز، اسرائیل و حزب‌الله اکنون در وضعیت آتش‌بس قرار دارند.»
شبکه العربیه نیز به نقل از یک مقام آمریکایی از توافق برای برقراری آتش‌بس بین اسرائیل و حزب‌الله از جمعه خبر داد.
این در حالی است که نخست‌وزیر اسرائیل ساعتی پیش اعلام کرد نیروهای نظامی این کشور تا هر زمان که لازم باشد، در خاک لبنان باقی می‌مانند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76520" target="_blank">📅 17:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dTc5fopX7Dw3FHulG9iWHBJzS4l-LtClcp9XuOBaDWmIjoqTe2Qg3qL8Y828xdfLp2kN-yVG5TDH6zx8j4dFXWE2pAQXGUhMGbC2koJw1crVgn7DQ-qUn_J2er6XDxrpmjXLOmqIxw3erS0ghc60TI3CCtEIJPghlmZMwdXzLu9mBOyp1VGpu_FO0YYaNBQgGfibhvz037V8flX6ANo5c8wp4sqlt3oTPMHNai-8DxLGbKnYhwl-iHv2dJmSzJ4y66iZLkpHxk_28F5mCt_3kO9gF-kW_BisF8AiujNcwPr4IqZQUlk1_vtPMB4tiKhS5vwShgoooLG9cWSoVMbHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957528437f.mp4?token=CdsNH_DWvK3ZnSMKqgp7EGpaAxO9gzVuGWqYCqshGGB02yGfOiFyJPnum0MloAhWdbJL0FurZcF3k3ziTsnXu9jA_YdgpCAWYiuoiMBF5TV0ey7ymsq_D6CbCtRocjPFfe5Oj0clXRTrGqwKxHJ0PpnyYs2JU-ZsQQb5_4Z9mBbW1seeCTnD_ze736PFvE0DojLfnEu-d1empS45vgs_d1xZ-yqVzah9IRgqf82tHzFyisFYN9Fq6r4qqh7QS-NX_BtBhW_7ZoOhHvXR6jp44tY8GiLrghCKqdz8ZDwsv_Fdk3ii8Vvb4rXOhh_P5Nu_RT9UH-DbO7PMGSMINydM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957528437f.mp4?token=CdsNH_DWvK3ZnSMKqgp7EGpaAxO9gzVuGWqYCqshGGB02yGfOiFyJPnum0MloAhWdbJL0FurZcF3k3ziTsnXu9jA_YdgpCAWYiuoiMBF5TV0ey7ymsq_D6CbCtRocjPFfe5Oj0clXRTrGqwKxHJ0PpnyYs2JU-ZsQQb5_4Z9mBbW1seeCTnD_ze736PFvE0DojLfnEu-d1empS45vgs_d1xZ-yqVzah9IRgqf82tHzFyisFYN9Fq6r4qqh7QS-NX_BtBhW_7ZoOhHvXR6jp44tY8GiLrghCKqdz8ZDwsv_Fdk3ii8Vvb4rXOhh_P5Nu_RT9UH-DbO7PMGSMINydM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه ایتالیا روز جمعه اعلام کرد در واکنش به گزارش‌ها درباره اظهارات دونالد ترامپ سفر برنامه‌ریزی‌شده خود به ایالات متحده را لغو می‌کند.
آنتونیو تایانی در شبکه اکس نوشت: «سخنان شدیدا توهین‌آمیز رئیس‌جمهوری ترامپ… به همه مردم ایتالیا اهانت می‌کند.»
به گزارش شبکه ایتالیایی «لا۷» ترامپ درباره دیدار خود با ملونی در نشست گروه هفت گفته بود: «ملونی آن‌قدر می‌خواست با من عکس بگیرد که فقط از روی دلسوزی با او موافقت کردم.»
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، در واکنش به اظهارات اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا، این سخنان را «کاملاً ساختگی» خواند و گفت از نحوه رفتار او با متحدان «مبهوت و شگفت‌زده» شده است.
او تاکید کرد: «نمی‌دانم چرا رئیس‌جمهور ایالات متحده این‌گونه با متحدان خود رفتار می‌کند» و افزود این نخستین‌بار نیست که چنین مواضعی از سوی ترامپ مطرح می‌شود.
ملونی همچنین این رویکرد را «مایه تاسف» دانست و گفت او قاطعیتی را که در برابر دشمنان غرب نشان نمی‌دهد، در قبال برخی رهبران متحد خود به کار می‌گیرد.
نخست‌وزیر ایتالیا در پایان تأکید کرد: «یک چیز را باید به خاطر بسپارد؛ من و ایتالیا هرگز التماس نمی‌کنیم.»
در ادامه این تنش‌ها، آنتونیو تایانی، وزیر امور خارجه ایتالیا، نیز اعلام کرد سفر برنامه‌ریزی‌شده خود به آمریکا را لغو کرده و این اظهارات را «توهین به مردم ایتالیا» خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/76518" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsSXUabnt8NO5QFYpgrUh1lZxxlPq3tYpxIgLoTHDJ4gqkZy45RDakzTtWDC7i4RC2WDVo31hDBXbLyiAHa5OuYU7Hj5uTOxLS3MfgNduKOloxeJUaKJz9JdHW9OwIJozEArL4OJLRscrxiWfNNTg-0KIVyRDRQqjY91yI5FNobmwqamrEGZEAbL3Mlu-9cxO3NeYDQfUhl5lkVLpnZq9zxTENfWB57oMWD8NrhGfFrkZoX6452z5azholQr7TNCRd3eNK_MfSZl4xOKI8VyqkbjW0UR2mta9RKpNQ_c7ojTIHFDcR9b1l_W9wWSEInXajK-ZmeeIDWyxKrbyokB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
#محمد_نوروزی
، شهروند افغانستانی ساکن ایران، که در روز ۲۵ دی‌ماه ۱۴۰۴، در منزل مسکونی‌اش دستگیر شده بود، توسط دادگاه به شش‌سال زندان محکوم شد.
🔹️
طبق گزارش رسیده به کمیته پیگیری، محمد نوروزی پس از بازداشت به آگاهی ملارد منتقل شده و پس از ۴ روز همراه با ضرب‌وشتم فیزیکی به زندان قزلحصار منتقل شد. او طی این مدت مدام تهدید می‌شد که رد مرز شده و از ایران اخراج خواهد شد.
🔹️
او در نهایت با قرار وثیقه یک میلیارد تومانی از زندان آزاد شد و سپس توسط دادگاه به اتهام "اجتماع و تبانی و تبلیغ علیه نظام" به شش سال زندان محکوم شد.
این حکم هم‌اکنون در مرحله تجدیدنظر قرار دارد.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/76517" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76516">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWZDT7ZEZwhKr2drbQNlMc1Vv0RH5mvT__XLHZTweRPp6E4DrpH6FTUerUInMSP3Ug-lKUD6qF59NNhW2186cwcPKU7ZqEOA82lqq2PU1-xIWNSoOb0RmYQrRX0Pm-2Xuu5ELAw4AmoXO5RyjF_uoyNe148VDzXqOCfLMtAUewCmCpbbuXhaDmLCnQZUQlt8TylO_hruxSkwjHVCQda1auIFR6Tj0SJVn6S7c4sdc9ohWH7V7mxTnsU-vyQr0IntF3K-2O9YUDo5GVtKrtmnmzT2KiJgP-s_CBmoFiBhZnVONPQq-L-OGal_JIMJGhI6UMwA9FSw_QBt-r8jRPme7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز جمعه بار دیگر گفت که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در لبنان باقی خواهند ماند و وعده داد که حزب‌اللهِ مورد حمایت ایران برای حملاتش «بهای بسیار سنگینی» خواهد پرداخت.
او روز پنجشنبه، ساعاتی بعد از امضای تفاهم‌نامه پایان دادن به جنگ توسط ایران و آمریکا، نیز بر ادامه حضور ارتش اسرائیل در مناطقی از جنوب لبنان تأکید کرده بود.
نتانیاهو در بیانیه روز جمعه که پس از اعلام کشته شدن چهار سرباز اسرائیلی در لبنان از سوی ارتش منتشر شد، گفت: «اسرائیل حمله به سربازان یا قلمرو خود را تحمل نخواهد کرد و بابت این حملات بهای بسیار سنگینی از حزب‌الله خواهد گرفت.»
او افزود: «اسرائیل تا هر زمان که برای حفاظت از جوامع شمالی لازم باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.»
یسرائیل کاتز، وزیر دفاع، نیز گفته بود که ارتش در لبنان خواهد ماند و افزود که به هر حمله‌ای «با نیروی قابل توجه» پاسخ خواهد داد.
لبنان اعلام کرده بر اثر حملات اسرائیل در سراسر این کشور ۱۸ نفر کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/76516" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76515">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LOu9GYC3HGzqulpN65e3XBx1qeFt3TuyCaOQXf9OTIAlPIxcnIvk4xWYeFlIlAHKloMMHnKpaJmbgb6KX6VwT2b4P9yQcQudTOGoxGMgJulDMjSzlleShTpKMf4FydxasYEYQF_YwTGm2UWhMu8Ekr42pbo3GNT6f3XG4OTybg3cs_ySu1v0m0vklNiUuxcq6sQAmxtTZxN3Ov0FwAAZj6Stt8U0qzZJui3TaSuBx5pLRM-aP3dHFjdLjexTeEVfY9cmyFZMLz7IkYZsKnirludeNGB8bCar2p1s72o6B4t_wV-qE4j68MAD0W1snKBtNuBrl1Qf8uvINr3zSgPOVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینعلی شهریاری، رییس کمیسیون بهداشت و درمان مجلس جمهوری اسلامی، در گفت‌وگو با دیده‌بان ایران، با اشاره به ادامه «تعطیلی مجلس» گفت: «مجلس را بستند تا هر آنچه خواستند امضا کنند.»
او با تاکید بر اینکه تفاهم‌نامه با آمریکا در نهایت باید به تصویب مجلس برسد، افزود: گذشت آن زمان که برجام را در ۲۰ دقیقه در مجلس تصویب کردند. ما یک بار از این موضوع آسیب دیده‌ایم و نباید دوباره همان اتفاق تکرار شود.
شهریاری همچنین از اظهارات عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره احتمال رقیق‌سازی اورانیوم غنی‌شده انتقاد کرد و گفت موضوع هسته‌ای نباید در مذاکرات مطرح شود، زیرا به گفته او «جزو خطوط قرمز» جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/76515" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a5NW7LDDkTqe6LtSuSVfUozE7p18G4LYnII8_BUPWNrDojaUfjGbMHquy9WyxXKGZkgOayXmgWy2yYmcXO28Pl1lj2xyonGgW57zDhHodtgs8Q_fTUnH5SZwA4npsCUiY_B7BdbHCxLMgWMt_vsZ-YrvBW4v8iOsor0Ng6YwFlUiOTcQkx5_hNzNQ60vQAyev6uRbJdSR4v7PpJ2cXzR9x9GGfQFqXVAMVK9SCxHI8TX_dpAhoQg4Jx_pQ4de_8Lj1D7tNI1y9ssahCcMjvZ8Ezp1Prd0Mn_wIHsoT981crA3sQ6G6bkfr_eITyWHr1YxFSOG4sxRNRmolq4ARNHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام پیشین مرتبط با تحریم های ایران درباره «صندوق ۳۰۰ میلیارد دلاری»: پیش نیازش لغو همه تحریم هاست که دکمه روشن و خاموش ندارد
میعاد ملکی، مدیر پیشین «دفتر هدف‌گذاری تحریم‌های خزانه‌داری آمریکا» در یادداشتی درباره موضوع «صندوق ۳۰۰ میلیارد دلاری» برای ایران که بسیاری از کارشناسان درباره آن ابراز تردید کرده‌اند، می‌نویسد: با کنار گذاشتن موضوع معافیت/مجوز نفتی و نگرانی‌های مربوط به عدم اعمال تحریم‌های جدید، باتوجه به الزامات برای اجرای واقعی بند ۶ (صندوق بازسازی ۳۰۰ میلیارد دلاری) و بند ۷ (لغو همه تحریم‌ها) به این نتیجه می‌رسیم که مذاکره‌کنندگان آمریکایی یا می‌دانستند که توافق نهایی ناممکن است، یا این یادداشت تفاهم فقط تصمیم‌گیری را به آینده موکول می‌کند.
ملکی که خود در طراحی تحریم‌ها علیه حکومت ایران نقش داشته در این یادداشت می‌نویسد: این چیزی است که «اجرای کامل» در عمل، فراتر از امتیازهای هسته‌ای، به آن نیاز دارد:
بند ۶ — صندوق ۳۰۰ میلیارد دلاری:
صدور معافیت ریاست‌جمهوری از تحریم‌های الزامی بخش ساخت‌وساز ایران طبق ماده ۱۲۴۵ قانون IFCA (معافیت‌های ۱۸۰ روزه قابل تمدید که در هر دوره نیازمند اطلاع‌رسانی به کنگره هستند).
خارج کردن سپاه از فهرست سازمان‌های تروریستی خارجی (FTO)، زیرا در غیر این صورت سرمایه‌گذاران با خطر مسئولیت کیفری به دلیل «حمایت مادی» مواجه خواهند بود و هیچ مجوزی این مشکل را برطرف نمی‌کند.
استفاده از معافیت مبتنی بر منافع ملی در قانون ISA (قانون تحریم های ایران) برای سرمایه‌گذاری در بخش انرژی و نفت.
در نتیجه، هیچ نهاد سرمایه‌گذاری حاضر نیست میلیاردها دلار سرمایه را بر پایه معافیت‌های شش‌ماهه قابل تمدید متعهد کند.
بند ۷ — لغو همه تحریم‌ها:
ماده ۱۰۴ قانون CISADA (قانون جامع تحریم‌ها، پاسخگویی و واگذاری سرمایه‌گذاری‌های مرتبط با ایران) رئیس‌جمهور اختیار معافیت ندارد؛ تحریم‌ها الزامی هستند و لغو آن‌ها مستلزم تصویب قانون جدید در کنگره است.
ماده ۱۲۴۵ قانون NDAA (قانون مجوز دفاع ملی آمریکا) معافیت‌های ۱۲۰ روزه قابل تمدید که در هر دوره نیازمند ارائه گزارش اجباری به کنگره هستند.
تعیین بخش مالی ایران به عنوان «نگرانی پول‌شویی» تحت ماده ۳۱۱ قانون پاتریوت: این موضوع نیازمند مقررات‌گذاری جداگانه از سوی شبکه مقابله با جرائم مالی وزارت خزانه‌داری آمریکا (FinCEN) است و صرفا از طریق دفتر کنترل دارایی‌های خارجی (OFAC) حل نمی‌شود.
تحریم‌های مرتبط با تروریسم، حقوق بشر و موارد همپوشان با پرونده روسیه: هر کدام مستلزم اقدامات حقوقی مستقل و جداگانه هستند.
ملکی در ادامه می‌نویسد: «لغو همه تحریم‌ها» یک دکمه روشن و خاموش نیست، بلکه پروژه‌ای چندساله در حوزه قانون‌گذاری و مقررات‌گذاری است و کنگره نیز در آن حق رای دارد. و این پرسش مطرح است که چگونه می‌توان اتحادیه اروپا را وادار کرد محدودیت‌های مرتبط با ایران را که در چارچوب پرونده‌های مربوط به روسیه وضع شده‌اند، لغو کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76514" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3DIEtZc7x9zUZsycbf7cpGvE5CE7a-SoLU6p8hxFkGyqlmpve2jTz_DLtrKDA4nzxXz1MkApCMltSJtzsbhw6tfIoSN1V-VKFp3flmO90souBGf_0dEeS8HeuYpt65QXv8YrUxG1uoIMtdJPHNoj5n1fpEvVor3WCeDCM7rF3xZzGxju7s-AyTi6wu8cLPp3VjUt330Hhfk9ftHo9EedQOEmSkstnRbJZcscsg51T6q0Ky5qlEQP_x_zCJFUJZh-haaIO5-sHtytx1_rFH7Eu3eMN0WqtaquuJAQacLO3i_JrBV5rYIYetoPxjawdG7BERdf3hPwiFfy9plVdPdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه هاآرتص در تحلیلی نوشت توافق دونالد ترامپ با جمهوری اسلامی، برخلاف انتظار بنیامین نتانیاهو، نه‌تنها به تقویت موقعیت سیاسی او منجر نشد، بلکه شکاف بی‌سابقه‌ای میان واشینگتن و تل‌آویو ایجاد کرده و نخست‌وزیر اسرائیل را در آستانه انتخابات با بحرانی تازه روبه‌رو کرده است.
روزنامه هاآرتص در تحلیلی نوشت نتانیاهو امیدوار بود سفر ترامپ به اسرائیل و حمایت علنی رییس‌جمهوری آمریکا، مهم‌ترین برگ برنده او در انتخابات پیش‌رو باشد.
به نوشته این روزنامه، نتانیاهو انتظار داشت این سفر پس از «پیروزی کامل» بر جمهوری اسلامی، سقوط حکومت ایران و انتقال ذخایر اورانیوم غنی‌شده برگزار شود، اما اکنون نه‌تنها هیچ‌یک از این اهداف محقق نشده، بلکه ترامپ تقریباً هر روز با اظهاراتی تحقیرآمیز از نخست‌وزیر اسرائیل انتقاد می‌کند.
هاآرتص افزود توافق آمریکا و جمهوری اسلامی در اسرائیل به‌طور گسترده «فاجعه‌بار» تلقی می‌شود، زیرا ترامپ برخلاف وعده‌های اولیه خود، جنگ را بدون تحقق اهداف اعلام‌شده پایان داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/76513" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkSqIUG-rQBE_zSgdm_bQ0n4T-2LYoy4KRh9L8PtFLrwTrLtnrpBk2UgNdsniq_sXhdy2afkuPIvnHILf83fas0lrKsPpJrPk-rl-LAu-51KbxZq2SNlqtHHEN4Zz8JNRcqp7VW1IPm1JZx34D3A87W5ZkbfJt-ZHzWIHid2Bh9oFOS2kWj95LD19tZrIpq95_W57GD7UIyWL4bKd9KTUDYBbV04BFLphgqBmn4YZMtSzMfekJjC1nNnzdt3msGlRhvWqqjVM9LE9mPOJRsi3buRo6jbxoq-XBpBlA8tPQerq2Kcg6Z7ak-2nd0rHhjuGG05mqALtcHaFTtumbBtMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«معین بصیری» ۲۱ ساله، ساکن شهرک اندیشه تهران، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله از نقطه‌ای مرتفع و از روی پشت‌بام شلیک شده و به قلب معین اصابت کرده است.
او در پی این جراحت جان باخت و پیکرش پس از انتقال به کهریزک، به بهشت زهرا منتقل شد.
نزدیکانش می‌گویند پیکر معین بصیری را از بهشت زهرا تحویل گرفتند و مراسم خاکسپاری او روز ۲۱ دی‌ماه برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/76512" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BaM7_6amk0tqjXKFzgXsEt1fq1yg2b7zzDXlLlNxHgrmKd3YqxYYtDdONvI_YL8wlqdNi0EtqtST4NpY0ius7oei0XqlqjG7GDfCRpQviHaC56qmNyAA_W0T0bsCFkl_-Lxox9viL78OwZ8BsHBee3-B7bZB1UES5Y2YU3sHtae7rat1h4S8ieEyGAv53Opw_mQnZrYs5aKTkRtdXIzghGVdwfMNbH80b9B1pW1zM5ePuPvgawFyhshJlJGKkiu4gzHJPNo9UjRf7owZ9smgSRTL56M5J25JKB-gxS_qd1JtYEWGnsLVpjx-d5ZoY1Y1rFloPQWBC7UCSOnPk7QHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
«جنگ، ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات ضدهوایی، نه رادار، و عملاً هیچ چیز دیگری هم ندارد؛ با این حال دموکرات‌های احمق می‌گویند ایران الان از چهار ماه پیش وضع بهتری دارد. اصلاً می‌توانید تصور کنید کسی با چنین حرفی قسر در برود؟ بعضی‌ها چقدر می‌توانند احمق باشند؟؟؟
رئیس‌جمهور، دی‌جی‌تی»
realDonaldTrump
«ما از سرِ درماندگی دیدار نکردیم؛ ایران بود که از سرِ درماندگی آمد. کارشان تمام است! این ۶۰ روز را هم طی می‌کنیم. هیچ پولی گیرشان نمی‌آید، حتی ده سنت!»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/76511" target="_blank">📅 17:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fLHTeP1MvcIqe6hmO1KIlINTbWFkcpaCBRj2zaf40940nJis_Oyh7yHqHwDuplsUOwBYqBGcaAUQmbyZkpWzdmu2LUogeieTr0IAE1T-ihPfdrUAXSyOb0qg1aCoImxk_12wRmMgBrVzTPU2zwkqGSy9agcm9FgJq0SGuXvnj_SpW2k-q5QGTu4eeGNdJErp8n7YZMMe0_-xKe3D9mONAtsMs095H7bF1iqani2A93_OE5s07wb2EzxWEF-IazIlZBympiPTAjnwedv31EUABpagnXGO_kgGoiaQ3EGF-lZd1Ibzd6vq2dBrzbMHzUDHtGZu3WSW1XztxkVGWvTOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EjQulgtGTbs2I8GyzkulSPJBv_0kq9Aigek5cS4HTj6JyuQIh3oFfSIIgp0bEOfYBWK8P8_BieoIQYqUPpMIGtuxVWzqecg_Fo6pGlaUkesj2El9rWtpFElsAv9QzoCgbfcrnIQ1Ly5WFIctiqYUp5e6WKCd5NuuykQyWDviF7xEwyecqfXaj4UncMxd1AC0QcMuihtpxLp6zPQsxMc08NOffcVN6vHKGiLCHeVO6ua6HSGF87lob7m-tCDjrVG1_Cz8jSOkto5JzJv4x5fAbxkzEdwv6HKMzvayBYw4M2qAuq_5WoqHBwSvW_mY2XQlwdB9_Jlif1u6VsbZQ9HA0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر خارجه فرانسه می‌گوید پاریس تا زمانی که اطمینان حاصل نکند مذاکرات درباره برنامه هسته‌ای تهران انتظاراتش را برآورده می‌کند، با لغو تحریم‌های شورای امنیت سازمان ملل متحد علیه ایران موافقت نخواهد کرد.
ژان نوئل بارو روز جمعه ۲۹ خرداد این موضوع را اعلام کرد. فرانسه یکی از اعضای دارای حق وتوی شورای امنیت سازمان ملل است.
بارو گفت تا زمانی که مذاکرات آمریکا با ایران به ابهامات مربوط به برنامه موشک‌های بالستیک جمهوری اسلامی و حمایت تهران از نیروهای نیابتی پاسخ ندهد، ثباتی در منطقه برقرار نخواهد شد.
او افزود: «ما به یک تغییر اساسی در رویکرد ایران نیاز داریم.»
@
VahidHeadline
وزیر خارجه فرانسه: کشتار معترضان دی‌ماه را فراموش نکنیم، مردم ایران بزرگ‌ترین قربانیان جنگ بودند
بارو که با تلویزیون «فرانس انفو» مصاحبه می‌کرد در پاسخ به پرسشی درباره سیاست فرانسه پس از «امضای تفاهم‌نامه پایان جنگ» ایران و آمریکا در قبال تهران گفت: «مردم ایران، بزرگ‌ترین قربانیان این جنگ بودند. آن‌ها از یک سو گرفتار سرکوبند و از سوی دیگر به رویشان بمب ریخته می‌شود. ما کشتار ژانویه (دی‌ماه) را که در آن خشونت دولتی بدون تمایز، معترضان مسالمت‌آمیز را هدف قرار داد، فراموش نمی‌کنیم.»
فرانسه حملات نظامی آمریکا و اسرائیل به جمهوری اسلامی را «غیرقانونی» توصیف و بارها اعلام کرد که در این جنگ شرکت نمی‌کند.
دونالد ترامپ تفاهم‌نامه پایان جنگ با ایران را در کاخ ورسای و در حضور امانوئل مکرون امضا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/76509" target="_blank">📅 17:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76508">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUdUUSYiufsWnPxkI1ZJPEK5T_POf1h8btNuDOqWcemUDJOo2sA67mXAN6F1t5Q4M0GAO0cW4-NQX4JWsJZUbX6lm5vNDPXSwXaYo_4-ALxDt_4fjkOuPKR2ZTs2zFSz9gF62wU8c0pXQRy3RUli_fsrBpPWrNZsytbDc9nL9VRdZOEhdMT5nnMzhy81FFVH6mshu-YuBBKZDQnhwX17OFoLRv6DuXiyoRihLEVVIOQ_Vtvy5uHYWz-VkcDaWI4HJLPJeguEthgyB1fZaOF_8u57uGhF3zfGjAB6Ypdqw6ubkEo99DzT6KH-2JukWvxGYCGUR_QbF38nTZTpHBqNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال از قول منابع آگاه گزارش داده که طبق توافق پایان جنگ، ایران حق دسترسی به شش میلیارد دلار منابع مسدود شده در قطر برای واردات اقلام انسان‌دوستانه و غیرتحریمی از خود آمریکا خواهد داشت.
به گفته یک دیپلمات آگاه از جزئیات توافق، این منابع مالی به‌صورت مرحله‌ای و در بازه زمانی آتش‌بس تمدیدشده ۶۰ روزه آزاد خواهد شد و تنها برای خرید کالاهای آمریکایی قابل استفاده خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/76508" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76505">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVBh3Qj-pVp9DYb4NKbiq4yEln8pFbCG9ePzNz6AziGEdRdHz6xLbfgzrwGLmeWUQjA-s5_Q0bczUbgUZwmetOmvbp3n93HNwHvFUEjudnFK5yLFfP90DzkJ_6eVUj9S-METOrRCOypfTFQhAHskekYxIFCTwTzriqjDy1lpc_-3FKqKr2OuQJvOEx72PJ730dCupUxkjjrZIc1dB_4KxhFMnIi2ctYBCUAlMBDv5doWmozoH-siurtEwmtRcyHUDVby7M9lh8COQqAArQhf3vHaSm1ZePzBCynp8TEq5srwTgQ9ck4wB9X0slmbIrvqP64o8gC1tj9VZnKfcIakbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrdhP9VoJ34qweNSgU27T1Q56Jejn3VIrg7JL9RPFOdw5BWa0pL9lisIZopVDbjH7IaO8rkaHKVxFyxOyrKs3Y4ssczlFNyDUkhCR1kPKUDFz5Fl5S7MCUbxoto_xlRKY4mNAycus7VOUkbKJ94AzdMbGBdx86Sv1s6uiVpXfZg6yZWdUNDBf79UAvkemJk5hYTesFqb9WvC62x9ckAzSHgd0hew2FvHu1g0ZOVoTFD2vc-qxIXoF0HmEERcN4KcqBzUXYZy6_riCHbUENsIcgPcy8osDvumGDVGvtab1wbxgWCOfEuX4_BZ4isDAO6eywObf6DZb_SI37K6t7TGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibetR6sfb4EOlKjydQNnbMFpyY8CNBmwV8quIu1VtqdxF9uYc5P0p7n4gUPER4aJK984fCqX2TzBnVSPQfVBvuXpalF_SGcbfHuwiLgKblyuI9MN7JFwJTQFwnG_1on-UZafrnDy_2aUXjsFBW3KmR_O4I5HiI3AwDRx04OcGG4_2P-xrl9SvIceU1SmAA3NdlzpQLpImwQiB1eechwmW2rDiO5dcVVKaq4VproibMfN2aWYEGnnaAd1XGbhwvvIk1xC3tA1JjyocY3BR6KpVhKp3mb222tZSOR8SLfRYeenWWwxlaQnMT04hFgR7mWVfkDbqJJtTRCl2vWZatTQNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بيكر علی حسن‌پور را بعد از ۱۰۴ روز به خانواده
‏تحويل دادند
‏
🔸
⁧
#علی_حسن‌پور
⁩ در ۲۵ خرداد ۱۳۸۸ در خیابان آزادی تهران بر اثر اصابت گلوله به سر کشته شد. خانواده او پس از ۱۰۴ روز سرگردانی، سرانجام پیکر وی را میان اجساد مجهول‌الهویه پزشکی قانونی کهریزک شناسایی کردند.
🔸
اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است.
🔸
علی حسن پور یکی از این افراد است. سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/61687/ali-hassanpur
@IranRights</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/76505" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4jZBumB6iUeo2DWy-HhLCn97gOk0SshTLL4XPG3xk4405oodS_NQRJsGm73nF0N4s5aMoTFp7rxtqo09eubvrjF4bsBuevBWb1C5OF14nWByGNvoxtJZR9hRvmE9LTXdhZhfLtSmyOlg_orra3XObUeU-ky2Y65tMgzCz5fvqeU_yq5GT8-q98Xf0heS_eA8PXVBo461Xfn5EgbqCCawnpxR-zJUmFTb4pPTjk0rrvFiwm1BCXbHOlYFHYspcm8Xu_NL8z9pXn9FGGzqkroCaR3-u6bJY0Fs74_bX6l1vJrD314ZI04N-xyNMvwkVvvVvB_Xgn62oU9wNTdvqA5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ملی لبنان می‌گوید در حملات اسرائیل به شهرک‌های شرقیه، حاروف، کفررمان، کفرجوزو کفرصیر در جنوب این کشور دست‌کم ۱۶ نفر کشته شده‌اند.
به گزارش رسانه‌های محلی لبنان، از ساعات اولیه بامداد امروز، حملات توپخانه‌ای ارتش اسرائیل به شهر نبطیه و مناطق اطراف آن ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/76504" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KD_3_NsgQZQLPjPpq0bx9I6rItkSVqjE9rioMtG0dp8XasBl6RNtvFii09qtVRkBEfC-Dm6yfffvnfHDJTOFCDtHr5X70OsftL7MFG19NfQPqmjGoMoR3KrUxxsRWJ-_FGqT233E94txTg0Q6PeyCfn3aB5BFClKNCIhvGj6PlZzTZQ80dFZvyJFfoORKNdf1V8W50U5qOY0NaGO8bu259sM3SS9yrjZqHCPeLXqFGiwBbDtyKCjQur4an9pQf8Qrj9MHfmy8OVJ8-0NaPXmwFKpYljvftqa_Ktg3OUwYZOEkWW6H1i_29eBohGpi7SRIUiYwSwi19PcbpEtz8Qzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام کاخ سفید مبنی بر لغو سفر معاون دونالد ترامپ به سوئیس، وزارت خارجه این کشور اروپایی رسما خبر لغو سفر هیئت آمریکایی و لغو مذاکرات تهران و واشینگتن در روز جمعه را تأیید کرد.
لغو آغاز فوری مذاکرات بین دو کشور متخاصم تنها یک روز پس از امضا و رسمی شدن تفاهم‌نامه‌ای رخ می‌دهد که یکی از مهم‌ترین بندهای آن ۶۰ روز فرصت برای مذاکره درباره فعالیت هسته‌ای ایران است. قرار بود این ۶۰ روز بلافاصله در روز جمعه آغاز شود.
اما خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز پنج‌شنبه خبر داد که مذاکره‌کنندگان ایرانی پیش از آغاز دور بعدی گفت‌وگوهای صلح نیاز دارند نشانه‌هایی از اجرای توافق موقت از سوی آمریکا مشاهده کنند و هنوز تأییدی درباره سفر هیئت ایرانی به ژنو وجود ندارد.
در پی این انتشار این خبر بود که سخنگوی کاخ سفید هم در بیانیه‌ای که پنج‌شنبه شب منتشر شد، اعلام کرد ونس و هیئت آمریکایی آماده بودند به محض نهایی شدن برنامه مذاکرات، عازم شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76503" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g5Hv0n8m8UPzRSc6jwgO7BZB1vsfqXXXGUjSM2Xr3zpBw3s8BwIrsVLPuIquQNOkYFsJsESPDjSrI1SsvcNoPR0Nau_R1rGD5WOEGNnqfhqvFpQIXrya8cgYvJlu7zY4_T5kR3L323BlBDwcZ_o-5DspzmL_rDvuoSGuZrhCtMrSmLdl-PlBTFbjlEXdmll2GuXpDTk5bVFxihfEM_8vNc2-Xiwv5lqzgWT7lZHg-CoNCntwZDFA_FuRl3d4ua73qagW6Nx3eRlLmxhP75cZCyFUqeEtpomSEhm0rKJD8JqlvLAOcpnRx4OlVDYOnRForqvtDBd6xZzXw5z7Pecgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود قنبری‌راد، متخصص امنیت شبکه و از کارکنان یکی از شرکت‌های تهران، با اتهاماتی از جمله «اجتماع و تبانی علیه امنیت ملی»، «جمع‌آوری اطلاعات طبقه‌بندی‌شده» و «ارائه اطلاعات به اسرائیل» روبه‌رو شده است.
بر اساس گزارش‌ها، محمود قنبری‌راد، شهروندی ۴۰ ساله و متأهل، اردیبهشت‌ماه سال جاری در منزل شخصی خود بازداشت شده است.
یک منبع مطلع به دویچه‌وله گفته بود که او هیچ سابقه فعالیت سیاسی یا مدنی نداشته و به‌عنوان متخصص امنیت شبکه مشغول به کار بوده است.
گزارش‌ها حاکی است که او در تماس تلفنی از زندان، پرونده خود را «ساختگی» توصیف کرده و گفته است که برای پذیرش اتهامات تحت فشار قرار دارد. همچنین اعلام شده که وی از زمان بازداشت تاکنون از دسترسی به وکیل محروم بوده است.
بر اساس اطلاعات منتشرشده، محمود قنبری‌راد ابتدا حدود یک ماه در زندان اوین نگهداری شده و سپس به زندان فشافویه منتقل شده است.
همچنین گفته شده که او از نوعی اختلال عصبی رنج می‌برد و خانواده‌اش نسبت به وضعیت جسمی و حقوقی او ابراز نگرانی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VsDD6jAh1oRSDk82OXNl77ue27PE5ErxGDc0Q0MYWH0pHr6by00E3BdWBtOpMJWTp4z8aiBGq_yzGocspP2X5YlhopW0gH-Knmkzb2q67rJH9dPAyDOzwBbj1wipJnVv2t10HsmkgmWAOxX_sOSjYlyQhHa_ttMYY0a_Of-MZN1B_6UbX5uEnm4NVZoaczn5PDmmSSNlLQbeVmS6JeNKUhEiHqW3zruFoXTOVl1CQitCQ-WM5vik6cWk5pRkXuwNxdRPpiGKi1-nRPwvN1ZWYToRmQrFZ6RPSyPR3CtyHOJE5svtby-9xAivBNYNn25leMaJbSI67LUVxq9YeFmyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از امضای تفاهم‌نامه میان واشنگتن و تهران  را
منتشر
کرد.
این تصویر مربوط به مراسم امضای تفاهم‌نامه در کاخ ورسای فرانسه است؛ جایی که ترامپ در حاشیه سفر خود به فرانسه و پس از پایان نشست سران گروه ۷ (G7) حضور داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76501" target="_blank">📅 05:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MYU3sxnGN9FMRI836Auyt5ebpWdFAwIX71krVdN9RhtMmIDGussj8o4dEYFcdQ8G5MRjE12Ws9WtG5m8-xXB6OYZT2FuRiy51qOzbQpEz2w9Ti_CyzdziC6uhlJNGwRQQrlszixRAWDr4PbxtF_2QjqyGqcyAwe7c8BXkelhkVJaonLj06r-XgL0EoDpKUdRDC1wos2uVpz_69YLiuHXfkQzwALQUrbsbxpwK5JxcJAAl_TOdVcCQT_eQu11aBWesXTsrH0vStMH3in0xVJ7RmDjzikgi8Xuh0xdIdPL3-pKqxvg6YAnZjJ1Db6S2FpykzMJpqyoq_-CZyUb_imOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در«گفتگو ی تصویری با اکسیوس» گفت یادداشت تفاهم امضاشده با حکومت ایران را می‌توان «نوعی تسلیم کامل» از سوی تهران دانست.
او این اظهارات را در پاسخ به پرسشی درباره تفاوت میان خواسته پیشین خود برای «تسلیم بی‌قیدوشرط» و مفاد تفاهم‌نامه مطرح کرد.
مجری آکسیوس در این مصاحبه به ترامپ یادآوری کرد که در آغاز درگیری‌ها گفته بود تنها «تسلیم بی‌قیدوشرط» را از ایران خواهد پذیرفت، اما یادداشت تفاهم امضاشده چنین تصویری را نشان نمی‌دهد. ترامپ در پاسخ گفت: «خب، احتمالا در واقع تسلیم بی‌قیدوشرط است. فکر می‌کنم همین‌طور باشد.»
رئیس‌جمهوری آمریکا همچنین با اشاره به جنگ اخیر گفت ایالات متحده ایران را «کاملا از نظر نظامی شکست داده است». او با تمجید از توان نظامی آمریکا افزود واشینگتن توانست محاصره دریایی موثری علیه ایران اعمال کند و هیچ کشتی‌ای نتوانست از آن عبور کند.
ترامپ همچنین گفت پس از جنگ با ایران، محدودیتی برای قدرت خود نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76500" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hKk-muUrRFCVyCJfWbyfyDPHA1Lyncu7Vkmv1dx37MPqvfoZaMLQh0eaT5MmFbp7dnNyK95Co4Hjzv-2XeFq1FGsHGGbRWADl4X9Kv4xgLlepsa29NSKyHMXCoIEunayK72ZpDxDybNs4ANj0TcptXUrrE7H-Hs8Ltc85OtxmlvkAqqX6RbGzDSGWliO5haHVz3_SXdGBxmi7ezDw6l7VVSqf83WnLeDum3kr20YnhSoYo287bwCOKRbJaVMC4RZYOFKmxVdFKO_wytm15Sq3VFAQ5ytkQYq0S00K_WbmYOPCu5N4p_tgGuz8bjRDEGDac8exqTw6TqrJK7tH7QjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر جی‌دی ونس، معاون ترامپ، در اطلاعیه‌ای اعلام کرد که او سفر خود به سوئیس برای شرکت در مذاکرات با جمهوری اسلامی را لغو کرد، زیرا برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و تدارکات و هماهنگی‌های این مذاکرات ساده یا قابل پیش‌بینی نیست.
در این اطلاعیه آمده است: «برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و هیات آمریکایی آماده بود در نخستین فرصت ممکن عازم شود، اما تدارکات و هماهنگی‌های این مذاکرات هرگز ساده یا قابل پیش‌بینی نبوده است. در حال حاضر، معاون رییس‌جمهوری امشب عازم سفر نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76499" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aFIkQF7A05yD7im__4COCq8QUVxvCH28DpQ77UoQWvOlxP0Sli3ozEkpNX7BrZNijWtZwg6O-a6pKa3QBH9KgL9P49m6EtG5vi_GRpahPRTCFxSCKsXNhxVcBzhY7EZuF84LSxLw6Waz6X54PfZ9vitLF8YOXjfSs-feNRIiXIDyyjxuxAC69XXbcbvju0qNe2A-5GATl7md9Fp4D4ehB189x-jgZPOwjLChRC6hixvnPR9f_yaFD2mDAu9Enud0WmYWUOSO5bavnXxQnxnZ6j3vzkdfaVe-H_1K97RBNn5YkyY5XW3jBpr35g-0TwTXdtOn3jbWxVEsMwhqIYeZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آسوشیتدپرس گزارش داد استیو ویتکاف، فرستاده دونالد ترامپ، پنجشنبه‌شب در نشستی غیرعلنی با قانون‌گذاران آمریکایی اعلام کرده است تهران از آژانس بین‌المللی انرژی اتمی برای بازرسی از تاسیسات هسته‌ای خود دعوت خواهد کرد و روند شناسایی محل نگهداری مواد غنی‌شده را آغاز می‌کند.
بر اساس این گزارش، ویتکاف به رهبران کنگره و اعضای کمیته‌های امنیت ملی گفته است تفاهم‌نامه میان آمریکا و ایران هیچ توافق جانبی نداشته است. با این حال، تهران و آژانس بین‌المللی انرژی اتمی نامه‌ای جداگانه تنظیم کرده‌اند که در آن دعوت از بازرسان آژانس و ادامه همکاری‌های نظارتی مطرح شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76498" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7tH9idl3sy6Vmh0AvSmzV4quPE_U0-aQeZJAsSUhUJ5qRRzOSn2XhNlk5HdRp4lunhi0egoxYu97Y5x0oegiQB2XNaT0r8pHTdKLH6yoN2K-j10MSF3DdB8cWVaBNDXcmM7cbhgAAcAJ8B3bvIgrwXeuybeF2lRUX_nv6-u-t5LspSBtY4eItXqU3d44uulrVVv2gVRA8njzyXopsoK2rEV1WR5LCAUL9tqIl4NYDl2M_EUH4ivHpRODFGUb3-uky1XpuGqV6yCNcl5egmRaG-bx7_chIgt7z8it2g49OBWRiEDqg2QkY8zJGU8PqPCm_GgAJ0rDbsnv7qM5sGd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجه اتحادیه اروپا، گفت هنوز برای بحث درباره لغو تحریم‌های اتحادیه اروپا علیه ایران زود است و این موضوع پس از دستیابی به یک توافق هسته‌ای با ایران بررسی خواهد شد.
او پیش از نشست رهبران کشورهای عضو اتحادیه اروپا به خبرنگاران گفت: «زمانی که شرایط فراهم شود، کشورهای عضو درباره مناسب بودن لغو تحریم‌ها گفت‌وگو خواهند کرد، اما هنوز به آن مرحله نرسیده‌ایم.»
اتحادیه اروپا در حال حاضر مجموعه‌ای از تحریم‌های چندجانبه علیه بیش از ۷۰۰ فرد و نهاد در ایران اعمال کرده است که شامل ممنوعیت سفر و مسدود شدن دارایی‌ها می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76497" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpBErEp-SRdrIiDyWABmQwSMreerGZtDKp-6KGC8QU99PXQYZlJ6YAYNgLoFwkrE1trOpWfTSd5DEqZPWFhtGD0Mio3VnP2lhFMeTKYrh1ywORj_paC59tCmg2z9uHRtapx8Slc67ZoPsFRDVadxJzFnhuUsVMgM7PEuwtMHRjDqLAhyJop-VyZQtF0Z8JTqFIBDO8kodKYSYD_rdWMnl2lwtldabkmvc8HJYO_3g121_5HX5Wgs1byG0ntQWJuV0PX6qGyzsRpAZi9fKq5ZOcp1-zBsTWF1-Q_yF5bXK9lpTsPEz975OG_yKSRV4AN2YPEb1Jmz8TsC_eo8gRswGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین به نقل از یک منبع آگاه گزارش داد هیات مذاکره‌کننده جمهوری اسلامی به دلیل ادامه حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس برای آغاز نخستین دور مذاکرات ۶۰ روزه را به حالت تعلیق درآورده است.
المیادین افزود: تهران پیش‌تر به آمریکا و میانجی‌ها اطلاع داده بود که پرونده لبنان در ادامه یا توقف مذاکرات نقشی محوری دارد و هشدار داده است حملات اسرائیل تا عمق ۱۰ کیلومتری خاک لبنان نقض یادداشت تفاهم و توافق چارچوب است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76496" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P4gdz80xgZd_N7rXkz8ttxvDlFyovPLn4lfl5wkrfzNM_iUeItuBQvlsLCeCYHT2SnXmkE1eVKC0BfH4JctUeavBNk_9PubT3iwEnkzYGbUW90-L27HDMWPQgaJ-QTezSBupoQgYo8bHzqDM8U-daw7XfDxTFv_1ghJ4dtJrsImzqUhGMeWM4qK_DAoSI77DeUQ4Bv7l-40TauaZsuBA3S2csSx8Z75ZHx-Woo1dw538Ni_5k4bWrA2EvU6Lxt2b8q_-6pIZVBZH4Xfyfz9XfDAu56p3QznWGFtX0KUxLWkliGig8c6ubh1qbc-UcEQi_9877G2yx9ZL91ERgFE5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت کاخ سفید:
رئیس‌جمهور دونالد ج. ترامپ تهدیدی را حل کرد که واشنگتن چهل سال صرف مدیریت آن کرده بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
یک پیروزی برای آمریکا.
🇺🇸
WhiteHouse
ترجمه با هوش مصنوعی به تصویر اضافه شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76495" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jmWEUExPoVDdS9YeNsFpgJR9hqA0Fwoc5qIaC3IdpMhm1P8o2apcPi-8sA9pZgtYFR3gw1TUe42Vzgpl-9RCR6vTea-fINnFMAsRD0JMXCjfntk8cTKON-bFzYudD-adPr37JizBwKo5XdsjgGgwrXVbf5WXqiK9Zk7z6BoeBHGJnFntrMQ3LuccWAoJFttsTBHfzPuZP8eTHKu-O9uH4p35fEPNwuNDrNx6F_pjZp4S55dJSI_RuB7y591aDKOBzdraEU1br4Umu5elzuo6PzG-67walXfnMm0g2e-qUpCYliLBeLG5xYNUqLXLn0KzVy5O_0JJS6GagOF9tqDPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'
بیانیه شورای عالی امنیت ملی
'
منابع حکومتی:
🔹
در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (PGSA .ir) ارسال نمایند.
🔹
به موجب یادداشت تفاهم اسلام‌آباد، به مدت شصت روز، هیچ‌گونه هزینه‌ای از متقاضیان اخذ نخواهد شد و این هزینه‌ها توسط دولت جمهوری اسلامی ایران تأمین می‌گردد.
🔹
بر این اساس به مدیریت آبراه خلیج فارس دستور داده شده است، در جهت تحقق اهداف تفاهم‌نامه درخواست‌ها را با سرعت و اولویت رسیدگی و پاسخ دهد.
🔹
با توجه به شرایط خاص و وجود برخی مخاطرات ایمنی در مسیر عبور و به دلیل لزوم حصول اطمینان از تردد ایمن و جلوگیری از حوادث دریایی، لازم است کشتی‌ها در مسیر و زمان اعلامی به آنها عبور نمایند تا به تدریج، امکان تردد افزایش یابد.
🔹
ترتیبات اجرایی و جزییات فنی عبور از تنگه هرمز از طریق مدیریت آبراه خلیج فارس اعلام می‌گردد.
🔹
در خصوص سایر موضوعات، از جمله مین‌زدایی، اقدامات لازم مطابق بند ۵ یادداشت تفاهم اسلام‌آباد انجام خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76494" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76493">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jXEUElLzpctfDigdtBdbiSQesyrF9SOaJmyzRdPhZWrdQtWgCk7DDmRQVYwaibwSE5qu0ZY5SpgfOyF7itSbfceQ8idkXJMCkGzkJ4FhpEczy_OTu_qcOIULaqzjqyjO3YQWCjd4z6e2X0WtD-7d8YeIjoRu2hgnu52MUZ6NxWfmxiSGygr78RiZFGxATIEzR4qQbGBJoGQZsho-8eOQpwoLqQUaGMqd45ZNMPY7gIsLtKFkh6mLf9MWfup_eq8VYyDBkxocxhQuxqyJMjy-EfPbwEyl6aKtBNE8F-9rZw2rO2l69UvZYi0rEME6BYHpyGtpfiujl8u6gPPKok8bnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: انتظار آتش‌بس کامل در همه جبهه‌ها از جمله لبنان را دارم
ترجمه ماشین:
ایالات متحده به صلح متعهد است و ما همه در منطقه خاورمیانه را تشویق می‌کنیم که به تعهد خود برای فراهم کردن امکان پیشرفت زیبای مذاکرات ما پایبند بمانند.
بازارها از آنچه در حال رخ دادن است استقبال می‌کنند: قیمت نفت به‌شدت پایین آمده و سهام به‌شدت بالا رفته است.
ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76493" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76492">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPourostad وحید پوراستاد🔷(Vahid Pourostad)</strong></div>
<div class="tg-text">« پیام منتسب به مجتبی خامنه‌ای در واقع نوعی فاصله‌گذاری حساب‌شده با تفاهم ایران و آمریکا است. مجتبی خامنه‌ای رهبر جمهوری اسلامی اجازه امضا را داده، اما مسئولیت سیاسی و اجرایی آن را بر دوش پزشکیان و شورای عالی امنیت ملی گذاشته است.
پیام همزمان رو به داخل و بیرون نوشته شده است. در داخل می‌گوید رهبر با رضایت کامل وارد این مسیر نشده و دولت باید پاسخگوی نتیجه باشد. در برابر آمریکا هم این سیگنال را می‌فرستد که تفاهم، زیر فشار ترامپ و دولت او به‌معنای عقب‌نشینی قطعی نیست؛ بلکه مشروط است و اگر شروط ایران محقق نشود، موافقت نهایی رهبر با توافق نهایی هم تضمین‌شده نخواهد بود.
در واقع متن، بیش از آن‌که اعلام رضایت از توافق باشد، تلاشی برای حفظ دست بالا در مرحله بعدی است: هم مسیر مذاکره باز می‌گذارد، هم امکان عقب‌نشینی تبلیغاتی حفظ می‌شود, هم به واشینگتن گفته می‌شود که فشار بیشتر ضرورتا به انعطاف بیشتر ایران منجر نخواهد شد»
@pourostadv</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76492" target="_blank">📅 22:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AxFL548rYS5Ev0UJPeCuH7xzUVmVnHTcvXNtgstnMeugRA7qVBgpJTxEA7NDej4mUJm5iCXouwLjhdUIsIqQsdnTRYQYSLw0nYXtqhI3yg0FCRVXXuocsjBdnReAB1NlyvfJyZe8Ihfu0a7Xapo1pBvVzBnzV2Hhgcr2KdDMsrsJq8tieHhGCTVgAr8sJGjCie-4gVb4UEbT0cgtGQ87ojRBX0Ix9pssslNZNpoZ0Q2jm_qaMo5WL_--Aqon-BBdbsve04HT8yfx9MLbDbWFQdnP44JU3vsxpVhnvMMFLW9ZH_F1JIltVKdQ1rBFvKVNsyd_DvY5Bsw3L52_M494uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول
گردن‌نگیر
جوان شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76491" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JDNEgfideTq1xVrewT370bK7zQ-kTAY_I8hsWp6sV7srZg23db03cNp5tjTVi09YXSAIsGllJYZ5tNMijus2tejSJEk9DTArXu8C5VVVy323cgi7KiWAqx7xQSQNntfbWNlnENfob-VykJD4ljMOnOxsNNW5FjHuJYkvU-6EO21UGWHnJHW3bBr9Guv1hUu-o72hRy86VEcogMsKpyP02LDMF9L3gWgOPREVP6F2aR-o3Y6OZA6OHs2y5Jx3yCn9ukougPJvlp_kyb5KiQW_WJ6VQ2PS4nsfTM7Xm0myHYfkr937Di6ggO8_NKJWoFIUGaJ1joLfAApjV3fFP6lhrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پنج‌شنبه شب متن پیام مکتوبی منسوب به مجتبی خامنه‌ای را منتشر کردند که در آن رهبر جمهوری اسلامی درباره امضای تفاهم‌نامه میان ایران و آمریکا گفته است که «نظر دیگری» داشته و مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا دانسته است.
در این پیام درباره توافق با ایالات متحده آمده است:
«بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیت ملی از طرف خود و سایر اعضا در پاسداشت حقوق ملت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه آن را صادر نمودم‌.»
در این پیام به تفاهمنامه اخیر به عنوان «تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و آمریکا» اشاره و گفته شده است که رهبر جمهوری اسلامی و مردم از این لحظه «منتظر تحقق شروط گفته ‌شده» خواهند بود.
در این پیام آمده که مذاکرات حضوری آینده «به معنی پذیرش نظر دشمن نخواهد بود.»
VahidOOnLine
در تیتر و متن نامه و خبرهایی که درباره‌اش تولید میشه بسیار تاکید دارند که این تفاهم‌نامه‌ای بین پزشکیان و ترامپه و نمی‌گن بین ایران و آمریکا
در واکنش‌ها از کوچک‌نمایی نقش
قالیباف
یا محافظت ازش با سپر کردن پزشکیان هم میگن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76490" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UMlRgGwG51kX7G1VV1WZgW_62ZdOWgQ-Q_UcnQqByHBS_KT6M9kSR3opRMqXc1GelV4d-PXIFEc-fIrKqLMeEBoVTg_1NszUGZuBLJjH3EgRW5-rddrjdJx53dclVpscJO7jRicFyyQ5tyN_dPr56v4kinKUGzFWuL0rUNr71Q7QNwcZ7HYV1GNLbURARbtbjevABuY7qSXLB90qRfMT5JuMJ0sl6HENHTSH8ps8UK53W3hEZuV_IQbmpppOdjifhXx3s-ssXfu_qk3-fCHcliGPMelNyogzQCtuBRzLpuFqoVyLWehYFdIe9LdoPAlz8SYMi_4pednr1r204OOWxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!!
رئیس‌جمهور دی‌جی‌تی
(توضیح: Dumocrat بازی زبانی تحقیرآمیز با Democrat است؛ از ترکیب ضمنیِ dumb به معنی «احمق» و Democrat. در ترجمه می‌شود چیزی مثل «دُمکرات‌ها» یا «دموکرات‌های احمق» آورد، بسته به لحن مورد نظر.)
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76489" target="_blank">📅 20:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFuoWBq8IdOMPBwpquFtTp919VuLaA3YrliT92J9XsL0YmBx_gHyCqP5TRJM4-L_K-LqQIGEGFom-i3OA9YuwgDDw6RG7_vk50T5kAPPFtAjF2NtYPwyY1rHOPQ5Qtkk_q_AVE0DAH92-LP1DKBoNgv_1eH2I4t6m4f6s0gug01jZEQlosPO2c7SJWHIfC7bke-HmaRh35zNFxxz4-D87r8hnlbyvcPhAqLFsaZ_90V_E4SMK3X-3-v0Q4vX9UUFwvSv7wPFmRYFHII5xYjrf1Q3420hNhWvU2u4h08T9Fs1YG5zI_endjYadkwswwamKfRAHhZJZ-aBVO0-HE7zhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام پایان محاصره دریایی
پست سنتکام، فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
امروز، نیروهای آمریکا مطابق دستور رئیس‌جمهور، محاصره‌ی همه‌ی رفت‌وآمدهای دریایی به مقصد بنادر و مناطق ساحلی ایران و از مبدأ آن‌ها را رفع کردند.
نیروهای آمریکایی مانع عبور کشتی‌ها به سوی بنادر ایران در خلیج فارس و خلیج عمان، یا خروج از آن‌ها، نمی‌شوند.
همه‌ی تلاش‌های نظامی آمریکا برای اجرای محاصره متوقف شده است.
کشتی‌های بزرگ نیروی دریایی ما در منطقه‌ی کلی باقی خواهند ماند تا اطمینان حاصل شود که همه‌ی جنبه‌های توافق رعایت، اجرا و به‌طور کامل لازم‌الاجرا و مؤثر باقی می‌ماند.
CENTCOM
البته سنتکام ننوشته خلیج «فارس»
🔄
آپدیت:
توییت رو ویرایش کردند و در نسخه جدید اون جمله مربوط به خلیج فارس رو کلا حذف کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76488" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
