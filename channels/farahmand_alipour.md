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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 00:38:49</div>
<hr>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXdR7AcjzRjBEfZwmQItLC1crIx3hIJQtf_d9Ep1IBhn-OmMWNL7xmF5fdC44V6vc2jqlBdLFqslP6365ZUTsOfTPD2zNNg9dhlVr2_DldgqmvYysI-CJrNiY82wHvHh7MRFPQVoAzcexj0r1Qi4W4RtuDf5LosyK2HhN6VJTVTqN4WEO5-t0YZlZmdKv_XdyPYp8KDxZDOGJ710nKMxHMP9Ba27kP4atgaqjgW3BW5wJRRxzwEnOu2Qy2EeFe9DxGGErz8wtK8-OVfUEWFDt08RQiOI512acm3uJqxIDp71fg8lZFJo1i7BYX_qQHTwEBrLRCt_K4-CfAxeaW5pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFR9mP27XuuGctu-j9UIthXRXcR2HkauBcp1vLGDZucKGnJvm6eCgYqeLOvCJYxlxP_FsBBPQArNZnG5bWZDEwg8-oRrf-Vs395QhuFLe4n0xgtcckZPJNY5zaXOh57Dn2kPUElOb_GIltlAf_xxkne8VsmO5yH0tHkbhceyuXQVw48OkPF6o13-oWWgXwHuGqHV_kMRmdG_2cieuC8UaZz-wOvzGoDrem8KfCz2jRHSP2VrOUFiX6qglWYIWeM0Iu44DJe1d3irDKrX5zLqC4gT-lw5sJi9TyfIXlCj8YcxMBdPEm4W35CEv8IZAj0QYitzECSm04Z6x6YqyGioJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYSlidjSFGizuNxf7akejcFa-W0V3nxfwB2eUuasb1PzDVKm0REuO1QswdLgrZ4WyJV93uCy9_BZpeXJ-KEUYHDlX1b-9z7fZsAG2ydDh8z4RuMEgvzHWtqlhFOA9VrxDnu_5UYxLANrAAMNGawKNtqU4TjMISXHHNav543K7N4L01Y_MaezrDdVVXcZRU2YQtIddfM9WrdazZWIOSQCCqda5ucIkrYtJolCCDPEoYH7b0kMEvRE_7G6_4OxaMWA1ga4wICJlt4ERIUinY75EczzXSj5N7NNnHfwjJue1jvnSR05_ZdA28_T9idA13qdvgyflc3HR_lQKUVqdP-x2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxbQzXGl1WrvlN9I1lmnND2NVF945lmXSD8zphNG79RXXIsZ82X5Iugs0692acWqBXfB6u7Rj82YgnNyijd1KQ2hAhhc5wZANS_qyBB9d_2iTpz9tmQD0gAXQcsCP3WY8Z1xloET6OosZziCYCUgQH93Jxz4q_5YzWzrZfB5UVjMMiBjkHPDraHMngf-3mtEYLQ3MP8Ysajo2BR1KqfaA00qokDrdaLRwRyACaELmwVUpmXg0e3zBG7E5AvDzKftNByph9k6dD4NbNlKM6ABkE9XD4ccs0vXxocoD0zsWzrH2d-MReZQ66Yrf00Yv9v1UNLKuuNWZcHQVcnpV_B3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJRkbhs9IbWoRZovuIbAdCL8RXSrfv_LsUrHECXlOyAb2uyCnEEv9ImGnUkRyGmvAC06Z2YVpGx7izQ-p_b2WD9xm-bTyR5IzbJa30aWfPj3lmO4UruESejP3oMsOJpBG7NLchPSl77nDA5NmHdAG5jEjqbm4o8iZQyOB8lfip-ciniSz7YpCk9ZbLMGfjSmj_rW69BB-5xaFhnYeIyVHfGFt8KxkjcULSzASE3rL-HTEk3EI1vda8CAZRClwHoNtnY5UOogMYIUFLiFLHvjQw7AKDT1iD_I28FYmfPpNWm07UmLfMN-GmjQr4YYQyUOtDqs0B-TrusDlkbR-DeOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYpS2AGyOFJVNJHDIntWcTTBzu3PdjdY18dppzEwL1jCxfGZv6syisx77E5hiMHQEPYnJtUTSN9gZXYvTd177TsveVJqvA0LGWivRTQChf1q5mzc4OG542pY63Y5_CSOZgNYufdzZz-B3Yd_U8TlsXDG9NEsdRvjAQnl97Cgtu2iWJI-GYu-Fbcn96_Ol_EWdmmJwESqGPryWonkVcZphsPFW_ju0RB1ZI5L3FWhEzAHL0zhw5psoQPDc1xzjYkbeyqPUNtH2cw3TGnubrI2qyZJVsAmo5TIr4H1iisaf-1ECwLlTi1o6uFduvMAV5l3KqysaEt2kONB3pF3l_-EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6p8jGj_erqIzymuNNH7CqkXx7WFj5Q67dTmM0GBCBTeKO2JR06nEfkRn9O--Fj-ljU-O-lSSsZBWprk3mezHBDePIVi6ZjUF3FZURIId_wEl9OlAYkOpwlELJFhxj4DgcLBTxFZrFoOlFTdV4VSGqmuYJ0tj1Wx54wQ-ALKBxgXghOtmRcN-gvflFwaXBQRoihdZHMEZEEmZVsOiI8TqnmgyXs_L89XSsfht6uupp8xnV-1Iw5xVqdMeBTBmYb6za4XWJr5VUiSDnX9nfo4nHs82iiRl17m8SqKxXsUqbeAqTY3PETy5hS2adcg-GXXnROgf4GmPAdS_AWJqIHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZKiyY-aTp0qDEKrp6Yrrqa54CWEEkg5V7dIZrjj1SRcHW-wGLJ9xc9Nz3dP3nVQw9r3RH68-cRAaIg-ffBOPlUwaftTKPrTf0r3o5KurJrpTOCc4LOBslM5TKEz7XbKDZJv1FeI4oaTTf5JfLNDGtQ-XjMI5g7VmBjOsI37QepOpewMYYgfwIz6HdwIasc8nyqHBHrypuSS7IbalJdUWBwmI2Dd18MMGr5Vvb1q6k_SsGw5-wGuEXJT0OA131dZ1haGl7dyMrFf-eh37JwXLCOEE-ddBazRIvzf99d0X0D3ims1q_VAJDVh7SMPfrmr5xJmXe9DDHHhaivLJNYdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJyICSScG8w5gh4zHFUwgeBMPU78Ocf3sPu_Oy7a8kmg8xJq_CVlElx0QDixCzfbNFcCHHRKMJeWxK7-Ptinzu0Z2PRp4NxiOhZj_BSQT3nrRxm3BmiD2Vj8liPfNH8SrTExP_t-muWmu05ULgg2aoXohpu69PLaN7x0A6Katy8_aaiEEVtoMMksasWxOp42smVKf23pScPC9Nj_jUr8veXI3ed010P1PZcn-4oahzw_A6PVdXi3bhiKbx-vvqpWhrQer58M_uV21OI99eedtM3x_Qwz-6mVoF3hSep2OWpM31ovvP33L3NPhPcNTgvZj83-vsb62VPnGxtpWbCgiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtohJesNZbSJmgFGg6BfdC2n4_8K8nNkEX_hgtwNsihYrqRbio9pkVAiC5zX-fNZJB6hC2vrooeuXqAFd9L8M8qt3mimgp-llY3SKQ_gUNOySYYAFEIcAyIqRp5zOkurtHiCnzLrq7erwAb41Kd_v-kyLSXTalerTCZ8lTyNEYuIkYTt6Nv_LOKZu8S_PV8KD6WUspY3yTLdP0gMx48LVXAGs1R-yRX3hnlN4Ey1Pi17aGlfGpCV8DHAW1fhGVXWvL4yhm_s-q9Bo022yCFvmJQAUvNNUw7yB-5rdVxHucLu5WcSQ6HW2XUlQGr0YHsT-CU8DZ4Jqws2Mkggb_pSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNTYxJ77ojeY7zQleopB_UcHLTvcFvN1qfGY2PASFcLVRp3SWs8BdFg4uEIH4F0s0x62vRuQq-TP68L1HvP15RPtIE07aWBI0w2gVXUiZG6CZCorqqIYkviaXKLkaQPU1cjKwL6ipRgexiYl5u2RmKLIRKePqAJN1s0Lc6G9mFzqCw_TE6yMFmqshVj0oub7iVMUGYt7hvFvoYazDI8t89eCdzc1k2hTzp6qy4U257xUNnqofz5pmmmLGUw8YGc_ZkMbSwg2TTMv31ctymPn_HAniifMH-keA-WqYf6Lpm_7Sdwzvs11bnDKjP9YVvczXNVLhH1M_dx7FF9xpsbOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvVUcn0nncvG0HoZzOuLrTxwkAP-ZoM3mdCktSzHWlwyiI00K6qwEpvDhrq6E-ejROreuxedUXZYNl-3Q_7-ChSUyb9rRsdxmgtV2hr9bEnPjw1kCdYufWBKc14DerjipadA1PgSzwAf3AQBhQoq_0EOCBAkCaIQ74LEmKFaMSiW9KapYXbGx6RI5vqSML1eEgBnTr5SB5Wnc8YYqed4PU9CSev6SCLyu0ztjxOW6aX9ouXRisxhx3YLZxkcZ1QnFNiDV6DcihXbCWrkc3SIcjUModRWVoTEqMqUQ8rgt7eNFv4AzjqW9GFcoXMUGT_uEF4jaWJTbVddu7AP1x_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=ZWX5GN8CRmjciUxQtJ7d6YckNcyLrq8v5qOYxgS7Jn46zrDIpGPB5N1DbcwRhvcLCyso8wpJycdgEdHxYrEVK_RX6IApFmNGrHXA3OrWPmEliK1EESMeqen7bJ-VrMSAQOqll5nuvMR1uRTuw9UIvrz1dfcP98yzYSOynpGb8WvPRztb5PbVQGE4nZJSR7jcFCuljDGVhyN-T8QoDR6fJZy7C7kiTqKqh2iFP7R2MC0gMW5T_p4JnZrD1vxL8T9vP2qMMkSF1A8vwQYPQEKzXWprC6u1LLF3xLeTbxkPMDZdNb8J2YXCID-8Ilmc_f0m_Yhu_-yfrhU4Un0Ondyfqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=ZWX5GN8CRmjciUxQtJ7d6YckNcyLrq8v5qOYxgS7Jn46zrDIpGPB5N1DbcwRhvcLCyso8wpJycdgEdHxYrEVK_RX6IApFmNGrHXA3OrWPmEliK1EESMeqen7bJ-VrMSAQOqll5nuvMR1uRTuw9UIvrz1dfcP98yzYSOynpGb8WvPRztb5PbVQGE4nZJSR7jcFCuljDGVhyN-T8QoDR6fJZy7C7kiTqKqh2iFP7R2MC0gMW5T_p4JnZrD1vxL8T9vP2qMMkSF1A8vwQYPQEKzXWprC6u1LLF3xLeTbxkPMDZdNb8J2YXCID-8Ilmc_f0m_Yhu_-yfrhU4Un0Ondyfqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWiHG2sIfDXqTFwB2d1PBD5YYSkdGwzATTUXHb2ULXXQwNsRmK20D_OhXGNU-8OTN8u4mXxR2WUn31gRYzGlxIvUwUI0wScDa6_oaVYEKMsHQzw0RqdSI0jK7roxHOJ5UYQH_BSSqwKDAv_9_3DyjUB4nYfzXWuDLX0D3v2d9zytEdNYr8xsWXAixTn3TtSGOhdbFHZpyZ421BbOMjgZXGsIp1sDSpdamj_zgUk1LJtp5jQWcDfoMIXPUohLTaQuexBjbS7MkzjZga9flZwPAjKUvWbqFfX0w_IQeU7RtbHtovmo2vyTGlEL4S2dlK5fxjsO-j6HdPkDqK0JWOAhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=s7v8foVAoaca9L2ngMCdlhcIpdZ-2lv-hKswlzII0h-O3nHKytgipPJVNRWRTvRsAPJH-qGAnfF-9GTDITBEt56ZwVCs8qK3_o_J6Ak6t8uiwx3JergczL6LYYLalrrXfA65UEHqvtx0BnvbKxDJjY_CnJy7W6bEOcBuPoVMR__4DVvpK3d-MweXzI0tO7_zbi3LwdFI_GsH7CiNXDG9YABYAJifk4em4MEoUguxU6-ftE_LMkG5kUUvCXBYuEhzDmc6dN0S6ukXqWdXyhsV3tQQSPAJraUXvHotVHuDJesiAZHH68yj8WQtUu_X_W50ZKjz6-0ygH8R1VpOm8Tf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=s7v8foVAoaca9L2ngMCdlhcIpdZ-2lv-hKswlzII0h-O3nHKytgipPJVNRWRTvRsAPJH-qGAnfF-9GTDITBEt56ZwVCs8qK3_o_J6Ak6t8uiwx3JergczL6LYYLalrrXfA65UEHqvtx0BnvbKxDJjY_CnJy7W6bEOcBuPoVMR__4DVvpK3d-MweXzI0tO7_zbi3LwdFI_GsH7CiNXDG9YABYAJifk4em4MEoUguxU6-ftE_LMkG5kUUvCXBYuEhzDmc6dN0S6ukXqWdXyhsV3tQQSPAJraUXvHotVHuDJesiAZHH68yj8WQtUu_X_W50ZKjz6-0ygH8R1VpOm8Tf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBzVHQAHtRBNZOXvZIXi_1Uxfin3Ba3p-qfooftM5jo1iEYadRGKG5khPwDFH0D61d7WdVvY04MgL7PqStDSh7ShzvZqvFW4W1UgX-sjbtNlH_e8UJNClHlzl78pdDWc0zTzJ_OYXtTseJ4ZvPfxYeSu30VjSwRfa8GQOpme94d3nLoAMOCog_SWrzZ8lAG41HIh7rtCdAtugYv2RVZ3h5jkVXX4NesgPHRsSTcKz0S228LwN2VusMqdu2O5dw9IIomUZH1ZTOiNPeW21JfLlgHFZXOKPHFho5Gxf5w-eZhVfqJksavqkWobbvBBAAy6lUF-q9f8D5u4hcNbBDb-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlBtwjPesH8X7bxNdkMxVpNHllGS35bEmFqlq27J2y-O_PAGqyikqrcb9Fr6U1vJY76_XDgRzkL721w-0xgG1WGMx21bE29cadO9xz31Ie27s_4tMs2-Bd_4WtfVChwL5OvMdefEZtzLt1c6lG_yGYVkjP72ANuKj4V3kNQ66lnCteVs6d7G-mIUOCsfsGgLKV51fwROebxR-DCtptyy_N038dFv8vCOLfAq-K95xyGbCnK8VjkO7wkeQNpJZArS_08odAnPAf5r2xj8V8hIg2bvCMjp4NvKlWuojdHIMB5OU04qSrS8ZDgvRPr053So01M8IhhwPEOInu0FbKKVLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxYAJb5oioPcXxeAl-W8wbCZYRZyjo0m5vghyhKJMt9MmGTV4PEf5D7YWXLcr6lDctSPC58EoBPVDNI82tdten2-TAkfAuxN0dHZT_8ZLD4R4XN8Fg37bjS7afTEWR-nL1H9IvsOnHW3QMt_vN_5lZ1yfc8t3tFpMJcqTyi9T7ZEs9fSjR7Jc6Kl09h8dUbb6SQziwocaj2aGDPxfwWjdfa8giVJaR7eMh_-_WI7Vn_N0Fm6f5PU2Y50aAmCIq-NGZFn6w8WFGdzMFmFIA1JkWi-M6XkcxR2enlgfSLkmkkqLDyHanA-0sP5ZlQainkU9xQF0SdixmTeMNcuP7vItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWFasbeI8L6rLbCXxYF2RicLZZIy6g9-ODkPLs1ZAJ9XcQnLy3blDEmQgBlo5jAd9Wy17-5euIHmiBRHE8CRZxyTmZOEkPKJkBDEOClpELy7qTW6KoRk3xQ1TRcBsmrUYuWHU5g-jMkhIn753jF8s3I5DrBpUY1YjxHph4wUEZd9BmhCiZXtVbdyXnj0WEo7a2ypXYzrsRwbQuqX93lVSLlsm0fnfz7V1hlq7TtNDMqNdgIhxa1NR6uggvkqfp5ZwUitYjK-LN3aY9DQ36pJHjXaulxZ-UNQvv3XOJlGb2-X4KaRnBVouAwbZguVpfgRKxJtO45DDWi680l_mseD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtkNNEixXfT_iWYnp7h_H540-mInUo4Whe9Z0D31To7fyZZXCj5QNsj2aTNbq2jAs78X1KXMTiVmPdtK8MOHTRKy5O8RVCoqm58MwoDtdvJkRSv_5uvmj3tFmeMS0Yo0dUI45hNEWZtDnSx6Kfh6oTT3ZYUUn8i9nhMo6oFzToni1uGyOrtQE6GlN_YrRcqIag1eFlNNIGKgcsSqdWLWWuhB30ADdTucQ85rLKhDhJUMfmF4pSmuqrMCMmM392lZDI7vCjfAijd8WMPvDtwRqHRKtsG9bmzROcCvZTotTU9--1HOlMV6F4H53xLDD0vHvH6JpGUxeOMGiun9QVvavA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfu2MM34ZV_CPfJVpX9E2Xz2LC74cPU7pCVya84JoVmjWLkOsQiMCjChIngZFbBg5BlZaf1p-z7iax5mLgB03REbod3HDi6AlspAgkYdy7WWy7zR60FP3WjagevEe-H8Tt9KAZ695hNW5PkmeZkzY8NDnIKr0BuJaIP8-455Apg919Lhu8gEJy-LKRyn4pE8wq2vEOheJwC0zcbtcXXq2xKRsRNXH6wRdsYij0Aja04wf7BsyGL-p0073yNNAg0dR7RPLoVe_dj-tyk8-G0jTRE4AZrK768_FqJwoXFw_SThzBNiJFoIT-O-lTl7qsbu4QpdJiCQP6DmSQmpU8xxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=sz_mP4A_8IG0cCRVlWbuoOidccioCWeGDJMRbkt6rkbcqE87pd6cT8ltUgMeTdF8S6Ln8PM89LOmrfV5VrCxK36_efOxe0bNcMz7mxvMYtceS_REWcVWjk2Ow2U3WQz8pLIJBngOyV9cFP31cy5UR0y03-7um2jLpvgvS--amHcdk8tBORTxy8wS7UvBjv7PN5eOU3K2dugOonduasgiLbUyAGhndG2crSpLS_tLhleuKpGvtsdLvOeeSbXf1tdVba4f_S3aQ-CeNjfNHdEDVOgQKia3_u5lWQr2vfrlc1an59wSivc4i9buzqEZtD7sbCQdPQbRjfmC-KDv27bhxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=sz_mP4A_8IG0cCRVlWbuoOidccioCWeGDJMRbkt6rkbcqE87pd6cT8ltUgMeTdF8S6Ln8PM89LOmrfV5VrCxK36_efOxe0bNcMz7mxvMYtceS_REWcVWjk2Ow2U3WQz8pLIJBngOyV9cFP31cy5UR0y03-7um2jLpvgvS--amHcdk8tBORTxy8wS7UvBjv7PN5eOU3K2dugOonduasgiLbUyAGhndG2crSpLS_tLhleuKpGvtsdLvOeeSbXf1tdVba4f_S3aQ-CeNjfNHdEDVOgQKia3_u5lWQr2vfrlc1an59wSivc4i9buzqEZtD7sbCQdPQbRjfmC-KDv27bhxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=QOMXqM_KoP-64sznT2oAR_GDjynSKlnseB5bsEbohKnMZW1wN8K0gKiJpo4a_hfmIa-gLv6mr2IW51QHwPDkFPuleN-dydskHt8om8Znso9S0u6xjUFChY8PgrbtUYMqxfRxl4PEse0g4SRuYi81uV3jnG_tbfTeWNZtxBk5twN7tBmVufT9J1TMkJ25jTxigamZVXMqADIvIU2g7SlWE9SyNfmLIKrCkxkhUdNA-Vt_Rw_lBp-7vBOo_cjv_4zQT2jZ9XM2Ml5s_5R5Q08C0KNPNruGw415tFgXhEndUQeK2Q8Mn5hZKz_OR0zGIZq9Cy_Od997QeKLlWfpEDCuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=QOMXqM_KoP-64sznT2oAR_GDjynSKlnseB5bsEbohKnMZW1wN8K0gKiJpo4a_hfmIa-gLv6mr2IW51QHwPDkFPuleN-dydskHt8om8Znso9S0u6xjUFChY8PgrbtUYMqxfRxl4PEse0g4SRuYi81uV3jnG_tbfTeWNZtxBk5twN7tBmVufT9J1TMkJ25jTxigamZVXMqADIvIU2g7SlWE9SyNfmLIKrCkxkhUdNA-Vt_Rw_lBp-7vBOo_cjv_4zQT2jZ9XM2Ml5s_5R5Q08C0KNPNruGw415tFgXhEndUQeK2Q8Mn5hZKz_OR0zGIZq9Cy_Od997QeKLlWfpEDCuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=ceH12BNGPFWr1KoqFqlqPEK-wwiU_m-W1LQ4rEAmIe_pEbicbAw6TeJzyGg3MVOgUmA0a4vHgxKIsu4jj_pFLLIgbXR5MSB6YzD38W8JaWfrnOnvecjFhCLvyvaG0oBUcgYcVSDyl1drgytTNoxyLo3-HYWFcOvtc44CwVdIzgP5s9AKJKmevbbudddqbYegmjkxEX9W7sDYK9UgoBj8Fb81PJttQ10Cl6gXO71eda1Rzx5pbAFB0DOGOI8pkOEO7WmGlum2kOJmmKVRN13WGkuxnFlkxtn7G1qkYan-FTh6fmw5cyNwbzqcLDYV3xG-BvYjrp14H7Wajo5ow6bRXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=ceH12BNGPFWr1KoqFqlqPEK-wwiU_m-W1LQ4rEAmIe_pEbicbAw6TeJzyGg3MVOgUmA0a4vHgxKIsu4jj_pFLLIgbXR5MSB6YzD38W8JaWfrnOnvecjFhCLvyvaG0oBUcgYcVSDyl1drgytTNoxyLo3-HYWFcOvtc44CwVdIzgP5s9AKJKmevbbudddqbYegmjkxEX9W7sDYK9UgoBj8Fb81PJttQ10Cl6gXO71eda1Rzx5pbAFB0DOGOI8pkOEO7WmGlum2kOJmmKVRN13WGkuxnFlkxtn7G1qkYan-FTh6fmw5cyNwbzqcLDYV3xG-BvYjrp14H7Wajo5ow6bRXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=SNe6L_ghXSSkaRdbJY4xzrITSjNNvJe7jpI5v1e-mAHrjCgBTM4xpTSwKVehnwP4psLenv75lo4dIVWoztyUyT3SaE3-NZ6T5NJynByAf1z6NmQAzAz1L7M_omTvDrQ93gbtiCZM8MWI8MZMMueuQB_z_VCLxsaIGJ3uPZw7X1FGAj0L1mt3VaraSN5UchPH2-FJ6jSBCxc2Qei17BaUl4AlsXGooUdfnsYGXzl-9DhDUvyaZcv35JfoDlP1Jm-pMZrbOMa_SNkKxylm2qY_XIQGnsMcM-vQhtPG4m5TVjXzS7ow_QQsLLzhpNIQ2K_dF6N8QbNDG-3D8R_Lk0NwaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=SNe6L_ghXSSkaRdbJY4xzrITSjNNvJe7jpI5v1e-mAHrjCgBTM4xpTSwKVehnwP4psLenv75lo4dIVWoztyUyT3SaE3-NZ6T5NJynByAf1z6NmQAzAz1L7M_omTvDrQ93gbtiCZM8MWI8MZMMueuQB_z_VCLxsaIGJ3uPZw7X1FGAj0L1mt3VaraSN5UchPH2-FJ6jSBCxc2Qei17BaUl4AlsXGooUdfnsYGXzl-9DhDUvyaZcv35JfoDlP1Jm-pMZrbOMa_SNkKxylm2qY_XIQGnsMcM-vQhtPG4m5TVjXzS7ow_QQsLLzhpNIQ2K_dF6N8QbNDG-3D8R_Lk0NwaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VugMDBr2pomIXfukcN7GTFvjcxVkQG2HnLaESmILVxJNwG_M2eRq3mQObj68PX28JFqgAerDppiuZ6BU2jAaU0FENZ3ZYl7v9XV1DW08Ybg9KfWrVimlYZMGaM6svYnwQvD534uZNqSU5z1B7zRMskOBond6UFqQZKrp_f3cq9pXgK9AnLltH2HJcIp1uLAD36e6Firabr8UTMLnJ103gGKNGvXtRwEs2JrjLx7VIaajvi1pbjKzAjBDNpJxSZeyvPRCeXqcxIiLYSesybejuK9Y89ImvbuNpVdqPhrgenp3MXBoowSAg4NiLDXaFgVr49LqOpql7lXCFcDCNOhkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhOABo6l0efpT8Gt3y7d6SNaZKc2m0MShdtc2Uq9XgUCEBV_BU7dCkMkBM0GN-6_nB1re7L0cPnFKZghBGxOcVTrzJ7CVoQ2it8gXXgX5fLZSzTirBhsw8mfpxaKjh7fNDQx2fQGAGgPp17aVbmuvHCUflX1J7gOqX4X7XSBKCcoGx4g6Ok6Ds9GssZylp7wxmE0U0bMr2Q5hfuCvGZamYRYsyvMdLFLHsiclOnFZHTgJWMKfoasmjsf12lk5w6Is5xvLdpQ2kkvzMbUKM9qwjrcEZbeZX_4Ra1vSdI6fNAMzVGHVf0IHpo4rRFAVeoMO3_YXY5tdmtZUDC9Qsp9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=r7GwWEM_wqw-3bnxAFdyOE3oAbX6USaqMk2muA35oWtxZJI514x8lQlBwnXECc3DJFrxDwJsAXG5aNrjVmd_fa_QbALsRy_vjnDjP130ab94JM0NqRNDd4Gnig4EhuqGCNCYtRLPa6DTXx9-FREofdIcN1aHe-mtGMzQ6jWSpVQFDYz6srInlhVP1qvv8fJ88RYLpStqTkvHwhu2iCGEMmCWkccY1xl0_O0hAyYbD0-8YcuA7zP_jvGD4EmbFdDtAJ6KlKr8zvR_E8C8EWDoSnLY0XK7X4KttIJjvsLsPdzzfoTNuB8OQjqW45slc8eqhjUh8rtre2cn6R0K5X-SDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=r7GwWEM_wqw-3bnxAFdyOE3oAbX6USaqMk2muA35oWtxZJI514x8lQlBwnXECc3DJFrxDwJsAXG5aNrjVmd_fa_QbALsRy_vjnDjP130ab94JM0NqRNDd4Gnig4EhuqGCNCYtRLPa6DTXx9-FREofdIcN1aHe-mtGMzQ6jWSpVQFDYz6srInlhVP1qvv8fJ88RYLpStqTkvHwhu2iCGEMmCWkccY1xl0_O0hAyYbD0-8YcuA7zP_jvGD4EmbFdDtAJ6KlKr8zvR_E8C8EWDoSnLY0XK7X4KttIJjvsLsPdzzfoTNuB8OQjqW45slc8eqhjUh8rtre2cn6R0K5X-SDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9XONVVNNDcSUNcRkxgZpgDBC7QCE4PSyQbbBGdGIOokUEVOs4KiSUgtMbZDsoFmUAqKzdPQwK8uL9gkCsCs6-qH6Mi90faS6KCpH3O06vx1Yan2LMOEL_ErsO2-YvKtjKsLLha2zagpg3AVxqVeX6GNSl1hwcxL8Kk5yWmq18GH5XZBYbd3iweSVIOOjJnJai_8OB7_-sUxROaShNufO847XbFfPRamAwK4LYMgt8jRMkc_ZGAF0qMytm8N0KI5RoIeq5L-QmoIX4skYk801HlVr4E7UrOF1XuaG_dOfKYt4uxkRd3ycvG4xIPc5dOfI7wGgkSuX592gTjRHMShLX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9XONVVNNDcSUNcRkxgZpgDBC7QCE4PSyQbbBGdGIOokUEVOs4KiSUgtMbZDsoFmUAqKzdPQwK8uL9gkCsCs6-qH6Mi90faS6KCpH3O06vx1Yan2LMOEL_ErsO2-YvKtjKsLLha2zagpg3AVxqVeX6GNSl1hwcxL8Kk5yWmq18GH5XZBYbd3iweSVIOOjJnJai_8OB7_-sUxROaShNufO847XbFfPRamAwK4LYMgt8jRMkc_ZGAF0qMytm8N0KI5RoIeq5L-QmoIX4skYk801HlVr4E7UrOF1XuaG_dOfKYt4uxkRd3ycvG4xIPc5dOfI7wGgkSuX592gTjRHMShLX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=FSAnHbV_KH9eye8O-V5L3PKdUZEiNPO7eR1g7aiV5LqSWRF-4Q1CRRKscQx_sNZqkhVvT7zPIbBo0RhaR98Vod3PWDb9EC515SnKekd1SDRV2FmdkbWiS5rf_Fq-CMT7sWFUIU1eJ6Ye5dE-e8wbKjIHtNOp3QYeQQ5QAuZJpEAtwkLJOdahVqd7b-qnyb0kX1DKxgaGRhhul0LuY0Zo2JjG1dY2ULuZ7c1MRlHoKuKTtUUSpTfrJQGesYI6nC3DLsMKGc2GmdBmZL9d3n4UkifjUv31n_O0q0sQCZeMUmWTAs8HdA81A5rGAW6DeowZS8MlIbRZxsGLmMguVDAdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=FSAnHbV_KH9eye8O-V5L3PKdUZEiNPO7eR1g7aiV5LqSWRF-4Q1CRRKscQx_sNZqkhVvT7zPIbBo0RhaR98Vod3PWDb9EC515SnKekd1SDRV2FmdkbWiS5rf_Fq-CMT7sWFUIU1eJ6Ye5dE-e8wbKjIHtNOp3QYeQQ5QAuZJpEAtwkLJOdahVqd7b-qnyb0kX1DKxgaGRhhul0LuY0Zo2JjG1dY2ULuZ7c1MRlHoKuKTtUUSpTfrJQGesYI6nC3DLsMKGc2GmdBmZL9d3n4UkifjUv31n_O0q0sQCZeMUmWTAs8HdA81A5rGAW6DeowZS8MlIbRZxsGLmMguVDAdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz6pgJd4RQviBsmzEz4E1XYwiADcoPJIdQ1mzw2UeHj4st8PLNbOqX-jqmghxLynU8meNZOt-k7lyuFRxJ-BxPEa_uUqMBRaCDZk-fN-ZNRsG3BjZHF8-j4p8ypCvSYIj8nhsF3-TwQyQB7cmqebN3aemdUvhgL-v_0ClOv31mlapgEqXdUlsRBxJrHY-afDanrpTXxpMju6y6j2SxJClwQrvYhETTtRDyc8TkXPAzcm5L57KLB7XkikszRBkoOnoM2fE8OWRCGxykT7FGKviwv1fBrAtzjPrlw5uUyM_tXLzr_NuoAWeU7trbAgyxfNStMHliH5l3gL6lIjvrPu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Z07xMvdeLnEuoUkglO6C0Bak2ipuSUnVGyhr6627leUGzFdjQWmQenjKEzqUoshQLVQWIGBFT1orkifzC_5yV0RDI82YAQ7jQEzP2daS9IEytv6rRjAnh0ddNKuMnq6ATruw94GV1vCuAF3WJ7h0RTu8wRdAtvq8saL6BYunxO3FjCZXwpXuG6HhRCdIr--DMmUPiNu-ZtsFGlTdSvuja4uu7uPkvBEelZLFDcNZs0d8KxKhy1k1IQb62ZIDimOARLc2vatxyCaNZDqObbjxRZ_2udnvS_8ZEAB2JOiWx-bWM7Mi7kH7Ngj19wOfT71IImaZA_1g8M4N-ArSqFLaww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Z07xMvdeLnEuoUkglO6C0Bak2ipuSUnVGyhr6627leUGzFdjQWmQenjKEzqUoshQLVQWIGBFT1orkifzC_5yV0RDI82YAQ7jQEzP2daS9IEytv6rRjAnh0ddNKuMnq6ATruw94GV1vCuAF3WJ7h0RTu8wRdAtvq8saL6BYunxO3FjCZXwpXuG6HhRCdIr--DMmUPiNu-ZtsFGlTdSvuja4uu7uPkvBEelZLFDcNZs0d8KxKhy1k1IQb62ZIDimOARLc2vatxyCaNZDqObbjxRZ_2udnvS_8ZEAB2JOiWx-bWM7Mi7kH7Ngj19wOfT71IImaZA_1g8M4N-ArSqFLaww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=vXqjifkMIRgpIoShKtNeuObpVfVs6u5t_JtedzG2Q4n8XLQp1hi0TlVMWb-W37uIH8Jq8okSIQfpPxSeA0pxaX6tzcuPgIeb7VzGXGdHa0JazeZxId1x3wbKL74S8VSSGK-dBT64Va2smncwRse3rsVhZ8d7pt6D-gplXaLQSgS30zKz-z1TsG0uwE5JRhaQhJcqDpJlH-Sxz_Hbs2RV64wkh_hFAPtUzBlG5FN1PKDQnEmtAaYiHRgALUZiY5q9LViLBHNhQgBK7Zbh9amUFsTF7Uewd4Mwc0u_uTCkDj-wEn-fRtCIfTwjpd5kkbV0vEy2MGfEcWvyxu9ghs1aQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=vXqjifkMIRgpIoShKtNeuObpVfVs6u5t_JtedzG2Q4n8XLQp1hi0TlVMWb-W37uIH8Jq8okSIQfpPxSeA0pxaX6tzcuPgIeb7VzGXGdHa0JazeZxId1x3wbKL74S8VSSGK-dBT64Va2smncwRse3rsVhZ8d7pt6D-gplXaLQSgS30zKz-z1TsG0uwE5JRhaQhJcqDpJlH-Sxz_Hbs2RV64wkh_hFAPtUzBlG5FN1PKDQnEmtAaYiHRgALUZiY5q9LViLBHNhQgBK7Zbh9amUFsTF7Uewd4Mwc0u_uTCkDj-wEn-fRtCIfTwjpd5kkbV0vEy2MGfEcWvyxu9ghs1aQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=aJkZsWasKie2EjVNeSzcCxQvQZQ04vyxqQiaAY8V-SQyl_eqg6jpfgj8UMK8BhVJAN7fjhUzARvkq7S5MKF9EO27I02imJAw3izRo1x2sgvCF_YQsHFD0Xa6HWvrzs2FM5C8gxahLigdkQpitsivUZHn9BE1x0cNZ7YTvpaZkYfucxoWhtmbN5cTM_NQBENaDr1NCYYA55431wGCPSqetz_V9-rD2cYvy646Zi9lSqqQIDz_Vljshj_pF-x0AaVI-jBehqaoPOKg8EyTeMsbL8cTRoH4suAZ7CQJpzToijQuWi5MgfB_0Oz_KdLaNFcsrX6wXeRAuCqFqTpAz_BfJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=aJkZsWasKie2EjVNeSzcCxQvQZQ04vyxqQiaAY8V-SQyl_eqg6jpfgj8UMK8BhVJAN7fjhUzARvkq7S5MKF9EO27I02imJAw3izRo1x2sgvCF_YQsHFD0Xa6HWvrzs2FM5C8gxahLigdkQpitsivUZHn9BE1x0cNZ7YTvpaZkYfucxoWhtmbN5cTM_NQBENaDr1NCYYA55431wGCPSqetz_V9-rD2cYvy646Zi9lSqqQIDz_Vljshj_pF-x0AaVI-jBehqaoPOKg8EyTeMsbL8cTRoH4suAZ7CQJpzToijQuWi5MgfB_0Oz_KdLaNFcsrX6wXeRAuCqFqTpAz_BfJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=mmLbvKZkhxNUxr6shf2VByrMKcv56fu1vmjwiIJgYOMM6PDVGxP_vwq-WcvDXTEXlb--TEZDbnbVN_97lEP7xjwSOl8Sym6OVVR1QPXPE7KuqTqZ3pxJ89xOu83TRRKmS2B-DWnON9viOh1ZxBsIpbw1_eWRsrbuSQAIJHu1Osngj0J6pSkFgtNc2YfFhXnIyJGSOZmGGVMDWyRWjvbBudkBJZ8F-_D00paMsy4LMeV0We9iJkLAgS8I5QwyR0dmW2ulDCfV10nVPTbPxKTQvPdOwT0gF8VWCyKuqtpVvarKOrPNeTh2Msb8Jez8bWZnwFoJ2t-D438Sdt1Cfum6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=mmLbvKZkhxNUxr6shf2VByrMKcv56fu1vmjwiIJgYOMM6PDVGxP_vwq-WcvDXTEXlb--TEZDbnbVN_97lEP7xjwSOl8Sym6OVVR1QPXPE7KuqTqZ3pxJ89xOu83TRRKmS2B-DWnON9viOh1ZxBsIpbw1_eWRsrbuSQAIJHu1Osngj0J6pSkFgtNc2YfFhXnIyJGSOZmGGVMDWyRWjvbBudkBJZ8F-_D00paMsy4LMeV0We9iJkLAgS8I5QwyR0dmW2ulDCfV10nVPTbPxKTQvPdOwT0gF8VWCyKuqtpVvarKOrPNeTh2Msb8Jez8bWZnwFoJ2t-D438Sdt1Cfum6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4QZ9HalVkJ13rpUVh_Dkju70Zucfed27w-_dfDS5FbewhGEgZqMo_MiWqZDDZ9USt9qg0UcTtrh7IaqeIhtYVelWPRP4ilmB-W0syxDWGlUENXTfaQrP-CGFNPW4qzXw3MWop6L7czZw9St65BlGpu8Q7bTQoeRRKGmbGAJnR6XviE7JlEyDeGIeDiXaof_PMBDCbBwxu9w_XhIeKBwu08SujhxYODvHJfXB0xWITSWe2_SPp_uoSw-5OiEUvP4-gRygE72FwsOJVQ3_Ms6kGThLiik3oX04RNbbnGiJMV8Afz16jdOXb8djbUQ4xqR1e-i0fscoXe8QlGJ-SECvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=lBKXaYicHz5nck98fG2WubIZF--CYpRcJDN8723qP7ZvWZwfpTX1KCiWgN4-_Jm4JqJvmbvhWeDjFNS6RBrQ-jDaK0Fys3uvtNZvfUllXMWQyKXprUaDpW59hQepcENCpd4-ZIHfrk7kIOrJ2jtL43mghtPitRG5bMOkxqTxMPBxa8jXSd9JyHOoY0rpJ5MThGv1OOGy-eHrOKxYTzRwxZTddFHb4qFHDa-yaAtgxvkGX1EFSsm-9I7Kuz0yiqvE7B5Wbw4DjhdRY-yUrMGz0AZf-YGnJOk1KVtyQ1ufjyXk__BLok2O70_Dp_7e17wQxouxEVn4Ywvmhu8HcQ1i7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=lBKXaYicHz5nck98fG2WubIZF--CYpRcJDN8723qP7ZvWZwfpTX1KCiWgN4-_Jm4JqJvmbvhWeDjFNS6RBrQ-jDaK0Fys3uvtNZvfUllXMWQyKXprUaDpW59hQepcENCpd4-ZIHfrk7kIOrJ2jtL43mghtPitRG5bMOkxqTxMPBxa8jXSd9JyHOoY0rpJ5MThGv1OOGy-eHrOKxYTzRwxZTddFHb4qFHDa-yaAtgxvkGX1EFSsm-9I7Kuz0yiqvE7B5Wbw4DjhdRY-yUrMGz0AZf-YGnJOk1KVtyQ1ufjyXk__BLok2O70_Dp_7e17wQxouxEVn4Ywvmhu8HcQ1i7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=DxRPNQkhU7Ht9sTC4c4g8Eg7XwHsVfzWIJuvjJwJF28-bUvOxg-s09ikJ04kG6i_av9hMIygDruMP449lpLi5YBDnWBqXWsXRv_DO9WxaECmK9PQ5p3tZFHgH-laabseN4-h-8V3zJwr40A6tQdmFbI9Xchwioxn2UvxAYhFqMNLgac4MUEabRqqONiSgvD8CRG_nfR7eui7BCmUr8KIIqj7ccx8SrCyV-o_rR8b_97YIduc_LwLU62UltAhYBUBvxPOJXA3tTsDpv7Wd4fgBJhix6La4mSYwIZc24L5Zlsg3K-Nb3kuUQi94c9ybo-4GfQZphMZtTzuwBGcLgIopg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=DxRPNQkhU7Ht9sTC4c4g8Eg7XwHsVfzWIJuvjJwJF28-bUvOxg-s09ikJ04kG6i_av9hMIygDruMP449lpLi5YBDnWBqXWsXRv_DO9WxaECmK9PQ5p3tZFHgH-laabseN4-h-8V3zJwr40A6tQdmFbI9Xchwioxn2UvxAYhFqMNLgac4MUEabRqqONiSgvD8CRG_nfR7eui7BCmUr8KIIqj7ccx8SrCyV-o_rR8b_97YIduc_LwLU62UltAhYBUBvxPOJXA3tTsDpv7Wd4fgBJhix6La4mSYwIZc24L5Zlsg3K-Nb3kuUQi94c9ybo-4GfQZphMZtTzuwBGcLgIopg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eojqcFDNxoj4ZlwViCtq8T4JaZFDjpzH-LnlzqLIoczQtADeUn7MfH1cgA-WmxAi3WHh8nJlgvKIpQIxcB4lJW4gmZB0vPuhfyDXwgsxlKO9KEJgeg28jhjL7hQSLjiye9RIKHBJexig_CUuryH-0_dm-zL_D0vO3fbBodbqtip2OXIHcwtWQ4KiIuUO62erzSDLHXzCt_hrFteHXMDUAOK3EX2Np18mX-HmIaLwm6QebU5sGQrkkwSgGncWqpU9uX-KsGPzt0VDv4N2H_-PsXr3Tgbqnk3VuebfAd5-YuGoS7AXNC8gDlzBK5EvKhHiMMs11PRhFKYsXz0Y3X4MLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=MAu4GLDRdyyOAmJZIy_U2SFRUkaY1JGlzAjwqdH_vv5XaTUFeaK17sVK71SpJ5czqCDlYMLa9fyvjvMKBkPJtMj_7FiqeZWf5AWQogejFfQDIa12N_DLZwyZqkQ0tB-_6zBf7gtwxtX42Lr8b9d82MNrA3i5-um1GLxLru9pTB5YgzPXaBeM83F7kjrNWExiUfhv_xN7gEKTKkOQZJZarVkQ2NqFAoORPGKr_DpWleE7lVKVqxquLxWqD26PKzGiX_kQqpA-4sDcxLB-v34I8OWntQFN-dKSC9MfWVUAjGVA_Ghfkd3KJdg-ujDLrk3JmLcdbWWBqjp4xmLe7A1_EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=MAu4GLDRdyyOAmJZIy_U2SFRUkaY1JGlzAjwqdH_vv5XaTUFeaK17sVK71SpJ5czqCDlYMLa9fyvjvMKBkPJtMj_7FiqeZWf5AWQogejFfQDIa12N_DLZwyZqkQ0tB-_6zBf7gtwxtX42Lr8b9d82MNrA3i5-um1GLxLru9pTB5YgzPXaBeM83F7kjrNWExiUfhv_xN7gEKTKkOQZJZarVkQ2NqFAoORPGKr_DpWleE7lVKVqxquLxWqD26PKzGiX_kQqpA-4sDcxLB-v34I8OWntQFN-dKSC9MfWVUAjGVA_Ghfkd3KJdg-ujDLrk3JmLcdbWWBqjp4xmLe7A1_EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=vJDQsmwROnu7lZcpkDVx9fn_iPNNjNi3dHMw4Zez3bra1_bNct3nafjLhg_3C9-WmJMg4aWEgiAnNe6HCc8Q5A_gj1Nw26ZWXYC74IKUDIukCTW-qYC1RtEWoH5ApGveXcE38HLQ2iU6pskuIbnclsBVlMXH335GdN6EhX2DGzjnlBBntEMrWV5xnPfdqYLgtwVHPx-Ppo7edldepE_VVRLSSx4BHitTXHsbKwtk4U4rF8Jn_GbovqGgZ8OJs0w5YEiTY7rBtf7aEP8K06X-28E7lIySxM-M-6MdTerhqV-Rw47cCwhZ7FI2gFNwsSXAjsULmhHzQ8MLj0YNZdE3cDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=vJDQsmwROnu7lZcpkDVx9fn_iPNNjNi3dHMw4Zez3bra1_bNct3nafjLhg_3C9-WmJMg4aWEgiAnNe6HCc8Q5A_gj1Nw26ZWXYC74IKUDIukCTW-qYC1RtEWoH5ApGveXcE38HLQ2iU6pskuIbnclsBVlMXH335GdN6EhX2DGzjnlBBntEMrWV5xnPfdqYLgtwVHPx-Ppo7edldepE_VVRLSSx4BHitTXHsbKwtk4U4rF8Jn_GbovqGgZ8OJs0w5YEiTY7rBtf7aEP8K06X-28E7lIySxM-M-6MdTerhqV-Rw47cCwhZ7FI2gFNwsSXAjsULmhHzQ8MLj0YNZdE3cDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6BwGAFe40--BKRCp8MLito3p5dtXQKRp50njgMA8-EFkqWoWlJwDSvkPJ_Dj91IgsCzaMxto9qWrfaI61Jk2UZExyIqaAAE_zLlL1z4vvzUb2FwD1WwWlzoV1LMWsEwSo5KkFqgOu0C9vfemv37qO5NfUN5irwFR8L_ZVQ8zu2KSz9ShrjPGk5T3THSv1qyhDeWSFe8NkLA0gNW5N4k_nV6LF_of2F1d8VJ26agCPWRqWFi7caIgCqwHAYu7U6WEuRuo97pOZQSHHtYiu6gOveOM6m8RrEGe7OLgtB879E7-a01oaDCs70ks5Jm0tpzOP2UF2xSD--DYCYuIPiDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9nGKalG2PXXC50nShFTNl9XKVxZQqHdSztPiqbEG-ClkPjaZ1jtCfROL6W28gq6NFN5EazT719o8Ql7h12elsbwdCIStUF44qHTajCYrKnnB_EdP03Q6SObAnUWfalcpsjJV0wsGdQZFwhcyx2k8pI4V58orpZxG5f_iHTuouiIxHQ78HAtCH9xt1W5qGXksRtewEsMVBE3eRw8N2nlErlysfsrdKwkX8t--5lfiUhqsWOLI8coNvTeBpCaWlV6Z5sTVbymX5NSLe59OlBk6JZtQv3ghQjqNRwu6rrHe9XAB5bPId9G292KAHCBUuacSGgeuVH_Nlemy865gpwzNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSoRD0cUrEIWEVpm-qmBvxc_8g-51keI4W2cmgBi2LYpU_fExmQb3FNEe5MOajVv_pAUQzWxCgdheb0rgLDyNzFoPuQMlR3Env0J-eHqVvepTSxQdGUBvz9xkVyz2gSL4endrkejA8eua8yUJGzdWSMTA98mZIhNd1eeRz0zdRi_OCuvKw66tAS1o9olnL57S_QvxoQZEuEhwiCqnDO-AlNLbZcoYLudmTE7vXfD9iSPh15RWH4AfHuZhymthqRXxOA1kmS6R0qwVX8POZcVyzy8rFEDrx7gX17QZlhKG5N4Y_KgnNzVybN-KhmekULsN4EN3zPKRbRUZVhna-q9MA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=T2oEeS4duATGK0HmXAGesJxUh8X8PHUQeiWWTWxAUytSrJwnGFhzJ_-wWuAgSEv1TxGqHfK4tcRuDx56SpMbWLrkFUEPvjXMo5odMlSRa9DTeA25Kc4--jrGhSLNetsCjz8Yq_FIkdtCxNkQjWuIJkS2hhLKSC9sJuK9pKEwNCuREjE2VU17EonlouYtLYIzym4tSVORS8uOnCAH88W49oJqPKdlNJmXBRxGTqdDcq_l52PRLhrQigtmEHZLJ2zKxYHr0PDshXVJ9A6e3iWih7_NS5GJn-1RMW_2va9Q0S7kjzfHcg0nAjPw1TCOWDIXxoM2oh9o8nsn0LRbiNLGkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=T2oEeS4duATGK0HmXAGesJxUh8X8PHUQeiWWTWxAUytSrJwnGFhzJ_-wWuAgSEv1TxGqHfK4tcRuDx56SpMbWLrkFUEPvjXMo5odMlSRa9DTeA25Kc4--jrGhSLNetsCjz8Yq_FIkdtCxNkQjWuIJkS2hhLKSC9sJuK9pKEwNCuREjE2VU17EonlouYtLYIzym4tSVORS8uOnCAH88W49oJqPKdlNJmXBRxGTqdDcq_l52PRLhrQigtmEHZLJ2zKxYHr0PDshXVJ9A6e3iWih7_NS5GJn-1RMW_2va9Q0S7kjzfHcg0nAjPw1TCOWDIXxoM2oh9o8nsn0LRbiNLGkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYiW22aUegtipHUE1Vi9hKS9WXoZHgILdNcTCHSw7B8Es5NHLqDMX2XbPPkMi8Pe55TWq_xpXEw2mXh4CGQQz78u1qkLZQAtc29q9Xg6zl_6CT9OrqN-SLYVOk8yLyY3flbYcZEt5NRdyr5YsKIQrKJmoNzSfk5szPXBWAK4HA-XLyM4BKle3VfTlmRnFd1n77LA-Zs7ZQgX8r9vxfJoPYw3YWjNRzCf0S175cIMDyRkjsNz-wVfN5RqtI-BQJKZrf7ADz4S35Z3_fun1Pmvbk2OzqlB3bemKXQbmkgfL4kqmM7Myko33yrrct4QXf6aI4CFI-peSEmFGwvaFHFuGmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYiW22aUegtipHUE1Vi9hKS9WXoZHgILdNcTCHSw7B8Es5NHLqDMX2XbPPkMi8Pe55TWq_xpXEw2mXh4CGQQz78u1qkLZQAtc29q9Xg6zl_6CT9OrqN-SLYVOk8yLyY3flbYcZEt5NRdyr5YsKIQrKJmoNzSfk5szPXBWAK4HA-XLyM4BKle3VfTlmRnFd1n77LA-Zs7ZQgX8r9vxfJoPYw3YWjNRzCf0S175cIMDyRkjsNz-wVfN5RqtI-BQJKZrf7ADz4S35Z3_fun1Pmvbk2OzqlB3bemKXQbmkgfL4kqmM7Myko33yrrct4QXf6aI4CFI-peSEmFGwvaFHFuGmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=hiHr7em3TifzYgqjXrl6Cz2CJypZPVW3-IhDhnDqR10a_xqrT9_AbDiHZRzkmWwEz4Ne2Ax_TIRl2RZtxAgHv1TmEHUgzseZtakrondb2yjqTLe3ypQxmNqRFZ8e2026Ifj3CMdC2jJatlpYVupKaT3F-A1yo6umR1uwR7piCsRBKuxwkLuhSWEOQbzsVufZIm2MjgjTIvuCyZS73I5v0aXrPrQwqj712h_u_rlOFX7REsgXfer1f7ysWNmndOyZ4TDWoLMlFS6hisykXumj8Xzd8lMtLrt7tAnUoehjJE6tVnaK66mK3B83J-jQuyy1qvZcWNj9X7K5ayY21MUidw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=hiHr7em3TifzYgqjXrl6Cz2CJypZPVW3-IhDhnDqR10a_xqrT9_AbDiHZRzkmWwEz4Ne2Ax_TIRl2RZtxAgHv1TmEHUgzseZtakrondb2yjqTLe3ypQxmNqRFZ8e2026Ifj3CMdC2jJatlpYVupKaT3F-A1yo6umR1uwR7piCsRBKuxwkLuhSWEOQbzsVufZIm2MjgjTIvuCyZS73I5v0aXrPrQwqj712h_u_rlOFX7REsgXfer1f7ysWNmndOyZ4TDWoLMlFS6hisykXumj8Xzd8lMtLrt7tAnUoehjJE6tVnaK66mK3B83J-jQuyy1qvZcWNj9X7K5ayY21MUidw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4jEwafeBJmzMSP7YGhJZRQdNCc8S5YqxjQR_UxveQ1IrzL3brnabeToqMyo-ivfoYqthuGUXnaVin8tyJrEMOBNDY6-F3Kjded37JomS6noca98gNZum6Y8bVIebaM-sNXV9sP49cWoNSSYXwWzoVPraTnFWgb2ISyY8PQjSfPKhFepDMzSmhFtYyiZgpbm3r1Y8GUcpJU979IQEwPDTojmvkOlTgS3zEX1r1Jip4bKEjhP51N2trHXv-xusBtXwX6wJHpQLGRBPV1M0IQLlL97wKrd4llcswpiwxHlZ53QRaH9VxsSflcxeS7NxjSpgKUaQWarAxJgozawebLyfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTj6Bth459O78wvVX6QWmgN7NFBjh5HxTvLlYmE9h2OFq7_woq2gCCIQ2zRsMGImW-1OT1TDf6hZfrEkO-w4ypJvmQHpK7s1X27iEQsCS26yQPoGmuB8SI2DJIuVSPkjhlAcXnrlvp0qkXvkN0WWWxGNez7zXWYNZG_PK3o4G55NYFyVQx_-q2FtWIfak6D-tBZPC37zwYYc4hDRBSqeet50okDC90nQiF2_h-Ppbak6UHE9ihmtEpWzBYlldbjetikK1LCWQTia1Rx7Fs93h5SPbyINmkWdTvz7QADy_i9PrLlX2k3iiwb-ZU2-pwTV_eb6Pz7ZZBzYmJmYWoHsFjDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTj6Bth459O78wvVX6QWmgN7NFBjh5HxTvLlYmE9h2OFq7_woq2gCCIQ2zRsMGImW-1OT1TDf6hZfrEkO-w4ypJvmQHpK7s1X27iEQsCS26yQPoGmuB8SI2DJIuVSPkjhlAcXnrlvp0qkXvkN0WWWxGNez7zXWYNZG_PK3o4G55NYFyVQx_-q2FtWIfak6D-tBZPC37zwYYc4hDRBSqeet50okDC90nQiF2_h-Ppbak6UHE9ihmtEpWzBYlldbjetikK1LCWQTia1Rx7Fs93h5SPbyINmkWdTvz7QADy_i9PrLlX2k3iiwb-ZU2-pwTV_eb6Pz7ZZBzYmJmYWoHsFjDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=LhsQvb4o76cWn7Wtpwc0q6YdXtMHjZsbq-LmpdPerD-KSfVr28sSftG7i0-kDZpjTMoop7gbiml2PDJ4HxrGSnTgAI7-TRrCBkIbpfH-EIRAfInmNNmC1i68r_OB4mzhhMwTX2GKQX26tBSkz9i-S5ltWBQtIUlzG7-mg6vZZcbOpn5C5YrwT10to9WK9dSU4reQ7mvsm_ZxP1HHBDur2TCBE8TTLfLpzhFFOtgNIF5ml8xGGzoY_YkglE8S5ox74h2NKLxHqfg3e6oDfhI2TjaX8QQ4FWeUFTQkD5twhiG5BLXotsSWLEpYfqsl8J_5qZCRdFK2EKEUfxciQYgyow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=LhsQvb4o76cWn7Wtpwc0q6YdXtMHjZsbq-LmpdPerD-KSfVr28sSftG7i0-kDZpjTMoop7gbiml2PDJ4HxrGSnTgAI7-TRrCBkIbpfH-EIRAfInmNNmC1i68r_OB4mzhhMwTX2GKQX26tBSkz9i-S5ltWBQtIUlzG7-mg6vZZcbOpn5C5YrwT10to9WK9dSU4reQ7mvsm_ZxP1HHBDur2TCBE8TTLfLpzhFFOtgNIF5ml8xGGzoY_YkglE8S5ox74h2NKLxHqfg3e6oDfhI2TjaX8QQ4FWeUFTQkD5twhiG5BLXotsSWLEpYfqsl8J_5qZCRdFK2EKEUfxciQYgyow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=fmmVUU4nLRZJ4onKjtzu-In13vX25Wn9eYQ68VRKcuPMaL5xIyKYm0ri52-TS3Fbsij6HqmTU-eH39pem0ViQIpTSIifMUmVou0UjzKpV6_tDQMDDvXU1enMHwxv5OdTYZpR3tj7W4-1ala0LtqQNp8ImhkvMmtjXTgmEHedHK772JeqBKeWcyeFLuRaQ0S_Q275sUS0CEFpkF9Nnnxevlclh4xo8ls870FRHMR_BNMHxNrQhTVV9iRESdcSEsH6bgS4qEVD7-eGohRG6lMRZK6AQxGJkyk6HSZWwAxxUxMoU8fgtAyhmQZ84xlUZh6_6Ozstirur84U81hW1c-stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=fmmVUU4nLRZJ4onKjtzu-In13vX25Wn9eYQ68VRKcuPMaL5xIyKYm0ri52-TS3Fbsij6HqmTU-eH39pem0ViQIpTSIifMUmVou0UjzKpV6_tDQMDDvXU1enMHwxv5OdTYZpR3tj7W4-1ala0LtqQNp8ImhkvMmtjXTgmEHedHK772JeqBKeWcyeFLuRaQ0S_Q275sUS0CEFpkF9Nnnxevlclh4xo8ls870FRHMR_BNMHxNrQhTVV9iRESdcSEsH6bgS4qEVD7-eGohRG6lMRZK6AQxGJkyk6HSZWwAxxUxMoU8fgtAyhmQZ84xlUZh6_6Ozstirur84U81hW1c-stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=hUvETsswZt8_ZxNOI-lOKAFZroPMi9trdWgHaGBHw-SbjkvRtOS5c7pmDhv-y0K33kFUaXbYXImriTtGMRbURd6ymTHs-JVHPFNz6M6KePIR1Amf9gcTPPZ34TMinSkqagxivK8IuPdv8hsTOZ4s5Th5cVXwLGwzfsX0RhZt-vGgmdcxfj5iVAIRrQtpM0zpWFwyUJvmvQO7qNEG6fJY7HyNo9mg6YGDSYTRDJe8ci-0_L9d63sFGM95YT71_Hki8uByyVgUJYhJpMkrj3glneLJD2OHgtBAcFnDH8QFT03a1nO6YDT9PU_f9cIiVgYfRl96kJNDxZ9GRw0hWJHA4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=hUvETsswZt8_ZxNOI-lOKAFZroPMi9trdWgHaGBHw-SbjkvRtOS5c7pmDhv-y0K33kFUaXbYXImriTtGMRbURd6ymTHs-JVHPFNz6M6KePIR1Amf9gcTPPZ34TMinSkqagxivK8IuPdv8hsTOZ4s5Th5cVXwLGwzfsX0RhZt-vGgmdcxfj5iVAIRrQtpM0zpWFwyUJvmvQO7qNEG6fJY7HyNo9mg6YGDSYTRDJe8ci-0_L9d63sFGM95YT71_Hki8uByyVgUJYhJpMkrj3glneLJD2OHgtBAcFnDH8QFT03a1nO6YDT9PU_f9cIiVgYfRl96kJNDxZ9GRw0hWJHA4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si8ilpVHtXK_wEhiniugB7qyyh_YV9ZBHgnvX4yiduYb-Vu74O6l9_0XqIAFIsCQVTLiE6XxyqsxWtbDFXdLnN25b2NSMJLGnv4xcgU3g5UKVReBxv_qh318Odf_k-viCqbxXdSd5-Yj5UXTPdcELG4gsBrkCeC7Kzlnvb9mlBpaIbM6qWs7sSN14vpE6DXO76EQvPewskhqKaT-L-86zrEISFTzkqRnX2bQu3xNj1Ad3H0OOxp9tK260VhnS_DZloub0B0lF_LMGODsQEZZEDqgWSyxsxJzsl2cv7vQgc1-huF1xhFkqZ2PcElvRiJsPTVOGspXR4SPJvEBv4kC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhlcD8ca_a5R7AdQ5AieMIwnMffYgX5mMfmqx6onM4Ufe7R3p769uKMXGyamgkcNHhDhLMlQ3HfY2s4Cbn8jP94oz-v1QcoB3ElGsO8hK3sqlJOXQc7eRqUfOrjjY1QL74VggzItzgdkPdeNpiJ59uXpx6Z_p8h26-BgVofZk8nkyiQZpt-yBLPylIRqh0QmpKzmC_axKmKBTnnZS2ptLwQokJld666uwCX40hpbW99npQs_cuRt3AmvBUuvrf5PqfsydwrAnX-Afd4ao70pVf_bfCdA0FiFaH74xI54ifGdK2tj11Z7wJ7x2gTnzO0jPZxwvvw1GjkpBmqztEfhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=dOfLHGneg3EgPIV_LB-1n80nfOvVOQ3AmOZwIyDf6Nabya_2NWn9ObujxEA-3Li_1Bswq3-pU186cUJAgrML_pjhdbjoeVC3uJ_jkXXDL9d8yr2JRAZnMylG6GJYyFd8-_FhKRtuhBE_aBcAe-nmL0KOLG7hXz3N1pwUzhqYx5VOhLalGuodu7AeihFFaQykLF9BXyanKMftRlBNqsfc3pe0avFYA36nxRHr2MaFEcQvBQlqcJEqYuvpYpvccaw9LHBam7YKQqE-RCRs0N2J7IQ6diETKMtHk5013fmzEt5Dm7uImPOrjeKQbD1Yw1UiThxIidU9OIpK1HlQAb0hQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=dOfLHGneg3EgPIV_LB-1n80nfOvVOQ3AmOZwIyDf6Nabya_2NWn9ObujxEA-3Li_1Bswq3-pU186cUJAgrML_pjhdbjoeVC3uJ_jkXXDL9d8yr2JRAZnMylG6GJYyFd8-_FhKRtuhBE_aBcAe-nmL0KOLG7hXz3N1pwUzhqYx5VOhLalGuodu7AeihFFaQykLF9BXyanKMftRlBNqsfc3pe0avFYA36nxRHr2MaFEcQvBQlqcJEqYuvpYpvccaw9LHBam7YKQqE-RCRs0N2J7IQ6diETKMtHk5013fmzEt5Dm7uImPOrjeKQbD1Yw1UiThxIidU9OIpK1HlQAb0hQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeBm6MusQfaDAyA1C0g_vUeuHyYpbfENC1YtAhZVNA4B1iD7PO74N2jcjsRwJ-jzcLpqlVj4FafPoRrlq6sOGq4UHLs5WRD_ZiQ5-KNe357Rs3dslO8muKqmxPyhDHiNX3M_ZSMPlrjTYGDzXqKFjyF3dpS73bJuzKuzYnLwzduBYqGFpnIyNFFbyfLDsdDGPHZ_hL3T65FB8Ex3n2Acpjn7LUzhgbcL1g4umm--IPdlK1skyF2m_IlW3zV6Kua5238wWj1lsNt49G1SeRMsq_2dYnVqUM107r9i-_JZJyeTez_ySb0BPJaKxxLMbOZK8FwCoT9ZnE1SEC8MeGextw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xxsv3qBDB6f-zohsaJfUGpAMpeuyTaQZ5vayLS2gBscyDXFoD0X8IkEiZxU4KRJCfgsdlpqHZxRhA8OX6iZJhm2hyRQMQKkihVBoVk2SJsBkHuveWt0LLU5F-Qcj1Hf4vgshSuRM-uQgd9lyzHNCNDWbb5KkKbRQW5-UAPoUtUkIX3EwDHVD4-SP-oy7BI7qAuzyzhiDx2AQ2KIbY8VGJ5TBWeyxHCn0gxsYIuTBnjtK-xuIsR2pdoX-JFrQ8oUwhU3c5yWBtik57gcbOfSkljM24e3B6sRrtDZYWqVNDRH9WegcgR12Hm5Cds5LHcVz5zcXlPunUJYJ2lkLLXDZmw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=XHvaJrx23Dk4xYOtTm4OzZOQSOUXiz1RDB42TSajUe7y01qAURtH9pp3qnR-Da2-0vtuAp8RxoH9VuY4kiBiho1xcqaeNZprmh-eJch68PU9As-Od8cS3M5R-3xq4gYbHiwylBtpP2P0wrIxNfHmKrL4Z09PJQIrOwov7LTFmGUUGCvoVeDzGXL_zQMrmHrLb1A5LqKbokt-IWCZD6L0PcENqwax09rrgChR7HcQ171YqVEmTiwXS7iToOoL_gKgApi9637QlESXGTA2kZRpsESSInVmjtXp0BuwVmOJ62nPfGL_jiwKtvd9BbIQdUGoYVpsKyGHWl6DxGQraGw4sYQdNekJZUHWj3RTr2uzL3UAvce1Fu9kEzzORUWzLfS7eW8tsEkwtLDPWXpsF7_ImLWJTBSpwETMorHpSbUGd1zF9UTza0-CJuUKfPkHbHBCXWFfaPu-n-wEPjNZodM8ODolodjwTmbScKMCokyDHNeikkOoRULYShvsislYQt1XpfUYGbGpcP5dWh1Gz2AftNbi-8rsScVnhje5P0mu-N8OhInfeGDhryIGb7T7GM-qws8qLN7tObilA8h5Q3VcucdX_e3U-lOfLmqs58s76a3xrjyX0KREjFRZ7BQh771rnf6_0VRgs3H81gZLN_q1enLm-xFoDH9vPPUq6I2rhfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=XHvaJrx23Dk4xYOtTm4OzZOQSOUXiz1RDB42TSajUe7y01qAURtH9pp3qnR-Da2-0vtuAp8RxoH9VuY4kiBiho1xcqaeNZprmh-eJch68PU9As-Od8cS3M5R-3xq4gYbHiwylBtpP2P0wrIxNfHmKrL4Z09PJQIrOwov7LTFmGUUGCvoVeDzGXL_zQMrmHrLb1A5LqKbokt-IWCZD6L0PcENqwax09rrgChR7HcQ171YqVEmTiwXS7iToOoL_gKgApi9637QlESXGTA2kZRpsESSInVmjtXp0BuwVmOJ62nPfGL_jiwKtvd9BbIQdUGoYVpsKyGHWl6DxGQraGw4sYQdNekJZUHWj3RTr2uzL3UAvce1Fu9kEzzORUWzLfS7eW8tsEkwtLDPWXpsF7_ImLWJTBSpwETMorHpSbUGd1zF9UTza0-CJuUKfPkHbHBCXWFfaPu-n-wEPjNZodM8ODolodjwTmbScKMCokyDHNeikkOoRULYShvsislYQt1XpfUYGbGpcP5dWh1Gz2AftNbi-8rsScVnhje5P0mu-N8OhInfeGDhryIGb7T7GM-qws8qLN7tObilA8h5Q3VcucdX_e3U-lOfLmqs58s76a3xrjyX0KREjFRZ7BQh771rnf6_0VRgs3H81gZLN_q1enLm-xFoDH9vPPUq6I2rhfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETpeEmM8SyIP4F4l86u2X7n6gUllWkdCxWVAFIhTUeynT3b9-7jMRJFabZKdmFWvtkoxnTAB66xU6TUjFD4DCJ_ingPvgcrLoWpTXIYk5ELrinc3w7ojisR0HfXrt0IxGzYPTBwGcm5rk7LmlH5zNXez-9GnVlJcgf65pfdeM8715DeOdE_Yv7-DczRiqCyGOXNe8WJYZmdF7nberJJS2cEOo8aUKEoxYNd8TREpJwv9GJMp7abb57cErTFgFW65WLhLs15iYqBV8Bcm1Sjutes4_6C7131wCrF-ejqqBgq1VWgKV-hDnZTqPk389Wm68chjc0jLyMDJ5WgkM_pQqWtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETpeEmM8SyIP4F4l86u2X7n6gUllWkdCxWVAFIhTUeynT3b9-7jMRJFabZKdmFWvtkoxnTAB66xU6TUjFD4DCJ_ingPvgcrLoWpTXIYk5ELrinc3w7ojisR0HfXrt0IxGzYPTBwGcm5rk7LmlH5zNXez-9GnVlJcgf65pfdeM8715DeOdE_Yv7-DczRiqCyGOXNe8WJYZmdF7nberJJS2cEOo8aUKEoxYNd8TREpJwv9GJMp7abb57cErTFgFW65WLhLs15iYqBV8Bcm1Sjutes4_6C7131wCrF-ejqqBgq1VWgKV-hDnZTqPk389Wm68chjc0jLyMDJ5WgkM_pQqWtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=TWfJwSq0nPJL8LipN93z5SxaO7nsI3vxS0nCVtwOx73qrrWYjEZ3llswGoq-OOEXAbRgmfWz58Zq5xM5t5fwO5caF6o32FEhUAPXhDEcUfsMIEJ4iY_WWFCzQ2w0bVuoHmdMUBPx_Dzb3nhT2hQuaqXpX_aRK9_YEi_HjghvFqWwJeHAh3nAalqmAuQXEECOgifT7htJLprBMZnWiX5dgtTd1jTUbCGIn4jJuh-jtfOu1sG0wzmpPlsw-o3vLjmFmiN0NXJdoMgBt33rv94-2a5IwwnGF6cI8LzAcD9WMf3fA7YTeaJIjNsHPY_t1ealxYVSrAOWuNS9hwdmPtbNAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=TWfJwSq0nPJL8LipN93z5SxaO7nsI3vxS0nCVtwOx73qrrWYjEZ3llswGoq-OOEXAbRgmfWz58Zq5xM5t5fwO5caF6o32FEhUAPXhDEcUfsMIEJ4iY_WWFCzQ2w0bVuoHmdMUBPx_Dzb3nhT2hQuaqXpX_aRK9_YEi_HjghvFqWwJeHAh3nAalqmAuQXEECOgifT7htJLprBMZnWiX5dgtTd1jTUbCGIn4jJuh-jtfOu1sG0wzmpPlsw-o3vLjmFmiN0NXJdoMgBt33rv94-2a5IwwnGF6cI8LzAcD9WMf3fA7YTeaJIjNsHPY_t1ealxYVSrAOWuNS9hwdmPtbNAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=tNlZBkng1XKx6bNQyOjf1Mc8nJptInNwxYhJQIGVi5Yyy82eLOxauRcM7xLjsRA8e0kVHkuW136IN9vA1QXpGj_yOuId7GlcC4K8_hn1rQuZtwLjmg3pRowsGm3YaFFIyILkiTYWsMF7nFp7CR-5XXMdvBUG-krHR5zZr0ufr423RU3Yk95paebACm_aTYVHG8BEOEPVOTbc2fLFzDgf7L28r6BwpBBQHWycZR70Fxg8pJOkN89OmHh0pWhoiAuKDaDqq-NdplzLviVSji9om4nKCLLO5aVE6_r4dp84MM9GdGm5CVTQzRqocXkaBUK7R4g2Eng-3wwr3HYUqY6ZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=tNlZBkng1XKx6bNQyOjf1Mc8nJptInNwxYhJQIGVi5Yyy82eLOxauRcM7xLjsRA8e0kVHkuW136IN9vA1QXpGj_yOuId7GlcC4K8_hn1rQuZtwLjmg3pRowsGm3YaFFIyILkiTYWsMF7nFp7CR-5XXMdvBUG-krHR5zZr0ufr423RU3Yk95paebACm_aTYVHG8BEOEPVOTbc2fLFzDgf7L28r6BwpBBQHWycZR70Fxg8pJOkN89OmHh0pWhoiAuKDaDqq-NdplzLviVSji9om4nKCLLO5aVE6_r4dp84MM9GdGm5CVTQzRqocXkaBUK7R4g2Eng-3wwr3HYUqY6ZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCGlAVZ6a3fmgIQflUmfYQNoLjOUb3BYi40VZCVQHPYqyv69EMZQxzdNyP0PygDkzg7ME-pVWLMHZn9DeThFdpcgHd5jxvCCWT5qmzh609ymBrWxpbMkQ8MjuWzjxihDslphuDWLXKMr_fYZcDtaEBIfsWC10XmcxozvtkpxWySt1JDLJpkxgfEYtflAhCyh1h1y9RwlKcF8ZdHTFEnEsmmC6EjqQHFDS1-Lmv7fqrsNgDPD1SQUpC_fQYAwRDS9IESklXTGn0LP45K0NxQU2Opz95rD-y_EA2ikFSuxmO2gzjsSQb5zYpB9h2PNbkx7jFSg8xUA9eeBFTmZNFAdPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruUYD_dJXMUNp41ZSDctmWFR9bSUnfL6sjHQI8D04oeZh8WgFRkPgh7eodksVKGEFS-GDget5rxJNBCvuOIqdPqOTSB9NNLHiRh2Q3fNUL5H_YT0KIQ_Tunw21HEutc6tAlYXssVLfKQqQBGu5r5kqJSdgf_ElypuIlLrTUwNui1i_W9Btx8PAqhXmrmU-glh7Ioj1XFpKVdaKoD2mwYJXPxDw-rNSs20rSKsYeEQU0TaCNEZfq-9JCGCNCrw8NQdIl-iyD5ZiJyAbG0uuB3WbqTV_KykPJUbDIxzuy-UHaDcSI_ud2W7ElnW0ZXxQCdieW27T2iBiP5xWocakrlLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv89KusZo4DPhCuqV-ncmhUCnF7D38cE0y1ywxo1FuZ4BfVu4DrV91jvK8owNC8Ez7qtcj_p-6XI5E0QAxmMFbGkcHeyk5sbQ8eI6thP6B2jFuBROdgevEAeCcskqqlZHb-eVhiricInnEtDXRDoa398puxuLlE8O8CLb2jSLYx17Idqt0Ijp3KuNRMiVRByNhvnmSy95k_Fs-LjI9QrZTsZNjVAgwzy-xZbYUfSqoTslRKtaggNPuGsdRtGaTu5EZkJpvvWEVMbO5U3PHSrtUiaax6TjlKZMYCiWwXJb6IZ838v9VUUCE7e6PXUCHkb2T-GMNK3dxl8ztOHKwOJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMQBdci_VjfLry6gRYtj-lVHPHj2PKH3_JbrXX535fBgY0_ddeFyAp70fIZRIY7GHCfcYcGZZBAiIM8ufh2luhwbd1-Am2LHzpk1injJ68q0aP6R6wG-6XSJ8AvPNXIJbmckbK8SR0R821txSP59VfXv9_VDsp-ZgW53gvY59YQn-9xdya6UcrnCUI-FBCrFAgtBArfb9IMz0sPxo4-z_QAqA_aSssJZaT78Lo4PY9cztuhnI2dAdbicOTmV_VcyCyBfWxGzDVY6ww-0S3VtPT2poPiUUHCK8r8r-1m40SdnP_p56qVKthKdXX85u5ClFnlwcRdrEmRqKG2Ii5mG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibAlvna94nxYC0a4K7zSiXXTBZ8AgdkQUNiIqHvHrsOoFw-XaEGT7ZPOVrelNFW1-VzgKkhopwjlkyB-FhUHRcRKYat2TkRipEapT0B3KzACoS9nAarfbxaCLHIvkDMIDshPAveOUr7ZxaNRyGeZfcY_qfxiN8camvXa4zGSVakgqjgBbnhMlxy_1iJfGI2EhkNl3P3O5epHpDstBB7ftuMT8SmEnzUmK3JLmjFuaJFNf1_MXDpTUcoXqErQ5_SvF6FvizGmROD36KDVFfmpUbfco9VkUnwHE74mheEsvnzSNccEQjCszT-AXlnlDOeByrQyWPoyCHj-6Sk3XO3M4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Q3tim6vvN0DFBruJszhPZT1y9HK3QGuZm4hPCFAczlHr0wGqtPaCBuGrm2qFtFWtWf9GllArbrtU9HwZ83myM3GLo7CuHPdWI4bwjbDLcENSxgTOD-8KwTTD0Hy7nQq2yIL14hU8QvZfgD3Pji_FaC8AfoydC9-M2phuf5aQTkMBM153zKuIR5BfAqN0YojYByOt_ygpi661x_iSXLUbH-DU-VnfzPmnKuiCjAc7oWaTlmXGKs7RgGpNGzo05H5No9Y08yrnjq-ilzVvzkaKwJrTWvhsesggRK0b7A5NFvCv82lY3oI3uB_nXjG4BmJCp0sy7mv25zW_fs3h6wZyjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Q3tim6vvN0DFBruJszhPZT1y9HK3QGuZm4hPCFAczlHr0wGqtPaCBuGrm2qFtFWtWf9GllArbrtU9HwZ83myM3GLo7CuHPdWI4bwjbDLcENSxgTOD-8KwTTD0Hy7nQq2yIL14hU8QvZfgD3Pji_FaC8AfoydC9-M2phuf5aQTkMBM153zKuIR5BfAqN0YojYByOt_ygpi661x_iSXLUbH-DU-VnfzPmnKuiCjAc7oWaTlmXGKs7RgGpNGzo05H5No9Y08yrnjq-ilzVvzkaKwJrTWvhsesggRK0b7A5NFvCv82lY3oI3uB_nXjG4BmJCp0sy7mv25zW_fs3h6wZyjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=vDKh4em8ExPbfogRB4PhTllVVLaEigyGU3yjNcSP365G_FZK2H0LpelHbe3Ur3OF43UfC-5qMgly03IxedFdlDwg7VMH3_Ah8hlg66y9G_ShfAhkkeHanP3z7di4yKl17KezyCVA_b5AJkwjM4cbXN7JowNZBnr2IKIclcMQVXUOeNff_EmQBB0IiuPfEH83PQsNOa2p0s5XYMM-6KrBTZJWFaN4lyiZHb8Jf4Ho741bTri49ALBeqD0Fi9EqR3wVeN6RT1hsxmvFnMAfZRmpjc932rSPinWgMwngEfgCRaDu8vGkWfjQeuC49-T19gLU9VWkS5pKr8V4CbPbpOYAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=vDKh4em8ExPbfogRB4PhTllVVLaEigyGU3yjNcSP365G_FZK2H0LpelHbe3Ur3OF43UfC-5qMgly03IxedFdlDwg7VMH3_Ah8hlg66y9G_ShfAhkkeHanP3z7di4yKl17KezyCVA_b5AJkwjM4cbXN7JowNZBnr2IKIclcMQVXUOeNff_EmQBB0IiuPfEH83PQsNOa2p0s5XYMM-6KrBTZJWFaN4lyiZHb8Jf4Ho741bTri49ALBeqD0Fi9EqR3wVeN6RT1hsxmvFnMAfZRmpjc932rSPinWgMwngEfgCRaDu8vGkWfjQeuC49-T19gLU9VWkS5pKr8V4CbPbpOYAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1t5hoqEC4JaS8OTTTylWpBz3K7Ykcil0aHKxI41DwFTTb8EsLAaCrYmmySbVq-Mr1w0NpGFnv2jHQAzL-E3UAfdlobD__zjDgmUyzUnQCq9KFh-5BJgsoYC_UZCuJroxC7x1Pa8_kEpMcgJm_DlX7vpheVTlbpcbEPOOYt0aAs1e2O4WP285bQ3avYE77p_QKh9zablqqVck7FhjZgB5sGnGKRvVaw823mLw7CIwZaeHpsmtEmartBbHfOU_b1JoZCs04zZjYgxXNNdBkZPaRzbUu42UIkQ8lZTWY42kuRkfLIhmeufiOf3JyoZParzFUJk2vzPUfIXeFwq99Vdlg.jpg" alt="photo" loading="lazy"/></div>
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
