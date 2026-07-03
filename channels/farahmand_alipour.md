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
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 09:52:45</div>
<hr>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXdR7AcjzRjBEfZwmQItLC1crIx3hIJQtf_d9Ep1IBhn-OmMWNL7xmF5fdC44V6vc2jqlBdLFqslP6365ZUTsOfTPD2zNNg9dhlVr2_DldgqmvYysI-CJrNiY82wHvHh7MRFPQVoAzcexj0r1Qi4W4RtuDf5LosyK2HhN6VJTVTqN4WEO5-t0YZlZmdKv_XdyPYp8KDxZDOGJ710nKMxHMP9Ba27kP4atgaqjgW3BW5wJRRxzwEnOu2Qy2EeFe9DxGGErz8wtK8-OVfUEWFDt08RQiOI512acm3uJqxIDp71fg8lZFJo1i7BYX_qQHTwEBrLRCt_K4-CfAxeaW5pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFR9mP27XuuGctu-j9UIthXRXcR2HkauBcp1vLGDZucKGnJvm6eCgYqeLOvCJYxlxP_FsBBPQArNZnG5bWZDEwg8-oRrf-Vs395QhuFLe4n0xgtcckZPJNY5zaXOh57Dn2kPUElOb_GIltlAf_xxkne8VsmO5yH0tHkbhceyuXQVw48OkPF6o13-oWWgXwHuGqHV_kMRmdG_2cieuC8UaZz-wOvzGoDrem8KfCz2jRHSP2VrOUFiX6qglWYIWeM0Iu44DJe1d3irDKrX5zLqC4gT-lw5sJi9TyfIXlCj8YcxMBdPEm4W35CEv8IZAj0QYitzECSm04Z6x6YqyGioJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYSlidjSFGizuNxf7akejcFa-W0V3nxfwB2eUuasb1PzDVKm0REuO1QswdLgrZ4WyJV93uCy9_BZpeXJ-KEUYHDlX1b-9z7fZsAG2ydDh8z4RuMEgvzHWtqlhFOA9VrxDnu_5UYxLANrAAMNGawKNtqU4TjMISXHHNav543K7N4L01Y_MaezrDdVVXcZRU2YQtIddfM9WrdazZWIOSQCCqda5ucIkrYtJolCCDPEoYH7b0kMEvRE_7G6_4OxaMWA1ga4wICJlt4ERIUinY75EczzXSj5N7NNnHfwjJue1jvnSR05_ZdA28_T9idA13qdvgyflc3HR_lQKUVqdP-x2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxbQzXGl1WrvlN9I1lmnND2NVF945lmXSD8zphNG79RXXIsZ82X5Iugs0692acWqBXfB6u7Rj82YgnNyijd1KQ2hAhhc5wZANS_qyBB9d_2iTpz9tmQD0gAXQcsCP3WY8Z1xloET6OosZziCYCUgQH93Jxz4q_5YzWzrZfB5UVjMMiBjkHPDraHMngf-3mtEYLQ3MP8Ysajo2BR1KqfaA00qokDrdaLRwRyACaELmwVUpmXg0e3zBG7E5AvDzKftNByph9k6dD4NbNlKM6ABkE9XD4ccs0vXxocoD0zsWzrH2d-MReZQ66Yrf00Yv9v1UNLKuuNWZcHQVcnpV_B3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJRkbhs9IbWoRZovuIbAdCL8RXSrfv_LsUrHECXlOyAb2uyCnEEv9ImGnUkRyGmvAC06Z2YVpGx7izQ-p_b2WD9xm-bTyR5IzbJa30aWfPj3lmO4UruESejP3oMsOJpBG7NLchPSl77nDA5NmHdAG5jEjqbm4o8iZQyOB8lfip-ciniSz7YpCk9ZbLMGfjSmj_rW69BB-5xaFhnYeIyVHfGFt8KxkjcULSzASE3rL-HTEk3EI1vda8CAZRClwHoNtnY5UOogMYIUFLiFLHvjQw7AKDT1iD_I28FYmfPpNWm07UmLfMN-GmjQr4YYQyUOtDqs0B-TrusDlkbR-DeOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYpS2AGyOFJVNJHDIntWcTTBzu3PdjdY18dppzEwL1jCxfGZv6syisx77E5hiMHQEPYnJtUTSN9gZXYvTd177TsveVJqvA0LGWivRTQChf1q5mzc4OG542pY63Y5_CSOZgNYufdzZz-B3Yd_U8TlsXDG9NEsdRvjAQnl97Cgtu2iWJI-GYu-Fbcn96_Ol_EWdmmJwESqGPryWonkVcZphsPFW_ju0RB1ZI5L3FWhEzAHL0zhw5psoQPDc1xzjYkbeyqPUNtH2cw3TGnubrI2qyZJVsAmo5TIr4H1iisaf-1ECwLlTi1o6uFduvMAV5l3KqysaEt2kONB3pF3l_-EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6p8jGj_erqIzymuNNH7CqkXx7WFj5Q67dTmM0GBCBTeKO2JR06nEfkRn9O--Fj-ljU-O-lSSsZBWprk3mezHBDePIVi6ZjUF3FZURIId_wEl9OlAYkOpwlELJFhxj4DgcLBTxFZrFoOlFTdV4VSGqmuYJ0tj1Wx54wQ-ALKBxgXghOtmRcN-gvflFwaXBQRoihdZHMEZEEmZVsOiI8TqnmgyXs_L89XSsfht6uupp8xnV-1Iw5xVqdMeBTBmYb6za4XWJr5VUiSDnX9nfo4nHs82iiRl17m8SqKxXsUqbeAqTY3PETy5hS2adcg-GXXnROgf4GmPAdS_AWJqIHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZKiyY-aTp0qDEKrp6Yrrqa54CWEEkg5V7dIZrjj1SRcHW-wGLJ9xc9Nz3dP3nVQw9r3RH68-cRAaIg-ffBOPlUwaftTKPrTf0r3o5KurJrpTOCc4LOBslM5TKEz7XbKDZJv1FeI4oaTTf5JfLNDGtQ-XjMI5g7VmBjOsI37QepOpewMYYgfwIz6HdwIasc8nyqHBHrypuSS7IbalJdUWBwmI2Dd18MMGr5Vvb1q6k_SsGw5-wGuEXJT0OA131dZ1haGl7dyMrFf-eh37JwXLCOEE-ddBazRIvzf99d0X0D3ims1q_VAJDVh7SMPfrmr5xJmXe9DDHHhaivLJNYdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJyICSScG8w5gh4zHFUwgeBMPU78Ocf3sPu_Oy7a8kmg8xJq_CVlElx0QDixCzfbNFcCHHRKMJeWxK7-Ptinzu0Z2PRp4NxiOhZj_BSQT3nrRxm3BmiD2Vj8liPfNH8SrTExP_t-muWmu05ULgg2aoXohpu69PLaN7x0A6Katy8_aaiEEVtoMMksasWxOp42smVKf23pScPC9Nj_jUr8veXI3ed010P1PZcn-4oahzw_A6PVdXi3bhiKbx-vvqpWhrQer58M_uV21OI99eedtM3x_Qwz-6mVoF3hSep2OWpM31ovvP33L3NPhPcNTgvZj83-vsb62VPnGxtpWbCgiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtohJesNZbSJmgFGg6BfdC2n4_8K8nNkEX_hgtwNsihYrqRbio9pkVAiC5zX-fNZJB6hC2vrooeuXqAFd9L8M8qt3mimgp-llY3SKQ_gUNOySYYAFEIcAyIqRp5zOkurtHiCnzLrq7erwAb41Kd_v-kyLSXTalerTCZ8lTyNEYuIkYTt6Nv_LOKZu8S_PV8KD6WUspY3yTLdP0gMx48LVXAGs1R-yRX3hnlN4Ey1Pi17aGlfGpCV8DHAW1fhGVXWvL4yhm_s-q9Bo022yCFvmJQAUvNNUw7yB-5rdVxHucLu5WcSQ6HW2XUlQGr0YHsT-CU8DZ4Jqws2Mkggb_pSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRhhhfSSrJP_3qmO2UhisCnLMO2MkOGP2n9hBLXcC6o_Q15DqsRzNcVvgPw6AdSY57fNRHL4B5s8W5kmkr2XklAEcHQ7VBFHZIXbhFTE-w30j8Yg9fSiF9HTx83BMw8FhhG3nF-cheN8oJ7MiKWBXJqInxFxbBF5qfajVpto_xnTIx3osLekVUgcye-LXL5ejcwszUTALmYwwhBWwcaZGabJdJg1uOxt_bzvTdod4XTRg8gyqTe2CvzLgfbq54CInAgIvYLA09WFl17dDrxyQJt8ZFb8xpv5b80iDyz7lAW4Cq9HhHPX7hndzjdvm0Yfwbx1StX1uVHZaXEEnEmpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK7oDUDR0Lg57fvSypTz4XtISIJZ7giIkFSvZCNXulBSgefQUmLBiq462Mvo4gyy5apAeRk1BAbAQHOlTs85y5sYwnV1YjtWFS8XDvpMy0WyulwZZ3KGUHYSUWD9ii7tFyjyfYBJ79xtUlO758sA99zX2xms1L_922SCaxIQxB5xb16oliO0sj2EdMVJILnCEpmgxmmnuG3OaWkjNIuF4W7s99NE82RooNum-pnJUpB6YSrgAdeftwQXG78Z3T9yVpvekm74ihYsq2jVTM_uJprvFb3-ca8P22bnkmotbTFR9R0lc_j6WAuHAn1jCBxheDFxnx5ACcreWxWyDuCong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=vo2cWCLGWze_0yzQ-c1vqvxuyGdiKo0m8TJJKK35iP53QbmzEWpEE8A0uwvbervS2K6byysUSczZc2f25RwMq16qzbn8312avPhj7du6rKDICFTBOdGSv9j3YeWJJznoRXUHgjqb7muDbwYt3qycXnusVaQ7eNjsimIUV67fLFwHdoY5qhBY8wZEJfw_H3ET4Tvv1oe_LubYqZXg5gSvilqRKGQsgN3YSqmoWaiX-cK6A830qYWWb3LqmMKU7cpv1q7ivL3bXw4KdGIdph8azBTTRC4gdB-pCpEfTETiiz95yEYg8vF1U85SahCDP4FUsC8GZhGZd4k3lQ_e26P9-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=vo2cWCLGWze_0yzQ-c1vqvxuyGdiKo0m8TJJKK35iP53QbmzEWpEE8A0uwvbervS2K6byysUSczZc2f25RwMq16qzbn8312avPhj7du6rKDICFTBOdGSv9j3YeWJJznoRXUHgjqb7muDbwYt3qycXnusVaQ7eNjsimIUV67fLFwHdoY5qhBY8wZEJfw_H3ET4Tvv1oe_LubYqZXg5gSvilqRKGQsgN3YSqmoWaiX-cK6A830qYWWb3LqmMKU7cpv1q7ivL3bXw4KdGIdph8azBTTRC4gdB-pCpEfTETiiz95yEYg8vF1U85SahCDP4FUsC8GZhGZd4k3lQ_e26P9-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=G_7XG9h4y5U2KTjua_3BDPpeeUcznrPCzHYSLhh8psuhXPLOGhavqe7dDJ9l4bNItGbEP4vndeqbDPe63lXgVV1JH37zmYUvGVZyVXGvz6WgIZJVhSB8RIwg_ibhj1rWd3XJ3o7spZnUEwQ7Z4DBlFKAdtF5at-S7INAb8m5ERhyiefguVN_RNldnVYB6gIUAWDLei_4ENL-Q3eEQeWfE36ybmdl8Y4IFFEQSuCvTbOo7ZWOxk-3j9lSDMwPQgsWBFoXRPcDznnQHMKeAtlcAE4UTXOLakIUEQ8bZ_RIxx3h-bN6l2tW8JOtNHgzCmE34PGEGKrvTVa6VGcWT9u9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=G_7XG9h4y5U2KTjua_3BDPpeeUcznrPCzHYSLhh8psuhXPLOGhavqe7dDJ9l4bNItGbEP4vndeqbDPe63lXgVV1JH37zmYUvGVZyVXGvz6WgIZJVhSB8RIwg_ibhj1rWd3XJ3o7spZnUEwQ7Z4DBlFKAdtF5at-S7INAb8m5ERhyiefguVN_RNldnVYB6gIUAWDLei_4ENL-Q3eEQeWfE36ybmdl8Y4IFFEQSuCvTbOo7ZWOxk-3j9lSDMwPQgsWBFoXRPcDznnQHMKeAtlcAE4UTXOLakIUEQ8bZ_RIxx3h-bN6l2tW8JOtNHgzCmE34PGEGKrvTVa6VGcWT9u9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=pqXibCrHIjKt4qcWJRLQecNeX5dD-q_L6Vk1h7ChMI6zHJNgqQl2s-JR0hdTfsPvpliyi9CgFax3HnKTk7gJPCmh3jyco-VpRoOn_KfAzO1VOtlg3o9gWQjY1w-QIlJUtwJWVSTrhlulNBmZgWUaGA2zVS_tqq5DtUfdGdUwql6jk9l1asAivhH2RMyRQFQb3Y5g-F4TE0rMrbUuA-oR8zrS9ldHZi8x_QKnooZixIKdsx35Km3UXc7F8Ww84xmh5MFFSH6poUDqJQcupcCg80GrL9PwhaQVHDdneV6LILeMQ_x0_75m_usPLs08IvG57Lzza5-eWcwhJfy5LiXpDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=pqXibCrHIjKt4qcWJRLQecNeX5dD-q_L6Vk1h7ChMI6zHJNgqQl2s-JR0hdTfsPvpliyi9CgFax3HnKTk7gJPCmh3jyco-VpRoOn_KfAzO1VOtlg3o9gWQjY1w-QIlJUtwJWVSTrhlulNBmZgWUaGA2zVS_tqq5DtUfdGdUwql6jk9l1asAivhH2RMyRQFQb3Y5g-F4TE0rMrbUuA-oR8zrS9ldHZi8x_QKnooZixIKdsx35Km3UXc7F8Ww84xmh5MFFSH6poUDqJQcupcCg80GrL9PwhaQVHDdneV6LILeMQ_x0_75m_usPLs08IvG57Lzza5-eWcwhJfy5LiXpDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mnQMK9jSjQ_emvUlD1PpTa_nYeNiPPCGkOuh8r_cpep_yMAq2k1NC8fYbQT9o6KbrU8AgOxgnPKn0-8lJEB32bAsG-m-xblhACYd5ELFByJfwyb8fBUxeVWeUEeGRHWPcFdIUV4a9Exgz5WdNq66YHECbESLWZND12hqfrByTigHRJVUjivKF8HzgdGqe-K6xEQHjoikOvTG6o7w8T4WljQnWVIqBKgIUvhE0lwrIzGNCOUH10oUkYTaQQicxITdR2Xl1fqXlHQxUWt-a9nOtWCEouiNpHvBNUXONNSJJNJSJvuRqsKpPojqXmMCV62dZbWVH2JvKmvFCbzWirBATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mnQMK9jSjQ_emvUlD1PpTa_nYeNiPPCGkOuh8r_cpep_yMAq2k1NC8fYbQT9o6KbrU8AgOxgnPKn0-8lJEB32bAsG-m-xblhACYd5ELFByJfwyb8fBUxeVWeUEeGRHWPcFdIUV4a9Exgz5WdNq66YHECbESLWZND12hqfrByTigHRJVUjivKF8HzgdGqe-K6xEQHjoikOvTG6o7w8T4WljQnWVIqBKgIUvhE0lwrIzGNCOUH10oUkYTaQQicxITdR2Xl1fqXlHQxUWt-a9nOtWCEouiNpHvBNUXONNSJJNJSJvuRqsKpPojqXmMCV62dZbWVH2JvKmvFCbzWirBATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=N96kUyD9cpcwfkMeeaGGjCJzZItu0DJeRkre4grFejTEshTW0uJKxu2V7T9eyEpo4nCAbXE4noOzYFxF5Y-eFkEu69QZMyzlEyCdlYo7tRlnmoeAGYGsokXKsgvqiFtQjnaLNcwqFO7grF1igmbOrS1xsggVECa4Z3png6qzTc0VzDBGffyKAAc2yhwkH0-XFiivs7P0xMv3QNhl1T5TBLLNtvaRM2EBr8JMEwdX4CB2BDxCswNUCXGR6JQeigNJV1AYvN-oUGnALjvH9oKdxpbah4iKV4O6N5vWbJgNSGAILs-Ww6ZXG3DAYZAfT0khP0O2FqAHijs1WiwkTrMbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=N96kUyD9cpcwfkMeeaGGjCJzZItu0DJeRkre4grFejTEshTW0uJKxu2V7T9eyEpo4nCAbXE4noOzYFxF5Y-eFkEu69QZMyzlEyCdlYo7tRlnmoeAGYGsokXKsgvqiFtQjnaLNcwqFO7grF1igmbOrS1xsggVECa4Z3png6qzTc0VzDBGffyKAAc2yhwkH0-XFiivs7P0xMv3QNhl1T5TBLLNtvaRM2EBr8JMEwdX4CB2BDxCswNUCXGR6JQeigNJV1AYvN-oUGnALjvH9oKdxpbah4iKV4O6N5vWbJgNSGAILs-Ww6ZXG3DAYZAfT0khP0O2FqAHijs1WiwkTrMbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6UUjufEBQDdAxwoKl6I7Ru13QPxrCkhU-lBHyxaHsC350EBZgI5NkwgTZSHxLe94672GM8_DY-MS5S1qdxLXk544wHL6Qdv5h53eo5nwkKsd769-c8OmVBx4eZID9Zj7GlkCb-ecR2f3Rnhyvrg7Obh8G7Xk74Pdb5GU3F8xpdCF4jewGEUJE8gGWiV7OBcrCEKyfGlAOZjDQUbbza3SLfTAayKxtzVYs5roUsahKxW2IOQYi-1DDfQ7CCxLRyGnYz70IPwfK758z3weFVg7ek5GvgDHuKhMGVrySeznaKZuvGMS9HtZteK4vvKh2JW9Gl9qDpjLTS_QYnHSLWJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=vAjQGs7Q0z6EHBl6nUjh-DnmUwR--v5MPThaoOlQ2xDCgwZt9yBq_mI6hT26cd7GTUWxLiFBtFqtzAxFBzKvzzAcqfdJD6eyAWpZMgx5xg48q4UETH_3KYUJpe2bO1SDq-ahX8Gkv0oo909Xki1-i0Z5WNJNNcGU1io4Kp0Vx_nojzQgXRAmNOixZRSj1RaNkMK6QWTFW1LwIab0w_s80JqxWoT-zjcVJsMzR50Vk5KH4WN4vKn0T41COYSjG9OLZy6bOop2yjHi61mixZasDINvynASu1u76p9gXVtVFFguVbYZCnt961vdWUTRZGlei3raXiF2G924U0XX27VTEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=vAjQGs7Q0z6EHBl6nUjh-DnmUwR--v5MPThaoOlQ2xDCgwZt9yBq_mI6hT26cd7GTUWxLiFBtFqtzAxFBzKvzzAcqfdJD6eyAWpZMgx5xg48q4UETH_3KYUJpe2bO1SDq-ahX8Gkv0oo909Xki1-i0Z5WNJNNcGU1io4Kp0Vx_nojzQgXRAmNOixZRSj1RaNkMK6QWTFW1LwIab0w_s80JqxWoT-zjcVJsMzR50Vk5KH4WN4vKn0T41COYSjG9OLZy6bOop2yjHi61mixZasDINvynASu1u76p9gXVtVFFguVbYZCnt961vdWUTRZGlei3raXiF2G924U0XX27VTEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=CtU9QrHvnNXSqTd9cqWAHHZ23iq3bX9rkzYVJ-JdR10ZuvtfE984ocT7TxDxK_MMKpZ5rMXko_Uc4Utc9CLHiiqVWDe4vzk4AZAP6mztUjbV51uLzksbsZ4RT_MWTk4F2frIIUe3jj56ba0I6TaSEgKGu6-AtRc0qR5GD40u4hc6nZwT4NTwTV6M1Ky3v8N8EtsYYA9leB2p9HRhRUR4f4b_kokr9vfl5Mb2c4gGRSYCDea4hHqdIhiDzNLd5qtLKNDc5Lzaf2DWIC8hGn-iTHUH10kcwz-RLF5UerFD32vl1M0n3dDPrCAGQezgRLqOQCojeL7FkT7t_lzapqp8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=CtU9QrHvnNXSqTd9cqWAHHZ23iq3bX9rkzYVJ-JdR10ZuvtfE984ocT7TxDxK_MMKpZ5rMXko_Uc4Utc9CLHiiqVWDe4vzk4AZAP6mztUjbV51uLzksbsZ4RT_MWTk4F2frIIUe3jj56ba0I6TaSEgKGu6-AtRc0qR5GD40u4hc6nZwT4NTwTV6M1Ky3v8N8EtsYYA9leB2p9HRhRUR4f4b_kokr9vfl5Mb2c4gGRSYCDea4hHqdIhiDzNLd5qtLKNDc5Lzaf2DWIC8hGn-iTHUH10kcwz-RLF5UerFD32vl1M0n3dDPrCAGQezgRLqOQCojeL7FkT7t_lzapqp8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=Z9lt5CNCxv6BWkyph3GV-3YX_P_wumLPjvlAuXp8LWUT45oLQyzFOY852P_4XPUqfxkpNfFgsIw2-6WW-UOQgeozTlaXSZSEERRdZ3v7GtkYo6FOCn-j0sFIlirwG-pWVNyArRk3i5QbI3X9PNfi1g7o2aawx8Nw3oqQKJzvOjaSnq-hpGKR9KVMY5i2rWGRi-LrjrtAN4BFLHpaS2fCYYiTWKbH074XuPAy9ZX5vqhpeZbPHkt-ytVH3Xxr7qDYXgFvixGrbDw622yqWVPtvowmZ5qcKQhMoHvdzCPlhCU-wRucXwcpTnAI9ixEYp1oQRxs4ExCnb8FuYzlkSjJG7CpbpXiqAnzvMY9chDzBlBMgt7_neS0GoaOPggif3udOCq00XgmpHwQJQQN2UoKBdG9MrmSTVdh_cI9tPO0Nr4Ut_yPEqJ1dD-IJmcoZVmI26lNRHnMc0O4NAqh13fcX0ZDFdlMC8lCs0zo_bCyrknaVVGbm2Kvvo8FjnMgh1JBuoXt7IEtzWoYjjo50osA65o-pK2NcFUhYQ95Lhxr1qb86_HBfQ6Im5DUaZQW88CuoyX_Ejh92ud2CY0sStSUNi8wZiVhiXAIYDMbc44vjaqGYU9RC-EHHAhUW12Ceda_lFWweaHS0jgmyz4L9J60fHgj_H8KoETNJomWTsSwI9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=Z9lt5CNCxv6BWkyph3GV-3YX_P_wumLPjvlAuXp8LWUT45oLQyzFOY852P_4XPUqfxkpNfFgsIw2-6WW-UOQgeozTlaXSZSEERRdZ3v7GtkYo6FOCn-j0sFIlirwG-pWVNyArRk3i5QbI3X9PNfi1g7o2aawx8Nw3oqQKJzvOjaSnq-hpGKR9KVMY5i2rWGRi-LrjrtAN4BFLHpaS2fCYYiTWKbH074XuPAy9ZX5vqhpeZbPHkt-ytVH3Xxr7qDYXgFvixGrbDw622yqWVPtvowmZ5qcKQhMoHvdzCPlhCU-wRucXwcpTnAI9ixEYp1oQRxs4ExCnb8FuYzlkSjJG7CpbpXiqAnzvMY9chDzBlBMgt7_neS0GoaOPggif3udOCq00XgmpHwQJQQN2UoKBdG9MrmSTVdh_cI9tPO0Nr4Ut_yPEqJ1dD-IJmcoZVmI26lNRHnMc0O4NAqh13fcX0ZDFdlMC8lCs0zo_bCyrknaVVGbm2Kvvo8FjnMgh1JBuoXt7IEtzWoYjjo50osA65o-pK2NcFUhYQ95Lhxr1qb86_HBfQ6Im5DUaZQW88CuoyX_Ejh92ud2CY0sStSUNi8wZiVhiXAIYDMbc44vjaqGYU9RC-EHHAhUW12Ceda_lFWweaHS0jgmyz4L9J60fHgj_H8KoETNJomWTsSwI9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=PUZnnuNkKyQdcEX50I_PWUUsw7C5bGWSBO9rUaSW6iNAt6EyRgYiWSsu8nktTUnCihz8YSAaz3k0XFiPdgjsDb6r5uKMYcF_MuPRbt5ZGyZHRjxe9FWkrVEUBRuHiU4fZ5JJgyBi9GpmwSEbguL3G8qJdq9zba1yTkk3_B-KJFqDkGgJWG6t1-SslurLcBLXWSb5ywhm_EczxoMhwHuZ3qo07v8JfnPVALQTqCH0h3O07AdKYo9MEJSBkCEIwF_DJrk8UeJQa2IKJ1nB1B39VIVsncQE1ygEwU5penYwerETZEIawu9cSMZnHNzZlQhVtY82rWaLSLlJPk855dsUOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=PUZnnuNkKyQdcEX50I_PWUUsw7C5bGWSBO9rUaSW6iNAt6EyRgYiWSsu8nktTUnCihz8YSAaz3k0XFiPdgjsDb6r5uKMYcF_MuPRbt5ZGyZHRjxe9FWkrVEUBRuHiU4fZ5JJgyBi9GpmwSEbguL3G8qJdq9zba1yTkk3_B-KJFqDkGgJWG6t1-SslurLcBLXWSb5ywhm_EczxoMhwHuZ3qo07v8JfnPVALQTqCH0h3O07AdKYo9MEJSBkCEIwF_DJrk8UeJQa2IKJ1nB1B39VIVsncQE1ygEwU5penYwerETZEIawu9cSMZnHNzZlQhVtY82rWaLSLlJPk855dsUOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=aSkjpxonPpf_GjWd2ln0noztYxmHkA5ibf_U7bsxrTrBXmYrw0Nwy9mnfCvbuJTQ_E8izEIw5AucWICDuCtAHLF_r9HLVhmUTBTN9NKUO6oy7cWSnOqk9ZtVGOeUPFGo8Qa3garf7p8WNS-pW0IfZxz_iurAIY4YH1eifutlmXBvDEOhlO-87J53p6hArqpWADXCNqU7GkD2p1_U5wmJooVqUufeWf52qL1KNqu5g5SZCyGhWJLLJkfY8xYnUXHjWnk9ZVUueYgbpJSIIJNBlt000pvwpb8s34t51R5lZjKyfn95F6ioGJvva_YwUVu2dQIpvmSlvHIn6RnLV6thdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=aSkjpxonPpf_GjWd2ln0noztYxmHkA5ibf_U7bsxrTrBXmYrw0Nwy9mnfCvbuJTQ_E8izEIw5AucWICDuCtAHLF_r9HLVhmUTBTN9NKUO6oy7cWSnOqk9ZtVGOeUPFGo8Qa3garf7p8WNS-pW0IfZxz_iurAIY4YH1eifutlmXBvDEOhlO-87J53p6hArqpWADXCNqU7GkD2p1_U5wmJooVqUufeWf52qL1KNqu5g5SZCyGhWJLLJkfY8xYnUXHjWnk9ZVUueYgbpJSIIJNBlt000pvwpb8s34t51R5lZjKyfn95F6ioGJvva_YwUVu2dQIpvmSlvHIn6RnLV6thdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNH-RbriA4t9ZIou6mq94yfUgNQPVuSsx5tnOtaxB6fWBe6_Riv1rKjtXiZDi_7jTJx0-7JaLz61voPNilcveRQb4rZU4TVgZbzMdtZdi6OK5_tprcglK68edVtEE6_c0epEJv3if7dd3eOpxEwaFJr_s5udOVCxPs_XdrZMXD9HhroK1OCRZHwoPAQVWZvw0EYJlX8CNHs7SeVhfbOWXntfo_uddHUdWUPB0tmTKINhdWVwTfGQ4WQVawscglMl8XSyTa06K10lP6Yb5JlXHxz_AfrY1NFiKMrogXxi0TQI6yAI0_w7-TprFwsRUE73RI3wVtFZkqG_ZeZ5txBZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1dk6hQB9vZOL13d1iwS64MyGqHpxSlLHXxDe5g2jDgqGQ0TKosGhx7V0fEsmm5djvV9K_8dVaw-GDdWajBw_ahoDzi2icrVeYakBqEQdb3dmZP8toAQxZSOhwM0wRu_PJ5XUMWTHhGmcflQZbW1JtEkfnbMMfbZFKhUNpOVJQsbIAo7rtERI8G6vd_K9q4ENi1UVQjkLP1Y3fCEP3YW5BVDu9kCYkQtbGOL3FWZhswrZukIJN_1q5YBjDDQdOUrA3es_6Gp0-V9QOet92pLY_8pjKZ26gcmzUJsd2Prweewe8rmYhSlVABTGnO3qACXKQdjQ6D7d-aAzq6GBptvdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=iBHxgbZNOW9U3Ey9lYFE3AMaQLk1IQPq46iop8Kw9EQhOktSXr8BUlLkvxCvB86_t8fNZOBZxFfdw2JJ94dR2vY3gken6kIwuUF4HKCUI-_JYNKVhyUFdLdjICCQrHG4qA4mFRT1CsLU8CVOcyLTiKoVtnAEGnZ0xsbO4-POFLBBHYXSo9Zthj3uWpQl2eVWBP9jPc_JJ73h8fqTeGzZW8Vk5T4mggn1-yaoUJ5WAuwGpKHdbYs1sZtOL0kyceVNAnuSgV3I-weP8uVbdZEvtvXS1ZDXslU_z653iJaKqll7oBuMJCVepyqLrWVRjc1mP1wk428Q8DLb9UbMu8x3by5NXl4p5Bg85sZyEcKNq-oQ5MQsBrh-ojGWpqTCE9JvZ2v4wcvPiXuMOQAFTNmfkzCc_Var7ZA2cHf1MVHWmBOCZGkh39x1RP9MYXRj9qYNYEywWGQ8sPo-IpIBWJQ6S0rSOTsPCTdKSuPk8Mi0iyH5PSIbW3j_jU4jlzszYnAAHLDNAwsePKqwflpgC250gZ2dNkGwWOFqoy96xyFI40FGXL4PcvG5dCmZUGLO_Qw1DSCQlmzPeeG-oW4sGkSnI5avj6ptxpVgXYk1hvSi6A6EDXFNIW8ZJ6DGO49OeT34uiYnGzbeQ6zHXmPhfdfDoCJlAvUqq3t9GkjTd8xEmJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=iBHxgbZNOW9U3Ey9lYFE3AMaQLk1IQPq46iop8Kw9EQhOktSXr8BUlLkvxCvB86_t8fNZOBZxFfdw2JJ94dR2vY3gken6kIwuUF4HKCUI-_JYNKVhyUFdLdjICCQrHG4qA4mFRT1CsLU8CVOcyLTiKoVtnAEGnZ0xsbO4-POFLBBHYXSo9Zthj3uWpQl2eVWBP9jPc_JJ73h8fqTeGzZW8Vk5T4mggn1-yaoUJ5WAuwGpKHdbYs1sZtOL0kyceVNAnuSgV3I-weP8uVbdZEvtvXS1ZDXslU_z653iJaKqll7oBuMJCVepyqLrWVRjc1mP1wk428Q8DLb9UbMu8x3by5NXl4p5Bg85sZyEcKNq-oQ5MQsBrh-ojGWpqTCE9JvZ2v4wcvPiXuMOQAFTNmfkzCc_Var7ZA2cHf1MVHWmBOCZGkh39x1RP9MYXRj9qYNYEywWGQ8sPo-IpIBWJQ6S0rSOTsPCTdKSuPk8Mi0iyH5PSIbW3j_jU4jlzszYnAAHLDNAwsePKqwflpgC250gZ2dNkGwWOFqoy96xyFI40FGXL4PcvG5dCmZUGLO_Qw1DSCQlmzPeeG-oW4sGkSnI5avj6ptxpVgXYk1hvSi6A6EDXFNIW8ZJ6DGO49OeT34uiYnGzbeQ6zHXmPhfdfDoCJlAvUqq3t9GkjTd8xEmJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0JZOTqlMA-ds1aNkewBh1XwqPy4CVWf8WSvgzDdkmg8L4lbFs0wCEWY8funZniQNyHMBz0_hMXkF3rToHohrBL5u3aK85Lh1pw1ETS1xQITLNcTL7_ihodP5XIRQH0558aGxw2gjUI8h02fpas3R_-rEICWFwvZj36hhCcfiCkjn8XIahrdRfP_qwfN23LFyGc0JbAdHAN9rf0KArUjFie4-PIHiBtUC_OOFPGK8QTuBUIfiRBCTIMuEijHGPN60FQTxmUAGOc4hrLssrv_4_iqntL8WCilDoi9MvyA-kuXiA0Y0T9K0rYm5ioJ7Wbjd0gtIsFDoCbTZxfkv5hYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_50060JwpIt4AOzP6G2Z7uBwuwTFucxwd-dthDk2JjeWp4NUm7Wz0i9j8KzX_UbS6AjydrDsGH9okksA1Klv50vx7xndyhf7SmCNEW6nmFVL4Y4jFJ8MAuxktCVIdUQv5ocv5tfSd4ytfESlpRCNyw2dBviGzJsEfAgxM9Rfkk7FaC4M3cAXZYhqLyqdmIrJyyZWXlhetkc4ZgpCy03dQuROqbIBFGoHWgqR2mcdtV68s_Zf3viSpwhkWt1wjMo_YrLraOG-7wRaacSQUOyxwlKLOSssoMZcU3j0lIhiLoSkoGKG8ED2q71ylFzI4RXeXX277idbFa7nwBKix12Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAfKPKVRa6SZ6Z1cIX50S0CcKEM0trWfzIp1u4-Uh0SDrNJbInbceWsKBbsuBvAfUeALg34HUyZDeWWpoCwUs9rfCjefwS348TAbaSu1vYdoYcwKVtE1DiLvW4ZeTIDbnDrWNXUv2pYkjJp9gNrPfzFsDC2BJva3uiYXo8bqPpif2OVh_WBH8XUu9jl3WdIV-OhotNkwnihmj1iVnrNZFQJ5kS2f9SJZwanOnP8Mun_6iwSteFnRIiwp93uw_fvogm4D31S7dLKgwAfEib5l-Iwkc03eCdnQK5zl2s0BEEfI9grkzKwrL3uuSRe13IwQHlGQTPVuLCWEZHOtr0jUsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNwt3XZLvpnw0B_2RzRFescLK0KiTacLKMxEVCKUxGz3TJDPYXDdFVAIxEEbravz_saBK7yNT3Yo09tR2HtIbv5zCSp_gIXidFx2J6jlyeCwu1E8gIDD1it1SqiueEiQsYUH0YmYYgSQuIgzXKC6_psn_B0uip-KL7c_tVKmNVIlzH-uLtCjGvCwOmiH-k2e4MmNediCSOb1FNJu72M91g-CV_cU2HuAadS3cBNLdzmIBOC6ODSbUoaQV9JpPvu0GhRNoCxaXdSgz1V-AZH4wliKmcRxJvvpgV5SYsl63SKNF6BuH0i6HLnFPCg-FfJxy29Yqb6zE2VdW9f_InnomQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=Euq2gI8QBCdGdqSV1QVQOsQUONrqm6ZoYz7ToC1vrNvI5U1iJ4eS6gyhN7juKtekA6CkHhGV2_bfjwp8gFMAdWbJdVDP1Op37JxAl-ue5pSP8xr2EDnHEoVyAgd04nIVYobwM_ETSm4VK9vUz514WVIE_9DnqUcDfixi47wGrz67ywl6HdxgAmdfmylzc4Xk_xLdlBQhEZ4Fo2F1DeD1_HXUJ6c0_Mv6cJhPOmfsstoNAhkg9G4XRZ791KrJaQPJeed2YwXdnlDAya6ZwqwlxYAFHxCtKwduYcunQHWKr2eYVhSM3ZGnl_TQtZ6ypKJkd7I9N_Hs5Kpc49XA1U40-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=Euq2gI8QBCdGdqSV1QVQOsQUONrqm6ZoYz7ToC1vrNvI5U1iJ4eS6gyhN7juKtekA6CkHhGV2_bfjwp8gFMAdWbJdVDP1Op37JxAl-ue5pSP8xr2EDnHEoVyAgd04nIVYobwM_ETSm4VK9vUz514WVIE_9DnqUcDfixi47wGrz67ywl6HdxgAmdfmylzc4Xk_xLdlBQhEZ4Fo2F1DeD1_HXUJ6c0_Mv6cJhPOmfsstoNAhkg9G4XRZ791KrJaQPJeed2YwXdnlDAya6ZwqwlxYAFHxCtKwduYcunQHWKr2eYVhSM3ZGnl_TQtZ6ypKJkd7I9N_Hs5Kpc49XA1U40-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=GjEqPgL6rq-twOwjrpYFqjB1K1FbCCMlgYK6faYA4uAAbAUYuDLcrb99nJOTF-WI2VuDCzBlmeaEUKxcvRaTimKEDA6MC7n5JGiqfzIS--SmnM1-Z2dA8VM_x7Kf6fKleGNl5UJN5A8Hum5njlu7bBQV9pctPbt9cyU2HgyZQjNBWUnQFInFg74pZWJ52ZWQS2IymdcetCIcBhhfx08NsqYHCGpt_jGsMEwgpn8A5jT6xAwG9g-YpgKp5A1zDnu6L_ZkoqwdMjUIZFeYypA-uULgkl-ZbFs2Qji5R6csO1eXo6-TaZSxlcMAgQ9nosyMAoruZG70pArN3svmKdaP-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=GjEqPgL6rq-twOwjrpYFqjB1K1FbCCMlgYK6faYA4uAAbAUYuDLcrb99nJOTF-WI2VuDCzBlmeaEUKxcvRaTimKEDA6MC7n5JGiqfzIS--SmnM1-Z2dA8VM_x7Kf6fKleGNl5UJN5A8Hum5njlu7bBQV9pctPbt9cyU2HgyZQjNBWUnQFInFg74pZWJ52ZWQS2IymdcetCIcBhhfx08NsqYHCGpt_jGsMEwgpn8A5jT6xAwG9g-YpgKp5A1zDnu6L_ZkoqwdMjUIZFeYypA-uULgkl-ZbFs2Qji5R6csO1eXo6-TaZSxlcMAgQ9nosyMAoruZG70pArN3svmKdaP-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3Js2JQySlOrCEtIibieefvEX9ijphQWo8ChFx1s58nvp2KVBwVNr6F_P_LDqsVeMZwBYHKTvXhXrbteR3cavx2zLKVKw6t4s2JRli2GGBmPch-I_oxVdttD5ogrg6HHC_OH1m2gqDLlmz0zV99ikoxCv7043TvZiXkC5NzEyGP0CwIoenBcMHXlpy_OEjva9972-wNkOWsQL7Uydwi4JlSru3OSJTCanA7U3MjL6BmgIEg6nhvFAl2zw5b_RsXa4K4V0V652_OJeiBkgEYLlE7-7mt4fswGgIq4IPHgLQslmWEbhaG8Qcvd8D-1GP8T479VgdrqZlQU2dVQxZsz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=iC7tH1AOdBpd04P7f8wo5Aqrus_ePOvhPddDdho1qYXh1GFsZyzZnH9jpV1bcLMw2g02XTLs6YP_qqvCHaMv-0HqtMwDuIN59Dp2n9vg2i29xZmd7P-dopaH9v3HZFZPesa9F6uUNfaw77oqvHotlc2yHJfAmOMlWcj-btptOsOu6_rC6-GO4MOuqBspBFuz3_tO-rLLHY7xxFs0dQFZHBs3Pfl068LEAVbT9JGBzlJmqZbMctxgDYvEOC73OsVATd5_cg_DLQ7zfYPT1eNwEWeo3m5Q16sQkpOr_kKimKtOVvJocXGXy-957o6Bi4DkydD34xHK4g9_J0F_4OjEhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=iC7tH1AOdBpd04P7f8wo5Aqrus_ePOvhPddDdho1qYXh1GFsZyzZnH9jpV1bcLMw2g02XTLs6YP_qqvCHaMv-0HqtMwDuIN59Dp2n9vg2i29xZmd7P-dopaH9v3HZFZPesa9F6uUNfaw77oqvHotlc2yHJfAmOMlWcj-btptOsOu6_rC6-GO4MOuqBspBFuz3_tO-rLLHY7xxFs0dQFZHBs3Pfl068LEAVbT9JGBzlJmqZbMctxgDYvEOC73OsVATd5_cg_DLQ7zfYPT1eNwEWeo3m5Q16sQkpOr_kKimKtOVvJocXGXy-957o6Bi4DkydD34xHK4g9_J0F_4OjEhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=EwHiRfBZ9CNac9_m4lwwOxpeIztcq71r02J4DOSWqLH72Oh4YDuWXQ93Slr87bDzAqtY4Y6SA0t4B-rcS4aTpZiQ8dToOMZ2ho589kOturziDBafQKZD67Yv_2cXY5pJ1XDzrV1iVLT7Z9PzgSu09h5GYPuSdm9oaGVHZavroGg6KdiGMuVgdkKGciziwmj0kOexsQvOhDARpzWHrn--dH914c3vSChodUX3pqKYiV8gvE-EhCBLxZjZXlBzDyr8aoWekgK31QfFuHQvVsi5JEt1E-cFOQiW_3cVKbCbHOdIrjVF_rtSdJ9FEBFLpvSgDjG2GsRwQRF7XMmgcglU0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=EwHiRfBZ9CNac9_m4lwwOxpeIztcq71r02J4DOSWqLH72Oh4YDuWXQ93Slr87bDzAqtY4Y6SA0t4B-rcS4aTpZiQ8dToOMZ2ho589kOturziDBafQKZD67Yv_2cXY5pJ1XDzrV1iVLT7Z9PzgSu09h5GYPuSdm9oaGVHZavroGg6KdiGMuVgdkKGciziwmj0kOexsQvOhDARpzWHrn--dH914c3vSChodUX3pqKYiV8gvE-EhCBLxZjZXlBzDyr8aoWekgK31QfFuHQvVsi5JEt1E-cFOQiW_3cVKbCbHOdIrjVF_rtSdJ9FEBFLpvSgDjG2GsRwQRF7XMmgcglU0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=SpEz2SVeuPiUS_i87S16AmFIfYeDLMfEwsarz_wIlS0BL5vSpzqgQnGhQuSTzKpbkMgn_ywBo_612h7g3bU-HIUfryo5v9I-Hbmrmm8YbHLyYlyCDtEGVU4BTheCI_kGxa3-ErpaR7Q7HkTqlWc6B75NqNoCscjr2wq9T36p1XGLnglUQ7WHe6ggE1r9FTaIja_9IYB0DRqUEhD6N8VfpYoLYvTzjwapNje49f0aiLVc2LZpk6iXq0vSPTjfEKOnNC9lRP6JaqBJpCZVu3YvlvWvCFXS7f49egmoGL38GHIKBFxj0UYAEEwANZ1QylBHy2E0nehEa6bRow8Z53L73w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=SpEz2SVeuPiUS_i87S16AmFIfYeDLMfEwsarz_wIlS0BL5vSpzqgQnGhQuSTzKpbkMgn_ywBo_612h7g3bU-HIUfryo5v9I-Hbmrmm8YbHLyYlyCDtEGVU4BTheCI_kGxa3-ErpaR7Q7HkTqlWc6B75NqNoCscjr2wq9T36p1XGLnglUQ7WHe6ggE1r9FTaIja_9IYB0DRqUEhD6N8VfpYoLYvTzjwapNje49f0aiLVc2LZpk6iXq0vSPTjfEKOnNC9lRP6JaqBJpCZVu3YvlvWvCFXS7f49egmoGL38GHIKBFxj0UYAEEwANZ1QylBHy2E0nehEa6bRow8Z53L73w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=v2Dr0lz-AQS19Cz5a2LFCl2HrUSQL3Xs2xL2FwLADSmHYpJ_vS6y7k_VWokGQRcTmQA_WnmruWsugZuKgnNteyBf1OQU1qVmZnsyop754dD75oFxGrD11lptgWqI_vcRlWEfmAvSm_CQZO71Uzn7Va2FB4ABKBoZVYOClM_hLxhDViFAQK_VHLsX1ZESQHksEAsz7KI4JiCFglqKuylhgzyCgZmHIWCAut20te44sijW12O6MOWgpcMMfXKkpbKX9bKxYWZaouMCqnrnHHRdQoDzXpqBlj3VtNoBqRFQAF0ORCTRClYvpS8ReFcmxA4-Xh-Y6YNXkZbwhjbDGfBE3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=v2Dr0lz-AQS19Cz5a2LFCl2HrUSQL3Xs2xL2FwLADSmHYpJ_vS6y7k_VWokGQRcTmQA_WnmruWsugZuKgnNteyBf1OQU1qVmZnsyop754dD75oFxGrD11lptgWqI_vcRlWEfmAvSm_CQZO71Uzn7Va2FB4ABKBoZVYOClM_hLxhDViFAQK_VHLsX1ZESQHksEAsz7KI4JiCFglqKuylhgzyCgZmHIWCAut20te44sijW12O6MOWgpcMMfXKkpbKX9bKxYWZaouMCqnrnHHRdQoDzXpqBlj3VtNoBqRFQAF0ORCTRClYvpS8ReFcmxA4-Xh-Y6YNXkZbwhjbDGfBE3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPaPWq8_cZd-m2hLeLsFbafrZzF-DN0tiK6T1L6Ecu3jc80L6dJcafnfBXQWInLCPJXhufM6YkaecD6q9zIkDM3YDOYKjviq6ESZbTuz7m1xyke0wKEE4pzZ0pwsK5x1NmuvlheFrjvDrpBRdI03Cq8__tV7MFcMf9tU0E2GBSDDjw_W2jzrGrfU2ZibOTjQkZcgw33615zJ7e_a7Kb6Ts5-aBo7EfcQpNSk93nazDsGnKeZdTHESIZVJ5VRUWbnJd6OQJpso2EHfkhKCIR5-YhnWMEonBTg-dYPqsqfWoEThnq1_SFbVoVCgxbzbyd-tKvxv4WtK5_lWufpVWlIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPpnWQKzB07pClXqCig_WF6UC4er4xuWkD4DvfqSaaFOFMAZaUNm0kHjQA1eBQwvxvccA-iruGugrFHzijJvqIy7CNMwkCptPbsmBVQVkp6CnJECkIvTlBPnTEqZgpNBThSXFIjhGNP08hgFgLjzi7B55Eo7P59C8toSasBYCtUqWxDz7I6udYKGxwsmYRFnaMxqW5KmoNFRKgn3HkJ3U7pyHC0nQzfhVG5PPeldDEy9Wzqo5pdKub0MjSOPW2S4II00Ujyeg9-p7Hwfeo53rVQBHSp7MX82FREcSe1oYaOlj21tcBgRDGC2624icuc0cDwLXSCKriTZ-gqfrU11LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=lXkkl_SD-zY7HCVfWMeARLJJP4y4SEvnEyLWNzwZrQ1-kjVuH7vhH_qlwLRxHR0BXPF6PLs8qJ19dixIUY3sVzeRU-LhiYQKro63k1NBB2zbWttHwu46DEMbZ_RbjI9BgHiZsuLzS7dYy9B9AxpjEPZp7x0-vwVwyKWv-gjuKXM5OhSgALz3DreChfniWmzFGuLALySulG9T8yQ0l6GfchnLPAnWzgP3oU6NR5Uj5rwls8Fb_WRCDDzh878Y25622mvBECaUMi-FtWhsxAA8-WiUsmuTMhe5gBbveIuLEr1dgJHpo1SwlrBKFBRjtaCtiP-suxQt65OHX-tLZg3V4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=lXkkl_SD-zY7HCVfWMeARLJJP4y4SEvnEyLWNzwZrQ1-kjVuH7vhH_qlwLRxHR0BXPF6PLs8qJ19dixIUY3sVzeRU-LhiYQKro63k1NBB2zbWttHwu46DEMbZ_RbjI9BgHiZsuLzS7dYy9B9AxpjEPZp7x0-vwVwyKWv-gjuKXM5OhSgALz3DreChfniWmzFGuLALySulG9T8yQ0l6GfchnLPAnWzgP3oU6NR5Uj5rwls8Fb_WRCDDzh878Y25622mvBECaUMi-FtWhsxAA8-WiUsmuTMhe5gBbveIuLEr1dgJHpo1SwlrBKFBRjtaCtiP-suxQt65OHX-tLZg3V4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0pzUcTwGOMfAtBTb-wL-IkjpwqM1HYTL29wlfBDun4fF2hP_Q3HuuuuVpi54aMyJJG-BynBRD5owDwzNKfkki10lqNewK1CF9U6LaeNS-_QsdCikd_6N-E9JB9nosESpJIH04Un5VrIDdOt0fsVPbSgaom1kukAOgwYIhl3cGuEz_BHDspJ_adffwidOzrAa8TEAoWHOojETNBmev5SANRGYOgpZIJ5JWxhTg6C6WiiSErSlwQK_JYgk_xdk8MJJMh84xzXMEUf7MgpFShqxwG1CmOPyt2oSwg8O5uIZ2IvouNJi0Je_2vuLFL1RX5e5fFNwCCgjhEk87k7Qu3mD5mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0pzUcTwGOMfAtBTb-wL-IkjpwqM1HYTL29wlfBDun4fF2hP_Q3HuuuuVpi54aMyJJG-BynBRD5owDwzNKfkki10lqNewK1CF9U6LaeNS-_QsdCikd_6N-E9JB9nosESpJIH04Un5VrIDdOt0fsVPbSgaom1kukAOgwYIhl3cGuEz_BHDspJ_adffwidOzrAa8TEAoWHOojETNBmev5SANRGYOgpZIJ5JWxhTg6C6WiiSErSlwQK_JYgk_xdk8MJJMh84xzXMEUf7MgpFShqxwG1CmOPyt2oSwg8O5uIZ2IvouNJi0Je_2vuLFL1RX5e5fFNwCCgjhEk87k7Qu3mD5mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=mAOLcen82Qbf2Pme7skE_1LpkB_VLROoyWIk_fZNWemeebnHkZxwDD7EMFtCGV2bMBiJKLah64lW_LlSCyhVaa_16GYCxW02A31-YSdmw2SKl8G5pyt8KV1fmnYDEpwNl3qb8NrKMMeTT6ua0LhNHwO1MHxYPRH1G_6HxihH7x6ZdKlN9y1gAl7Dyy82wTuRcBlwvK7-kVPZldJO5SjhrX0Wy2eUdshXKUaX4zlIQyqsJJgNgXZOgxf1fK7wmzzLaSShLkRNSWb9MS_3F9OqRXJ416nNK-sXS0G_p14UPk3XCTp6m_19X3jjrXDf63t-B2e12ydWaOlpzY-d0XNs1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=mAOLcen82Qbf2Pme7skE_1LpkB_VLROoyWIk_fZNWemeebnHkZxwDD7EMFtCGV2bMBiJKLah64lW_LlSCyhVaa_16GYCxW02A31-YSdmw2SKl8G5pyt8KV1fmnYDEpwNl3qb8NrKMMeTT6ua0LhNHwO1MHxYPRH1G_6HxihH7x6ZdKlN9y1gAl7Dyy82wTuRcBlwvK7-kVPZldJO5SjhrX0Wy2eUdshXKUaX4zlIQyqsJJgNgXZOgxf1fK7wmzzLaSShLkRNSWb9MS_3F9OqRXJ416nNK-sXS0G_p14UPk3XCTp6m_19X3jjrXDf63t-B2e12ydWaOlpzY-d0XNs1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVGWy-VpSunoO5Tgbwwh46OJErk8m5yZ9Z4a3i-uHry0my-0-9Qlx6-tMdIAb-9Jr3siJKoQwyesMpgVPjU-muz8pKAAKfGnvXmbCP7qRaSGFhpF7j3WQ3rv-fswaIyrJ-0qtvUhuS4LyGw5Shot2fn0eTd8_D7eHqVr393-A_GcecGbyi-OQ5sNzd219IMfM6jKZRLJMXp-GP-TLv2_thPKosCPxcX3fFHBaTaMxkgqkWq7WxdstIdC3UybrdnaElG86obkX8qJog5AURY9F0vkw-r_zlqiYNoXFyzyHuxOQrmTlyQIClU7rn2fHeKP2BQQv6-HIJQMt3sjsw0e0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Gxu9EyEjKmBZvRAeeNzr-AivHSXttgydAU9Dmk0OBsKtNSwu1bFJjjL2Dk_4mo_SsDkR6EHeMyxvXFWbCrU_UEBDaF00ZlycSGIHyaHgPtjLUO852kdfjDHR69RJXC9RxYHOveXe8yX-KAPUZQ27R6tS68G85kNW2Do6wRgKeq5OX7WjbIdipEA-vaFRrnRJSsfRx5k-1yGGH1wYuZp_VSmxZd8hidTG565HKJR4Kx6x97lWlMo2pV-GyYxhKYiN8hVxcElq27elCIgZq8uxjYOSPUnI0SHUlFJuaCav9k2yWA8Nrc5yQTO4AAz5gejhOWy0McB7xWg3whHpeGIpXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Gxu9EyEjKmBZvRAeeNzr-AivHSXttgydAU9Dmk0OBsKtNSwu1bFJjjL2Dk_4mo_SsDkR6EHeMyxvXFWbCrU_UEBDaF00ZlycSGIHyaHgPtjLUO852kdfjDHR69RJXC9RxYHOveXe8yX-KAPUZQ27R6tS68G85kNW2Do6wRgKeq5OX7WjbIdipEA-vaFRrnRJSsfRx5k-1yGGH1wYuZp_VSmxZd8hidTG565HKJR4Kx6x97lWlMo2pV-GyYxhKYiN8hVxcElq27elCIgZq8uxjYOSPUnI0SHUlFJuaCav9k2yWA8Nrc5yQTO4AAz5gejhOWy0McB7xWg3whHpeGIpXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=LOy6u27l5WAEfQFdUpif1mFYXTgr85tK1i1kwmsgWimZRxjLjYul2T7V1eyrFuy3qlH2WeA8VQWN65EuY6AF4vzuQETmWcmd4nEe9liat5HuWRCgozAzlTTbsoSTQ3YIK-Ky_-ASOZyg4Tqo22EBF2B5eF0ieDEektmwD1vUaBhQYbkPfmL-eUrQHTeogfxz-C8vy3cA54yapEJINeEG-gRD8iJGhm5JOtQJEH7Ub7vo7fXc5g88jsOBgB37g4dqZ6HYQuNNql0GrMvxZgcGHM5CVyuRVFgs9w1pUtylSeu5BsKZ0KbS8yyTCaawEuZaXpkb0HSYpHkyYEpKofefHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=LOy6u27l5WAEfQFdUpif1mFYXTgr85tK1i1kwmsgWimZRxjLjYul2T7V1eyrFuy3qlH2WeA8VQWN65EuY6AF4vzuQETmWcmd4nEe9liat5HuWRCgozAzlTTbsoSTQ3YIK-Ky_-ASOZyg4Tqo22EBF2B5eF0ieDEektmwD1vUaBhQYbkPfmL-eUrQHTeogfxz-C8vy3cA54yapEJINeEG-gRD8iJGhm5JOtQJEH7Ub7vo7fXc5g88jsOBgB37g4dqZ6HYQuNNql0GrMvxZgcGHM5CVyuRVFgs9w1pUtylSeu5BsKZ0KbS8yyTCaawEuZaXpkb0HSYpHkyYEpKofefHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Q13IsiUA8D_obIqsbbilsiDsvBBUMSGdBe3JOtz4Xn6PTxX4dKuVonNAmVaq90K4nDPR27COxkh3zfhTuRMZH-d-Z7Z-4h76zseAI3Gn5-5ubAFqle1auMkYurIideEMInO75KMd8nHWiqNat3U9Bjl_FypEuWv1NkLUrpd7AOeiujJzyW1Mr1tRTWFOOaapW7OkKNbX7hFC-yJoLlLT24z9EJoWcSKTBvEHKeXohrEkOh5HiRMHirAlujc9QjPe2w4Es_u-7TKDpOfAPDArQho8rbnUOXnvKU47vW4w05PgqfQOvSVh8Mmv3BNrjTdVlpB2lS0SGBy-uso6IIs4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Q13IsiUA8D_obIqsbbilsiDsvBBUMSGdBe3JOtz4Xn6PTxX4dKuVonNAmVaq90K4nDPR27COxkh3zfhTuRMZH-d-Z7Z-4h76zseAI3Gn5-5ubAFqle1auMkYurIideEMInO75KMd8nHWiqNat3U9Bjl_FypEuWv1NkLUrpd7AOeiujJzyW1Mr1tRTWFOOaapW7OkKNbX7hFC-yJoLlLT24z9EJoWcSKTBvEHKeXohrEkOh5HiRMHirAlujc9QjPe2w4Es_u-7TKDpOfAPDArQho8rbnUOXnvKU47vW4w05PgqfQOvSVh8Mmv3BNrjTdVlpB2lS0SGBy-uso6IIs4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=kLCeJcFz4sveZXTp7-zV37iS1bvsmcpE8_0Vm_Fmw6tdyUVbgasLdnayPv2ftEOtJ0AqfF3Q9Ektg2jaSqyynPzmsfyzbO7nNfMJVr5Agyq_9TyrL6cSTMVubE-LuCzZuboiLyUk9WJzoiw5Dh-1p9ct3S5lv3es3LuX9kay77ecymwdxb96WU64-jkrCx8sQ1X5dgcf-SzElobGuEZ2BUfQj__L5BjRxzQfzAV4qothF6yyj5UW11307s0Gsjkzu0HFqvAijxz5EwFH78xAHFskjRIAhBPeWOr5nGG0pv0-EHkgjg_j7lG3ZynJ5tar10M_vjrSuXGv42yTgxa32g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=kLCeJcFz4sveZXTp7-zV37iS1bvsmcpE8_0Vm_Fmw6tdyUVbgasLdnayPv2ftEOtJ0AqfF3Q9Ektg2jaSqyynPzmsfyzbO7nNfMJVr5Agyq_9TyrL6cSTMVubE-LuCzZuboiLyUk9WJzoiw5Dh-1p9ct3S5lv3es3LuX9kay77ecymwdxb96WU64-jkrCx8sQ1X5dgcf-SzElobGuEZ2BUfQj__L5BjRxzQfzAV4qothF6yyj5UW11307s0Gsjkzu0HFqvAijxz5EwFH78xAHFskjRIAhBPeWOr5nGG0pv0-EHkgjg_j7lG3ZynJ5tar10M_vjrSuXGv42yTgxa32g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jsbm0DxHLOiC5c4wILjIi46uJ92j98ohznJuTWyIKjLeRYOa5OilX076WIEnz6K1WV-7v9yfCGXYyCFMmKolV38CPmvm4J-EiH71wvfqS1DE5s9E-wXwICWWi6eaX1V6h0ZLaFdUsQ3T2abK2ryy6LeeGyDmGpgHImQWD_dqAhQbAPudXQPmRugz4glVNEM7oyenrMWpYbQv94tTKhohK2ZNRbNFKap0KFDwsUA4qaQVD-jiDgYKoJo59VbmxgTF2-lwho36himOtlLTBDjNuBQa1KHfGWzfEhOxfmNheHFhkMxqUuzMyzzjtUFnYpa0VD7AHCgryDx7WBaDDlANBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=ZuQrAo64_m_6tiVQfY4LNDeK2nlf97r3LkyaOW6FAH2RQdKpx9ISpF80ZZeeb3e45lYnUgZnuMOJJA2EaHSqVRdn1lWhBfuO2lE37ksWGeIO_pWGigUiWv9gKNCFGi_uM2M755SF3nmG1teuVUOx4vm4h_jSCYvvEglXiErhbrMOKWxyZgSxRkI_AwZr9EgxCi145LRMLQu5jjtZaZmp9Mu4NoNpqYjttpFJ_zlZMPTbjc-62wa9S2pfPfM6iAoNwDGGv8Ky6c1Z6DCXZD9tMaaLybBhpAG_Gi48C1ADwyPmcrSlB8_JKu80V2kMWtaiNuXzTFmV9t6AuXFn1KWUnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=ZuQrAo64_m_6tiVQfY4LNDeK2nlf97r3LkyaOW6FAH2RQdKpx9ISpF80ZZeeb3e45lYnUgZnuMOJJA2EaHSqVRdn1lWhBfuO2lE37ksWGeIO_pWGigUiWv9gKNCFGi_uM2M755SF3nmG1teuVUOx4vm4h_jSCYvvEglXiErhbrMOKWxyZgSxRkI_AwZr9EgxCi145LRMLQu5jjtZaZmp9Mu4NoNpqYjttpFJ_zlZMPTbjc-62wa9S2pfPfM6iAoNwDGGv8Ky6c1Z6DCXZD9tMaaLybBhpAG_Gi48C1ADwyPmcrSlB8_JKu80V2kMWtaiNuXzTFmV9t6AuXFn1KWUnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=V_4SL1lPCx-Y9AD2PYM9m3EdWlPsdXraEFDKQfBOswx9h6h3SRWQ1HD0NXqQ5dfaRy0UIl1Q5VKgIvq9jpuxLybCR-563qhy6tqjMQlw47lrloC45yQVi2dqHuuYR3X1H9BvE6se-IwGVSKhlzEzfdo8c_msxiYXQOE6yECmBfT1ID1eP6hoyLO8kqeVnOVsIE_XSJ1cf1OdT92e0EHQbHqokqBoG4W6pTtnZdenONceSt2zb3rH_XobvMkvPeDVRFpBXzCrAgBOXWU8el9LzuAhBVSJrLMq-5ok5U50ANS-MDpvb30Z0ZkdPxdMA2gg8X-gStvc17ujH2P66gJcig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=V_4SL1lPCx-Y9AD2PYM9m3EdWlPsdXraEFDKQfBOswx9h6h3SRWQ1HD0NXqQ5dfaRy0UIl1Q5VKgIvq9jpuxLybCR-563qhy6tqjMQlw47lrloC45yQVi2dqHuuYR3X1H9BvE6se-IwGVSKhlzEzfdo8c_msxiYXQOE6yECmBfT1ID1eP6hoyLO8kqeVnOVsIE_XSJ1cf1OdT92e0EHQbHqokqBoG4W6pTtnZdenONceSt2zb3rH_XobvMkvPeDVRFpBXzCrAgBOXWU8el9LzuAhBVSJrLMq-5ok5U50ANS-MDpvb30Z0ZkdPxdMA2gg8X-gStvc17ujH2P66gJcig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAAwo8Yjgu6eIaM8aYdIKMIFTV_G5LDLWvJoqrZa_QcXEiWC1LBMawIp7rkUe6YlC9I5DO32T5Gs3iEnW8AGXt9Ay1IlsocthWBIAM8WcAKTWr334xTW8GGSSSlV9bYhki6dNRTOi4PgMzH9lM552OdNUc4hDibcyC-tPM05fbcy5nydI9usvtmE_eF528QHUp429ZW_FZHCRuDD7v4Mq2ODI0ssESthjIb0poUXLOEFiW9SezvoyGXKkw8dg1PhS53Ew_FuVpuLWfc2FtWHdyfSRMBguR6tYNCOa4mivYki-u0vAcEL_fs38FPsLUBAZE_dJX8bbSOetDIBfg2dJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=KQsr5NG2BEePisWgKniyNjm26Px3YpJ-E-ULiF71Esi2nSdMwrGgfkh6CW5M3w-nrkyXE1e0Gwn-Dtc45UGA206pbkT0UZao-PZ4sNPWbtfas22_dbdtph9Plnpc8JoHz7XeRJFDBjpaBQlHcfX1UkMIaEMc-q-UYFYjpI5BdFGwM0BmOKZB0NDIOmrj7mqs-QBLY6nYtCFizizBFpvxpv06ZBAVALZon5B3sItLM1Nkij2fBpcJX_A34dmD0wLxA1kDubv4XFi7gTgze9xypexOC0esv1G2_R3NfEJ75HVz4pLo4NjvOMDBuCqEoGAAkxEPQiC-3MFFnc5Xgbu8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=KQsr5NG2BEePisWgKniyNjm26Px3YpJ-E-ULiF71Esi2nSdMwrGgfkh6CW5M3w-nrkyXE1e0Gwn-Dtc45UGA206pbkT0UZao-PZ4sNPWbtfas22_dbdtph9Plnpc8JoHz7XeRJFDBjpaBQlHcfX1UkMIaEMc-q-UYFYjpI5BdFGwM0BmOKZB0NDIOmrj7mqs-QBLY6nYtCFizizBFpvxpv06ZBAVALZon5B3sItLM1Nkij2fBpcJX_A34dmD0wLxA1kDubv4XFi7gTgze9xypexOC0esv1G2_R3NfEJ75HVz4pLo4NjvOMDBuCqEoGAAkxEPQiC-3MFFnc5Xgbu8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SlvNYJTMjM56tp2QRpkqezPkmEdcKmp94uSljlv03JsZ4GxmDiWSXLBhZSz9TUgjxzShiJABcLqjlKUOk33uwnNd_9uWprQH1-yXqTPku8WWSNJEUlJULHoh1i_XPaJ3hqGHuWGQBBAz5IowWo2PjsUICB8wINYXwAVkALXH8Uh8Inx41mF647jsu5e0ZuHkx6y1PaelV2hqWw_JOuNi5l1k3JLPwiY25GGWXDVlu3szmxJgMC3g1lu1QjMJd3qEx_UjNewr-Ap6zsiV2XSDPMy_UZAGVoJc074KBUioyYdZywynfi2aQdBIEmHHIDKkKpjzl5mn0aaoHx2iRX9Q7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SlvNYJTMjM56tp2QRpkqezPkmEdcKmp94uSljlv03JsZ4GxmDiWSXLBhZSz9TUgjxzShiJABcLqjlKUOk33uwnNd_9uWprQH1-yXqTPku8WWSNJEUlJULHoh1i_XPaJ3hqGHuWGQBBAz5IowWo2PjsUICB8wINYXwAVkALXH8Uh8Inx41mF647jsu5e0ZuHkx6y1PaelV2hqWw_JOuNi5l1k3JLPwiY25GGWXDVlu3szmxJgMC3g1lu1QjMJd3qEx_UjNewr-Ap6zsiV2XSDPMy_UZAGVoJc074KBUioyYdZywynfi2aQdBIEmHHIDKkKpjzl5mn0aaoHx2iRX9Q7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=IzrIRViwoALvZZU8C37WU2b4NNq-aZa53HsT4aNhnhjTTdo6k77Bcrv3Xt-V4laZ3WbSoKExxU7wSI6yXcFNUAUwKYoWRmhGnYtrvej51qlpubjDPfE0gF6NbAyAApJjE67s_LwtUa250HM1gFgCuANXz_KpSBtkYCWf2rHEiMGofl9KWUtDCf3-5RJe12S01jXH8W78e6Olb7dyf1ylXQJgOl6u4rZo_02z7gEH9saLiYuoksMNTTJ7cWUnmr5j_yYCSw7VrnwIxJ7G2haApWKWshe1Cyl6AUhmaC9lSuOPTB3uwSEh4xrgUmn6qLXqEN_PNfm_Ba8QtSMuLnZ-EzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=IzrIRViwoALvZZU8C37WU2b4NNq-aZa53HsT4aNhnhjTTdo6k77Bcrv3Xt-V4laZ3WbSoKExxU7wSI6yXcFNUAUwKYoWRmhGnYtrvej51qlpubjDPfE0gF6NbAyAApJjE67s_LwtUa250HM1gFgCuANXz_KpSBtkYCWf2rHEiMGofl9KWUtDCf3-5RJe12S01jXH8W78e6Olb7dyf1ylXQJgOl6u4rZo_02z7gEH9saLiYuoksMNTTJ7cWUnmr5j_yYCSw7VrnwIxJ7G2haApWKWshe1Cyl6AUhmaC9lSuOPTB3uwSEh4xrgUmn6qLXqEN_PNfm_Ba8QtSMuLnZ-EzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7Gs7XilFTnE45pEBEHox2ef1wtHAYPraQMRQ__Sx1LpLSoFyD2L3Z_MsNy-Jqv_PsJzh5gHg8hpbmhy_VXgiTpWe7d4bx9iezwCVAvt43wGrLTmGupBOtbH-6pY17fgZ7hlzGODhf-ks9zAECfrCsAnrwGIKXJnJ7iW6p8GE84sZew7LkIuXVu8efl4EoHudx1PFYLTWXEIICoUnwCcX5a0MDat439Nqek_6W-rUeG2DBMrzfIrpeV35WsLWxlbkb4FksG-mwZtjSj3mTrOB31Cni6FDJZ3C0LkHH-nFNnME5AUhNIbckyhZGM_EIYiZfh73gpTTwQ-YAoWDgKs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROoOqYigDvwdeF2WiXeBM_hMntlP8DaKWMQq5bpgr67bHtYAnxZuDHplyooKLAQny1s5g2PE3NJ75mnbfVYGisl2RRRGqnJGmYbRGlq4MGH9X9-LdH0pJ_dg8GUBhe662VCO92PcF_RV8Cjqwhl2kCDJ23-EKRIiSCll-G2ARwzJhiSiK_0TQy3nCAZDRiX1M2ipBP8BsHqPyj3o7fjP21Ph4C8hk45yKeKRcV3DbDDDEVUHIfQvZdUR-2oa0giin6JOe2GjpuNm0jjIORoK2Aazrxx-unphPubMiirwKov2UzdqbRSokQxPa_jkA2cfQ1yofvRLqIFuhb2-e9fhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GD2w_HCQxK0ryKr9XQ7tIyUW01qQv-GrN_s7rL1bbotvu-m2vzxWEQcAdVGnD2B0PzvL2OlSrAxBp4Ia_CqMea0NYL8_gGZgpF3eeZVldqNk5McapTzsZiwMrdV4QDR21GYrP0SG8LSc-gissvhedGSc9vsRP6nqFnbIEmOhfinVLhXvyo9vk50eEYEqi7RMH6mGTWmHH5wEEXfpVi2OeLA0wQpjnJUZg7-7A6h4tR0FhVZ8fnplSV1psKAkyx-RK3menhwBHmdxptM5WCPc9KXooqL0hu7tMfuxaJiUOFO8JVrO-G1WzWr7X587o37JZFvgd9BkH7FZuT2BWEJeDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=FHhdw-1IsxiQ1-6SGI0jqow8gXzAyG0Hu45q5aI0s4aKo8ouAMl7KMqdrbXZyEZ0NwZyBk0TYuTB1WxhuP7GrsLr5MnU_k_RdMJq5cv5m5CyUmOE6vS90fNLCE4el-zVk2mZcFteYFDxQTeMOL6PmPOeF5XMjuOsK78H9D03iKSwWFVXq8FqZFLHkZRxdBTrijhvPm63fmI-3DXmhdiBSHZDmeWcm1N5j4ndzcab0YQ86Qs6wPtXqmcI0bfFJQZVFkMS7nbT9d6iUvovEXElDqme3w1IIRYCAwoov2lWJ99k30KoOS6qrY9_b4mgll3sKpXD2WUnqZOt_doHJ5I-Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=FHhdw-1IsxiQ1-6SGI0jqow8gXzAyG0Hu45q5aI0s4aKo8ouAMl7KMqdrbXZyEZ0NwZyBk0TYuTB1WxhuP7GrsLr5MnU_k_RdMJq5cv5m5CyUmOE6vS90fNLCE4el-zVk2mZcFteYFDxQTeMOL6PmPOeF5XMjuOsK78H9D03iKSwWFVXq8FqZFLHkZRxdBTrijhvPm63fmI-3DXmhdiBSHZDmeWcm1N5j4ndzcab0YQ86Qs6wPtXqmcI0bfFJQZVFkMS7nbT9d6iUvovEXElDqme3w1IIRYCAwoov2lWJ99k30KoOS6qrY9_b4mgll3sKpXD2WUnqZOt_doHJ5I-Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaVcJlaeP3_L35Ok3idVq660IZl3ym27Bi17e8jDqDs4FPbIw6TLi6W9eeS83XGv3C14D_ep-hKinovy4YNiA8iGlgaiXVJ3h4O8zuy7htOCdh2MBhmNn1CLl72f_saftd2HUvZWH3KAXOQIo4JHFcDe4Rd7ehij8TcfG6dLbYndVrHGTFyBTPfxE4ukyI5j-9pUhjQksPd44IaXGCSSaahhBxiMEHUgRv40-KGTW_wXaK6IbPPMRAjhPubHXrqv6q5hUoSI1nBKx2OBsXqjpsr8wacvN7XjOdBdPIL3jVTNU2EC1I2vgPjJ0GIDs_-wzTGY1t70tFb03C7AO8e3vFH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaVcJlaeP3_L35Ok3idVq660IZl3ym27Bi17e8jDqDs4FPbIw6TLi6W9eeS83XGv3C14D_ep-hKinovy4YNiA8iGlgaiXVJ3h4O8zuy7htOCdh2MBhmNn1CLl72f_saftd2HUvZWH3KAXOQIo4JHFcDe4Rd7ehij8TcfG6dLbYndVrHGTFyBTPfxE4ukyI5j-9pUhjQksPd44IaXGCSSaahhBxiMEHUgRv40-KGTW_wXaK6IbPPMRAjhPubHXrqv6q5hUoSI1nBKx2OBsXqjpsr8wacvN7XjOdBdPIL3jVTNU2EC1I2vgPjJ0GIDs_-wzTGY1t70tFb03C7AO8e3vFH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=XaJTa9v1vkrhqemS_hsfECE46qYPg0hk-p3zYDAsdeP0FVhz4bXBt1PwSBMEzj4SkmMnThwltLPTrF4EPgKtuPUIT1cvKRO-sBzK0zP7sAekTDT1LkpV3LBFsjMSH8nmhvRQsPXHTxUUlbHsWP3Z1YXuIGLAoyr3qjy2zdMNDaGR135PeDv6g6XRomeHyJobpr7Px6w7uSo-tLexJGXc-0NIG5HlqoLBfL6w33wghvQa-EfoiI27Qg_oBQRzQb9e6Gp6iA7fV6Z2boLWkiZoJNra8q6Mj3MIcHH9Cya9b_LIvf3ycUpzPS0W1LybIO1mskoSSvU34h-pXVRoDXdhig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=XaJTa9v1vkrhqemS_hsfECE46qYPg0hk-p3zYDAsdeP0FVhz4bXBt1PwSBMEzj4SkmMnThwltLPTrF4EPgKtuPUIT1cvKRO-sBzK0zP7sAekTDT1LkpV3LBFsjMSH8nmhvRQsPXHTxUUlbHsWP3Z1YXuIGLAoyr3qjy2zdMNDaGR135PeDv6g6XRomeHyJobpr7Px6w7uSo-tLexJGXc-0NIG5HlqoLBfL6w33wghvQa-EfoiI27Qg_oBQRzQb9e6Gp6iA7fV6Z2boLWkiZoJNra8q6Mj3MIcHH9Cya9b_LIvf3ycUpzPS0W1LybIO1mskoSSvU34h-pXVRoDXdhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmVUP5oU844QgPa8ZDIZw4DNwXFG6gWnvDr6BnbfkxbIWDDMD_pb9MYjlXeHsliFU7DKv-P2cSunvYls7RVcr3Tt_EXrpu6FdBqeVmGyRvRD8yUmk3wn0IhRybXGL7M2eyoMvEtkPhSuB7VwfE-T7r4XdT_wD3oUD9xFtB90oqXhgoGLLPT4CefmpganY2cgWUdjv5lPo_90GWhsYNObYJm5uTrB1x2fHVT6fxezIwpgWutTlxErjtWDy1_xsC198iI5OOjKP9wNrXBg-5SO5RGlqEAu1sJyjmRll_CrbB4GmAbXkSbeXvxC8uE34ics9SAm1P8PcLN0gEE5CX2L6w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHGvZ2-5LE7avMxCkudcZyff0zEhqf6YQnSPlT7K1Mbn-eJChXxgYcx559IAO37ZrdBKcWDbsItZvJ_2rRQhIHHDU_2r-mis4cUmriueCAU79oH5poq_w5NLyTGCfQqvJFcdY5o-4lMlqo1nBAN-lgfsXVyfF7XdecLPjqHSzucaLdXhm7eO80Djf6tLK7UYNwpILwGB03ZMgpjtwGmuBJPfBdVMCV1HCBEbs4mqU8cWKgAr1XUpIM-MtatcFCQJkMa5U6Y28w87KmZ33qhHVbp-vImcPVfr2GXteZdRhy_snSY7-sU-5faSk1oBuhsi1vFeNFkSLg2-VZsRY7tswoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHGvZ2-5LE7avMxCkudcZyff0zEhqf6YQnSPlT7K1Mbn-eJChXxgYcx559IAO37ZrdBKcWDbsItZvJ_2rRQhIHHDU_2r-mis4cUmriueCAU79oH5poq_w5NLyTGCfQqvJFcdY5o-4lMlqo1nBAN-lgfsXVyfF7XdecLPjqHSzucaLdXhm7eO80Djf6tLK7UYNwpILwGB03ZMgpjtwGmuBJPfBdVMCV1HCBEbs4mqU8cWKgAr1XUpIM-MtatcFCQJkMa5U6Y28w87KmZ33qhHVbp-vImcPVfr2GXteZdRhy_snSY7-sU-5faSk1oBuhsi1vFeNFkSLg2-VZsRY7tswoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McPcc48kNQbXwFplmfVET9XNHB8CMEtNvmvo1q_8W7pqc10lhZKewHWKDUHFU97Fiwk1JwLRcas2uSNet8GPPzk9opZa0JiMhTnIMhr6tK8UC1p92opKDoGIzq4gTF4z5wutqFk1Ha-iejfP2sbgg_ZfS8k7Y-4xv28jtIGtkLHLjpwjm3-voueGsomk7qbw-Q9Qhcraibgan35aVO7jKY495OPxEY_5lHtxP3FuF2dLHNIBC7PXnH4hiOe9BHKuwJ08PiJDPWia6oomUET2DtI8mCi96NUr8PlPpH2p4bu-uHqSxH1RKErC2TjuAgm3kWJiG9LKR-ZoxGJvO87xzw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Ja4wwW_sCz9Wj6ziB94pNmpDOZd42P06LPBCdIygQL9MmWaChmy2CO5FfGlfzUsBi_chFMFMTl-3hiby3Lc7zFlcSmT9zdsYGRnfGa6hoyHJh_EvBGwKqOlGRXKlcj-63LkYBvWPkGsJTIMOUY6T-oDSASAmFnp0l0MFd16CVN16aOQJj6MwQG_XlpoA8EaYaLR3ykhJmctFw4ZZO0j98uzDNIkLYPGMMwL7w8hR_pJpw1Mu1zzyXUfM3WKId0S7xJg0YFC0rDo8fPeo1jXSEPwCPu9PxkbblfBAuheeUSpkop48Fsybmj9MJckVPQIcLdC8IaJU2YzKgWkOfVJ6rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Ja4wwW_sCz9Wj6ziB94pNmpDOZd42P06LPBCdIygQL9MmWaChmy2CO5FfGlfzUsBi_chFMFMTl-3hiby3Lc7zFlcSmT9zdsYGRnfGa6hoyHJh_EvBGwKqOlGRXKlcj-63LkYBvWPkGsJTIMOUY6T-oDSASAmFnp0l0MFd16CVN16aOQJj6MwQG_XlpoA8EaYaLR3ykhJmctFw4ZZO0j98uzDNIkLYPGMMwL7w8hR_pJpw1Mu1zzyXUfM3WKId0S7xJg0YFC0rDo8fPeo1jXSEPwCPu9PxkbblfBAuheeUSpkop48Fsybmj9MJckVPQIcLdC8IaJU2YzKgWkOfVJ6rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=gTh6XDsE-sQm_qLnC3LK918upLqtHKgq4BFrWR77x89w3LIRPuxSJyQFty4B4FQbj0LHvfs0ox_L-SzHEAPCooCWVRFdRCwAjzhhqgkdexk4B6ciKh9nfsvQvdEWee5-Kn7zV5ZuDSM-S_15nD5--LMMcQGF23y2aHHNXrh7KG2ZgQ6LjjzK46nuhBliXCIgzwTa8g32cAl6FegGReCFJRyK9IHlGQugMAplTw1FM6ri9wNeS1vog9dAMukw5dQ6ISWl2bhZVmGBfyPdQ-c21OW2ICZ1BUafSDDpnmss_fAgk5yMwRYl64_N7lr7w9o6JjzPc9lXhisFmEmUtmX15A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=gTh6XDsE-sQm_qLnC3LK918upLqtHKgq4BFrWR77x89w3LIRPuxSJyQFty4B4FQbj0LHvfs0ox_L-SzHEAPCooCWVRFdRCwAjzhhqgkdexk4B6ciKh9nfsvQvdEWee5-Kn7zV5ZuDSM-S_15nD5--LMMcQGF23y2aHHNXrh7KG2ZgQ6LjjzK46nuhBliXCIgzwTa8g32cAl6FegGReCFJRyK9IHlGQugMAplTw1FM6ri9wNeS1vog9dAMukw5dQ6ISWl2bhZVmGBfyPdQ-c21OW2ICZ1BUafSDDpnmss_fAgk5yMwRYl64_N7lr7w9o6JjzPc9lXhisFmEmUtmX15A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=BJIrCitD7XDgOqjQgOYTXLFh-SSAXKSBWbsX6V6caxn6qNp5aqTRu2i1jQaWQ_g-N_5NX4k7M2qHM0biixEaqzmB4CJrOfxculakOIs2k5TGZcvbWeb_KvsvJselhVsMjvaRLdsd4Tuh-ZQg4csf0nHr9h4GJS6GD9SaRadVCfFbYWWHvSvatHP8qw8XmYxo9L32YCYekU4KxjNyHdsQwo_t4dsLVFvBRdAUBDJxpFTZYWbTNBUTFYpjvIdWw9xqphDruD7WudxjYXHrhu6XEb9QL1gb_DDcx3nrZsOcwlQGCKdnRE_Ta3bcBczC_qZrPdqmLpzjVo14IK2AxrJLoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=BJIrCitD7XDgOqjQgOYTXLFh-SSAXKSBWbsX6V6caxn6qNp5aqTRu2i1jQaWQ_g-N_5NX4k7M2qHM0biixEaqzmB4CJrOfxculakOIs2k5TGZcvbWeb_KvsvJselhVsMjvaRLdsd4Tuh-ZQg4csf0nHr9h4GJS6GD9SaRadVCfFbYWWHvSvatHP8qw8XmYxo9L32YCYekU4KxjNyHdsQwo_t4dsLVFvBRdAUBDJxpFTZYWbTNBUTFYpjvIdWw9xqphDruD7WudxjYXHrhu6XEb9QL1gb_DDcx3nrZsOcwlQGCKdnRE_Ta3bcBczC_qZrPdqmLpzjVo14IK2AxrJLoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeWlmmibsgUTHyUDrTIKzfgF5pb5zpFvFzc7Ou2R54Mrq5mFec0OVOaD0nVIdHOS4nncuh8xXyfXZhOwcWJwsTF9lSnqjZdIW5guFupEZLlfAO2X-ITNevFqNBtDSLFHUJIqcYHKNM7_bLWvYFmLT3u2dBwNn7QncATd8WvlS-q9DVEAFaLW6GhejvrU7UDcjWoiVhW5Y1lvc_OPhDLq4FMNZ23nfwDOKxyTZdREdRzdjG0iIQ2ZP4JrrqKbxRk7CfCy3a5W_d7XfZHphDcFd7Irt7GyssJt6Tb-GJKmJxCT183LLEhSQ43pXOBCnD8SGzJXqQ8HgfJ-E4-nwSikCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSM89AdsSweN9tLFrDC8_utWFzXSUNJgk7YPH0lhA3BEPkEJLhgzz608w69b2MM5xHUoyNGD0Pn6EvpmjApEG7-3x7eq7-9hx_9oEpH07X0u2RL5sDpAt8o07cZeo_fsa9Zbfv3i14GoXeYWQVbelIywrNzUl_87e5phsSN2yYqj1sTEjTd9pu9A27zJQq2wIU3vXGhcdEc5pPTzZoTeIeCmFNcr4N8m39ok7yIvR0FF5b5H_Faknow66esswwUcvYvLOAk-3iOhDEy1bHDeQ4t9BUjJ0WwMK7aDFuq6kE41U6rdjid3q47BM1czZScQRaIABBRbWbQsdMG12QfORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=aApGF-hA51_sbLIdeU_4sWEmGBZCzjUMc0tK4JJ0u_8UFY_o1NN_hZMA3Q-Gu5r_f2-kEnEY-RGKcb8nIKBthG_xlQfbCCojPPMtTTcTkBLD7uygVGcNS5dAIRUdJ1QKL_XPx_qWyYiVEr2i3DiNek6Dx30GtcWyNOUTrm8nbptqTftVppwZ_Z4AuoPo0IdheX4MpJwf6ZX-Pcab57gSn5tO_gLrVnCsKAcsJCII5a7Kb2neQByTeFYN7u6nWzAhzFkdRfQbc9wBIcFx0EKVtqPDPshnypR3ohudFo7KTpZpjqZ2c3CUwCDHVb74ZrUmtK7MoDhpJ836SNsNdRYFZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=aApGF-hA51_sbLIdeU_4sWEmGBZCzjUMc0tK4JJ0u_8UFY_o1NN_hZMA3Q-Gu5r_f2-kEnEY-RGKcb8nIKBthG_xlQfbCCojPPMtTTcTkBLD7uygVGcNS5dAIRUdJ1QKL_XPx_qWyYiVEr2i3DiNek6Dx30GtcWyNOUTrm8nbptqTftVppwZ_Z4AuoPo0IdheX4MpJwf6ZX-Pcab57gSn5tO_gLrVnCsKAcsJCII5a7Kb2neQByTeFYN7u6nWzAhzFkdRfQbc9wBIcFx0EKVtqPDPshnypR3ohudFo7KTpZpjqZ2c3CUwCDHVb74ZrUmtK7MoDhpJ836SNsNdRYFZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDZ0Hfc_Ywh7Lsn-YDR1A6NAvxx-mG6rWVXjWWTmZ3abyjkNQD7QeVl1NivHHqdpObcSanlxGuMz3cMv72wyTyAY8QIjijt7Sy1MdTF5oyRmpyWXhs0Dgap-m0sv2SY_NmIFOuUgOxz4Qjx9j3MV7ei8Tw4_wYnM6hjGL8lwsBHN3InQalvB6Fp4ZVCeF5hG8BZTz0tBs_p6xUftEVKrLoxOAbw9fGVNYVx1sle1Z4O0rKp-MCXHuFzAPOEJpw0pdaebrVclNTrZz8ewjFI9mlyyKAeqJEcSBfy9Ow9-fSUCYr9GKkzqJx-3QdDhSALLh57by3-6p5zBsePl0WKH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzypgPaJ51OxYVGbFIU5RTmoUFJWvQ4WIwCrxwbltmmrXwiDaE8wGLNRO1K-eEaOht_Mx9_bRBkTXm3ZWPFmKCu0ksvUyVHhoZL7MAfcabxTFdwLZMu4-h_KvCmswrG54e291ufrAm7ohBiUX4mzNIoQrH3n__FrCuvIvzxU4YSWdhV4uYpmDuugHRclAvl3cCpF57sLZDtTwQJ6tGAR_5kbcx1E-NkNGUIfvHq3OumFz4GUMaIhnAz5QVH2hls4FP_dctE2NivsSuj5WY-Ybsb0PhslVGNiRgfB8Adgmpyc4L-IVq-Nlht-KAtZzlLv6th70sUZL4jDX-kZiYMK8Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=qayb89TqHRUNvHGFFDtbKKw9DD7pdZxhcQLsJpAy_miQ9d8GigKWyNw9tulMDGD8UjV4b22IDRKPzXVC3PqlR6e6iDkO1BBzOi4cKRsgUmlcZiLhqio92KH7nBGaWqrF1MTw7DjrzlvRL0AMGl3xeWPWLcsiP1DPZQAVETeDI8HGhIsebjfzwrCkfMLly-7JJYBz-zNa_vysmjvOuKpgWvwkGulPs3wvHKYmIE7YbXHaaapbN5eRXCEVza5awZqjvlbTnQ-wXLgOpxMU6J36E-OIrxM7j0z7qAMj2bQsI8sIR2p7j5aZvevQnHcKEM-M6_XJE4tBO81r7sPkZI0jD1TzFuRsADH2G1veQ7FjsFcJdq2Ei6No-CNTaIvdMIxudSGdL65Ag1neVO7eABk7tCKSmKXkCK0i6DFmhXve10NZSFNT7fdyB7pG6yuXdWGdncmBc9Sg1euzbZbFHnKnXEOuiba7rSmZx0CPUAQ5xZ_NR79Yi25rsflUP6WiOGe3cIzV_R5IzR1z93b_2U0gz3LHy4Lbqi4OiApUteG4AaCqe9wPZ5o-Mb278gcUB2SoOCZC94HcDqVO7OIquYbLRDb-BEa0gRyNM-bIl0km1fkE-LehPBtuqvI6-QmPRToSCj2jLTp6Cat_hzR-NlAQIaP9fZASjUsS9UxnHNwq8ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=qayb89TqHRUNvHGFFDtbKKw9DD7pdZxhcQLsJpAy_miQ9d8GigKWyNw9tulMDGD8UjV4b22IDRKPzXVC3PqlR6e6iDkO1BBzOi4cKRsgUmlcZiLhqio92KH7nBGaWqrF1MTw7DjrzlvRL0AMGl3xeWPWLcsiP1DPZQAVETeDI8HGhIsebjfzwrCkfMLly-7JJYBz-zNa_vysmjvOuKpgWvwkGulPs3wvHKYmIE7YbXHaaapbN5eRXCEVza5awZqjvlbTnQ-wXLgOpxMU6J36E-OIrxM7j0z7qAMj2bQsI8sIR2p7j5aZvevQnHcKEM-M6_XJE4tBO81r7sPkZI0jD1TzFuRsADH2G1veQ7FjsFcJdq2Ei6No-CNTaIvdMIxudSGdL65Ag1neVO7eABk7tCKSmKXkCK0i6DFmhXve10NZSFNT7fdyB7pG6yuXdWGdncmBc9Sg1euzbZbFHnKnXEOuiba7rSmZx0CPUAQ5xZ_NR79Yi25rsflUP6WiOGe3cIzV_R5IzR1z93b_2U0gz3LHy4Lbqi4OiApUteG4AaCqe9wPZ5o-Mb278gcUB2SoOCZC94HcDqVO7OIquYbLRDb-BEa0gRyNM-bIl0km1fkE-LehPBtuqvI6-QmPRToSCj2jLTp6Cat_hzR-NlAQIaP9fZASjUsS9UxnHNwq8ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E657xKPSlvwUs3g5Pd_me7AjLmslU6LuNdihlpdvs-VELdIgdog_Vf7g-WdMbWcAak6rOsV7vCvSZnucIOmz_-GZJKUjwZMoQiOafzknugkhtqjEoYnl5eoa9AYlbMmke1cKeSyalTd2NXOC3kqlNi0mQaCFK51xlPaS4NzG7jaG0MZomlBmRM4e9PSZ4niY7ft67-brGfZhR2RJIc9qYClyPEnvjsDp2-0WXmjcCGBQ5FVUHoL7OUGDAC88lw1g53R-oP3Ir6i-916cX7W050RHvmou2E7-Qz_u4qkARG5nSQ-OECjqQV3qUEO8rqFg1fu8veqye04B9WvoZO1wCRHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E657xKPSlvwUs3g5Pd_me7AjLmslU6LuNdihlpdvs-VELdIgdog_Vf7g-WdMbWcAak6rOsV7vCvSZnucIOmz_-GZJKUjwZMoQiOafzknugkhtqjEoYnl5eoa9AYlbMmke1cKeSyalTd2NXOC3kqlNi0mQaCFK51xlPaS4NzG7jaG0MZomlBmRM4e9PSZ4niY7ft67-brGfZhR2RJIc9qYClyPEnvjsDp2-0WXmjcCGBQ5FVUHoL7OUGDAC88lw1g53R-oP3Ir6i-916cX7W050RHvmou2E7-Qz_u4qkARG5nSQ-OECjqQV3qUEO8rqFg1fu8veqye04B9WvoZO1wCRHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=N7yydoYHn0Rs4uOcsUhS8B2Hr9sDqwGScVGznp95b8iOr2ttjRj0Z2f5h21asfsK_v_Ng2kjrKpqV8J2Ms-WAa-AwEeEFP29SvXGuaHxLKCv_Hr8uq4WvhJDKSXl5SWNYqCL9ZPuyGlzVIMgL8kLTEl_Qx0ex10euCZ-xj4E0nfPUQXw-pA4N-0jJNlTATC1mGDHvStXfiCjnO008sNaeXg95arSvketpiNLQ9P0zPyUZVDzFLqegS6aZbV-YXJBsmzU9QP36ajQ1WY0U_4wjnf6M5Pg_FXmcnJzzzggTLbD2OSpKAcg_ZcMWteWRKKFJoKkz4Chu7Hi7NiU54LkyYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=N7yydoYHn0Rs4uOcsUhS8B2Hr9sDqwGScVGznp95b8iOr2ttjRj0Z2f5h21asfsK_v_Ng2kjrKpqV8J2Ms-WAa-AwEeEFP29SvXGuaHxLKCv_Hr8uq4WvhJDKSXl5SWNYqCL9ZPuyGlzVIMgL8kLTEl_Qx0ex10euCZ-xj4E0nfPUQXw-pA4N-0jJNlTATC1mGDHvStXfiCjnO008sNaeXg95arSvketpiNLQ9P0zPyUZVDzFLqegS6aZbV-YXJBsmzU9QP36ajQ1WY0U_4wjnf6M5Pg_FXmcnJzzzggTLbD2OSpKAcg_ZcMWteWRKKFJoKkz4Chu7Hi7NiU54LkyYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=TY5Vm4qKBZZpSFcdSjYNP5ATuj9C_UUNlQTnv_T9qR3mULS9tlKZamcwboqjP_RfpP1FK0oAcqp-phE7D0m3hCIdmXmnRvpLaYEBWEvsf4yKB4D9_DtnG6CPwyW2PQErva6mWe0aKHdPLyQni2VJuNgDnI134UaW7_7wIChH8zYtQGZKvyNccIQ16CMjMrRw2rm6qUekqR6G394tFGUpQp6evEgiPwDO1HrxY5AiCtpfQxGqMAGqnOeiQvPqRsvPCZCRGO_3cz6zPXSjjl7iOE_S91ri8XindYg7oBVSuu_gVumY5Q1nPf5t-itFYIKkJgAVgnNpcWazV049ZLzsvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=TY5Vm4qKBZZpSFcdSjYNP5ATuj9C_UUNlQTnv_T9qR3mULS9tlKZamcwboqjP_RfpP1FK0oAcqp-phE7D0m3hCIdmXmnRvpLaYEBWEvsf4yKB4D9_DtnG6CPwyW2PQErva6mWe0aKHdPLyQni2VJuNgDnI134UaW7_7wIChH8zYtQGZKvyNccIQ16CMjMrRw2rm6qUekqR6G394tFGUpQp6evEgiPwDO1HrxY5AiCtpfQxGqMAGqnOeiQvPqRsvPCZCRGO_3cz6zPXSjjl7iOE_S91ri8XindYg7oBVSuu_gVumY5Q1nPf5t-itFYIKkJgAVgnNpcWazV049ZLzsvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFG7c0GVRH9sfUGf8LPPY52rF51eHtp9B0U6E1AQqjCMzFZT6T5psT8A-VwP448CF4QNZc00knS1e9uIMfV1RNRrP-UsyNp51WygeJl4XSSnbI-IRGs5RZViJXPTWVrEX19AFLavy2573A9-T1jcJLyaHhaSO1aBxcmFUYx-KK88TBE5s631UwsjsUtQREn5KQt_QliobZeofTXLo7Fgw9ObOyJ1McBB8naR9-ykFBqMDlg36VdC_EearkuC3je_J-FYBckjg0as8btj3-1ykZV-1qUXJfZ2ffrzGe2pw59rkmaLXQxkZBJZ5hDhN_ZTs4vo05RMt8WB89d9eF-FVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT-Tm1nWZMh2dZRZNlz1S7M03E0OgoLyV0x4-3W4YDdASVR6NjsPu78S0hPqW6L95c7hnSsZaFjjRn22fnp-exBHwGD9T0H3gDYsObR_04ly51DBIfIl8iu4nKEsRgVQ7be92eM51vrJYVKmdq-Qsd5OT1UFhLSab6eqvyUJpOH132g9_FsCU9HF7xb57YE7XxUO44OPTNIJr8tWbOTYnaECVXv2Mx3Ze6W_3cEEWx92C3KSV0S8tNSE516USZJqO5qKQKwOa-21rTRD0IqJEBD2OPVccYkSkVubrerjvTsLplYtAfx8XqTakd9_xRSkDeQC_reUuC2Dl9U7MksHfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSz5520uV_U9nYBfsTEePRDoSjiPM1PXVh3FGEE1aeJlmde4BdnTJmlVEle-l4d9Kxthj_X6o93VZXN1mjiz6DsQ0RkaDXv83_NKxOhfkRLiZNR4YRc-t3ho1x7ItpfhQ-sEjtosn7AWcXJCVvEiOY7bLUpZ7XRVZQGJvGUY17pXCLWVSHdvCFW9jXdnyhum1ARgfpgGEUaIWITfY0pkTG77e3VGysOl3cJmAvQK4C4AwTs7a_rkyNmk1vB8J7BlBkPsiOaG_fUreB4KQuR7KUoSmFZ-UVt7kU1cNmfqck5RC8LEWbZLrYBvZ3tMh-CjqvliKUW0MC0R7_Zm5tvXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqAGxCERj2slzRI5q8nHwiYg5nz-DK9VDla9BcBSQw9lp3QVVH1sRenTQzrf-9JkpMJo3t59gqbUHuLr0HOfp2pc6RRoVrjZORs6NFqwmcTZgc-oVKn6z1EkSBaq-rZacc8LZLm2ZBEpw_L3BoYJMzfrTVgBaJZT09CrILmtenzR-efCHOY8cr2r2rCbCY6guo9w2zcm9HRNpcl9fqCoadW7d8lt1nXzGO8ctp6rHKpKbCQRgDoj0_oQ8y1ZBa6bgqwVvn5aaQCP7eaHl6Kw1YyuqwQvn8h1zA0_ZVef_KT4kdyp2I505P7DAIuD7ES_IETJskc0XXG-LF64oPCcsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSM0smdVTymvoZYPHv61RoErnOfc97x1ZiUrlopFo2FL5UJ2vddUdWcKppXjd-LbP7d-zeAky1YOAly7RtKTbf4rnUyTO0NmT3n33HpLdAwal8rPGc0QybSHnVLr-DCiApUFw3rwvFAbv6_9lxPIsNScfxxTJFp_FJl8GoHtQ5-bJeD5dTI7xWznWIS9816zYyTS8FO7tT_cQ7XJgXCOA4fVk-mRs3fXptAdR-vXQUiWIuhQcEAb-mE8TtzdOAPJhJCJLNbauSynGrTWbZmCsnUE3k6ioRqfpYYBJ27dJykKLbD4MPkoAoS-ZpGe2hLsj0A7WUS87n8Q17dE-IMnOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=pilDHL-gfhpFAQWE3Ca0NYMD5c9wz36Iy2e2YJlQLjLHr3xyfqe4ZNK1_EYXbuF1_ogAwr3rKeEFw7Ubadq1fRDFVfVEEN0nXE45b4V7UH0_iZkTdd4n1EOX8t5cNxlvUold3FcoQykEI6M7q3prbaA3hRGdavMAVKFsk9cSCucvG1cEUJSgUF4gbgtCQqJ1-6V-2QFdvURwJLVGrkWgkqIRSMVAdpz9pNKxU5Ngg6IgM_VZ6jY57kKN6aPMPjmPvOBaamUL27g6gAtg6IspfE7_xBaMhBjIpRcN88LMdpqkvyw3b9RR8tQ27nFK9Q8TRzs2HVl36IhCdhDTPIYuqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=pilDHL-gfhpFAQWE3Ca0NYMD5c9wz36Iy2e2YJlQLjLHr3xyfqe4ZNK1_EYXbuF1_ogAwr3rKeEFw7Ubadq1fRDFVfVEEN0nXE45b4V7UH0_iZkTdd4n1EOX8t5cNxlvUold3FcoQykEI6M7q3prbaA3hRGdavMAVKFsk9cSCucvG1cEUJSgUF4gbgtCQqJ1-6V-2QFdvURwJLVGrkWgkqIRSMVAdpz9pNKxU5Ngg6IgM_VZ6jY57kKN6aPMPjmPvOBaamUL27g6gAtg6IspfE7_xBaMhBjIpRcN88LMdpqkvyw3b9RR8tQ27nFK9Q8TRzs2HVl36IhCdhDTPIYuqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=UwebPz9Hl4TG8sNJrgsvzs7-akWeYjeBYLj3QDZahyJieWB-PGMVGcQHVt9vWekN-aoOL9cWUVjc1pNs9-_7j4LY90W3R1chAGrKeqFv03ZS1a4wt1L2eQfgoTNamnm8t8GWd6jPQZczHlWyKIi-sIS4Jb0tcjzrrJziasx1Vw5a2J156C_J8md7l0nseqEEzZat5QZREmy_O4Ud0Z4wdYigSRfIXE4eSP8HqRsHPgGvI1yvIL4H-AEy_yYA-A7RecUf_8WlonYZLEgfeuJBFDwma-7E3evJFUPp0KhX1SPSVvDih6RRt1ONeDa3BlS2EUeAMWfPShZsnocgJqBArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=UwebPz9Hl4TG8sNJrgsvzs7-akWeYjeBYLj3QDZahyJieWB-PGMVGcQHVt9vWekN-aoOL9cWUVjc1pNs9-_7j4LY90W3R1chAGrKeqFv03ZS1a4wt1L2eQfgoTNamnm8t8GWd6jPQZczHlWyKIi-sIS4Jb0tcjzrrJziasx1Vw5a2J156C_J8md7l0nseqEEzZat5QZREmy_O4Ud0Z4wdYigSRfIXE4eSP8HqRsHPgGvI1yvIL4H-AEy_yYA-A7RecUf_8WlonYZLEgfeuJBFDwma-7E3evJFUPp0KhX1SPSVvDih6RRt1ONeDa3BlS2EUeAMWfPShZsnocgJqBArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTHOxFpNlTgOKPOdWA-A3mMGtjWzZQ2ZmAND724EdL1VDKAza9UJSVRTFlMEGmobMiGAFmKbzejYCJKcoIYyUSX15D8Eri_VdUSPI2EzpDSpKbQh2L2CpZADBGX_U8jqDs8WbIeVNK-hJGMG_Z-91Ch-k55tfouGWWL8htJ4CUdxBk4MlMKGMdLUxXVNi0GeAXC-h_IwAdIeL07iCKPRU3mw7C8yzuVjVsUgRH70ozN2MlsPjaaBShbNamY2Hn74QDWvYMgDeclxh0wW5AzMoBjtOaDZRciwNIBNovCmhnRJgpKl-Wae1xpUJvqNTFKm3qJ2bK6NgP8OT9C5P4MdRA.jpg" alt="photo" loading="lazy"/></div>
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
