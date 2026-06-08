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
<img src="https://cdn4.telesco.pe/file/t_lD_O9vtDOjG8xFisZ-Zi4gbfTCblaJ6Fi9AnO-jDVbp41P-ahX7ZFCsWHxa6SPcq5eFQ0FIuoMfQ_9okzyTw0KdM6NLJvLNExhWVmVR-wFeEg1bqiQoy8FlkQTFFnvDTJZs5tcJeGY8VRQ3w2g06yJ0N52qeukL4eUXIZhTD6XoawNCGJKfxPPt6cY3ipeGSn_2QOCVeXUbTSWWVv9TmfD7l5MueIsGGt2AFoGHN0M_c2Pf4s8kBVU9aXRGVqBMlEp0u7jrycyDhrkDP74WtsSSbZAD3Y2_PFnub2SneWrvF3Eu1XgURznkpVByGaP8RCnF6D6tgDVW_AivWz5QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-126361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قالیباف: هدف ما پایان جنگ و ایجاد امنیت پایدار است و نه عادی سازی روابط با آمریکا و اعتمادی هم به طرف مقابل نداریم. البته روش ما احساسی عملیات کردن یا صرفا اعلام حقوق ملت ایران یا محکوم کردن جنایات دشمن نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/126361" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
قالیباف: دست نیروهای مسلح برای اقدام همواره باز بوده و بر اساس تدبیر و برنامه ریزی درست و تصمیم تصویب شده عمل می کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/126360" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
قالیباف: قرار نیست یا جنگ کنیم و یا مذاکره بلکه قرار است به وقت خود جنگ کنیم و به وقت خود مذاکره کنیم و اینگونه است که می توانیم دشمن را شکست دهیم و این که می گوییم مذاکره ادامه مبارزه است عینیت پیدا کند.
🔴
لازم است روی یک برداشت غلط خط بطلان بکشم، برخلاف تصور برخی که فکر می کنند بین مسئولان هماهنگی نیست، هماهنگی کامل برای رسیدن به اهداف میان مسئولان وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/alonews/126359" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
قالیباف: ماجرای لبنان نشان می دهد میدان دیپلماسی کنار میدان نظامی می تواند اسرائیل و دشمنان را کنار بزند.
🔴
نه دیپلماسی مانع عملیات نظامی است و نه عملیات نظامی مانع دیپلماسی است.
یک بار با تهدید به حمله و قطع مذاکره جلوی حمله اسرائیل به بیروت را می گیریم و بار دیگر با حمله نشان می دهیم ترسی از قطع مذاکرات نداریم و نتیجه این می شود که آنها مجبور می شوند عقب نشینی کنند و ما حق خود را تثبیت می کنیم.
🔴
تصور کنید اگر ما در میدان نظامی پیروز نشده بودیم یا در میدان دیپلماسی جلو نرفته بودیم و یا میدان های نظامی و دیپلماسی با یکدیگر به درستی پاسکاری نکرده و پشتیبانِ هم نبودند و با هم هماهنگی نداشتند، آن وقت دست ما برای حمایت از لبنان و مقابله با محاصره دریایی بسته بود.
🔴
موضوع فقط لبنان نیست بلکه موضوع رسیدن به حق مردم و ایجاد امنیت باثبات برای کشور است و باید هر ۴ میدان در کنار هم و هماهنگ با یکدیگر این اهداف را تأمین کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/126358" target="_blank">📅 21:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cb167517.mp4?token=t2PGJkQGs57SdS3rTMA7f83nJ_c8aVoP67eyhqjwh4tWP42eNkv4GT9mt_HSFYcBTA4iiS0Ey_BKAPvD5jjKkjsftBXfJWe5OgHkv5-tgetbobpzMuRK78dYGwJPeOmqt8kpcFN3_fYfnDRv12K2kueKne3XYscFOcLK0JOn3EAd4QIi_bQtiZliL4Am7WVKhYSpfP-h-j_ZeP1tH9kyvOLN5GfOS64rdGZiMOvyDQxWEVr-TQlb3K5siEzE2FDL4EQUZUPDsb0K1bHCGpSnRgz3nujNgXFHIM_ecnkiP-fT9ntF92-P5uIP9rU-tXZdFjCzwoyZr9Mcx6BMBNnY1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cb167517.mp4?token=t2PGJkQGs57SdS3rTMA7f83nJ_c8aVoP67eyhqjwh4tWP42eNkv4GT9mt_HSFYcBTA4iiS0Ey_BKAPvD5jjKkjsftBXfJWe5OgHkv5-tgetbobpzMuRK78dYGwJPeOmqt8kpcFN3_fYfnDRv12K2kueKne3XYscFOcLK0JOn3EAd4QIi_bQtiZliL4Am7WVKhYSpfP-h-j_ZeP1tH9kyvOLN5GfOS64rdGZiMOvyDQxWEVr-TQlb3K5siEzE2FDL4EQUZUPDsb0K1bHCGpSnRgz3nujNgXFHIM_ecnkiP-fT9ntF92-P5uIP9rU-tXZdFjCzwoyZr9Mcx6BMBNnY1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیرو های نظامی ایران خطاب به ترامپ:
عمو ترامپ با توئیت که نمیشه جنگ کرد، این ارتش و ناو و جنگنده‌هاتو بفرست خسته شدیم دیگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/126357" target="_blank">📅 21:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کانال ۱۳ تلویزیون اسرائیل به نقل از یک منبع: نتانیاهو به وزرا اطلاع داده است که انتظار می‌رود اسرائیل به چندین دور از تشدید تنش با ایران بازگردد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/126356" target="_blank">📅 21:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
عراقچی: همسایگان ما در اولویت ما هستند
🔴
صمیمانه‌ترین تبریکات خود را به جناب آقای نیکول پاشینیان، نخست وزیر ارمنستان، بابت پیروزی حزبشان در انتخابات ابراز می‌داریم.
🔴
خوشحالیم که فرصت خوبی برای استمرار همکاری های سازنده در راستای تقویت روند پویای حاکم بر روابط ایران و ارمنستان فراهم شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/126355" target="_blank">📅 21:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قالیباف: صحبت های رئیس جمهور آمریکا درباره یادداشت تفاهم، مخالف بخش های توافق شده بود که نشان داد آنها نه دنبال آتش بس هستند و نه دنبال گفت وگو و باید برای دفاع از حقوق ملت ایران پاسخ قاطع می دادیم که به لطف الهی نیروهای مسلح ما با اقتدار به وظیفه خود عمل کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/126354" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
قالیباف: آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/126353" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دونالد ترامپ مدعی شد که پنج کشور منطقه که در میانجی‌گری میان آمریکا و ایران نقش دارند، از او خواسته‌اند تا بر بنیامین نتانیاهو، نخست‌وزیر اسرائیل فشار آورد تا حملات را متوقف کرده و به سمت توافق حرکت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/126352" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به کانال ۱۴ گفت که: بازگشت به درگیری شدید با رژیم ایران «فقط مسئله‌ای در کوتاه‌مدت است، احتمالاً در روزهای آینده».
🔴
وضعیت هشدار بالا تا اطلاع ثانوی، هم از نظر دفاعی و هم تهاجمی، حفظ می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/126351" target="_blank">📅 20:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: فکر میکنم ایران مایل به امضای توافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/126350" target="_blank">📅 20:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
حداقل ۳۲ نفر کشته شدند و بیش از ۱۰۰ نفر زخمی شدند در نتیجه زلزله قدرتمند با بزرگای ۷.۸ ریشتری که در سواحل مینداناو در جنوب فیلیپین رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/126349" target="_blank">📅 20:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
🔴
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/126348" target="_blank">📅 20:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
🔴
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
🔴
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
🔴
من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/126347" target="_blank">📅 20:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
برخی کاربران مدعی شده‌اند که دارایی‌شان در چند صرافی رمزارز خارجی، به بهانه تحریم و بدون هشدار قبلی مسدود شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/126346" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی سیاسی جنبش حماس مدعی شد ایران به این جنبش اطلاع داده که در حال انجام تلاش‌ های فشرده برای گنجاندن غزه در چارچوب یک آتش‌ بس منطقه‌ ای میان ایران و ایالات متحده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/126345" target="_blank">📅 20:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNotOb40_KGfOJSNRZxB8FMaRVLstjC1FcjVDnDdbaCQYYY4kGXfC3RrhfOgtbzb3x7f2LN7YpLijS-z2LhGgKU2zpp5k_RFK3Q7KulZn_Fe84ZgRe-97v-auh7EE7SU2ZyGtwnwIrSgX7eAT5Ro-HKAySqDmvSJDngbI7IQ9xedlcUmH5liv2cUqD0KOfaarbETBVkZMdkM5OPDRTOo-V9nZkecf0cMM0HrPHpp21D3348hJD0IyYVvGD04SqjU42tYOHl6ZTTcEF7pk9P0cg2Xn0QdOraWJGPecqIoN9JGRWr7rJX0QhVDYZN6-aiRWiTJgkvBf5ZZgmjj-XQcXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت‌های عجیب هارد اکسترنال!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/126344" target="_blank">📅 20:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd75eece7.mp4?token=Uut2GjXT0KngE5_7Lfeq7OoX3P6OUomPiK-HNxfvz_z8kA_9tB1eyXfZxspQiBRluD8__tV18ZAeyitNOL1bZ0IOrTch8v9bMnniqa2_1FERh1l5MO6pNKAJ7Be9f3Vp2LcCv8n1Psa9SEgist7wwTUu3UtHrqiaAnWaKvntpubuIPPCWkdg7jkA1CON7B0i24M_jhFbgHEpqWqiZ9jHPEYexGeQ8M0z1aqxvgQA5UtQuE_TTlCsxAo9aNJ-17MjB8yqVd8MqizBiHa6fTxpIho_BHvvkObG5_yQJRcfeOjKckdj63XDmCAMo39h9Kp97L1-21rj1_tIFzAUVOV8yYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd75eece7.mp4?token=Uut2GjXT0KngE5_7Lfeq7OoX3P6OUomPiK-HNxfvz_z8kA_9tB1eyXfZxspQiBRluD8__tV18ZAeyitNOL1bZ0IOrTch8v9bMnniqa2_1FERh1l5MO6pNKAJ7Be9f3Vp2LcCv8n1Psa9SEgist7wwTUu3UtHrqiaAnWaKvntpubuIPPCWkdg7jkA1CON7B0i24M_jhFbgHEpqWqiZ9jHPEYexGeQ8M0z1aqxvgQA5UtQuE_TTlCsxAo9aNJ-17MjB8yqVd8MqizBiHa6fTxpIho_BHvvkObG5_yQJRcfeOjKckdj63XDmCAMo39h9Kp97L1-21rj1_tIFzAUVOV8yYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل چند لحظه پیش ارتفاعات ملکخ در جنوب لبنان را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/126343" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
روسیه از شهروندان خود خواست به اسرائیل سفر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/126342" target="_blank">📅 20:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126340">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4242e53622.mp4?token=V8tLXHQsIEw5q2mGdVeGj9-OyIqtYn5Ut8PGbZU6Od_qwK-urbYeNJZStTblX2RW4QBSEwUIcEfeIPh3NWTdmWL_jITvS9GfvjPfw23b6HO6eoJFa1VNTH_mtJ-U0v79WB3TURQJehgcvMME7-VGn6zcsdhlMWdnYw1tUWmt2VQGJ29iebplDXnZ26LiT99iC-MspccME3Y2Vxlkl33cdt-w6LsuVB2kLRDjSoWzbSlVhWjgDqCtB0ctm6x82hDHqmZ0QYhpwiC4dlQCESineEWQwgDyggiD1hmxQKkI-kMWlxSYN4lkoleAnwu6gOYyCgr8GGBQhu7dqXS3xKXD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4242e53622.mp4?token=V8tLXHQsIEw5q2mGdVeGj9-OyIqtYn5Ut8PGbZU6Od_qwK-urbYeNJZStTblX2RW4QBSEwUIcEfeIPh3NWTdmWL_jITvS9GfvjPfw23b6HO6eoJFa1VNTH_mtJ-U0v79WB3TURQJehgcvMME7-VGn6zcsdhlMWdnYw1tUWmt2VQGJ29iebplDXnZ26LiT99iC-MspccME3Y2Vxlkl33cdt-w6LsuVB2kLRDjSoWzbSlVhWjgDqCtB0ctm6x82hDHqmZ0QYhpwiC4dlQCESineEWQwgDyggiD1hmxQKkI-kMWlxSYN4lkoleAnwu6gOYyCgr8GGBQhu7dqXS3xKXD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیستم پدافندی اوکراین پهپاد انتحاری روسیه رو مهندم میکنه، حین سقوط مستقیم میره میخوره تو یه ایستگاه اتوبوس
🔴
دو کشته و ۱۲ زخمی گزارش شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/126340" target="_blank">📅 20:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126339">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9417287cba.mp4?token=TCbR-_c40GUQAyt6Oq0Yf88t_z3aOcZNaP6Dn8vBd1YhjxmJUbGsAfPNbws0WDBknqQAH_hAUJE5L1IvQGHNTR92kWRNHjGKm2CgcrKCamokknWedArtLRafIer2KTB8gkV3K63Wvj715biTaKwPlUZzEV9gjogCDkelzLj-heAPKuddWGPjsInK3Ark0VUG0hsvWkpgGKNKQzFY-pdHL9xNHIm7M3Fj2b7fqyOX2jgpqk1I_Zy8zJkX4K1_JjfJTrRHTnumJ-KIx-rJPb2YL9VlEtRYBRfjxYDP98yXoq-Pd-bkRcEkXfxN2ybMpchxrpcFUMf38iCjfDzEPiBIBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9417287cba.mp4?token=TCbR-_c40GUQAyt6Oq0Yf88t_z3aOcZNaP6Dn8vBd1YhjxmJUbGsAfPNbws0WDBknqQAH_hAUJE5L1IvQGHNTR92kWRNHjGKm2CgcrKCamokknWedArtLRafIer2KTB8gkV3K63Wvj715biTaKwPlUZzEV9gjogCDkelzLj-heAPKuddWGPjsInK3Ark0VUG0hsvWkpgGKNKQzFY-pdHL9xNHIm7M3Fj2b7fqyOX2jgpqk1I_Zy8zJkX4K1_JjfJTrRHTnumJ-KIx-rJPb2YL9VlEtRYBRfjxYDP98yXoq-Pd-bkRcEkXfxN2ybMpchxrpcFUMf38iCjfDzEPiBIBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب الله تصاویری را منتشر کرد که نشان می دهد جنگنده های آنها یک تانک مرکاوا را در مجاورت قلعه بوفورت در جنوب لبنان در 4 ژوئن با استفاده از یک موشک هدایت شونده هدف قرار می دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/126339" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126338">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزارت خارجه ایالات متحده فروش احتمالی ۱.۹۸ میلیارد دلار سلاح به کویت برای سیستم‌های ضد پهپاد و تجهیزات مرتبط را تایید کرده است.
🔴
این بسته شامل پلتفرم‌های ضد پهپاد رودرانر و آنویل، جعبه‌های پرتاب، سیستم‌های فرماندهی و کنترل لاتیس، برج‌های نگهبانی برد بلند و دریایی، سیستم‌های جنگ الکترونیک پالسار، مراکز عملیات تاکتیکی، به همراه خدمات پشتیبانی و آموزش مرتبط است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/126338" target="_blank">📅 20:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام آمریکایی: نیروهای آمریکایی به رهگیری موشک‌های شلیک شده توسط ایران به اسرائیل کمک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/126337" target="_blank">📅 20:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126336">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گروسی در پاسخ به سوالی درباره ۱۷ حمله به تاسیسات اتمی ایران: من در این باره چیزی برای گفتن ندارم.
🔴
نماینده ایران حق دارد اعتراض کند اما من با آن‌ها موافق نیستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/126336" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126335">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
آی۲۴ نیوز عبری: هدف حمله اسرائیل به پتروشیمی کارون در ماهشهر، مختل کردن عملیات و توقف تولید این مجموعه بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/126335" target="_blank">📅 20:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سنتکام: یک نفتکش مرتبط با ایران را متوقف کردیم
🔴
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی در ۸ ژوئن یک نفتکش خالی را در خلیج عمان، پس از آنکه این کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، محاصره مداوم علیه ایران را نقض کرد، از کار انداختند.
🔴
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچم پالائو را هنگام عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران از کار انداخت.
🔴
یک فروند جنگنده F/A-18 Super Hornet از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از آنکه خدمه از دستورالعمل‌های نیروهای آمریکایی پیروی نکردند، یک مهمات دقیق به سمت فضای مهندسی و هدایت کشتی شلیک کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/126334" target="_blank">📅 20:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رادیو اسرائیل: ارتش اسرائیل در ساعات اخیر در حال آماده‌سازی موج بزرگی از حملات هوایی علیه ایران بود، با ده‌ها جنگنده نیروی هوایی که قرار بود به اهدافی در سراسر کشور حمله کنند
🔴
با این حال، این عملیات گسترده در نهایت انجام نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/126333" target="_blank">📅 19:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc8KtAkfwC2P4CieC_8vGJCcfuoob-2r3pGGePO58zEIEJPuDijh9-5T7Qi00N_L1VtbcSeL8Qx1ZIOd5iKf3m_2OwVsObJBS4KJhPqMR3i34wRHulAVZyuqnea9uztYlD67jJCr7znf_fx4r25UYzL7fYtKw_-VnRO9kanyVQ0EEbTtvc2SRsr8DPDXyiUqKuerVXptCz0UP6qUH3_VMrWULSGngBTBznQVJgmFwikDZJY_BSSRQO9G27MM1OE5UovGenk_lv4DbLzJROky8S6_ZkWNc38L-NGxwHwvAxsfknOk5e7KHkk-tNZH2nN4MEBJoLzagfn8ModpUO9jtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک این از جنگ هم بدتر بود
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/126332" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bone7TV1nFZaviRGwRmRVrtNzezSXMh2IZfyCqkohYFgtqdKlDfOaJUgEMc4tNFvx5enzl8lNFD4BHOeXBCWVzrbFJEgTt4OuIF_6lkim6TBxolEkNQi73cIdxsSX2J7e1PMoTDDKJws8qC7X3DuYsyHlGftXTlHbqWhEQ_HVhX9XRxf_3TAVvmQdIbkcaa0aQ36t40Zux5zw-Oa5-Z7d7YXjbXQYd2yyMqQy8McqIuLJK0qnyknz9oP-vOCQzC_Hc_eVNkAqeJ5pf-dDiAmwaVwfp_UZM8cdUyr5xJwOJz9_YStYcqPlox6VU0pbpLYaFvtgnrykA3uN-YKh4VeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/126331" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4446250ba8.mp4?token=LQ8HFVBE93Rn8kogGuF6g5rvfehhf8gu6tbh6TiuvaU9w0aZR5_RcE-97XxxhaR6XtEG_qJqi0MknPDXyohGsN3vL_Wh9xzu6wvBCbsaRZwxBjEeTSb-4WCgMpm9rMYCLHaRXH3KZ2L0TVhg6WcCufJLZDm5gy4z3314boyhvbInDudv2gZC7GCoNJ_Ot7i3HoHwAms8QekI4A4zejD6Zfg3BP-tUGMxUL0mwpb-aEfzf74li5sZArEG6pnRu8kwOAb9qt7UELAV6_ebnDsGw6H6wa1p0816v-CZf4UID79n07z_TIhYPSBt16RLB1J3VnRG9Jd0iCgTJP1NBxQ1CIeG47YZ7z2hHhF9HN14UsSKchct1wuw-CMzCI-hcOeNlmyCAFsYX4l6eIxIc24r89SDQmFPKaxmaC8KO07S-B9SA9f6ZyAGP683C5NxU8rfafI1Tw1bah4JSKPQ5QMFpsD1MhsvcDBss8wkEwvWKMJ6rBbFjDcpPFwCyH_qLbEY4lWlGy0qDdMvrL_-6fQZ-blLYkXyl41QzzbaAe3X4HfvbKN5SfmrJHjnEnvEPBf519TBmOFcU6WICCMpwQDLPiRXVJZ5S0iSSIiRAi6cQi489ZwGycF13J2zqvqYKAQKKsHo-ukap70VQ86q_2zcLsGqPP_7F4HpNjAvK2UZFnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4446250ba8.mp4?token=LQ8HFVBE93Rn8kogGuF6g5rvfehhf8gu6tbh6TiuvaU9w0aZR5_RcE-97XxxhaR6XtEG_qJqi0MknPDXyohGsN3vL_Wh9xzu6wvBCbsaRZwxBjEeTSb-4WCgMpm9rMYCLHaRXH3KZ2L0TVhg6WcCufJLZDm5gy4z3314boyhvbInDudv2gZC7GCoNJ_Ot7i3HoHwAms8QekI4A4zejD6Zfg3BP-tUGMxUL0mwpb-aEfzf74li5sZArEG6pnRu8kwOAb9qt7UELAV6_ebnDsGw6H6wa1p0816v-CZf4UID79n07z_TIhYPSBt16RLB1J3VnRG9Jd0iCgTJP1NBxQ1CIeG47YZ7z2hHhF9HN14UsSKchct1wuw-CMzCI-hcOeNlmyCAFsYX4l6eIxIc24r89SDQmFPKaxmaC8KO07S-B9SA9f6ZyAGP683C5NxU8rfafI1Tw1bah4JSKPQ5QMFpsD1MhsvcDBss8wkEwvWKMJ6rBbFjDcpPFwCyH_qLbEY4lWlGy0qDdMvrL_-6fQZ-blLYkXyl41QzzbaAe3X4HfvbKN5SfmrJHjnEnvEPBf519TBmOFcU6WICCMpwQDLPiRXVJZ5S0iSSIiRAi6cQi489ZwGycF13J2zqvqYKAQKKsHo-ukap70VQ86q_2zcLsGqPP_7F4HpNjAvK2UZFnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان با دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، در استانبول دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/126330" target="_blank">📅 19:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
تایمز اسرائیل: اسراییل اکنون در تلاش است تا جنوب لبنان را از توافق آتش‌بس حذف کند و با تهدید موشکی علیه بیروت، حزب‌الله را به توقف حملات به شمال اسرائیل وادار سازد، معادله‌ای که با مخالفت قاطع حزب‌الله لبنان مواجه شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126329" target="_blank">📅 19:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزارت دفاع عربستان سعودی اعلام کرد که یک موشک بالستیک که صبح زود از یمن شلیک شد، دچار نقص فنی شد، از مسیر برنامه‌ریزی شده منحرف گردید و در نهایت در منطقه‌ای غیرمسکونی نزدیک مرز عربستان و یمن سقوط کرد.
🔴
این موشک توسط حوثی‌ها (انصارالله) شلیک شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126328" target="_blank">📅 19:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
آی۲۴ نیوز عبری: هدف حمله اسرائیل به پتروشیمی کارون در ماهشهر، مختل کردن عملیات و توقف تولید این مجموعه بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126327" target="_blank">📅 19:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126326">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
دستور بازگشت فضای هوایی کشور به شرایط عادی داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126326" target="_blank">📅 19:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: حملات موشکی ما تا برقراری آتش‌بس در لبنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126325" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTaE04E5eE0d5p7yj3taT_h0m9Fkmyq3QyjUI6Mh-UFEePEtUSPVX-LjNKEUeFS4TgNqBi1frBq_oNqXzZL8QExe58F_Ou5kXtG9pBl_tx9alxKHIHnlp0WFOa5uP-0tPsIplcEpfIe0pTuhU9g7ubNyjzzGKP17pQgnn5i_n_ZfOnaQfMjLyGlZ8c1qHBnlH5TugjLiCflNhmbW4KamAJdDsIVcwZ0e8i2MFmHcQj0epuzfFcKuqkQO5ry36V1Uh1to3FHlPGAN0u4pekt1RrAtx9jwBIf2pag-jX_RnoT77oazaqc0gwpkXkbSF7yrmMDjJ4r2T4Mp1xQWEsHHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترور هدفمند در صور، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126324" target="_blank">📅 19:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نتانیاهو: اکنون در جبههٔ ایران آتش‌بس برقرار شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126323" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvqCphaaxITCesqNFS1xJ6YgzXU63O5gH21d2fMGnVwCsWWf2RM6lNvYd9JrUjV8bYLhqqhYR5SbxRJCoLA038w4GGw9Opa1P6d5siSfpPh4ui7Wb8kRXVrcOTfDTVBOj9yXKCnNPv4c-Sc6J1lr9bR-BfRMi-95O90z6RQ4vLCWQPyp3-UiT1NVMrQODRhrCa3WCV-XKuhvbtVGd-GyWDoREfsJnXlhtYDo79BMV3ufv3A4TpHstvK5iK9EDtNiDO0p2QL8i3JI-JkgLjnTWkXWxHsbY-Ed00ltcBPzuimjVNpKc-6xjv0JXmKDJezZB6QsZykCGlDZziu6hSM3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل به ساکنان منطقه زوقاق المفدحی تو شهر صور هشدار داده تخلیه کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126322" target="_blank">📅 19:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126321">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نتانیاهو:همانطور که به دوست خود، رئیس‌جمهور ترامپ می‌گویم: ما اسرائیل را با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت را به شمال اسرائیل بازخواهیم گرداند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126321" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: وضعیت حومه جنوبی بیروت همانند وضعیت شهرک‌های شمال اسرائیل است.
🔴
هر حمله‌ای به شهرک‌های شمال اسرائیل با حمله به حومه جنوبی پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126320" target="_blank">📅 19:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نتانیاهو: فعلاً از حمله به ایران خودداری می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126319" target="_blank">📅 19:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e1620903.mp4?token=OkjhT1Yf3EVQCiE4GtDoFVfRTXkb9nZKmAIu55C366EQhDgBdZvXPfnOsXOfrvrInzpQOJIiJK68miy1CEgmJ3dB80RPmprwW_Zxs2PNTKgh6647y9MxPkWIq1SK4LZOZMrae_kR9bWoJmV4-DWlhuNDoCm8zMKUsS7ATsgfVt7wLa1hTrMYutOixRl77oGS_FD6A28zr9L4gLwagXe3yw6dM8nAp2Eyf1EbLs2N3pknD_Gmt-0l6oIIlo_u7CNzVg3wg5_TN84Azw4Suw98_6fkGd32iwyi1UbNONRmw7h90EdNzOvu9TMWQUU9ADMOGO2f4w9iszjdIrrTiulgJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e1620903.mp4?token=OkjhT1Yf3EVQCiE4GtDoFVfRTXkb9nZKmAIu55C366EQhDgBdZvXPfnOsXOfrvrInzpQOJIiJK68miy1CEgmJ3dB80RPmprwW_Zxs2PNTKgh6647y9MxPkWIq1SK4LZOZMrae_kR9bWoJmV4-DWlhuNDoCm8zMKUsS7ATsgfVt7wLa1hTrMYutOixRl77oGS_FD6A28zr9L4gLwagXe3yw6dM8nAp2Eyf1EbLs2N3pknD_Gmt-0l6oIIlo_u7CNzVg3wg5_TN84Azw4Suw98_6fkGd32iwyi1UbNONRmw7h90EdNzOvu9TMWQUU9ADMOGO2f4w9iszjdIrrTiulgJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: اگر ایران اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما با قدرت پاسخ خواهیم داد، زیرا اسرائیل حق دفاع از خود را دارد و ما از این حق دفاع خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126318" target="_blank">📅 19:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02f10c40e.mp4?token=EqW5mo65UTyGMLwMlyh34hjAuem6z8XmWCJ01ytDef6A-AK8aEa9hLBGkskfGrE46ogaXalWRak9Or5irCuJXDutItgd0-wqeiDBMBKHnFx5byuxw0Hb5eRH9HlSqxTy8DdxW6BPCrAv4ERBGV3j_cUWj7aiztnkb9eDypt8t9dzKlO25PW4NDeH-IQToBwzktGDwtvMyK77SCs8GJTSmK3zS8R0l11HdeM2YIWr5FM7_q10x8ISWwsGyi_1rN_Iim0DqTe37E73ln7PRpiLaVvOycSyjJVuwOXFG7AiReAzaKg_oYmpiWpETbxVpQMSv-OE2LcNY24h1hb9LhE9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02f10c40e.mp4?token=EqW5mo65UTyGMLwMlyh34hjAuem6z8XmWCJ01ytDef6A-AK8aEa9hLBGkskfGrE46ogaXalWRak9Or5irCuJXDutItgd0-wqeiDBMBKHnFx5byuxw0Hb5eRH9HlSqxTy8DdxW6BPCrAv4ERBGV3j_cUWj7aiztnkb9eDypt8t9dzKlO25PW4NDeH-IQToBwzktGDwtvMyK77SCs8GJTSmK3zS8R0l11HdeM2YIWr5FM7_q10x8ISWwsGyi_1rN_Iim0DqTe37E73ln7PRpiLaVvOycSyjJVuwOXFG7AiReAzaKg_oYmpiWpETbxVpQMSv-OE2LcNY24h1hb9LhE9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ایران و حزب‌الله از همیشه ضعیف‌ترند و ما از همیشه قوی‌تر.
🔴
کارزار ما علیه آنها هنوز تمام نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126317" target="_blank">📅 19:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f62b9b32b4.mp4?token=j1OcLbOuUO3OuMJuyQu4PN-ucCUIx9aDNRyYKpQEqI0MfQOqS293dR4a1mCaQ59PTJeljgs3u4Mc8N8xjjLkrpVk8uYJKv4oSSNTonxpC7HrF0LtxldAWf_z1RrZQn0BH9GWaZHqf-7y43aJIzyuXA6HWue03QmeFYm_g1KC694Iak33rPMpjwwflLlIm5Df5jUwbbkRng3-u58veyLLH8DtEznIDcIW49qV0wq53kl3kFuV_Pxqz5bcWKkAoLTmup7uSa8XlHkwNg4Ogv0AKtF5H7KNnitxygSPLb42ImLu9mEwv4okbN3A4iz2dtp62IXHqi4-pgD7EloP1tRxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f62b9b32b4.mp4?token=j1OcLbOuUO3OuMJuyQu4PN-ucCUIx9aDNRyYKpQEqI0MfQOqS293dR4a1mCaQ59PTJeljgs3u4Mc8N8xjjLkrpVk8uYJKv4oSSNTonxpC7HrF0LtxldAWf_z1RrZQn0BH9GWaZHqf-7y43aJIzyuXA6HWue03QmeFYm_g1KC694Iak33rPMpjwwflLlIm5Df5jUwbbkRng3-u58veyLLH8DtEznIDcIW49qV0wq53kl3kFuV_Pxqz5bcWKkAoLTmup7uSa8XlHkwNg4Ogv0AKtF5H7KNnitxygSPLb42ImLu9mEwv4okbN3A4iz2dtp62IXHqi4-pgD7EloP1tRxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: حزب‌الله قصد داشت با هزاران تروریست به جلیله حمله کند و همزمان با آن، قصد داشت شهرهای اسرائیل را با ۱۵۰ هزار موشک و راکت نابود کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126316" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2c8a0c70.mp4?token=m2wx69fmv_Zji8XASY-3FksXKFdHIbkCJqn-xb2hef9LWU0h00D1Zm5pc-ijOSBIOUc9-rXqpFgcTbx9oL2LDif4_tWo_fychwPncEKXFEb2SK6snoKT_vWE8vKy6-wy3AIEwssSzIrWAFbOAWFOnmOsxkPKJiy2JtUFtX1XBqhpNuLvIMF9NSfOoEl1iXWwwWXkVmR8QKhEWkCMtV4i7dzKT5AImhI_KeLXlMz-ItnVAq3oeo4uI8wihB_WgO6L0BQuz2bQqfyuy9CIdj-im_U-gin4AN4QyvPYxm3SViVNJXbMrr0e-h96lnqMRTDMeWK32q96zmOXwq8rk4YQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2c8a0c70.mp4?token=m2wx69fmv_Zji8XASY-3FksXKFdHIbkCJqn-xb2hef9LWU0h00D1Zm5pc-ijOSBIOUc9-rXqpFgcTbx9oL2LDif4_tWo_fychwPncEKXFEb2SK6snoKT_vWE8vKy6-wy3AIEwssSzIrWAFbOAWFOnmOsxkPKJiy2JtUFtX1XBqhpNuLvIMF9NSfOoEl1iXWwwWXkVmR8QKhEWkCMtV4i7dzKT5AImhI_KeLXlMz-ItnVAq3oeo4uI8wihB_WgO6L0BQuz2bQqfyuy9CIdj-im_U-gin4AN4QyvPYxm3SViVNJXbMrr0e-h96lnqMRTDMeWK32q96zmOXwq8rk4YQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از عد‌دویر، جنوب لبنان، پس از حمله هوایی اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126315" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrzqDKF08e7_V4qvQpFYfUiwXxZ1gNLjMtm7qasc5AExKbBULWJ9No_P5d5eSl1oPYLyTGmOOTZRLS7VUx9Lk0t1nrgzq6va4or398JzSVFkVU8Cs82OCIsM0fXwwovvF08dAY0rT715XmhqIj5beX4PJz53D4SVkpYZK6s-9hANtQ0z7_m6SVwj6udRFRwtXqTX3xBNZmPXY5WW8zPmdPYXQJWNoAlqVRoy4j_bD9DOM4glM5Jj9sui7aGAGmVfs2gqcS3dCslxI6JNQR3cL2uevnG1zw00TE1LCl4UXx1bVBXvoNlc5bOezuyEjIICBDme9rOM904sPknkkAJ9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات شدید جبهه پایداری به قالیباف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126314" target="_blank">📅 18:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
گروسی: هفته گذشته بازرسی معمول از نیروگاه بوشهر انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126313" target="_blank">📅 18:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e941f5858.mp4?token=vn02gthPXwbbFpXsPGBU_SjVWDUf4NfMReILDY-pXwnbiEEOmSXLW6gpDO7JOkUjDdWupnEtPSR1rSmMpwQzUag-7qGz79QbAMOk18TIWbI-VEptqJGn1TtboD1OJzn8z934Kl9QUih9ZWfZXRCKNz6__PjzMiwokx7FlroT3ecCFvbdaN39fVC3vXj-lpChSvSTalCiOvfqt6BrWn-sb68ZCuhwrxvG1NZI9r2GpyldaOYsRFLxi8_BeIPd5_raFW08UG_5-X2xqeo5WHVcWoCFeNqvlSK6eBVkHIdoGfhCs7zIZJsYVs5AWD2dUyy-MF86wdJT5uTNN7ZE6nFdZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e941f5858.mp4?token=vn02gthPXwbbFpXsPGBU_SjVWDUf4NfMReILDY-pXwnbiEEOmSXLW6gpDO7JOkUjDdWupnEtPSR1rSmMpwQzUag-7qGz79QbAMOk18TIWbI-VEptqJGn1TtboD1OJzn8z934Kl9QUih9ZWfZXRCKNz6__PjzMiwokx7FlroT3ecCFvbdaN39fVC3vXj-lpChSvSTalCiOvfqt6BrWn-sb68ZCuhwrxvG1NZI9r2GpyldaOYsRFLxi8_BeIPd5_raFW08UG_5-X2xqeo5WHVcWoCFeNqvlSK6eBVkHIdoGfhCs7zIZJsYVs5AWD2dUyy-MF86wdJT5uTNN7ZE6nFdZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادامه حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126312" target="_blank">📅 18:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر خارجه اسپانیا: هیچ راه‌حل نظامی‌ای برای تنش‌ها در غرب آسیا وجود ندارد
🔴
توسل دوباره به خشونت، رنج بیشتری را به همراه خواهد داشت
🔴
کاهش فوری تنش ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126311" target="_blank">📅 18:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a021092ea6.mp4?token=MAUkAy2RkOb5CuajkBpK5N5Hj88CHNGr3AttFVqOou905hKKzqFfzj6js7pCVYDCo9RT__iLF8kM_x2Kim0p7YkiWj52ORno1VvLH3KYEyHEWyYKdQduDutVrwh0DHiYM-jqoQiEw6Va4759_1VkWfzi0HHL_YR1xVFNlxjeTuwjt7YMFNfYcWDLl-bXj93d_p96DjT7cb5CjJ08KsFj3OgS5hduMjVJ0yLccDslG52D-H7vmKCERbnXtQaSP8dFvejVKfHxe_e3J2USnYEiG8jypoQXSASCXdPUutHoNxLDTqzqrNDNztrhFBchZRvneCeMQYXQgZUKY6bSIN_6Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a021092ea6.mp4?token=MAUkAy2RkOb5CuajkBpK5N5Hj88CHNGr3AttFVqOou905hKKzqFfzj6js7pCVYDCo9RT__iLF8kM_x2Kim0p7YkiWj52ORno1VvLH3KYEyHEWyYKdQduDutVrwh0DHiYM-jqoQiEw6Va4759_1VkWfzi0HHL_YR1xVFNlxjeTuwjt7YMFNfYcWDLl-bXj93d_p96DjT7cb5CjJ08KsFj3OgS5hduMjVJ0yLccDslG52D-H7vmKCERbnXtQaSP8dFvejVKfHxe_e3J2USnYEiG8jypoQXSASCXdPUutHoNxLDTqzqrNDNztrhFBchZRvneCeMQYXQgZUKY6bSIN_6Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوخت رسان‌های آمریکا تو فردوگاه بن گوریون اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126310" target="_blank">📅 18:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتانیاهو ساعت ۱۸:۱۵ به وقت اسرائیل قراره یه بیانیه بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126309" target="_blank">📅 18:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKun9pOJ5drY_59pGTD3428Zlp1uvuOYuR9S8QzCV5H7xdgFuzIDrNb9oSv7PJkFbap0fE1bwiPvoByLETiePo6I5_VOaD1JP7JmEkXFpByn1pMhIq16LC4U9apdAz5edLl8Jy3zx1vtIsfIYKO1Y0349Jo_xGpyv-l_J4CcUTqxL02emravZl4M_QztaE8E30MkPeceOft7gMuWvOs5Q_5DTL3e5CVGrF9ik2EZ4gorBQJO0BBlYnxewO-27sFV6dvctOdi7_iDRzmmPVWJ5snvxWJXsc-bn4e03Zy-FwgYNMtnHdRL3qWzVQv_871I_JQGxDUWhDblJyzkeHAhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز: اسرائیل به طور قاطع تهدیدات ایران را رد می‌کند.
🔴
هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همانطور که دیروز اتفاق افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126308" target="_blank">📅 18:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq8oQPC6FjSbVkiJPSa_SNGAjSBCERMpHe8VaA8bl2ZJqcz4ToGU8_XuTGEh7cW7N611B8UFZ8TbpHoUZUATkChtjQnl3xHis_ZNKm-hk1kNcYHCVzK9-vf0351h1VZiREQr59AoLUzQU79sSP6Ti2zYyHB26uXl-aY64cO2i-lp1K2pgAc51HyCvZQ5R0milhZai1xklVA0KREUiCz6jh_T3IVlQHoIwLChMOj1WLxm4Gstvyw-t-iW3Jv4cMBdjmN7Ix15pk32teYXKo6LDemG4K85OTdzqjOImfcJBw6_IfSI-hrpQNhCwvCv7lUwNzbJgIGlO4yjPAC9ESU_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را برهم زدیم
🔴
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126307" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه
🔴
اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126306" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126305">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=usxD_oZbT8jiw0bNCSCYBlRHGV7VJY-1EIIWR1NQiVQ-UDxaZSwh-2mJ9B_sf-ou5Sw01nKXO_mnY95VxxGP6nv_v_vKIrd_z4Y6jt-ZAqr7Q36LiHvDcw354ynf6dnHMLDfrsKsxKOKDkpSfB0QONayaR9fhcA2EWRoCKimP82IhQuaageWOWkLng6dSgASpyz7FX2sfxShHjbeUTQW10oTeIrigBghArW6zLOs2q-eTfXb7H-IGpIOcRnEVbD9RY8bZpkl9OC3JkptEssKJgOuCnonHnO1Fq53n4DB270UjTHS64GViwsqNt4Xg3n5WHxix7vcCikO06uryOLMJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=usxD_oZbT8jiw0bNCSCYBlRHGV7VJY-1EIIWR1NQiVQ-UDxaZSwh-2mJ9B_sf-ou5Sw01nKXO_mnY95VxxGP6nv_v_vKIrd_z4Y6jt-ZAqr7Q36LiHvDcw354ynf6dnHMLDfrsKsxKOKDkpSfB0QONayaR9fhcA2EWRoCKimP82IhQuaageWOWkLng6dSgASpyz7FX2sfxShHjbeUTQW10oTeIrigBghArW6zLOs2q-eTfXb7H-IGpIOcRnEVbD9RY8bZpkl9OC3JkptEssKJgOuCnonHnO1Fq53n4DB270UjTHS64GViwsqNt4Xg3n5WHxix7vcCikO06uryOLMJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال هدف قرار دادن یحمر الشقیف در جنوب لبنان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126305" target="_blank">📅 18:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
خبرنگار الجزیره: آنچه ایران به دنبال آن است، تحمیل یک توافق آتش‌بس جامع در لبنان، در هر توافقی با واشنگتن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126304" target="_blank">📅 18:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJTct8zOMqqLT88zZlw6TDz14s2UMdR7KgYRKL4NkYn7utkDVuc03EMFryFLvFWnITvEcRT8ZeZwk_l705aiL6TENJlIJCiQNH32ev-ENZsWka87prrcuK_1vnHeccAqJeRS1TgMp7rCd3vzelcGHVwebvvYtGeRQMN_7hsety99b_4ZYz0nOiN9jVcr7sXQicWnqLo-rqMS0c1fYaoW_o-F5To3bAOHX-5wTUagonNdroKoYMT-mkAaMy-QhT1Xs8yOo7bdKMCX3A_HKy2Gi4eYtqbrBQ01bnvm8VpIqpe1LnJfaX0Mm2Isx470x4fQSVl3OsF4lV32jjIYbw0uOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای عالی امنیت ملی: اگر ائتلاف شیطانی خطا کند، منطقه برایش جهنم خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126303" target="_blank">📅 18:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126300">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8C2ReXEZn_1iOskrjkevgJtczQ3RHR2gVHd4ncuxIiS8RItIZDLa_9xq0LynNfi9Oa7IN3OIcm9liRKuX1-rnm_h9bPEr7lYBudYn-oYW4qBnO6yjekVOOrjrlmEwpxYlvBC40b3_Z6__X4O5Q0JVAZX4kRi3lmEBwZBtElc5ijvzBFHFd3ae97KcRGQKbOKdHB6d4dhbt2BGjtvXijxoTmNXy11MP0XVpclBBLW6hnNWAQI8shSPu-x8lUS36p7zG6r2Z6NkQpcqWsEbl9mk205Kn4owpJ8WKu1ergYHKm7sIl7J452siaJsC7kG-xloOSV0ZWGMtGDd0UZFU6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkDkcGMFGHvwrQErDyVHZj2BKupJdOV_ssiUHIpVcfOQekpv8fYRPhV_jPBjXgnJ2jcnhQwZUYKfwRgnErvIxKz4QYydKmF5HacVFtBU7ALIlbJnqU_nVKv7sqADI7JY-gSIH9OD-lrGDUfXDbpgiteOdZogcIUNqI9qw8XbPQjUCEUh7fjON-cY3MiEy3xq7bQz2fkUAsYoYnBhQq3915_k638jJP7U1fu9bOC-Sa1zAU0DXg0xRh6zNRuYtfQTylEVB-8x8cWpqkBWZnvbkmlF6nR3_72qVBLlMixdF2aiTyYR4QwxEF2UldkuUity-deU4-mdVxJl5-z_dKkbcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d52e06eb0.mp4?token=Ccy9pLRVY_7RGhDOLKtEXrmaj1sX3RF8RiI24U3btLK_iiYjOuRHKmY9XuUfyYDkkp3ry04GZT1Gi-2W3T6Wr39prCxtuYMRGBk8cab0Iae1Znb9fIL3u-JSBhfjPYmAfX_y4hygNJiiLsAEmi3swWttckSfl8ZNXaGYcgU5iTAzfs0O0ZFcqPbm0Jvn3aHfYvte-eUJQey30Vy7qbdCC7oA4f6gJX3CKQmk22WIjXE4AIw7i2B3DezyLUPhTG-rWQW3lJkv-T5HzOM_wae2ydxFxPmnBfw6nIu5UmyvL5m8GFWYL40NPheltL2ntPND7UZMdAp9Myycod2-i0LytA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d52e06eb0.mp4?token=Ccy9pLRVY_7RGhDOLKtEXrmaj1sX3RF8RiI24U3btLK_iiYjOuRHKmY9XuUfyYDkkp3ry04GZT1Gi-2W3T6Wr39prCxtuYMRGBk8cab0Iae1Znb9fIL3u-JSBhfjPYmAfX_y4hygNJiiLsAEmi3swWttckSfl8ZNXaGYcgU5iTAzfs0O0ZFcqPbm0Jvn3aHfYvte-eUJQey30Vy7qbdCC7oA4f6gJX3CKQmk22WIjXE4AIw7i2B3DezyLUPhTG-rWQW3lJkv-T5HzOM_wae2ydxFxPmnBfw6nIu5UmyvL5m8GFWYL40NPheltL2ntPND7UZMdAp9Myycod2-i0LytA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله پهپادی اسرائیلی خودرویی را در نزدیکی مرکز صلیب سرخ لبنان در ورودی جنوبی صور، جنوب لبنان هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/126300" target="_blank">📅 18:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126299">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
شهباز شریف: هدف نهایی صلح نزدیک است/همه طرف‌ها خویشتنداری کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126299" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126298">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل گزارش داد که ترامپ و نتانیاهو دقایقی پیش تلفنی صحبت کردند و حملات به ایران و جنوب لبنان بزودی به صورت کامل قطع خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/126298" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126296">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYDInFC1zlYANFPYshASvac0Qz_20uQcjmNMMqeygTzdxOq3oOcezU_MjBHXWD0BYpRXzIt3DJA7N9U8vjHc2xUmBBY1hzTqJj-X-7ZJoW-i9jd1yMKtiQ_NJpIv-Rl65Pm4z5h3LkoleFR0n4a5QPucgz1XTiw4rQEnAYZwk9J3rQJbhxCIC9Os4DI1MCjw5LpEPRmlzc91YCkuiI-va3pfcil1SOOKG5K62cwOEYq_wUg0SVCoS_6jIu7j1J-teuEClgG_i-O9tOzN2oq-RBW_HJd2K6lIBYlbkDWUw1n6hkewRGHCKkqObRPmKHizjY6XYFI4vzjl40-B01ZLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=eH6Po4Uuq4UcXNo2j8Bh4k8-yNhdrdzlstIQboFamcMJecHQfghUbv7-rdIqQaPCdEoIocUoETkwCpCz_QQ2ZKVFJPyOIJ212aoROmyt4gn1iXilhAoSxVTZAt7eYg6sIdcClMzET73HoODFpSMkWC-Y_Q2e7udOgBfgvRRRi1l4OonAzOYpJXZg0c1MylJ5apaWARSeS1zWevqsebcCsLrShuiDYiRfNVJ6mFtqwK9p9m00dLv7vLfsbD2cgXE5Ki2nkbN36_taOLE-sIUoMl5PxX_aVWb9QNn7GWYmmARK2aWxan57YH7Ya0DBalH5n9_fY6z61pxWHkM3mdH-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=eH6Po4Uuq4UcXNo2j8Bh4k8-yNhdrdzlstIQboFamcMJecHQfghUbv7-rdIqQaPCdEoIocUoETkwCpCz_QQ2ZKVFJPyOIJ212aoROmyt4gn1iXilhAoSxVTZAt7eYg6sIdcClMzET73HoODFpSMkWC-Y_Q2e7udOgBfgvRRRi1l4OonAzOYpJXZg0c1MylJ5apaWARSeS1zWevqsebcCsLrShuiDYiRfNVJ6mFtqwK9p9m00dLv7vLfsbD2cgXE5Ki2nkbN36_taOLE-sIUoMl5PxX_aVWb9QNn7GWYmmARK2aWxan57YH7Ya0DBalH5n9_fY6z61pxWHkM3mdH-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال هدف قرار دادن یحمر الشقیف در جنوب لبنان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/126296" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126295">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت دفاع عربستان سعودی: آنچه درباره هدف قرار گرفتن پایگاه الأمير سلطان در الخرج منتشر شده است، «صحیح نیست»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126295" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126294">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/ایران اطلاع داده است که در صورت ادامه حمله اسرائیل به جنوب لبنان، حملات موشکی خود به اسرائیل را آغاز خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/126294" target="_blank">📅 17:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126293">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام آمریکایی: ادعای اسرائیل مبنی بر اینکه آمریکا موشک‌های بالستیک ایرانی شلیک‌شده به سمت اسرائیل را رهگیری کرده، صحت ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/126293" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126292">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از یک منبع اسرائیلی نوشت: نتانیاهو عصر امروز در جلسه کابینه امنیتی در مورد تشدید تنش با ایران تصمیم خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/126292" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126291">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75c4ec36b.mp4?token=GeNeGv4v8zSIIWvITPhOpIOUpDYCIJ8YddWX-TCGZEQs_jlg85m0JPaApm7LTpcjOz8oX3vPa_yPeIQrxSZjEBsIH5KwTSt3tNPEvkw4eA8mC0wwahRfGtMNaSy0dcQRTn6WNWJohOCPOY15ndt9BQOfcY57VixyLwgBLb4xe_1fhhkLQB1Vm_njrBsYd45mO113U42o6uFtdWcO_S1j4O_3MWbiIQS5Stb2upZRynN1h_1YcYDtXsXkTooaYCsUUcM67H5AzDS6JzDmgBl9Sb8bAr9GBUe6GgRj5hr72nGMdpGk3tgK0dHpgrarXaohVdSeiHDCj2T27Q1JaDl1Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75c4ec36b.mp4?token=GeNeGv4v8zSIIWvITPhOpIOUpDYCIJ8YddWX-TCGZEQs_jlg85m0JPaApm7LTpcjOz8oX3vPa_yPeIQrxSZjEBsIH5KwTSt3tNPEvkw4eA8mC0wwahRfGtMNaSy0dcQRTn6WNWJohOCPOY15ndt9BQOfcY57VixyLwgBLb4xe_1fhhkLQB1Vm_njrBsYd45mO113U42o6uFtdWcO_S1j4O_3MWbiIQS5Stb2upZRynN1h_1YcYDtXsXkTooaYCsUUcM67H5AzDS6JzDmgBl9Sb8bAr9GBUe6GgRj5hr72nGMdpGk3tgK0dHpgrarXaohVdSeiHDCj2T27Q1JaDl1Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کالاس از اتحادیه اروپا درباره مفهوم ارتش اروپایی: چرا من از ارتش اضافی حمایت نمی‌کنم: هر کشور عضو یک ارتش دارد.
🔴
اگر این ارتش را به ناتو اختصاص دهید، دیگر نمی‌توانید از آن در جای دیگری استفاده کنید — همچنین نمی‌توانید ارتش دیگری ایجاد کنید، فقط یک ارتش موازی.
🔴
خیلی مهم است که ساختارهایی ایجاد نکنیم که ممکن است باعث سردرگمی شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126291" target="_blank">📅 17:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126290">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c5fd0563f.mp4?token=EdXMmfYlSSipJb8Y7z7S0j36FXENMXntT-H3CTHs6VBIvt-uNIe-QZWmQJibL7aurouw-NCgwX6MrvkkLcS_8l4c80TsgFTDBrrBbV1SLbhf0UgM0l4Soeegm2SRUmPANNxZeIOC0jIgl0MutNJMv-5Q--jw4WRWRRaqRbgFoOUXcyl5UPKGKR51u2ySR2j_fAF4qPA_wjqKyL00O7ib8o-FTD_ttfTIVhQelwwdMRSBZ1ckiVGXpuH-y1y-83TC-DlWSXoM1TawdD1CG7yxNK8Ulhwaa_0L7HFYzj1JgU7yies-TIu2a5HRH7PD6R66hN9YpZP3A1VUsP8-8a_CRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c5fd0563f.mp4?token=EdXMmfYlSSipJb8Y7z7S0j36FXENMXntT-H3CTHs6VBIvt-uNIe-QZWmQJibL7aurouw-NCgwX6MrvkkLcS_8l4c80TsgFTDBrrBbV1SLbhf0UgM0l4Soeegm2SRUmPANNxZeIOC0jIgl0MutNJMv-5Q--jw4WRWRRaqRbgFoOUXcyl5UPKGKR51u2ySR2j_fAF4qPA_wjqKyL00O7ib8o-FTD_ttfTIVhQelwwdMRSBZ1ckiVGXpuH-y1y-83TC-DlWSXoM1TawdD1CG7yxNK8Ulhwaa_0L7HFYzj1JgU7yies-TIu2a5HRH7PD6R66hN9YpZP3A1VUsP8-8a_CRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد شاهد-۱۳۶ مواضع گروه‌های کرد مخالف ایران در شمال عراق را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126290" target="_blank">📅 17:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126289">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اسرائیل هیوم: شورای کوچک وزیران تصمیم به توقف حملات به ایران و ادامه عملیات نظامی در جنوب لبنان گرفت
🔴
هیچ محدودیتی برای عملیات ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126289" target="_blank">📅 17:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126288">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فیدان: به تلاش‌ها برای میانجیگری میان ایران و آمریکا ادامه می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126288" target="_blank">📅 17:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126287">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
تامیر هیمان، رئیس سابق اطلاعات نظامی اسرائیل: «ایران در پی آن است که جنگ را نه‌فقط با این دستاورد که شکست نخورده به پایان. برساند، بلکه با پیروزی‌ای مبتنی بر دستاوردهای جدید خاتمه دهد؛ از جمله تثبیت حاکمیت بر تنگه هرمز و ایجاد بازدارندگی گسترده‌تر که لبنان را نیز در بر بگیرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126287" target="_blank">📅 17:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126286">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری / سی‌بی‌اس به نقل از مقام آمریکایی : دولت ترامپ دستور داده هیچ اقدام دفاعی برای محافظت از اسرائیل در برابر موشک‌های ایران انجام نشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/126286" target="_blank">📅 17:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126285">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نخست وزیر پاکستان: ما با شرکای خود سخت تلاش می‌کنیم تا یک راه حل دیپلماتیک صلح‌آمیز برای این درگیری پیدا کنیم، زیرا به هدف نهایی نزدیک می‌شویم.
🔴
ما صمیمانه از همه طرف‌ها می‌خواهیم که خویشتنداری کنند و به صلح فرصت بهتری بدهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/126285" target="_blank">📅 16:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126284">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سفیر آمریکا در لبنان پس از دیدار با نبیه بری: آتش‌بس برقرار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/126284" target="_blank">📅 16:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126283">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
بریتانیا به شهروندان خود توصیه می‌کند از هرگونه سفر به اسرائیل خودداری کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/126283" target="_blank">📅 16:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126282">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d160fb5d.mp4?token=O7B7MdZZxoTPxrBBVDoiC2xEqLIrZWiMvcvf4p79b4z9vKhrcSFvlCLOT_4lNvlO1iRpxwFjaIG25jUPh1g5hZu3HFGq1m04SsR4zzgE0mpd8bOpNOgiJgMZP7nVXj5DzpTmGyadA4k-eq_f4P6N1blX_Q6CNceyjRzK1wsUJY2yKQPIk8kruF_2ao_hEy4zFpcwr0sl9Mbh5Scz_AShjmk2FQBGwatDto5ocTxNV4OYmxc7buqyfc2VOtP3YLVNsRltwb4wUYMFTZBhGH8F1Rk3gxXZhRFaKkOa9N7SwF3naZWIc8k9QatjKigfDUW8quiUPHdq5gtUwyuRJvg9p4YHeNemUEgdxo0lNbFYtxeA6PdVHpbGpbF9UJ2gs6Wuk6sArCbLjrGTpCTc1UAhH0JqhLEuGfC8lqyi1ysG6VTMvkuDKS3ZMop5KfU591snMdcB8zNjoqtn6bgbpvuRmXLVnKJ3tYSomBC3phYqtTEWetbLS-1F1tfNgKolXQ4dmtUO2r9eMLHAEGVc4RyuOt9EbB9uw1WQzYqdkqne4Vvc5vfGlXVoDCZTc0ADW5s2r_LH80H95YBtTAjut52-P3GmODS6XMIMThkkJOe_QXxq_EfEkoATz1MVOmCGwVqGzPW0Sv50kBvqBcqPxeZWFokwMpsXNCV-gVrzX5VEQ0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d160fb5d.mp4?token=O7B7MdZZxoTPxrBBVDoiC2xEqLIrZWiMvcvf4p79b4z9vKhrcSFvlCLOT_4lNvlO1iRpxwFjaIG25jUPh1g5hZu3HFGq1m04SsR4zzgE0mpd8bOpNOgiJgMZP7nVXj5DzpTmGyadA4k-eq_f4P6N1blX_Q6CNceyjRzK1wsUJY2yKQPIk8kruF_2ao_hEy4zFpcwr0sl9Mbh5Scz_AShjmk2FQBGwatDto5ocTxNV4OYmxc7buqyfc2VOtP3YLVNsRltwb4wUYMFTZBhGH8F1Rk3gxXZhRFaKkOa9N7SwF3naZWIc8k9QatjKigfDUW8quiUPHdq5gtUwyuRJvg9p4YHeNemUEgdxo0lNbFYtxeA6PdVHpbGpbF9UJ2gs6Wuk6sArCbLjrGTpCTc1UAhH0JqhLEuGfC8lqyi1ysG6VTMvkuDKS3ZMop5KfU591snMdcB8zNjoqtn6bgbpvuRmXLVnKJ3tYSomBC3phYqtTEWetbLS-1F1tfNgKolXQ4dmtUO2r9eMLHAEGVc4RyuOt9EbB9uw1WQzYqdkqne4Vvc5vfGlXVoDCZTc0ADW5s2r_LH80H95YBtTAjut52-P3GmODS6XMIMThkkJOe_QXxq_EfEkoATz1MVOmCGwVqGzPW0Sv50kBvqBcqPxeZWFokwMpsXNCV-gVrzX5VEQ0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی رئیس ، جمهور چین  به پیونگ یانگ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/126282" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126281">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=kQV2ajsJsQSmxZ6Gq2j6coTQArdgRNzsB9vR9zUAOTsSm6MapNZaZ72jmjQxOay7EiJhg2Yh5c08PEfeMPA7iyL9-E8fYroU9StY-tFEY1vp720PRDmWkN3oKIuiDX0zLqaBOQFFavbrxNhyukNGx1PeZIY2lzAnEj-LFlC7y5oG62KqNpB5eGnaO9W79ug4u_pZXy_UpXf3nDaY2-uDbnr-K_JOuYFgN42VNCMMu75k3Ql3C2Rf3bf5_ELeGwVgyV7wc1NfrMGy1gvhKA0zplnFvjt9kDvA8PLug8eEN8vCzyVXOTvTPnu87-zrap6Ogq8Gq9iTORtkzIzWxXIu6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=kQV2ajsJsQSmxZ6Gq2j6coTQArdgRNzsB9vR9zUAOTsSm6MapNZaZ72jmjQxOay7EiJhg2Yh5c08PEfeMPA7iyL9-E8fYroU9StY-tFEY1vp720PRDmWkN3oKIuiDX0zLqaBOQFFavbrxNhyukNGx1PeZIY2lzAnEj-LFlC7y5oG62KqNpB5eGnaO9W79ug4u_pZXy_UpXf3nDaY2-uDbnr-K_JOuYFgN42VNCMMu75k3Ql3C2Rf3bf5_ELeGwVgyV7wc1NfrMGy1gvhKA0zplnFvjt9kDvA8PLug8eEN8vCzyVXOTvTPnu87-zrap6Ogq8Gq9iTORtkzIzWxXIu6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: آمریکا هزار کشته و ۸ هزار زخمی داد و این برای ما کاری نداشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/126281" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126280">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
بن کاسپیت، روزنامه‌نگار مشهور اسرائیلی: ارتش اسرائیل به سرعت در حال اطلاع‌رسانی است که شلیک‌های اخیر «به سمت نیروهای ما» بوده است. یعنی نه به سمت شهرک‌ها در شمال اسرائیل
🔴
این یعنی انتظار نداشته باشید که به ضاحیه حمله کنیم. یعنی ما را به حال خود رها کنید. یعنی ممکن است الان مجبور شویم به «حملات چند وقت یکبار» به جبهه شمال عادت کنیم، همانطور که قبلاً در جنوب به آن عادت کرده بودیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/126280" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126279">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترافیک سنگین در محورهای چالوس و هراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/126279" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126278">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سپاه : طی 5 ساعت گذشته سه بار مواضع گروه‌ های کُرد را در شمال عراق هدف قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/126278" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126277">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مدیرکل مدیریت بحران هرمزگان :
حدود ۲۴ میلیارد تومن خسارت ماشین‌هایی که تو جنگ آسیب دیدن پرداخت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126277" target="_blank">📅 16:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126276">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
دیر قانون راس‌ العین، در جنوب شهر صور مورد حمله هوایی قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/126276" target="_blank">📅 16:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126275">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کانال ۱۲ به نقل از یک مقام ارشد اسرائیلی: ارزیابی غالب در خلال مشورت‌های امنیتی حاکی از آن است که دور فعلی تشدید تنش را پشت سر گذاشته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/126275" target="_blank">📅 16:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126274">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
لغو تمام پروازهای کشور تا اطلاع ثانوی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/126274" target="_blank">📅 16:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126273">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
اورژانس ایران: ۱۵ نفر بر اثر حملات اخیر اسرائیل مجروح شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/126273" target="_blank">📅 16:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126272">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PReP0XFMk9EWF-5MTeQ1iX0MoNBJF5Pjzm1TWPerK5PTgBjAl1ROrzKLGsKgAIk6FnMxe9lbtLtI_pNSLCm8EXxFHCbD3oydwARp0C80pflSMrxM0Q_h2WBL_vN13B5LvPe4Cv2v6VNLIgVtKHHTCv-By0WQFPplUblxXL1kMl3PVKJvvBV10-zj7J0Q38sguTeVqy958o8gdC7b2Tz6Wu2iBCy0AjmFpLQlXwSQMAtMHhnceHE2d8dX90E2QmhelxkokGA2XbtBdNX5ZOIvHVP9hr-vA8fNGN4hQs-XNIHjuS5J-P-MCDHMqBBHJgkZ1nzEdC5PjnKlvwkNnyT5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارنس نورمن خبرنگار وال استریت ژورنال: پیش‌نویس قطعنامه آمریکا برای نشست این هفته شورای حکام آژانس بین‌المللی انرژی اتمی (IAEA)، که کشورهای اروپایی (E3) چندان مشتاق آن نبودند، اصلاح شده و به گفته منابع، اکنون به قطعنامه مشترک سه کشور اروپایی و آمریکا تبدیل شده است. بنابراین به احتمال زیاد تصویب خواهد شد.
🔴
بر اساس برداشت من، فشار آمریکا برای ارجاع فوری پرونده ایران به شورای امنیت سازمان ملل، به عنوان یک مصالحه، از قطعنامه حذف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/126272" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126271">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf6i1xzP6yvqOEziHOOzhN2mL3-e5WF5Elq_mWRQuz9qNRt2hBae-iaiZitlDTH-hNu8x-Cbxyn_O17jFy9efgpxcRH78n1YdpfRLWedpdq1pZs7MSj83qiWxWGHARslCOBrT5j6voLqg73-78t1dmgbURakLUzoyBVEd7U0hRrrGhDBE149ah_k2iZDXF9JSuuMwhBtQsyI-63XmQljQu9WxxEBYjZHGQI-amuj9m-5RB_UaT2S9jm2sPIgPD-znwOW3_KN7pxYMhJB384r7dNWHRJAt_VeYIo-5yz3Byvgar5r_vD3L_jNrjXyWHRLyB6k29n2j0eYrregHtNXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تخریب در الخریب، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126271" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126270">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رویترز به نقل از منابع:
اسرائیل تصمیم گرفته است حملات خود به ایران را متوقف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/126270" target="_blank">📅 16:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126269">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
منبع عبری به i24NEWS: نبرد بزرگ با دولت ترامپ از این پس، ادامه جدا کردن مسیر مذاکرات تهران-واشنگتن از جبهه لبنان خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126269" target="_blank">📅 16:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126268">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کانال ۱۲: به درخواست ترامپ، اسرائیل حملات علیه ایران را متوقف می‌کند/ حملات در جنوب لبنان در روزهای آینده با حداکثر قدرت ادامه خواهد یافت
🔴
اگر حملات به شهرک‌های ما ادامه یابد، ضاحیه (بیروت) را نیز بمباران خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/126268" target="_blank">📅 16:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126267">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwPBWOHXbx3NaOEhh0xrJMdjbZjSumfdxG3-ubMurqbl-j5Q-vyNlekiFxD34qJc7g0wvInq-BzQaZntA3XWn1QStIz9MROIZvq9MkAR89rCUyGibb9BK9gEOW5trnABurQ5bkYd0rvhUDgk0PF6rcQnCzGKawWRp-1Q46NAJvRXw53oJTZSwFFfA1GurdUHu5IrCcqM26LB7ZLXYuUckgb0sKFYNESmZG0b29_XFAEmZeFGMqoT7rYvRH4PlMdqnHpIh5I8FqRjRQUJoEmU5eCBNJn7MqCoXL4TXWLSuT-zgjwkg446uR92xujnYnTbz9KUhuwbZq4JPLSvsffudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام اسرائیلی به شبکه ۱۲ : به درخواست ترامپ، اسرائیل فعلاً حمله به ایران رو متوقف می‌کنه
- ولی حمله‌ها تو جنوب لبنان تو روزهای آینده با قدرت ادامه داره
- اگه حمله به شهرک‌ها و غیرنظامی‌های خودشون ادامه پیدا کنه، حتی ضاحیه رو هم بمبارون می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/126267" target="_blank">📅 15:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126266">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کانال ۱۲:
آژیر خطر در کریات شمونا و حومه آن در شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/126266" target="_blank">📅 15:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126263">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQ0nf_RTHkOIGYrWGFst2w-b8OlDc3v1Rj7mMO_eYWJbUIkrsHXTupf_1ne_BaxBTHoRQlcuwHNxSIBLy0MZcZx8fst8Dlbsq89aerFbdH9j_pThhFvxTt3LqeLa-HxubIgKJkf0oyYYlmAMOpgtsdKVJ2DCiOfMjB7ni5BNoa--82b2wMG6BXwvCZpHSC7VyX8saAsLIPkkOXp7DgC6dPmOXyPKZfe2Yrip2NA3Pk2WCckCzm1WNjFhlRjb4KA-pZYg8V3ifgbJ5oclI8trhb6TJ-k1foIdvPAig3Gc9uGmhZsz3M8gJG8HJaz0NWdtXhzQ3DJ9Og6zXyAQFQvBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2-dtWxDwNbTaf5HZb-Atr-U8-f-O7SpISD5FD33HAmxtxy2Uk5i_gu1OXz_ggTzZMZC9lckXcciyqkSfh55xalMaWGNci6nbqIyMsgLHahc0xSRvue_2NUsrAVnrowi7wziCpoiY8RBIml8XxTkPXcbGwoZIiTwSC3iiEjS6CQDfbZrZIvkrHTijK5BZ9cITx_v_2w6aLjpTaxjJeEXCUxvvLzpxCL2JHgnWf0h3M7pPjl0E_UiKD6fISuAhBcP2hcKg7l-S44A2iuJmHdWn4IZ0gMf7cuAIxqEr9W8wGsGBilXU2wqpMOGcDCWT1bPUU-pxQG0fwMPkJT5879_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2kCvNbQvyXBndSKMpqFc0o8J9KzWvDhQsywuv6yl6IdNnr0eNDgdHM0fqJ_wotATa8TrB3Gc-Zt86KrKaqVrDW1AqCj_QznH8z8UQN1UDgprDgVYafPaItIG0S_OFuYOYcbiXXmPy-yYHerxlx-y1c7_0glws_krv2mxWdfdfMvXI-0sRlIemSTDBGWcpjcfpjWlbIN8tZp297kJNy5dJARxU0lSrCAXQFqZ33hlvXkVXZUZvPaTSufMbMfq9AyNj72JYRWkHZjybM5BAuzucuAz6-Mdik5_TbTDQ9vIH2wcseasShfsv70kZ63Tj4oBEv3RAbLRdeMQaZKgZRxsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/126263" target="_blank">📅 15:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126262">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله هوایی اسرائیل به منطقه مسکونی در صور، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/126262" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126261">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEkxmniVuLpL7ptHbCNE1hg9JBcBx_l2jGK_YbTD2KU3nxKizI_-qbDw8vz3DJkA_8TEuLnG1LUFCvQrjQarcLC3YPIqByv1gqooxYUwJg9K2_vfODODMhNLUnB3dQGU3PTfY31WjhjrKpdwZmJlzMEVTkfBRWnfz_8ZgxnRU1lOe_D7zTr2YxVzUGsDu1u2j-LUqh9QLscMgDFZKevJlhz38Es-j2OCX_Y5riCfQed1lBiz9XID4JRk77NOckk0l1rT4kQmQide0NcJN_94oAl_hZd7KvlK7X3QTw05GbMHjXO8DFmHjFz0mKonoxQP8bWtSvpFHKKrpOKH2bEoaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه رسمی فیفا :
دیدار ایران و مصر قطعا دیدار افتخار همجنسگرایان خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد.
کاپیتان های هردو تیم باید بازوبند رنگین کمونی
🏳‍🌈
ببندن
@AloSport</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/126261" target="_blank">📅 15:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126260">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
عراق از بازگشایی حریم هوایی خود خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/126260" target="_blank">📅 15:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126259">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c09YbdWmzqmdugwnXzcumrDNC164liq-SmxS8tCa8etJ0F47U_Az49Q1xSdmCxmmAroIkpanPN9gplNbPrnr_dG5N3XbBGEKEzOp7Iq1T4dKu4mHhUG09JeIKANgBwCKvnOEQsY47NfCiUCR7Ij58xAg-86oa48M8jaFTyUGj_oyAoP5f2Z3AJ7qIoLyoYSUPmVDbb06wN1vqFBNGCmqQI412o79z9ZHcy_bNL2uET6QjvQhXQ0L1jtc59Bc0IeoPoQkV1u47mJy8BTwmArrGilMOTNaFI7Ulxjq4FHRjNA3xppxh7tVf6fdh4IL85EeZ9zCgNLNPzDmcnIWAsj4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادیو ارتش اسرائیل:
ایران می‌خواد دامنه درگیری رو گسترش بده و به حملات اسرائیل فقط تو ضاحیه بسنده نکنه، بلکه تو جنوب لبنان هم پاسخ بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/126259" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126258">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شخص دوم مملکت،پزشکیان: در برابر هیچ تهدیدی عقب‌نشینی نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/126258" target="_blank">📅 15:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126257">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVvZwGBbNvgl8OL1rgAW5638miJ7DziUNMhPgdZRjJeHnNRxzvHT9lyg35M6o_56vTw2NcMMGSTeSvK7665vuupeAVrJzS8n_bas4IH0jDvXul4Ow3O7wViZqAOSqxKNrV5a5_1mFXFSsZCl-Xvg3HwtxXTu0Qjbk9H0oV31DcicF9PbH7KRuioXGsd0l8KAewBU0auXYsX0Nq3d4L1u27bYon1LEg4a1QWKTJ33bn5Edv4xz_O4zK3NgvVl7UzCpj7fg4wiklEg7RHyoNNkIWpym_v2-Vl8esf6-CvYJr3NAS3YFe_LfKcxQkgk9Wf34XglZH1dMQpLPNLB-PvsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/126257" target="_blank">📅 15:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126256">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7zZGAm1oFfPGVutwkGm3aN6JHazygI4UakpHFZ73N87_h4sEXkbxnil4r_PDEwY9adpzzQbMBOkWhVIwyxLo6kTl0jKr0A2b3sLO9-rRik9tM8icp541TApOd64urymMLa-_jKgbxz_0F-54dwJkrqu32QoH7dtCKrImrrsBxVTfYjxp99-dTUXQA2K_lW9-A9gsum6BRfhKyYer1u1xWXGG0trflZLXYs6kpwfQeeSZM7boqLch8ck7wc568LBm8vgYDX3Q6ds7eLZn5mqr-VbZPTSDbAARNIcPECB8CBH32ZgXGpIYv8rMbvIO1OFkkoSMsQkqAAGTJjy_pT6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری منتشر شده از حمله نقطه زنی به تاسیسات گازی بندر حیفا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/126256" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
