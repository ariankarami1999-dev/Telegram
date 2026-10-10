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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 09:36:53</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUO-pUzMaQhyGvsVujnLlAHmpDkhsvFrTaqCh9DkmnmCsAbGyGLq9DL595ItFJIDJw1pR4MvB4KjA3Zt7HQkRySbIPNN-aeZeQOORmOxAS9jkXu93J1insljMEZEattNJ4q3QZ8rrEUb2mIyz0giVklh5mSr9cKaDRhPpLnA3n0PrVZn4e432GNZdNFWesui_QI1ZCtWRTqMI8S7UOIZostbjSesRTEyEDW9EMBQzbZOvhQ8r1STTy_WuNWQh3bHZFPXJxr8djWMMYz4jjXOLal6rZXOr-E6SsM-RtlDxx0JsMMV-UHz3qOParzNOvAx8gaqz0MRrgCUERr3qj870A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFs-dYQ89SSejfvnyaPCtYViyeH5hORS_Wjy-HF7Xq8oiRkMX3iZa6PwitdwNXfCcWg90OVoAC3R5kmmMc7jj6woNEuDFvGKFYxYjv_Fsk47kBE4fFcXWPKfeOyFFVZHDIs7s58tU_KHDS_B8jbV3J6b1B3vAx9OMUMQDHIdOHKKsa5Bi8Di9JRZ0ZVpircgcnsbdBupPnnxeEKF_u-wj7ZvZHBD4-aA3RlyGWFu542kPseaBXgADPOZ-YWJ_WwNNudxKJzXX5wgUrUgHR6UORBdJJdpdY61GgxFVsCR2d1NDowUniyn8EWUll3zVDIX5FkaMAAwiY6dG6vseKwl8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcGdZi3nDvg81ZyU-GFF0N8IVXpJZAU5RLM-i5EWLe13pjUcpuYtjsRhWwKilR_wJUr4LhLkeB4x5KfeLebhKWz4twakKSvIyijkj4YYqgul5m1BRaSuais7WrNZi3Hsn50Y75tYBbNfAkAwyoLz695kn0XIjLntBiqWrDVxctfyRa_sFhdd_2cc4TXO3LxWxQ17R8Y9Zv6VdViHvIJeqUxvF7CzDie3aoEFHLscF8sqgmKoz3apXCDwl4dVenmjx5IGZiiJO2VA3G6G-_tSbyWOlTjmnB-LtTqP7CJGshOBZfaPJ41RHKqD5SqEDTmXp8g4niVRUMHIxHSd5-NCVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh2BQPiMvJQlUaMDx_sXuh1lGoWwhMtE442ihm22oo57zFcpgMe0s1Nv4-4xcPBWeZysGTIjZ9b7Eed9gxWo6ybx3vqwiF6QEHiBEa-_WDe6Eoqi9fOU8iKL14bNF7bXTt4S_5IpyIKaNUJX4Aad9R15jn_4TuvWXujCSAfqKBoC5e_N_0kChUHLGCYDZVsUux-F1nqKlc6tozyFpuxzc9Xif02rkYg6rGP8ku4hGmxRU_xztkQI23fG0UeOqtqFaicIEM0t0xafPHaXv0V3CAtd_4xbbPzJFlsPn51ofGi_0Y4w9PsVvpkXDLoWu-zY7e_5laMXX_0n7MfZ-c2oFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PonXa1vvfDC_jBYn6Y4OmotSXxfuhoLpRaUg3q74-z8rTmBuCmx5dxQVkmgh4DTkLoBrkJmsv_B2my-1eY_81ZUfXxBNhlTIjJknycs6hNIIU-Auxwd001LeBABXafnJjCQoSfRjzBYE2LCfkedhBkI-dj7CZ46orMCIKSM5lTrMGYodss7dDYI4wup2-4ua0EdNstNN3ozoI7cL31n3JGW_uVtD3vRrZ6dl42PFoW0B2OfN0secCL4FZMSE7FZutKYhQHCDlI2EeJqZoblSA13bcDKPgPZWQql4xJD-ImgRcInfV_8fMd3QPxg4RTw9fTTQgUElatKyn9-rX0qNwQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=LQ4mDC9uhRZ7nTTOeNf_JNPGrSFEbTVKLnf9chIWBXBmTpsl8ow6S-OogfrXtyOWQYZWgfFdp03qdiqNA-QS7OW2GZW1NUQ_EFsZQ8EcwKPEo2QNHrHcXIoBTfYmYDIYUF4e7m8w6pNgcsk2KdQJ8h_1_6pEIiCg_WlU9cTF-Fgc82U2GcOA4Y4sevVwLbDMTKiF3dB1pbEe3NdU8hxAyFa7YSMSQDUk7IxV1A8-rXMoh_ngQ2KsrqG6j742DEY6RRPDRKL0vwj7pgLQCvyAo3cLQzBfJy6jrmH0nkE2t9RHMGyWR-lWv7fHHVKEEIdh6bifAet__LrRpT1Un40qgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=LQ4mDC9uhRZ7nTTOeNf_JNPGrSFEbTVKLnf9chIWBXBmTpsl8ow6S-OogfrXtyOWQYZWgfFdp03qdiqNA-QS7OW2GZW1NUQ_EFsZQ8EcwKPEo2QNHrHcXIoBTfYmYDIYUF4e7m8w6pNgcsk2KdQJ8h_1_6pEIiCg_WlU9cTF-Fgc82U2GcOA4Y4sevVwLbDMTKiF3dB1pbEe3NdU8hxAyFa7YSMSQDUk7IxV1A8-rXMoh_ngQ2KsrqG6j742DEY6RRPDRKL0vwj7pgLQCvyAo3cLQzBfJy6jrmH0nkE2t9RHMGyWR-lWv7fHHVKEEIdh6bifAet__LrRpT1Un40qgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW_rMjsKddgNHkwCxQH5OWv7ZJz_I6eiJbP4FjCVc91B1l9S9SgY_7xSz3MBmw7qA99xwAn-THZSi_JKcmwV3EitPIwQs8874hA_Fat2Jx0TI9EYJflOH58xM99O3v-p4s4D951tGRH6bI3Sk4HKHO0RJJuLf-swrBleauATbCAdOxpbIQez3zNBRAr7uzTPzhGZAxJFslMVd22HEBIHAa7tfanDBvAVzBcHNmf4rtp0heY3lgKc-7wq-u9tWLs6UkKLfZPrgnxEh1LkMpPC1TnJkJorWwIliJ9-ffLDOuTE1BA_KIC6-oMyr2KUB4J8EgqXpT1qH7kvfOE-r78Z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvoNfuE5KVGvzO7wpAPPDAWEAM0RWWatgyvTtKSOzlIHtINP6FKMuruDT0G2zM42h9LiCPc0WNwE3Ve0tcymYoLBKhvHnK56yU8vhsRWpcdvAGQfvhe-GJZL8K2_8-Rz37lUN-RlhlJOFp4TgYrUC5oW8AVLnu45Ps4FY-YV2IHoUpIVOwNdD6UQs4D77rZmpVB5VBEeD6y1PM2GAV_24td_krygEHmOovex7nB9OgjrScNwSrufe1ywAkRPYvUEzfDSlw_nJbIKyHIJ-wfn18hMo7EYe4pWHy7RaxsvmNTa2i1K8cv8dyXWny4fHDnpVX1FrDlb4mLZUEx0BcFLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dba1D8mZEY80dyWv6LlUyQIC5dyckdobRs9BJ0pzWGyijX9CbwdSa-t0oDFrLb62sUIRdebWkSJGjpPux0vSOC-WjZ64i1zEoaZdA5CWS3l4TRp0ffrwI0J_f-CE4QgXDBn-taL1WSQqEiqGJp6WkYtoIvjOfdSvX31n2OSeXu90WAD_7QpH_CntF_Cq7rIifpjM7xlJyAlji76RVBO5Dk3Sre6Voh4m7RmvtWzB0RVxi7dvB4RQsLPMFYw8O-26qqdqpAtrpZCC1g9uWU8fibOnNP8fMPdJsId5HhcyNNEy0DqQGg4MJG2R3J6j5peu_R0iv4-GnYBl204nNttmLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=tPL0PaJ9CO-XrDaI-TsZdRW2VX6lM7U2ULFePjUoJsD70neF4vKXYaxxUTvlxB8-8l33JNbppUOfg6fSVehP3AXmFDE_D58fhSCjxyqFWT3jlp4iGPCkcvUJyBVkvUC3tJB15Y4juwl_Y4DlMd_GVrM-K4du7a9OXITHvnEMzI0LHyP3PbJ2ftJpJdg4KYRVoU4j0EebJoR540bcSDmCFqJpsGQZCEPLZMcl3AfGoEBc6CTDAS5PRXOD6d0OMbrym-NWWCR1BqtfEbSlO33aQGRfIfy8M4k3cEQ5LS_43nRT9qzpcCA3A7Uvy0qXYCBtKfsnRuMQR-FIgRy3ELv-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=tPL0PaJ9CO-XrDaI-TsZdRW2VX6lM7U2ULFePjUoJsD70neF4vKXYaxxUTvlxB8-8l33JNbppUOfg6fSVehP3AXmFDE_D58fhSCjxyqFWT3jlp4iGPCkcvUJyBVkvUC3tJB15Y4juwl_Y4DlMd_GVrM-K4du7a9OXITHvnEMzI0LHyP3PbJ2ftJpJdg4KYRVoU4j0EebJoR540bcSDmCFqJpsGQZCEPLZMcl3AfGoEBc6CTDAS5PRXOD6d0OMbrym-NWWCR1BqtfEbSlO33aQGRfIfy8M4k3cEQ5LS_43nRT9qzpcCA3A7Uvy0qXYCBtKfsnRuMQR-FIgRy3ELv-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=CICnbKreoVzupuILywDctmnzUR33GB2G49przlFhoTAnEhkxREZasI-U7sOPV5ndz7dlP57jDPxcbgs7V6nskndTIQ_OqUsocz7TntWn2ScctAVeTcjJrYT8Krp4DV1t5H9OZ8KTgsn7s-5u1yywL-RpA3itBgA-SqjaBEJAsTKJpG65SsueoNnt8SlD2J4vbXNV8orLktzDG_c8D7CGU-Jy9YCTuI_iuJtMXCtCczcEVYItg6ChjP14II0Mi_eDrWTRCh9W3Pk4aipL2iZiQMWUZ-Yz1vpWReXeLdDdddR3ghY3RTvcMmDIs1hq8lzmd7ObQyYUetqZzxxYfz5q-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=CICnbKreoVzupuILywDctmnzUR33GB2G49przlFhoTAnEhkxREZasI-U7sOPV5ndz7dlP57jDPxcbgs7V6nskndTIQ_OqUsocz7TntWn2ScctAVeTcjJrYT8Krp4DV1t5H9OZ8KTgsn7s-5u1yywL-RpA3itBgA-SqjaBEJAsTKJpG65SsueoNnt8SlD2J4vbXNV8orLktzDG_c8D7CGU-Jy9YCTuI_iuJtMXCtCczcEVYItg6ChjP14II0Mi_eDrWTRCh9W3Pk4aipL2iZiQMWUZ-Yz1vpWReXeLdDdddR3ghY3RTvcMmDIs1hq8lzmd7ObQyYUetqZzxxYfz5q-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvG9PX3fre1WoHYffZWFt65mhEafCnMFuxPkBqaXaHVbg0oP7AWpMpp1zqMsouBOs0l-fYgqDLXS-yApJRO_VGALBi0UmdmhutbGCSHwuHaxPG3sJFvmQEsqDw0mc_t0TnbAh9pJsv1qJXZSK06oAiv9fw8SSU15V-7Tvir5X-48mgm8EEXm7-ewBwrTr8R7_2YjXVxinmfRaJA6ZwEThQ9eTvpLvmRtwjc9faDYxlYL2dsbB9RFr7mL5lGDSCw6bhmWpPbqxSXtIvHmTa4K_weFAhadqj7nkKV8fC1YWzyGyHYeEUBmqeIWza40i2lObqoyfmZDJniPJsZ1IKRxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=XeWvvOVDVJEH_hZg82hYsLnGc_0Kz0NMQx17T2p0mmtf6ATe91ECt4NxkAc7W8AHbVJp18jY9FhVdyvOkU1x3uWK-rm9VMKY25c856j71dlbQHfMfe1XQydULBYlYNGHaD7mKwUUNOLmoaQXafNIuwi_nY6gs5WflGPsKgQ-TVZ11gMWovhQeu484hkG3IkWMbEatvRBx5xo0gnTrH0HD7VfrQpEAmpzFKikbGiLMXRZVZ6GGF_h3U-3Z0RlsIvybt08iVXpxmqkW_OYhs1eppJC2__U6RIl1-1PqhoU9Eq6l86gP-w5uKBoyXNkgei6oRQ2dlRq706RR_Ut-wlUQHS5jnwaT19tLTtedl1pjTm17jni--WJV_G7rafgbraOMwnCORsiAUsI1YdIo5cxIjufeJKpLGVp28Q397f4Bx_WD1YMe5KBjJO8C3b2gzx2O_K7vs7_gkyCMdJIDiHzQjL_ymFQQlYu7K-3sT8dlnyhLOTWm4eYMzkb_pc1AWSgXcaePwXjXDePEsmlfKFp8P2gf_ErRXfJw_gSsDXGUIez82mb5lJPt7uIa6S2NDIqfIWE3whY5EZ6h7kpQZdjlebL8Z4w897ycIuASAydMLmHC3zb0XwzALM9fnzZLl-FUiHutNCYPIy2qJuRyg9IUo8LgR6-wQL_C14SR2CJYgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=XeWvvOVDVJEH_hZg82hYsLnGc_0Kz0NMQx17T2p0mmtf6ATe91ECt4NxkAc7W8AHbVJp18jY9FhVdyvOkU1x3uWK-rm9VMKY25c856j71dlbQHfMfe1XQydULBYlYNGHaD7mKwUUNOLmoaQXafNIuwi_nY6gs5WflGPsKgQ-TVZ11gMWovhQeu484hkG3IkWMbEatvRBx5xo0gnTrH0HD7VfrQpEAmpzFKikbGiLMXRZVZ6GGF_h3U-3Z0RlsIvybt08iVXpxmqkW_OYhs1eppJC2__U6RIl1-1PqhoU9Eq6l86gP-w5uKBoyXNkgei6oRQ2dlRq706RR_Ut-wlUQHS5jnwaT19tLTtedl1pjTm17jni--WJV_G7rafgbraOMwnCORsiAUsI1YdIo5cxIjufeJKpLGVp28Q397f4Bx_WD1YMe5KBjJO8C3b2gzx2O_K7vs7_gkyCMdJIDiHzQjL_ymFQQlYu7K-3sT8dlnyhLOTWm4eYMzkb_pc1AWSgXcaePwXjXDePEsmlfKFp8P2gf_ErRXfJw_gSsDXGUIez82mb5lJPt7uIa6S2NDIqfIWE3whY5EZ6h7kpQZdjlebL8Z4w897ycIuASAydMLmHC3zb0XwzALM9fnzZLl-FUiHutNCYPIy2qJuRyg9IUo8LgR6-wQL_C14SR2CJYgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=JkxAQfTywfaMxb13o_wW5kpsZCj6XYVFfAS_ynfIQuGP6u9IbrW4sqK7rMr3cwpIwan5rUiKzMy1AMX0j5kLaR2BXTYmUA1lZpI7tXF5JRsaqSDhoqlYpkuI5MdQJUlMy-r2F4inrbMiLXiFBQi98wcUtD15gIBMuAqlRkJvwC6bCkyYc0wSDLYvDTFlQEofZo6E-1WOf9mHbMC88ofL8J-hpBWvGWyKPWWa8vyITpZVhnMcxvoZNDo8F4izsE_hmF95ELqqbh6DzUIDxYhqUKkA6Hk7iFzOINBTbbcWYsat3VMH1elGuQ3YHPKdDn8w9rOY_Vbr0ROnCLFENNaEiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=JkxAQfTywfaMxb13o_wW5kpsZCj6XYVFfAS_ynfIQuGP6u9IbrW4sqK7rMr3cwpIwan5rUiKzMy1AMX0j5kLaR2BXTYmUA1lZpI7tXF5JRsaqSDhoqlYpkuI5MdQJUlMy-r2F4inrbMiLXiFBQi98wcUtD15gIBMuAqlRkJvwC6bCkyYc0wSDLYvDTFlQEofZo6E-1WOf9mHbMC88ofL8J-hpBWvGWyKPWWa8vyITpZVhnMcxvoZNDo8F4izsE_hmF95ELqqbh6DzUIDxYhqUKkA6Hk7iFzOINBTbbcWYsat3VMH1elGuQ3YHPKdDn8w9rOY_Vbr0ROnCLFENNaEiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs5wZUwnYSVteGeEcz9M7tHU-ncAJR_4EwpGPkkJiijj3mJXil6ymMt4sZZbt64hSLOsrelg0AXH8x5Hcx6Vc454CCN-JKzrOLEs6HE3eGZJrqJE89b_V906Dx7OEBlvnO5cjdQsJ4KkOqvJvImgA2c-Tjfdz6a4MT5ijqZXX1ZGg4RWq54PEPrDa02r8GNjQf1aMkUBme8YvEzvlvd-FLJAIajZ_qEY2billlnyJjU2eXdOyBlN1t_xDtHB6Qa9nx_LDo0Rg6n5Bgmf5h-wmCZ6vBgTN0K9aLFwDJAQqJRNj6S9egndDL2fWvBAIBE0Oqu4vJOnT2peUtgt877tTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=OKBZ4PPaCypfkyN-JyG-puz1FipDCXfTCYwxVaZxEsS3vn8S1qCajJy7X4Q-sW2pIvNORedeRXD-xLokOD137jyAqYfv1UpHoTcqdf0nG1ShMn73UQ4KZIkjRiOA2IskIa1-05Pe4uRgqAJ_7KG1RQebD547CZonhfQ8j6jdrIVOgzZW0FAGu7d3M88R05e22obH3tGJwirgD6WW5z8gRQWjdU-aARNJBoHixEI68DwttrrYpjDRfCihco7h-qjuLTZ28QcLpXM3PGIZXLUaIp_3dXpAmocbirJRoOi7Sr7CFkNYy0gnm_ibK2y6HCrZcBoJyvUJGToYAWodCgxqiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=OKBZ4PPaCypfkyN-JyG-puz1FipDCXfTCYwxVaZxEsS3vn8S1qCajJy7X4Q-sW2pIvNORedeRXD-xLokOD137jyAqYfv1UpHoTcqdf0nG1ShMn73UQ4KZIkjRiOA2IskIa1-05Pe4uRgqAJ_7KG1RQebD547CZonhfQ8j6jdrIVOgzZW0FAGu7d3M88R05e22obH3tGJwirgD6WW5z8gRQWjdU-aARNJBoHixEI68DwttrrYpjDRfCihco7h-qjuLTZ28QcLpXM3PGIZXLUaIp_3dXpAmocbirJRoOi7Sr7CFkNYy0gnm_ibK2y6HCrZcBoJyvUJGToYAWodCgxqiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXVKEC1vDsHrDNaSoiFmkRSyzvy2H_PwBN6c-A7KqclQRPyNZ4fUJ7pkQvhnSAuixiNtcmDmfwM_Ot__77cJH4nscIiH0b5ktIzEnOrwD_AUpEFfn46Mc7xt-8WWeARq6KBK2nP90myipZ-c3EsQjIaGa3TGFn45FwlpGbMu5RYYNBACqlKjLp5C64iHbgdZAZtJ5Ze_ITFDOB-h_D2_trcf4-DMz8czN9-HzcI_q2MfJ-yGE3NOwylmpzmAenSp_yZpp4NLrCn2sC-_47jr8aMBK9ur7kYt7JivwtNQUMaFofJLNIixHN0hBfWAMP3XTEgN1ZhkxA1UAHOn_rSmxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLFyTSFUvpoWBHLh6uisquxzMH9xbL6Y0nOiy9vWEDM0qncTXCABMQk6xtIqLdHVX6c-SL_LBYvDgyjF-PudBUe2neaqvZsO4m9booYtQlhCcFaP9dXiXE9K-_WSQ3vqopwiKpINq6Cnefv8oBSxr2vez53q_YC8_ahaRBlluISV8-AYFEulqem77t60i-r_hfnZHBXP-_xMaDaMz7V3cnGExKPCdBzdQkTLFAwGRxpI22rhThu8kx6P0gB8OQPuvkIk1cCyn00-VvJCXrrSCno5PP8g9NXEa6GkoscZD0CzLp556M3nQi0uko0CKnB5pYKkaxTeYYiYeGN4G5yboA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=HsIwZ-nRrivobLqNAuJdZAZbgsdwzzEewQB4HOR5KIFCL9Ll3mHMjV5flpOfWPfUVH5WzSmBwETOXkfGMpH_0x1DpWLW420eAnp-BcBKLb9ZpN821ucII_f7j-do-YhfCwQg3CrlLfcynp5WYHAJ_qSRsdgPSWPDEBWtaYerZ-0AZAz5bQpA_LdXMVC5oUgHa4yVSeUtPihci1GmfWaPn95SwzIiX5T4NuPkBSvx4g7jt-XwaJ2wRPtONsQXnA-OaRwd8C9RxpKZbquD8Gm8GC15Lh93NtDnJIZ5bTBEbN0Vvo8LZaLE6VBYpyz0j7lKZkkiu2o_f7HfdAQnlEFBizv33wcKDJpaLaaiFE64VMc5AzM79krLrbMwBa6oZXwFZTFB9gwlyVYubpveixeT_M9sKGGOdEOJTWgmMKb9NdjrlTFeYiEFsmX4sx1bAsulW0D_KQNotPKMQFTFpqIQ-QFDQHy3nMm9DWxJ4LQBmIsDINKSw6DFh4vyr-Lofr2dKEcVtQy0SSmxk3mk-gUO6rEmSsOhZ0Q1sG9DfgM8TIRIf0zPaFTw4k8L5SkWxL8BRjzWhy90nF8s1asnQhdnG3AmeX3sGsKRLCVpjpydOjEmXPHmk0a9HgQwa8BiH0272K71IDxxjiCg5bQXkoEXkyXsUhdcdqa3NQGOTUxLtq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=HsIwZ-nRrivobLqNAuJdZAZbgsdwzzEewQB4HOR5KIFCL9Ll3mHMjV5flpOfWPfUVH5WzSmBwETOXkfGMpH_0x1DpWLW420eAnp-BcBKLb9ZpN821ucII_f7j-do-YhfCwQg3CrlLfcynp5WYHAJ_qSRsdgPSWPDEBWtaYerZ-0AZAz5bQpA_LdXMVC5oUgHa4yVSeUtPihci1GmfWaPn95SwzIiX5T4NuPkBSvx4g7jt-XwaJ2wRPtONsQXnA-OaRwd8C9RxpKZbquD8Gm8GC15Lh93NtDnJIZ5bTBEbN0Vvo8LZaLE6VBYpyz0j7lKZkkiu2o_f7HfdAQnlEFBizv33wcKDJpaLaaiFE64VMc5AzM79krLrbMwBa6oZXwFZTFB9gwlyVYubpveixeT_M9sKGGOdEOJTWgmMKb9NdjrlTFeYiEFsmX4sx1bAsulW0D_KQNotPKMQFTFpqIQ-QFDQHy3nMm9DWxJ4LQBmIsDINKSw6DFh4vyr-Lofr2dKEcVtQy0SSmxk3mk-gUO6rEmSsOhZ0Q1sG9DfgM8TIRIf0zPaFTw4k8L5SkWxL8BRjzWhy90nF8s1asnQhdnG3AmeX3sGsKRLCVpjpydOjEmXPHmk0a9HgQwa8BiH0272K71IDxxjiCg5bQXkoEXkyXsUhdcdqa3NQGOTUxLtq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSSu0OZ5mtjTAZjnLt0awYhUgYAXupq_2d0ktufj9aC-urZfF-imd_c3K4rj_8oj6bmXvqTyIIfosiQbacZKp2sfshsfk7_3zvDCZqT_3i8lx0BIG45NYF8y_IoAhMhQAg0QpxvQAxTapbr0ThMnvVRSfoKv1hluuBAWrwYMTbhZTc2wMvGC4XU5DtBSIxIkNsfGgwCoec_FZ0GPXC5QpQiqdvPcw340yALijYSPtSnD1aMglX2Brwh_004pfq4iC4EhFAThGO_quHmVEK2Js7IGOt5LjP74x4zcDfwVMZ0ERB8xi86NXUjb850NEwPaCNZhe1Vk84z-UGUB341V9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvZTcSGa9d3d6bQ3ijKGz8hLuzVQ9u7lLF22vjN-l4MybxUOUHXiwMiEQVyT45-QBgfg7ql5PQ_Rdo31iInW9adiBg5uTqvaoGVaNMZAoxY11oy6pLtxb523JuFS-kWz5uuDv-KVoVno4VjFGTawZwCLct9dZBXYQfKXCZbg54C4bLWlkMvfsdX8MYih3X9MkV0jWFvVgEVx_hZrn_GEm2tRiIozjJ01GKdYFPpQJS5OOKjl3GRC398akKPI5tY0gLtOH3WSTdduN_NNxKaBOhmbM3I0rhSOTvX7JHHZxGjUuWTE1e6L98GVS7uQ-v8Dlhidr8XIz9F6Jueyj0qjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=vddUZtaDWVGYrNfwxZKb2d5jAp3UModJPXgyS8a8Df8InstF2DXZs8_F-l60rG0oXx1WB4s65V95wHdGngOFDe4r3vVQ1NKU_s3AOb0UjkENZtaaXb7EMetYbNAHXIO5AdK-6AwA8KiG4padMLSlzTit8yhbO25Iu5Nmgh0Fjcx6_3q-vZtKRgU11ZKexWwufH1Z9qOnWAYguJm5vuUEkmhG_yyplqJjH1C4aakHCP5jv3X1u_n4knLfn6atOX92GLVl7vb90wR7VXYsAlkPWumTCBPssCi47xdz9LRp0JpUGG_L29e_gMKWV1Qlmj2krXl0u5zlj9nLjKu6Th5UPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=vddUZtaDWVGYrNfwxZKb2d5jAp3UModJPXgyS8a8Df8InstF2DXZs8_F-l60rG0oXx1WB4s65V95wHdGngOFDe4r3vVQ1NKU_s3AOb0UjkENZtaaXb7EMetYbNAHXIO5AdK-6AwA8KiG4padMLSlzTit8yhbO25Iu5Nmgh0Fjcx6_3q-vZtKRgU11ZKexWwufH1Z9qOnWAYguJm5vuUEkmhG_yyplqJjH1C4aakHCP5jv3X1u_n4knLfn6atOX92GLVl7vb90wR7VXYsAlkPWumTCBPssCi47xdz9LRp0JpUGG_L29e_gMKWV1Qlmj2krXl0u5zlj9nLjKu6Th5UPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=KpR-Ps7toZIanYe1Zwm4iy0Ga55DXFZKNy4tdneaZH5eFjXO_tqPrLySZzwcAroF_LxaAcqoJmylBbcSnjBwt3R2CTqDNcMd2UZoQJVTqDCsmZ2tpgMCEw7lisAOG5cBWQBZzUxPN7l2MMxPk87gfIFMQQ5y8xgZeF1lOtFwWUsNEGm6c8S4XMBuL1sBGDf8pYLRL9jIUPRl5ruM3SKbXxEibGVksKc5UIlyog4FKZlACr-32pd27oyYNyrQXdCZg4zbe-wAyY05zKfN3kg8wSd_d2u48k_kbsB6PSBVceGkRKDZc2MS20XXH2QpgXuZfbpgOEa8ZIdvgNdvDAnrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=KpR-Ps7toZIanYe1Zwm4iy0Ga55DXFZKNy4tdneaZH5eFjXO_tqPrLySZzwcAroF_LxaAcqoJmylBbcSnjBwt3R2CTqDNcMd2UZoQJVTqDCsmZ2tpgMCEw7lisAOG5cBWQBZzUxPN7l2MMxPk87gfIFMQQ5y8xgZeF1lOtFwWUsNEGm6c8S4XMBuL1sBGDf8pYLRL9jIUPRl5ruM3SKbXxEibGVksKc5UIlyog4FKZlACr-32pd27oyYNyrQXdCZg4zbe-wAyY05zKfN3kg8wSd_d2u48k_kbsB6PSBVceGkRKDZc2MS20XXH2QpgXuZfbpgOEa8ZIdvgNdvDAnrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=TYSOR94xfnJ4KEZoWJ_2ur23baPflOLOs0POslPSYjl4HII5ZALVbh6_vEJKx2vGZkMHol7izsrP0fjxCNsosiPDrpsfRkKRFL3kkMFQ9KtZZCp5KazkTIMBo4-49KPVnndQH2UmtH1z8psONi_VP21uM64GLRE5i7yPbW8Sk1b6FM6VVP7dXS0dcGtM33PQnOtureUFuFJNgmtix-BDZRus19V2ZWmmuNpKTqUeNkli8M3DnQxvLvyu-bcxj7oVRKIQEPDR1pb1xPCjbJEWgVas5hR-y5Tz5-GnAtWnrdl7vJSmdpyQy-d58iYGH692zeWzmC2bzT-JG3WDEeJNlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=TYSOR94xfnJ4KEZoWJ_2ur23baPflOLOs0POslPSYjl4HII5ZALVbh6_vEJKx2vGZkMHol7izsrP0fjxCNsosiPDrpsfRkKRFL3kkMFQ9KtZZCp5KazkTIMBo4-49KPVnndQH2UmtH1z8psONi_VP21uM64GLRE5i7yPbW8Sk1b6FM6VVP7dXS0dcGtM33PQnOtureUFuFJNgmtix-BDZRus19V2ZWmmuNpKTqUeNkli8M3DnQxvLvyu-bcxj7oVRKIQEPDR1pb1xPCjbJEWgVas5hR-y5Tz5-GnAtWnrdl7vJSmdpyQy-d58iYGH692zeWzmC2bzT-JG3WDEeJNlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_dDQ4SY4HHWiLDJtZrcA0O6s8IL3o0fe8GJUtf0oLf_hodNFu29RXNVkB-OgrjLTE5zpCs0KK6XXoqtKLPVsbjwYy95qIPA6GzRajIxCefbAz6NE43EgXZoEbiGbn6JiDgi4kXTWnUH4coQvarG9XIKI_DhUHEWvb8nCtqIcL144T1ZjWXcFj0XHhmtjtn4DbyJ3046HdXE7Ygpcg19hmGcXvmfuEITzWInOG4Yn_v8v0OMlYyWnf_bKOKXU3v-Vx7i8l1tVufHgt2-nvjb5Y5ZILqn4EV-2vhl8Ll_dgnNZn6tEJKlJ18mEK_YorUxSEF7MkzhZ7IVQMf5E6ePtg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsn82Pg17OIRGbeb-enxV-LxTBmQgMHxHepG62ijUaOmKQQAS8pLUMEOXuN6I9ZquytOLWoMlKReZfQKZTFVU6uNVsM-WHZrQWvgz9mcWV-QRq_L0X4l6EyQKjkZpt19wDfwUVFPt0AXst7AaayRaxJp288fdwux8NKJuxLjJRRrkn7p7b41jwgVF5QEUjQHsrElQU0U8afcNDvUcJODdO0znik_-FDO8lY3qokUgr80SJ9czH43rgYEGBfV52EFGVYIcMG15pAbENMyNhHVF5m9fBm3s-M1GkurujvkwbSDELLE59EyLdpIz4DyGXizbL38e8USMQ1CmmuPq84pyYls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsn82Pg17OIRGbeb-enxV-LxTBmQgMHxHepG62ijUaOmKQQAS8pLUMEOXuN6I9ZquytOLWoMlKReZfQKZTFVU6uNVsM-WHZrQWvgz9mcWV-QRq_L0X4l6EyQKjkZpt19wDfwUVFPt0AXst7AaayRaxJp288fdwux8NKJuxLjJRRrkn7p7b41jwgVF5QEUjQHsrElQU0U8afcNDvUcJODdO0znik_-FDO8lY3qokUgr80SJ9czH43rgYEGBfV52EFGVYIcMG15pAbENMyNhHVF5m9fBm3s-M1GkurujvkwbSDELLE59EyLdpIz4DyGXizbL38e8USMQ1CmmuPq84pyYls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=MNl3R_gOwXgAQK0YC7CdcGTilPCgv8lHeb3Y8Jjm_3dPb0silAQTUHWks-LHu64ck2QlIaBq0ewa2Jn1pHIVg2M1-pD4d4HEiSe_mjYGTbO-pSDkvo07oG7fNLD55f_NCjUfVeB_4zJ_xw-PECyBvXQVlNSci_qkZogDLSraKKLeLnz1-JmH4NCfsEoAn9i_LVjR57alDAcvrG32J_5GMh4jsibbhz9ppeJnLHsLxwKgj4stYp-7UKUeu85PQa776O6ZreMcOzhCKNwOycEyLYUL94RPa_ZmQmeow6H8eKw7KfM3O9vVok2PH5tqwYkdnPyRquTuvpmq49h7DfDImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=MNl3R_gOwXgAQK0YC7CdcGTilPCgv8lHeb3Y8Jjm_3dPb0silAQTUHWks-LHu64ck2QlIaBq0ewa2Jn1pHIVg2M1-pD4d4HEiSe_mjYGTbO-pSDkvo07oG7fNLD55f_NCjUfVeB_4zJ_xw-PECyBvXQVlNSci_qkZogDLSraKKLeLnz1-JmH4NCfsEoAn9i_LVjR57alDAcvrG32J_5GMh4jsibbhz9ppeJnLHsLxwKgj4stYp-7UKUeu85PQa776O6ZreMcOzhCKNwOycEyLYUL94RPa_ZmQmeow6H8eKw7KfM3O9vVok2PH5tqwYkdnPyRquTuvpmq49h7DfDImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_0TthhbkDXtD8k8xewB1E62yXfTMG7Ns9G1l1WTj7OyYP_iG7gcscIPXCLzOM2n5XTDu-uaqidRXXcCnM-1fiZjRdGxXWPNX8PTvSQ0NobRp_OBXL_qia_wl5JK-2pcPkASFWzl1SJtUr6NnDQj5HewnI6BS67MEZvYgL6Nz8LZZawURXnjroWjQtQwdjMGFlopX6UrAb-9N_o-WEbub4MiPke8kWi-t41ees2aBuV0-myKHx3k7ggwPAqn3caQROa9UmsYPYGUEh6k9E_BmPvVaF_0_2uy5pY9g-CLiaN9lxarofMtnSew5OWcEeM7R6tdgXDQOTbNkLae7c0ZVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=dW9XbT-czCce6BCLdoyplX8KJV66HptflffHEz6x5TgiQhlZcfNJL0CzqBUliz_ORhtXZzjDnBwr-iPQz_wHfvspdxdFspgYyznMqRixzQCNPSJ9ZorQTCeDNzyVFicO4uQKbhsgy2xstK3SrhgCur-VJaJw9Kf5PTj843tteuWJaPv4ICWdo3_-qDsC2hcEsCyJmCBX1NUnAHDr7nFlnCMO5_yE-D8URGT8aiZ0TdRerY4ml7UIO96aZbwJ09exSa42kP_AoVpcNrLFxwknbY4Ob6LGCLTTuDsn50Habyh6-vTWCzkvigSDwsFs9xULDEMpCUsT-BsNfn984_b_9YgUMsP-DkAyqmkEx-9Rlf6j8-dHh0cxPX4A8eRh3efUMUbtLDh32XtnGNtoOtJmuUrYp1caz2AUAmXeyceturD7fPqPEHsNiP8z8OzBYd7QJaysAbTsro2R004hxAnVDgjO9OZU_ybphZntqzkmJbeejjZxpr7YYWuJrrpiklygZQFiTv5vgZViVGfH5YON_1ImP6G2uFiiU7Bl1Cd8dqQtKW-U_aBE__ShFsyu6MBxLNYCSaSEPllsvnn5BNTGgW3O25d2BOWWsdUThNlDN3T0OJQGBOYUp-_dewaeK5WqB7WIMzsZvA2O1wfqG3nIZYhjZOHE6KxZi0IQanbEEfo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=dW9XbT-czCce6BCLdoyplX8KJV66HptflffHEz6x5TgiQhlZcfNJL0CzqBUliz_ORhtXZzjDnBwr-iPQz_wHfvspdxdFspgYyznMqRixzQCNPSJ9ZorQTCeDNzyVFicO4uQKbhsgy2xstK3SrhgCur-VJaJw9Kf5PTj843tteuWJaPv4ICWdo3_-qDsC2hcEsCyJmCBX1NUnAHDr7nFlnCMO5_yE-D8URGT8aiZ0TdRerY4ml7UIO96aZbwJ09exSa42kP_AoVpcNrLFxwknbY4Ob6LGCLTTuDsn50Habyh6-vTWCzkvigSDwsFs9xULDEMpCUsT-BsNfn984_b_9YgUMsP-DkAyqmkEx-9Rlf6j8-dHh0cxPX4A8eRh3efUMUbtLDh32XtnGNtoOtJmuUrYp1caz2AUAmXeyceturD7fPqPEHsNiP8z8OzBYd7QJaysAbTsro2R004hxAnVDgjO9OZU_ybphZntqzkmJbeejjZxpr7YYWuJrrpiklygZQFiTv5vgZViVGfH5YON_1ImP6G2uFiiU7Bl1Cd8dqQtKW-U_aBE__ShFsyu6MBxLNYCSaSEPllsvnn5BNTGgW3O25d2BOWWsdUThNlDN3T0OJQGBOYUp-_dewaeK5WqB7WIMzsZvA2O1wfqG3nIZYhjZOHE6KxZi0IQanbEEfo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhkdAVqAYUQv639CiA3PBBnp62Q4uUnNxLIA-q8dr1GhGI5fhAth8It7B1bYDTCiUkZa6OgVTThnUS4sRvUrFXjcGdkh1iW-0ewRNZQfgbBDECME2_shEWMkKmFEV0cW6EH7KR4jox6bXQ0hjj7uDRf-LPEnDtdkra9GDucl7n5mr4DxJm8yW87U3nrlxDjh_FBw6b9qfwneMormndvsqLbN9JuvjaaCeZPLBnIvTaBOpiO3DmDT81bd53saLT4o8z0kudMbGI6u-Wq1h5VL0dADbsjJF6j-a-nb4J5dCLp32eqHydugSAVRuE0PNt889iTzhB6UKGGqklPutdP7yQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JDtWsPdClRf042kM61XA50q3H2rTaIE4h0fhr1IkrbFQm2J2yYQkzteXLJRfz26M3G7ludbHUfQe7aDq0QVSuDz4czqUhrftNj0IO2pGyFyIZzFtzUhGCz0FlV_UgKOUtCHEOh19yrmtOurDzjvElYjOfVP-bGByEa3ldHZW9wJzP_qwYnLClfN4m4j_QZDrhHTFwVQU7fnd3O8uw3k7S1xyBhBuGX4-2y1d39nHIAunKCPt6PvCm1988EPhlYOxA2dUa-2DTPPBqzelzsTb7RKvBMxG0IC7IG5ROIg1q_nedGd9zxmKIXRVjKq6QxOz5w-GPnd8AmR-TSPZGleskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JDtWsPdClRf042kM61XA50q3H2rTaIE4h0fhr1IkrbFQm2J2yYQkzteXLJRfz26M3G7ludbHUfQe7aDq0QVSuDz4czqUhrftNj0IO2pGyFyIZzFtzUhGCz0FlV_UgKOUtCHEOh19yrmtOurDzjvElYjOfVP-bGByEa3ldHZW9wJzP_qwYnLClfN4m4j_QZDrhHTFwVQU7fnd3O8uw3k7S1xyBhBuGX4-2y1d39nHIAunKCPt6PvCm1988EPhlYOxA2dUa-2DTPPBqzelzsTb7RKvBMxG0IC7IG5ROIg1q_nedGd9zxmKIXRVjKq6QxOz5w-GPnd8AmR-TSPZGleskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBN_mp45x1xEgsA-1SlkplRE83jfi4vMIvUmR5-ecHVl3UDJqpExi5yA5rOYTXzho116pyxy-WTPdsxTj9PXeBwqrP5JCWGXPaw-sc-8m4Mso_KEahjGkneR_H2vtx99AiXDrkJJYkun6SCwOoT_uOnF_iAvp0fYCnEhUchYahKyimKgR55rlDJes5frJ9RHrPf71molUJR5MT38KowM96zMkmWPm9w47HA5hPQzvkgTvxYB5FVAYc1aEnm3GxggMAcXTOuH1gPqtZ1MAXZFU_spiZx74_C6MUv2Qjdy35PABnYzD8cjlcYDRjkAV5qiFtkaeYZuuKZWzcGgylX6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUiD1Wx2UuNaYFTigMotW536SWouGEvrUFkN8OAUe3bZZ7s6hO3fSn89X67Fpmcoi-W4MvWRyTca9kdABeVFXerTnyliIk_ddAfgYdqDCHY6VX0w7k2b80YDiT_qj2p4BAnRLM96J00guOkuNv6l0uCzcb6tpVaEuyORpEJf5MdfPffReyFKZyTEskIROrGXea3ja9Vy3UblaBBxgtAbIdWEH00ue8swlfAmBfy8XmOfm8K2xAzIe9_86iDdlaB8poGod3LUeVlb8Aue0x09UR5gnfwBeXHgLq5ep8XR1l-kCuo-QtTIXgkfa663KZJ8qfKknULAUm9AoDMPR4ccbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPDWanL4Rkixw1KnnB76XKFuVaE-XDHl79AjRLn5Rsp-cVjfoTYlK27cQQC3yCjmjy3uDyDyd3Y4DY6RZEEo84JtjeREMUj4MzwUoO-fmQjSrQ5BtaO76nY-qPGWpwrKBlWEgS2Tpg5W08yQ5h94WOZgb-gT9O7dbHS0lt4wbnIfi-fnVwGDsPOsgurpclPPO5GSCLHo7dqfk2Yn9D45Zfu4JZlj-hn-oK50OuZOFL5ZwMRsS5-3RwSFWYyHTvKV8GZufqXb0aPOD2smj_gGgnHLWEQXYba_JkLoBkdctzuGaHPIPS31lgrsF0hoFdIimEsZWcKi2rRrj3S0tjnZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=EsfsIb7ueqiMHiQVhhleTjzuI6X97pV3s9H0OGZzXfJIU_FgRkQw0pDnLOjMsF5oRAk9cXDcYGyUHtRNuz4IpKQGPAu8EjYi3ZVQ5xOqupQN6pEkILIG2BJVuIOdUeJezrJlyAFZeSm4eBJKsFuXaLHiOSVEvjkpyY3b-ZUGGsylEgrvJpR1DFG25zXWPPjxTUdqOugTZ5yk1gGjyCTn4MajADWYA9ZRREPPfMQKtjKmFfMtdQ5Lw2-mrwqyis8kIvmzi5WWcddmOE2SI7BtAg5CBagBFBAXLtUGpMVUR0TmwHuRX8FRhbc_S_jT2o0b_Q-3JVuqr7UE2T7WFs1BIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=EsfsIb7ueqiMHiQVhhleTjzuI6X97pV3s9H0OGZzXfJIU_FgRkQw0pDnLOjMsF5oRAk9cXDcYGyUHtRNuz4IpKQGPAu8EjYi3ZVQ5xOqupQN6pEkILIG2BJVuIOdUeJezrJlyAFZeSm4eBJKsFuXaLHiOSVEvjkpyY3b-ZUGGsylEgrvJpR1DFG25zXWPPjxTUdqOugTZ5yk1gGjyCTn4MajADWYA9ZRREPPfMQKtjKmFfMtdQ5Lw2-mrwqyis8kIvmzi5WWcddmOE2SI7BtAg5CBagBFBAXLtUGpMVUR0TmwHuRX8FRhbc_S_jT2o0b_Q-3JVuqr7UE2T7WFs1BIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxsirHlkfHO1-Xkvsd5LLwoHgU5xAt7FhJ_LZFvK9SOLqWMgdRtcE6t7RqxWBMRYJX5vy26IjiIqjCsD_pMg_mjiog0k3rcL__-01ptxiA6jwcXTjwbxdqCKqUwE1b53ulqr5asARW8vBtM3GJtJjK6cZWeVXDhGz4z2TrZe2HvjSerlf2iRslMV0grt4PcpnbotImGLpktZ7Z0sjT_2obBJViLkxpob1HLWmG5FTgFlc4QNpeBKCztj6QHr3gsD4CKqNLjH09ApFy18D6HfxrOfWPr6vw8tjPhoD9t9FMtIjCEr-PES4WXdTFeRraLQ3x8mhHDzyYVoU9SuPFnYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuyCVEDTejE9cGHdxoGQgidR0SQ4vR1FFzHcp5EVSRmliABNhDK66dzWimNZna-PGZlfPc_Ku6y6SdNqv3geuM2aRsQmIMY9iWCyAGqs6Iof_6wE8VC5VkbMRFAd_wyN4z_8fjhpo-MUq7CeGjyQaxkInN7ghm6J71aIPVjxi5wAv2TrSDNOnQeVWvi4x-kyardYLWLQj4kVpA2sJd1Tov_6tXkl6d5KSrQDkw7VpCBi0OpYOnQXhS3chG3WwylPoXtChNUAnAmiuRVHwZ4fWcBW7_oSCPz-RqD2rk3j-0Ir_ZUW3lNT1-7xozhN0QAp6X9o38anuu6qMyvl3MFraTvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuyCVEDTejE9cGHdxoGQgidR0SQ4vR1FFzHcp5EVSRmliABNhDK66dzWimNZna-PGZlfPc_Ku6y6SdNqv3geuM2aRsQmIMY9iWCyAGqs6Iof_6wE8VC5VkbMRFAd_wyN4z_8fjhpo-MUq7CeGjyQaxkInN7ghm6J71aIPVjxi5wAv2TrSDNOnQeVWvi4x-kyardYLWLQj4kVpA2sJd1Tov_6tXkl6d5KSrQDkw7VpCBi0OpYOnQXhS3chG3WwylPoXtChNUAnAmiuRVHwZ4fWcBW7_oSCPz-RqD2rk3j-0Ir_ZUW3lNT1-7xozhN0QAp6X9o38anuu6qMyvl3MFraTvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=G7R0GG3UcmDbx3SKoHaVTbFNOo6Hh_pVPGl6AnuBxrc9kx_5yP2Jx-UQwE36_0V4rxMNjgU04WtPgS_PyrB59OIIfDy3WWkapdwnN3CILrINnPL1JXV5uqsm1kOgx9H5qFaqD4WFCaQLWng_O68T1Lz2pRPC52bokl6tKDwe6wkwP4JU6tgEBJi63kQMMQCvrvnundpKhQ1kTcfIs2Mze6AeZ8utnkQCIzuKviv_njrAXO5T6axvzfBgEuoV109_D1dw2Ch4hF3bqSBeLUUrb0o1n7rkybqWoCaQl1DsoRNWctWK0UL6HKasVA7kniNApxTd6AuLYmx-Z4spNdmo2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=G7R0GG3UcmDbx3SKoHaVTbFNOo6Hh_pVPGl6AnuBxrc9kx_5yP2Jx-UQwE36_0V4rxMNjgU04WtPgS_PyrB59OIIfDy3WWkapdwnN3CILrINnPL1JXV5uqsm1kOgx9H5qFaqD4WFCaQLWng_O68T1Lz2pRPC52bokl6tKDwe6wkwP4JU6tgEBJi63kQMMQCvrvnundpKhQ1kTcfIs2Mze6AeZ8utnkQCIzuKviv_njrAXO5T6axvzfBgEuoV109_D1dw2Ch4hF3bqSBeLUUrb0o1n7rkybqWoCaQl1DsoRNWctWK0UL6HKasVA7kniNApxTd6AuLYmx-Z4spNdmo2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=M37lktgXvt2-eTvEUuG2hOYNzEJCivRQyTHMIsgIHkhqKFeNyNO6mjpIk9az1SqCdELyyIceHcIpqBEdpHWXuIhpXnF-j33LIU0FVwu4ILl18KTT03Z9Z4ngFnDAFtbhGxN0SqJ9e6EEIF1SzO0MAXMmFe5UjirWRWuAxPv2qA5ypkFeRsSEnnLQOV9fRboDPm29TZGovARLvjttJWLMciVrqauuircXWe4zJkTYMzWL9Ddlt34itfYyX7KLhT_IFfCqXfltPSLzpZPasvqQnVXImL21ViCN4pw8Y6hUAJyMLsdFm0fm9vQVmSEnCpbRNs0DQFG-h3wUqCzfESAAxUjbqH6DW4WbHoLl6dTpTVTtKcf1jebk5GXFGZTcooGwok8_nnZmv84HUdHOzZXhzKLqKQ6-QC8DMsowkyPJXekxxbpyexDZ2YlaR8bEygli3v0c1MthiYI7ayu54ufCKt0X-uie1eF_AYQ5kvuWLlLgfc8PqsIrQgqHZ29XxGBBarASYtBqQL_PWdh52mgHhTqGb2dX-5-F7J9kq9klVEVDJVrHl-Z2_1lkJjjVy3VRq5yP9b2ulI6Q5v_oh5UT-ScUco53-la6nj3ck6VdgxZyjfnVo9-6Z2uSk8TD5_STklrZ0iMwVpa-LnfyK-ASUrP8A3bzwW23uS_N8eX_PBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=M37lktgXvt2-eTvEUuG2hOYNzEJCivRQyTHMIsgIHkhqKFeNyNO6mjpIk9az1SqCdELyyIceHcIpqBEdpHWXuIhpXnF-j33LIU0FVwu4ILl18KTT03Z9Z4ngFnDAFtbhGxN0SqJ9e6EEIF1SzO0MAXMmFe5UjirWRWuAxPv2qA5ypkFeRsSEnnLQOV9fRboDPm29TZGovARLvjttJWLMciVrqauuircXWe4zJkTYMzWL9Ddlt34itfYyX7KLhT_IFfCqXfltPSLzpZPasvqQnVXImL21ViCN4pw8Y6hUAJyMLsdFm0fm9vQVmSEnCpbRNs0DQFG-h3wUqCzfESAAxUjbqH6DW4WbHoLl6dTpTVTtKcf1jebk5GXFGZTcooGwok8_nnZmv84HUdHOzZXhzKLqKQ6-QC8DMsowkyPJXekxxbpyexDZ2YlaR8bEygli3v0c1MthiYI7ayu54ufCKt0X-uie1eF_AYQ5kvuWLlLgfc8PqsIrQgqHZ29XxGBBarASYtBqQL_PWdh52mgHhTqGb2dX-5-F7J9kq9klVEVDJVrHl-Z2_1lkJjjVy3VRq5yP9b2ulI6Q5v_oh5UT-ScUco53-la6nj3ck6VdgxZyjfnVo9-6Z2uSk8TD5_STklrZ0iMwVpa-LnfyK-ASUrP8A3bzwW23uS_N8eX_PBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=GsPxYm8HxzQdmkjoykc1wEeC-TsqwZu8dRMQyegHh5mVKVKcGEUBWxWRfZ9N4JCjHfY38efZPYfkhCg6P6_PaaK4re84Mc-hs_FGZrdklaLLAA56ZdKuerZgQ9feWG2ydcwO1Qi_0P5lKvp0WxfyBxNkhrJ-Z8zEZy289aRL2NoFhnaKQ4yT46lqJGvtSDiGg10VOU94zvjEp4l8nrgKzgsVZtn21ccd6w43F72FiwiNagVOrtAgP5BOYVF4MpH6MEuGM_iqoG8dwKLeNKdA2JvLI_rxp2_V89qC3HzRjw2mJyixZDkDtBoitJ7iuTDoR5oF0-COGGzrIp_v-U-XLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=GsPxYm8HxzQdmkjoykc1wEeC-TsqwZu8dRMQyegHh5mVKVKcGEUBWxWRfZ9N4JCjHfY38efZPYfkhCg6P6_PaaK4re84Mc-hs_FGZrdklaLLAA56ZdKuerZgQ9feWG2ydcwO1Qi_0P5lKvp0WxfyBxNkhrJ-Z8zEZy289aRL2NoFhnaKQ4yT46lqJGvtSDiGg10VOU94zvjEp4l8nrgKzgsVZtn21ccd6w43F72FiwiNagVOrtAgP5BOYVF4MpH6MEuGM_iqoG8dwKLeNKdA2JvLI_rxp2_V89qC3HzRjw2mJyixZDkDtBoitJ7iuTDoR5oF0-COGGzrIp_v-U-XLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X48w7su6QwcX9AiaMT3TEd6fKMgt24YSda1mHsfEC2x0LMQUavfIKidJ0WZYHb7pWGWE2hUoVIvEiAhMcI8aouzYrRqBBVZ0vcDrVEzf2Zd6RRuxHkuoJzIMZnGyhsjfIcJN9He_2A2M6zXCyk6YeJaLAH1fR4XjQXanW6cZKs-nyN9TBA-gBlZSj2v7nUqpWU_J1M8AEfXaPkS2K0HEppbS-GiT4R_NRTt44n8J4SbbhwXVZNM2PVcMj9BurB551lsd-bGT3IlWrhycnZLFqNks6FkaUY75V_o73BFMbDAAzyEMfwHtmPfXTIz3YP4PTGK1Ca_fA4jsMWsxkNezKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=f3aJ0FDluvd0OHFd6Am7wD9vPEEQKELa_z9lidpD6MYFiJQtxDzvybCFuhjL9et7eACGQmZwVrGxKo6DNTatGtqjqEp-R3EEUHm7OvsPyMeXObodV_Ic5ldm-rIS4VgsWzdKaSOU5YZQqdtN8Xba3GF9_uOlp6RLeZb_AoxmUaghnFuwm6eCCcgs_kXQBcEqf6lzgQDz-qVG8V5kwKT7w6ONUUhzmhUGIDmuYW4cOtLe6G9biCEWT-NDFygtJBY26rHaRUZ8paBS0vRx1eMTIA6eg0DEKS8iTFLrtGB0wBPVXDUdM2gy-sHWEQ_Uudyk9vjMdwif4_N_PsqJfJVgFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=f3aJ0FDluvd0OHFd6Am7wD9vPEEQKELa_z9lidpD6MYFiJQtxDzvybCFuhjL9et7eACGQmZwVrGxKo6DNTatGtqjqEp-R3EEUHm7OvsPyMeXObodV_Ic5ldm-rIS4VgsWzdKaSOU5YZQqdtN8Xba3GF9_uOlp6RLeZb_AoxmUaghnFuwm6eCCcgs_kXQBcEqf6lzgQDz-qVG8V5kwKT7w6ONUUhzmhUGIDmuYW4cOtLe6G9biCEWT-NDFygtJBY26rHaRUZ8paBS0vRx1eMTIA6eg0DEKS8iTFLrtGB0wBPVXDUdM2gy-sHWEQ_Uudyk9vjMdwif4_N_PsqJfJVgFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=CizHt-ZvlwWmPgGBslSbVR2iSyCxBCrWDtMbhPK4DWAqKyCHFoGhtz9E-VfMz4U93T55LshyZDLq_npW6E9X8WNGzcqK9nvlAdUPp1glsvLdv4laupaFxAcGvPbYV486BpyZBIji55oLW9sF_hoMHL8OnND3535WIVoTvXk9eSgjv28HzuXl6O94amSWLAdrnxdpXJAMF1i4icKtHNY4xe4RyOFT241yQCghkHeeIKhkVO0b32_gZyFHrdQeOUqw74NfyMNbexmhBx7eGgesy0SClYueWEVo2PBskc3TVtL0wtSkCsutFhC1ooOjHPLvOzOhAErnCu4uj9xvF8V3qS3KSmYD_2W77zY47Zqi9e5B3faq0DfSaKDAymmbbbLnB3Dh_vgJLrGidIyD0vUVF6EGOjoPuiRuAC14Bj_Y_2wsBgip80ATTKJVw5vRPoXrZBoJ0X4PcyGdPZlZr-SwnPhltHrgu2retu--xu7eZ9ELG3Clxg43GywwkzGJv-2upOTxvXg01tTg1WZy3D0ElP380XxLE_07_kYZtjBxxrfe6pJX0832Lh1JJkFky4at-5W-uqOzE8o1vEzjQsfMKf9nyi3nVzmuHxZaPdX17Y296A3JdOGvyF6VeNcEuP1p8apzPC8X7Cr-DqlzIHxM2ufv6OF52SIuXtGn5cM-LvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=CizHt-ZvlwWmPgGBslSbVR2iSyCxBCrWDtMbhPK4DWAqKyCHFoGhtz9E-VfMz4U93T55LshyZDLq_npW6E9X8WNGzcqK9nvlAdUPp1glsvLdv4laupaFxAcGvPbYV486BpyZBIji55oLW9sF_hoMHL8OnND3535WIVoTvXk9eSgjv28HzuXl6O94amSWLAdrnxdpXJAMF1i4icKtHNY4xe4RyOFT241yQCghkHeeIKhkVO0b32_gZyFHrdQeOUqw74NfyMNbexmhBx7eGgesy0SClYueWEVo2PBskc3TVtL0wtSkCsutFhC1ooOjHPLvOzOhAErnCu4uj9xvF8V3qS3KSmYD_2W77zY47Zqi9e5B3faq0DfSaKDAymmbbbLnB3Dh_vgJLrGidIyD0vUVF6EGOjoPuiRuAC14Bj_Y_2wsBgip80ATTKJVw5vRPoXrZBoJ0X4PcyGdPZlZr-SwnPhltHrgu2retu--xu7eZ9ELG3Clxg43GywwkzGJv-2upOTxvXg01tTg1WZy3D0ElP380XxLE_07_kYZtjBxxrfe6pJX0832Lh1JJkFky4at-5W-uqOzE8o1vEzjQsfMKf9nyi3nVzmuHxZaPdX17Y296A3JdOGvyF6VeNcEuP1p8apzPC8X7Cr-DqlzIHxM2ufv6OF52SIuXtGn5cM-LvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOtz8SRbDfwQng34YZGrIUrS0utmIBGOzUaOiLqhZ-B9C3o9mCXg_4gO4WtH-6zzlWU4qlnl2kbhFElN6hnsI8QxDsWHuapKpHt0lNDBYONRNV5HRW6-UNeY4zmVjikafrCwMuWoQTQd7i1FCllQBu-E-SYa496MVXDoqlU3JQKKsQPEtFDEhQxCzjRyCmLtZFK4NZQU7BA0l4wziHwDzgo5zwq87tCGGh6bslc_Len-uuXHwp3Pee8NHdhKlneZ7_lwuSy-hJyqgbvrcr79nERetuZYEhIz2UtwU78WLv57nhYJwdSbDRRsSbz_JTPHEhPkNblRuyVfTYvddeY1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=B9lZkeJm1iQW364S9z_68XcJp6ii-nrSjWTgiB_YYKWEsQcPoDMYcV4n-JTpSlKiI4LpFeKLuNpiStxx2pyCGBo-IhGKtfYA5U-QzI4dOCg6-UUOtX317jDk22KcwRMLGPQ7mCRY-3MvW6yFdI7OWg__RcJBxLmGT5Z65I0EvaUxYwOg8tW8ROnBU-nWb_FJorcOmIaL6-P_7WrRPWE_lN4zkRtspI_SNsZ9LJh5TZ8Bh_rnyGaAmiyff2baX2rrjdpKxP154RFmZd_o0pGAYHC8LZ_6rGTKNqqG0GngMesQ3JEl_-dFZJ5awtt9yEwozbEGpM0shxFpaSQDHdKfv0KqwUKqCKKzt3HdVActzCRDqM-aVf4xkFoXUr644JbczCG8PydtqJEMvD_-K3LZadrKxoJS4B_s5y1JUKtmqD6zjnmtmDAwHYQxh4k7pukjrtkCv2EioM-swv1nPgcnXQCB46hjRqy9jflezhKRx_SH6jf2acB9Ky78bNM76Yl3wYUsekLTP2NbJhwHcx1IQ7I_AgpmRxTXJuho2kgFalfAbQNA_95w_TomzZly_jOtYpYJTqYfe32V1oMsXmBmDckPWsHxbJRTPU30xQ9B_HEgLnlSeJjRBii0Oalw-yYDzvyPEHNIKGP2N6zA8OFBrpmbtd0xGmYmIH0B8j6N49U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=B9lZkeJm1iQW364S9z_68XcJp6ii-nrSjWTgiB_YYKWEsQcPoDMYcV4n-JTpSlKiI4LpFeKLuNpiStxx2pyCGBo-IhGKtfYA5U-QzI4dOCg6-UUOtX317jDk22KcwRMLGPQ7mCRY-3MvW6yFdI7OWg__RcJBxLmGT5Z65I0EvaUxYwOg8tW8ROnBU-nWb_FJorcOmIaL6-P_7WrRPWE_lN4zkRtspI_SNsZ9LJh5TZ8Bh_rnyGaAmiyff2baX2rrjdpKxP154RFmZd_o0pGAYHC8LZ_6rGTKNqqG0GngMesQ3JEl_-dFZJ5awtt9yEwozbEGpM0shxFpaSQDHdKfv0KqwUKqCKKzt3HdVActzCRDqM-aVf4xkFoXUr644JbczCG8PydtqJEMvD_-K3LZadrKxoJS4B_s5y1JUKtmqD6zjnmtmDAwHYQxh4k7pukjrtkCv2EioM-swv1nPgcnXQCB46hjRqy9jflezhKRx_SH6jf2acB9Ky78bNM76Yl3wYUsekLTP2NbJhwHcx1IQ7I_AgpmRxTXJuho2kgFalfAbQNA_95w_TomzZly_jOtYpYJTqYfe32V1oMsXmBmDckPWsHxbJRTPU30xQ9B_HEgLnlSeJjRBii0Oalw-yYDzvyPEHNIKGP2N6zA8OFBrpmbtd0xGmYmIH0B8j6N49U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pt2y7xsRNp_0dX7MzoWvG6XWUVzK6xYfAlqbaVPyrbBAwrvn2Zx1vy00U0rXCv-3K5IMWskA997Z71AD-U0dmQAvfHriqYuAetnVqQ-fTaYErawJ5fgb82JD1Qmb1V2slUoLFZ_X1G0YN0VJD03tG0YNP1eB85iuvoPjPKyMjsB9OSrsGFbsW8zLSnCteaNlB8RASIk1UMkAnHjgd2PGtFdnhNJCbvX35If-58QQGS2bTYuUMc398owdGrgx78YeCQWuGfLQ59Q7h4-XMfXIxo9QxcbPCWJpJKCF1ap0Otwvnxtf9hq66XpxJ0tcPYCAXotasx0WhXD1K3RHjRMYTkER6sIRque5qcA91jLYLd9SAtemDrF1VOP7WKDUjZE6XC7bpA1aBJdqnV-EjkgUi3sIJNar6y-37WrF4nY2xsFRx9DQxLQxzhOESsjlyqB9uaDAARGEYwnU8sqZmm4LEHqke7u3bQxdaWWOtz5q7KdxdEJP6jR8yZp7MLPNtf8Fd3g-RXFi0sr-wD_evbWOUc3zqgeLwyYY11Vevaxitn79snHgHYXtFDi5fomKzEeiwXKJR8wy7EjTtNqLkr4JboXEqT-PHCDKzjIxF6Y9ymDzY4BFfT3ooU4JTbBrV24w4WTyq18jlKLsTEcuXXttu3HlgOavBwAnw7OwV0XHyjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pt2y7xsRNp_0dX7MzoWvG6XWUVzK6xYfAlqbaVPyrbBAwrvn2Zx1vy00U0rXCv-3K5IMWskA997Z71AD-U0dmQAvfHriqYuAetnVqQ-fTaYErawJ5fgb82JD1Qmb1V2slUoLFZ_X1G0YN0VJD03tG0YNP1eB85iuvoPjPKyMjsB9OSrsGFbsW8zLSnCteaNlB8RASIk1UMkAnHjgd2PGtFdnhNJCbvX35If-58QQGS2bTYuUMc398owdGrgx78YeCQWuGfLQ59Q7h4-XMfXIxo9QxcbPCWJpJKCF1ap0Otwvnxtf9hq66XpxJ0tcPYCAXotasx0WhXD1K3RHjRMYTkER6sIRque5qcA91jLYLd9SAtemDrF1VOP7WKDUjZE6XC7bpA1aBJdqnV-EjkgUi3sIJNar6y-37WrF4nY2xsFRx9DQxLQxzhOESsjlyqB9uaDAARGEYwnU8sqZmm4LEHqke7u3bQxdaWWOtz5q7KdxdEJP6jR8yZp7MLPNtf8Fd3g-RXFi0sr-wD_evbWOUc3zqgeLwyYY11Vevaxitn79snHgHYXtFDi5fomKzEeiwXKJR8wy7EjTtNqLkr4JboXEqT-PHCDKzjIxF6Y9ymDzY4BFfT3ooU4JTbBrV24w4WTyq18jlKLsTEcuXXttu3HlgOavBwAnw7OwV0XHyjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=rG0q1o3YQaamphGwZ63bGIngqBoyh_yNtlshpEayEV2Y_HaCTUzq-ZumDHFxAC3GUqjDBe8qx2U0pbTRXOsHRllvuUZwkCP-e0lr5S5z0ZQNtJkzzPOw-EE5aNpIaouQ85z27H-CsyvyS4mGxO-mbhaCJL7yOAiIjxTm8K3bkhuHBhhEFYYkKfiKKaSpFl26vNDHYSUXkbrb8LO5LEiYY6h1TiY3BHX4Tsn2eCxOy2FEu-9gWcOllRQPWqzJ7P_yjUemK-ReHOVLmx1zoGNAf81iHaMiY6CtQXRLHOaujweaeTBvFVHN3nmSFBcd2ADez-_27MNsBNcluXD_fE8g3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=rG0q1o3YQaamphGwZ63bGIngqBoyh_yNtlshpEayEV2Y_HaCTUzq-ZumDHFxAC3GUqjDBe8qx2U0pbTRXOsHRllvuUZwkCP-e0lr5S5z0ZQNtJkzzPOw-EE5aNpIaouQ85z27H-CsyvyS4mGxO-mbhaCJL7yOAiIjxTm8K3bkhuHBhhEFYYkKfiKKaSpFl26vNDHYSUXkbrb8LO5LEiYY6h1TiY3BHX4Tsn2eCxOy2FEu-9gWcOllRQPWqzJ7P_yjUemK-ReHOVLmx1zoGNAf81iHaMiY6CtQXRLHOaujweaeTBvFVHN3nmSFBcd2ADez-_27MNsBNcluXD_fE8g3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=usg6Dj0bz3kRXTAnov0h4zNffW_CvOSw59ETETXbBZuGjXtz2LOzXjMM9LNgBS6OFSYyAqTzXZ1nNlzOWObBxp-pWVgpmR5ppKtqZ8EOEkrP9kAdgEMTA4otYXTCHA9BmWABrKevRaJv6ZyRDTESq_uERFI0ssvBCmJmjkhUKEjulKi9rN4mRym_4HdQMWq9_yz1QCfZYxKRL3PZRj9uaqB_1lEV-S0QYlciFGbiGIuPszJH12mhHp0yr5fOv4kSBvB69yjAwwDE4dv6pyWK67Q6T-iVkQpaQUquQ1Xwf5zHrBGDuiMUbubRmbJFdGeKntQ_sb95w_umexgUa6CExw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=usg6Dj0bz3kRXTAnov0h4zNffW_CvOSw59ETETXbBZuGjXtz2LOzXjMM9LNgBS6OFSYyAqTzXZ1nNlzOWObBxp-pWVgpmR5ppKtqZ8EOEkrP9kAdgEMTA4otYXTCHA9BmWABrKevRaJv6ZyRDTESq_uERFI0ssvBCmJmjkhUKEjulKi9rN4mRym_4HdQMWq9_yz1QCfZYxKRL3PZRj9uaqB_1lEV-S0QYlciFGbiGIuPszJH12mhHp0yr5fOv4kSBvB69yjAwwDE4dv6pyWK67Q6T-iVkQpaQUquQ1Xwf5zHrBGDuiMUbubRmbJFdGeKntQ_sb95w_umexgUa6CExw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=YFCEucXnFCL05qSPdRV0zHabrGJynTyQl6imM5o4y_29tSRCG5cJzO19rDNmYQpYVuGu6U008UJPiOjA4o93Ehrw8YUjD6XrxVnN0-QZx48ZyyQu0o9KzvEdr0RdjvluthIbLAIPg9f2Ta5oWUwbvpkngDUyTCORzTQqeU6e_pQNxftzxon1xoFHwCDpHJq1B8iy5NSga9TRzbuiodM9oBFHVUETFC5mW2--Zrf4WYVGbXAKRobotqa_bhPg3cj6lFnlbkCdbUKxaaSSShqPOgqEHIWKvpYVsHx6B6YTXTnVhJmSY2-Gc23i1gETLX8HvDTv6ZGvn9f0Zn7_kB03Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=YFCEucXnFCL05qSPdRV0zHabrGJynTyQl6imM5o4y_29tSRCG5cJzO19rDNmYQpYVuGu6U008UJPiOjA4o93Ehrw8YUjD6XrxVnN0-QZx48ZyyQu0o9KzvEdr0RdjvluthIbLAIPg9f2Ta5oWUwbvpkngDUyTCORzTQqeU6e_pQNxftzxon1xoFHwCDpHJq1B8iy5NSga9TRzbuiodM9oBFHVUETFC5mW2--Zrf4WYVGbXAKRobotqa_bhPg3cj6lFnlbkCdbUKxaaSSShqPOgqEHIWKvpYVsHx6B6YTXTnVhJmSY2-Gc23i1gETLX8HvDTv6ZGvn9f0Zn7_kB03Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=YI8ZQmOQKnXKE3d4USZ36iEO7d7N4egiB8o2K6EEH6aLpx4XbubOq3Njtev77GUSeoM_LWrhJoGFgtzdMllUZpp6mOhNjtfkr4y-TXJrRdms_AoF9MNdvS6r2NDWac1qQce0W4W-WKnJj0pgn5mR3pC1dtWwUEGKCeMgiT7FgI-pAQM_B57AQqZdObLnNMD-e1yPsDk32vY7Q5bMUeQLST5nINhk9Z0_0AqbJDw7PGmeDKvpqsvMOjb-9k2IGdcbquDV1m-rI70i3SyKtL4lYo4h8IwyRmmndMChjmSEcAxUoyDbsBWhI6AwSsNfm6Ptb96sdcV9iUA-6u0nM3vbmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=YI8ZQmOQKnXKE3d4USZ36iEO7d7N4egiB8o2K6EEH6aLpx4XbubOq3Njtev77GUSeoM_LWrhJoGFgtzdMllUZpp6mOhNjtfkr4y-TXJrRdms_AoF9MNdvS6r2NDWac1qQce0W4W-WKnJj0pgn5mR3pC1dtWwUEGKCeMgiT7FgI-pAQM_B57AQqZdObLnNMD-e1yPsDk32vY7Q5bMUeQLST5nINhk9Z0_0AqbJDw7PGmeDKvpqsvMOjb-9k2IGdcbquDV1m-rI70i3SyKtL4lYo4h8IwyRmmndMChjmSEcAxUoyDbsBWhI6AwSsNfm6Ptb96sdcV9iUA-6u0nM3vbmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=eE5cierdR4MePonz0mBqDoZjsOxzxnKZKE_bkW8EvlkQIRMBPvz2lBbraCA2VFNv4pFIdFah0kNV0BAB00Zb7uET9bmjxsa5ruNABF5h9oGcvJ7V4MfweHMqKIPdASKPwxMTNtVgXkqioZ3i0TFeR90A7DMV23Gjzk2t6blLBPacLHKHDujcmkDUnlNqxQOi0GToLUuUfQvIp_BgKXoAGaHdZdpAN4IAlKXlouEplFHVnvNt8cFfa-00J6j86yk_xrGcr1ctKq4R8K1aCI9Y95jjCCqhk8p37espmVKVcseQQOgr3aZQl5ZnBIbspsAmrPMxejaOoo2w2mbohWmGng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=eE5cierdR4MePonz0mBqDoZjsOxzxnKZKE_bkW8EvlkQIRMBPvz2lBbraCA2VFNv4pFIdFah0kNV0BAB00Zb7uET9bmjxsa5ruNABF5h9oGcvJ7V4MfweHMqKIPdASKPwxMTNtVgXkqioZ3i0TFeR90A7DMV23Gjzk2t6blLBPacLHKHDujcmkDUnlNqxQOi0GToLUuUfQvIp_BgKXoAGaHdZdpAN4IAlKXlouEplFHVnvNt8cFfa-00J6j86yk_xrGcr1ctKq4R8K1aCI9Y95jjCCqhk8p37espmVKVcseQQOgr3aZQl5ZnBIbspsAmrPMxejaOoo2w2mbohWmGng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=a8gpIsJ9ikflNGzfyhxgJlmPz5lBAN8X0pgnHMJQRfeKhotw8_vuXxl607WGWIkPs7nFfE4TXfeRXSCeQREtV2wsiOuJk5x4p0P2WGPYucsejK3-_N7BacRXnPQEP_Fk0CmrgfpLoCyU8VQD2qiOV7mmYn9X5ZmMfOZnEQeJH6SYVvauxC_y3GHcsDRNBgvDyf1HtgjQvFMtojCAufxdwKXlZ831yIpyQV_shwtxA32gdie6ybSPL5ou5dofpSOjLRFhtusux7-piteVNPPHR3W0RfxyJurM6N6G7-t8FyLFxrhmANuTl_r6aW5gTawOSqc53n-wn9VWWfFYc5a_eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=a8gpIsJ9ikflNGzfyhxgJlmPz5lBAN8X0pgnHMJQRfeKhotw8_vuXxl607WGWIkPs7nFfE4TXfeRXSCeQREtV2wsiOuJk5x4p0P2WGPYucsejK3-_N7BacRXnPQEP_Fk0CmrgfpLoCyU8VQD2qiOV7mmYn9X5ZmMfOZnEQeJH6SYVvauxC_y3GHcsDRNBgvDyf1HtgjQvFMtojCAufxdwKXlZ831yIpyQV_shwtxA32gdie6ybSPL5ou5dofpSOjLRFhtusux7-piteVNPPHR3W0RfxyJurM6N6G7-t8FyLFxrhmANuTl_r6aW5gTawOSqc53n-wn9VWWfFYc5a_eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=gLvPuIJxDuc1tzZiYLXYJfanSsaIL-xY0h9Xs3k8x7wK_zBROUFvgbrJjeV7r-JNKJTcLuRfn2JlyQlyhLeUcHRSYFuC8sENk5J0iF4JtIaXTKNJA03eoiygeVVmdUNf46BsnB_d0CAUv3gH7VOPoKlIXHF776G_6SjwJAaL0Agd0eu6zHaAv40tzWemsJr_pCd5sAxGFzCFVLnfwiMW71O_2mE5gUVSPji32BbZfbrkeFa3ghK-eknytTqzBoG-sqAAeRWc7Ttha7erbWQokTJQ0rjYnBhBZvmdQTrhZ7xxADX4CEqu4MlUup0_xyV-4OTfBIJtaJNPVJa2E9TKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=gLvPuIJxDuc1tzZiYLXYJfanSsaIL-xY0h9Xs3k8x7wK_zBROUFvgbrJjeV7r-JNKJTcLuRfn2JlyQlyhLeUcHRSYFuC8sENk5J0iF4JtIaXTKNJA03eoiygeVVmdUNf46BsnB_d0CAUv3gH7VOPoKlIXHF776G_6SjwJAaL0Agd0eu6zHaAv40tzWemsJr_pCd5sAxGFzCFVLnfwiMW71O_2mE5gUVSPji32BbZfbrkeFa3ghK-eknytTqzBoG-sqAAeRWc7Ttha7erbWQokTJQ0rjYnBhBZvmdQTrhZ7xxADX4CEqu4MlUup0_xyV-4OTfBIJtaJNPVJa2E9TKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqjbAHnud2AW8RrquQdwA7TczVkOanRoaLyKaN__mtfI4vmUCwOwDaMuy9GZ8MsJ5Zx-NdokxyFF-ewlgEMqx02lcZWIIsk3FMyw7MIXUO2DVJewyh-3QzygqnpkfC5GyMuTL9e9qAlAwXiH63gpyXO9_yOhhQSBZ7tXEKstBP5cE-0dCMzpQV-YFnrQSf7ZGBGM7pxYIDnBCs1i4lXLSfGBFJg9WsjZjnIIUCtjFdAjJ_XLn0PGBUkaFGEFN6JqRdc-LM0yxfDVXBwipF97wDgGdvl2q-n1c0_1bXEWxzEtyZA--sbNmBeoyw5dljwthNhDJXyCXh5BnCI8yAUQkQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=DyBg6DiF3pDOnxFp3COsDt0Bgi7OKgevbC1MceeUquEM9XQqzL5g4ddo26NP8jhGS1kVY_uizlpdAGi0mVCsL1xUPEJVOE2uvCr5chzQAFNSV1IaZzj9w-pvoIv0U3yNJIl0W2_p1frd_JhsCCZFagew9xOX33evYHw81_yGh_ObmpBj08Tj4pU1edb4CW8f7uQe9EixArk-rUzoWzKRE3W01RDtdrQV-y5r_IsBIX5hl5KuTOUgzoiazqsqVJGxQ_7jQpjzUFeRpv1S6DnMg0iawa0fmV4a8dpvnjlZx0zLBZY4c8B6zh-WxxRtjYvvnjptcL-ttk93HGBFefS2iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=DyBg6DiF3pDOnxFp3COsDt0Bgi7OKgevbC1MceeUquEM9XQqzL5g4ddo26NP8jhGS1kVY_uizlpdAGi0mVCsL1xUPEJVOE2uvCr5chzQAFNSV1IaZzj9w-pvoIv0U3yNJIl0W2_p1frd_JhsCCZFagew9xOX33evYHw81_yGh_ObmpBj08Tj4pU1edb4CW8f7uQe9EixArk-rUzoWzKRE3W01RDtdrQV-y5r_IsBIX5hl5KuTOUgzoiazqsqVJGxQ_7jQpjzUFeRpv1S6DnMg0iawa0fmV4a8dpvnjlZx0zLBZY4c8B6zh-WxxRtjYvvnjptcL-ttk93HGBFefS2iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=oYPYGCNNsp9IUFCcyZn4nWNAltRvjoYWhNh_g6vweyYFDJ-2zwuqbBKRW9qsdWgqGW8g1y-9ww9iJ7DpPhpWAObnzoKn3mJv5urliuUpd76vBvikYxTonZw8hrfsTwlpFqJjVewuaG7K9pjbB0TWkVdzf-YqY1gvDKY9_tGOgZgt3SqNBi-dqNt8yhueG1ienGqt6_ZZzrwisejIoCKkN2bT_tXe1Hamwi3JQmlkONx7QIxlgrTMzi0Sb7NDyVltNLTsLyTKRT4BzytgqkyQL4mAyp6JKx93FIZC8YqWTZpFPKQKJYxIBl5VOIImgrrw6ZZovMy8BN46qpsvsCZk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=oYPYGCNNsp9IUFCcyZn4nWNAltRvjoYWhNh_g6vweyYFDJ-2zwuqbBKRW9qsdWgqGW8g1y-9ww9iJ7DpPhpWAObnzoKn3mJv5urliuUpd76vBvikYxTonZw8hrfsTwlpFqJjVewuaG7K9pjbB0TWkVdzf-YqY1gvDKY9_tGOgZgt3SqNBi-dqNt8yhueG1ienGqt6_ZZzrwisejIoCKkN2bT_tXe1Hamwi3JQmlkONx7QIxlgrTMzi0Sb7NDyVltNLTsLyTKRT4BzytgqkyQL4mAyp6JKx93FIZC8YqWTZpFPKQKJYxIBl5VOIImgrrw6ZZovMy8BN46qpsvsCZk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=EORl9zV-PZ0UkRdhHfWrWbJG4ezVkK1fT1CztzWCL8lVFkaxOhPuibMM-XcT2ci6gF0NFDF1mBNTv7PY6Wp_ytz0RvKCE4_b7k6a13k63oJ0AmfBhjgES9PZxRVXekTbAlhluTuN61uwRk6QHEjKj9LYpIIlHAwdHfEa1vzdHr9yU02o1amaVNlK_C-xpOQO9xR9q-H9P_tXG72JVSc_Tcdsy3_0DGxABZuHTDQR_WvpKltyz6STM280TiiKzPgSsbcAXS43kznwYXrJHtraXdnP0uNyEzq8_R_SyGl48GfcE7CPx9cKLVVlXuEQp0rOj703TBYzjMDFVH9yJLt7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=EORl9zV-PZ0UkRdhHfWrWbJG4ezVkK1fT1CztzWCL8lVFkaxOhPuibMM-XcT2ci6gF0NFDF1mBNTv7PY6Wp_ytz0RvKCE4_b7k6a13k63oJ0AmfBhjgES9PZxRVXekTbAlhluTuN61uwRk6QHEjKj9LYpIIlHAwdHfEa1vzdHr9yU02o1amaVNlK_C-xpOQO9xR9q-H9P_tXG72JVSc_Tcdsy3_0DGxABZuHTDQR_WvpKltyz6STM280TiiKzPgSsbcAXS43kznwYXrJHtraXdnP0uNyEzq8_R_SyGl48GfcE7CPx9cKLVVlXuEQp0rOj703TBYzjMDFVH9yJLt7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=alqBDick1XoOHx_TnJNYKoVeaPexE8Eh34tj3czxhAzTNmgrB2hhiKGz_ObE8syaWr4h6j_v3QInivA3BirPp8Xy2SQRkte3L4L0ZcnSkyF3hyF1iiKEDSZu2GXRBU-kE9-MWR--bMJ9mBz_SUMOfWgZwojenHJRmtgXhZH1TIDX91sj76ZxHSrZVYSx2vT9wnal0i1Td2kWLLBSLpIukIisECxyHWIhwnZbOELFEX0ZTxw_7Lk-4IyG1u4TnxoIZdrwgnCL_t3N80NKvZEBB8S2hJXfYSz0YsBxhYdQJ8sojAbZU5uLKims6HGgOP_PoFFOr_dj63Cyv_f6DmruNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=alqBDick1XoOHx_TnJNYKoVeaPexE8Eh34tj3czxhAzTNmgrB2hhiKGz_ObE8syaWr4h6j_v3QInivA3BirPp8Xy2SQRkte3L4L0ZcnSkyF3hyF1iiKEDSZu2GXRBU-kE9-MWR--bMJ9mBz_SUMOfWgZwojenHJRmtgXhZH1TIDX91sj76ZxHSrZVYSx2vT9wnal0i1Td2kWLLBSLpIukIisECxyHWIhwnZbOELFEX0ZTxw_7Lk-4IyG1u4TnxoIZdrwgnCL_t3N80NKvZEBB8S2hJXfYSz0YsBxhYdQJ8sojAbZU5uLKims6HGgOP_PoFFOr_dj63Cyv_f6DmruNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJk21-kVsl9oG6-hwb4J7cAPWvSvhiPHV4DkrF4iID2xyhjpIg3Q3MU1RPi_Ikzq6-s9-hypXRBm7VnUW9zFXYa-TxSVxQAH0u3eNYm4irL1P6ehhQR1im6FW38ZkUNekJtR51q04ziP3bKQxgetSyvHdpU69b03-OrO6pnzbJy7sQ7p3rCBegzkDo7w0RwvTI2LMxU-Eqjm2ROf6ZvAc4VP9rWSNEPXiQPjB5wkI-sYGQKdLyKFtiO4zX9kLFw74UJR9w4dx3hAnR77Bm5vKpLvdQEKcFOBxwcdGf9znxC6sTr-UoFzBhFbojhys8xn1AV3Wjt1Yo095csJ1xEOkQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=gufR-4y0X78jBQR3aKaZPTlNYOQJY6EHeHVqRwrx-oyu0vra6mCsUFT8Gl_Y8oQVCKxFYu2xreQyu_4TMI5d2Qge4BAVqHTtXPsYvyir5yq7ACywXwbbc2m79fAIwLyX7FKHoHWqai_j0yMCwRTTyd5SqEGGZN_MpEYd2qRQhLtNqBYWrSvTj-8AjWfsOIn7yJUWYJt2R2X5Dq1HxvjLrzOLfbjVpYWoLXtjCFhB4W1YYzq78xXij-v-TxwQlRvynBkhPbJkG2EUhQl3vs63hRxqZH_9ER3f1gNzqiRz4NtQD9hFvfu2mW4dOJTj7AvbfL0IHnPOb_izGUYjKOmk9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=gufR-4y0X78jBQR3aKaZPTlNYOQJY6EHeHVqRwrx-oyu0vra6mCsUFT8Gl_Y8oQVCKxFYu2xreQyu_4TMI5d2Qge4BAVqHTtXPsYvyir5yq7ACywXwbbc2m79fAIwLyX7FKHoHWqai_j0yMCwRTTyd5SqEGGZN_MpEYd2qRQhLtNqBYWrSvTj-8AjWfsOIn7yJUWYJt2R2X5Dq1HxvjLrzOLfbjVpYWoLXtjCFhB4W1YYzq78xXij-v-TxwQlRvynBkhPbJkG2EUhQl3vs63hRxqZH_9ER3f1gNzqiRz4NtQD9hFvfu2mW4dOJTj7AvbfL0IHnPOb_izGUYjKOmk9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Es-2UjsHUharIxHifYBAeACArlq86oVg48e5Wy72Y5IBVUa76CJk7_uI-taUJNJ9KuMGuZKDlgNIHAB-zCUmXGngsujcw1gCGrN_5jY5oTBEGopP2WlKkU0Ixd5yh9nJAHmQp50oASBdf9kQ6OgMmfRWNd5_HZBbTyPulI85AQaoR85LTCVH5OCwMbJvFdoYtdSO7l2msl0LmODu6DwoKYpF5uMirLIsbUMeTYg5KpEhAvWFZN4ZnF5RHW4CKQWwV32V2XnSYKjtbsLQHY5jEV1mLCEgEx4kz0D5fqyRCoz8GcEYbi_P42GdOSwi9rL_GVbPT1BauCETpWiK31jdaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Es-2UjsHUharIxHifYBAeACArlq86oVg48e5Wy72Y5IBVUa76CJk7_uI-taUJNJ9KuMGuZKDlgNIHAB-zCUmXGngsujcw1gCGrN_5jY5oTBEGopP2WlKkU0Ixd5yh9nJAHmQp50oASBdf9kQ6OgMmfRWNd5_HZBbTyPulI85AQaoR85LTCVH5OCwMbJvFdoYtdSO7l2msl0LmODu6DwoKYpF5uMirLIsbUMeTYg5KpEhAvWFZN4ZnF5RHW4CKQWwV32V2XnSYKjtbsLQHY5jEV1mLCEgEx4kz0D5fqyRCoz8GcEYbi_P42GdOSwi9rL_GVbPT1BauCETpWiK31jdaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-gnXQQw3paQjvSXQpxA1bJ9yXArYmjObDMRJ6aEmU2jNYuQnFBYq3RrqfEPbph8FQFzIy_0b77gY6KcyWNLqEzf2-mIXpZ8skFYVkoGlYiIdIAHsHCz5ZYJQx1-6T_U98BvPNwtZnNxaO8hNemBnavUz_Qs0aL2gMdQZzXwT-F8eKha56GNA4fDO_qaeRJBDgJUk_RBNTM2ioH_H7w0zvkblpLkI42hnRrOEwEq7rMVR7NRIlL3A0JpKR9YF6GXsE9lzZsmbahaVx2aJSVHwnLU_t9mcEGzMdAXm-rnkfEr614K3p99-gtykt4E8h9wfA40liikAQENKKyNl824GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cuvj8KL3n_wnuOlX2Ogv3lDc2kwivXA-Hg5T1_xrLmWuhU547Sau4vqDPKjbYPJXoDyc49glCWfcwQZEQbMkwUuRrolGNFZWAfg4IRcXlA62JARsRYR3npMMMquwiZminR5HxNNhZoyt2ur0Izb9r7nAspfj5PES6EWOtoZcupnulowvcwv_Ky77zSBv4yIPxbKkS991KcjKXlJJ5xQZ9uPvXLpA2pfKnMXAab6AN7vg65_cBdEAiNe6b6ruEEMZOZKMs3R8U71XIxmBoFGszoGQw5Pk-Eutg7B6qdqzEVTM2y5uxW_H6EQxsjZGpGZrFJaukNFqDPEeqKUQslib9A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=J1qlI1kzdd75qPnmD_9pOotONGM74WkqZdUO18_I4b3XXobMlU_4fuARjJnD724gWWqx84o1LRsKxYZkyqRfgCV5KiH3l4sfF2mvwpFxJw0-Ls__NI2tE_2IVUmtG5kQb2vf_VfuOFs-t877EFgiA5MFG9cypabTtDneG3yivyoOaVHIp_zoI9VbvmsViTABzQwPAx82XjqWHVlGjVJPAUY0oXKRUsDQHPWCn8qfOs_Z3NFSrSTE6FIW53zCyXIn4t0cg-TRV3ph61PSUzN8CmXmbDpMDRiw1m3VowpRhTWrr2IV4uuvPHqkXlcz1EjspQYXXdjnDWM_xvKyCP7CXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=J1qlI1kzdd75qPnmD_9pOotONGM74WkqZdUO18_I4b3XXobMlU_4fuARjJnD724gWWqx84o1LRsKxYZkyqRfgCV5KiH3l4sfF2mvwpFxJw0-Ls__NI2tE_2IVUmtG5kQb2vf_VfuOFs-t877EFgiA5MFG9cypabTtDneG3yivyoOaVHIp_zoI9VbvmsViTABzQwPAx82XjqWHVlGjVJPAUY0oXKRUsDQHPWCn8qfOs_Z3NFSrSTE6FIW53zCyXIn4t0cg-TRV3ph61PSUzN8CmXmbDpMDRiw1m3VowpRhTWrr2IV4uuvPHqkXlcz1EjspQYXXdjnDWM_xvKyCP7CXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3_JVXKQTeCKIdupdytCbOo79U3eT87XuErjCo8jwKoqHB-0Bb1S8M8ITIfG1Ury_7Map5i0CUGMclhZtW7bbzkliqiQ0mkMi4xo61Q7zzUjkS-pv_h4i6Vc3oAUS-7uXsepnzKmFYLAvDMoOB0SF1_wYJ849dJU7mlfEGoVwqT5n5gc2f_iEeCYi6R1WuIxcIuc2AUTy8XoPNnqldufvqSokZXdpdsqyXgnKOQ6z5nrhUlGkQlNseKgDkaKUEc0oilmZ7nWltyyx6tS-j0ZJ4gsGLaLWOh44NMSFrYiY3sztBRof9_ar_Rlv3xqIKth17erTManGPv_rFFtZGUPYg.jpg" alt="photo" loading="lazy"/></div>
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
