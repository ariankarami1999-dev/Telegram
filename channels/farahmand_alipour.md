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
<img src="https://cdn4.telesco.pe/file/ZSAIG-h_J2S3tTNbgwosEErXXw59NflU7ocrUYpJ2_WPRoYSwwjhq7ek6vz2BqsIgkXCRtfj9SzMWqT17R3oiZGfazSq5yAHah9EVjFfcHqzqBvI7nCcZUlDw0W96-drU1_dioWZwzBZ88-q0dhhU-ZbweCwMkjkpcTbl6Sj8Tz0CEl8Y_WeU__uC0lFo9_zyqiPFcNnwLlbXct6UmZfetLCXvvGvfTXG8EaQEXY7iMwBZapukrQWZyoE8q2XS2Qf3AVkdchU_kuzVzELnixtluAX7GEJDV_7NIZbDzSOmnN4UJScGUZt_BvSTwCORvNq557UViWDLw4Zr9UZLn2Tw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 13:09:54</div>
<hr>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=P05kncIb0h7rNj_N9SSE4OzWS0pgnXQn88GMZEf6VaoOysO67rK7BOq16pRzBeuIegPVzFAuPv5OC2P1I5IPXgA_Rj-PD_B12P4IUU6YxH4dD3QCLk4yITuBBpXxNeq8YoFg89VjIXdHqbawlBVIBllnHoBQZeAvUkumsg8kDQ2_281Zt2oLQy_3birxmNQWo3E2r5gLB5K7WieZtNYStc42VMBT5B81cQ6ZIZQ1xGu-0yI5hxNKjpXPWOqPi6BkMT8g1UgiZhezBm_9ICt1lG3EenHjeDgAjCFHsne8s3nho6skJzTW9-AcA_NgnD8SFPcAzluTHnvc7LcxQPUS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=P05kncIb0h7rNj_N9SSE4OzWS0pgnXQn88GMZEf6VaoOysO67rK7BOq16pRzBeuIegPVzFAuPv5OC2P1I5IPXgA_Rj-PD_B12P4IUU6YxH4dD3QCLk4yITuBBpXxNeq8YoFg89VjIXdHqbawlBVIBllnHoBQZeAvUkumsg8kDQ2_281Zt2oLQy_3birxmNQWo3E2r5gLB5K7WieZtNYStc42VMBT5B81cQ6ZIZQ1xGu-0yI5hxNKjpXPWOqPi6BkMT8g1UgiZhezBm_9ICt1lG3EenHjeDgAjCFHsne8s3nho6skJzTW9-AcA_NgnD8SFPcAzluTHnvc7LcxQPUS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXdR7AcjzRjBEfZwmQItLC1crIx3hIJQtf_d9Ep1IBhn-OmMWNL7xmF5fdC44V6vc2jqlBdLFqslP6365ZUTsOfTPD2zNNg9dhlVr2_DldgqmvYysI-CJrNiY82wHvHh7MRFPQVoAzcexj0r1Qi4W4RtuDf5LosyK2HhN6VJTVTqN4WEO5-t0YZlZmdKv_XdyPYp8KDxZDOGJ710nKMxHMP9Ba27kP4atgaqjgW3BW5wJRRxzwEnOu2Qy2EeFe9DxGGErz8wtK8-OVfUEWFDt08RQiOI512acm3uJqxIDp71fg8lZFJo1i7BYX_qQHTwEBrLRCt_K4-CfAxeaW5pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=E56I7jbPGe5mE2Qhau2_CTWi_ri8DDf9Fpc2PApmr4ofS7cu83J-Z9g842v04tKRnWIVHevqXbNhZievqEwtP-4sr0Efc9UaITtoyL4nw4rudEuUFAc4Lmt6hWIijHsqmfvcwq0t48h1KydbhsR8R3KgcbZMqaLR_Zmjq9MzikvVxx-sd_DiuRRgM-KcaW26SSvpKU6aPOEm6EUImlXcjKTvM4uFljhkQpHdWHa_RLQUOSxiizcqiUEXtJZ3FpZO7J5U0sB1YXHGgzGKiTFALsCpknDWRLQs-c7EK0aIr-_CuSn5n3lMWyxvkJ1EXyBmgNyvnaA-2f9jLnse13gxBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=E56I7jbPGe5mE2Qhau2_CTWi_ri8DDf9Fpc2PApmr4ofS7cu83J-Z9g842v04tKRnWIVHevqXbNhZievqEwtP-4sr0Efc9UaITtoyL4nw4rudEuUFAc4Lmt6hWIijHsqmfvcwq0t48h1KydbhsR8R3KgcbZMqaLR_Zmjq9MzikvVxx-sd_DiuRRgM-KcaW26SSvpKU6aPOEm6EUImlXcjKTvM4uFljhkQpHdWHa_RLQUOSxiizcqiUEXtJZ3FpZO7J5U0sB1YXHGgzGKiTFALsCpknDWRLQs-c7EK0aIr-_CuSn5n3lMWyxvkJ1EXyBmgNyvnaA-2f9jLnse13gxBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=tIypavevWZjZrDiwVRYk0Dn2hlW-IZD3Rk06hPhDwhowJzzzLS_LvSbpCLgPRcxRKEmrzDL6CeDMm0M0g1v8qSs5EkINB-WLjczwBAgfN4sbt67YiNguwr1lvyT7eOulCoEaI2DxWOxK9vgYRBWFRJ7csZBaorKpHp-3RjEksVM2pJi5KxkNJuUGmSxJ9ZZYHJj-QM4MEI-t3lmtFYw2bzAllnAZsLOeU55aw2HaWoNobew3BS3OYUfP_mSE73ZytuRKqkLWm12C_JNp1d29vX8kJ0fHWTIQiczlQtI-Ts54tJday-zRh1j0FtK_XnjWJjSfL-by8xgtnKM_vUpzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=tIypavevWZjZrDiwVRYk0Dn2hlW-IZD3Rk06hPhDwhowJzzzLS_LvSbpCLgPRcxRKEmrzDL6CeDMm0M0g1v8qSs5EkINB-WLjczwBAgfN4sbt67YiNguwr1lvyT7eOulCoEaI2DxWOxK9vgYRBWFRJ7csZBaorKpHp-3RjEksVM2pJi5KxkNJuUGmSxJ9ZZYHJj-QM4MEI-t3lmtFYw2bzAllnAZsLOeU55aw2HaWoNobew3BS3OYUfP_mSE73ZytuRKqkLWm12C_JNp1d29vX8kJ0fHWTIQiczlQtI-Ts54tJday-zRh1j0FtK_XnjWJjSfL-by8xgtnKM_vUpzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFR9mP27XuuGctu-j9UIthXRXcR2HkauBcp1vLGDZucKGnJvm6eCgYqeLOvCJYxlxP_FsBBPQArNZnG5bWZDEwg8-oRrf-Vs395QhuFLe4n0xgtcckZPJNY5zaXOh57Dn2kPUElOb_GIltlAf_xxkne8VsmO5yH0tHkbhceyuXQVw48OkPF6o13-oWWgXwHuGqHV_kMRmdG_2cieuC8UaZz-wOvzGoDrem8KfCz2jRHSP2VrOUFiX6qglWYIWeM0Iu44DJe1d3irDKrX5zLqC4gT-lw5sJi9TyfIXlCj8YcxMBdPEm4W35CEv8IZAj0QYitzECSm04Z6x6YqyGioJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYSlidjSFGizuNxf7akejcFa-W0V3nxfwB2eUuasb1PzDVKm0REuO1QswdLgrZ4WyJV93uCy9_BZpeXJ-KEUYHDlX1b-9z7fZsAG2ydDh8z4RuMEgvzHWtqlhFOA9VrxDnu_5UYxLANrAAMNGawKNtqU4TjMISXHHNav543K7N4L01Y_MaezrDdVVXcZRU2YQtIddfM9WrdazZWIOSQCCqda5ucIkrYtJolCCDPEoYH7b0kMEvRE_7G6_4OxaMWA1ga4wICJlt4ERIUinY75EczzXSj5N7NNnHfwjJue1jvnSR05_ZdA28_T9idA13qdvgyflc3HR_lQKUVqdP-x2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxbQzXGl1WrvlN9I1lmnND2NVF945lmXSD8zphNG79RXXIsZ82X5Iugs0692acWqBXfB6u7Rj82YgnNyijd1KQ2hAhhc5wZANS_qyBB9d_2iTpz9tmQD0gAXQcsCP3WY8Z1xloET6OosZziCYCUgQH93Jxz4q_5YzWzrZfB5UVjMMiBjkHPDraHMngf-3mtEYLQ3MP8Ysajo2BR1KqfaA00qokDrdaLRwRyACaELmwVUpmXg0e3zBG7E5AvDzKftNByph9k6dD4NbNlKM6ABkE9XD4ccs0vXxocoD0zsWzrH2d-MReZQ66Yrf00Yv9v1UNLKuuNWZcHQVcnpV_B3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJRkbhs9IbWoRZovuIbAdCL8RXSrfv_LsUrHECXlOyAb2uyCnEEv9ImGnUkRyGmvAC06Z2YVpGx7izQ-p_b2WD9xm-bTyR5IzbJa30aWfPj3lmO4UruESejP3oMsOJpBG7NLchPSl77nDA5NmHdAG5jEjqbm4o8iZQyOB8lfip-ciniSz7YpCk9ZbLMGfjSmj_rW69BB-5xaFhnYeIyVHfGFt8KxkjcULSzASE3rL-HTEk3EI1vda8CAZRClwHoNtnY5UOogMYIUFLiFLHvjQw7AKDT1iD_I28FYmfPpNWm07UmLfMN-GmjQr4YYQyUOtDqs0B-TrusDlkbR-DeOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwLMcM0LJffTojGPVsjEqAgMoi1eJIRsww6pC98MoN0k_d-FmyfjeQ148E-HrPQnaDXW4MtxSnckE32jcUYckiVEK4nIMmGeJVwNk8qAIjhrHYFnB-4Kx2wQiZrcY1YHxuX5TRr1vLnOKUNNxJ8gpWT7NDkUtqHovi3GvNRz04OjmkfTrZ5WfmCUSbpXilS12lZYSL5f6iWe9dlHx0j5EOpq3dDqMYFtgTPinIul2ojkaMjj6_qY8RVGkB2-yNc0RUFeSUDCDUZTvcYbv9gDaJdMPFcW_RFvftYWnvv0WjCW932Lm_q8kZS9nSlPBeI1qLHdq6IO3M87qE2nVGcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZCqlPKpCjGMNcd25k9ah-VDlBEpuDpQYsZ7vniCaaOfMypdMhqaNih02Zgtm_AtyhjHLGbrzlXujuHK0lgJr_9OOH9ONVCWJJ4smWF0cftr1q7n9ictCggPO4X7_i5n8rJVyb5e0ou8AJKaEKI7ymcEPHwEJGIwkrhSJWTmt8c89wdEVTWWsv4gbxEQiiY7PqMEaSHBGDhw-S1vxnY4Yc4RjKQ-lc2Zi_X5RffMxiuqtkPbPuqDj2TUFq2EqQmPRT47V9MxM8BAIiSjunK3aPGOtYtkgSuhawksEmBTT5etN1WV7GvBpIb9F--tqgd5NybWSO7MVcn3hVpKSEYQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPoVVbCBR6fi79yNQT7R_sZJb2nV7-bH9w7Z9OEOnoi9v_58iZeP_A0x2dUPttRSG8u7puZZYEeJWBFkhESdQqfmEoDtQTyiDDmOoeBgb1yYDtLcFfQ8Et9RFJFT5lLsI16DTvsYUNQTMqbY_1oXHoSMrLPzalbpbelPLrwC6TyeANeNo2pPZtwxNdeROQSsnV607bzwwd8wrJi_Hz1Y6NJ9CxqQrL3HenzJJk8zhbgyh4RwadENoAxlwVYRMXcuxGS1_iQg2z85pS0n4Rhtocb0oK412lOgbxyVfe1dyLnZsZduyHp2kCO8cLqHb-lZ2YRc0Asezda3Kj1FoaWrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U660sy36EAf8-UQQDt4l0uR2a2kegaB6jKZIsKRPXQG-3LYkbOYBW-4Ti1fOVi9etOjegww7Rei_ULRgM2lgdT_-qglCj1GfQ18O_lzMBNHZGc1cSRrIvCx8w4F1SZhklh6z3oN2rAE0EC6sIK-QVHKM_LrfbUZ7lEu2l7NJ8R-shtvNZn5R4GHwYVdxFkZRDRcwRGmFeoJX4M_Bs0hlh2x-x5AA6Ip0kMoQPoW7BwxKdy6PVeBAg_B4OuRS5FQuf_x5B0OybTGg6CSK4d5ieamXCYpESVQcbTEHJJFafFl6Vsz_zokfZuOR4FDG7zj0PDTApk1q-XUV29nv0fp0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st63hidYDFToUuDVWw0QURz0DGn_Wjwt9EylQccuafRxutnA_FLTJyFPwSxKViEFfgvWQaEw62Es-bxE9zJRaOHwN09yIwdSk7uTm5UVeEFsK8HkRrD0IPT2deUjRqhNHGttUIqG6bctz7AdcQ2jM18SCWMARmpwvugNgOaTp-GmQaMu_cEdrXH2RcHBcwTh6migu_PJYPEifheZ_rfGh11vIpgeEzOKC5qKJo4g_ZP9Iu-l9mfzN4a-VJN-qtcP-wsuFbzvbWEviN8SAwqQNv3DwQNJtAnu7MIqJj2ZqlzIVlMiGMwLSm0vmgMUeZEnobvx7LpJmWv_33mjxWGCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRhhhfSSrJP_3qmO2UhisCnLMO2MkOGP2n9hBLXcC6o_Q15DqsRzNcVvgPw6AdSY57fNRHL4B5s8W5kmkr2XklAEcHQ7VBFHZIXbhFTE-w30j8Yg9fSiF9HTx83BMw8FhhG3nF-cheN8oJ7MiKWBXJqInxFxbBF5qfajVpto_xnTIx3osLekVUgcye-LXL5ejcwszUTALmYwwhBWwcaZGabJdJg1uOxt_bzvTdod4XTRg8gyqTe2CvzLgfbq54CInAgIvYLA09WFl17dDrxyQJt8ZFb8xpv5b80iDyz7lAW4Cq9HhHPX7hndzjdvm0Yfwbx1StX1uVHZaXEEnEmpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK7oDUDR0Lg57fvSypTz4XtISIJZ7giIkFSvZCNXulBSgefQUmLBiq462Mvo4gyy5apAeRk1BAbAQHOlTs85y5sYwnV1YjtWFS8XDvpMy0WyulwZZ3KGUHYSUWD9ii7tFyjyfYBJ79xtUlO758sA99zX2xms1L_922SCaxIQxB5xb16oliO0sj2EdMVJILnCEpmgxmmnuG3OaWkjNIuF4W7s99NE82RooNum-pnJUpB6YSrgAdeftwQXG78Z3T9yVpvekm74ihYsq2jVTM_uJprvFb3-ca8P22bnkmotbTFR9R0lc_j6WAuHAn1jCBxheDFxnx5ACcreWxWyDuCong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhOhRsIONcHbhyDqQg_lJtnYluf6dlG2a0SPTZnrTnBNuphUJq6FxEYDmTuPsk5ODjyD70mD3orZtdw8zjKwLCGetg-X_sv2Gnzgk0_GchpK84Zf4itRWZMBi597cfJ_ggXj_JcopWXgHNtjqT8aLofylcnCsX9AObKlUSCpvYgslL7D7Ad3h2UCj_aZB5n7Y-7zdDgA2lWEKCuKDjBrNDmxbB7By3sNl7w5H4DWTXkf4CO4MpyUpgkSdBP5n-I4ZmJBsTjMeptNZE2BijPb4gyNlczlX9rSv6sCP2VMQAWAcGhHTZzGzwqYtCJQoFpRTwXG-tcE-qKXsTLsn3y9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=vo2cWCLGWze_0yzQ-c1vqvxuyGdiKo0m8TJJKK35iP53QbmzEWpEE8A0uwvbervS2K6byysUSczZc2f25RwMq16qzbn8312avPhj7du6rKDICFTBOdGSv9j3YeWJJznoRXUHgjqb7muDbwYt3qycXnusVaQ7eNjsimIUV67fLFwHdoY5qhBY8wZEJfw_H3ET4Tvv1oe_LubYqZXg5gSvilqRKGQsgN3YSqmoWaiX-cK6A830qYWWb3LqmMKU7cpv1q7ivL3bXw4KdGIdph8azBTTRC4gdB-pCpEfTETiiz95yEYg8vF1U85SahCDP4FUsC8GZhGZd4k3lQ_e26P9-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=vo2cWCLGWze_0yzQ-c1vqvxuyGdiKo0m8TJJKK35iP53QbmzEWpEE8A0uwvbervS2K6byysUSczZc2f25RwMq16qzbn8312avPhj7du6rKDICFTBOdGSv9j3YeWJJznoRXUHgjqb7muDbwYt3qycXnusVaQ7eNjsimIUV67fLFwHdoY5qhBY8wZEJfw_H3ET4Tvv1oe_LubYqZXg5gSvilqRKGQsgN3YSqmoWaiX-cK6A830qYWWb3LqmMKU7cpv1q7ivL3bXw4KdGIdph8azBTTRC4gdB-pCpEfTETiiz95yEYg8vF1U85SahCDP4FUsC8GZhGZd4k3lQ_e26P9-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=G_7XG9h4y5U2KTjua_3BDPpeeUcznrPCzHYSLhh8psuhXPLOGhavqe7dDJ9l4bNItGbEP4vndeqbDPe63lXgVV1JH37zmYUvGVZyVXGvz6WgIZJVhSB8RIwg_ibhj1rWd3XJ3o7spZnUEwQ7Z4DBlFKAdtF5at-S7INAb8m5ERhyiefguVN_RNldnVYB6gIUAWDLei_4ENL-Q3eEQeWfE36ybmdl8Y4IFFEQSuCvTbOo7ZWOxk-3j9lSDMwPQgsWBFoXRPcDznnQHMKeAtlcAE4UTXOLakIUEQ8bZ_RIxx3h-bN6l2tW8JOtNHgzCmE34PGEGKrvTVa6VGcWT9u9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=G_7XG9h4y5U2KTjua_3BDPpeeUcznrPCzHYSLhh8psuhXPLOGhavqe7dDJ9l4bNItGbEP4vndeqbDPe63lXgVV1JH37zmYUvGVZyVXGvz6WgIZJVhSB8RIwg_ibhj1rWd3XJ3o7spZnUEwQ7Z4DBlFKAdtF5at-S7INAb8m5ERhyiefguVN_RNldnVYB6gIUAWDLei_4ENL-Q3eEQeWfE36ybmdl8Y4IFFEQSuCvTbOo7ZWOxk-3j9lSDMwPQgsWBFoXRPcDznnQHMKeAtlcAE4UTXOLakIUEQ8bZ_RIxx3h-bN6l2tW8JOtNHgzCmE34PGEGKrvTVa6VGcWT9u9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=cWFlJBoUTbl8CoVLQZMTzN9jDlgeXBRHdDY8a2TeVKSrQCuH5emqFnG8oks_kHVXBIBDery4tXni-Y-oYEkcmBdqikAGe72ujHOdFhimuJaDRCSnnQZsrZ0vH2wnD32ouSn361UR_VdxaCWLH-z3tGCWLWULyPj07auG33Suom1HCZN8MvCJjqAuY8Vg6t9WmPD643VeeyxPb-EH2wLfJVEZKwY7LZgBvEJI6ah1nijE1CMUJlB2v3hVx5vMAz1Uo_hGnIdjhzW56tFLLKIPn8LOWH34ednDxwSRB8unj2f8XDo6B_piNuUNWFZQrxEibvQMqI9xiAIgi7K6g48S6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=cWFlJBoUTbl8CoVLQZMTzN9jDlgeXBRHdDY8a2TeVKSrQCuH5emqFnG8oks_kHVXBIBDery4tXni-Y-oYEkcmBdqikAGe72ujHOdFhimuJaDRCSnnQZsrZ0vH2wnD32ouSn361UR_VdxaCWLH-z3tGCWLWULyPj07auG33Suom1HCZN8MvCJjqAuY8Vg6t9WmPD643VeeyxPb-EH2wLfJVEZKwY7LZgBvEJI6ah1nijE1CMUJlB2v3hVx5vMAz1Uo_hGnIdjhzW56tFLLKIPn8LOWH34ednDxwSRB8unj2f8XDo6B_piNuUNWFZQrxEibvQMqI9xiAIgi7K6g48S6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=TG-HwvHnlVrhX6yqgcI_lvaVzXAA2MxldVOO3WSTLTPb0RJerPnlE7fRW1loAtHeqTi3Q4KI-hMOqRF-vlC5es3kAuOx45X_2RgnXcxhN4b4jImFw2-dtK4eUrCTNsLHtcZBmYWAsSd5vchn3_wn68ILLbIwnIMt1x_WyVuehmuAjwN8JJ3YK3JX58VmSP72P8OoVUiqe40yG1qDD7XOoL2HR2MYRopnv8TZEtXAiNgbZgtD84VHsZLbG_E50j9aNFuQsizme3e3LDHh7pHPCAliLUZIdXSKM9vR0mXqiyARA4Y9WrWFffSg9VPZntb9yyOtVyuBkZEGS5MRrkjZWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=TG-HwvHnlVrhX6yqgcI_lvaVzXAA2MxldVOO3WSTLTPb0RJerPnlE7fRW1loAtHeqTi3Q4KI-hMOqRF-vlC5es3kAuOx45X_2RgnXcxhN4b4jImFw2-dtK4eUrCTNsLHtcZBmYWAsSd5vchn3_wn68ILLbIwnIMt1x_WyVuehmuAjwN8JJ3YK3JX58VmSP72P8OoVUiqe40yG1qDD7XOoL2HR2MYRopnv8TZEtXAiNgbZgtD84VHsZLbG_E50j9aNFuQsizme3e3LDHh7pHPCAliLUZIdXSKM9vR0mXqiyARA4Y9WrWFffSg9VPZntb9yyOtVyuBkZEGS5MRrkjZWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=AsVozOb9kRLnC4JW2BR-TnV0Sch-chw0qPuGErVARhvqzeKl_gyNC45WW1c7qlZHaR7rJdTnSNzXDyitjU24j4JJ4XpI6XQFNqhbSvb1TGb-3svE7BwGHB4pHIkiDd2KdyhCQ2HX3lGkx2g0IRwnaHkcSUXcp55fD2pwp96Ix_XZvoFNelXmSsWUnHjPG0cxGqWaRnEZGX678MHmChsLvJbU7PHGjfHiAKExkl1rWDPzHBmwXXLU0sCSyrOG_noULyiyogmnZ_rfvfv5jh2ce5Aig1suzfNzSXqQg1d-CMKmh04WFSwPhltvf_cYnBvyjj9-mVC7jpFXfw4mMEDbBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=AsVozOb9kRLnC4JW2BR-TnV0Sch-chw0qPuGErVARhvqzeKl_gyNC45WW1c7qlZHaR7rJdTnSNzXDyitjU24j4JJ4XpI6XQFNqhbSvb1TGb-3svE7BwGHB4pHIkiDd2KdyhCQ2HX3lGkx2g0IRwnaHkcSUXcp55fD2pwp96Ix_XZvoFNelXmSsWUnHjPG0cxGqWaRnEZGX678MHmChsLvJbU7PHGjfHiAKExkl1rWDPzHBmwXXLU0sCSyrOG_noULyiyogmnZ_rfvfv5jh2ce5Aig1suzfNzSXqQg1d-CMKmh04WFSwPhltvf_cYnBvyjj9-mVC7jpFXfw4mMEDbBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=iar1tRk7tD_a84D3gi84L7EHija-OWAtjxLuCwtPpHwdTpw8BqyxUNFtSlHTnrX-5E40SDU1HZ9spjcLbOKvfkaGsfmfo5TdNNwAWBQeImZ0w_vi3RYypztEj3xpSjjMoFkVk96g8Twm8aOQ45xFqPBXyY3cS51Qy42X7nOB6vJhVjUdrLC6A7dnRg7oIlXLpncxy_4UR-rt84wUKD1OnczwFTHFiUFYjgi1GppStIiagc4zd3NI2c2VrOk4qP3PFMz5gWXz2FpA_CIoEN3CPuyUOurJWX2l_QILhGRUdb3TMZfLyfpFJv4c676cFiPMEGsGT0slk0fM89djUBobjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=iar1tRk7tD_a84D3gi84L7EHija-OWAtjxLuCwtPpHwdTpw8BqyxUNFtSlHTnrX-5E40SDU1HZ9spjcLbOKvfkaGsfmfo5TdNNwAWBQeImZ0w_vi3RYypztEj3xpSjjMoFkVk96g8Twm8aOQ45xFqPBXyY3cS51Qy42X7nOB6vJhVjUdrLC6A7dnRg7oIlXLpncxy_4UR-rt84wUKD1OnczwFTHFiUFYjgi1GppStIiagc4zd3NI2c2VrOk4qP3PFMz5gWXz2FpA_CIoEN3CPuyUOurJWX2l_QILhGRUdb3TMZfLyfpFJv4c676cFiPMEGsGT0slk0fM89djUBobjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=LPDAS1yiIzcRwM7sIWvjjlsJWxi8ZdRYtn0j-riKTo3Ynywtpz0Epu5jM7AsocnI1BRzKG8ux3-6kH0r_-go5D4XcaYrP_SZTH2tYcYe1daSCPTJ8GKzYmwBjassZusl405PYSZYrhnXfOzJhpXLO6Lie6QvF3Ks8MUTZQmUEg17o7_Lz9eJPQvByIJZ88bZJSvwOxMWoPYrnxowyP75O3yKQR5ME9Yj_uxyGPxnvaDvMR3t2qgbSqUwANjUL9pGF3MXFzuxK6rEqwS_RF4-s2A4LrigpS23fhSbHSLpbyKGmZR2h3wG3WCaKvLVykSnX634C5iMB0znl5biZrjvbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=LPDAS1yiIzcRwM7sIWvjjlsJWxi8ZdRYtn0j-riKTo3Ynywtpz0Epu5jM7AsocnI1BRzKG8ux3-6kH0r_-go5D4XcaYrP_SZTH2tYcYe1daSCPTJ8GKzYmwBjassZusl405PYSZYrhnXfOzJhpXLO6Lie6QvF3Ks8MUTZQmUEg17o7_Lz9eJPQvByIJZ88bZJSvwOxMWoPYrnxowyP75O3yKQR5ME9Yj_uxyGPxnvaDvMR3t2qgbSqUwANjUL9pGF3MXFzuxK6rEqwS_RF4-s2A4LrigpS23fhSbHSLpbyKGmZR2h3wG3WCaKvLVykSnX634C5iMB0znl5biZrjvbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib1HzbWEaqi9WdvxdgY7FbEPw8iOqf0mC4wxKI8KxghKDv17h9lIZxlu9LCEKYUwNGuIc8LCZYQESuQNLJEp74Z8ii7cr9Yqjy3yznTtQH-NkCdwZ3KAF4_Ci0Hz19XC86PQ4BcvE_n3zON_ZBuXJZquYa5q4f99NUZiVInJmDQAL8JPfYsYgcvfQ_aw6o2okDOgj7rKMmXRGMwsHibD3PQfyYpXeTkhpuf7C_LMAYXZ_JYcTuHvXKje9COLqLnWLpmMqVEW7HRVl88PTGvC9vWx6uvrRwv6r3EyRTXQu_EMOurUhRw9QvuzL4XZerG92M0uDSHsBsuPQFcuLgZdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=A4Is3Hd7kQ4tev5IM0ME0Eq-45kh2UNmWXHopOkSJadKlcnFOeGDtJiuIBWWI12e13Zp4y7DHBuSoX8bL_1u2Y77VPJvuUio7Zbm8ROuWa4wtOPo440FUHusWTEVh3fQuxhp5clHF6652bjGJzifPnTadExe1oSVLVIOhvU8E0zTL7bxTdAFCaDs9_kRbi6hMh24ward6fn-VcNOI7dv6A7NXrX0CpiLalHPc0Vo8NUpj4vhmKvUpQyhL3-VJ0_DpCT-VxYE2KQpq5U4uJl_UXxnLOoE0TrhCqZi78ISijYrymZtvUDwL52i4yDARRaCJdLbRtDw-sunDwVQ26W3qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=A4Is3Hd7kQ4tev5IM0ME0Eq-45kh2UNmWXHopOkSJadKlcnFOeGDtJiuIBWWI12e13Zp4y7DHBuSoX8bL_1u2Y77VPJvuUio7Zbm8ROuWa4wtOPo440FUHusWTEVh3fQuxhp5clHF6652bjGJzifPnTadExe1oSVLVIOhvU8E0zTL7bxTdAFCaDs9_kRbi6hMh24ward6fn-VcNOI7dv6A7NXrX0CpiLalHPc0Vo8NUpj4vhmKvUpQyhL3-VJ0_DpCT-VxYE2KQpq5U4uJl_UXxnLOoE0TrhCqZi78ISijYrymZtvUDwL52i4yDARRaCJdLbRtDw-sunDwVQ26W3qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ZqFWbwv5_z-MOZEJxqbXK_F8HOcxQkW0h8VMpthTJkrAStVK1Yip6KqAbK_h37W8PB-VVABNaf4PPRSbZUN0Ob6Jz66TWXnh-FvPrCMA9qnznZ3jHxn-KIER6fQrXHBeJv8zilq1fnqxKcd2w_vD6jm8-deVeMPVBYV2FvM-sR0lbIKMmjBSwjzgJuD0XncBNGbo7FBQ9vrcoyp1X5FRjW5At08e_wQU1JvQuKFwcUapHK3kxRuLZFrcGXddcPVl0Us95Mrb_8xah-mqma1UqSSo8fTD8qaKFQKpUMnmSvEEh46_00-xQ7F0GagM9uN0Mu6Gzb0OhLvvgag-KVUJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ZqFWbwv5_z-MOZEJxqbXK_F8HOcxQkW0h8VMpthTJkrAStVK1Yip6KqAbK_h37W8PB-VVABNaf4PPRSbZUN0Ob6Jz66TWXnh-FvPrCMA9qnznZ3jHxn-KIER6fQrXHBeJv8zilq1fnqxKcd2w_vD6jm8-deVeMPVBYV2FvM-sR0lbIKMmjBSwjzgJuD0XncBNGbo7FBQ9vrcoyp1X5FRjW5At08e_wQU1JvQuKFwcUapHK3kxRuLZFrcGXddcPVl0Us95Mrb_8xah-mqma1UqSSo8fTD8qaKFQKpUMnmSvEEh46_00-xQ7F0GagM9uN0Mu6Gzb0OhLvvgag-KVUJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=ede_saILdwlM-L64jRh6-GHzBDaW97_fZtNvCIc3efmBj2GvdizTebkECygLlPd5Ly17NWaMFnvwMXW9sSAVbGkzMJqrz-OjOlhdGj3UC36DY4F4i_eGcR7HJ8sFCevLGgZuTpN4Ee632Mk9o3O0c9mvNh72783fVB9Xr2B2ONXLKw0qcaQ6udfcfFuHvcmct3bdOwUj2DmwOv7CMceAriy1zxMU1_iMlPpi8W2DWPlQovE54gxnxAzOc2Ejg_OmBa-WcZ0vroh5fkhHCixQsG3U270c-5KePCVUC3_PDwIMd0QwGw8b8IebJjGAoNUYBOyUk85felLDC0QPl8rIhxaEKmZBWS4XYwLrDd9w-oJ0VteYq_yA0JG0b1K3kXmb122aHaFl59lHsfczfSJlNYSukWfvZTryDG7NnJYbsnXly2-oqQZTxcQrLOYDFRgcmUgtSqT9d7Pd2S-2MbrvoeNSwuok3854BFYSRpnsbQwHZlypwP-ADBHLd83yyFTsU-NK_y-6APGsgRn1YkYOi_wSBb3iSh0fjesyXZ9LnMIUFRZQJiWqE3D_o-oXmozFQS3a3YQwaqT2iclGLsG1r4KHK8avew9F2YyzMYGNtgaPfV00ybrhzvEKF8jW_3LopuoVtsiCZay7CLaawrY0kDxhiVho4YLRvUK2bjsimoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=ede_saILdwlM-L64jRh6-GHzBDaW97_fZtNvCIc3efmBj2GvdizTebkECygLlPd5Ly17NWaMFnvwMXW9sSAVbGkzMJqrz-OjOlhdGj3UC36DY4F4i_eGcR7HJ8sFCevLGgZuTpN4Ee632Mk9o3O0c9mvNh72783fVB9Xr2B2ONXLKw0qcaQ6udfcfFuHvcmct3bdOwUj2DmwOv7CMceAriy1zxMU1_iMlPpi8W2DWPlQovE54gxnxAzOc2Ejg_OmBa-WcZ0vroh5fkhHCixQsG3U270c-5KePCVUC3_PDwIMd0QwGw8b8IebJjGAoNUYBOyUk85felLDC0QPl8rIhxaEKmZBWS4XYwLrDd9w-oJ0VteYq_yA0JG0b1K3kXmb122aHaFl59lHsfczfSJlNYSukWfvZTryDG7NnJYbsnXly2-oqQZTxcQrLOYDFRgcmUgtSqT9d7Pd2S-2MbrvoeNSwuok3854BFYSRpnsbQwHZlypwP-ADBHLd83yyFTsU-NK_y-6APGsgRn1YkYOi_wSBb3iSh0fjesyXZ9LnMIUFRZQJiWqE3D_o-oXmozFQS3a3YQwaqT2iclGLsG1r4KHK8avew9F2YyzMYGNtgaPfV00ybrhzvEKF8jW_3LopuoVtsiCZay7CLaawrY0kDxhiVho4YLRvUK2bjsimoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=s9O0XGnG9iv4WCGH1UPqGuXhrPnF1JTqNQ6xlcDtisuIP7QkKzhyQeBARP2p0aARZN07sl9njuDVprwTBF7EgH84_o7G9f8ryfXiYFqfzJZbbA_GhkYIkxdJCw39WU0Fcgc-_6-OZvfG5yfZHvvohLuAjON-3N4pzilJAUegG6t1vY_1HBIcxNxd4z_VmUECVUYkTddRRZHBcZFkUse4joUMMZ9-buiUYsNyj7CxTzeVQC4IHZu03WJ-wuQGIJ1tn4reoypptn2IZ_9o4De-ALmrknaif1F0csy1uSW4C7OwkSFsHet5g8M90wjlNyXvVknj7v1R9KgsZXCl5uKYjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=s9O0XGnG9iv4WCGH1UPqGuXhrPnF1JTqNQ6xlcDtisuIP7QkKzhyQeBARP2p0aARZN07sl9njuDVprwTBF7EgH84_o7G9f8ryfXiYFqfzJZbbA_GhkYIkxdJCw39WU0Fcgc-_6-OZvfG5yfZHvvohLuAjON-3N4pzilJAUegG6t1vY_1HBIcxNxd4z_VmUECVUYkTddRRZHBcZFkUse4joUMMZ9-buiUYsNyj7CxTzeVQC4IHZu03WJ-wuQGIJ1tn4reoypptn2IZ_9o4De-ALmrknaif1F0csy1uSW4C7OwkSFsHet5g8M90wjlNyXvVknj7v1R9KgsZXCl5uKYjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=O9-tYqa6wuGnjLg52-MRGjWPFXMryame_--HBKgjHyWufs9XTgGWgklEHmjhmXSxdQTfInHh5F_TPHEoELBXsWgh5eXcKuxKkTEb7BqQCpGVvhTzPEAvUypnqBaG7_hryhYgSS3LmzdvIFt-mXKH2cGm_N9pnXjz095zf8MZ_Lx2xk99wAPR7DOAJWXxVgyPaEDEVZmF8zabkZZJypEQKbiKTzgzyiImr-R-VRsePsovZ1FL2fiJVi2B6b3fWR4a-O2v0yDdhvmlkF9WU9ofamgjg_bV0Sh_t8DIv7hI3TFjAu0QCb30oAoBK2iom0S45fYuLSaN3b73L6u0sY9L1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=O9-tYqa6wuGnjLg52-MRGjWPFXMryame_--HBKgjHyWufs9XTgGWgklEHmjhmXSxdQTfInHh5F_TPHEoELBXsWgh5eXcKuxKkTEb7BqQCpGVvhTzPEAvUypnqBaG7_hryhYgSS3LmzdvIFt-mXKH2cGm_N9pnXjz095zf8MZ_Lx2xk99wAPR7DOAJWXxVgyPaEDEVZmF8zabkZZJypEQKbiKTzgzyiImr-R-VRsePsovZ1FL2fiJVi2B6b3fWR4a-O2v0yDdhvmlkF9WU9ofamgjg_bV0Sh_t8DIv7hI3TFjAu0QCb30oAoBK2iom0S45fYuLSaN3b73L6u0sY9L1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0e7ZbHyVCyUqFikLTd8qcvRWU9df1YrRlWjDm7OJjGk0k8LYEB28JJ35OCYmFyHqFfnrQtMkJAVgpNgSUr1O-ZjkxmC570iyhHk3mrVolVhEwSBnHm2c-K03VhU1QSNjKbpnuuuB_GluqtyI_REfLK8eAIJ6XgWixbyTrxHb1ldRWcXeDdk6eG2qSyeaZYoRsQw-Oaa2p-GaPnMHPD4d1YwJG-8GAf5fhuMHdKTI5wQUNw67fd6wsGzOPk2FZI-I2XWFlnjBFa11mZIWasa0CGZwFIOnYAScyCYZIaS4IWcTYbR_LA41c-71sVbEDC0z2uX6goyu6ci1ZlncfYyRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxirdSzKeR8MebHfGcG20ROYU7i04kI7dKQb5FukDNdpOCp9t9JAIAin0gOYKgqsm9uvI96DkrJZj-9BEgylYjtvuBn5-hHQQbnz9kFN-kHq-pL4LPoJHkaZ9aJj9UFE9v9EHrAn-ngW8KaU0cBvv9dub4aqkxWj3XsWmdz5NE5-WQXFTWWKG42CGW3ofHKbM8IHiI_L0ZeSXXy5K0-xKzRZbzwvUjfiaspkrv7FalQHriBhf8JbjWb4yIk1fZJl2pi0QE1Novn_0Om191A6lWUftTrb99WEsrv3QF8JSvzAz9rs1VCyjkyPPATy0DCCRtg5LPUMrAEaFkkzzEGosA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=na7Gl3YFsSl2xAQZhrRB4M3Ls-RFunWDLsvCrvO4E9Em3Q-txKiRaw4nLj9Kvctn1HXJ3DqQ6pmtnSrdPVsJEMKR1oQBNzH6tcPQXUUhKlNSs59XswqeUU-FRCB7xMvfU8F8rnHBfnGfu2-098jAsrgBpkmO0ZvZ5moSO9tzTTzhzXkFqoJGS3mHVVxzKfY6LC-UnUv7bZ5CrtUKBQEiWO-SLpgMbnV4Akbr_ypHGGBQAHvSacj3AVNtRsDwAT7FdTjVVBPWA3_uCpi3MhnL0iIWh9zz3FWydUwZAsbhLjuJlZ1caq0al4kJNfdfd2PCOHKCy95GQDSAtcdsZbl9VoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=na7Gl3YFsSl2xAQZhrRB4M3Ls-RFunWDLsvCrvO4E9Em3Q-txKiRaw4nLj9Kvctn1HXJ3DqQ6pmtnSrdPVsJEMKR1oQBNzH6tcPQXUUhKlNSs59XswqeUU-FRCB7xMvfU8F8rnHBfnGfu2-098jAsrgBpkmO0ZvZ5moSO9tzTTzhzXkFqoJGS3mHVVxzKfY6LC-UnUv7bZ5CrtUKBQEiWO-SLpgMbnV4Akbr_ypHGGBQAHvSacj3AVNtRsDwAT7FdTjVVBPWA3_uCpi3MhnL0iIWh9zz3FWydUwZAsbhLjuJlZ1caq0al4kJNfdfd2PCOHKCy95GQDSAtcdsZbl9VoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uurof5mbgcRwQkvzsqZEt0vcJuFrTzv0JR219A_1ZLuVh0wxI4qNAHKTAIP5ElVWc06u5u9wHcPh7yD8ywp5puYrHXiiIFZsCVmDkWv6uSbpefI9hWOFQC0UWcvG2lJYJHz8K63sib9TNM7KOle5xoLKFVtkGnZ-Jvhp6zZNqa6iEGxILmlAQ1tEEq3H3_1_afeHn881hQWI-HXoIQqn9eApkQw_QTI9c2pAXIAfnQ0qHnHKKjMo2cVx0GZbXxsAdw0bkgN5kne86ouTN69XXgvKbFefPGD8w7Fm2Uc0pE5of-sTmY060Bj6nhjtja7ypyrxEqseL_pjXXc2hp23TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2cibuKrXWE5bNvgiN6d9nZ4OWMX9s0BkbJC9_EdPcVK7e1vuCzHYLBB4lRApT5uLnEBsfNtzAwkBHiaiOcMao0bOwcdflE1h1PnRjRmW2nxwaSRHNOxXie-kYOB3TNaPEKSxMHOeE8qHkG9Nh1OqKXwHbdzHzBaYzvxQjmJCr0ZHMW2QqhZuTcFNWO0tdwm1iuImaHVcKZl7sYc-EtPdrSiCvL3ghRS9-nyL89KZE9BwxJe5ltiUw-BUsZms2nvwZG9CLPme7fQPQwEJT14LiZhlIR70fZmzmMp3YWk-StzRSVI9n8dsqsrBHs05U5yrUsng3Ny_0ZG5CIjawRBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYQGAjdyfBeNsFwTYbeMLRlKJxK__eboDda0b9_5iRsac3Lg7ZhEs-eZR8litJ27JpZRZge3A99iTZ_0qCrwbhR_pNPgjyyG9B1GqVReozlxHkilzhYQZWRNdq8NoKZi7iDqrpQkMUob3C5DdcdoJyzpRSP4pcYvMX7XNJ2xHyHEycAkM8AILIyzZLZg72kj_mDdecAtytjcrkiG2nxxADROQ2nQZHmh_irPAeAUinjLmMHYvcUQ8jhOhI_tRsDWL1RRXrg66TDYktu_7jwGZd7kHIqPLJYHd29Mc35xKWh8h6Li13v8NTATsKJHfR346XFPPzsZ-rmMLxBNPRVT_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huRS8GUIauHy9rzBLKsBYVRCC2bP61185TKDfnsByAhXUQgInBoP7untlZcbia0ithI0BXcxjRG0eK41SCWYjLtjUylMRcSuIqH0Ifu2apFDqdynjy_oo4Cx4u8xh2Epa_SwiNpQ2R_U7RUfFK2gyGlO5gb3SuV6Y8h256-IYAIQwPm9bZOVWcfEjqJWCoZj6R43S4NxeAmzyneMaa5vE_sGTS9iRgCsVMGJNJkEsNc3zoRnzdAhAKoYXGmuEdZQFcbmDLDTLqylcWT5ok_tE1vehH3jN-FHUL97WPcsOSuDgYEeYbU66mfx5O43bM3B5s4xsbpAmvnpCbZvahWvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=iP9Ar5UARCkjrywxwuOsM9eOzc3i0xzSk3BR8szFg69qcpP9FaZLIMw8IPDgkhFIiGPGomqHpynvN9Yv2mwq6zo2vlpA9qG6vs_E5qQgbBaxRlqF7s_N0XTY2wQaRjd8zdGAzLF4QdGsuzPbPrK8UP63xC1ks8rgcGESyHUteedtRVw0dgIdeAKikK3fojwDCgTDqBB5f7-TSWpOcEz9ioRNzQ1kFKuDN0-u3pCiHb4_IWCT20pb0bvyFUiSFJUkW4Iz6LWaj-oIX1oeM1_VwvSCXGb8g3WSAFpB4EB2XFFAiesgLStoCKrQ4UYC3fA_O31Lm5vPq2kFAUw7hSEs6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=iP9Ar5UARCkjrywxwuOsM9eOzc3i0xzSk3BR8szFg69qcpP9FaZLIMw8IPDgkhFIiGPGomqHpynvN9Yv2mwq6zo2vlpA9qG6vs_E5qQgbBaxRlqF7s_N0XTY2wQaRjd8zdGAzLF4QdGsuzPbPrK8UP63xC1ks8rgcGESyHUteedtRVw0dgIdeAKikK3fojwDCgTDqBB5f7-TSWpOcEz9ioRNzQ1kFKuDN0-u3pCiHb4_IWCT20pb0bvyFUiSFJUkW4Iz6LWaj-oIX1oeM1_VwvSCXGb8g3WSAFpB4EB2XFFAiesgLStoCKrQ4UYC3fA_O31Lm5vPq2kFAUw7hSEs6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=cT0Afm1XaQakb-xn20ysOsw_FqcZK55aAQwU0bpLTc22qVv79-fPJidHZ0YmxtH3WxK5mfrzUOTw8Vr6JkBouSdzlRxyHbAMfZc1QXroy8mNRaMCy0tvAjmH0oRP_9l1llLPFseV9c7kts8QZg3dt0-8q2S4Za7sr__3X7OiEes4wzwBi08bsgktRzV4rsafxXHfLzyw_CEwQFSjq-K4FjCvhto3_vSnXNLDgHnPNlfCDFYgr9ykQaYEosTz02eWBZMPLOxxO8V15r1zhy9_YD-RjpEfwQ0C_ttqBuvzf7PGGFM0dpF7MyJFKHr-MHtQEwx2IftydH9E0jC1husPrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=cT0Afm1XaQakb-xn20ysOsw_FqcZK55aAQwU0bpLTc22qVv79-fPJidHZ0YmxtH3WxK5mfrzUOTw8Vr6JkBouSdzlRxyHbAMfZc1QXroy8mNRaMCy0tvAjmH0oRP_9l1llLPFseV9c7kts8QZg3dt0-8q2S4Za7sr__3X7OiEes4wzwBi08bsgktRzV4rsafxXHfLzyw_CEwQFSjq-K4FjCvhto3_vSnXNLDgHnPNlfCDFYgr9ykQaYEosTz02eWBZMPLOxxO8V15r1zhy9_YD-RjpEfwQ0C_ttqBuvzf7PGGFM0dpF7MyJFKHr-MHtQEwx2IftydH9E0jC1husPrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRAbeWuy3F7hCmkxyss6Fa6yLBL4Pd1xyLkYMyABVEacHa9jST9AMTQ7Zgkmffz2kZghJX_CA1PvUpGP4ZnEGYJbc-wXuiNYSoK5xBWp_TThlMN9-9bK3-XyicFzKC80ne67SBT5Wsw_wYJDyO61qUck-bbUkfeUdQNroh37AxZV2PxTLrJTtpCsdwSYGkJOxE23ifAujIy5o0Sj_WQ5NpA_2GEv5XaDlgiEt8gO9gDCxn6SYCg2k_OqLUBPjCMqLWtTLYMW7lF4I5qYnlo0ViPOvVVIqc3lTM5OhAP95RRtjq7xQlRBVbIu46-NiHDVCAzb1A8g5Ue3-aKnv7BaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=BChYym3hskKU-n4MI_P_2UEoKqHY3maHKFMQAIV9paoXZdujJ3iE2H4X9R3tXs13Noog6xtw0zWZU2ScrNaHLzh7i4NqSFcThCEKp1RsiM7W7sB26YJGioZwcTBD5iHiJ-JEhA1AayOFrgQkg_vzky8iCMN0wTfNDzxjEu9akeFB_dQI_cb6UrfZwvADTARlZFnbitm6iJrR7p5EwqSxTrt9HSmL7Lkvn4OEbx8zstfe90idygaqDhyxX90AkgqkWrKM3LWcBeih3CMxGuh2Lru-d8S3Zw9LMifGa3S4u-LJ2_mEJSFkQpip4OswpducHyU35Vl7mlTCvz6hVNI6_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=BChYym3hskKU-n4MI_P_2UEoKqHY3maHKFMQAIV9paoXZdujJ3iE2H4X9R3tXs13Noog6xtw0zWZU2ScrNaHLzh7i4NqSFcThCEKp1RsiM7W7sB26YJGioZwcTBD5iHiJ-JEhA1AayOFrgQkg_vzky8iCMN0wTfNDzxjEu9akeFB_dQI_cb6UrfZwvADTARlZFnbitm6iJrR7p5EwqSxTrt9HSmL7Lkvn4OEbx8zstfe90idygaqDhyxX90AkgqkWrKM3LWcBeih3CMxGuh2Lru-d8S3Zw9LMifGa3S4u-LJ2_mEJSFkQpip4OswpducHyU35Vl7mlTCvz6hVNI6_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=QtG9OcUU86KbZJlbYBFOTFDZ2OKz5ZSAyMsDpLPwYL_mxanfuMNBdF4rZbvFjC2S4RcE4K75XTcXLj6bA_BBrHRRDDhnVR4jM9PS4QOuSHzxdtqQZ8pfj_M_f1os3rRfR4vrk5z-ZfSjib7eetvkZ2rY9RdqYtBKkvjTfOxgJebY-CqWuzbjUx4KiN2S8GP5KkpijEpXiCFq2qESFLvm-8GVtx6jRSXys75Z2R6zB_371gUo1WhebDZB1t_7xW_uVqpg2W4T9n6eORMRqRe37OBhZtWVIgyxhMMYkApynrT8ChPTjMwTgDDtfTMBuwV9XxXfQx5BEDJ5d1Z9cIBmUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=QtG9OcUU86KbZJlbYBFOTFDZ2OKz5ZSAyMsDpLPwYL_mxanfuMNBdF4rZbvFjC2S4RcE4K75XTcXLj6bA_BBrHRRDDhnVR4jM9PS4QOuSHzxdtqQZ8pfj_M_f1os3rRfR4vrk5z-ZfSjib7eetvkZ2rY9RdqYtBKkvjTfOxgJebY-CqWuzbjUx4KiN2S8GP5KkpijEpXiCFq2qESFLvm-8GVtx6jRSXys75Z2R6zB_371gUo1WhebDZB1t_7xW_uVqpg2W4T9n6eORMRqRe37OBhZtWVIgyxhMMYkApynrT8ChPTjMwTgDDtfTMBuwV9XxXfQx5BEDJ5d1Z9cIBmUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=JQZNjVe2ZIHqElC6zy4bNNZqnQNv-dFmS4lFfQ3-mBDMn7i_B3U68ZSvumW0_GXzhsQe8jbCo6HI9IQS0L28B-pNk8CLuYf2jyt0JcGYAqT9RCBdfU0S5Ae1tAhceCsrGNRKCg8igYK4egNvYZzCQ70Ei_cl0myb6iB9zguT9Axo3aOQN4i8lKTpu_u5fQRcPLKd_Q0verSn9R82ozzX5F0EUmHuTT86Y_KumWGD-GI7-oICwJ0plfvfrtjkJ9260ood87bELMcpaOrBbW60t0YySC_tDnSQgPJk2WNH2IFdMGoXtJoTtbxHW38V4ue4lI8UOEzHOSulAUtmeppZWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=JQZNjVe2ZIHqElC6zy4bNNZqnQNv-dFmS4lFfQ3-mBDMn7i_B3U68ZSvumW0_GXzhsQe8jbCo6HI9IQS0L28B-pNk8CLuYf2jyt0JcGYAqT9RCBdfU0S5Ae1tAhceCsrGNRKCg8igYK4egNvYZzCQ70Ei_cl0myb6iB9zguT9Axo3aOQN4i8lKTpu_u5fQRcPLKd_Q0verSn9R82ozzX5F0EUmHuTT86Y_KumWGD-GI7-oICwJ0plfvfrtjkJ9260ood87bELMcpaOrBbW60t0YySC_tDnSQgPJk2WNH2IFdMGoXtJoTtbxHW38V4ue4lI8UOEzHOSulAUtmeppZWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0PQLqNiGP5CaQ5YEDkYvdtYzJhxhkWjYeirJG4FTmQTM4bMJhI9B0A5U4ZvOnp8frvZFCY3vvD2msu5fV8hXk9H8---McVyQ006BuxBV7RfGlifJD-a28Xonc7fSLYHraXp-JtkyirjawjJpfg4XUXlZPdjft8dqisBVTRY24iWc8qH93m7jMXOZhAPg6xLZglDUzH2P_ZGD6JaYIgZe7tU0N4sVmQjvnLDJ8q24ZoKiO4ivefACYqVuuMmFGSdLx4TuydRGYFWzDIaok8JW-W-hoU-LK8sT2JuuAefpIZdO3LZuK2GdnJPOHj56bYFmjsjiqG4PCIIJvRebaWKUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=G6Z16AJ7yGcTQOqNIUoPEB0Tft8MN16uaKD298gMpUyfsXdeIiH30wLkeB7pZS0EyH1wJP_Zteww7w465qEnnJ0L7ceQTsMaywxbDlfJ__jPVH8E5K4DeddxHHagrDy-ttlJQCHkyvvzwoJ-YCtkC_Pvkb-doQyLjUOXWRbUrcaUtS4IENB7TGKBJ6UHRHXgRNTVcjLM-wW4OlKOdcWx-E-K0FYyRqaDn4-7kum9_O3epu81vqUYZfcZ1rn42TQeyVPPQeu4rV2XnR9-suH4J4ovXNi7O1pqTlDK1zrEqjHcs7htMYMjEwbAaes_4m1KNm_VaZWxSAsXd2wOQeC8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=G6Z16AJ7yGcTQOqNIUoPEB0Tft8MN16uaKD298gMpUyfsXdeIiH30wLkeB7pZS0EyH1wJP_Zteww7w465qEnnJ0L7ceQTsMaywxbDlfJ__jPVH8E5K4DeddxHHagrDy-ttlJQCHkyvvzwoJ-YCtkC_Pvkb-doQyLjUOXWRbUrcaUtS4IENB7TGKBJ6UHRHXgRNTVcjLM-wW4OlKOdcWx-E-K0FYyRqaDn4-7kum9_O3epu81vqUYZfcZ1rn42TQeyVPPQeu4rV2XnR9-suH4J4ovXNi7O1pqTlDK1zrEqjHcs7htMYMjEwbAaes_4m1KNm_VaZWxSAsXd2wOQeC8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5BbuvBLjuPsqblVwNR756UxXU1jJw2iJOBZKSXmucxWBBeqb4yHmHb1-cvWZgbFL79HNwQanMEyFI3lD_44H7WhuoI2UWWl8EX4gj1hgN4OJwzqJatwQkV7ODCIxy5ztTXYkH8KEagK-mqo-QcQVWlW2znN9W0HHVg4ayq6keP0h7XF2D_sgoTCulIOtFtdw362t6mLsFy8BzNzawzHYSknLHMC02tTuADRngCLyb-jvNbvgKEQq-FubpmuN0cTZ3m7d_7eYnV9OUpqSBETKnpqi6CBRVC2p6MAilH5eZjbTod9HL8VHYLfe8rE5KhRpbWMbGvBPTPCxqOwOo0huA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nauu1Pv-BeP-g7ZU6G8_nP8wITQ3gpF8LzwDsxtED2rDS_Ap3b-JxUyuYJ0fICY4OfBNLF2Jzx5X1X9tpNEjxUjkawa3ZwHUwOofSlSsjlHbyIhDBoC6V9wwMHdpuB9gH9z1UW2wiPQjPq9ExYsf4lbXpTlLc4upWNlqMGSv14-pdPZW8kO_lduFqaBf7XJLK8UWDvl33qAsf0DlELL9uEw4w-eDN9DmlRIWEla5_O229gNaJWBbkbXQ7WJUBxqKnbQwdsDvI4zii8j70ZCK03ZgNQTmwJR3g-YtloMokJT_jO0B8m52DkctX1Ixrbj5r9mIrtcpMcpX0Mkpwtl1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=q-rjthSGu_2ovnMUhpArNMDhWIrGobZq_nnEZTpKD0Cm9gVRRJ0Q88BeK1dJ4DORuRIO9kughF2WJS2RvbT0DX7DpryuIeTaAlGDrZ9oKGYAE7L2_eYpwAIH5WWQ_5IjVsuQwm-qrVHRfN0_xpcAKfr1Eq_Q80T1Zobe88EJ2MohFlYeuwv4R9Y7bscgESAjGA8AgLuCrYkZC50xTOM51_3c52YFk-umrg7BdYEr1-W31j_ju4tp6KRs2RRE3qonuen0iFst3SXm0ZCjGav5iT9821UfTcTolPbv9moe-s5wCljDuX8g0Kpqvuesu_u9lxp6fp3RF5plnEC6RN4VSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=q-rjthSGu_2ovnMUhpArNMDhWIrGobZq_nnEZTpKD0Cm9gVRRJ0Q88BeK1dJ4DORuRIO9kughF2WJS2RvbT0DX7DpryuIeTaAlGDrZ9oKGYAE7L2_eYpwAIH5WWQ_5IjVsuQwm-qrVHRfN0_xpcAKfr1Eq_Q80T1Zobe88EJ2MohFlYeuwv4R9Y7bscgESAjGA8AgLuCrYkZC50xTOM51_3c52YFk-umrg7BdYEr1-W31j_ju4tp6KRs2RRE3qonuen0iFst3SXm0ZCjGav5iT9821UfTcTolPbv9moe-s5wCljDuX8g0Kpqvuesu_u9lxp6fp3RF5plnEC6RN4VSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0rkhRPnAa5hobJnXob2boaJmtr4JpYN17rIhm9dz3u2S6_8Be3k6uFysmEP5nWGBAgCDOZ4BRH9kzelyVRJlSDqv-fn3xlPVicSidtEy-5upuRFE-wtqjxD2zsVMpnQ99FmZrm9mVPP3tFmZdBq1Klhoac6ar7_0kRb2EAKVMzIXOaq5G3vNIoRXKwssajKIPGA02msDSuFNJkpCy4oK02kXqgaQd0uV2n2UlgwH5kuJ_TEbNMtWnEwdnK8yCyKt54Oz4K6CwoeeiWH3YquEVUbM14yEh1gFmxJbQL-AkaQI1cUxlyoDOjE-2YW54dyTWINdSowsqoJgRm47J7reyJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0rkhRPnAa5hobJnXob2boaJmtr4JpYN17rIhm9dz3u2S6_8Be3k6uFysmEP5nWGBAgCDOZ4BRH9kzelyVRJlSDqv-fn3xlPVicSidtEy-5upuRFE-wtqjxD2zsVMpnQ99FmZrm9mVPP3tFmZdBq1Klhoac6ar7_0kRb2EAKVMzIXOaq5G3vNIoRXKwssajKIPGA02msDSuFNJkpCy4oK02kXqgaQd0uV2n2UlgwH5kuJ_TEbNMtWnEwdnK8yCyKt54Oz4K6CwoeeiWH3YquEVUbM14yEh1gFmxJbQL-AkaQI1cUxlyoDOjE-2YW54dyTWINdSowsqoJgRm47J7reyJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=W2pmsdhnXg6tq7LzkmBbAAmSO5xfm09EaYRqesEuYZaim1mk4CStNoFe3rHxiOnZoM7o1uJZHqIi-vUoT-7iF_zlRxiKkSfivCeWV3IUjB4MIMP18gbzXK1qYus3p_KTqu25N4QIyctSZrktiOX18I4nGRAUVaW8BAx4jRhbKkbLH7Nm2iNG6TI7NZESQZEn5bE-98Pjw2ZX_TRCAxTje2RXBktQTKr_SQJFb-HRNVEzCq0QJMiHjs2_UHEb0O4SAhO4026R8zggZn0h8rILXKUBA9_e75MUOuA1Z7h2KJdCxx8npsoIO3g66OVXBEtTu5NmoS_hTVqE2yTbAXHnoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=W2pmsdhnXg6tq7LzkmBbAAmSO5xfm09EaYRqesEuYZaim1mk4CStNoFe3rHxiOnZoM7o1uJZHqIi-vUoT-7iF_zlRxiKkSfivCeWV3IUjB4MIMP18gbzXK1qYus3p_KTqu25N4QIyctSZrktiOX18I4nGRAUVaW8BAx4jRhbKkbLH7Nm2iNG6TI7NZESQZEn5bE-98Pjw2ZX_TRCAxTje2RXBktQTKr_SQJFb-HRNVEzCq0QJMiHjs2_UHEb0O4SAhO4026R8zggZn0h8rILXKUBA9_e75MUOuA1Z7h2KJdCxx8npsoIO3g66OVXBEtTu5NmoS_hTVqE2yTbAXHnoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvYBlk8PLp1rJrLr057c5GTM139uIHxe6hf29QGLuNWe3HjEGqQYWfpoL4fdQ_ihXp776despGMHD2kAxA0h0p-mXjjRL66-edAtOU9DgxDSs6MzO7TnP2YzozGlTeJmsaJQVgPVqVcuf5XAhM2a5jukvhah_Yl9qdYIqicqWR1P04qucvLKa8aRdwWf-itD0x9dFW48H5LtzbCqAUw2VBrL9XBg81Pp-1pOw59t-iQdf411YjYFinFZmSm4Rt8rBu1jDhoxrmGIVPAFQHUwT4o7j5M9hAeE6BRd7f6mJfiO3VZ1-ZsvHola4RuI1T_aR8s0hnDgDcwwSvDntBVI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=jepcn7WUJjCe61ILhUEF_obO_2Sifp57yEsB0wgoY0MqMYwhnlwyAgvCwLhphc4zZFyWnYYplPkNWrRbxUtmNdOiw562Zgy_RSBA1tH_3yKP9JKf8KbM-ThM117JfZQWOQFtlpoYj7YF_GHauMp_7XCNJbDv0sz_ianTMUZQIV7346pQqwbgn-OWQQArOMJbbIG3DDoBpkG56fvxHpyQpKYDvhXKX4kFW09_wfXeDfUwGX9zVTqta3FhwWiIWB3jJEetWzUXkiVivTzFh1o9pwlRypyD5OytZM26_TAE8I1kI3R2keFesBITRIAxpx3QnJmORYlZxjV3xNGjIf_K1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=jepcn7WUJjCe61ILhUEF_obO_2Sifp57yEsB0wgoY0MqMYwhnlwyAgvCwLhphc4zZFyWnYYplPkNWrRbxUtmNdOiw562Zgy_RSBA1tH_3yKP9JKf8KbM-ThM117JfZQWOQFtlpoYj7YF_GHauMp_7XCNJbDv0sz_ianTMUZQIV7346pQqwbgn-OWQQArOMJbbIG3DDoBpkG56fvxHpyQpKYDvhXKX4kFW09_wfXeDfUwGX9zVTqta3FhwWiIWB3jJEetWzUXkiVivTzFh1o9pwlRypyD5OytZM26_TAE8I1kI3R2keFesBITRIAxpx3QnJmORYlZxjV3xNGjIf_K1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qnd6ALX6AwaGhZt_QBeJt9MHS7eBH8wZho2-oIfJcBJwR86q66It3dcxiV542En8z9tSYd-nLRe8y-ovKtKjm3a_tzFCmtF5oreNzRKovRQu9M43_kT6o5HdXNpIjnqN5koiRwIc7q9mK1x3o0giy_UoFpysrn9LzZlH7XHRV4u1xaV4qTy_t7zrTcYeKZJBQ8xrzhs5KIBp2sKVamaWr6U3wKyRURKwIdCL2lhULV-r5Q4VXZr6tfNbiFT1MECQ-YSVUCzOlh6pPrDGbzPAsNWW58T4GVflsiwGboxolrC2ouYEBrS-WAPBIyU16p86FJKth0kwXxoz9HdZku8ylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qnd6ALX6AwaGhZt_QBeJt9MHS7eBH8wZho2-oIfJcBJwR86q66It3dcxiV542En8z9tSYd-nLRe8y-ovKtKjm3a_tzFCmtF5oreNzRKovRQu9M43_kT6o5HdXNpIjnqN5koiRwIc7q9mK1x3o0giy_UoFpysrn9LzZlH7XHRV4u1xaV4qTy_t7zrTcYeKZJBQ8xrzhs5KIBp2sKVamaWr6U3wKyRURKwIdCL2lhULV-r5Q4VXZr6tfNbiFT1MECQ-YSVUCzOlh6pPrDGbzPAsNWW58T4GVflsiwGboxolrC2ouYEBrS-WAPBIyU16p86FJKth0kwXxoz9HdZku8ylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=uZF9aj3VN1J-x0dZwhJQlmUwT22bZktPVtXy4uU4DwdzMSFyhrpTUXBavSksB0R19v92mRySqKPhEJDkdjPt7yAh3CtDqd0E4xhT2MHIYDCCfV3peF9ubKb3FaWyystrSFf6PrZgR4_by00cnsLYRZ9qCJNzRUFV4Lj006bkP0xxvS3pEmtk-nGyyRopZweBVRyib5o_hbjpoB0fq0eXDM_J84jZx4UGQI4PddOkjmhmiWSSetx1lpZ_EgE4MymvJ8rkM4wTcwKIMIq0oX3cLabPY9yk67RZzE-QFrTg7S8jRCOTHxi_lnOgy15NsnyroJLrldZIBB8XTJfVwqj_Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=uZF9aj3VN1J-x0dZwhJQlmUwT22bZktPVtXy4uU4DwdzMSFyhrpTUXBavSksB0R19v92mRySqKPhEJDkdjPt7yAh3CtDqd0E4xhT2MHIYDCCfV3peF9ubKb3FaWyystrSFf6PrZgR4_by00cnsLYRZ9qCJNzRUFV4Lj006bkP0xxvS3pEmtk-nGyyRopZweBVRyib5o_hbjpoB0fq0eXDM_J84jZx4UGQI4PddOkjmhmiWSSetx1lpZ_EgE4MymvJ8rkM4wTcwKIMIq0oX3cLabPY9yk67RZzE-QFrTg7S8jRCOTHxi_lnOgy15NsnyroJLrldZIBB8XTJfVwqj_Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=kO1pm7BIEKdFt2NDfuf1NxKNQ6R8Lpq-jGZ3VFhT86pDjgqkfShUPyFc8XaFESpiXLqyxUrMZqekWKqOakMdTl-BwfhH7NgBI-bjvXk0EVUEqkgwyq4ak9tZ-nIL-roAJ_h7m38KBR_Cx03xz0sB8jJAG_E-1NlB3aOfdbDxdqgWcEim5neEwGsv1XdIzSofQg0pgNXhVdSuv_MbnQUC6vSCk32Qfmd4CTwUtbDelhXjicfkKXLJqVHtkSOBW3XicJE5NPnH7TB8qH3B2mPO8vOqAvLBXAl8Islk8TVh7nqGqD7QzoezTei-DzHeDnSUbVFM1OWGxsQI7rAx9T_tbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=kO1pm7BIEKdFt2NDfuf1NxKNQ6R8Lpq-jGZ3VFhT86pDjgqkfShUPyFc8XaFESpiXLqyxUrMZqekWKqOakMdTl-BwfhH7NgBI-bjvXk0EVUEqkgwyq4ak9tZ-nIL-roAJ_h7m38KBR_Cx03xz0sB8jJAG_E-1NlB3aOfdbDxdqgWcEim5neEwGsv1XdIzSofQg0pgNXhVdSuv_MbnQUC6vSCk32Qfmd4CTwUtbDelhXjicfkKXLJqVHtkSOBW3XicJE5NPnH7TB8qH3B2mPO8vOqAvLBXAl8Islk8TVh7nqGqD7QzoezTei-DzHeDnSUbVFM1OWGxsQI7rAx9T_tbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYEAZhm1EXnkOcNQod-SgKJsmzhkBVz2NSHzrbF89attb3gwelnovMMZ4HkCT5-Pmzxj7bUejOHxfm5L9i_9x0Xdn_hHq_rW8e_hYVqF2v_bhzS7cAqTAmRrdnc3yv6k2Xwm6QI_FIBelW2m8SBj_JSiXpy8u6TFDooTC_IaAlMc4UULpQ5b6_dAwbNRP5y1Y2grYLIyMJInKDaPqgBl5mrwKmPysQNII9S5vSkdY5OI44p0Ra8ghhrO5t_7gzzphuy_1GhPBlhpgGVE4wZLJ4tAtnx4X6I-lBBRW-zWFAOOYYuBRhM2NW1w4eSUio_z8FscLRiYugWxGLd6I5bjiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=azMTxPS_aOrAaEwG_JoiPD7IgkN9hZXU8QBswBaCThU-StlLPPihgEdn04FJ_HU45g5J3MVa3G2KQiMDNPKpd-f2Bbmdv7Mb57eyhNCWy1w8k2thNvAFW6s2KmZxoz1_Ff1byqdEvAgYAOZA4cdHHHyKIyOIPXM3ZeNXnM6CiJXYZQRfGdvN1syERzLiVCCIjoezOWuNNiJzA3VuNL9xKy6qjZe2I-C9cOt-VwL0YFDUj42btG9lP6cpdQBqrSVqehkh83rasgyaqYr_2FSg2Dg4Kl-eRktyUcekFOUe95DBrssF22mT5oApgEMT8n4iTE17JTh11icOBEheL5xdEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=azMTxPS_aOrAaEwG_JoiPD7IgkN9hZXU8QBswBaCThU-StlLPPihgEdn04FJ_HU45g5J3MVa3G2KQiMDNPKpd-f2Bbmdv7Mb57eyhNCWy1w8k2thNvAFW6s2KmZxoz1_Ff1byqdEvAgYAOZA4cdHHHyKIyOIPXM3ZeNXnM6CiJXYZQRfGdvN1syERzLiVCCIjoezOWuNNiJzA3VuNL9xKy6qjZe2I-C9cOt-VwL0YFDUj42btG9lP6cpdQBqrSVqehkh83rasgyaqYr_2FSg2Dg4Kl-eRktyUcekFOUe95DBrssF22mT5oApgEMT8n4iTE17JTh11icOBEheL5xdEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=E0nTxLvNZm9041Pyk4uJgbSYVJVPhW0nxXGPiMVpimISNaxIP9eFyfhYAakYtmTxHltMGXBzonBDVcs4jHYABcoR8piDZnG2aJD-_5auZYNDy8D1ukt3Lsu0P3uMEJP1kfYhD83Hhuxq5L_h43HOIgzI4yLT3jiXJa4kN3iNUsd0z8yHy4-AkngWRHI1w0VymOifhhL23D2Ww1h0yo_hw1PklpzRFVOIcHVAVQrkOoBfxjcjEQ-gBL5YXI02e2u8JHXM8iZ7VFZJSwo_q1Z29h-VKWPtYC78RjabQxljGj7gnttB2G21VJe0SYW2HDShAuPDxoRtPPkc-dkrauApcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=E0nTxLvNZm9041Pyk4uJgbSYVJVPhW0nxXGPiMVpimISNaxIP9eFyfhYAakYtmTxHltMGXBzonBDVcs4jHYABcoR8piDZnG2aJD-_5auZYNDy8D1ukt3Lsu0P3uMEJP1kfYhD83Hhuxq5L_h43HOIgzI4yLT3jiXJa4kN3iNUsd0z8yHy4-AkngWRHI1w0VymOifhhL23D2Ww1h0yo_hw1PklpzRFVOIcHVAVQrkOoBfxjcjEQ-gBL5YXI02e2u8JHXM8iZ7VFZJSwo_q1Z29h-VKWPtYC78RjabQxljGj7gnttB2G21VJe0SYW2HDShAuPDxoRtPPkc-dkrauApcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2AaMNGDmFPN_0Fb5JpeP3kJ70vbMJn-3byUjh5nBWo5OOkIc2xBYJjOwZ9chqWgdVbI2gRV_cSWouTAZRDNCBDEYr1ED9v7H7rFDnDGZCgPmZz4mZ1VSRlRiDNZMQNFUtFc038NCGa-R8tpTBl84SsXIQWPWyGjS1CgsojYCj5O0M--7TxCSRK7VOPKs8MonBdV5zpk7qmc3DnCwv77xiadFpkEuGV6hHNXkPScpVyjW1OaX4JszjfXQdoypmYRqjOQJWtQ6zTPUku9fb1kRxmtJK5DBLoJp2b1Sui0vQPJwcd4CR8MD9GaSV3alAIp2cPxWoldDLtDlnnDG3j_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=S6SLQvAgWICGw92UUnvHw67PdXqGrMQl2XnpDHaVylQoyDSNpWsBHTz-XiAuxLlEH6OfEUgjSGXPemNPG2kibMmE1mKHqzGnr_bPVqWYa3nTcXvt3gwgLNLeeAWJWRXz5Xxl_pFFqlZg3huEed1YZzaCkHgh6JtC9txM5C_YT8ER5vRBAIh_0cfUy_rVJHJ0odcdXl2NVgzPci34tHEwQDcJECCid6_m6UFhHeSe74uudcv6_LA55SyNANwbTL-wk32RoAGQCehFYCZsMYVKPRLS3KcjpzpEd4Nm6CDMZ34GAaJbraFjyc0bbUVy0p4qbXb0pTll0AZKCCeFr346UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=S6SLQvAgWICGw92UUnvHw67PdXqGrMQl2XnpDHaVylQoyDSNpWsBHTz-XiAuxLlEH6OfEUgjSGXPemNPG2kibMmE1mKHqzGnr_bPVqWYa3nTcXvt3gwgLNLeeAWJWRXz5Xxl_pFFqlZg3huEed1YZzaCkHgh6JtC9txM5C_YT8ER5vRBAIh_0cfUy_rVJHJ0odcdXl2NVgzPci34tHEwQDcJECCid6_m6UFhHeSe74uudcv6_LA55SyNANwbTL-wk32RoAGQCehFYCZsMYVKPRLS3KcjpzpEd4Nm6CDMZ34GAaJbraFjyc0bbUVy0p4qbXb0pTll0AZKCCeFr346UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=lD6KDHlfZJ_MhZG-FB9Ui7jQxus3JZQEylIivR6U0jUr_JjxE7xvR-lGs8-FMMCtPfGmNM_KCz3Iv2de8QcXKoriVpIYIr2jN8vEA0XFWiStX3oohs0PiKs6UBiYpVIG0ZbkjToh9iR4paItzLSR75dLlv26vpu1qenJIjlkMNhbNUYOWnlSgDv1n-YVB4GaP_uWcbs0W53LfidoVx8rj0g5-7e3P19prxAf8fArLnABWtN3IJf-euhRM5Whq4pHwq0IQLjpvQUOkXG-anJGhPyt8cs3mtJFrI6waHcrJDisNmoibCPCqEqsnDZWlVwBPejYoEINhJHJTA7JC0bXPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=lD6KDHlfZJ_MhZG-FB9Ui7jQxus3JZQEylIivR6U0jUr_JjxE7xvR-lGs8-FMMCtPfGmNM_KCz3Iv2de8QcXKoriVpIYIr2jN8vEA0XFWiStX3oohs0PiKs6UBiYpVIG0ZbkjToh9iR4paItzLSR75dLlv26vpu1qenJIjlkMNhbNUYOWnlSgDv1n-YVB4GaP_uWcbs0W53LfidoVx8rj0g5-7e3P19prxAf8fArLnABWtN3IJf-euhRM5Whq4pHwq0IQLjpvQUOkXG-anJGhPyt8cs3mtJFrI6waHcrJDisNmoibCPCqEqsnDZWlVwBPejYoEINhJHJTA7JC0bXPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=kne7WHd6q87Pg7tNlIICzuR8adbBUNRoZyHh3XqL6H7MkxNhhxPPX3xZe9Bzyrgqd6DxbpbbTU2TCF6oFXb5ai7tBXU7V6EuSS_6n5B9LT9rkYEANuUni9BFuJu8qiekgKeyNC87uGSqXGD0Wlk2BpmA5WBtJOOBwtBGgwx-ieWi7y6dVs5760rOXpdkI_zXkxPuRfNvH32Dyd5F1y6ER-nNF7jBrHGLVXrbqkD1lqRhflHSwX5ibt_sUi-DLMQijwpPbdJhft73ddoCC7-1V6UmTbn1xWazup9HWVfspTtrBPHMHJnvNn_sO3czMauDgIEBmKYYVC4CTiB2-k7kETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=kne7WHd6q87Pg7tNlIICzuR8adbBUNRoZyHh3XqL6H7MkxNhhxPPX3xZe9Bzyrgqd6DxbpbbTU2TCF6oFXb5ai7tBXU7V6EuSS_6n5B9LT9rkYEANuUni9BFuJu8qiekgKeyNC87uGSqXGD0Wlk2BpmA5WBtJOOBwtBGgwx-ieWi7y6dVs5760rOXpdkI_zXkxPuRfNvH32Dyd5F1y6ER-nNF7jBrHGLVXrbqkD1lqRhflHSwX5ibt_sUi-DLMQijwpPbdJhft73ddoCC7-1V6UmTbn1xWazup9HWVfspTtrBPHMHJnvNn_sO3czMauDgIEBmKYYVC4CTiB2-k7kETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhLa0n0Kmg1zegEmQrpimg8XWjOzI6XyQ-E1QThCckpYYGaZupxKGNtte91Ry3n6t3Fa7ZnpqjybbHSYpa3ZFollTipiV6G0LYp_zpjgLbEFGZgFazIaZsFuy5PuPAW31-TK7R6ez6FptW2i6wedcju5lpEhGv-0d3tKtz0wSBOVJqaN5pidUPJOEBP3HyWb_AGN4uiXavUhX9Luv7axGioZ35giEDaI8U1PomGE60CS31Q0UWbnFDYaDwtm6eigokloJHiI4OmOh37iKJz6QXh7dWKGxKYp0RBtutmRrjINjYgwPlvZCAYB5ZqY2dOMtlruYEFEBpq6TIi921aebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvTwcUlYPYMxYQfVO8zd1ElHeshl9_g8E3HftzCTQ2W3F34n8GOoOqsspz_0LRCHwLl2yXpAvWT8xXE1Rt3hNJOZdVU7LVpGuPWkz-Wk_BmW39oS_HXFjR3a_TML5Qe3p5rSsWWfWgTxM_NaQJ_3yJVx6IMrb00PKCwBsi20MleJPOiM7Puw4e0tHUjwaMWakKWhKyMRiZI2iGR3kFcKqPPGBGqIyO3mh0PQvi2HaDtkANUuqkxDi5utVExfr0fH9lw3aoAxELIbVipoBqq0nDpgAmD1LmR1s3ccbRajposK0ruz_cSCckJbbe9yJEwKyEV0fDrdt1UWGXZkqALuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-Dbg5nWgPIpuk4PWvyPriC0sggxsrGc6Gf3w59-WTaaKh9gJq5m7NKkdyfUoXiOzPAOkv2Y5-1s268jtAhYdJpWOvZBp-YwnK-Wayw5E_dgwlyGuoDBjFOgllSKKalrENMyEUDQWiXV-lRKGoe_88qCH2jCcSl6r5s5RcXxWC2y86J4G-DatTo7ODUEcO9S48GZw0HT6D-3LbivoFc_CP2OC_-7AtrPps7z1k86JEpnuq-yWej_mLyFJ2N3Y1NUAVwO56Hq_u-0FjcaQkSD4LSxismEY1Nl3RA7IXtjN8Hsc87365pein5qN9FdTLkUcP4YxKU1iX_RpBKPM-5YoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=KKa-56pxIO74Xpl_MS66tdH8VqWOXCt102rAaANnlrNcG8q-pv_dSotJ78dvtGkO8fJN2duUlJlyvlKGtaBMQPblP6m3cmTcVa0zoAV9kSaXZmYUJirD2KA2Y-znnnDNWGO_TnnGuQkT-oYcrhv5wO7scszf6r712pSONxLqdqztQZUqotKw-zOvE_dy5xxYAYjjPf7hPo9TXm5-hSnZHdK7McO3ayMG_ZtnoK0w_3DTGtIrxdjmHc3Uq0yWecVkrgv3v4vDKQE50LS4ZxDhLQEtkvyMGVh2FH7x42Bxi6Onu-5FmjzQwRm5FniECE4sDQhfNYtVlqHQOyDFlfO7Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=KKa-56pxIO74Xpl_MS66tdH8VqWOXCt102rAaANnlrNcG8q-pv_dSotJ78dvtGkO8fJN2duUlJlyvlKGtaBMQPblP6m3cmTcVa0zoAV9kSaXZmYUJirD2KA2Y-znnnDNWGO_TnnGuQkT-oYcrhv5wO7scszf6r712pSONxLqdqztQZUqotKw-zOvE_dy5xxYAYjjPf7hPo9TXm5-hSnZHdK7McO3ayMG_ZtnoK0w_3DTGtIrxdjmHc3Uq0yWecVkrgv3v4vDKQE50LS4ZxDhLQEtkvyMGVh2FH7x42Bxi6Onu-5FmjzQwRm5FniECE4sDQhfNYtVlqHQOyDFlfO7Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaTrabnyVPepd2-7fZXXv30mal3lBCt2Dq7R248c2bQBOsLzBDIdN5xbX4I7ERNgEAIpLYOKtL7XJCB654Q-WmoSMO_0eMGdIEI55OkaPsPIgEeldBFXXZpwc3jilYdQbsQTD0Zxmi-o8NkzO8Q39BXI10JdRjLvMFlDzV0lmw2M8tqGLh52q6U7T8DybYutgrEnDV4vboXY17rVuCJB5wwUFB85T9MnxDqMQAi2QKosWLPOIHem6K_B9XKzRAdFTYQuJiM1O0JB4retDnMdyFfH_7GPXvywLoG-LrsUkI1EiqAZvYW2bwsxVf73IdIYJlu9MAP543aUq69jwWzEMKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaTrabnyVPepd2-7fZXXv30mal3lBCt2Dq7R248c2bQBOsLzBDIdN5xbX4I7ERNgEAIpLYOKtL7XJCB654Q-WmoSMO_0eMGdIEI55OkaPsPIgEeldBFXXZpwc3jilYdQbsQTD0Zxmi-o8NkzO8Q39BXI10JdRjLvMFlDzV0lmw2M8tqGLh52q6U7T8DybYutgrEnDV4vboXY17rVuCJB5wwUFB85T9MnxDqMQAi2QKosWLPOIHem6K_B9XKzRAdFTYQuJiM1O0JB4retDnMdyFfH_7GPXvywLoG-LrsUkI1EiqAZvYW2bwsxVf73IdIYJlu9MAP543aUq69jwWzEMKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=GGmGRIt-cVAVvURIvCTe6CJwxGIedye0wX11cLYCTS_5yV5BRMiCZJaTXG8NpwfHXTbaH4YIlbM2KCFboDXHRSyICT7d9w7Ol5zgipZpC8B5W1dr56QJjDCBF75hfbYWzcrOzPFZglO5huyBpUtuVK-3ELKajdTK73hP2bvmXp7CAX_JcPKP8KNS1XP6d3b57hs3vObh5Ii-kGU6eFIFIZWaH9wWDJb7mxfQEyQ20pGXe9-YT1IifzvRaswuGL6AciI9RegDTuYyWgorNbgrdRQ1PAWcKrnZTDMCYLT5BpNOLJnb3j_5VwQoPZArPEnrdRSNSHVUW7lgxnICu_x2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=GGmGRIt-cVAVvURIvCTe6CJwxGIedye0wX11cLYCTS_5yV5BRMiCZJaTXG8NpwfHXTbaH4YIlbM2KCFboDXHRSyICT7d9w7Ol5zgipZpC8B5W1dr56QJjDCBF75hfbYWzcrOzPFZglO5huyBpUtuVK-3ELKajdTK73hP2bvmXp7CAX_JcPKP8KNS1XP6d3b57hs3vObh5Ii-kGU6eFIFIZWaH9wWDJb7mxfQEyQ20pGXe9-YT1IifzvRaswuGL6AciI9RegDTuYyWgorNbgrdRQ1PAWcKrnZTDMCYLT5BpNOLJnb3j_5VwQoPZArPEnrdRSNSHVUW7lgxnICu_x2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwm1ZTGwVkmZRE53F8tVadDDt0XfzpUEh7uFuOiPh9O-v2tBWeF1srZ3ujjUslMaIrB83xhckl6XfzhgRN7eCGPUt0s_oQKEGF__F68UtAQAhyzj8-egtHCsnfGLVWZpqPVs8FZq1IEixYM7FPUOLp3e0gUCLcKqK2gzQ40m2-NjJHfi75dQ76G-hiipAsvhXgvILXwwdamU6hcwr4Yn3lNE-Yx5cUO4vYyAtCt-dj0KTdezqTABdvBDzyYtak8MRHW1bFpycQ2sm16vhDxSMXmEFrRsSUU4SP_V0B5bx1SmFKpWC1Xf5RdJB3nLa1uxgnkAhb5duEhu-1_Etg2b6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTgLhkwvDyj3qOXVxigdUb3lmgxVg1UWImzKtDqLp-U0tVnuJtdjt89LjFlrlc0jMNZkHtvYfGWpffiIIIwi6Yus82HVOhQ_ABDiJ4BpVOMpIlJsIaWxnEJ6EXyZP1l32aLAcS5rTyPkrLQGMAp7r7aDKnVtXNPEdfvf8O0QvLHaAJY1UIheWojCCNMtQ2AxJkcNio-qF9udaucN0px7ZWWorh0QJjPZM6P0nnpABXi_fnua0AR0ZaF5n_PSxaQjRbxb1pStusBvbT-VMX5MW2mgNKdJk-0xOdOgHh9vRhYPhfQk4DoBbhpHR-KuczJ1Qj5jDeWdM_a-zRJHqVrXT2BY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTgLhkwvDyj3qOXVxigdUb3lmgxVg1UWImzKtDqLp-U0tVnuJtdjt89LjFlrlc0jMNZkHtvYfGWpffiIIIwi6Yus82HVOhQ_ABDiJ4BpVOMpIlJsIaWxnEJ6EXyZP1l32aLAcS5rTyPkrLQGMAp7r7aDKnVtXNPEdfvf8O0QvLHaAJY1UIheWojCCNMtQ2AxJkcNio-qF9udaucN0px7ZWWorh0QJjPZM6P0nnpABXi_fnua0AR0ZaF5n_PSxaQjRbxb1pStusBvbT-VMX5MW2mgNKdJk-0xOdOgHh9vRhYPhfQk4DoBbhpHR-KuczJ1Qj5jDeWdM_a-zRJHqVrXT2BY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym9e76DSKkzllbORi7XAuTFg0gwLANgmrx_R2Ug3fL8U2jJbalN0SrpWqY5v2VGKoA7EGDP_4bXJSes6y-5KGiqHgR9qCZjp3HBn004u18_TzYsYO7BBOoAHQfKGzEG8uIX-icpN7Tjv09ka9BHaB6Y0nrUGndfNQMClN4POd1GoqBjhaWRGQBhso6-z09uRHbv08L8CnHvXW3uI8JlT0MA4cDLvPsiHLXaX_aglrk7lWw1EodkQ-AOZV1aktAo9Dl_x-WFY6SZ-Imju4WaFeKMn77Qc68bm62gCRDfLN15ZfLf8UObletoRQXsGi_U-BuIV86_kxR1vEz4ec1XHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ApsDF85rVP0LE_KT8Ol7SlSsfGeqeA2EtvrTrnIx6blNVqFEtidsWM7WOgsuMQJTdj3qqteyXM9keo3WPZbKLgT_97y_3XMPLZ0zcqqOUvHYiTUtMqYG_3sALvKvFkRqBGGou3h0jnKgVBZrI3PGCa3JgeJ_57t3khqf6NXxPdz-04vGFNKnnu-TqDxRDHkAj5s3uf4koqxppegOqA1R69zJLxrn4kyu7FNaO4OjMB9tGw24xgmbnhXaZUi9G3Yvlfq3VWH-6Q1xVo6m0PF2aB4ZUFx6wXD3NZRqhV8Y9nR_Ic7QxccstEAsfaLknf9bkTh1w7Vd9RayWPK005R7pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ApsDF85rVP0LE_KT8Ol7SlSsfGeqeA2EtvrTrnIx6blNVqFEtidsWM7WOgsuMQJTdj3qqteyXM9keo3WPZbKLgT_97y_3XMPLZ0zcqqOUvHYiTUtMqYG_3sALvKvFkRqBGGou3h0jnKgVBZrI3PGCa3JgeJ_57t3khqf6NXxPdz-04vGFNKnnu-TqDxRDHkAj5s3uf4koqxppegOqA1R69zJLxrn4kyu7FNaO4OjMB9tGw24xgmbnhXaZUi9G3Yvlfq3VWH-6Q1xVo6m0PF2aB4ZUFx6wXD3NZRqhV8Y9nR_Ic7QxccstEAsfaLknf9bkTh1w7Vd9RayWPK005R7pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=UfP6M0PdUROF7gNMhV9XOi2kc9zP79kO8W751wh4u2bPlA_6JGAyoO57g-cP-pGbLEC2e_ZgYPq-tQCmkWPMkQ4PCIBlhGDNDI2gO2C8Y5qTd4wR-5NdXnr3QIffZW4uXprTMRgINaZNCPbGPtm7jYbQyy4NdsBvX-jNNiCtCr-p9vFbTxiix1l1f0qYnaRGpkZlA5q3ch8Vxlsy5944kBmG0LEG-Eo71Th78LzvCyHgRiKTyD-om1ACLc06SMbeZ1r9FiG8ZZTAHZo4LccCkh-HY-jqp_fWQ1jxAVv2TdXVGgXFfPROseAF_f-O5Ol32RSMdw5PVEPmwEmStf88sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=UfP6M0PdUROF7gNMhV9XOi2kc9zP79kO8W751wh4u2bPlA_6JGAyoO57g-cP-pGbLEC2e_ZgYPq-tQCmkWPMkQ4PCIBlhGDNDI2gO2C8Y5qTd4wR-5NdXnr3QIffZW4uXprTMRgINaZNCPbGPtm7jYbQyy4NdsBvX-jNNiCtCr-p9vFbTxiix1l1f0qYnaRGpkZlA5q3ch8Vxlsy5944kBmG0LEG-Eo71Th78LzvCyHgRiKTyD-om1ACLc06SMbeZ1r9FiG8ZZTAHZo4LccCkh-HY-jqp_fWQ1jxAVv2TdXVGgXFfPROseAF_f-O5Ol32RSMdw5PVEPmwEmStf88sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Tc9j4qFJ0GYO3UzMMUjNIgausEhKPuR6DdusR7Jhu8-_Nl3XfYGBF5TfjBDahYT6hToG1L-HTZXWfpEsG3TEbui2rAYEbN1R8c-Gr2ia5GYssA_Aup7EAMN7KAR1Hq5-8G1xVjj_M2ewt9OsiKS_R3ZTnGWoh9BbTcz7oro2iaOhnTtNkEeVyp_33lS-HnOmQcJCQPTOIKco8cDBWjBdH5X9EphVfO2Ng5ZZKVB61ZTmyMGGKwtGJUB6Idn_TS2Ixrjo_ZmzvYV8FkxI6MH4_a6cHJM3byMI9Ju9w2lENo4YyAnP_av2ZC1aDnSM-M8nZGvyN_VBECJHkGUA4_tbbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Tc9j4qFJ0GYO3UzMMUjNIgausEhKPuR6DdusR7Jhu8-_Nl3XfYGBF5TfjBDahYT6hToG1L-HTZXWfpEsG3TEbui2rAYEbN1R8c-Gr2ia5GYssA_Aup7EAMN7KAR1Hq5-8G1xVjj_M2ewt9OsiKS_R3ZTnGWoh9BbTcz7oro2iaOhnTtNkEeVyp_33lS-HnOmQcJCQPTOIKco8cDBWjBdH5X9EphVfO2Ng5ZZKVB61ZTmyMGGKwtGJUB6Idn_TS2Ixrjo_ZmzvYV8FkxI6MH4_a6cHJM3byMI9Ju9w2lENo4YyAnP_av2ZC1aDnSM-M8nZGvyN_VBECJHkGUA4_tbbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjaMOCmQaX9Jf6oofmYFysMjKMx8Zwa1uQ-fR4U9jS77O-J4NG5c-BmKe6uTOfyH4uQXEciUeNOLjYN4WApWbwjMSodymHHvTvxN_3D0--dk2mJhBa_SBbgL2simHL1SXH-5Qh77cD3wbtthHo-FuSgvdkSijnPmeTwsc5x9T0rDMwxR5Q9LnRP21BzAaNNtohhjWQTiP3q5zwxkWXkJWDDQf81dRCz45L13pseTqvUlMbZ9vEGVhUUJPVbxsTwHC6ITuNg6RAbRBrt5EipEmGmfOu2v1SkDUfq4jUv3-NfM9eSRxKBzjbDbEw4C_xBdcMCbEPCfhSq0C4Ik1TcYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz93XtqRknpaY4CPd4U5arCTZE7TRy7RPSwO9kYNq3_JFKnzvHgJ8nUxVIzap2BlKFF5ezwCy7uwoSLQPlDI4AkTDiiNyql2e7py9fd1q6k34FD6g5RMtzf7GZ8W9Oiau1GLgHrWZa_nHkVdO6l1J0260r-DnfQgjy4nNevw-cMexbkHlnqkrHPhkQpvvvEwZMkKZersUN3MynRWc9Uz3qcid1NubU-FNlo6LzQLXsqx9WVBK8U5_jYTkp4ic3NiaDqv6Ugzt6WePl0qywqFlyxFWVseJy08nb1wGR3tRPIkHK29Z00vnZbYtxiDIfe6uqJLs7wXOLXj2B00mozM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=mKQ3VwR7nypHmUSOcKSVm2Dr7MA6KT3MxRxiBtXTHrU9TFkS-o8hoaIR2vrlKP32Pg-vCJiHN1uz7luQf5QyTZQd5R-TZH2d-FFKmsz9TwGINUV_NcXEBmziUVdJ9jdXCGh-qKKvkqdJKW0nBRPKEstVTI7nCc_BXg8FGp8CWbduyckuSRL01Fw11tUmEnn5FcweK2YiOzXjLKcIbQ6li4zGp5xe9HO6TAoViXEqp3McYA42ZjLss1lTWdcngEgT9QF02ORLMHSilryez5TgIwdVHcSXRY39-ODYEmwtZ7cHtMLnapsfcaErDljylbhTgrRVK_jPj9lXBKBnrVpEzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=mKQ3VwR7nypHmUSOcKSVm2Dr7MA6KT3MxRxiBtXTHrU9TFkS-o8hoaIR2vrlKP32Pg-vCJiHN1uz7luQf5QyTZQd5R-TZH2d-FFKmsz9TwGINUV_NcXEBmziUVdJ9jdXCGh-qKKvkqdJKW0nBRPKEstVTI7nCc_BXg8FGp8CWbduyckuSRL01Fw11tUmEnn5FcweK2YiOzXjLKcIbQ6li4zGp5xe9HO6TAoViXEqp3McYA42ZjLss1lTWdcngEgT9QF02ORLMHSilryez5TgIwdVHcSXRY39-ODYEmwtZ7cHtMLnapsfcaErDljylbhTgrRVK_jPj9lXBKBnrVpEzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J95vMqyKQBVCp2T7VSXLtuKEcxjavFgfcUY1-AOiQd_lUw2vEoSmkPj-zGhGLbjHdiNxCe35rI_8a7KpZZFpfKYpf_0Oxt9tnv4D3fm6ETPQfaENPys5XgfNOVDRf1pbVv0WX5l0XXdKEUPmJ-_lVSqzByDvGJSqe0A5BDr9ZfSiEmaLNSXfx_nLEsYx9031-Z2YYPIZUqorr0U6jLT2hNs2h63QTMGM2sFql02J1l65N-J1MQzjz8BIbbdRYUcYU5vrEE_DYwuslPnSy2TCvA5lo4-QYlOAg7OAcI9NhpSHPDvv0tVlGjmeTMGAVNvFsJBuirPXQJNo1h-0vAKVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6d-sT8ICxiqVsBeaGk0kJ_MOCxyme48DJQ5qvuFo7dZqOMh4bOUzHblwqMfx9HnpYIpZBFSgVJ_6VblO0akG6Yi5nQ-hJeLHEzefcDt079_T1KuC1l-l_1_aPn1qZdBmnDOizDo7HsHD1gU54RZoiDu-Ou5iRDlOfp8HDIJqzgiGJ8zMJoYTtm2TC6o7_lcpeGXCK_VlmgkLe0v6VM4Trd02U4IbO1ulBdQbiv_iapZUiw6cTn1NFqWq5kHn4RHyB_HIPNuJB2ZJ6zEp_JdW6tNYYSgQeStxz73gP4AvLFajfh6dndLxHEcQzStjJDee7mDPNaVv7Cy1dOLhUl8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=bv7JR_3tgCjWAErj1ai-DyQxJUf_jyYg38gPhd2cle61LpnmePTaewcQEHIS6CPBXUhNqMb4U9XOzXq2Aj96gduZVXyVDHcvruzqP1nKf1DkA7WKuE0srGQx69Afk3wif7OH9nfoPFou417pF1Qr2zBCWrHK4Dlicd73oSN2NapqxEIvxVPwH0KMKMeqHESImPexKYZfUAJZ6fmIzQOUnUuWbuI_KTZlnWwQCoD_NZiMbbd_8aI5mBXF35EEaTy_Iv1VntZ25HAb3Orhitd4ic6Xa4J9LH6BQR0vqk1vzQBoKptnzokavklDOmsPHrnxIVbWpTia502UB0RFkNZTr1DgDILE6YXqd6c6oFLkNyusfxKm12ymMNGssBYQWFT2LipeOV3u5u4oEiBdSzyoFAtvwe1DaVDzi_olma1vS_GAsCWy1yG1sne8GClaMMpUqZz-VxEnxxtIgj0YnXuCh2vx5Pt_WPgfcK3iWYmWYd--_7QCOa43xz1hm4TSGMQ0L5X2gW9-4ftw11xumBcXs0ptxoznGYkzgkz94iwMytE8v7vtbeOh6bypakD-2mpiKcSe3KAP4yshJZywDakyi2AykIuaGQWHl5q_5W_AiF0Up63jI1TuUzQeV3wBKGWnncXBaOu9WAJea1t04j4_VGDjmsVbv9ayxp8e5l-w5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=bv7JR_3tgCjWAErj1ai-DyQxJUf_jyYg38gPhd2cle61LpnmePTaewcQEHIS6CPBXUhNqMb4U9XOzXq2Aj96gduZVXyVDHcvruzqP1nKf1DkA7WKuE0srGQx69Afk3wif7OH9nfoPFou417pF1Qr2zBCWrHK4Dlicd73oSN2NapqxEIvxVPwH0KMKMeqHESImPexKYZfUAJZ6fmIzQOUnUuWbuI_KTZlnWwQCoD_NZiMbbd_8aI5mBXF35EEaTy_Iv1VntZ25HAb3Orhitd4ic6Xa4J9LH6BQR0vqk1vzQBoKptnzokavklDOmsPHrnxIVbWpTia502UB0RFkNZTr1DgDILE6YXqd6c6oFLkNyusfxKm12ymMNGssBYQWFT2LipeOV3u5u4oEiBdSzyoFAtvwe1DaVDzi_olma1vS_GAsCWy1yG1sne8GClaMMpUqZz-VxEnxxtIgj0YnXuCh2vx5Pt_WPgfcK3iWYmWYd--_7QCOa43xz1hm4TSGMQ0L5X2gW9-4ftw11xumBcXs0ptxoznGYkzgkz94iwMytE8v7vtbeOh6bypakD-2mpiKcSe3KAP4yshJZywDakyi2AykIuaGQWHl5q_5W_AiF0Up63jI1TuUzQeV3wBKGWnncXBaOu9WAJea1t04j4_VGDjmsVbv9ayxp8e5l-w5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6603AiMhU8jJs_wFFFN20nB74IEBKk9E2F8VGlEPFkawcia6zUZ4A-BztSNvANOp8VBHDtOxxh4v0BhPqzEKm9TtUqXrfDn91plyZJlUGQcXCHRIqWhY0y0I9jd495kGwKrIew4oAkt3BQ5DZRZx_jucCXow-JAUcuTYzOAlaHJ_Iu2wVVx1uf8z4TwpxdibbZdGfBAcfnF01bS3psuTZ8y4xSr1dVjqEVDUgu1XoNcnL2JZClASMzLFWfH6VquWPcibrBf1b19ZW3rLMwrUsRhVd1h8_PfXAxiDlFPSKnJYyJPPbKqkePNYMjZC6ADzIp2_3m_Z7gPytgKDkrDLMqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6603AiMhU8jJs_wFFFN20nB74IEBKk9E2F8VGlEPFkawcia6zUZ4A-BztSNvANOp8VBHDtOxxh4v0BhPqzEKm9TtUqXrfDn91plyZJlUGQcXCHRIqWhY0y0I9jd495kGwKrIew4oAkt3BQ5DZRZx_jucCXow-JAUcuTYzOAlaHJ_Iu2wVVx1uf8z4TwpxdibbZdGfBAcfnF01bS3psuTZ8y4xSr1dVjqEVDUgu1XoNcnL2JZClASMzLFWfH6VquWPcibrBf1b19ZW3rLMwrUsRhVd1h8_PfXAxiDlFPSKnJYyJPPbKqkePNYMjZC6ADzIp2_3m_Z7gPytgKDkrDLMqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=bQTBkQUy2gX968uSZ-HFzPAF1oXa7nM7NeJbJOfXi-px5EWZqIGqYxGdsgzyz5btTEO0HZGGQkjsgCaBPtZ8b1hMrHjyYAuIgrFaqNs8ja82ltm5zGWurmwzn-ipCgMt6fgJXrOq3fXubu9Txeo_MG-fTeZOHyPYkEJTwdN_nptiug8U9TOHg7BtoGxsSVcrweSglXtx8_vV_2MD5WFEJbr-mqLY7XAiYBLDLqk9tobpWOwQ_9zZVK8Y7xJReYHGd8nAolXH9X_dtVOFfQwI9JZ0FjdTt5eoRqO1rx5N38CKTlcWzGiX9W2ctgvf1WeFgR4X6Z8HJ5abGYS-QZ-Pr4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=bQTBkQUy2gX968uSZ-HFzPAF1oXa7nM7NeJbJOfXi-px5EWZqIGqYxGdsgzyz5btTEO0HZGGQkjsgCaBPtZ8b1hMrHjyYAuIgrFaqNs8ja82ltm5zGWurmwzn-ipCgMt6fgJXrOq3fXubu9Txeo_MG-fTeZOHyPYkEJTwdN_nptiug8U9TOHg7BtoGxsSVcrweSglXtx8_vV_2MD5WFEJbr-mqLY7XAiYBLDLqk9tobpWOwQ_9zZVK8Y7xJReYHGd8nAolXH9X_dtVOFfQwI9JZ0FjdTt5eoRqO1rx5N38CKTlcWzGiX9W2ctgvf1WeFgR4X6Z8HJ5abGYS-QZ-Pr4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=JrhfS-6vDEzYaew7qezgyTtpHHYmwfcA_Uj6TxlsnstzjOP65v5FqBBANNctC1xHAaciUsDSKAGlr3lwI8Vk4ArWxY9d-KG2Jy0Hq0ngoSnhysazHPcSpOzNxLZOH0zxN4gR2noHkCNr4T494o_U5Tt_Br0wos9N3dxeWzeCBh7GyJG33VBZ4rekV9RnDGMDqwH-m3r9j1TrNV_ZPfEHYa_yM13s0-AI1pg8F2rhRfxtawAe4PzpDpCTZa68LLMtTFxvbykus8hoD96QIWw4Y8CsElsRq8NYrG0vRRzgaW_Bffg_q3lQ0PTMnfpJrUrFnV_yNX0K0XZ8N4Tp9c0taQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=JrhfS-6vDEzYaew7qezgyTtpHHYmwfcA_Uj6TxlsnstzjOP65v5FqBBANNctC1xHAaciUsDSKAGlr3lwI8Vk4ArWxY9d-KG2Jy0Hq0ngoSnhysazHPcSpOzNxLZOH0zxN4gR2noHkCNr4T494o_U5Tt_Br0wos9N3dxeWzeCBh7GyJG33VBZ4rekV9RnDGMDqwH-m3r9j1TrNV_ZPfEHYa_yM13s0-AI1pg8F2rhRfxtawAe4PzpDpCTZa68LLMtTFxvbykus8hoD96QIWw4Y8CsElsRq8NYrG0vRRzgaW_Bffg_q3lQ0PTMnfpJrUrFnV_yNX0K0XZ8N4Tp9c0taQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E696J4GM88kSIXhzwb5Cx7oZjqrdOjiyoAWprE7odHEdRwQNinhSUGJTxZ8dAFI48k-eQj4NG7lyUktig2XhIVnuyZ7-0TULZWydQhgFRfSKgQio36P10vRf5uJoDd7scx0LqAo4IbnCwltrfyBeCaMoKEcDnxtpDfPRO3IBvIx4V-IRvrr3-6QDL1B2gn0Ng2F0w1pWFrWkUQPLlc83l4dlIIIUnQuddD3dP9RYvpj53ZgZ6BzsqJO31u0JC90XT5lpfe9LE9k9wafl-nqB3kvSCgA4LOwShks857rAROh053FGwMW19KN13kHAAN_CFR8QKYMWPP48Gd4gqWnrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sscwtpsN0fdXmFmp7444Q7hT6dcgHB0FTdhXqG7HMx2OZckpy0tnej988HxhthH9ST8bQvpQ4dPBMwW3j1F0yDLJmqim91fCvRxYXOwB0jz-DUxtuXlvl8GDsD9sRQvFSI7QEy94YIVhSHDdRbJbgQk97xdqPFfR-bnMD5BTds2c_AXFNR8DBwwnewr55Wr62tBrODrqv_fX2UodRoS4vT3p_4RN4nOUiyHGF6apw07krUFil0TE1cJga7tTglxmXRQ7NAr8ijhmpvUVeD57bwZOb-Tzw7rmP6rr_7DS_6xWYMDJNYjehXv4m33Zv70-l7AvArew-6ik6GesdS0JWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1c5Lidj3AgWOWwVaNYbOAcAweYPyM4phq3lbT6JpwH3qual1rhFYRgYVOfrRRyBJizAI-cVd6bX40vpLc-_7pJAM_ov_llmAAfdfiMutJlYq65oNAnYdeBQyjXFYdQ1p7VdJsUJ4Id-HfafXo9COFMbh1cVjO0iue7wFLsaZ2qQi984LSkgLqb8Y7HBqnV_qXWMAMsLDKgyk6EhP6rmf52lH65GfDnd4KtKaXOXEFMEtT9UhluNF8BycAdqMN2M6W0x8V2mV7UFMYFAn8UCmJUzOE4o-WUBh48uZlFS2pyMsdQTKcg4MCzNt-eAAWIpp74DkZHDJNq3uq7Ms93kWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opBb7INQlSyQmOG4tSdPuHiOPT2DXJTBR0YbmEZqQXNy7BGtH8HmbuIMJTAXNi2f-MclLNv7bAy6l86b9QPBd-WRUW5eV8JXSDTzJS5fyYzH2BxJVuZet7QCRQzz4ETrlPyKC2HKKo7lkO8dJldOvXAcfR3mzHqBFMd1xyqmU5imy5LtYN0qz0vo8tumO6m-f2OV3PhouSbChlpGbiypJWCSsn7LXYjRYvGbtYgIOHx8O_hAePObLGH1iJgq5RKwDkNIWqHYuZfE6L00QJ8OJ5gsAd4u5B9hgRSv7R-0csif1_qyfOfzHbs-mE5WNfLMqP7QUD_POy8OsSzJcDSKpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkjKiboo0yjBx6n49PaJQTpp-2ODRV5d-8Z0KSYTEICR3W5Vja-3GGvZ8tc4ZJLqlJYRFH3Q0e9c-sOT4I7WsLYvr1SzmoQ2slxxTfVtabxFk3EfDeidLElMwdCjGZMkK0Wym88sI_xtgWWpB62pVsmotaZP324dmUzoup8-GvHxUqbHpVnHo5goQwK1c-m9jsrQ9tu39j4zOeOrk2UZwtruwrth2OtnaZwKfPbGZrRuCD_PDTiKflDlfPmRnODpj4w2ufCTXp22p5s8IvJF-sV4wVNTzt8FQmU_jHBxwAU1l9pf-oaZCBCqMBPoI6DfazbX9U4dc7Ns47tgzBv99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=JozaoUh9ZnKFJvR7cBhSS7GZx9VJL0ql-4HMK1q7apvWFsULHHeRY_5f38KkX9dVInARegxD4b_i3Y4UkviMZxbEwL-88d3N24Bv9oZU_hIzoMsV5NDZy0vY4WKbS8QW5EZ6Mku24nOb-CqbNRdg_IT6eIvDkWJxdv1RvE6Tga3cMxtEwdy-r46NNi3o2e0LUt7-ygaCNc3Mb0jxcz2NsIJ6Z_D2_U1OHVhH_eDvvkAQM65RKjp0RuYqUfpGgDcctAP8ZoTZhNA-KVHaX886IWz94V0TPOdCh9hexzcszxSeqKxObnVbQ7Grf4KoYT2O4sxuPgnyE-3vQ3PON17daQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=JozaoUh9ZnKFJvR7cBhSS7GZx9VJL0ql-4HMK1q7apvWFsULHHeRY_5f38KkX9dVInARegxD4b_i3Y4UkviMZxbEwL-88d3N24Bv9oZU_hIzoMsV5NDZy0vY4WKbS8QW5EZ6Mku24nOb-CqbNRdg_IT6eIvDkWJxdv1RvE6Tga3cMxtEwdy-r46NNi3o2e0LUt7-ygaCNc3Mb0jxcz2NsIJ6Z_D2_U1OHVhH_eDvvkAQM65RKjp0RuYqUfpGgDcctAP8ZoTZhNA-KVHaX886IWz94V0TPOdCh9hexzcszxSeqKxObnVbQ7Grf4KoYT2O4sxuPgnyE-3vQ3PON17daQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=c2EAFdBzQDpzoEp9DnhkmQd1T-L1MHI-Lz8DmLuwrKubODknOifSzxjy1MNPg9UcZmsQMJVbRrMyO_dro3wFTYnwEUJPjabSoctp2UIPlOHP_909Zd8R66knvUc-PNybogTEoCyMgR4DK_BbkmZlLYG3RJlMn_zRpisslOPoOEpEa4IxHpVLNqKLYlZv0RiysnpJwUF9wz4Qut06smIUuKhsLAWhQZkesaMdD1tEEGgoBpwAkv0YvoyupGuR4RtDgeIr2a6mPwJplMnjHZO5CLJsfM07BU9lQzkQXr11ovI3iM3geUUn2FKQi9jF7fBCV29FLsP_oms0i8giNZ28IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=c2EAFdBzQDpzoEp9DnhkmQd1T-L1MHI-Lz8DmLuwrKubODknOifSzxjy1MNPg9UcZmsQMJVbRrMyO_dro3wFTYnwEUJPjabSoctp2UIPlOHP_909Zd8R66knvUc-PNybogTEoCyMgR4DK_BbkmZlLYG3RJlMn_zRpisslOPoOEpEa4IxHpVLNqKLYlZv0RiysnpJwUF9wz4Qut06smIUuKhsLAWhQZkesaMdD1tEEGgoBpwAkv0YvoyupGuR4RtDgeIr2a6mPwJplMnjHZO5CLJsfM07BU9lQzkQXr11ovI3iM3geUUn2FKQi9jF7fBCV29FLsP_oms0i8giNZ28IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
