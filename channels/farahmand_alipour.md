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
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUO-pUzMaQhyGvsVujnLlAHmpDkhsvFrTaqCh9DkmnmCsAbGyGLq9DL595ItFJIDJw1pR4MvB4KjA3Zt7HQkRySbIPNN-aeZeQOORmOxAS9jkXu93J1insljMEZEattNJ4q3QZ8rrEUb2mIyz0giVklh5mSr9cKaDRhPpLnA3n0PrVZn4e432GNZdNFWesui_QI1ZCtWRTqMI8S7UOIZostbjSesRTEyEDW9EMBQzbZOvhQ8r1STTy_WuNWQh3bHZFPXJxr8djWMMYz4jjXOLal6rZXOr-E6SsM-RtlDxx0JsMMV-UHz3qOParzNOvAx8gaqz0MRrgCUERr3qj870A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFs-dYQ89SSejfvnyaPCtYViyeH5hORS_Wjy-HF7Xq8oiRkMX3iZa6PwitdwNXfCcWg90OVoAC3R5kmmMc7jj6woNEuDFvGKFYxYjv_Fsk47kBE4fFcXWPKfeOyFFVZHDIs7s58tU_KHDS_B8jbV3J6b1B3vAx9OMUMQDHIdOHKKsa5Bi8Di9JRZ0ZVpircgcnsbdBupPnnxeEKF_u-wj7ZvZHBD4-aA3RlyGWFu542kPseaBXgADPOZ-YWJ_WwNNudxKJzXX5wgUrUgHR6UORBdJJdpdY61GgxFVsCR2d1NDowUniyn8EWUll3zVDIX5FkaMAAwiY6dG6vseKwl8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRiUefXScZRjoEq0LOOP7HUIDj3ExM0zJnfdZ5LhF9HgPOW30-uN_Gzvde2yAl1zkvUG9dRoM5j_1HT-Y81QeAhA4bTfWAnKzJybHg7xFMBwTlRA-jfF4Btx_2OehD6nrZsJ1CSpoEqCVQHoNr68oTjObLkfbUbjLnjLcv6wRnL4PMkcvLIRRnk5HyrFT7MgO6dGc8pmn4Tz52gt7lSknJVCGKU5gh88k8mbELeioQdQf6t8OzeP2P_F3FxEp1Wz8JHFmgxfra5dVS96F0VFaJmQ-A2TY3sJEFjP0zmJhzCR4QvrB1a-qxRrS86E98cTe1puhgtDZMjzmK2nxB3beg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcUM3D98taNvziPQlmmlbVQgLXxF4b92wpqMxcBLA0i9Ff955zPZ3DcNYP36laNhJTXL9JObCpManPI8H1sdx6mORxE4yv-PaS1YamIp8UFfwExDuRY3rmoLYCNKh0RIIejFCxCltdna5nFBSYAe1evarveHkzk-fcBuzI2i28a9yDIuzoZuu9bJSFNuwJXOGXxcmvifPse9yc6Vqx7aYvjhIZ_rhyj30TzXHq4WbfIiKnv6_yZPVBVj7vQm02dD46bwNvwDnG9EMGnybS1ia1MBJEhPGYbN_449NGWi-UtinHSVaCl65aaHwvDh_Zw0lkv5zPiTSh_dQsj7a8mPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RumLJpIExNiC0sSMWV8LNRK7zLAXS4gL9Shs9Jw1Y-IDfX3ecxmVOi5XeQGA53fsmE7_23wBXKbg4AaQKTgKgBBIdX77plNpXHQoBRHUbIdoxbt9fMuQF6JIQIUgigoeEU2aRgtx7IWMabN5kDz-NvqLIO5ffHdf7WeCdv5m7r5gy3EbzHhcI5m4e77EWkp092hSxXm9zluX5e9OfL3Wnwl6CIGrP1StEQqEMwO29_KdTxopF6zZJ5-DPeSwdDAP_0sfrvxP_0VRm147RfEStnnt8MG9PsfTNKfeP7kyNV4invYSZTazOQjUmWlet6oHQXxEmOGucnLeKoUDtsvGpw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Ab-oqT37WbVNoDAWNYsiw3d3UsYuD5RBeU9Yon6Ny5PyzmThyah2fK5U4XIW4q2uPDsPremfNX23OddYi225koh0blaS-wtWgNjGgxRzX3KUICP3NQVJyQTZ5mlSy0a3FR9AEFf5OMrHSB4JDTCehpju78cbEgUvk4qWcLZcScfailJQwmDVbxEVmDDTlB8Gj0lSwcpFkGqASiEC2VOp37vXDA6X9KKsIJmdgdm0V23rsgFaKLsBVNi160BIupefvWrfGSpzE_y4GSoSIbKx6aO_xvBmN-np0_baruA3iOgyVyWZwaI_n8O4csr_EsFKAcCJ5ylTs18WNf0ho8_GWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Ab-oqT37WbVNoDAWNYsiw3d3UsYuD5RBeU9Yon6Ny5PyzmThyah2fK5U4XIW4q2uPDsPremfNX23OddYi225koh0blaS-wtWgNjGgxRzX3KUICP3NQVJyQTZ5mlSy0a3FR9AEFf5OMrHSB4JDTCehpju78cbEgUvk4qWcLZcScfailJQwmDVbxEVmDDTlB8Gj0lSwcpFkGqASiEC2VOp37vXDA6X9KKsIJmdgdm0V23rsgFaKLsBVNi160BIupefvWrfGSpzE_y4GSoSIbKx6aO_xvBmN-np0_baruA3iOgyVyWZwaI_n8O4csr_EsFKAcCJ5ylTs18WNf0ho8_GWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=L-gFBmzElAspQy9NSqEk5mIY8Vt0FmB5XkOQTajX9of7RdybWEUupMjTAgLWxfQP_snyrdPU8jdsCwsMwVGLBuJFrNvJgfQnKQhCIWqjEYp6oAnIgSSnNH3rFkAgGDqZzJaNnexEaNZgMH2dzYPndjma-7yRdzM9oZm20ujZo-HQbc7o8yGSMian42LSVYmUhJS6CgJfGDTG32HM1dddOXnULFi8idF95-Ax_axt4u3tz4O3WYfAKm2cIeiwQhiaWzqBit56CBaYet80Lq31uGPNTGRjy0imY_haGOA-6c9DXhCghA5d4489j-O3hQCrG04jF9HwD-eYUjygTlWJky_fpbLV_sNKZqSDvU5jYhce0sEUeqzbqKVB3LHaIu49M_zYGaWLm_L3uGjrvkRiOVjIsZjE4WFPHDBvKMpGhEymnBVNDP5FUEfaMbL0XCasrMjFss3wGBWDFmETMTj4r_Bqizdwz1TBSE77omDMZCO3lJ9ynyXeHGBN34ZuLlGII5ZMjEIq0SNiBij-t05suSAhN9C26rlLZZfqF-qCylP18wDYpKE5zd9iQ0y0WNr_e1gQR_FXcwnY3WL5hbe_jlyJpcTveu2U3yJktu6pY4--rLoZlJXsXQYS3qR5DJm__02PjX6uoh4kEDvBAusVy1qpCyvSkXkgrupXT3Oc1lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=L-gFBmzElAspQy9NSqEk5mIY8Vt0FmB5XkOQTajX9of7RdybWEUupMjTAgLWxfQP_snyrdPU8jdsCwsMwVGLBuJFrNvJgfQnKQhCIWqjEYp6oAnIgSSnNH3rFkAgGDqZzJaNnexEaNZgMH2dzYPndjma-7yRdzM9oZm20ujZo-HQbc7o8yGSMian42LSVYmUhJS6CgJfGDTG32HM1dddOXnULFi8idF95-Ax_axt4u3tz4O3WYfAKm2cIeiwQhiaWzqBit56CBaYet80Lq31uGPNTGRjy0imY_haGOA-6c9DXhCghA5d4489j-O3hQCrG04jF9HwD-eYUjygTlWJky_fpbLV_sNKZqSDvU5jYhce0sEUeqzbqKVB3LHaIu49M_zYGaWLm_L3uGjrvkRiOVjIsZjE4WFPHDBvKMpGhEymnBVNDP5FUEfaMbL0XCasrMjFss3wGBWDFmETMTj4r_Bqizdwz1TBSE77omDMZCO3lJ9ynyXeHGBN34ZuLlGII5ZMjEIq0SNiBij-t05suSAhN9C26rlLZZfqF-qCylP18wDYpKE5zd9iQ0y0WNr_e1gQR_FXcwnY3WL5hbe_jlyJpcTveu2U3yJktu6pY4--rLoZlJXsXQYS3qR5DJm__02PjX6uoh4kEDvBAusVy1qpCyvSkXkgrupXT3Oc1lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2eewIZdvS020DCzvTGyYWpl9TDBET80cpPEuC3hbmeYxzXBplEDUC-xZfQ489mpBFb-2Rn8ItxRgWYqSZUvCnFueYeQGGCaMdwJ-Hi9J2gyb3PmtZiv0-iaLz8_0QQQ9I8tAuJ-4yN_P0fpI9V9DZV_TMAXbsBs9wUjRpLGWK_cX_XTYvt0eqgyaCvYR0N2NfmDyHr8nwLeXtjby68jqLaRqJUL9Ve8YPEx3DAwsci_bhm56zrhqYudNkvq-nzmHI2I-M9-kBAvNmO4jyvvjXP3S7GqVhMYrkcWIxWopvoxMQJoATxfR6_Vw5OQl4OBfFf5cQgaqtu5rm_bHZPVIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIgbTwMknaDUcEEFkUS18CG_vF7EXnTomZoMQjjfFsKEdCtzSgXcKQge69LXW-xqzZvwN5v6uUEmlzNRQ6HefPD1YCCNiUpEd87jL3uN9ru4Tsw7TSgFafaoPC7IjysqadDfLXh1xZpOUoMdjubsNfAwXhGl95mRAWbtTb8RDnIe7OByOWbYL7qk1_iZbt1gW-4Mb5HF9mufJQSKBQBUlQR6NF3XvB5tlHoZclNEv02XvQ1AL5yfirZgtokvb_V9SJ9mqQynHSmdaBBXPlV6AWeNL6o84zYxmaIPpAKes5_sAtzSPagjN_yowhZaXIjrAb35XUK4NWYU5TzzZBEbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShiAuydVTA_SV9cyoPNM8e0RbYRYek03SxO31eUF4v73C9Meh45Qj4RY4bBFL7qXMAzosj-aTpVHC_38kC1fkXu_HyWsgqvQSNCZ6N4iVRUjGYNkJgUAiNWehAFnUO_NJ8_di2j1J1kaw7u-jCFeeRw0zSH8miJuahrwKg3esJvW2DuDB_TPMlpTS7KqArxfNe1CGsPdGBQOu27cMWur7-HfrywRKln30O826IhXCo8SYqBxzSog2znS3EzJdl5fMfcw7N6T9cjZvT0UmONbQtaQ9Opmp3GliBhu6IIhOW302idsO7T7jHwsPKwegrnWuRvKsUQzPc51v1EXdtdOpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=S4WM67eABeSJeTuMsnariqAW2RtQKTTaUW0KaduC4hdAAhf2rx8Bp4cKcCeeTiz7nQZzDUruGlKsc65A4PdwBaNwwlUf0EwgiFH4x2idcNJLIFBVSU22Ziywxq5rG5QVf9vzZFA1wbf_w9Jvs_x31Pip-n40lXeEV13Kv10YeEBM6u4Sdo-AEakocNRrUFVjpMBN7Mb4VchLUHwpmIQdNSWHuu4JWLK3iX-4xktKqA3RnpTkJvxnQ-sRTSB24DSFtsYdBpgX-k2084xy1hVujnjraOHYx2LnmZbdxMjdGOPh-bvJG61HwvrzkbaYIc00SpWVUQSl9MVICQBntg3HHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=S4WM67eABeSJeTuMsnariqAW2RtQKTTaUW0KaduC4hdAAhf2rx8Bp4cKcCeeTiz7nQZzDUruGlKsc65A4PdwBaNwwlUf0EwgiFH4x2idcNJLIFBVSU22Ziywxq5rG5QVf9vzZFA1wbf_w9Jvs_x31Pip-n40lXeEV13Kv10YeEBM6u4Sdo-AEakocNRrUFVjpMBN7Mb4VchLUHwpmIQdNSWHuu4JWLK3iX-4xktKqA3RnpTkJvxnQ-sRTSB24DSFtsYdBpgX-k2084xy1hVujnjraOHYx2LnmZbdxMjdGOPh-bvJG61HwvrzkbaYIc00SpWVUQSl9MVICQBntg3HHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=szmc1afR6UrhHVLscNJypEJyA9t1HHq5Fil7OvWpNmG1juSN5GocI0Ld9B1ZleEn466jS91hhRUvXvmNcRolsoMB6KAjBryPaVdFYgh3Ayz_7bRHacelWFR6hu2i3iFif6hsBjwaTeYFzNQxPiVMbCUOKjxs2cdU2dSDMhNNrydjRAUSbagq5cdra8iRjPqlRCnR84vtXxBwLZK7qBb7sXcEOvKFJnhHTC7qO6vf-FeK1f0BeVvCOB5GrZ82wNkfQZwbh9ClwYJl14WLJ5sYEWH_w_S0LDdpIzHsbHopOZD3iss40loKrhL-PZHYjrdLLoOY9nCz336l7TG16jsBrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=szmc1afR6UrhHVLscNJypEJyA9t1HHq5Fil7OvWpNmG1juSN5GocI0Ld9B1ZleEn466jS91hhRUvXvmNcRolsoMB6KAjBryPaVdFYgh3Ayz_7bRHacelWFR6hu2i3iFif6hsBjwaTeYFzNQxPiVMbCUOKjxs2cdU2dSDMhNNrydjRAUSbagq5cdra8iRjPqlRCnR84vtXxBwLZK7qBb7sXcEOvKFJnhHTC7qO6vf-FeK1f0BeVvCOB5GrZ82wNkfQZwbh9ClwYJl14WLJ5sYEWH_w_S0LDdpIzHsbHopOZD3iss40loKrhL-PZHYjrdLLoOY9nCz336l7TG16jsBrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugpg95NFfnd8bk4PN1igZgRPgc6ENmm1Fk6daRTJCKjm4IB2egWwd7LleAcUDORnK_6XBkmAfMQoSWZetHSJeMCiH1qPCXcYONoUiLZkCDTgI1mvIwjO8j-rPeavwCe9cHxhbyVeshmL-rTt0aLxl4O5Jk_9bDiMGsOt0bq7K8iBc3RmfXX7dSfyBJCEnu1JSzGniz5_52on6zblz1a9vRRRB4-qjy806bH5pCYZdtdbKuvpZF4NGtpR-OeLd3jR3VkEgH2pXuwbXFbIXXbSFpA7Vks6frfUGgJUXPSUSFzwKPfr336JEEYRAclgnwci0zderDKh-9RX3BRMDCNvOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=k3oev2l6mkF-d4YLP-vTH9Lq86VkOynVeFcESwPgdxnq4J-A3Q3ETTaV13gqRVyinthjVd-pItk-LwbWZhEuO0bem4Tj7_SIDOsznrNJZDhJbGP_9KqfNJM-I3dZsTCimtwWuqvexYTND7yB43N4yhJ4xHK2xcjn5DEzBGeP5voAVQ6mLDHvWV1-X49_IgJXpfM8as3r7HTBXztj1FyEMExbnpBoxt8lMfIuGFq5npxNJaoKjp4kJLYsohumPqtKECbwz2sQ4DwriHrjjEABCOQ9OGbqrUIya_Au_XQFQazmpFze6Vp2EHzowIPE2Zc6Y552NtYB-5ZH363_3t2-7y1n3z5TryfaGVskLWumgvTlHRvzaousDu8Y9j_qwrGMdk4q0zyg8kHssJBGkOm9aXalV02SVgu95_9raKUjoyUhwiz4RzNXRZimsoco2Z2LPi9SNrsCNxDcoHg2GdmKEhEoZmCp3szW4yDU4hDO-jUQkUBudpmSHwvj0I5SMHKO--tBWAUTHDEpgHwO12uxIsYkllTAO4FcPH6UW_ITjhm9lNJ3u19jt_MqbvHGQ_gxbh5OY-7OzLYGwEAEnd9zi8wi6cGIhOgaKpAu9SvydK29fX6TZJ7lRkfL1slIiQ4GHajObga0FMJYc33SalZ2tZwCWx6DmtjJ2IbXpS0fHcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=k3oev2l6mkF-d4YLP-vTH9Lq86VkOynVeFcESwPgdxnq4J-A3Q3ETTaV13gqRVyinthjVd-pItk-LwbWZhEuO0bem4Tj7_SIDOsznrNJZDhJbGP_9KqfNJM-I3dZsTCimtwWuqvexYTND7yB43N4yhJ4xHK2xcjn5DEzBGeP5voAVQ6mLDHvWV1-X49_IgJXpfM8as3r7HTBXztj1FyEMExbnpBoxt8lMfIuGFq5npxNJaoKjp4kJLYsohumPqtKECbwz2sQ4DwriHrjjEABCOQ9OGbqrUIya_Au_XQFQazmpFze6Vp2EHzowIPE2Zc6Y552NtYB-5ZH363_3t2-7y1n3z5TryfaGVskLWumgvTlHRvzaousDu8Y9j_qwrGMdk4q0zyg8kHssJBGkOm9aXalV02SVgu95_9raKUjoyUhwiz4RzNXRZimsoco2Z2LPi9SNrsCNxDcoHg2GdmKEhEoZmCp3szW4yDU4hDO-jUQkUBudpmSHwvj0I5SMHKO--tBWAUTHDEpgHwO12uxIsYkllTAO4FcPH6UW_ITjhm9lNJ3u19jt_MqbvHGQ_gxbh5OY-7OzLYGwEAEnd9zi8wi6cGIhOgaKpAu9SvydK29fX6TZJ7lRkfL1slIiQ4GHajObga0FMJYc33SalZ2tZwCWx6DmtjJ2IbXpS0fHcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=DhELnB-xc98nzvgOWGrd6z4O14TFhLb0MIQ_vDwRM53UZA5rW0wldyXAFAyMo4Dg4T41rcSQA_qDFR70W50gS9uTmlGfgnVoPlvZsT7rqtOFSwYbn12Yu4vLxi_HvSphgI4poF1FQ6D717cMi_cOZziMZuGAv7ShEfsnfBTRG8NKbPYPgsG-W2S-sRvF4vW_GhMDgdvLcwmIXjajBFYlWOgTmv5L6mtnpUYMUQJ64LLle4bHAQRZlVFYUku08FZnINnhYM4U6zs4usre4INNKjpZt_vNNAILqvKYmUVgc-g_V7nYweGKeH_VXK4xzntGn7euC5IJk3YfbYZdbuiBaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=DhELnB-xc98nzvgOWGrd6z4O14TFhLb0MIQ_vDwRM53UZA5rW0wldyXAFAyMo4Dg4T41rcSQA_qDFR70W50gS9uTmlGfgnVoPlvZsT7rqtOFSwYbn12Yu4vLxi_HvSphgI4poF1FQ6D717cMi_cOZziMZuGAv7ShEfsnfBTRG8NKbPYPgsG-W2S-sRvF4vW_GhMDgdvLcwmIXjajBFYlWOgTmv5L6mtnpUYMUQJ64LLle4bHAQRZlVFYUku08FZnINnhYM4U6zs4usre4INNKjpZt_vNNAILqvKYmUVgc-g_V7nYweGKeH_VXK4xzntGn7euC5IJk3YfbYZdbuiBaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjIs6ZhqthzXfar8WurCxWGsEHd_YpIQfjDz_u2vJnnwPSOiqG_ct6HYoYYxpvDQX7dK6DYjaz_l9QNBZXWE6ygP32RwNUkYKo2g0xNtMB5R9oVYQhlTIWcUnKZKrdyXkTZ4lSOk7tOtXtoOaWC8YM41VJSNJak5yS99PaJ9kzYJ0czJiKJFu3pjCaJ4OIiNE48R142nYfRgCApnBrBeXyHB9yRsAb7W8n8pou45uuWn3kAtByXscQqHlZo4bwN48Y7NEfzo1H19dewOmweBDlSb1vZtQgV0cBxXh6LKSegnTJXDu7toNDHMgrjmSsCHDOB6XcpvHVzM5embf2TVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=WcdMkC62ImUhkOBCAsh04C1Tp9OQ1F-EWwQjn7e4gFb1ulaoajeIMuHc7YmN1zwGhF3Ebl-SW6LjnRBSLNJKH5odydtoae1tQWoV3UDTZ98tVGvKMrBWNtAx4khrVR4dGqzOkEFCqNdK3XMyQsPpsrzy8zNtDs6b2YpTdPZeMhQRRd5OByzEYbKrFJsW9CIlGCqKsxxOckhWeo77Ol-bO3zdjjQsAYRHRKHJRO4tGFEtcTdSk-ziadfQPAre1PwRRlUzec96XBxxaAB61BXPe2omLLq1uKgXAwy16kZgZuJlvptobPtkLIF5vdBIObXSLNFffZAa2VznONVSkGaNbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=WcdMkC62ImUhkOBCAsh04C1Tp9OQ1F-EWwQjn7e4gFb1ulaoajeIMuHc7YmN1zwGhF3Ebl-SW6LjnRBSLNJKH5odydtoae1tQWoV3UDTZ98tVGvKMrBWNtAx4khrVR4dGqzOkEFCqNdK3XMyQsPpsrzy8zNtDs6b2YpTdPZeMhQRRd5OByzEYbKrFJsW9CIlGCqKsxxOckhWeo77Ol-bO3zdjjQsAYRHRKHJRO4tGFEtcTdSk-ziadfQPAre1PwRRlUzec96XBxxaAB61BXPe2omLLq1uKgXAwy16kZgZuJlvptobPtkLIF5vdBIObXSLNFffZAa2VznONVSkGaNbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAdztuwUlxkIBUjnqa65uiKLgBf4RS1awaNcbk9H-IKWGXGAUHbYrnw7mCAavA9INfagIUA0krfgNexswXLDJih6WFlsNnq2HLlK_jEDDxhrMcJrBcPxMxb9PbV3hsY5CwJpbuQXvPYkObVLzu0tOUm0MELU0_qV2hdUz6260cEzgQrRuJuDlrW1nS98E5oNZass0ePjba6mGzyKjGwFUeFsI_JzFBHbo8IXz8FWJO6xsb_NM8KfjbtAS0u_ynVS6Z1GmJr2ziMOLkAkunJS9ltsfiCLjzwx-PbmzLj8o1oRDsThCgT6LtYbRet6s0MJzGqebuEWiwogikrTF9cVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGXMyCFSv8BPSKNPEkPYItTQgOSPuQY5pfiTFi8iLDBBFUSmUMbKR0A10D4txrbdAEPrgIV2GbSpcoPt2AaJyrJWEfnqj8jNSNq5-HRnFOs6aAw4_v71E7LcwiWlEaNQqjX1B4OfohlTltyv2_7j4c3ccMtdtR8CrckglKnSxhaU7NvZtiY3kMvIPyf_YIpyiGrgUa2b_z5U-PMa2O55GkFKDHFUKrxNJJWlFx6h6PKgvknXiy-T4YoYhMUH5QJW7mWnQUUqgIjSQrsK5ZIF3ELdhLTM11bBSLZkqLpBkidaMaztgn07IGNOI_FuViZL2Vzta7QKmrTTzirk4NXVWQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=dAvsyFosoJL27u7WZifxVbQ5cxoP_vmCw1fLRojtvc7fhbfMLY3nQnvqPbQQOdtH_Q72rnpeLJmXmZ1yRqlEgcLt8WGhxUu9PKxWUp1Zq6Kji2FoZ2jUGLobHIkdXEtuYOO1W0tojkAo3uWtf8V-RU6-8l-L5A7yRq2wgj6X9K0LLbXmoPKsIEOehY-lVbaFrj9dzY2ddx_wDU3Jr5OlCTwhEMu5cMdJitLWV53zli1Gmfgl2l9_Xvc6VSBNwS7I7ZHQmigkTj4w7kXXCczwao4Jn3ArVU4DX1DL0_ujnJk3Epsrn4UeABS-hjuJ-cwBEqZEaQlOH-RApodKGC18_ioSZxXgNvjMcll6cqLxIP9sDS5RJPtvkHupwSYSJbQhywRO6s4_baQCP-IhCa-FWv3IxmDEPkSI9jkTrVz-h9YsOBO4v5xBx96kzqKEI96PXCdMQ71tIKReHDebHphVVXRXn0haiJ8I9BZogxcXzUoFHT1BzjS1X9PRNAcvRgCGgxya9Ijra1BWMdiAz-70h6QxBAF7VEtidi1EYHLVZNoNkFcKTKELerUcbwEle15C-2vtUcjzyB1cA14VwGJ24rL3y9rA4M0TFPxfyaz00xpgR22T6bVJGTGSDdnSeooxRdGUtMPbRdgvDNeof4popl-IzIwjYl63sqms5qzgVtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=dAvsyFosoJL27u7WZifxVbQ5cxoP_vmCw1fLRojtvc7fhbfMLY3nQnvqPbQQOdtH_Q72rnpeLJmXmZ1yRqlEgcLt8WGhxUu9PKxWUp1Zq6Kji2FoZ2jUGLobHIkdXEtuYOO1W0tojkAo3uWtf8V-RU6-8l-L5A7yRq2wgj6X9K0LLbXmoPKsIEOehY-lVbaFrj9dzY2ddx_wDU3Jr5OlCTwhEMu5cMdJitLWV53zli1Gmfgl2l9_Xvc6VSBNwS7I7ZHQmigkTj4w7kXXCczwao4Jn3ArVU4DX1DL0_ujnJk3Epsrn4UeABS-hjuJ-cwBEqZEaQlOH-RApodKGC18_ioSZxXgNvjMcll6cqLxIP9sDS5RJPtvkHupwSYSJbQhywRO6s4_baQCP-IhCa-FWv3IxmDEPkSI9jkTrVz-h9YsOBO4v5xBx96kzqKEI96PXCdMQ71tIKReHDebHphVVXRXn0haiJ8I9BZogxcXzUoFHT1BzjS1X9PRNAcvRgCGgxya9Ijra1BWMdiAz-70h6QxBAF7VEtidi1EYHLVZNoNkFcKTKELerUcbwEle15C-2vtUcjzyB1cA14VwGJ24rL3y9rA4M0TFPxfyaz00xpgR22T6bVJGTGSDdnSeooxRdGUtMPbRdgvDNeof4popl-IzIwjYl63sqms5qzgVtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpu62V1Fb7b_8VEymrddvbYNpLP7J2Bc4WoJUcjJA6z_Lp5pS1h1xhGKg-4rwsaj5fz0zT5I2xQcxLYz70Q-Ax6BQWHBWQjdOelJwhD0Y9GrQXOanW_QFrPVKd5S7OVhi2BfgrSXasR3LShIZ9YuvJQJFjOKvnwn6UjPDzlHvCErhN1hzVxnmxH_zaYs6a_ntd0eJ22Y0HhuUiEOP5pY1swqXB4Eh7AlRUiTsC4rwc7G-JQCuJXhHskgaTKBq211NUqZTTBr8gn1o6vy5qnD_XeXTZYIiz13i78VkxbY8godWEfhi2g5FGTDLS9CHKUm0hu7ckRQkMsb4VPhvLD92w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBzG6_MWePpshL2c3abzj7B-8sdhQFPeCJI_8ybWuwYVk3IDvevAUcRS41dXCm6Y4R1ozlkEB781l83-v1ajFDi1bY5gpgsny-wp-MA6cmyewlnC0iGEZA2CdP11nBRt3Fccic7k2G-2aY5ZaWyt1-5Y7Pq4f1zimQpytxkvkhck4G3pKORYGCv97GcNZz3B243gmF0lEMA27e41Xq8Eifl_Ag8vP3BeMbSdmnkHuyNwJ2pXJqumYa-y7yfuHxsW6UCt6Di_Sj9oHSmuPmbd6I04woEBopGzIJg-67JuSB2BdRYCNjhQcIT8rPL7H-TFWPD_c5KCF0qHb95OU57w9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=BKaZaTyOKrcLXOZsaMD8hxoWNGcAZLFyT8Gg88z_saFTVntKgd7FbKO5wEnlb_eE_jTl_v_H8hSPAwq2ZkaeRA0IYJcPmBSz9AL8Cfay2Q8bc2jDZeSy76XEaNk3OTzGcIwGo0vYXoBdZfuQasA-5c32lYUnYAfFPRRu8yc9y6KtNWtl3HVMqc_IjRXdmbfUwqiB0y-d8LS7jJg-3pFv98e-ebclDEdRelTAEYIs3aOkHm40VttbtAmrN4mM6pWVqb0OKFPJwpDnzCc405qqMUHWCyYMajF-ROrHZ_Yfl_kwYiM1u6ZEyHv_5O2oAChqk7RDRRHX6b4ixjc8F1iUXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=BKaZaTyOKrcLXOZsaMD8hxoWNGcAZLFyT8Gg88z_saFTVntKgd7FbKO5wEnlb_eE_jTl_v_H8hSPAwq2ZkaeRA0IYJcPmBSz9AL8Cfay2Q8bc2jDZeSy76XEaNk3OTzGcIwGo0vYXoBdZfuQasA-5c32lYUnYAfFPRRu8yc9y6KtNWtl3HVMqc_IjRXdmbfUwqiB0y-d8LS7jJg-3pFv98e-ebclDEdRelTAEYIs3aOkHm40VttbtAmrN4mM6pWVqb0OKFPJwpDnzCc405qqMUHWCyYMajF-ROrHZ_Yfl_kwYiM1u6ZEyHv_5O2oAChqk7RDRRHX6b4ixjc8F1iUXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=pkK56NVKloYrxuqFOgr3__i-rbHYhefBovuFwl0kiYjYNgQLjN4lWjov7E_0oqTyMnOxRPzz9qG5RcWWwTIMRxe6OSKSBmlmeCUE_-Xu-l8S2nbHViYVoP8j-aE5B9H7svipTluI4N8JgV3azmvti5nbh0zqpRnU0KdFGNgPDCMPc8ABijWF8l8gQVnjjiHRZbcdik8v7Z7E7pFCRj-dSAxq-l-Zvtq1p19TNmfNjfVsFShoQYFp4_YbJ-ySUGwnnifGYx8CiMO0QsG5BPna5TtReYDDsDaJWC4BMkm1Wo8bA9aDxqPo5X1lrolF2aNcVIlnDeeuskcz6wiz0b_yLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=pkK56NVKloYrxuqFOgr3__i-rbHYhefBovuFwl0kiYjYNgQLjN4lWjov7E_0oqTyMnOxRPzz9qG5RcWWwTIMRxe6OSKSBmlmeCUE_-Xu-l8S2nbHViYVoP8j-aE5B9H7svipTluI4N8JgV3azmvti5nbh0zqpRnU0KdFGNgPDCMPc8ABijWF8l8gQVnjjiHRZbcdik8v7Z7E7pFCRj-dSAxq-l-Zvtq1p19TNmfNjfVsFShoQYFp4_YbJ-ySUGwnnifGYx8CiMO0QsG5BPna5TtReYDDsDaJWC4BMkm1Wo8bA9aDxqPo5X1lrolF2aNcVIlnDeeuskcz6wiz0b_yLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=OgG_p7EkHxyeq94bg7D2M01sX39CJafuYq64SE62VPr0TvXNobIBy-nr3NR14iUDDQxJIn5_wj3vl9wUXJTJ7DP6ADPfyVtO70ZXKAc0AM387UHpNiv8D5HyA-r0RJGUWhdB9gFNOqPGOmQr-Hrk484ql3mJn3mHNrUodg3AyxNXNQnjDVSF3Yhar2ar2P7Umzw_-s3_zF9af65QLs3ldfZP9QUPcuwKPqEz9q5vYbVdZy4Gw-tDsrsBxjsppIuBy7YZknh0jZq6yFOgcLPAWrm0xbdPRy7Abnm8joRYVP3UX8WlT4aKU926EU9GDHiqial8yJO9HM0f7SkX5OIAqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=OgG_p7EkHxyeq94bg7D2M01sX39CJafuYq64SE62VPr0TvXNobIBy-nr3NR14iUDDQxJIn5_wj3vl9wUXJTJ7DP6ADPfyVtO70ZXKAc0AM387UHpNiv8D5HyA-r0RJGUWhdB9gFNOqPGOmQr-Hrk484ql3mJn3mHNrUodg3AyxNXNQnjDVSF3Yhar2ar2P7Umzw_-s3_zF9af65QLs3ldfZP9QUPcuwKPqEz9q5vYbVdZy4Gw-tDsrsBxjsppIuBy7YZknh0jZq6yFOgcLPAWrm0xbdPRy7Abnm8joRYVP3UX8WlT4aKU926EU9GDHiqial8yJO9HM0f7SkX5OIAqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov0BkYS3j_Ihh5R5JYLaEL-I2rAoDq_eTnRnQhuFrcnP93wL8hmJCwxID0I2ODwYAd5DTqS5f-lwJGswOm2bfcLIRmjFqZvlXQPjRWMCq7cvmLCUINCX7UjQ2jOy-yyp5GmmHHqSd1vn7zuf_xY-bDdGuRVg8VwgBuE4FYO79IPZSkTCHaojw1XCMptxfEtyU386ANxQaX-EE6uATRO5GMexnHEabZZN74I1Sj3UDYuGRmUHlr1gQlfxlwjdqaHPeDunDcona9P5nsHdze4uVyGKIyJ9mwWZHkPcVV02qvNq6Iqo05qTf2QJqcKJlZ-ccNJoh4B-vg0RSH-8o5nnGw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8EnqF3v5JvGLoa7mecByj536fZeznz0bs2HnDblx8BDFljj_ACdhfwvqtAqN6Aa9LbikeWFWX4qSTKRe4FbqRFG8xfd9PEK_oSyfkYTd2UinM4tg2WzjTRhtmtBKk8_VYbhLy63swaKtG014hHgg6keeseEvuxZhshVmXHtkPEjajp4Y7xtZ7af0nbVcfrZ_g4FDmTXpgi3-_9EN5lNosSovLz1O6mBAXkfjtB2YmPs0J9oJ8NTEVawvoBVxwTOPpswsCl-4smRs3ZHaog5keLX5CqxRI3kZiTfonPjyqg-W6e1VYvOdzs7qhKECwCbUOfZRPZJ5Mf4aTKVlWLnHAAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8EnqF3v5JvGLoa7mecByj536fZeznz0bs2HnDblx8BDFljj_ACdhfwvqtAqN6Aa9LbikeWFWX4qSTKRe4FbqRFG8xfd9PEK_oSyfkYTd2UinM4tg2WzjTRhtmtBKk8_VYbhLy63swaKtG014hHgg6keeseEvuxZhshVmXHtkPEjajp4Y7xtZ7af0nbVcfrZ_g4FDmTXpgi3-_9EN5lNosSovLz1O6mBAXkfjtB2YmPs0J9oJ8NTEVawvoBVxwTOPpswsCl-4smRs3ZHaog5keLX5CqxRI3kZiTfonPjyqg-W6e1VYvOdzs7qhKECwCbUOfZRPZJ5Mf4aTKVlWLnHAAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=WzGMUrQS70mYZwcZKQEIYeFjm_BRAm77g8H9KsSG5ix8rdwZi0mIuPG5eLfstWTbijO-SKEk3FCRYcZpIBeS1WRrQ201NgnOXdFZGdniXCPEqm8fzMkeR29nZ8k2wloNlncii3u7eDRh4lbpK2lOX5NO4fNIFelaSTUktel9rT3HAB3U63n-uSwrBjvks1lotFt24yUupflVdlVeydA-C06gskuqrUdOsfPjjWkNX2PFohRnXcN-lxidrHCJQ_RVGO1_RHQAcN1oMUCinxdYLVqXWZjFfjuG7Buv_rMcimkBks7kO3pYU2niO_3laIoY8NM5bBg2BefOylTT-AUhLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=WzGMUrQS70mYZwcZKQEIYeFjm_BRAm77g8H9KsSG5ix8rdwZi0mIuPG5eLfstWTbijO-SKEk3FCRYcZpIBeS1WRrQ201NgnOXdFZGdniXCPEqm8fzMkeR29nZ8k2wloNlncii3u7eDRh4lbpK2lOX5NO4fNIFelaSTUktel9rT3HAB3U63n-uSwrBjvks1lotFt24yUupflVdlVeydA-C06gskuqrUdOsfPjjWkNX2PFohRnXcN-lxidrHCJQ_RVGO1_RHQAcN1oMUCinxdYLVqXWZjFfjuG7Buv_rMcimkBks7kO3pYU2niO_3laIoY8NM5bBg2BefOylTT-AUhLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ovg4zXzkNBi_gd_DuGuIXqE8Qr3-0Y12ZlYL-VWlhTnl4WJEuW9r_3j-5OM4yyxlImi4ajWtDrZ0GA_pxm8t5IP9eLKLebUHZzPly3J6wNhRj4-Q5xK_20vo7klRd1o8HKxDGdtKCYtVRLsrUrsLg7UYn8-yLCk9YjYhkf1c3rT5JrPAFeLrlbKjDnx9W7i1PMnUOQVXg7WUUcPpjQno7H1n2NaJLwYbxJxg9Ead68IqDUvFgrjEPLZlJazms8349LeBdGMGry9FGw6NkYOScVfIMKxw13uFTdClFIO4NnNPjN6BkWTKeYw0Tg2YlhuBaP5RJi_uN7bj8sRM3XtE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=gJZcrFfSe90nyURHopg1QUPO8V6Gw4362ocDtuHQ_pxHwkO0KupyQ5vF3_LEOz8c9srTUkI4SHrFCEUzZ_jBQmJy9kMn6B73deEC0dDnHYNq7kTddOtTrtz1cVKIF9tfIG5qBQz5RbHyygYXC0REUahIhdW4ivD7eJK2IabJW7lvUdUhBQ-1AknOIZBVKX44xMdeyIxlX6IxFs4D5s98UedPnAS-8_-t-mdXC4r5SKFBHoXafDRlEreH_jwo9hGeTq_ZH-Gm8xKJNsBzF8Oua-CZ17GZ2AzAER_E9IfcSsJkihHC0rziWRS3ffAId6yzSS0HrzkeaRzZ9r95OmytUQ-ndMdbq-ECNm73cuzlX8tFYVmp0s9se8O665P2DEjP16L1s-OndM5vFZpbIZnl5XSkLlqADCorwYokH6taaJS_Kox0h_KElnMK5jg2TIJWqWdYJiXVNGy0Dq5jrIjN4NCBQyPn-qT0vUVAgC13zlXl7aaoNXmbxXL2nQdtu6uG1lr0HYs9xHt_VF29SE5x5HzOV6o98vg6PL3RPe2UmsNHvt-pYcNeF_8yQ3Ahef4V760AuDgpRiXCjmIDRSgBGdnnkZ36NkKBoZfJWZ6gMeHonfMX-ynmRPXL1ukk9rAHu8Nv6YUMr5se1NfCmlE3UvktF7XCZsUWUWe9TiSA_0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=gJZcrFfSe90nyURHopg1QUPO8V6Gw4362ocDtuHQ_pxHwkO0KupyQ5vF3_LEOz8c9srTUkI4SHrFCEUzZ_jBQmJy9kMn6B73deEC0dDnHYNq7kTddOtTrtz1cVKIF9tfIG5qBQz5RbHyygYXC0REUahIhdW4ivD7eJK2IabJW7lvUdUhBQ-1AknOIZBVKX44xMdeyIxlX6IxFs4D5s98UedPnAS-8_-t-mdXC4r5SKFBHoXafDRlEreH_jwo9hGeTq_ZH-Gm8xKJNsBzF8Oua-CZ17GZ2AzAER_E9IfcSsJkihHC0rziWRS3ffAId6yzSS0HrzkeaRzZ9r95OmytUQ-ndMdbq-ECNm73cuzlX8tFYVmp0s9se8O665P2DEjP16L1s-OndM5vFZpbIZnl5XSkLlqADCorwYokH6taaJS_Kox0h_KElnMK5jg2TIJWqWdYJiXVNGy0Dq5jrIjN4NCBQyPn-qT0vUVAgC13zlXl7aaoNXmbxXL2nQdtu6uG1lr0HYs9xHt_VF29SE5x5HzOV6o98vg6PL3RPe2UmsNHvt-pYcNeF_8yQ3Ahef4V760AuDgpRiXCjmIDRSgBGdnnkZ36NkKBoZfJWZ6gMeHonfMX-ynmRPXL1ukk9rAHu8Nv6YUMr5se1NfCmlE3UvktF7XCZsUWUWe9TiSA_0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHgiI9ljh_iiIONJp3y_3LlXoZV3m_-7D_9VO42g3QiddtfNNJXiYwuv0ACBzaHk7EtvyLe20uxBHdhwXA2iwWKneMXw_ZUs9aHkuYB7rkq61gwrX-rZWQKvkVtpj5M_9g9GqZNabT5zOBx9C8coQKWKMdsfcOwVAB0kD5v8M8H8pnWsowU5ow0CX70LuRpL9-QMexs9uQc7ib87KJnMone0uVh0AHYDZhTRMKjXac8mJ_PA3PV1cw1jC0kAAwlh6nDrhIoEm-aMWjnvZwwSIOcvs90oGBM0_fmYAU1EWGTwkBamfq4zZ1jZeDKlGt_IXVCYglMLV7Eghy7TAU-LjA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=i4m1AEpQ2d2xe_DU7TpZPEt7elb27O-MROr01z5CTdZmTq9IYF4eoBTlaxhVAygRvxgou5AMqR0Zr0MxnmVMRmQeb4iNyESCwwMpMY2HuDTGMtATOHsvh7VtPa9a7G-gU6ACtME1T5mX8Mvv5WwFlgiBcLERrXNhXvugdX5gHOzZNmWJt3i17BxAPybSHwe7oglMFtfznlh-6gjm9_vwFkso2TCqFZRb-p8vxh-dRU-KsPTCtrzbkZMbyArtAKUPN3xky3jxrm9ewnB5SbpUCBLFzoYhqqAQQN4gfFtmkAqAPK6Ui_q_DSBDYoQEoAxQRMZlbI32ER-ycJqDObB34Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=i4m1AEpQ2d2xe_DU7TpZPEt7elb27O-MROr01z5CTdZmTq9IYF4eoBTlaxhVAygRvxgou5AMqR0Zr0MxnmVMRmQeb4iNyESCwwMpMY2HuDTGMtATOHsvh7VtPa9a7G-gU6ACtME1T5mX8Mvv5WwFlgiBcLERrXNhXvugdX5gHOzZNmWJt3i17BxAPybSHwe7oglMFtfznlh-6gjm9_vwFkso2TCqFZRb-p8vxh-dRU-KsPTCtrzbkZMbyArtAKUPN3xky3jxrm9ewnB5SbpUCBLFzoYhqqAQQN4gfFtmkAqAPK6Ui_q_DSBDYoQEoAxQRMZlbI32ER-ycJqDObB34Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohQWCDoWRMFB_cR6eMLs80kTTakcMHteHXIqWU4neAf0KV8YtLTjCB_YtL0Md5B_mhv7qsiW12-j47OA3boVmJSQSPvYyXWNugmjoLLF-GA23dkwuY6wmcTZdE6_89JkoofoQ1whhg5feOlHToKCW4S1hXVHFswvzxoC4t-YabP-Yaw27gZB-5SW_qp8WwXm0hsyqhQZFQv2K_PcqrONaYUWIXieVONu1kt-77a1PDzTOQsZ-p6iCLpYkmgF0pbLVAvSOhrD5uFIQSMADREZ4MjtK_yWz1AZUpF8Ol27MjJ9g3m6CBamJ6YtQETKaAeq-g2l43ast7BNSLps7_eiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzWmG1eukamfT2__qlBHI6DQV2OQuK3LN_2ipBCGjhGMlPsChPJxGKiJASOgQVH74KSEk4u4SAr-Wt1GaBA6KYFy_8MOrjKFCa85cSPxU-6MTGH47WoL_VBR8YE-3hlsAtvT2G2KhMxNwyo47e8n8sHqPQiV_6wzuxEcJJt0h7Sz--eh4o4WqiZHZA3v6xAoP_G6lz6qAHUXs1yp_wEISCPC2CKyxWFzpvRA_N8Y0GlfuXBON9u3-IiAreoCd4v6P_8mvs2tPycIiK7cok9_vwVUfGcjhxVWtL_5Mcg6WzRtwRmM6ixpxTcqo2ctd7WYPdr2pqPrepG2IgYyRli47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMuxLy6sixF8kJCJ1B8a2ntyGwFWpd8KFz57dbqvFg4-umQF6DaDRZ4taG38bGlMcZMG0xQAnt7CGjk9awR-nWwlC9qTpOyYDD6qWvjz5YDrPt-TEgXJ39ENodQiGzl4E2Iq1Cl2gxuadyWDRCGJVdDuM2GhZaKep1rLBcbHVgzsr_AzOYtFKCBqz77NYzsSN-rR9v7vzYt7VIouzeTJk28DeKetk0S-iKXU5oEJOVbj1-_d4PneuwEqMxcyjFsN-8dI0bsLl6dLv5oZkT5bL9Pht_tRhhHYvnvrzpYJ1yDl1Wdt3md94Py7ZN8om5YcW_y4sxENgy6C6pomrNdf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=d7GFVcqYkICe8PSz3FUyewLANnJIEBBfGKBNkIlC8f-8Ve58w1m4ZaC6lVK91sQbYhmAi8GTkA4f_3GKuXabuec-P_DP-dTeFuPwNPfZcgwKh46eJOd2TyU7dCYknxnU8gA5XXUpzcDfK5TPn7fi7cwajk93SBoXMz4MqmHzZ0TcXZK7h-yWHXw_uik7Ff4x90ZZ1ylbUGYVQ1Wdgo721iJ1sixcDtekRKI4gv4lfjZ03UT5wVKdbTlGYGZFjc4cce-kAFSJrVvhZ_hnMjCKHrSa4pSqv6eYURpdXbJRHpGdXaaeAG-XsauESt2zaAsxzplMV5mYaNFn_XcYaBj8kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=d7GFVcqYkICe8PSz3FUyewLANnJIEBBfGKBNkIlC8f-8Ve58w1m4ZaC6lVK91sQbYhmAi8GTkA4f_3GKuXabuec-P_DP-dTeFuPwNPfZcgwKh46eJOd2TyU7dCYknxnU8gA5XXUpzcDfK5TPn7fi7cwajk93SBoXMz4MqmHzZ0TcXZK7h-yWHXw_uik7Ff4x90ZZ1ylbUGYVQ1Wdgo721iJ1sixcDtekRKI4gv4lfjZ03UT5wVKdbTlGYGZFjc4cce-kAFSJrVvhZ_hnMjCKHrSa4pSqv6eYURpdXbJRHpGdXaaeAG-XsauESt2zaAsxzplMV5mYaNFn_XcYaBj8kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrX3Ty4MjyzX5iT74zrEvBQwf8EW5dq3xP9hYk8-Q5TdTx_VItaZ4Ss1cf2leP9gbFpqVeJuyIw9Pjoh27H_k4mU3XVbcRl71hjInEjkEpLX_Zd17WHGW2m_XWEt0g0O5lrxiex0Cvl9onS60Bha-ESFJbg9fbaG65bOxOwiE6TqlH9_y4vYWebvYWYhLjW-WeBCC4s0WwssY6vm3EDxd7mpS81KDUrX1umt7wUsm79KRewmTs9NEG42RVZXuWIjzQvfoTkhqvot9DZ9NrZ-Bg3_W8H2IwoTgMXHOStUhAg3BAo5fZ0aXa2TVmqBdWPZIV5MKfbestvok5c8qgJH1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFKg6TGTEemJEbiB3jI8Q0tcJV_AkCejRhubTHG_jiLXEqHMUxzXSJO1FUm9Nh8qHoT9dmsTaeLARJgy7xotug9admTdpyyINFISMa0w8AQYTTS64D__oOisNwLjXrKIcNrwG5qaamwtMUSpALziFSBWlrjwGF5lId4yGXKNchO_-dXtJbmv08c4GvnqOrh-tuCRyfArab-r1EzZkdWrn7O6ywSrl2qi-H8Qzoi_wbWW6SKoB8DuCS_vgklp7sTu4cwM2t4wBdXG1XUdSOJEFsn1_7yln3M1Ym2AXCeG8R_D_PXR1S6CBiuVYl8hqpToHU_Dp7FduAeTjycKc5mBaJgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFKg6TGTEemJEbiB3jI8Q0tcJV_AkCejRhubTHG_jiLXEqHMUxzXSJO1FUm9Nh8qHoT9dmsTaeLARJgy7xotug9admTdpyyINFISMa0w8AQYTTS64D__oOisNwLjXrKIcNrwG5qaamwtMUSpALziFSBWlrjwGF5lId4yGXKNchO_-dXtJbmv08c4GvnqOrh-tuCRyfArab-r1EzZkdWrn7O6ywSrl2qi-H8Qzoi_wbWW6SKoB8DuCS_vgklp7sTu4cwM2t4wBdXG1XUdSOJEFsn1_7yln3M1Ym2AXCeG8R_D_PXR1S6CBiuVYl8hqpToHU_Dp7FduAeTjycKc5mBaJgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=kKsB_vWZmk1kTLaeWxxLeMwCd1jgQoDi75Y9qL80OjgxQC0hEABcPtLVu5OhLfH1Q6CMjZS-_dk1L0PsVSHhVzXzuau8am1sndRJwWP1tEaGB4od1lcZQ1hQxs06bcSBqSPU6j-XjJokDS8hL9aitdGylH3IGuuP85zyBP5BsWpD5m62hAso9pUixq4JwJ16VLgRgDIcktCUKVv9llMS7Pj3JoBQhvwO1bvn3tA53g55NcQtFUWEdcwRR29c9zDM-GrJumUIuEYiqWJxHvUwy6HCm9txs9WfqfEavAq8MawFH21LY9-VPnP-VbwnsYuwmApfBHdnGDbSXZehHlcTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=kKsB_vWZmk1kTLaeWxxLeMwCd1jgQoDi75Y9qL80OjgxQC0hEABcPtLVu5OhLfH1Q6CMjZS-_dk1L0PsVSHhVzXzuau8am1sndRJwWP1tEaGB4od1lcZQ1hQxs06bcSBqSPU6j-XjJokDS8hL9aitdGylH3IGuuP85zyBP5BsWpD5m62hAso9pUixq4JwJ16VLgRgDIcktCUKVv9llMS7Pj3JoBQhvwO1bvn3tA53g55NcQtFUWEdcwRR29c9zDM-GrJumUIuEYiqWJxHvUwy6HCm9txs9WfqfEavAq8MawFH21LY9-VPnP-VbwnsYuwmApfBHdnGDbSXZehHlcTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=SJjRtqq80qm7Nm_ngvmcsJ0QZ0DIp2g0WnoA2HMf-cTYZAT4YEChhX7u2_he-ZmyB-dqmcakeWJOPH4cxI4H1gt12x5emCEvdb0IAqLHShJhKvxeokedPP92w23p3SwAaUxcsWM6L-hSkaIkF0DxS9-g3sw6t0PSy-VTkZse_CRrmMsKMpZqs5YZT_wRIJq0L27XVtQZXnSAfK771OrJcrZd2h_qtIHAG_mFMKtuYU8kK874oLwvY1kM7iO8vqqOX1BEoOtGFlBamN1F5UquAEUSkyHm-16tquWiwjDIH-3g0-9dqdLqEdBvaWWW9eEAeCbTSdxYzYSsf5WHshXSQ1RAzTB56_ti1PMAVQ_ghoddY_Ds7kMUrN4diQc4ysPQkJCbMALyxnt6iNk1I4PJgziklw_kkuZ7YO0PULZTQ6GQ9vDbM2yRtPW6BU2Sf_PFZ57SFOwesmIwBq_9xyWxwEMffSwjX-e3PsqUrBtAL904i45j4-3kWAV6mhCFskwRLRDlKYr6E-U8ORvjvsDnPZU0u73dYmIp0kzSH50aWAG66p3jqGFc4Ddi4K0-ggdLNrpyalS0bayVYO56W1ykAAZPuwjcOUf2q8n3KeR3_LuZeYJaL6lTRyaZ1ziyX29kVgi1cYFUhrEyIvPX3CeqfBbzKULzuD4SmWrdpsIa-ek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=SJjRtqq80qm7Nm_ngvmcsJ0QZ0DIp2g0WnoA2HMf-cTYZAT4YEChhX7u2_he-ZmyB-dqmcakeWJOPH4cxI4H1gt12x5emCEvdb0IAqLHShJhKvxeokedPP92w23p3SwAaUxcsWM6L-hSkaIkF0DxS9-g3sw6t0PSy-VTkZse_CRrmMsKMpZqs5YZT_wRIJq0L27XVtQZXnSAfK771OrJcrZd2h_qtIHAG_mFMKtuYU8kK874oLwvY1kM7iO8vqqOX1BEoOtGFlBamN1F5UquAEUSkyHm-16tquWiwjDIH-3g0-9dqdLqEdBvaWWW9eEAeCbTSdxYzYSsf5WHshXSQ1RAzTB56_ti1PMAVQ_ghoddY_Ds7kMUrN4diQc4ysPQkJCbMALyxnt6iNk1I4PJgziklw_kkuZ7YO0PULZTQ6GQ9vDbM2yRtPW6BU2Sf_PFZ57SFOwesmIwBq_9xyWxwEMffSwjX-e3PsqUrBtAL904i45j4-3kWAV6mhCFskwRLRDlKYr6E-U8ORvjvsDnPZU0u73dYmIp0kzSH50aWAG66p3jqGFc4Ddi4K0-ggdLNrpyalS0bayVYO56W1ykAAZPuwjcOUf2q8n3KeR3_LuZeYJaL6lTRyaZ1ziyX29kVgi1cYFUhrEyIvPX3CeqfBbzKULzuD4SmWrdpsIa-ek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=lpe08SGeN5rW4fFPS3BWdCYOI0bTqsE6EDAcx9z247xSY-RWsofAyzxGUKYFUe7AD4iTEncQTHtAbiSF838eNkQ0i5Nhb-9c4Gnjb57EIHuJPYLE1QqHXZRwf_QVqA5IWqAzls58sdsleFYWTr-8JqhbMEZB4hOByg1w4YFn1zLdv_RZRLiq8VbEsKMetcMQjCDcY9V7n0ZeuXPDAYBvNkKRKORxwR2f0ZHFeKpsZsxo-_TX4tvv131lLzEvsPqxj5hEPAIlUUR4DsAmW6xf0EGp2P3Xm65vyZ-Ky-2HO8ZvacLl_cCp7c_p-v2fl5JXfXI-3HEAauzxBhXjBr-fqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=lpe08SGeN5rW4fFPS3BWdCYOI0bTqsE6EDAcx9z247xSY-RWsofAyzxGUKYFUe7AD4iTEncQTHtAbiSF838eNkQ0i5Nhb-9c4Gnjb57EIHuJPYLE1QqHXZRwf_QVqA5IWqAzls58sdsleFYWTr-8JqhbMEZB4hOByg1w4YFn1zLdv_RZRLiq8VbEsKMetcMQjCDcY9V7n0ZeuXPDAYBvNkKRKORxwR2f0ZHFeKpsZsxo-_TX4tvv131lLzEvsPqxj5hEPAIlUUR4DsAmW6xf0EGp2P3Xm65vyZ-Ky-2HO8ZvacLl_cCp7c_p-v2fl5JXfXI-3HEAauzxBhXjBr-fqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBTYttMeXpJCYw5PIP-3YIDU_Z3XsorPRdd_ZkiWfG0AEV6TmU2rXOC_m9TJAbzS9OXgu52vcvkAfDz76P5S_B8wbZpCzC2CHIP2ivWMhFiast-YjwaJGBTXruniTj1VrHAM24sVHnpSsgada372-7b8BqChTpcWMCA28X-mU19D6kcAcL_RH23BvzBfAAbys1SMg1h_sZAqKud8TDP9Dc3NZ6CVf14mM9CGeqT9-lp6_gh7YyxrXAYLQ1UzSMRk2FcVXmxxTewGVQYxLPJhfnZI7UJpzLYYxo9BbrezKWO6PlC0Ty2-ln2RDZfgexOy0hLM1nbxxF-e0zLdmo1JLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=q7nJUNC5pbEBACupCJn3yVbuhxb39j8fathd3xiTrCIvipPA73GQIip35ykNCK_0WK2BHBLttHcp7H306bXpoXpTO111Y0dsJq03RvDbuy5cIcILsVRIl6d9Oaz-Bn9eLenVyjg6i3E76fq7gZSYa-AOLFE37D_74soLt0p7Y_oxZC5Bm1Ncsix3P0tu_2lmbYo6Eat6GrrndDr2rN--n4NA9MfF3k51VuOSXIZgS0IvmGE8WqzFExNX5d6Qg6eb2qBKf9Nohr_-dfWE29QY8L5OBGQqyUtYm44zhoXNQl54ToFyR71T_uGr4205CGUh04GoHclWVcHz9qlDv5tLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=q7nJUNC5pbEBACupCJn3yVbuhxb39j8fathd3xiTrCIvipPA73GQIip35ykNCK_0WK2BHBLttHcp7H306bXpoXpTO111Y0dsJq03RvDbuy5cIcILsVRIl6d9Oaz-Bn9eLenVyjg6i3E76fq7gZSYa-AOLFE37D_74soLt0p7Y_oxZC5Bm1Ncsix3P0tu_2lmbYo6Eat6GrrndDr2rN--n4NA9MfF3k51VuOSXIZgS0IvmGE8WqzFExNX5d6Qg6eb2qBKf9Nohr_-dfWE29QY8L5OBGQqyUtYm44zhoXNQl54ToFyR71T_uGr4205CGUh04GoHclWVcHz9qlDv5tLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=gxN1n8n4UVBNH7hh_qe_lf50kO2eVhDglejTvc-HnOxRugsqMW8uOEiLA3WMgOnk_b5uMyW7y9EBa54HCmI_Umu0r_wdDGCXzBiQy0EBSi_8TiP7dzDR6-sx5r44xnURYfY6P1Dtmd7NtVG6038Nj_VepvSAVsj9ETvQXXMn7eG8NQkDib-nc6oUoyehOleVxNsbCL04waj4SumitldNZeAWXYqjkA6jMu3nLoE0YBP_DQLbrF47Bu-FCK5TgNB81ZPIStpDyFm7KpQ7xfpi6j3Dbw2MKebDJMHqvFbHJEH09_02qYwss6v316tFcZ7QjDGkgvduKiRNQVFDxcoJDlBQrvkE5oh-OwpEs_A0K1bSBLfYG8B2LLOpwyyYvS_79WOSaAuZndaPfU-LxVqgz8GOlj5xyf5_-U9N0C23EcAudPX7rXgCI7W-jmjNLRVC6t-mR4Oj0HcoXfAxL7_6Nj_XCJ4mSqzwUTCeKP4Yi_cgIc2yqmpcZnTYto9slGkbK_Ie0cOzJ6e3oT1gb-qA8uSSFf_6c235U0-5OeJ7D_zBs-AR23d_ysOXf80VgihLeHljhhpQ_e1LGwSHowZxyYrLZj3JCl0rSn0JLJe22ZlaijV9rz8HhZ2iuc_es5nNXFxDt7Enb5WjXn9PQiNLv-zNBuUSEFTwT_lo8nEPMs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=gxN1n8n4UVBNH7hh_qe_lf50kO2eVhDglejTvc-HnOxRugsqMW8uOEiLA3WMgOnk_b5uMyW7y9EBa54HCmI_Umu0r_wdDGCXzBiQy0EBSi_8TiP7dzDR6-sx5r44xnURYfY6P1Dtmd7NtVG6038Nj_VepvSAVsj9ETvQXXMn7eG8NQkDib-nc6oUoyehOleVxNsbCL04waj4SumitldNZeAWXYqjkA6jMu3nLoE0YBP_DQLbrF47Bu-FCK5TgNB81ZPIStpDyFm7KpQ7xfpi6j3Dbw2MKebDJMHqvFbHJEH09_02qYwss6v316tFcZ7QjDGkgvduKiRNQVFDxcoJDlBQrvkE5oh-OwpEs_A0K1bSBLfYG8B2LLOpwyyYvS_79WOSaAuZndaPfU-LxVqgz8GOlj5xyf5_-U9N0C23EcAudPX7rXgCI7W-jmjNLRVC6t-mR4Oj0HcoXfAxL7_6Nj_XCJ4mSqzwUTCeKP4Yi_cgIc2yqmpcZnTYto9slGkbK_Ie0cOzJ6e3oT1gb-qA8uSSFf_6c235U0-5OeJ7D_zBs-AR23d_ysOXf80VgihLeHljhhpQ_e1LGwSHowZxyYrLZj3JCl0rSn0JLJe22ZlaijV9rz8HhZ2iuc_es5nNXFxDt7Enb5WjXn9PQiNLv-zNBuUSEFTwT_lo8nEPMs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_icBDt4qZy-CyDwtNhABYGttrr1pPD29klie0WbfJewv6C_Lo7dyivAPS2x6by61hlq8sQ-usf1MaZxURiFpHgzydcCfjLvLrQrH1yFxmhZuk6WjPFD8Qkb8b-Gz7OZCHSR9qL-osnl1zrQ_C_hRlEZ495rKqgI6KNxWlZZ1jZkwiTPI-_xwfAmaVerEySTr2mLzSBXjyzGD423k36WPhDVPVtGmS3uEnwFvdgjUsLucRmusghHfSv7De41slQfq4EQ0KyH2UWiGWCfIefiIlIWZ0pkZUPF5cijX8gWgqcOCF0sLxRNEZdkbb--Qa8RFxKQQmej03-neBMoZV2X_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=o5bLUjMuBil6PeOFyd3bcvDXEOImWNQ6_snoKHFUgt9ozs0lRhUaeV657cwmp7UC-RSP7FiiygGa-AKF-sd1Oq7D-P7IvZcoxorCqsBtlw4la50VohvLeOjcO4Ig_VYRfexzQXx87WHFanQvpToo0ANlK-8tJ0z_3WgiyecQgXbsyLVp_aWxbc-04GfF27b1lQD8fwJiYuQ60FN2kVdT6j8PwKIm9a3SMy-oni2XmS2Mro057Gb0wWuTLileIm_lePLCHEvPmH8IzHHfr57sDGiGsyfDx06TXY3JVhbVSCRmq8Zn5z29Vdim0AZSXmiYfQnnXrXGbWtx-uOM7GmQqVtOe-HDTDuz2GAdjMkV5Zj-keWXdfOINhbZc4KrVsWWz0B02vVZsl5E-KbkfAYF5O9HikHl7Gs7P3yqRdaI5o5xclWmbqJFRpt2RfMSpIx-dGdXYWrxvm8zgmG9jYUDwgCnOwc9iTcVei1bQ6FZUdBw65YYdYLSIN-7CsohuS8jyhUIQC2X30JfkwHNFFVgw8dH0VRItBkTcb7u9YDwvZ7GbALLfaqjL4u609f6WLzei3B4kn1liD-R9ihN_JXBBAcdG16eL3WMAqF4T27-nt41TvgY1m9Xwo47zb_P5mlA-qmnv9QR5K2qCno20tNGXGumgt6tXDcZVrL-abmj0vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=o5bLUjMuBil6PeOFyd3bcvDXEOImWNQ6_snoKHFUgt9ozs0lRhUaeV657cwmp7UC-RSP7FiiygGa-AKF-sd1Oq7D-P7IvZcoxorCqsBtlw4la50VohvLeOjcO4Ig_VYRfexzQXx87WHFanQvpToo0ANlK-8tJ0z_3WgiyecQgXbsyLVp_aWxbc-04GfF27b1lQD8fwJiYuQ60FN2kVdT6j8PwKIm9a3SMy-oni2XmS2Mro057Gb0wWuTLileIm_lePLCHEvPmH8IzHHfr57sDGiGsyfDx06TXY3JVhbVSCRmq8Zn5z29Vdim0AZSXmiYfQnnXrXGbWtx-uOM7GmQqVtOe-HDTDuz2GAdjMkV5Zj-keWXdfOINhbZc4KrVsWWz0B02vVZsl5E-KbkfAYF5O9HikHl7Gs7P3yqRdaI5o5xclWmbqJFRpt2RfMSpIx-dGdXYWrxvm8zgmG9jYUDwgCnOwc9iTcVei1bQ6FZUdBw65YYdYLSIN-7CsohuS8jyhUIQC2X30JfkwHNFFVgw8dH0VRItBkTcb7u9YDwvZ7GbALLfaqjL4u609f6WLzei3B4kn1liD-R9ihN_JXBBAcdG16eL3WMAqF4T27-nt41TvgY1m9Xwo47zb_P5mlA-qmnv9QR5K2qCno20tNGXGumgt6tXDcZVrL-abmj0vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=twhKT2wYTPtfn8pz0HXE3MeU_yKwAP4tHbDBnzrL22sPupmfy8UPMGgAnBMktVwJEzMm-yl_xvGfoo6BdVJXY-moS-RrAb0AR7M5kvxduVOckVDVYTqXyhwzGd93appAw_sNK7vMq-cer0rzoTTJh2LWG7H0s0KKgTBNegTqdzazTWNdy-ytcjoGwD6Herx5CXZy8xS29DNA1ZH7krZahSGZWhNpQSYPTh4mRHpaxnXwbLC3jDvaQjfHf1zYedcjjyX0d3HTTt-DoJrkn2UnVWV1kKycMV2FjxOO7AxEKUUzaMnQmtcLMt6EuUj97NGboLZE0YBXY1u6HniKJR7Y0ojVniUemEtRKv0mmKXwexFASDHh5IfGgfs_aiizM-Wl6h2YLz78qNIdw5sjSxt4j9ZdalsWSGz8M8d809eX7arliKjwgnx6vmrun0_NRdU3IuAU6iB5IaQ-aWI50d-FwspvKxX8bXF5o9HgfuEwFbpW4y8xffJIVMmA31ZgvWAO3ssKqERz3gFMH99YgnWrP_OS5X3xs-ODjhaDyuKRcLEV-Ec893ypfwXhmgleOnUe_FwJR8DXoxwLh4hPZK3V_efuEnGr3dTsIMfIDV3EQS7_Bczxv1YcvPEvBPoTnVyiMtz3r5hTkRv8EEHTYcli2rB5kzNYbxdv8menDOzxmks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=twhKT2wYTPtfn8pz0HXE3MeU_yKwAP4tHbDBnzrL22sPupmfy8UPMGgAnBMktVwJEzMm-yl_xvGfoo6BdVJXY-moS-RrAb0AR7M5kvxduVOckVDVYTqXyhwzGd93appAw_sNK7vMq-cer0rzoTTJh2LWG7H0s0KKgTBNegTqdzazTWNdy-ytcjoGwD6Herx5CXZy8xS29DNA1ZH7krZahSGZWhNpQSYPTh4mRHpaxnXwbLC3jDvaQjfHf1zYedcjjyX0d3HTTt-DoJrkn2UnVWV1kKycMV2FjxOO7AxEKUUzaMnQmtcLMt6EuUj97NGboLZE0YBXY1u6HniKJR7Y0ojVniUemEtRKv0mmKXwexFASDHh5IfGgfs_aiizM-Wl6h2YLz78qNIdw5sjSxt4j9ZdalsWSGz8M8d809eX7arliKjwgnx6vmrun0_NRdU3IuAU6iB5IaQ-aWI50d-FwspvKxX8bXF5o9HgfuEwFbpW4y8xffJIVMmA31ZgvWAO3ssKqERz3gFMH99YgnWrP_OS5X3xs-ODjhaDyuKRcLEV-Ec893ypfwXhmgleOnUe_FwJR8DXoxwLh4hPZK3V_efuEnGr3dTsIMfIDV3EQS7_Bczxv1YcvPEvBPoTnVyiMtz3r5hTkRv8EEHTYcli2rB5kzNYbxdv8menDOzxmks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=EnMjkfOV8uKIwZDRDoR740vZZcRkU03ZDS3fCxO2EVYMXEb9xT_c1kOWryke6YfEFICJedk-htiRTui55K9h_MPRp888s_1hblcXKEzLWgJ3CTNLyOUtN3uY0mcEqIRuMGZQn6oI3hGApGGUb7L2dLyrdDooaQ0r8sHIjrIP3WecO9NqqFrE_5bO-wSF9L5gnoJnjtnzUAfqambqKzqtU8ZWetkcMdlezRKJOESJ9U37sZYkiwX-Bcf4HVlrO1RFEDxUpb2JDobV_hIf2gg2WVMksP1DBNSIpH2oHLa3rFw7fPpMgEeveHApqyJADTxH4NEc21UScRxzlyL1LvM1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=EnMjkfOV8uKIwZDRDoR740vZZcRkU03ZDS3fCxO2EVYMXEb9xT_c1kOWryke6YfEFICJedk-htiRTui55K9h_MPRp888s_1hblcXKEzLWgJ3CTNLyOUtN3uY0mcEqIRuMGZQn6oI3hGApGGUb7L2dLyrdDooaQ0r8sHIjrIP3WecO9NqqFrE_5bO-wSF9L5gnoJnjtnzUAfqambqKzqtU8ZWetkcMdlezRKJOESJ9U37sZYkiwX-Bcf4HVlrO1RFEDxUpb2JDobV_hIf2gg2WVMksP1DBNSIpH2oHLa3rFw7fPpMgEeveHApqyJADTxH4NEc21UScRxzlyL1LvM1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=CcR0L3YttqrzdHXj-ZB74NGKGOB7wbwfQozPR6Rm_eFHXWp5t-ZSpbTj41EvSdvUB7kTYYeut39N_nqcXa3_016GEokhiT7525iSpnPlhncsTnxZSWzhzACgQun4AUtRJQbIAkukq0SeY1Pgb52CaukwPH2YKvTnSM26tT6wKtZDoqhF1dyLYe24aCqryA9LBsams0oFB499ygZj57HKnHVYm9k0uojWtgs0NEG9rr_RvehxN_hQL5PbTNt7EgslskRni2zmIJ4iiV6Sh4UUb5XvrDz9f8jMMFhCTABSguJ6oCWSN-DZA15ONt_VDh5d1pYNOqKkUuuB5WzVWzwz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=CcR0L3YttqrzdHXj-ZB74NGKGOB7wbwfQozPR6Rm_eFHXWp5t-ZSpbTj41EvSdvUB7kTYYeut39N_nqcXa3_016GEokhiT7525iSpnPlhncsTnxZSWzhzACgQun4AUtRJQbIAkukq0SeY1Pgb52CaukwPH2YKvTnSM26tT6wKtZDoqhF1dyLYe24aCqryA9LBsams0oFB499ygZj57HKnHVYm9k0uojWtgs0NEG9rr_RvehxN_hQL5PbTNt7EgslskRni2zmIJ4iiV6Sh4UUb5XvrDz9f8jMMFhCTABSguJ6oCWSN-DZA15ONt_VDh5d1pYNOqKkUuuB5WzVWzwz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ty_ZejLV7W1uR6BKDohXfVwnWZBfobPSLyTw46bZTsy0c0bRqEaB9mpSt357GoPdb8P7lVwzfOlLicCIZsmJlkwDc3LRLRQ877AcLqImM0eFn2s1NQJs2vrNqI8AoEZKMBntDoVosYMg4m69Z9ElAmg8Z701YhZokWMi5-eZbi68UfIZkYTdzTzEkI4urTkYLO4wbBoGamMGZHtCb-1WCm_UVZqx8M2lMs9E2AAqF35xTZEuRtXSzpyDH4_0Pf9RIsS200t37JL9yh1JDuPQVyd_omhW4Kyts9Rn5F9FjrrGfG-Bp7JtznsZB-Rkvysz607Lr6T1K-0rUT_peQThaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ty_ZejLV7W1uR6BKDohXfVwnWZBfobPSLyTw46bZTsy0c0bRqEaB9mpSt357GoPdb8P7lVwzfOlLicCIZsmJlkwDc3LRLRQ877AcLqImM0eFn2s1NQJs2vrNqI8AoEZKMBntDoVosYMg4m69Z9ElAmg8Z701YhZokWMi5-eZbi68UfIZkYTdzTzEkI4urTkYLO4wbBoGamMGZHtCb-1WCm_UVZqx8M2lMs9E2AAqF35xTZEuRtXSzpyDH4_0Pf9RIsS200t37JL9yh1JDuPQVyd_omhW4Kyts9Rn5F9FjrrGfG-Bp7JtznsZB-Rkvysz607Lr6T1K-0rUT_peQThaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=HVioEBhJ6eRKJcUuTYzrnJZkhsM7CE_zFl4s1BglcbzDc1lVCKjVCziB5jU88mkWNJVxP95vnYsxRg2YntioBZMXXKpdHvFfI-3qmU2snx36mhP5T4axRGYaDhmGXcSboy1eI_uGkHJKn4nEpQb4C4_cIHdate5kwLwEtFCwAnSBY4qHJPcKx3fBDMwhBqJmpXPyjoMsINIgTn9Oyk7o9m2cFyX8ST-5DmmBPHYFWWWtrbPQwbBi_QEzZn13jM4vRtwtoagooX3jtexx9TknbmrpbsUSv6tBfDONGp1TabhZvL8ut0wv5DsoN-ZJKdAZMb-MocdaNYv7RuBcc4Ar4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=HVioEBhJ6eRKJcUuTYzrnJZkhsM7CE_zFl4s1BglcbzDc1lVCKjVCziB5jU88mkWNJVxP95vnYsxRg2YntioBZMXXKpdHvFfI-3qmU2snx36mhP5T4axRGYaDhmGXcSboy1eI_uGkHJKn4nEpQb4C4_cIHdate5kwLwEtFCwAnSBY4qHJPcKx3fBDMwhBqJmpXPyjoMsINIgTn9Oyk7o9m2cFyX8ST-5DmmBPHYFWWWtrbPQwbBi_QEzZn13jM4vRtwtoagooX3jtexx9TknbmrpbsUSv6tBfDONGp1TabhZvL8ut0wv5DsoN-ZJKdAZMb-MocdaNYv7RuBcc4Ar4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=uF457SNvvCcs7GzJux30tuBGe7ePTUrPY8OU_IJoLPlr5ZsZ-xMlxigvZcD5ehRMwko5EFsmH0t-p3MInMY-2DEF_e1tWKLqRcWGNCn-lKtnmiT7sVP_xkuLSKx8GaR9yq8X-DQIKmxbZueugmVD5-vBy8omrO7knKbwsAzzx3FuJ0RVyM_EizqYne-l_G3gcqFe3hcXQHS0Z8UYz1mgdGPl1M9q4JPg2FNkmww2GCmt8gtox6SD9ACbN_HBPpYzlS8DdfegMGISNchcwZy1cU4h8n_fL2Mdwbq1ZrZtCZgcD_UXtfjtz_2BxtZS0cL8aaFwwLpd4DotGrI-ZJiBfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=uF457SNvvCcs7GzJux30tuBGe7ePTUrPY8OU_IJoLPlr5ZsZ-xMlxigvZcD5ehRMwko5EFsmH0t-p3MInMY-2DEF_e1tWKLqRcWGNCn-lKtnmiT7sVP_xkuLSKx8GaR9yq8X-DQIKmxbZueugmVD5-vBy8omrO7knKbwsAzzx3FuJ0RVyM_EizqYne-l_G3gcqFe3hcXQHS0Z8UYz1mgdGPl1M9q4JPg2FNkmww2GCmt8gtox6SD9ACbN_HBPpYzlS8DdfegMGISNchcwZy1cU4h8n_fL2Mdwbq1ZrZtCZgcD_UXtfjtz_2BxtZS0cL8aaFwwLpd4DotGrI-ZJiBfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Z1pgivJl96n7FJ4uqdm4Zh6_tAD8N7cjqc9GJaaXYZTWXva_Q7xmlN4qcBNIUIilPu3a1xCsM2nkj5qO7aa_LMrVhvNruDixS4XpcYo1G3Bf8cC5BxD-ZpikzJi7G5WCKSAYhsjogPOAddD0xlG3Qw6xQhBZ_63SBleIC0kdmlxhdmaryTDNLON2mhcQiid7jp8YOCH96vMrP6Lp7VyvBj13nA0c2fq_yFcFB16m78XWEWXvNOMVncVnn0wmL8axQHDwXqma8MO28Mrmx-HwPN9I5cQ0KwnW6S3gUOUwB1Y5H-MshKCf9A98SwRiLOgl0zjsCnHVNvYR9jg4icZTTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Z1pgivJl96n7FJ4uqdm4Zh6_tAD8N7cjqc9GJaaXYZTWXva_Q7xmlN4qcBNIUIilPu3a1xCsM2nkj5qO7aa_LMrVhvNruDixS4XpcYo1G3Bf8cC5BxD-ZpikzJi7G5WCKSAYhsjogPOAddD0xlG3Qw6xQhBZ_63SBleIC0kdmlxhdmaryTDNLON2mhcQiid7jp8YOCH96vMrP6Lp7VyvBj13nA0c2fq_yFcFB16m78XWEWXvNOMVncVnn0wmL8axQHDwXqma8MO28Mrmx-HwPN9I5cQ0KwnW6S3gUOUwB1Y5H-MshKCf9A98SwRiLOgl0zjsCnHVNvYR9jg4icZTTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=aqPh_A909o8-3eB2cqqkoKvyaCSJnSgl4hOYRvUEdqhQaTpY-gBAdFIGnq84QFiwlCI57g1deK-lvSPrrj-ttSBGMXUUzM13tecJS0ImuR0f64NYr-qDqjevNUt0hlOmQ4f5MwTA7uZPC24Z45MvibWv9HXGBgw5G6QNpuIaVcbK0YF5F63bjEx1U4i-FwvPxihqgxnonbtXmQydBvOZZpE52-lzxZs6wWfx8DISeMNMeYK9q4Yr5EbXD4Bg-VWa9BdCI7xwmV9wh6y6HlTR3JtZ2JcMyBt5LuP4zqVTEZ8eA-5esSgf3XTYV8wbkTTB250NT7mnTRW6RXRNvi5N5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=aqPh_A909o8-3eB2cqqkoKvyaCSJnSgl4hOYRvUEdqhQaTpY-gBAdFIGnq84QFiwlCI57g1deK-lvSPrrj-ttSBGMXUUzM13tecJS0ImuR0f64NYr-qDqjevNUt0hlOmQ4f5MwTA7uZPC24Z45MvibWv9HXGBgw5G6QNpuIaVcbK0YF5F63bjEx1U4i-FwvPxihqgxnonbtXmQydBvOZZpE52-lzxZs6wWfx8DISeMNMeYK9q4Yr5EbXD4Bg-VWa9BdCI7xwmV9wh6y6HlTR3JtZ2JcMyBt5LuP4zqVTEZ8eA-5esSgf3XTYV8wbkTTB250NT7mnTRW6RXRNvi5N5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOrohyyYLkEzaIBH9XmDh5o16QDZgb1hIB12kw9Pr84_mCXR5wk_QzhXSre-5NGyZc66rlMlXFur909Zy-TZZzt2h0t13TWmD6pkRTHkKaPsiJrx5uM_Q1F5x50npseLXbpRlfAiDUwRQ0G5wJJ0JdNjY8nnGjZpnEcAJtCxXfj6kLyybXmix67uC5DGUz08rJaMUZ47czcXNsOBZaQWs9cVD1RrQK6B2cd8hK0hhGY6-f_gAjTyL7F5eVHTrWDmsvW87TYKgBm32oAZ7qZlafqCMJgxSn7Y8n7ZS9ILACMqzEP-Ch-1eb5pF0FPOgQBA_p6o3bXzIjgpYSWfGuqog.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Qn7ZeZt8fsvtNQWEUpChlHjqhuuMijI4wMurSVaFmVC5u2JrXyz4Ilj52Pqb4JshknNUIbY5zV-PwDwqrXIs3FE2B7i8zFYv11I2wgpPHs-gbGvA8hS7Iibrj11RtZFOqDiodFaGEPwkMfTHj9JVTHNffyRanxx8MIW-nWCFaR1jKd9GX5rHgS-kSVwMtvlTWe-PpHmmnlCXU_13KpZc1TuJ2puIVDoFT6URvMC_D6_CKlacY4xBI7virC8tEf87J7-bWEjz81tT9wmUbZD0nPC489PVMMobz4r2cOLf5K8s3jYGkk5rb-T9HZnGtRKiRcHhaUdkQ_H3duE5tuewjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Qn7ZeZt8fsvtNQWEUpChlHjqhuuMijI4wMurSVaFmVC5u2JrXyz4Ilj52Pqb4JshknNUIbY5zV-PwDwqrXIs3FE2B7i8zFYv11I2wgpPHs-gbGvA8hS7Iibrj11RtZFOqDiodFaGEPwkMfTHj9JVTHNffyRanxx8MIW-nWCFaR1jKd9GX5rHgS-kSVwMtvlTWe-PpHmmnlCXU_13KpZc1TuJ2puIVDoFT6URvMC_D6_CKlacY4xBI7virC8tEf87J7-bWEjz81tT9wmUbZD0nPC489PVMMobz4r2cOLf5K8s3jYGkk5rb-T9HZnGtRKiRcHhaUdkQ_H3duE5tuewjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=dRFPVGqHA5x9ggAQbXQfjmlwEQi4v4YBvAJV9lR61FwpRmSK_vss786UIZ6WFnjPVMuOsP_u1E3WMLhPXNVPfvsZq-oy_glBWJimqWGat0PxEub1zbwZKiztddKfDTx74oFxNnZO18P_6bqkhK2rG_gY4yagBGJ6OaH4AljB8or-6u40gNauiukJo9LqdUD-Jel1FWhbn0oQdKGwF_zC82qSAUTvaOUeCr-m0K5faqCEGsTUlvpHZRyq8obE9p0SdYgnJuWJqfgg9vxavH25Fp7mmDkOYwqUeSg-liWsbAFxvdZKGGZRxvaeAz1ke7O-GqaIObP54YTg14XQQ-RImw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=dRFPVGqHA5x9ggAQbXQfjmlwEQi4v4YBvAJV9lR61FwpRmSK_vss786UIZ6WFnjPVMuOsP_u1E3WMLhPXNVPfvsZq-oy_glBWJimqWGat0PxEub1zbwZKiztddKfDTx74oFxNnZO18P_6bqkhK2rG_gY4yagBGJ6OaH4AljB8or-6u40gNauiukJo9LqdUD-Jel1FWhbn0oQdKGwF_zC82qSAUTvaOUeCr-m0K5faqCEGsTUlvpHZRyq8obE9p0SdYgnJuWJqfgg9vxavH25Fp7mmDkOYwqUeSg-liWsbAFxvdZKGGZRxvaeAz1ke7O-GqaIObP54YTg14XQQ-RImw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oeQAevQ5ZL-tDT8XPQJii6DkX32BVKkWQLovOYnzqn8Dh1fdf_F4Wvm2S-3y5lUYdonVBJGl0v9ligP2O5ymcCdXHd9_TOldg__GJzbf8ORzdad5SVhd-BV2tQMXhW661yPqvYvMINUB3BS6MOdxgXs4TG2ZIAqB0uLl2iN3qbCmO2lQDvOcmjSzrKps4Z7fCLF1zP7R0IBYVKROV8mmqw-mfPXvcjw17TvQNQDbcn70hGbrhzLSfs3CaPCGFYgV7eleyuCzFtdLEPwmsk-yAJKwOCjULvfAZCG9Gdr7Hl8X5XDacR46fnPJz6RPvc0jDMjYd-WglAPYJM-6SNKKfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oeQAevQ5ZL-tDT8XPQJii6DkX32BVKkWQLovOYnzqn8Dh1fdf_F4Wvm2S-3y5lUYdonVBJGl0v9ligP2O5ymcCdXHd9_TOldg__GJzbf8ORzdad5SVhd-BV2tQMXhW661yPqvYvMINUB3BS6MOdxgXs4TG2ZIAqB0uLl2iN3qbCmO2lQDvOcmjSzrKps4Z7fCLF1zP7R0IBYVKROV8mmqw-mfPXvcjw17TvQNQDbcn70hGbrhzLSfs3CaPCGFYgV7eleyuCzFtdLEPwmsk-yAJKwOCjULvfAZCG9Gdr7Hl8X5XDacR46fnPJz6RPvc0jDMjYd-WglAPYJM-6SNKKfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=o5mGh_Rmosg2rAQi6uGXdtCuwndtTJQb6j_sjMicV4P2cg6zGUQYAg0L6hppjDDbKbxtF6nELMcVt2RHVw59Pt1zh79usPTbM3tbqHaLfHz9hlkOgVamQsi5JS9dm2RbTLt3ATyyg0IDPX2snV7wsArZDT8nlb92dDvw1Tv7zYlEpDggMBr6x5Y08-359LWkitzbHJxa0ah40j1svVO2lrgDxxxwryP6SeXZQZqfGuHSc7i_5jgqsrx71JB-AhPEQWqymDehMxgfnaciY8ABFAx7gDGwoIR1u5xmNLQxiJTdzkXuRcuXdcNFY5HOaK-zhKRAp207PhS50EE4SZitUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=o5mGh_Rmosg2rAQi6uGXdtCuwndtTJQb6j_sjMicV4P2cg6zGUQYAg0L6hppjDDbKbxtF6nELMcVt2RHVw59Pt1zh79usPTbM3tbqHaLfHz9hlkOgVamQsi5JS9dm2RbTLt3ATyyg0IDPX2snV7wsArZDT8nlb92dDvw1Tv7zYlEpDggMBr6x5Y08-359LWkitzbHJxa0ah40j1svVO2lrgDxxxwryP6SeXZQZqfGuHSc7i_5jgqsrx71JB-AhPEQWqymDehMxgfnaciY8ABFAx7gDGwoIR1u5xmNLQxiJTdzkXuRcuXdcNFY5HOaK-zhKRAp207PhS50EE4SZitUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZOAAckgMvPkLoo2MlRr0w8_ce36gEhTYEK6Qgm9eoc1Xda_75zGGW2fRO19hk3qyU1crtF63qKBiMoUV1PZ9utGDmhknKG95F0W9WHjr5XOu3f4H7iQ-AZADw4rXaIKL8QZGLiuWhkzhcn7gs9-AUdaMoHP5GOnmW-xwgqBZxYSE8_fCBx8gbV2VbipUa8jeWacAj-3jhQ8Irc3k9ByGf5q_m1bxmaRySl3Hu4hkxFxaUl3rN8L7CEdets-pPGAApeC9WnUoi2-eXpN5I5h7CsyPIJV9uw7zMoSnszpz-zuVnBu5ry2THnATMILmI8CnBKRu-KG3w6KXlR5GWQXHQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=nLW-q2lyl8Y3Bw996xl4_2llHbRKN2YDDjHA54MPLT6FIUCyM9-lkpPFdSs3oQMrtOluHIv8qWiLZOU8WARHmtiFqUHVz9wv7vf2e5k-sJotAJuFseaIX47yChJnkPjL8IIlW9sbsTf-oEV6dhT5zuQA-F2buXfgPaSJV2zHD_4b01eeou1kzUcH2Lp8FJVnh8DY518RWnrrARZkxfqCtcWjOsU9tXDelMQ-GywPcwuiEJyBiDNyYOhSHXop26lgkB7vf7ovLEjjP0rKEW8tL5E_GWWCtgYw56Lt3adMXSff1x5GgMJMtpdxN4FstItgiTCUcDdVsQz9y_wbDZvXDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=nLW-q2lyl8Y3Bw996xl4_2llHbRKN2YDDjHA54MPLT6FIUCyM9-lkpPFdSs3oQMrtOluHIv8qWiLZOU8WARHmtiFqUHVz9wv7vf2e5k-sJotAJuFseaIX47yChJnkPjL8IIlW9sbsTf-oEV6dhT5zuQA-F2buXfgPaSJV2zHD_4b01eeou1kzUcH2Lp8FJVnh8DY518RWnrrARZkxfqCtcWjOsU9tXDelMQ-GywPcwuiEJyBiDNyYOhSHXop26lgkB7vf7ovLEjjP0rKEW8tL5E_GWWCtgYw56Lt3adMXSff1x5GgMJMtpdxN4FstItgiTCUcDdVsQz9y_wbDZvXDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=h_uFSytB958tbvE-iKTT3YFCQNhPXJaQjEUeO9RMo5XlR_uYVKJbODxWXBgzWSO_pWnjZgta8d7nFgJeVRg3_Y_L6NaEYvGKfVeLz5h6PQWk-8YDpi1MBhTwaSVPTjpI5JDCMMGPJJIr5g0eRNHlp5pSKU1aOl73QY3gBC9Xk4HthuYR8sB1qExdavSooXNmxasRPGirw8RbKwmLrCCxK97YcYGWY1d8H9YPgpv_dKz1nM4AzNAgULlZWC89U8wLP7SDAc8a7-6JnTxBo-5DIoH5nC8MTuR-EaFWcP-W5T_X50S9msa-9xJuiRKMJRh9Drkj1TezGG-F5ta6N9kkPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=h_uFSytB958tbvE-iKTT3YFCQNhPXJaQjEUeO9RMo5XlR_uYVKJbODxWXBgzWSO_pWnjZgta8d7nFgJeVRg3_Y_L6NaEYvGKfVeLz5h6PQWk-8YDpi1MBhTwaSVPTjpI5JDCMMGPJJIr5g0eRNHlp5pSKU1aOl73QY3gBC9Xk4HthuYR8sB1qExdavSooXNmxasRPGirw8RbKwmLrCCxK97YcYGWY1d8H9YPgpv_dKz1nM4AzNAgULlZWC89U8wLP7SDAc8a7-6JnTxBo-5DIoH5nC8MTuR-EaFWcP-W5T_X50S9msa-9xJuiRKMJRh9Drkj1TezGG-F5ta6N9kkPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfszqMPOSfsygnodRec6Wplx9vj1GsxmIj0hNeDrjLwfXhPRI-9bR74SGzvOfdFIh_PusMHqAdhCwTHuth6IGpK_J8sUELsXGTbTgoIDni_kr7dhHf7WJ9vw6hfTqjaAXNOKwFw4TifkTBuhUYwQQ0a-ya8SiXWVdvyetqiipyrLkErICy0PDpvDPqERKqT7CS_WqVQQEdBMWx4S1Z5TBiTttBoYdhSCUeDRZubja-3CqkG2bwbyLgenecmNynal5GcZqpdxz8dgUvUGqWa7TD5ijlaTgTsOrmEutVt_kBOzgLXgJBdJqJXfbQejTwR0I0yC1dEjOfIk7S-t2JKsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSi4OTfwz9vmPBGnq_oQLgEBkuiRDwNsPsg-Jf4PB9FuKTBRYf-gQsD9eL_8kVLXjN_vMtJYGiavJT5OjcfjqkUYUU7MOlCcLuc5qDE0cM0s2DmHu4dK5OzXhU-hm-OOYO0STQ3F8E1UL6CgIG9o2B8ZDeuWOKAjc1N00IZ5-N0JTWJXYuMBdfy3PhBeHKgz_-IGrxc_efTEZFH-8y8wc6-3AYdgPswOtk48xqVBBz-owA-HI-g3SZP9rBfBpHLGgj24_u80ndE9JzMk1-7F7UJ4l0yVO5YElL4v3zFzdi0CEHbVAGbgPPuXZGlYAcmlvh76sBv6X599qgagb_Rj5A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=jVZI9uvXeSnRO1ai1dOZisdyGi_ekVwRH0Y6Tm-7PelZcUIIBN94Q_Ng52z3IcW06NUyIIMJH5wDx4NeEWWDeB_Hcctct2mVkP99VPFUGTSEByMpSWPRwd_SOFvRecu8_K5ssrT1Q29MbDfXtv7UIdkF5CHVYraWhUG-FNfak0v4Is8l_Q_j_ipdR9LbqJouzVZqf7FbdII-mfAUeYfophTbBJkqt70AJzh5m-taE6jSTZETD0NnXg_4bWSiK2yMnEemPqDNG9iXhVQ274-EWlXMzaF5wZ8jd3E2dDWD-idN_XY-L8O4R-KPDk1p3bu7tPoMgIrjU8FQLJXP2BCX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=jVZI9uvXeSnRO1ai1dOZisdyGi_ekVwRH0Y6Tm-7PelZcUIIBN94Q_Ng52z3IcW06NUyIIMJH5wDx4NeEWWDeB_Hcctct2mVkP99VPFUGTSEByMpSWPRwd_SOFvRecu8_K5ssrT1Q29MbDfXtv7UIdkF5CHVYraWhUG-FNfak0v4Is8l_Q_j_ipdR9LbqJouzVZqf7FbdII-mfAUeYfophTbBJkqt70AJzh5m-taE6jSTZETD0NnXg_4bWSiK2yMnEemPqDNG9iXhVQ274-EWlXMzaF5wZ8jd3E2dDWD-idN_XY-L8O4R-KPDk1p3bu7tPoMgIrjU8FQLJXP2BCX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXetAhiq7Zy8MrxyzBa3Gcv4A5ziM5pkF3rtgfNE94pdSzgazo2qxjFDvYZNBAc1NHUo43Y7Lbc6DBq4VtiHsKofmsJO_0t5kgKWMSQci-4L9FET7sMT6YJF70X-v2Z2qaIlaSnqa-wfgDveOtEjGiCcTt8QwwHy62CIIC2gj1jtj749dHrjHsyLyaFAcxOSsygjTWNeOP16E7FIJ79VL21IR_GE4UmN7mZkYGAGM_63dtJqFP_7SgKTxc9sTYE3mD83g-KC-xg50lkol_E7MA76hFU5PXm4yIQXswol7ukqlqhgFzArN-zWjgDOQb4HSjKbbcBLuXoe7ua2plCRgw.jpg" alt="photo" loading="lazy"/></div>
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
