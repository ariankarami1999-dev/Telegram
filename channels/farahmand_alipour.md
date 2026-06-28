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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 21:36:53</div>
<hr>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP4vT26DbMfIlfgLMivVG7lutp701B9ejeapkLI0VrzVKU8LB7Rpp-MYYvHCktEgy4TwPnuSREmON4Wgqnpg6e94h0JY4LkYOnXPMN38jKz_2CxCvBFyMVUv5IqKYHIOzI_iupWrldaIQCXB6B3dJ_1nmo1ISta0JCFR6TuCeRLpsT2FxwY-Cs__7LdOwJPjdg5OhJo-vLfkb4KDFDmmR0c8r7vByxc-jJQ0sbH-anD6KNOyB0dAep2LXVaWTZQKuX5ov48GOGDHNaA5KTuY-9ndEiIVOpMPW7skJsiSszP25K61fdyg0ON5xH1NR0p3yNkRHfuewrO_X29ytGiHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2eUKqlhmJbtg1wz1NSlqC9fcAUgjXQiP8ek9XYRAWnaIigrV172WEec2Djx3UuWwtQWo2saLUbqgfHg7y_Mss5Dv-KvOqFAu5QJ5pI_gDJyMTYoeN_UoVyKMdYeU4gwT8OdGDtgvuJTVZmGIn5KzMg1zZg54RMCn_KkNKQ8jhcde7zg49GHPYVZm_Y8jEMLnVRnXkzJy6w1z2_KQh_IdOIZ0hlcYg5KmfePYdWyfjkaLIOIA7qlP7t6zKMRhz46IrWpxZ2rZv7ZMpb_d1f8XljoYRhPmOKIwQ7ZbAy6-cu2r32yWc3zE9fsn6ldCgsEM9A_5-FRewn9qTIlfjKedg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKqNUiRE6mHv0uxf3oRgwwez_aba9xCjaJ2oXBkcQQWaQQvmwxlbUApkuzMRDwXaiSE1vuJUtEVE6PGb2PKQQ298icy_8V0NaEPd-UvgWC5304LVQwpK7aDT7SVNmvjH84aBTvY5z7oICaooArYb5ScqhuyFTk2UCvEW3fBR7YQ_8utUGV0E2EWu2s-TsXmxgPVK0QKx5CNHJL-9IG75XDVeHk7FNJbpEgnk0golgDxrIGVqLTOe5j0gy-gJhQ2vvGPW1ht8BlE9THeP6ysS7fDOxsuuDreQEaAG9Nyv03Jiok0S_FcHZNgLgOrnNEmfNuPzmKLKTpor3QbqlhZ0uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZUJgI5iDe8Inlp27vKd3U4Vhf4waJ3rHch9_t3J26bHIpa_UmqlP0GfX4BoklfGTUKCwHJlJptlcVfGQZdPf88o4voMNyyKmc7x81ynmdZT4yvN3F3tpcaEEAFZPorKYJCpimYDS42TYRv9gJMuf6OrSD5GtH1TWuzxFCsfxZKShDW29jLMiIfdb0WH1uiWt_ixOQoiUXdOsYqnhmCkAbF7u-l2jFyXwqxHftBxK4gCFUheG4dd21IpJ1avgGfH_mTbCL4QtpYEXi_iiY-dOBtofISOMn_2jdgA-AuCwxf2heXMcJdbNp1ZO_UzMS0qRp-mbKZVFUasNkShSgKtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXPVz0Np_Ya33TSnQneYdMg6X73aSANWGIQHXx8fudYtExSViu3b07qcG9LwhkkE279H7vX5skLFRBQgkcCbN21pAeRAUdB_0NEEnwoAGYACgynAKQUkkHo8tqBPTp6qPHl101ytxfC2rwb6wsxxcynCF8MetDr-LN8dNWUaQWQIfKXZpxtAmZgNKzp9E9kJ9jCKRL4ea_tjQuljPSUKh0Ix9lylD--2qmPWTenmtyX6uqXFnDFOoGxvfo6_LnNfT18XxPlhhGLEO8Zv8nu6LDaEH-XcHAf4G8cCxk4TuQ6H8EAJH_w-y29kXpMykRsOI--RfwTG4AqQh2GxIBM35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnifoBGU5wy5nDpEdOSenCSGZvVQwvbGzeuU4nBX8Cm9fJQzVyuxxT61pkVoZ2BFSjbWKyv-PJ2AGFptGztODuDWIND9zw3K7ZwMiWinsliVCjXDDkrHkMxvmX7oevwRWAzvMQIesTKxYbjh0Yk3KF4AYUhSAY4PbJ9awqc5mVwuB50T2gVCpkpPKmVPC8wy5HZvsfh_Ks3m9spGKgLip1brSeys5Dg-ZcsbxgQhVjGnP8XyQYoRil1ZzKKzO_-DqEdMZ23EyO0MaEKUTY4JD4hs_Wgizd2C4-pG2ZclAoNkRKqr6oW_WedfMoGVLc0-zL2N_uLwYcJZAoP5VK8AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=nj3rd5cgLSDk9YmZbIOdSVbkQe3lbDCk0ZwtYxYuAGYXjkS35Wm-Jva3uRTGA0hNAeExnZ55pFU0VZHfGukqx6-Ni86pi9j9L4TF3CUf40L8qOr_MgS6vil1KTVBoo8XRoOBJKiCUxWI3YVEqOLgCNP2ucrkVZpki2VzCsAM7iAJCZqaAJTVqoiMKyeMwYAqh5CEvFBOHIYAf4MPehQ6SXVjrbbMVJ46R0JKjSjCNuS7n5ha5_TnMh6QAtzUevxU57Yfq9Wol0akkTLlFzUaH3W7SZOfTvsBIbOMlHiiFS0_HUlaPLMq8waK_CojpqAyfndjQ6j6RJidRPvYy4RqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=nj3rd5cgLSDk9YmZbIOdSVbkQe3lbDCk0ZwtYxYuAGYXjkS35Wm-Jva3uRTGA0hNAeExnZ55pFU0VZHfGukqx6-Ni86pi9j9L4TF3CUf40L8qOr_MgS6vil1KTVBoo8XRoOBJKiCUxWI3YVEqOLgCNP2ucrkVZpki2VzCsAM7iAJCZqaAJTVqoiMKyeMwYAqh5CEvFBOHIYAf4MPehQ6SXVjrbbMVJ46R0JKjSjCNuS7n5ha5_TnMh6QAtzUevxU57Yfq9Wol0akkTLlFzUaH3W7SZOfTvsBIbOMlHiiFS0_HUlaPLMq8waK_CojpqAyfndjQ6j6RJidRPvYy4RqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=lxDONs3E7_sqVyW1xhH2F1K4MpeZxVnQL7_hDuYMQQikZYQPPh6StDOkel22reJNUIGGJ542yasZ5CFCHsjhGLvd4mHremXKZr_sRDierkYb4hDZv8aRXr0tWZUCLte0LY6CBZoyN7SraYT8vR1l_ZQd3ac65vt-4SNnC8-RD5oYMqMoi3nAjY_k5CmSKKuCePFuMQ8xZFlBGBnQ2IqY148RIA0sQ8MPGBdyX6mcqtrSuCMoQoQSqH7CVpfdrQyHsi9GvCYJkTx8nFSJjkk67gHpqouOsN5WdxYrdsRWFRvFXZ3dhyGJsn-FEJG_Zi36W1x-3Wea8VS_XfV1XpgaAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=lxDONs3E7_sqVyW1xhH2F1K4MpeZxVnQL7_hDuYMQQikZYQPPh6StDOkel22reJNUIGGJ542yasZ5CFCHsjhGLvd4mHremXKZr_sRDierkYb4hDZv8aRXr0tWZUCLte0LY6CBZoyN7SraYT8vR1l_ZQd3ac65vt-4SNnC8-RD5oYMqMoi3nAjY_k5CmSKKuCePFuMQ8xZFlBGBnQ2IqY148RIA0sQ8MPGBdyX6mcqtrSuCMoQoQSqH7CVpfdrQyHsi9GvCYJkTx8nFSJjkk67gHpqouOsN5WdxYrdsRWFRvFXZ3dhyGJsn-FEJG_Zi36W1x-3Wea8VS_XfV1XpgaAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFgWZSAUZfJPoR3TOkMaaIxiw72kua6cFEPdfPWPJMDamKuiiawRwlqA_IZds1y7964nVzxapX-FP1CccWTxpK3fmgLTxDRZ--ul_-3fECAkSq1sUw6oC3BloUOis3FJBK7ubX52NhWu50hAYm2nOzpqpxCWxbUC_3_P4cLHnSg6clCFUw2kHZW82cW1D70-GDZFPT4X1T5tEQQYZnC8iJS7dW9TtiOIiqf6CamRvt_QortxnXTp3xOfPeRfGnyk1kF_9Bq5WbUMC1v3nMoz2SZLDM3JyUP4wo7lEexWaBQWAUz8tgXI89EvyhPYHjxeME_K7-CmCZTs1ERNPbAkTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZ9wKgB4ZdZ97_70piCa55fZTKqAWlO4xt7Blmo3TWCOX6tmpGiyIhV1SRbYjAhfDWpNzw1-V8GPT4dxhNn7J8O1a6D28SaB2UTsKcp1AQWviiHmRgjiV5n_eNGVXU7wgU2pdY9pchSuf48GCzW2Y2imz1gZAq_qtnFS-iicoPSbFi8R65e_unXvG_PD6hTm3koK2uHOsemKvfxu8F7NnLnvHJ2fAa0nYanVVN28Yw7ebRRnI7pykBp_CQmNapOF9OJGTjv8ZCnErj23zwom-uun01nvv29cKbtIgT-KomCV37tEAXhDH9MHTR3mcYG8aVbWarGARK2kJHB5Qiz5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=gx9J8gUm8yxMXGx3CkBwDA5UOwmm7QhjL_iixnButvi1v97qbYLifCL5sV6SiUfmpFY0dQbDRrfbwpPJGJ94hcXMMCHDwxIY-EV6ckgy_Kh5zND4rWxU6nyt29GCnmKrjmb9OzyTB4JwZATJxuCUO0nxn-sVDHOliJT4qNmGZDFtNLFh_MCXPBm6jKPx-UhQ2_0X4HhXln3F-_gAeQpnUdd4C58M3O9Eg171M2J80rys6FRJYc0TPyz96tKzWlSqhcPSwZZv0odZq8iNijXBtU5PqJJsX0m2w2CCled8bmgiFuEuxZAMDgt2ymDCUKkz3y44wzvychBVNn8KQglaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=gx9J8gUm8yxMXGx3CkBwDA5UOwmm7QhjL_iixnButvi1v97qbYLifCL5sV6SiUfmpFY0dQbDRrfbwpPJGJ94hcXMMCHDwxIY-EV6ckgy_Kh5zND4rWxU6nyt29GCnmKrjmb9OzyTB4JwZATJxuCUO0nxn-sVDHOliJT4qNmGZDFtNLFh_MCXPBm6jKPx-UhQ2_0X4HhXln3F-_gAeQpnUdd4C58M3O9Eg171M2J80rys6FRJYc0TPyz96tKzWlSqhcPSwZZv0odZq8iNijXBtU5PqJJsX0m2w2CCled8bmgiFuEuxZAMDgt2ymDCUKkz3y44wzvychBVNn8KQglaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=gz6mzRqdkkEDB3Cd5X8K6EnFdjn-QawuZw2TuKZs_olXpXTTPdosd3pJ-vPT68GHVmOXjjveEcqQxGMZVH4O3otEIWzp6EhHn_U1vkJdNmtDMLCQzvcTVBdQzBGciXgDDZ5K2iVcZSohR6JUNTa--uDI2wS45G1B50XulVcWvsju2gbAPuSDd_s8bhWUPF6QlThAc-BP9h2QwwsCQJ1kv0OtXgp9g9RZ2uquOEB8AN6G3Yc6m8BWU5pPWtKZDeFuoAful_RvwqgYXFa7qH78ZUMU3_reU0SV4_fd7GsVUNTqygRISQ3HRXm1laXgvizE3TVmZLyygZEXdf6Hwkvenw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=gz6mzRqdkkEDB3Cd5X8K6EnFdjn-QawuZw2TuKZs_olXpXTTPdosd3pJ-vPT68GHVmOXjjveEcqQxGMZVH4O3otEIWzp6EhHn_U1vkJdNmtDMLCQzvcTVBdQzBGciXgDDZ5K2iVcZSohR6JUNTa--uDI2wS45G1B50XulVcWvsju2gbAPuSDd_s8bhWUPF6QlThAc-BP9h2QwwsCQJ1kv0OtXgp9g9RZ2uquOEB8AN6G3Yc6m8BWU5pPWtKZDeFuoAful_RvwqgYXFa7qH78ZUMU3_reU0SV4_fd7GsVUNTqygRISQ3HRXm1laXgvizE3TVmZLyygZEXdf6Hwkvenw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIa9ZTg2DbAHm5eJEsnGJpfWfhquCh7pKFG64FvqxvWVqIOHllt9RX2tOus2TFOVKWwTjjOWY3NOyJZ3X5T1316dEnfHNaUWuT4cTu-Ush3CavCWAO61U-YvvMxAuhjeq1UsW49P_XqEIl5mOW_jkog4Cu7iiHpLvwjSs9efxrN8kxKV5PR28ZkAckihG8jsmJz24ca76cIei3Yc82rJ1eUBNbF4tSDInTdITLOVdt8wXCcZKp0_ZzguryCgJLidKaEWwOQHfSie68iDlL3uFfjUrzVMx1tY6czuKTm9CtthvFMlLuFA_f_hPV3LEcNoWRj3-mZ_AOPq6S4MAqzlNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfgBbDhmcKmH_qiIv96bIGaQJH1SMHyRY8p0YBHEe7zKcbTQYoExGZ7OKYG4Rao5FEwMH4HCQQ_T1diTk4QfHigdNEObYwUtIIBf2BgoxwZKVyN8-nH57umCy5TV2bplzb1hZxt3mcmLbpKgMKBXI4H287jeE4Gdas6f1lbRsgtqaCl32nDAsay0RFJ11dQUiGhfyvw54ESMpEE-aIUF3t9wjync_CmDKiGFYx4x4_iRT_IhMw7ZLpxHuTWd47tXZF5SAU0yGZyH3G4VFLamcrKr1HQG9-c8U5VxDv32FCE46o1FOM2yalMpOB9hKOVgUiTRYqw8CDT-rzZvhLZMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnTaJ3eXBPUTQv_xcVSJDi2U2_jhbquEKo7d0GCRl-XCTbA-VadzF8hCPlPKQK0dsC3Ee_2-zEdr1WhhKBBdkJLcRdreMFDNqyvHuftcJOge2hHiYCkAhX7M5QztJxOevDVm1SfsO9dkUC5vMZoaCezrkFPd7czr43-SYwI89Jwyddt5uCGxgd6_gDE4cj9xqGqmAT8_0i6C22CAdIVZQXxABeOzO1FaJjChwl3LtvcfjbIXItNsJZ1FpT5Bfjjn4rMAT4u8KqwJ-QK0W2guAVAtyS47FM_Jslcf49TQsZqiH36KfBRQFvK8n5wbZAZN4RXWtpxXYDvNMFXJF_cq3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=movL0d9LWbg5VzGA40ZvqykNL_IIYuJjJxGlrYgi_XZOBwt5nXi-a4tUJINNep7-HqV2F5iwbzz5QkNZMtLphvTpoE0RfJp7YQ8pfAATQTgMR1qMx8VlLdegyY5GqkmXzxJbSWt8IZTk8RLjYxeXV3qMTzumtZk00M0FAxw8uhyRqc_ky7LiBDF23CfhXi2LPJ389GUfxB2UHshnhdyOpL0LZ9csOTl7LICEP3U9iDrL6il0wh5Yqu-Onp5W2jJiJaKs-s7d8n-Vt4lxXST5nyeop18qXSlUCaOC1owibEAKEtJtjKiyzUg4dNlzSkHPPCIt-TqiSGjcq2B9aA8Byg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=movL0d9LWbg5VzGA40ZvqykNL_IIYuJjJxGlrYgi_XZOBwt5nXi-a4tUJINNep7-HqV2F5iwbzz5QkNZMtLphvTpoE0RfJp7YQ8pfAATQTgMR1qMx8VlLdegyY5GqkmXzxJbSWt8IZTk8RLjYxeXV3qMTzumtZk00M0FAxw8uhyRqc_ky7LiBDF23CfhXi2LPJ389GUfxB2UHshnhdyOpL0LZ9csOTl7LICEP3U9iDrL6il0wh5Yqu-Onp5W2jJiJaKs-s7d8n-Vt4lxXST5nyeop18qXSlUCaOC1owibEAKEtJtjKiyzUg4dNlzSkHPPCIt-TqiSGjcq2B9aA8Byg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-NZCgtmw3B3nXXKH1BaYzeDxi4ERfLZ3RBE2ZtFSViOzO11Dm5hLpkdEgVQcWnesqsuUxLJFr6KE_G8Jn6XdZ-eu69D0X8HD3cj7AushPXCInil8LavpgsAge7h3DKdWA4KJsSXDCSje2CHAv6Pf-_1r4ZfFpU_ECAdZHuCNiiF8dDzJ2XGH4rvbbBl0B19U7sHd1Ey9Yki4AWck5FMkld1BC868hlWSMhGwN8WexIhaXz-EDCqwCG0aJykR7JZtaMJowNvEaws6LSIimtN8olyk-PaLh0sYdit_5Tz6xT8bXj4hAbXzsSyMTbdtPNt2un4-3vWxeUQfPUiCna-0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGXf1TfUXdovhpiSzQs_Tz24BbGdGMjQSckPk50D2jVkm1HqxZjvIA919CtMUDCelnwimiG5PpXc83VSXTNfM5sNFHpZyzDh1t65Nh4Be8GqNCInYclvGsTVpjOV0DcSc9xPEflv2eJvwI0BJGkiciKfa4du15GoprspGnicjsAzVPjDZd2PTYOdu5t78TfARP9Kp_JJcXcUWxH47qT6R9Pyf6ZyzzSZEFotaWqivZRbudDFKYVQUy9lFbYi0Q2eTWuHwC-EKpzUFH-pyBCobok2vcmVYM6rnmr_scTTgrUEsAWAm7Ti005-G7NyPY2dswyyMKZKIFz0-6KGInyysQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr55EHN2txhidW9T6lO2ZXx2AcPcxdRuMrUoR2TbT7Z3Y47eSiXA0jbtB8vNGMYU0mylHSI7BwOk8i6EauqRMCzoNtPr-7LbSzemelPXBmCSqsqidIsR9c0j_5k8AhUzF3rIX-KWcDAHN7b0vhRnt6F2jDQQ2pJL_xFHt6n3V2GwdI46lS3H6O1x-jfe7qWddKaLSmfUUlnnvQ08pwx95HfzVaMYFp01rTRohFNE_lZJ3GI372mxdArB6abfJuRcYzKAvkEJcs-YWFyuyQB1ciQpIjNTIZIrNna3-62yWozNGDeGiTURB6HLD2CYn0UKsMWv9r8epwipl7PrLKZgPA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=D-a1YPkjgyf9ZsV_aegaN7gDdzXQaDst1qS21znO6s3lzsXKC7g4sbi06twBFa7UZxFRC6XsL22883FK2WBoRHoa5tTvo_bYSPlM82CCVXrkIU1ZWz6IRbxm6257E3SYpRYREOpkHbCiTgcZtQM_3IvqIZy-FmnzaeeskRJA4CjMV35BxpOqxdvhgQy17KWG8IyfO3qS3_q12YsXx25HDVz5gv9FHkmcmjsrEQK9yAlCh5xYOT7Qte3Q8g9taP9V0pEzzNwX1i-7SpKYx3dBN7aSI2Qww0_JeF7tDmN6pG5_BLt1Bqq0AtcUHIBCxWL8a1eTLNrjpEeX5Xa36HMGWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=D-a1YPkjgyf9ZsV_aegaN7gDdzXQaDst1qS21znO6s3lzsXKC7g4sbi06twBFa7UZxFRC6XsL22883FK2WBoRHoa5tTvo_bYSPlM82CCVXrkIU1ZWz6IRbxm6257E3SYpRYREOpkHbCiTgcZtQM_3IvqIZy-FmnzaeeskRJA4CjMV35BxpOqxdvhgQy17KWG8IyfO3qS3_q12YsXx25HDVz5gv9FHkmcmjsrEQK9yAlCh5xYOT7Qte3Q8g9taP9V0pEzzNwX1i-7SpKYx3dBN7aSI2Qww0_JeF7tDmN6pG5_BLt1Bqq0AtcUHIBCxWL8a1eTLNrjpEeX5Xa36HMGWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYat8FJQCTOOm_4KUB18r4lyl_pDgh7PBe8D6M5SNo3tOvar6SgT4b-MuWMZUNnpzIW7Rehtuun5eTMVEC17SVEUJ4G5tRPudwFI3wtqcs42n48VL-E2_I1rn0IiFRxwn-My54OLB59j5IqfmIekFtFjUy5qV_8aNZf4VWwvL1bf8xU-sAJsc_kQ9NHzXPJ4PzaAyd0NQPeDM5093ccG8Kednr1cDpEh7YYFN3wqwJG6Ia_zXmSM53UqlhPMosioyqfq2BbMbqwPR5-zi8kcTDnQUqc3XxBA_speo2BZC-fmNNvksR4kGRg9YwUOSEi0uLWkNblOQfVGiHOee7a5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM27WpGbAjtKxOrCVE2XCCkIcxLvC-1zr05XKCwnMfGY401jlAoodCXTA87hXx63bDJcAO8pyWuuzjngEUcynp3rnCIC3E9j6PtDlWmAaW2EUriYKUA_eGS9WgDYo3CynpgnlihPTDZU_h-gTukLALFt7sqk9kvc-7wHa-_hgtSCPvj9sFeKe_9O5gyy7bGsQrN1Gk0cgov_V1gYPVMcbpvJkfkXWQUTZoeUUACNCVtS7PEWlx4uk-c9nC_Kj3N3MCyKRJflB7ERsBHuS2RFxI70J_zo_ISTqyNzxPB5LgVpdE82KXDRTa3Pc-qiwAqfEeTywaVT0xH5C_tOf9_ecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4VCetqDfuU3a93JqX4_Hujrb3adOMNfvoL8cfSy7SVzmtmt5Z7w-yh4ynQSBdl2f6C_mm6NOxwDu12Xx0N1UnvXhZ5epW_d3yN2byVIdKHmf1UaTe0GHcXaefJMbPQ7ion2LC09RBvaeoPNsJEw2z__2BewGi2YH4WFl9Wfye1WWI4EopE2f0MEuzTUlVWe1_Cvzn2b866ffT2ZEkSMq7ZR91ZDIrCs4L47VxWJg-DNOw1rqEiI0ynsPfxkFsRBwECtATids7knWHYZ09csUYYBYOi1h2Nfm7_BFTAeUNKSRoSjtGdZ76dN_iJes71YjexOlelq4_jPP1-NRu4JGw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=m3H6xegRH-1CD29Q4EhFvTi9inDYRu2wMNRxdSdWIeD7nbbtGv-lXDlwseFLrzSKyfwpN95E3jQbW27QdstI8nKGV5qEJspKWzARe86ZNrWWw8A6lpXAWfi5Waun8hPTPQYjGmZNoZmzP1d6XstmLOgjgFi2ws39a-IuTu7_uYwlkgFbErwW8L75CC6HwiuQDyjkwlgdv0aZ9ueNJ7uoI_Ss0jz9lJC3NQDf4yx_ogf6BDODyS4QMdns0qlsQ7A1lrX4R_sKLtr8TnIIMZO7dhdu3pUPSktZoqn4JKXQrCcaUdMvCEfRl0txIDWka85gycEJ-O3XHxrzjKD7OQzLSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=m3H6xegRH-1CD29Q4EhFvTi9inDYRu2wMNRxdSdWIeD7nbbtGv-lXDlwseFLrzSKyfwpN95E3jQbW27QdstI8nKGV5qEJspKWzARe86ZNrWWw8A6lpXAWfi5Waun8hPTPQYjGmZNoZmzP1d6XstmLOgjgFi2ws39a-IuTu7_uYwlkgFbErwW8L75CC6HwiuQDyjkwlgdv0aZ9ueNJ7uoI_Ss0jz9lJC3NQDf4yx_ogf6BDODyS4QMdns0qlsQ7A1lrX4R_sKLtr8TnIIMZO7dhdu3pUPSktZoqn4JKXQrCcaUdMvCEfRl0txIDWka85gycEJ-O3XHxrzjKD7OQzLSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=RLDvWFxL8MkglC0w2EIcYB6bI6aSZBnKHBlDJEeDzPs6wdOwN9p3tjZEhhbZO2_bEtuxffo4SQrlEGpOSRww9X8wZ-tX_x9WCEoBFsqXxPhKYKg6zDe4EmKeY8qErdGgur4OONm3Xya6YhS9oq-YnGntEhhnHB_HK-uTYSvjf4Ed8nK8uoK5drZsritRQBcW1V5PUcIxcRSgYaFvAzq0kDBzNKtXtUZ8Gf2cVntH-0pAu4tLnP9T3xPJswfYNl2d3XjA5bPQtNT966RuDkoIUIpvD26P586cggf1jx6nemyIzQLYd2tcPJt7MxMcdOCBfXixLhU8Fo8IQQIaD2XBXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=RLDvWFxL8MkglC0w2EIcYB6bI6aSZBnKHBlDJEeDzPs6wdOwN9p3tjZEhhbZO2_bEtuxffo4SQrlEGpOSRww9X8wZ-tX_x9WCEoBFsqXxPhKYKg6zDe4EmKeY8qErdGgur4OONm3Xya6YhS9oq-YnGntEhhnHB_HK-uTYSvjf4Ed8nK8uoK5drZsritRQBcW1V5PUcIxcRSgYaFvAzq0kDBzNKtXtUZ8Gf2cVntH-0pAu4tLnP9T3xPJswfYNl2d3XjA5bPQtNT966RuDkoIUIpvD26P586cggf1jx6nemyIzQLYd2tcPJt7MxMcdOCBfXixLhU8Fo8IQQIaD2XBXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcBdDEFDDDcJ31gqKeV19QwFrZsv7UgQLKxWchUAbKc6Cu8-0G-EUfJmwrGDUl6gjdHcq2J--4G9jN9XVgVbzDcVAqi6uQRSgSVqN1TtE-SJwFI0FdNVKvT3RK67oZB-Fox5XHI8h1EXf5yoldgdL1f7QzofPI6mvQJbsc2Pdhc2VVVfC5kNQr8Kd0pRHkWkZVhILqVB-ZY12ER8f5ztKC_YSRZJdxnDiFBL9wZMTI3PSNZj2g292TO1z2SqUEJeC8BqhFaS2wBk75i9zLbZ2_jM6WbZurdkpO5YOtt_Rxx_3wuIMMfpU2p6QoyItKlU4EAJyzxE6nEkpJuhEX2ckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2PzZZppF7wa9cSzUAsmaaUSALEY3HgCFflnJq2Ym0sh34kdwjVVXvY5BLScT409I17qGWLIn0Svo8nSHGqvIk9uXyUSTkCLqTZrDyJGdPo5W3HA7EIuYY7bc4kRUKcXOQaNz3XjiQVuorGtJqMli5tJ8SyI5hb_V6-35ePUa-QcjibliHwyoUjr6RqRAxueeu2rMU698ysGvEStvbFB0o8kpredIkBzrS6J6AWDVd8Q-Tse7m1CU9VWjwz-NjwRSr3L8beJ6z6tNtw4e2ibdTRu1hXIILbldG8DQfmqydQjnunjYEs2n6k2ssPuoBOq6np5g7QLOQmclx_Kwj_xdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUBOF0rk7XoKA900OZnn0PjkV9ufhggvgSdUucvErxp5fxSzrdMuY_mGAfYCRWb5FmEKd9CcBW88HlttFEvA6n6z-uOoQawtVDxu8qo85h_AoFFt7uuqcPhUJWzDy1uhmmFGobIHYsji9_mcwB-3_8sNKub2U9MKESi9aqZEj609zKKQal1ke6c0ktvnNHSnkg9hggH4j9US_lHvozsPSV3x5AkqRS4_M_zuxZRx8fefdBWm2DTxivPAAI_WaPiCRtiBSH5BGhUhyEefDOSvYx34SdLAgob6K-QZQ341HFIdUqRYRTvRsz7q8xVtkxaaLQ8-QnkcONiRgdoZ657K7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSLAwFxvZo7vzPfhbSUjYr1_jyr3bgbZ2otfMfLFnugruKXguEfR7eFAaRanhV8KU0fsiTFvdzdt-qqkhBjjQdw36wt-OTML2j51PJ2ltR93iVciLl8SZ-2mlg5AtnDIU0BbQXEeS4b43S7nnWTrB8RjApeB-KQtE9VBfNKlq5F7fxdCXTQGOox7CUEHCojNh5AHTdXTSc8HeJkoAUxi8VjontlpzgtUlvGWn0qm2p-5r0z_-VBvuYKrfJqLeaxJUKFEP7jYe61lSt8j10ftrMfXHb-HsccTIn7FjUZKeA_d6skIu3eeCyIK6ED4UPG1EUnZgSzjT4g4dEAMme40FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsS_bVcuJNeo0itPSIp43H36dEevinD2SdNWGTZ9INN8T7wzLApN_OoFqXENdRXonymhkQiR933TnSGx-7VDjQEaVSYTzxfsNUpzqab8H4vZ9ujRczjXW_wz6Ixy3DhXNPwqAuNo1YzP_dA5UIFjfuvyJWaKFYDR7GHZFRbxb_d0myxyg-SPEUNZcMfYvVIz2zAlJRrHuGFDfGutNjZxCX2e8EtdH4fCrX_TWYwKH8CQq2653wu-O60Lj4OCOwFosAio0SZvXXbTIPM61u5OnF4-PEm9RB5ZGff1LO-vN37tAHJ09yx1KOAyVFWgtG5ESVYnuE5NVpNAvHSN4gGi8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJMPXYH-zRmhY7wCTVl7NKpiCyS_Ua1PiHaq5rfCT5Il4cE1R-EdIdNIw3iEBTerKTQewGa1yvWHjUq-h27MSIuqqVvIFEoTvpZi5dPB6Zgj3_Vo9vJq1HLMWUMEMULHFFq2jKpYALDLp7oOlk5GyiY7jfgUIkdchrrwUDrFc1q-Lnulg-NX5cynbvUUFb5LSWWekDUQCDkzP-9FiO1oc0aWbX3ePBO8MjrYDVdv8vUzXUAhg06-lpEfgDaz0sTng7MxD9WR4MaSeUCFuoi9n5Kyoeogf97MUk_cpx9tSO8dyvLytiMCwOddrVOCherNaMzRqEKOU0jK_LycZgPm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx-Tqxvp93mkK5iEVgHUVSNCZSuebM1ftYM6F8i773-0FdnaW91R6J6_xo8QUC42nZ9yFcUF4ts7dvr3HFs7MASLdVYjyT-zv-7UG_iljCqwgWgwu4KjjFZlI9VdFb-xWCxJF8PvSqCGF_qy5Y0-ZhE2zHlm0AgpGHIUSVf8yHYssq0IdxRV5pYPulhHr0QIQx5oH8JhzBnmL_v1f43SY1SFtTEz57bUY6ysrM1cq2qodk2vsNBLZF8OhO8BOX_TFEPcMxSOQ5pMXUU6Zr7ZrBKQQpg0dgTHWhOomBkyVbMXq8gFgXr2xOilwXkxZvamrXSVbqVI2sEo-_AaEpvu8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsEZxfML076sYTjbDj9T-otGwGmn9xPtulEoVy_xWaekBCV7ZZUIiePg5dIfPCkQBg0FN-tgmPZkGGcENxMtj9sIyE5QE1ddlB36aSbCCG8bFVaqIaBtQgrWVeGHKc7SvIPBjIHQB_CAsebQpCEISu_k9_ZsnthCTyU2tkj_12ypmBZhHLqbD9CYblzLXZTvQq2MOMd4Qu-bpQ82JR3lLWuXTvNt3UNaRdBeYOzkD64ClUaf4a5ZjGCTndfxRQxesS7j3_uVGFevb_SeXpBEHkxo1_aaQRjqMUzXnvNBOaQzT1NDGzQoz4iXRml0kVaC3FinlyP-VoGTAB6fACA6rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emcuHceohRgsT07VTHMYjXewHqxR7c4ofazKEnyk63AvRHvmcYBq1tBepMWHju-TsWRxDPCOxcqcSDvu6z_Rm0EzUzXOzE6--izHTCvZYfNLmLCxw2dSaSql3DJiBd4J3kCeenu3oEnWfwtGrvb9C0gIJsBHoM8yFgz0tHPvY-uDXT05w3elmScA_aojUPi4xu1SBYucMzLtiDhrveI8mhm8c78teqhaUfXuwrqj0rW6Yxb1d1Yyr7c24Dsm3lWi5pqJN387zB7aHoLVol0YZ_gFE463fYCLFn76s_ZgDtOnlG1S-Kejy1f2i7BieW6-SeRvi1TmHi3At53Vy1Qnlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhOLJKboUqqlZOMxuI1ijoJGU9gOcPCTaTj8zvnMnApWOZulon7Mg-l5KkoaX0TtVfStZKReeHdluGPcE6IIc57FwnTxgOuTmAvsMndH6E5tlwxSH_RYwjM2jun4tC6p3XXb2wAUtJ1kMFPl_HxjUte8li_AfA9De6u4gUXlYdStp3v5ip8LscELZ1nD4At8L2bVWaXrBNs4lG1fPu8gyLhXL2g9BjDTp2QSXBa4BqQFMJRuvOX8J5WX0cGB21vYLa9MEKiyKCx14jKn89_k7sGQdxudj2N2JJqefOefN8bbxnRlrfRPbdNIxLYQbYBq0dCIs0O_VZCuY1yO7wtutQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-ykOYZVe4Zc7lX8Q-Zbl_qgUhNysVYURdC6-apmDlBkC2O3sl97O8x6vXDEvtbP48aqCUwHX6D5Iurm4Hjlbl-1IX5J8kzHN7GynCizDGcBu89vfYjqbAwrctvHk6S1XtUh104vQ_DixhZkX7tJlgYzc_kXO5is2tA2cFaqwFjbXEbqrUhsgcVR3A4Px1ox7RAVvvewPORT844yOYKonF4oUt1r91IWiHT1BH4leazR-DHt3YQ418AKyIK3zwuhmSW2cEaU5-0Q0JGLWesgLw6QfLMgC73WDdltEGkYPqNTi-kOSyxPuZWgODaLb9iR3Qq5JdaGLvo2s8SRaZ4LxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xqvd6kV6__hfFI_SkCd9TmGpzOCZcyGKjyfVbmHEOCtDBhj5Gdm9Xu6n7AePKy2hFZnIytokljOfoiGf0pGmfJgvVjX23K7C87qfhxJ3dqX3YywtiFHx0NQNSbQnPiTZSYpgqMsBAPRU-5HSt8vCyNnvuJ2MYtFo-nBgWNlb4nNNlnCboGTTgxweQecEZAKJwzhjNz4eyS7ubd1FxFtl85a9CoxjvMNRw9odEh8otuLK9M1iTtKEfaF8hroMYLYEtO6alJgVmQuzGgYn7f3GSiFWsusVH9VZ0NQnQHSwTcAV6kvrtedcWQrkHaw1BDrAk4d04HkcK5tFLvseRf-4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmfbw2FOaf2KZJy-_zBlJg0cjnkDG_Jr-_8yBMHWu04d0JyH6Hh69Fe2mTCcsGnMdeCkaXnqOku-ab8bTeNbMsZg7Sj9izBADyFDEVa5iN7n9zAGt6qBJyEw8h1TMey8-2qTOFOUSSsKugcpguwBZs9EdrXrehdraV6RaQLcxLWhggf-uz0dNqoMriYgmbUvyQIUKvcoaI_CQgsI2MkEJ-vzn4Z--QFUdlqtbvbqFBFUBTVk98A41DUTSFu0jy74DLch2B1uqGAn1cwb90Y8AJM55dxPFkifhx9jkA7hlk0FMzh1syjBKQ5eSE7v8_mH6WZI0CByQUuutsMcYfmoBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQIRrgigtVpIxbFhieQfRbGFcP7vImMw2nmOMBqycJDK0NME856CQUvh2aqlODJwoeps7S7AZ3D22jCtOnD4zMCHI54CjxQTMFBjQcNkGtUYze38cbsDGw_BxAnsOEXRrUHV9g4D1yhpTiaLD7t0aPLKopwDkYgPKMoAJ7Kyrca3MyF6CqrLCHw_0_uZCjbRpFSQuJo2JPejM9kx4BgfFhegJu1qMC8AXyQBKYIyhSN_ahN91XVoaeM06-0NDXQ1o3q3FqVyTZadIsf9Bfs9N64chtgMneJA2XDfwVMbvYSpG2HxR4hpV-SUgioWTrXctr40JbNf1tSuyaofssdpeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1nj5OuwuaDpd261DE0XBz7Z5CkaVfJF8cTn0P3VgTCQbdzyUNx0XXo0iip_VDY-5G_DPQ62p_xbPl2hPYqPtV18vLSAJ5HA8Iz__OLbEAmaTAyYgBhnK9QCM4e8MM9VAdEq9k_kPoMnTzrofdROpp6atu4z0ptUFL8hRReMgavxUftGm-pOHP3HSguBbsXZfBWbAoWmgXLXQX2OXPN34OnwR5y2-9PmvRYUpvzTZc2yJ6sujzJAcUYeEDrDZsC_Hn1595wIEzPs2C_DrP_c61PkuQRMTdPCVZAyq1IJzWo_XYykGZJvJ7EH1M8wpqrVOZQ2TAGFE3GnaIKZcX9_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=E8um-PjKBFVGzGYVPzuhdbisGISSkjJuqYOun6lbfu2O2B-fNiaGgPHlxhT5wTJo3j2mefeTrDe6IjrSJxdQfL3G8mX6spRsDONWVJvrka-FqnEAh8NiKQdga02qQNY7FzyjjddCOx9EFTBvV9D_0t3MXncKEAu6XJMI8p4a5H1cLcMyEI2V_7kP61t4bZ0SGgihB_s50gCO-kMUUqvRPNbxG045W0O65-UQcOrY0sRz0O4dY_BgWAn0UErvUNXpJiQuBFPwHcZPIskWhDbJb9Ncl-wtvysyghMHD5zXgAVVvlXvixTnyK0qgJZEsZB_2-xJRmLM6MVynmpug7M2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=E8um-PjKBFVGzGYVPzuhdbisGISSkjJuqYOun6lbfu2O2B-fNiaGgPHlxhT5wTJo3j2mefeTrDe6IjrSJxdQfL3G8mX6spRsDONWVJvrka-FqnEAh8NiKQdga02qQNY7FzyjjddCOx9EFTBvV9D_0t3MXncKEAu6XJMI8p4a5H1cLcMyEI2V_7kP61t4bZ0SGgihB_s50gCO-kMUUqvRPNbxG045W0O65-UQcOrY0sRz0O4dY_BgWAn0UErvUNXpJiQuBFPwHcZPIskWhDbJb9Ncl-wtvysyghMHD5zXgAVVvlXvixTnyK0qgJZEsZB_2-xJRmLM6MVynmpug7M2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1x7uPaerDFp28xv4m7wvMlfySmR5uF2q_fRV4PluK9HPnbCIVkgP_xxjESm0Yn73Jmd1JhxkRfNqkpVs1zOn74uVxj5UPwJ7zmfjo9yr4_ApBbUU8rNYDyabQOc0k0osBl6ZnCFVxCuH58t5l_vyhQ4-2ayyzNCMrHbIdbUK5ibU1e43P7itKPaRHiL2T8dUzCnRBIyRmCRw7SGZVKSmbaKRPmCemg72mNeUoTaP51BaOTwJRfqnbBn5SzSqXvxvyKS1yZpeVYv_HJbnOQOU0NAoV3Zlvd-BBGtz1wPcvLEC0JNl0iXnJ9mkYi2Mo9_qiXEtNIK9TG0SCXylhbhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=oY7z-OteTpk-H1RBuoj5nDZPlpsMcNipJ1YyfGYbPk-fm82VEB-8FqUzQmqAjVNA1ouBwVuSGT6xOaY6ZMQ5fMWQafBT1kL3dTyrcT8zCgvyjUkwaW9huQtU6CN7xMh8lTobt8HkXNrGFkxrmv7_B0inoPRvBeAlpM-arlRNT9PFeUhCs-FBUC35HkA0MVxDe0iG3IN8jRfbL7fh7kLC_3BX0womImWrxR4YQ9ZLAouPShNtobn-xA8ZdoKn_0ccmQ_OHVRYQpvYzudHDME9L87O7ZBtCpdGRrjAosIlgjKF0Iv0qSEvS2PgevBml_4vAx6hx0TjbXyqn5L26VWBJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=oY7z-OteTpk-H1RBuoj5nDZPlpsMcNipJ1YyfGYbPk-fm82VEB-8FqUzQmqAjVNA1ouBwVuSGT6xOaY6ZMQ5fMWQafBT1kL3dTyrcT8zCgvyjUkwaW9huQtU6CN7xMh8lTobt8HkXNrGFkxrmv7_B0inoPRvBeAlpM-arlRNT9PFeUhCs-FBUC35HkA0MVxDe0iG3IN8jRfbL7fh7kLC_3BX0womImWrxR4YQ9ZLAouPShNtobn-xA8ZdoKn_0ccmQ_OHVRYQpvYzudHDME9L87O7ZBtCpdGRrjAosIlgjKF0Iv0qSEvS2PgevBml_4vAx6hx0TjbXyqn5L26VWBJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Tt3JNfCY5NvBNxn7wJUV7tUdrqelwtcJa7uTtXb5953bS9gsAujluHyQT78S7gQ5Pt4GNKxdcNmnlKIIB_x_1NVm_ekAXZHJ9ZksmxwH4YCZVEKNK8WG9haH8CwBEu35fhwkKYxq7cWqhOLEdeeLaJ_qC3OvXAsyN1KlootEVwM9nq5faRpCOkCCPVkq8h3W_lS_AbQ4HR70eh-rsEmmmx92e7jNJnkX4QBexqFenyvDWR5nw5G19sTd8K2AifpO8REdR9rtxJtJUCCAOPZJnttpTh5KrYbcK-n29H3CbWorNI-VIjBqaHCXpctkVMXmTE5lpPwHH68tleuNw4l_Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Tt3JNfCY5NvBNxn7wJUV7tUdrqelwtcJa7uTtXb5953bS9gsAujluHyQT78S7gQ5Pt4GNKxdcNmnlKIIB_x_1NVm_ekAXZHJ9ZksmxwH4YCZVEKNK8WG9haH8CwBEu35fhwkKYxq7cWqhOLEdeeLaJ_qC3OvXAsyN1KlootEVwM9nq5faRpCOkCCPVkq8h3W_lS_AbQ4HR70eh-rsEmmmx92e7jNJnkX4QBexqFenyvDWR5nw5G19sTd8K2AifpO8REdR9rtxJtJUCCAOPZJnttpTh5KrYbcK-n29H3CbWorNI-VIjBqaHCXpctkVMXmTE5lpPwHH68tleuNw4l_Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz2ZQVsPoSuqhSjnG7_9NtYKJXWKsDXrEg64RksAUCWVMx0fANI3yBEKWnvu2Y1jS4ycDaHRdF0UNBTFJhv8putHzHJ4z-ihmigHQqfRjcNDNkLhsP6WjlsHOkbu3if-ROwz0AAHx1_XIF8-JUOUk2gu4hft2agNz3BBtSVhx2rvdu8Ez4waANnufAjn_MlkxlFX99pYZgk4jDFXqUSQ341M_rHuHm_n9yAI1mRzf6jwsQ7vQJaTkq8a7zgr-FRgAo1QnKb2t2B20y8CEge0kuZZJfr2TD_9VsafF90P8Ere6TNwgi544AUL-TP1Fzxon4Zh6grYsfNYFrTxrqmaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=OlGYMQMUNMT06JpneQ9wVOoJfkIvaKHgG1HlnwBWW_HE2zGAeFgeWwA5MLz1SY9h2CtO7qDAISHemeq1fJORmovanP1kGtOZes6bmFO2shInJWwxZLCTXYhids3Wne16kDw6lv6Sy97SaDF4UoRAo0IegO-WAH7Dp2z5JuS5cJnUe-Tfz6Zvfnzs12SnFWmX78mlMp6D2yaBjY7g6xNcrtIxBp7wlVdBU8XnzRVsIeXW4w0y5dubqtlkGB2pRX-H20kZ5E3cQO1dEJvPfEm0hiJhotitWTphsNVOXh6ydoJ63hot9XXC3z1sHhRUuHwfZmPeyNJ_p5rlA_JqtJ8Khg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=OlGYMQMUNMT06JpneQ9wVOoJfkIvaKHgG1HlnwBWW_HE2zGAeFgeWwA5MLz1SY9h2CtO7qDAISHemeq1fJORmovanP1kGtOZes6bmFO2shInJWwxZLCTXYhids3Wne16kDw6lv6Sy97SaDF4UoRAo0IegO-WAH7Dp2z5JuS5cJnUe-Tfz6Zvfnzs12SnFWmX78mlMp6D2yaBjY7g6xNcrtIxBp7wlVdBU8XnzRVsIeXW4w0y5dubqtlkGB2pRX-H20kZ5E3cQO1dEJvPfEm0hiJhotitWTphsNVOXh6ydoJ63hot9XXC3z1sHhRUuHwfZmPeyNJ_p5rlA_JqtJ8Khg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw3DaDPJ33aUgO9_RiTMhDp8nikO6C9LdacE4PgrtBtqlRno4tEWkKKwPfVmI1tb7KONwFYMxnH3krU1WEV_EUQOMVAuugNDLxjDViFC_Gnajks4KcKdRjQoFGx2g_fig0_Xq1E6Y1EDTN9Cp-WEVaAWwxYJwzNgGtS9RmMde17oULyq7-2CvBvSFRSM1PNbt8zZmGatdOkHG8kvv80MzWHc5jDvKfZXAf3oUTbkMPhHSXPuYIJc1bkYi2StEojQZeZzR5DOcDGX_p4ZjaNArBoRUbfdXTTpZOE_2RMVG3QG0QC1W8hDxeY_oXe5Uaps6-A1zb5CX-1RtGbmn3i2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4NS3y1ynPOfwh92bJzcvRfdWyITxcV_eHg4Z2skAL_fLWZrkq8WjV-yX0pYEU5IPhonKb4j-zGj5D3ib3HrRLo_zVfIlxJhoUMva3yJJpyuRbgwZqsmjyELvncwh1m8t8C9_EsbNDu0LFj0Twre5cbizQny6zZV-OGUHe5vjRrXhUqdgCdqMJmhtVE9_H0hIKPsBceje_ri5C_EVs_atMIFAIHO_jPrfhJWiyUW8FRmtvjiHWmqhd3Nl7VR-wlyKvu6fAbDoMSjDojJVWUVshVyIXOVDLclU-64NtuJV9_HqW5_Tvxk032AO79Sx6EIAMDSevUtqPIoPdRl6dpqyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhGeJuq8znu2hap780y6BNpWU8ORzh7CieA0uklpZJv6zP773EcSurvlDmfMsvQ117SM_IyKPSZ39Gk6cCalTvCn4Y5TiKulNyQAwHevlxQHaUhlKrZ3BsWKsLaYZx4lFSBDoGWDb2JIa4SOwZjYZJe3iGeBukAVb8AmxMkZ-72NSFDxiFBdV8CZSudSJAYZsqFOoORYXgl4x1kxmA5PQGp3skzEAgaROHexeGRIo3hP6QxqiNVXsoTaYrPpTzP1ELstkZNB0VCN-2RFNILUrDJNQZsYRSPXKJDolr6PdZCFOv_IZFhAk63Ej12nRN8Z76BAJn_y4xEq4wgkKf9ouw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg5Ch_D2_S92ni5edvy3mvPCOszDiyy0EqI6nh5QtAadCbhlMBWMqkCwwVZZWDZcJXufoAYEdI481_TcwC14e8L5IXAryPnnNRa6RvA1-M8rT4spf7qxffTA2eMAtZDjXwr-5bVcmW_GRZwRf6K_JjFK1bGUy_XQwROSfXv2_Aa65ox_LOJxsC-GLRLJ4lXBi8b9dCFxZR_Z8zLDU0sgxYkj5ZcWRgU0i_v2NnN0xRaV_55X6hA-AnaO3e2Hi8SI4pxodXte92-koTGLnivwxE3Ww-lOYRfXCzN3WuUYnOsLu7XpmpcEsDbigxfyHW4wHZt-MDYycAzB4oYZLFzO5w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=E2_zbwrMqyfyOGFC_wiRawHYXQGREOwk-gJ_Q5PABGOMQdqCJL3Ra_kaF76J69F4A2ZQgq3n4AILhu85trN3NPVeFqjk-kl9p12ko4nXEhYNJStQZXZpANNUUCUj-GZy3qPuQxf7XofihJKhtQN8nnxjsSKHgtfM35Wz4aUwpLRCkxmqhQxC3uTc4NJyGfyBTEpaxlycrd_jIl6VdyM69ezGlbH2iNklBb-Ij4lf_mL4l2v-g4R1SOSoJba4NWCRHIYxJEx1vW76c0I65WZYZM8-bptQmvG5Jp-vDqZasdEdAOJ-0w90dGCjIBimKngMITYQ34j4GQQsZwHV7g9tyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=E2_zbwrMqyfyOGFC_wiRawHYXQGREOwk-gJ_Q5PABGOMQdqCJL3Ra_kaF76J69F4A2ZQgq3n4AILhu85trN3NPVeFqjk-kl9p12ko4nXEhYNJStQZXZpANNUUCUj-GZy3qPuQxf7XofihJKhtQN8nnxjsSKHgtfM35Wz4aUwpLRCkxmqhQxC3uTc4NJyGfyBTEpaxlycrd_jIl6VdyM69ezGlbH2iNklBb-Ij4lf_mL4l2v-g4R1SOSoJba4NWCRHIYxJEx1vW76c0I65WZYZM8-bptQmvG5Jp-vDqZasdEdAOJ-0w90dGCjIBimKngMITYQ34j4GQQsZwHV7g9tyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=XwLVJa1dMiBXV-U6qBrH7qCG1gZalferm-O9kVlo1-riqUhgzGki6QK2LQ3LSXrbsCUWMsiKTPt0tyQitDx-KwKT0PEYhDCHmHs3eBkvB1YRApqyuY0vgDWZgHwFB1oAUyj0dKnppPgamGpeMtX1L_yLPnXIxhuhOCE5q3tNWA1vRW4dgPLPttgZP0ChMT2s38UV5JBXV6Ibt0W37EyRWr6xpnjcjvxzsGDTCVidYxDNSusEKB1sy0f7QRRVWrHQ4KhVrM_30sNW3uBZRxcRa830Zcv48aOZw7Hz0pS8tIhHQsYbKi_f6131uYyN7eKIU51lOojmr2H_w508YW5YBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=XwLVJa1dMiBXV-U6qBrH7qCG1gZalferm-O9kVlo1-riqUhgzGki6QK2LQ3LSXrbsCUWMsiKTPt0tyQitDx-KwKT0PEYhDCHmHs3eBkvB1YRApqyuY0vgDWZgHwFB1oAUyj0dKnppPgamGpeMtX1L_yLPnXIxhuhOCE5q3tNWA1vRW4dgPLPttgZP0ChMT2s38UV5JBXV6Ibt0W37EyRWr6xpnjcjvxzsGDTCVidYxDNSusEKB1sy0f7QRRVWrHQ4KhVrM_30sNW3uBZRxcRa830Zcv48aOZw7Hz0pS8tIhHQsYbKi_f6131uYyN7eKIU51lOojmr2H_w508YW5YBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=lf_6kJ9bcPgEayRQWgROu7z2Hmf88QmP4NGrzg4kWOv48gyV0grlTndAVfN3iKcSNaV0NdcZu7PROnLAoAZ0dUQb8fY7qrdHCOwC11sqCaIJEPMB-vjhsAOON93rWH6NaQ0ojnvz20i_vdaL9sHjtjUh2oHV_-ZI4LQHbB7BUrJ-MIdAuAgJAS77Vh_RKZkHfiXxCRYHRCvgSFxe-B4G9iKCUrDMW4D3XPh3pGhEuUdbyvkbej8IVqCZ4pHT4OYCO3IN9ibQh3Nnfi2jIpyFKfohO5Saa7AYaLIAAhmOhvassp1-1ITKVB97l-wOpmHZvNivnIUrNjetNw3Kf4aSvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=lf_6kJ9bcPgEayRQWgROu7z2Hmf88QmP4NGrzg4kWOv48gyV0grlTndAVfN3iKcSNaV0NdcZu7PROnLAoAZ0dUQb8fY7qrdHCOwC11sqCaIJEPMB-vjhsAOON93rWH6NaQ0ojnvz20i_vdaL9sHjtjUh2oHV_-ZI4LQHbB7BUrJ-MIdAuAgJAS77Vh_RKZkHfiXxCRYHRCvgSFxe-B4G9iKCUrDMW4D3XPh3pGhEuUdbyvkbej8IVqCZ4pHT4OYCO3IN9ibQh3Nnfi2jIpyFKfohO5Saa7AYaLIAAhmOhvassp1-1ITKVB97l-wOpmHZvNivnIUrNjetNw3Kf4aSvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=m7uZ-O5HxaiTo3q47N_oEPpvnTQkqs8YP5aUZvIszyGJvUr1mq9l49HfH-TSqktq897fMisMZLJzbNLgHxSq1SKO-r2gwd0S7YkmqHIruRM7QJd44wipm1rsO6k0ETr4L9ziJGpqKPt3HwlaFJRJBQRmzuHHZu8pJ5w9Klrbv633Dd5oKtWHniF-ckuvS4DMfvStCOnFv-0X1w_laatjp5bLm9536MHLrGwGoM5aRkcuqifLuynwXxZddxGn8V7LTfZQu9z0Ol-vTLjMZMFrz3c6vqFmAdiUuK0xbZzodZimDQtReAcDz6cLw3KPjquER8LFsMq2bjtkM64cAWcNg5Sjcyi0BncnMizTJrDQPj9lwtkzymG8XIUMRTOTAW2Im5x0RmKptrv3_Mea2X7HQ0icoRuwGzBry6X4NOoIhZ3EMWdCqA6XHvuVc8FzwXUqoyhx9mSK7pbILl1qK5O9pA5kso4WkRW3EJYp2GpKaDFeekpgryFRcQSLsDtYvAeAzPuU4AOxxXE6sJdk6xU0TRUY3dr-2sSo1zNwpqLcguxgHOazogmTIY78kmJcUnv5ASltOUnyVUUILfdWGcieB7G3FBmu61qRjZ4pvPOSDePAKcd_1Ni5WirTL8QdikKaLRStsAP2zW3fAKShpbwNG2s3doNx-AEt_xM8F5fw6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=m7uZ-O5HxaiTo3q47N_oEPpvnTQkqs8YP5aUZvIszyGJvUr1mq9l49HfH-TSqktq897fMisMZLJzbNLgHxSq1SKO-r2gwd0S7YkmqHIruRM7QJd44wipm1rsO6k0ETr4L9ziJGpqKPt3HwlaFJRJBQRmzuHHZu8pJ5w9Klrbv633Dd5oKtWHniF-ckuvS4DMfvStCOnFv-0X1w_laatjp5bLm9536MHLrGwGoM5aRkcuqifLuynwXxZddxGn8V7LTfZQu9z0Ol-vTLjMZMFrz3c6vqFmAdiUuK0xbZzodZimDQtReAcDz6cLw3KPjquER8LFsMq2bjtkM64cAWcNg5Sjcyi0BncnMizTJrDQPj9lwtkzymG8XIUMRTOTAW2Im5x0RmKptrv3_Mea2X7HQ0icoRuwGzBry6X4NOoIhZ3EMWdCqA6XHvuVc8FzwXUqoyhx9mSK7pbILl1qK5O9pA5kso4WkRW3EJYp2GpKaDFeekpgryFRcQSLsDtYvAeAzPuU4AOxxXE6sJdk6xU0TRUY3dr-2sSo1zNwpqLcguxgHOazogmTIY78kmJcUnv5ASltOUnyVUUILfdWGcieB7G3FBmu61qRjZ4pvPOSDePAKcd_1Ni5WirTL8QdikKaLRStsAP2zW3fAKShpbwNG2s3doNx-AEt_xM8F5fw6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=bbQs3YouZzWhpOG29w6ol210UMh6HfZ-kBjcBqQUKP4LKQh1yI58dyAttDIm3bMn23cLchQY3D5eeqGKgTS-gZ6Gx3ojFT3_UUpBOk7x4ETcWr9Y33HQtCWCYuMTR4scd74LyfE5E6MeCKHNPtWZK5zsCkEd9dTLDTN9VzZnv65zKjPIhEaHI6xYU8uKzLN4mbQ90NqigO0R1ALUY1gf7ltNYDESrtwkq82pVLGeE5yZD2RIjdIPHLyp0OjwYNpPM7JZvTx-AcC7biU0_Z_G5OoZ-ObHBWEBdkZZxAq_wO9F2PzlnLCBVRJtWJhMvfJ9kKuKVVEAQsDGPMGlHphcAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=bbQs3YouZzWhpOG29w6ol210UMh6HfZ-kBjcBqQUKP4LKQh1yI58dyAttDIm3bMn23cLchQY3D5eeqGKgTS-gZ6Gx3ojFT3_UUpBOk7x4ETcWr9Y33HQtCWCYuMTR4scd74LyfE5E6MeCKHNPtWZK5zsCkEd9dTLDTN9VzZnv65zKjPIhEaHI6xYU8uKzLN4mbQ90NqigO0R1ALUY1gf7ltNYDESrtwkq82pVLGeE5yZD2RIjdIPHLyp0OjwYNpPM7JZvTx-AcC7biU0_Z_G5OoZ-ObHBWEBdkZZxAq_wO9F2PzlnLCBVRJtWJhMvfJ9kKuKVVEAQsDGPMGlHphcAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=YZ7AnuuhTpVA2j1VqNg_rt6mrom07zL7ButZKIJ80K3LS11zI3ZjBkd-DK1O1WKtzgIS8kwUGbQ7lbdUdNF7wibk1BC13AjdTc8FE_AKjQQPSXKxbU1VnvoDUz6RAJnYIroTRG1eguepQ0Npwi5G4U1VqKaygacLg_r77tAg1fs2ING_U7yenOTZ6wZBzNdtFwvonyXIODWxwpgphFrHK_7wXZofAJJsl9ahWNIK8AVLuLknW8wHR497yoMzhi2Vz_UK2bk1ObNCCQQ-J5bmRrtNyBAqBOdO_TsjX5um1a7v4IiMPDHTVCzXMmrebUN5Hich9RtkJD1isA8Cn4C35A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=YZ7AnuuhTpVA2j1VqNg_rt6mrom07zL7ButZKIJ80K3LS11zI3ZjBkd-DK1O1WKtzgIS8kwUGbQ7lbdUdNF7wibk1BC13AjdTc8FE_AKjQQPSXKxbU1VnvoDUz6RAJnYIroTRG1eguepQ0Npwi5G4U1VqKaygacLg_r77tAg1fs2ING_U7yenOTZ6wZBzNdtFwvonyXIODWxwpgphFrHK_7wXZofAJJsl9ahWNIK8AVLuLknW8wHR497yoMzhi2Vz_UK2bk1ObNCCQQ-J5bmRrtNyBAqBOdO_TsjX5um1a7v4IiMPDHTVCzXMmrebUN5Hich9RtkJD1isA8Cn4C35A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
