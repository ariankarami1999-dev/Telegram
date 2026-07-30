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
<img src="https://cdn4.telesco.pe/file/hkrjOUuyViZ1jjCuqIc5TQOzPN2GPYLfNrJcxx3WrsjQ6BUhD-liLfk7oKMaTa7UT4PFsaTSDkP1VwKdpuJeZUXITLCuOy6OUskod1Aj8PxSJZbXhQDxi8AzkM4b6CCvop4PhEmAoMaX6RG-usuhJFJHzTr2VO8eU3SYr794TUtkLLr75ub0se212NSQkwsBmU5UBljNcRDXs3OcAp3khcL_gII6deVcw1vaK69EmXV9kBucpevIIm2nJQbZxJndjdo1kIKc8uN8obIQV1vf4dfMnlo4q39LeXGZ2I44xv7DEtIxHj_GbG92M6b23t19xyouISdl7NlZQFLDKElZJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 15:21:00</div>
<hr>

<div class="tg-post" id="msg-676665">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bec21e8e4.mp4?token=AgVK4NGUJZhz46doIJvrpWBp0-qhZo7Fw42a4BUztyymQIbTvSA70CNmMkAzKLLLWM4VQqFxWD3W9qi7AonhfZG9QhIwZqeyfCFzRx3Q0FuydqtC8yHXs3MxUepxlIX6T1enLkWZRjUX15BRsXbwOiWJBfVOUXdyUplbx8AUKQcQefIX2LfL7fnyg9LLcXtSa9AuVKthWuZI7VGDLI7smIyb30bvqxEvqi85y0lXlZlhwoeVXVkBRhkDFbhswgZA791AAt9_D0y_3kntRXXqKkCcbvNDCkyyz7STpU-uWEnokvEcWWC2p-vsQMEBARw-hX5u573dyOZeEyKWCh00-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bec21e8e4.mp4?token=AgVK4NGUJZhz46doIJvrpWBp0-qhZo7Fw42a4BUztyymQIbTvSA70CNmMkAzKLLLWM4VQqFxWD3W9qi7AonhfZG9QhIwZqeyfCFzRx3Q0FuydqtC8yHXs3MxUepxlIX6T1enLkWZRjUX15BRsXbwOiWJBfVOUXdyUplbx8AUKQcQefIX2LfL7fnyg9LLcXtSa9AuVKthWuZI7VGDLI7smIyb30bvqxEvqi85y0lXlZlhwoeVXVkBRhkDFbhswgZA791AAt9_D0y_3kntRXXqKkCcbvNDCkyyz7STpU-uWEnokvEcWWC2p-vsQMEBARw-hX5u573dyOZeEyKWCh00-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش تروریستی اسرائیل: تعدادی از نیروهای یک گردان رزمی بدون مجوز فرماندهان، پایگاه خود را ترک کرده‌اند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/akhbarefori/676665" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676663">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انتخابات شوراها در پاییز برگزار می‌شود
کامران پولادی، عضو کمیسیون شوراها و امور داخلی مجلس در
#گفتگو
با خبرفوری:
🔹
انتخابات شوراهای اسلامی شهر و روستا ان‌شاءالله در فصل پاییز برگزار خواهد شد و رایزنی‌های اولیه برای تعیین تاریخ دقیق انجام شده است.
🔹
انتخابات تناسبی شوراها نیز ابتدا در تهران به‌عنوان پایلوت اجرا می‌شود تا احزاب و گروه‌های سیاسی فعال‌تر شده و حضور مستمر در عرصه مدیریت شهری داشته باشند و زمینه‌ساز انتخاب شهردارانی توانمند و کاربلد شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/676663" target="_blank">📅 15:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676662">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
اولین واکنش الحشدالشعبی به حملات هوایی آمریکا و عربستان سعودی  الحشدالشعبی در بیانیه رسمی اعلام کرد:
🔹
صبح امروز چند پایگاه رسمی سازمان الحشد الشعبی در نقاط مختلف عراق، هدف حملات تروریستی نیروهای آمریکایی و عربستانی قرار گرفت. بر اساس اطلاعات اولیه، این…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/676662" target="_blank">📅 15:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676661">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07805a2c36.mp4?token=j_sgUA0AJH7qXQxY-DC6lKYzGPAx7d1YUBmyKY_Gk2EQOaNYcLUqzeFe_i8ZnTDQXZvBbsjTLsDfeeEKmdzhAnZEhtmayBZ3gwrujwhrfSN5T2vG03bxmqvb0DGhU52XyTy3Zzh8xsW1U5s1FQ10NJszgUBaubrgzTNned_RjOfgoN-oQBbXyZ-UPFTEF5Z2kNqw2rFlIgbYWl0bYbjFRaEFwGkVxh5WMPcMunnRxmK-YKG1xBSMlM3ZfeC3oyXBIzrcCoUfe43U9zi0OuqmF0mC8EUZrHHFMkVPUsbBMAjDXkDXf_FsPy8xvA6I_L3U2cagE0RptjYsJHnmGno0bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07805a2c36.mp4?token=j_sgUA0AJH7qXQxY-DC6lKYzGPAx7d1YUBmyKY_Gk2EQOaNYcLUqzeFe_i8ZnTDQXZvBbsjTLsDfeeEKmdzhAnZEhtmayBZ3gwrujwhrfSN5T2vG03bxmqvb0DGhU52XyTy3Zzh8xsW1U5s1FQ10NJszgUBaubrgzTNned_RjOfgoN-oQBbXyZ-UPFTEF5Z2kNqw2rFlIgbYWl0bYbjFRaEFwGkVxh5WMPcMunnRxmK-YKG1xBSMlM3ZfeC3oyXBIzrcCoUfe43U9zi0OuqmF0mC8EUZrHHFMkVPUsbBMAjDXkDXf_FsPy8xvA6I_L3U2cagE0RptjYsJHnmGno0bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندی برنهام به عنوان نخست‌وزیر بریتانیا منصوب شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/676661" target="_blank">📅 15:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676660">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تیزر قسمت شانزدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید حجت امیر واقفی که در طی  عملیات جنگ با داعش در سوریه، مجروح شده و بعد از انتقال به بیمارستان، روح ایشان توسط همراهی چند نفر به آسمان عروج کرده و تلاش چند باره روح برای اثبات زنده بودن به نزدیکان، بی‌نتیجه می‌ماند و همچنین ایشان شاهد صحرای عظیم مملو از جمعیتی منتظر در جلوی یک میز برای حسابرسی شده و با اشاره یک هیبت نورانی ایشان بدون حسابرسی وارد دریچه‌ای به سمت زیبایی‌هایی وصف‌ناپذیر می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید حجت امیرواقفی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/676660" target="_blank">📅 15:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676659">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
نخستین کشتی حامل گاز قطر از تنگه هرمز عبور کرد
🔹
داده‌های کپلر و LSEG نشان می‌دهد یک نفتکش حامل گاز طبیعی مایع متعلق به «قطر انرژی» شب گذشته از تنگه هرمز خارج شده است؛ این نخستین عبور ثبت‌شده از این آبراه از ۱۱ ژوئیه تاکنون است./ ایسنا
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/676659" target="_blank">📅 14:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676658">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5wH0kvNf7cywgKXMFshPe2kzIBwpPRL8PpvG4gSVUK43O3xJRFlTieXxBGKOU9n7BqSAi2mvPIULMAT323mg6lWH6_RE4NRa5Ykv9-lbL2UuObDKQuRZ7XX839zvBKKSMMPW6o-Wdk4Un876rshFiFvvpR6cREeG7P3HZUfGD_wl-M3Owlso3PJYVza4XI9xHdAqLiZFyapd2havgkZHbT22PRvUWV9d4OHWYAFzAe4uLqMlXkRZx9c1MtSHeol7yL3tHduB-YPgzb9A96xxAZqDBLGUfEXR1kWKY4IkeFd1TcNH5UkKro5LnmIg2Y4Ri143rPBJxIIvLUWU474Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر روز ناسا؛ حلقه بارنارد بالای دو آتشفشان دوقلو
🔹
گونزالو لاسرنا وارگاس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676658" target="_blank">📅 14:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676656">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJBLkNtxGZToxHRAp8ol6cgAtj64yVna2NzAcfPq5o4Pi49WxYgpo21UN0Zyou6DPPan8XsgbZp_Lz1FmW6RgxpwztHeww0NJTYWJDV-TJfxN0Pq49YVW1pKYf5juvzyYDBqMDj--UzJeauZVACCF30ZHDiZh4EJh4ELvmYoQOdBTBBALrfoJtqZbA2ZpN4um0oJYbbXqXWAThbIje75BFngtIXUB8xjN_nANW82n9wIneXRdynYGZ6_Vh3vRoPMQFH5EthGG7kpN006ceE4Hst3hMY8uaXObrkBPRev7HEuel7xCN2bqs2lI43vO0DNS-g7MdMrEeigZrUUopBqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHxOK1yhVrbo_9usjekfDaMoJeutPFyPpfEHUUYjNU5mz29StAQhvV3Nuo4D39X3d5ObVBzibnGvN77vK06WgFyPiXlNYGBDFqZwpQvYlMLyNqafqM8LHGafpELuQjDwWx8ixumVmaQulCmE49DFvYNG-UfJI0oieNvftC_NYofkL5g-BAFnQ6EdrWcau6Q8H8mYjKrdpf-NdIbyAUCyQgrnc-reg5l-Cr9XX-gydOxsPWwedSRdPs-EPXC0ZvWFNYK7gsnGS-X2eL9QbqZdqaUwodyZMAEWJsLjh64qbLeqjBTwSGzBFx-M_i8Yt_8yvjODA04AWD3pDmoDuZH30g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وزیر ارتباطات با حضور در موکب «فدا» در عمود ۸۰۹ مسیر نجف به کربلا، از خدمات داوطلبانه فعالان اقتصاد دیجیتال به زائران اربعین بازدید و از تلاش‌های آنان تقدیر کرد
🔹
در این بازدید، رضا الفت‌نسب از طراحی سامانه مدیریت زائران گمشده اربعین با همکاری اپراتورهای تلفن همراه خبر داد؛ سامانه‌ای که در صورت تأیید وزارت ارتباطات، به شناسایی و بازگرداندن سریع‌تر زائران گمشده کمک خواهد کرد.
🔹
موکب «فدا» که برای سومین سال متوالی با مشارکت داوطلبانه فعالان اکوسیستم اقتصاد دیجیتال کشور برپا شده، علاوه بر ارائه خدمات رفاهی و ارتباطی به زائران، امسال با استفاده از ظرفیت فناوری تلاش کرده خدماتی فراتر از فضای موکب ارائه دهد و نقش مؤثرتری در تسهیل سفر زائران اربعین ایفا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676656" target="_blank">📅 14:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676655">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
درخواست گسترده در اردن برای خروج نظامیان آمریکایی
نیویورک تایمز:
🔹
صدها شخصیت سیاسی، حقوقی و مدنی در اردن با امضای طوماری خواستار خروج نیروهای آمریکایی از این کشور شده و حضور آن‌ها را عاملی برای کشیده شدن اردن به جنگ دانسته‌اند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/676655" target="_blank">📅 14:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676654">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
انهدام پهپاد متخاصم در آسمان بندر امام خمینی(ره)
سپاه بندر امام خمینی(ره):
🔹
در ساعات اولیه بامداد امروز یک فروند پهپاد متخاصم در آسمان شهر بندر امام خمینی(ره) رهگیری و منهدم شد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/676654" target="_blank">📅 14:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676652">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtrw0sVyYaix2deDIj0RrqcMHZRrV3LF_tILZ-IFQ7O8c6YM4NOwWF-HFEQcNjQr4TWAKEfXOssentkhki0NeB2xio3slxNIpsoRW53Esfl5SDiLhIIfmlYOh9_vzpSOu3KkC6CSggAyBtSNsqCjLqVK9ml8yNMtnY5FtqUtyrBfNKo3DCQ1NShA0sEt78q9jYrd7rwMm4O4f5fmG78s-55RaUf4PPGcocbv-VpNTGGmdldUzKLQYHZq0FciP1D7-TDCtFl-y5px-JRS0A3sXdHGFwDe6xApi_f1qhJ5SGgT7vdS7QOwpSB3TH6LnrEzWgAaJesVNO1yYP4AIATTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311ed5f16b.mp4?token=LCtz-Y29QpY-Y31CDIZvlgCiaHs8G9Xu6Pck36eCEJvgx8Wl2labdmcDchPDb5TPyrkc7oOuXGRgFPAXoqF6k34DmM5-F9kSw96vm3VWwncQtfFPjLEP0ibiPCDUbsrFh-e6XY4N9HFl6ANCWmpJnfNSzeyvvItdRN78Kb2LEgr1QICPGOlOdWNDm6nNsW5ZAGpx7Pm-zZKq_IcYS4rbGyfHblN0T72yqpTeEldGfv6nEF8WJjsjWI1PFfR2TZIqRo_OaycZa0_ZBKRN68C8t_jS5ZNT6TiCJuh_FJePxHlOHEyfTUMbJUeteEhuswcEigpV3riCCRis4POYmUDeULkXypD1zDUS-O7ZqOw8guRxOlrGndjDWmJ16RyWXnuZeknnW_RtyFBNUSLDvSdzqB2UOLZ-fU94VUxZ466y4q0U0Ios4tBazEcGC_Gy0zEAgl6ttDqWhNRX_UnEKrvPuxK7RHBUATh7O3xTG4UigTacs95PoFTCiOKLju02pkog0l5aFTH5yCTh_apIkYuCVo0LOxC5NCANvIhVmyo71DRKWuUg37aaK9-Kn6IRF2sfUtDglXo2_30B1QmTDauH9DcZL-GNnvSo9GD4IwsOI6kS94Yf8lgwKfdt7EDMfEr0XMZuKkjV4nt0gRcuqybnXgxffsekIBYlHbETq67sQEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311ed5f16b.mp4?token=LCtz-Y29QpY-Y31CDIZvlgCiaHs8G9Xu6Pck36eCEJvgx8Wl2labdmcDchPDb5TPyrkc7oOuXGRgFPAXoqF6k34DmM5-F9kSw96vm3VWwncQtfFPjLEP0ibiPCDUbsrFh-e6XY4N9HFl6ANCWmpJnfNSzeyvvItdRN78Kb2LEgr1QICPGOlOdWNDm6nNsW5ZAGpx7Pm-zZKq_IcYS4rbGyfHblN0T72yqpTeEldGfv6nEF8WJjsjWI1PFfR2TZIqRo_OaycZa0_ZBKRN68C8t_jS5ZNT6TiCJuh_FJePxHlOHEyfTUMbJUeteEhuswcEigpV3riCCRis4POYmUDeULkXypD1zDUS-O7ZqOw8guRxOlrGndjDWmJ16RyWXnuZeknnW_RtyFBNUSLDvSdzqB2UOLZ-fU94VUxZ466y4q0U0Ios4tBazEcGC_Gy0zEAgl6ttDqWhNRX_UnEKrvPuxK7RHBUATh7O3xTG4UigTacs95PoFTCiOKLju02pkog0l5aFTH5yCTh_apIkYuCVo0LOxC5NCANvIhVmyo71DRKWuUg37aaK9-Kn6IRF2sfUtDglXo2_30B1QmTDauH9DcZL-GNnvSo9GD4IwsOI6kS94Yf8lgwKfdt7EDMfEr0XMZuKkjV4nt0gRcuqybnXgxffsekIBYlHbETq67sQEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران شبانه غزه؛ زید ۱.۵ ساله در خواب سوخت
🔹
اسرائیل شب گذشته مرکز و جنوب نوار غزه را بمباران کرد و شماری از کودکان کشته شدند.
🔹
یکی از قربانیان «زید محمد نوفل» کودک یک‌ونیم‌ساله بود؛ مادری که پیش‌تر سه فرزند دیگرش را نیز از دست داده بود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/676652" target="_blank">📅 14:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676651">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
استاندار خوزستان: در حمله شب گذشته دشمن آمریکایی به شهر اهواز دو مجموعه خوابگاهی دانشجویی آسیب دیدند
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/676651" target="_blank">📅 14:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676650">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/461cbd54f2.mp4?token=Tsbb22GI91Ba1Buvv7kla4zUPvQKqBDdyJI6dEYl0XDLMa8oM4iWBO3aWPqXe06QMXhsB-5UE89TBAz0wxLMSla0D_UxP2l1WuFUVUh1IhXsswv8WtSNIb38qR0PfVRUYPHJYVYnhtXnBHXXgcNFT6YOOYe-AX_3QcUfpFEUOSWCU6Xe0aoLkVxr8yjailMV5b3KTvr5r-xhAe0L-0Q0_VI6vqptbcjbdd_OwEuTiYfQ865qtrwmfRBpgOYaQJrgE84CRrdSKB8zzkROwy2fgYnUYEc_VL_QFBkP6tmcSfwK0tP69B2BhMRqpOBveKs3PBlUWIeGPisagou7hKm7xlp_LHwijUC5Si1pwontzfKSKMEx2dQSJTyz7LqHoo2H6f2qbtZgCj2c9yYnnkrO-yMiF7dawFwrML3U9SrvfpKyV_8LP6dO20byky74PQ9ytfwDtK76vgb5uVfr9jeQVdFa6ULljQ0qQ3L4LQgayAntNTeuHiQDV9nBLwVPlxzKMW4P78rFERm9mVfiDxvMJz6jN_39glsxDEOiC_i0sBwxM9fr-3-LEYsd2VkHOQmDFCmo3vhIJC8sXnG8uvp7oy5WMWS8SNjC3-pt2lj5cQhwci0jUoeJsEIgc5st7YByhB-gYlSEHMdOLkiMSECKCsgosP-sNHXn7qBsnTXfssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/461cbd54f2.mp4?token=Tsbb22GI91Ba1Buvv7kla4zUPvQKqBDdyJI6dEYl0XDLMa8oM4iWBO3aWPqXe06QMXhsB-5UE89TBAz0wxLMSla0D_UxP2l1WuFUVUh1IhXsswv8WtSNIb38qR0PfVRUYPHJYVYnhtXnBHXXgcNFT6YOOYe-AX_3QcUfpFEUOSWCU6Xe0aoLkVxr8yjailMV5b3KTvr5r-xhAe0L-0Q0_VI6vqptbcjbdd_OwEuTiYfQ865qtrwmfRBpgOYaQJrgE84CRrdSKB8zzkROwy2fgYnUYEc_VL_QFBkP6tmcSfwK0tP69B2BhMRqpOBveKs3PBlUWIeGPisagou7hKm7xlp_LHwijUC5Si1pwontzfKSKMEx2dQSJTyz7LqHoo2H6f2qbtZgCj2c9yYnnkrO-yMiF7dawFwrML3U9SrvfpKyV_8LP6dO20byky74PQ9ytfwDtK76vgb5uVfr9jeQVdFa6ULljQ0qQ3L4LQgayAntNTeuHiQDV9nBLwVPlxzKMW4P78rFERm9mVfiDxvMJz6jN_39glsxDEOiC_i0sBwxM9fr-3-LEYsd2VkHOQmDFCmo3vhIJC8sXnG8uvp7oy5WMWS8SNjC3-pt2lj5cQhwci0jUoeJsEIgc5st7YByhB-gYlSEHMdOLkiMSECKCsgosP-sNHXn7qBsnTXfssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپاه: تخریب کامل سه فروند هواپیمای اف ۳۵ و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم  روابط عمومی سپاه پاسداران:
🔹
مردم شریف و فهیم اردن؛ همراهی و همکاری صمیمانه شما، به ویژه مواضع صریح گروه هایی از نخبگان اردن عرصه…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/676650" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676649">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bac1495d1.mp4?token=JE4ZDlgC3A4ja8SCLSJLnqbU1xOCY6Uw1fLtcr2adXJBnL3jkbEDW-lHMk-pvTwOKbYIh74ZHbnB_QgwmEwvawdESm6VVW223aB4VZyoqrXt6HrqcTBjytd0JdIfoL1fRRGholQCKPRaMUMXX9X6Qh-B-xDmviubkui6GuO4pm-nA9ljBIwKb-Mq3mmKSwD1EqqjPbqU3Zj7sNOAzOnF4C4hvlXtYHIrlnCTQGzQ1LS_P-FXKc86UroMCivj7fS971rzmOhs-hlr5EgcW_F7cNeLWc3E4X2uW8CrUCqABnsBktI7S63dHyznclcRfBlA6jTUDxq0pb8Hjh0Lc10iig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bac1495d1.mp4?token=JE4ZDlgC3A4ja8SCLSJLnqbU1xOCY6Uw1fLtcr2adXJBnL3jkbEDW-lHMk-pvTwOKbYIh74ZHbnB_QgwmEwvawdESm6VVW223aB4VZyoqrXt6HrqcTBjytd0JdIfoL1fRRGholQCKPRaMUMXX9X6Qh-B-xDmviubkui6GuO4pm-nA9ljBIwKb-Mq3mmKSwD1EqqjPbqU3Zj7sNOAzOnF4C4hvlXtYHIrlnCTQGzQ1LS_P-FXKc86UroMCivj7fS971rzmOhs-hlr5EgcW_F7cNeLWc3E4X2uW8CrUCqABnsBktI7S63dHyznclcRfBlA6jTUDxq0pb8Hjh0Lc10iig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب ماهواره شناسایی ارتش آمریکا با موشک اسپیس‌ایکس
🔹
موشک فالکون ۹ در قالب مأموریت محرمانه
NROL-95
از کیپ کاناورال به فضا پرتاب شد؛ این چهارمین پرتاب اسپیس‌ایکس برای نهادهای اطلاعاتی آمریکا در سال ۲۰۲۶ است. جزئیات مربوط به ماهواره‌های این مأموریت منتشر نشده است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/676649" target="_blank">📅 14:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676648">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOfzmEyANmw2bn-SGyAEnPo-2lYj24DA8_wRf7cpWFeKOV1xLpuyjx_JN9hTwsjyFi9ukNvqJ8a0QCdS9Bh4QvEbz5uUJEP3mmsy9yszcFj9yZ1o5puKRRiLAoIDV0fEJQsCLN1QacuQMuStqBy5g66xjCzr6B0k-K-vP1yIOKm2LJP7eWNq0ylPuGBdssgvuKxxrTeeJvLQIZd9PW9B3YlSzkUQi1xWc6RTZLm48bb_1hcoC8t6jZ-4pvs8OZbZfBQSc4mKTaU8Vdj3NxNl8HbbKMD7DFPhy7-ACWZKxQmjVBMZq_p-k7dw5cfBfUDO91VGexVwUP1jSctlQll4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کشتی ایرانی خط محاصرۀ آمریکا را شکست
🔹
کشتی کانتینری نورا از خط محاصره آمریکا گذشت و وارد آب‌های آزاد شد؛ این کشتی پیش‌تر در نزدیکی قشم دیده شده بود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/676648" target="_blank">📅 14:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676647">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
رسانه آمریکایی: سناریوی اسرائیل برای فروپاشی ایران ناکام ماند
رسانه آمریکایی «ام‌اس‌نَو»:
🔹
بنیامین نتانیاهو در سفر به واشنگتن بدون دستیابی به راهبردی روشن درباره ایران، کاخ سفید را ترک کرده و پیش‌بینی‌های تل‌آویو درباره تغییر حاکمیت در ایران شکست خورده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/676647" target="_blank">📅 14:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676646">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0R1VG8RtA80Wf1Am0NgpCwzfT8_PJvE4SsALGE4bdplWKQ6Sny69efiTgHgyevf2URPgTpofjSHJG6B-TbQef9QzubVKXK6QPrSnorL4nazzA1yh_f-dHQjFNcsB5RC0tIUDXi-r5wJ7Ymxia3KqT5Ln01hmS1a0CAQO06qTCBkuCzeIBs20JEcMQDFSEY8f39RC1wHyNkwRz0F5lWV2Wq17fzWpTTwhFKFnap-u83KdaDWMbvdIYkVmby4EN1EVfwLBEL4923D2uenhxHkE6yHbOG89EXazv6HHFtaUmY8v5czKnsbltssU358kSAbbUitwaqWmurw3kHeQd12bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این آموزش بفرست برای کسی که عاشق شال کشی و استایل کردنه
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/676646" target="_blank">📅 14:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676645">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beded2c25.mp4?token=u9p7onJ_GGmYCtas3ScUlw41DLwfryn8JbsraEMFN1cCNqtTR_C0lrMv3fUdZXOs6En3wYJ1sLN92Y8tlS3xIQF4v1hYZMp46SDsKkBLGB-7r2EixAYqHvqCKy-l10Mw6Sy0wt0BawAr1B5TYPKWZi8LDEUQAfG4Tqt1dvxPauKGriIb_XRdyTdwkOY7BT3S02JvctrqzdFSTvO6PXUZMzFZNuWEP5gfaVVHjs8xG3o51NQmdvBkdyifJG-YzolyoBVPqcDJdHjxiDWo7FLWAxg_u_B472xZD453xpWR8Jtg4LC8blOoGraSRbrYAFsbehSdIC4bca-_lJ3k20-AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beded2c25.mp4?token=u9p7onJ_GGmYCtas3ScUlw41DLwfryn8JbsraEMFN1cCNqtTR_C0lrMv3fUdZXOs6En3wYJ1sLN92Y8tlS3xIQF4v1hYZMp46SDsKkBLGB-7r2EixAYqHvqCKy-l10Mw6Sy0wt0BawAr1B5TYPKWZi8LDEUQAfG4Tqt1dvxPauKGriIb_XRdyTdwkOY7BT3S02JvctrqzdFSTvO6PXUZMzFZNuWEP5gfaVVHjs8xG3o51NQmdvBkdyifJG-YzolyoBVPqcDJdHjxiDWo7FLWAxg_u_B472xZD453xpWR8Jtg4LC8blOoGraSRbrYAFsbehSdIC4bca-_lJ3k20-AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زمین‌گیر شدن شرور سابقه‌دار عامل ضرب‌وشتم بانوان با شلیک پلیس تهران
🔹
پلیس اطلاعات تهران بزرگ در پی انتشار فیلم قدرت‌نمایی و ضرب‌وشتم بانوان در فضای مجازی، متهمی به نام «نوید» (متولد ۱۳۶۹) با ۱۰ فقره سابقه کیفری را شناسایی کرد.
🔹
این فرد بامداد پنجشنبه نهم…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/676645" target="_blank">📅 14:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676644">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ef75004d.mp4?token=uvY9mtwPWpmNQbRPyNnS8BVcsuZH3kNCcrJz5BJTJ7hkwT5ZEVicTg0rUEYP92DmiAzH9Qbu0AOExbcn-TY2--wtJOEaUb7sDO2nYxWxvT_HRytdLzqYTQH0FwREDDr90Dt-7HGzz1cFRQZiVqvL79LkewvbNruLX64l3nk0nERzTan2cc7-kVriOyBm1Lb2pGdWEK45WAmrrHUOqQePWxu-HEG97YGdWjWtgrrv_YScGWXIIsQvbjVhkvk95gPNcKlrW47NRmWjsrhlVDUBayCmS0ih2Hz282G1ZEhdPFbrssI11zZqvJ-oaRFSO9yDC1n4kytMantLLVhCtkyLfmABVxwAHvxrbXmp735tY-osTkNU0TAM57NOVUwmXiholFU9d4RP5iw_FA3GmVc5fyMi2NmXMqMSNvzYEFcrx2qwBZi4xj82pPCdr1J7JFdzUxOgPFwO-_e6-Epqh9V3_VWsvoHqC13x9WCcmLL13LMyQ4TlNrxNJvcV1V98O208VAZDMCuM7Cgws1o3nK3BGjkBln6XfV5pCJ2exYsM2kOhJyD1gzK7UfT52Eesd8yBIDLS5j3_Z4yMUG62oFO5mfFh2ob0Ye4f4XT0rcrNXVh26q2PezNc6VjedXlwEWvU7oBCA6bSAHYVglp1Y2c6GKd1dfhNkwHhtZRMCsnDwPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ef75004d.mp4?token=uvY9mtwPWpmNQbRPyNnS8BVcsuZH3kNCcrJz5BJTJ7hkwT5ZEVicTg0rUEYP92DmiAzH9Qbu0AOExbcn-TY2--wtJOEaUb7sDO2nYxWxvT_HRytdLzqYTQH0FwREDDr90Dt-7HGzz1cFRQZiVqvL79LkewvbNruLX64l3nk0nERzTan2cc7-kVriOyBm1Lb2pGdWEK45WAmrrHUOqQePWxu-HEG97YGdWjWtgrrv_YScGWXIIsQvbjVhkvk95gPNcKlrW47NRmWjsrhlVDUBayCmS0ih2Hz282G1ZEhdPFbrssI11zZqvJ-oaRFSO9yDC1n4kytMantLLVhCtkyLfmABVxwAHvxrbXmp735tY-osTkNU0TAM57NOVUwmXiholFU9d4RP5iw_FA3GmVc5fyMi2NmXMqMSNvzYEFcrx2qwBZi4xj82pPCdr1J7JFdzUxOgPFwO-_e6-Epqh9V3_VWsvoHqC13x9WCcmLL13LMyQ4TlNrxNJvcV1V98O208VAZDMCuM7Cgws1o3nK3BGjkBln6XfV5pCJ2exYsM2kOhJyD1gzK7UfT52Eesd8yBIDLS5j3_Z4yMUG62oFO5mfFh2ob0Ye4f4XT0rcrNXVh26q2PezNc6VjedXlwEWvU7oBCA6bSAHYVglp1Y2c6GKd1dfhNkwHhtZRMCsnDwPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس عربستانی: حشد‌الشعبی با زور در پارلمان عراق به قدرت رسید و سازمان دولتی شد
🔹
مجری عراقی خطاب به کارشناس: میشه تاریخ آخرین انتخابات عربستان رو بگید؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/676644" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676643">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سپاه: تخریب کامل سه فروند هواپیمای اف ۳۵ و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم
روابط عمومی سپاه پاسداران:
🔹
مردم شریف و فهیم اردن؛ همراهی و همکاری صمیمانه شما، به ویژه مواضع صریح گروه هایی از نخبگان اردن عرصه را بر دشمن تنگ و آنها را مستاصل کرده است.
🔹
سحرگاه امروز دشمن آمریکایی عاجزانه از رویارویی جوانمردانه نظامی با استفاده از پایگاه های اشغالی در کشور شما و حمله هوایی به دو خانه مسکونی با بمب های سنگر شکن خود، دو خانه ساده مردم محلی در جزیره قشم را هدف قرار داد که پدر، مادر و یک فرزند خانواده شهید و دو کودک دیگر مجروح شدند.
🔹
در پاسخ به این جنایت و کمک به شما برای رهایی سرزمین اسلامی اردن از نکبت اشغالگران آمریکایی، صبح امروز رزمندگان نیروی هوافضای سپاه با حمله به رمپ استقرار و سوله تعمیراتی جنگنده های اف 35 دشمن امریکایی در پایگاه هوایی الازرق با چندین فروند موشک بالستیک، سه فروند هواپیمای اف 35 را به کلی تخریب و به سه فروند دیگر خسارت سنگینی وارد کردند.
🔹
در این حمله همچنین چند افسر و کادر فنی و تعمیراتی دشمن نیز به هلاکت رسیدند.
🔹
منطقه ما جای ارتش کودک‌کش که اینگونه با قساوت خانواده های بی گناه را نیمه شب در خواب به خاک و خون می کشد، نیست. مبارزه ما و شما تا اخراج آخرین اشغالگر آمریکایی از سرزمین های اسلامی ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/676643" target="_blank">📅 14:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676642">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
گزارش های اولیه از پرتاب موشک از ایران‌‌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/676642" target="_blank">📅 14:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676641">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نخستین کشتی حامل گاز قطر از تنگه هرمز عبور کرد
🔹
داده‌های کپلر و LSEG نشان می‌دهد یک نفتکش حامل گاز طبیعی مایع متعلق به «قطر انرژی» شب گذشته از تنگه هرمز خارج شده است؛ این نخستین عبور ثبت‌شده از این آبراه از ۱۱ ژوئیه تاکنون است./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/676641" target="_blank">📅 14:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676640">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8-wbkA5hELDRmrIsNGyEdpIZ6_5btk6F6YEe5RlR5gREnNKJqe493sUpVjeSRwK_GAujyn3tfdBBC7lJKpx528lcKHsMrYlufChkWtZEIvRvc_u6beMgJTUwXW96F_GpB_UryHBddd60acyZAtQs3PEKzoWW0dA3KGMXo__dBQkRrjLOle48db0HZm3PbgaTgOcz9AXheWs7V-NohtEQKMvC52Dl13BnY5N7cL23SRzSDZx9m00f7jasH6ORgYafZeRiXJ0kb0JAY5CbNafghoPCAcN0AduhNmeDfUjCbaeVNJORJUGGS9oUsrs5_Iwe3fsnLqKoXoB0sRnIJVLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خرید قسطی طلا تا ۴۰۰ میلیون از ملّی‌گلد
فوری، بدون نیاز به چک، ضامن و اعتبارسنجی
با سرویس خرید قسطی ملّی‌گلد،
می‌تونی طلای مورد نظرت رو همین امروز با
نرخ لحظه‌ای
بخری و هزینه‌ش رو در بازه‌های ۱۲ یا ۱۸ ماهه پرداخت کنی.
✅
بدون چک و ضامن
✅
بدون اعتبارسنجی
👇
برای مشاهده شرایط و شروع خرید قسطی، روی لینک کلیک کن
🔗
شروع خرید قسطی
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا و نقره</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/676640" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676639">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THWgOUZNWvm8USmloinGVtKYXp5E6mnkLHjwR5ibeagoegWd9iOBkISqE9YqpS9wEnX4hghe0uJtIJPb8vNTpdxJM75PbhCk2GUHekLLtujHO0Kua3SKsaVOgM9FMLBXosh63U_gPcS_MVnDjKgCvSmPLenfKMT7-6WaT3-zVmqZBG2H7qRp_qIsuYA4Jt7sZyB_Zillg3u8zGVWzTO3WJ6N6FUXNGQRojjErlmXuIPTartiJY_GTREKbpAkuUM1jsszuDOqVr4r6GqIYeuNjtyP0hTowkxcZJYubdMWfnsR4Uy6dOJ7XzCwmuheGqcQBTKAjIxJlf-l2ZzpaUUobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
شهرک صنعتی توس، میزبان 226امین شعبه بانک اقتصادنوین
«شهرک صنعتی توس» امروز میزبان هشتمین شعبه بانک اقتصادنوین در شهر مشهد مقدس و سرزمین امام هشتم بود؛ دویست و بیست و ششمین شعبه در سراسر کشور و نخستین شعبه بانک در شهرک‌های صنعتی.
🔻
اطلاعات بیشتر:
🔗
https://enbank.ir/s/mfa8Ji
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/676639" target="_blank">📅 13:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676638">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شهادت ۳ ‌پاسدار استان زنجان در حمله موشکی آمریکا
‌
روابط عمومی سپاه انصارالمهدی(عج) استان زنجان:
‌
🔹
در حمله وحشیانه رژیم تروریستی آمریکای جنایتکار در ۸ مرداد ۱۴۰۵، ۳ تن از پاسداران سرافراز و غیور  سپاه انصارالمهدی(عج)استان زنجان به نام‌های  محمود ملاجباری، محمدرضا چراغی، جمال امیری  در دفاع از مرز و بوم ایران ‌و مردم ‌به فیض شهادت نائل آمدند.
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/676638" target="_blank">📅 13:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676637">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حمله پهپادی به یک نفتکش در دریای خزر
اتحادیه خط لوله دریای خزر (CPC):
🔹
یک نفتکش در حال بارگیری نفت در یک ترمینال شناور متعلق به این اتحادیه هدف حمله پهپادی قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/676637" target="_blank">📅 13:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676636">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-myt9SpaqGhFc5vER9gLcaj-X9qmOFUPjygb1Lausnh2qE3RWmehY8BJYBfVR2w8cw3FBJHTu_W7RXcUC2nLb8n-LBlojDqTh4FgsIFHM04h1PoC5MfeH_SJrVMhgBJkVjD9-LMk-mpcOlVFeTYHKrixh2ORK5wAVcHgDM99O7IhnCn2ZxUI2EnDaPWOgfh-e547wGPHCbAgGkn5kU51Js-F7Yw_gnIERophLAunGhrMGtTwkp8c-MmcmxxsDiveGuOcZYupwRacZpMP4yUi-DuDVPGGhSEihhy8g0E6SPJA2ggSvGpRcFiAKVO0zlJ8nHynckXj-G7F3oOuTUhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: رژیم ترامپ در حال خاموش کردن صداهای باقی مانده از ایران است
سید محمد مرندی، کارشناس مسائل بین‌الملل:
🔹
رژیم درمانده ترامپ، ایلان ماسک و ایکس به سرعت در حال خاموش کردن تمام صداهای باقی مانده از ایران، مانند خبرگزاری تسنیم هستند.
🔹
خیلی دیر شده، جهان از خواب بیدار شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/676636" target="_blank">📅 13:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz1gAVbKdr1EGHC-ApYZeUE0wEX1sROUamdvj7jx3Ytl9CVdMiRZauIN3yxxRZUVRsGPZon1Fpo_wMgg2WIMf-bBbN-dPRvIsNPzryiciyH8mSkq-gkQZKOSjjMkAXZW_CSepmDROtWODSO3w-xBymeO5Hhe2GMUyw5s1Ip12l8sdMFQabwrR17iwM_y3lxTto6vh54RQ4vTVwct35MssatHvkZcgNkum0KGSqPG8FvgY7IBChgSQwwMKiXBWlU0nvXK_RVg-z8IkWjfo-Lkv_ClcJZ4Xy6Ui9ZJ0CJpjuqpR4wl6DA5Iki5udt3P-tqck0bNh66VM7gHtpPz1aQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از ‌حمله موشکی‌ آمریکا به منازل مسکونی در قشم
🔹
در پی حمله موشکی آمریکا ‌به منازل مسکونی در محله چاه‌تنگو شهر قشم ۳ عضو یک خانواده به شهادت رسیدند و ۲ فرزند دیگر این خانواده نیز مصدوم و برای ادامه روند درمان به مرکز درمانی منتقل شدند.  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/676635" target="_blank">📅 13:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676634">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iucTGjxtHPGljVRtfXty4RBVXKJjO41fYv_iRJ3mGIBIdqP3IjM6dZPoIEPzqgNqk0nO5d7oniOycPVxBt_czGlQKVrqTX6Dbyc7xZYExzrvf7PJ7VU8ga3SHZkVJ_-iA8xfoYggKcL-S7xi3cVlqE8oRzqVvI8Z5vRCSOj6ln6BlOImMYLb6ncKfGwaRlaHoX3MkWb67YFElEbRdD7PTYyBBtJV2trjfMnvZqZezwDdRDkqr4CBxktC3iTzpLTDTImGTKefczwNu_jORProZkFE-1Jm6i4KxZlG_GaolWBL2SBc35dWyUNntcDiKiQiwfCIKB5X2KH3acSMbfi43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۸ مرداد ماه
🔹
بازار طلای امروز نیز همچنان با کمی افزایش در سکه تمام بهار آزادی و و ربع سکه مواجه شد.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/676634" target="_blank">📅 13:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676633">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
پکن شایعات ارسال سلاح به ایران را بی‌اساس خواند
🔹
وزارت امور خارجه چین، گزارش‌های منتشرشده درباره ارسال تسلیحات به ایران را «نادرست و بی‌اساس» خواند و تأکید کرد که پکن همواره نقشی سازنده در کاهش تنش‌ها ایفا کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/676633" target="_blank">📅 13:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676631">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بازداشت راننده آمبولانس در اسرائیل به ظن جاسوسی
روزنامه «یدیعوت آحارونوت»:
🔹
یک راننده آمبولانس اسرائیلی به اتهام جاسوسی و انجام مأموریت‌های جمع‌آوری اطلاعات برای ایران دستگیر شد.
🔹
این فرد ۳۴ ساله از دسترسی خود به بیمارستان‌ها برای جمع‌آوری اطلاعات و عکاسی از مکان‌های حساس استفاده کرد.
🔹
گفته می‌شود که او از یک «چهره ارشد اسرائیلی» که در حال بازدید از یک مرکز درمانی شمال اسرائیل بود، عکس گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/676631" target="_blank">📅 13:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676629">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بغداد: هیچ مدرکی درباره انجام حملات به عربستان از خاک عراق وجود ندارد.
🔹
مقاومت عراق: گزینه‌های انتقام از متجاوزان آمریکایی-سعودی روی میز است.
🔹
با اعلام AFC؛ عربستان میزبان دورهای نهایی لیگ نخبگان آسیا برای ۳ دوره بعد خواهد بود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/676629" target="_blank">📅 13:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676628">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds5g0OhaBany9ntXKmvc-tRLRcCUGjoAWWehXPMHYKvOMZ-bWDZEYIg4Zp646MOQsjSgOejy9RfhbdMz1Asw-AItev01g1BKzYWAomXkzHPmCxEbe7oZJxG6Eg5O3-nI-b4-07RkW9-hObPDQdho11baNiGcnUb8XFlyrhpMyZMfPjoJhl18MhO-SQomz6qiDEzLxbpVWIQ3gaeWHeVpuMj6m-x14Mg6QaXwNEbFq4ugpMft-6hcOvF8LMDn80W2-mzCnsx4W8C-zotY9ba-cW4zraxVVw_5TseDAsZKunD2JBz6lNQRWdrpK-u1Fhrvo3RKmsaZKmIJ60_Yqyq1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای سلامت بدن خود این نقاط را روی پا فشار دهید
🦶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/676628" target="_blank">📅 13:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676627">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6af8976a.mp4?token=gzt5sLi9QTk8GM7uTroem77mvOw0_5j7qy7eVlVjg6BZeSly3jH7-tQFGIt8etjHM5m2dDUXVz9HJxITFXSPHbLqniRhIPX5pD8Jqg7sU_kmCJWUXLKqfY5ZWeuWfK-i3_IAEmvyEbOfizBh77mg_ewY43eR-54PfNF3erjsMXzqzgZc9n14vBR7Lp0kwyOFdil_SF8IC61sXb7r7Q-fhQvJYmbHOk1dAUOi_Pk8siAmYgkTcriUUupNATX6DSZRMzZZo0ybBKY_syhTkjZssdHi8WYFgzn-snHSqFP7oW1E11kB3DdhzhOid58p0Sb2TzcG3Gedo7Clxz96hB_CCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6af8976a.mp4?token=gzt5sLi9QTk8GM7uTroem77mvOw0_5j7qy7eVlVjg6BZeSly3jH7-tQFGIt8etjHM5m2dDUXVz9HJxITFXSPHbLqniRhIPX5pD8Jqg7sU_kmCJWUXLKqfY5ZWeuWfK-i3_IAEmvyEbOfizBh77mg_ewY43eR-54PfNF3erjsMXzqzgZc9n14vBR7Lp0kwyOFdil_SF8IC61sXb7r7Q-fhQvJYmbHOk1dAUOi_Pk8siAmYgkTcriUUupNATX6DSZRMzZZo0ybBKY_syhTkjZssdHi8WYFgzn-snHSqFP7oW1E11kB3DdhzhOid58p0Sb2TzcG3Gedo7Clxz96hB_CCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدیه پوتین به رهبری در سفر به تهران چه بود؟
/ تلویزیون اینترنتی مدار
🔹
قسمت اول گفتگوی متفاوت "پلاریس" را در لینک زیر ببنید
👇
https://youtu.be/RgUM8McWe-g
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/676627" target="_blank">📅 13:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676626">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b785ba8cdc.mp4?token=M_xEc6GkyNTry65Insg53wOb4_t_QIAYfy72rqPAclmTAflOJb6WVj7ysyVhnGH59nTae_eSCx6JxuIK6L4PvprSG_6FID4WSelF7o4JOj7-k1__IUE3BN2r3mRj3dsE2juUKBq3RdGvtuVygsHCIzqsoiyMSmszDZ6YHAWl1Ui9ShcY3LX9XFK_DICSlCyyjWcu2Jbgv_Ibp-6j0sb-_Y58yNaKGf2bitT4RpjnwvkzocjHC28QHNn_E5J7QAxrgpsWzyJTcMhS14xujOyvooPzAqEyxvWkryJJj8OfpKnn6qMHMoDl6Bpm5agAG9VA4W7XzdQOxpYX205EYqTWZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b785ba8cdc.mp4?token=M_xEc6GkyNTry65Insg53wOb4_t_QIAYfy72rqPAclmTAflOJb6WVj7ysyVhnGH59nTae_eSCx6JxuIK6L4PvprSG_6FID4WSelF7o4JOj7-k1__IUE3BN2r3mRj3dsE2juUKBq3RdGvtuVygsHCIzqsoiyMSmszDZ6YHAWl1Ui9ShcY3LX9XFK_DICSlCyyjWcu2Jbgv_Ibp-6j0sb-_Y58yNaKGf2bitT4RpjnwvkzocjHC28QHNn_E5J7QAxrgpsWzyJTcMhS14xujOyvooPzAqEyxvWkryJJj8OfpKnn6qMHMoDl6Bpm5agAG9VA4W7XzdQOxpYX205EYqTWZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت تلخ و دردناک نخبه و ریاضی‌دان ایرانی در آمریکا؛ پرداخت مالیات به کشوری که مردمم را بمباران می‌کند، بسیار ناراحت کننده است
🔹
شایان اویس، استاد دانشگاه و ریاضی‌دان برجسته ایرانی: برخی از دوستانم به‌خاطر پشتیبانی دولت آمریکا از جنگ مهاجرت کردند؛ من هم به این موضوع چندین بار فکر کرده‌ام!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/676626" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676625">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86381f1826.mp4?token=oKk6E37pwFxKGt9vOjzc9cFy8474zYa-0tC3d4lQdyXO7wtqQIzYQoLkThwoNSKAYnSRZ6K96ryICqR1v6ROQMqoN909__jHRjIzHiRxsokyKvIABGV5LJjn6IYEHVYDm4WPXEyAkkztDQsihOIIjcAt2XBYAWpqMq5p0TVdZEfA_aBoXEpJArgheCe-V0YFoDYaZ4AXG5BMliMv6XjvBgm9JIgANLfdZKqR58yZUkY9Gw1lI9OYax8YkDxsv2886-RdmG7FapJrolaUCtCOSdTs7J9edVXELMjgwfPoGwBlCee9dikrEl01hyi_Y2OLVLKgZg8ymMfRZa_787sOVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86381f1826.mp4?token=oKk6E37pwFxKGt9vOjzc9cFy8474zYa-0tC3d4lQdyXO7wtqQIzYQoLkThwoNSKAYnSRZ6K96ryICqR1v6ROQMqoN909__jHRjIzHiRxsokyKvIABGV5LJjn6IYEHVYDm4WPXEyAkkztDQsihOIIjcAt2XBYAWpqMq5p0TVdZEfA_aBoXEpJArgheCe-V0YFoDYaZ4AXG5BMliMv6XjvBgm9JIgANLfdZKqR58yZUkY9Gw1lI9OYax8YkDxsv2886-RdmG7FapJrolaUCtCOSdTs7J9edVXELMjgwfPoGwBlCee9dikrEl01hyi_Y2OLVLKgZg8ymMfRZa_787sOVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز زیبای منقار قاشقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/676625" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676624">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ef1a4574.mp4?token=j24B82P7osvz4JAGUoH7Bx6_8IPSL2wnB_WvGMX3vrg812PDOGZJkCCx3Zfh28Mb3tempfTM9E7d0Cio7BI4zUNbVHcN9ztww1Wfu2Xocd770o7CJ5S3gA2RE5H2jY6Iz5twpumihMiTDAEB8mHbQS0OWX-emFenNY7v76pgutkS3-qXFhmkScoLqC4OrU9O__71P_91tPl9Sr_R4DciG49YQ0KnswFXD46hCfWtSafxcsiLENMGLR6wFp_CE-7snUNLj9WhNfpc3oulLFNmT9zQBvVTt7qi2nO9J6ZW353NLcMF9ExRsTeeFybIgB1hSU3VeprjCpw2u8P---WqjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ef1a4574.mp4?token=j24B82P7osvz4JAGUoH7Bx6_8IPSL2wnB_WvGMX3vrg812PDOGZJkCCx3Zfh28Mb3tempfTM9E7d0Cio7BI4zUNbVHcN9ztww1Wfu2Xocd770o7CJ5S3gA2RE5H2jY6Iz5twpumihMiTDAEB8mHbQS0OWX-emFenNY7v76pgutkS3-qXFhmkScoLqC4OrU9O__71P_91tPl9Sr_R4DciG49YQ0KnswFXD46hCfWtSafxcsiLENMGLR6wFp_CE-7snUNLj9WhNfpc3oulLFNmT9zQBvVTt7qi2nO9J6ZW353NLcMF9ExRsTeeFybIgB1hSU3VeprjCpw2u8P---WqjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معادله عوض شد
دیگر صبر نمی‌کنیم تا به ما حمله کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/676624" target="_blank">📅 12:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676622">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG9oZG_W4in7P3zWL13gi_qnDNRshv1Ct28jQuFVu07kWRwbajLBZUHiIpiCj90wE_pZXXEzGOfuVl2ixpzA_jzj--6O_rSrBn4ns_iP0Xsdd-M56_QVkr2AQbcAg8XH41Nz6zW093XcsHdLmbJych2Su4wtMRCwdDbonZUjXoIcq3uGa6oG2MJJu-HhXiZJgUhQqFRfqbk7K_FkcXFuIdjrRvlX33rQg-_vVSgvzqPdv7cQTV6rpdLoXVIgmg4QmqwcIHdR-KvxrrN9sHcaUDUGpveCDcLe5bf2D10IwSrdxiuErfdC8-DWM5Prfot8DaawiYLZ39QKXdD4HYtDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gW99nm300oBq-A6cgRTJD5FIn-zUXWWi-viMCB0zHwz3wmlf_l3cymqbSofu2X56uVA4yxFyvIhEPcGnQ4QunOQavTwgokPX4UL9nudkqOndcxHc2-kKnm1IOTtr4uxCk7qfKwd8_jnJI7aGuRMklbD2z53RSoBv96c75A0wZSnaHJlk52fNRBaTD_-pzIO6Gh4nfwII8hq0gyZBjqiskapDm-NhFVlGrbvfSHGG7qxbw9Jt68u8n3EvAVEw7yh67RBWJ-JCh_gmKCk6S6ARI2eqFNjIxvf7wTXVF2lYHWO87kgJujrd5NU_oxAcCe5Dqyza0kjD5vYKvUELv-QVjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در ایران به ازای هر نفر حدود ۱.۷ سیم‌کارت فعال وجود دارد
🔸
ایران با ۱۷۴ اشتراک تلفن همراه به ازای هر ۱۰۰ نفر در رتبه ۱۲ جهان قرار دارد؛ یعنی به‌طور متوسط به ازای هر فرد حدود ۱.۷ سیم‌کارت فعال وجود دارد.
🔸
ایران از نظر تعداد اشتراک تلفن همراه، بالاتر از کشورهایی مانند چین، آلمان، سوئیس، فنلاند، بریتانیا، آمریکا، ترکیه، عراق، هند و افغانستان قرار گرفته است.
🔸
تعداد اشتراک‌های تلفن همراه در ایران طی دو دهه گذشته رشد چشمگیری داشته و از کمتر از یک میلیون اشتراک در سال ۱۳۷۹ به بیش از ۱۵۹ میلیون اشتراک در سال ۱۴۰۳ رسیده است.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/676622" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
نشست اضطراری وزیر دفاع عربستان با ترامپ و ونس در کاخ سفید
🔹
وزیر دفاع عربستان در کاخ سفید با رئیس جمهور آمریکا و معاون اودرباره تحولات منطقه به ویژه تنش فعلی با ایران گفتگو کرد.
🔹
گفته شده خالد در دیدار حامل پیامی از سوی محمد بن سلمان، ولی عهد عربستان بود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/676621" target="_blank">📅 12:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676619">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9b2bff6b.mp4?token=TBoSnqpIwDvJ96delQeVKYipjqBPOCaKqPXh-9svftiTtSoWpzJ9mIvRkvqmzqds-s1wurwIE5FWy71t2SeHv7VqTx_YCr1c3hWY5R7BTjWdqDnLrrJTq2h7MyMmKoQ87R1WaPLI-tVraUhdSBTd9YTU4HjlqlpK-8zdwxcZpAs4YrhLfbzXcmkvysTVwSTwlUeKBWDwCyLjXXQZh_KtbnNqR2uR1EnTCs6JAMdAvJHVfmcXHgrc2RdqJW8EHsZ7jTgltCgMjuOEQQa8O4kOi9OPjgFgGhC85ZODYH6LNJ0EC83g8QHkDcDr57C0L-ujcyz9FhPpKSwscGNFY6YVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9b2bff6b.mp4?token=TBoSnqpIwDvJ96delQeVKYipjqBPOCaKqPXh-9svftiTtSoWpzJ9mIvRkvqmzqds-s1wurwIE5FWy71t2SeHv7VqTx_YCr1c3hWY5R7BTjWdqDnLrrJTq2h7MyMmKoQ87R1WaPLI-tVraUhdSBTd9YTU4HjlqlpK-8zdwxcZpAs4YrhLfbzXcmkvysTVwSTwlUeKBWDwCyLjXXQZh_KtbnNqR2uR1EnTCs6JAMdAvJHVfmcXHgrc2RdqJW8EHsZ7jTgltCgMjuOEQQa8O4kOi9OPjgFgGhC85ZODYH6LNJ0EC83g8QHkDcDr57C0L-ujcyz9FhPpKSwscGNFY6YVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✂️
ریش‌تراش/ماشین اصلاح HAIR CLIPPER مدل GYT-999
تیغه استیل ضدزنگ
✅
| شارژی
🔋
| مناسب اصلاح صورت و بدن
🔸
نمایشگر LED (نمایش درصد شارژ)
📊
🔸
شارژ کامل: ۲ ساعت
⏱️
🔸
زمان استفاده: ۳ تا ۴ ساعت
🔥
🔸
شارژ با Type‑C + کابل شارژ
🔌
🔸
صفرزن و خط‌زن برای اصلاح دقیق
✨
🔸
همراه ۴ شانه اصلاح + روغن + برس نظافت
🧴
🧹
🔸
بدنه پلاستیک درجه یک
💪
🎨
ارسال رنگ رندوم می‌باشد.
💰
قیمت قبلی: 1,698,000 تومان
🔴
قیمت 1,398,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/676619" target="_blank">📅 12:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676618">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59db64932e.mp4?token=IM8XDSTInANPZtqa-wv3Ra3QJqAjiKczdbHMgd8Y3WSC48xykHK2ljOcMY05SwhP-au0BI0_Csb5ZGy8SIex-Nc7sSzMDdC0wKXatxiWmideqCo0gFADo9JdoWanaFIXf0gOMODTiuEMTLYAXyvc7-Oz_RupxoKhgY05bUubdS5X2-bs7Fadk-b1nM2IvHN4tQUL5hwSl93wPLbZoUz4g_lbbEmeGWzkIw2VW1qgQfivAPZhl_lbQKNCYnOA_6bk8i3NBHfmtcIAlRXkXwO6tnYNNlai9hpa3D3GAPBEKMWV5ZTjGtnoyiZa53l8UydpUPkX7X3TSpyfwhAL_exRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59db64932e.mp4?token=IM8XDSTInANPZtqa-wv3Ra3QJqAjiKczdbHMgd8Y3WSC48xykHK2ljOcMY05SwhP-au0BI0_Csb5ZGy8SIex-Nc7sSzMDdC0wKXatxiWmideqCo0gFADo9JdoWanaFIXf0gOMODTiuEMTLYAXyvc7-Oz_RupxoKhgY05bUubdS5X2-bs7Fadk-b1nM2IvHN4tQUL5hwSl93wPLbZoUz4g_lbbEmeGWzkIw2VW1qgQfivAPZhl_lbQKNCYnOA_6bk8i3NBHfmtcIAlRXkXwO6tnYNNlai9hpa3D3GAPBEKMWV5ZTjGtnoyiZa53l8UydpUPkX7X3TSpyfwhAL_exRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه آرامش‌بخش است دانستن این حقیقت که گاهی پشتِ گلایه‌ها و اصرار بر ترمیمِ رابطه، نه خشم، که عمیق‌ترین لایه‌های عشق و دلبستگی پنهان شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/676618" target="_blank">📅 12:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676617">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8fb1206a.mp4?token=Wc8TPKw0HuddZbsGgaWCc0HawsEsknjQls9FVtGRfrX8QfBu1LRD2Mtuuxj1cSoi-HjObgLcLNOxxyQWwTl35PL2Eb7Oz_bbTbvDYJiLna_LH4TynzgaDIdJfdAxqhBsH_Gcj22tO_ikPfFT_hyodReHVAu94ZgIzp2wFSFUpOjK6Vul9v5gTsZSXfyFVg0BAFsEANkWCECwTMhIBrJvqUWpL3OLJhWZ_Z2D8bezycWv1kv8CroiX86AOwnHaXRmnCbc8V8pNS6eXql6LHuKadUbvpOqPAwoz0n_eAZlqtTcPYv7E8n4_E-jng451tRAHnE7COzkbQdGzQmnHRvxzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8fb1206a.mp4?token=Wc8TPKw0HuddZbsGgaWCc0HawsEsknjQls9FVtGRfrX8QfBu1LRD2Mtuuxj1cSoi-HjObgLcLNOxxyQWwTl35PL2Eb7Oz_bbTbvDYJiLna_LH4TynzgaDIdJfdAxqhBsH_Gcj22tO_ikPfFT_hyodReHVAu94ZgIzp2wFSFUpOjK6Vul9v5gTsZSXfyFVg0BAFsEANkWCECwTMhIBrJvqUWpL3OLJhWZ_Z2D8bezycWv1kv8CroiX86AOwnHaXRmnCbc8V8pNS6eXql6LHuKadUbvpOqPAwoz0n_eAZlqtTcPYv7E8n4_E-jng451tRAHnE7COzkbQdGzQmnHRvxzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ‌حمله موشکی‌ آمریکا به منازل مسکونی در قشم
🔹
در پی حمله موشکی آمریکا ‌به منازل مسکونی در محله چاه‌تنگو شهر قشم ۳ عضو یک خانواده به شهادت رسیدند و ۲ فرزند دیگر این خانواده نیز مصدوم و برای ادامه روند درمان به مرکز درمانی منتقل شدند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/676617" target="_blank">📅 12:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8pZkopDVH6sEyT3fFt4KNpAhb6824y34qX-PSmmj3oukjEeN8MWrxhZ0LrB3Nkx-15sYSRO4pR_J74VAMLyZaF4l3zflThK1dMnAjR1DZAyRklZMm7ySRxwGh4EtaA51p7NnYGiTa1iJkXoFY0ATtb1R7prave6kIQjnLFCeDM2Ppnc5chbdYFgod68yHc1m1wuLjXUfYzATUWJG0aV5x9uPVHCbI626OAjOhoblvDQEkdcg1CYuvWB6rAGxhbF8CSx6RxXab-ZqJavG-CnuR_jo1XrJTR3HIw-cC_lZ90e8-YzuNfXQp9MaP6fsnSQ9M0nToAGscqzwvXg6BvT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلاگر متهم به ضرب‌وشتم زنان در لایو اینستاگرام، بامداد امروز در خیابان مطهری تهران دستگیر و روانه بازداشتگاه شد.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/676614" target="_blank">📅 12:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFbKHPqxqMU-3iaBkY7F-NnUvjrLd3EiGOO_swOO9PvSD4eYmMKOhy_NHnchhUkTeB7pA3ua-9xBBAf1iI0Hg5WizSOD6xSf8bNJjav22Fyeab3agwwBmQJ71qc4qYpfPaYeT0dypjmlaJ1ndWwrY8jC7Mu6XlDI1psXOcfawdHMwKZxfqRIiPmfiMJyVAItKjyydQsBHoMW7UERSzIdHxmz7Unj1Sdvvo8rvHOROCIQdr8r8rST8NFqjDyylGY8XutbgRokTB1mYJ5FlV97N4NZV80E6745xw3XJwsrfzrh1Lwm3X-sLnrbA7HTGfoQuEPU3J7mZjBhbkB30XbSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyL7m9YDeZLkNN9iPtmGIT1_bMxcUuv_xfcKJCQDaVvDHDg9vaA6A9_0DXNJeIZjLWL5KTXpojAsmlKoUr5jkP_xphzBnHukKYxWex58MvSgE7BWJFOblHslKY25skgzalE2O9P7z9yJJd8qiy8M2DLNnW6tdlZh8jIAbyddeMjrf8F4HW4Eq7bWFIIG-EsxzMkiRfzv9Z0LHae6aP0UU2rnEH0WJ5YIypOjJlr8_KppgqSdgTgF3XVj0pN6sG9EJJle2nl7EQ9FWdiJVW5qbLmlxy15ypRQiQizI5iGR102WFM7xSiaVYxm6i_XYUgcGCaJcogMsX86-mAB8CDEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpEBIhXYayzwPrDIB0-ta54tXDqSRNdgdNM0Uxa4JQRDdo0X0wPHkYmprtxk9b2sFo9_VCHqWn2HvZ_pXzdg5Mcddmj1Wr3UZN_Wr1E27aQ-XBl7TF_4dvl9qSl4GVe8oALY97B181E5nFVFQ2RWLivnxex4ZgDvlLbkqLLxkZxFVSw0yejn4ywILmCPOeQbLbJb5c9_EVFmT8kvF_AGuvZUXrQ2dyWh2lw-KEWOtTOl-8BXTDUQbngw7frRqwzNq0j12B0rt5CqX3BzRL70z0RlKdnYzIDi6CkvjulPeb_2hv2fbI3o9_eEVJvk1S65p9XFDcqa3ZMns31zyKvp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxJBYtoJl-LSfXlYJxafS6Obn3Th5mjUKQ44hnD2JyviU4sG1d0wV38CUEXgS3QrmzbNpPViPhpxmnkB9d_CirYbDpqKQsMYAh41305QGTOy-d-iX46_KxywlsVMjuWc0HGrVs6HH3MwfMQio1ywpLQmkLRCXCOAXBilMpZ-2f0wEkj-oRPuES_JkdA2tkMSYQM4TfIjs6H2QF5R1ZMZEymKTcq17SFAztLM3SiHhgECwIc7z108rUrWCOuQeYo9v6aqS92RpOY1Ogn2nRFwauumaNDdMwdm7M0Uk7Ll30T3YYoE9Xq454mLn-SFICme3n8NaqyY_CdsHp4dGvT33g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بعد از دیدن این ویدئو‌، دیگه خودتون رو با دیگران مقایسه نمی‌کنید #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/676610" target="_blank">📅 12:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693addf9fb.mp4?token=bB8GZ74rZL32Sm0fsvsEUCJihou1FUz_phPQHPAxk3dCS5WAvV7Nkgcy_mkb41zy2BJ34kIDi9HMjSNjVxeeDy_zs_GSR_L_-DGpUxsSfJ-bJcAfOjTSKMqReEve0o0V2fT8wQtmPlri6SnZZU8-nFD35VpwTy-I2YmaNBK40WtyJjn3FCOlTRJcyigAg0h6qGnqNIdvRFM9rgr3WaNTKBOh43WGtpywetStx_Eiwr9gvNuqtI_Zv0XPAxOTX5CkswSZk-RWDWO3LDAtB2maIU3hHT2uKz0GXW4_q7anIt0YlfD_wPl7dYLNu4ki7Sk2Z0RgHbG8FZnoFqajPqXSLJ_Jg3d6JhEZLIBEd7RSbv_RH9YZd9dYLQX56WFrDGDaE2-fLbau0FQ4JReEdl68gGnNvbWiw9gZzciej8Y_SZEWZtiywM_0W3GTLXdXxhYqZUQft_wSl00Vxux47l75ZiWapqrQWUnb_9mPrp9v9y_kUCmmzQY75jaPtQT67cQoHpr-0x5XNv4B7WgyM9GFM0ME1tp6oQKsIEYGPtT3tDiV21BlYqXp1h_oTtWpuVvhQBrXwbHBCBd7YOwMEwcwRIaYs_G05-FajO8vd_1-ZUh6MEjsNAWhhc6ndcw52Seis4MQVWSz6nU1OAfG_vw8zUu6oQM1xRzjG2IVZI4c4fc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693addf9fb.mp4?token=bB8GZ74rZL32Sm0fsvsEUCJihou1FUz_phPQHPAxk3dCS5WAvV7Nkgcy_mkb41zy2BJ34kIDi9HMjSNjVxeeDy_zs_GSR_L_-DGpUxsSfJ-bJcAfOjTSKMqReEve0o0V2fT8wQtmPlri6SnZZU8-nFD35VpwTy-I2YmaNBK40WtyJjn3FCOlTRJcyigAg0h6qGnqNIdvRFM9rgr3WaNTKBOh43WGtpywetStx_Eiwr9gvNuqtI_Zv0XPAxOTX5CkswSZk-RWDWO3LDAtB2maIU3hHT2uKz0GXW4_q7anIt0YlfD_wPl7dYLNu4ki7Sk2Z0RgHbG8FZnoFqajPqXSLJ_Jg3d6JhEZLIBEd7RSbv_RH9YZd9dYLQX56WFrDGDaE2-fLbau0FQ4JReEdl68gGnNvbWiw9gZzciej8Y_SZEWZtiywM_0W3GTLXdXxhYqZUQft_wSl00Vxux47l75ZiWapqrQWUnb_9mPrp9v9y_kUCmmzQY75jaPtQT67cQoHpr-0x5XNv4B7WgyM9GFM0ME1tp6oQKsIEYGPtT3tDiV21BlYqXp1h_oTtWpuVvhQBrXwbHBCBd7YOwMEwcwRIaYs_G05-FajO8vd_1-ZUh6MEjsNAWhhc6ndcw52Seis4MQVWSz6nU1OAfG_vw8zUu6oQM1xRzjG2IVZI4c4fc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی سنتکام ناخواسته مرگبار بودن حملات ایران به اردن و ضعف سیستم دفاعی آمريكا را تاييد كرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/676607" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676606">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLKVghMN4pdolkDTtymDZfTXUDsMs4MeZKRVLmuTCn3IDz-oIlbpk8o0esh5fdS1VNZnfRthJsXV-5ZOuNGBAoxF22koSbzGeu-LjpT4recIqLU1_XWKv8cF6l_inZ9C-cQsYOI4hua5ABtqSLsm-8O6X5V_VCrttDVZKOBEcizqFc6tYQdGqqVTncKV_oFhUPKB3VJkoxMGB92vTPIg0fn8g4cyCJ2ph32jmikSL0U9qAPqJyBsGKPFtBqBcn0pz9FXxe9RwjZ01PTd6ZAst1cHht8xCjTAoZxinnCzjktk1ggnJbENQWBGb40MwwZNup9qM5CDuo4fJ5mnFKMnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ درمان خانگی مورد تایید علم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/676606" target="_blank">📅 11:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676604">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a3bce682.mp4?token=Ws3I3D4tIoCJwZRCHMLRDi-GvShaGFJ_4tjGh7gWUOnpMPR-tg31uk0OmtAO6Y4u8e8PBnnm88VOQnMB3UGyQksR23eYLecfhmKrWllSrdqTND4cHZtcOXO5PPmlPVxHQBbRr-fPTOHCrroMzdWsjp5HjjShOmWZMZKb-vEOwSiYXXDIf-Ri--ZbTvnyMR5Arif5blenqMbA0tkMgNaSXi2C0jM7qKYEp-PH1ko12mvO0lqq8KKrCrPov7tyuIEJHcBuGqkTsGm28iKBjhT2PdcEYjhhdB8P-ZMGhTQbngaNOp5kbOS3W_NdgFZyRAC-dJRkAhS1push7egTMiYpMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a3bce682.mp4?token=Ws3I3D4tIoCJwZRCHMLRDi-GvShaGFJ_4tjGh7gWUOnpMPR-tg31uk0OmtAO6Y4u8e8PBnnm88VOQnMB3UGyQksR23eYLecfhmKrWllSrdqTND4cHZtcOXO5PPmlPVxHQBbRr-fPTOHCrroMzdWsjp5HjjShOmWZMZKb-vEOwSiYXXDIf-Ri--ZbTvnyMR5Arif5blenqMbA0tkMgNaSXi2C0jM7qKYEp-PH1ko12mvO0lqq8KKrCrPov7tyuIEJHcBuGqkTsGm28iKBjhT2PdcEYjhhdB8P-ZMGhTQbngaNOp5kbOS3W_NdgFZyRAC-dJRkAhS1push7egTMiYpMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یا حسین ما انچه در توان داشتیم گذاشتیم؛ هیچی چیز هم نمی‌خواهیم؛ فقط می‌خواهیم ما را به عنوان خادمین خود در اربعین قبول کنی
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/676604" target="_blank">📅 11:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676602">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3790cdfd.mp4?token=olVCULxvasTGsbcc4__DOY-ArBehqP9-8awHLMcpM6-v9Mv4TaxyGF3PT-SFbbmZg3dj3sKf5FfS-FA9-M6XLsUSLL2AhYtfXNHDl0QFlsnKXC7EMGqRjk2o2cfWLHRZuRuFRIbYWWyFLwzV3iwlxceIRbrUlOYvG9ai4NGuFGn4n643AJDcFqqRZDvyTSkqiH1MXQR3NlELd9m7BmC75gQeMkqcO18G_LbA6ipxjZlXa10vc-qDybOtdBmu-gcj27fOpclurIuycTGKmE55i36VyGrqSYvPqb_98PXQJx8pjTJtSKs30akKGsDanFFMeLkaaVbhREnGTxYtxL7tgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3790cdfd.mp4?token=olVCULxvasTGsbcc4__DOY-ArBehqP9-8awHLMcpM6-v9Mv4TaxyGF3PT-SFbbmZg3dj3sKf5FfS-FA9-M6XLsUSLL2AhYtfXNHDl0QFlsnKXC7EMGqRjk2o2cfWLHRZuRuFRIbYWWyFLwzV3iwlxceIRbrUlOYvG9ai4NGuFGn4n643AJDcFqqRZDvyTSkqiH1MXQR3NlELd9m7BmC75gQeMkqcO18G_LbA6ipxjZlXa10vc-qDybOtdBmu-gcj27fOpclurIuycTGKmE55i36VyGrqSYvPqb_98PXQJx8pjTJtSKs30akKGsDanFFMeLkaaVbhREnGTxYtxL7tgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ظرف سفالی، ماشین میوه‌شویی ۳۰۰۰ سال پیش در ایران باستان بود؛ بدون برق، بدون صدا، فقط با چرخش آب و قلق مهندسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/676602" target="_blank">📅 11:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676601">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b537f120d.mp4?token=kslR4CP1-DhFcXH4mJ6nMroLutxXz7ig9VbgOv1ngwjZ5yWNS7jd18VWBez3tF_4twlqMtlHZeWoRTSgdWnoTGWh2JN30KL44nAZXzU_lDtYzycnxv2PgxwRLZdYSucYFUWnHfozt2uTYLQ89ebcy_wTO9V5Yzmp39ssZfXSBUcgRQaBICptQOZQOrbhL3Tpxe2RuNqHMzASZfNB7uayF4rUSFvrhe-F1m2uWCn7IgOWYUTenKO_pqLTy86OUlA5CXcY2MDd1rh1CWR_8kWaplnK1enb2Mz9gtA7vx0gmYOB3EVgtjYgeCqNsftOyBrtk16gEquJdkRRtO341AC4rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b537f120d.mp4?token=kslR4CP1-DhFcXH4mJ6nMroLutxXz7ig9VbgOv1ngwjZ5yWNS7jd18VWBez3tF_4twlqMtlHZeWoRTSgdWnoTGWh2JN30KL44nAZXzU_lDtYzycnxv2PgxwRLZdYSucYFUWnHfozt2uTYLQ89ebcy_wTO9V5Yzmp39ssZfXSBUcgRQaBICptQOZQOrbhL3Tpxe2RuNqHMzASZfNB7uayF4rUSFvrhe-F1m2uWCn7IgOWYUTenKO_pqLTy86OUlA5CXcY2MDd1rh1CWR_8kWaplnK1enb2Mz9gtA7vx0gmYOB3EVgtjYgeCqNsftOyBrtk16gEquJdkRRtO341AC4rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از عادل فردوسی پور و وزیر ارشاد در حاشیه مراسم یادبود اکبر عبدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/676601" target="_blank">📅 11:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676600">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2ZiNTusisTcoUJj0NsN9CCZH7WuboSGEGtPV_gTaML6iwGkNdRGuCqkTf-efVkU_CupauzqN3G00m7__xcD36I760rouswR6kvR1v1oKC-2IzM1O3GkKKnEOk6VAoZ_qBhVauS2SHZFlIc4SaahNKDBJvav_6Mc3GTMl7nCOU6NORXNaVxNG5-uPma40goukYSFZvZb7RygNnUsLzFo4v5coAV1rpEdl8-EiGtVnEzCXG7tvHQN6s20hnnB_dVjo1z7B7_PtZFZm4D6vI-uYxVUD8_AvZHL2bfo5goIiGblM8WvJUKm4dTt8lL-ttQ-3UQbaMAP79t4ZsAJSKINeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موسسه واشنگتن: تنگه هرمز به قبل از جنگ بر نمی‌گردد
ادعای موسسه واشنگتن:
🔹
اقدامات تهران نشان می‌دهد که ترتیبات سنتی حاکم بر تنگه هرمز عملاً فروپاشیده و نظام جدیدی در حال شکل‌گیری است که هدف آن تثبیت کنترل ایران بر این گذرگاه دریایی است.
🔹
ایران دریافته است که کنترل تردد کشتی‌ها در یکی از مهم‌ترین آبراه‌های بین‌المللی چه میزان قدرت و نفوذ به آن می‌دهد. تهران در مذاکرات آینده نیز از اهرم تنگه هرمز برای تثبیت نظم جدید دریانوردی استفاده خواهد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/676600" target="_blank">📅 11:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676599">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
رویترز مدعی شد: نتانیاهو پیشنهاد ترور فرماندهان سپاه و ارتش را به ترامپ ارائه کرد
🔹
خبرگزاری رویترز در گزارشی ادعا کرد که بنیامین نتانیاهو، نخست‌وزیر اسرائیل طرحی را شامل پیشنهاد ترور هدفمند فرماندهان ارشد سپاه پاسداران و ارتش جمهوری اسلامی ایران به دونالد ترامپ ارائه کرده است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/676599" target="_blank">📅 11:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676598">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nt_v_g-BLFJDkGSAR7OczQLRE-nFJcrYDgi49hCWsrodHH1K55rNpeoYzBG_Ctv4IuHP2DUWwfKSsSiKA07xKEjOImp_iHDsYnNX8uAd8AT0_X_MSvwHDdQqOCuckoZeag7urtD2ei5b0k7b9beXaT8Cho74TT7qXd6wL3cN5px0c39ASjwnQr8WU4i6-vs0V2iFKEQaWflFzHqwl_VtAmX4nu01j2GjdhQ-lVhfZ3nXFPVU8sURi4SnKAxjgOgQP2ZXywEVoTYf0pANjNNs9xaope17EB9b_urHOyvtx130G5X_qDpF4FH27uZ1Jre2hMAPA6i4Fpfje4yA_myvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: ترامپ در جنگ با ایران وقت تلف می‌کند
ادعای اکونومیست:
🔹
آخرین دور مذاکرات به احتمال زیاد یک وصله ناجور برای یک توافق نخ‌نما خواهد بود. جنگ بین آمریکا و ایران متوقف شده اما پایان نیافته است. تنگه هرمز عملاً بسته است.
🔹
ترامپ از تهدید خود برای حمله گسترده به ایران عقب‌نشینی کرده و اکنون ادعا می‌کند که مذاکرات به خوبی پیش می‌رود. او در این جنگ گیر کرده حالا وقت تلف می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/676598" target="_blank">📅 11:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند، پاسخ سختی دریافت خواهند کرد  روابط عمومی سپاه:
🔹
شب گذشته دو تانکر نفتکش با تحریک پرنده‌های آمریکایی قصد خروج از مسیر ناایمن جنوب تنگه هرمز را داشتند که پس از وقوع حریق شدید در یکی از…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/676597" target="_blank">📅 11:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676592">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e83e267a.mp4?token=OxrnmmfnyNALoUzo3fsDvv69ERqRECLBmanGODfe7uJo8-vRg5SMr3xLkCGhAbrpRiA93cVDtJLwlgOI6ce-sR17ZzFZfl_aojZCxIiZWVZFY1zCd8Q8nCveeGytICzy-GI1XntXcF-AVFxqyMNIhhTwY3z06bvaXOJUVBxfiM5UFfqXFa-0nqql94r0fUlowVPD81D_s_5TWD6BqNDyYi42Q8eGuOiBs6XmykrtbQLppjbQpyRt5jMvum-_V3s1PToCXFiDkA-RvYqFx0DxNn9hhBcT7qYMXKthSvR2dRpUzQqZCffqXfEoECD4PKG4DrGPLwhJhBAMInSBQi1IGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e83e267a.mp4?token=OxrnmmfnyNALoUzo3fsDvv69ERqRECLBmanGODfe7uJo8-vRg5SMr3xLkCGhAbrpRiA93cVDtJLwlgOI6ce-sR17ZzFZfl_aojZCxIiZWVZFY1zCd8Q8nCveeGytICzy-GI1XntXcF-AVFxqyMNIhhTwY3z06bvaXOJUVBxfiM5UFfqXFa-0nqql94r0fUlowVPD81D_s_5TWD6BqNDyYi42Q8eGuOiBs6XmykrtbQLppjbQpyRt5jMvum-_V3s1PToCXFiDkA-RvYqFx0DxNn9hhBcT7qYMXKthSvR2dRpUzQqZCffqXfEoECD4PKG4DrGPLwhJhBAMInSBQi1IGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ایران را دوست داریم؟ #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/676592" target="_blank">📅 10:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676590">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyxmjOCVH3cp27U3rKnYWkm6jnomxewQwwcqzOD34jzqds7h-7hzDdG5K_7anjn1gK6MCW0ij-aqdbsTYBEg2ySeiWRT5CERR6znYidGouApJqZXFCUZujBtuzCt215y762UrBZgOcPriPmiqCF7qSvC4bqA6xPcoNGOLbhBMiIxPpTpWP5J4cChBU50tlMgQSoxGD_6Z0ZwPHwVngn8VpaspGWR827Usiers7wUL9sTsRce4WraNBnri5JHyePEYqY0idH2Pi2ymSjqyK2fi7gptpV-VYlnVVxViApQoUFF2duNbWUmQT2sWicaZG41jBZERWmML14wi_mrQD4CEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا بعضی‌ها راحت می‌بازند و دوباره شروع می‌کنند، اما بعضی‌ها سال‌ها در یک شکست می‌مانند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/676590" target="_blank">📅 10:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676589">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0GbDcNoBlbwnwUEvZQKClMVmVoHIEUqsZ7M4u-40EnSeVchTWoMABUS0EN3Cc78Berhg_cOHxTeWRGgovpLg47CvMJCO6xGmhafRoDTUsNuIgd78WOIyDQNZmJw95SNtHoUrma3Kca460iYWvLWu88qjmHI4S-7a59GDhfRXeFc0z4M-7Rlu0IZgG53Pw2YOUmLJ0bKNV1Nrw2h--IjQtopioiVcrGyDJGqPPKKYdy5aNGANfQKEesH9ZlOvcuRTwJO2PgR6Pf0VGmMYvH6AXK1qd_icNx1e9536Jt-qzJjgGuuwXP7ZekIFFFbTpJC5Bcg_iMI1eYXtNmfLrIZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگی که ترامپ نمی‌تواند برنده‌اش باشد | تشخیص اشتباه شکست‌های آمریکا، ترامپ را در ایران گیر انداخت
🔹
دونالد ترامپ بیشتر از هر زمان دیگری در رابطه با جنگ علیه ایران در مخمصه قرار گرفته است، این را مارک چمپیون در یادداشت خود در بلومبرگ نوشته است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3234105</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/676589" target="_blank">📅 10:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676588">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3567e0150.mp4?token=OURneAJMy1Y6Bu_RdVYn8xkk0jSvEIWdBoKYSrtgZLvfjASTqmJXabaBv3Y7z8Hu3GEB1qxDelil09LfeFjs0-ES1Lj-RilYfWPc9JanVwuwMXc4hrsU9I48QXHi_iHbBnZRjSdwg6RZPbImBB7QCRIBdeQskkDwoR-dTrOPG6Ec7bEjBfPzTSCc9av5PkAWXMwPrFwplLW0keJLBmNx_WzJzCva2H6i0BPn4gWJodZ51PO1ZeGe-FGqSyahy5ldW1iCIJ0TPa69c-L-TLjtbKRVDG2wXym7KVJgMQtQsAWBg7Z0QV36sN1W41ckZvhiDBLg1kC09wJnlRofN-JSgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3567e0150.mp4?token=OURneAJMy1Y6Bu_RdVYn8xkk0jSvEIWdBoKYSrtgZLvfjASTqmJXabaBv3Y7z8Hu3GEB1qxDelil09LfeFjs0-ES1Lj-RilYfWPc9JanVwuwMXc4hrsU9I48QXHi_iHbBnZRjSdwg6RZPbImBB7QCRIBdeQskkDwoR-dTrOPG6Ec7bEjBfPzTSCc9av5PkAWXMwPrFwplLW0keJLBmNx_WzJzCva2H6i0BPn4gWJodZ51PO1ZeGe-FGqSyahy5ldW1iCIJ0TPa69c-L-TLjtbKRVDG2wXym7KVJgMQtQsAWBg7Z0QV36sN1W41ckZvhiDBLg1kC09wJnlRofN-JSgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلزله در ژاپن با حداقل ۱۳ کشته و ده‌ها زخمی
🔹
نخست‌وزیر ژاپن سانای تاکائیچی اعلام کرد که در زلزله ۷.۱ روز گذشته در استان کوماموتو، حداقل ۱۳ نفر کشته و ده‌ها نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/676588" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676587">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اکثر آمریکایی‌ها معتقدند ترامپ در جنگ با ایران پیروز نشد
🔹
طبق نظرسنجی یک نهاد معتبر آمریکایی، به باور اکثریت مردم این کشور «ایالات متحده در حال پیروزی در جنگ با ایران نیست.»
🔹
۹۳ درصد از دموکرات‌ها و ۷۳ درصد از مستقل‌ها گفتند که این جنگ «ارزش جنگیدن» را نداشته است اما به باور ۶۷ درصد از جمهوری‌خواهان، این درگیری نظامی ارزش عواقب آن را داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/676587" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676583">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmnfBDbKazL0Zo7idUoM4iwe_IOQ63H-yiz_SA27qSfUkkyLa2d9X48vL1thVj47iReK8KJeggeUXl6hZjUT0Ub55yHaVeniYCYpF-AHDTHRzltMIlNupdyhGQFivhbx1ptVcPFvpIsgeXDzTFr4c3pyshBhPs5427E7-v2OEDNyOdLVHXx_wISS4KUruXbpSKArXtFl2-dJk0WSUDVfV5qQ0ygZ2rM_gfyQaSjRZzII66QmYrGttQ29RMiBEhCdzqxXjvOyN4vtTd_FNhQDRZJYdu5FBXUUo6sfmO-cFgHd04M6-WF3mcf5Ig6fhpzEnVrQtivi3WsYmhWBEqyfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzWd_QAr946V8X7gyAL3dIdllSe0Sxj5-n-4taxdr4t-jaNMJvL3n_fCHmjRsSJ6z0LPtuV2QlGXisg4Bk4IERpkC253KS2eKkfYMSP_UXcsZxKuHBFLOi04E7cwjbvQjt6k1mZZk6FxMpsmFOZ4B4_1hUDi17q2XA5iKEmp0OWSOywV6Nqsp9n2Qr5bLysm1RF3F2b2dG2YA4WpyQmlcZwMLyXf4Py8eK_J4vrhmZExMRoG7oZb4D9iOR4DtK_k0EdVDIQlY02cYbMiEefy5P6Y2iotCxbFkqnuuEYpH7EsEjhyuvL0NT3_9bqZfzTXsvyMu9aX83VEABjW3b5ekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvDiWSdtSsvcOVwep2Wk9axH7shjtm3UEUb_ev3LEN_fxqyUXjuMaKSNgTC0ZKQ4DV7rfkabJVEmXJvsGBLTSaHGIV0e6FtVlsBNFZp69oUMYlRtNC1Wr5q8dZGOYInF0KBgEgRxVToRXMfTVmGkJ2BQLFzmPufHXZkde0-264-XEck3ldZMAlbhaObZdRamRgHxP80S2sgjez1yAi1CW0YHCInHihY2sy29zOU3UvuENsDPNtMm8gZ6XhKCbLIP0H9zs-L5axp2FYDtQBsup9V1KtTSRqxT30Vr7i9BCkzGWI717J4jEulTL7hKNUoqK-9vAs41zj_VlY4cMM0Zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی از پارکینگ مرزی مهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/676583" target="_blank">📅 10:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676582">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30fc4e3b69.mp4?token=pmaGqRvjQPqHJJzbedV983SvAPNAo5f2z4npZveS_JQCjAFLfIERtfxFQGJ_JTopfIGmfoWuUDpSryU3F1SI47OEhp7w_uXR_VbQQol55DaSrCNJXPrkPkCVjsRWA8-R7SdAJpTWSbRDeMzvzeX9h7EulMlf8K11CngdECDJ4_0pP2bem0Pqg-KB-xA9yuoWYGdZjSK4ein4n6EsMIkqQV2YFRN-qUp1O--Ahd6_o09CaSqMBVfEe00XZWiHETS3rad49o_8OnxdcWDgW-6uAZky-igncf0LG6JI182Iy1Xz3vl2-XZz8dh_8cd04lZEvnDUn_5L_czYZALclWOlSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30fc4e3b69.mp4?token=pmaGqRvjQPqHJJzbedV983SvAPNAo5f2z4npZveS_JQCjAFLfIERtfxFQGJ_JTopfIGmfoWuUDpSryU3F1SI47OEhp7w_uXR_VbQQol55DaSrCNJXPrkPkCVjsRWA8-R7SdAJpTWSbRDeMzvzeX9h7EulMlf8K11CngdECDJ4_0pP2bem0Pqg-KB-xA9yuoWYGdZjSK4ein4n6EsMIkqQV2YFRN-qUp1O--Ahd6_o09CaSqMBVfEe00XZWiHETS3rad49o_8OnxdcWDgW-6uAZky-igncf0LG6JI182Iy1Xz3vl2-XZz8dh_8cd04lZEvnDUn_5L_czYZALclWOlSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا فصل زردآلو تموم نشده، این مرغ خوش‌طعم و متفاوت رو‌ درست کن
🍗
مواد لازم:
🔹
زردآلو
🔹
ران مرغ
🔹
پیاز
🔹
رب انار
🔹
ادویه به میزان دلخواه #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/676582" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676581">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoPYKvRFsOHlx_yEPVgycRI8lfD-l5Q2mkA4WCZs5ioHwy7ww3Tc_RtKSz4z9_iHtJDs5aMeIyiFjV3hq8e50ksRZXJDzMx3L5RxRTN_JqFDMep0Kkcf5K5_k7F-Io8JxM1N3CdtOfR9GgpwL3CYdgYPTMeVL1ZSaFhOzWF9uqkstmPYlECF5zuKfTJYjDs6pIiF2JhU9u7dtKndIgWzZIO1fzL9rKaZ0Hb09acqn4Xka33ISN6q5f5QCpicDQ7n5h15Fy6uVuOBUVCcB6-g8030MadvlOw50B8CvpDxGv2qQZRkx6nPF7hFDd6hrjUCLEQIPKPIIwyY2hOR7fQk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/676581" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676580">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
نتانیاهو: ترامپ را به حمله علیه ایران ترغیب نکردم؛ مذاکره هم روی میز بود
🔹
گزینه‌های گوناگونی را درباره ایران با ترامپ بررسی کردم، از جمله مذاکره با آن برای دستیابی به توافقی گسترده‌تر، ادامه محاصره تنگه هرمز یا انجام اقدامات نظامی
🔹
من کسی را گمراه نکرده‌ام و هیچکس به ترامپ دیکته نمی‌کند که چه کاری انجام دهد.
🔹
قابل پیش‌بینی نبود که ایران تا چه حد می‌تواند تجارت از طریق تنگه هرمز را به اهرم فشار یا سلاحی تبدیل کند./ انتخاب
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/676580" target="_blank">📅 09:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676579">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b9669417.mp4?token=NL53sOLyozpf6Sg8PkxbsjanMPM7dRU7Ne6MA9EHz3aDrc0aN6ECPEWdaRHGWjVXvHhUfuLqVo5geMf6hC-AaOfAjLQBPFoBRmtfEvwrnfpIRV8rium1StJpysGMlC5LCgdEWApA9Zgj3NuI8p-Anl4MWuXbbbgYV50suPbBTUnXrdrWGZergmc3-FTaGCBaU16PCml9XGhuKHUT-0auHymidycVs1x82C-u0I8D7fT24Ak_CKdh1yTq3GxiTeWOtF9oQS_ESblAoT16ZTlVrS_GRj2ZQ-Q_bRAMcadFM1g8a4gRHblF5KGg2v5RFeWXxgW0SLSqvYatSIUMeJ24sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b9669417.mp4?token=NL53sOLyozpf6Sg8PkxbsjanMPM7dRU7Ne6MA9EHz3aDrc0aN6ECPEWdaRHGWjVXvHhUfuLqVo5geMf6hC-AaOfAjLQBPFoBRmtfEvwrnfpIRV8rium1StJpysGMlC5LCgdEWApA9Zgj3NuI8p-Anl4MWuXbbbgYV50suPbBTUnXrdrWGZergmc3-FTaGCBaU16PCml9XGhuKHUT-0auHymidycVs1x82C-u0I8D7fT24Ak_CKdh1yTq3GxiTeWOtF9oQS_ESblAoT16ZTlVrS_GRj2ZQ-Q_bRAMcadFM1g8a4gRHblF5KGg2v5RFeWXxgW0SLSqvYatSIUMeJ24sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باید گریبان جنایتکاران جنگی میناب و لامِرد در محاکم قضائی داخلی و بین‌المللی گرفته شود
🔹
بخشی از پیام رهبر معظّم انقلاب به مناسبت هفته قوّه قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/676579" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676574">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
بلاگر متهم به ضرب‌وشتم زنان در لایو اینستاگرام، بامداد امروز در خیابان مطهری تهران دستگیر و روانه بازداشتگاه شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/676574" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676573">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW55CSaaQCBOH4noEvIA4rG0ZgWGtX0kVifI9_TWhe1eB4gaFqO9ihm_nIXxV9Kz4vuZyCDJYUOTswytzf1GDDqu0Bk8__YDuSioj6OjHw7ZOf_iKv-f6dc2Ojz5IXZWTvt4yGwaaSpFC5D5lWhS2szUEwQxhILR9z7TqQLvOIGo66IYLLNslRkv4tv33ievhbXizgYnTd2pat49EwmNSXYpBuF6nMPqMP4h3qG9HZZXUAnXibNNcgLpmwGsWbi1j8xyV9JQ13xGNVglp3KpIpmE067OUu5vP8-gTproarGe_i6JoxYzoOvtJvBYhGfIg8at2sTQq9X2hkpw-M0LEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ ماده غذایی برای رفع کسالت صبحگاهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/676573" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676572">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3Ne3eZsmPVfDUj6ezUxCDn3YThUN9E1W_GureXn9ELejwgxFxXh4KA1kp6Dx8njeF55eCc01gpjfv5u3jZzx0qmbbwbST90SZMhLW63n4-CAtkrYSqE1tcosIhDYBRRioaUob9uQ6B44w3icXd6iPE08_XvSvY_0ByLDqgT_9BXDIx6sXVLhZGI5xeMrWPED3kscvSkvuN7-4tJGq61e5kZjmbpJpxgJ0Zhgak0iFCNA9izsDxNgjEnUH9iA8RuaZjLo7CVLMhYqU-E4xpAIcrsgdqYHrxBuyHofDa4Iy1lB_8YMsdFMo3RtEG3lGwNzdVklOIJVkfUGiuQTokpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور کشتی قطری از مسیر ایرانی تنگۀ هرمز
🔹
سه هفته پیش تهران پس از نقض تفاهم‌نامه توسط آمریکا عبور و‌ مرور در تنگۀ هرمز را متوقف به تأیید ایران کرد‌.
🔹
این کشتی قطری با داده روشن و از مسیر تعیین شده توسط ایران گذر کرد و بدون هیچ مشکلی به‌سوی آب‌های آزاد می‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/676572" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676570">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2455db6e15.mp4?token=R_fsjTWRTDn6Ee2ikDyXifV04STpaY9k6W832m3NtdRVxd_pE8mK2u51c8F1rT2SisAACkG51OiTsb5WbSbcLPqu0d1lvBZ905_c0toBCLms0vX1MsSK39VEIkHZp9W6tflI0CmH-_SVcIMUw88bj0wwR1B0stgxY2EGvIVQ7u-pjMSbAOtO-Buewc-PB2WatywYjS02HIjE1j7A243mJhDgH0lUVUIP6zev4RkexRBtCSK84xawTWAHIsXSxUYpgZERWeSQpQf8MBVTDYOn5qq7wQd9CDKEGcowu3DUYfxKa9vB2by3kXr1uxMvlunoxn-TG-8qVkzFlT5RVBqIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2455db6e15.mp4?token=R_fsjTWRTDn6Ee2ikDyXifV04STpaY9k6W832m3NtdRVxd_pE8mK2u51c8F1rT2SisAACkG51OiTsb5WbSbcLPqu0d1lvBZ905_c0toBCLms0vX1MsSK39VEIkHZp9W6tflI0CmH-_SVcIMUw88bj0wwR1B0stgxY2EGvIVQ7u-pjMSbAOtO-Buewc-PB2WatywYjS02HIjE1j7A243mJhDgH0lUVUIP6zev4RkexRBtCSK84xawTWAHIsXSxUYpgZERWeSQpQf8MBVTDYOn5qq7wQd9CDKEGcowu3DUYfxKa9vB2by3kXr1uxMvlunoxn-TG-8qVkzFlT5RVBqIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر لو پورژ در فرانسه در آتش سوخت و این حادثه جنجال بزرگی را بر انگیخت
🔹
۱۸۵ خانه در لو پورژ سوختند و ۳۴٠٠ نفر از ساکنان بی‌خانمان شده و همه اموال خود را از دست دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/676570" target="_blank">📅 08:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676569">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند، پاسخ سختی دریافت خواهند کرد
روابط عمومی سپاه:
🔹
شب گذشته دو تانکر نفتکش با تحریک پرنده‌های آمریکایی قصد خروج از مسیر ناایمن جنوب تنگه هرمز را داشتند که پس از وقوع حریق شدید در یکی از آنها هر دو شناور با سرعت به عقب برگشتند.
🔹
کشورهایی که در کمک به متجاوز دخالت دارند، اگر رفتار خود را اصلاح نکنند، پاسخ سختی دریافت خواهند کرد.
🔹
تنگه هرمز تا زمانی که زیاده گویی ها و تهدیدات مقامات آمریکایی و دخالات آنها در حرکات دریایی در منطقه وجود دارد، قابل بازگشایی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/676569" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676567">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a211f83490.mp4?token=IkqamzEutath2UZ6zKC73dXy9u6tOSaQ-6LIX0UdkJEAzF8e3XhnHqArzvr-TEm9sKj7pWByJW0JSj5MgLy1hpQ21ojA5yw0LZGnXYLLzwb5xWzOAJGbuxwlnFgbi58_IfxP0M0r9DPo1kNw-y1NfEsyvMJAF9CT0vDxMd0gqhnh4EwC5FZLgUdTrAhwcDDOt-c1XiMalEPc-d1UXmN3SSMEVu8I4r69XWifKjcY4ZxpoMH68-twdDms2zzKhTLMlsURrJJP87OzmOeszI8vhip3uapMsRJR0e-mIDxhbDVrRBH66vUXUNnX34cDu65_CN8GLgZkDtMD57UM8cBeXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a211f83490.mp4?token=IkqamzEutath2UZ6zKC73dXy9u6tOSaQ-6LIX0UdkJEAzF8e3XhnHqArzvr-TEm9sKj7pWByJW0JSj5MgLy1hpQ21ojA5yw0LZGnXYLLzwb5xWzOAJGbuxwlnFgbi58_IfxP0M0r9DPo1kNw-y1NfEsyvMJAF9CT0vDxMd0gqhnh4EwC5FZLgUdTrAhwcDDOt-c1XiMalEPc-d1UXmN3SSMEVu8I4r69XWifKjcY4ZxpoMH68-twdDms2zzKhTLMlsURrJJP87OzmOeszI8vhip3uapMsRJR0e-mIDxhbDVrRBH66vUXUNnX34cDu65_CN8GLgZkDtMD57UM8cBeXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های آمریکایی از خاک کویت به ایران
🔹
پایگاه عراقی المحورنیوز با انتشار تصاویری ویدیویی، از همدستی کویت و بحرین با آمریکایی‌ها در تجاوز به جمهوری اسلامی ایران خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/676567" target="_blank">📅 08:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سه شهید و ۲ زخمی در حملۀ آمریکا به محله چاه تنگو شهر قشم
دانشگاه علوم پزشکی هرمزگان:
🔹
در حملۀ دشمن آمریکایی به منزل مسکونی در محلۀ چاه تنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند و ۲ فرزند ۷ و ۹ ساله بر اثر این حملات زخمی شده و به بیمارستان منتقل شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/676566" target="_blank">📅 08:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676565">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TymzKJ3xsFVDglqbl_Vq5IM6cBdnTFM_9KpzRqpMJHTnVnMDe7GD_Mt1CBjczJUW5yML3-a3-Ukq-2PF2FwkHllGQURC8RACJTCVT34itK_11XVFb3YAbmtq4RqS7v7BKO_jzGn3nI4Ns4EzTz5YhDtAUz4uQEwfMbOnZEg8MGaTyB9Bi7s_u7ocT8ZibDn5Z22vbIv6D1bovSCWfJa_51pzk4TW9NTCYctX-HxaxUjJTHtgdwM41krg1Tbqd6MFMwjg1NvwFXUKGUubaYU60tNsXODykeC7ouRKRY1MvTyO6YHj1sSaoxi3qGM13ex8tFbQ3Yi23TIWgq77mCu0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ترامپ با ایرانی مصمم‌تر در حالی روبه‌رو است که دامنه جنگ گسترش می‌یابد
🔹
با نمایش قدرت از سوی ایران، به نظر می‌رسد دونالد ترامپ بار دیگر در حال بررسی گزینه‌های نظامی است؛ این در حالی است که پیش‌تر طرح‌های تشدید درگیری را رد کرده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/676565" target="_blank">📅 08:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8238f76942.mp4?token=jFuuRMY5HsVU5CQdary5KMoG6IPiiX0sKG873JLQ-gPBm4Zo5olXM2TDxg2s_jPk0a6NHLtfxZ8dkw0FXQTUTJX_gj4yKb8kWNDovnunwvj0SsO8zWxvbqLJPJA5YG0HHFCsnv9qmoWN9wwYm4RIEyhWVD4m8xdS-RmP2-cTHDj_y-hlt9zhm6i5ULJciIlNq8f7apGK7b_aC-PF8KEIB2J3CRl_azbytDsBOyi16a1-SuDRFeoX8b3Ui6cPG69GNfDa0Hbkn93ppucZrOak-SBjL56twYhWBvNo0droIrlz6SVbYyyrZGBsAnpKi7xocBpTPbk-lH7i4BFeLJJCQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8238f76942.mp4?token=jFuuRMY5HsVU5CQdary5KMoG6IPiiX0sKG873JLQ-gPBm4Zo5olXM2TDxg2s_jPk0a6NHLtfxZ8dkw0FXQTUTJX_gj4yKb8kWNDovnunwvj0SsO8zWxvbqLJPJA5YG0HHFCsnv9qmoWN9wwYm4RIEyhWVD4m8xdS-RmP2-cTHDj_y-hlt9zhm6i5ULJciIlNq8f7apGK7b_aC-PF8KEIB2J3CRl_azbytDsBOyi16a1-SuDRFeoX8b3Ui6cPG69GNfDa0Hbkn93ppucZrOak-SBjL56twYhWBvNo0droIrlz6SVbYyyrZGBsAnpKi7xocBpTPbk-lH7i4BFeLJJCQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر زانو درد، درد هنگام راه رفتن یا احساس ضعف در مفصل زانو دارید این ویدئو رو حتما ببینید #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/676563" target="_blank">📅 08:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676555">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISAVU7tg-OCLTHuxOTw7YqjjGbwJEJAqW4RwGmh6uIrJLiEXX4sp5qm-3QCHzLHxKhrJixv1QDj5nCBowHt5LbWnhl4gwGCalaV1-K9r3WHIY8tdWuNpAvYP6ZGf466MGPeySJ-NuQ8cUuj_BchB7-LX32pgeV39AiAezX4fpRp0visR2DkzKDGoqZMvcKekb8agAxbABY_EnsIDLE9lpUqz1wgqsLQgk3QC9-TDZCaT0jQPiPg9cBuKradIEXp1IG6wPOz-viZhG6FiPfPQkK5ebGtSeuSYnJBsVMTSGnLI7s4OyVNwuhDZlUbzPnNq6GyIW67CzDJmyNYJ_ffewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۸ مرداد ماه
۱۵ صفر ۱۴۴۸
۳۰ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/676555" target="_blank">📅 07:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676553">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0654b37ac2.mp4?token=RjZArAHkyzeqw5Vjk6TyLcknrj90HJhW5q79hV4aoCXCGBzUyfx-ANE4t-e73POHMi7LdthHQHoCMiqMhMg-n9WNaDmjxhCEi3nTDoGtv2QAlhl62GIO7MeHCH-eVKlluDqUHDhZBKejQm0yYIwRveR4j1-OABQfJ6-KTPi7Zxa6qk2DRH4M5TK8qlwnCvMZ_6qLwJP0_cZiOHWZxG9-3EzK9POInoH-soVm7EFCVpgDy6c4HjydVioggZef4kSoa49HRQg1pVdnOaVHuFTe_jhBap0e5ACqfkDgY6tbWK8gdJrR7WkN1imrkiuqNZ8Ugnyk42levLwGaaGSHQvYQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0654b37ac2.mp4?token=RjZArAHkyzeqw5Vjk6TyLcknrj90HJhW5q79hV4aoCXCGBzUyfx-ANE4t-e73POHMi7LdthHQHoCMiqMhMg-n9WNaDmjxhCEi3nTDoGtv2QAlhl62GIO7MeHCH-eVKlluDqUHDhZBKejQm0yYIwRveR4j1-OABQfJ6-KTPi7Zxa6qk2DRH4M5TK8qlwnCvMZ_6qLwJP0_cZiOHWZxG9-3EzK9POInoH-soVm7EFCVpgDy6c4HjydVioggZef4kSoa49HRQg1pVdnOaVHuFTe_jhBap0e5ACqfkDgY6tbWK8gdJrR7WkN1imrkiuqNZ8Ugnyk42levLwGaaGSHQvYQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های آمریکایی از خاک کویت به ایران
🔹
پایگاه عراقی المحورنیوز با انتشار تصاویری ویدیویی، از همدستی کویت و بحرین با آمریکایی‌ها در تجاوز به جمهوری اسلامی ایران خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/676553" target="_blank">📅 06:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676551">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
اعلام پایان حملات امشب به ایران توسط سنتکام
ارتش آمریکا:
🔹
نیروهای سنتکام در پاسخ به حملات موشکی دیروز به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند».
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/676551" target="_blank">📅 05:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676548">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
حملات تجاوزکارانه آمریکا به نقاطی در ایران
🔹
خبرنگار صهیونیست وبگاه «آکسیوس» بامداد پنجشنبه به نقل از یک مقام آمریکایی خبر داد: «ارتش آمریکا در حال انجام حملاتی به ایران است».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/676548" target="_blank">📅 05:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3995d7f98b.mp4?token=OxMl0uSdJWktnaSmJSq3jqOU1BkQjJPbFFurFUsgvfz2OivjpfdCz4v7GNOxvpyszsMOrHC764t7cfDLh-Bl12fa8hIlVPB67A9oD5EUhkNmxx6l0O0oqVVlKdHo4eMzdDYVnNnENU5qkypWxZV49eQLJZX8JU8X54_Qx9nif4tsW_DcfykjclnbBG-N3RsVS0fcssKxifEMXS4TjcUnE79IxHIAKC5kQoaZS5jUmtVuHAzixTZXfe-Mpb4qIfs30rRvswOqt3ZSzE2In8YhAeIHVbVhK3e6agS5PXdK-puZK0hG5zO1gPLpTXyJi8vcxUgfVzW8KXMvcHHO2bQcNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3995d7f98b.mp4?token=OxMl0uSdJWktnaSmJSq3jqOU1BkQjJPbFFurFUsgvfz2OivjpfdCz4v7GNOxvpyszsMOrHC764t7cfDLh-Bl12fa8hIlVPB67A9oD5EUhkNmxx6l0O0oqVVlKdHo4eMzdDYVnNnENU5qkypWxZV49eQLJZX8JU8X54_Qx9nif4tsW_DcfykjclnbBG-N3RsVS0fcssKxifEMXS4TjcUnE79IxHIAKC5kQoaZS5jUmtVuHAzixTZXfe-Mpb4qIfs30rRvswOqt3ZSzE2In8YhAeIHVbVhK3e6agS5PXdK-puZK0hG5zO1gPLpTXyJi8vcxUgfVzW8KXMvcHHO2bQcNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله آمریکا به یک محله مسکونی در قشم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/676542" target="_blank">📅 05:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d885c0805a.mp4?token=UFLjE_joQ3f8fQdNPcRD-5zUsNKTtzkpadWGy6rnXJU_7DaFzgErIeFqJ40WSTwUVr3EM-fBynBpMZqoLnBIyMo7NP2t3ytsiL5ttSwk4JZP6_Tb4IspRc814rgznlajLdWwzAn6m625vlhGyoOowNWhCyIklHF16rMMqbpC__GX0bKQoTIyvjiAgMEbnNpkP0GvDb7cM0MA4_hi8C37porzTP0I0i9yZxY9fXgPmeECkDQZ7aA2d7AxR4hm9u4TpsMk7eCeOM57yRJmqVJcqmEXRjmVUFidk6mQ6DQL4kmHHXKM-vsbGU3gPnN9HV132DmJB3Bt_JWilDza3E8B6nKd1JoTYY7ee7qEaQ8YKmUJPa_UxwrT-q38hsODwWwMgoojZMBFZMNzVipxY_SbTJSRFK1HG-4WbuhwMdQEEMDRNpyqDybNVVuKrfSVvEqi6FTVexUjwC02naaoX8JFsde_fXaU6lVl5s53so5cw9CKDpjK7Z0auIJWIOPjDiC_DM-zBHuCNqu5EmLJu1nPguy_FGxNz3kERMprAbH7sM8JQ8ZKElxZIAYLfmpzdgYFAV6UtT9Fl_fB3o1wouV1VyznZFE7ur_xtcBnBx27Zkom28JV572ifHCNAdrdlun7uMVXFJ8-nw2AX6Bw5QP3_wMPpjgSMKih7M6-anLnofI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d885c0805a.mp4?token=UFLjE_joQ3f8fQdNPcRD-5zUsNKTtzkpadWGy6rnXJU_7DaFzgErIeFqJ40WSTwUVr3EM-fBynBpMZqoLnBIyMo7NP2t3ytsiL5ttSwk4JZP6_Tb4IspRc814rgznlajLdWwzAn6m625vlhGyoOowNWhCyIklHF16rMMqbpC__GX0bKQoTIyvjiAgMEbnNpkP0GvDb7cM0MA4_hi8C37porzTP0I0i9yZxY9fXgPmeECkDQZ7aA2d7AxR4hm9u4TpsMk7eCeOM57yRJmqVJcqmEXRjmVUFidk6mQ6DQL4kmHHXKM-vsbGU3gPnN9HV132DmJB3Bt_JWilDza3E8B6nKd1JoTYY7ee7qEaQ8YKmUJPa_UxwrT-q38hsODwWwMgoojZMBFZMNzVipxY_SbTJSRFK1HG-4WbuhwMdQEEMDRNpyqDybNVVuKrfSVvEqi6FTVexUjwC02naaoX8JFsde_fXaU6lVl5s53so5cw9CKDpjK7Z0auIJWIOPjDiC_DM-zBHuCNqu5EmLJu1nPguy_FGxNz3kERMprAbH7sM8JQ8ZKElxZIAYLfmpzdgYFAV6UtT9Fl_fB3o1wouV1VyznZFE7ur_xtcBnBx27Zkom28JV572ifHCNAdrdlun7uMVXFJ8-nw2AX6Bw5QP3_wMPpjgSMKih7M6-anLnofI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان: حمله دشمن به یک منزل مسکونی در قشم، چاه‌تنگو؛ عملیات جست‌وجو برای یافتن دو نفر زیر آوار ادامه دارد./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/676540" target="_blank">📅 05:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676538">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
انفجارهای مهیب و پیاپی در اهواز
🔹
دقایقی پیش صدای چندین انفجار شدید و وحشتناک در اهواز شنیده شد./جماران
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/676538" target="_blank">📅 04:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676537">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01ec2c1ce5.mp4?token=WOpMpdOTqGsCgdF-mfGx36DGrWgAoGpp_b6pnjOTZxNBIwtpvQRq5t2une7VnjVMryOIIxYhzIRJs-JCePYf_BmdJZ0rHmeTPTGJ1CUeNrifv5W4rq0eDrXMPwdQRnWbN-O9623EzsuIJqG_0ijqoITK1z_CHtXKl_bl9rVOYB0_Y-Z07GqFNLYc3gFCfF2Hh368TB2fg1qUydQjjyMAgzKoa5_LW3SfAma41j-9OuafsXW1WKPfTfisjfcWT_IDPPL7Jc_F9OgvynbnwW7wTllywqBZ5bdEnVvyrprpi8ZapzNeR7xOnH9Qn79PerKGaxFs5laoB68n-0PJym6Tpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01ec2c1ce5.mp4?token=WOpMpdOTqGsCgdF-mfGx36DGrWgAoGpp_b6pnjOTZxNBIwtpvQRq5t2une7VnjVMryOIIxYhzIRJs-JCePYf_BmdJZ0rHmeTPTGJ1CUeNrifv5W4rq0eDrXMPwdQRnWbN-O9623EzsuIJqG_0ijqoITK1z_CHtXKl_bl9rVOYB0_Y-Z07GqFNLYc3gFCfF2Hh368TB2fg1qUydQjjyMAgzKoa5_LW3SfAma41j-9OuafsXW1WKPfTfisjfcWT_IDPPL7Jc_F9OgvynbnwW7wTllywqBZ5bdEnVvyrprpi8ZapzNeR7xOnH9Qn79PerKGaxFs5laoB68n-0PJym6Tpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه شلیک گسترده موشک‌های آمریکایی از خاک کویت به سمت ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/676537" target="_blank">📅 04:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان: حمله دشمن به یک منزل مسکونی در قشم، چاه‌تنگو؛ عملیات جست‌وجو برای یافتن دو نفر زیر آوار ادامه دارد
./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/676535" target="_blank">📅 04:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676533">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
دقایقی پیش صدای چند انفجار در کیش به گوش رسید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/676533" target="_blank">📅 04:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676532">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کازرون
🔹
منطقه‌ای در اطراف شهر کازرون هدف حمله دشمن آمریکایی قرار گرفته است.
🔹
اخبار تکمیلی متعاقبا‌ً اعلام می‌شود./ تسنیم
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/676532" target="_blank">📅 04:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676531">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
منابع محلی از شنیده شدن صدای چند انفجار در بوشهر و بندر عباس خبر می‌دهند ./ همشهری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/676531" target="_blank">📅 04:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676530">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d49cdbe6.mp4?token=Rr5eC5o-VF8622374D51PvFRLNQFvxltCBIrOVaVy4xgWEUSKR0rVCS2iXaWyimaPpJDgT72TrahORPAaKJVaLsQTEy8c7lAFSdwTbCnDMTo3Bt5vMcv5JvrNOtE91rFVhyTDMcJkcAZLG_ZGXkWdYn97qFaPQjY5merHNp41J4ik6nWbK4_8WtKaGEJ7phobEZupNHInmQfYRPIk1ajb6FlZQHTVdCRJnPAeiP43nDDaONJjP7ynhvMNJaFi1X9CV1oDCoWiB09HklRGYfAHl7b0VLwcOW8xwPWelcvoqvuoKLTI8_HSSjoevKBvsahTOnXUMd4EdZ0tftnA59A-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d49cdbe6.mp4?token=Rr5eC5o-VF8622374D51PvFRLNQFvxltCBIrOVaVy4xgWEUSKR0rVCS2iXaWyimaPpJDgT72TrahORPAaKJVaLsQTEy8c7lAFSdwTbCnDMTo3Bt5vMcv5JvrNOtE91rFVhyTDMcJkcAZLG_ZGXkWdYn97qFaPQjY5merHNp41J4ik6nWbK4_8WtKaGEJ7phobEZupNHInmQfYRPIk1ajb6FlZQHTVdCRJnPAeiP43nDDaONJjP7ynhvMNJaFi1X9CV1oDCoWiB09HklRGYfAHl7b0VLwcOW8xwPWelcvoqvuoKLTI8_HSSjoevKBvsahTOnXUMd4EdZ0tftnA59A-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکمیلی/
همدستی دولت کویت در تجاوز آمریکا به ایران
🔹
شلیک سامانه‌های موشکی آمریکایی از خاک کویت به نقاطی در ایران همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/676530" target="_blank">📅 04:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676526">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5fc7618d.mp4?token=EJI0pmaQjhGoLB7r7h6xZOTlS-5dGsKvwLw1w1s3Kk9lFMexAQ3e6He42glzs3kfd9_dcwnN1gqv0EM3v23sNNRPEqnPG22LR8-NkkqgneZdjuqd5uVHUeS9cMJ4FeEdNIHHR_fX4pDD9AhLWo3zyGkNUPn_fxNwX6HFG7h9GZY-fGr_332F5-7R-7U4cSWctfHIJC1xZhnoLOENWJpxuCby-uYsOqh2-wjeO0tES434bSM7yf4R5NhvVRmZ5SmQCLEpjEAUWUoH8k9CLYfzESXgMANBx2zsTdz0GKaa_jZwrcKbdl6XdViHTHRUpTrcw8eTS0KIzhfFaAxL0aN6GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5fc7618d.mp4?token=EJI0pmaQjhGoLB7r7h6xZOTlS-5dGsKvwLw1w1s3Kk9lFMexAQ3e6He42glzs3kfd9_dcwnN1gqv0EM3v23sNNRPEqnPG22LR8-NkkqgneZdjuqd5uVHUeS9cMJ4FeEdNIHHR_fX4pDD9AhLWo3zyGkNUPn_fxNwX6HFG7h9GZY-fGr_332F5-7R-7U4cSWctfHIJC1xZhnoLOENWJpxuCby-uYsOqh2-wjeO0tES434bSM7yf4R5NhvVRmZ5SmQCLEpjEAUWUoH8k9CLYfzESXgMANBx2zsTdz0GKaa_jZwrcKbdl6XdViHTHRUpTrcw8eTS0KIzhfFaAxL0aN6GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اطراف بندرعباس
اژدهایی خبرنگار صداوسیما:
🔹
گزارش‌هایی از شنیده شدن صداهای مشابه در جزایر بوموسی و کیش و همچنین محدوده دریایی قشم و تنگه هرمز منتشر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/676526" target="_blank">📅 04:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676523">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=Zu7yYkbm2xny-YVsgZGsheTSkMWCSe5ft4wLXRVDkkKraT_I7ktvCcmzd7d1GObd1jUnFMfTYMzfkFQV3BN3Fzpjg_TWJYe21QE-N4DOWwrbr91y2WJWsy4NCtHgytunmAitBv4_eYkSAVLFDDLIp9lhiVj_BAD1HCTPXGrLNu7mPgAehqzCva4FhZ9Rn2itr49KxF8Qavcil3kVwgyz5ZsIZhD1qb4Wk-zmOis9WCwWZ2uhfWAWbYWmvlZDPWX2zDaLTUa2Hp7t_Z62jiNEmantSFWLB5A47Tvn3IYoCDemFl_O_-MhzkCx48ao1bbeYvf3dcDltoSFFkYDbqRUgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=Zu7yYkbm2xny-YVsgZGsheTSkMWCSe5ft4wLXRVDkkKraT_I7ktvCcmzd7d1GObd1jUnFMfTYMzfkFQV3BN3Fzpjg_TWJYe21QE-N4DOWwrbr91y2WJWsy4NCtHgytunmAitBv4_eYkSAVLFDDLIp9lhiVj_BAD1HCTPXGrLNu7mPgAehqzCva4FhZ9Rn2itr49KxF8Qavcil3kVwgyz5ZsIZhD1qb4Wk-zmOis9WCwWZ2uhfWAWbYWmvlZDPWX2zDaLTUa2Hp7t_Z62jiNEmantSFWLB5A47Tvn3IYoCDemFl_O_-MhzkCx48ao1bbeYvf3dcDltoSFFkYDbqRUgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک موشک‌های هیمارس از کویت به سمت ایران
🔹
منابع عربی تصاویری از شلیک موشک‌های زمین به زمین هیمارس از خاک کویت به سمت ایران منتشر کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/676523" target="_blank">📅 03:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676522">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
گزارش‌هایی مبنی بر وقوع انفجار در آبادان و کیش./ همشهری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/676522" target="_blank">📅 03:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676521">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
گزارش‌هایی مبنی بر وقوع انفجار در آبادان و کیش./ همشهری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/676521" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676520">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1001d1ab.mp4?token=ruIE9BPuDxK7Fudr9w9lbu3J7glEVeleERlCOfjaJavvvkQKnxK103MkLogbFm6rDyr4OzdAmTrRy4kie7n5s6SbVAGI-UZaGd40kzOmTqEA1Txulz2Erjna7qpOf1iFt90wokOtP7OGQJpP5b9xCNRag1TVhmYApJ3fxPq4DqB73xQ6ysmKXIK3PHguayakbyt8kmC1pOjnnUJTKE7pCTgfYKiQRKOVX8LJp_juNPOhCBN5IqvW9rw1Y1sJG-ra6UCHuXDOdP3rLR0a-K-GVwUedvVeE_MxHhGeP3E048J21taadlxb1kU_1Eqw0FG_CrnlJHEuDgjvP9fFbSC-NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1001d1ab.mp4?token=ruIE9BPuDxK7Fudr9w9lbu3J7glEVeleERlCOfjaJavvvkQKnxK103MkLogbFm6rDyr4OzdAmTrRy4kie7n5s6SbVAGI-UZaGd40kzOmTqEA1Txulz2Erjna7qpOf1iFt90wokOtP7OGQJpP5b9xCNRag1TVhmYApJ3fxPq4DqB73xQ6ysmKXIK3PHguayakbyt8kmC1pOjnnUJTKE7pCTgfYKiQRKOVX8LJp_juNPOhCBN5IqvW9rw1Y1sJG-ra6UCHuXDOdP3rLR0a-K-GVwUedvVeE_MxHhGeP3E048J21taadlxb1kU_1Eqw0FG_CrnlJHEuDgjvP9fFbSC-NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها درباره شلیک موشک از کویت به ایران
🔹
رسانه‌های عربی از جمله «صابرین‌نیوز» با انتشار تصاویری گزارش دادند که سامانه‌های موشکی تاکتیکی ارتش آمریکا از خاک کویت به سمت آبادان شلیک کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/676520" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676519">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
حملات تجاوزکارانه آمریکا به نقاطی در ایران
🔹
خبرنگار صهیونیست وبگاه «آکسیوس» بامداد پنجشنبه به نقل از یک مقام آمریکایی خبر داد: «ارتش آمریکا در حال انجام حملاتی به ایران است».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/676519" target="_blank">📅 02:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676518">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پیشنهاد سنتکام به ترامپ برای حملات دو هفته‌ای به ایران
نشریۀ وال‌استریت ژورنال:
🔹
فرماندۀ سازمان تروریستی سنتکام طرحی را به رئیس‌جمهور آمریکا پیشنهاد داده که ذیل آن، تا دو هفته به زیرساخت‌های موشکی ایران حمله شود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/676518" target="_blank">📅 02:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676517">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
چند انفجار شدید اربیل عراق را لرزاند
🔹
به گزارش، شبکه اخبار عراق اعلام کرد که پس از شنیده شدن صدای این انفجارها، ستون‌های آتش و دود از منطقه قسری در اربیل به آسمان برخاسته است.
🔹
براساس اعلام رسانه‌های عراقی، هم اکنون سامانه‌های پدافندی کنسولگری آمریکا در اربیل نیز فعال شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/akhbarefori/676517" target="_blank">📅 01:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676516">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjCXb3aBdhceoPe6i5T6J3xziAt5H5mCgR6NPiKgVVn16GH_Ziz5DTrqR9K1ifbtXdc3bQ0YNKcexeYldy6Zc1gVzfXr81o9gRMoCXQ6lZDdwKGtSdVHoEjO4WrO1dbjnemhBEwe-LwM-SYZGwKdYNunIfNNGuhTKLcSjL0aLUD4CegXl-AGDRG_t148GrlDhyYTuEVDhZ3XU7FzgTUpwHbxA8UG5YD8mbDX__vK7ksqIquraCViFmlWyD3gHkiM-2bsav0mMuW03x8XtuamRUhWR0pFrNlAZt0Pl4eRLx_1ZKgJyayBQj36oy1-6UKgZM1I1F8c2pUZ_yfJIZ8jGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروشگاه آنلاین داری، این پست می‌تواند هزینه تولید محتوایت را نصف کند.
قبلاً برای هر محصول باید:
❌
عکاس می‌گرفتی
❌
لوکیشن پیدا می‌کردی
❌
ساعت‌ها زمان صرف می‌کردی
حالا کافی است یک عکس ساده با موبایل بگیری…
رقبایت دیر یا زود از این ابزارها استفاده می‌کنند؛ سؤال این است که تو زودتر شروع می‌کنی یا دیرتر؟
@digitall_cast
ارتباط با پشتیبان :
@Digital_cast_support</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/akhbarefori/676516" target="_blank">📅 01:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676515">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a98Y-UX7SNllfACX9ACm2f0_zK-K93mwjkjX--N3f3Y2ypAKyX_-xl8be4qyDlY0RtEBQswBrdCvBT2HbyeoByPCTkeUhabZsmHA2fMzWu4QrYwTup_9f2SNLbXoAolhsBtvE_31aqtW3nQSqDLApwpb9AhPSv-kS_JsO5Jxd_ADvEfIHoNAYWLqUu5nxtOyoWyIU00Zb_g1NMVYUKHaFMefSw-fOH2_M7kWZxIsF2rOgfDlA0rI5MV0vStYIdaQRu489jJy8tGJFB7vSHIWmsOrEGw6OkGNdqIUr9dn4tV3RfbBA3rVTSkvsPxWO_ztzYS8iEOXC50PufV6lNlKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسیاری از هواپیماها در خارج از فرودگاه ریاض در عربستان سعودی متوقف شده و فرود نمی‌آیند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/akhbarefori/676515" target="_blank">📅 01:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676514">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKXPOaRheJO9ckjHz5e_G_JBI02DGQ8OD94wU6FpMJFmlpXzMW_N1Y3hvcegzszomiHvdWa8Ynuu2sg16ESrSGeK-FRT2jtVmp2o79Mxgxx_audp0OTwIOBnI3awc0eymfI9PyX4YxllXmUdKfgZySpLMPHQffn0L4myFan1P9irPlVpEtldCibtfZ4QjWR3Lo052mt3nm-em0zNAcDAHqUfv8UZtItmIRD8k7F7FLTNIQv2IU00XogIKlHFezDlFYStaR5FMbhvWIMZkde8bkRPkZg93Z9SgM8_IIGRZ6s6V_BJQM0k8s4ej_YE59qhkAMHdVDSL6GAHfkpJrtAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعلیق فعالیت فرودگاه «ملک خالد» در ریاض
🔹
منابع عربی می‌گویند که فرودگاه بین‌المللی ملک خالد در پایتخت عربستان سعودی، بعد از شنیده‌شدن صدای انفجارها در ریاض، موقتاً بسته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/akhbarefori/676514" target="_blank">📅 01:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676513">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع انفجار در ریاض
رسانه عراقی «نایا»:
🔹
صدای دو انفجار نامشخص، به وضوح در ریاض، پایتخت عربستان سعودی، شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/akhbarefori/676513" target="_blank">📅 01:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676511">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
روزنامه وال‌ استریت ژورنال به نقل از یک مقام دولت آمریکا ادعا کرد که
دونالد ترامپ همچنان در حال بررسی گزینه‌های خود است و هنوز تعیین نکرده که حمله به ایران در کجا و با چه شدتی انجام شود
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/akhbarefori/676511" target="_blank">📅 00:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676510">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ترور ناجوانمردانه در شهرستان ایرانشهر
مرکز اطلاع رسانی پلیس سیستان و بلوچستان:
🔹
ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی که متأسفانه استواریکم "مهران سالارزاده" به درجه رفیع شهادت نائل شد.
🔹
تلاش برای دستگیری عاملان این سوء قصد ادامه دارد و اخبار تکمیلی متعاقبا اطلاع رسانی خواهد شد./مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/akhbarefori/676510" target="_blank">📅 00:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676509">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3c2975d3.mp4?token=E_0CTGRypleKqo-HQQhYYVd8jI0nBioL1ZsdNpwZIDNfYvUPOMO9r0anOHCktcV0Bj8OcrTkRlPrEylgdxvmIs6xeT2NXbdD2WKKllck5iu0jz7byx8trNmzph-ZLp-xoRuQreXGsZcEiJDuu3dym0TF4qTsw_5ESNMnmvYXSoFMZv5haTibtSJ7-Ser16KDS_bvDppUhNWovToMW3qCzwYC5dOYrQ-I8XY9sbqGuR5L9bKv9nDGZ7U1-ZkORZBMSowSX0yGyHDN31iLgU8bcX7HhNHCbHxlBnVq7PY0MK_663n6KlX1taJkKr0WK-ggvZ-98xv42sBU-4ZOS-Fnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3c2975d3.mp4?token=E_0CTGRypleKqo-HQQhYYVd8jI0nBioL1ZsdNpwZIDNfYvUPOMO9r0anOHCktcV0Bj8OcrTkRlPrEylgdxvmIs6xeT2NXbdD2WKKllck5iu0jz7byx8trNmzph-ZLp-xoRuQreXGsZcEiJDuu3dym0TF4qTsw_5ESNMnmvYXSoFMZv5haTibtSJ7-Ser16KDS_bvDppUhNWovToMW3qCzwYC5dOYrQ-I8XY9sbqGuR5L9bKv9nDGZ7U1-ZkORZBMSowSX0yGyHDN31iLgU8bcX7HhNHCbHxlBnVq7PY0MK_663n6KlX1taJkKr0WK-ggvZ-98xv42sBU-4ZOS-Fnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین میزبان زائرین پرشور و عاشق اربعینی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/akhbarefori/676509" target="_blank">📅 00:14 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
