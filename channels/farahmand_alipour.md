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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 14:07:51</div>
<hr>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IotlhauxxamIoDVWB22596GsxhSImjjoU_l-RM3CIcp0hXl4G0fOXuVibEkxZIx2BZ3mqc6SOxR-iwulyUDdr9hlT8tNAGFOy4zwZxBuBsrfofLanDNYJxHgzMdi87aIPH3UEWDbmpJ0G075KHvCuGJnoi3k9WVlLN1y3K9dmvOpPWMvlQJt9EEtsagGgdeQJ5rY-womaGpExALUJnuXkEBji9W1a2_UVWLil_PcUrc-0Mt1gc4nJhVtF7iYrQx6Sdb0ntH6iKm3gT7cR_6NNjOOwivUuqMgb-nsEzDgW_p1wGaqx_6IU3IkfCEQ8-L0yys12NA7EHrx-hGYWYCH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh1gIiMO26gKmECsuBu-x7k7PHtOiBsdlmJvQDDWm9Iu4VRDM9H8ysl3rF1ztO0H9CVJQTQJh_gixp93GE6iF9sB08ueqJrv3RxESsmRam-I2-HbdJS1IJIrGrNP8_7obG_MfOEJ2xHxXXu9zQlWev68zWhM3xKr8wUKhZVLxYeEWBfzBhbK7g6LR7GH6jBVtHvZrsMwEeOrEV6FSqYs3gvFK_i9lC0h9QtHkxXPZaYPqzpN4v-aZ1e4KQzvDn02L5A3XfT-1EOpWeaDaC5epo6pbtaeV0e7OZQNvlhitP0LsH4oH2Vw3F-p4NALcS3byWd5oN9vThs7ng8bR0ESgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvHwqgI2ExWT3XuUSw163hbtaLrav_ZRLgUnBBkSckizl2iotJ3uGW8JdizVmP95Dlt-9wN7lZx-GxA0roUBIk4trkNLCcf27_xYee3NIzlB28H08OGwJlf5JJe_4ZIJSvunHLusgqlKwJap83XQmFRPoKuercvuMz8zau-qSsmsMe_mqIk8j07FupptfA1t1jJgUCNQI1Xa1ffiWc3NP4Omhv6KmW58gea19p78DndxXpGl_uUR3HRLrfUf2rrNBtY0WjT2NwKb3_WsxwH1gffr5XUcmRHyuqsnv8JaMQPH66d4HaRs6fahIt3AXf6PESxgMT1ivJVUbLZilcMp4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spomz7bjOu2I5arbglW-35Spx7_PdN3RWptxCq-doJKbFk-6lWPrCZFJn_pYKqr_7UqjGUnpoHTbhGiH8CvaSORrszeWYO24nk2mbK9LU6fyyT12tzRb0PrRPHZZKTbM2bQdxa6wkUB_mK7zZNRuOc68BTROshOtec272ZdhtlBpQas41pZJYVP1V7ozgWZn9jQGVPum47q58-Ho3QVsLc2sa5mz8g2rfYET_ac3A16C-bVldyCEdgeWAclSuZnTLhg1OegTQh0mz-hYlnyUyeTG1LIJ7TBpGBO_bMnGA3peyXFdhT4tURIHzXlpI89bqRNiKVRNGcmdP0YhKTqSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Sut8nM3uZIZ7LyP6eqZm-1g2REnsncgZ-iXHveWoTEaccVi5i7y2wOCPoxE5ET86yJL2zCpdHKDeru988b_PJaVhDCHPpg7DsuLwTwLvykrbFYXPWDUSBM-mIUQgiHlF6yOhIONwGB__Z91dEQsCktDWn85Z_-lS3PQJUVav00JIytS4PfNLmmgBJDTEuRj2jQmEVPImp2-oOkJTaXfcS2OHt35c2HjYWqmg0erF2FQ9tc32nN5pl7xutHi36HXeEdhQ3tn-eAXais36u6dffdiDWHwdnO-6I1OmBBvgEqGErnpzVkPupSLwRGAEj0AnEl8RnKeDBumMo3y-Kmh2Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Sut8nM3uZIZ7LyP6eqZm-1g2REnsncgZ-iXHveWoTEaccVi5i7y2wOCPoxE5ET86yJL2zCpdHKDeru988b_PJaVhDCHPpg7DsuLwTwLvykrbFYXPWDUSBM-mIUQgiHlF6yOhIONwGB__Z91dEQsCktDWn85Z_-lS3PQJUVav00JIytS4PfNLmmgBJDTEuRj2jQmEVPImp2-oOkJTaXfcS2OHt35c2HjYWqmg0erF2FQ9tc32nN5pl7xutHi36HXeEdhQ3tn-eAXais36u6dffdiDWHwdnO-6I1OmBBvgEqGErnpzVkPupSLwRGAEj0AnEl8RnKeDBumMo3y-Kmh2Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=DOgPu_zr2IkJz1x37SSg-3UbqFs1huiNeabmHYlTFjKjnOH4jlj3mgJJFbxuh5yH2ytodh3pvlJGWfm31N17O7cS-RV4As3XQHsjrT_J4eGZ3qEypnYC4yZY-euiYwXKXP_rTZokx9mKWuTAMJrDNn1kKw8Sj0OWWYUBHYA5q6LX9VV6J6jpRHKzjz216rwKVTGwze86VXjTPFcd7uw-aNg3d_w7G0QemdQCkju6g-oFJi3c_k2VHM7ZyLpuPkIKLFZ5fUS3lCGYQVp5V83HqRQK68ilvEpTA2fr_FP3DzH0VRrrf6yrik0Gs88amlKckkeZrWl8WNG0Tule8FAFwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=DOgPu_zr2IkJz1x37SSg-3UbqFs1huiNeabmHYlTFjKjnOH4jlj3mgJJFbxuh5yH2ytodh3pvlJGWfm31N17O7cS-RV4As3XQHsjrT_J4eGZ3qEypnYC4yZY-euiYwXKXP_rTZokx9mKWuTAMJrDNn1kKw8Sj0OWWYUBHYA5q6LX9VV6J6jpRHKzjz216rwKVTGwze86VXjTPFcd7uw-aNg3d_w7G0QemdQCkju6g-oFJi3c_k2VHM7ZyLpuPkIKLFZ5fUS3lCGYQVp5V83HqRQK68ilvEpTA2fr_FP3DzH0VRrrf6yrik0Gs88amlKckkeZrWl8WNG0Tule8FAFwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwYFxdI9KkYOpDnGyL6pAct0ypYenNuDetpbZpdpItiPaoacn1t4mM7g2h-cAu7uH95dBqIbF1r946LIqDUPw8mvLSffA5COh_x7yxrDLlQjGmNidvu-M5bPJnViTRA4gsUA0XIY-FnsC-CdXx8-6YcFNBTU2erPkAl6FYFE-hSvsDSvM5BWeylKpU97uNAh_vLNnGX5-7_K82De-M4MioIs_O-4sF7ciaBxo9y0ifre00Dw03cv-sT2Sg6GJp0sSrxTGJDEq4pvE3t2OobTEaVD3wM8RNsrRUl2qhjx9SRR34BL5xq4iFs2u-U3_VZZ7_dCcseIbRnGJHcDc_DfIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1bHDHg9XYxEmX9IlNfSm4QJTnTH7oktxBmuVCWGjmLD2tvkKcvdIQC58xYqpboBqH66zy3AdI23gqGVFOTtdH_ImJrRfTVRJ6QooSwyR-6PiQ9bYQvOE2FSsKdmFNb7WF3YPpEOO1Az49uqoeuLwF8N6e9TupYe_OvEkk3NiYjjVf7ABYbL30OsRPED_kZf5a-T8wFwfwdiCc9agrsE78DpCCsCu3wQSSOLAfxplg6TDd6t7gOO_c0GIFV4UznzYtgJXkUarSjwJ3X3tx6ywgvKrBtqSig1A_LOuwrIFRA5jMUxxgoh0bs2OwrUYR3rPHpqba8g-HR3UhmzkidbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=CSh0HAVL_o2S6Qzy2wDRoulY-ie8OWQXCqDPBqY21HFS9CVPjX4gJzAyOeTf_kbA--E8kLOjU9dLg1xzr4cfk3P9jQHpLptAYLaPKhmzjtrUaMV5Opswaclyh3012Nplaca2-f0Q7VHQpVec49J8ZZyY9KjEI3HcYAkxIDPrOxRpX6vJE0s6dvL-Ry-TFLRjxpjlbEmWWMN5fa1HHSSDJRbCOY2ceAN_MlCujxv1lueXESMv5588LuViMHN-eClJi1-zNWKGcfbOHcESzOzJ07Trfb67moV4KC-ll411zCGbP66vaF47axC-1xPJx9vn_j115Pcj1wXRV3fjz8BXCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=CSh0HAVL_o2S6Qzy2wDRoulY-ie8OWQXCqDPBqY21HFS9CVPjX4gJzAyOeTf_kbA--E8kLOjU9dLg1xzr4cfk3P9jQHpLptAYLaPKhmzjtrUaMV5Opswaclyh3012Nplaca2-f0Q7VHQpVec49J8ZZyY9KjEI3HcYAkxIDPrOxRpX6vJE0s6dvL-Ry-TFLRjxpjlbEmWWMN5fa1HHSSDJRbCOY2ceAN_MlCujxv1lueXESMv5588LuViMHN-eClJi1-zNWKGcfbOHcESzOzJ07Trfb67moV4KC-ll411zCGbP66vaF47axC-1xPJx9vn_j115Pcj1wXRV3fjz8BXCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOGh1bifddvkmixW-NA5p7gsccnJkcOSeWEO5m97DfQt6roYhBE4zzK0X3k779WzVdSepOa_pZCXxFgYPXcywcexU804v8VC-6WfxZ4dhCr1Uw9mqNFXmhSUSjtjmpebzwEf-DxxJPkuyWKY7Qb_nCqsawWr8NxtJ4lmwMjhPSRW32HEsUZrG0Wgi7xLhKypgpTlhR1nghWlsSNMmHBuNE3NedWl3w3LRVy_cD4NufpHOEEs85_zkubIZJl9R8CeHp37miBCI9JOBQeSMTg97G7YVruntPxDFjA4jaoPRLrYBXyPrGmXaDEzi9WGw4hS_y0xVASqyz3nkHTe6DW0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKSL2Y46k9lvdEcScCaX6qKH2m-WOqE6ttZkCcVui4DtLJE7YHMsxR4IR8IaaHO3tM7lnrorlTPCUuBPAAvIGgyWx0FrcJ8KXcehhvrRHsBZ5y7xiXGZ_Sg7bSBvy_OxklorObTqxbB38i4k7VAQfqs7bgHI5PUPbb05yTU2hOISSDgwcUx7W8d9_EQwIQj-hfAnSoME8Quvms4dWhbx8O7OC5UYVQEw_xijjZFrJJvXWD1bd1SjUu7CkvJBDJC99yC4HDs0ToKVdR9by_qTkiBTzRj6ZQNeT5Yix-N6ZiEgJvDOgTt6yQDK90dLeq4ib3xFXf4kXwApGswa7NRKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=HouiXrPaJ3BeSahoGTcXugfJAY8dg3BlUFGvXZ8UuSFkhYxju30IcVqdVSP-yG7h8AQCRhaKbbfPBGdmnK1QvKyzZFyMn8We9SZIiitp3Yfw41B6B1RMlRfDyAXP2cLuVLsm6P5gyIpI9yYvBNd3mdZ7_R8D9pAjUQAOXZ_PnMXkrbRc5Rjp1ulGPmVVjVSeFSdSIan6IKWooKKxEvDeH7vDAP4Qoot4_rsZ2qeczhC5MX0Ztgtf8tc879qxXOjsLgm3lWPxUdYzQA4DcDPfqzTCTJoXpYwmJSa4-P0DU_Ixn7Er_XHLoCYvTKqCnGnJFuu3f0hODNHMy_a2w1pwLINETuxP1TX3yAyFuGXueH8Zui74To-jPesaoUk3eboNEAo4GEORPqWxqHwNIBJLUFxVOdiYrF3hMhfgaO5rFfbNvTTIkcsdBIUg9jjotfdeAbcO4HenS0KJ-iSNiPxFnfSp93pHHbWUvKp9wxuwxyMK8ADIBRu2_i0ZXGtJ0CCag5Ezmw0VkQaTNWtUmkr5qZIWfKQLFQLB0Osvwos5RsVmLMXgjeJh7lneE1EsczPz2-Rh6OWl8IPViJ9sBBTgD3GEDzUXtw2tYtjmfom6ggytfZ075pemlyCLaDWkdJKKYGSk2v-jNNIk_R_RbOu4BPL1kanJGWoM5XTSq1pkBmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=HouiXrPaJ3BeSahoGTcXugfJAY8dg3BlUFGvXZ8UuSFkhYxju30IcVqdVSP-yG7h8AQCRhaKbbfPBGdmnK1QvKyzZFyMn8We9SZIiitp3Yfw41B6B1RMlRfDyAXP2cLuVLsm6P5gyIpI9yYvBNd3mdZ7_R8D9pAjUQAOXZ_PnMXkrbRc5Rjp1ulGPmVVjVSeFSdSIan6IKWooKKxEvDeH7vDAP4Qoot4_rsZ2qeczhC5MX0Ztgtf8tc879qxXOjsLgm3lWPxUdYzQA4DcDPfqzTCTJoXpYwmJSa4-P0DU_Ixn7Er_XHLoCYvTKqCnGnJFuu3f0hODNHMy_a2w1pwLINETuxP1TX3yAyFuGXueH8Zui74To-jPesaoUk3eboNEAo4GEORPqWxqHwNIBJLUFxVOdiYrF3hMhfgaO5rFfbNvTTIkcsdBIUg9jjotfdeAbcO4HenS0KJ-iSNiPxFnfSp93pHHbWUvKp9wxuwxyMK8ADIBRu2_i0ZXGtJ0CCag5Ezmw0VkQaTNWtUmkr5qZIWfKQLFQLB0Osvwos5RsVmLMXgjeJh7lneE1EsczPz2-Rh6OWl8IPViJ9sBBTgD3GEDzUXtw2tYtjmfom6ggytfZ075pemlyCLaDWkdJKKYGSk2v-jNNIk_R_RbOu4BPL1kanJGWoM5XTSq1pkBmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETrb-vfn2CJSHCJx_DDIyQtSh_BREtXQXqoDVG20X0dWmxiDRGhGfQXG9OoaCdqZXt4FCxLVpgfnNksP1b0dWbC0M1KRZTSUFyHLSwVqc4dBx8fuhuOOA6d3TbHcDZsLBlgsjWGb8ZoHGSRY3ABWbNhdbsN0SUeqw4nJkcEtnMY-V8N7YyI9WkYxzJywZV0ZAshnnhdiK7NPVh-gd2LNwqv6edcUs_LaV8LPVreLQpIrOp255_uemzoIfmqNBacOh4FsWoFtyK60o5FUP71CqezEqwC3jmvWDtMPYu3S2Q3OqeVckO9RcHSk8eIr7J9m2UyJpzvipZd7FPTlgvPxnQn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETrb-vfn2CJSHCJx_DDIyQtSh_BREtXQXqoDVG20X0dWmxiDRGhGfQXG9OoaCdqZXt4FCxLVpgfnNksP1b0dWbC0M1KRZTSUFyHLSwVqc4dBx8fuhuOOA6d3TbHcDZsLBlgsjWGb8ZoHGSRY3ABWbNhdbsN0SUeqw4nJkcEtnMY-V8N7YyI9WkYxzJywZV0ZAshnnhdiK7NPVh-gd2LNwqv6edcUs_LaV8LPVreLQpIrOp255_uemzoIfmqNBacOh4FsWoFtyK60o5FUP71CqezEqwC3jmvWDtMPYu3S2Q3OqeVckO9RcHSk8eIr7J9m2UyJpzvipZd7FPTlgvPxnQn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=v3jxP5y-PDFuyoy0crQjKRceywxHG5fIbd8JZgufWUEXIvGa3mqIcZqMQcuThPVerSLaP_RFEkYNxpqOR09hGiX0KeMChsAm1XIqh4R0Z-eFoRmz5q7dajzRw7d2mKr_EP-oDMYmlBGnx46VlhjNhMrm_YEG4Kv8aiMSkIjEcJfxZn8yegpOxHUWxOrkeFew2uSyBvEoPJItx1MT8NyeEA1wA9Br0Flby3gtxDUOhLVEZANr8Py3NbD0YH951r8plFG8Vlt6U7oKSbOockgeWUeGvOlKcgR73Jshv4YGzIW-8ejtGGhdmWC4kJooWdSz39PxMyo_HgZ2i2cPW7hNboi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=v3jxP5y-PDFuyoy0crQjKRceywxHG5fIbd8JZgufWUEXIvGa3mqIcZqMQcuThPVerSLaP_RFEkYNxpqOR09hGiX0KeMChsAm1XIqh4R0Z-eFoRmz5q7dajzRw7d2mKr_EP-oDMYmlBGnx46VlhjNhMrm_YEG4Kv8aiMSkIjEcJfxZn8yegpOxHUWxOrkeFew2uSyBvEoPJItx1MT8NyeEA1wA9Br0Flby3gtxDUOhLVEZANr8Py3NbD0YH951r8plFG8Vlt6U7oKSbOockgeWUeGvOlKcgR73Jshv4YGzIW-8ejtGGhdmWC4kJooWdSz39PxMyo_HgZ2i2cPW7hNboi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=foFYSFEBzl54dyOa8dTMfqljbfKcoMLCLyy4fCyykZmTPB1ULsByGUkY4-B1Ny1uPYv5l_zXv5A3U-Gmln3LOfEF6O2Br7CxQuk4LltDZPd_YbQHirz3LdcP_NC7Ma9IfgoDSk-N9d1jMux6m6tG6Se2Vo7ZWLxQuXlDW6OqdIplvKP1DEZPu_nhlMZ-7jczFe5Bn_4Tdeo-9fNwsWTWudtpoG4_cQZ57gyeVPoXVQvgWSCWPN9XyTMRTivIjdEWMgGAa5wjgkoDPM4uWSm9niedgNLiOvGA4o8yMSsTXmv5y4iaiUXlRqsClSt2_vjmOX0c8DPjMk-EMiynMmQUpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=foFYSFEBzl54dyOa8dTMfqljbfKcoMLCLyy4fCyykZmTPB1ULsByGUkY4-B1Ny1uPYv5l_zXv5A3U-Gmln3LOfEF6O2Br7CxQuk4LltDZPd_YbQHirz3LdcP_NC7Ma9IfgoDSk-N9d1jMux6m6tG6Se2Vo7ZWLxQuXlDW6OqdIplvKP1DEZPu_nhlMZ-7jczFe5Bn_4Tdeo-9fNwsWTWudtpoG4_cQZ57gyeVPoXVQvgWSCWPN9XyTMRTivIjdEWMgGAa5wjgkoDPM4uWSm9niedgNLiOvGA4o8yMSsTXmv5y4iaiUXlRqsClSt2_vjmOX0c8DPjMk-EMiynMmQUpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwxmkAay9S2I3e6w5oNqSGaOgKoT2XTRoemAMwgZF1vILm4BX0paacZhocDoftfcAiks1URr4Edk1Ql_DST0XD-7VEPSHWZq6tMjMnz8W02SkiuwfnczSf3r2HX_0e7m1aCzqWfex9-iVuK5-M9IsmwWgOuL7Xaf4-W15TymYfX_QedBTuTosd7haZ1MOU5g_cdn0q0cet0C22-Rwdu-HnbMaXe194vhmMdR6G7YPoAvTF4nAhFmmmt5-p-GKCmfpfAE7T7Ckx_ouOtfgDKHJiqu1pFL0sfb0JE4xzipzHEwMQOaWs1T-lrhRVprHQuFiw5HM3Oi1FTgd3CM8VK0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F262WntQkjS_5JBAuXkK71WRwja0FwZfEXQxAxDplbr6jURFM_bdQk87NX234fOSASMjKy-JBw6gH1r4VtfxdPJZgkfy4OOcTESkvwBaCagT4fUOS27Yxi-UOUyOphy9eQqOCWQCqh8YaX58s1hAzAxcdbZjWEDogo_dy4ZxaMzjgqlQ_nasDe1np6aNvSiXnc8l1H5GLCbIPd3B5Rj45EAE9zHMNmWmhC3LPknkLKhJMMJ1-5Vh_zhwz4mS9ib18JADK-GgBpgnTbJbr6Bag0PDTk7UbBPoZL1lj9nk68c-qppJmaWgndb6iUg4GQMqLgk7BkRP6gnW8sZAWTyKvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLCdH_4UmAV_U_ibr_Jz3nFFsl7RBrq7Nqm_TxyrzFJ2X_JuZRU3mDV9wF6Zjg1ZeZ9Ac7DTB51zGjaqBXZFFfYH9_c33JC5qD1XRG1RjFzJSdj8z9kqOAnz900Em6AcVh1Jv0GklzY4igXovr9OCKXiS7U01mVpFE5fV3ZMpVu9n5Vj2QL5insRmqBxLBNxhwUTCw3Pify9-GbCpi0pqsumowjz-XNeJ_byVcUoLFiWLH99S0rn4ROXki5MrUgAWlzKeBUM_Atec2709HIQigdG4NazuFZpSACJO4KncQmcxtmi31Qkz4VLkh8tDDH8SiJKLDoj1NEbijLDrIiA7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMvqul0L1Z52rsGJstgryimkCqjFQFp-41S09gNy4I_fHnxnu7Vj3C2vHBcpyTUZn8mUsCvr0KdwxiRK-iMd-1IxpsGohyIEN2nW5bqXXzgfRDd_dkpmKidUxSiIW0wc6q3xFoqmGRpO4Mqt-d8I9ZNBzt9KIYtXkxMHvq7IKgYiSoqQEQ3nr134H1Rjt3OdjHvNQOZP_9cSupgxtPDImM2Xil2zVX90LzLG-a6U8kBrpZUUWRMiS7QGWNmEOk25_yZr1h324aCO1coyeRjJDReungKxGfMLruUeTAnoSpSg0udMPfdwkejr-y16cXIYGFRr6lOAK70Mrz3MpT0JXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loTpPMZx3r4LxScZ_Lp5JYHiyCLJBFGtgxhYkNBPTVcWcrxl-3ukjIqeJZcMvfdtzHJX8GH4YM7lvB_Mf5RVSVeCk4-E5FZa4znue4KUdznVnWa5gLFMEA4boBtVBMQp7qp2ETvvB46gUDPNp47ftQISPNks69b76eGhlwc0Y6VG6QZeZb3EvThPopcqQR1yp8hN4R1qMpg2An6bFA36J6W8sReOTfYc3FCBtGUITY_AIdCd7PI2mxj5ucb5ShxwMjcimSoVuQtc64xcrSYPuydMQVPWCjW79xYO0Rcnpd7jZbvU2ckrKxKnBH_JdNAAGfp65k61VIcWbcC8Nb9kkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=OVeA_3HFqYSWok6d3lqJFFdgR76RJJS0iCk-sSQwilskwOZegvGoAaOjPajB4_SBTQxHfCkGLVi2FddY3ZkIg7oBngImxbPGcwa_Z4TBWpG3okcxcQAl_A2wopsWueAj6xZ8MHuYgLWCqtSbBbUjAGxxRvOQsUJiaJcnXTKNXcn-_ZcTmOjzJctMZVePfibd9bzF8IYtK-KHIvKAdcHG_9XZ0wrrELczRtqe59ZIAYVLRBwia_Is_THnY0lj2oU2uJuuxoRUxvGb-xuy4UR4jneNRKduhZELhR0G3E3RKOvun-L1XH50VeeUP9HyvqDPYLiF8V8wShSe2u2uVTSnHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=OVeA_3HFqYSWok6d3lqJFFdgR76RJJS0iCk-sSQwilskwOZegvGoAaOjPajB4_SBTQxHfCkGLVi2FddY3ZkIg7oBngImxbPGcwa_Z4TBWpG3okcxcQAl_A2wopsWueAj6xZ8MHuYgLWCqtSbBbUjAGxxRvOQsUJiaJcnXTKNXcn-_ZcTmOjzJctMZVePfibd9bzF8IYtK-KHIvKAdcHG_9XZ0wrrELczRtqe59ZIAYVLRBwia_Is_THnY0lj2oU2uJuuxoRUxvGb-xuy4UR4jneNRKduhZELhR0G3E3RKOvun-L1XH50VeeUP9HyvqDPYLiF8V8wShSe2u2uVTSnHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=EummtFvxc7SsQ2iE4bLnH3lFFcCM3v4z9X0fyQ19IJr_gdEc9iKs_6UZLvNBNhrQeqPPA1vGS0s3TZkKOPtW8_O9OaFZS65wW7Xzvobbin5bE6c5Tu1GMwmG9pRvE97Z1hmxVLwm2_FMsIWj9t0osWwjTicBxRHHCWuvbql_K43pHiARvfwWWfqBFUKaB_dmpMMs5Fjnv1Jvez2V0EPxz8wclCAW_sISu0JvY8c7gwSIwkMRJeq5QebBqmgJlCcyUG40r-dzS4FtG5WnCLePifgekqzWDAvn-JTjyWXuj5SmA6_mmdU6fgC22zWOBSHCoN_rui_i33b2Al52p0D7Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=EummtFvxc7SsQ2iE4bLnH3lFFcCM3v4z9X0fyQ19IJr_gdEc9iKs_6UZLvNBNhrQeqPPA1vGS0s3TZkKOPtW8_O9OaFZS65wW7Xzvobbin5bE6c5Tu1GMwmG9pRvE97Z1hmxVLwm2_FMsIWj9t0osWwjTicBxRHHCWuvbql_K43pHiARvfwWWfqBFUKaB_dmpMMs5Fjnv1Jvez2V0EPxz8wclCAW_sISu0JvY8c7gwSIwkMRJeq5QebBqmgJlCcyUG40r-dzS4FtG5WnCLePifgekqzWDAvn-JTjyWXuj5SmA6_mmdU6fgC22zWOBSHCoN_rui_i33b2Al52p0D7Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFqg4XY2B3zEFzliXr1Wt0Ni1Z_j7xZXUP0CX12yA2MdQMv3v9sCbyudRQN_VPlf9b6xi3u18r99GCZvcDVF58kAo-fdO2afxZt6_3t5BqOOP_CPMYwsOvuxx9TWg2BQtzbDmvnEFVEcNktGdgoz2D5-GNUPiuJ6ulxIV_kpksudSZtRLF86hBg1_o5VupKhKLlz1XE-slxcc_Pa_frvD9E2Kw7B0IinnkZ7R1V_aRAZar06WmxLbs5GQ5CuOAAR3HcWI52s3wFf0LSh8G4zUfYMHIEmi1uMDM20XPEug-bRv10dFXqCwiirC7SY7c7-apIrwGnv5lEBSunGQdv3Pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omCLsA3Fs5pq5sDiEIOXO32Ge95vs4wAHMiIK-PVR67JLjQSVbaeTNOnsWgN1MciY6kMY6VtblvUaPox6prgQg94Nahk7x_SF0v8-xwxiknoMUgMDniQbfcBsz7icsVMHGpcCS2aGUYM64WA_wBJAn40MfXHARqGlEOg2LBgappAdk4YD7BnsFZtAQAjm3ryE9r-hFcfeftsE069Vj69zEQ1J0-u66GQ_lvjJRKia7WDwlJbhv2onsGzBzJN0YZMQvZE3tFginXdHaxIkyubQ1F6QurqXZIa02AR8uj9c69EtcicZlELL6sfeN9x0Fa_GCaYsq1mHoE7x24T2nGqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=NbeTsV5Xweaw00Zdwa5_MiGlyApRU3xk4l3VDusTd_8N9I7LegB4kydSi-3_9aMIqm6bJKbafxDVAMoLYzmcbbGHk35pYL57NsZbGq1nPHF7biYaLbIFqVKcR4Eaqp2UwvFFd4Bigc1dfu071cH0Fdwk7pxy4-acgjtPs_TqWOn_tL5TSJdPFIO-q50hUMSWbe3r3hyVjdq4cbDVoFBb5Ayfykt6N6UV_9pdtvw6js4V2Ot7xE7kHydeGGD4-ZzCxYgi8KchryuW5mg0hsFDQuIZznoBFZe8vk6xcYRbKm39DMQjlJWNpheoNQNV83eouyoWB4-ruXeyCUkK_h6Hzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=NbeTsV5Xweaw00Zdwa5_MiGlyApRU3xk4l3VDusTd_8N9I7LegB4kydSi-3_9aMIqm6bJKbafxDVAMoLYzmcbbGHk35pYL57NsZbGq1nPHF7biYaLbIFqVKcR4Eaqp2UwvFFd4Bigc1dfu071cH0Fdwk7pxy4-acgjtPs_TqWOn_tL5TSJdPFIO-q50hUMSWbe3r3hyVjdq4cbDVoFBb5Ayfykt6N6UV_9pdtvw6js4V2Ot7xE7kHydeGGD4-ZzCxYgi8KchryuW5mg0hsFDQuIZznoBFZe8vk6xcYRbKm39DMQjlJWNpheoNQNV83eouyoWB4-ruXeyCUkK_h6Hzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=sGFg_2dXO21FEoJyBYUZO_EMYFmeoK9iaK1ItpgLhR8dzDZE5EVBNeNpbLGXJu_mmZ8UuTcpGB6jcVSD8W-MLlOgsAuxs_c3I9cY04R6GBCvkPjHNLBL-1J3MFpU7Xd0jdXvgETdgdj1lVspfbnAhJElNhVgjE7qovE1ZEil8e5-zobempXTDFIUxOcFNvmEAl4uHtckhAc2slbGNBw0KovC_4-OFd3aikSCLnC2d-WlL_NgPRTrSAK_Z-i2GUioHG1fikrPmLpBSfettYgrTYED_WmG30ABTaYloX1pC_TG-h7SiLervmgsRTTZDK5hnFY8FeMKQocedAqmKlcljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=sGFg_2dXO21FEoJyBYUZO_EMYFmeoK9iaK1ItpgLhR8dzDZE5EVBNeNpbLGXJu_mmZ8UuTcpGB6jcVSD8W-MLlOgsAuxs_c3I9cY04R6GBCvkPjHNLBL-1J3MFpU7Xd0jdXvgETdgdj1lVspfbnAhJElNhVgjE7qovE1ZEil8e5-zobempXTDFIUxOcFNvmEAl4uHtckhAc2slbGNBw0KovC_4-OFd3aikSCLnC2d-WlL_NgPRTrSAK_Z-i2GUioHG1fikrPmLpBSfettYgrTYED_WmG30ABTaYloX1pC_TG-h7SiLervmgsRTTZDK5hnFY8FeMKQocedAqmKlcljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAQHX2HVfkHWb29VKlhU4y7LyU2eOObYwNEwRadpO7GkYbxkJxmC7ZbVPRl748i4INZlsirWsWCDzVSeRgW97yzScxwcq23u2EKHM3Wkn7aX7OjP3QCVx1zY5F8kAGKn8QLReqQ119RO_dEZXxuSButDV7gbJAe4Erq8Zo0k7xZo3ftX4cJkuX3wmNEX-pCNDMeArx6sTolyq6xaFmUVuLWaPtoxV6Vy_m9Opnlkr85J7g1VM3ubhG3v96N9YkLXf1kT3TTSA4XGaeWZ_UAq18iXAF2yotEoc87r0zAkqtKDI8x41MH9G8YKMeasQCUqP8re5V6B1Fu_3YUB2kd19g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUg-KxnRaLCo5HdGoNZkQW894xglYOL49DOfBvQOiDMHMyIAwRfi7q21I40E_VcNkRwtyTa4dyODfxlYOoB0LzETgdPVvVeq-lgK4oheMZNi-Wz6bqXywFtS0ze60bUn-DhYB21Dlum6S6TypoTy-kmzv1tSBbKP5fXqNBrIMIkJU4YCHUIaoruj9xL7AfTmYN4JJzhnmUsS5XbBBbXq3iJTnsda7j0JLjuLGJOhEDb_iRC8bx0mupksN0ZV4KZEIA5P4dGLjwwtKm7NpEKb1C5eG1LpfiYuthNYoBmqDB3-6icbfj_CV_MVwkjqgE_po19EOR1CRfHVJfaRORyTVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzXHosDHDQsXAkrhIH6Smnth63UzZzI4VuCGsY5FcR0W-OKnCyEAdzS9QM1hpbHifyos5YfJfHAQA4of7ecSFjEXHni01S1lbOks4GVeSpJ4sZHgK9bUPUuaC03rPoBWDODOnV3qoQron_ctRLQqUbmlxTD23mSOzXMMl9HExuWaNdT8_DFl-tmHwrNZYOcUakGUkhlheWSMwibLKlMq9QTsp4gfEVSX3xxZz0lURXgQF05YezI2wNkg5pY11vOW0twTXyYeJBbcl9it6MI8WCiJ3kUeVeOiZ3ntTAdxyD59zOxrRXgFlvmLxtqDhZ1Hv0dQW9GIDogj66ekKQgwUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=U0tx0OkEoQFh-qNfandVfdGCRmqFHL5QJrE_hlkdnsu9WnoGgnAH4nDBrDJp_esxTpvTgzATVXP2KUAAlNOkd6NQNONuTPaMjNUcTDagNjyMGeHcLS1Bvul29E2SAJ2cIdHZzDIoq5F2At6Z02qPKJxxKDmepDJnOTkyC9shfm1mWhWa9bRMbgq7L6R4s8tzaUeesL1eMlTcpWPJMSSm9lG6ZAkiz3X8xV5YtXEeGIDOPCl047juXLXuujYsYyFz-SQmuLYeYsr8uXVol7B1_ww8u6hJTTLUSebdaBjBOOnqEP0C5NFOmpNolvROC3Oys5MKBtWy3F6DUYM28dT3KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=U0tx0OkEoQFh-qNfandVfdGCRmqFHL5QJrE_hlkdnsu9WnoGgnAH4nDBrDJp_esxTpvTgzATVXP2KUAAlNOkd6NQNONuTPaMjNUcTDagNjyMGeHcLS1Bvul29E2SAJ2cIdHZzDIoq5F2At6Z02qPKJxxKDmepDJnOTkyC9shfm1mWhWa9bRMbgq7L6R4s8tzaUeesL1eMlTcpWPJMSSm9lG6ZAkiz3X8xV5YtXEeGIDOPCl047juXLXuujYsYyFz-SQmuLYeYsr8uXVol7B1_ww8u6hJTTLUSebdaBjBOOnqEP0C5NFOmpNolvROC3Oys5MKBtWy3F6DUYM28dT3KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu6FcXWi4CnznHRpgBsuJNrCRBRfL2TjYKOroookCTiUT_5YkrkdEw4S4WdvxOqCW2FpERnpiaoLOqbQqPCN7cA1EJryxEfoF0nMX7kDclLRQkVw4EXAKFzJJoPawgS6Fh1Z6QKsLQ1iVNCmMqNhLFrZqIOTY9HyirJTYkw6qrNf2uOu2UcClr5eeCqqjNh55shK-o1I4BEWGTfcju05DjeGPLCPQr_IGD4_Bnl4JmH_wt3EgbLnNXgE8TlZaZfcY-ilUDSuQrD9iyszDwcO85NOZ9TbVBDs4Yutb--GbH6gAxdoJcGuGcghgspwbziOrGKrI3gyu0_qi3lITLDuHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O33AQGVxnsvpo2rk63K7fVxEm66VDad4DgI5ZKDvUjBStiK_jo5EfQcsAid3_g_E_wlssyCmh52RYnvighMHwxG46xDtinCG4IEz4PI4CgkS3syWZjgbly3BxSHFZUx_4b5vJyVD_Z6OdcvdNCLuVUm63Vw26mgLQEVPbTbwBst0QaCTxpLtfxii8zsuwr2_vvEOqK_psAa3RV2OtT3F49NKNzzYfnrEPuK0dutK9WINCbKe35R8NW1pwRXcJBZKzU5iLdVoY-39zmicLWnngUtnp1PgvQiU7_K2x2ZUFMFm20aChtKHT656mhKPPOxSs2JQnadxGtGh3eUFWz09SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmgNMW9kWxUeHpWlfqJoAPEGHrhI7FouVjwakQqt-Sq9KmE0MzsxQdNRm2Kkyyp703MOjk2d440dwlDL1-CxzgaqLil8lSMZNBxeFEiwHBSyLXiN2UqjZ9HL4hwEeYugVDrQ_FVZc3tV5KIjCIHRvQOJR2dAbOkdpMy3j0AdLUXMH59meHRGjOCqa571wM0dX7TGHe-8vyVnyDKZtT8rRuFj7a6dq6qWFgAVGdgu_XhbFn7ILTrAgLdaCTz3K3gPPjoE_u4jZW2RqwVYBXspG37OQ_gGk1SNrX0x9L6pzAn8MQ1G_2EEZyK-KlaY4dQLYDiQSxGPHBjq65ZUvPOe_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeclxcF1uxinYWD3Eq73L1NvryqG1gIQftI_Vg4adUD8v_n13WD5rpGaAcCDC-xS17lfzDEAJB6i1BHQiyODN7-unVGPGnryrvhY02knDPU4lUJCtW1U8sh9UrYZIaU7I4EF1i8v6O_v369eSDrR45y0BZTR30m21If9J3ZO0Z7OFfbBSUuVK3j47QHTgAWmsewZ4gJ_dir-QZxiZ6K62FQOZ-Mnr4Sp2sErfuIv5cKRSo5iWYlgGD88cKLRJQ0FhDxAz8F1a10uwXiK9LkVRLJSGX05FFtsEcbfHBWBHtmv6zkY3etS8moxdu0c5RP-rzRttkjWom8ZSRejHyMwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Mp6pAZm0ep8g-rkCt3vf0OJOSQV4l2y0b25gXw3CPk18etfgz5V9gXgU6pgqSYAsqbInH05rTAD56n_558xbXw-dHPllt6H24TH-EwjHpj_bGjgiz-BZq755cqaRmJ91-Bw3OogthHwp103z4JJd6GCdcIiD7jljLAbj-6m2Jm4_j4TggbbJA9q1swQT0-Y7yO40MZFc4q11_i2y-YFE9pnc25JbNMKAo0q8UIOSmIZuOnoyYRLx7VSYAuG2jghyXvWOnOmQ7o6Q67INVOmKgfVMDepkVmW04wuLSpkOKGRQZeyldQjoighL7lRGSy_6uO5aozjdyitdjKpgbEqpew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Mp6pAZm0ep8g-rkCt3vf0OJOSQV4l2y0b25gXw3CPk18etfgz5V9gXgU6pgqSYAsqbInH05rTAD56n_558xbXw-dHPllt6H24TH-EwjHpj_bGjgiz-BZq755cqaRmJ91-Bw3OogthHwp103z4JJd6GCdcIiD7jljLAbj-6m2Jm4_j4TggbbJA9q1swQT0-Y7yO40MZFc4q11_i2y-YFE9pnc25JbNMKAo0q8UIOSmIZuOnoyYRLx7VSYAuG2jghyXvWOnOmQ7o6Q67INVOmKgfVMDepkVmW04wuLSpkOKGRQZeyldQjoighL7lRGSy_6uO5aozjdyitdjKpgbEqpew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJLPVQtc80WRna7awr28Ph7GICQDYQxXlLnPGhtxoXpSwvApnG-e43WL2zjvhKtfy_gZ3DZcKXC3YmlFTjY-OwXtV681cY4lfCc-n880TiQ7X3FZuguVE0hE1rZ9mtZmFqZwvyQAlZ8xNuJnrtMF1_uFE6WPOUczsupBGSFQ9X7or_ggj66PmAj2M_aGhJsXSjmpk5qczJqO7EPykjVwGAckqDyU1R5Mm1p6g0yCoAOEIESwY4Nm-RQfmDwCY6bSFKP6CIx34Zsx-lWcfUZHXVS9vRyFO7uluvugEdd2lQGOxu_1V-479LX3d2y7Gd30x1RtquBdlwK1gLGNiImCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7mJdVXjUPma44faAF8HuuZz7c_UZa4kJ3nkJuvla6oJgV5lAOk3C_STeKldG41xF4kR2jN51FGRhYHRsws-PsGfaLq_IKq-f9wNV1HlbWmOPp9B6pzssvRa19dsSKowfDOdYX4vTGaCm2A4fbPC9-dCT_9C2muuVKo9kMInW6A5BRYxZFqrQjc1cau_QVlUk6neZKXlCu_znnv-obIQNh0huxRxtAOezc3shOlj_FS9wAMCOm1kLunk_WBbfSwmXBDfPvukbpZrGokMSytEo2cyN519NvEMjuI6OpoM5-OVqulMhUxqCgUb_JSmYRgHd7xi13ScpP_hssWZcFf8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffM5iWrbwzTnB3t05wWpsk3q9Qj7e8iwlDTgkuXeVUu4Vkg87ez64epOXiN8H38WTuB4Es2sF19FS5Ixi-EGtfCEn9ZrMN01Z495-tUJgOydkahedwV7QLUpJdZQq1j3q-itGYLEWaKtHG9X7CLMoXoxw-AuktVPOth84s8_mwwwjvrGXdx03FJVfaH43P5bBAtT_Bl8g9rGZJk7Cp7r-t6rofPGxbsgVnWbylk4kT1YSSKOug00iOSWAH3LUoGWIEY9LlRQCZbtAwJ6W0Swpn39KpbvqJ6xZrCiNb1BbFISPOS_hqdsheeqQu_NKCad6_g1L_m509hUIszQoSWJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=k_ODjW7LwmdDQpK-jnDwKUkrrqIGWv5Mx5vhD0ily9_iHo_h9jjIHZUX1H7ET_uFTSOpm2iyYOKNSMBtd1Mr3fDwiSh6jB5mREe4caWPRCtX_eEuzvAX6eDjmgyNE3qDS0Oac3XiFPvYt0VaqvdGFfpCyt0LKjQoxQGvdD6JxD4aCAJ5JH5470dws_-n6VWSZJ5I4Sgt8BC2GaOLrLWX6GSerXW_h6nGAKgRYYFbtw3NB_-QwNVK5kGMZffp277yIs17KSh8O4jGL_iZJbRauHb7FYIPDwQajqxmBcXCJBwugtl7wt_CODzXQ6ZyVs9gaCGnO1BprBh_92LUX7E6YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=k_ODjW7LwmdDQpK-jnDwKUkrrqIGWv5Mx5vhD0ily9_iHo_h9jjIHZUX1H7ET_uFTSOpm2iyYOKNSMBtd1Mr3fDwiSh6jB5mREe4caWPRCtX_eEuzvAX6eDjmgyNE3qDS0Oac3XiFPvYt0VaqvdGFfpCyt0LKjQoxQGvdD6JxD4aCAJ5JH5470dws_-n6VWSZJ5I4Sgt8BC2GaOLrLWX6GSerXW_h6nGAKgRYYFbtw3NB_-QwNVK5kGMZffp277yIs17KSh8O4jGL_iZJbRauHb7FYIPDwQajqxmBcXCJBwugtl7wt_CODzXQ6ZyVs9gaCGnO1BprBh_92LUX7E6YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=bh429mmW0bp6zMLrgi38C-SJuwB5nOL1KkAJ--tZqQT96d2YUB3g1XoPei31eJqLJ01sW9m_hfMzAqHto6QHKG36C-eXFADHEjrRmwsEhHNM9YCBgk0gUrOHIAEc3LOiWASlDCOFAsBQqZnXYLptDJMNg2EjksSp4x7Oo9LicVR-Y1ZROdRnEjpvWyeQo4mTXWL5OQFqiLs0UrIbhE37qibftTxgyg-KyTMDdmyujUD_TQoS0pmpl_DRUHR6v9wYhA6RqAa3VqUjDCaZVZX9B-Oqvj3t_3IiTfklitxFVNPTwci1I01CJ4tA_gCKBqbxgZsq_7Rogojjh2NJtjV-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=bh429mmW0bp6zMLrgi38C-SJuwB5nOL1KkAJ--tZqQT96d2YUB3g1XoPei31eJqLJ01sW9m_hfMzAqHto6QHKG36C-eXFADHEjrRmwsEhHNM9YCBgk0gUrOHIAEc3LOiWASlDCOFAsBQqZnXYLptDJMNg2EjksSp4x7Oo9LicVR-Y1ZROdRnEjpvWyeQo4mTXWL5OQFqiLs0UrIbhE37qibftTxgyg-KyTMDdmyujUD_TQoS0pmpl_DRUHR6v9wYhA6RqAa3VqUjDCaZVZX9B-Oqvj3t_3IiTfklitxFVNPTwci1I01CJ4tA_gCKBqbxgZsq_7Rogojjh2NJtjV-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=UdfjfYQOGpTLOxW4ERRADYtwDqMvZknZAyNjZ8j1-xUvX0XH0eD7tNTUFgCZjXJuQgUWspUWkB9hF2V9YMJ2OqgUruN-YodraCTEQEiqSLnlPk-3iSDca0Try5fsjiR7PfyIATCfyFwxRd9b2WTqdaEQGrJJrFp6awKZLmNNyCCh8jfnpUs_fHcMGtpwb244x_l29Xt7c6eIGY0CAtQduEZ5QesX9GI6alWj8jzAy0GINNu-U-Fh70upEDH-tUK9HO36nKU0HEzqpOzrpkKqZP48nYygYBaDEQ_hIHGeTw9oyv7doVBFyJwI2Qc6fstBxcVLqnlD35NnjF5UP6O9BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=UdfjfYQOGpTLOxW4ERRADYtwDqMvZknZAyNjZ8j1-xUvX0XH0eD7tNTUFgCZjXJuQgUWspUWkB9hF2V9YMJ2OqgUruN-YodraCTEQEiqSLnlPk-3iSDca0Try5fsjiR7PfyIATCfyFwxRd9b2WTqdaEQGrJJrFp6awKZLmNNyCCh8jfnpUs_fHcMGtpwb244x_l29Xt7c6eIGY0CAtQduEZ5QesX9GI6alWj8jzAy0GINNu-U-Fh70upEDH-tUK9HO36nKU0HEzqpOzrpkKqZP48nYygYBaDEQ_hIHGeTw9oyv7doVBFyJwI2Qc6fstBxcVLqnlD35NnjF5UP6O9BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8Wc8TItdh370Blb3pXKJvxuLomKa8W6IwslX3KPkPgw2Hr5wsIUJC6GTl1oU2K1ixICol3e_5ANbnKQTdamA9Mf1DO5scPQJsEWT0C8D1-kvSNeI3YVrSPOR8GDYebflAFy-mFC6a6h_TTgg5VZ666RC6pNQvEdQVEj4oS3qcplDVsjSU7ZCvsJEA3cxBLA3yunH1idoTjr4Vqx-ENq8miKIoZwZ9GLZ7TyAdos4yd7HZqgzsoOTHYohck3Bl1wao73bl8n1uZO_GkUayXKWY3oaWcDClWokSlOGDuklxzBAN3SwDfmFpO3uqrk1qGna2r0pXHl46SVDjp8jKP1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUxl6o1hVA8i8nSrHI-kLzyea0thFxFYVrb9oONBlA0wZWYEDZJmnzTeP-EkJ3-0t2OZ09yJxwu1DEur5zlF2gJH4BzWX6o7jbN3LnBBzEqHBmEzALL_2qvLN828lrUyCIsrNmaY7viRGRBANiGmYCn72SA8Q5dena1AcqTo3Uf_wy7S1L85NiU6pzRIu09s225uWlww2mot7d5K8HzA1xHqrI0Xj_zpLYZ0-yc36p651U7NktJ3s9dbTQ21RMLCXOimt7dRroJ1ojay-x6jmep4H1YuFvVLV1PsPgm7Dv6BLOn83kLbSBYMdUbOMLpMQx3qx_FBGfUD0_k1wBTL5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QK_pw608ZrZbhe8ifFYxJrMgYHewWvsTMMAwuh7yhfHCuNIdXuL_Tf_Sd4557azJIDkajYXCohhsy97FH1EFKMFImWr2mKlCimPYisWQLJ3A_OTndCNgHi_0Swa9JI2-m4m4SHwbAARL0PXMluJPeXSmd62tBBMa0Uo3pQG3jAoPR80abCVPV1xLc8CfrqGOSpDBybt3Zg1YNu9C8J7Mw2K7mVnape_9WA8tptw9OCcXDwP_wotxfp_pfJuodocSfrmNMUAUwjdVZlhvDAvDhfMEdtLhaTkGnGt5jDcJPpopOPc6zAs1uSFyaGe1RZJnrOLdN1imBNdf1QTNUwS9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsSFT9gbmua7mnLhTF4qwr_du4K0JWq1aRRL84nkIcICf3qV_sx_yefV1gFuIXKSh795xT005vZLLeIYwa4ASFeFEDrHDhUphHfn3koyC2GEhYD5t8QwVuYTvFK0Iu_LFDV5oH8KUI8AMPqkHCU9TUlJOlrQ_l9xMki-C2qV9KJ5pb_O_ErgRzt1w1tNFSfqcTnJ4orLw1nbVYHZkFQ9XncTpwfIJo_4NNcBxONhY85hS8qMTOo79soC6DLQncWGcvoZgfAw0fV4efJXoMIXzBVvmYS9bdsKCj4Dbk4JNIUApNBZ7-pE04ZWGFBN8KfE7nE3OrmcS4JH7sbj6wpgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMmJqZe8XApCFnRiWGdnhCT7BhBhZg-u9Kgp9J0y13_UgysNawi7vjPOvmPoRqh6zsV3YiCjWwpKUkvW2xeFG5FeaCLrjdsMOJnsyKGcAz5PN0iODHe1oq9iCJNkGb3qZkL9PgeveVQlYMCM3ZaHe5qLMa6WYmLZovwQiIoir3amSQ8csz6pUa0QuWySqRYyp1zwIIAk4ZZWYpefRFf_ub7R1cvkOcAntyjzSeLoPnA7jW1CS1tgY2OJaypP4T9zo0D7HxCfjfzggDpo2CF8oE8ZTisqRqZufk5WPmPef_2P_QL5WgChBNH0oZfsDNz7p-uTLpAre0Ki9hOC8yE25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jMwgDOLUvT6TCXlEsyU2YjQGQg_OMaUzj4kX9QHFfm1Pra1oLRrQOB4ulldcvgEVlGKmNpQq0SsfVuo9rZpNh3iJEqR00iaEj0VgzO_4uZUXxFmTroqoROGY1IALnhHBcknFs37nIZxZeJJOVxRtcXK1asIawnuetgHtn2IhR8gk3tApP0H0hZYqRAROCgAIq5a0JCC86eJP2kf5U_R1MDHkMdiFkCl_7YT5ROKtUKlfkKkc-RPdollY4u_4TGXf81N-zGe-G0PAuSHgrLmbO8bw_Sc2plr278vyYXBmdTxvrkntFG-m3NeJvqeRe6Oo4FcPDcwOtrJGbtPIKe7oww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDknw2Q7riEF94OzH0kq5Otp6jtlsS4EF4dDYXtVopbA8VsjX_3ONvd9gGsoSZE4ul0FqwDq35abG9Ss7y_au7acdjyZlLzYY3JRU2QLUqnvS7_KG1bG82tajtu8G-cnZN00xD-FHJCT42ERCJ3bkyv9xqfVVN-c0-rSG3e-jniIUasnRYae2TH4yrzNt27oUwlu3lQ3zAHerS0cF32VyNFh2sXKoM1L4q5P4X3Xh16EMKxLFZNDhJnwFSX8ZG5og7qJikNRDlq2hlYNbAbxmTqe4dhjz6fYZkfDE1NROS168neijv5QC_5nwBx_QO3fjlaUg6FakpESJYVkGLmDLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLPewH9DF0f7RVSrPJN8pI5_u6Shog69mheqmgFOwO-_GBLxZWL4Q9VKOYuGlxWIQIxjHH2q0k5_iCjJcmA7LJPqcC5ulb5fKiNbnXmLj5Ml6PF3-aunOU5LcXfNDMQNlDKKjhGmFaEcRuXYqmoV2fra4L90sjd2K0jtZW9EzGxvOoCz6OdmPfOpbgCdJ3bElkk27U25hh_ncYMqwxe1jLXuensra82ypu3AJaGi27MtGV_JnzS55o9ZLko-Yhg5fPO8BFXzRhUZzek8BsrJ4Gb5kENMEuoJ9PdYx1lfhXAHIi36wSucCAsQszrEakx5-3HXalGJ9qU7rSdoqMtrig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ash18GhmutSaicVT2_Qu3F2ureKyFS4DfPaXZ8n7Ap1jh9opG4IsAonbdSHsDje2uxEXlzw8VU-2f2K-MOgkqB7BylzJeYaxc0F7OFK8zV4clQ5drYxlnJMklYntfm5E-xaEXAlnLNQ1kow9a20D1YB0cEnN8-iqm1BexTG-tVbZAZg5rQWK7-cBWovu1XtbvlQb70olCmsK8_dwzlzkTrTuB4NzGDrOjNrQ8dKEA6pIntYhl_wdKznbEcFkHBysf9f0PaVrrWTblNfX67yvEQzQhvZQ5KUewIpT0DRddyF_OEuPmP3mvG6kLACPl1EdHxKufvjsOTSC8VldvS_J4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvamrUxfcJKU6DN7vwewJvBC08gaNJgTl3u5rTxEL9prUMuE5SB0uWFfgE02DtzX1vuuKezbKJHE0UZHu41dgpj7wwPGeKryrnnSu19DxFbgNwj8HitMe-t9o4EW6CNEpw6ck-fsfWWbe_k059xZuELajpGp4K8MXn1tWqFSNFEmvWrV6gTSQ9BKGLvZVpr7p5-N4Qf9Q0b7jRm6VKhz4dgRJfI-3RmAaIyGGzqVSLedWM4HUSbh6AWKu35rpj2ACgbBR0DKskhjc-7NmofvnNoY9EQUwpNZNB1d15ml7QE27tS4qfdDXZXqWJY31VslqAmQ5LZp8lEySFv6LjqXfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxscvIm4WNxWwiM-7tllExMe01b4BijT5DWJu6aIx17qtfgWcdGHDIYGPukmBYypo7FMZt3c9Ewf9u1PNCIX-S0IZulJiaT-ymwms9to1ZL-zXRKSKqFE3wpQqVQ5Yp3ekuan9osLNH973DJTJcfpCFHtRnDQD-OiaKhNvk5je5-luVdjPlxb3igmg6T0-j23D55IVJd1aHN0kQnL0pgGi8xVUFP7M13GhmGAB1j7XbXCP2baM3gp-bxfKsSpkM2tax1q8TuYhj2u6kz-dQ-nExiBadXRb3H84mIbp7732SIv2G_v89HuHz0cR3wGmbGNPn78un0OIHSTbC7j6i2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAlVeu2VKAwg3xHDSawP2PAOV8ofLklX6uju1IE2Jz1K0UF8zKSb6uYSZDNlylmwyYykXz1xFgmBYAL-tDn_r9v4wD2Ca3v9vfZKg1KcvcDX4a8C5XQp2xilQemHj6REu2l9nxGPjztILNAaZpOZxU76l34v7beBLmrF926-8e70Bb7Jyw7ugi8FQCpyld7WIMBY_u5-qQGxCe6lLggoJbj7GWbb1iMNuAO602A2x-8yDuVtB-UK1RU8O6MfN2g0bZ5rfr-BsODP8kqhtjpq-ShRxWh90P1v9JRd3uLCKpXfqqhfSGFiVgx32ZVTrSFcn798PJ0R3uCCrZS4z23SVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_dmxLBrv_hq_n_jF0qmcl5ZkKHICp-IvkRRm5V_r2TkKDl0IFSB5pgLAYJyfKkyYB7obEN8WmKmfZB5T-DIc5g3DueXGZqbO6TrJJcIRfr624qgEK5nfzvgCLh_44xFHdRi0walESYUkNH2R84V8fM87vx9fKv4Oei3W1l0wQEcye-73NdoFpg1Om0KXtasMaG1QQBUTfOYwyvXYGS3s6rmh-q4aTYUj-EodENHbqVzKC9gjBsqxf4Oy6koeO4Tmg4wU2_V5YXYBkROcgHaLgoUkRbMZauRPU0b6_bXDFzmT7LJiWD39rOhqFOqpeDLDFpCk7qeTSYc_dI7C4fubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8FEzD4Vx8J9hmvywyNugBy_DAeWr_25uFzmrMRXJxyog_jZvxtnZJUzgaxIq9yHq3oeRAgwSRQ727vP5KvktX_StPxH2bdMFOo4mERevXf02ctJJpa7ZmSAkVRAfkIx8CKnGA9tRNbf_fWwHXmmSbFZWLRosBDdectuytRKTqumj67N570oObtPdJImTj6oCrO0MGaxC2XaFzocZCJuQFe6XAnaPYftCGcFKbmD1Oc-O3HRrwLz4Vg23Paa2apwA6xYoHt1ntzceaWtWgGozLd9vFlmkU8JzqfXZaz-EN7bF8ONRdYibyEZiLaernLHrdRQ7i0JCqQaor9mh9WWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTyHV7qynK1E7LWqsGenyuWFYAnWa8dKi1PXUa3HZxyYnNdgOApwqIlAU-xhdmOnsLxq63ZK9A6B90ZlMVs39xJ1XnPUShhL0mxSiI7yJxtekWPwzs5O83SxRqEAhQ-s13Rp-GEJSvZq9AVFAdwwiF6q_7B-CgB7g4bzNOBjRH_txesh_Rn2hrl7QiRti6aC_e7FqBbh7g-x24ie4_Bp_g7F5gGUN6amhzGgHD9LShmfNW6HjmUcZGG-WPmkQjCXhhrYXe28q6WObl8v69XgUcDzhI202PtE3ZzFTlFbcRUcho3_N6gnm29BSP7tnvhkjhpDyG4dDNuSvulnLA_X4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=AG6ZlCvdl2y0CWpLG6CqdbnG_H6h3dFsyzLUFNr0PxE3KgTVtn1BD8nz0beEsPbBRSJWm3PXJC1hgxTwrK7LC0fKch-odRWnH8dAEG8M1SMbm2ebAx6B2a4qo8ncLOhsQMvCD4LA_rSE6ULoZfKf9T4F8S3OHth3zVb5JNiJnEOQwC8DXqfybnb0fvUJwcJBdIfjZ3e7O_owqloGU_k-jZ_s9q9eoyY9Ed7qgLC3Z5xUIpps3jPUKbp_IIX0fVdbfm0pkqZz-SEnBPp1eMHr3xv6HOEQFUVruPZf8vgZJMsc5Gwh0Xj5DNAfzDUMlO_cBWuRCNzhnTlKP_yu6e767Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=AG6ZlCvdl2y0CWpLG6CqdbnG_H6h3dFsyzLUFNr0PxE3KgTVtn1BD8nz0beEsPbBRSJWm3PXJC1hgxTwrK7LC0fKch-odRWnH8dAEG8M1SMbm2ebAx6B2a4qo8ncLOhsQMvCD4LA_rSE6ULoZfKf9T4F8S3OHth3zVb5JNiJnEOQwC8DXqfybnb0fvUJwcJBdIfjZ3e7O_owqloGU_k-jZ_s9q9eoyY9Ed7qgLC3Z5xUIpps3jPUKbp_IIX0fVdbfm0pkqZz-SEnBPp1eMHr3xv6HOEQFUVruPZf8vgZJMsc5Gwh0Xj5DNAfzDUMlO_cBWuRCNzhnTlKP_yu6e767Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9k9yDPrS8sriip6ixV7abhecw4eJ6XoNRUz4M8DJ_vo1DOW8NQd5KpeC7fMLZ67G6VKVGVlTmTIqq6vCdsVE-GDQEWf_KrdkX4qFT8K6zyOHhRUE_f47qnJyvGTLAoTjUnM3hjx5O4xzcbSg7SHj2f03mgnIowbXzc6bmK82qNV1RtXTCfrwSpodAC-Ijks6AuVezgYf1jW6CF2kY6GfUxK_Hx9TxdHkZYPUg3tmDl4m1YuJkgOByQFSm5XWyR4_rTXyMKOnZdZw72dJbWBBiOXNz-SFXf90yqBtbA-i87YsKFFmBVDJIVoMH2RvWyxNZhLYwl4kK_j4rGIp_IekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=bT2EP41OVzJgToJud06Hbek6RuKaH8vn7ZYpRSZjZPIWiJmeoXxA-vEPRI_zYSFpeGJjAbcJK67Owi70__q6eJ9fTE6mZcEd0XL12ud-hJKF8vhWBlfSAkmn5-29XYR-cD6DGhfo7MpHYhJeinvOjpjueBrqFlX_pbL-VU5iMuENyO5hoFgW74jNvMxz8ghjzU2YzhmN9BglpGHTIgco8frqa7Rl6NK0MmT5Zt3UvRiyp3mQsU65HIpGtDhglR3AhrpOuO26DSqtDOIcbpEDTfzYhLGsSkBmFx8doUEn6c3mu7PhOJ1pUiQc_EErUTSaFHFzG0q7n35Wbw_uSqLRcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=bT2EP41OVzJgToJud06Hbek6RuKaH8vn7ZYpRSZjZPIWiJmeoXxA-vEPRI_zYSFpeGJjAbcJK67Owi70__q6eJ9fTE6mZcEd0XL12ud-hJKF8vhWBlfSAkmn5-29XYR-cD6DGhfo7MpHYhJeinvOjpjueBrqFlX_pbL-VU5iMuENyO5hoFgW74jNvMxz8ghjzU2YzhmN9BglpGHTIgco8frqa7Rl6NK0MmT5Zt3UvRiyp3mQsU65HIpGtDhglR3AhrpOuO26DSqtDOIcbpEDTfzYhLGsSkBmFx8doUEn6c3mu7PhOJ1pUiQc_EErUTSaFHFzG0q7n35Wbw_uSqLRcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=pFdIoBx1A8rUhDvp0XODDJAMHbPxYBrDNeCeW_RhKslWxbfgyj4VHnUQM7iUE6fvE2M7vKpGj8D6DBoigfUsGQA0Sg16Zd52WcgcOte68IBEiuYD2NUHQC0NMtX0D1FsMIDVo5o2zdTho41eqzNoPE-f0xqoTpHSOsNz5DbbIgwdgHDLTOjaEWQQbJOcW19SbmVEb9rh379cU7lE6pVL3snWVktoyoUWRTX7XJ5UF-3nu4fb94H44QdXUtm_inl7AoLVyF-PcXNz8j5lZ89aE3B81p6pLKx8shuwNWpcJK-q6m4CVuMK_R0pZRcBx6AhETlwz8cVz8N_cCL3EGfVEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=pFdIoBx1A8rUhDvp0XODDJAMHbPxYBrDNeCeW_RhKslWxbfgyj4VHnUQM7iUE6fvE2M7vKpGj8D6DBoigfUsGQA0Sg16Zd52WcgcOte68IBEiuYD2NUHQC0NMtX0D1FsMIDVo5o2zdTho41eqzNoPE-f0xqoTpHSOsNz5DbbIgwdgHDLTOjaEWQQbJOcW19SbmVEb9rh379cU7lE6pVL3snWVktoyoUWRTX7XJ5UF-3nu4fb94H44QdXUtm_inl7AoLVyF-PcXNz8j5lZ89aE3B81p6pLKx8shuwNWpcJK-q6m4CVuMK_R0pZRcBx6AhETlwz8cVz8N_cCL3EGfVEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP2W6r5Z--LBXIPyRXIjuEN6j9dgYJU4lOoYqO2-QoRUD6B_lO0LOlcjHXX5aACmShnATxr5NWJ65YJNq9qPyc-bRZhgwsJltRcLR3k35HHgFImygDvo4uLSyDcdy2_jWMG3jt_-m20uBIAMQH4fmGuTef89tPUbwj10eJk8476S7A7LUFCXjTUSElVKeH2nKw0JRGYBUMzoyMw6dF8dy0zPa09gGG8eezg3D6wkD0I4kHsvIKzgSkC5BCDPECsASDbFI9IUOzOmSW23TB60sfqkhKrwsYdEmIjMdIMxxTK9kZ2-diyY8JGCMVLMb696bojIavGg07uo8gEbjoCbKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=AQmh1SYc9QwlC6wJUuTLb0JrNcpKXds36T8wfQzjrbYAoH_QQl4IgqezU87bhUOMv7oBRMUaauJRogJ-LidOLz7usFc347QP1dK3kLPkEXd_1JTdhha4fBOJXVx-2gmUuGKyf65O9zFpSe8X1UxS_2gt_dU-J0y8-bnusnbtBcWVtoG-CeEh3ssX1HaA5-9VFTaDqQsBkPguD8LX5S7xioiFBINEzh_zO00kIqCjnJ0Qw-s-_3HxqIctgpqpO4RLh3UanOpNDHvrOVkzIyCeP2mMc85EcZGk9gJD6bcKWLEiXa_ywK734yXPXMW3jb2dRvCMWdGFEuNRxXtztcc_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=AQmh1SYc9QwlC6wJUuTLb0JrNcpKXds36T8wfQzjrbYAoH_QQl4IgqezU87bhUOMv7oBRMUaauJRogJ-LidOLz7usFc347QP1dK3kLPkEXd_1JTdhha4fBOJXVx-2gmUuGKyf65O9zFpSe8X1UxS_2gt_dU-J0y8-bnusnbtBcWVtoG-CeEh3ssX1HaA5-9VFTaDqQsBkPguD8LX5S7xioiFBINEzh_zO00kIqCjnJ0Qw-s-_3HxqIctgpqpO4RLh3UanOpNDHvrOVkzIyCeP2mMc85EcZGk9gJD6bcKWLEiXa_ywK734yXPXMW3jb2dRvCMWdGFEuNRxXtztcc_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py6mfhqnhRr_2LeyQ_3aAf5YvyMYDXri7Kkdd2ZmFGHXKxKh5BOVEL5BXjeP05emDFU1i-67Ytqy_Gt11JXldY4NVdlj9tQ9suvJo7GyL-VUqeNizIkG8hoBp8W8bA7gmPflu6sCF-no9A8_WRfQGSof4z776xf_3DQOZIK3pHY9CDqTWUBoi-6FR2Ri1m4M_SyY8EdqqaIYtLi0lMyyTRsHKfc8iA_hDIa2Euy7uOxMW0kn622ohOe54z2UtuPehsQYF7NOWm9DliGTTCOPswWLqDvthaYDuIZ9MVTEVxw-2Tz2TDaM_hWqHhi7LHlc_rEaQDfgEROsIX8Kr1Qt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMyPTFI1EerB8rxxGLFYKQV9E5BeQm8YTRcQgzYGMYHe3mt0rWYXjZk9qUYciZ_nCjFWNH5HEEI3QEGl7AKP5XweuxSwHF1GqeDMG1KbBtbFW6JHIy6GqcC7VCnBcjZUsSLlWoOKK8LiZFaE_fWah-mJzBoJH0dux5hRcAU6yxX5lWgLLLMxuv_RQVA52YHszdk48CXpiRim8mHfsMBZ0CRz9mPAcv0C4ulmsJov2QnvuFeR7zA4DIWEPlVgMFAWoB3mPEojP5nPExDFRUn2Wxp9qhuGS5zRrncQwN4Q7fEmNoiLojUmIpIpmee3h1q87Hs16ZbHQ1f-hpSfA423aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCTfmE1k7YuDHEW2uzZQtwB0m7IrfyLcoK7EBzJ2LovSrr9uX7M7XC1HCVHK9FEppSOPxh0dA9QyLF6p5lSYVJzE7JtEVnllEApSqQ6kfDVmw_2MDXuIjYXXrolUK5H1cVVx4Uh5VJa_-i0My3GSK01BphPX_f5WDnDQa0QZDg3qdyLR53yYgCHFptvoCRDkDdIb4-3DKmYWVS45U-uwJgNxMe5Ct1MpmtVuREZM1f3eRI41XwQdhb9z1ELIxUVlFElNh2b_YiPoJLBlTtkyfl7sidd5B0uEwlu5OWSyyQbFV4WC-bjTPQKM7oaOuTtQmXBePgZE-QzNwdjEK09sSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2VVsKif_5uoEtq03N3Im48cPjYOSnZrKH-ArFCS_D-H8iwEi82_GAQ7JKSrI-NZwSMoelsqxn5mCsShlTA9bLea0nu-M4I_2RouDlw6vHdazsu6ezi-WGtJyrniw7uayNn63wHFr_phJELT-IVyfoanIAoHtwYdIZ4dg29D-3fpfZVjs8ikt4elq5ac8Bk88RRYg5zI6fK9ktwq_8SkhNTq0rv8MmTkAq8Vm7-38HqZ-0Q5it-we-eHB4KkuVax6L5ZRyjcuxBwSAMsnay7VBOcqNAJNYHie2GB9pFseJLk6TUcJQznZ0_nA6dke_oNzpIj1BebEy2XJE5NOJePsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=nD6ic-4yfwPsmBltXvafOWTXPzVcijz64OCnAGJrsXFZ2mnikBxUSdLc7CXiUb4__6OhF2zeyU8fxQH4Z2ucN4uEswbrSfGZJLGL9dYN1ENoJ7W8Oh8XHfCKiKFat-4fDuhAL41P4k8niPRTuBg6OtK5NiDkXri4mqu_Yp-zwAuit-aX51NYioHGAz11WIQdMJCQkyNTMuSE4SaKng0lV8SrccdFMG1UgRQPy0ck8Kq3-jtyMNaBuoaXsTi-vKpLblFp7JtrD_fLqbORs9zVk7S2qj41ZyXXgcEqfHvDdzmNEwW1CBBZnln2VrdlU22jsY9JSDSF06cQhoCdCnlQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=nD6ic-4yfwPsmBltXvafOWTXPzVcijz64OCnAGJrsXFZ2mnikBxUSdLc7CXiUb4__6OhF2zeyU8fxQH4Z2ucN4uEswbrSfGZJLGL9dYN1ENoJ7W8Oh8XHfCKiKFat-4fDuhAL41P4k8niPRTuBg6OtK5NiDkXri4mqu_Yp-zwAuit-aX51NYioHGAz11WIQdMJCQkyNTMuSE4SaKng0lV8SrccdFMG1UgRQPy0ck8Kq3-jtyMNaBuoaXsTi-vKpLblFp7JtrD_fLqbORs9zVk7S2qj41ZyXXgcEqfHvDdzmNEwW1CBBZnln2VrdlU22jsY9JSDSF06cQhoCdCnlQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=DL4IMYi-HGlqX7iLKxjW4O2W4LqJclz56vxd__--7b3RP090wEh5pI43B3RokauRoMnrXsTG_Z3Kn-yxILVmiFfNABr2erH66XUrPLCgGV6NAIvY852BdtFPDJ9_pDgJxWFhnKUn8hcoi1-x7Z3V1JcfT0vbso0YmKNN1GYIZXpkTm975eMMwfLtrR_bViSy3-Oi5B_KXdYK4R6GAxShk5WWpyDYDw44oDbW5t7MX8AQxrj7D7TyozaPiF49AsG0qh1upSYSkb5xexYqG8LNpG8S_dk9zGmDNMEkD4eGzul2fgZqduv1fwmmhr02gYromtd5QVK1ryYZIshC4v0ibQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=DL4IMYi-HGlqX7iLKxjW4O2W4LqJclz56vxd__--7b3RP090wEh5pI43B3RokauRoMnrXsTG_Z3Kn-yxILVmiFfNABr2erH66XUrPLCgGV6NAIvY852BdtFPDJ9_pDgJxWFhnKUn8hcoi1-x7Z3V1JcfT0vbso0YmKNN1GYIZXpkTm975eMMwfLtrR_bViSy3-Oi5B_KXdYK4R6GAxShk5WWpyDYDw44oDbW5t7MX8AQxrj7D7TyozaPiF49AsG0qh1upSYSkb5xexYqG8LNpG8S_dk9zGmDNMEkD4eGzul2fgZqduv1fwmmhr02gYromtd5QVK1ryYZIshC4v0ibQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=LrZOgLm8qGekloVGGmvAk67JjX5TIwB3EKrgQET1apxFybhTbU4XwwcxICHbpAMVpDJUMosnp-NsVCoMskbFEu-sTsQvK30IOQ1UKtErVLv6ZQNUSfMw9wGWpubQaezNjNjIkm5iRJNLvnGeZTppOPS1oJVa9Uj_01VAOLPjUc2SpfIABQaOYaSQbtQ5ZhgwvVMSKqVTBrVQr7Vzsb-V0ojkmbjpei7suNpU1U6KHwu0ALQXXjR6sBmNBmsxG1sfKpz2QCWYZPFWk8Bj5kBDs1XTOy32wKyA94NXAx3LOr_tf2N9GzIlrbDO6vVbpGgFWlt-4l8nyzZkoOXCHJoiQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=LrZOgLm8qGekloVGGmvAk67JjX5TIwB3EKrgQET1apxFybhTbU4XwwcxICHbpAMVpDJUMosnp-NsVCoMskbFEu-sTsQvK30IOQ1UKtErVLv6ZQNUSfMw9wGWpubQaezNjNjIkm5iRJNLvnGeZTppOPS1oJVa9Uj_01VAOLPjUc2SpfIABQaOYaSQbtQ5ZhgwvVMSKqVTBrVQr7Vzsb-V0ojkmbjpei7suNpU1U6KHwu0ALQXXjR6sBmNBmsxG1sfKpz2QCWYZPFWk8Bj5kBDs1XTOy32wKyA94NXAx3LOr_tf2N9GzIlrbDO6vVbpGgFWlt-4l8nyzZkoOXCHJoiQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=rribBziE3nrgObAZE4rGNtg6nAb2FzUHGjJeYy7A10PE01kmk25qsgYjsKG3H76HHTIcw3n1BsruO8ZyyLpDe-tWrQdyPfAcFD-KrnTwYz9Yo_JEuyElqlgmp8kt8Xgp9JKLduK1l92xHN92nAZRhuSTrEszHtNrRq61E4DPj4NPCvURjH1LEZSWmtIBKV4-gg_UTg2LAvLGs27AtjCgbt5FOyZoWO_YZ1dKWQaEc1nLrL-IJUGHTTq0ixzJJBmv1cTJRQYm5zH4WQd03z_aK1zAtogo1KcUc8d35J_ZN9m4j0w0FKJ_Vg_zvy6992iIkjNCwGU4AEpAqUO4R4BxEna7KvVjR5h4TDJ3R0WOmNCMArlJFUboS47njZ13yvSA6px1co4Q8TdTtINXw5oydPUfXVYVEBH6Qw1UUIoLHqD6Wk2IBSfgMzJfzE2EZJRrSOcrHczW0Rz_yz7J-cJ89Gowf-0iLS-CwM_YkYQXBhOqCJesTgXBQ40cFwskMUpmr-G5Wxt1iRZizb7QJwhlUGSkUZHYRBWyC9RJ0N9xQISpKAv7CjTZbXd8l9MrDFZxjM-3NHc9Frguzfy43jZuX-kKOmikLwlkJnF4YzbDmpVcYxhKBeDJJysBiIh1JUVtVVerrQh3_LTY1SOM6hC8TVb-brcaQDYGoUVEaRBC_Kk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=rribBziE3nrgObAZE4rGNtg6nAb2FzUHGjJeYy7A10PE01kmk25qsgYjsKG3H76HHTIcw3n1BsruO8ZyyLpDe-tWrQdyPfAcFD-KrnTwYz9Yo_JEuyElqlgmp8kt8Xgp9JKLduK1l92xHN92nAZRhuSTrEszHtNrRq61E4DPj4NPCvURjH1LEZSWmtIBKV4-gg_UTg2LAvLGs27AtjCgbt5FOyZoWO_YZ1dKWQaEc1nLrL-IJUGHTTq0ixzJJBmv1cTJRQYm5zH4WQd03z_aK1zAtogo1KcUc8d35J_ZN9m4j0w0FKJ_Vg_zvy6992iIkjNCwGU4AEpAqUO4R4BxEna7KvVjR5h4TDJ3R0WOmNCMArlJFUboS47njZ13yvSA6px1co4Q8TdTtINXw5oydPUfXVYVEBH6Qw1UUIoLHqD6Wk2IBSfgMzJfzE2EZJRrSOcrHczW0Rz_yz7J-cJ89Gowf-0iLS-CwM_YkYQXBhOqCJesTgXBQ40cFwskMUpmr-G5Wxt1iRZizb7QJwhlUGSkUZHYRBWyC9RJ0N9xQISpKAv7CjTZbXd8l9MrDFZxjM-3NHc9Frguzfy43jZuX-kKOmikLwlkJnF4YzbDmpVcYxhKBeDJJysBiIh1JUVtVVerrQh3_LTY1SOM6hC8TVb-brcaQDYGoUVEaRBC_Kk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=kpmoAeA53zs14RBZE7hQWAJr5O0_ZeyJrR-WoisFvUgA-CXFC6m3P_EitMTZBuGJDfv0E0Eg_D4nKSYePKmuY7dMxNLAbUA8r1qoXAaPEW3BWOlmiDs1ZpSzgBHyqvn7gyqEsIT5nGnaOOXOhAUSFHc1wbilwrikw77CN4ew31QnWpAky6PWoT4J_tWYLyTIFlp-Bzf8CmxBeOtxy-DxCkwujmvTohlyL6JnGCH06muBdi6KVybXvwQ4QzFNT7r9SxKVWmyHDYvrc1W0IcDAEPGao74dE4Yhif-0yLVtNDDwlf9MMc04m7hunmnJ96kYxmik-ppAXGFE6JZZE_Q0Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=kpmoAeA53zs14RBZE7hQWAJr5O0_ZeyJrR-WoisFvUgA-CXFC6m3P_EitMTZBuGJDfv0E0Eg_D4nKSYePKmuY7dMxNLAbUA8r1qoXAaPEW3BWOlmiDs1ZpSzgBHyqvn7gyqEsIT5nGnaOOXOhAUSFHc1wbilwrikw77CN4ew31QnWpAky6PWoT4J_tWYLyTIFlp-Bzf8CmxBeOtxy-DxCkwujmvTohlyL6JnGCH06muBdi6KVybXvwQ4QzFNT7r9SxKVWmyHDYvrc1W0IcDAEPGao74dE4Yhif-0yLVtNDDwlf9MMc04m7hunmnJ96kYxmik-ppAXGFE6JZZE_Q0Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=panoHlb_tyMPoOgNmW2xzD7JFMC356-VgsQVPYF26l19_PX3R4B2L5Xd9hzoz7BPRvJ2qNAhps8DDFk6po55y7qjiR_-EPGSrr3q5FMchHQ6GxzU1XqiXI8RgSTYdNCeRsb-kFlS90aSLIllcvveB9N9N7NOfx8trxOlEYAba6InrpV3FmpmlM9cAGyC6Yz1yDGxW12hjMy5ttu7gsb9fNpFApKXq2VmA8kffuBvA0gTShf66OKU-TX91tds5rVwGjGoIugKgDU7h_Xoa44dCWO0Zf70_EezuCmkU0oQwWzl8ldfv9cGwk4uHY5MXjLud7qRcrBA-H0X2PLsww2esA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=panoHlb_tyMPoOgNmW2xzD7JFMC356-VgsQVPYF26l19_PX3R4B2L5Xd9hzoz7BPRvJ2qNAhps8DDFk6po55y7qjiR_-EPGSrr3q5FMchHQ6GxzU1XqiXI8RgSTYdNCeRsb-kFlS90aSLIllcvveB9N9N7NOfx8trxOlEYAba6InrpV3FmpmlM9cAGyC6Yz1yDGxW12hjMy5ttu7gsb9fNpFApKXq2VmA8kffuBvA0gTShf66OKU-TX91tds5rVwGjGoIugKgDU7h_Xoa44dCWO0Zf70_EezuCmkU0oQwWzl8ldfv9cGwk4uHY5MXjLud7qRcrBA-H0X2PLsww2esA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPtt6fgFpT2GYSWNJC3PfCUPzninj_wQGujIjxRroTyU_I2cwvKtcxVPLRzXAX56N6N0ifV6E82GcBW-e7PxIqc-IRuRqUkxl1OGBFAHazQWFO0KrCtpo_eHcOFWempYtgQz1Q0r3gMJsXKyYiY8eUnpBwdhK5doHxK8I5_y4qbnGyPhisqrTsGCKa9w9zQIOuE5sBUzHo7x0n6vSKFAfzz1imwMVgT3zONsgCfxMkUgefzoavcyJWBaxS7B0CHNWJPlZYMRXxBazswrPy7f6xHjimdRBwXgndMK-sj0prSEPnt98jSKA3InAcza-agHraCvnX4RP7H13Vntg-_ghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=YNRvYkZ9Qyj_u8s85-liA8t9fCo3vo9kBwC0E_LnPhTIoueHRJqyj5ek_Yn5L8odSS7Tz0WdWFjek662nhY_WFXpDSW-iSVWg_Mcg3goSD2Ac6nIvVBWMWKKhO5TUrvb1tkEw2qwWdnxi1bmwtZVo1yMipnhwqW8mEEDM4ErLoLFkB5Hd3tBOP48i6zWcsdFXON3J8f1MmGaLGHMIRp3C6JNGrapZx7uaXtz5ReaVZSX2pU-n_eilCrYWLksx47z6ERYoqJXbTuB7_KWntjrQQiYJ1kSK-rnsv8xgEM5o45aisLlLh8MZIsFIkR3SSih2oEUlTHPA9bO2wiqda19VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=YNRvYkZ9Qyj_u8s85-liA8t9fCo3vo9kBwC0E_LnPhTIoueHRJqyj5ek_Yn5L8odSS7Tz0WdWFjek662nhY_WFXpDSW-iSVWg_Mcg3goSD2Ac6nIvVBWMWKKhO5TUrvb1tkEw2qwWdnxi1bmwtZVo1yMipnhwqW8mEEDM4ErLoLFkB5Hd3tBOP48i6zWcsdFXON3J8f1MmGaLGHMIRp3C6JNGrapZx7uaXtz5ReaVZSX2pU-n_eilCrYWLksx47z6ERYoqJXbTuB7_KWntjrQQiYJ1kSK-rnsv8xgEM5o45aisLlLh8MZIsFIkR3SSih2oEUlTHPA9bO2wiqda19VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
