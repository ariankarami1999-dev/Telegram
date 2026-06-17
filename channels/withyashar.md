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
<img src="https://cdn4.telesco.pe/file/OqkIfdE7UyyexyzDUvqd6gaCTPcDr6J_TTdSpaj9I7CPLVNoFpYvRJZvIav4OvTDonO9T69zL_vndEPzJGTJVF3isCOcKJuDWWAM1LylOLiJx-sd6TGpZ4UuCq2Ks5Oeznn5pgMhHSNct3tAEq5arE0_dk5afJKboRxsAIzRfX_qgnG9cC6moldalgZqEuzFLsl2XjYrHUyJpM67pnFOm_fn90MO-7YMyx8LwoPAoDzDijumUqsgRX5ISkV0wiMoMdFyRYfW1JjEq-SQshmvQbLHZq2oCjr21Hy5bLFcbi59IaMtmNN0sSOiiRSrA8HK63iClERNJsEs_ItsplrmOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-15138">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تسنیم: متن توافقنامه به صورت کامل در روز جمعه و پس از امضا منتشر خواهد شد
یک منبع نزدیک به تیم مذاکره‌کننده   گفت: تفاهمنامه همانطور که پیشتر اعلام شده ۱۴ بند است و موضوعات مربوط به ۱۴ بند نیز بارها در رسانه‌ها مطرح شده، اما جزییاتی که در بلومبرگ‌ درباره هر بندی آمده است در موارد قابل توجهی ناقص است.
@withyashar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/15138" target="_blank">📅 12:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15137">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRnw-DTlwwU2oABOhyOYtb5MyWtEb6sytpNukUzyHYNGJpk9MgyB5_COaR7DQHmm-6kS1P9g47rljxxVMxc3QtIhdE6zxktNKswkZ6Xk4YO4tpl8Xx9oz2aj7I_YiBigdIH0sSFmRRcv1tSV5GyHlMHmip_KlGz89BzfCeL3OIfijWEQBfgPWXlQwhgaL1p0tt-5jyqQvwdpqlAGQ-zqI3_7laZufBivP9mc3H2LNYOgYpo_HFFfv3CaXZ5ABNNoKu8rGHiYIC9XJQuNKtRRUp3v_CXtD58ymB4PrVWmtViHssyPGHYdAD-Dl1Uxhfxh-eix0VYI68U6T1Axnie6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودرو پورشه سردار آزمون در کرمان توقیف شد
به گزارش تابناک به نقل از ایسنا، سرهنگ اکبر نجفی ۲۶ در تشریح این خبر گفت: خودروی مذکور که به دلیل تخلفات قانونی و برابر با احکام صادره در لیست توقیفی‌های مصادره اموال سردار آزمون قرار داشت، توسط گشت‌های محسوس و نامحسوس یگان امداد شناسایی و پس از طی مراحل قانونی، به پارکینگ منتقل شد.
@withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/15137" target="_blank">📅 12:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15136">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">صدای انفجار‌ سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/15136" target="_blank">📅 12:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15135">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بلومبرگ به نقل از یک منبع آگاه اعلام کرد: واشنگتن شروع به توزیع محتوای تفاهم با ایران به کشورهای متحد در اجلاس گروه ۷ در فرانسه کرده است
@withyashar</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/withyashar/15135" target="_blank">📅 12:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15134">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرگزاری فرانسه: یک گزارش حقوقی دولت آمریکا نشان می‌دهد ارتش این کشور از ابزار هوش مصنوعی گروک متعلق به شرکت اسپیس ایکس تحت مالکیت ایلان ماسک، میلیاردر حوزه فناوری در جنگ علیه ایران استفاده کرده است
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/15134" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15133">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پمپئو وزیر خارجه سابق به فاکس  می‌گوید اگر برداشت ایران از موضع آمریکا درست باشد و تصمیم‌گیران اصلی (سپاه و رهبری) واقعاً تغییر رفتار بدهند، می‌توان به عادی‌سازی و حتی ورود سرمایه‌گذاری فکر کرد، اما احتمال چنین تغییری را بسیار پایین می‌داند. او تأکید می‌کند نباید هیچ پولی—چه مستقیم، چه از طریق واسطه یا حتی
آزادسازی دارایی‌ها—به ایران داده شود، چون به‌جای رفاه مردم، صرف تقویت برنامه موشکی، سپاه و خرید تسلیحات از روسیه و چین می‌شود. در عین حال می‌گوید اگر واقعاً تغییر واقعی رخ دهد، از آن استقبال خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/15133" target="_blank">📅 10:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15132">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBaBrDKqSM8YqLI1OnybSv9Ml3C20RhMDQI9b0QWE0aR3UhJO_rp0Hlx5cGyyrICB1Ebtw0LeOv5Ssen_o9HV2DSOPlOuN3MPETaApOIKayoQWcbqbtZFOhTknUUf2YkyllHoUKWoXRHWFBzaWSUZ1A3sXrI3-IQi2XP6DcrfQ1AvPDykv2eUb49OB4_X2uxFk_HX4D3yenyV5XzM0wngi579yVT63eMiba_QG2UEz5veIyZldQv1yltcJFqzgGWqaKIFZjd7f-yIjxvDgiYye2SWqqcyUWr790LSsJ3xhRpU1rv79FNmO3WxhCNi8YOafpTVpUZBVNeQldSzc_RqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ایرباس موقت ایر فورس وان که توسط قطر اهدا شده، رنگ‌آمیزی شده و در نیویورک آماده است — درست همزمان با تعهد سرمایه‌گذاری ۱ میلیارد دلاری قطر که دیروز اعلام شد، بعد از آنچه برخی آن را تسلیم کامل آمریکا در برابر خواسته‌های قطر و ایران می‌دانند.»
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/15132" target="_blank">📅 10:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15131">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یديعوت احرونوت ادعا کرده بالای ۵۰درصد از پول‌های بلوکه شده ایران دست چین و عراقه
رقمش هم کم نیست؛ حداقل ۳۵میلیارد دلاره!
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/15131" target="_blank">📅 10:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15130">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرنگار اسرائیلی : این یک اشتباه تاریخی است.
پرداخت میلیاردها دلار به بزرگترین حامی دولتی تروریسم در جهان، فقط باعث تأمین مالی راکت‌های بیشتر، پهپاد‌های بیشتر و حملات بیشتری علیه اسرائیل و غرب خواهد شد. این سیاست «آمریکا در اولویت اول» نیست.
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/15130" target="_blank">📅 10:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15129">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c657925428.mp4?token=aat-EtukME0Nvj-M47dc7OZ3yUmjmm3WNZVTvGydl89MAXTiP0d01Vcyf1YgWQPqfxnsTGAzW69UlifVkyQw_MuUtKXnQDSJ5kXJBHR0ONZQk9L9C7L4lM8D0V8naFibrEtd9aC_031lWbC9poMzT7xg5SneHYhY4cW5cCnME5FL2eVl3tIkmJlGqePTEC1ikrfPBC9Ip-GR8Tu1Vs7ZAgiipLsA0VlYnhsFbmK-Dh-tk9wv4yonUcsFXvooYtWmxIPpzcPqsb6xjiuh4YPJXEymOGBbbQKPMVapZmxG29OMKRhqaHqZDLQ_Q2Oowy9YuS9TbCgWFfeU_TgHCnU8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c657925428.mp4?token=aat-EtukME0Nvj-M47dc7OZ3yUmjmm3WNZVTvGydl89MAXTiP0d01Vcyf1YgWQPqfxnsTGAzW69UlifVkyQw_MuUtKXnQDSJ5kXJBHR0ONZQk9L9C7L4lM8D0V8naFibrEtd9aC_031lWbC9poMzT7xg5SneHYhY4cW5cCnME5FL2eVl3tIkmJlGqePTEC1ikrfPBC9Ip-GR8Tu1Vs7ZAgiipLsA0VlYnhsFbmK-Dh-tk9wv4yonUcsFXvooYtWmxIPpzcPqsb6xjiuh4YPJXEymOGBbbQKPMVapZmxG29OMKRhqaHqZDLQ_Q2Oowy9YuS9TbCgWFfeU_TgHCnU8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پنس، معاون سابق ترامپ: «به نظر من بهتر است به نیروهای مسلح ایالات متحده اجازه دهیم کار را تمام کنند، تنگه را باز کنند و قابلیت‌های تهاجمی ایرانیان را از بین ببریم و به مردم ایران فرصتی واقعی برای آزادی بدهیم.»
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/15129" target="_blank">📅 10:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15128">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چند ساعت پیش، دونالد ترامپ با استناد به قانون تولید دفاعی (یک قانون از سال ۱۹۵۰ در دوران جنگ سرد)، دستور داد تا تولید مهمات، موشک‌ها و تجهیزات دفاعی آمریکا سریع‌تر شود. این فرمان در ۱۱ ژوئن به وزیر دفاع پیته هگست ارسال شد و مشکلات سیستمی در صنعت مهمات را هدف گرفت: ظرفیت تولید محدود، زنجیره‌های تأمین ضعیف، وابستگی‌های طولانی‌مدت و گلوگاه‌های تولید.
هدف اصلی: تسریع تولید مهمات حیاتی، موشک‌ها و تجهیزات دفاعی برای دفاع ملی آمریکا.
نحوه اجرا: قانون به ترامپ اجازه می‌دهد با شرکت‌های خصوصی توافق‌های داوطلبه ایجاد کند، تولید را اولویت‌دار کند و زنجیره‌های تأمین را تقویت نماید.
توافق مهم: شرکت لاکهید مارتین اعلام کرد با دولت آمریکا برای چهار برابر کردن تولید مهمات حیاتی به توافق رسیده است.
دلیل اقدام: کاهش ذخایر تسلیحاتی آمریکا پس از جنگ با ایران و استفاده از مهمات در ایران و ونزوئلا، که باعث افزایش سفارشات مهمات شد.
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/15128" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15127">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdyhZgQADxwlQ0cib-NmlhtLz5KwklZ5eGyVA5k_-RiNTUwJN-XRvPR82uMOXtKJJwRMkY58kmXGDRgGyjic7g5G4Uq30_1oASE6Eso7fzxmLkPMFHE-ul-NXNXYr-3mMBN72GWjFIljfpAOy5F5ean6CAsa9VFqtPvGpt9d_t-bCNn66ML99F94eoHG0pldYcMly1dhaMQwuAJpT9c8JCPGyvIzjT9jscprT84u57pUmRxMU0K-CgIbYLMlblETvPwZWC_6szUVYtaehQnZeOWxtIskA30EFafCXK7FO93nAXfhJlo5SUdg7PAS5YpSOp7LBDPKgvILivECha7C8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️ارتش اسرائیل اعلام کرد یک انبار تسلیحات جدید حزب‌الله حاوی ۵ تن مواد منفجره و ده‌ها پهپاد انتحاری را کشف کرده است
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/15127" target="_blank">📅 09:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15126">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15126" target="_blank">📅 09:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15125">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تنکر ترکرز: ۳.۸ میلیون بشکه نفت خام ایران از محاصره آمریکا عبور کرد   تارنمای تنکر ترکز بامداد چهارشنبه گزارش داد، دو ابرنفتکش ایران که مجموعا حامل ۳.۸ میلیون بشکه نفت خام هستند، از محاصره آمریکا عبور کردند @withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/15125" target="_blank">📅 09:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15124">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرنگار العربیه: جنگنده‌های اسرائیلی دو بار به شهرک‌های «انصاریه» و «المنصوره» در جنوب لبنان حمله کردند.
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/15124" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15123">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود @withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/15123" target="_blank">📅 08:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15122">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15122" target="_blank">📅 08:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15121">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، با بازنشر گزارشی از شبکه 14 اسرائیل درباره کشتار دی‌ماه، در ایکس نوشت:
«قربانیان سرکوب در ایران و خانواده‌های آن‌ها شایسته حقیقت، شفافیت و پاسخگویی هستند. جامعه بین‌المللی نباید در برابر این وضعیت بی‌تفاوت بماند.»
او گفت: «تاریخ حکومت ایران با رنج مردم خود نوشته شده است؛ اتاق‌های شکنجه، گورهای دسته‌جمعی، ناپدیدسازی اجباری و خانواده‌هایی که بدون پاسخ رها شده‌اند.»
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15121" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15120">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">منابع عربی: اسرائیل حومۀ شهرک نبطیه‌الفوقا در جنوب لبنان را هدف حملات قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/15120" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15119">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وبسایت خبری سمافور: مارکو روبیو، وزیر خارجه دولت ترامپ با انعقاد یادداشت تفاهم نامه با ایران مخالفت کرده و هیچ اظهار نظری درباره رسیدن به توافق با ایران نمی‌کند.
وزیر خارجه آمریکا امیدی به رسیدن به توافق هسته‌ای در مذاکرات با ایران پس از امضای یادداشت تفاهم نامه ندارد و تاکنون درباره امضای یادداشت تفاهم نامه با ایران کاملاً سکوت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/15119" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15118">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwiTtxXShJqJHTdk_6sgcteliW2GkggLgCkhOBLqb-8V0YH8AEM8cZTRdZfnbIq4krqwcHRIlT55KvOtlP6kN2meAl4tyjED0N9y5FjdEhBlLlASBWppg6oMzBWOo37Nu-c_1yllVl9Wz0tffpMMVJPo61d0cVGO5bwxdcOxdp77zvBltBZBQgyXOWaFe9CWXMJ-4u7MV0Be3HNLlZFvgnSaLkFp1olb3_k-CfgE_2GUY_TRPscO7-6OpmueEf6QWmtNeyAs2ghNx3V2xPiP1F4OQZ_Kq5yZoueRdBq4d7Qj6ZB3B2n8dDZf8yeh8WbvjsXTRr4rJXs-s6q5HF2-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/15118" target="_blank">📅 08:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15117">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NafGg3rs6ZbNayO8pLslCPlt04gkAnMcuQ0MJm5lhQxpbisCGrJYS7pTlOievSufEPezAZSzriQZIY1yPbBBLYsPhY0sOSY7zZtvLL_u5b3MuibG_hxJw5nyUFd9tPHG_ZK21qnN_-vWngKBN4vdsiEJ1HegwcdGudzzTzCEnOT-ql810KBqOOHLfv3jv9Gff7CGht7nsS9IKpBY3NlLXkGY285gLE8jTDc5inLcrsTrVaPgtrwTeOtafmrmOfbjzHBFpaudxhL90VPySIubIhB0uOt4-4O8-2lR8eJi3IUHq5ymB6hyOYCYNobHhN4X9Tv-Z_sqB7xlLYebpaPZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید:
«نه سلاح هسته‌ای، نه لغو کامل تحریم‌ها, نه پول»
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15117" target="_blank">📅 08:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15116">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
اگه میخوای بدونی قیمت دلار طلا خودرو .... درسال جدید چقدر میشه این چنل تمام پیشبینی ها همراه تاریخ وقوع رو گفته
🕯
@link
🕯
🕯
@link
🕯
🕯
@link
🕯</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15116" target="_blank">📅 02:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15115">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPGdg_iy1_aMouWTfZS_N-iyI-NDeAZEmKn244eaa5taB7IOtvs8zUcA-gULiG78sWpcVRAAi7rW8t2Dl4Fdbirkld1oYxaUwIWkj9-QNgZJwpbIjKbhIqpbr6PVvLTzlZKQOR7j7IbtXBtwu0i7kycrpwVfOnVmGRRN2EQq4ahO6yqgJ_rGS8urGF2SjF9Hr48H1MwpWbVjTSFq6BbfNpmzHPI0UJdIWgMgDvH5hWYgIyVFRUGr6nhsWRrq5DXGPhXECo4R0RQB9_CXUYdoOAFFR7AnL_17o4r7IqCVcj1lTn5jRuZQCux7hFjRHA8Gk9SVgxDFHPukZtUzRrr3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین  الان ، چه خبره خلیج فارس
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15115" target="_blank">📅 02:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15114">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15114" target="_blank">📅 02:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15113">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95de30e10e.mp4?token=iG0ZynP2rd2iQ4cFJOO9SPXvtMfAoLsvhCo3gixvwwLmXHGwvLZqch_p1hck1QhgIbZmXf9BOUnxPQDghEjCWnBARCI2-wnhzV_0-xOjFwR_KqXK6nSVJaIBeCc9VhR7LmpKRx5bST94UsD_sJRoToVfuwZfH-jRNlMhgIkb0uGcmJtY9Oqk2U4M7iKni6Gn1dr0ufFKB9d5UbtmzVf1WR8I7xaoelnU1hGZHQdhWa9-3JHLhnX445DHHcvvoh3fd58kZTaiPVGsjVVk4TCbHH0HgOEHdVvvhx3HN7sTJ6S1N6PORZ22KPKbdopGvFxzZacKwPk2cxAY5odODFv6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95de30e10e.mp4?token=iG0ZynP2rd2iQ4cFJOO9SPXvtMfAoLsvhCo3gixvwwLmXHGwvLZqch_p1hck1QhgIbZmXf9BOUnxPQDghEjCWnBARCI2-wnhzV_0-xOjFwR_KqXK6nSVJaIBeCc9VhR7LmpKRx5bST94UsD_sJRoToVfuwZfH-jRNlMhgIkb0uGcmJtY9Oqk2U4M7iKni6Gn1dr0ufFKB9d5UbtmzVf1WR8I7xaoelnU1hGZHQdhWa9-3JHLhnX445DHHcvvoh3fd58kZTaiPVGsjVVk4TCbHH0HgOEHdVvvhx3HN7sTJ6S1N6PORZ22KPKbdopGvFxzZacKwPk2cxAY5odODFv6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس : اگه دونالد ترامپ حتی به عنوان رهبر معظم انقلاب در ایران هم انتخاب می‌شد، دموکرات‌ها باز هم می‌گفتن آمریکا شکست خورده
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/15113" target="_blank">📅 00:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15112">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23735193e5.mp4?token=NMEe0CQFmZ9Z9QUJr-9i-mGlUzkFbikQgPRBDnuuxsBwXXUZwTKpIJeD8nRY1VVyVLZ4wfZcqxsZZNqurQM8jdcwwzFAt0e_bNMsuFZAVu5HI5y5ugngYyitXsA3zfbKN4PZXQ18C6A6969Fli8CcopUtx6IVsSm5tpqutCDGKBQfuzvCZh2ZfP4QoJYuUhsvItshGnH5gp4x8T1sMBDjLr4OW8ZcrKuz8-2COCskPbhIuporjIovClbpYett6U6D7EPjcKpkL1ThACuSAD9umcjLRN005-OoGe5BagjebZm86esav0EugmGkkiSW5CKfc_ryydP-gJSSvh3YhOCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23735193e5.mp4?token=NMEe0CQFmZ9Z9QUJr-9i-mGlUzkFbikQgPRBDnuuxsBwXXUZwTKpIJeD8nRY1VVyVLZ4wfZcqxsZZNqurQM8jdcwwzFAt0e_bNMsuFZAVu5HI5y5ugngYyitXsA3zfbKN4PZXQ18C6A6969Fli8CcopUtx6IVsSm5tpqutCDGKBQfuzvCZh2ZfP4QoJYuUhsvItshGnH5gp4x8T1sMBDjLr4OW8ZcrKuz8-2COCskPbhIuporjIovClbpYett6U6D7EPjcKpkL1ThACuSAD9umcjLRN005-OoGe5BagjebZm86esav0EugmGkkiSW5CKfc_ryydP-gJSSvh3YhOCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور جی دی ونس:
پرزیدنت ترامپ هرگز نگفت که هدفش نصب رضا پهلوی برای تبدیل شدن به رهبر جدید ایران است.
آنچه گفته این است که اگر مردم ایران بخواهند قیام کنند ، عالی است. این کار اوناست این بین آنها و دولتشان است.
چیزی که ما می خواهیم توقف برنامه هسته ای آنهاست.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/15112" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15111">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f65655673.mp4?token=R3AMR68Vz61uriYUxxjf0eYJA4ZBv6MPQg38jncG9b3urgRji5qwOtEYTnZ0D8lPeO-pk18DJyd1o-l77Jh0Ffx2clX-cNf7xZ5UjnjocI_xsjqfeO7BgUVykA6jLuUKRxcPl_1vmHuG7yfbVdQDt8UzNFZuVnUGUNIMT7DgKU7k-tunQNGnh7vSEBPV4Udkq6CkeHFQQB3PNESs-7nzt_WidcT1BViIriT86TTLhTLcFLD1MJx2xee33USrOhqAJ3X8BUDCcPznasAYouFRyFV0Gsinp7OZVwAt12PRtPBobZyIGuXAKaJvVSkENv9RUX-zdhI6t8KAAwAp1mlSpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f65655673.mp4?token=R3AMR68Vz61uriYUxxjf0eYJA4ZBv6MPQg38jncG9b3urgRji5qwOtEYTnZ0D8lPeO-pk18DJyd1o-l77Jh0Ffx2clX-cNf7xZ5UjnjocI_xsjqfeO7BgUVykA6jLuUKRxcPl_1vmHuG7yfbVdQDt8UzNFZuVnUGUNIMT7DgKU7k-tunQNGnh7vSEBPV4Udkq6CkeHFQQB3PNESs-7nzt_WidcT1BViIriT86TTLhTLcFLD1MJx2xee33USrOhqAJ3X8BUDCcPznasAYouFRyFV0Gsinp7OZVwAt12PRtPBobZyIGuXAKaJvVSkENv9RUX-zdhI6t8KAAwAp1mlSpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور در به در دنبال  دکتر خوش چشم هستم که او را به صنعت فوتبال وارد کنم
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/15111" target="_blank">📅 00:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15110">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">همکنون
انفجار های مهیب در جنوب لبنان،
گزارش های محلی از شلیک گسترده تانک های اسرائیلی و درگیری شدید با نیرو های حزب الله در تلاش برای پیشروی در جنوب لبنان.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/15110" target="_blank">📅 00:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15109">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اورشلیم پست: ماهواره‌های اسرائیلی در طول حدود ۴۰ روز اجرای عملیات «غرش شیران» بیش از ۵۰ هزار بار از ایران تصویربرداری کردند
میانگین هر روز بیش از هزار تصویربرداری
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/15109" target="_blank">📅 00:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15108">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جی‌دی ونس: برخی خواهان اعزام صدها هزار نیروی آمریکایی به ایران هستند
ترامپ جورج بوش نیست؛ در باتلاق ایران گرفتار نمی‌شویم
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/15108" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15107">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">واکنش آمیت سیگال خبرنگار کانال 12 اسرائیل به توافق ترامپ:
ممکنه دشمنی با آمریکا خطرناک باشه، اما دوستی با آمریکا مرگباره!
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/15107" target="_blank">📅 00:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15105">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال ۱۳ اسرائیل: ترامپ مانع اجرای یک عملیات نظامی‌برنامه‌ریزی‌شده اسرائیل در غزه شد
این طرح در بالاترین سطوح سیاسی و امنیتی اسرائیل بررسی شده بود، اما پس از ارائه جزئیات به آمریکا، واشنگتن با آن مخالفت کرده و خواستار عدم اجرای آن در شرایط فعلی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/15105" target="_blank">📅 23:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15103">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">با این جماعت چه کنم
😞</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15103" target="_blank">📅 23:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15102">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArtin</strong></div>
<div class="tg-text">اسکل عقده ای یه پیام رو جواب نمیدی
عقده ای هستی زیاددد</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15102" target="_blank">📅 23:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15101">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شاهزاده رضا پهلوی به نیوزنیشن: مردم ایران اکنون میگویند چرا بمباران متوقف شد؟ ایالات متحده باید بمباران ایران را ادامه میداد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15101" target="_blank">📅 23:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15100">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش حملات پهپادی سپاه پاسداران به اربیل عراق
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15100" target="_blank">📅 22:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15099">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به گزارش ان‌بی‌سی نیوز، کارشناسان ارشد صنعت نفت هشدار می‌دهند که علیرغم فضای مثبت ناشی از توافق میان ایالات متحده و ایران برای پایان دادن به جنگ چندماهه در خاورمیانه، بازگشت بازارهای نفت به حالت عادی و از سرگیری تردد در تنگه هرمز فرآیندی زمان‌بر است و احتمالاً چندین هفته به طول خواهد انجامید.
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/15099" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15098">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHsc2gZ2ojT3Kflv9Sv4UexsYpqdzhRiXeAVPyCusuyNsbH5ErrdDZ7QTVqU4FObpbk7aAZ7V4pBvPrY9fxHV1tERMgcg-CjRinqiksNEg85zX1bJbeyqw6x6FahDzGhq9sjwwvwDw1_VjHcZGB-bp3G1inUa4Om_FDF_BjnUAr98_m9GvXwITagjArdoPpd5gKAAVRmCBDDr3W788JwtvVvjT26-ag3TiFGSL1U_WLLI1ANdILw_R_QZsIES8S-w8PepA6_Ekv7df1gwdGfWXD_zPLh04Ho_qgl87g04B6HtTYycTFzO0iH-s-J4qLvC79Oj9_E130TsgbvyHkxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پایگاه موشکی دیگر در شامل شش ورودی زیرزمینی، در حال ساخت است. یکی از دلایل احداث ورودی‌های بیشتر، قرارگیری این پایگاه در ناحیه‌ای استراتژیک از ایران می‌باشد
بخشی از فرایند ساخت پایگاه مذکور، پس از جنگ 12 روزه صورت گرفته است، هم‌چنین برخی از سازه‌های روزمینی این پایگاه در دو جنگ اخیر هدف قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/15098" target="_blank">📅 22:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15097">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b21de6065.mp4?token=F-gGIu8uzIZSgACa0nNC-gXpGPkxBNQyeaAETUYWE9Tk1M8DzFnxdPm7YQ1I8qCeV3TkinZiR0au2lDw6pGP7wtyYj5ya_XCyxYy5ixTOcfC6__Hp7RTQEJWCcSzwMnoAyiF3fsPIN5GKgQx_pOOvJ0Q7qp7g3zfVk4NPHdHy8vjADOBM6C9uuaxHSb9ZAb-Kxh0IuxYHTf-kwu5MEQJR1W-yXKFAgyig-pkn0lvFRdHt-STQDLRQqsAvh3-Eh0YEuuAY-7F0UufHV0D7nssv9zihjUOmB21p6LYxoTUDmvrynxUlWTg_L-zGOP5Bur_h4ooXqCGuae2D5mbzfWvCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b21de6065.mp4?token=F-gGIu8uzIZSgACa0nNC-gXpGPkxBNQyeaAETUYWE9Tk1M8DzFnxdPm7YQ1I8qCeV3TkinZiR0au2lDw6pGP7wtyYj5ya_XCyxYy5ixTOcfC6__Hp7RTQEJWCcSzwMnoAyiF3fsPIN5GKgQx_pOOvJ0Q7qp7g3zfVk4NPHdHy8vjADOBM6C9uuaxHSb9ZAb-Kxh0IuxYHTf-kwu5MEQJR1W-yXKFAgyig-pkn0lvFRdHt-STQDLRQqsAvh3-Eh0YEuuAY-7F0UufHV0D7nssv9zihjUOmB21p6LYxoTUDmvrynxUlWTg_L-zGOP5Bur_h4ooXqCGuae2D5mbzfWvCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئو احمدی‌نژاد بعد از توافق
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/15097" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15096">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68844ebd5c.mp4?token=RCNOHxm8tWfqi0wvsl_CR7HzCGUilIrp2vgOXgQj81fwm9O0vQMTrSH8gjMiU1ysjWHU5xLuNmGBUCngH8wcT2SoCPonO0JpiQ4rr77fzQnsB38BeikJc7mw5XS3VK_jru3LpnVlN9UndlKygvrKTzFGVNqZH28Vir6jZ6xAWi-KtmRbpBR46ZUTikT-VxYtiuaN36IU9VxityJC_ixSVp3tCJLaxgg6GT3qgI41gbg3-LQAdI1YzlxGLOxiEQA0qUuNDGzvdFdSRscM7y2ukp9kbzzdTXMM9zDNdFs00zAfsRUfXz0MsW6plyO16ySYrONRP6w-QjNv7xvJitsI1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68844ebd5c.mp4?token=RCNOHxm8tWfqi0wvsl_CR7HzCGUilIrp2vgOXgQj81fwm9O0vQMTrSH8gjMiU1ysjWHU5xLuNmGBUCngH8wcT2SoCPonO0JpiQ4rr77fzQnsB38BeikJc7mw5XS3VK_jru3LpnVlN9UndlKygvrKTzFGVNqZH28Vir6jZ6xAWi-KtmRbpBR46ZUTikT-VxYtiuaN36IU9VxityJC_ixSVp3tCJLaxgg6GT3qgI41gbg3-LQAdI1YzlxGLOxiEQA0qUuNDGzvdFdSRscM7y2ukp9kbzzdTXMM9zDNdFs00zAfsRUfXz0MsW6plyO16ySYrONRP6w-QjNv7xvJitsI1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد اینهمه شب تو خیابون رفتن، آخرش بهت میگن اقلیتی تندرو
🤣
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/15096" target="_blank">📅 22:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15095">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا:
اسرائیل تو دو روز گذشته پس از اعلام پایان جنگ توسط رئیس ترامپ، 84 بار آتش بس تو جنوب لبنان رو نقض کرده و همچنان به جنایات و کشتار مردم لبنان ادامه میده.
هشدار میدیدم اگر اسرائیل به شرارت‌هاش ادامه بده، باید منتظر پاسخ سخت نیروهای مسلح جمهوری اسلامی ایران باشه.
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/15095" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15094">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی: در صورت بدعهدی آمریکا، پاسخ  ایران، نظامی و کوبنده خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15094" target="_blank">📅 22:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15093">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15093" target="_blank">📅 22:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15092">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">12 بند توافق ایران و امریکا به گفته باراک راوید خبرنگار ‌آکسیوس :
-ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان. ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند.
-ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
-ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
-ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
-ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
-ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
-ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
-اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد.
-هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود. ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد.
-مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/15092" target="_blank">📅 21:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15091">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نفتالی بنت(نامزد نخست وزیری اسرائیل) در پخش زنده خطاب به جمهوری اسلامی: باور دارم به زودی یه دولت جدید در اسرائیل میاد و امیدوارم من رهبری اون دولت رو به دست بگیرم. از همینجا به رژیم ایران میگم؛ من قراره بدترین کابوس شما باشم، تاوقتی مردم ایران رو از دست شما…</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/15091" target="_blank">📅 21:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15090">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شبکه خبر: تمام کسایی که توی بیت رهبری بودن کشته شدن جز مجتبی خامنه‌ای @withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/15090" target="_blank">📅 21:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15089">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شبکه خبر: تمام کسایی که توی بیت رهبری بودن کشته شدن جز مجتبی خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15089" target="_blank">📅 21:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15088">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b67afa5b.mp4?token=JnyNLhvTNuSYgQJ3cmjUckKlb8Xg577YD2oXT_jfbw78kEUMd9mJWe8-XTChC24yvx542kVEB9W6KOvygK7Nw6qFecAtzaiqAZaQG1cYy9x0_gf8ulJYsO9rWzbRxyRwkCVmOMOAsO23nWsxAvbiaLU89erqNLFjK42tnzkeRSkjqtAaNv3VuBHZgWBYUU2DcK8DVon-FLoF3scg1s0OY9y2u3NWo3kFt3xVXprwoj0_7jKz3-rgqz4G_gKwOZBxCWiuTcQBSnUckIHuGYjNYDR1lyAVK_oeQaTIrZ3LzM7gfbptNTC3pU0HhNvWerkysGs-VK2Guvw6-I-3yuAV7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b67afa5b.mp4?token=JnyNLhvTNuSYgQJ3cmjUckKlb8Xg577YD2oXT_jfbw78kEUMd9mJWe8-XTChC24yvx542kVEB9W6KOvygK7Nw6qFecAtzaiqAZaQG1cYy9x0_gf8ulJYsO9rWzbRxyRwkCVmOMOAsO23nWsxAvbiaLU89erqNLFjK42tnzkeRSkjqtAaNv3VuBHZgWBYUU2DcK8DVon-FLoF3scg1s0OY9y2u3NWo3kFt3xVXprwoj0_7jKz3-rgqz4G_gKwOZBxCWiuTcQBSnUckIHuGYjNYDR1lyAVK_oeQaTIrZ3LzM7gfbptNTC3pU0HhNvWerkysGs-VK2Guvw6-I-3yuAV7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت(نامزد نخست وزیری اسرائیل) در پخش زنده خطاب به جمهوری اسلامی:
باور دارم به زودی یه دولت جدید در اسرائیل میاد و امیدوارم من رهبری اون دولت رو به دست بگیرم.
از همینجا به رژیم ایران میگم؛ من قراره بدترین کابوس شما باشم، تاوقتی مردم ایران رو از دست شما آزاد نکنم دست بردار نیستم.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/15088" target="_blank">📅 21:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15087">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15087" target="_blank">📅 21:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15086">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شبکه ۱۳ اسرائیل: امروز یه نشست اضطراری تو دفتر بنیامین نتانیاهو برگزار میشه تا بررسی کنن چطور میشه بین جبهه ایران و لبنان تفکیک ایجاد کرد و با این شاهکار ترامپ کنار اومد.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15086" target="_blank">📅 21:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15085">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/15085" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15084">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">@withyashar
استادیوم</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/15084" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15083">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMona</strong></div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/15083" target="_blank">📅 21:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">@withyashar
بی‌بی و ترامپ
mma رو  گفتم wwf</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/15082" target="_blank">📅 20:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15081">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=aC65saxvMij8-HwbJNeW53j9KkNabThgdl583gz4RlGQIaai3jB1dGE8qDbb2EI2Amhgp4hGnYJ5MVjv4-BWgSuufp_X2EolXE2u8UdFrNmGAS_FftHDbnFxKaKmbFvt-h7-7n_wM_ZKI69TdAV4oqFHHZQegYC6CQshu8TmCi_regmU_M28h3NwNX42Wv0d889OFn6XwDfCn9cOHyPPZgoG7e9eDVfSptoZIrBB4Tv63JCA4uSoZdipLajNLKEUoVZTvxVkNa-qcREPqjllhghWqFqeAAbzLOjPOs59A6SbpWP25qBaeDMMsdU8JUfMHJZj3mfuic7Hxq76YvAsQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=aC65saxvMij8-HwbJNeW53j9KkNabThgdl583gz4RlGQIaai3jB1dGE8qDbb2EI2Amhgp4hGnYJ5MVjv4-BWgSuufp_X2EolXE2u8UdFrNmGAS_FftHDbnFxKaKmbFvt-h7-7n_wM_ZKI69TdAV4oqFHHZQegYC6CQshu8TmCi_regmU_M28h3NwNX42Wv0d889OFn6XwDfCn9cOHyPPZgoG7e9eDVfSptoZIrBB4Tv63JCA4uSoZdipLajNLKEUoVZTvxVkNa-qcREPqjllhghWqFqeAAbzLOjPOs59A6SbpWP25qBaeDMMsdU8JUfMHJZj3mfuic7Hxq76YvAsQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15081" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15080">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from자</strong></div>
<div class="tg-text">یاشار اخبار خیلی دارن میگن که شکاف به شدت زیاد شده بین بی بی و ترامپ
به نظرت زرگریه یا واقعا ترامپ پشت اسرائیل رو خالی کرده ؟</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/15080" target="_blank">📅 20:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15079">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شبکه ۱۲ اسرائیلی به نقل از یک منبع امنیتی:
کاهش محسوس در عملیات‌های ارتش اسرائیل در لبنان
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/15079" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15078">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دلار ۱۵۲،۹۰۰
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15078" target="_blank">📅 20:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/15077" target="_blank">📅 19:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj7HIGwZKhBrD1ysH8R1yYZYWoWKMz1rRNbZcTekLXTWR1uPNIfRd-wl1FLI383i4x-KVUSBvsVRl5DXbP-w2jrSZMsmtzIGzOdPwQrrr61757TDBkre43sn860j_RxFo0FtFRTFcatpUQLSuxxwtLIpgJ7fV262J6le1PvJRi_pmD64yjHUPppnAXxPy1j5A0ZSaIMSc9X3Cp8PbB2Dc7IOrRFUmtEmPQYpDWfn08EsCP7AtvAFgtJ40mPICGKeIF9nLMM54Vfxc3mCDBF3cmAEZZngY_tnw3TypM0j--_om03MawvNFjbrxfMMqksyKi5CzH_Dcg0FtDY7z1SCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقتصاددان سابق ترامپ می‌گوید توافق ایران به معنای رونق اقتصادی بزرگ برای ایالات متحده است
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/15076" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf6dxBJ-t0io7J74YJ248FeW3QV-7SEaFZWUDAhtk38-QqbLFut6czz6a1_yqICM7y_zp4fjztpqBNhJS63K0xlCzGuuvFJHZhDRe00NONtfyoZEt9CGak9_u3VxKSnsFVvB1_od4cUDiwWT5ahCREUSSkEmQZuK2KNJDSGSxy4MTXlr3pBu2OmCs8igyKXBez3ar_r5iQJ_AaiUis3q0P4n2PvKwNGdHFQ0gyEoqzVBFFdhyAVP7tSBz1VvVNLCruSNqN4-cpgot25Z_6Uj0zN7oor3asO2b3kwZTRfg4l5ASDAxrsach-DVK5rCAb5vJcLhtLjBvq4r5Ib5EpUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته ایلان ماسک ۱۶۵ میلیارد دلار سود کرد و ثروتش به ۱.۳ تریلیون دلار رسید
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15075" target="_blank">📅 19:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نفتالی بنت، نخست وزیر سابق اسرائیل:
توافق فعلی بین جمهوری اسلامی و آمریکا فقط یک توافق موقته.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15074" target="_blank">📅 19:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15073">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعای وال استریت ژورنال: واشنگتن به تهران اجازه خواهد داد تا بلافاصله فروش نفت و سوخت را طبق توافق پایان جنگ آغاز کند
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/15073" target="_blank">📅 19:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دلار ۱۵۳،۵۰۰
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15072" target="_blank">📅 19:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15071">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf74c8a754.mp4?token=FfHSvWVp6qJ6dY7ftCCXiD3PWYfRLc7CYa7ZsK0NlOdvv6HVdvh-ABIr5IgJDzLZGmH4zBBdMc-lJl23n6LWJDw4l0zJW8IJYm2Y4BAD3lwZ3LsVJfUghOEH6x63Om2l_IN-YBbYMPpC8bm0gadI_EuwcqhMl-dxIbWCZu43s7YsGf_ewYRD5EXX34TF0V5OFTzlCv0pn_qPxtaO1xvK_djVRdJz7bkCK9571inOH6CCQMkE1xY9q7JXHnIly25Bo53f37tIqxD5qQkv99WKMLt9VUpLRc-FSHuQgD-2Lbt_vOmRBEM_dQiZSmm-qhO-fSsduwp8k-C-UPB6oU-uaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf74c8a754.mp4?token=FfHSvWVp6qJ6dY7ftCCXiD3PWYfRLc7CYa7ZsK0NlOdvv6HVdvh-ABIr5IgJDzLZGmH4zBBdMc-lJl23n6LWJDw4l0zJW8IJYm2Y4BAD3lwZ3LsVJfUghOEH6x63Om2l_IN-YBbYMPpC8bm0gadI_EuwcqhMl-dxIbWCZu43s7YsGf_ewYRD5EXX34TF0V5OFTzlCv0pn_qPxtaO1xvK_djVRdJz7bkCK9571inOH6CCQMkE1xY9q7JXHnIly25Bo53f37tIqxD5qQkv99WKMLt9VUpLRc-FSHuQgD-2Lbt_vOmRBEM_dQiZSmm-qhO-fSsduwp8k-C-UPB6oU-uaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس فدرال آمریکا (FBI) در جشن تولد ترامپ، پهپادی که قصد ترور وی را در کاخ سفید داشت شناسایی و خنثی کرد!!
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/15071" target="_blank">📅 19:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15070">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری وابسته به سپاه:
اسرائیل آتش‌بس در لبنان را نقض کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15070" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15069">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618d127639.mp4?token=DvI1KQedept2uNzPTkut822Vv4o1fxh_6h6vPanmXqq9ZkCX9xPcnFpyjlXF4MKh_ZxjLLsjMFE5b1uZBU_7cYm5ZoEDum6WL_iAWzGNoaNsxtqKdaIzdUYFiLLg5y5AHFkOSuDeWoGDSiEEF0_lWCVrbjwSbksj8eqplr3EIkO1qFAqyHq5ihuVmmiMDmJXt9wdN-fRpKxHM1TXiFiBCLPEON9YEq218NNjV4qK3InSTgke1DGgjHxSXTV7re62rgimW7QW0PUXfWEUkHirKZTSidBTwsKYJFl7Sj8FHgdFyRdRkFv-SEiwrkhdxmeM_2igVUOpECHvwylWTyMvwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618d127639.mp4?token=DvI1KQedept2uNzPTkut822Vv4o1fxh_6h6vPanmXqq9ZkCX9xPcnFpyjlXF4MKh_ZxjLLsjMFE5b1uZBU_7cYm5ZoEDum6WL_iAWzGNoaNsxtqKdaIzdUYFiLLg5y5AHFkOSuDeWoGDSiEEF0_lWCVrbjwSbksj8eqplr3EIkO1qFAqyHq5ihuVmmiMDmJXt9wdN-fRpKxHM1TXiFiBCLPEON9YEq218NNjV4qK3InSTgke1DGgjHxSXTV7re62rgimW7QW0PUXfWEUkHirKZTSidBTwsKYJFl7Sj8FHgdFyRdRkFv-SEiwrkhdxmeM_2igVUOpECHvwylWTyMvwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند عرزشی هم صداش در اومد
@withyashar
اینو پیدا کنین استخدام کنم اتاق جنگ سبک منو داره میره
🤣</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15069" target="_blank">📅 18:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEoDxH-4f-XU7sSZ158DyZG_uhz3Ej0h4Huj5V5pDydI39ZWZe4hJ7fNyzUrlBgmR4-3k--p7XjqokqtdnJOvm9_0QZLrctw0wLtHynW929YW_q76HLGu-jL6-GqI1-KiumnOUCXIxcGSele9r5oojnXnvc51GV8MdwiyKPfoCQOD7H-FgDwqnBz4w3K06xiWeT4HPitK8iKK2fJUntlTjSmYbPJqNTn_TgFCVgphRJoDx7aC7kyR1fr1XqratF8s2EAstvf3m_XpoN48u893TnKxB-eS40DQLytjGm7zhxoF9SY2rWyHW-b1pRfIK_M9o2CeJTvXzjioC2Ib1YuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراپ سایت: ایران برای تحلیل رفتار ترامپ، دوتا روانشناس به تیم مذاکره کننده اضافه کرده
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15068" target="_blank">📅 18:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15067" target="_blank">📅 18:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صداوسیما : همین که اول بازی پرچم ایران توی خاک آمریکا به اهتزاز در اومد یعنی ما بردیم. دیگه نتیجه بازیا خیلی مهم نیست
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/15066" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15065">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4feef4c4.mp4?token=KyWNIkLtE478oMr0ggA6RnJpjPI1YRBtXnamdLCBzRbmVMXt-UJZ1kV52yjrobZUfzUK9PoopjmkRZy5ICK1Cn38ecO5CsXVvo76Hj3b-tCWnV_3m-HWlPXFRBWKxHgbx7ciqvjgkbhgQPNtJH1FGZlldM5OExSNFYgU1D2XBot-Zmr7ojtcSKRSCrnbxkYjJ2hGZuI-W54g_QHcofNccjkfOwK12d6z5KzxiMUNVxbWP2WFXSuZ_1dR1Nt3D39c6jbOL5eL-X2Szk1evQP9gUU3yUSuvhDeRhXNM6JFjPT6xlZljYnN5Peme_S_4Y4dvqs9rOOT2Zi0hVSoTuw8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4feef4c4.mp4?token=KyWNIkLtE478oMr0ggA6RnJpjPI1YRBtXnamdLCBzRbmVMXt-UJZ1kV52yjrobZUfzUK9PoopjmkRZy5ICK1Cn38ecO5CsXVvo76Hj3b-tCWnV_3m-HWlPXFRBWKxHgbx7ciqvjgkbhgQPNtJH1FGZlldM5OExSNFYgU1D2XBot-Zmr7ojtcSKRSCrnbxkYjJ2hGZuI-W54g_QHcofNccjkfOwK12d6z5KzxiMUNVxbWP2WFXSuZ_1dR1Nt3D39c6jbOL5eL-X2Szk1evQP9gUU3yUSuvhDeRhXNM6JFjPT6xlZljYnN5Peme_S_4Y4dvqs9rOOT2Zi0hVSoTuw8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند.
اگر این کار را بکنند، عالی است. اگر نکنند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/15065" target="_blank">📅 18:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15064">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ونس به فاکس نیوز:
ما پیروز شدیم، چه ایران روش خود را تغییر دهد و چه تصمیم بگیرد به توافق پایبند نباشد
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/15064" target="_blank">📅 18:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15063">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال 12 اسرائیل: اسرائیل درخواست دیدن یادداشت تفاهم بین آمریکا و ایران رو داشت اما این درخواست رد شد.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/15063" target="_blank">📅 17:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15062">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: ممکنه یه کنفرانس خبری برگزار کنم و متن یادداشت تفاهم آمریکا و ایران رو با صدای بلند و کلمه به کلمه بخونم تا رسانه‌ها اونو به درستی پوشش بدن.
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/15062" target="_blank">📅 17:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15061">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: اگه لیندسی گراهام بیاد و به این توافق با ایران شک کنه و حرفی بزنه، واقعاً براش دردسر درست می‌شه و حسابی به مشکل می‌خوره.
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/15061" target="_blank">📅 16:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15060">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آکسیوس: جان رتکلیف، مدیر سیا، به دونالد ترامپ و مقام‌های ارشد آمریکا گفته ارزیابی‌های اطلاعاتی نشان می‌ده ایران احتمالا تمایل واقعی به اجرای تعهدات هسته‌ای خودش نداره.
گفته می‌شه تفاوت میان حرف‌های داخلی مقام‌های ایرانی و آنچه به مذاکره‌کنندگان آمریکایی گفتن، باعث این نگرانی شده.
مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر دفاع آمریکا، هم نگرانی مشابهی دارن.
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/15060" target="_blank">📅 15:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15059">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، سه‌شنبه 26 خرداد از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی، دو زندانی سیاسی بازداشت‌شده در اعتراضات دی‌ماه در استان سمنان خبر داد. میزان اتهام آن‌ها را «افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد در شهرستان…</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15059" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15058">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6041510c69.mp4?token=YgKZ3-aZV9bsdmpiC_neMfHXjI6zS1o4B1bFJwZluvIPQsIhWS_2skjmUzhfqJlXp78TwS3yW0YtUCa3VCYV_PYwu0DeUxa2nhydsB4OIJ2G4l9M_Ntz7HexRi5C1Z9T7fWs9PV_JN8JRL4iTaIM4H_Ra6PJqHUI-uuxdB2iCNBe7LPYAiFgRd1MCFtIEc4L5HvmHhGIFvDWTrh46bZCWeP6hk0t92gDvw0YSe49zJ0QwYxhBXZrgo-AbsokgH28T--iweYGSx334uwOFrOQBqErq-LVHa-waOwcGTvorKUA3wNSHWpoHsBRQ1nbDixaMAiNfXc78uEsHfuBAlqfeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6041510c69.mp4?token=YgKZ3-aZV9bsdmpiC_neMfHXjI6zS1o4B1bFJwZluvIPQsIhWS_2skjmUzhfqJlXp78TwS3yW0YtUCa3VCYV_PYwu0DeUxa2nhydsB4OIJ2G4l9M_Ntz7HexRi5C1Z9T7fWs9PV_JN8JRL4iTaIM4H_Ra6PJqHUI-uuxdB2iCNBe7LPYAiFgRd1MCFtIEc4L5HvmHhGIFvDWTrh46bZCWeP6hk0t92gDvw0YSe49zJ0QwYxhBXZrgo-AbsokgH28T--iweYGSx334uwOFrOQBqErq-LVHa-waOwcGTvorKUA3wNSHWpoHsBRQ1nbDixaMAiNfXc78uEsHfuBAlqfeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با پراید رفته دم لانچر در حال شلیک
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/15058" target="_blank">📅 15:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15057">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری دولتی ایسنا:
محاصره دریایی آمریکا در حال لغو شدن است
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15057" target="_blank">📅 15:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15056">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=u6E_aRmW8f5MDELGb2SBqB2_3OCs9mcl2f8-NxjrwYc9vEcc4GTX39hjI_CdED6O3GRPotT_zAWaX3rjHC3NKtSd6XaWkommgKVoBx_t2ptqmeQeKdRsqsznHBjV6PaJS3fVG6t6bPRe7A5TFY-Yss9RTJL1ofFyiYrcIQ1vYtylkfNbExtl_dBAwHzHSf7eb8no7YVyp77oQcsy3kBtFTCk15OeaQUg4EWBV0ZnJLiLF5c6nJlUZ0AdzIfzHJVNOXy4y6aZlHjVwf-jlT2agFtBl4t-g8l1Ijm-DZ7fIl2vmLBLYidscQjEf5RAF1aSytWwz3UvSaxZ8RvuTIoOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=u6E_aRmW8f5MDELGb2SBqB2_3OCs9mcl2f8-NxjrwYc9vEcc4GTX39hjI_CdED6O3GRPotT_zAWaX3rjHC3NKtSd6XaWkommgKVoBx_t2ptqmeQeKdRsqsznHBjV6PaJS3fVG6t6bPRe7A5TFY-Yss9RTJL1ofFyiYrcIQ1vYtylkfNbExtl_dBAwHzHSf7eb8no7YVyp77oQcsy3kBtFTCk15OeaQUg4EWBV0ZnJLiLF5c6nJlUZ0AdzIfzHJVNOXy4y6aZlHjVwf-jlT2agFtBl4t-g8l1Ijm-DZ7fIl2vmLBLYidscQjEf5RAF1aSytWwz3UvSaxZ8RvuTIoOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران حتی یک بار به ترکیه حمله کرد، من هرگز این را درک نکردم، هیچ‌کس آن را درک نخواهد کرد
این مشکل است، آن‌ها کاملاً غیرمنطقی هستند و اکنون آن افراد رفته‌اند، فکر می‌کنم ایران اکنون رهبری منطقی دارد!
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/15056" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15055">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش روزنامه New York Post می‌گوید که پلیس فدرال آمریکا (FBI) پنج نفر را به اتهام طراحی یک حمله به رویداد «UFC Freedom 250» در روز تولد ترامپ که در محوطه چمن جنوبی کاخ سفید برگزار شد، بازداشت کرده است. گفته می‌شود این طرح شامل استفاده از پهپادهای انفجاری، تک‌تیراندازها و همچنین تلاش برای نفوذ و شکستن دروازه‌های محل بوده است.
بر اساس این گزارش، FBI در تاریخ ۱۰ ژوئن از وجود این توطئه مطلع شده و سپس طی یک عملیات چندایالتی اقدام به بازداشت افراد کرده است. مقام‌ها می‌گویند در جریان تحقیقات، چت‌های رمزگذاری‌شده در اپلیکیشن Signal کشف شده که بیش از ۲۰ کاربر در آن‌ها حضور داشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/15055" target="_blank">📅 15:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15054">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=A8Z7DQjN08doEOqMX5WDutT6V94U9QImoalO6VzgdZ2KhadhCfp-8Yfs0J5GI29Gsz35GMlHWzlHzgag_I5ZYfxcJoWliQ5JzoHa4O-DEwV_Q9BqWUjkgR_sTURCs6d9eFd72i2FA-FWxfUzH99IR73hCUQYq6XWHStCkHJ-29rpy-NBE8UhcBHP-LPUTubtrGguuMMu4PHOcRtFRq500dBgyU0FfQaXPjoYt2IaLLqXg6ht01c3gnlE6YgMZHZ4GProK2Ia7EC9-E0G5utCyZmAWiKF9w7zGnnJ_hWn5oNQPnxW5ctxaglTT-uSvBf7Nt-rAeAymVUCsqjj3o90yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=A8Z7DQjN08doEOqMX5WDutT6V94U9QImoalO6VzgdZ2KhadhCfp-8Yfs0J5GI29Gsz35GMlHWzlHzgag_I5ZYfxcJoWliQ5JzoHa4O-DEwV_Q9BqWUjkgR_sTURCs6d9eFd72i2FA-FWxfUzH99IR73hCUQYq6XWHStCkHJ-29rpy-NBE8UhcBHP-LPUTubtrGguuMMu4PHOcRtFRq500dBgyU0FfQaXPjoYt2IaLLqXg6ht01c3gnlE6YgMZHZ4GProK2Ia7EC9-E0G5utCyZmAWiKF9w7zGnnJ_hWn5oNQPnxW5ctxaglTT-uSvBf7Nt-rAeAymVUCsqjj3o90yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدراعظم آلمان در جی۷ پیراهن «ترامپ ۴۷» را به رئیس‌جمهور آمریکا اهدا کرد
@withyashar
خانواده دونالد ترامپ ریشه آلمانی دارند. پدربزرگ او، فریدریش ترامپ، در شهر کالشتات آلمان به دنیا آمد. او در سال ۱۸۸۵ و در شانزده سالگی از آلمان به ایالات متحده آمریکا مهاجرت کرد. پدر ترامپ، فرد ترامپ، در آمریکا متولد شده بود و شهروند آمریکا محسوب می‌شد، اما از طرف پدری کاملاً تبار آلمانی داشت. از سوی مادر نیز ترامپ ریشه اسکاتلندی دارد. مادرش، مری آن مک‌لئود ترامپ، در جزیره لوئیس در اسکاتلند به دنیا آمد و بعدها به آمریکا مهاجرت کرد</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/15054" target="_blank">📅 15:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15053">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ با انتقاد از نتانیاهو  :
لازم نیست هر بار که دنبال کسی می‌گردی، یک ساختمون آپارتمانی  خراب کنی.
تو اون خونه ها ادم های زیادی زندگی میکنن و همه عضو حزب الله نیستن
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/15053" target="_blank">📅 14:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15052">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7693c44486.mp4?token=SAIbRP7Cdp_uYXk_GLWt80LWBnk_mBN4SLWJ7TCVafXjEBInY4xJCj6pXavGW1AMbwXB_A21Ct28W5iOHIM1-8EOynEUwYDAozuqB7GVttpDoQTPPnY0iD-TYMdOnXviX4a2tCn_6MAhLNc9R67BiBsEAjY_lfdq0zNNhV6JGNbN5o-Yf5GhD9eVw7rircx2x57qZAgeE4MbNKpKq6UsxPQWdraoFHLmGBIZERcNWfqCLSUnui6Gre3ysAbJygLK8MJh0eMK8ZQDBN6QoV1lgDnAJZ7ZqNB7gJAOh8J3D4L0Ehj5tIT-QXaEyDcACjyxiqEwUcDSJmEHQ5Y0-G-RgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7693c44486.mp4?token=SAIbRP7Cdp_uYXk_GLWt80LWBnk_mBN4SLWJ7TCVafXjEBInY4xJCj6pXavGW1AMbwXB_A21Ct28W5iOHIM1-8EOynEUwYDAozuqB7GVttpDoQTPPnY0iD-TYMdOnXviX4a2tCn_6MAhLNc9R67BiBsEAjY_lfdq0zNNhV6JGNbN5o-Yf5GhD9eVw7rircx2x57qZAgeE4MbNKpKq6UsxPQWdraoFHLmGBIZERcNWfqCLSUnui6Gre3ysAbJygLK8MJh0eMK8ZQDBN6QoV1lgDnAJZ7ZqNB7gJAOh8J3D4L0Ehj5tIT-QXaEyDcACjyxiqEwUcDSJmEHQ5Y0-G-RgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : اگر رژیم ایران به کشتن مردم خودش ادامه دهد، آیا شما همچنان این معامله را پیش خواهید برد؟
ترامپ: ما با آنها در این باره صحبت کردیم. بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، بسیار بیشتر از الان.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/15052" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15051">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرگزاری msn
: ترامپ و کنگره به هگسث و روبیو اعلام کرده‌اند اگر با توافق با ایران مخالفت کنند ، از سمت خود برکنار خواهند ‌شد
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/15051" target="_blank">📅 14:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15050">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: جنگ لبنان مسئله فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم که از حمله آنها به بیروت خوشم نیامد
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد
من از نتانیاهو ناامید نیستم. ما رابطه بسیار خوبی داریم
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15050" target="_blank">📅 13:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15049">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: من به تغییر رژیم اعتقاد ندارم. سال‌هاست که تغییر رژیم‌ها را دیده‌ام و هیچ‌وقت نتیجه نمی‌دهند!
فکر می‌کنم توافق با ایران عادلانه است
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/15049" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15048">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ:
می‌خواهیم اورانیوم غنی‌شده را از ایران بگیریم
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/15048" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15047">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: ما می‌خواستیم برای دریافت اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/15047" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15046">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: تلاش‌هایی برای تغییر رژیم در ایران صورت گرفت، اما موفق نشدند.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، اطمینان از این بود که ایران سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال دستیابی به سلاح هسته‌ای باشد، جهنمی به پا خواهد شد.
ما از نحوه مدیریت امور توسط قطر در طول بحران اخیر، احساس خوشحالی و احترام می‌کنیم.
توافق با ایران به مرحله دوم منتقل می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/15046" target="_blank">📅 13:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15045">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5d35b80d.mp4?token=DpHCu4yuLgyAzKctYX9UigHSkIIjPykLpO6PWY812NZyvT84CUXhRM3tcKqhfrVpHQsUAJd9JlZMhAHm-LWWRlV7fPinol5rkV-DLEJPQCVjlh6LYrEoUDqttTvJ52A1HVtkHNWvOUcXOQ9Kp41IzWTYMeO_qW_JnmllcTuokg-WWRjjBuE42786eNCpy7C43l_dAu-K-CzzfVFHaRcmmDgBIkyYlWK_OAZtpzdPy-vIn7lMF4uo9UWg_Zy52YJBntSzoKI3ItZgXH1cKiDexmM9zFOW_IXFDgoC9Q_uzFvcvhE5C2YZ5ww8S-8WqJuyNzDS-yg7EJpjIeAmUAECeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5d35b80d.mp4?token=DpHCu4yuLgyAzKctYX9UigHSkIIjPykLpO6PWY812NZyvT84CUXhRM3tcKqhfrVpHQsUAJd9JlZMhAHm-LWWRlV7fPinol5rkV-DLEJPQCVjlh6LYrEoUDqttTvJ52A1HVtkHNWvOUcXOQ9Kp41IzWTYMeO_qW_JnmllcTuokg-WWRjjBuE42786eNCpy7C43l_dAu-K-CzzfVFHaRcmmDgBIkyYlWK_OAZtpzdPy-vIn7lMF4uo9UWg_Zy52YJBntSzoKI3ItZgXH1cKiDexmM9zFOW_IXFDgoC9Q_uzFvcvhE5C2YZ5ww8S-8WqJuyNzDS-yg7EJpjIeAmUAECeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ما هیچ پولی در ایران سرمایه‌گذاری نمی‌کنیم، راستی. دیروز شایعه‌ای پخش شد. مضحک بود.
ما حق داریم روزی وارد شویم و اگر من بخواهم کاری انجام دهم یا کسی بخواهد کاری انجام دهد، اما ما هیچ پولی سرمایه‌گذاری نمی‌کنیم.
ما هیچ تعهدی برای سرمایه‌گذاری پول در ایران نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/15045" target="_blank">📅 13:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15044">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: ما هیچ پولی در ایران سرمایه‌گذاری نخواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/15044" target="_blank">📅 13:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15043">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، سه‌شنبه 26 خرداد از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی، دو زندانی سیاسی بازداشت‌شده در اعتراضات دی‌ماه در استان سمنان خبر داد. میزان اتهام آن‌ها را «افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد در شهرستان شاهرود» اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/15043" target="_blank">📅 13:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15042">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ویس میلیارد دلاری ۲
💰
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/15042" target="_blank">📅 13:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15041">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ویس میلیارد دلاری
💰
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/15041" target="_blank">📅 12:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15040">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/15040" target="_blank">📅 12:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15039">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15039" target="_blank">📅 12:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15038">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlkWalTw5C4hRSQHyJVMIcnA36t4Ie6AF18OLDwS_YKyhQMF_8rhzZjBawWkeoc4hf_Yf9fgAnRTyVfDi5B54f2CC1zna6XWW3tQlZhiZXWpgpUQwWduw2bGUkwl988f3XtCPkY2krwdLPUbkO6VW-J_U2cD_oedm46ApI9FyI41PsJ7HHxvr_K6gNZg2tBjfLQG4XwVLd1aJPh6NGKtksDFz90W3L3xKBFAyzRMTw7ZdfIRixENtrRYS-xk41dlqxRegBj3iaKM2wamwsX0iVtzb1uEj5NAWvKUC_Mm7nYaEiMb0VkQbhq5bZixSYt6ef0vby0WhixUMbKaPsvD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی پیش اهواز چیزی نیست کباب‌میزنند
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15038" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15037">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/15037" target="_blank">📅 12:26 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
