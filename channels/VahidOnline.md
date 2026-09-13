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
<img src="https://cdn1.telesco.pe/file/s_wuApLIuDSksNXU7IrFIBdCP3YKVN4creflSdS0L-Jc-W0bYVa2EVrU7sQLGRekmzw5aQ1fTZ6rhhVA0ucAZ1KjTAmojKqvWGbFgB7HxolbyePvYamydYxtAJQqkfUUfvs07wwv_Y2zB4vCuPJHe9zSm-uTukmh6AnXdINyoPnWzwNg_TvArSH2NFMPOiqzE475HoMuBAjUQWk7EX2spF6CHDVFLr83EW0kYpb5fcIisMJk0wieWDkwWofruPTgjjP0_Rvja-W9pD3UkfY-F7ipGvu6BljyIe3uMpiY93JjjLFHemcBIaWAPBsnIqwDjICOiXYFZ-JP3sSHq_GGbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 03:18:25</div>
<hr>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBE7Ot1KjqvxZoI_iNNC1vmn2-SJ_kMNOI2rl_Et_t-a46q5jWJfSNlfFqU9FZ2uz7eEtPmNY5cx_hM--rSxDEKORbJNbAe3-Soa1oKM2sziz251iisN5tqoO8tqjkx8W2OB6lnAFwjFSCdN2W_basNt15jQb7SkGNi7gOnq78Rn8oSfXChkEtYgRc2Y09KImEJJIU_ouCDN9QKJrssAQ--5gK1fBt-qd5tnskFVFdXRyg0FlE49WWn8VhM-K_9ykpd6U4M5p9s7_uV1cQYNzkW_4ux0S_ycarvjfTLKyxfBolFT8febBVmHsZto2G70U4dOG3vA5kSGmxwHxnz49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZw2Z1yARoD7fzz9rGozbJOjPuQEe124Qs9Pw5brtfx-SOcPLOrowy6xy3TNxnAfTWAlGnEl4h099FjyRvIFs3uljfSQxFX97nOJevaQKjGOLwLBgkcQoAcp_WSAZzEPEVJkwypli9_34r_HYwFFH2165Xz1aCPXYsuo3Vt_H3Ewv_o0ISY67fjhYaQDNXFRKI5_rhue0wYGz1MhoGzkcy7YvnVyh64OYNdXDXRxqXODJteKGDTIz6V7qu_XtqQ1_NDrScKeFRQ8dollKhtFor3vVVCVsGUu9zK7iwvMDwTmsOL5PMKdoL4Jilk2440uIRQMMT7GENzGKkHiWIpxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=AyvWqtRy2z4cHILq5PdKXvRUBjaxHZIRnC0plciUBuTbBxhpByQLXfHz7wfCeAubW3C7-g9cABMLBgXQMNMNLK0tZTCeGOOuC9zjrNXpBqXvN7Kc1I_PG1Tkrx62O8DQGP-EUV_aPGBa4B38BY_YtLeuGvlAc4AvqkJZbJMi4nNz2y6TCV2PnL_qYGilBKsT8tQagtUvbPOMHhdqAoihaT4hcTfl3tv5dx5T3ktzjtSOV3nnl98wPd9o6Cew-q5qnvKlLFc8ZBDm-6ISGSQRFir4r3P4PXo4WmfsonLPcgWxXOafX7WfzWzyiRJJz-lXZ-UFkZt34rdq5R7EcqdmFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=AyvWqtRy2z4cHILq5PdKXvRUBjaxHZIRnC0plciUBuTbBxhpByQLXfHz7wfCeAubW3C7-g9cABMLBgXQMNMNLK0tZTCeGOOuC9zjrNXpBqXvN7Kc1I_PG1Tkrx62O8DQGP-EUV_aPGBa4B38BY_YtLeuGvlAc4AvqkJZbJMi4nNz2y6TCV2PnL_qYGilBKsT8tQagtUvbPOMHhdqAoihaT4hcTfl3tv5dx5T3ktzjtSOV3nnl98wPd9o6Cew-q5qnvKlLFc8ZBDm-6ISGSQRFir4r3P4PXo4WmfsonLPcgWxXOafX7WfzWzyiRJJz-lXZ-UFkZt34rdq5R7EcqdmFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWMT8plSOBwBz2Ifgr13bOLljKMIStkXbh4um6oZQ2Imk0UxsDPEFWvJDEwBcfTuGesWplwk8k0nszzQGyaFbjE2PLgds2JTOSYWt4s0fh7b3uL2cfpN7RWNh7ioAdMO_-TGo2yb_xcrp9_X2mgdAJ3YEmMb8xLX8Td0oFzZjt11UC0Y08KuCURuqK9NaqQ9sDwpRLuPkx4DJSg7TpwjNK0EfNWefH4QTi53ENXd0G9VjmeoV0fcFdo3X5hvOWG6lZgvAl5gFQmLyWaoziVUcNII9RfCKIhmgPKaNf1fX6AF8_yOrALijoHIbV5CwMnSuhVNS8L_o8B1h-7vieetTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eAvyHzX7gIwYQRi80l2u_mWRIPlXwDiJ7WUhpeU-NqzPdiO5j0Gr14pX7VbibYAB1Ny_CvKEYWvgGeaPicn-HoLiGnfOfBASwotMdaIR_lA8ULtiogAh8xCqs5Z8bP29d6itdPOdWCJPXd7y1d1F4mFZzgOxzl6eqNjPDtJJR-NRXy8aaNc8FnIW7TOqvZLqRKAM6LlnweGiMxv6XoNNYXd_5sah2ssXMoAcxRI4y_BlHeJqpnWbUb6uXurVrQ3Hph3GtI3RPbu_freKS5E3P6LYwUlhWo2YYfnIXXkf6Aj8zns9Y0o-8LEC3Zsdg3raeQ-lZ94GZaHo1SIM33srug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GT1jozL6bq05-y-YMnItEET2ou2vP0U3Fa6a1M2S8CYc3ja6hWMO2fCzB7fVbhu6KXJ8jkTSNcnd5Egw_FHQ0W2y41BVduoMoXhkLNA2-OxxxEeAHecDEXJ1AJHPbgDEYk-AdIgBxDj0NRpE35KwFoZgl5ZT1ULEsP-5GREuAUx_nE6HiG7w3GQUUy--dgAVFPzZb7E_8tamghhvUEqie2sjwJ7KKKfGceqa3mC3P1iWcTNNsHpxFWEiuZDt3uiC7c2QaSMEm6BJwYp-rJCDVVZ_vJPAwIzkZyYOJZi4s_nGa96qHHksAspMq2CwvwmvaSxRFNZevG9JJmYzvyFsQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PUfGMuRoZXkr7NF_37L2Tv0M5PHDp7cIYpxRHLMX80xehi8zjyLzyyvUZypGKgy_baSQJtcQxACqhmwx-kZmNitow7RA4c-l_TQiy_hpiyHQHMRtb_2roARmBe0pW2swuXAQ4CHEqSEx0k7drEXcS5RaJjxH69NzOFH-EkuIjrHRAywIZ95G7iQgkjuKL5LCxVmhY1VRIcERlKHIHLLuOnQ2Y51rOjWBgfN8MsWfqMJGKrk-L8jbZuRhqoa7vD3nRfhdUzTET57jGK4w1xbCjEzmupVe-8E2XOZ3nHhFL88PindQximfus1A6GfSIgBCz_bJnR9NBK_jtdJRl09JcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kgj3WpGSW5UXqnrHXFdoM8vujH-UlYzHDb3bYLP2mWRZLTgn3YwdMZsCZgHjs60_3kAYxp36U4fPUDJ-ZBIo8CXRoTPQysZlgx9R69MGwIiK2ficc_QDoU-wzXhSzJoNBGRagV0hMlLqKWVUe1cH5zn5Xookg-ukGGCG9K7bxx9bw2rUaRH_huuMAqRmycoQ2TWPHrz8SQY4WCyN7WF5ljH7hg22EV2r8_FVednk8cBavlXm0UuvBcJuOLbCQEfukavcKCsuctNVV6FEhoo-fyu9ZtB47qtsiqzLyJuCNcqDzcE6D9hSU5XVWcXzHHjEcnn1yj9E0C3lc1cLFQIrSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nPZiAFrLOB7Qfzxf80LAUc0kSi8QlLJsOiDXKuf_Kqjrlr_ify4XLMjKzqgXCMDiMR29gb-yA-BAi3o65vKcyPPLWlG3DQxVIAGHGzRyuCI1zU-eB_aj794vDojAWZI1uNdsYciN4XR6adBMWEGziN8JaCXk3XhP1rHCWvEFUk0I242E2y12w-vfGF_WOJAr7eWaanHFNkZPUwGYsrYHIKsv6sWVXhrZ2aGzT-bCHkQ3zOHEbqX_Ucip34YHFr1ilKNeQQcmTh6xmkqPTU7kWfeGek_8stqS4OAfjWB7PpqBI-0Yn7jOTT8SluvAu8FSHi4DvkTJydhINvSjJyXtNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=n6D7JRvrK_1DBzrydHYSX-RJAGtoAwG5b-7yFnMISzLty1Jjbl6pishSCl0Uj2MDnkrprKQpON2yQS4-laR4vrM2SIRGphbJWI7svgw37KDz-FD5TkDrsHQ5udVJectNgGs3HCoOPfuCwV1DL4ERUr2Iaq3SA-33i1F3viVVP6N7VAEjKQTFe5eXiumI60c_j7K5AswlDQKvxzkll80lZkgX8CryTh3smMn9g_HjNWauP5X2RM1x0uqXm6_0Ijeu1o9PrbKDwvfMq4WPy8Mm59yYkvPZ46qh_J4NDyY-IxzznSFpJr5xyWEcNwI5jgZ6cbcN70XUAcl7ppL97voU14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=n6D7JRvrK_1DBzrydHYSX-RJAGtoAwG5b-7yFnMISzLty1Jjbl6pishSCl0Uj2MDnkrprKQpON2yQS4-laR4vrM2SIRGphbJWI7svgw37KDz-FD5TkDrsHQ5udVJectNgGs3HCoOPfuCwV1DL4ERUr2Iaq3SA-33i1F3viVVP6N7VAEjKQTFe5eXiumI60c_j7K5AswlDQKvxzkll80lZkgX8CryTh3smMn9g_HjNWauP5X2RM1x0uqXm6_0Ijeu1o9PrbKDwvfMq4WPy8Mm59yYkvPZ46qh_J4NDyY-IxzznSFpJr5xyWEcNwI5jgZ6cbcN70XUAcl7ppL97voU14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=YNQKZXGFdPZV3ZMJxmJuN3yWr5Zc-Ze400gXDwHvawNVhD37YxIJUsDefEwCSfvfwWJq8K_TpnXiyenhrL4PjRDEC62_WqPP0is5r98-2cUJ3bnzaoRHYwZXOcJeLIPjz22lyKlz9spZ8T_09nUdMqGt7q__KSVwZhIZkywcaKYFz2nKwPw3RRJ9pEyRNZLKIzxOiWOlrGu9aSRXAKhNlhdzs3G-HfiZ0VM4r1a5bTic9eijjg2WKY_zzPFQBVM0EqZpkmIu_CLYLl02Rlfxgu75swr-imG5ZmyeLbE-HNy-ZYuNuphl6gS7GBFTBAO1Pq0djDHwXiyHbFsNKNEGzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=YNQKZXGFdPZV3ZMJxmJuN3yWr5Zc-Ze400gXDwHvawNVhD37YxIJUsDefEwCSfvfwWJq8K_TpnXiyenhrL4PjRDEC62_WqPP0is5r98-2cUJ3bnzaoRHYwZXOcJeLIPjz22lyKlz9spZ8T_09nUdMqGt7q__KSVwZhIZkywcaKYFz2nKwPw3RRJ9pEyRNZLKIzxOiWOlrGu9aSRXAKhNlhdzs3G-HfiZ0VM4r1a5bTic9eijjg2WKY_zzPFQBVM0EqZpkmIu_CLYLl02Rlfxgu75swr-imG5ZmyeLbE-HNy-ZYuNuphl6gS7GBFTBAO1Pq0djDHwXiyHbFsNKNEGzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZDtxkdnLfFX_mvR-ahq8YXKpdAFrTfyZPsIWbt9kP3TZuHzkEqey0BQbSf8gEmbtZV-LVfHtl-2PS6fVgCQBTa9LScjeCzmB5pqaeiM8MhqX4mLrn-pkxr0Q4WREfz-Rp8ZAuyy3PV-4XInnkdHqtd2mWvX2qFZcFsd7zE3tQj4LeqivDVFShXif9qwIH80K4CO1WdG0vaRgnkrgKqjStOxal9bip9Qpxn36Y1jNtDmeBJbJ7EfpEGqGHBvjVu09IFduxz7o3Dp_lMq4rU3zl8fRgFLO_EKfkbhEyA_o024PJyNbd_hm2qt4GdETBv6mpJU6DUtGZQpnSB8EhsXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfCigAYjEPWeKd81EZDb7SivSCOHymbVPvTEC5Y8VtrAM-3LLOJUjePuphGszwb5TvMMTA0UEjfLMa6DWFBxBwhF1x7omIWigXkoDwctzE-Dyx3sjdKDDy9g8IkxY_wYaeAk2lS6xgDpbuVH0B60KtskEF_VFmjtPAbj1lIC_KB9t5Ty6E2PdhDehU0AlVgI33VlgPfB_Mg-aGAplFljLAhk3_GNp_GP4OCxO3nIT0YbHxd8ieal6erDqVtL7TRir-EhcO2dCYogthAKMEHPDNL8Ye-biRPMkASHiPEICeGk0W5AYIyHDNqo_vwoWs0H0-exikF9klHGCB6vziD38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syGTsGn2F7b6vJWWpcajQhwvY0i9twKN_TBHFf_chgZyrpL5tW_4rdmNNpPJspl_fThT6YOb50C-S93u-H8ldpMY8OU0_ctvbIHQFtS4NGRC2NwymJiK80yBrLXYNAglpfbXlvM7A-46PYonMkj8PBYhh6OwTvVCtWVYi1gxrqZ_YrLiyk72e31aMVE6r_JAvlnlDRAa8CDxP_1aim3ivaOxG2eKXRe_0pJSZBUmtJUl_pUBoSPA1_pwdCmsTOJhcq2HQ4x7Q69bP8xWcnrL3eYzvADag6A2Nb9MR1oqFeLl7ltjwJwJ8xiNCRDeW8najQswNuUDtlbOjx24-1-gag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=tizySJOGEd7uDPuK2pSzJRTZPLn2C6NMeIyr48d8Ti6-3K-bckotJwybdRDz5zC8Wza24tVy2YYOJd_39Ijb1TMeF0dhBpCzG_5QMeYtX9b3O-PoJM0ysAi7qzN3H4I62GSRs_txFkWRWKgJ-6JtwJ-wq6Et74wJpWYszyF9BQpWxrG-_znz3x71aoNnEV2lAyDJbHpuXLv1PqMmcOBT2lOTsExeGUlDX6x7NlRu6YegZevjku74I1o3GvSg3klCirei5SZEKCy52TexZrMg-7oy9VRXIZFuUhXF-XJiP9WYkD4Dygid7w32K1xjKKeRJC8P7emjI7hO0j4IqiHnLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=tizySJOGEd7uDPuK2pSzJRTZPLn2C6NMeIyr48d8Ti6-3K-bckotJwybdRDz5zC8Wza24tVy2YYOJd_39Ijb1TMeF0dhBpCzG_5QMeYtX9b3O-PoJM0ysAi7qzN3H4I62GSRs_txFkWRWKgJ-6JtwJ-wq6Et74wJpWYszyF9BQpWxrG-_znz3x71aoNnEV2lAyDJbHpuXLv1PqMmcOBT2lOTsExeGUlDX6x7NlRu6YegZevjku74I1o3GvSg3klCirei5SZEKCy52TexZrMg-7oy9VRXIZFuUhXF-XJiP9WYkD4Dygid7w32K1xjKKeRJC8P7emjI7hO0j4IqiHnLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abkLNDnawJVPDu-XKn6H6EdRjgHBlDoIcwKb6Q9Ca8w7VO-V6pOtxlpQN_O3bBuAqnYHZtCPYWdwlIQv7T1rGsyq_2As3nVpfQRaXh7t3f8GpC8Er5cAQ25lVNOmIgjt458VVLgqsb7XTkhDE92j6eripHfNg_a3hNbZ5b5PQhrqv6KaZMzfsniKByWjhr8SS8DqMLJDPFEnSQXqHu7BxcHMTgPtTGzy4_A6-Wv4n3RAXeYvP5e5Eqs-ybawRq99rO8njetvw1_jE0sPCClyMPnauFt2zKS8Rav-FUa0YNaWebKkO9uUVYqnQKd4MxYbJVw2jvbaR1PQi1X9F15ZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=qVkgYOjkPxUqBcHSaLfMK-6UyIitv1lF3dq7CcbHRGjZHHtqo27a0lHfRlIJ-Q0jVLViALMLGtTw0szTH7ZwA9blTRmpA-5aq-mWaC8p6aL_cq9vMYOMSWISphZvtmLufFQqQFBl4RqsfwKMLEYDbY5HHXUH4G7zwDf5gagUSxDsN-5ojaIP-kPN_zNBJNODorjyGkPX-Y7uJQ0d74auWAy5tvtZqUYgQIUGbyT9QkSLD7nxrE8bx0edupUPDtACwidU2eft6pUsljR8sZgqdMVKOhQmLiv81qgCvB4jbNAq8NdCuGc5RcX3e-teDvluczkfdC5l74Tjixw9aLpqjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=qVkgYOjkPxUqBcHSaLfMK-6UyIitv1lF3dq7CcbHRGjZHHtqo27a0lHfRlIJ-Q0jVLViALMLGtTw0szTH7ZwA9blTRmpA-5aq-mWaC8p6aL_cq9vMYOMSWISphZvtmLufFQqQFBl4RqsfwKMLEYDbY5HHXUH4G7zwDf5gagUSxDsN-5ojaIP-kPN_zNBJNODorjyGkPX-Y7uJQ0d74auWAy5tvtZqUYgQIUGbyT9QkSLD7nxrE8bx0edupUPDtACwidU2eft6pUsljR8sZgqdMVKOhQmLiv81qgCvB4jbNAq8NdCuGc5RcX3e-teDvluczkfdC5l74Tjixw9aLpqjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtWQS4ovRZPuY8K9b3sbdTM18pG32EUNbewvaAz5LhKFIZSXP2FRjSBlDnZb5KrKaoFQpbYIJ09PBj7mM3ZRpxXVMBsobNA-GGpm8MV5m9KjGz1OVFdNm8fZ_YN2V2SLH0E609Bcs6Q1UvvGlMuws8XjhOcFdwIuoJ7QmxMQ0b7NmwvfVqbQKzxUQiEShf-20_fUdpVZG3Cy7DOrxYieqQ-0B4z-2-bukqmPo-vPsJnUOkuJ6bSiu0ZXA65eCHtyZEE-yd8DufF0Kya_3XVDOXzBZAj7ovUnTT12PM5wXErKbRI2af9blAGi1_30C0RZlOcUNmE6KI7Ot1rzPC9n-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/euNj5LbUW8NS8vYnhlZPe0KsiB0NPOEmn4Gl65RqNnSGM1VZktKiTK7dtO-Beg_vOvv2N6CGLZSkKP_kwgYCWoE6gS2709Fntb0RnAj0Aedokbl6_qOJ7ty9j-aHjGPNpLoxsBqqAmatucKWqltDMC1-_gg-zEJaha81BjpmE71uKe9sCMlqQS3cZZwLiynZtw_6uhj-TVqsHmrzHMZZ4czHpLk2NJd1wo9Gt5bJMwotE9OxdKgnCkVuvaTfBSaejW60J6eq8xiviu59omLCVPHbmitlxH8C5EqLBoYLu4WYOA_ENANLedJHVKMgE-tsKmi70v9Fe4daQQScTQExlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NEY5lAuXcpwQ08GgxIs5_dLgxaHjK8Y3Nsc8vcoVEBC75s3DazGUkODzunWF9rsf7mdHI76un5fB336hQKTmdlSADh6Oz2UwMXm7uT3m-OhNjcvuz6ybZepU3RP3zfLX4Wzjj00Yr4xXNd_DLWJ21UQdFwRWwkLq2JZ7FugzZxDdwKDTy2o0ZJJRZ-MSZ3J4kGs-05Y2Nm0w0ArAxtJkui07KPbKoPDD8vYKkcewm3gROCCLwI3zz43BOFdOyhKas_BqZ6HC2ns5aTI77TGaQqeZAtRT7jW8YtZ2K06Z_WHNKZTF3NqXsDv5WWotfo6yEKcCXjIRm1iFCl485ujZwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/StBL0RXYBedEv45qAm42h7txGsF_Gtw9SUzPrnhRVYNcd7hnhdfY_hAZyH9GrgDXugWWHzTpbXhqvWUv2DY_jZdivSGIOE1B6-Ob_H_H0_6UCozMf407WwgVFg6Rhwy-vUZ8W3wf1uVsSCZf4L1MLhn9tmV4BKwHbwWmZhK7b2RM0tgrltGZlxi9jDN-WL_uz-DLuXSIAIEZDNXoqa8IF9FH19L_3rG3D8QMKzDtBMnQOrNhER9PdbelUGuR7_Iq0tvi2qpfa6FVoV-UEDr2m9KQmJrbYUyDLHrOrLKd_ciooBxc5wskKzh7MKjRP5Xn0Qk6sXWINMo5yArpI3XuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bjg7_qm6Q9aqrydPoqXmLYBCYY9q1qBJccEkXY8yhIbpHKgJzDgTvHGzvxgeE9dTjcS-ZkaIhlh1-MOpTxhYApZ_O-a-DcMxaN6F3dbWP_KwrBy65EnNv3EaNulAH1jCpwA1kMOwo4dr1yurlBEpzymegFaNh8Zjp_-3nvMHuWAyxpdJnhdGUyxitVaUPxc7MVJj8q56tgDxOxNAu4nwSOCKfSt7e_FTz-VC3PHvUMQSlClz2CAgrN1YkdEqUJzYTc38TgRx6t43ocY9Cz1Rl0W0n3XTY7VTMdnKHSMtvuVMCJXmYhzToUD1S5tYVU5a9uGNQ5SA4qL4c_6dkCdi4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xp-nRumxB2Sl6Kxliz7m32gzZeVULXK_r86AEDzHNk5oRg2vog-ukuY1xkpu7nu16dvSswFUflHerv-YHJRUvwVcDpqBobLECY8--DngI1r4QRjKz0hMSQSwZlzP8QLkZaeikvcz6Yf7H82A4U5TREjIZ7Sw0KBMvUbNP183sIAfeO8mk2uOFqvc1S_rqPsVg5hPFMDAUTtgEK17xtUiMq45Gu1aU7MExP_ZZezy_mwyt6oLxhlsg1rYBmCSZFS0VI6ri6LEopyfuIC2eghDtHrCadbOqHXHPo24CnSWzbsww1HSCNTPIfjR5GPrUUlXQCeGgRnVa0sl3ZeQLJfU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aQ9TyFF2vTlaYoY5KMvPL7ecRWTRcQyR_uwQa23z7cb2Gzixknocv2Id7SbcowwXGxY5eLpooauS1fAi1V7Z-rJsa4V2GyrTq9C3qF22Suy5I7X-NA89eRWERKoJLD73g7ZimcfSA0Q9pQpCzv68_UYGV1Sp3X_-6JRmLMdpMPCRLDjqflfn2q-GUykDyRnKyfYy-erGEBiPBvbApXNzTM5Hh4cy5nXURJx4rU6m1W8kjKb-LcTAreHiq3EqyhRDd5kE3bG8JD-bFRQGbYCxzaQfUDbI0CTZa_vK14FQ8psoaX3fDOM1KbfYtLD8M1McB51U05GBaTXcKTSLAHT4LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIfAaCeI9-6XdWlqNnwUlcIBsCBxRAaidjdZCFrSj6IlsAMZwFSOC0crgNdxvwCJWNz5121WjyZHxtbU2dsPZAe3gythszWzgEMIHZKg4oj5l2NlnPIHRkhHfiXQCu1NCYtNjjWjqTAYNWn7Qf7lXj8DX9a2K8Cgi6cw2dvYDq8QoJrWN80XRQaJfaKGpqZ5vxXyzweJiyso1J0uEksSeIJZh5-cSrP80PVvJyizY7qkRw1KaGkfDRtP9QqxhypGdMsbjlcJw60EJbcxajucYgQJrmqkZSEoN84KkGVjVE-BreyStVZ2cusQ4rLm2sMNvE94X_wgw05q1hTBrMeCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=onn0lZiaMKbG0JQugndGJn-XjdlTT768KKXTq9LOo0n7XVDlHZkkGrNH5TiK0bF_p4qwEBG2vE3ZXJNb0bdd5slgAUoKhhb3f2YLnRW1rtLKEmDsb7hou4jhkYtl0axKKWj4FgVF9OK6V4gka0zremGqsiCvM57oH2BGqmOeJ8eLZpAIOBzZcleJdpGFe0QW6bMoanJUXO20speYJsNyCF8FQk_mNGLHxV4UTdtkCiAFrLyjtAvEgsl8DeHMZeZY2XjxOZjLml09vJGhScuQpdMhc4QGcetose4ki5HEdjchQondvbRaBPUSolX-8XtLv88XUoz3czHM-L-eyTw1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=onn0lZiaMKbG0JQugndGJn-XjdlTT768KKXTq9LOo0n7XVDlHZkkGrNH5TiK0bF_p4qwEBG2vE3ZXJNb0bdd5slgAUoKhhb3f2YLnRW1rtLKEmDsb7hou4jhkYtl0axKKWj4FgVF9OK6V4gka0zremGqsiCvM57oH2BGqmOeJ8eLZpAIOBzZcleJdpGFe0QW6bMoanJUXO20speYJsNyCF8FQk_mNGLHxV4UTdtkCiAFrLyjtAvEgsl8DeHMZeZY2XjxOZjLml09vJGhScuQpdMhc4QGcetose4ki5HEdjchQondvbRaBPUSolX-8XtLv88XUoz3czHM-L-eyTw1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=PrbMATjp3NDUgTmdLH5WnpJkLmbRtYz_4YcuDUXsfyi3iw-MrMAEesdotCaJehW_aLYb0pSz1XtA_6-e3lWTIJ9y8Y3ff5bwDCev_ulABp8nw05fPb8WnAenPnJZ-nZ7parlkjSxQU1rRSsrBqV9KAspaDcSOgyy0kiqYwYFOx5dyr0ty47kyHKyK_sGrqw4Q3CIrAX0ZmeU5yk1-JgcFCY1CZiMODkyayBEdqmirbS3ARP-YDrhH8RedzmxN7LMH3ntAm6KMXuqTg6pDbRcxKrsKgqW9HBSb4u06s7z_62AlmGMxUImwgc_CvdSjow3_WK9-enG_0iSGvZG9s6W1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=PrbMATjp3NDUgTmdLH5WnpJkLmbRtYz_4YcuDUXsfyi3iw-MrMAEesdotCaJehW_aLYb0pSz1XtA_6-e3lWTIJ9y8Y3ff5bwDCev_ulABp8nw05fPb8WnAenPnJZ-nZ7parlkjSxQU1rRSsrBqV9KAspaDcSOgyy0kiqYwYFOx5dyr0ty47kyHKyK_sGrqw4Q3CIrAX0ZmeU5yk1-JgcFCY1CZiMODkyayBEdqmirbS3ARP-YDrhH8RedzmxN7LMH3ntAm6KMXuqTg6pDbRcxKrsKgqW9HBSb4u06s7z_62AlmGMxUImwgc_CvdSjow3_WK9-enG_0iSGvZG9s6W1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE32_hS75MnzO8i3OPAr_1rfGWDe39PgfOhJyryOTK23AQ_HK_i6uxLYNbP9WlNowbFTDCbcJ0sz8spAcE0LKvHLg0isusLibMWLJEDZTt2BuT21L8DzqiIKpcSjo6MSQ6xGeEhxt4u5ljhAXVimXwXZ6xUdOdRh6z6kkLp4AWaxpLCWkHZdYh-Tj2WSybb5sU6LgdwejoI4XqboKI0G7WbdLrRl-c3IFESqstTcT2fKVlBRXrltXgcj7pS9wu08nxmOSqTD1JyxldctIUpXUOaBtXUfMXBZ8MC4KiXeog6uu_XGYIdl7wuGdwj57J8m_6E7cQiOlwh_AOs3xKZ8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/htYvJLPrNi6YrpDoiRamsmB-jPL6kLHOCOP-GR1xRYzGLurWDdz93oj_eP0pY432tE6Z7tZ13rZSkZpCtJoCPN-6tCauxL44_2k7DgMccCk82jKuvTLw81AJDUu1HacW4RRiR7QQgFCCVl0ty-UX2fan8MfGFTe5In7YMo8Yke9HIJgP3uzvQEuFVrYNeAYb-u70nf1r60YcDl4L8EjKrbT52jQbr6ZNtXhtzh2G5JLv4ZF525SH_przUWRds0o0UxjaEpvoeiKl5JsBsFQV0NqaGouDuEDNZ6lEL275pmsA7DWm97P5nyE7-vYEJIjFeJLE_gRja4q1ZQOY9r4Ypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeSNWwLE24T-Jm1yrgqClUf2rvLHGEs_IF_0qGZ49UKuE_haLiMqTh267Lzva7hWShnMrN0Jvsx6MNBxKogYrMqlA4Ee7kjx8ymAObWWvbF5u-Twyt3yGF3voi7hjLOBMEA5f12lECJSH1Q97wrs5e5lBDjyL5FOGW1vu6VzqHMyHL2AE792Zbeob2aWE4VjCqQQryusnxmdtR_0UDmBSL853JQ58bC8XojV4UGNlhPPnLkLV6S3do498w9amQ-FstbhMRqNjbreaG6cpTNpx4DrLYvE1mSvtpDfOFVt1hK-XpLcEjSYElpEzyvrEFf3npKY02sdZD_U-wuQRpjXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=qWaBGbMBA7cbpupxCooABDl4wZV6ZasOZrqNSZViXAP2gSbpPPgf9Bf0W7EY2xIrKEQlk8SbnoVPJFpL8VGAqXA_Q7j5zKEyETnW-Flu818NCMwC1fVdIywYLOhMQM75fomLzXpdZWg0buEeiXa8ewY-Y1lUzJkfGgntdpHRB_hX3azIcdcp6H6-gNFoEzCDTTfWe9tRD-Elyy-ZbMUOTs2IzfwUmt2HW8G_5EmmcVIw_varHSozAplzGXlJUuQUTmJbtk4et5HKbXly7Rcjj2DqYKtvH8wCKx6hF6E_lQ1-Xq_e232UttfOlASQPdNS0Z8UJCr1K9NdpVrte2SXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=qWaBGbMBA7cbpupxCooABDl4wZV6ZasOZrqNSZViXAP2gSbpPPgf9Bf0W7EY2xIrKEQlk8SbnoVPJFpL8VGAqXA_Q7j5zKEyETnW-Flu818NCMwC1fVdIywYLOhMQM75fomLzXpdZWg0buEeiXa8ewY-Y1lUzJkfGgntdpHRB_hX3azIcdcp6H6-gNFoEzCDTTfWe9tRD-Elyy-ZbMUOTs2IzfwUmt2HW8G_5EmmcVIw_varHSozAplzGXlJUuQUTmJbtk4et5HKbXly7Rcjj2DqYKtvH8wCKx6hF6E_lQ1-Xq_e232UttfOlASQPdNS0Z8UJCr1K9NdpVrte2SXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmgT6e-MmDzvTwAi_6S5IOqdJo9K5eAMYlN1u4VFh2jtZyUidnDt_-k2QHm18GR-41MNrZc-mLKeS5F7o5ICjxo0FpsS9ikNBnhnGGiX_hIMC5Kx6fUbhxds8PKrbRCjfPvHm3Tc3kdRwqy77g2tnwLboApkzovFiD-9gkd9qyzIw-LT9-qSj6sPWpNMN5H5vdzTvGykfLkkIi0Ti0L5mTeed6b7jwJNGVwS3Y4zaOTFOJDphhh3S8KkZAVKpj-EDMgC6n4cGnYjhr1H9S3FhVyRuvW5v90lcLOH6NKM7Zkx57W_UfJZ4mJhUhqZk7cKEJqtS2Whs3utjB2h_iVojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wih43peQInaaFxyGAQD0g5L2Y3WnqFo3vHZk-xQ1qD218i5ud-CLR3FMc1K9lbUmfoK9-xBLZ5bmKJudDjWEyB7MNsbynwIVuRzpLbFIgPqXQ4-uOiUOKqFqeYAIGjbgUZ0xSqQmrsl9zZA5VsVnJDKGTrEbmEM_GBsmmBwLa1FEaAxY73l8pslUqZByBrtcP9srQQ-10RZRPeCVLEIMFwia6DE1iQFdak--1N4YEju2RNgewaOecCovwUCPsNYjRXyl76bmHCA9CKbTw-zUEgOBlJuIHlOozPQbzusg-Ra0xjpnu9PUFDS721QJN7j7vvzQAQ68KpfhZJ3ddoIVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrmVDG2xP6re1qMdVll95-vOwajr5euaTE6c0fabCBXTq3HBlzQ2jR_vVNQu7lnqcwDYH-Z00OUPVDmJ2CudoMpgySZniGaZWhJcQmKAkpD55EBcyUDZdVbxCMln9ssSbJxeqt9qvWHQulIo8sCHDMz5I-k-Jo__OyHxl2zQQI4_GCoQplojJDK7YP4UJB-sUTUMIdUtgAjrbTY5KfhTuU5t4GNcSAaQA4hGehh2_SojERumWPBEWqsNG3DHFyCvqlY02JOMGWfyXlPETdITfRvt6K1u8nVMYW2w3CAs1kNtvVU29ovYcpSbq1Vo3aWwbsaYrkODqnj9gAEewwnD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=t-pl3KXh5eXgZwHr1MLIevYqzojP2DTjs0KV-APzpYqr3xdjIf11xTbAzCmGVVPucMd2QXZj9YZZEOc6qdUyrLtYgUaE-OTdz5OUpZ0NGQC6mDY5bnTHdJEP0HSyAM0CHrA3krTGW3WPw6CpDk1Q2Kur0NKuxLtjx7FuVkkSpkYLN3D7PhHHvW2uCZv4jDywy4Jz7KCRXitxVR97yQpOvq8rDXBbmKeR4y-AiKpmbRcnW6WkSQHzCdLqdazrtv7h7iLWti6NDH-YDjqNCb1VChrCxd4C_wbPlD9fcOtWNmKFszpksFP7riHvi9q2s9kAodXdxlJv_5k6w82A8AJqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=t-pl3KXh5eXgZwHr1MLIevYqzojP2DTjs0KV-APzpYqr3xdjIf11xTbAzCmGVVPucMd2QXZj9YZZEOc6qdUyrLtYgUaE-OTdz5OUpZ0NGQC6mDY5bnTHdJEP0HSyAM0CHrA3krTGW3WPw6CpDk1Q2Kur0NKuxLtjx7FuVkkSpkYLN3D7PhHHvW2uCZv4jDywy4Jz7KCRXitxVR97yQpOvq8rDXBbmKeR4y-AiKpmbRcnW6WkSQHzCdLqdazrtv7h7iLWti6NDH-YDjqNCb1VChrCxd4C_wbPlD9fcOtWNmKFszpksFP7riHvi9q2s9kAodXdxlJv_5k6w82A8AJqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی در شبکه اجتماعی ایکس نوشت
:
امشب بزرگ‌ترین پایگاه ایران در خارج از ایران، یعنی تونل‌های علی‌الطاهر در لبنان را نابود کردیم. در حال تکمیل مأموریت هستیم. سال نو مبارک!
پیش‌تر ارتش اسرائیل اعلام کرد شبکه تونلی حزب‌الله در ارتفاعات علی‌الطاهر را با استفاده از بیش از هزار و ۱۰۰ تن مواد منفجره تخریب کرده است.
به گفته ارتش، در این تونل‌ها که طول آن‌ها بیش از دو کیلومتر اعلام شده، ده‌ها موشک، راکت، پهپاد، سلاح‌های سبک، موشک‌های ضدزره، صدها مین و مقادیر زیادی مواد منفجره کشف شده است.
بر اساس اعلام ارتش اسرائیل، با انهدام این سایت، عملیات تخریب شبکه‌ای متشکل از هشت تونل به طول مجموع ۵٫۴ کیلومتر در منطقه علی‌الطاهر و قلعه شقیف تکمیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ml5kdgr5KvBTf8zme42EJb-LqzSaVQNA2FaeA1y5AEIrsAmzNlUtbonXveCAHGdbKX3jfCEOK0IHVaM6xF3iH7ekxpni1yngOLXn0ukRUC2SbGZaOTXmNe0JbIfGh_-HqR8isunVQpuBkT4nKaRjwDz7VNBJ6hBkHnmq_E3LGI9h1zKf2HTo8ydUJi18g-HqxZCnWk8gNOBO9FwKNpGRURwbCjKND8mfoxvUtQ73pwZiGYZrJs6i8S1HIfrM64xRmNVQEJIEpZWjWUOiS99mAWJTUjU5RfI5PjY5Tae9Duc1FQ1hHEF88hTYdjJ7m7Qb8wKEq9pDdZiwPIq08s37gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=uatCVv4R5wngSlFg-xWPd1rQ4NuToqnrC1dFnSN5p9AKbGfQP8q1f2ROkz_kGPzio5SnxFRhCypEIcWUi0w-QCJnx46XwIJsIQtiheSxj4aNfYz_lABH3CklIrNJi5GVb9dPb59QUUy8-gFa_KqvAiF_v_zKKeNmfikRKyfz2pn647bdU7cDHCydYH7j-6jDdLTuETfzjF5_wcWPrxB4oXW8aBS04KvTbRbUl1KbwH5Jd9nhyn9ySmU0YKUEkpmCGaAiRLYEtGYbCC4ydpL69Jmo6x0tFYpZvkQ6zKNXZE7bqE1rBWuKpc40t45SNXmDHpb2ziYFU61tvSkOrAd6NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=uatCVv4R5wngSlFg-xWPd1rQ4NuToqnrC1dFnSN5p9AKbGfQP8q1f2ROkz_kGPzio5SnxFRhCypEIcWUi0w-QCJnx46XwIJsIQtiheSxj4aNfYz_lABH3CklIrNJi5GVb9dPb59QUUy8-gFa_KqvAiF_v_zKKeNmfikRKyfz2pn647bdU7cDHCydYH7j-6jDdLTuETfzjF5_wcWPrxB4oXW8aBS04KvTbRbUl1KbwH5Jd9nhyn9ySmU0YKUEkpmCGaAiRLYEtGYbCC4ydpL69Jmo6x0tFYpZvkQ6zKNXZE7bqE1rBWuKpc40t45SNXmDHpb2ziYFU61tvSkOrAd6NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Muq2_pfMmrFKyjEV_oTeNjECy4phsc9kbdeOBJ0GBLztS3lwUdfTJqLByBba8AJ0w1nuLv-RoKkM55l4i867DhA5v3uPv7g8YEkaAoOzkVNc1jjkHO0s_cpHYTtJutrQJmJ-dJKhJQSHfcdfhl05oEaFA4L8hPEgO84xQ_6u5gnOaLU5oAzGMHRNudYj_7OALl7iEL_ueoFVdj8WpwrHuGvOrDqW2-k0cCiGLQ96z9U3paN_mN4mDpKYJN8Nz_uuJN0Vw0y3G33vWQ7XRMmhNwhsYphl2UkP0PTuIypzKbUhKMDAn-4eY37pGlYviV5wp74BMNMtcDo8BXKNjAWCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLxYVYYQ832psX6bVZ4qvgIeMUgZkOLKywx-HQVCFargSOh4rrklYWumKardz7NSQo5UHA6pdZRO_3cNWK3O5E6PElGcZOk2tx3aDt3goM0QQ-sAtrXmz4lTATPbP4MVkbXbUQUtTPji5Sck-g_dLBRP0eIfiphRNpQ9H6ZLVYd294S5AIwKFNpNAe9uw31xyQzWUgAMRKfd7rmRv74g-I33dMWTEX6d0Ey2SNefbJOShvaeiP75BhPN9NDHZyYviyRL0Z3Te7G8OD0t8d06DMerE1Ah9F6zEfWaKUZXmWEWKheY8e0_yNC-Mq2Pq7oo9VFJNrSFCymqBo20rVcIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7Ack5N5FG5Mm6BP3uAwsvF-RmMJ8zyj0HcEKEkmK32qRZhONHsJZMTMaqWbTpoQZCOumphdeBur6Vli7Jq5n-v0SXPayftXL8AZ3YI43EPcn3ybaBdRKWaB_PD9rDSwZxUGsCK8TBhSaXhH2Yqg559z-SXEx1fEQ1JE9NcQBBXQQVh1P62roW4C9thQSJkK-84puoyG03HUIbC1M-FvlPQrLhvXXhtsKMKySRbe5zKmKNNp7IMgwX8cZZ707Hyfd84RMlDS81cDLOhALsF9axv7CEQXAFpFeDcMMDRnEFBxo12evl9Q8Q1OREhOCTFb6ZDEKjF7p-NktqC_nlkXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d_vc_K0CcrrRGmsldJ_sqfYR1NFVVQE881iljicGGsii9zIx8Lrv42mZN8y0OASi3CuLkNnB1XsjPtISp1IyMFc8mBXBTsa967eueoTMLDSE0Cj_GOfqf9E12udC_cdMjxuNNzwiT_un0tsJZixW76a-Hn9TetczDdX71LocTvMucEIUGtXY_8_EDmVghWxNBZzPFQCjlUGXUwNduQczuxIymRTyeWE9-pX7EeOHr0UP1wvjy2nh-K_7JiI5xGC4wsVsuQ5tqD7_pqAewOp_QYw8ZsBes921sWlBCAAEs4DCoXIbWL-nUWssK9PxjCDNQAtcdRp3UyJeRsvEvdj9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CpK3A7mBYg1WqO6c7unTcEf56hldMkPvsp6ZXdu5t2TaXcn-LiAtarAOo09__thA9X0XYxx6czwckx0BO6bUy4pTZ7wfNO-D61XKHt-afH3VypmDM8db9NE3QgBv4UMW9KCkQeVMEoqvY3OTxaivwsev5CQW1a4Opfoq0eYGc1FR6vdP5xA50qHO2Sod1sVVt0oWDlbK8IICk1TUkW2sps8pq3tkOiubUDNxNbYmxaZdkp-ZaCbQPLxyCPJ6mt_0W6lEvgzv3OMfms89RdAg-RfUkr1NUb61j2ZVwcjhL44ktbjDLhcgaT8uHT9FEW1ZMxnSzq6oSo8HaWJeGACwxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکانتش در توییتر:
MaryamAzimih
مریم عظیمی، مهندس ایرانی اپل، که پیش‌تر از بازداشت و انتقال خود با چشم‌بند در خودروی نیروهای اطلاعاتی جمهوری اسلامی در مشهد و تصور مرگ قریب‌الوقوع نوشته بود، در مراسم جهانی رونمایی اپل، یکی از فناوری‌های جدید دوربین آیفون ۱۸ پرو و پرومکس را معرفی کرد.
عظیمی در ویدیوی از پیش ضبط‌شده اپل به‌عنوان مهندس کیفیت تصویر معرفی شد.
او در بخش مربوط به دوربین آیفون ۱۸ پرو، قابلیتی به نام «تصویر مرجع اپل» را ارائه کرد.
اپل دوربین این مدل را پیشرفته‌ترین دوربین خود تا امروز توصیف کرده است.
حضور عظیمی از دو جهت در میان ایرانیان مورد توجه قرار گرفت: نقش او در توسعه فناوری تصویربرداری در یکی از بزرگ‌ترین شرکت‌های جهان و مخالفت علنی‌اش با جمهوری اسلامی، از جمله روایت شخصی او از دوران بازداشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ORjMKVw1C1IrJln3ic8NX5ZVa735Z-cdZGEw8GxoghM6H8lF9vpBRVgQ_Wj0VNPolqf8eKu-6gJKlxkESlsvB0guR06aSY20xUY3t7mU_SkoKd5eozNiUW_W7x_hyGKrYhteL-0u86R8b1nZ1HrFWTyzAXNQVRdp91FCsV5pJfI72Aki8EkGhKx9cKAhuYI8eiAPP_kZEOm7HjRjPO7DgUuBeto5rGQXQJIu0ScpYxLFZyePE2B36-enoFaVCrOWoM__U1-fGIbFyuaN2TxEL00T_kWzMpAqX2HKEKC-BY5RHqUZaW-v5Xd7D6MY9iruU7yx6eGewTIYvMjjXmJzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fyXN8Fl1Aa9JCWGBBjDKjcZko517Qcy4O72QvGooHWBVmQODuBiK5hnYwaCNaIxSb-J61QVbrhrtxdpsJCbXthgE11jT6CuHT91OU6naqae4ib-9OXKbjJgaRE4KD2tVToJK3a9CcZvwF6bWgRu3087VxcTlPuuN19zZPnvtvXu4wuqImqH01ghb8eKg58y6cP8xHRcsqSBsWf8zTdXog5OOL7N-2-FGZUEL4PzjVTa9LlNEE8Umzn0Lf2nfXrGXVJM2piR6A-UcNMr94O-_Of7ZokYE7FgeHuXmLOuwHOK1m3xdOr_UjndSHAFnnTiBD64JwkVLTl1YCslKo9u9cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bxd3NPVfWhwhfAyH6L9UPCyDIzKt06YujaFLBZJWGAgBKa6SjumGTWrNDjQ5tWg2sEYGbanLXemfRUCMoi-Y3D0XvtISKLV8BnJL6eB5RTKPykdH-6r_n_2PtR8saD9bYEhJUda5J87wHGS4MaGXGE9OoyfNnusOuB56CmAfm6WEsoHEQZQ_GafHwHNPxV_17WtoL5rHTiMS0Ac3u_ZYoQPaTXlDSTnrpZCMCgfFEKjmhoICsT60K-TWQ01ms6BpixrTAzVRW0QpZjLoPXS4N0a311F0UijMoRRjDSPdKeR8H4I3cNkt22B9xgBpzb9zNas8h1LJJj69fWt3euYoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0ZFI3f-dDuenQCnSz1TiSDrO-x2ZpAFFuCyD46CjA9kaJPpOMK20hqoiMZJzNVwmiZo7OUYwZ-1kiX9egnAYXExDq-u7Q5Y3c6gmsf1wSqG--YNPggpa8EF7_rywmfLf2M_Q24-v6j8C47dZbALvMDo8hEnqIiCOGb6E_Ce3UzBRTuM5nyRpolxO5ZlTTi2NGKa7PUcrmGU8JovhOXJz0wEB_RJgGGc5HC27ymrwvnoP0kX4M-2F1zDvkXxEGBTDuM2HgMSGeLwr3xheZ3ySW2jdVex3hVKagzZIfIPdCzWPlVELHHSUArpF6VZxwRqksKUJ_65nQMf7oHLXt8dzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5TbcJgqD5DfC89xtBvon376_etQoi2gX0k_JpqYGn2o0GdLYpEQFT04W_bkjYCMC9dnkma6TtwL3vfnmzfnExy7pYrtbcyBX_8-lGepgapSaRHlC41U9QefDhQa0ip2_tX2_pT_TuVHv9hAcJhe5BMfWmKiLFVJ4Yb13iOIdYgddlF7lEngjT7pn7u-cQpBVinPUPpa_0IZbCPQDTE5287h2uUdLCqoqHak9UUXScWwhdGTNbbJtjuyFFd6nbMSu3uEgq47pZbGeuXtYFULXS63JJ9h3pYZMDnCbp3pGm7wG3wQzYpw_i6Tjho7iW4ejX_53AbM7c-i5xg8FIEj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=gB4Gp13SUCmNUyEXhNUgHCg_y1ecq0pOY7Y79wqRarnG7Vq0snPX1y4vkseWszDF4788KAC1SUnw9LJPnQzDcTNsZdNEeF1y02Nhn9ywcMVjrj0k2nGVwTEHVIWacmfejJ1c0-gpQlZXfaodvpm1vlMfm-dq3hTaDoGayfVX_xRuK6KAA_tIEb8-P0EOgtUGdtZfL6x6PiaK89qhJVXzCOJoO63VE3b7-NVjO0kY8XtJ7o3E3_Kb1o6fndV9zcYcTDQYCzm1XecCiodsq0dFgpMIQTF_kQTh5VWTP_FGWc_me2Ma2Tl5xkj5nxEPnwWjitbp1WCkLIglH_9p4tbgYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=gB4Gp13SUCmNUyEXhNUgHCg_y1ecq0pOY7Y79wqRarnG7Vq0snPX1y4vkseWszDF4788KAC1SUnw9LJPnQzDcTNsZdNEeF1y02Nhn9ywcMVjrj0k2nGVwTEHVIWacmfejJ1c0-gpQlZXfaodvpm1vlMfm-dq3hTaDoGayfVX_xRuK6KAA_tIEb8-P0EOgtUGdtZfL6x6PiaK89qhJVXzCOJoO63VE3b7-NVjO0kY8XtJ7o3E3_Kb1o6fndV9zcYcTDQYCzm1XecCiodsq0dFgpMIQTF_kQTh5VWTP_FGWc_me2Ma2Tl5xkj5nxEPnwWjitbp1WCkLIglH_9p4tbgYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب «کاروانسرای روس‌ها» در سبزوار:
quotes
خانه واجد ارزش تاریخی «تومانیان» معروف به «پادگان روس‌ها» در سبزوار روز چهارشنبه در روز روشن با لودر تخریب شد و اعتراض گسترده فعالان میراث فرهنگی را به همراه داشت.
تصاویر منتشر شده در شبکه‌های اجتماعی نشان می‌دهد که یک دستگاه لودر روز چهارشنبه ۱۸ شهریور بخشی از یک بنای تاریخی معروف به «پادگان روس‌ها» در سبزوار را تخریب کرده است.
«پادگان روس‌ها» یا خانه «تومانیان» در سبزوار با وجود آنکه در فهرست آثار ملی ثبت نشده بود اما از سوی میراث فرهنگی به عنوان یک بنای واجد ارزش تاریخی اعلام شده بود.
معماری این بنا متعلق به دوره پهلوی اول بوده و در زمان اشغال ایران توسط روس‌ها، ارتش روسیه مدتی در این بنا مستقر شده و به همین دلیل به «پادگان روس‌ها» مشهور شده است.
مجتبی کاویان، مدیرکل میراث فرهنگی و مدیر پایگاه بافت تاریخی سبزوار در گفت‌وگو با صدای میراث گفت: این اثر بدون هماهنگی و بدون مجوز میراث فرهنگی تخریب شده و اعلام جرم علیه تخریب کنندگان این اثر واجد ارزش تاریخی قطعی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LqfmFdK1PZxi1T7PRxkliv0iMK9Y5xPg7Tl0pNK4U950zsWkQMNxM3A9RWc2JK4J9eVepMhgQlv4MnuCHi70tcWKB39Z-9QOQlWFvZgdP4g0nhGxo_SPkRUXdxM2wpsRCph73_UVpisff9vs3ufeKTd-uZ3Tu2XRYsBsZKyqbQWzc-nm2zM0nifQAZs_Gqn8-dSCj20BmLTvntH6nba1l9fgwtAQid80l3mXXZiG0lHGM331kl3GIVi7ya-npbWLhvgbYXugPN3b4X9XW6fqBm3MyIDwG01Rt3u1JAyY1xKvkQ2DwZbYwlp9bz7kMYsw-V2pYlOGj47PWpla94iLtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t9yJQNACdtBwnL8xbcYoect2v0un_Cv_q1k3yhvxT8uEo11PLulMJfiItieHT8z3OrWARXcwilqAEsFvZaqNpnejMr1tdftit9d32d7hcMUXW9LyLTL24wjuC2sogPi4-RIWBlW8ujp3Kj-NdU0dxCmJTdB7ZAa_LRbTPEYG4Qp2TT059wkDRZtkJ1VZzCUqmFmzOhrv2ObOfEktoR49TFbGTwp-YNCtC_z_xPmhWw1F86cHKCD4pCWzCN2p18O0J4EgaQTDJO2ri3dbs6JkpvvfSFFPOz89IOjxPzeWvQtYBQky0AHpYTiPvZh48aiu-OXL5_y2nAzQERFGHjIAQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ از مشاهده «تحرکاتی» در کوه کلنگ‌گزلا خبر داد و به جمهوری اسلامی ایران هشدار داد: «توصیه می‌کنم ایران زرنگ‌بازی درنیاورد، زیرا مجبور خواهیم شد بسیار سخت به آن حمله کنیم.»
ترامپ در ادامه از حاضران پرسید آیا ایران باید سلاح هسته‌ای داشته باشد و پس از پاسخ منفی جمعیت گفت دولت‌های پیشین دهه‌ها تلاش کرده‌اند جمهوری اسلامی را از دستیابی به سلاح هسته‌ای منصرف کنند، اما به گفته او، مقام‌های جمهوری اسلامی ایران «زبان گفتگو را نمی‌فهمند.آن‌ها فقط یک چیز را می‌فهمند و اکنون به مقدار زیادی از همان نصیبشان می‌شود».
@
VahidOOnLine
رییس‌جمهوری آمریکا، در گردهمایی جمهوری‌خواهان در دالاس گفت جنگ با جمهوری اسلامی مدت کوتاهی پس از انتخابات میان‌دوره‌ای سوم نوامبر پایان خواهد یافت و تهران خواهان توافق با دموکرات‌ها است.
ترامپ برجام را «یکی از بدترین توافق‌ها» خواند و گفت جمهوری اسلامی در مسیر دستیابی به سلاح هسته‌ای قرار داشت.
او افزود: «اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای بی-۲ آنها را هدف قرار نداده بودیم، اکنون سلاح هسته‌ای داشتند.»
ترامپ گفت در آن صورت مجبور بود با رهبر جمهوری اسلامی تماس بگیرد و بگوید: «جناب رهبر، حالتان چطور است قربان؟ کاری هست که بتوانیم برایتان انجام دهیم؟»
ترامپ در ادامه تاکید کرد: «ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. موضوع بسیار ساده است. نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=sn1GbNZ7jHjAW8iFmtlYRBfpjJLmrz6TpO6KjEohLDw91loPsskmMtPnxbLp7jbBhJ1TQPQagSZ64Zn8SNTRZvivcAm0v18GkLA_nDS0qjkPmyIeDtZ8imdfazrKI1F1ItorLJojzRxKUiKxQCdU9TqDQrx5awn_LwJLSOOAR_G5JhO3BXJ47C6tYeHeGaxK0MV3BjhsDlqEkgvwc9_rrRD3IlitfZLPo1cxnL7QzvW6WnBukEoM9OEjyCAqUIJpwwPWBFAVuHkKr_KrxfK6PyOp2p0XBEU5E_ecbJXvF3ezbPhuLAY7F2j6DSlKtbiynpd6Gtr2Jgg_k3_VfrSS1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=sn1GbNZ7jHjAW8iFmtlYRBfpjJLmrz6TpO6KjEohLDw91loPsskmMtPnxbLp7jbBhJ1TQPQagSZ64Zn8SNTRZvivcAm0v18GkLA_nDS0qjkPmyIeDtZ8imdfazrKI1F1ItorLJojzRxKUiKxQCdU9TqDQrx5awn_LwJLSOOAR_G5JhO3BXJ47C6tYeHeGaxK0MV3BjhsDlqEkgvwc9_rrRD3IlitfZLPo1cxnL7QzvW6WnBukEoM9OEjyCAqUIJpwwPWBFAVuHkKr_KrxfK6PyOp2p0XBEU5E_ecbJXvF3ezbPhuLAY7F2j6DSlKtbiynpd6Gtr2Jgg_k3_VfrSS1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=XmMTyim-Bu3arFve3VXfGeE2-3PXBBjTdwRi9jLwmY2X5sHxnchtlcm9FGihZIljOcDqaBAflJImyOElo4a6Slze-ekmw3QbGQgUegEGPGgmSBYepnnOniADw0OVQN2TSyMBJGyUM-WceZR-G7MlX3S1IwBER3EgKwA9dWPctTWwCM6KZjhJMYPZybm_Bovo--0ivMo8NKebWpzfz_PMMZ7GSQg2IIxRlG02Fg2akEvl2isl9as3yxlpsr0phqzkMnedS-N-DopKlcdaI3azSwT8jrPD-0pIOfIhKUr9Ic7lPrNYhaYgFikMCTTxUO-UfSGGLyGKou2vSXk2Poqs-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=XmMTyim-Bu3arFve3VXfGeE2-3PXBBjTdwRi9jLwmY2X5sHxnchtlcm9FGihZIljOcDqaBAflJImyOElo4a6Slze-ekmw3QbGQgUegEGPGgmSBYepnnOniADw0OVQN2TSyMBJGyUM-WceZR-G7MlX3S1IwBER3EgKwA9dWPctTWwCM6KZjhJMYPZybm_Bovo--0ivMo8NKebWpzfz_PMMZ7GSQg2IIxRlG02Fg2akEvl2isl9as3yxlpsr0phqzkMnedS-N-DopKlcdaI3azSwT8jrPD-0pIOfIhKUr9Ic7lPrNYhaYgFikMCTTxUO-UfSGGLyGKou2vSXk2Poqs-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKu9HZrwD0y6o8x-heVOswPdWR08ctOkJrIcTyZTSODbr-OrqMLCena6L_QLUUgPXHT5t3EPfkr2Emd-EusMY18CXknV-6_PYwmXfdkEYw27pDPtJ7jbZr5ZbWhNMC2qzhxXFCgouRqAt6LZbb4jP694I14W7I8y-69Cen_7tgt3owRPnTCvznsh-MQbzDMCIZvNfulIVhq3_Xka8uwJOGHStWF7gEkw7QiTmZxia6ZM2jOn9JQXazBKzEjM2BnvtmY08KAa6Y8aCct884RRvjWyxfYzp0v9yzwY3jgfAJkrjVPnf0MXfoXXmL80pCsmSa-OOLhncRr5B_lnhRuZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DsCIEZeQmn7QTWgDKjdGk_1Ic84Nnkxzcpl2XMZlj-hnWE7KvwnfXVycpWcMnw3Up_aJxtBEwJ53K5Xevr1_oUjxs4Vh0IuFgFdSI7AwL08yzqkjEH0Myl1WRJeuV_DfAtHomfnekFdWSbPp_akNNKDuBLni38ZBH9ugjvrE2KZi1npfMXBHf_oqKPAt5HfBm8TpWYD13aFVvfaKCxEmEpnb7vEOjNXXGfDMYs1cb53rx-Xq7PQGghw-QcSmGpW0bTaO_sj9czKymunF4it7p1O6cj1zs_2zXsvjabe7ZidvjeVnoDDIjJ83aP7Y23X7x2oT2RX7-378MwDuzxhoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=YSptPhpWf2DYmc6wRy27iq-Q5CvPY_DdDmKUrZ-kkh-FiIERogtQkdZ27EJgEy_GU24BHOwp3wzaVWzZuzGM1dL0vYQpRAUdnVa4_bWuAuGE1sIqv84IyYHfJ2TWfZ58KmyHyL7pD47yciugVSNYx5hIvcc7OX3USYK1arhXmEAjmf2BkRoeS9s9uObELb9EhhECezQD_hoHx-kVZMVJhIWXpqlvW3NkZ9jOLbl3kWSsBwBn84yJpYD4bZTAuLirF5y_P62ghmdx0wLAssiqxh22Uv7IV4hVtcsLcGZ_LfMqlDS8yO5zJ945_Ufjt0_TuyWCTig5oTLz_XCSuBp1BA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=YSptPhpWf2DYmc6wRy27iq-Q5CvPY_DdDmKUrZ-kkh-FiIERogtQkdZ27EJgEy_GU24BHOwp3wzaVWzZuzGM1dL0vYQpRAUdnVa4_bWuAuGE1sIqv84IyYHfJ2TWfZ58KmyHyL7pD47yciugVSNYx5hIvcc7OX3USYK1arhXmEAjmf2BkRoeS9s9uObELb9EhhECezQD_hoHx-kVZMVJhIWXpqlvW3NkZ9jOLbl3kWSsBwBn84yJpYD4bZTAuLirF5y_P62ghmdx0wLAssiqxh22Uv7IV4hVtcsLcGZ_LfMqlDS8yO5zJ945_Ufjt0_TuyWCTig5oTLz_XCSuBp1BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/glTZ699eRW-_YrQFjO9EQd7r-5lSlA2hNOZgEBlCMIG69DHAwNgwWfJgDu7Wt88CtOKn25wBtf3ULxMx6U9VajF6bvz5ynbgKEIlVTu7XRjW3aRGiti5xLWquZ_mTErneosB_fEXHkD98jFtcrVEEECtkyEgnX35hlbmw3cTXiUQd31-7pv5d1CF8BXIFHSdSy2475qfMihwYI9EjFzfSLIv6wrze7TtwIyUHNl5noQ4UnvKjYZhfly35vFJkjpsHZkZ_dnp6MW_-Dgj_RPPTmnggCJYq0_YEFz1Uel8tGmts3vvKOAAnUsK-pRd6cwzDgEYORCIn2IBZN0vM7Yuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sedVoCfOMTOMCxVUHXgJlc430zoneApc1qbmww_cXdtzROd5h9ot0MWzvYoUW1icHAZzNEEgemaKY8cyI2u7E3OJybTNYb7JHuiYuvnp3Ff05PUtKngYBYKpvUMOwsbxUNSlqZZ5HcxUHMESPpIKfIHu3awLN43bP2GOq9vpEmy1M8ErOAzAWuW382aNF8Vr_UA6Y18le6j1oVB-6oGwZb6cBRQk7XmjliVD8-wdb6jkwYPumr_20PrD8p-6KkQbYWUzpriiEM5h0lT-KRunFQV_aprk5RIL4CGLriMA7BPEnyDT5sa38OB9h2iZ1W90ZQYX6YWAwTthX1Y8UvMBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErgK5hsaXbTCszb3hqnR-IT4jigjxKRFJCzZECTanDGywQz1RvIFueNhv6hWSjRFB-ZzdwGgARK6mwjN1pqriSGKdKOQ-g5wIVnRXIyW-nBh7NF1cR5D7gE9F1UJ1PWHdMZUcG2mY_dSdbMc9HGJF1ZWbTQHcEKIgWcn3e5x060A0axj6y6ZUGgiOMSixDI-ImYwghtGVi5BKXny1Y8H2aEatXSHkS4fYV94desVNwWuGZZj_tbOB35teMH74DDPexAicDPlVOEoZi3nS1rXdI3AgfARAgPN_x6QRBO2PT9nROiwjXRR3bMvYIutCJzNzAYGwtv9Y6pQnPm33Ru2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aMAcgNyNSjdSx3BiWZHHcaXFAaGTbr0kLUe7InIsmKQ5MatBdefwVfvBAI0YFovf4WNR5AEIRw0QlGaGhOlekXn3CcAwrZdhFac7KTnUNfiZOPKmVc5oP_ZVuiEIKKXgFlVvBMFBVMP-7KLP2ESpUc2tMu63zWhy-kMrGL0nDcGNBsIbNW4UXpKVP4vFHHullXZRUMF4vr2Pu69l-F0RMHxC--A0fTvP2jw2Ap3oOruV28MFUMrwNZo7jeXEZ6Wr2oNaU2_z5eo68obvrw6eEZTY0tTNzUm9dr8awADmoNjoAo37qg3Bd-ZJdd1YLSYx87CvUIu3-UjBOdvcTGHNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cGDO-sZ6oedbPih255dG91L8GiEvhbPd6vcqJrYIrqs_UgI-HpXJ5ZGp0ERBapawkJjEgbiPQikGHQqatyhoLYP9Hx7CYkLCFjDc4hCQDIBOxmy78IAuUEFAUoy_wfhRQKpTvNPu6-zdGLSpe6rH4IRN9suOJL48WxIqMrglXtBUEoovKq3ynrewek7TKVAJZBNDsTXHpLrtsbuaIx5o8hmQsOh866f-5cT5exv-Q8exxawrjdBMFv0hdHkdBe1ttaWCTG7ovQHMhW9ja33HBtBvcRYm6CHSQpnU2MSqW_0QUgZNjJkoWWuQMuQqeuYr4GKHSJ9nJnMKaBXX1PG7TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) ظهر چهارشنبه ۱۸  شهریورماه از وقوع حادثه برای یک نفتکش در ۲۴ مایلی بندر راشد امارات متحده عربی خبر داد.
براساس این گزارش، «کاپیتان یک نفتکش گزارش داده است کشتی‌ای را مشاهده کرده که در حالت لنگراندازی کج شده است، که احتمالا نشان‌دهنده ورود آب به داخل آن پس از حمله با یک پرتابه نامشخص است.»
@
VahidOOnLine
مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در ۲۸ مایل دریایی جنوب شرقی بندر فاو عراق با یک پرتابه ناشناس هدف قرار گرفته است.
بر اساس این گزارش، ناخدای نفتکش برخورد پرتابه با شناور را گزارش کرده است.
خدمه نفتکش در سلامت هستند و تاکنون هیچ پیامد زیست‌محیطی ناشی از این حمله گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78295" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IIxtwtp8F30Mc3FBTOyttLYvZFnjAi_nNNo1lg1tGid4D1mL-Go7CS8M0aGLSW2vyUQlwSwFOpluGg74E_6UE6i3zZ9p2iihq0TnChMxBgYgNyv-wHtG9t_EDjD91y4zw1pz_KO317h3xKlGjPMidnSH9JfhF2lkMWUFBS-xroOIaVmyKioVDrQiq5Ls0ha7VgLcky60pyZM58Q50o48lUiEmnEoixiDJiHHXUwp1BQPHG5b-RxF2ES-eLlcmiKIf9RiYFrCXAyCnZwq4EpKnY_9vzekuqLaEr7fQFQaJc1Q9rjLHtnObISNTg0Gsl4kNvl8r2dOEMVrVEnb60HViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
🚫
ادعا:
نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که دو ناوشکن نیروی دریایی آمریکا را که در خاورمیانه در حال عملیات بودند، هدف قرار داده‌اند.
این ادعا کاملاً دروغ است.
✅
واقعیت:
هیچ ناو جنگی نیروی دریایی آمریکا هدف قرار نگرفته است؛ تمام حملات مورد تلاش سپاه پاسداران شکست خورده‌اند.
در همین حال، نیروهای آمریکایی تنها طی هفته گذشته موفق شده‌اند ۱۰ نفتکش ایرانی را منهدم کنند.
این شناورها بخشی از یک شبکه سایه چندمیلیارددلاری بودند که منابع مالی سپاه پاسداران را تأمین می‌کند و ایران قادر به دفاع از آن‌ها نیست.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78294" target="_blank">📅 16:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ql5P_Cd-Hm5AaF57bug-A7UVSEl1HINCPt2Ae-UP1BftKQJq3Lc1AeBY9bDOfde2MVlV2ucDsSjeYFtv9IvHB3546lEu3UeI7syRrSZe0qysh-MAzPEpHPKz9OfGPJx-KXZq7MxQ-oLGCWJFojfiaf6_YgXGZRmYlOW2vwaDnQPwdKZlguZSnNAb96L1wQTc1k6fG1Gn6W6rtmkHCFVs_VOWIFMrfZSsMAGc-4XAT-4LioA0v684PKYfIa7H3oGx83XjbgG2fUPJh1Ht-T-HtLfknk3IWjfVjUeK1Ft5kPnbgZ46tg7IM4g7qEJILISKAyxF1MUdnbdBicpsyPtUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ماموستا محمد نزهتی»، روحانی اهل سنت و امام جماعت منطقه چیانه در شهرستان پیرانشهر، در یک حمله مسلحانه کشته شد.
سپاه پاسداران او را از روحانیون همکار با بسیج معرفی کرده و مسئولیت کشته‌شدن نزهتی را متوجه آنچه «گروهک‌های تجزیه‌طلب کردی» و «صهیونیستی-آمریکایی» خوانده، کرده است.
براساس این بیانیه، نزهتی سابقه «همکاری طولانی» با «بسیج اساتید، طلاب و روحانیون» داشته است.
سپاه همچنین فعالیت‌های او را در راستای حمایت از جمهوری اسلامی و آنچه «وحدت شیعه و سنی» خوانده، توصیف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78293" target="_blank">📅 16:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=fJ8cUYvDiTFCTF44gdT3GONIHX7RPBgusIRA8X5joseCerdHWU94agB4YQxp_PZ3rFimXkms_MRguU5yK4g09SlSkluifZGvIyw8_weXsXM8g9cM-GpeGyF0prk4OpLCXAx3XtJQB8fPeY_iBptJ-GrhcdpRbtgn3NhNLfnc1G1ltrASGwU4VUk5wdHz6wsDZbOUAnvNY176ULAIgdc_1zlAOUJhi0m7cpD2myM-gi0HUsPZpLhB_lOPjBg8J9dve0YOx700TG8kEjl8-rWbVsSsbW1EtN0QFB3pbLG135As6_x-UNe0nV_7D35LmCmcT-nHoUjRSTuD_w1MkUxFHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=fJ8cUYvDiTFCTF44gdT3GONIHX7RPBgusIRA8X5joseCerdHWU94agB4YQxp_PZ3rFimXkms_MRguU5yK4g09SlSkluifZGvIyw8_weXsXM8g9cM-GpeGyF0prk4OpLCXAx3XtJQB8fPeY_iBptJ-GrhcdpRbtgn3NhNLfnc1G1ltrASGwU4VUk5wdHz6wsDZbOUAnvNY176ULAIgdc_1zlAOUJhi0m7cpD2myM-gi0HUsPZpLhB_lOPjBg8J9dve0YOx700TG8kEjl8-rWbVsSsbW1EtN0QFB3pbLG135As6_x-UNe0nV_7D35LmCmcT-nHoUjRSTuD_w1MkUxFHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مادر یسنا (فروغ) اسکندری در سوگ دخترش
یسنا اسکندری، وکیل دادگستری و نقاش، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در منطقه آریاشهر تهران هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78292" target="_blank">📅 16:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qnbhj8dix9cjCYrv_hsk7cia9BMC192TzGQWxyqWI-I8f2OlOCyK7IlUkKhO8ovkRvszQ_r6Luzq4pv4rJQ63LN4hUdloQFyMcUGEeYrty4lvkH7CjIK4Im8ce-JtvCcGKuOjM7WjiiC--9cEGI2_4fNB1P3M1XHs5s5N1hT0cjsDQ-z-HVBu3V1-U_p7S4nJs4VlgkVYf41Y5OUgzKRpT89Rc_DoMo1E07nPkOkPNnvQukGlU0nlG3hiyYDWrMgYrHTB8ukQ0fO9TTHEbCia06bWTcnbTlQZV8R4fzQB9SO9JKS4KZLZBydORyU17z0W0RKs7MkoCruz-mLVP4Wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=fdqwwEcvPpZsGUifxaKeRwTEJO-3uMzs-XnXS-2RVdzsN2MCxKApueXbVfQHSgoe8ShZoIX9ppdPszOIHp9_Qpq8z6Esa_NPPI8-afv3Iaf4hAcUjX-9JwE7ItFz6sQaeeXJe8lVyozHOeO66viYckGMEKcgL0txZEEkUXf7ykGdXhvg0C184mxOjRmrvlxKQVNomu199jIq2iBkapxpSrh0IkMnpPEBvdxydjStDbwIMYmtHgk7GsFRoTzxWaOqiTOUkp2EEFGfLG4YyvtAB4ercHnC9Q234gMBhRBNI-rMXjgYoedvAAE5aFxeeivwDq9G256nwVS0V0HAIUQDjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=fdqwwEcvPpZsGUifxaKeRwTEJO-3uMzs-XnXS-2RVdzsN2MCxKApueXbVfQHSgoe8ShZoIX9ppdPszOIHp9_Qpq8z6Esa_NPPI8-afv3Iaf4hAcUjX-9JwE7ItFz6sQaeeXJe8lVyozHOeO66viYckGMEKcgL0txZEEkUXf7ykGdXhvg0C184mxOjRmrvlxKQVNomu199jIq2iBkapxpSrh0IkMnpPEBvdxydjStDbwIMYmtHgk7GsFRoTzxWaOqiTOUkp2EEFGfLG4YyvtAB4ercHnC9Q234gMBhRBNI-rMXjgYoedvAAE5aFxeeivwDq9G256nwVS0V0HAIUQDjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bNnx4yvdLUIzPd63x4D2uomrSecxTo15WIB0XRAApwKGXvsjdF7ZsebjsBIWHBBhTgUSVFD4qp3QAmYvVG736XTsQtBDpZOD1xIfgsTcakamaAZiBrwhaaoehpCnLwa2Mx5STW1INnHcXzgdQrmp2XzUvLG5d5WjeU_wd71fCcKT1shw96lwtvFPw6couZvnh9j1sxxX5pz_rN08TuKbmOhRKJXdvXDCdtz-uXNCeP78lqBDYXBg6NRggCgbq7ccpGBOhreKq9SIVFJAdi2z-V8uh24y3ZbPeuZZLE2syWBN3Cq73diS2XuZ_Dfkr3q4KhqoKrOhiTQ-Hz7UxmkIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای خطاب به «مردم مبعوث شده ایران اسلامی» اعلام کرد که با رمز «حیدر کرار» به پایگاه الازرق اردن حمله کرده است.
در این بیانیه آمده که به محل استقرار جنگنده‌ها حمله شده است.
پیش‌تر اسکای‌نیوز از رهگیری موشک‌ها در آسمان اردن خبر داده بود.
تلویزیون دولتی سوریه نیز گزارش داد که پدافند هوایی سوریه برخی موشک‌ها را که از ایران شلیک شده بودند بر فراز شهر مرزی اربد در اردن رهگیری کرده است.
برخی رسانه‌ها در ایران از جمله همشهری نیز گفته‌اند که سپاه با «موشک‌های خوشه‌ای» به اردن حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=PphEzkiNn4RMzqmFrdxnVpvg4nndC5TCCxtVAFvmQBWob2zQngdbDOAPuJ40co4XHFc6zD0C8E4uJH2zb_Gvk2ozaJp21JRJhVVRif3bhkuAnwWIhUed3QsdWWmlldFojrFgq0MsBBmdMXV5lMrFszgHUSb2zDiVKQ0J-QHqGM1HlNBmMf8xUw4FtjLuCB41W1sqbhrRjhXlOnRsv6AQUpAsQNOlEHyMRvp0cGTtlsRIaRxGe8sSnGTHXkI8I5hekjo_qORS1pk-N6lPUvRy6zTBFmzsRD6tkdtdPiUuyn-_elgwFjad4jAu1gBZOumjyMCQt3tURYjAsdMvi-CGgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=PphEzkiNn4RMzqmFrdxnVpvg4nndC5TCCxtVAFvmQBWob2zQngdbDOAPuJ40co4XHFc6zD0C8E4uJH2zb_Gvk2ozaJp21JRJhVVRif3bhkuAnwWIhUed3QsdWWmlldFojrFgq0MsBBmdMXV5lMrFszgHUSb2zDiVKQ0J-QHqGM1HlNBmMf8xUw4FtjLuCB41W1sqbhrRjhXlOnRsv6AQUpAsQNOlEHyMRvp0cGTtlsRIaRxGe8sSnGTHXkI8I5hekjo_qORS1pk-N6lPUvRy6zTBFmzsRD6tkdtdPiUuyn-_elgwFjad4jAu1gBZOumjyMCQt3tURYjAsdMvi-CGgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین
خبرنگار:
آقای وزیر، بخش زیادی از توجه افکار عمومی آمریکا معطوف به آخرین تحولات در ایران است. می‌توانید درباره حملات آمریکا به نفتکش‌های ایرانی صحبت کنید و توضیح دهید که این رفت‌وبرگشت اقدامات در ۲۴ ساعت گذشته چگونه بوده است؟
مارکو روبیو:
بله، این رفت‌وبرگشت کاملاً روشن است: ایران همچنان تلاش می‌کند کشتی‌های نیروی دریایی آمریکا را هدف قرار دهد و هر بار که این کار را انجام دهند یا تلاش کنند انجامش دهند، نفتکش از دست خواهند داد. فکر می‌کنم امروز هم دوباره شاهد این موضوع خواهید بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78287" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b638672d55.mp4?token=GxmhpHBwW5iRncaGU55ZJR34CBVwsjabwIPWHAIe5w6K1YhAV6o1oQfkQ6CvAM-85qxS3ZyfDem5WmGKCSIofdyzz00Cr6dLzXujkHlW8N__U_9gd6muPMKpfIvJEU685-PvI-pZSKPoJNFL6U0dH9jG0_YcacHjpK9rq8Tona90r6NSYw-UStvv5QIAl0G7wDABspziKf4FSBJ6CWq2myEvVS8wEDhNHZGOXFOD_yE6GWDMIxSKrWReKjTI6JGk9vGhyBW7bUmiPZon6TwYK3Tzz7lZJLCTdhE7ZiGjoepzp8XbuylyH03RJXfRmTWlJ_-NhKNDNWh1WNVZXa5OHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b638672d55.mp4?token=GxmhpHBwW5iRncaGU55ZJR34CBVwsjabwIPWHAIe5w6K1YhAV6o1oQfkQ6CvAM-85qxS3ZyfDem5WmGKCSIofdyzz00Cr6dLzXujkHlW8N__U_9gd6muPMKpfIvJEU685-PvI-pZSKPoJNFL6U0dH9jG0_YcacHjpK9rq8Tona90r6NSYw-UStvv5QIAl0G7wDABspziKf4FSBJ6CWq2myEvVS8wEDhNHZGOXFOD_yE6GWDMIxSKrWReKjTI6JGk9vGhyBW7bUmiPZon6TwYK3Tzz7lZJLCTdhE7ZiGjoepzp8XbuylyH03RJXfRmTWlJ_-NhKNDNWh1WNVZXa5OHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: "
آمریکا ۵ نفتکش سپاه پاسداران را پس از هدف قرار گرفتن یک ناو جنگی دیگر آمریکایی توسط ایران منهدم کرد"
"U.S. Destroys 5 IRGC Tankers After Iran Targets Another American Warship"
ترجمه ماشین:
تمپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) روز ۸ سپتامبر پنج نفتکش حامل نفت خام ایران را منهدم کردند؛
این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی (IRGC) طی دو روز گذشته، دو بار یک ناو جنگی نیروی دریایی آمریکا را با موشک‌های بالستیک هدف قرار داد.
ناو جنگی آمریکا با موفقیت از حملات ایران اجتناب کرد و به گشت‌زنی در آب‌های منطقه ادامه داد. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
در پاسخ به تازه‌ترین حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران
M/T Kaviz، M/T Charminar، M/T Horizon 1 و M/T Riesco
را در
دریای عمان
و همچنین نفتکش
M/T Derya
را در نزدیکی
جزیره خارک
منهدم کرد. نیروهای آمریکایی پیش از حمله به کشتی‌ها و از کار انداختن آن‌ها، به خدمه دستور دادند کشتی‌ها را ترک کنند.
ایران از این نفتکش‌ها به‌عنوان بخشی از یک شبکه چندمیلیارددلاری پنهانی استفاده کرده که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ وسیله‌ای برای دفاع از این شناورها ندارد.
در ۵ سپتامبر نیز نیروهای سنتکام سه نفتکش حامل نفت خام ایران را پس از آن منهدم کردند که سپاه پاسداران تلاش کرد به یک ناو هواپیمابر و یک ناوشکن موشک‌انداز هدایت‌شونده آمریکا حمله کند. تمامی تلاش‌های سپاه پاسداران برای حمله به ناوهای جنگی نیروی دریایی آمریکا ناکام مانده است.
centcom
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78286" target="_blank">📅 01:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=HDJsLBuXsmFCK70EyFVVADR6zAUd6Yt1J71gbIbB9nTkD0uVQyShO36CMwLzYw5OBT3sWqptrq-V73gXozQn5pGQjI_UEeZ4-zhtUVaaqko8WBukgLyqCYqtsFCF82ei4syVdbRkKH-EMNzyYRysMU6p8YcweRC_0-686wWsbjlag_zQbs7GLG87H27Gt-muMGMlk-QUPpXPy7ZlYdEZQQYTxiFNHTokJKbEnuVXR2iLJr98NQ4WtM523hocCvuG9gSVZ-0TO5IKmLHAt9xfmrrOhYP7F-2i-z6_j7V-MSUQAfOLtXwDmSr3IQshxwFb9JwPcQtUe0XlUNKJsb4EhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=HDJsLBuXsmFCK70EyFVVADR6zAUd6Yt1J71gbIbB9nTkD0uVQyShO36CMwLzYw5OBT3sWqptrq-V73gXozQn5pGQjI_UEeZ4-zhtUVaaqko8WBukgLyqCYqtsFCF82ei4syVdbRkKH-EMNzyYRysMU6p8YcweRC_0-686wWsbjlag_zQbs7GLG87H27Gt-muMGMlk-QUPpXPy7ZlYdEZQQYTxiFNHTokJKbEnuVXR2iLJr98NQ4WtM523hocCvuG9gSVZ-0TO5IKmLHAt9xfmrrOhYP7F-2i-z6_j7V-MSUQAfOLtXwDmSr3IQshxwFb9JwPcQtUe0XlUNKJsb4EhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر ده‌ها پیام‌های دریافتی از صفهان، یزد، خرم‌آباد، خمین و شهرهای دیگر چندین موشک پرتاب شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78285" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p2MombLxYljNLu79yNyi96ydXHG5a-3Kq1GFMMypLQMP91KwoMrgB9YZSbFzpfa60lHS-kNKukL8BnAytn1BG08hOPbqgR024XS93v857-BOZi1lSTnUTMRoMnOg1HjYIpNBKW2GBx0JxZEGtI_8X6353U3JB1wkcm4kAnAibZRzUHAV-rsWMWl77E8eLcNUD4lwMh_Zwsxk9TmmIy85XffZWMdle8WCziT8eMjCcm5NklrPUOiR0NZ7Dq_GN3QyAW2wLQuwrt2MVB9zsl6hX5EnM9SIpxWW9-qgRzQ3xo9JnYvI54KHQljMo1-J75wFd7pNWDeUiahwSdXht8gvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی گزارش‌ها از حمله ارتش آمریکا به اهدافی در جاسک و اطراف جزیره خارک، رسانه‌های حکومتی در ایران تائید کردند که یک نفتکش دیگر نیز در اطراف جاسک هدف قرار گرفت و خدمه آن با قایق نجات در حال انتقال به مناطق ساحلی هستند.
پیشتر رسانه‌های حکومتی در ایران گفته بودند یک نفتکش در اطراف خارک هدف قرار گرفت.
رسانه‌های اسرائيلی و آمریکایی به نقل از مقامات آمریکایی گزارش داده بودند که علاوه بر اهداف دیگر، چند نفتکش ایرانی نیز هدف نیروهای آمریکایی قرار گرفته‌‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78284" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vLmtgW3SjXvqOcFn1zv-4k6VDufEKlusp46qrHJcR_AT0TQu8byYP5s0K9eFiMegS-Hyim3hkg6j7o2u9sBdWFSti-emH3UYlJlhumrFxWNfATL61MxJO-Qmu0_Tf5ENAYMj80gt-U58cwjzaxOrEvcoiwQRV2076oE0DxulpQABWam6AUO7b6RBQTNBgsZI1UxUi0U4nQFk02-_NCbe-EtCNK8fWCJmennvLxjc_PUBB7R14iesMq9_Xj97UxZatjYyiepZ7CsMorEaA8bs5z1JT9vuO1YFiKZ-AjlNde7NhIr7wbUlglUKWShTh72hSTBgv8lVKgI2IRxdTcvzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سپاه به خدمه نفت‌کش‌ها در کویت و بحرین: شناورهای خود را ترک کنید
سپاه پاسداران انقلاب اسلامی هشدار داد که نفتکش‌های مستقر در لنگرگاه‌ها و اسکله‌های بحرین و کویت را هدف قرار خواهد داد.
در این بیانیه که در رسانه‌های جمهوری اسلامی بازتاب یافت، اشاره شده که آمریکا به «چند نفتکش ایرانی» حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78283" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WH4raUX-K68GQ2LO2zGXgJWIMFvymihlaBh-o1U3j8FY1RMiisLkaSXvcaoJ6gqLqk6LGhhwrsoL734rtyM2KMLTs08Xfonb_dWJYxZlRYd-zaX9SUoQQEcbJMs_GQxQ_TZ6vHwSvyZRtRjjI1Nuiq9kaFIluVbduh2W4sCm0W-8PdTpX5391khMl2tqphsVEkyFnR8ziHEfwXlVrQyYxq46ou6YutkE2zYr4LRvJu4RwDcWWdcUFtSobNniBvwJcHahIHm07e8mNPDe70fIUQUppTtdIzUh_BXpaHj6ruzsRJBUE2W3IPPf9CJNzJxSE4AqJQfMR-tiazfXHaX2Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا نفتکش‌های ایرانی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است
شبکه فاکس‌نیوز شامگاه سه‌شنبه ۱۷ شهریور به نقل از مقام‌های ارشد آمریکایی گزارش داد ارتش آمریکا اهدافی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است که شامل نفتکش‌های ایرانی می‌شوند.
فاکس‌نیوز به نقل از این مقام‌ها گزارش داد، این حملات بخشی از تلاش گسترده‌تر آمریکا برای افزایش فشار اقتصادی بر ایران است.
مقام‌های ارشد آمریکایی افزودند این راهبرد شامل غرق کردن و از کار انداختن نفتکش‌های حامل نفت خام ایران می‌شود.
@
VahidOnLive
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، گزارش داد که یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارک، هدف حمله موشکی ارتش آمریکا قرار گرفت.
تسنیم نوشت که این نفتکش در محدوده لنگرگاه جزیره خارک مورد اصابت پرتابه نیروهای آمریکایی قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78282" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciRTbOrO5aEOcSno6FMkNhy5ZZ-0_J9AgZhE2kUn421pSfQRLHLd9kKnuDKh9Ip1OuC0kImyHwjZv9NrWFKbdJ-_vZhNPMySrER3HWWxOthnXVvNvYUQ4p5HSW34xEDkMIpLlNx31yc1bLUoXCGll3kuww50epcje6gpm5QKdqaoGEVilxok9FMdExupYgKuXph0d5C4Zsx-TDeYagz6Epltlp436NHfFjLiwFhxYbe5picDPFuQ228aCAolqEBkOkow_h8EtxLksqsV27BtmvBqk531aI2VDdpP-ucYoeyhy3VpAEm7-Kr0QR42ckpKbWeQi_aRjVKu_-tCGNhjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، روز سه‌شنبه ۱۷ شهریور اعلام کرد ارتش آمریکا به سه نفتکش ایرانی اخطار تخلیه داده و آن‌ها را به هدف قرار دادن تهدید کرده است.
عبداللهی هشدار داد هرگونه حمله به نفتکش‌های ایران با واکنش نیروهای مسلح جمهوری اسلامی ایران همراه خواهد شد و پایگاه‌ها و منافع آمریکا در منطقه هدف قرار خواهند گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78281" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">"صدای انفجار از حوالی ساحل جاسک"
خبرگزاری فارس وابسته به سپاه پاسداران:
حوالی ساعت ۲۱:۴۵ امشب، صدای انفجار در شهرستان جاسک شنیده شد.
منابع محلی می‌گویند صدا از سمت دریا و نزدیکی منطقه سنگ سیاه به گوش رسیده و انفجار در دو مرحله و با فاصله کوتاه رخ داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78280" target="_blank">📅 22:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtepRqpLBBwSoP9ZZKO16QeNQPWQNI44oCf0p30gAIGidz-33MlL8OitmGseUzsjqFnEFcrXpDrEeHrneUZq7qqll3PQFh-pDJhYjTpaH1nI1lHppJm2huA5ku-F_Y5Q0jYHBpA0RFm4EoNq-uufTITliU7ns5Uj9awDhBeFSbiIkfNIiT9mar2-n1lUvdErqqCfbKd8zIsKcL_3Qa6OtThLqQR1vT0y2sIcG1y1bIAbTVibNXpfm6ZVX_6Tna0tjOcmnt03g-oUKHu_Ff7gZGZu6_YHDG9nHH6Sqjc5ifNjG00dZUtfPynDCCgcrvPOHRXzUNugAZHybMqFWZUW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی روز سه‌شنبه ۱۷ شهریور به رویترز گفت یک شناور بدون سرنشین زیرسطحی نظامی آمریکا در خاورمیانه، هنگام پایش آب‌های منطقه در حمایت از جنگ علیه ایران، دچار نقص فنی شده است.
این اظهارنظر ساعاتی بعد از آن منتشر شده که سپاه پاسداران انقلاب اسلامی از «شکار» و به «غنیمت گرفتن» یک شناور زیرسطحی آمریکایی در تنگه هرمز خبر داد.
مقام آمریکایی که به شرط ناشناس ماندن صحبت می‌کرد، گفت این شناور معیوب از «مدل قدیمی‌تر» بوده و هیچ‌گونه تجهیزات سونار یا رادار طبقه‌بندی‌شده حمل نمی‌کرد.
او افزود این شناور بیش از یک روز پیش دچار نقص فنی شده است اما به سرنوشت آن و یا کنترل نیروهای نظامی ایران بر آن اشاره نکرد.
در بیانیه نیروی دریایی سپاه پاسداران ادعا شده که «یکی از مدرن‌ترین زیر دریایی‌های هوشمند و بدون سرنشین» ارتش آمریکا در بامداد روز سه‌شنبه به دام افتاده است.
پیش از این گزارش‌هایی درباره مین‌روبی آب‌های تنگه هرمز توسط ارتش آمریکا با استفاده از تجهیزاتی مانند شناورهای زیر آبی بدون سرنشین منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78279" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIEDZvLLK_ppR4KMOcZZdQSKieDX0oN1s8k4TpgmpctuCs0LN9YLYJfqB48x3Ezeod6fzT-JB3O8JNH3OJv9goEZwo42XULoHhibs8_6XYKX_TXQdDFBbLMP7f4xxAHuezwh3lSP6oVGRCbc5XaZIA49IWKZm9B33-zLyy5zt0HsCAnUnTnqisljzEw9p7WgAW5VP79FWflqdVWUz9oMPvwsYQPOiZPOqSLo81fV0f8Jn8nOy1tBRecR3CfAqZW3TLcf5EA8K7gqvQQb2t4ISccXlOh5kCx3OMyXpFZD7Si9V7dNPm-8QhL0WtV85D_tltaTcZcACxzN1o_RgIZAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای دولتی یمن روز سه‌شنبه ۱۷ شهریور خبر دادند یکی از فرماندهان ارشد حوثی‌ها را در جریان یک درگیری در استان تعز به اسارت گرفته‌اند.
منابع نظامی، این فرماندۀ حوثی را ابوعلی الاجنی، رئیس سازمان اطلاعات و شناسایی انصارالله، معرفی کرده‌اند که در یک درگیری سنگین در تعز در جنوب غربی یمن به اسارت درآمده است.
این چهرۀ مهم حوثی‌ها، که با وجود جایگاه نظامی‌اش در کادر رهبری حوثی‌ها جا ندارد، به همراه ۹ تن دیگر بازداشت شده است.
درگیری‌های سنگین در تعز از پنجشنبۀ گذشته در جریان بوده و تلفات زیادی به جا گذاشته است.
در همین حال مارکو روبیو وزیر خارجۀ آمریکا هم با اشاره به نقش نیابتی حوثی‌ها در قبال جمهوری اسلامی، گفت معتقد است که «دست ایران پشت بسیاری از حملات حوثی‌ها به عربستان سعودی مخفی است».
وزیر خارجۀ آمریکا با تأکید بر روابط دفاعی کشورش با عربستان سعودی، گفت واشینگتن تحولات یمن را از نزدیک زیر نظر دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78278" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGzwEREvU37OH7Hc48bfEEUwOVGi1tK7FVaQe4mTcuGnqWG8BMh6PXCSuXjO98KVMtbymoaqrm36_-ROokthFcWfWONZY1mHtvsXVjEXQoz4aL64r1ypvBJoygFPAgIxjnaifmtoBJeyHn0TEe5Bp0kgtq5Uc_3e-nXBH9Uw8OHL7Qupff0EaDcqG45VVAJApZX-bB0ECH3s-jsr-hQkIKhOOa0GneBqr50uGtxXPcDCyq6iI2IO-b1qkoARYjY3mW6LmOYirvpYZiAnRvbKkS8eu90rmmoOerPrB0zgi30isCa4wqNIuO2w-QkhwMmEQu-l6BzL29wtlxJYQkA4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا، روز سه‌شنبه ۱۷ شهریور ۱۴۰۵، اعلام کرد در چارچوب «عملیات طرد اقتصادی»، ۳۶ شرکت و فرد مرتبط با بخش هوانوردی ایران را در فهرست تحریم‌های خود قرار داده است. این اقدام شامل ۲۷ شرکت هواپیمایی فعال در ایران و همچنین شماری از شرکت‌های واسطه، نمایندگان فروش و ارایه‌دهندگان خدمات باربری در کشورهای ثالث است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78277" target="_blank">📅 20:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rGLmLsD0JZhpd04Z-zeD1VlrKUEer00s5jYR_lcFrXvdfGaHSDE6waHFC4gNOQDM6E7esXezeN8SPsiOHCjo_PKR2fBVnzEbaIGYTN88WHs4PVLKsRUpnv6hq9vaDGbElHL6NTQyAlnhVOYRJpNq7ugao94zk2jkM1hm7AiyVxQSSHyhGvHu9EtmCVgerJq8uTpXzKivq0UQlF2Gm0BuIN7O_hJfMdWDfNhNiwbXwnrgeipAZWE5wSvkclwzNQ0ZAgVQX4nyujZ43aTNAbmmPTETR15Fe313QHi_KWYsf3VPJGx4_sywvkXlFFqeHK8A_XaEzVyr_Q3wAk7kBtEVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tgrKlePsElTLp23nwhPXkT4QfMBuf7ZlxMrpl7W-yfB8D3jCNKZdXWugfSYGaYk_ui242YC0GO-VCQLh5iNtye3YYiz6Q5U5VMcwVAFlINXzgMUff0kjFQmfTehYelhE5PPH0la3of0rARBlb-fuIZQ3K6gZcQ9SJcKI05Gt0tdgxbKEQqW0tG7fR74Dh1Jm6orfeiFOuoGbQ6Xo4kM1kzYHUrSDG9XPfGrFXt7ingk8c7VMrBU7Ygu6lR1HtDjgy7giSTV8tqBlGX-cybBpM2zsPxgFDGkmJ6zujOFgixRW2eRoAU-_pa5R1Po8CAzmRCmwELGXilyYdw0oNVSJzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک زیردریایی بدون سرنشین متعلق به ارتش آمریکا را در محدوده آب‌های تنگه هرمز توقیف کرده است.
سپاه پاسداران توقیف این زیردریایی را «غنیمت گرفتن» توصیف کرده و اعلام کرد که تا ساعاتی دیگر تصاویری از آن را منتشر خواهد کرد.
این زیردریایی هوشمند حدود ۵۸۰ سانتی‌متر طول و نزدیک به سه تن وزن دارد و می‌تواند تا ۱۰ روز بدون نیاز به بازگشت به مرکز هدایت، عملیات خود را ادامه دهد.
@
VahidOOnLine
روابط عمومی ارتش جمهوری اسلامی ایران، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک پهپاد MQ-1 در آسمان بندرعباس شناسایی شده و با شلیک سامانه پدافند هوایی ارتش، سرنگون شده است. این پهپاد تهاجمی از سوی ارتش آمریکا مورد استفاده قرار می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78275" target="_blank">📅 18:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh5QpSfBeiKvjvtMoO80Pt7QH-2Abp0HA_Evi81_BUmYi4-BivGxSwhuVwMpi1h5TRR_UUOHESNwZ9m64VlHsmQtfEfQH2B-RhV0qSMlukMMBuK9G0uvk0YISuOWhMkwFue6ejIdnIcm7m68k67oGvGQP9u9h4mYZTzcYQfA6SDlDx-tBqxckns_m8tGZv-fSgx_SWqqlBy35i1fZC5AjdzVI-pSeG5rR9IGRcbB3_R-d_sEXqx2HRbCBiYclUv8eQKopQ8XCMRJOkcLaGqJU9GE7bWj-Y8i7ZceEkIBoNtlEfksq-bfslZdiLDlXVnSmNs-l_DfV6NW6jAriXam1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرئوف اسحاقی، فرمانده حوزه مقاومت بسیج پارود در شهرستان راسک استان سیستان و بلوچستان، روز سه‌شنبه ۱۷ شهریور در جریان حمله افراد ناشناس کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78274" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kEKGp7_yWbc310R9KGpSrThe7JCWxOLnNJ9nAACy4AETZwU1MACJ4LBBJP1OZuAAeusSZMEvIScs23YpBkAF95zmoY3nuj6E-1WNm_NhsSWxzzcQzYVphpwes5DWm2Ccd9RwoBJ9twPkOiyTRPBGGb1qrQtFFLmubmFxXop8vvK1DiJVDt2OBsNiUB7sde6i0yRCz01bx726OIhn7792Rtuxhh18_aFvpCw_R_KCVgE1U5QKqxt0Pd_SzhHDuYEuq5oY6k44P4BpVJnK4i9JHApc9JbTlE7fI5LFWC52UdnOFELWFUK9XLRKwqwUg7iFdO4fPNZdmC4CL8txsxWaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eqD0oddaMm0uLpObDSpM7xyeZPxG0AAZYUfm7Xol9_kprWM-tJ-KlWgIKCdHi5rR1rYdRn7lJlAzC57vQFAb5ipsDrlhZIedTu2AegzglKysF_XEigbtNRoyMgP3dYsOMhNsb6QP-vsBvMG1wYQ5vgksq9mhCcrCSzt2sTBM7V7GxGfhnTLBvIo2Y5jObisJ8RlxBGMSxf5hzPIxjlgoUJJEajumpbfekU_dn73MX72TMebTAiAw59ltEWkZKVEMm5Opg4nl3Hu6dTp_JB4VSUUmxKTQ7b98vp3XTxNWBr5_2fLxjpYdUDn3v0AiLlUCsDwGYBNhoXIDZ6oCRtxSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GnWYg3FSC-ZPJTAgrOvSx2mWr1nnQH9xc_kM4XfCLeiBxvRl2DnKeIFao_zj9eB9ZbusKrdRlFjbODoau7R4_mkqa7c4SSGP43lGIpMZDeqfsK97zcTD7Di35q3qhblWZZO9-7e302oBWlgXJl2QLYukndN6w6fmOaB8GpYCARSzojgDtGhktTKqo3BPKoGKFxxQB3cw4zplokTrHYA20Gg28pQQ0OmqtMSTyr5mQCOiAVDwGSiqfxntBdEsM87xc0OLR-TcEDiJXR8_2uDa_Z_BjsgywmIvLUQqAENRX-vgr4eLqFsPphPdhWErtw_6j089FS8HpXJBRID_kKPlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hw4-7owFkyxuZxfezXIVoX2bw7FMGPhBro9gdJ8zysZRe8EG6iFm582-6p8at5nt-7V0DgoTGLKJrTWmFnn9GG_3GaQ1YjOB0tptkzqJBrWdQtR_v8VdhVQq2VPmSIWRoVDns2mW6-yOi1xsxTe2RSWZILyg19NbCrQY3CV28xBQWHbW97HxJyBv7BltJjVPTRwNFjVWw11ZSzLWNfX6ISA4XmL9hK7am1fUTXJPuXEZWyDX7nyOvZ4SgR-i4fI98_bgDLXie-MVbs_AxUzWSel7yhEe0gIvvX0hAmETqFNDD7jfQy1ToymQkCsq0eJdtrFDTk82eLXrYrWgp-2xrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ehrv7pxWdNJHCB0YuOyp2t96YcrhSzeN8wciZGT0_-Llc9Qqnr0aHQ1aBPUPDa_7O1L1dISaOy8cnZaoi8hK0HbsD0mDsxtYr6pYatBwbz9bgqBhnljpZrD5o_PM2nwfIxkwDGEZkeTFbTbuNSfjhp7t40TgiK-bh3psnxJYOWVgPkyrI4QwZlFF6q6ufaU77fGpJCT8Pmy5qEKJtBffTf2mOf3cAD118tZkk6jw_ub0jdTzH2LsVLqd1RdkR_PJRGttASo3ii1jHANlkDw_5CLytqYOJUMX-4iBpSRQ11calltrBzpKfNUPJQS3f9Ft22GnqVLYUpRYBUTCaiTXUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=i4bL4S34GoN2MAGdkfVN6WDjAsI6dDaINJArMgM0PuP4yvzrBWtzFt63qsaVD-9Ws0-7EDOS15FNImXyIKvpU26GauocwbS5Sy4bJ2-XENWxxwEcXyJA4IQdBZjBydW3wHAa8OKY4p03GiZ9azIqiK1B5K1HKsAhCJ9NZuW4OGPAhrjv_uKaUXnbHCHRt7RiD1S-p6_FwxJSZcbUme2ne-t6-paAE7ZnYG-k6J99Gq_WrQJKUucooW6BEC35tgB8X7qGs2vdBoXpUrKJySqWxyt_pA_EByE55yo9umeIEQ8Rlg3ClwLFTvtKguaxwv_snWPusb2BiYRCW09DXE5QRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=i4bL4S34GoN2MAGdkfVN6WDjAsI6dDaINJArMgM0PuP4yvzrBWtzFt63qsaVD-9Ws0-7EDOS15FNImXyIKvpU26GauocwbS5Sy4bJ2-XENWxxwEcXyJA4IQdBZjBydW3wHAa8OKY4p03GiZ9azIqiK1B5K1HKsAhCJ9NZuW4OGPAhrjv_uKaUXnbHCHRt7RiD1S-p6_FwxJSZcbUme2ne-t6-paAE7ZnYG-k6J99Gq_WrQJKUucooW6BEC35tgB8X7qGs2vdBoXpUrKJySqWxyt_pA_EByE55yo9umeIEQ8Rlg3ClwLFTvtKguaxwv_snWPusb2BiYRCW09DXE5QRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرفان میرزایی، خواننده رپ ۲۱ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان دستگرد اصفهان جان باخته است.
درباره چگونگی مرگ او دو روایت متفاوت منتشر شده؛ ایران‌وایر از اجرای حکم اعدام و ایندیپندنت فارسی از مرگ بر اثر شکنجه خبر داده است.
بر اساس گزارش ایران‌وایر، میرزایی پس از شناسایی در ارتباط با اعتراضات بازداشت و با اتهام «محاربه» به اعدام محکوم شد.
این رسانه می‌گوید حکم او روز یکشنبه ۱۵ شهریور بدون اطلاع قبلی خانواده اجرا شد و تلاش نزدیکانش برای جلوگیری از اعدام نیز نتیجه‌ای نداشت.
ایران‌وایر همچنین به نقل از منابع خود گزارش داده است که خانواده میرزایی پیش‌تر برای خودداری از اطلاع‌رسانی درباره پرونده و حکم اعدام تهدید شده بودند.
به گفته این منابع، آثار متعدد جراحت و کبودی نیز پس از مرگ بر بدن و صورت او مشاهده شده و پیکرش با محدودیت‌های امنیتی در روستای غرغن فریدن به خاک سپرده شده است.
در مقابل، ایندیپندنت فارسی به نقل از نزدیکان میرزایی روایت متفاوتی از مرگ او ارایه کرده و نوشته است که این جوان در نتیجه شکنجه و ضرب‌وجرح شدید در دوران بازداشت جان باخته است.
خانواده او گفته‌اند هنگام تحویل پیکر، شکستگی‌هایی در دست‌ها، پا و لگن مشاهده کرده‌اند که آن را ناشی از بدرفتاری در زندان می‌دانند.
بر اساس این گزارش، میرزایی اواخر فروردین ۱۴۰۵ در یک ایست بازرسی در شاهین‌شهر بازداشت شد؛ ماموران پس از بازرسی تلفن همراه او و مشاهده ویدیوهایی مرتبط با حضورش در اعتراضات، وی را به زندان دستگرد منتقل کردند. نزدیکانش می‌گویند او در ماه‌های بازداشت برای گرفتن اعتراف اجباری تحت فشار و شکنجه قرار داشته است.
دادبان تاکید می‌کند، تفاوت جدی میان دو روایت درباره علت مرگ عرفان میرزایی، ضرورت انجام تحقیقی مستقل، بی‌طرفانه و شفاف درباره مرگ او در بازداشت را دوچندان می‌کند. اصل ۳۸ قانون اساسی شکنجه برای گرفتن اقرار یا اطلاعات را ممنوع و اعتراف حاصل از اجبار را فاقد اعتبار می‌داند؛ ضمن آنکه هر مرگ مشکوک در زندان، به‌ویژه همراه با ادعای شکنجه و آثار جراحت، مستلزم بررسی موثر و پاسخگویی مسئولان است.
dadban4
دو منبع به ایران‌اینترنشنال گفتند دلیل جان‌باختن او، شکنجه شدید در زندان دستگرد اصفهان بوده است.
اطلاعات رسیده حاکی است پیکر او هنگام خاکسپاری، آثار متعدد شکنجه داشته و دست و صورت و لگن‌اش به شدت متورم بوده است.
بنا به اطلاعات رسیده، ماموران امنیتی به دلیل ترس از تجمع مردم، اجازه خاکسپاری عرفان میرزایی در اصفهان را ندادند و پیکر او روز دوشنبه ۱۶ شهریور در روستای غرغن شهرستان فریدن به خاک سپرده شد.
زمان دقیق بازداشت عرفان میرزایی مشخص نیست اما منابع می‌گویند که او در ارتباط با اعتراض‌های دی‌ماه بازداشت شده بود.
بنابر این اطلاعات، ماموران پس از بازداشت، ویدیویی را در تلفن همراه میرزایی پیدا کردند که درگیری میان معترضان و نیروهای حکومتی را نشان می‌داد و از آن به‌عنوان مدرکی علیه او در پرونده استفاده شده است.
iranintl.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78268" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjpSViQG5C4TdLZ3uEZRFvimgYf_Ia3pVukECGhmdFIfYCidSfWy8Xe8JxfVVIk4ssvmYTSxKwdNYyEVhzzkCMbSI7VLvKNp5arGsNNp7aewDXmS0jnokBFbayYhZdlGIamsUKEIKr5qddE9Oyfy01HkiFFAyo2-5VI8kyUDtzCEyL-XRdbO17Ow5722S5I_FLCcbudmRqxHQQKbX6TOk_QQGOBDeRR2VJDy0bcCCtymGVlhoQQuSrqq4KpcISYu8m1ZXJ189ATIP4T29MoFdEX2INPnGrSNj3JsPQwVa2SlMe5pQ3ezBAszHR_TIgvt0wv7RF7NQWwd27MoJK32yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آسوشیتدپرس مقام‌های سعودی اعلام کردند موجی از حملات حوثی‌های مورد حمایت حکومت ایران به عربستان سعودی در ساعات اولیه روز سه‌شنبه، ۷۳ نفر را مجروح کرده است.
سرلشکر ترکی المالکی، سخنگوی ائتلاف به رهبری عربستان سعودی که در یمن می‌جنگد، گفت حوثی‌ها «تأسیسات غیرنظامی و اقتصادی» را در شهرهای ابها، جازان، نجران و خمیس مشیط در عربستان سعودی هدف قرار داده‌اند.
او گفت ائتلاف به رهبری عربستان سعودی «با نهایت قاطعیت، تمام اقدامات عملیاتی لازم را برای بازدارندگی شبه‌نظامیان تروریست حوثی» انجام خواهد داد.
به نوشته این خبرگزاری آمریکایی، این حملات در حالی صورت گرفته است که درگیری‌ها میان حوثی‌ها و نیروهای دولت یمن که مورد حمایت عربستان سعودی هستند، طی چند هفته گذشته تشدید شده است؛ درگیری‌هایی که آتش‌بس چهار ساله در جنگ داخلی یمن را از بین برده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78267" target="_blank">📅 08:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlXS_xILt_OEcbe9ePVu7NBr9l7pscAGIaN2dP8ooqGrDESq1EgPX0roc3O0KGhoNUo9mINrGqr_lMeu9IMGhET9wiJtWWMoAu9QdBeL-g5Si3Od7Vm1LtG5FT-JpAKUV7QZNgbCEGcJ2lYosbO4zaKRvFGcIR6OXRzRBL5sYVhx1wn7iv5YYvEdjuZOWyqtg07StiXUmQgXH8png-x-IyhmxhJKcAYryQEGSYgINNM55Df1ym_LSha_7QVrLuZZkRHfgo20UvqbS9-iYLQdQEPir5KcW7mSRufeyRWU-9EnFuf-NXJ94CTjz_papJq88bgbZ-EBtUS1uDzOGzIRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی ما در جنگ با ایران پیروز شویم، قیمت نفت به‌شدت سقوط خواهد کرد؛ درست مثل هر چیز دیگری که دارد سقوط می‌کند (اما بیشتر!).
بنزین گالنی سه دلار، اما در نهایت به زیر دو دلار در هر گالن خواهد رسید.
همه این‌ها به‌سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
MAGA!
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78266" target="_blank">📅 04:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/980dd40283.mp4?token=caDCYg3_74rnFbz6GQeuKU9iYaEnrNcy523XED4T0EwsIJJktzJiN1U7FMpMOq-tCC2WNSGVQLHUwGz_hbrLUpkOtMi7zBakMnavXT6X-HMcJ7MfcSturjggZw1IYjP5J5rxjJfieFEspudrvHrHYYPjIN88HFo7NJka0Oei5yYFnfeeEZ7c0HPqUNsBjn4rbSA3kJho3SYwrUhGDX_pBGmYqRnWeWOI9vtn-wYlIHpEgJ3I_KiJ7In_wSKPlfa0M6_UPWvIgP7YtBYefwRw8nUbLM4Fv9902EV3jdOVTIMuRphJ_mbUfs7QKDj9x6nHvpyurbA02JBxCF4ZFnQ8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/980dd40283.mp4?token=caDCYg3_74rnFbz6GQeuKU9iYaEnrNcy523XED4T0EwsIJJktzJiN1U7FMpMOq-tCC2WNSGVQLHUwGz_hbrLUpkOtMi7zBakMnavXT6X-HMcJ7MfcSturjggZw1IYjP5J5rxjJfieFEspudrvHrHYYPjIN88HFo7NJka0Oei5yYFnfeeEZ7c0HPqUNsBjn4rbSA3kJho3SYwrUhGDX_pBGmYqRnWeWOI9vtn-wYlIHpEgJ3I_KiJ7In_wSKPlfa0M6_UPWvIgP7YtBYefwRw8nUbLM4Fv9902EV3jdOVTIMuRphJ_mbUfs7QKDj9x6nHvpyurbA02JBxCF4ZFnQ8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجید ابن‌الرضا، سرپرست وزارت دفاع، مدعی شده است که نیروهای نظامی این کشور توانایی هدف قرار دادن ناوهای رزمی آمریکا را دارند.
روز گذشته محسن رضایی نیز گفت: برای اولین بار موشک ضدناوشکن را بالای سر یک ناو آمریکایی آزمایش کردیم. این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.
فرماندهی مرکزی ارتش آمریکا - سنتکام - روز گذشته در
پستی که در شبکه ایکس منتشر کرد
تلویحا به حمله به دو ناو خود اشاره کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78265" target="_blank">📅 04:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pl1z4rx_lmBhhZYeILiZ8vgdZfoIRMbkGMQlUfNaQeTW6Yh20_CeUrbwppeqXkBmX4gwhOmfTPiC6SXfSmPBSlFquzgU0a_LPCUe_uXk5va8geYIa8YvBUjxtwsQewypIgBcha20KiKDBBqhlPTux4ar0w50nvQ0V4RA_0epbLNhpM-uLiRaVchjw6AQZsV4ukfCbPoZUhFDsIfM4xeRSo8-d_VT-5wy3IY1HlZ--Wm1E_o4ns2BdNVH2XixeOsrqcN0D5be7mTw7-kCHpj7MwF3-2z-GE7xPvRaWgZnb74yeejLCUfz597XxLcgE4zJhZ3XQG1mmw1XudqnEHRJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال کریمی، پدر امیرمحمد کریمی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴ در مرودشت، روز ۱۵ شهریور به زندگی خود پایان داد.
امیرمحمد کریمی، فرزند ۱۹ ساله او، ورزشکار و عضو سابق تیم ملی نوجوانان تکواندو ایران بود که ۱۹ دی‌ماه ۱۴۰۴ در جریان اعتراضات مرودشت با اصابت گلوله کشته شد.
پیکر او در روستای جونجان از توابع مرودشت به خاک سپرده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/78264" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzlrV5H-EzPhq5zHmtmkvbd6W6gFE1i7nVZr4nfC5oGT_N1uYrc13-h7QWK2blX9oEUMzt3EsLQ4O7dgpIKSyS5xCwEFI_8B1V9ZeUzyhm8xBkSYgXsA9oiy8pnW52FAsGErsuYo5QJhFS8EYZE8PcBONxtZjDCFJd1SfxQdxKAn_NoCCe4HrNvv_c7cp9aey4d5RY1KNaApnCanxdgT8NAFwhtsoMLskgOCpUOxWtgQo1X7SvrzyxhRpxXnTB648Yq030o4Cd_vD7QnuW5WrVBTTRb_swbzdFisMjq4_uEUfaGDHrY7q_BUP_-4-8YgBNJembm_uMAXLiLo-3GcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیدا حیدری، نامزد ابوالفضل سلیمانی الموتی، از جان‌باختگان اعتراضات دی‌ماه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ به زندگی خود پایان داد.
منابع حقوق بشری ایران، به نقل از خانواده آیدا حیدری نوشته‌اند که این جوان ۲۵ ساله، حدود هشت ماه پس‌از کشته‌شدن نامزدش جان خود را گرفته است.
خانواده آیدا حیدری گفته‌اند که آیدا و ابوالفضل قرار بود همین ماه مراسم ازدواج خود را برگزار کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/78263" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4nl4tF_sFfVsnupbNB79Wu-KbqG9j7JmxHCb-uw_A1bc6UKKXpciIYp4RwFqILmTqy2Lmeb2GrConojYzMRXpw4jJrotUA_UGoJhTn192mdl6IFvthhp7pIQaVc85X_-nS45zs7HFXNeLUcZkRNA9y1VtFgmSunO4CK6efzUh7Vr0q6vqZadMnl_b1qP0OGZua3gpaPHTf9vdeO3ErA8ePin8UKcelgpwj-BPB37shDl_nO1QJ77x7LMMxMXFx1slS5gsrhQXy2KJc-z54xQH_LFgrlFISSaT2BYk9tZ1hQd6fJ-EBNaTgKeaaJaqhixVbmht3eDdm5uzQzzFPG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته‌شده با هوش مصنوعی از حمله جنگنده‌های آمریکایی به جزیره خارک در تروث‌سوشال منتشر کرد که روی آن عبارت «خداحافظ خارک» نوشته شده است.
realDonaldTrump
رییس‌جمهوری آمریکا چند تصویر دیگر نیز در این شبکه اجتماعی منتشر کرد؛ یک نمودار آماری که روی آن نوشته شده «ارزش پول ایران از بین رفته است»، دیگری نموداری که روی آن نوشته شده «ایران با یک ابرتورم مواجه است» و نمودار سوم که روی آن نوشته شده «صادرات نفت ایران سقوط کرده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/78261" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/78260" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krulOHq0gUQBUmJvcTR9Xm5jTZv9IW9qFYdFg1l5FBo-KbqkU2Sro7B9G-nlBQJ_Dik8vCtujUSGV2aCk7e5jSbox1B9x8ESfTvJRFcn3tw-hSR_u_DXSNWtzavWr6m6EYKz4ootu7K6Io7DE458CGKDfQZl_xnuPTV3COl59Ayzipxjk_tA4Obo_9fzOq2P4Q0fWPV2wYitzQ77W58Q1gLhU_7SA13jjKA_aoYOO3H48aAQSswuQvWJQl9h-aqqJAzc4IU6Q6hz4l4u80FHFxtJ_4pinsAIS2lpZ8KmpqvvIKyxr2LqmRCzKImblfYEgH4RbKSiBpjaUBiyYsPK9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/78259" target="_blank">📅 21:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=RqJaIqsVVEf-dkEeVYjOiBVRnEko5uKYL8SiMaQBlBMpNZdrGNYlYUOxcTU-pPEyoGqqyVksKp8r_I7DIrZJ6pj7ivtSmzVdMy1IBOarxnd298Se_lZVmOCiz545IEMEMsVzGvtXqwdin-5zsERxGNIORDX4TafZQZf4yydwA7U5Ywm4m--gYt5woorACcS4F0xpzkE9KVZog9iNkBVvHxT6aNbkI9uhEhLUElzOQGKUpR8eEELhOYLE_wiDD_yOlmPdtPESZISi-vLaR9kycWSwv2EGhNXi1kyasEYMT-8LAzsKeqc3VXQo1uSrHqtLFMHAWd91fhSIU8lpHyd1-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=RqJaIqsVVEf-dkEeVYjOiBVRnEko5uKYL8SiMaQBlBMpNZdrGNYlYUOxcTU-pPEyoGqqyVksKp8r_I7DIrZJ6pj7ivtSmzVdMy1IBOarxnd298Se_lZVmOCiz545IEMEMsVzGvtXqwdin-5zsERxGNIORDX4TafZQZf4yydwA7U5Ywm4m--gYt5woorACcS4F0xpzkE9KVZog9iNkBVvHxT6aNbkI9uhEhLUElzOQGKUpR8eEELhOYLE_wiDD_yOlmPdtPESZISi-vLaR9kycWSwv2EGhNXi1kyasEYMT-8LAzsKeqc3VXQo1uSrHqtLFMHAWd91fhSIU8lpHyd1-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ سوم بنزین به ۱۰ هزارتومان افزایش یافت
فاطمه مهاجرانی، سخنگوی دولت گفت نرخ سوم بنزین از بامداد ۱۷ شهریور به لیتری ۱۰ هزار تومان افزایش می‌یابد.
سهمیه ماهانه ۶۰ لیتر بنزین با نرخ لیتری ۱۵۰۰ تومان و ۵۰ لیتر با نرخ لیتری ۳۰۰۰ تومان بدون تغییر باقی می‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78258" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78257">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iM7XndUVdiYsIn5SiI_SHRToIOehGacAI4C3gffSiaI3q9fX0s9KGmTRVRND7p-VvjVM2rn0r9Z2WbK73cB7XSguOry8DqQxqkOiVsRSZgOC-_iXch-tgtoaJTIFwQOLitY0rmhSHYHhL6TNDNjhX_WOJ7aNk6dJN76B__4ucdCEPEZ3sTKLa7AHUKV9gk126L55MFyt5MQ24evM2AJK-yc7P8unu6fgLBv-EnZwIps9LGPATBIKjrcSDDEZmpkMHsqVzAi7IIkGxRhcKjhcpczPzgRm-ZlQSKGA5ZXULc957s582mpjqm8UyjxEeq25O3KH3ZkpQzugkFzzEaREmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که سپاه پاسداران، بامداد یکشنبه ۱۵ شهریور ماه در بیانیه‌ای
اعلام کرده بود
یک شناور بدون سرنشین سنتکام را در تنگه هرمز هدف قرار داده است، ارتش آمریکا این ادعا را رد کرد و آن را «دروغ محض» خواند.
رسانه‌های دولتی ایران گزارش داده بودند که این شناور بدون سرنشین آمریکایی قصد ورود به منطقه‌ای از تنگه هرمز را داشته که ایران آن را ممنوعه اعلام کرده است.
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی آمریکا (سنتکام)، در گفتگو با آسوشیتدپرس گفت ادعای سپاه پاسداران «دروغ محض» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78257" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=GxnET7hZAi_35kYHcQ32xPolmfG_DKe4Ru5X353Q9DR6qLmw9VXaQTYEkiShlt_Mdc_m6Oir1YQodI-YNN3NW47UDr-jIp2Fa6kw2MvFMm_KRiv7-zcrBMKOeaRdwJeN1TmXm6cJoPwLztD6DKEz5MmbB5tbGVIBrKaZBvhw_FDUK6gljze9pVkTBoUlPz7C6u4ta4PBTmachhQKYXNXu1umZz-hME5E2yi3h-afRZKxv7LrAbFuyFpFCbkv5-PISlviZKG19jsqTUdT0bvUGJfa1gWHddQX6HzQ1f4rY4GbdRPeYnManWJUSU1MvZr1RHk4DVPOCJuMDDhx-ur8QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=GxnET7hZAi_35kYHcQ32xPolmfG_DKe4Ru5X353Q9DR6qLmw9VXaQTYEkiShlt_Mdc_m6Oir1YQodI-YNN3NW47UDr-jIp2Fa6kw2MvFMm_KRiv7-zcrBMKOeaRdwJeN1TmXm6cJoPwLztD6DKEz5MmbB5tbGVIBrKaZBvhw_FDUK6gljze9pVkTBoUlPz7C6u4ta4PBTmachhQKYXNXu1umZz-hME5E2yi3h-afRZKxv7LrAbFuyFpFCbkv5-PISlviZKG19jsqTUdT0bvUGJfa1gWHddQX6HzQ1f4rY4GbdRPeYnManWJUSU1MvZr1RHk4DVPOCJuMDDhx-ur8QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: قاعده بازی عوض شده و دوران پاسخ متناسب به پایان رسیده است
رئیس مجلس شورای اسلامی روز یکشنبه ۱۵ شهریور، یک روز پس از حمله آمریکا به چند نفتکش ایرانی در خلیج فارس، گفت دوران «پاسخ‌های متناسب» به پایان رسیده است. او همزمان به وجود مشکلات اقتصادی در کشور اذعان کرد.
محمدباقر قالیباف در سخنانی در جلسه علنی مجلس تهدید کرد: «هرگونه تجاوز به منافع و امنیت ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر دریافت خواهد کرد.»
قالیباف که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای بعد از آتش‌بس با آمریکا است، در بخش دیگری از نطق روز یکشنبه گفت: «نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشت مردم فشار جدی وارد کرده است.»
او افزود: «در کنار میدان نظامی، امروز اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است.»
این سخنان یک روز بعد از آن است که قیمت دلار در بازار آزاد ایران تا مرز ۲۲۸ هزار تومان بالا رفت و از سوی دیگر آمارهای رسمی نیز نشان‌گر افزایش شدید تورم در ماه‌های اخیر است.
علی مدنی‌زاده، وزیر اقتصاد ایران، نیز روز یکشنبه گفت واکنش تهران در برابر تشدید فشارهای اقتصادی آمریکا «مقاومت اقتصادی در کنار اصلاحات اقتصادی» است و این دیدگاه را که تحریم‌ها باعث تغییر مسیر ایران خواهند شد، رد کرد.
او با اشاره به اظهارات مقام‌های ارشد دولت دونالد ترامپ درباره اقدام آمریکا برای قطع رابطه ایران با اقتصاد جهانی گفت: «تصور اینکه بتوان با فشار بر اقتصاد ایران، تصمیمات یک ملت را تغییر داد، اشتباه است.»
وزیر اقتصاد ایران افزود: «مسئولیت اصلاح اقتصاد ایران بر عهده دولت و مردم ایران است، نه وزارت خزانه‌داری آمریکا.»
این در حالی است که همزمان وزیر خزانه‌داری آمریکا اعلام کرد ترکیب محاصره دریایی و تحریم‌های گسترده، صادرات نفت و دسترسی جمهوری اسلامی ایران به درآمدهای آن را به‌شدت محدود کرده است.
اسکات بسنت در گفت‌وگو با شبکه فاکس‌نیوز که روز یکشنبه منتشر شد، با اشاره به نقش چین به‌عنوان خریدار اصلی نفت ایران گفت محاصره دریایی مانع خروج محموله‌های تازه شده و برآورد کرد که «احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز نخریده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78256" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LRkO8aphiu2M8tAhnuG_Fw0DncSs3g_JR3Cy0tYVfJIDiA9Z_0wDb73GlOjv38YOUYyqPty1RLiwmziTFdnMTYBjRXDO7SZFEQaSOevZSbMJANI5fOmRssWy3fubnTTa3LJaaH5szg5YG_k2V51mHjXUpkBWrqbsYOQSjlzUfEPHPbSkFVwr6V39J8o-agqV8gZCybHjRM18H68NPNQ7ZnpLPsiaL6J9QkDP3ntkly1IvBkibGBp8VnKCUxaeba9neh2JnO8GRH7fmy1hhwKqZrHg_GR80A2gw1s57aLoLQhvjWbHc_1No-mVhpFZZ1jVJNIoLRtEr3ryDDp7IkEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران پس از عبور از مرز ۲۳۰ هزار تومان، به کانال ۲۲۶ هزار تومان بازگشت.
بر پایه گزارش اقتصاد۲۴، نرخ دلار صبح امروز یکشنبه ۲۲۶ هزار و ۱۰۵ تومان بود. وب‌سایت‌های اطلاع‌رسانی طلا و ارز پیش‌تر برای ساعتی از جهش قیمت دلار به بالای ۲۳۰ هزار تومان خبر داده بودند.
بهای دلار در ادامه با شیب نسبتاً تند عقب نشست. اقتصادنیوز این افت را به ورود بانک مرکزی به بازار نسبت داد و نوشت این بانک به دنبال جذب نقدینگی در بازار است.
حواله دلار در مرکز مبادله ارز و طلای ایران نیز ۱۶۰ هزار و ۹۸۳ تومان اعلام شد که شکافی بیش از ۶۵ هزار تومان با بازار آزاد ایجاد می‌کند.
حتی با احتساب اصلاح امروز، رقم کنونی نزدیک به ۱۰ درصد بالاتر از آغاز هفته گذشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78255" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ha2bEs7asELY4cCRStBn2898C7C-t5lXv82WDnQa6ngzQDt21l_iysT1jhglUrkFAk3Usu07w8r_wPNX1JMNW0294mWeaJ7eBVn0UUCcPd6el-hkBqYhNIaXMhSRNpiL6fRwSB3VZt6AjolW8ommGXVEYkpYFb6BLKcAXOWUZRe_x-MWppkd9Gsgkr7jPp8TTYG4gIo6Wd4GDMQH19GoTT-QpL7ouqnaUpDT3q30vX2k1iVDtaBDZEC6ftzhaI9SkCu_5COCuzDjlqYs0oy5dg4w2lO8jccdvW8b9awkjOSz2xsZA7QWllC1dftLFmt2tGQ3S1BBPeHOyCXJVgB8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QB34RHTufhAgcRczZUOSSnwu3Snb9JoknUcCyzlW3xI3DoLbH7OflyYztno5RQ3CZglQ9rcAq4z6W8u93LSur0grF7QY6s4Nllr8QkblOvdhoU_v2xPTyOQZ2WFpcqn7aU-m-e_Ye08aqwq8FTItmdk0IZe3ua50cQ7hpJnDZ4BwxCDBUbcL838_m0RzVMXxBXujp-bQvoEOpau6B44-kDDQ0SWCVz24xQy5XV8OKVu0R8xgG8YcJfF12tBiLwRfwbyEf5UkFOT50sFbrCK_PGe6npAk_FCXbKfLHgbnw4xLnK4wq3tjJexySIQjXSaWvE0UFKipFzM462QFhoXGLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bndwg_Fwqam7_ocfHlW8msjuzVXsfJn70Kw8fvaJIXroZqqIkfop3Spl5Jl_yVoVhwFISaZhS2nkn5NFpAKB4KhiU_T8IkCS2MZOH1nNOIg0MG3ItZPR-mAN9T2YBt-xM9qBgFvHVqTZrjcq7C0KpOkCdlYmfABpKlGlHoge0wh_j6Ar0kTjj4kcFu34eipb1NjZMF0UgSxRmme0u58Ub2h96bA5jdUBahJgYQOjKoMxlScNthMj4dVdcM6wd06KIj3APbzWnAA8uTEOl0GgE7G65kzlrqQv4WGRuv9QJh437gl2SNksAH5fwxeuILIPCbt-FqghUipOUR1CDippoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UacNecu7Jd1pHp_yAg0aLmxyzg83WVzl2C7jiS1dEPkkBf82FnuSh83BQV3jCxbG1KWol7G0T3BPnUwHAuXVUAzHDHt_JbNqdu6LILdCLmTU_ndLNORhxDsJ7_JECbxxoULbECVzY5FGsbaZ4jFIOniNnYcZJQTfxzg0jujdIIunwO9lwxeZ1usiieqGyAXhZk02zQ2xDgdMGu6LG7DobuU5_nKenrQox5XqTjk_v20Ra3-dMxP6zc7IZVs5zhkrwCnSwEcHQvpUsQB6s99s6k2OsOl_VDWDFln8TR9S-bfIy9iyZvj6PTJlWF5snKYXRH9qzyDxu0by-fjotr2Lpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GZcs3p1Gb7ZtPXgfkn2Wj6IT1nxLhQmcqvNJbgikqMGu2d559mHrF0FcONol6Bp9Q4SEonGXz9iMx3MIVh1YedKrJb3n-akOYs7iJ9RZ918SCPSm9Ex3hPt_TJVfrZjp09G_Rvv6MCaFGSEcyAMiUrSM3mYpbchqMKH4XhxMUdCzs9AzeJaIYG5iVZhJAqsKHh33es_Hj68znNDEDAHqXsZefwmtP48Zjbonx7ut4ARNOrMchOZf6KSxDApvF4EjggjsxuqjXi_GOnrJdo88zocgyiF5sx9y9et9kUZUZuPZyVtswliGO1hyJwVEM6i2STiYbbGAHf-JST-c0RGu_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">BadAngel66636
آرمین تیموری راد ۱۹ ساله
پدرش: امید تیموری راد ۴۷ ساله
عموش: امیر تیموری راد ۴۲ ساله
نوشته بودند ۱۸ دی در فردیس کرج به دست ماموران سرکوبگر حکومت کشته شدند.
روی مزارشون نوشته شده ۱۹ دی
و نوشته بودند:
به جز این سه نفر، همسر امید تیموری‌راد و مادر آرمین هم در پی اصابت گلولەهای جنگی، بە شدت مجروح شدە است:
@VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78250" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JFi0oDb8FmUbZlFeORo5jIJAygtc2ZnEG8BBwbC_XOGM4NtwPQfGhspJdWrDda9GtSPjkrrmZusfcZTTcaUzI5yult5bfSLAHSdI1rKqjP5e-fZaxVDOpTnKq5zDB3yLXMiqrAvRWUpyQybyVJU_qYJAryN4z1UwJn1DmXWtyRXwRB_0Ce9FaWxRyCQHAR1GXrujdNlpOhLLGmDsRXQcPDEy0XgmjMfmjgsM4mpUFFaWUJUr1duAQgg-cezOZxCqjflRiZN4JbQK3ErMkU4dHIFEuXFd6lEpsSQm_w7xeG9xHxfXq59WJ0eNJH3gqFScr1H2NeXjlmnaBygU_f7GSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران می‌گوید یک فروند شناور مدیریت‌پذیر از راه دور ارتش آمریکا را هدف قرار داده است.
روابط عمومی سپاه پاسداران در بیانیه‌ای اعلام کرد که این شناور قصد ورود به «منطقه حفاظت شده» تنگه هرمز را داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/78249" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=GjuyhBJlMq2pijF16QNerBC247BySvZCr43R954qPPhqfVEzXoDnjGAbosY0igbOel34mYJPlzmg9t45Hwqt-kCkznKNH7ZjulHSEe3qhdY5GPq17JCl9cMgDxrTbnR_0hn9_zqOG7fDsiSZYhJN6OIhccas2QFFEz3gZvX0hSmA6KX3R2Ylggjchd1Sh9L6iOfcXrUsWYNjvSIABeQKctrJGUdj9O8ULmtfoOoplO7fDEfZVaEgq8B6atKktdBvswwh_Kl6YfBsTvxbwKn1UKIXbYikRc3TrOKRqZWN2oP_QN6CosYbpkpJC338iH4YVArDemu0u3G1sdfzIxPKwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=GjuyhBJlMq2pijF16QNerBC247BySvZCr43R954qPPhqfVEzXoDnjGAbosY0igbOel34mYJPlzmg9t45Hwqt-kCkznKNH7ZjulHSEe3qhdY5GPq17JCl9cMgDxrTbnR_0hn9_zqOG7fDsiSZYhJN6OIhccas2QFFEz3gZvX0hSmA6KX3R2Ylggjchd1Sh9L6iOfcXrUsWYNjvSIABeQKctrJGUdj9O8ULmtfoOoplO7fDEfZVaEgq8B6atKktdBvswwh_Kl6YfBsTvxbwKn1UKIXbYikRc3TrOKRqZWN2oP_QN6CosYbpkpJC338iH4YVArDemu0u3G1sdfzIxPKwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام ویدیویی از غرق شدن نفتکش M/T Kylo در دریای عمان منتشر کرد و نوشت در قعر دریا به نیروی دریایی ایران پیوست:
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/78248" target="_blank">📅 04:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b4qAKjD4JY9QvqUL-T5BQAQdoi9o3uB-vPHRW41eg0ii4LB10esZ20tUjR0z1meiTFw68b7Doibh2m34DFPEpITUBf-WocXU1bpkqPIGmfRYbM3v4512Ks0ZBQHn3ODeDKp21Wa4VoUtJVxEGvnqGiFdRwmAdRfL9LLjBRY7YqgJz2J4slXxB2deG6D9MXXcoPqD1wZHeeuFmCIAY4dinSo2PhCkcyhfsMAOH7i04AVzxXzhlzZndyFcOkopC_82AKhOvPy9w95fwo5u2cq_DyhtprxU345I5eqVEwLBV5fG4JG8AZm2VQFlEmGRKLidn_ImhNLdHVBjhZUt72A6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، بامداد یکشنبه، با انتشار بیانیه‌ای اعلام کرد که نیروی هوافضای این نهاد با استفاده از چند موشک بالستیک، یک ناو هواپیمابر و یک ناوشکن ارتش ایالات متحده را هدف قرار داده است. در این بیانیه آمده است که این شناورها در محاصره دریایی و مسدود کردن مسیر کشتی‌های ایرانی مشارکت داشته‌اند و پس از این حمله «دچار خسارت شده» و «منطقه درگیری را ترک کرده‌اند». سپاه پاسداران همچنین با اشاره به تایید وقوع درگیری‌ها از سوی سنتکام، این عملیات را پاسخی به اقدامات نظامی واشنگتن دانسته و هشدار داده است که در صورت تداوم فشارهای نظامی و محاصره دریایی، پاسخ‌های نظامی گسترده‌تری متوجه نیروهای آمریکایی خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/78247" target="_blank">📅 02:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKru5FY-KMinEabHHSzv3xnoGwz1E2sDCnRi8kyRPO687lp0KiUrTkSSgsmH_ypNjGF5dDkaiI5sEDT837NzyJu_AadKciNRCUVT9CxN9C7gjSmIAiV4WXUk28CGsCCc2dSMzb2r_FwYV_QfCSmNqqrITJeP6hw1X3R86ki_IziU0irT4OounaFflNPtAIEBOs_bfUJNndI9MsBpcdMFyBpl0HzQDoTUtxGgh20Us-JJ6Sv1-I8C69L1Ivj5KA2YLlzvDEYdfreCPB9dTlXw93wSLD-0HSlBDl_-6j_sQ-9LeMdcqRuLSo8DXiBMVvQIW5MVQDU9B_ed4kMV23Hu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم نیروی دریایی سپاه پاسداران انقلاب اسلامی روز شنبه در بیانیه‌ای اعلام کرد که سه نفتکش را که از «مسیرهای غیرمجاز در تنگه هرمز عبور می‌کردند، و همچنین سه شناور دیگر آمریکایی را در مناطق دیگر هدف قرار داده است.»
نیروی دریایی سپاه در این بیانیه به هدف قرار گرفتن سه نفتکش ایرانی توسط نیروهای آمریکایی در صبح امروز اشاره کرده و گفته است که این حملات خساراتی به‌بار آورده است.
@
VahidHeadline
علی محمدی، معاون سیاسی نیروی دریایی سپاه، روز شنبه در گفتگو با خبرگزاری فارس، گفت: «در ۱۰ روز منتهی به هشتم شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.»
او گفت:‌ «حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل اراده نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/78246" target="_blank">📅 23:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=Owb43ZzFMAzdQFVQND8Q8351iyhN3fSEER-oHMlmX00_GFrHGvRvnm6h29DWhC9WVRp8OWnI2RnLyKZVqIYjtTxmKmClhZn9TQCi3uLwtUejWJWGdWTmFhAEqFac_XWxl09hA31ZlbbnbdS25n8Cmavq9sSgYCGc9Nu0WNnilg1k_n-YsOtDRDJQ_2d3Kc49d1TAgEr3yB3DTOPEucFSKW0xU2Jt6jx38m_LcJ3uaJoJ3lK439rDLUml-Hvi62WRq6-I8ow0_VoQa-zO0aEEU-X_XktiODfWU9fIxkxWmgI2iC1dKfg_WEFH5jdyNtCuk-HUOsJKU41h_K39LJ83XA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=Owb43ZzFMAzdQFVQND8Q8351iyhN3fSEER-oHMlmX00_GFrHGvRvnm6h29DWhC9WVRp8OWnI2RnLyKZVqIYjtTxmKmClhZn9TQCi3uLwtUejWJWGdWTmFhAEqFac_XWxl09hA31ZlbbnbdS25n8Cmavq9sSgYCGc9Nu0WNnilg1k_n-YsOtDRDJQ_2d3Kc49d1TAgEr3yB3DTOPEucFSKW0xU2Jt6jx38m_LcJ3uaJoJ3lK439rDLUml-Hvi62WRq6-I8ow0_VoQa-zO0aEEU-X_XktiODfWU9fIxkxWmgI2iC1dKfg_WEFH5jdyNtCuk-HUOsJKU41h_K39LJ83XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مرکز فوریت‌های پزشکی استان کردستان اعلام کرد که در پی آتش گرفتن یک تانکر حامل مواد سوختی در محور سنندج–همدان، دست‌کم ۱۱ نفر جان باختند و پنج نفر دیگر زخمی شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78245" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eir_GxU6YYPqxS1CiSQ1iTMTz8fTYuyjCKdP3NVd9ognwcgMI_6S2xKnuyODMIX1DB9ZlKfPiLrsjuMVdjdRuvWa0Ewe5oWOz2kQ8pnfKkFmXBu41lViRKMMO5Qryysm_Pc_ncNrl4Rp0LncUuhHrDUkTOuGtG9bqZj6jDdho83bx9nXo5pSs2HtUOJCSjMQwb_EEBxpowOh2fftSm-ej72Hp26xePRngIYGyDDtuDjXVBSenoPoC6zACq9jyfvI9oG73MwW7TAyiSRSEa144L9aq1YKzMPDuvr77xyncSAgNyXYeVyTJENn8eEy-X09zozH_oc0FooKUN8CwtBJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی درباره چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها در چارچوب فعالیت‌های نظامی جاری در منطقه، هدف آتش با هدف از کار انداختن آن‌ها قرار گرفته‌اند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78244" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرانه‌ها(مهدی محمودیان)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StqmtmszeHHyIlOzVyl8jyPoOoqpGUiTdUQ45Uo7pgY0rlTu0QGAjDvBevWAtufQSxtck-EDNexQjss2KFB6v3-K2wNsufJ5omZy-nKfm7dTFWeRItL5-Md1WyoSGpi6tGZENcQvvSvipLrZDgTS5EfDd61p5GSSWNS9JlbRiY209Ad75vLfm3Inc_FkRulYE7IP0gM4ixxRKigbfhA5jadKl95ytOxm0IkEXXXMssXpS39PcmsKrCXSquoyqYf4NI5TXx3zglWihRGPGG00qo6KE-RkrubJpO4dwPziVh-Ot_ag86k_VZTBd_3AIo4kMD6RE8X3pv60N_tOvdQQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TA98nnUeDy5mwVGqwMOkdjVuXDyfxfQE3XzQICWOWD9znCpvuhI8t96dhERrLew668vreZVCHt5hFKTuDZYrBkPbGw-6YYtHYnBWyA9QMkn5HbsKVt2iL0fIJhKD6ix5tycr3eDrwAU3ESNUCOvjDIBcTEJDBLeo0YiKfPOBJXPAZ3rLLdbXbCusBSSMp88bqFSmj4kHDKSXJVczjmtKrpkdoSF9oQMFkRuuvtSbQsBswSWCQyjKuDi22snUY1_pIdFXi4VT_6_FIQVbLZrrUq9m3HIXGlLvkhVtXetZqTX6cIZO8l4WpBKkmZ62yGn57NVghpbSCn0UpCrNBD0Bhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❇️
مادر دو معترض جان‌باخته، در لاهیجان بازداشت
🔹
مادر دو جانباخته اعتراضات ایران نزهت میرراضی، معروف به «مامان نزهت»، مادر علی و عماد شوش، دو تن از جان‌باختگان اعتراضات سراسری ایران، روز جمعه ۱۳ شهریور در لاهیجان بازداشت و به مکانی نامعلوم منتقل شده است.
🔹
نیروهای امنیتی نزهت میرراضی را در حالی بازداشت کردند که تاکنون اطلاعاتی درباره نهاد بازداشت‌کننده، محل نگهداری و اتهامات احتمالی مطرح‌شده علیه او منتشر نشده است.
🔹
بازداشت این مادر دادخواه یک روز پس از آن روی داد که او با انتشار ویدئویی به پیشواز زادروز یکی از دو فرزند کشته‌شده‌اش، عماد شوش، رفته بود. خانم میرراضی همزمان با افزایش فشارهای امنیتی در استان گیلان و جلوگیری نیروهای اطلاعاتی و انتظامی از برگزاری مراسم زادروز هومن صباغ بر سر مزار او در لاهیجان صورت گرفته است.
🔹
نزهت میرراضی در دو دوره از اعتراضات سراسری ایران دو فرزند خود را از دست داده است.علی شوش، شاعر، بازیگر تئاتر و نوازنده اهل لاهیجان، در جریان اعتراضات سراسری «زن، زندگی، آزادی» در سال ۱۴۰۱ جان باخت. هه‌نگاو می‌گوید او در جریان اعتراضات در اصفهان به دست نیروهای حکومتی کشته شد.
🔹
عماد شوش، برادر علی، نیز از اعضای فعال خانواده‌های دادخواه بود و بر اساس گزارش‌ها، در جریان اعتراضات سال ۱۴۰۱ سابقه بازداشت داشت.
🔹
عماد شوش روز ۱۸ دی ۱۴۰۴ در جریان اعتراضات در لاهیجان بر اثر شلیک مستقیم نیروهای حکومتی و اصابت چهار گلوله جان باخت.
🔹
در هفته‌ی گذشته نیز جعفر پناهی به دیدار مادر این خانواده رفته بود.
@MahmoudianMehdi</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78242" target="_blank">📅 18:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=YM0LSdHDO_UYdSF2Mp365NMLJNGh0C1Js5hduLgO7Y_fmDzF7zWtKVerkWPoBlpikK5fPpsX-WJYNb_zqYE53U5ivTo0dVOW_SGd_nx8ZkBmYSwD-qqdLtRpXM0Btnhs2RzTsOKWnBdYTqF-24SvkexsXrOJjAtq3u_Ggnf1f7Vm1o1iOu4rxysgmiSfNdHGeN8BOM8rrSDBCiMjCjhpY98SIwrtyM2WCFjtnMd3pcWghK1wT3voesSe51Ub8-bZq7H_j06xnI2_bGLmEKErlP385DthlHtutEuMRrdUet_4FndMSpgyh8nGZkCsJPXoAiLW7uND3k2_19ITaOehEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=YM0LSdHDO_UYdSF2Mp365NMLJNGh0C1Js5hduLgO7Y_fmDzF7zWtKVerkWPoBlpikK5fPpsX-WJYNb_zqYE53U5ivTo0dVOW_SGd_nx8ZkBmYSwD-qqdLtRpXM0Btnhs2RzTsOKWnBdYTqF-24SvkexsXrOJjAtq3u_Ggnf1f7Vm1o1iOu4rxysgmiSfNdHGeN8BOM8rrSDBCiMjCjhpY98SIwrtyM2WCFjtnMd3pcWghK1wT3voesSe51Ub8-bZq7H_j06xnI2_bGLmEKErlP385DthlHtutEuMRrdUet_4FndMSpgyh8nGZkCsJPXoAiLW7uND3k2_19ITaOehEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت سنتکام:
'
سنتکام پس از هدف قرار گرفتن ۲ ناو جنگی نیروی دریایی آمریکا توسط ایران، ۳ نفتکش سپاه پاسداران را منهدم کرد
'
ترجمه ماشین:
تامپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) روز ۵ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی موشک‌های بالستیک به سوی دو ناو جنگی نیروی دریایی آمریکا در حال گشت‌زنی در آب‌های منطقه شلیک کرد، سه نفتکش حامل نفت خام ایران را هدف قرار دادند.
یک ناو هواپیمابر آمریکا و یک ناوشکن مجهز به موشک‌های هدایت‌شونده با موفقیت از چندین حمله بدون تحریک قبلی ایران گریختند. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
پس از حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران،
M/T Downy
در نزدیکی ساحل جزیره خارک و
M/T Stark 1
در نزدیکی جاسک را به‌طور دائمی از کار انداخت. نیروهای آمریکایی همچنین نفتکش خالی
M/T Kylo
(که با نام «Noxen» نیز شناخته می‌شود) را در دریای عمان به‌طور کامل منهدم کردند؛ این شناور پس از آنکه به خدمه دستور داده شد کشتی را ترک کنند، در چندین نقطه حیاتی هدف قرار گرفت تا غیرقابل استفاده شود.
این سه نفتکش ایرانی بخشی از یک شبکه سایه چندمیلیارددلاری هستند که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ ابزاری برای دفاع از آن‌ها ندارد.
دریاسالار برد کوپر، فرمانده سنتکام، گفت: «پیام به سپاه پاسداران روشن باشد: اگر به دو کشتی ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه کشتی شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و در معرض آسیب ایران را نابود خواهیم کرد.»
CENTCOM
دقایقی بعد در پستی دیگر:
«پیام به سپاه پاسداران باید روشن باشد: اگر به دو فروند از کشتی‌های ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه فروند از کشتی‌های شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و آسیب‌پذیر ایران را نابود خواهیم کرد.» — دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
پیت هگست وزیر جنگ آمریکا:
ساده است: اگر ایران به کشتی‌های آمریکا شلیک کند، ما نفتکش‌هایش را نابود خواهیم کرد (و غرقشان خواهیم کرد). تنها کاری که باید بکنند این است که شلیک به @‌USNavy را متوقف کنند.
ناوگان نفتکش‌های ایران بی‌دفاع است — ایران نه نیروی دریایی دارد و نه نیروی هوایی. هواپیماها، کشتی‌ها و زیردریایی‌های ما می‌توانند همه آن‌ها را، در حوزه‌های @‌CENTCOM و @‌USPACOM، هدف قرار دهند.
PeteHegseth
خبرگزاری صداوسیمای جمهوری اسلامی گزارش کرده که خدمه دو نفتکشی که امروز از سوی آمریکا مورد حمله قرار گرفته بودند «با قایق‌های نجات به ساحل منتقل شدند.»
براساس این خبر یکی از این نفتکش‌ها «خالی و دومی حامل محموله نفت» بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78241" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TPWsmLoZCGU_ApeczY-fcK0ZbdWqClWtLXtOUkr_LhIkjJrHF2BIZCipgDeMwPUKnlzFploStsrdy26zawV9G4FE9ySo-ATcOeNmqF3AZRv8aNVBkNwf5r6Qar6Nonpzbrt1dWD-de1HsyPYgcO1bSlKiDB0dvKC-iPTOF9jUA3IhKMb4fclADeUiBNyb469pf-F-NeHFIWqV-7SwD5TmcpYqF82E4lmp0jDI-CvbykbDUvMXcfb8tWTvEQkRrMi7H8aCPBgXM3VSkIu0n6lJtsatNSbTFXgnmObIu_pwUokDkW19VlwV2psmBGaynzPOZmxv_aCJVbxCw_QS6RwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز شنبه ۱۴ شهریور با جهشی دیگر به ۲۲۸ هزار تومان رسید و بهای یورو نیز از ۲۶۳ هزار تومان عبور کرد.
وب‌سایت‌هایی که نرخ غیررسمی ارز در ایران را به نمایش می‌گذارند، همچنین بهای پوند انگلیس را ۳۰۷ هزار و درهم امارات را بیش از ۶۲ هزار تومان اعلام کرده‌اند.
این افزایش مجدد تنها یک روز بعد از آن رخ داده که عبدالناصر همتی، رئیس‌کل بانک مرکزی ایران، کمبود جدی ارز برای واردات را رد کرد و کاهش شدید پول ملی ایران را ناشی از افزایش تقاضای «احتیاطی، سفته‌بازانه و خروج سرمایه» دانست.
قیمت دلار در ابتدای شهریور از مرز ۲۰۰ هزار تومان عبور کرد و طی دو هفته گذشته به شکل مداوم افزایش یافته است.
این در حالی است که همتی هفته پیش گفته بود ایران «به‌اندازهٔ کافی» ارز در اختیار دارد و بانک مرکزی در صورت نیاز آمادهٔ تزریق تا دو میلیارد دلار به بازار است، اما این اظهارات مانع ادامهٔ افزایش نرخ ارز نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78240" target="_blank">📅 17:10 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
