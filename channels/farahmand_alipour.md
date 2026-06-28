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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 19:15:55</div>
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
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spomz7bjOu2I5arbglW-35Spx7_PdN3RWptxCq-doJKbFk-6lWPrCZFJn_pYKqr_7UqjGUnpoHTbhGiH8CvaSORrszeWYO24nk2mbK9LU6fyyT12tzRb0PrRPHZZKTbM2bQdxa6wkUB_mK7zZNRuOc68BTROshOtec272ZdhtlBpQas41pZJYVP1V7ozgWZn9jQGVPum47q58-Ho3QVsLc2sa5mz8g2rfYET_ac3A16C-bVldyCEdgeWAclSuZnTLhg1OegTQh0mz-hYlnyUyeTG1LIJ7TBpGBO_bMnGA3peyXFdhT4tURIHzXlpI89bqRNiKVRNGcmdP0YhKTqSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=qC7WbJsM-HparEK7d2OMddB3-LbsXaDp_0vPglcL9_lfsuk_H3TTzzYJYRoLaNa32HaCHRjVD_K1tmg2LqeYED3F_D8yh-p-nQRCi89-i6RAen_3koMNcAhAzl2lXHdCPti6uYErb2YTIzGDvQABkONzlOHO-lkj0ecpnaY-E5E2TgAp8lFGOY8gFxppGUjgrlHxq1tsBLhTg8ZKH1Cy4M9sbxKHclcwalhUZTFXeOmFAaPBYVE2l_Is5BJxsY0C2doiNDgWDR21CrHQTpkfvuzYbGRB-eOcL_oZwUL4EsHZTSLz-jjhElLCy4VTvl2owkfKNVwAaNeitVaNu04zVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=qC7WbJsM-HparEK7d2OMddB3-LbsXaDp_0vPglcL9_lfsuk_H3TTzzYJYRoLaNa32HaCHRjVD_K1tmg2LqeYED3F_D8yh-p-nQRCi89-i6RAen_3koMNcAhAzl2lXHdCPti6uYErb2YTIzGDvQABkONzlOHO-lkj0ecpnaY-E5E2TgAp8lFGOY8gFxppGUjgrlHxq1tsBLhTg8ZKH1Cy4M9sbxKHclcwalhUZTFXeOmFAaPBYVE2l_Is5BJxsY0C2doiNDgWDR21CrHQTpkfvuzYbGRB-eOcL_oZwUL4EsHZTSLz-jjhElLCy4VTvl2owkfKNVwAaNeitVaNu04zVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=T440vcuVGF-QJSp4m9H8mssH0M-Uuk3n7tFN82sJXx42dDKs8UjCLhnoBVCZeNMEp-9totLFGT10HFOchwY7cWFwExTbunidiNhz0bYh0Gci-5Ri5pXFUwg2aE-c464GYy2EnsBCHuC1w6mJOXd0MrapNMDfWTXtbpv12IiyfVJMwQFY53lz8nw8g6nmy6FgH922mVovIu900WhAlAX03MIBbNw-nO2J-ekIJV2ffPpvqRpVxe34_GGq0_UrMj-n8SFplHcfXfr2cKjkFWxqdCHmMI5OrDqHWZgZ1gFDoQydm4QZgErxbbFTolPJCQ9_mCNcHmLrftTEIlP3e12V4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=T440vcuVGF-QJSp4m9H8mssH0M-Uuk3n7tFN82sJXx42dDKs8UjCLhnoBVCZeNMEp-9totLFGT10HFOchwY7cWFwExTbunidiNhz0bYh0Gci-5Ri5pXFUwg2aE-c464GYy2EnsBCHuC1w6mJOXd0MrapNMDfWTXtbpv12IiyfVJMwQFY53lz8nw8g6nmy6FgH922mVovIu900WhAlAX03MIBbNw-nO2J-ekIJV2ffPpvqRpVxe34_GGq0_UrMj-n8SFplHcfXfr2cKjkFWxqdCHmMI5OrDqHWZgZ1gFDoQydm4QZgErxbbFTolPJCQ9_mCNcHmLrftTEIlP3e12V4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTMIWD1-xdGTqweCeUqag0o1TG4gHj9DxoYn5upoO8hWAmRJD5rU9ukB2Xmm0bE1sdTdsUiTtoU_exALNiA_KjIyTwdGNlrcZ2KSpZWQ1WLrNKTT2qnq-YBJTWOEHUHDFl5uavXT0DjHG25ShvNOc-0txndAC07k69KhLkcVbHvovp8l_WbA5tWhnS4FQgKnCai1wDir0mIugc4PG3fufq9YDmVbdOr0hhym_XBOFBozgSd_KslAlKcldvq401wtMeMp406PyC6YBWxogKKglNhJFeV-DNzx83ZksFAr6GAZGZPNyBZm8DpxxI89MOU_5DROlUL38TyjxQiF6GBiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzu_btavXw3ZvXCs7ahJmIaW4OCkUBMHDw8qv1BRtXp2yK2flhKuDsxudSyXdnBwvU78UbEJ8mE6Ag7osXRXeVEyc5TEzY7d0LgONr1Cgk4DdxPrinua7QPiPXQvZvci_OXAvx9omeOA9I4-xW-i-cSdTdkFgi0U7BAaDRSYzhMYJX0l0cnQwYznshk9mUUneiHo1EQCOept0TvV1NG-rCG-Vnm5D4N6Z0h_yWqKQZzOM_ko6_0tZVAU93uSKbPVFypYSSBEoeb4kInopCHvT_6Dm911gR9Cn2HpaX1VJmnP7O-5mbdoAvhBjub9gf4thYmElvfZmulIpxfnqKwyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoRCWhwEdH_iBxludJ0gFH_UeZxBfOIbeAhcWsxVUm_7A89uooNsIa7fK4pOATxIA3uQUQqEmmskIf7eXflZBnkYbGuakC61-QjJ9fmEwxyc26t3c1rCp1yf3FVmhZyBSN7lyPLg8krxRUaKlbrEny7QkipzzoxQi5jv7eDkTMxJ3Vicg3r-Vbj2xmV7c1LcQErKQKhv6OhdpNxvmx1Fd4Wfl-H2CbQOz-oyVjT2IwGY48DqtRW_BypUe_tYJ6sft3ckMzUVzSZVBF_ivWtXXUrM54XJpBy93w7o75P4_cvl5YT6-VvpKiBpOGdf9b3_QcfI1w7cc1Wy1N3_0c6LZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K87Mwa-O6RErFSJQgVQlB-LtnCO3WTMXg9wEycCTHwNNE5Tc68Qm2kx8xgNJ_z35l0eAC20o7wecPyzJYPB4ETGRUnRn67h6HKolo_W2kYGxTvIPWhi0j4ku8tnoU3mIlEivnvbexyMzAXaQ1wmh91QQPndcA1UCvIHtNM36JJgDLd1g4JScvFZZt6IpjOwMHPSTYnmJYYeVzeJevs85oFVJjjcWpGNE8u9YApfSm0yb8A-GRNznNqrz7SvCjZY_TqklfYEncKE3JhEf_vDXSGm5bQFVXc5LSBH3IiNQ5WGdriiN778GW9opo4kgMVz2fl3wqgg7yvyybEYTt_B2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=FfoTNj8legPZTKljj3RK7nMlRHIlIVy_JPg97a5JK0woBXY2V690hnwl8ryse_aqrCjv0Tdj8r0a16Pc5WkiRftoJldBmWER5FRVKfkQF007TckzLhlHaMdqC3FbdxyhyOG7kJxOGkUIT44pQ3Cnl-_afGOuUQOBGo0A2ZElAGvK5DrxV7SRv2smLHgICuRUZCTgMG4oSpUQA9xvHWIUThxyljV3-e8AD5XAdO9D5fXruoSPS0k-iC6hsNdDSSX-m4RsahSJ9I1JbN3HG7LxqZa8HsmWCYW3yQVD235N6Dwe0rny35pd9XXXvyUh_PiGLoKRuAYQAhQXOeTImVzTVa5xLl4qjmbXk75iSotNJywEIWQ2mF9FdXlY39yLVLdyVX0w-or0_KKbyCmQOAW5OOTtlDOD6_5tRIm01Nr6M7EbAMpN2a8fxpbbYXrQEQrF2c4JaYeczU2hvNQmZowqXgI-IK9-vnssuD96zLBdPaIiHD_3sQppSTSL9ImEsoIsV4k1dNBA8pLeT0KKI__048O64sCzryp0ZpGlArPpJp36AbcNhwzbesYaW5zSZZsUhVKpf3fux2rDzBoDZJOFL123V9-fX5n4PU1vV5AS2pWa8_6Wgv0wyst5FsyYd9tAH7vbeF1pCFZXlGRM-YV_r5790d1zD4CGHMhEZ5ySM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=FfoTNj8legPZTKljj3RK7nMlRHIlIVy_JPg97a5JK0woBXY2V690hnwl8ryse_aqrCjv0Tdj8r0a16Pc5WkiRftoJldBmWER5FRVKfkQF007TckzLhlHaMdqC3FbdxyhyOG7kJxOGkUIT44pQ3Cnl-_afGOuUQOBGo0A2ZElAGvK5DrxV7SRv2smLHgICuRUZCTgMG4oSpUQA9xvHWIUThxyljV3-e8AD5XAdO9D5fXruoSPS0k-iC6hsNdDSSX-m4RsahSJ9I1JbN3HG7LxqZa8HsmWCYW3yQVD235N6Dwe0rny35pd9XXXvyUh_PiGLoKRuAYQAhQXOeTImVzTVa5xLl4qjmbXk75iSotNJywEIWQ2mF9FdXlY39yLVLdyVX0w-or0_KKbyCmQOAW5OOTtlDOD6_5tRIm01Nr6M7EbAMpN2a8fxpbbYXrQEQrF2c4JaYeczU2hvNQmZowqXgI-IK9-vnssuD96zLBdPaIiHD_3sQppSTSL9ImEsoIsV4k1dNBA8pLeT0KKI__048O64sCzryp0ZpGlArPpJp36AbcNhwzbesYaW5zSZZsUhVKpf3fux2rDzBoDZJOFL123V9-fX5n4PU1vV5AS2pWa8_6Wgv0wyst5FsyYd9tAH7vbeF1pCFZXlGRM-YV_r5790d1zD4CGHMhEZ5ySM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETqrAVk-vkZ42_MlMOS0bkhH_l7TZiAEcV-HuROqKLhPFWSg0MYp2Loo5zlw5_GOva1OJYUqAEVWle9_U6CsWBZaEueeKocN-OhkZ9dBYLmoEknfWXUKf4OvSnsXvAO0FHK16t3oMFUnOqmQswY7PDw7rz6FEKwn4ZkmGLGtNgpL_6pDCWEkDPOOdtTHYPOlKVmUzn0j5uV5qICYzJudDMLDY26-IrURs5dB6YDMyKAj-bJXNhZAL1b67ULmSYRWTMFa2LPtGFRSpnL4p8PrwiLROIpPDFooV-yHIbIwmXId1TX6yuZOBl-1zVuLUXO--Q1Px2oUnGwtH-sAQVc_YOLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETqrAVk-vkZ42_MlMOS0bkhH_l7TZiAEcV-HuROqKLhPFWSg0MYp2Loo5zlw5_GOva1OJYUqAEVWle9_U6CsWBZaEueeKocN-OhkZ9dBYLmoEknfWXUKf4OvSnsXvAO0FHK16t3oMFUnOqmQswY7PDw7rz6FEKwn4ZkmGLGtNgpL_6pDCWEkDPOOdtTHYPOlKVmUzn0j5uV5qICYzJudDMLDY26-IrURs5dB6YDMyKAj-bJXNhZAL1b67ULmSYRWTMFa2LPtGFRSpnL4p8PrwiLROIpPDFooV-yHIbIwmXId1TX6yuZOBl-1zVuLUXO--Q1Px2oUnGwtH-sAQVc_YOLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QeBgfN2TGU3qKLNVv6wS21kn8AbAuEjEom-wvipv0JI9F20WcQvHyse6X_s0nQChswFusfz3msFzOqJFmCWzZgKGb4w7_Oll9gyEme0PsZMRZOFl4wdESY67s1hd6dfnwlj66cuYjnCi4g7GoV2wDny93Yiqq90hL8W8gaJaiyPWcENcQEtCAKlBOJAg6WrABhuGtWe8nRVd2CjsY_Snc-tNfYrV-UyTe5-cEs82sEY0rHeKwv6iaikzGTVEG8FoXsLQYWVV0Mw7L7hlEpe9WNLQuTqZ4s-6gur3yvlOMe_CXWe8c0KLAw5i3f_jAKtdbyx-yDXTQ4JWAgX8n7P51oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QeBgfN2TGU3qKLNVv6wS21kn8AbAuEjEom-wvipv0JI9F20WcQvHyse6X_s0nQChswFusfz3msFzOqJFmCWzZgKGb4w7_Oll9gyEme0PsZMRZOFl4wdESY67s1hd6dfnwlj66cuYjnCi4g7GoV2wDny93Yiqq90hL8W8gaJaiyPWcENcQEtCAKlBOJAg6WrABhuGtWe8nRVd2CjsY_Snc-tNfYrV-UyTe5-cEs82sEY0rHeKwv6iaikzGTVEG8FoXsLQYWVV0Mw7L7hlEpe9WNLQuTqZ4s-6gur3yvlOMe_CXWe8c0KLAw5i3f_jAKtdbyx-yDXTQ4JWAgX8n7P51oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=vpKOLufO-pWyt3hy1fedeXKvEMjZYYoTpLp2FkcibCeUMVSW8ZvPhN77nE5z1gnR2jWtayHly-NdzEUKgAaUOePDGyiShxd-mEFVjftF1GKuIGzkhWi1g_3ZsyabBbDwrjIBcHtFNAaVzdPYWXJBz1IosJ3MK35CNfsgVqVR3RLLmBh9oYVTWxM3WM3tHVc_HrEs9W8x24KzOJAG_P5I-lbq07WSL95hpcyLdFkH5joqtTvURXfaRBTxWVd3WAM1s7Sy-XrBuKi1vRSKgGj_WC5I4s3vrYIxKo9-aTlq1Bcu6JTuheVnqe9kS94AT4PyE-dgyD8tKLF-Vfus-bQItQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=vpKOLufO-pWyt3hy1fedeXKvEMjZYYoTpLp2FkcibCeUMVSW8ZvPhN77nE5z1gnR2jWtayHly-NdzEUKgAaUOePDGyiShxd-mEFVjftF1GKuIGzkhWi1g_3ZsyabBbDwrjIBcHtFNAaVzdPYWXJBz1IosJ3MK35CNfsgVqVR3RLLmBh9oYVTWxM3WM3tHVc_HrEs9W8x24KzOJAG_P5I-lbq07WSL95hpcyLdFkH5joqtTvURXfaRBTxWVd3WAM1s7Sy-XrBuKi1vRSKgGj_WC5I4s3vrYIxKo9-aTlq1Bcu6JTuheVnqe9kS94AT4PyE-dgyD8tKLF-Vfus-bQItQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bgwn1u0hVcWAPGPGzw0GbzlRyEX6HTXQPLxBSPfc17ewDq5ZxE-Bruf3__jGXiH1RhI0mXl1gtM5r9g1g9hPY8FEtj9itx9vY9ADZRZf2SapQDd4Vd-EKk5jGTUIkm7TdksSASDJ-6n8sIuLIf8ehlh5yRtx63W2FQrL0X_e7zaf-X8mSDwnzVepsL_wv5ja8DJF3i8_E1xbeXUsc82jKLQskDt6V-wwwrPTeZOz5jrofuUfc-L1IHIncT93sYK_GcPQLTttKrAUUh8dzmc1DkS41qidxD8z3IRM2w7Nh5YTa-qfqILeVVFrSwJUG_5BQGVKDKgtpH9AsYN48ONEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYyW2n1lfms5JZMepiLlzxhxVX2PaJkstDSlzdNWhbo1y-LFj5slJDXcqyj-2gFgYh_rDqM87RSiZwjHhTTgnWQ69O67ilHemtEkkusU9783iZO9KwcYklwMXEBdNurZMk2MZJtgId2IKlSumL6RXH8l3FguCHIhoof0988dmTSBdzCTzMA9Q6e-zY-UrPWc00hs7ieOQJLakx6soLDHKDMTk46J6tbAjAqFwZmsJZhb8t6S-S6n_1Uc_FCnuSFkjqf6EmEXt3Lxk2sgqchgCUZaemuean5WjguDkmv12jAXtDoXyAJSqz9sqanPdj1m6jrG8sIWTUWA_5bTqLhqzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCKK4WmZf82fi1wVUXdUqpol_0QK-Sqlz1_DdcH25MCvWKbsFWS4CBY-_6tMa7tt3CsawmzihSb0_lfF4O1pdn91n6Y-nNLBHq0CUmKW8j9x0CcIJV33zSAf_QpmMPwtmSYmWZ9QVqKrL-_bpLYqFZdJAnuq25aOfMPlSgTCUwop7wByDhCFNcmDj3uax9LG1aalmH4Y06VSoNIDo-FTtFuiq67qtel5cXV9Y0OfJlVc2a4b3fzOyj6SG6a9gHyZYx3LI1C9c85txMrnCrJDszy0hkbpAWBG-l3rCpiO3xEYjhEDKyG0ohz68ne9aWWmytrS7D9E3H6Qgrqo3jWiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrnDT3v8bxpe-HPZybQwi6t2QgbRNHCxyY3fnnpnsmiBewA5_GIb550A9nsDZy2IVv90lpomJzsrqH9W66XO5LdxjTyhLNQPTHAJ7MjtAyeCvbQTLEstHz_qDZ4CA94FMklad3SIKP_ke3gjpkrZZmYySnADAd96kN4bcsKBWbXtjAYDrfdvnqqeG2JOTrXCnhKszp0yCrnVNaC4K8hFjhi9MLjJCZLbPHUahYUCV5rB4vE_qTlf1rmT4D5_m71O5FCOiyKH2wspIiQg22jYLOqGM2HQWWQnjzqf3wpTSTiaalSV-s-xAyUbzHOmnI26re6VgkRBqSLJIFHs8qjGoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz4IS8yB2IABGHjaufpynJo7AjPe7t97h2l8p_CH5zwLpk8dvEwMP40AXm87Yy-TCPr9_phoyXeTp6QvMXIgxCly_RGNxiqTydr5MjDSlD98ByCHpnMzMPmjFAFmAEYcZlkJ2atGhQL55m8yrA-zP2aAo7MTK3pdWUNFtrhekssKfyvub4yE9RtZnRqPfQyss6vnGrIdGBvZyRb0kJ-Fm8wRdDkbgUgEG_7b1HN5md15kO1pmTF2uBBsuQN0j2bzlNlXwtnVGHHjLsjfKM7JggMjZks943ql70KTesB_-376pjJSlWEcGA7sXkoRvAaXLC_bZIO0ze_DLpWfRsNJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=tt7Pcnck7HwJQvAejqBkEvliwrIW3W7OmFwQWjtDtxZuaymTUEhNYZEMdrjJmOiA_ZodwrO4ojX4JLxYf7B-BIgQdIfNpEPk1tTrvsxlaLUi0gKlm7ZRN1d6AoJzFxFQFoWytXJ2OC_Vlj_znm1wEgOTRL9i4xbrF9RlHoo_tWXEgFffCNLqEQe9MyJPEs_R5absVpvAQCp3S6WmbPgHI2ONcnYh7TEH2tTjYfff8Z0lqXHm7Wd_KtpVIhFUdurPzHaBAG6-v_BbJfzGAddiK0d4ZDnryZApC1KlX4Jj1lQfssP5PsH-uCuaY4OdFMz4kn3Z7pDLCloavO_Bmb_ZYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=tt7Pcnck7HwJQvAejqBkEvliwrIW3W7OmFwQWjtDtxZuaymTUEhNYZEMdrjJmOiA_ZodwrO4ojX4JLxYf7B-BIgQdIfNpEPk1tTrvsxlaLUi0gKlm7ZRN1d6AoJzFxFQFoWytXJ2OC_Vlj_znm1wEgOTRL9i4xbrF9RlHoo_tWXEgFffCNLqEQe9MyJPEs_R5absVpvAQCp3S6WmbPgHI2ONcnYh7TEH2tTjYfff8Z0lqXHm7Wd_KtpVIhFUdurPzHaBAG6-v_BbJfzGAddiK0d4ZDnryZApC1KlX4Jj1lQfssP5PsH-uCuaY4OdFMz4kn3Z7pDLCloavO_Bmb_ZYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=n6VZfxKIoH1_9Is-zGF7n9vKyMGH2XGnwwxlzT5SlHvN3ra7wEtx9qyocknRPjpo4UY3RYdA4ramvfDSl2_5V3IazUr4Zr5SGgUCgYzlqoP4Qr9a1iJPDyw1cd-Lz2bzNZ7ZSDZdmipoaVAVWd7ytw_oQcpOnXe2N1AF1QlRTzsZLNHNT3CH1CHq2iwPZN_-ds7R4NjQ0XdUsIn8NNI_ovtBztxHMyxKnEwzub6UHSWOBPYSvQwjDCHVZaCbhnA7C4XiziN-uExSFf87s2CdFo7RWqt4Dz7vPMCuXesEmEZBegs_bdfbgOnKbC_m4WzZkKXdvoof4c7TFnLs0ws46Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=n6VZfxKIoH1_9Is-zGF7n9vKyMGH2XGnwwxlzT5SlHvN3ra7wEtx9qyocknRPjpo4UY3RYdA4ramvfDSl2_5V3IazUr4Zr5SGgUCgYzlqoP4Qr9a1iJPDyw1cd-Lz2bzNZ7ZSDZdmipoaVAVWd7ytw_oQcpOnXe2N1AF1QlRTzsZLNHNT3CH1CHq2iwPZN_-ds7R4NjQ0XdUsIn8NNI_ovtBztxHMyxKnEwzub6UHSWOBPYSvQwjDCHVZaCbhnA7C4XiziN-uExSFf87s2CdFo7RWqt4Dz7vPMCuXesEmEZBegs_bdfbgOnKbC_m4WzZkKXdvoof4c7TFnLs0ws46Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R80f28_0R8w0Aa9JoBf51cPJHu8iMpgs8WsB0HfVxPRXOErpP9FPP-XueXz7WdWdSSlvSQI1JzjXj1DY3mNz5EqUKRZH9LG-xdse8us8EiwrhdTvC4rCgmzhs3ssDoBZyG_lumDZDcCKEn6rcTrMJbxyQWtSO50fr_bPAz0CihZBSZyOJJ5q7qbgb9VgwOsSwoE2fWpUVEaKSjXA6Xj8Ml05rj_iNk7Ry2pUcz9CZ3EhVlPC6ajjnF_k0Lt2MR2ZwT8n_t_bL3p777vZZY6Cc5HKbCNhJezVl8TP9jUThgzqqT5XIln980_hBbVGZtIwaJiWfF8CQNk3htYGBGJTUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbcgjs4Qf6IRT7Pdut-uJQ4xyPzLBtfvrTnuwns9KvQ3_k3xhRkdt-w65Q04NHuCrOYV6p56xecbS8bEOzPfEYxyuC150_v2y22irGtidNc2DOIiQi8S5x3cr6G_YSMLYfKshNR1U97fFVUBcSxIapxg-c6A6KDMEkrOMbYlin2OSvfa9JTPhSrbDbbk2r9RphvxBPAvXD3eH0G5k3wjnbbOeFBsv0HdUGa3TyG8yFDFPiicQQDBn6RdmmIUu4Lv2bu9ljE_cxK8sAbv5WkgynT9p6r3bZ2x2Ztg1Pb45_-Wo6xwJx07y1Tluw4C4HD00o9SDLjozpKbKPtWRcrr-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=O0vaVkpTjVHuU74Szo7-Z6IIIF_-DwZXI1Uq-sbjVmhFdhxB-7Nvr1db3r-OaZCENtFqqCPLi4KuekxvYtBBC9VaX4kF8kCIoPazx2tdc4RfLPQ03kVC9NIXXxtL77tYrTLEHtxe7ZfOHG2y-sQxtpJvVN4t5MFpHipxsMpn1yWIWS4E5VyjfkYqsKb368h4VodDSshje_xds5hRyP6vTUX2ULZ6DzET5Uq3GlXDd6smNlM1OHbouEmFu48qY2wueMiLt8dd2KPpyEMWTqHUSzKppk0IzM4F2HYLxclsvbxpExnT_ji7hqKR8CnCRFZz1WC0eFH-aX0aQKN1xDzewg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=O0vaVkpTjVHuU74Szo7-Z6IIIF_-DwZXI1Uq-sbjVmhFdhxB-7Nvr1db3r-OaZCENtFqqCPLi4KuekxvYtBBC9VaX4kF8kCIoPazx2tdc4RfLPQ03kVC9NIXXxtL77tYrTLEHtxe7ZfOHG2y-sQxtpJvVN4t5MFpHipxsMpn1yWIWS4E5VyjfkYqsKb368h4VodDSshje_xds5hRyP6vTUX2ULZ6DzET5Uq3GlXDd6smNlM1OHbouEmFu48qY2wueMiLt8dd2KPpyEMWTqHUSzKppk0IzM4F2HYLxclsvbxpExnT_ji7hqKR8CnCRFZz1WC0eFH-aX0aQKN1xDzewg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=L8GCKe6TiACGeT8Oc-kEgrNkHijOD7q1VIi-KqL8zN8_Fm6DDz4bXZAUJabwK0HAnheoCYqp9ArvVvAZdT8RlPPVlVhj_gKytSYwxntToj0GHSPFud6NawXX568SHjhHmo1xZp-TybuC_H5GEE8z81EriXFW_-H84VJGri4nl3NAqWX4P0pk3XkF4SY08dSjleCQYwcXaOH5GCThf2n_GI_KjR79x9YtOWON5Ar7ZRpqDUPdt0SW8f7azDRQyFbNu7McMNQCxtJ6RyefX575Boy2YuCPWkBOSF2V0pY0ZR6_7b_UQedMxxtHpAfXEPX_NV3PpA_ACjmWTaHlStmcLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=L8GCKe6TiACGeT8Oc-kEgrNkHijOD7q1VIi-KqL8zN8_Fm6DDz4bXZAUJabwK0HAnheoCYqp9ArvVvAZdT8RlPPVlVhj_gKytSYwxntToj0GHSPFud6NawXX568SHjhHmo1xZp-TybuC_H5GEE8z81EriXFW_-H84VJGri4nl3NAqWX4P0pk3XkF4SY08dSjleCQYwcXaOH5GCThf2n_GI_KjR79x9YtOWON5Ar7ZRpqDUPdt0SW8f7azDRQyFbNu7McMNQCxtJ6RyefX575Boy2YuCPWkBOSF2V0pY0ZR6_7b_UQedMxxtHpAfXEPX_NV3PpA_ACjmWTaHlStmcLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOFCBCzXDr1EK6XB0yRF-LUSQ-qM0ct2D1s2IRGplN4dQZVXOL6M9lZIabsJNMBI7av6R-V5Zb8N8gfSQqQECqjPkreQ_IGsYJb9FmbHmoo7JDYWOaMi6v5dgAmxxETUE_4xOzIVggI2iJNQn-TL0IC3EQQ9OMG4yJWY6YaU09ldJc5i7QYYhkLoRjxzmMpMWKNKFqCp76t3Yf32FbAJO6GRHkGXlqiuA3H3J67B83HeZ21huGkTIj6pPreNpDInckUTZ9FiIO3-53oAOtIbfy5OO0auFDZS-qm5QjW4Qo1wTybxL35t-tvIiUljmpb0cNbbXirhGFfUturW8xsQQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNARWPH6_RtqIc0-MMxGdmq3aDp9_RiZsyjo75y32V24WNQ_AD8JtTEMfHxfhjpboiK5HuxaA9Fe3iQMEmTgg7B0Zut5VjOmgWSBxHfApxw8XfFFVcyQhGArGHjhm4UAnG2a7HxzAUUKvlNi1Mbw5lXWDXywneJvqndeW9r-Mokzbm2NkVgVLw1de0GR4S8ZEWSGG0Dx3BqfytnR6BSnn5adVYG1ct5hZb8Jbiq2OJZUJalhVmvsc_kPyX1dY8DIlcOYqkN1cIrAmMRcXCWM3--MxdsKFEa5GKsurCFaast9wfbHDP0WMd1kJuBY33X8o0rqnRa9q4zo6H8orYvbQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQ7Z6ucL38IoM9y5ZQiLeCEXzxYKJm_q2-rLil3sEdZgPnsK6IYM82yXa5iUD_Ee3V1AIv5-eediGK6N1suvgqlnc1N5XfsORHFDH1ALhBkSFhvKGBLd-KRG2ic0o0DuwDBbXFDbQSkPgzB4-a6wrNILYOjofnhffKsxsFq-cb7gCgbepDcbcWcD0zf1WHYhgm6eLSG3r7MXmlPu1wN8WryKIgrrfb34PMCgCGORHCvyPDQ3P1LkVE8D9WtFUNwuKTcvtKSRdsh7xyy_WAzl3Xb3Z5LhW8JKqsazmYbThnHbEsICOlnjHpycffTrkxeU8GMC4ogJjjJyZvnZJ5EU4w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=jiTy8JwL83M6k4ganNWqeGhVegH4xIK3YhrGXBMHFCyWcGYzIgKuzZLE0R2db2VIG4uUPTiuNoa7lGVomAhVBh9UHomgPuvHUwNj-JEp1NlD5nkYlODBnHXEx5h_j7_mgQJXURnhjsRdNToEm0ej1zmV1O0vDvvTLpcHt055A12iNcOzfu6KWKPFH7SlYDUTk1BvDU_ItQ4oqHvjtEFE8PPDLcKto2tBr-5TQCeAtFZfQnNwERJp0qrCl189wd2lOS0FKJCU_5-6-gJSylRwQaoGQ6Ci7iwnPDuMIfPiNwUZzN6MfbYFMsGfvgUgZvOoQqBUJwUt_Bxg8-lS0Lg98Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=jiTy8JwL83M6k4ganNWqeGhVegH4xIK3YhrGXBMHFCyWcGYzIgKuzZLE0R2db2VIG4uUPTiuNoa7lGVomAhVBh9UHomgPuvHUwNj-JEp1NlD5nkYlODBnHXEx5h_j7_mgQJXURnhjsRdNToEm0ej1zmV1O0vDvvTLpcHt055A12iNcOzfu6KWKPFH7SlYDUTk1BvDU_ItQ4oqHvjtEFE8PPDLcKto2tBr-5TQCeAtFZfQnNwERJp0qrCl189wd2lOS0FKJCU_5-6-gJSylRwQaoGQ6Ci7iwnPDuMIfPiNwUZzN6MfbYFMsGfvgUgZvOoQqBUJwUt_Bxg8-lS0Lg98Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuR4amgRt1SUkBWo_sBnrkeVZISr2TkDCMX9R66KLLhQHcE0ihW0tqyJtBj3XmUm3cnX6QVGdL3W_gtv9TuZz8Ti2hebKoT6bV2FE4LnfZCyungO1bloRtNifycrHB1IKdn-RAS293_OIkinBXOsRWZZYIIa0SgzTSVkhsdMoh8itJpazsSrZfgMT1Zohk_8VaHIMXizAn-zMw4NjF-j5AM5pVB8zl3VJFlGBVk8vn5Ci3O5SBxKR-e-wrqiB4zyQOQSBt1mdZNk6EBcdEuAtVnsEiXQ2bz50dTf90AATBTPaKzfUe9wBsIePu8TlQgdEUZu8ZPYt68GfdtpvRNR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O33AQGVxnsvpo2rk63K7fVxEm66VDad4DgI5ZKDvUjBStiK_jo5EfQcsAid3_g_E_wlssyCmh52RYnvighMHwxG46xDtinCG4IEz4PI4CgkS3syWZjgbly3BxSHFZUx_4b5vJyVD_Z6OdcvdNCLuVUm63Vw26mgLQEVPbTbwBst0QaCTxpLtfxii8zsuwr2_vvEOqK_psAa3RV2OtT3F49NKNzzYfnrEPuK0dutK9WINCbKe35R8NW1pwRXcJBZKzU5iLdVoY-39zmicLWnngUtnp1PgvQiU7_K2x2ZUFMFm20aChtKHT656mhKPPOxSs2JQnadxGtGh3eUFWz09SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewTDkbgU7oHM7eabHVoPKhwftF9yp92IsyelFIbSQFNGRo9qyM5NTVN-OUCaJ2437QsfOHQkXE9Hw-s9drFCg4586XfK6hllYLGxa0NnDoZ_1N7ctsTLBvOzjq_MLLR_F6xoZHZv8Uqu_BtR8QigxTJOZizKOMDOauDiyNrf6XnpsbznM_UFN4rJIX1ZJ7BuMmQ5072KTSUMLRywt6_UeJfM6j6buy0MlKLFcvvR9rodWTNBEU-AFHnTCT8AkVoo07IgVwp2qrdl-fVIoL6qkFLfCeGxgLKh9uCDeCBiXvZzJDneaydXrJs0edZJDQaXJ1XaQCFaUEMn-H9JTNBMRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcyoQv7-HOcuJY64XlcDMKT6xWEWQqhcJ9q4RppjzohW07b06xPxGmaPEpIkOLJwiZ9uZTuoZq4pXK7V-3pPqn5h8d1xzrac2fqeuTOvb2oXg2e5gKK25R4pef2sqBdS6cLV8NlIGSp1ehkudPDnKqdRi2_qM0DJfaOtj1sVwWRI5koeZ_TonyyRVQohSPXIG2uO4uMkbRLQQ5wtAAxE-YgQawzyL59dxPD0IfyvPuYfawA2qI-KAy9ADjlvwYoRcerMPCb2EFTx5_XT50-V_Ws1THrlB9uXgCqX2ArGx4U5ZM0HWhogYjhBR8o7FCV2L0_3P7viU5dCUuBloKIODw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=EbbuNOF0f86rEe50HrJhs8XjrHioTuiN44usPrJygXpBrEWQ0l2NjRtD5rsw3PrhyX-hzdHS1Mxa5jFcWmBHzKZMwpT1Yr8ydnYdWvuv_ifRZFbNPL4snXmjA1wUddW1u5YPpW2ubq_WJ7zlEc68Zt1VC4OyjG_Vxg3Y1J0ZZYAw6cTMb8-hwGZ3NK27cfs-Im7NXsXq3yAKWgsHEtJDeUCEXlBTNfBHWLYSH3pb0UxwpdNv2msuu3O3P3lqigyih5slx26SQmP-VaZ1ogs_ec9kL-Ud2MoR7Nn4O-X401QoEOnp_HwRjjuZbFyfYfYI3FPQ7U93XuDTyYxOVun5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=EbbuNOF0f86rEe50HrJhs8XjrHioTuiN44usPrJygXpBrEWQ0l2NjRtD5rsw3PrhyX-hzdHS1Mxa5jFcWmBHzKZMwpT1Yr8ydnYdWvuv_ifRZFbNPL4snXmjA1wUddW1u5YPpW2ubq_WJ7zlEc68Zt1VC4OyjG_Vxg3Y1J0ZZYAw6cTMb8-hwGZ3NK27cfs-Im7NXsXq3yAKWgsHEtJDeUCEXlBTNfBHWLYSH3pb0UxwpdNv2msuu3O3P3lqigyih5slx26SQmP-VaZ1ogs_ec9kL-Ud2MoR7Nn4O-X401QoEOnp_HwRjjuZbFyfYfYI3FPQ7U93XuDTyYxOVun5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id_iuOPex6Y1MpZqmBYMHpoW5cQWlFKD1ySiuAESomMK3wXnEK_S_WkjfhHCCetCR9fXpnbuM_pf2yWn-KH8_8trlheXI3ALK0q-NyCW3WmxC7oFOwU1K0EApiFcFN92Jb6eSoxgr05wNa6XpTHIq2mQRAHdOawAvwqYvQ-mbK6zEoDTJlchfXas6Qfhk14U91TQK7A2XkPpS23y6dU6HzY1G9oHGHVoKTyYyfF984tmiy8ZBGBZCt0lswH4C9qxZbrd7CsEhNIoG9gLPIwCnbRx8JJV1D0RX1C_qr64L7C5A3vSAJrxTJbfbqx3pwUcm5tNfnptvd4KVvHD9_U-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiU2XwCo__I9_AMoUj4lQOUX1Y7q0fQMbnruqQkFtA1b2AlPD0VohTRoUlMq_I12l50-131x6U2AzjqVMXX24qE6u12NmgyJGVJcF1VM3MmGQkOIyUb5oyeSPMpYFLJu0Cks-Y5m8UpM0QcNRz2Rx2n80DI3R65ZTqMIVr-r-nz0EHFiIY1sxvJko3lAsgDRT0SVxDg9A_JRXh2T4JsDGcuY1ucakzfVAle974m84GbiRlLlhbm5jcq_c01r9RcJlwRgRtmfmmRMIo3XWZqNuzc2NeORKwJwW-Vq2YT894AD2jg3XySfBrBlcw_ZFz01mXn_2nVlYA8eYSUq6Bf1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig3t-vevCP1yPongtFFE1dfI9Wv0Q92CKBOK2hz3S6szxPapJkTRrsG4XyGaRpz02Usvg63-5BShJAEC3RX4Sv4rWZo1qKbScQahuasBz7whB7szrEylsrVq0NNn21N9bRwssBeqDZ2XRY6fVvPtfejjfVoDYTq7l3LzzT-ClkHtcNpSnUFIpcRXhYCrYP3f_5HJaJD8bznnncBV9CoMn7Onm88PjPDQxf6ySztSCC2g4FLSiF4QE-K-w29zVYzCgGO9uzU5VZEBCs-iv00pFe7Wo_-V5jVM49CVT0w_JL-nCgSNZYIY7PHJEwCh8rJsfZa19FQSMspNIlrMghVw3g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=syVPJlDjgNL-m6IRN4iCo6gm_LIqm3ZfifAgxN0DThCIz02AYlqDX6orlAj2w6qIeiEybgiYTh7UIdbKyh1ixTyjjH4GUgM2ztjI4ZD7nsnRJugK0OWl_ZUBuux7tp1C2Jwn_-lqXHyQP8s4c3XT2CibKnnHX9HsTNj1KenwgKKuLXndDxAYY9GgeAHo8rPIIE6AS9G45Ep5tSNBa8MeFuzUUAabbtp2wOmmdrm8MN5dBSpF0SY3EfcFi0A2vCLYmtqBPyh8BvOEboQaFPBdFIKCW50bT9ZVfoKUP3aE7o5Qa2jQPygE0FMA8ZqwI4zUt1q1TpvgoHCjjvyOPhvBng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=syVPJlDjgNL-m6IRN4iCo6gm_LIqm3ZfifAgxN0DThCIz02AYlqDX6orlAj2w6qIeiEybgiYTh7UIdbKyh1ixTyjjH4GUgM2ztjI4ZD7nsnRJugK0OWl_ZUBuux7tp1C2Jwn_-lqXHyQP8s4c3XT2CibKnnHX9HsTNj1KenwgKKuLXndDxAYY9GgeAHo8rPIIE6AS9G45Ep5tSNBa8MeFuzUUAabbtp2wOmmdrm8MN5dBSpF0SY3EfcFi0A2vCLYmtqBPyh8BvOEboQaFPBdFIKCW50bT9ZVfoKUP3aE7o5Qa2jQPygE0FMA8ZqwI4zUt1q1TpvgoHCjjvyOPhvBng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K1f1Mb5Q-ZFD2NnKDQbYRpV_-ns3ZIGzWVP4Uzmula4tw1fifOqc8q6h32m74blBOgVwwWKRq4u1nC6oDP0ZtQt31rfLFzTdpVnw81pxboq0rI0WKzllueg15kCjzOCQc5VQ6xhwGUJQhgtbt3JvdUf_8wHCqXrXgCnm39FzB17I98DgnZn9-sfYVIwBkuwRiJ7gzYZAU4hdsDvo5FJRBry9jd-mYwlNcwl_1vYreUQaNKXZnAGCQkuyuQVBhruJrqGH-eGGbp7BRrKeTQT8LTA-gkgR70ER_Md0XECdOQ9xiGzL-QSfkWNkQFGqfY5qOQYyrnuV3IIwahVXR81IKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K1f1Mb5Q-ZFD2NnKDQbYRpV_-ns3ZIGzWVP4Uzmula4tw1fifOqc8q6h32m74blBOgVwwWKRq4u1nC6oDP0ZtQt31rfLFzTdpVnw81pxboq0rI0WKzllueg15kCjzOCQc5VQ6xhwGUJQhgtbt3JvdUf_8wHCqXrXgCnm39FzB17I98DgnZn9-sfYVIwBkuwRiJ7gzYZAU4hdsDvo5FJRBry9jd-mYwlNcwl_1vYreUQaNKXZnAGCQkuyuQVBhruJrqGH-eGGbp7BRrKeTQT8LTA-gkgR70ER_Md0XECdOQ9xiGzL-QSfkWNkQFGqfY5qOQYyrnuV3IIwahVXR81IKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=uaOjtfgTHgTgVOKr5m5M0jKKWe5DAm75kkhvL1eTdMOBVvbBKXVU8Uo9htQpFr4YQ6ASmcfzqI0NsSYapOtg3-0Ig3r1UjYHkUdnS6_Hi-mRYjRrMN3BAEGTta8WXFELnxqoxptsL_XOqaIbSIaeLuRGaESBnm3DuhqvxKw0mLA5sFskMwgVQBCjRfRVqT2eEQM3v0tH6RzKoEiHO1GJZX8hqcQXWX8bpTazrD49J1OJswQRCJ8jAp15wIkxz6Y2KgjhBLpd1Lx-U2D77Xh3W_hRp_xcjU5PA0CqzTPcYusWldfP2Dk49IfKa00VszgDo5H_TEF2dBig-38urOzmlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=uaOjtfgTHgTgVOKr5m5M0jKKWe5DAm75kkhvL1eTdMOBVvbBKXVU8Uo9htQpFr4YQ6ASmcfzqI0NsSYapOtg3-0Ig3r1UjYHkUdnS6_Hi-mRYjRrMN3BAEGTta8WXFELnxqoxptsL_XOqaIbSIaeLuRGaESBnm3DuhqvxKw0mLA5sFskMwgVQBCjRfRVqT2eEQM3v0tH6RzKoEiHO1GJZX8hqcQXWX8bpTazrD49J1OJswQRCJ8jAp15wIkxz6Y2KgjhBLpd1Lx-U2D77Xh3W_hRp_xcjU5PA0CqzTPcYusWldfP2Dk49IfKa00VszgDo5H_TEF2dBig-38urOzmlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVDLXHNuHbr-go6T1qtm1eESv1Hc9nspfESIq721tqOcPD1dg4XLBh913kWRGWMwRv89rk9nz933bKib6Xn8xqvtVfx_AWSKDSnYEGSzUhPc41NKcoKKA5xdmGq3WvOSleySVn3Bpel1pUCtV_Iz_rOAk-TORsLTs4LSh4Wi4ZcSVCGK2k4Y33Aqt8b5dXIfnEvC5sKA5slkjlH-nwRMpRZM1JVXbbUqpzul3vAnvdx5zCmmUBdaspuMsFDVrnxpLOd6fRAQTehFF_T1zES1FL94k_eVXYnpWO0SRGyZ8Y5sE2YaI6l1mM3fl1xqz3ScGPN50sv_GkmxNhlJ7pi35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgY3KJKhfrVEyGYcTypmUvDZD2kwSAHKTMSLfmKWsRHQLyAibx8lH4t1hlc_9Ql1Bix-xFhJNC62OURsoGAGKCxQHHKcP4Ym62G-J5IveH5nYnKyDnEBM-Fepv9Vf6zTUMPPAcAg0Jk02eXOW0Wl3KyF8T-dWbVg3PePRAL0ENsoPrPsLw1kKpIzPZViwDyRJJMdees4md-z3OOyop4vDIJ5kR3wiBkUugTBhgC8dAlcB0g8y0jsXQ_YM_A5jgmEiQnsm5Fx0OgGxUV1S7txNRceHGUkLCnqOUqtbn4U_-8SCEaHte8dQe7I1doiz6Lpql_b7kDquArZ861QEirLMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8sLeGzu8uyMCKSn9HzDnxdKsY2jaB2KdPonK0wqxSk5XNi06qUkPeFuZlSnIOsrmWkeRWDKjAefRSU9PX7KxlhBdrL34djF9WKCWoCHauSwVbej9IA1PxcnVYPgrKhUt7DQYp-ocOJnQX0c5mlog5PAhGm9HIRuH2ytnxnweBEoxmPPbHCG1wv9tJ5Tkw45dZKickHetDmO2901zeN2IjiJMT9OL3h77vDH07icPdZj3BoPHaWDeTPCQ2_hxa-Tq20UiyIpTzzm4elDmDYUNzb3cvq3e1P6UNYouYePe__ACP3eyQ9YQqA5vxOr6HsTB3Asc8_GW5A_xY4x8y1EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9tEXtSknCE10yY8VES9kCgTuCkODzeMASFmmSBKSR2Fv7RNdfPlVRWSCK-njudrbnsJJ2UQ82lP3gZaos9hVxJyLSBVmZHrjf3UU7ShlS9Uv8L30GTeDumVuYNPA5i7ZxDTxCPrl7zJjzRbXnuJ-bjuvgjSnZTuSHGuDKrDgzlr8yC1kmspxSgWQqJcHrsj09YZfiMEIMpzrgaBMY12YUdItE5VBZqWn2vQxd3zBNjEB-7jmVEKSxLihYgn28HBZCV7MJIJElAznD6fPg6cHR_feco6wYjPLkgTHbXESD2xTMySQBXEwRYd0si-UFSL5pt4r2cfX5YOEninQcs51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWnpc_Y6-9-n4gSEczhTTNJJo-YWaDVC-7mrS5QfMebKm9Ru2USSoz9hQ0jwatRLc36EZGIcnqugrYRY1K8a6PlkV9Wb9ZdbUkoBPbcbrs9YxCmssIty09TvIM6L910MPWUA9vcYD9HfZ62eCADbblMtPKlreYpyt5vltuu05GMJ4OuXbHLZGohdkgcnXNrpricjGx3CleANQarNlDET8k4GFnkchiKKq9f4_IO2djFv4tOltMA9HtToMVULs1Y7-Ec0cimJ0d7Nq_4ARMISU1TMolzk7giIDIprc7GNJWLsa8Y5V90RiPMd5E-cuQssex54sLf5frgWK2ap2bA_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzhjD_Z83suy7TvMcikP7y_o4jgtXb9Nb5OlI-Dbd_b3HHGFjhL60MFb0C80TdANLf1FDSy3nLMmHLb6hdbb1A7QV8FQCtleZGtXiEQGBhlhFbyH6KkQnwbHdbjArNPcE_SNNraX0Ob77CXFYCFx15Jsl9AQzjpcR0jfPfie-vPazYyZLvQr1ujlCnXx1zm7YkEp5WkegYUVDvwoGTIk68VnUfFq6CGB0drPJ7M9i0SddsidVLO39378yAvzb_Ambg1NQkPLz8BUGUavJnDy0Mk-k8ZmmzZMcVgbSVL3P549YJ759glgO4l1qUqfjvVIUTNopOIVf1H5RUYyEXPd1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YR5FPc6MOn8BlNG3R5X9i3uQjaIEe8jCSfSiQ2A77z7HylH98bEkrGp07GJYpuLDoLIO1NSmKU03O1VeBrqw3FkXCDGBIT3IETDUddSK_Ge40QurNYmnm-v-CD6ERtNW2l-ZnEgBR9grhTxfYLdSfXoP6XncVcYPbsdbk26-f4r-iFs2jKViLIsMLnJ87VOUcLvJtx1eFMhCaeDgzJoDuvn6vfzm-gNhdruc9V_d14pdq8JEoSo4UE6xZ5GvPkIerBfb0m46SFPw5UGq0ptSaRomwqtpckWdKZJFHIWscLlLBYUKHsYCN_lNi1i2Tl-pifM4kSs0ba5AGO_CNYRRaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz0y31_fcSV0IBLO49kNb4WXlXhphUfFjCllElRUdBS-0xShpzfvma_hoBxxWaNDFYjbqWt3vF4orpD7CbLpwsbyaPDNZ7x79PCOuxssbUoaEwNh2Qhj453wOaAku4IY5gaX5pvizYhkrK2ea_83W-uSeqKpEDRI9TRTZ44JH7wSKohhzhsY2f3pTLjVFSCg89gsgYVuTTrO3cfwHWlaX1csR4IaFjty_EXruNFPURIZWUje2_OHYLwzDGonpOS-BmtRf19zT6wq7X9gyYqzj0byAyDnYcoDf57QTt33zWctPyTfUAZeJUxuJuwlAgYDNYPspnbjdnVfD6oPOBlg9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf7iTa7w2jga-ioo3ClqwSm7G78xE5ABchobMR3Js_C_teqQ6AZkRjXXEjuu4FlyK1x-14uX4vZVdoZeYDa4rY4_WsBUN5tdiDzF2DkuLTPTyEbMlZomb9hj9CIXNpBOF_JONDjysCVwpmxTYqoFRpjEkGwCTh_BqslcCp3TXlRNUEGw552NOZLkLybSqDaTzkbtHOxZ36vCEdBM9yaH9EChk1VCeB2DycYiJP6JDMfEPsJ2LcROYMlXxCssGmxggVnfT_vUpfrvkASKzvNcfws3G08kGopYC3iIiTI7BX0rdzjcgDK_DH-AEl_S7cchk5AwxifCMbT9JvEtOBMAEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGY1QI5ua5YHk2cmr6W3GAM5NM79pFAS2kRGCOskcYwrQPCDUHezYlGkd4ptXymcwXme2v3sq58PZ_SPOZL5IopD2d4zl1WrAcbRtef9xwIL1mEBCBBDMibZ7pxDC9A1m2nUueRK0BfL6KwIgo3wsFpMx1S8FNcjEcvRrqoFRZD50NF3XTYCx7MYtvwYE6XVcp5GvXEF1-dRQGAWlEHmD3AFao_WfVUJcq_nljnfCM1CLBJludsgXR4hk7kgehDWNYlKQfCm9F6-rT72S0asVsJB1BOCr6hdCaKucXUnRlsiYGnf_u6kMaMq46XThPDxIGX-SqlHK-Bk8N87pqMzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFqAk-DJysGWYHrneyVTFu62RHws2tqrmjrj-6O4FpKxO6ORc3UiDmYVqqEUi5HmBKFcKdW-rgFdbziaeXsusvetqK0J2hXeeJpFJTdLcxgYuuw7xaGgelao4Ifh2XiLaXzwq6BeFIfdWATztK7xXqUqYm5cGAvhDfc64yPLnR5nLpkElr5h-TO1HvM8zsBXHbCUc2eU_ITV69RNWy3715C_S-pkQ2SFSXtHxxzZcnxbLAjESecw-ui0lapTwv8oITnD5edBTJrDXHizUkWIRVP-oGQx2ahezqV-O4v69QFTYOmbtmS_fwLvdNBrkI5BTgG8Ax7biZzOmJg3BJqW8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueHyrEFBCqDIZ6viBOu6bOaRJIvvoECNW5hegK7WnYA1Uq5h0XHaEdeedqjFhUyJuUWhIw6B66jzQIjkwdLLdqb1mblQrFJ5T1E9qFyjaXMrnR21eL76osekqNe-aaqgCtHJlLpdR8L0L8Q43EGxqEceNh4KvBF2VIXTj9k5c8X6BR_CHaxxVjnxoWpwPHuvbJjvxFcnvdo4wkvCeot_Jo0iiqR4v8BSmQpL4es1cpjpr7mN3vNTSq8U4wF6xs7GhCVMWFyPND56iuxZ4MRUu7F0t2smry1xZZlzv1TaLoou8z_PCGgi1WuxvKvBq_qLQCPCf3tjTpVNRvSX1lhwtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjA6NbY6HVE0WAnnXEqXGUB9f4YL9fZLXxH1cLDflrK1SR9uXez1zYAECsipWhDZxW0vgxixbZQ3seplf3ZEt2dfgtCONWKWVBm-F_bb_cMPxZzduRa0cG8M5tiw_cr6lHcFtwtnr6DdJSQjpVYOj31urM6QBJ3CF1DTlbfZ9gMh_u0WaR94OwK1KJGP7O4GzgVixiXHyjJO4NGVK8Vdr3L3oTmDZaK9pLw6V_IyocUwWt4Cnd6bXLJ-4dZufjgwVfBje9sm6owRI5U7QnpqvgcLfwjfucqNqYjSz9TdieF2WrEKeFzo3veQOMY1aoXfM0engSPqt6ZJIza5aq2OZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmFRfkOHfaosXuOu-GNbkpAtEiAasnohNdhdnVLAnBPRqrtCgSCp2yO6wp2As9PE43j543TRshrbR__4RkHS9t9t3W4F0u9fN-7t6PzBw3T1lPTSmPhU7_SRC4j8zs2ULO4g3hAy9mSPRyjk9Ba5qxJBlH-bZjWkrJB4dh5l4VLevm5pFvK-pd3pjM0XT_PZP9ZD__wCoiL9riG2DJ5nQQWFbFmLJubTyj-y0cMMNNiexbVigt-LaYj-XHflIqH8p3lzvVLkEMWjzX-nh8NspxkVWe1HL-hcFL-dn0oENBvmXXT34lEcRDKOLO5K_BJxwKPRFPNywio0cXYnmT6PEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0T8YqADML3ICqfwzzJFkl3eXcJISzOqD-tiyK_QPXKxohru83esoL5JBs9L8Zn2_iC09pbffhHeJ9OrbgYxo_OZ1v9Pgl3tjameId6N039vQRsxy2wOOZNm3ASV2IxRiJA-wADJw3m-YcAO-6VMMMSGca5T4HAz7aOPsRZJ7uCDzSHMCi8JGo8F3kojeAU91Y8Qg_pg-BTZQYtIFBZ3-GKr9YF9gAJh8xNtBfFuIgYjli4DYoZ0g4WKTzH-0Xpm5Cba4SDx3Zdd0RfTXNLII9JwTgWlaEh87EtWbDXPaQPxYHb-6ksdo5r_qf1AA2k5kBt2SBGCi6snTNPpoR-txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=h-Yi_QY4k0glt5ZIjFPTK3f7oRNILTieh1WW3oXWgc0ta0uquBTPKKz8BRQIH7_ytZRtGstqFc51z19B_tMnPlqh0-1b_EP7gYVnRSXs8tvEUwYAO_DDuiFAidXKWcrGPWEMBzH6bjFRkOBzOlLx0nm38KxpMupc2UEIyEI-AgqItoqhZzDQIMxIPbtzZqNnHYrrxj7b2ol7hahNROxSm0V29HRCeQlRmGT37Svo44S_A0z9AeiuDI7BT3_cfKdt5_sOlffrIrGsik_99MsmGC5p7Z0QOMTQLXsFHRCp76RTm-RqkgHzvuNDNEBvOmpj0Nv4MHx_gSk4gfkVfO3njw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=h-Yi_QY4k0glt5ZIjFPTK3f7oRNILTieh1WW3oXWgc0ta0uquBTPKKz8BRQIH7_ytZRtGstqFc51z19B_tMnPlqh0-1b_EP7gYVnRSXs8tvEUwYAO_DDuiFAidXKWcrGPWEMBzH6bjFRkOBzOlLx0nm38KxpMupc2UEIyEI-AgqItoqhZzDQIMxIPbtzZqNnHYrrxj7b2ol7hahNROxSm0V29HRCeQlRmGT37Svo44S_A0z9AeiuDI7BT3_cfKdt5_sOlffrIrGsik_99MsmGC5p7Z0QOMTQLXsFHRCp76RTm-RqkgHzvuNDNEBvOmpj0Nv4MHx_gSk4gfkVfO3njw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi1nFShW4fEJcByZodMGv5E1mx7Q3O-mRmCaQNNJG59qRA-nV0tVCujz3urM3JLkCtwtztTzuPTlY3zp_fFSjL8E3IiO3sKfN4fqCvDNgfGLSWvcDBmUWX57NvfAPtU32Lt2zXxotvGZo7b6NahWGj2plZh8FixcY0eGjXivGxZMHhNHgKhm9EyLDFUEtVOGnbhQlkR5FTv_PCZNS8NNiafGpsbBXMcqWg7FH_fQVh7ftMK4FrS3pT7wIibRZtRREob3eJER424yz3jhlPdUfmTL-GTNqdrjuV7k9OxaUFLfSI3iANb1DYN6ohx7vdNBy72PnOBdvZQe6AtEdTzNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=W-_uXyNCNf_rCxe7tZraI1vdYdG4MxQgCRrCd5AX98JHHkYhZguUVy2WGX1QCk8Yz84x7zMcXbXHJGNGPw86brlyg4CR7mFGA3QVd1ZV9X193G-PebHGYAL3F5nmd7u1kYfyVdksEFCTPIxIguHxarAXcTWOQs7347nGOfoFLkbE2H_BUiVzSbKvE8vlNMIFbfY9nKo75fKpkTZEUcxvc8CUcKVGsKCXqorWMUqfyUcORmzTMe7Vjk-BEN0BZdtmSNWvZbv6GJyxTNjBu-FFwtptGJLrE4A_3xrT603ClkCuUljFnPAN1wfGX6QZ5nlxbGbQPr5_B5kE5M9RoSABgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=W-_uXyNCNf_rCxe7tZraI1vdYdG4MxQgCRrCd5AX98JHHkYhZguUVy2WGX1QCk8Yz84x7zMcXbXHJGNGPw86brlyg4CR7mFGA3QVd1ZV9X193G-PebHGYAL3F5nmd7u1kYfyVdksEFCTPIxIguHxarAXcTWOQs7347nGOfoFLkbE2H_BUiVzSbKvE8vlNMIFbfY9nKo75fKpkTZEUcxvc8CUcKVGsKCXqorWMUqfyUcORmzTMe7Vjk-BEN0BZdtmSNWvZbv6GJyxTNjBu-FFwtptGJLrE4A_3xrT603ClkCuUljFnPAN1wfGX6QZ5nlxbGbQPr5_B5kE5M9RoSABgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=eHLMjjNqKyEG4nhFGjxgyzM_JshSkcUU9AFrm0xCeKsAvH_X8lhpeF562MnKMH3xleptsXHWKGS9OAF-cl9XnTFYmeaRRLbCJowMoT59RnvXRIiVdHiI5K9KX1ltMVnaFbIAa8yWMhyDTvfg2JmKvmPfioYZ76Gff2C3LUigQu6gCk1q8q4PDJet0OstK6yWz51d5LZ5E3EAEAESU5Ir55qsGhSfAwu_dz2-IpWyD1BLg0QR0NVgkQ1XuhdwonSfW7oJKlpiUps0iKwoZwo0hbVWkUNz0hYRrs9frkZqC3LPuydL2c_Dnve8Hak_akhf1O1xHwCbyXK6QiGR3ZmKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=eHLMjjNqKyEG4nhFGjxgyzM_JshSkcUU9AFrm0xCeKsAvH_X8lhpeF562MnKMH3xleptsXHWKGS9OAF-cl9XnTFYmeaRRLbCJowMoT59RnvXRIiVdHiI5K9KX1ltMVnaFbIAa8yWMhyDTvfg2JmKvmPfioYZ76Gff2C3LUigQu6gCk1q8q4PDJet0OstK6yWz51d5LZ5E3EAEAESU5Ir55qsGhSfAwu_dz2-IpWyD1BLg0QR0NVgkQ1XuhdwonSfW7oJKlpiUps0iKwoZwo0hbVWkUNz0hYRrs9frkZqC3LPuydL2c_Dnve8Hak_akhf1O1xHwCbyXK6QiGR3ZmKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikgjyNrelQPmFuLP8UD5pylSqAeJX0NRGddnOFTpomI4VdoORL7tnthZnred4yHvnBOtdFbijBhCCGVeCB9gn4QerBEf8VBWB203eSiNEekfPwDiBJCS92vDsQM1HvhBZn7vNx40Q--LADgm7qFrsbzjw1oB9LDeTfWgdXXpjW7v--g4ncstW31ZbKdryXPZqyMAXjU4EUM9ZRut3L7h922ZyXQlIL5YtfR_VZWotDs3aWL9bAIWpy61RkBFj67NsxzeNH2PETUoooszIqX6wBf-kmwkh6LokTQlgNpjHYhzL_V07n2tKRCvBMtCs7EK6gNlTHowWyvkZPFUu1VSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=npWHjGJR1lGWCj0uG8QZUwd47cMF7AQAKTiGHWawv7p-glNUGID2TnARb3W9dlaMLYkb6Or2cdPtenH57Z5gVXKZEXRqnQvGH2KXS6y36_H-UO-FZvW0kDgYtAja8QZkRzYjT1HWgOKkDQ0C7PBYtCazMQ9qiV1Vyd0UTum7gVdpGWLnX9ewEgac69zsKyTwC9rjitkX3rdfx1U7EigmZPpYnLITHerBFZ4d-1T3UgeWWEmNMBwTSuRBnGgrgBatkCM8eSPjJrqizF5soce3FMwciLEqDmg48hckmm1JFVwxm1ZvvqSmelsB0XXNvPQwV3eu88NCSsX-wjD56EC7jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=npWHjGJR1lGWCj0uG8QZUwd47cMF7AQAKTiGHWawv7p-glNUGID2TnARb3W9dlaMLYkb6Or2cdPtenH57Z5gVXKZEXRqnQvGH2KXS6y36_H-UO-FZvW0kDgYtAja8QZkRzYjT1HWgOKkDQ0C7PBYtCazMQ9qiV1Vyd0UTum7gVdpGWLnX9ewEgac69zsKyTwC9rjitkX3rdfx1U7EigmZPpYnLITHerBFZ4d-1T3UgeWWEmNMBwTSuRBnGgrgBatkCM8eSPjJrqizF5soce3FMwciLEqDmg48hckmm1JFVwxm1ZvvqSmelsB0XXNvPQwV3eu88NCSsX-wjD56EC7jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuwkURPnTuHxKQCmt5tNiyYdvoiQktEOXjjvITKwMuKoPmG6V8qbAM11MkfPMiDXGOj-ox3tRCvX-ZG5BYyZz4VNx2P__zkGWBYCK99Tu2Ft62VqX-VvJk8MPVszStnpNBBLgE-FXUwb-Are_DaD2Bt1N_oAT9ONWe0wj5fkDwlMDzF9q4QeRTpbbI46dQ3kQ_MueJvo5j8mnrMmZq4DPCyL7QQPUxR9hAxRoZ_1YkvDKbHcc8CgE9cJg_QLVjxkpS5udZhQYM8RgU7mz8uItE7wAlr5OvXlOfo1pdy8NhV5qA99GR7FiJAjBMWpb8_SxA01Qxv2KOQUu3Kz7x5H0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIEuAm1tJ18WZBZpSN0ZvX0PJ1SijxQk4VuLSE5n8pnLQI93OTpDLA45khy3YWOlpb--tPszMXuJ_c9h0rNr2VxMtLT4BYW7CwoKA_1JNovfkd0BJFrgTxGOCTarmqtza0ovamGtGI7VB87JBbfcYBZZgox8lx-0bRZ7aqafMeFhv8B9XJMwPL5bvXc8j73H15fIpmTQ0F8GYQFWG59BlzaYaStAtjTujxM3bnzJkbLWi1UK2n06tzcpCfOJXPTVbxTiEVrOzS3MDMdD1bjqdAQ5jUKFL5E6ZTiEqhz_6GBjjqaEyrietI_ffB-lnhOvkWZnIETZZCtFjiIItrE-Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9BS80fIYQNw5h7LbF5XcCixSK-llIjozhUjpaop8N7tpEPbZa3tLp93yv-f0DXFri_wan5bjNd_DaC0zgHin0dMG_x-52ScOsPaI4f6SZAPR0rst5FiaXJClw5gmpE-70MFucb2MVk4A2dFQG1937jQZdLFvE0WThOUBHjR7GveCbeJrk0wUESrw8vmJu9rzi-nAgLT-Ar1elmWpvJZ1yqb47bOQGeOPBouyT3cjExpAg2x2U3TrgG6W72FNMjeeG8O00Qs3wgQa6rxMEhtNIHMhUC-OgsiqfnFia30LSb2rRN5fI4CCI0OiS9b5Ts3M_byIHBy3A95alPwBO04_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSpwI0c6VLOBzs_o7LFs-JignfSOxmLng9VJ3rey4Fe_YQS59eMCHU079kziNE1K7VQAbsN2ba7jx2fS-O8AZqOr46dXaQD8P15ZjHitqd30CQJuMKqEzweScPnsYgLFDJJhCYm3dwwiNUrDzs6OEXbKJD5Qjq-g1qMLexMcbOqNd7CAI1Njp4tld2AOI045IovaM4Wsx_crj1oE2fM0zuldEKvxCzLKcKB32ESNP1U9_p5obJ7IgHRJBLXnGlsYVnghEd2ydsxBWh6MfSfyJAfJpx9b_hIlGVYCwhOnRYXUCg3yp0Atzxt1DHBEIQufhgmlGl6fuCgwO9Wq4ZGimw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=YxwR835RjtU7fPI69-F8LFCHrBLn1kCoA1yrikRRL6YFoRub1Ir6KxKI9kgSJPgNt5mq7n-1W8M1zKyLjPJ4Y4mhAuUdMp8pf3dlAERRB36sEb-JdQ9WqVgGqneXoXkhrPGrKhOxbujSLamjEwX_faWfcBpicVf_wt6fDhX97KuraV8G_uUcLoX8t8xm3ceyLUHXlOM5OkR5RH6roKr36nOMQcnzyAusuiVb9NmJfixZZ2yffEMNTEUiU6NUMTTODaSi7790wMt1L99IdUHiFCykswrmyrUXIgD6CI2nhapRiloy1BsYiLf5f446Qanpy6OS_S03BXhH3-XLqZJDLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=YxwR835RjtU7fPI69-F8LFCHrBLn1kCoA1yrikRRL6YFoRub1Ir6KxKI9kgSJPgNt5mq7n-1W8M1zKyLjPJ4Y4mhAuUdMp8pf3dlAERRB36sEb-JdQ9WqVgGqneXoXkhrPGrKhOxbujSLamjEwX_faWfcBpicVf_wt6fDhX97KuraV8G_uUcLoX8t8xm3ceyLUHXlOM5OkR5RH6roKr36nOMQcnzyAusuiVb9NmJfixZZ2yffEMNTEUiU6NUMTTODaSi7790wMt1L99IdUHiFCykswrmyrUXIgD6CI2nhapRiloy1BsYiLf5f446Qanpy6OS_S03BXhH3-XLqZJDLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Oq5SXxJNT9GRQFbqXpZtOFCkIp4VMxbHK6bjxsQ_l6bhvGFGunlfh9_4PwNw7-MTS2ivl6ETVsbpJdG5RXgFELQnNEHqFi6UzWCbNTQb6rV8XBX_L8uyOL07pPdqlrdwBsNV-qUQVYAqDgJpKys2oHgNf2KZB6fSp2LjP_yGagEm2FS2VuJzPbfAoCfrs1TTFEAu0EpnVHDsyJhOKQKiNmxot00tWsnX5IV9MkA8cFYqWDByWUKCG18ZlR_qn04HInq-NHWr2zom4eIvyoxYpNlQupvTVjQItPJa_7jlctEHbWnG382u7Cw4Ml1YuMaIW27rajAHOzzUyX1aDtYocQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Oq5SXxJNT9GRQFbqXpZtOFCkIp4VMxbHK6bjxsQ_l6bhvGFGunlfh9_4PwNw7-MTS2ivl6ETVsbpJdG5RXgFELQnNEHqFi6UzWCbNTQb6rV8XBX_L8uyOL07pPdqlrdwBsNV-qUQVYAqDgJpKys2oHgNf2KZB6fSp2LjP_yGagEm2FS2VuJzPbfAoCfrs1TTFEAu0EpnVHDsyJhOKQKiNmxot00tWsnX5IV9MkA8cFYqWDByWUKCG18ZlR_qn04HInq-NHWr2zom4eIvyoxYpNlQupvTVjQItPJa_7jlctEHbWnG382u7Cw4Ml1YuMaIW27rajAHOzzUyX1aDtYocQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=aozvnHBx7eTKvdzJeLdifMITFZDKMfVi2Ke8bWoNFol7V3MsGHx2PPpN4xXW1B-AK085fdSoZ-CtmFjy6WqwKHwo3H7gBzteWwwJf4u70AQR9Qf9NbDgR3WWCt9_JBdgNThw6Z9b_ZqHVjSlioFtZwX4oOSFTPwpBHSPhY-h9ADSwkyK_KfiDs0dq5kk7SKZogSH667mFg1O6F0QfyrUg-6mXPPqPq2xoWOhPgrr_ULGtTCRaA9oi80E7asCWiGibS7EIHHtzR72jRsZlefusCtFIhC82Nxe2W4QPCqRV-HsNhrFN8Rf6mYwnmW92BMYAm9VQIN3FNCHPJX9fnQuEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=aozvnHBx7eTKvdzJeLdifMITFZDKMfVi2Ke8bWoNFol7V3MsGHx2PPpN4xXW1B-AK085fdSoZ-CtmFjy6WqwKHwo3H7gBzteWwwJf4u70AQR9Qf9NbDgR3WWCt9_JBdgNThw6Z9b_ZqHVjSlioFtZwX4oOSFTPwpBHSPhY-h9ADSwkyK_KfiDs0dq5kk7SKZogSH667mFg1O6F0QfyrUg-6mXPPqPq2xoWOhPgrr_ULGtTCRaA9oi80E7asCWiGibS7EIHHtzR72jRsZlefusCtFIhC82Nxe2W4QPCqRV-HsNhrFN8Rf6mYwnmW92BMYAm9VQIN3FNCHPJX9fnQuEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=EsrK5llh1bY_TuRNbNjqjXZiAzbXyu1KAIzEcRSctiqvMzc_fZTmwgpwO7TkH-JoExWH8QH24I1t9zgZwpnPQbev-8wSSLDu_fM4ENicWsWGPR-ia-pCufDlKO_ryMM8KTcKyZQ9NRAHSsng_VSzVARm4E5yvXChA2YtjYRjhU8v8NdnD8Xo3HcsT7IuJ9wAnPjdrLIUNeLgRudVDsMb7bMpl6T5fETe53RtYm3e2LRsFXaWoy5sdaBPGnp5BbQcPZjJO3VD3-l7zzEG4t9EYItbM6GWhNxKQ2Bmaukw-w06AsEFPiWXkaqlT-OmHxaB9s8h032YdwFLvfTxm9Z2kGHP7BLFxZfRwVCfXwHmUnx1N0cnJVm_HQ32BVorlrs8v6-Yv_ph_Opnu4lT4Qz4HQ9196puCtlUSLSLPtxprlL8YlnCJCE1BOcbpf4x_4UE1DYjfjAKokxOMZdQc0664rkw4zCxSmA8jkRFHapm_KsqfvjrvMAJ1qivGIc_rOIr8sQ05DxcoFrr3_3FOOjzC6rcnMzq1UbqL3cMjYXoM46ohaR6YBClJi76NIT4Gzw638cLpGWZnTiBok8evXecedqrrcT3SLuTwON2ONuatGuG8rwK_K0qBcSYx2B5YNqznoW2mlhHUncmlNvdb15WNCLxxv7jjRyn2JXGO17Dxrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=EsrK5llh1bY_TuRNbNjqjXZiAzbXyu1KAIzEcRSctiqvMzc_fZTmwgpwO7TkH-JoExWH8QH24I1t9zgZwpnPQbev-8wSSLDu_fM4ENicWsWGPR-ia-pCufDlKO_ryMM8KTcKyZQ9NRAHSsng_VSzVARm4E5yvXChA2YtjYRjhU8v8NdnD8Xo3HcsT7IuJ9wAnPjdrLIUNeLgRudVDsMb7bMpl6T5fETe53RtYm3e2LRsFXaWoy5sdaBPGnp5BbQcPZjJO3VD3-l7zzEG4t9EYItbM6GWhNxKQ2Bmaukw-w06AsEFPiWXkaqlT-OmHxaB9s8h032YdwFLvfTxm9Z2kGHP7BLFxZfRwVCfXwHmUnx1N0cnJVm_HQ32BVorlrs8v6-Yv_ph_Opnu4lT4Qz4HQ9196puCtlUSLSLPtxprlL8YlnCJCE1BOcbpf4x_4UE1DYjfjAKokxOMZdQc0664rkw4zCxSmA8jkRFHapm_KsqfvjrvMAJ1qivGIc_rOIr8sQ05DxcoFrr3_3FOOjzC6rcnMzq1UbqL3cMjYXoM46ohaR6YBClJi76NIT4Gzw638cLpGWZnTiBok8evXecedqrrcT3SLuTwON2ONuatGuG8rwK_K0qBcSYx2B5YNqznoW2mlhHUncmlNvdb15WNCLxxv7jjRyn2JXGO17Dxrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=nsAGzAx_qQ7Bwxr_v6GFNPCpASglQce3yNeapgVV1Abs6OrMoxR23SgDehZgHKD3H1uS7VkOFC-_LitJ4cJ9kA2CUTGpM6V0hCuskRGvh77mNbBxdF2gBNqpBxFqdZAZl44PEUA6u8J2DAVDyJ1z5Cxkl0Ebgb0e_luKrd4FTlA0ZLZJSaHP4x76NxRYq-6zuNLe--siBapmMKtU5yXtQ7C1m79ZVcSLEiO0tSxFf2pW3jLWuoFbCKpWF8uwP6M0fxxDzQcauM8jeqivkn1_XGqyD2thQqQwJanz-DIqJJKtRg_uINbSWWeUDubtBL3faSecnh_7h9LSv_55Jt5nPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=nsAGzAx_qQ7Bwxr_v6GFNPCpASglQce3yNeapgVV1Abs6OrMoxR23SgDehZgHKD3H1uS7VkOFC-_LitJ4cJ9kA2CUTGpM6V0hCuskRGvh77mNbBxdF2gBNqpBxFqdZAZl44PEUA6u8J2DAVDyJ1z5Cxkl0Ebgb0e_luKrd4FTlA0ZLZJSaHP4x76NxRYq-6zuNLe--siBapmMKtU5yXtQ7C1m79ZVcSLEiO0tSxFf2pW3jLWuoFbCKpWF8uwP6M0fxxDzQcauM8jeqivkn1_XGqyD2thQqQwJanz-DIqJJKtRg_uINbSWWeUDubtBL3faSecnh_7h9LSv_55Jt5nPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=faEZwmL6nn64VRtt2GLuViIfLwkevO_vBnVfv4aEROJm2nI5NmT31H210iZQzFQ3CZCgkWXtZwNVJJyW0kNsYtWyvSEY9NtBwpiDYHgAUEie8cOOJ0W5JxAeMgSK_0Ze0eRMtcB3ehCFlZ-bKI6XGhqUyWJr7oNoIYQkxhCuEHUXNrjc77ujCiUMJLI3P9MQmLN00f0nmBeNZoV3Cslw3aiBXjAH9P7m9Lc4cHVSe3T5avDp7a4rJHcjQsbnbNLWF8-9BygmNGBJFJ1vg8nu8Mrqzk4U3mAgH1tULLNLxnF9PLrkqVIdb7cMjGU3CPN2RYWNprj7z0OaHJpe-HdZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=faEZwmL6nn64VRtt2GLuViIfLwkevO_vBnVfv4aEROJm2nI5NmT31H210iZQzFQ3CZCgkWXtZwNVJJyW0kNsYtWyvSEY9NtBwpiDYHgAUEie8cOOJ0W5JxAeMgSK_0Ze0eRMtcB3ehCFlZ-bKI6XGhqUyWJr7oNoIYQkxhCuEHUXNrjc77ujCiUMJLI3P9MQmLN00f0nmBeNZoV3Cslw3aiBXjAH9P7m9Lc4cHVSe3T5avDp7a4rJHcjQsbnbNLWF8-9BygmNGBJFJ1vg8nu8Mrqzk4U3mAgH1tULLNLxnF9PLrkqVIdb7cMjGU3CPN2RYWNprj7z0OaHJpe-HdZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uljJpEDGAFvzF5nngQiz1WaVLEHT0MvVZf0q7iTrLnSuGA5g13j3FIlLoYs37bL7N8xbeOPZor6l5aAkPkOcXZ-lzs-PAlkA2lKK-rtlhiqipXKHRqaGU-U3S2KOWHOqhCsMQn_GksL9nXSMaHDADP-9jKwOmDh-veX2mSH0V4NLhJuBTA5clCwtp3OH1SEj1Kacmp9sKeTnZy2h6_lWEfE-0IBdNs2fkfz-CNtz1FlXnTsAhA1ab1zXTHYUNrVwVEzJMMQ5EmnBJQike7zTr1ysLeZDL585X__1R_FnOPmStI0GHXUTK1EGjcrPbkXEDrPlXZY6VT2Ycl-FYuHNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
