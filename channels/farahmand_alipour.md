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
<img src="https://cdn4.telesco.pe/file/CxVYziccE7QQdPMQFPvmFi2pu_OiZX6YLvLe1wg1BKT9WuHVha8UzFYOgy7ZQY2oPh2Da5H8SXxsatQu246MbzsH55hvfcyMAs26aNxmqajS0DpnxnlGWn6q0T5Rw60qXwpdIkWjo1pZeqGJ6Ra8FPN7QVEzmn4QzSGPLMFb7120Kg0jxWQXx7RsZNUvG9M4jaKmE54_ML_XUqSntXZkPG4mTOo0EcDFaSCZUo4KHp4lJxLZ4uziPNQqABNXC8Q1NXeuo6U2aqh7wLIYjRLQO0TdXMT_r1VdpZeIPmMp8H0EPSxGqfJ5tIf_y-OMhKw9zzEFWbJNBgY575UDggJAog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 03:38:05</div>
<hr>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBluMpeWmucJSzzAooFM616mkHEodXip-V0Y1Qwlyn5ot9PJMhH2tA46J97Gyz863Ud57K6EY95AfjTWBcd7JJMBf8bnDDnqnIMjvqs1uKiJsxgOdGvhFyHSyqXkrKajXfEb72BdoUf_lIxClTHavh3wafhsT_eP7douYJXTPhJ82qQAofvJZ-VvpQOhqTFg2Cj9wLJQleRl5axsBQ20hRbFyJQyt7s40bMZSpQFN8a5GbnZEG8fUjUhAqoGzJFddBKiyEWOMurXVrfiSo64FGqCVCo2opSn1TbKVHnwVYVlBennQEt0_c6l0T4gqng_X_ogWUHVybvYLVq1-qbE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYci7xeyfH_vU9ObdhWhq0KESqGliaaSRJ6O6GC2RqILJXCiUD_yRaSTdgZmcF3578doB0k4UTOYazdMu-HphHWiIp3r4NUwmEkL2_4cwgp7arHAABmFg6OFyBFiEN-ltTbBfIt1alqknFTUfGf5YSSBQCuM_Nzy4ZZ57nOWyrDJd_9kA2Lskf4b46kp3-Bw9As-z66F7mEiS2CwXze13GXSfXOAZccwUY9FKz3kqxgIajrvyD9NdsNmeB1hrJAR3WYmYv_HSs6LdH1twYRQPRANpQBU4QJ5io7odo9mWO5rF7Uo8TsDDIYP8VatVborB4FhZcKinnYM-T6tQ_0vjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=r5q-glFWd9YyhnIztmDV3SA0toeJM9X7BpqYd4qGMOLreXzoonWQVV1NegI7htdCm7bMVIKE4mQvL3eQtWbGIcfLYtpo8l87WhJJvTVLm4fx46SorNAcIUWeuopQ8JVxqlRpCfFteSh9xNx3eEnPAnWLBIio2_H6ZxocXhyLgASND1ScCJFqO5H8rPEQ-dGFgAWyPXt6euzXm7HOM4O-Ex8VrUoYWeQhQ3tHPIPWdRFlqC8KsvYy28yF9n1eL1smxekmOvQQbRzLVguRXtsWDA4Ixsm7wdY8jdHDz8vcVbIUWPAbpfdXOqxXFi81qNGkg0tM7zu_lpQIHHW-O0qXKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=r5q-glFWd9YyhnIztmDV3SA0toeJM9X7BpqYd4qGMOLreXzoonWQVV1NegI7htdCm7bMVIKE4mQvL3eQtWbGIcfLYtpo8l87WhJJvTVLm4fx46SorNAcIUWeuopQ8JVxqlRpCfFteSh9xNx3eEnPAnWLBIio2_H6ZxocXhyLgASND1ScCJFqO5H8rPEQ-dGFgAWyPXt6euzXm7HOM4O-Ex8VrUoYWeQhQ3tHPIPWdRFlqC8KsvYy28yF9n1eL1smxekmOvQQbRzLVguRXtsWDA4Ixsm7wdY8jdHDz8vcVbIUWPAbpfdXOqxXFi81qNGkg0tM7zu_lpQIHHW-O0qXKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=VRTy3IJb2l84UCt8ydl1KtHU2QVvHkyzRSPqKjcJzgWTXJCW_kJSJjJJyXgPGUQwQdqiDONXoIanQKlaRNXNxeU6v1yynknpZfozBWb5b0xJxO6XIhNyuDetY35yObGugsVGVKV5FoACd_b_c_M5WNeJQdB7Ew69roAKjL9Xpy37husieWfq7xqQ6SMR8qbLxp6L2LSkeP728TalBLic9Z0_Y_oplUx1Y47P1yA_2CZI6nuA9Co-RcEGY2qalgHHZMy6_jZM7ewaXBMHX2JvGv_IfAWEn54InHnQyH7AJuvg-SqVn3z7pg1O1dN2kt0UbWtwUW0DQj98qJGPLFAQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=VRTy3IJb2l84UCt8ydl1KtHU2QVvHkyzRSPqKjcJzgWTXJCW_kJSJjJJyXgPGUQwQdqiDONXoIanQKlaRNXNxeU6v1yynknpZfozBWb5b0xJxO6XIhNyuDetY35yObGugsVGVKV5FoACd_b_c_M5WNeJQdB7Ew69roAKjL9Xpy37husieWfq7xqQ6SMR8qbLxp6L2LSkeP728TalBLic9Z0_Y_oplUx1Y47P1yA_2CZI6nuA9Co-RcEGY2qalgHHZMy6_jZM7ewaXBMHX2JvGv_IfAWEn54InHnQyH7AJuvg-SqVn3z7pg1O1dN2kt0UbWtwUW0DQj98qJGPLFAQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUO-pUzMaQhyGvsVujnLlAHmpDkhsvFrTaqCh9DkmnmCsAbGyGLq9DL595ItFJIDJw1pR4MvB4KjA3Zt7HQkRySbIPNN-aeZeQOORmOxAS9jkXu93J1insljMEZEattNJ4q3QZ8rrEUb2mIyz0giVklh5mSr9cKaDRhPpLnA3n0PrVZn4e432GNZdNFWesui_QI1ZCtWRTqMI8S7UOIZostbjSesRTEyEDW9EMBQzbZOvhQ8r1STTy_WuNWQh3bHZFPXJxr8djWMMYz4jjXOLal6rZXOr-E6SsM-RtlDxx0JsMMV-UHz3qOParzNOvAx8gaqz0MRrgCUERr3qj870A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNTLYX37coBYYr2-M65ZDfLxZMTDds7YqjIRIMnD37nxU1k_bVtYIZRPd_upxubbKUmjHHR2-AbO9j8-WOUZgfN4yPxGPxGdBxHyfvl5gqMME6ERhkMvbjpKQfAZxbmZ0AC3-IR-HjjiMrz64GT9vuMGg5wIS1Peq3PNtC9KP7ailPhIU7PYIWr_rgtesZMNCcA4CWPYImQES4I_ncFXyP7olUCF1eKNTQigWC-nvLlX8voRVs0mT3dtcXignk670z6i0eactzcXLCFHKkVUzkClLUvyfi1bNaUUhRXvKCBMtYkF58VCvxpisrjp2bkxe9GuzkCGcQMn0v92S2N3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=BGonb3s3FfGB-be2eqEslvJnlMEPmMHk_OHbREWBxBeu-XD7vBN6o17DKW3LiDDM3NAyf3MMRShpRGWSfYa32E2F5ULSZuVA0AVxmx2xy0J-4NK0VdRsaLet2ZNtt060WdtAwYHO-Jo1xTs7HyLiBEHNQyZJKvsTmd6ILJu5MQ7oNdl4pPfuw4yVyQNr0MGbp43yHlgloUAGKxNcLE2ejgYA_l0Xzo1Un42YfMmFaRxe-Vr2thskfFzXDEsgIH3W8aDvJSWYkakvl4SSkPac-ZwD3dGZH7eFKduzgcmosCQdmojqHBMFjRaFsXC7oRA1bKzohB3pgCQiCspHPu-qtgTIyUT01y40dfifLQnRaCmu1E42VaNtq1f3yYF3H5LzU5AWPRSTgUN2s4Ivs83hrNVRChmRgPPnApY8Kej3ui77WMV6-8qZXxYfSgEVbftrLPyDVl_2GMJnx_yO_EP9ntsT3V22ACSclws2M5UucyE-dq7uu5VSDKKHpt0oFeuBvhdKsa51c6ALkp6nqde213GhbU8YV4Q7orkwMdK6Mn-w0wCv46fiLNLAFkLBMdxUJwkVLL_OB7Wdr0Uhndwt_0RkC1SOWQiCdeMkB6E2PBBnaE3V2UgzmZiW2H9cNik0hAcJ_fpvDYCnUUNcDnHHa04zrRM8bjSgWX77o5yAZIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=BGonb3s3FfGB-be2eqEslvJnlMEPmMHk_OHbREWBxBeu-XD7vBN6o17DKW3LiDDM3NAyf3MMRShpRGWSfYa32E2F5ULSZuVA0AVxmx2xy0J-4NK0VdRsaLet2ZNtt060WdtAwYHO-Jo1xTs7HyLiBEHNQyZJKvsTmd6ILJu5MQ7oNdl4pPfuw4yVyQNr0MGbp43yHlgloUAGKxNcLE2ejgYA_l0Xzo1Un42YfMmFaRxe-Vr2thskfFzXDEsgIH3W8aDvJSWYkakvl4SSkPac-ZwD3dGZH7eFKduzgcmosCQdmojqHBMFjRaFsXC7oRA1bKzohB3pgCQiCspHPu-qtgTIyUT01y40dfifLQnRaCmu1E42VaNtq1f3yYF3H5LzU5AWPRSTgUN2s4Ivs83hrNVRChmRgPPnApY8Kej3ui77WMV6-8qZXxYfSgEVbftrLPyDVl_2GMJnx_yO_EP9ntsT3V22ACSclws2M5UucyE-dq7uu5VSDKKHpt0oFeuBvhdKsa51c6ALkp6nqde213GhbU8YV4Q7orkwMdK6Mn-w0wCv46fiLNLAFkLBMdxUJwkVLL_OB7Wdr0Uhndwt_0RkC1SOWQiCdeMkB6E2PBBnaE3V2UgzmZiW2H9cNik0hAcJ_fpvDYCnUUNcDnHHa04zrRM8bjSgWX77o5yAZIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFs-dYQ89SSejfvnyaPCtYViyeH5hORS_Wjy-HF7Xq8oiRkMX3iZa6PwitdwNXfCcWg90OVoAC3R5kmmMc7jj6woNEuDFvGKFYxYjv_Fsk47kBE4fFcXWPKfeOyFFVZHDIs7s58tU_KHDS_B8jbV3J6b1B3vAx9OMUMQDHIdOHKKsa5Bi8Di9JRZ0ZVpircgcnsbdBupPnnxeEKF_u-wj7ZvZHBD4-aA3RlyGWFu542kPseaBXgADPOZ-YWJ_WwNNudxKJzXX5wgUrUgHR6UORBdJJdpdY61GgxFVsCR2d1NDowUniyn8EWUll3zVDIX5FkaMAAwiY6dG6vseKwl8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhoyKScEE5yctXHDN_xUPfZ1PDSUMxpBU2rsqddcVhs_32wjw209rAeKqwBl7OcCrOUe0a9dngMijH8mKBZng0GcIvDReCo4E8_IA2Jfh1FBnhTAb3K8NTNCD-GcKaI987xOoOIR89g-V6VE5cfcmntMjKojvQFAaS3V-Fo5OfuIxSk89crnVdo6MO6okuDitVXgq8bWV86JHampMYFowAZ90GsUKHR8cGcnsktGzeGDl34aFHG9nqZiOByRIvBclu7_T_mvNukpQHdwJFDDwO5i53szhhGyEOgFN0kBUwG_aw-DcnrAlTB4Labt4aXLlirUMUpm1FyloISjdfUvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnsP3erPlOpmRmvqgYFxaIORv_ly9njSuTTyn3erl7v9Q3RD8MpHt2RBkP2NcrqUSU3UabH8GlSCSLHhWICZeGGeDyU0Y65yxat73MGtTBtVnJWBGrgzuujxvV-eHlDB1ChMftvEcBHW6AqciZss99_AJrJjhgFY7FjuarIOWrn16vZBik0Zxk8Wf3CNHmo226nJroYhBNx1LNJfRc7NlQU2sOZPk4jMUW6XUmx9ytUcn6W_85z5SkSFwW_o2LNtV5J_Fv903r_AyK8n37IXK13lecCe1LhZ2E3BPQvOI4LxwWW0q5ExGe0_6vRxt6fO-Vl789Sjfz-bS3PdxUYJnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HReG_sp4SrdZOcHD1ZPrtjMla6fg0WN7BXtembhS0RfKmPhGODGQM8G-Z-n3KjF4OdYYtVcmQPW0DsK9M2RJifUBVt59H6_vVMb0ZGSA-7Ji5s-J7a1giUcJ5JZGt1hSNjxadPin6tObJdk61pdX0J3GWXIPXGkx5XcIHFSaIKhi5kYW3WZvLWuUMno7tDAj_CNVNyQr2i1L2wKIBPd-SMBXhdjKrOcP8xsypPNRiqDfnl-LnhypKZ0A9ZrFckEO2LT3_IU535XRBc0c81nOXpIxDeEL3WPcuN7RDc1MdlTxAtf_NLCo-SHsQTgFmlRb2K_Wau5enS4KN0sL59lr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNHWeFiCw0xRski1PTgluOJoEz1R1PiiqRHIR8oqvhwverZ55QbxhvYvSDf0V5CNUCne9YsNgMuIf1NrWPEcSxERQ2eR9kLQE3wZA0wjnueT4Z4o2P2hoov9KKuJbwxRkO6Om7HzpLKAN7mLxERnD_2iDgXHHplDEhWRzctnAnVTpkNaZ46zLMSENjlndrID1McMV3NAlFevo17Z7qz10mvXfMIfwACEzbESsvrva9xKX7JJOXM8srGw-CL6EJfJQyCwzbdV4YphnCmpEZoL3EAR2ijvBA6o1oMtPl_5JyGBhsGLs_JraqLdzCuJ8ogPBoD8Y4VleKWqOoX-y3XHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_QNbkShFkZkGKz29TMZ4q-RxKS0TezL36L5xf8cPdqLYc9jOQwYKQsDmWyfTaCe8IReNLryAtj1biRGZx8eC27C3_1w52aWrfx_odtQqmZw6i3QOh43yQg_DZcd9Fo0X08FesPOGNEPHkfBE3Saf__Ofxbd0t_pewKowHyNdqs3zxKkeVd8xuUSSyuFp1vNs115kjJlbcHl7hC2OsUY4YTVPpCphee5TWKi81wQSCjtdvBl9Y9RyQzYozME061oEnZCa39iglRADMgfN-a7p1ccLauqkAGsG1Qxor5dVjq6LNOdBvGrDREuV1BiOWotqASm_5-6KarQDn1Z-u-U-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=TNvfcuEalLWhdkVPStQzCHyKWuQPzaAH7kKJcyA803Qet0WfeDVzTHY2Pjc18TZFNAjiQB8DWQ5DZZg2HCbqNleuroKOyveIOkNdMg38XsV8Moepz6MTsnxNX3ySfDhOumkxRZJ_gepDamlZooe_aoobxIMK0BNvpzoQy7VtcoGzRriHsSmGuArLYzin8x_XD_H0lgekfP5XgG7QI3lsqqzvVZGfjVAVf4197wbAjIc7KoQPBZKNMMswvejbBOgq09TC8AFrUaqLNUqT0KLoBnjp7017NPBJ5sWYPDuDguUMff9ZZCeZ_wIojOaFvPQCxZB9ckQUEHcqT1ISDjxXWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=TNvfcuEalLWhdkVPStQzCHyKWuQPzaAH7kKJcyA803Qet0WfeDVzTHY2Pjc18TZFNAjiQB8DWQ5DZZg2HCbqNleuroKOyveIOkNdMg38XsV8Moepz6MTsnxNX3ySfDhOumkxRZJ_gepDamlZooe_aoobxIMK0BNvpzoQy7VtcoGzRriHsSmGuArLYzin8x_XD_H0lgekfP5XgG7QI3lsqqzvVZGfjVAVf4197wbAjIc7KoQPBZKNMMswvejbBOgq09TC8AFrUaqLNUqT0KLoBnjp7017NPBJ5sWYPDuDguUMff9ZZCeZ_wIojOaFvPQCxZB9ckQUEHcqT1ISDjxXWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Zfo39ouLa4W29y-UFBS7kF45iMAIN93yF2wbUHbfFdStk5BQ9L78Z-zOvKW0QwcIZ8ZjXYOPTfrwZI7D82tUKE08jDdw46rO3y9h0gM1pgmIQwDC9zG9yvMpQfltOaPOsMpIHfhzr7qz1FkjJoY4pxLJ-TfApR7kGNiMznhREpfbZk-KqUE0adJKcChlbqxQBSTotYZjXcW3lXaLIctp0ZJwbwS4Kpp5i3tauJWlucIR_EGcMwMUunNlOMzIMx-S1Ry1omClvRyLgwkUWP7on3qURJ97snc22H_e8KGOM1SSqS7-6OsvC2vTpqkKGtV3m9mnjdKckAQh9LgJuIqKwi8Jou6XHTu-qmcYZK4SiUrURnrxSFghgrVveuBnJLoTdiI_R-fuApDFVdkCjrxqdKqq5BA_x7bR0Cg55Me42UVzPBylZbEDD4TmjCVewK02dX8HWiGQ6GKYOz5WIKOMORELsB3oaEw_OCo36VL2gWzx7vmjdTBzXKvp4WGMjjnfyOxTe6EPeeLZmhF3QMN3yoBbAP56yzH4kEvL-raso9EZrLcSQmIVcbJstpYTDqoWuwXwZCz_QKCzNChPDze3PmnMG52roe3zp4FkEgRyfq8fE86h0uNHnS3TWdLgyI8xmNbUw5_Lkze_Ic_YjKYFIwLKawgMqkNzMOSQWXYRkgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Zfo39ouLa4W29y-UFBS7kF45iMAIN93yF2wbUHbfFdStk5BQ9L78Z-zOvKW0QwcIZ8ZjXYOPTfrwZI7D82tUKE08jDdw46rO3y9h0gM1pgmIQwDC9zG9yvMpQfltOaPOsMpIHfhzr7qz1FkjJoY4pxLJ-TfApR7kGNiMznhREpfbZk-KqUE0adJKcChlbqxQBSTotYZjXcW3lXaLIctp0ZJwbwS4Kpp5i3tauJWlucIR_EGcMwMUunNlOMzIMx-S1Ry1omClvRyLgwkUWP7on3qURJ97snc22H_e8KGOM1SSqS7-6OsvC2vTpqkKGtV3m9mnjdKckAQh9LgJuIqKwi8Jou6XHTu-qmcYZK4SiUrURnrxSFghgrVveuBnJLoTdiI_R-fuApDFVdkCjrxqdKqq5BA_x7bR0Cg55Me42UVzPBylZbEDD4TmjCVewK02dX8HWiGQ6GKYOz5WIKOMORELsB3oaEw_OCo36VL2gWzx7vmjdTBzXKvp4WGMjjnfyOxTe6EPeeLZmhF3QMN3yoBbAP56yzH4kEvL-raso9EZrLcSQmIVcbJstpYTDqoWuwXwZCz_QKCzNChPDze3PmnMG52roe3zp4FkEgRyfq8fE86h0uNHnS3TWdLgyI8xmNbUw5_Lkze_Ic_YjKYFIwLKawgMqkNzMOSQWXYRkgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip3j9v-jgVO7ee1ielNikJuBY0VMZYey6IHDi3KgOQ-Lp_i3DIVEeoRSz98J_n78Le1t6v9tJXOYxedR4TIrtFvkGSh5HEaTJj4F_Qpk4bLYvZDn00ix2srK-qinjHT90macFWYopC0L2FRisYt1qF4-FbQSR2WqHKim-Ho-QqwiFGur0trOHo2i9GMM4kkNLcK4WYcv-vlObXLbpE64oz_c5wauhjMyz5Dn8aFR0EcYKU2cYu0kJD0WoS7D1fYS8wTB9oneJWNpcvBFo7aiCgAWiByZ18aZX7rItfNij5xMi9C1XMnSd3biGhc8LOu8I47UFh-dEdC6ZghfcAJa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6idStY67iwoBEbxxV5HzqpdkXXFyhCrLKh9A1G8YNPfZsgH18hoJxkuXtw1fRkWIKPSu1jqhPazjmbHd-c_IvJaDmIm3KJQWNVG-Dt-R37fkQmDsP_YU2nfFPKYE1cALljP6Ng5IXpdDsXuWcpv2BLZe2BZnNe_i9mfJe8Mx-XyRAZqnwBpl_gXpFGlSsyUur__Q9TrDVXkj58E2IBQEvw1GGf0aFANfFD9E4-71_-GgvtqFaxYf5MAHpKUjGYeafJ63kRozcHOKRUrKFz7UBziW83U9QTlI-J41FFGfDKF-ZiridvsYEyKyA51ZrV1uCApnFY5qPnXCyRM-b1Zrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTvWXH07lTHung0Kl-mhJ30flbGHsk9Wm0wpEfYNxfvFlKB-ZUXM488pBVSJ2mqU-Yc-n5ZlDwsgjJ4Pk_0TJTl8AbQBfmQCv4bhBT7EQftpHxWnH0WvKyAweUlXtD5OkLDAOZDmfzRU5giPbPiExfKtxPv-p1IWJ988KsTjm4-hzTIeQNH33n2IvZIuwC1v1QrCIWMy7VxisiPJTqTFDI1LoZCK7LwQf8FdDGVlIDxpZnsvpyQfCkiEkg6p95c0zhohG051cMZyD95DjHJiheoCUGTbd-PPLUQqnvywwWvPIGwucq8bort3G_mqrpzcG4HHktjN1n0_gh6Nqn8SAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=tKzeIoDL6FnAtOekZuKa6eeIsfbgciA6qDWBoDoZFVkLgBsUHl6qKLadRyHsaya07p-C6QFrJrSyc5SuhUCSrtiWpoL_T2C1f-w3LhaFB6STzhCJEuiVyDxuKD2ifsSehnFWJL7cgYuK2M7o84QMHKdF7lg7P4gKbD_MwSdF5vQYOICydWfobGvZdZR8yXchbvxGd8FnApcHvOX8qxJdc5LGeJcFVW9BgBkOj0TsNa5VVayNfgo39LjK6k6CSOClTeqstYCdh8o6gMQu_QtulraHQ87RW_lLfrPk3q8SRFoezaeJw-Hdu8rUw7zPDR2n_AdtiBa6CBAhUJC7dFgtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=tKzeIoDL6FnAtOekZuKa6eeIsfbgciA6qDWBoDoZFVkLgBsUHl6qKLadRyHsaya07p-C6QFrJrSyc5SuhUCSrtiWpoL_T2C1f-w3LhaFB6STzhCJEuiVyDxuKD2ifsSehnFWJL7cgYuK2M7o84QMHKdF7lg7P4gKbD_MwSdF5vQYOICydWfobGvZdZR8yXchbvxGd8FnApcHvOX8qxJdc5LGeJcFVW9BgBkOj0TsNa5VVayNfgo39LjK6k6CSOClTeqstYCdh8o6gMQu_QtulraHQ87RW_lLfrPk3q8SRFoezaeJw-Hdu8rUw7zPDR2n_AdtiBa6CBAhUJC7dFgtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=ub63ageVKhrWWomyT2RtYaElMrARSDIPT2Kr2ytEAcBDIMfJNCjjA2cMzT1GwvrVfahcgMXCT-ZoX_zsKFWdWYoSpX8arbqKsglfHaIQIpuZHaV75GXFKi33VStWxDQ2bPRS4NES8W8fDLXHW7mWq7fraQRIyG0w1_4XXCtBCUPvv_JnfmSc8kS0EIuSEKowxQk_DUbXbiv2W2WKuhMiCgwu2WTnJPQrNKNilrLM7sZDJy6UMP_cecnPEuokXDLa-KneYtOEaEOoPjeGnR3l-FOiy_KJlQOo_-aA86jao-4hEWPbkYTc0GnTrOSqDYLZ0UCbtPd1Q7zLBwOL6i-77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=ub63ageVKhrWWomyT2RtYaElMrARSDIPT2Kr2ytEAcBDIMfJNCjjA2cMzT1GwvrVfahcgMXCT-ZoX_zsKFWdWYoSpX8arbqKsglfHaIQIpuZHaV75GXFKi33VStWxDQ2bPRS4NES8W8fDLXHW7mWq7fraQRIyG0w1_4XXCtBCUPvv_JnfmSc8kS0EIuSEKowxQk_DUbXbiv2W2WKuhMiCgwu2WTnJPQrNKNilrLM7sZDJy6UMP_cecnPEuokXDLa-KneYtOEaEOoPjeGnR3l-FOiy_KJlQOo_-aA86jao-4hEWPbkYTc0GnTrOSqDYLZ0UCbtPd1Q7zLBwOL6i-77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8GhQvhbYIu20VxrZU3YsWWbBx6bgS3fpy3P-aK38pLVqYyarFNMrWhJhJtAW0EZRjsK7jg6sewhygF9h6W0Mc8rH9yPIk2iP7mAOqF7cVpxj6o50x8vKf0GGAmfsAUePd9vKOuXcy_tfHP8RZyG7x4HLZxEuhj18D0OkWAJG5rqn-XELhemYsgaa_bkV_2Kni50Oe-OtZBlSlu655GutswVsZ7kX0lkQ3ZCubmhJi-jbt-ijC5P3kBqiyymMC1Q6p5SmUWGTCrCVuzB4pwFv8R1d2EhP00fD1TIW5bz1KuckdOIVXDkxdVXvdxDFD1VlM-GxFU_l0df6PJXHTVGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=amN24G9XQ5uS_0Ow9jabWuIszxH0QhNo4pAKl7Vy_QD6sLtYZTH5VcwSfNZOQ1QLtp17fE4jvcFMIkADAYlbuiXTCbdGucl2uUQLHqlBrddVJMPnAA4fPslaK1kLZeWCTHzL67JdkH5BEEe389sL9iZ9pnqM2EpMIFOsat0K9GUXyPptO559JY86lWl0JlNe1Jd4HOxvxndFfShLgtgP7T0KEa6KrcD90u_eQnLJqQRPlohqhhqCLSnrgoPO0e3cf89nW5t8FjY87E2jwFzkzwkY7GSllh1qRxzBLguiJZ3DufDlU9Vr5u8hUjxTHZ0gCXFl41-9_N-CDjEhn6gqOJclegwKs_0KRzbc4bKhHznw_tspPK0wxwnO3BTT5HfORe3E2qWi5TTJ-JKeY0A7wwGmzRtYpiDal7KL93yF_6NUVcjou9VUP7uyLuS4UFE3G-tzjsxd3_TjkAxSAwBUJ8PZ-WhXmz_MgSFXN16xg-IGq6SDfQVqe4HkDlybTZbWPKXelqun-6vs7RobqDERXgmW7lLK_CLUKR7RmomhkvIjzqokxNYZc2QAqrk0RTPrpBSh6J0rcOg8WrU22mvKGQXl2oo-ezxi7nTF1CNng6vrZb8r8YkBBlUI5qwRAh9moDlzWfDY1xfXSqy-bZJFbfXNFMUzD53_aghBDOLL400" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=amN24G9XQ5uS_0Ow9jabWuIszxH0QhNo4pAKl7Vy_QD6sLtYZTH5VcwSfNZOQ1QLtp17fE4jvcFMIkADAYlbuiXTCbdGucl2uUQLHqlBrddVJMPnAA4fPslaK1kLZeWCTHzL67JdkH5BEEe389sL9iZ9pnqM2EpMIFOsat0K9GUXyPptO559JY86lWl0JlNe1Jd4HOxvxndFfShLgtgP7T0KEa6KrcD90u_eQnLJqQRPlohqhhqCLSnrgoPO0e3cf89nW5t8FjY87E2jwFzkzwkY7GSllh1qRxzBLguiJZ3DufDlU9Vr5u8hUjxTHZ0gCXFl41-9_N-CDjEhn6gqOJclegwKs_0KRzbc4bKhHznw_tspPK0wxwnO3BTT5HfORe3E2qWi5TTJ-JKeY0A7wwGmzRtYpiDal7KL93yF_6NUVcjou9VUP7uyLuS4UFE3G-tzjsxd3_TjkAxSAwBUJ8PZ-WhXmz_MgSFXN16xg-IGq6SDfQVqe4HkDlybTZbWPKXelqun-6vs7RobqDERXgmW7lLK_CLUKR7RmomhkvIjzqokxNYZc2QAqrk0RTPrpBSh6J0rcOg8WrU22mvKGQXl2oo-ezxi7nTF1CNng6vrZb8r8YkBBlUI5qwRAh9moDlzWfDY1xfXSqy-bZJFbfXNFMUzD53_aghBDOLL400" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=hH0Csb5u-QGAldyTMQVmSE1DzLsKmm4-vIZPsKYdNrDAHpQ9w_E24PFjpDkJ0y_BzKvlr5EkR31NWAIYYw-ak7E1v2r15_TXgjT45QjC4zQo7-R-T9kUvuygWLgWhBGvjfZEAWhsfhG_xrDlWUzVqXE1_49g2rusayPp_GdwO-sMVrIAXcf9lU9hqczVUVtTzCS6qgbgFzTRr1lGfrJypUUME6qPfYSuzHEojPo98lWaDdC_jtuMMBRP3Ur0OoUp_9fv_LF8vQ7lzgOkdtmPxBUdsfu67p237w4ooFXyytCTJ40U9AaQuKHsHkSPtdJWyoq-ARk6hSp-A97PxDgWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=hH0Csb5u-QGAldyTMQVmSE1DzLsKmm4-vIZPsKYdNrDAHpQ9w_E24PFjpDkJ0y_BzKvlr5EkR31NWAIYYw-ak7E1v2r15_TXgjT45QjC4zQo7-R-T9kUvuygWLgWhBGvjfZEAWhsfhG_xrDlWUzVqXE1_49g2rusayPp_GdwO-sMVrIAXcf9lU9hqczVUVtTzCS6qgbgFzTRr1lGfrJypUUME6qPfYSuzHEojPo98lWaDdC_jtuMMBRP3Ur0OoUp_9fv_LF8vQ7lzgOkdtmPxBUdsfu67p237w4ooFXyytCTJ40U9AaQuKHsHkSPtdJWyoq-ARk6hSp-A97PxDgWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY7y9jq7wBeH0T2RdBLsXbx-I8HD9G_qrZWBVTMxbBFTM-4WKNy-8jNjhY9lk0LyseZAwwS66-id4uVnQ8q-IrIPUN5zrF_O2EdMwl6mAy1KbGbnfMy7uh_KdiZhTkM4H-TkMJGUaJfKDiOnyi2m51ingnQuC_0O7juYwy2S4Z8KpqGwGL4etfonDE0tGC-MdiTcS7gathhhXlEdS2E-VlINe_7dlzBj2oLj7mwvhGGmmMu-mTs_ZLbcOTTPzj6XKClH3CnOYG7xUkCUAL8DfL8fFe5fZ2a0Osn7KMaaHCoEiBb7c2Cd19E2y8eHL80wngoqE2qdrR5DjmhNi4f3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=mvhMpxhe1hzOQnVMxPblqr6dqS6TyGhO96LHtzNygEQHRP1ATYFuFCr3FzIkS0I2LmZOuvUtADOnF-2hBmAxitSdJqh8jcRqaDovOOvzKOZkitD6T6Jy4LGXq_RwZCMrQqY0-UMgHG6LW9oy2Nhq1fJnRZKCDU-XX0_ZRiIKUCalsEJ_ybZjapQLGuiVBnwHduwTo5-vrDZRQVjBmhDFoCCwpgSXfscuiVN0Uib1lts37r5j083utMozcmVuoy_IJ8dnQWVOVCS3hr-RVooWnvXgS3gF2zawJNrvsLQdHH7ePG-nKitxhRZK_40CoNYiveP5BN-cv_e-zmd-myjO4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=mvhMpxhe1hzOQnVMxPblqr6dqS6TyGhO96LHtzNygEQHRP1ATYFuFCr3FzIkS0I2LmZOuvUtADOnF-2hBmAxitSdJqh8jcRqaDovOOvzKOZkitD6T6Jy4LGXq_RwZCMrQqY0-UMgHG6LW9oy2Nhq1fJnRZKCDU-XX0_ZRiIKUCalsEJ_ybZjapQLGuiVBnwHduwTo5-vrDZRQVjBmhDFoCCwpgSXfscuiVN0Uib1lts37r5j083utMozcmVuoy_IJ8dnQWVOVCS3hr-RVooWnvXgS3gF2zawJNrvsLQdHH7ePG-nKitxhRZK_40CoNYiveP5BN-cv_e-zmd-myjO4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-YDmO1guHgwFEDq86IHZyx2tXtQan1Nroy0Yl1GLJIGUAOuywR_I-fYbJaWoOFqHFsN24uIuy6ZKc4-b2vwMoNpSLCscl9XpTAWHcL-IIAXXX3q3IHaizIc7ctNBnWx9zq7msgfK3xeJlymEeBlI4xiRPWxM6b1TSTcHFfJO4z9uJG2xyeT7hfwxRVZhz-uFJ-2MKHXw5q2dEbnmnTXY7uuC3zpOMnx9cyQatkpH7C-_uJqGRJKy_XyU53UlAR1or4r0RodZnSQznaBjDNqT0IkEy5tiG0B3w1GWTrOX-fsU2MB4paC9IROAAbPF3f9ycwTRJD4K4WbBGz-DgQt1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPFTfXPKl8qU0a8Vst0PZF7KCBZhKMtqCRso_hFR1_qG8APh403rhIzi_wu7aEaIHylGiMIN9lr4aS9t5RjP8KKbrZugre3PRiL2tKefXn64Jw8PGxO4jaKs0GO2_zNKMyXgruIFFrf8b7bPyQCtXdbypofzF_ZMNn9Za74Mb9wQNLWdhv09YniR3qu7EM4JZf4-pPw60ReTL4PhIBHN_Xhx-n_ljpeacq-gHKf7Ubh3WhLbIBtSPfoXHKtN1YjZ4uDQtq7kZVpQnZx4gXiBw20OhEMDvvFZMQQSwSus42rpFz6M7NOhyfMWt_Kvahcs8OPgEYJFneMjvYYkZ7YsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Uw55rV3FReEN4Dd8Ziic_VRFYmhtKjrTQbQHQ2WWUO44TpjjlQhrNoPcqxyuOvqTF2VXQo2SRRucy9fQ_u1Lql8uL9oHGNuPUwqlSrCHSSoucoJYm4og6HBw_-ksok-P9iGlz4XHFiAktrUmBq--BwgbciPuf8f_iwdaaEzSToe15SYBmSaFXLTWmkuAVuP9JrNFYsmbhZCUO4rge_QD8Oul876m23yNp553N8omytmEvpCyoT86jBKmALaLXEEMFsG5zNP6VGfUm-OiZh2PA_9QdArHoadqYlTf6fq2QSj7gLJUswD3SAQhLbxVlsKbKK0y5_6oxO87cIAq2uwiADGhbzyZvABe9oSbSVuZL7-Vm0aqHslmCr9V6Mr1Sj4skrNqdZ3gmZoPan1YHDimB_buH4Qm_3hCVIm7ulWsdUhnILArtaBSC-Eq5KyBsFj30u9YQs_K_25hYMRQljwnbR_gO6Zu5pSM-7ObiqCaRkUIR54qQ3IwGeiRzxybxnDnfiTeQ7CN7FxG5I22bH70G2L8kIlkQ2t8sr9RbBgotXMYQPnmK6HMr4fW_bn0U4xOW94M5NOT2uqzJwDWZmX9Gcx3XdnVWHJm1JpIpgfbS2ldk_vew5C71bWSTRDTntDmj9cXkCHCoosYQQhkJCK07OJL9hh0lT7YQdcNTHfw2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Uw55rV3FReEN4Dd8Ziic_VRFYmhtKjrTQbQHQ2WWUO44TpjjlQhrNoPcqxyuOvqTF2VXQo2SRRucy9fQ_u1Lql8uL9oHGNuPUwqlSrCHSSoucoJYm4og6HBw_-ksok-P9iGlz4XHFiAktrUmBq--BwgbciPuf8f_iwdaaEzSToe15SYBmSaFXLTWmkuAVuP9JrNFYsmbhZCUO4rge_QD8Oul876m23yNp553N8omytmEvpCyoT86jBKmALaLXEEMFsG5zNP6VGfUm-OiZh2PA_9QdArHoadqYlTf6fq2QSj7gLJUswD3SAQhLbxVlsKbKK0y5_6oxO87cIAq2uwiADGhbzyZvABe9oSbSVuZL7-Vm0aqHslmCr9V6Mr1Sj4skrNqdZ3gmZoPan1YHDimB_buH4Qm_3hCVIm7ulWsdUhnILArtaBSC-Eq5KyBsFj30u9YQs_K_25hYMRQljwnbR_gO6Zu5pSM-7ObiqCaRkUIR54qQ3IwGeiRzxybxnDnfiTeQ7CN7FxG5I22bH70G2L8kIlkQ2t8sr9RbBgotXMYQPnmK6HMr4fW_bn0U4xOW94M5NOT2uqzJwDWZmX9Gcx3XdnVWHJm1JpIpgfbS2ldk_vew5C71bWSTRDTntDmj9cXkCHCoosYQQhkJCK07OJL9hh0lT7YQdcNTHfw2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlscyxECaYp5XD5mj2gwkSG82Pd8UN6oyKw31u2GqcY29KabfDAp1XYq4xtW2-xrKBkxliEJBnmTVIqy0wYoL92499lPlLQUjQsN3Bwzx8weGGj8YbR3ygQGV_qRf8fHjKJTK17B9AZjCkLKiuR59jaB8_9tDkl56OnIk3APG-QfDAeinlQj3YUkcOTTC1m8eu83-JwmZcZshLa1pJ3eBZmU2RitmaZE39YmEPFTgvbtrAm68VgE-4HYy5SwENA5txhO-2WqV_oWqnUHaCo2cXC1LTGwaNSvjv2mUdnOn-1G698iQRXGKA1pUhP_gWfJwEcoxOLMNxzI6JibSA-Y1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRcw4D_XiZYh-sm_qL4QrusSOk08x3rNfipmZGZvBTql3h4T8y76-YQa2rGawEdSeEDW3w3UKZkZ6H7ZsE1Cz-s2b-lvl0b4VtWE2iLwizuaD8cPiO7qqyIdKNd9U7QkLoCMiTQUz_q3k89sLO8XTcqxlPQzzQcmj6BbV5nsk3l4p4ukN7sMMcujWtJ_iGKjqUztajfbxdpr8BQc21o3iqEHEYtyBQIPfWgkmBFMhmPTTuMnttFMmbuR0ZwFdwJyRjdHKjBEGIy66N0-Uq1CmCyB9851sB-FwFt2Dw_rAbvnkapdZFeghpdTWM7gYPIv3rTlDmfpHjRfFDVP17gA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=erxtursZefZxkR9XFz_Vx9mD-fA_kOl_dAul9G9BGjoMUnRVnwfhIKiGCeOYz8juw0tzuddvPEkg79g6--B9M0-vd7zZ_EK9VlX5ptH5xNS9t_H3wRTy4Z4-1LJTnskzpzWR8_V3o-PvLcW5z9hlVF3wTh0ZNzaZJfupXbaL5gb-A9agV53qT75PcwQzUzpeAUYQnjhyC85vCrp4-vC8uwQwhNlgplrojRuX5ZdDKAWQ9mlFXZly738S5FtVq1EuSl0hh1wuTFCp6_hqUG9ok-aRCwxd7etMImJPq5UB43QKeS3DyFrjgxjc2UNbikjSLXY88jL9AElmgYUxCc1R0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=erxtursZefZxkR9XFz_Vx9mD-fA_kOl_dAul9G9BGjoMUnRVnwfhIKiGCeOYz8juw0tzuddvPEkg79g6--B9M0-vd7zZ_EK9VlX5ptH5xNS9t_H3wRTy4Z4-1LJTnskzpzWR8_V3o-PvLcW5z9hlVF3wTh0ZNzaZJfupXbaL5gb-A9agV53qT75PcwQzUzpeAUYQnjhyC85vCrp4-vC8uwQwhNlgplrojRuX5ZdDKAWQ9mlFXZly738S5FtVq1EuSl0hh1wuTFCp6_hqUG9ok-aRCwxd7etMImJPq5UB43QKeS3DyFrjgxjc2UNbikjSLXY88jL9AElmgYUxCc1R0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=fy9T_DVct0k0T2vJ1JMUZnerp-h-wJyIrEbgVFJ85cy-ZPWwYLkIxMXXQ8Q5cZZqgru5oVPWfFAdn0RFsCMMFWpW64hvuLkBzGtfcCbbYXOTM2Vwzhm7lTw1OoByPA-Elm9AGKNDsTPjKDdPRkhBgGYOVtSW7-l3WwAfOPv75aQtsKaF-Rt_L2qAaAHw0anc8GMgWUrQqzn0NjHc6Kkbf6JieCQCYSxQkQ3wtZvG0H1brOIzoBkO9lwTTyZyl6SAqzn06kUxwIOzeUsN4D2Paeph6pEOHRSPZ1zh0q_Fai3QQ73-DD7cyedPE6AIymJxrkvCM7_4etfn4k_rQMzlrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=fy9T_DVct0k0T2vJ1JMUZnerp-h-wJyIrEbgVFJ85cy-ZPWwYLkIxMXXQ8Q5cZZqgru5oVPWfFAdn0RFsCMMFWpW64hvuLkBzGtfcCbbYXOTM2Vwzhm7lTw1OoByPA-Elm9AGKNDsTPjKDdPRkhBgGYOVtSW7-l3WwAfOPv75aQtsKaF-Rt_L2qAaAHw0anc8GMgWUrQqzn0NjHc6Kkbf6JieCQCYSxQkQ3wtZvG0H1brOIzoBkO9lwTTyZyl6SAqzn06kUxwIOzeUsN4D2Paeph6pEOHRSPZ1zh0q_Fai3QQ73-DD7cyedPE6AIymJxrkvCM7_4etfn4k_rQMzlrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bhaiF176lOulh0OexEWgSCTk2k59DH06jrjEDIXKyqIE05HTQVGo3F18oAp0PXI2-_g6GNyBnP8-PyHP0NJr0sNjP8kJeSzvpnwiADS2m1nlzcmQA1kMQFk1IvOU3eoMHqnb4_iUQD7NZ2nLJf-UyOoPA_yuu6QtpSFhLz1-8FjXRk0X_0xnS0-93MOwFUxDyTTk6J7R2QEhthQPVHcOF2ZjxDrwHCDVXiMI_5rppavUz1XP6BuRL3WRcz1pPSkg4dZw-p-6cZA-uxEnW7qGTnvsvUj-hGX6bQjdnhbLsGVvVvMHVJrnVaQYx7c9yqBjepQ3FD2p88xTpbuUduTlbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bhaiF176lOulh0OexEWgSCTk2k59DH06jrjEDIXKyqIE05HTQVGo3F18oAp0PXI2-_g6GNyBnP8-PyHP0NJr0sNjP8kJeSzvpnwiADS2m1nlzcmQA1kMQFk1IvOU3eoMHqnb4_iUQD7NZ2nLJf-UyOoPA_yuu6QtpSFhLz1-8FjXRk0X_0xnS0-93MOwFUxDyTTk6J7R2QEhthQPVHcOF2ZjxDrwHCDVXiMI_5rppavUz1XP6BuRL3WRcz1pPSkg4dZw-p-6cZA-uxEnW7qGTnvsvUj-hGX6bQjdnhbLsGVvVvMHVJrnVaQYx7c9yqBjepQ3FD2p88xTpbuUduTlbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqp3bSCgP9q9_xI9q5EY4yQcn-ZNrjWnj_3K_T2I6hxBjUmri2Il3rOLV93syGBb8D6UHbOs1ElyP4_va9cLdMhsTy03xu-21oQ8ypMoEJAMC5hIM433AJNvQJqfZxqdI-No18OuLm7TlvG4nSwdBitOWJSFqacRVxAR7rVpDnXlx-PWbVI968e-eTUGwUBh21nQ0Axbrco8vM7JZ2pBLOB78YqzSsHiu3gBcuJYjfffUMIQ8J4NgvKMbHEvJI2IxdBB6VuuKjjW3jGPpbg7i54xfjRqhG2Z2gXE_Pu32YgpofPPUC15YA7GbzghrEiTvZ0E_blIhZMH6g6KofnUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KtkifqF2o6d2J2mChV0W18w48o6axNggUvaqV4x-tf3RseRFgDiYE1LXwtw5lPWO4Gyoxe_8kRKoyGvaN5xST8KaX3IOYZAEie1LDSf4zzNeqdoR9GD7CiHt_FC3OTbMJ9O9yKs0iKIdhqBOzZ2zHtT2QE9SqAdywj-yfHZI8S3wV5dYgtlJYLpn59koE9bxquKTG5boc9imFSt56lWK5lJsgfz56QWYLoMNVKcABhJxyp683FLLuh3KhTkp7Ki_s6H3U2bcCDNk1P9ho6n2PGLQ0p3CjH1RKSTc7CQszbhzs33cmsx7PDgRYMjlYqLSZ7D7SSVBlTs8siM3mCoiwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KtkifqF2o6d2J2mChV0W18w48o6axNggUvaqV4x-tf3RseRFgDiYE1LXwtw5lPWO4Gyoxe_8kRKoyGvaN5xST8KaX3IOYZAEie1LDSf4zzNeqdoR9GD7CiHt_FC3OTbMJ9O9yKs0iKIdhqBOzZ2zHtT2QE9SqAdywj-yfHZI8S3wV5dYgtlJYLpn59koE9bxquKTG5boc9imFSt56lWK5lJsgfz56QWYLoMNVKcABhJxyp683FLLuh3KhTkp7Ki_s6H3U2bcCDNk1P9ho6n2PGLQ0p3CjH1RKSTc7CQszbhzs33cmsx7PDgRYMjlYqLSZ7D7SSVBlTs8siM3mCoiwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=aqBFkT-OfJVcqMCk5ieRC6YV1m6XKxhDutvVRL0IQ-_ZFQZ16fSCXJ954Jyr69OkpF8n1ARgObcaYGj0GEzCDxbixQtSlo2x-UwQO7tKfa67HuljYTEESVZ65jNwO6lujJRC89cgKVwrWAT-yI_Q7qEEBe7hlprzd-dLtnHbuSiUGfErlUpWBnQYbhDSlCSLbk2h51-unJyiw9BQIiggR9AmB9dF5gm7o-P9nJHoSJO5ToHGEVQKkjriXVyPvz9S5tMpATQpWW7qICTZceKiDBqZRBeURKj3Xi4Vnwl_cnJLKNIB1uVM_HFu441ZfjirqrBubgX3GNBWf6cvZNkl1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=aqBFkT-OfJVcqMCk5ieRC6YV1m6XKxhDutvVRL0IQ-_ZFQZ16fSCXJ954Jyr69OkpF8n1ARgObcaYGj0GEzCDxbixQtSlo2x-UwQO7tKfa67HuljYTEESVZ65jNwO6lujJRC89cgKVwrWAT-yI_Q7qEEBe7hlprzd-dLtnHbuSiUGfErlUpWBnQYbhDSlCSLbk2h51-unJyiw9BQIiggR9AmB9dF5gm7o-P9nJHoSJO5ToHGEVQKkjriXVyPvz9S5tMpATQpWW7qICTZceKiDBqZRBeURKj3Xi4Vnwl_cnJLKNIB1uVM_HFu441ZfjirqrBubgX3GNBWf6cvZNkl1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJCZcCxcORWvAMmX7p4psm1StaBEt-GBKDq6EJuCCBPG8Nil_kE-5gGpKOQj29DgCUfRSiXhN9iQGDBXFOvg37Jwz-nng1bU-EgecJNEaU3BN7KH8isrbuLJqsVD2fh7_QZcHaW_dAtmqjQuXxzqJV98LYptJZZ0jyxazABxUNC51MM_aN3KPSuc4K28Cnd9QYkQRJKpcp0p-ujGjejnMqTvtpsujXDIdJcnWgQdX0V6GKvdF36xXcuieJmm-6PU3Q2LDQ5qa-g-5uKJD2pgkNnqiXZ4_UbBuN2NVaiOzP3RyrFS9-u5XKujJqaNOD1q_kRz2RqzgyOIPEZQFVahlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=BFD0UMaz2rGHNh8pP8EXS60AeNUU_zvC2zX6VGOSZqRi8-jglnS3pEd5-zU9CpofVNwIZrwZkFfm-YNI-fPlEh1Skf3OdK9T8CpjBf6pNnyQ3YayxDTZCtv5zaSxL9SV6dglK3L3fxPjigKOgCThyqrOeef2__QgzllaJ2xPfDbjgZBehCHsHm8neE3Vn9RLLf62DpkcBmQdyVjfn_lf1CipDPGHDe3Um-1jNQnt_gLVXAS_FNSQ1M95Y8lag-VrZpyCOMyKNa5FDnRSwTBaX1HlKX4MWDwRr0PWwpvv-26Puu95TqT-C8bzk-PTxIMLLKu_SpvBQGWFQEI5oH7yF0eoyucm0NMrl3qH7Au82vTkG6L80GyvPdgX30-u76NW_RibICofGeOEchzEU8n6T94TJ_jYYm8SedabAs-Wdgk-EmxdpQ1nU29wIUAXGUKi0rkaqTCVx0Np-Ui4AY7Xb0j2Cy6y_hc5NvxF654mIiGohz9CQ-N08XbUpySsByMCzonq9UsR3VNimXiF2TjwJSmNxatZhmIDDyc7JbWsR002SWrsxEpZy8vlvXuKd7XT1-z4l5F5WMSBuQwgHrw6y_b6wXckNAbn3DNNISzmE-OUb8mRSc7pY-v1ieldxVOQXYQnrI6iRggs0Zl2Lxd--2PGjDla4nD-_cYlIK_7NdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=BFD0UMaz2rGHNh8pP8EXS60AeNUU_zvC2zX6VGOSZqRi8-jglnS3pEd5-zU9CpofVNwIZrwZkFfm-YNI-fPlEh1Skf3OdK9T8CpjBf6pNnyQ3YayxDTZCtv5zaSxL9SV6dglK3L3fxPjigKOgCThyqrOeef2__QgzllaJ2xPfDbjgZBehCHsHm8neE3Vn9RLLf62DpkcBmQdyVjfn_lf1CipDPGHDe3Um-1jNQnt_gLVXAS_FNSQ1M95Y8lag-VrZpyCOMyKNa5FDnRSwTBaX1HlKX4MWDwRr0PWwpvv-26Puu95TqT-C8bzk-PTxIMLLKu_SpvBQGWFQEI5oH7yF0eoyucm0NMrl3qH7Au82vTkG6L80GyvPdgX30-u76NW_RibICofGeOEchzEU8n6T94TJ_jYYm8SedabAs-Wdgk-EmxdpQ1nU29wIUAXGUKi0rkaqTCVx0Np-Ui4AY7Xb0j2Cy6y_hc5NvxF654mIiGohz9CQ-N08XbUpySsByMCzonq9UsR3VNimXiF2TjwJSmNxatZhmIDDyc7JbWsR002SWrsxEpZy8vlvXuKd7XT1-z4l5F5WMSBuQwgHrw6y_b6wXckNAbn3DNNISzmE-OUb8mRSc7pY-v1ieldxVOQXYQnrI6iRggs0Zl2Lxd--2PGjDla4nD-_cYlIK_7NdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZT6vantjRSAuSbs2P6fo_qKv9eIMgfjAQ4BgZwBFv8WppQh1QoVrF_dSHetNCTDdVaZTtExQBv3xwFSZrCNJzoif2CSmTAu6Fm7QIQENwo1ES_HBk4OXM53i4BD4_YufXNsweMxZWaonoqlG2p0mafGBXBapxZh6D-A1y0ahoA4QYem0FVdbux5l9nce-kSL02svoYkay4iaoHyIEGVLkQE2HAsxoe7nqYpLp7cYkfUNKuIVKzizATA9MFWPNC1nBOJJ26rqptwA0tWhP7Ekz3MI0BwDLtWtHtbFEnUWeuApJbeKz7x06Ls7iHgvtA-WPUqgWfufm44R7Qju2amMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=bJsoj29_s9erTMe0zJqpYziCKCGqZgTa6MemXynXEjtpfdohAXrHURVkmS4cvnQlMjCyFO0DrqVLNclvQJizNxFbYWZiHkr_xBmK56shEbQh4qgp4eBIORg61SV0foUZ299fbO4Aw2Yww71_AboMZrINhVjOlMhQZjJOSugUqQrKWWRDqrsmRgM_Tjt62AUvw3qKLAgK0hKtqUv87oxx_N3nrMkX4aSOK8BV0A8sUm33fvkxwZsaxvOmTW8_3wpmkxrWPzuTbiupUKLUcGDWvp1ReYQcWbIPfxR-WhQ-dln3Hjd7GBGBBhzIVIEZjkeuAa9OfKcRVO3te7RnnVRlxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=bJsoj29_s9erTMe0zJqpYziCKCGqZgTa6MemXynXEjtpfdohAXrHURVkmS4cvnQlMjCyFO0DrqVLNclvQJizNxFbYWZiHkr_xBmK56shEbQh4qgp4eBIORg61SV0foUZ299fbO4Aw2Yww71_AboMZrINhVjOlMhQZjJOSugUqQrKWWRDqrsmRgM_Tjt62AUvw3qKLAgK0hKtqUv87oxx_N3nrMkX4aSOK8BV0A8sUm33fvkxwZsaxvOmTW8_3wpmkxrWPzuTbiupUKLUcGDWvp1ReYQcWbIPfxR-WhQ-dln3Hjd7GBGBBhzIVIEZjkeuAa9OfKcRVO3te7RnnVRlxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A__3NzsS4cGqjKHOl9jUS4sRMq42VeDe6LIz5wNnsxa_H6Xs_KdnFQ9fLG1xro2P2QqgBalY6zYL3_f9c9mp_iYhubavZIXyUNed6H4w3RUZCOk9_KSFTtAj_tI9f0biYqd1Kp-vVFLYOKZK4P8jDj2i0vPXIXwUr1ubrG5XhC8frq7ZL5PoCD08DvqYxiGNTiDMp20248WLvF76aHfnyLGHFEV5HRa_sMJ43Wpyl6Sq9lLFBXRhLT11R91GuM54MQJFKSzZrTNu79Gq0Vx0W-qun7wMWXMshQ_CsrqjSL3fp8PSRZ-g8k7-kxT3GNnOc1aRDRAo3I4z-0UdvRxHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjFVSIXntbMs4zhsn-_t3Psxi1FmYrX0wnfEv27nUgiwnkMBVW8ipDfoqA6_o8wJj_UDkywNKWdy-TB42Ye5INe3f-SUr1cQBPbtqYk4RtiaoWZOQIX_KDotyX5SeiMwhnh1JG5c-cmR7fEAGAlZWV2RDpI71tsy0ufEwZJHH19t9_AsBv3zMB7_ha1Mgt6hVbBPz5KklcTSjc85Q-Q1_vorm2PclWMbpP7yGtYX2uJkxBr895ICZ8GMG1U7DaFFKJnC_F27Ms7vtjAW6mDvFsc7z_5ht4UXdGrl6Fp6EM50dtZA_LsSLv3j5S5UMNYT0eFVrw8-UpZFhRJYjPH9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9zNmGQTHzZJJa2OHBGK8o2bKikyGV7nn66KzDqMcRsbC_SX1uhi-9CyDSlB97i6XAYZCB2Ki73EfVZtgOrTUn6gVT_DE9rHfZoHLSSmbNo-xeP4WPEk5dqeGozueYptHA0AdbrAK_6P5mkTODne2qR3o2rid5jYJ9BFWDDbyx_Zp-kdlFfTDPIekrAScOOlwt2J-muh8EqyrWUqEGFxWN0971jO-TpwwXOvEO4Rfv_CPgr2xsI0FblGKs68ynkz_JYtpR-Vwmth3LgU--Hb9qTHulJfcQMxUFgIflbjxNFA-TVBjZlXpeGtHlurs-bThyyc81yW7kJ_QuKfupZcQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=mHLzIuJwuIKJAr7eakFQRhKFKihfNEIT-CjFiRlPPI_lstzZ65O4Qo-HpT3poJywNKqN6jZWzHtrURYkh76V6dZKzSCcF5nMuEQzlJ1MfHVMNMt6XZaJG9hPtadl3s60qkZXFk9Y-m_aWZ3RKAnr-C9bz2oRcRSk_rAbnnF0ZrLZY95Fx9eDX-17yOyvUQgps_O7BJP6n0dfc0rZoz1m7WqEBY3tMD5C_zxg7TmgYol2NZ11MHsRqXeGQskA9FDsSe0W8Ka2VssnFZ5cBwQDXG9xkyPKo3pYtpDNaFKhR1-oWpoBYlo-bjq8N7u7_eDTpvu1sbmTTwPYaOiSnpBfew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=mHLzIuJwuIKJAr7eakFQRhKFKihfNEIT-CjFiRlPPI_lstzZ65O4Qo-HpT3poJywNKqN6jZWzHtrURYkh76V6dZKzSCcF5nMuEQzlJ1MfHVMNMt6XZaJG9hPtadl3s60qkZXFk9Y-m_aWZ3RKAnr-C9bz2oRcRSk_rAbnnF0ZrLZY95Fx9eDX-17yOyvUQgps_O7BJP6n0dfc0rZoz1m7WqEBY3tMD5C_zxg7TmgYol2NZ11MHsRqXeGQskA9FDsSe0W8Ka2VssnFZ5cBwQDXG9xkyPKo3pYtpDNaFKhR1-oWpoBYlo-bjq8N7u7_eDTpvu1sbmTTwPYaOiSnpBfew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4GptyQXpGiygKie4xTzBHrR49_Qzd1ifYCOwVN0ohzO1UZeSszyqBMQrXmq_Nu2312d0t2MmgCLNWUKwEm4XKgwFKyFr62TIlnvDwA0ALhqenohEpM_lZBKlmUH4FLpoLWZ3xyLlqxV8vnJFbZKAIIit2GgdbpkUBTzsZKe-K38oDupWGeLYPFADTrMUldgA4OO03n0oRoiBe3-oWjBTt6EMkv4bdFbsryE_pe6rd39sAykxMyGK18wAJAOMMLfF4sdOmfyFF_XkfxHnAe7u7lck7youdip1vfKk3ntltWnFZOhSbPKnoqAeSMt24DYAAL8jA4yZ2Pw1DrhrM90RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuztn42OskFTR7hw_17biyJTZ8L5LZw4BAKjbGNW-C9JLCgXJsnP1f04UJHBEqhynSFcyM75JlhLM7EUxvl-UZDMTeXMB-Lpd2J_Enllxahx_xKXunnZSMz_ttN2hN34DA2Q9ufSVxjuWySHD1WW1Zrhcai0DHYH0geq11Ixc5_QMHnzJKVaoKoAsXsvwkL3VOVeosBFCV_OGnAJH2RpoyXmJLXEP06gG2lGuCq60U2Oi3lJZ17r6r8_5jF7nnxYPV5LSt0Jb5IGqvPmjOG1efNBkLe1FiMBd7hrGl09VZqg9wwGFZKvI7oEy86YFy65MifYBldTlh_sL5A3JUwvZ5fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuztn42OskFTR7hw_17biyJTZ8L5LZw4BAKjbGNW-C9JLCgXJsnP1f04UJHBEqhynSFcyM75JlhLM7EUxvl-UZDMTeXMB-Lpd2J_Enllxahx_xKXunnZSMz_ttN2hN34DA2Q9ufSVxjuWySHD1WW1Zrhcai0DHYH0geq11Ixc5_QMHnzJKVaoKoAsXsvwkL3VOVeosBFCV_OGnAJH2RpoyXmJLXEP06gG2lGuCq60U2Oi3lJZ17r6r8_5jF7nnxYPV5LSt0Jb5IGqvPmjOG1efNBkLe1FiMBd7hrGl09VZqg9wwGFZKvI7oEy86YFy65MifYBldTlh_sL5A3JUwvZ5fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Sqqfpy_XgRNSSW4-QvPJY1oxGw1PxzIRIU358tJFfcua2Ln5Wal_-spKEAMDxVJ9TWj2ZIruKfNBOp6_mM6vD0zzzziWmmlhlUmPy6vi5yCJ4OPWrOBglIqX5FVgQR5pSzmuCMMsg2wR5KiJPiWVMDah-DxOiGinTd0Slq-1qe_sofoKp_uZA4u4GhU7QP80mMEDuRvqsPT4muO36-lY7wPzEMqjTQsdtEaKhq61G7hB__UDpt8v1ukiKHjPJsWZtiiULXnIl3m7OsK0BfbLdAWL_J5I404bYoHKhk82JkMZT3lvqQ3AACNkwIMu2n7zYkggdZUALBl2lD3lQR6u_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Sqqfpy_XgRNSSW4-QvPJY1oxGw1PxzIRIU358tJFfcua2Ln5Wal_-spKEAMDxVJ9TWj2ZIruKfNBOp6_mM6vD0zzzziWmmlhlUmPy6vi5yCJ4OPWrOBglIqX5FVgQR5pSzmuCMMsg2wR5KiJPiWVMDah-DxOiGinTd0Slq-1qe_sofoKp_uZA4u4GhU7QP80mMEDuRvqsPT4muO36-lY7wPzEMqjTQsdtEaKhq61G7hB__UDpt8v1ukiKHjPJsWZtiiULXnIl3m7OsK0BfbLdAWL_J5I404bYoHKhk82JkMZT3lvqQ3AACNkwIMu2n7zYkggdZUALBl2lD3lQR6u_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Rxui6fgZfbunSrCtYIDvA6WVwPqUovFzHc-askvkC2JOKakxbVRF3nHFsV76GPlH5IG5LvMgrUa0Zs_spGeS293gKBwE5x-Y3JmV574_E77nOATUxZxgIRRiMqmzOEpZIxHanNw_TAqZHjRwNs4pcM9epg-lTXlQHjlQ6eBJqdolsidDEVva31tCN5OHrv4gxeQUNemfNyCS7agC1bh4cUMSL5vneyz8rycciN4MYicgyrmOfy6H8dcSN6dAGIYu90g9j78--9PkddXNr864IGdo-EbFFar-hu2sdlSYIKam5yU04YNb8-QE7fbNVtIJHEZKWcLhBVT5N4kcxKshcwsqW2zINhUUk05euDDYxNupvcWI7vtU3_IW83ii8B7egQ-dbXaCPgzaSQDLBNXW3IeLujjXyEGV41f_DvWolaCHpbFrWfPvcyJVL4KHtCFlyiSIf81RwjDK_ut6B-i4GXW4ZvbmtQqAGBXYlAoeluwvYsLaRtAQsYlFF6yvpLg-vRc1EWTyoYTTit9SExRPM7FNcmihsvUPzHgBmzLUV1gS0XgSI_1Gf1XDjdlTT4T5zCvhfyb7_WJRpPUQY8TgSDNMtZ3X7AEudNwDAA7JRf7rbVqsCKsms6URXkdcE5oZ4UOE7jZXIwk_8iMSvDrtw1bi4hmOySh_QBM1899546M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Rxui6fgZfbunSrCtYIDvA6WVwPqUovFzHc-askvkC2JOKakxbVRF3nHFsV76GPlH5IG5LvMgrUa0Zs_spGeS293gKBwE5x-Y3JmV574_E77nOATUxZxgIRRiMqmzOEpZIxHanNw_TAqZHjRwNs4pcM9epg-lTXlQHjlQ6eBJqdolsidDEVva31tCN5OHrv4gxeQUNemfNyCS7agC1bh4cUMSL5vneyz8rycciN4MYicgyrmOfy6H8dcSN6dAGIYu90g9j78--9PkddXNr864IGdo-EbFFar-hu2sdlSYIKam5yU04YNb8-QE7fbNVtIJHEZKWcLhBVT5N4kcxKshcwsqW2zINhUUk05euDDYxNupvcWI7vtU3_IW83ii8B7egQ-dbXaCPgzaSQDLBNXW3IeLujjXyEGV41f_DvWolaCHpbFrWfPvcyJVL4KHtCFlyiSIf81RwjDK_ut6B-i4GXW4ZvbmtQqAGBXYlAoeluwvYsLaRtAQsYlFF6yvpLg-vRc1EWTyoYTTit9SExRPM7FNcmihsvUPzHgBmzLUV1gS0XgSI_1Gf1XDjdlTT4T5zCvhfyb7_WJRpPUQY8TgSDNMtZ3X7AEudNwDAA7JRf7rbVqsCKsms6URXkdcE5oZ4UOE7jZXIwk_8iMSvDrtw1bi4hmOySh_QBM1899546M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=HfP3uEOxUDZUOVux_4wV5l4kqGi4Fs5PrYfBVKlf4cbT4XmpjzIZzrKgS_DaERBASgeuEtYxDG186yctwIOtuvZ4QlfXYqJgzmbX42pxhUtCRRGmuyz9wQynxmenYXOT2-Uw9bcdIdnpIUzU-e62MdM5A_O7DEB3uOgKCyQ7_WtvztpgZXpWNuAzaRX_u_N9uHEdy2bMfRaJTVGCiaNcjqAkHPdRyc5WOADEkflHZ362XiO92QP2NCcGpoWP5QBQFNWcZ8SjBVa8G9U05Bf0w71tO9CtjJfKc9kk7aqvSYCiWHZF4OUrga_oELG6LOPlElPzaHxXwoPEJ--6CM8YfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=HfP3uEOxUDZUOVux_4wV5l4kqGi4Fs5PrYfBVKlf4cbT4XmpjzIZzrKgS_DaERBASgeuEtYxDG186yctwIOtuvZ4QlfXYqJgzmbX42pxhUtCRRGmuyz9wQynxmenYXOT2-Uw9bcdIdnpIUzU-e62MdM5A_O7DEB3uOgKCyQ7_WtvztpgZXpWNuAzaRX_u_N9uHEdy2bMfRaJTVGCiaNcjqAkHPdRyc5WOADEkflHZ362XiO92QP2NCcGpoWP5QBQFNWcZ8SjBVa8G9U05Bf0w71tO9CtjJfKc9kk7aqvSYCiWHZF4OUrga_oELG6LOPlElPzaHxXwoPEJ--6CM8YfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nskH3DIedmjVLm6T6GyTTFvMHazYq58zf6Y4zg5w14N10Zo2oNzR_PLt4tG0WPFHKPoWgNClFuQe3Lirk8-wpUzOMca_f9pOs10h2KSlYiGBT2PHZHjLXbF1vXk3FmmeH9x0ttHRgDYa6E98oohruCJcQSabybNEB06lvAMQ3UAYV3PDJo44ss7H0nvpLJ21MgCVf2iKvfj8AYZ88sXqffzK2cOMMWBaG_MHDYZkDMMja8szA0B5HK0wrG0RuCGsmGJaCjABIItyCmpxUELlO5CvSGP4M-5hOe0P82Xy0tmmo2l9cFUZNN-PRsW7Yb8TRtgRoAYboI8drInKfkaG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Ymlcp0nX8k77lGXwlQygAWLvLK2bqcueymXdGgZpe0QspdzRNjSg21xaC3vLeSST9MKVEk8bqxTq3lZYDFp-c-w0AsA0Z9BrEk1zeHOXZjGtOgmj2Srpi3OkG30x70U5rYgFRfQUmF3C73yYfQC4M9ZHmoCB5C2Iu2EEgtSMhrOJpa1cmshoUlQ1dhL2d4ER6e_gPlr29FD9_jVUihh9cP3jWA2PNvplf2lZ9Pf6e6-WPnA5I3lhHxYKFWrYmbUKZVkZb1DBBgaGSLrctmkNcnHJBIMQ6AYyuEP9OUl7Dpitf_bkosyJXB4ommExcEcdQNpFCuyspufivXKOs0s7Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Ymlcp0nX8k77lGXwlQygAWLvLK2bqcueymXdGgZpe0QspdzRNjSg21xaC3vLeSST9MKVEk8bqxTq3lZYDFp-c-w0AsA0Z9BrEk1zeHOXZjGtOgmj2Srpi3OkG30x70U5rYgFRfQUmF3C73yYfQC4M9ZHmoCB5C2Iu2EEgtSMhrOJpa1cmshoUlQ1dhL2d4ER6e_gPlr29FD9_jVUihh9cP3jWA2PNvplf2lZ9Pf6e6-WPnA5I3lhHxYKFWrYmbUKZVkZb1DBBgaGSLrctmkNcnHJBIMQ6AYyuEP9OUl7Dpitf_bkosyJXB4ommExcEcdQNpFCuyspufivXKOs0s7Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Nzg6mYRZB5DzQ25EiO8u-4cqv6uDpAqXvgyuPh9Un3o8Zf-aew2gsDNmF2l4k4SirEX1iL1GNA-447TKreWfNlMPw2y47NsAZRxMjse1kf2YdzTuhACnmjJyrcZa86lds3jLWt5DXJWHCkOF_wM9ureC6FWV9Fu3o-VUbG_LbrESssQZae1c8WKOMZfSl0Q3ZKPBiLWJMtegj8ipEJwB6tsWNfAIDtJs-m76kODVNB7gDWyWP3OsnS7ZXKenY4gJpoy6AqrPhjvmJyOv4rf_sBt7Kp9Zko8IZc2noaS8qBaB_u-32Qnwvnj9izEobpCYyl5_HkoCq4LArna45TjMAjIDwZc5ucFY7M-hw3Si2HgWcQxkPf7LvsZodY-ArrxUZorAU3LNMa-FQqQ8_0PFQSZnMgz1bufqoUwnmwD3aP6SmEAZNvIWF1k2P2DoK3D-Y6hdlwwwEtYC9uGNPw1LdR_5DOVhuoifsCZh1SciS0QFjIYGlbU8d0Aol1jAXwXFwy5MPpvqHvhHd9aoPyrJx-5giKOVfoiPzdHhBSbzYm-jP0nmg94mFrD_v7BrcAL-D5lkQJP0fY3dWzBZ_US7SAixUZ2olBS7m29Gxj5iSHDNim_abKO69L0XpHRtARd6cw6jkR5sFcTXkHpvWu_eHhlyO56tHYnzoB41ecoEB1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Nzg6mYRZB5DzQ25EiO8u-4cqv6uDpAqXvgyuPh9Un3o8Zf-aew2gsDNmF2l4k4SirEX1iL1GNA-447TKreWfNlMPw2y47NsAZRxMjse1kf2YdzTuhACnmjJyrcZa86lds3jLWt5DXJWHCkOF_wM9ureC6FWV9Fu3o-VUbG_LbrESssQZae1c8WKOMZfSl0Q3ZKPBiLWJMtegj8ipEJwB6tsWNfAIDtJs-m76kODVNB7gDWyWP3OsnS7ZXKenY4gJpoy6AqrPhjvmJyOv4rf_sBt7Kp9Zko8IZc2noaS8qBaB_u-32Qnwvnj9izEobpCYyl5_HkoCq4LArna45TjMAjIDwZc5ucFY7M-hw3Si2HgWcQxkPf7LvsZodY-ArrxUZorAU3LNMa-FQqQ8_0PFQSZnMgz1bufqoUwnmwD3aP6SmEAZNvIWF1k2P2DoK3D-Y6hdlwwwEtYC9uGNPw1LdR_5DOVhuoifsCZh1SciS0QFjIYGlbU8d0Aol1jAXwXFwy5MPpvqHvhHd9aoPyrJx-5giKOVfoiPzdHhBSbzYm-jP0nmg94mFrD_v7BrcAL-D5lkQJP0fY3dWzBZ_US7SAixUZ2olBS7m29Gxj5iSHDNim_abKO69L0XpHRtARd6cw6jkR5sFcTXkHpvWu_eHhlyO56tHYnzoB41ecoEB1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS_FEiNJKOHoJQ7zKb9TjhAsAqj-l2UUii7p56ROEdpsQiNYunmA6uMhknBn3cjX2JPkzbouN5Y0o8W1hAY5tXno1glUvyqyU9SMS9o5fC-UmQ9dwYCIYjO0g6YwMONJg5eAYKISqy1-oKu1jfWUfQK5S0OHZ9V4mc8EckD-XYlTPmLYZ2FfNyH-BR6R0faVQgj-rqm_1mtjCGXNsRPaLxBJ5CIGmxf9fqRUc4c--qx3P4yoabTCx0EutfMHMeVwxDfLSAXcLWeNqiz9uECwGHar5sF2oETX5qBPaFtg30veRzwUlS2roUMhGwH4c2XbeGuyCPprSkwi5DEajRV1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Lwaj7S899sFqlynLwBSzqR7nXK9Q8EE_OAaWoHHWoAkM6ZK8_B84p4mSn-QHzr13oLR0WkqSdh5pKxliJX5C-wmp8n5z1GQC4afv-31t3PmSwDnC5DGrBeHelKlmd4GDCZUVXwoGyPsFQkjB67ZfYns9BZNeSaRJY-Z57lB-sB5jzD8Fl4ytuLU6nU8qEtSLePPYplmuXzzOiEfhdJcJamKs2VAJlIcWr3ZBmqXZjtNBSmP35UhzWC1p0ZPGge9r5WJxyvVOm6mKJG0O-RE-xwDu8vfE7MOD6_Pwo2-7d621JYhoZMNs7iXbNgmjXiQBRCIoVJqgBFpJ-a20CnKNmJf6T9_-vc7n0mAS_O_-Yicfg_YKRqrEdXtr__s40U8A-DTibF-jEF4bV_qlw7WfBpZbO9vTWk6ZCDFJTv3Be_68uutvUIrEThv6cdSC9cpHwVCvKxwwO4hbj-3FAIDrl8bSL95ysjnZ90IKAFio1GzY2epg9n9Cx5FMoTjf8iShtTIzgllc8DVbzNOvQ8XhDTRIlSf7pynxQBt4Hlr_oyTlQy5cJNpHNsVFxaB8r2KbktpXoJJCFQAO7w2O4tBiGZ3fBmlj2NLYdUZIyMWcbf1q4iuPWlzFZZXB6xsuGG39CsFdG3nAs4Pnhq63pgRGBNNwUnaw9dRPV2DV12xb-Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Lwaj7S899sFqlynLwBSzqR7nXK9Q8EE_OAaWoHHWoAkM6ZK8_B84p4mSn-QHzr13oLR0WkqSdh5pKxliJX5C-wmp8n5z1GQC4afv-31t3PmSwDnC5DGrBeHelKlmd4GDCZUVXwoGyPsFQkjB67ZfYns9BZNeSaRJY-Z57lB-sB5jzD8Fl4ytuLU6nU8qEtSLePPYplmuXzzOiEfhdJcJamKs2VAJlIcWr3ZBmqXZjtNBSmP35UhzWC1p0ZPGge9r5WJxyvVOm6mKJG0O-RE-xwDu8vfE7MOD6_Pwo2-7d621JYhoZMNs7iXbNgmjXiQBRCIoVJqgBFpJ-a20CnKNmJf6T9_-vc7n0mAS_O_-Yicfg_YKRqrEdXtr__s40U8A-DTibF-jEF4bV_qlw7WfBpZbO9vTWk6ZCDFJTv3Be_68uutvUIrEThv6cdSC9cpHwVCvKxwwO4hbj-3FAIDrl8bSL95ysjnZ90IKAFio1GzY2epg9n9Cx5FMoTjf8iShtTIzgllc8DVbzNOvQ8XhDTRIlSf7pynxQBt4Hlr_oyTlQy5cJNpHNsVFxaB8r2KbktpXoJJCFQAO7w2O4tBiGZ3fBmlj2NLYdUZIyMWcbf1q4iuPWlzFZZXB6xsuGG39CsFdG3nAs4Pnhq63pgRGBNNwUnaw9dRPV2DV12xb-Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=IJ0x46on2mvbWreWwFcka2CF8HvAImErstanLIJZXIyNnt3kMHVp-N9z4o9tK3FBbbIPs3UgDULQZcSCs_V5BRS8F_XamByZnPayrAf83Afl-3Sci_nTo2ffFbMYuSZLvZ_OwR_DkjeSLK4HZ8Dg_xxHKqSdFQpokRS1Pg84KXHJZdJ1CEzyk3PPI0KBfxVBlbRs0bIYfssrqUTghTS_L3vd7RAsEa7siqkFqxny7g6bZcY-YYHxMNQKwEJo99yGhn70eKCvHhrSY2KFzNctlVxe6ESa9f_3mWaVQYhfsvaDN4JF6xx7wAzpC9XVyJRN6QlFtaR4W-iJxUpZ27vh-DH3vXlGAoLQkgHYNHddYVfHt_xGv0PU_nz-ncQ180NIbfl92VfhuPPZnVOw06Vpdb9fR2dPFnKRuf_37Er4RLnWGNFO-zrJAgQhcJ6tOZbqwtgY58gD-BBNstzHmBW8GgWIkYGMSSufo8RdCB9omiS82YZEKlfOyQ96Oh6-E_bus3zuLqhlxkYFeyYnllAmwLT-t9wqthP5cvU-fi0ncVqOvs-WZiVcELLfuZJ1ePkuHR2lD0pOc4Hq1koapLt4tX-X4gQH64kemqOVy0TzGr6Y4D50-7bUAOVekLGC-2LxBCiBQj0upbKjwXruAWtbX1vTycMwMnvQ-lC6npXFPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=IJ0x46on2mvbWreWwFcka2CF8HvAImErstanLIJZXIyNnt3kMHVp-N9z4o9tK3FBbbIPs3UgDULQZcSCs_V5BRS8F_XamByZnPayrAf83Afl-3Sci_nTo2ffFbMYuSZLvZ_OwR_DkjeSLK4HZ8Dg_xxHKqSdFQpokRS1Pg84KXHJZdJ1CEzyk3PPI0KBfxVBlbRs0bIYfssrqUTghTS_L3vd7RAsEa7siqkFqxny7g6bZcY-YYHxMNQKwEJo99yGhn70eKCvHhrSY2KFzNctlVxe6ESa9f_3mWaVQYhfsvaDN4JF6xx7wAzpC9XVyJRN6QlFtaR4W-iJxUpZ27vh-DH3vXlGAoLQkgHYNHddYVfHt_xGv0PU_nz-ncQ180NIbfl92VfhuPPZnVOw06Vpdb9fR2dPFnKRuf_37Er4RLnWGNFO-zrJAgQhcJ6tOZbqwtgY58gD-BBNstzHmBW8GgWIkYGMSSufo8RdCB9omiS82YZEKlfOyQ96Oh6-E_bus3zuLqhlxkYFeyYnllAmwLT-t9wqthP5cvU-fi0ncVqOvs-WZiVcELLfuZJ1ePkuHR2lD0pOc4Hq1koapLt4tX-X4gQH64kemqOVy0TzGr6Y4D50-7bUAOVekLGC-2LxBCiBQj0upbKjwXruAWtbX1vTycMwMnvQ-lC6npXFPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=NfjzZTlVbHU4glaUQaU0HOWxDs-VYuNZsQOSS5woe5RS3VVfmt5UOlhJMjOBTtXmdJBDBHwvzX2QKsK_waKuf9yoX3Kyve5Ye5W9SJcgqa6VA9FP9_YFoGMRhYp4ldL0ozEaZaHK-a0pTkI2L7SpNElulZnB4bbR-51j8zo5HoAQbqncVO0HmswnYtHJr_Xg5HBkrWI3bHSYfXO7j8gP00BPO5leslmjDOr3obU2LnXcd4aiULM4Ug0s8tC4lFpPOuipGuUrkHPZKVoeSF2cKUuzZnL9fmFPPpU0GdqnnIOym0a1VpLATdlLY7OKeWYrFowv_NoAUSYVwfguRylp-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=NfjzZTlVbHU4glaUQaU0HOWxDs-VYuNZsQOSS5woe5RS3VVfmt5UOlhJMjOBTtXmdJBDBHwvzX2QKsK_waKuf9yoX3Kyve5Ye5W9SJcgqa6VA9FP9_YFoGMRhYp4ldL0ozEaZaHK-a0pTkI2L7SpNElulZnB4bbR-51j8zo5HoAQbqncVO0HmswnYtHJr_Xg5HBkrWI3bHSYfXO7j8gP00BPO5leslmjDOr3obU2LnXcd4aiULM4Ug0s8tC4lFpPOuipGuUrkHPZKVoeSF2cKUuzZnL9fmFPPpU0GdqnnIOym0a1VpLATdlLY7OKeWYrFowv_NoAUSYVwfguRylp-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=L7mFI3x2bKPU2azzxmS-Mp_WqF8sunNYAzsAiynXNZBfeO8OqaOCBfx9GDOuP2zwoCppGh7qkWPjg4rIJHGCu1EEgHq9fJWXblcqPBAX8H0sQ3Am1-xVinIzG6LuuN3mw7N0xsByzlA7kQb8_P199yZizv5gHBWIbkmyiEcip_xHsqVbgOViDTq4pOej1yaNFGx5OpINh9n4Hq6lLxDTO_DlQ_vMYjn7iOBIOh4kjGuF-tnRvQWJJNWiTRQDpSj3vJbYyA1Hr16rvnJ_wcqA0_INjbcASiHPj-gySRIoY4VQVMbtDTc8YCuL4FiHbA4W_qa7ezkMCxUjYsYsCvne_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=L7mFI3x2bKPU2azzxmS-Mp_WqF8sunNYAzsAiynXNZBfeO8OqaOCBfx9GDOuP2zwoCppGh7qkWPjg4rIJHGCu1EEgHq9fJWXblcqPBAX8H0sQ3Am1-xVinIzG6LuuN3mw7N0xsByzlA7kQb8_P199yZizv5gHBWIbkmyiEcip_xHsqVbgOViDTq4pOej1yaNFGx5OpINh9n4Hq6lLxDTO_DlQ_vMYjn7iOBIOh4kjGuF-tnRvQWJJNWiTRQDpSj3vJbYyA1Hr16rvnJ_wcqA0_INjbcASiHPj-gySRIoY4VQVMbtDTc8YCuL4FiHbA4W_qa7ezkMCxUjYsYsCvne_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=lQpkIihs9wW5diGNuNXV9bSM7Cjj43JbiIQbSvevnQkqEvLKt_OVy_MhxvIrlIjVuh-IIL6QgJ_Xufai6f3z1It1o3_rxG3iAt5KntgupQut_kj1CvweAjQkLJ-Aygj4BKPZ8n5Ne_SOCXkuFiNKSl8ZBxmbuE8i0CAnxi6jNiFO0pmpyXl7-ARTauIs6fr5Jp3M1q5uUWATTiQWfOkukMb3fuwg_X_qAASUzViuKtUm2uVahLEdg9bjtcvs0uIDZWnzAEj6WxRuLRkHIREfJ4DPuLdKDnkZ3nzkVLfMZhZirWI7WXDI1ZkcjFld6ttFM_K3acUjTfGrRbuWihyb4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=lQpkIihs9wW5diGNuNXV9bSM7Cjj43JbiIQbSvevnQkqEvLKt_OVy_MhxvIrlIjVuh-IIL6QgJ_Xufai6f3z1It1o3_rxG3iAt5KntgupQut_kj1CvweAjQkLJ-Aygj4BKPZ8n5Ne_SOCXkuFiNKSl8ZBxmbuE8i0CAnxi6jNiFO0pmpyXl7-ARTauIs6fr5Jp3M1q5uUWATTiQWfOkukMb3fuwg_X_qAASUzViuKtUm2uVahLEdg9bjtcvs0uIDZWnzAEj6WxRuLRkHIREfJ4DPuLdKDnkZ3nzkVLfMZhZirWI7WXDI1ZkcjFld6ttFM_K3acUjTfGrRbuWihyb4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=tA_-ytBYg9F_roUjnY_Rl3g-LhJ15I5MY228tXxAlCqmrdj2udZikpoSKFKnVvI-Tq2fp6ic40jIOAYrHHzkl5sC8ig8dkMsOUcoUh6RKc48Ug3gBDhujNcpyTXdbjxfzXehRH2JRO-vgaWqUx0OyE9AUW4aLCquLTobRN3_sjPGVNCwO9oxgxAEd8wmGj1St3CAsQcO8ayS7bBCSNqeK_KORp0pAtoic3UZaNM0GUGCAlRBYYdLx5tp3POdYQO4dEmHPBunsUk0AZWvGa07wfown5Pkyt32-FExr-yoMd1cLrwzel031ZnsyyuADIK1iOg3ChYKoDLJTHdNVXC-eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=tA_-ytBYg9F_roUjnY_Rl3g-LhJ15I5MY228tXxAlCqmrdj2udZikpoSKFKnVvI-Tq2fp6ic40jIOAYrHHzkl5sC8ig8dkMsOUcoUh6RKc48Ug3gBDhujNcpyTXdbjxfzXehRH2JRO-vgaWqUx0OyE9AUW4aLCquLTobRN3_sjPGVNCwO9oxgxAEd8wmGj1St3CAsQcO8ayS7bBCSNqeK_KORp0pAtoic3UZaNM0GUGCAlRBYYdLx5tp3POdYQO4dEmHPBunsUk0AZWvGa07wfown5Pkyt32-FExr-yoMd1cLrwzel031ZnsyyuADIK1iOg3ChYKoDLJTHdNVXC-eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=hM5hV2-dcYRQ2chVWu2_zVgY48ZuhdzFR4TvyjekRd13XPeeCVtdcmPZ0FBdqidS9QJXSH2YbisY6fQjJIoiaxymtTMd-ZqyBDrhLAZgTds46J2TkzsfuT9hKtDb1usypq-95fhiNDgftXnS-s0i14Tb_h8lKkeoNGSd658hcsTnN7_A0Gj2i6U3wKz6pfQSq6AiAxeGo-fq13xxQ_UBWEbiWTHeDlrBlo_BB7H73UpPH-suzPss2lGZ5zS0CrsDa8f2o0tgRFreGQDcKAGJIWzpiW3Qll9R9345NtRzJ6vru5O9xlvPJnnHB31cwt5Bmz1Dwk6CIaC-rcZsMvZUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=hM5hV2-dcYRQ2chVWu2_zVgY48ZuhdzFR4TvyjekRd13XPeeCVtdcmPZ0FBdqidS9QJXSH2YbisY6fQjJIoiaxymtTMd-ZqyBDrhLAZgTds46J2TkzsfuT9hKtDb1usypq-95fhiNDgftXnS-s0i14Tb_h8lKkeoNGSd658hcsTnN7_A0Gj2i6U3wKz6pfQSq6AiAxeGo-fq13xxQ_UBWEbiWTHeDlrBlo_BB7H73UpPH-suzPss2lGZ5zS0CrsDa8f2o0tgRFreGQDcKAGJIWzpiW3Qll9R9345NtRzJ6vru5O9xlvPJnnHB31cwt5Bmz1Dwk6CIaC-rcZsMvZUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=dvNhoyzs07cPUjpEiFrYWheM-Feo5WjtrVoDQuCXWegP3R78AWmhR3M9C-vFT9a7tc0ZpZW65Ab7Tdfdy5r2EGOV33ZBzPp66xu1sN5OYp8lPR19ayubkB824pncc8Nu2lBW_5yDLqzrWWDUHqs3LO-2M18O0x-NOQBHXxPjc97IxQdFhAH5pCNInKXK77mGjCmyJPVvH2kl1NbaEkKjsjH_ZFORij8FTF4sn2EF_Z5T7aiDt6iA-B7rMQZe55AbXSDcqA7tMExuMiIxl1SYR8QnLlRZJCToSImaA4Es_PtMmKXnqrCGVZcQ80m3_AvtBqU6FmjjLZGN4CDVHvuJmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=dvNhoyzs07cPUjpEiFrYWheM-Feo5WjtrVoDQuCXWegP3R78AWmhR3M9C-vFT9a7tc0ZpZW65Ab7Tdfdy5r2EGOV33ZBzPp66xu1sN5OYp8lPR19ayubkB824pncc8Nu2lBW_5yDLqzrWWDUHqs3LO-2M18O0x-NOQBHXxPjc97IxQdFhAH5pCNInKXK77mGjCmyJPVvH2kl1NbaEkKjsjH_ZFORij8FTF4sn2EF_Z5T7aiDt6iA-B7rMQZe55AbXSDcqA7tMExuMiIxl1SYR8QnLlRZJCToSImaA4Es_PtMmKXnqrCGVZcQ80m3_AvtBqU6FmjjLZGN4CDVHvuJmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=MhmhpIq5piKNkXFLGsL-h6rPWZsS1zMpG5GOJqddkydZcooaRFTEI1fKw_9N7JREKq-muW-kuJqa_E78ohIahpqugVjRTuQQ3JBQtGgT2M4ia-OBaP9-HUUmwqTGa9cViYfgpxy3mc00NzHYZ1zfpABLLBwfJgaD2bnRjL61hilJ6luAHCP9a1Jag44nyxv4vWiwAilwR8js5AEZtEcwmX0iOJCev49X8po0MpgmU_utxIxLQLSyXEhUpk7S2JemFbmteQav5SpzPBNTNme4xGzyLFMRYoUsTOrwXLiqRuMVe-tcSqis26vxiRdDDfEoWiVFYH6dOy-MeollQydxCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=MhmhpIq5piKNkXFLGsL-h6rPWZsS1zMpG5GOJqddkydZcooaRFTEI1fKw_9N7JREKq-muW-kuJqa_E78ohIahpqugVjRTuQQ3JBQtGgT2M4ia-OBaP9-HUUmwqTGa9cViYfgpxy3mc00NzHYZ1zfpABLLBwfJgaD2bnRjL61hilJ6luAHCP9a1Jag44nyxv4vWiwAilwR8js5AEZtEcwmX0iOJCev49X8po0MpgmU_utxIxLQLSyXEhUpk7S2JemFbmteQav5SpzPBNTNme4xGzyLFMRYoUsTOrwXLiqRuMVe-tcSqis26vxiRdDDfEoWiVFYH6dOy-MeollQydxCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKoMmypYUkfsLb3D9yKMfKcKbP6Vm_sLUyFJiHofmhc3d-Dvl7j-dO8AaEdzKAf8Fmo2nzWzTJiUaMY8IpyUX9DLiENzzi-LoZKP0iRf3cvlt-Pc0dpexCr1QOw6-L3VhK6KbT_bNUPKY2jJit4UtfoyI_tZw7j1v4ecUwHhPri2Ydmh55H1iOAvYzfruaOlJL-REdDzloaceKqRtkw4x0GGcPj7hCSHV8bZ0Wj67ncIsVnyz3gZhzAGu3mcronBOPWdxLGJFeygN2scc9b051zH0XEPdOiuNNBxVyHN0vuaPxpnAV-zCybF_j_YHpZwaiR-bPEKcVP5N9RfUfGp3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=m_2hwn7Y5e3ec0orKyFeZ4e4tuEVD1zXDWXOVtsnrmraZJjmwG1lCOwESsOeBrmKcW3FsEAY0FU4mgoF2mujOvyztPsNlZMW7uEoyD1t-QD8lpipPhO41s1aFVX7ZwZDmsNFBkpIdXgaaIf_Ju9Mr7Rq-45_HXWt5_ZxqnQnlVsARrzGSdg1JG-mJOM6Llw774PefSWggKLCbErV5UaC17Z1VRH_ppOjIDN0XrE2C-FrvcMcGADbVwjsHHRfThns_-m5Pltghhb2G__8c3BedN-ugJw9PER26Df_LF9rAAmh57w_jgMqI-Q08BmxVzA7irq3NNuIYqYxOTEjIuPt_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=m_2hwn7Y5e3ec0orKyFeZ4e4tuEVD1zXDWXOVtsnrmraZJjmwG1lCOwESsOeBrmKcW3FsEAY0FU4mgoF2mujOvyztPsNlZMW7uEoyD1t-QD8lpipPhO41s1aFVX7ZwZDmsNFBkpIdXgaaIf_Ju9Mr7Rq-45_HXWt5_ZxqnQnlVsARrzGSdg1JG-mJOM6Llw774PefSWggKLCbErV5UaC17Z1VRH_ppOjIDN0XrE2C-FrvcMcGADbVwjsHHRfThns_-m5Pltghhb2G__8c3BedN-ugJw9PER26Df_LF9rAAmh57w_jgMqI-Q08BmxVzA7irq3NNuIYqYxOTEjIuPt_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=o5vKRp7PouB2_E-0qGb3zBFtwbuMTGFfmwsx8B5Ga9qCbuUl1C2CXrXTIULAMdLasF7ZQdjxGNZ_GSgEmJjDdKI0XuveRxGrobkJ9idu4Pja2HbituSZHZw4Z5GfDz7s5T4x9iUSkGIHTSu1SGL7TO5bFWFXEBUUcct2-CeIZY9m2sQxRM0_NATG0Xeh7DyXpNG__SBzpKCH1IpKgMP-KZueoGQn0yK6yTpFzRjViycBQsDoULWgF2PtoS3mEZ09YQfG69byWYoxIDEY29Yes-AdSNgCYUTcO9S5oAkO-fOqd42nusa12ZMgjKjJHIbuabXDdQDB9WROAVya93w83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=o5vKRp7PouB2_E-0qGb3zBFtwbuMTGFfmwsx8B5Ga9qCbuUl1C2CXrXTIULAMdLasF7ZQdjxGNZ_GSgEmJjDdKI0XuveRxGrobkJ9idu4Pja2HbituSZHZw4Z5GfDz7s5T4x9iUSkGIHTSu1SGL7TO5bFWFXEBUUcct2-CeIZY9m2sQxRM0_NATG0Xeh7DyXpNG__SBzpKCH1IpKgMP-KZueoGQn0yK6yTpFzRjViycBQsDoULWgF2PtoS3mEZ09YQfG69byWYoxIDEY29Yes-AdSNgCYUTcO9S5oAkO-fOqd42nusa12ZMgjKjJHIbuabXDdQDB9WROAVya93w83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=S7VxObG_D5i3IjpztbnaITVKKVniXJYHt5cCYG5S8yYvULavMCtbAmgSBebKEvpYbE-IBvCvTwcDgZ6qsUPXiVB1APmrrJFn3t0s64YmYY96HEFWkHWmIAOgoCqCw4DzLzyykUZ3Bs7-KN2lx8OjWkYbTmvfoa5FlCIfpJpK6y7oPzxqjnVEznVK7vaC9EQxLnzte_ahta_-PhQ7kr_GtLUl-M4DsRmFY9Xnj9BoLo557yldclsPL28GnGrzISXDZAByz3XDS6MGZKKNE0Xs1CN4nxKZs2-sMgRisOdPBsQln9Y-GdK9-XKoUZLlvEyw-amfKWmwluXwj1rkExiEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=S7VxObG_D5i3IjpztbnaITVKKVniXJYHt5cCYG5S8yYvULavMCtbAmgSBebKEvpYbE-IBvCvTwcDgZ6qsUPXiVB1APmrrJFn3t0s64YmYY96HEFWkHWmIAOgoCqCw4DzLzyykUZ3Bs7-KN2lx8OjWkYbTmvfoa5FlCIfpJpK6y7oPzxqjnVEznVK7vaC9EQxLnzte_ahta_-PhQ7kr_GtLUl-M4DsRmFY9Xnj9BoLo557yldclsPL28GnGrzISXDZAByz3XDS6MGZKKNE0Xs1CN4nxKZs2-sMgRisOdPBsQln9Y-GdK9-XKoUZLlvEyw-amfKWmwluXwj1rkExiEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=U7eqytZlFPfwULUdJ10NWPK_7nHe_WZTHf52Cl3zm-Kd4fybGq7AfZBXUFFSmIIcprK-a6PCPaRJDeS0FaLM5csoubv3LT8U1LkRkz-lSGabFV5WZsGMIIBNL-q1RlfApfZqR-DMgFXV5GQ2BrHkxK83rWA8Sh02AFnyHH7V39OLMylKwypOrWduI3XUmVok8BqPNMNaDZ9A_J4cfwThKykByWaMvmBqOXSjebl9UL6vqLH4SVMavqQnQe6klfVrFNAjRTCW_6hUtGcT7Fh2tgCtU7jugTN6g3axg5vfO-uQ0S8tS3bsTg34XkoQMqnFZSWli4FXb4trwPFvvLquZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=U7eqytZlFPfwULUdJ10NWPK_7nHe_WZTHf52Cl3zm-Kd4fybGq7AfZBXUFFSmIIcprK-a6PCPaRJDeS0FaLM5csoubv3LT8U1LkRkz-lSGabFV5WZsGMIIBNL-q1RlfApfZqR-DMgFXV5GQ2BrHkxK83rWA8Sh02AFnyHH7V39OLMylKwypOrWduI3XUmVok8BqPNMNaDZ9A_J4cfwThKykByWaMvmBqOXSjebl9UL6vqLH4SVMavqQnQe6klfVrFNAjRTCW_6hUtGcT7Fh2tgCtU7jugTN6g3axg5vfO-uQ0S8tS3bsTg34XkoQMqnFZSWli4FXb4trwPFvvLquZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXFxuw-jPO-Ol423s1-kJA189e2HaN4SL8nqmdjg2rMTs09uVne0AjKqiAbU_88u0j85_qrNTQnK6-FuJ41mhoeM_uKjckBqbp5Yo5eT9OngKWQEGiDVaktRcbF-z8ioZptPRbW7LNsZiYboscLbV2VRfKTHNIUGJ2g3rFiUjKctcan97HSGnGiSEng44pnbZZZm3QvZWApS1d1UxKAaCg5KasnEN3kMAPPA_pmM-SskH-7rGfnRZe4Jiijh2qiK-oreTmJSzSAjwAqLZFN8_gpCLSRMPK026I_Rajn3hLFM2x-UqNHfkneVEWUj1FElscFa9SiCkRlz0Q_WtY8tRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ApGkfExglxRmWJtA3wI8U3PJjjXk6yt7XZAOp1pl3kpWBNRTL3oqUbBRZb-Uq_EjNbKUdGeF7m4Sa_-QG46KSXEQ4MAg2HBLSr-Qfe5WeQjI13mpFfgqS7dTawh9iYaEsxk8g1FzTQ4wZT8omBqK4ew3LIkseMPSOLaoVDdINsWbl92uKHDtrapO04QojYHgoXL3BCUoHZDrubqBvzHQvR9OiatfYzhJMz0WbV-_BqaXlxEXLpss66rRwbGlCqhHOH5u_U4mqujeGMsIaW73N8WeKIyFdoGT1HdfMD-qWgmAHRxXy-j1EIKKdNtC3eUnmsu9i--AOq9GRAsbNXFqnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ApGkfExglxRmWJtA3wI8U3PJjjXk6yt7XZAOp1pl3kpWBNRTL3oqUbBRZb-Uq_EjNbKUdGeF7m4Sa_-QG46KSXEQ4MAg2HBLSr-Qfe5WeQjI13mpFfgqS7dTawh9iYaEsxk8g1FzTQ4wZT8omBqK4ew3LIkseMPSOLaoVDdINsWbl92uKHDtrapO04QojYHgoXL3BCUoHZDrubqBvzHQvR9OiatfYzhJMz0WbV-_BqaXlxEXLpss66rRwbGlCqhHOH5u_U4mqujeGMsIaW73N8WeKIyFdoGT1HdfMD-qWgmAHRxXy-j1EIKKdNtC3eUnmsu9i--AOq9GRAsbNXFqnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Xrn792TjQLnsGzzTFDNtqmLvvd35VGrTqDWqOeWoUa1le1e_-6-S9nkv1yMouHgGHXTXDrPGIWImS303qRt0o4RoZOWtqlQ2iYnnxEbtmvCvwEqjXkIqB8mr-ZaqaCw6h9oaqCEUpxyshEYW1bfl_M9fCRbA3zbYgNKW5MfGSThTtZPC3e1SIX6KghzhJ5LkvFpPn2WwHX2r8BBeJqEoQOtgVJs1lJPNZJWPJD38xCbWIF9YlCw-wYdi9ZvYlmal-UwLMeIW2_xgo6TgBhoNzpM08_5xrNmfp1s2BrMHQOwEx_7ar1x8UoJHBCJOZWlvVtpxLRP-aBTUGr88B5_BFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Xrn792TjQLnsGzzTFDNtqmLvvd35VGrTqDWqOeWoUa1le1e_-6-S9nkv1yMouHgGHXTXDrPGIWImS303qRt0o4RoZOWtqlQ2iYnnxEbtmvCvwEqjXkIqB8mr-ZaqaCw6h9oaqCEUpxyshEYW1bfl_M9fCRbA3zbYgNKW5MfGSThTtZPC3e1SIX6KghzhJ5LkvFpPn2WwHX2r8BBeJqEoQOtgVJs1lJPNZJWPJD38xCbWIF9YlCw-wYdi9ZvYlmal-UwLMeIW2_xgo6TgBhoNzpM08_5xrNmfp1s2BrMHQOwEx_7ar1x8UoJHBCJOZWlvVtpxLRP-aBTUGr88B5_BFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMzLwZ4DLjsCFj6iVDMbgFqVNnM4KAMfwZvTPLJPrlP-RT8IiUkOOW_pq1pT0LYiVKIG_a7Sm7vIj8ErWr43Ygcr_bjYtaPs77qH_im_zHGRUaxx03QtURN1PAv7bm7j-hBekvNuJ0r7u2cHAC_ucM5oQu4JVGPFcPDfjXHaRRfSrtHOkfnLxp-cjEw3v4KJITcwZUVCBaFrKYaPbsH9q-msELXjT_iyZwbGku8i-av4whgfeBYk3pp-KxOEdMWHQyBR1DaklyvHHPPc7dyrR39BDQpt5HPaxBEwy81K9uN8eE2pnvd9VpOGjhzAFieUdOxxSmVTIbJA_VZe2YBTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxTLWy6R5Wa--rwgXFElMeztsVEmenis-nvMmQzNNb64lQG6UFOSSfXetrptOg59grBUSc7IpoU8L7-TCrNFBNU7vB_kypQVk8rR5KaAHhfK-mfP0xMVqEHy2-8W5nI7md_VIGSMui_f3-pHi_zuuRrasp7mumuJ6D48HjBGp864H2NSavmHplGUEjMywIYBonqOaKfThVQHcZeXeKW2C-p2_n4HmrCU2OS8p33bTEZbXdCQrVy9ya0pwj-7BnVJsN3FnuSUWJ0qBWH1o-XukIRO7WUvBRigh8X9v-euM961m4NJYtSLhwXExb1It8XQoo4kZs8s3Hqbgzl2g7YZkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=OsVChJgkFq-foyZAP0xJ8DsRbMDTjtbAy2RhM0hitFFBUx0pEWk4OCG4re96W3Loc-63PkUd_sJPNLUJTFkQn5MNgsTNgaVZ74x5kd-M5dEnZVnQG8rJz-4ddRqL66dM9gsBxHpBsnW0kaLiSj1ANW4tl0WwvXh76-dF_NaNd3jE9pZGHpugma568w35QjNcgZGUWq0KsJkUKIJEZc9PKcRBM3I0Sv2ug7NrO1qyTeHegcLh7UBi-OR8B9494qvdjftBJCNQjUWmASJSIffGERq2mwVcg3nyt8Y1RwAo1Ja8loWrdDclXDFEN3k3kGQ_4N90U9Tj5EhOeEF4DYagjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=OsVChJgkFq-foyZAP0xJ8DsRbMDTjtbAy2RhM0hitFFBUx0pEWk4OCG4re96W3Loc-63PkUd_sJPNLUJTFkQn5MNgsTNgaVZ74x5kd-M5dEnZVnQG8rJz-4ddRqL66dM9gsBxHpBsnW0kaLiSj1ANW4tl0WwvXh76-dF_NaNd3jE9pZGHpugma568w35QjNcgZGUWq0KsJkUKIJEZc9PKcRBM3I0Sv2ug7NrO1qyTeHegcLh7UBi-OR8B9494qvdjftBJCNQjUWmASJSIffGERq2mwVcg3nyt8Y1RwAo1Ja8loWrdDclXDFEN3k3kGQ_4N90U9Tj5EhOeEF4DYagjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJC9PSkYZGnEo0Ryc9KkCzuzL0P_TsEgt0cvTi_03bH9tN2fnJdtG0Eu2ooq-605w39DrIEHvFYA5F6ADaKczgTIu85qgneh0C25-TmxYfm2h3dwqkbeenjYi1NmOrwwcAbOC3m3g5kmGHlBz3W0oKYxpi8WqH7O8BbPub0RIAph1-m4WJTMbgLoILBXi3yG7yub2t_W5swmgOEQbw0jsbXV-mR3zgNfbXJdhFcWvQH7fivBBIWPZJTuc8OvkxMBWlCK59qxThyZWxMAcZC37GO0qUgtrbZ8_BbacxkJtTZoeOqTrFcBRyo9hIU4N1fTul7NjDWyI8YmOek_yvaFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
