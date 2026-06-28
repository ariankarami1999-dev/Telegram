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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 01:25:17</div>
<hr>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP4vT26DbMfIlfgLMivVG7lutp701B9ejeapkLI0VrzVKU8LB7Rpp-MYYvHCktEgy4TwPnuSREmON4Wgqnpg6e94h0JY4LkYOnXPMN38jKz_2CxCvBFyMVUv5IqKYHIOzI_iupWrldaIQCXB6B3dJ_1nmo1ISta0JCFR6TuCeRLpsT2FxwY-Cs__7LdOwJPjdg5OhJo-vLfkb4KDFDmmR0c8r7vByxc-jJQ0sbH-anD6KNOyB0dAep2LXVaWTZQKuX5ov48GOGDHNaA5KTuY-9ndEiIVOpMPW7skJsiSszP25K61fdyg0ON5xH1NR0p3yNkRHfuewrO_X29ytGiHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=gq2Q_WO9_mgi1Erkiy4Rsna_MprBk6ZB3Z_v48ZMLrVoBE8jYKqCvofM1mG1e39jTStFu1jEYo11IVNqIN1yx90uIIF3Cz4LQbyN1rDTtpcFrZAzVCO6sKqwKuouwcCuK8NIKl_rtM_psTvCzgKYs-2yK8tx7L9rii4xfDd80acD5xMwUHlQVW4T7F0Zm36VVQvCbCcpMUCP0HU3AHWAkLQtvWfv0dr8u1GzIWGTMTCg-O0FBv5V-36Pei0jdTgqt60-1skkNGlNZkQmmEtnPEpMTwAFT2Ox25brySrPQlOyWooqNlodsfiMhwSKx-LHbkPxn4KY2R6HeUsg_tFMig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=gq2Q_WO9_mgi1Erkiy4Rsna_MprBk6ZB3Z_v48ZMLrVoBE8jYKqCvofM1mG1e39jTStFu1jEYo11IVNqIN1yx90uIIF3Cz4LQbyN1rDTtpcFrZAzVCO6sKqwKuouwcCuK8NIKl_rtM_psTvCzgKYs-2yK8tx7L9rii4xfDd80acD5xMwUHlQVW4T7F0Zm36VVQvCbCcpMUCP0HU3AHWAkLQtvWfv0dr8u1GzIWGTMTCg-O0FBv5V-36Pei0jdTgqt60-1skkNGlNZkQmmEtnPEpMTwAFT2Ox25brySrPQlOyWooqNlodsfiMhwSKx-LHbkPxn4KY2R6HeUsg_tFMig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9ipeTVJKoXVenduwuoVJWq6LyV7utuWfDNz1uI-nRSokeJRx3mx5bWRaVAF5QHFRjbpWBIACUze0zmKwGGpLykZBfCJw_AhlMjBcGmLvrhw0bF97tuUV-LP5Jmf-1lvFDhWb2LYR3ZbL8sp06VAb3MlH54D68y2_IbDy2CGDR7Rp3E11Ev04brXF2lK1urrVIRK2PM2am4-ZV2Imtxk8SHJoJz6Z3BlL2hnrnH9dltOucROrL3WRhUFZJ7NUmbRN5QU5sInnSEa7hIda7cmr4jftGIc25_RjydggypF7vU5rF0C0eZXmRNEq8FGlb1Ou6aggEn56BeD4awXtvTAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzu_btavXw3ZvXCs7ahJmIaW4OCkUBMHDw8qv1BRtXp2yK2flhKuDsxudSyXdnBwvU78UbEJ8mE6Ag7osXRXeVEyc5TEzY7d0LgONr1Cgk4DdxPrinua7QPiPXQvZvci_OXAvx9omeOA9I4-xW-i-cSdTdkFgi0U7BAaDRSYzhMYJX0l0cnQwYznshk9mUUneiHo1EQCOept0TvV1NG-rCG-Vnm5D4N6Z0h_yWqKQZzOM_ko6_0tZVAU93uSKbPVFypYSSBEoeb4kInopCHvT_6Dm911gR9Cn2HpaX1VJmnP7O-5mbdoAvhBjub9gf4thYmElvfZmulIpxfnqKwyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S56yRTLwDdAQo0PKqwgZPpYXcEbHZgVlM2eDQJKSR2dg2VZAxySB4PD8q1fHeCO45YaxsxgbVjeCnBVvPsb9556cG4bk0HSTQvTEukaH-wnhSl5NH9k9idwQiNoZSpm_KvbtH1SaoP1qs89dOA6ip4zZvM3QlgSkvweYRyuK6K1McjIHLiaj_W2RdBYqgUAclXRuE8omtycdp5wAPNftToh2p2S4lqh28A_DIFHGd-Lgeqit6y70E1huNJe1wje61O81zbVs1stY6swl-sY6NBClve65UFU4orkuc0XiakBjAmM2E-UicKJlZkqOw7kXkumqjP9iZYqeE-EmWK7d3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtuutK9b1lPmFFLZ25ZKJvaKPCjK9EU5LJzRh7GTdAMUEkQ9nrEENzNb3izELg9XuBfrPBlUnFbPHYMjeJJv659NunMtu-zgAXVefVZxNPEaCpEgOZUEsEwst1uxWYEPHjWPTwKuKbWQwhMTyIk-7SRPzQRAefxJzO_wMomtOb9cGYGBWpwu_G1B3_3HVo2bMSb2fD5gliiYygV45zNwuDmOGYhsgkNNyQYLcH77_ziA1KHqhvi34Xwp-qHag_Poispm0ILEfDnXkGhahgXmSbw8HPzHinlFA3uSJTKBJJMd1_fypiPanMwjzorZHh89wuTA-sOmxuq_G-cpEe6fNg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=O7AkuCtKavJu3Oudx0LjXq66f0k97gzQ8ghEJ5V-EZ8nQ-b2XaFwa8dDf5UY4vnC7GsKKKQ_BXx3-Rww8Iy2oYXiOn_m475qCbfiUGbPxkBpqaj5p0x53V0wEgEmZFga_h1j5HZQQFCT7SPIJSKtmbcqIWnVcXsxknEwgwrBsS5PJGhfA7d_elecHkSYsF2gBlgQeHKo27COanwbMJdT0-nWF4CWptzs4H42z0TtEv0TZN9TgXeC1a8DOxxewm3X3FAsL_HZnZs57D0YrXzpp6rIRltjJoWJJP-BQJwAzUyTc_sXPWAaDbmgl7mBvK8ZnEGUO1tOFITpQnBV9KAotqvLk97eUSrSjYcJhF0RtROT3zQxBVQe57JFiKcAdSnXe-YirnGSTV0kuNwijMj0Jddy0ZbJ5P0YSJVhAODayEhv0HOZHTnnlJW5byLcpmcax3H24zW6tP75NYAXcQZvbMs3jd4_-Wf0ns0dF2HgO3Qffh0F7mJ59ywRMYvg4cc0xJbia-TcBVJWCrOJ4-yHziYE6xdsEEJVHfgsWLl74yimjnIQtC4WDkkZxjc0C5DizJs2Hp_K8MFtIx-RAq8ruYQAzpf0p-_pmr0w5oR3aq2EPbyoLt2DieRUjZJeNuYox7Vufzivq16-0e5ozMDirG5ePPBKL41DMruDoSnLvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=O7AkuCtKavJu3Oudx0LjXq66f0k97gzQ8ghEJ5V-EZ8nQ-b2XaFwa8dDf5UY4vnC7GsKKKQ_BXx3-Rww8Iy2oYXiOn_m475qCbfiUGbPxkBpqaj5p0x53V0wEgEmZFga_h1j5HZQQFCT7SPIJSKtmbcqIWnVcXsxknEwgwrBsS5PJGhfA7d_elecHkSYsF2gBlgQeHKo27COanwbMJdT0-nWF4CWptzs4H42z0TtEv0TZN9TgXeC1a8DOxxewm3X3FAsL_HZnZs57D0YrXzpp6rIRltjJoWJJP-BQJwAzUyTc_sXPWAaDbmgl7mBvK8ZnEGUO1tOFITpQnBV9KAotqvLk97eUSrSjYcJhF0RtROT3zQxBVQe57JFiKcAdSnXe-YirnGSTV0kuNwijMj0Jddy0ZbJ5P0YSJVhAODayEhv0HOZHTnnlJW5byLcpmcax3H24zW6tP75NYAXcQZvbMs3jd4_-Wf0ns0dF2HgO3Qffh0F7mJ59ywRMYvg4cc0xJbia-TcBVJWCrOJ4-yHziYE6xdsEEJVHfgsWLl74yimjnIQtC4WDkkZxjc0C5DizJs2Hp_K8MFtIx-RAq8ruYQAzpf0p-_pmr0w5oR3aq2EPbyoLt2DieRUjZJeNuYox7Vufzivq16-0e5ozMDirG5ePPBKL41DMruDoSnLvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETkOqbNuMhM7588lM7RVnRGd61LRvnHywGdhBiQh634oW2Ia2NRY6LwveGtaSLkdtVOqQa6xX8pwulZdMI8N3Favi5HPXb-x3u0KHCGS36Ul51vMnLE4Y4rdGPYHJv1k2aGwLb-Z-tkV68EkZo05YDH1o8A6Psbcprx36pc74NAOBTnt04Tpmt9i477bXc6sLC5YoLFnXPp9W3kOO951rsD-No17p6Lk7aNF3kXjHs8J5jNxI103BEnZ5iP3bofPz08m7cJVB5SvO6pmbkykulaT_IDo0-3Qpz3kFGm2KIU7see1zSh9ijhzIX68887DulpC1lI7gIDSN6CrfkwW4WOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETkOqbNuMhM7588lM7RVnRGd61LRvnHywGdhBiQh634oW2Ia2NRY6LwveGtaSLkdtVOqQa6xX8pwulZdMI8N3Favi5HPXb-x3u0KHCGS36Ul51vMnLE4Y4rdGPYHJv1k2aGwLb-Z-tkV68EkZo05YDH1o8A6Psbcprx36pc74NAOBTnt04Tpmt9i477bXc6sLC5YoLFnXPp9W3kOO951rsD-No17p6Lk7aNF3kXjHs8J5jNxI103BEnZ5iP3bofPz08m7cJVB5SvO6pmbkykulaT_IDo0-3Qpz3kFGm2KIU7see1zSh9ijhzIX68887DulpC1lI7gIDSN6CrfkwW4WOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=eSV4TCXcWutNCpnDoOBBlR4jTbbz2O1dfRAFZgVmi_bKsbR7p0b6LD8aBlk4bY4z7nC9VQrcEGiG2rTWHK8D-rknYcMG3uOQVIpphj_vvP2kfLPP5KpE7udJ_5ceaLIfFAh-2e7H_sn5se0IgtpfSORLwHyqya0b4yzPVWZED5lO2ZFp3ikE8agYidOq6oJzf2YRiHsVjEEaq72lC82stzMABHhnQAB38PLQQ3rIWi1o0BawfaH09C2cQDIZO2tFRu43oFRPlsgjrdD30XgFhUoxsnmGzPaqOonSQKvh79fMQfot-QsjZCHI5sSa6mMdpDsnYvgb62Uio1YyVkp8DYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=eSV4TCXcWutNCpnDoOBBlR4jTbbz2O1dfRAFZgVmi_bKsbR7p0b6LD8aBlk4bY4z7nC9VQrcEGiG2rTWHK8D-rknYcMG3uOQVIpphj_vvP2kfLPP5KpE7udJ_5ceaLIfFAh-2e7H_sn5se0IgtpfSORLwHyqya0b4yzPVWZED5lO2ZFp3ikE8agYidOq6oJzf2YRiHsVjEEaq72lC82stzMABHhnQAB38PLQQ3rIWi1o0BawfaH09C2cQDIZO2tFRu43oFRPlsgjrdD30XgFhUoxsnmGzPaqOonSQKvh79fMQfot-QsjZCHI5sSa6mMdpDsnYvgb62Uio1YyVkp8DYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlpBmTslPWMGrF0HjjmzEIEoVX7GenO0YKtlO0fgXjiom3pLW6wDEqR7VKkgSWD868FKgpwGNVygiHwFM383SvTCqaQL58YrmfV2pBzmT0Lrvhd_31Jg-Zdibl-fh9_43X2lU00uWm8EchVSoFWacYpl_u7WBi5uFKQ9plyWe9cxR-fNnDU5T3mzya8BDYcFjU8L0N8ELVVmc-Jh13S4PKMbGWp7J0sP-pOvlSWjBlQZ3rm24vgH9XW1bNe9DUagjfYSnN0Jm6b2WpZpmy7uuH5ELgOoZE-WfC2T5qckVAP2x2i0N7MXfC7a5NWlSIv6vDSX8Qi3JPJaTiWRZZaVPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS-tyhtQUh6EpEFlazRWoXKhDO_NPW-t6oBIeDp_FoGprupccfwbMpit6_ZhAQQqeKDrK-z_sJg-UbkgTUeBd9LWvAueFS_XWmb3rmpwSntJXxi9-YA4WVTsnuhA8VB5q7wLnxl3iGstnmb6IOKT5MsvZRgWgZjax1BzG0x3zfDy4z4QFnfHVxGpwdQuiNIR2_5cmpoYWyOFM7cOkp1JYQZM4AeLqbYxqCS38MjkAyYWEoVTMT7dVZ9sGEsN2J9ZL_bi7vRTXTZWnEYxzQMPuc-bdKRe4jS6O1ANEewnc3uI1Db6GhSd80DOUdvG5ML6OKijY7EmBx9WSWI4LbYhVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btKcdAuNBWrLujwQOYgokVQYvpQCQDfkGTmKUlVo3ZMQzkk-1aM_--JDfu-HrFDsYxhjkUPeT8AwNmxbMsRbhWG8zdRGPmt4a4wm4EM-jPbgkWMPtgi4QczFouMyPPMqU9N2SITFa-M7W-14-FemcNgM1HMld3UXmgYuBGnS4YOfKj7yEA0GZgw1Qc-76EeBmVGBMOFwjpe3tuTQ4GL6fdYcchSAiHAlZBq1bvQcDAStMoIvErSIDYO5Na_UufSaMOOtI3Gm-goauiZfgZ5_wsAjhL1vAK8LsX65johoSYInL3rfK3Humymg8zNPWS-5igbBmTvlmOwHtq6KODNA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXLoou1CpYPs5VNi_zfL-qgdTIPINGWPRe3FR8-gBdVy2kcfTw4YTT3mWLEi_FY2ioOUfn0D8iYYOMPhjdpwJ1HwFheRP6U0lYQm3PSpy8n0bdZPYqStgCR7KpgFZ25TKDQ1l67kYF8l40HpjJGjjW--77PHvjn_A88R2DCvFRXxO-P7rkYmHis08ofCy1H6jecoZninJQykwo25Wfro10AoWC6yjby0D-aIzz8KlgMNczq3JMpZuwGQrlzmO6FpkegwH0p7nOOp88jsu0zguLBxj7kfTQAyLNcKgbSkhfOPPj84F_Zj1dBtbUzg-Rs67JC4ocVt8an7s8RkNeFV-w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Kagibj6Q3Y1WbH1FhFUqaHLcS9mogU8Uur-bqgTtGSJ6MNLRTDrpdIT9f6ilhJv40w0AbIJ72zSDf0ugzUShWBOaeKSKQbK7O6-Innk61-K2TKkBw0QF0uoUO8jDRn80G4ZCXFHL-xFiVIz_ddfhxj2JAF47GS1Y_TRy1UN7pO7c8meEC90Ca58RHp5pU6At8pKJ3yUEF7dtX670crdKb7WddOTIOunVMHLE0tUD1zvjnAs1Ta2WCMSh1Dj968larYbBJevitNla7rHyTJ0KtQRCbo8AO2mrvf7ptUnCvk39Heo5FwDB2xIQfuFkIZwf5wL9DlEVsUty8zrs2ZpIxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Kagibj6Q3Y1WbH1FhFUqaHLcS9mogU8Uur-bqgTtGSJ6MNLRTDrpdIT9f6ilhJv40w0AbIJ72zSDf0ugzUShWBOaeKSKQbK7O6-Innk61-K2TKkBw0QF0uoUO8jDRn80G4ZCXFHL-xFiVIz_ddfhxj2JAF47GS1Y_TRy1UN7pO7c8meEC90Ca58RHp5pU6At8pKJ3yUEF7dtX670crdKb7WddOTIOunVMHLE0tUD1zvjnAs1Ta2WCMSh1Dj968larYbBJevitNla7rHyTJ0KtQRCbo8AO2mrvf7ptUnCvk39Heo5FwDB2xIQfuFkIZwf5wL9DlEVsUty8zrs2ZpIxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=lF_YoYz3-KlfhrK95oRi9Jc6WSNyOp6y04AHRMb1HWhQbkGSZ7-pkzak3gsvGrGiq6drFZv0ON9kmGJtENj97bS_FrG44D86UpYJHnhoHwWKQwbA5sxAJr3SL6IsbRtx-ZcCyapXSOds45v0vAwCYdUCP9aNyONHeNhNSoE1zej2vFxk6EediEq3Itkj-Kc2CesDogx8wXJFMiEzWqJesVmEh8wXnpRScXMhqG-Q7CyjlKN8xitsGxNAfmTwn_2zb7-npKpTA4sEOAERddHDRJ75Kcmu9EP605D0yoz2K9Ga6K8VtyzU61DaxrIWF_XnMO13OVGMK8zQ8iMFrntuZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=lF_YoYz3-KlfhrK95oRi9Jc6WSNyOp6y04AHRMb1HWhQbkGSZ7-pkzak3gsvGrGiq6drFZv0ON9kmGJtENj97bS_FrG44D86UpYJHnhoHwWKQwbA5sxAJr3SL6IsbRtx-ZcCyapXSOds45v0vAwCYdUCP9aNyONHeNhNSoE1zej2vFxk6EediEq3Itkj-Kc2CesDogx8wXJFMiEzWqJesVmEh8wXnpRScXMhqG-Q7CyjlKN8xitsGxNAfmTwn_2zb7-npKpTA4sEOAERddHDRJ75Kcmu9EP605D0yoz2K9Ga6K8VtyzU61DaxrIWF_XnMO13OVGMK8zQ8iMFrntuZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPUsPVEH67cnKS7dUbShaCUkvFu7VKTtMRp3Nl7FR-t-G-UNEGONmJRdzmCGlIbav6G8nKKhjXiWnhb7quDWdsx1hlhvFS7G_quk8jSTkSGmgq3Y-IsCcKdHsMIgYjm_O43xH0No2nyAyiPuOC7Pce8RXMhfrUgnMfztfnzmHry-SWt5PnZgflFWr0X9rQyCCpR82TLSpaKu_5jc3ul7pOseZc3qAKZS-r3Vk1IuC2pRXbuJvUDDm982OOPx6ONdCoH87XvQ1W-tPQIIkImvhPJihZ0K9OToVDf-Urh80AN5h8lE7Nq9c29l0QAWHTfHD-N_0dJ5V9aLF6sPUsBgfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP1OUt76u8IPmeRC3e2xsiZW302_whEPnDY5Fw_LPhL7NjDZBpIgctUf3WQcmVdPbnthDZG7WTEHCdhppNRZunxKEAWENAYelgErnystUmIrRFHUXyYDs_gD09WQDcMmL5QNU7QBpv-8KrcLCPyt0Oc2tqJL-_n-GwoXcBoV9wo6Sq5Ne8d9TFI2HK6Ib_kha-Zamm5i5ERtv12qoVsGIxwJianQHPpyEqr2fQXKWvy7MPE06iEt_4t9sBAgm0E-pNEYTQHGnt4_mQtyg8k5QDjWody5x0jTHmaqI9s2Xxj3AntJ2i6auUBz0-zTEaFcswpOZLi5CEyugrTaOGX2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=BpOCby6GfhFszZt6TBTElf359rjrMJ-WDjIHYfkx3P0MyCdroWad9YxZtiCvBdjsXCawwYZNGh9WHp5em7PG8XqBujrnkKaKWEted1OwQLDHmeBHHvXXfMRV-RdDhyTCBNZyhFvWYA2UiN99HuAcNoJruSTWgpNpCtayeZuq-tkPV0EIwYW3fu2cb6rRaSOcVQyYLrf5ekmPuCZahIShZtD7-eRsdS6EjeN8SD_3V8CAdlyS0pL0RJrrtkJ42V1erVrbvd_3tuxdFPsQeB0MmR7hqqUVMwq3I8go7HDS52K2_iTB2rTcasl62C1OFwFmlhAoJiW_WdSTzyVWwUBtxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=BpOCby6GfhFszZt6TBTElf359rjrMJ-WDjIHYfkx3P0MyCdroWad9YxZtiCvBdjsXCawwYZNGh9WHp5em7PG8XqBujrnkKaKWEted1OwQLDHmeBHHvXXfMRV-RdDhyTCBNZyhFvWYA2UiN99HuAcNoJruSTWgpNpCtayeZuq-tkPV0EIwYW3fu2cb6rRaSOcVQyYLrf5ekmPuCZahIShZtD7-eRsdS6EjeN8SD_3V8CAdlyS0pL0RJrrtkJ42V1erVrbvd_3tuxdFPsQeB0MmR7hqqUVMwq3I8go7HDS52K2_iTB2rTcasl62C1OFwFmlhAoJiW_WdSTzyVWwUBtxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=NLtPaYNd34uS_eAiuKWHjWOjrijPSp7fL9JdKj-UThuJnp3nahrVlnWGPPWefwXPLGvkwpWEOkgjEWGSQ8IlleEyu29IQQlzDRrfcx8tZJWkCRLFswl4s5KbP98paHLZJdPjNaq1hU66-n9NS7Dv9ZQzYQg9WsWKZ5Ly9Kcxt1J8NxFujnKyIZJYr2ICm4BoMshaUQcic2CdxrLBq2VyKUJRvxhfnulDYxyDCzxn1z0vfRmY4tuGBJzi6mvILY4_Sa9ZmOhf0T3I72rfV2UZENu5XHFcV8IXGL4LkkD0lxkoSKnCB9i3lxWzRJqOPC_0uACbb9Fs_VtX3ekPJYBHhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=NLtPaYNd34uS_eAiuKWHjWOjrijPSp7fL9JdKj-UThuJnp3nahrVlnWGPPWefwXPLGvkwpWEOkgjEWGSQ8IlleEyu29IQQlzDRrfcx8tZJWkCRLFswl4s5KbP98paHLZJdPjNaq1hU66-n9NS7Dv9ZQzYQg9WsWKZ5Ly9Kcxt1J8NxFujnKyIZJYr2ICm4BoMshaUQcic2CdxrLBq2VyKUJRvxhfnulDYxyDCzxn1z0vfRmY4tuGBJzi6mvILY4_Sa9ZmOhf0T3I72rfV2UZENu5XHFcV8IXGL4LkkD0lxkoSKnCB9i3lxWzRJqOPC_0uACbb9Fs_VtX3ekPJYBHhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsLKHQ21nXYlJWosdKRpS-9TB1FZR9wFDgSskK0r9MwNrcHmmiLxRDxwkV85i__XsmPpWhPIS17IbZvabL5bCoWnYGVkaRCqFZ0TBa6pAIfH7uaZA37HX092RBI3woGbYjQTWgoirSLs8YIDUfBaFwFxinzjlaV28VsPbe_ROTjuFsytDD4gjGwpu6MIAMpCBAXVSdkWdqfXMBCbRkCqS-i3XlLOr-U-ADDpsHDKDu1SOPIxyT1FoVfIdl4VXjDuj21aWTEv5caEPPeWqEKHqPO3QuL5ubk5yZhb7wUHjPQYkH4ZzhCbqWAX8ldGPgEyg70i6ifkCRpBApO0j65pZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3Q5q32ypmxyJD8nMovkNfh1nDSmB7h8yoWNr1bJylr1fO1OJeJa2GCMZr2Vosu3zdDt3Q11GOk8Ko2Hq3GLZu4VWOuw0gAN919wzifkhywXOemRJS99Y2ioj4wF2R7RWkyyJ3zhOESVJJyBVIYwGXNPuerP9OTZe1xHTrcR2wa-xMnqnz5r5VRKTvLhzGxbAcbuxVwce264D3e1GjKeFuZ6oGWyKGn8czyvntzd4vwnY5FdqNYPe7DWKP7yMqATFW0kdSuSHfvkMvYRsc3tx39gfXgPe-fGRn0AohjNd-OGNQ6EAvgvT05FzTuHnHC8qd2vCwxObBy8mU8i-qdV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvhKhlaBOJIecLs2MHqlvebwyJUCCuSGaAA4xS6J6LFZzt_6U2CQz-U2a6iVpSkhvXM8KSb4RGxZ7XtuuCZpqbWQMN3g6yFVsgwO2Q3DIyw5eQ0tK0GGjoW1taF_ietXXnl3_HBGLvcv9cIIVwQ30umwV92Llt-MmJasrl3jEyx7LAXyOgRYboMzzK-fUrBXLnjSQlanqrho4ZrLuHZom9n2IJJGibzUpYOSVv0jSNrBPnAokJ15sS1vmkkxzCdAamemPzbts8gi_ui3CKO8SVprUwcr-BV997u8Z03oyQMxUO1Aw4T7dH_TkJQkr3cQWEispVfMIXwB8FxPGD3GZg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=mea3Db64sTCnEG8DoZgExOtaf_jOcPGUb6CIkqAmpQ497Bv0mF_wgX-lUukjrazAip-yEmHOL42-IXOM5PsF9UHBi119grBE4yPP48P52Qkx6mlNuouoKDakTYzL3ogdqsn8dmqS8_U7g8YZWnv4Kfio02UuTzS1TZvT2Cd5ttfPIr_wbLfdJOAQbsKsObjmJiOCPMMtx7s4to1c0s-U0mb0iGQVVfmVf5_4VxS68ryHIkrlDrYpnhME3-6Cr1SNdoKajs3QOuySlyAf_xspeBcNi6u-jxJeWyhlw8K_voGlTmyW2grGuSK4hsMHhfoyYPjsTFxVU_8HdwzAzUbQxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=mea3Db64sTCnEG8DoZgExOtaf_jOcPGUb6CIkqAmpQ497Bv0mF_wgX-lUukjrazAip-yEmHOL42-IXOM5PsF9UHBi119grBE4yPP48P52Qkx6mlNuouoKDakTYzL3ogdqsn8dmqS8_U7g8YZWnv4Kfio02UuTzS1TZvT2Cd5ttfPIr_wbLfdJOAQbsKsObjmJiOCPMMtx7s4to1c0s-U0mb0iGQVVfmVf5_4VxS68ryHIkrlDrYpnhME3-6Cr1SNdoKajs3QOuySlyAf_xspeBcNi6u-jxJeWyhlw8K_voGlTmyW2grGuSK4hsMHhfoyYPjsTFxVU_8HdwzAzUbQxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBSbVnYpNiNbtjdUdINoEMrq-naDk4Yo336NbcOr_dpeGJTQJABLf4uGETDzczh5sOxIOyCLLayr1aeXcEVx6l4A1QfI11_KdveaVf1vwftaNkV7_vJS87pG7uSWwV1W9zOH1Em5GedvjO-_EAK6Mo1v7I6vsL4g-O8jEd_sHV8-apeyOKVq6d2ZNFaK568LDBn-CjHmVFDs3WagxX08__M815X6tQq1Pgc-vf7C2xA-hy_XkGb_zpW_rMv9vt_jD8PNC-p3AG7nk9F2ksvtx6JliJ5yvkaEO2sBGoicRPs6JnQl0Tgx-0hAfVYUS51DKUrirBrTSqX5zUO4UFS-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo6DOAcHEb7iWiX_MiJBaXqOUg2vFl2NBpRelMRypHhiaj-62rNSAc47teqPe1vp5JWybEw9CFL9RQsxvNcUCWmAt1jvowGjWoP93MFYayNvfVdg_hJPkv-cbrc1T7aWG2LGbmxC87Wh155-0H0ASNv7dkGDIqRl4EUx54XydFjGZvTCRZSy_rHneOkUTimTxUwq1otS4ykhg67221RPYE-jI91K2dOHH_wEGlPFbWITm-YgHeW6D3oaBHxI1UmBCm2pgUbsmDWE_wL6C2Gt9d_fEnB3NDzgzDNIE9lEHMDcDwszrmYJ0Ur8ZWsc22IAPyDZ3dnzhdJf-SNoX3B9nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8v0V8q3dKJh2TOl8PX6dmiJtm99BHYRrmXKnNB7QB8Vl4-NDFZGWVXM8H5UI_EUPEgK_MZBrKQTG5ipxPuK4Vld9VSh2avZdmN19Ty_D_O_gl1yXt7A9KcF8sCI0GWooi0QiBrCL8ZSB_uiTE-7q7jyrhjxcOqlzzQdq57_gN_ebSSDFbzvJHcPlE4ui8XVnuDzT-vNs3fsnXmdapZUfudxkXqAfdkyBWZgnOdWNhwU32zTihqd680J_Rpa_IO0ZB71tw4ckmswl9gDy5II5YHza4OAtodW_F77sINt3GJC0i04oJY6FAYW0jTjphcxyM1uD7389g-Ku2oJptbtDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=sRv3uKt3P6Yh5zkTqyrw0fg3c6Mbq1ULRv71OKfCCD2vTxnxJjIQyWXaUzC9HUTv6ncfV-kPISPa_Rg1qpkdEm5ZdJBZoud7Sh1sAeO7VuctDjs5LuN6frUNNSx6SytSsXnBFF4w4jojZs5QOluku5QVMC1DyTcfMCRy9WEBc3AOeoGUAL9aTYjGR1Amp1_n3aFJtEO0PaOF-qjiKCK417Sc8Hz3xYQYMuA4M1q1a8LsC2YJGtLYjaseHrmW03cEku1L7ZVRGZNNveulHVqdvI3mBxq_EGeHyB6cM9_AriqV_Ybz6Sxw0iTlXkTvMZEmHCnp1teaMHbDzy_V1swkSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=sRv3uKt3P6Yh5zkTqyrw0fg3c6Mbq1ULRv71OKfCCD2vTxnxJjIQyWXaUzC9HUTv6ncfV-kPISPa_Rg1qpkdEm5ZdJBZoud7Sh1sAeO7VuctDjs5LuN6frUNNSx6SytSsXnBFF4w4jojZs5QOluku5QVMC1DyTcfMCRy9WEBc3AOeoGUAL9aTYjGR1Amp1_n3aFJtEO0PaOF-qjiKCK417Sc8Hz3xYQYMuA4M1q1a8LsC2YJGtLYjaseHrmW03cEku1L7ZVRGZNNveulHVqdvI3mBxq_EGeHyB6cM9_AriqV_Ybz6Sxw0iTlXkTvMZEmHCnp1teaMHbDzy_V1swkSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwz9Ud9dfUzqMUAfRg6hsUFhXmMbAiYRxppAz9bfG7ycu-Oa74NmFiXYGWj2Slha8S_-pBsz_6LZnleXtWUF4E3v9YicH969yS7onDdJAM6EvoWzcmRd-K4F-zOkWVJVZcsO4wfWp2N77xng0Ga7KTWFgglA_o6w8seUZ7zXxVnf9glPzI70-6MTzmooSwztG0zgplgF7_SkaybtTz8KhQyXmjpAUfRhLU0mx3Ed4S3w3czgL5_cQaoZlGEIn22UQPjfi9On60fH9RrLwM0JW02s-X_JZ5ajOr-PyfR73CDxeYmupj2heOEChIqirbHmdV81tiJZ5Q2q45vVcutAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz0x6rOVFVjkRsXtPukojtm0BLHmUkONivetO20O3jJiRqUDD2YWV5yO09VFLZuBHB5qDKVZyUGrrs9SrnO-CUInPFMBedZEtt8KUkpF8h7di_dofCMPmQ3ciBUjvhMxSczNxGj--4sdWeRRpe3KeyYpdNHshSEfRQAmewe6cyqiTaO1xFxuVNwNBnp-goxyWOnYx6bd5S-8RMOtf5LOsNi1jMNXguMfiHgeD4T4RfE9cF3GFDnxiP7qH2lNLWJ9HvjkPx-B5gmvxvGgiMdMYYlgFOZ2z1wUKSM8lAa28djP204sudwUB8jKV7rcbF42EKVETp1WcIJKnGoCgF81cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoEUfZGhd29tlsh6x_UCdR5qjoS2GN3QvwBVgXj_Yx5HDyf4jxz58xtxs_S9IHufkPprX90XuNtSakE8ZaemBPudVBiKC3kW_QFnZlOs8a8Uazwsm_HFR-Vjnj485cWi34FtLPmlcVQ68c8cY4lqEKrI60QBrqpknD-GjKb94Y-PoZnOP3LBlH3FLJJU2Wu7p29gUa8juCfNBFPelUQrMaTm-a-mE-iqCo_aeiaV2VFCglWgFLCrSKFr3V86rS8JFkhI8Rttzi1EIkgp9SiXt_AWByOqRf-bpwtokpWCApZSrVuxgE_csWEw0pQi78QUGin7b06l1ouAah6mUMGOLA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=GGUr5dzuhYU6qpnNUYuWnOF95gRnrp_WiczbEVMT8wplh7HvzEAvAhOaZi5NCl1K9vgGshZ4s5Y4T0PySeE1Cqce0AWTpD4wvh57iryv5UQwX7vOiTO9OFhXr3gy-tIobs3gbcEY5H6NZds-UuP9Cw6nb_LrWfXc6UDHTvHg6PM1nC5ao3p0lk7KI1-sop0l7-V8kIGEYj63PTuQApU1lzGoZNabO6tDeN-wqouy737DhnMh8WEV4TE-WCjNMRk9TnwN1zjKp4PQbOPSkiB4mLHQwhiQZxwTx4dWvMTTIWcXQ5H60Xut0TlXvNMPavqOoTPCIVkXVgaOjxOKoibFPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=GGUr5dzuhYU6qpnNUYuWnOF95gRnrp_WiczbEVMT8wplh7HvzEAvAhOaZi5NCl1K9vgGshZ4s5Y4T0PySeE1Cqce0AWTpD4wvh57iryv5UQwX7vOiTO9OFhXr3gy-tIobs3gbcEY5H6NZds-UuP9Cw6nb_LrWfXc6UDHTvHg6PM1nC5ao3p0lk7KI1-sop0l7-V8kIGEYj63PTuQApU1lzGoZNabO6tDeN-wqouy737DhnMh8WEV4TE-WCjNMRk9TnwN1zjKp4PQbOPSkiB4mLHQwhiQZxwTx4dWvMTTIWcXQ5H60Xut0TlXvNMPavqOoTPCIVkXVgaOjxOKoibFPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTjzazfEoVY4NriNq60YCUENFjjIxJ3kKs9sYZYkSe6fuO6rJzvBCpGUhDU1BzMXv3c7NSNBFogY0dss5sGF_JkPTHS8qKhxuxx1OuKIjtmtC4ivDT6Ufcl9YMEL5trnnu_wQ_f8N5iWpxncONo4Euuo08ZFySqLClynqylPER2ty8pvPXky5ZVi2h6ejmh9yU5AsO5ZcwpEVbtYjkEqVYJvcHXNsSl89TvhgMH_5Q4WaKJ1gWGr4MKjaiK07CuVBG1j_LuGpPyUy7xkR6w9L-6POoyy2JFrW6t8XXFeC7A6B_34y0c0esrLPew2kto-OC2MEbJJ-XBqhwfeQrvgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeYqeJwgKrHJEhxpUd9kK1F9Jj2xRPTITal3Ho6dia_fyxdTfk-mTzumVbMUU3-LIEw7S43Nr99zS7rdQmvFHgz1iDV-HvYLVR-Xktatq6Kz-cAM9-_drbYLq1TvSEWoh7PCnNk7hpXZtluxSKFPHd2eM6a-XRNi9zL6NQ8BAPZWR---8U5jz0kcpl-1nDq8MSz-7q8UATcBBxvW4etZ6b4-Yqr2WDemOaA8x7Vx7efpBF6w1Ag9Mh5gv75DehfQPUbTvGnwlb_q5DrLs8ql0ylR0a0RasQtw-lX0xlwuXdU2nFB4xN1MT_6__R91tEt_Kros85W8LlcrNadRhbXDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qseCPqJXFcCDSNwoTqB34yrx-TE8oDmBxZBzbxu5yaLS9f0x5cuaLlSLHT_wIcGGtBsXxXnO8q_gwjvKN-YohmmF6vNobKnw_OjTkPghK8j1uqhBvfkRNjgLp-c4pjQr8U3Kn55uckPTR_JvtFl5guBLl35_JWko0mqH7Y6uRCUXF49zzBcjI4eJtuVdCiHt704h-V-Ibby8qinLyNITsIeYGHyG1gKLVS4uPIXN67wsk9elC-PXLo4qAfW_3uHfr4A5S7AZ7VFced2WfhvMvp_Y9dgqjEwxsKswoO1t3KHXlND5NEgOoun2A0Hbvq4lFaSHbVmU7CV1N0oh-QrvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjLcUFDYPGa1lEECcvdgkmJAHcRiiJDIZ4XcL6UqJ1XK8qxfvBKdtTVs4rfL515u_tGboggWZQDVI67zmdz2kvOvrgF6pgzqYZ1l9PIKXgHE5JXlQRhdIKq4F-cXmPbtwcvQ91LA0rKen1w6VOh70vWse1FdNhp0uLS0k52HfcK38-YZgdZ8wKdYg4dK_QJWlMh9G4XLoS8hT5k4PLqJ1uEalO2ePjyo3b_QHaBeEEq-XoHxWcwQS5d-Xis4Vb6T_r955pSqP6SNTbWPo7wvhJJaEVidDmTyS5B024kia-bLDUfN2_oRenadGgMRtGz8fQ2snl_df1AcxnQCVb5CFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaPlThZuFEZZ5EklaqnpuMDXEf8ACNfb_nmfqlUV-QAyhllKu9-yW_8XNRIBiYlEvrn0WdWN-LsLfNNOsBYX08Ay66_XMwoGcPecToXHQF8xzKksghBWIYYeEcRxKnF0PeBo-0NSHagRBUnjbpo2cd3MhiMx0cbyZg34ymo3lYqqtmk2wM1AzeDQNNkbi-3s6L0yLWxaZcgIEoaAXfOrM1ZbpoGkpbtgPgBbbClFTVtuMx1pxDA3TiSTb5qJ_zqC7YHMYRveFLwQJczvS6XUAJMOeNW1btaDMarBrIocK1oR4OSu0mNhbWlNuezUVLOblZoE46B80WvtAUlljAhb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChiYaDFVF-7fYXvSWcj43XawNr2kzoXLztDXV_cCYpxgd1SVO0iy42XCGX-DVejHFbGdR3on6g3E0gqaDAbjVpf7Y4sPA3IneE3JieNZBa7aBfzyNKeIEwOTrYfP8SIIXyHQevDD3ifKOuXcAvOtjkwatMiaYiGh_iOhs3XnCc94Tl4svI1gHHe9oH0l-LYIn99j_kTEhLv0Q9yYFBW5JSPPbnoqfmd9EIEhVHOOxDllImCc6QzhHIdyqMJ8PZPpmHdLqqvKi2KKngf9L8m5Td_4-y-aZgwMTGCpzHQHxGHeMLJD5pIwd84YKjEjCO-3-cEAwZqJGbQlOx1fWoVAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JzzRcWhR5R3m4pTl8KzsOYIv9-K651d845P8KUw-3UusDyXOrsm_ECre4qdv6Xe6jWIFVrhiPzDhTwgkDXq-8AQHIJDb7722BmIpRJwv7Lo7ziabsHU-m5ajyDNKuf5YDh8neSND4YH3ElGqetQKQdJgAKnInDOzfXG7iTqglEDXwT-m3XhNrbmGLpxteHnuou5lWEoY14TDWCP4ZLqcqoywgskjAtmsTz5ymkmdD8EjLQ5VPumkhnnQqw1BSE-zqHYDYqLk9htfLZU1wAa0NDcgMSHqHAjIPuDX2tw-O8O_OCc4UdFoOjDrkg5pIKV1-Io2452LfwmUkcfwwAYOPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj2AK6iLT5emvuM7b7egmAsq3-bSkgyUZPMp3j3tzNJbHC_QbXVk02iJE934ibw0iQZGoKB6dIKPKmV1875sCxwSKoHlpmlBZjFZUWezXJ3nXTyiJFapOjLqxeNerK9XjqAq_P6o8RsSu9_112NVNg4LnJFxi_l6ao8K5nlKTrrNlODVx7yW6_VPltPyERwU4qsWA51okdvrpgEa4C53hwJge5SFV0LVNQT7M7-OznHRCPwEKFsGPzAuAWWXtk00uqtCEIHsSz2OVIfBdcaJdlrW8fiEfj4KVY_fBsIZcD_ewy3qPNa7mTPrjtpDINSx53fLGqZaNnRJhYCFdbDwLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6Qa7SX_0xKPH0NvYsqwG0jqTingk44MxnJujSnD4zKM1O-wnK75pDG47F-YD_IYit1kTJ4IAhVMZigFLGL1pJ5sTTTb11cA3IfqeM21GzdId7IArWvjFam87nNsnYeBuqzEYBvA56pOezELUyS0JH1E6Z1bH0qQ_mqoxj64K-XLGabvNx2oGXxGX6Doopw1sT-nRCaFFsIrPrqSrcw0DhfDYUNsDVjV7vuBa6KC8tIA8023JkBuN-myRglz8olGxmbuG3dcwu0qU_HaNVRfSL4WQcX3deW1g-pJM7rZkMtuqI3vLuaiIqu9JEf2vzYGpNU4aXWg2nERexk5H-mp1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igpnhuMXxhWF9UeWV24YLlki01ltQEyvDnhxEgFuPfcZhjyqLSPPbceeWa8hOBUXNRgVjpCzhsDiqgAjY3TVe2fB-skW_bjAS5GrB3m3fpy2SbcKJI0KDMGl_3SST08X0Y0frKSl6nSF3nLAa6-X48mQxFgVbkSYeRqlP4LJDjhr0j085l5pPB-HPdlodU_PglysDZg6Aki-8MQ9rr-tz-YbPXhKZywhyinE8g3V0LQ_rPDNiuynIOMNl8EJWp2K6fbWBzu1fAj3riqZN5OgSSE0yRvP_JLU3QAkh8ZSm6vAoEBfaOCIZqh0u84SE9xoIeSHRGFNzJWeZmPA_yf3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pds48X7_O1bCMbANM8tn8CesVOl-jjtoOkMHzW2q7yuhHJQc-KdwUa_mfpNmAveErlozKn1MKxQES7tyzo7u7FlZ7Ti_-sjJo6-d34-W1J5Ksy-bYBKlV_SWg_7Z7TXoNF47Pi8TpGurlQ7EGEHpLtPqGVlOip8Oj7KdDwtshgbfcJgHoWWqGhzDX4EwuVYTyg809qPEsi3YGoQj10USzFFraUm9w4-T3hyeFzbKg8pxtNMRlOIWY_pCUWVIoI8B3aHATw4mNZ_ytox6Ykhtfk_auognAOWCQOZBCUW_bWvc3ovYt4Y6ajTNK4wiSrBSOaHL2Ub8YhbAuJ0NcYTZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2nIbXamAnoWFpYKbu3g_sohsaMiStakxhvXBXUg9jTegp0vYJ02lk6iDnff_avdqMAF_y3C7ReUepxzKe6ParUrxktgmeLjRB8iuMI_QavCdkMFnczqL3XTsQseGvgLfiBa54OzZDFz0KNRaAK4yq3bzCij3W6TTqXZwFpm1eXDTaQ2XxbMqHuY8fcjaSz2_ouu9scSQNsVcRu-n9rzUsZvvD_y-IhhaVIs8hrIIXLqqj5UbEIne0o7X2LCv5ZMlVUDyqSBQHKfTr0MWwSRprkopOHlHYvzU4vShRqamS9Rr90znmiOYCMQHeY0Yzzt8CXxpuNb4h-AHLcW-TeiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7oaUxQKUMKmZwtktNz2Wbspu5iV_lf0Vi5DhoubvMMY2piF62Tquy0w0CJ9c5TrT_9bKqOX3-FEGAHAAFEswRO-4eH8Yt-1f1z6Ebxrk43iYLwsV1vNvexYooexzk2s90bPqMwdIZ5t79cF9CJHTPZ6vJ98bqZu-fImG8z7UdeDvyjLKWhZybJjiLlwXXc3_Hrh9mfR3_nZXLA70knfC8qMtsJL6W7qdTM5jl73l0TPuSzNMvqvfy8EEKfP-Ylf5j7cP1SmZo5uGMdtIhCDOyWuUJK_dL2b0AMO4NiMDpE16-yPF04j2dKVy62blLZSzjirUiGTMyth7VhRwYR2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkDjqA20rE3UOnm7GXPVwuUxX0hvkMqzfckEn-AYq-NHeZzUIXunXS1KfqvGXgRpt67t12U2ffwZ3ZACmEPc2i6GzQkj0Gp80A3PnHR8UXhL2EUgEhQ0vuXc3hcN1qZ0z-nsbPUjGeHPkYVrKnuityN7_E-uxv7aAP2ySJVZP7uXO5MGwfcIGrFDiTcFgFqvF3Zay1gdYw8Xskyx5uo7g9MNiX765Ohiy05s8KhZYgTIsYvKhJS1XyU9LVG5RMNzhSrvrt3UCIF_yWn51sFC95RGmy5UzqAybd6kcYwQZiGANghv6hWidToOFepWypN_b5CW226CgS6HSxWH6ERJNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X973Baesp6O_tJ45t1uJIzWJlk-p6eCGW1RXQkXYP4SyG78-i-eI7RD4JgSI_OeXvgTJCuVjb5rPsbLWYtXt-uUyZcHS0FLlD5jvX26ndtBVDkj7xCwoLPuDKmMkknsz85iS_ReEcaiU1rKB9rC8qlrWjEz7_LZ3rRASRIH9xW2x1My6VVOui9cK0mr2pdr3ahzn9Pxj9P_hXWPLSnAo1qW_fReDyNqVhttuhrPgwtrnEXbrvLePy2h1-9TjEkQRy8JPFwn4xUsaCvISKE37znOv38Tjh9gWi_34C0Is19O2uXwNxn4U1ayMzBSNv4_a69OC-STJc4VLCtxuETj4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=XTO-dz4tuDPXOn5nQ4JGDCrdYeG8zPHe_et4CKcEUZea6toZn5ziAkQflrZ_Iu7YlHdxLN1AS8NKLni5zEX8RBa2YBwHD6_A6MtFYqRia70Ni_gZxbTwjDOsdotXe9rXWyApZZYKAeOgjEo5xZthoF0qZvKEf8twTxAPFgT_F2Y5lteecszdiJPHPNIeZ9PHEe6rwOeO21N9QhFlvOBNBveyUXwW6nkhJywL5DNXQENSYpR76RB0sVybgTDF-VbaWgFgGoiy7QgUD1PyLaTTxYcRclpHl5lQM4ggQsfc1sL-wk8lziBrnYn8JuBO6TSS16nJAzRxjpIQqRItQbYabw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=XTO-dz4tuDPXOn5nQ4JGDCrdYeG8zPHe_et4CKcEUZea6toZn5ziAkQflrZ_Iu7YlHdxLN1AS8NKLni5zEX8RBa2YBwHD6_A6MtFYqRia70Ni_gZxbTwjDOsdotXe9rXWyApZZYKAeOgjEo5xZthoF0qZvKEf8twTxAPFgT_F2Y5lteecszdiJPHPNIeZ9PHEe6rwOeO21N9QhFlvOBNBveyUXwW6nkhJywL5DNXQENSYpR76RB0sVybgTDF-VbaWgFgGoiy7QgUD1PyLaTTxYcRclpHl5lQM4ggQsfc1sL-wk8lziBrnYn8JuBO6TSS16nJAzRxjpIQqRItQbYabw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ9pkqd1eZNyYUqm-lbblfoX_GOF-AGiYl5PWsyA501IFfk-BIuspBB4BWH-QVABXnXpB_gg4anS8najHoOOpI5_7uFDId6VrKkuDW_6OvjiQ4u7bguvhUkYBryYKS1ssdEpF9_QYA8k0zIpTh-FuqLulSkMt-g7a9W1A6exj0NzI19Y6-dlTc9H2n9gyunvK2zcbyaO_YggHf8vaw_WpN03yGyXWXoZLO55OZAM_Il8otf1PnQkk5T27F95Ifsv_XTm02HkoskB-gEZr8YrOR3Pj-SSUq9EF5tVHurJk2xDfnT4zPnhQtbobnzbJL19CZxcl5pSe1AeYz2xQOrbwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=BEQ7jCsWtbv07_mYttb99Jr-1INGdbH8L0j58DFF4M66JtQfAqU7ltUeHa8ApojIZX66C5DF_9WKKaTb9_N9lgCrnmncltcrot9WcvDoXhH2mEtbEsLFf_-kpfHTf_V_ShcElR6F_Yl0PRn6Z38tlxpW_TUYEy_TfnDMAbpN9aoGvl8yf3KxaNBtZ7qH6xcwaXfWjsAaqKDPpkP7W9LJ6cgIyeALYp3RGgF140-IwUHIGFnIn2FNPiFmmVwgzQts2k2PAGB3RhRb9etKOdPlGy1LbSkScQGw5u-ukS8obLoLEVHSPrZ06yWtXsuuw1S2pqSz-UhZMwdwsgn6jmwntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=BEQ7jCsWtbv07_mYttb99Jr-1INGdbH8L0j58DFF4M66JtQfAqU7ltUeHa8ApojIZX66C5DF_9WKKaTb9_N9lgCrnmncltcrot9WcvDoXhH2mEtbEsLFf_-kpfHTf_V_ShcElR6F_Yl0PRn6Z38tlxpW_TUYEy_TfnDMAbpN9aoGvl8yf3KxaNBtZ7qH6xcwaXfWjsAaqKDPpkP7W9LJ6cgIyeALYp3RGgF140-IwUHIGFnIn2FNPiFmmVwgzQts2k2PAGB3RhRb9etKOdPlGy1LbSkScQGw5u-ukS8obLoLEVHSPrZ06yWtXsuuw1S2pqSz-UhZMwdwsgn6jmwntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=FGlAlMH661iMd323xAG2TdHAH77wbT2Houeu7j-IGfKcpexCQAbZ767m7tBfgRiUvPpp2rzbRho0r6QuPXT7okw0o1jEM41XVaHDn5qbac_4yMB-zHb1gEVDj4Rfpevjnagoz9wsHj4a1k9kneIVMciNcEpa-yef9MvQsDzdFaRzfBpYN4B__EIj8-jwYRl7CW9K__rXK7EG19gonKDDb9INFDqHxKicj2UjVWuUAXp6tjLVZVIzRVH3WiCpV5CnA86mzvVRJL_sgGh7bfgOQdspGJUtrHAog55JSnWWe5OJrlWjr89YDet6F0NqSrfvk8OkWvajTR1gpir63VoSNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=FGlAlMH661iMd323xAG2TdHAH77wbT2Houeu7j-IGfKcpexCQAbZ767m7tBfgRiUvPpp2rzbRho0r6QuPXT7okw0o1jEM41XVaHDn5qbac_4yMB-zHb1gEVDj4Rfpevjnagoz9wsHj4a1k9kneIVMciNcEpa-yef9MvQsDzdFaRzfBpYN4B__EIj8-jwYRl7CW9K__rXK7EG19gonKDDb9INFDqHxKicj2UjVWuUAXp6tjLVZVIzRVH3WiCpV5CnA86mzvVRJL_sgGh7bfgOQdspGJUtrHAog55JSnWWe5OJrlWjr89YDet6F0NqSrfvk8OkWvajTR1gpir63VoSNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUNI6Tjssspnow_8u4nORgCFMeTU1RZ2gT5htQBUQpHSzbLde5yBMcGiJ5hYUe15xGKQcF2YDUu3LoN3KbYbaixf3blh7J8iC7OSiauZaECXJJnVxNhSWV1raVxgJ71S-ryZ02s46eltHjYh0H8uWSg8hnzhjKHxLb15W_ScNFl2OxbyYuq0WrELh7SGEKESeT5eprPSmvZyfSECjXTyQs7rPpgYWXHWtR124eXMHjs1SGPgttE7OTXOtRJQE4ZfHHkQP9KQfREz8qOBatyBHA3F1LaDQb9jJY7BXjPAR2If5__iUxKL_dZoJVqvQNFqatFXefw1GMlUHj_ba3vVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH8MqiZqp08gXSLYv4YJHPRrgI801Dh_v67PWYTNEHDObozXv9wJdou3invwb8fiTAJFBFd6feDZrvcMjcUW1FBHnj2pw0nirLAckO3Bx8bfVdoGph49k5VmqZJO8RfLz7Ch7BdgawTdnGbKERK96TFUiJ3QOSZv1F0UlQboDWnFd_fygBVKHrkg480upgIMnVsjMBlCvdEmqeIcyIAT_dE8jEF-4lYm-OPQICjApvrqWE5_Za-Y440cFuF1vjtiSpk97ha2yuet98V_yzTWs00XyU2l3O-mQd08ZOBAmkjh8nNbCswyuQ7D55usdceCTvw7IUVc-5Oyeif-xf-RJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viEU2QrRmq5iba097vqv2bJ6Oa_EzOHBt841moTx3j7Y34U3Na29uNs8jifJBNMajZgP6NoO8uoNDZMBWaDTbT35l2eGiudw5n4yO9OigyqzXHBc64A4O3xoqxj_zbUPAoVErVym2Dduladp7AiNVpt3Uw0iM4mQJERccIGNcHTxhuvcbhUYH643rjpux0w2Y440qOy8zq5k7BT1arwsnhdB7JN1w6QsGyWQieyJ0c2TcWFSM7x6-TFE0uoj7Fw6jfZvm2wYgEHkJeEpPCVK09PRi0lxEPzktG0AQKM2FivdmwC1W4_l6Iehkk9k9V5XzRXzqH0TvqrD2wS8LayUKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpcdg1xzCtoO9Xoh1eiJnnJuEGOFz2taGAA459X0XGfBmadkOUkRHCtOcoitxc5sN28qVN0jiuQpKMiydO4167vYzZ4RPDiIbUkgMcTtuWl1pEV9sAW_V6KcFjn7cL4xCBTpImlamTgcFInV3b1zQEsZ4_Yc2S7fafvqhiYbmLqJ1kDsfMhGjMeT3ptHnMDBzGV3JEIW6-2VUtPbJvMdReGwlLnYlCghN7lwReWpx9d5tBOBl-iRC9goJoUvxeIYg1fCCekp96Dc4nYCk5oSyGIL9xM_v_9r599C3ykv0V9X6BrazxZNjUD8oPunr98XeQJRrSbpE9V48_rngRnTvA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=MH6isA6Axo_RYLLnWDG19sWv6BrpwmZiNO5pDtKXP61kXlBgXmMRQ5NxgZanJSV53lKAOcSLw8JaZBNeqBPdkj4V6z27VYPRNLfXUE7q9uFA5RAbtJWUAuwgJ0jtB7aLM_THEjrbKZM8GI1F7CGzd1rfjYuyBIa8022UMBT1i0xOgVfduY_esUS4Lmx1e7JP51CXEaWMaVa07cWd5Do_bVmjoj36r5SAZG1tMGRU55I-a0swZNo3EiRbcXhxKcPtyVLqNIAktv3uRxuhomPLjyTWe3GFv60qYW_iDkO1bfJQT9WC1fxG0-JFxiWB0q_nElPRqrOCwegqe1gvgXMhOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=MH6isA6Axo_RYLLnWDG19sWv6BrpwmZiNO5pDtKXP61kXlBgXmMRQ5NxgZanJSV53lKAOcSLw8JaZBNeqBPdkj4V6z27VYPRNLfXUE7q9uFA5RAbtJWUAuwgJ0jtB7aLM_THEjrbKZM8GI1F7CGzd1rfjYuyBIa8022UMBT1i0xOgVfduY_esUS4Lmx1e7JP51CXEaWMaVa07cWd5Do_bVmjoj36r5SAZG1tMGRU55I-a0swZNo3EiRbcXhxKcPtyVLqNIAktv3uRxuhomPLjyTWe3GFv60qYW_iDkO1bfJQT9WC1fxG0-JFxiWB0q_nElPRqrOCwegqe1gvgXMhOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=ESY33bX7Vir283I5zp0tFp9vpuwd3aCOVqc6elH5WB83xKLXyEsJy8FjptrX9FEnnESPfjkFxg5WUn7kHF7V8no_e1qOy-6XONomGLXQ8bx0HBzENCRAUxoOqi8kPaBVbFKKJSJoA-yR1EvWa17qOmhjdVMwgOZk6DcmsbISo69_NufKohJn7yOWtCfVZpmZVcovy4JIcC2LwbiKAJpvqoH8gPuh7PsrtCdg0x7tHRFyIBDNQmbWUsva6wQhSjoyu3sxqx-iJl_q_zAs7ezZ2OK_O4aY6SXFGGVtnYioAaOZZvnhl3kkKUo6f5oPuWj1iTuWpQLXR9XO8urZU22W6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=ESY33bX7Vir283I5zp0tFp9vpuwd3aCOVqc6elH5WB83xKLXyEsJy8FjptrX9FEnnESPfjkFxg5WUn7kHF7V8no_e1qOy-6XONomGLXQ8bx0HBzENCRAUxoOqi8kPaBVbFKKJSJoA-yR1EvWa17qOmhjdVMwgOZk6DcmsbISo69_NufKohJn7yOWtCfVZpmZVcovy4JIcC2LwbiKAJpvqoH8gPuh7PsrtCdg0x7tHRFyIBDNQmbWUsva6wQhSjoyu3sxqx-iJl_q_zAs7ezZ2OK_O4aY6SXFGGVtnYioAaOZZvnhl3kkKUo6f5oPuWj1iTuWpQLXR9XO8urZU22W6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
