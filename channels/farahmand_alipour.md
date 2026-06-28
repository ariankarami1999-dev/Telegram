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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 17:50:05</div>
<hr>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vs9FTKdeDZgvZj0MBKsAA83lOMf-tZY0ojRCx73d_0OKQ_xVzYnLIi3uWnZM6flHqEu9JL0GRWpirffggSRbWuvSjG1AU1Ft0ie_q-AL9HeYxnhKkBat0lTdS3cffoycKTI8qVpBq1MOFYXaRIb34EstwnItTl71qoMFUfUbhsHafqhHFC6gziVrNi82K2sCwPi3AMNC_MLPi1Qb_7mOJrJEQCogkCnhPjRWKR4f_0gWxcrRwl5OJs5bvVlGdMYo3jNibKSgQydmfaqenaf2aZaCRlm3HuQrxhWiXl8pljXQbz-a7GP7hD3-Fh7JE9GhGYGonz-hhWXYRAqcZY5idQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vs9FTKdeDZgvZj0MBKsAA83lOMf-tZY0ojRCx73d_0OKQ_xVzYnLIi3uWnZM6flHqEu9JL0GRWpirffggSRbWuvSjG1AU1Ft0ie_q-AL9HeYxnhKkBat0lTdS3cffoycKTI8qVpBq1MOFYXaRIb34EstwnItTl71qoMFUfUbhsHafqhHFC6gziVrNi82K2sCwPi3AMNC_MLPi1Qb_7mOJrJEQCogkCnhPjRWKR4f_0gWxcrRwl5OJs5bvVlGdMYo3jNibKSgQydmfaqenaf2aZaCRlm3HuQrxhWiXl8pljXQbz-a7GP7hD3-Fh7JE9GhGYGonz-hhWXYRAqcZY5idQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IotlhauxxamIoDVWB22596GsxhSImjjoU_l-RM3CIcp0hXl4G0fOXuVibEkxZIx2BZ3mqc6SOxR-iwulyUDdr9hlT8tNAGFOy4zwZxBuBsrfofLanDNYJxHgzMdi87aIPH3UEWDbmpJ0G075KHvCuGJnoi3k9WVlLN1y3K9dmvOpPWMvlQJt9EEtsagGgdeQJ5rY-womaGpExALUJnuXkEBji9W1a2_UVWLil_PcUrc-0Mt1gc4nJhVtF7iYrQx6Sdb0ntH6iKm3gT7cR_6NNjOOwivUuqMgb-nsEzDgW_p1wGaqx_6IU3IkfCEQ8-L0yys12NA7EHrx-hGYWYCH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh1gIiMO26gKmECsuBu-x7k7PHtOiBsdlmJvQDDWm9Iu4VRDM9H8ysl3rF1ztO0H9CVJQTQJh_gixp93GE6iF9sB08ueqJrv3RxESsmRam-I2-HbdJS1IJIrGrNP8_7obG_MfOEJ2xHxXXu9zQlWev68zWhM3xKr8wUKhZVLxYeEWBfzBhbK7g6LR7GH6jBVtHvZrsMwEeOrEV6FSqYs3gvFK_i9lC0h9QtHkxXPZaYPqzpN4v-aZ1e4KQzvDn02L5A3XfT-1EOpWeaDaC5epo6pbtaeV0e7OZQNvlhitP0LsH4oH2Vw3F-p4NALcS3byWd5oN9vThs7ng8bR0ESgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvHwqgI2ExWT3XuUSw163hbtaLrav_ZRLgUnBBkSckizl2iotJ3uGW8JdizVmP95Dlt-9wN7lZx-GxA0roUBIk4trkNLCcf27_xYee3NIzlB28H08OGwJlf5JJe_4ZIJSvunHLusgqlKwJap83XQmFRPoKuercvuMz8zau-qSsmsMe_mqIk8j07FupptfA1t1jJgUCNQI1Xa1ffiWc3NP4Omhv6KmW58gea19p78DndxXpGl_uUR3HRLrfUf2rrNBtY0WjT2NwKb3_WsxwH1gffr5XUcmRHyuqsnv8JaMQPH66d4HaRs6fahIt3AXf6PESxgMT1ivJVUbLZilcMp4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnJoDBqq329PIGb4Afybo7MsPSivmktuG4l4eFtSRCTE8Q_Z9ZbvnQYUDu4AsgkPLCMJzGEZGj85ihCa8zN_IyCEaqmT0NAigLIko1O3wAaFZ138nO31LVr07-TguZaItVw9oioEVtK0RjafdXt021BJ40b-orsFlpyhw0HQN20E9jCNhG0OR9Y1LJOSn6gZmoAjwr1lGCGGEZF8804etaz1i8YjFvbjPZckZwIS5S9hnkPKzdnfnIqHbWhw-ag8u-4ofozs79Bd5n_yEoVMHY27_GWsEA3y8bVGpqz6VXteCdKD2C7-RC9THkauZSjx8bBTEqS1xYsSiELkEzyTPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnJoDBqq329PIGb4Afybo7MsPSivmktuG4l4eFtSRCTE8Q_Z9ZbvnQYUDu4AsgkPLCMJzGEZGj85ihCa8zN_IyCEaqmT0NAigLIko1O3wAaFZ138nO31LVr07-TguZaItVw9oioEVtK0RjafdXt021BJ40b-orsFlpyhw0HQN20E9jCNhG0OR9Y1LJOSn6gZmoAjwr1lGCGGEZF8804etaz1i8YjFvbjPZckZwIS5S9hnkPKzdnfnIqHbWhw-ag8u-4ofozs79Bd5n_yEoVMHY27_GWsEA3y8bVGpqz6VXteCdKD2C7-RC9THkauZSjx8bBTEqS1xYsSiELkEzyTPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spomz7bjOu2I5arbglW-35Spx7_PdN3RWptxCq-doJKbFk-6lWPrCZFJn_pYKqr_7UqjGUnpoHTbhGiH8CvaSORrszeWYO24nk2mbK9LU6fyyT12tzRb0PrRPHZZKTbM2bQdxa6wkUB_mK7zZNRuOc68BTROshOtec272ZdhtlBpQas41pZJYVP1V7ozgWZn9jQGVPum47q58-Ho3QVsLc2sa5mz8g2rfYET_ac3A16C-bVldyCEdgeWAclSuZnTLhg1OegTQh0mz-hYlnyUyeTG1LIJ7TBpGBO_bMnGA3peyXFdhT4tURIHzXlpI89bqRNiKVRNGcmdP0YhKTqSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Rn1aVjz2yVWP--CnT-Zu39ls6Yyg36U-wNzNtCP5-k4gBGeFscSOu1V8JNxaVri7wKVg9cNPJiVfAuUWJE0EZNPuH8wqN8TwONYL2j1LGEUzs_SP9MRfpP9XQu_XgM99pZ09fmTJOO4grd_kH055vUbvYe2NOZfDVFadAlaXzeSPbPKcT1r0kW3b5oIJTWHkdQweujOBpOX2VX4AJfHhLJsiPfdAvkLtJCAx-MqAuIIRIH1bGp3vyT-xEFdxQ70GyhHbowLffdCiCaWt5coSkgIQn1D_-FNrcDm3ggEbmtbfK9xrXl8nVSnvBN_mn8j0pblRUIURVesRvxQQL1SYew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Rn1aVjz2yVWP--CnT-Zu39ls6Yyg36U-wNzNtCP5-k4gBGeFscSOu1V8JNxaVri7wKVg9cNPJiVfAuUWJE0EZNPuH8wqN8TwONYL2j1LGEUzs_SP9MRfpP9XQu_XgM99pZ09fmTJOO4grd_kH055vUbvYe2NOZfDVFadAlaXzeSPbPKcT1r0kW3b5oIJTWHkdQweujOBpOX2VX4AJfHhLJsiPfdAvkLtJCAx-MqAuIIRIH1bGp3vyT-xEFdxQ70GyhHbowLffdCiCaWt5coSkgIQn1D_-FNrcDm3ggEbmtbfK9xrXl8nVSnvBN_mn8j0pblRUIURVesRvxQQL1SYew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=SlPYp5_GRPb0rojmg4Ky4I0P-rajgBu5DXdz1LSMjaqT9zgQQw6DidsVivU6G_CiScbf_ifXMWG4oOj9aciLfghAQZCRFdVwTIKABskdmHqTO3sXPsv1s1RZp79leu8Fcd3-KHF91n7BwfBqwApU3OK2voeaCiowO8Vgy2xj5w3bkZtVfpvctPpf-X26bY3Lrp_nOah9jcSv0tfTiRSvSmaZvFuO5iedPCuio1kAs3ACozBs8kRws6ZGgXMUErm0gAKcHl_26vzVwRb4a9ND3oYDGWec8lGU5NrJ4qNYPw9zfOjsxescsoWppa3oJ5Ls8kcQ1TuJvGjohEWnpVfFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=SlPYp5_GRPb0rojmg4Ky4I0P-rajgBu5DXdz1LSMjaqT9zgQQw6DidsVivU6G_CiScbf_ifXMWG4oOj9aciLfghAQZCRFdVwTIKABskdmHqTO3sXPsv1s1RZp79leu8Fcd3-KHF91n7BwfBqwApU3OK2voeaCiowO8Vgy2xj5w3bkZtVfpvctPpf-X26bY3Lrp_nOah9jcSv0tfTiRSvSmaZvFuO5iedPCuio1kAs3ACozBs8kRws6ZGgXMUErm0gAKcHl_26vzVwRb4a9ND3oYDGWec8lGU5NrJ4qNYPw9zfOjsxescsoWppa3oJ5Ls8kcQ1TuJvGjohEWnpVfFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=V9L_xy52G6v0rz1oZDb-62l3GibTB500UBewQqlni0SW8P8RKao0BTZb86g4lBomRZSgJrS-pgSc1zYCRNJTOt5tFJASDxq_hJTJUkVkQMTJXeJgRa3LEcTGFX74t2B3PErJda7v00WnnhMFrVwd3Sp3_qNT4ASW-BoaK58MI1joYvmwfCFP0pyq0RvHNa49ul2lLhC2Sm2GwBp4HhSS-jIXEVqx-Qz8Wf3xhfBDB8oCjqQvJgUYD02eKgNZT5xDa3iozUlKFfzC1n5LKNxcq9TxPo0WPkXlfMMe4XTrQuwneAsXVRO6mXRgj8Hv6KJBnAn010EIOimKPoE5oVlXxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=V9L_xy52G6v0rz1oZDb-62l3GibTB500UBewQqlni0SW8P8RKao0BTZb86g4lBomRZSgJrS-pgSc1zYCRNJTOt5tFJASDxq_hJTJUkVkQMTJXeJgRa3LEcTGFX74t2B3PErJda7v00WnnhMFrVwd3Sp3_qNT4ASW-BoaK58MI1joYvmwfCFP0pyq0RvHNa49ul2lLhC2Sm2GwBp4HhSS-jIXEVqx-Qz8Wf3xhfBDB8oCjqQvJgUYD02eKgNZT5xDa3iozUlKFfzC1n5LKNxcq9TxPo0WPkXlfMMe4XTrQuwneAsXVRO6mXRgj8Hv6KJBnAn010EIOimKPoE5oVlXxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9rmGjOavrkh1ENg5BBGqme7bj9Qsv5FzvNFnTF5jHCXFhfAhkFXAFMJM33SI6wm6KxvtiD2Ur4zvlcuvTvTlvHjtqigwbFyuQrJNAO6SUh9lcaEo5Bu2KWcdj3wG3GDK6J-3F1OkquYbHdH00cUjmoLeXr96d9uH91ZfvlNy2KZ83DKXIaetntusCgCpOvSHxTXB8ZiYuur-b3z70Lcyqt9Yhwo0vmUX5YWQRmxU23pl52NLxL1Z0ZsR4eNTAZQ5MQcszOuQCSKo9x3EF1TfiyaN3pLWraVBbAgzzOwXwlC9Qi53eqjo6zJv5zlExvgOhHKPzIYzWZTkpKJ6eaY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndQF0pp0rKFkxDgEAVz-JpzOmg1xnqV6Xhd_4nJVoBpVoCwUTxjNMm6C4ukqx03boUDrgGqf4HZC4i2tCaM3iPtCIAojEOBlFW3xRqhUXanSqxIFqN525nPA2iYD1WzMsetYFypZ6x6s60IxXBLu_GPy8EJBzrqE9gvv8JTFPT50KLkqJfPm60zN7YOHlKL1lehlVg7wsb-JjvgPbrh0DGw7grqHZlcJeapQgAVoNmI9Y7DL6KelSDhaLaIVmggI4CZg0_1scIoElr99v6zaHICFqq0GXPRImth3EDBiAtMG8MDSUY5uKOAC4O84R-CPWBEHeAGUzrZ_zlHfuSES3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=rcBAJMqRNSQPPsQcGnS5HAe_WdD8bEnqyVgKDGP478QmJtybHmwk01rwU7XjQOnGez590MtPvDaWk8DgTa_XVl-nBMhS0VYLpaPLsEgzrC4EmqX8Xxw8vFyllDMNOYDoUoJXUONJFwjM9Nt0PoyKIFzd55S1zQZl_vhOcWOazr_RlzK8x9P_KYOPoK-7CeH0_2bkP8y893PZD30-mNajwXccjfMNGOPR5oOH4iEe6J-3Z9YmFfKgQsezvelfJ30c7o-qFxHCC5e4SiAviiTkRvm4_Cj7sXYGXZINHlJFecLzURI0ntLL-YaDQKeu4sW41dpPJiBZFL0HczIvOwnT_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=rcBAJMqRNSQPPsQcGnS5HAe_WdD8bEnqyVgKDGP478QmJtybHmwk01rwU7XjQOnGez590MtPvDaWk8DgTa_XVl-nBMhS0VYLpaPLsEgzrC4EmqX8Xxw8vFyllDMNOYDoUoJXUONJFwjM9Nt0PoyKIFzd55S1zQZl_vhOcWOazr_RlzK8x9P_KYOPoK-7CeH0_2bkP8y893PZD30-mNajwXccjfMNGOPR5oOH4iEe6J-3Z9YmFfKgQsezvelfJ30c7o-qFxHCC5e4SiAviiTkRvm4_Cj7sXYGXZINHlJFecLzURI0ntLL-YaDQKeu4sW41dpPJiBZFL0HczIvOwnT_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbqSo2o0rUvd_iBw_IWvPwoIhY1h6_BxKp4WhFplC58x2kw24576MHD0EfRLFpT8q1qp1kqowjBTWVIEt1USN7CMyUQvNK5L5PAgRZUT2IDditdq1gL8xX2GPqgBZxx8_e2tSW0eCKIlkO9KyELtrniIX9H9Xc5fjdk7av4Sh9Tl6NBJxTXW10Pfb3GnT6TxnpRrfzXIpeteJGJ-eDo5alZEg0IVSBJyEjaNsm73-O4nn9O6bIRzFGne4kdumOMvNUmxZTXHIOh2R7-18Jdg9ePkHxGD6CSUjn9Lcqz9HXN_ImoBLWJe1-djpDqjIjNO8aLaeRPmBEtBRz-Edzi0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWpE6Uj9ZBlycchZuOV5tI9kIHQdIcMdxNAxJNUqvlQlRLvJN4PBNRSGCed7zZaP5-HbtzeWJ8-KD-3C0lZA7fZz80W1hpFGpTP5Avx8clt5NIQMmSgUDMcBju9wM79UdhX9c4P9STXavE15UP5OC1EfAUjttu-J2kPfW2EvgpKqBDqyceaEU8vrjLAhYx4MMbZ__2abRsHIaFdPMLAy_XBPK1lpGXyw2YW1SvH6kGxC7VpiaUxil2WTQhQ2Zhbbn-LXhZW9E4NzDCL_33py8d0062gqEqvAOOELpi5RBsANbJOdmxkhlioYJfgKMClZP-VgSBGjGC1bfhprmwGCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=atEuDA3LoOPJGIPNMeLbj0o7_r2hFTPYLoy-FyI_urbfTXbt6vtzBdc1VmdtDN6Ycb3KdTuAyQgUebyAuf_maBSwZZ41UgzmeHjuRPzqMfvhEwAdH8nfJnI_JsLGBo069ucN4q2yAvwuClPFx3F9rCQeQU09BEa_Y6OpvLOxKpsIQiIXP1Yit-z7tOR2wyjSFi95ls884bDFwjSD3kd7_wOrTxbWi-sWe3ArjEd7JDAMI5AAB6bgw8H1pdFShCUHE2b1-fRmhJYbTzEVPwBA0kZ4kbcV1AmjjzZLvLFD2rxz_mDf3hlDbcIwyXhYngdj9F6ZyTaN2784UxdTDSKImr-e7lJDOEx7JltqVvlDo7ao7rWNBM61Achk573WHso0sEHctn-QoSuxPXXlIIYj4Xr3h7IBm7c_bgeNi30WEq9NP3xhf5FH0z-YYSLJKcAKb2VxUtTGt4gdRYKB_t703-XROl25ZlJjP1RSWsrPCCsiA0uaiZUcHibSPQf0cpui7iA7s9HGVCh9zyWKjZttNuR_QQfDgPw3XnfmSINSPS4MDstMkGvl5OoUAFSkkHYIIBQ4Qi0Y4omLRYhB3nvCcRAsN9chC4vmRnDMTL7EC9B8daoxQci8ECZMsy858uUwszZwlhftSf1NfbwcGJDtpjRLFs1XiZ44Ys0IDrTvYSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=atEuDA3LoOPJGIPNMeLbj0o7_r2hFTPYLoy-FyI_urbfTXbt6vtzBdc1VmdtDN6Ycb3KdTuAyQgUebyAuf_maBSwZZ41UgzmeHjuRPzqMfvhEwAdH8nfJnI_JsLGBo069ucN4q2yAvwuClPFx3F9rCQeQU09BEa_Y6OpvLOxKpsIQiIXP1Yit-z7tOR2wyjSFi95ls884bDFwjSD3kd7_wOrTxbWi-sWe3ArjEd7JDAMI5AAB6bgw8H1pdFShCUHE2b1-fRmhJYbTzEVPwBA0kZ4kbcV1AmjjzZLvLFD2rxz_mDf3hlDbcIwyXhYngdj9F6ZyTaN2784UxdTDSKImr-e7lJDOEx7JltqVvlDo7ao7rWNBM61Achk573WHso0sEHctn-QoSuxPXXlIIYj4Xr3h7IBm7c_bgeNi30WEq9NP3xhf5FH0z-YYSLJKcAKb2VxUtTGt4gdRYKB_t703-XROl25ZlJjP1RSWsrPCCsiA0uaiZUcHibSPQf0cpui7iA7s9HGVCh9zyWKjZttNuR_QQfDgPw3XnfmSINSPS4MDstMkGvl5OoUAFSkkHYIIBQ4Qi0Y4omLRYhB3nvCcRAsN9chC4vmRnDMTL7EC9B8daoxQci8ECZMsy858uUwszZwlhftSf1NfbwcGJDtpjRLFs1XiZ44Ys0IDrTvYSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETnOzVAQZpkzWb0qZLYN8S-FVgwnMJm7z2JROW4DcJ72pKEefFNreRWiFGcPAwrQ5VnLJIE_Y2XRfw8LkXRw7UJp4_NZb4Kml6fxesp1xc8EcgZmhqhOL9ZuvvJdhTjzDvQVI7XUaYmXSqBctdMNFJo_UWwaE04k-gFKusJ6heNuGCDhfDKJxuWb4F-3VxcA4Ua8mqO6HAGEz-1Fhl9gQKl5Qwf5LxyonLZsTLTNbgb621P03HZ4YWitZ92cspJmx0FzHmhEM3p0OTM5pkhrtqeGE-1Fvd4jFSLunwv68sls_1ZTp8bZEQKm8EpQELbMD_3JHmVoTR9sH3oHZjErhErw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETnOzVAQZpkzWb0qZLYN8S-FVgwnMJm7z2JROW4DcJ72pKEefFNreRWiFGcPAwrQ5VnLJIE_Y2XRfw8LkXRw7UJp4_NZb4Kml6fxesp1xc8EcgZmhqhOL9ZuvvJdhTjzDvQVI7XUaYmXSqBctdMNFJo_UWwaE04k-gFKusJ6heNuGCDhfDKJxuWb4F-3VxcA4Ua8mqO6HAGEz-1Fhl9gQKl5Qwf5LxyonLZsTLTNbgb621P03HZ4YWitZ92cspJmx0FzHmhEM3p0OTM5pkhrtqeGE-1Fvd4jFSLunwv68sls_1ZTp8bZEQKm8EpQELbMD_3JHmVoTR9sH3oHZjErhErw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=GMSoQf7EMLQvd09jgDlE54z5YNt7d07ZTZqEg_ncajxSshizxUIFFTkRkachGOduD5kDlEJZltlNd33id1E_H7N0TiBDlhPMj7PwdGQXaB4lhcrZ3i3BNGFZqCLxn5BefK0VOlFc3eomgE7L5QMAPjaPEBQ2okQiZHfpFkrNuJoaCxq25wEH9IsL3dhtZnaH8U24os1LojJ35YGGCNR2MWWGvdLNaqBKWHHRO-vZSmDSroxSu3aARlZ7lqPVLPErgs6daDa1eapwv8lTrqGHsrJ3lir3MujCQps-k3LkHZqz5QOIXuXsixoYHJFvm_mb3CUuv0oNLzCTzqMHT6VBNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=GMSoQf7EMLQvd09jgDlE54z5YNt7d07ZTZqEg_ncajxSshizxUIFFTkRkachGOduD5kDlEJZltlNd33id1E_H7N0TiBDlhPMj7PwdGQXaB4lhcrZ3i3BNGFZqCLxn5BefK0VOlFc3eomgE7L5QMAPjaPEBQ2okQiZHfpFkrNuJoaCxq25wEH9IsL3dhtZnaH8U24os1LojJ35YGGCNR2MWWGvdLNaqBKWHHRO-vZSmDSroxSu3aARlZ7lqPVLPErgs6daDa1eapwv8lTrqGHsrJ3lir3MujCQps-k3LkHZqz5QOIXuXsixoYHJFvm_mb3CUuv0oNLzCTzqMHT6VBNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=Zdl2iRm32gG_6gYx8G_g8Mvpix8tjqy0MwmGNybJyqo2d7qX2WpJVxy36y09Q-Seb2rQAYS7DoupzpjQf3PyQOjyc748nEHjHNOJy9NMsdGRXslUhfjgTjdUgzGC9xjBoWPbgn2s1J_fBxz5B3icL4hRyvOSmKMSw1FgXMlHlzQyVv2Arx5wyvI8kCRiS1SWKPlhO5Q-yVW8F5XbkU9I3DNKi3lxtKlkmGiOryFD3DKMDpN4aoyIO07AxTzUOKfaOr3MuFPSF13hg1O2B9OMtskQiPwGqi2OR7M_aJVhm2lGoJIoSXj4J3JQtfxvBnLGn_PIgmjF5lvwBRMxJcEe8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=Zdl2iRm32gG_6gYx8G_g8Mvpix8tjqy0MwmGNybJyqo2d7qX2WpJVxy36y09Q-Seb2rQAYS7DoupzpjQf3PyQOjyc748nEHjHNOJy9NMsdGRXslUhfjgTjdUgzGC9xjBoWPbgn2s1J_fBxz5B3icL4hRyvOSmKMSw1FgXMlHlzQyVv2Arx5wyvI8kCRiS1SWKPlhO5Q-yVW8F5XbkU9I3DNKi3lxtKlkmGiOryFD3DKMDpN4aoyIO07AxTzUOKfaOr3MuFPSF13hg1O2B9OMtskQiPwGqi2OR7M_aJVhm2lGoJIoSXj4J3JQtfxvBnLGn_PIgmjF5lvwBRMxJcEe8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9QrLfGUCN-vKGEOOxZIYLUNrzHlGbQNnfyTT-jBvhIQIOdLpdPDeuIN-2UcYshk6pn7AUDv5fXGWrrCsMtdK0HaCIhR6hI2TQBrvlgraDWyyxhaHzPlLuRKUGmJu11x3ueYvp9KwlevUYYiuGLJNw0iWSJUmDT3W2d-wRxXFTojuOZZ0P00rP5mcjnx3NILqTL6RuBvZQ84cu531avhmbywh2eUBQoFIQg2KtEU1Ypdg-OUcFBP4WsEDHOK7CThT0DEPZSF-VNxnP1jlny-92NEXxeSZNqHrC8WEuU8u_EX--IVzAHPQGKzdKKDJBx2OHfoDpUZ9Cqq01kYObmsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFXigEaQwmcFsoGmS4_nrKaTPuXsYishF_6KxoIybn8OVTeHf4hnalbaj4sG55-ZvvXWdhbNzGmsTP5tUKl4Kg6B86ZbJZhp86u8fURWvAv_ItbHqYe4-zBtthlKxIV6MmyxJ6GYoWdtmV3trIo3zpiGGeGBEcSMwGdyy3nAl637qcEbLU1YYUb0mpWgcQp-qd8Ghs73aCmXEWvaWBXavIAAeUejvpGqg6KObM7C9Ii6FZusfH8xN0yhMX_3mIPjertk0tim08DvgtXCpW9yM6tgG3sqoZis28m3bx7A1Mb5kHVupXtGBS-k0i5tLdvsC7_HOSLsPZxF-fCMfcmOdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4yWMaNJgDbt-gVjB14HwjybovZj8QIhiysGolFu8E0gRMk24UQbflgC_KvusQtR3mNdKLy041eh01MFlS86bWq1scGWvRN1sa4QkcRTIVdos0KdXBFhxm-J9GKISaFUMoLY_8J5pv6qQZiOH4t0etCavk0qfveJOfgElUEFsLeIqoMuvbX4CKrPLDDLdjyYpcM5chJaXaHwqdoOV41Xo1KfFFJGVYdKGHKF7D372SH2Vp07ecSaxdXM-CC3Fb4tUc6uf2kS58Bqhh7DP7iAZZr7yFKgz1pPKG6u0RsaL7vNFQ9Dtzq5PVE-zzw7SKlJI8BPNtE2TGIe4Wj-LBtZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUv_ZaONddoUjfDbLpFwMLSSnkI199jrGZhocTWjyb3igUvR_GSvX9ZN5XbB9BSED2koRpQI8InWism9qF9LwDLEsc4qnIND6BKIcWRmXgpabeh-yXLc4swzM_UowPcysTSGfXA3Yu7L2wk-PdaZQ7v5G3iIRpO8Fr4owJDX7hLavnQvOgmlP4ZKfAOOiMytd5PXLAeAv3JNjhjdNI5OyFfwrtPutsJ77bCVlYJn_qVY7EV4ndN9ezTjJiowDbnasF0VkNMkVWk6UG7w5L_5f8MQp5XOImvJ9-z67GZThjdtfou388ikeGigz7PVL6BnC4ym9VtSY8FFi1piWY8KTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1dbGnmtxhd6J_TABHpPMyAmhcRiakmej4YMyfRTw1CZIz_Dob1YhRNaAQVFHBUsuMUm3bRuSupPk-4d4UbOCc6Q34RF4q1rFRyvd7rS6xuaEH9edFULOcG2p7qFrEZpzugwpNhlfIRx-zympwH3z0sls15NtNzLvGZoL26lVWsnx-XWS1RdRgaZTwjDONCzx2_A8LC9wvlRPx26PD1F1snTSGNmlf88yEFJCZX-8x_QP1irS78lU85jASKkJGi0RcRJei_cLTSUpz3KxS8RxRrMGc0ckUtJjJMl8CIZJ7p5lmVH7DHZ7_uqvjHYeULUxgpgHynp-8CZYPKZj_dhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=IxZ7Tt4QMGOaIFAu2t-oG1_z_vqTK_fs8kvOp8WeGDYsBT3sU0iY4_JpEw5UrPozL6OoPeMuQwB3cbP1Hbegob1QNk4vqDtfyIkcQf-kT92vd0zDn3EHGxlJ5BswOwydV-NoEHpdAsV8Qk0FN9Vq4cUAbABA6YoqseHEtS1RZAy6H7vTpBu2ovTDy2PUUe1ktw3lATFe73VOLzqlWRbVz_XXKWSCY99dAWOTVLz60f1_5t9dqlMs_5vJu0kUv_c9blbz_JAFeKr7FvOaJrHJiPS2DHQyDPAr-gxhW6x4IAuyHJ6RpKuN0S9zncSGtjSqKgDu1K68c-vLRWZMHXA2Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=IxZ7Tt4QMGOaIFAu2t-oG1_z_vqTK_fs8kvOp8WeGDYsBT3sU0iY4_JpEw5UrPozL6OoPeMuQwB3cbP1Hbegob1QNk4vqDtfyIkcQf-kT92vd0zDn3EHGxlJ5BswOwydV-NoEHpdAsV8Qk0FN9Vq4cUAbABA6YoqseHEtS1RZAy6H7vTpBu2ovTDy2PUUe1ktw3lATFe73VOLzqlWRbVz_XXKWSCY99dAWOTVLz60f1_5t9dqlMs_5vJu0kUv_c9blbz_JAFeKr7FvOaJrHJiPS2DHQyDPAr-gxhW6x4IAuyHJ6RpKuN0S9zncSGtjSqKgDu1K68c-vLRWZMHXA2Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=okeqL8H3sAo9aSkIKz2WiwLJq2xS_Bev6QKn7vvHbKWT0ibzSz9OMaECj9Xh6eWKKB1jdqYOTBoQF33l-vP5EqJPuePglzSEjzCf3uiNy0kV0vm3bmI_iR5B1gdsEvqnS_iHZg_LFN1p8IAmdM8U4R_ezYOYzaKUm7RYTDv5FFyLOxchbPKGYVDOMeWjLQ2x3T-ahqzOC7MmXzjswNmLkbHq75u-MkVHi94yvJNMsJCpPo24LY9KobSER9yQkBhDa0irlkvhCTAy1Tp7aT_uwGbqE1z_Cd5UDdlrQxRS24ISUI3HdNsKmOg8WjKvvfNqlMA-wNuvbwi8pHpLyBrhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=okeqL8H3sAo9aSkIKz2WiwLJq2xS_Bev6QKn7vvHbKWT0ibzSz9OMaECj9Xh6eWKKB1jdqYOTBoQF33l-vP5EqJPuePglzSEjzCf3uiNy0kV0vm3bmI_iR5B1gdsEvqnS_iHZg_LFN1p8IAmdM8U4R_ezYOYzaKUm7RYTDv5FFyLOxchbPKGYVDOMeWjLQ2x3T-ahqzOC7MmXzjswNmLkbHq75u-MkVHi94yvJNMsJCpPo24LY9KobSER9yQkBhDa0irlkvhCTAy1Tp7aT_uwGbqE1z_Cd5UDdlrQxRS24ISUI3HdNsKmOg8WjKvvfNqlMA-wNuvbwi8pHpLyBrhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCm-pqIgQnkYEMxvrA3VGaVbReALBtkfkZD6Y9orUsJYcUcNnMu59mzzwSFIOpQYl-62xygH0rHDfOEp7-mjXRbkwfDzmjjstRGMw5QNNGcqSFXrGssIvgw4LPL-_H6ZR8bT9-N9M9Kke64w0rp9jXB5TkgqV2iF_fGZHNn5FTVGz2dtv621ac_ZyV1WLvfaUjLKuM6vteQWwABTBfENHWIPJEeSBdHn8f8EU8IEAxJ6zgyMLmJJN011RPkbkdvIK0a8CH66O2P9bA6Z31WWsew8YaLtjSs5y3wntLQc6CxVcuIbytF6rMwqgLgXadFattvgdgS_GZIhd3Jv7ZY7Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJo8Dx-DTRvBwhWLCiWBgMyCMOUA2iKppYeR1nb4kgz3Jql5g_1QV7Ev2E9feAtxncErFTPJIUrOUYJ9ByvZYvOqAkk32eIOCx0DgoMdah6WWG702RJNBZXeWTG5sq-x0Srn9WfKGEKKbN6_4ylZkEhl-Y3_1ObFrbIz0CI3yWmJthSdLBCJNJ-njiYhzFVV8F7fxdzmxc7VVijI7M8H2h5TUDk6e51cffZH4EmLxN0vXdH4bcV5WusVRty25bNtJBQspLehsVvyC6nxd8H3_cwNmSy93Du-Y5o-JMm7sGh6Op5D-zWEb4p9gNwc0ZBbZOxyj3p81IPNdzgDw8Hp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=fny6FaWqY-mx62RqmEewwvg3clD_mgcrzSJomPtOx_eHvT1LEQiQr_9QDBQAnCMaTEJGKDk91LuZf9C7BdF76CbMJQczmPtmb-LWML1n6qJehBi9ARDnU73DGnFl7YaShHmMMZP0AU3lpe3hBHVdbdYMZt2yuii0oHFcZAOXlYW_IPsxixa3WPYDFvQj_B4sv-FEWib5K_534pojYQYrPM9v8HJoI7gvaNT5IK9byK8eH7HOsDf1j1pgd_m-dK9hDDvOAzgaapANMUnCDpjCTkLwfzJ3e_C3ZumBvZGS2Y5BweCbiwUZHtpY6_vs_PDAoy9cwUmeiQOPUxJzNOR_Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=fny6FaWqY-mx62RqmEewwvg3clD_mgcrzSJomPtOx_eHvT1LEQiQr_9QDBQAnCMaTEJGKDk91LuZf9C7BdF76CbMJQczmPtmb-LWML1n6qJehBi9ARDnU73DGnFl7YaShHmMMZP0AU3lpe3hBHVdbdYMZt2yuii0oHFcZAOXlYW_IPsxixa3WPYDFvQj_B4sv-FEWib5K_534pojYQYrPM9v8HJoI7gvaNT5IK9byK8eH7HOsDf1j1pgd_m-dK9hDDvOAzgaapANMUnCDpjCTkLwfzJ3e_C3ZumBvZGS2Y5BweCbiwUZHtpY6_vs_PDAoy9cwUmeiQOPUxJzNOR_Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OU-ULyfjxnQqWXYW88GoBNx0NGsYPTgMfxw-U9zbQvqecwQIBR5vEEL0TLVw44iu-q5pjdqMmXaqTV08q7xrIbn1l3y1AtTySVzTHiHyqP2Bbtykr3f0Nd79_KdvDyrsbGpHwA09Rx7efx9ed_ju8ZjYTW00QLOvk_gQG8r7bxn62Bo0pVhFpz_iTrd6VrcCGpAuX-eFlrK6dhb91_UI1v9gneKwjFbnrz5QL1Cczm6J9mea9DNoMHkEPsAWBIuXONWDkqrYTqk6uxWciwD3sOjUrHCKsDedJXgKEdyA9JKP5ahB7-E_lDdB9nQhgQCJtsqa0b-ZVbuCfzofUxXZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OU-ULyfjxnQqWXYW88GoBNx0NGsYPTgMfxw-U9zbQvqecwQIBR5vEEL0TLVw44iu-q5pjdqMmXaqTV08q7xrIbn1l3y1AtTySVzTHiHyqP2Bbtykr3f0Nd79_KdvDyrsbGpHwA09Rx7efx9ed_ju8ZjYTW00QLOvk_gQG8r7bxn62Bo0pVhFpz_iTrd6VrcCGpAuX-eFlrK6dhb91_UI1v9gneKwjFbnrz5QL1Cczm6J9mea9DNoMHkEPsAWBIuXONWDkqrYTqk6uxWciwD3sOjUrHCKsDedJXgKEdyA9JKP5ahB7-E_lDdB9nQhgQCJtsqa0b-ZVbuCfzofUxXZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyIjYc-7qHCiJTwXCWZm8SN9vyauKv2HW1HsuAomlQ48G_aVeTiz3FHxWZ4iDtM1f18lN4Fb7Y2pY00CkA8S7kboe1bb9zQpvlVFSw2fxwX9TELrX6df6G2JOO5oXZMoILWzjkdai3NnF0iCQLEPszqC2dnix2WQCWxSYtvSM6u0dZb2pZ3CA_vz9M6WcM5aXRT9PVdZOphuPDHoa6Vwb-2hNGQ1AWvcICTgcqRAZT64I-__fv21O_XPz1gKGULceuhxQA9vAHpYxOLq2re6X5HtmC3oxWPrTiMpvNXbjvV1GYtph73WwKKiiaJB2vjdQJn4qSeK5XeB85Q0krfEqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RxahKqHg3tUnCcycF7-3dfmHMGlF0zpWcF1dIbAQqDiJx_ryqRPjF7cb0x6WO8zpWrw77c7xnXeR4twR30m_yKRwlAJLsO2sPBEEmSIjzJQlDA8z9hjNjHAbkYaAABoO0TIyFp8kMpup-zSoC-3Bklc5kWbxzj1uSibbX0EyxD30vKKFmhQF6Nlb7ccXVUMIjkB79SRr06yf_Jq2VzyB4ePv2P4t8bPiHhG461o53Z5I3Zc4Djg0tCvadqoexV_xUeKv51pK_E8ggEmIW_-wlvfUfBYsVhFpgxAiwb4pjxZq6pq2nKWHoEEp3P0Ss5eP-oeBtO555aSCFrocE_vxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xf9x744sUW-ytXIK-dYY9fuvbkgz11Q3sQrlXUbnsY4CDIjkcEjFoNRx6SzqJQ0sCCWl29HAWJg7SwWQ7HJUrI5qoifRTSLPkxmkBvZBzjq1cHgYwdS5LAwrdeYTI1JLbI3miGxPMacEu73J6lKS91ZpiG5GNNU8DBaRv8djb19IwalGzB7MNCy-OPchk4xcQrJMqubmmBgqUhGXiNkdlJ0U85u3uwMNsbjKC-jeq4zDwGi6PUXLJh86wDT_bKU42e7xl9xAKfpXMQPBbdANLs3aVVVoGEfS1xlCrXRbnxa0ooK-01GspvUO0WZRRlfyQJgWSa7Ev1id7T209VJ-SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=h7kNg3N5TY6GjTGw9-IBzp895BX9CfM_lm50ATHfykObni6VyI9kswAuOeSquG_Iufdf6dMq_-OUswWARb9olyB09N0r3StwJsAH4-iY4TV8M0VCAGck4RZlLWYtxOxmN2kJg32qVvkcDO7DO3MuObHnQOm8gUshUMZUa1r5V6GtnsSyjAX3uJg25fTC2WHK4QyGTgo9cnagOFxipwSNHpBt7TIe9cXK2tl7xJUZHTDPqTR65PVGvcoJVFxd_qronHMpiI-r5L1dwTftskFNz_IM5Bc5xmc3GlN2Y7F-L05cQ-ExUGu6Au_QSZx50ieo7WbV3TduVwQhttZNNuSh1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=h7kNg3N5TY6GjTGw9-IBzp895BX9CfM_lm50ATHfykObni6VyI9kswAuOeSquG_Iufdf6dMq_-OUswWARb9olyB09N0r3StwJsAH4-iY4TV8M0VCAGck4RZlLWYtxOxmN2kJg32qVvkcDO7DO3MuObHnQOm8gUshUMZUa1r5V6GtnsSyjAX3uJg25fTC2WHK4QyGTgo9cnagOFxipwSNHpBt7TIe9cXK2tl7xJUZHTDPqTR65PVGvcoJVFxd_qronHMpiI-r5L1dwTftskFNz_IM5Bc5xmc3GlN2Y7F-L05cQ-ExUGu6Au_QSZx50ieo7WbV3TduVwQhttZNNuSh1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckZ2s-KxUPmnJ9qhdk-iJzUdaDu7dw_m-U1N3IdcYsr6tMdCPZ6PHRHSQXVHtmWW2XkIMR7_aVnm5xDmztCm5CQ4xhOayuGfMlawuQDU5RUuOGpEpk4YVErPgurJUPFs05MUJfcvNg97ZXefnlD13as2Ub63GCLoWKcNbHjabNvwzSFCX_ZfqqXPH7i_0UqOnp9VeQSbnUXLBEyeMpo-xBmHjRW4WEBSvqS5x1X9hg-Hvec1sfo4vWhooznKfnUNm26cZTSoFhgpwipT7X6AAivTkrbmFZKLS8xqIat8GW2oNG4aDKkaEDxPKQe9Bde747u-uNfeXYWARnhOIWKKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O33AQGVxnsvpo2rk63K7fVxEm66VDad4DgI5ZKDvUjBStiK_jo5EfQcsAid3_g_E_wlssyCmh52RYnvighMHwxG46xDtinCG4IEz4PI4CgkS3syWZjgbly3BxSHFZUx_4b5vJyVD_Z6OdcvdNCLuVUm63Vw26mgLQEVPbTbwBst0QaCTxpLtfxii8zsuwr2_vvEOqK_psAa3RV2OtT3F49NKNzzYfnrEPuK0dutK9WINCbKe35R8NW1pwRXcJBZKzU5iLdVoY-39zmicLWnngUtnp1PgvQiU7_K2x2ZUFMFm20aChtKHT656mhKPPOxSs2JQnadxGtGh3eUFWz09SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESVej1ec8BAMeU_2i8Oca3LjUfsM3rRG_fmGod9eXX-KpD4bAZnpFo88ZAtpORWGjniZFDTKcWBruwOEO1m2ZSjbMjPLfAx6MuOECoGj9nj-fXrGoRdOwxxc3XxxXsEvWz4VVE7Fz09d09HbL6ruKCiXVg3dLbwH_AqaDRJGNEsnRbH7KGbXav9DrYLsD7I3RvmC_2MeE51hTQhrc5njvff-jpL-TTyD10_NsIK6BPMAVyms_pOJzV-8bumal3kxvzvyyUjO48gNKGQHmR3ZhdIu3T7mxVQbTPnRTmsfiq6KFX76g_4wkLw9FgnJz4bnP3C0qxk2ldJ2d4Vh3ZAl5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOORsFSHpmFgTCL8HYkM4Yby0NJ2uyYKkOh18pAPcUBnvB3hL9Puc4Xbi_FNJWzVf5WMb92skjORyq7IUcocCSMdEUy4sz_0T-6O1LQDM4SM987eDBLCvQUOeYDaxlariusz0oItklW-C4EU7fYNpis6CflGzjq9AbiL-CqgeHaehDpC-7OCYslOwK9c97k8_-5ipmI6M-tHZ3ZzyiyfQ9C7nY72JfWQnuOC7wUmdx_3ffrsxnCchtOeCk-TRth4r9vFX00a5U57KRhC3_lJ1nD_qNVz7CuyHZEq8aXOycipv63VfDeF34NTjGuMIueO5k1wiuFvJfyWaC1hSm2klg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Cu9t_0tfkY0jYo5UUs2kf8R_VR5iM4yiSd_DLsUNW3QBh9bayHA0ZYAr5q9Msv24f14VcSvaby275Y9Bs9pb7hPS_g3q45IPk2J3ENBJwdK0olWhcfJAYs-nsGvUzOzJuoTO_T6BvlONJmXHbQv3zeZESWf2h1HVb5orqH6mB4JXTxVmYuocrdhY3Y6MtsPuRW1g0cuf9Afnc5VaM36Dy7Ij879p6Zeagc_mu7-ipulsV_S5e4u-kp5HBdmgebxdwKCL7d0ljv6J2O59km43xvgq31ngBsXNxI8WPB58Cn1Nmm-JO3WIRjJbYNPRa6Asht8lfb1n5RdUJmeZRt6fbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Cu9t_0tfkY0jYo5UUs2kf8R_VR5iM4yiSd_DLsUNW3QBh9bayHA0ZYAr5q9Msv24f14VcSvaby275Y9Bs9pb7hPS_g3q45IPk2J3ENBJwdK0olWhcfJAYs-nsGvUzOzJuoTO_T6BvlONJmXHbQv3zeZESWf2h1HVb5orqH6mB4JXTxVmYuocrdhY3Y6MtsPuRW1g0cuf9Afnc5VaM36Dy7Ij879p6Zeagc_mu7-ipulsV_S5e4u-kp5HBdmgebxdwKCL7d0ljv6J2O59km43xvgq31ngBsXNxI8WPB58Cn1Nmm-JO3WIRjJbYNPRa6Asht8lfb1n5RdUJmeZRt6fbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFmtjECvy9goRlGhiB3IaYWe-Fg7aMytcW7ZiiZyf_g2ju0xf4OJnkSJjqq3KCHu0I0qzqBbfcG5NqoUZjNa8nRTxvgcakKqK0r51DUyxOiw0qScarzPlqZkLp53fWxbpjJzRZnTnOfYmGIsX24DGDA1UlVQuOgtkvSIuJG6TYaXMRaHRJy6x20vS7q6fiFl2zK2G-pt-0PGsCL0rbcazBG2z6WFZmzCbm4hqnRFGTSxth053Y3PSiZoul_5EII4r8lpiGsElEyb2VOWMf5VjAAZ02BwcbsFI5_AjEE3ferrJYRezMqNvkh1yepNJBf8qNNSPH7fkUYl4DuyLgQ45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIZOvMD7DTeurQ_9B-JhOX0RMeeSKx3V1ZkEkdEdCf6roDLeGEK_-GGjF4bjkH5iuipf5_MoCzjvGAlvlZnp3yVPKKyMoy6CF3g0NDPd7DhrM7o2MZkbkFJB00u19csuYPjXP4HJiGbGrM__kZLpoBeWZupWDZbKzGON89WJiVBgiq1NEAPQI5wTalddLZcqPjifh9xyrXV_p9RWftuuhXguNTW7XJtTyBWqNLDbtXIEJiNxKVm1iPCXjAXDhElyIAjHhqUkpYa4ifiIDp5GxZ0K-WV0d30QsC0w1RaQcDosci_VAE1GSkfV0dPGwf6dG7zpzoNoVsOZOK12kLAqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPi9YJa9jhhe_eTP_GzvFnvidN-njBMv5zEGtcPt4IufCHX2DXi70NwlTMPxIXoDutVM9eWTVLHDcCIC74gNKZTMNsJTweKRCU4xQdatPZDi_V5aRSmZHzz-fVzhSSXgOVk97gSiBL5CSIU_lQxhwobj6VNd8oJJoUTjO87yEfdI9e5WTSEocY6ZBHfSU_gPpJnfZ22I65cyqUx4vI93VNTm8Oemuws4Ke-G8I0vyEtl-Nu2kUwlDNnHnRPW2KQq0IVwZP5WM6srMLZZE1t8VUqbfFGyYz2sWxto6QN-2nMT0meoNZ6pDxlPlIHXLMIDbIUnl07KLnR5Z6Kqb9V3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=MePmQXZmaFZznRnDPElBeUfd3YM4lGSb3O18YAbmRvzYLGlv4ZiVGQZMvZBS6AqeMqXjHaiC10tTbdJfHbAiScl4CsyW0jCCnVpq8JB8K5A-ChBF_m6T_2JWIDIy3FcS1qFe3bykNAHqXXgRv2GbYrimf6yI2tnT9dbc-GSSBN5L0WMGLlF9TxBLH3XigkTWbVaniEGyv9n_QOoXOmS4fyt4U33792swck7gopc7CKp_3E1DemWjWCJSQD_5Xoj5QA1ZqvlONu0SyRCvaKz2PMtuFHp7i9N7dBGOq7oEpS6tPb4zuN73RFrL0-6ayEwjPqlrnkyhJElDa7vHYYkXeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=MePmQXZmaFZznRnDPElBeUfd3YM4lGSb3O18YAbmRvzYLGlv4ZiVGQZMvZBS6AqeMqXjHaiC10tTbdJfHbAiScl4CsyW0jCCnVpq8JB8K5A-ChBF_m6T_2JWIDIy3FcS1qFe3bykNAHqXXgRv2GbYrimf6yI2tnT9dbc-GSSBN5L0WMGLlF9TxBLH3XigkTWbVaniEGyv9n_QOoXOmS4fyt4U33792swck7gopc7CKp_3E1DemWjWCJSQD_5Xoj5QA1ZqvlONu0SyRCvaKz2PMtuFHp7i9N7dBGOq7oEpS6tPb4zuN73RFrL0-6ayEwjPqlrnkyhJElDa7vHYYkXeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=agJ45Bnj4auqi2sS9-CJYe5YxXvV_eDTO7fGif5DQlJUJSQ3CUJvoo0MinUWxfvN21InRuhTnTnFhcXFF4C0pIbfpzkIpxpc9RnWOKt5e65uYu_Js_dpLxwEGufsa16iEc6iNRjrmO96sPE3ujlwkS-JebAhP4VHYXZRaYaqko7XHEY1KXqOPISLn8ixQ0pazVSRWmRXpBcYiMHysijXciAjHL7fKIeBQ7LHxVIIRBgXFTzPvqRlSb2-LKqzMG0GJLjVneJwFZeT4YUb1M9ZT6B9Rvlw1qgae5IUSV-OGuekrYzZ_8-wkKcCV4bMgiWL-7aIGYUk7V5XgFbaF72GeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=agJ45Bnj4auqi2sS9-CJYe5YxXvV_eDTO7fGif5DQlJUJSQ3CUJvoo0MinUWxfvN21InRuhTnTnFhcXFF4C0pIbfpzkIpxpc9RnWOKt5e65uYu_Js_dpLxwEGufsa16iEc6iNRjrmO96sPE3ujlwkS-JebAhP4VHYXZRaYaqko7XHEY1KXqOPISLn8ixQ0pazVSRWmRXpBcYiMHysijXciAjHL7fKIeBQ7LHxVIIRBgXFTzPvqRlSb2-LKqzMG0GJLjVneJwFZeT4YUb1M9ZT6B9Rvlw1qgae5IUSV-OGuekrYzZ_8-wkKcCV4bMgiWL-7aIGYUk7V5XgFbaF72GeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=R0QsqC-QBABhSNdB3JqvvMm7y_FnFb7uV8dqO1xdT5aPcoSdkp2VuDTfuJgL_fs8B_ZqOAEXt7m7MGHMNiSty5TwgJ3KY55-JmlRwGfmWPqpR1bffPcAusRQn9KI2Tqk1lJsotuzlFd6i7OeH0J-Z2NPYAtooyTzmdu6vrToQj2qSxcs7O8q0Y_4gbzVla87p_0chVefG3vspElDsA6buxHfN_1s1t5eATa4iI12O4nQ6_QrxZE1QaRj6qKcbZLYwfJAxpg6PLSJ0G_YIxKSAYrMQ7LPDReKM2Xprqqenj0HaMg2L0rRRf15DvoxJwucPqUAmiVlM9_QGkJBYqzReA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=R0QsqC-QBABhSNdB3JqvvMm7y_FnFb7uV8dqO1xdT5aPcoSdkp2VuDTfuJgL_fs8B_ZqOAEXt7m7MGHMNiSty5TwgJ3KY55-JmlRwGfmWPqpR1bffPcAusRQn9KI2Tqk1lJsotuzlFd6i7OeH0J-Z2NPYAtooyTzmdu6vrToQj2qSxcs7O8q0Y_4gbzVla87p_0chVefG3vspElDsA6buxHfN_1s1t5eATa4iI12O4nQ6_QrxZE1QaRj6qKcbZLYwfJAxpg6PLSJ0G_YIxKSAYrMQ7LPDReKM2Xprqqenj0HaMg2L0rRRf15DvoxJwucPqUAmiVlM9_QGkJBYqzReA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBMwLp9rfhlAt9DpfNEFLB-yFG9se8WsziLmy6Z098Zd9DiDLW5S2jA7SNhgWDJdRRyPttW-5kL9nKgcUZWmQ8SdLZEZp3PcGsfn8FS1u8ICTLT5057zRV8Us8PvXpFaSwCUWfyWuu76Cu9qkbdXNN68H6TIsMEj8ff5XMfjYUvLIO6jag-YVP3Mykk6p4r-GLEizGhayUztiiq9ryfWb6S8QCZUoL0ubQG8j5WDMjZc0JG9TAR9AuuXvjHljUEB8b281sc7buDH6PWWiY7vp4Ml_ATMWdurcuKr2r_Jd9w4f0t0BaHT1K-TT7pySbZHSADt1GHwI41J9O9VeLFV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_07Gj72hETYt6jTufASXJEagvQH1jkK56tXcNCTGZt2ZWbiejZIrYo4HA0CaL5KQtM8O-yz0L3DWGeuUppleE-T7jKQYHRqxNMOFUz1P91JzQ3xg9i43Hbb-fxjR_nDno86JsjZz5bhvcvFYr0g998_dLsRu3V9VF0bknOWI-CNuhvwAIaYn_AlnkuLj_buRHT5sWW3jJLPHnWQb29CJxzt0Dy92TYcH7tZvzvCbYxnufhZtT6Lh0O2HazKfdTwDkVmW7EE3PIXl2SIx9TlcVrbXtOVYhnN94EHIsurRZMHyJfZwYpF88H97H8LytVRH_C0WTfToTw1kjHB-BxSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njwcIz54dDpiV6UmCY7ezNpZWmz408zvseYDSP6VeA5Ne2OJbjzD3Sl3wOrD4_hcLmMf14CS7AHujhEMboFw2F2aO8JAVxdE8Wu72ds6bCSQaqOiu-4R-1Z_4shvc2UoFPjFlj_nNDCuI2xHqWTczaEJ3YM2WZ3mhwiuyRHWDOjw2EIbMBLza1msdzIHYC2zz3ztRrDQ5Ffw0SBsmQ8AbQitiYGGzieYEJWnweWs2aqKUC3jao8eUhvLc4zqPyg-rkWyG_P8X4XhhElLHJuSLQXIGp7jJcovkdgtAGB0n5JbCklUMY4_fS4VhiHQX1L1V0A5aVfGYh7U4870vk7gsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOJinGjQOONlFzDLuXf5E2-pNBnAZBoQBWHJaPgXLpoKtWDUd4SAN2HIxaxpk4v5EKVBi7nOlrV62xw_EgPngERx_9KUfetOrfO7z-hBzAqPR8sV3iNu8XJ99Dxb7eak4bpDCI8D9i5J3ixHxGa2lhVIjI4U763ul6TZ7e-GtuXV1jQHdw0Ie3tViouxQ5dyHuP21OKAHzqgPHCxL6W5oijV6LeDf-TpNsMa7ovMNTg0AdJlax4M__a2c1KBj8FkarS8MrL6NwZJKvbNRbavzZEAuoqKNCmPjNU0dE4uQ65_sy69-RdtFc1Jwja30x3X-gdRhOl-dQUIt1jNVYHI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOwGnccNZCHnfW5Sq7FClCs2MKnTdkyODW_UOJFSnHq_2PYRBFQwOI-SWiEyLziMlxn4xnP3oYqmXnkdOMwhipW6e-29i5hIPCbVfZ0dDWNWSWnHaX4T3Gok2WRSwdq5d6Gft0eGJvh8j9AsYOe2TMeBhTYO_YVgJ0LARHo98_vUwD3J0Qifke-4zg0BQhN2Fx3NHb3Z2bZR8GpKYxkEl1pOi9rki-hZmXdgugtDNGX_sE94jCEUwBQy11THl8AXz7Yqiy9nsY4O5An21sEDd-jogXEysLcKsxEzCbNCJwBDtzlHqO4Ls0r2ZAr0DMxvBWl4jN0KSq6hgIhuylP_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGXS_bwyIopowoFI7XDQkyOTZZZOwOKZy86rsXTNjA2VlRlUFjnhYqSmyw1QL-i2fk2--KoCgY41qXV8whFswktjWon_61mPA1E0ql8fuVrKXgD5jnEAP44pXN4sX_jtx8JdziwKrES0hlXRLQDweakTPT7cOU2V-7kgbav6excIzFEyV3wLjKkY8PQZgxuOddvVviz-3fWcmvsphRmkX9yBxTV8Wu_nlVF_CPqSyAff_cNf5M-ATXlNrwAWu7DMK-WsvyIXfTrK-xP6W8s43Kcz8XLniSC58Wj7lXd6WJ2NBZekV6hyfguz0uFy3ynhjaxes8yzj-y-2ZrnHA61kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/maNwXYnbi_lD7YTVMOeKtGXKIcCrCILkbCeobySAsITRe72K_Nv0HkrNjZQgWhunJBeARW6rh0mWhZ2jdHTVXXbB8xJSptz3yYhnc7hCA9hhGLiriuBlMgLmpwxgiVcSbMHR2zg4V_HRYuKO9njfaYOTMsOJXRZxLbih4WpVGVIpR2fes9o-LdKdOZcLRww6KqiAY5JwPQ7Dxk0ccZn8jwqdgoJh9UxCYuX7VS7VYxx1VuASzwt6WlZhfcRB7L1QzhxERGrFRxVLplb7oJ6XH3R8OhR70GyyogfBsRapme88PZov8nrL0C8jtygU-SDFe7mgT2pMySwBZTNgVY97nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q21UmmYYy6pPnJPxkroES7ZclTBgkIScsR5ETmr336e7j-4whSRiiA2Bj0WdlOUyCdxwCREyNMWCxQsBO2XZ8bk_gquZ1qN1TeQ-qkJm7TotTCZ53XhL0PC8-HNMLBZYi8JMogOCSYHC-IdE9fEKj6rvpQckKx81D124z71bK5C6qZKTaXpvJD8Sd8-IZHrw7H1Wg_n-aTgMrkiIamEtPwrgn23DSwAEORSSHod4iMg4BXjwxIEJhJK-PSzyWwSLMKl58Zz5NzUTt3ZccD7eBAUFKDIGsS6CtNbOm-OQn3T4D9_V1jlyaNHH2SFVWmElp-k-x43fOe7VAy3Kj_z93Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvazti1jroD3vVaZgaeP2hBD-WRXdbXDhAPKmTB7p-d_OWU4rX5OjUGmOlb5sB1DHEtt9-vM83ty-LcM3tKSowchKl06JNjRObnAwI5ZI71ascDn2YgS5qklrQ-hv1yswrYWqKuisiYYX18yzjsxgtC13ogy0-gs5m_WmtjHALoC_BaX1Q7v_Uk6FjG9ZHZpwcBXRrLCQu6gDQWbt0qNuSheaO2wW6XmOPb3dM2Zv1JRRAbOw-sy11t5NwnnBJyG1P6C-9S8KIGwSrB2lproYTUIx8p3JzabdQBTs19zmtLoieW1mNVeRzyeiaKaYKBmzFqCgK5Z7MScqHqdnKsU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glQQExFTd8crEOAi9YprZWlvSpCI2sB7U0CbDo29Fr3FxpOAF1jjCL1h6-tgAju7_fA1RqVTEvoaQLhaQcdlRociJWn9QP_dEcA8iST5mK410x4DVwCTyZshHEsMEqiy5vojHM_utn0P50l8q3yGG22cFeDxeyDlaylDoYrJtiLAfeSB6inLJUjbeRlE4LEvzlpAK6ZzsV5nu4SG2sCtaJUNMTYe8hcNKxUAddmoRViLUUo4-zSeSot8DoY5OefElUTZYJwVM_ImsWDR-bP37dtq36H0GcUaKnPRZMYfVH-p-7Z2tSYLZ653DTvf9jmAKQY3HdGcVk_Y91FH3mcUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FORR_Dw0lM5XdioXbXr5AuDmyqhwAG9L5gOrsnXa9A9AfvoxEid6_6aA9tth3hiF5Jsziuh8ApD0cyqovVcVni_H9A6ehsyv00AvALQ3hvHWwifHendBJE7RBA6vPeyXeHn4D7gu_IDtu8NtMFdiiBAZDzFZ7OnyA15Mn-coowhVBI9MNnddky3VgDY933gwjsHUPnWslorSRm2v5gIWaLncA6t6xNA02k6Irnj-b-HxkAXnpUauMu6GCst3qUH-aNMUKwDo8fsAEjvkDkvQ6kzN--FBPlxLRfVnHXRC2cKNJY8CGFWWQCSCPZ7JE_F-uZBkqlpVZlWk50MA3dkJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFZ65kguz7icGG1lL0_PV-PBSCXGXfw3dyAkqybGpFUNq5mLjVvKuWpaNqI73Ul5IV0hS9m7X2rhg5ntPd3I8iPbqNdqdqP31lTSsSIstZpc9vkPeFexbnJ_CQkAbbG8FD6rpFZeYA8A_DhfYf5MtrwVzNpYzJN6gTfZiMGEXaJLQcrC8iyV-Ym4g6IeQDQ6lLzJcPUu9XBGpfyr1BZWlrbN_RrD1RPw_NuCk-U1ZIRrJdG9BFQzleDBpPeuH6uD7P6SuTSgnON7e7TqLsvcGqcq-2pskpiswOR-x2Cgnz6eS5rRsuFkIKNntsfLierhLkjssb3qcMXxgS2Iw_4l0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bqfb4NsbSY0FjiJJIjfjg0hz99IuqACDjoz3wJuKSTDGONBaLpnvwRcEubkvRNJ1FTXj_EXCUQbbhJYp1WGjzH-BdjWvSbSBtC8xMdqKQD3KQ3A6p2cEDc2yZ19_tTYJx47U3AEcnp8T_d8DQeMxKV6NqHXPX5YEWBCqwp0BzCV4CEZQmbupURzXlkq6BnuFHCPI6xoeQJW_illDisvkqizup1PTDI5c7fKXA7q2okPA71I7AOJMAaMq6UgJVJakYgfU24DdaRXjVr0Js-kXG0d91jbAqq4bY9yKBmcr0QJiMx3cBMoOyrqj6T72SYJ69nWpS40i345UPv6MUnejcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6YdXx_SnvMA3ezu8daqZs7zYvvNVDo8QSstC8_smJaMiYCsQ-6Dzvwh496GFVpoC9Xl6TgxOFUUPc9u7p06axuxOMteE2jy00HcBA5_sPShYwDHZztyC0saTeE479L-9Uld8fHXN3qcljfCLcUthjat92KboyI0KgFqCO-AapGtWB3KF1hDryNInuPk7xZMlRPsVT2PTzvMKAZRrMWXIRoSk8zZIv53rJi_lOdpgMzBtXE58ukd3eQb-DU4vVYmd5-synBhaTmeEEa9h-2z5wUiUW6jpMJcuS-FBWVlvLdHLL6Di5G066KcYyW6ryuyNci-6ZVQrAN64WfD95B8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4e3xSu0TE10c9ofST0dVmQ44_zqAdNpIdbmIYBBGuLc-lv9zIAVlzh8bxXsZDA7wLdNDtSA4o0BoBcv1F7lxT1s7EDQaI5hjSsxUyhpnZsz0UMsswvW4zyUA2IMtLiUQ3ZvHyIg11dpEponjEnPEF4DCLlV-9Dj5uwggpctYft5N5gFFIWFCi_2kO2l7hSMFsyrqBkrHevQJ9pMaSGFbqTZcJQgNoh0NXwta8ZtkGqMWh85YaYxuRab4pIL5UTl9GhvBnpVI7AzKygj8WESXWmfkoguQCQyE1n4zyFh0D_yxvWt1LGYrhx40usBHrY62waiptVF3o-3CKGIpXnm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=AA4l4DgLBop2irBJjG_IYICgNZ47H1IA-vS75hs81Aup0cOMTbhbfs7L7BAUGCIu8W1RpFEBjKn9JRIABiEMf9Q10Ad761yNA6Q7hEtChH-qlba97RU7-JQ14v5oyOyi0AjQprwj8W1MasQJUDCsQp7y8kaYfH6UCt_TZs5lLhIitr4Sqe5ltEqwYHPcDqXuLbVlHa4YIofV2lyI1JGv0Q-82SYjnOk6o0FHgnLBfuZMnYkfpimWNlUSJnlWdbp9HGKMmV5HoOQiu0nI2Ws6-qs1lj_alMyMxUoph9yEgIkfzjylWH6w2gebLNep1FWIc3D20UIGt5IusSJkb9SkTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=AA4l4DgLBop2irBJjG_IYICgNZ47H1IA-vS75hs81Aup0cOMTbhbfs7L7BAUGCIu8W1RpFEBjKn9JRIABiEMf9Q10Ad761yNA6Q7hEtChH-qlba97RU7-JQ14v5oyOyi0AjQprwj8W1MasQJUDCsQp7y8kaYfH6UCt_TZs5lLhIitr4Sqe5ltEqwYHPcDqXuLbVlHa4YIofV2lyI1JGv0Q-82SYjnOk6o0FHgnLBfuZMnYkfpimWNlUSJnlWdbp9HGKMmV5HoOQiu0nI2Ws6-qs1lj_alMyMxUoph9yEgIkfzjylWH6w2gebLNep1FWIc3D20UIGt5IusSJkb9SkTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVd6ULCyL9DY527anh1B2CPUDY-ZIxyac1TYqTzfzBSf3O2HhAWR4u-N7H19euYDpIDDM26S7aOzJzY1Cu84Vi2QloAFjaNQV5XOK2DKWp7Xwws1LHHBsSlQ9M2hgop0MGsIdyXZEuuRQCteStsV6Sa6lg5urF-uvZWvTBSy2L-8kkH-lVlkIgsosjdgTAXJfR3FjRKSe6Kh2ZADrPoElPtx1fklGDqm4lNDZWgni128cQCaE02C8n3siJIdx23eA91lxduyWKEZabHYkapllfd1emwMncAEguIZlxUrfoFnYUce5mwLMA6r0oNzzr5zWDsoeLhUthc31-F74V88Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=jViaNBHfBQfmna3qi5UvMe0_isVxmwPN7ThNBYvgc28hOYp6YfIGRGIDooO2uaz4NMYlm5aXMof-C4RpeQK9ijumufDCbr0cQfC_3C4veW1tj2dMSST4l4DfT2y-AcgPVyeEQYil1apJ7GVoq98BX2dF7yulrLtzuKzGee2Vr2W8wmIdKkRiGMiSO3u_2o7wmRkZUOyLFkWPt_RD8Jn-Sn6lY26xSbTiAHmDV4RzbqwES2pAYV3BraRmMvGbo9haLhg7Kw3fpXQz-iyfB2FyX24jzf3FYKd1RjQfEzvjqC7dKpuqe1EpVbhIqwetf5wLVWGMBw7ZiM6NNmorn6m2Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=jViaNBHfBQfmna3qi5UvMe0_isVxmwPN7ThNBYvgc28hOYp6YfIGRGIDooO2uaz4NMYlm5aXMof-C4RpeQK9ijumufDCbr0cQfC_3C4veW1tj2dMSST4l4DfT2y-AcgPVyeEQYil1apJ7GVoq98BX2dF7yulrLtzuKzGee2Vr2W8wmIdKkRiGMiSO3u_2o7wmRkZUOyLFkWPt_RD8Jn-Sn6lY26xSbTiAHmDV4RzbqwES2pAYV3BraRmMvGbo9haLhg7Kw3fpXQz-iyfB2FyX24jzf3FYKd1RjQfEzvjqC7dKpuqe1EpVbhIqwetf5wLVWGMBw7ZiM6NNmorn6m2Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=QQXsiEKAXD96P1ltmWCxCc8NyuCiOrlwg1Yz0fbxJF33FvjA0Isbe8k1dSnRZntSQkrIOmmbx3OVKuICBQxpnBGK44w6xBMNetQ9GcS2fF8IsyUYTEXEy41M3zlD6N9KvZbsrz7u3JRg8euufpc17T2P3fayhFB1wca99cSqInuiiHRpSMBhRuvZCXE8SxeT235heJ5vwwzCdcW7jw5QyC3zGchjZiHiXj3mdHNOV66O2K5KH9Gy8x1i5Ea7wuLwnvhuqPlO_w9gKcLRh8WIGXxQKr0114ngr7FQwD0gHLHtgiI6cjStpnNKeREBwkX2ib27fdyTXr2zIm3doeQQzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=QQXsiEKAXD96P1ltmWCxCc8NyuCiOrlwg1Yz0fbxJF33FvjA0Isbe8k1dSnRZntSQkrIOmmbx3OVKuICBQxpnBGK44w6xBMNetQ9GcS2fF8IsyUYTEXEy41M3zlD6N9KvZbsrz7u3JRg8euufpc17T2P3fayhFB1wca99cSqInuiiHRpSMBhRuvZCXE8SxeT235heJ5vwwzCdcW7jw5QyC3zGchjZiHiXj3mdHNOV66O2K5KH9Gy8x1i5Ea7wuLwnvhuqPlO_w9gKcLRh8WIGXxQKr0114ngr7FQwD0gHLHtgiI6cjStpnNKeREBwkX2ib27fdyTXr2zIm3doeQQzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwVdL2mw9Y4PpAJoXx0P41XzTvbK_xjs9xAx4J73DAjoLlvF_TH70bCpLBPfQYTufOgTOuym5Ub74tezo3nfu5eSbpTfYyG_2x7DrMQ-7SDtgZGPhjabavt3oSMIYYsyV24K6yoaogARnjVnouTuF0zYjIjeXgnfvO7KeXMAjEwQplzDpn3fKKpi50L5ND8DOXnzN6p2le5jC_yG9ue4UjuJ_2oebnIE6-YmSaU3HfRdIpKv6Kv-3iTymYs2TCFvmHjJH-HN8Z1ASTzFUM6z4vO69hLbf0L1-F7NnTvzJZhcjiBU4Hqp3LZa1Xo7RHebBnpTsV9dKJLH27qkOxG40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=QcrRFdSl80k3uKzC0Bzq8YotUssx_To6Y9AM1au-ZThweErtzNQcLUrdD6Y8Y6bUDdvcA1tNbyd1Ei5xw7-fU14UQNBuHGtsl4WjnLBCHXPyHe3s2pM7r1b6_pHiJ0yniJRfCsl0Ye30ZOXjrXYp0yzQ6N5pmc1hZOY_ckIMgJWL94IgC_EkcvKgWkp27va8etSrtYuYLCWnX1jO1pWtTpnbdyEOzQde0PPdL9wtlLFnt3FyJ9r6frUxXycmYok3MAVojSmepc8kEUnI3B-9KaLA0WSYe2Cm7dMispsJ2bEb4JzN3GCeuIVcPXgAxEUulZGmhLspXfTE_hWl07kGjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=QcrRFdSl80k3uKzC0Bzq8YotUssx_To6Y9AM1au-ZThweErtzNQcLUrdD6Y8Y6bUDdvcA1tNbyd1Ei5xw7-fU14UQNBuHGtsl4WjnLBCHXPyHe3s2pM7r1b6_pHiJ0yniJRfCsl0Ye30ZOXjrXYp0yzQ6N5pmc1hZOY_ckIMgJWL94IgC_EkcvKgWkp27va8etSrtYuYLCWnX1jO1pWtTpnbdyEOzQde0PPdL9wtlLFnt3FyJ9r6frUxXycmYok3MAVojSmepc8kEUnI3B-9KaLA0WSYe2Cm7dMispsJ2bEb4JzN3GCeuIVcPXgAxEUulZGmhLspXfTE_hWl07kGjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjZqI89JBPQQsAyw9BAWZT6_458Pt50B1FJGtyVWOIgJZhBu4Xw69lpZDJpt_NaoEhnLnqGgTNMMi_gtKg6ZRJ5XkCCuoNR1BUB-3yyPjHAG9sPDzU-9hGMyKM0gnVXfBIT9HsHGSj9VXJCNWEtWEJdSCcsLxKpgMTpXm73XgYxR0K_CjtLCJVAgrpz_T4RklfmwNNeA3WTxaAdTGa5uOdmGwvRQv8XEYqQtSt8p68WZZyIX9oiQRAhpw5bEGQ_Yf1kf6GK-WBuB9aJvKuN85HwUH5C46O0ATReqVvSDkorB27TlbkDd-kOFdmjDLybCNZ14fg6lJ48SEHfXnRIe2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pknC-4VyfrxSIQblD7-cxlHGFnAdqiPGAT7veW-y_kNm7ajkVQZIWpOmJPGqjuRh4a-M4_siip-wqjkCqdEvkj25NUWL6lgriP9ROiY_QcuRfhGjEuyi4KVzOTAxkWpCa-Ix7whdunQvvG6HHLYRvlOag_hedcRlMXs0q9RWLsxRs_MZ0JemK4SsP-OHikwpCQFfRlSBrSO92IUh1nJr-Sa9rgPza2G3RS5BLA0KnbQMzfhe23gyFfoVLplt4I3QlT6sa00Nj98rG4GydmOT_4zCx_zpf1hs9jJY1khgXoHs9mG568ZysW170KP5Lf0Ov3pA_QhgE9-epgkRG0vvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_sqPz9-22u5pkd9EVaddtnnH3i_teQbIh-ayt16lWsS6OJJPZcn-Bkwhk15RnboB7Vzh1nvbWGi6bXbokX3Ba-e_V6S8xVRTy5UsaIdsMaQALOh8TrK4HGX5sC1zj17VDBx2d9BqfTW1nIGauiUXbueeWXD2n06PSCcrNllQ91bLAsViKA0JLAFIfBe6HQgeGAryVMvezTqm5WMpX3LBvCGfoD9EhswypnX62iKmjRJKMHoi_MckReB4P_G4gB4xE23wdJDW2yUr6STDFyUagQOGUSpPDogjJCrxBZd29RplpQHCoJ_4KY-0oa8MA_X8znNg6-MiJjgYkWeIEDyuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVUrNrD4lmKTKuIHlGmq0tzOHz72yBsKAjWZN1HM-ZIcgnzoQQ1QM1AFYQqgVZpi0mN9OtYS0ix-w9t2JxG94VdxMupWDhPhHV4DoibnzRJZnlGg4WvgQwwnVzNf0PT9RYBeqwmQMwNnlEtzSOhOh2LMY2ftg9fRLjsikzZ1DsqVxDk8ULnMou5iVD-HbVM-_Jzuf22BWEqSuo5QdaTN_wXhZKogMYz1w-Hfp05ttkngbITwBgdDiqgYp6do46xw0PcyC4iQZpY4vSDPS2_dPaTsbFeBLz9nnjdsC3aZFETYDMxvJOphUQePp6I7eBzOA9_hcL0PxVUyYnPyl4kHPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=LscolGmkAMEUliwMhmJRGgGHI0D4q4scjRFFeM_AS5sgUTVO6h4FC0Ph1shWPwhGHicryyiKAkVSQBdC7KvKvePO00i-kF_98fzbbqKUxkBX6fyxjQ-RxinEXaLURE4LqzT4ze6LRPhIAdBkhDRpxFoN8U1jQ3Ow7qHBHOIde7aORD1erj1xM2nqFAK1Ulcj1ieubb2BMGHMb9sRGuVutoIngJZAyvkbBVxXJdZgoiJBDp85LS9UKZPdK6qW80DZij3ZuS139pP6E8RkLTeO32lQ29E8ddBsLY1vgoXWIaQLfVVIz02_0chxHXYS_hfQ35uAASAoBJpPAEGI3mACmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=LscolGmkAMEUliwMhmJRGgGHI0D4q4scjRFFeM_AS5sgUTVO6h4FC0Ph1shWPwhGHicryyiKAkVSQBdC7KvKvePO00i-kF_98fzbbqKUxkBX6fyxjQ-RxinEXaLURE4LqzT4ze6LRPhIAdBkhDRpxFoN8U1jQ3Ow7qHBHOIde7aORD1erj1xM2nqFAK1Ulcj1ieubb2BMGHMb9sRGuVutoIngJZAyvkbBVxXJdZgoiJBDp85LS9UKZPdK6qW80DZij3ZuS139pP6E8RkLTeO32lQ29E8ddBsLY1vgoXWIaQLfVVIz02_0chxHXYS_hfQ35uAASAoBJpPAEGI3mACmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=IEBdTpL_5Qde9NbhUEaUj9pKuuP39oJd8q9eVQ-mCPCJN35HDezIKORsJkPfFclK7U9nBQA43a7wJeACn3Wtiw_iEUedIbLV5QcXfvImjOHqsH4S_PKkqsoS-6FPdbyEzeUmiD9iRX2Aqj7XRMATtarG-4Pj67lqpmDuAsGtMYUVRhFuWlVPRNcjtYG_piUaAirKAG2B7U-Xdl-XIvWPT4pOpKoRR8BAl0LPue3zyINtEFVCfNmxc3ZqakKr-p4UfDHk5RtuFrmjpkM-S-ebk3xan1geUA7DmGXfwmdjDQac-x-JaMpR6_WbuHn8YtbvE2G_gtiHSYvAj3ZV0s3q7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=IEBdTpL_5Qde9NbhUEaUj9pKuuP39oJd8q9eVQ-mCPCJN35HDezIKORsJkPfFclK7U9nBQA43a7wJeACn3Wtiw_iEUedIbLV5QcXfvImjOHqsH4S_PKkqsoS-6FPdbyEzeUmiD9iRX2Aqj7XRMATtarG-4Pj67lqpmDuAsGtMYUVRhFuWlVPRNcjtYG_piUaAirKAG2B7U-Xdl-XIvWPT4pOpKoRR8BAl0LPue3zyINtEFVCfNmxc3ZqakKr-p4UfDHk5RtuFrmjpkM-S-ebk3xan1geUA7DmGXfwmdjDQac-x-JaMpR6_WbuHn8YtbvE2G_gtiHSYvAj3ZV0s3q7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=PsQp0nj6j_ALGNzQ5m-UqKsuQEQiMg50_RhK2T0Dr3FlfBp74OmazkdEmS5jUc7M_6tpcuC5WF08nQdMDuuOvjFrf2J-eR2rOeTT1fecIsAJ9rcRbp2V7n9HX-OzYDVD-1livzj51fUGvgHF1ITGbx39mvdtNYzd0fRnHFSNIYeZRIcV_Fk-B4YQ_uc6-diiHu3kEpBRnT0-oI53vXHAHsc7dDpGuwVCW_2K0q_3ySi8gWI3p6od2_iVvvZpBC_kpXM22OxLZ8jkkutNgWxnoj2uy04xmdbGI_dDKW7PPverN0Vxxb5NiBAcJpphfSGY--FT1n-ArBFTAeW9VlaXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=PsQp0nj6j_ALGNzQ5m-UqKsuQEQiMg50_RhK2T0Dr3FlfBp74OmazkdEmS5jUc7M_6tpcuC5WF08nQdMDuuOvjFrf2J-eR2rOeTT1fecIsAJ9rcRbp2V7n9HX-OzYDVD-1livzj51fUGvgHF1ITGbx39mvdtNYzd0fRnHFSNIYeZRIcV_Fk-B4YQ_uc6-diiHu3kEpBRnT0-oI53vXHAHsc7dDpGuwVCW_2K0q_3ySi8gWI3p6od2_iVvvZpBC_kpXM22OxLZ8jkkutNgWxnoj2uy04xmdbGI_dDKW7PPverN0Vxxb5NiBAcJpphfSGY--FT1n-ArBFTAeW9VlaXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=CY-avO_0LVidRqZj1n2aSQ5oYE4wAJXy-lGAMix5VEdT8eCl3_i2aq8ZPghhEpnT2yfNI43ZBjOnpZ5MLRhXrWATzJf9fYJ9kxedVoljpmK9yJKTeaqKjWKroFs0hL7O2gtsJHbMiZr_zdpuABdilBFvGE2BB7mpYhszqloeajgwDS746GJZYYrhptYRTMLwx6xm0ReXncUUwJVPYVE97R96ADduyeRI75nUhdKhHsOZSUWH2LNYifpf5NO6bRSj-XqYFzfFLiD89JGvXuXLHJB0ee6MtXX-RcTxga_8ZBvt7i6QrJdprN0MMwKaLPOPmALF5LlnQ-5ZxmjrlXiRwAM1aeO8eMMF1DFtMh0tcWayd1iUyxAFmvZDcxVQjLwoTB0WHvoHr2FhX_R_PrmxSnl8BZa28crGWmAt5iz5YViZMJkDrpRqy0d1B8oHmj07CVaedGTqfH6DYgmXs9bYCUbUCUotSnizZOI-ltxbehI07gCPAxWMIXJzrcmi3sUkLLIJVEzxCp2QuWbwyfmsnFjVS_JPeHneSAsMZZOxPKgTs1xh8Oe0FCKaz5HRxFi1EpSJDbeo5XkVUKZzB8K3Qo4DakJkaosh3sy2krSNKZ7y90Z3nPHRZsopFqI_t2eQ5XVFlhkksHVZq9PK9Fbtq_4UjjPPjWvRi1KAPZg9oWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=CY-avO_0LVidRqZj1n2aSQ5oYE4wAJXy-lGAMix5VEdT8eCl3_i2aq8ZPghhEpnT2yfNI43ZBjOnpZ5MLRhXrWATzJf9fYJ9kxedVoljpmK9yJKTeaqKjWKroFs0hL7O2gtsJHbMiZr_zdpuABdilBFvGE2BB7mpYhszqloeajgwDS746GJZYYrhptYRTMLwx6xm0ReXncUUwJVPYVE97R96ADduyeRI75nUhdKhHsOZSUWH2LNYifpf5NO6bRSj-XqYFzfFLiD89JGvXuXLHJB0ee6MtXX-RcTxga_8ZBvt7i6QrJdprN0MMwKaLPOPmALF5LlnQ-5ZxmjrlXiRwAM1aeO8eMMF1DFtMh0tcWayd1iUyxAFmvZDcxVQjLwoTB0WHvoHr2FhX_R_PrmxSnl8BZa28crGWmAt5iz5YViZMJkDrpRqy0d1B8oHmj07CVaedGTqfH6DYgmXs9bYCUbUCUotSnizZOI-ltxbehI07gCPAxWMIXJzrcmi3sUkLLIJVEzxCp2QuWbwyfmsnFjVS_JPeHneSAsMZZOxPKgTs1xh8Oe0FCKaz5HRxFi1EpSJDbeo5XkVUKZzB8K3Qo4DakJkaosh3sy2krSNKZ7y90Z3nPHRZsopFqI_t2eQ5XVFlhkksHVZq9PK9Fbtq_4UjjPPjWvRi1KAPZg9oWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=NOaC75O9N0laQ4JAMiN7KjFnwfQx7PlZzAzzuEJRUooCI9mIFhPcA2rVZW-Fa-NafcERYbnzopBYi7uH-UywidA9wTuz0E6LRRVgu5M9jU-2_91hBc48DQ1FfIvXAQhU1D9iPFmByddujn-qFHybczQmrP4XUeD_FDaGCc__qHvGEIHjkn-UgXSp19I2lmNgerEgGIj6Z6dv-I3gL8emm8uq-jkdNK_USfURqlY18SJSzb4g79IPgo8E0kCmix689cdGuKcN8BZ3xVP2Fk-Zsh4o0oMRSCmPQXFZWIKPLAj990vsbsWmCO5C2OTRWXQykYBvCOLlgwMoS_7bR-uS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=NOaC75O9N0laQ4JAMiN7KjFnwfQx7PlZzAzzuEJRUooCI9mIFhPcA2rVZW-Fa-NafcERYbnzopBYi7uH-UywidA9wTuz0E6LRRVgu5M9jU-2_91hBc48DQ1FfIvXAQhU1D9iPFmByddujn-qFHybczQmrP4XUeD_FDaGCc__qHvGEIHjkn-UgXSp19I2lmNgerEgGIj6Z6dv-I3gL8emm8uq-jkdNK_USfURqlY18SJSzb4g79IPgo8E0kCmix689cdGuKcN8BZ3xVP2Fk-Zsh4o0oMRSCmPQXFZWIKPLAj990vsbsWmCO5C2OTRWXQykYBvCOLlgwMoS_7bR-uS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ODFrfeBk1Nzl0p-0OPSxO4926fIWcF26vS6qIgQArn0Tltxs5WWxEtdtQceEVZj9n0Z7_9FFQa0_w1EinHwpVtEPUJxlnk5quYlDxRO2FPhqSvByHYeJD9QkeOsmoQB00UyN-gnNaI0b9VXbDVSJKnbUqH-nII5IthPJXJMx20cbcfIvICTIi_HBeMcfzsMDIC1RH0J2aCOMdp3mimXIXx8ODYjIpH9Z73n9T9hSqZTeHRdOHWPOb3BnaRaPGpA_m3Q650prXQvLha3-S1FUjgFca30WEJhT3SJNo9QDyBx5-tzGX5e7kEMNSdSJ_gETKTcq6SFcbojkZtBu3K9H6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=ODFrfeBk1Nzl0p-0OPSxO4926fIWcF26vS6qIgQArn0Tltxs5WWxEtdtQceEVZj9n0Z7_9FFQa0_w1EinHwpVtEPUJxlnk5quYlDxRO2FPhqSvByHYeJD9QkeOsmoQB00UyN-gnNaI0b9VXbDVSJKnbUqH-nII5IthPJXJMx20cbcfIvICTIi_HBeMcfzsMDIC1RH0J2aCOMdp3mimXIXx8ODYjIpH9Z73n9T9hSqZTeHRdOHWPOb3BnaRaPGpA_m3Q650prXQvLha3-S1FUjgFca30WEJhT3SJNo9QDyBx5-tzGX5e7kEMNSdSJ_gETKTcq6SFcbojkZtBu3K9H6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcF9E6yOIVupHiR8vz78S06WD516T4wY3JhKB0uMNogtSWpB8FGg5A-MFwHiIamU-YcOQ4uX5Z-Gkb4vLSBqcIF20mrFo7G0GUaMrLMg-MHy8YYYHJmTEwHJT0m7l60YhUXq4jm_dRIKlL4Otqs3rqdeeGp6BwqXTBSuTid5h62IBLgEKKuBXY6Osxa-iLP1JHRckqtyNi6rVoXGpvrMTuxRJJhvr5qtbcQ8wo-kb8_0i2zFaIqYrGvQGzIdcsg3V99W_lOScms00PqKkFpMo9-C3wMfBRgSP5V5bR16ljejFqx-dX-5cm0HLzgdEiE1-sDGPKbTkZdQ6DlhIqIy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
