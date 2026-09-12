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
<img src="https://cdn1.telesco.pe/file/qR_0to-ITAFUSu8uFUJA3dA5o1Opxcg4MdKFuqWv9xqvX6fC_C2tE6aDHTPQxXbC6R8bktbbZj5hviwAa0aKWp5NVxanyHy9NIIp6urs369EnBY-UmzOe65KUQPt4l2vA2oqBo7IfARL1ntPywRm7S15kcwqaknjVqg8rPVSWI1oqexsCnP40h1x-mzG8rwFnOB4h_2tlQmsy1YNTPqTSTrQIG5Nl3KJoVFaYBQHRHdyi7kLyx_62zcUaPfQc2pHXC6VTzQ4nyMfukjTq2GuxyjCTGumD-2fK6r4Ulw6jBYHXO0h9Bi8OKLQ37OYRRIn-aijMF_dHAkOj1mBYFpXww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 17:45:14</div>
<hr>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ad1uejJCWUeYM-z-VQxlYGko7-LMn8-0sq4CyviOUQxmDQDXALy4f8kypLKvBmJqe7nSC-f8QSchD_ds3L8HQiq93WsG6Aauj1gwq3HSUzTMPwYknwrZqw0pHci_70Vn8nlzKTCOGl-HrGoBcx_LTa3udGnXFO-WzouzoUtV8ltwHHRd9X2aeNbtovlSo1Bz_S6KXFmZyryfgY_wdFHg6rUoa0fAUj5dEaA3G9uhd3meTSZCQTLhkUC_6mgNk2zlJL5wzxDtkF1Nmjf2A5OigYswXGCsJz26xvvIi5zhutFnmfkaUfmSYMr0oLcsiW3JVoOyJteHQpsQ-bLSk1Ue6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aW2qAby0cJSuQ8Ot4nwy2Z4WJTVv68FyKIFKelFCFMsNihte5ztyZsxRo6Rz1U8zbnggWJl-5bevNnSv2J_TtCvk6LAycyzrxfHOjCgyAshrJR3CVsT5dx7t9c72Q8prEIyN5RArNodTZyU9foItMwWyGjpoDFf8fkC89QoAT8QEdOoMKyRsRTkAw6O7sNkP_kkIxduQ6uBCCdXMHwNpPH2W3q7avIQGuauugHlatF58RJr_Wtz8kY_ajT62NHfqgfdo9x7h98N3pGIbtMU9CmodoXtd00QNSBzm9xpYaX5HN14DJnvYaeH4_zQdv1CzFwgp04kX6RGFuidJ9Seebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kmtnJMN6NUiNvVT3vI8wlHoq0bdCtniyBc-m-v82EQIg9KTLkj9_hEwghIuknJPfYh-9XQIuO6C6ueBe6DQApovcAu9nR6G8SYLSwomaAamDWHhWR6Tuw-0Mr8kdinOuoB3hJpQ3Ty_104Q2G5AJemdexIVUjlU5iL2Lc_BWgvI8NehA88UAlZktxFQ5w8xeUbEdhHxN8x4y2te4faTW9E_ujT9j5Ap0ccdIq2PdTa8PQnE35raDo8_a1wUs0V7P5wfv3jgc6PKHc7bCnor3saWq02T5_6Isxur1JP0Fa8bSv5PfivjnHg0gpQQLUKEoRw5fcXx0nnodwkbsFX8BMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0Dy9vHwjHjqrgB5I5Aw4k70CN5FIP3U2CGqvxjNHTIMO5F48QCpC_yV6q1uTD9whjPjhYLcu6kT_qB0QEaypWrlwaJKhw6eFipItc9ROatVdk7fnW1hcnStn-a8LUZWA60QRdxxwkSYkvavaZd300mv-lljZ4V3lKEcAy0tGkcv8syyXGTQPRQ8Mr_jKWR5t2lwHsIK4gqnr0f3WukM8UGzX5z4khBzOBxap_hD4kAjxlXhbelqZqSa4mxmLhdr5BcU1BEapINflRmMG6b3y_mec5JqyBrJ0CE8p-i81CmekXijaToe1m0mQ3UQ4lYMyxtFUrMzOVVc-oQS_Ut8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=K9j8hR2hh67TGBgLaK4NFUsEda4bmbma83nKmzqSNKZaXeAHSvSLX6d22qBtNWEYVRtPw-kb_wZXao08YgAPigGWizgS4PS37wHk0Jan3WNHahlD0jKBEJldvZMdfwX-k2KoHNdsxV49UdJ-o-Y5PwFbd282EsvHm5Npf8opykXYXQBryI19FCJp1JShAYKmeltwccjqO0C97dfvT8G6TfGKHNLTDeEEesQLyJ2X6bhw-cpB2H3BxCyUEm_MAEJLI0wIqdIPH1CvFPsw3Rwrt0qv85P3JgSFA2qtWZSsnojtVD9P7nk92qbTAZN-KX-TJ9_nt375AQcYcXr0ln7HYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=K9j8hR2hh67TGBgLaK4NFUsEda4bmbma83nKmzqSNKZaXeAHSvSLX6d22qBtNWEYVRtPw-kb_wZXao08YgAPigGWizgS4PS37wHk0Jan3WNHahlD0jKBEJldvZMdfwX-k2KoHNdsxV49UdJ-o-Y5PwFbd282EsvHm5Npf8opykXYXQBryI19FCJp1JShAYKmeltwccjqO0C97dfvT8G6TfGKHNLTDeEEesQLyJ2X6bhw-cpB2H3BxCyUEm_MAEJLI0wIqdIPH1CvFPsw3Rwrt0qv85P3JgSFA2qtWZSsnojtVD9P7nk92qbTAZN-KX-TJ9_nt375AQcYcXr0ln7HYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=sr7_RroRq7InjBb3z6xY54CBFPRKPUns6D49I6B8EVADfhrv8nqa-hHn6ZXhdN3bt9UjJH9pC8lphdHM0qcyPrBqOdWHYc-8ArHC4yK0if-RNHkVrIwQQIut9V071sH5u3Q3wS_LIzTcTTQscdU_huq4ILYnnG7-R48QcM_KYiKksk0QuE_4MVT3vYl_waDzC14IZ1adyDQib_fC5oR3BUA_zdode8yAYnBPAb8nNNQ-g5sSp0hT05G3mi76BlrUakCCJju-8aBpEmee-O4lR0twXT6dW_KctTKioAhgGgJKqTmHejQZvIWuV6c6KEPvopaJDTUfxKG5koLkIGlwrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=sr7_RroRq7InjBb3z6xY54CBFPRKPUns6D49I6B8EVADfhrv8nqa-hHn6ZXhdN3bt9UjJH9pC8lphdHM0qcyPrBqOdWHYc-8ArHC4yK0if-RNHkVrIwQQIut9V071sH5u3Q3wS_LIzTcTTQscdU_huq4ILYnnG7-R48QcM_KYiKksk0QuE_4MVT3vYl_waDzC14IZ1adyDQib_fC5oR3BUA_zdode8yAYnBPAb8nNNQ-g5sSp0hT05G3mi76BlrUakCCJju-8aBpEmee-O4lR0twXT6dW_KctTKioAhgGgJKqTmHejQZvIWuV6c6KEPvopaJDTUfxKG5koLkIGlwrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4B9OV8Xge6mTU_mGgIgFlnRXu3RcaMoosdMtzwmDKKa8I9Egzp8u4uAr2_w2ps8tP233xEdrz654DxUyLog-aSVd4wLgKppkktgixZc0TNCxNDQBJaB6ssULGiqe4ihP3ISBg8B78-tWqp0-_PlQeYW3l3LLqkgcY_FANQajVEL_Rz7CkUbh6_uepQzpWsEM-iS8JUpOcagLEi4oCwwvINJeaHTiW_XPXK96WErAEe933kzmW5R6dPmVvUNemBDk6vtq0Db7CQ0vbX9ayzxCXRGr_Ytn2lj0XzHVDRiwV4jSqSbRB6EnzKXcyQovEbAEBj0M8K_K13zHNoWrF4i5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTgds8V3Lp16HZtg08w5QRsW-wzXDXJBEQKpnbp3_i4ZBaTDDPQQCj3c_aSaHSa4MpgzMPHfGS1RY84_Z7xlp94YOhU0KRNjxjYuOdYuJUXb1tXOyC_GOIdbeo5BkWjib_jJbKNCp6APGsjZ06fK9by-lqDeAuxEi1UjQbfyeJ4eL29dsQCsF6HAbL9_H2GADE-FEgDnrs93kCgzH_ODouOIjJUbwzPIyp0TEULJ7fYaVsT6mgj_IMCFe4mUVqENl7tb8H6xL3GKj8L83pAHpPND4l7AFoZ1e4Ct1td6OAG3f4T4hPQAP2-u-kjGNeg_CIdmDKcvkKmQordyb4clwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnlH5CEZ6mto-Fm0NeNJTB7608_OD-zvYLxx7F5QxWD49mcPyZzHxMWVpD_LqjuIez-MgVyb7yxSlbIBGAuci1JYNVmf2U1AB1b7xuSiZqaEtF_gCfG6jSi5Of0Rk5ad3xEZNsexE4tsXBHJwzVIsbY1UIhW1kA5O34x61bFBy8MXdNOBlI_JhQ4vgZ2GbodL1Zc8qJrbhwdZS2CEW7giTdpx7v8vBCbOrd4rgEln1c0_06QPDwmS4UXAgPOmr1mHg32eR4XXDcCJf1x11y7hb_O56g8rtJWYnbROfNN_76EiHKbzisau4CB_pIhprISnVLxhQOgu-3ZliwqM7ikAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=A0aJbEV-TzhEH_PzySQJ01Gm-TLqHaP80cvOasxJkZx13e0EMRM1nw7xRKXEYdSml3kLiSCqFBkG6VKFG3mTI4e-hx1xJFsJ7Z-9lXsb0cXtjpWWC37Yo2I1k7wDvichl4FSl85b6_-kNZNaMxLXd4uAvNDqvCLDEdCwZZ_nm7dj6xjvkqhP81v0EcHXlAzTP3uMk8GOpu9OVcAjh1JFFy9zrgHygg30AlNuH0L0NRlqnttlglGphGSgJqsh-fPCyIf34gwFm0kY50o_7YKM50BLVAe2OfvLUzYnsoGdcEliUKv83d5kx-qFzdzFPwJlSJKwZoIssKtsn9fnFwW_lg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=A0aJbEV-TzhEH_PzySQJ01Gm-TLqHaP80cvOasxJkZx13e0EMRM1nw7xRKXEYdSml3kLiSCqFBkG6VKFG3mTI4e-hx1xJFsJ7Z-9lXsb0cXtjpWWC37Yo2I1k7wDvichl4FSl85b6_-kNZNaMxLXd4uAvNDqvCLDEdCwZZ_nm7dj6xjvkqhP81v0EcHXlAzTP3uMk8GOpu9OVcAjh1JFFy9zrgHygg30AlNuH0L0NRlqnttlglGphGSgJqsh-fPCyIf34gwFm0kY50o_7YKM50BLVAe2OfvLUzYnsoGdcEliUKv83d5kx-qFzdzFPwJlSJKwZoIssKtsn9fnFwW_lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgf-eo-T-2IETvru-dEZogNgLj3gMe_7PrL1l2HpYdbxBdVExMeRRBmKcMZpnSI22AW9DNImOwQVVH4sDDiSNlpwiBQ-_9TDFQoXCk6IJH4tZUMK3q5pGUS_hmLr_hOYDPWebEChIWq5hmPaEamri-ivJ38UhDSxEQYb6opzazKyY0Eg44clvsiUo7lql-gMcMtlPd-EI3qhJ-CWczu2aSCNheqonPs8U-mt1MTyG5XMR3L1aC63F2rdfIBiwnth0hGvUh1DzvAZr2CkJhdnRmwwzr3036iiCZUJ0jSAhHvhVL_rhX6I6E8dxA0NGnAhgbubf5VngX4E6zUWyYPUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oByTvs0VEZqTwjhJczBmg6qvJggKf37nqHbcRbEEE_HliBjao7ON3w5a3GeyusFrNzmHl4KjX_g1P6ml2QVRNJa6ed-1ph_muiE6W27Zsc0gHOzP9ij7nXyahe5Orp79Mz4RAjFWzUYD0GHBamgfqPsDte7UlQ3opH3p2w83gsR2nmY7wSa9NxWHYzbDNLQm-t7x3DBh_23Z2dSRRKzISm2TFpHeUwdsLyE8oTTn8a3JO7VnGedgQ9bT7AZX9eA67-brx3UzxRuGfOlPcehnmf6zLvZOiYE_6EQghfBebRJmMLNAK2HHt8GEAbe78kvmFxGtJzvBmO5DHEWBJNfv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvIrBICMqyM3J49MySDDoPGaEf8aEEHhmnJ39OM_8e83DsQ3h529NlOz_R5WVm5SEB7Guuj035_I8yvv272kILkg85qUo0wYCUF2Lg47WkvPWl29dtDGjFGMwDD-RSCR5q1pgdoPvyMaRSgSSiGt4v0RaB4asKiw6xf4MkFqLw7CwNgjXimShPPScKkCUX1I2q7DUJEydOTkq346XEK2DFb-I-RIU50V4e0ADZe6jTURhRvcZWkm7y7mc0c2RfPmNhd_GpZmXf7jJ14cvh5Io76IZnFTDG1lINUSI48IJGhQzmX-YgqQHq3zd7VKEp-aNxs7l4eYoMPUKwqHggUFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=uNYUgdZNZneRBSNcNiVG4r2zaKPfZd8G-oW_TgdlO5Mxs15X01J8LwFDYJlxwYXa0YdXFD3ApT3-trj6qwCk0S7NYQ2S-Z_WS76_v1hsxlofZ0idAtknhhx7jvNLr7WvzWIIxAxuSleCnk7z7KbufeoYJg93BGiLvRT2Zf4BF1POAOs4X2W2YwMh-fEKxAdoJCVtV8LrP_AgNFwjjKYN02YWfN1GwVVli33ifQLT82q8uPxzWScjFxP7PSsv8P2mp2lt0NqKDiqutqi9tF74uZqUZWzux4SFQJ7T5ZO8YQMtWAhiuQc9GQ3f_5oTVn4WPQixe6gRu-bHFT2gu1Yq5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=uNYUgdZNZneRBSNcNiVG4r2zaKPfZd8G-oW_TgdlO5Mxs15X01J8LwFDYJlxwYXa0YdXFD3ApT3-trj6qwCk0S7NYQ2S-Z_WS76_v1hsxlofZ0idAtknhhx7jvNLr7WvzWIIxAxuSleCnk7z7KbufeoYJg93BGiLvRT2Zf4BF1POAOs4X2W2YwMh-fEKxAdoJCVtV8LrP_AgNFwjjKYN02YWfN1GwVVli33ifQLT82q8uPxzWScjFxP7PSsv8P2mp2lt0NqKDiqutqi9tF74uZqUZWzux4SFQJ7T5ZO8YQMtWAhiuQc9GQ3f_5oTVn4WPQixe6gRu-bHFT2gu1Yq5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T2GFA7ikX3tB-MNHJBXZF3nVsX6o9b6oBEeI2HxwWQSvfbmbtleYVCZDw5n4cgq7CgVKQ-wJlul6Ubgj_30E7SBxz8iGfysjrQc1r0cib7nBX7Xtav_Vx7FlW39v0NZrdvs3T5mA6WZrgkpubKYls7FinC_UpRC-FozEO5I97NpWCA8DHHCxxo0Foa7DQ5ZJHZk7lMOzPIIRARufFEIWCp_WbrMVJ09LcklYRdZ4fcQ29iA5S32zvFfc0F4Gqg4L2XTpUSpwAINGfAlDTkT9IM37UumaH6hMeFZjUp2JWMxpDLRUDbN0CDO-sx3EdeaKCdoLsAP9ZHXBvMLnQvwsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=o7mnk17ImzT2XyW4tbU-z0CcSm4qUts6cAR3UhWpCl8O6cCwpSxF9DRN7nTm7xt8Jj0bdF0l1zI_2sWL2xR90lVukIXUpqV6JneWUuZlMj7hN5OUJxi8k3NT0GiXCl2i2D-ndz6kumARKozlLdEZAv3FPmBv0PqU0hRNZpYpZ1vLO4iQh-1_KqdaRONvfinV0l7bQu0e1t1hOrq77XEB40Cf76L5w4oGoepft762ERg9LD4_fFvMR3FUqv2gSxnln6MrPD5hqjJOEz1zHExOPbmMf1plhVXdPYHT7iBWaNWs1y4GV_UGBypoVY6QhYBJec1f6GgwVnRaVj0FM7hHEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=o7mnk17ImzT2XyW4tbU-z0CcSm4qUts6cAR3UhWpCl8O6cCwpSxF9DRN7nTm7xt8Jj0bdF0l1zI_2sWL2xR90lVukIXUpqV6JneWUuZlMj7hN5OUJxi8k3NT0GiXCl2i2D-ndz6kumARKozlLdEZAv3FPmBv0PqU0hRNZpYpZ1vLO4iQh-1_KqdaRONvfinV0l7bQu0e1t1hOrq77XEB40Cf76L5w4oGoepft762ERg9LD4_fFvMR3FUqv2gSxnln6MrPD5hqjJOEz1zHExOPbmMf1plhVXdPYHT7iBWaNWs1y4GV_UGBypoVY6QhYBJec1f6GgwVnRaVj0FM7hHEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8a-uAt3eEbkju7QgQnCQbLSlqamxe-6A5ClLhUYoOOtfOJN3ppwyH52v2qWW1I6ZDF0rrl-UoMcEbH2OkL4x_7p3Axsa08O6nbH95YpVmxcjJCu4lkzBS5FC13mQJTqQIykAeGUxiTRn7sZAPJOnXYuW_Y4uTVgD8lubM3p4diAY5PLM8s3VqV17mEvx30mHeKnU0MVjAQyHk8R4T6Mtk03uA2CPjMGyCAa6Efbip8s3c7URLDRQdvPItmgDXwbGT9-0RlPirOJKyMFudU2SkE7i6N7TXnw9JkxFMJD9f5hgW1gypEIgI0YhiM7e1wEQuuXdV0Irik2UpfAsM6eFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgOrK69ABUkqk0AsdRMvU-OCnqaLti7iOOzncSQYheuDJzY00YPSZnjBgmswZLYEyMjfy-u8Fa-GPVPROx0e_UDVaKl_bOHH9Oq20XwCaUcg6LwQFBuZkWuZZNu1YUU5DSWQCVbpL_hlzWxw3yhhHvs7BDKbrxsLjDYGySivE_ZyljJHb7pgOtvDc0vuLa2oO-Rdh4OjmUYNe-ECrI6U6umZzfwI8xECShilL41JAEJ9GsnshLyFTNWuKTYhcnN_iZUxdhojgiKl5cfb7VOien-IiEhNQ8Ujc-6QadjkMVRx4DIklA9sdMTvjo8Ry9hCAOFdVmM8GOLEMOuKGtvCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgbcdeOvFTOVMB58BInOz512TmY8qvrtMgemjPtgUj3BbSlePRgR5KGzq-4ZDgtlIWv_uuwXVV3wky-nnfy375-i15iPZkWveslWADCtSkjR2JsMtmikLhK9DCitvtR9vInpTtIRB7iOTgrd33B0QI3Kv1_ouwWoJMM7QKFLEDrZNbNHRv9udvG2TP3sXZtATr6VCikjD_I63onX7fvVJV_7aoHTOxq7tQtbP8Pj1IMdpeAe-288C4aoTw9yduRemfXqdet-nD6WaHZfdYuIHEpEQmdql5N76ehgNOYaPMb1npQjy1WA4uMyQNA00WOrP_H09OTWOZI1l81WdPIVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eziVeRumQ0iXncEdz_IztKE-O78MeBwxBuTF8kvFiDQ_s2jqWXKvYPHrjLga4YJFZjXLt6KE2ko-lokD_W7D1xMf4ciCl-8o0ysIEJrUbeJ-gBiuyFLD-mmbBDBmVAhhU0p2B_u-F6BqGpiDXhmLIcHpaO2d9b9wFcsMwLguZ9avXL-JwvJUsrFzQhfDsTbdxycSFOVeUeyDddPYiJdLo_qxPvuq_wYMJF-f15q63j_bV_0iuloAVGReqO6FPZmaaieJc2Vs5KcYbXFn2ozdlsc5Asb_uwWbezNk-P3hG4HFXYnErWjN9zgKO5BglwSM4dKrBREbJIM9FHcTPRYQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HT_WziJYUWtHArFpge_2JJ0NO13GddtnBv7C8XYQCeUCEWI-gIt7RCACyndJQiU73v-o2zF8nzvzUVpwul_SRTWSV63seiGWGl71wPRrIgsCYKiSMlSVuR19WEG30fiKi9n5tsf2aB-ZUpzP37iVk8RR8cz5fOvn5BygZnNdhoZp_uPjbr5mJcrOi4xybaZ3Mo-2gwLh-xUTGOVzSEu3DLzgpJiJ9mRxDprSixoa2tqnULfj86heVCq0mraZ_D0znNdAbLZygv0UJgNSpjzK57Qer4lqHU5iDUbDzifGtIkujb1zigqoZZ9OqzDkzYIAF014Tdo1oAcgwSQ8X0LYeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bly3HxOetNWwtTXTXg49pXj18x0XGytDd88Bjs9t608KUPQGJlbgYNUuyUmzviznchIh6xBFaZnZqrHSyJwyvy4D5mWDhSw3vtMu4rVdAcdkSjm2W7CjkDQXs1c-zrmF7rubRm0XrSmSYwZEC5JjbNC_tyjg0YbQOiSBbwdrbiTVVmZpKwsvM0VxIIe4ny3QleT4XjrW0FLoFyZDOJod3zrH5SbgLa3FY-uJxXj-TT7e_Wc3t3tXnZJbpuStP5bL2cyHLubRmTxw3MaI_NsgLp8KWsHEsLD_0Gi5FU03P1jXLXW45g-VZXLaEQR9PXqaRfBIB0WPanvDz1Amrg8ctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CAeby3L9_4LY31cY39_xd4qf3dz4jc6eznD281HzUqZSO3LysuPXmtqpvZ8pU1wSGB8NYdROXd-vvd0mZY1N4svAEcNilj-f-frHyvLyD4VeVGb5fACRNg7l0zcCdt0Yvy-Jg6mhOaI0HquDvvrMCmWScfcjKy0UZROV9rjeOQAfjYn1KLMwsMg7Eo_Y36jm2sYPMxkYBzn9K6EKIE0RyUF4efYirio-qU1SPSCxiD8BUvn07t8BIPqP_E7SDbJGphQZX06j3uxGTaK_RolW79htKTLsAJ5LExRKqHBhTBHAQa2LhHzgkkO4p_fHq71sw-EGjDUQYncBMTWyzqRzKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NekozDxOki8LblFTFkr368_kUo8QwNlEmS3RCiY7oCGzxFbvpTq3fhF3TkViPcN6LaAN7lH8DHjUZT0JLm6A73rE_uA-yMQEcGDsNjnL12wWGqhuuQakXmWAPxfoU-Jzv_WItUH_XqiQ9Egc5XAe5W-2y6Ma1OTt3yinMfNhFpkj_j_3rr-LVSmhQ2iKwuqN8PcwqAa0-eynMkBRB-jH7KT6Wze-r-fJZh7z0V5KL2o6-sRZ6Z04i3_gdIw0Dr60uzd2ZDZx9DWhHSuxwXwgTtWWMBXac8DzAs0XGuVpS4P_9ODyPuhBpaqSaEfy55VO3HDKZQ-aVArSmhdXiytYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKzAl1z7XpbrDEGizbx4gANln4E55rNvWcymWqYkc2BAbn4ZcNwKnC7Z2m_Ru9DoVDybc0h2f2-armA438D3RN9bpVDmeGkc7Y35aUF4PzTVtcLwJFLdVbQMYrHgdst-CUUOfYf6B9ZCObG_egIQvqfxTQS1QKGfL351xKaH8HVPIhai2cUFg72NeUxFVQp9knowou4sjzRpdiZFbENSXkQ6Mn2VHJubrwsd1aESeSGek-DecBYzaI7cyv5ohhnzpR_HfIdFUFiJCGjIXPhxIITbiXDseL8FtYV7Tn1vwd4O7cHSjIRFBZS2L_diXKsh6XO_WJbS0gU_emVP2iM2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df4kSp32y0KNUUGJhjQ8UGV0wpEfe_61ZWvJF_8rya04pQBAt-E8HlhuLI5MQpMU2NSKBzP8BVJUnA4udRYfMU8ObI-Ey9YyCcM2qre5pQGNndjQuCGvWAGtjz659U12hbF8Qgn7abylPFhsT-VQxanVuxVHfltHkYQxNv8M67wuEX-aqBFNOutfo_pXNjjY9li22soS6wJOEV7UbWW32jsUmIo_LTWo89JCk6PiLI3dR5mSDdmV4nbz0AviWAviVYal8UsisVstTLpd2LwlNyxU_4YosWEpYuz1LzQNXxeevGIPNHbeidukn9BoEoVrvD8NcyJhWX55buXpqR-leQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=PeZzO-YkS4s03DPZTme7AQcWBTXAAfy55fBkVS07mNRifkVHI5E-OlKTGHA2QZYSbYeoRpnUZn_c6alPBHkzJGcNz6nKAIz_ReCRvq_PZd0Uq2S4zEPsYRpZlW08DEufeWg-kp3gl62TyCCgQQukoIFlToPmRWI7kIlPxTHIjtPpWq5Qm_PjQve1oyf_4HVmJCUYSohSXQ8JIvJd57-VmpbBX0z-OpaxdTH1gqGtCPxTTGX8ICobLdwPsxIOPGWHE-0ItJwtOEc3EJ6uxakKcM3F8PgpvvJUXuA9gJ58v_rz4RDxJLxEhrOd4KnXuEKsLwOGhMtrBfSKTFDkoiq_4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=PeZzO-YkS4s03DPZTme7AQcWBTXAAfy55fBkVS07mNRifkVHI5E-OlKTGHA2QZYSbYeoRpnUZn_c6alPBHkzJGcNz6nKAIz_ReCRvq_PZd0Uq2S4zEPsYRpZlW08DEufeWg-kp3gl62TyCCgQQukoIFlToPmRWI7kIlPxTHIjtPpWq5Qm_PjQve1oyf_4HVmJCUYSohSXQ8JIvJd57-VmpbBX0z-OpaxdTH1gqGtCPxTTGX8ICobLdwPsxIOPGWHE-0ItJwtOEc3EJ6uxakKcM3F8PgpvvJUXuA9gJ58v_rz4RDxJLxEhrOd4KnXuEKsLwOGhMtrBfSKTFDkoiq_4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cYu4NlTR8WndOnYZa0AAnqYvuVx1R_KXiutQthXB9TyuEc9tmiCosHZglD4c1K6wglH53yvAqg8HiDE4X7jd7DLTOsWcxfucFL6v2l-_13ACvfu3hP39ioZicQmyPYlyx8a08aYZIpAPXwjDl_NCnTD5FvUCyFAiC98oVomex74jtc2Wuw1qIGVyW6qG8qtH0k4VTS_yxslUfloxewz_JTFLU9C5GHxCyV6jxOaPZajBLHWX1zn7lotn71Ms5wZx0K0a42P8Fl66EygAeIAyEt9B0WRpd4AivZmab6pVt46DcDhCROy-EADFK_dzZei_R6w1OxOHykaZe1aKlPEvmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HcnvsFfxDLHOmzheOYiHEXPsc0ABHPTFu12ml201RLzUqa383S1I6G1qzCD50xH5MoWDgt7R99CGJaN0V-utc5wpz_awazxE67DuNxhrKLcimx08xc4b9ETu52ztxTtZehp9UAzaqHVdc7n4uyN6pNkJbPoWCEMlGtvXPn29_H1Y1HglQdG0Gs4rk6rqom8te0CHgOCaOSW4G2b8eaV71ep044mv8ucJ6fhMjI0hLwJnuvsQJ5Pit5VR7rxoIQYJ1qjxQsY2Wfx-RX2umIYTpojsgTcy3i5-tDOwFO2qGASoFsP33A5xBqX8nEHlEE-U68776tqTSRZPAdvONloyIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=Vp2LT-EMW0pPMZFDDGAgPzi_gIxOPu4pjqba4XLspf7Fq0SIdwlniJ76KA6mT0HNtltTcZfoXvRSwWBOchoFmNIGZmTaOjFnSmARg7YM9V8tcYpF4jYHqzPTzptXRRWyBqzb6FHg59lB5c2wdMPjAcAPetKmHXraoSnM02g0Vg4OSg-tgzRO11huSY3m4kKpMCSsN3b-wXHxy4TSmdNE34ExUwZK_2QanEEQ7F7WPY2bOOwlJS0lwTQogxz8U8LtkPoNwxv8h0mXsoF5grn9hDEGUU9M9T8jkkkh7H_sQO2C_M5yHSqow2enXIlmbyrfe2cr9y12sNlBAGmEgHI2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=Vp2LT-EMW0pPMZFDDGAgPzi_gIxOPu4pjqba4XLspf7Fq0SIdwlniJ76KA6mT0HNtltTcZfoXvRSwWBOchoFmNIGZmTaOjFnSmARg7YM9V8tcYpF4jYHqzPTzptXRRWyBqzb6FHg59lB5c2wdMPjAcAPetKmHXraoSnM02g0Vg4OSg-tgzRO11huSY3m4kKpMCSsN3b-wXHxy4TSmdNE34ExUwZK_2QanEEQ7F7WPY2bOOwlJS0lwTQogxz8U8LtkPoNwxv8h0mXsoF5grn9hDEGUU9M9T8jkkkh7H_sQO2C_M5yHSqow2enXIlmbyrfe2cr9y12sNlBAGmEgHI2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=AYGZDkAyK3ToI939CaKIXmjojzB3PnuJupvOEiUEkm27bPmj9r_ajZ_iradQCFrkYRGtRkd3oAzxnFGLWR8QAQs_cZxxj0LB2UWew5ogeqwQtd39IzpKEwvAALPpU0TTpg-0ebAoDlCYHigojz7MhO-TiYPUMw9Ce-4xjNXFCqtJTrd7Fhhn0SA2J5DkGwTqOuCGs4g_DLvBFx1m30ag2dkS_pqJ6LqLQL3fBvIcaSIuJio7A4LHSMXdVi6Jh--GFVera8y6RsEs_BNUA7xQNfZiHhPhqEg1gNVilcLAvX2BByR3RU9Kd2fC82hbrQBSZ43ZM6s5mqRktTr4yaaVCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=AYGZDkAyK3ToI939CaKIXmjojzB3PnuJupvOEiUEkm27bPmj9r_ajZ_iradQCFrkYRGtRkd3oAzxnFGLWR8QAQs_cZxxj0LB2UWew5ogeqwQtd39IzpKEwvAALPpU0TTpg-0ebAoDlCYHigojz7MhO-TiYPUMw9Ce-4xjNXFCqtJTrd7Fhhn0SA2J5DkGwTqOuCGs4g_DLvBFx1m30ag2dkS_pqJ6LqLQL3fBvIcaSIuJio7A4LHSMXdVi6Jh--GFVera8y6RsEs_BNUA7xQNfZiHhPhqEg1gNVilcLAvX2BByR3RU9Kd2fC82hbrQBSZ43ZM6s5mqRktTr4yaaVCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DDO_tfWGOzWc8CNmDzt_qp86lSq3KUliXK47wBURaSlLgwHRHW8h4QFsFsWpL-A1wIgZUj5MgbF8SlJYvfBGuajaVnnJ8zDxD1AHbhLwCQrIs2l2Tu4OfJushn3KEIyL1HOl_NKGf4uz2wIypVAbciB2H5TBKFwOVxXwCN10laW4N8vQqPSQXib2XJTmkkqR-sDzL_wXfgg7NNrpk2DXiQq_I_E9OFkPo-HQBSo9tgr3YBrCUzFQiR8mOmTwMQ2ugpc8LU3OOs6HImnZECzV1RzA_yOdwU-sP4bqTVNSN07vUMj7KGH6jqF33T1szt9tarGv7BhLCz1nmUE8KBEKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m7b1FVaxQyMttZUSMd9K5qmTtKETNQuX4X4BdmRQ6m84PsAtxXepqNLe4u0A2F4CFzte_cukJJjngkpRLIghv7vSDXZc3nc5_EgEaPsA6svyDmi-qvBtf32O1EPk8ufJthb4irqAev95IEqv6GK9PT8b2NyB9tcle6_lEvpcKdncGf5Sx-UTXtfx9uXhaZd9B2krAn4EHRoaR96i5NFKP-darbQ5hjp7d40uGvO142hqUQGZ44jnb6kAKdvYqRWfFkBDS1ImL0QqVKh8dhnt7Z6RpLwzuMkKWMDVIfXJhpedthdeH1Fb6XtlbiXPaEoxRPfQRCmpmVieT77-RQ4cJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=bqjHWJLz3P4FH69p8j620XiVC4HtwybIv9fSslbxYzuZDpreqpMbyTLnhlLhae7MZAv-znQeDYpQ_KaGsiZ-j1B4ENG_GztBeF5a11yW7p6Zi_XNkTaJo6WxsjZYICxJe0wltlckmgONamXOBw2N9qqhw1ZmJzw-NQcz-h5V-CU11v3QeZOLceqxLwKcOXpUU7VH9chcBz-2qD-xIBHqy7OZw7UmcpJgAOONI1QcQMchUvssqG6XpWbXttbhfMQCFjZ46ZaHWNQFlLJyTJsuGfZ7Va3VwjRZ1ktGn9e75TAZX_c-a0xVhqOwqspGJGp_70lfaca70AB0XrbwU3bQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=bqjHWJLz3P4FH69p8j620XiVC4HtwybIv9fSslbxYzuZDpreqpMbyTLnhlLhae7MZAv-znQeDYpQ_KaGsiZ-j1B4ENG_GztBeF5a11yW7p6Zi_XNkTaJo6WxsjZYICxJe0wltlckmgONamXOBw2N9qqhw1ZmJzw-NQcz-h5V-CU11v3QeZOLceqxLwKcOXpUU7VH9chcBz-2qD-xIBHqy7OZw7UmcpJgAOONI1QcQMchUvssqG6XpWbXttbhfMQCFjZ46ZaHWNQFlLJyTJsuGfZ7Va3VwjRZ1ktGn9e75TAZX_c-a0xVhqOwqspGJGp_70lfaca70AB0XrbwU3bQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNdHto83yMDMdfZb-nxV0ub18VEM0D1QpLd9fsskGvNw5bfRTttjErLv6nCV59h1LhmVlO0dTpsCrDJq3HTuYYPr6TESvFefUydFbf2WEJVc8pp3TWk0LhFegnDw4211oX9_aj-awmDZe48Z93s_rKVBSTqDWGLzGo0F0VQsrdkz0njr2-3fuzjGT9dZowzFUZcUhvUj9z1u5j5_d9cbFd68RO9NIaAbdbQlRhqOjqSHCKK5bMfiroqJZ7fwHuYR0ladfGYQuyzX0bqTLpCdHhH_PWB7lWGGSiiZgoazEIfzYvH7A7095J0XLdb8GxQnapV6m6857q0GjROfwk2QSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV3dB9iBQuQYMwqYgt1vs3cQRQmLoZiCRCc5L3_DcHHkxFzsAUSf5vmrHYyq2J6CXeNpfeYvW3wPE25DEYLzBkW48qOKX-VaeHkiE6QD6ng3HRfz4qL8cfPlzEZoiaPuHRmKm7i7PHOBae4hbtSpaVgU1Xq1aowyMlcw85Q3n-0ePkKWN2DFk1FI2tPvjAvbWGym9HuptY_y5tY706tWQbho3kZGK7R4HmKqPo-bwO37x71Xnjkud23oBYBBBuxbU_-JsONB47WOD5mt10harbC87nV2wgBadwyiDUtR7pfiIGniInZpzsx6kvEBlfcraQg2ceb3amOscBCWfSFeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhbVCRJnMiNShzg57h1CJZXGoFIE0cjZmUut7nl6_SNiwFpovUliw1wtH5UHYD8TG5dcuR1b3cl-YOqIvJrui-wObrrcahrhf70Oy_OmmmpMXc_eBiSMyZ4J8tEmSyiF_13xJAk4DNwvxo5Xb_dcYjMquKVBxS2wY1V-6R4Qrnp0slxMAXHz6o9wHIEvQVVbnd_GqIGz-5gu1DoQGRPiSVaW5rnRKAGuwYTWxthkuJDX4h6z24PfBMktQ0BzfAHcjiLkacv0x_VzeSroj3-YGPgfwZlMYKrybtDGe3XbAtRcbYLoR3H2UXDTflKebi0cp-GYXKleSo1oUoUYSKqn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O6OgUAi9t3XXEZTjGMN1OFCF5QVPtFX117EZgdv5Pxms7o5LlgYGLHhWitBAGr_eU6mpCjG06aYhkjnjp44GrOB-2kX6J0OnQBLEMup3sV3-ZW07jSnHUisRN6P7ZXCxG0PRkaN4F3l5rYPuSM8wKYgtcOjA7duMLzt0dVYf3lqXxZ4X0Ag3s-bKMIcct_pUkVDtdGSwqn_c5hzf-BCzSvNCr1kwd7yL1b0Mrldl0ooNu4Ixx2s9aLQ31cJHJA_-hHnUv_4HnP2LeYoMKEDOEZ_9-HEwSuaPtbmc72hfcJzeBfgkggEpmLYd7vnzDZI93WSJP0Dgjv1spzjNKEE7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mvxIDgpR0G4pu55ziSpZunxIJkfdS7Uo0q6QU32Kg0uco_fCFKC719HPW-NTo9ga0F9Ou94J-wzjGoU1AxX8S-CFvddKUjbcHInnqWQ3RVq7ZF6vHDgN4Z7SWWNsIYoD0j8asdCg1KdbLp6p6aQt8Zr04S-2Lt7A1kqOfJrWeLL6fGWFsk5YeGqqxjnaAuHlJOrjm-iTZlvIxFg044D98I52YzluL5Ula6b4xlIHtCTKRW1PGKtAUMf7pYEpnpRvllA4iAw2e1-E5NNk1J04ZfBFJ7iW020JiyfNEqKhVq6HjviPa2AV_ynyWrDbAoy970YwIQvZG8fqwlh2Koc3dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78295" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CbQom2bL3y0Vl4TPefz9MjVp6oYaGc6aZkW4Cdg1KnUDzxZMR5_ExBEvFtT0yJeUOliVoYbUQU_-nwx_XC3-RfAydVIE8E3jJ__EJ7yE2Icf1ypHzudERG5vLYKP0iIb-xVrJR8p4gMWsCiwbgRlgwINaj8PRaZSxCWCnNJ5BdJcCYB4W7Ed0N7yAr8rFfbkhagN3d0NqXgYNXiIgZ_IFHft3ujlznUGgG3dAE5Rc7pDzXSLNfFdYV7dUvGRIw9lzUjxf6OKuKHZTRIr6RpayoM0QH2q_RzYM-jRdXBDXVAN8NOhRYY44ZJnmt7ybYNdlBXm44PIj0Hxhdmv5j-7zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78294" target="_blank">📅 16:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WHsiaSDJWaviRMVIuxdqKOkxj6WMHHt7yN9ZwLxFLAKpdswaStXYhBLW6AhydNyYfg9tS27Do8QA4gz5Ql70_32WN6pNrT48XA3TGPXXD4Ni6ahinP0jbGQYrl0m55_BPclAmu0nDc_B8HKSjGfjbymoRYdwp6AY_7hesxrCZ6f5QMtwvfPjn0rGH_RAOpJNRvrR_uwEUAw0S7OTHgQ6iXYJLj_YGiltkIj-k1x_YLOHSja-B2j8GXN1XG6hYEyxSrUVhKV1VcKLA1FkcRq3kdBk3_lM6_Zw3_YwK3NeVD6-qqUrBAnVWW2W17bK4yBHizmrT-WRwQ6KCZ9TCI-BxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ماموستا محمد نزهتی»، روحانی اهل سنت و امام جماعت منطقه چیانه در شهرستان پیرانشهر، در یک حمله مسلحانه کشته شد.
سپاه پاسداران او را از روحانیون همکار با بسیج معرفی کرده و مسئولیت کشته‌شدن نزهتی را متوجه آنچه «گروهک‌های تجزیه‌طلب کردی» و «صهیونیستی-آمریکایی» خوانده، کرده است.
براساس این بیانیه، نزهتی سابقه «همکاری طولانی» با «بسیج اساتید، طلاب و روحانیون» داشته است.
سپاه همچنین فعالیت‌های او را در راستای حمایت از جمهوری اسلامی و آنچه «وحدت شیعه و سنی» خوانده، توصیف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78293" target="_blank">📅 16:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=m55_iUnhGUrxdqGDpodaMt1WgjB5W940rnDG2DbpY0kXAyP7S9oBpLt0hIU1VXURyW4aabm_kNerj8mGBBCFIAj-rLgeg3Eq-wHlivTkxk51PvjG91sCwjuR7BLTyzbsixA1gNKnNXo9Ez9Wdv9ZuDvrIEKuv88tBsZpRrbgx-McCppWdzxy_6uqfdXBu_gtLBek1VVFGL1cN6SAATAqJpwFEUIMD7qQK2vBEFTq0H21R-FJgq_Yh1GG7V_qF-KJ-WdQTZBJB-hHr3JthTQdLQM7DbVdXXDDTwYKCAnSRQA3FPr86MS9e3uztXFrOwjQVaGHaS4Bqs1984Y4yI6Cvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=m55_iUnhGUrxdqGDpodaMt1WgjB5W940rnDG2DbpY0kXAyP7S9oBpLt0hIU1VXURyW4aabm_kNerj8mGBBCFIAj-rLgeg3Eq-wHlivTkxk51PvjG91sCwjuR7BLTyzbsixA1gNKnNXo9Ez9Wdv9ZuDvrIEKuv88tBsZpRrbgx-McCppWdzxy_6uqfdXBu_gtLBek1VVFGL1cN6SAATAqJpwFEUIMD7qQK2vBEFTq0H21R-FJgq_Yh1GG7V_qF-KJ-WdQTZBJB-hHr3JthTQdLQM7DbVdXXDDTwYKCAnSRQA3FPr86MS9e3uztXFrOwjQVaGHaS4Bqs1984Y4yI6Cvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مادر یسنا (فروغ) اسکندری در سوگ دخترش
یسنا اسکندری، وکیل دادگستری و نقاش، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در منطقه آریاشهر تهران هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78292" target="_blank">📅 16:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dB1zTcbxtVC-w8N6B25FAOA1wwVcMfRwGG-EdOZBKLUm6KFPu932SSjOwSDU80p4MRI2BtCcCk7hvjer07kXxEQSHTr7FEhTqJihJYvt7_x90NnvYtI1tBruUjztyg5gt2KALaa3OeTzZPW8xXr_2hgZWlPxaK21zNnmbXFBiXOmtL445Cp_rusP3ldGHaT2398tyVlp_kb5Dru4_Oq49aRnW_i4je0fbuMdeOKZ7b-iBmzuMCQkJrjmAh_mUMOATRHcY0PemBzsfWT8wKyq3NYPK8TMJ02fXedBvfkkOz24nYuPnZCVi04PiBbXJsO9JBc7K0K8Yh9ZcRyg-KNpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=Zc6BMVjR0f-9r2Avk7_pIvO40oM2TykpNBj6hHkmr-PcSub6pJWfglWnbI9qjvRNIJpY-Av-yr610FpwAIyS-PNHKZBO4_-sVYWdyEonAz0kPXo_JKc3OE8a7K5OO6juXbBEB64JZBrzlqR__mr5leLj6mchlSbooS1EYbyWwIGhgp0qhQVdJMxt0Ylxrqh5ZTHYOguwaS0vpHps41XWsqfl1yLtf9tSHycjqUTm4pCqREkp6bAkAaeedLyN2SjtAljAPXQ062AOvDbOL7FpKBTzBGhYRN5JQl6cFIFCTXrsjMbbBWPGPNFBILZFMjOIfR52Ca9hEnhmgoFmP1uPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=Zc6BMVjR0f-9r2Avk7_pIvO40oM2TykpNBj6hHkmr-PcSub6pJWfglWnbI9qjvRNIJpY-Av-yr610FpwAIyS-PNHKZBO4_-sVYWdyEonAz0kPXo_JKc3OE8a7K5OO6juXbBEB64JZBrzlqR__mr5leLj6mchlSbooS1EYbyWwIGhgp0qhQVdJMxt0Ylxrqh5ZTHYOguwaS0vpHps41XWsqfl1yLtf9tSHycjqUTm4pCqREkp6bAkAaeedLyN2SjtAljAPXQ062AOvDbOL7FpKBTzBGhYRN5JQl6cFIFCTXrsjMbbBWPGPNFBILZFMjOIfR52Ca9hEnhmgoFmP1uPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UVBwVDUd71u9myfefomp1PuSSiLGgrvv1JCPGVAUoYjPBgOdSE99URgEfZPMYUdrTIyNb22478wars62LSpGEWzz85wSLByQd7hc6L1_QILl88i34_1BUJ_pYNV-90ZxLcCQ5q_FV7ysS9D912pJMph2g3GYiHEPVLxz9CbNoERZe3u27HH3b_-LhzCfj-8PhmiRjUhY0Q618lY8NTum_OI4asULcqMQNyz9V4sp59ToGrVMZ72q4nGOoX3FsaZPC6_u9OaWrK0YDIJaSLPOCNxOPCDdOGCuh7NzSNsar-UjishqWaTaAcZu-kF2_sq62agDLJA49-Ia7kSfT6dNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای خطاب به «مردم مبعوث شده ایران اسلامی» اعلام کرد که با رمز «حیدر کرار» به پایگاه الازرق اردن حمله کرده است.
در این بیانیه آمده که به محل استقرار جنگنده‌ها حمله شده است.
پیش‌تر اسکای‌نیوز از رهگیری موشک‌ها در آسمان اردن خبر داده بود.
تلویزیون دولتی سوریه نیز گزارش داد که پدافند هوایی سوریه برخی موشک‌ها را که از ایران شلیک شده بودند بر فراز شهر مرزی اربد در اردن رهگیری کرده است.
برخی رسانه‌ها در ایران از جمله همشهری نیز گفته‌اند که سپاه با «موشک‌های خوشه‌ای» به اردن حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=Ci1qUjFBDM8UJ47qbA7OgLl8GcuDqBRcx8eWGIrczl5Rr-inJg7xIFtMHYsbN0OpE8W6UYwlqlDpa2yBAHvLijMpIOmHUPhf7HiW7HbxlzEwm-hw3A0NTPn1pm1oOmAqnptYMImJxxiUaalxtt-11X8GhqXXvgm4FxlmFXMgQYITEEkIDlE9hGsBcohWQkQCTZ2K5kj_7bTTrf3-tc6wirDfRd4bNK7ARLYpii5HreMJBG_wV2yfhfFQMmrcbep7vFJ0tfmtRt0N00NoM5gFWm7qiJ_b66Sr8YSvz_8wAFopY4miZQVkwCwXjfVMMe_O2GJsJ5ZUfXuG4Cc_DHoZgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=Ci1qUjFBDM8UJ47qbA7OgLl8GcuDqBRcx8eWGIrczl5Rr-inJg7xIFtMHYsbN0OpE8W6UYwlqlDpa2yBAHvLijMpIOmHUPhf7HiW7HbxlzEwm-hw3A0NTPn1pm1oOmAqnptYMImJxxiUaalxtt-11X8GhqXXvgm4FxlmFXMgQYITEEkIDlE9hGsBcohWQkQCTZ2K5kj_7bTTrf3-tc6wirDfRd4bNK7ARLYpii5HreMJBG_wV2yfhfFQMmrcbep7vFJ0tfmtRt0N00NoM5gFWm7qiJ_b66Sr8YSvz_8wAFopY4miZQVkwCwXjfVMMe_O2GJsJ5ZUfXuG4Cc_DHoZgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین
خبرنگار:
آقای وزیر، بخش زیادی از توجه افکار عمومی آمریکا معطوف به آخرین تحولات در ایران است. می‌توانید درباره حملات آمریکا به نفتکش‌های ایرانی صحبت کنید و توضیح دهید که این رفت‌وبرگشت اقدامات در ۲۴ ساعت گذشته چگونه بوده است؟
مارکو روبیو:
بله، این رفت‌وبرگشت کاملاً روشن است: ایران همچنان تلاش می‌کند کشتی‌های نیروی دریایی آمریکا را هدف قرار دهد و هر بار که این کار را انجام دهند یا تلاش کنند انجامش دهند، نفتکش از دست خواهند داد. فکر می‌کنم امروز هم دوباره شاهد این موضوع خواهید بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78287" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b638672d55.mp4?token=MJpQghV4vylecmFUP6vpShN1m574YEnrGrhJSaTsEPNsGywTgcOj4KxBxacqb_xIHzvzbT0_5KJwFfKTlPogzOWgorR1wLM4oZesNSYSd8NYNwXME9FObUiSKqNV7Je08aFKDCVX6_mQ_dEFnQFyOqZWIw1o_ztwcAtd06qNX52G-h0WErEEkPINj3-b2-Ggy1H64nZTp5sVOfenPkjxDtIVveSm69deSiDysu9fidb9pRduJmxefJ8annQaV7qiPj_vDk_686pE1tIcj_rdg6eT09aCWqNNKQjXZqEFyoFpStD0zwREhjjVMr5mWoHhvQeMZ3nHwdvkBMiX8gkvdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b638672d55.mp4?token=MJpQghV4vylecmFUP6vpShN1m574YEnrGrhJSaTsEPNsGywTgcOj4KxBxacqb_xIHzvzbT0_5KJwFfKTlPogzOWgorR1wLM4oZesNSYSd8NYNwXME9FObUiSKqNV7Je08aFKDCVX6_mQ_dEFnQFyOqZWIw1o_ztwcAtd06qNX52G-h0WErEEkPINj3-b2-Ggy1H64nZTp5sVOfenPkjxDtIVveSm69deSiDysu9fidb9pRduJmxefJ8annQaV7qiPj_vDk_686pE1tIcj_rdg6eT09aCWqNNKQjXZqEFyoFpStD0zwREhjjVMr5mWoHhvQeMZ3nHwdvkBMiX8gkvdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78286" target="_blank">📅 01:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=LSDBK7pPRdciW4GWmqa29K5wIg796w3TWPkiR7UsKbFArNvTjqPHoz6N_Xh0wv4lq250PoFHYCQqI9qwr8d7uaYdbabNkg8IdQk0UXwpBMB0QD612urGC49va7CC8LbBNr0RD_0exFZUlHhoUEZJX8u5Ah8fZ5J5z_V6WYvciMAJRvmTctfrOoyl9CFIhvyCW6waWq-96ydWxuXYNHFc1drEHqTrWInb0z_VBG-qkJJSCME1EHMxweM7-it1n6VB0-uLuoHMJGvYdrLprEuSxyFB3FTYAASNbqzw44PpA5Omb0p-MJrRsrKT5gVJfToTT_PUDXcXFlpFuWcvZUI_4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=LSDBK7pPRdciW4GWmqa29K5wIg796w3TWPkiR7UsKbFArNvTjqPHoz6N_Xh0wv4lq250PoFHYCQqI9qwr8d7uaYdbabNkg8IdQk0UXwpBMB0QD612urGC49va7CC8LbBNr0RD_0exFZUlHhoUEZJX8u5Ah8fZ5J5z_V6WYvciMAJRvmTctfrOoyl9CFIhvyCW6waWq-96ydWxuXYNHFc1drEHqTrWInb0z_VBG-qkJJSCME1EHMxweM7-it1n6VB0-uLuoHMJGvYdrLprEuSxyFB3FTYAASNbqzw44PpA5Omb0p-MJrRsrKT5gVJfToTT_PUDXcXFlpFuWcvZUI_4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر ده‌ها پیام‌های دریافتی از صفهان، یزد، خرم‌آباد، خمین و شهرهای دیگر چندین موشک پرتاب شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78285" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lVryZyzQkAVzJ2vBumYPVKpB77RKN0kJbdUn0jSMXOoyQr4YvNW4k8nnd5_0Imc4rkYiZR7OD5knSsFjeDQFxx2nEWqLyr3sdSpHF2sCFRHjPlzBPTv_8zJpUmaXKcCArdQZJEHwjErV4_Vl5p1fRYDKqiR2S5-vfbNEglQIpWyvHSP1LpWqdPUO2vsjClHlb4LXVAOievO9jiN39Li2JFFN2XhIuDR229eUaCsHFz5qFOgC5weyhmXF9C6eyM6WXXy7uaznoTcZjkGxG5BjE81c1Mfp6gCnlmHgXyUiu97o0trM4pGbjP7veZZH5o19aFCegF0PlSpJ8Bv2Q9kZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی گزارش‌ها از حمله ارتش آمریکا به اهدافی در جاسک و اطراف جزیره خارک، رسانه‌های حکومتی در ایران تائید کردند که یک نفتکش دیگر نیز در اطراف جاسک هدف قرار گرفت و خدمه آن با قایق نجات در حال انتقال به مناطق ساحلی هستند.
پیشتر رسانه‌های حکومتی در ایران گفته بودند یک نفتکش در اطراف خارک هدف قرار گرفت.
رسانه‌های اسرائيلی و آمریکایی به نقل از مقامات آمریکایی گزارش داده بودند که علاوه بر اهداف دیگر، چند نفتکش ایرانی نیز هدف نیروهای آمریکایی قرار گرفته‌‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78284" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FxT-YtNz4Q1L6CBB88eu-qAOjs6FOqjqStFk7YJmFzsBZlJ1VbGp3xkoY0zPzMmMw2MBX1eMAcoWNyA557Rf-8nguT6pB2Ru1KesW4Xa2_AWnJubeRmds774lBGOhcDFo7t6ZUPn_2Hb2Cnv3v15MSsYOf5uovTHMlYOnYSu1ZTO3LrWjWkUpAMMXRhekSHbvSTFe5OggWBQF-0qhXcnWGXsk-a6YTWuUT2RDjtcnvt67k8L1k9oqGu1gunHdOuyXGlJMV4U4cyygDxSqkfnng_-JZZ12tMpIPwuGNXFiB6SPdnV5aFZfqbwL5632hL4qhhRVmDEol8PESkdO7gAHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سپاه به خدمه نفت‌کش‌ها در کویت و بحرین: شناورهای خود را ترک کنید
سپاه پاسداران انقلاب اسلامی هشدار داد که نفتکش‌های مستقر در لنگرگاه‌ها و اسکله‌های بحرین و کویت را هدف قرار خواهد داد.
در این بیانیه که در رسانه‌های جمهوری اسلامی بازتاب یافت، اشاره شده که آمریکا به «چند نفتکش ایرانی» حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78283" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gRpCohBPksrZh-zFbIsRheSoQevzIX6jsdFu2Zr94VfMDxrAJLUEgF8qI7bUteEVrVD5kRRRw5-ftA1dGKewKc17b7JTtyL79rwAlNFj6HR3ezve-yfwtN9W66CQ2OFHOubPnsckjqtOikjos3KcJ2ADmOlh6qkwk4iESRWWIkcN-swOGU9n5ge3GZsI5rWPCIJfowrrBBQRqnmW3WSiSGmvyiO4kZupvKpZVtDLEnF91Z6yKbV2Y812dhvRFOsUMuBY2Xanpon2G8QCFbBi4ZPkapGF-wkCK_6VF0PSqmMjDpg2aujQtXq6mdoFvFq-P_blGS8d94VMsv5CQt_iSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78282" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1PtwQMTbp1ogZHiJNauQHNIYhTLu1s5BZqH866mrvK2Dnxju-Vhx4nYg58byftcrT9ljVXMn5p00VWRpUFk2F5-hZiskDwJUEW5v1QPznZ7ObzKtCTxHDMxUcG09G-qsbdgK0JER2HVeq1c9U8OpEVkF27BPiQ6xFIv9ZOcq3yApECDq4fy-z9FQvktTYSM6AqPL1MqUHxH5rbYA-TFlewmvq0pTlNVkEo_nHYa6bgFaeeSiTBFpBC3QdKr-LKKhqWRoAuyWgzLOgb0CDYyEAYTIG6H5moxxCnSBR9Zx23wwpij3cXCZeqDNUxXyOjQ2mbMG5-Udyb7j9G2-Dbd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، روز سه‌شنبه ۱۷ شهریور اعلام کرد ارتش آمریکا به سه نفتکش ایرانی اخطار تخلیه داده و آن‌ها را به هدف قرار دادن تهدید کرده است.
عبداللهی هشدار داد هرگونه حمله به نفتکش‌های ایران با واکنش نیروهای مسلح جمهوری اسلامی ایران همراه خواهد شد و پایگاه‌ها و منافع آمریکا در منطقه هدف قرار خواهند گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78281" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">"صدای انفجار از حوالی ساحل جاسک"
خبرگزاری فارس وابسته به سپاه پاسداران:
حوالی ساعت ۲۱:۴۵ امشب، صدای انفجار در شهرستان جاسک شنیده شد.
منابع محلی می‌گویند صدا از سمت دریا و نزدیکی منطقه سنگ سیاه به گوش رسیده و انفجار در دو مرحله و با فاصله کوتاه رخ داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78280" target="_blank">📅 22:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBBdvQ6accSZkQkPjzUj6wIt4Zxnapbo-m_ohrUiHNKUeW_w9uN_QGQur3YHNVY97cPiR3i7TGtetn3PoZF3HnPxMdH9_wIX4bsF_DFm9UJsf2mzPb-E2p3d135bRpXKob2YpEfqaqtEKIHvh_e4623VqPPWEb7u3R3M1HlY4NJESGBzoOEtJBhtZrZgAhHVLAuG6ypgnkLx8UXDBZIxrFKflfM9dPndBbCfh934ypSZspxhHO3xtExb0bCcTjnjj_3XUR45EJTAHt8lkeMrZNSl2AWBm3lCauj2VGAkOmXFD46x0qq-D3cJv9UCC_VLfdGCw2jVJWMTLpo50hLiTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78279" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j99abHY9W7DMio-mrCBIfvijUzMwmuFmgdC9cToKv1mG1nYZkvfkQmCu1nDj1FLL4EIUKXgtQQEvdNiEfr46e-BlTLhv5FNhG8DxRfuKDbkv_3AxAH49GfQXQMa204b0n2mh53O3wFOGoiW52Lmcy72bCH_YpEcEii5wDLpTC0Prr_6xOHSJOhjhCCIQiJI1v6JBhLd7RYMz8z1ItygQIeUmTdXh3J0wIHfmWS9pBaa9iPS0l38nMQv8lu4fhfK0LdTxi5we55BbIk-2B4x301OQ_Kcgzf8C6GUwiBGD3PXMgGGc5_zU5_qyIc4ueFs7-7o__Sd8zzmOv7LlICq2fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78278" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF-tO-I0d7AlRb0tTpoKY_9b7LR0_AVm3djqs22nm4QorsMHdbBGqyOwCwsginG-k7Sj2Trd_VXoTKVKF5l2IiaVFpybcU8n8qGqQb8BR5fiAgq2ZH4eDJYkXmZlHBZEVvVSYhGkZnlCPj4ew4KGcy8vbDdsgHPgfwUR9-neIWTRWtEpunAQ97IJyXwE5t5InYQ3oc6XusQswLRvu6lKjv1AaiPh4YldqCzBjGAWoRR729QkENeIJ3e2WzbDJ-2hYwSg7Sm0f90c4Vjj7OtT9XXEoS-7R4JZxMNcw_ivJDQ9P0ZfP0Q2_VWRBDS-Cbl9LiqxX6476J9B7uVJUX_F5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا، روز سه‌شنبه ۱۷ شهریور ۱۴۰۵، اعلام کرد در چارچوب «عملیات طرد اقتصادی»، ۳۶ شرکت و فرد مرتبط با بخش هوانوردی ایران را در فهرست تحریم‌های خود قرار داده است. این اقدام شامل ۲۷ شرکت هواپیمایی فعال در ایران و همچنین شماری از شرکت‌های واسطه، نمایندگان فروش و ارایه‌دهندگان خدمات باربری در کشورهای ثالث است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78277" target="_blank">📅 20:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RnHSZaacxEDp7xsMMJgjN1y8pdRFTuWmwtVz64R3NK1zZ7GATYNBF6usctBykiMvdysd7slai2N3yXIaTIGJuK2jLhCRpCVIubII2d-OLtu0izRhtz6rMgUeX9ptwMLrjIOZ9MaFCL2CHD8GqWLW8Su4WWB6ZxXJYGgeG6oWSgxGUzr06R4Hx5HxTw4ZbQ1BoYHrhT5zSP-vuHGJaQ5Y_nzXRtPeNIcpwrqdNOA05ao4bQMjU1X_OGRNd9_YLa0pl7O_8KRweMLGLpLYJqcgIWoZzxP56xkgLi3AhFpSKsleOMU8KQHL11pLPAhPzKy3zcpL0k1RO19m-6gObybFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mxKZbH01sUKhviIchl4TGaiQpDpIWJznrmiHFY1XRoACQJqlnc6M0rJtVa3DNUjZG3y5wVauBmkSkecyDP4Tv3cjnWxv0CAv7e0D9zRd_-Di5a_kWndRngom808S5un25UTJZqCYh6fQYGqoENeIm0SzJj40I_ton2lFoThEN6EvJ-suwD59xsw2i0VqUG54DatSrf2_xRZ0FLVwbS55MpCyX5fQb5lOLeW562Zajxr8_O5h1cczF5T--ItTULtoq8qLhEGdsFO5wQeNDAJ_qr0GYf9C9AKjAwsVmRTXqkKJhVP_A1wGk_vfU47lfc9Ix1L72yBh8gpglU7tCK72Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78275" target="_blank">📅 18:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6cdTtuojHrJG-dDKc8WqKsGjPw9xfUtzWWURrHeav1Esmse3sMIupdFUqGcDDrohMeQYI07AgK0u-reW7edpmeDaAqF-MGWrdnymfDv7VNAgGUaf1P0N77DaGH4YlO-W02r_D3l8hIWc4kjr_ZA5fmvJTdzrRzUl35eHRIGJHrwWqSTaTs6ESC9bL_ajpFYJOIIWoAO15XLPDldsU53ezZNl2SmVzIHZ3hFiozKpHTwttg5B7LEgSdpEdK0Rcbht8eqOjrHBnoNDn7RyPMygizL-Kfo2F3rJCQHqf3G8Th89_5xrBByUjQd97WqbMiQnsmhtorz91IQ41Gp-FUrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرئوف اسحاقی، فرمانده حوزه مقاومت بسیج پارود در شهرستان راسک استان سیستان و بلوچستان، روز سه‌شنبه ۱۷ شهریور در جریان حمله افراد ناشناس کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78274" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hEGb99co_tjpRQ75My1RI-HV-jvGCm1cl3AYEhOiwrioSpX5L0cZnaBRW8hbwle4J2EtPSr87eSUpBa5GqdWlGvO3H8Pb73zsZcwLUFV91LVEe70XI0xfEl1pT86k8f_u4fCPAE6EtPfbPegySwfFW8QiE36JlDK4_bo0FCLisz6uoDiFSWQaumM2-mGo0-XzFOa6E5I8uMD-Jy12PQdic0louO_G4vNtQjqRlgb1CYhSH1iHVdgylg5RDxQ3i9LMTz_NZMgq7TjfjTrxikclV3FkuOyQwKFsR4W27KkZO77YUc15vRMcm5bWdp4_NWPavk9MTvsa8vElQn4uQtANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/unO6I3r7hGg1z_2nKDBUQOXV62f79fx3Isq49SPjuH7vCdR8whnIteq6zyQsaEP1vDduSabRDfXhXFWK-SF1sdfh3snVPMN4dB38RfP08GzEYfAseJNH-gSxYaVDHwcfediw0G4MZpyYycFp1xwBuO5Vb95qMSjRz_NdCS0hKOj75DAjCYOrqF-V--WUhe8mu2Dv6CiB4TePzQXSo154oQKOYTh3mRUxgjrJqLi1YkxPMkHtIlBwTa4XpVj6RqXUnJdRM4CiCjN3IxmerbZCf4yHtL3pHU4vCSa3aA5PobM903G6VWCdt192ngq77Zd2rUuMhhdgT2Q3dOrvOey-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uIu-pcWhHqQZneFt9GemFCs1yuLnprQetpLNzfRhiW6kz9zffm36YBOA4xxm9zVxhg8IlAQE2ssek-Goc5fId6nYguwHjvorK-BBXlOgylby4AjZvhiMOLnLQGEPJyBR1gMCLxXd017wFtehQf-zbcopCbBIr_iGjcWmq1zv0UUpDuKPqaBWNxEsU_GE9HCZrnDKLy9vkO8mY8jWH1fBOrn3ZveWdTapS0lXemLTxEOLfrFK-RYJgiQ84GUbdehKVJtSW-m_Xf-a2WdvNuuKlgLXluL3CZI-iyL3r-q5olx5HdUGZnj6xLKW68ASyyho5RQVS1Ld_IqqbqJH5Yc58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S-O4wQbZyy2JWHFxiZNQLTjtsgj33Op7IrtySEevHOr5_h74tyI0x9x3XqsK2eLDeAMkS4j-LfH-nBHNdcJUwmnP_7S4tEvbUEJmVr9A3-OU0uQzOmUPIF2JkqogIV-_Fs1QYGn2n2-HXj1w8dGx4-pn1Q8BdAm3JAXjrUP1PJ0av0bsxrUt3VB-gn37X5cDrUkPnUWx2VduvAN3xSmOdiok1_TBYbhzpCVrbVhC-GX7SZN2Ef9waJMfDQ-U8zvHFSVPBDEqJ6O0bB1bNczbOTAzXxwaUzReCqzRG_ow4pwEjn-R_2kfKqDdXcP5iDrb-PsyT-F4OKuTFCXX-9us3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/evet86t0bkgxY1KShKS6-10sfayuR_EvmRGBoUQwZXdcyR9fjC5dDg5Zutmz25c6jmI1yeTa4IV3njuz1a4iQdfD984NiGXl5ngiG4hBhH9E0SIpIfKtnbmm5BvkfTdc2q4TfvA0hzz66mGZlDwIijdpEt0bYM-Yvyf5Pq0gHN4THkHGrPsHPejkE4RMSfxjPFL4nps9rqkm-J3A0G9NXzGZ7B1rXUP3-q6QpYHseJ8hl_C525z4JcOpCBAEk4Lj6QeRFzAy9WWW4pKwDBO9RNnlFc2A40SJDVPq3PT-ld_k3aAR-uWjBpPMwwhNvB62BDLyImB1TZSwmbqNlLxVsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=NPvmESEQrj0-Iknl-sW97YUK11fFoyrvSdoMWhElv_fkR8O8NJPmqIqj8OVwd_sQnIW-Yg0s28PPRZVkieDrlJildtmeUH0VSSJFJHs1SDojoZcPr9lqenLapkTHOdi-hXHnRH--AGTlw7_MvayFSdcrr1MoIRlJbNb_OqbSWB8J79hNqpV4yRFcxqrveI6kFMk_yfWE_khwyeHlKVnAHlyKQqPKwnSyaqzA7oi7L1cDc3184rgXtoSfwNtpXuaWSSKG04HnOHIjIs5De5tg36Ay5qvazVZH6iW_62vd10uQ9P6vIgDJCjSUIEF50kt52hyKOYazF9xTsgu0EnQJSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=NPvmESEQrj0-Iknl-sW97YUK11fFoyrvSdoMWhElv_fkR8O8NJPmqIqj8OVwd_sQnIW-Yg0s28PPRZVkieDrlJildtmeUH0VSSJFJHs1SDojoZcPr9lqenLapkTHOdi-hXHnRH--AGTlw7_MvayFSdcrr1MoIRlJbNb_OqbSWB8J79hNqpV4yRFcxqrveI6kFMk_yfWE_khwyeHlKVnAHlyKQqPKwnSyaqzA7oi7L1cDc3184rgXtoSfwNtpXuaWSSKG04HnOHIjIs5De5tg36Ay5qvazVZH6iW_62vd10uQ9P6vIgDJCjSUIEF50kt52hyKOYazF9xTsgu0EnQJSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78268" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW_Lp7QtfU5sANFXsGQj_esuS9YFFpENkTV2Je9kwHnUYPCOwkqm6XnnsMIECHl6DjEgOuCRIND6qmvUbDyxweNdcSTrpSrtVBT5halMxhmuurUwP5Nclgzs9d0wOCB1JtK4dhkMD8sxWrEpyxv5Vx-Cc5QCI2Q9uyNWWlIl30X_tW5iHxpI8_sjBtkxhs1wLU6IyHZp-hNcyChi9x4Da5lPkNNQXl-rWbtFYd66UlRVsp37j0r1aI8kbQOEKF4MY_SDGbfRW8nOp1C6VRlNmZ0Xyet9QnJAPqg8vknRkJ4bGNvE44t4JWkVZzDl9AAxKeELBTy0mjz5wp0wZkTPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آسوشیتدپرس مقام‌های سعودی اعلام کردند موجی از حملات حوثی‌های مورد حمایت حکومت ایران به عربستان سعودی در ساعات اولیه روز سه‌شنبه، ۷۳ نفر را مجروح کرده است.
سرلشکر ترکی المالکی، سخنگوی ائتلاف به رهبری عربستان سعودی که در یمن می‌جنگد، گفت حوثی‌ها «تأسیسات غیرنظامی و اقتصادی» را در شهرهای ابها، جازان، نجران و خمیس مشیط در عربستان سعودی هدف قرار داده‌اند.
او گفت ائتلاف به رهبری عربستان سعودی «با نهایت قاطعیت، تمام اقدامات عملیاتی لازم را برای بازدارندگی شبه‌نظامیان تروریست حوثی» انجام خواهد داد.
به نوشته این خبرگزاری آمریکایی، این حملات در حالی صورت گرفته است که درگیری‌ها میان حوثی‌ها و نیروهای دولت یمن که مورد حمایت عربستان سعودی هستند، طی چند هفته گذشته تشدید شده است؛ درگیری‌هایی که آتش‌بس چهار ساله در جنگ داخلی یمن را از بین برده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78267" target="_blank">📅 08:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MHr5jr5_JQkfXSyH2rEXa7rQBbl78gJzIO9-GJfibxq_itj1kprjUf8S-HdaxXUYfhW4vzkLTstGetqmsgMoglCHdI2llebRkTqzpHq-OvwkKG8wfWnZSGh4lxpsAZpxuD0tbtw9ZDhixAcN3_zzN6l424-3RMdeRyKtVlB_4a1L4sldJZlmb6qTYecEf-tcLSdQiEW2Crz75fIPK6gZ_s73qSiWLESQMDD4pjlivfPAmmzTZwu2vvQe7JIRRdP1JB0cd_HCPenKkh65ieV6TYFiqvT_6K9aoK7zhfpzuNpnhCNdY2kZSRnMRWD1S6iwQYciReWH3MYah4vBr91EEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی ما در جنگ با ایران پیروز شویم، قیمت نفت به‌شدت سقوط خواهد کرد؛ درست مثل هر چیز دیگری که دارد سقوط می‌کند (اما بیشتر!).
بنزین گالنی سه دلار، اما در نهایت به زیر دو دلار در هر گالن خواهد رسید.
همه این‌ها به‌سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
MAGA!
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78266" target="_blank">📅 04:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/980dd40283.mp4?token=JTX7azGBGMaOfXFWL7p53dLSq1GT_N-2F8cXPYFUWl2-q7LJeJ1EmupBvPG0xy_kNnFBYdLE5oJ4UDGUnk08bNbPpG5DH5ahc1C_QOUMAsfDxeSQP8pzLkXkncq2nmMlgC5kWybh3r6NQhypkj9W-SiAKV8HHmb_RRLsAxRu0yjLrzn-BkwTBEcspFG_c6WV4VOrGNXbFwn1rcTtN9uQxtVP7rg4j5pUxLsTY0XTAvGP2F5faP-A2XUOcE5zmU9vIsffdiYo1e2V2azsjmi3FQppudb0kAyhA2AnvkvB_G-DEWicZ75aKDOgfEq-WXi-240otSBrSumX2qDrhCNDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/980dd40283.mp4?token=JTX7azGBGMaOfXFWL7p53dLSq1GT_N-2F8cXPYFUWl2-q7LJeJ1EmupBvPG0xy_kNnFBYdLE5oJ4UDGUnk08bNbPpG5DH5ahc1C_QOUMAsfDxeSQP8pzLkXkncq2nmMlgC5kWybh3r6NQhypkj9W-SiAKV8HHmb_RRLsAxRu0yjLrzn-BkwTBEcspFG_c6WV4VOrGNXbFwn1rcTtN9uQxtVP7rg4j5pUxLsTY0XTAvGP2F5faP-A2XUOcE5zmU9vIsffdiYo1e2V2azsjmi3FQppudb0kAyhA2AnvkvB_G-DEWicZ75aKDOgfEq-WXi-240otSBrSumX2qDrhCNDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78265" target="_blank">📅 04:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bGoRL7JYU_zXsqNK6i1skn2-Via3otJV--0wgaXQiQ0OaEYS0d7l3IDf_kNqKt8Hcsee3OQpTcnn6OET0RK8PxtoPwu_CtiOcs1nBKxOiKyeFFSTPQ-qAqqO8Y0oaRXIO6S_2cH59Z3iiQolX5se94GazRMV8c5mQhI9odoB2_rpPOeSOMEEKkzhy6jQ5oyObcg8_nrOcMtm01sJZivS57By5Yhx5ByzeupsDZSoqqbwQh9F_7KK_7Q-0_ZjmFIN_o_Ytq_k1aKukqMauQaQnkmfJqSQLZrIiFRCDUw00-Nf9ljgnzvJ9oeO82RfCfhBl0pSwdbOkP9y-YQ5wHsitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال کریمی، پدر امیرمحمد کریمی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴ در مرودشت، روز ۱۵ شهریور به زندگی خود پایان داد.
امیرمحمد کریمی، فرزند ۱۹ ساله او، ورزشکار و عضو سابق تیم ملی نوجوانان تکواندو ایران بود که ۱۹ دی‌ماه ۱۴۰۴ در جریان اعتراضات مرودشت با اصابت گلوله کشته شد.
پیکر او در روستای جونجان از توابع مرودشت به خاک سپرده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/78264" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwVgXE63NhEBpbBOKP9PWJuVA8_KZjI9651p0IRyw51qinE4QpHtHaYrAkXVc_ZC-55MyZ8q6tEr-cjLQrsg5g96hcPD5c1KwkgAtujcI27PkjVmods2JvVo72KI78n7Xi-Q7YQDB1iEhXXhO46q8Z8L41hHid135Fyt4fqlaqr93DvnO4AwGC-U4saEb5k2y3MpbHT4Sco8LQwwBQ0vRVLEyaVPpJlVwYvYltzTIs-jIX5dy_I665mZN1Kdk996jRhU1Ooyvf8nXx1HCNDEhxgabCuLCF2dk8fZjAepbP7Vp-vuk4W4fbm4r5Znh58l7IOErMm2Mf_5SZqPVR-blw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیدا حیدری، نامزد ابوالفضل سلیمانی الموتی، از جان‌باختگان اعتراضات دی‌ماه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ به زندگی خود پایان داد.
منابع حقوق بشری ایران، به نقل از خانواده آیدا حیدری نوشته‌اند که این جوان ۲۵ ساله، حدود هشت ماه پس‌از کشته‌شدن نامزدش جان خود را گرفته است.
خانواده آیدا حیدری گفته‌اند که آیدا و ابوالفضل قرار بود همین ماه مراسم ازدواج خود را برگزار کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/78263" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ekj1gduwnsCIW9SoLyHHQwXMnQvOyRn7lZLnDf9M0dPISniNgJFuj9NRBQnZeE1gLh4MY2sF4zHaccRvhKDIPuPCeNrOKk1Ul_jWIzpLFGdvoEpl6xuGLPvobejZdRR1kzCIJMBN-TBoC08XYlMfWU-xa1CkVLBu4e5kJsG5UnqOzNVGbs-GRVPFB3U7IT-pKhCZP1no3-ONcLk1ljrkY4YjMrD2vvOcPDXCsV5qQZ2Oz32OU4e61kxvj461RzxXp5PDwh46guGo4n1dJmiAIlaNLMcTbqwHbcLMzbpbQuXBcSHTTGtCkdY9PBop7Hr2LdfTRlUABYx8UXWHfasgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته‌شده با هوش مصنوعی از حمله جنگنده‌های آمریکایی به جزیره خارک در تروث‌سوشال منتشر کرد که روی آن عبارت «خداحافظ خارک» نوشته شده است.
realDonaldTrump
رییس‌جمهوری آمریکا چند تصویر دیگر نیز در این شبکه اجتماعی منتشر کرد؛ یک نمودار آماری که روی آن نوشته شده «ارزش پول ایران از بین رفته است»، دیگری نموداری که روی آن نوشته شده «ایران با یک ابرتورم مواجه است» و نمودار سوم که روی آن نوشته شده «صادرات نفت ایران سقوط کرده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/78261" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/78260" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MoNYHtTMhueFLQBDGaBiyaOYsxBH4sol1Tr0nwwgxQOiXAe_ZGhRndkudLIndMsKKdErkbKp0KRS1BhCK6mcSc8PyqQ0PVDtQvgbJjQ6rRR81ruclgutRI4etUdQx-jPNOCniiRFoaCLBS5LxNJi-80zC4EdZHB5cZ-Af8F-T2sy48L6Sp-EBZMqS8ygudOmi-7lxjfdiG8ehKVT3wy2Ea-2Ro1OhcTZS53-aRJx5RyizEhvDo4E-d4ITIldNarrler5W0UFTN4d0Eb_EMHHB0bAO7vxFZYUad6mouOlKpJQiP__Wr94CaUC3NqX85lw5uwxKQdTa6FBSgVPzmPObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/78259" target="_blank">📅 21:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=O18YF6rKGuJmxQXs_SgUXNTkH5X8Lcg8Id2EEtcG8V9TufRD0h9AmiUsGD6kzGN7cJHsxLj8Yhfzuwy6CE2N4WuYaySWUS9NfXidQBmGHjChAAlXZGcMq_hIvoA7qja7PNJn7dw_6Gx2G96wOn4As4H4sV1xTVK_Ry-JGqagI5XfmqsiiyxGh1zSL7LH9mrpPgNV3lPingC-yjBdf9DUxA0_uVizAMAMRd22KP3LfBBLky_jYzjKTsYmmAvn3HJpINf4RVmfK53tURLIOmsH3tx_ADrlk_0w_0tCeXZRHUDT6YJhufIXnS3fSA_plHJCBlFUmuPAalwccn5dzJz10w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=O18YF6rKGuJmxQXs_SgUXNTkH5X8Lcg8Id2EEtcG8V9TufRD0h9AmiUsGD6kzGN7cJHsxLj8Yhfzuwy6CE2N4WuYaySWUS9NfXidQBmGHjChAAlXZGcMq_hIvoA7qja7PNJn7dw_6Gx2G96wOn4As4H4sV1xTVK_Ry-JGqagI5XfmqsiiyxGh1zSL7LH9mrpPgNV3lPingC-yjBdf9DUxA0_uVizAMAMRd22KP3LfBBLky_jYzjKTsYmmAvn3HJpINf4RVmfK53tURLIOmsH3tx_ADrlk_0w_0tCeXZRHUDT6YJhufIXnS3fSA_plHJCBlFUmuPAalwccn5dzJz10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ سوم بنزین به ۱۰ هزارتومان افزایش یافت
فاطمه مهاجرانی، سخنگوی دولت گفت نرخ سوم بنزین از بامداد ۱۷ شهریور به لیتری ۱۰ هزار تومان افزایش می‌یابد.
سهمیه ماهانه ۶۰ لیتر بنزین با نرخ لیتری ۱۵۰۰ تومان و ۵۰ لیتر با نرخ لیتری ۳۰۰۰ تومان بدون تغییر باقی می‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78258" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78257">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHr1vtz30e2pzlWOIc7BL9Ht3ENcxPyFMvxLYkhGVg0Zyc_Jh-XinJ6CkI92DPm_36Y6jL8sbRwP-4F1Jl9NbTI9mB9L3zJE042fKFwoblBObVIZ9sv8igBv-CjpCyCVHefb38vOwPoxlYxlKfldv7MwSGpvqhKU6mPUppBlfI_upW1ZTJUdc_wLb0w71ZJ6sbUgwITfnMXhlRPlydh8T1m7PUw1L7Pp5zsssflu9xTO4fdDHsKl79bFo8ihpmoMehlzluu8EQxU79A7nYDdTRxIHrX1DvYAfyCV9hS6p_4RIZTEbuLvQKOFnpT5DBLuyK6DD5RyETwj4DfHwUJItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که سپاه پاسداران، بامداد یکشنبه ۱۵ شهریور ماه در بیانیه‌ای
اعلام کرده بود
یک شناور بدون سرنشین سنتکام را در تنگه هرمز هدف قرار داده است، ارتش آمریکا این ادعا را رد کرد و آن را «دروغ محض» خواند.
رسانه‌های دولتی ایران گزارش داده بودند که این شناور بدون سرنشین آمریکایی قصد ورود به منطقه‌ای از تنگه هرمز را داشته که ایران آن را ممنوعه اعلام کرده است.
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی آمریکا (سنتکام)، در گفتگو با آسوشیتدپرس گفت ادعای سپاه پاسداران «دروغ محض» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78257" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=J37gAjnCFc6814LvvzOYGDW7zIGfbUqMlR7ztOm88yOaqI79mhr20HokXNdoOXG4f-sKYbzjgOAC4qgJSEe5xrVYcWfOPK2z-CjMrGrE9o4zZSm1pUsI7NFU0_NEM1Iu0RY9nCXDs6-DYgJJkH01QdYDXXn-yLOsBSUeicOqei0rGJ4tF82Q16QiKIDshglazMtxwiot9N9t4SoXNu7YvGClWG6QXZHQ0L-X3piea2Qr8fpuOaJ9VX4FuSoUXa17XMhsUShuGY0txOpy7h9AYK8hCtVXE-SGvWgVR796tELtjx3MGLxfqWessLPIF58Z4GHc1Dwx5g3thoZcQQABwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=J37gAjnCFc6814LvvzOYGDW7zIGfbUqMlR7ztOm88yOaqI79mhr20HokXNdoOXG4f-sKYbzjgOAC4qgJSEe5xrVYcWfOPK2z-CjMrGrE9o4zZSm1pUsI7NFU0_NEM1Iu0RY9nCXDs6-DYgJJkH01QdYDXXn-yLOsBSUeicOqei0rGJ4tF82Q16QiKIDshglazMtxwiot9N9t4SoXNu7YvGClWG6QXZHQ0L-X3piea2Qr8fpuOaJ9VX4FuSoUXa17XMhsUShuGY0txOpy7h9AYK8hCtVXE-SGvWgVR796tELtjx3MGLxfqWessLPIF58Z4GHc1Dwx5g3thoZcQQABwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78256" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NnzfT5KJyAgJyUnEiqkwWtezFAmTwW01TNJ_I4YQgUb7rW-KzbZYQdk-xXzsv84S2D6LKXcbge3Xx4-VsjmtuRo9PstY40YWzK4hEuWejbmetfN2ixHq01gqO4boI-xtBMCbbmAky9hfLC1xmcZoXz7H2WGJDEh2Xwo-F4HMWOF9hJCvNJ9uWk0TkirLExKH7kR1IDxbGXWCWjDXKke9z9ZL71e4gYGCpG7A42h2Eg9rR41Q55nM3520jhNMiTKsx1TzQTmpT4_2US5ZGhSoYMOLkNb3hb8T_bYCvcTqzlirdb_SneDpsh_ZJpEevQkFpX_wqSft7ttdVxu5xLDnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران پس از عبور از مرز ۲۳۰ هزار تومان، به کانال ۲۲۶ هزار تومان بازگشت.
بر پایه گزارش اقتصاد۲۴، نرخ دلار صبح امروز یکشنبه ۲۲۶ هزار و ۱۰۵ تومان بود. وب‌سایت‌های اطلاع‌رسانی طلا و ارز پیش‌تر برای ساعتی از جهش قیمت دلار به بالای ۲۳۰ هزار تومان خبر داده بودند.
بهای دلار در ادامه با شیب نسبتاً تند عقب نشست. اقتصادنیوز این افت را به ورود بانک مرکزی به بازار نسبت داد و نوشت این بانک به دنبال جذب نقدینگی در بازار است.
حواله دلار در مرکز مبادله ارز و طلای ایران نیز ۱۶۰ هزار و ۹۸۳ تومان اعلام شد که شکافی بیش از ۶۵ هزار تومان با بازار آزاد ایجاد می‌کند.
حتی با احتساب اصلاح امروز، رقم کنونی نزدیک به ۱۰ درصد بالاتر از آغاز هفته گذشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78255" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fpGFaLi4ySEpWdqD9xIiyO1ZHzpijdpQq3mXgkmVgu20fTueBQj17RpmN9Chil3QtkF-nyldhwwyIfLUvOMvSymtIwk8zzjcchkScFppEc8sR2xAsimKAI3FR6DQFt9Iew4n7p6oZ3NFwbQUd9LxObHuP3xyhRATo6OniMmyrzl7RAVDx9I8gbjGTrV17oCgHZLcvHu4fzkiJISdCDJ2dPTuuityaSlNhTQGZ_qWP7EaTVcGhlIIW3yTjLWIJYpPJ-O23ECpPhztoo22qGprOhL1gNhpWCsJAdRyiK8MliIRwVRrcKQJyYZd7K1eJE3BbfZXA0nraHzah0u-mPazug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bo8kXPO3rJT9XGDjMrAPQKN2sc7gvmtir4f1WZY8bsxN5Hlo-Coqf-3n6-IhXoMwpFJvlq7DYLzXV7byypRNDoZ7B9AUCGxQneBgGD6Ou8S_F6bKErxACemd_mpprbTRbiXHAW5XJGsEfuFIDw-UrwNL6t0nW0UMQiNYglV5MDxN5BzdmEXf4sYFTfzHndQiiwQKSA6Q4v9YZMnp4U1d_XY8N15DAeUmSbIs8ZPGbjOy83NGdqtAF8ZBJbt8AZBB9PwAQLb0jdJQtaMfQ_c3czlI2pgXt474wdCQHUTK5bG7FefXiAAfbBax6zpVUfSxBPTl4oxcr4b99xazhEr9Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TvoX7ktvicwjASs7cZPtKPQX3_WIfgFWuwRPknB87KfsJVckHitLCtYUx4cckSX4wE6hK6ooKiHQEBBFEHo6fEAXQjyWKhdqmwrKQIri2mVYvdL-O9iBEmkwCicRoiQlChNDrevsndJlRtQbS_zO-qj-M6Sq5EJ1PbatUyXFLReV04OH2Ton2_xT7obypMRTtm2gQYTjzOo14NF4iWF_Nacl25ovKL3BKKP7qJ5V2vBuYI18MtzY-mZ_utoIYnDsaGI9jZjolpSiv-Kl8ZBiKqVyB0giWum3l-W_86E1neXszZDaS7x3_aGx1vhqm0uPg8SQclGPk0-NrA18LAzvYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/inpjAzx-qsz5em8g_LU1ugdLSE7lHHFyULdfBBqxYuBs0cbPuDs_XxyUXMJDvjv_EkIZB_aLHi3hmkwbN4JELzBH3IgLwBNP9mokA0wOJbCU537jdc5hXSIriWbb_fxuJMbS0HB631orosbMdeJ-QZTqp3c3UiHlBRoaqkO3kV6pZrSeXaqpnGk8QJtkzsHttYLEakEczw86J-Cf9zUcdBChBPKkTcHwEsQGiZbgY6ktAqmadikwvraIa-8AyCrSQrnYmq7P8aRa6JJUlkTalXubsyHa1RK_rplFNMu8SQz9rqfDu_JFJZrldQZ7SkR6Vdj8gcGf4dtshRxfuO2qGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i-gZVO-LXo4uw_j6HYkL-NbR-AonJlbqmZ839arxuuc7DX4sr9skvwIaKVP9jioOmnWphiTgIFkJaUmQtJ-jiQzFACKQNfvdW_r54ieRX9eQCwDsottUkvDKQrkpjoLyCuNsxSwruvPzy-loFMfeq5Bqh5mvzuK90mqRtviZkda4pMnBp1gmqSM1g4cDYSS-G-goD-eTyupE3eXJuaJl9vxLC5QdJFynDvWJUqbzymXYdCJuEbvMruEO7neS45EIsfer-gNegVfdBNnGJ23YvpyBSXkeAZMxZ1M2qmrHI_KLfmXjLgTM9TZqIQW5Xsd0riTDqfHoSK1N1DPh21Cxpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78250" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78249">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HL9GnlO73tRsc42q0DnzkDvD70gMU8ID4YiCyPlwrwj9cQwNUwPuaIDUUnFJ-X_4vDCExZZmhPjSVNBb2mg15kU3_Ea1o6OkcMl8j6yxyUVeDbXFmcqh9WGxwJ_OBxfzx0UDdk8TMCKBDdZrHg6Tm3mCkMLWo2o0lkgo9MmwZ1depM5O2PIo1rZSnFzlO4ffWuK6XBvBMxZHAJQBrPlmDh1yuMiStXy3hNjLIv64MmMlKMa_3Y9uWaKA2UBTEy0LK1pvJsnn5IFka6-GYC192qMpdaIQIcm8uXHDtto3RKzMdUEUiWxqhmDKOaLlmc-FfYEolhuqCMxVnIi4ex57FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران می‌گوید یک فروند شناور مدیریت‌پذیر از راه دور ارتش آمریکا را هدف قرار داده است.
روابط عمومی سپاه پاسداران در بیانیه‌ای اعلام کرد که این شناور قصد ورود به «منطقه حفاظت شده» تنگه هرمز را داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/78249" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=d8S6j59yTKkmSLClDHY6NH11lSik8pZnmY8wed25Slg_FchYFsAn0RTdt2dt0ypXbDY6PJCxJ0hF9rKrUsRRisvpD3ubJP-d9-khv_z2q8c-Xe5CJbZ91tjxnBs1h1LAYTMiCrlCx-Y-fux1HHKpaeB8M4gIeNca2vZ_Cdu4MIB4Y0hPgdv-1uvmLo8b6P60emlJrtYRwUPbW4PD2L7J3hSPywYP7r04jyIXpBsEor9dp-CMvdtmSfaZeLv-XRHY7S_Ak3mPEvYwXEVGEVSDyGsIGe42EvazLUNXxhwMwTOr9qj9pAF0EVcwGy5PxMgRSJutjjUmSFNO-0gkFAVyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=d8S6j59yTKkmSLClDHY6NH11lSik8pZnmY8wed25Slg_FchYFsAn0RTdt2dt0ypXbDY6PJCxJ0hF9rKrUsRRisvpD3ubJP-d9-khv_z2q8c-Xe5CJbZ91tjxnBs1h1LAYTMiCrlCx-Y-fux1HHKpaeB8M4gIeNca2vZ_Cdu4MIB4Y0hPgdv-1uvmLo8b6P60emlJrtYRwUPbW4PD2L7J3hSPywYP7r04jyIXpBsEor9dp-CMvdtmSfaZeLv-XRHY7S_Ak3mPEvYwXEVGEVSDyGsIGe42EvazLUNXxhwMwTOr9qj9pAF0EVcwGy5PxMgRSJutjjUmSFNO-0gkFAVyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام ویدیویی از غرق شدن نفتکش M/T Kylo در دریای عمان منتشر کرد و نوشت در قعر دریا به نیروی دریایی ایران پیوست:
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/78248" target="_blank">📅 04:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uKVmuf4ZUw7vdVUmMTnu7GEizO1jMqiQT9NtvB5A5jPTumSWS796fNh2DyReCUQPMKiRCFyRNZX11G-axZCWQ8TRgL0FcAeorPWH56-ucp3AXNbLfMwhtk7_fuXiTEDx56hZl0ZfgSMkl8Xi33L5Ib-jRzT3Sp-d58azyDgXUpUmpTLzyYFHnZQOApUq0Wdaff4g3N5-sgEJJm2Z4LEBiGSghXPDzrA31xH8khSjIaA-CM1TacTpRP2sr_qItaIs0JusRj5a-D_VqtArroy-kgr8uNejxmAlvRzmTwDMc6mtLXnzAcWbTBqwqNBKvL7rYRvY8oSIPgwLjwXCsa9kGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، بامداد یکشنبه، با انتشار بیانیه‌ای اعلام کرد که نیروی هوافضای این نهاد با استفاده از چند موشک بالستیک، یک ناو هواپیمابر و یک ناوشکن ارتش ایالات متحده را هدف قرار داده است. در این بیانیه آمده است که این شناورها در محاصره دریایی و مسدود کردن مسیر کشتی‌های ایرانی مشارکت داشته‌اند و پس از این حمله «دچار خسارت شده» و «منطقه درگیری را ترک کرده‌اند». سپاه پاسداران همچنین با اشاره به تایید وقوع درگیری‌ها از سوی سنتکام، این عملیات را پاسخی به اقدامات نظامی واشنگتن دانسته و هشدار داده است که در صورت تداوم فشارهای نظامی و محاصره دریایی، پاسخ‌های نظامی گسترده‌تری متوجه نیروهای آمریکایی خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/78247" target="_blank">📅 02:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7VCsqGBfhIANpwovG1dpvd0Dz4ni9hRE7w2pMl7PxiGnfYm7J3ICxay6UMq6aj-g2m9iKlBp1br370uT6nkDER7c83I11_76C_g0e7O6ME36UQ5A1ZIKa0v25ho3ZKb7FoXjd2R3Ea-Ut2kA29qZXD4oWwA0KtELMqAvj98qycj-R3lmAgRkeXznOZ2KbA6FGI-AKn3vPGrxLS7WNXu3GfVtRbc1k6wcdAmB3RhqQywSOvO2MUtc11fU3Ngd4OFivgVQrtMPJAuQ3FbEVYFJVVdZMuNICPKIMUwXhzXRT4nX_Zo55Org1rpsXGhGp76CbxUGLwHtTiF8gV_tmqq3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/78246" target="_blank">📅 23:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=u_dQVTbROj4GwNvVEERN0gvBFSyS7_e6X09SvxKULxP7Xg4vE5Q3WHAYAdRtwZHjXH5e0jI_Vs136eC8Wfe2lSUJdOUkgSKqN9vBcQ_lTz1G6FPg5kVB9Sgi0rhYesZNSl5VFliPwQNIYNALzP6MMhB03SaIjQo3iFKa0VY_5cIcXfsDwfFioWqJWx2ub3B-vG5y4SnffGDIXm249wqksG9JrIhcEaUSvD7BMcQrtjyLupH4LIvDgb4QXxOFAbRauiQgGA4wuXi4uGfduk01grbLusi0ZVLROO9HMyDB4YsTv7gQX-nX20usnWV2-1D74aFHMsbCOPXl3Ol-Ij6VGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=u_dQVTbROj4GwNvVEERN0gvBFSyS7_e6X09SvxKULxP7Xg4vE5Q3WHAYAdRtwZHjXH5e0jI_Vs136eC8Wfe2lSUJdOUkgSKqN9vBcQ_lTz1G6FPg5kVB9Sgi0rhYesZNSl5VFliPwQNIYNALzP6MMhB03SaIjQo3iFKa0VY_5cIcXfsDwfFioWqJWx2ub3B-vG5y4SnffGDIXm249wqksG9JrIhcEaUSvD7BMcQrtjyLupH4LIvDgb4QXxOFAbRauiQgGA4wuXi4uGfduk01grbLusi0ZVLROO9HMyDB4YsTv7gQX-nX20usnWV2-1D74aFHMsbCOPXl3Ol-Ij6VGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مرکز فوریت‌های پزشکی استان کردستان اعلام کرد که در پی آتش گرفتن یک تانکر حامل مواد سوختی در محور سنندج–همدان، دست‌کم ۱۱ نفر جان باختند و پنج نفر دیگر زخمی شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/78245" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ROqjqQaW-3WOR5Z3VAyFxjd2TtrV626z_4yanCUzRJkWlSAvuMpgaBFA1c8U7g02nq3JwdExNgWpQui3EB2ax-guXBECc0ofFt-aaxnmfT6rasPaPkVlsZzN5zBCv-TVOO2R5fnJRvirtc5KZ3Wx5dwakNy8VssVVe5ntORV54isxd3ORnrEKgZsoEk3kRhuLkxoxWnmWxnuIfPSalYR0rxrgFSAuQ-8sj3i3kQUROffb1KsCB_fb8f8dA9JqqHaePx5654p1yzdqgnwfiqj7Qa2ifqgaBc-cDLT1f7veFDtLCOksFPDwnO981bxFqWni2NMQtv4OZOgNNqjQ6yTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی درباره چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها در چارچوب فعالیت‌های نظامی جاری در منطقه، هدف آتش با هدف از کار انداختن آن‌ها قرار گرفته‌اند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78244" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرانه‌ها(مهدی محمودیان)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9owg3YR0G-N9QSyY7Y8FubtUB2cJoYxAIBfdDw09n52v8k2SNkj1Tl-VTO5LLq0FWrq_ak16Mj4qKMBAcoDxcv3FTiF4IW048Sp4MIpR_3B_NomtwsmitofvaWeNOlqPYYNlGLl71oPrgrSjRdVuIXVDxw_gYhuvKZHDMc8-yWJbGagT96r1saXIGIMcPK2qoaANAgiKIJryN3Jz6cLcW0kVjcw54wiV1q-P-IzpM5iox9eYUDYLvfXvrxeU9Nx8mQvCrKD8NEWLxnU0nMePbgZo-bcwB7Z1X1ddGx-OQcS1za9s4hR-QLlJcq6zAvfROWTyE8ggN3rjqhNTURo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9m-br2Vklyq_JqRO89oZDtry_VW5jZ5W0SPLGxWURD_Z-KXzjoRa_KkHLEa9J9VfrVvBJHpsBRLwf9q51HL7IUFmegEUaA0DmWCO7buG9qTS1r3Jd90asOLJU0UAzyYd5HUUUSLBQXYUGWt41Mp4KIrYC8IEVza1w_E4LncnxgJZvdGmR_Ix8VqUt9IbtqLego1Y_NeSVqtN1LryxH048bHgNnwBE2rD2aYpph9W0AhBuaY6pk040WXY3ZHK98_jo_ZLy9spT9XQvjPZ9YrCW9ocwsii3ZGwlZfIaWzF00NHAX2WrrB_J0jqd18zsZdUryN3QNOmzep_1tOkEXTqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78242" target="_blank">📅 18:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=bEOI4fyVfjT0SO3h01Wah9eoFz_CG4kWJ7wkm5tLZGblcMNSkc3VeYiYqj0MSlBXkQ_xnngeXSGDoDOMk_IyON-RYg_uc-tnXxTWNGBFFtL07WciQ7eClaPxvp2FCIL9vJ2MHjgyyP6Fiq_FhYbK_o2KRP_oQFL40sn4DD09vWuI8vbQGBs-aedJWsHhvQenhxNkKiHqqKstvDCQ069LSUQ9aOuY5Au8DZz5el4fqce-pcXuEcu3A-I0owx0-HL7Ta36kD_A6Origb5FeUOuETvU7qc9GhJd-h4CHi4PTF6bPsQ-6OlXXq04yTsyNA_0QFirMSL0HLeqe_DBo7c_bg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=bEOI4fyVfjT0SO3h01Wah9eoFz_CG4kWJ7wkm5tLZGblcMNSkc3VeYiYqj0MSlBXkQ_xnngeXSGDoDOMk_IyON-RYg_uc-tnXxTWNGBFFtL07WciQ7eClaPxvp2FCIL9vJ2MHjgyyP6Fiq_FhYbK_o2KRP_oQFL40sn4DD09vWuI8vbQGBs-aedJWsHhvQenhxNkKiHqqKstvDCQ069LSUQ9aOuY5Au8DZz5el4fqce-pcXuEcu3A-I0owx0-HL7Ta36kD_A6Origb5FeUOuETvU7qc9GhJd-h4CHi4PTF6bPsQ-6OlXXq04yTsyNA_0QFirMSL0HLeqe_DBo7c_bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78241" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtbKD4GN-3wmJ14SG0uJmE_USvihd1etC7JRtxrdZ4FCRg5aGGSiFwjV2DzbUE_aCafHt6tV0JLaby2xIBLgdxg41ZCzpNAj1YxUSQ3DP6fz3V_rshLPsiLeus5ScCEDsheOTx3V_CtXiYLQ7MmzlbtBKUUbbCK7gm9FQapRNXhh0Ltv0veLsV4zY8SQqKN_rQG7Vpb3t2vgTYaE7RwY9KCzMyL35p8TUuYmfQIdhm1OFCDIwYMMW3NKHglLSsL0jrrNhUr9j8hMLMu_DTQ9BAWrazyxSdO-WxVYX3GZqT9EnuOt7RHEOaTDNbMWPwiWetYSMDlbL9Cf7RBF9j0vhg.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/asnR6oT9BOaWM5uaIZGXIrA8DLYWUxMPir5YI4KxoMGaTQmYBQuZXTNQdw3XvDYNfIIaFQQQPWqMcThJ919iUXxVK_oSIjL9uyXalNZOgG7HwXnjzt-Hlxt_fsxbr1xwirn62Owt7t5w8_L_NKw34a5-nXOlX7qlugbhd1X4NVxTH7KgfDSSNXGEYYBbv1IzCNTAlhf1NrYKk6Jpf641vuCc6B3wt6RzwpAPkxrPIURjBta3UDcL6CmbBtifpGTMS5aUQedGjoSEyqPeCQvWbjszitUSB9F6Wj_hjKle9KllugcSOTFIFpdgGIcARHA8rdDyA-YYHycymLZKHHzy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده روز جمعه ۱۳ شهریور از موافقت با فروش پنج میلیارد دلار بمب، کیت‌های هدایت و دیگر تجهیزات نظامی به عربستان سعودی خبر داد.
این وزارتخانه اعلام کرد این فروش، توان دفاع هوایی عربستان را برای مقابله با تهدیدهای کنونی و آینده منطقه‌ای تقویت و هماهنگی تجهیزات این کشور با سامانه‌های نیروهای آمریکایی و دیگر شرکای واشینگتن در خلیج فارس را بیشتر می‌کند.
عربستان سعودی از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران بارها هدف حملات موشکی و پهپادی نیروهای ایرانی و حوثی‌های مورد حمایت تهران در یمن قرار گرفته است.
وزارت خارجه آمریکا کنگره را از این معامله مطلع کرده است؛ این فروش برای نهایی شدن همچنان به تأیید قانون‌گذاران آمریکایی نیاز دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78239" target="_blank">📅 17:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19446f537f.mp4?token=hKZnUVLyrLUZhTAG9_FB7Z9fZWBTHhKoW5dJ5gxOSZ5IjnxFNSK0yGSz2dO6vz54vB9dDbDzx3goEpj6PH8mlnAtQIBNvv_wduDCgajKA1SzMo8GfuW9b1FFP0FFPVbaEBe71EI90Rbl3r_GG0y7EFc7Vg9TWEt0am-wnn03wKJKuw68J_nwGttsRehKknEN7d8GczexS-T8GzK_daJLLc3vTfuBUJxvZ97n75VPuFoW05lbYj5JdhjiKLyGHRmVz3ZI1B5YaC_m1quUh7TmWaVXvB3P0AEVr-8Esq2jJX2fCv6U65GBQZRrhqDqdO-5u8LXh5OvDiVIhfrvu-hUIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19446f537f.mp4?token=hKZnUVLyrLUZhTAG9_FB7Z9fZWBTHhKoW5dJ5gxOSZ5IjnxFNSK0yGSz2dO6vz54vB9dDbDzx3goEpj6PH8mlnAtQIBNvv_wduDCgajKA1SzMo8GfuW9b1FFP0FFPVbaEBe71EI90Rbl3r_GG0y7EFc7Vg9TWEt0am-wnn03wKJKuw68J_nwGttsRehKknEN7d8GczexS-T8GzK_daJLLc3vTfuBUJxvZ97n75VPuFoW05lbYj5JdhjiKLyGHRmVz3ZI1B5YaC_m1quUh7TmWaVXvB3P0AEVr-8Esq2jJX2fCv6U65GBQZRrhqDqdO-5u8LXh5OvDiVIhfrvu-hUIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های ایران از شنیده شدن صدای چند انفجار در نزدیکی جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و هدف قرار گرفتن یک نفتکش کوچک ایرانی خبر داده‌اند.
خبرگزاری تسنیم گزارش داد این نفتکش صبح شنبه ۱۴ شهریور در شش مایلی جزیره خارک و در محدوده لنگرگاه، «هدف قرار گرفته است.»
تسنیم می‌گوید این هدف‌گیری «با چهار پرتابه نیروهای آمریکایی» انجام شده است.
به گفته منابع محلی، این حادثه تلفات جانی نداشته و کارکنان در حال تخلیه نفتکش هستند. وب‌سایت عصر ایران نیز اصابت چهار پرتابه به این شناور را گزارش کرده است.
خبرگزاری فارس پیشتر اعلام کرده بود که صدای انفجارها از محدوده خلیج فارس شنیده شده، اما نشانه‌ای از دود مشاهده نشده و منشأ صداها مشخص نیست.
نورنیوز نیز به نقل از منابع محلی، گزارش «حمله موشکی آمریکا به یک نفتکش ایرانی» را منتشر کرد، اما آن را تأییدنشده خواند.
خبرگزاری دانشجو هم ویدیویی را منتشر کرده که می‌گوید مربوط به این نفتکش هدف قرار گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78238" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=PnA2kPk9zlKVhpHuXsqIJtI_9iSyBoOYkHP6f0GVMfmLMkkc_Yb1K0QmMHyVzrdS5VaV2iDFBoYHlmO-nboCgJjm10-DkwLTo0Gk_K8rc7Hf5Mw1xhcNmL7y_VL8uyvK7TO0zifFnQD6ELoLxKaWxEHm3widWU9PxlOWmDDBPNzioBffIc8zE6xC6qLw7VxTed9i-4eZu0QFCEaunqJqIGD43dgul9_NkAAwub344qqCwOtYCKv-4m9NHx6ulxeTf4c5G35w-5KxDcHwksD868psb5pJSX1HLFnf-0kglYtaavM8IFSQxEdpU40NMam2zQU6XnQzuM7bIZ8XLTuzMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=PnA2kPk9zlKVhpHuXsqIJtI_9iSyBoOYkHP6f0GVMfmLMkkc_Yb1K0QmMHyVzrdS5VaV2iDFBoYHlmO-nboCgJjm10-DkwLTo0Gk_K8rc7Hf5Mw1xhcNmL7y_VL8uyvK7TO0zifFnQD6ELoLxKaWxEHm3widWU9PxlOWmDDBPNzioBffIc8zE6xC6qLw7VxTed9i-4eZu0QFCEaunqJqIGD43dgul9_NkAAwub344qqCwOtYCKv-4m9NHx6ulxeTf4c5G35w-5KxDcHwksD868psb5pJSX1HLFnf-0kglYtaavM8IFSQxEdpU40NMam2zQU6XnQzuM7bIZ8XLTuzMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتین خواجوی‌نیا، دانش‌آموز ۱۶ ساله رشته کامپیوتر، شامگاه ۱۸دی۱۴۰۴ در جریان اعتراضات مقابل فرمانداری شهر قدس، قلعه حسن‌خان، با شلیک گلوله جنگی کشته شد.
مادر آرتین ویدیویی از جمع‌آوری کفش‌های فرزندش منتشر کرده است؛ کفش‌هایی از دوره‌های مختلف زندگی او که حالا به یادگار مانده‌اند.
مادر این نوجوان کشته شده، نوشته است: «از اولین تا آخرین قدم‌های تو را مرور می‌کنم پسر قهرمانم. از لحظه‌به‌لحظه بزرگ شدنت حالا فقط خاطراتی برای من مانده که هر ثانیه از مقابل چشمانم می‌گذرد.»
«از آن نوزاد زیبا با آن لباس زرد در آغوشم تا آن مرد بلند قامتی که باید برای دیدنش سرم را بالا می‌بردم، تو همیشه یادگار مادر شدن من خواهی ماند.»
او فرزندش را «قهرمان جاودانه من» خطاب کرده و نوشته است: «هر لحظه و هر جا یادت جاوید و راهت پرنور.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78237" target="_blank">📅 17:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/78236" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hYhWPUAblHtK32b28wg2sLeSqNPsgAdUhg-amawqz0YNWIsqtTOrForo99CjcvVgEbRBWY0ZftedSjE7uryVDHN-q-QxReq1v_ciPxdQmYxIQO4ngBZhdDNt7cWd84ncmq2Zij14iSlURVimJfZmqpDHQo1qX0Tfmv8qkFE5hv0V-_j3aWr_M3oSxP4NtlS2YOVcDoac0xjVxuay4VP24vE7F3gbjeLBTKF31UYTpdeXbofAe7sJvibbOam9Y6bHreYRG5mP8Y0tz_ZtOrfoJGH_PdeL3PDIma55af0ChBH_AGnIztXueLqeEOSqJ8piLwl31EBlUNxassA9KKcB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده آمریکا همراه با بریتانیا، فرانسه، و آلمان در تلاش است شورای حکام آژانس بین‌المللی انرژی اتمی هفته آینده قطعنامه‌ای تصویب کند که پرونده هسته‌ای جمهوری اسلامی را برای نخستین بار در ۲۰ سال گذشته به شورای امنیت سازمان ملل متحد گزارش دهد.
خبرگزاری رویترز روز جمعه ۱۳ شهریور به نقل از دیپلمات‌ها و با استناد به متن پیشنهادی قطعنامه گزارش داد که چهار کشور در حال رایزنی با دیگر اعضای شورای حکام ۳۵ عضوی آژانس برای تصویب این قطعنامه هستند.
مذاکرات درباره متن نهایی همچنان ادامه دارد و پیش‌نویس هنوز به طور رسمی به شورای حکام ارائه نشده است.
بر اساس پیش‌نویسی که رویترز مشاهده کرده است، شورای حکام از مدیرکل آژانس خواهد خواست قطعنامه جدید و قطعنامه‌های پیشین مرتبط با برنامه هسته‌ای جمهوری اسلامی را برای اعضای آژانس، شورای امنیت و مجمع عمومی سازمان ملل ارسال کند.
در متن پیشنهادی همچنین بار دیگر از جمهوری اسلامی خواسته شده است موارد نقض توافق پادمانی خود را «فوراً» برطرف کند و اقداماتی را که آژانس و شورای حکام ضروری می‌دانند انجام دهد تا مدیرکل آژانس بتواند درباره صحت و کامل بودن اظهارنامه‌های هسته‌ای حکومت ایران اطمینان لازم را ارائه کند.
اقدام آمریکا، بریتانیا، فرانسه و آلمان ادامه قطعنامه‌ای است که شورای حکام روز ۲۲ خرداد ۱۴۰۴ تصویب کرد. در آن قطعنامه جمهوری اسلامی به دلیل همکاری نکردن کامل با تحقیقات آژانس درباره آثار اورانیوم در مکان‌های اعلام‌نشده، ناقض تعهدات خود در زمینه منع گسترش تسلیحات هسته‌ای شناخته شد.
یک روز پس از تصویب آن قطعنامه، در ۲۳ خرداد ۱۴۰۴، اسرائیل حملات به تأسیسات هسته‌ای ایران را آغاز کرد و ایالات متحده آمریکا نیز پس از آن به عملیات پیوست. بر اساس گزارش رویترز، تأسیسات غنی‌سازی اورانیوم ایران در این حملات تخریب شدند یا به‌شدت آسیب دیدند.
جمهوری اسلامی از زمان این حملات به بازرسان آژانس اجازه نداده است به تأسیسات بمباران‌شده بازگردند یا وضعیت باقی‌مانده ذخایر اورانیوم غنی‌شده را راستی‌آزمایی کنند. شورای حکام طی یک سال گذشته دو قطعنامه دیگر نیز تصویب کرده و از حکومت ایران خواسته است موجودی اورانیوم غنی‌شده خود را اعلام و دسترسی کامل بازرسان آژانس برای راستی‌آزمایی آن را فراهم کند.
آژانس بین‌المللی انرژی اتمی برآورد کرده است جمهوری اسلامی پیش از حملات به تأسیسات هسته‌ای، ۴۴۰.۹ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار داشت. بر اساس معیارهای آژانس، در صورت غنی‌سازی بیشتر، این مقدار می‌تواند برای تولید مواد شکافت‌پذیر مورد نیاز حدود ۱۰ سلاح هسته‌ای کافی باشد. آژانس میزان غنی‌سازی ۶۰ درصدی جمهوری اسلامی را «مایه نگرانی جدی» دانسته است.
جمهوری اسلامی می‌گوید قصد تولید سلاح هسته‌ای ندارد و فعالیت‌های هسته‌ای خود را صلح‌آمیز می‌داند. ایران به عنوان عضو پیمان منع گسترش سلاح‌های هسته‌ای حق استفاده صلح‌آمیز از فناوری هسته‌ای، از جمله غنی‌سازی اورانیوم، را دارد؛ اما آژانس می‌گوید جمهوری اسلامی تنها حکومتی است که بدون داشتن سلاح هسته‌ای، اورانیوم را تا سطح ۶۰ درصد غنی کرده است.
رویترز گزارش داده است در سال‌های اخیر هر بار آمریکا، بریتانیا، فرانسه و آلمان پیش‌نویس قطعنامه‌ای درباره برنامه هسته‌ای جمهوری اسلامی به شورای حکام ارائه کرده‌اند، آن قطعنامه تصویب شده است. با این حال، اقدام عملی شورای امنیت علیه جمهوری اسلامی ممکن است با مانع روبه‌رو شود؛ روسیه و چین که از متحدان حکومت ایران به شمار می‌روند، از اعضای دائم شورای امنیت و دارای حق وتو هستند.
@
VahidHeadline
نمایندگی جمهوری اسلامی در سازمان ملل در وین اعلام کرد این اقدام آمریکا، بریتانیا، فرانسه و آلمان نشانه «شکست کامل توهم مکانیسم ماشه» است.این نمایندگی افزود این اقدام نیز «هیچ سودی» برای این کشورها نخواهد داشت.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/78235" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ah7_nkXGhl9kYoPUOK3pdhGhgiq0l_BrMk9SBzDE257wNNUPT2dEeB91rJzKKkm528PaXsYfl9CBCFHIw0pU5rzxPd30rgCrc3W4IwuUvAp9lkvXY0swkL8uybix5vcNWk5tKFaYKKyurCWycgCwkf1yPGgCN6kH0Gq4rBvoaD2t8ObibpFGTpn1b0fO0bTgg0fPTSXe3dAwbab_eVcMpAIFsEANdDjOclBSoyf5IHEDRt2FrSWxn0-98tm_gcCei7lqWtpesg9Nv07DNKj4d5ke6mSzWZA0X49keuOHPxhxDbNY2fuz2wlH-_RW3NQEs6sb3Ol1jXh1ynXjIA1XZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه شامگاه جمعه گزارش داد که موشک‌های پرتاب شده از سوی ایران، در شمال اردن رهگیری شدند. به گزارش این رسانه تصاویر رهگیری موشک‌های ایرانی در شمال اردن منتشر شد.
ساعاتی پیش از این گزارش، برخی کانال‌های تلگرامی نزدیک به سپاه پاسداران، اعلام کرده بودند موشک‌هایی از اصفهان، کرمان و کرمانشاه پرتاب شده است.
@
VahidOnLive
وزارت خارجه قطر جمعه ۱۳ شهریور در بیانیه‌ای اعلام کرد این کشور طرف درگیری نیست و حمله به خاک قطر را نمی‌توان توجیه کرد.
این وزارتخانه افزود موفقیت نیروهای مسلح قطر در رهگیری حملات جمهوری اسلامی، از خطر این حملات نمی‌کاهد.
وزارت خارجه قطر همچنین در این بیانیه نوشت «تاسف‌بار»است که با وجود مستند شدن رسمی حمله به راس لفان، وقوع این حمله زیر سوال برده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78234" target="_blank">📅 20:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twWz-f-hMoJZ40q05FHNFwvNdHHTpdG9TSo7u0fujmDTeiLeTh23XwIZSp_4VlWWxhMTJREvXXpphHkCqM99wBKbpRYIld3LdOBeIMxAjYXczsL9lpoSDKuW8Ara-dVBoEAAKKxUxeeUQoS8QaBfu1foZiQQjw9mWTcWBmxNsLWiSP2eUh7pmn-fGvREHU53DFUPVL9B7G5zFFYa8XvwIfQRz2_kZAi0vlcz2UZrvaFUNg2buWp46rFhyaj8ZOVCIdecOSiBlfUssCKBWpH-XY0iQAf_G7JJJiaBxT_QyrdR3R4eJgu_qB4iyPMLC8iaEyVoHGYU5N6xSuPuc6wsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا یک بانک مستقر در ترکیه و دو شرکت وابسته به آن را به دلیل تسهیل انتقال ده‌ها میلیون دلار برای نیروی قدس سپاه پاسداران و فراهم کردن دسترسی جمهوری اسلامی به شبکه بانکی بین‌المللی تحریم کرد.
وزارت خزانه‌داری آمریکا روز جمعه ۱۳ شهریور اعلام کرد «گلدن گلوبال بانک» و دو شرکت زیرمجموعه آن، «گلدن گلوبال وارلیک کیرالاما» و «گلدن گلوبال پورتفوی یونتیمی»، در چارچوب عملیات «طرد اقتصادی» به فهرست تحریم‌ها افزوده شده‌اند. هر سه نهاد در ترکیه مستقر هستند.
وزارت خزانه‌داری آمریکا همچنین در حساب رسمی خود در شبکه اجتماعی «ایکس» اعلام کرد این اقدام بخشی از عملیات «طرد اقتصادی» است و هدف آن قطع «شریان‌های حیاتی مالی» جمهوری اسلامی در ترکیه است. به گفته این وزارتخانه، گلدن گلوبال بانک و شرکت‌های وابسته به آن ده‌ها میلیون دلار تراکنش برای نیروی قدس سپاه پاسداران تسهیل کرده و دسترسی مهمی به خدمات بانکداری کارگزاری در اختیار جمهوری اسلامی قرار داده‌اند؛ دسترسی‌ای که امکان جابه‌جایی بین‌المللی منابع مالی حکومت ایران را فراهم می‌کند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، با اشاره به کارزار دولت پرزیدنت ترامپ برای قطع منابع مالی جمهوری اسلامی گفت مؤسسات مالی همچنان درمی‌یابند که ایالات متحده در اجرای عملیات «طرد اقتصادی» جدی است.
او افزود آمریکا امیدوار است بانک‌های بیشتری نیاز به تحریم نداشته باشند، اما این مسئله به این بستگی دارد که جامعه بین‌المللی به سرعت حمایت از حکومت ایران را متوقف کند. آقای بسنت همچنین تأکید کرد ایالات متحده به همراه متحدان و شرکای خود به اقدامات علیه شبکه‌های مالی جمهوری اسلامی ادامه خواهد داد.
بر اساس اعلام وزارت خزانه‌داری آمریکا، گلدن گلوبال بانک برای فراهم کردن امکان انتقال درآمدهای نفتی جمهوری اسلامی از چین به ترکیه ایجاد شده بود؛ درآمدهایی که پس از انتقال به ترکیه می‌توانست به پول نقد و طلا تبدیل شود.
وزارت خزانه‌داری می‌گوید این بانک همچنین آگاهانه پیشنهاد ارائه خدمات بانکداری کارگزاری به مؤسسات مالی جمهوری اسلامی را داده و از این طریق انجام تراکنش از طریق حساب‌های تحت کنترل نیروی قدس سپاه پاسداران و شبکه‌های وابسته به آن را امکان‌پذیر کرده است.
در اطلاعیه وزارت خزانه‌داری همچنین به شبکه «سیتکی آیان»، بازرگان ترکیه‌ای، اشاره شده است. ایالات متحده این شبکه را پیش‌تر در سال ۱۴۰۱ به دلیل نقش آن در انتقال صدها میلیون دلار درآمد حاصل از فروش نفت مرتبط با نیروی قدس سپاه پاسداران تحریم کرده بود.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، جمعه ۱۳ شهریور در شبکه اجتماعی ایکس نوشت از زمان برقراری دوباره محاصره آمریکا، هیچ محموله نفت خام ایران نتوانسته با موفقیت از تنگه هرمز عبور کند و به چین برسد.
او افزود نفت خام در کشتی‌های گرفتار در داخل تنگه انباشته شده و امکان جایگزین کردن ذخایر صادرشده وجود ندارد.
بسنت نوشت: «مسیر حیاتی صادرات ایران در حال قطع شدن است؛ نفت سرگردان، ظرفیت محدود ذخیره‌سازی و درآمدهایی که به‌سرعت در حال کاهش است.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78233" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78232">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z7Vr4xLs1GUZaRjVoYx3_R6_KYUf87n4IAzMzizliYFZlMg7djhxbAd4X45QBvOc39GY6sYYJvLtll0CREdJosMMgUighLCZ_rJJT1PaxyF7cl54yVvCwxIfEGWj2DWC8iuDLhlOlIbPpIPBbItOMcTZ_idBqFHmV8QBVwAdJLBSO8ajaZ662ZT0VCif1vJcFxHdEvRG5yvEvHaahyalcUvn4yUr17uETuefGY4IU_gfVfRj3XceMduhHXhqpqrdcTOoCzTNqJ33j7mvPcjA7oCkXUhtaHnA0smEQ4sWJdoQQl8PD7pvvTzALxBlqE86AMfT40axFZAuIa34vGq2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
دیوانه‌های چپ رادیکال، دموکرات‌های احمق و کمونیست‌ها ترجیح می‌دهند ما در جنگ ایران شکست بخوریم تا اینکه رئیس‌جمهور دونالد جی. ترامپ جنگ را برای آمریکا ببرد.
به عبارت دیگر، آن‌ها ترجیح می‌دهند ما ببازیم تا اینکه ما پیروز شویم!
این‌ها آدم‌های بسیار بیماری هستند که از TDS شدید رنج می‌برند؛ چیزی که گاهی از آن با عنوان «سندرم جنون ترامپ» (TRUMP DERANGEMENT SYNDROME) یاد می‌شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78232" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78231">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF_Hxp8SVtcpUkeNlSiiJCSGVpYuI6ZmRWMLD5KfLo5Xp5V3gZzmf-rlvjy6jgXhF6jed5sOp9ktK6ob-rDiIqdZJmhjQIBpcqPsjtBW1t2KLRqZgGzyjQBRp2LdSDDOwXUQd-E4Li12HmGV1VUljh3A13UJNFdfGTyeodINICgRA0wEX76oS0qH5rXcDZ6ipXZBn3Sx42TFX7Py2-1vAiUSxPwBdV9KLWPlnrr5tvb80UmC7drNHQ1fCN5_8gid3RPgTt1R_h5ox1T-xiC7oqWL4Hoi3T_0rkRE14fAO80mDIz08M7yXG8WNlFdDWWkmz2ZpHVsj_FOIiOUBZ1NCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «فایننشال تایمز» روز جمعه ۱۳ شهریور در گزارشی اعلام کرد اختلافات میان ایالات متحده و جمهوری اسلامی ایران بیش از پیش بر سر آینده تنگه هرمز متمرکز شده است؛ چرا که دولت دونالد ترامپ بازگشت به یادداشت تفاهم اسلام‌آباد را رد کرده، در حالی که تهران خواهان احیای این توافق به عنوان زمینه‌ای برای کاهش تنش‌ها و ازسرگیری عبور نفت از تنگه هرمز است.
بر اساس این گزارش، تلاش‌های دیپلماتیک برای بازگرداندن طرفین به تفاهم‌نامه اسلام‌آباد که شامل توقف اقدامات نظامی، بازگشایی تنگه هرمز و آغاز مذاکرات جامع‌تر بود، با مخالفت واشنگتن روبرو شده است. آمریکا اکنون خواستار توافقی جدید و فراگیرتر است که علاوه بر وضعیت تنگه هرمز، پرونده هسته‌ای ایران را نیز شامل شود.
در مقابل، مسعود پزشکیان تاکید کرده که کشورش آماده است به محض بازگشت آمریکا به تعهدات خود در توافق موقت، به تعهداتش عمل کند.
با این حال، واشنگتن بر اهرم فشار میدانی حساب باز کرده و با تقویت حضور نظامی، مین‌روبی و ایجاد مسیرهای امن، سعی دارد ثابت کند ایران دیگر نمی‌تواند از تنگه هرمز به عنوان یک کارت فشار بر بازار انرژی استفاده کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78231" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CbIQsQRGTsbT65LwynIzo6CAZZ1ow_jPj2xirfwh1CRW_ga6awZdqVcFFhfR-EJxPV4FYPfOQ6uXvqrauGJR7mdHKKduZojXusqFI1YMsmWhrYYNbmwDi9wI3wU7q1kHPJAijmpRDI40jh9iK1EYXqhi8m2Xf8AhQ6z8fAlgmhlfYBjSj_UKGJ15F6YK30kb-T4kUWuFvqC2icTi0tV_yWMjjv1vxpKRER2ZMHw6T5MfETlaLqaMS1-UQMAb41yqSN8RnmZKBer5Ho21GJkbuufXWtQ9a5e2qZRpO69X4EEYhZ9uaPI0qHa7Y-xdgprEr6S7AHdXUdFOAZasFR9lxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت گازوئیل در آمریکا با ثبت رکورد تازه‌ای به بیش از پنج و نیم دلار در هر گالن رسید.
انجمن اتوموبیل آمریکا روز جمعه ۱۳ شهریور اعلام کرد که قیمت گازوئیل در این کشور در حال حاضر به پنج دلار و ۸۵ سنت به ازای هر گالن رسیده، در حالی که یک سال پیش قیمت آن سه دلار و ۷۱ سنت بود.
هر گالن حدود ۳.۸ لیتر است.
انجمن یادشده این افزایش قیمت را ناشی از اختلالات در حمل‌ونقل سوخت به‌دلیل جنگ آمریکا با ایران عنوان کرده است.
گازوئیل، سوخت حیاتی مورد استفاده در حمل‌ونقل جاده‌ای، کشاورزی و ساخت‌وساز محسوب می‌شود و بیم آن می‌رود که افزایش چشمگیر قیمت آن، نرخ تورم را افزایش دهد.
قیمت بنزین معمولی در آمریکا نیز چهار دلار و ۱۵ سنت به ازای هر گالن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78230" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/is-ym1OhXODCcvGZiMqVKB5UMdacWKbYmnjpSr9P9_X2UwwtIi7cLMV1m4oNyxSynqxpf0FciXa8m33uns-_phiwIlSSg2djFHzKn5WnXxoUfmioIH4KCWh0lIWzp_7NhIKH5ak7IfobM1mmQ8wCZBhcqWuCZtkz1UZx3xXD1oyrur7noTR3haETwqEeT9fEwpWOCl8lentfAjOATNE40TWT6Bwe3W_50T6ObZV24gxAvgW2JYzGg8k6OXb7jDTP-yLw2gGK9tcfDkLK1VAcaXgrXiFulY1l7ycaviuyf8_LYiIt66KXIOBdDLyf9IqN0AKUQEIxG5k6hufJEjhYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌هایی که من دیروز دریافت کرده بودم:
▪️
آزمون Pte  زبان برای ساکنان ایران لغو شد
▪️
موسسه‌ی پیرسون هم تمام آزمون‌هاش رو برای ساکنین ایران کنسل کرد.
امروز صبح روی سایت اعلامیه زدن یک دفعه.
مشهورترین‌هاش برای ایرانی‌ها امتحان مدیکال کانسیل استرالیا و وزارت بهداشت عمان هست.
و امتحان‌ زبان PTE
▪️
ما جمعی از پزشکا برای مهاجرت استرالیا تلاش میکردیم و هزینه ازمونمون ۳۰۰۰ دلار بود
الان لغو شده بدون هیچ توضیح خاصی
دوستان هتل و پرواز بوک کرده بودند برن هند پیام بدن الان میگه نمیشه باید کارت اقامت کشور دیگه ارائه بدی
خبر:
موسسه بریتانیایی «پیرسون» که برگزار کننده آزمون‌ زبان انگلیسی «پی‌تی‌ئی» و آزمون ای‌ام‌سی (شورای پزشکی استرالیا) است، در بیانیه‌ای اعلام کرد که به دلیل تحریم‌های جدید آمریکا علیه ایران، آزمون‌های داوطلبان ساکن ایران را لغو می‌کند.
پیشتر در تاریخ ۷شهریور۱۴۰۵، تعداد دیگری از برگزارکنندگان آزمون‌های مهارت‌های زبان‌های خارجی، از جمله دولینگو و تافل، اعلام کرده بودند که این آزمون‌ها دیگر در ایران برگزار نخواهد شد.
پیرسون در اطلاعیه‌ای درباره لغو آزمون پی‌تی‌ئی آورده است: «در پی تعلیق 'مجوز عمومی G' توسط دفتر کنترل دارایی‌های خارجی (OFAC) در وزارت دارایی آمریکا، از ساعت ۱۲:۰۰ بامداد هشتم سپتامبر ۲۰۲۶ به وقت شرق آمریکا تا اطلاع ثانوی، ما قادر به برنامه‌ریزی یا برگزاری آزمون برای داوطلبان ساکن ایران‌ نخواهیم بود، مگر آنکه بتوانند مدرکی دال بر اقامت اصلی خود در خارج از ایران ارایه کنند.»
در ادامه این اطلاعیه آمده است: «آزمون‌هایی که در حال حاضر برای داوطلبان مشمول این محدودیت برنامه‌ریزی شده‌اند، لغو خواهند شد. به‌خاطر این مشکل که برای آنها ایجاد شده، پوزش می‌طلبیم.»
سرنوشت شمار زیادی از دانشجویانی که قصد مهاجرت با هدف ادامه تحصیل به کشورهای اروپایی، آمریکا، آمریکای شمالی و استرالیا را دارند تحت تاثیر این اقدامات قرار خواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78229" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=vCyNsNuCDYD4HqkgspZ_fmplL554kavvy7btDvc3yoNiXa2Z_8CWI0cKVO5hg2Y3q3nD1iS3Kf0YiMgezgGEke1XRtY3_W2m25Bv-Zvo2Ebc3FkzKs5-FfGl1c2mq8jkXAmMHujlJqQ5ZXGVW-3zgCzoavk-bjVg0X5tdq2fJT6M2wIdVNI6ZJ7QZcT62lHsLUVQriujLY2pEnM4_EUspYRDtRX1Ky3Ax3EzRAZ9GaUABEhe7BhIBIEjIHOGY-NN3WSafgYrARXtcaf8Hf9WhhSTVqfMdldZ5BhXSoQzoMMqidY3MI75qohfDilRsy2Oyq2e7qvZlTnYfbZAMhSpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=vCyNsNuCDYD4HqkgspZ_fmplL554kavvy7btDvc3yoNiXa2Z_8CWI0cKVO5hg2Y3q3nD1iS3Kf0YiMgezgGEke1XRtY3_W2m25Bv-Zvo2Ebc3FkzKs5-FfGl1c2mq8jkXAmMHujlJqQ5ZXGVW-3zgCzoavk-bjVg0X5tdq2fJT6M2wIdVNI6ZJ7QZcT62lHsLUVQriujLY2pEnM4_EUspYRDtRX1Ky3Ax3EzRAZ9GaUABEhe7BhIBIEjIHOGY-NN3WSafgYrARXtcaf8Hf9WhhSTVqfMdldZ5BhXSoQzoMMqidY3MI75qohfDilRsy2Oyq2e7qvZlTnYfbZAMhSpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
الان از اصفهان موشک زدن یه دونه
سلام وحید جان
ساعت 7:12 دقیقه از اصفهان موشک شلیک کردن ( از سمت [....] اصفهان)
همین الان [...] اصفهان موشک رفت
19:13 از سمت [...] اصفهان موشک زدن
همین الان ۱۹:۱۲ از سمت [...] اصفهان
فکر کنم [...] بود
بالسیک شلیک شد به سمت [...] رفت
از اصفهان همین الان موشک زدن صدای وحشتناکی داد
اقا همین الان یه موشک از سمت اصفهان شلیک شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78228" target="_blank">📅 19:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjglx20q1Fc4O4R2cGIGxohJfY1awL_MlymEdwNhEa_HD2k7BZLCU6nMqE1LE8BGBH4-N7atshCCMvpeHdWR-FN_xIYB2phCr0wGfUSYw-ervHf49-Tm3FhEnFlyo5vCvkxUAs3Ff3o5xTzG7H4e3JflackpKD7lBBpj1yOgZE0ZsN9UYo5sce06qKBHh2Pdv5oY1aEkZiaiZQuSQyFidVB7qAxKPTGh4CNwUhZTsPvwENQWCMznCTlOFNpHER_xUGBlZ3YjRwitf18uj6jZP5PIUa9swnc-qR99rv9-AA53TGqzOsdTiavcu5TO28z4_IlZTOE2z7M2Ih-AygF3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست پنج‌شنبه ۱۲ شهریور به نقل از یک مقام ارشد منطقه‌ای گزارش داد عمان پیشنهاد جمهوری اسلامی برای دریافت مشترک هزینه خدمات از کشتی‌های تجاری عبوری از تنگه هرمز را رد کرده است.
این مقام گفت مسقط حتی با دریافت داوطلبانه هزینه خدمات زیست‌محیطی و امنیتی از کشتی‌ها موافقت نکرده است.
یک مقام آمریکایی نیز به نیویورک‌پست گفت شرایط توافق پیشنهادی میان جمهوری اسلامی و عمان برای تقسیم درآمد نهایی نشده است.
این اظهارات در حالی مطرح شد که حسین محبی، سخنگوی سپاه پاسداران، پیش‌تر از دستیابی تهران و مسقط به توافق در این زمینه خبر داده بود.
رویترز هفتم مرداد گزارش داده بود عمان طرحی با حمایت کشورهای خلیج فارس به جمهوری اسلامی ارایه کرده است که بر اساس آن، مدیریت تنگه هرمز به شکل منطقه‌ای انجام می‌شد و شرکت‌های کشتیرانی می‌توانستند به‌صورت داوطلبانه برای تامین هزینه‌های ناوبری، حفاظت زیست‌محیطی و عملیات جست‌وجو و نجات مبالغی پرداخت کنند.
عمان پیش‌تر نیز با دریافت اجباری هزینه از کشتی‌های عبوری از این آبراه مخالفت کرده بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78227" target="_blank">📅 02:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JbJg_ZFnjk0-f9Qz2r_0M9YaQjsQytRbsl5tDQws_FNmCc2ClzikUz-x3W6CKbocxA7-jJpGsOIMBMeDq7pwNEAkir3JQhR1ESSVVVwUv-_Ghj5HC5hg6h7_ydsfNQjA3fFc-drofqWkHxj6yNx3vVUcm7OgRLdU7F6hatbA8v_irtBj7hANBcNrRuODbw_OTZ-QBtOcxKnMMKDGRH76LT68vrBtY2-7lw7DoXfqcZm_uwIyCK3qJAxLGaRjHXU5Y3YCQWoDElWcU8gmkX_74qOFCeepRCwhg2e0dJ1t7kE_WJyxTnGVG3UvSDhW8QC2F09xCxaqj1rxdEsdiDb2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EmTEYj-gPqdYRBrh97oRCD2NdipV93eLgIig1o7BpZBcAvdDJZUsh8fvmJm5quLolF3ejp4jdES59CcjDjD1shPZuUln6IZbUbcYWXB3SbkQTPxMt-vrtDw70Q4zM7cp0eh0kmvCsnpzPcm2xteeCktF5oTiOO9IHXIr1QkalEH3yg8vcNi7ax1KlhQFrTUoFL6UR5YtzE1agz4WahPot9PTOUcmxjMNwW2TmkdwErbYDtcqk27VUVztpYCngoaQA3mbEagelP17SInEIEt6Mb0APdy7UirFIggHw01KonKnErcvFAEHfw2TPgh0Tsi-d6FnA-u508q4Lc79dH6suQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگو با شبکه جی‌بی نیوز گفت:
«آن‌ها سه سایت داشتند و شاید حالا کوه کلنگ گزلا را هم داشته باشند، اما ما روی همه این مناطق دوربین داریم. می‌دانیم چه کسی وارد می‌شود و چه کسی خارج می‌شود.»
او در ادامه درباره توان اطلاعاتی آمریکا افزود: «حتی می‌توانیم از فضا اسم افراد را بخوانیم. آن‌ها حتی نمی‌توانند بدون اینکه ما متوجه شویم جابه‌جا شوند. ما دقیقا می‌دانیم چه خبر است و از این بابت کاملا مطمئن هستیم.»
@
VahidOOnLine
گفت:
ما کنترل کامل تنگه هرمز را در اختیار داریم. هر شب ۳۰ تا ۴۰ قایق آن‌ها را از بین می‌بریم و رادارهایشان را هدف قرار می‌دهیم.
او همچنین افزود اقتصاد ایران «در حال فروپاشی» است و افزود: تورم ممکن است به ۳۰۰ درصد برسد، پولشان تقریبا بی‌ارزش شده و نرخ برابری آن با دلار حدود دو میلیون به یک است و هر روز هم بدتر می‌شود. آن‌ها واقعا در وضعیت بسیار بدی قرار دارند.
@
VahidOOnLine
گفت:
با جلوگیری از هسته‌ای شدن ایران، اروپا و بریتانیا را هم نجات دادم
«من کشور شما را هم از این تهدید نجات می‌دهم، چون اگر ایران سلاح هسته‌ای داشت، احتمال اینکه از آن در اروپا استفاده کند بیشتر از آمریکاست، زیرا توان موشکی برای رسیدن به اروپا را دارد، نه آمریکا.»
او همچنین افزود ایران تنها «دو تا چهار هفته» با دستیابی به سلاح هسته‌ای فاصله داشته و حملات آمریکا این روند را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78225" target="_blank">📅 02:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پاسخ جی‌دی ونس معاون رئیس‌جمهور آمریکا به پرسش‌های خبرنگاران
بخش‌های مربوط به ایران با تشخیص و ترجمه ماشین
متن زیرنویس:
https://telegra.ph/vance-09-03-3
خلاصه‌ای از اون متن مفصل به تشخیص ماشین:
1️⃣
ونس: «تنها دلیل اینکه بحران جهانی انرژی نداریم، رهبری ترامپ است»
▪️
«دلیل اینکه قیمت بنزین اکنون این‌قدر بالاست این است که ایرانی‌ها به کشتیرانی تجاری شلیک می‌کنند.»
▪️
«فقط دیروز حدود ۱۵ میلیون بشکه از تنگه هرمز خارج کردیم.»
▪️
«ایرانی‌ها دارند می‌فهمند که کنترلشان بر تنگه هرمز عملاً از بین رفته و این اهرم هر روز کم‌ارزش‌تر می‌شود.»
▪️
«توصیه من به ایرانی‌ها این است که دست از رفتار مثل آدم‌های دیوانه بردارند و به کشتیرانی تجاری شلیک نکنند.»
▪️
درباره حمله به مراسم عروسی: «در این مورد مشخص، من فکر نمی‌کنم اطلاعاتی داشته باشیم که چیزی را به این سو یا آن سو ثابت کند.»
▪️
«ایالات متحده هرگز در جنگ غیرنظامیان را هدف قرار نمی‌دهد.»
▪️
«در حال بررسی آن هستیم.»
2️⃣
ونس درباره ایران: «فشار اقتصادی، نظامی، دیپلماتیک و مخفیانه؛ همه روی میز است»
▪️
«ابزارهای اضافی زیادی هم در اختیار داریم. رئیس‌جمهور از برخی از آن‌ها استفاده می‌کند و از برخی هم نه.»
▪️
«هر اتفاقی که ممکن است بیفتد روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه.»
▪️
«ایرانی‌ها مثل تروریست‌ها در تنگه هرمز رفتار می‌کنند.»
▪️
درباره احتمال حمایت از مخالفان ایران: «البته، من قرار نیست درباره‌اش صحبت کنم.»
3️⃣
ونس: «آمریکا تنها کشوری است که می‌تواند کنترل تنگه هرمز را تضمین کند»
▪️
«ما تنها کشور دنیا هستیم که می‌تواند کنترل تنگه هرمز را تضمین کند.»
▪️
«ایرانی‌ها دوست دارند صفر میلیون بشکه از تنگه هرمز خارج شود. دیشب ۱۵ میلیون بشکه از تنگه هرمز خارج شد؛ و این به‌خاطر ایالات متحده آمریکاست.»
▪️
«اگر ما این کار را نکنیم، هیچ‌کس دیگری نخواهد کرد.»
▪️
«پیام ما به ایرانی‌ها ساده است: باید شلیک به کشتیرانی تجاری را متوقف کنید.»
▪️
«ما با آن‌ها صحبت نمی‌کنیم و صحبت هم نخواهیم کرد مگر اینکه شلیک به کشتیرانی تجاری را متوقف کنند.»
4️⃣
ونس: «برای پایان درگیری با ایران ضرب‌الاجل مصنوعی تعیین نمی‌کنیم»
▪️
«باز هم، من اسمش را جنگ نمی‌گذارم.»
▪️
«عملیات عمده رزمی حدود شش هفته طول کشید.»
▪️
«با عملیات Midnight Hammer تأسیسات هسته‌ای‌شان را نابود کردیم.»
▪️
«با Epic Fury، پایگاه صنعت دفاعی آن‌ها برای تولید سلاح و همچنین بخش بزرگی از توان نظامی متعارفشان را نابود کردیم.»
▪️
«یک ضرب‌الاجل مصنوعی تعیین نمی‌کنیم.»
▪️
«غیرمسئولانه خواهد بود اگر راهبرد و جدول زمانی‌مان را برای کشوری مثل ایران تشریح کنیم.»
5️⃣
ونس: «توان ایران برای مختل کردن زندگی عادی آمریکایی‌ها بسیار محدود است»
▪️
«اطمینان زیادی داریم خاک کشور امن است.»
▪️
«ایرانی‌ها تلاش خواهند کرد کارهای زیادی انجام دهند که توان انجامشان را ندارند.»
▪️
«اگر توان ایران را برای مختل کردن زندگی عادی آمریکایی‌ها در نظر بگیرید، به نظرم بسیار محدود است.»
▪️
«صفر نیست، اما بسیار محدود است.»
▪️
«من خیلی بیشتر نگران حملات سایبری از سوی بازیگران دیگر می‌بودم.»
6️⃣
ونس: «چین به برخی درخواست‌های آمریکا درباره ایران پاسخ مثبت داده است»
▪️
«ما قطعاً چندین گفت‌وگو با چینی‌ها داشته‌ایم.»
▪️
«فکر می‌کنم چینی‌ها به برخی درخواست‌های ما پاسخ مثبت داده‌اند.»
▪️
درباره تماس مستقیم ترامپ و شی: «در واقع نمی‌دانم آیا رئیس‌جمهور مستقیماً با شی صحبت کرده یا نه.»
7️⃣
ونس: «کشورهایی در خفا برای مجازات ایران به آمریکا کمک می‌کنند»
▪️
«فکر می‌کنم جمهوری خلق چین قطعاً بسیار مسئولانه‌تر از ایرانی‌ها رفتار کرده است.»
▪️
«اگر به ترکیه، آذربایجان، امارات، عربستان سعودی، قطر و بسیاری از کشورهای ائتلاف عربی خلیج [فارس] نگاه کنید... کشورهای زیادی هستند.»
▪️
«گاهی حاضر نیستند علناً بگویند، اما در خفا کارهای خوب زیادی انجام می‌دهند تا به ما کمک کنند مطمئن شویم ایرانی‌ها بابت شلیک به کشتیرانی تجاری هزینه می‌دهند.»
▪️
«این کار همچنین منابع اقتصادی لازم برای بازسازی برنامه هسته‌ای‌شان را از آن‌ها می‌گیرد.»
▪️
«تا اینجا ندیده‌ایم که تلاش کنند چنین کاری انجام دهند.»
▪️
«همه این‌ها در خدمت این است که مطمئن شویم ایران به یک قدرت دارای سلاح هسته‌ای تبدیل نمی‌شود.»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78224" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ونس: نسبت به احتمال نقش آمریکا در حمله به مراسم عروسی در سیریک بدبین هستم
🔸
معاون رئیس‌جمهور ایالات متحده می‌گوید تحقیقات دربارۀ «ادعای حمله به یک مراسم عروسی» در جنوب ایران ادامه دارد.
🔸
جی‌ دی ونس که روز پنجشنبه ۱۲ شهریور در کاخ سفید به پرسش‌های خبرنگاران پاسخ می‌داد، در پاسخ به سوالی در این زمینه گفت: هنوز اطلاعات کافی در اختیار نداریم اما ارتش ایالات متحده «بر خلاف سپاه پاسداران» هرگز غیر نظامیان را هدف قرار نمی‌دهد؛ اما گاهی ممکن است «اشتباهاتی» رخ دهد.
🔸
معاون دونالد ترامپ در ادامه گفت: نکتۀ مهم این‌ است که حتی در صورت بروز اشتباه هم، نیروهای مسلح ایالات متحده، «باز هم بر خلاف سپاه پاسداران»، از اشتباهاتشان درس می‌گیرند تا چنین اشتباهاتی تکرار نشود.
🔸
ونس در نهایت با تأکید بر این‌که تحقیقات ادامه دارد و هنوز اطلاعات کامل نشده، گفت شخصاً نسبت به احتمال نقش آمریکا در بروز این حادثه «بدبین» است.
🔸
به گفتۀ مقام‌های ایرانی، در جریان حمله شامگاه ۱۰ شهریور آمریکا به یک مراسم عروسی در کوهستک سیریک در نزدیکی تنگهٔ هرمز، چهار تن از جمله یک کودک کشته و ده‌ها تن زخمی شدند.
🔸
وزارت دفاع آمریکا از ۹ اسفند‌ ۱۴۰۴ و حادثۀ حمله به یک مدرسه ابتدایی دخترانه در میناب هم اعلام کرده که مشغول تحقیق است، اما بیش از شش ماه پس از حادثه و با وجود فشار کنگره، هنوز حاضر به انتشار نتیجۀ تحقیقات نشده است.
🔸
مقام‌های جمهوری اسلامی می‌گویند که در جریان حمله به مدرسه شجرۀ طیبه، بیش از یکصد دانش‌آموز،‌ معلم و اعضای خانواده‌های دانش‌آموزان کشته شدند.
@
VahidHeadline
بعدا ویدیویی زیرنویس شده شامل حرف‌های احتمالی دیگر می‌گذارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78222" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q3n9VZbwTd76fbO7HAtwa8N1kb6aDUBWeQiDDweY-omFBiCNPBtYpXUkFnkZltJWmOZ-CjoxeveDDTTEzMAMs1qdRRtAMljVH4nB3rnKlYTxNiW9snaAldevUFPDOtUjQ4LemqNnMJ8k6HVHEYX9mZLK4jwZuWl52beDCBW8I20-a-h66zEhWyynTXSTCHQAJcw8bbXL3uGeRQ6BNnKF9Jq9Laf4UwyqAFQXc0WwhKpfTD9rCW_KOufrozoUBwsyeuOfl06NlZ4SY68FsRKtmcpopCyoFo4l_95a_yTx7jNqP5t-v7jrhndF3KqdrHSeMV-Eu1E6ifgvbRxL6yzufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ppE9dDHXREynpLh3vn5e4-Xjl0RyOEWAtTPBwQtYTEuFCf_TLTi7ELsMl0RGM82pULwM02N7BB8pNvf9p5Pf9LkAT4WNfu6A7vPMWVhT1FP34oRElfnzttesQAv7__i1hgnrpxRNjdnGUJqKUyC7FW0zFr4mZvsD_WKkBh5zr5r3c5P6rtITIpsrk2oQNGOEszL1-_WjWmQeY-eH5oTN9-zPW9uYtuNddlHSG_RNNyGIrhsXQayn9O_LuYDH7bHNYRx5ToILFqBsaev48Fu2ClTG8-C86k73cML7gl9JgMagN-rq7ep3YheIu2JooTXsPjo9CNT6uvnZ5Ofrilyk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ca-SZMmVThtYPt345C6Y0H61OTcggQVrpQlA7RK6mVgolnnokQykZHNYl3QXXURvNiTvA5cyiM7CW9M7L2a5vL9gaKCAK3Yn_6l6iqj3tx-7vhBRpVnbypaUzk_esIREq1StDV51Z3fzgqDeqswrqHhIWEg-UdJGnFWZAxOEnB-sI6ME4OboidWRD9m3nE-VT-w0HOfNfDh2JyGPfKlQbip-62mxk7FC5pItgz4jELds1tC2uA05sbMK7LSuiU88IWE_UAIUDMhCQofYMvlPd6x7sDUQlMzlwdHZ8U8LrTUCT7SrWK8bTLEI7lugz91v3_r3UJA326R8QGYGmFUK8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📝
درباره حمله به مراسم عروسی در سیریک چه می‌دانیم؟
🔹
همزمان با حملات هوایی آمریکا به شهرستان سیریک در شب ۱۰ شهریور ۱۴۰۵، انفجاری خانه‌ای را در بندر کوهستک تخریب کرد که در آن مراسم عروسی برگزار می‌شد. بر اساس گزارش‌های منتشرشده، تاکنون پنج نفر، از جمله یک کودک چهار ساله، جان باختند و ۶۵ نفر مجروح شدند.
🔹
تصاویر محل حادثه، صدای چند انفجار در ویدیوی دوربین مداربسته، بیانیه سنتکام و تکذیب‌نشدن حمله از سوی سخنگوی این نهاد، انتساب حملات آن شب به آمریکا را تقویت می‌کند.
🔹
همزمان در شبکه‌های اجتماعی ادعا شده بود که انفجار خانه نتیجه «پرتاب ناموفق موشک سپاه» بوده است؛ اما تاکنون هیچ گزارش رسمی یا مدرک معتبری این ادعا را تایید نمی‌کند.
🔹
برخی حساب‌ها برای اثبات این ادعا، ویدیوهای قدیمی یا نامرتبط را منتشر کرده‌اند. تنها گزارش مشابه درباره یک پرتاب ناموفق سپاه در همان شب، مربوط به خمین در استان مرکزی بوده و ارتباطی با سیریک در جنوب ایران ندارد.
🔹
با وجود شواهدی که از حمله آمریکا به سیریک وجود دارد اما هنوز مشخص نیست دقیقا چه پرتابه‌ای به خانه محل برگزاری عروسی برخورد کرده است.
🔹
این در حالی است که در ویدیوی دوربین مداربسته، صدای پهپاد شنیده می‌شود و پدر عروس نیز در یک مصاحبه تصویری به شنیدن صدای پهپادها اشاره می‌کند؛ شواهدی که احتمال استفاده همزمان از موشک و پهپاد در عملیات را تقویت می‌کند.
🔹
این در حالی است که قطعاتی از موشک کروز SLAM-ER در منطقه دیده شده، اما میزان تخریب خانه با انفجار کامل سرجنگی ۳۶۰ کیلوگرمی این موشک سازگار به نظر نمی‌رسد.
🔹
احتمال دارد خانه با مهماتی کوچک‌تر، (مثلا پهپاد لوکاس با سرجنگی حدود ۱۸ کیلوگرمی) هدف قرار گرفته باشد و قطعات SLAM-ER به اصابت دیگری در همان محدوده (دکل مخابراتی در فاصله حدود ۱۳۰ متری) مربوط باشند.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78219" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3IGbae173Ajv07I931RPobyr7EHm8xgPO8B4E5hxLSuYkE4dgTMNafugujQ4pTh8FZxOsclkfHTerAwL4Bt3OjHqDKNWxWtouFkihcO---Wni-XJJuYqjHyk292JwT0kBpjnhkDO6NRcJAIiOvPuQRIj4JXl4P0z4gnoo6IFibu5bH6B7rMMBOBa29uBFR5zE_h0kfYXftdWoh5XokpnKM_svrmQx7YyMKpewpDDT7LiPTBVpV35ppZfLGAQ_OLyUD-QmWRgcwFPLm423ula9yQsjnMd7POBH4VHkfHmIsTzlOxJBaLPXSRulON8bispf6iMcHOau3485-uvDffdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست‌ها که در گوشه کادرشون نوشته شده Ad تبلیغاتی هستند که به خود تلگرام سفارش داده میشن.
من نمی‌تونم جلوی نمایش‌شون رو بگیرم:
https://t.me/VahidOnline/73400
https://t.me/VahidOnline/77482
https://t.me/VahidOnline/77989
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78218" target="_blank">📅 19:03 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
