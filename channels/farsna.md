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
<img src="https://cdn4.telesco.pe/file/VAwxHeuMcfOYwO5FawhPWJ7MBR-AUhXN4O5UtwjA4BcyjoEbeLCa9Sy0bI8x88eMDohopdK0jYLx1eHL0Svnh2qTO7-lw-M8hzwHWLDnfO9Iz8Kh4VfAV3xjzufosKEcP7qD7gzdwiL6ZmfL5efg2q-z6SE4JsUYXA6-U7CBfBZJhlVuBUkeZFiuAEs9gYGuDvUHahJZMgx0s0a8vEnobYfsjbtQaP5q1aoa3J0hItAY4muLglAf9TiwUJIzqZsMyu50jxVs7gf_yMwsl98Qlcj5oiiC654AoVA0Itvhh0fLPxJoXuXur1AjnfBOiqAuvoacfu_Cwx0IPRGsffzAdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 22:23:04</div>
<hr>

<div class="tg-post" id="msg-461443">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مدیرعامل بورس تهران:بازگشایی نمادهای سهام عدالت درحال پیگیری است
🔹
سازمان بورس پیگیر برگزاری مجامع سهام عدالت استانی است. در صورت تأیید نهایی دولت و شورای‌عالی بورس، زمینه برای بازگشایی نماد این شرکت‌ها فراهم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/461443" target="_blank">📅 22:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461442">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آتش‌سوزی گسترده در مسیر خط لولۀ نفت عربستان
🔹
داده‌های ماهواره‌ای ستونی متراکم از دود سیاه بر فراز جنوب مدینه در عربستان سعودی را نشان می‌دهد و گزارش‌های منتشرشده با استناد به داده‌های ماهواره‌ای، از وقوع آتش‌سوزی گسترده در یکی از تأسیسات مرتبط با خط لولۀ…</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/461442" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461441">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f182f209a1.mp4?token=uFKNUetrH9Sw3oICGnMjzlsWqRCAyBzHQ4IblbWja2f5ZwreP9mYrdiwLVg5WMMqthtdD4ZwAWflxY9XJMwuUavFfBczkYVqo1TpKjQhGIUsMtCqa__bhZF3N9I4Ad1o_UhG-PVIgOKVM93pQTT8a0mNthI7HBbHWNw5KfLVxaoxNmKjE0N7q6XtDZIGy6xODdTZ8UPq1IvDw4_3MhfeB00ypWJ07RrmT_UAPWXOyGSdVnloptnYyLuf2IYJDnW2-FqH-vaiTYek2nbLGAVBoyvxmOcUeFO7dIxRTITVyAXsdz6xLO2yVX15PXe7U74F_RWmVOUVrdegP97XWpFkQ58Ct20CDDyJcwSIVC8S_32P3l3u-XSdwRK7OsTUFY2xMtalS5k3IRRgZIxSECY-VI8yMIW3yA_YMRp8M6cyiSyAMHkQBSowqDDYI8guD9CXWxpj1cdAiXMPrtjOxVPUr_1heN7FImmxF730a5f_C-OGrNI0if9fiKE2gucybMP1LvVOmtA5zbLUh1G2NW5AoxU7I2dT74DryueyGI2XGCjE-MHBq2kSdAGdb7mW96m2bV-9CTLVxS79SO-C-YlPsHZO9R2I03PPJTTKTu4Z2G_2Vzhzv4NYf2jY6WCfAfSOhHXMlxq-f6mcr1-ZY2yLw7BUG43BOQP3dlahsumzjl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f182f209a1.mp4?token=uFKNUetrH9Sw3oICGnMjzlsWqRCAyBzHQ4IblbWja2f5ZwreP9mYrdiwLVg5WMMqthtdD4ZwAWflxY9XJMwuUavFfBczkYVqo1TpKjQhGIUsMtCqa__bhZF3N9I4Ad1o_UhG-PVIgOKVM93pQTT8a0mNthI7HBbHWNw5KfLVxaoxNmKjE0N7q6XtDZIGy6xODdTZ8UPq1IvDw4_3MhfeB00ypWJ07RrmT_UAPWXOyGSdVnloptnYyLuf2IYJDnW2-FqH-vaiTYek2nbLGAVBoyvxmOcUeFO7dIxRTITVyAXsdz6xLO2yVX15PXe7U74F_RWmVOUVrdegP97XWpFkQ58Ct20CDDyJcwSIVC8S_32P3l3u-XSdwRK7OsTUFY2xMtalS5k3IRRgZIxSECY-VI8yMIW3yA_YMRp8M6cyiSyAMHkQBSowqDDYI8guD9CXWxpj1cdAiXMPrtjOxVPUr_1heN7FImmxF730a5f_C-OGrNI0if9fiKE2gucybMP1LvVOmtA5zbLUh1G2NW5AoxU7I2dT74DryueyGI2XGCjE-MHBq2kSdAGdb7mW96m2bV-9CTLVxS79SO-C-YlPsHZO9R2I03PPJTTKTu4Z2G_2Vzhzv4NYf2jY6WCfAfSOhHXMlxq-f6mcr1-ZY2yLw7BUG43BOQP3dlahsumzjl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۶.۵ ماه است خیابان‌ها قاب حضور ملت است
@Farsna</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/461441" target="_blank">📅 22:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461440">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
آموزش‌وپرورش اعلام می‌کند مدارس دولتی حق دریافت وجه اجباری ندارند، اما در عمل چنین نیست. به‌دلیل افزایش شهریه مدارس غیردولتی، تقاضا برای مدارس دولتی زیاد شده و برخی مدارس از این شرایط سوءاستفاده می‌کنند. با وجود نامه
آموزش‌وپرورش منطقه ۵
، مدرسه از ثبت‌نام پسرم به بهانه نبود ظرفیت خودداری کرد اما بعد از پیگیری‌های فراوان و پرداخت ۱۰ میلیون تومان، ناگهان ظرفیت ایجاد شد! آیا این عدالت است؟
🔹
اغلب
فروشگاه‌های موتورسیکلت در خیابان ۱۷ شهریور تهران
بخشی از پیاده‌روی مقابل مغازه‌شان را هم جزو مغازه حساب می‌کنند و با قرار دادن موتورسیکلت‌ها، عبور و مرور مردم را واقعاً دشوار کرده‌اند. مسئول رسیدگی به این وضعیت کیست و مردم باید به کجا شکایت کنند؟ بعضی‌ها می‌گویند این مغازه‌ها بابت
استفاده از پیاده‌رو
به
شهرداری
پول می‌دهند؛ آیا چنین چیزی صحت دارد؟ خواهشمندم پیگیری کنید.
🔹
بنده یکی از داوطلبان
آزمون استخدامی فراگیر ۱۳
هستم که تیرماه ۱۴۰۴ در این آزمون شرکت کردم و برای دستگاه اجرایی اداره کار پذیرفته شدم. با وجود گذشت بیش از یک سال و طی‌شدن تمام مراحل شامل آزمون کتبی، مصاحبه تخصصی و گزینش هنوز
نتیجه نهایی و زمان به‌کارگیری پذیرفته‌شدگان مشخص نشده
است. با وجود پیگیری‌های مکرر از هسته گزینش کشور، سازمان امور استخدامی و منابع انسانی واحد استانی، نتیجه‌ای حاصل نشده است. این روند فرسایشی، داوطلبان و خانواده‌هایشان را با مشکلات جدی مواجه کرده و ممکن است باعث انصراف بسیاری از پذیرفته‌شدگان شود. لطفاً درخواست ما را به گوش مقامات تصمیم‌گیرنده برسانید.
🔹
لطفاً صدای مردم
خمینی‌شهر و درچه اصفهان
را به مسئولان برسانید. جاده منتهی به کارخانه رب آیدا و روستای جلال‌آباد وضعیت بسیار نامناسبی دارد و خرابی آن به خودروها آسیب می‌زند. تاکسی‌ها نیز به‌دلیل شرایط نامناسب جاده در این مسیر تردد نمی‌کنند. این مسیر نیاز فوری به
آسفالت
و مرمت دارد. مسئولان کارخانه می‌گویند مالیات و عوارض شهرداری پرداخت می‌کنند و جاده مربوط به آن‌ها نیست.
🔹
من با هزار بدبختی و به‌صورت قسطی یک پژو ۲۰۶ مدل ۸۲ خریده‌ام و تازه این ماه قرار است آخرین قسطم را پرداخت کنم. حالا با این
طرح جدید اسقاط خودروهای بالای ۲۰ سال
، واقعاً نمی‌دانم باید چه کار کنم. اگر قرار باشد این خودرو را اسقاط کنم، از کجا پول بیاورم و خودروی دیگری بخرم؟ آیا مسئولان شرایط اقتصادی قشر ضعیف و کارگر را در نظر گرفته‌اند؟ کسی که با سختی و قسط و قرض توانسته یک خودروی قدیمی بخرد، چطور می‌تواند یک‌باره آن را کنار بگذارد و خودروی جدید تهیه کند؟ مگر مسئولان از درآمد و توان مالی مردم بی‌خبرند؟
🔹
لطفا مسئولین درمورد
بازنشستگان کشوری
چاره‌ای بیندیشند. با این
حقوق پایین
و قیمت‌های سربه فلک کشیده چکار کنیم؟ پول درمان پرداخت کنیم یا پول خورد وخوراک و مسکن؟
🔹
چرا به مردم می‌گویید خاموشی برنامه‌ریزی‌شده نداریم و بعد قطعی‌ها را با عنوان‌هایی مثل خرابی یا مشکل انشعاب توجیه می‌کنید؟ اگر محدودیت یا کمبود برق وجود دارد، صادقانه به مردم اعلام کنید. این تناقض‌ها بیش از هر چیز اعتماد عمومی به مسئولان را از بین می‌برد.
🔹
برای ما احراز هویت انجام شده و حتی به دفتر خدمات دولت نیز مراجعه کرده‌ایم، اما کالابرگ همسرم که برای زیارت اربعین به عراق رفته بود، هنوز واریز نشده است. کالابرگ من واریز شده اما برای همسرم با وجود انجام احراز هویت، اعتباری شارژ نشده است. احتمالاً افراد دیگری نیز با این مشکل مواجه هستند. خواهشمندیم مسئولان وزارت تعاون این موضوع را بررسی و علت
عدم واریز کالابرگ
برخی زائران اربعین را پیگیری کنند.
🔹
در
آزادراه حرم تا حرم
، دو بار از ما عوارض گرفتند اما متأسفانه
وضعیت آسفالت
در خیلی از قسمت‌های مسیر بسیار خراب و نامناسب بود. حتی بخش‌هایی که عوارضی پرداخت نکردیم، آسفالت بهتری داشت. وقتی از مردم عوارض دریافت می‌شود انتظار می‌رود حداقل وضعیت جاده مناسب باشد.
🔹
دیشب به داروخانه رفتم و برای بچه‌ام دو مکمل و یک کپسول خریدم. فردی که بیرون داروخانه نشسته بود با دیدن پاکت داروهای من گفت همین‌ها را از
ترب
بخر؛
نصف قیمت داروخانه
است. باور نکردم اما وقتی بررسی کردم دیدم واقعاً قیمت‌ها تفاوت زیادی دارد. واقعاً ماجرا چیست؟ اگر این فروش‌ها غیرمجاز یا کلاهبرداری است، چرا نظارت و برخورد نمی‌شود؟ و اگر محصولات با همان کیفیت و اصالت عرضه می‌شوند، چرا باید در داروخانه‌ها با این اختلاف قیمت به فروش برسند؟
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/461440" target="_blank">📅 22:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461439">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65f3678981.mp4?token=GbESNv23_-NoYC9oOm9mRHHGvEQ3lWVvWaDn99h0TXbtbnMGKlPlktJp-x0OcuvYC7rZ94znOkWKayuOaRbVUlfmeTjP_gBS1505Zkmdc0NUZzkx572aUoHasTMyGRiqWOXw7i0LXtm_vyoqXsXSPemC_652AjkMjwjUsCiCdDS4sXFC6ru15xTE2wsrdN4H5aCpwyOE0r73r0lfE7ynlB91ZOJ5dUaLBP2i6dbcjNXcVsybOyUNFfgIAIYmH3j08yux5zrQ3Q491cvd19QyEIsoCRYMtW1QjdOCuKv5GRrbUGEo7dRFWr3t1MQdHnCuc0dBhHqi81bm4H4AOlFS57en4xrQmyywCcvO2oTkLd5UsXLuiVHQ6wiatU1-6RZ5v2bubxw9djjFl0xtLixw0K7PLDEPmmSaSmNrlovmV02yPaaOJTDq2s_aaBettFoVoVN5_NrTGSf06v7DW97dDkQyTknxXEIj_bFwneehWd2OK4e7h65zVO1CpKesak9JuZcabB5nzJYpXseNxF23PWX1kwgaxXBDpVbwoVGDv9-YngVuV4gp8BinZ7cuyUYSRw6SGY6Rke48d7hVEzLpsbbnCL0hIoBWsaTwkx97WIjpNfFCDZveOwEDoYVxIu4b01565zmp5w3pZ-8Mm-D3NoILjNLuRonlKzs25THp_ZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65f3678981.mp4?token=GbESNv23_-NoYC9oOm9mRHHGvEQ3lWVvWaDn99h0TXbtbnMGKlPlktJp-x0OcuvYC7rZ94znOkWKayuOaRbVUlfmeTjP_gBS1505Zkmdc0NUZzkx572aUoHasTMyGRiqWOXw7i0LXtm_vyoqXsXSPemC_652AjkMjwjUsCiCdDS4sXFC6ru15xTE2wsrdN4H5aCpwyOE0r73r0lfE7ynlB91ZOJ5dUaLBP2i6dbcjNXcVsybOyUNFfgIAIYmH3j08yux5zrQ3Q491cvd19QyEIsoCRYMtW1QjdOCuKv5GRrbUGEo7dRFWr3t1MQdHnCuc0dBhHqi81bm4H4AOlFS57en4xrQmyywCcvO2oTkLd5UsXLuiVHQ6wiatU1-6RZ5v2bubxw9djjFl0xtLixw0K7PLDEPmmSaSmNrlovmV02yPaaOJTDq2s_aaBettFoVoVN5_NrTGSf06v7DW97dDkQyTknxXEIj_bFwneehWd2OK4e7h65zVO1CpKesak9JuZcabB5nzJYpXseNxF23PWX1kwgaxXBDpVbwoVGDv9-YngVuV4gp8BinZ7cuyUYSRw6SGY6Rke48d7hVEzLpsbbnCL0hIoBWsaTwkx97WIjpNfFCDZveOwEDoYVxIu4b01565zmp5w3pZ-8Mm-D3NoILjNLuRonlKzs25THp_ZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌اللهی که منبرش سنگر مبارزه بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/461439" target="_blank">📅 21:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461438">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7928214bf2.mp4?token=Bg93T9NdSkN6_g8d8rlOM8XRypZVuzY9sCSo9dNbzAG90nGnvUs92-I1U1Jxr7buv1CTGTFB2PICGrp0SGCw289YTjl_3T478xMU9rycPT1K_vM6AUGaIzGODO8ejrS9C4ODs_YofFCnhVfGY1-Byb5Xcc19yEGzQ5wVV1SRnxob6HWhz5pmfRXQQy35rgB6X8wC8qMzvMgEg-mUOBtCtga1oKrrWOEIcjIS2ByKN_LyYDjzSQj-4TQfpq8yumq8_rIm4gObJ3Tin108zVZVtgq3n6aBRfp-muy7P6BqUTRqx-2a-F44GYZ4-lsAcEX9BCZlwkA42_r6Ja0T2fP4YzEqYTk-CNBJnxKEwntyTgKQhoxhHhcmFRdCUS9jj4OH-4ainuAzsglwlcISOnmgPinTRcEWTwnB7sXIEv0BvY9t--YCnZz61I2aRB3svAZvSms2rUKXlkOv3b_jX8A0aickzcXwbdCoLec9EBj3ImCYdKcxbuTWjs4VTCfhhqLnNxOHSNKxcbmdRDBPLHPIvJXq1M15TPjgo6Xw4BsWRZzuJWiLUliNi_7my4OQFe_pZpjqpTMV_47UgpddLavZNyveDpYRh2tXSD0ZNXVsrRcIoax-aneIWQ60YzzjobPyndP9t5TG5yUDlEzNqDt_O-z01BDLBLqA-2F8KsD3pKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7928214bf2.mp4?token=Bg93T9NdSkN6_g8d8rlOM8XRypZVuzY9sCSo9dNbzAG90nGnvUs92-I1U1Jxr7buv1CTGTFB2PICGrp0SGCw289YTjl_3T478xMU9rycPT1K_vM6AUGaIzGODO8ejrS9C4ODs_YofFCnhVfGY1-Byb5Xcc19yEGzQ5wVV1SRnxob6HWhz5pmfRXQQy35rgB6X8wC8qMzvMgEg-mUOBtCtga1oKrrWOEIcjIS2ByKN_LyYDjzSQj-4TQfpq8yumq8_rIm4gObJ3Tin108zVZVtgq3n6aBRfp-muy7P6BqUTRqx-2a-F44GYZ4-lsAcEX9BCZlwkA42_r6Ja0T2fP4YzEqYTk-CNBJnxKEwntyTgKQhoxhHhcmFRdCUS9jj4OH-4ainuAzsglwlcISOnmgPinTRcEWTwnB7sXIEv0BvY9t--YCnZz61I2aRB3svAZvSms2rUKXlkOv3b_jX8A0aickzcXwbdCoLec9EBj3ImCYdKcxbuTWjs4VTCfhhqLnNxOHSNKxcbmdRDBPLHPIvJXq1M15TPjgo6Xw4BsWRZzuJWiLUliNi_7my4OQFe_pZpjqpTMV_47UgpddLavZNyveDpYRh2tXSD0ZNXVsrRcIoax-aneIWQ60YzzjobPyndP9t5TG5yUDlEzNqDt_O-z01BDLBLqA-2F8KsD3pKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین وحدت در شب ۱۹۵ تجمع مردم مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/461438" target="_blank">📅 21:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461437">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یمن: ۵۴۰۰ کیلومتر را آزاد و ۹ هواگرد سعودی را سرنگون کردیم
🔹
ستاد نیروهای مسلح یمن در بیانیه‌ای دستاوردهای خود را نبردهای روزهای گذشته با مزدوران سعودی را اعلام کرد.
🔹
۱. بیرون راندن نیروهای سعودی از ۶ منطقه در استان‌های تعز و الحدیده، با مساحتی کلی معادل…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/461437" target="_blank">📅 21:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461436">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f433103ae3.mp4?token=PlBb1SwnoB5cLMbBYrJfVb-AO9Cp31nIn_rDMvJLOjjsQDjpL9CSNobHAj6UMN4BB9HK740LTtkeZfWyTpLa94ilznixS89BinksQJNVuONitzp305z_X38wXgcSeKjXpbvRrBmEWKYz3oEdMPToZV_fGiF94CyX9b6kmolXIovpzHWxPC8dqHiTNsa70Ppg2H_XHHSMViw-2RIGCI-xZw_Owc5hmj0nSIiTrY4kxLODl9nvk0DTbv3_RwAOZKPNCg1G3PUqAJfWcskVrJhRCNqIVWrWIiSwSL8FZ7y5k0JTl8oIiwsjs-ORcPpZ7qn0w1V6OyvZiLwcP4_7EHtErK6JdVz73ArFmFqul0zQNX87f3-hKCsimkmX8LnN-TWGcnym5FYYrWAweHg-93wDAI0lX2XjAeJrTtGaCt_lLZQBJnt3v7U1onimYr1PH4dPUfCT4cenYxFgUMkgvRi6hfZ9vu6Bsyv0IgBuzNkyBOzcR0GHrn6pN2rC4dRw2iK0GqPC46xi4WBYq33bSCKFXqjq4-EniJCIG0N2vO-PzQ73nfMOa930Knd-DMENzpvhkG17a43uRQm9jZ5o3tH3GsdnuCcojnSKADvtXpkJYCPbMSUjIVQfdRgK9h6AjI3fQsoG_ILK6XdazEpctr_trSu7hTRZOJrGAAEzaTj1tTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f433103ae3.mp4?token=PlBb1SwnoB5cLMbBYrJfVb-AO9Cp31nIn_rDMvJLOjjsQDjpL9CSNobHAj6UMN4BB9HK740LTtkeZfWyTpLa94ilznixS89BinksQJNVuONitzp305z_X38wXgcSeKjXpbvRrBmEWKYz3oEdMPToZV_fGiF94CyX9b6kmolXIovpzHWxPC8dqHiTNsa70Ppg2H_XHHSMViw-2RIGCI-xZw_Owc5hmj0nSIiTrY4kxLODl9nvk0DTbv3_RwAOZKPNCg1G3PUqAJfWcskVrJhRCNqIVWrWIiSwSL8FZ7y5k0JTl8oIiwsjs-ORcPpZ7qn0w1V6OyvZiLwcP4_7EHtErK6JdVz73ArFmFqul0zQNX87f3-hKCsimkmX8LnN-TWGcnym5FYYrWAweHg-93wDAI0lX2XjAeJrTtGaCt_lLZQBJnt3v7U1onimYr1PH4dPUfCT4cenYxFgUMkgvRi6hfZ9vu6Bsyv0IgBuzNkyBOzcR0GHrn6pN2rC4dRw2iK0GqPC46xi4WBYq33bSCKFXqjq4-EniJCIG0N2vO-PzQ73nfMOa930Knd-DMENzpvhkG17a43uRQm9jZ5o3tH3GsdnuCcojnSKADvtXpkJYCPbMSUjIVQfdRgK9h6AjI3fQsoG_ILK6XdazEpctr_trSu7hTRZOJrGAAEzaTj1tTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توکلی زاده، معاون امور اجتماعی و فرهنگی شهرداری تهران:
«بشکند آن قلمی که ننویسد ۱۷۰ شب مردم ایران توی خیابان ایستادند» /
🔹
کجای دنیا مردم ۱۷۰ شب برای خون‌خواهی، دفاع از نیروهای مسلح و دعوت مسئولان به وحدت به خیابان می‌آیند؟</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/461436" target="_blank">📅 21:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461435">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFexTgm_vg3FmLK1z8iuSYAf17EaUNfC5dvL-4IARqWGk9-kg7RuEfoB1h7le6AK5sOp_yo0juEDzUqy8oegjyAR9YmM5efC3z80QxsgcAi_ONiGhRnq0l9f_vxNxIihA_6-ZN9SdNOIMYAU7nMpeDztv51aA4b7a4IDU1tHhYC4Zfnm3lQXUovoFmAAyWNpH6mf3aVE_jV0dju5a37DM09sYawoceuB5yFZ29NmrSD_hvHbkmGuPE3eQR96iN6nP370ReLcYE24FJGHXQHfSpzDJYUr82N8s3Mq44P6MWE40pPXxmpKoXs7n8YumFfRZqhEEn31RxA26a1vaVxb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش مدیریت
#تحول_گرا
در خلق ارزش پایدار؛ چگونه
#بيمه_البرز
هم‌زمان صدرنشین بازار و پشتیبان تولید ملی شد؟
شرکت بیمه البرز با اتخاذ رویکردی تحول‌گرا و ارائه بیمه زندگی و سرمایه‌گذاری پروژه‌محو‌ر، ضمن کسب
#جایگاه_نخست
صنعت بیمه با ثبت ۱۵.۵ همت حق‌بیمه تولیدی (رشد ۴۰۹ درصدی) و سهم ۲۴ درصدی بازار، طی سه ماه ۱.۵ همت از پس‌اندازهای خرد مردمی را به بخش‌های مولد صنعتی تزریق کرد.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5096</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/461435" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461434">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/461434" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461433">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_yj6OTHCp-agMMm714xRTXiMorY8fNVtXu770l9_GwTRe5vkg59_eN7WuynxZg9TEf0dQEYQPkBmLvDREemOMjUqsMMnGNvKzX0oSabJsBp_Y52Z3Sz9-Q73vtl5llJuM_I_LZwV0-hn0hBgI23qW9gC82PSBsPEFP-HJx5l0wya0J_q7wseb2vMpFMz6tIcbbZ5Ls-gd0kbovMBgfKvkRewaCMsiBPS1vzHDjGZpQXcSKMA7zDXg9xqzDLfrtVpTcgmnO7fpwOSI2aQZmqcsn3fef3LxOinWwhhBUlij9PB6MBUHGkG43ZFYY1CVlKProl0D9ykq-03JiJVSae3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: آمریکا دنبال ایجاد اختلاف در کشور است
🔹
آمریکا دنبال این است که بین جریان‌های داخل کشور اختلاف ایجاد کند و ما با حفظ انسجام نباید اجازه دهیم آن‌ها در این کار موفق شوند.
🔹
اسرائیلی‌ها منتظر فروپاشی خود در ۸۰ سالگی تأسیس رژیم صهیونی هستند و ان‌شاءالله زودتر از زمانی که رهبر شهید انقلاب فرمودند، رژیم از بین خواهد رفت.
🔹
ما با حفظ انسجام و وحدت داخلی باید با مسائلی مثل حجاب و سایر موضوعات فرهنگی مواجه شویم و اجازه ندهیم این مسائل انسجام داخلی را به هم بزند.
🔹
باید عرصه را برای حضور همه مردم با سلایق و رنگ‌های مختلف در بسیج فراهم کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/461433" target="_blank">📅 21:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461432">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de15aa0aa.mp4?token=RQni9SEWgjTRDPmzHFu21EI-HB75_9m6qguIidrWEKqS935xb5Ga5G5F9_pj28IqABYqBmSgLVR0-3YOR7_D5QWeJQL3Um7H3BsFsoq2DBpl5jhPe-1hmOJFjMFfU64iTjUVArK74XgFotI165uo6bQYyZgSADM-X1JKXTKWaLVCPsJRvmVH09ANYPL7QnpejDrGbPXse16M-Tzz7KPiN0onCdnyXzLuVJr86yGbBZZ83BEOmXqVi_1B6JaYksKFP7Ddi0Q_S5IGgA83Fdv7zmF4euGzMJvfgAKpuBeMZoaLcqLv6CaAxUGvXT7SL1w12FKtnxILqA6QwtpvtezUkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de15aa0aa.mp4?token=RQni9SEWgjTRDPmzHFu21EI-HB75_9m6qguIidrWEKqS935xb5Ga5G5F9_pj28IqABYqBmSgLVR0-3YOR7_D5QWeJQL3Um7H3BsFsoq2DBpl5jhPe-1hmOJFjMFfU64iTjUVArK74XgFotI165uo6bQYyZgSADM-X1JKXTKWaLVCPsJRvmVH09ANYPL7QnpejDrGbPXse16M-Tzz7KPiN0onCdnyXzLuVJr86yGbBZZ83BEOmXqVi_1B6JaYksKFP7Ddi0Q_S5IGgA83Fdv7zmF4euGzMJvfgAKpuBeMZoaLcqLv6CaAxUGvXT7SL1w12FKtnxILqA6QwtpvtezUkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
‌ بدون تعارف با خانوادهٔ شهیدی که طراح تونل‌های شهرهای موشکی بود
🔸
همسر شهید مصطفی عارف: تا قبل از شهادت همسرم نمی‌دانستم او کجا کار می‌کند. فقط یک‌بار به من گفت بعدها می‌فهمی که ما چکار می‌کنیم.
🔸
فرزند شهید: پدرم یک قهرمان بود. خیلی دوست دارم پدرم را یک‌بار…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/461432" target="_blank">📅 21:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461431">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c433d1a34.mp4?token=MU2H6hScRSHiP1Apxjvs_Pe1TXw44l5VVoYDTCbmrcMARUn4RqXAMYTzZ5lc3LoHARL4uvJMnG77KZnvNU91u9nGwYh0NfQ5gZaklakTjMgjVxDnGpX9zAeWfyybDTuVH6-vETQRBmdnosHoJgUvytCX-FFZMAXXV1T0RpbVahAffCgQOn8k7JfcVEDBHlKW5uqvy6K2ve3nZQNzqsFe2thHEiQHQxHddztNuUrOjg7EQt1t780T2Rv2a-YJRSdFk3marc5Q_8XdmFiJKgvftqeN1lS_OFFv66A7HQVdgxhZ5UhGAc0kKrYlkFWBgnVybOrTvM7tTQdunVlG4f4DMhzRgbkUtVh9SySqgZ_xjaTEtnM0mtEpFlQ3MT4ciDF6vj9C9mVFNqJNtzHyy59DnSUBEt6F2QHY32vSTKUu7ZLv4yU32g9Fe4bHukPP_i533XXWQXXP-XQl3eO4IWlBufyibVIcv3KWHk_Q2gzrOKusedkA3B9jhWPsSmOpSDS8eN5KdSgERhCP8z0t1OmM16zif5nWUgjGuatqLDPCiq_FMV-HzpCzr-NSpJrdLi2AmP2wpQBHdaSm8MF2CvmX5kgvg5VF8J1QQDcWLSV1FJ4DyR72ka3LcSi6gvTGJ_o-e7RfndPX-AdC6edHq5k73UCdjxjTXEvYrkhqtq64iQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c433d1a34.mp4?token=MU2H6hScRSHiP1Apxjvs_Pe1TXw44l5VVoYDTCbmrcMARUn4RqXAMYTzZ5lc3LoHARL4uvJMnG77KZnvNU91u9nGwYh0NfQ5gZaklakTjMgjVxDnGpX9zAeWfyybDTuVH6-vETQRBmdnosHoJgUvytCX-FFZMAXXV1T0RpbVahAffCgQOn8k7JfcVEDBHlKW5uqvy6K2ve3nZQNzqsFe2thHEiQHQxHddztNuUrOjg7EQt1t780T2Rv2a-YJRSdFk3marc5Q_8XdmFiJKgvftqeN1lS_OFFv66A7HQVdgxhZ5UhGAc0kKrYlkFWBgnVybOrTvM7tTQdunVlG4f4DMhzRgbkUtVh9SySqgZ_xjaTEtnM0mtEpFlQ3MT4ciDF6vj9C9mVFNqJNtzHyy59DnSUBEt6F2QHY32vSTKUu7ZLv4yU32g9Fe4bHukPP_i533XXWQXXP-XQl3eO4IWlBufyibVIcv3KWHk_Q2gzrOKusedkA3B9jhWPsSmOpSDS8eN5KdSgERhCP8z0t1OmM16zif5nWUgjGuatqLDPCiq_FMV-HzpCzr-NSpJrdLi2AmP2wpQBHdaSm8MF2CvmX5kgvg5VF8J1QQDcWLSV1FJ4DyR72ka3LcSi6gvTGJ_o-e7RfndPX-AdC6edHq5k73UCdjxjTXEvYrkhqtq64iQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
‌
بدون تعارف با خانوادهٔ شهیدی که طراح تونل‌های شهرهای موشکی بود
🔸
همسر شهید مصطفی عارف: تا قبل از شهادت همسرم نمی‌دانستم او کجا کار می‌کند. فقط یک‌بار به من گفت بعدها می‌فهمی که ما چکار می‌کنیم.
🔸
فرزند شهید: پدرم یک قهرمان بود. خیلی دوست دارم پدرم را یک‌بار دیگر ببینم.
@Farsna</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/461431" target="_blank">📅 21:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461430">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5365198c.mp4?token=dZO4gDvEEbmhxYCzo80baiW6oiPI8R3q4WaRqzkzaiXlR8FFYULXN37LaesCqW-93V8CHjUEKnw__aVa7D6mMNeJ-VzlBeSMGN2rlqRLa5fn9BxfRZkbdIcyXCWysHemKHwxJgfJDtpI1ijKSzKbm4eyWN0AdCSLbSVKc4o22AwbX28Z8ikFipRXm62wY4ztHCzZ1MUFm0MOApdIvcgaLKSOHjWeNHflzUYl7xcgn_NqNgedWO1pgdFNDQmM52wgtOMxkG-4RZ0dAyxK1DcpS1xVukqUaAyWtPuVwBi2oM24GCtwFU-COO1db7U0ndb9OXY-VixnRFCpDslZHuDA0QEBS0-wGX1vJcBpm15lMOGh8-kpp0cQ-2XutkBWLNWsDxqw4-r8AXazj4OGf3b-pDdHEcRRW97nG2kW3PSMrBNbKnn-aG0WAj2OSpywtvHEprPAR8gsitQhyRUmP41N3c2GhV_kJL1anapL22qYy3CFx3MyuS_wUuHZsU0ESmjFfvrXwIP6dfgbwHHouD63d-74W1skj9urDvqaj-s3xl6JRcelc74-NOCeHh5TCVFs_aSVjDoWK1fVX6HvAkND7GAZiq5_J32hdbVcwAj_WW7xx_0wpRuwMv7ZPky4rTCuEMRFC9kqxmxEOhrgLIdEw-S9FwUkXHYrfD8N94ETtDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5365198c.mp4?token=dZO4gDvEEbmhxYCzo80baiW6oiPI8R3q4WaRqzkzaiXlR8FFYULXN37LaesCqW-93V8CHjUEKnw__aVa7D6mMNeJ-VzlBeSMGN2rlqRLa5fn9BxfRZkbdIcyXCWysHemKHwxJgfJDtpI1ijKSzKbm4eyWN0AdCSLbSVKc4o22AwbX28Z8ikFipRXm62wY4ztHCzZ1MUFm0MOApdIvcgaLKSOHjWeNHflzUYl7xcgn_NqNgedWO1pgdFNDQmM52wgtOMxkG-4RZ0dAyxK1DcpS1xVukqUaAyWtPuVwBi2oM24GCtwFU-COO1db7U0ndb9OXY-VixnRFCpDslZHuDA0QEBS0-wGX1vJcBpm15lMOGh8-kpp0cQ-2XutkBWLNWsDxqw4-r8AXazj4OGf3b-pDdHEcRRW97nG2kW3PSMrBNbKnn-aG0WAj2OSpywtvHEprPAR8gsitQhyRUmP41N3c2GhV_kJL1anapL22qYy3CFx3MyuS_wUuHZsU0ESmjFfvrXwIP6dfgbwHHouD63d-74W1skj9urDvqaj-s3xl6JRcelc74-NOCeHh5TCVFs_aSVjDoWK1fVX6HvAkND7GAZiq5_J32hdbVcwAj_WW7xx_0wpRuwMv7ZPky4rTCuEMRFC9kqxmxEOhrgLIdEw-S9FwUkXHYrfD8N94ETtDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم همچنان پای کار دفاع از کشورشان هستند
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/461430" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461429">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حملۀ تارتار به سازمان لیگ: دستی از غیب تصمیم به لغو گرفت
⚽️
سرمربی پرسپولیس پس از لغو بازی با خیبر: از این تصمیم غافلگیر و شوکه شدیم، چون مدیریت باشگاه و بنده هیچ درخواستی مبنی‌بر لغو مسابقه ارائه نداده بودیم و این تصمیم به صورت یک‌جانبه و بدون هماهنگی گرفته…</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/461429" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461428">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be3aa62e63.mp4?token=rhlhABLL2J9u8OEvItj_lgXd8VIVAaNyEdqqM2_cedUuJeNtMeYhTLhMB7zs9gHgmv0cxwQErorg_yJ9DhAdA-hx0LzRWMpkska4F1NStIBASRLj1nIYpDA4tw9HR8Dy6ITR_U5mn64nEpDOi1xkMj-W-E29W_kXUJPq3yeCqygWxJ4-MOmf9n2ijIEHtjTaBEGZoLgUQX7p8sTbSzoUsGQI_MtCdN_jV0rgqZ5mqOEsGK7AZqypSSH_BqKfwiVndn6zayPN_SOABd7wOG9v9uKQlBokZbfBCgKB_hyxfMA2T3ZXE9DdbAHI5QGhPe9zd4AAIAvP8zV2HQxi3L5yAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be3aa62e63.mp4?token=rhlhABLL2J9u8OEvItj_lgXd8VIVAaNyEdqqM2_cedUuJeNtMeYhTLhMB7zs9gHgmv0cxwQErorg_yJ9DhAdA-hx0LzRWMpkska4F1NStIBASRLj1nIYpDA4tw9HR8Dy6ITR_U5mn64nEpDOi1xkMj-W-E29W_kXUJPq3yeCqygWxJ4-MOmf9n2ijIEHtjTaBEGZoLgUQX7p8sTbSzoUsGQI_MtCdN_jV0rgqZ5mqOEsGK7AZqypSSH_BqKfwiVndn6zayPN_SOABd7wOG9v9uKQlBokZbfBCgKB_hyxfMA2T3ZXE9DdbAHI5QGhPe9zd4AAIAvP8zV2HQxi3L5yAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا چون نمی‌تواند با قُلدری مردم ایران را وادار به تسلیم کند می‌خواهد کاری کند که مردم به‌خاطر نبود معیشت و امکانات تسلیم شوند اما مردم ایران تسلیم نخواهند شد
🔹
اگر این‌ها مرد جنگ هستند با نظامیان بجنگند؛ با نان و معیشت و زیرساخت مردم چکار دارند؟ اگر این‌ها انسان‌اند چرا راه آب و غذای مردم را می‌بندند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/461428" target="_blank">📅 20:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461427">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb125a3a80.mp4?token=k3NKuA54256Tk0ZTLbLiP_6WASwT_tflVgtNEM4OsAs4-mfScXcAn2G7UCKGDZWFoq8b2nZAP2jMY43BslJy3P3uim07-bHQLJGO_gmsupDCoxJfOycbwAqjciSJJN-qR_nZccAUonkGQiVRsrnbYDw2iBOoHtQmj66OU4u4igWaS2ZvKdM2rONPDsJNjJM9HRPwle09Xi106KNpgU2q8MNiDm3dlleX5BeG9BnXry3scO2w3nU86hN9h8L77IXoGZ-mBe5REqErDPBjNVvvNGA0pu_NMYoQsdOfy_UACMe_osivucHNdBJmy9mh4iQ0EnsGzN8AjNf1eXMmVKZmqpXtjB7dxcZIz_PZn808OIxdrgtm7EFRqpx2Ny_987Ypb4u49qoYJRc1bmnSAY7YenN_hoJrzcdOKwv1kAIpfg2t7WAE8jDOHp3JIu2hm2a8RS52u8vTHye4bLk4cnTrhD3tMxtGcXRyetIoj4yWLaA2cJ_Nj-41VS1M1o2Ce0KLeM8vfRWG3tsQ3cQ0y6dSgKTOYFi_AID_XmyluvUDJ6KVqaBS-2c3McWFYLVjTZBbzZKLQnu7rij9kvg7gE-MjrZOM1wQLaygJ-XLyfHQxyP4cS7zs265V44RNoXr7ZoUO0Cd2FgMRDm72QkOKyq3I004nJoTiosEWFsU82N12Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb125a3a80.mp4?token=k3NKuA54256Tk0ZTLbLiP_6WASwT_tflVgtNEM4OsAs4-mfScXcAn2G7UCKGDZWFoq8b2nZAP2jMY43BslJy3P3uim07-bHQLJGO_gmsupDCoxJfOycbwAqjciSJJN-qR_nZccAUonkGQiVRsrnbYDw2iBOoHtQmj66OU4u4igWaS2ZvKdM2rONPDsJNjJM9HRPwle09Xi106KNpgU2q8MNiDm3dlleX5BeG9BnXry3scO2w3nU86hN9h8L77IXoGZ-mBe5REqErDPBjNVvvNGA0pu_NMYoQsdOfy_UACMe_osivucHNdBJmy9mh4iQ0EnsGzN8AjNf1eXMmVKZmqpXtjB7dxcZIz_PZn808OIxdrgtm7EFRqpx2Ny_987Ypb4u49qoYJRc1bmnSAY7YenN_hoJrzcdOKwv1kAIpfg2t7WAE8jDOHp3JIu2hm2a8RS52u8vTHye4bLk4cnTrhD3tMxtGcXRyetIoj4yWLaA2cJ_Nj-41VS1M1o2Ce0KLeM8vfRWG3tsQ3cQ0y6dSgKTOYFi_AID_XmyluvUDJ6KVqaBS-2c3McWFYLVjTZBbzZKLQnu7rij9kvg7gE-MjrZOM1wQLaygJ-XLyfHQxyP4cS7zs265V44RNoXr7ZoUO0Cd2FgMRDm72QkOKyq3I004nJoTiosEWFsU82N12Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی و بازیکن خارجی که به استقلال نیامدند اما پول را می‌گیرند
تاجرنیا: با کاریله و استراندبرگ تفاهم می‌کنیم
سرپرست مدیرعاملی استقلال:
🎙
کاریله از ما شکایت کرده. درخواست مالی او از ما زیاد نیست. می‌خواهیم با نصف مبلغی که می‌خواهد توافق کنیم. با استراندبرگ، بازیکن سوئدی-موزامبیکی تفاهم کردیم. با مبلغ ناچیزی آن را جمع می‌کنیم.
@Sportfars</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/461427" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461426">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صدای شنیده‌شده در قشم مربوط‌ ‎به آزمایش پدافند هوایی بود
🔹
درپی شنیده‌شدن برخی صداها در محدوده شهرستان قشم در حوالی ساعت ۱۸، مسئولان اعلام کردند که این موضوع صرفاً مربوط به آزمایش و ارزیابی پدافند بوده است.
🔹
پیگیری‌ها از منابع رسمی در استانداری هرمزگان نیز نشان می‌دهد که هیچ‌گونه انفجار یا حادثه‌ای در این شهرستان رخ نداده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/461426" target="_blank">📅 20:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461425">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab4f3eb43.mp4?token=vZPKeygcHvXSeoBtQztF2IHBXN9-4w5XjrKQsp_DLdcgczmjOV4jD4M9Otpbcowillyu2A6LBKQ347hOxC-F37-bQdNrq0zo21XlCWxGtcjmYRsvK-rels5dCautanqnW5ziKFyzuGGd-oitm5taNah3syO7Kw3FqdSXJfTYhSMPLx7FPUuI4bqVYsZ5eGumE6rLKsTreh1UgHYTYEV1jqVPXwTo5AxBohLT7sF_8QHW5AzZ8hlbcEji7bc5uB4jPca1G5dwM2lBCdI9tUshOZeT2TUrvEIFXilUwlZ0rI0pOrFfbZbPu9FQ46oxairEOD4HGEQaTFcT7nIiXMfBJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab4f3eb43.mp4?token=vZPKeygcHvXSeoBtQztF2IHBXN9-4w5XjrKQsp_DLdcgczmjOV4jD4M9Otpbcowillyu2A6LBKQ347hOxC-F37-bQdNrq0zo21XlCWxGtcjmYRsvK-rels5dCautanqnW5ziKFyzuGGd-oitm5taNah3syO7Kw3FqdSXJfTYhSMPLx7FPUuI4bqVYsZ5eGumE6rLKsTreh1UgHYTYEV1jqVPXwTo5AxBohLT7sF_8QHW5AzZ8hlbcEji7bc5uB4jPca1G5dwM2lBCdI9tUshOZeT2TUrvEIFXilUwlZ0rI0pOrFfbZbPu9FQ46oxairEOD4HGEQaTFcT7nIiXMfBJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسخهٔ جدید اینترنشنال برای ایران: بمب اتمی!
🔹
ایران‌اینترنشنال که پیش‌تر برای حملهٔ نظامی به ایران، دست به دامن آمریکا و اسرائیل شده بود، حالا که از بی‌نتیجه بودن این حملات مطمئن شده، نسخهٔ «بمب اتمی» را می‌پیچید.
🔹
مجری و کارشناسان شبکه دربارهٔ این سناریو حرف می‌زنند که چه سلاحی می‌تواند تأسیسات زیرزمینی ایران را هدف قرار دهد و آیا استفاده از «سلاح تاکتیکی اتمی» می‌تواند راه‌حل باشد؟
🔹
اما شاید مهم‌تر از خود این بحث، ادبیاتی باشد که برای بیان آن انتخاب شده است.
🔹
در این برنامه، حمله‌ای که در صورت وقوع می‌تواند پیامدهایی فاجعه‌بار برای مردم و محیط‌زیست داشته باشد، با مفاهیمی مانند «بازدارندگی» و «اقدام پیشگیرانه برای حفظ صلح جهانی» توجیه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461425" target="_blank">📅 19:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDNXDJrRBl2o5S_zUUOOAGlslORwDh9MK3B_oPA6eLtH-YlVruj3V6bf7tXv0hgoAuoaKjx2Qi3lsNGq_PwlQSfCvM-Mmdp3GHJqy0wHGOun2bnAbfjQDwhXvOuhwQaT152N_Iq3dQKXvdnWm_69OoYzhAF9GpymbKJHsV4sveQpsnJd11csFIhfPTjqzhK14-fUr73V0bNrP04iHGgOrgEXZPuWwMItF2hXzhG4C8--I88l7WnXCIkWuyhnTdDjzFRIn25eoJ17G-en6h1GKwB7mecZj3vjlAcmiyOSAZLv-2Bg15SS5eu00aXPoQJ7jAha4eU6yGLA_Q-BnMzU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNzVIr41jLrXXDJAB1WG9pICCc9WKz1rkY3i69IwLgAjaL6qTCRFHf6k5pPPNE5LWJtKxE-JzewkkEoPRwBEqbLrr6Vqreqjr_1mWzH-uqOg2pwQQW2S6iFRq5Ua68DHgfmZmKvoTve_GyIq0XnsyRbuZVZBmcQYeRyjVJtt4IMHS_BNbSHHGbnLMUFpi_Bd4BkvPVlrjpdz_zmjzg4bYCAW_Cf_EdzGgNcdNxGoBoJ9Nf8VQm20l6JZ4judRl8_7z7Jfve8Q4qGDSNysRtmJ1TOSdioRYLRgm-036X3pMko8jSHCYLW7xVRv9vRfVoeACLndWLuXU5YEEO_KmddvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdkfPNrMgnTA9l5Ay4sUc8ROHl8heh6ooFQGzhzasevLTDQLTdukyJD_JsOvTeTi9MVmQO1ja7iqQX0GMuGOOLE_Y-dO_CDiqKQK69rdSOwJIU8lXaOgnvxgS0EyEwBkSrSqaMlp7KPppcfmJgRzXJI_54CVEo18FV2Ppq1WdMk3mJkmd-Rqfmw1G68PlXp-07W522G_l_Yylwxvvlh8iLcTRU4LIU6kUMJ1zC12VSph1_btAFGtZ3_i2N6rGSzlXANz3XLLQr0l6BmcFmQd6Zq3wvYjnkVU1m6-gENtLyKlgFCRHw9lRW8XOT6hFy9OlUJp5a6A_B0fVLyhPs7VEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGgN02qd3zoVd9lzBe6r32vqhrw3pK1YNK7nZ5dAzylFNZQo2scqZm4QTGGA7fqbJE3S-UXNMC7sBq_8HG4YSJqEduZqXV3vzNyKs86FDQVNS49iglGHaIVrPazaf0NL9U-zvAfieMkdCj0i5mFS0I2t72a2uLbQ_9yQBRx16oi_V3w4fdPTnuzTXWs4C4Impdud2BdZHW7Z-6eCvTVsCnmgnJi9uAsUDW0D7dTJAxJBy4nsrwwP4GRPdKPjQw8yE2NeVmForo13665XGEQJ_Z6RGSP9vCRMgkG_L3HoNEbQy2z6V6OeRxJRNnuq_J9M9QNrjUWoeDGxw7xZsmXrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIPo-h4LIxvkzspa3eSFg5cO1S7_fUEfSuUKuEUz327p8OSMYN4_biBenyu_9iKNiCj4h2kiUic4ZDdZJPwjJQQw51lV51kIwO6CcS-Lwl6yMXTKsUBX1NUndzuxOMwXweNcrqXDHCg_99RnmfSkclO_y9GaCPQTlDZqQCUYUWwo1UkXfen_AabIqof5-vU6rvyE_yT2NgSEQt3iYnc3SYw9pDx6Dkl8Z_qpHiO27P4bxBnBZ2O1odFuXk1_VO0rU10bMY1M9SHjy9MP1qveSTkD_l_CLx723tUazb1ZXdt5JZR5Tcfd7k-MoI9PPLtIvHSxvVQ2VWqEWEXeFSBTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EesaChFlZvhFnV7nS_R-iwqBl3T0II3RAUyPKWPgreTq8F9_Zmh7Urm2oOrv-mJMz5EoAY4LYkSk-vFZPlwfGI1196HnbiMue7XAGVOzsymM1cpvL7XSIaMy4yNmBbOognDa-DnnjMDtm_sNHqqRq0d8nw8fcz07M4k-lOJT2cFDkeSMc6ac5M1F2OvuM_8Ty0b9xh5DaQ-kZfUNaC1TqVxBUOZoBeMccwFd4LYNPxLIFxi_3t22naSM7z7ztSAlAjDXFinY1B5NkB3xShiY8mx3yu6eUiGGByiE3hwYf1rL0B93E9pAs83SdiAtEzIwhnJGxJN4X5sFCr_yMCYEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEE21Xy4C4E-k_jmt0MDP909s0ZdgnTWusHPIKQ5-dyhC5rsoKEBGkvtuhA0dh8hDKpX-HTopSeX0WbXzsPEw833jFujZs8K6jHZxmCzMin_bPjVieKuEZhjS87MMIFHb945ifIs0KEyKiHADx0E0VOQU1sabwjqvsNlNC7oe0Kh2s8Npcl2DvASNj5GT3_0Fmi032AT0-DO99xgJpnOyPQSsVEqSWEv0mkVWjOBrDy2s9jsBR21p4PDoxiE2RDnSWvU8zoUnyvRJradFLj9jZiaGnMXnwgGgTF_gh9TCCu35VXSZkRrWBYurOGa8EVNlxIXDjiEjZmxbU7GkeU-Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک بنای تاریخی با استشهاد محلی تخریب شد!
🔹
تصاویر تخریب «پادگان روس‌ها» در سبزوار شب گذشته در فضای مجازی چرخید و واکنش فعالان میراث فرهنگی را به دنبال داشت.
🔹
مدیرکل ثبت آثار وزارت میراث‌فرهنگی در گفت‌وگو با فارس می‌گوید: مالک با جمع‌آوری استشهاد محلی و طرح…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461418" target="_blank">📅 19:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22277b2e4e.mp4?token=vgTpQxfd1QF-L78DvjO7gd5u5hO7XImGitJAP233_QO_TYfwUwKozsWotdmwDp9tEFMqZcMcTyT0LDdeG-rgo0pwbz6prn62UpZwaIRegAg7hh9Jilf6Chu2XDO0B-2cFlIUgymmSvRS-eOSzdUcsUEEj2JODMsDZcJfvAZIzA-tlqNKtd2EtmF28Ls-D30ZVdn8cgJc_JCRAF28Xrh5N07MuaVJlioNbzZVKxJqASaVB2aWseKo3elrVDhtK6Jn7rRK5QVso1tAZf2EoVq7MmuQr1fUwSN0HrT0LD8sToKQU7fZeT_W3c6TTQj0GBCIoSWFYlpWFrf7LLC7WnhkBGWkMOVvrZN3QHvTmODmEVbpgbd3NGRNrxXLsUx8Ee2Xzb4rK7LifcDgVvR0RPL8-FP20MCumGpu_h96r0I3Y75LfjUvQVswHfXbpErkYvUfmngYW7XSMeTXEoCj9A3JgBcnS3Px1TLX5yk_pqcWVdPI7SlFbucs4pj3eAImOWXzfqmp4sj9bxCHiVXXaV5q8GOOjWfcwsu2ScfmLmHlRvVk3A6ASfnGxjyfTCglD_QZ2otaZsn-4IwX6JFWVjNadcmqlvet1I0t8HtjaVzUyYKPp_1_KxjwfT0y8ITTA_02RI9xUN047RpIg3j26PfdAE_EfEJ2w5NnVtXIVBvIzgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22277b2e4e.mp4?token=vgTpQxfd1QF-L78DvjO7gd5u5hO7XImGitJAP233_QO_TYfwUwKozsWotdmwDp9tEFMqZcMcTyT0LDdeG-rgo0pwbz6prn62UpZwaIRegAg7hh9Jilf6Chu2XDO0B-2cFlIUgymmSvRS-eOSzdUcsUEEj2JODMsDZcJfvAZIzA-tlqNKtd2EtmF28Ls-D30ZVdn8cgJc_JCRAF28Xrh5N07MuaVJlioNbzZVKxJqASaVB2aWseKo3elrVDhtK6Jn7rRK5QVso1tAZf2EoVq7MmuQr1fUwSN0HrT0LD8sToKQU7fZeT_W3c6TTQj0GBCIoSWFYlpWFrf7LLC7WnhkBGWkMOVvrZN3QHvTmODmEVbpgbd3NGRNrxXLsUx8Ee2Xzb4rK7LifcDgVvR0RPL8-FP20MCumGpu_h96r0I3Y75LfjUvQVswHfXbpErkYvUfmngYW7XSMeTXEoCj9A3JgBcnS3Px1TLX5yk_pqcWVdPI7SlFbucs4pj3eAImOWXzfqmp4sj9bxCHiVXXaV5q8GOOjWfcwsu2ScfmLmHlRvVk3A6ASfnGxjyfTCglD_QZ2otaZsn-4IwX6JFWVjNadcmqlvet1I0t8HtjaVzUyYKPp_1_KxjwfT0y8ITTA_02RI9xUN047RpIg3j26PfdAE_EfEJ2w5NnVtXIVBvIzgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئله من و ساپینتو ربطی به رفتنم به رختکن نداشت
فکر می‌کرد نمی‌توانم اخراجش کنم، همانجا عوضش کردم
سرپرست مدیرعاملی استقلال:
🎙
ساپینتو احساس می‌کرد خیلی جای پایش محکم است و آن نقطه‌ای است که می‌تواند مدیریت باشگاه را به چالش بکشد. من خیلی در قبالش صبور بودم. فکر می‌کرد نمی‌توانم عوضش کنم و من در همان نقطه اخراجش کردم.
@Sportfars</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/461417" target="_blank">📅 19:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۱.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/461416" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۰.pdf</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/461416" target="_blank">📅 19:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سخنگوی سپاه: ناو هواپیمابر آمریکا را در فاصله ۵۰۰ کیلومتری هدف قرار دادیم
🔹
سردار محبی: ما امروز مصادیق قدرت را یکی پس از دیگری به نمایش می‌گذاریم. نمونه بارز آن، جلوگیری از عبور و مرور هرگونه شناور بدون هماهنگی و نیز ممانعت از ورود جنگ‌افزارهای دشمن است.…</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/461415" target="_blank">📅 19:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8LwFmuilhaWTjJwn1DnBUyXJuoQX4_hrmSTCjA0ZL1J_j_Gv-_gd1KT5Ah5UaCW0n5yYzI6QKyjQdBEv5niGSe99kUetjWFMzDFzdTIbCN0n_GOYCEpUMx_khvK4r2SRpuoJH78FdQQ1KBwWSyFTOa9YIsJ8mKISZBlp5fgHPRgJnl7ccV25zP2TyfP5mlTeYNPgZDNMrX4Uv-dg9kt2w6LIB0Tc-VTvK9hkdMO77IL6gMoFcS1snNiRSbDgqAL90j4o8HQk2NSZN5dz2HwaeVsXOqoNLa27avGRkpl-Y4EiXSxh999lpdA8VmG5WohyXA0eHA3cdkTluxFxVXLPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYITbwoIbEidRU9-T6mbGbwgcvDmPsv0nGZerNr_-DZbj8T-phHjtW9iHkTbnrJcGxJdLbfvlI6QUX8pKfvk9wfqqvD8dOcZ51Oe5fQAWwIRUPjofhbzMPzF8boCMCIQ7PBnpnGcnZNXBqUrAlvO29ZNyr5siYM79qxAJ-aka51F-RSlqveo0TDwZ0noQzYSNGLFlBd_otPusrSAedoVOOGy_dVhaLTn7O6a-sjVQh5go7aIvEZ6nR-ggq_MkLDdZ4lD4jAPHhIYJa3jkYjgxwMEk5L2Y_TFDqNpZVM6UJFUm5PzDHCFayOfHetSqycFz7T1fQ-MgjLh-bXAL5ncqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b69dPvgWr5-l7z0815JR2D-pa7uDNR8emh7gOZAKw0nMlycY3eOOfNxs04Ttil3SE61W9Jai2kL1_7F0DQ9BNy1IPzDDzIZ1lBhjt3Q_y5KFkXKw9c_2qKzWXzDSm4L4hFXU8YgpjFcwuSpdLIatYCDzhbCyozLrIW9XYWP7o852TKlEEjc5mgH7hOUxZqM1q9yVU8YcCgWl17x3ikJW5EazcWbSM64TQd_DVT5zhDFFnYENAO46SFpJSRLeKSlqtYtlVlWUpLKTbiC0waKtO8LRv2_kXp8yNka4bqvW-DJUaVRPAGmLfyC-X5uPooMbqQn0GbK3o1D-CQKhA_gDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oosNJ8yUwV3sFCcfvhPBxaKYhwnSNE_L3rnIivq3VRWSXcUetEpwiKN2RApoKNX7jZdCjFIEAphvXRFAxmMaNnFok6eE_ZsNbSE-zI6k7iQKCBHVRFt1StIFolj3AVeMjogrpZrqei4za-mAEKR3LRwalgSZbwjbwRLcCMYfFB_w9iPsBsJ_eI6xyKKaBTeqfFBpM5pPkhLidGpOh8_SzWVTVq4wESu1A3a811jpB1ezH8HbGNaWzhdo6St4-MWEC-LmNF9yvbmYLDd9vrKqVIVt3EEecw5i6OwQSdUGFesfLrbGXWOcjYEeJOzmkxXiw4g7v8qY3njKcf827U67gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-NqSFxjTgYdExJH6Aa4OIt31avnR-ZWu-_QhTLFHcEEttBy841FB2GfXF2PGm_CYO2qdA7mB2oBi7HuXHnFfy36CyNcl8Vudmz39fdOehn25AeNNPz795v0HNBFvQA24PARP7exwqUTyqPI0m-1R7LF8JTtdz5UW4HRSUbo5ZkVOd73ypIQ1NbygEZbF7YPs66RhBeeiEohqxPYKrH1kSWVh0rV73z1OpdKsIAPinGKtvYT8GOtDSlo5MKuimzcY4ixWL3EdMejptAVxeQcKL5MkKO91HDMQjt-iwGx7qyfCcaUHNKxzsT-t_zhV_VTpM-UasFcvwK0ML74kB4Zfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: یکی از پیشنهادات ایران برای بریکس راه‌اندازی صندوق بیمۀ ۱۰ میلیارد دلاری برای پروژه‌های بزرگ زیرساختی و انرژی است  @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/461410" target="_blank">📅 18:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c3b00cd2d.mp4?token=KbpuXo805a4sOGQRtCxwTD8YZ1CYe2x7Ir-S1aJ8_vnJV448MVI00v7ubODWhSFlLzjc5lFE7s2vIzYHccFWqIMGaGPdV7SQIy9zJ4TyyCYmI6xtbkX07qSFyi6Q36vu4mc0w3nLjuAg8XCsEBr4XePfomjoAGftXhP9BW5m7py33tX8R2QIsTHPYLYZ_9rqI92MzNDowD3s6m7RLZtakRrY_pzVgr5Ht8Ewc0GmOcJn4KXsCcXqoClRoOahUfqrEApNwhr7YKiiy_3H3hUv2vhmkbYeAP-RR6d1t2ejTrUKcjn9hZTBxkcZSzDMiTM8C-7IMHOb914Hj1qSZDRYKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c3b00cd2d.mp4?token=KbpuXo805a4sOGQRtCxwTD8YZ1CYe2x7Ir-S1aJ8_vnJV448MVI00v7ubODWhSFlLzjc5lFE7s2vIzYHccFWqIMGaGPdV7SQIy9zJ4TyyCYmI6xtbkX07qSFyi6Q36vu4mc0w3nLjuAg8XCsEBr4XePfomjoAGftXhP9BW5m7py33tX8R2QIsTHPYLYZ_9rqI92MzNDowD3s6m7RLZtakRrY_pzVgr5Ht8Ewc0GmOcJn4KXsCcXqoClRoOahUfqrEApNwhr7YKiiy_3H3hUv2vhmkbYeAP-RR6d1t2ejTrUKcjn9hZTBxkcZSzDMiTM8C-7IMHOb914Hj1qSZDRYKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نکات معنوی از زبان رهبر انقلاب
🔹
اگر کسی استغفار بکند، مغفرت الهی برایش می‌آید و رحمت الهی شاملش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/461409" target="_blank">📅 18:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94303b4379.mov?token=UobmQ0bFQ-wlO8BuPraVYBtsHiZhIaQoVFsUeY_-qYFM2SjUJ1WMiPVnkf91qU7gxN8RCKG-3NYxNbY44g5IcK06W8Mp9HUwHEzJxylMi79gaRb_NSz0U6kWgSiK-gcHFG2FLkc2BdcMlgXGRn84V8JYNntyH-KyVs3jF614ciX0XJYcg9124D1GzzdmM_qlc843-MbURXp6mEeKLsIYfh0DvzFh4xIef12d93YGf8u_SV1EHKFyHhhMnafKeg1Kr-KszDHVvfQLaJz2mIyR_boqATnl7nXjj3c2BPjTeP2HMZmhjcXqtVLHMDI1p-4WkZ3B8gZ8VhVbvmBLdsBNSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94303b4379.mov?token=UobmQ0bFQ-wlO8BuPraVYBtsHiZhIaQoVFsUeY_-qYFM2SjUJ1WMiPVnkf91qU7gxN8RCKG-3NYxNbY44g5IcK06W8Mp9HUwHEzJxylMi79gaRb_NSz0U6kWgSiK-gcHFG2FLkc2BdcMlgXGRn84V8JYNntyH-KyVs3jF614ciX0XJYcg9124D1GzzdmM_qlc843-MbURXp6mEeKLsIYfh0DvzFh4xIef12d93YGf8u_SV1EHKFyHhhMnafKeg1Kr-KszDHVvfQLaJz2mIyR_boqATnl7nXjj3c2BPjTeP2HMZmhjcXqtVLHMDI1p-4WkZ3B8gZ8VhVbvmBLdsBNSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان با نخست‌وزیر هند دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/461408" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تبلیغ دارو ممنوع است
🔹
رئیس سازمان غذاودارو: شرکت‌های دارویی باید محصولات خود را صرفاً در چارچوب ضوابط علمی و برای جامعه پزشکی معرفی کنند.
🔹
معرفی علمی دارو در همایش‌ها و کنفرانس‌ها مجاز است، اما تبلیغ مستقیم دارو برای مصرف‌کننده نهایی ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/461407" target="_blank">📅 18:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7QV-EI_JXhEeHMNE62UDrfy9d56v1RD_rSMuHobyjwZjL05tghh9tf3kkxk_G2sFM-MqeSvzoXB7rFTkhCazyhG9LPAOEp6Ba91Iw-GZtrrkrMnGiEMnIQvSVuvYfjrCcDBEe1foUOfgc0RsTa6q2Q9XoqEqxOhK_4l43DrG5fx09TzZWzu2fSg1o9lyfvwmSt4vN1_p9q97k5JZ5rUIW_PIfW3o7bCwmIO6p1LUzMLgCqOS9_NPsKKRDzg1SFAFX6acVGY6U6JO00UNv-TeIOJgQk9rtI0qPn6NZ7glgkmoxz-RcpDgVNLYm8fShIYCBGw9QyQVm3USpgU4djqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژۀ هوش‌مصنوعی امارات از ترس ایران زیرزمینی می‌شود
🔹
پس پاسخ ایران به تجاوزات آمریکا و هدف قرار دادن زیرساخت‌های فناوری مرتبط با آمریکا در منطقه، امارات در حال بازنگری در معماری یکی از بزرگ‌ترین پروژه‌های هوش مصنوعی خود است.
🔹
پروژه‌ای ۵ گیگاواتی که قرار بود در قالب یک مجتمع ۲۶ کیلومترمربعی در ابوظبی ساخته شود به شبکه‌ای پراکنده از دیتاسنترهای کوچک‌تر در نقاط مختلف امارات تغییر خواهد کرد.
🔹
طرح اولیه امارات، که نخستین فاز آن با نام «استارگیت امارات» با سرمایه‌گذاری ۳۰ میلیارد دلاری و ظرفیت یک گیگاوات کلید خورده بود، قرار بود تمام نهادهای دولتی و تجاری این کشور را به پیشرفته‌ترین مدل‌های هوش مصنوعی جهان متصل کند.
🔹
بر اساس طراحی جدید، بخشی از تأسیسات ممکن است در زیر زمین ساخته شوند.
🔹
ایران در پاسخ به تجاوزات آمریکا برخی منافع آمریکا شامل زیرساخت‌های دیتاسنتری در امارات و بحرین را هدف قرار داد. در یکی از موارد، واحد ابری شرکت آمازون نیز اعلام کرد پس از برخورد با یک مرکز داده در امارات، برق آن مرکز قطع و آتش‌سوزی ایجاد شده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/461406" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461399">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtzq0eIrx8FgEfdav035ZbqddUVo7FSzx2oj-tvqH1ByZ5gdtoWL8hS9CXRcUm30M7DOi0kkhkJplHEF2sCmqstONf8nYHe9rqGTzYERr6BGzbr5dKXmTa4eDuInk6NZq3hgAItvnnyhu8JwwcLHuAzrSsrxCM7s2FnQlTrE63oe7K2klvRYUCImHGWUJ8Bn_-yKEni-KC8M5e0-NYO8TG0nsTCjC4EqIbjqiVefnO1ZS8Q-W1q1QE5nGC0xXWF6AsF1Z_yKC-X9eImDu9tbriAOXV3wWtixysONLJ1Z3oOuD1ZWH27nD4geNWm-RIbMxL-QnOU7sdudSSuTsiyEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d35eXFiFjKGHyDz2Z3Kpl7H9AQX24ESR9edjwciv0LB3KzZdNPdyp5_eq5IbKqO_41suQXJtSB2CxXDuzFGgthNnTtc1Vnbf8vYraf_Buw5-_VZNgpg8DQcPSRfNVLFVo-LrqRjY_C8PZT5moE8hEM21qaD3V4A8qt4sahHCQsAA1M2k6WUxnOjYk6f8uYK-yHbe3myZt983CWH7wZ0UQe3R5NKAPWuGheMu0Vpr-5G5c6FTt5t0TS-N24idh4_k50JLzU-xQlbTqjjiJCOLAA79pb-hssyMDZPVWmp7MH5peR2Dn_--ofRSNG4sZ7rCmaa1PCw0fGyDIV7DTu1D8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOl7xP83Mbs-qEUNMS0QobkYsBSYrRrovHMDMOPAznTbIjqQa-KYqpbgPwFr_7uscm1zZ0Kzijh7Yul8ENlADMunWJC7tF1Cyaqxn-41xGCy4wk_aI3Yt1Bee6mqEVFws7_Ato1YfqTZ_sK41mtkMpPgXlj0aV8fLvi57K0vy4_dTE1m9LSwd09Dns3bKImYNqSjN0PvPiVG7dF3DNz5p9-6jKWXH0dIbGT2usCrafQgNA0qvvjEFKA6M9ToH918MhzJmM4oRFUti19BWC_DiNvXjnvLuTKvRMMAGZXdMF9ph8xfvaiHQVlLRRJi-uDIw9LRYtYi3NkYL3RNjxX0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Np35zkr_JXW_eekLcQy2qEE4fre65DGrbedARB_cQT7X-Vm7GVue9T9eG8ROTSi0-siqu2J-BxQoNDicwpEP7X9Or3wduKEGYFCUiPmbkmD65u0ALgE8eVKEBfSLm50fFoOZveND4NUZjLbygvok33FMQZP0eJH9gbOsWAAOdYJ9h-28DRWzyGCgQHkivkKByutsgfaxBgjKLd7_g8JWZ94qjcvvE1VvmnszTnxTRDGLl63TDf9WtXbhAVVN2othy3z0-J0OW5Skh5n7Wp8jXdd6hUp2ydDZC3XCOUMzTQWL8FGRlqOdOt0ytwt4sG4S6NpWkTmpqGeq31wiJZUrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hsvah4H0xJCkzHgsKHu0MMwKTLtdefZYxp3MdyZsrjMuufaUOIMZVUgm6snqc_WJIWTAutgnNHqwBsExbHJxY1SVNuWKXhKaTsLE4wLaKYz8F0Ob1uxY2XWHZbS_iSKu4Ccopq0ogYNUMothC5yWTgAZJfmDMsOm5-5mdMOdQXmsy0STXqKjRTonj_KrEF-gDGd_ptN-Ne4Zg46l3W5GqSoUYiIfYywEL182n2i4TGRW02e-A1-CHpF8c6FJvxsqthVzSSTQLhoBpU7zEcMXkIR1JVX9rZyTCo3R2E-A6BRXrrp9e2NdYkYq1Y3bXz2xCfO6ogeDB2daiQVf3C684Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKjCSio4yGZe20mEEu0YyKSt4R_UL_Qb-87YmpBmunZTY56d7vzI37FoAQ0DmW2ZD54-HRvlzplnLdOA_lUhy5_xQ0ZBc38xcAspOZMzdQFG4gsQg0cB6ICsSjamT_SbJpRhbRxMect30wAXXx4GZxFRUb4A1oaF-kmWy_qOxcNLRq1KKAyWN7UfG3XNasW3f8WO1zJoD53M0_iCcXQ1z2NEzsgqWrINdUh-icXBKywGtZsJ5P_7Gf1iuV9_lgwgmNdSPr0CRSvUnL9jzyvhR-EzJGe23h3E9QEDKDphq74gbVToFafkJ8dc5uuVjlSdjF35Qd_0XkFYmtiy7t5osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m28ajtiEB42rDxoI-gPaiQVRQzHaUyoqDd_RuoYeUL6TJErmF66wHPfUHKEvFiFFv4ydeRonbDChrMrzlBQ6OJvuFtfdE97wirSNyymOB4KDBB3H9ky4fVH6ap0IqReDi9NnVUa3p5VpHUbnYw2nN47_2mZ3iuZ03wt1cEdODSpNZgt3uUyvFs3PlGMiyTsFP5xaFtQAliwPpLFCWAmnX2LkGyagk3Eiz-gOGVrusjwDe3SgDk23FYJOLVrShfvkjWm-Dn_5cZyncKqQAEhq3ZGfJn_KQc_7l8iDYK3JmKWexfWRwH0AmV938kODJK2DZZMrXfN2odptQhL_aZBuvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونق جاروبافی در خراسا‌ن‌شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/461399" target="_blank">📅 18:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e75b37fe.mp4?token=E3Zm4Zy83A_M7GSj2upeBmjeNcLWg83HbqwcD3tXFqgRt3IAmaWimsa9_njJQ70bwuiZDOw_5nzX0aTSZNexGBxpcJmF5b4SVV_giaDD_6LnXKxkVTOBm24fSM9I0YF0HhrsT9yroQzkM91aaI3BrH9a_tcIGKp0StCyNzKI_CbszcrlYX8m3gdYrnNjQ_ei1vX9LRsOXUAiuvusTTGjV4j9xmKwxuEmIf6RiO9UuD-9HP2AYwmpz9bRF1Zwx5xvY8bX2QC4RJbpoSQUvSyhpFegvtGXBcMkfc57Gjjt1IC1Vq97C_C8TOQM18DWuSKLcaA4sJ94feC0NlJIGlzmdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e75b37fe.mp4?token=E3Zm4Zy83A_M7GSj2upeBmjeNcLWg83HbqwcD3tXFqgRt3IAmaWimsa9_njJQ70bwuiZDOw_5nzX0aTSZNexGBxpcJmF5b4SVV_giaDD_6LnXKxkVTOBm24fSM9I0YF0HhrsT9yroQzkM91aaI3BrH9a_tcIGKp0StCyNzKI_CbszcrlYX8m3gdYrnNjQ_ei1vX9LRsOXUAiuvusTTGjV4j9xmKwxuEmIf6RiO9UuD-9HP2AYwmpz9bRF1Zwx5xvY8bX2QC4RJbpoSQUvSyhpFegvtGXBcMkfc57Gjjt1IC1Vq97C_C8TOQM18DWuSKLcaA4sJ94feC0NlJIGlzmdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنایه پوتین به گروه جی۷ در نشست بریکس
🔹
رئیس‌جمهور روسیه: بیش از ۴۰ درصد تولید ناخالص جهان در ۵ سال گذشته متعلق به اعضای بریکس بوده.
🔹
درحالی‌که سهم گروه موسوم به هفت بزرگ (جی۷) تنها ۲۹ درصد بوده؛ نمی‌دانم چرا آن ائتلاف را بزرگ می‌نامند!
🔹
گروه جی۷ یک گروه اقتصادی متشکل از آمریکا، انگلیس، کانادا، فرانسه، آلمان، ایتالیا و ژاپن است.
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/461398" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461397">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4610158.mp4?token=UX-eMdSRMVi4d7gTeJ-EZYgVBbwa_hypAX99gQTx6Tsc2-r4VR5cgUr4GTLdeLBOleDhfA82MQDCHO-hXtlO-uT1bNQ47259By8QOgt29Ue_ZBUIlWD1U8ClazE_4qHaTNMHgQ3JMOyjy4wHtniccJZZqAO-Mly2qaHotpmt1YcaBaqyOcSP5EmL09FP5RVcp8aIWUK31z-7qhhdHrWXH1Zo_MMT6GuhTF_7RqrcVIF8Z_obejTEm01c0fOqB184Dz59_795io03XrpqJLFlWk1YdYiq6c6ruIIkfSTcAboCZW1SJUMHNwExJBVSEdonJly2Y0FJf2ZQSkzEDc2mTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4610158.mp4?token=UX-eMdSRMVi4d7gTeJ-EZYgVBbwa_hypAX99gQTx6Tsc2-r4VR5cgUr4GTLdeLBOleDhfA82MQDCHO-hXtlO-uT1bNQ47259By8QOgt29Ue_ZBUIlWD1U8ClazE_4qHaTNMHgQ3JMOyjy4wHtniccJZZqAO-Mly2qaHotpmt1YcaBaqyOcSP5EmL09FP5RVcp8aIWUK31z-7qhhdHrWXH1Zo_MMT6GuhTF_7RqrcVIF8Z_obejTEm01c0fOqB184Dz59_795io03XrpqJLFlWk1YdYiq6c6ruIIkfSTcAboCZW1SJUMHNwExJBVSEdonJly2Y0FJf2ZQSkzEDc2mTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلیپی از ابراز ارادت مجاهدین یمنی به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/461397" target="_blank">📅 17:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461396">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3c267ee1.mp4?token=Rf87RbghrxdZL2_9sU2RqAJbXbIICAbcUomRaNHq-izw2SneI1JTb7zr03Obei-qEPHP-VZImhALqEPWchToGXXCyTSvy4ohpOf8p1GfoMvM7JXy-0x8vSsUC1-csqNS4KH7zttcVL4e5r1d82erFMKQePmXDlPc0Nyzu7zZiyrgwUwXOGYDj9ND6s0nnDgadsdr9-C4AIZwrgbCY598tcEIhgkGN1_mJOazLdjwHyDIRYZVjMqAlPEWS95LrDgtFvc8BPijbdbyh39aus8tglpR5p3b0mVS3hs4V_Yv6pQB3-ckAT_oqHok5m13WRgIHOSJlgfZZ1XytBt6CLS1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3c267ee1.mp4?token=Rf87RbghrxdZL2_9sU2RqAJbXbIICAbcUomRaNHq-izw2SneI1JTb7zr03Obei-qEPHP-VZImhALqEPWchToGXXCyTSvy4ohpOf8p1GfoMvM7JXy-0x8vSsUC1-csqNS4KH7zttcVL4e5r1d82erFMKQePmXDlPc0Nyzu7zZiyrgwUwXOGYDj9ND6s0nnDgadsdr9-C4AIZwrgbCY598tcEIhgkGN1_mJOazLdjwHyDIRYZVjMqAlPEWS95LrDgtFvc8BPijbdbyh39aus8tglpR5p3b0mVS3hs4V_Yv6pQB3-ckAT_oqHok5m13WRgIHOSJlgfZZ1XytBt6CLS1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: یکی از پیشنهادات ایران برای بریکس راه‌اندازی صندوق بیمۀ ۱۰ میلیارد دلاری برای پروژه‌های بزرگ زیرساختی و انرژی است  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/461396" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461395">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk4L-je1Vfl33Lv1EezHWJYR-kRPjiaSUwN9ua46bDn5XOVyF5dcAx8CDCF5qKf92Q2P3N4zI2D43kZ-DeMQ65uvrOfZj9j_y2z-b36oxDuTDj-Vi_mBnYsS73O9lO2KNewHGNIiaqXNEVXHX7-5vNnpIetS6ugwbx47aj67BGt3cESMQguOnqx6y0zd-R9e8oAJx24Tg4KC36FWzAqOM20RWJt8HwbaZxSoZUuIn1y0L_f8SdTK8FP8uThMu-A1SnJ1bVWIDSRO9P2v2TcKvMOO6ZcqjyhJiZyH0twcO4YCfJnQFhFMzD0Cn3Cse9MvGiIrFPWOlRihBVttyu9New.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست ایران، عراق و کشورهای خلیج‌فارس دوشنبه در عمان
🔹
سخگوی وزارت خارجه از برگزاری نشست منطقه‌ای با حضور کشورهای ساحلی خلیج فارس و عراق در روز دوشنبه در عمان خبر داد .
🔹
بقائی گفته در این نشست در خصوص تعیین مسیرهای امن برای دریانوردی تجاری در تنگه هرمز تبادل نظر خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461395" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461394">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac23c245d.mp4?token=TAzf2dEG-hhTCVvL3cANeeKVt1_c3CLTjLiaLco1v1KoHJ8tkzZSqCPWelcK9A8DAm9WBKEzKXHc8ajqnj15BqfVHjrOm-B0I9paclYRlKczaBzFlg_DR9ybTV8G0hMXBjho4RJAw-ZxlD1XWUFhv0XfSs0ymJxNc872gsM3xaZ3OjNuBONhmrzmIK08wk6tI1T8_wDIAZveaKPg4fioJ7mOCx4zU3p6cRFZeFYZf90Y5dj7gG0QjPBb9L2ym70MvQjJdtpmF5k5MrYuPNUeSIk4yStdOpAmLIRDcSRBdMT3fzcLG40S6MikInWhUJln3V2BnvuL0MbC-CQ6QKW4ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac23c245d.mp4?token=TAzf2dEG-hhTCVvL3cANeeKVt1_c3CLTjLiaLco1v1KoHJ8tkzZSqCPWelcK9A8DAm9WBKEzKXHc8ajqnj15BqfVHjrOm-B0I9paclYRlKczaBzFlg_DR9ybTV8G0hMXBjho4RJAw-ZxlD1XWUFhv0XfSs0ymJxNc872gsM3xaZ3OjNuBONhmrzmIK08wk6tI1T8_wDIAZveaKPg4fioJ7mOCx4zU3p6cRFZeFYZf90Y5dj7gG0QjPBb9L2ym70MvQjJdtpmF5k5MrYuPNUeSIk4yStdOpAmLIRDcSRBdMT3fzcLG40S6MikInWhUJln3V2BnvuL0MbC-CQ6QKW4ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد در مرز ایران و ترکیه برخلاف شایعات جریان دارد
🔹
پیگیری خبرنگار فارس از پایانه مرزی بازرگان در آذربایجان غربی حاکی از تردد روان در این مرز بین‌المللی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/461394" target="_blank">📅 17:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461393">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOgRXmS6_XP_8-n0TTv-3OjOO9j0tDWHYhBiN_6fqP7P30WOW3kI_nx-CtQIoD6-vEI7SPacaBqq5619rHvZPzdOnYpsLRgOPrE1DTQfDV3-Gx4_IzSGYBhyxig-q9dW6s-91U5MqObMjozHW8pJxn8lY7lFevui2CbUyYQJdzWMRPQdAPjyXMmxzl5S0CjdoKzqGTvCVMfbhnVsf2l-rqs40NOPXBXmH1yE0p3LvStqiVQYP_aA9C-bYq-5TRmWhgqejHGB6IUgNSxyUp8a6AbjkBLWZRu_ResFtowIm2TbPYmwxrJWdB714IzPn4sBiqQcLjMrwDS7SvVcCuRVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: بحران‌ مالی بدهی‌ها برای آمریکا  تازه آغاز ماجراست
🔹
وزیر خزانه‌داری آمریکا با شعف و افتخار از تمایل خود برای به فقر کشاندن ایرانیان و فروپاشی اقتصاد ما سخن می‌گوید؛ حال آنکه خود در برابر از دست رفتن اعتماد جهانی به نظام مالی آمریکا، ناتوان و درمانده مانده است.
🔹
بحران ناشی از هزینه‌های تأمین مالی بدهی‌های آمریکا، تازه آغاز ماجراست.
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/461393" target="_blank">📅 16:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461392">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=coYj50ivXOPoXx4rxcMqO3y4plCtNCfBrZgrvJJmuDyZFlREAE5zfA96IYAVPl3QQRbe3IFYsyq8D9Yfk7kyasinEkiqSKUlwl0biKC52os5JCXwnL8snfqOa2k0Bt9NDj8CyCq2G7lgGL_c3-Fz0oeK9TX7AYnx3kc75ECyMRuPI2c8cZytytKjJs2QHc2-txrt6ji7E0ce-X76gt5K3nC746hjhSa4jCtpWXMH9EFxmHmBD7ig3SObc4X62CTha4yXRqwvXv_BIt3OCLoEWBmguJ5ofMha5NbEUljIm0tYlP7wMw-RrwlPClQObnkxB2tiFuzUbdIEgj5qs8ZYEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=coYj50ivXOPoXx4rxcMqO3y4plCtNCfBrZgrvJJmuDyZFlREAE5zfA96IYAVPl3QQRbe3IFYsyq8D9Yfk7kyasinEkiqSKUlwl0biKC52os5JCXwnL8snfqOa2k0Bt9NDj8CyCq2G7lgGL_c3-Fz0oeK9TX7AYnx3kc75ECyMRuPI2c8cZytytKjJs2QHc2-txrt6ji7E0ce-X76gt5K3nC746hjhSa4jCtpWXMH9EFxmHmBD7ig3SObc4X62CTha4yXRqwvXv_BIt3OCLoEWBmguJ5ofMha5NbEUljIm0tYlP7wMw-RrwlPClQObnkxB2tiFuzUbdIEgj5qs8ZYEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
قالیباف: مداخله‌های مالی و یا حتی دروغ‌های خزانه‌داری آمریکا دیگر تاثیری در مهار قیمت نفت ندارد
🔹
«اگر دنبال یک راهنمایی برای آیندهٔ بازار نفت می‌گردید و مقامات اقتصادی دولت آمریکا چیزی نمی‌گویند، بیایید به آینده نگاهی بیندازیم: وزارت خزانه داری برای کنترل…</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/461392" target="_blank">📅 16:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461391">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pegxKYkzCl-e2tRBie9rDNWk_1ZB0k9g4o2pKMd4K9FwsSZ2LAsJ_RT2-9dCQNk_VLTce55ZNbmmMcXrk1KwroqwQ2E0OyglFHbrt1jsf22tE27jdMF-sloBjos3mDWMHc9mhxN7jwdPBlO4inRgOiFO0ZjiP9lgjpc2YeuvfZGeerkT-HfOREf5sB4xzXbeCIbN0jCS8fNjUoGYhkfWsHYsWjfj6jtqd6ulDEkDi_6y8x-F5nWOsBGjN80fEs6jIGBLnZQBoVH-k6t75jZOht_WAK6746KMSE7_gojNxUuitG0Z0M4CF87nUs4fm0kpHnbjRI-MGwY0JJ2K3E1vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد جزایر آزادشده توسط انصارالله به ۴ رسید
🔹
نیروهای یمنی امروز با آزادسازی جزیرۀ میون از دست مزدوران سعودی و تثبیت تسلط بر جزایر زقر و حنیش بزرگ و کوچک به عملیات‌های خود ادامه دادند.
🔹
با تسلط نیروهای یمنی بر این جزایر در تنگۀ باب‌المندب، کنترل انصارالله…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461391" target="_blank">📅 16:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461390">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks7-jbLzzyFSQEZvAH6WY_NkBGYWDkQzximtht1dYKUoDG7Z6oRqrNRXaithW4mO3hD7PAIMHomyK2spATFUKx-0y9RwCL2cAboIibC3qf79AeNHeHe-2YlrH9lClqSxTYwiZszY1wcYVQz5RpULn5UxTB-f4GiU-Ll9Cr78NrQOBTlo7I6Cd-j5A3nzFEMIFtEoInCfeIIbRmOOpmDu6lHUG0TWFqj0uOgYPC0KOr6lkYLPe6CIEw1777oyoyyhHUpJBiIlMajncG86cKQEv9PWGimLtf4yGzx0HZaebXpA5OP9nDqdmz7KMkceL-vqRKzRulkTnN31ktUiJxh54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حماس شهادت ابوهیثم الیازوری، فرمانده محور خان‌یونس گردان‌های القسام را تایید کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/461390" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461389">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f316aab8.mp4?token=AyglLBCCXDnKkeiIOLmFVULspVgH2JlB3opp5NWP7vtSNPbKf78wH_fa0RzGmLca6cMm3m0TzpNACgfesYxMs7xnUU_vpK49bI2-id1G3TXYUePkKxzKHx1IcwTJvkYPIFXeJPKnyYoOr-4gNirl-Yr9zmel_Vq_kDUBE_cI2zuzASkhVBDXkG-yh0mQp_bQT17Q2h8J4N0Mt4GXAJhirAZR_UHZ-xSF_U08BaEo8SdVa6EwxZdDOYcU3N9LoKDMJDg3PPmp43E0oiJqlm_y3RWnusn-e8Dxov6SsD3RMQIPEVIVEDsScjDAcqxW6mJeIYBdve1Gc36oVsNuzkF4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f316aab8.mp4?token=AyglLBCCXDnKkeiIOLmFVULspVgH2JlB3opp5NWP7vtSNPbKf78wH_fa0RzGmLca6cMm3m0TzpNACgfesYxMs7xnUU_vpK49bI2-id1G3TXYUePkKxzKHx1IcwTJvkYPIFXeJPKnyYoOr-4gNirl-Yr9zmel_Vq_kDUBE_cI2zuzASkhVBDXkG-yh0mQp_bQT17Q2h8J4N0Mt4GXAJhirAZR_UHZ-xSF_U08BaEo8SdVa6EwxZdDOYcU3N9LoKDMJDg3PPmp43E0oiJqlm_y3RWnusn-e8Dxov6SsD3RMQIPEVIVEDsScjDAcqxW6mJeIYBdve1Gc36oVsNuzkF4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران با ذخایر عظیم و موقعیت ممتاز آمادگی دارد نقش شریک راهبردی را برای تامین انرژی و غذا ایفا کند  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461389" target="_blank">📅 16:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461388">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243a25b953.mp4?token=LHj0us-iElATTLaJlWUuVpI8SU0IB223a5WtglzXM9NDZ1wNGBBENvbaUbubyuffKVsFTTKNXFTyK9EjIVPHoa1gTdHiDP9Vn33Ml9YjoISDNSJ6OY0V84lbY5PWcK3wHTr4ljpo3TOCjQaDJ8RgsRD9bkJFywnva4_6nnbW5lpY1OB2UVGRj25rsg-jCRpB0bMxoZzBjK2y8fKp3CmB2WnkioWcl0R_z-IvTE5pilazULuWjZIKRfk0PrvSwQ_NGVU4E8PhLjq6RgfmfdNRnhzWpPNAqjntRhNUA99MIUU0FVwoqBhxVRU3SP4luD6osKcUtnCjDagmOMWL8Ywgdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243a25b953.mp4?token=LHj0us-iElATTLaJlWUuVpI8SU0IB223a5WtglzXM9NDZ1wNGBBENvbaUbubyuffKVsFTTKNXFTyK9EjIVPHoa1gTdHiDP9Vn33Ml9YjoISDNSJ6OY0V84lbY5PWcK3wHTr4ljpo3TOCjQaDJ8RgsRD9bkJFywnva4_6nnbW5lpY1OB2UVGRj25rsg-jCRpB0bMxoZzBjK2y8fKp3CmB2WnkioWcl0R_z-IvTE5pilazULuWjZIKRfk0PrvSwQ_NGVU4E8PhLjq6RgfmfdNRnhzWpPNAqjntRhNUA99MIUU0FVwoqBhxVRU3SP4luD6osKcUtnCjDagmOMWL8Ywgdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: بریکس باید شرایطی ایجاد کند که هیچ قدرتی نتواند اقتصاد اعضا را تحت‌تاثیر قرار دهد  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461388" target="_blank">📅 16:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461387">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/652564b011.mp4?token=Nw2xo93BNnxTPrCBJyHv9Wy0T6busGX-VVadiPHLDBjT5een9OsqmpM1Czo3Ajon8xMkiZJoN3Hu8fy81ZPindGlajkhnhxdZzR_am63OR_A_HX9JcYLCKCkqQ9nZKgva686tKKZ30Th-YL_JYw58xiIXa3p3hJgeXjWcgFwU125CrJq_UhbgYxsUiGFt7abl4I3vozM5ubr3qvxPBRy57lATC0zD0M92aEOv3es0lTXUhF-P_Za8RZn-Zy-1B_H5jOv6iYi7fustq01kBNUoQVztC_Bwo46qzOf3wCy62UaAdhkT4Cb8TECTxybmmbkPWAGgwCbw_O2oBk2TGMOeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/652564b011.mp4?token=Nw2xo93BNnxTPrCBJyHv9Wy0T6busGX-VVadiPHLDBjT5een9OsqmpM1Czo3Ajon8xMkiZJoN3Hu8fy81ZPindGlajkhnhxdZzR_am63OR_A_HX9JcYLCKCkqQ9nZKgva686tKKZ30Th-YL_JYw58xiIXa3p3hJgeXjWcgFwU125CrJq_UhbgYxsUiGFt7abl4I3vozM5ubr3qvxPBRy57lATC0zD0M92aEOv3es0lTXUhF-P_Za8RZn-Zy-1B_H5jOv6iYi7fustq01kBNUoQVztC_Bwo46qzOf3wCy62UaAdhkT4Cb8TECTxybmmbkPWAGgwCbw_O2oBk2TGMOeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عکس یادگاری سران بریکس باحضور پزشکیان و پوتین در کنار یکدیگر  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461387" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a436f57505.mp4?token=BNcqrEJnaku9NC3htyRpRZBmPRIo9qoHvi14l08h7l1rJl9X1cvB7-l5fMsBYnjgKBr1gxyNoB4RQRGM6Pqa6YWSCgIbgMdiI6cBJfcqGdFX_AUC3SlIrKCJO_Ra8qwnEgeys9R42AYY6HQF5PkygkdXjpvDtNJ-4rk3uSmFJY_mp4SPCMNXoX-4XKxtyCN5GP4bj29hb_cbnyXVEyXGBhYXL_-sMSE3WWOlNHafpkZ2cOsk1nMdOZhrZOtsqwqbGp2vUgwNU-ab--0-gbcZiD775e8i9dEBIZClvGbL1pYBTuSWRDFRzIRmfbGTKJ_R4hOTcgc68bnHXhn5n1PZQVVqnawsi-ZNeM1BKjeRzyrDK-DCjLdGb2NdHXz59aELOzIktiDD3Rt_LJlJUQH9l5Xq39SfxyASB0iEFPzEuCQISnrpqpGl_vZzawZfIrEWn6AvmO4anK4PbhpUmlqfpjmFfPw2ypY_c_WsAPFasTSyxGbB7LnibKAw4FTHrTlZnKrs_4FdSLrVbHjE_WnHN2dXrGHBzo7hn5HaK0VY6EJcfrHFBIDO_dAjH6vucT9nt7Sad5kMkDMdrRMyvxg5M62fNSLcMg7iX9K7gQnAJnALXsk1BJtU8PYtffksFQOtd-hydgzRMCyq5Jh1wNOx6P4HSO__hWh-nE7DbLkV-wE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a436f57505.mp4?token=BNcqrEJnaku9NC3htyRpRZBmPRIo9qoHvi14l08h7l1rJl9X1cvB7-l5fMsBYnjgKBr1gxyNoB4RQRGM6Pqa6YWSCgIbgMdiI6cBJfcqGdFX_AUC3SlIrKCJO_Ra8qwnEgeys9R42AYY6HQF5PkygkdXjpvDtNJ-4rk3uSmFJY_mp4SPCMNXoX-4XKxtyCN5GP4bj29hb_cbnyXVEyXGBhYXL_-sMSE3WWOlNHafpkZ2cOsk1nMdOZhrZOtsqwqbGp2vUgwNU-ab--0-gbcZiD775e8i9dEBIZClvGbL1pYBTuSWRDFRzIRmfbGTKJ_R4hOTcgc68bnHXhn5n1PZQVVqnawsi-ZNeM1BKjeRzyrDK-DCjLdGb2NdHXz59aELOzIktiDD3Rt_LJlJUQH9l5Xq39SfxyASB0iEFPzEuCQISnrpqpGl_vZzawZfIrEWn6AvmO4anK4PbhpUmlqfpjmFfPw2ypY_c_WsAPFasTSyxGbB7LnibKAw4FTHrTlZnKrs_4FdSLrVbHjE_WnHN2dXrGHBzo7hn5HaK0VY6EJcfrHFBIDO_dAjH6vucT9nt7Sad5kMkDMdrRMyvxg5M62fNSLcMg7iX9K7gQnAJnALXsk1BJtU8PYtffksFQOtd-hydgzRMCyq5Jh1wNOx6P4HSO__hWh-nE7DbLkV-wE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای یمنی تانک‌ها و تجهیزات مزدوران سعودی را به غنیمت می‌گیرند
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461384" target="_blank">📅 15:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
حاج رضا برکتی: مادر هر روز با عشق، انگار برای یک سلبریتی غذا می‌پزد / تا هست، دستش را ببوس؛ یک «دستت درد نکنه» کمترین جواب این همه محبت است
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461383" target="_blank">📅 15:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-text">🌆
هر شهر، بخشی از یک روایت ملی‌‌ست...
۹۸ سال کنار ایران
🇮🇷
📍
کردستان
صدای ایران؛ سرزمینی که باید آن‌ را شنید
و باید آن ‌را دید...
در مهربانی مردمی که ریشه در این خاک دارند.
🤍
#اعتماد_می‌ماند
#۹۸سال_کنار_ایران
📥
دانلود
#بام
،
سامانه بانکداری دیجیتال بانک ملی:
📲
https://baambank.ir
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461382" target="_blank">📅 15:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461381" target="_blank">📅 15:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf797f04f.mp4?token=PYlbIau0xb_7gB7RLJnPQwXNyTP6jPP3PfcsSQVM16BFu75WztVhBY527Au65kcnhRiaxdZ_UGJ21dvYTXgxklTpqXUdZNAsZBbZSNPCx8YG-XSbsvSWwSLm6wd7Z3-nU3WkloaGVDJQ6JAIwJNPA5AWFL0i0cjtpKxTKLWSJIpBlg9HWtD_xNuPQ99hLzN7kn3CuptcT6Kv0zsUE_2rCPQYIvfhkEmrdyedl7-isyslfXbPJxqyGf_P3GHbW6yHfQNqmJf5YGOZgN8cP-wXDRerWBuYKrLsDqCZ3hKKeABa-FsQ2gLOXQ3e5tVswSvwNUNA8qdcVJUYNedwL6zY7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf797f04f.mp4?token=PYlbIau0xb_7gB7RLJnPQwXNyTP6jPP3PfcsSQVM16BFu75WztVhBY527Au65kcnhRiaxdZ_UGJ21dvYTXgxklTpqXUdZNAsZBbZSNPCx8YG-XSbsvSWwSLm6wd7Z3-nU3WkloaGVDJQ6JAIwJNPA5AWFL0i0cjtpKxTKLWSJIpBlg9HWtD_xNuPQ99hLzN7kn3CuptcT6Kv0zsUE_2rCPQYIvfhkEmrdyedl7-isyslfXbPJxqyGf_P3GHbW6yHfQNqmJf5YGOZgN8cP-wXDRerWBuYKrLsDqCZ3hKKeABa-FsQ2gLOXQ3e5tVswSvwNUNA8qdcVJUYNedwL6zY7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هدف ما  در بریکس مبارزه با یک‌جانبه‌گرایی آمریکاست
🔹
در بانک نوین بریکس سرمایه‌گذاری‌های مشترک بدون وابستگی به دلار انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461380" target="_blank">📅 15:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhyRUBGDjaauXolFo69tL2I20IfphrDWFdVkqyu2ajQ92tSyBh5fA0KID8rSOVVUXBSmoWaXghKH_iap0YZ3tc3r7E1ywzzFeVjg0UzrfhAfnL_zBjfG_hA3OHZjzXkkEs8mkRVKQ4MWiYVFVN6tV7qzuP5bEw207kPZoYr2x5-UTqrUQLxPsNeCqb7SWCC4gV0D_-RKxyeJl7mW3lGn8ZROeB1IW8UMWhStJqXCyAzrw4pah7XRrmfVWL8QWG6RUaqGJotA0EgxTnODun0DerjGLAuED0lGnS75kVWgt9BGV99GF8gQetRzvdPSlngE8sjvto9lW2MUaIXAY-2VhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب، حردانی را از استقلال کنار گذاشت
⚽️
بختیاری‌زاده: تا زمانی که من سرمربی باشم حردانی دیگر در استقلال جایی نخواهد داشت.
⚽️
او  فقط به خاطر صحنه ضربه ایستگاهی در دربی کنار گذاشته نشده و از اول فصل ۳ بار به خاطر بی‌نظمی به او تذکر دادم. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461379" target="_blank">📅 15:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6hFT8vzHFd3Fbmr149VPCzHN0rjCkSL5_f405S_SNVHzgyeNVsLrwDWX0jG-vYwaRJcIwj_bhF0Rv2yNzDULCRYNDQzwBKfssQDY2kCgYFu5nPn1NpNH3AOyYUjKstA8671Jsfp09SihSH1dsZa-btFFUcmV2Wt_XyHgwhi8lU8Qiyo_vEtdRdRUIYGrBCyYRuSaS50tFORCPUCEgrrZDrL5ouO2b_BntnoOGElnGzM8wo9RYqtk68YhfWscMjQlIRTnHyrWGdewndtz1NV16viik8sVx5xixVhP3OuFUB0fizXfJ25Aic4Lf5GsPnd0Lobtjd1xScmdQduR2L_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد جزایر آزادشده توسط انصارالله به ۴ رسید
🔹
نیروهای یمنی امروز با آزادسازی جزیرۀ میون از دست مزدوران سعودی و تثبیت تسلط بر جزایر زقر و حنیش بزرگ و کوچک به عملیات‌های خود ادامه دادند.
🔹
با تسلط نیروهای یمنی بر این جزایر در تنگۀ باب‌المندب، کنترل انصارالله بر این آبراه استراتژیک جهان که ۱۰ درصد انرژی جهان از آن عبور می‌کند تکمیل شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461378" target="_blank">📅 15:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFZkqhFHFcA_PmG8jZmz29vZWBnPDHu6KqJa6JtLuZFP8fjsx8DpVE_z-rG_ecFE4cIwFNO-KNRZBT9HaKCDrHuLAbSTNlTvDhdQgwQlMOVf_2HcPuIzS_1N8qcxjfVM6VoFMZKcoKGVJ6lOICgVI-o9li0I58lhSzoJ2SybptU8Vu44vkKgjzk-RcqAsFfNyB8SX6alN8u39_lCvQPv2s50mKmhDDi5TiZvP1VfCG69N0powirvVDOeGdd6GFqzNJQ52AaN0KtINZPcyNb72bUvaEV_P-Yel9qs6v75VhOMITYn-gDa0ovAhtvXArcwNcHcpkADagbrVPOMHkHclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده‌باش در ۱۸ استان برای سیلاب و رگبار از شنبه
🔹
سامانۀ بارشی با احتنمال ایجاد سیلاب و رگبار شدید، از فردا در آذربایجان‌غربی، آذربایجان‌شرقی، اردبیل، کردستان، گیلان، مازندران، گلستان، زنجان، قزوین، البرز و تهران فعال می‌شود.
🔹
شمال استان‌های همدان و مرکزی، جنوب کرمان، شرق و شمال هرمزگان و ارتفاعات سمنان نیز در محدودۀ تأثیر این سامانه قرار می‌گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461377" target="_blank">📅 14:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzniFJ028LPT0cn_r-Yt5vuQs7BDSOn5pmtWN5NLYyv7auxPitHjnN6tLDDwyerFtZWMSZp7TqZ3fl4qL-qmGUOSYf0tMKa0Y8OHGada7R-1O4FiTzKIjkdulI2BS-9ZZo8m0u0_2ruzPGCEFZsobao5ocgYMcbj8AMfnYj-gCUq6jAJdUrbIkZrino0MHXOPxHxg7_CCeQnjnlgFEhrY6Fj9MbpnXehW47WV_VtLu4JJ-AFca5uHqywjLUWPw_pYlIZ2NlRGg16AzsSJZLi8yYRWOMqd4d2ysfdO5U2fcMYuhEyrE9V1MR4o9ahVfYIWpavm9Gh1TeZ9tQhzNpKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: فتح مبین انصارالله ثابت کرد امنیت خریدنی نیست
🔹
آمریکا و متحدانش در استراتژی و تاکتیک به بن‌بست رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461376" target="_blank">📅 14:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461375">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF-nNXccDhF4atI46esdbAfJ3pxhOw4x0hJMYUiJDn0-mYwkww28rybmYuDD6B5zNxLxvwjsggsssizTtMTERFWR433kUc7ey5NKtZWrchgWj9HqWyRXUTI7n6Ab_5NsYo8IVcPOldDV7J-nWPJG6GRR4sVILm1OyulCNyTvpGUQf9V_xyO5LSXs6IltdUxcHUyHrw-npwGNDljmDy_x570PaTwyNlanMwNFAzfS6gArWL1xWIdql9eWs27H6WwEMHmtASdDjOsRxrPSsqobLMK-TQl_jQR_Dzvgt0n34mQn-BsGm9dr-XF9NMQQ9AOuglwMW12tqxeS8jqXABCpFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم حملات رژیم اشغالگر به جنوب لبنان
🔹
گزارش خبرنگار المیادین در جنوب لبنان: آمار تجاوزات اسرائیل تا این لحظه شامل یک مورد انفجار در شهرک برعشیت و ۷ مورد انفجار در شهرک المنصوری بوده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461375" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461374">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBhIMQfkrf_53IgrFSCSOs5D3IEdP9DonY0bcGCoHm3Lno8ys9gS0ZSEp0yJWed8Oin7TJh2PBdPDJV4h613l-2EzDqCmBNqoc_PjVtWbnEu5uc29SVCy5xHf_HFXmKb8Rmsy3LtWIHknEIhFeiGEvGliFx6PT7fgtuR3k7Xc0cKH1tsdthWVKnGlUSHRVFyJryIumu4l8dlqp6nAmmuHehv_-T7JQiNyCLKEB1v3pHTE2on0bESeIRu3Z6Jz8U9fU3Bflk-9GYsv0KxgateaVUdUJP5Kgx50udxvjuaeYGJuSU1Xrd-RzqDTQYF8mLx68cQNbkvg5kJQIE1vPFfnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ ماهی‌گیر ایرانی بازداشتی در امارات به میهن بازگشتند
🔹
سرکنسولگری ایران در دوبی از آزاد شدن ۱۰ ماهگیر ایرانی بازداشتی در امارات و بازگشت آن‌ها به کشور خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461374" target="_blank">📅 13:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461373">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwUchaYL9t1ERVpTqTwDgP2B1flJo_pUmgDT4Rn__VghJtsr8TvtLSafL0methmDxnqnz7aKQ8RzyiXrvqEcbqNMfc0jD3zwsGqj6oNhALyxQov4f33puKjs67vNkhLbedqIZWUqykiNO9pxGq4AEy5k5fGldACDBz59VwTptw51pfxoLfQgSxIAUcZDT13PhkvnGYvmapWI927nPD_ErhvZOAhVbKWC_h7hujf3z9MlF3Px2WffE6KJqu9qP4adXeum3GWaTeF_WN47VTPAzC-UWxmhoXGSBX2cTDvlIMBe0Dk6aljQwegGQoC4wb_x4bGwqxO2QccL3Ls0gLi3ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عضو ارشد انصارالله یمن: هرگونه حملۀ عربستان به زیرساخت شهرهای یمنی آزادشده، با پاسخ متقابل مواجه خواهد شد
🔸
نیروی هوایی عربستان در ساعات گذشته به فرودگاه بندر المخا، شهری که روز گذشته به دست نیروهای یمنی آزاد شد حمله کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461373" target="_blank">📅 13:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461372">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlQ-5cwx7p81jSgGAqHVEd3VMxlpa-SFq1-wsNjIVElbmI55DD1MGBtH3YIpFMXhII9OQn53pC9ECA-XbFXdyrdDauTfotdVeeywpTqzTbcK3ekI3kY-ejl2-uG65oV5KwhNgEn8gorbOtB-ECgN7e4lXRzgzVlQf4TvdFwrMut0DmjOSQpvrdz_ZHThGETa6ppZDClVdLgBLsK7JXjwOo0i4_zyhSofDLQDo65t_Nic9FGJ-P_ydYtE-NKPU7tjY0DpoO27vX0v-BqXnm_BKjBB_RlI_8lNxcrJMlIFJ36tCWwEKqva7B9BzW0k7gG3qzbeHdBGOjwNd0_iPlQUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: از پیروزی‌‎های ملت یمن خرسندیم
🔹
پیام ما همچون گذشته به حکام منطقه دعوت به عقلانیت، رهایی از وابستگی و وحدت حول پرچم اسلام است.
🔹
تشکیل بلوک مقتدر اقتصادی و سیاسی اسلامی با رعایت شئون همسایگی و انسجام منطقه‌ای، ضامن منافع امت اسلامی است.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461372" target="_blank">📅 13:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRBmMi__sqtPHX3Ivzjpzi6BCg_hYAmMM8OgiXa_eVNw2EFR7_KFj1TLiVKsWDVIjlynKuk-sRhh5TlIXnx36uPSJwq4XYG2ApokfOp2GfqfiYApGOz9GVdrNsdx8Q_w5B6FaEzjC3N49Z1U4Wrez6RbuGL9TbGcMkq21CNk1m59s_Gr8vZlEtWhxDTF0yHQY7KUl-LcX3HmH64G-Y8A44Kki9ydZFk8_qfn9b9Hxa_PuIeNMHDiCpL2Wo-jGlgx7pxHo_c3ezCarKbOM8My71fEGfL-8ZHEKF58h5V82MZLQ5jf_C3IIKw85Ak-rEGGivT9EGKZJKI5rBXSLQpNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزائر با امارات قطع رابطه کرد
🔹
دولت الجزائر با اعلام تصمیم قطع روابط دیپلماتیک با امارات متحده عربی، ۴۸ ساعت به سفیر ابوظبی مهلت داد تا خاک این کشور را ترک کند.
🔹
رسانه‌های الجزائری میگویند تصمیم قطع روابط به علت رفتارهای تحریک‌آمیز یا خصمانۀ امارات اتخاذ شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461371" target="_blank">📅 13:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461370">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TM71ST6OaY4ArLKVGRQPqOsYY8w_rUYO-YMtS-HXSkYe9eMDYoKJvfiOSGzeinCV4mk3vtL37i91gart7vzNcnKuIijN0gBiw5HQosqprR30JU3TC2BLxZAHpCny8PbQf-XjLy-5oF2QuWHDiHgVwkyKpYg21DJnq0TDqtBI2-E_PVDD8tdAnWE4kvemcS4xuDwgEU4duPDJy1xPL4GrPgs8XFkpvrVEac0du9IIR22JcUkaHWislQJz73P-cft9d2D4ynbh3tB_eGb3_iMIKDIT_rrf2i3ytRG2El6lMV6W5EL9g4uXj-AeRAhZ5ty_iSgEqPb0lIp3mzr4v2qmEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فوتی و ۱۰ مصدوم در حادثۀ برخورد خودرو با تجمع‌کنندگان در مشهد
🔹
ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد مشهد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و بیش از ۱۰ نفر زخمی شدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461370" target="_blank">📅 13:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461369">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91036a20b4.mp4?token=XskxT_h-rnNYCrOYw4wxPJMB5bh2RjyeFxzDcvguJatnvC3xhbMmP_TYnuewIEOl1TQ59zFZg5XTkDyDSLwGiZcXHBHeso4iL8acxZdkK0a-vJiB1pQLIavHi7K4ZliO5VVlCwyFydmcf_InwL7KQG1AbOoS-_IoewxCQijptrnEesvMbG714kWkVMEJ_wD0OPtKLSt8-ZWZe5bOamGbslcKcyUaz31wObdoP4u1_LydtqHOjMPnhQ7-KUOZiT0b4dfcVxrWPoFlK6kaicRMRGO5kd9zyyzaaXef3g4T3ea5FllQG-MYw0GlSwYqccX9fRMDCT1CYLX_Su54tJL7nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91036a20b4.mp4?token=XskxT_h-rnNYCrOYw4wxPJMB5bh2RjyeFxzDcvguJatnvC3xhbMmP_TYnuewIEOl1TQ59zFZg5XTkDyDSLwGiZcXHBHeso4iL8acxZdkK0a-vJiB1pQLIavHi7K4ZliO5VVlCwyFydmcf_InwL7KQG1AbOoS-_IoewxCQijptrnEesvMbG714kWkVMEJ_wD0OPtKLSt8-ZWZe5bOamGbslcKcyUaz31wObdoP4u1_LydtqHOjMPnhQ7-KUOZiT0b4dfcVxrWPoFlK6kaicRMRGO5kd9zyyzaaXef3g4T3ea5FllQG-MYw0GlSwYqccX9fRMDCT1CYLX_Su54tJL7nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: تاج بازی بدون تماشاگر در لیگ را ممنوع کرده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461369" target="_blank">📅 12:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461368">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9aQsQMvhaBRVGi5i1fiURpHiSsT05wnPVa5PHw4i_JaVqPg8rDz8KsdqfbfYJVaPd_T7NYArsMGhAZpcA9JSgMBi0zqjpa0SIkU-FNc7zisHT6gPTDvU3mCJhiRalNoC40ckiYDD98N-PM9BzLdtk61MymHQu6q5BrsaXlydp_8EMtKWRIiCvwI3fFDIrQiHlASxpX7SvCxErguJNMildcG7gMb5W5hVC46QPjDe6AcVMHjtNMnQeDoHxV4ppW42HOx_OSe5cm0buAeK-N4E5PNyAhu12QeHWzWx8AR3TOqXwI4JG9ZAhZNJb7nwaxOEKgAr-4QlPgkNFbfHBAASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه،‌ لیتوانی را به حمله اتمی تهدید کرد
🔹
پسکوف، سخنگوی دولت روسیه: در صورت استقرار تسلیحات اتمی در لیتوانی، خاک این کشور هدف مشروع ودر تیررس سلاح‌های هسته‌ای ما خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/461368" target="_blank">📅 11:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461367">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c41b04fc9.mp4?token=XMtgqsaLJDrWGadcVadBwSoZxsNJETxMQCGHCBRQfbDjG7vz1QwQPkY0yjouub0Ox62h2fblDA311LUq4zwomKAAJ8esHZsm6d_akT5_8eqVCh-lcn7UBGFYEfXp2VLUxadfXBdUuNeFRne-RVA9kurfuV2Sthoshq_OAqsQEDQnhi4csOqdC21B9JYLsneRXMsI3AGckI2YKV4QMkSB8OsOGVkrNgM2RXqzt8acpV8kGIYPuF4NcoRRwARBHLiARDBMnXuf8g74RQdswgXCoI2v7BJLptoIKHBuNiHRg-6xVgFmm6526lNFRyuAuqLIGH4SIhj60C-amVX28_Z_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c41b04fc9.mp4?token=XMtgqsaLJDrWGadcVadBwSoZxsNJETxMQCGHCBRQfbDjG7vz1QwQPkY0yjouub0Ox62h2fblDA311LUq4zwomKAAJ8esHZsm6d_akT5_8eqVCh-lcn7UBGFYEfXp2VLUxadfXBdUuNeFRne-RVA9kurfuV2Sthoshq_OAqsQEDQnhi4csOqdC21B9JYLsneRXMsI3AGckI2YKV4QMkSB8OsOGVkrNgM2RXqzt8acpV8kGIYPuF4NcoRRwARBHLiARDBMnXuf8g74RQdswgXCoI2v7BJLptoIKHBuNiHRg-6xVgFmm6526lNFRyuAuqLIGH4SIhj60C-amVX28_Z_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصبانیت ترامپ از گزارش وال استریت ژورنال درباره ایران
🔹
گزارش نشریه آمریکایی درباره احتمال ادامه یافتن جنگ آمریکا علیه ایران تا پایان دوره ریاست جمهوری  ترامپ، با واکنش تند او همراه شد.
🔹
ترامپ در پاسخ به سوال خبرنگاران در فرودگاه دالاس مدعی شد که «اصلا احتمال چنین چیزی وجود ندارد».
🔹
وی افزود‌ «آنها یکی از نادرست‌ترین نشریه‌هایی هستند که تا به حال خوانده‌ام».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/461367" target="_blank">📅 11:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461366">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVmzQfbkXausWy3kQctH0kCvCgu2A2E6OhTjMO73WspskdEOGjTkAJhY8o6Llg1GyY3POkiX9ILIMgCsAu27Z0WsK9CnqwcI67zLQdQUL4hCKdVfd83ocwnUB_QYxiPK27V17O7q1d3EbQ-7e4rw5wo0TNNmkzhT9eiFT9kzac2APnlFjglRr2nuIcsHPCIilPxYnZ3N9WGmlwV0MSfjZIO6osmZ5RxBz7SL4FiY5IKCRY7kk0560f4Ja0yfmQSFfMSnT1UEmqIUAiUhVm8L10oBQx5g3SHkpOh7e2mM9Gc0AZXqiTGZJd3a62UNkTaVjmoXUu_hTaVtqBMdMeECRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت گران شد، عاصم منیر دست به کار شد!
🔹
با افزایش قیمت جهانی نفت و همچنین گران‌ترشدن قیمت بنزین و گازوئیل در ایالات‌متحده، واسطه‌های ترامپ برای کاهش تنش‌ها با ایران دوباره وارد میدان شدند.
🔹
رویترز گزارش داده که عاصم منیر، فرماندۀ ارتش پاکستان به‌منظور تلاش برای کاهش تنش‌ها با عراقچی رایزنی کرده است.
🔹
رویترز گفته در این گفت‌وگو دربارۀ امکان بازگشت به مذاکرات و تحولات مرتبط با حملات انصارالله یمن به عربستان سعودی صحبت شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/461366" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461365">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHh-8nF2NLDazqwt20e7A_YGZPA8ZjJ73kvhxjQ_KTTEd4v7rUpuLpDYUi3adoPNASN9r99jHQSZ_BFugV5LqCIFH4-kkzNnktBXxSFo3VhPIzyZ2-ZyC6dXhKT-xYbep-tmRO40qdRzxPUlMvwkwC5Fv0Zp9NQq1xmE1gGUF3zOS8tjH295W11awoMcyKPGiQBAufv3qDHuqBmib8KK66huYgH6Bd6bQDCrIlO-G1Xst-IsRmqk2NOnF0WGemkvLl3R5bcd2TOrlIVcSI8Gb9yLDtZEOrg8BnN9EwTv3Cr-l24fUSSCfdrQyuQ7tzbB57od9Jg8g0NpFf4ZVqW8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک نوین بریکس</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/461365" target="_blank">📅 11:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461364">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PBvo2qEkHW8kJeu-bb7Ht8Qr9LtCSCihK0yrcyuzmzsljB1B-pbjYkxnAH8LRq8hLRR_0pKLt5qwdWh2noWUM70HVcpTbX9aNB_2lKR1xMxZbVBvUZNZ34fyrTu3-QYaQT2dBa3GqTjFh35JY9dK6uSJfsHiyzIirHvu_O4U6fdMTMIYDqhrCtWaF92cd6EaMqYxEjYmvigqmCTf-czkcdtWbaUpeTmFa-j0ns_sJqo0rwKJXLH-V9V4dNxaz629XEtINQv0MZ8Mp77uMM1VEH_nqPp1OhnvXK2GGclf5KYSxtfiHjOhLOQcTwBdWDPGxwxib0YJeOaMWjZtSMmkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای نخستین بار در معدن‌کاری ایران
چادرملو به عمق 300 متر می‌رود
🔹
مدیرعامل شرکت معدنی و صنعتی چادرملو با تشریح برنامه‌های این شرکت برای تأمین پایدار خوراک، از ارزیابی فنی و اقتصادی ذخایر T1 و T2 در عمق بیش از ۳۰۰ متر خبر داد و گفت: چادرملو در نیمه دوم سال ۱۴۰۵ برای انعقاد قرارداد و آغاز عملیات استخراج زیرزمینی این ذخایر اقدام خواهد کرد.
🔹
به گزارش روابط عمومی چادرملو، فرید دهقانی، سخنران اصلی کنفرانس استیل پرایس، با تشریح وضعیت تأمین خوراک این شرکت اظهار داشت: در سال‌های گذشته با دقت بسیار بالا نسبت به اکتشاف ذخایر جدید در عمق اقدام کردیم. راه‌اندازی معادن جدید در D19 و آنومالی ۱۰ هم در جبهه شمالی و جنوبی، و اکتشافات بسیار جدی در معادن A21 و A19 حال انجام است.
🔹
دهقانی ادامه داد: یکی از مهم‌ترین اقدامات چادرملو در دو سال گذشته، ارزیابی کامل و فنی و اقتصادی ذخایر T1 و T2 در عمق بالای ۳۰۰ متر بوده است و فعلاً از این عمق شروع می‌کنیم.
🔹
مدیرعامل چادرملو تصریح کرد: برای استخراج زیرزمینی این ذخایر، اقدامات لازم صورت گرفته و قرار است در نیمه دوم سال ۱۴۰۵ برای انعقاد قرارداد و شروع عملیات استخراج اقدام کنیم.
🔹
وی تصریح کرد: این عملیات با مشارکت شرکت‌های داخلی و شرکت‌های خارجی انجام می‌شود و کل مطالعات پایه‌ای را انجام می‌دهند.
🔹
دهقانی با تأکید بر اهمیت اکتشاف برای تداوم فعالیت‌های معدنی چادرملو اظهار داشت: همه ما واقفیم که اکتشاف چادرملو یک ضرورت راهبردی برای بقا است. به همین خاطر در ۱۶ محدوده در یک‌ منطقه و ۴ محدوده در منطقه دیگر نسبت به اکتشاف اقدام کرده‌ایم و در معدن زمان‎آباد به یک جمع‌بندی خوب رسیده‌ایم.
🔹
مدیرعامل شرکت معدنی و صنعتی چادرملو ابراز امیدواری کرد که در سال‌های ۱۴۰۵ و ۱۴۰۶، توسعه بالادستی بخش معدن چادرملو به‌عنوان یک راهبرد اصلی مورد نیاز و ضرورت اصلی، برای بقای تولید و سودآوری این شرکت محقق شود.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461364" target="_blank">📅 11:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461363">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxnhESTIA77vRiDGpSrdVJfe-UIIlD4N7W7pkgiVmynMGceiy3XLh1SAXlBdPUXYjhGzxlJFVfXHkZV22fLtXzA20yWzWpAJdiOzzl17IB3Z2jG0tlmZKQ8Y4OuILXc68aDBof_ciwlTs2Xn-9y5t7lbir9reERWStLIaw4E00yLDaRj1ilZeL54Ahf0cBvHJgeRi5TJHXfJvYq7LT3rUJyybBQe-Dgq3SeKXgdJW64fVxqbZu29VlCu9Tnn8_qg5LC0uWWBgJQB_VE80eQUCy_CFcijz7vRFu7XJw5akYcGqkUGqTbhTxahlmmXRdGqmFmNv_51Rn-7CK4Y7-YIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
شتاب‌دهی به تامین مالی واحدهای تولیدی با ابزارهای نوین بانکی
🔹️
مدیرعامل بانک رفاه کارگران گفت: طراحی و بهره‌برداری از ابزارهای نوین بانکی مانند اوراق گواهی سپرده خاص، کارت رفاهی متصل به اوراق گام، فکتورینگ و برات الکترونیک، حاصل تلاش و همراهی تمامی ارکان بانک رفاه است. این ابزارها، تامین مالی واحدهای تولیدی را تسهیل و تسریع می‌کند.
🔹️
دکتر اسماعیل للـه‌گانی با بیان این مطلب در اولین نشست سراسری مدیران صف و ستاد بانک رفاه در سال 1405 تأکید کرد: توسعه این ابزارها و استمرار رویکرد نوآورانه، می‌تواند ضمن تنوع‌بخشی به خدمات بانک، ظرفیت‌های جدیدی برای ایفای نقش مؤثرتر در تأمین مالی بخش‌های مختلف اقتصاد ایجاد کند.
🔹️
وی بر تداوم مسیر توسعه و نوآوری بانک رفاه کارگران تأکید کرد و گفت: آنچه امروز در این بانک به دست آمده، حاصل تلاش جمعی تمامی ارکان و کارکنان بانک است و استمرار این مسیر نیازمند هم‌افزایی، هدف‌گذاری جدید و تبدیل ظرفیت‌های موجود به مزیت‌های پایدار با هدف ارائه خدمات مناسب به مشتریان است.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461363" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461362">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461362" target="_blank">📅 11:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461360">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR3Cw32S_a3Cvwb2v19OHtIyJem4q083cuOc52osdRD54UBze7VY1ArqjO0eWKYSJWUpWvVo8oam--aSCf6Ulblwpxs7SaT78elsjGX_Pkc2NEmr8dzkSbPNy5Fii01eXOdTrJgq8-tmn_FgX-LGy6cBnVz5HXZZoE6fYBahBIH7xDod8hdCJ55rhgmUoviy5OWhLld8d4tkfR0UN8cKwX8QceR-hyeR9I2ZuKxp79wAC4plykD0is2rUfNnw8cs5f_y9mSevWDIK9-ReqnyUiuTiv_P5GeEdAiXdAQpj7cYETgsS8RzeHkiTZ4PiWv-OxKCZ341m1cTrgQ73wKBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست رد ترامپ به خواهش بن‌سلمان دربارۀ یمن
🔹
رسانه‌های آمریکایی می‌گویند که ولی‌عهد سعودی پس‌از حملات شدید یمن، ۲ مرتبه از ترامپ درخواست کرده تا آمریکا به این جنگ ورود کند و به یمن حمله کند اما با پاسخ منفی مواجه شده است.
🔹
آکسیوس دراین‌باره گفته مقامات آمریکا به همتایان سعودی گفته‌اند که ترامپ دستور داده نیروهای آمریکایی بر ایران و تنگه هرمز متمرکز بمانند و از گشودن جبهه دیگری خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/461360" target="_blank">📅 10:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461353">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0dfIGQsxKJnHM4yT-2osgFr_ELXoIAG7utLlxMP5sVttAhQInZmuFv0TMH8L-ufmTa7is8alUFh93D75hPjEXDleZq_f_Mn78GvUUiysrvs5xUqA_UIjPa2b4WSDJBDB31CeMuy8yOEnmwKTj8Z9Udp4ooONvUduhPkaBL_EsyKPGQLSzfh2S5lRmRsL8b-kCMXftUj8nWumDf43zFiHC73Vlo6oF8mHDVe0gVM3yoTj4-I5GxLGReSA7TDFYAf7bTcUimQTC1TXrJ9966m3Y49Eu6vSBnRIo01rZHeEw0AnS-StUA-bzidt7f8WO7SjcaxtASwdqRvJ6DinUPZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMDcirRbR4vbIBnjj2Yd-jePoGrbEvdXxeVZ36tXXxXAZVxwvhOSym0UW05FxGxn-ssNl-Sh51IzfV5Che8l69ne6azrCFceQDBMzSt7yCTwnycwZCNISsmOZ_FHEytGMxDTxtpzlots9IrkhXgO4C6oBTz6EWIegGLaUHk8HsE58cIqpYl5zK3eFY5aG6DfcKloX7ylRGIJxzIEddVObcmSYfcy1rfxosZ2CtGJWW3pvUrj0SEnzO3MwXo_YB1tO-bSb1B1Pz-KHVMfqf0ZDudeeL5xO514LX1eFDyyGIPg4fsYuTyofQBW1BGqHPWFv2GrVoBL--z5qxw-6tSpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjtHi9BgpshkowcVqyze8SJXdfqmfEg6-M2AniW3EseekbOnQD45RgPrcXLVBLy7uGtZcHnEGpCHcj0VU5tgznkkzUmajZB7yjmrENzBtw3Kp4b1BxgYea_qEyGHsGtC773PAp5D0PakVqmzTN58SSZziynuuWUuLMRmBEHmwXtdgbaeXeKgXhBuRqa23MRCU-HScivbyEC06AWG1hjk8DI1jO80hDaNdhzCXgOGEYeHkLVZW_AstRnyuTLNZSEwVi13ApQkg33f2DgEd2aE20p71ZwbtEVJj2bKGtOO38bv9JG0xt3LhT5mR-2zdeIfiVEYsuTstFZUYoweDiONMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phldIq1Ucuin7jOyuyXLWxCXVQveggDf7q89LBG6BjLnMon-Bn251ueb_IrR_JFhO1JL9WdsncgyPSceERkYxt4MqHZFh7aluGbPm60H6kk2BjcpanNMgEe0AF6GN71sZSNqMdZoNe2u8KHE2tqDl9QYaCUlEL-qrFagl8KlFNZ-DbjzZFeW6QhD1LQtuegUrL-ljb857uZcWo1wHVHewoKSnBk7F_rEIvqJhVtSxPDA2u2effHW7lyx_FxCgLMSEVxnD1BfLDKbSaK1d8PczwyheBHwcwbpvhtjX3iIdnVhM10_xg8mytDJysZFwG8ar_YX7uk8xJmY13eMLso_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRjbzdVObOBd5bsr_xQXzMULAOk7fH8aa-JYrobogU6aeq_iqJEt9xgbO4MixybNlNIaP6WJ_nks0JMLhMTry7wT_sBdBN9D1hGI4hNVEUzLBwHq1ZVEmNb2iJ0GBHSWdbXFR7oHYV9gA_A82vzjXP-nYmNnfXoCTnPMHmuLv7_hPABnjupa-dM2a20vWY-oMbD1j0YOkbUOzecj-mYo18BtVEbZWcCpHHvLLFO0iYFsfPmHt163VpVHpEqDbKleEOLlrXtW_EwP1JVMYI_3eV7I2Soxv4xMhQ6RaRMTsTtqURorn-cPVK3JKDJVkNnt_7-Yl2hTexhTHz2cFJvE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8_wpUtRX8ezdb7X2cunomzlA6Om5xZGpa90mz3_7ZG_HOIIxbwbTKduFyc5x4_zDWmzrcajFOVfIAuP6dS4mN7M4ypEipyku-UNtRtfJjL7EpA7rjFyTyTTHgtPOssKbWG0F6Xe5IGfZFhVcXrzFjGUcTfSvMZWH_yJ_QFeX6g1dfwE_pzc2BvN1Mop_TYZwFvLOgv2doku9A7SiBWu8Cxc7J-Xme0o3E5XJtW9T_X8B-paHiQkEBCEeKcdTDwLZ3TnKTXXxwO2XWfPHnvnYltF_ffSR3uwQNTo3CSmml1o52rBk2a5LpiM_HxMwc-r-R4mT4Tisxy_WkfPrKd17A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5vzYChfIvq7avQSjgFAnubZChvIuPxipYmvoNJjwl8htBTTm08OzRdFyk_UAyOWhLTWsOeuySs2ypNFywwHGODiqyMPC8dt63GE5ArcLbCFwpHCW8AXYnszIyDE_OVaa1snExL9gc0jsAVVmcExkH1vZq5_XZIPoPhbXNKF36kOLEsncYYnR_Faei0oo8fggR6lgHIaeApLd9-5MZe2-JgSt6V-SYq79DT_nIzNVTE5mvYykpiB4MXc9LLeyK2H6r434ToXqzLSmHzRc64eTKkjbV2dMptZISOEH07Orqj8wTkm8R_uc2ArlIAMbwdhNQAAtyLprc2oxvAyVcTREA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استقلال با تک‌گل آسانی پیروز شد
⚽️
استقلال ۱ - ۰ پیکان @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/461353" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461352">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSqclQWu1ai1slHqhK7QZHjCQqp2W-XZYf2Ihe4WAi7yN-O6MMCJiR6mwcYaB_8AWJJ7W7SPmG2RNN4U_6svNs7ciia4V7ojpeoB8rIlCBX4KM5U3ZkuEMl2oLDZtDVe2y4EsxrPfXeTi-KJCq4UecLI72pu0EwGEkZK451ryzjRNRHLOPQGtN2wKbfg0yuLSAkkne5CHLcKF_hbgVl4RJ22YbWNzmim2L71vTGTEFeU20LJysurEIXQvxDOA3dKpl2xcXekoAPPNyf7z6fLS6yIf6INr2VaRPhYKpIkXUkUWdPvYvNJejdlfZIRpvAPqt2Fch-UFRFs8xZKQRpfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/461352" target="_blank">📅 09:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461351">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02784790ad.mp4?token=r6kzbVxORbizhI8Gw5hnDWi9qdIhj8IkC9E8axWD-4B0KHvWXt9ssT5wJNj1PC1bJMaaTRY-Vew1APkjjliFgLFO51Ep93DtzUs8WFEvT0o16s2uuXz7M2k8vK5KCkX32Zldsnpi6AcTn7Fs6CGf0uH78b6BTpjOApdUeyIssKdxciaii-bntTTRnEFBrH3AFd_4QN5RHVYRTJSPgByFvpBy3GRpkfoWLl1n1fXsNNNuFMf7nIHwCzp-X2u5hkb4fayCIO5FQzEs5Q-M7kE4f5RS7fYNPv4ypdFpI7OmJV3NQ7jNk-POlvK8vGIQgzrouRLWFQJ52CialQAqXJylIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02784790ad.mp4?token=r6kzbVxORbizhI8Gw5hnDWi9qdIhj8IkC9E8axWD-4B0KHvWXt9ssT5wJNj1PC1bJMaaTRY-Vew1APkjjliFgLFO51Ep93DtzUs8WFEvT0o16s2uuXz7M2k8vK5KCkX32Zldsnpi6AcTn7Fs6CGf0uH78b6BTpjOApdUeyIssKdxciaii-bntTTRnEFBrH3AFd_4QN5RHVYRTJSPgByFvpBy3GRpkfoWLl1n1fXsNNNuFMf7nIHwCzp-X2u5hkb4fayCIO5FQzEs5Q-M7kE4f5RS7fYNPv4ypdFpI7OmJV3NQ7jNk-POlvK8vGIQgzrouRLWFQJ52CialQAqXJylIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور به‌منظور شرکت در اجلاس بریکس عازم هند شد  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461351" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461350">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO7kaFMbvXFp11hKPNJ_P9P6NpdNlL0yEy2LXyThuaNpIXw_rin1e4ub6_2YPGX51tfTiv1-wawaBGSQ5XMo-wQAqDMV76WtJP25BquuyHOYlZaVDWK-utJNfSUrULbtGWNsX8dcj3v-pmf9m73YLn9DesB3rLnMrjIqbOkCifZNRDNWpSPkhRx2i15VaB3hHCIpTtyKGN9EY3ushu0qjF9zaMjVZLY-LH4S4GkLcI_7BL293CrEHg3ioYwJjo3ksvLA97O761qw5zF6ICJdHY3Gcz_n8QNveewxrg7Ki1y3aFiM2BjYeMvDalkqg4EHSE4UnRjbyi7jDlR1tgZLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش عراقچی به اعتراف مقام آمریکایی: بله ما ناوگان پنجم آمریکا در بحرین را با خاک یکسان کردیم
🔹
صراحت «هانگ کائو»، سرپرست وزارت نیروی دریایی آمریکا، جای تشکر دارد. او درست می‌گوید، نیروهای مسلح قدرتمند ما واقعاً «ستاد ناوگان پنجم آمریکا در بحرین را با خاک یکسان کردند»؛ همان‌ کاری که با دیگر پایگاه‌های پشتیبان تجاوز آمریکا هم انجام دادند. مردم آمریکا واقعا نباید هزینه جنگ‌های اسرائیل را بپردازند.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/461350" target="_blank">📅 08:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461349">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBv4jsVujM_0vzfAZZjCB56zwIoYA59qzPYsEmQtcc06ROHX5yhgorw5PBOkG-e2cEDJ1g3n74noVJq0h4HXLgnv6jDRWznobgaRKOpluAD7ABQ2LSXYiQGL-5DtRHsTL-gnEIaPKJYnCsc5I40q1aPZgug4xBm5TSHJDHIGH8yVyRNXmODMTmWVjp1c2MEim92Gr9OEfsTjm5gA0eDLT5Wfde6V7Kv5nMfED_tor3q-XfGQYNvvAgBBtPLHUNruU521FFyHo20KZC_Gr9zaC4LpAWR-TZJO5SfGmPRGKbYAXX3REQ1y1TMYwGHKfEbYiqZE01qU9ewYCrJZ2uwVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور به‌منظور شرکت در اجلاس بریکس عازم هند شد
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/461349" target="_blank">📅 08:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461348">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
شوخی ۱۸+ «شفرونی» و کنسرت «شادمهر» در تهران!
🔸
در فصل جدید «پشت صحنه» گپ‌وگفتی دوستانه داشتیم درباره خبرهای ترند روز؛ مثل کنسرت شادمهر عقیلی در تهران، شوخی جنسی و توقیف «شفرونی»، فحاشی خداداد عزیزی، قیمت بنزین و تنگه هرمز و...
🔗
نسخهٔ باکیفیت را در
یوتیوب
و
آپارات
ببینید
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/461348" target="_blank">📅 08:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461347">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مدیر جهاد کشاورزی ساری: بارش‌های سیل‌آسا حدودا ۳۷۹ میلیارد تومان به بخش کشاورزی شهرستان خسارت وارد کرده است.  عکس: مصطفی شانچی- روستای اسبوکلا ساری  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/461347" target="_blank">📅 07:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461346">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هوای تهران امروز هم «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۳، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/461346" target="_blank">📅 07:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461338">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7m8MeeV6UvyGr3j_l8SxlRrBAnIMGkS4I0ksBm_mwA9kg5TfBbtet5OBAKw9888FD4mpbQfqg1EqollPCSkzipEMDHYMuDBDIqWQQc6CgTY3T5lxy_bs9XMHyp2DA0PPcxJXmsL4Lg6KU5KIr6e2UtiBi_8Uddce3FmTDXdKzKKA45adiS8WxlG9ar_ER5ofUaekbgZ81u59fyit-N08WUKAkGf7rWZfVS9xafNFmut9Aub3H6g963PhcNv-Cqxk9JvcNqGnsTSP4-pLYJs8e4oGFw0YpWJw7HoUQ21WIQjLHkaOXjpO2_c9xLMdiYkg0GypMbzI1ssz5XBL0RyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBgVHkyyDwxkTCEVIKZgRzHSTf8IOMqQTEgsC1nHRz7oIRM_YJtRJQSovbPbKkRExZ7LQOeFf_kMQORXU50ne2bdX2G1BTmjjzvpNGLD4rjI2qtakLx2_vQerFCbvTrHSm3zp2WOXFceeTOYAgyyHCBQ9XpQLHoYc_gJsQASgEyASYJ9sSXXdoH3S8a4rkrg0bRlWn7zGywFzjSCmsp7vjgnLiDMTwBParl73WB1kmg9La03ipfHZoKSeJ8_kw15ldnACvaapN_KHYnCutyinY_MvX7OW25AN52qq1iMd5VYGR5BW5Cs4GO5esyKPYAQ5oU9Je2GG9BRPU31-XZ4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fthCOL7yOQ6HqU5jj7hZtg_ODU0XaJm1_hSQBCRgsfV2Y3ble4W1zW_rDDhcjxb1nLfzQLZDTBqXBvmKz4SNkcHabR9IMkLziXdi-6P2YDiIOdsZkm110NBai85UnvfT-SXLQqtHRIfk89Xs4S-iFoTmyROfDLhm2dE_s8-1qebzUCC0sBUaQ65iETDb_M5GK_VSj1UzRElgl_Rus7xKcTkJp_zJC21i917UHlkyaezbF1MBforIpYsujvF0xQF2PVWsYlm815Tt2dNLwelKs_B5H0Df_e5PmCgA2UMV2QCZ7p2I1FPycw21zkIQW6-6-A-JqWWZ_hR_qPghiQG9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAuk1iMi0jaHysqnMDdfQql1BT0A34qF8xe4Cg6Y2PFowR7iAib_p81W-oGly6uZN2i8bJDOzu9Z6ewi3jg82kCDn-rEVlv1dNBXYRZL7yC-lsJwQWxb6jSSH3K06eJccJzUidtrXnQRjizDZit7ymyVIDWRqxz6JhysnjKb-u0DMOSutd5Cc-3NdRSdKllE0Uz0xmudJh3Bo4UNHFuBKEmpGeUNx2wJRefCQQQclgl9lFnPRtIgOMTG9EMCPT0SulfNMWvBns2MjPeNuIiJ_HV26l0Bj2tnOx2baoY2gQSr1-Gdw0PFLhmGhO5enwjIEl0zbp9CwGSVHGthrLmS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWFqNmcBz0IeG_MU3RWCTwvQlnxif9bRUK8pRcmtG4qRN7MFav0px63fwlbO59knDHEMSc2Qo7Y7IMBfc2Nn0be4ET5rZpH6UHBoXGA_6lhzjw7i-IoUQdQ0SgWf48x9In6U8cArWM8jJj4l0M6O0BId6hkw7u6pK0Fzm_jIYEdBG6OEoIpiLJ03svjZ05tkSuFt3b4DIT4h1IxePr2AcMotycx5Cuj8e38nfcJ-VEjGnvrvtXwTqxp8pcVwZOAcqe15Pegel0lgIHvs1AZxILWWy8JfbuE6SGKa96lj6KREqFcYesWxu1woQPspa_PF2Vv7961nMfu5grlAF4595A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dF04f1hQSOaXLeRnxztKIupX_yImKk-NQKZqQbEYHjn8VjEjch5aj8hvaOdZv90ADrbk_VUD--3d-JgH9Bmqgs59TsrkFpJ5sx-tc7auUSwUYM9AhMOKjZxCUJSZBRTTiEdZV-T07UG_xVI2xzUcQwLcu8Q6V4L-_wMnv8sRP_lhHWi423WBBLpDJkesRUH79eRWOJ6wEZNnpu-tRQOfxTiG5j8EMAYM6dzIT4ruCEMzzRnyB_ODFf4Var6b4knQXSKYLa-QR5LSTULSj4PnqKKrD0y2nTMXacU-vvY0_ub1IMDNNxeBdQo4IlE_3oh9BM-eFYZ-eQwjwF6XGbkdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMqgJpVlND5k6J1-pu64nZX3fV-IwIdfv-dowWV-526Hbav3YEiEZH-QMO3mSf2UTWFbApdrmlgV00NWfYEPgxk9wGuqb_gUs9NbKMiNft-_55DcXOg1K88MBYtlGeqMC7Xz364B1l60cHxOFtCWaEICQ-lPQqeNiI8rjbzvFDX54uLcNkm3p8iPI6MudgZpYSmtTAKMc5GYVBo1T8QEeccXzQjSl-qItxfpeqBwYpH8RE32VvZHZuXrowyLiku4RppecqSAlZ8AnajQmitOvfmObeYU5qDSGj0vQRtHw70gDJnWTIBkgpEm1HEdb5NkdVuYHokGqzzuND9oMzR3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7CQ20SF-uLOExPyBXeFXGBfo4MQ-ph3YgE5OhxroG7zfRD6rSAz77JBob29xhK3yI-RAZXBtso-X2W8GmG__8ezAcb5F2Y5bxcCBvw2_HanT-dtNJGIllZJVdZWB66e4OQT7CXSYPNOqKHz-rqmP6_a7OpqXBpDMStgD22HTLTzneIuBbGGXSxTlWFcZ-kgYIc7FTOCSQm7aMjuBH65pz0DY5NFyXVodFrXjfJN4_SOBfACASdeWvDFhE5v6IjVQanBharrkbmetTbxDZObkSVKvLP4sN8FQbaSG0zi-Zvn6niddRzqUu51LpgCPJVrowD3kShp4EApRI5BqrbqSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
باغ‌وحش ارم؛ دریچه‌ای به حیات‌وحش در قلب پایتخت
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/461338" target="_blank">📅 07:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461337">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmaKzUjQ72JcY8xg8i2XI2xUQRUD-jecAB91goBWV_gP6QbOsQZVltVO_baF-zubn3trc1Y8RMI9xUsZla5i9o0061DLWtjb9pfFf4RY8yX7k6jxVtd9I1FdnctXKkNatXh6baKektyJK16pUV4lO7Yn19VmHHp-cJu598ZMxQo0XSk7XprjjJ8TzyJsBdeacPa9v6STtBZVY2DDeEE609tjJnrGQZPhVKKC_vpszKDN5ajRy7a8cp9INS8NkrykuQq8mRQwwg8lKcVtVv2P8l0yoxRr_lU0Bv138ojenJIHkleGmcei57Q-zsa-ebA20tU-HRmFW342P_oy-b5Ddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای آتلانتیک: خروج آمریکا از عراق، دستاورد مهمی برای ایران است
🔹
اندیشکده شورای آتلانتیک در گزارشی نوشت که حضور نظامی موسوم به «عملیات عزم راسخ» در عراق به روزهای پایانی خود رسیده است و قرار است آخرین نیروهای آمریکایی تا ۳۰ سپتامبر این کشور را ترک کنند؛ اقدامی که به بیش از دو دهه حضور نظامی آمریکا در عراق پایان خواهد داد.
🔹
در این گزارش آمده است خروج نیروهای آمریکایی از عراق یکی از خواسته‌های اصلی گروه‌های مقاومت و دولت این کشور را محقق می‌کند.
🔹
الینا ال. رومانوسکی، سفیر سابق آمریکا در عراق، نیز به این اندیشکده گفت: کاهش حضور آمریکا در منطقه طی نزدیک به پنج دهه، همواره یکی از اولویت‌های اصلی دکترین امنیتی ایران بوده است. با توجه به این پیشینه، پایان «عملیات عزم راسخ» را می‌توان دستاوردی مهم برای گروه‌های مقاومت و ایران دانست.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/461337" target="_blank">📅 06:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97223f187b.mp4?token=T1iBkJ-IrSujiYyrq3UsgZKSmdg-hC46S01MzxVjDC4NHWFvGDkASXpk40e9K8CLuNiZ_jd7MQEaUlg3iasktQAO0zyWI9V-2BdfBGGEJzQYMWoYcym7O6bR458avDCOqlbJ-PPpJ0CtU0pScmefoK8wikKth-mjTKn93A1RVvP9-P0sm15SW6otej_SO6iCX4l1w9W_KNOi0NXugTrvtazTV-JM_6FPoXISe2-ifNCjzkdmz7VMSYoBdidAkKTcI0cv_BiqNK9Js9NeGI7VN8gVNhmm0ydZLDMJSMvQWleCWGfWGKoELK6t1n2PZRvjuEm9ojnqIvqvbAaDzwHpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97223f187b.mp4?token=T1iBkJ-IrSujiYyrq3UsgZKSmdg-hC46S01MzxVjDC4NHWFvGDkASXpk40e9K8CLuNiZ_jd7MQEaUlg3iasktQAO0zyWI9V-2BdfBGGEJzQYMWoYcym7O6bR458avDCOqlbJ-PPpJ0CtU0pScmefoK8wikKth-mjTKn93A1RVvP9-P0sm15SW6otej_SO6iCX4l1w9W_KNOi0NXugTrvtazTV-JM_6FPoXISe2-ifNCjzkdmz7VMSYoBdidAkKTcI0cv_BiqNK9Js9NeGI7VN8gVNhmm0ydZLDMJSMvQWleCWGfWGKoELK6t1n2PZRvjuEm9ojnqIvqvbAaDzwHpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در خواستگاری دنبال اعتراف گناه نباشید
🎙
حجت‌الاسلام شجاعی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461336" target="_blank">📅 05:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ce2bba6b.mp4?token=sRVNzC9VktomEHQ5GPIHO1c6h0ob1qwzOJbdPxyuAPpz-bKLUXXJKIHk_P2KeOXd8MmPJb4Kco5_BfA2gJL492fMz_MQ1ii0qpJyoU5145gBKSYIiDxg3lGyE0XV_NgALAabuk2hJqjG7GV2hpT0k7PSof1DVEhZA2vGwvLdCmkNbVhkRdNIPGgAg1JLFFBlS3K0636xADiKAgMIJBksQhl32lPr4ifFMmqsQFdW69V6lKMy9ys_RbnbtI5tYv3hYPRD-VMLkTNr-Lce56yKBEt66HcMUAMtXKoW8C-r94duRgpdUeuGpcr5S-q82tjpYUqTYG18h6eLn4lW1RQY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ce2bba6b.mp4?token=sRVNzC9VktomEHQ5GPIHO1c6h0ob1qwzOJbdPxyuAPpz-bKLUXXJKIHk_P2KeOXd8MmPJb4Kco5_BfA2gJL492fMz_MQ1ii0qpJyoU5145gBKSYIiDxg3lGyE0XV_NgALAabuk2hJqjG7GV2hpT0k7PSof1DVEhZA2vGwvLdCmkNbVhkRdNIPGgAg1JLFFBlS3K0636xADiKAgMIJBksQhl32lPr4ifFMmqsQFdW69V6lKMy9ys_RbnbtI5tYv3hYPRD-VMLkTNr-Lce56yKBEt66HcMUAMtXKoW8C-r94duRgpdUeuGpcr5S-q82tjpYUqTYG18h6eLn4lW1RQY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری مزدوران سعودی و اماراتی در ورودی شهر عدن
🔹
صدها نفر از مزدوران سعودی که از مناطق درگیری با رزمندگان یمنی فرار کرده بودند، تلاش داشتند وارد شهر عدن شوند؛ اما شبه‌نظامیان استان‌های جنوبی (همسو با امارات) مانع ورود آن‌ها به شهر شدند.
🔹
در این میان منابع یمنی از درگیری شدید میان آن‌ها خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461335" target="_blank">📅 04:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqGGhhLQ1BBLqxfCDeE56317wI9HTgrm4Cj0BUVkYtX3LkSH4xorBj1iEXAIRxstOlvz95tgPoNy0k1xEw9wHUfWDtasHNmUxH5TFYDxhCe4DfEFfV2lN0UY7XvOyJXA2_dBDD8to_ZyvjV9Ebee0UdSxABkSJHH50HqvNIxy0jQ_j7AX6NdwbRamZy4_eGM-1ADyB9V0LP4p4f8zPBAULSQzlsx6hEppWCt13fN0ifMmfVSyXP0Ifun6xiyyq5Jos876XwFWl_xUfzO4fJa3A-fFbB7Clp6JIUD4YKRLQBpxlZUOWCROuHaTilmAp5_1Qm3OCTOaenuFlxIqiHI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توهمات ادامه‌دار ترامپ؛ ایرانی‌ها توان جنگیدن ندارند
🔹
در حالی که رسانه‌های آمریکایی از
نگرانی عمیق در کاخ سفید دربارۀ مقاومت بالای ایران نوشته‌اند
، ترامپ به سبک همیشگی خود بار دیگر تلاش کرد با بلوف‌زنی، حقیقت را وارونه جلوه داده و مدعی شود که ایرانی‌ها در وضعیت بدی قرار دارند.
🔹
او در مصاحبه با شبکۀ محبوب خود یعنی فاکس‌نیوز همچون روزهای گذشته ادعا کرد که جنگ علیه ایران بلافاصله پس از انتخابات میانه‌دوره‌ای در ماه نوامبر پایان خواهد یافت.
🔹
ترامپ مدعی شد که ایرانی‌ها به سختی به جنگ ادامه می‌دهند و در تنگنای شدیدی قرار دارند.
🔸
در این میان مجری از او پرسید چگونه است که موشک‌های ایران را نابود کرده‌ایم و آن‌ها همچنان شلیک می‌کنند؟ ترامپ نیز با دستپاچگی گفت آن‌ها همیشه مقداری موشک دارند، آن‌ها موشک‌های زیادی داشتند.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/461334" target="_blank">📅 03:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9Os6uZR7KRlYjyQemffROcMlY8TH1_eBoHJxwEnq3vPZJ1z-wAtztD7iWDwPey6DhE3Juh-e_cp2x1O4ZOiyJtdQxwQ7KuohzfryRf3Y8fCbxFPgUkiRXqnYmcaaxggKFM-VN3yJeMz7pWl_UZWyhfspimtWs-FhO_niXfqwCfor9howrIulaJyFAy3w4hlAnKMaIUr_k9Cs63SD7UURgD9LZzpi6B4D7at4IdzQ9FIizdd8mi8TOcyHovC_8MvLoP_Y9b74HMwANriCFnAXI-JHuWdZkHhHHFD4SFmg85uRxciaKROH7K0k8EG508538gzhcu40obJ_a7jCzAKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور موشک بالستیک چگونه کار می‌کند؟
🔹
موتورهای پیشران در موشک‌های بالستیک، قلب تپندۀ این سلاح‌ها هستند که وظیفۀ غلبه بر جاذبه و رسیدن به سرعت‌های مافوق صوت را برعهده دارند. این موتورها عمدتاً از دو نوع سوخت جامد و مایع استفاده می‌کنند. سوخت‌های جامد به دلیل پایداری بالا و قابلیت آماده‌باش سریع، در موشک‌های میان‌برد کاربرد دارند، در حالی که سوخت‌های مایع با چگالی انرژی بالاتر، برای پیمایش‌های طولانی‌تر و دقت بیشتر در موشک‌های قاره‌پیمایی استفاده می‌شوند.
🔹
فرآیند احتراق در این موتورها با دقت بسیار بالایی کنترل می‌شود تا فشار خروجی از نازل، نیروی پیشران لازم را فراهم کند. در موتورهای سوخت مایع، پمپ‌های توربو که با سرعت‌های بسیار بالا می‌چرخند، سوخت و اکسیدکننده را به محفظه احتراق تزریق می‌کنند. این فرآیند پیچیده باعث می‌شود که موشک بتواند در مراحل مختلف پرواز، تغییر شتاب و مسیر خود را با دقت میلی‌متری تنظیم کند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/461333" target="_blank">📅 03:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAINaEtby2GBlvBChyQQKSwsSeMXUdiHYali-rUhcQY-KfMD6P-mfuzuk0kfMF5xlhirg4QzIWHbVMlQLmORrkVUgnTHazwIaC8feiB3w-3I6QBZsLE8KoV_6CggddL69x3G8jZO0WbbJwSQUebHCtCO_eo_UICf7d0bFM3yB_GLp3Vo7X3rOmg7S87v3UxIbudM8I23EK4eSZ1Vs6qNLyLn3qF9EgKfBdnSHYbOi-QjtHgH4PH5OmOVwOt2gX15SSACCq2Gw9247vxLFpHtZs_jm0sXgSasyDBQtBbpKENwtcVF-ZEYrRHvEAe8mVFD7SHP0SmqPCMA4NgrYmht1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tylylhuZUcbtL9yAS8mFyZ4swV1T72ySGGa7DIgQHzEUFatng8Xl_aps3huKqrUUA0d-eN51Vq2S6IiF-Vb9dZVDAI-DqAgnJPkZdZYilkLULl_0pcHEmGVkesnZwiiyhtPAxJ2xIbbbnVuBDuLLjCjlM0pj-yarXNY_KLqd1nUen4SRsZRMtmB9I92OKi7whuJZL3O7hH51tgmVcqA73VF6PZqO7DTSlFwJ_9wt7rtMfhsDFKuaKLMcm4SNfBvn8gBqk4RnAAhppWQ_iqsUfoGZN780bK93Lp0RCgUikRHjl637GPD0CvmkNXeuuvG6cRNfkZYcoir6dhrNDbDgLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر جدید از اصابت دقیق موشک‌های ایرانی به پایگاه موفق السلطی
🔹
یک حساب کاربری اوسینت  با انتشار تصاویر تازه ماهوارۀ «سنتینل-۲» نوشت که نشانۀ دست‌کم ۴ نقطه اصابت موشک در پایگاه هوایی موفق‌السلطی اردن، پس از حملات موشکی ایران در روز سه‌شنبه، وجود دارد.
🔸
بر اساس این تصاویر، یک مسیر تاکسی‌رو و سه آشیانۀ هواپیما به‌طور مستقیم هدف اصابت قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/461331" target="_blank">📅 02:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461330">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FczKntjyMYCbk7ECx1kc2dFzHaY9kO3TXBrdw2i7iAJTjFbqPyfZcxxcfVslTFzivnLNyIF6iRTxU3os_u1Ftp8MKO26dwj6yEvSCFMdA3EC9xcnUW_yavnk3ksx65l07ocAkJTyYl3thXAzKmVhLFA8yWCZJ_4ZA2IUocx7Qh3Gzw1Jg_uk3waa5C3_ps74syJTzCn84wEg8ngo-3tspHkeorJ8j5TBMJzhJhxk_ivyaApophKk45VslQoT46UKnE6nI01HOBkHlqSVNKlUq-QXDO1AktqvIFg__iR3ivZ-SINfa5BTEp7AvH6AAOAs4UP4lFLMfeMzDjgECjejCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیۀ وزارت خارجه دربارۀ تحولات مرتبط با یمن
🔹
جمهوری اسلامی ایران بر موضع اصولی و ثابت خود مبنی بر لزوم احترام به استقلال، حاکمیت ملی و یکپارچگی سرزمینی یمن و خاتمۀ محاصرۀ غیرقانونی و غیرانسانی این کشور تاکید می‌کند.
🔹
بدون تردید امنیت و ثبات در غرب آسیا و منطقۀ دریای سرخ، بدون رعایت حقوق حقه و کرامت مردم بزرگ یمن حاصل نخواهد شد.
🔹
جمهوری اسلامی ایران ضمن تأکید بر ضرورت توجه به مصالح امت اسلامی، به‌ویژه در وضعیتی که منطقۀ غرب آسیا با شرارت ظلم و توسعه‌طلبی بی‌سابقۀ رژیم صهیونیستی با همدستی آمریکا مواجه است، یادآور می‌شود که حل مسائل مرتبط با یمن از طریق ادامۀ محاصره و یارکشی نظامی ممکن نیست.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/461330" target="_blank">📅 02:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461329">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎥
کنجی گزین و تا به قیامت مُقام کن...
🔸
غزلی از رهبر شهید انقلاب در نجوا با امام‌رضا علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/461329" target="_blank">📅 02:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461328">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974851bf5b.mp4?token=PU5zKkvXVcE7ey_F7s6QCVbmoWIHIbUhMbNY5GJ1abF14tklBUHFobz62kJQ4yabri_KfPXuXXGRyybczy6Jr_Wt2AJCUzBHe9BAVCLqIeRLoXChfVVBceZ-CWMqYi7wwdnZsrwLrdf-wsaDahcw7IeqAwHOx-ogLHyAg_ntop-VcPOduSiB5Vpuz6rd3D5eIwhihB4p8fMI1LlKSxdQEei62Kp0aVaMzDMJw6uCrglDu-VOjNMvv-Mprwrhxj7tf7iTJpvHtGYAtTY50pjbqdkAG8mu1t2AiVfPFa6uumaMzKd1NKHolfqUIzvRHtNofVoDQhDkWK_jq0p_YhS3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974851bf5b.mp4?token=PU5zKkvXVcE7ey_F7s6QCVbmoWIHIbUhMbNY5GJ1abF14tklBUHFobz62kJQ4yabri_KfPXuXXGRyybczy6Jr_Wt2AJCUzBHe9BAVCLqIeRLoXChfVVBceZ-CWMqYi7wwdnZsrwLrdf-wsaDahcw7IeqAwHOx-ogLHyAg_ntop-VcPOduSiB5Vpuz6rd3D5eIwhihB4p8fMI1LlKSxdQEei62Kp0aVaMzDMJw6uCrglDu-VOjNMvv-Mprwrhxj7tf7iTJpvHtGYAtTY50pjbqdkAG8mu1t2AiVfPFa6uumaMzKd1NKHolfqUIzvRHtNofVoDQhDkWK_jq0p_YhS3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غم شهادت شهید خامنه‌ای، هنوز با عراقی‌هاست
🔹
دلنوشتۀ بانوی بازدیدکننده از نمایشگاه بین‌المللی کتاب بغداد برای امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461328" target="_blank">📅 01:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461327">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9pBuW76WVHNz5dfnQjq5lLGDPWDZnPpNsHLf9HeHhF8lXHMt6eb4ukBtJIZGqHlSGLf8lQhQUmP_c34Mu5NL_Dwi-sITDMgeOzvIX8UTkyeDcoBDPeVCfvgGNMsNOdnCzmDtptumJfso9ZwKyDxBZilwmABURHbATjUcxRFM0BhReLG9nq5L6BVaKf7--iHxXhCY2pIKS0q9HmJFl1wgLG3pthvQAgA3ar4xKQY7QyOtLY0xFj6KD63aCnysRuRpiSV1zuRKW7zJUPMffQZqGYTPaYGg735bkHcKm9XHxQBzpK_CacSZ6FTCxsGFDe5tKPUjFwzFUuykLqWbi_8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی گسترده در مسیر خط لولۀ نفت عربستان
🔹
داده‌های ماهواره‌ای ستونی متراکم از دود سیاه بر فراز جنوب مدینه در عربستان سعودی را نشان می‌دهد و گزارش‌های منتشرشده با استناد به داده‌های ماهواره‌ای، از وقوع آتش‌سوزی گسترده در یکی از تأسیسات مرتبط با خط لولۀ نفت شرق-غرب عربستان حکایت دارد.
🔹
طبق گزارش‌ها، داده‌های ماهواره‌ای نشان می‌دهد شدت آتش‌سوزی در این منطقه برای چند ساعت به بیش از ۷۰ مگاوات توان تابشی رسیده است؛ سطحی که به گفتۀ تحلیلگران داده‌های ماهواره‌ای، می‌تواند با نشت قابل توجه نفت خام و آتش‌گرفتن آن تحت فشار بالا مرتبط باشد.
🔹
هرچند هنوز بیانیۀ رسمی از سوی ارتش و انصارالله یمن منتشر نشده است، اما برخی کاربران احتمال حملۀ موشکی از سمت یمن به این خط لولۀ راهبردی را بالا دانسته‌اند.
🔸
این خط لوله نفت خام را از منطقۀ بقیق در ساحل خلیج‌فارس به بندر ینبع در ساحل دریای سرخ منتقل می‌کند و یکی از مسیرهای مهم انتقال نفت عربستان برای دور زدن مسیر دریایی خلیج‌فارس و تنگۀهرمز محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/461327" target="_blank">📅 01:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ونس نظر بی‌پردۀ فرماندهان دربارۀ جنگ علیه ایران را جویا شد
🔹
روزنامۀ نیویورک‌تایمز گزارش داده جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در اقدامی غیرمعمول طی بهار و تابستان مستقیماً با فرماندهان نظامی آمریکا در خاورمیانه، اروپا و آسیا تماس گرفت و از آنها خواست ارزیابی‌های بی‌پردۀ خود را دربارۀ جنگ با ایران ارائه کنند.
🔹
به گفتۀ افرادی که با او گفت‌وگو کرده‌اند، ونس پس از برخی از این گفت‌وگوها، نگرانی‌های عمیقی دربارۀ راهبرد کلی و چشم‌انداز موفقیت در جنگ پیدا کرد.
🔹
این ارزیابی‌ها نشان داد که حکومت ایران تا چه اندازه از تاب‌آوری برای تحمل هزینه و فشار برخوردار است و همچنین مشخص کرد که ذخایر تسلیحات دفاعی آمریکا برای مقابله با حملات تلافی‌جویانۀ ایران محدود است.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/461325" target="_blank">📅 01:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461324">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برخی منابع عربی از حملۀ هوایی عربستان سعودی به بندر المخا در یمن خبر می‌دهند.
🔸
همچنین شلیک موشک توسط نیروهای یمنی به سمت تجمعات دشمن سعودی نیز گزارش شده است. @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/461324" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461323">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برخی منابع عربی از حملۀ هوایی عربستان سعودی به بندر المخا در یمن خبر می‌دهند.
🔸
همچنین شلیک موشک توسط نیروهای یمنی به سمت تجمعات دشمن سعودی نیز گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/461323" target="_blank">📅 01:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461322">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نگرانی آمریکا از مهندسی معکوس زهپاد خود توسط ایران
🔹
بعد از اقدام جمهوری اسلامی ایران در تصاحب یک فروند زیردریایی کنترل از راه دور آمریکایی، واشنگتن نگران مهندسی معکوس این فناوری پیشرفته خود شد.
🔹
خبرگزاری رویترز در این‌باره گزارش داد که ایران احتمالاً زیردریایی…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/461322" target="_blank">📅 00:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5869d8727f.mp4?token=ftqocHEun-XUae2v9l28WJzbYK5VDhxfBCiBc9bLy507VqGEshDWx1nuYgTsYpjmPeBIHcCSr-JHNKJfZS0JW7l2G53rECby6_9pSJYYwjqqySorD1BRVhKwpnaLQ9RehgefeSNZ1iC2NFRg126pFq3JwZNOpkS8vSz_1BbTSYuIvYkuzZ_opTtpiSv3khC76HcHSdrn1MPL4UWG9Xh-Ft7j-ngSsY_0aLNaibzT_keaKLV10uKcM2UQt1OjMsHuuXhlAAf3wloRJVjaUKPXr-a3w07WkG2ae3PTyNWllDD8FEZ9mL9QxBekV4TnGdqTqlpUIL21edtXkj_cYujtXkED4OtY12Zrj3v4QM6XBMHwxF640Fy9LUN83-cBjZgPWM13QlY76mc0W5n-RLIALye6nq4ihYIxe-URFRa_HHHx-xSyJeTfHi8XRzNH-PWY6ZPoMzDnvU_1x_6SBnf2U7VLecMT9lTzfvfANjhiXJLHy5uVFoQpFtZKtfMPs3KZ4dhy6f34mCuG1lbtazrRW_9gUPrUxLVEpoYoM-U-_73TWtddsR7o3d_kGkaVprHN5P1rZEdKJzPIqvZh7QLsyty09lwGaKGscnyyoKhYXAVCiT7z3gGh9qtifPY3Tje4TlZ5ALDVPVF2uytnnROmrOuQ0WYIxpMZN6al7QF7ULk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5869d8727f.mp4?token=ftqocHEun-XUae2v9l28WJzbYK5VDhxfBCiBc9bLy507VqGEshDWx1nuYgTsYpjmPeBIHcCSr-JHNKJfZS0JW7l2G53rECby6_9pSJYYwjqqySorD1BRVhKwpnaLQ9RehgefeSNZ1iC2NFRg126pFq3JwZNOpkS8vSz_1BbTSYuIvYkuzZ_opTtpiSv3khC76HcHSdrn1MPL4UWG9Xh-Ft7j-ngSsY_0aLNaibzT_keaKLV10uKcM2UQt1OjMsHuuXhlAAf3wloRJVjaUKPXr-a3w07WkG2ae3PTyNWllDD8FEZ9mL9QxBekV4TnGdqTqlpUIL21edtXkj_cYujtXkED4OtY12Zrj3v4QM6XBMHwxF640Fy9LUN83-cBjZgPWM13QlY76mc0W5n-RLIALye6nq4ihYIxe-URFRa_HHHx-xSyJeTfHi8XRzNH-PWY6ZPoMzDnvU_1x_6SBnf2U7VLecMT9lTzfvfANjhiXJLHy5uVFoQpFtZKtfMPs3KZ4dhy6f34mCuG1lbtazrRW_9gUPrUxLVEpoYoM-U-_73TWtddsR7o3d_kGkaVprHN5P1rZEdKJzPIqvZh7QLsyty09lwGaKGscnyyoKhYXAVCiT7z3gGh9qtifPY3Tje4TlZ5ALDVPVF2uytnnROmrOuQ0WYIxpMZN6al7QF7ULk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتهام بزرگ خداداد عزیزی: فدراسیون پول به‌روزرسانی VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند.
@Sportfars</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/461321" target="_blank">📅 00:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ذخایر راهبردی نفت آمریکا باز هم کم شد
🔹
درحالی‌که قیمت نفت امروز به مرز ۱۰۰ دلار  رسید، آمار جدید ذخایر راهبردی نفت آمریکا که لحظاتی پیش منتشر شد نشان می‌دهد که این ذخایر ۱.۲ میلیون بشکه دیگر کاهش یافته و به ۲۸۵ میلیون بشکه رسیده.
🔹
با بسته شدن تنگه هرمز،…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/461319" target="_blank">📅 00:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حادثه برای دو شناور در نزدیکی سواحل عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه‌ای برای دو شناور در نزدیکی سواحل عمان خبر داد.
🔹
بر اساس این گزارش، این حادثه در فاصلۀ حدود ۴ مایل دریایی غرب شهر خصب در عمان رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/461318" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461316">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9264531775.mp4?token=dluU27YPut71SXCbo_uL52jwoMqrtlgVt6stM5NAPCV9gQp15KCbLy5GW_rzoqOY8kQMnnM3KCk0_d6rTG2k5ga6kR4HXXscdtKTZdZWDu4ICXZrnaU-2fI-BRKbvVExenkVAwSqySQa8qy1tBqdyihAUox0boBf9W64tuC35NuitHW25lyd9SN014uUVM8CPF6g8-TnxbojE1CEetjCipPubSmTjSNOdQ2I5hS8XS3SDKVQI0of5dgjYbNPw0ynjrSpeoEqpE3koM7QSMhDa7WTuScEtTTrTP_iLaRMpWIStiaQMrTOAnL7wJ8Q4jNiEROrrkxTkPQHWE5pkochGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9264531775.mp4?token=dluU27YPut71SXCbo_uL52jwoMqrtlgVt6stM5NAPCV9gQp15KCbLy5GW_rzoqOY8kQMnnM3KCk0_d6rTG2k5ga6kR4HXXscdtKTZdZWDu4ICXZrnaU-2fI-BRKbvVExenkVAwSqySQa8qy1tBqdyihAUox0boBf9W64tuC35NuitHW25lyd9SN014uUVM8CPF6g8-TnxbojE1CEetjCipPubSmTjSNOdQ2I5hS8XS3SDKVQI0of5dgjYbNPw0ynjrSpeoEqpE3koM7QSMhDa7WTuScEtTTrTP_iLaRMpWIStiaQMrTOAnL7wJ8Q4jNiEROrrkxTkPQHWE5pkochGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امت مبعوث خستگی‌ناپذیر در شب ۱۹۴ هم حماسه‌آفرین شدند
@Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/461316" target="_blank">📅 23:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461311">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUP_V4wly0v6HVMO6xMm5RQ37T6mSEkVqsktaEZJZqCTKKH3pPaLLcKCoytobQMDvAkZaMEo-C4osWf0O0JR6Jr-rmubFhgobryNTXkUnwQnX_d-vx0NKXVRY2cOcIvEFB_ks4ztxlMHDbt53eVE943UXafvSFldvGkdpdydC7kW53Sba2qECV9Y1UPuQYn2sjpfu6tMIbzjJuqfNQM2vso5YBa84JWr5ngXLgEecfUVniRKy6Xihi9-my0wlh3nUAqijI9PrjU--YXbAofwLaKJ3kAUk6RaZ2VrAMJ0N1e1Jr_cq-yDP8Oibx0Vmlbg-nyZ1jAKPFmVIIj0_oD4sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AV1zPwG7O7ymqA_zO0REEF-0xVvEwsIp_1lQopZViRdJ2oZvZYsM7p6BI9L_27-Mizf5DBCuuJlsOIHVJUewzUBfc4hUninFvFjFLVg8zeDA8bUbJf3jIR4vDRTOkbaqCnOG0cKtKbLpDYSDqDl5XIU6NJDtisSLBR3tWn8jICVKnD5h2Ir7bxB4rFV8yrPfpLfbLzJ9EpaWgdF37Ka142-_mOnaAYN3Q8bSq1fEvEfmuC2F2uVSkeGjfTbMXQ0UVuTDptezgDPE2GYlNRycnJLTPe7Xq4G3BIDWj7gFixUueffznPDS5YV4N6CDKvf0ec7gRbi0Iu4ovrAzFzp06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBOHfsK3jFNG79YTVLxFysLmhH5toqqNTkiJIEnxQ1jbLjVtAemV7Zkh1Egbrpl-rox8tBvsMDlmxwDBu5HSCBkXkuYFUdoRJBU0H2RCASA9EF7wy8hgwxXwxUAeEUpLp63gOOzvt9sYTHeqQkkYSMWWUrfiBExjUh_rCzIcHAOnO9BSdnwmZEMWPgQgTUqRECOYODywyasQ8P3zbuAiZyuNf4JtIaRtXba7kFCvQgxEYFwMhrEUfAiDwMkJTfTpaGZ_V32gniksso0fBI0N2jVHT2xZnI0fRoRex74u_UE_7hHdpjZ2WrASmKNfeLex980SqAOYs182i9nvJo0ejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvxRmzx0UcrH2JHTSQ6kVDCsPYV7KL8K7l5SZgGfb5pwok99C8OI8LrRN9er5jNiGeMnQnsRtC11qX4yIJBTlyvEmhGtqM9-TPebXOb7_0E6x4wspcNUwTeSaEf74rCTsTt9eRp5ctVoc1jEvUE3raCbFuuRAsTl3x2EhETUaP0BSFLEC0QIKsHv3IlUqgAJIh-0MAPk4qnmi2SkMp4MJm-LpYjiOBuH2ErGiLzHS6_tRccugyfwLQ7Efu-rsfwPZGJh7PY6qzybo-ecCmoJldY4bmNHqHzcQaCbsZ9r1AlHy8EDfLQjPQXPOh7ziytuMILquOhMiBlU5HapgbAyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXBfFr88zCLPOZTWdVqH6X1GoJ0bndfCAoMoTZrLDbANrI5UAu2Vvw8KD34Da71bOEDwQgKKcqGrRnDWGustuOKGcn-C4Sy9KzLMNeWc9Ayh5TXrQMMIKqF9eHOQOxrzjWf9U2ieXUs4m83rFaB8EuIPJespSvo6RNrESY8symkMKJ5vlWTgRqMoKbKfAefU3JlXzG6DSkgYcBzhqZi3-Z6UcJq1lkyYdicqAnN2lvwAELsz3q4NXdoPu-O67aRDjldNCabf3fxRobgh7ln2d_hlXIjnFDtCN3Uoc60cXb5JwIthD3goG4mZujgX5aNutfm12vjpvw7LMW3uQVeXDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دریچه‌ای به حیات‌وحش در قلب پایتخت
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/461311" target="_blank">📅 23:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
ما
معلمان حق‌التدریس
با وجود اینکه خود آقای وزیر سال گذشته قول دادند
قرارداد معین
برای ما انجام شود، هنوز این وعده عملی نشده است. اکنون گفته می‌شود دیگر قرار نیست این کار انجام شود، چون نیاز آموزش‌وپرورش به‌تدریج برطرف شده است. زمانی که به ما نیاز داشتند می‌گفتند قراردادمان را درست می‌کنند اما حالا می‌گویند انجام نمی‌دهند. ما عمر و جوانی خود را پای این کار گذاشته‌ایم، اما اکنون هیچ امنیت شغلی نداریم و با حداقل حقوق مشغول به کار هستیم.
🔹
ایثارگران و فرزندان شهدا، فرزندان همین آب و خاک‌اند و شایسته نیست پس از سال‌ها خدمت، همچنان به‌عنوان راننده استیجاری بلاتکلیف باشند. متأسفانه رأی وحدت رویه مورخ ۱۴۰۳/۱۰/۱۱ موجب محرومیت جمعی از
ایثارگران
راننده از
تبدیل وضعیت
شده است. از مسئولان محترم تقاضا داریم برای رفع این بی‌عدالتی و تعیین تکلیف و تبدیل وضعیت این عزیزان اقدام کنند.
🔹
وضعیت
آسفالت ورودی اصلی شهر کرمان
، از بعد از بلوار حجاج تا کارخانه سیمان، بسیار نامناسب است و چهره خوبی به شهر نداده است. مسیر از پل شهید معافی تا پل نعل‌اسبی فرودگاه و همچنین محدوده بین دو دوربرگردان، پر از گودال و خرابی است و خودروها آسیب می‌بینند. لطفاً این موضوع را پیگیری کنید.
🔹
دو سال پیش از شرکت
فردا موتورز
یک دستگاه خودروی SX5 پیش‌خرید کردم و حدود ۶۰۰ میلیون تومان هم پرداخت کردم. قرار بود خودرو طی ۱۵۰ روز کاری و با پرداخت حدود ۱۵۰ میلیون تومان دیگر تحویل داده شود، اما اکنون دو سال گذشته و هنوز کسی پاسخ‌گو نیست. جالب‌تر اینکه وقتی پیگیری می‌کنیم طوری برخورد می‌شود که انگار
درخواست انجام تعهدات قراردادی
، توقع زیادی است! می‌گویند اگر ناراحت هستید، بعد از دو سال پولتان را پس بگیرید. سؤال اینجاست که چرا با وجود انجام نشدن تعهدات قبلی، همچنان پیش‌فروش خودرو ادامه دارد؟ لطفاً مسئولان و نهادهای مربوطه این موضوع را پیگیری و تعیین تکلیف کنند.
🔹
من یک راننده تاکسی هستم. امسال دولت در ابتدای سال
حق بیمه رانندگان
را بیش از ۹۰ درصد افزایش داد. از اول تیرماه نیز ۲۰ درصد دیگر به حق بیمه اضافه شد و طبق اطلاعات سایت تأمین اجتماعی، از ابتدای پاییز مجدداً ۲۵ درصد افزایش در نظر گرفته شده است. خواهش می‌کنم پیگیری کنید این میزان
افزایش حق بیمه
بر چه اساسی انجام می‌شود؛ آن هم در شرایطی که درآمد ما رانندگان به‌دلیل جنگ واقعاً کاهش پیدا کرده است.
🔹
لطفاً مشکلات ما کامیون‌داران را به گوش مسئولان برسانید. یک جفت لاستیک بارز به ۱۴۰ میلیون تومان و لاستیک چینی به ۱۷۰ میلیون تومان رسیده است. با این وضعیت کرایه و درآمد، چطور می‌توانیم یک جفت لاستیک بخریم؟ متأسفانه مسئولان توجهی به
مشکلات کامیون‌داران
ندارند.
🔹
ما ساکن شهر آباده هستیم. فرزندم در مدرسه هیئت‌امنایی تحصیل می‌کند. دیروز برای ثبت‌نام به مدرسه مراجعه کردیم که با درخواست شهریه ۱۰ میلیون تومانی مواجه شدیم. چرا شهریه باید نسبت به سال گذشته دو برابر شود؟ در حالی که سال گذشته هم مدارس آنلاین بود و شهریه را کامل پرداخت کردیم، اما نه برنامه خاصی داشتند و نه کلاس بیشتری نسبت به سایر مدارس برگزار شد. لطفاً
وضعیت شهریه مدارس هیئت‌امنایی
را پیگیری کنید و شرایط خانواده‌ها را در نظر بگیرید؛ مردم توان پرداخت این مبالغ را ندارند.
🔹
لطفاً از شهردار منطقه ۱۵ درباره وضعیت
وانت‌های میوه‌فروش در افسریه
پیگیری کنید. این وانت‌ها به‌صورت قارچ‌گونه در حال افزایش هستند و بیش از نیمی از خیابان‌های اصلی محل را اشغال کرده‌اند و باعث ترافیک شدید در افسریه شده‌اند.
🔹
در میان کارمندان دولت، قشر زحمتکش معلمان به‌شدت مظلوم واقع شده‌اند. بنده ۵ سال سابقه خدمت دارم و با حق مدیریت، کل فیش حقوقی‌ام ۲۸ میلیون تومان است که پس از کسر بیمه و سایر موارد، تنها ۲۲ میلیون تومان به حسابم واریز می‌شود؛ سؤال این است که معلمان با این وضعیت چگونه باید زندگی کنند؟
🔹
من از اهالی
روستای کردیان در شهرستان باخرز
، خراسان رضوی هستم. چند سال است که در فصل تابستان و پاییز با مشکل
کم‌آبی
مواجه هستیم.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/461310" target="_blank">📅 22:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آخرین وضعیت میدانی جبههٔ یمن
یک منبع اطلاعاتی آخرین وضعیت جبهه یمن را تشریح کرد:
🔸
۱. از شب گذشته تاکنون طی پیروزی‌های پیاپی انصارالله در ساحل غربی یمن، مناطق مهم حیث، خوقه، بخا و جزایر حنیش و زوقر به تصرف درآمده و آزاد شده‌اند.
🔸
۲. عصر امروز نیز مناطق ذباب، تنگهٔ باب‌المندب و جزایر استراتژیک میون تحت کنترل مقاومت قرار گرفت.
🔸
۳. هم‌اکنون کل ساحل غربی یمن تحت کنترل مقاومت است و مناطق تصرف‌شدهٔ ۲۴ ساعت گذشته به بیش از ۴۵۰۰ کیلومتر مربع رسیده است.
🔸
۴. شمار زیادی از مزدوران وابسته به عربستان به ویژه نیروهای طارق عفاش به هلاکت رسیده، اسیر شده یا متفرق شده‌اند.
🔸
۵. تنها از ظهر امروز تاکنون عربستان بيش از ۸۰ حملهٔ هوایی به مواضع انصارالله داشته است.
🔸
۶. مسیرهای کشتیرانی به‌طور کامل مسدود شده و قیمت جهانی نفت به‌شدت روندی صعودی گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461309" target="_blank">📅 22:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی و وزیر خارجۀ عربستان
🔹
عراقچی در تماس تلفنی با وزیر خارجۀ عربستان، دربارۀ آخرین تحولات منطقه گفت‌وگو کرد.
🔹
دو طرف با اشاره به تشدید تنش‌ها و افزایش ناامنی در منطقه، بر ادامه همکاری‌های دیپلماتیک برای جلوگیری از گسترش تنش‌ها و بازگشت…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461308" target="_blank">📅 22:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تلگراف: ایران برای نخستین بار موشک مجهز به حسگرهای اپتیکی را سمت ناوهای آمریکایی شلیک کرد
🔹
مقام‌های آمریکایی مدعی شده‌اند ایران روز چهارشنبه برای نخستین بار از موشک‌های جدید مجهز به
حسگرهای اپتیکی
در تلاش برای حمله به ناوهای جنگی آمریکا استفاده کرده است.
🔹
سپاه پاسداران در جریان حملات شبانه، موجی از حملات را علیه نیروهای آمریکایی در اردن و ۱۰ فروند شناور آمریکایی در نزدیکی تنگه هرمز انجام داد.
🔹
موشک‌های مجهز به
جستجوگرهای اپتیکی
با بهره‌گیری از دوربین‌ها و حسگرهای نوری، اهداف را با دقت بالا شناسایی و ردیابی کرده و به سمت آنها هدایت می‌شوند.
🔹
ایران اواخر سال گذشته میلادی از سامانه موشکی جدید خود رونمایی کرده و آن را
قاسم بصیر
نامیده بود؛ نوعی موشک بالستیک میان‌برد که به حسگرهای اپتیکی مجهز است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/461307" target="_blank">📅 22:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a8860a2f.mp4?token=AqmuCxOh1dluByPIvTemnoL4DZHNbVz_D01K6oHa5J-uQC4s1V_MqBdiUPcd1Fdb_MSbxSvsGBge-nMQ_6JoRox8NoOiMIu4NjiF-yxXurE_wBFTL9pKuG6Kg5o5t3FM_Y7weiJFzMgV_TrRPtpDCKCW34646avDa8uJ1iiJjfXscWTE0pyyfcKkDG8gjP_nfgjBpBcA4OwxEOK-4bPrzjL69M5oRUHIAuTxj1h3b07QogAZPGyPSMGPaWh1W9xa4RieAiJ_8oTUXJgCDqKNN_ScKAb1bPN42akHgrV47ijQQcD1rvrSI5qg3PsZUjmiuU8_TUkaG-GKaTC_nEy6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a8860a2f.mp4?token=AqmuCxOh1dluByPIvTemnoL4DZHNbVz_D01K6oHa5J-uQC4s1V_MqBdiUPcd1Fdb_MSbxSvsGBge-nMQ_6JoRox8NoOiMIu4NjiF-yxXurE_wBFTL9pKuG6Kg5o5t3FM_Y7weiJFzMgV_TrRPtpDCKCW34646avDa8uJ1iiJjfXscWTE0pyyfcKkDG8gjP_nfgjBpBcA4OwxEOK-4bPrzjL69M5oRUHIAuTxj1h3b07QogAZPGyPSMGPaWh1W9xa4RieAiJ_8oTUXJgCDqKNN_ScKAb1bPN42akHgrV47ijQQcD1rvrSI5qg3PsZUjmiuU8_TUkaG-GKaTC_nEy6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشای لغو عملیات ویژۀ آمریکا، در نتیجۀ حملات ایران به پایگاه مهمش در اردن  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/461306" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
ویدیویی دیگر از انفجار در ارتفاعات علی‌الطاهر لبنان
🔸
شبکۀ ۱۲ رژیم صهیونیستی: بیش از ۱۱۰۰ تُن مواد منفجره برای انفجار تونل‌های ارتفاعات «علی‌الطاهر» استفاده شده است. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/461305" target="_blank">📅 22:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی و وزیر خارجۀ عربستان
🔹
عراقچی در تماس تلفنی با وزیر خارجۀ عربستان، دربارۀ آخرین تحولات منطقه گفت‌وگو کرد.
🔹
دو طرف با اشاره به تشدید تنش‌ها و افزایش ناامنی در منطقه، بر ادامه همکاری‌های دیپلماتیک برای جلوگیری از گسترش تنش‌ها و بازگشت ثبات و امنیت به منطقه تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/461304" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
