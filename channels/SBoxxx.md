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
<img src="https://cdn4.telesco.pe/file/nl02Buj8uC0MZA2sgJGdoL0VDBGsXv4AJk0qmdyPeKMSkE7bUBXGkF406JU5OKW82d5iuRKGt-I5hspNIe2mSU9dF12bKyv8xuErmJN5EbeaLOZYmGjnBoGsQ-Rd0hI-OqkKuDokkrpjExGfx7RykQs4am0-tzpwgAGpkIkgublfAOTThGNjCSPcogzXVU2PA3nd3iqHCgLpT1YY9KxGt6Vnf7KeXDiDnCx8dvX5JHprpQZdNeIXbziNWLcz4DFCp8BsIKegBAS1je72QyirJxZ2hFgqwcG5Cph2rqDacxFl5ON5q5NBd3wtRugq5_BqYcHNlIY4ZPlTHVZ8laMsiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 17:57:25</div>
<hr>

<div class="tg-post" id="msg-19555">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_Ik-hnxGpqd5b4P-H_3lLhYUMhGtKrpRjeLUdKji7_C1_yCdmL7Q1YIFqqJlME7tC4Nr1Xo1hUshfHOhjksYLF9Q791kpVVCQtsHloNZvsP1vr--bwCJu2_8bnbOs_e_qrrj6IsWjgm8QWTB5h7qp-l2LesAX6oMMv1SsnJeHLr0w6Chtkvjq9R6GEZhUYP6vfbgnLnr8Jw8DhmaCY79aEJWZRUvxcptcGX6TdAEgUucF9fzlR9R-fLGsg0xtvrzKzSwL-osQgCvHIuklhIwG5t5mf4k4yOwqrnq1z1IsdSCixkNFUrUoKi38f6ROCfkXzv5J0pFbr9N-dAiaGrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه روسیه با پهپادهای ایرانی رقابت تسلیحاتی در حوزه پهپادها را تشدید می‌کند   رئیس‌جمهور اوکراین، ولودیمیر زلنسکی، ماه سپتامبر مجمع عمومی سازمان ملل هشدار داد که «ما اکنون در حال تجربه مخرب‌ترین رقابت تسلیحاتی تاریخ بشر هستیم»؛ اشاره او به بهره گیری روزافزون…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/19555" target="_blank">📅 15:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19554">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به جای جای ایران که مینگرید، نشانه های بازدارندگی قدرتمند جمهوری اسلامی را می‌توان دید</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/19554" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19553">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در اسلام آباد غرب، کرمانشاه خبر داد.</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/19553" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19552">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در اسلام آباد غرب، کرمانشاه خبر داد.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/19552" target="_blank">📅 14:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19551">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd37ccbfd.mp4?token=aL35l2FUuZ7U4QalHNpTBPGEK8uEMVFStyAlCSXZc5gbiJ0fftBG0hGPbTj8yf4IX6grfsdOLzy50yUwA_wku6UIOq-r-ahZlsOD5INR5rxUe3v6XT6mq3j3aAX2mrZsSLClBcwpxHfO4Xfn-ANZpgQ1Lm59GrG_UHcp45RJHICVWnOZcWR6dTB3lZ5NXz6_po319dMMFG7o9tOTSH-8wFQ8KebPtqYSRE1lMEqfj-NMP4ItsRnZR0uAm4OX_4PGLX4gOUoH69c9xpWoje6fcy2DCuYN15_gBoyAoWffvIYoDDwmGugU2cpMlRvn27q1ZzaPtYZOjHNY2xCyUdJ3rD3WLdTkxkHxgA-QVZsG0I7zjcY6pYCI0p4JnqOJ58RVkqP3Dc9eOa2-kxHVOKQUPdqba0wz2I4BibNmbP-Dd0w6FeR8rU3mNq0b9dAENJ_dOCfph32VmL62i5mzcj3sp_HLUJ4FtY8tGewhSQpGzMC1QRJFs1BYLgPeJOZ2kK57_2fv3_6mlZ3_lEHNbsAkS1Vs_92itmFJKtw69PaHZO34U0PpOllM-MuLcbuYilJAxzAJ9NOJ6TDcL23Z9TG3fOH-5WfCjbTKXsYUyqnI-TaQun9v0Q1H_hCsOv3Jrs97wN_IqyH30kWn59tWf_s8k7vyvl23z9FZP-jjSNNyGtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd37ccbfd.mp4?token=aL35l2FUuZ7U4QalHNpTBPGEK8uEMVFStyAlCSXZc5gbiJ0fftBG0hGPbTj8yf4IX6grfsdOLzy50yUwA_wku6UIOq-r-ahZlsOD5INR5rxUe3v6XT6mq3j3aAX2mrZsSLClBcwpxHfO4Xfn-ANZpgQ1Lm59GrG_UHcp45RJHICVWnOZcWR6dTB3lZ5NXz6_po319dMMFG7o9tOTSH-8wFQ8KebPtqYSRE1lMEqfj-NMP4ItsRnZR0uAm4OX_4PGLX4gOUoH69c9xpWoje6fcy2DCuYN15_gBoyAoWffvIYoDDwmGugU2cpMlRvn27q1ZzaPtYZOjHNY2xCyUdJ3rD3WLdTkxkHxgA-QVZsG0I7zjcY6pYCI0p4JnqOJ58RVkqP3Dc9eOa2-kxHVOKQUPdqba0wz2I4BibNmbP-Dd0w6FeR8rU3mNq0b9dAENJ_dOCfph32VmL62i5mzcj3sp_HLUJ4FtY8tGewhSQpGzMC1QRJFs1BYLgPeJOZ2kK57_2fv3_6mlZ3_lEHNbsAkS1Vs_92itmFJKtw69PaHZO34U0PpOllM-MuLcbuYilJAxzAJ9NOJ6TDcL23Z9TG3fOH-5WfCjbTKXsYUyqnI-TaQun9v0Q1H_hCsOv3Jrs97wN_IqyH30kWn59tWf_s8k7vyvl23z9FZP-jjSNNyGtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/19551" target="_blank">📅 12:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19550">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سفارت ایالات متحده در اردن :
«آمریکایی‌های حاضر در خاورمیانه باید احتیاط و هوشیاری بیشتری به خرج دهند و برای لغو پروازها، بسته‌های دوره‌ای فضای هوایی و اختلالات احتمالی سفر آماده باشند.»
«آمریکایی‌های حاضر در منطقه باید به ترک آن فکر کنند، یا در صورت تشدید درگیری‌ها برای ترک منطقه آماده باشند».</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/19550" target="_blank">📅 12:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19549">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ویدیویی بسیار جالب درباره روند ایجاد و تکامل ایده ساخت پهپاد لوکاس که مشابه شاهد-136 است اما مجهز به هوش مصنوعی و توان رهگیری بالاتر  https://www.msn.com/en-us/news/other/watch-how-the-us-turned-iran-s-drone-into-a-weapon-used-against-them/vi-AA20tLa9?oci…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19549" target="_blank">📅 11:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19548">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ارتش آمریکا یک یگان ویژه پهپادی در منطقه عملیاتی سنت کام (غرب آسیا) مستقر کرده که در آن از پهپادهای Lucas با طراحی تقلیدی از پهپاد شاهد-۱۳۶ خودمان استفاده می‌شود.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/19548" target="_blank">📅 11:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19547">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">افزایش اهمیت اهرم فشار چین
به گزارش رویترز، با تشدید دوباره جنگ ایران، کشورهای عرب حاشیه خلیج فارس به‌جای واشنگتن، به چین روی آورده‌اند تا از اهرم اقتصادی خود در برابر ایران برای بازگشایی تنگه هرمز و مسیر دریایی دریای سرخ استفاده کند. این وضعیت در واقع آزمونی است برای اینکه پکن تا چه اندازه توان و تمایل دارد تهران را تحت فشار قرار دهد.
منابع کشورهای خلیج فارس می‌گویند تلاش آنها برای ایفای نقش بزرگ‌تر چین، ناشی از افزایش نارضایتی است. جنگی که در ۲۸ فوریه با حملات آمریکا و اسرائیل به ایران آغاز شد، اگرچه به رقیب منطقه‌ای آنها آسیب زده، اما هم‌زمان صادرات حیاتی انرژی این کشورها را نیز محدود کرده و آنها را، با درجات مختلف، در معرض حملات قرار داده است.
سه منبع منطقه‌ای می‌گویند از آنجا که ایران و متحدانش هم‌زمان تنگه باب‌المندب در دریای سرخ و تنگه هرمز را تهدید می‌کنند، کشورهای خلیج فارس از چین درخواست کمک کرده‌اند؛ به‌ویژه با توجه به اینکه جنگ محدودیت‌های قدرت آمریکا را آشکار کرده است.
وانگ یی، وزیر خارجه چین، ده‌ها تماس تلفنی و دیدار با همتایان خود داشته و برای دستیابی به آتش‌بس جدید تلاش کرده است. همچنین ژای جون، فرستاده ویژه چین، با مقامات کشورهای عرب خلیج فارس و همچنین ایران مذاکراتی انجام داده است.
اما این دقیقاً چیزی است که وضعیت به آن نیاز ندارد! هیئت تحریریه وال‌استریت ژورنال هشدار می‌دهد که نتیجه جنگ ایران تا حدی به رفتار و عملکرد قدرت‌های محور مقابل آمریکا بستگی خواهد داشت.
این نشریه می‌پرسد:
«با وجود اینکه آمریکا بخش قابل توجهی از زرادخانه موشکی ایران را تضعیف کرده است، آیا چین به‌سرعت به بازسازی آن کمک خواهد کرد؟ آیا روسیه که به دلیل کمک‌های ایران در جنگ اوکراین به تهران بدهکار است، به احیای برنامه هسته‌ای ایران کمک خواهد کرد؟ آیا هر یک از این دو کشور، سامانه‌های پدافند هوایی پیشرفته‌تری در اختیار ایران قرار خواهند داد؟»
در واقع، نگرانی اصلی این است که چین و روسیه به‌جای ایفای نقش میانجی برای پایان دادن به جنگ، به بازسازی توان نظامی ایران کمک کنند. چنین سناریویی می‌تواند جنگ را طولانی‌تر کند، رقابت ژئوپلیتیکی میان آمریکا و چین را تشدید کند و هم‌زمان ریسک اختلال طولانی‌مدت در مسیرهای انرژی هرمز و باب‌المندب را افزایش دهد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19547" target="_blank">📅 10:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19546">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">CBS News:  آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.  ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19546" target="_blank">📅 09:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هدف قرار گرفتن ۲ کشتی در نزدیکی سواحل عمان در تنگه هرمز</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19545" target="_blank">📅 09:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX175qKMffFJlpMCiqPP1S1ThUIla9_n8aceoUT0BaorQojNYRM60Zz-7McrzAoT2cQpoRlwQcClzhvxP-iQNjY4CK7OyvfuTqTWD0d5tS7VDo2JZE10N1O_iiueHAYdKhVULbXEEiWG9uKBKMsmAvDtPZlnfRzFPKuqcuREXWBo6b9iRbSwPaHAcuQ2bOj9CF5ogFVpg5NZiQjWNSBf8eRDOsOg33HBkkrRNbOSxy2IPyJ9dYoHZTvLZrPJtjFFjPE7-4miMn4RTio4OGP_9HGO_4Tc3ZRHQHgwxxS71SYc98vDfsgfauO4uxpVbK_Br1luRA_rEtWR18-28t2SqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار : آیا چین و روسیه اطلاعات هدف‌گذاری را به ایران می‌دهند؟ این حملات اخیر ایران  بسیار ویرانگر برای نیروهای آمریکایی بوده‌اند.  روبیو: هر زمان که در یک منطقه جنگی مانند الان هستید، خطراتی با آن همراه است. منظورم این است که در نهایت، این واقعاً ثابت می‌کند…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19544" target="_blank">📅 01:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19543">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو خطاب به رئیس جمهور ترکیه:   اردوغان یک دیکتاتور یهودستیز است که مرتکب نسل‌کشی علیه کُردها می‌شود  او که از حماس حمایت می‌کند، مردم خود را سرکوب می‌کند و مخالفان سیاسی خود را زندانی می‌کند، آخرین کسی است که می‌تواند درس اخلاق بدهد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19543" target="_blank">📅 01:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19542">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">CBS News:  آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.  ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19542" target="_blank">📅 01:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19541">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مرندی:  رژیم مراکش صرفاً ابزاری دیگر برای نتانیاهو و ترامپ است. آن‌ها اسپانیا را به خاطر حمایت از فلسطین تنبیه می‌کنند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19541" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19540" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">CBS News
:
آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19539" target="_blank">📅 00:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ:   ایران موشک‌های بزرگی به سمت اردن پرتاب  کرد و قبل از اینکه نزدیک بشوند  توسط سلاح‌های فوق‌العاده‌ای که داریم زدیم: بینگ بینگ بینگ بینگ بینگ بنگ</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19538" target="_blank">📅 23:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📡
استفاده ارتش چین از هوش مصنوعی آمریکایی برای تقویت توان نظامی
🔷
خبرگزاری رویترز در گزارشی اعلام کرد که پژوهشگران نظامی چین با بهره‌گیری از خروجی مدل‌های پیشرفته هوش مصنوعی شرکت‌های آمریکایی «اوپن ای آی» و «انتروپیک»، سامانه‌های بومی هوش مصنوعی را برای تقویت توان دفاعی و نظامی این کشور آموزش داده‌اند</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19537" target="_blank">📅 23:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19535">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e924f93a.mp4?token=PLgxg-mGXsw4F8XeMtkIC3L-AQrBHYv0Uy8UTQA9ezN7fBCJhivzsuJDZn_MOgcxbtLtZFiiY5QbO9cjR_8K3UpqnQZHNe-4FIkOjWqWxETLfawSf9FtU_N6IX2CMJUkRCmD5KZvGAa_ltO-jAAiiaaTajn1cUhP-FZeKzZGGn_I9CaGrhHvl56hiIHMz6ADq80Ub2g4PEhZIw7q6eBQACY4TCyHvfkMrEDzy1dqpabXGZbNoXc0_hvMWiXf995OZ-t26oCy2tfIlAuqyVkLjuN9tZLkPux4TyWGwImGA7txa4WoDuPfsbcCj8ydzWz1_V-PntuRwSOy372m_FdaMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e924f93a.mp4?token=PLgxg-mGXsw4F8XeMtkIC3L-AQrBHYv0Uy8UTQA9ezN7fBCJhivzsuJDZn_MOgcxbtLtZFiiY5QbO9cjR_8K3UpqnQZHNe-4FIkOjWqWxETLfawSf9FtU_N6IX2CMJUkRCmD5KZvGAa_ltO-jAAiiaaTajn1cUhP-FZeKzZGGn_I9CaGrhHvl56hiIHMz6ADq80Ub2g4PEhZIw7q6eBQACY4TCyHvfkMrEDzy1dqpabXGZbNoXc0_hvMWiXf995OZ-t26oCy2tfIlAuqyVkLjuN9tZLkPux4TyWGwImGA7txa4WoDuPfsbcCj8ydzWz1_V-PntuRwSOy372m_FdaMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19535" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19534">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ درباره اوکراین:
تانک‌های روسی در حال حرکت به سمت کی‌یف بودند، اما در گل گیر کردند.
یک ژنرال روسی تصمیم گرفت به جای استفاده از بزرگراه که به خوبی در حال حرکت بودند، از میان گل عبور کند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19534" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19533">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بسنت وزیر خزانه داری آمریکا :
ما در مارس ۲۰۲۵ شروع کردیم. در دسامبر ۲۰۲۵، بزرگترین بانک در ایران فرو ریخت.
بانک مرکزی مجبور به چاپ پول شد و این باعث تورم گردید. اکنون آن‌ها قادر به پرداخت حقوق سربازان خود نیستند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19533" target="_blank">📅 19:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19532">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19532" target="_blank">📅 19:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19531">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ:
شنیدیم که در مینه‌سوتا یک حمله سایبری رخ داده است. آن‌ها آن را به ایران نسبت دادند. من این را نمی‌پذیرم.
من آن را به مینه‌سوتا و فرماندار فاسدش نسبت می‌دهم.
آن‌ها دوست دارند بگویند، «آه، این ایران است. ایران باید خیلی خوش‌شانس باشد.»
ایران مشکلات بزرگتری نسبت به نگرانی درباره مینه‌سوتا دارد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19531" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19530">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">روسیه حدود 30 هزار تن بنزین از مراکش وارد کرده است تا کمبود سوخت ناشی از حملات پهپادی اوکراین به پالایشگاه‌های بزرگ را جبران کند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19530" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19529">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFbBV9g1Qe7dMdywJWlYDSPv13sjRFgZARhGRptMdzOBhu-hSeyXGGnB3wualtFh8xWdAWrowos10X6ce8WHU_rlpWJCIbQlvjHVtsguEouYRngaNKXb_MfEeAuAQku4lv0-IBQKa62_lcp0ZQ4t0M9JkJVoSzbH9NGwJ-2_ft3HXPrE3qgLgik18FZcWr5TyV2913l_Lc_yiZw5Ji2R2hF-Ktq2F1LdQB6Ewd0pUeNkVaCfMuNvoydXZhvMjbwHZRBh8UPs3gkav7-DGy8xOMcG81mvD1nvccVlyeAXNZjxo8Tptq9MAO-TIEt3VdQVlCzD83HT4V4ypX3mlBDc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19529" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19528">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اسرائیل طرح "هیئت صلح" رئیس جمهور ترامپ را که هدف آن خلع سلاح حماس بود، رد کرد. این کشور مدعی است که این طرح برای اسرائیل قابل قبول نیست و اسرائیل هر حقی را برای هدف قرار دادن و کشتن افراد در غزه دارد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19528" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19527">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این اسپانیایی ها 700 سال زور زدند تا عربها و بربرها را از خاکشان بیرون بریزند؛ چپ ها در 2 سال دوباره همه آن کوششها را بر باد دادند!
چپ = نکبت</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19527" target="_blank">📅 17:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19526">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک زن وحشت‌زده در سئوتا درخواست کمک از نیروهای نظامی می‌کند و می گوید: "ما تنها هستیم":  ما به حضور نیروهای نظامی در خیابان‌ها نیاز داریم. آن‌ها اینجا نیستند.  ما تنها هستیم.  چطور ممکن است من نترسم؟ من می‌لرزم. این یک تهاجم است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19526" target="_blank">📅 17:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19525">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19525" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBsMiImuQxhUnBf7nfSGSZqfZ3Q8dEAac_4Ri93LaHLElmbDjDOGjOkWS_6GD3XWWv3cumhimlwZICmtUUicxbhNFjlCpBmicFZbZmbJJqNRZjgg-U4KhYAVOAzSBdxMY59UG6qwYQgbL0wslAEKXdjKW5aoJsuAJO6ejrsUQ021DVlF3ENYhbwfi9XNOVLi89qf7C2OFaEn0-uj2gon9Om0tFlgLMa91OMjPE9Lw_VdByxM3kb6JKIqroXB8uGbnVvLXBw962QWwG5Cz2nEuQhwWokivCANcV0Zx2JmogRvJNzC_qS-JFhBCUM7gaEiwXW5S9fTiP_EYgV7LJVa_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز بسیار بالاست و پیش بینی می شود طلا (و شاخص های سهام) زیر فشار فروش بروند. (خصوصاً شاخص های سهام)</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19524" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ:
"جنگ با ایران به خوبی پیش می‌رود. ایالات متحده ضربه‌ای سنگین به ایران وارد می‌کند و ما به سادگی به پیروزی ادامه می‌دهیم</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19523" target="_blank">📅 17:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19522" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تنگه ای که استراتژیک نخواهد ماند  وقتی گفته می شود ایران‌ استراتژیک‌ است، بخش مهمی از این‌ گزاره به دلیل اشراف جغرافیایی ایران بر تنگه هرمز است. چون دستکم‌ یک پنجم انرژی فسیلی سالانه جهان از آن می گذرد. ولی گلدن ساکس مدعی است که تا امروز ۷ خط برای دور زدن…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19521" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8jgTkbgWNcr0WQM1l2yognYDVwC2m0Nvm4xySJssdsdFVr_Z-Yrv1x81Hq6ifVeLxs1AuoKA0xkua7Lx2hFFJKyEwrp5w-FtzIujes5CjkO6NRrNIl9i5MPmMFOWeRV2r__lgSqmaO4rztyRqQ27AsthUa8ckSC7sMJuYHG01r0WGF3uM-aZko80Oaemxask694TLW-gGO9bzNx4UcMus7u78xMz68euL9Um6GF37gjXqistzu826FCCcrs59GuqDOo93DFjoUYVPHF6U5IspYfZHmAuVAfxDOgpJfMt09fOqrutWiqxtKNCXOsKyvrKBiXXwk9wLrSEGce_pW15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عصر اقتصاد دانش بنیان، تنگه بندی و گردنه گیری تنها منجر به انزوا و تیپا خوردن خود عامل می‌شود و اندونزیایی ها خیلی سریع فهمیدند که این لقمه برای دهانشان بزرگ است ولی خب.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19520" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_0_HoiEw8zB6XCosHiyCq3lWPU0x7JIJrfBYfZR_OURnKdU7lyRVbtNmkZ9ekxXwy3BazWl4R0ms_6tlh6412c32IxA_pKTUMJdui3gF_sgUSHW-4TTWhIl3AexBfg-YCiSVEeEeXX1jKr2mZtVL2pyApy8GS4bug3JzT161ozp6m0uj594SfmNS_NtxQJxWYIS0nSEHa4zqL9uNIMCHkf32FHCim9yWIhfr_PBXayD1JdmOGbSkv1UXXa_7UjRU_8Isl91mxasqWYT24rSFAduV2KdBoEnav61HuxgoCa9GaCgmi8FqQ_XNNOKhNfw3OG3Pj5YklkcWQIhpTgKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید  همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19519" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 16</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19518" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 16
جمعه 31 جولای 2026</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19518" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک کشتی حمل گاز قطری که میخواسته از مسیر تعیین شده ایران عبور کند توسط آمریکا متوقف شد!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19517" target="_blank">📅 14:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ایالات متحده و اسرائیل در حال بررسی محاصره زمینی ایران برای افزایش فشار اقتصادی هستند!  این پیشنهاد به دنبال متقاعد کردن کشورهای همسایه — از جمله افغانستان، ارمنستان، آذربایجان، عراق، پاکستان، ترکیه و ترکمنستان — برای محدود کردن یا بستن گذرگاه‌های مرزی با…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19516" target="_blank">📅 13:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایالات متحده و اسرائیل در حال بررسی محاصره زمینی ایران برای افزایش فشار اقتصادی هستند!
این پیشنهاد به دنبال متقاعد کردن کشورهای همسایه — از جمله افغانستان، ارمنستان، آذربایجان، عراق، پاکستان، ترکیه و ترکمنستان — برای محدود کردن یا بستن گذرگاه‌های مرزی با ایران است تا واردات و صادرات این کشور را محدود کند.
این پیشنهاد در کنار سایر گزینه‌ها از جمله حفظ محاصره دریایی، از سرگیری حملات نظامی یا پیگیری یک توافق دیپلماتیک مورد بحث قرار گرفت.
طرفداران این راهبرد استدلال می‌کنند که انزوای اقتصادی بیشتر می‌تواند دولت ایران را تضعیف کند، اگرچه تحلیلگران اشاره می‌کنند که اجرای یک محاصره زمینی با توجه به مرزهای زمینی طولانی و ارتباطات منطقه‌ای گسترده ایران بسیار دشوار خواهد بود.
— تلگراف</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19515" target="_blank">📅 13:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گفته می‌شود عربستان سعودی در حال آماده‌سازی یک تهاجم نظامی بزرگ علیه حوثی‌ها است که برنامه‌های آن می‌تواند شامل عملیات دریایی در دریای سرخ و حمله زمینی در یمن مرکزی باشد.
این اقدام پس از حملات حوثی‌ها به تأسیسات نفتی عربستان و محاصره کشتیرانی عربستان توسط این گروه صورت گرفته است.
منبع: گاردین</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19514" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
روز دوم تهاجم مراکشی ها به اسپانیا آغاز شد. خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✍🏻
Desert Eagle
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/19513" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=d35wvm5OQyRQHgPFMqCOiLfwYCWEic5RxTUpyXOdlO-X-naNd9xkDu_iMsNuItQhtADCPD0zWALukSRJrzfV24240D_touTxyRuE5YKEKjZKoRwSNd_a6n1_4cRMqcnNKFVemMDeG6p057YSQ52W0bCZ9_2zjSEcwF799qgS0KLyIX7x0H445BT_ggf2c9P5Exah1yUs-REAsog2jtCsP0AWAxiL2IixfAqn1WzG-FK2Rog4BXYjlCx26CRksmIIvDbgSs4n3r-tNbTPTlq_Y_WnnMwDZPf3hnUS9CISPD-FBmRzyoTZ2jJlZWyy4NubarbGmYnbrysnwS59BHc8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=d35wvm5OQyRQHgPFMqCOiLfwYCWEic5RxTUpyXOdlO-X-naNd9xkDu_iMsNuItQhtADCPD0zWALukSRJrzfV24240D_touTxyRuE5YKEKjZKoRwSNd_a6n1_4cRMqcnNKFVemMDeG6p057YSQ52W0bCZ9_2zjSEcwF799qgS0KLyIX7x0H445BT_ggf2c9P5Exah1yUs-REAsog2jtCsP0AWAxiL2IixfAqn1WzG-FK2Rog4BXYjlCx26CRksmIIvDbgSs4n3r-tNbTPTlq_Y_WnnMwDZPf3hnUS9CISPD-FBmRzyoTZ2jJlZWyy4NubarbGmYnbrysnwS59BHc8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روز دوم تهاجم مراکشی ها به اسپانیا آغاز شد.
خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✍🏻
Desert Eagle
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19512" target="_blank">📅 12:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3eQ_QAWFsSpFYd6-KxL8IB-IPjR_206OQE4PldMWelPfMjttSNXHx48bJqNgzDR_YcJe5FQHCTgqJFywRpn0lTnol_F2iGg9xnIO_5ZZ7hBtl0x_g_Zyv45dPuatqqyFb9XA2zNsodG1FYghA-7-zSewKXJ9Rw8nbEhX13RcZaSXL0RAtXlZaaV-MiPqaXzvsQE8cepCm6_PKvpaBxnIGFiA_awuUW7S2FwRVvr_nyB1Nw3X5TAHDvgQCBy88xd7HcXbD-XlC9uS3qzvRmyQ6iB4vm7_YYXbrGB5squBONXYxg-xHNhqqmLdFoee4wVp8Jkcy1GA_zSHguTy8K6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19511" target="_blank">📅 12:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19510">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خب سیگنال پایان موج 2 از 5 دارد صادر می شود:
استاد خوش چشم: فک نکنم‌ دیگر جنگ بشود</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19510" target="_blank">📅 12:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19509">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پلیس:  زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19509" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19508">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پلیس:
زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19508" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19507">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19507" target="_blank">📅 11:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19506">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7gUYvHf2inWeCIUVAm2oMHN5q8uukZXOKSYhoOG0R3So6w68gkZIPYp5rek4d0uar7ClX9iaxVUr1BdlqJ5lDCoBHLS-uNA8KiMXnstAYqkn8LuNBd_2t3-8j634HelGUogVE3P4Ay7u5_GL7aDXTdS-dFIXoavIe2nAmoi8oNolfpibLv9H8xAn_3f-WkRkINyBHjOOQqKW0SUDkMCVC2zvb5BFmtbPwy5Q4V_6jOxvK2v6nlCI_o8Wr5BoPG57Gohs9_mD6FBg3psD5lue6dP7RuJBYpn0BFt0M_tR0DbpioAWRsH8EAduujHwdtqKROkY6IO-g-8q23ju6gKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز بسیار بالاست و پیش بینی می شود طلا (و شاخص های سهام) زیر فشار فروش بروند. (خصوصاً شاخص های سهام)</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19506" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19505">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbh4lRg5jbtclu0oE0ufMaZ5XmFFpSFLs7S75ro5ElTSTNgTZz8Qld9J9GQs7C4zDMhes9kAwxvFR9IN0E8N7TjL7G-YBsrIyrEHTJKrsd4ybXWQhHVmA-RFUdvLt93ZuCFZRCRdJS_SvDzvpSrfTm75bCXX8eGulz1qr2S1P8qPN7KB1e2ZVy_xUPS93ngmH3A9M-zG_8NNy11mL9_VBmVfoQ3Juk3yYr6iK5qzfO8LdQXKH0lLtIyMWhVom-6WEbSOxL7VSV6AOFG1KGZ3Cplb-sSchlz7bpdpAa7S6YiEJfh0VpdxARITa_-z577d1xHYmFDSu_Fah4ePye-MZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19505" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19504">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شلیک موشک از ایران</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19504" target="_blank">📅 10:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19503">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مجری
: آیا می‌دانید چند روس در این جنگ کشته شده‌اند؟ آیا تخمینی دارید؟
زلنسکی
: مجموع تلفات روسیه ۱,۶۰۰,۰۰۰ نفر است و حدود ۷۰۰,۰۰۰ نفر کشته شده‌اند. تقریباً.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19503" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19502">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قالیباف:
ایالات متحده هر روز دست‌های خود را با جنایت جدیدی آلوده می‌کند؛ حمله تروریستی به خانه‌های مسکونی غیرنظامیان در جزیره قشم ادامه‌ای بر فجایع میناب و لامرد است.
آمریکایی‌ها عادت کرده‌اند که با ریختن خون بی‌گناهان، برای ضرباتی که در میدان نبرد دریافت می‌کنند جبران کنند.
آن‌ها بهای آن را خواهند پرداخت.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19502" target="_blank">📅 10:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19501">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ اعلام کرد که حماس به طور کامل سلاح‌های خود را تحویل داده و غزه «در دستان یک دولت فلسطینی جدید که در خدمت مردم خود است» قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19501" target="_blank">📅 02:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19500">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مجری فاکس نیوز:
آیا کشورهای دیگر در منطقه که توسط ایران مورد حمله قرار گرفته‌اند، در حال تماس و تمایل به شراکت با اسرائیل هستند؟
نتانیاهو:
بیشتر از آنچه فکر می‌کنید. بیشتر از آنچه می‌توانم بگویم.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19500" target="_blank">📅 01:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19499">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نصب سیم خاردار روی پنجره ها از سوی مردم اسپانیا برای مقابله با موج سرقت و جنایت مهاجرین آفریقایی</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19499" target="_blank">📅 01:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd_IBG6KdbsBGgfaxi0ghvZNQbgM_-WUBUwK3Oc_ksxVsW5MHRNuJ4d-6g391yw78yi-KFg0456Mm1yiU4MGfT_6Gu9vKp87YEH5zMTboeGwU0pWJFFUA-1csC7Y3hzCwwQosGfOwxjmbHeDJjA47yxbXViC2IWbq2CY_gh9oGpyFaXihxR84hcL_nCAwHM4zwsS2WUsfKZnIGfjBbhSdJ8WRsY0a6Z4j-dBl_PNdVNqW5SYDILTIyjMJI84uz2sj-7jtUUrr-hwx5Uiacuo2SR6xKQNJZZIah6-EnH6veo2PO6YxTTf9-qVGJnBYlfVhLTMEMIKkk49LznVPzkIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19498" target="_blank">📅 01:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">▶️
Snow-like dust covers towns across southern Lebanon following violent Israeli explosions.  @PressTV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19497" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPress TV</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0fce5d57.mp4?token=P81tNJ4USqecZtIHwlechvpUBIqPYEzrBZwKwHU9lwfVw8nlC_kAiNkxlkWSiiCv2LgvxBbALNB7GN4HRGlSRNIPNuc7GKIvStlU0PvnbfsI_4XWngoWou8Jg-jWD7itUO_OnW_v94e3j3eyaDlv-EMxaIJBmWtPx3idCzWnkW_DsWjswIqrza91WG3lUs1C0MAOA0y8YCsTRHqcwqwylJaGWdxYx1Y5CQCHUXQ-0r--EfHwJIA244nLkN-fOMQNRirlMz6grsPZuz3XSCLH84zdtcSII4LoV1jVi8YiPwPdVf5Fx4HwRb6mucg7ZRx3JVyYf6JgUSWjdSv8nhHNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0fce5d57.mp4?token=P81tNJ4USqecZtIHwlechvpUBIqPYEzrBZwKwHU9lwfVw8nlC_kAiNkxlkWSiiCv2LgvxBbALNB7GN4HRGlSRNIPNuc7GKIvStlU0PvnbfsI_4XWngoWou8Jg-jWD7itUO_OnW_v94e3j3eyaDlv-EMxaIJBmWtPx3idCzWnkW_DsWjswIqrza91WG3lUs1C0MAOA0y8YCsTRHqcwqwylJaGWdxYx1Y5CQCHUXQ-0r--EfHwJIA244nLkN-fOMQNRirlMz6grsPZuz3XSCLH84zdtcSII4LoV1jVi8YiPwPdVf5Fx4HwRb6mucg7ZRx3JVyYf6JgUSWjdSv8nhHNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
Snow-like dust covers towns across southern Lebanon following violent Israeli explosions.
@PressTV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19496" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران:  "مصر یک دوست و شریک مهم در منطقه است و امنیت آن برای ما از اهمیت بالایی برخوردار است.  ما همگی باید در برابر توطئه‌ها و عملیات‌های فریبکارانه اسرائیل که با هدف تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.  تهدید آشکار،…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19495" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به نظر می رسد مصر هم کم کم به لیست اهداف مشروع ما بپیوندند.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19494" target="_blank">📅 00:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19493">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عربستان سعودی ائتلاف چندملیتی برای محافظت از مسیرهای دریایی کلیدی را اعلام کرد
عربستان سعودی تشکیل یک
ائتلاف دفاع دریایی چندملیتی
را اعلام کرده است. هدف تضمین آزادی ناوبری و مسیرهای تجاری بین‌المللی در
تنگ باب‌المندب
، در
دریای سرخ
و در
خلیج عدن
است.
بر اساس وزارت دفاع سعودی،
۱۴ کشور
در حال حاضر از این ابتکار حمایت می‌کنند:
بحرین، جیبوتی، مصر، اردن، کویت، مالدیو، پاکستان، قطر، سومالی، سودان، ترکیه، یمن، عربستان سعودی و شورای رهبری ریاست جمهوری یمن.
بر اساس وزارتخانه، سایر کشورهایی که در مشورت‌ها شرکت کردند، در مرحله نهایی رای‌گیری‌های سیاسی داخلی برای پیوستن به ائتلاف هستند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19493" target="_blank">📅 21:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">— منابع یمنی معتقدند که عربستان سعودی در حال آماده‌سازی برای یک تهاجم نظامی بزرگ علیه حوثی‌ها از طریق دریا و احتمالاً از طریق خشکی در یمن مرکزی است تا گلوگاه صادرات نفت خود را در دریای سرخ جنوبی آزاد  کند.
— گاردین |</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19492" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19491">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزارت دفاع آمریکا، قرارداد ۵۸ میلیارد دلاری برای سیستم پدافند هوایی پاتریوت به شرکت لاکهید مارتین اعطا کرد.
این قرارداد به ارزش تا ۵۸.۶ میلیارد دلار، مربوط به موشک‌های رهگیر پاتریوت است و تولید این سیستم را تا سال ۲۰۳۲ افزایش می‌دهد. این اقدام در حالی صورت می‌گیرد که درگیری‌های مداوم در ایران و اوکراین، ذخایر سامانه‌های پدافند هوایی آمریکا را کاهش داده است.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19491" target="_blank">📅 20:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19490">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">329.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19490" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 15</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19490" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19489">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19489" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19488">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">در صنعا توفان و رعد و برق شده، فکر کرده اند عربستان حمله کرده !</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19488" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19487">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رهبر حوثی‌های یمن، عبدالملک الحوثی، درباره عربستان سعودی:
آن‌ها دام‌ها را نابود کردند؛ شترها و گوسفندان. حتی حیوانات بارکش و الاغ‌ها نیز از رژیم سعودی در امان نبودند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19487" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19486">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19486" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19485">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYSHTicc9uigPCXx12wn80chUiRreErYSo1BSE4XB1MN4KXSznK7472EQqI5WOi5Q6V0J0MRNzjmJluM_35FfPnnDAUN3f8HPCO54IDTdmHF0tE-3Cr-HnA5fl-OCyTU1hGYM4wPETgmSKiFycX10YWW6RIQ9fHOEWAqOS_ord78aQiYcYbwPw4bOK2syQY8xhoefLSiCR5tQ_-GJhU6ILBB9YfiQ3Ek_mBAoQW2vsLqs0pbDwGXwPyqXXm-BpZDOWtkINp0eBgYTZhyuLsOVJtHF9K0peyx0Yprk47yVWElcT3hepDF3XFTX7-uZMd3zR4SEv0VFi9fO7fzuEg-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما ببینید در روزهای اخیر اینها به لیست اهداف مشروع ما افزوده شده اند:  — بلغارستان — بریتانیا  — اوکراین</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19485" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19484">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGBgem991w18u-bXqXy9b8t7jagwq6rbKKhGqXNDB-pWYhIGHTo9l2TqkVqQ4mHu-_gv6B4fVLrXm9IXA6fZduoBjAW2o3j9EsSTiAaCUzLQPx9BbA3UnFcuiHH6plO6N079A4bRr0PjF49uJK_q-GRvViswhhXIX2FS2nzemESIHSBc4FYChTPVj2mhBCrmz1tM7rAsL0Zk-Timpzjcf-84PufqTqxi4oN8OdBzLlNm0ZclipVe8WzCRGy-rkgKPSxNJUEG3pCLQd-UdS_zNGWXgPJGDFcGDHAGjdZ2vd_v6Knk6dPVgQa_CR_teSJtS1spfjZkat4wkUVj7JcO0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19484" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19483" target="_blank">📅 18:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">— مشاوران و اعضای کابینه ترامپ گزینه‌هایی برای انجام عملیات نظامی گسترده‌تر علیه ایران را به وی ارائه دادند.
— فاکس نیوز</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19482" target="_blank">📅 18:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سپاه پاسداران: ایران پایگاه هوایی الازرق را در پاسخ به حمله آمریکا به قشم، با نابودی سه فروند اف-۳۵ حمله کرد
سپاه پاسداران انقلاب اسلامی حمله موشکی انتقام‌جویانه به پایگاه هوایی العزرق در اردن را پس از حمله آمریکا به خانه‌های مسکونی در جزیره قشم اعلام کرد.
طبق بیانیه سپاه، این حمله به منطقه استقرار و محل نگهداری اف-۳۵ هدف قرار گرفت و سه فروند از هواپیماهای اف-۳۵ را نابود کرد و سه فروند دیگر را به شدت آسیب رساند. چندین افسر آمریکایی و پرسنل فنی نیز کشته شدند.
سپاه گفت که این عملیات در پاسخ به حمله آمریکا به قشم انجام شد که منجر به زخمی شدن اعضای یک خانواده محلی، از جمله کودکان، شد.
در این بیانیه همچنین از اردنی‌هایی که با حضور نظامی آمریکا در کشورشان مخالف هستند، تشکر شد و گفته شد که موضع آن‌ها فشار بر نیروهای آمریکایی را افزایش داده است.
سپاه در پایان با تأکید بر ادامه عملیات علیه حضور نظامی آمریکا در منطقه، بیانیه خود را به پایان رساند.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/19481" target="_blank">📅 14:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کشته شدن ۳ عضو سپاه پاسداران در حمله آمریکا به زنجان</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19480" target="_blank">📅 14:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 15</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 15
پنجشنبه 30 جولای 2026</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/19479" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19478">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZwOJW3EGjIGe4rST4E1sFyW66rp22YHvZUiqffB-q2OJ3XtWo8y04ym7WON06Ew-lvVMs3U5tfIcTCkAc7ymLhfJHyVhuagfO0uI_qdjWNcI5FWh04eB3y8Sf31Pu9qqAVXwnjGph_mB1h2_Zag9bTW9bDyGCRm1ByOoOObmD7eQ9uJ9xzAzddnyBcmKZ1wK3WlvUUtXxU_Gwd4iM2K8k2-KRSKSbZntESKDcM__RVy3Csu9s_DqQBbptVsi8eWnQzDH2W4V9nm8gXnJCOJV236gWLkVa-HbTX9vPPhV7hUErajB-4v2dMhz5RhvYYBSsXSCrdPWQc2Q8Qif-tP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک نشست دیروز با نیما</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19478" target="_blank">📅 12:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=DzWaxweQmFY4vqufit_8ihVI5IG_OFAYWqEWVqjVaW7eGkiSTu1Fx0pgi6P5Iapzk-qhFaRFfq-talVzYkk9tjnL4NeGJjnatJUzRJiExyO1744UkhJHkBxA3N5zpWsi8WialQf6GbaVygYcV7XgJWlb54YgrdtjDXOoIZVfcScg7t74NOv8hS53bt7t7bV0NEPXYooNrayypPyYMusnw1W3ElYLMw68QnvsnSefisikUkLjXmQSk-w2bNz9YzLJqFWgsIfp_-NX7L3hg9w46j3QUG8ebSGS5lEhiVMP1hDq6gdYXDeFhLer3nnw78n_3Wh3gxfN7svcBcx4O_nhTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=DzWaxweQmFY4vqufit_8ihVI5IG_OFAYWqEWVqjVaW7eGkiSTu1Fx0pgi6P5Iapzk-qhFaRFfq-talVzYkk9tjnL4NeGJjnatJUzRJiExyO1744UkhJHkBxA3N5zpWsi8WialQf6GbaVygYcV7XgJWlb54YgrdtjDXOoIZVfcScg7t74NOv8hS53bt7t7bV0NEPXYooNrayypPyYMusnw1W3ElYLMw68QnvsnSefisikUkLjXmQSk-w2bNz9YzLJqFWgsIfp_-NX7L3hg9w46j3QUG8ebSGS5lEhiVMP1hDq6gdYXDeFhLer3nnw78n_3Wh3gxfN7svcBcx4O_nhTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور موشک های زمین به زمین اتکمز آمریکایی بر فراز شهروندان کویتی به سمت شهرهای خوزستان</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19477" target="_blank">📅 11:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMBn2UGPpWzdcOMBrQWdCOSTssrQ1ifpnmf2QjyDWaO1DQk1eOFpSBHpMTtl0DbOB__4aQUXaN0_rTKF8cX6hRe3aA1_0vqMGH-u_iOmjwdJfDRMtKgx-KdzRNV6RZAvs85ttmHjNW-xpGixWf2yAPvnewtS1MAN3_gpxd9CJAoB43S7IMG7zAZLH89E1hDR2sdmfjjCWKl1NH05niQ2S03YmHm-pflyz68rBLeK-D2vt-ucI8cHqHwgKyxgYyZreVSDgoJf3swW7WpsuHzvCrTz7Fuk7RYXmhhARvnAbxIp3r18ZQs7cs4leZ5gU5JNWD7TmtCJvLjSf_iaS739PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همان حرامزاده ای است که دختران را در لایوهای خودش کتک می زد و به آنها اهانت می کرد که خوشبختانه به این روز افتاده و تا مدتها نخواهدتوانست شرارت کند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19476" target="_blank">📅 11:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTgQypq5TMm7D6WxGpQ_1UHo4sszevLIgYMJJRQRCEuui0XW3m4kL1KdHriKqRXmH8SFxjvVweS0d1qg9U1tsPjvFm-GaUR8nM4TI2eFtlPXLiQmHdzs8OcVsb--j9UuFdzr9lWBIyBMFFdziWU1Fk3yl87iqcjkhhyVw2d_K_fxb4wgsC9iM8wr2hqr6YWXMunq2_iWSmmfWs1HcNiiu0VaXRiuxHEx5pA5aEBAnGPZdjy87KPsR8-HpKEcyFmLDFhUTRC4-huJCBEobxNNYQK6jHmv-pAbea2BsWj34gVSdPvs0KCOtHAdvIpOoslz4-E8iMPe7yTEpR_4IsSJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها چهره سیاسی، حقوقی و عمومی اردنی، نامه‌ای سرگشاده امضا کرده‌اند و خواستار خروج نیروهای آمریکایی از اردن شده‌اند.
آن‌ها حضور آمریکا را یک خطر امنیتی، سیاسی و اقتصادی می‌دانند که این کشور را به جنگی می‌کشد که تمایلی به آن ندارد.
این یک اقدام نادر و علنی است در کشوری که به شدت سرکوب‌گرانه با مخالفان برخورد می‌کند.
اکثر رسانه‌های اردنی از انتشار این نامه خودداری می‌کنند، و برگزارکنندگان هشدار می‌دهند که امضاکنندگان ممکن است به زندان محکوم شوند.
خشم عمومی در حال افزایش است، زیرا ایران همچنان به هدف قرار دادن حدود ۴۰۰۰ سرباز آمریکایی مستقر در اردن ادامه می‌دهد.
آژیرها در سراسر کشور به صدا در می‌آیند، و بقایای موشک‌های رهگیری شده در مناطق مسکونی سقوط می‌کنند.
این هفته، در پارلمان، یکی از نمایندگان به دلیل پیشنهاد تسلیت برای سربازان آمریکایی که در خاک اردن کشته شده‌اند، مورد انتقاد شدید قرار گرفت.
یکی دیگر از اعضا، ارتش آمریکا را به کشتن "کودکان، زنان و سالمندان" متهم کرد.
دولت همچنان به این ائتلاف متعهد است، عمدتاً به این دلیل که واشنگتن سال گذشته ۱.۶۵ میلیارد دلار کمک اقتصادی و نظامی به اردن ارائه کرده است.
اما جنگ بخش گردشگری اردن را نابود کرده است که تا ۱۸ درصد از درآمد سالانه دولت اردن را تشکیل می دهد
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19475" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoTktSxeklVy39ILrMauXT-jOt5sCnQzlIZveqrMF18FELg2HjoXw3xSwMMFTe4E1jvmvCwsIzjOKYC56S7e9V0vb8-QrsxbghG-O4A5ReAIDNrQzlAhjjh0hEajEzaIIE3Gd0grAUWbH4CLUfP9PjZhWwc9vSQu-emp7hdmuOS10Z-Sp2UgBm1zuG-TD184Dv0ki5yucYqst2lMpC6o-ef-jYR0hamkGuO9NL_QqQHwgca0OBu6Tud14_YEA1w_b1lbwJAY1Rgi0ekQvycQUQQ6gym39F-36qyu03SJmU3NfBEUdvMh4tBmx4Hgklzo3lmA_KFcBuH0ZM1FtpennA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف حمله پریشب حمله مشترک سعودی و آمریکا به پایگاه های حشدالشعبی در عراق</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19474" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه پاسداران:
با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19473" target="_blank">📅 11:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fknBiOY3AFV9LwdbAE69KcQMkKe1w5rOVOPVyPXHqho2GhOUg4RhyNRjt3NlWOlj_a3o3iRRsVA8cc_YBgIDHwew8Iyy8ic4pzLdAvwODa8fYhI7zwHBXvwWXJdoa5VPdZpvm05Uebfp6VDIXm7wkUQjfiK3mYMhmFtejsIFf96dLNMYiqzcPjAIFY3csywI7xdDVGd4_0k7rWYuwiGi86r6lugeIC7ZESnUziw59tjCl4l4sPHIK3hEBXP4olAoBYs4Yazaic52RV1jsHqpWDTyN3wUc4WuP96kQLgvhWjJOOJl0_sUpJcESdGRz_27rVyOtnGbq90w2c5NXtSmOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19472" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19471" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پرسش: اوایل این ماه، رئیس‌جمهور ترامپ در مصاحبه‌ای با یک خبرنگار گفت که در رابطه با شما، همه می‌دانند که چه کسی رئیس است، یعنی خودش. او کسی است که تصمیم‌گیری‌ها را انجام می‌دهد. آیا شما هم این‌طور فکر می‌کنید؟
نتانیاهو: خب، شما می‌دانید که در آمریکا اغلب می‌گویند ترامپ هر کاری را که من می‌گویم انجام می‌دهد. و در اسرائیل، اغلب می‌گویند من هر کاری را که او می‌گوید انجام می‌دهم.
و گاهی اوقات، این مسائل توسط هر کسی، از جمله رئیس‌جمهور، در بحث‌های عمومی مطرح می‌شوند. اما حقیقت این است که ما شرکا هستیم. ما متحد هستیم.
او شریک ارشد است. این کشور ایالات متحده آمریکا است. بیایید این را فراموش نکنیم. و من شریک فرعی هستم، اما من نخست‌وزیر اسرائیل هستم.
و وقتی لازم باشد، من برای دفاع از منافع کشورم و امنیت کشورم، این کار را انجام می‌دهم.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19470" target="_blank">📅 10:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو:
ترامپ اساساً سه گزینه پیش رو دارد: اول، دستیابی به یک توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
هر چیزی که منجر به پایان برنامه هسته‌ای ایران شود، چیزی است که ما می‌خواهیم. این هدف مشترک ماست.
س: وقتی با ترامپ در کاخ سفید ملاقات کردید، آیا تلاش کردید او را متقاعد کنید تا حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک تصویر کاریکاتوری یا تصویری اغراق‌آمیز است. این درست نیست.
ما در واقع تمام سه احتمال را بررسی کردیم، و من فکر می‌کنم که این کار را به صورت شفاف و در بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19469" target="_blank">📅 10:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت  احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19468" target="_blank">📅 09:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فیلم سنتکام از هدف قرار دادن اهداف در حمله بامداد
چند پرتابگر متحرک نیز دیده می شوند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19467" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19466" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت
احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.
احمد نفیسی خاطرنشان کرد: جزئیات تکمیلی این حادثه و وضعیت افراد گرفتار، پس از پایان عملیات امدادی و ارزیابی‌های میدانی اطلاع‌رسانی خواهد شد./ایرنا</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19465" target="_blank">📅 09:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19464" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19463" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حمله به آبادان</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19462" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGHI_5PQik5KCKsjkqF0aYwcwCidSPDSvaEMu9Q7kndj6yUach-KjnXK35KzDJyGRDtrz_MW97YwzIH6SjnV0Y8ylpfGKcktizVtXpg-y_ITYiXD1ZuF5R2_SFUtm8Q34cFpx0tH2xr9lQcyR93OotiqcYEFL3R1nzelpETjLdTXlWK1tG1Wrcl8A-a88OdiSEqQuYj8mHm0ZoO1rmTQpTZUfXMY4zqspWgMkLdxg3z-pa6sKkuV2YINvnPLBQAK5BEJg5d1ahL6-XZqERWn_X_BJHBPGs7d5hY7V0KS40dGbolAH3T1CNr1ESV7dRn3w4GKlTTAhAVR3VHjIdmxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا تایید شد</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19461" target="_blank">📅 02:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چندین انفجار در ریاض، عربستان سعودی، و بسته‌شدن باند فرودگاه پادشاه خالد در ریاض.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19460" target="_blank">📅 01:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجار در اردبیل و ارومیه (تایید نشده)</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/19459" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZHch9DlK86COOA6c_7v8wW5bm5_m4wFLj_BKCywDss-rNb9yeAZQ2E9Ssqo5IhkBtlGqI-DQhQPRa26sBdUIFilg_bAZEwZiFkrT435T1qE04Vx3PPE5yCBe3CLcbL5YVxokeIuHYY-d0gRe2gmTwzPshkgDPl2Fd1RtsKuTWL0em9QjdGfhm960RPRgt7tGMpwn2Vn2tOaAuzfxDJGYHtqzqTqcYbYnFbLTM3DL3IIW9x1iisale6wERxxC_DUGSjtEX-cA6GOIGXESPpxnZ4EEx7uQDXDyxnSTwjjJy6tKoK97R3Gx9MJvMriFbfVL_wAzIQ3bPSUNoPoQwuEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/19458" target="_blank">📅 00:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi7JUYAuBJP2ic0wWqZeTCNMCG9mW1WfCDiHLcYLnmNJmO8XQpIt3-JN0EQTeoDwVgEneXaL9Y9ZsrtNSu-a8x7jxUEyprmJv58U_mrHzXDdKdpDv-ywFVVpR1AiKJt1fcsSnACKWALsOHSC0uk39scV1z4X4Y24tqS-JdwNyfrsOIgg698xbhZDzvxkZXHhttQiQy5MuoomphZT7M_bLQ3QBKDTquHirMtYnZiG_uiMNYcYl6XeJOKjS-o82rYxKSOJCdQCjva6jXZh3AMh6CMbsS2-CBFS_2FeKX7zzKN5t-JGS5viNyxT3zZR9fMb-6Z5rhOYuhmC5JC5cp8vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19457" target="_blank">📅 00:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN4ZQ4cjAQ0R3utizw_uw0__JUjGHDJj8vcW20558UiWF_pvOlJsSpDSJkWogYu-BIlzrWs3CJu1yzcDGcKGB5D2fxyUBcnR7bWrxTQkY7gi1sX5sdQvpKsc7Jo4N0PEGCqcfpRRBqU6TiqDaqOKHvnyYTvaBG_WNoph8XLRqY_mDN9C_3EVuqPuiWMuo2qHgFFig7EF1niLW3OGhCUe-0hj5eMOfwlhPdHJYBxp3fTtQJ_vKz9i2wHsn63eLlCv3E6bxdt6LsC1kT8gEqVe8laebuiSMADN39OO3MFc5zdj9KWQMy4X4HAHQ58Xp3wahfWSNYzXlDafZPkFqlP0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدوارم آن یک هواپیمایی که نزدیک تهران است جنگنده نیروی هوایی ما باشد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19456" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر
به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19455" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
