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
<img src="https://cdn4.telesco.pe/file/OAnz6I64xVSrLJNzCYWhXoj1F9ir-H7_ZSwgU8iCYp2q2kkLn6i1v1BRXqAsu2IcwNZTRkbVRxgKYKc-zhM5mENjkQ92T3p6k85FnXxdCme2JbQj7xHN3zPOqYTiapuLH5IloMvI7fhUP_Ckm6h33NkLJ54sc7GAjbuVBmAgnQKZINXPoZtkDLMjv__6xSLB2E65wNZSlzEX-Wh1qbU3yloDz3659eYc8WAGeB3lBNmdlEgdbl09SwgrKX8sxJyyJ6Z-IcllKTMr9QI8VDnUtS5AX06zjkduyuaEp9qUedqAKAns0dcHPk40BmxidjWRBLdcslWy5CvJvXQcDmYARg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 06:02:13</div>
<hr>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXdR7AcjzRjBEfZwmQItLC1crIx3hIJQtf_d9Ep1IBhn-OmMWNL7xmF5fdC44V6vc2jqlBdLFqslP6365ZUTsOfTPD2zNNg9dhlVr2_DldgqmvYysI-CJrNiY82wHvHh7MRFPQVoAzcexj0r1Qi4W4RtuDf5LosyK2HhN6VJTVTqN4WEO5-t0YZlZmdKv_XdyPYp8KDxZDOGJ710nKMxHMP9Ba27kP4atgaqjgW3BW5wJRRxzwEnOu2Qy2EeFe9DxGGErz8wtK8-OVfUEWFDt08RQiOI512acm3uJqxIDp71fg8lZFJo1i7BYX_qQHTwEBrLRCt_K4-CfAxeaW5pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFR9mP27XuuGctu-j9UIthXRXcR2HkauBcp1vLGDZucKGnJvm6eCgYqeLOvCJYxlxP_FsBBPQArNZnG5bWZDEwg8-oRrf-Vs395QhuFLe4n0xgtcckZPJNY5zaXOh57Dn2kPUElOb_GIltlAf_xxkne8VsmO5yH0tHkbhceyuXQVw48OkPF6o13-oWWgXwHuGqHV_kMRmdG_2cieuC8UaZz-wOvzGoDrem8KfCz2jRHSP2VrOUFiX6qglWYIWeM0Iu44DJe1d3irDKrX5zLqC4gT-lw5sJi9TyfIXlCj8YcxMBdPEm4W35CEv8IZAj0QYitzECSm04Z6x6YqyGioJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYSlidjSFGizuNxf7akejcFa-W0V3nxfwB2eUuasb1PzDVKm0REuO1QswdLgrZ4WyJV93uCy9_BZpeXJ-KEUYHDlX1b-9z7fZsAG2ydDh8z4RuMEgvzHWtqlhFOA9VrxDnu_5UYxLANrAAMNGawKNtqU4TjMISXHHNav543K7N4L01Y_MaezrDdVVXcZRU2YQtIddfM9WrdazZWIOSQCCqda5ucIkrYtJolCCDPEoYH7b0kMEvRE_7G6_4OxaMWA1ga4wICJlt4ERIUinY75EczzXSj5N7NNnHfwjJue1jvnSR05_ZdA28_T9idA13qdvgyflc3HR_lQKUVqdP-x2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxbQzXGl1WrvlN9I1lmnND2NVF945lmXSD8zphNG79RXXIsZ82X5Iugs0692acWqBXfB6u7Rj82YgnNyijd1KQ2hAhhc5wZANS_qyBB9d_2iTpz9tmQD0gAXQcsCP3WY8Z1xloET6OosZziCYCUgQH93Jxz4q_5YzWzrZfB5UVjMMiBjkHPDraHMngf-3mtEYLQ3MP8Ysajo2BR1KqfaA00qokDrdaLRwRyACaELmwVUpmXg0e3zBG7E5AvDzKftNByph9k6dD4NbNlKM6ABkE9XD4ccs0vXxocoD0zsWzrH2d-MReZQ66Yrf00Yv9v1UNLKuuNWZcHQVcnpV_B3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJRkbhs9IbWoRZovuIbAdCL8RXSrfv_LsUrHECXlOyAb2uyCnEEv9ImGnUkRyGmvAC06Z2YVpGx7izQ-p_b2WD9xm-bTyR5IzbJa30aWfPj3lmO4UruESejP3oMsOJpBG7NLchPSl77nDA5NmHdAG5jEjqbm4o8iZQyOB8lfip-ciniSz7YpCk9ZbLMGfjSmj_rW69BB-5xaFhnYeIyVHfGFt8KxkjcULSzASE3rL-HTEk3EI1vda8CAZRClwHoNtnY5UOogMYIUFLiFLHvjQw7AKDT1iD_I28FYmfPpNWm07UmLfMN-GmjQr4YYQyUOtDqs0B-TrusDlkbR-DeOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYpS2AGyOFJVNJHDIntWcTTBzu3PdjdY18dppzEwL1jCxfGZv6syisx77E5hiMHQEPYnJtUTSN9gZXYvTd177TsveVJqvA0LGWivRTQChf1q5mzc4OG542pY63Y5_CSOZgNYufdzZz-B3Yd_U8TlsXDG9NEsdRvjAQnl97Cgtu2iWJI-GYu-Fbcn96_Ol_EWdmmJwESqGPryWonkVcZphsPFW_ju0RB1ZI5L3FWhEzAHL0zhw5psoQPDc1xzjYkbeyqPUNtH2cw3TGnubrI2qyZJVsAmo5TIr4H1iisaf-1ECwLlTi1o6uFduvMAV5l3KqysaEt2kONB3pF3l_-EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6p8jGj_erqIzymuNNH7CqkXx7WFj5Q67dTmM0GBCBTeKO2JR06nEfkRn9O--Fj-ljU-O-lSSsZBWprk3mezHBDePIVi6ZjUF3FZURIId_wEl9OlAYkOpwlELJFhxj4DgcLBTxFZrFoOlFTdV4VSGqmuYJ0tj1Wx54wQ-ALKBxgXghOtmRcN-gvflFwaXBQRoihdZHMEZEEmZVsOiI8TqnmgyXs_L89XSsfht6uupp8xnV-1Iw5xVqdMeBTBmYb6za4XWJr5VUiSDnX9nfo4nHs82iiRl17m8SqKxXsUqbeAqTY3PETy5hS2adcg-GXXnROgf4GmPAdS_AWJqIHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZKiyY-aTp0qDEKrp6Yrrqa54CWEEkg5V7dIZrjj1SRcHW-wGLJ9xc9Nz3dP3nVQw9r3RH68-cRAaIg-ffBOPlUwaftTKPrTf0r3o5KurJrpTOCc4LOBslM5TKEz7XbKDZJv1FeI4oaTTf5JfLNDGtQ-XjMI5g7VmBjOsI37QepOpewMYYgfwIz6HdwIasc8nyqHBHrypuSS7IbalJdUWBwmI2Dd18MMGr5Vvb1q6k_SsGw5-wGuEXJT0OA131dZ1haGl7dyMrFf-eh37JwXLCOEE-ddBazRIvzf99d0X0D3ims1q_VAJDVh7SMPfrmr5xJmXe9DDHHhaivLJNYdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJyICSScG8w5gh4zHFUwgeBMPU78Ocf3sPu_Oy7a8kmg8xJq_CVlElx0QDixCzfbNFcCHHRKMJeWxK7-Ptinzu0Z2PRp4NxiOhZj_BSQT3nrRxm3BmiD2Vj8liPfNH8SrTExP_t-muWmu05ULgg2aoXohpu69PLaN7x0A6Katy8_aaiEEVtoMMksasWxOp42smVKf23pScPC9Nj_jUr8veXI3ed010P1PZcn-4oahzw_A6PVdXi3bhiKbx-vvqpWhrQer58M_uV21OI99eedtM3x_Qwz-6mVoF3hSep2OWpM31ovvP33L3NPhPcNTgvZj83-vsb62VPnGxtpWbCgiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtohJesNZbSJmgFGg6BfdC2n4_8K8nNkEX_hgtwNsihYrqRbio9pkVAiC5zX-fNZJB6hC2vrooeuXqAFd9L8M8qt3mimgp-llY3SKQ_gUNOySYYAFEIcAyIqRp5zOkurtHiCnzLrq7erwAb41Kd_v-kyLSXTalerTCZ8lTyNEYuIkYTt6Nv_LOKZu8S_PV8KD6WUspY3yTLdP0gMx48LVXAGs1R-yRX3hnlN4Ey1Pi17aGlfGpCV8DHAW1fhGVXWvL4yhm_s-q9Bo022yCFvmJQAUvNNUw7yB-5rdVxHucLu5WcSQ6HW2XUlQGr0YHsT-CU8DZ4Jqws2Mkggb_pSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNTYxJ77ojeY7zQleopB_UcHLTvcFvN1qfGY2PASFcLVRp3SWs8BdFg4uEIH4F0s0x62vRuQq-TP68L1HvP15RPtIE07aWBI0w2gVXUiZG6CZCorqqIYkviaXKLkaQPU1cjKwL6ipRgexiYl5u2RmKLIRKePqAJN1s0Lc6G9mFzqCw_TE6yMFmqshVj0oub7iVMUGYt7hvFvoYazDI8t89eCdzc1k2hTzp6qy4U257xUNnqofz5pmmmLGUw8YGc_ZkMbSwg2TTMv31ctymPn_HAniifMH-keA-WqYf6Lpm_7Sdwzvs11bnDKjP9YVvczXNVLhH1M_dx7FF9xpsbOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvVUcn0nncvG0HoZzOuLrTxwkAP-ZoM3mdCktSzHWlwyiI00K6qwEpvDhrq6E-ejROreuxedUXZYNl-3Q_7-ChSUyb9rRsdxmgtV2hr9bEnPjw1kCdYufWBKc14DerjipadA1PgSzwAf3AQBhQoq_0EOCBAkCaIQ74LEmKFaMSiW9KapYXbGx6RI5vqSML1eEgBnTr5SB5Wnc8YYqed4PU9CSev6SCLyu0ztjxOW6aX9ouXRisxhx3YLZxkcZ1QnFNiDV6DcihXbCWrkc3SIcjUModRWVoTEqMqUQ8rgt7eNFv4AzjqW9GFcoXMUGT_uEF4jaWJTbVddu7AP1x_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFRJOLf7yUOZDG6O2-P9-XbuNcHV40g_NRT1u0ocoZ1qR3iadf3re8NBpxnniuPm4phQ2q2E4-AotiwJ73YEo0xq1eB8OTnIU12vsJAertDdXHmEBa5kBD6uIjzZ52yOwmXZ6Gm7Stv93GSIPa4GXuIYgKkeHW3-ag3M5B-9njyewMRFP7ghkqG0jSDyXnHQZaT-Z-v67o-ml3bN_KP0z7TSYklkT9lsocmKMMAIk8IH5BWaZcajNDWd1syMML4wC0hDIRsiEFUQmh9MCWlnJjQLz77eUId9r6B4YEAzHNcaR6-C6hFJmKtZR4ExHF4i8SdknRts-a7My4a-3MZuhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=TG-HwvHnlVrhX6yqgcI_lvaVzXAA2MxldVOO3WSTLTPb0RJerPnlE7fRW1loAtHeqTi3Q4KI-hMOqRF-vlC5es3kAuOx45X_2RgnXcxhN4b4jImFw2-dtK4eUrCTNsLHtcZBmYWAsSd5vchn3_wn68ILLbIwnIMt1x_WyVuehmuAjwN8JJ3YK3JX58VmSP72P8OoVUiqe40yG1qDD7XOoL2HR2MYRopnv8TZEtXAiNgbZgtD84VHsZLbG_E50j9aNFuQsizme3e3LDHh7pHPCAliLUZIdXSKM9vR0mXqiyARA4Y9WrWFffSg9VPZntb9yyOtVyuBkZEGS5MRrkjZWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=TG-HwvHnlVrhX6yqgcI_lvaVzXAA2MxldVOO3WSTLTPb0RJerPnlE7fRW1loAtHeqTi3Q4KI-hMOqRF-vlC5es3kAuOx45X_2RgnXcxhN4b4jImFw2-dtK4eUrCTNsLHtcZBmYWAsSd5vchn3_wn68ILLbIwnIMt1x_WyVuehmuAjwN8JJ3YK3JX58VmSP72P8OoVUiqe40yG1qDD7XOoL2HR2MYRopnv8TZEtXAiNgbZgtD84VHsZLbG_E50j9aNFuQsizme3e3LDHh7pHPCAliLUZIdXSKM9vR0mXqiyARA4Y9WrWFffSg9VPZntb9yyOtVyuBkZEGS5MRrkjZWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=p4D0fddbrxN5ygxU-ME0-YppT_OWtQvfvyIR05SxcVOvGx7h6Jg4g7NT8DyLeHEM_D9ekSqBDq_18jMa4uiRcMf51Mm0MkpfFNqSya2T15J5CnawGC3Fd3x5RSz00OBX-S2ts0rS-inV9ZVKbYgBsjADRK7JcI1jGwN6KbQbARZ31skvhyRclr8FK11Q8VZ1soYXRCJPcqmdEnYSLD9zg7Gbh3bVh3XJ6EPMAi1xoilXAIgmd6QPxqzLQ5J8jU0WYAy4Tznwlu4rME50tHyRca7XG8a8uEJGnu77y7g9S3lHBDq7qHy5Ab7eBnIpQBCNVxE3JgLm9m-Lv2T0RGEnkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=p4D0fddbrxN5ygxU-ME0-YppT_OWtQvfvyIR05SxcVOvGx7h6Jg4g7NT8DyLeHEM_D9ekSqBDq_18jMa4uiRcMf51Mm0MkpfFNqSya2T15J5CnawGC3Fd3x5RSz00OBX-S2ts0rS-inV9ZVKbYgBsjADRK7JcI1jGwN6KbQbARZ31skvhyRclr8FK11Q8VZ1soYXRCJPcqmdEnYSLD9zg7Gbh3bVh3XJ6EPMAi1xoilXAIgmd6QPxqzLQ5J8jU0WYAy4Tznwlu4rME50tHyRca7XG8a8uEJGnu77y7g9S3lHBDq7qHy5Ab7eBnIpQBCNVxE3JgLm9m-Lv2T0RGEnkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=dwxprBU3C2Iib9lj9TGidlLI62c3QwLZxO7JUNHDTbcUPX7uA8IVRU1EaSAd1HzEW8-_X6WQhhn3PPuNGOvvl32Csrof25bn0w8FjO-EJy7uxUfuJzuuIBYpZiFRykr4NvQnmCzfd8GMQd9Tvk7EEYD81C99S9sn5VroE1B6uvGwo7nNc52tuZQ5Zo3wcNZEA3knIdGwmHdLRiFWJOiRcJcXg_EJlxOs605LRv4k6fItde5gagu201KtbtFgWF5cmvlgpbnGcDk5pFKZWFd7Cn3lLA6fMAoPdAuKCmyjDDFH0zIi6fVDXkGPFsMRmuBPbyHCdXPnQhpDEsIIJc2V1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=dwxprBU3C2Iib9lj9TGidlLI62c3QwLZxO7JUNHDTbcUPX7uA8IVRU1EaSAd1HzEW8-_X6WQhhn3PPuNGOvvl32Csrof25bn0w8FjO-EJy7uxUfuJzuuIBYpZiFRykr4NvQnmCzfd8GMQd9Tvk7EEYD81C99S9sn5VroE1B6uvGwo7nNc52tuZQ5Zo3wcNZEA3knIdGwmHdLRiFWJOiRcJcXg_EJlxOs605LRv4k6fItde5gagu201KtbtFgWF5cmvlgpbnGcDk5pFKZWFd7Cn3lLA6fMAoPdAuKCmyjDDFH0zIi6fVDXkGPFsMRmuBPbyHCdXPnQhpDEsIIJc2V1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=qwZR_uaeLMPaPyGvAubuTLKaGdE_DQTRhTPNU-yUz-1Y7t8k6XXO8P0hOq1-xiSuBUkeN13pLBmiT2mNaj4Mk5uck5C4KIz8Zbp50DfH5prA0opKP0v9Z-dbcGHmLSgkntBYylauJymglNHjqElx-jwXo_G5jB8dyBKI07DxXCr5c6vHS9fbjda7eohzeE_lipkpIRuXw1tdsYs94sUEHUmZ1IcvCYC5xZq95B08UUWK1syFSwd73bLmNNSXPQwT7PXIQaEbVyrpdybKgJzWR7fL5lEDFdpvrIdM2ZeyZv6xCrBY0orYd_xpGnEUW25UzCQI884ouXkB1UrTVC-giQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=qwZR_uaeLMPaPyGvAubuTLKaGdE_DQTRhTPNU-yUz-1Y7t8k6XXO8P0hOq1-xiSuBUkeN13pLBmiT2mNaj4Mk5uck5C4KIz8Zbp50DfH5prA0opKP0v9Z-dbcGHmLSgkntBYylauJymglNHjqElx-jwXo_G5jB8dyBKI07DxXCr5c6vHS9fbjda7eohzeE_lipkpIRuXw1tdsYs94sUEHUmZ1IcvCYC5xZq95B08UUWK1syFSwd73bLmNNSXPQwT7PXIQaEbVyrpdybKgJzWR7fL5lEDFdpvrIdM2ZeyZv6xCrBY0orYd_xpGnEUW25UzCQI884ouXkB1UrTVC-giQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWiHG2sIfDXqTFwB2d1PBD5YYSkdGwzATTUXHb2ULXXQwNsRmK20D_OhXGNU-8OTN8u4mXxR2WUn31gRYzGlxIvUwUI0wScDa6_oaVYEKMsHQzw0RqdSI0jK7roxHOJ5UYQH_BSSqwKDAv_9_3DyjUB4nYfzXWuDLX0D3v2d9zytEdNYr8xsWXAixTn3TtSGOhdbFHZpyZ421BbOMjgZXGsIp1sDSpdamj_zgUk1LJtp5jQWcDfoMIXPUohLTaQuexBjbS7MkzjZga9flZwPAjKUvWbqFfX0w_IQeU7RtbHtovmo2vyTGlEL4S2dlK5fxjsO-j6HdPkDqK0JWOAhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=MtV4581ASE3hcl01axfyyQCb7fqzXYFv07LRQHAcJqfNoeZsw_b8PmUr0mccn2gBjsTbc86IW1urVF5wQ8jDQBrmJ7YfgAlnSrQ_iTV3dOBY3Kp_L0jEXQVb5cSR2zyva-rRdpfvZ1fzEO02zqUA6gJxWIkwd-US9WoOGrrEoT2eiiPWz5JYsj-y7pHrBIESa8AGQaL2Te-czJ7sDc8hldOO6h4nZIstIovVKdBToaWWtGC2B0vhrP4tEdzx9uGoNvoD39SyEvKp-37NYoC91rq5NLzff3xtn-MyuOEkO3i94Vv8m_Rd85YUyFZ7UrWF87-9l8HmETtcDPfeb484Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=MtV4581ASE3hcl01axfyyQCb7fqzXYFv07LRQHAcJqfNoeZsw_b8PmUr0mccn2gBjsTbc86IW1urVF5wQ8jDQBrmJ7YfgAlnSrQ_iTV3dOBY3Kp_L0jEXQVb5cSR2zyva-rRdpfvZ1fzEO02zqUA6gJxWIkwd-US9WoOGrrEoT2eiiPWz5JYsj-y7pHrBIESa8AGQaL2Te-czJ7sDc8hldOO6h4nZIstIovVKdBToaWWtGC2B0vhrP4tEdzx9uGoNvoD39SyEvKp-37NYoC91rq5NLzff3xtn-MyuOEkO3i94Vv8m_Rd85YUyFZ7UrWF87-9l8HmETtcDPfeb484Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=AGe9fTVj3v1rF0uEnep_E0mp9n7T0Qmd3MoKm0Z2JgY7W0BTjNEinQP3RI00xhTm3TtIzPg6UMxvXx9yrfMNy7b0AXYqa5euJAH-D3AtCiPDcIKtf_d_G2SfYBFZ19pFjF1vwvOsuVycueKQisFFhAKuAYruziPKrBY0UBDins9UHTiI_fjucIiVSTn-T9ZVk9GYS8DKI502_AQbpEJSqVel3l9_m7wH_PSVg5Ab-kAJEIUHHGuddbaAhbnoyUl-fyhbfrf8lj8UZ-23xznJrmigjrBgO5-8SW2T-OWOI_4TaIli3bQN1mUHjpqVzwBlyKzjj0xwmzE3QA-eAH_EvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=AGe9fTVj3v1rF0uEnep_E0mp9n7T0Qmd3MoKm0Z2JgY7W0BTjNEinQP3RI00xhTm3TtIzPg6UMxvXx9yrfMNy7b0AXYqa5euJAH-D3AtCiPDcIKtf_d_G2SfYBFZ19pFjF1vwvOsuVycueKQisFFhAKuAYruziPKrBY0UBDins9UHTiI_fjucIiVSTn-T9ZVk9GYS8DKI502_AQbpEJSqVel3l9_m7wH_PSVg5Ab-kAJEIUHHGuddbaAhbnoyUl-fyhbfrf8lj8UZ-23xznJrmigjrBgO5-8SW2T-OWOI_4TaIli3bQN1mUHjpqVzwBlyKzjj0xwmzE3QA-eAH_EvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=m3saLWQsrPcZa3QKsHApCBguxjCft0oYJmkkrWAX8dy3dD9Uc0AOeQeOryqtfOZxVmmfF-9ir7vxGU2Z3xHiWhW25unbLkeNYXgpgHkfJ0J8jiOx3DA2MCrjLGsOAw_Q0DaD6gxd37104eIJFwSmo5yqSq8cexqNw-M7k6wJfNOroMDkSA0Hvyn3caOEcse58_TZjuVwJAOBs-T48pqjr801WwGSskiuCTn_KMpTeyVkI6-HnXaHjvJaf82NGT2_Nesx-fdHJSJAix1_WH7uXH0mpQisUFifUJVcRDfkxmT6x5I5Zq74R8eSTI5GbbVpsCdOgYnp5tWb9Uy_KsdyFVcotiA8Fi-7JaWpWlq2jx_TrUYqBBQqa1WW4P2YoK2qQRZmgpBO1QnBWeDNPcl7b7R5eQreclV4184uSPcRvieE292lZxl6jCS0G_fN4zcTJ_FVc7W7mBDBpf-Z0-ISA02ZRDmobHKZI1ZOxOrGuV6N0qjYVmaeIX9ekjbCJZZ7EhgAz9zwqu3MTDdzuruxSXo0XYk2Czi1JhNLz8-OiE6jaHUgjGk1VzgZzSTYlhE-1nmH9-638FiOp9AzNKqfYpjvPksZQWTdJcSa-f07CIdGEWgXpDkJzTSb2ZPrh3OGqOCEdFWOKumROb6ue_8lqOJWcXqMlo7dEXrkQwNHOi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=m3saLWQsrPcZa3QKsHApCBguxjCft0oYJmkkrWAX8dy3dD9Uc0AOeQeOryqtfOZxVmmfF-9ir7vxGU2Z3xHiWhW25unbLkeNYXgpgHkfJ0J8jiOx3DA2MCrjLGsOAw_Q0DaD6gxd37104eIJFwSmo5yqSq8cexqNw-M7k6wJfNOroMDkSA0Hvyn3caOEcse58_TZjuVwJAOBs-T48pqjr801WwGSskiuCTn_KMpTeyVkI6-HnXaHjvJaf82NGT2_Nesx-fdHJSJAix1_WH7uXH0mpQisUFifUJVcRDfkxmT6x5I5Zq74R8eSTI5GbbVpsCdOgYnp5tWb9Uy_KsdyFVcotiA8Fi-7JaWpWlq2jx_TrUYqBBQqa1WW4P2YoK2qQRZmgpBO1QnBWeDNPcl7b7R5eQreclV4184uSPcRvieE292lZxl6jCS0G_fN4zcTJ_FVc7W7mBDBpf-Z0-ISA02ZRDmobHKZI1ZOxOrGuV6N0qjYVmaeIX9ekjbCJZZ7EhgAz9zwqu3MTDdzuruxSXo0XYk2Czi1JhNLz8-OiE6jaHUgjGk1VzgZzSTYlhE-1nmH9-638FiOp9AzNKqfYpjvPksZQWTdJcSa-f07CIdGEWgXpDkJzTSb2ZPrh3OGqOCEdFWOKumROb6ue_8lqOJWcXqMlo7dEXrkQwNHOi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=SETjKueOe74ESn9G9dSspNrljPFqvSO8GsiMfXBHfYbnoacR-ZxkfMOek7_Zr9wlQhdbdORMDTUaPOqLSZtioJoWFhrV0cONdhFnY8_EgkBssv39ViuIwdryqfaXU-RTpjz7lzspX2gSy-bJ79BlZWLPL-wlCv6Yr9wKS1PKjbkIZBBWdG9vXCAmidFNQL92Rs8JgmjN7Ts8_pHwRWEVOvCecwgkjekiUIoAG5NOnnBGh80YEeJIRmu7IDNqhSJ4XaR8lTPSlm6YDBb-TSHG8UTeQordo5xBxoPyuN0Iog2sK8DffrgHhZymL7fL-N55xSLg8Ex1bzu4K_zRuct2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=SETjKueOe74ESn9G9dSspNrljPFqvSO8GsiMfXBHfYbnoacR-ZxkfMOek7_Zr9wlQhdbdORMDTUaPOqLSZtioJoWFhrV0cONdhFnY8_EgkBssv39ViuIwdryqfaXU-RTpjz7lzspX2gSy-bJ79BlZWLPL-wlCv6Yr9wKS1PKjbkIZBBWdG9vXCAmidFNQL92Rs8JgmjN7Ts8_pHwRWEVOvCecwgkjekiUIoAG5NOnnBGh80YEeJIRmu7IDNqhSJ4XaR8lTPSlm6YDBb-TSHG8UTeQordo5xBxoPyuN0Iog2sK8DffrgHhZymL7fL-N55xSLg8Ex1bzu4K_zRuct2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=CtCfVmYcj28mNAXB7t1ysBAU2DJJqSSBXmZR56BoYphQtO33NXxKRGGUvsYe6uybavdr8F9C_-hCxTCWkDcpgmzBwRBwS74DXbCUvXG6SgPxNh0xifAEQPnDZLvqgoCE-ucqv0cZ1pmc7ifC33r6rLuBha0Cxs3XU-_68Uwe75D8BgqGv_w0PSiHWObS52bLhZQc2vjUWRvv9IfEA7LCn2iI1fJrLio45ek9-aY37hUfA-tucC1OaNWGdFai6exigmDjCPSpH3lTZ_ne8VBJb8oBh4tWpT28bBzR39edLJSTX6j2QJ9MWWqPDEY1MfGgaE9UCor8yya6shn88oFlSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=CtCfVmYcj28mNAXB7t1ysBAU2DJJqSSBXmZR56BoYphQtO33NXxKRGGUvsYe6uybavdr8F9C_-hCxTCWkDcpgmzBwRBwS74DXbCUvXG6SgPxNh0xifAEQPnDZLvqgoCE-ucqv0cZ1pmc7ifC33r6rLuBha0Cxs3XU-_68Uwe75D8BgqGv_w0PSiHWObS52bLhZQc2vjUWRvv9IfEA7LCn2iI1fJrLio45ek9-aY37hUfA-tucC1OaNWGdFai6exigmDjCPSpH3lTZ_ne8VBJb8oBh4tWpT28bBzR39edLJSTX6j2QJ9MWWqPDEY1MfGgaE9UCor8yya6shn88oFlSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBzVHQAHtRBNZOXvZIXi_1Uxfin3Ba3p-qfooftM5jo1iEYadRGKG5khPwDFH0D61d7WdVvY04MgL7PqStDSh7ShzvZqvFW4W1UgX-sjbtNlH_e8UJNClHlzl78pdDWc0zTzJ_OYXtTseJ4ZvPfxYeSu30VjSwRfa8GQOpme94d3nLoAMOCog_SWrzZ8lAG41HIh7rtCdAtugYv2RVZ3h5jkVXX4NesgPHRsSTcKz0S228LwN2VusMqdu2O5dw9IIomUZH1ZTOiNPeW21JfLlgHFZXOKPHFho5Gxf5w-eZhVfqJksavqkWobbvBBAAy6lUF-q9f8D5u4hcNbBDb-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YygFCiiMJtE8AK8nB0lmdRpg1kyxU-0-WIwo0amxUsHs-ou1-9-XCSnd5S352qcg0zMwH52rcWOGyFZUq1L_jMiBG_D74CrOFWFHaFiSJQOEMDGoPnFCKw5YIeuVMv5eqFkur5cgtYhYoNAPKJnH_srEIeW8d4IiutF3GzEtpTwnyg9fukIXQNdML0erl1DXP6JHC7IRvlSraNRgqqco6-hgLxg9FZCdqpagjdxwBXgZQg63_JPMmKTx2Lko93GkdRGVMtxZBpU85_gkAcvrnrQAHBQIe42y3wAAqDSebBLj3ZsdBdUG8R1mWFa7f-NLU_MJpd2ic3BFGgfdn2kZkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=RLzM5o_jUi3PyYmNZ9pndjN39dh5asAgYO9acxHBP9PXS7HKHdAE_YZFKzuwLd6-HhkA-wRnBeY287zjQ26QFIVsZnid6VGYW90zpUq9p6qRELbQTK64PMkeNXqEuZNXwxHAOW3jztcrBqK6VUIXV_lDkUfjp6aW61W6tK-4Q9e4bdsL3lpIokwuIRSp7Xnn8Mf29zRqVZOLCCTSjyK3rMLzc3MgKIiUhU0XWnoNxuv0KNa7dbVuPCc1YPqKF4pO4RiFFazClCxBZ4zoXNOMJfCxZQcAcTz_6V5APMLIftUe7qi34SHR1XxCe_j5rJ8mkFUjQBUPP4X0Nsimyy79nIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=RLzM5o_jUi3PyYmNZ9pndjN39dh5asAgYO9acxHBP9PXS7HKHdAE_YZFKzuwLd6-HhkA-wRnBeY287zjQ26QFIVsZnid6VGYW90zpUq9p6qRELbQTK64PMkeNXqEuZNXwxHAOW3jztcrBqK6VUIXV_lDkUfjp6aW61W6tK-4Q9e4bdsL3lpIokwuIRSp7Xnn8Mf29zRqVZOLCCTSjyK3rMLzc3MgKIiUhU0XWnoNxuv0KNa7dbVuPCc1YPqKF4pO4RiFFazClCxBZ4zoXNOMJfCxZQcAcTz_6V5APMLIftUe7qi34SHR1XxCe_j5rJ8mkFUjQBUPP4X0Nsimyy79nIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxYAJb5oioPcXxeAl-W8wbCZYRZyjo0m5vghyhKJMt9MmGTV4PEf5D7YWXLcr6lDctSPC58EoBPVDNI82tdten2-TAkfAuxN0dHZT_8ZLD4R4XN8Fg37bjS7afTEWR-nL1H9IvsOnHW3QMt_vN_5lZ1yfc8t3tFpMJcqTyi9T7ZEs9fSjR7Jc6Kl09h8dUbb6SQziwocaj2aGDPxfwWjdfa8giVJaR7eMh_-_WI7Vn_N0Fm6f5PU2Y50aAmCIq-NGZFn6w8WFGdzMFmFIA1JkWi-M6XkcxR2enlgfSLkmkkqLDyHanA-0sP5ZlQainkU9xQF0SdixmTeMNcuP7vItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWFasbeI8L6rLbCXxYF2RicLZZIy6g9-ODkPLs1ZAJ9XcQnLy3blDEmQgBlo5jAd9Wy17-5euIHmiBRHE8CRZxyTmZOEkPKJkBDEOClpELy7qTW6KoRk3xQ1TRcBsmrUYuWHU5g-jMkhIn753jF8s3I5DrBpUY1YjxHph4wUEZd9BmhCiZXtVbdyXnj0WEo7a2ypXYzrsRwbQuqX93lVSLlsm0fnfz7V1hlq7TtNDMqNdgIhxa1NR6uggvkqfp5ZwUitYjK-LN3aY9DQ36pJHjXaulxZ-UNQvv3XOJlGb2-X4KaRnBVouAwbZguVpfgRKxJtO45DDWi680l_mseD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtkNNEixXfT_iWYnp7h_H540-mInUo4Whe9Z0D31To7fyZZXCj5QNsj2aTNbq2jAs78X1KXMTiVmPdtK8MOHTRKy5O8RVCoqm58MwoDtdvJkRSv_5uvmj3tFmeMS0Yo0dUI45hNEWZtDnSx6Kfh6oTT3ZYUUn8i9nhMo6oFzToni1uGyOrtQE6GlN_YrRcqIag1eFlNNIGKgcsSqdWLWWuhB30ADdTucQ85rLKhDhJUMfmF4pSmuqrMCMmM392lZDI7vCjfAijd8WMPvDtwRqHRKtsG9bmzROcCvZTotTU9--1HOlMV6F4H53xLDD0vHvH6JpGUxeOMGiun9QVvavA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8ixnTLlxNeccg9ny7fz-5g-Cgf-Fwa_eCIe-wa8kDiUaE2swqfMb1ny_w_GMtffzupPP1KWnCUyVfNr0gt_yvhsZWeXz4WN1KW00s_-_wysMCMbiRHXAP2QYPgRsnJsv4RQLjWp8_EZAMK1Or27-kfV49U2AahcIlnEFrMY8V2ViXC29fitt4PlY1aZ4nLGUWD0UUwcJ8Z28ZEtNnacx71NSL8HfY9HMKMqczee6i2RL47MDQZL_4C-RBiEnWcrdS6y7b_5DAv0PX8xgnAtMQn7heclXhoJgSHHQ4JVMP3fUqN97aXyhnbCJ1MleMHgeiBvWKaxId5DcT2shNt0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=YGf-M767VJsyyIOcYWQp4BTL531cpR-uDYh4DWhQJcJjlfIm6-N_WGylEoKbdvyDfQbtilRpAEUJoLyZrntzA_VtF_aliRh2G1S9jg-RbNHj9kr_FZiIi7O2srLlHEkzda3GWt0zDErvPoNNRmQIeNaA5GhPJST-v7QQFMI6HCJ8dukHqjCKxdcOzGpEWnQCDZ0uZuV8E6gT403oGrDCay4gzIcjEqM_d-lhwTyB9IYA9dpshSUC66zjWf0t34WNndUIMKsrdt3TBbPavCBWUnLZFHi-CL11eZg6ymWhFInvPDt13-sv2yyHAl-zC9jN-sAeSr9w_sWoFQ2tQVFzeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=YGf-M767VJsyyIOcYWQp4BTL531cpR-uDYh4DWhQJcJjlfIm6-N_WGylEoKbdvyDfQbtilRpAEUJoLyZrntzA_VtF_aliRh2G1S9jg-RbNHj9kr_FZiIi7O2srLlHEkzda3GWt0zDErvPoNNRmQIeNaA5GhPJST-v7QQFMI6HCJ8dukHqjCKxdcOzGpEWnQCDZ0uZuV8E6gT403oGrDCay4gzIcjEqM_d-lhwTyB9IYA9dpshSUC66zjWf0t34WNndUIMKsrdt3TBbPavCBWUnLZFHi-CL11eZg6ymWhFInvPDt13-sv2yyHAl-zC9jN-sAeSr9w_sWoFQ2tQVFzeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QuHtIQu8e62kKfDGLYSseHaUVMFD3WGFjjkusNv27_51DxgarFrCf_AmjP99w-8TWw-fTGXwPyAva9p19DQra6e37mRbYiy5fw8Hb3L10Pa5qiM4E1lEanvdOa7wyhtJHWHi4vkToE2AuuwsKwLyUTkBH4ephmvFsXi28UQ1g9Y7V2WPzU_Xod1avcRHlBsf3zAhGMX7zibdPJByIDs9CzwLKF3fAoi9hL1QOxBTjinXkIV1B7_1LYZjtzvQ5rF7enYQ1vCEV-BiOiGrQMq3aKjV2BzmnMS-l9T16bBkSRewOLcN93RhQsPf3NTgnSoh1iYhYCU5e01YDxkwfnRfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QuHtIQu8e62kKfDGLYSseHaUVMFD3WGFjjkusNv27_51DxgarFrCf_AmjP99w-8TWw-fTGXwPyAva9p19DQra6e37mRbYiy5fw8Hb3L10Pa5qiM4E1lEanvdOa7wyhtJHWHi4vkToE2AuuwsKwLyUTkBH4ephmvFsXi28UQ1g9Y7V2WPzU_Xod1avcRHlBsf3zAhGMX7zibdPJByIDs9CzwLKF3fAoi9hL1QOxBTjinXkIV1B7_1LYZjtzvQ5rF7enYQ1vCEV-BiOiGrQMq3aKjV2BzmnMS-l9T16bBkSRewOLcN93RhQsPf3NTgnSoh1iYhYCU5e01YDxkwfnRfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvBSOZfi0n_COkz0s0AMWD9FGfWmCqUZlbplmuw_jxa4849VE4hZ77YcjteIaGo6Ox3lmJHbAraL8It4AOsK9T2E_9PO6RUSsdEMCsF0PaKKRH6HcQZi6HSEACZubSj38JV8Tz7yQl421ctWK9Z2kKC-Sc1tsS4MJM76cFFOl45r6043R0LTISK2ZrYMvGVQwolchnakjLaklY6wmhxnRk_mEB8a86elmG1rdM2Yncfudl7-Ur0RpDG2LWR9a0g_NuzsoBvN2dGyEh4Us0vtzMsDb793iW5dzWj-CGyYpTN9GUFoBMYn9zh1T2GwL4gmjDxkLPsNZfW7i9jbfu-MBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=CRI2Uor7A7pakrU6CvPbpsg9dpoUw9uS2KvfSQobpyaPPANCLLUI_DDr5i0z2QEntjdxfP5fUs56XRk-ryMW9exGP8iae0Ch7L31EmGLgpoqNCsgUMJoS5OMYBc21HkYR3MXn337Dzs4rvSoJVJ8AIhzH1La0Co13VonhZbDXeO41DqBqzX0KqgFD3WZNKjfDHrvozvhSrhdjryY46gZbKvKOWTKR17rXCn8qm9JMZ7hkhjS3dcobSSyPcP2OH90Q2fXTWVciUceOwo1uP3NeAPlRj6oqmXVe2ZamOs7jRxu7HlxTfqIZZwdpiXI1RIrdaSbsXYBKq6P8u_2RVudkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=CRI2Uor7A7pakrU6CvPbpsg9dpoUw9uS2KvfSQobpyaPPANCLLUI_DDr5i0z2QEntjdxfP5fUs56XRk-ryMW9exGP8iae0Ch7L31EmGLgpoqNCsgUMJoS5OMYBc21HkYR3MXn337Dzs4rvSoJVJ8AIhzH1La0Co13VonhZbDXeO41DqBqzX0KqgFD3WZNKjfDHrvozvhSrhdjryY46gZbKvKOWTKR17rXCn8qm9JMZ7hkhjS3dcobSSyPcP2OH90Q2fXTWVciUceOwo1uP3NeAPlRj6oqmXVe2ZamOs7jRxu7HlxTfqIZZwdpiXI1RIrdaSbsXYBKq6P8u_2RVudkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=JZWdMQt1Wlq85fEtLRs-A390r3mn6iyI87VYv3-LKoK1rXfxD59nMtTdl5MDsOh99oW6JeNkRJNo9FzLYJu3_bKJHyRr8T_MK8AD77S7UpI0Y10Jne8tKDLc217DkbbKctxWAC7xY_D6OGJd_4nYUER1JxCcjGLUIRZgFv1jZmqTHUXdvgI3EkwrJ4XoTw6RCjnJLMT3xXgLlU0-KouPc3QebB4exq5AXjESUFh5-c77NEiNZDJDoLZsH2UYfnXXX9K2_1PaiZM59RDVjNq-QVwECgOP8QlxihGIRFF5Ge_2y10UBUslR6F0wUOjuCfCHvbtjGoVkekihiyBwxB-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=JZWdMQt1Wlq85fEtLRs-A390r3mn6iyI87VYv3-LKoK1rXfxD59nMtTdl5MDsOh99oW6JeNkRJNo9FzLYJu3_bKJHyRr8T_MK8AD77S7UpI0Y10Jne8tKDLc217DkbbKctxWAC7xY_D6OGJd_4nYUER1JxCcjGLUIRZgFv1jZmqTHUXdvgI3EkwrJ4XoTw6RCjnJLMT3xXgLlU0-KouPc3QebB4exq5AXjESUFh5-c77NEiNZDJDoLZsH2UYfnXXX9K2_1PaiZM59RDVjNq-QVwECgOP8QlxihGIRFF5Ge_2y10UBUslR6F0wUOjuCfCHvbtjGoVkekihiyBwxB-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=GqJCzB2SPalrHGSXb4qL1V4a21ne3BZC35eREZtd6nIBxpaTBDSHBZKu21gHX5Nyd3DbLf-Z24hClNq2L6MyoQCcY4bz6paO3Ov3tETeB_ZiL3HDphhaPcTUidyfqTF3WwHLydaWRQYQsO31Pxf28esq2kGSl4tQsPcisKi2ULxU3EbJTSFwb7rXJfKZ4Gw_9-ooy5jmhQ6-gc97hetDgBwmY6mjehkEyv_kx19Iq6cjBPr6NnQJK3k0xcClSN0lUAV5XCiGK154VvLshem3oDKCvtrxPUWJodnbQpCwvV_vbSvAWIdmhRCrOyrLkuIB468d2_f9c_ijx-A9LDAZQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=GqJCzB2SPalrHGSXb4qL1V4a21ne3BZC35eREZtd6nIBxpaTBDSHBZKu21gHX5Nyd3DbLf-Z24hClNq2L6MyoQCcY4bz6paO3Ov3tETeB_ZiL3HDphhaPcTUidyfqTF3WwHLydaWRQYQsO31Pxf28esq2kGSl4tQsPcisKi2ULxU3EbJTSFwb7rXJfKZ4Gw_9-ooy5jmhQ6-gc97hetDgBwmY6mjehkEyv_kx19Iq6cjBPr6NnQJK3k0xcClSN0lUAV5XCiGK154VvLshem3oDKCvtrxPUWJodnbQpCwvV_vbSvAWIdmhRCrOyrLkuIB468d2_f9c_ijx-A9LDAZQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXpDzqBBQfovYvX1_tgVSNdCodQQettIHe6uQyOm8MD2b005OkfP9qmV_uX4_pv9deQAAlndfApy6-zXdCyLrC9J1Qwvfk2ncz4Plba1y-HCTCEtxKlBWp4evNMBzzirvpl7ed6c9UM9G-FVnhBXAtXAsrNj4n_HRb-Po_ZAVC5OP-HDJfejmYvlFXCgK3XbuaNehywrGPzXf2tvIrn4mnJAJmUmrUcpthBMBxV43PSP4PqFX5sourDesekZW8-6-3JJCjiqlS02xGXo9BkBCLSvTNRZ8yr7tVis34JLAeifSl1mGpgBeyoeuuwCzhO8toTDGPYjHB4UdzCIulfTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=qdFSUqZ8hRzdNgUUP9I9MiChlae7dCFSWUZr6B-fLzuuGhihjhkfrRT-cgH3AbVJrN21OfrENBWR-MipI9NCHD-5RSLayA564O6gQZOZ_YCg6oao1UzK-jdSJ0yUmnn2J5dyraY-LArZ6fkdU3vOH1OOG2i6QuY32X08v0fx8i2byLDP12JgVts8PT0QSZW_9zao9LnePZrGazmkoHHNF7KvsgNV2izRWdbEKvqahsC5nsmS8zyIHEYgzJ7w7bYcMMu3dBwhlIyP6zHfxUc99RrvR-E1uqErNnCPeswi_CmMSrtHAkf3hrz8gTR0vnNYgfglv2jXSaCsnBmHXRPrUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=qdFSUqZ8hRzdNgUUP9I9MiChlae7dCFSWUZr6B-fLzuuGhihjhkfrRT-cgH3AbVJrN21OfrENBWR-MipI9NCHD-5RSLayA564O6gQZOZ_YCg6oao1UzK-jdSJ0yUmnn2J5dyraY-LArZ6fkdU3vOH1OOG2i6QuY32X08v0fx8i2byLDP12JgVts8PT0QSZW_9zao9LnePZrGazmkoHHNF7KvsgNV2izRWdbEKvqahsC5nsmS8zyIHEYgzJ7w7bYcMMu3dBwhlIyP6zHfxUc99RrvR-E1uqErNnCPeswi_CmMSrtHAkf3hrz8gTR0vnNYgfglv2jXSaCsnBmHXRPrUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1nE5vuKe_amu4IJEhiStWR--qMomi868LVrc_79meNPN_nJiFeZafUYiC9dkNTgOOT-ycQclu2BkEmbwMoyt5vK-dd1D-q2pTSOIMlIA6_RsDClGtcUnQ0FKfc93gp2Rdawx5JiulH8Vi4WKfEbZK1nOPOyKDyKW0DgJjCGZDG5n7JYI7oM3E6FEcVXMR0E-5JQE0LmMHkH4fjCLFlIDfslGX4NDUu_Pti6tC1t--N5n7gb18UkhjgKWy6XD596zdF1xf6OUfJ7SE68BFB38heGO-xkjFum5ti57Ob-8DT-cfUdobmVYmyBN5Z2rb5_M0zniwGh4fVWmbxPea_MEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8Y2CM1EN_EbLLRuEekxIj0ZgQQL6TWUvdIKffuM1ek0197bm6w5IUBqDDAicCrZIw85gtLFauqN3FnWS_HSdKk0RoH6AmgFmE4zio2Hf0mu4eyu24XhJo7QDXijGCtkvRWTMSTCFQ24_D4G7-KPRY2bEWQwbmulq9x3Y1HieKLE9wMyD3na91QG74p4_twlwvCWg7LJ0pTkYYZM2dyzWGx9YCZCiBIwx9oVcVowHDUNk2yq94KKO1rbgGa1SyKOKLJhPEGVxBCYmtMGlN1W-yvn7vFiBy_vhfLuCHUTmtvTTtWAQPYYKaRB0tZnznCtWDvBOgaIm-7gCvOZenkenQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=UnI8HjtXpxzD96huEzyav6qqxz9RBoCQVatfIH1mNlAmNIYY7xiFNyrQyD-vmcqhUsCT8elm4RmjHeItLqnNsKOoGWoKyFvz9E4RoXHUSY8oFsHbBeFlgZIAYUMvIwF1p_pxOslxiUVCzXLYytF929g1z6F7CX4P0sIPZVazGA9nCNcdNar7_m8BzRSYG7R-pX3uqlpj9Nr1y_nU8B2ULuuFK8QP0A1bvn_foFSqlNGdsaFUAFJjGgDjVcJWNmSUkTAXmIneXjONFyBQybYAvsbes1ubfibSCVuLuXPXlL5hTKLeeHlyRjtofeCJOoLOwnxSoTgDs8wbFfadh0lb5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=UnI8HjtXpxzD96huEzyav6qqxz9RBoCQVatfIH1mNlAmNIYY7xiFNyrQyD-vmcqhUsCT8elm4RmjHeItLqnNsKOoGWoKyFvz9E4RoXHUSY8oFsHbBeFlgZIAYUMvIwF1p_pxOslxiUVCzXLYytF929g1z6F7CX4P0sIPZVazGA9nCNcdNar7_m8BzRSYG7R-pX3uqlpj9Nr1y_nU8B2ULuuFK8QP0A1bvn_foFSqlNGdsaFUAFJjGgDjVcJWNmSUkTAXmIneXjONFyBQybYAvsbes1ubfibSCVuLuXPXlL5hTKLeeHlyRjtofeCJOoLOwnxSoTgDs8wbFfadh0lb5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9RExGNneVEJlbznXGyfQkhWaEj45d_t13S0LpK9T7g2kgzXNuJEU-wbPjXA7InUtnsUrxxZFgS1N0GzLXT22K1VrHcrGcyLr5wU1VC5zV4fho6XAJ0TmzJDXlVblV6W1mtvFnzqRe1m1iFTvip06gNgI-n6Nl9boOpQp4e9QZfBSRCm91Xp8OxTiLAROQ7phq-WCgaIxKyml6hOCznHxUQeV0r-MToG7MOT--36JeY3mQveEibhVgir3UcLf_pG00qoQWa_MFAZgA6qVgiEo-ht7bmPoDQ9mhmYa93PFyvpvuEHlcl-LigSmz_Z6OR4z8yl1mEPGUTWf_XMWBv5E3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9RExGNneVEJlbznXGyfQkhWaEj45d_t13S0LpK9T7g2kgzXNuJEU-wbPjXA7InUtnsUrxxZFgS1N0GzLXT22K1VrHcrGcyLr5wU1VC5zV4fho6XAJ0TmzJDXlVblV6W1mtvFnzqRe1m1iFTvip06gNgI-n6Nl9boOpQp4e9QZfBSRCm91Xp8OxTiLAROQ7phq-WCgaIxKyml6hOCznHxUQeV0r-MToG7MOT--36JeY3mQveEibhVgir3UcLf_pG00qoQWa_MFAZgA6qVgiEo-ht7bmPoDQ9mhmYa93PFyvpvuEHlcl-LigSmz_Z6OR4z8yl1mEPGUTWf_XMWBv5E3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=pXIz0pF98a5kmqX4IFWo2kl1xAnrNxNTP3XoAQWVDU4dnv9rizWEGsVz8MYuO21pqhSPQ04N9Kp5FfhPE-_ZTCJEceEMFfRtpeWSmE45yUtnG4uT6D821pkrs9Rii0pEqt7jtIHl3zz1bK_UaoprXPcvv_ckUCGqq3IqvMo_tA-StioWZjLZtaGtAdD5zvpI4AEqhg8Ey2n2YCalWWrIfRHFTQXIB3fn7QAnx1Ga-AB9BbUFO3oTHg6Tjovq-fJ-12MrKMEOnsnhBq01xMYio04FvsrMzUuuwE6tvDPmCPWqLhyvGN5b_-q9__dGpW3RR92C6QjmSloq-GqgEVKMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=pXIz0pF98a5kmqX4IFWo2kl1xAnrNxNTP3XoAQWVDU4dnv9rizWEGsVz8MYuO21pqhSPQ04N9Kp5FfhPE-_ZTCJEceEMFfRtpeWSmE45yUtnG4uT6D821pkrs9Rii0pEqt7jtIHl3zz1bK_UaoprXPcvv_ckUCGqq3IqvMo_tA-StioWZjLZtaGtAdD5zvpI4AEqhg8Ey2n2YCalWWrIfRHFTQXIB3fn7QAnx1Ga-AB9BbUFO3oTHg6Tjovq-fJ-12MrKMEOnsnhBq01xMYio04FvsrMzUuuwE6tvDPmCPWqLhyvGN5b_-q9__dGpW3RR92C6QjmSloq-GqgEVKMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj7naL4_fMP4YiT9dViSC8JMRULYiXVP6Qc0W9CpuSY8Zvz1iN5jnJQQ-eoVgzfLP6-bqe1JboWemxnuxWYa3Y88Hp8rYL2_oIRMWuCEE7qiSJtVwRUMjQswNDmrzAR2A4F8YHk_f71asShXNWxpQLWMuhxzJ4Ywq7zQj_8CS9NowmI1QfeVni1jd34_kXDlBkg7D8PWHmY1GXHHnpCbWUaQZEhfqcdLjD6wVn2KqnAfEfn2AK618wrzl-CDDAPurAfcximOO_xJkR1Znj_VC-rvt6m1ox4XOwGPDub26lyoXJwdvCHaMulxuwpQUPrZpheNUTarGBu6xG0kHZfA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=HPmFgMAjYE7kSqS0RDLTZ9X1r3JNlXU1MXRIpftmnsMF-KYZ4_fREW_PxN8O387w_weqZtVAZALne8-GjsZ71RTRUSERED_pplsjd5YC2eEqSixT3D8AgEAZyWrY7mnERJjZs0clVi7fYEURjTOqnFNjE5gnK1bTNms_Kj9XP26DaQuOA6jYNvcjhW--qQu3-bpimDnslv00QaFjy5TZLD2ux19Us0rJ6CzTxHDzxo4Wf-QdH1ii7MmSTxKmq5-nxtFnrjZP9JwDGSktFw0_lWDW5awSBcgsU_ggpbG-pJS6OIpzCxE3TDHuCFfi2jArMGS1POwHKa0B5NUZKnkvMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=HPmFgMAjYE7kSqS0RDLTZ9X1r3JNlXU1MXRIpftmnsMF-KYZ4_fREW_PxN8O387w_weqZtVAZALne8-GjsZ71RTRUSERED_pplsjd5YC2eEqSixT3D8AgEAZyWrY7mnERJjZs0clVi7fYEURjTOqnFNjE5gnK1bTNms_Kj9XP26DaQuOA6jYNvcjhW--qQu3-bpimDnslv00QaFjy5TZLD2ux19Us0rJ6CzTxHDzxo4Wf-QdH1ii7MmSTxKmq5-nxtFnrjZP9JwDGSktFw0_lWDW5awSBcgsU_ggpbG-pJS6OIpzCxE3TDHuCFfi2jArMGS1POwHKa0B5NUZKnkvMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=LHzEBuw01GcidibWms6ZJFbVq4umFR7d-unPdK8Ix1L85lKzr9nOYF6Vq9q1DIVxyTI_-59xkxR8gC5TKawouX9ZzN06RE_3ajX742zvmfjgugwCarpLePt2BgbGPZJ4Ql9rWhKfr05FxZVABPIEB40_c1GRMqo7PNYoQUB8BygGfoNcWdr7dADnajIWQ_--ORtIaczBVMhZqIfRcX9fyR81sT_PTtdtpxqY51KOvy7zP7D0-90vJxe3ZMQVhfNURDyHcOhCsbAVZvPQeigHgDfOGfhH5mq3LZxHhfr2ksFXPmKq7byLeia3axwmfYyxtyhURUn_eh-EFtJBPfV7xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=LHzEBuw01GcidibWms6ZJFbVq4umFR7d-unPdK8Ix1L85lKzr9nOYF6Vq9q1DIVxyTI_-59xkxR8gC5TKawouX9ZzN06RE_3ajX742zvmfjgugwCarpLePt2BgbGPZJ4Ql9rWhKfr05FxZVABPIEB40_c1GRMqo7PNYoQUB8BygGfoNcWdr7dADnajIWQ_--ORtIaczBVMhZqIfRcX9fyR81sT_PTtdtpxqY51KOvy7zP7D0-90vJxe3ZMQVhfNURDyHcOhCsbAVZvPQeigHgDfOGfhH5mq3LZxHhfr2ksFXPmKq7byLeia3axwmfYyxtyhURUn_eh-EFtJBPfV7xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=C4Bs2-XwcO6cWrmBKimRY6lKbdpzOaaAD923AF-mH94Ld3Fdcdc4xkf2yXiKwzmqZFh7KCnyuTICfukjfY2kb2vAxThI__K9eUMZM8Agvg8Ga_kliDDBXV9MVmBndbvunARYSLf_B62exbm5iCBQo6o60oLhsckBx6jmVRaWXlkmr1liEzl0AdhsLJPOCEuzNjvFnYd0Pa4LGjUb_lhcc7zry6i7j0jjCzn8E2Hoc1ySpRngTjJSXz0LC9CtVBqcryI8vyC03ZyNN8LDHDzlBaTnT1O7fD6CSKFIEYzyBC59bNjZCxFGeJx1W7QkPxZjUP6O7MgdmH85xDHNy_6gLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=C4Bs2-XwcO6cWrmBKimRY6lKbdpzOaaAD923AF-mH94Ld3Fdcdc4xkf2yXiKwzmqZFh7KCnyuTICfukjfY2kb2vAxThI__K9eUMZM8Agvg8Ga_kliDDBXV9MVmBndbvunARYSLf_B62exbm5iCBQo6o60oLhsckBx6jmVRaWXlkmr1liEzl0AdhsLJPOCEuzNjvFnYd0Pa4LGjUb_lhcc7zry6i7j0jjCzn8E2Hoc1ySpRngTjJSXz0LC9CtVBqcryI8vyC03ZyNN8LDHDzlBaTnT1O7fD6CSKFIEYzyBC59bNjZCxFGeJx1W7QkPxZjUP6O7MgdmH85xDHNy_6gLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=eF6yjrtNNOLu_I8Ok5Ux8d-HyJ10EfkzSFI49apr5tknV8ebFqZyxoAyvbzeUj43tRzGTVjI0OI_98BSa4tzwkGqcdLxMAMJPU1Y8iwjx3xBok7WhwR_W8eORLtNX97LmP0B3_vKOoNTDk7hneIFjACRSj6G0hEnZlXi6rW0m8zoSLgMrjb_N_cvQo6m0PHTLRgyP0D2BXE0TcljvbEe9l0yRdgltUOJOuLJmcdskDp6HnNtzcD5L6yp7GB6odMeBTHgvOQgsPpCTO1n2z_ZYkQNQpAFTtRMOb3ifltgKfyChEUHlMqokJls-PYAvHu6FmZACmMG59S--8j74Uyg0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=eF6yjrtNNOLu_I8Ok5Ux8d-HyJ10EfkzSFI49apr5tknV8ebFqZyxoAyvbzeUj43tRzGTVjI0OI_98BSa4tzwkGqcdLxMAMJPU1Y8iwjx3xBok7WhwR_W8eORLtNX97LmP0B3_vKOoNTDk7hneIFjACRSj6G0hEnZlXi6rW0m8zoSLgMrjb_N_cvQo6m0PHTLRgyP0D2BXE0TcljvbEe9l0yRdgltUOJOuLJmcdskDp6HnNtzcD5L6yp7GB6odMeBTHgvOQgsPpCTO1n2z_ZYkQNQpAFTtRMOb3ifltgKfyChEUHlMqokJls-PYAvHu6FmZACmMG59S--8j74Uyg0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAiXAmsdlEiDZasw7uK1bf0mgOkQMclne4uCOHDTBaj99pRSigujlZ8K2R8S6fr4suGeHM85IAF2HMPs1IoOy7Gc9i2bfZPfGRyczgcNEqr5eUU-95iv4nmc6T20aFSVFB3a-55YWTbhqQCMH4VWcER0lGHjxl0Ira-YBhoYfpbM4PtxfUJWvHChowPALm98z0TAX9XI-20qbPXymPTqH6fwr7gjCbCvtsL72I7eHqT_aGt9Dg9u3YQQI_WysWE2M4TBE54GaIwMdiO_l5CQBTS1OjOLXaw4DlKt1wAe3W7h_fHfo5r2y52-rxdC2XuwSDQNdHFbmlz_jdkYKZK57w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=JCHRWD9nM7-90iJeRkPE5hzGowPNPmoub9uliZ2NKrJ6zPWsUUsN6pD1erXU0MLJpdSEaKJ0iQLDpq_RWX3kZ7RqoOHMQBIYb-BavUPw8AYDTZqZ40P1UN2rJIPovbsNo6pFuuOP1ru7qWtonrycbkkeS4YiY22dBD--gg6jSSARlIk_2QbkRHcL93P1IS2ijD98zC9azO3leX-dFUwpztgAfud5nMdLIEm5jpNLcvLTTXrtUrHfL9MpVTdGzOc50GswmJGuNG4vK9mx-DLaJCi6BtVdzJPd8Iro131yKOJyNYziDYSYJUyHDmebbX-ksV-xo1gqKPizK6vYBcE95g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=JCHRWD9nM7-90iJeRkPE5hzGowPNPmoub9uliZ2NKrJ6zPWsUUsN6pD1erXU0MLJpdSEaKJ0iQLDpq_RWX3kZ7RqoOHMQBIYb-BavUPw8AYDTZqZ40P1UN2rJIPovbsNo6pFuuOP1ru7qWtonrycbkkeS4YiY22dBD--gg6jSSARlIk_2QbkRHcL93P1IS2ijD98zC9azO3leX-dFUwpztgAfud5nMdLIEm5jpNLcvLTTXrtUrHfL9MpVTdGzOc50GswmJGuNG4vK9mx-DLaJCi6BtVdzJPd8Iro131yKOJyNYziDYSYJUyHDmebbX-ksV-xo1gqKPizK6vYBcE95g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ErBzbx__VEN9qQBjsrg78NZxnGJDsLhOE0EX0LrZG-glF4t_VgjANLCE6KwrX01aPltR2lHipeHuZnPkGQYrYawKjTF_qjTY4kegHvXP1xDAcJctjMisGlVwP__peKMRFmKFkNWjE8DpYo0QL4EzdDBoSrUHKufnUDLPE5_y1zBUtI-5X0GAOPeYeNVqaDGX6ZU2wAaF03EXLoz6IMP6CtXBp6oLJHW6x_TmWyE9OpH_N9UUrO-R32cVLNSzWFDvCOo0ZHYFmPnoRHwvab3daKDqKQO9dtFUv-zDUv8VqU7B01hVpfcGfedchhr8k2AoNdhaQtVJRsT3OQp15Y4HJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ErBzbx__VEN9qQBjsrg78NZxnGJDsLhOE0EX0LrZG-glF4t_VgjANLCE6KwrX01aPltR2lHipeHuZnPkGQYrYawKjTF_qjTY4kegHvXP1xDAcJctjMisGlVwP__peKMRFmKFkNWjE8DpYo0QL4EzdDBoSrUHKufnUDLPE5_y1zBUtI-5X0GAOPeYeNVqaDGX6ZU2wAaF03EXLoz6IMP6CtXBp6oLJHW6x_TmWyE9OpH_N9UUrO-R32cVLNSzWFDvCOo0ZHYFmPnoRHwvab3daKDqKQO9dtFUv-zDUv8VqU7B01hVpfcGfedchhr8k2AoNdhaQtVJRsT3OQp15Y4HJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfKxIdgN16aHuqV_PfGEQidN3jqAknC9FThB3YH6ioHYwFfoNxg_M77LsbUigIxRvddhD-FWpFITQIGFWbtuva-uUSCYtMl0bDJOH9N5gCplXlrzmc2o72Vn3ynszxb74YI-ha6XbIURzSZbtw4BIszwQv1CoxlhUjiLfute7WRq4imE81HqDnIb10Evwz_tLFyTLU9o-YQT5mqGdkrFLnxasHSO1KMc6Tp1juzdDfzPK5A28Wr12iL3UTfQAUahP-IX2esDGm2Yrh_SpKvGGhXs8TvFdfXLMLkrdqj3jq0aQdzdoqHPeT-VCJwznVJFfkuQRw1v99cCGQ7Of2v8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=pRQDhGzNJTDpxIJaUF82pV_Bppgn9wSZchpklFvGMJjn8JT1zgE6N16ERr036wQe4W7UBQj-Vn56-eVTnfxH0pzQ9c47RWzsvtcVVOl36f-NBLYC3G56Q_1wVKAHQtw73CU6-hPpAJYRnOCT7itseiM_k_olq06dtwYxQOUICD9eS6mgxOTzDSu62_jPvmxgmmYhcObmcAfDVBlBneR5bvaABDEqmhjybNlPFFXx8SFKvxp06aqaoE6K-vaS46GO_3MV8h89Y4J3bKu1unDHGcy1VJGcAm5EHXkD0Szc_p6ZgRgeHW4cNRdHKWEzskP1AIX8bndm9n-LUeTAKicl5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=pRQDhGzNJTDpxIJaUF82pV_Bppgn9wSZchpklFvGMJjn8JT1zgE6N16ERr036wQe4W7UBQj-Vn56-eVTnfxH0pzQ9c47RWzsvtcVVOl36f-NBLYC3G56Q_1wVKAHQtw73CU6-hPpAJYRnOCT7itseiM_k_olq06dtwYxQOUICD9eS6mgxOTzDSu62_jPvmxgmmYhcObmcAfDVBlBneR5bvaABDEqmhjybNlPFFXx8SFKvxp06aqaoE6K-vaS46GO_3MV8h89Y4J3bKu1unDHGcy1VJGcAm5EHXkD0Szc_p6ZgRgeHW4cNRdHKWEzskP1AIX8bndm9n-LUeTAKicl5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=vyBMoC-nP0Fv98W0VsWgr2hLYLVTm_VWB98vI4ZWrcehfvlLqwLisvzaLUOgpwIXWo_lnN48dPgRtKUjob-e82qMVh3OKfl1pX_R_ZwLCX64TOo9ve505Mc9WQ5DyjUzjBFFPv9WzjKqJ1LQrO6VXV9qoytydICyEAevmhg8SsPLjpPPRfgLV183Ior_SsmF1v_F_b8pXEsJl7Z_GrghBVe2lZXXDJ6lo1UyEeDVCYZcuQuQTaWeptkdK6lO2YKUKEmtmR29M_nfLCyP3dSua0-NzJ6a8rlaTZAJtlDfwtsgM1WXEm60PchMmJ9vWjH5NbTQV0-Iz7X1gyolc-mq4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=vyBMoC-nP0Fv98W0VsWgr2hLYLVTm_VWB98vI4ZWrcehfvlLqwLisvzaLUOgpwIXWo_lnN48dPgRtKUjob-e82qMVh3OKfl1pX_R_ZwLCX64TOo9ve505Mc9WQ5DyjUzjBFFPv9WzjKqJ1LQrO6VXV9qoytydICyEAevmhg8SsPLjpPPRfgLV183Ior_SsmF1v_F_b8pXEsJl7Z_GrghBVe2lZXXDJ6lo1UyEeDVCYZcuQuQTaWeptkdK6lO2YKUKEmtmR29M_nfLCyP3dSua0-NzJ6a8rlaTZAJtlDfwtsgM1WXEm60PchMmJ9vWjH5NbTQV0-Iz7X1gyolc-mq4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=RxOYv_7Vt5zLw6L8hcHh0JYL6vuPwHHGF01t8bPrkUOWrgBzgI2CztNK8vTWNRzNClQ0ToEVPE1y2dZmhEPTddk-HnfU8NgLf1zyAhoWdaIIz0aJp4PkCwJ32sL1zKkLsfvXP13K3FeL_m4UoE18W7Y_HIMcahtwT0dx43gYutSAJ1EvEUAq1_B9dkGn1U8206m94ZIMa1IVpnzV_9xVTPgwb6QzmhbNkxh1JSb_KCIwtQUC7XU2FlRu9O1CmZJpY_VwN3ZkBL9iYLU1wA0lluev3ZMj1WsEfMkdhWzjN8msCMqXT4GRDAHZ1opHgoVtdQRLHzzVjG2b54MA4XRFHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=RxOYv_7Vt5zLw6L8hcHh0JYL6vuPwHHGF01t8bPrkUOWrgBzgI2CztNK8vTWNRzNClQ0ToEVPE1y2dZmhEPTddk-HnfU8NgLf1zyAhoWdaIIz0aJp4PkCwJ32sL1zKkLsfvXP13K3FeL_m4UoE18W7Y_HIMcahtwT0dx43gYutSAJ1EvEUAq1_B9dkGn1U8206m94ZIMa1IVpnzV_9xVTPgwb6QzmhbNkxh1JSb_KCIwtQUC7XU2FlRu9O1CmZJpY_VwN3ZkBL9iYLU1wA0lluev3ZMj1WsEfMkdhWzjN8msCMqXT4GRDAHZ1opHgoVtdQRLHzzVjG2b54MA4XRFHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJCcwAQK7xtK_7u1ZFg2WCCBW2zxIrCFa-aj-GGmBJ4FKu4iK96BVNarMUfBBhTZsI577rdgXDbjAeRAz_8tFHIFeKOeId-cVOUgjAR8INfwm0FyR3tGwV61y05LDJ6m3av6cI6NAmYSEVnyrpN0Ky4MsXiNcWxcu8nKX5BnDjkypmyFUIEExiCCuynJYctiqYj8uaK3GscZF1jf5LOG1mWiNKtSDMNB4NvJbBrnV7joMQTF0YQg1Ye6ClYxn0H44uvyAdm75UkIRfpZ8z9AMJMPmqf9Xc3YBDCg5m3w9NGqsWIi6BGr4T-5ahAPX9EpRfE_7I5J0Ibq7ONUJ2UoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rq-qfUvmntSKtI7A-BKaMvO70gva8Fz2dSxXYoCBMxXwNq7W3cT7-fYZXLbZp40VHDMhF0bzvsUOBhM-nVs92l18RoQZt4YU7wYj-BTiOk_642C2qq6Geuee43RoLrag-8H44pgTnzmyX7h8fyXIU_eoDpLw6O3QuGYdYVaejONIFHmUL398z81UJq8gMqZwnc1p6qovIn_yILlEU_llEXk5K0SL2NGBgTJdCOi6JwrvzmNqcus2QcwAwxiUZj9JZ-q2lJUuan6OGBla1IySZ-x6QC2n02nVdojOg_B1BW9FhN207c6l_0AG3SFUWmi_0NTu4pycN1cU1RbTCjxjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyyrohgz9Ri1uq94lKONl-5T4xLIZcPN8ZoBu5kCjY2v5G68w5eWgmqbsWJtKkLob2NLRQbogd7X_hFTDIk8Gs7bDCN_XYb859VWxp1j0ZGmJcF0JUd2KY2vhDwMCMpEuhWVyLhqVR3mUXewOCIEYiCDn64CavZJ1ZejjgxADH9Nstorrr6VtvGjet7mNyfqczG7tYsTar3BwdrnpyJ6OaC7RkOwb55w9m-Yhr4vhEadhYOJEYT5UsceZxqmdGQvLXvkLyLqV1kyrFoMgi4VZRqDf8q_Dh9k6NSS5F8TVDkBgY90XwbynFlzIauNlDvqb2b4hIKiXJjHAi_yoqMeKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=JCjep7F0jvuXaNerFB_ZMyo9VcV46faClepxkYOuxeEC7mo6-9LsGtDmU7XudmBdUGWsVrjLIOueWPz-ZNZk9rpf_sFdAlPfJajh4YDN1PWFAs28nwRm5poppnjqmFKqQ9v7Zzjk-u2HUA_K2ltzJR082E4k9FuCWHM0xqRDAqNIDatnH7jRJrr9IVM1laW1-fuPAHZ6YSm7xlwqbERudxqTbtAHhDfC8DtCIOtebfxo6ybS-vxMXLifUwqdihxUYAep4SHVujhVwEK0NA9keqD0UY1ZPJfCg33dHWD9XnNkxZkqv2DeD3a-92uvsIGZpROFCl3yppXwVrnHT-sOAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=JCjep7F0jvuXaNerFB_ZMyo9VcV46faClepxkYOuxeEC7mo6-9LsGtDmU7XudmBdUGWsVrjLIOueWPz-ZNZk9rpf_sFdAlPfJajh4YDN1PWFAs28nwRm5poppnjqmFKqQ9v7Zzjk-u2HUA_K2ltzJR082E4k9FuCWHM0xqRDAqNIDatnH7jRJrr9IVM1laW1-fuPAHZ6YSm7xlwqbERudxqTbtAHhDfC8DtCIOtebfxo6ybS-vxMXLifUwqdihxUYAep4SHVujhVwEK0NA9keqD0UY1ZPJfCg33dHWD9XnNkxZkqv2DeD3a-92uvsIGZpROFCl3yppXwVrnHT-sOAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_2YX63Dsfy7VJvVzOqyDTd7cLnc7E1PfxO1oANrywMKX3AeCNhZEdkPSjChBidsJ0P6Ky6wazsL4lUygijt60dVmor5D0wjY0u7mu473YwrDY3cvjsD4dGi0nL9-ehn7w8I9AcfB3dOWXQwTBSPd9It9TkKhbELrdq0X1VhPSyw7FNSglMWfEsqhekvjMvvByblR2OcR6kvIpAUZqk37p24BQQODwA3FmkkPogCgPiQxHMObv6n9fzPbZrwbSumrBVOuuVjcFsdqWHbB0i_yFTzqMzUUQkanhck8EGfAy7sGJ0VMxqKN-8cZR9MufILhdnhdktBdAsna-O67O0PBL-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_2YX63Dsfy7VJvVzOqyDTd7cLnc7E1PfxO1oANrywMKX3AeCNhZEdkPSjChBidsJ0P6Ky6wazsL4lUygijt60dVmor5D0wjY0u7mu473YwrDY3cvjsD4dGi0nL9-ehn7w8I9AcfB3dOWXQwTBSPd9It9TkKhbELrdq0X1VhPSyw7FNSglMWfEsqhekvjMvvByblR2OcR6kvIpAUZqk37p24BQQODwA3FmkkPogCgPiQxHMObv6n9fzPbZrwbSumrBVOuuVjcFsdqWHbB0i_yFTzqMzUUQkanhck8EGfAy7sGJ0VMxqKN-8cZR9MufILhdnhdktBdAsna-O67O0PBL-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=rM7iLMS0zaw87PU_oWvjHHOg7vwITlPwL6RhGMVLyQ5k-DDF9zYGeeNKMTMX62YSISMhQ2IewhFKKo0Sh6zJaHQsfshTYmwS4kBR3AFn90Fbk_BbfkMDdQ6x8As4RNm6ceyY2TK_Puy8BWL9rylb62qGpMoBNH5QI-Serg6tTChq_WPjg-qo1dqisn644ZVETD2VLUNznQkVTdd_IQVyDFTSAJtPVwSVGkwN4sNdUZ5AZjrQcJinQAnxsLtuTnvLGV-6r46vCO-_V5yq6Yek7EZsTABf6xSD2KY55SCfSE9n2QrISLliE7LnUBghRcpdpPis0OZkEM09AW7H7EtU1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=rM7iLMS0zaw87PU_oWvjHHOg7vwITlPwL6RhGMVLyQ5k-DDF9zYGeeNKMTMX62YSISMhQ2IewhFKKo0Sh6zJaHQsfshTYmwS4kBR3AFn90Fbk_BbfkMDdQ6x8As4RNm6ceyY2TK_Puy8BWL9rylb62qGpMoBNH5QI-Serg6tTChq_WPjg-qo1dqisn644ZVETD2VLUNznQkVTdd_IQVyDFTSAJtPVwSVGkwN4sNdUZ5AZjrQcJinQAnxsLtuTnvLGV-6r46vCO-_V5yq6Yek7EZsTABf6xSD2KY55SCfSE9n2QrISLliE7LnUBghRcpdpPis0OZkEM09AW7H7EtU1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmTwl8CYPmbIgG-JwF2mw8xytKmFj1LT4I6SJCJe8Ay4Jk1vdetHQEpFmRMaPADKBdLoFS44dGDFZPPFVLp1UqKj0zNTa7asNfyq_RtyECeWBSyypXRS1BBfjcH7x1we_Af_pB64OwHjyQEba_fsQuAVoLCAqe7n2trqiUs1AJiBV0ii1LWjxp23VFbSiQtzAg_4MinHO9Eb6LYv2h8mctg_MI2viOzq2zSLxUkNW6GAnAvbo49WhADv18eIV7SA1wtipUsp54e3rVugQUyXiKfHuC-oeG0Xts49Dpktzaol2g-0sUPDJZSk8P_JXS644lGFZAXf837VNN-_zJkLeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHD8LTiacYm7TM13ZGL61mKfo3OT-U7DkggzcHR8NVAkL6S1YV4ZHF7yESFILXGjU8wpxVUlhjtPkbS9p7zHcfI5ajEUiJ42IocAbKN8vor6GhChAC_2ldergHnVN9FNdaWqXtARiP0U4cN3wK7G74m6g36LrJfPLUFB1sYu1hipDfgZmpDN8om8cg4m2GShulnSyyZHJ5Pv1s4myICD7THcbI-kZKcBxkBCvPtfe6APiWpAWNlobARTXewYUjJkJmJ1uRnXZQb5L4-VQyBZsOVTyw3E1A5Rk24Tq-v1YbE7VaqHlnEVxkAlA0m4wCt3Ps692pHq2qv6zuKk7IWDGSlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHD8LTiacYm7TM13ZGL61mKfo3OT-U7DkggzcHR8NVAkL6S1YV4ZHF7yESFILXGjU8wpxVUlhjtPkbS9p7zHcfI5ajEUiJ42IocAbKN8vor6GhChAC_2ldergHnVN9FNdaWqXtARiP0U4cN3wK7G74m6g36LrJfPLUFB1sYu1hipDfgZmpDN8om8cg4m2GShulnSyyZHJ5Pv1s4myICD7THcbI-kZKcBxkBCvPtfe6APiWpAWNlobARTXewYUjJkJmJ1uRnXZQb5L4-VQyBZsOVTyw3E1A5Rk24Tq-v1YbE7VaqHlnEVxkAlA0m4wCt3Ps692pHq2qv6zuKk7IWDGSlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHfqQyGB0s82UQ8kOpWCE6ZT-oP5N9Im6W2vfTRvsj8tVM0AF9dbcNiBv_885k3Q-o6SmU-CV2EkmFczK8oVpIddy06GRuXX1a0tjJYlY-e1S0GcLjBccewz5VwlcEckcCmWkWbmByZTx1eo_b4tu_p90SiCTvdifg-Lumliy2CsOhEf6jShSKgF4VwSN_aHkmgId_ertvTrOHfpS6d6O59TcB93BBqR3Y8tpZ0ZwwnMDM4vSiC5ImoJbGREy_R1xoL1xLJQLDvYGpoNi-Ior9xTrtxBRXScPO1O_hK1ahlDG3Jw9cIQLKPkWBGyDUmxB7HQaQHlTUxheeKkMD1bHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=oYQLi6PEYn7Nmdyy6m6nFvQlNgrMfFLvYCizD2xq7-Aq9R-5fSoga1xDcufjTDYPCan7gkI0tCFWhOu3QgCC2C0DnQBzGpDtxMtIKRkojYeRA5AZVKwm-v3N80BrdGCliZZUtnrbvi_DYLQwD_LDeXoN2-hCH12wpenVdTJZpIIgbMBp1WpBaqRL8bxn7QDt3UxXeu_hgBnaktKvn1AI3NLsYHhVHVx-zksnNYgB1Ln0EaqPDbJcQIEB5zpMOv2aCp4vfWu0JzBITBISwkR4TIpThISt-i4KpOspArCvQdWDyyrw3gkM1Al9YineysFp3sLVJ1Y3JiL5FpuTVADuEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=oYQLi6PEYn7Nmdyy6m6nFvQlNgrMfFLvYCizD2xq7-Aq9R-5fSoga1xDcufjTDYPCan7gkI0tCFWhOu3QgCC2C0DnQBzGpDtxMtIKRkojYeRA5AZVKwm-v3N80BrdGCliZZUtnrbvi_DYLQwD_LDeXoN2-hCH12wpenVdTJZpIIgbMBp1WpBaqRL8bxn7QDt3UxXeu_hgBnaktKvn1AI3NLsYHhVHVx-zksnNYgB1Ln0EaqPDbJcQIEB5zpMOv2aCp4vfWu0JzBITBISwkR4TIpThISt-i4KpOspArCvQdWDyyrw3gkM1Al9YineysFp3sLVJ1Y3JiL5FpuTVADuEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=s9ohIF1YKMr5mKUA1lNjYpWGwixp3Al0OlbrJ9sQsxNipwSpyj-J6lWnU_UuZt2hjgVGm3ADrjQWVJlBcYfbQf1zayWdxeG-A-2ILUivWCgQNnYsQqF1PVva8DPsrhDe_WWLGYDPhgisnJStemoJLzVvQG9XZV7ZCSSxckT0kbq2YLCMLxmkJURLdnWznxn866RY4f52dxP3tPFhmfgK64ZvDgN13Hiu1LBwC50khvdImBuD70fcerdGtHW62UBqcHPOC25C2ntLir68VFHKR3FlCRPS2LPqW3I-SsaLo_B29MNxF9m6JjZHmZaNQgJ4HTnQ7-MC6xgDSEPNCzfcZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=s9ohIF1YKMr5mKUA1lNjYpWGwixp3Al0OlbrJ9sQsxNipwSpyj-J6lWnU_UuZt2hjgVGm3ADrjQWVJlBcYfbQf1zayWdxeG-A-2ILUivWCgQNnYsQqF1PVva8DPsrhDe_WWLGYDPhgisnJStemoJLzVvQG9XZV7ZCSSxckT0kbq2YLCMLxmkJURLdnWznxn866RY4f52dxP3tPFhmfgK64ZvDgN13Hiu1LBwC50khvdImBuD70fcerdGtHW62UBqcHPOC25C2ntLir68VFHKR3FlCRPS2LPqW3I-SsaLo_B29MNxF9m6JjZHmZaNQgJ4HTnQ7-MC6xgDSEPNCzfcZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=ecs7negB8Q65pimmaGveFelfr-Sc9awMOtyotgUM9I2Ugu7Xhjck9YkRV9kHGsGHy_MJCW_-14vVrgNLkMqt92swZTFBDjx18OZ57s2Igm46ECONJUTWWpKxaf34DehJ1TCftMCnMhDeDjZoHf8BFxXkuSkgCWr9Tfnh9gakeeMQ2YdrwmKGDcY-qzgNbBA5wp1-Lv-IqrPpcoL-mghcFL1BO3TZDPbo9kGijGLPTVaK5w7tfxG5s8InTvb3k8mQOOijd2F3Btj8BbQB39KLenDZSORf2eyndhJMRUM-zPq5-R6is-7-5j-sXKL0Ps-oF5r9LzOqADo-hQMfzYxjsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=ecs7negB8Q65pimmaGveFelfr-Sc9awMOtyotgUM9I2Ugu7Xhjck9YkRV9kHGsGHy_MJCW_-14vVrgNLkMqt92swZTFBDjx18OZ57s2Igm46ECONJUTWWpKxaf34DehJ1TCftMCnMhDeDjZoHf8BFxXkuSkgCWr9Tfnh9gakeeMQ2YdrwmKGDcY-qzgNbBA5wp1-Lv-IqrPpcoL-mghcFL1BO3TZDPbo9kGijGLPTVaK5w7tfxG5s8InTvb3k8mQOOijd2F3Btj8BbQB39KLenDZSORf2eyndhJMRUM-zPq5-R6is-7-5j-sXKL0Ps-oF5r9LzOqADo-hQMfzYxjsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue7EmIVbx2m-01Ug_duiiBkynz2JlCHknE9-cwLVFYS-z3mspQ6w1rSuQJFpa954tujPACJxldMYWsEU6UeTYtcHSIKD39yufl4PPtxKleINUu2cx1dYiWgqd3cRp7Q8aNJetcckodvyKm-5npYKYgiiSWioYoR3MxoxYArprn4wtmt3jKWp0jlN2XDnilKPPZ41e-DLXBDhhjP7ZSmIJRpKGv6zrlxIBEivexvjC45u3Ej_i4khY5IIVp-5JVFcfHvaR_8dbu83pdqODNJPCyhVsl7bxMv7FWfvBgUkI0zqZTrpYxPtU841Nk5ffspTTai4sO4cvRkf6oxruRisww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pORphCbaJ8Ut7DVTN3cKQHkcXs1ebc2yhUyCCwB0FF-iieIaGliEaZF0qU6m7IaSQodsx7VfvuoguAjB_6t5ZvarXOmsCF_NZSp_XBAm0Mvedg4m2Wv19RiKjjWPA6RDDAcBXJ91UxVrTLCBU65vTxd-dmJgkgF71myj7GLYDH8QerZ7UestntJnYY4BBtq0RNVhq2Vy66QtoWikdpk99Tg-Wri8nOvCTUHe3v-40-CL3VjY6_HI520RVor0_IKXWzl9JuA-cBMd2vyzOKSvHwvlBFF6XiWaLbxrh5EALBFecMa0fxoNNrB6-y6Y4V8Wxzji_k-Uzy1rcmEuPZiUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=sHeVTbXvI39fu_vYvcG1WsZCCzJQyd-oBvX6xnzwQi-_rminTJyZNnbJvJiCbUJyf2ql-b76TMvB0qDTXkbKc053zgFUQ2-9Ja7Wf-duAAFbndkx2dmiKRihYHhKB6Ospuh59UQkCbvOeacxZCexXFzA0CLLUQJYUPs6z01_8a5-IuPqAMFTGx68PKKORmitr_Cr2_DZB50pN-cvm9A_ZkrAtDx1ry5QHRuQNY2L2FQt4Iwi-PknH_a6eIDb844UjdRnSXDbenNydxyqY1aQg3RXtcJcKHojYuAUzh0ega1sjhermGIM6zC8GsjNk5QL8nsKGB9UD4StPROiUiqmbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=sHeVTbXvI39fu_vYvcG1WsZCCzJQyd-oBvX6xnzwQi-_rminTJyZNnbJvJiCbUJyf2ql-b76TMvB0qDTXkbKc053zgFUQ2-9Ja7Wf-duAAFbndkx2dmiKRihYHhKB6Ospuh59UQkCbvOeacxZCexXFzA0CLLUQJYUPs6z01_8a5-IuPqAMFTGx68PKKORmitr_Cr2_DZB50pN-cvm9A_ZkrAtDx1ry5QHRuQNY2L2FQt4Iwi-PknH_a6eIDb844UjdRnSXDbenNydxyqY1aQg3RXtcJcKHojYuAUzh0ega1sjhermGIM6zC8GsjNk5QL8nsKGB9UD4StPROiUiqmbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joEh41gQ-2Jyc0I41LlphMIWQlSyzKo_FTgmCUeofcYZWHDxuqr5uxBzeYl5OC_E9KojLKfDflb6nD1bxQ9HsVlZ26BRmWLOGxlqMEGiyRL0-wmSMtsSFdjDBPRfx4ctzf0FZrM2fsVi_SpPe-fAJrjhfte83n1tIFfMAChTJ2885tKSU2q4YB835apHoLwccids1pJ7qtB1qn52DabIUI5uw07pQBGt9yB6YGSEaW9-r8nTMARc-K3x62l9P5VtQ9DYvbtokbbD9LWNR9NhNpYPAaZJBOsWqcbgL7tcKpIRyidluejDGoyHwAeLoHo78sqPs2g-8_i3Gtnb6aNFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruB0pk9Dgs0l5E1OKvWyxI3q9y5DyPFWQtVhIXnDif9C897lft3N2mGWBoDTCkHG3xZjz8NQMBfoO1klvyugfObDphmkr3bp0n9UU-WE9HdAmuSIKPjz_Q5k3pAtgBx1s_xPQ2pHkualnFNdNpbfExZpfXxXZA4LJqLF1gMU_1V2OP9JOREoO-kwxLfbAopkJSDKi7dp_K0EhyMLoNrgFuC7uatyP1uGdYs1n1PlG_7RLzRPRkEToidX_0HOsKV1pMj7tsro_weLQNgoj8iFvn7Fpb2aZFMEUrIKV5xrBa6cscMVLYjg4uywSQp_OtGAQki7wwNFfPgJR3NuvQyxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=Jchjr7THvyl70IKw6VgNyGetwB73vd32BYQG7hQfcWfoaybCjOHxUSViw_cdBHm7vfEQxcRirEYXIIVhoeusrgsOwEEedvRPNIvvRnX8gi7bNklOwqCxvcdy9WImcN1hOaLZHQOpK6uo90OpenIXkMfCXjqr_p2xJv1u1bITlbd9zSLePnbkEMTCWZggw1cUUgel483RmhTr0TLJwowrxkyu2Gu2a8VmeD70LSfPfrpal1_p4piqbGVQEob60cEZinh31CEzTyBvg6UB1-tOf3wrhVNZrPhAm-t9qXflSOWqqYU5MQpABWlXVUH_6CD5irF69SjjaUEeBupBcqloWKJfZ2ZZBmwmQCnvVPsaCs7xlM3RiCyrVbd5elWEgZNfPOF9dNbQoRUnArSH-IQUp4hDH9utrqRjuiAO2TQbd0KmME5GwPjOEdLr8aqYm9pfmpKBj4yv4N9ZWgNr3kP91EyIBkl6bNVtbc6OhKsp-Eyq7t77q2873-vn8W7kxtlvUVuxhNdckzTdRV9qGVyShZD8VdBr5GR0QPp33s-u3-Ra5ps9F_m7oz9K76_DhvdaTq6S3vOBFI8boDNIxP43dInswxEQDqSzgEx3RwrGF96ziW6QeMF8PtpnwXCykhFxYHYnHjVoKG899iZObPik6tOIpnkv97PhiznOuNEf3kU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=Jchjr7THvyl70IKw6VgNyGetwB73vd32BYQG7hQfcWfoaybCjOHxUSViw_cdBHm7vfEQxcRirEYXIIVhoeusrgsOwEEedvRPNIvvRnX8gi7bNklOwqCxvcdy9WImcN1hOaLZHQOpK6uo90OpenIXkMfCXjqr_p2xJv1u1bITlbd9zSLePnbkEMTCWZggw1cUUgel483RmhTr0TLJwowrxkyu2Gu2a8VmeD70LSfPfrpal1_p4piqbGVQEob60cEZinh31CEzTyBvg6UB1-tOf3wrhVNZrPhAm-t9qXflSOWqqYU5MQpABWlXVUH_6CD5irF69SjjaUEeBupBcqloWKJfZ2ZZBmwmQCnvVPsaCs7xlM3RiCyrVbd5elWEgZNfPOF9dNbQoRUnArSH-IQUp4hDH9utrqRjuiAO2TQbd0KmME5GwPjOEdLr8aqYm9pfmpKBj4yv4N9ZWgNr3kP91EyIBkl6bNVtbc6OhKsp-Eyq7t77q2873-vn8W7kxtlvUVuxhNdckzTdRV9qGVyShZD8VdBr5GR0QPp33s-u3-Ra5ps9F_m7oz9K76_DhvdaTq6S3vOBFI8boDNIxP43dInswxEQDqSzgEx3RwrGF96ziW6QeMF8PtpnwXCykhFxYHYnHjVoKG899iZObPik6tOIpnkv97PhiznOuNEf3kU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmceAGQjCP3DnkxcxxTL6xFYyyeTR7XO4K3grCekQ7KMJZG3A7EgczdyJArase3vNjlhtDds-IyUIM5PVo0JOa6EDo8WFVrsN5wtxb-BXzmtKnL5L1DjR5IVjKRYl-nixW_yCCzZd2N4BtxOT0WOrG8yZObmnowEG07kB1huR6lfShg1suiF-moaHkqDGOfx658esejuzM3SKluf4hBUYkqy9eojpjO343rCLGWd-mU0a4ahNq2pNZcA6Rg-uMoGX9zXg-pyEWx6_sgF6v9R1eX9ZNvB1D1LlInOOFg2cj-MbtMWeydetGwyEN0-2UZ-h74YVo5Q2W3liJ2qFksU1Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmceAGQjCP3DnkxcxxTL6xFYyyeTR7XO4K3grCekQ7KMJZG3A7EgczdyJArase3vNjlhtDds-IyUIM5PVo0JOa6EDo8WFVrsN5wtxb-BXzmtKnL5L1DjR5IVjKRYl-nixW_yCCzZd2N4BtxOT0WOrG8yZObmnowEG07kB1huR6lfShg1suiF-moaHkqDGOfx658esejuzM3SKluf4hBUYkqy9eojpjO343rCLGWd-mU0a4ahNq2pNZcA6Rg-uMoGX9zXg-pyEWx6_sgF6v9R1eX9ZNvB1D1LlInOOFg2cj-MbtMWeydetGwyEN0-2UZ-h74YVo5Q2W3liJ2qFksU1Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=fh47sk4D7s3MpzAC5l_OQKPMvLlKZhVRPOAdUcmEbtTBzBD12Sxj2YVdGrnL6CvJoO0wgIr9hPJaRFOU97w62vUYo9rJHy3a0zU6FyeE86ejj34FYmziIDm1_aop0aSt6s7taBxjVboqm5wwiYi-pLtWrxY4twzmMO8AShhW8RG-_JcAWbgdDzEbbycrZB_jJfNhxGMsniJAH_hIoNQIEr7MZQHglvV5mFHk21FIBKa_MiH1J2BB6SrXLH_0jUcjV1tafhJGDWfJj47nruqxCOpicbmmCAT0lEYETQXKTpu-eiPl_QxBWLjSBhjvK9au0NXWVRV5QCXeSw3yRtm_k4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=fh47sk4D7s3MpzAC5l_OQKPMvLlKZhVRPOAdUcmEbtTBzBD12Sxj2YVdGrnL6CvJoO0wgIr9hPJaRFOU97w62vUYo9rJHy3a0zU6FyeE86ejj34FYmziIDm1_aop0aSt6s7taBxjVboqm5wwiYi-pLtWrxY4twzmMO8AShhW8RG-_JcAWbgdDzEbbycrZB_jJfNhxGMsniJAH_hIoNQIEr7MZQHglvV5mFHk21FIBKa_MiH1J2BB6SrXLH_0jUcjV1tafhJGDWfJj47nruqxCOpicbmmCAT0lEYETQXKTpu-eiPl_QxBWLjSBhjvK9au0NXWVRV5QCXeSw3yRtm_k4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=ifxBbCihvbcePLqsTRq1apGeGsqTxZAG2fE-a4KGnoLaBy28gGry6Y2vAqRj9UaABrtClPCsGxdt_5Yi6rJQVRRb2xK_q4PRe51F_XuOWX09lTrX4cvEtedUFLLDGAKtdlTINcB6DXlCxNJBzVOv9zscHA5NM72BuN-wt8ZtxBqmz_JJhY7jlsuB2M5uIRk7RbwqzQ6erZbErT8_z62VFrH-SujdefSGUSx6i8TyfyzREzTD67mglcF5kRttgBYjo9822hWKVMgcXnH8HMJmQ3AKmN4oy7PXk0RVzQ3U8qyXu20BMHGSADDuU4mosGIFpX1iqk9rj-zxZSXj_0HQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=ifxBbCihvbcePLqsTRq1apGeGsqTxZAG2fE-a4KGnoLaBy28gGry6Y2vAqRj9UaABrtClPCsGxdt_5Yi6rJQVRRb2xK_q4PRe51F_XuOWX09lTrX4cvEtedUFLLDGAKtdlTINcB6DXlCxNJBzVOv9zscHA5NM72BuN-wt8ZtxBqmz_JJhY7jlsuB2M5uIRk7RbwqzQ6erZbErT8_z62VFrH-SujdefSGUSx6i8TyfyzREzTD67mglcF5kRttgBYjo9822hWKVMgcXnH8HMJmQ3AKmN4oy7PXk0RVzQ3U8qyXu20BMHGSADDuU4mosGIFpX1iqk9rj-zxZSXj_0HQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpMO4pP2aGWIfvx6bkjHpMpyfIEmEpZm3k81ttVAo5LVxNI6SSg3Nx_XM7dm9EUuTU6AN5FPoB8jyOKW2PrrYuC1m_WNE-JqbKGk-K9hnJca7tUvpQ4bKQDxkXuKoukZ5rzzNAdo-PTnJmWdDprb-cnRc2V1YG0v5Kw1bp7oFFMo1yYSmqUarH585n1YVuVcUBPq9_Guk2LrJbBMqay2rXrfqk7LEdGz8P3sw5lG5ufPw1vsiJOOgCrpxET_qqAF70NqUEbzsWL8sHT_xTGSv_TRs1vbdtJlWHhlKuEMhp8QiU-Bq9O60Jq_icqrxWulGlduKH8g4pPZAmkfRvEGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shGwPkLCrTcq6GanUEb2hkpBxSQgDSVP-ogJNyzTkoE9wqpaz_U3yp2OVsoBNgpdeUdQp8FANjcY8zD6FvzeYQO-e5QY-UbqZSqmYOaql0FHIHuVZRLN6xasskN-BtD4pcmqLwhoZ6Tsz9XHkwHf857LElXm8jp1AZblbRZG8F_gYdk4K6mh1mrHAAgU0pEIwZGkClyc46CjbkrhwOt4oOnXT-8suYy_96ycDAWAdWUY-AVXmoUSY7TLUyuKpEK_wAr6bVwGhyWQ2ZlFxsBldK4oajOfmIMAmkgixxblZ1DzFK4hiL1c9h3CY8gmcKkxmZUAQf-lEzOcTqnvFU2bdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUabTw5NINYJexrHHSym6lpllMrfTHx6umorJWxcDUCtksBZh3zjPEk7aYc4k0ePt0_CWuxMdJbiUuptkAS3ViBNuwHynxSNbi53b_e4FNnmkU8Mn1N5y7gWkANtcNAh3yo2ZILdiBxROaRlwrAEVBefKFuFADrV7-7m-ria1-NHYvlhRS-A3cVQOwNW533yFyolxT7mBfW5g7gO15a9q47x3VrwdRRe2e23vJNdMmYC5OL-rJNmEl-w6RrWG2YeCGvcR7sw10Q55jP6MUIMuzpkA9k4bG1GubyRlQgrFyx4tYL52D9CMWFxkOko5BXIVf4DXnbJ67geVetpWHTnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYJwORAzN6v6xmuj-LfOiuB4jnfOKbk9HtRSD1pXnmYZiG83my83DrntRHYAGmPN7pocJlz8mBUPV-s8iWZT1lHrzpit2Pt6bWYQsWPAkXJfM7I3Fmtyd0FAayn2jvIcaGLfHHyMQG_0VDHbJ3p519RzxbDaQSKRlDNb8p5scVLaBcbM17z9vY0rjfEKGKFIr5OYq4XskC1f5_DvR8B8X59pEWgXO_8_Z2iEoW33LE_jZam5ullWS8Xgh9Hy1EEcfJVpMhEHXS1QxGh2Crv3J-xKlnjcINjF2Xeq2JXxTU7GWO82a0g0cwygiCHVEzdKLge3P0gHJ9banIWaNaLCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpPYeWUq2JECHQ9J3oWh7eMvPcm0gViz9d1EsPHiMONGhqvRyZyQADvqBc8ic0ZkIOHfQZCFhcXRii-DexjS6NE4qocgLhCOr4SfFHPGViViKg6rRYM_lst-mPLUB80nOlVCiNDmB3pVt58VK3Tv24N1AvQ-xoVEpCFTXEqRnNKk-X7vwBBFRWKSBWSbyUdytWp_N4oBNpWY5OC7dtujaJx8DoQKOX3QTgGlRWn10qecMd1PZ5NCCgVu1guCbXzLEfAxb-A8TaIiBsHo3LmszjnM7vnExIm6orLgwJY8f5-lpFqHfYMjdMv2cWoUvDI8kFhgWqGljf35m7nXEFLAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=OPQtIXVDjj0vRMCvo86V8f08Qn8mL3fHYCGYcVkz3HVmRwnZGDiEh0wOG96RxlxbD46gBszsgOt-e6b81DSCpQ3HYcAb_OS8JhFUDJXMzmxdZoXykbOin8CU1wzRWqEZlxd5-D-XLYDCzolGdbh5K4APIY0wflH01rQdkFOhducNdUD-WZjvf5j8k3ulC9PjrkqTCZszT9G1zun6OxzVvgev2ueWmy7-NFtJLlraq5NA1Bt2u6iys8HN5X52r6D1EEMT9Cg9DfWCGmt_k3cfDc7pZRqaaevrQ6S55aHcHmOk91BjhaeUSATRxdCzhY4CPguffDADtJv7_qSQggGvLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=OPQtIXVDjj0vRMCvo86V8f08Qn8mL3fHYCGYcVkz3HVmRwnZGDiEh0wOG96RxlxbD46gBszsgOt-e6b81DSCpQ3HYcAb_OS8JhFUDJXMzmxdZoXykbOin8CU1wzRWqEZlxd5-D-XLYDCzolGdbh5K4APIY0wflH01rQdkFOhducNdUD-WZjvf5j8k3ulC9PjrkqTCZszT9G1zun6OxzVvgev2ueWmy7-NFtJLlraq5NA1Bt2u6iys8HN5X52r6D1EEMT9Cg9DfWCGmt_k3cfDc7pZRqaaevrQ6S55aHcHmOk91BjhaeUSATRxdCzhY4CPguffDADtJv7_qSQggGvLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=JMTP_IEMzP5tp0OI3V7s8m8lONQPPl3D-V31bp2Fm4A4Ia7sY83u-DOkq9lecvI21dtCaoNYO9oAwQ0sSMpv-CtH3FRpNlifnhh_4IrBdsFCg7v_5nJWM6bvZ0Ceo4dP7L0TUQ19UOAibeEKog3zdERcahL4MAOp1B3mbLvgpzq2EcgWDUiOeF6URW4Jq-7xpXulXtvjO3TwqChRZywFLJoKQGBRBVfNFsutIlyuJ-xOrHKrQIHCbzmCW6C0p-sxnA32GjEj9PVIS3PpRd-ZHXg6xb8PkU9PYjzIgDkNRJenY4tsDLcFKsnIetKyGQoZmQZtbyoW_2k0jM6yfQtPTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=JMTP_IEMzP5tp0OI3V7s8m8lONQPPl3D-V31bp2Fm4A4Ia7sY83u-DOkq9lecvI21dtCaoNYO9oAwQ0sSMpv-CtH3FRpNlifnhh_4IrBdsFCg7v_5nJWM6bvZ0Ceo4dP7L0TUQ19UOAibeEKog3zdERcahL4MAOp1B3mbLvgpzq2EcgWDUiOeF6URW4Jq-7xpXulXtvjO3TwqChRZywFLJoKQGBRBVfNFsutIlyuJ-xOrHKrQIHCbzmCW6C0p-sxnA32GjEj9PVIS3PpRd-ZHXg6xb8PkU9PYjzIgDkNRJenY4tsDLcFKsnIetKyGQoZmQZtbyoW_2k0jM6yfQtPTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO-rWvZeYzEJe2TsXkoZnJ_Xo-qyg-HqZhQ5FQqNFBbC6xlG5Xw5mQ5cbF3HSgUI2esGeDB2wCDOGDaES3mUoueBwLw5v6tivfgF_q9WHSIW0KKrSD-zWhWsDXM8I8x9wkr24hN_OGiPtOwxyTtr0YGBN2j5i-w4FmlI8jKCNgCIm66Jl-voXWzRkVibN051ZHFcQjgBtZDeoCr_CLALAJ0o1IsG6aEPK_TnMQDEuJmlzxLhgKB50joKqFV11Joc-H2r5m0v7QEfe5z3uZv25dJH64Qu4bg19963FRdG9VRn07qiNmtz6kdmpgXsPa-F_MGW5OHusQt8BWBHdClQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
