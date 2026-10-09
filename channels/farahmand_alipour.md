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
<img src="https://cdn4.telesco.pe/file/lcAJsVvK0ve1DjFRXkHjd9_8632bfWUPzUoVH4ttCYMyIg_a-A9i3ZbxDspY_c2funG1JSKLDwoVkk9SYrPF8Q9-uC208rENsU_RPHNZ3ji0d5bILwFWL4tEV9iOJk5Af520b-zfqihprlo8U5i5_u--KpY0AOIa4ydj4Q2rrIQtH9XHxFSsOhy_zLNKkGt0E8iKhTSAzicUat6e2kpAIYvKbLnFHQVAtCP789yHr9_apANp_Q9Zd5rp9F9lSZxwXv4pw30ZeqsWO_wDNy1JjH20Yq3coz-I2zVZk6qQFygGjtjv_sIa4xezTfIhDlAblCRJMKq-Tz92RV52sXXMJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUO-pUzMaQhyGvsVujnLlAHmpDkhsvFrTaqCh9DkmnmCsAbGyGLq9DL595ItFJIDJw1pR4MvB4KjA3Zt7HQkRySbIPNN-aeZeQOORmOxAS9jkXu93J1insljMEZEattNJ4q3QZ8rrEUb2mIyz0giVklh5mSr9cKaDRhPpLnA3n0PrVZn4e432GNZdNFWesui_QI1ZCtWRTqMI8S7UOIZostbjSesRTEyEDW9EMBQzbZOvhQ8r1STTy_WuNWQh3bHZFPXJxr8djWMMYz4jjXOLal6rZXOr-E6SsM-RtlDxx0JsMMV-UHz3qOParzNOvAx8gaqz0MRrgCUERr3qj870A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFs-dYQ89SSejfvnyaPCtYViyeH5hORS_Wjy-HF7Xq8oiRkMX3iZa6PwitdwNXfCcWg90OVoAC3R5kmmMc7jj6woNEuDFvGKFYxYjv_Fsk47kBE4fFcXWPKfeOyFFVZHDIs7s58tU_KHDS_B8jbV3J6b1B3vAx9OMUMQDHIdOHKKsa5Bi8Di9JRZ0ZVpircgcnsbdBupPnnxeEKF_u-wj7ZvZHBD4-aA3RlyGWFu542kPseaBXgADPOZ-YWJ_WwNNudxKJzXX5wgUrUgHR6UORBdJJdpdY61GgxFVsCR2d1NDowUniyn8EWUll3zVDIX5FkaMAAwiY6dG6vseKwl8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwogzXtXVH-jJs2CwJRMlesTBpQMKaUTI3rMSm9xtyXv1dtCBdGw0sxg8Zs_P1fXso6csP8nj3JMLj39oZc71n_abd7vNNHTut6BIxBkVGuvPkOTuXKDcIo1addVdOdhLH8Go8uFUj2yrGHBK9PN49vSea9rXRAv8jWiHhTXMuHWbBj1FmsQXAFmwSC3gPZSGLUgPylFxgDUhTj3X6r_FACuKiwyPnssBn6bW5kqTcEzeBzpDVqMvLUgdlcjnQ-vgHoUyhE3zf44X2v7oh5EC3AmHskTp23-RPs9n-tzdZqimZWwiTRXs-GjfSBJDR3yWByo-awTQk6LzZz18nNGOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO3_Q5HZKjc7ZSOQU817kMXTO3vkTCd1qtP2z54zF5skFKUunrrG4VdIBhc1Xhv6_SxlmGDyVGnzdbeEhGAT2okXAdH36gSAoy9foGNmSb7939chd03-HILgTvxYzoZ91q9yZtX2wCyhpg6vzhxZQjju8DhDHJBBT8R3bGNPqUVihc_fA5jJnMX-YaFPKA8Tgu9rB1N-5U0si931tTRdkYRjpEEC5ZJ5rBvmNMr5p0dVXUdy8nR4l7YO1I-2JGYNHdxjqgDap1RP2ykD1oEfVj5a_8LjLPgUMETab9_Q37wzpAo4SS5Lx8Xd1mA0yFM44zejMxF_uC7uPo0Oj-lTfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqSsoONAACs7U1gt_2c4GVroxpSK9swIOSEy7LgWg_rZWmCfiCMK2HUJ2cIhoe39IkATw9-nK6xGFiktxi2vSTDkL1WkOlTNF3gFNCzUd19ATCsiXi5ySGdJAFBwUURcxLsUa0b3BD2CPIyoZC403ek3fwQE2qirkOjwuDBOHf7jCHgI1U9ndtvHMQ2VWxeujgxRAwlc6CIiMenar63YhMdvTlGLFE7g5aSbL7fPwhYV4k3q03GcGI4f-TgyxwEFIC3ZKR9Fb8ZefGp2Y3Izv3g02QvvzfxicypFP1-SVV3s2LT-D0xxMthKsx0fI62byDUWJKfAtr15Nl0NzVgwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=MaWhLEC3_eDH9Ojy4q2BFttkKvSgDljT7rNY3faDAaPxz-sqSgvA8wjvGJcvOnHlEYrBO9zI4LFUw-FsDRhGjdsBNUBpvovB6uQ96_zezMLn3HrZ1T2FMCReNTuTBKlWWsAgi4Bf5IM-SsfTkKpjuYvOHsv6xxBezYna6DNKjU6jum4QRJ1V-BCSb_UialyC29XnSZdrS89EQqKYYS51zm8wFOgqbCmWlB86imMAbswJDGnA-vrvxG5M01DV0P45Xt9OSJhhJBoHwjDWZZ2rEBtFFGBBIFvTtPPPG9ARw3oMnfkPiNxDEbIGmpijloeVni6sG3dyw-EhYcsztbsiFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=MaWhLEC3_eDH9Ojy4q2BFttkKvSgDljT7rNY3faDAaPxz-sqSgvA8wjvGJcvOnHlEYrBO9zI4LFUw-FsDRhGjdsBNUBpvovB6uQ96_zezMLn3HrZ1T2FMCReNTuTBKlWWsAgi4Bf5IM-SsfTkKpjuYvOHsv6xxBezYna6DNKjU6jum4QRJ1V-BCSb_UialyC29XnSZdrS89EQqKYYS51zm8wFOgqbCmWlB86imMAbswJDGnA-vrvxG5M01DV0P45Xt9OSJhhJBoHwjDWZZ2rEBtFFGBBIFvTtPPPG9ARw3oMnfkPiNxDEbIGmpijloeVni6sG3dyw-EhYcsztbsiFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Ulyr5gRjkZSRwgCQsa3tCxmEV7swAlSE75o8pqUZhoVGMuOM8Mle-zdYbEH6xeAxLj9RZuom3w8wN-rlTARNnglT8lgc76K1flfUqujObOjD_fiLh7L48K9BY5R_xNRRgZICIys5hYcgwJ70IXqNQyJN36QvpzthkerC7IaLdd6lrVwfFPd_7ayBabFQZ834jQUmzY1ndM83QuxSrUi5odt5c2Tbt9OO53jPkNZr9JNNoxNz5bqKabVqrY4H-ougtv5t-NR5irkaDzC9LCjSo_OvnQF-66Da3jgOU3lytI81hqea5_5OT1aR_bpGeyWio8iHpZQ7ExLLzZzUZQ-ANLk1ZTACXkuPmgNtFKjsRqKjDWLWVbzrO2aqXa8CZE14rRH9pGP_fh-y-PtpRxhXG6S17UmzlvMHDZxc6ltTgEcuVx9FR9sglMybrJKJX3aavU1A9DFep7F6790R9Zu0sj6r4s88WeF5j0Hv9jYsaMLxMeCdYusiafJwyDvh0Wvy0G95xvZ90Zp0iKzzX_R8qGghOzD5QMmrWzq4U-9wGictWEWueTSMFYYaRb2-E4asTfc2_1JhxfMlHwVGdvTwRDfxdHwCd_RB8-n--aY7VTlLEAH8pG6BgxEukyHkxRT3i3mLfanvzo0nRlCTg2_xRs9yucjhg_t3tfntPagOCjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Ulyr5gRjkZSRwgCQsa3tCxmEV7swAlSE75o8pqUZhoVGMuOM8Mle-zdYbEH6xeAxLj9RZuom3w8wN-rlTARNnglT8lgc76K1flfUqujObOjD_fiLh7L48K9BY5R_xNRRgZICIys5hYcgwJ70IXqNQyJN36QvpzthkerC7IaLdd6lrVwfFPd_7ayBabFQZ834jQUmzY1ndM83QuxSrUi5odt5c2Tbt9OO53jPkNZr9JNNoxNz5bqKabVqrY4H-ougtv5t-NR5irkaDzC9LCjSo_OvnQF-66Da3jgOU3lytI81hqea5_5OT1aR_bpGeyWio8iHpZQ7ExLLzZzUZQ-ANLk1ZTACXkuPmgNtFKjsRqKjDWLWVbzrO2aqXa8CZE14rRH9pGP_fh-y-PtpRxhXG6S17UmzlvMHDZxc6ltTgEcuVx9FR9sglMybrJKJX3aavU1A9DFep7F6790R9Zu0sj6r4s88WeF5j0Hv9jYsaMLxMeCdYusiafJwyDvh0Wvy0G95xvZ90Zp0iKzzX_R8qGghOzD5QMmrWzq4U-9wGictWEWueTSMFYYaRb2-E4asTfc2_1JhxfMlHwVGdvTwRDfxdHwCd_RB8-n--aY7VTlLEAH8pG6BgxEukyHkxRT3i3mLfanvzo0nRlCTg2_xRs9yucjhg_t3tfntPagOCjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDTqO34En9LR-EdYZGlINS7Wzvwm_Srfgxps0Ok1DgN0OuDLm-1LsXoWAQZRaHHA_8hgWkM09qdiqoZDMDHRCjtf58GddWgtWNGLzH5nebT2j9KxSU0QqXCOJP3Av0cN9BJcKJkLAP8FE9XSuwbYUHwD0-8vP34Wl0XBibY0SvyQRoOnJ7z4G6Sj7gAwzSFT7WHovwRcNq9eQFTA5FEU3q4VDyGjt6yz_dGryApZWt7B2l_JQoMlaTIUT7N-PJQmahl3yOTWUnd1EY3iylAReDSjjrCUVMb7QZgazu4rcoGFfUnmltZdv4nKQWiZz32_e1ZretkFDGH5uKrVZhbXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qvu16pdrqnyYF5t_BMkwjEejO4VWjPiyZJ31-e_pgLZaUT5AucmxATY76e_euLjf9_NJH0WSWE_8DcNAzlmAlwn7vyzwpt2vHFCLjKeO8GJ23UHgBKOgASc9qi48djqsKNd4QPPi1hoFBD8z1ghicFpA228_ZZDumVGjTcvkdqsPnH-0j_PnQnp8lI-qSNcHWP2tSz60_n_hIUHxoyrUNZwhStxRqO-oZSrZPDd4DUFgzDVC1FmXUkhc_v_bq6MfxmT5bgDWVwy0FEaK7NsY4fr3Br37r5qiOyjNHNkLrFsOHgPTQzzGnm3LcgZaxS4t8YZUBjxOy-yF7CtHcDyb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIPBEau4gj0CdHcWhrN1-Ydte5rt2seD9x-AJToyP8XWb9StdWJq82-o8JlT-aDY_8nL8hMx_GrQAZPtv20bszY5u_DDzPtHL5VCFoBmTq091V-9f-x4Kru5tqbUR5rQ-CsAs83VTecaPkDH26vAFQpk8wrTKll2kCxFCWhqVFlyGuQNzCp4FUMmcW7RrwUUDn8wI9zJYOZKr3WAfcGspBTa0qJzszyw0kMb0mJauk1iOSrH2lUo3C9XT6bmVKHiNiurZ-htBscS2SkT_qy5fbjP1BN2JLr92Cuh_YgDAcFe_DYFgVcNXt8a2pkzCtOaP7l24Wy3zocwDiQRe8hjGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=CQKkF5gHrYFbzmv91yLF_wUmV84WxbLz0eyqOsjqWKGjonu-PPm_0B1UzWDsqY9LQxrZky2_v18Yxpi8SwIWPimcn9Yo6f8KcpC7EurHLYmARzS171wQiY0X2oZhx7TpfPWeTGpBkzC00FYwXJa5jO19f1Iuzt6JZmWrxKIwMt8ARUgDNS1St-2zawdnxnx1ZY-SuL9z4UOnRDvRwO3LQV4BQDj0GViVWaT_sn1g4Jrkr64WxZrvlYd_JFY2nrYkqW8wcnPKXtxIlJ1UyMVP0czD2IT1pHSqTV-0o_dnY-6q6S679UKPyRZBTK6D5brFAmatDaE7hGUdHxp_o2HkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=CQKkF5gHrYFbzmv91yLF_wUmV84WxbLz0eyqOsjqWKGjonu-PPm_0B1UzWDsqY9LQxrZky2_v18Yxpi8SwIWPimcn9Yo6f8KcpC7EurHLYmARzS171wQiY0X2oZhx7TpfPWeTGpBkzC00FYwXJa5jO19f1Iuzt6JZmWrxKIwMt8ARUgDNS1St-2zawdnxnx1ZY-SuL9z4UOnRDvRwO3LQV4BQDj0GViVWaT_sn1g4Jrkr64WxZrvlYd_JFY2nrYkqW8wcnPKXtxIlJ1UyMVP0czD2IT1pHSqTV-0o_dnY-6q6S679UKPyRZBTK6D5brFAmatDaE7hGUdHxp_o2HkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=UwjTCFo-gSWgesoVCXqqxBExH4_IQRpbxYVr2JRk-QBfeGJaod6qQWb8u7fcBeg_E4PaXe3qQkL_YS4Kj_mf2AgpoQ6qVENWUi4lVyWzglIahh2nJVSvMNsC8J8id2ekXXGMFjovZejtpbMp8f4Jp3U4xz3FnhN519Y65RcYkfPMR1VEjAOSQWAu2wr1kiKtBJCszhca4hmFlozVi0KYPWz7H5fmR_ph8qanKyLLvxtd8ko2k9lhVu7Reak7NLZN9uP1mSal5wW4tE_V5NjnwvPy6WwY0WSshjVtaySb6WM_k7pzWCKbx0VM2nkcId2EYicbTHzEE_1_Kixeq2UtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=UwjTCFo-gSWgesoVCXqqxBExH4_IQRpbxYVr2JRk-QBfeGJaod6qQWb8u7fcBeg_E4PaXe3qQkL_YS4Kj_mf2AgpoQ6qVENWUi4lVyWzglIahh2nJVSvMNsC8J8id2ekXXGMFjovZejtpbMp8f4Jp3U4xz3FnhN519Y65RcYkfPMR1VEjAOSQWAu2wr1kiKtBJCszhca4hmFlozVi0KYPWz7H5fmR_ph8qanKyLLvxtd8ko2k9lhVu7Reak7NLZN9uP1mSal5wW4tE_V5NjnwvPy6WwY0WSshjVtaySb6WM_k7pzWCKbx0VM2nkcId2EYicbTHzEE_1_Kixeq2UtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5nzF0UPxPdWsTizUOE7vW2ztqQgjV-7vYyev7ud2cnYtjD1HS1FK2D0rrRzNrZPPO4iCCi-8KJX8sMYY_xGnkZthucaNAbKcEbZrISHChk2YPS7DOsbH2XWWBUbAVYgfmiiBLDWNiJpyTI1g_AO8nk_5nrD_9ABSZF1tOEvYsUaIBnUOhsQM91cZ5Ru3t0GTtSc3vEP2ApntX643UG1a6Bs0C0wzIL5zR8roiyYLdCnEX-qnDC_kKe8fB33Kg12jfANjIr2LYjkaND7_BDpYCFNgLFuksOn_yQOP7XA7lqd_-vCp4pGjpeEx_v-z8FCj3BfDaJ7Wl9dkyfq6BZjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=h5nr3M3RTz9jmXdaetErNcrCbaOnfcAXcVL9qWSkhFLmkgcUTcD7vtzX_EYxzuDqU0U7uKwijjRSetoBBCput3A-8O6CbOXMRqwoip2qXaRPgLsFz1L7CfnOZwi4jXNpE3xvylMbSpiWgWCYIYemY6-aP7cstGwaSGBJ5fpz7EqrPsla4u-qbV9jx7XYt7IBCO1V0ivM1hfoP_ZDhI4fcKklPX1cXAFf1bHugOEs8oBsZeSPXJGA53HQzRKcJx_cT2rOsI3bK-ejDV9IpnpVTNMPyfcHJjtWO2_BfQzu4z_az-iQvoE0EKVNB0khu8RUdtZN5pVVBrwrsAMFfx5mnZIcflBA9Iazah3HqXvmrpZE-B2Jdo2WVsxKXWS8NIdb-bbUMagGsZ5UGaS6yb9ZBrvhHjzyxJMIzVO1yb5UeHuaOu-uwvOtP3nyHuQzpRVVk8mxexC6z0ySTGkLeDu68h6HvJVDgWRY_uX5T5eAMAv-ZS1fxbrYtl0yRDrwVqUp7_-r3u24h8x4lbabDMc-0jMdC1BP_Ogyn7GzqmpCpVKgiB_4dKfcIpZ1dimVIN4InTldMubrnsJZ08IzFMKhPJWJO-jCf3PwS9hKBcUaSB3SQAPXNKMhf_ob9CjzDdUXm8_pWjD-5SLqwpa1tG8JUWN3BqhAmpV6_MhEBrDJj-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=h5nr3M3RTz9jmXdaetErNcrCbaOnfcAXcVL9qWSkhFLmkgcUTcD7vtzX_EYxzuDqU0U7uKwijjRSetoBBCput3A-8O6CbOXMRqwoip2qXaRPgLsFz1L7CfnOZwi4jXNpE3xvylMbSpiWgWCYIYemY6-aP7cstGwaSGBJ5fpz7EqrPsla4u-qbV9jx7XYt7IBCO1V0ivM1hfoP_ZDhI4fcKklPX1cXAFf1bHugOEs8oBsZeSPXJGA53HQzRKcJx_cT2rOsI3bK-ejDV9IpnpVTNMPyfcHJjtWO2_BfQzu4z_az-iQvoE0EKVNB0khu8RUdtZN5pVVBrwrsAMFfx5mnZIcflBA9Iazah3HqXvmrpZE-B2Jdo2WVsxKXWS8NIdb-bbUMagGsZ5UGaS6yb9ZBrvhHjzyxJMIzVO1yb5UeHuaOu-uwvOtP3nyHuQzpRVVk8mxexC6z0ySTGkLeDu68h6HvJVDgWRY_uX5T5eAMAv-ZS1fxbrYtl0yRDrwVqUp7_-r3u24h8x4lbabDMc-0jMdC1BP_Ogyn7GzqmpCpVKgiB_4dKfcIpZ1dimVIN4InTldMubrnsJZ08IzFMKhPJWJO-jCf3PwS9hKBcUaSB3SQAPXNKMhf_ob9CjzDdUXm8_pWjD-5SLqwpa1tG8JUWN3BqhAmpV6_MhEBrDJj-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ob_IS1RjmnGUPOPXMrzGlmHIRJp8oHlsXNM3r2Vcc_572oV-9vlGQZg_Olmsl4e0uGbs2gFW3aWfLv2wfGT6bzfy4n0BPGRWUIG0SjaGmdp_rGtRoK7GrOVYuvhyAjARn0kHg92ig1UOn_yB_zZyx64Gu3F4jGJU9AjOq0bwrPFHcMFQ6e-NmbYOMaOmxCMZL8_JGHF1wr2XJaEW8JI1fzdTyAUodVGxQIuJuESgjKZfXaBYHNvdY4KzYo5f46KKmMi5X51KCWcbHECegdfKfcDqUnqK6YUDtkg5hjxoS1Z_q5WZCmeAdNbuthlqzZwUs5ZVZIlXKP1Kl8AMvdJ7Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ob_IS1RjmnGUPOPXMrzGlmHIRJp8oHlsXNM3r2Vcc_572oV-9vlGQZg_Olmsl4e0uGbs2gFW3aWfLv2wfGT6bzfy4n0BPGRWUIG0SjaGmdp_rGtRoK7GrOVYuvhyAjARn0kHg92ig1UOn_yB_zZyx64Gu3F4jGJU9AjOq0bwrPFHcMFQ6e-NmbYOMaOmxCMZL8_JGHF1wr2XJaEW8JI1fzdTyAUodVGxQIuJuESgjKZfXaBYHNvdY4KzYo5f46KKmMi5X51KCWcbHECegdfKfcDqUnqK6YUDtkg5hjxoS1Z_q5WZCmeAdNbuthlqzZwUs5ZVZIlXKP1Kl8AMvdJ7Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCPZnnr3d_SSTk4ysnJBG7Q-JSN_-JeRWGBje2Z_Zf0cz_lEQ1I7KAKAg10oz5cqgwuPYZlYD82P7vYBuAocGpxXCfMiiGJOtBXjzyP3_IUB6eQqLEIN1bzVhFVJIABN_AXUv3mnPydvReuKSQ4i7Q8IN6OWvBrt0OWFDKQLo1EFEhkXVVdS39JvDu6GH5FZD2ujJRb60AFC6Y4lQwEDEgg5FAdduIxzk7ZHGpD-CiejzqJ-tUqiRYSpFgB3q2ZgPxEts50KUSXUkUachJJ_W4iEib46oMGlmVw-mJ24vmANogYewFTO90mp_W5dc6zWWEEG-BrZUAUq45giwcXgrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=RS2RmQu6m636WiTWvhB27tMeZ1iCNWObaDJqwNl5-v5Z3k7JqTH99GCdwGkDfHVqVYgPWff7DE4dsDBAjpF2C1rduLAXzuMUyKVqMqGIter5T1OrXjD7S1JoNtoTWZusJGXOm33dE4SeHHsAvZe2ZwWFz3LpeBQ-BiMwfyQmhLB1feYCi8dZJSzMh4KuSxJh2Gw9mH4mpXhWaHJrVjVqkSq02j6VI3f8rzknp7Q3pV8oofh6YZz6Iu2B6W-MNABazRch-dx-B07lAiPE1jhyth9MYcJbCYNahHMkJmiS_ovLPwP8MnOBRvBYbindfbKGImfMK6T6UDbWCkyOwN8izA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=RS2RmQu6m636WiTWvhB27tMeZ1iCNWObaDJqwNl5-v5Z3k7JqTH99GCdwGkDfHVqVYgPWff7DE4dsDBAjpF2C1rduLAXzuMUyKVqMqGIter5T1OrXjD7S1JoNtoTWZusJGXOm33dE4SeHHsAvZe2ZwWFz3LpeBQ-BiMwfyQmhLB1feYCi8dZJSzMh4KuSxJh2Gw9mH4mpXhWaHJrVjVqkSq02j6VI3f8rzknp7Q3pV8oofh6YZz6Iu2B6W-MNABazRch-dx-B07lAiPE1jhyth9MYcJbCYNahHMkJmiS_ovLPwP8MnOBRvBYbindfbKGImfMK6T6UDbWCkyOwN8izA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Bn61mHczcwSiQs27MEDWUOD1yWJjN-5v0-vH970Ncw8_6UglX3PQZxoYdUilYuwqWYpEbRpvJImlc_qNEIvxp_L8yABAfaLUct4gXG5GHgZ3idOvGLCL38t4gkaowCHg-Y60eBsKLSlIAVtBXokL3RwXVO9AAIeti9veVwjcmHiYM4nYX1NZjFWr-I-wmW_nCxdmeSfsIkmaP5zCk2cJcFWL3UKF598S2vuDfsjJsk9EuNa0OY5GpSCF97SxR4D8Dtp8ob3yF56ec9paL_XRiTKhWamBmSGljWDiqNIk6m5U6CiV0M4vyE0wVM0lepf89RkEDMwrJ0FHQyuWDoEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxv5QsWmkDrQjg9yY0LBPkDzAQ82sSr7MxcSS6Pps90vxU1LBiOSNDi8Bqe7WRji04BuOIuXuwgj5IGKTdMdcLsqos8xAWNSBZtFrTT0prrUlRVZ6REo3fyb06-hcCAOQzpMV4OPW0mDNNSJWmpvvPJ93zNBA-YOwem3mET0m2RhaL-RjB4LAhgyrW_g1ZJpZWkbWa7tEt04qKSM9rCdwBQZwsdIagaPvItItDzc7N7cmIC-9i6QiQqiqYuhRPpR4p727R7FmJwkWEfSY8pLAse1qm3ug4MCyJkwdRswofP36HfyY3rHdSa2sTsv5CiTG8OUkFv7N7oJPTqsny_18A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=CbH3uEHcvYAS4XpIJW2QycYnVPDvsEIwSHQkluVYH0SBZRwo_xhWQzkiMOqDvXepMQ0f31VFXz9NdeA2jOMVzfCSdh8X6baxZ3rLp3q3EaulDd2KYZnvAQKQSHFy6jsIEUtsWIoFe2Ys49AZbhP1izTOIEAL2F4Ai3rcZ2gO8_OcWrXzUGpysJzAm6lOj8z--cEnxaK-Mkh4aF3OmsjDxxmLMayMky_GbzWb9cYox0p9VI-_Z2wZPw06JfyAQJ-61aJrwsi0APzQO3a_QYxMzFoRrd6wdAPIEn7wv-lKN_HSlZ06vMyM93rhIgd6yveslatINekRUeRB5XEFOkRDFS9sxFmSk3SlfaHM-lJXrRHQqMz7EKkqb_nzqLqIUBQrZzccq4ybCMJ4aFZmq4mrIwul6UwUHpe82WPK9K09AH4gV6khfNc6cJb-M8a-XeIDl1RFD93XPbYKXej481fcecbx0r1nFVyC4INEr7ZO40V7Nz_88IOfKb9xAh-LXtLYTSJBppira44b0_uuXaaq3Jy3qkRz8xV5xzlCO2P4EmXiNIVyodbdgg2pIoo-95q5_l0OKy3mTVfXbzOwzWlb1_5Cb_Oq88dN4gsNcTpbPz09qHiQhWzZ3X3FhjwfbThb2OpegT8W9Ie8TUNow1MnxngQOHo8xJkZ0XF_7iAToFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=CbH3uEHcvYAS4XpIJW2QycYnVPDvsEIwSHQkluVYH0SBZRwo_xhWQzkiMOqDvXepMQ0f31VFXz9NdeA2jOMVzfCSdh8X6baxZ3rLp3q3EaulDd2KYZnvAQKQSHFy6jsIEUtsWIoFe2Ys49AZbhP1izTOIEAL2F4Ai3rcZ2gO8_OcWrXzUGpysJzAm6lOj8z--cEnxaK-Mkh4aF3OmsjDxxmLMayMky_GbzWb9cYox0p9VI-_Z2wZPw06JfyAQJ-61aJrwsi0APzQO3a_QYxMzFoRrd6wdAPIEn7wv-lKN_HSlZ06vMyM93rhIgd6yveslatINekRUeRB5XEFOkRDFS9sxFmSk3SlfaHM-lJXrRHQqMz7EKkqb_nzqLqIUBQrZzccq4ybCMJ4aFZmq4mrIwul6UwUHpe82WPK9K09AH4gV6khfNc6cJb-M8a-XeIDl1RFD93XPbYKXej481fcecbx0r1nFVyC4INEr7ZO40V7Nz_88IOfKb9xAh-LXtLYTSJBppira44b0_uuXaaq3Jy3qkRz8xV5xzlCO2P4EmXiNIVyodbdgg2pIoo-95q5_l0OKy3mTVfXbzOwzWlb1_5Cb_Oq88dN4gsNcTpbPz09qHiQhWzZ3X3FhjwfbThb2OpegT8W9Ie8TUNow1MnxngQOHo8xJkZ0XF_7iAToFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dklJjiQmctqPyXggJax-5k8XRZ-Tgxwfn3gG_-SZVapyp9mnNOqH-y_vSzJ81Dk-vUjw9HKQBV3oPhMBbtfh7d9S0oFFlSdu882k3e1fHmN4ZEDGnGTJEOGoXT1dqxBuqqhx8VbbnNWU8nLN670uC-AQcCb2sFcLh36ehOQ0cgeBT8brREjZxcQ1X5UDvWhk09jJD4sGHPxCxvhE-ax2XWyMw7izbGAS4A_I5OVkyv3P49HLDVTqx6cPup1UksEy35SQ1VcrlaaP6QvmXeOD8bpkKp077TtNHs3llZuHL0NFiDVj3uWEGiBiOmlprOIcTWQPZtuf2OoRwsHLMFFDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqHV1gp9xLj1FCEGopmBcT3frjX1A4cT2MQjpJsg_DBpkA2DPOzhlt1Oj2DILC2QKh04UFzUrwDTy1I0z2isgkltuFTGC0Pp6waO-4jfm8SwDqeVk0T9nc7tN8dPLBJOq-Aa_YPLanDusTEvx-ZM-RPRwNc1tQWJtytW2poizmCFtrxPvFwjrQhWs8qPa6PLbmIO9XD6x70FBJoV2iTes_2vBd2tSugH8bG3POwRU_6ckjA1__2wYhdW2g6DGz5bOmmCMXpWluRerWYtjxnbBH-rHNe0cRciecchb98QshwT-2nhgTcxAVgpPiShnaj2NQqoVSitSV1fcTt8zPfbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=R0fR6-FRm5fG6TkNBdcL5UEnYxrpcJ2pqbTK6YzwFmSvD1LRbbushU75LVPIYEoKqt81e_6DazeHtfWv3q3tKR889FmzYxL8oqVRVCmlK-HjqSoN0V-6ZjK4jasdPTrLLyPwVx83nyGJQRSbZRXk5GB_pHUTpBrw3TAz2ycexu7FIIFQTLwOpiqkz77T4DE65Jf-TRpE-LDRLBFlCCci46TeY8155DzS0bPfJDeKharpLkBMGkw9AvEFgBnVyayuQKhbFO172RhpAJ2NTEIaQFYK54lig3XQZJSDY8sr5DqP4gPYIrIb3AIksX7HdyMYRD0TV_U7y4S99yFDMr8BwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=R0fR6-FRm5fG6TkNBdcL5UEnYxrpcJ2pqbTK6YzwFmSvD1LRbbushU75LVPIYEoKqt81e_6DazeHtfWv3q3tKR889FmzYxL8oqVRVCmlK-HjqSoN0V-6ZjK4jasdPTrLLyPwVx83nyGJQRSbZRXk5GB_pHUTpBrw3TAz2ycexu7FIIFQTLwOpiqkz77T4DE65Jf-TRpE-LDRLBFlCCci46TeY8155DzS0bPfJDeKharpLkBMGkw9AvEFgBnVyayuQKhbFO172RhpAJ2NTEIaQFYK54lig3XQZJSDY8sr5DqP4gPYIrIb3AIksX7HdyMYRD0TV_U7y4S99yFDMr8BwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=FwyIXNQGcSCFWP-y8dAfne0u02uwy6aGEvVkMRHQy4byDw1hoevobRWEZzhteTqSahEeV4C_q5Gxm7nlpW51oQaz4KTyYW4xczZsZcnYgWJXwwrnILLJPVqfF97ohscTl7_hrYKyYgQZDlEH_fLpaY11wQYYqMH7G0aJiIm1tejvBfA5Fe_3HPRaEm61o-M-wH2FGvFfQ_-fc2CYQmwj9ni9GbahE09PlfmrxQbYiMxm2TWMFWEYMm-a7LO5GyrjLeVi1FA5dLOzAo9UDBExdWXdVodBaNdYvfo1A_Zkj17On50WalMwqxM9qE41EKNZtcHov62xKOg4tVauv5EiKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=FwyIXNQGcSCFWP-y8dAfne0u02uwy6aGEvVkMRHQy4byDw1hoevobRWEZzhteTqSahEeV4C_q5Gxm7nlpW51oQaz4KTyYW4xczZsZcnYgWJXwwrnILLJPVqfF97ohscTl7_hrYKyYgQZDlEH_fLpaY11wQYYqMH7G0aJiIm1tejvBfA5Fe_3HPRaEm61o-M-wH2FGvFfQ_-fc2CYQmwj9ni9GbahE09PlfmrxQbYiMxm2TWMFWEYMm-a7LO5GyrjLeVi1FA5dLOzAo9UDBExdWXdVodBaNdYvfo1A_Zkj17On50WalMwqxM9qE41EKNZtcHov62xKOg4tVauv5EiKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=eoZ9GXqmTt7EuUJSni3y_QqBbrlWUmrS4lKYZauv5TsoFuiurKpX21EcGgmW3Kqn1J0CT9mlh20OQMyAkzSuNj024Tw-walvc5iFWoRkzc6agzTQa-CuMYcgGUGP2PzvGJclWQIpu-kDEWTE4K0b3svJG0njlBHB1zvaDc4WOHDN1xYjz1rN7izr9EN7pf83FdX6SmDkvu91rZXpCBFIHbtp4ygPAi4JqZTLYw-Q_mQCFcoNx1GYUlQImflXfU2uWdcs4Smm4nfQIs1AohbDGPsLeAdqSTgDr4XHMjt0BTu8lUxfxBKQ2-QsYkAJ6YXNF5-aLHjzO8ogy73BRczGBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=eoZ9GXqmTt7EuUJSni3y_QqBbrlWUmrS4lKYZauv5TsoFuiurKpX21EcGgmW3Kqn1J0CT9mlh20OQMyAkzSuNj024Tw-walvc5iFWoRkzc6agzTQa-CuMYcgGUGP2PzvGJclWQIpu-kDEWTE4K0b3svJG0njlBHB1zvaDc4WOHDN1xYjz1rN7izr9EN7pf83FdX6SmDkvu91rZXpCBFIHbtp4ygPAi4JqZTLYw-Q_mQCFcoNx1GYUlQImflXfU2uWdcs4Smm4nfQIs1AohbDGPsLeAdqSTgDr4XHMjt0BTu8lUxfxBKQ2-QsYkAJ6YXNF5-aLHjzO8ogy73BRczGBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q98A6vyQoD7oBDQHuhC2zHBDsY16zZ7wJFkNRX-2HC8s7vrpM38m-0-AU5RkmianrDG1fsFcBSCSaufJ4FeE2lZalK32GWaNm-qt2zgMmKs4Sdmcd2zF9ogfF6mAGeqlOHSSH-zjqeSEb5Z7g0f-3xrdK1DpdD3pcwy_qgnb4FiCg_pwEqFG3E1CAQ72ts07hBVMb1KSe0TZ8nIiImlifWByPMBuGP_qnI7mzcBIpbJHQwkJU0wnSURu7PsKkFOKxUDpVqmJNHmm9_r1XgEUVKGdPSVViRM7YrqZqQIo53D98PPD1QLK8KOusgeKwKeDMCAa4XKaT9QyOA89yWfHPQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Iel-UDNC2GTsJRz_PgcHffDTx2DEDaeIkxPIJOD3ejX3DZ-BBRHMftp2IcAOSbO_UeV5_88NT0eSbPLhjruznYL3BS006qCbroeXn0W-dhQfw1nCPp2vssRNN_sMQdn9qxGc1i2Hnqr-UdD_rWaFpgMwzd_5wbbbVmsLDjvZzZYEmSU2CPSb02F7dYUVbkzri5D43xx3yUZV1CvahLVdDzbkdcEPHKdGEEywH_kifTd76Cb2Alr2s3v-ydjlukR7qFrAoDxHCf6JcVUS3uI1BW56yoCcLoGTBe7tN3NedqPKzZUS5hxXWAtzuE3jwEBWp-6yA91yfiJ-b9N_Bh0UDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Iel-UDNC2GTsJRz_PgcHffDTx2DEDaeIkxPIJOD3ejX3DZ-BBRHMftp2IcAOSbO_UeV5_88NT0eSbPLhjruznYL3BS006qCbroeXn0W-dhQfw1nCPp2vssRNN_sMQdn9qxGc1i2Hnqr-UdD_rWaFpgMwzd_5wbbbVmsLDjvZzZYEmSU2CPSb02F7dYUVbkzri5D43xx3yUZV1CvahLVdDzbkdcEPHKdGEEywH_kifTd76Cb2Alr2s3v-ydjlukR7qFrAoDxHCf6JcVUS3uI1BW56yoCcLoGTBe7tN3NedqPKzZUS5hxXWAtzuE3jwEBWp-6yA91yfiJ-b9N_Bh0UDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=YZ7M4NQ-4NJV59QoHwLwRjBPwAA1K-NNt7gpGpUWgXI3lNmKaLfEV3u9TtuyxKOrC3jHBBa5olvbxWC3pD1wmM8mjPDEtECTfBj9AThTTn5h1iX4IN7eOFSe4phim0OwsYjIyDgUVLL8aCo2C8iTXKh_nRL31mf9OguEC3r6923CCxwHdp0xlCGU5ftwB7S9fSsjJCHnhJT0trDaEyQnjpklVDTOF7ZG85zYUatHmuRyR3gvIQQCXgwQ0xnT1OIuQ8WNNGjvChv_reAUJL0NL4UtQv8geSeHrDaCcg4voqgQADCwk0WNri26f87z0I5IB-RLa1zWRcda7pYUYX_nPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=YZ7M4NQ-4NJV59QoHwLwRjBPwAA1K-NNt7gpGpUWgXI3lNmKaLfEV3u9TtuyxKOrC3jHBBa5olvbxWC3pD1wmM8mjPDEtECTfBj9AThTTn5h1iX4IN7eOFSe4phim0OwsYjIyDgUVLL8aCo2C8iTXKh_nRL31mf9OguEC3r6923CCxwHdp0xlCGU5ftwB7S9fSsjJCHnhJT0trDaEyQnjpklVDTOF7ZG85zYUatHmuRyR3gvIQQCXgwQ0xnT1OIuQ8WNNGjvChv_reAUJL0NL4UtQv8geSeHrDaCcg4voqgQADCwk0WNri26f87z0I5IB-RLa1zWRcda7pYUYX_nPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRszFiGofKi_dvfMPPoE6sfK9BN_USIvfnPKg8Hfs1cojEG6j371FzzXfbiBbwZV7-QuzUxAC76eNBrhO6_if38FlFCt5S1nFzGVOUCO_LqBz-6SUx8U-I_Vzx8_YBnxxFRrkPW24ulYCaaltavqKg3-066Iic-ASa1kmsV22hbI-GUbz8oLFs9K5Fsmr-1nbtUP2HhuVcvpNp3OdARRUJ0sFU_BSY5RQUkTcUqprVnctA9_BYCL2TWakHoaJLN9lQi57bvIPpbTqTs0YYcx6FGsgx7AD9XwPoV0cnBubau9Y8tO0mOCiYyhpN8tCZHvZcpq40giPMBuZoKk2CMz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=mMbRZG8Yvta5Th-l1Qr5vtpV-pa89raTFB2mR3Etlnjvw95I9az_0tuIwZTUEzcVxYDKZEyAa5Gjh0-sHH_Eoxiznj8ZfTB67Zf0BWEVHD2kwK25n-_iQ2ES2MHU_D5B8uIFhtuyPF-OEDCBqN1qa4EmMR1h3knFXF3MjxFPoWQdKBUzGp5S6v9ffWHmWy9WUrldtG1AYXVT5n-g3N_A3ynLSb7YqlTaTphuJt1VJEpnsXJbaYj7oksbx6ZpohYpWKY4G5T15JZgaEOFF7VYp5ZIyG4xrhLgpPZl0XF8Hk3sZnm6pmT01777WLEcl5Vdxqw7zkbPFDIjH90MECKkT1LezOLvQt3Yhm3_XOLLQ3hWDhyWMI_ZxxkuZVhfDa7xJaXj5dZbHzw2QtVs8NZpYkAhbWFWyXobkpALjZMwcf6PgFCnPDn-KZsZRHBSTj90Uzy3TTpIC61WekKFELm0zwm5FTNMUftUHhYbWs-STC-W7gkIFq-rKuppT12JG57HIcLJ9QZLD8I6gk3m4y2jraXN52YCW-gg1I6g5FfRXUhGW3Biwfgvtwd90GjHYQ2Vhs5wOCH6pcPLhY0FFESepEB9RI37bCWIVsZ3d8woe-xNKs1VEGGsp3PaKb5yegcXo0Yy_TzesJPJyVQEE-MVBfNnXQx4OoRGTQd2AuKv82c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=mMbRZG8Yvta5Th-l1Qr5vtpV-pa89raTFB2mR3Etlnjvw95I9az_0tuIwZTUEzcVxYDKZEyAa5Gjh0-sHH_Eoxiznj8ZfTB67Zf0BWEVHD2kwK25n-_iQ2ES2MHU_D5B8uIFhtuyPF-OEDCBqN1qa4EmMR1h3knFXF3MjxFPoWQdKBUzGp5S6v9ffWHmWy9WUrldtG1AYXVT5n-g3N_A3ynLSb7YqlTaTphuJt1VJEpnsXJbaYj7oksbx6ZpohYpWKY4G5T15JZgaEOFF7VYp5ZIyG4xrhLgpPZl0XF8Hk3sZnm6pmT01777WLEcl5Vdxqw7zkbPFDIjH90MECKkT1LezOLvQt3Yhm3_XOLLQ3hWDhyWMI_ZxxkuZVhfDa7xJaXj5dZbHzw2QtVs8NZpYkAhbWFWyXobkpALjZMwcf6PgFCnPDn-KZsZRHBSTj90Uzy3TTpIC61WekKFELm0zwm5FTNMUftUHhYbWs-STC-W7gkIFq-rKuppT12JG57HIcLJ9QZLD8I6gk3m4y2jraXN52YCW-gg1I6g5FfRXUhGW3Biwfgvtwd90GjHYQ2Vhs5wOCH6pcPLhY0FFESepEB9RI37bCWIVsZ3d8woe-xNKs1VEGGsp3PaKb5yegcXo0Yy_TzesJPJyVQEE-MVBfNnXQx4OoRGTQd2AuKv82c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUbkM8_L_r6xssJT0fH_JCFHo95rW3VKv_LhBgY0hrxg-72pv479eeVPvl1EXkFxfC2fmkQGp7h4qSYTLvS0x0Q7g4NFMCU3TPjgamoSpTsQ6sh973Vi1VgYDK45iQXGu5VdCJnblbfnCVoe8cXNSeyumYkNrJ0ov6DJMAOXH1xvR4eajPAKj0AVcTYBLqSBk5QBQAGgM7s8X8Srb4Adeo3H3QtODqll9N359bex0y1hFE6avPomJCkk3OwGkQqZumKHLTwNdhP1En_eB06KwGWHYQVDkeKWcYPk7wtmTSUa64ZpAYGiVxeGg_nreKXJD-AvWXvcfRq2cAqU2p5H2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=RNaxgLlDgmkFtH4qEm5z9X7Qm8vJzo5GaKSmpGfzHpoXbsFeuq59xtRZOn4cpGzfdPPD4fTFzZNWLV9tAvsvHfvxdqQbIdDaw0g_l9EyUbUKwGM2cs6nvYWd4GFR0vzS3ZbNPCB0EIUUUW68elRBeqd9Tc8ILXmIlHw1jMxelnIzhUaWyNP4Gx9Y4joAIsoikWAJ2SH3nXpvQDlnnAT5d_BlhBpHZN5JZZaq-05l7bZlGWp1wegYz6UVJk75MbSgpyutYg5ROIU_Dyyz2PC-TRc3dwa53ttRvjH2RwqOrR5l9nMfT7KcVbrfgd7fYf8H010-aQ2dWjj3jd607LyMwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=RNaxgLlDgmkFtH4qEm5z9X7Qm8vJzo5GaKSmpGfzHpoXbsFeuq59xtRZOn4cpGzfdPPD4fTFzZNWLV9tAvsvHfvxdqQbIdDaw0g_l9EyUbUKwGM2cs6nvYWd4GFR0vzS3ZbNPCB0EIUUUW68elRBeqd9Tc8ILXmIlHw1jMxelnIzhUaWyNP4Gx9Y4joAIsoikWAJ2SH3nXpvQDlnnAT5d_BlhBpHZN5JZZaq-05l7bZlGWp1wegYz6UVJk75MbSgpyutYg5ROIU_Dyyz2PC-TRc3dwa53ttRvjH2RwqOrR5l9nMfT7KcVbrfgd7fYf8H010-aQ2dWjj3jd607LyMwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7ckdoNvJohEiXwFx6zTXL8HVhPmoYoT165YKnItMKDVmOxxEQ_p5vpW9fONwmDv_AlRiK4tmhsBRqTwYBvKBGYA8uHjIdMBR9U6Rbf1ZT8hH7KC915dD0ki_oxbTCrcK5FX28pB7J8sPJiWirPb3yxh7ccZ6kY0p5zAs9OTqB400_DnO_LHwlbaQDVUG53ra6FrofN1yDmH2z1ML8A14tbv6F94tCfEWeWdxdRoLRjaz9rqaXxT8Kghx2rTQb5awuQJQFkeqUfZUNekO6COcqLVF-o1XQXVaGs4FptwYLcGxLWFM6BuowI08eLP3YXgsSD4bkJKusH9KRQqbJVFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIwgBs7RITb-KoUXbu9tVKwxpoyqNk8p91ILmuzNZ3dWkKUu1kajGZxr9LdiFBeR7NzZRG4MieS6R3CrZk1s-giW3GsAS4lmCGzukn8xMFpRWZwvUYyqaGna17wJljZFrMiBEEQb8L3FB7prtsQlYR3xlnU20KZjG_gE3z95dFoM1w-CfZDBQ5k-6tMZQayzz-FsHqViILgd-NuxAqkxcFQYcSgmuwlYvoEEbnjKcCOWFdk8USaX5lb2zi2IoJyhUdoElX8kQiZIHZ-aic7v21o-72eogIBW-Xpus3ktJzG2J2Zz-w8mCf2-uQo5GObfGjAE3qYwskttKXvUKhP2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkI0D6nFx9xsa0WhS1dWGvqp_oV8x_a6fEQZnLwOzJ21-kVXhmFa1Gp0zOjMYNKuk76-Oo1rtZl5tLujZej4Ii9g7P8CF9jBTdcQQlrSbWki1gZ43FD0wLqxPBf3WxDo0BWZp5NxRbA6v2Py6ckdHrE-YJidGBBl0NE9SIi0qlyf83nNY_YXdtiFM403r0qYIEg0cZXTiNEJJ2cE5qtdwTrRTYtX6AugwNlbHomcMfh19vViEcpqIictBMckKu9xBtTvZ6bEu2I6JKdyCJTER8DIQOhiBNRJiCQoiVGw0b755cuwCmGP27YeD2KGx2axCVLeYINPViOZOzBsx9tilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=L58J4Y0w9JZFO1pcaoKe_oksL8jghaheo7-xZ2l5gBDzqxbrgHiIs4s8VJHtixBWFcvRNKpa2ZFKBHMQguc7SaqSqohgnPCcX_OkiAi4T9N-JrqGuomIqwOUujbaAUuX1m8qvLkySozo--kUZTWtJrTZRF8QaJcl5mX0eo0pRmdqJQedCoMxNZS12i8lfPlmBaUfCzmtPkPRwt5NssejrrX1FMrszIDTvW8guR8jA_Uyv9FxpZhEIFhRDNEkyJOUOlZ5bZ6LWBECmaaee6crfshC9EoJc6A_vpWyBJM398TbCJFF1m8laNys5lyoZTWpCoFXvGvXy0CZEIYXgLSWsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=L58J4Y0w9JZFO1pcaoKe_oksL8jghaheo7-xZ2l5gBDzqxbrgHiIs4s8VJHtixBWFcvRNKpa2ZFKBHMQguc7SaqSqohgnPCcX_OkiAi4T9N-JrqGuomIqwOUujbaAUuX1m8qvLkySozo--kUZTWtJrTZRF8QaJcl5mX0eo0pRmdqJQedCoMxNZS12i8lfPlmBaUfCzmtPkPRwt5NssejrrX1FMrszIDTvW8guR8jA_Uyv9FxpZhEIFhRDNEkyJOUOlZ5bZ6LWBECmaaee6crfshC9EoJc6A_vpWyBJM398TbCJFF1m8laNys5lyoZTWpCoFXvGvXy0CZEIYXgLSWsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaECrMEecH9hLxdKEs-IuyBDbhmo3Efzrdy8nSalQgl0Yyt0t_mNiyic_Ob_vFHnTqDwR207CsN1lOrpBQlyZtfSRnw7TsWRYieIKJIXzbpdzpvA1G-uKKLpx0rKdok8JlZBM9ja9zSr40s3fGPpT8NYeJmCZYzh4S7Q0XylFgE5_qcWhcyO6v9yfSsmIEtK3p_BROqSm0-29xhOdS0SW8-3IlBgeyop_bnLJlYT0OJ-Cg9oENAp16C-f8pNvGm95qzOdrdw9XeiufDkCgXLyLk_nPI_Ov-HC580y0my1og0TUbViIJusgP9tH8U8osqwVc9hPAzSMOmBvV0vHTlMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFAfeUz5bfUc2Ve3NXpVl0luT6eXYPBe-cO5ukGdxDkqvDOL9sSG7GZj3YpiTHV3Or3nMHkFMIG7t0-ovar0ptk9-mtr87O4WPN0F9O6VTVTdw9qqgTISgrvEEgTjMAN78KftV26cb0ILleI_7ZEtx2shjbQNzHdGtPg_a9llCZHaB5LVxD5Gvbk1ksvKE61GnbQhpbr1hDTpqvqbiG28qsi1iynznJh9f7weU3NtIbt31CqrIgzqqU1lPB83kHBjyNTrDPPwyk0Z3Dnu84vTLhAHxL1BLHX1qFcrBtbnTFnpRHCiIu8txBHh5A19xC9wT7Aky1NKnZ7HxhnAeUu_mVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFAfeUz5bfUc2Ve3NXpVl0luT6eXYPBe-cO5ukGdxDkqvDOL9sSG7GZj3YpiTHV3Or3nMHkFMIG7t0-ovar0ptk9-mtr87O4WPN0F9O6VTVTdw9qqgTISgrvEEgTjMAN78KftV26cb0ILleI_7ZEtx2shjbQNzHdGtPg_a9llCZHaB5LVxD5Gvbk1ksvKE61GnbQhpbr1hDTpqvqbiG28qsi1iynznJh9f7weU3NtIbt31CqrIgzqqU1lPB83kHBjyNTrDPPwyk0Z3Dnu84vTLhAHxL1BLHX1qFcrBtbnTFnpRHCiIu8txBHh5A19xC9wT7Aky1NKnZ7HxhnAeUu_mVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=v5ivAdPqU7JYLfW4wuWlUtVoV1fI9DDRaicWmInM7rr088S6cSL9AVFIlw5j1bpDXJfbtTtLnzCZfNBOifuupicvRAB6V_UhYyeaWu9Dq6layXVjx6pTxjkS70c2NMTXu7XtSDAjadQJbmfKvOwp9uzmDgHtVQGQGHZzTrV6WmwmFKx1Xe4HIyt8laqhZEXQZCXQf7RdT0rVk0J_GiKXeachbbcESQUPCvKAZszqcC2CGlPDneCfCLJzehiCS5i_N-4fXA8Fisit0GrdoQiuYRqcAxB8DfsF0qz3uKWA9gDtLGryoB3T_4bDUHf9XJKFlZS8qtQ4knIHSCgyGRnajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=v5ivAdPqU7JYLfW4wuWlUtVoV1fI9DDRaicWmInM7rr088S6cSL9AVFIlw5j1bpDXJfbtTtLnzCZfNBOifuupicvRAB6V_UhYyeaWu9Dq6layXVjx6pTxjkS70c2NMTXu7XtSDAjadQJbmfKvOwp9uzmDgHtVQGQGHZzTrV6WmwmFKx1Xe4HIyt8laqhZEXQZCXQf7RdT0rVk0J_GiKXeachbbcESQUPCvKAZszqcC2CGlPDneCfCLJzehiCS5i_N-4fXA8Fisit0GrdoQiuYRqcAxB8DfsF0qz3uKWA9gDtLGryoB3T_4bDUHf9XJKFlZS8qtQ4knIHSCgyGRnajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=MB1XGZxYvDT9fY5tAONigYugs2_TPJNVxh4xyE6MC_niOnsErN96nBLk4e0M1aN6e31imki1boJFZLCeVlVsZxlaCWqpvKrO3zcEMecJAcqAZ9XyY_2RxJ8PntPHt6O-Rr29zguAFPjkmW8pPrxXAqPUs-fHIQ9UqUkWu_sQuSy_s393bubzXrbfjBdqFVqSuBFWUWw-QExQP7JEv3oBxJWG1C77KWiT_R1PU4deJZpyY3PxQ3D-uElmFdIYK5cZgyeYOH5ppjJxepn1CI7PvdZNNPmv2oHDIOzfghmIiITW3lsE2ye0JmJPvpMv2Gdd1UcNWytCw5UBJQay-NvwEGYUda4qL78l3xC9kIrVabHBoGSBccos-zWLoFLw0P4Tg6um6g_Nqbjq_M7xHLBfOAaVBfH_ZaU3MK_AP3S8OwpJz9WUgpmQJe72OIA1gwHhBHrZuGKxETlx0fl7rUbgpUHK8jRi56GcWOynMfFdc2SCCkNXDvjSQpT36-fIA-0_Kn6X03QU6AHh39qPzLTYXfHRc_UUk_em12tag8Fgk-rLgU1jTifVAUJXe1uRtlp99zVwOPebd0bj5TfOfQ8xf3AscfpKoLOSsLij-EcHX-AkCKT4pIxIx0RCQncessJzwWaLXFCnsg24QTcOB9mTOJiNQIW_tyvXwC9lNu0z7bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=MB1XGZxYvDT9fY5tAONigYugs2_TPJNVxh4xyE6MC_niOnsErN96nBLk4e0M1aN6e31imki1boJFZLCeVlVsZxlaCWqpvKrO3zcEMecJAcqAZ9XyY_2RxJ8PntPHt6O-Rr29zguAFPjkmW8pPrxXAqPUs-fHIQ9UqUkWu_sQuSy_s393bubzXrbfjBdqFVqSuBFWUWw-QExQP7JEv3oBxJWG1C77KWiT_R1PU4deJZpyY3PxQ3D-uElmFdIYK5cZgyeYOH5ppjJxepn1CI7PvdZNNPmv2oHDIOzfghmIiITW3lsE2ye0JmJPvpMv2Gdd1UcNWytCw5UBJQay-NvwEGYUda4qL78l3xC9kIrVabHBoGSBccos-zWLoFLw0P4Tg6um6g_Nqbjq_M7xHLBfOAaVBfH_ZaU3MK_AP3S8OwpJz9WUgpmQJe72OIA1gwHhBHrZuGKxETlx0fl7rUbgpUHK8jRi56GcWOynMfFdc2SCCkNXDvjSQpT36-fIA-0_Kn6X03QU6AHh39qPzLTYXfHRc_UUk_em12tag8Fgk-rLgU1jTifVAUJXe1uRtlp99zVwOPebd0bj5TfOfQ8xf3AscfpKoLOSsLij-EcHX-AkCKT4pIxIx0RCQncessJzwWaLXFCnsg24QTcOB9mTOJiNQIW_tyvXwC9lNu0z7bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=kIsc53eQBkWrAtu2Sn8a4Kjtjope8DOAuLspb1g-_k8uw-1n0Z23WTqPA-6ZmzF9baAWNS2cQyzLWOcGGBl7hz2zSnPTf_iUBnichNLtNwAd93LcuMAnexusCCiNXjJ5TQBc4kIttCWQhl0Rkktc-ed8ExVU29mB8ZTK7y_4EFdRfQlAIJ6H5KeGz9pMIUCzI9IFp13nF7tPyG1fkcaPZ2vV9-jZZhz7tb8ydVRzG4DqYpJxI7beJLUuPqDIng31mrzFWFjxQXnCX3C1MKYo5m6dSzY-L2wq973fHJQA6jvyRLdur04ucgy6CaQitwO3hDpVPZW1c05_ep-Qwah_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=kIsc53eQBkWrAtu2Sn8a4Kjtjope8DOAuLspb1g-_k8uw-1n0Z23WTqPA-6ZmzF9baAWNS2cQyzLWOcGGBl7hz2zSnPTf_iUBnichNLtNwAd93LcuMAnexusCCiNXjJ5TQBc4kIttCWQhl0Rkktc-ed8ExVU29mB8ZTK7y_4EFdRfQlAIJ6H5KeGz9pMIUCzI9IFp13nF7tPyG1fkcaPZ2vV9-jZZhz7tb8ydVRzG4DqYpJxI7beJLUuPqDIng31mrzFWFjxQXnCX3C1MKYo5m6dSzY-L2wq973fHJQA6jvyRLdur04ucgy6CaQitwO3hDpVPZW1c05_ep-Qwah_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geGVN7FrLHPgLTlWQJP5BVAMt8xxPuuvVMAdWA-MTGbJPZjCSXXnM2R1ycKTOco_l-6tco3gsJ2bz_dI5LDgvwt-jpp_oCp7PjVO7SBCzKe7wTHjskx1KenDpP0Zki5dI0YnhI9fitAP8RkDzBcAB4-S9nFCII5l-HJmYa7HWEL4PhSfsNPD9iCuiZFu3b0d1LIS1jp31659pagyZgbAeHPN8WpAKKo-4UEDrQaJmhm9FMxCwLSwj9fj7McfcM-tD3c1nTRiOKN26NRm27um_rWHWDn2DeouCqsEo8zSsVK8Wnkjl_Y5Sykqk4BFSGG8JUtsUuZmif37PV8pr7ZpHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=coyJOV1ZEYE78SQdm6OU8ksb6-4uv54H221pZCtVcgtcVtqcZEOVBWUVAp7HikZ9ttxi1Pfy62-sr4FmPerRlfSw_LktAeCaPEc2LWl6n3N8GnnZ9B4XsLUj7AVqTnvGSUxqJnCXoGggNpr8xEFH3RIy503ObaDD6YND2UZk9SGJ3E1DsDxopof8IddkBQWQVCRxUblULNf2_Nqb3P1dUTNP97QjG9oOYpAnLwNZuib8OIfP_YQy96cYIkxtvoA2_OgiQ3PQdCGE0tM3nHcPRF5hTFY55Ux5Yu_WRfZFpqUJSY6f8omof_fYwAlHuSRcWQe97mtp5KELiDLDccTcJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=coyJOV1ZEYE78SQdm6OU8ksb6-4uv54H221pZCtVcgtcVtqcZEOVBWUVAp7HikZ9ttxi1Pfy62-sr4FmPerRlfSw_LktAeCaPEc2LWl6n3N8GnnZ9B4XsLUj7AVqTnvGSUxqJnCXoGggNpr8xEFH3RIy503ObaDD6YND2UZk9SGJ3E1DsDxopof8IddkBQWQVCRxUblULNf2_Nqb3P1dUTNP97QjG9oOYpAnLwNZuib8OIfP_YQy96cYIkxtvoA2_OgiQ3PQdCGE0tM3nHcPRF5hTFY55Ux5Yu_WRfZFpqUJSY6f8omof_fYwAlHuSRcWQe97mtp5KELiDLDccTcJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=p40DALREKOWYPoZO0SE2sedjK_Fda0vAO1Y7V8ehwL_WPlYYt7YR8kZ1OCJHdzfJT9qo4WER3mkY7Oyu11lh3MxUHkSHq7xR77X1GxBor3vUWLd8gR81notVLH_qcBpdOL1mcMwfFwWQE32o30LzJ8a6EV7uyBNwBb4ST1pXRs26Ga1lUQHI8HrIg0F2azSsiY9qotCxzT2r7QL5cRxcJYOf0kIOwD8nBFIp9N41h2DyXwECw_a4um4OlS3O5RvFj0SvaSu0O1DLSfFc_zgs1oY-bquw2DojNgD3quRCmxPNxcDrY94gZAzFp5e6ZNros5yUBE7-Ww_DlADVl1At4bduhb-3A4zdBDgcg0b1Nnmew2VSmTTgpBvzsTGaXTviJN74wInSWEQtkuq3U0Mpf6pdr0A54YWoF4URYL6inDm3EabxNuxnM4MNEnKaUMna4CGz95IOGSsg1HiinmUcXcP4C3DboCfn9pPufNBDqCGjVSbaDTCbHo2Q12H7hiG7DT2gjPItxhvbyp5d7tctWulCvR0XHm8XUWPxpD8BkSQN-B0GiXKwhhgyx3iq-wFE2j4pEXFn_rwQ2HdyFGMvTK2-vaU9KeGns0HVeTFw_UZsLxHwPyqNoNm7EWOnRj6Mfcz-VKv3jbHxorxnAj2GD7B37vFfcAJq2VEZj4-xLsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=p40DALREKOWYPoZO0SE2sedjK_Fda0vAO1Y7V8ehwL_WPlYYt7YR8kZ1OCJHdzfJT9qo4WER3mkY7Oyu11lh3MxUHkSHq7xR77X1GxBor3vUWLd8gR81notVLH_qcBpdOL1mcMwfFwWQE32o30LzJ8a6EV7uyBNwBb4ST1pXRs26Ga1lUQHI8HrIg0F2azSsiY9qotCxzT2r7QL5cRxcJYOf0kIOwD8nBFIp9N41h2DyXwECw_a4um4OlS3O5RvFj0SvaSu0O1DLSfFc_zgs1oY-bquw2DojNgD3quRCmxPNxcDrY94gZAzFp5e6ZNros5yUBE7-Ww_DlADVl1At4bduhb-3A4zdBDgcg0b1Nnmew2VSmTTgpBvzsTGaXTviJN74wInSWEQtkuq3U0Mpf6pdr0A54YWoF4URYL6inDm3EabxNuxnM4MNEnKaUMna4CGz95IOGSsg1HiinmUcXcP4C3DboCfn9pPufNBDqCGjVSbaDTCbHo2Q12H7hiG7DT2gjPItxhvbyp5d7tctWulCvR0XHm8XUWPxpD8BkSQN-B0GiXKwhhgyx3iq-wFE2j4pEXFn_rwQ2HdyFGMvTK2-vaU9KeGns0HVeTFw_UZsLxHwPyqNoNm7EWOnRj6Mfcz-VKv3jbHxorxnAj2GD7B37vFfcAJq2VEZj4-xLsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cipQmA_PGouKhRcOY7lDYStvgMvj6SuRyBMjHKQYcpaPAFZpTP9Qm56cyD44AeMNWjoMSLSCHKIV_kVH06Begu_Rla0bHK_K-AAOB9m10CYKi9JxBb_5S1yUdZ8qs-Cbd-_c4rSkjoJfPu-AHcn9_66WedwIXDyKCpR-jfKYwRPaA9PN0BlJzIfJLHxWYlnpBtuscHDauOX0KFQp-UESfLLp1dtizD2K_lyzMbxCIx8Aqv2L7CdDc1W3O66qmoQC_RQbzfPugLauA-MS1riu2g_P_ZVm64sfgMxYbKASTZ2yFw6IFkvr06dcGfk9T2OHJJn6rW7gt83B_Tqo1tSK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Ky9h91wFi6WPZxgCMkDzCB5GI3xoj8tTcmm2PDmPuQ1O8zhds6n9Xakead8w7fCUCR9zJsaPXxS6NJriHXWFd-EhHBZTOolIMsE2yQU4oucs1SKPIWPlnOfvS1k-dkn0wAhwGIRkCoeoEB2H-ht4FqZRSl_aopULkKWCW7lKThB-AMHaq18PGcWvmQGiflsrbSxQAXz8HoRfMpM6M_G8H0aqX-1Z7T7Rfml7jxJ5DzhiTKMcQqzdxkTdBLLYCc4gMqwqgo-pOxSQFk8DGSszMMdhzUyhbns-mmmDbn9T38lCGKQKl9wEGMKkdZOZAz0WBhipLXUpjdpi_AH7QyNXEZLQkvAvo2yW-PeaxzA3zVjQ5UTnaqIuri7LQUkjMepoJKNFBzpWmt3JZWoqx0QJHJSbYIvTI6sBLm0r67gSE_K2HU8iVm1lGW83TUMEdvkxt2NeS8AH0Z8sJkYslvsMvdnpPdRfLyd3BExlEKpFIMpvRf88lbNa_ijteg8wCC9L3AaY2QNzbCRL9s-tLZ0zoPrbfGuPGsdoXHcchluxijm-9ldyCDK1YMzEpNSSzmMKcl-9oLVzSS3ez94Z3pfrQb0ui8dfmniPzu3FaXmZZgS5FhMNDyYBIBJ3wrpwXdQ2_F_T8P9O9Hiki9trJxBwbquZ3q8LqdCsdXFANhJzJCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Ky9h91wFi6WPZxgCMkDzCB5GI3xoj8tTcmm2PDmPuQ1O8zhds6n9Xakead8w7fCUCR9zJsaPXxS6NJriHXWFd-EhHBZTOolIMsE2yQU4oucs1SKPIWPlnOfvS1k-dkn0wAhwGIRkCoeoEB2H-ht4FqZRSl_aopULkKWCW7lKThB-AMHaq18PGcWvmQGiflsrbSxQAXz8HoRfMpM6M_G8H0aqX-1Z7T7Rfml7jxJ5DzhiTKMcQqzdxkTdBLLYCc4gMqwqgo-pOxSQFk8DGSszMMdhzUyhbns-mmmDbn9T38lCGKQKl9wEGMKkdZOZAz0WBhipLXUpjdpi_AH7QyNXEZLQkvAvo2yW-PeaxzA3zVjQ5UTnaqIuri7LQUkjMepoJKNFBzpWmt3JZWoqx0QJHJSbYIvTI6sBLm0r67gSE_K2HU8iVm1lGW83TUMEdvkxt2NeS8AH0Z8sJkYslvsMvdnpPdRfLyd3BExlEKpFIMpvRf88lbNa_ijteg8wCC9L3AaY2QNzbCRL9s-tLZ0zoPrbfGuPGsdoXHcchluxijm-9ldyCDK1YMzEpNSSzmMKcl-9oLVzSS3ez94Z3pfrQb0ui8dfmniPzu3FaXmZZgS5FhMNDyYBIBJ3wrpwXdQ2_F_T8P9O9Hiki9trJxBwbquZ3q8LqdCsdXFANhJzJCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=R1Da1gcZvBST_DaiYPvDWn9BNaxo74yHQtc5WDAWv7RMNj1mRqosRtl8D1Z6upJfLELTGzgBNZgdHMwAeVDpvZV0Hp045gMpK0cKbu_HN6tSbEwd5Kq0x8h8LHxx9_cHre-1i_iNqdnY6y5e1lvUUWj7tm9xSx-la1xDUFic1bjlMBVe2-8gi9VYUFuQKRGymKyAf8gxEMR0KtMeHiHtznzxo4NhefOa2mUEHg1pE6lNayP9ONzKQNrCNew9m1m8MpvtptLbknWFoniFzoS04_9zkQaTd5_Tvghsc2NIqmFJucCgb0PNAO1QYrc_W9Vt04dpw8_9Y_NSIXKBdp4BAoLRYIgsAYB9qHyz-ub_qKDiVqig-olqKqmNKOY9JO33HnTWjmn1Dec7Nlq9RjK86JuxKCeicr9ywYPEZBpLqv-oJn3dFEAzsGbtFydz6Dxukia5A04QfdNS2R7S7lqO3CTFduJug7ioz7Jri03GCyPVqZ7KuKMmOc0c9y92KifKiJzHHhRN_-y5RWQVDkli-6tDIesFFg06mu1wSA1DsKksqeQ2dZeL39xJC2-aqzMdv6fsouZ6TFQg9sT6Z_znMo27b8dxtqY5P3DCGkzGWVZW3oiYE7xjpKIq14eUIEJlqgUUQ5FO_4xvRJpPv0szVoN7smv4EWOMNdbUAIuUDxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=R1Da1gcZvBST_DaiYPvDWn9BNaxo74yHQtc5WDAWv7RMNj1mRqosRtl8D1Z6upJfLELTGzgBNZgdHMwAeVDpvZV0Hp045gMpK0cKbu_HN6tSbEwd5Kq0x8h8LHxx9_cHre-1i_iNqdnY6y5e1lvUUWj7tm9xSx-la1xDUFic1bjlMBVe2-8gi9VYUFuQKRGymKyAf8gxEMR0KtMeHiHtznzxo4NhefOa2mUEHg1pE6lNayP9ONzKQNrCNew9m1m8MpvtptLbknWFoniFzoS04_9zkQaTd5_Tvghsc2NIqmFJucCgb0PNAO1QYrc_W9Vt04dpw8_9Y_NSIXKBdp4BAoLRYIgsAYB9qHyz-ub_qKDiVqig-olqKqmNKOY9JO33HnTWjmn1Dec7Nlq9RjK86JuxKCeicr9ywYPEZBpLqv-oJn3dFEAzsGbtFydz6Dxukia5A04QfdNS2R7S7lqO3CTFduJug7ioz7Jri03GCyPVqZ7KuKMmOc0c9y92KifKiJzHHhRN_-y5RWQVDkli-6tDIesFFg06mu1wSA1DsKksqeQ2dZeL39xJC2-aqzMdv6fsouZ6TFQg9sT6Z_znMo27b8dxtqY5P3DCGkzGWVZW3oiYE7xjpKIq14eUIEJlqgUUQ5FO_4xvRJpPv0szVoN7smv4EWOMNdbUAIuUDxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=QRwXN8GahtJHElEDvq_t3hEURxAizctD-yDdO6-RPNd0W6sJxJORMKEepvA_cO9PFWqY0IKUijuDbdxzGhNGnRq2SvoZOjuUpdq_gsIP-3prWlTKLDv0fy6vib3hHEk3jHt7gUarqvVs8FPbcE9E0hl8GDmVTPA6rZVBQZYT6fr2J2SgxapY0PrKjE0GBNN3HsBPrbc8ODtwerhPtx8RdSFCSzW9JSh9qLUzm4fR4aenc-ek4lZhKLoPnv-B7MvfDqjUQJE_fLr9UAIk0gaR7pJp-34XOd8QuAtMSWHR1fDAXXIGD3zsjhsaayeOtu2Yvs3wjZ2HG9_TCcP7h-sDyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=QRwXN8GahtJHElEDvq_t3hEURxAizctD-yDdO6-RPNd0W6sJxJORMKEepvA_cO9PFWqY0IKUijuDbdxzGhNGnRq2SvoZOjuUpdq_gsIP-3prWlTKLDv0fy6vib3hHEk3jHt7gUarqvVs8FPbcE9E0hl8GDmVTPA6rZVBQZYT6fr2J2SgxapY0PrKjE0GBNN3HsBPrbc8ODtwerhPtx8RdSFCSzW9JSh9qLUzm4fR4aenc-ek4lZhKLoPnv-B7MvfDqjUQJE_fLr9UAIk0gaR7pJp-34XOd8QuAtMSWHR1fDAXXIGD3zsjhsaayeOtu2Yvs3wjZ2HG9_TCcP7h-sDyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=bTZS0J1BBGalfYrEo_D1akorWZhQuryZjZgKI-gXVlPzTD-UZrCPy6fsonzSazSIcBQnwIlnsH8kK_uTGgTFvu4sZ1gDVdKpLLAfvRoLMm4UqJmtKBEULR0X3o0PvIUJIHB884YxLV6DL7K5fclnug2d2d25C9hO9IgP7LSe6LLaVxu6eXg3q5uXV8kHu0RCHpFJ1bA-zHjgE-DDHR1eobUegA2lwDV-ZEPs-2MF7jiVvjnWW2ymH0Om1XGIsa55NxEkA9m3uFcphrFXGmUm-cDbTGBqlvKCI-vV5sqrKsuQNXV_KNfdc-t9sC1-BdF1u-Iifi6VqQhjmYPgIoW6qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=bTZS0J1BBGalfYrEo_D1akorWZhQuryZjZgKI-gXVlPzTD-UZrCPy6fsonzSazSIcBQnwIlnsH8kK_uTGgTFvu4sZ1gDVdKpLLAfvRoLMm4UqJmtKBEULR0X3o0PvIUJIHB884YxLV6DL7K5fclnug2d2d25C9hO9IgP7LSe6LLaVxu6eXg3q5uXV8kHu0RCHpFJ1bA-zHjgE-DDHR1eobUegA2lwDV-ZEPs-2MF7jiVvjnWW2ymH0Om1XGIsa55NxEkA9m3uFcphrFXGmUm-cDbTGBqlvKCI-vV5sqrKsuQNXV_KNfdc-t9sC1-BdF1u-Iifi6VqQhjmYPgIoW6qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=PBTlcyQ1ndaW9pDbR--Y49KwDjF8Ntmgy3hfeWpJTV1cGpFlX7TME0exKDeWShMZW29CnJTh7jJOFMiT_5aiKinUglYP6ivHLBMU40VxHG1XgHwIjNkrlkLa0Lnz129wj9HRonOyzRueaBJ4wG4MgbqtYdBJUPYM6jcxbSknc1hn5R4dUdGvrJPAMfg10BnZOKFt2SDosCpdaqpVljBaYsQOHHJx8tGEwnmJ7LvyOCfRi8vNOYyaRrHsYp61il8O5YRbCgjXhdfUFTMiVX0AmypkD3KdeEb7kOSOLeEumZisHVEAEjPg1R7xJpevFTFF2VNUJv5eEP5lstoZbIU3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=PBTlcyQ1ndaW9pDbR--Y49KwDjF8Ntmgy3hfeWpJTV1cGpFlX7TME0exKDeWShMZW29CnJTh7jJOFMiT_5aiKinUglYP6ivHLBMU40VxHG1XgHwIjNkrlkLa0Lnz129wj9HRonOyzRueaBJ4wG4MgbqtYdBJUPYM6jcxbSknc1hn5R4dUdGvrJPAMfg10BnZOKFt2SDosCpdaqpVljBaYsQOHHJx8tGEwnmJ7LvyOCfRi8vNOYyaRrHsYp61il8O5YRbCgjXhdfUFTMiVX0AmypkD3KdeEb7kOSOLeEumZisHVEAEjPg1R7xJpevFTFF2VNUJv5eEP5lstoZbIU3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WaNmQPkaVIYXVvtklUXZG4idnYijraiToPSHoz_u4rWUeAkLpVid4o-QrDungFCCzusQVwQG7Fy9AETWqPcW-mSVgbLwqaLTsO-QnTm8Hq9veMcTgPxY2UE6A9jQL0e1HMWgEkX9qKC57U4aMQTLg6_uabas-1vyBtzWSqNqIYFeC0o3kq_azvmD86cnqtEJawpXC5-Cn7cZOtR2LEQE2er2Wft2dXszuaQdulE6_ZTyngvrJSaTAL9IRRrhBFeejqVOaGzA_ZYiaKVTfzW7r0YoyyM905zJq022YIKAo_D_iGZ_9dH4tjADgY5DKkJijf2SANEDvPMTzLJg4sPOpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WaNmQPkaVIYXVvtklUXZG4idnYijraiToPSHoz_u4rWUeAkLpVid4o-QrDungFCCzusQVwQG7Fy9AETWqPcW-mSVgbLwqaLTsO-QnTm8Hq9veMcTgPxY2UE6A9jQL0e1HMWgEkX9qKC57U4aMQTLg6_uabas-1vyBtzWSqNqIYFeC0o3kq_azvmD86cnqtEJawpXC5-Cn7cZOtR2LEQE2er2Wft2dXszuaQdulE6_ZTyngvrJSaTAL9IRRrhBFeejqVOaGzA_ZYiaKVTfzW7r0YoyyM905zJq022YIKAo_D_iGZ_9dH4tjADgY5DKkJijf2SANEDvPMTzLJg4sPOpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=rWxvM-f2wNgiEViVE7qLlbiLSrB51NCrInluRwc5rL3yHOH1ZwtoDvz0hWUS-duGs849ovXiaf3v6jwAaXbSjSlRlg6aTfoyDLJSkrZhTgAQ4GP3KaZioCIOpu1WF_14PjNFQn5xiSmCr2xc_JZJHejUiS-qx1_6ImzPpZI4SCecBkJIWYeUS-jp4vIMNyJr1Vzhz5G3mv2Mu-QjI_COWgqGITApvb-b9VpUikC--GDz9F_8gqEZ2uMhc1xV0HxqwMn1-tsO3qj_Yg1uFkgoMsLWCtXr3OvK7qSEWQjeOs66YhRmx3jzn1iVNCAOtU6BNBLlwNSqjuxSkifVo7cklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=rWxvM-f2wNgiEViVE7qLlbiLSrB51NCrInluRwc5rL3yHOH1ZwtoDvz0hWUS-duGs849ovXiaf3v6jwAaXbSjSlRlg6aTfoyDLJSkrZhTgAQ4GP3KaZioCIOpu1WF_14PjNFQn5xiSmCr2xc_JZJHejUiS-qx1_6ImzPpZI4SCecBkJIWYeUS-jp4vIMNyJr1Vzhz5G3mv2Mu-QjI_COWgqGITApvb-b9VpUikC--GDz9F_8gqEZ2uMhc1xV0HxqwMn1-tsO3qj_Yg1uFkgoMsLWCtXr3OvK7qSEWQjeOs66YhRmx3jzn1iVNCAOtU6BNBLlwNSqjuxSkifVo7cklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Ki-vtGb00s_FwCAGXqY1dMpmwhZ3cbCsvnL9juhN5ghT-aMxg-_DB9ehe4HIT0lNFghScRJBYiujxqQRmpXvlAmylQ9Oqz_JSLbU3RX10lVCZ-dPKUdl2eLs7GE9_ttA7T5oWxyd9V6eqWKVKi6-DQX4hw_BkDZ4a9n99lX-4JhYBXg33z03EOh4OjHm3v6KjRwXTjWH3wOhhQqYLCreM4x7TE_2HWOA6AXqk2G9INIrbOwDEkufuUXk2FARgqPFCm8n7XnwCGs7qc64g5Rv67usEQHdpBDZMj8F1mEmp-dErjDxyfKmPWIl537UmF2Mai53oM3lfQFy5ayOm4HtUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Ki-vtGb00s_FwCAGXqY1dMpmwhZ3cbCsvnL9juhN5ghT-aMxg-_DB9ehe4HIT0lNFghScRJBYiujxqQRmpXvlAmylQ9Oqz_JSLbU3RX10lVCZ-dPKUdl2eLs7GE9_ttA7T5oWxyd9V6eqWKVKi6-DQX4hw_BkDZ4a9n99lX-4JhYBXg33z03EOh4OjHm3v6KjRwXTjWH3wOhhQqYLCreM4x7TE_2HWOA6AXqk2G9INIrbOwDEkufuUXk2FARgqPFCm8n7XnwCGs7qc64g5Rv67usEQHdpBDZMj8F1mEmp-dErjDxyfKmPWIl537UmF2Mai53oM3lfQFy5ayOm4HtUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=oz0GCYk0JqZYMt9gSZQpAW0tPe8DZvcFrbeQhLrMRV5GH62mp--xS3C2AbqyTPWVXmDIWTWD-EWD7d0mYcQ_HZZmvi8ZT405F0jUlL0ZbpYR3tF7AWzgyV4MfPkMhaUDdH0fd8ImhUU6F3NsjLztCQZta5IuSbGkgdWLKDxb4j0DJlNNXrNjkdBjZdMfH5IKACklBtf7tQdUGxBTtQLnRgofhp2e-hF_fR2FTYuFQmmca8JZl062norkvYYqjkyBMfg4ZMz5JU1BRINL9yebMHwjEquelRvAQDi6G_gEi0MYgW2gWuBquOoW94ejBYUQXrLzUb4DDWQCAVSEirLWNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=oz0GCYk0JqZYMt9gSZQpAW0tPe8DZvcFrbeQhLrMRV5GH62mp--xS3C2AbqyTPWVXmDIWTWD-EWD7d0mYcQ_HZZmvi8ZT405F0jUlL0ZbpYR3tF7AWzgyV4MfPkMhaUDdH0fd8ImhUU6F3NsjLztCQZta5IuSbGkgdWLKDxb4j0DJlNNXrNjkdBjZdMfH5IKACklBtf7tQdUGxBTtQLnRgofhp2e-hF_fR2FTYuFQmmca8JZl062norkvYYqjkyBMfg4ZMz5JU1BRINL9yebMHwjEquelRvAQDi6G_gEi0MYgW2gWuBquOoW94ejBYUQXrLzUb4DDWQCAVSEirLWNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjNLDjpnUCJSBKbXocitHgXPM6eZ5OjDpIq-62_fbBotbdUPZAXRqSAEEA4KGPWmrikOTSidc7XUCzuQE7-dVi4fSxBl7soWjNsEF8TTzca3V_qthJ_R1PwXfbM-xVvGdTVUaQMmGEgUbI6NmyaSzKgxAcAVyM_iAWeyRn75fQQw5v9tAJKu1lcORHUe4Xim0sZgJYfRoJMz80P6f2kROB5LMYyJ3sGMtZxGk0L32QNzqrUOZwf3s6C7vC9chMyEd98uew0SimfUf_aX-UiCLakKfhlS2T12wVfY4r_U_YjBx2N9Hg02ImiBbN2sqw0G9hBOUaFFcfXq59pU53TiEQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=BBTXbtMw1vs5WHtLLjDVCoiaOla3m4OMPWbXPZ9ULCzXhM3dFehYwafJ2-VC7dtWfxFunGHY2Hf6ZfSR-ECbm4CmgIk6O59HifGCoB4OjFwuPKRMm2-dSdWyKKlNqWv2s494u-2cVe8m12bMhwo0mIYEoBMSqW_hNO0vLSna0yfmo9a8q7IP0XUkeqCpb6L_BkpT2ZxQ-7u7yldkSOFsmZRXb40rk63TRqXAard0QJFTThOWRSTGxxG3Met22K8n5_3slJCwpWjfjkUMqfVndaj0p2gJe8PQucFA8k0QWub6wXYqcrDLzQkSD-v5Nt972WAEtjoyO80BSf7h6VkL9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=BBTXbtMw1vs5WHtLLjDVCoiaOla3m4OMPWbXPZ9ULCzXhM3dFehYwafJ2-VC7dtWfxFunGHY2Hf6ZfSR-ECbm4CmgIk6O59HifGCoB4OjFwuPKRMm2-dSdWyKKlNqWv2s494u-2cVe8m12bMhwo0mIYEoBMSqW_hNO0vLSna0yfmo9a8q7IP0XUkeqCpb6L_BkpT2ZxQ-7u7yldkSOFsmZRXb40rk63TRqXAard0QJFTThOWRSTGxxG3Met22K8n5_3slJCwpWjfjkUMqfVndaj0p2gJe8PQucFA8k0QWub6wXYqcrDLzQkSD-v5Nt972WAEtjoyO80BSf7h6VkL9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=O7RweNwa3gOWXh-LE5czzAdcx1fZpRGy4xVAW2JKWM099zMjEdPiDVCQ0swDt6XggKXC7ztiucViYoYJJSgjt7zfCMsPVD1oTfa225hju8ymf5DtyL9yRbpeFcFWA1NwxYYMbT61acAaHvP_rd7awBQEKCWfWl-lhQ9KcEtshzexUo6dKL5AsYTVCNp7kilG-qDCNmbLaYUq0dNXOwruCwwDXTEdI8AcCsWqNgOS0BRss_VKRx2oMfz2Z5s7lFBlUcbwovlTWV6JEiZBxOQN45hLk98W7hjPVBARtybBA_oCoxJDPHEsRe4JZnWNT_aJVS1n88L5HqTUbIWp7BX0yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=O7RweNwa3gOWXh-LE5czzAdcx1fZpRGy4xVAW2JKWM099zMjEdPiDVCQ0swDt6XggKXC7ztiucViYoYJJSgjt7zfCMsPVD1oTfa225hju8ymf5DtyL9yRbpeFcFWA1NwxYYMbT61acAaHvP_rd7awBQEKCWfWl-lhQ9KcEtshzexUo6dKL5AsYTVCNp7kilG-qDCNmbLaYUq0dNXOwruCwwDXTEdI8AcCsWqNgOS0BRss_VKRx2oMfz2Z5s7lFBlUcbwovlTWV6JEiZBxOQN45hLk98W7hjPVBARtybBA_oCoxJDPHEsRe4JZnWNT_aJVS1n88L5HqTUbIWp7BX0yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Q9PTz8e1VJJG7mdPGjxFySMbkh4-3sB1C2SE4ONUmGQbSwDUSBB79N88AMYLVJGhqCPGpT4XrFxlAXmd8B4LuDrp8z87hb6mUIYXjmjKNVmtTmSs8hsaQ9kLFA51MWpSjUrIwJcfMXeHs-BhS_N5KSXkdYzEu8ROMXFed-_nnxTdJRFUFcRNWHz8gNH_M1pfJt2BpYR5gW7e0dcymiBgf8nCZTEClpVaNBpS9GU0AHQapIxVIuKHmwVOJBXdKjH5DdnaUwqQVCgafW92mgbeRy1t3sSPuffiCvXQLU1qzgpKrTr0-WZkuzw6cM6bNXM2winlBJ5zpkk9Ma-PNCzLag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Q9PTz8e1VJJG7mdPGjxFySMbkh4-3sB1C2SE4ONUmGQbSwDUSBB79N88AMYLVJGhqCPGpT4XrFxlAXmd8B4LuDrp8z87hb6mUIYXjmjKNVmtTmSs8hsaQ9kLFA51MWpSjUrIwJcfMXeHs-BhS_N5KSXkdYzEu8ROMXFed-_nnxTdJRFUFcRNWHz8gNH_M1pfJt2BpYR5gW7e0dcymiBgf8nCZTEClpVaNBpS9GU0AHQapIxVIuKHmwVOJBXdKjH5DdnaUwqQVCgafW92mgbeRy1t3sSPuffiCvXQLU1qzgpKrTr0-WZkuzw6cM6bNXM2winlBJ5zpkk9Ma-PNCzLag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=mQbbwOWBFAtrM3LpHbak6Ae_E-K6ef3HwukroBNa0srFWAyTsTmRFzOgWQDgF2Ivz6EMhAqpvm6aX16KvJsJoOTm8ZhkNckpPv0JNIXGfQWXcsi6gxO8QXsORELDgkyr7GkUgda5AqlNSa9BcGLUZp-ZeQ-9vNn9X76QEpoueOnpGeqEVyw4HRAsiFcubSyjTdwJ0T1c3ZhoMTwrPfgZxRtGhg_DkDg5MQUz91KFMTZDjNgZM42tEoX0XsWq8qcp00DFUBuo0VXlhBTPVZmuoJZE5-EfBv4G75D0aoMfNjOicL3AH1bkvVMODGslvQUno7iOZt80asJi2Vo3BSrofw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=mQbbwOWBFAtrM3LpHbak6Ae_E-K6ef3HwukroBNa0srFWAyTsTmRFzOgWQDgF2Ivz6EMhAqpvm6aX16KvJsJoOTm8ZhkNckpPv0JNIXGfQWXcsi6gxO8QXsORELDgkyr7GkUgda5AqlNSa9BcGLUZp-ZeQ-9vNn9X76QEpoueOnpGeqEVyw4HRAsiFcubSyjTdwJ0T1c3ZhoMTwrPfgZxRtGhg_DkDg5MQUz91KFMTZDjNgZM42tEoX0XsWq8qcp00DFUBuo0VXlhBTPVZmuoJZE5-EfBv4G75D0aoMfNjOicL3AH1bkvVMODGslvQUno7iOZt80asJi2Vo3BSrofw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYTqgK1ZJLhTYMTZBLSlkBjV5uAVhWRtDXK8OFjnus27xDLn8AIlHuT54HeQoPxSSIgKKRuFt1WnQvIoI_tG-CLDeLveQOlt7HxnK20v1cIBqpHxuCdVUJTA3gAk6VPo7Jh9iACzyHlHe3sD-7AmW6NRF7wGcFwqwpqKRnZcxjNg1GFjU2ohi52npdLC-t8m_q5bVE1WOkV00heW1oHJ-iow6lOIRwuPodtpmxK5Dby2jshQ_JFLYZrPcv4pLQpDArtPdlvAflMBW33VGL3RBX5xCnQGgn3oVfAnqPFgLnr5Vszv-3yEkcesmmFwkofjeCg25ZlcCDmvGJ9s0gFdgg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=JqmnUFOT7Yp8SsvnjkOZ1-hAT5-_epYoyCfQUeHzeuzkCulJcVNw5jwA0uWYvhroPPyIhfztaqFVJ3C1fMswqg_NvQNg7u6RGMXjbcW_1S1VjAjBU4EdZyMnXyI5U5vXpi0U54-YfEJ2h5EX5WMqGP54VcByoviVE_7vWWzMm-mFFG4NfVDPB5JtF8--ckdJRkR1NVzvBUlFbYqdE2QYs211uzUwfyMkUIKrol6HCG1HFMYwJ3Hxk-W9N5aQ8G6i1y0JxfaKutrTDly8tj_a2XJBUJRkfATPCRppnZ3gc5QdyUw-4NNXHGaW1LJvOf1ndU9cg9aVfGEfVdM9N7LZ-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=JqmnUFOT7Yp8SsvnjkOZ1-hAT5-_epYoyCfQUeHzeuzkCulJcVNw5jwA0uWYvhroPPyIhfztaqFVJ3C1fMswqg_NvQNg7u6RGMXjbcW_1S1VjAjBU4EdZyMnXyI5U5vXpi0U54-YfEJ2h5EX5WMqGP54VcByoviVE_7vWWzMm-mFFG4NfVDPB5JtF8--ckdJRkR1NVzvBUlFbYqdE2QYs211uzUwfyMkUIKrol6HCG1HFMYwJ3Hxk-W9N5aQ8G6i1y0JxfaKutrTDly8tj_a2XJBUJRkfATPCRppnZ3gc5QdyUw-4NNXHGaW1LJvOf1ndU9cg9aVfGEfVdM9N7LZ-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=smOt2VPbUp04rZM_vvF8U7G0dBTmKBqhy2JHshxsrkglEcZR2lLLPhB5sCoUKMJrdV_ElmUZj-fuWz3Gj975OoEUo51OYi5GgRtf1tvsflNMiKrAJ0lOX9Y2cERDCaQDiffueaoBNIrBtsmuEcj3xca5bF6agvZuYWU7JkX_wmB0_fJlH_DEdNQyLO-t_MLiJWiODRYtMSjsrRddjWs3ljN7cCmyZWjBRsxabKPWZmnAQ0BwMOjF6hRdLk1KP4SXoYcwdBLwiCIWqGArVxgHa4BcuLYA0mahkyo5jA7SIIqWcx_A9bkGF8W1PrkCj_0AHdWoJOIINUHjh5THZuT0-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=smOt2VPbUp04rZM_vvF8U7G0dBTmKBqhy2JHshxsrkglEcZR2lLLPhB5sCoUKMJrdV_ElmUZj-fuWz3Gj975OoEUo51OYi5GgRtf1tvsflNMiKrAJ0lOX9Y2cERDCaQDiffueaoBNIrBtsmuEcj3xca5bF6agvZuYWU7JkX_wmB0_fJlH_DEdNQyLO-t_MLiJWiODRYtMSjsrRddjWs3ljN7cCmyZWjBRsxabKPWZmnAQ0BwMOjF6hRdLk1KP4SXoYcwdBLwiCIWqGArVxgHa4BcuLYA0mahkyo5jA7SIIqWcx_A9bkGF8W1PrkCj_0AHdWoJOIINUHjh5THZuT0-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDPwneO9p_GfkacOJ_BQ-AreJjAHCP0ObNevbPpTQnD9YuX_u8AE_9V1H6x0OhzKrd5gcKx4Ztkn2qo7eO-8gqqOEo1vMw9yZOCFTUrdRgHQg_eoJM44DiNVACIZQAmGxbpCPvzOKKLQFUgBA6wCdFeOxtFBrk6bzpciFsmYrxFPpcxX_Idxxz3Zm5HuVqT83RMQzaXPGyBojr3asrSyA0pzCGOz6O-MFEvTWYfBEoWjFHMoBPs6ERQOIjMXGxqFAZ92NKgiNviyRp1rYtIG5BZy8o1JDV8v522ClRF0CUFMuFJHrgkto8lG-aDCt3VgqPgd4JhUxSFlHjExEowCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsTlRzROOvst0EHuSmVFmZe0FTJ8vMB5QjNoItL6vvYwJ3TbxgClKHiLCuo4bKdFRLczJjoP2DwsoR2u449CYqCNuQtiziMeBO9jiU_t6Uh1CoaZfEF-HXlZxkbDsSP-ZLL52GCNttxM6n_u6d5kMqLwEFuvD1B7gBJZq207SUJhCToTyumiH_cMjRc4L2s17FilgRXS4UwIRu5k8OdpuYaQfviiQFCHZrE20oYVJP9ZsWU1PPjQ6rYIvkbi8s8O96L0qjbdLJgdssx5_6w2sF8FYCoXmXxC_kfLpDtTIHIsSMk8MPUBnclKGsMjWDltxKtF9KowkwOWuAQ14E9xRA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=G81nQ34629FM-RkgRhYJRrVONP4iCZivDVHQmX3ZNJ7IIY5-sHg8Xgu5MGPQJFd0JBwqFex8fwJitmC68SJE1gH-lJN2JuGTlOHDPCKigXYzW_MkPYQnLGDC1Phffp2cmJ2F62L5IYTpzgw8Fcvc8-4ZlXK6sAQN4tYLmxYZzYhCh0RL6tCKQYmr_TSDZy8Ds0YD-G0a9TK7ozehlgjSOlIiouRfhPxzeCh49gAzdIv_9i_pJ1rs6AgzKHnlkiPkaSJ0orltqFz0I4fFIQG714UmWJYGeHvbo1L1_tALQZXxuJ4CD1nVOkaTHRhUweokfGFpxhjRz-CZvAvUqquvTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=G81nQ34629FM-RkgRhYJRrVONP4iCZivDVHQmX3ZNJ7IIY5-sHg8Xgu5MGPQJFd0JBwqFex8fwJitmC68SJE1gH-lJN2JuGTlOHDPCKigXYzW_MkPYQnLGDC1Phffp2cmJ2F62L5IYTpzgw8Fcvc8-4ZlXK6sAQN4tYLmxYZzYhCh0RL6tCKQYmr_TSDZy8Ds0YD-G0a9TK7ozehlgjSOlIiouRfhPxzeCh49gAzdIv_9i_pJ1rs6AgzKHnlkiPkaSJ0orltqFz0I4fFIQG714UmWJYGeHvbo1L1_tALQZXxuJ4CD1nVOkaTHRhUweokfGFpxhjRz-CZvAvUqquvTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDJ4MNmEZsQmbL1wszFqE3xeGcecmjh-s8Yuph_8gye2srljz4Ws9vJiMU6QmuE2DV4okS6Qq6hH-P9NX4J5_f0-Ot7VTRnRuCf6NdrMY7CJtXAUvdTH2_Ss0f-vbK16VwweDy19ciOlchAw1gYrHV7n1sw-JSDh6qHExqeTt7uRUJKz37CCRB1vaqKRIdmNO6f-jZSQK3T1WDJHxGBf8oHTkJgj1UNsP_ag92eylBiTs1vxGMqHY60ZZFRS8AYXHgO7kdFiYJR-b3YuT_QU8kYHWQ-fb7o9HoSvO-iU9GuZrprBZiLInK1Ry8iqAp0gjyfxm12_PIuQg3EsxDTDgg.jpg" alt="photo" loading="lazy"/></div>
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
