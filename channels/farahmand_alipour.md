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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 11:31:22</div>
<hr>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Sn8wEoQiLmbQ4-W7jkNFFId3c39vwB2620el9J3azJXUZ6332ZPLtol2vrbmNfy-CiaoGSIigP0hiWQsMutT-8wO_gI2Fvs5ta81YEddTcg8Y_S5ekYS_7zm-TOIpUWTYfKxyn-HSiHeFWkosg8LDHIar44mp9Vtl7YB4VEj89cpEONrG4hWCrS0LGpUN-q5gQVRxsmehgNQH1LErtPgUpEaxQZ9AA4UcrK9nKjjXCfK82FkZ35lSp4pRAbks5hPsD-yUanRsMzaXkn3NabcWu_QG-AeL2r-TQhkBQF9HGRchItTNU6gjYG6V-gwhesGSx4K1RRiKmKGsNmu_hsVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IotlhauxxamIoDVWB22596GsxhSImjjoU_l-RM3CIcp0hXl4G0fOXuVibEkxZIx2BZ3mqc6SOxR-iwulyUDdr9hlT8tNAGFOy4zwZxBuBsrfofLanDNYJxHgzMdi87aIPH3UEWDbmpJ0G075KHvCuGJnoi3k9WVlLN1y3K9dmvOpPWMvlQJt9EEtsagGgdeQJ5rY-womaGpExALUJnuXkEBji9W1a2_UVWLil_PcUrc-0Mt1gc4nJhVtF7iYrQx6Sdb0ntH6iKm3gT7cR_6NNjOOwivUuqMgb-nsEzDgW_p1wGaqx_6IU3IkfCEQ8-L0yys12NA7EHrx-hGYWYCH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh1gIiMO26gKmECsuBu-x7k7PHtOiBsdlmJvQDDWm9Iu4VRDM9H8ysl3rF1ztO0H9CVJQTQJh_gixp93GE6iF9sB08ueqJrv3RxESsmRam-I2-HbdJS1IJIrGrNP8_7obG_MfOEJ2xHxXXu9zQlWev68zWhM3xKr8wUKhZVLxYeEWBfzBhbK7g6LR7GH6jBVtHvZrsMwEeOrEV6FSqYs3gvFK_i9lC0h9QtHkxXPZaYPqzpN4v-aZ1e4KQzvDn02L5A3XfT-1EOpWeaDaC5epo6pbtaeV0e7OZQNvlhitP0LsH4oH2Vw3F-p4NALcS3byWd5oN9vThs7ng8bR0ESgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvHwqgI2ExWT3XuUSw163hbtaLrav_ZRLgUnBBkSckizl2iotJ3uGW8JdizVmP95Dlt-9wN7lZx-GxA0roUBIk4trkNLCcf27_xYee3NIzlB28H08OGwJlf5JJe_4ZIJSvunHLusgqlKwJap83XQmFRPoKuercvuMz8zau-qSsmsMe_mqIk8j07FupptfA1t1jJgUCNQI1Xa1ffiWc3NP4Omhv6KmW58gea19p78DndxXpGl_uUR3HRLrfUf2rrNBtY0WjT2NwKb3_WsxwH1gffr5XUcmRHyuqsnv8JaMQPH66d4HaRs6fahIt3AXf6PESxgMT1ivJVUbLZilcMp4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kP1MUlDDjAP-c4E6q4mLBd_Pst9kOdt6e2QzrbHXKI_Em4LQ8GkNgOLYZm15CgI3Xdy3aj4hQC-ICKXlskXTo31Q6mMur7t5nR5GW2h5aK1XHUbgLA6PIrop76z2oggfQNMKfr7BOKAfQBMY-PLElSDHkvdmELJ8SE-8Y5NUOliczIimjm7UNGrApzJC3e5HFS4xQC5tNAR4FTEcvBPapPKKctakJNzvphO64S2N2BAUiR_gAQNcL6MNpv7oGhz5Gi9Y7JmRhSAIzUCOn3KzCU3uDDW1EcCqFvkJkA4gf06uIkgyH2tSKNOx54lsBrRV2WtVjLsn5uttTiiKczpHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spomz7bjOu2I5arbglW-35Spx7_PdN3RWptxCq-doJKbFk-6lWPrCZFJn_pYKqr_7UqjGUnpoHTbhGiH8CvaSORrszeWYO24nk2mbK9LU6fyyT12tzRb0PrRPHZZKTbM2bQdxa6wkUB_mK7zZNRuOc68BTROshOtec272ZdhtlBpQas41pZJYVP1V7ozgWZn9jQGVPum47q58-Ho3QVsLc2sa5mz8g2rfYET_ac3A16C-bVldyCEdgeWAclSuZnTLhg1OegTQh0mz-hYlnyUyeTG1LIJ7TBpGBO_bMnGA3peyXFdhT4tURIHzXlpI89bqRNiKVRNGcmdP0YhKTqSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Z0HeL6G2_i4reMfSotOtIFcFarf3AnYy9oIXgkQISyiZIFfEfjqoPtsdp_W3KRXsk3qCmTpdQUt0aI17gu0b0LcCWw6wyhMbSeqLQyp1_DHPveZx9xicfvEwYD3Ta3gMFcp_H6XP3B2C8hxynpblYVtwmgg4_EQ2IKPegaEcjat6jNM50XEp7ROsMs4rY7aCSgdYYc7bGRb81X9KfEIM4KIV1GmKUT5f2ZEyqYNSAlhaz_2TLEexralZ8FhFYx08W1n-Fsa_rCMcCjYyAGLH_Az1xHRhGw_YBsyXxIC8zfDUV0iHLURxHuOvCoa0G5JxnbQXOlht5_FIHaE70bXwtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Z0HeL6G2_i4reMfSotOtIFcFarf3AnYy9oIXgkQISyiZIFfEfjqoPtsdp_W3KRXsk3qCmTpdQUt0aI17gu0b0LcCWw6wyhMbSeqLQyp1_DHPveZx9xicfvEwYD3Ta3gMFcp_H6XP3B2C8hxynpblYVtwmgg4_EQ2IKPegaEcjat6jNM50XEp7ROsMs4rY7aCSgdYYc7bGRb81X9KfEIM4KIV1GmKUT5f2ZEyqYNSAlhaz_2TLEexralZ8FhFYx08W1n-Fsa_rCMcCjYyAGLH_Az1xHRhGw_YBsyXxIC8zfDUV0iHLURxHuOvCoa0G5JxnbQXOlht5_FIHaE70bXwtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=CGevgSG5bukOS0klFuX2LuI4cUUSeJ6mYMHmRtW-IVeuKNMqPP8qrwLCJayOrxFSObbP970IlPzbzvAh9vUPKIjU0LcFoFfnp9WhmnDjka9iWuKZuyXCVRYOezuwadR1g_Odye5nCpfEUOuuLoizGA04fPGHwV5pLuVHvb5BqjRrcZFNBmt9e8ep3EtZV7_VUCqElhjFkUld7WBO91JV-Oz6nebuMDKxY7RvMOIjJcNMajdEBdqw48wzxhoI3DELAkSifh81IZ7tIPJ0sSnzLuN1Ed85lSpkiCMzBF3AL3KPCnWPY28ry6SCbX_lHYGq8s5puOvdViDLcJC5C6I8rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=CGevgSG5bukOS0klFuX2LuI4cUUSeJ6mYMHmRtW-IVeuKNMqPP8qrwLCJayOrxFSObbP970IlPzbzvAh9vUPKIjU0LcFoFfnp9WhmnDjka9iWuKZuyXCVRYOezuwadR1g_Odye5nCpfEUOuuLoizGA04fPGHwV5pLuVHvb5BqjRrcZFNBmt9e8ep3EtZV7_VUCqElhjFkUld7WBO91JV-Oz6nebuMDKxY7RvMOIjJcNMajdEBdqw48wzxhoI3DELAkSifh81IZ7tIPJ0sSnzLuN1Ed85lSpkiCMzBF3AL3KPCnWPY28ry6SCbX_lHYGq8s5puOvdViDLcJC5C6I8rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it-RthdAPGrdl_tGeYR8Zfym_3-z4QI6yUph-PoagL41RKheyzeYATd9rD6O9iu5RQQRFMrUNDTXXg5c97QZ8s9XA_aOCQq9e75Kovdj62pD3vs3-XUQ7m-hHmwz6oCsOLvvuhOqab9b5QXi70rA3_PythfEZUl9QaH_K-uAUH9VzK8lIJKBt5oS3FtJgqaIPsTyWGuxREy-iYePjXMRoufe2Aim_8ssXvCLmY5nW3TeYj22Trq5CdCCD41YDcYl6yFlg_IhoKpPXEHLpghKTwSfgLAkrzhkqPp5qImCDhYFjiL6WM8kgPJLHxU3_0VEk-3rfSXMvbdfH-P6g-ptdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2uB8-PG7PyTsnw4XXYiPgV-ACtszVe1DmuX_ahu1YuXZ1pRZ0GaRTPnZgzLl1PFBHShAuEGxETZNvU6qTh3Ivx2059GkhKNfM0YMJB2ZLBSOZ-4ZHe0kjQovOFv4-zU9eeWrA_1m60g4vXfGYU5f3ZBZsFI4YukKk7LDOQurwEnR03QQVhBfZwDPlJFgivyNHz_VUxPbNZFw_0xQUFfvDPtMBJuKvtpOvisAJ4iThEjzKCehFUZGIPzhFweTif6N6kL0r1644pAKVftCWG0Asyx_waw9ZHtpTQl0G3HuE5NXjD9FTDan0QoF2zO_9uluK8Ytrhl353cyzPjgok8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=AYYjd4k82XZGTkK3MrsGg-lkHdy9hCtog4DYp017IUGcdm8WpFfsGDC4Q187ls-D7Wu7RD5jMr_iRKudmscPS8VMmavMdd1yqxe8JI4YXJscAmlpuuBdpIIvdYbvcuXiNheXPszKGAA4LqE4AsT5VnEZo45qtqol9y7a1d9xr6aHb4JfMKP-ivZurZ_DTXELQRwlZIh3oUpBiNxfqXEceLIF6jcNpydWCAOk816o0Nibu0dXkvMFenF-aOQGDXQhkmG80ui3GHgGAS4nshotRdqX9ywA835puk5M0zO91U0DVAH7q-v6U-BXRW8cVVDADcmCbJ5cEWJqPsc4FBdWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=AYYjd4k82XZGTkK3MrsGg-lkHdy9hCtog4DYp017IUGcdm8WpFfsGDC4Q187ls-D7Wu7RD5jMr_iRKudmscPS8VMmavMdd1yqxe8JI4YXJscAmlpuuBdpIIvdYbvcuXiNheXPszKGAA4LqE4AsT5VnEZo45qtqol9y7a1d9xr6aHb4JfMKP-ivZurZ_DTXELQRwlZIh3oUpBiNxfqXEceLIF6jcNpydWCAOk816o0Nibu0dXkvMFenF-aOQGDXQhkmG80ui3GHgGAS4nshotRdqX9ywA835puk5M0zO91U0DVAH7q-v6U-BXRW8cVVDADcmCbJ5cEWJqPsc4FBdWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugjd5jhK7RwlB1CYo_zEBJAnSyxr5MlV98fRkjSbkZqRFC58zbY36cxBoaGXslVnTG2X5irBJ_Go1CMqwJR50U4_SugaiqaiQbA5gxIg-j9jMj71mDlFa-qm98upE036JCEQL1pScAPuyeaoTsaSCOOORlLfN19e0lNwaawImb-HiD1cgqmS3fBsck7SMRz4kHjZMqOsSmroj3SoZskBSvre5NfCsmwIGrw5pwowMcFnIgRJBZqBqLYLAFja6plo6eFPCsBUPgspZxwM0ZyDreDGDxKfX8dyQotht90hKy2c3FG0GrOqd5yVi2_qKM1akbyqmJOb3T3n0V2LsvNeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsRAIFDKmhhy0ZedggxlxEY-DMwX0QuvVTcNxnx3Dth7pK7eJ5LwAg7T5unqTqtpLQ6hHyd5BnK4FCDPlZejdzn75pufolTkzKZ0IXCG8TXtJe80ovxDfr0IMF18wEFegQp-SuDQD9oD5H9zG_Nz4GrCxz-y-NtF_U69qU10RzX5idADglAN1l4kW1b464gBVhyuDr8u_wAiB8POxbkWi1EJsKEdc-caABHIYPK-8E1doR0gjQoGocdmHTklflIIif2vBoZY-8Aemw8RLbaoVFEaJd9_13s5Q6x3CizELVTFeF-eJ-GsxMnC-wre7qLdl05N57ZuAjweR_39zG9hzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WljizC3DvVzlZll3QR3k5ffVx7JJRKmqSM2ZZQfZmZ_t6PcXxJp_YBjpUKk4M9A7h1lnikPuc4FYnsebmLrCRyjxiAmTo4tErysAXnDhmm-zw7I5EgGQYTtrXLxmyJODwyXp4c6PgOQzfa9gGY6H-OYcBqI51hDLxr-JguZow9BdSj_nc8UDER1KDuBi77iaF_Mtu40hfoL4-o7FO8G9hpKKMcmabDRqbVVHBFNcvfcaAzaDgncJWeeCZQlakaqaPA6OwmXHcD8vMT_KxO0DGA4KgussJV_G-TyiqTTAmtj4WluqnDaxKiR83nZgqO9he6tPAfjSN4DpjOAqdX_Cpgkq66-tlMkyGSSuE6pbTl6D8u5sRgGFsmQvMULDlTzEWFC6w9wikYSF3JJxRBO4Z_n9S-zQYESuHZYM3MI2HyLKPZ-H1yI_qfwHGlgO7SoeFzZMk1-42uKwXSWDZikw5MkQgoDatf9ymWIVeGIuvxwtpCXcRJG1gPsn5LtxJWmCbQOAd7W58eTb2YYC02MBxPEcfzN7rMU37IZrnhMmPd0TDBu8-JgjjvEo6InxhFrTS1rSshLWKiK8oOZS9m0lURRq7JuzzCE8gT8nv8WEm7alkYdkmR2qQv7N79MHDCqprckWXuluCRrE6-iXAPN8qeSt-gchwya2o8QWi0b6_cI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WljizC3DvVzlZll3QR3k5ffVx7JJRKmqSM2ZZQfZmZ_t6PcXxJp_YBjpUKk4M9A7h1lnikPuc4FYnsebmLrCRyjxiAmTo4tErysAXnDhmm-zw7I5EgGQYTtrXLxmyJODwyXp4c6PgOQzfa9gGY6H-OYcBqI51hDLxr-JguZow9BdSj_nc8UDER1KDuBi77iaF_Mtu40hfoL4-o7FO8G9hpKKMcmabDRqbVVHBFNcvfcaAzaDgncJWeeCZQlakaqaPA6OwmXHcD8vMT_KxO0DGA4KgussJV_G-TyiqTTAmtj4WluqnDaxKiR83nZgqO9he6tPAfjSN4DpjOAqdX_Cpgkq66-tlMkyGSSuE6pbTl6D8u5sRgGFsmQvMULDlTzEWFC6w9wikYSF3JJxRBO4Z_n9S-zQYESuHZYM3MI2HyLKPZ-H1yI_qfwHGlgO7SoeFzZMk1-42uKwXSWDZikw5MkQgoDatf9ymWIVeGIuvxwtpCXcRJG1gPsn5LtxJWmCbQOAd7W58eTb2YYC02MBxPEcfzN7rMU37IZrnhMmPd0TDBu8-JgjjvEo6InxhFrTS1rSshLWKiK8oOZS9m0lURRq7JuzzCE8gT8nv8WEm7alkYdkmR2qQv7N79MHDCqprckWXuluCRrE6-iXAPN8qeSt-gchwya2o8QWi0b6_cI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToCtddJjJMvRaV9CWPmoApWEh1HCadugx3lrAv72Y3RyoPH3Fva1qGapgzh1xGgBRohhtkHcRiHwoXAUMEkdt5C8OJJZ-e-LVQzp67vEYGmrZVz_nSr2syigpJRM4Apu4r10_qk28bdsNsMlZfEzYtzd-SQx4v5o5_4s9e0lPTYCTj-cZQ6PgX4OJRzcVH2RfVwTcXr-jEICTs5sfVJcJnEMARtO5avvXNvIxaKkaBrhJXTbaVpeVisvu0RIku7svraWSlGIEIiZ9Qpiv147IcoNMO_ibkd4TumnBesOe_6Dxlhe1ekSIvkERNi2B8EQmTOmF8OwEFW1HLuLwAKSg30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToCtddJjJMvRaV9CWPmoApWEh1HCadugx3lrAv72Y3RyoPH3Fva1qGapgzh1xGgBRohhtkHcRiHwoXAUMEkdt5C8OJJZ-e-LVQzp67vEYGmrZVz_nSr2syigpJRM4Apu4r10_qk28bdsNsMlZfEzYtzd-SQx4v5o5_4s9e0lPTYCTj-cZQ6PgX4OJRzcVH2RfVwTcXr-jEICTs5sfVJcJnEMARtO5avvXNvIxaKkaBrhJXTbaVpeVisvu0RIku7svraWSlGIEIiZ9Qpiv147IcoNMO_ibkd4TumnBesOe_6Dxlhe1ekSIvkERNi2B8EQmTOmF8OwEFW1HLuLwAKSg30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUtP6oJm-WqVxE0s0OXZPgSdIcvJsr8YhpM1oKp9-s70qZf3W1gPWmCFYRZNu4VksKZTKITYQh_k_9K0G55Ibi4pZyZvZC3DBxzVfuuf0CEFSzoZfMaFXzzSE5IX5hxq6DUfVtZDtfzBUH8W6_jGwkWAhS3rJD7kzZSXEQIQiVALLT6rmmosYjuuV90IgQP8Je-z6jiL3btf-_iocuwAn6K-bdFFngH2vcUCpYII9Zf2Vw2sfFoqeluP-11NVV0cbh2sbtZMjyU89JXll6cna0upyWXKaSlXvEybLk2NpQ6nWrYyFFRfu8zc8shCeaXvp3dzjJ3q1zfUgWfU1dCTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZV5mprrmbYv15Q6DaGu_Yg-lIA9MTHIbYh7kY0mMOBZh0LP-OyIC0n2SzULFvnCndgic44Xv8msnr3xM8QYFoHWi7aJqQahgRYzef419H1AH8yQXXdcAumczRsDlZjRKXMS5lNsWoRX8Ne4HGIVmX8p6ZYhFHd0klIT4cFMB5cBMqBhqAzQDCcCvOkn4rLnc1SBQHN33NWJ7-llPWtbPL2tEWSzGrkJS0wSmVQuqLYhKWqegu13DY3TwLo6zqZz3wGo5AhIzOfSvqDKcnF7y0oNG60HrwC4S6upaDrxdf-MVFU2PdTjRUHCA3SlEK10dwgsDffW8IbR5YAsVX7X8qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JztU_xTlUVt_fpbRI0-Wog6cPnMHMkPyMPImguY5zl-q_yiPiI_n0P-7n5paCoabOMMXzeSVVYVzFEkuXS64zsL9fLczawMPDRseFsrX3TqfyzC5wl5v2l4xed0em-WGYOfTp53j6aq5VhNsITSzUdo1n-3IwLS65r53S9u_BURLYb6moN8Mks-fR6o1QL7BYioNgwCI7yts4fu7enbQzhHZ35bpVXUDZIrjuCVq9Gctimop7hzZpT812Mhv9eej0QPRBIviIlfXB15vYHTs2Q5NOMrUm1cEMFBkcH6daXzG-XrOM2IlEYP5Z8zkcaUNBS4UBUJF4p3OMG4cyHUTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrAIuIHJ1rpmgH9nnLV-MWaRY-MF2Tf3tS83a_XR8u8M6ZSRyGf_jCxnd90g2gjJ_KwJ-swnWgsHEawwfSMyWYZKRTy475M4pHYQKLPNkFGb4i7tE1kSgeo1vTcxWr2STDZBy9S_287DNAP1yOE-GQ9hLQ0Iev1X3gvSvSV3pkuDvvuRaXEzULWoB5MbjivoknSoQ5LCGmiz1FOL0VUshMsVpVep4_RWsqmt2bLMYVXsOhk_fvgrwnGBhDDwrd3Hzhl3jr1ZyjayLZu3jQ3Vm7h58TrPwhxeDSiA4BvtmBlWvqE0M0BLS-8rLCsh51WxSNFJOv0v7sgwnqeoUYsEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yoxtfii8wIqr6Mt5hpI-HK63nYZWB0TuBnKiBE2d-c5lx_pP7tFgSY_WY-ipSif2MxgfYGoKF4rv1sSmL-w0ayY3PJO9PduUz3P_vy_FJ6nF0lU1bO_LPcxhVaoriFYkYO6JxYPkzaLa22HgPcosLXcSpJDEYS1Qo9kuJ-TygKA5ByHKTXyvk1caNVxSux-nazU75iUNPMAzYOxAUhifpo0P1iFwfHLjgJFArp5WTqFkq0E8gV6-JkP5fI5tdznj6ej-WQxSlLMG858sxV8XwqfEQbO_IR5sVMusI3Vp7msgySqXQdVVhNCPYH4Fj9676x2XpHHc09buWUATO6bbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=H_vywW_m1VBpDzU_YfDdI5ExBlCcCzwW03nFrl7QyieLUXlbd6F7DVWUMkyS645dobxSTErpQ60VNhLrW5VXzW9nPDehlIPptX8DDN6uTVYOKRzDLZHk-k4PVErTJiKSc6fLxfjjhqt9xXivV6PXh9j4FUDt9S9Jz2KYnvRWo2Qr2OePUQM3iOwQ3pDKbDXbgMJoNW5HahxAnoJSUy_YujTdmtGcqXUW8h0Dc81U6-_GpHVK3c-LcSYjBdSeWFtjEzf-YwVgST6N61ggrfIncw-rOmxVpsVSKviBCZ_U0TBoY5O0Cw0ME_JgPjnDivulrIy2JGMKQ_6NAk4l7iaO-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=H_vywW_m1VBpDzU_YfDdI5ExBlCcCzwW03nFrl7QyieLUXlbd6F7DVWUMkyS645dobxSTErpQ60VNhLrW5VXzW9nPDehlIPptX8DDN6uTVYOKRzDLZHk-k4PVErTJiKSc6fLxfjjhqt9xXivV6PXh9j4FUDt9S9Jz2KYnvRWo2Qr2OePUQM3iOwQ3pDKbDXbgMJoNW5HahxAnoJSUy_YujTdmtGcqXUW8h0Dc81U6-_GpHVK3c-LcSYjBdSeWFtjEzf-YwVgST6N61ggrfIncw-rOmxVpsVSKviBCZ_U0TBoY5O0Cw0ME_JgPjnDivulrIy2JGMKQ_6NAk4l7iaO-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=n9_DWTIggH2oc_Oj2IOORn8ZaZizG7see_jMFh6dXdFxfMv2PsQmxIViysAcJtwS14QZhwxMAKTHW_yxtXvGP299w8xFmzPBSCz4a2pHE0mMEu0ERfca4Gj-uh_1JBQcxv5cFKVYKH8EU46KFKXb8eLSxRl9LBX-3Y5M2FNWeJk7whvhOoDQRmLMNGOK-ge74iBxelijSV4zS1u_ukzdG9FUZUibi6dgx4ugqe9BAQpgk8IevEhm5NdwGKZwQoT-uQBzjjFUqSfntxEupMoEHZWQvX9cY50bV4qRe1q_IFa4CQTs1XtJOKqHG9b0fPrLe8ggUhOX7Jq7kwgmmoTNPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=n9_DWTIggH2oc_Oj2IOORn8ZaZizG7see_jMFh6dXdFxfMv2PsQmxIViysAcJtwS14QZhwxMAKTHW_yxtXvGP299w8xFmzPBSCz4a2pHE0mMEu0ERfca4Gj-uh_1JBQcxv5cFKVYKH8EU46KFKXb8eLSxRl9LBX-3Y5M2FNWeJk7whvhOoDQRmLMNGOK-ge74iBxelijSV4zS1u_ukzdG9FUZUibi6dgx4ugqe9BAQpgk8IevEhm5NdwGKZwQoT-uQBzjjFUqSfntxEupMoEHZWQvX9cY50bV4qRe1q_IFa4CQTs1XtJOKqHG9b0fPrLe8ggUhOX7Jq7kwgmmoTNPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czEU--pt4rIlzJMTf0Jn6j0KnJiuVOz7ddWKIjOcJWoVZXbA2EWlW3TnZXaWoZ1UUdbog8Bq_Q21aNYzhVfiO7QbytavwAZaBggEUb-4YnW7ievX0b2_S2PUoUKeqGU9HthxFHkktvOC1mmPdE83dqTO0s1E9XJt33a7sKbHl8263cHrFefasnDYGGnsYvaFz-Mf_GTFuMymjcoEl-0iD5LJl1dZUsIw9RCBrsQ65mJh6llZsj_UOEdOGwglDdb-geOexgI7TADWfdYyLCdn5MiTFm1wsBOlTBTBwpbyZIjU2yvfFd3hTMElmrTzD8x_4XUsFZsYvsVKpIBNTOVpoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4r-GsSYUvzSJgkxYW9zWnjUHNwLXfNjiy_Ha8Un9vO6kkgSAsyQu1LogpuOBkh1rZggteBKaV2ZviTI_VuA-wRK17A_LMos1F8Lfnt8jUpjt-qISqTjK1lwWINbi2Cr7C-lb-fkDXSUswC0dLmsMvoKLL4pSY2DTt2icLe0rfxHWqs7MRNj9TfEku3B1jhyEftbWY6KdoS5Vb4OmX9D90lW5fGqPWUfqsrrTeH9V6OhJ7MKTnkzDyZbDqYH-hMfmpgyeHxLfCfYKq6Lx8pDXUnMZMv2rS93SivjcrsvJs4YpMXbB7cRxWxsO70TTo1r8pjVspvpi0YRHWi6mDCWwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=IK2_c0gAJed6tYqsg5B3WIuAaxRrs3WVR8eMvacrSM37lIsRsvuHRMJJY_cHOwqrunOM3pBNP-mv0FTpluRkZFMH7z9dpqjXXJmnlLWaY_qwvtjCB89Pf40S7E7IS0tBfVMEsee9pYG1BA8_dxFUVfhE3d4vC2QC5BOqvlxVa8yXhmcMEWYsAGESAIjdD8LJoUVy5hXmf2LK4juAMjJLebLKIRSShars_rapvbVYCxfePoPBRxCb53ZHSlMBVhwPnhDgKsqEXIEhq5xRJYQN8Jvx2j5t80SPh_fRIxrowLf8taKq_XX5YtsTKlEDgLW01rWQcOB-Ndc3Rt96Ii5ogg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=IK2_c0gAJed6tYqsg5B3WIuAaxRrs3WVR8eMvacrSM37lIsRsvuHRMJJY_cHOwqrunOM3pBNP-mv0FTpluRkZFMH7z9dpqjXXJmnlLWaY_qwvtjCB89Pf40S7E7IS0tBfVMEsee9pYG1BA8_dxFUVfhE3d4vC2QC5BOqvlxVa8yXhmcMEWYsAGESAIjdD8LJoUVy5hXmf2LK4juAMjJLebLKIRSShars_rapvbVYCxfePoPBRxCb53ZHSlMBVhwPnhDgKsqEXIEhq5xRJYQN8Jvx2j5t80SPh_fRIxrowLf8taKq_XX5YtsTKlEDgLW01rWQcOB-Ndc3Rt96Ii5ogg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=jkGlZM1XRxVj6FkZUd_Lrvz0Kzr2m2092HpdKFwakDo6Tn1JNYzMaCp4xwVt2PqlJowgd7wp50t4hfT1O_gIIafdCxUDMquBi2i62EVx_7qR248VSEL0paGG66fABtK0u0IZGAMZBRFhIGcnxOQO7twi4AFbIfZzgwd824gYekk73Mcr1RCNMEXe7gQqjp5QbxyP3v83rJs4MYYj2jQS9RwJXaFEgFwVAVB90sDEGbA9ltgMu2Zvmb_TUei0Or2bZpKLs50uWM-PpDnI773dRJUeb7DyYLrWCg49w4iS1QIGTCtgRC6iZdUrFwEEBycWxlBFKziWWMW2Ee0eIX175Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=jkGlZM1XRxVj6FkZUd_Lrvz0Kzr2m2092HpdKFwakDo6Tn1JNYzMaCp4xwVt2PqlJowgd7wp50t4hfT1O_gIIafdCxUDMquBi2i62EVx_7qR248VSEL0paGG66fABtK0u0IZGAMZBRFhIGcnxOQO7twi4AFbIfZzgwd824gYekk73Mcr1RCNMEXe7gQqjp5QbxyP3v83rJs4MYYj2jQS9RwJXaFEgFwVAVB90sDEGbA9ltgMu2Zvmb_TUei0Or2bZpKLs50uWM-PpDnI773dRJUeb7DyYLrWCg49w4iS1QIGTCtgRC6iZdUrFwEEBycWxlBFKziWWMW2Ee0eIX175Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtoocHWKKYWECNZE8L_OEZe9CBj-6FaIvn5H8bWXo4d1FuXO-qDtMFas6KyCBpsIRmbjFIHOiykLml5CbP4ENYAnXbPnMPPcN65CDJpto6hRPbMBGkR0KeUYi-n2p73s718OITvvkaiV5jmdj6NyF6SqfxyXeoolCzk63OQVxrZACA_qzXFPKCNpNZSKQb1GdNh2AtFPa4ocS3J6T1nn0Ld51xLuIQPRwU7tchPaWbgdhIisC4jyHXvcpVgCuIlt1TRljxCUF_BwgwVuXsaqgc2BRWgCaCSIKyR710UMK_8kdc-cwCV6g8Y-wxBa1iDXJQNJA111bCyFLhD74_84Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xb0twuJgBIG6vuuoLFeLhOzLyJgdAv93Qa1chqRihf40hFIuSjlC2ZnuQq_-SV2zzBzS27gjO2V5Qpe-L6Zl7QcxfE2yMziOO68KGsabfPOH75ieF5k2swMOy5CBdUlDPM-8ostyqSu1YPTS83EEmOet8TKLeAkcm4-ADHrYD3ebHwTmLZ7kVpR2LmkRN4Z8eIQ3IwPdjU47IRJayhquIWdjqRxGsJDwEzZ-69w9jgU5HvfGnhge3oNV4lKb7nhnN-flAbBMBW5y8h-33aX_5y9CP41ew8O7Db4rV7Ingx1MgqQGqJOkdNnoK7dWAA0xqqiYoKXimO2JW-VBX7e7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udDXAmSwxjaarCxV_QyRsBUF4rAmfLmvuhFZicPTJvhA9Bw6tFuJNGO8geDZXRfaO3Im6Qp46KHAyXZish158-hM1ibnEFXgaA7JRnQQmfczuDUoDkOBEQDII5O5xFmm8TFIeeTzR3WukiZwI1ngNtaPmGK36llRbOniiNKGElbnSpbCzmUkbSzzta9kiOUiDvfuhbQPyaP6Ow1sFanAmFvicg4m3psdRbt-5EgFADpCiuUGtG382aEJed_ERLmp3jXVy62qpAnNE0JJVOkBevaHMA0fPwU1RVEV28YhGMmRJN7JX4yVj77Oi_W7TzytA1b3L-03wKCLtzL0UKlxZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=iY-tfuJvqI5lNjzptg2gjor8vRZh8s37gqgKkGV8OWWS7rUBj-pOsQzcu13vIhh7KOQuh_k8x3xVexCl4A8hrzL8UfYU_CmmKKThc6krLHW48Le5x9g9F_Beg5fZwiz0yqU2ePb0aD-PNnAISzg7ayVWgAlg9gRVQl6vHX4aWQ8vr6c_W3QfQzaZrs_IxyVL-75Q6bvGaXk9EL_saoYHtXO86Vls_hQcg5TaN7fo89cXYUL_OBsOKcOmhyneuFgL6XOpelHNpXhLQDPnsGFjeseCa2s-ZjoIX7400Cx07sQqKvz39_NJlPBEQVNR3QDIeYjAOhEFErT_xV2U7OV83w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=iY-tfuJvqI5lNjzptg2gjor8vRZh8s37gqgKkGV8OWWS7rUBj-pOsQzcu13vIhh7KOQuh_k8x3xVexCl4A8hrzL8UfYU_CmmKKThc6krLHW48Le5x9g9F_Beg5fZwiz0yqU2ePb0aD-PNnAISzg7ayVWgAlg9gRVQl6vHX4aWQ8vr6c_W3QfQzaZrs_IxyVL-75Q6bvGaXk9EL_saoYHtXO86Vls_hQcg5TaN7fo89cXYUL_OBsOKcOmhyneuFgL6XOpelHNpXhLQDPnsGFjeseCa2s-ZjoIX7400Cx07sQqKvz39_NJlPBEQVNR3QDIeYjAOhEFErT_xV2U7OV83w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1GriCI2EyZT2AvbJFi9GObCZ_lA8XWxJJ1U4TbjwUnG7bgpHZIfxcNfzq0t4PaI8nzWq6RnhB4BAS_JhGHkrlSwP8gbJzLNjVz24lpzwY2UvZxLuGfK3HciCOWyarKPMtM7g7KQtDQDvYcP5ywlENs2S7vlszAyYr1DapT3bJfKFWfdBIRIQ3R31nfCsOuAiKUaHXD8tZTrZUu1xF22qTSTM5Vi1NCfnEq45BbRzC0IRn_1oMWvdcZknE-tZHyXg3VqSUSn8Rby5eXlF1Io2VfBWDV3jV2TRboTnltWhVH_dy-sPdyTrI1aBIccQ2T-a9KpoKY8pCh-_YrDKQck8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M708bAOoCrS7bSjDkfXPGXPGapQPjAi0HrAxouaMTBNGV1n0tI0M5S941jUEZFYPx7kffmEBLHyHBLcHXHmTR6Vv_7S7ubpFDSM-Q3D3bq_96ynyJ8xPXcnmARWcRRIvVDZ5ojZYNOeyDg-CnTRkEMpt-fj5joDUdMJ_PdZxMXY8XtBqSx6ctETt1bI0V0r1vy8R7DYsLep1NiZmojRsWznKo3W1jYS7gpbpaLji8UFmu8Id6S7kExpaQ384NI6yQuiPi52BT9a6CX6yH4_GaVI52Y9s80SKJu0_UMZZeMNDQMjb8z4f8pac7dqcS0TUEaSfz3sOl3lqWjrcfoXDvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/As2iP16dW2RVaOrg8D3PEhPrQQ-sa8VdQVTTL-KSA7DAwuPtgdRJkZVG0Y-9v3qCAcRjUe4sePnEAqFBKSoWGMR3Duy6HOrAUE3nsugGRNu0_MHL1-AlovadLzl1B84mNdHbxTncMjgPC8r1_msPN-0t0tyVTDK9Lg4rV4BENI1_CbHt7907bjdOfpwbQs3xxT4YqBJwW2Jo1wP6l-zDaSpRKBmTKwEGjPa4ErN8cH_QHEfraTK9zFNTqmMGpAcGtd4nGkn8txvRGo3jWlJbGwwM5_OYXOFDqFgpQ2VDprPVSJ2isJ-C6yRmZU6iDwpQ2ZxWpqQ2qyU-iTykvFQsXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tF15qaglaCT57VfTuc5tASJB5ono6vCsVZRkyFS9jDLYesnaEIuLg7niOgxrLEgefESPCCUr3T_CXnaQOJ5rQedVelUVEDXp3j91aCFYd7F1NGqwqZ0kV_hqy6DCVIno09VggYw9Jg7xFdiNy7uJbQBjB_4tc7Fm9kMZIaVE8OkiCv0A8GJQEkl_iSAiGx609p3lWV8g_CDBjZ8VJ5MFIhsxixOKQcaCLVBxMIr2a69q8gu8SRUj0v8QNXBZQ4QfHaN4tKkxymJOTryIOqGuxV2KLzJ0GcN9YFDBDuIQkKTkw-K8p6LR4Skt3p0VzvyCmjEwea2ikYPB2zpiOB8S9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=ZuY2T1o3wZa-EMowxdZC1WHZCaKjkYZ9xaY5Ng7FIiSI7yJNtUaC8f6x0vUve8lXmBENuM4m5CaIQU16IBp5-ZHhsR7puMUiTfVZhMieNfTl6TMt1-kIJ7EETBIj4CFaUCi3wJIDrjtIRYfyYggdoU7dD5OJ6eJAyYzh9Ni16HEG4urmxpmy7zvx087-pZNbYJUkbMNroxP5wocABQaYYBfkvdoH5-gYvhF8gZFbb-CcXKDoRrJi68pf1oilMFkEXikyf72aL9q8FuYUue8vHdnQE-gl-J4ACYXKMQOuvQ8rryDURReVMOeVAEC2Xv9CsDsogMja9AY8MMIb6WzY4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=ZuY2T1o3wZa-EMowxdZC1WHZCaKjkYZ9xaY5Ng7FIiSI7yJNtUaC8f6x0vUve8lXmBENuM4m5CaIQU16IBp5-ZHhsR7puMUiTfVZhMieNfTl6TMt1-kIJ7EETBIj4CFaUCi3wJIDrjtIRYfyYggdoU7dD5OJ6eJAyYzh9Ni16HEG4urmxpmy7zvx087-pZNbYJUkbMNroxP5wocABQaYYBfkvdoH5-gYvhF8gZFbb-CcXKDoRrJi68pf1oilMFkEXikyf72aL9q8FuYUue8vHdnQE-gl-J4ACYXKMQOuvQ8rryDURReVMOeVAEC2Xv9CsDsogMja9AY8MMIb6WzY4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQzR4j4b7CCdWR0jNbiQ0QWxzqM1xayj0Z1zqkWQ3pU4qwUtmd2MfOvayGw9ESIeMurErQPshEIk-HWXHwFRLvxGrK0oM3SemH07IADYSd_lDRhSul1hD_t9INFlf-wFZT3Z--eEPIkB05kP_cOaxxoIdhXhjAIQCByhqZNS65DVourVp6vLJVU5WlvV0nnSOaQK68hCf99DzHHOu7aJ6KmSg6-FZotnadvJytj4njZigbZQDxFxqO7cXYJGzQk4N-FoIV_D7aXMgct0fBfYPgfYlSIaDr81SL3xhp2MrVoUHUZPX4iDIYWJzWsN40zM6lHsRvkN9BbcjiwcClnSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amPJdOo3VtiecRIdiAO_NpztQQDCQTi3I-QgCUXW8APv5uHML4reAdKeEaNUHCF6bdZPzYpcngFOI0OoxossGDVPkebbFtcbQbSmyu2_QTVco999A3s6uNwqrpXgfxG7OrOKNuSNGDqGdL6drm1G-K0lp_yz4TS-lferqvjeq-W9VR6zzD7f9NnwCK9dynCEfHit9IRxfRSyh9F4xrNSHpzztpkCTwNvKsqlBmjkRKpU_Gac9vI4bT3xZtywuSoKjzYwbE8ppQVel8zQC_HTmFht5AknUN7lj4BH94NKotQTd-WYX5enSXAB-hAEwpNsQPohC91FTmyI3JiSUnZAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqBxm5l8lMAFnnx4TuCz6B2wI5CABp_jh8Z3mEYiFSOXUHaiECmU4NR5EpEnlPpKoVXB6wYDanJo6VSVRCz0K6M_oPLJ9T8iHl-pGi6FN16UoPybaRh_FPGTGOpUH_oL9-PZeTCiohCCCaFNzUQI7wehiyX7_1Y5LuVvtEK9jeSB2q4pAiAdxqWE9xWOy60ylojJ-g6mtK5ZpY4CSa_hmaGz2ewxJTchvuPagoPoA6iFe3SSEoWcb4nUnGrMs3dZiNBP3cCiHD8tL21MYn2qlKdakS-vfxz-i9CcqDhhXzr7kKxUjFYnT0l_h6ZZ5EWhVwBTzU-cO_aWurgc7zEYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=chjg4qIPqDD96m-WcBQVT2mMnd64E-hMBWn0a5SIy2rYz8mgZO6pExgWTfTeAaYkihBRovqIs1XKg0JVk2roZzeo0fLKR5WZ1tc1Os5ar9dU-GTPbPZZVQOvNcFQ3BmbYOBkOgjk_ye9E6k6aiVXGquDAB06vpyVGoTy5f8fEUMvDlHX5EATS3BRBpNInPvSbC1PadYSgpkp5ypAU_vtsloWb5aPRLSo8DIZHNoVXdj358oKYmMzsMkesm22MxNCvukDp9XVU0VvmfKXSsPbmIz6y-aAWZujsejB9C-uPlY7acxntPZBYOMiYcMGKKHQomY7vlwehrBPxtrVw3PVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=chjg4qIPqDD96m-WcBQVT2mMnd64E-hMBWn0a5SIy2rYz8mgZO6pExgWTfTeAaYkihBRovqIs1XKg0JVk2roZzeo0fLKR5WZ1tc1Os5ar9dU-GTPbPZZVQOvNcFQ3BmbYOBkOgjk_ye9E6k6aiVXGquDAB06vpyVGoTy5f8fEUMvDlHX5EATS3BRBpNInPvSbC1PadYSgpkp5ypAU_vtsloWb5aPRLSo8DIZHNoVXdj358oKYmMzsMkesm22MxNCvukDp9XVU0VvmfKXSsPbmIz6y-aAWZujsejB9C-uPlY7acxntPZBYOMiYcMGKKHQomY7vlwehrBPxtrVw3PVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Q5RrOB2jjAWe-li0W9pTPAshoHXbawLsnSuQNG5pjhqRq4y85bpQFICSy3NYFVg2E-07dtMQpzp10tb-WRMr4qR4glomSofmQXOVTovcjD-DHwF1VbLXYDLGrC_XZa5_HXe3yWvNsrR6sASmRG9ioE888sljVpkJ2zjww01i4M84oBjCg1iB78JgofEsbZ129gARvmDcOLTso7bqKtuJi5cK-u44Cp9dvSQmg9Cd8SKVFMupwrK7fPLvIh7DRrhQ_sfI8pJZoYYkNANslYiw2FC95OiE9L931cRRLLQVRNMwMRY6B4uoYeowVUuxC2LP93LTkYpg82TyFNw-E3NeAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Q5RrOB2jjAWe-li0W9pTPAshoHXbawLsnSuQNG5pjhqRq4y85bpQFICSy3NYFVg2E-07dtMQpzp10tb-WRMr4qR4glomSofmQXOVTovcjD-DHwF1VbLXYDLGrC_XZa5_HXe3yWvNsrR6sASmRG9ioE888sljVpkJ2zjww01i4M84oBjCg1iB78JgofEsbZ129gARvmDcOLTso7bqKtuJi5cK-u44Cp9dvSQmg9Cd8SKVFMupwrK7fPLvIh7DRrhQ_sfI8pJZoYYkNANslYiw2FC95OiE9L931cRRLLQVRNMwMRY6B4uoYeowVUuxC2LP93LTkYpg82TyFNw-E3NeAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=LUwiWuiS3xlpO4nqLwqDknFczEDzE1AtPYMWLU2O92Lz94k8z_L6v-Sk_g36cMhyPusC9gaAKGyxv8OIzOTI9-H4aMGEbHfF-MrokIfUEKpkVQNJJ5wpSNdn3FhLWtyCM86zXzwVSqzeh5m2WJbLgMeUeQ0Mtv1PefN96_0oGta6yBAJQujUCesz4ERAyfT9Aeo1uyUYWHcPU2ga0ojcPEFQnu8FeFWkOVlFy_jFrQidhfWvXZbq335m296JFwJR14AdIUa65Z1TzJiuX0KPd9Rma2MuC3kdQs0_W1V3p9eUIQNg5mftNzRcP9GbOnw51oA4msDjGnbIUCpuUPQNTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=LUwiWuiS3xlpO4nqLwqDknFczEDzE1AtPYMWLU2O92Lz94k8z_L6v-Sk_g36cMhyPusC9gaAKGyxv8OIzOTI9-H4aMGEbHfF-MrokIfUEKpkVQNJJ5wpSNdn3FhLWtyCM86zXzwVSqzeh5m2WJbLgMeUeQ0Mtv1PefN96_0oGta6yBAJQujUCesz4ERAyfT9Aeo1uyUYWHcPU2ga0ojcPEFQnu8FeFWkOVlFy_jFrQidhfWvXZbq335m296JFwJR14AdIUa65Z1TzJiuX0KPd9Rma2MuC3kdQs0_W1V3p9eUIQNg5mftNzRcP9GbOnw51oA4msDjGnbIUCpuUPQNTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYi1U_yaR6szEfYIAyTvWEuVhKCqv4Ak_FoU6wo6lWXuWds7M9qigNsH52sezcS9mfqucLpsBS5aCV9JApC5PNmaEp-KvYudaoFWQdubl3ukX5uGUpQZjQ7uo3kDG9-Fc6PwVoJrKQIpqzvrrNcoNI6t1Pcnwj5Doh5bltIL-UEfxhLFm5nNdZCMIp3BB79-inhnPa0KDXC2MjTXoRxpT3X-mHsK8APuoRX_Vi-717mTmQ3gNembrXEJS3NuYv4-RvRa6w3q9mawOuqE0Ngt9KoVg7pCzAvrOSZ7Y4AuRyDg3XCT5PA-2NM7yzVSJXUkWMM1DEt6GrlH-cFJwvjjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_52p5F2K9cXIC1JL9Zke4g2nKPNLPWzT2iXXju7LkwmdlyeYTAKX_i8NgINn0JzXeAS8rrvmUrOnvsVXAfzjgbgGoDaD-Y8sWmuTMhSKFFa50QtiJMVK9UpbBXipQdxxo9AzoN8zW-Iz6TXmUJXfmLG1M9cQoGKESsZiE6L5yZws0qR-r-DmQo_gcAqGZBXh9y7iIqUNZwRfpB0o74aLxdR3CD-w4YJ7p6-2k1VeFqunMmKnwlNgQDh5mWxwFMCxL4kXJCunTKvN0rDzE3VAb2LOi_E95wvj95xX8lmfEkNNNnYiCLguwXj8bZ7KWbf5SdhhAG0XGRpbj9BfW-7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XB0t_67jyDoADAY-u0WZhG6J88e91R3iZ11gajTwU5hjxHhfl6N-zWkLbizcQ0FgEwNr1rKoruX_71vtd-YdjyWCHkKomcktG_9AYiIXiLPOOmr4aFCYvm2dI8sohmgEozbDWvFTAsA7Gd00DqEf18NnAygiNW44XxdO-HNzLX4u1mt4kT8f5I5rzLCb2Zubxa27u4-izWJr8JQfsppj2VYGxcWDPNjTBXOl7lwXaL-RFL90WD3-fLCgX5BTKoMmkr8IovfaNN0N-FxtyxxlRtuRuZqhCWqjW90KP2osfdlIMgiLxoJsB23fqetdP1U9Jk13cMcX_0CIdjnxE5sX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ul06M7M6M9h8SyZD0LPBnHY1Ly1T6FywMYSJ66NLRqg4WQhDfiJw4q5MJQQln_DJWJ1HT8I1BzKsGOPp5925vRpfyULCvouFcmeF2SdW7mrkP4khAbxPQDy0MJbo0hQOLG2ntRAWSQqGz47sVqfXcUl-UeC-Mx8yVo45S6WWtcnLEDpZEbMIqCeNRCZiDOm4gHiSBotAgp5ervnndbdozz55vxH2TMexv2_LE2pDiMCCouws94M1FxEAaeE0hp5yS-YrxRxJoBpOUGi0AUx25JdNe8khksZDldjRjXm3zirQaC6_f9kocbT3tMRhkNm0Whlp1hZV3KgCF0lMHJlrKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldoi7rXALFHNYlIdrPzZZsJmT8fnbb_OTrxWlUzaEY0pkHoLqC6KyYUB3J8t7R5IwvU2bWNRrkGOgw2Ax8WfRk8nMyI7OKYzkLJjxdVETqL7fWuMu0uaPx3Cm2qTA1_tUJVYM6WGXJ3gha_DQOd7y9k17r99tZ0PzwBFIC7kD7A6PmsHSE-EQqWQGdvdLjGBqtbfYWi-79XEmCQDVIjaz-yO0-8nCo9w4IIyP3rM6gkTJTU4p8yfpvhe9qyNT_qhphY6sp3GMn5YOLQmAxToscjNqLk0f9cJMSK5Ba_u3pkyk6Sx5gxkJzrp2e2eWClReqCgz9HuVjJ0R6SmncZjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EfYIovv318lFHzNcWbR_tVKpb3NMdQ2CUaP4fJGfXSJ_a2b5ytDc90PqBcj1xXhLgZaEVoDjEi9CvOnxAs9x6OoFBU-TGYVovqqtarFWMNmaxvb2bls2bV9jjR8Xb1Yfrs7eEBnig10r4t3GUJPrT-02RpEJ45K_6oLgShjD92Lw2xy69EAYsX2kytrciGXogBDfpIwDBq0fjH2wV-7zEPHf5t13Gk-xON-FyGrg06LutylDvPMM07_aDBAcF89pxbzenCF-zBnrJHSwqPGtHt8BMyuFRGuYdXWV87AF9_MpA5AXOnY-uP6Yaq3sYRgJ1d-0JM_eJ74n-Op5rp-7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6OBUgsmduKwf922ZsFQ5kHyYpQLVyfskZaM0vJ8VlGM-FeD54IC7E7HG-EFnnjNdkj1otGFvgqDWVR78SGt84_1itr5cctwpFAnDAl8aQJO0OD8CQ7AzfAjIQaX74imlrHWvMPgCSNGgID2KUUbFsyDg_vJvdaOxSzWj_iEWfotOWkakEjdUU8OzxM0tcH3yN-ptrXTo-gUJuQdkfHhAS2Wc-y003UvujPX-phGssiU5tgytdzZ2B64ARyBkvrU8Nw12226gSbR2BscOfQ1gE-kCqa_4-QGVnarEWaPHq36KNaYUkRUwBHl8Ghl92yd0WTyR_SyQtVYlNwcfoSQDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7yBvUCPzaRJgU7sUUwnEk75go2g5nWUFmWTqfaNt82Z40XFrGaOFnn43ehlNqzexnQ64tiG_PkVdngV8EGrk1G4GN4TnnmSJPiVGTe_jL8Q5JvrW7Qg6TQESPhn3V-i3pp2drKJuDcNddsSvFAZ5XUFwTtvBTj9NFKsohulIbOdea-n09zLh7uqU_SBhpz4ZrDiW9gOxxXSgQj78NNMfqJKIR5pvT7OZG-MEOrSOhWU1GoshHZ-WbI_os3y9Q-ud7omua1fSiUZF6YGegP2nsj6UFxZrReLFyHkv6lvbNNz07qfOEMnoVNmUltl93mxcZvDQrGGVhcpUZdP357pBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRLEytl465cv7eyL0ejE3V2OlEot9OaM8Xv8rum1mmxawKlV4RTGc17_bC5BkmerIuRxEjZzdtck_iFI-PRoyZxhvCF8kBBmgpMQCfruWCJUdMYtpcB5TFCySRGumn1t2gGVATOaYEzIb7cwX1E_Tgkmox6sawe35pGPEwF4ePeIGLMhNJPznq2VRTVbVoRd4tQryFAnx2gMvv9EHOuPKQnpl9vEUL2R3tWubCjrI0Qq7aB8kvkWXWgB94Xu1-jtlAPa3rocIevL4ZStshRBR_AngcbRxS3_oq22jZ83U5-E8LoBrfdIsFhkPSrmZfAiZFVUMqOftoCE9t0brjOkCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j64SbU0Lzvkz047AJC4206zY3C_XnsAMXi_fXA4EqvP67yToEySGzuILAFA1aC-PttKeIS0Bb_OTbyfIkc7VujWXENMvcevZoP6Jy145KJT4Rqf7ojj5HyvYcVDKgq2G1oP8GmUQ1RJcD3gXDK-pYVl9D-Ttrk1Kz1y156x-S2nsHYYj-q_Bs1eEHDx0QrQ9suv3NFsETA_sEMfzxBuQfZb1y8UoQsd7RHQUPxDWrfgUCmrI9R1zd8un9dhsUz9USOfiNoho1C5gMPOJTraL3cZ5rg5fWDI2dkabM7kdgStjmEI1xqveAkt59eZuBJ6R04Xq7NJIS9x4BWknL5nmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFNoRs8ZKK2Y1i72Yt4PhAjes9q2OcbZINuT0LaqL78VLofgk5FtLn4atjCKivTeDrZOmJO4XsKma3j9OZAPXhciFpoktXrCDzld1eB-Xm4pyhbTWS7bJk7Zi188OKgZgONkBy7AiUSj5GxsrIkgu45AgmFi7ivfJ9Po-lwv3G0S8MyNjNmqi3MAWHk-nD9zdRRdVhYa6ncxJ0xbdjHgCK99i0kRDb1Su63pbRS0fgWGbpoagWGrsiKgFD_8nVMfpywKXK_LO-2Ggr4J8Iccrn4_9Y8KAADpPmWDwk00alcc6PiTgKh8PmtD2YXD49A2uU2xb5LTVhWcjma3rmx0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5klLElif4qYsYFVtdak7yUOiahm6Dk97pHNIQ1v2EEjlYSAu_D-1OC0_kcqTrxapAEsQk9CGzsFGV8-OF0nJWMRa-buxf3OAu4chaImYAk0Dpj_OTx81CONY7u5G9LPTDpF3IcQ0rJoS--OmVbddvNAGEeS2qRhJKNzdSFOXktIJDISTkdYwQGal6AwXiJKHumzT2JMtZKzMhZjxOHF93sp4VBJxpfr4IDXWGjgubn47891YECuElFe3R9fe9gYNHhTHeaejGFflPpsiXybMJIEx4NT7qZkKEtlr0cwvQphZDFmF12w6M3DFUiiVDJUBZvLbvKh_iCteceiEsDN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ravuyDB7H968mlOx_6VSbgpHTddyFleBULkGz066mhnBFFScStze9F0PWeWt7xr1FI0R6oBce1ZL62cCYCZerPW-2Cvm7xi1-go9KXkXW3julUjvSUqvbAUpe9C5oA2XfHwUMSNeaRifn_vM8i2JunulkVHwIALFfiscOc7ePKp7CxZUIM1cKu0BABHMfd6DcAc0jNWe5GwM3y1A1BO5LB1bA5EaQAI2xFhhLFkpPbIBVVpmULxK1sXoULP0TBzL4Gv7WfcxXTYHElvvgpHoDhyDgdFDhC79ffNjqcq8_TOh-t2FWY9ztULk4OTzbswT1PYyG1sZrVoOCZ_y7Ki9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjrmWfu8qHqIjX3BNKyZmHRuYTBmXsrmih9HkBUhTGY7syKQrz_BLGKrDAO_fjPbeHksHShuBicHh05p8tP_MTC6bp6UA4QPTBiT-oMh6wMiDeY8t9tBvel8SBaKWms0ze6TxwfCLKva8lDMgjk3bBz9KxVcMU4uATHv5T9LsAbmXf0H4ofZpf7MGhPzWPfhrjVfGxJkGLiwjy1Wxz8wP5BVb_wB7TLZp2IQI69hz1NLBJTwB5b8L4WNZZ2VW3a9rBEABHCvR1NAPciCoLYYrFcDUnDGT3b5awjmb9w3fsTZtltUl0AyfB1oDc9kD8i1D5R9yu6jVsK6GoDHyNC74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X90-iO8zb_fTDJir2NN4k8WWPEluAEtg402EcAU81ASY6DbnXqOUxmVnLsKCISRBAqmvnyDwaeiZlsTKXglHkiuMttqGB0z1nNBeR2WDLf_Wyf6KBL4TFYrxNCLmpfY0mhb_vDj98zSkJ36JeFOTxUWR7MC_WuXkJg-OQHXc77CRUVIWP10az6GSuebZoEZ1joMhGPto_wgdGC7fjvp9PATjk1LIoBRjZxMgE8x0DeESNxuQ7SBeeb6QsJEJJAvnWn2L86hlxrorvHxBxf13bHyp47CVH4QpL6A2zAXAun1Yr4oCy0igeiMIPpj3OMN9GibSciv_8QBPMe0x-6pPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=mF87c9XDnk3FsJXKP4KewDQWtj3ga_bQ_-qy72LO3y85J6MPX9qgYr9eZ0aRb_QA9vJcBBPJAbmfRmgrEI4IV85-bFern87CX9aeD2AOnk8LW-tgJEYA-_8poqAkoj5uFsUi_dhovml0QEBnEmthTQ9efd8K_tvdRetW6vzZNuGU_ArC2LI2AFUG7wZv2oj5VbMDMrhLA3Grotsl_h_n8GrkWSpJUNaJx276ZBLkoArHjw3P6ASaYye_2nNeNxC-0SrDUvQhv_2q2gt1IfJi4C0pEWnhxQLY8MSrAUSJQfv6TCNtwi9sQZOQzdqYVJHUigJAVvDTVJ9AnuasewpYnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=mF87c9XDnk3FsJXKP4KewDQWtj3ga_bQ_-qy72LO3y85J6MPX9qgYr9eZ0aRb_QA9vJcBBPJAbmfRmgrEI4IV85-bFern87CX9aeD2AOnk8LW-tgJEYA-_8poqAkoj5uFsUi_dhovml0QEBnEmthTQ9efd8K_tvdRetW6vzZNuGU_ArC2LI2AFUG7wZv2oj5VbMDMrhLA3Grotsl_h_n8GrkWSpJUNaJx276ZBLkoArHjw3P6ASaYye_2nNeNxC-0SrDUvQhv_2q2gt1IfJi4C0pEWnhxQLY8MSrAUSJQfv6TCNtwi9sQZOQzdqYVJHUigJAVvDTVJ9AnuasewpYnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqsuYo5VMiDRXLV3XXeO6riC7DwwAbuZF75QaSxPnqOCR0-UdCzvwi5pMqauYzYfM1g2KRNj45jnvgVMcGcV966ANqg3h3SrywAkIVVjRIyFYWaidEyGx4yG7jGqlSI-gztMX_rRnbWM6WDfA6HTm58OPy-7uhbdO54pjRbNe-79MdERdPlM3CQ_FxWGQ0bBIxwpgTgQiXVZo1M9yuikuVjPMPEWzMRf_bqwzq5N1j0Ajv4G04GoPNrsdTaQoipCRqtCZBPciXeU0lrY09stDpMYa1UIOWoW6TEVnBur0bmQeaTCE6kB-4Wpm1ybPa57wODnmsr8tgKNnlzaB783mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=lu7bjfEPF-GRts1ayf61dc2KU4eu0aluLWgqkz9bP0TorJlPifCD7JNi0sDEyV7QIDTx5QVgQKZEcDjMFiQZSbw4V32ASqfsRiaWi7g35mG64jjSZcz3mc-UeR14qoz_kaArxAG1pLEQVE16uY67d3hl4UhPFsgcHGMphBHJdTFj43n01_iD9YFRvcaEljOtXn0CP0ZOrUatY8G7CcqB4UJas0nyHgCzzfl1Ws6buD1eD3ekxtNzCo48sKC2pl4UUSmhAV_Snm4y__oH2jYbU3e5puOPVE7TBmVFa-od5Sm_KT6zvjhj2T6X7sRhmmgyBXJ3HbxF-P_-XrvifnZHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=lu7bjfEPF-GRts1ayf61dc2KU4eu0aluLWgqkz9bP0TorJlPifCD7JNi0sDEyV7QIDTx5QVgQKZEcDjMFiQZSbw4V32ASqfsRiaWi7g35mG64jjSZcz3mc-UeR14qoz_kaArxAG1pLEQVE16uY67d3hl4UhPFsgcHGMphBHJdTFj43n01_iD9YFRvcaEljOtXn0CP0ZOrUatY8G7CcqB4UJas0nyHgCzzfl1Ws6buD1eD3ekxtNzCo48sKC2pl4UUSmhAV_Snm4y__oH2jYbU3e5puOPVE7TBmVFa-od5Sm_KT6zvjhj2T6X7sRhmmgyBXJ3HbxF-P_-XrvifnZHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=oqe7h8BGkUgLL3Y-T1SpHwh7VrdfsyquUhueH_5d-ZcvDASjKqKFc5gybraonmGq52VWrMVlhxSbxBEfVMn4Tq8fwK3vaRMBbNgq7FNG953rWqGX1VD5qInFUAab-VtI3G5xcihqXxz8vm3-r8FEt5bXLdKIJzaTqT0zYfe-9wj0jlNcTGNMFB0CUKyLArC5uZ1CS_88PhQR-js-vB1gxr-IkJZr0W23c9OAqpJSQDxnpk3zpwuP5NfxQDujUKfylCKITVJBhexPDAtI8rnenweqoJPYPX-C4aV7oG9wCqpKdbvKhQf_H_yo8oVOVlCLkz0-LVBhp2aUdMHTHW2sWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=oqe7h8BGkUgLL3Y-T1SpHwh7VrdfsyquUhueH_5d-ZcvDASjKqKFc5gybraonmGq52VWrMVlhxSbxBEfVMn4Tq8fwK3vaRMBbNgq7FNG953rWqGX1VD5qInFUAab-VtI3G5xcihqXxz8vm3-r8FEt5bXLdKIJzaTqT0zYfe-9wj0jlNcTGNMFB0CUKyLArC5uZ1CS_88PhQR-js-vB1gxr-IkJZr0W23c9OAqpJSQDxnpk3zpwuP5NfxQDujUKfylCKITVJBhexPDAtI8rnenweqoJPYPX-C4aV7oG9wCqpKdbvKhQf_H_yo8oVOVlCLkz0-LVBhp2aUdMHTHW2sWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAxRKfHJucUs8T2PRgdHxX_QT_43Dy4yq7C6nbzt3FTlJZkNBEsqU4C_HjGToDm1ohDv_ld6mAOZIsUWAl4h3-I6Y8h6RgKkNPWY9Z5ZFW8EK6ceWxmgmhNrr22CBdfACxWOKj6S3D9J3dBEz-4ijAZBRZtBmHFE-AszKtXWn1STJUM9Q6JNdTHGhP4Kb46SBlRCdlYckoIFB4CfkvAWHOGO0A7uKT9ejhdZsNbRMUPe9TF9hCUDTX-TlnsRvRZNh5F2O3mVhPeH8fwuCD4UaSLajoAqkbUQpNBGDFXqPmxB0ncxUJYhZGQV7RpCBCuNCGQeLG5VoqT9qid6ps5H8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=p_BfaTjjboArFGR4IaCOJjeY8L4CFv0yfP2wp3_31RtS5ATbJUHfCx7tqPqNAOgwTvWFkQStMLHu7GCSd88QhZwqGO9o4O9qj5gOAMX60CkLcjsGvsh3RnTcFuV_N39ywYkAap78rRIA0ZWT_Wh-YyU_TZ5WIwWARC5gytcOFu4Vuw8ivgFi8j-gjahDSUIb8Kl_zRODxOidVUwfNrf1QUYD4GXkWAuqHhpKC9xDOj7Yij5Ote_zJveVDFXceRQ7EMkWF9cbMHbrUKggEeLIIgPctUXR7JzSR70UmeVoUm7CYr0S5CAZ44gE95hge0b12zTmnvUHnELNP9a75Pl92Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=p_BfaTjjboArFGR4IaCOJjeY8L4CFv0yfP2wp3_31RtS5ATbJUHfCx7tqPqNAOgwTvWFkQStMLHu7GCSd88QhZwqGO9o4O9qj5gOAMX60CkLcjsGvsh3RnTcFuV_N39ywYkAap78rRIA0ZWT_Wh-YyU_TZ5WIwWARC5gytcOFu4Vuw8ivgFi8j-gjahDSUIb8Kl_zRODxOidVUwfNrf1QUYD4GXkWAuqHhpKC9xDOj7Yij5Ote_zJveVDFXceRQ7EMkWF9cbMHbrUKggEeLIIgPctUXR7JzSR70UmeVoUm7CYr0S5CAZ44gE95hge0b12zTmnvUHnELNP9a75Pl92Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vITmj62oXctYBQyYOlsZ1CfirB2s4nbhVD3QPPWHPbe0vjCnk1xiLGo78KOPoBy75P5kxWxZ7VyiDSO-HZkHCJrG0Qvvg2N7zch4pKuVqFj4WnV78S0lEQR7CZfPX9lZDQHRjcXN6BdD7k9XOTwHXsFDqXp7S6xM8Ven09TYihX2AP1Mu_NldHsAEAfNehH4LTLF0TpGX3fSARMNG9RfXQnwf30KOQ4Grl8VAzuDiO_4oqfK8bKnKoWhmMG3AQuYWIL6XJCJKCCx3WGLntI1z7ehghMxu8J94mC5bRFhJ3vTHRFwBANbX6181dAqUAXWzIuiZzdTKUod690vceB54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG8z-FpZyNCSR0gof80LjHwDrfqPDoPDAq_Elfe7xVs311O9UXE9Ovcne525-dxmOeek_Jm_wJzCyiKLB4XqS9kZC96w2jHcnntIutBRzdRJ6-Cya1GY99EcLW9BkGCfJxJakSNmoySjm4QZjkh8WLtFevj25fviPzbiFn4OoqwjOGnyrNQ1SJXwfe8-qS83CCZHprqxX15ZeyD0WVyjep6fGyTh1IUGjUUsrOnvy_kvGsjC786kn4goOjO2Uq5kuMtAbnpUVEseDkpQ3oeMHqrASEi2zHKvMNuZY1SKr2M2etalV9LsV1qzJwsB0fE1WtjatHa2mfgXdKdE-i_uMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiKtX8znBLW-NsB_frUzZhdAodM-xhVW-quhveRhU_N-M6y2EPDJzxsMQ4PNo_BFkqXpuQy9niWnytmM1uqqEcbMSjCGHICcpUY7l3mVxBHDccAVTgM80AcNoiaTYJ5cCZs5sAWdt4wwe56Ru8NeYyXzWOvrCVz6mJrABlmrzM10sOHnK9PIlAjnN988dYnxEtfzxN2avTE9Ws496dXD0zZrwMprcuPrZXlFBEs85d9Hc2HL4DtDs6eSMG9LfB7_vEPBVmZPWA03ejRl27BpmNRYI98YNG9srqtyg6RrxjKJgq9S-xpaw_oCtrgRWn7i7kIw9EydhPG9BxVMG9iHuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlkpxkcBwQNK24TjegPJZ1YQcmZRMGyuRfrStay-dtJYpjN3LbcwQYJ-fFZcuSVcL-aWgLs2CT88QPUG6G4oYEx1aazhGPmQQGw76zCucPwr0MOPzFMBo2_T7r1WwC7nZkZuRm7_XfSuUFjZmrtoRThmKHcJakS5WkXi-OniDhjVYQiAIrahUTm2-p3cUVipEl-DYi2xh9KU1ce17gLEvT3-VJSxPPiwzHfrwgbCutogcDOcSvFKg6EwLoU3ewqyDKwbRJVwdq1siLDiDVjV4vlMbJG1GPukp87n3I2GTab7CZsZg05pHutChCUGpu3uLUhmLwZfUs9q8EDFN7dB_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=mJyI1rk4w1DN7HWSQM_Vfmu96u5CIq2KC1zKRqLCdPBOd47NWAFIIBVZEjWoX0qUMdlzqDxI1KhdH0V6oODhYNFY381owuOqqekQ4i0QgRAt1WM3F1CBTZq3VXd5pks9ilH8tmI7vwFubOtmJB3ZdJBg2T3XnKJZ-PDhlOrWBFYLFg785Dug5Kx-6NEx1jHqRcM3uxms6iyAbhwd4Xwx-bCjYHu4wo5SQy9CDPm_DzLN-Xf_mtoHnXzC-EXbN72Q60CRGSvl86Zuck97CQceqMeWe_1sWUXWQEiUkdb4tkBrZzadlVMZpW_UatrjKmb0XnBBKjerR2HU7v5E6lF6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=mJyI1rk4w1DN7HWSQM_Vfmu96u5CIq2KC1zKRqLCdPBOd47NWAFIIBVZEjWoX0qUMdlzqDxI1KhdH0V6oODhYNFY381owuOqqekQ4i0QgRAt1WM3F1CBTZq3VXd5pks9ilH8tmI7vwFubOtmJB3ZdJBg2T3XnKJZ-PDhlOrWBFYLFg785Dug5Kx-6NEx1jHqRcM3uxms6iyAbhwd4Xwx-bCjYHu4wo5SQy9CDPm_DzLN-Xf_mtoHnXzC-EXbN72Q60CRGSvl86Zuck97CQceqMeWe_1sWUXWQEiUkdb4tkBrZzadlVMZpW_UatrjKmb0XnBBKjerR2HU7v5E6lF6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Xto9hPQRSQO7rjj7aOJX-N1XmNuwGiZ-YxP4sNFwfoM1Wsrnc3W00pUdqKvO9G3pzM4O5tqXIBmhCzssZDpU6ajwg4TqkgfW7yzYeLclRA1-x0GgxbEg2n3NwlCW5VJq1aF386SadCunWUNcSbBsK_BfUP5vfd4WBmUNjQIWZzcA7XfnMKr5fXatdOy2ejpGR4hacuy3t4kLUTHg8SbqUYuW0hMsTNVrezwnVbm3koLD-5GYR_nQnSZ-whbFXkEwdhx2bDr_F7fB0yDr2YhTKSNar8Y-9gQp2l9eeIwaZTIp9wruimjS3y_G6xiubRyYjVk3xqZ8WL8WHqGs2LMwyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Xto9hPQRSQO7rjj7aOJX-N1XmNuwGiZ-YxP4sNFwfoM1Wsrnc3W00pUdqKvO9G3pzM4O5tqXIBmhCzssZDpU6ajwg4TqkgfW7yzYeLclRA1-x0GgxbEg2n3NwlCW5VJq1aF386SadCunWUNcSbBsK_BfUP5vfd4WBmUNjQIWZzcA7XfnMKr5fXatdOy2ejpGR4hacuy3t4kLUTHg8SbqUYuW0hMsTNVrezwnVbm3koLD-5GYR_nQnSZ-whbFXkEwdhx2bDr_F7fB0yDr2YhTKSNar8Y-9gQp2l9eeIwaZTIp9wruimjS3y_G6xiubRyYjVk3xqZ8WL8WHqGs2LMwyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=WBwIkz7md321McSAq6Ad_lIVMwnNIPr_DLu72pDOIB9GICsyZANadtsPBRJSlxy3an15h_q74x2Bvqk-mI-o8yNEF6Nu6HNvk8Mkk9kAUoM-TQnFZBdDxMHzBGgIUTV9lv3TABVCOZtmkr4dSGP1dhwXzLVB7RbA2z4x0FbAKhPLOt5_jyJ09JcBQZCJZNHr80cDBGuKAofIYD9FwxpqTD96Ci9apPQkb4MVQUaIcTVpeneq_Hc-Zq7K0jwuAZ1jeyyibgcaXOz9XarNgNsSkI3PROsAvj82AM_aBpcXOvtcQSzWDh4a0o1Po1u_9GlaD3z0hO6mkJPsIYOq_1Z_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=WBwIkz7md321McSAq6Ad_lIVMwnNIPr_DLu72pDOIB9GICsyZANadtsPBRJSlxy3an15h_q74x2Bvqk-mI-o8yNEF6Nu6HNvk8Mkk9kAUoM-TQnFZBdDxMHzBGgIUTV9lv3TABVCOZtmkr4dSGP1dhwXzLVB7RbA2z4x0FbAKhPLOt5_jyJ09JcBQZCJZNHr80cDBGuKAofIYD9FwxpqTD96Ci9apPQkb4MVQUaIcTVpeneq_Hc-Zq7K0jwuAZ1jeyyibgcaXOz9XarNgNsSkI3PROsAvj82AM_aBpcXOvtcQSzWDh4a0o1Po1u_9GlaD3z0hO6mkJPsIYOq_1Z_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=q3zTT3Zvgl3Zsvq5eAG-0kYeQlHi1ovi47ThmUPFoqNC-ve_hSGNb9DIfD_eXlNHPPwCT0JGxgRYwqmgfK2-yjE0HkvJ92ssG5sIqCQnRjF0wxR0zpeLebjv_yZDnME95FTRFg3N1IWYVqyjQLgY_a3Vh7hYGiPYV3Hagpywnpy__cjLXvgmY7H-WRcX1En5KNjQ59IX4BxqSqBa74GgyrMRizqtd6JrK3eYTTLOICY84wELbcrQL9OAddJYLRM5w2dr0l_ghvTurpTrQ_51PR4rK5CIlak5CYEC0_wRQIq3ApCpp-s89vHF6HGUk905nNjHJY40meqgeQS5Ay5ovEq4_6n4_Gpoi3P4zZ6aRF_6fJXaQ2ZITYeBgAzThw6SnVnw_Dosvhk4etwURXjLhm7YCnXkY2py2wjXdWQfc6yLSgMWlQLfoXdVNVappT3FxtQYXtqKCmn0JTmq5BVYya8fWsL1vay6afFa8IzsCsrWinN3eQZpsXBYX117POphWuxuh5ctL3yDudKr6odBykWXgKZ5OnMBXR1Z8haUwBYhp4SixC-lrwSWj2yeT7vg62w4t2yRt6t79tqOtodBLbyjpripH-s3A2-9O-rQJ9Un_ccXUuhWikzr7EwyRJF7d61fFGbGP88UMdkkVF3M5WwGx-krcp53AgMxXPX72sY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=q3zTT3Zvgl3Zsvq5eAG-0kYeQlHi1ovi47ThmUPFoqNC-ve_hSGNb9DIfD_eXlNHPPwCT0JGxgRYwqmgfK2-yjE0HkvJ92ssG5sIqCQnRjF0wxR0zpeLebjv_yZDnME95FTRFg3N1IWYVqyjQLgY_a3Vh7hYGiPYV3Hagpywnpy__cjLXvgmY7H-WRcX1En5KNjQ59IX4BxqSqBa74GgyrMRizqtd6JrK3eYTTLOICY84wELbcrQL9OAddJYLRM5w2dr0l_ghvTurpTrQ_51PR4rK5CIlak5CYEC0_wRQIq3ApCpp-s89vHF6HGUk905nNjHJY40meqgeQS5Ay5ovEq4_6n4_Gpoi3P4zZ6aRF_6fJXaQ2ZITYeBgAzThw6SnVnw_Dosvhk4etwURXjLhm7YCnXkY2py2wjXdWQfc6yLSgMWlQLfoXdVNVappT3FxtQYXtqKCmn0JTmq5BVYya8fWsL1vay6afFa8IzsCsrWinN3eQZpsXBYX117POphWuxuh5ctL3yDudKr6odBykWXgKZ5OnMBXR1Z8haUwBYhp4SixC-lrwSWj2yeT7vg62w4t2yRt6t79tqOtodBLbyjpripH-s3A2-9O-rQJ9Un_ccXUuhWikzr7EwyRJF7d61fFGbGP88UMdkkVF3M5WwGx-krcp53AgMxXPX72sY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=pKwaBymFxvEaUEQvq5gm3O7FVimJaj_2bE0OcLEmQrSI9PUQMZ3Jnp8-Ke6xylcYwEINOnDt_ziynDEoqe0GQITxVzjzqTOKc-OiOkHGmh2DopgWUVvC6Dz1cc8w_AVIWnOkwip3Ix6xX9PoqOPQKMuyHABiQ9rXHk1RNZRg4N0-cNuR_IZXqispBMKIhbXG1rRXXS0JIGd1sM3qEmLgFMwRbzM1ekgMIBCFYuAOgpyYvHgYuKMrstSuYZtAw--ecwsFfUcjcb7dS1jzenDVFOjYiVIuSLyDymm1LRy4qXeaePwXUCCALeXHmz_xwHJL0i_N4l79x-7u_Z-ok6qbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=pKwaBymFxvEaUEQvq5gm3O7FVimJaj_2bE0OcLEmQrSI9PUQMZ3Jnp8-Ke6xylcYwEINOnDt_ziynDEoqe0GQITxVzjzqTOKc-OiOkHGmh2DopgWUVvC6Dz1cc8w_AVIWnOkwip3Ix6xX9PoqOPQKMuyHABiQ9rXHk1RNZRg4N0-cNuR_IZXqispBMKIhbXG1rRXXS0JIGd1sM3qEmLgFMwRbzM1ekgMIBCFYuAOgpyYvHgYuKMrstSuYZtAw--ecwsFfUcjcb7dS1jzenDVFOjYiVIuSLyDymm1LRy4qXeaePwXUCCALeXHmz_xwHJL0i_N4l79x-7u_Z-ok6qbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=amVb2yZEgut4NJ-1YEUsHDVguD2tns0iWNgljY4_oWcpxVvdjriBIcvTpLbvUFSYiVrkZkBuajtFfPjLPEp8Fpuk9MmGnBO-_dpPrqXVEa33Axu5yGXb0UR7gaisBBuhWQX8Vuj4TTwhXvJPfSAWZB_618sRMgcQpFS0aw0aEN0TDfelKmw-sjzuduDFv5YAAH04C_x-MHFE36VTv7_2yh7KLxS90OJGb4OPCA5_QozithPVVT93ai9aXDin5Phdkpit1RONGTbiXFAz_-_SwNibW5eyQt0jnH5WM3nQ3DKdFI6VtN66OWDSjQuSoK2g2jhgJLj91p6fK5vl-dA7Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=amVb2yZEgut4NJ-1YEUsHDVguD2tns0iWNgljY4_oWcpxVvdjriBIcvTpLbvUFSYiVrkZkBuajtFfPjLPEp8Fpuk9MmGnBO-_dpPrqXVEa33Axu5yGXb0UR7gaisBBuhWQX8Vuj4TTwhXvJPfSAWZB_618sRMgcQpFS0aw0aEN0TDfelKmw-sjzuduDFv5YAAH04C_x-MHFE36VTv7_2yh7KLxS90OJGb4OPCA5_QozithPVVT93ai9aXDin5Phdkpit1RONGTbiXFAz_-_SwNibW5eyQt0jnH5WM3nQ3DKdFI6VtN66OWDSjQuSoK2g2jhgJLj91p6fK5vl-dA7Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPmV8Lh_jMBzv1NBmKJWLHjlA7hbXRbpPiZA3tYjzJqwy7QEU0oyU_8Rn74FLwNz-LzvwNTgr951J_eAtzEdavMgCPFCgUAusDbakU3sjvoKXIBtTNG-qwOTZydN_rlGFdgGrhFbUnJv-HTxcdJ3PYQ9kqrIO72bnQLoh43U9C2jVck4mVDOMG8xOhoHRkYxvb2sUF0-jaSx07n9PPDsP1KZquyrfW2O3qBvz6bS77OyjABrb9bj3NE8YE-HElEqjGwnQS86fNpGV_LRSnSSzkE-PP8SgQtTGBO5zrIwfdBLXkO_aA6O4-r4YIekUaUqlvUnW4EjN2VmUC9ogZUVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=QwbWC5eGTrdO8fhSRSdF9_k9goakIbsJFPmEbuGbmqlMEP0xuDUrgC0OEAkKMov_-t1Qk8qsTq3BLTwt_CTRxegOM73p0jFiH_B2jZE2zN9VNPZmcRuEWLQ_4fupifMlZ7-TgRFK3ZOY0WrKnRv9WSes5tLh31xjI98bjarV2-DVhTLXcWYp6djwnHgyC8xgVmt63wHCzl9Ud9gHxRHC9gOd4nYyYxfGCrA26o0P6glu-vheYVyGEk0YbSNu124fxf8DjO8Osm99FAJWX7HrYeA_bl89w1yQ95oMCzqHO7oVIv8iIcLBuX1cxF2zEauGec1lD9u3NE7aFOiCsLAgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=QwbWC5eGTrdO8fhSRSdF9_k9goakIbsJFPmEbuGbmqlMEP0xuDUrgC0OEAkKMov_-t1Qk8qsTq3BLTwt_CTRxegOM73p0jFiH_B2jZE2zN9VNPZmcRuEWLQ_4fupifMlZ7-TgRFK3ZOY0WrKnRv9WSes5tLh31xjI98bjarV2-DVhTLXcWYp6djwnHgyC8xgVmt63wHCzl9Ud9gHxRHC9gOd4nYyYxfGCrA26o0P6glu-vheYVyGEk0YbSNu124fxf8DjO8Osm99FAJWX7HrYeA_bl89w1yQ95oMCzqHO7oVIv8iIcLBuX1cxF2zEauGec1lD9u3NE7aFOiCsLAgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9uAS8jZ6hpVPk4TyEx5BiPItvehRCyya6-vGinF7i8vFs3FMXIzsDc82nI3dNBhIQ5ACORBedlyMQfl3l8OM8MZVUMaAS4_e8HGz_rfjQan3sZGQ-u0wgtmUyxpEdn9TmqkGjeKehNSV9_Ch9YUW363-PustABIyamFLT2k8RRQkrrFVjmaW8gV7ezVX9Hl5xjoqwa1ZsNOvuXiTuzSERCzeR5H7voVKhTy8t2-LfoIHhsmGMyPo_USl571a657UTpXvTM_YSiPKoMNWuruwSKIBwdH_PdVTiDnephrkdtg5GVritZVkRaT0Ns_OjgTtKtGYsz6k4Zq5qzCjW2jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
