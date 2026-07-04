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
<img src="https://cdn4.telesco.pe/file/vq2zfOw4mPPnOWZuLtaXgJGMNAJXzLnWgw-dasAxcdXdrl6dBkjHJTgPJuUU9dgC8iInGxljxXYR5TvdMnfSvCBtEeK57dXd_y3-vQc0-GcBWquolFA1-hPXkAWnQKuHpifQZwGMRBYQ9MtNn3jj27a7HIDJzVg53CBRg5yjr521o4f0yG5cgwScjJD-EdB7-VjbnURBQjgSoFXvmv6pVYFyEaeqlxDj25Cb-XRtytwb5FriaIOj1lUOI-Aci7Ru5_Ct7DdP3ZTGwl9LzGUff_Oo4UNEtY5i6_dap-xntqlHwBnFSzxzFupd_6S9vhaCiwqH8CXdOHdgBXMC6XCN-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 11:38:00</div>
<hr>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B46qcDMo6RYxaj-UxKkLkDM9oJWBs4YdTd2cuaciChQGftegZ2ON8BJtsJAhtasxb_TispDy_dF4vlsAxgRb33WoEDrjXyUBqJ8BxnlDp2H2oFkTzrHIqWMdib4LgGOj5clIVEBmaFu4Q7kLi68wAi26jSQ8eMffr-c7UCQE3nKGaMHI8IkH8LCUhAyLf_BA3xk6NYfFPVRAvyTp3KscA0XUsHscs4AwFq_HSOGCjQwO-Clks3Z9Q9Silb_tVWsCsf9IVvFaV9fz1KuE_vMoXrCHggX4OV9FcDePd76m4-o37QuF1WD6pN1Hc8y7nVqmAnyqK0SdZlJmKO5ZdGvRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXTjbgCJkleIVOisM6GX8PP0FVo5QKTn5h1grK8ON36GqfeBEyyofb8ObyZzmCaYM9gXrH3kwKcOCZjJZkb2CrrNzcB5Yfby1xsRLEyoLXlN4Kq2fsbQyj-vn1atMtsT2BL240C9opySd0BgdpRhuh_rhZw7NbA0wlEFlCBLX7xLKB-qDFsMttDLYu8tAAQylBiVYGOCQniM-HR-54biMYJ46A9rcifOnVaCY7d01K3dd3elaayP3X5RQjYmENp_c93CtkDi0t0CtKo_oJ-s_i8QlFsiH2Q_utYbLbditgSYnPKD_W29R7t_dgm0i_zzdsPwMwJ4stQhyk9-6J2Dng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuwvQxP7MWyGOP7Jy4AhvuaJFv9Hb61w4gpKTyBcBF6F7t1GtOXMxj-_GiBON2JVB_wwXTWfP6bDTk-g_9EMrxsq7f4sDpL2a4Ire73jXSh8akgW3hVulH-y5j7B9FXJNW4ZVZ7cqiROawcm3MNzNXVeyOxLhOmqjCm07SuFHzf82FBA2w1esHrBZkXggWWmJ9P0dZLCHUJ57ZK_1ha-X15pOKZ0lwfDLvSGeW2NbXdhMJTfg6gC3wj-OZwe4gOjgAFOTqQGiLWAjQqja_cc_2EzaMzNJ5E7jb9R2gIRvXHXojHyD1dPDBXB1vtrX8BWLbCyesP-hr5B6dBsgfy57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=v8qSdGD14Onic1sJ1CB0hiprR5DEnlFQ3lS4EdO1ZkdnJegnuewGSLOeHWSRDDTClQQxkyD3mt4TsQB8S3a7vb0WbsnmN9YtBsHt9_lrIMWHXIRhImCYz-ZgDtgUDH9UvE6Ld2MtmDfdDzO2GLOGu1odHT2wu5d2gR7a8CII-Qr96eNXtZWCbJN-Ce7Ni3Qy5BchdVNimoQxdTG9ryxdqrZMajdsp599bgAgSkttTrMfs5axTTXQc3n6WCcDqdtJHTOUBJoV1fc9EjW15nv4lFx-ZTNg1wUzVbEUFPwypfh6FjomDvjmTNoNNwbTUCdwTVacQQa11PbesPAA72qi4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=v8qSdGD14Onic1sJ1CB0hiprR5DEnlFQ3lS4EdO1ZkdnJegnuewGSLOeHWSRDDTClQQxkyD3mt4TsQB8S3a7vb0WbsnmN9YtBsHt9_lrIMWHXIRhImCYz-ZgDtgUDH9UvE6Ld2MtmDfdDzO2GLOGu1odHT2wu5d2gR7a8CII-Qr96eNXtZWCbJN-Ce7Ni3Qy5BchdVNimoQxdTG9ryxdqrZMajdsp599bgAgSkttTrMfs5axTTXQc3n6WCcDqdtJHTOUBJoV1fc9EjW15nv4lFx-ZTNg1wUzVbEUFPwypfh6FjomDvjmTNoNNwbTUCdwTVacQQa11PbesPAA72qi4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=jecmGUBr1sPp12rp8-ArKzZ0Hd3rTWAw1mHkWs_qKdyp5HNrlaqmJ5P0qvvpr67PUtgPErNy4YNefH9rM-EHjD3Zsv3k_NexVMG22IalcmhQN0bCrXb341TtdBkMeaslJqcdm0hYlsK94DNGZTm6iha48KTtN9Gtdjfcv5IPBhogsxcWKLCaa3tIbbOMOh76GxOKyAY1EwwaOgqKJGMuwFeMUffaNglQyTm2GwTINo9in6pk9CqPlCLUBq3VjYVwYzwhJsOwA49mlqbSdyhKwHvOAUKAZRig42FpMtMDDdegxEFTTf17BzLMAkAWlFlBfiVF56zJxR-VDfI_TKN7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=jecmGUBr1sPp12rp8-ArKzZ0Hd3rTWAw1mHkWs_qKdyp5HNrlaqmJ5P0qvvpr67PUtgPErNy4YNefH9rM-EHjD3Zsv3k_NexVMG22IalcmhQN0bCrXb341TtdBkMeaslJqcdm0hYlsK94DNGZTm6iha48KTtN9Gtdjfcv5IPBhogsxcWKLCaa3tIbbOMOh76GxOKyAY1EwwaOgqKJGMuwFeMUffaNglQyTm2GwTINo9in6pk9CqPlCLUBq3VjYVwYzwhJsOwA49mlqbSdyhKwHvOAUKAZRig42FpMtMDDdegxEFTTf17BzLMAkAWlFlBfiVF56zJxR-VDfI_TKN7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=qXzRLiALUPXNTTwYRPNRm6zec4HQ4hf6D9JRqrYhSxYxBintpbqEDSiF0DkTFuWF61l5ZOGIZ7zn0aWEnOGjkmsrGtxwkrSc_sfPRl6wbEQ5OAD0B4QxjDQ7Tw7rCJfvO6kPvwmd9-STtA-DfaiVPnT74ugn5ud5Wg10NYf4UIpsCfExu7EfKyNC8u7Bd5TJd0QmjulRl2U2Qtt0xuAcx0vtALYaF42yapf2ZiQx12ZKo72VyhWjyoCndkfvw639uwiF4Mbfxou4CFZsDfkSBv4tu04qizPWf3fLW6Vqv-X1S77HFqLQqaVN4V-TNo3BBdA7TRPFsgAZWiY0BPboJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=qXzRLiALUPXNTTwYRPNRm6zec4HQ4hf6D9JRqrYhSxYxBintpbqEDSiF0DkTFuWF61l5ZOGIZ7zn0aWEnOGjkmsrGtxwkrSc_sfPRl6wbEQ5OAD0B4QxjDQ7Tw7rCJfvO6kPvwmd9-STtA-DfaiVPnT74ugn5ud5Wg10NYf4UIpsCfExu7EfKyNC8u7Bd5TJd0QmjulRl2U2Qtt0xuAcx0vtALYaF42yapf2ZiQx12ZKo72VyhWjyoCndkfvw639uwiF4Mbfxou4CFZsDfkSBv4tu04qizPWf3fLW6Vqv-X1S77HFqLQqaVN4V-TNo3BBdA7TRPFsgAZWiY0BPboJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=fk-smHdSeeP3y4wpcZ0Q245pWVI0EuwgdMFB-SJGSGtGFGUe0yU4-bpEJ15fQCX90ff0Wc-cCCi8PKaFPau0Ng43zvs3OdT4CyjKrmiKPuCzsNoIGDewdjwkxnM08eK68V5J4FjZPze8s3ywZKUD0m2vNuc7yt5U4P24iOr7Q1c-Syk19nOQM26AxFvsKMmz6nDhiD42OzJr9cczfTAtWQ3EKZQNENifcu5HBLLJOw1JUqn_PZRootVRezQBn0aDBvuzRNIE7IsLCwGrk21ZWFAeKoG0eTo8s89BMfhM_KWRkSnAmIJ38LHzxIm7muQDZy_-dammSTrbAvOniGuZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=fk-smHdSeeP3y4wpcZ0Q245pWVI0EuwgdMFB-SJGSGtGFGUe0yU4-bpEJ15fQCX90ff0Wc-cCCi8PKaFPau0Ng43zvs3OdT4CyjKrmiKPuCzsNoIGDewdjwkxnM08eK68V5J4FjZPze8s3ywZKUD0m2vNuc7yt5U4P24iOr7Q1c-Syk19nOQM26AxFvsKMmz6nDhiD42OzJr9cczfTAtWQ3EKZQNENifcu5HBLLJOw1JUqn_PZRootVRezQBn0aDBvuzRNIE7IsLCwGrk21ZWFAeKoG0eTo8s89BMfhM_KWRkSnAmIJ38LHzxIm7muQDZy_-dammSTrbAvOniGuZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=P05kncIb0h7rNj_N9SSE4OzWS0pgnXQn88GMZEf6VaoOysO67rK7BOq16pRzBeuIegPVzFAuPv5OC2P1I5IPXgA_Rj-PD_B12P4IUU6YxH4dD3QCLk4yITuBBpXxNeq8YoFg89VjIXdHqbawlBVIBllnHoBQZeAvUkumsg8kDQ2_281Zt2oLQy_3birxmNQWo3E2r5gLB5K7WieZtNYStc42VMBT5B81cQ6ZIZQ1xGu-0yI5hxNKjpXPWOqPi6BkMT8g1UgiZhezBm_9ICt1lG3EenHjeDgAjCFHsne8s3nho6skJzTW9-AcA_NgnD8SFPcAzluTHnvc7LcxQPUS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=P05kncIb0h7rNj_N9SSE4OzWS0pgnXQn88GMZEf6VaoOysO67rK7BOq16pRzBeuIegPVzFAuPv5OC2P1I5IPXgA_Rj-PD_B12P4IUU6YxH4dD3QCLk4yITuBBpXxNeq8YoFg89VjIXdHqbawlBVIBllnHoBQZeAvUkumsg8kDQ2_281Zt2oLQy_3birxmNQWo3E2r5gLB5K7WieZtNYStc42VMBT5B81cQ6ZIZQ1xGu-0yI5hxNKjpXPWOqPi6BkMT8g1UgiZhezBm_9ICt1lG3EenHjeDgAjCFHsne8s3nho6skJzTW9-AcA_NgnD8SFPcAzluTHnvc7LcxQPUS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXxSDLlUePGQsu6_bHEPLaz7rerSO839oNpE5JzXuURKpLtG1ehiTDDqAI58tbtaezQTzTI0YvGWknhYJxP3cv43t65JSviH0rhlDsupU8KLRifmakRQWpOwabJAa-IL86VCvUEoH_2nPexnOeBjuo1s35L7ysIWf5rT6mRjUxac51Q4vtUrfberdinlpAGEYDWKGyGdQrAKhijZGz_HCyTtKtFBIYUxR4r-F1QFUiSUYAFjRPPJzcP5PYSbNbzESqt9fSL_E9CGprvMjo590bxhismlq0oVl3ySAdeEuLt9mCNfwC2Mx31TyFrVAWqXAibFiqem1K15fSRaux-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=Gy2L97td1oZWl5pxWeLIiBZ6xAZRKtav9XVpgZF0srKbRS5f9kcYzayXQd4SLy2WmiP8HKziDdz7OfmI9-jbx8JYCNNHTZ11ePqPNlEjHJnNxUCgguAq_OvRf56K6XoFXOBkcLWLlLzvlj-ZZkUYcWoSsYOR8Yl5c_FVOB8if4Oh_cu3mPiMtDn8cvV5IGtKsmnqN1iZIc9axpt13Eq3HXMIwgbgi73qGHJJk28vD8o9frx3u0x-_xpcVAtuVFYub_0CUe0cg5lcOFDduKw2l77CN0DOvN7fGFdz-GmUdQUigf_C-Jgk30zyARDGbp6qkShEF6uCpg4S9WjPseQDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=Gy2L97td1oZWl5pxWeLIiBZ6xAZRKtav9XVpgZF0srKbRS5f9kcYzayXQd4SLy2WmiP8HKziDdz7OfmI9-jbx8JYCNNHTZ11ePqPNlEjHJnNxUCgguAq_OvRf56K6XoFXOBkcLWLlLzvlj-ZZkUYcWoSsYOR8Yl5c_FVOB8if4Oh_cu3mPiMtDn8cvV5IGtKsmnqN1iZIc9axpt13Eq3HXMIwgbgi73qGHJJk28vD8o9frx3u0x-_xpcVAtuVFYub_0CUe0cg5lcOFDduKw2l77CN0DOvN7fGFdz-GmUdQUigf_C-Jgk30zyARDGbp6qkShEF6uCpg4S9WjPseQDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=KHVPPEt5qSsh3WLxn35RhaGSdNFQ3RaTJOmJ8-Cze8SyD6jbteV-oQitjqg_HZlEuGqnLIhb1GEWIJPbxMlSg8Iv-WKmzX6eRdv48NW8R1XiwoIqmBfTPP3vVw68wrA1s-reknqFu4sVU_A56eMXfNlZOgb5xeg0C17e-_xVpyuu85_IZafjX80HIQ3O4SKyCjpA7rvuRxtnGNxbfY6xTYmcrwqL06dPcHQRwEKQwKQ9RYbsVautg9sd4an6DL534dWi7KJZypxA8LyYZodduX2tDexfxErGoCyxwqPnGCOEvPcTsRV57TCZxtvBFwYmQ0rWXYc5-fGdePIW875BNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=KHVPPEt5qSsh3WLxn35RhaGSdNFQ3RaTJOmJ8-Cze8SyD6jbteV-oQitjqg_HZlEuGqnLIhb1GEWIJPbxMlSg8Iv-WKmzX6eRdv48NW8R1XiwoIqmBfTPP3vVw68wrA1s-reknqFu4sVU_A56eMXfNlZOgb5xeg0C17e-_xVpyuu85_IZafjX80HIQ3O4SKyCjpA7rvuRxtnGNxbfY6xTYmcrwqL06dPcHQRwEKQwKQ9RYbsVautg9sd4an6DL534dWi7KJZypxA8LyYZodduX2tDexfxErGoCyxwqPnGCOEvPcTsRV57TCZxtvBFwYmQ0rWXYc5-fGdePIW875BNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM--pm2aXLrUwexosohD-Fm4YjMX7R9A2ubF8-GPuyt5hisIIlhVjmO2JyLqhOX5Oxz9zIOiffEqYjxyACjR2MPoGsBA2t6aSIRsjpkcml2lZ17RupGxeaWeWzu3Pfe4EMiKamhzq1aN2EYuM_lnUMJcO1rd9sjJr-t0-1sidfXzRn-57eLvw3N91TQK6N3SJ_F2qP1-iKdXEjdcbqtAWFmSovuWHjpYKb07epUTxesOJe38uH6QVYca8RY6duY-0koiH6LdM_ZSjCqvVPSdx1g28fHSDD4xRk1pwyNvDpaIe3KOXDgOoDqgH_uYQCk7zaoRz9E7tvYI96OG-00vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOpDUgL7BgRgOkqy4jb7QdzAU7mFEjK1zKzusFAPf1p998ztN0LY6YyJ3f6pUuKcTPB7Ce9tit4vQpzILhHll6ybAQad_QNR0nkA-u8sY_dUY8tegmfO-tNVgNoYukMKWiL9QePkZ6GpP7wrUF-TEBwL-Fjxjo81LYDZHM8s9-KFtHvolKuB-WWuwU5lZrwj2Z7J2iH8BpOK_Ec6x2Dbw-wW4fap7reuAhxcQAb1i2gM88er6MGA1wL-NZaV4cP3q6PLTKOoFLEuuqFPD4gV8pEutgHU0YW7m4hHTHKAwcTTZOyWIayw8r9LhpzpNfsWVa0mUBiLORvQszZ7Ht0NVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTzyRrOMm2FTkadtQafrkP7Ne2QlIwLGEoXhfNe4Jq9TbHMLSm01kJxTu_M30GkcDLxcmSzjUQs70gB5y1TGaBp0tMHa-vjUqapzuMBaXHRl6ZbQvZLFrda6h8zNTCpz7GHlYvPxkxV1NQjH4MiXASXKEPFfpRtMAfp6y9-tX1Ppu1x-IfigfsHX53ik9R8H9QDOtDBiyl0MhRLMm2okSdHl1NIUEiZ34hSB8Tpsdmhsd4xI2cHC-VO21Ss_6uFbHG-nMuG226EWwVF1zLjhnkeUkUJhuLfnt_TbfsV1qvvBZohNAzmHw6LG5DoDUqKes13OzEj7iNZ8vYqZsvaucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqQrR0O1bUGwYk1tJYs70kevtbC55IbG-K55QcXaXM89SXUtz0fmCNlGmst59ahSQs9jHhljrDtejZIB-rkpQEAiwdiOLBe92FKvkW3lCphnrJ2Gpmb1zZS1a-ogLBuxqTajXzSj_poXI7UmsRGU_4_E2SZvdhmY8a_HnhKWR8HF1cEgbpm-RrpZ4LgM7NF7KG-Yfy1sBtZLAVKjHQtnN0VlbkBcLLGZw8hzF3AW2R3BmqrlutT6TMLJQRYeRd26-GK4tv0oqgUvTZqVKXuCnfjieomUxOSfWUuUXXiBnIyFJmy0aAxwnfu5H5kH1CudLZbTgWUebxhPOvvRcWWmaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0rrUHF313rrzu5-NDf5yYfVvBpUd3ptvK_buYhSCHrFWMXyUx7JizTLmWZe8ERMRClS6UZ9O5ZItT1GewJkRd5nRBtes59lJdaPcWFhfZdiqEPcbdRTIGcIPMyCBVpMioKELFGr4m588cNnRvZYvk6jCBM6Svl1pEucgQg1zmnve_GjLsWUp_GwJ_F0l4iFzQi16aDmDvNRCwVhVuWKLJ8vq53OjY39U9LkEBj2p8MLQY9hU0eqWDxKN86aAkQidpZ9jryX_K4Ego9RnYOOUAu30_j7WZFpzDXiNwnxW5UatWOmsYyTwQMl-C3_Pl8nduzO0eNdFwov0YjX1aKndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngg62cNnK1Px-Z5h59jP39dYz8u51VaVF75F4-UhjPdDWDtX-_LJXlWyTfw8q0PIDbwBldtwHlB9iiHTSiwyoVqT-assey2G_WBUxHk49T-sE5kkJXW0zpwG-2ePSzs9tuCkB-YucVYiZoKDzx1pF8E28H3huEM_g1Xz0fmkKVwr4lnLvnHy7fOVpvER8BqAmQ4JsMFVIbVFz2p64V2Xu9iX0RwNW0GmvZKD7P2HS3Z6cGdFrCBV6Oo8xSffFUB1yDq33paQQIJ9BG0aSAho-0XJfOfp3E5h3p95dqNBSsvCxvKeNAqwT3h6wu7XALBxHju8QQmA2jFjJQEt3RJXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p89QwURns5GQN4srye9YaxWT32tbYzsRGQmBLHEhaomG5Iwes_92PbKBzFlMO8JbPw-GWsCgN86Oo4kCY126H1rG6yYiwvmA8t4zxVAIlPEJtsSO_jmw4CZHGAWW8NtLprU9OT9Cv9wPP-11LpQ8E4tWjt4_xpfO30wlrEwuL4ZPDsYh2myKOQsVIAdlC2kBydqHnEouWSeGTgOhP_F-Ab0DJFCJFSWaWhydXplGx8Fb_QJ9MUWTfqjzSSEdBn_13ceO-u8kENn3wvat_J6o6G_vXoxLMCWy66rj5xVjWzMLuVmjxbUmDZviuBCP9gMQMUKHfH582KqOTVGQ2nxK4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLJQHKnWLKWoaa2AsYYSuDfo8cgcgDIzwLlW8Lzn5VDKxvWR-K7g2nw--llWgRqf8y60shJYs15esOj_-sE4g6-aUtE4JZzvTTEicFd9Cd2f1ZPpKaJu_PjGXsblA8KOaqG44fBt1d4vAqE32cKokOcAgrsMmIPOeHQ2_sRiGgB2ibegjSZIPs_6p1LFETwPytietRAddfG21YFsP6VSkqtdlwjVCBr3ImH2XpXv-fAOBeAYjUEUjsfqTkgmuR4ogSkf2rnpWGtUnC7_1TK79EgSNDEPtmn8tyFQCq4r1yWtrzyw9LQorqyb7WywWuiXh5qQdtcrO9gbLgpim8NmtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=C_utPIdBB07lyBgl6kkgZQ1518f2SsdG6icusbfWCYmaf11V1-u-bh3oEoRs7l3X_VFnX39ejak6dOphaHSCTuIjVo41dM34bIgFi91fQuq7x9AWswJJVrwTTcYLuYMn0cyDNSThJBHHJcpiOb4EzbtEX67qjX-d3kcAACdgkReGlyN6PlmA-Zu9Xdm0Sof1MnQWbJGX3muW0vAgzL4wnpbnkPeCilvOoFjO1rkyd_KyQCpCkdr6txCvbMHej_Skfbze07LZlSep46Ybwd0i82fUZbg39mR8APN4ps5DvbxgKeiUKC8XS-HXqZDCFXGtHL1XIMM2hAckTQs4d4Tplg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=C_utPIdBB07lyBgl6kkgZQ1518f2SsdG6icusbfWCYmaf11V1-u-bh3oEoRs7l3X_VFnX39ejak6dOphaHSCTuIjVo41dM34bIgFi91fQuq7x9AWswJJVrwTTcYLuYMn0cyDNSThJBHHJcpiOb4EzbtEX67qjX-d3kcAACdgkReGlyN6PlmA-Zu9Xdm0Sof1MnQWbJGX3muW0vAgzL4wnpbnkPeCilvOoFjO1rkyd_KyQCpCkdr6txCvbMHej_Skfbze07LZlSep46Ybwd0i82fUZbg39mR8APN4ps5DvbxgKeiUKC8XS-HXqZDCFXGtHL1XIMM2hAckTQs4d4Tplg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nkFh8MK7ypJp_4BH90Qhto0z1gN3EnyxM5JEniFggw1tXIlFUjRjV71pGbuDuxalDew3a77NpqsNBmtmHvYRGGa1Vs23IvMMRhz3CxjSPHKxko7i5i77Z5Aaj613dtpcFndNbP4quQsvpzLofkrW03h5L4AzwqBxhzcrkhSH3CJth4XXaTFQaajLKd_ETggIzmmAz-7G3k5fXKWUR5hgu-TCJW5YPJ491E5zPCw4kS3SYr3EUt1oT8aXb9AwU6XEXOEuokjUJ2REUYlacUO_Ypcx2fPvf_1AnoMgdGfGsnKWOyxgPDscUxpsbDbxdepr7ruRlVE_WcfhZeUdgAiQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nkFh8MK7ypJp_4BH90Qhto0z1gN3EnyxM5JEniFggw1tXIlFUjRjV71pGbuDuxalDew3a77NpqsNBmtmHvYRGGa1Vs23IvMMRhz3CxjSPHKxko7i5i77Z5Aaj613dtpcFndNbP4quQsvpzLofkrW03h5L4AzwqBxhzcrkhSH3CJth4XXaTFQaajLKd_ETggIzmmAz-7G3k5fXKWUR5hgu-TCJW5YPJ491E5zPCw4kS3SYr3EUt1oT8aXb9AwU6XEXOEuokjUJ2REUYlacUO_Ypcx2fPvf_1AnoMgdGfGsnKWOyxgPDscUxpsbDbxdepr7ruRlVE_WcfhZeUdgAiQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=RwxHQuU2ft2xk1DCm-lSsz7c24miv8EIh_puegeLJSfvFbPXr_KNJsqu3F5MnPkM9WjiBHcL--JwsMzlzuNyAE2YwEBB3ZFdEEsrdykl18Dk394Qs6IW7wFcYkBgu1ZdWu55T9PE4HG2NsUQZ1muiMkaRE9tCyjvD29KCe2Qsh0iG-p3jLbvN4VFaGhEklACO95kViLJ6jH5CgF_iCgyjwbMT9ubPQigKhcGn3-cvjAw8eL7sxlLoGPAlG1WM5vn-BPvG5yCLw1ESWrx0mAQIu2j6LsibBxZ1QPDeSXalbAPH7hcpLzj4UczJmxSzF5mpzvahIz8t5pWOgjL4c-puQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=RwxHQuU2ft2xk1DCm-lSsz7c24miv8EIh_puegeLJSfvFbPXr_KNJsqu3F5MnPkM9WjiBHcL--JwsMzlzuNyAE2YwEBB3ZFdEEsrdykl18Dk394Qs6IW7wFcYkBgu1ZdWu55T9PE4HG2NsUQZ1muiMkaRE9tCyjvD29KCe2Qsh0iG-p3jLbvN4VFaGhEklACO95kViLJ6jH5CgF_iCgyjwbMT9ubPQigKhcGn3-cvjAw8eL7sxlLoGPAlG1WM5vn-BPvG5yCLw1ESWrx0mAQIu2j6LsibBxZ1QPDeSXalbAPH7hcpLzj4UczJmxSzF5mpzvahIz8t5pWOgjL4c-puQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=j1yjZNONTCisJkMp7pTEzLTxDPFtCOgH0KDKb5c73deqIYPls_bCZ-2HrZCYOZFNMIVp2AY3bhXI3liwrZQ87tvg65ex2k4Td4QA0hPAXdAPQ10JdqlkEyIZkQ4acLaesk6ZQ5I05rcjTiTLksnGB9D6QTq_0lmr8YjigoK2e3jhTef7gTP8idztPXRr2OHWie8UMVVa57exXr4lxz61w-nZfutehxh9XoREgqFudDg4UCFspfGke0Zek0Jtfu9OpzJNjKQD-cLumNBPGIePMDwibf5BGPS5rTbkPvTGdPP2IsfAj95gCdTknM6ToI4ggmdNoKfNl8Y4OvmleFw_Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=j1yjZNONTCisJkMp7pTEzLTxDPFtCOgH0KDKb5c73deqIYPls_bCZ-2HrZCYOZFNMIVp2AY3bhXI3liwrZQ87tvg65ex2k4Td4QA0hPAXdAPQ10JdqlkEyIZkQ4acLaesk6ZQ5I05rcjTiTLksnGB9D6QTq_0lmr8YjigoK2e3jhTef7gTP8idztPXRr2OHWie8UMVVa57exXr4lxz61w-nZfutehxh9XoREgqFudDg4UCFspfGke0Zek0Jtfu9OpzJNjKQD-cLumNBPGIePMDwibf5BGPS5rTbkPvTGdPP2IsfAj95gCdTknM6ToI4ggmdNoKfNl8Y4OvmleFw_Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=bYU4APG3cXKl7dEePXmevrKiTMGyi-jqWzog7zYDFDt57YqsPG3xfvu2UuX7olw3mnAgfzYz6fxLW5cZQP2QaPLokHaCXnhor73pqL9SwVt2MyMNeiz1cwCmSKE-6RNosfooHAY0ZXDupkqUmyG6rnINMHhplplZHT9QHW9QewGhLcWFLSpbcuwF_R-qwPbGxNqtlFNwmJYokLjNcW2nWFJXWnsNS5S622VbIHeDNe-9wHyuwPLJcvZgurmoSAF2yVUWHVMQPWj4kyOMyLD5-FRpAkk48MtmALlprP5jh2Ym8XkIjZIWZODLvKS0oa1yhlL3xyjAF-9JfqL5LYqabw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=bYU4APG3cXKl7dEePXmevrKiTMGyi-jqWzog7zYDFDt57YqsPG3xfvu2UuX7olw3mnAgfzYz6fxLW5cZQP2QaPLokHaCXnhor73pqL9SwVt2MyMNeiz1cwCmSKE-6RNosfooHAY0ZXDupkqUmyG6rnINMHhplplZHT9QHW9QewGhLcWFLSpbcuwF_R-qwPbGxNqtlFNwmJYokLjNcW2nWFJXWnsNS5S622VbIHeDNe-9wHyuwPLJcvZgurmoSAF2yVUWHVMQPWj4kyOMyLD5-FRpAkk48MtmALlprP5jh2Ym8XkIjZIWZODLvKS0oa1yhlL3xyjAF-9JfqL5LYqabw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=q70CxJ13fN4gGGT3f97FbBr5dYeLJM_yOda-3J-Fmz2vq_aO2Wc981AJD7FufOVY0vBvO0ej0DWi4xAxIChflXha8rI1ON_TrnBsSlSlcAor7gshn0YS5Pvi1D4EZozKVc2rHV4a3MOCgLGzD4mgSp-2QX18KYl-qqN5iyylmFZnwij2dUEX8jFdRhnFUyfKGv9mvB5p1h-M4cIul5XP_lo7HsaRxQ8yNaVS5fmC5KOVakX13dvdvpFJEr7Q6RuyBPOL9r21NrTwC4x92UcMsSHcHofigvT6OwwImOJp84O7MFZ0mzldYhQ13niW9t_B70kIvtuKkGf0iaB1FE6sGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=q70CxJ13fN4gGGT3f97FbBr5dYeLJM_yOda-3J-Fmz2vq_aO2Wc981AJD7FufOVY0vBvO0ej0DWi4xAxIChflXha8rI1ON_TrnBsSlSlcAor7gshn0YS5Pvi1D4EZozKVc2rHV4a3MOCgLGzD4mgSp-2QX18KYl-qqN5iyylmFZnwij2dUEX8jFdRhnFUyfKGv9mvB5p1h-M4cIul5XP_lo7HsaRxQ8yNaVS5fmC5KOVakX13dvdvpFJEr7Q6RuyBPOL9r21NrTwC4x92UcMsSHcHofigvT6OwwImOJp84O7MFZ0mzldYhQ13niW9t_B70kIvtuKkGf0iaB1FE6sGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=oqkmyj2MvUYHNCcRv__qBhBa80VRY91rP0_TKaaPohIoZ616bvnQsNZDK_t3QkKHJBLrpQMBc-s5-kI-G11cIFXUsIv0D2gfhiV8aBMD-aQ11PDYw1stsnsmopXz2HLSEQOi6t8b7ZJVsHOB1nNUr5K3Z3BSwBfH1jxrN6nQWgI9m-_8yrp1fTRsl_t53BULHusGXDZcg4c4yi5StKF2TPbn_oz712f8Ob8P3KRuA6PDgP-O_NB9vrNPTtYlaf3fapE_VxrZw5lDrdZhalAwSasj8S-WtXrD-BoXGhP5m1EBLYvBFPIrJHeCsnAe7RkPQa_NAnxgaMcL3A9Z1OI-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=oqkmyj2MvUYHNCcRv__qBhBa80VRY91rP0_TKaaPohIoZ616bvnQsNZDK_t3QkKHJBLrpQMBc-s5-kI-G11cIFXUsIv0D2gfhiV8aBMD-aQ11PDYw1stsnsmopXz2HLSEQOi6t8b7ZJVsHOB1nNUr5K3Z3BSwBfH1jxrN6nQWgI9m-_8yrp1fTRsl_t53BULHusGXDZcg4c4yi5StKF2TPbn_oz712f8Ob8P3KRuA6PDgP-O_NB9vrNPTtYlaf3fapE_VxrZw5lDrdZhalAwSasj8S-WtXrD-BoXGhP5m1EBLYvBFPIrJHeCsnAe7RkPQa_NAnxgaMcL3A9Z1OI-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWKUrHRM3Vg3ZrHJf_iYVZsERdCUCe0J0YQCWghu0LZRLj6tOx9c_CeDHrN_n8Rfea6bang4fv11zwJkdQLpDd_D_PwlV9iwSViHwhCHq8XG6dFRRKaCmPom-_xt9cmkg9xsStY9l-kF9YRYEdCOxtpSfu_nMI44kcMiDV_-V0xAqhAVBKqEVwolGHgAo7cjTlxNLbANrEALnGlUvD_j-Rrosq0hu5YwDmRaV9qHtaZAXTOEIyDnumDqIKRsqqpGKLDSRP18STirrUfxa5ht94jaWEj7H4h5mpOhakNVs1-XS07_jtgz8Qa7FqDf02sHUdMwFusY3XCe2JvYrEmk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=bB34C3CqqNDLaBzlOYSP9kclllbZcVGgGbUBmWwgoc1Rujz3D50jnuhBFJof-s2tcHb6xJrkwOWIIUL6alVMTCM4bUB3sR_P2vT0FnJiLpIjjfjg_E7hic0Qd9ZvZ_ONP3sj8tWGv8FJQ8cjx8d67ZViCGYpQQarlG4KHZjM5vQnkhrqgoskdk8InQPEZG_-RTPvQfr0GRsbPys1OK35lvjp5UI0bS5fQeJ7v7YztZQYvszG_IPRwDV0f-2XHAs3tz_ajc6Jmg20fxkeBKSn6_WTEdIZFTa8r1XmOXNhy1IcfBXMw3jHd66qEOWMN7ArsLqhqfdr4kHuadFSZWK3vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=bB34C3CqqNDLaBzlOYSP9kclllbZcVGgGbUBmWwgoc1Rujz3D50jnuhBFJof-s2tcHb6xJrkwOWIIUL6alVMTCM4bUB3sR_P2vT0FnJiLpIjjfjg_E7hic0Qd9ZvZ_ONP3sj8tWGv8FJQ8cjx8d67ZViCGYpQQarlG4KHZjM5vQnkhrqgoskdk8InQPEZG_-RTPvQfr0GRsbPys1OK35lvjp5UI0bS5fQeJ7v7YztZQYvszG_IPRwDV0f-2XHAs3tz_ajc6Jmg20fxkeBKSn6_WTEdIZFTa8r1XmOXNhy1IcfBXMw3jHd66qEOWMN7ArsLqhqfdr4kHuadFSZWK3vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=UYIx4C5gFw1s7P3F7M3BT0AS_UYpROBwm_FoeSor8N-O0srCrUqhGDI01oTuPqTHqQh0Iq9IG8Qbv1b0KSXQMN9RgWE6uqsxsAV8rufsDZJ5oWnk_sgW-twm_Qto4pEkOFpNw_zz868S7A1tDTtBssmBLBgTYt8j6nh3X8JBYJgtE-23ZnE3n3JLZFRqCy02aSokkgoqskCBJco49PY8Gek_6kdDzbxdNeFp6y90cLqNeD9SC1ClREsvrk7TyOt0i4zimGDDKIe4ltcq7_no4p7mFi7XEF6ATSA7JvJb8lf-EDgWSktmUcOTpcUbAV_oGImUgd63bT0l_iMt1PSS6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=UYIx4C5gFw1s7P3F7M3BT0AS_UYpROBwm_FoeSor8N-O0srCrUqhGDI01oTuPqTHqQh0Iq9IG8Qbv1b0KSXQMN9RgWE6uqsxsAV8rufsDZJ5oWnk_sgW-twm_Qto4pEkOFpNw_zz868S7A1tDTtBssmBLBgTYt8j6nh3X8JBYJgtE-23ZnE3n3JLZFRqCy02aSokkgoqskCBJco49PY8Gek_6kdDzbxdNeFp6y90cLqNeD9SC1ClREsvrk7TyOt0i4zimGDDKIe4ltcq7_no4p7mFi7XEF6ATSA7JvJb8lf-EDgWSktmUcOTpcUbAV_oGImUgd63bT0l_iMt1PSS6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=Dsb5vjN06l_XAeH5VHhQMTz11ED3PvZjgdWS8BWrQkiITVqy3nBF0IhkfP7ocanVrdPzU5rl6j9yoQnaQAq2pUnjoV8PoAzluPNxGjs0XmY959jiToFdLj5B1ZWLT7hEoijGfEY4xZfYO8g2dpAF6qVT8qCzZGMHZqRjqns5mZWC09S8g6YDeaMotyYeY-qGAz2F2Mor_zo5ktPSRjzgMoO8Sbynu6G8QXgC4p-tm945qMhDZQNEVX15H1kJxyMmQVOpYGVmePKvFLWH2JFj4cNTMRz59FZ3kypsbBe13gsou0pK3jqrJvJ8BGDJLJQLLjLV9AKMuSpsRIiPWxhEsyqPJ7VSn423QECr1URe0KjDxSTyPAJ7p5arPqUbx3bfEiD4JAfjcKDdnVK2624_D9nU7xQNE6wgZJmKEYadPCwDrY2UA2HXdGp1upzZt8fIT022C59Ny9LqrhHwG3ci5h4d9kodsEMPAhMT7iGQUdZUAxJ7MR4Qx6XwL5oCW2wfCj3fjgDh4WAJppf2IpMMMWvP7YM6mRTVZ2Dqd4B1H1iDK7itWCOAVCDr-cJA2QnNkVOSgagb-j_cV9ChzMkFT_ekwe73Vp1cZjMdocobelQS3zZLgPVMsLeQHE9xRX0ez4GSm5a6nFEG-vQ_L19JDLaYnZjEVRIhzxbxNO3eDI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=Dsb5vjN06l_XAeH5VHhQMTz11ED3PvZjgdWS8BWrQkiITVqy3nBF0IhkfP7ocanVrdPzU5rl6j9yoQnaQAq2pUnjoV8PoAzluPNxGjs0XmY959jiToFdLj5B1ZWLT7hEoijGfEY4xZfYO8g2dpAF6qVT8qCzZGMHZqRjqns5mZWC09S8g6YDeaMotyYeY-qGAz2F2Mor_zo5ktPSRjzgMoO8Sbynu6G8QXgC4p-tm945qMhDZQNEVX15H1kJxyMmQVOpYGVmePKvFLWH2JFj4cNTMRz59FZ3kypsbBe13gsou0pK3jqrJvJ8BGDJLJQLLjLV9AKMuSpsRIiPWxhEsyqPJ7VSn423QECr1URe0KjDxSTyPAJ7p5arPqUbx3bfEiD4JAfjcKDdnVK2624_D9nU7xQNE6wgZJmKEYadPCwDrY2UA2HXdGp1upzZt8fIT022C59Ny9LqrhHwG3ci5h4d9kodsEMPAhMT7iGQUdZUAxJ7MR4Qx6XwL5oCW2wfCj3fjgDh4WAJppf2IpMMMWvP7YM6mRTVZ2Dqd4B1H1iDK7itWCOAVCDr-cJA2QnNkVOSgagb-j_cV9ChzMkFT_ekwe73Vp1cZjMdocobelQS3zZLgPVMsLeQHE9xRX0ez4GSm5a6nFEG-vQ_L19JDLaYnZjEVRIhzxbxNO3eDI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=rvLNIvyW5lR1zyFstvnwtDofxO_Amr3tvUEbuACfPoCuKtl02nud9alHPiegShE7l2OtAloJQSywrIjkaaz10aQ1FeEdRnqsPs0SFvJa_LeXmhHulSZ-ZnUgP1uZyR90xV6DV6e6AhzNJnPTl5hMYrjXSizne4m4pOgcAvRXCnOZvVq_fZuuMGK51qYJBeSfcAxxIJ9uMjdxbGiHjJatBn6Om3xkKv7qThoPADDCV3W2TCaM12SN40QwCbwFVCRWiEt7x4l2bdyFvDhKNBtE536wkwbFCufjxu8fBvzSCu1j6kNJS6JaGjj68OZEHfOfZvhaxra_dmrmE-Homvnkig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=rvLNIvyW5lR1zyFstvnwtDofxO_Amr3tvUEbuACfPoCuKtl02nud9alHPiegShE7l2OtAloJQSywrIjkaaz10aQ1FeEdRnqsPs0SFvJa_LeXmhHulSZ-ZnUgP1uZyR90xV6DV6e6AhzNJnPTl5hMYrjXSizne4m4pOgcAvRXCnOZvVq_fZuuMGK51qYJBeSfcAxxIJ9uMjdxbGiHjJatBn6Om3xkKv7qThoPADDCV3W2TCaM12SN40QwCbwFVCRWiEt7x4l2bdyFvDhKNBtE536wkwbFCufjxu8fBvzSCu1j6kNJS6JaGjj68OZEHfOfZvhaxra_dmrmE-Homvnkig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=j3lThWb6twKHtcwTKhB7jWBeqJ9LeZm2axPk2TIafKTNgOzH2S_L0Mk6xbP45oxYpTSe99Wee87ieOKRrmVxigzYoVKxdTRxOZMgaerkCrQwt3sSEOgd-7bmJ1v9_RXBniwyvJ9p1eeLInlXY76keb1iRpbp-wnGc5TUqD3Pyb9VW5WYK7mf5yYCTxY_OJQE3Q8B1SIIII_KolJL6RfdaDvBiuLYzC6LzkEdEY_Uz896sdBjzBYHCzX_OtpalVyXTejgw-1tVyZTwbq2OKSztG-MTgVlEi8lWhfZGC6yX62BO2q2mtAT8drnEXgE_h15uiUE4I7bDeFtNoiPIIdv2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=j3lThWb6twKHtcwTKhB7jWBeqJ9LeZm2axPk2TIafKTNgOzH2S_L0Mk6xbP45oxYpTSe99Wee87ieOKRrmVxigzYoVKxdTRxOZMgaerkCrQwt3sSEOgd-7bmJ1v9_RXBniwyvJ9p1eeLInlXY76keb1iRpbp-wnGc5TUqD3Pyb9VW5WYK7mf5yYCTxY_OJQE3Q8B1SIIII_KolJL6RfdaDvBiuLYzC6LzkEdEY_Uz896sdBjzBYHCzX_OtpalVyXTejgw-1tVyZTwbq2OKSztG-MTgVlEi8lWhfZGC6yX62BO2q2mtAT8drnEXgE_h15uiUE4I7bDeFtNoiPIIdv2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZfRQQtVh3vmRfiCpjU1hLLfCLHQ1aQa8dtRSMIwn73omCpcfOPinFlJgP3qllR85gjy00J6FP0wa5lsmxpQR4fMFS8bVH22djqdyApbOCeSeDtvKValWCTFNgdaDeEmutdrmQmld0RIz0mqTD7lILtLbPbSvzUJ-j-6gh31HY4uBP6bHNRSIcu5NErVlxmQtT5iSghV4w_LqUL2fTZVE50pZHMrBbqI8xgW0-ZhsgStYRNBhjnTrxQLc91T2AI6XH1RIiU6dZJSZ5gSSYO2v0kC6-QUXHww32JlJgokpxDdvgZ8MKQGotfLdfUy2roxGsurbLEH9Gp9UP7sT9J5sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fC9gZW4_urLIreH86rvBPAX2k1YSz3LTlr_epquOd_k_6D-y5Y2WVCOXrxXHFAMPovqJAhf3qE-I3Bh-lwF7fn2AipGD95GAMK6F9ZKPEPjylm9kVoiDelJRknf_IvW6gr0bxoJJjexdiB4jeMAuMIS5exE6Q-Kid0-MSJGgdvSZuzkj3KS5YpmTnuNsVo-lN4Zflwy0FhR13q0_NaKTTPPCTjR2C6wsvd-wPOnI4CP2qCI0gU8oXHhzq7H0USbaQvH5BrbqrTmVOyGOVX03tTNwfSCbZo_PIkhMz0Bz9Jjaz7z6n822Cai8RAnAXE6nJy3jyHVYZulVfuljBXOP1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=qzJdQ-DVKFHI4QCOq5vmIoPx3dINRZPV3RX0ZeowjuaMSvpn0GoLxKUxAxY8GOelcEW73E6AiC-5V95mY0c9QCJIcN5KCkqGD9fs7dAVGSWK6xZEhaF2V__oKC6dKkPDy1Yl9qy8gAiR064rEUWK88kjYXFzfHJ4NTEKEzwtZhpdyNL-zz8SmKlozAKa4DBTmRsFWEl5_4o2Zhm8oP6fQa6PQmGm2RgoLWGtD1Qj55IKA0uWzSR2gWRvH1EmWpUM8auy6SqFzzgFQ6pm_cnOVPSTMPxETQqaITmMA5Qr-G36rv0EDq_MBkRdg9B7Tc_XKb5helFQHbJi5B02-NGRfyB2rO948aRfjgtosm_HUnvdhC_rWjFBNQSyfOUqUD99MnpcbGoUmdZWF1wsNAVnMw3mwJ3GDPTANweLPcWhfkhmz5KPLgt4NLF-_3j4lEgMOn7YiDXrTzwdVBTEoIJndqXvuLmNk8o-LW16upu7NpoXxpQmIojtrazJaa__UA7E3YSK069ea-3yP51ZSdN6pFnIteaS_MwujyeckqYB50h16RuAk3nnoCHrf_RfIKZPNiGKXmM6w3d3FL-pwTkHFMNxl_olIDYc5cb3-omUwYgV-XcT9-dB6VbOYqiML0JqPlzmPGI-uN9P7ruVchsB7_6Uv4WVEcA_-QPcFsn84iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=qzJdQ-DVKFHI4QCOq5vmIoPx3dINRZPV3RX0ZeowjuaMSvpn0GoLxKUxAxY8GOelcEW73E6AiC-5V95mY0c9QCJIcN5KCkqGD9fs7dAVGSWK6xZEhaF2V__oKC6dKkPDy1Yl9qy8gAiR064rEUWK88kjYXFzfHJ4NTEKEzwtZhpdyNL-zz8SmKlozAKa4DBTmRsFWEl5_4o2Zhm8oP6fQa6PQmGm2RgoLWGtD1Qj55IKA0uWzSR2gWRvH1EmWpUM8auy6SqFzzgFQ6pm_cnOVPSTMPxETQqaITmMA5Qr-G36rv0EDq_MBkRdg9B7Tc_XKb5helFQHbJi5B02-NGRfyB2rO948aRfjgtosm_HUnvdhC_rWjFBNQSyfOUqUD99MnpcbGoUmdZWF1wsNAVnMw3mwJ3GDPTANweLPcWhfkhmz5KPLgt4NLF-_3j4lEgMOn7YiDXrTzwdVBTEoIJndqXvuLmNk8o-LW16upu7NpoXxpQmIojtrazJaa__UA7E3YSK069ea-3yP51ZSdN6pFnIteaS_MwujyeckqYB50h16RuAk3nnoCHrf_RfIKZPNiGKXmM6w3d3FL-pwTkHFMNxl_olIDYc5cb3-omUwYgV-XcT9-dB6VbOYqiML0JqPlzmPGI-uN9P7ruVchsB7_6Uv4WVEcA_-QPcFsn84iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay3f999K_1Y2_3cI55_TKCkhfiNLvgbNMk4EVl3WVwxpb1PCo47jnrPSOLZUYow71zNi8XvQSrQotBVWCmVQm2w6UL9v-8-1OhvEDlQzT1sndxOUlEIfwKGmun6-vCmN8ZZ0J2sqgpFuwiA7NIblaqro2ObgdfxVxuIYru-8g0CejugE3uCvcPfQ_AG4jZaPRjkBhy-Jcl8Q-LIlPX1XtWgighIImhlSaDhBztLr8w-x1RinWpoza_UiYz3P1HHqxc-BmYWOrE_cqnCjmetLBuPv9jR4yxSq5FME-GPOeGIE8rF-FjDInNt0V6McooB17GJzKApH4faD1n3_-orZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLUPs9cQe-1_BdxJhfhF7Oy7kYwX9fjrGqM7KRXhDATBRJEOvlTaYSoB6Ap0z8h6baaYGe5CwkpybT7atMK6u4Jx2V3XMd8AtI2LFDiza9RPFDoAnrFILxxwd-sLxnOJHoaRCqHTiW6sTnCVsYqnPbFkt0gg51MiLJ3ytPBHcUuZYO1X2qSFWAxllz57s5yb67NnFNvt9dWstb4Sxivxmvs4oEcPcPcPG2G9RjguwgYtP2Bt6AfLeoXzwUwYIBKx6kWGtxQn3LBq-7pNhnmt8MbiCa8-2FiWZ6lXklaUz6Yy23WryjD1nCVofhLe0Cfum8_hvSpJXLWavtDPQ8Shhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlhG1yOkFWzblBxsu6r4IX6eHkz_JRk2CaPTqeRhgXYCW4-DtIzVHLDUg2BcnYz05qfBgxsxQBvquC_phHviGTmUSOkAeOcVopHXbzdJwfQH8cOcxKgI4AMBaxyaz8XNeKUfRhGgFH82_4vG1RUv7uU_JbazijCN4Pev7FeDmeyEu6A0_Af2N-liWD9iOubiqr_biEvHmdkpn5NLM4rmkbTY98LA52gJsWOln8hPkWNfts5FzOoNNRsoEJFb3nNH26TqY5RX0Md4rkSgyUYpE4uFY4CJc-4W_igCawe9qw_fgpYuJjDnRwgPQPoeIxcQ_NMSEwBGHZKdvfcPcGyLAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua9qi3-FGQC5_1fwMm6RAjKlQ-yrUIrBd3-1_Vl2Bi4Qq_kNaV11wvQFeksiSGdolvEb6EpAG36ZhFQgOHa78OLUZd8mHVcIfNQOb8C_srNOEUhOmwaEXYnF_xZ0J21YiSUMSB6C4cmRRdn7fWh3A5Osw0ghfV7OmQfGDU-PymMk_whVh75bjKtfpDJA9G4frDe2tQrZaLceempYicOL5tp3GHsa_bVDOglb2tajW10KHqE3yQvZ3SQSQTishQ90BMGo7BlHEs7Gp8EU6lpal2XZ6hUtnSIyjtzuViEYZdFhAwyr1gGgnARSU02GpMTu8cOJJ_RShnver5ndOiDgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=dzcgIwi4qla09cVzHmOuhdgMYHeeJkpTGAMtgdOxZfamoTvi6FZOfpHIIK7AWx5rn6tC2pWDSReK6juLeaERkIAEky78DZmVSzmWD3rL4ijucplWtSTuT5IYaJ9ijtb-r3fOGGcwhWKa_Q639PuNtwqttEJYl0-SkX65OOoXqZl0ItXcapKqrqT3hmF05KFgJp4BFlPCHyHwJBMjoHE7iFqiRuRTwBddtqn_zTevszc11wIVAXX9oJ872x6rk6wX79VgfV1CshKO90KAGRJBPRhrScXQmAQOVEoXmuyMsWSNBQo6JVVzXR9xc54XgW-RD0TGpfPxzX7lg-yaNhScAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=dzcgIwi4qla09cVzHmOuhdgMYHeeJkpTGAMtgdOxZfamoTvi6FZOfpHIIK7AWx5rn6tC2pWDSReK6juLeaERkIAEky78DZmVSzmWD3rL4ijucplWtSTuT5IYaJ9ijtb-r3fOGGcwhWKa_Q639PuNtwqttEJYl0-SkX65OOoXqZl0ItXcapKqrqT3hmF05KFgJp4BFlPCHyHwJBMjoHE7iFqiRuRTwBddtqn_zTevszc11wIVAXX9oJ872x6rk6wX79VgfV1CshKO90KAGRJBPRhrScXQmAQOVEoXmuyMsWSNBQo6JVVzXR9xc54XgW-RD0TGpfPxzX7lg-yaNhScAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=eA0b_TRT1rgZ3FVlcMzIhZ5ueOaEzagfYXKFfV-Td-4r9rRYIAoRgsDkW3CqFiQdaqpPOK5l7R8pTYFUQsqNV8WMWH9u7whPiNJ6baydcohEm4u78BfXV08Ft7FzNvJ-sH6dS7GAsjnuW2Qq7qA99aS7b6ZZe8hlYxw1tEGAlHCavl28YmPhnc5cqU4jf4M6YtbbicEu_RUMEXVS5_zTLlkyQC8pmXxKiUrWTGs_Hieh0r_XHeg8Ckgsu5bTL19iBXMFtBEDP3OuhYmxEBniWMT68WVgcDAzBfdwE9E4eH-tGC0Q9wx5sv-4AKRKXtjXdSnO4cB2ie0Gi7ScU781cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=eA0b_TRT1rgZ3FVlcMzIhZ5ueOaEzagfYXKFfV-Td-4r9rRYIAoRgsDkW3CqFiQdaqpPOK5l7R8pTYFUQsqNV8WMWH9u7whPiNJ6baydcohEm4u78BfXV08Ft7FzNvJ-sH6dS7GAsjnuW2Qq7qA99aS7b6ZZe8hlYxw1tEGAlHCavl28YmPhnc5cqU4jf4M6YtbbicEu_RUMEXVS5_zTLlkyQC8pmXxKiUrWTGs_Hieh0r_XHeg8Ckgsu5bTL19iBXMFtBEDP3OuhYmxEBniWMT68WVgcDAzBfdwE9E4eH-tGC0Q9wx5sv-4AKRKXtjXdSnO4cB2ie0Gi7ScU781cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyIn3eAZCg1SAxAjpaKO7a075o1QUdeYcZoFxA6uGojAJ1Qrzs4I05tZgf20qh_9eVMunC0yJFdStAlYPkW3qi1QFi7o6X4YkcK_Q4jjwPhXrluTJxbDm6tLON8mUVHJjIRz7OcPnfVYwS_aGtEbkx8YyZo81uoKd1O4Y9ClRi2109QmbgD_-9b7rg8efLiNlix-MmMkYF1_r16i-ud6KAkqbqbh9Li4wr9JfQMjsP6qZu1pLFHiAISLgKMNJ4rp4WM5NNeED3Q1ELAFwmcxLJ5dV5L1gFITD6oKQbA8FPl-DL_H-HTsvobfCD4ZiJWr1qwD4yiUcUzzGPbH1LrlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=OMjv6o24fM18y-JcS3RBUaXIGji8pxyjNlk9YSdtSmFW3i6qPD_KdgQr6Doy5pQSRoRV5OWjmA9B9BRte3Cylbw2IRzIosUFIQ4TRWCu8wF1NbI6mRrCd1_Jc6takpz0me6Y6wmo3MUdi_elSEuZvKDunXqeGtGCRt7ZtIZyPRuEwj0gyppIFWn366YtxbCeW6atE1oavuuuzxVlSYv8-NRozOIy1iURbuKcxA2YQJ7C99CtBL-3HWvrLbSJULuxN40hicJSoZjhDiFdq6LrX88xc90PXdYmNTD8QSbUxaFOPDRpuC6XLgBXi6UUzQ5h7Z-Y04xt9X0i2oHnHvcJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=OMjv6o24fM18y-JcS3RBUaXIGji8pxyjNlk9YSdtSmFW3i6qPD_KdgQr6Doy5pQSRoRV5OWjmA9B9BRte3Cylbw2IRzIosUFIQ4TRWCu8wF1NbI6mRrCd1_Jc6takpz0me6Y6wmo3MUdi_elSEuZvKDunXqeGtGCRt7ZtIZyPRuEwj0gyppIFWn366YtxbCeW6atE1oavuuuzxVlSYv8-NRozOIy1iURbuKcxA2YQJ7C99CtBL-3HWvrLbSJULuxN40hicJSoZjhDiFdq6LrX88xc90PXdYmNTD8QSbUxaFOPDRpuC6XLgBXi6UUzQ5h7Z-Y04xt9X0i2oHnHvcJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=g50wSxZKgENaTeFVrcfdTN6DCeh4RniWaJc6SC3ItSolmKEb9SUSw9reUV1PG-giA_uAQ7JCbG6_BYxPPM88xMSaTOYgD7oJn5Pc0RKNRumCoVv8Na9aL5YiGlNUFJZ-gKyKeaxrNg-M9Zc8mufFq7leSBuwmWzkmOMBI7BnyUJ9695JhL7qAf0AxAzzuLNGEX0WYGWDBtUsrGSxqgYFo_vNVx3wfvTJUc78Xq0uIs2HPo2w5NtPuHVIc5j2iVxaz0-K0W6u9vJhi4seokhnVt3QWV7YA8ICROciDMCkCfqe_4A_8IGxx4O2llo0zlKp0PU3pNg4GjwB1JKpsS4P8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=g50wSxZKgENaTeFVrcfdTN6DCeh4RniWaJc6SC3ItSolmKEb9SUSw9reUV1PG-giA_uAQ7JCbG6_BYxPPM88xMSaTOYgD7oJn5Pc0RKNRumCoVv8Na9aL5YiGlNUFJZ-gKyKeaxrNg-M9Zc8mufFq7leSBuwmWzkmOMBI7BnyUJ9695JhL7qAf0AxAzzuLNGEX0WYGWDBtUsrGSxqgYFo_vNVx3wfvTJUc78Xq0uIs2HPo2w5NtPuHVIc5j2iVxaz0-K0W6u9vJhi4seokhnVt3QWV7YA8ICROciDMCkCfqe_4A_8IGxx4O2llo0zlKp0PU3pNg4GjwB1JKpsS4P8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=VVvPKOwHiJ-5S4TIotqfKK6qgbJse69URBZBxx2ao5uyLtRmnXwpEyOPL8eWW34fCkiTNSGCbiSBaLqny7u1htmVWBWKz6KfCRgAbUZfjgIBaLPbcZhOKF6E_xjDoay0Lm0hZZWcJy55OQr_DKq8YdkYnUQFeoXNLU7N5LJ7jXkgOm4FoY_NwYBf_6XwVLbMh7mamwwr2wVBZmsM7aD87Ixc_PLQT2S9NxJiWs7FLJ-A4P6b_RBfYLOK_vxDAYK8-9PfCSHVKkYvodMUnRCBrsXu6bL0alDekpGFTSzgioVSZ4f6cY1gZv7eVKAt1piej_skVQj2bd8IEIHFhLDN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=VVvPKOwHiJ-5S4TIotqfKK6qgbJse69URBZBxx2ao5uyLtRmnXwpEyOPL8eWW34fCkiTNSGCbiSBaLqny7u1htmVWBWKz6KfCRgAbUZfjgIBaLPbcZhOKF6E_xjDoay0Lm0hZZWcJy55OQr_DKq8YdkYnUQFeoXNLU7N5LJ7jXkgOm4FoY_NwYBf_6XwVLbMh7mamwwr2wVBZmsM7aD87Ixc_PLQT2S9NxJiWs7FLJ-A4P6b_RBfYLOK_vxDAYK8-9PfCSHVKkYvodMUnRCBrsXu6bL0alDekpGFTSzgioVSZ4f6cY1gZv7eVKAt1piej_skVQj2bd8IEIHFhLDN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZXxh1bFKBxGYMhqakXDYwdZPoCsuvAw21vhAUOdA5Rzc5Gj053G_BGS20BzsWM9V6YgYq65dk5TlFtz4rHTpMsvZj4_YIOLMaM3gIZY0fkc5H68nLb3tkVj5CowkgNFopsZVYjy3T6TN1-tqhojpJZUZ5BKMfFqLlwpSD2xYM8LS7hsJejTk_92kLN1-RF1Y98oABuQvkUmzwbLn9ZcMMTvjNJaohAOCvDGe-FduIUiXNiQPggHpVGpayBAJql7f2hjcElW_bqDehn9fHah7HGe1Q4XiyylUXWvBzHVVj8DcpjE1jOWxVxPtUUah_mVGACGpW2Vir0yi0xlkg5i1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=SUFqarQrcE0nxK2M_vfdB3HiqA19UnBeLzvO-dq15Xw8mYVO8Ubr2EvakE8vrLJyu3T__-qvAiqA3leDPvsDLHLNlxlF5CVlXM6kbLKfwZ1hBgO3zorvKHZLMzYOMT-xVxklpGHzD8cgKlGiwA1_0o6uBoVAPAaZtLmUnEmxgX-uvhmOn_xW3q0JHlP-YIT872A2796jBG4CF3aqM4Mplv5iba6PQBsotyVpnbVuG8WLgcHogY7XBRQvR2_igVp_5MVkDln2OwBc1aQY8BJCCdQvXrnpGRYDG0iDxJV-Q2ZemUv_AiBFzAokAOOJmns8niy3O3qb2G5MOFq4AmL9AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=SUFqarQrcE0nxK2M_vfdB3HiqA19UnBeLzvO-dq15Xw8mYVO8Ubr2EvakE8vrLJyu3T__-qvAiqA3leDPvsDLHLNlxlF5CVlXM6kbLKfwZ1hBgO3zorvKHZLMzYOMT-xVxklpGHzD8cgKlGiwA1_0o6uBoVAPAaZtLmUnEmxgX-uvhmOn_xW3q0JHlP-YIT872A2796jBG4CF3aqM4Mplv5iba6PQBsotyVpnbVuG8WLgcHogY7XBRQvR2_igVp_5MVkDln2OwBc1aQY8BJCCdQvXrnpGRYDG0iDxJV-Q2ZemUv_AiBFzAokAOOJmns8niy3O3qb2G5MOFq4AmL9AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQQLLViZ89N_hSJ0n78TwTbORXnbUWt7OWAGPp-TuHTJn6mWqdEev14lTdScBHytKOGhc5H3cKK1g3YNASytiPNAC2Y4JmSGT-ML9ZdhknK0NXSVOorFm2J2Naoq2bIIq9Yl7w66J69n86zPiR6nPf8uVNutdpGs9XbzCABqVgzY2jeptlhZ9N4Rh-KWZdFq2BtXxZGB1eK9akNeyhXpOigcCyRpBs3IJuK36dk_6UMSpRMEYFJUE15cCy6gXyu26UMpiltl5HMTH6JJcPlsuVhTn9rEvi6iYm7aqlwaqxcI0OIzhFngMMJBRsXltxi2xLkRpR3Jg4dTKIM3jBTUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6JSJTz97yZADJn8SUCOf7dd-x2jBmhdLtx1rV9iSm6tkJH2GNItL_5RGx-A2UkEds7fKIX0J67uhqqy_81bwdO8LLAifScPC2h4CW1PMjNXB_M4qw5w1TREvIcA6FeFGhwOmUuhMB1fA0bJlaZKsRo2R5cLP0_DKvdy0LSnLoFvK6y-M8Lck6j1Zj6_8pi0Ruomf2ChSG6Qa0ehX_Va1DoikReYVvE2Ebv-QMxycj6b5sgFQsDgvZeWmF_TCT-Bo5pS-BdUjsMrSBXHMxCDCS1j5Srv9ZstUv0JhgVVQDznGI8XUCRbWlXvPYSj6pDzub5IJ80z47eH-Y7n7DwBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=YgBNgxY_NhruYJZb1oLLsSCUEtg5lAWjSvm7sRc3znmQGRpcyNVrEhvrQcDKysFu94c1EWzvVhORzQ0oXfK2mfu_c_icwwfUlv5M7w_ZsO00Dxxhn9lUZr43zxbPmMxa4UFKWQMZt64aDtDeMFuVw79w85gCS0fXU324KxspVwcnwWnGxjQnjSr0SkFBkzkbJcDADbvKX2BNGXf1TugENOlpT5qOI0KylfwvdAK2MttXHOgTKQZSRZk2qDgKEC7K8BkYKXA8AMbSKq3NdyJRFRvRtPvIiTo85xKwz1k4LoO3-1vcoTlPaukr-O5yyStQDRNXQQ7TB5AMoSfkJJCAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=YgBNgxY_NhruYJZb1oLLsSCUEtg5lAWjSvm7sRc3znmQGRpcyNVrEhvrQcDKysFu94c1EWzvVhORzQ0oXfK2mfu_c_icwwfUlv5M7w_ZsO00Dxxhn9lUZr43zxbPmMxa4UFKWQMZt64aDtDeMFuVw79w85gCS0fXU324KxspVwcnwWnGxjQnjSr0SkFBkzkbJcDADbvKX2BNGXf1TugENOlpT5qOI0KylfwvdAK2MttXHOgTKQZSRZk2qDgKEC7K8BkYKXA8AMbSKq3NdyJRFRvRtPvIiTo85xKwz1k4LoO3-1vcoTlPaukr-O5yyStQDRNXQQ7TB5AMoSfkJJCAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9ZilZjw1r4pQe0OD7aOuIpUJVckYdfEWOjN-NTz9EtnFSgeQYIIqb_Cm4roqUGbecOQ8VxpYyFiRpriVmJ86WiSc_SJ0EnfFf1xWiK_FF_kU2Dd0XU9iJz9rRHvSV4pBtKDqi0Wz_DnaMcf_mATsbOdwsHNMjq1jKeuBOJe4jnV7kw_7vmFXPCQn0tIut_CFx7iSNMwwM3Dn-1Bq6OO2YpPhXe9hVDz_xLB366C3f46YRg2_PeDezz52ggevyCFzA87bYs7vh1Jnsnb8aCGO9MK1hVm_Jm0GnkyJ1TXJEY2stJfAyV7ByqG9jv_f10bg1wGE4eTSCU_bqMIErjAqT-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9ZilZjw1r4pQe0OD7aOuIpUJVckYdfEWOjN-NTz9EtnFSgeQYIIqb_Cm4roqUGbecOQ8VxpYyFiRpriVmJ86WiSc_SJ0EnfFf1xWiK_FF_kU2Dd0XU9iJz9rRHvSV4pBtKDqi0Wz_DnaMcf_mATsbOdwsHNMjq1jKeuBOJe4jnV7kw_7vmFXPCQn0tIut_CFx7iSNMwwM3Dn-1Bq6OO2YpPhXe9hVDz_xLB366C3f46YRg2_PeDezz52ggevyCFzA87bYs7vh1Jnsnb8aCGO9MK1hVm_Jm0GnkyJ1TXJEY2stJfAyV7ByqG9jv_f10bg1wGE4eTSCU_bqMIErjAqT-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=BhxBF_TNoJMQgd9QKMjOPFyeWLum8nlZdzB2sgmPzm_UjCkiwMU3Q0oqMVxbClDyz7ixgZRj7A_3izdEO7TZRspEsHQfNi6w0Bp5HsA_niR3vSgEcmuQJ_xvllWn0MIAz2ZxqgX6oVuDOT5l12Sj_6o3rdIwaY4RBCRwQpTYcDFkAukWivqmj-p8n1J9WGkQqgPegCYdSXVx2GmPEdf7PNN3ywdBVRwJqKMEmT-fyXDv-uMp1dxgy1mp92pspAsOJjIkRYrtxFrKeXzSu3YZjxXcnJaX0ikyhjZrWgreLhp7iH8b6WOqtCYfT9wSR-fF3QrhU28VJOKQDr0zeeso-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=BhxBF_TNoJMQgd9QKMjOPFyeWLum8nlZdzB2sgmPzm_UjCkiwMU3Q0oqMVxbClDyz7ixgZRj7A_3izdEO7TZRspEsHQfNi6w0Bp5HsA_niR3vSgEcmuQJ_xvllWn0MIAz2ZxqgX6oVuDOT5l12Sj_6o3rdIwaY4RBCRwQpTYcDFkAukWivqmj-p8n1J9WGkQqgPegCYdSXVx2GmPEdf7PNN3ywdBVRwJqKMEmT-fyXDv-uMp1dxgy1mp92pspAsOJjIkRYrtxFrKeXzSu3YZjxXcnJaX0ikyhjZrWgreLhp7iH8b6WOqtCYfT9wSR-fF3QrhU28VJOKQDr0zeeso-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEuozUWA0TjGEtfuThffTW8kPwbjQN2dWANu8TWF-Rr20yuyg5meSQHaAxaZgvklHoDuK7HqS0cEHJlBGjk_60ONNidRz1PqPF-_OR6C2crHtPJv6n7ELcxGUUtwPpxSRELnESzPIxSngtbElQ-xLkJbKLP5OuIARbeBnxP0G96dhJeXpfCtW_HJ3V3wSNK5DOo-3Kpj3R_SqkrgJo6RW-cKapVka6ztf9KiAYZze1sAK5G1KKU8M9Y9PtjEHeOq18Az1EiVOgeIITvInZO5C4bUMEkpFeY6RoNA0QF2ZnmC5QzgYxGpQ4KtIzOm-f9_olm7EFQ6uZvFQX4uXQhGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=F-ofjfjS1qMeCztkU1sZcfG2GDY4JzACmR1_fg4SL5tKlpXcggy-dVrpT1LywYPu87PXs1D8TVbfRPpSZLZTH9J-e7zeUlcbPh_CV7ty98WnCpIaEV3uj6Zf4uO_II5kstA2ShvHpd1qrrIFhXfBbcd0JcedkV6n57D74BcjTvKFYIbZXcL4K8HK_LF4KT5Vik_2EpJdUCEjZEt_i2UAxfRDS_MRUUxR4uxVCRiqs0Pp5vinVnEcH4Qq3NyWI1mhUTVYhPk_JTx39CayrdkcW2E_Yhye76GLcmfKMYL0EKvcQBZEgcxyyGXLAhCZ4QDP_iQyKfU3P4Futs7JpqvlmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=F-ofjfjS1qMeCztkU1sZcfG2GDY4JzACmR1_fg4SL5tKlpXcggy-dVrpT1LywYPu87PXs1D8TVbfRPpSZLZTH9J-e7zeUlcbPh_CV7ty98WnCpIaEV3uj6Zf4uO_II5kstA2ShvHpd1qrrIFhXfBbcd0JcedkV6n57D74BcjTvKFYIbZXcL4K8HK_LF4KT5Vik_2EpJdUCEjZEt_i2UAxfRDS_MRUUxR4uxVCRiqs0Pp5vinVnEcH4Qq3NyWI1mhUTVYhPk_JTx39CayrdkcW2E_Yhye76GLcmfKMYL0EKvcQBZEgcxyyGXLAhCZ4QDP_iQyKfU3P4Futs7JpqvlmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qtGySd2BWyoHH06WzZSF2csJf8KOMFxX5o_pxZhll2fXuc-V0V8WybW4cShZUb34-0_skf4mmTb9l73MwgpQn8gMXd5B4Wp3PABdjtSaVrqMF9bfQJLc2vdRTIeCsWeZEiD3wN0qer3yWUJQyJTKVqBPW5aie9vYQQTreWaSbrI_Hl7VT6qsWIGeDxWLoa7iLI7mQYhu6D5NJxP0NJe_wIoveYB0yDVxBj6fH377T-RtEUccnuLVRWK6Tug97tbbJ7fSQovOE3dR-hiCoDsj0VpDvQ72YLs_fbczz913kShiTcM-RRHJrIm-ezNFZ3zZoHdwGZuqNKIXFPg_a_4pfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qtGySd2BWyoHH06WzZSF2csJf8KOMFxX5o_pxZhll2fXuc-V0V8WybW4cShZUb34-0_skf4mmTb9l73MwgpQn8gMXd5B4Wp3PABdjtSaVrqMF9bfQJLc2vdRTIeCsWeZEiD3wN0qer3yWUJQyJTKVqBPW5aie9vYQQTreWaSbrI_Hl7VT6qsWIGeDxWLoa7iLI7mQYhu6D5NJxP0NJe_wIoveYB0yDVxBj6fH377T-RtEUccnuLVRWK6Tug97tbbJ7fSQovOE3dR-hiCoDsj0VpDvQ72YLs_fbczz913kShiTcM-RRHJrIm-ezNFZ3zZoHdwGZuqNKIXFPg_a_4pfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=jAer6iyprg4QfJ_-0kP_C9m2BanQkxDnHFLruQZzqBgEItAE_PpaDJrs5D6jkidEmpJYFsnwZif4Or65DGRx83qEw1QPP5naTK21Z5ig6PBaQ-QecJQ8SceMPT9kMzX_vNKhUljd5K7oz6Rfm7-5LrJcjpByJZTPUrSxVR0RgdQ12sQFTGisgGaY_Hyc9Om_AD1IkAu1ctPWwnRDNIH_LgrsE724oAqkchk5Aqz_-JbCaqwNFTIacpGuBVC6bTojj3iPe8qnJ8XKSOPOhGXpmsthrFix18rG33nJi8Jrlw9RxpYIY4eYSW5dnfZDt225XLH08Ozq_cjWsZlrqQO2dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=jAer6iyprg4QfJ_-0kP_C9m2BanQkxDnHFLruQZzqBgEItAE_PpaDJrs5D6jkidEmpJYFsnwZif4Or65DGRx83qEw1QPP5naTK21Z5ig6PBaQ-QecJQ8SceMPT9kMzX_vNKhUljd5K7oz6Rfm7-5LrJcjpByJZTPUrSxVR0RgdQ12sQFTGisgGaY_Hyc9Om_AD1IkAu1ctPWwnRDNIH_LgrsE724oAqkchk5Aqz_-JbCaqwNFTIacpGuBVC6bTojj3iPe8qnJ8XKSOPOhGXpmsthrFix18rG33nJi8Jrlw9RxpYIY4eYSW5dnfZDt225XLH08Ozq_cjWsZlrqQO2dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ps4wTtxosLLUgGxdCfaUDnKkRrLmlGU1XpXUCHmAcz9jgFQ4kTFBc_DVieini94Z_mPP4CCIQK_ZgSdXUELXOT1MYXrpvbyAerL5aB-BZ08yWWbVC4vdhOY1YT4OEmfNNexyQ5Sb_qNua78jF2pIzkNPaZ6Ork5Xk-XPS1gQWRfB-c9g4mNI5aa9EypsqhlYfPhtpiS1jhLmOZ2YjQ3Q0Z-0SJlC1OCcmFbnZkWBbeYzZa0NTje30g1ah_bQoSlROM2HRWUzx525rIubQsgXwTEWU1uvwp67DIUXTB5-Dr2UOxse6oBzt-Xt8W6FKGVk43NNal6TzvEaWUTGohLb6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ps4wTtxosLLUgGxdCfaUDnKkRrLmlGU1XpXUCHmAcz9jgFQ4kTFBc_DVieini94Z_mPP4CCIQK_ZgSdXUELXOT1MYXrpvbyAerL5aB-BZ08yWWbVC4vdhOY1YT4OEmfNNexyQ5Sb_qNua78jF2pIzkNPaZ6Ork5Xk-XPS1gQWRfB-c9g4mNI5aa9EypsqhlYfPhtpiS1jhLmOZ2YjQ3Q0Z-0SJlC1OCcmFbnZkWBbeYzZa0NTje30g1ah_bQoSlROM2HRWUzx525rIubQsgXwTEWU1uvwp67DIUXTB5-Dr2UOxse6oBzt-Xt8W6FKGVk43NNal6TzvEaWUTGohLb6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i143Cp3ZcXqPEgK3KtuIaQm2FdlrR80rPcEh82N846iknFqCygCWNidib7Kj0Ax20i8Hq577unMviNVPvV_y_fbj-JcE8Uqph6hCiCNnHJ0oTKSEXVcrYI1LM0JoMopXhXCtWzoyE8Fp2Y_G56mWJnMMQd1q17BC3oOgUdLh44pAzTFPiEYsFUFwKuOBPYHPetSSGB7PY4hKzh-z-NIMtZcv5F8aYnQarRiO3j0tUe9pU4QV27VbS8dvev5_0vFkNxirRrmRcubHl3kHj4bd6aCvI9jBO6z40ZCqBove-edZwra4bWvNx2sOHqZDgimW2entF1MNgWmjxTjGC5IIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=XeJYmmrqph6uGF79BciYfUUEmYOIZ-6cyQ17_iNLU2sQS9yIHgB-HV9uBHJ9coqPnl6IGoCkRIiFlPIJmInzKEVkeV7k0tD8qSKsFy28C0YTi7vm1cQ9F1Ehqn6Za2oy4Kk4dAoZ5DH4sJbye4otx1TKL9sS4kAHnC_JW857kRlJq4sdURRa_ur_Gl9lHx3MUPHg0KAohLNHXGw9xawfC2D6-xFpYLLEi0EhrhE9zeX48gKc9T-Wp9NOtYUyxwzakNiNOP2f-QJmZ95D7-rk99_mEEvKAg_lnwROrap6cPVjDefw71yqW2gDE5l49BIoCr-OI_GCGlCryA60E4GObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=XeJYmmrqph6uGF79BciYfUUEmYOIZ-6cyQ17_iNLU2sQS9yIHgB-HV9uBHJ9coqPnl6IGoCkRIiFlPIJmInzKEVkeV7k0tD8qSKsFy28C0YTi7vm1cQ9F1Ehqn6Za2oy4Kk4dAoZ5DH4sJbye4otx1TKL9sS4kAHnC_JW857kRlJq4sdURRa_ur_Gl9lHx3MUPHg0KAohLNHXGw9xawfC2D6-xFpYLLEi0EhrhE9zeX48gKc9T-Wp9NOtYUyxwzakNiNOP2f-QJmZ95D7-rk99_mEEvKAg_lnwROrap6cPVjDefw71yqW2gDE5l49BIoCr-OI_GCGlCryA60E4GObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=VL49idhkQuu8cK4JHEXta4cdCtnuEOtaGvy515xQFwq3CkYKCSQbKHj38NcQrsaBSTiREIHauKQiqlX05mf-guVjpI98ygLf5vz00UgWVEq7TeD5GX_vhRv4yNtdbT5rQ8lnffLQeEEht_WSU3XzCSw6S-UAR49lBxJzVbqWJxlzVOGlVWQYRTLepXu_71gVFVytDxXQiICmElCFO8ZrKQS8MBR-vstrj2p6KXtyjiObpcDPRbc8TV0cIW8Jo-ARblOW_7TIqHQaI6uEGSv--h8gFVurZvdJmibTE0zJsZDamQKdZO0hO7aUOEy7GJPqYke85dGeuOtVCZ5UseZzfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=VL49idhkQuu8cK4JHEXta4cdCtnuEOtaGvy515xQFwq3CkYKCSQbKHj38NcQrsaBSTiREIHauKQiqlX05mf-guVjpI98ygLf5vz00UgWVEq7TeD5GX_vhRv4yNtdbT5rQ8lnffLQeEEht_WSU3XzCSw6S-UAR49lBxJzVbqWJxlzVOGlVWQYRTLepXu_71gVFVytDxXQiICmElCFO8ZrKQS8MBR-vstrj2p6KXtyjiObpcDPRbc8TV0cIW8Jo-ARblOW_7TIqHQaI6uEGSv--h8gFVurZvdJmibTE0zJsZDamQKdZO0hO7aUOEy7GJPqYke85dGeuOtVCZ5UseZzfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0RrO9pRwNaIzcpXXblscP9Bu3yKYknjGUPXHkDkeQRMusAydAgxlnpNY6jdbht-UR7eHtyS0jnSlgI79lTcroPteB9Sy4FvB8j1G8XIXaaKrgZvfn8QFUtwp-Iub24S9ORRCf-RFVSTIHRXIpiOFDnheOPxtzEpXPuySmfBggbvABqGssvE9wFKOv1y_qZ3PVA9Q0yLBvEzTNR62sP60Glqadz2lmbNCuuGf_bhpUYyjenRfE7XGL1mTVsGaxGOAnicTf8bkxAFV6JmFyBgvN7AScsGBkLh5G8gp6XrLHPBgKfEhtr8qzRK-D2Vs3Fe09c4eYoO_ZMJOg2ZBjmFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=SdohO4rxxC_NgoEvVtRKaqX45KF6NQQQfO6lpEhrcpDN-blT0JepGi-dMcFC9B3Y-UJ-hHyoj2b8yCNn7OT7stoTOEM8yC2l2fslPz7QAT6DmDMH4nc5n60eKuL3OQLc5JRkrivnauUvk_WHU9ciA4D92tEq37G4C0ox8WfxByeenaHVKLaX0h7hQLj6L3FC5b_PemSlPfSJBy81xOlRvwGD0JzKah95GmkuAx0oZyepMpZHX0QjknTvxvAhhvIKuz_qnX2y52BNcFEPeOicJP1g0D5n364wdjGtN9_ipUXbVAdMDfpao_CJ1NS9x6Sjs8A_TCOzW8dA0CmPRptV_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=SdohO4rxxC_NgoEvVtRKaqX45KF6NQQQfO6lpEhrcpDN-blT0JepGi-dMcFC9B3Y-UJ-hHyoj2b8yCNn7OT7stoTOEM8yC2l2fslPz7QAT6DmDMH4nc5n60eKuL3OQLc5JRkrivnauUvk_WHU9ciA4D92tEq37G4C0ox8WfxByeenaHVKLaX0h7hQLj6L3FC5b_PemSlPfSJBy81xOlRvwGD0JzKah95GmkuAx0oZyepMpZHX0QjknTvxvAhhvIKuz_qnX2y52BNcFEPeOicJP1g0D5n364wdjGtN9_ipUXbVAdMDfpao_CJ1NS9x6Sjs8A_TCOzW8dA0CmPRptV_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=KSMuZ-fKJcqwwoWsqv7kTFDK8sEu2CnI38oc3IMW89AjEcmv7w516gs9UvwnPVSsicWTyhlr2DFw091XUNOxAvZHnE5PK-UKdbdQ4Giw8pzseuJ1MpIT37JM1uSyDg2a5QvnKMMAh-yUu3USXfKL89zVh8XmmRzJonaJuxjBSHh1PuUBsYeRtoXONNRBwdlFYt1vxBVKFbN51UUpFUY9Z6RMx38mZV2A8o7B2AqAbT3fh-FIuWdMimhTk5SCkIsieWyVzokRhkdWHa5tTp_eJ_F8EAvixZAZ1SFW8Iedto8YStZ49cBrSIcvZeY0WsuypEXn8QroZry0uy0p63q9kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=KSMuZ-fKJcqwwoWsqv7kTFDK8sEu2CnI38oc3IMW89AjEcmv7w516gs9UvwnPVSsicWTyhlr2DFw091XUNOxAvZHnE5PK-UKdbdQ4Giw8pzseuJ1MpIT37JM1uSyDg2a5QvnKMMAh-yUu3USXfKL89zVh8XmmRzJonaJuxjBSHh1PuUBsYeRtoXONNRBwdlFYt1vxBVKFbN51UUpFUY9Z6RMx38mZV2A8o7B2AqAbT3fh-FIuWdMimhTk5SCkIsieWyVzokRhkdWHa5tTp_eJ_F8EAvixZAZ1SFW8Iedto8YStZ49cBrSIcvZeY0WsuypEXn8QroZry0uy0p63q9kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=VFFueNgOSJfOyZX8xpVkb9eZSqO4mObhe3tUv5NRBWTz_BkkSqMRlhtu3FhLcHopptRXLJTSgopzuusw_r5dy4e-iKjQl5zq2ZkOZtRW54C6Tp-2F9Elu8IlCe-1I1ZYIHaQQ922A6WRwVVzx1lit9ZmRfnKSHYOkyqAndzu7pBCUPFUjMMOYRKtDsfSaBOr1pzkplQYYf3174n7OxpfgExms-urclUqaF0HH5F2B261tiNR-75s-U2GxNlnmWNzkU_v7zx5bEzXHSdy9Pes3Rpxaq43qQMFa7115OMtnnsGD1YMqGN5Nbx-qSAnnxLvGrFrBW3gztKsFDNOBrbypYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=VFFueNgOSJfOyZX8xpVkb9eZSqO4mObhe3tUv5NRBWTz_BkkSqMRlhtu3FhLcHopptRXLJTSgopzuusw_r5dy4e-iKjQl5zq2ZkOZtRW54C6Tp-2F9Elu8IlCe-1I1ZYIHaQQ922A6WRwVVzx1lit9ZmRfnKSHYOkyqAndzu7pBCUPFUjMMOYRKtDsfSaBOr1pzkplQYYf3174n7OxpfgExms-urclUqaF0HH5F2B261tiNR-75s-U2GxNlnmWNzkU_v7zx5bEzXHSdy9Pes3Rpxaq43qQMFa7115OMtnnsGD1YMqGN5Nbx-qSAnnxLvGrFrBW3gztKsFDNOBrbypYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmZY7BT-ocTfip7d1l3YjG_cl0grbpXm886nSer8UmZs3qespR_U3jvEAcaWw6xe9rRWh4gngSSOhKPyNxQLNtAVnJGZzTvAKne2r_Qn3DmTm7GI9LMjxrgQmV75mjsgI7mzJRTBk5uQhdeq9jmQ2SjCxjWzNdtZjeMmT1f1NWUaZ2YFNHRi7VOpV1PPxBFGJQbXxpWholtTbeAW9MCxKY4qrNgoA8aA9I_wBlAYiqpeHy6CeqC0CmZRe6Gvdfai_4fYnLLO0euiS_qepHl5MCL4euEW8VYibxrPl6UuEhRpS0FBlePzjT3-8_Tx_J1Ch9dqN-nLrkv7kBV8R3ZAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYFEgevIP1NqgXCUrFg3z1h25DRnmnfIN_HDd_RfVXOzQeZrBbLRvDieULT_qgDOOYI7OEGaLmMA4UEumNUvbyYjIjyPSaNJ0w3ys3iX5mYcDU4gatrEg-2bvvoG-R7w4YlsdXDCRvlLev-JKBxIGX8JrW5GLN8ZQgrNIK-lupw42BLhyZez6WVtXB4Bq-0lTJy6sB9iTWFuaXALTVt-nYzEsQvyCjkJrOpcOGp9xDCYnQxDJLaVD1yfdf8qgUpGZa7eTdSsqvgG91t23Jq_qgjs5KXlgvC_SRCRNrNYmJLtQ4q2a43XW_JxFuNMSZo0T2Aj1AiPLXM6X7V412HWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEO077DGA6ph2X-zAYfHDqAV-gxCZS1KhpIgXROU5hlPmqqnDkQdE_jSEvwyxhWF0dmtMsT_gQBm24g_noHD7oCfJL1owvcIRHL84GnHgcTPe1qUW43lYsNSq_QFMi3VE00-SuI0703fahJEC6OEft2K_cz4ezF1eBcashvriCXkcK2XswN47S2Fw8oCFqz3Hiczn7B1JTjancpJMZTngHXAklPKbc8BrW_jc30alflPDffhCjC3crZpqPkgv5Z085O-LVd4rz5ZQKnEtjfM9lB2DKJDnQh-k53X-J4HFX-5LqpED9T-fkBcEyCcQALi7H7logqDEbbk0SdLGSRzjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=tIUlsuGZGibBkLkhhhHQaiEtwLF2bNqriNcjau7WZ-tVMPJfzbGhry1ELWIZXqxzQtksQVYUJ583H5MaexHjA6tik1e93w2V_OTl6GgSKKckzKL3EW10amslS56ouf8PQqPyA4dAJyOVwsC4QCA_8LJjyBs0NmVqnNwLFBVVyHr1HKVoJUZGx1MAOv0MZ1RNdkiK4yXj59XuEn5XK8CD4bOnRecZaVOpW-GwaEFX5MjVP-mH5CKu4zdaI0PdCi4rpPH87O9WYK5X1dbwleiEKCJ_czERJoVdMMyHkWaKihcUfFF93maXMT_HL1xHaNc2Lmc6LR1BqszM-2XuAO2f5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=tIUlsuGZGibBkLkhhhHQaiEtwLF2bNqriNcjau7WZ-tVMPJfzbGhry1ELWIZXqxzQtksQVYUJ583H5MaexHjA6tik1e93w2V_OTl6GgSKKckzKL3EW10amslS56ouf8PQqPyA4dAJyOVwsC4QCA_8LJjyBs0NmVqnNwLFBVVyHr1HKVoJUZGx1MAOv0MZ1RNdkiK4yXj59XuEn5XK8CD4bOnRecZaVOpW-GwaEFX5MjVP-mH5CKu4zdaI0PdCi4rpPH87O9WYK5X1dbwleiEKCJ_czERJoVdMMyHkWaKihcUfFF93maXMT_HL1xHaNc2Lmc6LR1BqszM-2XuAO2f5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYXVNHKf2X_t66JiUGJz9fzJ_0CMUC8wCO21M8dHj0K2jhCxCvj32kOsu-vsbYhXPOoVc5IGC3-42Sk-nKfTkGQnCQ-Dgk1LFXv5ZjTuTm89imNQJDvsOCYzWG5aARZsKxS2uQ8yf7BRG5hEn8whk7vnjQXLP_ZjrTxL4koymu834ikRH6-uLPsxKTKqJbDbrA9NVEKHEYDiFd3cq-Bqjzaq_-8i9czp9yDawqjgFJhcY2eId4QPMmUrooyTImxp7Gqmzettbh01B7b1_5A4LU7pfcmwTeZ2X-fpRAliJdU66QPxpG80LZ9jZnfnrBtGxx5sZusohSPJe7aDGLStmL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYXVNHKf2X_t66JiUGJz9fzJ_0CMUC8wCO21M8dHj0K2jhCxCvj32kOsu-vsbYhXPOoVc5IGC3-42Sk-nKfTkGQnCQ-Dgk1LFXv5ZjTuTm89imNQJDvsOCYzWG5aARZsKxS2uQ8yf7BRG5hEn8whk7vnjQXLP_ZjrTxL4koymu834ikRH6-uLPsxKTKqJbDbrA9NVEKHEYDiFd3cq-Bqjzaq_-8i9czp9yDawqjgFJhcY2eId4QPMmUrooyTImxp7Gqmzettbh01B7b1_5A4LU7pfcmwTeZ2X-fpRAliJdU66QPxpG80LZ9jZnfnrBtGxx5sZusohSPJe7aDGLStmL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=RkjxdEFduq35kE2vRa6fyzzLjLuVn8y9jcTSGXZDDbykYxfJPmUdGlXnYGZNf4FyJ-QlA7FaKD6hoe-LFEmeiKbfPwAbWCikrlDEBbKGLGo0A8Q8ed_ofAA2xmwletedfwZT_eZ4DmwuXeG4tfQoOthX9R86pc2D90uq-V0SvlWqDw1FnDXKi32MnhBSX3ODgYiAd8efkJG5GBU04yU1X8eFuWa3cMPwQWnubxbDsqN67lprosQWf52M3MD6GZDkiRSE4Q6assElIXQffeHMcr31hRqJ5aDEp3n5euM9yFhznG9P8Qm1OcL_PDDSQhKqGkdwqcb_DTDTlrcl0zbAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=RkjxdEFduq35kE2vRa6fyzzLjLuVn8y9jcTSGXZDDbykYxfJPmUdGlXnYGZNf4FyJ-QlA7FaKD6hoe-LFEmeiKbfPwAbWCikrlDEBbKGLGo0A8Q8ed_ofAA2xmwletedfwZT_eZ4DmwuXeG4tfQoOthX9R86pc2D90uq-V0SvlWqDw1FnDXKi32MnhBSX3ODgYiAd8efkJG5GBU04yU1X8eFuWa3cMPwQWnubxbDsqN67lprosQWf52M3MD6GZDkiRSE4Q6assElIXQffeHMcr31hRqJ5aDEp3n5euM9yFhznG9P8Qm1OcL_PDDSQhKqGkdwqcb_DTDTlrcl0zbAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fve_tjAzLnn9Z-wTslNxBvS2jXcEsxyuhNY0-hHCcDRl-YE_hFwpyg5CoBk6SqzP1B2nOOVK402cC7wZkP76a38oUtFOoGFpTwYAUYmMYl49Op1PGNd1k0T0M-QSquTKzou_gubvCwV1NL0hbdcLEcJwPtWCKK3eyZaklgBitxHzYAsh_hsoJJnX6oGQcT4R41GjsMSwjf6FGWvnQG5OLunNPFkJeZ-ezuRD7xys4tQtihSI6L4dKB1F8NPVCPdeVvmnTOFD9kYwRCZX2HmXQZPz7sssDiBinLS1M4UhANHGcDy2LKo3EZ75QLKroNjmgYiiyeGQnz2RvAbOiL7PNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHHBArNkM2uIeA2r_kYr6q35OobjtIcBf8jGQJScIWfCJ6QpUYYx156L29D-Zl4ECIahDXR0jujIsDxCOpZA4EwcLAO7-DS3WPhYhZRrFJ_a3zL5UOgNfNgHU7xnklvTBdPht_93nSlW3TkrcGK_nIT4aUvgr6VOq-qyRSrV8N_4ar0Yh7RYlHRPRSFqVslKcqcGNd-9gqoAhUvSLMdpwuT-RoqRGRISk0DWqHOBbl2_gr1WDxXup-AmvO4rKSP7_LE0WUIWI_fHBJm4hTkk9UPskVCXjdr9dfL1AIQ7_OXUlsy81Gug95hNHePRin0ris6hASWkSIo2IPBpOwFWhRV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHHBArNkM2uIeA2r_kYr6q35OobjtIcBf8jGQJScIWfCJ6QpUYYx156L29D-Zl4ECIahDXR0jujIsDxCOpZA4EwcLAO7-DS3WPhYhZRrFJ_a3zL5UOgNfNgHU7xnklvTBdPht_93nSlW3TkrcGK_nIT4aUvgr6VOq-qyRSrV8N_4ar0Yh7RYlHRPRSFqVslKcqcGNd-9gqoAhUvSLMdpwuT-RoqRGRISk0DWqHOBbl2_gr1WDxXup-AmvO4rKSP7_LE0WUIWI_fHBJm4hTkk9UPskVCXjdr9dfL1AIQ7_OXUlsy81Gug95hNHePRin0ris6hASWkSIo2IPBpOwFWhRV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1HxFk6diyHTbT_TXW8Jl3A8t6GexEOIH75Y-uqs9FXTPTuzDOtqdngX_IqBq-2jwvqIsNOXXYKn65J4od8K3NzQj7lwr9tpAK44vTLPku_t-cCvWNDvM7LsFuguP-0fM6pg2Rv9SfDOfdR6XIkKNeuKIAJk3HdVXXTGChtFtwYtEJpNIkBQzUJEyrGjQZmMTaNtCUC4e0BlgRtv89Lc7q9WXVOTXflTP5sdfoHIDuN-TRpOhk00VzuT8f1_jMPYfcg9zq-yf3yqz6vzCdxjy_Uu6utkT0TDvLEpuMylWG8BJpTjsrMw9VVdrI77vVClr0kutaLd7ArxA6VbBntAUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ch70CvFKbv0BMilm917dHgMAkmK-ddAuP6mWOiSaipZA0oflirM5GMfUTCE9_3-9tN_Gmw0pGiN_t0tuPsXoyRf5jdMGNyghK6vMDLGfxFHc2Q-keWzH8HxxAQ4S0Oa0X9QYRSpRi7lxq5_bxSb4UDBBuy67Ty1qkHFuLipK1FoH0PeiIVzm-S8xepszXdHh0xUBsKYzRbqZVlHzDCYIle_BLaS3mwW1Wz0VRnhH7WgXfSf0aEF5I_4IIbrARiyDiWy_-SnL9X8_k0_tQnp7dWVrbD8fMV7SUCBLoMEPu4eifPyncHno_G3lr5jZ15fG-2J07z5AvAkHfKSqdGMBig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ch70CvFKbv0BMilm917dHgMAkmK-ddAuP6mWOiSaipZA0oflirM5GMfUTCE9_3-9tN_Gmw0pGiN_t0tuPsXoyRf5jdMGNyghK6vMDLGfxFHc2Q-keWzH8HxxAQ4S0Oa0X9QYRSpRi7lxq5_bxSb4UDBBuy67Ty1qkHFuLipK1FoH0PeiIVzm-S8xepszXdHh0xUBsKYzRbqZVlHzDCYIle_BLaS3mwW1Wz0VRnhH7WgXfSf0aEF5I_4IIbrARiyDiWy_-SnL9X8_k0_tQnp7dWVrbD8fMV7SUCBLoMEPu4eifPyncHno_G3lr5jZ15fG-2J07z5AvAkHfKSqdGMBig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=G48scg8cmkMP2CtsqzxiwdNvn6AmXQBp4uTuYuqxWLBxQASlhgZVsij9yNDwiNLZOya_zkSfMlztshrD6mKAsbL3-txExupZcb7EAVqX_qheM7--Y31XhWBRGu43t74G_VRFA2Zt-q5QHpyE0bAHJzlMYOiGNS0RpeGimaMZHRjc_GZwovdGR3129K_S6zjeYanQElMBKFVAwYHUdxrfWmdv3_8bBwVV49Jigz1MVdNOg4oGVi-RrMXqhtAGZXap-bSFsdFYLrAfxHdTS3DBL66arKdcZRWAEhjrlCqBZ2w9ZArXqNVexscWZ1WVloWS1isrZfgtKpmP2qiP03S9Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=G48scg8cmkMP2CtsqzxiwdNvn6AmXQBp4uTuYuqxWLBxQASlhgZVsij9yNDwiNLZOya_zkSfMlztshrD6mKAsbL3-txExupZcb7EAVqX_qheM7--Y31XhWBRGu43t74G_VRFA2Zt-q5QHpyE0bAHJzlMYOiGNS0RpeGimaMZHRjc_GZwovdGR3129K_S6zjeYanQElMBKFVAwYHUdxrfWmdv3_8bBwVV49Jigz1MVdNOg4oGVi-RrMXqhtAGZXap-bSFsdFYLrAfxHdTS3DBL66arKdcZRWAEhjrlCqBZ2w9ZArXqNVexscWZ1WVloWS1isrZfgtKpmP2qiP03S9Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Jc3KP-PGt-dqjCBDC5h7vCzMB_bw_IU9QjJRr5kOKF2vmCugUvjTKLrRhWvJZGE4NgicuNwCkQ2xXHagx--LM44b-17LEELD5bOazOxiNKXrRymTAm-t-pZOg0RyO_1hnFQ9n_OSuwe7xPk7baKG0zj4N0S8AOb5H4n7b8WtlJSwrayhKI-3TQKaCIba6-Qlbftu5O7rpQ9WYR9BmsHC9bndn42kEL-3E8VsUDa40n4zPv0nNxM0sCTF-Ta4llQnXX5weibmvR0X3NmjjtlkewIJMAxWkhsCKXSUaBldzjqnf4Iv9iWRnKT3JugecWAZRQ0u4TykpM6U5rlv9sXFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Jc3KP-PGt-dqjCBDC5h7vCzMB_bw_IU9QjJRr5kOKF2vmCugUvjTKLrRhWvJZGE4NgicuNwCkQ2xXHagx--LM44b-17LEELD5bOazOxiNKXrRymTAm-t-pZOg0RyO_1hnFQ9n_OSuwe7xPk7baKG0zj4N0S8AOb5H4n7b8WtlJSwrayhKI-3TQKaCIba6-Qlbftu5O7rpQ9WYR9BmsHC9bndn42kEL-3E8VsUDa40n4zPv0nNxM0sCTF-Ta4llQnXX5weibmvR0X3NmjjtlkewIJMAxWkhsCKXSUaBldzjqnf4Iv9iWRnKT3JugecWAZRQ0u4TykpM6U5rlv9sXFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvuk1gGXa1DMo0-awUkYR2g8lm-2804Ambh7eenmyipaJUUsjXTUosQaOeHEOdejgH1QREbECDHR_RVwkkOBye_VjLY0uUNdRPyCWth1F0xgysHiSXqk1m9eym40PUH11xLZNo5u3mO0thJDNB2GocDlfLg7veOKy3_OajVAtWFgTT9prQW92vlpx5MdmI4quy4gjhosA9Rb9gNrOZMJDvKCrudF2c1du5Yw3-uYAKDWDvwo92E5VpsaFChdijB3cbzSPxV6N3n6zOnGG0S7DxDYwRG-v0NlF8iXzBqM6bCkAe_V1k3hQE-zXrKQ6Pece8ytmcZKFUYgkUiZKtNRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRN9yc0GHPfTbu4DYdVQNV-6KmJCo_Y6YhUp0a6bLgAZHgcwDnZR5hfvZmS8_mYAnyhuHGv_0TrkjaW7A0_hDz0_UIG_etrhcHjyZCoE5XaHF6p4aaF2A8OQHoLk9QwuxB11Tj94MYl0eIi-S6UMb5po8Hf7JPX1IPpd0MImb63F0lRAiLBZ5y0aOLB5C7c5_ALrSSeFNGVCbjA7DsMOT1g1rnI-QAWhHoo0n21GdHPWbhk7WcN0RRe02GwnWnWQAXafNX3O8FsZZ0Ih-LbXcGVPqC5GaRQMi7bYVfoGknZMbAtstdcCPb8EPvxwSvyAWyZQ9HjmMVG_tBlGV4kIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=hVgHhMZMH9TbjiVqDFMza-Ae_R0GleRUzZFEbEbNTgec0ey0gfZI5JYeU-M5CFa0Zny4XjWjPirx4AtLoFEbyiU56sHyrNHnvaXg35PX4pjASfLE9XXthFDFl89A56RhEYmPs-k39l1GhRAZbotG6B9hLM8JzMrUBirds1htRcnnT_IjpQcjzB5z3pRgPQrQblVB7dwWw4s7QKINQ4uwAq0SnUyl3jqLeFKYboK0DiyJdIPe7-xcDpMI3fgdWD8G9Xheq4nLZfNBFKfIf1Mv53aL9AyUZ1zPCPhw5uHq6gMcLmWLbGByOY6qn8RqoZEtSPq0cOa3pY686pr7FRx6qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=hVgHhMZMH9TbjiVqDFMza-Ae_R0GleRUzZFEbEbNTgec0ey0gfZI5JYeU-M5CFa0Zny4XjWjPirx4AtLoFEbyiU56sHyrNHnvaXg35PX4pjASfLE9XXthFDFl89A56RhEYmPs-k39l1GhRAZbotG6B9hLM8JzMrUBirds1htRcnnT_IjpQcjzB5z3pRgPQrQblVB7dwWw4s7QKINQ4uwAq0SnUyl3jqLeFKYboK0DiyJdIPe7-xcDpMI3fgdWD8G9Xheq4nLZfNBFKfIf1Mv53aL9AyUZ1zPCPhw5uHq6gMcLmWLbGByOY6qn8RqoZEtSPq0cOa3pY686pr7FRx6qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZteN_k_D2kxhydHDtx8YMx6_MEPcaFxvrO6WSg9O0YZZBJJc7n_tCvBZAn8Gbi2u2bqhmlkYpIpyiv9oC7_PvZUX5iba5isRq5B3M3gz-PKsW3M1oGM4AkkXscssHJgWM_BSHsTl_rf--QhefE0PsT-Xj-JuWB8XqDl0V17Ic9qgw6dN1jIqNWACh6ouy1W44kC0NAHXrkDQ0qKfInS2PmPo690zmazztdaLSgZ2gvvMPJuqWz4n3aQK2CWMNg5xfMy6mhQCjCXlv-ZQgSMR7elTQTKjq6RqrFHWZWhYMr2jssep355gX8SdPaflZwoGzWGXJUT75emgE1Fud3_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKZmavaEAq9jEynn-1D4a02LFnIZfu63eR20NQeuerGcBYZ1GgdPKaINcdfFfMRA9b5OaJcFpzpCg_WDMHSacZoFaaAcqkQ6VknmWHGpQIJh067bTZz4s6VaWZsAgpGAZz7k889wx4vWkzVcA5o6rtV1WCfqBpfTLlZIQtgY0AiZI9RD9vEijpc03C8xebN6tA9QocRGyizXGkVR_xi9so3r4bPh5cgeyxGFf2jNf8meoJBEE3iwoBskpR28MSA79e-GUq1OTS78KV427mvh6aWsLjZjRL-p9iXEf-JR1gm_CpLlLkv61DJGyr7SPUFRYs_khOPJkKnIeYVPwetp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=t-2Tc6_demnDLNICSvvD1flm2fl1lcepaUFML239uSkQsHhzTLerGKgnpnmyH6y5R56RUnT_RECcyxBM359ihSpSYYCaXBycA-meLivsdD9FmppjPYpPK_kLki8Zs7HcA6NX3patKoYZegJd6fLtP6MdQwfI5DFRQmqOAk18xlgyhcpq0Mji5zOlWgeM7k6lRWL05vDLmUZKp8hxCHFmJsFLMZ4RM5g3_tUzuSAP0ovTaGzkbELbTTHcSl7dwT4S3Bx-CxPVF7duxfKcy6hGngP4lXg6Gzq379MNXtEmyVkVvAL4EbDaTEI9Qq156r3QrMwCVprYbepuqYcT-13PFLcdwgU8M5bLJWWA2uyPlQmeQR3y9auCOQYu8IZjlN9P0E52m53gHkCr_7ByX2h6reHHb1uABpjDQ3h2-8tjQQpqJ6MQEMVf3BuV3eZqw4pzvPYlbuarOkOcKzCaeOknTIdQ7QH9q5HBK3dmb6CXtxUck-W1G1KoPkkZOMCe7PYp7J-BksBiRlSaVRm-rD6FaW2WyleU06UdzODXa8wneVKJeY7jBInL2CoicDH9p18P1jehpVgHa2cY5Hlf8Hw2pZSXbJ8VicHyq3PzE9ztMej__t7o7LHOy8jiBSjCZ_41nPPvxLgSyIvubdeK63UYpXGQQghEnrZU2eVN-QAG6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=t-2Tc6_demnDLNICSvvD1flm2fl1lcepaUFML239uSkQsHhzTLerGKgnpnmyH6y5R56RUnT_RECcyxBM359ihSpSYYCaXBycA-meLivsdD9FmppjPYpPK_kLki8Zs7HcA6NX3patKoYZegJd6fLtP6MdQwfI5DFRQmqOAk18xlgyhcpq0Mji5zOlWgeM7k6lRWL05vDLmUZKp8hxCHFmJsFLMZ4RM5g3_tUzuSAP0ovTaGzkbELbTTHcSl7dwT4S3Bx-CxPVF7duxfKcy6hGngP4lXg6Gzq379MNXtEmyVkVvAL4EbDaTEI9Qq156r3QrMwCVprYbepuqYcT-13PFLcdwgU8M5bLJWWA2uyPlQmeQR3y9auCOQYu8IZjlN9P0E52m53gHkCr_7ByX2h6reHHb1uABpjDQ3h2-8tjQQpqJ6MQEMVf3BuV3eZqw4pzvPYlbuarOkOcKzCaeOknTIdQ7QH9q5HBK3dmb6CXtxUck-W1G1KoPkkZOMCe7PYp7J-BksBiRlSaVRm-rD6FaW2WyleU06UdzODXa8wneVKJeY7jBInL2CoicDH9p18P1jehpVgHa2cY5Hlf8Hw2pZSXbJ8VicHyq3PzE9ztMej__t7o7LHOy8jiBSjCZ_41nPPvxLgSyIvubdeK63UYpXGQQghEnrZU2eVN-QAG6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETjoAfHpz4HkFEcILpsnh7aWOASCiuUKvDQQYMeCvvm2GiB-hTwssaooc3N_SYC8XOMKbU3ZlM6jkFje0_BC5ZNgaJTpU54ZBWqKVlkvidMwVKtCYTQ_Teqtqh6drpi1R6tRsKfU5_hLCq2jKRwt2EjcFGo7-5Y4TBGb_Qvnx_eAOzhhUyffcmW0ykLKmDgMnJPByGAfAbs7-M5RXqCv_6fLXguZKPRDNGqx1_N3NPr9OusVHfBcQlUx06WRiLhj3r5VgpJG2u49Z9N_CXUXlJVSOHf0fCXyDwrxHoMq5pkqAPVvhJOwPzqnI88TvJXfEtSZCVuc-xLY4KYDfuxXrl6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETjoAfHpz4HkFEcILpsnh7aWOASCiuUKvDQQYMeCvvm2GiB-hTwssaooc3N_SYC8XOMKbU3ZlM6jkFje0_BC5ZNgaJTpU54ZBWqKVlkvidMwVKtCYTQ_Teqtqh6drpi1R6tRsKfU5_hLCq2jKRwt2EjcFGo7-5Y4TBGb_Qvnx_eAOzhhUyffcmW0ykLKmDgMnJPByGAfAbs7-M5RXqCv_6fLXguZKPRDNGqx1_N3NPr9OusVHfBcQlUx06WRiLhj3r5VgpJG2u49Z9N_CXUXlJVSOHf0fCXyDwrxHoMq5pkqAPVvhJOwPzqnI88TvJXfEtSZCVuc-xLY4KYDfuxXrl6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=j1EBYjRT8i8fjTcox2QXqLy-GRZ1unphNFnP25BTSFGeTKk-YhjLXeRljRAwouzS6r35_YfOiGZozAwxo-mcrdYE2_Ypep_2nh5HywylP_clTPNjuL1qlb9AQQ5rDZH9Ud4cK6DSadXgHGiWUJkhdbF-fVONp8_CtCuFHc_ghoN57xK2CyZeEoey8YZ9Im7PKPAAkZVV1xjB4dPgHx0KSomDtaJSuxXagLSHo2DSnT7ps3TUr58UIbm8krgwPV5GkqAhG4YHXHFxT35aDjhN7IprIuUFa8NaBuOpg37uxoUMbCGahvbckAwTc7l0uhGXEL3U6yNtoAk5yrJ89UGYBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=j1EBYjRT8i8fjTcox2QXqLy-GRZ1unphNFnP25BTSFGeTKk-YhjLXeRljRAwouzS6r35_YfOiGZozAwxo-mcrdYE2_Ypep_2nh5HywylP_clTPNjuL1qlb9AQQ5rDZH9Ud4cK6DSadXgHGiWUJkhdbF-fVONp8_CtCuFHc_ghoN57xK2CyZeEoey8YZ9Im7PKPAAkZVV1xjB4dPgHx0KSomDtaJSuxXagLSHo2DSnT7ps3TUr58UIbm8krgwPV5GkqAhG4YHXHFxT35aDjhN7IprIuUFa8NaBuOpg37uxoUMbCGahvbckAwTc7l0uhGXEL3U6yNtoAk5yrJ89UGYBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
