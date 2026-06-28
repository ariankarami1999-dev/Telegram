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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 20:29:22</div>
<hr>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP4vT26DbMfIlfgLMivVG7lutp701B9ejeapkLI0VrzVKU8LB7Rpp-MYYvHCktEgy4TwPnuSREmON4Wgqnpg6e94h0JY4LkYOnXPMN38jKz_2CxCvBFyMVUv5IqKYHIOzI_iupWrldaIQCXB6B3dJ_1nmo1ISta0JCFR6TuCeRLpsT2FxwY-Cs__7LdOwJPjdg5OhJo-vLfkb4KDFDmmR0c8r7vByxc-jJQ0sbH-anD6KNOyB0dAep2LXVaWTZQKuX5ov48GOGDHNaA5KTuY-9ndEiIVOpMPW7skJsiSszP25K61fdyg0ON5xH1NR0p3yNkRHfuewrO_X29ytGiHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vs9FTKdeDZgvZj0MBKsAA83lOMf-tZY0ojRCx73d_0OKQ_xVzYnLIi3uWnZM6flHqEu9JL0GRWpirffggSRbWuvSjG1AU1Ft0ie_q-AL9HeYxnhKkBat0lTdS3cffoycKTI8qVpBq1MOFYXaRIb34EstwnItTl71qoMFUfUbhsHafqhHFC6gziVrNi82K2sCwPi3AMNC_MLPi1Qb_7mOJrJEQCogkCnhPjRWKR4f_0gWxcrRwl5OJs5bvVlGdMYo3jNibKSgQydmfaqenaf2aZaCRlm3HuQrxhWiXl8pljXQbz-a7GP7hD3-Fh7JE9GhGYGonz-hhWXYRAqcZY5idQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vs9FTKdeDZgvZj0MBKsAA83lOMf-tZY0ojRCx73d_0OKQ_xVzYnLIi3uWnZM6flHqEu9JL0GRWpirffggSRbWuvSjG1AU1Ft0ie_q-AL9HeYxnhKkBat0lTdS3cffoycKTI8qVpBq1MOFYXaRIb34EstwnItTl71qoMFUfUbhsHafqhHFC6gziVrNi82K2sCwPi3AMNC_MLPi1Qb_7mOJrJEQCogkCnhPjRWKR4f_0gWxcrRwl5OJs5bvVlGdMYo3jNibKSgQydmfaqenaf2aZaCRlm3HuQrxhWiXl8pljXQbz-a7GP7hD3-Fh7JE9GhGYGonz-hhWXYRAqcZY5idQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IotlhauxxamIoDVWB22596GsxhSImjjoU_l-RM3CIcp0hXl4G0fOXuVibEkxZIx2BZ3mqc6SOxR-iwulyUDdr9hlT8tNAGFOy4zwZxBuBsrfofLanDNYJxHgzMdi87aIPH3UEWDbmpJ0G075KHvCuGJnoi3k9WVlLN1y3K9dmvOpPWMvlQJt9EEtsagGgdeQJ5rY-womaGpExALUJnuXkEBji9W1a2_UVWLil_PcUrc-0Mt1gc4nJhVtF7iYrQx6Sdb0ntH6iKm3gT7cR_6NNjOOwivUuqMgb-nsEzDgW_p1wGaqx_6IU3IkfCEQ8-L0yys12NA7EHrx-hGYWYCH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh1gIiMO26gKmECsuBu-x7k7PHtOiBsdlmJvQDDWm9Iu4VRDM9H8ysl3rF1ztO0H9CVJQTQJh_gixp93GE6iF9sB08ueqJrv3RxESsmRam-I2-HbdJS1IJIrGrNP8_7obG_MfOEJ2xHxXXu9zQlWev68zWhM3xKr8wUKhZVLxYeEWBfzBhbK7g6LR7GH6jBVtHvZrsMwEeOrEV6FSqYs3gvFK_i9lC0h9QtHkxXPZaYPqzpN4v-aZ1e4KQzvDn02L5A3XfT-1EOpWeaDaC5epo6pbtaeV0e7OZQNvlhitP0LsH4oH2Vw3F-p4NALcS3byWd5oN9vThs7ng8bR0ESgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvHwqgI2ExWT3XuUSw163hbtaLrav_ZRLgUnBBkSckizl2iotJ3uGW8JdizVmP95Dlt-9wN7lZx-GxA0roUBIk4trkNLCcf27_xYee3NIzlB28H08OGwJlf5JJe_4ZIJSvunHLusgqlKwJap83XQmFRPoKuercvuMz8zau-qSsmsMe_mqIk8j07FupptfA1t1jJgUCNQI1Xa1ffiWc3NP4Omhv6KmW58gea19p78DndxXpGl_uUR3HRLrfUf2rrNBtY0WjT2NwKb3_WsxwH1gffr5XUcmRHyuqsnv8JaMQPH66d4HaRs6fahIt3AXf6PESxgMT1ivJVUbLZilcMp4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2eUKqlhmJbtg1wz1NSlqC9fcAUgjXQiP8ek9XYRAWnaIigrV172WEec2Djx3UuWwtQWo2saLUbqgfHg7y_Mss5Dv-KvOqFAu5QJ5pI_gDJyMTYoeN_UoVyKMdYeU4gwT8OdGDtgvuJTVZmGIn5KzMg1zZg54RMCn_KkNKQ8jhcde7zg49GHPYVZm_Y8jEMLnVRnXkzJy6w1z2_KQh_IdOIZ0hlcYg5KmfePYdWyfjkaLIOIA7qlP7t6zKMRhz46IrWpxZ2rZv7ZMpb_d1f8XljoYRhPmOKIwQ7ZbAy6-cu2r32yWc3zE9fsn6ldCgsEM9A_5-FRewn9qTIlfjKedg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=qC7WbJsM-HparEK7d2OMddB3-LbsXaDp_0vPglcL9_lfsuk_H3TTzzYJYRoLaNa32HaCHRjVD_K1tmg2LqeYED3F_D8yh-p-nQRCi89-i6RAen_3koMNcAhAzl2lXHdCPti6uYErb2YTIzGDvQABkONzlOHO-lkj0ecpnaY-E5E2TgAp8lFGOY8gFxppGUjgrlHxq1tsBLhTg8ZKH1Cy4M9sbxKHclcwalhUZTFXeOmFAaPBYVE2l_Is5BJxsY0C2doiNDgWDR21CrHQTpkfvuzYbGRB-eOcL_oZwUL4EsHZTSLz-jjhElLCy4VTvl2owkfKNVwAaNeitVaNu04zVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=qC7WbJsM-HparEK7d2OMddB3-LbsXaDp_0vPglcL9_lfsuk_H3TTzzYJYRoLaNa32HaCHRjVD_K1tmg2LqeYED3F_D8yh-p-nQRCi89-i6RAen_3koMNcAhAzl2lXHdCPti6uYErb2YTIzGDvQABkONzlOHO-lkj0ecpnaY-E5E2TgAp8lFGOY8gFxppGUjgrlHxq1tsBLhTg8ZKH1Cy4M9sbxKHclcwalhUZTFXeOmFAaPBYVE2l_Is5BJxsY0C2doiNDgWDR21CrHQTpkfvuzYbGRB-eOcL_oZwUL4EsHZTSLz-jjhElLCy4VTvl2owkfKNVwAaNeitVaNu04zVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=T440vcuVGF-QJSp4m9H8mssH0M-Uuk3n7tFN82sJXx42dDKs8UjCLhnoBVCZeNMEp-9totLFGT10HFOchwY7cWFwExTbunidiNhz0bYh0Gci-5Ri5pXFUwg2aE-c464GYy2EnsBCHuC1w6mJOXd0MrapNMDfWTXtbpv12IiyfVJMwQFY53lz8nw8g6nmy6FgH922mVovIu900WhAlAX03MIBbNw-nO2J-ekIJV2ffPpvqRpVxe34_GGq0_UrMj-n8SFplHcfXfr2cKjkFWxqdCHmMI5OrDqHWZgZ1gFDoQydm4QZgErxbbFTolPJCQ9_mCNcHmLrftTEIlP3e12V4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=T440vcuVGF-QJSp4m9H8mssH0M-Uuk3n7tFN82sJXx42dDKs8UjCLhnoBVCZeNMEp-9totLFGT10HFOchwY7cWFwExTbunidiNhz0bYh0Gci-5Ri5pXFUwg2aE-c464GYy2EnsBCHuC1w6mJOXd0MrapNMDfWTXtbpv12IiyfVJMwQFY53lz8nw8g6nmy6FgH922mVovIu900WhAlAX03MIBbNw-nO2J-ekIJV2ffPpvqRpVxe34_GGq0_UrMj-n8SFplHcfXfr2cKjkFWxqdCHmMI5OrDqHWZgZ1gFDoQydm4QZgErxbbFTolPJCQ9_mCNcHmLrftTEIlP3e12V4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTMIWD1-xdGTqweCeUqag0o1TG4gHj9DxoYn5upoO8hWAmRJD5rU9ukB2Xmm0bE1sdTdsUiTtoU_exALNiA_KjIyTwdGNlrcZ2KSpZWQ1WLrNKTT2qnq-YBJTWOEHUHDFl5uavXT0DjHG25ShvNOc-0txndAC07k69KhLkcVbHvovp8l_WbA5tWhnS4FQgKnCai1wDir0mIugc4PG3fufq9YDmVbdOr0hhym_XBOFBozgSd_KslAlKcldvq401wtMeMp406PyC6YBWxogKKglNhJFeV-DNzx83ZksFAr6GAZGZPNyBZm8DpxxI89MOU_5DROlUL38TyjxQiF6GBiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzu_btavXw3ZvXCs7ahJmIaW4OCkUBMHDw8qv1BRtXp2yK2flhKuDsxudSyXdnBwvU78UbEJ8mE6Ag7osXRXeVEyc5TEzY7d0LgONr1Cgk4DdxPrinua7QPiPXQvZvci_OXAvx9omeOA9I4-xW-i-cSdTdkFgi0U7BAaDRSYzhMYJX0l0cnQwYznshk9mUUneiHo1EQCOept0TvV1NG-rCG-Vnm5D4N6Z0h_yWqKQZzOM_ko6_0tZVAU93uSKbPVFypYSSBEoeb4kInopCHvT_6Dm911gR9Cn2HpaX1VJmnP7O-5mbdoAvhBjub9gf4thYmElvfZmulIpxfnqKwyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoRCWhwEdH_iBxludJ0gFH_UeZxBfOIbeAhcWsxVUm_7A89uooNsIa7fK4pOATxIA3uQUQqEmmskIf7eXflZBnkYbGuakC61-QjJ9fmEwxyc26t3c1rCp1yf3FVmhZyBSN7lyPLg8krxRUaKlbrEny7QkipzzoxQi5jv7eDkTMxJ3Vicg3r-Vbj2xmV7c1LcQErKQKhv6OhdpNxvmx1Fd4Wfl-H2CbQOz-oyVjT2IwGY48DqtRW_BypUe_tYJ6sft3ckMzUVzSZVBF_ivWtXXUrM54XJpBy93w7o75P4_cvl5YT6-VvpKiBpOGdf9b3_QcfI1w7cc1Wy1N3_0c6LZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K87Mwa-O6RErFSJQgVQlB-LtnCO3WTMXg9wEycCTHwNNE5Tc68Qm2kx8xgNJ_z35l0eAC20o7wecPyzJYPB4ETGRUnRn67h6HKolo_W2kYGxTvIPWhi0j4ku8tnoU3mIlEivnvbexyMzAXaQ1wmh91QQPndcA1UCvIHtNM36JJgDLd1g4JScvFZZt6IpjOwMHPSTYnmJYYeVzeJevs85oFVJjjcWpGNE8u9YApfSm0yb8A-GRNznNqrz7SvCjZY_TqklfYEncKE3JhEf_vDXSGm5bQFVXc5LSBH3IiNQ5WGdriiN778GW9opo4kgMVz2fl3wqgg7yvyybEYTt_B2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=FfoTNj8legPZTKljj3RK7nMlRHIlIVy_JPg97a5JK0woBXY2V690hnwl8ryse_aqrCjv0Tdj8r0a16Pc5WkiRftoJldBmWER5FRVKfkQF007TckzLhlHaMdqC3FbdxyhyOG7kJxOGkUIT44pQ3Cnl-_afGOuUQOBGo0A2ZElAGvK5DrxV7SRv2smLHgICuRUZCTgMG4oSpUQA9xvHWIUThxyljV3-e8AD5XAdO9D5fXruoSPS0k-iC6hsNdDSSX-m4RsahSJ9I1JbN3HG7LxqZa8HsmWCYW3yQVD235N6Dwe0rny35pd9XXXvyUh_PiGLoKRuAYQAhQXOeTImVzTVa5xLl4qjmbXk75iSotNJywEIWQ2mF9FdXlY39yLVLdyVX0w-or0_KKbyCmQOAW5OOTtlDOD6_5tRIm01Nr6M7EbAMpN2a8fxpbbYXrQEQrF2c4JaYeczU2hvNQmZowqXgI-IK9-vnssuD96zLBdPaIiHD_3sQppSTSL9ImEsoIsV4k1dNBA8pLeT0KKI__048O64sCzryp0ZpGlArPpJp36AbcNhwzbesYaW5zSZZsUhVKpf3fux2rDzBoDZJOFL123V9-fX5n4PU1vV5AS2pWa8_6Wgv0wyst5FsyYd9tAH7vbeF1pCFZXlGRM-YV_r5790d1zD4CGHMhEZ5ySM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=FfoTNj8legPZTKljj3RK7nMlRHIlIVy_JPg97a5JK0woBXY2V690hnwl8ryse_aqrCjv0Tdj8r0a16Pc5WkiRftoJldBmWER5FRVKfkQF007TckzLhlHaMdqC3FbdxyhyOG7kJxOGkUIT44pQ3Cnl-_afGOuUQOBGo0A2ZElAGvK5DrxV7SRv2smLHgICuRUZCTgMG4oSpUQA9xvHWIUThxyljV3-e8AD5XAdO9D5fXruoSPS0k-iC6hsNdDSSX-m4RsahSJ9I1JbN3HG7LxqZa8HsmWCYW3yQVD235N6Dwe0rny35pd9XXXvyUh_PiGLoKRuAYQAhQXOeTImVzTVa5xLl4qjmbXk75iSotNJywEIWQ2mF9FdXlY39yLVLdyVX0w-or0_KKbyCmQOAW5OOTtlDOD6_5tRIm01Nr6M7EbAMpN2a8fxpbbYXrQEQrF2c4JaYeczU2hvNQmZowqXgI-IK9-vnssuD96zLBdPaIiHD_3sQppSTSL9ImEsoIsV4k1dNBA8pLeT0KKI__048O64sCzryp0ZpGlArPpJp36AbcNhwzbesYaW5zSZZsUhVKpf3fux2rDzBoDZJOFL123V9-fX5n4PU1vV5AS2pWa8_6Wgv0wyst5FsyYd9tAH7vbeF1pCFZXlGRM-YV_r5790d1zD4CGHMhEZ5ySM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bgwn1u0hVcWAPGPGzw0GbzlRyEX6HTXQPLxBSPfc17ewDq5ZxE-Bruf3__jGXiH1RhI0mXl1gtM5r9g1g9hPY8FEtj9itx9vY9ADZRZf2SapQDd4Vd-EKk5jGTUIkm7TdksSASDJ-6n8sIuLIf8ehlh5yRtx63W2FQrL0X_e7zaf-X8mSDwnzVepsL_wv5ja8DJF3i8_E1xbeXUsc82jKLQskDt6V-wwwrPTeZOz5jrofuUfc-L1IHIncT93sYK_GcPQLTttKrAUUh8dzmc1DkS41qidxD8z3IRM2w7Nh5YTa-qfqILeVVFrSwJUG_5BQGVKDKgtpH9AsYN48ONEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6ge1wPgXlDHC-PpnXxOoCJc7mXq3NBFMjQ9dCBWkZSbpW1xQGBfrmhxBHHSsgXdcRAv3GFrDOXNvIC3d4OTNcb69sA3ce1EIqL4Z0Ch-ClSRqfS5Iibqy1cYbCtYT_zQK5mboX9DrcqV-m6B6YhvkZ7cIUVal-ZhGFK0wfOf4akk67BnF4wr7p-UbDcu8KOEVXrKrTXQp1bWaCGkaTMQe3ZDS-cHVUYWnSBia4fF3BLB8lI2EIxXLGt5SgDT3Pd-GbDgLVuAUnx169_I49tMEWw2XcX1G0wZofadX9Nh8p__7KkQHcv5tepZy7_NW5ilrti7_4kf-G-2RVsoXwd3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Axur_2dRLCv6odLvBlowksYlRklT0ZB4JX8rUHO0gVDcdcfU0PW-JV4hfzaYbmvB8xQdixL9QpXcBXS8yQ1DmIeI8bg7Uzwgan5I60cWdmQphx-PNDdPTCEytEFGpBi3cp5zdDfzdu8u-PTLEaJPDAu7Wu88zu-oV4_KiLd794lzm_4N320v4TLkZLBURz1L6G8abwrTmspSt_UzztBpHtGTmJeDa1yjMNiBLOq0RqdwUbF1LEGD0JMU4PbVDYb3s780bIcGx9ecft9p2MCulxfL6LFiBq-1C26fIbPEaHXee--aHJm8HxrPYhlR-E7Ld_ykzJDDJ5m1-IWj--08Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1fky2T41U6l1l5jnGNGxOiI725HqrR9ue73r1q0HUqpimlV2J13MiWsNcmkieSa1NacMvYaMrAxv_HuygZ20WyovuRVDPhXXmQgP5QL7oowi7McBHmH9EztbBdgn90-FAWYJeaP7QGSyN6UG4Y7iiYNUkzu3mqETaEX3-s3UjhuMYxYML92vcFZ3uqOvHpKVnnr4eHeyo1PSIptBUF1tIoH5ePM75Gf3MO_2JBRB7j-WDDevfzO7vWTCfSWgOJ0aDeKjf2w2UlPPPU5hnkOlUWhR6J89MTVyDwdiY9DG8DM18F5aNZG4oiDVKmj95Qehr6g788yNcfONdZzJ8UpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpQrxyiof-sxqQFO4Jsm5cS3LNduh6wukgUbZ5OZTp512Dejg6mK1RC0nrbN2053reIqK76YtPUZn-e9z7_nwoW1KryYVz23manv99ZBofQxmrQoJznwFmSZi7eH5P1r92sqroz-2Gee8e6YhYtTeT1WZQLpsivvWxlxFYnCvxoucX3dj1ak6fUjmZrvbsrM-ahP1s4AI_J6JtJft6OwxU6YTE83op4vLssOFzXqS7Lw_--AXnwHx6LwghEFPqkALfHh6w4Vvw3xyI3fxytk8rvEjg3POzIv0p4Fem_xZiB0doEs_DL2TIfZBJwJB00KuD-pLXVNi5VmqEN8xl7YGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=IjyhjiCehWOViUnTku5d1tbngwCIa7nTL5fn5vHcwEvKgsgrWpKLMXGZkaS0MZLRI4lbYkOobauLYRr9FJ3XOC4pl53ZzxJlbC_8W0j44socJxBvp1My0jCZgZ-tr3BXoX5oEpV_if0oCPzwAu-0v9piMzBFmaTPWYf6WD1EqqPluV28TCFWpLARyaLcun-WdMpz9Kf310VJewCdIO8yibIIws5Dcaw9e7_H8tBMBy8NQ5VqQFWFOxQEHLmHAeoTspc5a9B0e8992wDt5Tun68y2yC_0YO8HIEPWh6BuwEt0E3BzzGCe7BNhOOKM4TLuZQj50pgjfhKqKx-XIAI7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=IjyhjiCehWOViUnTku5d1tbngwCIa7nTL5fn5vHcwEvKgsgrWpKLMXGZkaS0MZLRI4lbYkOobauLYRr9FJ3XOC4pl53ZzxJlbC_8W0j44socJxBvp1My0jCZgZ-tr3BXoX5oEpV_if0oCPzwAu-0v9piMzBFmaTPWYf6WD1EqqPluV28TCFWpLARyaLcun-WdMpz9Kf310VJewCdIO8yibIIws5Dcaw9e7_H8tBMBy8NQ5VqQFWFOxQEHLmHAeoTspc5a9B0e8992wDt5Tun68y2yC_0YO8HIEPWh6BuwEt0E3BzzGCe7BNhOOKM4TLuZQj50pgjfhKqKx-XIAI7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=YYUgSqWBWQUYJ_HsPoFYFGaDCxB_sv_nSi8VoLDlLD1JhVp35YbVoRwu5kOtDpPbENc8Cm-KRodBTu7KasrHDzurfDZqcWKe0igDg_HvfbGzztoPjJSUaFJMJgfc0-xgW9OJYiJ-VMheT_8WZzS4jLP17HrzmvUgaNnNnovKJ8fRvYIM4rRFsrfJrl-OVU_GFzTEcj1eWR36q1dcrppzQJii7vz9oA_FyO7sxzAHoNR3l5Y8hDhUk4HnjvACGCpgTd1uUVaRBXEb7BYOTbAYAV-ZzIy-wnu0bN98haaRAV9MWTAwZYcpmMqa2-TQ5TbXj_ySYLbrBR8MyPcoSe4WtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=YYUgSqWBWQUYJ_HsPoFYFGaDCxB_sv_nSi8VoLDlLD1JhVp35YbVoRwu5kOtDpPbENc8Cm-KRodBTu7KasrHDzurfDZqcWKe0igDg_HvfbGzztoPjJSUaFJMJgfc0-xgW9OJYiJ-VMheT_8WZzS4jLP17HrzmvUgaNnNnovKJ8fRvYIM4rRFsrfJrl-OVU_GFzTEcj1eWR36q1dcrppzQJii7vz9oA_FyO7sxzAHoNR3l5Y8hDhUk4HnjvACGCpgTd1uUVaRBXEb7BYOTbAYAV-ZzIy-wnu0bN98haaRAV9MWTAwZYcpmMqa2-TQ5TbXj_ySYLbrBR8MyPcoSe4WtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDAFHQIuK9YzZKpyEGSOoAWyWefHXUVfzdC9_1tFF4NuRKxAqP5QD-bSo2aNaKqCXMpYC1xUZC2f4Avkli61WyOWH2znOtPAAc97fSfAxp6DkFaLrA6yFnU8Sm6g1jfylXB8wlqaJhU-5QQkuXT-6OU-N77YI4DXGWOF1dky6M1-RGJ6MmdK1RQyjYricmMQVIioR8hqi5diRReeXw8tLBdf38fGhGT-cX5_aMuJ8RJNagSwMmGpWwAVKnHNsuVxPjIFavK7HGd5HgTYLG89d1m8Pbx3QO27WFgYXgy2pDmZdXtlVG-JxJ-eH2QAK3ebuJ7CjqnH1JrhYFTY1veYZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIZIH5joo0bwcXFuB5n2cuHINvj0GQo2HVljIDv3JVdC4aYZ04afpNqN7kd5hbnKGBO12kcQV3jMyR0zb0W-06HHH2v6-HyiyYtkj8LJ9KMNl-mAwB6urSBBAmcKG5qn6CXd3AJl2-q1AZXnfDN3a_IYzytG9djxaIF2q2UtpEtjr86XBsufakfJuy3MT1EXWJXUq_UlyiBb3kZJl6WVwQxX-47aXUsODw7mdX1SyQPiCyAD9XJseN7PKHddbp-ljB9vzxgGGvIezyx9u3vdSw803ZCepZ04oqWwpnXaOuoPklNZbox1v_H8txMq7S__nFKQ3-NsXVxYiy8LTTXUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=RXXUcH5cprFUT4HV7FZxIbUR8gU4J4IpHtCxRiHd_CbDy5_i3WHWtxQikHNh-Ip3YZaprw0Z29dJU5XsuF4w8N7B497BbgR3-snvcITdEsWi4yBavoYHeB4jLfwFesg2kQCGjln7v7Jd8-KbG7G2SjuE2z466eBI1f8kXi7RbxOZu5_61xzofr898Jkvx02L2HYWeG_mWnV2zAfW2YhxG618G87gCM8WOjylffYB0vE91bYkq6C3SH_oqdEHi63A40QMKNrFpOLZLt6Uz-hSTqbdfpb6rfOrv9dUH4n0yoK9RoKrok7a18A05ewJuhXfB7nPUN3cyMN-b3y8W2O5xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=RXXUcH5cprFUT4HV7FZxIbUR8gU4J4IpHtCxRiHd_CbDy5_i3WHWtxQikHNh-Ip3YZaprw0Z29dJU5XsuF4w8N7B497BbgR3-snvcITdEsWi4yBavoYHeB4jLfwFesg2kQCGjln7v7Jd8-KbG7G2SjuE2z466eBI1f8kXi7RbxOZu5_61xzofr898Jkvx02L2HYWeG_mWnV2zAfW2YhxG618G87gCM8WOjylffYB0vE91bYkq6C3SH_oqdEHi63A40QMKNrFpOLZLt6Uz-hSTqbdfpb6rfOrv9dUH4n0yoK9RoKrok7a18A05ewJuhXfB7nPUN3cyMN-b3y8W2O5xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=Z4nbpuF8nNCwv2I3Xq7nwXImIsbqe-ZSAYURdFl2qdTML3dBCFw5jZleXvC8UskzY-ZYCSimjq96K_wiQ20VxQQTvCZYcL_64EE-3spRVmE46ML70SGkqvPWEPiEPLBAChSkSDPlBEf8Bs7DVp1OWQewtPTXyzHWPZLsSyHizymxKI-abZkrreOkw3Pf1LFaWJHdvKapKqS4h3txsJ1IqJD_l_AV-3cE0sMDgyfe9sHCDV2VpJgHGvnb4qEQKVCCz80i6kuyLIE2SjOSm3ySA2sb6Mph4P2qc5T7rNoWpC1jD9SmVq684JhT06U66U52id5G9ZA70rct7stPcxfKaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=Z4nbpuF8nNCwv2I3Xq7nwXImIsbqe-ZSAYURdFl2qdTML3dBCFw5jZleXvC8UskzY-ZYCSimjq96K_wiQ20VxQQTvCZYcL_64EE-3spRVmE46ML70SGkqvPWEPiEPLBAChSkSDPlBEf8Bs7DVp1OWQewtPTXyzHWPZLsSyHizymxKI-abZkrreOkw3Pf1LFaWJHdvKapKqS4h3txsJ1IqJD_l_AV-3cE0sMDgyfe9sHCDV2VpJgHGvnb4qEQKVCCz80i6kuyLIE2SjOSm3ySA2sb6Mph4P2qc5T7rNoWpC1jD9SmVq684JhT06U66U52id5G9ZA70rct7stPcxfKaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZmym7JxLrErnk5R8zlhYJZ3rZzeeDw2lGLhKHp-6kl3Hk9hLanj7hxn0TArKQR5MNRkUQVK2rYkGDyGEhTsgvLnuKh1noz-MY20ky03-TGBTQg60PO053ldNo6JSfxokiLJaue3krAMM_i1xVpl39nRmMrldLLfN7KGT2RSmpAG8txnGA0FsWjkQ4ZqDqCVRDFZ_KTa1EFOXc40faTQ4Ii450vX4F4h14xQO_I2oG_f54y-tD_rIv7zSx3pw21faXUHpBxS_aZlS4mDhVZSUrVXDwsFPyCZrXWaCyDWJjAd8-ToAzp9Iw9s8HBpdz_xG6jSawodXYxE1Gr_whntxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3IHluPZwSz5Iv4BPVDLQ3diHVRrUYyfro_cnd2fp8uSmg3aSAr1KDpXXXZCdCnZUTnkbhDlC1iDxbr2fSOysLrXEefOR8KrWE_Mdx24cTzDgjm37pjq29HiypPooIxoHH9kUdcUIT2PliOt1m-ooMY1lcwyoTo9_MFodt8y49FbrcRnHpVXO_Tpg-ANCbiWx31D9UD25-wIG03Y_f8GcjCbo4mq8g2NHMwqxkxGQ0_IK1yBYvVaSmEhHgagdhM3e7PebEpP2wcrPBMZqr4GdbKIWJ8qAWM31WBlhn6Gmpaup-cwG5Y6fvIlZRNnhblT5XSDcSgIa_yMGcwy4UGYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmOiKzswWjik2uz_epHUPrs-HOkhqAyYLlNyb-cHWn-_hfKhH68QoABMeHokn_w2DMKzhtiLIxYirXphMKJOMin0lyvMKR9Aaw9sxfnKJkBY6V21Z2MmFg1Tnr9amCElWY5nA-Qt4ugnDPeNGtv1PoE-ZwLweObfxOpKgggAXwp-53w2O5G10G1lRE4XFaV6hyVLH38-DJ_0rV993hNG4Y5yOjqFR75lHlOJxmYAtRrQIAXnV_63qgvNoMdsSDJj0zuJGEveVRdkrEpLpgGJ_LbV-sV8wLR66NTHCEma2caJb5BzcSWK5Xvw6SG891Ue2JG34ZRmVSCOcHqdwZX4Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=mw3DeLTvYjf_bHhJVlO1JXl7873kYHewbGdZq03bzIUgN_ILQns1OWZVXlPV0ppI3lQ-qoo6rkVnx3Kf2LdGAftg2cz9soelV7BT_Ooc2j4TbZUqi32TSucSaJBNL6W53gn7EzYsMy_DghESi9TkgPfYxLAx6IndBgujDJiCyj1laDwh5EZEoURUCvTMXAtdyA_y2yEWo8NRzLmNyTGdCuZxjq2bJkxhUkm8SmRE8LEXOUOk0NCWsRaQpKkioSwCGefLzTtEdMx0e_UspOAB_-EtQwEkROENTH4emBcESWZdqAyr-dDIEjD4mahwhXTDVdSGHl8-bYVCu-AsMNm05Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=mw3DeLTvYjf_bHhJVlO1JXl7873kYHewbGdZq03bzIUgN_ILQns1OWZVXlPV0ppI3lQ-qoo6rkVnx3Kf2LdGAftg2cz9soelV7BT_Ooc2j4TbZUqi32TSucSaJBNL6W53gn7EzYsMy_DghESi9TkgPfYxLAx6IndBgujDJiCyj1laDwh5EZEoURUCvTMXAtdyA_y2yEWo8NRzLmNyTGdCuZxjq2bJkxhUkm8SmRE8LEXOUOk0NCWsRaQpKkioSwCGefLzTtEdMx0e_UspOAB_-EtQwEkROENTH4emBcESWZdqAyr-dDIEjD4mahwhXTDVdSGHl8-bYVCu-AsMNm05Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrxhNvzo4WhSkhRwUowmmP0BswsKyz98jxKi5mrf84cvb1vC3NBMUNE6n5cQqSdC9i0npD2DZOoLTQQHIyOzTC8swbgg1Y9DvHUmBFxEsaULDVc30CdyX18MbMeNk3UEZmmyWMkJHHTiMBbbZIIqeH1t9DFA24-QhTioHRuy4XyvPsE45SYf6wKhUNWTiGqHZKi48XSh41eLTZbswg-HMh0pi5CCpAB44KEAak12YXPY3fN1KclPZDJMWUeKkI5JpIyWGdQmUBMqSxbOGRIao2O9jx-2By_dWcrBrzyCwh89a27NBpaVwR1aB-fbDpBMhd6fayWR06UkiSt1uj4A-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O33AQGVxnsvpo2rk63K7fVxEm66VDad4DgI5ZKDvUjBStiK_jo5EfQcsAid3_g_E_wlssyCmh52RYnvighMHwxG46xDtinCG4IEz4PI4CgkS3syWZjgbly3BxSHFZUx_4b5vJyVD_Z6OdcvdNCLuVUm63Vw26mgLQEVPbTbwBst0QaCTxpLtfxii8zsuwr2_vvEOqK_psAa3RV2OtT3F49NKNzzYfnrEPuK0dutK9WINCbKe35R8NW1pwRXcJBZKzU5iLdVoY-39zmicLWnngUtnp1PgvQiU7_K2x2ZUFMFm20aChtKHT656mhKPPOxSs2JQnadxGtGh3eUFWz09SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpDW-cmrvkunOsVaepjtWMV3mzxR9k2Iqs8BRWAR1mpcYZqc06BHJAt8klzTwJERnpTCE3eQ28YE2ahqhr3iyn3oH_wFlEMtEkucWT9aYUovzMF2-MZ2LqYuAxY2dbKu86PmEJdgfq4eADAhyjCRoDhYTRLjuemgf4oMJ_jmd7NQom9aIVF9PD1zfQezz9m-nZVN4QB6pIy-71ObZeBO7eIBOnzTWhuaQXioywL51bLbN7odRkOIyligCel-NQirrqFc8CAMduAlGhnKqjAKUGQv1Yd-9d95e5RX5AN_8vlN46yFfAJdFesUfoa4COkC7UwJfMKz0-2ppmH5dGihAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWQg3OrA-SY-vJ9dJLMCvYlNzttlHDQAxcAyvC84Do6mcByp_C85VrX6h-0WBpaUSazVdmZDM6g5MF3E8uwTW61vSa3KSeCA0SgGKRmhMMBQAWQ3NV-yGDfChhwCxpKYRqOEF73DysBTQPJcvJAQc7Y8XBbCWOB8dzvQ6hgtahI8VknSU_lljyNlxNrhDeBuFucKJwOEXLoEMCQexdERLyuI_dgUoq6zaha7EhZ-2JR15iV53h-7dx381CULOL5K9uAKRDWSAQ_ES_xRmAFqTrA5_HP-HhhbjV7jovGa-w8w4Cw4Nd24CobdDa2ZRZkPBMLAxPrKbQME7n_Hd6yTAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=MiyiUqiKz_GC7yk8lL4xyhoIuvE3Nhikz3WuMwqupcgWwiW73nIY-FejuKWXZA-pB6nuniWtsoR5udEhcjDzKVXeqQizbg3JMBKYftbUyK0s4NloE2uv7eFMz_6GXV92ikjf__3gAcNkgyGhYQTRNMC6Z_DClM6bxRB4-XJQkgYal8t27XajbFjHpGUH5_RTQeg3J7MP9RAQxUHFLSiMaCchluzMaidFGpj2SfR75XcGZdBYCTfpjcXzguqZg8lsA8WVaNkqtiGVRv56BcoGT2KlY_sf5dv6pBAuhqt8X1vdMNFlEsCPjz3na_FC2RTMelxFNBSIo9pQMn8VMvESew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=MiyiUqiKz_GC7yk8lL4xyhoIuvE3Nhikz3WuMwqupcgWwiW73nIY-FejuKWXZA-pB6nuniWtsoR5udEhcjDzKVXeqQizbg3JMBKYftbUyK0s4NloE2uv7eFMz_6GXV92ikjf__3gAcNkgyGhYQTRNMC6Z_DClM6bxRB4-XJQkgYal8t27XajbFjHpGUH5_RTQeg3J7MP9RAQxUHFLSiMaCchluzMaidFGpj2SfR75XcGZdBYCTfpjcXzguqZg8lsA8WVaNkqtiGVRv56BcoGT2KlY_sf5dv6pBAuhqt8X1vdMNFlEsCPjz3na_FC2RTMelxFNBSIo9pQMn8VMvESew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKSfusvAkElMd2kbBAEG3P-Zf-4Zqo817pVFIyyEhjcxKZSPPCtAybWTHoTcILQuSFFMpNTRvSGBqp9BwEZ5DMRy_Jsl05lrcmu3ievaAaaNSF9lDy5eXOEF718Ox242fipY678-pQLmYMsWHXkgS6gzJgWGAlRvoQrfyq4PQjX2z_2WbCgHQ5Mz-ki6CiR7OYoMbYd2lTam0SM9fVUbA3fKHtCZT1s9mVy7ErKZc6u92Bp7v9LlxxHgpp71YwK0uTHEqien9dmQzzFFRVdxpgMGTRIM5-7EajJJtscI0rUucmpQbJ4XuVSKB3gEKvLUrA5be0Bau3l33zEnb05ZWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9fnABV9ve7kkBMc-Lj-T_rWHNDGIm8Ud-6lTyy5InY4bJgf9liLyNVtJDPg7epPe7OTnVDueq7ESUtKSDLT0uEUbYRghIKIs-q2fweycknGuW1q9nZlCx_Qq3V0yUKeOatDHR99RXUhYrT62isjFiBitDyyP3WWI9hpDtX_LRzkq589XreA3f1nBZYkTHDQwkapBnF4Pv0kBHaFi5bA6KD20Y1GDpWCBWiVg1TCmyTJINWvqEnV-mmZD-RDSX7hiZWe0EeDZqrXL8ZTc1mSgTfHQikgX0Lg9w4JbxBfE-RMfwOXFCm00FQNjkZab204Cm2perniY7Gx1F5wkDVvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2NO7sciXwhp43WoD-ejt1iYA4QoX8T3jhgYjO2nJ2X6XsB01C-Vju_jJc6FkrGTthWci2fgVTDSYS_0ci55daHVxukZXybjN_N1bykI7MKwjwSN7uTE0nUWT8Fy5iyRGaSqaDWI-Hj10ymOuOUMRUdasC7xeXDlbls7tM2qg1IbfrcAlY328mFO8Pk4XHKaynYvH1E3vbSjvvvt6ca_DWnYzjThZD1YcTj_ZVv6lDmVEwnjdOsyq-_Yq-AAyWMf6a76Tz_kPcd4SN-rDu9kXOSJ7drEulKbQGEvK6n_MwJ8Waq3PLgAh392_dBvVNjUqpnG_Hj4zb75wSjBGYOjYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=F8v8SHX81L-fOPrbS62ZmVwOgyqmEvXageJgwFRfUELG7-mCZVcTwx2WCcSd9yq-2rjUmM9Q9vEzHkdKyjhwqHmSjvP_MoKR0Ocy_KKfSya7WZiNxPNa0scLSKeRA0iLxKPd6gGQFeD98wtokjFSCLTjBU71ykIsFB2fYs4Lw1OQ3TXztntvyCtnvUJUsSvIPkx4hKtT2DCv8lw-nZPHLaENmVkkq9TtYxySpmOsIR_GfkfiS3Qd3auxvqXCi9fowbQhfSG37s8HHV1qc3R-M-RXWk6cEaap_6-lk1AN7VRW3G_xz2earBTygu4n59PMm2t9rDtbZ4NIkXJiZ84Y_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=F8v8SHX81L-fOPrbS62ZmVwOgyqmEvXageJgwFRfUELG7-mCZVcTwx2WCcSd9yq-2rjUmM9Q9vEzHkdKyjhwqHmSjvP_MoKR0Ocy_KKfSya7WZiNxPNa0scLSKeRA0iLxKPd6gGQFeD98wtokjFSCLTjBU71ykIsFB2fYs4Lw1OQ3TXztntvyCtnvUJUsSvIPkx4hKtT2DCv8lw-nZPHLaENmVkkq9TtYxySpmOsIR_GfkfiS3Qd3auxvqXCi9fowbQhfSG37s8HHV1qc3R-M-RXWk6cEaap_6-lk1AN7VRW3G_xz2earBTygu4n59PMm2t9rDtbZ4NIkXJiZ84Y_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=kjApF3zmzSiIT0NF0kxwAkj2OpDf9dBx956ItHjpEk5BnJz6eIUi6YzmIbV_fHkHNlQLA2jUiRACKPFiOeHq41PS5jTEW9_x_ESWcFP3EJ7SDVDzRlF0Of6qbd3Idyl9zd3ff3NCV7kTAEQYYUuE8PWir81aJRZTnzuyPtR5fVrtaFUnZv0Diz-iOe0xFvHrpNP-c9n9VNCl8Gm1fQx0hIUcAQPOO-sfKM4TQWantYoQ3Ppy1hViJ6OFLFXu9W9iQZzuv1UwWhynCULxBV9wEOPUn7gLEGUhKGg2fp108GXZE7Zr-FaS7so_eG0wxi6YcrNEKoec_J46OaNcNRUz7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=kjApF3zmzSiIT0NF0kxwAkj2OpDf9dBx956ItHjpEk5BnJz6eIUi6YzmIbV_fHkHNlQLA2jUiRACKPFiOeHq41PS5jTEW9_x_ESWcFP3EJ7SDVDzRlF0Of6qbd3Idyl9zd3ff3NCV7kTAEQYYUuE8PWir81aJRZTnzuyPtR5fVrtaFUnZv0Diz-iOe0xFvHrpNP-c9n9VNCl8Gm1fQx0hIUcAQPOO-sfKM4TQWantYoQ3Ppy1hViJ6OFLFXu9W9iQZzuv1UwWhynCULxBV9wEOPUn7gLEGUhKGg2fp108GXZE7Zr-FaS7so_eG0wxi6YcrNEKoec_J46OaNcNRUz7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=X09vKPozo2UuooEehML1sjHNzAJQ_cOW2GOFfvvzezOjns_cqiHzSFQnbBjFLWtDSqPNVw31N772zpUhbrNQusl8wnaQ8xEB3SUGbd-seQtqFJbcGuS6V28AScpfHXX7dehzeyY3bZK2kpyjLjuMUbnC2GMoS0aXapHPjf9AUhqj0_iZS9VRJ33PasHyKY3y3YxQcHOOeZx1uD4rTMc0XU4ykuMVhLOQVlIy1K6E0gIDQrm0_c4CE9LsuEfMaXOyygoKNQWBtAodjsLp7O9RJw7p0jKx6-GVKczGj6Chr34udaTTcxpfQCyOPTm5rD3d1z7Jda9XFH4ulAXLEmxLZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=X09vKPozo2UuooEehML1sjHNzAJQ_cOW2GOFfvvzezOjns_cqiHzSFQnbBjFLWtDSqPNVw31N772zpUhbrNQusl8wnaQ8xEB3SUGbd-seQtqFJbcGuS6V28AScpfHXX7dehzeyY3bZK2kpyjLjuMUbnC2GMoS0aXapHPjf9AUhqj0_iZS9VRJ33PasHyKY3y3YxQcHOOeZx1uD4rTMc0XU4ykuMVhLOQVlIy1K6E0gIDQrm0_c4CE9LsuEfMaXOyygoKNQWBtAodjsLp7O9RJw7p0jKx6-GVKczGj6Chr34udaTTcxpfQCyOPTm5rD3d1z7Jda9XFH4ulAXLEmxLZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS3jl0wn_VO1wtNulq2gXuK-dkGMb9pwMy5QVuOhctu5bGNXGECTCtdZwI0qk1X70HpqI8fxUDaqzpV5FSWwfjChJhx_5Fw2rVuMdJ9kh_59ncsbqdBZZa-3jD8uhtwDuA5nBTESEcwaCAB9Cx24ueRyKzn71NeRhgyPKECFOd-SzwpuZ2pNpH0K_g2U5XKJTuzsgeRYAYuOc9TNFrMozOsjYqNJwxONvcppNiLFbj3spo0GtUCfMvru5_ozgPic0vrYqIX9wF5v2rY90T29sTuqkkCWRxCi5toShDS_NMtbL283NBCPrmvTUGvKjn92aXZ8YsBNPOAo8U4y1qYrdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYbkrX8Fmkcv_59D38nl_RKhSI_UfjyJey4Gjif1DbCyDAh0bo63wFGr9Y2FVvRFR2AFECCLV6LMDRrOmLHB-ROQ6UG00JTopXq6_F6WDAUVe900X1QCA35mmBWhaDD21URlh6xsgS4fCNxVoFTNmqaK75B3ryoog7DTMV8RbZN3H5oeyZfuC5r_r_UCSIZXevyzxpeixDKCQOLK1v0gC4oxu6X85MUQHphRyYUygPqAaEqP4RGdVJL_yA3-RaKQNzv1xRImbryOg8FDaDHyZ0JSw7rVVc7HQDBFRWjzg0rdpjSj37zIgP7ORQI1W5jCmuplkf6Eka5_nKXiIKXjyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6JN8YQgpxLaMdianV0gWqnYK1xTYO2iKWOv9_ia-HA2i0OfmEfWYd3oemo62ThjYYLQxKfevQhBECqyLGEdefhKUPVmt9vzayzHgaJHPdC8E0nbEcSpwH03FXyh1v6X7_BCEBm8fU0yEj6SYGe0eQ-jYXwaBtugbGLl1djnCcq6unVXxM2ogYleVTf_y6vmT3V5mt2ARc4R1h1twKhOGLwWvVjl9KbNRCBSXfc44qZAaru51qpn5P3S45OzvQovtSOKw0Q63YwdmVwfoKNwJC2e2w17VpN80KT--o6YsUJn46-GM5i4EiuDPTGMagAOgIsnknhTA9fuqNs6SXq6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4QypfyFK_L6tufuN45rrfGtlDnZ7v0slL2k-PXudk-2YMZSYWHbK3TaBTeGjTllAA2xfShrwUaKgfWiqN8lT2ABPFaV7hQb2zzde5bjsLuZ7fKEqhLg5OJMWrXQr4GJ7smge47qAq4r03dqT-2GG65DUJtGVQg4mIorxBAHX2lQMSi9sa0enyop8BPWX7kliew47DDTLz1C86ZG055PuWC8X03JNwKJ2Iqo33670CGmofUH7b3qyt98j2xFTrTDuKxVgEXpnO7Eb5ElV43GHr4RXhHUdR3zi_1y0mcwWCS8Zqk2AKG4R0Am7McepJgQbSEO4cLT3iRmSi8AZhpIdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAHsNpEY1zGaqXQyol0Ur0WOwF6QYh4z43eGjc2AV1y_w93y74xV3Lerkwj5zK58f9rn0gMFG3CX2OhKegeVVJZR4AxGODkmyoru9QHUFhqGk5w54BSgskSITJWQ_SIDZqrwRpQR_6eYmlNCUJpS9BUgyjpRoxxrYibotguVFrLl4gvcu8DCLOPX20n6aL-riKIwlITmpojPo4a1ZIK7YPEKckxjllf0UbrdPH1XgqsXXOTHndGD5yxypYhfm1RPmS5RRIiXjTIMZzny-b7CHsZ7sib7cYzJvSBvcmL4LCI7sxYsQatDHnmWwkih92e_B9a2JSmcAW48-b6XvVnE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnI7zIsvTRJYwVV_tl52T944mzMR6pPb1LTQ7hjv4M8lM3zL_VNPIoBR65f3eMujR4pM_CFzHEX3j3XPELN5dgc_JmnYYN2WH5BrS60uZyAi2LTrxxn32zIVJr6xGaKfxLej2ZVDWmR12meQFtPD0PA3PSKub2YY3BE364N3DJz91NuZygXoyB2dNNICCfQujXF5QAE-MRJ-D8xgMB59cIiEXqahInABqL527rY-ZC2D37PNNN9c_N8EpxMIUrbvoF0feS10yDoHMO6Uc43Mkofs3L6-qV4pxhXScTvoQrkU3G0J0YimzCsrVdxIPAfaD1eeCGdsLY4PmX0jYiWdAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnYGMKzYc3rkCfenHnJ6J1iIqkqlrcTLmQHeQmmWdGcrnyXyySBDj1U6pk7K5HawKDBbQUmV-hW1Ma-hMMcgqXSVhOA4ixavznImDXm2geGDviBA0YzoZUl-3hPqhS6jSnqCQfUtiaQoXM2GAb3behEc8PPY6aV5s0HYMYFgtdb3yK7kRB1n4XAitCkYERv5TFDiOfwME0T_UmWoZfpKu3DmFlYTDdDan3jcrTfK6bCrzmql2bViQTJtw1UjF4BYg4hKimEKIHxVdwzceS03ZmsDtyMJLT6Gu0iRx-UuB3jgmJy1ZM-y7dU2AEQBlv2v-3G9XFCLzQig96rV-bkgUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH5v45D01YMHSiklxI41QeiPgKtli6VdkAFaC8_Le-tYAEkvvMFWssf0sx86cIYE_4vJ942i-CaqfKCqJe8BCekrhTOqR18doTsiO2yUflp1f1z_hbVa7uAv8yX7MKbGgobgVujSrrHD4uiLGNCRYzS7nfT2GbFjwLk2Iof55q0AmrZnJ8H2qedX7g3ktIzmUXYVHv8zD2h7d8sqn2W71skgYKibYqN80WZcs94iF02izxIQrxtmsniSXwdnqlduLuIgyXqzZ751VmtYQZv9gkbgxwlBsQ6fPstr7Kwj3tj45xu5gUSk8yxmYyznCNqLeYpT4KiZpD0yOV2rUysAbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsszbZR3EOlv00CiDuX9KfgbZ77mGOXA9APzEN_gGfuLf0sW5k5XPbZvRRpDH-HMwyTxXARwR8XbU73uvPIkz93DVg0g7xGYCgBVtiNtwwwYgsf-0cA_NRzWjYT4LxvEWVz0fXSYelVO4xERJbsbZyu57I8DuTBl4QuBif9FaM23Lw-BIJI_sACuSVnOwEUsCGovmTEfs-i0XhDR9HUbu--SaIYUTjoscKy0xCvUHVjWba41EvVF9YU63o4rhQsiQ0mUG12j_rNKsv4Ooaf4kvX3jX6KPYoA7Zb_E80zcRYdE3yegJnbE0-CCQJwpiLs43x2zLUWR5OSz9ghi8Aynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-d9cN71rgwSzah7Tz04N3IPN-_eCZYuzEIK_RB_saaN-LCa9SabIj3mxUlqu1DByUFXjVT1_HfwYbiQG4Hv8AnBJ_ysl8_WVU1z18XWkc8Md_4Nd1xkgtR63-NFuE2kOkuNbogby9EdraJC93zJHyo1Ee6JVNpj7zkfalwMZWJofGTW1IcMG9UYR2lYh5T61OXbe1z44vLHLW0E3XcFvmvg4k-0QNy7Jx4EICS4uP_ifKdJJ-FHdUXRO46cYDdLpO_puOr87TznwPRASoCs62BdgpcvfzIihowLfbyiy72kQ_B_Q6BPw4op8MsLDTDBkuYDc3gOdiPKP6Og6b6L0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAT5Vy4WArUp5zNuNmZ8EUAPN2lEV9AgzzA3fCcFm0fb4o4JnVdcIj17STUJa_ort7N8NZxJo-X5dD_9Fo1914sGh9szeyTVE_fhXEzny3dpNARVxqZXaN7rGCFNZ9-6nfQpdWPmlLjsYh7Q9Xrkas5JvtCnPcAUgjfOiOkXU_GNyVOLOc4UzO9gLn7ERVyk5-kFRFV0Z6QpNuom6O0lOsUvM12Mgo-IbIt_iyCAIHXvixoPwQFrENFNUnYFm59czR8AseJ4xJDg2kBYhzYnerjYTKwFYDNHKbHyuccaKG9GOQvHrl0-IAczJLg8lTytgyzr72SbihZQRLK44x4bag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya9XX_BQnFzRU8pP0OfSsQKJea8RAFmObh_Fn85RQQ2KK6JqfzJjpI4xb5Tg8nL_2AXRinCkgV0_0kJgvbuIKCl4yDf36Z5K5C4yKQ-QESCsHU5PHCT3am1sQQ5HTED5Y6kQTohc2qiufTQOpF8hnj95dSN1jdvBwjAlOOvSK95rU5huKCx05DH8jGhPYh4rSi7P6PIJLQYy05u0dzbW3WLuXUfh85NTftjOs1wGvhrbF6uteOlCQk4FRCg_TkCOpKeqYz_jNnWNvKJPYhexOGTSZnmjs-vBoHkUmsmLxeT_VRaGUgymk49duSM6By7SFP19aYeacyMCDBdXl06jnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCBNuD_6Lc2h7NDq9LpOccumX83qX4AfRezd1uvQ2X4TS7rrOqMIsskaWYCfSIzotTxQa7T61C-lScDeAUTb9WlaY4gG1yvj6ZBakShbaufJfJbvcFt7nwUeCfkjKTzBXbL5rwEvAQibxn75dTeX2nRNE7YV9f1brGgWLNo8G88fBlC8sqc1ST6aWOuN9TFQK9NCJ6qWVfCVlgsY_K1mAwPzZHgh6UlSXf6bhuzFBfp69AxTMmDYjHrKYS3-eqizWC4OEenEOSxHr3-Ow_C2PRsdqZA1v0g2G6XZN_7nNzexNA2RiwI0Y9vpZxUDTZbJi-_4_WqmA0QjmJgAsvoIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImfW_iBacR9FwlKox2SKYhSfS7DoWW8x54W1tZRal6Ji4wvvJ6Um0tu6NqyaDwoqzciBivjNPkipwXyZY4hXp3-ZSGS7lB6wS_4R33GSEYO_C5GKJQYUUioO6zpQGsrH2Ns_9zAmehvOLMiMBcF0UbYe3zPJzG5Q5_rhq8HcckeYcR2z4pChb1wRLls3uHalnxcr4xXBWRM1PbQ1A96-r6gv8zDiTHlgwSy75eBaGOStD1LvWD0I8uGp1IDF1O8fzJsV4p0pLN3ASNfpRvts_JSQWpJuec5xX5H1UQUaQa1zBe-yzazABUCJSXVrfG8WIJ6bcl0S-gNDguUL7kxMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvvagKVYsZHzWqZHFniZwEd29HvUnVV6BP9b2F85X0GGOsbcjzXvwbp2HXsXRmJqiskXj5SJD0pXXKYS9xJeMD5BAhFqyrBlPPAchWWi8kB3gnBHeu4FKwgNi7qyiQX_yxOWkmXr0Yuh4CmonSPuiFeDfAnySrjYEfIifeteCiUQiO3Wjc9PeCjw0NxD6JjfMlWtjpNJoAgdjNJvU8RCTeiGVVo9Da3W8IiZ5ygjFKmchtW4ayBBkjrmygLfjGpPA7WBTPAVdUzU4GpJaN7KYCMetJFBOx_mIgkY2IfNWTk_iW2EqyyhA2_XAgG3pjucMtOTOykBCA9_W-yzghEibQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=FasWBd5o7814_zWbUaISwYWupQL2K75hcnwXgexofRdcQFCo6DhDzPVVGvm_vPqYtVOZaaj6b2jQ5kL0nTRfPQUHXR0R0Ec5AvyNMdul3h9WozXbVSzYw2fsHWGt7A_X5q_K7EwBXWeXeP6JxEEB6Xy0vn_i_aBKGTm21aEPa_6M4pgUhOnHhTcc548EIx9pAIuUj8vdZBdZlGtHGUnyHQ5iK-5SOdc1xO68uL5uYsAhmfSAGI2YuZR7h7B9dlSHGMDKuA5e79YanJNxLEwYJgIkGV6QMPRV-EmEMTZ-O2Iw5BOXqFI__wtpHYmMnoHqmjNchAswj3XpdZ1TEhLxTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=FasWBd5o7814_zWbUaISwYWupQL2K75hcnwXgexofRdcQFCo6DhDzPVVGvm_vPqYtVOZaaj6b2jQ5kL0nTRfPQUHXR0R0Ec5AvyNMdul3h9WozXbVSzYw2fsHWGt7A_X5q_K7EwBXWeXeP6JxEEB6Xy0vn_i_aBKGTm21aEPa_6M4pgUhOnHhTcc548EIx9pAIuUj8vdZBdZlGtHGUnyHQ5iK-5SOdc1xO68uL5uYsAhmfSAGI2YuZR7h7B9dlSHGMDKuA5e79YanJNxLEwYJgIkGV6QMPRV-EmEMTZ-O2Iw5BOXqFI__wtpHYmMnoHqmjNchAswj3XpdZ1TEhLxTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJZWos0DYhHXcI-TYlErI4PjWzNUq7tTjC219dPrKSRiRKarlhC8tS9vDhaE1TuWTBz_Pu_m-tGz4elw4YMWJSUK3WQTHTqOMq5qPQH5MtsTp4iPxjOV46siCaDsaeFhcaFUox7bZC0OPOR6EZDRXSG_W5EHCHGozz9wnGBsiR3blPe454IXYrlM7FEKikDroOr0Y0TrPWCB773rcrbEpByWJ1K0A-UvjHddhvY4-Rq7ppsmEFlEWo8KunOKRUBjZe0mScJC78xvmvZl1u2LG8_jfejgU0WCEuAs7-CsP5IL0mKtLHy8so-AjDvKV0zdelSiYm4779ki_TXoqMOEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=XwCcA3ellTH1qWmv2uBBlfWZkCSRGI3eK60msom2IG_3yPqy2WvdiRbdX7KFb6aRjfOyED34MoxMYjDO7nsXaKaSb76o_f8ny9U3QVGek0YHfTIXTaU3re0-JJaqiZaoMhUYSIdnQHAYWO1HO6RpHU_YfymHIhvGp3kPELqiKi0lT3xWDR3sb5C2Fy0X1Uo7r4QwZMGo90ObUde06Sm8GnvypKB1DutUAl3wM5tm_7X537CzsVLQKdvqQFA9TVtagxXwylcu_lh2oumPhDnLFZmDO1ODiovsmznFoGJ9qc6dxXyK6uDxA1y2QzGfiRGBWhvy6rXLB8VZlRE6joAqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=XwCcA3ellTH1qWmv2uBBlfWZkCSRGI3eK60msom2IG_3yPqy2WvdiRbdX7KFb6aRjfOyED34MoxMYjDO7nsXaKaSb76o_f8ny9U3QVGek0YHfTIXTaU3re0-JJaqiZaoMhUYSIdnQHAYWO1HO6RpHU_YfymHIhvGp3kPELqiKi0lT3xWDR3sb5C2Fy0X1Uo7r4QwZMGo90ObUde06Sm8GnvypKB1DutUAl3wM5tm_7X537CzsVLQKdvqQFA9TVtagxXwylcu_lh2oumPhDnLFZmDO1ODiovsmznFoGJ9qc6dxXyK6uDxA1y2QzGfiRGBWhvy6rXLB8VZlRE6joAqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=ByCw0hFkgd6swcM4FMi1a-cVa_9BMqfU3yxLRPLWHZVfrPzmBYRJ-rzNORMaJwvkX46JTA2wjYzbC5p-iHV6m3-IRda2ni7ZnIRuMPxI62BIsu0RxnPZdqVS_PkFG-Jj5xmn4dRK28OhJZwYUoSDNFyFqkO0a1X4P_fb90KDPf41DRNppR7HjujIEQuC5eOODUD_IRvKjNRNurSWoBTPhE1261GtRXoGSUz1Orl5Uz4PeDC0ceU9urzrBxCF1JMCsLpZlYeFxEkGoTdlxQXjJXY2LRgdiwVPzRcxYpdZ63CXwnLIzAIAj6splDJHgGMDw7KM-WhdbSvenapO0deqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=ByCw0hFkgd6swcM4FMi1a-cVa_9BMqfU3yxLRPLWHZVfrPzmBYRJ-rzNORMaJwvkX46JTA2wjYzbC5p-iHV6m3-IRda2ni7ZnIRuMPxI62BIsu0RxnPZdqVS_PkFG-Jj5xmn4dRK28OhJZwYUoSDNFyFqkO0a1X4P_fb90KDPf41DRNppR7HjujIEQuC5eOODUD_IRvKjNRNurSWoBTPhE1261GtRXoGSUz1Orl5Uz4PeDC0ceU9urzrBxCF1JMCsLpZlYeFxEkGoTdlxQXjJXY2LRgdiwVPzRcxYpdZ63CXwnLIzAIAj6splDJHgGMDw7KM-WhdbSvenapO0deqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Br3uWqPezsmUAdoKMJPvl_PFFf4uK7RZLRvMSOPn4F0xgKMqc9_3p3_r8C3EIABCvGikOjAxqF-4uyOcAQH4Pnlovr-OaHuyfroYJnKOQo08Z55FynGcWfS1d6Vjd4JRbG390N9RFDc9atZK6K8p8-SagRh85bkAGO2z3qwGD5sryHa4XJctf3FV4bIdXGa-1MaRZRtphNu-TI96AC_PBHxoJwIP6hmB5z6fgWMnwRZgqzt3G3hZRa8DHOZNph5BO5UmqRRal6a9DIHNXRC-FdzndE01qmEkwg4UvEMw3wdERbA_T9MmZgD5ZiPqB2mzoTEFbqynGJQA8i0NqD4mdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=WdWC5DOuw2sXNtOmZ7yBDx1_WpcA8CjVfR3lO9FLyx01LH9z0761hlF8KDCIvgaKaEufIc5fHi-1wJsEFUZrcua9QoaHfIE0gNHipDpQ3iyOBlN6G2H_astupA20k516EJGq_dZqO2GZ14jIUgp-E8oUbz34l5qPKB3coO0plEyKZEiGshZAF2uvNrXufe0U3sUJ5UYr_53l949-TpoUjQICZFGL2kGAClhvusltjQM94jA6_9tnIwo-3mPU7GKfkGWNHMnsv7DkYIHdx-p9HqXw-UqHTauSSdDWLjI3HZE4nqnS697Un2pf7wBc02pMRHi9tXe-xzeMcRjGWFRF_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=WdWC5DOuw2sXNtOmZ7yBDx1_WpcA8CjVfR3lO9FLyx01LH9z0761hlF8KDCIvgaKaEufIc5fHi-1wJsEFUZrcua9QoaHfIE0gNHipDpQ3iyOBlN6G2H_astupA20k516EJGq_dZqO2GZ14jIUgp-E8oUbz34l5qPKB3coO0plEyKZEiGshZAF2uvNrXufe0U3sUJ5UYr_53l949-TpoUjQICZFGL2kGAClhvusltjQM94jA6_9tnIwo-3mPU7GKfkGWNHMnsv7DkYIHdx-p9HqXw-UqHTauSSdDWLjI3HZE4nqnS697Un2pf7wBc02pMRHi9tXe-xzeMcRjGWFRF_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIAdT6tEAds00UUYvQ9QZ0PLQL5AywuW8CZMAnXGqZhbUjQ_1fIYTShKQehSlfEcOAFt7a2nAKkCf9aqcreQMZ-f8YgCmOL9iDOptIXhGu93XAOKyfn90mMJXewa0qfdrGlswnw9KqPFJBQxConNWAZdca4bxcr4cIwbV4aUO8iI3GmqmAjab2Alfrw6xc_knpCqW22q-ef68qtJByFCYy0825QrLvraYrcowP-kZZYxteURm-f9rAfSZB0FmZ3PMlxnIGkgGn0vKvm47Y0X9k8KB9Z7zW2mYLHkOQyZG3bBhnjY2vvANdbOlxzLQFWvqTgbnT8treXjxuZRKbAe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeIeqwGfZkfEmum-SJ4jmWKLVPfbMo9ZS3SjI8bBzTjLQS4xQlThk9RxkB8NlZDiTPTIU3Yd--cvVPN5GyvhG39ypamQMAIJTrDu4P-abf5F4zF7qY8PYgHYJYUBMs0Ug5Ad32Vzzod6yEtz4pIUAojm1gU-pu2amNoSqfrNGCpeIAo7lAqaROIpXBLAbpAKShJBr8L4gQjIUFV9Oedj1ijuE_114XLzn7s215kX6nFkf3DT9U7q0I3XvS2CH9d_y_AGpbok4mW35cT4kZgNdOYxTWg3nhGIfO93buu8iyi80QzSJq9oU5E0K_a7-6LjBE2U20mYmixr3p-ZFVcc9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6T7VmYEJDi8x3NXMnLlsAVlfQkgAQS2SqeDjzETdJ2AIboIeXBFHjYoKIwG88s23NC34uwxW3fpr4UPukDjr2i2JOYkNzLqbfnowFHOFRJF9XZXbrQNNU-nKluo_hNkm-lSxH7S5STZgB2eZ6SNB1Q_UfFIWR_iET3v77lJ8FzupdISWwMGWs-n30jahdpKWr0RoSQRw_KjB2E4dGpj2WUtzbL-3R584PrvJetuyUfErnWE8e_UOCihfjSN1brexbCDcOQSaV02ciBFNfmQUPmb5OB_JAxtI7giVeTct5UTe0OMhRlIVr3F_oEJaCqXUmAOf19S1O6KoBdHDYjwag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-3yfIEyozwIWwcatWk6TBBOVUMCkH0FbQXeJ4fbIkJwG4dat5IGjaw9neu9lfqCpN7txs8RdBKfS1PaaN9_fs_9kxXNr4pegWP387Up9tjCK7nn9fE4KSRJGnoCn0wqhwYkULy48OiPLaS9oIACCHP4v_SBG1vJ-IxnPzDt-blfsqgyJsueHD6Q4X8WgnPTQ-VAVOtQdN8FX-fVc4bvQyE2-45Tv4nyZsfFrYBSTcM_MA7qWX_9L0DBJOv9n2JkQYR98wrkZZs9sUpNo9NNBBF5ux9wYjyvq0P1NRj3QTLI5QvXfiQVD81i2m8YpX6F09kE4X9FPyjMF5Wm3AxvTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=I00oQVqqQ3ULjyQs2ZSmCmN0COQvOWd3hzJC3lN3qpW_UAbYG0O7J9XrSTdLp4yGSpau5ZPrggs4YkoAuKVQC0Nh13Y881tMttfhOa8uUikPFy0yKGkeVhDS8vxDK-6DZznomhpDK88qbYK8DCk4AIGUngDW28RHzdmSpGSEcULATkmW1mnk_E4lUB7sVH9WDaY3xdHAiodt3kPwaPSplCUkqHbnF-EoGZvjFE8_cp0SWnPwIKhpW1O8Puwn73xm5BMTAKubFzJ6I5pjlVpftXC4p2GlRMeM84QWB_WXpfL75vK_tMXZtVkRTPFdVNBFJcIpVVX5FkcSOOrVUXc0dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=I00oQVqqQ3ULjyQs2ZSmCmN0COQvOWd3hzJC3lN3qpW_UAbYG0O7J9XrSTdLp4yGSpau5ZPrggs4YkoAuKVQC0Nh13Y881tMttfhOa8uUikPFy0yKGkeVhDS8vxDK-6DZznomhpDK88qbYK8DCk4AIGUngDW28RHzdmSpGSEcULATkmW1mnk_E4lUB7sVH9WDaY3xdHAiodt3kPwaPSplCUkqHbnF-EoGZvjFE8_cp0SWnPwIKhpW1O8Puwn73xm5BMTAKubFzJ6I5pjlVpftXC4p2GlRMeM84QWB_WXpfL75vK_tMXZtVkRTPFdVNBFJcIpVVX5FkcSOOrVUXc0dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=gdKJHeSz9xVeHPz3hoQofuzxu1QYw0yE8QgcOihTk35smKqzbO15ihClquO7utkP9DawFTUoM4HnG5dls875xE42TiabsEb6R9JqjRhuXhZ4vwuYbW1mDQCsxdyuO9Ozr7kLYgebMmNLLs3XJ3jl83D0m-1Ehbv5z5sXD_RiXWTAstNo-zSGyIY98gWho9H6X-pTioi_rMezsB1GrtFesOTOHm4IIDeNeEiKem1NL9PPKTnQMI83rb3NEsQpj94ke_NGap1SCWxezAGoPmFVwx1P41JyCGK7AkxAkV1Y030j0zBNz44LIi3Y3hrZ4-BRqyaWw79POCcXuyrGgj0CMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=gdKJHeSz9xVeHPz3hoQofuzxu1QYw0yE8QgcOihTk35smKqzbO15ihClquO7utkP9DawFTUoM4HnG5dls875xE42TiabsEb6R9JqjRhuXhZ4vwuYbW1mDQCsxdyuO9Ozr7kLYgebMmNLLs3XJ3jl83D0m-1Ehbv5z5sXD_RiXWTAstNo-zSGyIY98gWho9H6X-pTioi_rMezsB1GrtFesOTOHm4IIDeNeEiKem1NL9PPKTnQMI83rb3NEsQpj94ke_NGap1SCWxezAGoPmFVwx1P41JyCGK7AkxAkV1Y030j0zBNz44LIi3Y3hrZ4-BRqyaWw79POCcXuyrGgj0CMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=crgI75JwWV4VTUP1zc4jMGGD3lZ78SC8KAbYoMLvZjq6n0H9hG3Z09SPHMb6EgNL046EBMtQT5MKJajSL6oFE0kLMlV0Re3KawWZV06g5RlbNoVxFCFdjDVJeCTIXJkTGoq5HLKR7ndsEy4lTDIzXlaAIgdS3Mf89WZA2DzZ0yvbEWLAPMf4DWt3ffQGKZdUYNLWp7TbGyLhriHFpG6Dwx4idfCFGimrg81GwBkEUbzD5-zhMpALLAvT6HDDX82n2F4BjhlgqoySUpH8Unju2pS-Nw2vuBrHlHB0gYq3W7-jD3p_q0j2v-Xlq8KCWKwhRsp3iMzjQ2voJs6owJavtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=crgI75JwWV4VTUP1zc4jMGGD3lZ78SC8KAbYoMLvZjq6n0H9hG3Z09SPHMb6EgNL046EBMtQT5MKJajSL6oFE0kLMlV0Re3KawWZV06g5RlbNoVxFCFdjDVJeCTIXJkTGoq5HLKR7ndsEy4lTDIzXlaAIgdS3Mf89WZA2DzZ0yvbEWLAPMf4DWt3ffQGKZdUYNLWp7TbGyLhriHFpG6Dwx4idfCFGimrg81GwBkEUbzD5-zhMpALLAvT6HDDX82n2F4BjhlgqoySUpH8Unju2pS-Nw2vuBrHlHB0gYq3W7-jD3p_q0j2v-Xlq8KCWKwhRsp3iMzjQ2voJs6owJavtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=uPv-ErwsozxK_p2xBHewdElTsqUFy4snojAF08iMBc2lIyPvPNDcRiUlFZPk8n5dfkw3l8JlRqsldeaGPh3kQiSUdouee_NnbrjEn0KubUG706uzHZoR9xd3bzqBVcggGIMooh4k7e0VBZB3JxhmJf0w70GFil9U6yEpICqFYRwsTMXNgx3q9jbW3YFp85Xg9tbX7_FJyFCCrlcJcjX3ivJSbz3hUWlZnNsbzPM11V59bKcy_k3r0xC2VVPuOAgiPKS9SlnNhoCXeF3HmpB8gWtRxXTuaYoT1kT1T1BGl70IZ7SNjG406_XI-U7ashr5RT89h1x_rWpZiSX6jAJ7KlGjelgOKJWCGMMwWLPxOi4IS1R-QVqm5IhrloQwHUCWQ_RZvTlQlDkm0_ZDZv88NFRiiSHezHbSGh2RuqtreDmlPkeEPfAqsjxPfbID5wPP7EUjr8hhq7-DArxSsGBtneeYmz7rDDojZjYR3a1LMGmel9_yJygrxpjqGP3wyxA-hli8M92XAojhjMc_Sk7IIMUpBRPb5NinDceJk_B-unpJL4KH09xl6MjMTjEW5Sx-V3bvEVpAZt9eQxrIax6FyNhGCDTShPHQprxeMa1r6Gu5s11DvLWt2DGvgysORAnxuyGPBdvV367ZHv5Eh7piEVV8EqFHKDjk5raLDiTvU24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=uPv-ErwsozxK_p2xBHewdElTsqUFy4snojAF08iMBc2lIyPvPNDcRiUlFZPk8n5dfkw3l8JlRqsldeaGPh3kQiSUdouee_NnbrjEn0KubUG706uzHZoR9xd3bzqBVcggGIMooh4k7e0VBZB3JxhmJf0w70GFil9U6yEpICqFYRwsTMXNgx3q9jbW3YFp85Xg9tbX7_FJyFCCrlcJcjX3ivJSbz3hUWlZnNsbzPM11V59bKcy_k3r0xC2VVPuOAgiPKS9SlnNhoCXeF3HmpB8gWtRxXTuaYoT1kT1T1BGl70IZ7SNjG406_XI-U7ashr5RT89h1x_rWpZiSX6jAJ7KlGjelgOKJWCGMMwWLPxOi4IS1R-QVqm5IhrloQwHUCWQ_RZvTlQlDkm0_ZDZv88NFRiiSHezHbSGh2RuqtreDmlPkeEPfAqsjxPfbID5wPP7EUjr8hhq7-DArxSsGBtneeYmz7rDDojZjYR3a1LMGmel9_yJygrxpjqGP3wyxA-hli8M92XAojhjMc_Sk7IIMUpBRPb5NinDceJk_B-unpJL4KH09xl6MjMTjEW5Sx-V3bvEVpAZt9eQxrIax6FyNhGCDTShPHQprxeMa1r6Gu5s11DvLWt2DGvgysORAnxuyGPBdvV367ZHv5Eh7piEVV8EqFHKDjk5raLDiTvU24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=DuMJNIvX3DOXV12IDOS1mQ9UCDF7CspAhx-EZCbjgi4tzoVLZ-tvj-c2eE6dq0XI5EDoqejCmTmYaVDNiXyhOGSLZeNCiz6jbVSmAG8C_a2VpmdNLj-TpQEuAagJF5QPR2PBFG4jOvKrvIXT9TvRkkgg47Uds7xeRo5A-ek_pfv6MiXU3jxsk6kZOzh2Xt4x7isrKgRDV1A3H_RE8POn62TM_28qucpUmxRu5y__n4-VFD__HNqXTjZ_NVfcaBiDGuISwGdT54FdJmLOcWII-zfcUVqX-zjfdhK3in2vD4kA6WxncrEaJMVo8wofixaX_te4gThE8BuKpJvOJ_l2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=DuMJNIvX3DOXV12IDOS1mQ9UCDF7CspAhx-EZCbjgi4tzoVLZ-tvj-c2eE6dq0XI5EDoqejCmTmYaVDNiXyhOGSLZeNCiz6jbVSmAG8C_a2VpmdNLj-TpQEuAagJF5QPR2PBFG4jOvKrvIXT9TvRkkgg47Uds7xeRo5A-ek_pfv6MiXU3jxsk6kZOzh2Xt4x7isrKgRDV1A3H_RE8POn62TM_28qucpUmxRu5y__n4-VFD__HNqXTjZ_NVfcaBiDGuISwGdT54FdJmLOcWII-zfcUVqX-zjfdhK3in2vD4kA6WxncrEaJMVo8wofixaX_te4gThE8BuKpJvOJ_l2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=pbBYOsg4fRQqyIAI1lQHVNL3g9q7HAf_XZHKAGQN41LZgUcWwTc8gh7ceYjdPE5o2oWuPjpMhSeXBGt7OEWQmuELyEU51VmumSdCkUvjpCVA70sLG-Eui-l38dMqPui1OAt_vUxJUA7BzBMNjX43RbOI_-eX7wdHvR8iUm5lPXq498b4D-N6aJNAy_R7VM-w2Ljzh608ty7GAdSc04ec_wn4FQuxyRF33ncg9gVQ3TCGvk2rR5xXYD4-z9ECAagx00dD2sAsSxgTxUTL0Qo21zBs0YSbaOVHfIw1oMmWYgEOrCfKRHduILIUsuEW7F9wVfplTdmPt33NnpEpUQGrgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=pbBYOsg4fRQqyIAI1lQHVNL3g9q7HAf_XZHKAGQN41LZgUcWwTc8gh7ceYjdPE5o2oWuPjpMhSeXBGt7OEWQmuELyEU51VmumSdCkUvjpCVA70sLG-Eui-l38dMqPui1OAt_vUxJUA7BzBMNjX43RbOI_-eX7wdHvR8iUm5lPXq498b4D-N6aJNAy_R7VM-w2Ljzh608ty7GAdSc04ec_wn4FQuxyRF33ncg9gVQ3TCGvk2rR5xXYD4-z9ECAagx00dD2sAsSxgTxUTL0Qo21zBs0YSbaOVHfIw1oMmWYgEOrCfKRHduILIUsuEW7F9wVfplTdmPt33NnpEpUQGrgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
