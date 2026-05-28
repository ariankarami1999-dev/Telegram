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
<img src="https://cdn4.telesco.pe/file/RXqocQr2uIPH12uv7t5dB6IpwDGo_3TWNPIMVk9laTgBY2B-x6pQglUwecjjoCs8dr7tGge6K-O_ps14qKEuU1NNbS0oZOlmJpqglnZkRWJem91d8_GuZQFJVCJhbzbB9ZYZsYV0_-XBKTSriqX2qR_kb6_NLzMDDP2uSvFya2aCPmo7gNJz5sBWQS2huzOa2WfKvgiUScwWqayOhz-x3q9wm9MK9HasJWZqiJ_JXK75EVpiMXNPhXRmNOC-lq_j0_SXYCLLx5Kcg3GhqlzGDPZQpoYyNUGiArFjIy0w0I6P-soiHED9UNWHRzgkzGlrKeYmutaVRP7BnVYndPtAxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.98M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 10:05:14</div>
<hr>

<div class="tg-post" id="msg-654428">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379afc78bc.mp4?token=DYHxj_BBgaI1q4vEfVDtnYlzCFwBkgA5uCUqpp5R7eok3PzwEJhdTQ0jjU4cSNLigRJyprp3E0KbGU38ISpxryGGPWbeS1XUmskvJ9KEZKQhCRDmAVCR6gtqz-fwFyGdqcKU3u7hyIzhdFyJhudh3JsK3Ct41LX5LaUdq3KGpcddhtRnmU2lidX_izSAjvZqDRZj-0liVFRyk911zm3SsG_RQxqY8C3MDMJQxMxxqp2ceN3Qf7WrsT9uUXu949ZMIO3GhMsqKqGgUQzEG4IH-DfkOvSV9Ao8KCkSj_VywC3eXu4XtmPeYhzG5w-X-PR8Z4O23UKdx4cWc7377L_loQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379afc78bc.mp4?token=DYHxj_BBgaI1q4vEfVDtnYlzCFwBkgA5uCUqpp5R7eok3PzwEJhdTQ0jjU4cSNLigRJyprp3E0KbGU38ISpxryGGPWbeS1XUmskvJ9KEZKQhCRDmAVCR6gtqz-fwFyGdqcKU3u7hyIzhdFyJhudh3JsK3Ct41LX5LaUdq3KGpcddhtRnmU2lidX_izSAjvZqDRZj-0liVFRyk911zm3SsG_RQxqY8C3MDMJQxMxxqp2ceN3Qf7WrsT9uUXu949ZMIO3GhMsqKqGgUQzEG4IH-DfkOvSV9Ao8KCkSj_VywC3eXu4XtmPeYhzG5w-X-PR8Z4O23UKdx4cWc7377L_loQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک دسر خوشمزه و مقوی برای بعد افطار که می‌تونه کلی انرژی بهتون بده  مواد لازم:
🔹
موز ۳-۲ عدد
🔹
شیر حدود ۱ لیوان
🔹
کنجد و پودر نارگیل
🔹
بستنی وانیلی و انبه ۲ عدد
🔹
خامه صبحانه ½ پاکت
🔹
پسته، بادوم، گردو
🔹
عسل ۲ ق م
🔹
خرما بدون هسته ۶ عدد #آشپزی @AkhbareFori…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/akhbarefori/654428" target="_blank">📅 09:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654425">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ig0W2Y04o7etzVqc-zGoSDbCDcOtc6NPn2KJhyTBPIPxUFDwC3VVrflI5JX_aEnEhBuSI8Phi34F-l9roJsHM8ioySHC3se4mmkZekgrhHxU52OI3nC5nDjnvdq8c_TfvKTZuz9JS34e0VnXMS6zSWdJ1HwcABkpeUrkmmbnxSB_t2ViX0g7D5sCS-xuH8nWsWEq2_cfNOnq8Har0W6zTQcJwvXm7C6vQVIbWqwDSklJWpLCvH-N45wrW0iKpgqV7uslP1ydRK7hSS_62pUg-2HxQO0g4LtgvzZXNSSikB9NZOI4x42yA0hez4XWqPE7iN-gS03AikTdhT3G8_NY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-KF2lG-L1SGH3AJJ58KARiwzzPXlj4X9m2j_Bm72UsLEifloY6YpSYZ7ba7jROsC_omZiZio2wMxIXqTBYsElljox7QDVbpykwWjRTB0_1lCGtH2aQRwpflnYhECtfmOP9D1I4IBd0IWVE_ZwB-hs5IfddEeHqvZceFPCchkMYFxT-qzrXs8uEwc74-QfoWstxCn9xBeSSOFFQQ29FHCjT0gynLwAxCYiG9-IDiOq-itOUP1NJRAIidZlJpHHOym3gx9n4_cGpVXw_a0QhcDcQ1GjyoBIMVuXIlVKrkOPQU6kzXQtuXYszBZPD8tk89RIAdnMR4_KDDxl0ciMVx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/car9ZYe0IVscsTsWIFt1AcT8z6CYeCFClBQsCdgUDwA6yYt7bUNCwbkTFYybxGxD8mw-nXKUyvLgj-ATQZeK2fTM_lbJ9E32jpWOIgg-OSi7MZSoTv3fkRn_Bv5zdUwQItXfslW30J4TV-WuDx7Z1s3Jol5ZfqlPNEFz_5oHU4bpSc2rbuWo09zlaBkM6laZ9oHS_A5Z1QdYl5u9vvnEM0Q5Gk5sh4sAi7Fa2DTh2Of3C9GjpznQeN1K5dLq2JWIYeiINae1Y2-zJwOHPizEDm94KYDSajL7HXW2ehlnKlNLTVNqwkq0F6XSxCA0GCOXAQYZ-wKk-tC9I-l_0itw4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اینستاگرام پلاس از راه رسید؛ قابلیت‌های ویژه با پرداخت ۳.۹۹ دلار در ماه
🔹
متا نسخه‌های پولی «پلاس» برای اینستاگرام، فیسبوک و واتس‌اپ را معرفی کرد.
🔹
این اشتراک‌ها با امکاناتی مثل آمار بیشتر، تم و شخصی‌سازی عرضه می‌شوند. قیمت اینستاگرام و فیسبوک پلاس ماهانه ۳.۹۹ دلار و واتس‌اپ پلاس ۲.۹۹ دلار است. همچنین متا روی اشتراک‌های جدید برای Meta AI هم کار می‌کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/654425" target="_blank">📅 09:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654424">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa3af3e65.mp4?token=JPU6PcChoMcPQTp6pcRW9EORknTorCaZW02Y6vic9Hmai8kq5LbvwNV-4rj-6mrnbUNX2hYrBdR5ZThH7AQkQZNfCJgQxbdQJjofoImNAK0UJYyzoMBfej0_WlP3go2pkwRRktUqSWw0oWxYpC6G25fR2mRraUU5xZdZqfIZBCoXtv-1Iu8PFmzciE9sv-b3_o0ubYyRshSmz-GUIdf_62gUyEt1_XRaWHWmyDXS0Ld7lhrnF04m3N25cGwDeZdBPzOuQ0r7DcGIxxwBBujrO7knQFdPXyvPe0InNaZJ1AQWFmlpa7SreqnnfFRZIZz2keQWTTvQd8zwzLfE5XobzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa3af3e65.mp4?token=JPU6PcChoMcPQTp6pcRW9EORknTorCaZW02Y6vic9Hmai8kq5LbvwNV-4rj-6mrnbUNX2hYrBdR5ZThH7AQkQZNfCJgQxbdQJjofoImNAK0UJYyzoMBfej0_WlP3go2pkwRRktUqSWw0oWxYpC6G25fR2mRraUU5xZdZqfIZBCoXtv-1Iu8PFmzciE9sv-b3_o0ubYyRshSmz-GUIdf_62gUyEt1_XRaWHWmyDXS0Ld7lhrnF04m3N25cGwDeZdBPzOuQ0r7DcGIxxwBBujrO7knQFdPXyvPe0InNaZJ1AQWFmlpa7SreqnnfFRZIZz2keQWTTvQd8zwzLfE5XobzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون - وضعیت تنگه هرمز
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/654424" target="_blank">📅 09:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654423">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb4864206.mp4?token=v5uH5nzQltU-weaL19mpG4943gQGhVNbWCsJBXH-y2CjYM3ogzuTYBzE73AaijTNT0bmypTq3GytnvByPDmyN67dgKb93Qc-cMdp_7-3Yx3M1wItUhfiSakqS9VNjm1BrQDuWFlZum6E3U1HM1nJCMhA81lfvLk2ygwvSRcmzukXh7r0LpmMwxW0XH4gd_W9incgqgFNEbf-Smb-Qq8XOJ31WEV7RkICLHEEREBVVXy8GPtWFGv4pDOdW8kiodvrtF1JM65ri3NshGtIqArpzcrriUNVM_eh-DiyCrFmJbd0hJnzsiqEQRRk507a3zgcDFVM-KwtA4uHnONMcHOC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb4864206.mp4?token=v5uH5nzQltU-weaL19mpG4943gQGhVNbWCsJBXH-y2CjYM3ogzuTYBzE73AaijTNT0bmypTq3GytnvByPDmyN67dgKb93Qc-cMdp_7-3Yx3M1wItUhfiSakqS9VNjm1BrQDuWFlZum6E3U1HM1nJCMhA81lfvLk2ygwvSRcmzukXh7r0LpmMwxW0XH4gd_W9incgqgFNEbf-Smb-Qq8XOJ31WEV7RkICLHEEREBVVXy8GPtWFGv4pDOdW8kiodvrtF1JM65ri3NshGtIqArpzcrriUNVM_eh-DiyCrFmJbd0hJnzsiqEQRRk507a3zgcDFVM-KwtA4uHnONMcHOC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جیل بایدن درباره آخرین مناظره جو بایدن با ترامپ: فکر کردم همسرم حین مناظره سکته کرد
🔹
جیل بایدن، بانوی اول سابق آمریکا درباره آخرین مناظره جو بایدن با دونالد ترامپ در انتخابات ۲۰۲۴ گفت که تا سر حد مرگ ترسید و فکر می‌کرد که شوهرش دچار سکته مغزی شده بود.
🔹
من ترسیده بودم، چون هرگز جو را قبل یا بعد از آن اینطور ندیده بودم. هرگز.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/654423" target="_blank">📅 09:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654422">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnSUXXAM4tDYOOKe3wo0zhvGEIcgdkAzNhnzhEXHBxqj4VsmKn9x6YlfmkoW4e3fbS7ziaU04vW8w8Up6cdKtQWOf__l_moFVH-OEdXgWpzHIs3C5qpYYmzDTxAhmb-QtOsskDrReilmDZZpdZ0-y23FUInGZrpNHhhNCV7p23wqVb2XCFNz5FQ4fvWzzRQsHyAmTuJOqP4sVVVGpEH_isDEoVMoMCXnAyM-EnkJBgb37RGzFLFO4s3lnQkOuEk7zQ9_6PyygAW7m3gAfvz49NgB-6ZcVAH3-iWAHlHu0O8sYc61saYf3LRJHOLLyFzpIcGoDw2EXvuNiWkYXAyr2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باقری: دارایی های ایران باید بدون قید و شرط آزاد شود
معاون دبیر شورای عالی امنیت ملی ایران:
🔹
به دنبال آزادسازی تمام دارایی‎های مسدودشده ایران توسط آمریکا هستیم و این حق قانونی ملت ایران است.
🔹
دارایی‌های ایران باید تماما و بدون قید و شرط به ایران بازگردانده شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/654422" target="_blank">📅 09:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تاج: از احتمال دعوت سردار آزمون اطلاعی ندارم
🔹
ما قطعا به مکزیک خواهیم رفت
🔹
قرار بود ما، فیفا، مکزیک و آمریکا این موضوع را با هم اعلام کنیم
🔹
باید ویزای آمریکا قطعا به ما بدهند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/654420" target="_blank">📅 08:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654418">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
تحرکات نظامی نفت را گران کرد
🔹
همزمان با برخی تحرکات نظامی بین ایران و آمریکا در تنگه هرمز، قیمت نفت برنت از مرز ۹۷ دلار گذشت.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/654418" target="_blank">📅 08:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654417">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908fba3964.mp4?token=iUUkgtuJdnTo2SVwmvhnVZYj0OkIzUhzfpMmDlqfERSKYPyHWGdKgtoRZTVoWzXgbs2iXrbJ1lGZsdHLBmZdKxVaQ9a1YXpynrR7dkR7AvxZUdPHSpGgxPqRTd0u9jcCwcR0OvJ1WHCRXlNUiBHguk5EKEDx5hTKWWnhEeheIESrr_dplUjV_V-Y4iUI-Ta1hzKAWHtatadgoZUdCHPDcvR9iiBh66mjSrJzBHv9mWXBIptup2UTX0Ze_NH9dmXvOL4LR5tQ7-hhJFmFp-MHuzSLKfilzwbMRO5maFAQSP_nZQvvG6K64-a1UNiKjIzoyGeizZi4eXq4oUIJh_aw8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908fba3964.mp4?token=iUUkgtuJdnTo2SVwmvhnVZYj0OkIzUhzfpMmDlqfERSKYPyHWGdKgtoRZTVoWzXgbs2iXrbJ1lGZsdHLBmZdKxVaQ9a1YXpynrR7dkR7AvxZUdPHSpGgxPqRTd0u9jcCwcR0OvJ1WHCRXlNUiBHguk5EKEDx5hTKWWnhEeheIESrr_dplUjV_V-Y4iUI-Ta1hzKAWHtatadgoZUdCHPDcvR9iiBh66mjSrJzBHv9mWXBIptup2UTX0Ze_NH9dmXvOL4LR5tQ7-hhJFmFp-MHuzSLKfilzwbMRO5maFAQSP_nZQvvG6K64-a1UNiKjIzoyGeizZi4eXq4oUIJh_aw8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات اصلاحی برای افتادگی شانه
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/654417" target="_blank">📅 08:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654416">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fea9bc79f.mp4?token=N4og7CdeSmGEoNZGkq6kE5qDiANLW25bdgW428FtihCxl7iDZUrxoY7DfOuLuRQAj8lvoFsTPWpkQd_ry6U59vSy6DrGzYMLsD13IzcqYKeQiRepR99vBF_Sq05M7KuppvEfD8MPZIThCSBGLp59m6AS-P8UxSFtD0oahmu3airtAhFukWnFxUFiuWpOgsbndgvwI8Wz3AT5qcLImZvcU66fNFIzFWBLiQF5HThuAEvfRMGIW63cgXpSihCBN2bQMTh_jrOkl8AJ99mBRVIjFENVucXeds8cpnFc9O6mGG8NfT6YPjL3Z4vGRACKYGlPUnW5iV2NTw55OLQtLZn7L10YBlcNcCZxd0h508foOY_7x1m73ykIWpskh4D8eRaBu1BDKPggw3nExamQ5iGUywQqNrauZRWd2HnCWJzZVeuT3zNOpDJGJe3WZVtZCDd0DfGLCJ0fN8AnzAGTmFxT89kXAqvGVqpPCdszmbFZ66OSsgcddHmNQewn55KwngDovKn85JQmd15Ch6pMcLrpYI1J48jPN1449ppdKxe4l-C7jcQ0XMxoP0ZgNd-JX_RuE9hy4PBKAY79wmzqNdsSvt7CHH8ldPiy3XojWaPieMBzLXHHIQh5HJWiav5imHxechlpRpbxrXHUarvq9HGX1gxL2rFvU9yBuqFxHtnpwL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fea9bc79f.mp4?token=N4og7CdeSmGEoNZGkq6kE5qDiANLW25bdgW428FtihCxl7iDZUrxoY7DfOuLuRQAj8lvoFsTPWpkQd_ry6U59vSy6DrGzYMLsD13IzcqYKeQiRepR99vBF_Sq05M7KuppvEfD8MPZIThCSBGLp59m6AS-P8UxSFtD0oahmu3airtAhFukWnFxUFiuWpOgsbndgvwI8Wz3AT5qcLImZvcU66fNFIzFWBLiQF5HThuAEvfRMGIW63cgXpSihCBN2bQMTh_jrOkl8AJ99mBRVIjFENVucXeds8cpnFc9O6mGG8NfT6YPjL3Z4vGRACKYGlPUnW5iV2NTw55OLQtLZn7L10YBlcNcCZxd0h508foOY_7x1m73ykIWpskh4D8eRaBu1BDKPggw3nExamQ5iGUywQqNrauZRWd2HnCWJzZVeuT3zNOpDJGJe3WZVtZCDd0DfGLCJ0fN8AnzAGTmFxT89kXAqvGVqpPCdszmbFZ66OSsgcddHmNQewn55KwngDovKn85JQmd15Ch6pMcLrpYI1J48jPN1449ppdKxe4l-C7jcQ0XMxoP0ZgNd-JX_RuE9hy4PBKAY79wmzqNdsSvt7CHH8ldPiy3XojWaPieMBzLXHHIQh5HJWiav5imHxechlpRpbxrXHUarvq9HGX1gxL2rFvU9yBuqFxHtnpwL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم ملی فرانسه این شکلی بازیکنان دعوت شده‌شون به جام جهانی رو معرفی کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/654416" target="_blank">📅 07:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654415">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2MFUY56ly73v-N1jZv-HhV3864rEuufXt-xFAJkwryEpH7n-n08gB23KdJ1Cflp8Xdn5CQCkESwzXUB36eJ0gvBfXtysVg8OHO0BWTcbXKkWSHEC5_ttCJ-cTWGwJiFm7uEZdCK6Cw5_zp28oazrnFIp8vRjT0wxF1jZPfUb4RMQh7Bdy3P2_vy6Gu8VBV31PTsZTxWNdcIs2JZUuj0isP9YWbar40GG11tk50I3hCscr3-rjvXQqpcfs4VDo0DVtUJt3UE_G2vOi8s9FClTE9M8XbHqNosknqXnCAgKpMIQXVhzSOMm_2aa9w9c26Jk3M1vCQ9Az9oCbYucU-_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهکارهای ساده برای کاهش هزینه‌های برق
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/654415" target="_blank">📅 07:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654414">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7fd8e750.mp4?token=fIjdI7E4XIpdi1DakAyIl0cHh0F9MLBcaEP1GRPNOBOlI8jHqHc4m87-jTDD3Jy7UQAoGRfmbpApzLa0MJjYbXm5TabV5ORvVfuXCI05J1l2eZJoQJ0ggNFIcIeveUtsF48w6PHcdb41Mpmdke31gMV_nasURWw27nCXDqR8nFGOfK020d4MjmmDWJhGcEoZ9_ZFz2WGFgJEFr9e0qgMDpiEG368shp8ZP8OOFXYDiqM0KpQrhct1f_nbWe9K5qS7TNyE9JvYhCD5AArHaooMFFQnWqLgsxDBQxUG01c7SJo2pP22o0nQ7LBdG_750JlA4THybxCjtLmaT-_1Pb7ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7fd8e750.mp4?token=fIjdI7E4XIpdi1DakAyIl0cHh0F9MLBcaEP1GRPNOBOlI8jHqHc4m87-jTDD3Jy7UQAoGRfmbpApzLa0MJjYbXm5TabV5ORvVfuXCI05J1l2eZJoQJ0ggNFIcIeveUtsF48w6PHcdb41Mpmdke31gMV_nasURWw27nCXDqR8nFGOfK020d4MjmmDWJhGcEoZ9_ZFz2WGFgJEFr9e0qgMDpiEG368shp8ZP8OOFXYDiqM0KpQrhct1f_nbWe9K5qS7TNyE9JvYhCD5AArHaooMFFQnWqLgsxDBQxUG01c7SJo2pP22o0nQ7LBdG_750JlA4THybxCjtLmaT-_1Pb7ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویرانی گسترده زیرساخت‌های شهری در اثر حملات هوایی اسرائیل به شهر صور لبنان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/654414" target="_blank">📅 07:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آمریکا تجاوز نظامی به بندرعباس را برعهده گرفت
رویترز به نقل از یک مقام آمریکایی نوشت:
🔹
ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگۀ هرمز محسوب می‌شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654413" target="_blank">📅 07:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
🔹
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیه فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.    روابط عمومی سپاه طی اطلاعیه‌ای:…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/654412" target="_blank">📅 07:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYD_FQrFEjVPwxHngCyWJraU0Yo9i2426YHmSd7iwPyRiVEast3SEnnC7C-_1VnzN6ocky3zl9YvNa2wKF9IDhkvB6Lb6AbXnxIeGVUGfP_h-7Ik5GgRxi3a9KghHyMYLAO5w5a1m8NXpHOPr7h2GxvxQHiUHOFaQoCFBYnJ5C04eqrvTH7FFXyvtz5ChPfBFIR9FMJvSUFyIL9KUTW5IATV8XEKZF6d88oREu6YkpfCNPbZsUdDDY4msWcXkfnGPf8Yzf5DJNj9bzjhrJX-TH87QIM3eFECqZFlIZutI6-vYdET-UuM7LFNAyH15mCJ_bhnSgxYsF9hOoBiZJiBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحرکات نظامی نفت را گران کرد
🔹
همزمان با برخی تحرکات نظامی بین ایران و آمریکا در تنگه هرمز، قیمت نفت برنت از مرز ۹۷ دلار گذشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/654411" target="_blank">📅 07:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
بیمه کامل معلمان مدارس غیردولتی اجباری شد
معاون وزیر آموزش‌ و پرورش:
🔹
با پیگیری‌های سه‌ساله در مجلس، مصوب شد که معلمان مدارس غیردولتی باید به‌صورت سی‌ساعته و با بیمۀ کامل در ۱۲ ماه سال تحت‌پوشش قرار بگیرند.
🔹
عدم رعایت این قانون تخلف محسوب می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/654410" target="_blank">📅 07:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRa0_pN-uAQxMFB6DLG4c6865nrZtPiyZT3HrmoW2FFBnTEal0_SBlkNyW3HQSs-MMZajSOkRk3EcG2Idb9GnGcnu9TRbz0JwhtM_7UD375xrg1Jv85hmpk6SteUi9DpdIfNrosO0fZrQhcUqz7DB2ldmidgFck_J1GPrpsT4X6mTltOLz_Ya5Gf4rBljGNlukt5KLFvQK0aA4-DU0kis1Yflc5-kdMah-ASoYLbPDmfQv6XMHVP_fN9H1a9tjGaNqMBjUA6FVlR5kAb6GmZ8Eww9BGHycNYlGjlNUzjcc75XHP7Or4wYp1Ksrgic-JT6EF3mHt16E-5ZJZPCD9rAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۱۰۰ دلاری قیمت طلا با تنش‌ نظامی بامدادی ایران و آمریکا
🔹
همزمان با تنش نظامی بامدادی در تنگه هرمز و تشدید نگرانی از رشد تورم و تیره شدن چشم انداز نرخ بهره در آمریکا، قیمت جهانی اونس طلا ۱۰۰ دلار کاهش یافت و به مرز ۴۴۰۰ دلار سقوط کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/654409" target="_blank">📅 07:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVjIoo1HwaCcDflJ5kx6OkGoMnK3mBS0e7IjibwhKG3qagrRHeSzx67fTB8YIPj2mfZSRzf5i8y4WkgTU25o6T4bbsjQutF6lAeN-2RyTpW6K9go8gqlwLprzrgSgm9dgP1L5oR8_tGqDSwP62KH_Rv5tShPXnao4hv5qEVxYgZFlkWuSbEXPRDxdqTuZKjGNNOhgqxZ3jYn9Gowh7Sl3xVnz14cmEHlf-rr-JsfGc68e9vpZM0Llq8Ap7hg62IPyVxLNWByJ_ukV0lPO58fcYf2tBatpTbZyurn1GAU9CLIkBSd1tI1Hrbe02agl6ECpgaIAFgM6V_GOecRYUww8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۷ خرداد ماه
۱۱ ذی‌الحجه ۱۴۴۷
۲۸ می ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/654408" target="_blank">📅 07:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654406">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست
🔹
پیگیری‌ها برای مشخص شدن آن ادامه دارد
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد
🔹
اخبار تکمیلی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/654406" target="_blank">📅 06:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654405">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آمریکا «نهاد مدیریت آبراه خلیج فارس» را تحریم کرد
🔹
وزارت خزانه‌داری آمریکا اعلام کرد سازمان تازه تأسیس ایرانی «نهاد مدیریت آبراه خلیج فارس» را به فهرست تحریم‌های خود اضافه کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/654405" target="_blank">📅 06:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654404">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
کویت: پدافند هوایی در حال رهگیری حملات موشکی و پهپادی است
🔹
خبرگزاری رسمی کویت و ستاد کل ارتش این کشور اعلام کردند سامانه‌های پدافند هوایی در حال رهگیری حملات موشکی و پهپادی هستند.
🔹
ستاد کل ارتش کویت: صدای انفجارها ناشی از رهگیری حملات دشمن توسط سامانه‌های پدافند هوایی است. جزئیات بیشتری درباره منشأ حملات و خسارات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/654404" target="_blank">📅 06:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654403">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست
🔹
پیگیری‌ها برای مشخص شدن آن ادامه دارد
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد
🔹
اخبار تکمیلی متعاقبا منتشر می‌شود.
جزییات بیشتر
👇
khabarfoori.com/fa/tiny/news-3218404</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/654403" target="_blank">📅 02:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654402">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
برخی کاربران از رفع فیلتر گوگل پلی و اپ استور خبر می‌دهند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/654402" target="_blank">📅 01:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
روزنامه یدیعوت احارانوت: نمی‌توان حزب‌الله را نابود کرد، جز زمانی که اسرائیل خود را آماده سال‌ها جنگ بکند، تمامی نیروهای ذخیره را به کار بگیرد و تمامی لبنان را اشغال کند
📲
‌
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/654400" target="_blank">📅 01:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ایران و عمان درباره سازوکار جدید مدیریت تردد کشتی‌ها در تنگه هرمز گفتگو می‌کنند
‌
🔹
علی باقری کنی، معاون دبیر شورای عالی امنیت ملی ایران، اعلام کرد که ایران و عمان در حال رایزنی‌های مشترک در مورد سازوکار جدیدی برای تنظیم و مدیریت تردد کشتی‌ها از طریق تنگه هرمز هستند.
📲
‌
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/654399" target="_blank">📅 00:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654398">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Toey7EN5cqxSKaeV7bRUFOgJCdM-T9q6_jb3HPXa1f3QlWRn2E2TZBVghB3ApipU250DFT3L2fZU7Qns-Oyx5oa0X7vP0mhbNbWG2ETZZwtzSk-hqOl0NHPl73cAbemU-JFKe-qAZeJPJ0Kww55qlU0TLCdsvY-nxhZMY7wkNdYU-jfjqtxhFomWhnmfP9ExrZeRsM5Xv-p3imVtQxNZLYlfwlI_xx_HH7CqcuPE7U6JWL2Y4rYKg2YonKYbpRYZXeD6-UDcR-5AXf6d1MrCN7RN1yzTzt9jgNgK6s_e93mWl9qGOdt_m8jQfN_f3bdZrnY2KHOiSuhKxEloJxiewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت آلومینیوم به بیشترین میزان در ۴ سال اخیر رسیده
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/654398" target="_blank">📅 00:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654397">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: ایران از خطوط قرمز خود در مذاکرات کوتاه نخواهد آمد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/654397" target="_blank">📅 00:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654396">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه _ جلسه 58</div>
</div>
<a href="https://t.me/akhbarefori/654396" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وهشتم
رائفی‌پور:
🔹
0:03:40 تشخیص حق از باطل ویژگی بارز مؤمن است
🔹
0:14:10 هدیه خداوند به حضرت موسی
🔹
0:20:40 تحت تأثیر بودن صحابه پیامبر نسبت به اندیشه یهود
🔹
0:33:20 طریق صحیح وضو گرفتن در سوره ی مائده
🔹
0:40:00 آیات قران در مورد ترسو بودن قوم پیامبر(ص)
🔹
0:55:40 قابل درک بودن نشانه های ظهور برای اهل خرد
🔹
1:00:50 دشمن اصلی امام زمان(عج)
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/654396" target="_blank">📅 00:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654395">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ارتش رژیم صهیونیستی مدعی ترور ۲ فرمانده دیگر حماس شد
‌
🔹
رسانه‌های رژیم صهیونیستی هم ادعا کردند که این حمله با هدف ترور عزالدین بیک فرمانده تیپ شمال و عماد أسلیم فرمانده تیپ زیتون و تیپ غزه حماس انجام شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/654395" target="_blank">📅 00:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654393">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LobkJGw2CyHGIDVqCBG9FOM89W0cQ7LUWjtFULXBIYRIVVyqMwnxK_4GYwQgeBoGPD9m1mbqh9S4wYalvaFfGNKCAhAN6LFhwJzUqyW_ADc-OnivUML6MVuOeWBQeMAk9dMOeLBVKDLeLkj6mfpxK7hCmGOwPIhsEkHBYs7PAXP8hVFqLRlqxyfpMSuYWjDzGvcafjTYij2bFKOl4vOU4ODmNGcKQi9RZm14biD7Zps6lJFhODR5vqXpQzwkBN52qyUF2-jZ_VVi7ioFjNhme1t6fIYcE9AgAliG3p5CNjSf1QwlIX6PjORpjlTSL7_SZBB9JQgXFoXrdnVbhqneEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه سناتور آمریکایی به ترامپ:رئیس‌جمهور به جای رسیدگی به امور کشور میلیاردها دلار برای جنگ‌های بی‌پایان هزینه‌ می‌کند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/654393" target="_blank">📅 00:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfiY1PEFYn9vp7gPZB6d6vTGofIblARAz-S5JXds5cR4NR0jjVvpwO2eqfHXrZ7SDfFgRCv53Csjz-j7a4o0ptwI5QpqH5wGVhj8Yjow2DEyXuh7TnpKKijHwWNoAan06LDrlXt2USnLZtHSgxwFQknA-r-LsmGklQn4xh45WjvLne925N5quu-jM70j9MhsH1R6n3XYByxSvc90Ar7z6XcwfkbppDmEsx_Ta5KIXSdJHj1vgBwqJInOPcavgOXh9aBZne8AvqmB3Ki-jl0xc7FAhDmZoPpJ7JNz9QLqMIpyPWZIU-WNG00p_hJPFIYrP-MiqZtiRqwrRt80Fi6ysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منتظر طلوع «ماه آبی» باشید
🔹
ماه در روزهای ۹ و ۱۰ خرداد ۱۴۰۵ به بدر کامل می‌رسد و پدیده «ماه آبی» رخ می‌دهد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/654392" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
موافقت ضمنی چین با دریافت عوارض در تنگه هرمز
رسانه (Responsible Statecraft):
🔹
چین اگرچه ترجیح می‌دهد هیچ عوارضی دریافت نشود، اما با سازوکاری منطقه‌ای تحت عنوان «هزینه مدیریت زیست‌محیطی» موافقت ضمنی دارد. فرمولی که حتی دولت ترامپ هم می‌تواند آن را بپذیرد.
🔹
امارات و بحرین بشدت مخالف هر ترتیبی هستند که به ایران وزن ژئوپلیتیکی بیشتری بدهد و خواستار بازگشت بمباران ایران توسط آمریکا هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/654390" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
برخی کاربران از رفع فیلتر گوگل پلی و اپ استور خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/654389" target="_blank">📅 23:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
عضو تیم رسانه‌ای نزدیک به هیئت مذاکراتی ایران: سفر قالیباف به قطر درباره آزادسازی ۱۲ میلیارد دلار از اموال بلوکه‌شده، موفقیت‌آمیز بود
🔹
براساس پیشرفت‌های فنی که در قطر رخ داد، قرار است بلافاصله پس از تایید تفاهم میان ایران و آمریکا بخشی از دارایی‌های بلوکه‌ شده ایران به‌صورت غیرقابل برگشت در دسترس بانک مرکزی قرار گیرد.
در بطن تفاهم ۱۴ ماده‌ای چند اقدام ملموس و عینی گنجانده شده که برخی از آن‌‌ها این موارد است:
🔹
در دسترس قرار گرفتن اموال بلوکه‌شده.
🔹
معافیت تحریم‌های نفتی، پتروشیمی و مشتقات آن.
🔹
رفع محاصره دریایی.
🔹
اگر این اقدامات توسط آمریکا انجام شود ما وارد مرحله دوم خواهیم شد و در غیر این صورت اساسا اعتمادی برای ورود به گام‌های بعدی نیست.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/654388" target="_blank">📅 23:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
خبرهای پُربازدید امروز خبرفوری را از دست ندهید
🔹
گزارش لحظه به لحظه از توافق ایران و آمریکا | ترامپ دوباره زیر میز زد!
👇
khabarfoori.com/fa/tiny/news-3218211
🔹
انتشار جزئیات اولیه جدید از چارچوب تفاهم احتمالی میان ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3218296
🔹
وحشت از اولتیماتوم مخفی ترامپ به ناتو | خروج جت‌ها، بمب‌افکن‌ها و تمام زیردریایی‌های آمریکا از اروپا
👇
khabarfoori.com/fa/tiny/news-3218203
🔹
پیش‌بینی بازار طلا | قیمت‌ها به کف رسید
👇
khabarfoori.com/fa/tiny/news-3218244
🔹
ادعای توقف رفع محدودیت‌های اینترنت | VPNها دیگر باز نخواهند شد؟
👇
khabarfoori.com/fa/tiny/news-3218350
🔻
ویدئوهای منتخب را در آپارات خبرفوری ببینید
🔻
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/654387" target="_blank">📅 23:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
آتلانتیک: ایران از جنگ بزرگ با آمریکا و اسرائیل «پیروز» بیرون می‌آید
نشریه آتلانتیک:
🔹
نه تنها ایران از حمله نظامی گسترده آمریکا و اسرائیل جان سالم به در می‌برد، بلکه با توافقی بسیار بهتر از هر آنچه قبل از جنگ به او پیشنهاد شده بود، از میدان خارج خواهد شد. مقامات ایرانی احساس می‌کنند که در این جنگ پیروز شده‌اند، یا حداقل آن را نباخته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/654386" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54437140ef.mp4?token=mFaxrXD8anR8E5o8fLj-66FtY9_q-AAoMv1iniTYcPVoiXFHkzqYLb5-Cim6Y8cy2ac8fPJCIoa0xQ5QemjRcrEdsXz8E28UqX7h3c8kraw4vph8XE3735-W7V9ZDp6LHt3x6BiCrE-mVa6NZskNlqdMXsxBjUESC5SNixSinWOXB3v562ROzl7goZ2Vc0iBHC-tF6kGoPlF4-iD9XC1DHrcrjrypAdWlWVERVLMnDqHyZytH_Ir6URep5QSxFPM7mPEnrvYIUzwqc7wrIWlZ1lWoDJybjv3ovhefaMyVqPylDYgQ8myb1gODxTBWwWoSUyztvHEoPfOvgMfKWD52Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54437140ef.mp4?token=mFaxrXD8anR8E5o8fLj-66FtY9_q-AAoMv1iniTYcPVoiXFHkzqYLb5-Cim6Y8cy2ac8fPJCIoa0xQ5QemjRcrEdsXz8E28UqX7h3c8kraw4vph8XE3735-W7V9ZDp6LHt3x6BiCrE-mVa6NZskNlqdMXsxBjUESC5SNixSinWOXB3v562ROzl7goZ2Vc0iBHC-tF6kGoPlF4-iD9XC1DHrcrjrypAdWlWVERVLMnDqHyZytH_Ir6URep5QSxFPM7mPEnrvYIUzwqc7wrIWlZ1lWoDJybjv3ovhefaMyVqPylDYgQ8myb1gODxTBWwWoSUyztvHEoPfOvgMfKWD52Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیدا یوسفی: در کارخانه پدرم روی شمش‌های طلا راه می‌رفتم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/654385" target="_blank">📅 23:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7c0d72db.mp4?token=FlrMBmfvAkFmF3mjs3EnNMiZif31alPObpp9-rSN4fOqg8xEATXxn__vTf6rhPu3daBE5iFEprG6_RWre83BmreRRmijBjRmShCX403YXcpK_hyElpm5XfTz-z27xVdjs564xOPEou9MyYnZsPkHiEWgWOVpua6DxK6yx11GeTgWWUV62vqF4FFeOfs_Ra1XJayHlaVJakn8uWE_6bzmBUu5J0H4iRKdDMSbHOAzOftIkowAdgQaCRvC9NUV8IpPIdLL3CP4W4wzX4Yn3eCjThdt7Wa5V2pHBDz6JkHa-NxwDdIXgJkqgvzyInKXnPGpll3PzXZaJ18s8ykMl6CDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7c0d72db.mp4?token=FlrMBmfvAkFmF3mjs3EnNMiZif31alPObpp9-rSN4fOqg8xEATXxn__vTf6rhPu3daBE5iFEprG6_RWre83BmreRRmijBjRmShCX403YXcpK_hyElpm5XfTz-z27xVdjs564xOPEou9MyYnZsPkHiEWgWOVpua6DxK6yx11GeTgWWUV62vqF4FFeOfs_Ra1XJayHlaVJakn8uWE_6bzmBUu5J0H4iRKdDMSbHOAzOftIkowAdgQaCRvC9NUV8IpPIdLL3CP4W4wzX4Yn3eCjThdt7Wa5V2pHBDz6JkHa-NxwDdIXgJkqgvzyInKXnPGpll3PzXZaJ18s8ykMl6CDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه رهگیری و شکار موشک کروز آمریکایی در آسمان کشور
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/654384" target="_blank">📅 23:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
کارشناس سیاسی نزدیک به تیم مذاکراتی: دسترسی به بخشی از منابع بلوکه‌ شده، یکی از شروط اصلی اجرای مراحل توافق عنوان شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/654383" target="_blank">📅 22:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bc27a3ce5.mp4?token=g8_Tu12JmTHKahBdySMbk9v84iTjQ-UPzelH7WXBk8nPKWKdDQ16jTYYu7rHOb_M8dUoGY-Fb4K-r5fWWVQpDMqG9W_Cj0oBjVdDuY61aUHuIa1luY3GRuVSei2XPYHpg0lwhr_ZrVzfLziZs0huJwju2L22NGpKNvajcBtNbYKbczRRg1jWrZUoNS8NvCEL06XKC2QmtpM0QkyK25ku0F6Cj0bdOnJH22b7sSGG54cax9s7wZ6f2mITc8n2JieZEMeu253fz9r0x7A4y0fdhIfcH36J-S3rWI7HHAr6M2ngt5jDINBePMlEJiWilMm6uEdvACUP9axuS0WCPuT7mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bc27a3ce5.mp4?token=g8_Tu12JmTHKahBdySMbk9v84iTjQ-UPzelH7WXBk8nPKWKdDQ16jTYYu7rHOb_M8dUoGY-Fb4K-r5fWWVQpDMqG9W_Cj0oBjVdDuY61aUHuIa1luY3GRuVSei2XPYHpg0lwhr_ZrVzfLziZs0huJwju2L22NGpKNvajcBtNbYKbczRRg1jWrZUoNS8NvCEL06XKC2QmtpM0QkyK25ku0F6Cj0bdOnJH22b7sSGG54cax9s7wZ6f2mITc8n2JieZEMeu253fz9r0x7A4y0fdhIfcH36J-S3rWI7HHAr6M2ngt5jDINBePMlEJiWilMm6uEdvACUP9axuS0WCPuT7mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود جالب ستاره برزیلی به سبک فیلم‌های هالیوودی؛ نیمار با هلیکوپتر شخصی خودش به اردوی تیم ملی برزیل اضافه شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/654382" target="_blank">📅 22:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhPm2s0lG200sdK6Zyorlndx-_eeaGhjP9s2n_EQymBIHqArgYlrVpsvG3U4XrqfwoQEECRDQnASfispMMH_usjOLSNq6dzTtJLCNdvlPlWsUvk635aEix2-k3KPm4pYXCvr4vygvXGJC5mqcEMmy7lqFX0cQSyGG5-ZZXwFp-XEbXdm5svXJfRHHaQ9cEsx_s5c0AA4Uq7Ku-CIk9O6My4L_dI_V8_dTwCkVXEiSzDq-TxSrsOBp3PdaV1TUYPBRXfyybkZMdrTqRjj1EBa1bvgZKSFoPYD04blgSz20M4PyMy5wOtLQ6d8IzQ9J8vTSZnxB_RWg6HBn2L8y-wbxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر نظامی، داگلاس مک‌گرگور: ترامپ تهدید به انفجار عمان کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/654381" target="_blank">📅 22:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وزیر امور خارجه آمریکا: طی روزهای آتی میزان پیشرفت در گفت‌وگوها با ایران را ارزیابی خواهیم کرد
🔹
توافقی وجود دارد که می‌توان به آن دست یافت و ما خواهان تحقق آن هستیم. فکر می‌کنم مقداری پیشرفت و تمایل مشاهده شده
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/654380" target="_blank">📅 22:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-DI_Iv9KyktEXfe48qP5AjG5o6RXKKaE-Hdy8rsgHfIPBM6C0oASLxsFPtzXImadFhWtbsYD2MV4n7AsCAfufhLfmhTJrIjh0ltEQ5Q0Bc_SuJYWpYWh1uSTPU_8cKcokTRBVfYSHT_o33sfGiqEABtG1LBncE6S0JsrI0baeSj23H2-kPOBfNJ9eyRXqZrL-3V2P5ovdn4rqj8WVMAhvvpYuZCEjuDlI5Hi5OxdcPypqWbN6nt4cay2DJMnSvQxC_k8Zwigmw_YQec2sqRjCS470WKusHaEjjBEyeS2JXI2CGAp-C8jS9lqiWDcvk4aBRK8DIpvbNk880La0NhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*از سفره خانواده‌ها تا تابلوی فرابورس*
🔻
شیفته آرای شرق، نامی آشنا در صنعت غذای ایران، پس از سال‌ها حضور در خانه‌ها و سفره‌های ایرانی، اکنون با نماد «شیفته» وارد مرحله‌ای تازه از مسیر رشد خود می‌شود.
🔸
عرضه اولیه سهام این شرکت در فرابورس ایران، گامی مهم در جهت توسعه، شفافیت و خلق ارزش پایدار برای آینده است.
shiftehco.ir</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654379" target="_blank">📅 22:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654377">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaHXVSY936bVxcO5CI62bOrRu6IdEYRuf_tXfbdawUq4RjIYRCnNjcv5JBVUTMrqaeYw3SGqDniZDjNw7BiDaBbtpvGu4l2vQpRTzKWy_9kwcmBrDNBid9CHGa1fhLblqEwHk2QkRga1XPFyQQM00Y_6qXZUH_nIb3K_cpy6W7c75-doTssAkWJHuenXrck9AgbxdjOKXkbMwI1Q3a8mYmqOCTPx5gmgPkEBbgqPio7OR9EilMQEZIqwGcKrGSnEvHV88IHrt93gazD9AJBDZOHMnx6DevHDw0u7lkdtC4uBFrNFVMS1yrZTmxJgNeWRzRg0uKzVt2zSvBZ4RrEOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی با انتشار ویدئویی درباره کودکان شهید میناب نوشت: پیامی از دانش‌آموزان شهید مینابی: مبادا زمین را به شب تسلیم کنید...
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/654377" target="_blank">📅 22:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654367">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHJMPLdNiH_GbBNlFMYSmHTtRA4aFZpe5soZH8kHdg-gJPU02FdLOM1l0iF6PXuvsE43t_LbRJ7RyH3evMhdU-vaPckIGxehpmCpOOI-_4fAX2_Fc6d3kFZmrxCrXhrhH5qqR7eI6iB2vl6xo1gI_WCVXrI0_iM0-AVt7gnDuxrmrUxErxG5e_8c6PBYuBQsWG2C-UcNd7pxdQ5hZfJ0cY9un0RQkD2K3ieD4Vb_imB6I-6XurbWgbuV5Fn6-FSB39p0vQuALkq9FQYTKkwayeCsSTmKwTPeFJoHSDdPL2W3Csb3mgjjnA-DQ3g1EKxXcFK_m7tYEgN5nFFLU-mTTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAtQ9tmctbvONXI0qlNPtfaNwXYGtQyAwAHRcqtPq9FeLIl_qcYbZ-GFWwtW0WACVyTAHxn9bllH1fH3gs9VcrCahcLRNqwE0XM_PziZ6LFRTwFL8Z2DSt9qg7JHurKuN3mvw-a83SRRLIfTNMGUCfNIir1WcXty6pAMWS8Ysm9WAvozbkLVuZYVHU9aV9gv1PDmmaB92Eqcj5QzqUAQ-Po5Tuf0lIkZcCJnXFe9dTW9g-Tt2xa8te8eKC9CYiRJ6UImD6RhrCr0d9V6dtfvjtpzd4nEVsUG9Q-5Op6tB6_RGSpeIrSq4XErXlbcmEKKyNxQcwWVdzElJtkv1kGp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsovBQKabCz7UsdSfE9Qyptlr_U8HHY8vtnPcO_ADbg4EFd5jojlJXxCEr2ekDpmFpgEYeZ6sb4fj7B-IKRVEW-OROqJpZCaCGylmP8P6A_lE_y42Z_PZkJetI17SDmuuklo1LDbYkqnlompZ43gwPfuEverSG3ooe6tPOU5J-v_g7bcsRBZtRo0lkfnsSnXPhUellROsPzNUH4js1EF5tS5IhOcxJn86ytuLUCwLrg1mzhwCHU9oy_dYa0EmGmMluv3YZHg0uyF8cU-3FlJxJLEnp4EBg1cFR3tc-lMqkcL_lj-1ClD6Ftr5pLuLxP8HC-GKvDoLCw5KceI8ZE98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jUzHzQo_WxPtuMXiTZNfBszsVi1H4WgLha9frLw5zMCk2TX1o007HrI_gyUexDhqWi4lwwkmXHPkb5XBbJ6ZOTcGOUyKojlRaizNS_-fuAJltj47krQIrPsYoMncWuGhRwKhlBqu32arbkcu384kULJlFZTdPK45mxotWRcL2_cdAiyNt8GLH3jAOBmN6H_MVuS3Ll-9byELsKR7G1bLKYsKre4ykeUp_yOWv9eWOQ0BOI0uchSMSEhgsArpNc_kNUpprDi3SvYvxjW1sw9gZu4hNgjCMjNxnjkop117-jv67ZHPzwnka0cq4f9wwyVThBm29vcb0sJ3MXY0VxXSFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJj9OBYw68Pwr5uNVub79aJHBKFIwlg7UMwlEYo809QoQjc0fpu3KLlSf0aldhfi5-mMyiD_nkToBJbSw3ghlgcuUKYsao5LOrNBS2wmyytAd641houxJ0jMYoexyVjsnThw8vmy75UEI6AkFvLJ1HHLWwSL6fpVSA2LwU0HITdqxlozsx_p--kUrR4vJUQ4uUFW_Hx84zAShWG4Fse9Q_qJzGv_d3dthDtfBewtVt4_Aj-Tpu0YigbVJb8_7cgbYn0YAXcLd--KKUjMiRFW2LDQxY9azBqTKZje59S2xHh-u_1za5OESVApk29iRa3_K6yn187SytmKfR7Bvi-CIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cn31C2pbLKjZ3yOpxTBzvXeYg0bOgPQEfPjQQmVOECz8Kh-yI1M4tokpk1u8-Ze8oq1ePOnpD4RMsuNQcSJQTJ36Q7M2IBUrURu_MtfM7INDmWGQzDO7yLek0nFlF26wRclwVPmHJbf5LiRb9HiYQQS5SlxEqhz1QPjaaqBUQa_B0WGLZFPGx3I42Ysr6rJlt--fpZlV0HQ1znHvTXA-zhESe1IuN3XmwkaivyTJaB2qE6GLFsGIHshxl-Doi3oiHIW5FAJHmPVrGHFJoUsotZiZV30gCfbrjqBMJ8p3JD_D-c-CY7YtrQ3jdVvihBYrXOQA9W2fBLnc0pzLigmxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0M-_ih2Tr78Ex87AxViS2FkyC3eiWuv9EpJlB9Wx5QspxirIW2ErLA_sFUNQhYPD4WpH6czPZq9GWb-Ssl5n7aK9lSlF1hQiRyK6yyOAvGNFt9E17ayxXIMw_y4pTNsMMYs6K4sQS61MTEKa1EyLuup1mFyrLjMwpxIabqHthuYWrOYvSxUbGJaDJ2BtIdjfgcM54LMf1V9PSC0AgyI08I0Mycp28yAigtzFvsQx1JSeTmlJQsJLyegG7rxbtURaPQ1FW7YnFW2PfdbQlJ0sSeXym_tKSJW9ijyPZyl5bouvqQTLWr2tTnAVCswEplv5omGQ7_BmWEn5rJRzwkMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QC4CiwRX3O12ImLI-4eq_BBxWK00Howk8UKMx9enFBt7AIXVYkEbIjp5OQVqlvuBq3s_qsF23AAN5xud5_oUf3ymcHqngm7_8JJF6rUAHQATQrQPrJKGyOnIB3CbdS3fKXZAaSZv8zfV5YhPgE0xWlbjgfwRsFGVhE-zoJ4oTOfJWnD5jhRSbwAxKwB8zaLHtg_GgW2sa-Wju_0HOqXluWaOSPVjGRu7h4vx6vTYLWdioaHTPz3ou6XUB9M1dfnQoyVE_NojcpcP69eEhW9UDDLMkX8a_VZV2bksyKTCyK1LbIc5XycHddKZjvO_QMe5VSkstZ6SelSCFcstJHtPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mE4dn28e7H4bqBEuTsvwarSCABYj5I1r4prwKokTuUHL9RLawfIRGcc6RTKWHpJZDIovUSzUNVYg9VZqNVD_TEwN8LXxGZfe4viG3F1sP_1D4LiDwMtL96k8rbkt3rrt8JHa25Yr0GN82kBUY75KTbCN83ud63X8BCGUioa7IhZTchaR5SUXAwKZ5p_v4yXiKc9t_GlXwcQjB9lWuims9Fp2ciXQfYMuSnFc-f17dysLWca6tzhRiKJq_QP8ovO0X_GZcPU30WpaZOAdf7hW0qzyYOruNAvPXGaY01JW1456UvtIrxgn3u33d9olpR1KazOiKgmUa4JmnmjoF-pINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHBHF3xQuNfoSoRlfp9pPAOvchLafGIM3gHWoMhG-keyghWGvDHkLorPKdQdjcZbr60Dfg_JygwLd6WL-ibLdCaJowfoR7cGfF_aYJJxTC-NLMpWFWHetNhdVSOX8DEWfGjUCXFBEe-rKPwIdr2tiy9eZJIAkF7jNWgk2WtDQfR88g8N4ONIJS_bjwmztUCE97NUOD65e_QftW8GMYvkmdh6DybCcks5CwdbegyHlFPsswLAvuGWX2OhzGjavZFk1wqU3c49Koq97TS4scpQDHCjsfxgxw9dq0ylDeUx4V-R5Cbvh4C1WBAh6CNl5eE-BV4EyqWzCsCiO7o18lhEuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ همدلی
💫
هر روز، به پشتوانه
#همدلی
و همراهی شما مردم عزیز،
#هیات_قرار
با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، گامی در مسیر حمایت از خانواده‌های ایرانی برمی‌دارد.
ادامه این مسیر خیر، حاصل اعتماد و حضور ارزشمند شماست
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/654367" target="_blank">📅 22:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654366">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee2E1wAExEIEdv9uOU70kdF-qfKMkrJ_cvir_n6SJV1kArjdoF4h1Y9wcuEyhlabYHSHJF4YsGsf2_db8WgUudUP2rCJlFGwI2TwIORqt0M4XyEH7bTD7xxEloOKFUX9biihBXOrj2RmI2YHabmwlJWVlo2FEEk-S5SkMwveJYAYLx694EGFxO1WSPtACQ1QMsXOfep_-j0SCKtYgZ2SgNoYrjgljAUL0H1O_BhdZZGe4ms5n3DQAAGuNA1qhAeHPUsvmWMpAw2HWXT6Zzw-u8clY0xMMqjhAWPDTZwT_14zV6iZw3px8EYpOiXcDkKvv5ap0G3EoiLF7XH7iBK29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاو شبیه به ترامپ از قربانی شدن نجات یافت
🔹
گاومیش آلبینوی ۷۰۰ کیلویی با موهای بلوند خاصش، آن‌قدر در فضای مجازی معروف شد که قبل از قربانی شدن، راهی باغ‌وحش داکا شد!
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/654366" target="_blank">📅 22:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654365">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c6ee552f6.mp4?token=v_Bx8vH1EUjGWCEkuTvVO3jN_nGHkRpFIIgpHB_OIUxf5VVm4i2h22cd1harjkNm9nJjZhYWKRzMATx5aXsuh3l_r3VljejJjpvKI4pOVrMLLPMF4hXx0o-hkIA7dMrVpjipJWWMqrlSjg3wWtiekX95RwwugOsc6a3VnmE36Ld1yzbFV1fI1j-pwt7y7zG0lMl7N8sklc0uANKfFzhKvrVKuKcIZAjXFiPiD5T8TKzxZ7dU5uRBRHh_4auYMQjPQomiPjPQnZ3ntk8DxbRnLg6oq0HzDpMPEEwTDG0v7rbA0dGEGLy5CJWlfVVhLWxA0jNX6PdtCtDcB613Xl_uOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c6ee552f6.mp4?token=v_Bx8vH1EUjGWCEkuTvVO3jN_nGHkRpFIIgpHB_OIUxf5VVm4i2h22cd1harjkNm9nJjZhYWKRzMATx5aXsuh3l_r3VljejJjpvKI4pOVrMLLPMF4hXx0o-hkIA7dMrVpjipJWWMqrlSjg3wWtiekX95RwwugOsc6a3VnmE36Ld1yzbFV1fI1j-pwt7y7zG0lMl7N8sklc0uANKfFzhKvrVKuKcIZAjXFiPiD5T8TKzxZ7dU5uRBRHh_4auYMQjPQomiPjPQnZ3ntk8DxbRnLg6oq0HzDpMPEEwTDG0v7rbA0dGEGLy5CJWlfVVhLWxA0jNX6PdtCtDcB613Xl_uOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف شبکه صهیونیستی اینترنشنال به ابرقدرتی ایران؛ اکنون در تمام دنیا و خیابان‌های اروپا صحبت از ایران است
خبرنگار شبکه اسرائیلی اینترنشنال:
🔹
تنگه هرمز، تیتر یک اخبارهای اروپا است و شهروندان اروپایی در خیابان‌ها هم در مورد این تنگه صحبت می‌کنند!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/654365" target="_blank">📅 22:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654364">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC3zOQrk_8hTn0DuR4MCDC6yoHEC1E3GntBnLUzO3z3kbprQ4S_inymL-na9Ej7PX4RAzUgSHbS_qliMprT5jUlj0-ZDAsKD9gIZZBTBmGy89xzKFQji8-2U5UDWuX_M-Lk5C8D9axamnq3x06na6M4AKH1s1FAPoZVYm4HLb93EHeXPOTIyK8RnsHVxqBpTDgumWfU4o4m-02wp-O-4P06B9aGZQrmvbkgkQoCMVASHm0qVYpKa3q_7uVrEeJ8RU5a_h_FV1lqTDwBKF5M8FOsGtupGPmoPucBstWvSp9OLI3ulQvI-24-h4-W3Mzip6nSvfWqsgxPv5Dnpxy2z7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهردار مسلمان نیویورک در مراسم نماز عیدقربان
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/654364" target="_blank">📅 21:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654363">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMPk4-VWPaO_7688peLJSg0byxwZQ28P2H6dkfqzbgG4VoKOcOf64455kG6xvTlNUg4a-jXyk97XgqwO7CthcaJI03IrUlnpa_WYPjTtHbS2thc8bk9Eu164TMd2_Y00R6VdXbUXRTY1mt_vWwmdf4dNbyMS2-Dzwfn8cGXw1GiJgBBKpFfFkvkTzPBVp2xN-q0M9dtLMxsRhTm6ZxM7nw5FLDUEUxwJUr4j9YYl9jXMQUWOhgvRJuiiHDouJM3bXaO9c6_xnGSiPgsxtsrb88bL32qoh6z5vIi5tOuISOqpeJ7lcTv0ztPz4sPSSO6lm3bcz2aGZ9QdPYrqB2KHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتورسیکلت موربیدلی N249R
✨
249 سی‌سی
💪
تندرو و قدرتمند
✅
37 ماه گارانتی از نیکران‌موتور
جهت مشاهده قیمت نقد و اقساط و مشخصات فنی روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/80x
🏍️</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/654363" target="_blank">📅 21:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654362">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f63fdbc2.mp4?token=gcPwDUu8PAGw2BbOe768sF6K0qyNhbrHzdZwpJsESu-fOV_0HCbcg-_o1-UeplEsy04i38J6-e3Nb2fMG82FBzQy0PI_2sOsEU3eHhcZKIxHJAtjT_amHnAjTtmmkf8v1GGcY6KxQz8Bv4fn_vz7TP_udFOE0tLe9u9Fe8UhFNi_QDE3BAxERxWfZmOb9o3-ZDZS13XqL6g6nkpn311dn-wP3eChZySyDVKJLMA5sw8LzCUCCmNrrJw2M6LXwWtYIEusz-0quSwlL2EsUAjw7Et596-metjPwRGSRiuBmtOsqBnXsePZyv0vNhgYiw7OWvz9Ur6zDg2kKNd6ZtKWdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f63fdbc2.mp4?token=gcPwDUu8PAGw2BbOe768sF6K0qyNhbrHzdZwpJsESu-fOV_0HCbcg-_o1-UeplEsy04i38J6-e3Nb2fMG82FBzQy0PI_2sOsEU3eHhcZKIxHJAtjT_amHnAjTtmmkf8v1GGcY6KxQz8Bv4fn_vz7TP_udFOE0tLe9u9Fe8UhFNi_QDE3BAxERxWfZmOb9o3-ZDZS13XqL6g6nkpn311dn-wP3eChZySyDVKJLMA5sw8LzCUCCmNrrJw2M6LXwWtYIEusz-0quSwlL2EsUAjw7Et596-metjPwRGSRiuBmtOsqBnXsePZyv0vNhgYiw7OWvz9Ur6zDg2kKNd6ZtKWdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشر شده از مکزیک، لحظاتی عجیب از جوشیدن زمین و خروج بخار شدید از زیر خاک را ثبت کرده است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/654362" target="_blank">📅 21:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654361">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeomfawIo4usnxeFaOu09CFn7pcQuYEwHjqq7GlXveHZ7ucLlw4T7Xqi-mMB2BwHoN0ZvIg17QMb2yfZ72-6Vf0QsUDo28eRG7Ru2F1GKLZdUBVDDNJ6OZUeVICrAfd5uPwTLIQFBNraFUrBhHStyWoQ5_aOYfI_T1Jw4jJp86tUKoFfwObavqfsXf-oRZYNrel5nzZAESdBLh415gl9MJ6ajBjshJm74AWU_YVfmCJ2F2ZroI7huX_inPkjC37t4HnMJo1q8ShkbVM0QhYIDuchGBu5VyX6g5o12Y6CMIMIwOAcuSVn76T8zzfPu_Oc6jGtyVxeE34aJeKa-AACjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر امروز ماهواره کوپرنیک از وضعیت دریاچه ارومیه و مقایسه با زمان مشابه سال قبل
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/654361" target="_blank">📅 21:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654360">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69bb560a4.mp4?token=BLCdxKFOderuIEx9nYXw6Pgdg0dGya4w9Bq8musEU1bdY9YcxvXkvRlIWav1SnnvFgLrDiDrUdiGvbgxnjkCswGq0AA5IOdbeZ5f3zSrAQcTsoAwRaQqKkNKiI_AwhgtHmuoquAL0MFvqKK20qVK8VZ_HQV6EWxFJGLVVvhiWjD1I-FAgg93uPLVbIYCnPIJ-0jRRZv-NLZ4FTMRpla8gfQhCpTp4E5kg1RnfW5tWw8kCTCyON0TXf70aIrP6Evo8FpeWfpaH1aoggRPKuYHKoBpLjSYiFk5ZnYtkJVBmXe0nxDjQuzVGh4UeorkVOTHFeXdM1UVOS4IxopgIk8UEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69bb560a4.mp4?token=BLCdxKFOderuIEx9nYXw6Pgdg0dGya4w9Bq8musEU1bdY9YcxvXkvRlIWav1SnnvFgLrDiDrUdiGvbgxnjkCswGq0AA5IOdbeZ5f3zSrAQcTsoAwRaQqKkNKiI_AwhgtHmuoquAL0MFvqKK20qVK8VZ_HQV6EWxFJGLVVvhiWjD1I-FAgg93uPLVbIYCnPIJ-0jRRZv-NLZ4FTMRpla8gfQhCpTp4E5kg1RnfW5tWw8kCTCyON0TXf70aIrP6Evo8FpeWfpaH1aoggRPKuYHKoBpLjSYiFk5ZnYtkJVBmXe0nxDjQuzVGh4UeorkVOTHFeXdM1UVOS4IxopgIk8UEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما شرط جدید ایران برای توافق با آمریکا را اعلام کرد: پرداخت غرامت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/654360" target="_blank">📅 21:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654359">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
نماینده ولی‌فقیه در سپاه: در طول جنگ می‌توانستیم اقدامات سنگین‌تری علیه آمریکا در منطقه انجام دهیم اما چون مردم خاورمیانه آسیب می‌دیدند رهبری موافقت نکردند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/654359" target="_blank">📅 21:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654358">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbXquSpPOmF1DE9jDJXydqLmdY0K1wtFyxWfbOtS62kF-2_CUBxh8ipAL2r--GSHod01YW-VYVRngNybHyl2uUjqljSmkrMwNqpGTAa55XuXR6jBclhgCVtlErB7OhiG1KvDDcsLZi3jGpxDF2Upu1ZcbPtw5-HqE05EAKopmb7q1Iqn3cMsOWN8CCRWRpMzKQHx7eBq8Hb6AXRa8HDu6gTFbR6qlUX5AJSYsJP_KGSf-iQ89JgmBEeaLGjJmJSdzarMEz_k_TmKJ_I0VsmUlSFemICH6ThWKkE0Nh3P1Y_ohDZu1FBdsy2WIlppB-T3TeOVh7ooaKER4KHl1hyEng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش سنگین بازار سهام آمریکا بعد از اظهارات ترامپ
🔹
بازار سهام ۲۳۰ میلیارد دلار از ارزش خود را از دست داد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/654358" target="_blank">📅 21:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654357">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb3e0f9ffe.mp4?token=k9Y5_oPEwKRh-OE8Lj1nTJ7Cp5LLuw6CJFg8gHeMmVDsTTe84koORWonu_sm2BS0kfdeVar7JCD6W3NQaThuIYoaBtgLfp6bnzrQWwlgmkgo7Rb4zy7hsArTF0N3sQO-x_MULX0RjzQOlZ9Jkj_7aX6ZWI5ri9F_rG2-p5z526UzbM874n3I6CpR8rh59FvAc6YXkZJaBzJ-CApchjA3-dLhUR9xlJMrrwfDKv54Ef8n_DRPr2NAWo4Ykm2dFqpdjKopXUZe4y_i7k9WA3_ZB2ZSTdF8Yl-TpuYw4WTQlPHBrsZqx5Nn1YkV5acTPwcHmFDsuVkNKP_dYUd_ANW8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb3e0f9ffe.mp4?token=k9Y5_oPEwKRh-OE8Lj1nTJ7Cp5LLuw6CJFg8gHeMmVDsTTe84koORWonu_sm2BS0kfdeVar7JCD6W3NQaThuIYoaBtgLfp6bnzrQWwlgmkgo7Rb4zy7hsArTF0N3sQO-x_MULX0RjzQOlZ9Jkj_7aX6ZWI5ri9F_rG2-p5z526UzbM874n3I6CpR8rh59FvAc6YXkZJaBzJ-CApchjA3-dLhUR9xlJMrrwfDKv54Ef8n_DRPr2NAWo4Ykm2dFqpdjKopXUZe4y_i7k9WA3_ZB2ZSTdF8Yl-TpuYw4WTQlPHBrsZqx5Nn1YkV5acTPwcHmFDsuVkNKP_dYUd_ANW8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سگ زرد: اگر ایران را بمباران نمی‌کردیم، اسرائیل با بمب اتمی نابود می‌شد!
#Devil
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/654357" target="_blank">📅 21:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654356">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f703feb9.mp4?token=ECx8ojQRMhQeUH0E_Wzu4K8_rem-svLXS_PMT9XC3R7gfu2UXfKjk6h_OHYDYZruDILIl8RfxwLZGQacHolbiQefhArzSRMD6btCrD6WDa3-YQwH7iuw3HUgXWFGoOcsAaf-CS9JR_7gChGb-exHPAIXFIg83utaj7-rEtYM4_VbEv9rildS5Py-uWHD0zWgO_psuZg-TecuAGOQ-_W55V34KR1fwg55iDQwOB2rZrHKsQQC_NWqiXbb9EbMP3wj9yK9fZFTKiF4KE3R-IQyGzoynm9BT8ioYHQTDxBThgLLnB2u2ZxawGEPF1NcH6ALZjHVNkdTjjb6-EmSQOc0xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f703feb9.mp4?token=ECx8ojQRMhQeUH0E_Wzu4K8_rem-svLXS_PMT9XC3R7gfu2UXfKjk6h_OHYDYZruDILIl8RfxwLZGQacHolbiQefhArzSRMD6btCrD6WDa3-YQwH7iuw3HUgXWFGoOcsAaf-CS9JR_7gChGb-exHPAIXFIg83utaj7-rEtYM4_VbEv9rildS5Py-uWHD0zWgO_psuZg-TecuAGOQ-_W55V34KR1fwg55iDQwOB2rZrHKsQQC_NWqiXbb9EbMP3wj9yK9fZFTKiF4KE3R-IQyGzoynm9BT8ioYHQTDxBThgLLnB2u2ZxawGEPF1NcH6ALZjHVNkdTjjb6-EmSQOc0xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم یادبود شهدای خانواده
امام شهید و رهبر معظم انقلاب اسلامی
شهيده زهرا حدادعادل
شهيده سیده‌بشری حسینی خامنه‌ای
شهید مصباح‌الهدی باقری
شهيده زهرا محمدی گلپایگانی
پنجشنبه وجمعه، ۷و۸خرداد ساعت۱۶ تا ۱۸
مصلی حرم مطهرحضرت عبدالعظیم حسنی
ازطرف خانواده‌ رهبر معظم انقلاب اسلامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/654356" target="_blank">📅 21:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654355">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341480826d.mp4?token=MfR82iXR1vdEk9Ws1-IEJ6ortZqRfbrymdBfbq8RDkr0F8rZjiF7suvC3242w83UyF592MhXPKyp1rRRlaFfO-ehBRHGFzm8A4X4If-IhxYfgjyHLhbS9JYqW4CFEXZ2UwlVvqTlzzIAuD4R-qUAhAUDGJb7x-jExqyrvI7QI_J9w_V4qE2RSHFDh7QT1UsvrmbJXJbGGhgsphtSl4rhLVN4yFq8YlWnT5aRkMALGzSimpi4fNjUiXAEYL-vn6zxVLqMzu2lZYGKBAIvI_Hw4GQTP3bWI54XQi0RjKeUCpkCcpBbuZx3rSDJOaR77GkjFkTx9cOEfInwrYj50njxNw_AHggASihgTjAZ3SeDBdHKh3jPXC4DYp3f83v6Kx3idE6IQeusbfGTgJPWfAKbMEJ3ovlowOyLSp50-yAS9ypLhZDGnDMHzdYsjGWo__BihCe8WnUwYPw3ZipwDpRpZIeOEDMBuPE75v14Qm9GdAHe4s6KbGldDht3pvJ2tQDQVVkmKHS2lP2OsHGVfXNSjcxa5ieajrBJVCqk_iqF-8XxXKONmRbxFCIsN9RRQyyrN6IpQzUAZU7wcFUq1ndOKj-fvVjjyDnw1tNG5r08KZdvASSXiUo-3zHp4rCa7oM769nKlYxkNB9YeuX__uhCJqla6j1sP6BQqHbdPxEX1zY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341480826d.mp4?token=MfR82iXR1vdEk9Ws1-IEJ6ortZqRfbrymdBfbq8RDkr0F8rZjiF7suvC3242w83UyF592MhXPKyp1rRRlaFfO-ehBRHGFzm8A4X4If-IhxYfgjyHLhbS9JYqW4CFEXZ2UwlVvqTlzzIAuD4R-qUAhAUDGJb7x-jExqyrvI7QI_J9w_V4qE2RSHFDh7QT1UsvrmbJXJbGGhgsphtSl4rhLVN4yFq8YlWnT5aRkMALGzSimpi4fNjUiXAEYL-vn6zxVLqMzu2lZYGKBAIvI_Hw4GQTP3bWI54XQi0RjKeUCpkCcpBbuZx3rSDJOaR77GkjFkTx9cOEfInwrYj50njxNw_AHggASihgTjAZ3SeDBdHKh3jPXC4DYp3f83v6Kx3idE6IQeusbfGTgJPWfAKbMEJ3ovlowOyLSp50-yAS9ypLhZDGnDMHzdYsjGWo__BihCe8WnUwYPw3ZipwDpRpZIeOEDMBuPE75v14Qm9GdAHe4s6KbGldDht3pvJ2tQDQVVkmKHS2lP2OsHGVfXNSjcxa5ieajrBJVCqk_iqF-8XxXKONmRbxFCIsN9RRQyyrN6IpQzUAZU7wcFUq1ndOKj-fvVjjyDnw1tNG5r08KZdvASSXiUo-3zHp4rCa7oM769nKlYxkNB9YeuX__uhCJqla6j1sP6BQqHbdPxEX1zY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از پیگیری ستار هاشمی وزیر ارتباطات برای بازگشایی اینترنت بین الملل
🔹
ستار هاشمی وزیر ارتباطات: برخی نگاه های داخلی ریشه فناوری کشور را می خشکانند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/654355" target="_blank">📅 21:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654354">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec94eb44b.mp4?token=i34C69fAW4PlWRD1CFe40tx3Sxg5H353tG2_i6Ifyw8rYdzMYx9phNVKOTTvTw-o127G6V4Uyk4kSdx0OvO8JnMo-oRU-E7f5SsApCkIgDFmQR-xZsItDV9PYvmRx_UCM43sn_3spP8qupKgoz9BU5WPr1IvEEGrrOHJ2qYJpYBDpFucrN39ke12-pEKIoWTCPC7YvwTD0nSTTek20AYtEPw0LtnVM8Lu5tmgt1r-5sjI9iT942awc_A95w856-TEsnKafUYmtKQ3YAHXfvuqPoT2hH0m4pdLl0j2N5tJjXbAkRvX438zSjRTs0h86RTT8s-GTh40JgxnX19S3h-lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec94eb44b.mp4?token=i34C69fAW4PlWRD1CFe40tx3Sxg5H353tG2_i6Ifyw8rYdzMYx9phNVKOTTvTw-o127G6V4Uyk4kSdx0OvO8JnMo-oRU-E7f5SsApCkIgDFmQR-xZsItDV9PYvmRx_UCM43sn_3spP8qupKgoz9BU5WPr1IvEEGrrOHJ2qYJpYBDpFucrN39ke12-pEKIoWTCPC7YvwTD0nSTTek20AYtEPw0LtnVM8Lu5tmgt1r-5sjI9iT942awc_A95w856-TEsnKafUYmtKQ3YAHXfvuqPoT2hH0m4pdLl0j2N5tJjXbAkRvX438zSjRTs0h86RTT8s-GTh40JgxnX19S3h-lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز توافق با ایران را به سازش کشورهای عربی با اسرائیل منوط کرد
🔹
چنانچه کشورهای عربی به پیمان سازش با اسرائیل موسوم به «توافق ابراهیم» ملحق نشوند بایستی با ایران توافق بکند. من مطمئن نیستم که اگر آنها به [پیمان ابراهیم] ملحق نشوند باید توافق کنیم.
🔹
عربستان، امارات و قطر مدیون ما هستند
#Devil
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/654354" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654353">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اسرائیل هیوم: ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/654353" target="_blank">📅 21:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654352">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0848db393.mp4?token=hIrGLl3Rb_abqw_MsO54iw2Iuq_BG9rZgr6P8NnMDGDVe6ydAzrZ3oQnkpbhCvKsGC0UdWpUbNQf7jCyi-nCX4IKPj_mSPRv6Ao33gSuldQq7BE-wpp0ouoOp2tMTscYSgDuS1EuGkCrYZdgukh5qFsxKFTY8x-rSbtDi7zlEDrlYQkrI2hEnRB7eaaSXRYOuziIloctqWFA-87mDF4eP5bYIztPDqLRhY81Kpp0KTA8eiv7iwYQUKTX-6VBwOGIMPUsN71_fxlLUq2vdFvJSC8IGDQ_A9bHFLrwBB4gR4uL_SZc1icH3Kd0iUA60ZK7dfym0POGl7jlDnwabUpH5W2lDPOIpim836AQ8fapPWXSS0-DAwJUffVP2vlocEG64mcB3u2j4vPJvIZpJAMKoIg-uVTt1hIr-pzoiubLR0GIQHST86keygwdViX2EGgr2XM4Bg7BEnBd0LS0MtDnrxPCUl-PuKU75rcNjyOaQ5_g1cscpK1SRev_w6yVtvttEZn1iGCH2bxMU-3J6U-Fp_sGK_LN1etu_0Ow6LjK7xu9t3pVFORzmTbSzzMbUeq2nzVnADjvDvrQho6NbLasw1GDpzPY7g11nEwclZGFsDnGlwkgKRAFVfe8NFYWpn3fA6GocJCdbmase27VewQWPRqK4CNg7cO_1uEy4FHafng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0848db393.mp4?token=hIrGLl3Rb_abqw_MsO54iw2Iuq_BG9rZgr6P8NnMDGDVe6ydAzrZ3oQnkpbhCvKsGC0UdWpUbNQf7jCyi-nCX4IKPj_mSPRv6Ao33gSuldQq7BE-wpp0ouoOp2tMTscYSgDuS1EuGkCrYZdgukh5qFsxKFTY8x-rSbtDi7zlEDrlYQkrI2hEnRB7eaaSXRYOuziIloctqWFA-87mDF4eP5bYIztPDqLRhY81Kpp0KTA8eiv7iwYQUKTX-6VBwOGIMPUsN71_fxlLUq2vdFvJSC8IGDQ_A9bHFLrwBB4gR4uL_SZc1icH3Kd0iUA60ZK7dfym0POGl7jlDnwabUpH5W2lDPOIpim836AQ8fapPWXSS0-DAwJUffVP2vlocEG64mcB3u2j4vPJvIZpJAMKoIg-uVTt1hIr-pzoiubLR0GIQHST86keygwdViX2EGgr2XM4Bg7BEnBd0LS0MtDnrxPCUl-PuKU75rcNjyOaQ5_g1cscpK1SRev_w6yVtvttEZn1iGCH2bxMU-3J6U-Fp_sGK_LN1etu_0Ow6LjK7xu9t3pVFORzmTbSzzMbUeq2nzVnADjvDvrQho6NbLasw1GDpzPY7g11nEwclZGFsDnGlwkgKRAFVfe8NFYWpn3fA6GocJCdbmase27VewQWPRqK4CNg7cO_1uEy4FHafng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده ولی‌فقیه در سپاه: نقشه دشمن این است که ما را مقابل هم بگذارد
/
مذاکره‌کنندگان بدانند شما نماینده یک امت برنده‌اید
🔹
هم کسانی که مذاکره نمی‌پسندند و هم کسانی که مذاکره را یک مبارزه می‌دانند بدانند که دشمن می‌خواهد ما را درگیر مسائل داخلی کند.
🔹
اختلاف‌نظر همیشه وجود دارد اما وقتی فرمانده بالادستی یک فرمانده واحد است همه از او فرمان می‌برند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/654352" target="_blank">📅 21:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654351">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ قمارباز: ایرانی‌ها شروع به دادن چیزهایی کرده‌اند که باید به ما بدهند. اگر این کار را بکنند، عالی است
🔹
اگر نکنند، هگست آن‌ها را نابود خواهد کرد.
🔹
ترامپ مدعی شد که به درخواست فیلد مارشال پاکستان که خیلی مرد محترمی است، به ایران فرصتی داده است #Devil…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/654351" target="_blank">📅 21:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654350">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2a6a8d3a.mp4?token=n015TW3waCKfWQM00csxeslCakbZFkb3XvIdrLOPmeYES43c_MPSFX0XLQ4CXSVLULw9QYoFa_TDFq3XD4NdOcz4R5dcHLNyRx5eOah-Yvscquu1RT9WYeZvfZt90Kaz-97Xiv0wl9nDF1Ak6hmnUtmVrg4E8SeuVn9qC5K9ZMmGj8LH2Or6Tlny40zJ_FPuEI3zS8UnailXEWOByZRaC-zcqLkoVTBXyzJcbsNmgONt6soJuwXmX5QOnsUHxJRpJPTRnpFwP5tFLcmJq0P2v0kkasXFr8IhcXbXXptbc3pxDDmHVp2AD05mSulGLl3CHm4BoeRJoK8VXfUx7MoAEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2a6a8d3a.mp4?token=n015TW3waCKfWQM00csxeslCakbZFkb3XvIdrLOPmeYES43c_MPSFX0XLQ4CXSVLULw9QYoFa_TDFq3XD4NdOcz4R5dcHLNyRx5eOah-Yvscquu1RT9WYeZvfZt90Kaz-97Xiv0wl9nDF1Ak6hmnUtmVrg4E8SeuVn9qC5K9ZMmGj8LH2Or6Tlny40zJ_FPuEI3zS8UnailXEWOByZRaC-zcqLkoVTBXyzJcbsNmgONt6soJuwXmX5QOnsUHxJRpJPTRnpFwP5tFLcmJq0P2v0kkasXFr8IhcXbXXptbc3pxDDmHVp2AD05mSulGLl3CHm4BoeRJoK8VXfUx7MoAEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه باجناق ها دزدن! اونی که شاسی بلند داره شاه دزده!
صحبت‌های دکتر عزیزی، مشاور خانواده در برنامه محفل شبکه سه:
🔹
نگویید «خوش به حال فلانی»!
خدا همه را امتحان می‌کند. فکر نکنید همه خوشحال‌اند و فقط شما نیستید.
زندگی خودتان را با دیگران مقایسه نکنید. همه در حال امتحان دادن‌اند و شبیه همیم.
▪️
برنامه محفل ویژه دهه ولایت، هر شب ساعت ۱۸ از شبکه سه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/654350" target="_blank">📅 20:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654349">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای ترامپ: تنگه‌ها برای همه باز خواهند بود و تحت کنترل هیچ‌کس نخواهند بود. ما مراقب آن‌ها خواهیم بود./عمان مثل بقیه رفتار خواهد کرد، وگرنه مجبوریم آن‌ها را بمب‌گذاری کنیم
🔹
تا زمانی که ایرانی‌ها رفتارشان را اصلاح نکنند، هیچ پولی را به آنها برنمی‌گردانیم…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/654349" target="_blank">📅 20:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654348">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای ترامپ: تنگه‌ها برای همه باز خواهند بود و تحت کنترل هیچ‌کس نخواهند بود. ما مراقب آن‌ها خواهیم بود./عمان مثل بقیه رفتار خواهد کرد، وگرنه مجبوریم آن‌ها را بمب‌گذاری کنیم
🔹
تا زمانی که ایرانی‌ها رفتارشان را اصلاح نکنند، هیچ پولی را به آنها برنمی‌گردانیم
🔹
همچنین ترامپ در پاسخ به خبرنگاری که پرسید آیا با این موضوع راحت خواهید بود که روسیه یا چین اورانیوم غنی‌شده ایران را بگیرند؟
ترامپ: نه.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/654348" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3dbac181.mp4?token=lqwXIE_3CsU_p_IcvK6U-Ufuq0EwQEXdpD9w5rkCkoZ_fNpJvr2uEKQ1yVJbYfR6pWPvGj5uIgYg-qbu1TBLbAkECoKgfFuU2pthVEts1HBv7TqP_B5qI8W40XT40y6S4QL8imYEREeJrbmUYNJhLtCftDJnexUw3KYkCOqImWLE67vLxklx0DQXI8pzn6fZNpAzGWdOWAqGMafTEggNjOHq1aumxF9hl3BIavd10PjQdoBo-qIkKcnKzA_Z2mqnL58LeXAQGHNIDUrcvRNL1ttyQrYP-DQeV6KJU7Zrs4YYqDiIltagoTJNgqoK-HYdp2OajX2BHb0kc3aEV-oIkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3dbac181.mp4?token=lqwXIE_3CsU_p_IcvK6U-Ufuq0EwQEXdpD9w5rkCkoZ_fNpJvr2uEKQ1yVJbYfR6pWPvGj5uIgYg-qbu1TBLbAkECoKgfFuU2pthVEts1HBv7TqP_B5qI8W40XT40y6S4QL8imYEREeJrbmUYNJhLtCftDJnexUw3KYkCOqImWLE67vLxklx0DQXI8pzn6fZNpAzGWdOWAqGMafTEggNjOHq1aumxF9hl3BIavd10PjQdoBo-qIkKcnKzA_Z2mqnL58LeXAQGHNIDUrcvRNL1ttyQrYP-DQeV6KJU7Zrs4YYqDiIltagoTJNgqoK-HYdp2OajX2BHb0kc3aEV-oIkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاف ترامپ در نشست کابینه
🔹
دونالد ترامپ، رئیس جمهور دولت تروریستی آمریکا در سخنرانی در کابینه، ایران  ونزوئلا را با هم اشتباه گرفت.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/654347" target="_blank">📅 20:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654346">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
هگست: ایرانی‌ها هنوز موشک دارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/654346" target="_blank">📅 20:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654345">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
دولت پاکستان: شهباز شریف در گفتگو با پزشکیان تأکید کرد که امیدوار است به‌زودی به یک توافق صلح دست یابد
🔹
شهباز شریف به پزشکیان تأکید کرد که عاصم منیر تلاش‌های جدی و مستمری برای برقراری صلح انجام می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/654345" target="_blank">📅 20:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654343">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4501e83e61.mp4?token=cdjdsqyV4dEdF56_uQYu4r8hjTAtVQpRbcCHT9SJtOyspumDR3f5IEQ8VutSwZuwtmlXccaCsi6v47TiGB739RjYAa4yx0c_JpHdXGqo2pLCu8ZJZhPlNEmk5TPtFwSZkzqAvC6v6IutK2AZPlomTBog3EgpFlg-vjFR4jrmgXY_jXoOtLQMULyf6u9lHe_ZMfrmtkJPP6kIPFyi9TflxhshLGCklIcPkgXNVEhMqYMDVUxAoAIJqpgl4cYVGHZ2JigzrlZP9pql0F_7215oOAXCpG_CnLhXT98bZUh8eZRZ_9L8Y3EK24c-PFFWJ5DhZzw-5nBSryPGqjqYCcde_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4501e83e61.mp4?token=cdjdsqyV4dEdF56_uQYu4r8hjTAtVQpRbcCHT9SJtOyspumDR3f5IEQ8VutSwZuwtmlXccaCsi6v47TiGB739RjYAa4yx0c_JpHdXGqo2pLCu8ZJZhPlNEmk5TPtFwSZkzqAvC6v6IutK2AZPlomTBog3EgpFlg-vjFR4jrmgXY_jXoOtLQMULyf6u9lHe_ZMfrmtkJPP6kIPFyi9TflxhshLGCklIcPkgXNVEhMqYMDVUxAoAIJqpgl4cYVGHZ2JigzrlZP9pql0F_7215oOAXCpG_CnLhXT98bZUh8eZRZ_9L8Y3EK24c-PFFWJ5DhZzw-5nBSryPGqjqYCcde_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ما به نفت نیاز نداریم؛ ما به تنگه‌ها نیاز نداریم؛ ما به هیچ چیز نیاز نداریم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/654343" target="_blank">📅 20:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654341">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ترامپ جنایتکار بازهم تهدید کرد: اگر به توافق نرسیم شاید برگردیم و کار را تمام کنیم!  سگ زرد:
🔹
آنها فکر کردند من را خسته می‌کنند ولی من آنها را خسته کردم.
🔹
من تحت تاثیر انتخابات میان دوره قرار نخواهم گرفت.
🔹
در مورد جزئیات توافق ویتکاف در جریان است.
🔹
ایران…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/654341" target="_blank">📅 19:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654340">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای تازه سگ زرد: تحریم‌ها در ازای واگذاری اورانیوم رفع نخواهد شد
🔹
دونالد ترامپ در گفتگو با شبکه تلویزیونی پی‌بی‌اس گفته که ایران در قبال تحویل دادن اورانیوم با غنی‌سازی بالای خود، هیچ‌گونه تخفیف یا لغو تحریم‌هایی دریافت نخواهد کرد.
🔹
آن‌ها اورانیوم با…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/654340" target="_blank">📅 19:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654339">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307416dd7b.mp4?token=UjBFIWq4jlFt5Gnh8XOLWdCzGKe5zYqQJQmCg46f1v5gzg8nr5SICkFFNwxK7-OppUwydUDsBj0B16FdBjBMkoSQ3ou3ueOVE9eO6ihim-Pxg3pchxrD9s8FdCb1hsTYMlKfOAlzVp0AlWUf9R8CQS76z7tSMylFSL3z27RtbxSIGXzJ31o9P4iToEkebD8IlJ8iv3vnANxKweuS5kc69v2WI1gB1ZNs8tNIIwA8zd8gqtgZ22LNCyJse-gV9mQQN4DpkHDHF4_Z9wRdcmx_62CXdDK0L40kM0QF3kMdvAsv9PLHGiGQ-KRctzT5tqHBW1bw8iTK7_dS60T1M2wwLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307416dd7b.mp4?token=UjBFIWq4jlFt5Gnh8XOLWdCzGKe5zYqQJQmCg46f1v5gzg8nr5SICkFFNwxK7-OppUwydUDsBj0B16FdBjBMkoSQ3ou3ueOVE9eO6ihim-Pxg3pchxrD9s8FdCb1hsTYMlKfOAlzVp0AlWUf9R8CQS76z7tSMylFSL3z27RtbxSIGXzJ31o9P4iToEkebD8IlJ8iv3vnANxKweuS5kc69v2WI1gB1ZNs8tNIIwA8zd8gqtgZ22LNCyJse-gV9mQQN4DpkHDHF4_Z9wRdcmx_62CXdDK0L40kM0QF3kMdvAsv9PLHGiGQ-KRctzT5tqHBW1bw8iTK7_dS60T1M2wwLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای تازه سگ زرد: تحریم‌ها در ازای واگذاری اورانیوم رفع نخواهد شد
🔹
دونالد ترامپ در گفتگو با شبکه تلویزیونی پی‌بی‌اس گفته که ایران در قبال تحویل دادن اورانیوم با غنی‌سازی بالای خود، هیچ‌گونه تخفیف یا لغو تحریم‌هایی دریافت نخواهد کرد.
🔹
آن‌ها اورانیوم با…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/654339" target="_blank">📅 19:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654338">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDlbYTlrEFYwullxLr0IXlvEtjIIwkiDW6pR6agbjFo3mlotYOL61YB9r5ucVTVnuJxm7Mh9Hr6W80DLBIyHFKvL8_5R07q8AsnR57_ARiDVnK_K-2yybEErdjd7Werv4Z5C44Av0IfjqxpGx6WINNTCI0A6vvziEUzDT3o2Wd-I_4eVbsYRVN_yDVS42rLw-GwhitE-y2DZMRPrQz2IubXjEKGdL3TYnFU0DdO84OmFEbqba-DH7kiU4uHBNexRkf_75VJq68XffngP-Z5ccuqNvU3_yg6Iy6qQ-wjZ9uQExvKTdV2e3h7zOzINfJm61LCRXXeCBPfo-CKRBIrGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تازه
سگ زرد: تحریم‌ها در ازای واگذاری اورانیوم رفع نخواهد شد
🔹
دونالد ترامپ در گفتگو با شبکه تلویزیونی
پی‌بی‌اس
گفته که ایران در قبال تحویل دادن اورانیوم با غنی‌سازی بالای خود، هیچ‌گونه تخفیف یا لغو تحریم‌هایی دریافت نخواهد کرد.
🔹
آن‌ها اورانیوم با غنی‌سازی بالای خود را واگذار خواهند کرد، اما نه در ازای لغو تحریم‌ها؛ خیر، به هیچ وجه این‌طور نخواهد بود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/654338" target="_blank">📅 19:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654337">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wwy6i9gh5CyTariC5TaFwDmduPI1-07z1to7BsCnJYFfHamjk3mxjSzWHR_v_JZIw9vDmv3rfW1zSGNNtaCPLTz0V7UiHcTKKlBnau0RwoRG31TGK8K90jyx3xjF5ErBV2PGv1HMBXwP3J6-rJe0pQbr6xwAyfB6N-gRCObXE3pbYYyw_3i5s1Cn5QFuL7ypeko9Ncu5dwoMkCPOSuJIvj_nL3y3onUXJoK0-idMKNsRf4zJxVCfL5djiftEzPWxawiR5ffe7EMBKEd5vYbAKkhPQ7QdjNgBXB9oQVmCAlwshEcw3DpAFSli7yRKiG2vcsKKa4IcE87kDZYOAQxW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار امنیتی؛ عکس انگشتان‌تان را منتشر نکنید!
🔹
کارشناسان امنیت سایبری هشدار می‌دهند که با کمک دوربین‌های پیشرفته و هوش مصنوعی، ممکن است از روی عکس‌های واضح دست، اثر انگشت افراد بازسازی و برای سوءاستفاده از قفل گوشی، اپ‌های بانکی و دستگاه‌های هوشمند استفاده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/654337" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654336">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
احتمال اعلام یک‌طرفه نهایی شدن توافق توسط ترامپ برای فشار به ایران
🔹
منابع آگاه می‌گویند ترامپ ممکن است طی ساعات آینده به‌صورت یک‌طرفه اعلام کند توافق ایران و آمریکا نهایی شده است؛ اقدامی که با هدف فشار رسانه‌ای و القای توافق پیش از حل کامل اختلافات ارزیابی می‌شود.
🔹
در مقابل، یک عضو تیم مذاکره‌کننده ایرانی تأکید کرده تا زمان حل کامل موارد موردنظر ایران، هیچ توافقی نهایی نخواهد بود و در صورت جمع‌بندی نهایی، تهران رسماً آن را اعلام می‌کند./فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/654336" target="_blank">📅 19:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654334">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1SH3-D2w_d8sn2ORtUuK3IvVoudmwEZg8txdaC-ftKNkMu6I5PYjKNjhYQYMHDZOWJ0MymtVdloVKbuZy5ac3hmxtSyGFMSv-yAcn_aXlrku2eshrzjy14U4tnC2bvi6t1gshZVYAUZRecTQ4_WbptApTIcsc2wPX3NwZGL8C300FwGc-Z04SrhWRuxhqgDptlKMfCeot24YScL4WHmzC5l_OH8Fx6a1Uwl3tPyoGSCtPIBD5oLGow4U9yJnIHuEhu56y2nWXpjeyu7FToAgwkTxVh9SmyEKAnqO7rjWrK8Vqz01U0e4mP3ibubeKl0f9CWUQUyA4nX9pIRBxKKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد شکنی ترامپ در خالی کردن ذخایر راهبردی آمریکا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/654334" target="_blank">📅 18:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654333">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02107287eb.mp4?token=C-doXsJmbPmHu53cV-XElThCkupg6GLnswsvyx299-sqZVSjqRIqG2L4Cyd4-yckUZ6PJao_9s-dceOZ8lfOkggs8Et-DjGoYHnB13NWUJ7GfkuWB-hw_XBY-WGjNb7TT-QjsycksWU0Ve-AkiHzBRlBl78vVqOgYMjdMpfqxgtOKnEQdFEDlbbUGy_uMAUWNOybLvSdnx-CJgmxhQhX7AfOmrpezwVUbIswdJkynsr3TlYAK0erm7149IzANlU1gSAK7npU83Nxenlsgpng34UuLmrrbtiVj2Hxl_MsBPaJAgyiblt-JjPy_9Z0DF_D_XZ1D1QZ7EctRC-qTk1c9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02107287eb.mp4?token=C-doXsJmbPmHu53cV-XElThCkupg6GLnswsvyx299-sqZVSjqRIqG2L4Cyd4-yckUZ6PJao_9s-dceOZ8lfOkggs8Et-DjGoYHnB13NWUJ7GfkuWB-hw_XBY-WGjNb7TT-QjsycksWU0Ve-AkiHzBRlBl78vVqOgYMjdMpfqxgtOKnEQdFEDlbbUGy_uMAUWNOybLvSdnx-CJgmxhQhX7AfOmrpezwVUbIswdJkynsr3TlYAK0erm7149IzANlU1gSAK7npU83Nxenlsgpng34UuLmrrbtiVj2Hxl_MsBPaJAgyiblt-JjPy_9Z0DF_D_XZ1D1QZ7EctRC-qTk1c9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدرو سانچز، نخست وزیر اسپانیا: من معتقدم صلح با موشک ساخته نمی‌شود؛ بلکه از طریق گفت‌وگو و احترام به قوانین بین‌المللی ساخته می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/654333" target="_blank">📅 18:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654332">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مخفی‌سازی لوکیشن در عکس‌ها؛ مراقب حریم خصوصی باشید
🔹
آیا می‌دانستید هر عکسی که با گوشی می‌گیرید، وقتی آن را در شبکه‌های اجتماعی یا پیام‌رسان‌ها به صورت File ارسال می‌کنید، دیگران می‌توانند بفهمند عکس دقیقاً کجا گرفته شده است.
🔹
برای حل این مشکل در گوشی‌های آیفون موقع اشتراک‌گذاری عکس، روی گزینه Options در بالا کلیک کنید و تیک Location را بردارید.
🔹
در گوشی‌های اندروید نیز از تنظیمات اپلیکیشن دوربین (Camera Settings)، گزینه Save Location یا Location Tags را غیرفعال کنید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/654332" target="_blank">📅 18:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654331">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkvE7s55pevjPegfqd2vGs16Ydey7cqn1VhsQ481hwn5CWgNqf35VlatExg_mmLa63ZjX3FyABQmcAxcX7OskHm9fCkWclgg6I5fX2ncKrCHqdFDGJsZYCoV3YaQPodETc8ri8c5uDYgvbD0_lWDGML1BZLAtF98Vqi4lPUC3Cf3b7LvMlXG2au-iurSnZcsGEKm1YmtBK108XuM903Isz-SSIrmQSul9thEBaoJ_r15BuGMd1JfR5Ozmf8EzqKuVlmFY-IbbnJ4j821slN5JHGURHnLdxRsG80Nmf-5taFanzxxqL15tiAbRTXrPCzHzGmiwGuPHWocaGvIKaPCkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطر تبدیل شدن اروپا به کانون ویروس چیکونگونیا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/654331" target="_blank">📅 18:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654330">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSuk_g2pqstnOnSz62gRDxHnMUP099IroTTTDIjgKL9Gsx2KPLl-EsNx0CtmhvjL0GZc7pW2vq-skgup5DevVfZDAI6X2QKaYxDZ6URC3k8dniz0HTeFj-HEX4Tl6kU4yWGq1GQXplpUXpBHJwvRxFBMMKMv6wDGmfQWwZkhElqvfdGUZXugXvmAbvQ1MvcBfmsR-8rNu3maS8lr9w7RokOG8HkT_IzulQe8CxKyVkPu7XdRskvEVpdHPbpXZgXVNBc_aNiD10mbFuryqdDjCp0Ar1TzuDjrQ_reK8sD-2Z9mOezOiFSni0Yb0SmfFmT2NOdeDYPdC9wNfzSQoN4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طنین صدای مظلومیت کودکان میناب در قلب اروپا
🔹
کولیوند رئیس جمعیت هلال‌احمر ایران در نشست ژنو، با حضور مدیران و روسای نهضت بین‌المللی صلیب سرخ و هلال‌احمر دنیا ضمن تشریح جنایات جنگی در ایران، عکس شهدای مدرسه میناب را به نمایش گذاشت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/654330" target="_blank">📅 18:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654329">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار کودک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn0VaHAbmr35SaZ_07b9H2XZBkIRCDtKAeAIOkWkiu4EAp7yWELHVQFjLL12xXXyrUpzdAUdTbgA23LMEmaePO3fs-R3Tz9JIVcAIPUFVWXEQVOaTN2L93p2gJ3ElaUZC47Q2kp1dkPB72TfnXvLePgS1JnstLNVf3z1tlRa3CBKzYYPnpShVAk9B0_7sBKuINiv7-Eluj5e32ZHv_tnUAA1VMikjFsaMmWKiSPRVkb71OmvtROAvrPn7XY13RJoTO2-kgOXKWA0OXVrKzgZ2CaL9ohIlEGwW0oLQkFJzZAWmXJVN_4FYJkynLS5r8uAs8f-DkLBm3Uy1mdmLaXGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
✨
پویش قرا‌رِ غدیری
✨
🌼
بچه‌های عزیزمون قراره با دل‌های قشنگشون، خونه‌ها رو برای عید بزرگ غدیر حسابی رنگی کنن
💚
با نقاشی
🎨
، پرچم، ریسه و کلی خلاقیت خونه
🏡
یا اتاق‌تون رو غدیری کنین از تزیینات قشنگتون عکس بگیرین
و برای ما بفرستین تا همه با هم شادی‌هامون رو شریک بشیم
✨
📸
منتظر دیدن هنرهای قشنگتون هستیم
👇🏻
👇🏻
:
@ertebat_gharar
🌟
بیاین با هم یه دنیا شادی غدیری بسازیم
🌟</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/654329" target="_blank">📅 18:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654328">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECuxs4jFe4r3kfWXeznCO5pJ5Mp0cD_pLKGFonR49xRD8IkMwRImpK0iAaPhMgbpelEDSe8wp5oO8uZA8MSDspKEYafexathYBOXItfBddkKqnShd1T4FlgP6AAMSbVKAAz5XFDTVhDFSQruPeNwHzJI2WAmnFCc2ds7iGicOh987mR85H5zlB3KMGfc3Z2-tBqNGowcQbagiRdE_GXHC7WkCQj6Abd3GkFrmNSDid8G5iEBrnUw9OXGlj5IHsFP8PLpOtRixDOy3E9M03P3v9OMNkvzMkiqPl7muHfJQjTvDZvDHTvNcw0QSkdOo38-mNjaoEtPyJ6k4mnQo1quSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حریق در نمای یکی از برج‌های چیتگر/ آتش اطفا و عملیات جستجو و تخلیه دود ادامه دارد
سخنگوی سازمان آتش‌نشانی:
🔹
دقایقی پیش یک برج مسکونی در منطقه چیتگر نمای ساختمان از دو طرف مورد حریق قرار گرفته است.
🔹
آتش خاموش شده اما تعداد واحدها زیاد است و نیروهای آتش‌نشانی در حال عملیات و جستجو هستند که محبوس شدگان احتمالی را پیدا و به بیرون انتقال دهند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/654328" target="_blank">📅 18:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654327">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آتش‌سوزی در فرودگاه امام خمینی
🔹
دقایقی قبل یک ساختمان اداری در شهر فرودگاهی امام خمینی دچار حریق شده است. این حریق در یک ساختمان اداری گمرک شهر فرودگاهی امام خمینی به وقوع پیوسته است.
🔹
تاکنون از علت دقیق حادثه و میزان خسارت و تلفات احتمالی اطلاعاتی در…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/654327" target="_blank">📅 18:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654326">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای تازه کاخ سفید درباره توافق با ایران
🔹
به گزارش الجزیره، کاخ سفید مدعی شده است که ترامپ تنها توافقی را امضا خواهد کرد که به طور قطعی تضمین کند ایران هیچ سلاح هسته‌ای نخواهد داشت.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/654326" target="_blank">📅 18:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654325">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHNS9fNH5Fq7XeJ0pjc3CRhlH6jYLlLvt8Q0X7-4Dgw6L_mnHSiB-R8X1IN7JyM4N2PjI-B1m-awC8aSjfPuYHy6fcu4IqXHDSzL6cZfxcXO3yxTO5eVVBHGpomrqFDRdY3P7jDonarwnMkRz6Hpzm5CqBepIN21b2DSZoja_Eg2AHuUVBNXnHvO2ZHLmAHYbsuyt3qqYGZvhK3YzVnqIDZvZm9zdYul1k8oCks1DNcpJmgjCHTeiJqrCefHgD7ndpaw0iAngLPP9jxvg4Y8qQpDFq6p272ShkKTna2X6KaP-7TnBLspyVJUAyfrRxrdnnpFhYomwKMWREkq0RturQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیماری‌هایی که ممکن است حین ذبح گوسفند به انسان منتقل شود
#سلامتی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/654325" target="_blank">📅 17:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654324">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای تازه کاخ سفید درباره توافق با ایران
🔹
به گزارش الجزیره، کاخ سفید مدعی شده است که ترامپ تنها توافقی را امضا خواهد کرد که به طور قطعی تضمین کند ایران هیچ سلاح هسته‌ای نخواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/654324" target="_blank">📅 17:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654323">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3knYYBLWJRqpvy8Apd14YizkIvjCA0yBQvrNy6K7jP2b07TLZAsgLe32bXBC-Ft5pRaLz-7MTPznYBbSQ9uw2hF5egnt8x7d1Q26M8VxKFO_6rg2SPJtVNgH7Bjrm2FkkcgCglTNH4B0u91cWM20usFn_pbGuN0Y6iUjZwThfvj6G0DlV57S9e9db5RFMJOeboiwrMcjTEevIKt4dYFv8x3bdi4gawqvEZvUIB2sgE7LbtWa5vqB4ZS7OZBZaM9zYTG29mQewRLFhooRV2MrzDe6gA4hgQ4wkDZUrDD3TRMHl3sg2msSW4_MsEINa2MQgq0N_EI08UohQJFepoSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار به مناسب عید قربان؛ دستخط یادداشت شهید دکتر علی لاریجانی از متن مناجات امام حسین علیه‌السلام در دعای عرفه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/654323" target="_blank">📅 17:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
آتش‌سوزی در فرودگاه امام خمینی
🔹
دقایقی قبل یک ساختمان اداری در شهر فرودگاهی امام خمینی دچار حریق شده است. این حریق در یک ساختمان اداری گمرک شهر فرودگاهی امام خمینی به وقوع پیوسته است.
🔹
تاکنون از علت دقیق حادثه و میزان خسارت و تلفات احتمالی اطلاعاتی در دست نیست. نیروهای امدادی و آتش نشانی در محل حاضر هستند.
#اخبار_تهران
در فضای مجازی
👇
@AkhbarTehran</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/654321" target="_blank">📅 17:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRNC2QoWCdmWyffmz5fQmKnzskMqrPds26kizWFz8mMYXdkyqqc-TWwSgzYhLzvq77DeRrTc529d3dlxgph-9MapYv-1LKUkpFNxH_RmVF4An_AIwGj8X6su8VWGuqWSqz4WLK50F9IBU2ks1MRcPO2VQ0QLW76s9z2lbrE6aL7UOHn5eIOpBccNT-OJE4ZfHcGiQ536-CD_RK7y7SkdOmS0Z0pi1ReC3VfZFMDpf7h3B6CYdzVL6nHv8HvnOziCpRnBXmq5j2cG8rf-n-Ytr9ozSPl0wJKzmxhZrgt374NgGq6dfefr0-N-ija_mnkHZAs7GaLJ6d3hInS6q4gfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناسا قصد دارد تا سال ۲۰۳۲ پایگاه دائمی در ماه بسازد
🔹
امریکا قصد دارد پیش از پایان دوره ترامپ فضانوردان را به ماه بازگرداند و سپس یک پایگاه کاملاً عملیاتی بسازد.
🔹
ابتدا مأموریت‌ها توسط ربات انجام می‌شود، سپس ماژول‌های مسکونی، سیستم‌های ارتباطی و نیروگاه هسته‌ای ساخته و به عنوان سکویی برای سفر به مریخ استفاده شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/654320" target="_blank">📅 17:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
الجزیره: جلسه ترامپ با کابینه برای نهایی کردن توافق پایان جنگ با ایران
🔹
در وضعیت فعلی، ترامپ این ریسک را دارد که پایان دادن به جنگی که خود انتخاب کرده، با پایانی نارضایت‌بخش همراه شود؛ زیرا توافق در حال شکل‌گیری، بسیاری از مسائل حیاتی را به آینده موکول می‌کند و این مسئله او را در معرض انتقادات شدیدی قرار داده است آرای جمهوری‌خواهان را در انتخابات میان‌دوره‌ای در خطر قرار داده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/654319" target="_blank">📅 16:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9QJ6PjefniobjyOHkwA3Rw7Qcm2up21OtZi1UtFln_JWYj1q9qrYrQE4a5JsHnge2kva8eISItN-sEEvcBSz_E3QbwKpcoLvq5OKiDJfzbkEOTLyIakn-qvaSNas8ymzLEYnvfi54Cw0CmT7H14dPBfyJqaQg0lVFo3atbTyRn_pQbm2yO1Xgr8PmWUTNrcY10IOb11HMshuFg0L_v-rEzYu9TkJvrq3RiIpFaEAzJMMVxjyyGqiiOHgpHYtIgn2zyaavZ97gWGcgZs966u3C-vAvnLWRET6SIGPdAGfoD2a_mQQ8h6sVhlZ1kDHPLVxXt0KIPUjhekdEgLtnAoxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین قیمت نفت: ۹۵.۱۰ دلار
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/654318" target="_blank">📅 16:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اقدامی برای کاهش هزینه درمان؛ حقوق گمرکی دارو فقط یک درصد شد
🔹
دولت، حقوق گمرکی دارو، ملزومات مصرفی پزشکی، شیرخشک و مواد اولیه آنها را به تنها ۱ درصد کاهش داد.
🔹
ارز مبنای محاسبه حقوق ورودی این اقلام، دیگر نرخ‌های دستوری نیست، بلکه نرخ ارز مندرج در ثبت سفارش تعیین خواهد شد. به شرطی که وزارت بهداشت عبارت «ارز ترجیحی» را در اولویت گروه کالایی ثبت سفارش درج کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/654317" target="_blank">📅 16:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654312">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
باقری: ایران و عمان به طور مشترک در حال مذاکره درباره سازوکار مدیریت تنگه هرمز هستند
معاون دبیر شورای عالی امنیت ملی:
🔹
شرایط و رویه‌های عبور از تنگه هرمز کاملاً متفاوت از شرایط قبل از شروع درگیری بر سر ایران خواهد بود.
🔹
تا زمانی که در مورد همه مسائل به توافق نرسیم، فکر می‌کنیم که در مورد هیچ چیز به توافق نرسیده‌ایم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/654312" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654311">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
رکوردشکنی خیره‌کننده بورس کالا در اردیبهشت
🔹
آمارها حاکی از آن است که درآمد بورس کالای ایران در اردیبهشت‌ماه به ۸۶۳ میلیارد تومان رسید؛ رشدی ۱۲۶ درصدی نسبت به فروردین‌ ماه.
🔹
درآمد کارمزد معاملات نیز با ۵۷۵ میلیارد تومان، رکورد قبلی مربوط به بهمن ۱۴۰۴ را ۳۹ درصد جابجا کرد. درآمد انبارداری هم نسبت به فروردین ۳۸ درصد بالا رفت.
🔹
جمع درآمد دو ماه ابتدایی سال با رشدی ۱۶۵ درصدی نسبت به مدت مشابه سال قبل ۱۲۴۴ میلیارد تومان شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/654311" target="_blank">📅 16:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654309">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
مقتدی الصدر دستور انحلال سرایا السلام را صادر کرد
🔹
رهبر جریان صدر عراق، امروز دستور انحلال کامل سرایا السلام(گروه نظامی این جریان) و پیوستن آن به دولت و مسئول کل تشکیلات نظامی خبر داد.
🔹
بعد از انتخاب علی الزیدی بعنوان نخست وزیر عراق زمزمه‌های انحلال گروه‌های نظامی غیردولتی به گوش رسید و این اقدام صدر در راستای این گفته‌ها اجرا شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/654309" target="_blank">📅 15:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654308">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqQw_TTEm6x-ltGzSieAuN1FsSE57B7fXnVjD2zYfn0hdUEz1iiQi5ovNo7hdGGzWjBhcs_OpwDJHb5vPjiP_JYWoKDzySPj-N30yhgZotINc_oK50STHMlasrw_WM37Ge2vySzacAbIFZGznx0EHu-s_FyYuiu4gNBAv_YmJhDlgwuQLB8odeYJWR3ItZqr5JcH3gyO6xpPh91-uKlJolXQeE2Bs6NrYavyF7fKTgeO8ZtiuIaNF7aq0vdB6fLurbH02OL_Pc_ao61yxODBiCVY_-5-gSElpcwAy0Ga0U_Jda5cCfOJ3jC0uS1HWEqGNlcYPIGWHeD1hdtqJfXCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل‌گر فاکس‌نیوز: ترامپ ناچار به دادن پول به ایران شده تا آبروداری کند
بجسیکا تارلوف:
🔹
ترامپ به یک توافق با ایران نیاز دارد، اما نه برای هسته‌ای برای آبروی خودش. او در آستانه دادن «پول قابل‌توجهی» به ایران است، آن هم در شرایطی که محبوبیتش پایین‌تر از همیشه است، قیمت بنزین به ۴.۵ دلار رسیده و کشاورزان آمریکایی التماس کود شیمیایی می‌کنند.
🔹
ایران دیگر تهدیدهای ترامپ را باور ندارد. توییت‌های زیاد و وقت‌کشی‌های مکرر از سوی تهران، قدرت بازدارندگی واشنگتن را صفر کرده./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/654308" target="_blank">📅 15:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654307">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT2G-NU70c9OwTNlO2XI6xIiNO8-GpBHJqP7qkmLeCwgqa6JbpuNTc2lQCqw1VvSdVqIIwZMa24ZrJjybTir2vSh55iiX3V1C5bFKeQvAOc23aldoFT8A1qNAOtQ7iHJpHyH_jku5Ypb_xM6XLXDVgdkKdsgeHQcIMAURDFtjK_Ixx9o2AhPBS8xXCy2UhfdxY4YgzAwRHzZ0NlppX7NXYnPniWlp6d7AuRSUY3MREcOGu6zX0_7oaO3zWFXKc5amTGQJqcbSSTofxnsWNL8ztzeXUYMLrNlYEAZgo49aB3WdGbce4M0rgM-PXPqOX-GUE2VlccB6TtQ5hWcy2RmBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین مدل‌های هوش مصنوعی به تفکیک کاربری کدامند؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/654307" target="_blank">📅 15:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654306">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زارعی: ترامپ نزد مردم ایران به ۵ بار اعدام محکوم شد
مجتبی زارعی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
پیش‌نویس‌ها و هماهنگی‌های اولیه درباره طرح ترور ترامپ در کمیسیون شکل گرفته و پیرامون قصاص فعلا مبلغ ۵۰ میلیون یورو تعیین شده است.
🔹
ترامپ به خاطر کودک‌خواری در جزیره اپستین یا توسط آمریکایی‌ها کشته خواهد شد یا در دوران ریاست جمهوری توسط خونخواهان به درک واصل خواهد شد.
🔹
ترامپ مثل سلمان رشدی برای همیشه باید با تجارت و قمار خداحافظی کند زیرا اگر از دنیایش یک روز مانده باشد حتما قصاص خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/654306" target="_blank">📅 15:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654304">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ریابکوف: سرنوشت اورانیوم غنی‌شده موضوع گفت‌وگوهای آتی خواهد بود
معاون وزیر امور خارجه روسیه:
🔹
پیشنهاد روسیه برای خارج کردن ذخایر اورانیوم غنی‌شده از ایران همچنان روی میز است اما مسکو کمک‌های خود را به کسی تحمیل نمی‌کند.
🔹
روسیه بارها به آمریکا اعلام کرده است که آماده است اورانیوم غنی‌شده ایران را خارج کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/654304" target="_blank">📅 15:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654303">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
جزئیات اولیه از چارچوب تفاهم احتمالی ایران و آمریکا
صداوسیما از انتشار سندی غیررسمی پیرامون تفاهم ایران و آمریکا خبر داد که محورهای اصلی آن عبارتند از:
🔹
رفع محاصره دریایی ایران و خروج نظامیان آمریکا از محیط پیرامونی ایران.
🔹
بازگشت تردد کشتی‌های تجاری به سطح پیش از تنش‌ها توسط ایران (طی یک ماه).
🔹
مدیریت مسیر تردد کشتی‌ها با همکاری ایران و عمان.
🔹
تبدیل احتمالی توافق نهایی به قطعنامه شورای امنیت پس از ۶۰ روز.
🔹
این چارچوب هنوز نهایی نشده و ایران بر «راستی‌آزمایی ملموس» پیش از هر اقدامی تأکید دارد./ میزان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654303" target="_blank">📅 15:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWvSyGopHVhDsuXbNE4owHPVXXonWK0VOmPxhIaIQes_LGh_4avY--qQIA4aYKaojRl-Wlhn8m0Kvpz2TybG8INM-L03DUcneBllOhMWT2kcf2TFxFkiGIrXifW8yTWb4khZ69vQOejaL8cRI9KO7nhrxDwxv7nxD4-pcp12UvmMTou20B1ywTYcC4Fw-8Iaa7xiQbcoulOBV1KT7-EKSY0JwSb4S7-Uvbf4mZMEoHx4Yruts4l_FtwtlyTRaNQIxjW7mNTdts_23_WyH_qB4B_AzpUl1E38BqjmlGGlTHO-omjTE_ZRAqiz00_9sy7oNUHpHRvwppUDcG4CSwg9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: ترامپ برای رسیدن به توافق با ایران، باید تحقیر را بپذیرد
نیویورک‌تایمز:
🔹
ترامپ برای رسیدن به توافق با ایران ناچار است «به‌ میزان قابل‌توجهی تحقیر را بپذیرد» و از سیاست «فشار حداکثری» که خود بنیان نهاده عقب‌نشینی کند.
🔹
نویسنده با اشاره به اصطلاح “eat crow” در فرهنگ سیاسی آمریکا تأکید می‌کند که شرایط کنونی ترامپ را مجبور کرده به سمت امتیازهایی برود که پیش‌تر آنها را نشانهٔ ضعف می‌دانست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654301" target="_blank">📅 15:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654299">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: عبور شناورهای کشورهای متخاصم از تنگه هرمز همچنان ممنوع است
🔹
۲۳ شناور تا این لحظه از تنگه هرمز عبور کرده‌اند و عبور شناورهای دیگر نیز تا ساعات آینده ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/654299" target="_blank">📅 14:46 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
