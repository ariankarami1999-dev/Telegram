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
<img src="https://cdn1.telesco.pe/file/gtL8SkRxiJEeSQSAcmBc0K0ZAmBnVR4XX9BYk_oz9bLrP9XWfU5aX3PmAL3bBrBoQxHW4QVsC0eYySZZmSIsZKqEFpucd2E1kf7iEYUzzG312b4bKAlJ22uoJd7XC6zUu2eunqIPfUHozJTH2qwm0pLlV-zBfNNAnQp2ZNaweMfW0mxiYHxYGTYodSth5JR0BJrobHGtzlLK29ne_ORZORkIetl7o1kHLDpuSMvmwgb8UFmG198x07TnR3oi-fElj2xVPNy2Mb9udpJtd60phDcXC4mn52MME4K65ZUGhZY1-T9nY78Xi-zBYIwkr1D8XPYbrwfji2AuFkOI_cZ70A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3hbE973k9_4riEpDsXp_04kyD7dOTZl6rgtTzwI5dL7mSHtNnB1MB1PJ8zKZZi_aNAhqGdjQmFfetPKFLt8lk56cdLGuW8ihMXYt2ctJkAOXfr_mt1UucGM1yqESTZvBfeXweHQYYLhifnuC_KPsPDcFNLbBidCBnbFRwwdc-JIwkNeXealsLOrUkAIQ7A_XYIAbEPVSdFV-iu1A7wrOD47IYLM3zPhQ0e_XqY1mLsLxcLvaD3Ie0LvGEnk5mFjfMzQxZTSvhnLhwAqWH-mK_MkfLHWW2YXsAjuz-4z2qs_gZepooriT6SaPSQ-lxV9z3MIC4CD7G2SeQRFK0ABwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس سازمان اورژانس ایران، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اعلام کرد در جریان حملات اسراییل به ایران، ۱۵ نفر مجروح شده‌اند و تاکنون هیچ موردی از جان‌باختن شهروندان گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/VahidOnline/76063" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWvamWPV6sBQ8vxxzof1aDm_2q-yRmrrBgP1dHvMYVOos-BGls0JPy4uUnqnaAwiAZ5qVVdZAE9DV0h984j7nv9x-3JGOAt-viLAPdZZ-8-XDe46yIXSK99ULPYmCAqdzQuaUU6oOxB0PxCwY0AnVhNs7khmygmAk0-C9W6u3GS0Nswci0vLEq3593iy_Oc8Y1_UqwL6YgQv5WDnyze2oApKEDxhSzsHTClVHYPpZFnt7VxkBb2VwnN2r8rm9caQUaQTxYMHBhb2DD_LKQw1k1dA3Jmhupa6LyABaoqFeJvd3RCBFtxuHxhIO0aAhKABUz9mU33X0i6YD2crkF9_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایسنا عصر روز دوشنبه، ۱۸ خردادماه، به نقل از شرکت فرودگاه‌ها و ناوبری هوایی ایران خبر داد که «همه پروازهای فرودگاه‌های کشور تا اطلاع ثانوی لغو شد».
این اداره همچنین از تمام مسافران خواست تا «جهت حفظ نظم و پیشگیری از هرگونه سردرگمی، تا زمان اعلام وضعیت عادی از سوی مراجع ذی‌صلاح به فرودگاه‌ها مراجعه نکنند».
این خبر ساعتی پس از آن منتشر شده که قرارگاه مرکزی خاتم‌الانبیاء سپاه در آغاز بعدازظهر روز دوشنبه با انتشار بیانیه‌ای از توقف عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل خبر داد.
همزمان رئیس سازمان حج و زیارت خبر داده است که «با توجه به شرایط پروازهای بازگشت حجاج احتمال تأخیر در برخی پروازها حتی تا ۷۲ ساعت وجود دارد».
او اضافه کرد: «برای فردا (سه‌شنبه ۱۹ خرداد) ۱۰ پرواز پیش‌بینی شده که امیدواریم بخش عمده آن‌ها انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/VahidOnline/76062" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns28mmaEqFHd715oBQ8Ul7u-gQHwAd8dczbTTpai-8Rv3leACEOiMCcCscVoeqmBS6D6qbZJeIEe5DrnEsz8iCIqlPlrpNdAtXL_T8GBw86GOwlGP-4H8I_SDsyuO030mmbjAF3Uj7aFFpp2wz4MG8rBxRg5kXow0pr7NvNr-nzHzvnHF8ARtXZs6R1UUWFe4yCGnIrKxxG6msXEfVgUR581n-fIiJD8FGTg3wFX4DRcoAJFmy-fdRmPwWEtPRgUXs4uE15QhpQgL4NSS6hFX1ShQe78sSqkFpc4zl1aI_Diokqwps8hqMDiKodYwD4Fq8zhvJKdvKlYupf1ZX2l5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا، روز دوشنبه ۱۸ خرداد اعلام کرد که اتحادیه اروپا به‌دلیل تهدید آزادی تردد دریایی توسط جمهوری اسلامی، تحریم‌هایی را علیه شماری از افراد و نهادهای ایرانی اعمال کرده است.
کالاس این اظهارات را در جمع خبرنگاران و در حاشیه نشست وزیران دفاع اتحادیه اروپا در قبرس مطرح کرد.
هنوز جزئیات بیشتری درباره این تحریم‌ها ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/76061" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b31564948.mp4?token=O59wzMvsVgFtboLWYy9_DGFQDIwq2USHlqeGL_qgsWC48RDZPKzjuNGjVZO5gTVrnTGqRm1kwHfXS1pD8L1RF20wN7cBDyRzWPSNdWaKc7ia3kIoPFVoZ7diIyT0ow7fDeIrQhOhdZuZB4DTMxLyLy7yMF2M6XxbgvVYEMR8TraRUcyhfbNMQrYSXcoYKJYtBTcear4ODYXsWSptSfZF_k_1lYkU3v7ZbuWyYyCxdhqjJsLYC9vCFT5V90XxMiPo97r2NczdJyaiym2ApuEIwEhJPMfOWyOyEGOO2UKFDcbsmDD1UN6IX6JIs0NFYnEt4VGGmzWNvJNezbcOKU2CVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b31564948.mp4?token=O59wzMvsVgFtboLWYy9_DGFQDIwq2USHlqeGL_qgsWC48RDZPKzjuNGjVZO5gTVrnTGqRm1kwHfXS1pD8L1RF20wN7cBDyRzWPSNdWaKc7ia3kIoPFVoZ7diIyT0ow7fDeIrQhOhdZuZB4DTMxLyLy7yMF2M6XxbgvVYEMR8TraRUcyhfbNMQrYSXcoYKJYtBTcear4ODYXsWSptSfZF_k_1lYkU3v7ZbuWyYyCxdhqjJsLYC9vCFT5V90XxMiPo97r2NczdJyaiym2ApuEIwEhJPMfOWyOyEGOO2UKFDcbsmDD1UN6IX6JIs0NFYnEt4VGGmzWNvJNezbcOKU2CVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی از لحظه حمله‌ الهه و شهربانو منصوریان به اتاق ریاست فدراسیون ووشو و شکستن دوربین مداربسته منتشر شده است.
طی سال‌های اخیر
خواهران منصوریان
بارها به ساختمان فدراسیون یا کمپ تیم‌های ملی حمله کرده یا با مدیران درگیر شده‌اند، اما همواره از حمایت نهادهای حکومتی برخوردار بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76060" target="_blank">📅 15:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAbzoYyBTM4k4Ys6S0dkeYqyTISv_rqOel4vTE4gP2wGnpmJBPvu9T3SDL7EDwxpzovud9MbSgfD2PnJUbWnuMOq2OugMmC6U8LCh6twQT0Ix4okUxe2jY19-fiiJNXdgc6X70eOfgijLf8B-2xTZmTdL0mxgiVSSfFFVYRqOIemqBWdV4I5fXPSrCuxt9yaH3mD5UpikUvshT7VbtEYquoNgJh0xSnaaFJy_I4mDNlS9Tusty6YnV-w1haCIyq5cP275bv-mHXWpeEDyqWQFSDau5LUqTQJKGe8uoTsqclJzAodrTyujaxdcGW8tZh0lY9vjNo3St9Bz35OAFfHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سپاه پاسداران از «توقف عملیات» علیه اسرائیل خبر داد
♦️
قرارگاه مرکزی خاتم‌الانبیا سپاه پاسداران، روز دوشنبه ۱۸ خرداد ماه با اعلام آنکه نیروهای مسلح جمهوری اسلامی ایران در واکنش به حملات اسرائیل به منطقه ضاحیه و جنوب لبنان «پاسخی دردناک» به این کشور داده‌اند، از «توقف عملیات» نظامی خبر داد.
بر اساس بیانیه قرارگاه خاتم‌الانبیا، پرتاب موشک به اسرائیل «در راستای حمایت از مردم مظلوم لبنان» توصیف شده است.
در این بیانیه آمده است که این پاسخ برای اسرائیل و حامیانش باید «درس عبرت» باشد.
قرارگاه خاتم‌الانبیا همچنین اعلام کرد «توقف عملیات نیروهای مسلح» در دستور کار قرار گرفته است.
با این حال، در این بیانیه هشدار داده شده که در صورت ادامه حملات و اقدامات اسرائیل، به‌ویژه در جنوب لبنان، جمهوری اسلامی ایران «اقدامات بسیار شدیدتر و کوبنده‌تر از قبل» انجام خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76059" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76057">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u3hRruqTgnk9KVaBKoZX1sqDkNR9T7zTZ0MuObaGPRhooi_lLMkk6Ficdvd1PcBvPuAkBVbzklCmWbOPh9zv0R0WB_AKbSucOiDoFC29Tfdrcec5_XCtHP7nq_zsBSTHJaLyVFxP1b9B8U--GV7kEJ6zkT1zjFnpNQNZFpCvtc7rvmiXjvKYKfjaRlFVEKS6lpUyQXO7LhWSWEm53t2jYBhapfzXdm6sAI_PARwSDoMKQqDPwXswmrOT2-MwqSTJcqvld9bHA-Xm0L7p8gRQovIAOESD6GyReeEdvlOdBNygYbIsThQZZIBU91ANZa_c0ZNvAMaQ_PROQ6tHBbRVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qO3dujOpiGLweSgtzZLBB5m3wR5Ca0h3BAWTucMreEAiyE4Ce3ZedOLBAF5OpdJrZvVBj9YOwxy-oNHtZmAZ4kbSx5Q3bGfjSoEAwENh2I7VtDmIun8gjtSxJM2GqxWRSendIKMV162tOhCH22en261N78ze5l3wXWBzUG8dcLSUt0SR1c-8Rz79L_gOCf2uN4xJeADS3BlUGTBe5dYOGzsgqHcpm5jqQ3NX9gQqJvBhV6lP_XR_ba_zaiHs6O2GEr-ZkyVcfeZxpzERr_dqCQubCgRGR0nQIheFwGOsTeprM9dV3zmtXnicFmxyth1Xo3eMeTZfUzNEsHfbsB4nqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «تیراندازی» را متوقف کنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دو طرف، اسرائیل و ایران، به دنبال برقراری فوری آتش‌بس هستند! مذاکرات نهایی درباره «صلح» در جریان است، مگر آنکه نادانی یا حماقت مانع آن شود. محاصره تا زمانی که «توافق نهایی» حاصل شود، همچنان برقرار خواهد ماند و با تمام قدرت و اثر کامل اجرا خواهد شد. امور باید به‌سرعت پیش برود. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76057" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UGZY9JJmLB5IvTBZIQWkI0QoVa8-5tq6phw_OpE4poilx52gABU47eY02GbBmeT5SeSVh395eAE5g6O6lkeOT-dO25DD65tqiZycFRltf6eclGzqMOnfDpsZtfHmsFZ1KjvG6NWNrZfix5EO6bwbYLKtOCSF7JygBbbDFft6NNGo6n28s79EqlS0xNwjjacPia2e8OnLqDVQeMzNkZGcE1HkaAzEzbUi6YPQnmguj3LqblfU8nD_CzuWjv7mE74aG3VuqZy3FKiEPKAiRA7iEk8C2I8U-ewwrGPcuAOnFhPR7ae4Jbrs_Gp9u5byVwpqldl-xTkxDF0WmNk-5f5KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی گزارش داده‌اند که نیروی هوایی اسرائیل همچنان حملات خود را در نقاطی از کشور ادامه می‌دهد.
بر اساس این گزارش‌ها، فرودگاه شیراز در جنوب کشور نیز در میان اهداف حملات اخیر قرار داشته است.
هنوز جزئیات دقیقی درباره میزان خسارت، وضعیت پروازها و تلفات احتمالی منتشر نشده است.
@
VahidHeadline
در خبری دیگر:
خبرگزاری مهر وابسته به سازمان تبلیغات اسلامی نوشته:
"پهپاد متخاصم دشمن آمریکا_صهیونیستی توسط پدافند هوایی در آسمان تهران هدف قرار گرفت و منهدم شد./ مهر"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/76056" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT7P8V3sYARYfsHGIXcpawuF8kstLRj6I3x4YDwg1kmNseYD8s-yBVk64f0nHMsJUmpBNShlg00hlRQFrJaV8-zKMUby-vatEJJYWMVfGaX8QxuCss1abgaTxpOHaMNaaOZqE0IDcb3H8eadyFTk0-cN1KZS_cp_ZKMOSw8X7tfmXHxhmXVuk829BTvP_XqdXHo0ceuxcf0iO59qwlJ_FhYPJU2LfL6wWol2RYr6wZv-5xbyp3r6rcGUMPBMJyQK-Iu2W47ZNcBCR70N0PnNVWzHkJjs9AJ9PcGus0OaJvpfMUwTUcfzeuSa_w3KhLuFjfsPdo-TUPFcXset0Hq0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای گفت در پاسخ به حمله اسرائیل به صنایع پتروشیمی ایران به صنایع پتروشیمی حیفا حمله موشکی کرده است.
بنابر این بیانیه، هدف قرار دادن اهداف غیرنظامی و تاسیسات نفتی «بازی خطرناکی» است که زیرساخت‌های انرژِی منطقه را تهدید می‌کند.
پتروشیمی کارون ماهشهر که در بیانیه سپاه نامش برده نشد، تاسیساتی است که هدف حمله اسرائیل قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/76055" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پیام‌های دریافتی:
‌
وحید تهران صدای مهیب وحشتناک
ساعات 11:33 دقیقه جنوب تهرانسر صدای انفجار اومد
سلام ساعت ۱۱:۳۰ رباط کریم صدای انفجار
تهران صدا و موج شدید انفجار ۱۱:۳۲
همین الان صدای تک انفجار غرب تهران
زدن تهران صدا واضح انفجار
ساعت ۱۱:۳۳: صدای یک انفجار شنیده شد - تهران آزادی
صداش خیلی زیاد نبود حوالی غرب باید باشه احتمالا
اسلامشهر صدای انفجار ساعت ۱۱:۳۲
تهران الان صدای انفجار اومد
تهران غرب ۱۱:۳۳ تک انفجار بزرگ
سلام وحید جان.۱۱:۳۳ تهران صدا انفجار اومد.من غربم صدا دور بود ازم
۱۱:۳۳ دقیقه صدای انفجار ملارد فکر کنم زدن
ما سمت مهرآبادیم ساعت ۱۱:۳۲ صدای انفجار اومد
صدای انفجار در اسلامشهر ساعت ۱۱:۳۴
وحید ما غربیم 11.33 صدا انفجار امد
یه صدای تک انفجاری اومد الان انگار سمت یافت اباد
بهشت‌زهرام. از نزدیک اینجا صدای انفجار اومد. ساعت یازده‌و‌سی‌و‌دو.
همین الان اسلامشهر تهران ۲ تا صدای انفجار
سلام وحید جان، صدای انفجار در فردیس
غزب تهران سمت پونک همین الان صدای انفجار
تهران اطراف اتوبان نواب صدای انفجار
شهرک غرب
صدای مهیب انفجار از دور اومد
وحید قلعه حسن خان دو تا صدا انفجار قوی
سلام باقرشهر کهریزیک صدای انفجار 11:33
وحید داداش سمت دریاچه ۳ تا انفجار ولی دور بود
11:32
گرمدره صدای بمی داشت تک صدا بود ولی دلم یجوری شد
سلام وحید جان من سمت مهرشهر هستم ساعت 11:31
صدای انفجار خیلی وحشتناکی اومد
از شرق کرج یا غرب تهران
ساعت ۱۱:۳۳ سمت ملارد صدای انفجار وحشتناک اومد
سلام ۱۱:۳۳ صدای انفجار اومد از جنوب تهران از دور بود
تهران سمت شریعتی ساعت۱۱:۳۲ صدای خیلی دور انفجار اومد
از ملارد ساعت ۱۱:۳۳ یدونه صدا اومد
وحید اسلامشهر دوتا صدای خیلی وحشتناک اومد
ساعت ۱۱:۳۴ اسلامشهر ۲ انفجار با فاصله یک دقیقه
ما سمت چهارراه ولیعصریم دقیقا ۱۱:۳۳ دای انفجار از دور اومد
سلام ما عظیمیه کرج ساعت 11:33 صدا شنیدیم، دور بود
سلام من نزدیک مهرآبادم یدونه صدا اومد بنظرم بلند بود اما خیلی نزدیک نبود
بازم هم مهرشهر کرج صدای یک انفجار
ساعت ۱۱:۳۵
درود گلشهر صدای انفجار اومد همین حالا
ما تو یافت ابادیم صدایی که اومد نسبتا دور بود ولی خیلی مهیب بود
سلام وحید جان من سمت شمال تهرانم ۱۱:۳۳ دقیقه صدای انفجار دور ولی سنگین اومد
آپدیت:
پیام‌های زیادی درباره فعالیت پدافند در مناطق مختلف تهران دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/76054" target="_blank">📅 11:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qaA0y1OZssQ4qWQDu2YsTf1r2CuqZE1rkZXJ6D_CZrFbIyZ-WRuRR638NVCQzQBD8-YYxUviSpGcTGo4J0VIgHLkxF6KvupZTZ9AP7G1Yq_W1mb_T3CzEdJzZZHC0R8OjAg1H9Kxbmbvm6YMZtLYzNFAUwHgrRTbWP8u-2w81ZwlWxHGZzw6bOIhQGUDEGuvWl62lNqB5As_u4cMuTsHrbnoCpJZF-xx3FgjvnaUcag8cO93i2CSCGH4yIov949_VNq5qzCCaXcAzEM-_rRKY55atdMogLsx-AUfi8-O0sd9fQQgyS0TCEzGPSRUUdMflViKueZaWgXr-hqqOHZSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ایلان ماسک: "تنگه هرمز به نام اهورا مزدا از آیین زرتشت نامگذاری شده است."
elonmusk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/76053" target="_blank">📅 11:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exzVUZ27j-yKSUwABXgtcmjTt2uu_Q6vSU9cOLdZXRJ5JJf1QqekGxxa8a3WxYP8NfnekF2gdRj9PJc2tr3ewXsVhN48Dk4O_RomhMrpf9iacqj80cCCkROKteYrOTbO-VS2ylh2RbTVKWAsN4njkTSIG5ce4GnsPHsAIpTqo1z9UlPrpwC6Fc8S_NMj8q9jAgvg9KpTrq7pDwgGVdbhaBwPXTpCQrAnygKknXpM7rXlpqwF0Trm-TXaEPOsJD4_d1E8kOK24m4MxHmT47EqjayBr_m79-xY0F9uhnWcqSyRhUKniBX6_HO0GRkDu1qhb-Kq3HkesJ-dJcmFbeO4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نخستین کنفرانس خبری خود پس از آغاز حملات ایران به اسراییل گفت که اتفاقات ساعات‌ گذشته، به بی‌اعتمادی موجود میان تهران و واشنگتن دامن خواهد زد.
بقایی در نشست خبری خود گفت تبادل پیام میان ایران و آمریکا تاکنون در فضایی لبریز از بی‌اعتمادی انجام شده و به گفته او، آتش‌بس نیز «به طور مستمر و مکرر» از سوی طرف مقابل نقض شده است. او تاکید کرد جمهوری اسلامی هر زمان که لازم بداند برای دفاع از «امنیت کشور» اقدام خواهد کرد.
سخنگوی وزارت امور خارجه همچنین آمریکا را مسوول تحولات اخیر منطقه دانست و گفت اسراییل بدون هماهنگی با واشنگتن اقدامی انجام نمی‌دهد.
به گفته او، وزارت خارجه آمریکا حمایت از اسراییل را دلیل اصلی جنگ علیه ایران دانسته و جمهوری اسلامی از همکاری و هماهنگی کامل فرماندهی مرکزی ارتش آمریکا، سنتکام، با اسراییل در حوزه‌های دفاعی و تهاجمی اطلاع دارد.
بقایی با اشاره به تفاهم آتش‌بس ۱۹ فروردین، آمریکا را مسوول هرگونه نقض آن دانست و گفت پیامدهای تشدید تنش در منطقه متوجه واشنگتن خواهد بود.
او همچنین از «رافائل گروسی»، مدیرکل آژانس بین‌المللی انرژی اتمی، انتقاد کرد و گفت در صورت تصویب قطعنامه‌ای علیه ایران در شورای حکام آژانس، تهران «پاسخ مناسب» خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76052" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/025351cf82.mp4?token=HJqFyrQpcIeRYe-YwLctnHGYgs2M7BcYUUG--OFxwBdkShiEP4xbg-yPn5JcVHlH0okG35eEXjddYjdshelf_ICUHfREvnSYE2xbr53nam4oCJFNAKjdg3klE8nqLz1xFxl8QBTWnp9lcpTYC-papqXK4Pal8fnQt777v3TB1-eo5EDyLcJM6U_A9WQgE86ZSQh5fAuUNVRiASFNqJJkMOEJruHnNSnz3HWrww4ubFfmP2e9SQ_CsNCrWU3lWgn4Ap2EyZ0oyxM6Wha2UiAE_6HkiKUwLXCLUBz45DAmG5U4H0GpAa7Zpb-dJPmuQKiSt0PoPezrtr8blHgWt-t-sw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/025351cf82.mp4?token=HJqFyrQpcIeRYe-YwLctnHGYgs2M7BcYUUG--OFxwBdkShiEP4xbg-yPn5JcVHlH0okG35eEXjddYjdshelf_ICUHfREvnSYE2xbr53nam4oCJFNAKjdg3klE8nqLz1xFxl8QBTWnp9lcpTYC-papqXK4Pal8fnQt777v3TB1-eo5EDyLcJM6U_A9WQgE86ZSQh5fAuUNVRiASFNqJJkMOEJruHnNSnz3HWrww4ubFfmP2e9SQ_CsNCrWU3lWgn4Ap2EyZ0oyxM6Wha2UiAE_6HkiKUwLXCLUBz45DAmG5U4H0GpAa7Zpb-dJPmuQKiSt0PoPezrtr8blHgWt-t-sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت ارتش اسرائیل با انتشار ویدیوی بالا نوشت: "در دوره اخیر، سامانه‌های پدافندی در چندین منطقه مختلف در ایران مستقر شده بودند، ... این حمله منجر به انهدام این سامانه‌ها شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76051" target="_blank">📅 11:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiEajPXiKMih9L3ScGpLQ6_8IS3yu75yyLVUeTqJz2rIkOIbGcX69Pbv-x-j52N82oGMsiudAqP8DamA2YUB__2wzE37MOOtDrJ4XmKRYPRJ4x2yf3_hvcLmSFvdm2XoDunZyj72BbCVsv9No0j6Hl5qHVK0m1TVcoVOHwS6am--0QIzwQZl6piQtrL2Vo8q0N0CUEKWNBSOxEQ011lsNLaguD5PnO_anzAI0xTfPXaQbqRQI8mxGJplPz46TpKYzJnMI8lHGYLKO2Yapmynk6b6kHCkEtHEmE2X6OpymhGXtlfy-zxNdFLkAPEd4BLDzzxDos6zPqN1GWCfCdzO8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه قطر اعلام کرد «محمد بن عبدالرحمن آل ثانی»، نخست وزیر و وزیر امور خارجه این کشور، در تماس تلفنی با «عباس عراقچی»، وزیر امور خارجه جمهوری اسلامی، درباره تلاش‌های میانجیگرانه میان ایالات متحده و ایران و همچنین تحولات لبنان گفت‌وگو کرده است.
بر اساس بیانیه وزارت امور خارجه قطر، نخست وزیر این کشور در این تماس بر حمایت دوحه از تلاش‌ها برای مهار تنش‌ها و دستیابی به توافقی جامع که به تقویت امنیت و صلح در منطقه کمک کند، تاکید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76050" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dew4RyEW4vXEKHu6Gu2wDAFyW221SXNuZyCf0PIsdcBNsH9ipZzcYGuRwS4jAwKkXM2QBVKAtbh28xGOT_YO0YoXjh5xHFez6ebp-r5KoRQ26DM6OMbsyW1Izg4vJyJWPmTGm-7P6vEHXA2xO1bMXRpLcR6BfafKnFYWlIOpQIQvHO8pQlViZYopzuhVpkkwi3fHUigBxgVNFIto40bR78g9DeUEUbS5MzH5VD9h2aJhnGzWKnntLLpwKCDw29GvyFib71JvgagU2B_gKoVEzqGzzy0QsyquaYORWXjPR7_lq7qk4ED3n_MCVK6s7nCKaFIyiSa2ki2Ol4yf62MMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PO9MfzBqsIbgyy5ZspWZDALiH9TLUA700HXkIMyVi1ocavBRSBDmKv2KLBapt__sQy-RvAAWi-8w0N_AzLiTD3olzuScqM3HL91gaSBgEIfeXRIW_0LdujWk8hD3Ywv-PexCh9BGjB9d6HNoHfkIXEdvpgQ7g4I40ud47liyxJwIPpXRoPI4qGM6dlWj-kFB295MP7AabIuORBSfR2JhorXDMx0N9ACtIFaa87LLetENFnkwuYQO8tcQH1HWkXh2JAWH_JkCpSQ3Bd8t8_JeAJhGYEQtygWdudK2rGaaY59u8p-IO2dVmYvc4SCwaAaUKek4MyKfs35k4xbH7Fnl_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HIvTlHixRGR8LQ1v8RORiB4mjGogvr7GmgtPtSJCllxZeyMssntkTvOwk4NRrlClnW0G2JzUiFaw351lF7ERAUuB1Jdud2eCP0VqJwPqVdhoijBsW7oYwpEkvImP1agnqtDjDchmjmKfagUfsyljPffbvFldm58bGBBWW3e6aDYQpGmtZ4OEf2goH458c8Xp80upqANipq49CGkQdI_j6NaY9h-_WtmxiUGg49OIHWzrcVjF_Oqvs0iy74tWoOmGbjbM4_WxQNBTBKSRR8JJIqpyyDjiMJ32LIcyd8niKESD-86YXWokUAPYJw7VjiHtYThGGaAN_eo27-tEtFeqVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=ZxSvpoLhxzqOa2JpgV52lTkOC_BJmA82tbqsY1z6IWrlEbwrSkEbZgmZ0rEXhcJwVwVG63V4FdjfrlWQSTMefghLWly-3py-IW_teoGX65AfNDLHi-JJjNJA7RuA2r1JS5KF687KHrMWl7JghblrMVmHYCWF9LW9M5xyw_t2DmTIp8FTebwyoCXHoWXPWiTQw5DFkVkclbklao7nlyaQ4TiJEUjqpWeLR62dbNB2KY2rKKVOuDjFsl-tfZX3sNlRrpFXHUv1reRiy-ajWr69_uUc5bPv6TGUZzVJ5memLNYT7oqA07OLSEgutsKMY45bZwym4R3MMBm4qtBLJbH71g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=ZxSvpoLhxzqOa2JpgV52lTkOC_BJmA82tbqsY1z6IWrlEbwrSkEbZgmZ0rEXhcJwVwVG63V4FdjfrlWQSTMefghLWly-3py-IW_teoGX65AfNDLHi-JJjNJA7RuA2r1JS5KF687KHrMWl7JghblrMVmHYCWF9LW9M5xyw_t2DmTIp8FTebwyoCXHoWXPWiTQw5DFkVkclbklao7nlyaQ4TiJEUjqpWeLR62dbNB2KY2rKKVOuDjFsl-tfZX3sNlRrpFXHUv1reRiy-ajWr69_uUc5bPv6TGUZzVJ5memLNYT7oqA07OLSEgutsKMY45bZwym4R3MMBm4qtBLJbH71g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
ما کاشان هستیم
اینجا قشنگ صدای موشک رو حس کردیم که داره رد می‌شه
همین الان ساعت ۱۰ و ۱ دقیقه.
از خمین همین الان موشک زدن
شلیک موشک از ابهر ساعت ۱۰
خمین ۹.۵۷
وحید طرفای ابهر خرمدره ازناب زنجان موشک زدن ساعت ۱۰.۰۲
سلام شلیک موشک از استان مرکزی
وحید جان سلام ساعت ۹.۵۸ دقیقه یه موشک از ابهر زدن
سلام از کاشان هم همین الان موشک زدن
شلیک موشک از زنجان ده صبح
سلام از خوانسار صدای موشک اومد، رد موشک هم توی آسمون هست.
همین الان از زنجان دو تا موشک بلند شد
هم‌زمان پست ارتش اسرائیل:
ارتش اسرائیل شناسایی کرده است که مدتی پیش موشک‌هایی از ایران به سمت حریم کشور اسرائیل شلیک شده‌اند.
سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76046" target="_blank">📅 10:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76045">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=kUyhL-dSLd0ng5g_qQdvjw0h9xbRdpPu9p5-bguUhyN6OXfbqLVETkU0Gmo75RFr8Q3ccQDznuxFEdMncH4fcJUzSLNfqwRybTGrLQYwBi2hry_SQ-leX6A4iP6nT02F_GJfiMKtlgPeII_Dvac6_I9R6XMREW4oh-XHnk65qLV9cE8P87rpjtIn6Z0AVsuXOaM6pi4yzW2kRxy_7iX33uBQLmT710uOmcaw1eMfaO96yHKUcV5RMy7wYSFngyE8uJObHcIuRuQj_ymlP1K3m5TpxIZlNkJwacTKUMis-6RbdaoJysMGdF_h3STXIltQwETeeaAVbRpl8-H4TKLNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=kUyhL-dSLd0ng5g_qQdvjw0h9xbRdpPu9p5-bguUhyN6OXfbqLVETkU0Gmo75RFr8Q3ccQDznuxFEdMncH4fcJUzSLNfqwRybTGrLQYwBi2hry_SQ-leX6A4iP6nT02F_GJfiMKtlgPeII_Dvac6_I9R6XMREW4oh-XHnk65qLV9cE8P87rpjtIn6Z0AVsuXOaM6pi4yzW2kRxy_7iX33uBQLmT710uOmcaw1eMfaO96yHKUcV5RMy7wYSFngyE8uJObHcIuRuQj_ymlP1K3m5TpxIZlNkJwacTKUMis-6RbdaoJysMGdF_h3STXIltQwETeeaAVbRpl8-H4TKLNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اعلام خبر حمله موشکی به اسرائیل در تجمع هواداران گروه‌های مسلح شیعه در تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/76045" target="_blank">📅 09:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIiVYqYaS7EvD3FvJuj89-FeZydriki6wUdoa0NV5o-B0E1ayo6KdvMoD66hOHbh9Iw9T3xWtnzw_dr9OaU_OfPje4GL1lzBDGaMjv-JvbowjD0_1dCZj19JEqUE-5Pjs2hJKrPbCoRr_oqxqZYZqzhzG97OpXIKCRPz3gWbTQegKuKXazz3pmfcbA2BRpRpkQVY65Lh0uSEO8NMRNF495jTC2dAxWGqxQ_vSeWMPMt7bGFHJD7ZqLy-lpQKBVo4rXkWOjQC1r3nhl35YNDpGevX5Yne-L5gROeg08jrwuza52B29fvtmlpSJ54KIVXt0u-TtBCALtHQ3nVDXQDpDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که تمامی موشک‌های پرتاب‌شده از سوی جمهوری اسلامی در صبح دوشنبه به سوی اسرائیل رهگیری شدند.
ارتش اسرائیل افزود که پرتابه‌ای که به یک زمین باز در کرانه باختری اصابت کرد، احتمالاً یک قطعه بزرگ باقی‌مانده پس از عملیات رهگیری بوده است.
در همین حال، پس از آنکه هشدار اولیه در اورشلیم درباره حمله موشکی جمهوری اسلامی صادر شده بود، برای این منطقه وضعیت پایان هشدار اعلام شد، زیرا موشک جمهوری اسلامی موفق به رسیدن به خاک اسرائیل نشد.
@
VahidHeadline
به گفته نیروهای امدادی اسرائیل، اصابت یک قطعه از موشک‌های شلیک شده از ایران، به چند خانه در یکی از شهرک‌های کرانه باختری آسیب وارد کرد.
در این حادثه مجروحیت گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/76044" target="_blank">📅 09:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=hGwQs6XfTPJDkZEfugeFc4OI_JW1B83dQogZm1uX-tgYA3iPaeWsGlneV--toXQydWX8uZZ3z76mTYYsgnER5NujBuGnaJPCOoPBihgBHeNKQwW9Udr_ibaGKvmX9DSpkc1lCJKktvZuHn6hyXyQQflg-goTWbtdm_goq8Zt38DUOt4zIsatnS52goh9kKQk6D-LP3ENxyVBwdJYIh1YLMwwYaxqwm8UJadaAF5a_C3jlCf12DGjzxAuTY_FLJJS_PI35SUqozd-bGFuQ7I_h8v_PwPFrs47qma3OVlyzard5eseBcyFQwNPcOfnsXphhmR2DKp3975NnbhGm3Fd-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=hGwQs6XfTPJDkZEfugeFc4OI_JW1B83dQogZm1uX-tgYA3iPaeWsGlneV--toXQydWX8uZZ3z76mTYYsgnER5NujBuGnaJPCOoPBihgBHeNKQwW9Udr_ibaGKvmX9DSpkc1lCJKktvZuHn6hyXyQQflg-goTWbtdm_goq8Zt38DUOt4zIsatnS52goh9kKQk6D-LP3ENxyVBwdJYIh1YLMwwYaxqwm8UJadaAF5a_C3jlCf12DGjzxAuTY_FLJJS_PI35SUqozd-bGFuQ7I_h8v_PwPFrs47qma3OVlyzard5eseBcyFQwNPcOfnsXphhmR2DKp3975NnbhGm3Fd-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@
iliaen
ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد
به دنبال گزارش خبرگزاری فارس مبنی بر حمله به مجموعه پتروشیمی کارون در ماهشهر که خساراتی به دنبال داشته، ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد و گفت به اهداف متعددی در مجموعه پتروشیمی ماهشهر حمله کرده و جزئیات مربوط به این حمله را به زودی ارایه خواهد داد.
ارتش اسرائیل پیش‌تر گفته بود که مواضع حکومت ایران را در غرب و مرکز ایران هدف گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/76043" target="_blank">📅 08:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=tJGWWQmp7sdGGnJ1LUWICyyd7tM_MahSUt0XoFUCWS5_qXfy5yCHp7RvJGf7l4MHT9vsKPOMzUeMe1gBj2CeW-9jv4xCq2v3iqLUya3hKBMsUKNYVPAevjN6_35HJsv44aphBo5EF41GJAu1dyFMSqDyLg7zrR370QsNT9zsjxCu492yjC7fNSEgQ2VZhVe93cZb3s2kewU0qa2ZaCANcNvJthlYZIbpwRuXuPS5QwxJfx53U6o6CcoHDcE9WPu6tbsAwv39QrUMUz5N8TQE-3n__gkFAhZ0P_wQwJZWdn-IT9gs2o0XtkeR5kk7QALrAsZVAV7G8XsYKcBb-Aj5RA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=tJGWWQmp7sdGGnJ1LUWICyyd7tM_MahSUt0XoFUCWS5_qXfy5yCHp7RvJGf7l4MHT9vsKPOMzUeMe1gBj2CeW-9jv4xCq2v3iqLUya3hKBMsUKNYVPAevjN6_35HJsv44aphBo5EF41GJAu1dyFMSqDyLg7zrR370QsNT9zsjxCu492yjC7fNSEgQ2VZhVe93cZb3s2kewU0qa2ZaCANcNvJthlYZIbpwRuXuPS5QwxJfx53U6o6CcoHDcE9WPu6tbsAwv39QrUMUz5N8TQE-3n__gkFAhZ0P_wQwJZWdn-IT9gs2o0XtkeR5kk7QALrAsZVAV7G8XsYKcBb-Aj5RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابت موشک به شهرک یهودی‌نشین ایتامار نزدیک شهر نابلوس و در بخش شمالی کرانه باختری رود اردن
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/76042" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjBeE-MHvT238-momXhDYAAeOL6pKZeySKT1GWmM2sVYo6orrJJ9k2h_HfID2CnoYuiuyTaTJWE2AkfhsdkKILC6qCfcWIJm4_-pKCZoJ4OEHk1tTf8ofgX7sN5vES5z8wC8dTNV-_uBuOf5ApLNvt-Mh6tb2TyT33AQTxCy0xA5IpasLplDIZeOBpn2X-0TQxm-fla9Lti37e9pFlidVoy35jV9PHI4eM8-OwvGUs_w85XqB369ASUB9qDnce6Q4QCHNV6m8mBF5to22OF6zROUTVMhqtNE6RTR_FEGylLH3ivyD2B6cZRP6lqO8srNwAY_cY6SZfmsrDYOxL8M_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بامداد دوشنبه از رصد موشک‌های پرتاب شده از سوی ایران به سمت اسرائیل خبر داد و اعلام کرد: سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/76041" target="_blank">📅 08:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76040">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پیام‌های دریافتی در پی گزارش‌ها از شنیده شدن صدای انفجار در ماهشهر:
وحید پتروشیمی کارون تو ماهشهر زدن
آقا وحید سلام پتروشیمی کارون منطقه ویژه ماهشهر زدن دستور دادن کارگران و پرسنل برگردن خونه هاشون
سلام ماهشهر پتروشیمی کارون ساعت ۷:۳۰ یک انفجار رخ داد
وحید جان منطقه ویژه ماهشهر صدای وحشتناکی اومد. میگن شرکت کارون رو زده
آپدیت:
پیام دریافتی: کانال ماهشهر هم اعلام کرد
پتروشیمی کارون رو زده
اما صدای انفجار مثل انفجارهای قبل نبود
همه نشنیدن
معلوم نیست با چی زده این بار
🔄
آپدیت:
خبرگزاری فارس، نزدیک به سپاه: " تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
حیاتی، معاون امنیتی و انتظامی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
خبر تکمیلی در خصوص خسارات و تلفات احتمالی متعاقبا اعلام خواهد شد."
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76040" target="_blank">📅 07:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76030">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jYN2b_Ab7WUnNuUbIti7K3_gFr9mR8L8kH2kHBepliMycCUZLtzzAQG98WXFpMfWY5V_9yNCJ3GDIu3BWpKjC1t48J6TMG49-Tuyr9uK_FVCNkielw4rf_Pjw0IkJ5Dgnt2I_qC-ggb8jpzmg7IGaP5gEd4qLC35TWgp3rdwRTXVtI7W_WBVU39k2AEXAY9hTd3yLX4P6bY8HdzrVP5JLiK5s2f9eDZ7O0IyyrvfoY1rgRyEeT8vFPcOxSIPS6IdaghRqlkgvXTZnRwpfqt9s5JMeotnbjQOrO2aiCAkjn3rsOxMs1DuCkQQ9yMQ-zZg1K6xIAGSruJoR6Hny474iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pqre4c6ZhRCaPP4KnaeN237ztui8OOkQ2lxrIPRggke1Hrxp2tV4bQalJaqbOKlRiz6iL3KYxAOrJehhI0L_dX6Ar18rFwcyjh24mqDl1ZlRGbDQaguFA3UNfCPNhx5e2acecWT-IDiUby931fP2whwuYhRf1cFmmvyB7tpzoLhCckeNV4BtzcAjifRB1kvijOD8cDSit0ZhVx2uprWSpaT8SPD653k_Q2OOD8Z2w70sfxxr-PrquExilkyLWvP1NJ3yP7Je7YOnTMfekHhZaC-k2tw68YybDePDJ4B6S8ggj2MwgRgkVq3_1VEubta4fGLHOj6w-Vl-G2lg6p6PQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p4iVb-FZLeny_D4hk0_6k28bRqZDWkG9khcL__OUtFi-Nxm2-Qi1sZ07gAe1cOCGX7LXJFNHwotOqWB3XxXVfc5r12dYFmJsXgnHOkBP5ALmLSEeyU9dtc9mucTATxYg1b-mATCfu0Sdhn0hS6EkrmNsyOm2ris-f67C3lvluCJvsLNo7qzFR1LP_4kEPpz5Q7Bp52FpCiN_2Hnl_WPa4Eupz4WVXq0zPwbRR6sWQ1ofoayss_suMzY3pnnGSPUz6LBBOR7OS8d61JR45blOCfexHCMpkLWoyi60yJZr94hoY-7oPjcgfE14JsmDrAz4yLNOLUiz4kSjZcMeTOP04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RR-Ek3qCGMyybV9vG_ZGWCqWTvN77M0EqjVmnruZ7aODd6Qc-eAwwZG8sJArjSqvYNAmjEiJGoWZUojPKeNFvKZk37xYtZQ3IFc7kNqSekHnuk8l5RdUOqghd-5fpf-yCSzYgLgRqjqbe5ehwzIvdU2LRgN7oKPDorSJHAWQdJEi2x2CqjUvkbaxtrfzr4sHXqV_LzhkduCM6yYMNLpCqaOX4lmgtDJwA44uNOWm2kzUqlaFzA298ytwQcVoW1c6_3jrT1oxu0Pt4p378gllmql1amQRNu-SVEOK3DeETsaJ96pgKb69BH5OVe87m-Buuy4m83kfIFWGNOKF9ED1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ee7Vyn5HCFEjelsxdk5OI6qlmchrc1q4Xx-W_LosZijp1IhIhSyLotAfmNzxSTL6IOClg_qnh5h1HlxJS5NCyii2VRSAacH0Hq8DIntd29xgZHbIJfUaJ-exZ9JNz13kbbgiur3BmnO0hL7C7eBo1BoQAEpd241M5xAh9g1PoH7l46Y_4Em8ukqFOovg-5unVav8eYtXQfB7nvNg40gs_p7JsBIaAZGnCf2hOnx7XwMbjLni7Mri8xCcsgioSpG2z3JZeSSpdE3lvZycLi7p0QvnjGeDYFJ3UpZfKDXuROx3Faow00RIA5Z3pWQCfUN5Ngqf6hN1Ke1FHXqkQ_LS9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=JoPhe7QlrSbKbBIzkzp2T1m1rC5vho5zwVAM_neZVKj3Ggc7PteASaRd3IYFEqIVVmBXSpulI0Fq9w9-Kc0DyBGY4GwZnLywJWSOf-RSi_u7Nej5thvx973LIePUTvrTtNId2QWbux9vHmcSEf3v8ZLTWbypogFfgWFCkLDxUHMwPLQOjEqpRRv8xuVjjBnRnSPxHUnjpnYs2vUCJ6PmUEs6_MfTRWNNh-ExQAXhTtMR1NUZUsQS8VWzn38jlV_pYm6sbaM4HWaIAX_WV_zAg9Jf4R9XPFfVMypQJdSYVZALJ4FtpCi-UOE9Sa3dYD4JRq32PG_2Vz7sBykoyNgsvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=JoPhe7QlrSbKbBIzkzp2T1m1rC5vho5zwVAM_neZVKj3Ggc7PteASaRd3IYFEqIVVmBXSpulI0Fq9w9-Kc0DyBGY4GwZnLywJWSOf-RSi_u7Nej5thvx973LIePUTvrTtNId2QWbux9vHmcSEf3v8ZLTWbypogFfgWFCkLDxUHMwPLQOjEqpRRv8xuVjjBnRnSPxHUnjpnYs2vUCJ6PmUEs6_MfTRWNNh-ExQAXhTtMR1NUZUsQS8VWzn38jlV_pYm6sbaM4HWaIAX_WV_zAg9Jf4R9XPFfVMypQJdSYVZALJ4FtpCi-UOE9Sa3dYD4JRq32PG_2Vz7sBykoyNgsvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
۷:۴۰ پرتاب موشک از بیدگنه
بیدگنه شلیک موشک بالستیک همین الان
همین الان ۷:۴۰ موشک از بیدگنه رفت
دوباره از ویلاشهر نجف‌آباد موشک زدن
وحید جان همین الان از کرج موشک پرتاپ کردن
7:39 دقیقه از ملارد صدای پرتاب موشک
یکی دیگه همین الان اصفهان
شمال اصفهان یدونه موشک دو دقیقه پیش پرتاب شد
الان دوباره موشک زدن ٧/٤٢
اینجا،اصفهان یک بار ساعت ۷:۳۰ دقیقه یک بار هم الان،۷:۴۰ موشک پرتاب کردند.
۷:۴۰ از سمت ملارد انگار یک موشک زدن.
وحید همین الان از جهانشهر کرج صدای پرتاب موشک میاد خیلی صداش شدیده.
سلام وحید 7:40 صدایی شبیه به برخواستن موشک از نزدیکی مهرشهر کرج
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76030" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j0q0GgUM5zSSgnsvF4PRrvrZpY9q3L7yCi3puTpgRYqaotBeS3KjJbl0Rvfy8tRQsCrMkHxkOkIKyyldF_fPMNOI0Nr-tsN4PbIPlzFzcfo9N4BWR6gcuu95K6wcK8vmnqC2CXGHT3yJUhbLAlK0Vsx9yk_vXhDoZQO3ucVTHAlnLdOJ5GJXUdihX6n0iWcfHe48pr_j-H3Qc2Oo_5kipQJo91Op9qrcr__KQ9gxr22Xf5bB7hsEVEnX8rJTiivB9ZNVScylFGdNpQN1-cxnwJhAT0NfzRAhIITF7MVfEliCtFafz94W8dxijytkCINc2YDiBX_OU2nFNqmrgNf2Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
۳تا موشک از کرمانشاه همین الان
وحید کرمانشاه همین الان صدای وحشتناک اومد
سلام ۷.۳۰ صدای انفجار از کرمانشاه . احتمالا پرتاب موشک
سلام وحید جان
7:28 بندرماهشهر صدای انفجار اومد
وحید 7:30 دقیقه ارومیه یه صدای سنگین اومد
الان ۷:۳۱ از ویلاشهر نجف‌آباد موشک زدن
الان کرمانشاه صدای انفجار شدید
شلیک موشک از ارومیه
خرم آباد 2 تا موشک از پایگاه امام علی انداختن
از ارومیه موشک فرستادن
پرتاب موشک از نجف آباد
اصفهان شلیک موشک
سلام وحید جان از خمینی شهر یکی زدن
آقا وحید همین الان شلیک موشک از فلاورجان اصفهان
شلیک موشک از ارومیه
با صدای انفجار زیاد
سلام وحید آنلاین همین الان ساعت ٧/٣٠ از اصفهان موشک زدن
سلام وحید جان همین الان موشک زدن سمت اسرائیل از اصفهان
موشک الان زدن از پادگان پشت ویلاشهر نجف آباد
سلام ماهشهر ۷:۲۶ دقیقه صدای یک انفجار شدید اومد
از کرمانشاه ۴ شلیک، نه ۳ تا
ماهشهر حدود ۷:۳۰ صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76029" target="_blank">📅 07:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGiT7yKVtymnp78KAKys5cEOJHgqpq2d8CWxyYrnUW6kETB9DYg3xojQPmKmtbYJWSCtaabg8ieZOLrwpbSLSbAsO_q6M1aovwUYThg7J7zwvVCv50IBqvHB1-4v9Ol5cD5KXu_ZAOWaMdpeAX02xjWr4EPrXPGG5z1V1ObrzX7B7jXKxqALvZGuLCkbskf2xNMUvoOmUOCTinMN-MPGXtRh610oApygcN-M_a7QlNNaShh-hiaBfXIEZFHgh50dL3GaCDYY0F8v4Qxbx0HUSGd8dRGB41w1l7BUNuhTclgHAXgwuOG8dKaBQFJsg2CuxYOSnVtx8w-SUkdWpuMHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی بعد از موج حملات موشکی ایران به شمال اسرائیل، خبرگزاری تسنیم، نزدیک به سپاه پاسداران، در تحلیل و تفسیری درباره ابعاد نظامی این حمله گزارش کرده که در حملات موشکی و پهپادی یکشنبه شب، سپاه پاسداران از «پهپادی ناشناخته» که از موتور جت بهره می‌برد، استفاده کرده است.
کارشناس نظامی تسنیم همچنین از شلیک موشک‌های خیبرشکن با کلاهک‌های خوشه‌ای در جریان این حملات خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76028" target="_blank">📅 07:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsAN1cUIi9b_WjJsTUklyZDPAmXqRafcs89Y4kqn-Az41ugH2HjfCdz2Zoqrythgx-BHkBzl6dtuzOhWFE4LMJGry6ziPz2_RPJ8Tl6NU8lXzUte_ivID81gsrGwuSkc-I-zh5G07GCTAtM17rv2X2GspJQqnrTQltGTz-yyZHorB8OP-C0SURn_z1kWphA-kG6kPrRxoBPj25Gh9COvwjheksiBB6p2EslpT8oUM23Ei0_a7MWVAhLFXyu1nVODNy1oJw8FU7rfMkIhHzylswk-FYZ7yR3HDW2cku1xFI3Zi54AQSxkvs5fwiFDE6oDlsIQhcTC11ir3e_XEfnlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یخیئل لایتر، سفیر اسرائیل در آمریکا، در پیامی در اکس نوشت: ارتش اسرائیل پس از شلیک موشک‌های بالستیک ایران به سمت اسرائیل، سایت‌های پرتاب موشک زمین‌به‌زمین و همچنین زیرساخت‌هایی را که به بخش انرژی مرتبط نبوده‌اند، هدف قرار داده است.
لایتر افزود: «ایران امروز ۱۱ موشک بالستیک به سمت اسرائیل شلیک کرد. هر یک از این موشک‌ها می‌تواند یک محله کامل را با خاک یکسان کند و صدها نفر را بکشد. هیچ کشور دارای عزت‌نفس در جهان چنین حمله‌ای را تحمل نمی‌کند و اسرائیل نیز نخواهد کرد.
سفیر اسرائیل در ادامه نوشت: «مردم لبنان، حزب‌الله به‌عنوان نیروی نیابتی ایران را رد کرده‌اند و به ایران گفته‌اند از کشورشان خارج شود. اگر حزب‌الله به اسرائیل شلیک کند، مراکز فرماندهی آن در ضاحیه به‌شدت هدف قرار خواهند گرفت. این موضوع هیچ ارتباطی با ایران ندارد. همه از این رژیم ایرانیِ دیوانه خسته شده‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76027" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q15SBhto4GGSsFAOj8IWSfOkU8ND1280N5QRz8hXxf_FfH37fusN5O0hrxh2cKaeTIddLnpxdIeS5mkaJGAE9kzzCU5SgNfXOOqyXzGouT4Ic2_LXpo-d4FpVnV6tSwFmFNvhSuwTGDyViraGyMGtyffZf265nrPIS0qbMd0cWkYYVnnRLevoQBp-JNMxgazmzPSeiEcWivHS51S_U8_lMspi6A9DSh7f3VYa83sTjwri5n4keznHC4Ye8CTRl1QlgIdmNOdJNfY94hfbgKb-DwpGRzaz-nvptWvfiH50eiUtS9-eQnbSRqqhXjxqofDVLQQmy_p0j33g2k-bomR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
یک مقام آمریکایی به رسانه‌های این کشور گفته است که ارتش ایالات متحده در حملات شبانه اسرائیل به ایران هیچ نقشی نداشته است.
نشریه آکسیوس به نقل از یک مقام وزارت دفاع آمریکا گزارش داده که این حملات اسرائیل «نسبتا محدود» بوده است.
این گزارش در حالی منتشر می‌شود که دونالد ترامپ، رئیس جمهور آمریکا، پیش از حملات از بنیامین نتانیاهو، نخست‌وزیر اسرائیل، خواسته بود در بحبوحه تلاش‌های دیپلماتیک جاری از اقدام تلافی جویانه علیه ایران خودداری کند.
آکسیوس پیش‌تر گزارش داده بود که آقای نتانیاهو به صورت غیررسمی یا به تعبیر این رسانه «تلویحا موافقت کرده بود» که این درخواست ترامپ را بپذیرد.
حملات شبانه اسرائیل ساعاتی پس از شلیک موشک‌های ایران به شمال اسرائیل انجام شد و در حالی صورت گرفت که واشنگتن همچنان می‌گوید در تلاش برای نهایی کردن توافقی با تهران و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76026" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3X-qz4bKo_QxzvkWH-g-xgxm0yJcvTiSxyHUqAlRdr8cc_5GvpkgDLAgUFQ18otBRazNsqY-bikjY7sT0bFXz2n2O8JOw37D3fmVJEmV_h-nvsm83auPAVLjHq26xiUoxGew2OFnjpLSmN5rHDmYeRR7xv3jNI8zvK4d1pGStRwTQjRCWo4pmmZI4wXdAb-bJhBZ2xkeaxzo5aK6pQl8o8c0Z5-ov3UcpJbrrEFuHiIJYw_mUkiwhKRrKvbWxiU222PRaCYk_BcFFlsvvJFCR_hLUPjk7oY2Gjy4uXRiDEfGcA5lsDAwa-tEj-tbFShDHgak4SR4cBJUebwwq_DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل پس از حمله‌های یکشنبه شب سپاه به شمال اسرائیل و حمله‌های متقابل ارتش اسرائیل به غرب و مرکز ایران در بامداد دوشنبه اعلام کرد که ارتش اسرائیل یک موشک شلیک شده از یمن را رصد کرده و سامانه‌های پدافندی در حال رهگیری آن هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76025" target="_blank">📅 06:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/un8rswjyJa9X0Fy4WKESvau3_MVxWLvyl_gBv1z1fSgJABiwscQnI3prTObjtkSljfUZnaTYbduZ7g3laswNNeVjrCcvgq4kt0s50oHUEQVmJrqGZK9xORGnmmYfmCwXaXbcRyzQDKXAxgkmVKy_4TKLhMmw3lxVGA0psNVBNV2-fxI-0x8_P_gFfync4wjRf9o2Rbi5x4yX9jukVBjMe3NWNYz9Z4jzQM2boJ6rME48kYhrs-VBAVmSgBQmP3J5Mg13l2TuXWcV3qzAREQidRgN7UJyVSWUTdNbOts5gwvZ7UgqnOl3ggnQMHo3zZjZkE-s-c2FBrzAo_O1RpWA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس گزارش داد که عربستان سعودی در منطقه‌ای که پایگاه هوایی شاهزاده سلطان، میزبان نیروهای آمریکایی است، آژیر خطر موشکی به صدا درآورد.
@
VahidHeadline
آپدیت:
خبرگزاری صداوسیما، وابسته به رادیو و تلویزیون جمهوری اسلامی، به نقل از «یک منبع نظامی» اعلام کرد که جمهوری اسلامی هیچ شلیکی به سوی پایگاه هوایی در الخرج در عربستان سعودی انجام نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76024" target="_blank">📅 06:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNnnPwdCugg8o79lJvdmrHCLXg6cNis3HcTxUEU7Ii6RUB1MIQ6HiVJeZAAZtswDH9Hm5Yz2MerB_AskG4vbg6xnTxHlVEBoX7iVyChI9Jj3ltAj5a9jp_HvVCGdEPLOr8OLRoXL3iwT3_z4rZ161d5jvcra9M-4fW_rujz2qHM-YoKSCLyKXNbqMsdc0OuJ6KxklE5FdCiVVv9AUbdvHeVMewkFcxCJChLUc-sA4wwbIADhaZ7XFQiJ80DAhk-YtjyL37fupmMLN4tOazDqBxeyhucnMFBFdMflRDksvN4TuYSA0WYH5zefYO8d53Tnhj5lOLrc4sHbMZPgor7KhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌نشانی تهران اعلام کرد: صبح دوشنبه دست کم صدای ۲ انفجار حوالی ساعت ۴:۴۳ و ۴:۴۵ در نقاط مختلفی از غرب تهران شنیده شد و ادعاهایی درباره هدف قرار گرفتن فرودگاه مهرآباد منتشر شده است. سخنگوی آتش نشانی تهران از آماده باش آتش‌نشانی خبر داد، اما اعلام کرد که نقاط شهری در تهران هدف قرار نگرفته‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76023" target="_blank">📅 05:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76022">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYtD8wNSQXYfaxOiagNNRmw8QNd_F7xr4lnf5bvKqOjxqTvdfW_TaJ5ARgc-XR_WxFWL-PUzAk1nM99dirtX6g7U-XkLwCIAPt93NPsbUzMf_N-oSbXe4XjRC8pMVSlvsxJAhM7z-WU2SGmZF1-r683jm7Y4bPPw-kz4vqK7nlIgx0A2yPpeYAnzKn7AtYU0ZzK6-pT6_2JJdbd355olisJniVaCyNWvJ7Dzams7vjPOcOJ0zh8laQ09ULM6jK2qdOrPTEyjqHS5caFRUCRpN6RwoR3hf6n0RAjpbJfabIV3zsPKmElNQUskByMiksfCe5e-9c4fp2-yjUTLKNb9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک خبرنگار اسرائیلی حوزه دفاعی به نام امیر بوخبوط می‌گوید که نیروی هوایی اسرائیل صبح دوشنبه به ده مکان در ایران حمله کرده است که از جمله سامانه‌های پدافند هوایی و موشک‌های بالستیک در آن‌ها قرار داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76022" target="_blank">📅 05:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76021">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LOXTpADuV0QvDnwaufLqszJVzVaHhSBuVYlX7APU920ibhDxcu-OJSX_4hIs0bqP7cJ6RHWr2FShDFQN8Rv4y9hjX2elUxeGibVdXycgmdp7Jh2Apso_oqhQJPQKpDr1PeJf_zUkjDxIik9RKDp4oRS9qTrh9APbdr1tP5dL8S2q9TeGkrDohouEZWFKsMhGqtFvSPST110cKtwWmVNCHW7pioKTyDnu1Hk1wv9u9v0qlrqokT7IXUYZREv8WvVxLzfb9lFs3NrOi5l0-K-nhmANG4eVxk4jkIOEm2402sbox6eu-3GdkqD9xy67TqLJPTSrwV9aGO_wf_9SqqRkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درپی اعلام حمله هوایی ارتش اسرائیل به نقاطی در غرب و مرکز ایران، سپاه پاسداران انقلاب اسلامی بیانیه‌ای صادر کرد و نوشت که اسرائیل «با استفاده از موشک‌های بالستیک هواپرتاب اقدام به حمله به اهدافی» در خاک ایران کرده است.
ارتش اسرائیل حمله هوایی به مرکز و غرب ایران را اعلام کرده اما هنوز نوع سلاح‌های به‌کاررفته در این حملات را اعلام نکرده است.
خبر این حملات درحالی منتشر می‌شود که یک مقام آمریکایی به اکسیوس گفته بود دونالد ترامپ، رئیس‌جمهور آمریکا، روز یک‌شنبه در تماس تلفنی با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از او خواسته بود فعلاً از حمله تلافی‌جویانه به ایران خودداری کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76021" target="_blank">📅 05:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yh86YCpQDM77ImkFTSVZ7gOuP8gaBP9r2IvKYWTSnudgmfvnU_vu5zufKGcjHXhBi2Zsdyb5l9StEzDxDO6qppOzgMe_zEkPVW6_kaQYhlh5ZskLIR7YGWLNHUw_AEiA5eXppOg0utTP_-YyoR72OXTbyZC6pwbleYfoXIHdF-pQdUqRdVEIi30KBCJx_OAvRf1Xe7J-r0qVsHj_M-KZGFtX4azKtrcIaDRRkktH-JMwEX7qOttI8cLx3DgO-vMisuhABJlNJSlF0kFybkIoWpJ8lb9sZP1VB-ichSHly9RxRz8sKjDVZ7iydDmyPKAI0pumYJR_agFdYm7pcjH0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cnutMO1Y933TRrigMhOiN1fyUJ6OHgCsi_MfZ3hqLc9nhhBhp0teLDIoCJRTNxOZe8_kZdAaj5rfhYODg_BfSSaJoTvOzYi7H3EJgknuKctEYsvKmB8jzJJxVNIjgw2ZZQfpvzmSZINo2K2fMd3RICIXbj7bRdktn8lGw23d72DM940n-RmgyctVPPkGouGAlaySsXqvYi_u0wYxaCE820fvl2h_0WcEzuOyolZ3EeH7aCtBCDV_kBcyJni85WOX2gUg1C2Myo_hWgmktSPQ1U9KkV7Dn0aP6gZ-q1fsPWPxEfSVj4cVJrhPHgFGlGG7MC9gxnyLNAYWXIbaGPV-SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کانال ۱۲ اسرائیل از حمله نیروی هوایی این کشور به فرودگاه مهرآباد تهران خبر داد.
@
VahidOOnLine
درحالی که هنوز ارتش اسرائیل اعلام نکرده حمله‌های بامداد دوشنبه در پاسخ به حمله‌های یکشنبه شب سپاه پاسداران به شمال اسرائیل را با چه تجهیزات و تسلیحاتی انجام داده است، کانال ۱۴ تلویزیون اسرائیل گفت که جنگنده های اسرائیلی اهدافی را در ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76019" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EB3PX3wYDdxG89rMx1-V2fezA6ggu_9QqbSz4eKivVkL4ggvtnzy6DIT2KIJtBasBFdyiK_Drf2rTkZZub8G9LK3HqT48E-ZEgqxkRd2gNq9_ZOFxdtAO8aPvbuJQ2YASkgrWlcjWv2fdLWTuDdAyitBeQ7iP3kAndWyPtAo0nJxo9V1JQRa_LNDeH11BUA3ngUUEAFcueCuCC4UB_dw9XuuP3giUTZkEc1pq7K88ViEefELacf7Q_1g_S55KoSSaPZNZuU-oJONp1pwFfV-zxg405AOfO1f5mdo6IaYFp2hE_aV53SWZwmKBRQo_or9m5uUsSl34txCGQjJlvOwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
نجف اباد ساعت ۴:۴۰ فکر کنم با پهپاد زدن
سار پیام‌های دریافتی:
کرج هستیم الان  دوشنبه ساعت ۴:۴۳ دقیقه صبح  از راه دور صدای انفجار بسیار بزرگی اومد
سلام وحید سمت شهرک غرب ۴:۴۳ دو بار تا الان صدا اومد خفیف بود
ما رباط کریم هستیم
ساعت ۴:۴۵ صبح ۴ بار صدای انفجار اوم
وحید ساعت 4:44 صدای انفجار نزدیک سمت جنوب تهران (باقرشهر)  شنیده شد طوری ک خونه لرزید
سلام،چهاردانگه دوبار صدای بلند اومد ساعت ۴:۴۳ دقیقه
سلام وحید سمت مهرآباد ساعت 4:45 دو تا صدای انفجار شبیه دوران جنگ اومد
ما شمال غرب تهران چند دقیقه پیش و دقایق قبلش صدای انفجار مهیبی شنیدیم ولی دور بود. صدای جنگنده هم نیومد
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76018" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gj7GREz74ZCbskm6VxOJ0ZAxSzEOtQ-0PF4sT5011ihSe7VEWpSYrr92cIbgyYRL5Squwc1qFmmXoeuWH9Q_MPDxAi3RTByur_Yv0VwQV_x6oNsEu01jv2_HXqTdb9lnHp8v13BTH2-RvhlaldOQd3VU7WF90roNInM7XdvmIfSnIWPem4SYOthbMjLhnfinwKly1nCiOReZLUrEzA7QbKB6R2-klH1gEc_HsNsGINcDDfG7MtHcN-kL6ncNLjHLoohrMXyWk7juKNEUF8AXnGje3v9Dw0Q4RZ6gwrZ74oGQZDqvLf0SBU8jNlkNouqaT0JQzLuePpqJ9-CqnnKqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
دریافتی با شرح: نجف‌آباد
سایر پیام‌های دریافتی ساعت ۴:۴۵
سلام ساعت ۴:۴۵
سمت خزانه دوبار صدا انفجار اومد
صدای بمب جنوب تهران ۴:۴۵
سلام همین الان صدای دو انفجار از میدان المپیک
داره میزنننه
فردیس کرج ۴:۴۵
همین الان صدای مهیب سمت مهرآباد
ساعت ۴:۴۴ سمت غرب صدای عجیب و بلند اومد ، لرزش خفیف سعادت آباد
تهران اندیشه
دوبار صدای انفجار همین الان
سلام اصابت موشک غرب تهران تا الان دوتا انفجار 4::44
صدای دو انفجار با فاصله کرج
ساعت 4:43 دقیقه غرب تهران صدای تک انفجار
دو دقیقه بعد دوباره صدای انفجار اما دور تر
صدا انفجار داره میاد سمت غربه انگار
دوتا صدای انفجار غرب تهران
تهران زرگنده ساعت ۰۴:۴۳ صدای دو انفجار اومد
الان ساعت 4:43 دقیقه و 4: 45 دقیقه صبح غرب تهران صدای انفجار کوبنده شدید
همین الان دو تا صدای انفجار در اصفهان شنیده شد.
سلام وحید. شهرک اکباتان. صدای انقجار اومد دو بار همین الان. ساعت ۴:۴۳ و ۴:۴۵ دقیقه
صدای انفجار , کرج , ساعت ۰۴:۴۲ , ۱۸ خرداد ۱۴۰۵
صدای انفجار , کرج , ساعت ۰۴:۴۵ , ۱۸ خرداد ۱۴۰۵
کرج صدای انفجار 4:45
جنوب غرب تهران دو سه تا صدا مثل انفجار از دور اومد
صدای دو انفجار مرکز تهران ۴ و ۴۵ دقیقه صبح
یه صدای گروم مانندی اومد اما دوره مرزدارانیم ساعت ۴:۴۳ بعدی ۴:۴۵
سلام وحید جان ساعت 4:40 دقیقه رباط کریم حداقل 4 تا صدای انفجار اومد
ساعت ۴:۴۳ و ۴:۴۵
۲ تا صدای مهیبی اومد نمیدونم چی بود
سمت خیابان زنجان
زد صدا اومد شهران ۴:۴۳
دوباره زد
نزدیک نیست ولی صدا میاد
۴:۴۵ تهران شهران
وحید ۴:۴۳ صدای انفجار دریاچه چیتگر
کرج مهرشهر دو تا انفجار به همراه لرز ساعت 4:40
احتمال میدم سمت فردیس باشه
وحید تهرانم سمت شرق یه صدا هایی میاد شبیه انفجار ولی نمیتونم تشخیص بدم
۴.۴۵ دقیقه تهران سمت غرب ۲ تا صدا انفجار
سلام غرب تهران دو بار صدای انفجار اومد
سلام وحید ساعت ۴:۴۵ دقیقه شرق صدای انفجار اومد.البته دور بود.
وحید ۴:۴۲ پرند صدای انفجار مهیب حداقل دوتا
سمت م معلمم یافت اباد
همین اطراف بوده صداش همراه با لرزش بود
دوتا صدا انفجار 4.43
وحید جان ساعت ۴:۴۵ سه تا صدا شبیه انفجار سمت غرب شنیده شد.
وحید جان شهرری همین الان دوجا رو زدن شیشه ها لرزید
ساعت ۴:۴۵ ۱ انفجار دیگه شنیده شد
دومی صدای مهیب تر بود
جنوب غرب تهران سمت تهرانسر همین الان صدای دو تا انفجار اومد حس میکنم موشک بود
سلام تهران سمت شرق و غرب صدای خیلی بدی اومد
۲ تا پشت سر هم ساعت 4:43
مرکز شهر سمت ۷تیر. ۳تا صدای انفجار از دور اومد الان ساعت ۴:۴۵
وحید جان صدای دو تا انفجار به فاصله یکی دو دقیقه حدود ساعت ۴:۴۴ از نزدیک ستارخان شنیدم
سمت صادقیه تهران تا الان دو بار صدا شنیده شد
از ساعت ۴:۴۰ تا ۴:۴۵
اما بنظر دور بود معلوم نیست کجا بود
سلام مرکز شهر تهران ساعت ۴:۴۳ دوتا صدای انفجار پشت سرهم اومد ولی صدا دور بود
سلام اسلامشهر ساعت 4:42 بامداد صدای خیلی بلند اومد
صدا انفجار تهران ساعت 4:44 سمت پیامبر مرکزی
دو تا صدای انفجار مانند اطراف اصفهان چند دقیقه پیش( فکر کنم نجف آباد ۴:۴۲)
ساعت ۴:۴۵ و ۴:۴۰ دوتا صدا انفجار اومد
سمت مهراباد
سلام اقا وحید ، سمت شهرری رو فکر کنم زدن خیلیی صدای بدی اومد من از خواب پریدم
سلام وحید جان  الان
دو بار بیدگه ملارد رو زد
کرج مهرشهر
صدای دو انفجار ۴:۴۳ و ۴:۴۶
وحید حوالی ۴:۴۰ تهران صدای انفجار شنیدم
دو مرتبه بود، اولی اومد بعد از ۵ دقیقه دومی ترکید
4:45 فردیس 2 صدای انفجار از دور دست
دوتا صدای بدجور اومد ساعت ۴‌.۴۰
سمت خانی آبادم ولی صدا یکم دور بود
ولی زیاد بود مثل غرش بود
شهریار صدای چند انفجار بیشتر سمت رباط کریم می خورد باشه
درود وحید جان ساعت ۴:۴۳ دقیقه ۳تا صدای انفجار توو پرند شنیدیم
سلام ساعت4:42دقیقه صبح صدای انفجار در اشتهارد شنیده شد 2مین بعدش هم بازم صدای انفجار صدای بمی داشت
سلام اقا وحید من اسلامشهرم با صدا انفجار بیدار شدم
صدا صدای زدن بود،سه تا انفجار شنیدم
وحیدجان سمت شرق اتوبان بسیج صدای 2تا انفجار اومد ساعت 4:45
رباط کریم صدای شدید انفجار
چهار پنج تا
غرب تهران ۴ و ۴۰ صبح صدای دو تا انفجار اومد اولی شدید بود از خواب پریدم
ساعت ۴:۴۵  دو بار صدای انفجار اومد کرج
تهرانسر ساعت ۰۴:۴۳ صدای انفجار شنیدیم و از خواب پریدیم.
اصفهان چند تا انفجار شنیده شد
ساعت ۴:۴۲ دقیقه، از سمت غرب تهران دو تا صدای تک انفجار اومد. یکی دور و یکی نزدیک
درود صدای چهار انفجار شدید اومد ما سمت نسیم شهر هستیم جوری بود از خواب بیدار شدیم
ما نزدیکی اکباتان زندگی می‌کنیم و توی پنج دقیقه ی اخیر سه تا صدای انفجار شنیدیم
کرج صدای انفجار میاد
قطعا حمله شده
رعد و برق و غیره نیست
اصفهان دوبار صدای انفجار 4:42صبح
هیچ صدای جنگنده یا موشکی نیومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76017" target="_blank">📅 05:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیام‌های دریافتی از ساعت ۴:۴۰
سلام وحید جان
4:40 دقیقه انفجار از سمت سپاه تبریز طرف متظریه اومد
۴:۴۰: وحید ارومیه یه صدایی اومد نمیدونم چی بود
صدای انفجار شدید در ار‌ومیه
مشخص نیست صدای چیه
سلام آقا یک صدای مهیبی همین الان از ارومیه اومد ساعت ۴:۳۹. شب هم البته چندین تا موشک از اینجا فرستاده شده بود.
سلام وحید ارومیه ساعت 3:39 صبح صدا اومد و انگار زدن چون خونمون لرزید و دقیقا مثل موقع جنگ بود
وحیدجان نجف‌ آباد صدای چند انفجار شدید. ۴:۴۲
وحیددد
دارنن  اصفهانو میزنن
نجف اباددد  سمت ویلا شهر
دوتا زدن همه جا ترکید
لرزید داریم سکته میکنیم
شاباد موج انفجار شدید
سلام وحید غرب تهران صدای انفجار شدید اومد همین الان ۴:۴۳
وحید اینجا صدا انفجار اومد ۳ بار
خیلی بلند و نزدیک. ما کامل از خواب پریدیم
بدون صدای جنگنده بود.
نجف آباد اصفهان
خمینی شهر دوبار صداری انفجار اومد
وحید زد الان تهران رو
یوسف آباد ۴:۴٣ صدای انفجار از دور شنیدیم.
مجدد ۴:۴۵ صدا اومد.
۴:۴۲دقیقه همین الان دو انفجار پی در پی اسلامشهر
انفجار مرکز تهران ساعت ۴:۴۳
وحید زدددددددد
بالاخره زد
همین الان ۴:۴۳
غرب تهران سمت جنت آباد صدای وحشتناک اصابت موشک یا بمب
صدای جنگنده نیومد
دوباره الان ۴:۴۵ دومی  رو زد
توضیحات اینکه چند دقیقه قبلش برق نوسان شدید کرد
صدای دو تا انفجار همین الان نجف آباد اصفهان
انفجار لرزش شیشه صادقیه تهران
غرب تهرانسر یدونه صدا
اسلامشهر همین الان صدای انفجار مهیب شنیده شد
سلام ساعت ۴:۴۱ صبح، صدای انفجار شدید تو تبریز اومد، جوری که از خواب پریدم، قطعا پدافند و اینا نبود...
وحید جان از سمت قروه کردستان صدای سه انفجار شنیدیم با فاصله ۱۵ دقیقه، به نظرم موشک خوردیم چون لرزشش زیاد بود
سلام وحید جان
ساعت ۴:۴۴ صبح اسلامشهر مرجان آباد
۲ انفجار شدید پشت سر هم
جنت آباد جنوبی صدای انفجار - ساعت ۴:۴۴ صبح - ادامه دار نبود در حد دو سه تا بود
۴:۴۵ مجدد زدن
ساعت ۴:۴۴ دوشنبه صدای ٢ انفجار با فاصله ١ دقیقه از هم غرب تهران
الان صدای دو تا انفجار شدید اومد . اصفهان
سلام از انديشه
وحيدجان فكر كنم ٢تا صداي انفجار بمبي اومد اينجا
صدای انفجار از دور
غرب تهران ۴:۴۳ حدودا
ساعت ۴:۴۲ دو تا صدای انفجار توی قائمیه اسلامشهر  اومد
پشت سر هم
آنقدر شدید بود شیشه ها به شدت لرزید
ساعت ۴:۴۲ صدای انفجار خیلی خفیف شمال اصفهان
انگار خیلی دور بود از ما
فکر کنم ۳ تا بود
اسلامشهر ساعت ۴.۴۴ دقیقه صدای  سه تا انفجار اومد
وحید حان مرکز تهرانیم، ساعت ۰۴:۴۴ صدای ۳ تا انفجار شنیدیم.
وحید سلام. صدا دوتا انقجار ۴/۴۱ نجف اباد
صدای انفجار فردیس
وحید نجف اباد صدای انفجار بلند  چند تا شیشه های خونمون لرزید مثل چی
بیدار شدیم ۴.۴۳
یه جارو زدن داره مثل چی ازش دود میره سمت همین نیرو انتظامیو اینا که توی جنگم زدن
الان صدای دوتا انفجار اومد
شیشه ها لرزید
مثل صدای لانچ موشک بود
شاید جای رو زدن ولی صدای جنگنده نیومد
خمینی شهر
سلام نجف آباد الان صدای ۱۰ تا انفجار اومده و جنگنده
سلام نجف اباد ساعت ۴:۴۲ دو تا انفجار خیلی بزرگ کامل مثل وقتایی که میزدند بود. صدای زیاد و بعدم موجش اومد
سلام وحید همین الان صدا انفجار اومد سمت تهرانسر در حدی که شیشه لرزید
دوباره الانم اومد ولی دور بود
4:41 صدای انفجار اومد
04:44یکی دیگه.
فکر کنم بیدگنه رو زدن
چند دقیقه پیش تو استان کردستان شهرستان قروه سه تا صدا اومد آسمون صافه ولی اطراف رو زدن احتمالا
غرب تهران صدای انفجار
مجدد
وحید داداش صدا انفجار کردستان
سلام كرج ٤:٤٣ صدا انفجار طوري از دور اومد. رعدو برق نبود
بازم الان صدا اومد
ساعت 4:42 صدای انفجار خفیف و لرزش زمین سمت صادقیه تهران
4:44 صدای دوم شدید تر بود. صادقیه
توهم زدم یا صدا اومد؟ سمت ملارد
زدن وحییید زدنننن
انلاین شو وحید بد دارن میزنن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76016" target="_blank">📅 05:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76015">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVRCb9AnvFef1bgbFkm8S5-9mVgt7hU0MJgQb9waOa6OIk_VVBZmVW8ivL3cMV4HCWugSPL-p02S7pz30QTpUd071Ykwk2KtACG6B5DOCv9z2NZEnivjAaO_pjAYP3AnYU17FtzBHq_eG7AMnT-Es9FTmO9sNGbc4WLYt8-6wF1_RcIBGWK11Dla_4LOSyd0FLzQjJKZkRoFGhlB89ej48IXjxejyQ8XWGsv2YYc-uTXxeWIPi8TmBVMA7RfpdlEyqVTNc4A3iq5LsBMlqxeon3L-9R_v0I7nGhW-Va87xnjj5i40pY3Yzvivikpp9ByW8ze5AvqDCxPOFk3Mowd2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل با انتشار بیانیه‌ای از حملات هوایی به چند نقطه ایران خبر داده و گفته است: «نیروی هوایی اسرائیل، تحت هدایت رکن اطلاعات ارتش، اندکی قبل به اهداف نظامی رژیم تروریستی ایران در غرب و مرکز ایران حمله کرد.»
پیش از این سپاه پاسداران هشدار داده بود که در صورت اقدام متقابل اسرائیل با شدت بیشتری واکنش نشان خواهد داد.
جزئیات بیشتری درباره ماهیت اهداف مورد حمله، میزان خسارات یا تلفات احتمالی منتشر نشده است.
این حملات پس از آن انجام می شود که ایران ساعاتی پیش چندین موج حمله موشکی به شمال اسرائیل انجام داد و سپاه پاسداران اعلام کرد این حملات آغاز یک هفته عملیات مستمر خواهد بود. همزمان، مقام‌های اسرائیلی هشدار داده بودند که در برابر حملات ایران واکنش نشان خواهند داد.
این تحول در حالی رخ می دهد که دونالد ترامپ، رئیس جمهور آمریکا، در ساعات گذشته از بنیامین نتانیاهو خواسته بود از اقدام تلافی‌جویانه خودداری کند تا روند مذاکرات و توافق احتمالی با ایران آسیب نبیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76015" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GabR9I7FrrzLwYKpqtcyoQ-Wk--Qr7R9kc18tplUZyerJeLfJ-Jk8eCjrut40-8BA6LT0kjBQcK9qDVCsz12ulmxizWBoAG38S1R-hVBu6LdbNytIRXZxLDta9Y6BRdbfmicAYqzBTRStTgyVbOyE4xf2mm6XYwn7QWAhHCVv3zHFntw4I1ylLkvCtI-R9eSWC5R01MxLhung7Bi0k22emFo_Vnzqb-5QqhkNDJDRrVnGQvknfbu6ld-cCCusMFzU9iWyQM8AC7kKaohPEah6chlXAjgPc-6URQI5EsaB1rEwW4oJ7ykONIsLv9HdvSgUq_kZ28VuI3eEwetMmZsmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه‌های رسمی ایران از شنیدن انفجار و حمله هوایی به چند شهر ایران از جمله تهران، اصفهان، تبریز و نزدیک به کرج خبر می‌دهند.
bbc.in
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76014" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knp_95B1weuhTRtcG6zwJzkFk1sGQOCEBvmryVnvSAisxJrNXkB3xYOS7cbVK1Vc6aPoiAjG4ZkBlUSlHbYFXzfl27i4dlXpGqnuGUFeLEbfQgvYocdTQLh8y2GaoEyKpjVC1LAw8f5HmYSSv2nPfJL97Lg4Ir2eOUFLuwBCxPA4SE33Q6GZP8N68CNerVyWPJwGdzbMPhLMJtjGYt6jEMa4OIIOxttT8sDYcYbXX2gfkKgS8qFBQoco7G-lSEk_VPOetUhYcna4IXObhZWHNXOJDVqSrJZfOMDdebcqfcsejgpcJ0xGNAxI6KrPObJE9MUDs5oFjccEU_Y7E0DJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در تهران، اصفهان و تبریز در بامداد دوشنبه خبر داد. خبرگزاری تسنیم از وقوع انفجار در کرج در بامداد دوشنبه خبر داد. ارتش اسرائیل نیز اعلام کرد نیروی هوایی این کشور «مدتی پیش» اهداف نظامی متعلق به «حکومت ایران» را در غرب و مرکز ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76013" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YRQYxzBCZRJafsZUU40rgICbGqOqL-NtuOZ6WQQ7golTfBWFxONNPuWk2FKbxjj8AnTvE_7P8RI8bFPKoGl9aMaNyhuWcMHdvJPaNWNuwtTWVqBSTyomkp3Kk3HETf3VTMle-PFCmVEgwdl3EZ0YuCjICO-jo_3B2kWo480D5SngFKauwYPzvukqE4UD-3PdTjo0ZwAkUfvqdbM5ZJNdIBxd0rCCn-KOa8cebWxhJBrilQ1epEOs3rrOMMHz8x1rwlW6GvMRsgRpUcqPrAH4CAbJLrFEvevHsZ4u0kVp6VS5uLZpwkhjxrdeETF7jwRRBJlnuRx5LzNK5Ff4DzgVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با درخواست دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به تعویق انداختن پاسخ به حملات موشکی بالستیک ایران موافقت کرده  تا به واشنگتن چند روز دیگر فرصت داده شود تلاش‌های دیپلماتیک برای دستیابی به توافق با تهران ادامه یابد.
بر اساس این گزارش به نقل از یک مقام ارشد آمریکایی و یک مقام ارشد اسرائیلی، ترامپ در تماس تلفنی یکشنبه شب از نتانیاهو خواسته از انجام حمله تلافی‌جویانه خودداری کند، زیرا به گفته مقام آمریکایی، او معتقد بوده «ما به انجام یک توافق خوب نزدیک هستیم».
طبق این گزارش، نتانیاهو تلاش کرده با این درخواست مخالفت کند و ترامپ را متقاعد کند که اجازه حمله به ایران را بدهد، اما در نهایت «تا حدی به‌طور غیررسمی» با درخواست رئیس‌جمهور موافقت کرده است.
این مقام آمریکایی گفته است که این گفت‌وگو بسیار آرام‌تر از تماس پرتنش هفته گذشته درباره طرح‌های اسرائیل برای حمله به بیروت بوده است؛ زمانی که ترامپ به‌طور علنی اعتراف کرده بود بر سر نتانیاهو فریاد زده و الفاظ تندی به کار برده بود.
پس از این تماس، این مقام گفته است: «فکر می‌کنیم رئیس‌جمهور کمی زمان خریده است. او بسیار قاطع است که ما به توافق با ایران نزدیک شده‌ایم. فکر نمی‌کنم در حال حاضر حمله اسرائیل قریب‌الوقوع باشد.»
او همچنین گفته است: «ما در یک لحظه حساس هستیم — چرا باید وقتی در راند چهارم هستید، یک توافق احتمالی را به خطر بیندازید؟ رئیس‌جمهور فکر می‌کند سه ماه است درگیر این موضوع هستیم و اکنون زمان پایان دادن به آن است.»
با این حال، هنوز تصمیم رسمی در اسرائیل گرفته نشده و طبق گزارش شبکه ۱۲، نتانیاهو تا نیم ساعت پیش همچنان در حال برگزاری نشست با مقامات ارشد امنیتی درباره این موضوع بوده است.
@
‌VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76012" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76011">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G3zB9DbzXP9Q4al6VqHv8xT91087Ijwz6QOiDvgriX4_nOaIRB-M86Yyza5CgIxie6QLT4pnFr5Z4x0NxeD0msg5DnRwW2qzFl4uXsBP89lJruH7H-t4baBX5kxpg-MpE6UiRHEqPD1ZSNpJI13M3TFrriXDj15oiq6sloJ2eu6en1lh8nRBeSNqK8jdv4BxS-9z6AEJE-CmpuKbYEgUcRyvt2hbupVlf2KB2Gd0NasuRD1HrnDKRkeWcK7msOesLuf1GbPTkJM10bvQCP6jXsK6WVrGf5NZumC0gHyRcckDfOQgmC7rIw475lYVA3IbgLG8iHltezS56_8El944gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید هر توافقی که او با حکومت ایران کند نخست وزیر اسرائيل خواهد پذیرفت
رئیس‌جمهوری آمریکا در گفت‌وگویی تلفنی با فایننشال تایمز گفت که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، چاره‌ای جز پذیرش هر توافقی که آمریکا در مورد آن با رژیم ایران مذاکره و نهایی کند نخواهد داشت.
دونالد ترامپ گفت زیرا «تصمیم‌گیرنده اصلی رئیس‌جمهوری ایالات متحده» است.
دونالد ترامپ به فایننشال تایمز گفت: «او (بنیامین نتانیاهو) هیچ انتخابی نخواهد داشت. این من هستم که تصمیم می‌گیرم. همه تصمیم‌ها را من می‌گیرم. او (نتانیاهو) تصمیم‌گیرنده نیست.»
به گزارش فایننشال تایمز، آقای ترامپ این اظهارات را اندکی پس از آن مطرح کرد که جمهوری اسلامی در جدی‌ترین نقض آتش‌بس از زمان توافق آتش‌بس در اوایل آوریل، چندین موشک بالستیک به سوی اسرائیل شلیک کرد.
آقای ترامپ تأکید کرد که حملات موشکی جمهوری اسلامی تغییری در تمایل او برای به نتیجه رساندن مذاکرات میان آمریکا و حکومت ایارن ایجاد نکرده است.
او به فایننشال تایمز گفت: «این موضوع هیچ تأثیری بر توافق نخواهد داشت.»
ارتش اسرائيل به صدای آمریکا گفت که جمهوری اسلامی یازده موشک به اسرائيل شلیک کرد. ارتش اسرائيل پیشتر گفت که حملات موشکی جمهوری اسلامی را دفع کرده است.
در همین حال در واکنش به حملات موشکی جمهوری اسلامی، ارتش اسرائیل در بیانیه‌ای به صدای آمریکا گفت که رئیس ستاد کل ارتش اسرائیل، ایال زمیر، در حال ارزیابی وضعیت در مجمع ستاد کل است. ارتش اسرائيل به صدای آمریکا گفت: «نیروی دفاعی اسرائیل به محض صدور دستور، با قاطعیت به دشمن حمله خواهد کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76011" target="_blank">📅 02:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76010">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری تسنیم: "صدایی که دقایقی پیش در تهران شنیده شد مربوط به رعد و برق است و این صدا ارتباطی با پدافند یا موضوع نظامی نداشته است."
من هم پیام‌هایی گرفته بودم که بعدش با «ببخشید انگار رعد و برق بود» آپدیت شدند
.
زیاد پیش میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76010" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DbMLcDWgrZzMdTDciRf7P1r1WAqgYqYE2ZWIlc09xS9hKx3yEL6HiYmP6rURIcofVL8VMItnPafl1M7_Yd0_zJNK74VEX8MCg4UF00QROIZqtzD4QCPaklQq_B1Zb7PYqhtPN0Kpzhb1SQx8SCQCjzZLLKqR_FHpn9bROi2Q1sl2zzVDKvladz-YiNm3DyI87AbFQTe6fdxdL0GSWLiGdHLVLnKSVVZ72QX3KTQzlB_GqOiAIViVdRfbyhmpubN6XxanTLUmZnMgYofUYFt6oKkiCOVg5sMhzdvsat1PN6rC2X9K47WBmUzRumioladBRwwhF4-EEAmYWkN34fcYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">shamidartii
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76009" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76008">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S14CI8iLPcfUm7lAYg6WBATqYN4GQV658C9OeZx88MqgEYmYdtzydZwMH6GfEpcPDszffCpBsHybbaGwC5ojPn92GZlnpd874W9ivv7B6FDfly7Ce6yoGjLLbXYW1ZdUlMBccbrpUVYz2HLL-j_aFcf75PzBLcdCRfY7essjRnFnXWvUaf4lsBECWjYv5iGiWoJ5NS2y4EzlBpkw0jaxKlXiXPDwDbCP0EtskxU5-Ynis84_JaBBXYcsoL4N5wK_me98Xx51PHmeF67vKdSrU18y_9JPWVXDHbHQ_ZdyQgHYr6amepWwmPi0kCDJF75ZvEdYE_Z7-Kf91pL61AwBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با به اوج رسیدن نگرانی از آغاز درگیری مجدد نظامی میان ایران و اسرائیل، سازمان هواپیمایی ایران اعلام کرد تمامی پروازهای شهر فرودگاهی امام خمینی از بامداد دوشنبه ۱۸ خرداد تا اطلاع ثانوی متوقف خواهد شد.
در اطلاعیه این سازمان آمده است: «مسافران از مراجعه به فرودگاه خودداری کرده و اخبار بعدی را از مراجع رسمی پیگیری کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76008" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76007">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jz6fAAoq8Sp3rVhsH31MEO0c0c-OfMJU4dejYDRx2ryBvx_-fb2Bzr00UU3aX1Ja0dnzGgOrefQ-5seHUb4YY-gZOt9uuAuGzCRm0lrbeVibzKtdzSBVuEh7h4EEO2NbfpymxAmxEcV8L6cCAPPHPzhUaWVynliGowx4AN-8-_NhDgF0CZKBANkvJ-dniODDa4Xk7OM0q5MkCAE0cD6QX_qSrcNPNy808T46O9bZnxmDc7owXN6KA5pZ1DRitM1bmpHzh7BhbZX9_NgB6IgnaTCrjcXL1bBKbBCncSvbagOwDJbKqC_9bduQn31zMMZaRoCXpM31E34WuGLQQNlloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایتامار بن گویر، وزیر امنیت ملی راست‌گرای تندرو اسرائیل، پس از حملات جدید موشکی ایران به شمال اسرائیل، خواستار واکنشی شدید شده است.
او عصر یکشنبه در پیامی کوتاه به زبان عبری در شبکه اجتماعی ایکس نوشت: «امشب تهران باید بسوزد!»
اظهارات ایتامار بن گویر در حالی مطرح شده که ایران ساعاتی پس از حمله اسرائیل به حومه جنوبی بیروت، موجی از موشک‌ها را به سوی اسرائیل شلیک کرد. ارتش اسرائیل اعلام کرده است که این موشک‌ها رهگیری شده‌اند و گزارشی از تلفات فوری منتشر نشده است.
ایتامار بن گویر از چهره‌های تندرو کابینه بنیامین نتانیاهو به شمار می‌رود و در روزهای اخیر نیز از توافق آتش‌بس میان اسرائیل و لبنان انتقاد کرده بود.
@
VahidHeadline
نفتالی بنت، نخست‌وزیر پیشین اسرائیل، در واکنش به حملات موشکی جمهوری اسلامی به اسرائیل، در شبکه ایکس نوشت: «خویشتنداری یا واکنشی نمادین، این پیام را به دشمنان ما منتقل خواهد کرد که ریختن خون شهروندانمان بی‌هزینه است؛ از این‌رو اسرائیل باید با قدرت و به‌طور موثر عمل کند.»
بنت نوشت: «این یک لحظه آزمون است: «آیا اسرائیل کشوری دارای حاکمیت است که توانایی دفاع از خود را دارد؟»
نخست‌وزیر پیشین اسرائیل نوشت: «در این موضوع، همه ما، تمامی شهروندان اسرائیل، در کنار یکدیگر ایستاده‌ایم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76007" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76006">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BIlTitCM8LGz7nmqpKarITiaQx1vHAx6QQndwHUyIa2k_K9-Q2yHXEajn8ZJDZn2oR1Getfg-hOaom7ga_5qSOJ9Vl1sDAzfWeQ18YFuTGvwIja3D7_Re2o0bGcJ1Yub_k4wKT3hcp-BdS5yIIBstf3s9XjNzcgTNudbz2UohfDX_2K_NBnPvI3RFx_hUUMGymc4Y7P2B2YpD9PsqJDY-aOqxOakLXvTwZG3CsU_zbjCWK11_MivzMaawEiXVqnHyMrATu9iq81mVV1c6t0ZaRi87F4O3wH_c1a6mVljARGxLl6cTWISTXRu5n1zt1Dkmndcj7Pw-9P5xDAxu0csbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با حملات موشکی ایران به اسرائیل، تسنیم، خبرگزاری وابسته به سپاه، یکشنبه‌شب، در پی شنیده شدن صدای انفجار در تبریز، گزارش داد: «براساس پیگیری‌ها، صدای شنیده شده در‌ فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده است».
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام وحید جان
الان ۲۳:۵۵ سه صدای انفجار بزرگ آمد تو تبریز
پیام بعدی در ۱۹ دقیقه بامداد: همین الان باز زدن تبریز رو
سلام وحید جان
تبریز ساعت ۱۲:۱۵ نزدیک لشکر عاشورا صدای انفحار اومد.
البته شدتش مثل انفجار های جنگ ۴۰ روزه نبود.
تبریز نیم ساعته صداهای عجیبی میاد
مطمعنا صدای پدافند نیست انفجاره
هم اکنون صدای چند انفجار شدید در تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76006" target="_blank">📅 00:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76005">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GTG0O_nSytzIyUH2US2n0Xi6P_LtLAlQYrfi0jA1rOGtAsq5GWadK1nbMMWgaLLdQYMGtQI7gw0KhnvOX9gLIWvklXquqan0RSqx5ttJwKM1wFpPkPybMV8Udijmqa0fYh3SBUjFJyayTHqGlyHfuXhL1BlkOe_luzK3j5Hk1njgOcmpG_bVYybB4Ojz-rchu_LYetupoGJVWTDbkxftWt2N3jOCN4SCpREdv8gkbBpiIr_BoHoE6V6ziUOiUF1UT9yv7fY4hcoh4oT7WMFFru5CArVsLZ4qpTKKIA6KFE2tmu8ryC9_bpt9wWVNV1LKCAzWadwo6SX4zBhcsGyOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل، افی دفرین، می‌گوید پس از حمله موشکی بالستیک جمهوری اسلامی ایران به اسرائیل، ایال زمیر، رئیس ستاد ارتش اسرائیل، در حال انجام ارزیابی و تصویب برنامه‌های آینده است.
سخنگوی ارتش اسرائیل گفت: «رژیم تروریستی ایران اشتباه بزرگی مرتکب شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76005" target="_blank">📅 00:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76003">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/upYSylL-k_e57scWLLSkiFhMvrvPtiFb8gFZijBfr2OslArrkkMowFkV0lB_9bcmeBHnWg87qJ1pQtJeaH_FImTgRdk5D2YR4stbD4M1miT33jW88qvIqQ3VjgsqCpGjO2djbEv8qxk9P6KSLv5nPyXGHLN-zeUwNF2030nV67lKHAXrx1PIjM2gyDAjYStZjZghc9axat08A-KBA6KGvB3OSfa56AfFcDx3UqJSLMMTxRNZh3BWbsxecWLw2TQ24s7G6H2gD7gsibB-uGqQIisGvcearhK5zWIMDlHRCnVrRwFGhKwSEtscnfDydz06wfaMKuc1ZoeRkd-JsXJtAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YEx0I3o1FjQGCD-PcaRjj8XjSK8lW3v1kblAPQjUnUigdIgsG3Zvbf8NVToI4KBNoQZ7cTBIL72_IAJLM1wSfmZdrAzGegNh6LM8GmDWx2BrB40D-8gZgLnazYSjd1HJ7NgggIhM1SjiTaFn4qAlrn5YLWj6aRZyxP44SyzgPZJ8xX54MW-R6LWeSuTLAMHklQmw8yfDQWF8uwMRpxISEdCetGWMkDA1iBXj03OdYTS8KVtqX1zZTL7NThZt2HcgIGUUfA2NMJSY4nuT_wWmVYW3NgoRjMqzJKb27e29Z9iMze-zltBOniPqx903HkfKGTuIFjFOAQ3Uv4pY3NxgrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
ما تهرانسریم
تو این 1ساعت اخیر که اینا اسرائیل رو زدن
نزدیک به 8تا هواپیما مسافربری از مهرآباد بلند شد
نهمی هم الان رفت
انگار دارن فرودگاه رو خالی میکنن
سلام از تهران داره همینجور هواپیما بلند میشه همشونم تو ارتفاع کم پرواز میکنن
همین الان از بالا سر مهرآباد یه هواپیما با چراغ روشن از غرب به شرق رفت
مسیر خیلی غیرعادی با ارتفاع خیلی کم ۰۰:۰۸
آپدیت:
بعدش کلی پیام مشابه دیگر دریافت کردم.
آپدیت:
وحید جان همچنان پروازها از فرودگاه مهراباد به سمت شرق ابران ادامه داره احتمالا هر ۴/۵دقیقه یک پرواز بوده لاینقطع
شاید ۳۰/۴۰هواپیمای مسافربری پریدن تو این دو ساعت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76003" target="_blank">📅 00:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76002">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sgprDiZvb9MU3plHPaI7xADhwsR6uzVi29VswiLfH3WrXiqS8GU_haML4YULk8YAXEunJKK-yLZUIGgnz-riZxm-LJcNbe1NHbkykIHuzsUpNPwJgae09dCVwhIVZodoxxL-xmPCRE4U1zl-dYViAQ76b_vBkXVJoia6SQqQ-OZ5N7DyKK3TNMfMg9VdCmC9BF1AEqIKl9q_c2kwjUkOdtbX6cSQgx0V_DUtRpFE8r8m1q3FityVWBTMjdQxiowhE3ja7NL6-xruzBMZiEcCaNP_r1-kOivTPfPjbRQHL8gnV8fuzPG6dNrtEFCki4iKNI5Jq73xgss4_gr4_xGuzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: حملات ایران به کسی آسیبی نرساند، امیدوارم اسرائیل تلافی نکند
درپی اعلام خبر حمله موشکی ایران به اسرائیل در شامگاه یک‌شنبه، دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌وگویی تلفنی با خبرنگار اکسیوس گفت: «همین حالا با بی‌بی (بنیامین نتانیاهو) تماس می‌گیرم و به او می‌گویم تلافی نکند. هر دو طرف کار خودشان را کرده‌اند. اسرائیل حمله خود را انجام داد و ایران هم حمله خود را انجام داد. دیگر نیازی به حمله دیگری نیست.»
دونالد ترامپ در این گفت‌وگو افزود: «حملات ایران به کسی آسیبی نرساند. امیدوارم اسرائیل تلافی نکند. اگر بی‌بی (بنیامین نتانیاهو) پاسخ بدهد، این ماجرا همان‌طور که در ۴۷ سال گذشته، یا حتی در ۳۰۰۰ سال گذشته، ادامه داشته، باز هم ادامه پیدا خواهد کرد.»
ترامپ افزود: «ما به یک توافق نهایی با ایران بسیار نزدیک هستیم. این توافق، توافق خوبی خواهد بود. نمی‌خواهم به خاطر اتفاقاتی که اکنون در حال رخ دادن است، این روند از بین برود.»
این اتفاق چند ساعت بعد از آن رخ داد که ارتش اسرائیل منطقه ضاحیه در جنوب بیروت را هدف قرار داد و ایران تهدید کرد به این حمله پاسخ خواهد داد.
یک منبع ارشد ایرانی هم به خبرگزاری رویترز گفته است که «ایران به هر حمله اسرائیل با نیرویی شدیدتر پاسخ خواهد داد.»
ارتش اسرائیل اعلام کرده است همه موشک‌هایی را که تاکنون از سوی ایران شلیک شده‌اند رهگیری کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/76002" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76001">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B24q-v85IdkxJevQZOZ7FZ1UMVdjyzwv4OC1XHK1ky-fxC0elH8xMog18zSuoLUjZdET4nKoXSdVNJpmFySinXoM0x-hzWhgprlQU0zOxk2J1_OgEvbsNngkkGhAgC8skGcIlZ0hcwDQOM_m0OYvj2g6mUYNI3iocEzXzZ3nkXYeM3CDywXpNjWZZ5ZUlnwAMOMil49nG9fenlxutK-8cqP5ef_SRZ9OOXPyyapRAoKYBkJHo3bfjKuDyRblnN9Y82HW_laVTQWabC6Mf6K3Va4TZJ5lRc8ddxFBY2NlC7dMsS9JsCKNQOwLl-qpg5ukbni6TEvNg9ZsPOrZ_c1YEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">mohsenreyhani01
سپاه پاسداران پس از حملات موشکی به اسرائیل در بیانیه‌ای اعلام کرد عملیات شامگاه یک‌شنبه صرفا یک اعلام اخطار بود و در صورت تکرار حملات، پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-اسرائیلی را در منطقه در بر خواهد گرفت.
در این بیانیه آمده است: پذیرش آتش‌بس از سوی ما در ۱۹ فروردین ماه مشروط به توقف آتش در تمام جبهه‌ها بود اما مثل همیشه آمریکا و اسرائیل به تعهد خود پایبند نبودند، هم حملات را در لبنان ادامه دادند و هم با تعرض مکرر به سواحل و شناورهای ایرانی در تنگه هرمز، دریای عمان و اقیانوس هند آتش‌بس را نقض کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/76001" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76000">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y3pc4wE-dxFIL5NADxZs8asnkgUxdatdApEapZncwulojqZkSPiqgIJBo5kmGDi_2BFuDvYWWwSBlZ8M5ZzFMfgBGtV_H4NWOYMOx7QL8L5CvZEfJGWAtJ5MXWk0hTFvtYg1jxtk6ZgMGHqshEjISiYMFF9YjZzIJeGciQFN5SFIpldLbxLYVq24agPuFSIV84hOPsU5HW-biUarXzYmKsbkZqp1_90Bxx64MrkVyXzzjh3iBey3wUAe2Si6pUDuQDIcjBTnwaCdgnWYzMWJCW_vt-9bFgaJ2QqnvGXMQk2_Tu03yMx040X3VRh-XFLKY9ifb8GNqsyHJEHhdUHFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز گفت: پیشنهادی که به ایران دارم این است: موشک‌های خود را شلیک کرده‌اید، همین کافی است.
او افزود: به میز مذاکره بازگردید و توافق کنید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 473K · <a href="https://t.me/VahidOnline/76000" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75999">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ti6LWtoN4q7c8jBZ1wQvJgkN2mUeHUXZCzodSeRNB0As6XXqDcmH1UkW96CLppP4J5e-wN9VovVkfVyo23d1tGLwYpjux8yjrECWKgFYeDXp3KbiXpbiK81WWt_Jgoc1amsWObM_ja9r-FySms5xtHMGFRGlieAu988MNC1QSrlKy4Ak1sG3780QvTwGqwGB6zDFJK_tf-zeea5DwstFSVVndbawkzrAwQcDtZsGQ9jrRME-co1gkYowxvMqu4khna4rOFaqcujHhnI6BqGQgly37dPCciXSrYMBoFZVb8nPLkN52IkY54WMWyq63NWmfe_ijfov6d1Py8frinxXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی اسرائیل در بیانیه‌ای دقایقی قبل اعلام کرد که این نیرو تاکنون تمامی موشک‌های شلیک‌شده از سوی جمهوری اسلامی ایران را رهگیری و منهدم کرده است. این نیرو گفت ارتش اسرائیل اکنون پرتاب‌های بیشتری را که به سمت اسرائیل شلیک شده‌اند شناسایی کرده است.
@
VahidHeadline
ارتش اسرائیل به صدای آمریکا گفت که جمهوری اسلامی تاکنون یازده موشک به سمت اسرائیل شلیک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/75999" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75998">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">توییت باراک راوید، خبرنگار آکسیوس:
یک مقام اسرائیلی به من گفت که اسرائیل قصد دارد به حمله ایران تلافی کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/75998" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75997">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOHgYOb3-nsEuwtV17ig4O5t2mefVXlvYOuilw8zq7Rjgfz_Mk4e4awDUh_vb_4EaParyy7dKKoTRq-Q72sSw_4rhphDq_RkMjJY5dH82J02XHoUeU2Uogz2b4IqYifdyi31qpv_oyyo3xKHqTz1MTqSVTPikQxLmXKqHfHYBxrYN6R_kqL4E-VN7i4nrc9WfMR7yemqccLyia2sSk4SIvVgW27zOsIpOckk-RmP9JjhrgMTgtp5z_acfRGlgz92agJoywK6LGa6rZhVIGLnYRmvfkGTQ8Zdt3ckwTwX9Can2VQXHbQUZoENdE-xGhfLVcTjIsbY0pSa5XuM90LgnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: در صورت گسترش حملات پاسخ ما کوبنده‌تر خواهد بود
به نقل از تسنیم، خبرگزاری وابسته به سپاه:
"فرمانده قرارگاه حضرت خاتم‌الانبیا(ص):
رژیم متجاوز صهیونیستی با نقض مکرر آتش‌بس شرارت های خود علیه مردم مظلوم لبنان با چراغ سبز و حمایت آمریکای جنایتکار و سکوت مجامع بین المللی را روز به روز افزایش داده و با استفاده از سلاح های ممنوعه از جمله بمب های فسفری مرتکب جنایات جنگی می گردد.
با وجود هشدارهای قبلی جمهوری اسلامی ایران، رژیم کودک کش صهیونیستی با عبور از همه خطوط قرمز و افزایش حملات در جنوب لبنان، ضاحیه بیروت را هدف قرار داده است.
قبلا اخطار داده بودیم در صورت گسترش جنایت در ضاحیه بیروت، اهدافی را در سرزمین های اشغالی مورد هجوم قرار می دهیم.
ارتش صهیونیستی باید حملات خود به جنوب لبنان و ضاحیه را متوقف نماید و در صورت گسترش حملات خود به آن منطقه و یا پاسخ به اقدام ایران با ضربات کوبنده تر و پشیمان کننده روبرو و حملات ویرانگری علیه رژیم و حامیان آن آغاز خواهد شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 474K · <a href="https://t.me/VahidOnline/75997" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75996">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">☄️
موج بعدی شلیک موشک به سمت اسرائیل
پیام‌های دریافتی:
دوباره شلیک از کرمانشاه
دوباره یکی دیگه زدن الان
یکی بود
10:44 دوباره صدای انفجار اومد کرمانشاه
صدای انفجار مجدد
بازم زدن
همین الان صدا اومد از روانسر کرمانشاه
22:47 شلیک موشک از تبریز
آذرشهر [نزدیک تبریز] صدای موشک ۳ تا
سلام وحید
ساعت ۲۲:۴۰ ۴ تا شلیک از تبریز به فاصله هر یک دقیقه
نور خیلییی زیادی داره و صدای زیاد
🔄
آپدیت:
منابع حکومتی نوشتند از اصفهان و ارومیه هم موشک شلیک شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/75996" target="_blank">📅 22:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">☄️
'شلیک موشک از کرمانشاه'
‌
بعضی از پیام‌های دریافتی:
سلام همین الان صدای موشک از کرمانشاه اومد
سلام صدای جنگنده در کرمانشاه
سلام وحید جان.
همین الان ساعت ده و نیم دو تا موشک از کرمانشاه شلیک شد
صدای غرش  شدید ترسناک ساعت 10.31 شب کرمانشاه میاد
وحید همین الان از کرمانشاه موشک پرتاب شد
از کرمامشاه الان دوتا موشک شلیک کردن
صدای پرتاب موشک از کرمانشاه الان
سلام وحید جان
من کرمانشاهم
الان ۱۰:۳۰ یه صدایی شبیه شلیک موشک اومد
مطمئن نیستم، ولی دقیقا شبیه صدایی بود که زمان جنگ میومد.
🔄
توییت ارتش اسرائیل:
ارتش اسرائیل موشک‌هایی را که از ایران به سمت اسرائیل شلیک شده بود، شناسایی کرد. سیستم‌های دفاعی برای رهگیری این تهدید در حال فعالیت هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 486K · <a href="https://t.me/VahidOnline/75995" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75994">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیام‌های دریافتی از شنیده شدن صدای جنگنده در تهران که لابد داخلی است:
سلام وحید جان ۲۱:۳۲ شمال غرب تهران صدای شدید جنگنده
درود وحید جان
صدای جنگنده (؟) غرب تهران
۲۱:۳۲
صدای جنگنده غرب تهران ساعت ۹:۳۲
بازهم مرکز تهران صدای جنگنده یا هواپیما رو نمیدونم ولی خیلی پایینه ساعت ۲۱:۳۳
شهرک غرب
صدا جنگنده
صدای جنگنده ساعت ۲۱:۳۵ دقیقه، شمالغرب تهران
مرکز تهران صدای جنگنده میاد شدییید
صدای نامتعارف جنگنده در مرکز تهران از ساعت ۲۱:۳۳
غرب تهران صدا جنگنده داریم 9.32
۹:۳۱ شهرآرا صدای جنگنده میاد وحشتناک خیلی پایینه
سلام الان نیروهوایی صدای خیلی عجیب میاد صدای جنگنده ست انگار خیلی بلنده
سلام وحید . ساعت ۹ و ۳۳ دقیقه شب مرکز تهران صدای جنگنده میومد واضح . ۱۷ خرداد .
سلام ساعت ۲۱ و ۳۳ دقیقه شنیده شدن صدای جنگنده زیاد ، امیرآباد تهران
صدای جنگنده میاد سمت مرکز شهر
آپدیت: کلی پیام مشابه میاد که دیگه نقل نمی‌کنم. درباره صدای هواپیما اهمیتی نداره که در کدوم محله شنیده شده.
بین پیام‌های اولیه دو تا پیام هم بودند که نادرست به نظر می‌رسند:
سلام وحید، اینجا شهریار صدای موشک میاد. احتمالا از بیدگنه جمهوری اسلامی داره موشک میزنه
وحید از بیدگنه موشک زدن ۲۱:۲۸
صداش تا فردیس اومد قشنگ
آپدیت:
در پیام‌های بعدی روی این تاکید می‌کنند که صدا طولانی بود و چند دقیقه طول کشید.
بعضی‌ها هم نوشتند این بار هم هواپیمای مسافربری بوده با رفتاری عجیب و پرواز با ارتفاع کم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/75994" target="_blank">📅 21:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75993">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KBwwrpkuXXsNASnIwAFF1BH-hJaNwo7gd_xwN86gwQs-x6_fHVQcGacgudO5LYO5hz8Nll90iGzyHYZMo23YFdgH5yyfAOjnwqQweGrtGFzm3lvbA8OTiNKgQXDLC23zdN0gsWHeZbBKXmTnB6io6o1fS7kSOSQpW9b4HwQcIeYQ660fp8w41vdz_RW2yOduxGXkZOh5ygY0tFQzcVKyhIlIGylTG8P4FqJ-zQlriEO6qlPSWuvV5BL__E5YfI9bmiJ8ygMVrJFLseFxLThJuowHNCdw8n-UCZ1NdIz4vnXmAnT5YVm38VP5ZbrgNcP1shFxWrUsT-_yJY0BrfnSsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت پزشکیان علیه صدا و سیما
رئیس دولت در جمهوری اسلامی، تلویزیون حکومتی را در شبکه فیلترشده ایکس تهدید کرد:
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/75993" target="_blank">📅 20:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75991">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oUjieCrOn8wEmCIVvsxoRQbQzQXzOF3an0HCiBDh5C8B8uo6gdWNdNF3I5Lmto27KV8VYquFhi8BSCjI4xROpKszMkU14TcmKnaBpGSY9_jolxG1UiWHdI0fH_w6I-zF7QL3F_olnyGNFyTOyGLPNX3QmyetiD047I1ZPJTCMakZnAB1xBvEm6yiuEplHh4h8FGqVAAfa0rGsky8eFhGI7Sf2nPfARjkb_HtMva8zP9Sl5jvUFXpjnv2HMkgW1TAoyZj-ujFUV1I1JNTyjsbLU0mN62w6Vqfi8_0WFv9Lwf2TSBSt84mydQYAINmrqhGhxUtBtxvKFFYGMQGGRYy8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DvmDaJTf80p1YtAocwYjpfK50iGrdUw-L95WKywX3c7MyYyvsYUgTsq1ApVqPkFz1Un-K078jj52asGfXlvFwuF8nhTUf0y9t12rPy-4wKuWrFKjyCU3HuVH6eb5xsLn_hl6BMc4yFFYFgK8FLC7ZAR62OMHspi5-tGUelbUuqedB2EeFG0f9FdJf6YFwRfn1nlJA8guiQSGHkYlpbY67jHAK_HyU2IQUEFGEeV9NfNWOVnhtsLIDXp-RxDoxV7BXJHH_1ElVvO0g3J96harIEpCTzmipNK1oWqWSjGfajD8YPN3Fwz-KcMxNsF2TDfkHrZXKIo_0ve79xMDiywoZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف در واکنش به حمله اسرائیل به بیروت تهدید کرد پایگاه‌های آمریکا هدف قرار می‌گیرند
:
mb_ghalibaf
رئیس مجلس شورای اسلامی که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوها با ایالات متحده است، در شبکه ایکس نوشت که محاصره دریایی علیه ایران و «چراغ سبز امروز آمریکا» به اسرائیل برای حمله به ضاحیه «پایگاه‌ها و دارایی‌های آمریکا و رژیم در منطقه را به اهداف مشروع تبدیل می‌کند».
اسرائیل ساعاتی پیش اعلام کرد در واکنش به حملات حزب‌الله به خاک خود، مواضع حزب‌الله در حومه جنوبی بیروت را هدف قرار داده است. از سوی دیگر دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرد که قصد دارد نیروهای آمریکایی را تا زمان «تکمیل» روند توافق با ایران در منطقه نگه دارد.
قالیباف در بیانیه خود ایالات متحده و ‏اسرائیل را متهم کرد که «نه به آتش‌بس پایبندند نه به گفتگو باور دارند» و افزود که این کشورها «با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/75991" target="_blank">📅 20:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75990">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AoOvJ_JULF2ldAidsVihWE45kATrWLjRiTN7CkLhl1SKIls9VEWyCqcLJwzcbLXlprN2QeRID1VatRUi29v8rWoPbfC9jae0cORtI16-Oe41WDSefGSlTUyDeL9ktIgxnpKfE8WiiuDlLnXzsXh83RYOlsFloBxUkxEa5ShbXwaY40v-Hv6RfhzUg0GXHYJhUnCmcuql58ASSDvL9UZsbS53H2nr4S917nH7LvBKSkArzeUzAYgE0vxol9tQ4w6sCXCa1wSH3oU7i38G4bAo3NF01dIjAq1jZ89yy78F8m-Ux9FkFfO25QK9oIpmLI_J-hFSEC2R_PFNTfy9YZcvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی: امشب به اسرائیل پاسخ دردآور خواهیم داد
توییت سخنگوی کمیسیون امنیت ملی مجلس شورای اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/75990" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75989">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0y7FTCUDCn1ig3VnvnECeBhRYjIASGxsXUH2o7jPoboyMKaD6UTO7RGT1PS658fyyKdMC8fT2mg8vSY45vxKswLHf-FB7Qan9VqSpnVHzuI3puFyVvJHw3A3luuUA9wtlqFixWL_u8kRBTLVwObBrBnPqIupBR_DraBk2OTiLJo7Z6AkYkcCG2829W8-thC6Q9YkI5ESaWrID1fAPcFByCtTMWzbVM8kBkmtWhmIr9B362bqAAhRTD4eC-0o_Dja-KN9mXgkQuwcAP994i2O6myVqZaIhpuqGlK9X05K_opdK06eoYlamPUPGFip6NVnloBhaU8HcW6akZiASBOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«وحید هاشمی» ۲۶ ساله و تبعه افغانستان، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در خیابان ۲۰۲ فلکه تهرانپارس هدف شلیک گلوله جنگی قرار گرفت و ساعاتی بعد بر اثر شدت جراحات جان خود را از دست داد.
به گفته نزدیکان، گلوله جنگی به ران پای چپ او اصابت کرده بود. وحید هاشمی حدود دو ساعت پس از تیراندازی به بیمارستان تهرانپارس منتقل شد، اما به دلیل خونریزی شدید جان باخت.
خانواده وحید هاشمی پس از ناپدید شدن او به جست‌وجوی او پرداختند و سرانجام پس از شش روز موفق شدند پیکر او را پیدا کنند.
پیکر وحید هاشمی در تاریخ ۲۴ دی‌ماه در قطعه ۹۶ بهشت زهرا به خاک سپرده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/75989" target="_blank">📅 18:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/awabjxhFT0cz5__h9-CrCfvlXZ6Rp-joIAEkFdlB0DZ31ByUf_FA5g3RNK3kPxbs1zsJHbBgstmiBnqaNVyufQQrR_4UsFYIY2XC2hv_09ZqZV66U8jZi426d0QiUOIeBUlz-JAyBpzV3SivfX24r3t9Yu2XbTOgbXXCwYFKjvvCs5cVXNgFv9gu22PU-i_T27C6sujlNHLmClmrWCIi1qSRPPTrgbPhcA9btC9LHW2OzKpAOY6MmuDkplgVBVYpthKLrx_EbXdKH2qNn9FYykgco9DLImj_zdWYwJNP13-bHNMUPLddOI0nGyIuax_9qACiBDFM3Bq2Pw1Ehm_uJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fgh8ak7i2HwvosRdsy3bj1bXCRsCpB6Ybw1TtuBk9iOypb0RTyJ5HroqZZnQN1UT0SrBZvNsMexcqvkR2zclpmZetnxfTuMQTuQAkH6JtjcxYJ6ZGUDRf8zwa5tWjFjMEVtz4Gi-2Z6eBEvhpvZARavwsdvJvnRX1vYGtMJ7t5pqPa_dCSIT7Z2FTQJ-jH1DpM7MD5jdKq75OWsYCmpyhScUqUXTQy0kOhaBI-wo7Ubxp4Lc_s2filqNPZ5UY2rd3y_G-2jJcQzLD8cMvBNFtY1-JTQHLKvo26ZluSTS_6BcTuFDoInTNVD7DtJRhuaGBU4mOlafgeRWAvEyEPa5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aYd1MhtHIzD0Q0D9zzrVWAdc-u24Ug7M_pEOHU_LSLLvzHntVlFph5sa4958JYszxBq6Ibnc8kD02oGOUaL_4b-9c18jpjmYFUODHVr5vRi5lLNqq7FLmuwNa-FXCdgYFK2doqS5vrA4krW52AidRkirES8mNHz3zueW5SCLtwIIfNRkBrXMlBQV_f4fLu4FeKUUPIDju3ZVrpkkvnXPZgkdNxLSCpi6EU4TOvtJ9hIe6pddCXFW0QmDfV1KQ6NnvJiE-piBfdfdvNJGjnBhSuaW6a6mEn-S_g0ScYRalpNdm31veGUBgd33AVXPjET8l63KO-VS0V2xlZB8ux9ZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/poojeyx9qDZYZlNs5DqyN4c1TbmmWedj_QyTyhJaoLVS5ZLpk_Lo-tElFrvPaCWuN3AKzSKkVBo3qGlvu44bCMn7B8r56WuYU_sKYJqFdhjBSWW6mhIOhhUENKJXXrvST0kdVCLUH0BsvKjHjodyD-cEnXbcDD9Zc67eZxYPSQ5xSHzm8S1Dm5KL4pCL-qvyIVLRfzCJrm7Ta3vnbeaHEb40FwIzxV1254smdZhKNAtVh7C136tNLQFOqwADa0VI0gMA0vT5hn1MReIUk1vDCq1r4gATDVBrMnpsL3BIpBv6U8W8QTKQKby_jcIQnex0z1y-sDVTfDSk6CyFdxHqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K_451NI4MpCXCsHg-Qblj15RhQro7VD1q4ml9GW9E_Z9iC8mcc9e4hWZCWiDUejuCKAYmfm4oeMXjzgXRsSkEwQkBsDHf7g8KMem_Xsda2csie6MBxJ13mlTunDoIjiV6T76hZ4znjLZVxILKdr9iPka3X_0xqmyv5F-tJ5FL5YU1aKL-wENLbnLfQIqW6ocCeqNcz5gR8wyLYcc5X6sQqeErSwyhqmzAtWAmJUhHSjfnDXeeLc5RXv0vAubzBS9sfQu1or6gCXHG1mvogN-y7-3VwegDyQ89p9cprC28pYnIIVpOy360Lp32G1Rb_O-GT0ctV1HI7dCT5wMckfs7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ: پیش از نهایی شدن توافق، دارایی‌های ایران آزاد نخواهد شد
دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
او افزود که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: «بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.»
رییس‌جمهور آمریکا اضافه کرد اگر بتواند با تهران برای پایان دادن به جنگ سه‌ماهه میان دو کشور به توافق برسد، آمریکا با ایران برای جمع‌آوری و نابودی ذخایر اورانیوم با غنای بالای این کشور همکاری خواهد کرد.
او افزود در صورت عدم دستیابی به توافق، واشینگتن توان نظامی جمهوری اسلامی را بیش از پیش تضعیف خواهد کرد تا نیروهای آمریکایی بتوانند با امنیت کامل این مواد را خودشان جمع‌آوری کنند.
ترامپ افزود که خواهان اضافه شدن بندی جدید به توافق است تا ایران نتواند با خرید سلاح هسته‌ای یا تجهیزات مرتبط، محدودیت‌های توافق را دور بزند.
او گفت: «پرسیدم اگر آنها خودشان سلاح هسته‌ای تولید نکنند اما آن را خریداری یا به هر شکلی به دست آورند چه؟ من می‌خواهم در متن توافق عبارت خرید، تهیه یا کسب سلاح نیز گنجانده شود. آنها نه حق تولید سلاح هسته‌ای را دارند و نه حق خرید یا دستیابی به آن را. تهران در ابتدا کمی با این درخواست مخالفت کرد اما از موضع خود عقب نشست.»
دونالد ترامپ، رییس‌جمهور آمریکا، درباره مجتبی خامنه‌ای و محل اقامت او گفت: «او به‌شدت زخمی شده است. نمی‌خواهم بگویم می‌دانم کجاست یا نه، اما احتمال زیادی وجود دارد که از محل اقامت مجتبی خامنه‌ای مطلع باشم.»
ترامپ همچنین اعلام کرد فعلا قصد خروج نیروهای آمریکایی از منطقه را ندارد؛ حتی با وجود آتش‌بس شکننده و ارزیابی او مبنی بر اینکه توان تهاجمی و دفاعی جمهوری اسلامی به‌شدت آسیب دیده است.
او افزود: «هزینه نگه داشتن حدود ۵۰ هزار نیروی آمریکایی در منطقه بسیار ناچیز است و ممکن است برای اعمال فشار در مذاکرات به آنها نیاز داشته باشیم».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/75984" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f1a01266b.mp4?token=hvmfqOIauQZsFCGJ8NliMYLzRboM0NncEwAYyR7ZOTZJ7lIZr9GHc47nc5DZ-Zeh_PTtsaIiPPZ0eaqAQ-BzLmiUYaJ3F7wCqThDnOGIVeeD4YI5Og6rq6cfs4MUz-E70fUchlZCvk_yMGrUOrTVB-jztSTlyew5ADepwErzbrg-kjX6L6Z56x-EN88dVV2f61G-OVIaGmLbwOkKqSdpbHpddH7g9tSDAxl53cr9ecX5RK2wj6W8es_6etQ5y0DaWFsBKLGYR5IFP0ZFzh1flFb5dCfp5qKVWp2oefyGRFhXUZjh69AqnCaCAZcnEs-L0CTZDEpRZOEs8sP2ym8dZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f1a01266b.mp4?token=hvmfqOIauQZsFCGJ8NliMYLzRboM0NncEwAYyR7ZOTZJ7lIZr9GHc47nc5DZ-Zeh_PTtsaIiPPZ0eaqAQ-BzLmiUYaJ3F7wCqThDnOGIVeeD4YI5Og6rq6cfs4MUz-E70fUchlZCvk_yMGrUOrTVB-jztSTlyew5ADepwErzbrg-kjX6L6Z56x-EN88dVV2f61G-OVIaGmLbwOkKqSdpbHpddH7g9tSDAxl53cr9ecX5RK2wj6W8es_6etQ5y0DaWFsBKLGYR5IFP0ZFzh1flFb5dCfp5qKVWp2oefyGRFhXUZjh69AqnCaCAZcnEs-L0CTZDEpRZOEs8sP2ym8dZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز یکشنبه اعلام کرد که ارتش این کشور مراکز فرماندهی نیروهای مسلح را در حومه جنوبی بیروت هدف حمله قرار داده است.
در این بیانیه آمده است: «مطابق دستورهای نخست‌وزیر نتانیاهو و وزیر دفاع کاتز، نیروهای دفاعی اسرائیل دقایقی پیش یک مرکز فرماندهی نیروهای مسلح را در منطقه ضاحیه بیروت هدف قرار دادند. این اقدام در پاسخ به شلیک‌های حزب‌الله به سوی خاک اسرائیل انجام شده است.»
این نخستین حمله به پایگاه اصلی حزب‌الله از زمان برقراری آتش‌بسی است که روز ۱۶ آوریل با میانجی‌گری طرف‌های بین‌المللی حاصل شد. آمریکا هفته گذشته اعلام کرد دولت‌های اسرائیل و لبنان به تمدید آتش‌بس به شکل مشروط دست یافتند.
حزب‌الله، گروه مورد حمایت جمهوری اسلامی، پیشنهادهایی را که برقراری آتش‌بس را به خلع سلاح این گروه مشروط می‌کند رد کرده و تأکید دارد که اسرائیل باید ابتدا حملات خود را متوقف کرده و نیروهایش را از جنوب لبنان خارج کند.
ضاحیه محل اصلی استقرار فرماندهی و نیروهای حزب‌الله است. این گروه از سوی آمریکا تروریستی شناخته می‌شود، اما اتحادیه اروپا تنها شاخه نظامی آن را در فهرست سازمان‌های تروریستی قرار داده است.
ارتش اسرائیل ساعتی پیش گفته بود دو پرتابه شلیک شده از لبنان به سمت خاک اسرائیل را رهگیری کرده است.
ایران که در حال مذاکره با آمریکا برای رسیدن به توافق پایان جنگ است، پیش‌تر تهدید کرده بود در صورت حمله اسرائیل به بیروت، جنگ را ازسرمی‌گیرد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75983" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9915e8c302.mp4?token=bHPdBYSm0Dlq8w0aqapnYritTyfYBCIOCNPRre80DKxmqEDwc9xg8qjRGMNZeINtxwf9hGs8AWdIcYjFRpGasQ1ySm0Hho0QfngNLUVaG4PTr-VxH67a-2KKgN03kS6meMBxacIMXfp0A8a7n5u-pAthId5QnZrW4bRuRUiJdOAx4IeMl50Y9vXpkhjB_L14K2omqnMendpO5pEX4BobRXpJHEd5v3lcbkMU2DQd5-O5RyJ13rHmiN5iCf-xv1MILjduQwCMtt6BoeW3wZhSCtMoXncrK9X0OlHeyM4Sw15wXcsx6YKv0BJfU9XIeezxQgo6ZbrtE8omOVTMAen6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9915e8c302.mp4?token=bHPdBYSm0Dlq8w0aqapnYritTyfYBCIOCNPRre80DKxmqEDwc9xg8qjRGMNZeINtxwf9hGs8AWdIcYjFRpGasQ1ySm0Hho0QfngNLUVaG4PTr-VxH67a-2KKgN03kS6meMBxacIMXfp0A8a7n5u-pAthId5QnZrW4bRuRUiJdOAx4IeMl50Y9vXpkhjB_L14K2omqnMendpO5pEX4BobRXpJHEd5v3lcbkMU2DQd5-O5RyJ13rHmiN5iCf-xv1MILjduQwCMtt6BoeW3wZhSCtMoXncrK9X0OlHeyM4Sw15wXcsx6YKv0BJfU9XIeezxQgo6ZbrtE8omOVTMAen6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کشته و دست‌کم پنج زخمی در تیراندازی مرگبار در اسرائیل؛ دو مهاجم کشته شدند
ارتش اسرائیل اعلام کرد دو مهاجم حمله تیراندازی روز یکشنبه در مرکز اسرائیل، پس از عملیات نیروهای امنیتی کشته شدند؛ حمله‌ای که به گفته امدادگران، یک کشته و دست‌کم پنج زخمی برجای گذاشت.
این حمله در چند نقطه در نزدیکی حصار امنیتی کرانه باختری رخ داد. امدادگران اسرائیلی گفتند قربانیان در سه محل جداگانه هدف قرار گرفتند.
به گزارش تایمز اسرائیل، یک مرد ۳۱ ساله که نزدیک تزور ناتان هدف قرار گرفته بود جان باخت و یک مرد حدوداً ۴۰ ساله در وضعیت وخیم به بیمارستان منتقل شد. چند زخمی دیگر نیز با جراحات متوسط یا شدید به مراکز درمانی انتقال یافتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75982" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9PsobPjys87qPVOFvFoCpOLcB60U_4_OpiwM3e6iNdr-itGK-rvuqDk3R2bQp2UFrORqx7ra4k17EB7isqGSm98efyZJLRadPN_ycBxTuoDfUIiGzjSEzjcjVZTn6RguqOI7lp6MuGmnLL7QEaqmmnJrD-n_qC15y0ygLyI0hijaEarefGxpTPLK8lQXunwcgY0M-g-iNnf1PP8YFqKHxrguhgiMksruZiDRcdqMFJrvGfAvauAfY-gaPJPcVCLybcG6inoPMdWJoOYwHgoyeMPKYUzthSxuYbrBDorTd9ugo2ZQIoRg-Ykp6igZbY_G8tmbW8UW1ZKv8zi5cMpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان که حامل «نامه‌ای ویژه» از طرف ژنرال عاصم منیر، فرمانده ارتش پاکستان، برای مجتبی خامنه‌ای است، روز یکشنبه  ۱۷ خردادماه آن را به عباس عراقچی، وزیر خارجه جمهوری اسلامی تحویل داد.
خبرگزاری فارس، نزدیک به سپاه پاسداران، روز یک‌شنبه، ۱۷ خردادماه، ویدئویی منتشر کرد که وزیر کشور پاکستان در آن می‌گوید حامل «نامه‌ای ویژه» از طرف ژنرال عاصم منیر، فرمانده ارتش پاکستان، برای مجتبی خامنه‌ای است که به عنوان جانشین پدرش، علی خامنه‌ای، معرفی شده است.
در سه ماهی که از آغاز جنگ و معرفی مجتبی خامنه‌ای به عنوان رهبر می‌گذرد، نه فایلی صوتی از او منتشر شده و نه ویدئویی که نشان دهد او از حمله مرگبار به بیت پدرش در روز ۹ اسفندماه جان سالم به در برده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75981" target="_blank">📅 17:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWYdsQz49DjUHIDPm-hCmPpFX8SHV5bY5XmJ0oPVw_AfZYShu7bg00fGHIoFWnbJc31eY30blzO03jaG8IGwmW1QZj0A6YsQLu8_jfd0Es2HXk9FV-xvYNOSG88TZBJIWQrPS8FCLTPOCB_AZHWL7PT43Wi3AN_hNEhS73C80-PGBOM0iFTC5xTGEI-Imz0HyVbBmMOlvavHZrGRjCNLa5FS-EQsEjNHhfqOl8e0khTHrjSNcXL8egpXaj1h8BkexxMo0m7ZByKbWfNArZBs03UX1y9-yUGDIkfKZ5qMhYrUXNfGo1FVLIywbOKFr9cDkVnS9DU29WrlqEoBR3WrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف برخی گزارش‌ها درباره ورود و خروج تیم ملی فوتبال ایران به خاک آمریکا، رئیس فدراسیون فوتبال کشور روز یک‌شنبه توضیح داد که تیم ملی یک روز قبل از هر مسابقه اجازه ورود به خاک این کشور را دارد.
پیشتر ابوالفضل پسندیده، سفیر جمهوری اسلامی ایران در مکزیک، گفته بود که بر اساس شرایط تعیین‌شده برای روادید اعضای تیم ملی فوتبال ایران، بازیکنان و کادر فنی تنها در روز برگزاری مسابقات خود اجازه ورود به خاک آمریکا را دارند و باید همان روز این کشور را ترک کنند.
به گزارش ایسنا، مهدی تاج که خود نتوانست ویزای آمریکا را دریافت کند روز یک‌شنبه همچنین گفت: «واقعا عجیب است که اینها تا این حد در حوزه اداره فوتبال دخالت می‌کنند. این کار نادر است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/75980" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtj3QkSZtbSheQAaiqJYjZdOeHK8_4jUi_l6fu0eWw35r0SgvQ9fofSAtiHel_lU9eMdeZreJ5a26L7lhKw-IGJ3nuHp3X-4vx4FbA66EL6lmCmwVSgY4sFU5g3NzVZmHNFJWMLCabQo-8IOWzeMmjMECafg5l4CEU6IA8MlbMAdk8CPQLQGK1bOtvPtV2aNuo6j81xarhn8Lwr4-RUH1xXAAfe1IQyVIVJUGvLztfHlZawhsLlIZ6QeyubaD1jEVp83ehPTFNuLj6bmOwB9u7NYZhyqM9gP3HeN7sAWuAXnlFax2qMSAAxbDcr6-VnA3P-nK3EVngWMq0fQGLwmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون، روز شنبه ۱۶خرداد ۱۴۰۵ در گزارشی درباره اجرای قریب‌الوقوع حکم اعدام پنج زندانی سیاسی به نام‌های مسعود جامعی، علیرضا مرداسی (حمیداوی)، فرشاد اعتمادی‌فر، حسن مصلاوی و رضا عبدالی هشدار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/75979" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gSdV9VrZBGZABdzPPrinlVCpba73Qv3IYCDOZ3FF0IVFq_mQpAIwG-kugua2_Pyx08_vJElvc3U9GTPCKH5Og1Iin0nf0Rx2dCaLSI6vFVLZ7iD_l7v-9SKNqg1u41MG2sjRo7WZgsCuQqM8N_xZNmvk8LmK_oWs0r1C5wiK44Ga4Qti9DM3BykMvfnhrcuJT5xF4nKj0lhCBKxmBfjPEWgTxb7UAvWfO1wlbnK-_oHVwFH-wl8ugbC5RWaLrmTEsKYPl4N1wxIB18Uh6JPZTBPUmMP8voizCN9Z8kvO63YUs9klR46rDAIBON8J-PY3ezSNsFxyV-VLCgpeuDxH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، شنبه‌شب به وقت واشنگتن در بیانیه‌ای گفت اوایل امروز، نیروهای ایالات متحده در خاورمیانه دو پهپاد تهاجمی یک‌طرفه ایران را که تهدیدی برای تردد دریایی بین‌المللی در تنگه هرمز محسوب می‌شدند، سرنگون کردند.
سنتکام افزود که نیروهای آمریکایی همچنان آماده در برابر اقدامات تهاجمی جمهوری اسلامی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/75978" target="_blank">📅 05:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCuLoieggzEociSn4NVVMyC_6DS9COkZtVVOJKenj1HkYKD-lX7J-be4DIHWztDhpaIdYGcq3MDVaNWAeODj_WQou2e57RhUW8216pl7GE6hX5OI-q0nOix8V8nnVJQv3Epq2frhra2k1TvW1yEpdGHRkFoCo3ZKTsNj-FiJbqlabJtOPlMhh1SS5UBaEHFXxaxnoE0VCFQc61HUhyqkiTEdnzIKjR1xZkpwt2Gb0iY2l0gcCmz1TIRrGLCfIf2xwdvH-WG4aNJ4IhSOD2tNZXqxfcFWcbL4ajskFU5bzX90N5qBZM8DTRoSmp-IDoyBc4Ffb6NCrSvrWKwbqpo68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فرانسه گزارش داد، ابوالفضل پسندیده، سفیر جمهوری اسلامی در مکزیک به خبرنگاران گفته است بر اساس شروط تعیین‌شده برای ویزای اعضای تیم ملی، بازیکنان و کادر فنی تنها در روز برگزاری مسابقات خود اجازه ورود به خاک ایالات متحده را دارند و باید بلافاصله پس از پایان بازی، این کشور را ترک کنند.
این محدودیت سخت‌گیرانه در شرایطی ابلاغ شده است که کاروان تیم ملی ایران روز شنبه، تحت سایه یک بحران دیپلماتیک شدید میان تهران و واشنگتن، اردوی تمرینی خود در ترکیه را به مقصد مقر جدید خود در شهر تیخوانای مکزیک ترک کرد.
براساس این گزارش، با توجه به اینکه هر سه بازی مرحله گروهی ایران قرار است در خاک آمریکا برگزار شود، این اولین بار در تاریخ جام جهانی است که یک کشور میزبان، پذیرای تیم ملی کشوری می‌شود که با آن در وضعیت جنگی قرار دارد.
این دستورالعمل جدید واشنگتن در تضاد کامل با اظهارات قبلی امیرمهدی علوی، سخنگوی تیم ملی قرار دارد که پیش‌تر مدعی شده بود ویزاها «چندبار ورود» هستند و تیم یک یا دو روز پیش از مسابقات به محل بازی‌ها خواهد رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/75977" target="_blank">📅 02:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75976">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oaBpzjodvLKQdLFWCjlNQ5UwmMUIWaG3uJqOznHMFxmZYNbIlfCm9HmngSbCZLwcjkLQJnYqr5En0RJzoAKQLPRN0Ft2KVEkNptsumxcFA2hCFqILaF0ltzsiUyYXZKbdL7MM52THI20znKJlKropdQ_PCiWwNM3EW7n1LbHGbpQLXo5ZIa8nxQ7-OWDX55akvpx7gj7bSJ9tlKq8ItR_fPrgddx_7-PTPanqcl7NUgfR84PlPiTPMI9qyPYfSsxIwsjtbyZlYQncdhtullONoUpX6AfdgYdmhvDqiDrUjOkiIE7mp_bbSOLwDiQ6DQUfOSaudzQ5-hnHWC1nu-Zgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از منبعی آگاه گزارش داد که آمریکا در حال بررسی تحویل دارایی‌های بلوکه شده ایران به کشورهای خلیج فارس جهت بازسازی و جبران خسارات ناشی از حملات جمهوری اسلامی است
رویترز خبر داد که وزیر خزانه‌داری آمریکا به تیم خود دستور داده خسارات واردشده به کشورهای خلیج‌فارس در حملات جمهوری اسلامی را بررسی کنند
رویترز به نقل از یک منبع آگاه خبر داد که آمریکا دارایی‌های ایران را برای حمایت از بازسازی و جبران خسارات آینده ناشی از حملات جمهوری اسلامی را در اختیار کشورهای خلیج فارس قرار خواهد داد
رویترز به نقل از این منبع نوشت که آمریکا همچنین بررسی خواهد کرد که آیا می‌توان از دارایی‌های ایران برای جبران خسارات گذشته نیز استفاده کرد یا نه
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/75976" target="_blank">📅 00:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تسنیم،‌ منبع وابسته به سپاه:
"روابط عمومی نیروی دریایی سپاه: صدای انفجار شنیده شده از اطراف جزیره خارک مربوط به خنثی‌سازی مهمات باقی‌مانده از جنگ تحمیلی سوم در منطقه بهرگان است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75975" target="_blank">📅 22:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75974">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C53DqE8Dd-oTuYH__bdIXdp-cVEa4JpFKxwRjqL_1njo1cvCGvrufQOl_TPsu4mxNAwmTHkJnG_eJhnawvg8LqRnoGJI4f5atDGPktv9_o2rBhFsQR8q7Uf54J_SyPIAsFFq2ue6_NJ-22Uimzh_Zj4ByZGjSvo2UY9tdNJ38WaFfuUN4pzdALrYXQgbC90CipYVuvEvTAfx-c0LfNk_GOG_WEqSM8czAlqfNl2FGgV8_5x1IbL3R7Ish2Tfp_uXEf0kCON2r9rP41cJxL9pflVCgnKuWg1_Nd_Q2B3BF3Aqiu_a35-i5sSMWzEzTbt7uBgldMLbWKxB8r-cACNBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد خاتمی، عضو مجلس خبرگان، در دیدار با اعضای شورای اداری شهرستان سیرجان با اشاره به وضعیت جسمانی مجتبی خامنه‌ای، گفت: در جریان حمله روز نخست جنگ، او از ناحیه پا دچار آسیب‌دیدگی شد؛ به‌گونه‌ای که احتمال قطع پا نیز مطرح بوده، اما این اتفاق رخ نداد و او هم‌اکنون در سلامت به سر می‌برد.
این در حالی است که از روز ۹ اسفند سال ۱۴۰۴ و حمله به دفتر علی خامنه‌ای، هیچ تصویر یا فایل صوتی از مجتبی خامنه‌ای منتشر نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/75974" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IJXw9rB5G-rX1GMjTO8h9tes1AHUeEjdrdA9nOzjlIjNOJ5vWUKJTb4QrC4cb6Q9IQ10HpVD-KssEzlBfUiiC4xbT96gFM_HAxQmFgIpQO3TQW9rSwFJp4VPFQSo5LcHLtw_HaieVaPM6Xrd6QFXazjm_CxeTqNaxbnoAA46bihgT6-2vuILbd9_WZ6Oi6FAwneT1KpHsZCQfNnF34j_1n6IXZjkSXBFWDSmB2B4FEGcx-DSW-kMmvYqkG5KDDZxWn3M49bn5ZQBZU4HTfGbonn4mYuQ3hROFL3FBVb-Te0NcwPn49WqYfEQI5-Mw88dyzzK92AIIdMfWG7GaYbvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایسنا نوشت که محسن نقوی، وزیر کشور پاکستان، در جریان سفر به تهران حامل پیام ویژه‌ای از عاصم منیر، رییس ستاد کل ارتش پاکستان، به مجتبی خامنه‌ای است.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز شنبه ۱۶ خرداد ۱۴۰۵، گزارش داد محسن نقوی، وزیر کشور پاکستان، وارد تهران شده و قرار است با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار و گفت‌وگو کند.
بر اساس این گزارش، نقوی پیش از سفر به تهران با شهباز شریف، نخست‌وزیر پاکستان، دیدار کرده و در جریان این ملاقات، دستورالعمل‌هایی درباره سفر به ایران و روند رایزنی‌های مرتبط با مذاکرات جمهوری اسلامی و آمریکا دریافت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/75973" target="_blank">📅 20:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XQozMp8DxRKAQpRZsfs3hR6f3fUxqrlwq_eHIcIj_k6WU6yWooHG5dEw5_WjawGE4jHQrMrepfibZVyoro8QHM4TNFGJyoYr3MtwzWVRJoktnXxmi4HsmBycX4YX_fJ-DB9i8FCw5wKSjTM7ZXxcnxuUp9mfUbw3RDicfBgMF_amR4vSHvgSMFfeRkdYxdlAr8u5xfe2WgS1j_miyNL88RjQ12eW6rAtKoAZlloFTB_RxZxNRiXSTI7NPDaqvKkTz60z4_Nt_ID4KP_W3RGqQoRTi2gpapRi6Un6Tmgo6Ww96sgZejaMzO2nLPAOcqwF6ljTsEgk7zzRYrbgsNFOjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول مسعود پزشکیان، در بازدید از دانشگاه علم و صنعت گفت: در جنگ‌های اخیر شاهد مهاجرت معکوس نخبگان و مردم به کشور بودیم. باید از ظرفیت ایرانیان علاقه‌مند به خدمت به کشور استفاده کنیم و با طراحی مشوق‌های مناسب، زمینه بازگشت نخبگان و استادانان را فراهم سازیم.
او افزود: نباید دنبال این باشیم چرا استادان مهاجرت کرده‌اند، بلکه باید به بازگرداندن آنان بیندیشیم.
در روزهای اخیر، بینش بلور، معروف به قصیر، خواننده لس‌آنجلسی، با حضور در تهران در تجمع حامیان حکومت در میدان انقلاب ترانه اجرا کرد.
همچنین صدف طاهریان، بلاگر ساکن ترکیه، تمام پستهای صفحه اینستاگرام خود را حذف کرده و با انتشار استوری‌هایی، از حضور خود در ایران خبر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75972" target="_blank">📅 20:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKrZlmoThM-W5HOttifvHzk76UGejGE03Bx7l5k7nXZz3gFsSxPtZyv5_mdoXlF2LhYVO5gyWYOperaXGiG60jztRn5fpsobvcBGd0aac80Dy0cFCVJXDPXOx_kZjA1VEluDc67LS3su4vooh4XzUdP2HbbahLjFbfRlod_eswBLx4gbogph-3OqonvNGstCtgIXjlzM56nS7mjs5Tk2L-1Bs53eTP0cnBVgVzV13JFns5A99HqWf0ze6CKn4JWwko4Pa1vMzIzQlXPHHWMkNxlW32FW-MRvm2idTJGvjN1nIJlR-282NBtxYfbCB1RaUmjBi9cUd6j7S5Ktg_JkHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی در بیانیه‌ای حمله بامداد شنبه ۱۶ خرداد ۱۴۰۵ ارتش آمریکا به تاسیسات راداری و نظارت ساحلی در منطقه سیریک و جزیره قشم را «نقض آشکار آتش‌بس» و «تجاوز نظامی علیه حاکمیت ملی و تمامیت سرزمینی ایران» خواند و آن را به شدت محکوم کرد.
در این بیانیه آمده است که تاسیسات هدف قرار گرفته، ماموریت حفاظت از امنیت مرزهای کشور و امنیت کشتیرانی در آبراه‌های بین‌المللی را بر عهده داشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75971" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OXh6Bn5oYv_6ZGOEUNWUp28hBlAr0ZdcvtquM4OuQOkSK_vLBpE8bbUEM3ZPCjtzPKrZCmKjGYQcgnKV8PndEbv58mLo73VYTzMdLrIgHTh7WtPKCF7s3Qh_93vPLodWxZn_c0y8YgyKgEcfgi7F_Wx1ALRjk1KhLaBpzPmGyld1P1YWeWGex4z8fQSMWpvp2u9thrmyMmyENY1JmoGR1z8AV5vWj1cLXdUrDcWnD4ePFCmSBYN-M-fhtRKLPSoI9yj2fLNYseLeS0musC7aLfuByJpDbt3NWx5iskFh19JAsAFSZe_7fWhDH6t8-0kgXu8enHUFw909_QqS-YnEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lXy-ZW2pxT_HFt-KcqZ8PG9zfILLRhXq1laojyRIMUqWO8H-4xdNDVumej3_VJWFgvVzpYjDCS52WFrSHpgElk1WOJ7Hq_8m5CWtx6qPf-duKsToaO_PWcpXGX4s_HsFCne8Ejih2mBsgdcMpPUfPP5a-yDRnsSB3sHkbqDyBd7-LXBC5t--VEQSNXR8gd-o8zxyTYGZ1DoKmAXIUaHs0r9gVDWfVwQ35ATu92GgCL0WwIYZNLLcUY0ZBsktEiNSeB5Z00Ou7dOx5lXEJVBeyJmlfe38NPWGaJk90vYTBAM1z7owptj8PbHqr2PB3R9Bb2h8MghfjwjaGNqzYRoFxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز جمعه در شبکه ایکس در پاسخ به انتقاد صریح مقامات عالی‌رتبه لبنان تمام تقصیر را متوجه اسرائیل دانست.
نواف سلام، نخست‌وزیر لبنان، روز جمعه، ۱۵ خردادماه، در یک نشست مطبوعاتی با لحنی صریح رهبران ایران را خطاب قرار داد و گفت: «به جنوب ما رحم کنید؛ از تبدیل کردن آن و مردمش به یک برگۀ معامله دست بردارید.»
ژوزف عون، رئیس‌جمهور لبنان، نیز در مصاحبه با سی‌ان‌ان پیام مشابهی برای ایران داشت. او گفت: «اینجا کشور شما نیست، کشور ماست. مداخله در کشور ما وظیفۀ شما نیست.»
در پاسخ به این انتقادات که مقامات لبنان ماه‌هاست با صراحت مطرح می‌کنند، عراقچی در پیامی نوشت: «اگر لبنان ابزار معامله برای ایران بود، خیلی وقت پیش به توافق رسیده بودیم.»
وزیر خارجه جمهوری اسلامی در ادامه خطاب به عون نوشته است: «آقای رئیس جمهور، لبنان را از دست دشمن واقعی‌تان نجات دهید.»
عراقچی در پیام خود می‌گوید: «بر اساس گفته‌های آقای عون، هر کس باشد فکر می‌کند که ایران است که یک‌پنجم لبنان را اشغال کرده،‌ یک‌چهارم مردمش را آواره کرده و هر روز کشورش را بمباران می‌کند.»
@
VahidHeadline
ساعاتی بعد نیز اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، در پیامی به لهجه لبنانی نوشت: «بیبیع اللی واقف حدّو، وبیشتری اللی واقف ضدّو»؛ عبارتی که به معنای «کسی که کنار او ایستاده را می‌فروشد و کسی که مقابل او ایستاده را می‌خرد» است.
رئیس‌جمهوری لبنان همچنین خطاب به ایران و سپاه پاسداران گفته بود: «این کشور، کشور ماست نه کشور شما» و تاکید کرده بود که لبنانی‌ها از جنگ خسته شده‌اند و خواهان زندگی در صلح و ثبات هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75969" target="_blank">📅 19:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04b6cd8529.mp4?token=h0YRv1vfhMSxEU9lwwcMWhZ7LclbdGGr3Ku-hegp5nD4u1GE6Kplv3MYxkN5UV67sT7ITY4uYw-tSP1sK_ku6fq8mD5lo3Cb_da57d_8jS60m-cK3w_ltU9RauXbpFHvxUuADC6tbKLMkuk0Sc1PrmsTuE3pPjTEXwuy65OJPTD-T4XNYXO_6CZknoLNU_4T5m_wMoxSjnZiPNgcI0xXc6TbfB0Q_RLINUfLaC6CR7PST3TCU1juoV7-dc_ZfC8SVpZG9nPVNpbBKsEH2blINkx1d8Z9N4QROu-g2Qko38QRVnBV71zRqPwo9pBupidAWDng6N1WzhBoCeVJX4UlMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04b6cd8529.mp4?token=h0YRv1vfhMSxEU9lwwcMWhZ7LclbdGGr3Ku-hegp5nD4u1GE6Kplv3MYxkN5UV67sT7ITY4uYw-tSP1sK_ku6fq8mD5lo3Cb_da57d_8jS60m-cK3w_ltU9RauXbpFHvxUuADC6tbKLMkuk0Sc1PrmsTuE3pPjTEXwuy65OJPTD-T4XNYXO_6CZknoLNU_4T5m_wMoxSjnZiPNgcI0xXc6TbfB0Q_RLINUfLaC6CR7PST3TCU1juoV7-dc_ZfC8SVpZG9nPVNpbBKsEH2blINkx1d8Z9N4QROu-g2Qko38QRVnBV71zRqPwo9pBupidAWDng6N1WzhBoCeVJX4UlMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شماری از دانش‌آموزان اصفهان روز شنبه ۱۶ خرداد در اعتراض به حضوری برگزار شدن امتحانات تجمع کرده و با سر دادن شعار «دانش‌آموز داد بزن، حقتو فریاد بزن» خواستار تغییر نحوه برگزاری آزمون‌ها شدند.
@
VahidOOnLine
صدها دانش‌آموز روز شنبه ۱۶ خرداد در شهرهای مختلف ایران ازجمله تهران، مشهد، اصفهان، شیراز و چندین شهر دیگر تجمع اعتراضی برگزار کردند.
دانش‌آموزان در تهران مقابل دبیرخانه شورایعالی انقلاب فرهنگی و در شهرستان‌ها مقابل ساختمان وزارت آموزش و پرورش تجمع کردند.
آنها به تغییر قوانین کنکور و افزایش تاثیر معدل در کارنامه کنکور سراسری معترض هستند.
گزارش‌های غیر رسمی از حضور نیروهای انتظامی و یگان ویژه در اطراف محل تجمع دانش‌آموزان در مشهد حکایت دارد.
پیشتر هم صدها دانش‌آموز روز سه‌شنبه در شهرهای تهران، مشهد، همدان و چندین شهر دیگر با تجمع مقابل ساختمان وزارت آموزش و پرورش به تغییر قوانین کنکور و افزایش تاثیر معدل در کارنامه کنکور سراسری باتوجه به تاثیر منفی جنگ بر آمادگی آن‌ها برای آزمون ورود به دانشگاه اعتراض کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75968" target="_blank">📅 19:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5eFd6ugv-CepkT-PBGxfTcgIkDY-2yJvEr0s4l9xYtS3lkBgo3Vps6QGB2fWdnBaHtoFF2t1YhWE8LefcMA4o_BuULj4xeg2lM3zhkWwKoBE3JZ77MOlWnx8hlmTfLLN2x6zu9teOOUhcl6bxGfP0KKryh_1CUUYf8Ws0afCluDIFXj69_dL7SBvJ19Rvuj3bMGc5l-Q7uW0Zvso2vTAtMfzWOGCJ-F-kRHph1i7aIgrq3nhsMMLENf8u5GPBZvhLFaHwDGz9jv2HVKno5eVcPg4bV1o3IFN00NIx2l4sCmkNpGZjb-Py0E2WrJhb_lTVKkFsX4-jg1eCyHzrAgnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«رضا کرمی» ۳۴ ساله، ساکن کرج و اصالتا اهل شهرستان طارم در استان زنجان، در تاریخ ۱۹ دی‌ماه ۱۴۰۴ با اصابت گلوله جنگی به ناحیه قلب جان خود را از دست داد.
به گفته منابع مطلع، رضا کرمی به حرفه ماساژ مشغول بود و در کنار آن به طراحی و نقاشی نیز می‌پرداخت.
خانواده او پس از ناپدید شدنش، به مدت حدود یک هفته در جست‌وجوی او بودند و به مراکز مختلف مراجعه کردند، اما اطلاعی از سرنوشتش به دست نیاوردند.
بر اساس این روایت، خانواده در نهایت پیکر او را در بهشت سکینه کرج شناسایی کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75967" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcQ9jiDOMpU2wHvm1pJoJyw6aDKJdcEp2YDHxBfiyDYFZ-E40vzZEL70kUgzrgot5aFTv3iCiA7c_9FngmokP5j_YMvWsYsgLJQwqxWHquK0yVJShWUsDYZMUtKhB5j7lwi4IM5Efy_6xlCkHZnFG42t8Qs4Ltbb7I6pjxqv1s5utVy1C3vGu3dij2Jojgoc3qaAevNwpwEaxoma9BMZOmbh46gfuyd8YRLbNyxw6aTaVsYMJPv3wU17eJ0LaBDd3kSQlucLdia9-oLmpRF2cKnZGIxHCowAMlLGO_DBlwaQYac10sEHAfMOEZigP78nV6EIfG7Y3bZUhItjXpMm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که بازیکنان تیم ملی فوتبال ایران پس از ماه‌ها ابهام، برای حضور در جام جهانی آمریکا روادید دریافت کرده‌اند، گزارش شده است که درخواست روادید مهدی تاج، رئیس فدراسیون فوتبال ایران، رد شده است.
به گزارش نیویورک‌تایمز به نقل از چهار مقام ارشد، درخواست همهٔ ۲۶ بازیکن ایران پذیرفته شده، اما بیش از ده نفر از اعضای کادر پشتیبانی و مسئولان فدراسیون که قرار بود تیم را همراهی کنند، اجازه ورود به آمریکا نگرفته‌اند.
یکی از این مقام‌ها گفته است روادید مهدی تاج، که سابقه فرماندهی در سپاه پاسداران انقلاب اسلامی دارد، نیز رد شده است. آمریکا و کانادا سپاه پاسداران را یک نهاد تروریستی معرفی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75966" target="_blank">📅 08:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/262f970692.mp4?token=tAi_0vCjEA8AXtSh6xufveusHbk2WhudaN8lVcmoUuecSccvOAt3O10mbDvxL8aaBPvwzBuFJh6niICzZ5HLSxYDqskmBjnPqdV4Ix8rPodPToFSuzCvPS-sMfvLy578e_J0s5U_vYzGeHzuxIiMaKXHo09RlfPDVnsEg3HDTXtdRuP_1RQ2B1xqEKtod4ceREcdoGZc66cuMpoc3-iFASK4a3kDpfL6ZjQ-JDqywFAkFBM6zFm08RotswQmCbtxg5POYVbKI5vl2f4TY_ecLV5NXFukeFGFC4mOdtPYxbki7SgBZv8ouNUY1JPWXyB2Ctf1veje-N_GUZCQ_Xy90g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/262f970692.mp4?token=tAi_0vCjEA8AXtSh6xufveusHbk2WhudaN8lVcmoUuecSccvOAt3O10mbDvxL8aaBPvwzBuFJh6niICzZ5HLSxYDqskmBjnPqdV4Ix8rPodPToFSuzCvPS-sMfvLy578e_J0s5U_vYzGeHzuxIiMaKXHo09RlfPDVnsEg3HDTXtdRuP_1RQ2B1xqEKtod4ceREcdoGZc66cuMpoc3-iFASK4a3kDpfL6ZjQ-JDqywFAkFBM6zFm08RotswQmCbtxg5POYVbKI5vl2f4TY_ecLV5NXFukeFGFC4mOdtPYxbki7SgBZv8ouNUY1JPWXyB2Ctf1veje-N_GUZCQ_Xy90g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده: "نیروهای سنتکام موشک‌ها و پهپادهای پرتاب‌شده از سوی ایران را منهدم کردند"
ترجمه ماشین:
تمپا، فلوریدا — نیروهای آمریکا در تاریخ ۵ ژوئن، چندین موشک بالستیک و پهپاد ایرانی را که از سوی ایران به سمت تنگه هرمز و کشورهای همسایه در خلیج فارس پرتاب شده بودند، رهگیری کردند.
ایران چند ساعت پس از آنکه فرماندهی مرکزی آمریکا، سنتکام، چهار پهپاد تهاجمی یک‌طرفه ایرانی را که به سمت تنگه هرمز پرتاب شده بودند سرنگون کرد، هفت موشک بالستیک به سمت کویت و بحرین شلیک کرد. این پهپادهای تهاجمی تهدیدی فوری برای تردد دریایی منطقه‌ای محسوب می‌شدند. نیروهای آمریکا سپس برای دفاع در برابر حملات دریایی بیشتر، سایت‌های راداری نظارت ساحلی ایران را در گورک و جزیره قشم هدف قرار دادند.
ارزیابی‌های اولیه نشان می‌دهد شش فروند از موشک‌های پرتاب‌شده از سوی ایران رهگیری شده‌اند و موشک هفتم به هدف مورد نظر خود نرسیده است. در حال حاضر هیچ گزارشی از آسیب‌دیدن نیروهای آمریکایی وجود ندارد و ادعاهای ایران مبنی بر واردکردن خسارت به مقر ناوگان پنجم آمریکا در بحرین نادرست است.
نیروهای سنتکام همچنان هوشیار و در آمادگی کامل هستند تا در چارچوب دفاع از خود، به تجاوزات بی‌دلیل ایران پاسخ دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/75965" target="_blank">📅 06:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3uAtuQq-Ew9PlNddP5JZ-gE0KW2b1wTxv5UKOJU0jcsXIAzBitaOC74yjvHHyfyqAUv5RO4WITkRmPZHeXyd6aNflykJoB5MMJYcE6heIlg4Ra8ivoBTBRikjm_dsptZknzSTTJVPNBF9_DWRZ7UDwL8OC4LW4WJ5OyOnoxhhk6YoiBt-l0s-1PL9LrmfDGfI0wJU_e1OeLCZ1XTDftwdWjcOS1v5ZM-TGGNWSW7kZ7Tv0y1V4E9wXIuZGkFFr_YaMWnVPFQI3APOKcj4EzEvqT4PrAwue1QxlqBrd9WhPSVowkvAavE2e1wAJADVLWpWw8C9rUw1BLWGZLIAGCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه، بامداد شنبه، با انتشار بیانیه‌ای اعلام کرد: «به دنبال حملات ارتش آمریکا به سیریک و جزیره قشم، پایگاه‌های دشمن در منطقه مورد اصابت موشک‌های هوافضا قرار گرفتند».
@
VahidOOnLine
سپاه در بیانیه‌ای با اشاره به اخطار خود در ساعت ۱:۳۰ بامداد شنبه به چهار نفتکش که قصد خروج از تنگه هرمز را داشتند، گفت یکی از این نفتکش‌ها را هدف قرار داده و متوقف کرده است و دیگر شناورها نیز به عقب برگشتند.
طبق این بیانیه، در ساعت ۲:۳۰ بامداد نیز پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک با دو پرتابه هدف قرار دادند که نیروهای هوافضای سپاه متقابلا با موشک‌های بالستیک به پایگاه هوایی علی‌السالم آمریکا در کویت و تاسیسات ناوگان پنجم نیروی دریایی آمریکا در بحرین حمله کردند.
در همین حال، ستاد فرماندهی مرکزی آمریکا، سنتکام، در بیانیه‌ای با اشاره به اینکه در حال حاضر گزارشی از آسیب به نیروهای آمریکایی وجود ندارد، اظهارات مقام‌های سپاه درباره آسیب زدن به مقر ناوگان پنجم آمریکا در بحرین را تکذیب کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/75964" target="_blank">📅 05:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75961">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GPX3eXNyGWoQSVlpUuhgx83HNZDbSq7GpmXx3h5Y7ja-yq1matorIl9knhRACyoTrcsDmYaOGffv97z6OJkhEE307nLIyHDLY7TUejiVrQ_yX2GcnlDet2GWw-u1BeHPce4-cgPxRUWki4ndJgfADCNW_tCuMKxxi7NsMkCcp88saa8zwqBU0n0YVTGv9GDXb0JiOFsTPuo9fGjaEAhL-pWMVdYBGo9qDvqFtUyh4nRjqYP5DgAibs-dgUtnlROmetExk48K3abk0QC3VMHMvg4eOcamGbQFtnY-oXS4cJCN6EawdCIrppsOfDJ_iFigdKqEGe05_K0NdjVjYQDQLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F9REWUtp6YsAjonu40cx80O8lW7l1e5vGT7GewxyWw_Ew3p2_cAAI_XfDh84oYZAPpJSvj9g-5URfl5hErIsEb4OnuJmmclFcOA999GEPyPS6AwrhevIULYfTQDI9CEnrKDkRbvWS0GDz2e1ihNFszd7HnlccNk-1EyCfIEbTkV8OWXiQOmrT2t-6XsFTbHYAEqSJCeIprFu9JkR6vej70WCSzrxyK0N6b6rUXSTaFlndrGLqUdpE6_6TKbP99X1Vvb_XfoGt67fjee1B3uMSmY0CZvE0uEi_HODCQWilpxgKNAiMkBYvSgTn5uRLl2Jf0pk00RNu1Bk9vfj3HM5iQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0de9d2e9d1.mp4?token=HeM32PmLj3wmuSC6_od-9XYYXBCE7XS14tBaM9F-7oLgElMGU8ttcS09Wwsqo_W6FqyWC26tczgA6Wg5bzsg-OIJg55E_MgYLoiawQceaWmAlfY2yieMovNAB6JEb3VVozt8y1vuJwpiXyopoS7ZV8fz-dnVWTyL_gIOWWpO8z4xEnvKRuu9dRqmc6oWZZaJ9Btd9FOwMZ1PO70YDNISCU2E2tX3Iu4adyOIH5RpeoB8Dz5PSKnVvbT5rHzSg8JzfshhqVZ4iGRQCVtQ_ffC5_Y1_2QNq8sqt0fZnKstKJn6PbyaApEMYFs5SgIT57KplUm2FxQIMJzZ5pQ9sscyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0de9d2e9d1.mp4?token=HeM32PmLj3wmuSC6_od-9XYYXBCE7XS14tBaM9F-7oLgElMGU8ttcS09Wwsqo_W6FqyWC26tczgA6Wg5bzsg-OIJg55E_MgYLoiawQceaWmAlfY2yieMovNAB6JEb3VVozt8y1vuJwpiXyopoS7ZV8fz-dnVWTyL_gIOWWpO8z4xEnvKRuu9dRqmc6oWZZaJ9Btd9FOwMZ1PO70YDNISCU2E2tX3Iu4adyOIH5RpeoB8Dz5PSKnVvbT5rHzSg8JzfshhqVZ4iGRQCVtQ_ffC5_Y1_2QNq8sqt0fZnKstKJn6PbyaApEMYFs5SgIT57KplUm2FxQIMJzZ5pQ9sscyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'رد موشک‌های شلیک شده از ایران'
تصاویر دریافتی از استان‌های فارس و بوشهر
آپدیت:
وزارت کشور بحرین نیز دقایقی قبل از به صدا در آمدن آژیر خطر خبر داد و از مردم خواست به اماکن امن بروند.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75961" target="_blank">📅 04:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75960">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nhbea3umHszfYPIX7SKiVxzDfiN0kx8APNXA-bJ1NgZGzqaE7aQuPZHKGzcSSQEOMB-JeKw4PcJM1y8VF_NiOkrBm3Ms1RHhcdPyiWjMULIxfEIUmPGqko6Yfm_bUronnpPY8yO8L1j4mGrPWf-hEgIJfBjQJSa7QXwCjI_Ba3OI3SRp44Hh7jPWRB1CTYPvxN3NP4lICX4vE3YAv02TAEKb3BQL6H7Y0IpHRVAahs22NEo8XYjyknee83ikfWsh04ZRDWbUR43K2ySrlnp-62waAaKBFeHWgd1ANpZKiU59TNubt4V75wwLUICWUO-8KlWO_Qmhz7VpCuSDkYqF0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک‌هایی دیگر از ایران همزمان با صدور هشدآری دیگر در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/75960" target="_blank">📅 04:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ekE-lpDaohFOoxzokH4SiUAklTdZ8hhqWGmme7X9GUy4QQ4A27gY1xJcGuy8CqFtNy_MKTs4du5Gs-PeZN0qvYRVi0TF9GSCAo5lb-TsV2pxpFFQxs6T1m7IiaRW4ZHaEnB_6_7SNADsu0CB8hTBNzhYPgLg_o_ULdkC8Ef_1XiAHsjPQFkr-dnn1aNHAu14CzDGHIempkB5EPPpDsBERTXB2-6yIcdRFEch3Bf_x-zNqB_jzt4f0RKMpRxfMfaZhFnSyv5f1jo9bZFAvKI8jujCyaWcjKHrK4jhZ67Qt-9Di8oDxsC04PnyzRQ3NmDoq1zCKeiUxwxrmWRuXXTWBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: اعلام هشدار در کویت
آپدیت:
ارتش کویت دقایقی قبل از فعالیت پدافند هوایی کویت برای مقابله با «حملات موشکی و پهپادی خصمانه» خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75959" target="_blank">📅 04:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBQ_JhIcLjaLTT3RSyH5ZQqPiE20EFluvFam59lsb35P5JYzqnXG-BsA1qpk_B3w_AGd1ANpIMnyBz-hAdqofx2btMxQCeeRUdAaP8BNFRvWsz_FR5AlFw5lsi7X6F0Nmflcs9hHiMjOLbWXT-pKvfGFXASeyXk3uJf4le7ejVBdmmRHyJ0XIqj9NH0BBtAZ1DPrApnGnNCQOE5sQfBWoZ3J0ItKQbs2Y7x7qsKtxFGqFlu_g1zG8Ok3-tu9oF-S9_xt4bxWCxJW_spwnzl972Kz7yqZmHn-REG3BEshOe_rFd27VciEFQYO6ozPfiv5_wf9TQdmSYK7AQw-igFFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهی مرکزی ایالات متحده (سنتکام)، بامداد شنبه، ۱۶ خردادماه، با انتشار بیانیه‌ای رسمی اعلام کرد که نیروهای ارتش آمریکا چهار فروند پهپاد انتحاری (یک‌طرفه) ایران را که به سمت تنگه هرمز پرتاب شده و تهدیدی فوری برای تردد دریایی منطقه به شمار می‌رفتند، سرنگون کرده‌اند. بر اساس این بیانیه، نیروهای آمریکایی متعاقب و با هدف دفاع از خود در برابر حملات بیشتر، سایت‌های راداری نظارت ساحلی ایران را در منطقه «گروک» و «جزیره قشم» هدف حمله قرار دادند. سنتکام در پایان با تاکید بر حفظ آمادگی کامل نیروهای آمریکایی افزود که واشنگتن برای دفاع از خود و پاسخ به «تجاوزات توجیه‌ناپذیر ایران»، در حالت آماده‌باش قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75958" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سیریک در هرمزگان
پیام‌های دریافتی:
پایگاه نیروی دریایی سپاه بندر سیریک  رو همین الان دوباره زدند. همون
لوکیشن چند روز پیش.
شهرستان سیریک صدای لانچ موشک ساعت  ۲:۱۴
سلام ساعت دو ده دیقه
پنج تا انفجار نیرو دریای سپاه سیرک هرمزگان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75957" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dg2H0QnLPjyztNzmtwv_OPwd1p4ueh8VuZQ-Go50giHEwAIV4nydTOf2XGrtWK2RUpsN-ePlZSimsZg3F6VZerJxEhCyY8YiNwozOzcr-KrsQVeSctqX5XM3CSHjt76T0Nw8YC3T467evwJUdp8B3lmsfP76aRSJq_IFc6Div3ty9C6E3a6SOEBgJsAnEX1zNUhD9jsriHeSU-sswvyhcl5gSCXgkdVaGpBfx-lTHTXHXvuzz9kt-Rx5rrih-fDE0F3IKNXVCa6sZsA0FyUvb_8oKwOb_8kROAFewWHAf6muG8NbMUZgyOwggJSuatluh-_3jadlM0bo_UC-BJDNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
وب‌سایت آکسیوس گزارش داده است که استیو ویتکاف و جرد کوشنر، فرستادگان دونالد ترامپ، روز پنجشنبه برای رایزنی با گروهی از کارشناسان فنی به آزمایشگاه ملی اوک‌ریج در ایالت تنسی سفر کردند.
به نوشته آکسیوس، کاخ سفید در تلاش است با ایران بر سر یک تفاهم‌نامه برای پایان دادن به جنگ و آغاز مذاکرات تفصیلی هسته‌ای «به توافق برسد» و می‌خواهد در صورت آغاز این مذاکرات، تیم کارشناسی لازم را آماده داشته باشد.
به گفته منابع آمریکایی و منطقه‌ای، تهران و واشنگتن همچنان بر سر برخی جزئیات این تفاهم‌نامه اختلاف دارند، اما مذاکرات وارد مراحل پایانی شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75956" target="_blank">📅 02:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75955">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KRZvZkd1MeEkA9l2xN6MW3mHz-ch8SBLiGohxmzH2za5BiNQIz_bERwFEFEZ_QjVcDqHqUEb-OFBZmwY-1t8lv-ASCLJ5GQI8MCk_YzvWmCX31hZXI0haujxn45A_CUVeRL4uHFgHtaoNcq8CxELONZlBdtIZeVwMX7Gxxg23obEKCvr6wQTeWXqD7mSj-mvrj0pUu6WGmr507YDqG79if4cK5QWSBe_UNF9x3abuZNaQslbcYc1KmyxlJCvLo4-Z4FAPcl94yiuKjyBO6K0bFEiChpHofFjqrOoOu0vwEGGDs57VCLhqIzUe5i1gV1Aurxif6rylxOAzuHHlri6Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مقام آمریکایی گزارش داد جمهوری اسلامی چندین پهپاد انتحاری را به سمت تنگه هرمز پرتاب کرد که هواپیماهای آمریکا دست‌کم چهار پهپاد را سرنگون کردند.
این مقام گفت مقام‌های آمریکایی گمان می‌کنند این پهپادها کشتی‌های تجاری در حال عبور از آب‌های منطقه یا نیروهای آمریکایی فعال در نزدیکی آن منطقه را هدف قرار داده بودند.
@
VahidOOnLine
ساعتی پیش‌تر اخباری درباره خارک و بندرعباس در بعضی منابع منتشر شده بود، خبرگزاری مهر میگه صحت ندارند:
جمعه شب خبرهایی مبنی بر شنیده شدن صدای انفجار و پدافند در جزیره خارگ منتشر شده است.
پیگیری های خبرنگار مهر مستقر در جزیره خارگ نشان می دهد، چنین خبری صحت ندارد.
بامداد شنبه برخی فعالین فضای مجازی مدعی وقوع درگیری‌ها و حملاتی به شهر بندرعباس شدند که بررسی‌های خبرنگار مهر نشان می‌دهد هیچ‌گونه درگیری در این شهر اتفاق نیفتاده است.
شلیک‌هایی در این منطقه صورت گرفته که جنبه اخطار داشته و کانون تحرکات در دریا و فراتر از جزیره لارک بوده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75955" target="_blank">📅 01:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75954">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4d85c72c6.mp4?token=N2fzh1saLPj5cN-bdPgYZm-7PIPMbINl0ST40RBja4LYJ7520GvTbEb0KHrKbMJSdxzgMM0xdl7HlMVL7YGsZ6BqleGRDcSWRz_oEATgTmFljv42CQnKl8g9Ng2-hqr8XHqfrMTNNSqiF5EierxIQwGkFVt-hovXXHdQ50vSpUDzs-tMb_cRScB7HZ3FfATzlKobnEMzLPS9YpAFU9scagNTZ4ICMzOTcj4caaPFhuliK4ZuOprdXdbXWUDntNoIIqxIxQx5qH1Up16zaDVdf_MEVcKkgdnVVodBo3WDImI7tBzM-QCDsMfQiRwynlJpjzEVPUjtVPOc6hwqIU0qQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4d85c72c6.mp4?token=N2fzh1saLPj5cN-bdPgYZm-7PIPMbINl0ST40RBja4LYJ7520GvTbEb0KHrKbMJSdxzgMM0xdl7HlMVL7YGsZ6BqleGRDcSWRz_oEATgTmFljv42CQnKl8g9Ng2-hqr8XHqfrMTNNSqiF5EierxIQwGkFVt-hovXXHdQ50vSpUDzs-tMb_cRScB7HZ3FfATzlKobnEMzLPS9YpAFU9scagNTZ4ICMzOTcj4caaPFhuliK4ZuOprdXdbXWUDntNoIIqxIxQx5qH1Up16zaDVdf_MEVcKkgdnVVodBo3WDImI7tBzM-QCDsMfQiRwynlJpjzEVPUjtVPOc6hwqIU0qQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش امشب برنامه «خیابان انقلاب» به خاطر این حرف‌ها لغو شد
beehnam
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/75954" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75953">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7JPhUBFKtPh4gdG6FanDYDetBLHK-g-RrUvzvSLeTYPRTERUk2aqA1khYUMXdP3T8WFfG8s6h6koRftMewcY1NBJx-xhr5WzOYXWg3cgEqvuf_AROqhw0Xl0IVP7323J2PQC1A9-kYHGZqPe89d8JjXiCQ6gk9GuwwS5Zo3ULmMtluEVita0n6crgsW0mpcqnFf390_i7wfeinOASG0udRuMiciS4cPkRAXL70G5rKL7OaeLfBSOSzGEW5MQpJXN1jPe0fuqNROgXzBurDyCIqwroQg5whZ5_Rww7QSw8WuoIHiaFLk63glQzH19ue8Pp97Dgyhs5vAzbcNmSbFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام کاخ سفید روز جمعه به خبرگزاری رویترز گفت که بازیکنان تیم ملی فوتبال ایران برای ورود به ایالات متحده و شرکت در جام جهانی فوتبال ویزا دریافت کرده‌اند.
تیم ایران قرار است نخستین دیدار خود در جام جهانی را روز ۲۵ خرداد برابر نیوزیلند در لس‌آنجلس برگزار کند. این تیم سپس در همان شهر به مصاف بلژیک خواهد رفت. بازی سوم در سیاتل مقابل مصر انجام خواهد شد.
@
VahidHeadline
آپدیت:
فارس، خبرگزاری وابسته به سپاه گزارش داد که ویزای برخی «اعضای کادر فنی و اجرایی» تیم ملی هنوز صادر نشده و سفارت آمریکا تاکنون از صدور آن «خودداری» کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/75953" target="_blank">📅 21:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75952">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWh6OyloEqGNRW3TavwbwxOQPhuYkW-EhqMVLLui5eLcVebt16Yyx6tcBYp49CtL_C0Miem3hFlu3yEkEkDfV-5IEJdoOpd3lXTpW4OBSsycXkrsqKuMu0O6NTuj0zB-Xmpomv4DW208agEm23eFAOWFMd9TU2sMezxczQ-XpvPz8pcHKGlmZrb1Opl3Wb8JVrVxE9MMOSDNSTOdKK1eZrzljbKiP3S7ZFvvREW8nJciZuow26FzX__sA4OFbNsE_vJ6QoktUgCnZGBHWIR5RFkGxf-d_wFqVraBP38wAXQItCAd8c_vGdzlNncj0C6zDghpZHs_pnhhVMOSCYFuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسعود نبی‌دوست» خبرنگار خراسانی فعال در حوزه میراث فرهنگی با انتشار تصاویری خبر داد که کلیسای تاریخی انجیلی مشهد، از آثار ثبت‌شده در فهرست میراث ملی ایران، بامداد پنج‌شنبه ۱۴خردادماه۱۴۰۵ به‌طور کامل تخریب شده است.
رسانه‌های ایران از جمله «جماران» نوشته‌اند که تخریب این کلیسا «توسط عوامل ناشناس» و با استفاده از بولدوزر صورت گرفته است.
فعالان میراث فرهنگی می‌گویند این اقدام در سایه غفلت مسوولان میراث فرهنگی رخ داده، عملیاتی که حدود دو ساعت طول کشیده و صبح روز ۱۴خرداد نیز با بستن اطراف این کلیسا از ورود افراد و خبرنگاران جهت عکاسی ممانعت به عمل آمده است.
انگیزه، هویت افراد یا نهاد تخریب‌ کننده، مشخص نیست اما این نخستین بار نیست که یک بنای ثبت ملی شده تاریخی در ایران بدون اینکه نهادی مسوولیت آن را بپذیرد شبانه تخریب می‌شود.
کلیسای تاریخی انجیلی مربوط به دورهٔ پهلوی اول است و در خیابان جنت، کوچهٔ گلستان شهر مشهد واقع شده است. این اثر در تاریخ ۲۵ مرداد ۱۳۸۴ با شمارهٔ ثبت ۱۳۳۷۵ به‌عنوان یکی از آثار ملی ایران به ثبت رسیده‌ است.
پیش از این بارها بناهایی همچون کلیساها، آرامگاه‌ها و بناهای متعلق به اقلیت‌های مذهبی از جمله بهاییان، مسیحیان و یهودیان
تخریب‎ شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75952" target="_blank">📅 21:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75951">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امروز ۵ ژوئن ۲۰۲۶
قاضی فدرال آمریکا امروز حکم داد که تمام سیاست‌های تعلیقی USCIS غیرقانونی هستند و باید فوراً لغو شوند!
leeleehozak
چه خبر خوشحال کننده‌ای برای دانشجوهای ایرانی آمریکا، امیدوارم بزودی روند بررسی پرونده‌های USCIS شروع بشه و استرس و نگرانی همه تموم بشه
21aban
بلاخرررررره خبری که ماه‌ها منتظرش بودیم، اعلام شد.
طبق حکم دادگاه فدرال، پاز برای همه‌ی‌ افراد در داخل خاک آمریکا برداشته شد، از این لحظه به بعد دیگه
#USCISpause
وجود خارجی نداره، چون این بخشنامه از نظر دادگاه غیرقانونیه.
درود بر استقلال قوه قضاییه که زد کل بخشنامه اداره مهاجرت رو لغو کرد.
درود بر دموکراسی که در اون قدرت، چک سفید امضایی دست دولت نیست.
پی‌نوشت: احتمالا دولت درخواست تجدیدنظر بده و اعتراض کنه به این حکم اما خب دیر یا زود پرونده با پیروزی ما بسته میشه.
BrmTheGreat
این
لینک اصلی و رسمی حکم دادگاه
ه
اینم
لینک جزئیات بیشتر این شکایت خاص
ولی از یه منبع غیر رسمی
mozfang
جزییات تکمیلی:
دادگاه تمامی استدلال‌های دولت را که سعی داشت سیاست‌های جدید USCIS را از شمول بررسی قضایی خارج کند، رد کرد و رأی داد که:
واژه‌ی «امنیت ملی» نمی‌تواند سیاست‌های مهاجرتی قوه مجریه را به‌طور کامل از نظارت و بررسی دادگاه‌ها مصون کند.
قاضی رأی داده که هر چهار سیاست جدید چالش‌برانگیز، ناقض قانون تشریفات اداری (APA) هستند و به دو دلیل عمده غیرقانونی اعلام می‌شوند:
۱. مغایرت با‌ قانون (Contrary to Law): اداره‌ی USCIS از حدود اختیارات قانونی خود فراتر رفته است. دادگاه اشاره کرد که اختیارات مربوط به محدودیت ورود (موضوع بند 212(f) قانون INA) منحصراً متعلق به رئیس‌جمهور و مربوط به مرزهاست، نه مربوط به فرآیند پردازش مزایای داخلی برای غیرشهروندانی که قبلاً وارد خاک ایالات متحده شده‌اند. علاوه‌بر این، سیاست اعمال «عوامل منفی بر اساس کشور مبدا»، به وضوح ناقض اصل منع تبعیض بر اساس ملیت در قانون مهاجرت (موضوع بخش 1152(a)(1)(A)) است.
۲. خودسرانه و دمدمی‌مزاجانه بودن (Arbitrary and Capricious): این آژانس نتوانسته است استدلال منطقی برای اقدامات خود ارائه کند، منافع و انتظارات به‌حق مهاجرانی را که طبق قانون عمل کرده بودند کاملاً نادیده گرفته، و به دلایل ساختگی و بهانه‌جویانه (Pretextual) متوسل شده است. دادگاه به یک «عدم تطابق جدی» میان اهداف اعلام‌شده امنیت ملی و آنچه در واقعیت رخ داده اشاره کرد؛ از جمله اظهارات بیگانه‌ستیزانه همزمان رئیس‌جمهور و کریستی نوم (Kristi Noem) وزیر وقت امنیت میهن در شبکه‌های اجتماعی، و همچنین استثنائات خودسرانه‌ای که آژانس برای ورزشکاران جام جهانی/المپیک و پزشکان در نظر گرفته بود.
🟣
دادگاه رسماً هر چهار سیاست را غیرقانونی اعلام کرد و آن‌ها را به‌طور کامل ابطال و ملغی اثر نمود. از آنجا که این حکم یک دستورالعمل دولتی را ابطال می‌کند، عملاً اثری سراسری و ملی در کل کشور خواهد داشت.
🟣
دادگاه درخواست شاکیان برای صدور دستور منع دائمی را رد کرد و استدلال نمود که حکم ابطال و اعلام غیرقانونی بودن سیاست‌ها به خودی خود برای جبران خسارت شاکیان کافی است و نیازی به این ابزار فوق‌العاده نیست.
🟣
درخواست دولت برای رد ادعاهای اساسی شاکیان (مبنی بر نقض متمم پنجم قانون اساسی در خصوص رفتار برابر و رویه عادلانه) رد شد. دادگاه بر اساس اصل «اجتناب از ورود به مسائل قانون اساسی در صورت امکان»، اعلام کرد که چون پرونده بر اساس دلایل اداری (قانون APA) به‌طور کامل حل شده، نیازی به صدور رای در خصوص بندهای قانون اساسی در حال حاضر نیست.
این حکم به امضای قاضی ارشد، جان جی. مک‌کانل، رسیده و لازم‌الاجرا است.
منبع‌:
کانال مهاجرت به آمریکا
BrmTheGreat
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75951" target="_blank">📅 19:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75949">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dvDF5T3j25LUdfcckq2EVK90oJEUHA6Z_sgAGNaXHJFe6sL-61Y4MVH1BA1u1MJoTaOOTTID5NaHF0pYST-4CCdqfjroBfNZ61aClVEFyA2d7lfbF1mFGGZqy0wFi6FKtUnPYP3dfCjOPDh7uBkNKQD9M9CMinjNLpvvhm_O5n4tBk4znyRNSAk-ZUW9WNU-4ANI3AZo_m41piAOOFZHtzJRqB9AZR_5SZ-wkQ69j8lmIOTezGfy0OKUHo0XCKz4RCKqbBPdGrEG6WAVztowVwX8eKmf6iNHxiknUIHPTgm3wAHlNStgedzKFUlplTZtiIT1IAa9BcdnuL1cIX8Geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LSIxFj-GUnSYNDnrubLtewws9V-ZuLVRowGjZLYRHGI3-83QkqvxfclDvFJDVCsbbojx6Lu9Unhg-cLGgvbPX_rY7sAt8yLRrZmm-Yu-1qXPv7viri5HhDsbD-lBAVojxcZ8Riq4L9XuZQZnIjON-Xc0UCOs79pUpSEFNB3QPTzkGziJSvPMQ3wwkHZpeC9KEqWGY7jXpMllJfq-MTCc6JQ2KQDqtotfaz8e_4PyubZBEYhQ7Iv1vyjPujq8UmVdV4kFGqP7HvOHgC-kZIH7p52iBnaFcQiPuOaBe0x4GkxOQZCLzEFg3KkNSFZhlQU6qk6MfBsgkePd-Jbg_objAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شبکه خبری الحدث، روز جمعه ۱۵ خرداد ماه به نقل از «منابعی آگاه» گزارش کرد تهران موافقتش با انتقال بخشی از ذخایر اورانیوم خود به یک کشور ثالث را به اسلام‌آباد اعلام کرده است.
بر اساس این گزارش، اصلی‌ترین اختلاف باقی‌مانده در مذاکرات میان تهران و واشنگتن به موضوع آزادسازی دارایی‌های بلوکه‌شده ایران مربوط می‌شود و نحوه و سازوکار آزادسازی این اموال همچنان یکی از شکاف‌های مهم میان طرفین به شمار می‌رود.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران،‌ روز جمعه ۱۵ خرداد ماه به نقل از «یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران»، گزارش شبکه العربیه درباره موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده به کشور ثالث را تکذیب کرد.
خبرگزاری فارس به نقل از این منبع گزارش داد ادعای مطرح‌شده از سوی العربیه «نادرست» است و موضوع انتقال ذخایر اورانیوم در دستور کار فعلی مذاکرات قرار ندارد.
به گفته این منبع آگاه، موضوعات مرتبط با پرونده هسته‌ای در مرحله کنونی گفتگوها مطرح نیست و بررسی آنها به مراحل بعدی مذاکرات موکول شده است: «ابتدا باید طرف آمریکایی اقدامات مشخص و قطعی خود را انجام دهد و درباره برخی مسائل اساسی به توافق‌های روشن و نهایی دست یابیم.»
شبکه العربیه پیش‌تر گزارش کرده بود تهران موافقتش با انتقال بخشی از ذخایر اورانیوم غنی‌شده به یک کشور ثالث را به اسلام‌آباد اعلام کرده است و این کشور ثالث با توافق طرف‌های مذاکره‌کننده انتخاب خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75949" target="_blank">📅 18:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75948">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsRubBB7c1vdel9b3o9lk2HNsVPZ9CWIkiIuFu5CM725caZVpc_0fmLeykjPW9yDZWZmY025-OHrXb8RDifo8spqhiGOJe6VLOeTdZRTGfIHJ3AIjGFt3Bs83QpdxfT98SP1GsuOgPDGX_zfhYHX5QXogMzMtKp_flKhcZA5opaXnv7IpdGHH1QE8y2v-6R_JVN5BIrK0YSBhGEMplc9gNV9vHnOOo2ZEzNy0FZqWDV9UvkjemrV62HSivPJjpQWDc0AqLZoqKrcC_LbKIIagOrwrbRclK5rbz-wOzDRoYFB3Vu-G2wpP_glfOYUbGRUVUO93C3ES8q61vy9yYikag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوزف عون، رئیس‌جمهور لبنان، در مصاحبه‌ای که روز جمعه منتشر شد، از ایران خواست در امور لبنان دخالت نکند. او همچنین به گروه حزب‌الله، متحد مورد حمایت تهران، گفت که تنها راه‌حل درگیری با اسرائیل، دیپلماسی است.
او در این گفت‌وگو با شبکه خبری سی‌ان‌ان خطاب به ایران گفت: «این کشور شما نیست، کشورِ ماست... دخالت در کشور ما وظیفه شما نیست.»
آقای عون افزود: «آنها از لبنان به‌عنوان یک اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کنند. این غیرقابل قبول است.»
رئیس‌جمهور لبنان همچنین گفت: «حزب‌الله باید درک کند که هیچ راهی جز نشستن و گفت‌وگو وجود ندارد؛ هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده است، جز از طریق مذاکره و دیپلماسی وجود ندارد.»
حزب‌الله از سوی آمریکا به عنوان سازمان تروریستی شناخته می‌شود اما اتحادیه اروپا تنها شاخه نظامی آن را تروریستی می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75948" target="_blank">📅 18:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75946">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JDSFz3FVJtuzqYwj8U5tSJOESpm72qSmetQjPHHQgK2B0Ryz7VcNq06rQAWa8HT0XVTiPDFboyBwWrJDrJfW4QwDp-jC65Q_zFBiosIGTLazGButOvEoCi65XYIPuDXArVxML8AF90JXPnF2W5Y6HtIknIUeqPUfsw-7kU9tiEBQPSDx2mYzhHqLxC7ZbdvQ4Pft3R15vUUcsm15VmfWbk_C7YHMbs7q1U1SG_Y6DmrQfE6w6jCqTFj0w7hHoTj5iv5VqAFOmi_hJWZ9DDk41BeNTMM8nmKQtMU8Ra0GAVeZYIbh6oHxlAvb24cXXEvYnzAPuiNJyE9KvKuMdebnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/03b8183b03.mp4?token=BfBFgKfqF1JVhaQ_O1UOLPRQ0O7iOWdNWloKlqksMSe1J1q5x0Dh8xTBNe3DVzjV1t2bAharujmpJDqoBsIOZJ4f4zSG2LtitpENqdLVlSAtJqyzhHATlgWgsz9PPPkl619ztndqL31Ecb2pE7eud7bC_6XmRWsb75aFcq7jquGw319ks73cZH-jzbIfMKP1n_uXUNQjub2SB8GtwqllSNDgYbM4mkmQ8f2i1UUaiLK2mdEomW2qJVVJl-hmFg1pO31c7o5I7jMgtuSzIaDrThPMKgDTEPzH6VS5oa9sbCPwnsxU12Vk799XvGhP4M4UxIVRjOnW0Uq4-fKVY4_Ogg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/03b8183b03.mp4?token=BfBFgKfqF1JVhaQ_O1UOLPRQ0O7iOWdNWloKlqksMSe1J1q5x0Dh8xTBNe3DVzjV1t2bAharujmpJDqoBsIOZJ4f4zSG2LtitpENqdLVlSAtJqyzhHATlgWgsz9PPPkl619ztndqL31Ecb2pE7eud7bC_6XmRWsb75aFcq7jquGw319ks73cZH-jzbIfMKP1n_uXUNQjub2SB8GtwqllSNDgYbM4mkmQ8f2i1UUaiLK2mdEomW2qJVVJl-hmFg1pO31c7o5I7jMgtuSzIaDrThPMKgDTEPzH6VS5oa9sbCPwnsxU12Vk799XvGhP4M4UxIVRjOnW0Uq4-fKVY4_Ogg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده، سنتکام، ادعای ارتش جمهوری اسلامی درباره شلیک موشک و پهپاد به سمت ناوشکن‌های آمریکایی در دریای عمان را تکذیب کرد.
رسانه‌های ایران روز جمعه به نقل از ارتش اعلام کردند که نیروی دریایی آن به عنوان «اخطار» به سمت دو ناوشکن آمریکایی «موشک قدیر و پهپادهای تهاجمی جدید» شلیک کرده و این دو ناوشکن دریای عمان را به سمت اقیانوس هند ترک کردند.
سنتکام که فرماندهی نیروهای نظامی آمریکا در خاورمیانه را برعهده دارد، ساعتی بعد در شبکه ایکس اعلام کرد: «نیروهای ایرانی به ناوهای جنگی نیروی دریایی آمریکا حمله نکرده‌اند و به سوی آنها آتش نگشوده‌اند. انجام چنین اقدامی نقض آشکار و فاحش آتش‌بس محسوب می‌شد.
در این اطلاعیه بر ادامه محاصره دریایی ایران که از اواخر فرودین آغاز شد، تأکید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75946" target="_blank">📅 18:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75945">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnYVZvgbpjnwRnPUWYxiBdoAWza-IdezRN2fzL1JjRWCLFMMCVq3iK5J4NoXlAf6C2gONBmNaqfezWWJAl9AKtblADSX8XCzoWqGtLMGboCbsdVApM30P9mqDb0jHmBSOcQ7F0SEmObE7RdvLOLRdSYctgULci06kNIAcfZhUfvi5KT-b-thEf1IoqQM4mpSuXrEsIrETeyVbo5SXuYTbdJe5cTiZTfwEZqsCEkhC8slm_iNxRNbieiu4eUuXlsa3yj5XEOjv8-Sh5c30iNOuINPvnJ0Y--2hkpWbTklZ97r-BdATmRJ_dQmYDCkMBNNOMLCaSoo9-pPE7URgc_zKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کمالی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه ۲۶ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌است.
رسانه‌ حقوق بشری هرانابا اعلام محکومیت علی کمالی به اعدام، نوشت این حکم در حال حاضر در دیوان عالی کشور تحت بررسی قرار دارد.
به‌گفته هرانا شعبه ۲۶ به ریاست ایمان افشاری در اواسط اردیبهشت سال جاری حکم را صادر کرد. کمالی که دارای اقامت مالزی است، ۲۲ دی‌ماه ۱۴۰۴ در تهران بازداشت
شد و اکنون در زندان تهران بزرگ نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75945" target="_blank">📅 18:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75944">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uCXHnYVEYILFFO_hNwl2jpXqH6Xhi2JoSD37kvoF5pIcbAl8J7BWJKRuYxa4IChjeUkWafbVdpXOYpfm0Vih1t0s3tASWDMEA-ke7k5F5zsjJzrUDVaTfX5_LEItr35sNhWLSEd54gdRkA6sAqDyW13SndutVEYRMNpk4QPqBbEKkaNwDuWtwynipA4OM9aZ9B9vsx8bR5W2JsofjhvDIHNfNUD1nhkHlQDoIX8FM6xp0Vt4AZkMSaY00Y7Q4RkVnILYqEmoKgt8hVeUGLJ71vfllmgMNrzDkTs-oaq7stSsWoOqGoKJGZ7LQBPCX4w6TDNVx4MPBNCqp5H_aM0aCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع در روز جمعه گزارش داد که پایانه نفتی مینا الفحل در عمان پس از وقوع یک انفجار در نزدیکی اسکله‌ها، عملیات بارگیری نفت را متوقف کرده است. به گفته این منابع، انفجار ظاهراً در پی یک حمله پهپادی رخ داده است.
@
VahidHeadline
AJENews
هنوز مشخص نیست این حمله دقیقا چه زمانی روی داده است.
بر اساس داده‌های کشتیرانی ال‌اس‌ای‌جی، روز جمعه چند نفتکش بسیار بزرگ در نزدیکی این بندر لنگر انداخته بودند.
رویترز در ادامه
نوشته
:‌ رسانه‌های دولتی ایران روز چهارشنبه گزارش دادند جمهوری اسلامی یک کشتی نظامی آمریکا را که «مرکز کنترل و فرماندهی» توصیف شده بود، هنگام نزدیک شدن به آب‌های سرزمینی ایران در دریای عمان هدف قرار داده است، اما ستاد فرماندهی مرکزی آمریکا، سنتکام، این گزارش‌ها را رد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/75944" target="_blank">📅 06:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75943">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b8JZAQbBZXS7fnBcN7TAQ-6b06VgQNlL5I-OR0olCxlRPgzOOqvXkyv4XEayw9AArfxdHEsdKgGdrUBuLcOgdLeE6z1LhBLBv83uT-G3vuT7lPbCl5734TNhn7t3osiYSzKasg1lM5zcjcj-yNzf3RSQ6_PTFy8egAy331r5b0XbgggDTljT3iEXvqhRIsFym7WKzqTFAB8uC4PI2vVgbDyeHRL52hntl6Fge889lSEkDUAtIRoFGS9FKHCvNW6oTJYYa6Rq_AFyOCyCML9OTNxk1-bLF03268AUnSzIiMdB78InBmDFBPeCBoQ56uE_xaanCLcKTv7UD8buqWWmBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: ایران نباید سلاح اتمی داشته باشد
دونالد ترامپ، رییس‌جمهوری آمریکا، در کاخ سفید در پاسخ به این که اگر حکومت ایران نیروهای آمریکایی را بکشد، آیا جنگ با جمهوری اسلامی را از سر خواهد گرفت، گفت: «این دلیل خوبی برای چنین کاری خواهد بود. اگر آن‌ها نیروهای آمریکایی را بکشند، فکر می‌کنم خیلی سریع دست به این کار بزنم.»
ترامپ درباره جمهوری اسلامی تاکید کرد: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا گفت: «ما برای به‌دست آوردن اورانیوم غنی‌شده آن‌ها به توافقی با ایران نیاز نداریم.»
او درباره کمک ناتو به بازگشایی تنگه هرمز نیز گفت: «ما به آن‌ها فرصت دادیم که کمک کنند، اما نخواستند کمک کنند. این موضوع برای آن‌ها بسیار پرهزینه خواهد شد، چون نباید چنین کاری می‌کردند. باید کمک می‌کردند.»
🔻
ترامپ درباره جنگ: چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد
دونالد ترامپ، رییس‌جمهوری آمریکا درباره جنگ ایران گفت: «چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد. بخش اصلی این است که تنگه فورا باز خواهد شد.»
ترامپ افزود: «آن‌ها (جمهوری اسلامی) هیچ نیروی دریایی ندارند، هیچ نیروی هوایی ندارند. ما آن‌ها را نابود کرده‌ایم.»
او ادامه داد: «رهبری‌شان را از بین برده‌ایم و تقریبا همه آن‌ها را نابود کرده‌ایم. بعد در رسانه‌های جعلی می‌خوانید که آن‌ها در جنگ خیلی خوب عمل می‌کنند. واقعا باورنکردنی است. ما هر چیزی را که می‌شد نابود کرد، از بین بردیم.»
🔻
ترامپ: حکومت ایران درباره توان و اراده آمریکا دچار اشتباه محاسباتی شده است
دونالد ترامپ، رئیس‌جمهوری آمریکا، در نشست کابینه در کاخ سفید با اشاره به مذاکرات جاری و وضعیت تنگه هرمز گفت یکی از محورهای اصلی توافق، بازگشایی فوری تنگه هرمز برای عبور و مرور کشتی‌ها است و تأکید کرد آمریکا «هم در میدان نبرد و هم در عرصه دیپلماسی» پیروز خواهد شد.
رئیس‌جمهوری آمریکا مدعی شد توان نظامی جمهوری اسلامی به‌شدت تضعیف شده و گفت: «آن‌ها دیگر نیروی دریایی و نیروی هوایی مؤثری ندارند. ما تقریباً همه توان نظامی و ساختار رهبری آن‌ها را نابود کرده‌ایم.»
او در پاسخ به پرسشی درباره احتمال ازسرگیری جنگ در صورت کشته شدن نیروهای آمریکایی توسط حکومت ایران گفت چنین اقدامی می‌تواند دلیل کافی برای اقدام نظامی جدید باشد و در آن صورت آمریکا «بسیار سریع» واکنش نشان خواهد داد.
ترامپ همچنین درباره ذخایر اورانیوم غنی‌شده ایران گفت آمریکا در مقطعی گزینه خارج کردن این مواد را بررسی کرده بود، اما به دلیل نیاز به حضور طولانی‌تر نیروهای آمریکایی از این طرح صرف‌نظر شد. به گفته او، واشینگتن همچنان توانایی دسترسی به این مواد را دارد.
وی افزود آمریکا با استفاده از سامانه‌های پیشرفته نظارتی و امکانات فضایی، تمامی مناطق مورد نظر را به‌طور کامل زیر نظر دارد و هرگونه تحرک را رصد می‌کند.
ترامپ درباره احتمال دیدار با مجتبی خامنه‌ای نیز گفت شخصاً تمایلی ندارد و چنین پیشنهادی را هم مطرح نکرده است، اما اگر چنین دیداری انجام شود، با احترام برخورد خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/75943" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75942">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QHlGMV7bE-dygd-EDoYP6acxJWrtM3iUUZAnPQciOkNiXAdCqqQzxEv83dX2WEkbN3cWuu8yRdKNH2Zpis3hqTzulmPncCi55l6kzzPFpr36_UT3kLceJfu7xLlkG23XCFC38INH7vGDUqenYJ7wDbtuMTO60DVnzOd0QHmBAoHLJw1BQEl0HkvrSJzK_calUZsWqhzQSi26sZWyrQWaQqOnSMY5DUKizF2w4qqTIztAYAObDVS40AOJuZt8-369ZZ64AXSQ2YK8mo-B7Fesm3sC8xnkQwoUKi86R4khTThEJHJHYlpUC3rvCGNip-jMT7iI-S3oeWURFKChzYfPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه پنجشنبه شب ۱۴ خردادماه، به نقل از منابع اختصاصی گزارش داد محسن نقوی، وزیر کشور پاکستان، برای پیشبرد مذاکرات میان جمهوری اسلامی ایران و آمریکا به تهران سفر می‌کند.
به گفته این منابع، سفر نقوی در چارچوب تلاش‌های میانجی‌گرانه اسلام‌آباد میان تهران و واشنگتن انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75942" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75941">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a-8e3Ltgh_NffkwJtbZ-jKjEUjOK3DUh4UJsglVImkuw6MByw9Dm3pSxfH3fcg18JGE85hwzfITvUTT300IciuiURt7M-fGohZOfajJFjucydv9l9D08xeBg4WepfOy5pF7jnI56fpPGApxxshQ0hlsRG-57XbXVf5TV-WRrZ5cPgEZkjXtCqwIFpX2zkL8n2H1o5WrNdF9nqr2ndfRzZQOT5lnMbRdLyXQz4Gub8u7-ZJ_C2DXYwddmITp1cwZTi3caaFpbSld2TVJdtykUiA0Ly4imaL8j1U81IEuNxcpCD6lSz8PEDL711bqtj8lMU2Evk98zwE5xRInbFwBkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه گفت ایالات متحده بر جمهوری اسلامی غلبه می‌کند، یا با توافق یا با عملیات نظامی.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/75941" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75940">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dg3yeS3aZdcgkajQguCsLjy43jtD4jUB8kSYpXtKqZ_yGLtFOI70Yu517KeejbYxupj3jxhHidxxJB8B2lkiF_4Amgft7fmRw6ykW7VHXDx9Z9Yy0Ryd_kEPpp2zliGC6T5Z4gtyR1gdWB2dLwfrz8f_G6uzealA5OyVP-rOG44yCdTr89ikIa-ZHBKHQrDc7oZ9flIMnK7lE9E2TwJE6g_ADBBS1CuaBl_ccql1SQVi3ABrt9Or8AKAsLzvA9dmwjqtdyQ01yjiyLxpOq6d2iJZYmdSyo2O-44z7BJyPkYfVYoKclUFxFts8yiyb7-DmnEueODEYuka3NBL8QpToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی پنج‌شنبه ۱۴خرداد۱۴۰۵ در گزارشی به کشورهای عضو، بار دیگر از جمهوری اسلامی خواست «به‌طور فوری» درباره سرنوشت ذخایر اورانیوم غنی‌شده خود پس از حملات سال گذشته آمریکا و اسراییل به تاسیسات هسته‌ای این کشور توضیح دهد.
در این گزارش همچنین از مقامات جمهوری اسلامی خواسته شده تا زمینه ازسرگیری کامل بازرسی‌ها را فراهم کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/75940" target="_blank">📅 19:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b23HAoPWranAE6frEqJaiHbr9zdAmfrXZ2ZsT2HLx-_k2TGCXEjcDkUebKTPCkevxKSartcWuNFTYyh_kr2I6g1eyh0Qjf3w4Mpxo0ADHNBC6dvURRFZlBOgsBhe3Afsj43ojYFJJwqBuekXye_NmAbdSlxULXhRtJ3kuIlcdbhmP0KZSGH1v94ZLccg-mheLEqrSAb-xaGSglTA0cS33Kzz8Dv5njRbg-j3L5gWsamfNqCNBgSkw5N2Wvstqk5AqP24nq--t_3p0MOjNesSYrlPHWV406QlU7KEY2kHu74ajJ7V6k4Nqg0PIk6i0fUlVMqntILWegT17xvP52VGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل گروه حزب‌الله طرح آتش‌بسی را که دولت‌های لبنان و اسرائیل در مذاکراتی با میانجی‌گری آمریکا بر سر آن توافق کرده بودند، رد کرد.
ایالات متحده روز چهارشنبه اعلام کرده بود که لبنان و اسرائیل بر سر اجرای یک آتش‌بس به توافق رسیده‌اند؛ توافقی که مشروط به توقف حملات حزب‌الله و خروج نیروهای این گروه از مناطق مرزی جنوب لبنان است.
@
VahidHeadline
نعیم قاسم، دبیرکل حزب‌الله لبنان، توافق دولت لبنان با اسرائیل که با میانجی‌گری آمریکا تدوین شده است را «تسلیم و شکست تمام‌عیار» توصیف کرد و گفت حزب‌الله تنها به توقف کامل حملات، آتش‌بس و خروج اسرائیل از خاک لبنان متعهد است.
او همچنین خلع سلاح حزب‌الله را به معنای از بین رفتن قدرت لبنان دانست و تاکید کرد این موضوع برای حزب‌الله قابل پذیرش نیست.
پس از توافق آتش‌بس میان اسرائیل و حزب‌الله لبنان، آمریکا برای حل‌وفصل اختلافات مرزی و مسائل امنیتی میان دو طرف نقش میانجی را بر عهده گرفته است. در همین حال، موضوع خلع سلاح حزب‌الله و نحوه اجرای آتش‌بس همچنان از مهم‌ترین محورهای اختلاف میان دولت لبنان، حزب‌الله و اسرائیل به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/75939" target="_blank">📅 16:47 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
