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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 08:38:32</div>
<hr>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP4vT26DbMfIlfgLMivVG7lutp701B9ejeapkLI0VrzVKU8LB7Rpp-MYYvHCktEgy4TwPnuSREmON4Wgqnpg6e94h0JY4LkYOnXPMN38jKz_2CxCvBFyMVUv5IqKYHIOzI_iupWrldaIQCXB6B3dJ_1nmo1ISta0JCFR6TuCeRLpsT2FxwY-Cs__7LdOwJPjdg5OhJo-vLfkb4KDFDmmR0c8r7vByxc-jJQ0sbH-anD6KNOyB0dAep2LXVaWTZQKuX5ov48GOGDHNaA5KTuY-9ndEiIVOpMPW7skJsiSszP25K61fdyg0ON5xH1NR0p3yNkRHfuewrO_X29ytGiHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=sM3atpJGrbxjqLNqV0xSSXVBwq7zzHjsBXllLF7EolXSllwmmd0BOY_CNZXZ2BPY_O7wLqtritLox93M2tsWG6ph1sKGfGBptBYg8tJ4czjXzLj6i9Jhg3JUYftbMPY4uM_ExTcQQrGrhXlRLmZZCi-JCxNiM75d1zwejWl_nE93GGdH22OiqSYVBEE3p3cAQibOTEqn6IEOLC5IPNpapqmk8q4-mS1KpOv9dld1TA4F27sYMpsgFW59234wjag4FmObZ5nZ0H0iNiN9u3CfhBLPhjAE3fupMMjHKC_zhaXucGAZk36Iev0lgPJlui48OfFdLSJeCrLZzdXcVh0mEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=sM3atpJGrbxjqLNqV0xSSXVBwq7zzHjsBXllLF7EolXSllwmmd0BOY_CNZXZ2BPY_O7wLqtritLox93M2tsWG6ph1sKGfGBptBYg8tJ4czjXzLj6i9Jhg3JUYftbMPY4uM_ExTcQQrGrhXlRLmZZCi-JCxNiM75d1zwejWl_nE93GGdH22OiqSYVBEE3p3cAQibOTEqn6IEOLC5IPNpapqmk8q4-mS1KpOv9dld1TA4F27sYMpsgFW59234wjag4FmObZ5nZ0H0iNiN9u3CfhBLPhjAE3fupMMjHKC_zhaXucGAZk36Iev0lgPJlui48OfFdLSJeCrLZzdXcVh0mEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYQm5M8_na1f9lRk_-0bw9mGXQuz_-oPfUDGp0V9Dkeik1fNfk_TiWSIsbsDad3LExQ2jpjo7plBKLMcQChzrMWWBZokCvTfCTUHHIHxQKtVksfKcBMJhdjFY6iFJa4DNDT0jOIMRRKwLbpmvf-ukE74QpGY_pNKwVpLfv8CSXlQg86v_8Zht6-iLunqMBari8ouTrlFFKuUxcHLexNL_ZSbXlHCNNziE_LImBDIlc3o3wWfhR5qmurtwVqtGJcxgFYq39_cUoAp-kAFKvF5KZllYd4ZoAuuVsQ8miMrLjUys1PV07hwniGxK8NT4Ke6sjGi2-3jIqSF_F3jl7c-Zwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYQm5M8_na1f9lRk_-0bw9mGXQuz_-oPfUDGp0V9Dkeik1fNfk_TiWSIsbsDad3LExQ2jpjo7plBKLMcQChzrMWWBZokCvTfCTUHHIHxQKtVksfKcBMJhdjFY6iFJa4DNDT0jOIMRRKwLbpmvf-ukE74QpGY_pNKwVpLfv8CSXlQg86v_8Zht6-iLunqMBari8ouTrlFFKuUxcHLexNL_ZSbXlHCNNziE_LImBDIlc3o3wWfhR5qmurtwVqtGJcxgFYq39_cUoAp-kAFKvF5KZllYd4ZoAuuVsQ8miMrLjUys1PV07hwniGxK8NT4Ke6sjGi2-3jIqSF_F3jl7c-Zwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=phjcfHW9VHEC32KTum2AzdYpVhq_YUuCwv_dDNXWXAYfszA2f7lGhmeOOWokMDyEPP6CwdnlBGXWUK62YPC1doJm6lSWDW1KMkwqTBRxCkA6RUu9xiqclSvA8853X62QrQAoSh58rVfS1vCp0b0G2ECbebF-Yv0iUy_Hj5LGSwxLB2cY9wH2pXvPXXwDy9ff3eNIbha-AzHlsi2rUzHtEN2MOUz-54x1MQUOBWa0_FNh6hNa3SvsWZDqYx7zrPCyDszlgdduhiDuOhRCR18dCXKcG186Y8nN-9eqAIPD7hIDfMGDvthmagvlHjSFNtqEUWm87c2sYi0enynzjynJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=phjcfHW9VHEC32KTum2AzdYpVhq_YUuCwv_dDNXWXAYfszA2f7lGhmeOOWokMDyEPP6CwdnlBGXWUK62YPC1doJm6lSWDW1KMkwqTBRxCkA6RUu9xiqclSvA8853X62QrQAoSh58rVfS1vCp0b0G2ECbebF-Yv0iUy_Hj5LGSwxLB2cY9wH2pXvPXXwDy9ff3eNIbha-AzHlsi2rUzHtEN2MOUz-54x1MQUOBWa0_FNh6hNa3SvsWZDqYx7zrPCyDszlgdduhiDuOhRCR18dCXKcG186Y8nN-9eqAIPD7hIDfMGDvthmagvlHjSFNtqEUWm87c2sYi0enynzjynJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukuLxkFYCRLe1TZ9CXmAE4TLj_hyZc0C1WFH4nOonFPymdI2cTn4B5fouHhmIPtVGnu9Q12TA_IWW-Z8-DhdiOnIr7yFK_l4ROk1DvBwon8IEUZzyn0UuuAoftQNgdA_1tkiHcstYnWWGKqTpTplP5na9wlewXVCrPnVwy0ohrjzpVIhrMLVKKqQ4361M33RQGqvODoNagymuuBOaIh4LpfeyVXAgZ7lo9dn8KMr0W5wXGXgn1E56l0m1E-1-FTAPwpPvSiugmLRqy3pUL9uALOmSNkmF-eldjNtg5G1sKPO1XNkYIp_uMS5qG2s-t1VkdJJl6Tf7e052T0vW4mtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2eUKqlhmJbtg1wz1NSlqC9fcAUgjXQiP8ek9XYRAWnaIigrV172WEec2Djx3UuWwtQWo2saLUbqgfHg7y_Mss5Dv-KvOqFAu5QJ5pI_gDJyMTYoeN_UoVyKMdYeU4gwT8OdGDtgvuJTVZmGIn5KzMg1zZg54RMCn_KkNKQ8jhcde7zg49GHPYVZm_Y8jEMLnVRnXkzJy6w1z2_KQh_IdOIZ0hlcYg5KmfePYdWyfjkaLIOIA7qlP7t6zKMRhz46IrWpxZ2rZv7ZMpb_d1f8XljoYRhPmOKIwQ7ZbAy6-cu2r32yWc3zE9fsn6ldCgsEM9A_5-FRewn9qTIlfjKedg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ftsAVFPthFDWCQiliw834FPu-MAYWFVjGr00VpuJxN-BMaxL8r9jZdKP-kKffhNatpPyPjrqfZzyZ2qlL-0LDSUeuMhBEZvZaU-0Obxw2UMNU1MqmtANAwHD3Q_kuxI4Pg94k-A5_5Zwd1P-49CobEJhZ0jxjLd44j5qSXrr-AP6L2mn52GQv6dh43ot0Ba2jJHgweB0a8ZSsL6O_WQrV8ZjKwsN_7pxXxtQVQ2qsS2pB__T6Mf0qqunfjYenYI4eObsYJr93pwbv9Fe7D6w9w7qsA9LExFb2ZqymtC-7MPPuTQhZxPn-gRLMU4GKnyMYMP9jxo4Rzq36rBbxFLRGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ftsAVFPthFDWCQiliw834FPu-MAYWFVjGr00VpuJxN-BMaxL8r9jZdKP-kKffhNatpPyPjrqfZzyZ2qlL-0LDSUeuMhBEZvZaU-0Obxw2UMNU1MqmtANAwHD3Q_kuxI4Pg94k-A5_5Zwd1P-49CobEJhZ0jxjLd44j5qSXrr-AP6L2mn52GQv6dh43ot0Ba2jJHgweB0a8ZSsL6O_WQrV8ZjKwsN_7pxXxtQVQ2qsS2pB__T6Mf0qqunfjYenYI4eObsYJr93pwbv9Fe7D6w9w7qsA9LExFb2ZqymtC-7MPPuTQhZxPn-gRLMU4GKnyMYMP9jxo4Rzq36rBbxFLRGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLRg9Dyw89v61yOI89w_JilRJRUQmI7Wq81aD-MfP2fCSSZ-qJLnofzUkAxV5ascqCYKMLx75EaOQKkNRWRRcpZd-UO_4xeU-YHdWWk_KlMyq8AnuVW4BXZJniJmr5U0Jf_OZoNNKMAQIl77S6987p3ZInHVZSdHiY91UhCbuVJlJ9vnjb9f0N3ZtyZofahzZof0xBxh4aUzk6wRuiVIphYBiNfr-fWWCnndMPZeFFERiJWI7s6MWzOE9pzIiG7yJrDABGsEK6pFacxh1OWpbbWDEICQPlQBmB1MIO2aAKFGesL_bIpUzrVqLteZrkzq6_ccCQPs11omZsotKvrszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzu_btavXw3ZvXCs7ahJmIaW4OCkUBMHDw8qv1BRtXp2yK2flhKuDsxudSyXdnBwvU78UbEJ8mE6Ag7osXRXeVEyc5TEzY7d0LgONr1Cgk4DdxPrinua7QPiPXQvZvci_OXAvx9omeOA9I4-xW-i-cSdTdkFgi0U7BAaDRSYzhMYJX0l0cnQwYznshk9mUUneiHo1EQCOept0TvV1NG-rCG-Vnm5D4N6Z0h_yWqKQZzOM_ko6_0tZVAU93uSKbPVFypYSSBEoeb4kInopCHvT_6Dm911gR9Cn2HpaX1VJmnP7O-5mbdoAvhBjub9gf4thYmElvfZmulIpxfnqKwyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6uokWHefM2fM7P7S2XWN2qviAfrNiTLl8FPWyZO9bZtrgaXVkib-JtP_L1F_RDN-00EYaprFeoFHxj7c2CAOriVW_LLtFI676b-7q2iOj20t40aYRglm7lvcdJx563ZlKsi95SjZuf5crSUnXaZo8RBrPeINa6dkj-pEhR06V3GcO9OQG3L5l1sZugoVo6-WrNoLatFHHVL0hyBj7wQtznTNd2JPXntuAC81JiISujaKBRI2lKE53BRhXIk1Z8ZJ5lfJsb6QJ231m1cG4E1QckEPYgqb-yHl2XSgzoGygg2Vl6YOMfw98kmnmRyaSfZeB9GxSEZi5k52XedZhE79A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpjRgWjjrrGbLxeNF4O6bnIvD8wDlp6CmuioJ3cVSY7zuAHC4CMubtJltBjQ4T-Iwt0KSMZEbuIePPYOipSC-YQ20IldTwHbaj3VzpdDE0wA2dq34Yyg8RPvMN21C9Mqf8MNMPqYtgn5h8v8WqO4klNIOEBkH0tHK0O6WnI-RWCWaznsEuNUAO6xMaMWk3XE-R5xPaTqj9_vvF7rPL-pfuPUGimoYtsCDFMtN1E7yB7euvx9x-Ewn3A1BybN6zu_ggNz7bnCOS4VEdV8aKgauw999uU17tPTl0u_Buna6tmJXY7_ybeitCXJq0Ao5w3dgxs-KDPof_D3ovfpvXsPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=B_1KabHD8H_Fx8m4zlphdnaRX6yGGGGfqBf2zIFMLj7neIaE_hhqy-I_tOB26nK_TQ5Umg8NjIiJjQGanr238EBcZCRo86Pvb9KSH3Ft_p-YH5pkRPQfz0Zc-WiwX9Aajc2t7yerGCK4hiV9G8h8BOpjmzkelJGYpfeuTofWzdkeSVLLUHQq81dHsxQMjnvGYNxLtpUDF5wQa3IikSsZdGvTTl8VQXvBtETEIcF69YgLAleW-B2LNIDURVSN4OSSa8FEhPjV90rMLH2waVxRj0Cn-E-rYXNsEGxrMTGxk5hwM_-3XSRLjYu0Bt1kWPhMeAzjXBHckNE0wyxyYOcbOBA6xDYZllQ4xmtAIPlzJ7vijUYqRKmSNQUnCddgu1c8uCBut55uRaNy1ZFQ-IVFaCj5XkcnCLApdRnJcTFCx8RH-HQsYGD1LbA9IHyZAI2OJzZHK-dxYylgDL4S8I8TZmx82oV4_DQ28aV0r_cb8iFhqElN3WRQ2c1d0gOuRmXXUjU9yZi3tTYLLMh_1F3XqxfpC7iNOzK0P1qWJI-X6iU78LVzH0emvVTyrE1MXMsOoeywvjfP2Hdb6v70AIZyv-4VVJMxMfFb7NWghcTNF6cLtoBoT_pKXQYZwoZJws1YAIXSSIK_WV-xDMh8yzPWpZ6rq2TCA31QEPkdQ7T656Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=B_1KabHD8H_Fx8m4zlphdnaRX6yGGGGfqBf2zIFMLj7neIaE_hhqy-I_tOB26nK_TQ5Umg8NjIiJjQGanr238EBcZCRo86Pvb9KSH3Ft_p-YH5pkRPQfz0Zc-WiwX9Aajc2t7yerGCK4hiV9G8h8BOpjmzkelJGYpfeuTofWzdkeSVLLUHQq81dHsxQMjnvGYNxLtpUDF5wQa3IikSsZdGvTTl8VQXvBtETEIcF69YgLAleW-B2LNIDURVSN4OSSa8FEhPjV90rMLH2waVxRj0Cn-E-rYXNsEGxrMTGxk5hwM_-3XSRLjYu0Bt1kWPhMeAzjXBHckNE0wyxyYOcbOBA6xDYZllQ4xmtAIPlzJ7vijUYqRKmSNQUnCddgu1c8uCBut55uRaNy1ZFQ-IVFaCj5XkcnCLApdRnJcTFCx8RH-HQsYGD1LbA9IHyZAI2OJzZHK-dxYylgDL4S8I8TZmx82oV4_DQ28aV0r_cb8iFhqElN3WRQ2c1d0gOuRmXXUjU9yZi3tTYLLMh_1F3XqxfpC7iNOzK0P1qWJI-X6iU78LVzH0emvVTyrE1MXMsOoeywvjfP2Hdb6v70AIZyv-4VVJMxMfFb7NWghcTNF6cLtoBoT_pKXQYZwoZJws1YAIXSSIK_WV-xDMh8yzPWpZ6rq2TCA31QEPkdQ7T656Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmFiPOLg6BEI_q8WdPTZGKdZETjG3eLh-YyxPp-Q5u620mLqvInftkr1uJXR5ODQ3V51HIHSeCxTHIY4idoaQNXA-CTtG1gi7O8PCP1hB7FNaCvj2qOkr1dmbTrjEOD1PxfwJU_RouSt_wOPi1reEPgRuN1KyCl6g81plhWgwLdji-alMr2n3IDPNikKFsSZG6m8TecQIDj0lUqJcCrumo7bAG-Ej2QoDVKyEAH-Awn5W1RWfie3bAzOfH7NGtqFCSvsSr-HeJDPZBFc2P-qOdk24kUISkZmsEicWa7HuhiNHRu-8NtR1yI2-cARBuRebXNzteopXrvTpIK96ePzIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmFiPOLg6BEI_q8WdPTZGKdZETjG3eLh-YyxPp-Q5u620mLqvInftkr1uJXR5ODQ3V51HIHSeCxTHIY4idoaQNXA-CTtG1gi7O8PCP1hB7FNaCvj2qOkr1dmbTrjEOD1PxfwJU_RouSt_wOPi1reEPgRuN1KyCl6g81plhWgwLdji-alMr2n3IDPNikKFsSZG6m8TecQIDj0lUqJcCrumo7bAG-Ej2QoDVKyEAH-Awn5W1RWfie3bAzOfH7NGtqFCSvsSr-HeJDPZBFc2P-qOdk24kUISkZmsEicWa7HuhiNHRu-8NtR1yI2-cARBuRebXNzteopXrvTpIK96ePzIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=ceRnuiANP2bnKiTqb_ZYx4PCskFJcmD5xiQfyTvS3rtlo2j9Z1GfYBKc9PXf2l0gp-VJV8eq8ynEmcPSHZcKlli6Alpc5G16BxborgpQ2eM7QE_V1vSOfBXoxlGC0lqsv77DqR3fBSUp-8xGIOaciNuA1VveuehiiqP8sNqyHnpl54BknA_ds4nw1ZZ67TjZRzWb03hHA4BT3JJ4cYurujbeMTMrxFAlYE4L1E88PYFroAA_PPT3ehcdZTw-LfIH6J4fwnmCb9SqbId0a5LBqJPioxL4twyxCZNfNmq8TVE3O-XiCjsfUJrJU2f9cr6NUdmyGi6YLcIbCNaSfvWZGIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=ceRnuiANP2bnKiTqb_ZYx4PCskFJcmD5xiQfyTvS3rtlo2j9Z1GfYBKc9PXf2l0gp-VJV8eq8ynEmcPSHZcKlli6Alpc5G16BxborgpQ2eM7QE_V1vSOfBXoxlGC0lqsv77DqR3fBSUp-8xGIOaciNuA1VveuehiiqP8sNqyHnpl54BknA_ds4nw1ZZ67TjZRzWb03hHA4BT3JJ4cYurujbeMTMrxFAlYE4L1E88PYFroAA_PPT3ehcdZTw-LfIH6J4fwnmCb9SqbId0a5LBqJPioxL4twyxCZNfNmq8TVE3O-XiCjsfUJrJU2f9cr6NUdmyGi6YLcIbCNaSfvWZGIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=T1Vz6o5ka6vBXCbwKVzONFskGHK1axUFq9q24SnlPj6Gnq0HbkDVhX6zjN0KPOfGYPqjf7oPITA1uO9uBJfNFhgezI8BgQ5qAZxauX2lXPVgyBCe6L3WPohCRrD9jjaILdPyqVj2txIO2vAjGweFzUxYbRZMpnSgoeiLqO7gzIVlRZMKkScsvjXMWiiJzSErtgbqSZ5HcUzgs3RO2dVpYHe1NbC2j0Dux29fL-Lj6Lb0CyEm79YoDjKWwF2PlfMsJEFXKvkUxrLMhNz-8qX8Hs7qLWxMUrlMJP-whrbUAKyR85GRh3NaiQQ3rnJsOHEV96kMBCI-jaMfvd83Z6QjZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=T1Vz6o5ka6vBXCbwKVzONFskGHK1axUFq9q24SnlPj6Gnq0HbkDVhX6zjN0KPOfGYPqjf7oPITA1uO9uBJfNFhgezI8BgQ5qAZxauX2lXPVgyBCe6L3WPohCRrD9jjaILdPyqVj2txIO2vAjGweFzUxYbRZMpnSgoeiLqO7gzIVlRZMKkScsvjXMWiiJzSErtgbqSZ5HcUzgs3RO2dVpYHe1NbC2j0Dux29fL-Lj6Lb0CyEm79YoDjKWwF2PlfMsJEFXKvkUxrLMhNz-8qX8Hs7qLWxMUrlMJP-whrbUAKyR85GRh3NaiQQ3rnJsOHEV96kMBCI-jaMfvd83Z6QjZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3EAJNZTvdHjlQYg1oHYv2OV1tCRuMLuWFamd5x4LeJkXGUlvWZLmV-2B6-3SUx6Yxc0Yvb6lYetIsZpLz7F4m9Qy1Vv8xyzZ9NVp7JYe3a0-dfzHyL7vDb9fXikc8CiJlV2bN89KFyio3c4BGH5ywo49_A-31LzcdvwgZ3W86thzNB5L-GdTH9MHVPqReYbZpePimrBfDpKsSRUiUiZhXs93RGKPwbZvTsN1KMBqSWBSiGshcpFGDbgaort71Gv5RaAgvlhsPcyuKnvSbEy2esTNmUoBSu_eW-mZHxg3WIj8E7Es1mmkGOhI1-0VzsrEXe613hGC_Y5UZnO_qCWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj4ZogUfS3crtjRoSEVUPU5gZeIfMCQbAtP1NEziAIvGJ0-2mb6HEVnt0M27S1B_7OptZtAke9acDkAXGwg-8mkuNSoQNHUHa72BEdzBxJdhRQ3jVFCrtijSs24ApzazTP-IknLxdEeWjmCdW6bM04RSjZNiM97NYq1P6w9s6YEr1ESfdGpTnPkwiONlQfd1ubkko4JB7GOW05OaxzsZiGNQx_k_YvtB-yOGZUbbXhEp3tvUujfDs_Xf-n9t9vuSPYpXG4OmEFmFdNLuvZozffKXmir-BI71JpXBqcDWv25ObsseWCAD6LGqG1FbRasA0Ggi5ASMiGIPbeBRK8_JnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr2_dZm3I7cYSd0fahql1E3Am5mhMzzX-DN2S8qO-hIJASKEIBHm17RAo5o4u5dBoSJBRXOPYEnhseWE9ZNhg59l5n40vJx7s4bAKHrJE0tebcT-4-YhsuVUpquCt2LkQ04HvFa40b5W_SOz6jwAIbE13HoYe0fch4ktb7q7U39-VtWX0jATGz-2jDAP_pRAO_lix_dXTXcFIVQruCkeaWuczGVkNj7TcetgJw_etyJXjIis3m5EbHecwLzi1XpQa4YsV0hC3H6oDilWLb9HFJdqy1_09UlKgR2-81iPgXP1crcIiOOHYI2perBCxucWgj0Ys15wWlpbl07CttmUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZRtWqXC4jPd4dPDJPHKe7RS8RHMJSkAOBQ9WCthKDt6icVAb8eNFx5vWzNYYNrC8dQFQ-rMcXyrXSb59Ue3zRv0IUGVBX-7DS6b3XbW2-B5xBRfhQ3y0panIVMdt7oQsr8avGMJq2r5VLj6_BH6bpU8ne34H3WbvcgUfbdq-JoztQTMz_Hd1tufskG9lLJK1B2IHnxotwX1kR9WS1ojmIOLMhGMescLknaI9i-ByWWMuuqbhuIIZGq3L5qplBuW3MlwIWqRd900tEmHTslaAneNlXl1nR4D3ELmvziKqsA74LOz9c8VrKTUMT2597gV_1ZYbe4BXMYsR4Uavp6pJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=pj-TqkqeiV-IYbRsb7u1ZKScRT-uOnq1WrQ2LmSDEvO4AfXVIyJRzb35nT0DVtC5Xjzq8dVEBRPTvbsdJrvngZeCujRy23cbftpIGf-pbTfBfYyx9rCB_lMlWDF188ll-P57H4UI1pSHPrJzotXby1eCYNP1IfPTv3aIjhTzHOnniSpPOaQjLOvbuQMxkZzhU0D2yXhcD5shSlj30Nqj_10gBx-tIUO2nKdnhlzQmzuBynjxE9kxX19vUkPb4bugG8g--ggvb9LTdzB1a1Fbnd4yxFk3jUXuVflyjhPiaXDWeP60NH9iEHUwiR9G5gcq5T-Mag-W3wW3ka6hodbNLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=pj-TqkqeiV-IYbRsb7u1ZKScRT-uOnq1WrQ2LmSDEvO4AfXVIyJRzb35nT0DVtC5Xjzq8dVEBRPTvbsdJrvngZeCujRy23cbftpIGf-pbTfBfYyx9rCB_lMlWDF188ll-P57H4UI1pSHPrJzotXby1eCYNP1IfPTv3aIjhTzHOnniSpPOaQjLOvbuQMxkZzhU0D2yXhcD5shSlj30Nqj_10gBx-tIUO2nKdnhlzQmzuBynjxE9kxX19vUkPb4bugG8g--ggvb9LTdzB1a1Fbnd4yxFk3jUXuVflyjhPiaXDWeP60NH9iEHUwiR9G5gcq5T-Mag-W3wW3ka6hodbNLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=KOU0W-9qNP94x0lGzOf1pXY0LiIqI1c9BLdI5gjzp2_xXEbFOSPa_dYIEfR6sr6qNGMcWkLe5aXXiDKHx-1YZi2b6QkW_AsOmTfyFyKeqW0FBlIk9Rhv0pAHjyYHzO9eaNm9AwFxrnYNb2nwqHrcwOIGoClICBfbT6wrpIQ6mFohx0N-snq35Rr-lSO8S_7RN-56_27ChJFJg1NYihLM3rOQ7uWt4ulx51eVB5k7LxH2FZBa6qpNKHDO_e7RQd4UfmsCwOj2nvP5bIBGYZ3QhXxucJK_NFei9j5O0-7Ec0zC6Au-2ZfWvL2fzR9z2ZmDlKIc0d2UFHn4PfVzi9fPkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=KOU0W-9qNP94x0lGzOf1pXY0LiIqI1c9BLdI5gjzp2_xXEbFOSPa_dYIEfR6sr6qNGMcWkLe5aXXiDKHx-1YZi2b6QkW_AsOmTfyFyKeqW0FBlIk9Rhv0pAHjyYHzO9eaNm9AwFxrnYNb2nwqHrcwOIGoClICBfbT6wrpIQ6mFohx0N-snq35Rr-lSO8S_7RN-56_27ChJFJg1NYihLM3rOQ7uWt4ulx51eVB5k7LxH2FZBa6qpNKHDO_e7RQd4UfmsCwOj2nvP5bIBGYZ3QhXxucJK_NFei9j5O0-7Ec0zC6Au-2ZfWvL2fzR9z2ZmDlKIc0d2UFHn4PfVzi9fPkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3xjtQE2rGcnhdpp8LEIEqzrYSIA8vB6CpVn9rxwu2UWxLB7vy5MjrFctMqFREUXOEeoiFFxB5b5kglHCN7K37N5HDSAn-I5ri2IvaphYW9Lxu-hh_0UrYi-YlekqHbEkcaofyJLQtiVHM_waaN8TSJpRp9n4vOYh51SwiakTaRvmYwxtj7UC6qY-mKrIsmi1ASLEpm03RX3isEJItrmT9gopqbcScA3OBfnRxZhezPnGytjwBZAbWVaY48cTFbILENXzESuwXp5IeVdG9RvVTJsD5qVFiEZAISZC-VKWk3bLRH2sTJD1jw-AJneBhDcwcwbeuja_7iXGWVQDlrz_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKyL89qReHW2dXkD4evb4zCFY5Al3nNiBxsdYoYZYMehDvJ-RWkRlGhKTePAGJYN7y7NCblm0Gp-Cso8TsUlqKK7dnfzIilLP1AY8wn1Ju27ZDelc5ynWdOYwVp6WyGxaA-N5S_55Arpwb4wPp33gChoJ4eSEFHEV456mfDuiVbx9YzyGCxllWipD3nCDITk7cBJAeyy_gsz-CwqPM5gm5DG-HHUEzNnQh2pJngIoWEjX2Pgi0iaSzUdBGDjZ2M13DeGT7Uh2Pcicde8z7cvNu8w1H_InVgS0T3fX1cE_5NFY1ODvQIhyLzgjJTvgClEo7yYr_QhAIaLrNMLxUpGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=fXBkDeMMB8YEDdBU_F4sFOdzt5bzA9AxWEpmq026yopsh1-GwVZa3vp7NwDfKWVwMQpsH0MAhNRbwBBXbkiJiC3hC98Vs5BTgarynqBOjBxRz038CuZkyA0-q2Xmu3rczgE3TERX33FgnUMkcI_B4gEV37rbNV--t75kQgO1QSod6ZIQpFpWilFO-yFcYY3nE1npUOqFtYmP7VErwptnnz7tS2xW6OsjN2nzMCcZwlmCc0o-UodSXOs-1AFxsU0pNjj1vY8zJYl2Quq0l5FOiAMNMbsGtBJbWvTHKK-iy155EHVcShU-lvby-vraxBk9-dbSm-XZt1SqHrx1y9gKbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=fXBkDeMMB8YEDdBU_F4sFOdzt5bzA9AxWEpmq026yopsh1-GwVZa3vp7NwDfKWVwMQpsH0MAhNRbwBBXbkiJiC3hC98Vs5BTgarynqBOjBxRz038CuZkyA0-q2Xmu3rczgE3TERX33FgnUMkcI_B4gEV37rbNV--t75kQgO1QSod6ZIQpFpWilFO-yFcYY3nE1npUOqFtYmP7VErwptnnz7tS2xW6OsjN2nzMCcZwlmCc0o-UodSXOs-1AFxsU0pNjj1vY8zJYl2Quq0l5FOiAMNMbsGtBJbWvTHKK-iy155EHVcShU-lvby-vraxBk9-dbSm-XZt1SqHrx1y9gKbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=FVjRw1NhsyrZZq5QLRtMlbzwzp9aiDQqC9HK3TFrfXGTIj4OiWNA7APTDfPSw8TrnCnMlj2lGLOHDvPLbcFyq7wEvkqOQvkM1bz7RaeI9uOijhHFq_0cbu5jJRGxs-XAr8240wzWlTQh-ht-E3DyaauaIs-LHN8ey2dJXaYowsxd4O5I2vTANzGkKoq__4P6lhMYsXZlK24tssv8th8HX5zhN9F-Q19xdAFFnJa7F9IkL8JeUbbVsMDn-FkSPftH4GfZ3mvVOyGrkbxgFg6UyHYx4iofkvNn3aY7vCqgRPNhpgU5UceJm0uqhl8UpVqfEw_FRZcFcFPB4KM4APH4CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=FVjRw1NhsyrZZq5QLRtMlbzwzp9aiDQqC9HK3TFrfXGTIj4OiWNA7APTDfPSw8TrnCnMlj2lGLOHDvPLbcFyq7wEvkqOQvkM1bz7RaeI9uOijhHFq_0cbu5jJRGxs-XAr8240wzWlTQh-ht-E3DyaauaIs-LHN8ey2dJXaYowsxd4O5I2vTANzGkKoq__4P6lhMYsXZlK24tssv8th8HX5zhN9F-Q19xdAFFnJa7F9IkL8JeUbbVsMDn-FkSPftH4GfZ3mvVOyGrkbxgFg6UyHYx4iofkvNn3aY7vCqgRPNhpgU5UceJm0uqhl8UpVqfEw_FRZcFcFPB4KM4APH4CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruX64dKw48NBAmz-PrI_EnfIRQ2qihZOVg98gJMiyIVti4nxRUi1QMpjDipLCNV2EfwqpT97ssUhkKKFe7o7hCgEr_VRUO8H6mn__5Ewtu3LUTd4Q5zVvO7lNVT6ls92gXnORQvdehqydWmlOd7AcdAMcB7y5-u6WVgOWBM9GOthxkKeNkIvgaX102g7w3zu6R2xY-v5nWlEkR9ClO7C1ZKkHwnIJPEBe4wXe3zDFZIothfoKHdZVEQsV_6_8aCOmFAzjL1qaPc22ilhhgvtxzt-jytnqQQy6vFmdYaozc9__Blq20PvvRU8mfLDcqMycUwZlsSxHDbAPt2vfICB6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ff8_2wPFUFxzi5_5xvIPlfeDHWWkoY0rOdDre8PMOrAT-oFh9ZKSGhuyE1TrEpkPXKiqJwgfdL9li0AHt_oXbLpaNw-1i2Rzsg3fLiB2GQ3aKGaCspp6LNYFanK_pvRurZDtyZDg8WFtdKGILTEvizRsYGfrYhC2ZGriMIWt1W85mOw9Xt76KiuOOYBeBVkgkW8_8v1GfoV2ZeEJih5FAkEluImeIk2aOZ4Ma77ogyhG_8TO7c4xMX7v2U6wAqOUZa5kuH2hyix1OJJ57V2W5FGV8i6zOQZFnnX8dM-GeMw6NmZZo3gCow5FNSMG2wXPUKIkJ2bvc6yofmXbla2HvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcOLUJqCmn6rpu9pA8hk9rcKp7u2rJiyvGL8F0QWYjr4q9y3RxXbJZUAlVzZvcAi0A6vnNRMj-w-GcjzQr22qr9k6_sncHQriyII4WZRd_oxN2seldiFNM4mgwMUdzGCngSh4qTACvkP-NaPqKW5LMXs4cM7CjNRznNp8an1tfQdF14WjAuipjpnNZCngrya8BC-CUDGCOtvUa5yImG6kdoYe9wQT6GftoZw4cr4OAMkqZyate9kHpJ-1awredLwyoW-k67pxaZ9hNbNIAVVhjVneoMCG84FUd8kOSSOCSpjiNAnBi83WubUKg9VCLxLGJD1dPT6tSjC4EANAlZXXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ry1q-QYpFJDPW2s1njt9LpnAyMa8v2oMqGRG7FmQP3lcTN-lwWWRIArn9tq29hQn6aj70FKydehMROXF-p4sXq0xU43-erGD9u9ILcR47ptO6waDv7aRoUlTgNrD_AZtb1fBZU9snlMsL6OQFJNHI0Dy5u5R1OvbdwZlZ1M1nOpJluSqTGwhI3Mlmq8iySt-HnTqwjhe2-6a3QDQNphccBzqNLt661Ei6N7kBj5vR_lyihcMyAFXIHhOXZfpgWYbJU5-fdOSixY92T4x9F0HH13vn1Ych0CXB9hELq90MakNdMw3G6ia8YfPI5RpEtE-nYcoH7lW5CxA6O_kjNDv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ry1q-QYpFJDPW2s1njt9LpnAyMa8v2oMqGRG7FmQP3lcTN-lwWWRIArn9tq29hQn6aj70FKydehMROXF-p4sXq0xU43-erGD9u9ILcR47ptO6waDv7aRoUlTgNrD_AZtb1fBZU9snlMsL6OQFJNHI0Dy5u5R1OvbdwZlZ1M1nOpJluSqTGwhI3Mlmq8iySt-HnTqwjhe2-6a3QDQNphccBzqNLt661Ei6N7kBj5vR_lyihcMyAFXIHhOXZfpgWYbJU5-fdOSixY92T4x9F0HH13vn1Ych0CXB9hELq90MakNdMw3G6ia8YfPI5RpEtE-nYcoH7lW5CxA6O_kjNDv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj3vP8XtdVUwr8TDHsOMm-qJKcW0EiM3SN3JtzxB0RRZQZ4jROOQ_aLnQb8BWEGco0WxcuLqATBpfx13YioH9k9iYLpsKUvaXE0pzb7pnTp8FatGqDzRdRltuI0qMhGBsdogcY5M-2IO5eYNz4VfgogdomjMytBtyzQUkn2grQl9SksjgwlsSWaqaX1BKSG4t4g_WvkY8VsRRH5EzbML8oNZJnvl_aECicNUpr1I7D3G2yipmNlS8eBOiTmsof1dBtcrEcWK_SWKUwhfw0KHSAnNgevfovLnguUZkk0COc0k1gvrVmBniA_0vMNd9Fzl_SQGFmjFu7paXShoB6W_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxpwKi9BDsnE1wU-QWbhwIal2fPrT36K9lE2ROGLglubP7ViV1I4-vPEcUwwLvfXrkgia8_9bnD7fXHFenjZMraAH-PFfzTayOguzRd0xciez6GqjR9Ll4gjhQqeACwxtti8nOq22-NF1CMalfH5fZyTpXbSrK7IA1OPD_768VIKjwWmop0P1rRWIRaRbuSKgLlWTLAnORav2NN4DeLbKHL5zBQil5vQbillhyaISi4bEuzU-u5YcaGUjAQJ7IdXU4NzgYe1Do1PFNh91da3tDPp0D-xVMYT6enkB4GLc_f7pVfQldN02BLmbT2qHNHSMNDmMK-RRFxEuU_jK-nJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBQ4dJURqwnoT_mKsszcjhXxexa2jXxAzZznVCDBorPeaQAVvsT0IhQl4m5jJ3x-eWAoEC0SfcwHhSEPnL790itDxeRzQDslQ9KWtF4SbtUJSfIiRmpxSUDZE0CSRDfR3NWs9vcY2D81tb81indF-A1xRLwZscO5upD1uudHiWDfiV7UVcbpw_J0-uQPPSyWwrerVinj7LkTeYOtanwQklyoqv5VRpawRUedZJohD0ongTAgRm8rpHB4ImlyUTyAlZJIuf9o3_bY65wxcmEL_BJx6ZlJVeCO6-ZG6NxoA-PmOjMmQWXbImAO2zW23DSURQtYBPBx4SHgdKDPerAJUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSpN6f2_We2k8wn5Y3ps-OkulQThZ2IJnF_EV4R6UhF0Sp4Us8JIPMjru-qKrjfdtfymA9yHgNezgHmKwvaZb5oPmJpvtVFMDy204XZrFCWguCaJy0aLcBuFQiEu5mb2LjMCxbct3k-zHRjpatnP-R6WPmDOy-XP_dj7nKd8wQ4axNhtVu3BTcoFYQXkFAQ4B8Qes89w7UMVk_F0yuGUaeZL7QyWInT-YC5iZOUHaye-ZaE_odOtLsmLgYAI0f3SymaLRpXa35t8H23HptJFLe8f_1IF7NjEPUDb7tRjc2RbHLxQymAUA4v4sTGIXLzesHHP51mmv8svv5kFo2xWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=fmJ2UZhiB-gduPB1vRQDAJacnlnclClyXymhSeN684vKYNpDXEb62VVC703Nj6uG6zY0VgHmPir5N4FjUAinHeDVM2fUYWDpgVTAiSRNBtve5Gf7TKStN4ObIFr8Kv2TqZfHlenUoYxdMCFpvqUitbwIDDq3WzjuWb0HDU1LpRCmb-NVF15hB6fHmjZflsrjOHQcT1VxdtICbJTjZVayhFOOTB1qnYV0DdT-weRyuTHALF7yswzk6aFVRSVw9oQfDYcVCTMkb_fMdF1J-krHHr3pCY1JDjf-QM96eLQUgQ5jJ_ihrv64-xzvGnOFLhIXRUaMDraDqgbRqxHxAfGb2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=fmJ2UZhiB-gduPB1vRQDAJacnlnclClyXymhSeN684vKYNpDXEb62VVC703Nj6uG6zY0VgHmPir5N4FjUAinHeDVM2fUYWDpgVTAiSRNBtve5Gf7TKStN4ObIFr8Kv2TqZfHlenUoYxdMCFpvqUitbwIDDq3WzjuWb0HDU1LpRCmb-NVF15hB6fHmjZflsrjOHQcT1VxdtICbJTjZVayhFOOTB1qnYV0DdT-weRyuTHALF7yswzk6aFVRSVw9oQfDYcVCTMkb_fMdF1J-krHHr3pCY1JDjf-QM96eLQUgQ5jJ_ihrv64-xzvGnOFLhIXRUaMDraDqgbRqxHxAfGb2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yjm0PoPwIrrzAIgi_KreZEMkw6cxGXwsMX-jF99STS2GSo7-buHZ1sjF-0e4XhPkaOr1A_zsSsnqxLzh16rNdNIxD_kagaBp68qaZcpaG9GTlWOVLWCVo4Xw-g1ivpsImQ98v7jlNwq8kdfvyHUBFAxDccrk_gfAWt651Z5hXNS23ulSBgg38Oxbkgwn1m09R6pN0jzTByEiDKiog-7wb7u2TCIJeNwfTvfa3uNeOOoPnmHtko9pcpQ-O_HZoF-dHV3qtr7nGnVkmlbDdAf8VTOM4825T1cyHaW64bUNldGYNxPXhskSnSNRUYrg8vST7SYf82YEZz8w6AXBcn1-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WozXD372FtUqwA32RGGMofGvuXFNQ4KQcrrxuxuhUKP6OONMgAjIqoT8OrBwx78FmKGCWUlftM85fTdhqi0y6dA9os_QK-DgfDaM6fNHd8HA-5U1jUfqPur7ZBnob3dEPsYeHw-3euLo8dCnfc2uituKOPX72RAayk0m1dobXn9q4qrMsWe0wPgv72NabGSyKidrb01Tw07S0c1RoJgpilXFCfsSfeCG9O_tXQtiU9RTmgraotEKoSZyV9mqRjx1TyYSIQjra-8BgIpl5z2PCuSGcBaJYVNjbJdNv9du-9y1sG6hVczJlqRhYsHpMiCg29aex9w7c6W2I3mvqVwVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWiSS94X3rGlZpadXYwdrYJhtfzgGj9dfHH6-mUNFRT8RCTITyo0e-ypbGSu_1hmVZfoz8KjzdU-Nn5XgA0cBECx7CwQ1pf4gOWsSBoVTrJSdZXY6S2StVNQizF9-p19PoXJAM2Y8cQ3bitC3W7v_bgzXrSKmBx82nMxNqds_2Jkfr6aQz-rLspLq2L-UK07ghiGGfR8lhoMoyOXuMZjBG6WBXeu0fTKJguSuKazsyIx1QLvd1HJ5NKjGWnTbdzsyqc8BLORDrFtS5xocUDZ0BXin6RhMzmkDODmw3rt4ZKagvUiNGH40j7OY-8Ojn1j9r4ChvZp-V_dzNc8SGwxLw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=QKiIDAiIEB__lmSLl92v6q5Dmb6Dfrgfzlw8pART6Os8rQP941OvQsboJPemUOTy5WLroM0BnBXj_lSkH9YvMe1tA1KxR6hj_jUycJDqh7fBbqxjikwXs74giali__XSZm0Etj00nVVKVkuKlv3iRUBeWgwE6wQVCCpZtqYvfdP-R9BnfWAfc9SNZ58P8aHhB5zviX-PHqQoCgJUb4Zd7PpNhvOiC6nj8YkAF0SJZ-jn5KbhQJAMg9qzuRUjvE_LyvPGv7d0ckQ0EJdeuPs6SUbfcDhtEmwmufkwu5mQ3MY46dybROpa-IYG846AEmjODshk7VL9xC8AN-NQdS3zwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=QKiIDAiIEB__lmSLl92v6q5Dmb6Dfrgfzlw8pART6Os8rQP941OvQsboJPemUOTy5WLroM0BnBXj_lSkH9YvMe1tA1KxR6hj_jUycJDqh7fBbqxjikwXs74giali__XSZm0Etj00nVVKVkuKlv3iRUBeWgwE6wQVCCpZtqYvfdP-R9BnfWAfc9SNZ58P8aHhB5zviX-PHqQoCgJUb4Zd7PpNhvOiC6nj8YkAF0SJZ-jn5KbhQJAMg9qzuRUjvE_LyvPGv7d0ckQ0EJdeuPs6SUbfcDhtEmwmufkwu5mQ3MY46dybROpa-IYG846AEmjODshk7VL9xC8AN-NQdS3zwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=PX9-NlqVDyQj4iicVkgjoZwmsz361XACey4a2y6lXDiJBsJAnL3TzH8zOg4U1nqRkaSREYKG0YXkQxV0fC9Qfap0gm9jKulfVccp7lXy0uFN6atLf45ZstVyhyY9lrAuHmBzMPijscCaMKPrXq5poXEdCN1v9u2tHNTwDN7GlxDsTAAivlW2IvDHaXkbFwHMV0GOG7_wntE4nzpA9Y-CZzrcAD7OImACcSkDSwD5Dh-QFJL0LTN517VftvYACK63bYUhcnSNyOs8x8th7vJrOmph0InIho4f0R_2GBdFcBoibHpjIFvo3X5iBuV16BDxBKDevl8g-Kp2G9KRaLS-zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=PX9-NlqVDyQj4iicVkgjoZwmsz361XACey4a2y6lXDiJBsJAnL3TzH8zOg4U1nqRkaSREYKG0YXkQxV0fC9Qfap0gm9jKulfVccp7lXy0uFN6atLf45ZstVyhyY9lrAuHmBzMPijscCaMKPrXq5poXEdCN1v9u2tHNTwDN7GlxDsTAAivlW2IvDHaXkbFwHMV0GOG7_wntE4nzpA9Y-CZzrcAD7OImACcSkDSwD5Dh-QFJL0LTN517VftvYACK63bYUhcnSNyOs8x8th7vJrOmph0InIho4f0R_2GBdFcBoibHpjIFvo3X5iBuV16BDxBKDevl8g-Kp2G9KRaLS-zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=YMQvtPr7MZ8w2Im2GmCHqjFuuc5ilNzlyi83UiAWW76eun9tfYfH5oYLomITgJ6NK_wrXjoRxG6Jt7GvgkgZsVKmC0_-zOa_B31Xv2ENwFc3GX11RfU5Yv9PXpRiTkgb-nmZLueOhia8kMMKXSPkTVq6BF7a3pVFkl-GpApAjq40iEsGAb_oDbghY8SKI3QrHZc4B4rHmjzseS8i3i6pvgZ6ERb4x8bEaoJPj7RF6EiGrhAfTk9O3nevka-l6GcOnN_AYfE75JrTxpxeJpcYNU2hiVLNtldOzcScSvTHP2826ui_e3Od7yCO9qoYlsDY1Zviw_tsKaRJAImY3X7y8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=YMQvtPr7MZ8w2Im2GmCHqjFuuc5ilNzlyi83UiAWW76eun9tfYfH5oYLomITgJ6NK_wrXjoRxG6Jt7GvgkgZsVKmC0_-zOa_B31Xv2ENwFc3GX11RfU5Yv9PXpRiTkgb-nmZLueOhia8kMMKXSPkTVq6BF7a3pVFkl-GpApAjq40iEsGAb_oDbghY8SKI3QrHZc4B4rHmjzseS8i3i6pvgZ6ERb4x8bEaoJPj7RF6EiGrhAfTk9O3nevka-l6GcOnN_AYfE75JrTxpxeJpcYNU2hiVLNtldOzcScSvTHP2826ui_e3Od7yCO9qoYlsDY1Zviw_tsKaRJAImY3X7y8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyO9X-kA4ylNvVqe1gtOeeB_TV0Lkc6Y_5dGDztKLtLNeFjGtCymKFYAXwskQzMovq5oCrTI7PUZXxa1OFS63jt0qOA0IqBen51cNwubjbhL11DpofMdgjwfxNEdQSD4TBTzKZkk27PEEtbmYzbkqji7WMgNNDMpCV53LaW2PaL-N8u4QBfnjUsuW6BiFcN0Zb6BGH4jtQbIB0Gk8sKlxtYrrhw8GU547wi3LqcOaEqV8ayo3qhy-9b3F7DSY7w0JGD7xc11GaP822MMLdy0ienI5dUqLf34ewpgVa6bTEMsS2MYFBtod09GO2Wx7jBoweoKiJrzCZClZpwTQHINbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI7ILhSmo5CUmVQAUbtXxDOCzrvwhYiK3ZegpJt3mLsyhsroz8KReClzNCxrX00UlwcOQ2RctJYHBBeTMIeSzlGKkhwipL4W_H8Byo0y9QzgZgK6XWRxAVZxwM3x9v7TjEjIa38qOOL4OSqkstREH9AIIk08ZPzcOwiHNr7tXwn5oLSywrvsVwvoqYkEk1ZGQi-L9JknBcUjxzPF4CxOt_LInhl89O8PijFX0hjTMYUp-W_TBfm_sgpKPtCIh6SLBksl1NlDziOOlehtsfsuKgtwbXjgEVLNuhooE6iRkJGzsuQ3IbqVEkclh6gldRMvRyLQoAl2RdQ6-HGaevlsjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9CL5kdkWQdZw3NJ4g0tiM2PRYiphpr8ROXbUmYjgIHrYUHByln0AwVk6_pX5kZR4GeXBX5MEU5_ym_FyQz_ARFONHUu6YAN6dJuTq4XB8NDAzj4tP0Gv-bXEhdTNIBH0reX08oTYs3EtC_JwvQE49fwO1y8HI4veTJb7udYBLCmyOfFCudD-MJT8xNFjanTAc-KEbNP_07WGNgqHv1rbZyrvjoPCTjcQ4X8Ipns4gUUMjWxhwDtdBKtTcjfVQr2vuk1T-a-eZMQVuHTtYWFR2gzAVbLTulQBXW6F0BQVXOgHPKPuC1cWJ288wk8Eajgmr-wEG3c09_7kkBnLyX9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fix_y_rNUqx2SuRJL5dgaMTHMRd7XX0Jf3-YymDoGn_meiYSqR1Hwzn7CYBIg33tnRh60Vbun_662m8mZI_IKmm3cVjEdw2W6ZZG_5VgePKXRWtNiFU9aI5ErjMSYNlINLEI1fsLc79l9wdHAUnY4nKIrkNSppQZhVO8AmVMDVDYnNy0tAHacGtj3hS6V7fbjavrpufmvmemcbl8VMg3Gkfjd0p70k1xzPCWTcu2UMZP41ftqVo5cijrvbIKYQywTOYQSbzvUBV_lUJcmDbKl-AqCR527D1thENjHVhIYdYKGsZuGNVHRu21vB_B36I6X_fJixxvuUsONearFQ4-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ste32kwqovP5ndeTswNbbuMdgZTqwkuaE_EBx7qnWchJ7vTmVg0MMY0IynUGs1URrgd09MozZ_DSLkkqJ93KJeEZ4oacAD0KVsa7CSQZulc5Sj_IWIMHagReR7wYYY1OPwA31XxiPtWtkEjWldt1jmaRBpYirrxhQ08bgji1snUTIxO9ANAzOd6ta1nYBAWB-5oCX2cI7yAoyD8WdeRpH8iixMSdG5iYsC9pt4kjDT_w7kGxcIgyMQkRJPJSbaSravc-6Vfklkv2Egvj-E032OTgPtqVyNTA-zTB8A5Xynd8NNUDnqQpKSHELOW7_mEikbNEchGJVT6ZpGPN_tqXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej5c7KGDGRRDo6oJPEAZtQh-ZkwDKGoBy5Rw1RZkEkkVUmsCq8AMrq1oHjuZskQTd56q4u8AT6EviNnpyYFtFA54-jB80XRZOnQ8-2_Na4ieBeziPE9byiLqDci-NHJay8nEXXOwUQnUbKlwIEcOAhE4qiNGT0hLjD6uTDBaDb-sIdVQz0MAnFdoeaKLi-Bt6PrvFtjfl3fPVdVbX5HKrN3JqQHYOhgossLZu3BpFSAq0_rvFN_RbVWYfFWh04jz42CTeCQWuq3YTsu2qSeHkfytgLP3eZCLCQS48mWZtk8Yyz0O-L2BFQWPqf4eX1unCXzkna-hlF6mwoZQr6KViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxm_wCFYeZLj6AeTV0K7VKbT-kdq1bOQPmO-lyj4G5k7Vf5lBU1zO8Oa308E8mAXGtoNCLDI3PRYDrFgnW664fhhaZTDZSmQFRH86F0MC8A-9lqp3RFnwwdnb6C5lhtlFeSYFuEegMxkAuPq89dWycL2dOxtkcsQ4OlMLpM0XAl3NZ3VBP1NP5WKnaEXJo8wTPFCsYiCr4VoWYXw5AzsS2NmXsPEoFlnlSJh5SnO_ohjEXmQjd80GONeH8k5u8P7Z55u8q1db6WHH-xWmeJio77Fdsg501dwWWnRBoo8VkI3ERL00lXSdqnGCntJGUJnskj752MJkan2N_7Jl9R5xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNDR52RNCEYuDoRWZJz9fS2f4X941AWbqLukyrQuRksxCIUncas2jIoDFjKgfnCaeOy-bDJBLggJrVnrXppt1mYzXyQYYkTpOKXBmaknlWyXvIOY-gGjw7tm1AZM2R8M8112DjITyiv6aZlCddc0hH-RrXMGnukH0Sc40lkhBc8Eo6v1IZ5FUk1DmGrWqw7UCIJly2kpO1a68WwmNZ2ffw70b1yR63ES-T16qXZSycYaFwY9b0fcifRXxpbcxKrjzNHe5kfWxXPzy701RI7gPo0CQjTghdvO0ZPk9DIw5VdV-rAEcP8FqjZrd30PyiBwkdUyfUbh0dm3ae4xkAriEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjd30tGj_PJFAJQbBVZISdhPasjjyxmvHuN2WVBuGN__2VMS1rzQoMH-7h2BeGO38_0Xbrb0wcvjpCd7TFRf91-5cYpzss1uIYu2osNHG__lLGx_GZUfoCPIKZTECpiI9nWCedsEu4kAJyIau7M9xVMy3l336ehnCEB4PYDKTc38qW7uHJenhAOe69zT_zj0pUBdTzvKCuFIe1gUKCWti7rZ4L1qdPQsUXpWIjio_ogfXDpcxsaWOoiMkDIywlWJa5JqCjem8pvwPxIXH3qqnRgxkPzMqph24h_NNIB8lo36k8ykjV4Q2bZCtG51hEKiOGvMkFp8AdUsNozPFm52VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2Qcf4zWuE0NXa5WHk20nvXqp7-HJ8mZsqCvFpVLkVCJTWQa27MQCgG5ZvBFJ3JEC0k5dyVAJ4kftibtZu4FP76KZeAY3WrxUdf-XolHwUA5WFp-YwLO6Ml_569WLtAY8-148pUP5jhH1rp_Lg4_8fbivHXe4upC9sqa2J0EWMyoTwzSDOCgEFWytEzO5UvVlBqKEdybn1aouZqLJ0rmKa4KzUbz0OmqwZwdzxnCGCNIhr5d1_hEkvN-G2eG2h7V668fSOvTZKAn6FnGlQdYSd4BzDn5jxLe9GXANu_h3_gr1ATXt9M2rUA6CPH-edf_N3sbm6EsUX7PJOtCAeDCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEHKj5ChQ-0_HRr15OOk3uFoSXmZ6qGJfVJqKJy5jiE2XVLQsw6412r0KDRElExvkMbWmD2Pc2YnmIX6EL2ZvrFeQi-9lDxWubBtM7S60D5XMIf27yU0PabnQuGHemZZViJm6RFH0QKJZwVyCRRVuUVXEDYg5kxsrCfIbNt216vaUKrX15GYoXjd6-Z4Lv4PkB6fTFpeTQgdow9XwM02g6q6KjZ3KOE0dOxHxf5o1v_CX-476e7iLVNj4A6-MDwsuzOpluk4sgt_iaVu308A_0GGL3X9btD8uWIKOV1RTqjf0AowBw0YkYYFVr9PpOKx7g_wRhV-as0C2f61pkpX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JH5OKnAyNh5eGMy6DWO00ICgG6DPS04_2JSKBqw-PRIemytEBjdGzHoMUeEr8WO2gvxQmsfdthuwEXPU_lQJvUtp0f94YkMQGCyN8fC3SS-22N_LHYtGXiEfiNXyH4qVCBLGw-hlrhJ52MJR0b1ckriaoADsbAeVqCCXm7uHGZD3drrZSiGa46i3ev1elUlMovMtRSVctUAMohbPd5R6lt_Y8-vklhU6gaqfGFBRMT5SBLAvkWVQFva5p4wmPE_46b8qNYpD04CvpPQtYfFrSY82-o8sDhtkxYU52Nv7fSERQ532GFDMDDYjZ34K3sYA_qNa09JY-mZAi70RT9sBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omCUUsCElu9PCbP0IelTc7OTMHKyBw0mCGPT9-_LoKM8Q_SdPLCU1UTeRd97tXfaKbF8FqWsWiNMO8aFjs1-gdKbf8ohquj95payOXg98Y1tT3r5rDnBSMseOfAQxga_Ohx14uOHgm2-zuGezUD9NpNC0Rp28HxAds2etMsfyjrRImM2YsvsDphpUT9iwOrrvLgV7uk5aZzzSgfmNSWjMCcTaDVMkPs8POzy-PxC_dipi4kRJXWMM1GLK_4gqTRAReePEI7VmRtrib5JtM_r1z4QJwcL891LNYOWy8qhkSHib38Op2_Ao7QBh0JwcicJo1rMNIJgyny7Ob4gwDfoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwR2bLSHF5XgUP2DCo_eCf8tlbX_avbTvCDGYcNdFF-IHigJ8m4aoqRItLw9Pkxnr1FYE9U6y_PIV07AIJKYfELozuw4l2_StDWeMNNlyuiXhr1BS24FFwX6SUF8CMlbeHl4jOnCLRrkGi2dhs0scOkVboec483lk-xsMXHLNVtkuK66SBmU_Rqs14m5JoF7pSjC0v-u1EduIAXNXdNggBBoDs0YPhdKPm9TlCK2m6WBHnKA1C5EJLjWVcVAh6lThIy8yhi0TO39LtImuRyeqo5eBKYUw4XPHUoYBrNZGidVQDX4QncWG42QyvGiEsT85IaD96KOSOGlTUe5NdLuVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUV3WpP_u1Ax3qS_U4aWTnUztzVdOwbP49Sj_bkocPODy5wCdcV0nbiDUxosstGmX6K8aqDaMy8oGafN6c1AyH2G4ofVzwAP2Jhzfil7zPyED53WxEGSkWCYbZmNvR5HJjhPgS7MIDKb6bzRn0KT0SnEsGQPu_YxDWJ9oMJR7ouuT4qCSVSjg_FKPQvRsUHun8IuYGbUNqWRamIS4JAc3tu_GiKoQwPzWFa1UeuYFvDJxlRhSYXnt6ruQm7kdoEZnR0n_GvXp3nVjLn2SSF-9Cd2hBs1pqB6fxVVQUnCN_g5WmbtxXK1PzAOW-n1y43DnKpNSIrJBgVrgcC1I2_ykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=EzypicCp4lMHKIM71ly94OwK-QPlHHFm01aFbIF6IpETULbFmD8R84IYLFIyp1oXMJwPoNkJ2j408jJw_AcT0EGI-NNPHaybR5vdpzC0e6osRGr5VYd8CcDpoQIwDquzcaJdSTzyYBRQ6frjjLgkEVoZjoWyhlwjCaUhHZEDo_6aUhy3j4e834E9n_XGLKcfOXARftfXqZBqru2LkIv5MdJn3OAZs8ovkXpAdfBGiMt8D74npgBN_SFyeqkCZWpGU96Vg2CfX8SVIT6tMJi3_zPQaxx-pXn7jHFi-RYEltBkjgEdBqQe2j7gB9PbjA_cVDv5W7d8U03Q5VXw0Kf3pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=EzypicCp4lMHKIM71ly94OwK-QPlHHFm01aFbIF6IpETULbFmD8R84IYLFIyp1oXMJwPoNkJ2j408jJw_AcT0EGI-NNPHaybR5vdpzC0e6osRGr5VYd8CcDpoQIwDquzcaJdSTzyYBRQ6frjjLgkEVoZjoWyhlwjCaUhHZEDo_6aUhy3j4e834E9n_XGLKcfOXARftfXqZBqru2LkIv5MdJn3OAZs8ovkXpAdfBGiMt8D74npgBN_SFyeqkCZWpGU96Vg2CfX8SVIT6tMJi3_zPQaxx-pXn7jHFi-RYEltBkjgEdBqQe2j7gB9PbjA_cVDv5W7d8U03Q5VXw0Kf3pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTxSZrJdHrsgqVdLSrvYBofE6tr7yYctZ92igGXd33yXC3U9t2zaZ5AAeHxNjnKKKbpqT520kNbHEbVmWPPPOzBrJBmKtmMY99p5u3cAoxOpYRI8b5pGsPbyQobwPIsJa6AbBfZltxJXdadC0gMIysDi_i7_FO5vle31Vh9QhsFH7UDDpJnpiPTGtUf7KnRRRiNCoUhiyxfzqmpQGxlKNT9_PHKuhaAXU4XHgqDWce1Jm3HhCsKOEC8LRiwwq2V03dnz7C3eJcOzrtx640fL0R6SFkL-lsEfItYpHir0-TTv1oMkBxdyWy4UURqMmparXr03U-CiuTEtLDXrLWQv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=h-dGL5mAwRU2RfgMPT328OoqyNPQgDdN5zWJIVAaPOkkwSBUpToV8NLkxe0yhrILr2qT-94zEVnYqsgjzLafGOlbSzua4QOMFnVwAaZMTGj8hDs03MIaU3Pbe__wERQEzRGZ69mgWQ-LHi2TtwpaLaoSCnNj-W0_09EF08QbORSgBgkypATory3Mra9QVT7GmfNkzbIHta4QSJKs7ZIS4KgD7ayWDqIhkIPBiKYrJevbeeQkLQXR8HMyqyKEabJRjOtP-q2MubXxTxSGBTuKyUzfDcGs8IGniHgx9NWdPt_bc4d8yjddyh7pEgfXJDeEKINZwM2EDcuyZ83Z9bz6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=h-dGL5mAwRU2RfgMPT328OoqyNPQgDdN5zWJIVAaPOkkwSBUpToV8NLkxe0yhrILr2qT-94zEVnYqsgjzLafGOlbSzua4QOMFnVwAaZMTGj8hDs03MIaU3Pbe__wERQEzRGZ69mgWQ-LHi2TtwpaLaoSCnNj-W0_09EF08QbORSgBgkypATory3Mra9QVT7GmfNkzbIHta4QSJKs7ZIS4KgD7ayWDqIhkIPBiKYrJevbeeQkLQXR8HMyqyKEabJRjOtP-q2MubXxTxSGBTuKyUzfDcGs8IGniHgx9NWdPt_bc4d8yjddyh7pEgfXJDeEKINZwM2EDcuyZ83Z9bz6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Bg5kJcNbhFfC12byA2lS7l1c4DNJADuv7EKfc-F0aNXqQGjuoHxeQ7LD1hSWvE8WmmjngD7WRC5LqDB-iyRM4v4WkqrxnVFoWJmkgVAGsKCn8bUfS1lP-1juSzFAxBrPtGiR5cw24Mc1cGFB6PLkBBy8H9v0ZKE_WaU98J0cj4GTYJ6_YFaOrfRRcoAuVxrtH1vUOPpwUj04yLCLRUcu1BUhLe4ArFGLlqDBFTaZNWijKwq1KzslwrQXgQSYigk9zGmYD1dd4TwpfNfvX13mRNwCe7P1znPx7PWTLi3aAc-HXcppz5K2Ccchh6xODNmVXOV4AE2GDhC4Mw01gfUfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Bg5kJcNbhFfC12byA2lS7l1c4DNJADuv7EKfc-F0aNXqQGjuoHxeQ7LD1hSWvE8WmmjngD7WRC5LqDB-iyRM4v4WkqrxnVFoWJmkgVAGsKCn8bUfS1lP-1juSzFAxBrPtGiR5cw24Mc1cGFB6PLkBBy8H9v0ZKE_WaU98J0cj4GTYJ6_YFaOrfRRcoAuVxrtH1vUOPpwUj04yLCLRUcu1BUhLe4ArFGLlqDBFTaZNWijKwq1KzslwrQXgQSYigk9zGmYD1dd4TwpfNfvX13mRNwCe7P1znPx7PWTLi3aAc-HXcppz5K2Ccchh6xODNmVXOV4AE2GDhC4Mw01gfUfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx2I-oudSJA5iBxvFLpUQRLYQGxBg5VUt7jVkvzbKjcwcALAG6qIP3XJC3ck6OHVAzYd58JrS86qoDjGl6O37fZsQXUd5WdGgGZfgluxDNrMixFzKbTZKzresx8heQCyXdCr3taLK-9mAkml7TyDoCnH-ib2cZqgHQKWb90ACZO8NqvVje6k-RMJERITLJz43Bojms-AkrNEcC54QWWYHKhHhyN-Uz5nKbyPZYe-WCgourNKC1GVQ4Zr39bivKG_UyDi02Zm3KnkBARzud1GNC29IIPbWgdcY8_3VNNPnQzCZG9ufLgXtes2yoPbukzIzDmMPfEnkYf3anJo1xu6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=NxtUoAq1AZAVX_ulJkjImIlU4YDuZwOiLneGYKXJ581kohWl_n0RvKlqni_IhesFY3LxILNoWupz7GsI45bZ-oeggFBjiyyjnjMjKrYXY_OSyC_iCV5WInjqXkt7PsEUp0kC6atLhXb7pP8IsCA8rsObKeRdZ0GSL8vprpK8ow4JoNdMrcYFe_S6i0mncBSTNJfsK9jkcPxvASGVvoI_Eg5kSFOGNpxKvfS_rHxBGEbRuXbr7T_y6JWqaj1CJC-cA7NgzB1Q_bkFM29myI0_4Z0381L9TCvXYJ94YtEcOizEwC-FPapMJU968Flxt8E-hEbkqSnMoFZroPn2_F-49w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=NxtUoAq1AZAVX_ulJkjImIlU4YDuZwOiLneGYKXJ581kohWl_n0RvKlqni_IhesFY3LxILNoWupz7GsI45bZ-oeggFBjiyyjnjMjKrYXY_OSyC_iCV5WInjqXkt7PsEUp0kC6atLhXb7pP8IsCA8rsObKeRdZ0GSL8vprpK8ow4JoNdMrcYFe_S6i0mncBSTNJfsK9jkcPxvASGVvoI_Eg5kSFOGNpxKvfS_rHxBGEbRuXbr7T_y6JWqaj1CJC-cA7NgzB1Q_bkFM29myI0_4Z0381L9TCvXYJ94YtEcOizEwC-FPapMJU968Flxt8E-hEbkqSnMoFZroPn2_F-49w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmG6QELV6wFiKeHgRlkGNJp8_UQFOmdTCywZZVmCZGEqE_vojRQFFXdOjixpSHt00MgxsSXm5hMzXHYjUJfETxDFhAMYoz3J5tgn5oWRG8WL8I-0uNXqslRjsx7hsMqXaWzaep9_0cpToR9VeInG6Su1hILDtD-0f79-xGzBTUqlDt0_h5OU5hE3h-arbFaGzZjkYA7ud0DlB4HBcGtFBzcj5kRwbhrDDMH_lMJBoXxlR_u_kbGfTVvHYZasZpmRa_03lKpB6N5UaXNozxIC0eQeHrxJ-l9kOd59NysN3imm59DvDJLj0Sg_w_eMmoqZTiC3ii32BZXFLryvFiMc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tsj_pz4mf5I21S9OsEOlyYu8t4Q388rXXnngmLXdjNeBPwCK14fY0H9Jj6XNKwKl1n-8v6sjJwT1X-lHgBIDj-JRuUIBvMr_Kkf5SPs0q8Jb5Tyt4l1RUCeItW-xV1GjURVvcDRSGo8T13ZlL-7OA1dgRDR1-RZ-5WYfqV_PSz1tl4vCgR1KSpFEtk7xmiOaJqq_9Tq07iBMst34QGFLcZT4YJJJDBD4VtVdBzz1QG4W1KrL9_popBvGwvj1Y3yvmhTdNJmDHriPOjaqwTjEo_jPMMSJRTCu-qk9x6O7yJdJrBhFQ8eeSfXhfbtrJGKpVVNYigO3EMfNuVovgkba9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDJxEyL9Kme2dZemRbtA7AFY6tgjqOt85fi9UBmtltMKUvjs-NlFTGqY6GwGSBRAUne4EBzAGIiBQxFQ5Xl3eGd773XhrN4gY_oDrs4k6dOhXkIlESKSgszISL9DoEeU_69r0AqM7VOSPp8wFNJhQAhX9uRQf3uJrnX2OC44n0G1rVAie8cPzBa9V5MaA0Y6mw4G4k2yUn7YnbbGBmWsdmxa5RTPFQtKmdyyQH_Zky_OW9N7tv4yKcF-Thvo6BEGRrL5tBdehEP70PsilaYDLaYDxYgx3XinyyRaU4yaVGkp96cYAh6WgKElusvSdYBsv_-sDfiVOKQl_kt9EIhhhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHoNyZYB9KDKkQmoIbz8y-jPbI_FJkkx0YVT-2IyKOlZgDg_p2JPT_6iZhj2m0LHVFP0tE--NqDt-4VvQzlcoiQOf6lo8gL8m1sfFBejvDfV7PbwaTFlOOXKsK6Gv-A2L9On2KDSWFVChGzhYgdjLas4b5ymUywsaNmpxYviU5GT57Ayj4Hq2vCeBY0Vx4gW3yEcHngZbvbtxMvl1t0cr-maDBDKJ59eFRW4STPglUC8rFFcxajyno3rjrwhA9kZRvGpg2ZpKWLtnv98fhYbjYnEgSc8a_Bp2jcxISlvZXXdEYRyKOaey0FPi3pnC7esE54MGPxq945x90px7gJJ_w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=KDjakT9ERpTbEP2WNjRa0HlEaJTSh6PMZtLajOiPDJd7lxgxUXuMZo7m2mdsdyNqr8ijSoFk0gu7LYy7yePeoato95YABfaWbKeppWEzdrwuturpnp2m77WLofygAZh6yr6zYqOibHceyFYAJkk5xJlu4b8idF-OHejVbLYUyte8_s93G0QIsvAwOKrK3wfr49MIKN1ti_2jjDS_UGdZYcqWOtjLzPzLT8pUkLJ18KvA8Nqk7AadluFIMav9thULVbufd1LdGCEPubEnxA7988H7cxNuA3ekIMkrJDfyfu7GSG8XluT14dhb_YcLa1lQtlXl7_KZ8oq1nCbwyytSwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=KDjakT9ERpTbEP2WNjRa0HlEaJTSh6PMZtLajOiPDJd7lxgxUXuMZo7m2mdsdyNqr8ijSoFk0gu7LYy7yePeoato95YABfaWbKeppWEzdrwuturpnp2m77WLofygAZh6yr6zYqOibHceyFYAJkk5xJlu4b8idF-OHejVbLYUyte8_s93G0QIsvAwOKrK3wfr49MIKN1ti_2jjDS_UGdZYcqWOtjLzPzLT8pUkLJ18KvA8Nqk7AadluFIMav9thULVbufd1LdGCEPubEnxA7988H7cxNuA3ekIMkrJDfyfu7GSG8XluT14dhb_YcLa1lQtlXl7_KZ8oq1nCbwyytSwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=gn0biTzky0WM_MeJldIGcFnM-2OMIzl2x8u6DCe5M4kd3L4a5y0cqCFkusO5t5UeqGLjGvToAHmvrBKM9KEcZS4InEcTNptj4lZurJcMHhrVmwHAj3PQuoSgCqiRv5t9YyCUwOiVUL7U461GDCuYgJXGCmyQQQ9FR5RzZiEa4-jjPh83FBYCnEESMKSNbZBIH7POlvWkCyEm9CoHm9LZPJs0u0qD4nPbNQZhbdJ6PK627QKoMDOTKtRCGZMBGTb95DWL_Gjciaqh2u5YHh_tbsAkdUBafMq16XSUbj8z2SBSb-DxAYRHRVnd3lnM0NZwIQ7HER4TP5GEuPYkvD05rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=gn0biTzky0WM_MeJldIGcFnM-2OMIzl2x8u6DCe5M4kd3L4a5y0cqCFkusO5t5UeqGLjGvToAHmvrBKM9KEcZS4InEcTNptj4lZurJcMHhrVmwHAj3PQuoSgCqiRv5t9YyCUwOiVUL7U461GDCuYgJXGCmyQQQ9FR5RzZiEa4-jjPh83FBYCnEESMKSNbZBIH7POlvWkCyEm9CoHm9LZPJs0u0qD4nPbNQZhbdJ6PK627QKoMDOTKtRCGZMBGTb95DWL_Gjciaqh2u5YHh_tbsAkdUBafMq16XSUbj8z2SBSb-DxAYRHRVnd3lnM0NZwIQ7HER4TP5GEuPYkvD05rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=L7dhRIMgTS4gENskZeKbs_nTuoAppSOGm1VKxF-TECEjMYzB13gdJyXqsXejjlyaW0PzU1gRPoWUM_9CHTPteB9_ND8vLIjnyol_pj1DlgmlLtgORb2zPnTcaPDu61elVQ5bk97PFcXPMuUoGv5juRUh-Utt1dKw9E_mvOBxVCuNFe89csJdK5q5NMt_GIa9qAv_t5M33TByrUjY3N2Jl6u5cLox4-DXolgiVGP4fB4TxJyJf2fKiYT4_MGu5JAbblXdgP1bwPWTl3uSOGIv_zLjVksKgRwn6gz4GoyOJ01foouFPEK9DX8uix-DS--Xk7XHb4Sctnr20S8MLBYGQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=L7dhRIMgTS4gENskZeKbs_nTuoAppSOGm1VKxF-TECEjMYzB13gdJyXqsXejjlyaW0PzU1gRPoWUM_9CHTPteB9_ND8vLIjnyol_pj1DlgmlLtgORb2zPnTcaPDu61elVQ5bk97PFcXPMuUoGv5juRUh-Utt1dKw9E_mvOBxVCuNFe89csJdK5q5NMt_GIa9qAv_t5M33TByrUjY3N2Jl6u5cLox4-DXolgiVGP4fB4TxJyJf2fKiYT4_MGu5JAbblXdgP1bwPWTl3uSOGIv_zLjVksKgRwn6gz4GoyOJ01foouFPEK9DX8uix-DS--Xk7XHb4Sctnr20S8MLBYGQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
