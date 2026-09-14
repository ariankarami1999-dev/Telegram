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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=uqq_nh1DQTLFi6OMhkn_7rbhn6H7c8Xr2IB-0w7eayeZo_RTWjUqAJGUMMUFXP5hW-0ylC71juH9tQJ_TqHlXZrlRdvkeo7xT7x8S8JpUW_j9nXzq3QS8CmNOHZ1lqp1T04N126XMjsCkM1zqrGfkneATGO_O_q7N8ywyZknIgR3ydDT8j21uWYss_BYTor3tTpyh1mnz5_6nGOoNRgjtwOH1raE9-ztYvDtqpJbntTztWfynGLhDrAjdZdCgd-AAt9zAQEquiC3rDHV7ZMW5cfpIlnC5uC47J6DkGCIFDP4N5YlmVy9_sX2q47oSawuexCocnH3MYOGv12zU0MXKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=uqq_nh1DQTLFi6OMhkn_7rbhn6H7c8Xr2IB-0w7eayeZo_RTWjUqAJGUMMUFXP5hW-0ylC71juH9tQJ_TqHlXZrlRdvkeo7xT7x8S8JpUW_j9nXzq3QS8CmNOHZ1lqp1T04N126XMjsCkM1zqrGfkneATGO_O_q7N8ywyZknIgR3ydDT8j21uWYss_BYTor3tTpyh1mnz5_6nGOoNRgjtwOH1raE9-ztYvDtqpJbntTztWfynGLhDrAjdZdCgd-AAt9zAQEquiC3rDHV7ZMW5cfpIlnC5uC47J6DkGCIFDP4N5YlmVy9_sX2q47oSawuexCocnH3MYOGv12zU0MXKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqYhUM7EpsBYSW1690TWjQSWOIH1zMQe3Fi4jGxN6pQ-Q4hCBYNDkvvIi2H34y4xXPj5FTahVQTDT3hMXOIks3Gv-NlWhPAC3aWCgWLmKKVPPzQU6UYTmWZ67HJnw_zTFZm4ZGE88yN_oICf2_Ihm01_nQ24Q6sLrfZx54AfR90q5RghJa9juErHMqVAOABhFkLqVhH7EcmIW0nWWhtBzYjM1XlPw4KCiQlj4XtPz-jzVBPzG2lOX5oGTRV1B7Z55NCn_R_U_mvtDDhwIMZM3E5Z6k34gmBtdhxhuW99lb4zEdN3Zdy0h9exCBrrUSeWQWYuWigIi5NOokOgFYVmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=DAQeec1RYmpVAUBEz7qajepbmE-FpuAvJmMOrOa2EX4WzVBGThM5VU8I2Bx8p62NKSFIuX2VjLzZvQYiaI0o_RcoKcUKYle__7gTiOJXQQnfnnFLQEXmM2IHmEIUo3B9RZb7FXMr4WP8rTOqGZgMtuIWOy3EWefsRvTTdgP6i6-_smJTyYNIfSUitpJ6iESIwsaIpjWdeYDpMzgjMwMIBKPY0mJmOcbTaAQNcFseqXSUWNi_x2O1lYeaevhEIhq5FMJFZoD9M74E-RbjXaO2t7ihhLCKHQeURznqzvLkM2-RUeB2vJK8oD-wf-XV82RwNYwjMM1ukLplmsBB-tY41Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=DAQeec1RYmpVAUBEz7qajepbmE-FpuAvJmMOrOa2EX4WzVBGThM5VU8I2Bx8p62NKSFIuX2VjLzZvQYiaI0o_RcoKcUKYle__7gTiOJXQQnfnnFLQEXmM2IHmEIUo3B9RZb7FXMr4WP8rTOqGZgMtuIWOy3EWefsRvTTdgP6i6-_smJTyYNIfSUitpJ6iESIwsaIpjWdeYDpMzgjMwMIBKPY0mJmOcbTaAQNcFseqXSUWNi_x2O1lYeaevhEIhq5FMJFZoD9M74E-RbjXaO2t7ihhLCKHQeURznqzvLkM2-RUeB2vJK8oD-wf-XV82RwNYwjMM1ukLplmsBB-tY41Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B5OWPz1wlBmxonD6YTNfwYshvFto5UjCrZtFhcPgeywIvLH77NBG_KkPVxPt5ArOA8Y2bt6zapHRYmOosBbmomY43bVPs484-duBDSl-9xdyAxXgq33-TqUyaSdbKrq35u9eLdNhcGiPwKme8lzoKBprf0sHjsuyC-2YcrhkgccNJrRmdvZBui1X-cR4p6J-PhHVjGMfQB9RuL8Qa1y-lpYY2eOaizlQuB0ovkkKQS2i5nCXvSMCXNrSpk-MFoGf-JjqAT6nftOr5ME0FKLupXHxF64uEO44nCW76Uc5hlxzrbU0QwGhJZjcvNTLlNjPspHFqYWYnoLX4v8Ebo9YjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hfbwfEBNpiJxcuFETSUUV8yL4tD8zQhkuWcEm9Bp1LUsyTAWz2vmFxJWQnmdYv3IJH_Z70FMoYQOv6YOqOxG_sNsSgOfV4KTxTG9MUwHrosHu4g971-g8zhZGHN4oArnfE0gZbSTzUzOAyTtHiTmTFdTsVuZWrImXMU_5nQroroBtLGXWYhXUK_TD3Tywjq4XjNybuYJlDkQNGAK9pgLSwCtt-J2YYtaWajsTiWpltNp9uualc60bLk2f5GNnmzSrkxYVWij3T9NeH_STaZ3PA1naHlMEMg8i5LUSbYRpU8FK7CmixO0qrDXacv0SM4IjN1C4f3Lj3LDxlRo9i1bfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwI8zh5Rb1-iQ0OWEcUJCDwJdTpx_yKhdGV-TzASJ2XitjYnZYtvF58mySYa69LFXlFOO3qO7Xm2MUjn7dvDR5DT6SYaNQ7kYa9neYmCafOE8wT5S5J62jFlQV_mV2q7Gay-JhHf6bFyFy_T_1bd26xnyZEgOUoLrpe-PCWkP3Zn2-FMAatqypX2aoRQQkvPqWjnP-5If-v5ZiVlC35fGyLGi-b9Q8lxxrgAes7vsOfyT-D63qIbNbvmAnX6vOZboEedLDkVQCC-2vd4Vt4OZMWHwgBirMVjZXdI47c8qF3hXMfdsqIQ5-qxPCT2k2c2tcfENy3lqYSaML1uTrZN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XGcFQiA7dLZ9o8uqcpJZI2bU7GW7EHMsmcwFO4gSZ3QQrLiUha19SH_QdjJmQVqFc9XOjQoa3suzZnfrIo2veGwXTnn1VFa1MvKLNHbLK4mEwla-_LV3Q5oIHPSFqIXFGVMVBH3xWRiKA2TEAmLMdolzeA8sUbBcf6L80irh7g7Cps90_lzR78EOeuPANL4o9ny-LfvRyUQ8hM_FzyTb0SLvfyAYsxpGbIjdlDo2pCpDi10gP_K_mxD2UsWQCO9K6CByEoWqax2bo27aOj_KO5IBXa-fyKXKtyORALi9KGYGx4XFnFUWgGH7FxJ4FmafDNYJUMgvjb0WrhSzfieNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kPH9m2Gb7ijpgiwP5AEQ9lbYKqllgEbNduqT35nVQxCvwICdF3dlT5_Zrze9ECsvQju9t_6aoKvXDTd3K35GsZowDHAQ3SX1o_sUNEQCNM5no68f7_H4ur2xSQ3Ni1_n1LY_tnwfmHGI9fHtu_fpWvQQMSd9A6bRWuPUb2gOw81cAugZgdGxCBgGojw-PsAFQkp-173TVXF_Skqmo156vK5lvP1k1koQMQecCgz2N91UyeRmfQmykbmvbG5s1OpOazL9UC7LwvoGgfjJc_SzYRhwxDWABIpLy0rmFQwPA9njyjOMz_viYP7gU2gcdk9thsVKuZ-etnXJx9xdwWMnRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AQXbssNUn2jY0R2t4dg62hjchDrt4XhcrscYq0I7Bb8YsnMkFpsZ1wY_V6qrDDy_Ykzi3Ogv5GMsUptbTMwhxFHmbdsL2W5OCRxUi7URiTZGKU-rwj_PzNdOyzqFJqbjQXvcgVodQ_eRkF1Omf5U896h3w0aUTv2WWZHfbe5RIlx-z1Q0hnv2eA7G2kEz_RAcPYUpaqF3dQbRlBoMFOVSrJl3ykH8hrE2GydPT1llo9F-PHhfRp9TNFw9GTV2mW4L09ToqqQKNAnToL0_CZN54wjmnmXQqIXA85ic-pdlgTfLdgcl_70WNdh_B_wxuA47S_mbTfFEytlgnQXKTXrEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=KeZzYeWhsZGpJ6Z2cPpKwvXPEx4wkEKobOkieS4LJNVDiId-cZgJJOVxbN8tKqVYr1s2_fPrtwq9TifmuwMJZqsnWbAG7wwJlfSnGURHW89XV7XGgCXhYCR0pvSiuc6A6rufExSllVzoBU7Cq_El1MEHtKgwwgj9s-yCKpXstro9KVK0Th7klSUbHg3TOrvMN6vavXo6dwOQx_qLobFbHKkeHBwAwGfxXEXaQqjNk87cCVp9YVUnNw7mFaWh1xxQBgB-f-KswycL9cRTvPN0b7E-IsYQDdA4TFUoL2th8bSsfKLcf-LBL_v62Ib3S6CqM5KK3pOZGxY_kFr909OEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=KeZzYeWhsZGpJ6Z2cPpKwvXPEx4wkEKobOkieS4LJNVDiId-cZgJJOVxbN8tKqVYr1s2_fPrtwq9TifmuwMJZqsnWbAG7wwJlfSnGURHW89XV7XGgCXhYCR0pvSiuc6A6rufExSllVzoBU7Cq_El1MEHtKgwwgj9s-yCKpXstro9KVK0Th7klSUbHg3TOrvMN6vavXo6dwOQx_qLobFbHKkeHBwAwGfxXEXaQqjNk87cCVp9YVUnNw7mFaWh1xxQBgB-f-KswycL9cRTvPN0b7E-IsYQDdA4TFUoL2th8bSsfKLcf-LBL_v62Ib3S6CqM5KK3pOZGxY_kFr909OEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZw2Z1yARoD7fzz9rGozbJOjPuQEe124Qs9Pw5brtfx-SOcPLOrowy6xy3TNxnAfTWAlGnEl4h099FjyRvIFs3uljfSQxFX97nOJevaQKjGOLwLBgkcQoAcp_WSAZzEPEVJkwypli9_34r_HYwFFH2165Xz1aCPXYsuo3Vt_H3Ewv_o0ISY67fjhYaQDNXFRKI5_rhue0wYGz1MhoGzkcy7YvnVyh64OYNdXDXRxqXODJteKGDTIz6V7qu_XtqQ1_NDrScKeFRQ8dollKhtFor3vVVCVsGUu9zK7iwvMDwTmsOL5PMKdoL4Jilk2440uIRQMMT7GENzGKkHiWIpxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qiz5EvDT4XqZKwhM7N9Prqo5o8xNdK7hrlLU94bZKbHvNTnyAIMBoDTgIp6cQGN7YPbsnzE9REIcocg8ibuD-j18ogKvgtEHxKlUPltljmHdQX9QZ5D56AlDhru_yy8hEljTmlP3pqhCiKvbkUjzV40kdii-iWU91rgVQlbg4BodnoW28sqtM1fhc9qYUsVMktwasYvMgzYfoDW5gMIhaUp4kNPTAavaYX420VD3lqoPHlevJdt9e9QmQEHeYArkRVfJcZqbmSO9X5ZuKcIhajXNeqCNPWbH9FNeQmcctqBt--v1_wVNWMYHBEBcCFdP3F3brO6dmvkFTvBWDuqLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pIahZmXZG-hdy7OG6Zgl2DwtQUKABGRYDIxpFj6EMFERY0YtygyxeJVaezKBDhBNCs-u4EVvvGx7WKYTAhIEaqL8oK5lOfiDCHmrZEJUNyh6LU209T_wld64Qvx2ED3THQyeQrLYM9YsXpwLZDwJmPDHyPidRqNYFoOAfAzqZgi0o72eUXwnIqBq5drjg7v5UklUmhrUUQfvF3-qVaEz7UgBqcIlfJo491Ad6l6TDTI5ku0pLHrXOJzAJUal4urMcqStjV82ToVYJj42ayWLXbbIweFbbNXFFnF41z7ci9AJQLyvRpBLio4wb5TqoAKuwdvCxJV85-srvW3IVsU-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HzE1vF0qlDdaWeA4dtQL3d4B6mCDmxnBDmnIpQYp8phhuKBUx7OdBKuyqeC2zcpyDd4AB16IeJqRlQpjgNsoEQ0-kzA39jtY6KRw_FDIqamrMBqbz05YvaPPIdkN1Z2yk037C7WSbT-n-T8aL4_7BBedAw0NAef8dM0Qdgmz-zXOCdwgrZmEFt7Wb25jQZf6EC0Nfc0bWAzoeSEe7dGMdLVfqfDj1HONUBvfGtfXZ2mbuxsIJ3ok3MoEGdbVImpg-xR7I2gj3V8v16kuRuOmMXVTn5W21CEE-0o1Je1l8TdcR-p09JYmz313S83Ml3tiSphYHgdSRkG5Vh_afHKb1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l4bJkKO_Mf4C0cgVYKz2u2EX8lXkeEO4JF7Ys-8C40MQE_f3v1QqG_vdEmh9N5e5V6EWAZ9FWgZ0G4_MsxbJkVWopeH8HtIcZoOH-yNx46yUwuFiABAlxqIXuMZFXVPtGMfUGz66Z7AJjokeMMpr9el4WewejIVeMG4eC1lKKRIYvakR9jQu_sasu3hhu72gRNjJccQYt_8bny0nuj9-izeZb1q1ULKc3aXUws93q0JrzAi9KuEc2eWglm7l6RjgxDgas5wA9NySKvMeeUhhtztot3ktZLpSJckRKjig942OQjYkNbwpu8iU2uaERSuN3WylQ3Ue6obEb5ZOqmXroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DIfcHdEzGRwBNmhmgrnCbTJPINpGMeg5jykWNDwAD3QLNLsZtFLG2uBuhXtzbkxY11ARSozpbGtAy3TwTgsAfvBQVB4XWo3v9usbh_jsd0XU_U6T1UWBacjlCbhrfgVw9_PD9pt_Ld1BNzTK6NQP2hHTke7KlEJeBmf0-tlpYBYQfrGWSomAS_2qL1XfDylGpDnfGZc3ts2JkpeiFt_fhQBurT1aLONlEBZsr-FhOOizZoTHmmqSvfvfxNYDxOIs2DZJ8aTzmP2ieTn8hoqyRNymyVH5bWWKhR_JSDTDxlxVSj5H15RciNzrVBaOIBSunIBx3cPJ1_byFo5bU-YfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vs2C1Wf73wMu5cDH-Jig6Sz-Hrl-gly34rvdyrkODYoKkXABeUQbx3a9ox5keatLmo-IIsSljqXoi37X1bGqkssBHfjSoGK0R0-UPtKojNMWfVAtkKX95lIjFUWbWye5mcwBkCEUSOuMr4zVctgwexzTW1d_gbHcuFtq1JPoIsS1jCTlIDfnYB3C2I08lK3uNT5gCb_yfLB62V9A1_-14SKNybbcGBPOep7ETE6TGRDHpCMk148jfmd2_D_s-mRxZ1TH0uozGiQUOwnml_HtwPEpEEKT-2M2SfJasM2-wk9v_blWNGZhfPkpk7oFhBdDyxYqQ3mYtWNplLT0XSbbpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=FYXZUw7MJcAOH6E2YH1_8Y18rPl_0STBIXUXbfVe4UTdctIAUGot0CbLMXhqnrvERgxzO-aQ1CP9jcYqgtSq1lK5QgUbLalrbCZapT5ku43YRAh5VnltY8a2-SSPLDnd3lHJ3MgtT-2uMyg_7imdxy24Skn-rXqrhp_AjJZ2NSXedYjoxxVwGhVW02asp6AvTwDX5MhDR_n3FrjFcaWQ33t_DJnXi6FbuHpagBwaS3tVXSm7ArbK_lFYMXFPPFgvTL2vs9bBhzk-66AKonnd6QW-UA_RCCstDJHLOfI9ud7e5KtNGqi7U89stoCRx11sC6F-TExX-2xm5oPtjLSg2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=FYXZUw7MJcAOH6E2YH1_8Y18rPl_0STBIXUXbfVe4UTdctIAUGot0CbLMXhqnrvERgxzO-aQ1CP9jcYqgtSq1lK5QgUbLalrbCZapT5ku43YRAh5VnltY8a2-SSPLDnd3lHJ3MgtT-2uMyg_7imdxy24Skn-rXqrhp_AjJZ2NSXedYjoxxVwGhVW02asp6AvTwDX5MhDR_n3FrjFcaWQ33t_DJnXi6FbuHpagBwaS3tVXSm7ArbK_lFYMXFPPFgvTL2vs9bBhzk-66AKonnd6QW-UA_RCCstDJHLOfI9ud7e5KtNGqi7U89stoCRx11sC6F-TExX-2xm5oPtjLSg2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZDtxkdnLfFX_mvR-ahq8YXKpdAFrTfyZPsIWbt9kP3TZuHzkEqey0BQbSf8gEmbtZV-LVfHtl-2PS6fVgCQBTa9LScjeCzmB5pqaeiM8MhqX4mLrn-pkxr0Q4WREfz-Rp8ZAuyy3PV-4XInnkdHqtd2mWvX2qFZcFsd7zE3tQj4LeqivDVFShXif9qwIH80K4CO1WdG0vaRgnkrgKqjStOxal9bip9Qpxn36Y1jNtDmeBJbJ7EfpEGqGHBvjVu09IFduxz7o3Dp_lMq4rU3zl8fRgFLO_EKfkbhEyA_o024PJyNbd_hm2qt4GdETBv6mpJU6DUtGZQpnSB8EhsXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfCigAYjEPWeKd81EZDb7SivSCOHymbVPvTEC5Y8VtrAM-3LLOJUjePuphGszwb5TvMMTA0UEjfLMa6DWFBxBwhF1x7omIWigXkoDwctzE-Dyx3sjdKDDy9g8IkxY_wYaeAk2lS6xgDpbuVH0B60KtskEF_VFmjtPAbj1lIC_KB9t5Ty6E2PdhDehU0AlVgI33VlgPfB_Mg-aGAplFljLAhk3_GNp_GP4OCxO3nIT0YbHxd8ieal6erDqVtL7TRir-EhcO2dCYogthAKMEHPDNL8Ye-biRPMkASHiPEICeGk0W5AYIyHDNqo_vwoWs0H0-exikF9klHGCB6vziD38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syGTsGn2F7b6vJWWpcajQhwvY0i9twKN_TBHFf_chgZyrpL5tW_4rdmNNpPJspl_fThT6YOb50C-S93u-H8ldpMY8OU0_ctvbIHQFtS4NGRC2NwymJiK80yBrLXYNAglpfbXlvM7A-46PYonMkj8PBYhh6OwTvVCtWVYi1gxrqZ_YrLiyk72e31aMVE6r_JAvlnlDRAa8CDxP_1aim3ivaOxG2eKXRe_0pJSZBUmtJUl_pUBoSPA1_pwdCmsTOJhcq2HQ4x7Q69bP8xWcnrL3eYzvADag6A2Nb9MR1oqFeLl7ltjwJwJ8xiNCRDeW8najQswNuUDtlbOjx24-1-gag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjRCK3z7e8Up6sCFZo7VzlZ8rD0SAf5oaxhZe1Q6WtzBhVbLVb4wjxxWonSCZsXNbRXyVlCdAR8DeNYSF5b3tywb5bQC1rNhKID0RCAnsjpL00cH0FAMbDIKVG_uJNRKjbTc7IXocpMo-rnGVNw9odPcbBWPgYD6H8-H-BFOPDBSqp6gi4XyaOPMmx3aeBC7Pq_bPtmWmlGw__Uh8rHRSnSmlKm5teHOlgwBDmjlOVLBrTiBmZrs-yRRujfIl-mbDyk6MVigae-6PD_Zw2-LVL4cGgNYuUszIgW-xxkCvmvixcr64GRPWfIQ_1-z8xBYBZoodyeWS6DgJgtzHlvM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Dq8erU8xwv278PGDf6ThWir1F1Y1SrKdBaGByfKP0AdLPu9PO2fFD2VUJgxUIJOyTJYz5IV65a2Y4TmUS9Fdga6FRNrWENYSPoqFVtZ9HYc-2Mdq_WTGX2HefgNhrrWDdJqsQFqObraOxLryhW0xLWnkGWWkHNOLyblb2PGLAfBkX5ykI6Zuz5rlohzKQMxnh_wFHO2Qz92-PCQYHjcEljiqQ8ArhL1qGq-2v0hNMMOj4ieOiqgN-mPcVzPZZp7T35imq7bHBnAvv8VgQCLhRrP6PLNoMOr3xY-scoNhErxdOq1FkaK3EC_cLJNn1rkYHltCyAHLXhuzgE1CXns0Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Dq8erU8xwv278PGDf6ThWir1F1Y1SrKdBaGByfKP0AdLPu9PO2fFD2VUJgxUIJOyTJYz5IV65a2Y4TmUS9Fdga6FRNrWENYSPoqFVtZ9HYc-2Mdq_WTGX2HefgNhrrWDdJqsQFqObraOxLryhW0xLWnkGWWkHNOLyblb2PGLAfBkX5ykI6Zuz5rlohzKQMxnh_wFHO2Qz92-PCQYHjcEljiqQ8ArhL1qGq-2v0hNMMOj4ieOiqgN-mPcVzPZZp7T35imq7bHBnAvv8VgQCLhRrP6PLNoMOr3xY-scoNhErxdOq1FkaK3EC_cLJNn1rkYHltCyAHLXhuzgE1CXns0Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I__C6NZJOtKYUr5RxLKLbeNiqAjGbVcPPiJzQ8jltWOK_yMw0rQ8yB8wbiLmrd10iO8jGAaNL9XMqWDrP4zCyATtzAD-_pohLI3dZkQMmyF3jmt6sxtMoe7YKqMJthNu9q0ZhnVHm6L1cMMrA1M9OqfCf6nSFLQVKI1JmXBJHl0g2avLdwNXBVaV0DI8RjftPkmOQJq-7YyttruMJtJAd7yhx6kmJg-ZoQ-vSeaMxfJqBsoyz_ocmG6spo9ZdTY9K0rQSmnabqNXvIpZIasP-pFNy2Ndy2P8-xmKGAJmFoDwOqmtd_aaduVxVRi0u94TWjjbjbHTp4sxPxy9utYqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iz99V8Y9dJ3U0AlDYp-Yu0XZB8aBWtpLim739qDo-yx6VGyiubAOeU7DarsXaM_tr1BU_z8CwOGDvofXh02q4Qms13Wvr9PY5pMS5PpO3avBFNBJgekwzU9BxSAaKUvmjok7MjPdjmd-wz72Ur_8h7NUznaeUaWUjhb94lgf8Bxf9UNvgTDoaVzVO4RerwemLk2CJSPZIXYYBvHeiJWlwuL2k9-UJQDIOimu3aVbdPsssiaz6_sqn16Uj1htkPQF0ieUCqdeq5RoPjenQJNMTpk4s0QtL5k0FZ-lpqoaWThS8QSr22B7280rGHkYROGPXT_vu2E_HbreLmw81LxgNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lfUh84t5Fd8b1LSQT9Ka8_d9kV-WnK2vGvkdkfuNb4UdhVShOc7G_nW1plVtbPzeUJisXK-FBE4uqOQNDy45c-dklj2MlcS3uPAB9OyoJde1xdKk6HnwHNP_g5WZSUqWYkqn-W-JhK4tpFr2-Qkod6JxLEvCA7tB1zDcv2pf-LqYQ6OXB9Y_AiXZachGkVKk4UB2M1B7LfOTioyanKYvB4glI1tJK9D5VdOb-C944C8ak3bC87fY5Ahq8rrgHEQWd9b3TkBjBTDbtPw5hamfvL7JIu8DWtWCalPTTvZqzPf25kKMEi674HxZSXBWxStcgwNovcHXjSslu8Jv4PCPoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nAWoAFGmUQpHyMCpmTV9qF2XE6t59Z_fEhDg8-HKATizIacM6w2CEwT9-gimkO_h9c57kyCJkUrhTyrmrOfZrAn0g3GTKQ8T9ijYyBVq0R-H5vm7wntPqWNesU5w_4pDvFE1nGxRaPC-DNdmF9yoYVWgn0CsbsIk_sqpAOdDtttxupTXTQhu1DTWQt0rkw1Ry8Tr42TixkSZzpOXQq1M36aV1679-Ef2y0FcNfV6t__5FpEIhRbrdj81UzbiAjXbDiiqr8ImlfSqtiK88cJhWAlmUTD1MgvkVh2HpMJeCJ8Ck0JQOzvOxr0VzCBHZSsapYtee2qjbCIoAwHK7cQSQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bjg7_qm6Q9aqrydPoqXmLYBCYY9q1qBJccEkXY8yhIbpHKgJzDgTvHGzvxgeE9dTjcS-ZkaIhlh1-MOpTxhYApZ_O-a-DcMxaN6F3dbWP_KwrBy65EnNv3EaNulAH1jCpwA1kMOwo4dr1yurlBEpzymegFaNh8Zjp_-3nvMHuWAyxpdJnhdGUyxitVaUPxc7MVJj8q56tgDxOxNAu4nwSOCKfSt7e_FTz-VC3PHvUMQSlClz2CAgrN1YkdEqUJzYTc38TgRx6t43ocY9Cz1Rl0W0n3XTY7VTMdnKHSMtvuVMCJXmYhzToUD1S5tYVU5a9uGNQ5SA4qL4c_6dkCdi4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F0umtZm4kTT26Qu2NtTL8HHqasdghBiiekFZIIM-uZSJtyYVzSFIU-DXeACmDV9ggOhLWKLaMKtQmbyORHBFCh4HG-qnfBv5AjtNtcpGXtNq0S4TaIU5ho2FhkRzKMdvBmy1qCPX9ObHNl4awiXOjYAslwLwCNLrN-yszACO3oHBUUm91t184nNDegY93YZC9tvXF7ZwdHCNRWjbYJymzEOQ39XJEECjApBIELEljaEb8QohRDxxUAgkOP_52hoJ48YBEGaxb6L8QQuaEGIP9alHPxnVujTT0c0mzjWwaUXwr_WCIo_0GER6JUTu5p5SFEZnCxykgjoY2md0_q9kGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JpPoFvE4oynfiz-OcV8r8d1DnlPnLs6B1UVTuC1mVvowW1h35PeSKIvyFQvW40NKaT8xWMwE_TR1tBKaFNMvOeVTSLQrcbewHPsJt9i9A4HtDlQAlC7BnkpGote80XWM4NuB4Q-nKCixihpkxrw7RT7mgNqkjh1Z6GwkVVtyDT2kNHmLZxFQssXf4uscW6izCAsZEljd9pf_SkzWPPQJPwbtlz1qhkmdcQonLYfbRt0v2vfMqXXJBaHkcURaIiDsMQ5mpU_ZV5NEeKcK3aESfHEc-XLT7Ufb-Lim1qZ47K5k39Z5D2gKmbYVm42b6yNGb9txF5iDupNRFn_A-ECRgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIfAaCeI9-6XdWlqNnwUlcIBsCBxRAaidjdZCFrSj6IlsAMZwFSOC0crgNdxvwCJWNz5121WjyZHxtbU2dsPZAe3gythszWzgEMIHZKg4oj5l2NlnPIHRkhHfiXQCu1NCYtNjjWjqTAYNWn7Qf7lXj8DX9a2K8Cgi6cw2dvYDq8QoJrWN80XRQaJfaKGpqZ5vxXyzweJiyso1J0uEksSeIJZh5-cSrP80PVvJyizY7qkRw1KaGkfDRtP9QqxhypGdMsbjlcJw60EJbcxajucYgQJrmqkZSEoN84KkGVjVE-BreyStVZ2cusQ4rLm2sMNvE94X_wgw05q1hTBrMeCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=kzSPmz7jPN5JOvKgDmq0kotBODueSyHqzzuCjFrtS_YGJVPMNSM1lASzx9_3x_IQJdRlwSn3SS5F0yilD28GZn_yE6RTsfFeW6H0u-n7oMSGDECojEArpn6gacdoLMmr2Zd3HXiR8pvK6ELbiynJd5wGiRMCHJxmdizDB2ErllmWnnLsbJ7FWAfP3LhGzSVcWMdwl_K0Dq8ceETou4NLmQBJqLWXlLTBm7I14JID0c1qNv0acBSO-eIcjkqIGTNS6jI8GwV4ScF8I_6E-YmMQjk0lh8zvzaU6E0LobXh8C5HD-lvpH3tcZ_IC7XwihikD0cormgNUIXjAHRw00W1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=kzSPmz7jPN5JOvKgDmq0kotBODueSyHqzzuCjFrtS_YGJVPMNSM1lASzx9_3x_IQJdRlwSn3SS5F0yilD28GZn_yE6RTsfFeW6H0u-n7oMSGDECojEArpn6gacdoLMmr2Zd3HXiR8pvK6ELbiynJd5wGiRMCHJxmdizDB2ErllmWnnLsbJ7FWAfP3LhGzSVcWMdwl_K0Dq8ceETou4NLmQBJqLWXlLTBm7I14JID0c1qNv0acBSO-eIcjkqIGTNS6jI8GwV4ScF8I_6E-YmMQjk0lh8zvzaU6E0LobXh8C5HD-lvpH3tcZ_IC7XwihikD0cormgNUIXjAHRw00W1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=MXcQF3ntznIM-RWeg5XwEzazvumN1aKjWsMcI9bPK0S2KLqzf3ohEoZ8JaoZ51xJNjrJVPJGukvjqWKXL2H2rSGZfqZDx4RS_4ue0Esj6F9UJDveoETxZxihdGB3SWQNoavnnn6k1GByrh42h2DbZu8lRwreJyH9ZOHp0b9GmdJaclUrXkkHLAZiV1agzuWtlgLhh7isY16kUHpk5rHMA8E2UNmPEiFywqO1IokLI3kvUklxMrPIa2eNuKOGVFhrPPF6EK7iE6JQm8RFPOaYj8va8THU6gzymalbm4V_TzPVM9WVHPcDlquiJEN8pRa6VxBGGtp11dyGMm1UDzA9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=MXcQF3ntznIM-RWeg5XwEzazvumN1aKjWsMcI9bPK0S2KLqzf3ohEoZ8JaoZ51xJNjrJVPJGukvjqWKXL2H2rSGZfqZDx4RS_4ue0Esj6F9UJDveoETxZxihdGB3SWQNoavnnn6k1GByrh42h2DbZu8lRwreJyH9ZOHp0b9GmdJaclUrXkkHLAZiV1agzuWtlgLhh7isY16kUHpk5rHMA8E2UNmPEiFywqO1IokLI3kvUklxMrPIa2eNuKOGVFhrPPF6EK7iE6JQm8RFPOaYj8va8THU6gzymalbm4V_TzPVM9WVHPcDlquiJEN8pRa6VxBGGtp11dyGMm1UDzA9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae2ehLk0YXl47tOUwtAUl64u0YzYA6gwdBmWOuOEmGE-9NcPPa8FirZYDuBfOCMJ0nkGxANXcGF_BhCLUntL60XJMNTW-KCNIcMmHAS6adulujxeZJ6eFNg7LsAJa-IMlDnf6nDzGAHY3SssvaPWpdkqbWoLRLlb9D06hrZCqj0pnK8ua70DiSnxurt5580EQ_0vh1OK_0FGEH0BS9_x34rR8GBO_ufoV5fr0vYcdutTiqJH_gHNSoflzpHFIKe-Pbd6e4pl-F7UgnjUWKBBPP4UXVphNr0TFVD2iw6pMCsxR_dZtKaIkHlSwFSgncn21hFOoy-YH_UlREhDtqnhmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIUy6lxhEzAgROnNfGb6SFp8nX7-EeykZ4q0xm16_fyu8cMXhhQ-inx5OB6gncTOVZ6usxRW6qT4a8l1Di9QWaw52mF7wYU9C7o8O7CCZr4et8z3dBvrQrApn1ktQFodusw_OYZ0zAaf8X_0G_yGoYQHV9D5xai8iJRKc4VZRBjBk7oUFeASTXmDHa5IUaDE6eS4jHgUYwivQtMUlAl_ZptcQIE9itKLtH5ts8w1oUgvc4HFlpFaBtpuryhRiHCVqPlTx9AJqtO3vAIFIV9JnWwOH0DSs9Os8yqti3EHaJnOwo7UAbfhmHb0rTd8hsRwg8p_BCODi3PpfR3YCnm4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5B0RnKDfxgWhDqSoJqaoNMzDVVbA5aK31xZjtya7OfNFLHcFA5lhqo6AFB1tbknJcQfvR1drm4nN9FXz6LtZffqwpGUhckbfwfKILZDrMt_py9tdWkfCG55hXZX6qWZf6gyN8e_eLcjLccdH0V8dIUbCGo-djMISpSO5JShDd8zXSgWCE5sOg1VbFdD2wH5ohZTnb8iyd2TeQxbXsXYbU9ZJX19HQfhbY3w4jzt1trvJCduuC2IM0aMG0pDE8lNt4j99pjzFMIbSKmA2SrdRyvfzlATsIrBf4NzV6Q1qx9nMRrleJyyEAJHLFpNvnGCbMps0i3Afmq1-owSRNqDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=qWaBGbMBA7cbpupxCooABDl4wZV6ZasOZrqNSZViXAP2gSbpPPgf9Bf0W7EY2xIrKEQlk8SbnoVPJFpL8VGAqXA_Q7j5zKEyETnW-Flu818NCMwC1fVdIywYLOhMQM75fomLzXpdZWg0buEeiXa8ewY-Y1lUzJkfGgntdpHRB_hX3azIcdcp6H6-gNFoEzCDTTfWe9tRD-Elyy-ZbMUOTs2IzfwUmt2HW8G_5EmmcVIw_varHSozAplzGXlJUuQUTmJbtk4et5HKbXly7Rcjj2DqYKtvH8wCKx6hF6E_lQ1-Xq_e232UttfOlASQPdNS0Z8UJCr1K9NdpVrte2SXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=qWaBGbMBA7cbpupxCooABDl4wZV6ZasOZrqNSZViXAP2gSbpPPgf9Bf0W7EY2xIrKEQlk8SbnoVPJFpL8VGAqXA_Q7j5zKEyETnW-Flu818NCMwC1fVdIywYLOhMQM75fomLzXpdZWg0buEeiXa8ewY-Y1lUzJkfGgntdpHRB_hX3azIcdcp6H6-gNFoEzCDTTfWe9tRD-Elyy-ZbMUOTs2IzfwUmt2HW8G_5EmmcVIw_varHSozAplzGXlJUuQUTmJbtk4et5HKbXly7Rcjj2DqYKtvH8wCKx6hF6E_lQ1-Xq_e232UttfOlASQPdNS0Z8UJCr1K9NdpVrte2SXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah_rZIa8SQRcLh_z-crK1J-Fvcx8FISBZ5Lj7kRnDw2C0TdZb-N_7_xjB9ivGQOlTy-B9PaCbkcmxCbKDCBNvhKPQxUSsyY9HuE1A2Iohc6iVXNeWfTc6tJ1xrkINBOpGahXpShm66QiTJlr6wlwieBNfgQwqsiGenwVg_zA4pd6-Ch5mZm0vmefia5RYuT4P8jsXmcnANNzabszVY184_95KAMWYybUDHtL19wK-nnBEZn-9PzNmFSUDvrd-ltAagDe4ZRXX5nb_BH8ITeAxtYdITmUvfQt08oD28sgjeSnKtk7-vHl5zaEKpVvmTSq_8sBCPTOV1blvuusJzApMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oChvXm12p2csCXaTnHgy_nbORxTGnflOFG5uxwwoVuPd_SmdKsooKD4YqmkSPlv3gLKFfhKhacruJDdjGU2JCA64NGvDZOoQgvq9SiafBlg9TsQ5OagZ1P3xJpzYyuqry-USETzet3Qdbw5Xr8ZPM0Za-bqNek1dodVzfu06v4-5sKDRxxVlvrLT6s7eM119fCGtQEMaMHkWdFGA3LelzpHUnf-f-76Kh19W4mYIrPxxkdKz73t3iBNAsiFd6fCU9bhCFQ1ejwRRGS3iFkMzUrBb_h4UBXcveRvzdTCh8jDnJ-egLAUc4TxccIYDQ6yyBw_4zgTH64fcQRCo7U0y2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrmVDG2xP6re1qMdVll95-vOwajr5euaTE6c0fabCBXTq3HBlzQ2jR_vVNQu7lnqcwDYH-Z00OUPVDmJ2CudoMpgySZniGaZWhJcQmKAkpD55EBcyUDZdVbxCMln9ssSbJxeqt9qvWHQulIo8sCHDMz5I-k-Jo__OyHxl2zQQI4_GCoQplojJDK7YP4UJB-sUTUMIdUtgAjrbTY5KfhTuU5t4GNcSAaQA4hGehh2_SojERumWPBEWqsNG3DHFyCvqlY02JOMGWfyXlPETdITfRvt6K1u8nVMYW2w3CAs1kNtvVU29ovYcpSbq1Vo3aWwbsaYrkODqnj9gAEewwnD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tf2HYyDCKsC3FsyazpRUDXmgUr1SejksFw7W20-uD4xDdJ8oKwHsiKS3d4oC7pxddk8kA50ahz6Qv3ePKb48iHu5V70z9vGrxEMlwKKnWki5ofjCrthpJqxaOU5vmEKtx2O73BnRIzM_X3pWy1TiWXhbmn7qdP2PAm6-kSephzYJ8uygcp5IJFG4nS86Bq7vZrdhDna0jN03P3pCsftk0g5B-Dk01MNq4vcuTmoVfA-ll8p39jkxaCrXmSllDb-6MeO4v5NiPMYaVYj9toWcfXDOkcPHeUTc414u_PeeK7lX4jlfCC_Vva4scPKQdUBjVuf9SMQCADaBSS7qzHVOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCYA3EofFg6rYNBV_v7X4k45vta0xS7T-TuJpwCncqBEx8f4CCHnGRf5kj55s4a86bxjkdeWXYXILCVq4SnUdcD-xSZtIz6C7rKPDyjxMXIdO--haiJPZVlYccTsn91TInd8TCVpyhf8m-WewWac8lCdnvGkR7EuBDgVoqhDoPTRH6j9jzIoLBz6QenLM8GjFwIslHLjBAaovxyUKrIe-kNgsHmS8hvp7nmAW2--UrK68nkNpn_VMsObbUOBFFRPw1YzPMVBhMqx_aeHyZlwDQZaqV4V_LF_YHg_m4T5g2PjjGUkzOX-hPBMS8iy0YTNpTU4L6s-kD-x4Vh6bv98SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA5Qvjr1BV1Mzw_gkg9l2MRyBUF2kzyJ5eu-AOWn3PD2U_eMrFUT_1eBIfHtqXcF1tpL-_Z5-bLJi4MQvvyfYPeDvbsqaxI0yX09Eiwvpi2Mzm6PJjFeQgTEXR1Z1A7V6uXEZ9eTnQdaJg6kT2x1VWy8TdidKcNxHAIztesq0nUlHqfnKRRPA5F32KLeuCYQJ9j-R2hEkq4YMJBbjprJboO6it4nM-iRto1pqzTjHMfcuTimAKtjb6pd6TbkHAWZnBRfdBney-rCaNcHA0rDbEOgEnH49O0kvaH-vavQBth4uJR5A-GA1VJi4IC80DnGYwPLAwSjzG4aB6L-Ec-btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P17gpFpfg5LpIbo1BIrpbz6dhZkhhV_yQxW1JkSjvO7jYI2Orod1AWXZ2ZlnKzeZK4UTD7vvpz14epTaKfOa7jubs4rc_GdlhtV_v6Ov6ppOqsRfKXB61CyqephPrIDptKqt3V8OLbDYKQvHGn4vPtaC0l6JuNEczzmcKg1QF5oAah2Rcy10vjwcmkLAnuNTemagS-cQT-Mxa7Wfi2A7Bm045p_6FAmVAydGqu617hD_pXvkvuSSCWpmEh9bNS5Ag2CUQ2TS56CZGuV2Gb7rGpuprFZnTUg-aRRRMdW4VJp1_YFBqHs78kYhz6iGac7FRuGXXNMuRhNU6SID4Y5zBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TAkpPi0hoqHAgTR6oWgqCbo_eJXnnnVMPbIR95pBEYz-hUHKl8Qp3wL_XJGBXlQ7mtkAU4U9aoXPJkaJOZ0uFOnc7f2hzVQDB_t37_VIiUA6Rw838yY0noaERu5Zj19Cj3VEyZD2Dw3urAEVlHUBT6W3pxy_Wk9aJjlxu0PtuRLET2U4fUDt4NO2zeczNutHSzb8R6ZxU-Z4uaXQ2W56buh2E87qbrGuRrh8Jtuy-um7u4FLoXR2iyFmDF2Oxico2TfJYdcJ-lmuvMXxzCjzNfYbk3sfl7OXTZ2AzmVtrQxG1pNj2NIyzsU3HJq9UHLJZ0uZeZWg1qdLfzF3ctI7yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bG5M3ykv7tn-bleq4pqEuoQncOkR8ZeS5xSsoM2QP6JdxEAhj9_oD9xRO-SlXZbWcd-T9qMVFs7Db7_KFKyj3BksLiW8wPGwfywTQt9ZjkAyVgDF52Se2NF1696bMydGb1-DAo2Jx1GXyO12aT8wvdRHvCoUvHEjj3Tq81-PQp_NPjdG3j05uqHtHtD1YFO3DdyDbuRpak4Gd33HjogFThXKxl-JqWQYADNZHJHve3vGWavDnCijdxC0IfJ9DpYZqG0kok--sK4jTQ1m99OlE2ETk6oMEW7fl8IVXDBTuRKA_Iko6u1_VS2idSwkj2ar9ZUP-5zVUw598Cr1iBTX8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cJbNQOxfTXVUla8mu7A0giOFNIvo5sCZnSH1dyC7zcZAVJDX6U7Q51Uk4-B29_FcZD7oTzskaB_IFCk7H9EqtdfuvfsLRtOKuJ79eGUSpJkzvgYT9gNsU-13ELlpFWOmOlExStj22KJ1Vl9LTstaKChWnLoAG8MoCZAKjpx-3f3a9RUJQu6-0AtckyecwTFuXGSVjNjm4X6mj-ci4Az4Cf2h2kinuAdhQptiNXNbRiS0hnwvE7i7lOkUWhHOkpfTOzQFN02c8ctSTbcT8b5psnUhLUIu97PnWUC5pWsJqarBoTQc_a01wNDJ-klhikz0JqG_byPf-KstaMkRzDn52A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GkTRTt1dPIfcGMzMt_qIK4he6D5FdphPnoqN6oc8kR17g2sg9iBbYcUu9C6Cd8BWOpWpWvA3XJrG1vZ6CNMVPahmK8MieSIQs-mpcwW9f_eICVCULtv-uSPeMPwW_1FvNOAIfao5Bpl_rKQ-uxi9ouh6lW3sd5PHVaM2gamwu0eKARvGeCb-6bsh1Xv8kdPYUnjPljmuBzDJ5QivfRAnr6PFZ5bYekIj_lXEGNXoARcx2RJN_FSJ7QXjvaJCfOYjdTWGRGKhOtj_B9Mb564Z4gcavyjzxtpJxk6ik64CTapWn-UM4FaB_aX5n_buzAAjIRaRh3m3RUfHg6CmbZOJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctG5Dc0GVhBz_tZAWbVsXrG1pzicZ5dywKoKQJ2dlE3e83Pdbu-KXiHcMEkHd1EHpGb2cw99NT0cnQozh2xdMPJoIigmla6ORK3ZhJ83Q-UvsZ8XKBTmoJCSxe14e8MfGo7tp5giIDGYrkeHx1zVozcAgOqh0qjZ9I84r473RmyB7evblztBgQhdu47Akr1pHzmJ82xXldPeTtbNn49jWeJDxwDrbDZCLo8oCM3HbZ8beAtS7DyNgpX756bJyyxYqIJSU2sHHnYpZsrQi5th0WtJkirvDBR4IAXbrPd-vO_bCZyzqxH59aNWUgnQxAcia5lIMi542CpTyvxcReYCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZxeVhN_01GUef5IKhJxknlu7EIUA6mz-eqO8BEAbfbL9pSRXjLxiMHFYlJw4BFAAKOUE0r9V32ST0eNPD_lplHUEYWErt_3ksB_OxYfoOsxIvkrVc1CudHG3PU3qua5CMWEH0QqjBTpu_P4dOPTP8cdD8I-IptLsF-fFZf58N2jEBVvggYRSd-g22_18F0eyVjA-oHioMr4lZ2Jxq67BCq1Sf0JMKe-oBfEh1_5IrocBiO3cWoi-qf3gX2AhPm0qbpkgsrmJiH-sJjzZt9eU8EgWtf4tJOTcqFJENQ44US9w3hLoEL60V0FVDIh39YEuBecton42IomVsqglrV9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=hmaFJc_gtoLcekWqWIxeAIxUW2j0ie3XBM0Jij0aAvM1YgqPDJkXYuJ44N-YDbySlnEYhR5QPDufL6Fb3mTe2YZAYJLTBuI20HZw0uu2mDmxm0udg59bE3wzHRo3DHzUAuYEJwcuLPz_ML5S-_QlL4xVE3jTKsjhUTJSEbL1YuI8kndDJ9n091IAmZ-zg777YUjXBzCycRfPJW-5Y5NrwOjHovjdL2WNHBwPXuuISvRgpTOaCq8rPku5xO4n7dWuVrpXpIOo2U9yvuiD3fvMU2dOHQ1lc-_Tf03w4M5AmmD11yorCqX07ST0JtLJr_dkPlHuyRysxg6u6QVJqGq9nA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=hmaFJc_gtoLcekWqWIxeAIxUW2j0ie3XBM0Jij0aAvM1YgqPDJkXYuJ44N-YDbySlnEYhR5QPDufL6Fb3mTe2YZAYJLTBuI20HZw0uu2mDmxm0udg59bE3wzHRo3DHzUAuYEJwcuLPz_ML5S-_QlL4xVE3jTKsjhUTJSEbL1YuI8kndDJ9n091IAmZ-zg777YUjXBzCycRfPJW-5Y5NrwOjHovjdL2WNHBwPXuuISvRgpTOaCq8rPku5xO4n7dWuVrpXpIOo2U9yvuiD3fvMU2dOHQ1lc-_Tf03w4M5AmmD11yorCqX07ST0JtLJr_dkPlHuyRysxg6u6QVJqGq9nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZqCcC1iHEhyQuYRyrEcUEL7UaGU-YbTXaBU7wd4gmnwUZ1o5-uq7luIOVF2e4nWWqgmJEwJD9xMOM_ECF0Cw__O4wCZepzbgY0RtEhwHcXLX9KOJ_eJa3l4JWrdjyDWZ6f46A0v7caEyaB64U9HktTVekM8z6MBS_g_HX4XeJ0ozXhKUVB1qZFEplgSVlAygTHyxEEJEcDZ3W6tjVaBm7Lo64vvmXE9Y6tv17opfJV2OqZuvxFMTqQ28vVLZHYDLmh0d7KqHMwf9WuilqFam_VzuZI7Y4k_17jvIpCgIN7lhXDAxwQBgsx7Natu-i4Wl6TQIGVCP0sCiniUGU4dLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NddZl21LC6cjTn8fKoNY_YbVycBYFh02CBXyBdd9aY5WDwSHIylDUL7vwG_ztcQd1N6aYwKOhVD9fUesvRZhpYFE7WMdASn1Z4nXeiWZk5DSDGfNF3w6LNk5aZRj8W_P8YEmg9GvITG7GjT6zEqWkRCqK8X4gihQmgZixpO_cjdvJjQfd8rAwuTXM1ufZ3s88h8hDuTtNwdH3XaU6GjWs49JXecisv60nfWbwUntRz67aR-4q_tuY-BHOU13Zcy1Fi1m4iN5Y0BzIzXlw-jXriaaxXGsZhVoIHJ5O_KJiYEGBI-jPq4CSqiU_xFyhW-vUTQB-tfOKwa4DFvIL3OBqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKu9HZrwD0y6o8x-heVOswPdWR08ctOkJrIcTyZTSODbr-OrqMLCena6L_QLUUgPXHT5t3EPfkr2Emd-EusMY18CXknV-6_PYwmXfdkEYw27pDPtJ7jbZr5ZbWhNMC2qzhxXFCgouRqAt6LZbb4jP694I14W7I8y-69Cen_7tgt3owRPnTCvznsh-MQbzDMCIZvNfulIVhq3_Xka8uwJOGHStWF7gEkw7QiTmZxia6ZM2jOn9JQXazBKzEjM2BnvtmY08KAa6Y8aCct884RRvjWyxfYzp0v9yzwY3jgfAJkrjVPnf0MXfoXXmL80pCsmSa-OOLhncRr5B_lnhRuZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gjxgc6xxZEBzsJmfiLN24umjnaYmfmYwMZi8Uyk-6j5dJZYDe2LfHYa_96unkErf_c-7U7sDBisNc5dzw53nbVfZcOVc2Qtvfng2AYsbWuYXPk_NDH9NlWyEMWxm3PPy0m4ZtnQDJQAEdOw968IzJmuuVXDIanUB2lubIl2uCf38Ikq_WZsi2ccg2BmHhGEYhoLl7njLyGZLin9BlOHpQhjviCoO3YWpCEUwupfjP69SOAN18VyMmRzVVHtqBYCfX1yNCKwPhfcsIVMWV_nSocu97Pm30bKVDeQco0pYhxwjAD_8Fw-Qk7Bqpa3b1D-3ATJI2WK8JxXQDp6ARGG5hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=nkh1mpfITCF3S_a9usJqLbxdOnRNefZH6ZG-U4iD2fWf4DOblphBuYxrJXAKsd-D3HEZ6RrNjlwwjVnqUohxYWPmjxFlgvXDBl65mnysmLcNbC5kpqgK8jd44t4Cq2_qi4ok5O7n5TyPqRw3arntiZPHgoHhJvFb3pRs5YmT2ejuNFiwvToJn-2kl9z65nP5h10WWZC2bxmG7IsC4hnJOS8btMENXgdVdG2SRPe1XuCcEv9gy8Qtyxo3GQ0R4akh2mY9xhZ1zTn7IDNjCiVgT5kRo3nprSvQBGOCCABkXTX06cyDW2rP3H0E6RRjW8Gaf_vmmJ-X-QcOIhesdKQCYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=nkh1mpfITCF3S_a9usJqLbxdOnRNefZH6ZG-U4iD2fWf4DOblphBuYxrJXAKsd-D3HEZ6RrNjlwwjVnqUohxYWPmjxFlgvXDBl65mnysmLcNbC5kpqgK8jd44t4Cq2_qi4ok5O7n5TyPqRw3arntiZPHgoHhJvFb3pRs5YmT2ejuNFiwvToJn-2kl9z65nP5h10WWZC2bxmG7IsC4hnJOS8btMENXgdVdG2SRPe1XuCcEv9gy8Qtyxo3GQ0R4akh2mY9xhZ1zTn7IDNjCiVgT5kRo3nprSvQBGOCCABkXTX06cyDW2rP3H0E6RRjW8Gaf_vmmJ-X-QcOIhesdKQCYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ufqbASvR0cwxloZe2njensz6AY2f8CXzyKF8DmsTiI2lh402no0uN8Y_AQan9Ju9YFk09a1oogkXSncfQ5fwsrSX3jDoHczqRGxgMRUuld1vfE22f6Vos9llIvg0tpSKFTEOHerRlE9dUNEt2h9XmAE91BxmK8anwAYFmiV7Sl37ofpgY1AlWg7LKdAXwlYe1wJRXY_GqHR12PWu9zRnQz-ft3S9k8uWnRA0ns_T1jxctovnbDzY5UeriupsqWiCuVXQ3h4FIHfwGpJD5OAzlkZ_nZe_vSPKrLqBq0gpxJKxss2ef-21OAkFEEo9CPhTsG5IpZfxStqU_0Aijw2bIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC87Kum3syLzgK6RMvr_3hifT4d7JjI-H5xtyGQeGUM2_3aEMcHg1yh076x9nL3ekPrjMqux4w5pF5j9xoJKM5QNlE_pkcuUdklchaWWoPiWnJfVx_qlHXPIr0xzyNrX9DqvqW32UMhtZ-dd-I7NHjv9nQmbd63DDH5uZgk3lrgR3Eu5SKZVSlqbja4RCYbHCp_0wXpOU6wWPDZviqfPoDzdp8NlU1LUUac_8-Kgvr0JnHjw-3QKPxh6-4MPxdatKkpDsMRbAxFS6GoipHeKj1qOafA4tWgeyzWsa6boa-9nQTiDpzQUNOsCUQ-k_x7hPyEoO_MlFFcb8nVG9ihlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0A0_o5B_OVbVR48-b22YDjSFbJcVE3EfMixg5FocHHhNHLfePi4mL5IKev-J49nslJ9sNpnOmTmrcB7gFSD2D24JaFfUQTAev6lxtBF0HbtkBVfv8MGIb8EKSIqRionaMCBDJfT8oADYmG6s7xnYlKrMsky42In9wRruKXfBvnQaI5x72IyXoOhNuLJibRj6ZVCxY-ZB9_qLU4bCWtehUiNknx7sERcWm0Jqe5wt85qQIZe9v7vgoHkJvh8SZlcUh1vUDd4Lhi2vglrRsYM9LH5a05x6fQoQnIjaAGFxd5kgdFE1LKsC6gmcKlN2vmsvfRel5XeE6nYxsbKplP4XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O8MmommEumSLV_GCUnShtAcrc9uvKuMaSGBhcxFCLXl77kSx-6VkOuFFrv2EptvHICbbhtVBV0g-TneobfrsSfqOdKNCkQ28zDNQ7qouTR9sRIvIVWAKSDFUDqrE_G-5mTRWiS93sBhsvvuuGX3r8IqLAgYFFMAchmuJijf62WQVa7pwUfXp9VIHc6DXhLiMh6M-7JFssAV4syJdEnbFDol_4pXExmgVmLVsKkJWJ9r1WHR29hQ4asLxQLh4xlp3G7EiU6D2f6Vl8qGgWm65TA1n6-jfTZ5xyxpZNLetxjIqb_-ab0GTd5_GxzWIcweqa1Awp_W5kQoU2fBjrtWu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fNs3EmO4r_TpEzvkUWJYm7EB3yxMz8T4eXLx6ItBO0OL8HcaLxHh-AdIRnrL5h7JTw_hZBy7yFOF-zN8b8naMjmHSOdGZ-nRWmOEIvJuQ5U3oop2e105Virc5e1m9Sz0ovKOObq1LhxZ9nVwzjSBPyXK6E0k33if6Oti0mb_bs4uhDnHNSPQG1PYr2LzRPWYoqkXRkoq9xPik_kSdViTBKcaF3wxZtuBMkd7vm3PiQ0UKN0uD8-xHP1GKQY_uDXDZRqYkGcACD4MZFCsZcbu-Bul_DHEJoVn3dg2H6DOWfZY1ljayjQIlbVfX8pOvAOOyRqkRMlEpX3xNApNtHGVEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pNTVyajKTecFFu3FR1CrHwC3yk_nbQZaA5aFXx1JVEXyuEsE_-p-oQwGqwoilsz7lrMnBGaFi02lDYpwkj4EqU2EcP3_jgdHrLdI96y0dhQL_EbKFIno1q3Xov6-RT0vO8b0mFD3i6H5g5dR5W-fPv22JiUl-toBBjBSP9DvnBuYx75BR-17Ws_ICS0F-DNb8zmA0Vl7VdhmmyYsPAPbifJpnR6-fGpBgeHnx88k4Qu6TyFA9X1tNM9PRVii66CB0HKx1UKvmegs9-o8bIobYdVgu7jW7W9tBfyNzZDCOcsHb23xb9PmXyorMHiIDKooHIvhNczZJO2_RJUWu9tkEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78294" target="_blank">📅 16:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUkeQapkD3tsmVFEmo9Z8hBHkzqPxlV6-j3G6WOAJ_njhj9KACH0pgg_xMAJ4a986UDU_q4OVKN5A13BQWFKLdjIOFTmrjAt6iG-uYfHVLS3-wB9JIGc3zptEDN-Mp6JwGP55rDAx3E6ETY9mT1T7YdXkzf8f59-HCAcH5wF30GYk0-NUyghJtbcN7ZsENaHuKaZlPPSm1qeM4QuSORyRLAwWKCAaGfBpu1o6b2NNu6OKV4p6uht6B91BnW_tuWtv4hMuUgMxhQQh02TJQbUOm_zbEtQ851WDyfUlrauRP-2Jq8qdFgGpSuClfSGxgBv8cIlKe0Q9heSb4xTEtGkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ماموستا محمد نزهتی»، روحانی اهل سنت و امام جماعت منطقه چیانه در شهرستان پیرانشهر، در یک حمله مسلحانه کشته شد.
سپاه پاسداران او را از روحانیون همکار با بسیج معرفی کرده و مسئولیت کشته‌شدن نزهتی را متوجه آنچه «گروهک‌های تجزیه‌طلب کردی» و «صهیونیستی-آمریکایی» خوانده، کرده است.
براساس این بیانیه، نزهتی سابقه «همکاری طولانی» با «بسیج اساتید، طلاب و روحانیون» داشته است.
سپاه همچنین فعالیت‌های او را در راستای حمایت از جمهوری اسلامی و آنچه «وحدت شیعه و سنی» خوانده، توصیف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78293" target="_blank">📅 16:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=lvFDbwrrQkJBcA-3nd7wibZB6gKwZNohnR4CH_jsqK-1HgLQ_AwB9AaAkDtGCKKCsFuqMxoDX9tzDb_61mnXtYuIlH_4B_-GuV0mxi-RwtqjqR3tfNFlh2GvEacX2OXe7lEUjLTFvgx6gUBqmHIfhkDCywAvOX6JbN0plE9JbCli5wseGu3PuTlGLNimheAK-JgMXaN1l0f5k_k3SvH1N8IfxgLXnEVv5O-NqDjuVR1xvXoLY0SIjGsDFgZHeqFza-8YhWdD-Eb7ovHUPa7RS1q0y73PP9nnyCmuoP5gzgg3-OwI4-LPeeLfHRWuJX2Ef_xpmcvfXlOVDSyUGWlmsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=lvFDbwrrQkJBcA-3nd7wibZB6gKwZNohnR4CH_jsqK-1HgLQ_AwB9AaAkDtGCKKCsFuqMxoDX9tzDb_61mnXtYuIlH_4B_-GuV0mxi-RwtqjqR3tfNFlh2GvEacX2OXe7lEUjLTFvgx6gUBqmHIfhkDCywAvOX6JbN0plE9JbCli5wseGu3PuTlGLNimheAK-JgMXaN1l0f5k_k3SvH1N8IfxgLXnEVv5O-NqDjuVR1xvXoLY0SIjGsDFgZHeqFza-8YhWdD-Eb7ovHUPa7RS1q0y73PP9nnyCmuoP5gzgg3-OwI4-LPeeLfHRWuJX2Ef_xpmcvfXlOVDSyUGWlmsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مادر یسنا (فروغ) اسکندری در سوگ دخترش
یسنا اسکندری، وکیل دادگستری و نقاش، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در منطقه آریاشهر تهران هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78292" target="_blank">📅 16:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dh0Tc_DRC5W7ExbjntQ5tycRtVN-mka2iW1AbhAA4Fc0lmttkLbMRJR72-yv2DUWTF55WA-seMUOXUL5ScGdMdMahvrnaXSlQ9fpDZYjGX13MI9UXe_B4E17cEHGfa5XKMZkgNsK6ZjjocNCDkvQ_BBtJx4p5Od3SXmnugDFUJcaZl-N3Qr8yrMhFrPzyays3WmFJ-ecgDRGH6k5z3x99lxJcbOK4AB8SXaL1Q7rLxfUeGQ3MHT4qWEMUieoIehYSFFUnM90wOwiTtXyEzA70p9f2DPYCydpI1qhhLwJJEIb6NGhPJO9l6xjefMs04xHzIbGrDycbEn-kxdTRAlVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=p05pxpvnD_8Gj5qfsABJjtMdhSZh-cwae2MwhznOBi7nyZVJaAaWB63iW1hADaVYfJKXU7qg0GxKCVfcxWVLiXoy88BNoejdzAJnaYDMjkqfYNsTxK4mzs-FVPUZ4mk9A8xnulh3PjzqCHC5bImf_gF67vF-QeQgzmuOqVMVWQ6AwTyC4Sp5tZNqpTtTrr0wJ5faAlm2iwfqS_9xoj3d09IzO9YozmuHzgamuipetaU6GccjnRgazgKz2Q3V8emno1-v4WWyF2JpWxQjtibszs4FeIjFEoEmvI08B040X6hAu4VViV2d-OQliXEzEQDpUifYlTkl5MbIF10iYW11_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=p05pxpvnD_8Gj5qfsABJjtMdhSZh-cwae2MwhznOBi7nyZVJaAaWB63iW1hADaVYfJKXU7qg0GxKCVfcxWVLiXoy88BNoejdzAJnaYDMjkqfYNsTxK4mzs-FVPUZ4mk9A8xnulh3PjzqCHC5bImf_gF67vF-QeQgzmuOqVMVWQ6AwTyC4Sp5tZNqpTtTrr0wJ5faAlm2iwfqS_9xoj3d09IzO9YozmuHzgamuipetaU6GccjnRgazgKz2Q3V8emno1-v4WWyF2JpWxQjtibszs4FeIjFEoEmvI08B040X6hAu4VViV2d-OQliXEzEQDpUifYlTkl5MbIF10iYW11_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78287" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78286" target="_blank">📅 01:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78285" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p2MombLxYljNLu79yNyi96ydXHG5a-3Kq1GFMMypLQMP91KwoMrgB9YZSbFzpfa60lHS-kNKukL8BnAytn1BG08hOPbqgR024XS93v857-BOZi1lSTnUTMRoMnOg1HjYIpNBKW2GBx0JxZEGtI_8X6353U3JB1wkcm4kAnAibZRzUHAV-rsWMWl77E8eLcNUD4lwMh_Zwsxk9TmmIy85XffZWMdle8WCziT8eMjCcm5NklrPUOiR0NZ7Dq_GN3QyAW2wLQuwrt2MVB9zsl6hX5EnM9SIpxWW9-qgRzQ3xo9JnYvI54KHQljMo1-J75wFd7pNWDeUiahwSdXht8gvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی گزارش‌ها از حمله ارتش آمریکا به اهدافی در جاسک و اطراف جزیره خارک، رسانه‌های حکومتی در ایران تائید کردند که یک نفتکش دیگر نیز در اطراف جاسک هدف قرار گرفت و خدمه آن با قایق نجات در حال انتقال به مناطق ساحلی هستند.
پیشتر رسانه‌های حکومتی در ایران گفته بودند یک نفتکش در اطراف خارک هدف قرار گرفت.
رسانه‌های اسرائيلی و آمریکایی به نقل از مقامات آمریکایی گزارش داده بودند که علاوه بر اهداف دیگر، چند نفتکش ایرانی نیز هدف نیروهای آمریکایی قرار گرفته‌‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78284" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciRTbOrO5aEOcSno6FMkNhy5ZZ-0_J9AgZhE2kUn421pSfQRLHLd9kKnuDKh9Ip1OuC0kImyHwjZv9NrWFKbdJ-_vZhNPMySrER3HWWxOthnXVvNvYUQ4p5HSW34xEDkMIpLlNx31yc1bLUoXCGll3kuww50epcje6gpm5QKdqaoGEVilxok9FMdExupYgKuXph0d5C4Zsx-TDeYagz6Epltlp436NHfFjLiwFhxYbe5picDPFuQ228aCAolqEBkOkow_h8EtxLksqsV27BtmvBqk531aI2VDdpP-ucYoeyhy3VpAEm7-Kr0QR42ckpKbWeQi_aRjVKu_-tCGNhjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، روز سه‌شنبه ۱۷ شهریور اعلام کرد ارتش آمریکا به سه نفتکش ایرانی اخطار تخلیه داده و آن‌ها را به هدف قرار دادن تهدید کرده است.
عبداللهی هشدار داد هرگونه حمله به نفتکش‌های ایران با واکنش نیروهای مسلح جمهوری اسلامی ایران همراه خواهد شد و پایگاه‌ها و منافع آمریکا در منطقه هدف قرار خواهند گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78281" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">"صدای انفجار از حوالی ساحل جاسک"
خبرگزاری فارس وابسته به سپاه پاسداران:
حوالی ساعت ۲۱:۴۵ امشب، صدای انفجار در شهرستان جاسک شنیده شد.
منابع محلی می‌گویند صدا از سمت دریا و نزدیکی منطقه سنگ سیاه به گوش رسیده و انفجار در دو مرحله و با فاصله کوتاه رخ داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78280" target="_blank">📅 22:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGzwEREvU37OH7Hc48bfEEUwOVGi1tK7FVaQe4mTcuGnqWG8BMh6PXCSuXjO98KVMtbymoaqrm36_-ROokthFcWfWONZY1mHtvsXVjEXQoz4aL64r1ypvBJoygFPAgIxjnaifmtoBJeyHn0TEe5Bp0kgtq5Uc_3e-nXBH9Uw8OHL7Qupff0EaDcqG45VVAJApZX-bB0ECH3s-jsr-hQkIKhOOa0GneBqr50uGtxXPcDCyq6iI2IO-b1qkoARYjY3mW6LmOYirvpYZiAnRvbKkS8eu90rmmoOerPrB0zgi30isCa4wqNIuO2w-QkhwMmEQu-l6BzL29wtlxJYQkA4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا، روز سه‌شنبه ۱۷ شهریور ۱۴۰۵، اعلام کرد در چارچوب «عملیات طرد اقتصادی»، ۳۶ شرکت و فرد مرتبط با بخش هوانوردی ایران را در فهرست تحریم‌های خود قرار داده است. این اقدام شامل ۲۷ شرکت هواپیمایی فعال در ایران و همچنین شماری از شرکت‌های واسطه، نمایندگان فروش و ارایه‌دهندگان خدمات باربری در کشورهای ثالث است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78277" target="_blank">📅 20:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bTJIsjRkC4u5UG0w28FCdxIwnsAn8cUB4WJlXyTfs-QPjoXFXJPI1YGCexnQVGmAK9NexJnNKu74pdoYNlmZbeyqsII96BPyX7dW_yB3x0Jej39MsElgtqXg4atnj2UupqjxGGGQ4JUgs2XqSx8yGR0DrSLeKotel841UnGgZ5IF81IG6Orb9tBpzfzuo7GoNqV577LcCssbDp6HAdjWjW2gV4ul968J4-BjBsGMhYjGqanJ3OAdHkZGVYgF_6i4I3__PNWj5w9fiuwjBwFU3v9HOQaNfSzJ22Tt4S4G_aPQbdGaKKBUMuBHdc9RkUjY39HelEIGpPXnei_2F1ypoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cbsY2r2d6wxlzUYYhWkjnCHyQ_XqZVnG_4-1AVZVTqNJucFxzPv6STQU2vIs7ezohC2mT4HSyk8tIXs8j50qBzhFAf3qsYmqKu8WWs9qk5oj_XzS8eIAI5CHjIDb_hwZerCO4oRdRU_WD8qZ-dNqDM4wuz4p1_G-1cIRb-4LGJBUu-cOvDXAv5ARaLUsrOMcN4I45efO5IPUBz2NcNTdk3dNFOPr0rfjVVYLD7EAFD1v22EUZXAePoGBZdB0qgYnjNoM4alcO0Ly7Ol6nKJJxbEMHO2OFkL89bVpFsbvIEtHBmu6ndrFQh3G8Lij7pFYQu96KhPA17zkfzvRXELUiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuff6dRe1D8qHP0_vJhW7o0JCM_OwrHDKOryL97KLURbBfQJ5e2jX6383XreRgEjeTE4puaTSdvyYLD48E7zwrROgkL7cMm40v6bHiIcxfKvY1UblUXhUvPq2dfNYg8PlU5uXcaA6qqZBsi6u5OrWb-rcHlywZ_qPEqNzfvXLy2Ed8SIj5NMt1wYaMnZxdHKE5J9a2wwhprBfnwWdsjTfUGJsQIeFf9fuloA5BkJcwVWEkSZheriJXFywT97NThWzG0kkPSONvKGAGXBkP-OiwQumiRUa4an-tjRbvElCwAsqYhU0OciKEMBz28qc8SlbvSION2EVGKeV72QGLLzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرئوف اسحاقی، فرمانده حوزه مقاومت بسیج پارود در شهرستان راسک استان سیستان و بلوچستان، روز سه‌شنبه ۱۷ شهریور در جریان حمله افراد ناشناس کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78274" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YgbSGmb2Lbvu-nTcJ9zkdUM9hWIah4Bzzc_brvyeJET_7aOyUswgF7iyXRxYc6P300fp81hPKE2CBZpzyD560rScOjgTbbM8jdgnyLarjbQBHRtB3no1vhbiuzYs3RxH9VY-vTWfxaLrtPui41SNA3FQC-aBjLGG4e6BHOTdCJ7FXhxfM5TJgT-CKvAa42_71zwW8qb5v3ezUsqhZRTWMkpnyi3B19GjQ_9hlYtF6cArRNPG6dyYiUlC1MEIic6ndpZ7d9C-Ukj8bc8mzuIBN-IyZ4eDUVs31FzS-nYDobHgh7DpBFdb6GLsDUafCqzRGhxcKjSzdHCyp_W0yHZUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/avc9y3WqglZVL2Q-A40vfTa37PDtj2mRCYRD0gID44715Rar0b14DUXRDzQKZFUtckku8Sik0uGEDjV9O4i1O7H6ChaWXnN8f_jNtraeWaQqNaNzG1Ui3HF6ljiEdte1ViyuGYHErGdK7L2aIwVsHI2qOTOlC7VeoZgU7txF_5pDHVxXDPvDW-nZPl-UPSgQ-8iHZBKEfHEFbL3tZIBTQZbp5WMwoUP9M8q0VI0WaaxpGwxHypylpOedl78grkEJMC2RXz1rNZ_7FimU9JQosrNmcT-49NAhuQjvZdN6RDLGLQUgmiKUQwxsMz_62SGaQGxp8qkX14mBKXyeOoAkYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UpbfEwtkiNlLcsz8opGAQUtQmv86J_gCWI94Eli9HEocFLQI3uMmrXef3HWWqUfIAxUVMxa54rWjoDPaSzoiyKE1fGaIiPDb2b6lpITXj8lxPT8ShWfFy2kN2Swm1k5kwKXPJPjHNc52h8FKlXsxe1AEFSUWuxRo-oCvAoK0rS6EQTLY3kKoyB0pToxQlvtOXm7w-W2yTmU6YSZeLQHzAnIVV5FoDOXjxkIcxBtKRkTrKcD3cohab8lJxQaGiVBoBoUTPP3iruFRC7DuHiXyXbPLhjzl-0MV-3FWt1r4jqx4CGO8mFJ0NeWlZ1FnRG8e6hHCK_LWLFdaHnVaOAqR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cF7kuL2izGC9k1IaJtgB3xcKsQWqW9dlajqVQj7gHGikPUXtjfNVs7S4mOOmJC4Ljm9yArWa1c77asbp2P0hmvUi0JMEHCAI2UHA2c_9gOSLj7fcWGQr_N4Ywo4SSLAttxkk3WL_0RIRcrqMAn7u3XiQd3sgha-ypW45l2rvnzfaHMEG1qskCjXCdv3wOpkXhw8o0DFtJ3AgBeXfuSbgoiK8mLQgDy6_au6gcOKHcG--rCMxC0qbHKYfbVmiZLp6oUbRSXnesEfYW0ePgIXqAsDhhXp1rQR55X2-x39Y_nEe-VgykTzXdP2i8MUT-6M8-aCpe01pssA43wajc5fliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h2TELEb9tuuX5x4D5sj6XsIPXuHvTZyjmu5zvLvX5Qhnzs5g3vMz3sQ8u-NlvqKy1e4Igrweg4jMANf0Ut5nI3ZakQ6U5FSOgI3gi1lF0qm2fvoN28ajrYfhExGJSObutxmk5iCFxkvbHaIdq8ODcWMFy4hviQUqcEJlnNRI9qYnQ5ApoGnhn_MurOWqSkZNumY7N5FihGD2hPrBrUhoS_X6EXkc7__n1wOL0DB7ynhajoqecLL7AfNWCSUJN84Jn78EYb7nm72deBswGuCozOLMCHBpwSYyg1cnvlZHHiGYSkZ1Y_-4vw5Tj3XWW49qRrBOH-1GwRyoOR9-uXGKOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=AYXvmvfKRgZSHLV0jEz9thcbzNRL1VUj54BVn33xrOIJrD4GfQTCbcEleoZcB83L-fVRDyMjVy-2PB8ahVgaS4H7LDg_hUNKkI2r8LIJU7sjf0WOKK_BbAgpcaF1wmr2JDloP5KqRB9D3OSdJJ6fFr-h9JF7Ia5fghy6mqnrcsoDw458BQOoLbrAUhWS9YxtEgcKCXe5cW2UIdntrwVGpy98aczZTw4oJ-D34xFkhp6MJgzqCW-ZaBeb88DmWaOO-G3tfENdAr30yecmn4b_6ls7O-KgoIuXQ1WyoiTVxHryt1WbCL-I4RsHWcM9KS0BgM5xYoh6TdK5NN4MD_XNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=AYXvmvfKRgZSHLV0jEz9thcbzNRL1VUj54BVn33xrOIJrD4GfQTCbcEleoZcB83L-fVRDyMjVy-2PB8ahVgaS4H7LDg_hUNKkI2r8LIJU7sjf0WOKK_BbAgpcaF1wmr2JDloP5KqRB9D3OSdJJ6fFr-h9JF7Ia5fghy6mqnrcsoDw458BQOoLbrAUhWS9YxtEgcKCXe5cW2UIdntrwVGpy98aczZTw4oJ-D34xFkhp6MJgzqCW-ZaBeb88DmWaOO-G3tfENdAr30yecmn4b_6ls7O-KgoIuXQ1WyoiTVxHryt1WbCL-I4RsHWcM9KS0BgM5xYoh6TdK5NN4MD_XNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78268" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOr5al6bdnTD5UgDMj7JSlW_xjoBgm6pP8hB7XjOPJNxis5_ylcc2nmIz6pooO3noHSgbntibnOa91LRqVtraNX_O8VWkhN0OgBIYjfJvfbGei8upUYrYAgj-VONPA4XDVtrJRTKBNiTghSTTmRBGnh8n1hI3YT9ccR_Sh7eXsnODbwEsxlHJRRPcnsEjNG3GyA4Rm9FgKKVaNuAWILSAZrsr5NSWRDZwsQ2NQdvo1EVZl1G-VE2I8gSLgRxVo5An4aPS1imJKdmT_MAFhvvFmeBvI8jtHcMqbF32KXsXbZm3DHQM0raXgwjFIvmpfaQ2OSXTlsr8bPAdnmqzNU9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آسوشیتدپرس مقام‌های سعودی اعلام کردند موجی از حملات حوثی‌های مورد حمایت حکومت ایران به عربستان سعودی در ساعات اولیه روز سه‌شنبه، ۷۳ نفر را مجروح کرده است.
سرلشکر ترکی المالکی، سخنگوی ائتلاف به رهبری عربستان سعودی که در یمن می‌جنگد، گفت حوثی‌ها «تأسیسات غیرنظامی و اقتصادی» را در شهرهای ابها، جازان، نجران و خمیس مشیط در عربستان سعودی هدف قرار داده‌اند.
او گفت ائتلاف به رهبری عربستان سعودی «با نهایت قاطعیت، تمام اقدامات عملیاتی لازم را برای بازدارندگی شبه‌نظامیان تروریست حوثی» انجام خواهد داد.
به نوشته این خبرگزاری آمریکایی، این حملات در حالی صورت گرفته است که درگیری‌ها میان حوثی‌ها و نیروهای دولت یمن که مورد حمایت عربستان سعودی هستند، طی چند هفته گذشته تشدید شده است؛ درگیری‌هایی که آتش‌بس چهار ساله در جنگ داخلی یمن را از بین برده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78267" target="_blank">📅 08:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vY25TXvx9VsE3xGg2wBq0xeux5Jg5RNA-REVLPYjnvYjLfXbuiSwPkFNWCBaCmIA2qk6-0BzQDc__xDz-pyaWEiRywEgau_QRtf500s1nUzfRZ5aTlbA40EcD5BM0Omg3ss_868buGhTVB_5fD1mOl0SXJSfggZJenieI7NhLdGPk7CdM8i9D5CxY7Yu6UBh0GDnqC2-MaZm1mE1tx42jrgWuV4S2iOYnDPJr2KVK5wRoPfgSYjc35ctOxZBD7SDdFGX-L9ZbT-_XGVTTQ_nKpdkP2WAzQkRl_nPyhfqXLYPjhapRxC8tdaiqomqmRpw7YoEdI7FILOhtVfKnhC6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی ما در جنگ با ایران پیروز شویم، قیمت نفت به‌شدت سقوط خواهد کرد؛ درست مثل هر چیز دیگری که دارد سقوط می‌کند (اما بیشتر!).
بنزین گالنی سه دلار، اما در نهایت به زیر دو دلار در هر گالن خواهد رسید.
همه این‌ها به‌سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
MAGA!
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78266" target="_blank">📅 04:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/980dd40283.mp4?token=Ufatj4qF8fbcSVanJzsCNDoz2e3Jn5jzC_jRFKiwzv2_HULl5cJjbBz1zHfAYJ8s4WLWcPBLaTC1wXdWwYKQ_I4Mj4TuILUE2C4f3xESmM92W5e1T0OkS3iS_D_acRWHfCM3OaJu7k0CgoJaK7DGJpZKemj6SNjj0aoviofnQvU4kCLUcbryryd-JEvIS0ydn4AQbF6tijv7HTHwE9f8RTCW0gyXq9zqJetKEG7y6a-lXEHXRv5fYVkcleqlyPgPR_kvPK5bJAI1fkOM5S-MsD4jDLM2AoTHeaNBFhGf3gS8UMhQ8tou130BNDvKygfsBQNnHXNtYsvPHb22-obNdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/980dd40283.mp4?token=Ufatj4qF8fbcSVanJzsCNDoz2e3Jn5jzC_jRFKiwzv2_HULl5cJjbBz1zHfAYJ8s4WLWcPBLaTC1wXdWwYKQ_I4Mj4TuILUE2C4f3xESmM92W5e1T0OkS3iS_D_acRWHfCM3OaJu7k0CgoJaK7DGJpZKemj6SNjj0aoviofnQvU4kCLUcbryryd-JEvIS0ydn4AQbF6tijv7HTHwE9f8RTCW0gyXq9zqJetKEG7y6a-lXEHXRv5fYVkcleqlyPgPR_kvPK5bJAI1fkOM5S-MsD4jDLM2AoTHeaNBFhGf3gS8UMhQ8tou130BNDvKygfsBQNnHXNtYsvPHb22-obNdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78265" target="_blank">📅 04:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pl1z4rx_lmBhhZYeILiZ8vgdZfoIRMbkGMQlUfNaQeTW6Yh20_CeUrbwppeqXkBmX4gwhOmfTPiC6SXfSmPBSlFquzgU0a_LPCUe_uXk5va8geYIa8YvBUjxtwsQewypIgBcha20KiKDBBqhlPTux4ar0w50nvQ0V4RA_0epbLNhpM-uLiRaVchjw6AQZsV4ukfCbPoZUhFDsIfM4xeRSo8-d_VT-5wy3IY1HlZ--Wm1E_o4ns2BdNVH2XixeOsrqcN0D5be7mTw7-kCHpj7MwF3-2z-GE7xPvRaWgZnb74yeejLCUfz597XxLcgE4zJhZ3XQG1mmw1XudqnEHRJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال کریمی، پدر امیرمحمد کریمی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴ در مرودشت، روز ۱۵ شهریور به زندگی خود پایان داد.
امیرمحمد کریمی، فرزند ۱۹ ساله او، ورزشکار و عضو سابق تیم ملی نوجوانان تکواندو ایران بود که ۱۹ دی‌ماه ۱۴۰۴ در جریان اعتراضات مرودشت با اصابت گلوله کشته شد.
پیکر او در روستای جونجان از توابع مرودشت به خاک سپرده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/78264" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsDOz0mo6EN6kZtP4hFM8sYzfmZMqpk4pGP5YaTAo3cY9aEbahjWxWtSNjAyvdXBMmUIpCiJLpWiBe3TQbdTNF1kXlFOsu3rq4Ow1O8ulfpgwEFDQPA0pwuxJHSQEMxizQLjKM_CTqv87uwK43u_IW_V5XAe336EChQZKaMjyyCJsP_XAlE6cZjvGyTriARUIIZg_ClEIbM3-lujOtnZBrYU9A4worj7bZIfemdPMXpoL2aBdByuEhiGFTP4XtzXwtuPFNyO1Fq-gsR-ohF-XKznJ8vzTe9XHdZYJGb-E18lS1q9YR4BBDH6Wznj1R723MKlzzTuz36ZoRvpA-hhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیدا حیدری، نامزد ابوالفضل سلیمانی الموتی، از جان‌باختگان اعتراضات دی‌ماه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ به زندگی خود پایان داد.
منابع حقوق بشری ایران، به نقل از خانواده آیدا حیدری نوشته‌اند که این جوان ۲۵ ساله، حدود هشت ماه پس‌از کشته‌شدن نامزدش جان خود را گرفته است.
خانواده آیدا حیدری گفته‌اند که آیدا و ابوالفضل قرار بود همین ماه مراسم ازدواج خود را برگزار کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/78263" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/78260" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krulOHq0gUQBUmJvcTR9Xm5jTZv9IW9qFYdFg1l5FBo-KbqkU2Sro7B9G-nlBQJ_Dik8vCtujUSGV2aCk7e5jSbox1B9x8ESfTvJRFcn3tw-hSR_u_DXSNWtzavWr6m6EYKz4ootu7K6Io7DE458CGKDfQZl_xnuPTV3COl59Ayzipxjk_tA4Obo_9fzOq2P4Q0fWPV2wYitzQ77W58Q1gLhU_7SA13jjKA_aoYOO3H48aAQSswuQvWJQl9h-aqqJAzc4IU6Q6hz4l4u80FHFxtJ_4pinsAIS2lpZ8KmpqvvIKyxr2LqmRCzKImblfYEgH4RbKSiBpjaUBiyYsPK9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/78259" target="_blank">📅 21:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78258" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78257">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UottwBQb4Svdkv00Zjx-b8zI-Xa--sEMgRI9gCWBPSU2wgBAQboKpiAPRO-4aEmiGFTbDeCT13DbHbSu90TnQbfegAdB2vm8ft5eHM3VkcAsjzrzvtnbm5SSd0j_S4Cyywl1tCiVN4yMlvZGprGdAGGZvGHRBm5In8MVjU1WAcQqx0fYvjJyNxvvjYIe0Wmfr76Oxg1YRsKzPtpScQXXC-Lo2xghQ4Oo7YJQfHuWrWPUQA5I9LEREMkxEDnnTSTwdo-igRvV8rsUECMnlTlyObrTNgkqVfk-36keMg6DyindpOH2555UGcZL0FRyul8qEBACCJaYiX4-ZteDvS7FZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=JU09nJU0UHqprD7q_oJ9jCoHO3WfxmtSj6bC6_ROgT0D6ZpWj4B-AcYkKtBqBz3OhL5JgZflpJ4RMLbyoS321wzltP1HRgLCBGQRRhkr45EqG06IDtlKPbF-9gAFcMS1iXgJe57av5OtW0qQatt0SnGIiM9SVBtDF0Wb9mOC95_VDKnIKHMRoLbUkuTdeL1PBLW7R3dxRusubv2MQlssQzlXTfcHL3Mj8m7SYwtveH1wN3yORJOFj8_t0p6Nc_cHmHsUlv53mgbtoLno1FL2Ue-lsrwj8oQXN5eRHzaaWkiH1pHrxzUh2eKz1Y_GTGNwJH1ONCP9KqfPI1bDhhdC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=JU09nJU0UHqprD7q_oJ9jCoHO3WfxmtSj6bC6_ROgT0D6ZpWj4B-AcYkKtBqBz3OhL5JgZflpJ4RMLbyoS321wzltP1HRgLCBGQRRhkr45EqG06IDtlKPbF-9gAFcMS1iXgJe57av5OtW0qQatt0SnGIiM9SVBtDF0Wb9mOC95_VDKnIKHMRoLbUkuTdeL1PBLW7R3dxRusubv2MQlssQzlXTfcHL3Mj8m7SYwtveH1wN3yORJOFj8_t0p6Nc_cHmHsUlv53mgbtoLno1FL2Ue-lsrwj8oQXN5eRHzaaWkiH1pHrxzUh2eKz1Y_GTGNwJH1ONCP9KqfPI1bDhhdC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78256" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXkl7sxyAb1pKKLbaaN_zLyJnP4PeiKoKn8GDZDE03RJnsSCCUyR110qVhN1JwnjJFVefSSc8pYBKvJcD8ycymqXBzHMJfb-I3p2xpYAvuCcn8upGkXgA-RofCs-c0Sjen6BQ3CJTu9_bW2KGwFUOXzMH0plWWjFw-p8QKwbEJBDeX495heJ1I7OmSYtUoTQAH12XGTHsMSlBMNwOd4hG2RsCcZ2NsfJRz3H-gFkT2PZC0vwGrEbWg7cKbAQfdkiEdQbOcTK6GRrdbUMdjoQIaF5Hv5qYE3iZ2lqpkxzMvXYYy4O1F-5Cw9uDIAZ22bDwqNbcjFuBOY01mQnzftQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران پس از عبور از مرز ۲۳۰ هزار تومان، به کانال ۲۲۶ هزار تومان بازگشت.
بر پایه گزارش اقتصاد۲۴، نرخ دلار صبح امروز یکشنبه ۲۲۶ هزار و ۱۰۵ تومان بود. وب‌سایت‌های اطلاع‌رسانی طلا و ارز پیش‌تر برای ساعتی از جهش قیمت دلار به بالای ۲۳۰ هزار تومان خبر داده بودند.
بهای دلار در ادامه با شیب نسبتاً تند عقب نشست. اقتصادنیوز این افت را به ورود بانک مرکزی به بازار نسبت داد و نوشت این بانک به دنبال جذب نقدینگی در بازار است.
حواله دلار در مرکز مبادله ارز و طلای ایران نیز ۱۶۰ هزار و ۹۸۳ تومان اعلام شد که شکافی بیش از ۶۵ هزار تومان با بازار آزاد ایجاد می‌کند.
حتی با احتساب اصلاح امروز، رقم کنونی نزدیک به ۱۰ درصد بالاتر از آغاز هفته گذشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78255" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fiC2_Z2U4PGKUmu-SFeWLGDx6YWvoyJtxYd6ZWSa6XBS0PLfzrSxjpZE-MukaHCXwdzJ52TzreCieAr4Qz-P7PxaoLJPvvT_iqrbXShZqWiTIxmYBIU7lrvT0350FIXQCYoPcxObmT1DLBYxEnw9YzdwDd9bE1us2C_LZjlFIzew-hS_JwF4HUh-2yYx6svGZsnBbxva8Vw_faBDdh9Bisx5jU7VJ9ASvUV1VYQqzzszVmhcQe4tuLETCpCAOzK5gSh_gwclLq4t3kCe8u3xPde5qTuc4415SrWI1BN_w6n399-Om0mEPotU8JwNYnSXIxi4hrMSn8s4TRqUw5rtaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jQXjwrgZdjcllGac8XcjIQl4Gh-ufiotM6kL5FYOjWomJwcl4dmOEsgDdtvh6xTGvklVBMBKAPSQWjxNupU3AMB-5eYYRZwqpNXdxVeDAsN4i26qRhQBPvXWgXnf2HvaqtI-WkW0gvaia9nkm-r0-ESg1fug6r-BF09hQtWKZ8oJ9qJi1jbZtKsDPBrWXR53wBvg9BMtWyvEzBkrQbTANEuR6KNop5JHvWDhpDM9N6DlTlC6Vj4WRDABhdflup266HBBc1Yn3x6J0RF82F0dGrHWL-1-IAMTxjHT7N1dm466ivhFdYfwMoAhSOjKlY6DNUw22swaSMuDLZ1easplRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K3j0UPJrf1KuJatCrgs4LYYtuNoMzWcHADRci2_ursota4Mn3fPdGTZ_I1HG7OxEkUnSrztBJj0GjQZgRVaiXZv_X-AOhLtF0zdPR7xZ0S513kPO98LNyt9RhAhWIQS74r3AKWWdf4yX5dzkNuv72xyJjhziYTd8I9p7uRRnlTzBDxHjz7Dod8wDy4CfTBE2GboJvSNgReh7-USIAwouC4ytvutSqHVSF3qWpz-NfyDd8DxG1__NPN7hW6zI8wlBOw8MgtSrPXNkiT1OakSWxZ7_Bfu_BhlSM-kcXHoDV6aOe20MwVA09_4JMA1SsG4LzNo_Uhd88Vs_1BCrPuVSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ipg83OBRoANs7Gg0viWvegS6J2c4rC-6LA41xF_PZeg-dUoiR3_hZ7t12DVXCjdMWSfI05CLw_BN6opvav1TcGmkXP5mOrADrKFPtmVVqOnql3rm2gH-6bRFnZLMr_gehVaY8WbvM7SlI1SHNiVOFdfYfyknh28a5uRYFoqeO1KYQ4r60UzeBjh5elozcGKX3tr_7Z-ET2i09YLscr3z_rHGMRggH6KHRtjenjasvSkdTPAfDBclyNfOgV_9CeEfRoSnVZnt4vETG3IlutxjzIf08DxuBGQ42RGgKUBEVI2FXEEDtHANuApt74iKQ4CJVZ79enn-UHVWupWB0-Pjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/okjIq7LM4J01aJ1JolyzykQMFqhzqfdMWDYyWKrHHsJKqjXWpmozd6i9zyixfuDVK4WRU4Df4SizoCINxogLfBEfdIvj2xtIMMmHEZvCS80uIAaiXmcX-AD2ymY2xxli2w9LfA4A0Zn7BD2CIrzVkgwm2yVOYh3bO0aj1vt0kt2wMGuszSF0QxcmDUaKYrZiSJKVZm5k99QfwTzK7EBP2NLvIl3-3vmGrewTZSrQ82RpW_IJcxKr-YUiAxyOLH16DxnquL_sLUsNFmlAsP2sSRp-fbFKWknOKAKYj9M8EjDx6oTI_Xe3fDcCP902k9KstrgFApjFDzSC52ZLpYGgcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78250" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hI78YBlS1r_8-5YUkvrTGjicppAj_xlar0lRAxgyKWv-8cfhgPfTe9XrbUwDluTnMjZTuZNsQbzOr5xmXvtw4la3btFvWW5rZ5_NDgj42tyhlvdcrFPs98M4HbIVnMd8bGwZwrcRAQycJeTI-GD6iREN2T_KvSv5tMGsBC91dP_VDwk5gdABBp61GfPQl7HYAdcli6nEaLGWghTMKVfwowvCeT-sHT_c4FzAkWpG7gEf6SSApOcUtiZCF_9P7XpJuOxoIdnWF-2Ugk1LnsuPL9W0kaORgheiOJyrFdeTZp_Nt84gRZSM3EKqUzhjTyyGFkOEgEDybh26JrpUwrSpYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران می‌گوید یک فروند شناور مدیریت‌پذیر از راه دور ارتش آمریکا را هدف قرار داده است.
روابط عمومی سپاه پاسداران در بیانیه‌ای اعلام کرد که این شناور قصد ورود به «منطقه حفاظت شده» تنگه هرمز را داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/78249" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
