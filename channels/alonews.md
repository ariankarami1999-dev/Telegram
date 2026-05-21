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
<img src="https://cdn4.telesco.pe/file/GH370c3CoXfxxNOC_9z81wb50K6ayQ_3evKGfxtXiDv1_rvqF-b45Yp-8xjtB9z0ruJAaI_DXJzQ6eMQ17ZkyaSyaWwhkgDuOD5fM7wjVsDJbyampl6_ofJUxN1Le77qIgppXOXodv5EYvJ9iRqztQKo8fQ_QGb_y9ZG0468Ysn-5pz78RGerWQyZGEsyIOZT1HzQjeSWt5fgXcUMUNixH-QgoPuDbwfHcuf3cc_GjdtQg2TcXJudnGiKqmwH8s5lkFIg41KqgDktoxHjiAV7nvRjKt6klU0k5nMk24fo1qYnVq0-GJ6IZdMFVUbtVvvG_4QOcJ-YEtKS_RjIumGtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 944K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 14:03:13</div>
<hr>

<div class="tg-post" id="msg-121519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d126d72a1e.mp4?token=q1I8s7w-6b9krD7-tMFovXSw4xxORDmSzAIxsK8cRSweowuWOy1slggwfH3fNlkBdnfUDmmP2RMyDuGajch_LpM6K-yooGHzogZTAMofMkpCBa1M-qjGKKsKJ8LYm9YBYCEL6WOfvqtFN7cyPyOO0BvczmvyHZ8qm_n04nAeTMbC65Yzxlv-d3yjsJOugx_6FgE9Iy3XcZ8toRHTJ22x_X6mRtMtRb-qTmhFn57CZr4wLFxqp9b4fgCfCZFYiKLoRNLhmuEXnn4GptVsRy4WJS83lx3OmIZQ6W1sWquhI2r5EdR73gilCiu1o6oTnqoa2eyzvyFKtH4obBicuAcPxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d126d72a1e.mp4?token=q1I8s7w-6b9krD7-tMFovXSw4xxORDmSzAIxsK8cRSweowuWOy1slggwfH3fNlkBdnfUDmmP2RMyDuGajch_LpM6K-yooGHzogZTAMofMkpCBa1M-qjGKKsKJ8LYm9YBYCEL6WOfvqtFN7cyPyOO0BvczmvyHZ8qm_n04nAeTMbC65Yzxlv-d3yjsJOugx_6FgE9Iy3XcZ8toRHTJ22x_X6mRtMtRb-qTmhFn57CZr4wLFxqp9b4fgCfCZFYiKLoRNLhmuEXnn4GptVsRy4WJS83lx3OmIZQ6W1sWquhI2r5EdR73gilCiu1o6oTnqoa2eyzvyFKtH4obBicuAcPxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان، رئیس جمهور ترکیه : ما همیشه از صلح و ثبات دفاع می‌کنیم و جلوی کسایی که روی جنگ و هرج‌ومرج سرمایه‌گذاری می‌کنن می‌ایستیم
🔴
تو غزه لبنان و جاهای دیگه منطقه کسایی که زن و بچه و پیر و جوون رو بدون رحم می‌کشن ما مقابلشون می‌ایستیم
🔴
از ارزش‌های مشترک انسانی دفاع می‌کنیم تاریخ هم پر از اینه که دوستی با ملت ترکیه سود داشته و دشمنی باهاش ضررهای زیادی داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/alonews/121519" target="_blank">📅 13:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
معاون وزیر نیرو: به ادارات پرمصرف برق، اول اخطار داده می‌شود و در صورت تکرار و رعایت نکردن، فهرست اسامی مشترکان پرمصرف برق به صورت عمومی اعلام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/alonews/121518" target="_blank">📅 13:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بندرعباس لرزید
🔴
دقایقی پیش زمین لرزه ای به قدرت ۴.۶ ریشتر بندرعباس را لرزاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/alonews/121517" target="_blank">📅 13:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121516">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کامران یوسف خبرنگار اکسپرس تریبون پاکستان: پاکستان در تلاش است اختلافات بین ایران و آمریکا را کاهش دهد. با توجه به اینکه دستیابی به یک توافق نهایی ممکن است بلافاصله میسر نباشد، اکنون در حال بحث بر سر یک راه‌حل موقت هستند.
🔴
این توافق، در صورت نهایی شدن، به هر دو طرف اجازه می‌دهد به طور رسمی به جنگ پایان دهند، در حالی که مذاکرات درباره مسائل اختلاف‌انگیز ادامه پیدا می‌کند.
🔴
نقطه اصلی اختلاف برای توافق موقت، وضعیت تنگه هرمز است. آمریکا و سایر ذی‌نفعان خواهان بازگرداندن تنگه هرمز به وضعیت اولیه (پیش از جنگ) هستند.
🔴
ایران معتقد است در صورت بازگرداندن وضعیت این آبراه کلیدی، ممکن است اهرم فشار مهمی را از دست بدهد.
🔴
در همین حال، فرمانده ارتش پاکستان قرار است روز پنج‌شنبه به تهران سفر کند.
🔴
هدف سفر او یافتن یک راه‌حل عملی خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/alonews/121516" target="_blank">📅 13:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121515">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نتانیاهو: اقدام اسرائیل در توقف ناوگان غزه درست بود اما رفتار بن‌گویر قابل قبول نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/alonews/121515" target="_blank">📅 13:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121514">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
دولت پاکستان توقیف  کشتی‌های ناوگان جهانی «صمود» توسط نیروهای اسرائیلی در آب‌های بین‌المللی و بازداشت خودسرانه فعالان (از جمله یک فعال پاکستانی) را محکوم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/alonews/121514" target="_blank">📅 13:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرگزاری آلمان: کمیسیون اروپا به دلیل جنگ علیه ایران، پیش‌بینی خود از رشد اقتصادی اتحادیه اروپا در سال ۲۰۲۶ را کاهش داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/alonews/121513" target="_blank">📅 13:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121512">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAFmAr4bI6uj4L-Z0RKLNQEtrplbCAnjk7qR8FenZ-QwJ5ZQHuKry5kig_H2Wt_uEi_svqv-yI2Nb1digE3-15ls-Clhdz48DUsZeHwvzeNGvD7soKLV1ba9KoXSVxw2zM4aTzgkEseVLT7PPyUhuyGUHUKM9hluL_rUAQRfaoe_4KmLNe26VGldjbXB7oqVBYGJeAGziVTixvi_AL4IxHvRFheb55JE3T8s_i4H10X__HY7MRMDR15gJLWhQNUXWjqqvTpDB2JlppmxoAVHv3P4r1wa9mM3FeFuVHST56F_Ad4k02TX1jkLEFSe3BfXUpm67B98RqnWHBHqGKpS2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ،  این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/121512" target="_blank">📅 13:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121511">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
داده‌های کشتیرانی LSEG و مؤسسه کپلر نشان می‌دهد سه ابرنفتکش حامل ۶ میلیون بشکه نفت‌خام قطر، کویت و عراق، پس از بیش از دو ماه انتظار، از مسیر ترانزیتی مورد تأیید ایران عبور کرده و راهی بازارهای آسیایی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/alonews/121511" target="_blank">📅 13:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121510">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d52e08826.mp4?token=SYn9rsvLVJMYllRLzFT1aBciC8NXrp_vzGN7y1bn6vCpjBUx9xVjp9QZBjjyiWJGrabG24r7gw5UFtYO0iud3BCue6MPUHN_mN7B0OW1ekBgttg8EC0b45JpvBggjWJv2s-5grRUGjgZ7Yd_bzOZqob6tlRd-nT79aMWqu-s63jp33YJvQPL6psM5wo-ZsInUpmcGV6wookYqjVrcsuPkdIfLkZgkJY_7Qv94c-M_Rfgr9UPxELzdy4jVXaqiT2-xiqCpqHXaSeaKtD9Xgmn5OqD1UHHCwkHA4ArJa56pMsZIbSTdh0YEggcc0Y1T-KHUvt-o6OUHvF4POR8gyySyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d52e08826.mp4?token=SYn9rsvLVJMYllRLzFT1aBciC8NXrp_vzGN7y1bn6vCpjBUx9xVjp9QZBjjyiWJGrabG24r7gw5UFtYO0iud3BCue6MPUHN_mN7B0OW1ekBgttg8EC0b45JpvBggjWJv2s-5grRUGjgZ7Yd_bzOZqob6tlRd-nT79aMWqu-s63jp33YJvQPL6psM5wo-ZsInUpmcGV6wookYqjVrcsuPkdIfLkZgkJY_7Qv94c-M_Rfgr9UPxELzdy4jVXaqiT2-xiqCpqHXaSeaKtD9Xgmn5OqD1UHHCwkHA4ArJa56pMsZIbSTdh0YEggcc0Y1T-KHUvt-o6OUHvF4POR8gyySyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع بریتانیا اعلام کرد که جنگنده‌ سوخو۳۵ روسیه چندین بار و به طور خطرناک دو هواپیمای شناسایی بریتانیایی را بر فراز دریای سیاه رهگیری کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/121510" target="_blank">📅 13:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزارت خارجه روسیه: بحران ایران تنها از طریق کانال‌های دیپلماتیک که منافع ایران را در نظر بگیرد، قابل حل است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/alonews/121509" target="_blank">📅 13:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عضو شورای عالی فضای مجازی: رئیس جمهور نتوانست مشکل قطع اینترنت را حل کند، معاونش هم نمی‌تواند!
🔴
«محمد سرافراز»، عضو شورای عالی فضای مجازی، تشکیل ستاد راهبری فضای مجازی برای حل مشکل اینترنت برای حل مشکل قطع اینترنت را بی‌فایده دانست و گفت:
وقتی رئیس جمهور نتوانست مشکل قطع اینترنت را حل کند، معاون ایشان هم نمی‌تواند.
🔴
رئیس‌جمهور هم نخواسته و هم نتوانسته از اختیاراتی که در قانون اساسی پیش‌بینی شده، به طور کامل استفاده کند و به سوگندی که برای اجرای قانون اساسی خورده، به نظر من پایبند نبوده.
🔴
مسئول نهایی قطع اینترنت و سیم‌کارت سفید و اینترنت طبقاتی کسانی هستند که در بالاترین رده‌های حکمرانی تصمیم‌سازی و تصمیم‌گیری می‌کنند ولی پاسخگو نیستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/121508" target="_blank">📅 13:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر دفاع روسیه: ایران تنها کسی است که سرنوشت ذخایر اورانیوم خود را تعیین می‌کند و روسیه آماده کمک به تهران و واشنگتن در اجرای راه‌حل‌های احتمالی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/121507" target="_blank">📅 13:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouxOeYuIaEu0HMGwQoCISsQDnG0v7i8bOrVD5uqgxREJ-qesC1RQtRYW3WtncFhWyHoErkw3D9FH245-1w0B23TeIrIuAlqNX2cgFQ_McZIJq74N6pzURWWnPejYwvVTyyAjburjaArTuPnQYvH3ClIS7k8Lri8TgA6PlnEQmGHZkLMNZ6GtdA7VwttI-bwau3kbhJjTGW2HYnbojwGN1gTanTCuExXwt1xjm5PzI18GZdC1BrJJ2Q3CGtRT_XYafsPxMFNrCA9y9Hrwh2L0WLxIPmhS1d6jY59eMUJsV9heLHkjRO_gfRWyeHmSeTaOmtrdE3MFjaF_v6ZqMxrluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی تا حدودی متن توافق احتمالی را منتشر کرد ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121506" target="_blank">📅 13:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121505">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سفیر ایران در پاکستان: من صمیمانه قدردان اقدام انسان‌دوستانه و خیرخواهانه دولت محترم پاکستان در پیگیری آزادی ۲۰ ملوان ایرانی هستم که به دلیل توقیف کشتی‌شان در آب‌های سنگاپور در وضعیت خطرناکی قرار داشتند.
🔴
در این رابطه، مایلم از تلاش‌های خستگی‌ناپذیر جناب نخست‌وزیر محترم، محمد شهباز شریف، و وزارت امور خارجه پاکستان، به‌ویژه جناب آقای اسحاق دار، معاون نخست‌وزیر و وزیر امور خارجه محترم، و دیگر نهادهای مرتبط تشکر کنم.
🔴
این ملوانان پس از تلاش‌های دیپلماتیک از سنگاپور به اسلام‌آباد منتقل شدند و چند ساعت پیش به میهن عزیزشان بازگشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121505" target="_blank">📅 12:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121504">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری / یدیعوت آحارانوت به نقل از یک مقام امنیتی اسرئیل: ما ممکن است جنگ‌هایی را با سرعت بیشتری علیه ایران آغاز کنیم تا تهدیدی ایجاد نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121504" target="_blank">📅 12:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ورود ناو هواپیمابر «نیمیتز» به کارائیب همزمان با تشدید تنش‌ها با کوبا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121503" target="_blank">📅 12:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع پاکستانی:
مقامات ایرانی از پاکستان خواسته‌اند تا مهلتی برای ارزیابی و بررسی معیارهای آمریکایی برای مذاکره دریافت کند.
🔴
اورانیوم غنی‌شده، گره اصلی در مذاکرات آمریکا و ایران است.
🔴
فرمانده ارتش هنوز در پاکستان است و سفر او به ایران بستگی به نتایج سفر وزیر کشور دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/121502" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/882a666404.mp4?token=WiZi3x195w0IYvfEzyguP-NS7rLLqkhXcDVuxh2w2yGvl5aXMMfNoggBMcXQjCjNSBuN4vNSeELnzcz3XnZL4zAqFL2FXLgKQLACS2Jnx78F2W41aed65UTvYWrpLXpuEMLdr-lutHqywE7OItD_StO-o8ijlZ30ndPRQ1RKsS6Zx1wXomLRBbxZ-K3eyxUwhnLMMkzvKNKIxtVTn9CMnARCebzLuSv9D64aYYVDqzV7tX81TB85pJO2Rg3pBFL3TJaGCVIcudQfdTKpLwEthbJUVyeMoMx0aQXCKWYMCALrEbhrCTE8HeOf7SbibvfbdsFdWttnlPTsc_GenaqE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/882a666404.mp4?token=WiZi3x195w0IYvfEzyguP-NS7rLLqkhXcDVuxh2w2yGvl5aXMMfNoggBMcXQjCjNSBuN4vNSeELnzcz3XnZL4zAqFL2FXLgKQLACS2Jnx78F2W41aed65UTvYWrpLXpuEMLdr-lutHqywE7OItD_StO-o8ijlZ30ndPRQ1RKsS6Zx1wXomLRBbxZ-K3eyxUwhnLMMkzvKNKIxtVTn9CMnARCebzLuSv9D64aYYVDqzV7tX81TB85pJO2Rg3pBFL3TJaGCVIcudQfdTKpLwEthbJUVyeMoMx0aQXCKWYMCALrEbhrCTE8HeOf7SbibvfbdsFdWttnlPTsc_GenaqE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رامی گرا رئیس پیشین سرویس اروپای موساد: کل این داستان غیرقابل باورست. احمدی‌نژاد هرگز به عنوان یک رهبر انقلاب معرفی نشده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/121501" target="_blank">📅 12:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121500">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
منبع پاکستانی به الجزیره :  گره اصلی مذاکرات آمریکا و ایران سر اورانیوم غنی‌شده‌ست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/121500" target="_blank">📅 12:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
تایمز اسرائیل: ایران در جریان آتش‌بس از فرصت برای جابه‌جایی لانچرهای موشکی و آماده‌سازی برای دور جدید درگیری استفاده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/121499" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بر اساس گزارش‌های تایید نشده،
عربستان سعودی از دولت ترامپ خواسته است هرگونه اقدام نظامی علیه ایران را تا پس از عید قربان به تعویق بیندازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121498" target="_blank">📅 12:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlaH0bzsVBN237RXTznnTeM2G6yQZA9oqLLmZzgLgLKHTyquNIyEJEq-vQig3MqjgcI_EpV1yd22dgkAlc9C1evq7lnVAHwN2WM0AJe4Lzz76bjxwFHByLO-GvwlynleRV0FSlTdFWlhHapeIFIE1NYxcXGKKH593RfF-O9fywDdilS2TdPkVjMk3Zvhb6dA4Cz0c132DYqkuIFNV7YCqi9Etrpv5iT9jloLX5GsMiBGg4UirCjE0thtfGSrXMSW-xULnniOrvS-grTLHJUBlQnFLTKYNfkhF8eW1LsFdaUjk5ghKqAtH7UerAvfkJS2ix5W1rksjRNPuFljeu-QtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست به چین سفر می‌کند
🔴
به گزارش SCMP، پنتاگون قصد دارد ظرف چند هفته آینده یک هیئت عالی‌رتبه را به چین اعزام کند تا مقدمات سفر احتمالی پیت هگست را فراهم کند.
🔴
این اولین سفر یک وزیر جنگ ایالات متحده به چین در تقریباً هشت سال گذشته خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121497" target="_blank">📅 12:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ایسنا: ایران در حال پاسخ به متن ارسال شده از سوی آمریکا است
🔴
متن ایران در حال گفت و گو‌ در تهران بر سر چارچوب کلان، برخی جزییات و اقدامات اعتمادساز به عنوان تضمین است.
🔴
متن ارسالی به میزانی شکاف‌ها را کم کرده است اما کمتر شدن شکاف‌ها نیازمند پایان یافتن وسوسه جنگ در سمت واشنگتن است.
🔴
ورود ژنرال عاصم منیر به تهران، به منظور کم کردن این شکاف‌ها و رسیدن به لحظه اعلام رسمی پذیرش یادداشت تفاهم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/121496" target="_blank">📅 12:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع دیپلماتیک: تهران در حال بررسی متن آمریکایی است و هنوز پاسخ خود را ارائه نکرده است.
🔴
واسطه پاکستانی در حال تلاش برای نزدیک کردن دیدگاه‌های ایران و آمریکا است.
🔴
کار بر روی چارچوبی برای یک توافق موقت بین تهران و واشنگتن در جریان است.…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/121495" target="_blank">📅 11:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
صدای انفجار در منطقه سوران در استان اربیل، شمال عراق شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121494" target="_blank">📅 11:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع دیپلماتیک:
تهران در حال بررسی متن آمریکایی است و هنوز پاسخ خود را ارائه نکرده است.
🔴
واسطه پاکستانی در حال تلاش برای نزدیک کردن دیدگاه‌های ایران و آمریکا است.
🔴
کار بر روی چارچوبی برای یک توافق موقت بین تهران و واشنگتن در جریان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121493" target="_blank">📅 11:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
المیادین: چین اعلام کرد که نخست وزیر پاکستان از 23 تا 26 می از این کشور دیدار خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121492" target="_blank">📅 11:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121490">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JT8KARNo8Or4YPd4zrXdC4CKp_zvYQCGZww9FL_r4-rkKfYYP4Kx9FBSYFc6and9gd_Udiybra_v8MnokZubXQvbBMwTh7FoiH51dJCsnK5-Mri2t2dR2DGdiy-cruN0eKUi2JWw3CQSHAQ_Wv8NcJg1cMnWjMp-fK8Qc02E6vVTgMa-JzlC0LCg_NNDNPW1UtpRZF5gsYHYo4FSD0PLguBWgkpDPOMeSoX9mIXNFsXzffEBUMh7Cm2g5nUUQg_SI99xWtFlBl-Zt8TbW2gxPnBibUmqiprRHNO7a0E90RRJI60vZLdHw-1Z9I2GpC-Iawo1_h7kQyx41y42_TcVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kPcJQEAKPfOyPgtkHMA-mOZ_2KgdTQGQi9ZTPZgdK2hWxq_d96zgjyzpUpN8mbyU82Dg37g6pb9YJSQpVpxgjauEl08h3gDylQAzJJec65J2m-hBdSG0d96zEJyNL2oaxS68Iq78g_3xHL2tp157r4ijxn_B6VQqNpxuWAim2hehKrxNXAknULJ-QDFdhC5I5WYIzLXBXx9buUR_poLfZbbCNXJPkrJMazGlkkeK0ZnhFN2rYTS4OVY-xnXcjrxJxtDl6Gh-RoSAUVvhpYdzOtMfJknanzrE97X2XdEpy_4mmiJX0hcksUlAHG3kIGdJBLnTkCBXliKi2XTAMrTsQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوش مصنوعیِ بله عالیه، حتما استفاده کنین
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/121490" target="_blank">📅 11:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121489">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
مخالفت بنیانگذار سپاه با تسلیم سپاه
🔴
محسن سازگارا که خود از بنیانگذاران سپاه پاسداران انقلاب اسلامی است و سال‌هاست در آمریکا به همراه خانواده خود زندگی میکند، در این مصاحبه با تسلیم سپاه که ایران را اشغال و زمام امور را در اختیار دارد، مخالفت نموده!
🤔
زندگی…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/121489" target="_blank">📅 11:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121488">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
امروز هشتاد و سومین روز قطعی اینترنت تو ایرانه، بیشتر از ۱۹۶۸ ساعت ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121488" target="_blank">📅 11:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سایت عبری والا: منابع اسرائیلی می‌گویند آمریکایی‌ها در مذاکرات با ایران یک قدم به جلو برداشته‌اند، بنابراین برآوردها این است که حمله‌ای به ایران در ۲۴ ساعت آینده تکرار نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121487" target="_blank">📅 11:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8042b1a87.mp4?token=Mtf1a0f02TcvojlTEuulSbetCQJUYxx0fThGAECkL9JtkRah3Qh4Bbgxld8ePgufy77UqfK1m-R6wxRw0zbUijZMmq2FZadOqMF0P-pEpRu6DnpT4bHyTG8h7HnW0W59gXX39vt__bm5gV0ZtFsOOTr6_MTwucH7U46CoF2KBsBDMmeS7j_DdXQH4Be1zKyTfiiaONKQe5H9vr9Z0CkM3HmTvenCgKqf3A6qIelsHQudWcl3jUKfpw-ZbifeFFS9ILwDR9B6W6MTPpMPLTfgOdLquHwyPZTjNw2vMzvfoQIOUGxhd9IxKypfeA5fwCq6B4yKS5bwOVfz74GzJLtdEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8042b1a87.mp4?token=Mtf1a0f02TcvojlTEuulSbetCQJUYxx0fThGAECkL9JtkRah3Qh4Bbgxld8ePgufy77UqfK1m-R6wxRw0zbUijZMmq2FZadOqMF0P-pEpRu6DnpT4bHyTG8h7HnW0W59gXX39vt__bm5gV0ZtFsOOTr6_MTwucH7U46CoF2KBsBDMmeS7j_DdXQH4Be1zKyTfiiaONKQe5H9vr9Z0CkM3HmTvenCgKqf3A6qIelsHQudWcl3jUKfpw-ZbifeFFS9ILwDR9B6W6MTPpMPLTfgOdLquHwyPZTjNw2vMzvfoQIOUGxhd9IxKypfeA5fwCq6B4yKS5bwOVfz74GzJLtdEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : اگه ما نبودیم آمریکا اصلا به وجود نمیومد
🔴
ما شما رو آوردیم تو این دنیا و هر وقت بخوایم میتونیم ببریمتون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/121486" target="_blank">📅 11:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رسانه‌های عبری: فرمانده گردان ۴۰۱ که در لبنان به شدت زخمی شده است، پس از اینکه تحت عمل جراحی برای خارج کردن ترکش‌ها از سرش قرار گرفت، هنوز تحت بیهوشی و تنفس مصنوعی قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121485" target="_blank">📅 11:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121484">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
زمین لرزه ۴ ریشتری بامداد امروز فراشبند در استان فارس خسارتی در بر نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121484" target="_blank">📅 11:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خبرگزاری CNN:ایران با سرعتی فراتر از پیش‌بینی‌ها در حال بازسازی پایگاه صنعتی–نظامی خود است و تولید پهپادها را نیز از سر گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121483" target="_blank">📅 11:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یدیعوت آحارونوت به نقل از یک مقام امنیتی: باید جنگ‌ها رو سریع‌تر علیه جمهوری اسلامی راه بندازیم تا برنامه هسته‌ای و موشک‌هایشون دیگه تهدیدی نباشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121482" target="_blank">📅 11:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922df6f8eb.mp4?token=e_sV67cyH1xT8pohaU-YsFFkpS0STI65U74doE6fdduApTjMeP2w-V6YZKtUy6Dcc5fqs8HU5nQb_vNZ-hSWjyPMCl1dvlEaTZ3ia0sOJ2WuJp2Od5aFHr6t2E1J7MT46RlkKQMbQUiGO_-P5ALNoKHtEtFWW9QIDgMs58NCPK4ODnM80XS2LAstMKbINpDzg063l81w1U3fl3ePM5VRKs0nFNxDMMgEoz2d7UkwvcQOUhq1veQB0pFzjqVn0XrWEFd5sqJsZxVa3ebPladGfIVXjlWy9sjwty7Obgy71b_iVAa6ZdLBtkNiETJ7tjJAsJla8bCK_c2Oy9NnwLcCB4tbNYvLLJAfk_mbkCIBr16dlMe7IXOx51K1Daw2qdwe-FoD5r3uLWEiY9x2dybWFALCBWBe6qCo7LKacIvLqJEUWyPEEujGVti7NDfM-bPsSfh8x5y8sfMLyddisSRiuEL9J00FDkwBQDjrhiJdipyfeIRdQ27b9qvtbyoQZDXq_khHg1UTSbsdQNB7Dn6sG-hzBHX4eKMyy8FTRCe4HVIu9b5Kz7qhwjM2AmGCwW65uNW1BMmRt0QPLqA761UM7YkRg32HH2SC77r1g3iM2MgM_L_t3y65pyA4yyOlti07BjdMutl8xeyA3rv_QQoumImShbus5l9E3szX2y7CWy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922df6f8eb.mp4?token=e_sV67cyH1xT8pohaU-YsFFkpS0STI65U74doE6fdduApTjMeP2w-V6YZKtUy6Dcc5fqs8HU5nQb_vNZ-hSWjyPMCl1dvlEaTZ3ia0sOJ2WuJp2Od5aFHr6t2E1J7MT46RlkKQMbQUiGO_-P5ALNoKHtEtFWW9QIDgMs58NCPK4ODnM80XS2LAstMKbINpDzg063l81w1U3fl3ePM5VRKs0nFNxDMMgEoz2d7UkwvcQOUhq1veQB0pFzjqVn0XrWEFd5sqJsZxVa3ebPladGfIVXjlWy9sjwty7Obgy71b_iVAa6ZdLBtkNiETJ7tjJAsJla8bCK_c2Oy9NnwLcCB4tbNYvLLJAfk_mbkCIBr16dlMe7IXOx51K1Daw2qdwe-FoD5r3uLWEiY9x2dybWFALCBWBe6qCo7LKacIvLqJEUWyPEEujGVti7NDfM-bPsSfh8x5y8sfMLyddisSRiuEL9J00FDkwBQDjrhiJdipyfeIRdQ27b9qvtbyoQZDXq_khHg1UTSbsdQNB7Dn6sG-hzBHX4eKMyy8FTRCe4HVIu9b5Kz7qhwjM2AmGCwW65uNW1BMmRt0QPLqA761UM7YkRg32HH2SC77r1g3iM2MgM_L_t3y65pyA4yyOlti07BjdMutl8xeyA3rv_QQoumImShbus5l9E3szX2y7CWy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس دفتر کاخ سفید در امور سیاست‌گذاری، استیون میلر: ایران باید انتخاب کند: یا می‌تواند با یک سندی که برای آمریکا رضایت‌بخش است موافقت کند، یا با مجازاتی از سوی نیروهای نظامی ما مواجه شود که نمونه‌ای مشابه آن در تاریخ معاصر دیده نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121481" target="_blank">📅 11:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سردار وحیدی و وزیر کشور پاکستان دیدار نداشته‌اند؛ ادعای شبکه العربیه نادرست است
🔴
براساس بررسی‌های بعمل آمده سردار وحیدی برنامه دیداری با وزیر کشور پاکستان نداشته و تصاویر منتشر شده هم برای سال ۲۰۲۴ و مربوط به دوران وزارت کشوری او در دولت رئیسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121480" target="_blank">📅 11:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
۵ سناریوی نیوزویک برای آینده رویارویی ایران و آمریکا
🔴
در بحبوحه تلاش‌های دیپلماتیک برای مهار تنش‌های منطقه‌ای، وزیر کشور پاکستان برای دومین‌بار در کمتر از یک هفته به تهران سفر کرد.
🔴
همزمان، مجلس سنای آمریکا در اقدامی کم‌سابقه با ۵۰ رأی موافق، اختیارات نظامی ترامپ علیه ایران را محدود کرد؛ هرچند پیش‌ بینی می‌شود ترامپ آن را وتو کند.
🔴
در همین حال، تماس‌های تلفنی مداوم میان ترامپ و نتانیاهو ادامه دارد.
🔴
همچنین احتمال سفر سید عباس عراقچی به نیویورک برای شرکت در نشست شورای امنیت به ریاست چین مطرح است.
🔴
گزارش‌های رسانه‌ای از آماده‌سازی آمریکا و اسرائیل برای حمله نظامی و تردید در پیشرفت مذاکرات حکایت دارد.
🔴
«نیوزویک» نیز پنج سناریو برای آینده این بحران ترسیم کرده که از «دیپلماسی توأم با اجبار» و حملات نظامی تا «جنگ فرسایشی مزمن» و تداوم «آتش‌بس صوری» را شامل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121479" target="_blank">📅 10:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر امور خارجه لهستان: کاردار اسرائیل به دلیل بازداشت فعالان ناوگان آزادی احضار شد و از اسرائیل خواستیم فوراً شهروندانمان را آزاد کند
🔴
به شهروندانمان توصیه می‌کنیم به اسرائیل سفر نکنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121478" target="_blank">📅 10:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f43cf4ada.mp4?token=fMuOdMt9Prl3uQg1JIRVUv_aWCzQ8-zedaBr4_egsbH1XaNIiqxIZKrNdTgFdEvn1ZLuoJvjscVEjRyCHRbHqDodgbLTPsH8ejQ8UX9pBanuTxXU9kGX4OvrGPzD5S2mu30PoAy92rhiN--BaAzMab1L54641Ml5M2pCzDH6QuyXDlT-jkDS_uJpuX7D03QDHTODkid0ClkTDkKkp2Jl24qUL-wd9hMBInIaMzB7RcBglMjb7qe7c6VdOgYwmlqs8ZcoASMk1mj1hlxdml6yGhPCSVJ1wnx_kdVldFJZbsq7IK5B1M4BhaZYfaQyBeT7-U7Z5lKrfNkez6_1Cq4CIp8vpyUL5JEawhhDmS4gx_bRQeEQ_rqLFYe1CZZRrAC_qeySbZ62QyIoHojlXRKtRWmB5hu5DZiWMAscpI7h8O8kgATXHLmWwRmEcODCh-712l283rGmmDHBEEEf5eKHvlfGqmkjffknE9fBgx7hQDer9h9QUa-OVSsRu7R7FKJwFSwvugwMlzM40VTAt1QwZEbHFKr0He5pbIGgevCkqKvKRDL-N9SEZFSMURNHdlqUzyogWoWANJB04mrVud5VcJSQrDVJImf_zkgNmPxFmgV1lK788Z5meu5YeqPOAVGraBLqVN72IPcHUfnwkvvmcavC1g-qyXtmKtRhz1R4TzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f43cf4ada.mp4?token=fMuOdMt9Prl3uQg1JIRVUv_aWCzQ8-zedaBr4_egsbH1XaNIiqxIZKrNdTgFdEvn1ZLuoJvjscVEjRyCHRbHqDodgbLTPsH8ejQ8UX9pBanuTxXU9kGX4OvrGPzD5S2mu30PoAy92rhiN--BaAzMab1L54641Ml5M2pCzDH6QuyXDlT-jkDS_uJpuX7D03QDHTODkid0ClkTDkKkp2Jl24qUL-wd9hMBInIaMzB7RcBglMjb7qe7c6VdOgYwmlqs8ZcoASMk1mj1hlxdml6yGhPCSVJ1wnx_kdVldFJZbsq7IK5B1M4BhaZYfaQyBeT7-U7Z5lKrfNkez6_1Cq4CIp8vpyUL5JEawhhDmS4gx_bRQeEQ_rqLFYe1CZZRrAC_qeySbZ62QyIoHojlXRKtRWmB5hu5DZiWMAscpI7h8O8kgATXHLmWwRmEcODCh-712l283rGmmDHBEEEf5eKHvlfGqmkjffknE9fBgx7hQDer9h9QUa-OVSsRu7R7FKJwFSwvugwMlzM40VTAt1QwZEbHFKr0He5pbIGgevCkqKvKRDL-N9SEZFSMURNHdlqUzyogWoWANJB04mrVud5VcJSQrDVJImf_zkgNmPxFmgV1lK788Z5meu5YeqPOAVGraBLqVN72IPcHUfnwkvvmcavC1g-qyXtmKtRhz1R4TzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار وزیر کشور پاکستان با عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121477" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121476">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGisz3ebxmruWBSy8NrWFr31PgjBvExqlwrRx-jZnuYsUhZnSc4odN5dFNE7ReRRkCT9xdmwdBAkpZLnYsGR9iolfnKozWUBmqXP9yIA_jJzkN80e89_nT5HfmjWQUvy76I0XKWN0Z47LwX8ttrbbuewvTvc_2iRiJAf0CkDis09_Bb69T1X3rywikwwFIq5yoeJa_K_7xOfcg_EVbUEBKcGSbeb8e9R3EoNJrQ_x9jkRq9BmRkCp6SmEsS2IMOco4eomnU3IGVF2LIrJw4CA28hSFXZu2tEJzGOHLQ-wZ4cvLTObPuTBA5LL_Ck6TT3TAulaH0dMhEqQT4yxOQ0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزبه چشمی به دلیل مصدومیت جام جهانی را از دست داد
@AloSport</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121476" target="_blank">📅 10:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ایندیپندت: ترامپ بعد از جلسه با معاونش ونس تصمیم گرفت که ۱ فرصت دیگه به مذاکره بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121475" target="_blank">📅 10:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Atr9puYvBWwyKOSHNFjAB_6_KLXoKOv1YgIiPejhSOoo7L0CITR24cXqn77dk8sWgUeMHX2fKtvGqpac7zkm-gUgJefqaAwWyQ5QWVUaRltHPPLy2RBsAuvQqCk5qhkzUorqTY_eP1P0MILiuthCjc9GFZnSOOdzLVOH_plyYfrxsKqiTszbvh6coiwmeyBNt7FjWf3PhFrJ1WluMFw9IehOtnOJ49KYHwg3SobvtwoQptLW1KaAeg3-2cZXeifDcUVGkX60RuB6mUrLovCVcn3kiw783D8ZJC49jHfrVPLhc31aX4HJpq-QUca90MJHuKCyWeRXbJg38ntr6QO_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از وکلای کاربلد متهمین قتل یک بسیجی که توانستند حکم قاتلین را از اعدام به پنج سال زندان و پرداخت دیه کامل کاهش دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121474" target="_blank">📅 10:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ادعای «میدل ایست آی»: به ترامپ هشدار داده شده آغاز جنگ در ایام حج، آمریکا را در جهان اسلام منفورتر می‌کند و به همین دلیل حمله به ایران به تعویق افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/121473" target="_blank">📅 10:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3399d3dd7.mp4?token=Jb-898vsQeMTVXO7cScP39EalxjG-oayYv87sl_ckkv63ZI0iyD9imTbcYralzJ9i4qVWiV9AXDwpaYQNpMGx9AKB101KyS0hZmF1T1Q-DGW2lBbsxTYncbG0rU-lsba7jBG84y4IUVS8L9qmknk9t18GqYLtYMNkaKIeeAJi2VOYvZG0HZqep3Vl45ykAchLmj47D5MIYWquGcqPSl_F0odoLWG8S5jMx9fUEb7q5xNQ4bTcZyku2dmtYwAjSv2fmPrf-Yx7ZOQhsH3yRmNwKylwk3nZ9SntcKX99U_wW8ZTijd3XDk7n8AbnSINd9mBkBYuHKkrgpxPxMWLL_hsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3399d3dd7.mp4?token=Jb-898vsQeMTVXO7cScP39EalxjG-oayYv87sl_ckkv63ZI0iyD9imTbcYralzJ9i4qVWiV9AXDwpaYQNpMGx9AKB101KyS0hZmF1T1Q-DGW2lBbsxTYncbG0rU-lsba7jBG84y4IUVS8L9qmknk9t18GqYLtYMNkaKIeeAJi2VOYvZG0HZqep3Vl45ykAchLmj47D5MIYWquGcqPSl_F0odoLWG8S5jMx9fUEb7q5xNQ4bTcZyku2dmtYwAjSv2fmPrf-Yx7ZOQhsH3yRmNwKylwk3nZ9SntcKX99U_wW8ZTijd3XDk7n8AbnSINd9mBkBYuHKkrgpxPxMWLL_hsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غرفه‌های همسریابی یا همون .... در تجمعات شبانه تهران برپا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121472" target="_blank">📅 10:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
احتمال شنیده شده صدای انفجار در شهر ابریشم و جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121471" target="_blank">📅 10:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
خبرگزاری نور: سخنگوی وزارت خارجه ایران، بقائی، گزارش داد که پاسخ ایالات متحده به طرح ۱۴ نقطه‌ای خود را دریافت کرده‌اند و در حال بررسی آن هستند.
🔴
«بر اساس همان متن اولیه ۱۴ نقطه‌ای از ایران، تبادل پیام‌ها چندین بار انجام شده است و ما دیدگاه‌های طرف آمریکایی را دریافت کرده‌ایم و در حال حاضر در حال بررسی آن‌ها هستیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121470" target="_blank">📅 09:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
«میدل ایست آی»: سه منبع گفتند که انتظار دارند جنگ در هفته‌های آینده و پس از پایان دوره حج، از سر گرفته شود!
🔴
ایالات متحده در گذشته از سیگنال‌های فریبنده و حیله‌های دیگر استفاده کرده تا سعی کند طرف مقابل را دچار احساس امنیت کاذب کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121469" target="_blank">📅 09:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رسانه های پاکستان: وزیر کشور پاکستان نقش فعالی را در این برهه برای اطمینان از تبادل دقیق و به موقع پیام میان تهران و واشنگتن ایفا می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121468" target="_blank">📅 09:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نیویورک‌تایمز: ایران موفق شد انتظارات آمریکا و اسرائیل برای یک پیروزی سریع را مخدوش کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121467" target="_blank">📅 09:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رویترز: سه نفتکش حامل ۶ میلیون بشکه نفت خام عراق، قطر و کویت در حال خروج از تنگه هرمز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121466" target="_blank">📅 09:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رایزنی‌های مصر، عربستان و قطر درباره آخرین تحولات مذاکرات تهران-واشنگتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121465" target="_blank">📅 09:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
متکی: با اولین شلیک آمریکا، جنگ زمینی را آغاز کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121464" target="_blank">📅 09:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اخیرا یک هیات ویژه به نمایندگی از امیر قطر به تهران سفر کرده و با وزیرخارجه دیدار و گفتگو داشته است. این دیدار در چارچوب تلاشهای کشورهای منطقه برای کاهش تنش میان ایران و آمریکا صورت گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121463" target="_blank">📅 09:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clV3gWsFwQCriTgoTPkqfdmYdnISWSLhQkyLLc4JMRx9E8QuldFC_nNXc_HT8RbXIVy2wN9exIHhZ49ksn5Oacjqm0EfSS-VTKRm2NrR9HjhYpONLTL3bJABBu5OmDMeBFbr77cSY1VGpss8Jsh2QL0aS2IgxWkplABFoKxBiK88k48yZq39gRYaD4ebxzltz2cWycX46qTpzSRuVvWyI8hEEuyBsAIMtdPJkZQIKXHEBpmf-m1AZ2QytvciDNctO1ORPu-dP3LX1yFrUpjUnpKOy1g57XnqmRbuC8tWRgfz5pZfcHR5i0ohFAGvscPqWPWlTDKiwwxfuP024LABjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: ایران تهدید کرد در صورت ازسرگیری حملات آمریکا، جنگ را فراتر از خاورمیانه گسترش خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121462" target="_blank">📅 09:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزارت دفاع روسیه: به عنوان بخشی از تمرینات تسلیحات هسته‌ای، مهمات هسته‌ای را در انبارهای بلاروس فراهم کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121461" target="_blank">📅 09:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: بیش از نیم میلیارد دلار ارز دیجیتال مرتبط با ایران رو مسدود کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121460" target="_blank">📅 09:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت خارجه کره جنوبی: در هماهنگی با ایران، یک نفتکش کره‌جنوبی روز ۲۰ مه با امنیت کامل از تنگه هرمز عبور کرده و به مسیر خود ادامه داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121459" target="_blank">📅 09:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سفر قریب الوقوع رئیس‌جمهور چین به کره شمالی
🔴
خبرگزاری رسمی کره جنوبی: «شی جین پینگ»، رئیس جمهور چین هفته آینده به کره شمالی سفر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121458" target="_blank">📅 09:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
مخالفت بنیانگذار سپاه با تسلیم سپاه
🔴
محسن سازگارا که خود از بنیانگذاران سپاه پاسداران انقلاب اسلامی است و سال‌هاست در آمریکا به همراه خانواده خود زندگی میکند، در این مصاحبه با تسلیم سپاه که ایران را اشغال و زمام امور را در اختیار دارد، مخالفت نموده!
🤔
زندگی…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121457" target="_blank">📅 08:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ایالات متحده. جامعه اطلاعاتی در حال ارزیابی چگونگی واکنش احتمالی کوبا به اقدام نظامی احتمالی آمریکا است، به گزارش سی‌بی‌اس نیوز، در حالی که کار بر روی تدوین گزینه‌های نظامی برای رئیس جمهور ترامپ آغاز شده است.
🔴
تحلیلگرانی از پنتاگون و آژانس اطلاعات دفاعی مأمور ارزیابی واکنش‌های احتمالی کوبا به سناریوی حمله ایالات متحده شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121456" target="_blank">📅 08:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
فارس: آمریکا با وجود شیوع سویه جدید ویروس ابولا در کنگو و افزایش شمار قربانیان، ویزای تیم ملی این کشور را برای حضور در جام جهانی صادر کرده است؛ اقدامی که در تضاد با رفتار سخت‌گیرانه واشنگتن با تیم‌هایی مانند ایران، الجزایر، سنگال و ساحل عاج ارزیابی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121455" target="_blank">📅 08:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE4TUmpSSQDXgzbNLF3Z1gWgQj11ODVr6Gu0fg41ovt41WoR7SOOwqMVF05GyLMGJBjMvA6Pelf7Rt6qra1DHhPvKR3Kzh8IKFeM9J4ZoTXXwr15GcRPeB1k-8gJIst3bK_c0yKFPTP54Xa048yrrx7noYLjwhJ7fYQJGg8DKotZgibgotvDVE9G3KBZ160DLtGNvM5TyPdsP9BSLD-rq6JBEpfzJZvbpWhPLd1Okmst-emB5JETn_0p7cMsY_udQLoA8auSFTjjEfO5-QKb6PwIUnrPo0w3xdbR2n9Wi9RKbBb9Wnb-n7_LXUevGht0_mBOlxSwQ8Ud1nr8VivrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شوک در بازار خودرو؛ پراید وانت ۱.۲ میلیارد شد
...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121454" target="_blank">📅 08:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
دومین زمین لرزه‌ طی ۱۰ ساعت گذشته به بزرگی ۳.۸ ریشتر دریای خزر حوالی شهرستان مرزی آستارا را لرزاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121453" target="_blank">📅 08:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع آگاه:ترامپ می‌خواهد شانس رسیدن به توافق با ایران را آزمایش کند، اما نتانیاهو انتظار داشت اوضاع به سمت تشدید نظامی پیش برود.
🔴
نخست‌وزیر اسرائیل از مذاکرات جاری بسیار ناامید است.
🔴
او به رئیس‌جمهور آمریکا گفته به تعویق انداختن حملات اشتباه است و ترامپ را به انجام آن‌ها تشویق کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/121452" target="_blank">📅 08:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: قیمت طلا پس از افزایش خوش‌ بینی‌ها درباره توافق ایران و آمریکا، تثبیت شد
🔴
هر اونس فلز زرد به ۴۵۵۳ دلار و ۹۶ سنت رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/121451" target="_blank">📅 08:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
یدیعوت آحارونوت: مقامات اسرائیل از اقدامات ترامپ راضی نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/121450" target="_blank">📅 02:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کانال 14 اسرائیل: ایران و ایالات متحده امشب از طریق واسطه‌های پاکستانی نزدیک‌ترین پیش‌نویس‌های پیشنهادی خود را مبادله کردند. هر دو کشور فردا جزئیات را بررسی خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/121448" target="_blank">📅 02:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121445">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bqm6RKpAU51IeRzBggxARZzQn3uhx76XQVPlBap_DqWyPNZqKLeik6umV8CeBhx19TTMOCIeDakbLdq9RXQU_b4WBPOmTeha2NflvNh6qI8EJhkKZ_cYUk1OgMk-QLjtRNMD5xFvLZACa3vJueCdbmGBsjtkzjZ3hstoQn-dkvitxiiHqAxymaatOHjQnO-XDT43TNpdKLlBFzPnd2ybzCOGcGGCVsNN52xiq4DVj00O7mm9kDg_YvYvDSrnPkeB1Lb90DbQo7ZRDAUTQgyLwtB1UwH6sc5kUyQTctgG498ApbjIsLpuAiUWWSUhVLiU5LG0tS_qOzt6AWQn5CQtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mtyv9eINrp8YVOHsbhv-k5OeaBMQxdV2hVGSYEmj01rVPotzJbUH15vPDzAzkpflmR6ZLGatdbJvFZNhPU7jVDzU4tT5CQj57fVlBtejovGuCanlVHev1fLUzFl5foWIRWW8n8y9Zo6GOdCRfHk9GAXe3JuLavxvtv5pRDIiNH_FduX8C_aUwmWaAeT1pXFc5DoTdFqVebRsAWiNlC8Z6du3F8MLoAz4ek_zpjV_HpgY5RVfrZr5DB9u9erG_WkU2fYW1baggZlnB2Qw3ARrjZqv5dBg7Xj4CaNGPojTZeAtDHFkCKSR3KWcFn6SVIKNhWx-iYS9jm-XWXD9gIiKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqs__QyymFh1wf5ZUgl9DGZpZI0dWO3Lb7kt15q7qDhvNJw8QD9NsBdEzmh_hpcX3uP7BNU4cc36l1uSQATAXLvCv4lNuxqy75L4f8IKLO-oF6ayljP6HwSnGXWbskc8ovDIDOU4oRrw66xMIEsaN_p_2SVghysrLHpprZ7-Ycbkc6TuOxERlbv4vUkQqa0mRq8wRRVx9652_2Iq2gh9xfba1GidEab3SENYByT5-DT-CsBTq6LEtKt_4dCB9pEdC42KwydMyaaELeRk2kTb_ZIq2MxnEm0rjnRZDwlbfw_4F-Mjl_C5LbcMk-KR35ams6xg30v5a7po2SblWzqUjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کلاهبرداری صرافی
#رمزینکس
⁉️
🔴
پیام مخاطب
:
با سلام
من در تاریخ ۶ فروردین ۳۰۰ ملیون معامله اهرمی در نماد تتر گلد صرافی رمزینکس داشتم در عرض چند ثانیه قیمت از ۱۷هزار به یک هزار سقوط کرد و دوباره برگشت همه معاملات اهرمی پودر شدند با پشتیبانی  هرچقدر پیگیری کردیم آخرش میگن که شما ریسک معاملاتی رو پذیرفته اید یا بعضا قبول میکنن قصوراتشون رو ولی جبران خسارت نمیکنن خواهشا اطلاع رسانی کنید تا بقیه تو دام این کلاهبرداران کثیف نیوفتن وسط جنگ از این شرایط سو استفاده میکنن و پول ملت رو بالا میکشن و هیچ مسؤولیتی رو گردن نمیگیرن.
🔴
این اقدام صرافی رمزینکس مصداق بارز اخلال در نظام اقتصادی و سواستفاده از شرایط جنگی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/121445" target="_blank">📅 01:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121444">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHATzKZWFOYhMMyPM_-mxHYCp6gnaavZvtO8uTIL-lf8TSn7CE9P-XvWfigHQ-bO7d47oi6cHkJSPelDI2dRc8SizKwCPw0XZRIYTPwNyzN8nUq2xe7UAd9zH95kMhswPG7viBVKzFVX3dAKyDuA10OC3uVOlPYMCUibRcNm2qyaHpnt7-H3jAEcJgnRScdwmFFnLSu-WmBoiTT-h6Bsg7Z-z2eKLXcDlHy1lnSRWLfQfBncm_6FcBbJoOQ9t8an0qA3pqrN4mGLQVZpe7eEhgm49tGQuhy9yaRrlTi3e00Xvc67xa3Aw__84WdA3YPZH_69DOiiVn9l5N8LkoFLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پائین کانال نمایش داده میشه توسط تلگرامه و دست ما نیست و  کلاهبرداری هست و فریب نخورید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/121444" target="_blank">📅 01:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121443">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4cff02f6.mp4?token=Jemw-fORjgnJHLDit5knD8aFJp8wV4F6bv1HH-qKcdxldsfo5dx-xgD7Pil5893xrGmZw7nB60hiyGW6eY5dPgJHa4dgj1jXaBstn4L-Gadb3xJr0kFIXryIxgjcR3kuXs4ktG2kylMLvDxxBOxGK9HD0jQSpyq-s36agmNhkM1ast6yY3pQCpGbUznK_JM2M7ekEefJ2kyQqKcHq8k-Pi1wQEdZhCPl8TQKjFrRTDvyKOMeoZuBc4Qc90amWkKp8s5NrH8q5WcYU9V_KWTt_e3577V0iiTjzAe-Ljcnp4Ap83oltLTindHMbwhp5-rqyD_6dRrGQEGlDN8rV3QIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4cff02f6.mp4?token=Jemw-fORjgnJHLDit5knD8aFJp8wV4F6bv1HH-qKcdxldsfo5dx-xgD7Pil5893xrGmZw7nB60hiyGW6eY5dPgJHa4dgj1jXaBstn4L-Gadb3xJr0kFIXryIxgjcR3kuXs4ktG2kylMLvDxxBOxGK9HD0jQSpyq-s36agmNhkM1ast6yY3pQCpGbUznK_JM2M7ekEefJ2kyQqKcHq8k-Pi1wQEdZhCPl8TQKjFrRTDvyKOMeoZuBc4Qc90amWkKp8s5NrH8q5WcYU9V_KWTt_e3577V0iiTjzAe-Ljcnp4Ap83oltLTindHMbwhp5-rqyD_6dRrGQEGlDN8rV3QIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاخص پیتزا تو اطراف پنتاگون رفت بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/121443" target="_blank">📅 01:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121442">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41972ea087.mp4?token=IjMIOaU4mffFQbZZ6OLUuRcMvWL0O3DyeGh-ONSqxHlHACfwnPUZO6o1-8BCWCN-aaV1vbwxjnfizY7ujUUKK5PBWJpH7OrRn3Jsd7TY3GfLRabAy1njj8tk57CrJkhCWacYqZpNrAEu7u96QN1LkcbTElt0pF_mEyIz51qZ2QSSmtrcpZFanm7FNvVNVDgIy8-2WBGVpysdsv_v9fHDMMkfVt_G0hWiGYr0YUN5gE5zRm5enkavM6xPqiglPv4QjwDvZLSc9nthKYfpcEcTQRA2iUBmY9pGhtnhaV3jiODqOKg4zG8cfzaALzvcEGbX_pJxsyu8olXdhgxPZc2Q6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41972ea087.mp4?token=IjMIOaU4mffFQbZZ6OLUuRcMvWL0O3DyeGh-ONSqxHlHACfwnPUZO6o1-8BCWCN-aaV1vbwxjnfizY7ujUUKK5PBWJpH7OrRn3Jsd7TY3GfLRabAy1njj8tk57CrJkhCWacYqZpNrAEu7u96QN1LkcbTElt0pF_mEyIz51qZ2QSSmtrcpZFanm7FNvVNVDgIy8-2WBGVpysdsv_v9fHDMMkfVt_G0hWiGYr0YUN5gE5zRm5enkavM6xPqiglPv4QjwDvZLSc9nthKYfpcEcTQRA2iUBmY9pGhtnhaV3jiODqOKg4zG8cfzaALzvcEGbX_pJxsyu8olXdhgxPZc2Q6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: پیامت به خانواده‌های آمریکایی که از هوش مصنوعی می‌ترسن چیه؟ اونا نگرانن بچه‌هاشون تو آینده کار نداشته باشن.
🔴
جواب کاملا مرتبط و منطقی ترامپ:
ایران نباید سلاح هسته‌ای داشته باشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/121442" target="_blank">📅 01:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121441">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cea8257e.mp4?token=ZDZGsUsF1i4zil71NKh3crtiCgCnPtnaQtRxqL4JGxI4DGGVNYz9yiiRNUPyegKOzk6HsZdgFz7IUjaD7jYfsuLrh5lhEXidO5ivr2El6R4DlH_he9H9Lv7Y7wyerTQhxZEqZUW1tR12JfM0sR3pU1PqBtyF1YvM4bFKG7Od9DPORVMpkzvhobn-xQM68YRkFLooNFyYthoMEpgi0P9WmbZ7QCH9uJj1YfVh4bI_97eq_DmDsvJk6kw_a73Bv80Sou-dwMVfcDlwIEKmC65eAeniCl-V_9TRoCOlasTQZ5MsZRF_fWRlt5OBedEIXO46MERtAwFOZG092WJ3j1_SKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cea8257e.mp4?token=ZDZGsUsF1i4zil71NKh3crtiCgCnPtnaQtRxqL4JGxI4DGGVNYz9yiiRNUPyegKOzk6HsZdgFz7IUjaD7jYfsuLrh5lhEXidO5ivr2El6R4DlH_he9H9Lv7Y7wyerTQhxZEqZUW1tR12JfM0sR3pU1PqBtyF1YvM4bFKG7Od9DPORVMpkzvhobn-xQM68YRkFLooNFyYthoMEpgi0P9WmbZ7QCH9uJj1YfVh4bI_97eq_DmDsvJk6kw_a73Bv80Sou-dwMVfcDlwIEKmC65eAeniCl-V_9TRoCOlasTQZ5MsZRF_fWRlt5OBedEIXO46MERtAwFOZG092WJ3j1_SKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر بهداشت و خدمات انسانی آر‌اف‌کِی جونیور: من همیشه در اطراف دختران جوان زیادی هستم و همه آنها در آن بخش از زندگی خود واقعا دیوانه به نظر می رسند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/121441" target="_blank">📅 00:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121440">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2BiHwMG-jDoOM0_tzBUQyFvyfJHH_j180Ex6DSaG1hQp7aDeecIt-Wfsz_7SUN3PeJrGD5k2z8n6B1cUbWEJoxHqXGyYD6OvaAbrPiEDnFrvmSbKQsun4SzvGAyvHw_mWs_niKu2Xubg3lJXAiwlpfUyB8Gdziao_Ny_aCCuaRMpaYaRFedQJyHDDFpJcYXEOEF25pHmEzQGpDAXWvRySk4pTfBKqbUNudcZDdTiJwxjC5mz25UXPI_08ZC_3Uy1F--3Cmwc-xckU5QhkcTFHzR-sOu6gE06UtgV1UZJl-7E-3W5I5V94nIbabmGxbk9qYmAB0prf6pJMZTlUYITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بزرگترین کشتی جنگی ژاپن برای آموزش F-35B با تفنگداران دریایی آمریکا آماده میشه - USNI
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/121440" target="_blank">📅 00:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121439">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjlE6GiiDrpD7ToWqCdyqyHe4VVAP5xxu33RkTptB6KyF8yRQsRtaQmNF1MTqdvb53iaWvVrhbjPeV5EknD8ydYuN9gT844UfZXQxDLhE12_vJAHY7XyDCA6qlAgTsKCNO0F-2AAeQ4lis5SA7t7ucbByYA7c5r5JF2KTb_KiRa727rqCkdbF7GZYx0yOqSPHv4QSKKdnyUxj3U294aR8mjK7PQT1nxjk4kG9CoUm2iBFyuIcuPq0FBcnFVtx6cAXA_32gE-y7E9pEL-kYnL0P6sB8OobMbMNo7AVPcHoNQExj2jaWEGBiIzCtLFc6vqbNeMm6iKBkAwbuKOBLlkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه مارکو روبیو:
اشتباهی نباشد: ایالات متحده به طور قاطع از دولت قانونی و قانون اساسی بولیوی حمایت می‌کند.
🔴
ما اجازه نخواهیم داد که جنایتکاران و قاچاقچیان مواد مخدر رهبران منتخب دموکراتیک در نیمکره ما را سرنگون کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/121439" target="_blank">📅 00:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121438">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
زاکانی شهردار تهران: آمریکا ته زورشو زد و دیگه جرات حمله نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/121438" target="_blank">📅 00:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121437">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5AanDcQDzlK9DFxDI0WP9Os6MWCPEfE-hPdQ3qJtkCMbP7lFhfibEdqGaEIdf0224_1tHwlzaOFvizsk91fJl4VF3X-A0Dgy6oc8TkapuX181H2gwWyKjeusRMWK7xtjYcGs3hYqWuF2A8lyUD6fRdDsRvlEUfrnI_06acNbyZJLstBMy8gkFmNz_hRE1pQk98seRB4KpUPvFIyfuGimkAiCLd3ZeVtOQEQqWpNAVvNTzpDb26iQpq1jmrq3fMuN8EJnJ1RN0rlOXoW3HYOQSLZvx6WY8FqofNOmzQVUtkmQZ-ebvfdySQlR4XPnRd4Z0g-6e_XDXtjtpDyPqpPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعداد زیادی پهپاد به سمت غرب روسیه و کریمه پرتاب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/121437" target="_blank">📅 00:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121436">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ادعای «میدل ایست آی»: دونالد ترامپ، حمله برنامه‌ریزی‌شده به ایران را در این هفته به تعویق انداخت، چراکه متحدان عرب و مقامات دولت خودش به او هشدار دادند در ایام حج، جنگ را از سر نگیرد.
🔴
به گفته دو مقام ارشد کشورهای حوزه خلیج‌فارس، به ترامپ گفته شده بود که…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/121436" target="_blank">📅 00:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121435">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فرستاده ویژه ترامپ به گرینلند جف لندری: زمان آن است که ایالات متحده ردپای خود را دوباره در گرینلند بگذارد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/121435" target="_blank">📅 00:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121434">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ادعای «میدل ایست آی»: دونالد ترامپ، حمله برنامه‌ریزی‌شده به ایران را در این هفته به تعویق انداخت، چراکه متحدان عرب و مقامات دولت خودش به او هشدار دادند در ایام حج، جنگ را از سر نگیرد.
🔴
به گفته دو مقام ارشد کشورهای حوزه خلیج‌فارس، به ترامپ گفته شده بود که حمله به ایران در ایام حج، بحرانی را در میان کشورهای عربی حاشیه خلیج فارس ایجاد می‌کند، زیرا این حمله باعث می‌شود صدها هزار زائر حج سرگردان بمانند.
🔴
منابع همچنین گفتند که به ترامپ گفته شده بود حمله در این ایام مقدس که منتهی به عید قربان می‌شود، بیشتر از این به جایگاه آمریکا در جهان اسلام لطمه می‌زند.
🔴
یک مقام ارشد آمریکایی که از بحث‌های جریان‌یافته در دولت ترامپ آگاه است، تأیید کرد که این گفت‌وگوها انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/121434" target="_blank">📅 00:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121433">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbr5YoF9cZO-8xgChg1N2po6iaditFhTe58vC4loNnzI1_E2k9XsvKZBrkFI7L8zk899t8PcHprPQi-szSqxl97T7cjeeArKmw7gC9u0MrDxB1B3mGf6iggTfA0SFnKoUmOeTonb04eTlIN9ZGiV-bv19mdQRezHJjAAqL3qwKCHPZFwBno5YUR_NYksmVEbonXcg3mIHqjWJJmNAqmQngppjr1nhVqPidfEE2M45FViZAe2DQ0GR8fEXwM-7mTkg8UXTzdcgihbArerMjGfqRBn8VdVOButk9B-QSekYQxfpP3j1lzaE6SjSB8FWkXVD26dEaVoCNIECVxKjw6hLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرستاده ویژه ترامپ به گرینلند جف لندری: زمان آن است که ایالات متحده ردپای خود را دوباره در گرینلند بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/121433" target="_blank">📅 00:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121431">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqP18i8po6iUyxzZGsOKyDAkIOf3p4FOY9NVq6c-5jAoJm30iaIifsaf7UmaRe3qF89u-j5HaCf0j4OEYZXByxC8TPrmJk-pfcaDR54IoOztlDJx_yMta1VWULzUMDW8xzd37s-kmK-xqao6BFp-tnV1xlo0S6rT_TKdaG6eFExGPWLGaaxFa4TW-USn4y_wmALlgSycC74QXlhZ7HGjtk2BhoDtZUjsaJB767-id78H2_NVW0dYPUlD3UnR34Xs5L0MqBX6IicPzH90h7uFZ0IC4DNv36OnvpTFAzEBMtLGz5jjDI2Ez7p28YQDF1PTjeBkZffQBvSETKmQlG44fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ToTWyqRQl78IRGBmJDsfPtEi5iFAfP4ze_T3wYu6XKos5_DmDRQjGGkWWYyiLpV1e_tcfTxiH3V8XxTVI0_ko3swOAKR_Ypjc_mvPMmFfeyXb92BjpTl2KdFLZIdycRgUpfsEN4VhWxh7GuJ0rRy2SMvA6MSs7_kMO_17lGWKiVUhZOX8WuRlo8cAMd7O_8nMhIecw0ODaFgpQumkTns4W6QD4mj9ZeTJUn-wgGO8KMrQCEmXWv3r9XNTnxs5QU3QfLG4jPKiX85OjWAXHW8YlpqUMUP9XLJ9Jsz5PgSDfXv-yxgRq8rI3N3KIsZ7LVCYmQpdR14Jb5b41ofFgdAxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لکسوس LX600 غول ژاپنی با قیمت 110 میلیارد تومان ناقابل!
و حالا همون ماشین در فرانسه به قیمت 124000 یورو که میشع چیزی حدود 26 میلیارد تومن…
شما فقط اختلاف رو ببین
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/121431" target="_blank">📅 00:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121430">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atJJNPu5g7FRTj81Kyvnghz0Fig53YDxZr7pnGNqr7MLKJqm91cAVZXsBPTKkagSf9QDEdB6p2U5yCLVUz-eYGUQg22o6Ii_tDxFmma6ulrjPnmbL8VHCLKzP_nOeY3GBKs1susfDbqrXTvYqbpm9LqosIi8qJeqhIakmniK1MqxxNgz7Njl9SfRB3AQqeAPYzBmW2xtZbRuQY-UfOHRx8irrGq3gxhJDBFkZbQdQfgOyY25bFjomt_YkTkVWcSHJ8aGJzYcsKvy7YFfawznHHZDSF1pZ8yqjizB8ZJ8Bo7du9XgsCF8i9FUVrVzjbMZdjvMWsB2mhN2uGO9tmO3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس محدودهٔ نظارتی مدیریتی تنگهٔ هرمز را مشخص کرد
🔴
ايران محدودهٔ نظارتى مديریت تنگهٔ هرمز را به این شرح تعيین کرده است:
🔴
«خط اتصال كوه مبارک درايران و جنوب فجيره درامارات در شرق تنگه تا خط اتصال انتهاى جزيره قشم در ايران و ام‌القيوین امارات درغرب تنگه.»
🔴
تردد دراین محدوده برای عبور از تنگهٔ هرمز نیازمند هماهنگی با مدیریت آبراه خلیج فارس و مجوز این نهاد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/121430" target="_blank">📅 00:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121429">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/121429" target="_blank">📅 00:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121428">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نخست‌وزیر اسپانیا: فشار می‌آورم تا کل اروپا وزیر امنیت اسرائیل را تحریم کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/121428" target="_blank">📅 23:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121426">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R757crf25Qi7-KvP_DT63IvScZe_u6hdzgehsdOZox1pyvtn0-Ch4qNsaY7Fcwks1PJFN55sDLcOere746Qyyn1VHA6wfi4pQhzlGyWbheMoeh5vrSg623Ab6JX7pNUqddQ7ac_aKURd7ZJXhDkALo2oKgAbwk9QPFCnJZ6nJsDFFYzZFdLVqPOa8HkTZ3a_IqDuASmaNG93ENq2OEVEgNaEoUMS5brs3ybwfq9ioJTYsy5nrkEfcl-cNDq304N5wvIOl69Xm_Fq4gG4t9y_ZC-HbHOuNYu0yHD4ky39aJChIMlqPp2K_nfJwa6v8cVbC-oQez5C0XYABZEZmMacww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۵.۰۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/121426" target="_blank">📅 23:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121425">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYvl7qjNpfEUcEIxQ7v455BmoL52o1h-FvKhhu0gD2xx9IaG_dnStzNFbOtF2lGz3FsIFFKYZYXTB9Rzyoolu-eJcQ4eJLLn4D1X1fK-Mkl21VgR8gOzVuwGqGji0O3fjmKc-Km23SyezwGZqvGurbnHhlduYRTkbBcM5Xa80pznjoANs3ye7_Q_mr43euRjqVBHinRweZas9tU6JKHDzvfc7_IU00GLwaj4wS_cAe02w5IfKc6-UZzZ7657MUuxfEC2FoFAqOkLNcNk1bwbFAg1ASw2KM1rwuB66R3X7dE7Q-FGfE0vqDk1bVVSVd1Kn3SbYP9uI9-QLiKipLU36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: یک منبع آمریکایی که در جریان این تماس تلفنی قرار داشت به من گفت: «موهای بی‌بی بعد از تماس آتش گرفته بود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/121425" target="_blank">📅 23:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ درباره کوبا: مردم غذا و برق ندارند، اما مردم بزرگی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/121424" target="_blank">📅 23:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121423">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYdpH0Ovy0RdOkfCmKJFXaTq-9aejQs3XUZqsBGl2B6F6InHCfqEmjCPIPndRLgIpP9x2oDeD5tQ0zRh2Czxq4ZFGdC81LkIsP2oA7Q-o-YNJwDRtg9zXedJcJftb5H4yKkhfZLbJQvbhSv5b_wwPgN42l-fr3CHrm1TwxPzegtCLlIyv43jmmG2XGJrLz4tD7vIJhF7wigGozA1-LFkg00iVxKX2w0ymcX9GyOnxSMAxvP-k7GEte4DkOd0j_6BfXjYKYHdpKRmeExs_ra7RlkPFl5lHVbKt1_r3QZLED8PNyz9zlTopyerl1EvkOwvjZdFDU3FARzlj065D-JMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر اسپانیا، پدرو سانچز:
تصاویر وزیر اسرائیلی بن گویر که اعضای ناوگان بین‌المللی حمایت از غزه را تحقیر می‌کند، غیرقابل قبول است.
🔴
ما اجازه نمی‌دهیم کسی با شهروندان ما بدرفتاری کند. در سپتامبر، ممنوعیت ورود این عضو دولت اسرائیل به قلمرو ملی را اعلام کردم.
🔴
اکنون قصد داریم در بروکسل فشار بیاوریم تا این تحریم‌ها به صورت فوری در مقیاس اروپایی افزایش یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/121423" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121421">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cWUDbq-Qso-bZeaICDw28NMj9dt9vU5WI_1tXQYrYPkGKPEp5TLTvko-bwP2vQzB_d36Yb2jeaJP5LnrFjm4ezD0N4O7AqNbVn7OpIuu21zdWSJYFWLCZq4-YonGlOEm2DWVJnW-4UxzzLlp7u9QIaFVHdRrhlv3DgqIFIvouyhcoj_A7-Z-m6draVww3uEcp8zB2wlQSej_KkWbyjyuQfevU5QuybqIPy-W70YXs6O88rcK_bCQncSsGsg2AxPId2wpFMpJOlUjJ4eyLizJMOVkDDhbGJoXGa5JlmiTkaGNhu0zCpDkvrKyxwNAVFGHLM69Dn0CoMWiDLfPSapppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dvr_KBXz5ukevM0TVGuldc6Mrlmdoes6sj9wxvS46cKZgJn8atZvMzex8GcCtyZJEbQrJcff4ndwuukgm1X-oRm0DrzGK3SQYOKsmq2K1CDq6GYYNSjE0JvpguG6Fe8UP42ql65sBF6GITggj3LnNG71jsvtccoktQD17ure7xHe3LmxTTMDVvJN0IAcCl1gcAqtYY9xLiyYGp09VCcA3adihgcrnZHTvop9LAMExjTBTAAYKeUt4p2hSJd5nesu_abScbqw0g3_bWTW8Pvb-hISoHnWLLfZ0N1Ry84kT6SHqp9eujso0t3Poq-hikaT9_ve0V42yooLAePq_0eMeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یونیورسال پیکچرز بی قرار است فیلمی درباره نجات دو خلبان آمریکایی در ایران بسازند، پس از اینکه جنگنده F-15E Strike Eagle آنها در عملیات خشم حماسی سرنگون شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/121421" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121420">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0624b84a4.mp4?token=aZ0UxAEbTz-jsFDM_zMjjrofJSPu3ve2yStPvfc2gfZMaSvgvBwZp1hfJhh1O0JW4p-C_p6XZ0vANUUH-rAEmAHSMp-jI8MrKwKfPP04Gc08twYrmXvdDAy6oKJHJJdlZmEvti0SYd7I2VxnBhxv__T-_eXwTWI5G7FVJeV-QbhWmfZNNQb8lQ5dnlkw8Uowm2ZpNVit8n3U8v-H5LRWKRksKpfJ1QIormVaDfmt859cOlDa4M8ulzzwNf4HlH5GkW1etZ0XHGgfMaZgp5j6UE1QaHGdQjKBLMZ3VnMT_Lzx51rpA4YszKpGpaRFXIbGfzJghDFCV7NPtWCN3iS_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0624b84a4.mp4?token=aZ0UxAEbTz-jsFDM_zMjjrofJSPu3ve2yStPvfc2gfZMaSvgvBwZp1hfJhh1O0JW4p-C_p6XZ0vANUUH-rAEmAHSMp-jI8MrKwKfPP04Gc08twYrmXvdDAy6oKJHJJdlZmEvti0SYd7I2VxnBhxv__T-_eXwTWI5G7FVJeV-QbhWmfZNNQb8lQ5dnlkw8Uowm2ZpNVit8n3U8v-H5LRWKRksKpfJ1QIormVaDfmt859cOlDa4M8ulzzwNf4HlH5GkW1etZ0XHGgfMaZgp5j6UE1QaHGdQjKBLMZ3VnMT_Lzx51rpA4YszKpGpaRFXIbGfzJghDFCV7NPtWCN3iS_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از حبوش، جنوب لبنان، پس از حمله هوایی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/121420" target="_blank">📅 23:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121419">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c0740884.mp4?token=KTAdXc05uJXJbKl8YN3FGuGPP6OV1fiaG26sIyWc3-bKXaT8EK_2txKN2EayS28sipj_-3lunfipv5ctkzDv4FsE0SptWxkGXc4QEGcbIeHrLr9wloVQ72W74KTXijlYAB38FBXIFmM45Z0FjW8w34YlLxexcvxPsyumgh-EW11eB773HHgetGlmQeRqYgla6k_7IjfOnL62YSnL1cFYDuOT136MwUdIQMBJ-eETxzlJ6-N11dCs6tVYBF2nywTYLAcW6giixfBY7WklXRUPAaAnpfWMe0tr7uZu1zxqwzauFn0TXRebEV1X8fDBPQh3N68M3hycI8p3WI74tKYJ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c0740884.mp4?token=KTAdXc05uJXJbKl8YN3FGuGPP6OV1fiaG26sIyWc3-bKXaT8EK_2txKN2EayS28sipj_-3lunfipv5ctkzDv4FsE0SptWxkGXc4QEGcbIeHrLr9wloVQ72W74KTXijlYAB38FBXIFmM45Z0FjW8w34YlLxexcvxPsyumgh-EW11eB773HHgetGlmQeRqYgla6k_7IjfOnL62YSnL1cFYDuOT136MwUdIQMBJ-eETxzlJ6-N11dCs6tVYBF2nywTYLAcW6giixfBY7WklXRUPAaAnpfWMe0tr7uZu1zxqwzauFn0TXRebEV1X8fDBPQh3N68M3hycI8p3WI74tKYJ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مخالفت بنیانگذار سپاه با تسلیم سپاه
🔴
محسن سازگارا که خود از بنیانگذاران سپاه پاسداران انقلاب اسلامی است و سال‌هاست در آمریکا به همراه خانواده خود زندگی میکند، در این مصاحبه با تسلیم سپاه که ایران را اشغال و زمام امور را در اختیار دارد، مخالفت نموده!
🤔
زندگی و آینده 90 میلیون ایرانی به خاطر همین سازمان تروریستی به فنا رفته بعد این آقا از وسط دل آمریکا داره دفاع میکنه ازشون
#محسن_سازگارا
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/121419" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121418">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ادعای کانال ۱۴ عبری درمورد اظهارات امروز ترامپ: باید به یاد داشته باشیم که او یک تاجر است و اظهاراتش با هدف تثبیت قیمت نفت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/121418" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121417">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a113557850.mp4?token=Buk3dKyF76uD6c60Ju6f2E7Kuvc4cbUDP7UIY3G9d-y3aeuLiArSsr5eK7pXANTKWJdbsogD4vFxU6f0L1Sem-4yg7OmMUBjaP-A_iifEQ2cfBRPlFd7qD9Zyr1U0YeVDGVvFscGTF-ByXokTRYsVlN7uLIT11OvXxGnZ23ZVXFud0ZDJ-yJ0JYvNvhUAtkqM21SF4hCBHM1ZNf-lITNqN0bvYnD4QqGXiCuVPvkGo0Xg7T44s_8vDBmuh59zcrBxrRnFAGbW1UUUTvi_g2Z7m0-BzGclH92JBxr3s8FpZU0ip88Jyp_PrFhuWogJpRXVDKi-MVSahpvWflHEu4oZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a113557850.mp4?token=Buk3dKyF76uD6c60Ju6f2E7Kuvc4cbUDP7UIY3G9d-y3aeuLiArSsr5eK7pXANTKWJdbsogD4vFxU6f0L1Sem-4yg7OmMUBjaP-A_iifEQ2cfBRPlFd7qD9Zyr1U0YeVDGVvFscGTF-ByXokTRYsVlN7uLIT11OvXxGnZ23ZVXFud0ZDJ-yJ0JYvNvhUAtkqM21SF4hCBHM1ZNf-lITNqN0bvYnD4QqGXiCuVPvkGo0Xg7T44s_8vDBmuh59zcrBxrRnFAGbW1UUUTvi_g2Z7m0-BzGclH92JBxr3s8FpZU0ip88Jyp_PrFhuWogJpRXVDKi-MVSahpvWflHEu4oZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاکانی : تنگه هرمز حق طبیعی ماعه و اصلا نباید درباره اون با آمریکا مذاکره کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/121417" target="_blank">📅 23:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121416">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
عاصم منیر فردا حامل پیام جدیدی از سوی آمریکا به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/121416" target="_blank">📅 23:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121414">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade9e3bc09.mp4?token=DGA6spIhaPINrfQLMdgGY3EMT5KdZK6dZNLttAWJB3fM9Sk3mCWslIdUiIPNQn72R485C-Gul-iLEoUGQlDvYfD5X_rbnQ5xq-JYcbsxo7ooXvCea_pqB9e8gCWh5G7lSCm7dcpzPL_NFBNwCo2GC74jz7axUcmAZYnMCcYSi8KXSyPttDnXa3-ZYT2v2IrzXyckWTdkCTyhx2B1UbsOoT0x2VtwvSRmzXyaE9XXbtKyMPx6pBFBqUQCNBJFgIi5nnZ4jX6jakz0iLRVmLcq96pahXNmzwDb_tjXv9rZRqFaijRGQGDaI6cxHniBU3u0Lhbw2wX5tDSOfV5RvT4vSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade9e3bc09.mp4?token=DGA6spIhaPINrfQLMdgGY3EMT5KdZK6dZNLttAWJB3fM9Sk3mCWslIdUiIPNQn72R485C-Gul-iLEoUGQlDvYfD5X_rbnQ5xq-JYcbsxo7ooXvCea_pqB9e8gCWh5G7lSCm7dcpzPL_NFBNwCo2GC74jz7axUcmAZYnMCcYSi8KXSyPttDnXa3-ZYT2v2IrzXyckWTdkCTyhx2B1UbsOoT0x2VtwvSRmzXyaE9XXbtKyMPx6pBFBqUQCNBJFgIi5nnZ4jX6jakz0iLRVmLcq96pahXNmzwDb_tjXv9rZRqFaijRGQGDaI6cxHniBU3u0Lhbw2wX5tDSOfV5RvT4vSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل، چند نقطه از جنوب لبنان رو زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/121414" target="_blank">📅 23:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121413">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ادعای کانال ۱۳ عبری به نقل از یک مقام ارشد اسرائیلی: در حلقه اطراف ترامپ، بر او فشار می‌آورند تا با ایران به توافق برسد، اما گزینه حمله همچنان روی میز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/121413" target="_blank">📅 23:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121412">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: نتانیاهو کمتر به احتمال رسیدن به توافق باور دارد و خواهان حمله است، در حالی که ترامپ می‌خواهد هر راهی را برای رسیدن به توافق امتحان کند؛ همین باعث تماسی تند و آتشین شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/121412" target="_blank">📅 23:10 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
