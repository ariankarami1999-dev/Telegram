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
<img src="https://cdn4.telesco.pe/file/gggBcrXKwiA6b7sjN8eYBsXdfxFxUJHxh8WdOLDcHogXUArxophY-4bp4lFcxy2QeHknLMe6GKqSyf2_YfxxYv909YwRNc3D4sQWJEf1HVzAZfUChFdZIcXqJItADLNnnGqoh25Q7nzIOsB-k50awZHDj6eqKEsltl93QWmBomnhIpfLtDrLHKs1lIY8wOqQWAZUU-3XgXyJChnvq9RMRPWrvArt-bhWY4EWLA0zDKhv6D_FNLYJljoNbk4zkhyyRBvKc7ERhuGwzeKN5Jdjbe8xknIh39FOhbEyq4WZ6c0sy58hvHClSbXQ3BKngTFHXcDgN9lJ0o9PaQdaYm7Kxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 00:22:11</div>
<hr>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tTZzMplzaWAoi6Dbiifgg9cv5SryPq3XiuVsjrPVdxWZ0cfxb2vVu4pfqUmfJelmgV8b6-t484nCwJtA8w6rjMVauABA4Xar52lID1jQrSAnzBKbgo04RlJxKRDRbtWQDBMCICCV6SSBk3IR_O1RpIlussrMn7ggyCzEYhrdPGJMTzuNxjzdRhkTQqi5E3HiHgvpQkVHQshT4eSLhEPL5pnofhh54GtMDBLIlX_1IGLIGThnvj7PQ0yvsGo8ImwmUGzdOozUmv5L3hAJWJjc9xjamogbnPBqHscfMKfHAzFN4b22JiOGHIya2zzMvsudSu1wIVEBUPmJpAG-YoaTZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tTZzMplzaWAoi6Dbiifgg9cv5SryPq3XiuVsjrPVdxWZ0cfxb2vVu4pfqUmfJelmgV8b6-t484nCwJtA8w6rjMVauABA4Xar52lID1jQrSAnzBKbgo04RlJxKRDRbtWQDBMCICCV6SSBk3IR_O1RpIlussrMn7ggyCzEYhrdPGJMTzuNxjzdRhkTQqi5E3HiHgvpQkVHQshT4eSLhEPL5pnofhh54GtMDBLIlX_1IGLIGThnvj7PQ0yvsGo8ImwmUGzdOozUmv5L3hAJWJjc9xjamogbnPBqHscfMKfHAzFN4b22JiOGHIya2zzMvsudSu1wIVEBUPmJpAG-YoaTZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iER6FA9e7nxY9M8TSdTlwo6h89qYM33Pu2lej9RROyZFpcfKBQaJid322sv359nmrQk2kTS3aKgUbOl9bZ5Jl2o3g29F26nBaFK64A4iwOU9yU7zItl1yEDyttjcpQdjrjMPy0e8n1sI1XHS63ok_XgKQXn0c2AUXbziOQsnAx-6X8Cl_SPoTrRGEPFnxwrOaxMn4JI8_LvvZ2aohf72RqZQ59WThVorvEo0dbWl2M13g5WUDyODI9cEZ9n6wRF3u3yZ4X4lDcU8remAu08Biy6lfvoGTdni_JhnH_UifP_lOCq36ngnuUlF7KnhPx9kxaL93qtb7owDnhSYMYYrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iER6FA9e7nxY9M8TSdTlwo6h89qYM33Pu2lej9RROyZFpcfKBQaJid322sv359nmrQk2kTS3aKgUbOl9bZ5Jl2o3g29F26nBaFK64A4iwOU9yU7zItl1yEDyttjcpQdjrjMPy0e8n1sI1XHS63ok_XgKQXn0c2AUXbziOQsnAx-6X8Cl_SPoTrRGEPFnxwrOaxMn4JI8_LvvZ2aohf72RqZQ59WThVorvEo0dbWl2M13g5WUDyODI9cEZ9n6wRF3u3yZ4X4lDcU8remAu08Biy6lfvoGTdni_JhnH_UifP_lOCq36ngnuUlF7KnhPx9kxaL93qtb7owDnhSYMYYrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP4vT26DbMfIlfgLMivVG7lutp701B9ejeapkLI0VrzVKU8LB7Rpp-MYYvHCktEgy4TwPnuSREmON4Wgqnpg6e94h0JY4LkYOnXPMN38jKz_2CxCvBFyMVUv5IqKYHIOzI_iupWrldaIQCXB6B3dJ_1nmo1ISta0JCFR6TuCeRLpsT2FxwY-Cs__7LdOwJPjdg5OhJo-vLfkb4KDFDmmR0c8r7vByxc-jJQ0sbH-anD6KNOyB0dAep2LXVaWTZQKuX5ov48GOGDHNaA5KTuY-9ndEiIVOpMPW7skJsiSszP25K61fdyg0ON5xH1NR0p3yNkRHfuewrO_X29ytGiHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vs9FTKdeDZgvZj0MBKsAA83lOMf-tZY0ojRCx73d_0OKQ_xVzYnLIi3uWnZM6flHqEu9JL0GRWpirffggSRbWuvSjG1AU1Ft0ie_q-AL9HeYxnhKkBat0lTdS3cffoycKTI8qVpBq1MOFYXaRIb34EstwnItTl71qoMFUfUbhsHafqhHFC6gziVrNi82K2sCwPi3AMNC_MLPi1Qb_7mOJrJEQCogkCnhPjRWKR4f_0gWxcrRwl5OJs5bvVlGdMYo3jNibKSgQydmfaqenaf2aZaCRlm3HuQrxhWiXl8pljXQbz-a7GP7hD3-Fh7JE9GhGYGonz-hhWXYRAqcZY5idQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vs9FTKdeDZgvZj0MBKsAA83lOMf-tZY0ojRCx73d_0OKQ_xVzYnLIi3uWnZM6flHqEu9JL0GRWpirffggSRbWuvSjG1AU1Ft0ie_q-AL9HeYxnhKkBat0lTdS3cffoycKTI8qVpBq1MOFYXaRIb34EstwnItTl71qoMFUfUbhsHafqhHFC6gziVrNi82K2sCwPi3AMNC_MLPi1Qb_7mOJrJEQCogkCnhPjRWKR4f_0gWxcrRwl5OJs5bvVlGdMYo3jNibKSgQydmfaqenaf2aZaCRlm3HuQrxhWiXl8pljXQbz-a7GP7hD3-Fh7JE9GhGYGonz-hhWXYRAqcZY5idQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=E848AjbmUxMz0iDTkvGp__69amNvpEbjl78K34yQIS4y9n1E0x1BTRqTbCkHSvd3J_mj0vmvR3RtzLy2LcjrlVENNh3XIlcklkOTKo-Exs0tm6YJ96DA6lrH4DS4Z0PMupoCwB009-Xc3THQoUcWG68ZefMinAq7CTg8tVztYYSqO1-6wo9XeVsK4wCMeUhkZS6S2XfL2heDyXvFMFJ0qToZ6oqNKpHjVDA0KSsJo55EoBAgqOuXkg5SJMjI5AfiEXSLfMB6CPI3mKZQ9M2Am9ucEqzxADyOy7m6RWoyqelVntbeykYs1mb7gl8ufMaQmQV2YH8wClzEs4-DqdA9vTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=E848AjbmUxMz0iDTkvGp__69amNvpEbjl78K34yQIS4y9n1E0x1BTRqTbCkHSvd3J_mj0vmvR3RtzLy2LcjrlVENNh3XIlcklkOTKo-Exs0tm6YJ96DA6lrH4DS4Z0PMupoCwB009-Xc3THQoUcWG68ZefMinAq7CTg8tVztYYSqO1-6wo9XeVsK4wCMeUhkZS6S2XfL2heDyXvFMFJ0qToZ6oqNKpHjVDA0KSsJo55EoBAgqOuXkg5SJMjI5AfiEXSLfMB6CPI3mKZQ9M2Am9ucEqzxADyOy7m6RWoyqelVntbeykYs1mb7gl8ufMaQmQV2YH8wClzEs4-DqdA9vTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IotlhauxxamIoDVWB22596GsxhSImjjoU_l-RM3CIcp0hXl4G0fOXuVibEkxZIx2BZ3mqc6SOxR-iwulyUDdr9hlT8tNAGFOy4zwZxBuBsrfofLanDNYJxHgzMdi87aIPH3UEWDbmpJ0G075KHvCuGJnoi3k9WVlLN1y3K9dmvOpPWMvlQJt9EEtsagGgdeQJ5rY-womaGpExALUJnuXkEBji9W1a2_UVWLil_PcUrc-0Mt1gc4nJhVtF7iYrQx6Sdb0ntH6iKm3gT7cR_6NNjOOwivUuqMgb-nsEzDgW_p1wGaqx_6IU3IkfCEQ8-L0yys12NA7EHrx-hGYWYCH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh1gIiMO26gKmECsuBu-x7k7PHtOiBsdlmJvQDDWm9Iu4VRDM9H8ysl3rF1ztO0H9CVJQTQJh_gixp93GE6iF9sB08ueqJrv3RxESsmRam-I2-HbdJS1IJIrGrNP8_7obG_MfOEJ2xHxXXu9zQlWev68zWhM3xKr8wUKhZVLxYeEWBfzBhbK7g6LR7GH6jBVtHvZrsMwEeOrEV6FSqYs3gvFK_i9lC0h9QtHkxXPZaYPqzpN4v-aZ1e4KQzvDn02L5A3XfT-1EOpWeaDaC5epo6pbtaeV0e7OZQNvlhitP0LsH4oH2Vw3F-p4NALcS3byWd5oN9vThs7ng8bR0ESgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvHwqgI2ExWT3XuUSw163hbtaLrav_ZRLgUnBBkSckizl2iotJ3uGW8JdizVmP95Dlt-9wN7lZx-GxA0roUBIk4trkNLCcf27_xYee3NIzlB28H08OGwJlf5JJe_4ZIJSvunHLusgqlKwJap83XQmFRPoKuercvuMz8zau-qSsmsMe_mqIk8j07FupptfA1t1jJgUCNQI1Xa1ffiWc3NP4Omhv6KmW58gea19p78DndxXpGl_uUR3HRLrfUf2rrNBtY0WjT2NwKb3_WsxwH1gffr5XUcmRHyuqsnv8JaMQPH66d4HaRs6fahIt3AXf6PESxgMT1ivJVUbLZilcMp4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=sPfSjsI6evb3QtXhGwKpeIKxSTR838-jugCUIKroi3aKZ7JPzGa8AhX8XlCfK9O49q1zW9en989bY5rPXjucAsNstIhMsA89ijrz0rSpo9XTG_KSgfbBbaD2tGUDX83ALypa6A0FzvKf4XDJDvrWgY58dOLyXgkdYUaDEG4PS3IvSt-brmVbaKzJBhEwn--0_eE7_VGopHD9tcOCFF5D8IE9cL7WwX-eOs22zI7pGnPtMXcE7mVGIV2K0F2VfxDPPpYUvsSybQSfEI4ztd5rtQLOKJzuy9BdnYC7FTOZqjuTvey5KNCHSRvjmKo2dFH-HDrmXvnEsK5rcpoUz-0JSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=sPfSjsI6evb3QtXhGwKpeIKxSTR838-jugCUIKroi3aKZ7JPzGa8AhX8XlCfK9O49q1zW9en989bY5rPXjucAsNstIhMsA89ijrz0rSpo9XTG_KSgfbBbaD2tGUDX83ALypa6A0FzvKf4XDJDvrWgY58dOLyXgkdYUaDEG4PS3IvSt-brmVbaKzJBhEwn--0_eE7_VGopHD9tcOCFF5D8IE9cL7WwX-eOs22zI7pGnPtMXcE7mVGIV2K0F2VfxDPPpYUvsSybQSfEI4ztd5rtQLOKJzuy9BdnYC7FTOZqjuTvey5KNCHSRvjmKo2dFH-HDrmXvnEsK5rcpoUz-0JSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaadJEufd-eQaZxQuDB6UdiReVN2_pjz3rAj5RxYaztdlPyfhLBPuV30IAIckKPrJlzmj1EtN_FqTJpCfrUljpwWeOKnhuT97skJLCJ8SxuBti6nOGSJhFucmKbOUaIZsFkCmDTAaD9TWXRXsEJfZ0KlFCAxqKu0FEUGVD78uzF-QqGQUdOsRRs4Itjg32HLgAm4CJ40TmgUmNGyd5q26SoHpqpeHNeVC4BuRW8jumo-GEMRZH61rCioF8Sv2bs-WXoqU7suKlkKiKOKxOPeU46sEE4kHiOa-irhGTzbx0OU6AegBCyY4CHPKVNUlYa_fCTrdGlQkKREBd9sP21wHE5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaadJEufd-eQaZxQuDB6UdiReVN2_pjz3rAj5RxYaztdlPyfhLBPuV30IAIckKPrJlzmj1EtN_FqTJpCfrUljpwWeOKnhuT97skJLCJ8SxuBti6nOGSJhFucmKbOUaIZsFkCmDTAaD9TWXRXsEJfZ0KlFCAxqKu0FEUGVD78uzF-QqGQUdOsRRs4Itjg32HLgAm4CJ40TmgUmNGyd5q26SoHpqpeHNeVC4BuRW8jumo-GEMRZH61rCioF8Sv2bs-WXoqU7suKlkKiKOKxOPeU46sEE4kHiOa-irhGTzbx0OU6AegBCyY4CHPKVNUlYa_fCTrdGlQkKREBd9sP21wHE5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if2isJUAW6XeM3cbi9dgilGPk-cQV5ajf8nvSQoxyk054DNKOsZ-ETQWi1SacNyF3Wafs1JiFI6021VrURAwEMnOnTHBWZ0JEW0ve4GDkGcLqt0yHJg6dpscN1v5pCY1nNRaxdmwwJy3VPzDgUV9pWZ1rPRk2tbFFc7lNi0ILr36rjJl9bvOyuUMPo2s6w8pQGKtaIP9twspAnMhpuFJPexVE8g9VUZ3ERmJnij9dmEY6ql_YnfsrhHsMPreTUzaOQ5l56wHnzA0Bmz5d3GfWzCOjBZBtk1T1V0PkyGbSuqz1sNRftfhA2J1q8Z1rEixOMtMxZd6CRy1XlUlqEDtOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuThb6k0asFq6emuW5J7sBU7myVgh1o69VFaXTRTfse0R4tcvU_8_8cJF2XhTSWejsEQJoFJ4w0tPU5lC9AfBpBzv0b30CkLWhL2-UC0zInV5f4o5yOu-SibqVUgKWvGmaszvvWb93Y-SqsxgvlDWNZ9dDQz9QluPpgUL_1ABHOgQUqG2tA2-LXEvYgtU9opC11YXx903M8vD0uQQl3cN7-NyyUvKH57K1DVTDjaZTCZMhZuGuViDo2hCoKelvVyLfKKw0rSShNuxdVSgUHZYVLKYlNlU6vVqrt3MqAtVRoMPhmToTn6pLFEt5iJzm6QoVR-0bCn59lYRDOYhieGwd3zU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuThb6k0asFq6emuW5J7sBU7myVgh1o69VFaXTRTfse0R4tcvU_8_8cJF2XhTSWejsEQJoFJ4w0tPU5lC9AfBpBzv0b30CkLWhL2-UC0zInV5f4o5yOu-SibqVUgKWvGmaszvvWb93Y-SqsxgvlDWNZ9dDQz9QluPpgUL_1ABHOgQUqG2tA2-LXEvYgtU9opC11YXx903M8vD0uQQl3cN7-NyyUvKH57K1DVTDjaZTCZMhZuGuViDo2hCoKelvVyLfKKw0rSShNuxdVSgUHZYVLKYlNlU6vVqrt3MqAtVRoMPhmToTn6pLFEt5iJzm6QoVR-0bCn59lYRDOYhieGwd3zU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2eUKqlhmJbtg1wz1NSlqC9fcAUgjXQiP8ek9XYRAWnaIigrV172WEec2Djx3UuWwtQWo2saLUbqgfHg7y_Mss5Dv-KvOqFAu5QJ5pI_gDJyMTYoeN_UoVyKMdYeU4gwT8OdGDtgvuJTVZmGIn5KzMg1zZg54RMCn_KkNKQ8jhcde7zg49GHPYVZm_Y8jEMLnVRnXkzJy6w1z2_KQh_IdOIZ0hlcYg5KmfePYdWyfjkaLIOIA7qlP7t6zKMRhz46IrWpxZ2rZv7ZMpb_d1f8XljoYRhPmOKIwQ7ZbAy6-cu2r32yWc3zE9fsn6ldCgsEM9A_5-FRewn9qTIlfjKedg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Wt7X391b-EqSceld9EBP8zkwH_gvsG-YM_8_3SDG0jbQomznCmnzVEDysehJtB-YN4ZXk9Enp3HRAaizV7YPq8t9KYhr2AGV9d8KiW44_2VEaTfpWP2ReMTrNKO-lVL1SzUN8yHcFWJpB3TovKogUXNt2wghvE-h7D4A9lKL1M9KZV3H8Pqkv5TgkX2Sl3H7x691FNOQ2JFJlV8svAQ5ZeNJhZ39qa6mad3A7ryQ9lA2Dl1P4SCZQvwm1KjwyrklE3ZAK2KPjjwiAKK5faOoOrL0M0B7Y8ZOA4J32hFJfFE3rmhfo8LhsXYOMeZu1SahCppl35EHyjvCcZutR63qSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Wt7X391b-EqSceld9EBP8zkwH_gvsG-YM_8_3SDG0jbQomznCmnzVEDysehJtB-YN4ZXk9Enp3HRAaizV7YPq8t9KYhr2AGV9d8KiW44_2VEaTfpWP2ReMTrNKO-lVL1SzUN8yHcFWJpB3TovKogUXNt2wghvE-h7D4A9lKL1M9KZV3H8Pqkv5TgkX2Sl3H7x691FNOQ2JFJlV8svAQ5ZeNJhZ39qa6mad3A7ryQ9lA2Dl1P4SCZQvwm1KjwyrklE3ZAK2KPjjwiAKK5faOoOrL0M0B7Y8ZOA4J32hFJfFE3rmhfo8LhsXYOMeZu1SahCppl35EHyjvCcZutR63qSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Hf_5THS3S5SdRnZZDi1zEb2Mmr0yfIdzXHc-usiic6SxL2AFyjTxYBofvzeuyrHgp8DsyAOlKlO3PFCtvu8lyg6rLXuFqsaMBK4VsJ00jQcEKcxt9p8fSHx16ATiSDvagtUFb4tmZcIWguhOIccUEqsuuZQgDQPWHGrijqsEmGNGXBrVNOR4DSa_vY4AeNwVlIakPCe9EAiF3k82hTrh6EVCfxHd966rfxpmWpKWy-TBKvUPcQK8YyG0rzrB-ZiAKQ7nOIB9MEhRcHW8ZBgDABllVTUUEId31zIv_MP_pJB9sulyZuHaFVTfhzujZ-irA4m6URA0CfpQBHx1ltMp5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Hf_5THS3S5SdRnZZDi1zEb2Mmr0yfIdzXHc-usiic6SxL2AFyjTxYBofvzeuyrHgp8DsyAOlKlO3PFCtvu8lyg6rLXuFqsaMBK4VsJ00jQcEKcxt9p8fSHx16ATiSDvagtUFb4tmZcIWguhOIccUEqsuuZQgDQPWHGrijqsEmGNGXBrVNOR4DSa_vY4AeNwVlIakPCe9EAiF3k82hTrh6EVCfxHd966rfxpmWpKWy-TBKvUPcQK8YyG0rzrB-ZiAKQ7nOIB9MEhRcHW8ZBgDABllVTUUEId31zIv_MP_pJB9sulyZuHaFVTfhzujZ-irA4m6URA0CfpQBHx1ltMp5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=T440vcuVGF-QJSp4m9H8mssH0M-Uuk3n7tFN82sJXx42dDKs8UjCLhnoBVCZeNMEp-9totLFGT10HFOchwY7cWFwExTbunidiNhz0bYh0Gci-5Ri5pXFUwg2aE-c464GYy2EnsBCHuC1w6mJOXd0MrapNMDfWTXtbpv12IiyfVJMwQFY53lz8nw8g6nmy6FgH922mVovIu900WhAlAX03MIBbNw-nO2J-ekIJV2ffPpvqRpVxe34_GGq0_UrMj-n8SFplHcfXfr2cKjkFWxqdCHmMI5OrDqHWZgZ1gFDoQydm4QZgErxbbFTolPJCQ9_mCNcHmLrftTEIlP3e12V4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=T440vcuVGF-QJSp4m9H8mssH0M-Uuk3n7tFN82sJXx42dDKs8UjCLhnoBVCZeNMEp-9totLFGT10HFOchwY7cWFwExTbunidiNhz0bYh0Gci-5Ri5pXFUwg2aE-c464GYy2EnsBCHuC1w6mJOXd0MrapNMDfWTXtbpv12IiyfVJMwQFY53lz8nw8g6nmy6FgH922mVovIu900WhAlAX03MIBbNw-nO2J-ekIJV2ffPpvqRpVxe34_GGq0_UrMj-n8SFplHcfXfr2cKjkFWxqdCHmMI5OrDqHWZgZ1gFDoQydm4QZgErxbbFTolPJCQ9_mCNcHmLrftTEIlP3e12V4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns57GPpKmm5Y_eiJFYcqx-zIj5gSqLkgP_wsjZNGsYy24kcX-EeynV2_-LzIIPeNly_DiLJULjKY-S-M93OWfliEMc-ai_I0lK3mrqL0sbw6IlhocqJWW9Z8e70gA5_ZL_ssOQNDt7wxLoAYHCtbzbCz_E2iP40i4Zwwty-09PuNGAoCh8rIEGq5nfsUBOe2SUWxo_8HK8yexseBQ-bH1aEtWKiK8enJ80WBVr9CGLE7bkglMtM-i-YDHkV4-T1NHx_KhZvrPYJGaejCw5056z9-DtqpToDHlh9SRspxMPHNXIpnqhwqPk1Rph6Ag41Kcdu9xE6p0u3IYURGqvOJvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzu_btavXw3ZvXCs7ahJmIaW4OCkUBMHDw8qv1BRtXp2yK2flhKuDsxudSyXdnBwvU78UbEJ8mE6Ag7osXRXeVEyc5TEzY7d0LgONr1Cgk4DdxPrinua7QPiPXQvZvci_OXAvx9omeOA9I4-xW-i-cSdTdkFgi0U7BAaDRSYzhMYJX0l0cnQwYznshk9mUUneiHo1EQCOept0TvV1NG-rCG-Vnm5D4N6Z0h_yWqKQZzOM_ko6_0tZVAU93uSKbPVFypYSSBEoeb4kInopCHvT_6Dm911gR9Cn2HpaX1VJmnP7O-5mbdoAvhBjub9gf4thYmElvfZmulIpxfnqKwyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=slhOGWKI13GO96yR0yKQqJmzQRMtJhhEFAHmB4A015BHfvsc2NDcIkIQfLiw9Tg_C_dD_sT61Xl8-WBSea5ScjjG21wxiBS_s4SNeOEqBe09VXQ0s4VPCnuue8P7LnREPgFoBMPuIkd361uRi9LJM9aXMdzcd65PdMyArymMj9_iP-QAcUXFc1h4Q8jtrYYuDA8LbufLKlIh_oZ0ewRZYPk5t5aWC3eRYUNQKfrJhg5IggzMaOs2y3sUJ431ZEBrl2sl2o8Ksho7lHAwvCtetP6SYgxCVRpGmdgtxqGzURAdT5VXmP4zKUu9SKifZpfYVMho5kHvRGAlxyAZnrYleQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=slhOGWKI13GO96yR0yKQqJmzQRMtJhhEFAHmB4A015BHfvsc2NDcIkIQfLiw9Tg_C_dD_sT61Xl8-WBSea5ScjjG21wxiBS_s4SNeOEqBe09VXQ0s4VPCnuue8P7LnREPgFoBMPuIkd361uRi9LJM9aXMdzcd65PdMyArymMj9_iP-QAcUXFc1h4Q8jtrYYuDA8LbufLKlIh_oZ0ewRZYPk5t5aWC3eRYUNQKfrJhg5IggzMaOs2y3sUJ431ZEBrl2sl2o8Ksho7lHAwvCtetP6SYgxCVRpGmdgtxqGzURAdT5VXmP4zKUu9SKifZpfYVMho5kHvRGAlxyAZnrYleQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo5ptbsUoWZAuF4Dgzq_v2sfoXI30XHP4WarIobKFHU4DAaGgMcwctAzLCOd4n8bm43Cq7-m9DWOM6NCfXlX0uO6f5Wb90Bb41BhaXiao8TNrmSyXfyq8dQu7C6bKndgnJVwvN1EaE82SOQ1xHmMM135VoV-uCvD8Sgf6y6xWZjaMXluBZNjkrrrcQp5g2E-sSMCFA3nUGYw2sNDfidWnmO1gAiw7AIuOC3_MvgPqz4rYr_M-NjNwolRKm7t_Q8sc8unAcXspYpLaJvPsGEpZaUFbr9lBJiNanctOUS2ZSayOI0czkaT2-C5prh8D03Q9MPjIq8Og2vucwAbFzMsbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQK5PmctJhGE2EZVjX2Am8SQxDQ9D4QQ0jdeunhzcVjQCDAics4kNGEd1immUUXFCM-K2SIy_mFH3rpmvy_aD9a4FaLFp4QjHswzzLL9iHxrEByrW-GOOxMtEVavNJeRQd97iBWvEfhqszoB-uJ0uiU3d43VdWjWQdqwTC1xATkJfnsAMa0AQhaxwWwecgIgO4yqeazBnwXGTmFycRH9XFuaJXe5CgS1wTndfy4HPxLjhhxtdszY27ZglSIT5DYf090cMUbMs2WJpm0RVIWLiEmUW0ORa8JL_xZbilAVWUs4mmPqDwxK3TKcKHfwB2iu3O8cNrdAmr6q8pp1Uc9MNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=IRWgK_2kYG5-BKOTfUg9e_9Zzba9Pgu5COiM0agmM1TASrZ7xdOkJa_i2dccOlGrqufHlJkFV8Io4RmcSlvRlT8fXbjpL17ouJqlwreynWOPqan7m2E2-lFd3OI8_me5i_jJ5nST5m5ihxIIIvn_v3WVHtqR3ou9DCsxXDzVfC5eg23GpxlYmkp6LShF-OaIIyNcAxUCSqA3pTVwRGVKxXM4XgPz37Qr1xPw_P1xUTo2UPRAFvY8eTcjwSsg4e6E7HOYRt35PHQK6Ql6MjVkvCUz_AGigs61eh5euaRnV1lDJg31Kfcc50txMFQoF55vhYFTDZhxv7D38azhsT4gdy0TfrhCNkx8Wf9XZ563-N-QPAP0sdZrOXChSCgaPeVnwDjt4zGzjVNcOwnTXusMiWskHDIEqFp7JgTPtzRssGYL1um227xjr9sOwqFbh8Y246huIMv-1lhETP93ux3zSsn7-94LN72o9PsB3vqCkX0DNrm-OQeLnMmW26q_Ff5lZ22VNT-2N7nzwwxWVsnjTnT56sklIZlRJYXH5_AzwSKCTa54dmM8yuXK5jNAoJmxQM2MTlyLorWmDQDRMKdHgX0QWlAQ4Xf0gm0G_fr6FgwYo0l_rAFlrmX490VwQosR2D8kMJn3VfEpic453_9k2Z25SeN2_ToVnJSYGebfKx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=IRWgK_2kYG5-BKOTfUg9e_9Zzba9Pgu5COiM0agmM1TASrZ7xdOkJa_i2dccOlGrqufHlJkFV8Io4RmcSlvRlT8fXbjpL17ouJqlwreynWOPqan7m2E2-lFd3OI8_me5i_jJ5nST5m5ihxIIIvn_v3WVHtqR3ou9DCsxXDzVfC5eg23GpxlYmkp6LShF-OaIIyNcAxUCSqA3pTVwRGVKxXM4XgPz37Qr1xPw_P1xUTo2UPRAFvY8eTcjwSsg4e6E7HOYRt35PHQK6Ql6MjVkvCUz_AGigs61eh5euaRnV1lDJg31Kfcc50txMFQoF55vhYFTDZhxv7D38azhsT4gdy0TfrhCNkx8Wf9XZ563-N-QPAP0sdZrOXChSCgaPeVnwDjt4zGzjVNcOwnTXusMiWskHDIEqFp7JgTPtzRssGYL1um227xjr9sOwqFbh8Y246huIMv-1lhETP93ux3zSsn7-94LN72o9PsB3vqCkX0DNrm-OQeLnMmW26q_Ff5lZ22VNT-2N7nzwwxWVsnjTnT56sklIZlRJYXH5_AzwSKCTa54dmM8yuXK5jNAoJmxQM2MTlyLorWmDQDRMKdHgX0QWlAQ4Xf0gm0G_fr6FgwYo0l_rAFlrmX490VwQosR2D8kMJn3VfEpic453_9k2Z25SeN2_ToVnJSYGebfKx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmwqyUMUma4VSTs8N_wdF4c0V6-6cJtB-ONH-A4pL2BuBCVGfVlMa625-1NeOZNo-LS7mLVuS4zJVMptRMBl7zGED9cX4Mmgu9P1KR5GP2GXsg8lYdwe2GfmsxicwlVXPPyxch1vsaR9wzvhdgRUQGv4XMBrzr_p0ydUnwxR4l7dIP2yOCtxdEM_HP_edY7pznFTXdhN_by2FeEptUxi8zc8uSB05QO4hABkxtLmJFJtugCsnDXoyHJ8JQ0H1Ae8LwGCK1oxRJ5WHeSvKpvg9X_XKk8h4ZPSDtBnHB0PLViyq0R_Ov3zejqBrnQrMME8gQe4Jy8KrCkYkdvsonMwMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmwqyUMUma4VSTs8N_wdF4c0V6-6cJtB-ONH-A4pL2BuBCVGfVlMa625-1NeOZNo-LS7mLVuS4zJVMptRMBl7zGED9cX4Mmgu9P1KR5GP2GXsg8lYdwe2GfmsxicwlVXPPyxch1vsaR9wzvhdgRUQGv4XMBrzr_p0ydUnwxR4l7dIP2yOCtxdEM_HP_edY7pznFTXdhN_by2FeEptUxi8zc8uSB05QO4hABkxtLmJFJtugCsnDXoyHJ8JQ0H1Ae8LwGCK1oxRJ5WHeSvKpvg9X_XKk8h4ZPSDtBnHB0PLViyq0R_Ov3zejqBrnQrMME8gQe4Jy8KrCkYkdvsonMwMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QeBgfN2TGU3qKLNVv6wS21kn8AbAuEjEom-wvipv0JI9F20WcQvHyse6X_s0nQChswFusfz3msFzOqJFmCWzZgKGb4w7_Oll9gyEme0PsZMRZOFl4wdESY67s1hd6dfnwlj66cuYjnCi4g7GoV2wDny93Yiqq90hL8W8gaJaiyPWcENcQEtCAKlBOJAg6WrABhuGtWe8nRVd2CjsY_Snc-tNfYrV-UyTe5-cEs82sEY0rHeKwv6iaikzGTVEG8FoXsLQYWVV0Mw7L7hlEpe9WNLQuTqZ4s-6gur3yvlOMe_CXWe8c0KLAw5i3f_jAKtdbyx-yDXTQ4JWAgX8n7P51oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QeBgfN2TGU3qKLNVv6wS21kn8AbAuEjEom-wvipv0JI9F20WcQvHyse6X_s0nQChswFusfz3msFzOqJFmCWzZgKGb4w7_Oll9gyEme0PsZMRZOFl4wdESY67s1hd6dfnwlj66cuYjnCi4g7GoV2wDny93Yiqq90hL8W8gaJaiyPWcENcQEtCAKlBOJAg6WrABhuGtWe8nRVd2CjsY_Snc-tNfYrV-UyTe5-cEs82sEY0rHeKwv6iaikzGTVEG8FoXsLQYWVV0Mw7L7hlEpe9WNLQuTqZ4s-6gur3yvlOMe_CXWe8c0KLAw5i3f_jAKtdbyx-yDXTQ4JWAgX8n7P51oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=EeO9azT2a5gbP0YD0Vmysc_Vh_b0tgFXfVkGU6jgdwcFnspEpW0CAWHoBZHxhv0flQgVXQXfl2E4XvuYkrcRBIvG2wJTX3FCU4nmIP4I_3BgVTocnoUblMaqt5dv3MRjhgCJ0it5fUXFV_cTdU0wnQ0qI_VLZYorYvcV0iCYK93OX4iOZUHSJ0hNQ0oGWRZOru-kGMJBcqRh12VkuIyl7ymmOIFVRj3a5XHvMY3qJUxRgJfLyOrRROb-3FlevO2RFJv0nYEqZqCApwec4e1xyxWhA5ZxUG03G-P3TdqfXKNDc224lCYiZq83Aq2y45x_evzdjZe_qOsPIOrlwEtxTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=EeO9azT2a5gbP0YD0Vmysc_Vh_b0tgFXfVkGU6jgdwcFnspEpW0CAWHoBZHxhv0flQgVXQXfl2E4XvuYkrcRBIvG2wJTX3FCU4nmIP4I_3BgVTocnoUblMaqt5dv3MRjhgCJ0it5fUXFV_cTdU0wnQ0qI_VLZYorYvcV0iCYK93OX4iOZUHSJ0hNQ0oGWRZOru-kGMJBcqRh12VkuIyl7ymmOIFVRj3a5XHvMY3qJUxRgJfLyOrRROb-3FlevO2RFJv0nYEqZqCApwec4e1xyxWhA5ZxUG03G-P3TdqfXKNDc224lCYiZq83Aq2y45x_evzdjZe_qOsPIOrlwEtxTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIPzi7Ijl5oOOmpfE26SgI7UuQE-tDXZAjbEM4myZ0VmMQe5Z4DRpxXsv4y94GSMwSqqhAydnPRHw1vq44z6hGSUWYoFO30pglGFE0Se1_WyxZQanYHUQ63V8O_fm3drnV7mpDsmFdzXNswLvMpmUn1q2jLXrmqtjJs1Z8mWQKsTfKxsvJu2tnI_4l0odapP69ztZjKbFR8znKttn26TZdaIxTNazjW5MosLLvSFK0u52NCOViYVOYwhZP2GnhzCso_XeoPpkPNJ5-DB4hh5jOeJ4-N-gMtN_A_6leIo8naX7ak3wAfvaLzmdHq8ri0JdQ5sOykEzlCHxO2ckEuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0CqIcUOSkllu-iekGLtcDJJQy8Kf4RLH79TVYhcfuyBBzPz8tgucPxRYfEVXdf1eb5I0w03q8x4JbfxIMHwtU6csz5h3IoXzeS5K3F7iZ2MaRHH7p_QBRR6-qLKc1kyzJXYiC3hvBLMoW35sLqG8oP394OXZmbzTtv7S4YI1nKp7HIjwFutINRUG2NzffPh26jRcsaUBh4P51A6rGQtSa5H-WNDMFPodzMH4dTVOn3aXq5XuM5fGVu02pMg3wWrAv6o7jBbzc0HY05RHQkZfeLjf4LX_5c6DIppC_zUZDRx0esaBFRuzdVL9fKB1WzsZ0Jk8ac7VYIgrabmEtmGkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edbSAG-AqpAc4CaBntYGeEis1m81W1mP0ppEPnE0ZfzUyAjXOgitGxDEsGDNPkP2JnZLeOqZLrSotdZyciJe9eBpXfbtuselIra2bY_gSuBr0CB2Zk5028OuwvsHILrl8aW_GqibJ312-QRZucF25a8ov-R01Rc0eFPsvokYNubbAUGRI6jiQKgeyvf_3JUpm-7MpIDlM3RqGCXzrFPyaz6ZfyYkI1tkNQHq0QxvWw39Xswh2yWCz25vMA9OQjVyZTsaOatX2q5hhDZ6OpeUZ2ENnfKO8CEChlnUzPmbXODpH5LTMH4oc_-85UO0LJbNwCrMtT4BMtfg-xgzJ4MIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5iBT8YZ2GQrtfuTm00fBYQwJs46RzgT16Fkqok2VlqNs6SJT493RbRZRPq2p1Ah4yZY5qlbeXcsdJ2lfuAjx_bRIgwOzXIYMLdLBRy12xC2xmKpNbzEDPMhVnYmyYsUHOtNTSf3MWN_yJDnDb3psYEmSJmeuocKKcsa1z0vrbMdw1ujKUhGXMPgZu79cmLBoGQnXlrW8l6pqlz41LcPNUbqNQQUDXbvMHJXLBD0urq2e4pwre7yBtcsvPhkcVF-N8Tm0n2G1gXu4RdnFzKUnAMDNNIjdGJXZj-8g61ONLVtfAFCmFEchI2kGPgMAmuH1mkq6KEnFr5bbpX5RHKu6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgSvI-3Bjo41i6sMRPHfvmqHBofEQqvLp5HfKhK7BBZDu1y3Alz5Toc0QNVUthE_pabdx_OWW7zA2XXAlcu91NAIH84GqjVEmsxzCfdHySiq7QNxiAsWNe8sGFvyHelGaQqV-8vrV49_NrtgJmAT04YB_IkIeSMSrwvFcQ7r1pPLNH2mwzuMoNVeQOP3VmnQEimIqLZqS2ZcsDq40CidlHXrTkmafimLmfGSIdy2JO_y506AMEozOFsMBkYlmmbjX-upRUKjUBriTQiewbcFuv6-FAENTGAM1R0hFKWFXS19418hYNqrB4fOiOvDnsVCYysI5lS10F2kp4zmUuxPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=IwqWwtruEhnbPH-yDg4vFdZfO6qr3qRmZd_6zf9UpARzratDYs9LIXFqUhBS5e-HLocnPMAoBDmopOYEoEYNZt8RUk5WjsXwmIueUfNQ23Oo0JOtOUoeTj2L-2T0wsGPNTQcqEuRwD2FPcNShicV10RW4acBdd0NWnMZrvINwHyyIMxxUS6TLNJp9PVy9sK2X0vVV4-RzqqQkubismPFn0DCvJWDl1SLrYS4BxFGYjoXd3VIpv8STKXMc8ry7VwpsXIP5IfkEHVsIpoHOvy2ROlLVh2GZ65CSQvhHQf4VO9TLUOpp6_TJSELmN3EOVR6pOLf7Wvvp3B3_zzfmVJfRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=IwqWwtruEhnbPH-yDg4vFdZfO6qr3qRmZd_6zf9UpARzratDYs9LIXFqUhBS5e-HLocnPMAoBDmopOYEoEYNZt8RUk5WjsXwmIueUfNQ23Oo0JOtOUoeTj2L-2T0wsGPNTQcqEuRwD2FPcNShicV10RW4acBdd0NWnMZrvINwHyyIMxxUS6TLNJp9PVy9sK2X0vVV4-RzqqQkubismPFn0DCvJWDl1SLrYS4BxFGYjoXd3VIpv8STKXMc8ry7VwpsXIP5IfkEHVsIpoHOvy2ROlLVh2GZ65CSQvhHQf4VO9TLUOpp6_TJSELmN3EOVR6pOLf7Wvvp3B3_zzfmVJfRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=GiO7tUiEMxNHP3M91GqOg4bkK7Yw6o7y7BrIrbgOfVb6TQTI78R6_Mp1utLchQBfWrpWBgXjexResj6QxVmcDlh-6MCYjvjHNQxLZMrPL6NDx_D6uSslUJfbkblAWQmziZInvdOgfYKa1ImoT470vvV7ZM7nyNxy4c3s8vplKx9wegfSr9EweKpUJM2mTUnv4xFiBeBhKM_mS6bsMdMLYCxiVK5mIGRFpxiSJPnjXjtTFARCiNL94UmYU1sTSWtRBp3-Qz0Z5TiwIUhvuxkXefwiQtVpJkvUfiSVZeMixrzDOfONs4RkZ8leDiFjm5BMhkrVBqTCnK7woU8eFpqeaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=GiO7tUiEMxNHP3M91GqOg4bkK7Yw6o7y7BrIrbgOfVb6TQTI78R6_Mp1utLchQBfWrpWBgXjexResj6QxVmcDlh-6MCYjvjHNQxLZMrPL6NDx_D6uSslUJfbkblAWQmziZInvdOgfYKa1ImoT470vvV7ZM7nyNxy4c3s8vplKx9wegfSr9EweKpUJM2mTUnv4xFiBeBhKM_mS6bsMdMLYCxiVK5mIGRFpxiSJPnjXjtTFARCiNL94UmYU1sTSWtRBp3-Qz0Z5TiwIUhvuxkXefwiQtVpJkvUfiSVZeMixrzDOfONs4RkZ8leDiFjm5BMhkrVBqTCnK7woU8eFpqeaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX0VX_l2xBS7Ga3-xtXJNiPqEYuNXnql2ei424chZ4DieOPbAm6o3UGUyqf4LD9veatpj_Y46UOhDYDFxmWGAA151RB2WBV_js7zS4TY8JkIovA9xdLNNf-l3lYJLTmLlCVNikGAWCr_EJdkHiywXTvDhGECFsOkNPy1BjpXfwj0It8fTJ6lmOBu-1tCzPH5loTL-2mzgAEjkKfvuEX4TPvdYYm9ZOVYDXtTEDDjxrO_1QyhbYLGLC9uiLeoOSTU_YIulhcJKMxjV9rF2BlRFmkTD8eUwsu0CJl0QJ9JBZaqXQ58xTzC74D9VFuOtjKHoeJ4eqiYcHMbpr9b42a59g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1X3U19kReBlAp-TafqPOl4jlX5kiXdZQaOUztaz3I2eV-85HaT8GpDpY81GgLPhCSGa4qNTZWMiiNaa9Pr2PvoDULW528983ej3RNKKMKGD-4jsT4wIeXlEweoiE-TFIXy0KwY7V-AjUd_38zPwgL7uc58cHG6qw5jqugWLbEd11gWTMQtKcMUCpzpeovXkCz-GMF3FOIVRrBY9Tk-L97c8LAqksEPMz1LbgqNbGhf99LU__hKvxYXZaQY8XyXThrj9dbyGU49bDVkzthkcniV7t3OcrwAOvSIRJTHN06Waep28uNalQCuNlxJLf7nPW1afv6a_Mr2mlqQpqPzYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=byGZMyikrpnKrCLeOGwpenABawrvPJ4bjvi3eI2Z0yng5aIp7AanJ7U5fgIrjlAWjVVKram6poof-BYBc0S8RUcbXXgz2Ze_fVXclOWJmxAutRwwKWkCuJM-548bKpZPsG7kLm4mnnnfWBc4HYtg71zrBvgnD6RoFEJ9xgHpZJn6mfb8MuJqtAmBd6WVqMpHJV174sUHm8DLZSCD5MxuDEhbmzqhsOrt9twM7r-QL87Px-vsNzOu_SPe8-xnxYLsI3kP-0a2oprFjhI-5Nm4NsSAQP3bMWhCWmoRdAA2dHGVqhwd-rkA366ko9ApI-uwFiA-CUH8skIM5KueSND6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=byGZMyikrpnKrCLeOGwpenABawrvPJ4bjvi3eI2Z0yng5aIp7AanJ7U5fgIrjlAWjVVKram6poof-BYBc0S8RUcbXXgz2Ze_fVXclOWJmxAutRwwKWkCuJM-548bKpZPsG7kLm4mnnnfWBc4HYtg71zrBvgnD6RoFEJ9xgHpZJn6mfb8MuJqtAmBd6WVqMpHJV174sUHm8DLZSCD5MxuDEhbmzqhsOrt9twM7r-QL87Px-vsNzOu_SPe8-xnxYLsI3kP-0a2oprFjhI-5Nm4NsSAQP3bMWhCWmoRdAA2dHGVqhwd-rkA366ko9ApI-uwFiA-CUH8skIM5KueSND6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=JDXxQb82adyfLZrR-kwhryyg2Unii96HGaTT_dDh1PqRnU1_hglVFuwNkdPQiG9qEpJuiKVj7QH9qYg-TlGAe79cM9TvtwJRGBkTnKxEdQBvAmb3Q6zk3310TPtDhSO6S2s_83lmsPzBZo8nsa3nHeGgMLGk1aEKVsaguIwobChpZB4wV3k0MZtCxy1A6s7aynVRCaHRmNhUofLoDQ4WebwAMpqD6hgOp6JntJ4TtwBvlhskgbc6uRuBjAFdPFONVt3cM0Wf905qLxBtl_T9jtrnvsrtqKMY1d0_qdEtfJztSZpwkD7nz1N6n2ndbtPGzB4IpnPHOT88T9Ki68i3pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=JDXxQb82adyfLZrR-kwhryyg2Unii96HGaTT_dDh1PqRnU1_hglVFuwNkdPQiG9qEpJuiKVj7QH9qYg-TlGAe79cM9TvtwJRGBkTnKxEdQBvAmb3Q6zk3310TPtDhSO6S2s_83lmsPzBZo8nsa3nHeGgMLGk1aEKVsaguIwobChpZB4wV3k0MZtCxy1A6s7aynVRCaHRmNhUofLoDQ4WebwAMpqD6hgOp6JntJ4TtwBvlhskgbc6uRuBjAFdPFONVt3cM0Wf905qLxBtl_T9jtrnvsrtqKMY1d0_qdEtfJztSZpwkD7nz1N6n2ndbtPGzB4IpnPHOT88T9Ki68i3pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaLyyvpHcEuhBN-GlLEYafx3mTz6LQUNEYhAsXlfIixKQOaSVuajwOP_UyPsVXPIUerQ_ppipMq6Vtk6sO7DCIrLsalWRJlxtNdQMFkpS-lMupm91d8Ux8ZJI7S3LWhpkRnb3GJyKpDFwWymRWVB8J_Ag61NRW-n6rYOqyi_7tIHC2MrDlsCG-RouSTPkmRdyJxz8oEelb9B2APTyTzdWa2wLl32Q4xup9x_VWSz06a5tkfkGvbmE3OWxUUBk-l0k5iWqWeEE9Q_lpMyeDWB9_eQbwAYBSlDSuFnZ-OhcJOKml0ujRqn9GujAIaHeD3CezEU5r1oJd1UlwYbeS0IhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_pqK7h8Tbya7wJ0iNhW1ar0niyDUYjIuTJYrNRdGaeT2Oh0QG23F5F5OtcuWaBA5weJYnXZe3x3u11qmC3xIH9zRTWWi6e9pr7JLJO0CvDbiWH5w2gT_n78bO-uQ_cAOQ0jYc--Qrd5TIo5c1hpoTi8OCi8-BHnvglMVSaKti1ZX6m2RJZIrTuBFRZJf7ssgQzfXZyCaPSGeew45prvbeF1gz94yp-CO-R2tgZ8kUX-qFoNXSSzRAsbcfB1eHrwxuKyw-WzAL8Znjt5AC3tiNRQzrin-qKNhHazETkf8v5zpYQ2_TqPEu7PUZqbZS6XBIDST-e9jhJeBW4KcpwgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGUMNOHMAzQ3INbO1_3y02ZRGMkTHxPV4Xx3giAJF4U-Z0F4P_AYgnVqzmxc4nn0G62N0ZsA7_HrY_BfDRt718qkt5IyY8I82DCGf9WcqcqJxcIPF9-MfVbQR52Bpnd-965DsE66rIcK0Tze3Z2--qiWJh8rOXhnHKHNrgf1kg-m8RpJT85FEIbFqTZtI6KZy7uB6Amifv2FERQO0MLOLL1C4_ZDZP63ztrBBZ_SFF77fYtD9univEbU698YIXkhxathgd6X4SVDATBake4Od7EDtMLvRLELCTKmfMELir2SrYHeJtx1TvTUr6TEshIZB_-RAAapBcUnejNjmkZYJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ek9wTxk2IkfLOMr1laeCq4KweOvr3X7UsiLaV44qFGkb__QzYExn7osIeXA-lXHMKnf_3xG8jZ2iIrUUSkUom2eYe-_DI8t9ngR0d7jdGd7t4NhSOdhewKyEDvla1WKgpX45k0JUPM4IBanMhgTZGHae1cszK8hCE67WA4iH7ngaog4j1Xf4tGKIuQ-bHCsyjxtKddg80MK5BwVwbVpU5QpvEzbiETbZq3llqI5MXnpchPBWCXh0RYTApRsRXzg46Syh1mi4Ktej2gbAQuiBUzjqxVnuStDfwxD2I2xo0pLXjXiNZAunEls69FMv_bZu4KWRm2PvYFNNr83Lp7D1CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ek9wTxk2IkfLOMr1laeCq4KweOvr3X7UsiLaV44qFGkb__QzYExn7osIeXA-lXHMKnf_3xG8jZ2iIrUUSkUom2eYe-_DI8t9ngR0d7jdGd7t4NhSOdhewKyEDvla1WKgpX45k0JUPM4IBanMhgTZGHae1cszK8hCE67WA4iH7ngaog4j1Xf4tGKIuQ-bHCsyjxtKddg80MK5BwVwbVpU5QpvEzbiETbZq3llqI5MXnpchPBWCXh0RYTApRsRXzg46Syh1mi4Ktej2gbAQuiBUzjqxVnuStDfwxD2I2xo0pLXjXiNZAunEls69FMv_bZu4KWRm2PvYFNNr83Lp7D1CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMIEjrnieXS6SoTpl-Hf4pQ2i4M8YW26oWwOXJCagx7PGUpyWEAA8MxoAf9slORIT1kzcUY04tyySk9YRFw8mdbjuPpHyEosj07hEUclIOPn9E0zAI9C96vFZENlgOpK1czuuKqlIDRxjouMtwT3OH193kBh_71exLDh_FQEKTjJJgB57GgFJ7fWWs5x6uTzaeYQw-nbSvkieoVy6AmwVZeJq6NF9EvfLUl1gpFw2Ku6KsIoL8AkQQoWBAAyYaREIRhigujEVM09rH1qYRs6LvjguoaWKlhinJgymfZXG96MMCyAXWNpjwIxDG093dEXvJsaZGvOB_82MuV8mmYnPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxpwKi9BDsnE1wU-QWbhwIal2fPrT36K9lE2ROGLglubP7ViV1I4-vPEcUwwLvfXrkgia8_9bnD7fXHFenjZMraAH-PFfzTayOguzRd0xciez6GqjR9Ll4gjhQqeACwxtti8nOq22-NF1CMalfH5fZyTpXbSrK7IA1OPD_768VIKjwWmop0P1rRWIRaRbuSKgLlWTLAnORav2NN4DeLbKHL5zBQil5vQbillhyaISi4bEuzU-u5YcaGUjAQJ7IdXU4NzgYe1Do1PFNh91da3tDPp0D-xVMYT6enkB4GLc_f7pVfQldN02BLmbT2qHNHSMNDmMK-RRFxEuU_jK-nJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7BcNIZgnGXZYDsab2dOVCAvzmSex1yDyU0njxuz4EE-2JrtS2Tk5LsrdsY7PmjxcHg3NHuSaKLZqEXtkG1o7G3jgTEulc3_-nBDde6NLcMFKn-t6j8Le9BSy_cS_Y4hbGFJjwGz-ckEFcN_BX4YQOCVLa8brmZcUBV_4tizR4GbsKLtWXxSk8xlBR-uNQhlOvmbhFH9rE0VFrSBxZZ0auL8-RnvDVVdcL92r3afLlFm2Yu4AphhsyTfDiuw0l65f3BN0BowpaDruwAyJCW6ErtfhTeHlvmxzjeBYa8LEQoFmsbr2fY6SbGOsYARpuKYi68dyqheTobivGnzb2YxPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nf5UoNjbSOronboxFIS0pt0zI39lY2qjL6hpc9w73S_Iwd2Ce8wECt1_F3Gf5PWo_j2YrQYesb9LJ_gMKr7opRUkc59AOoAqZm_TS9ZqpyHypdEXEVlLHKDNlvJuBQKpLh0nChLZl3kmUXlq1R71BKl7mfaXLdA5URNtEAN02DMkzOtqFQXG7bkz4ZMcHifqnkTxmt0PGTutqpViJMPb-pueQIohQq_hVw77_UJyY5U8FcIBDaElchb4RlC29BAfDeeB_SMSz1orJFChKsxU37v6fJDBx8DQmdAniQDIQdG3mYJumFBWwJEoqVFJhRauAAB3gp8GSoIbzvSEXQSTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=VEmdx0BnBFsL1MzXVf8qOWf2f83ouLLtjksR0Iywte_Zklkk104xHalrQtgiBDSL7HIxcWXlTpCMZ8J3t3pQk5p9AcXgltE0-sQIQ3EI_obWayl8oaxA7wfulCfpOQT3r-PW_Zoqa-92elSDOF-vBoe-yWAQf8SbpP92wMV6DiE7YYZv_V9BFxIpWaOvS-wUILU1Ng6flaVyb7CGeV_cJrYgP--d7-MSiAsiakcf2x-34k2t2BiSdlFazuV4Yz1sid2l2uPXNpTQwF50tVi5jiBQ1XUDtyiP1h-gCxsMDwNGUEteldFS160xVYaWKNg3UgnAIKGsEey3lYk8fuztUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=VEmdx0BnBFsL1MzXVf8qOWf2f83ouLLtjksR0Iywte_Zklkk104xHalrQtgiBDSL7HIxcWXlTpCMZ8J3t3pQk5p9AcXgltE0-sQIQ3EI_obWayl8oaxA7wfulCfpOQT3r-PW_Zoqa-92elSDOF-vBoe-yWAQf8SbpP92wMV6DiE7YYZv_V9BFxIpWaOvS-wUILU1Ng6flaVyb7CGeV_cJrYgP--d7-MSiAsiakcf2x-34k2t2BiSdlFazuV4Yz1sid2l2uPXNpTQwF50tVi5jiBQ1XUDtyiP1h-gCxsMDwNGUEteldFS160xVYaWKNg3UgnAIKGsEey3lYk8fuztUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcystKEdNEG_eenjYxzQi9yvN_PEIX0iZuLjdhbKhMVAe33HbnCkhsPdilGWU7gjNBwbSHGpj3CjflXW_Jcw3K3XcU_dVqQzKq1y7kH9r7vuK2CD7gJm0ZK1HfL9p4zcDHpSl4l1BhiizvHi5GPWfD5_oC2ghODojCbx92fehz9fyoZf5l2c2iot1pv_68bsSELj8aCUspovA5IDbtp05HRzYIqUoz5jGg_ZTv_I9nKVI9YWlzajW0YotRWzxH6V4QE2jW5pQnVEB-4wFrjxEDC-jUa1AnXOsCX1Fd8GHpNFhA8XTPqqaeM-EJJ0ceNntWIVp_ax7ARP1KvcjT9F3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr5CxpZA5-Lgh5gp1GQisLMAtPnWJ8xC0GzV87MXn849xrC5QEDwnpMX8tEeQAkpreKovjY0T5VuFDFYb0a2YEDbfHNmCzRKr1vjJlqVK3ky_hXdAKpJSZgNopjp4TD3HPHvIeB4WS61UGCupIY-FnK8zYzbku7p2QKGQOQF-2tnf_nJRZUD8Vn-MqMdplH5mnWFpdHWCYiKVDERc_kLkS6bP-cyuxww6L-bVPkHQzStsspscMR5LVUfbvtL-ZxYF93MUvKbROR9ibs2EZVAXB5MVxF3rIBS7L9rTdMY8Un57PeSmvsSf2yO_hg_zeKYNB0RPION2BEIDVd6qwTZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cphtK41AZO8YCQUiWHfTQy4m6IWVswwnC3So4ruBX2FUB5sl_Mdke8xbgOluavwxo1cbl_usk-zZ40W-_8ge_qIFeINyYgCVFtKcyTh2MyyOUmTRY2ybt-i5s8ZzC4AngvsPD2Bt3-gzk-5iUnHoHONmBn-IrXu3KEHiy0mDdhDfn5eP9-wEbgALBNzb4qf-E3m0nqTSJNTWNkUbZz-IJ-1EklaFaaMXaIrVrb1bu9tOd76lBNw3kOoSQNEc3RqHiHcsvpeQFioADFzXRNQ9DNXmxwQilt1hYzC9DpzBFaq3tvCFLjoOfry0qQJIpw5PPiwlrjAEo0P5BcQEb6cxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=j0GED9Nb1HwHpGHlG8fAfllO93SjETEq_VB5VRnpL1mD3rI1FG5E1nFpg_lVLUBuXaqa5yFS-viyMSvQAOdq5MEo5eKVghB2Qw8DSNAbIQdZW3vVUKr_VoLwOicC7Ss5dRNRtAUpBZTfq9Ghrycw9FI8-y45k7A5iKqfGz4VD5WhnhNOLgrCDU2LVkGM-XEjGmbLZrhW-F7nhyMq2wRhX2iv4xXPefnHdllOwFt4PH54HDTZ7QdlfxqpmJAeK_kXVorBsMoD3I9-rZmRKRnNt3WmVECzQmdgyi1uYcZJYHMZsQTlbCk9ZsmoTHxM82G6RYiGmKOP8QMdvCnRy9Vb9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=j0GED9Nb1HwHpGHlG8fAfllO93SjETEq_VB5VRnpL1mD3rI1FG5E1nFpg_lVLUBuXaqa5yFS-viyMSvQAOdq5MEo5eKVghB2Qw8DSNAbIQdZW3vVUKr_VoLwOicC7Ss5dRNRtAUpBZTfq9Ghrycw9FI8-y45k7A5iKqfGz4VD5WhnhNOLgrCDU2LVkGM-XEjGmbLZrhW-F7nhyMq2wRhX2iv4xXPefnHdllOwFt4PH54HDTZ7QdlfxqpmJAeK_kXVorBsMoD3I9-rZmRKRnNt3WmVECzQmdgyi1uYcZJYHMZsQTlbCk9ZsmoTHxM82G6RYiGmKOP8QMdvCnRy9Vb9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=c6Pl47SkjKQTmGzg-rTm3MtgX4vA-fOC0vu2YxQP2b8PE1SQwZuHfNa5p4DR6iWMDkMWRXfpkrK6VP3W5RlnmGb_ck3D3boVrifgwttkIyLen59ukG8l4MAcH1HTTFsAnahloZUNKsjQqGOmkvZl1LnqvlfvnEcx2rt5KPQ9Eezr1ZZVKL57AjD0WgFk9x2QoTHaLwaMGMxiHlNz5sO_g93GUfe9x4U_y_xpnZWQPajtQq8vKYoXr0iaoz5hv0DezldIbqBT4ilwAN-gCB1CL7mzRwZKYOfQYlaCC8dvuyubvVeTosX1gmorgMV4QDKsA4_9BbWWB91S65pZwqlMvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=c6Pl47SkjKQTmGzg-rTm3MtgX4vA-fOC0vu2YxQP2b8PE1SQwZuHfNa5p4DR6iWMDkMWRXfpkrK6VP3W5RlnmGb_ck3D3boVrifgwttkIyLen59ukG8l4MAcH1HTTFsAnahloZUNKsjQqGOmkvZl1LnqvlfvnEcx2rt5KPQ9Eezr1ZZVKL57AjD0WgFk9x2QoTHaLwaMGMxiHlNz5sO_g93GUfe9x4U_y_xpnZWQPajtQq8vKYoXr0iaoz5hv0DezldIbqBT4ilwAN-gCB1CL7mzRwZKYOfQYlaCC8dvuyubvVeTosX1gmorgMV4QDKsA4_9BbWWB91S65pZwqlMvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=fKve05f1S0TxN1ZyY5hpZB1cN_Ls7CvLs1_jrltoMAfGF1mA1Il2ImMqlgG2jXG48Ybu24EvBTeW6PRhpcwqrpK5cRamj8rpMQi13WKFzZoobQ3uQCMFbA0lRcrihcLzKh0Out8xBrTzkPOznxEVcSt-dJVmD5VD9tQKimGmTk2XT8SxDaefQU-_cfqcQtNwRhny0kE6a_T4ldhQ4gaE1OLl13I1kOeIksGB2R9DlTZ1SnRYPQz5SNRCZSzWtBmcS_OJKjjKzuB0_nP8uqObQhKf6qqvHN5RZb6y5bt2fxNTcEMJoFlkeefkBwV_8PKKS2mRslLC1jUxLuXqCS_9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=fKve05f1S0TxN1ZyY5hpZB1cN_Ls7CvLs1_jrltoMAfGF1mA1Il2ImMqlgG2jXG48Ybu24EvBTeW6PRhpcwqrpK5cRamj8rpMQi13WKFzZoobQ3uQCMFbA0lRcrihcLzKh0Out8xBrTzkPOznxEVcSt-dJVmD5VD9tQKimGmTk2XT8SxDaefQU-_cfqcQtNwRhny0kE6a_T4ldhQ4gaE1OLl13I1kOeIksGB2R9DlTZ1SnRYPQz5SNRCZSzWtBmcS_OJKjjKzuB0_nP8uqObQhKf6qqvHN5RZb6y5bt2fxNTcEMJoFlkeefkBwV_8PKKS2mRslLC1jUxLuXqCS_9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hteMRwBnWO6zzFf2Ye5w3_G_dmDWya_UjeStcMTcw5Hr9XM0WsEpKPbHHW8E9k2e4Xr9_PEqfNhRgJmYDyV0NVvXhrYr7VodYd8wjn1QD8r9VYNRqC_gqaFIjq901dHKwJUOyYzMo_tTXYTnc_KRJVzJS5HxgDDy8z8poahuTccR1VRnz55Ze42dMEWop_a1UuGm9mEuxOg6FSH7uxnRXvx3MsEaOD88GTUkAaySyPdLZbBe97u3XMPyvq68QKuF8zv8k2s9CD5MKYhlz56Q2qnMajwJAA9Of6LSuCplW-PFLkSR-yoOk9oCzB4tJ6sjayUBtqLBUuF3X6YT23_Nvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHG1u04o7S-_oITq7gdzPAoh95klbREXEaMT4z6_ixuxwSIWj5JYueBFhEJuQMbB6GgzjjZ3oStdoBZUUus7nUTrJx927svXI9spbImU_WiSZ28mMjGEXRFjZOL63neobnTUrEitL6zUFzBzJWXwYEt4oYv4VP0kTbwRyYoBxi3mo7aZMxQ4tIU74Ot8yJvOrhW7KrgNCEb-pkNapGQe6PBMDkY3VD1RbYGSDsDZxC0K5MpMw169Ob-aBsrCvR_ifz8gQ-csDOE5aSWT9Xw1qV6lBXO4144IGcalSiQ1_vh-idPttjll2tK_6ZyZmcqHLuZJrBQjoqqa1MW77_bDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0qiAFmDcL1vKD1fyTNMZ0w6cmGCq5D92ELlWNmOKcnsqXGIkzP8rnx_aLRDm5PJmW-8AtntlZLDP6ptkOZF6FeMOaTGgZyoxUR2h1XPIYW03QB5V7osrkmMh567SI0b9Avs1TmnyO-ylvlaH-QR81xjBMuVuT6JJ6c1mOt2o0KCTO7mJxHzhY1a-q2NcdcFi0G4gibPTypvNltWLAGtBRrqPn0vG5wcwv4dK2sKF560hVoc4cNioE7G11KUcvHAqvF_z4IENb54ZTf0JvxkjbhTWwUZ21bFI6Fac5JdZDIYXbVnuvb7vYC14ivvX_TOIZczuYBTW3OdGNK0zjMpzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1J0K0VcgxtvTcQ9kR3iReX9ElA7t4_uxBW0wLYzFlYJzGY790y_QOFCQvygg8sOnpwYcEsnYBXiRTqtUgW9-1WbUkT-nbSnkbt0pSLHpHrRIVu7b9J9Gx_lCsLBawmHGAiGzk_VExd_dP3QzA0mHQl7ajCJmYVkbLxZ9Pi-CNjK2tw7B85LQhx1x96wdvX4Y5xlpgLBpd2jl3MfxJ2uQEkWlhA5hqGiVeyfAa7YBhfgM28Gunwjf1JZo7qM8zfLK5x-CezeCU9_5cxqV1vAp7UPjNX9mMbguG2zwpHb4Tfk2oZeME5C0ljqP8Zv2v47yGpXkBKLF_3FpPc9hTfcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaPlThZuFEZZ5EklaqnpuMDXEf8ACNfb_nmfqlUV-QAyhllKu9-yW_8XNRIBiYlEvrn0WdWN-LsLfNNOsBYX08Ay66_XMwoGcPecToXHQF8xzKksghBWIYYeEcRxKnF0PeBo-0NSHagRBUnjbpo2cd3MhiMx0cbyZg34ymo3lYqqtmk2wM1AzeDQNNkbi-3s6L0yLWxaZcgIEoaAXfOrM1ZbpoGkpbtgPgBbbClFTVtuMx1pxDA3TiSTb5qJ_zqC7YHMYRveFLwQJczvS6XUAJMOeNW1btaDMarBrIocK1oR4OSu0mNhbWlNuezUVLOblZoE46B80WvtAUlljAhb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwkeMQO-LZQw5ELZ58veQTovG-w0PX8baGrOUtWCv2LiCQbsKCQetCyiTO7NuLDFlebtWsOvTLlMRIoJVIV6rBFQR6a7X5f6uVndjjzbIAdus396tHYOiGtLrF8nQyCO07x59f9XaRjHNZbxwpu70vfGS4CeL1DkRb6bXzdRm4n2N4kzQZ4u3P-JA5g4BDrDea7iweeQ9IRpKQSaU_TWcuJXVVBdoK2vFQ-L2U3rRBtrDGYm1UWWAmilcXQxJy1aQxfqP90az1-nCV31-P6uiDHLNW0uPVSvo-NGrg6pYsWnGlIVvH2jLIF8NwOlHTN0I17ewMA28qgIISdBSXfWTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBJqGrHp9_wnkExZ6jXaua6JUv4CZzUYCDxCyfe9865ass-29rl7wW-Fld3fp6E2GP4V31DBnlATgFFMWrnMAMxucrYGabN3bH5klHNDpdTevbIdAWftTNPDcrOesV_Q8zAb5BEwvLyU8gHUWUUDIrm2nRgm5m6WdBKr_-IVsOR9lpuq6HJRDNmDRUXfNoydbHcqG1pQS8OuEJ9k3XEDFkSpVPwGGM2mblaJoH1sWOBfxBS1kkgTIXONZkDn68El6CaZQnpDAskfPKyDUTahy49GJR762Ib9a7-eb00swE269GfQsZmf0PBcjleP7N3QAJejL49kqFEd4v_4ytBShg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eClYg6Xmd7D4v0hkZiwzHFrh1LHoFGzPMIFw5eQYEsXV962Wg2l1MEbLHMFUcdFUIUxGl30lZZKYLUW6ia9tZSgba1A7utS274n_oI0P1PpbhR6fomBTSrJ73bbBi41koGvA6qYAzJjRsO1yGi2nWcUQYH_Mxc3UwzZY3PDeZtNJcb441b7ag5-9LifZgBh9fQWt0JNhopLNusfC1jNxbtEhDWZIZ9bOqIzvi3iLoMuKMqXVQror8zmEQ9m9IP-0lxtGxVkbzqfDDem2o1FmPUT7vnFowt4b3-9H51G7iCRPklIXPOlDNvgh-t-zYO7lxfiQUv4mJEMbnSFKFOR4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2LZ-Vbko7iuqcE9RRZdS5SwhGNHaQuydFl_-awVKnmrS4fokYZoo4Vv9abhkQngGT89VeUOhE5ADs9niohBeqffuvYgAFxqTrPr_rFdcpq4N9xDp5Mby-TZoQ6M-o-qJO1oqkOYVRHbU-zQAPcpeSnhmACJuVu0Yg2l3BrfcAJjMFYX4gwpYzltT1RrM8fz4y-L3HFh83KG04KeRhzyYpm5wG-9gb3_etADmkL6yoqVomCASdcr-rG0PDkHg3XXhzgxMhNTwBP3I7v4GXnWtrFmGhRX-Pq8770FxevfeI1oUpttKX2aVVYzjM_9I6WWUlCtbkWMFuisHwzQwbQIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9QJtuQxtL8lE1xoE7LqkZNcsd25zOacVGPUYbxlWlazzHkpBOInqvU5xQTvkbdBqP3St0bpT-t7_LgAI-JbgABXGglDJK4JI4HIgfsnZ5na20FN75jF1NNZQrjB_esWdIMMXcSgA6DqwV3CE_jIXsHEUL7Lmj_n02iUKiVz5z71UvnsJ_Fu_oeAQ70UjACfNTZgUE2BPcZLqJ5gKmEahaaboST3lXIGnbt4s9eTL5WC9fc0RGsv015KEkSF-0tZYjfCBRSYeBEyV07G2BIavLnND7nbojTq1bDyueAx_DNH7mTq0cfx57F_p5L0aL7GiyCy72r8-yM02rkdE5ZWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCN-bmUEENrKrosi6Yv9YMcICDqyOVcpWCCeU6O1Vx--OOetNbvTjF0ZnAq2ZDxeAYS71MolKU1WDF37VzHv7p_k3ZeQQCwJiA75AIUu1Ad_qWzTZH1dIMUNqbAwWFG5TZ12hTuAMwEXySeoMG-fsWYwFHJB61KexZ2UU03vkwWledjwZsohpi5aVYexxk4d0g3vDZCAKFlkRSH_ERLDSaJqCj5LFdfJhhaElHCGB9zsLXo22WEhzdd3v-hz3_0scP0PwTwdtwhFUA-hLd3cOEw9Y0rHGQHqRT4DbT5-1lB1jPZEEPhW3e1D3MNWFyFscXglhS9VajSa43HlZfV4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLP9u-ucS4WiPNq_1eBj3wzsAjGBHLVH5ILE5x8VLLch8ffQGuU-qL3xUN179fZGEIpBzTSvxtIwTmeBakV7RZHL8oHOf5gGE082vE-pKIeU7ivYsPUIQq01RmjZSAjXBVuUnaAPAH1qL7KKPTzKHNpHNSu_nj4Lk9Yj5goV1_rroUgfrHPB-U-2wzt-O8phGyAqDezChhH8BH3x89ENtx9eK_AEnpeC4RM6T0xqEgVNcp0vPiuSaAtl7C-l1RXM45Osf3UVxGtInWOh_MWHZk2j5OZ0n7oxGerqiYH2cNTgJ2NP-VMuL68D6DtWnSPz1MV2-v92wK2yPNkVWJZdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_H1o69JpLJmcJkmwv2BVaPT9LA2YAaMSvUtcbB03j20XAnE7hfB7P_C9FEFWSDfp1FUamtC1YcPxFDcZWCdvxs0QcxTJvCCttiTpyoceWZEI3yfgeU8C5sSp9jTwDoyK4Ayxtd0NZJS5xqB1ZZyhJy5VBgCvePbkIxhAK4CvstbTGkR2pGR4zGAx4a4arY5glYCjMRXZp6K7fDoXs1j9st99WpABr61-ZVMjnJyBIo-iBugnEBAuLsDV6e0XuGq01H0hL_P8Fz3L-2n_D9SGXVox2smw6dA00rLwhI-ZcfCGwDA8sjDiyH8sFWPQvmOz0otoSKmjkv7ReNK77X0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6IeLBj0GtOOTDWt58iN42ck8PhkQ-jnNz0Zg5_cT8iBZptoDm0y_zS7eqLQ1wdujGpeaAhGstBscrk8Gt_5IfzJ2Q7ITLRYJqj5Gh0dYhGOLxNdyFBUWHZyFuq_X4ncF2okzbWWNhsrwbNupJUL_steUb996lZ9o7iAvs031KCMXHFEwPXmC08q_TudG_CdmQt1cca5Gxc9g3kHG3epebKRFdrm1-ueEj9O5LFi46fehT4uyc0mqYBCYq72B1vT3v6AQYoeYO-hi0s0b82xZu4fIbwrU5ZRwEFpMMLCFK1drr-f7I4hX18xMwM-ZhOpXjzDjk7e-V_7_B_DEzcIXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr87wCpn0v36GA4oTjVvLgymWZyE3ZmK7TAfAup2tq8nXOZg_qf3i09WfoCvTpzr-k2AzjV7XCn0ictXx8EFcLUsPkzXR7HGvncofzTx_uiocyaOXZrinIB0Dg6xIRXvI5otVxcGV2KX96k_wfpMDzVrnxHMivPJe_FwbY1VIiIrgS45_UHrjxrPlbX8FZunUSbiGVqATio9tze7CS5XH5al40JGXpF6zzd8_NJtleZlBN91Zqv2CmDVRN96qwEcSxAZ145-dHaONpwvQTe_HBqbrAKBj4Pzx93Sl9dGs6FXN4zQpop3VzWUySgS4ofiz3EVKXS_SJgxHqat3v6gJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=SwJRK5r4ZyBldenhnv4MlkQnLAK4Ff9BnEmccGT2keeZRiAdIrGgnGhKCiu4dts-Qe0wjKvZWzeULw7ZplQ2-4eySlXfIG_1g_KcFQdyVxUsj35TSCmKqpflVtEgZDGxiz7BdDs9ERCr-u4Xvfo4igLn_vOP8GHK6lTQ5p-WsAmPBNbuf5W_7RT1Xajug9OY2hk0Li7wEZJSwET4Tu7cSZzkdvpOYTDnGsr0kJzB-vB5YtyQ8KlxGuqZi6zxTq8txR6z2utUDYPZSUL9nCqTspj0M9XIjzn-qkn3HTGyJlWLykN3c0KtBFGPg9qWJZLs_1F33vhXHJQqec0ujMysDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=SwJRK5r4ZyBldenhnv4MlkQnLAK4Ff9BnEmccGT2keeZRiAdIrGgnGhKCiu4dts-Qe0wjKvZWzeULw7ZplQ2-4eySlXfIG_1g_KcFQdyVxUsj35TSCmKqpflVtEgZDGxiz7BdDs9ERCr-u4Xvfo4igLn_vOP8GHK6lTQ5p-WsAmPBNbuf5W_7RT1Xajug9OY2hk0Li7wEZJSwET4Tu7cSZzkdvpOYTDnGsr0kJzB-vB5YtyQ8KlxGuqZi6zxTq8txR6z2utUDYPZSUL9nCqTspj0M9XIjzn-qkn3HTGyJlWLykN3c0KtBFGPg9qWJZLs_1F33vhXHJQqec0ujMysDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2x2fwhcNZg7-dLeBzIbR4laF95PtuE3T_8jy5JOgWtt4p9-fG8PsWJ8-f5U_RqYMWw7j940UWQnf2vnetvRrGIBUbyZyUE5wIg4zgrGPcOGlMiqH1nCmfJgC3q1NUpEcXd1gDUVS97RaxlNGAVX4arUJZRVFI9g7hMCbHegpUz8F-4_O0HqqAlCjrivqq-PYYVTtjC9y-lbOW8NVxuolVUP1QNpXRCOnOLS5EhY6iyhEyAUpbl8ampDCh_KJT42ge8M0hsDq4akmCus1WrvQ-rX5XM02DVuWQo1-4wFV9DmUjNzcnvQPdVDLJZTGCMk3iY7fRtdLrJNB0kkklcbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=QnELZC365XzO_D1aIoz25vV_r0pDDKvHawU8ax9z33aCi-TpsrHW7guyunpgUmjJwXf9MgJAaa12cY9OprSCrxuPooFEhirUEJyiLU0w2msNGCGKaiJqv4J3GMKjX3Mhs2TtgcFx_-jvGnp6sfphlTwzeBVRgtoQ2eZrCdN0PHXLdL0Kr_JGyS7SIiF1utbJ0Oo2DksK2aX6ywOch_ZNasHAww_HBYDiSjp9eWuJjUHmYb1ypSkxOMNRnIiB4rPYPon6PxOSwlvzDR5CYZUKebooFdQaeI9vndyH63D9v4_wdr-1QnYThdBAR-V-t8qEZo6Rp-yMoCw9QCBmUXPOTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=QnELZC365XzO_D1aIoz25vV_r0pDDKvHawU8ax9z33aCi-TpsrHW7guyunpgUmjJwXf9MgJAaa12cY9OprSCrxuPooFEhirUEJyiLU0w2msNGCGKaiJqv4J3GMKjX3Mhs2TtgcFx_-jvGnp6sfphlTwzeBVRgtoQ2eZrCdN0PHXLdL0Kr_JGyS7SIiF1utbJ0Oo2DksK2aX6ywOch_ZNasHAww_HBYDiSjp9eWuJjUHmYb1ypSkxOMNRnIiB4rPYPon6PxOSwlvzDR5CYZUKebooFdQaeI9vndyH63D9v4_wdr-1QnYThdBAR-V-t8qEZo6Rp-yMoCw9QCBmUXPOTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=WPhvrOOq4NvpMbMAIkMlZN3tFSiUNfg3DbZBngQsEcDH-juMkKS240tykvnCotbgJ2IpFFwugy6DhjcUb4bmlqNWGG7a_UZWegOe5O5RLK4bpD8NTQwrPKVaGkWD5H73dQ0g7jA37SjjaZOm-MfE86c-z4A15LKVrYfIDrpcOd0dKjVviyH30ifQge5Dj5MZFEIjJBGONIoA2n1LEO2xWoLSKbfYA7Ca41NnI98_p6W_sJNfFgn-wGJyupBkHJVLO4HexDrZBqVG_EGT1i-8JFydwWwZidGhkF9NF52cVaw-Ur7EdRuQ7vOAn6f1A1i9o_YLlitGQlnuM-g7oLOTfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=WPhvrOOq4NvpMbMAIkMlZN3tFSiUNfg3DbZBngQsEcDH-juMkKS240tykvnCotbgJ2IpFFwugy6DhjcUb4bmlqNWGG7a_UZWegOe5O5RLK4bpD8NTQwrPKVaGkWD5H73dQ0g7jA37SjjaZOm-MfE86c-z4A15LKVrYfIDrpcOd0dKjVviyH30ifQge5Dj5MZFEIjJBGONIoA2n1LEO2xWoLSKbfYA7Ca41NnI98_p6W_sJNfFgn-wGJyupBkHJVLO4HexDrZBqVG_EGT1i-8JFydwWwZidGhkF9NF52cVaw-Ur7EdRuQ7vOAn6f1A1i9o_YLlitGQlnuM-g7oLOTfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBA0pwSVa255Wklscx_pND6oWINnWdtk_HylQ63CBZxeNW2YE8kwQX4-9HbyCmGre0x5Uj4nd-94zfEvbTfy7naqwRs3hgJC0SI6rs7N6ksnV7p6wzzW8e_7FnwPkpl8xYCC2ux3fWiRRKlyiRTf1lQh5X69nQuTbMfc52zSzStoeLUvprak0pbCO5zTZQnHsDpnfMEqqwGXvnDlw9wzg-8-JCKXhjYesz9F7r3QhjWvregKqk2RrUPXAOrgjdTrtK9aGSTE9mSzwSgOMYsB7KtL_GiaZpV5qrpXy56bndnqowNVdxFif4qNo3swSIAc3B9h2UlHhni9Q4dSclDXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=CaPWOnTOpnPOu196BdY7tO9sb-uRKmVSeXHQuH0bP5IyolCx_RqBdOqPAWliKZ2iT5cA-TkvDSNOvNdZZyKHA2CJC1sPjSDDw-899UPMNhIXtDKopKLeuAI9ux6RWPtBVYrhN-pC28J-iNMiMh6xOSEyiAqF4BCofOj4du--wt36NMWbPne7nGfeS_sdjF3jTmhmQPsjv9qFIdBLlOPLvH7IO6zGPHeii8_QZxu5pu4zGT1-pBIfAciiTtOwjSumqv0Np81LOl2Xri9x6mIeDj5YKQnbuSpD3c4iic5inpxZ5QUzm8LGi7QsQa2NQwhI8W_JCzEpzcKhsatWsoHczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=CaPWOnTOpnPOu196BdY7tO9sb-uRKmVSeXHQuH0bP5IyolCx_RqBdOqPAWliKZ2iT5cA-TkvDSNOvNdZZyKHA2CJC1sPjSDDw-899UPMNhIXtDKopKLeuAI9ux6RWPtBVYrhN-pC28J-iNMiMh6xOSEyiAqF4BCofOj4du--wt36NMWbPne7nGfeS_sdjF3jTmhmQPsjv9qFIdBLlOPLvH7IO6zGPHeii8_QZxu5pu4zGT1-pBIfAciiTtOwjSumqv0Np81LOl2Xri9x6mIeDj5YKQnbuSpD3c4iic5inpxZ5QUzm8LGi7QsQa2NQwhI8W_JCzEpzcKhsatWsoHczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZY-WIsXSaGoGsVsKm5IRomTVbBqJYHfX-pkC5gFWZYLHH4hv-HkCYWGKvjKyDV_W3ctfU-kUe04oM4_JjITUOaBI-1FmVLDfUnywbGX_XUOoBFqEw6aBJFqVapq3uSUKX19P8lmEguk9-BIE-W72wWQ1HpYE8kpv384qkB19WOQPL0t8TLNbC3cDa2wqvfhYLJCEZn4BORpfpuF0SHUsF_QO1vyd7otHplw2ddNqkC5YZcoT71usIDXnNjMJJ2Dkd5XgbPBcQylWibIYAW5iBgKmaB3EK2jpNgHTkCKYFIDwVTv5UXtvXreq83bQWphPuecqIN6TucBDzltqedl-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEhtwxQ8zP6KEQrH1V01cyZFK3tg_7CpVtruroUUlCkWHFOWgqnE-eKb2cBfy5InCIhUX_C1zGSQVXSPqwYoLOTD4OAPUvHoqgGM98NTSGG-o1U6Sux-KjJXt-Um8mmL2XFzv3OUffE8BWwmncZJN2s-Dds2MF6o-vJDZ-07KJwOyqUOccy4Eo3RsxmFpTsmB2wu85fJTq8RZpDuwr9MTadk9UNIM3AI6tf4vzgFe7nhdzwVFsaJH0D2q8GgMGAaNEunGP0Elg4u9Z5j30DKk7xvFDdqmzRd4otua9cZoy990V1hMRvfc-5NjKR6uIeU8iyFpcMUiAhH7rODHTF_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2JleuWN1ylq6np6a7I79PY-DYH4Y2IPx42eOt_lJ-Xn5fYDpo5MZ43UJYHngCNkWdswmgxnOWlBewzIe5vUywQeel_xMwHhQSY37sjk6BrKFWyU0by7mfrMODwlfVuLnEyt15DhYOGJMPMogS7V50kwFqOTEOKD4GfIegUE-Z9rFxmCXSW4_kP88ZkzpcjJCyU0jwzfCkhxdorKyqteR2ltm6HoIS-cxNcyJYdxbWxtyIJtD9iJZF-TEUCCpZeO-_N4gwYbwSU8zleckEsnUD1hlHi0yEd7qLM2DXxOLz5Zeb8VwAD0OaRazMMKY7cq6K6_CJcCyQ6OzeAmFACakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwjYhUXKwhSdntsIWKaTV5YGN-EQq8HFPTvCQLxnk6CjkzXF8FWaPUnx1YoWrxzWKklNaaUAkT5ibNz2YJHfQg-tEcRnC-tOCZj1eV9ZOXKNyrP83MC_tJ6haxUazilGFClW4kaVQLr6_cJffTs5sA2orIPypOpQuV7jmr_x9bprBzUSvPafBIrXelDv-tKvJoZkaAeo2RdXpVuB2Td7EmFhCnpuZnq05l0yBKt5wRLln7R834WOseirjAKG3iE8NAZy6mfoWK-qI5FtYFRClGIMuIfKkvrEAdLaaGQjyJWKKP1ymc26aIrNREpJ21sDdhxKquNd706tS9UkjPNgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=Ji1MVwbNHx3Pczymagbyk0i3a-5kPcglYFLSpU1Bp8czIWSQfN2jckqoGqFufpKLxrje6YMAdnFhV_HfTZusSwZLsQm5mt3yEjR7NAOEmrAAOTbSSEm1Rg6nS6EnfbeNXTVe63U7-WhRAKcm0jhtoVQ_4fMEGg76sjXXDZ0e8phZxAImkJkCfh_1TpCS4yIst8H4WAIBhCUvFf8CBtveQJnWFQIb-pM2IOXpTf0ph-U8gzvtQmgvAqBVBhdBy33wXxZ0ZFevvt8WcJtER-UsnM3a3JqNueldyHACTA9RaUQ-fZR_WJ_XLQjuQ_lU4QeQlnVxfUUSj8FudWrz_7OEdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=Ji1MVwbNHx3Pczymagbyk0i3a-5kPcglYFLSpU1Bp8czIWSQfN2jckqoGqFufpKLxrje6YMAdnFhV_HfTZusSwZLsQm5mt3yEjR7NAOEmrAAOTbSSEm1Rg6nS6EnfbeNXTVe63U7-WhRAKcm0jhtoVQ_4fMEGg76sjXXDZ0e8phZxAImkJkCfh_1TpCS4yIst8H4WAIBhCUvFf8CBtveQJnWFQIb-pM2IOXpTf0ph-U8gzvtQmgvAqBVBhdBy33wXxZ0ZFevvt8WcJtER-UsnM3a3JqNueldyHACTA9RaUQ-fZR_WJ_XLQjuQ_lU4QeQlnVxfUUSj8FudWrz_7OEdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=T3CUu-wes6e14zPNCyAPm3pSZhdFoLnzQI0huSZNaxLIQgimoxICNagoGgmh_2JSFRxPvgqRrO-Y5peMle11OLnf0FyVDYM-Umo7sKiIOASFhoiHKaK-yKtXmKk-3ssJETL-ymDYJOgvOg4p_MJHuOpQ9f5_YhSkMxy1FLC4BZHNfT_5MZ8y9UavZaWl5B_idRAh7il0p0OtTan-d9CuuHLm2wRM6sQxtFv5EYTwaYfF0XkHG0l3R_7MoPEuqs_GkoBtikPMilv_VIc-Xr7lpd5USwb7s2EawY2zmaEBKnMejkCRwMKbwQzmdREYSlq7xmtlXvMEo7qQ7kFqBNGLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=T3CUu-wes6e14zPNCyAPm3pSZhdFoLnzQI0huSZNaxLIQgimoxICNagoGgmh_2JSFRxPvgqRrO-Y5peMle11OLnf0FyVDYM-Umo7sKiIOASFhoiHKaK-yKtXmKk-3ssJETL-ymDYJOgvOg4p_MJHuOpQ9f5_YhSkMxy1FLC4BZHNfT_5MZ8y9UavZaWl5B_idRAh7il0p0OtTan-d9CuuHLm2wRM6sQxtFv5EYTwaYfF0XkHG0l3R_7MoPEuqs_GkoBtikPMilv_VIc-Xr7lpd5USwb7s2EawY2zmaEBKnMejkCRwMKbwQzmdREYSlq7xmtlXvMEo7qQ7kFqBNGLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=CEqa_dnINRfKXoQ4Jv7jC4m4k7sxQ47v_h6FaqM2Hch0pIfmfq4N7lZh4Sl3VgFBZjATDHmgcKNbKRiWDH60slhsgyNjY2z-0x_zZrUI4nD3D5yR2nCbK9JGU9SiVleEgRSSXKRxkjhb0TFbPo55Ms3e0VchuvwsF8xStf0-3dLuW-SSozmbXh3ml-iThZ2klYB-VF5Kjy9mmxxbqnAIZy6Cp7loClefhcbkyGt-5z1xfguVB1yFdGF-vAo1Id-Dzzw6Xlb0Nxt7BoQvo19f4yF-rUBRjEh8y7Lz2o4FfnfftnzfxQgo3Pst23ouLQQENGrXcCKSGClp62BlRl59pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=CEqa_dnINRfKXoQ4Jv7jC4m4k7sxQ47v_h6FaqM2Hch0pIfmfq4N7lZh4Sl3VgFBZjATDHmgcKNbKRiWDH60slhsgyNjY2z-0x_zZrUI4nD3D5yR2nCbK9JGU9SiVleEgRSSXKRxkjhb0TFbPo55Ms3e0VchuvwsF8xStf0-3dLuW-SSozmbXh3ml-iThZ2klYB-VF5Kjy9mmxxbqnAIZy6Cp7loClefhcbkyGt-5z1xfguVB1yFdGF-vAo1Id-Dzzw6Xlb0Nxt7BoQvo19f4yF-rUBRjEh8y7Lz2o4FfnfftnzfxQgo3Pst23ouLQQENGrXcCKSGClp62BlRl59pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
