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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 14:00:23</div>
<hr>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B46qcDMo6RYxaj-UxKkLkDM9oJWBs4YdTd2cuaciChQGftegZ2ON8BJtsJAhtasxb_TispDy_dF4vlsAxgRb33WoEDrjXyUBqJ8BxnlDp2H2oFkTzrHIqWMdib4LgGOj5clIVEBmaFu4Q7kLi68wAi26jSQ8eMffr-c7UCQE3nKGaMHI8IkH8LCUhAyLf_BA3xk6NYfFPVRAvyTp3KscA0XUsHscs4AwFq_HSOGCjQwO-Clks3Z9Q9Silb_tVWsCsf9IVvFaV9fz1KuE_vMoXrCHggX4OV9FcDePd76m4-o37QuF1WD6pN1Hc8y7nVqmAnyqK0SdZlJmKO5ZdGvRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuwvQxP7MWyGOP7Jy4AhvuaJFv9Hb61w4gpKTyBcBF6F7t1GtOXMxj-_GiBON2JVB_wwXTWfP6bDTk-g_9EMrxsq7f4sDpL2a4Ire73jXSh8akgW3hVulH-y5j7B9FXJNW4ZVZ7cqiROawcm3MNzNXVeyOxLhOmqjCm07SuFHzf82FBA2w1esHrBZkXggWWmJ9P0dZLCHUJ57ZK_1ha-X15pOKZ0lwfDLvSGeW2NbXdhMJTfg6gC3wj-OZwe4gOjgAFOTqQGiLWAjQqja_cc_2EzaMzNJ5E7jb9R2gIRvXHXojHyD1dPDBXB1vtrX8BWLbCyesP-hr5B6dBsgfy57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=lZJVMhtnh4i3dU31P7Ez6QGcWfwMBrteHdZ6BvY7Vkd9fAEy3yYApAUYYJMRE7dot-HqLir-tIqdYX2A4vOlWzt_AhcYYYDTJtarSv8dgDGTSpUdLCB4lrCsUBmmzAJ7i7eeUmfFr8sb6xHsiq8crQ0vZDymA16HIZdmf9HmIRQQU-lNKPoq7e4lnGCGyIBMM196EuCgx07Yb0rkcYnehtxgcugAg2lN6FVbiZewQZjlt-qMUoDw6KRr0Uh4Z3EQihkrwR7Dz2jq1-nGnUI9ZzU9kodWC-01fL6vQysdDhhkAvv0GLdSBNMjXN9YyXRB492aw4nDLJKNZmbSjiU-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=RyIjoGOLK3HCkmoJofVVleghvHh-8rMbwcG-JCqHfx1ljWy14CezMMp6vW7szTq60pKelKsgomjbKoNf8zC9WeCdlBg-t02HM3FVWEaatqKru5GIZNAY8pwIcJ6VKrFlO2PGTJKPY8z35dNro0yoKlnWLi4GS6snd530KbCpqOZYqdiYMS4vNSIL1tow89yuEJEnyYJY__nZQAWPfgJg3H31hQI2HA1hnqjlcKDSwujqHipLgGzfAPM82JNHOvkBHp68EPkWd8ytItbKgsh1G4FHsHyfw2P42PcpTcDWMW-aDylOLF9x4WjmTq8pJAVWBZfgNWqecH90SrGoxK_LRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=RyIjoGOLK3HCkmoJofVVleghvHh-8rMbwcG-JCqHfx1ljWy14CezMMp6vW7szTq60pKelKsgomjbKoNf8zC9WeCdlBg-t02HM3FVWEaatqKru5GIZNAY8pwIcJ6VKrFlO2PGTJKPY8z35dNro0yoKlnWLi4GS6snd530KbCpqOZYqdiYMS4vNSIL1tow89yuEJEnyYJY__nZQAWPfgJg3H31hQI2HA1hnqjlcKDSwujqHipLgGzfAPM82JNHOvkBHp68EPkWd8ytItbKgsh1G4FHsHyfw2P42PcpTcDWMW-aDylOLF9x4WjmTq8pJAVWBZfgNWqecH90SrGoxK_LRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXxSDLlUePGQsu6_bHEPLaz7rerSO839oNpE5JzXuURKpLtG1ehiTDDqAI58tbtaezQTzTI0YvGWknhYJxP3cv43t65JSviH0rhlDsupU8KLRifmakRQWpOwabJAa-IL86VCvUEoH_2nPexnOeBjuo1s35L7ysIWf5rT6mRjUxac51Q4vtUrfberdinlpAGEYDWKGyGdQrAKhijZGz_HCyTtKtFBIYUxR4r-F1QFUiSUYAFjRPPJzcP5PYSbNbzESqt9fSL_E9CGprvMjo590bxhismlq0oVl3ySAdeEuLt9mCNfwC2Mx31TyFrVAWqXAibFiqem1K15fSRaux-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM--pm2aXLrUwexosohD-Fm4YjMX7R9A2ubF8-GPuyt5hisIIlhVjmO2JyLqhOX5Oxz9zIOiffEqYjxyACjR2MPoGsBA2t6aSIRsjpkcml2lZ17RupGxeaWeWzu3Pfe4EMiKamhzq1aN2EYuM_lnUMJcO1rd9sjJr-t0-1sidfXzRn-57eLvw3N91TQK6N3SJ_F2qP1-iKdXEjdcbqtAWFmSovuWHjpYKb07epUTxesOJe38uH6QVYca8RY6duY-0koiH6LdM_ZSjCqvVPSdx1g28fHSDD4xRk1pwyNvDpaIe3KOXDgOoDqgH_uYQCk7zaoRz9E7tvYI96OG-00vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOpDUgL7BgRgOkqy4jb7QdzAU7mFEjK1zKzusFAPf1p998ztN0LY6YyJ3f6pUuKcTPB7Ce9tit4vQpzILhHll6ybAQad_QNR0nkA-u8sY_dUY8tegmfO-tNVgNoYukMKWiL9QePkZ6GpP7wrUF-TEBwL-Fjxjo81LYDZHM8s9-KFtHvolKuB-WWuwU5lZrwj2Z7J2iH8BpOK_Ec6x2Dbw-wW4fap7reuAhxcQAb1i2gM88er6MGA1wL-NZaV4cP3q6PLTKOoFLEuuqFPD4gV8pEutgHU0YW7m4hHTHKAwcTTZOyWIayw8r9LhpzpNfsWVa0mUBiLORvQszZ7Ht0NVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYTdN9zNV9cLsFKGUHColQWPjlFUyhpOu66srkTpn0MrOeFyy6NDQWmAbFf7uqB1m_u9mKfQ-EwNbiP2l66Byt_Tfm-mjvuL_Genz1SflD7aFO99xH05lbI-SN8-OzHIXOSdZpXLX_nEOi7UQourjaF3RWMUxP28Fq41LevdGRUtl_b298pJYLaICDPGqBKvj7JgeKRMq8RKGezqQaGErlpyBbvik6pHrPkO5Ud9iElH2O9cRubuR5JoRp5yufoP_Vkkta8Ljcme20h03ohi7KN0NI1E-_TVxxXnPetQ9dnkqC2MP3vvNvge1oHICgjU2j--pxv1SPE_S0O5gZaHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpBwKp_4DzTmGHrZRI2zenV3Tgq4Foc5D2HYST0SPzEUuV2Z3Wudsz6OL11ND7O3FbWW9df8P2HoEYfi5874ci3RzqJ6gI_NBboKmQN6dxZzq5vrPCBuF2CwltUkqIIi5L_px6bw8TpX7S3yeKDSa3AJDUpx48pQTkMqwOdSjrY0QeV6D24_ytgIKoG7Gq06fe9Z7pXu9rJwTwOWV2ZfomQGoX99AHDoW0pgf_gDKxTCaR5qK38XKpfex9ekrE-0qz02P_9cGmeOVntOPwrBeU6IHYL6wplTesoPeA8G4XFJbhLb4CpNM3jJMk_IACgIb21Yjv36ilAnici7IaQghw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgcCvjTFOR8GqhJu-3Sv1maZNtRAk7_pAFM4NbLeZWptBUz21ZXN6rKAXnSlyq9RkjbSdFnmS2nxilZc3UGx9gDQAat8ilhnlD9RvZehnOwmMv_oSiIV8yfVaP4VhseVjSept0PgFhCvweVljo4j8f7OD_QBTaY80ZmRj8gQyD6ssztqq6-SKvFGpJXlf5lh56ovq-VnI9Zb7rNx5Ks86pc8c2h0dzN_h88mtqrnSEuzRPtHi0aF2G012bcbKpIlo7vvvDOlb6U6YIK6TmjDe7z94acOONoG2JVxBkX6tWglgmyEfIpHmjSbVCkphwzoBXgtsyLFAhGjOhchDpA1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7j5ZPaOjHzDn5KKzhHO0iHeh9boNWYWh-LAf5AvcPlMGG8RDTNi0TBGz_LSVqHjkXgTipIk2p7kvuEbSnhZ5FGA-C_0U7AX5h_N6eO1ElnXnXD4y6b1XyhMtd3NwzRGyvefQSxezzNRyN0Pt5RisDLu05FwzCT-PN8BpBtM2YrzbLeJQmti5z0TVtnzKmjg30g_E67xkoOGksGBtoGPnP42peU34gAZk6MK4YPE7yptaLy3BNOlJ3mmJFx_IRhNfRiHvpeEaZwdRAnD6f-OQAD9UWBqJLPhMYx1WTE7d_sUtiP-UXJaBETrl9KQCR717THSqnsZ0Kuq_se04ABa3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpAjo9IkgXXJKQy-yPJbyzvWkD5tDLh7gx_RtBswznmSqvMvL24WTVFPVA8X1LVq1daIIBZgpPuBsho_puVWu91HBzbKf4N7SejSPBG9etTdwMo4GvuDwJEqkTrE9M8bZF2Fm91O5HoZlD4wEmFwaO6TFqmx01NbqUj1dn5dnsdLx8pRw2ko09oG9J12J2Ho56vtszVDLIsAMRRSl-t2Zh0KwmkKYac7Z210shFJBR0ce3fOmrPFcXZFCraS7w2Snr5XyqViU4KmC1CHFyfo34rAJX19d6NwP7M58HT8QiIfpth3SL6ck9rH13KwBgAUUwp2egaPuz5c_e4giVQCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaoYyzmcE66nYz_iNDFkj26I05FEp5Ou2lWla6pEeEd5BcIGRSx7GGQuhy-ZobLGz-9e1-4NAj6VEJDIZ7_3OV1dC5Ul7erCY-fE8g_uuYRJir7AsvZ_ZCZDYNlgO_igndqtBG9rwJr21jKa2LOOcl8q9MerxOoUAyBTZBJdv2VXoVAU8DN-e_bv1RW9xx2V1ZEq4jU1X_X7nL68JAL1vw16XNpucu8iz8MZ2G916wUN6LVg3booWZ6tfe7X1FCispcu6ub94VdcdH_d5RwNSyrTkfLgQnUIs0lM2tJHHKWqes5mgTHWUOoLLVrqGxrikDlCtmhve4Iid-Zv1KIevQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EIMbvwpsB1ob5G5e-1tMAxK5DQFIYXm3ZpAD551zVnnaewChOXYhFnKKWNX5cdDh_a3QkYHt7xP85AKjG62XY4BQQB7UFFaG0ovJHKFP5P-6VkTvHVIBR5sYvSMXwhkNwZElixIpBjcaFxLsMki7N1ackBcDf6yRtqoGE-SbhCRf5gjQdWIe0r9UTKCgrPt2rgBewgPLakS4-t4G-D-LKtS8b4r0g2BtzpBaieLB4f5AZXDF5B96q5JXfEfw_Wjcqbsm59AIYh3cH-zU561xuYZzFa7aU4zwaaaiG3R9kxVkW40loIMMA8Vs-xHK1kwcHCjxAG7oKyFdi09cYCPZGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EIMbvwpsB1ob5G5e-1tMAxK5DQFIYXm3ZpAD551zVnnaewChOXYhFnKKWNX5cdDh_a3QkYHt7xP85AKjG62XY4BQQB7UFFaG0ovJHKFP5P-6VkTvHVIBR5sYvSMXwhkNwZElixIpBjcaFxLsMki7N1ackBcDf6yRtqoGE-SbhCRf5gjQdWIe0r9UTKCgrPt2rgBewgPLakS4-t4G-D-LKtS8b4r0g2BtzpBaieLB4f5AZXDF5B96q5JXfEfw_Wjcqbsm59AIYh3cH-zU561xuYZzFa7aU4zwaaaiG3R9kxVkW40loIMMA8Vs-xHK1kwcHCjxAG7oKyFdi09cYCPZGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=l69xEVh_L7YnlqGlllTrwrvNp1tuIxXxFfy_S5V3X8GPMh4FY7ZpwM3QvAXuR-Kjc6sjGFFgDbHSbX1kRlBEJebMj4YyEVoveWwQimYEvI_0pMhD72E-NDnBNVPwKUAh6xdLD3AsHXB1Y3E38HX2XTvJc-K5Pd6KiIyLmrgkUrex4LvoeCDD-B_d1GJI2wShF3a4Y-CbgA4jW0Sm_K79O-KFK22SWlsX0bxPa6Cz6RZBZNd97QaDkslBavw8br3ZOQQj4k899zkpfTDtlQjR7Ep7gREU14mYNmJ2wc6mtnRNmGDPyo9Yo4hTrxdisVPpZsJaai1vPA_jr4Rfc-DzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=l69xEVh_L7YnlqGlllTrwrvNp1tuIxXxFfy_S5V3X8GPMh4FY7ZpwM3QvAXuR-Kjc6sjGFFgDbHSbX1kRlBEJebMj4YyEVoveWwQimYEvI_0pMhD72E-NDnBNVPwKUAh6xdLD3AsHXB1Y3E38HX2XTvJc-K5Pd6KiIyLmrgkUrex4LvoeCDD-B_d1GJI2wShF3a4Y-CbgA4jW0Sm_K79O-KFK22SWlsX0bxPa6Cz6RZBZNd97QaDkslBavw8br3ZOQQj4k899zkpfTDtlQjR7Ep7gREU14mYNmJ2wc6mtnRNmGDPyo9Yo4hTrxdisVPpZsJaai1vPA_jr4Rfc-DzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=iHzMa4dQWd9-lmPm5hSVYwML0NGOZItPiEDGmkECoyLpbA8Wk1EWU5LLIi9wQNosRmUl8U2cpmtIpCJDFKi5SJmicUDYqYsIaTwhfOlFjTnDQc7eq4sZiCFujmqoadlQuU-_pSAkmyjeRvsclp_Pq_YnUJAcuK3kRV6lt6y9Lu9jUrQ8tEpjEqNkl1MX01Eh4FmTkgg3uEwf-B1pyBOWsPPHQDwba4nnM1hpojKEGBYEyR1QxAQvnPl2UffePnPtV-1-L62TGA5vzTFeDGZgO-wxZ3xRTeT4wR_ox5bntcu9Ghu_72lgqLzhLjfzSPF__t1ipyTSxsfvjY8ClcSIRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=iHzMa4dQWd9-lmPm5hSVYwML0NGOZItPiEDGmkECoyLpbA8Wk1EWU5LLIi9wQNosRmUl8U2cpmtIpCJDFKi5SJmicUDYqYsIaTwhfOlFjTnDQc7eq4sZiCFujmqoadlQuU-_pSAkmyjeRvsclp_Pq_YnUJAcuK3kRV6lt6y9Lu9jUrQ8tEpjEqNkl1MX01Eh4FmTkgg3uEwf-B1pyBOWsPPHQDwba4nnM1hpojKEGBYEyR1QxAQvnPl2UffePnPtV-1-L62TGA5vzTFeDGZgO-wxZ3xRTeT4wR_ox5bntcu9Ghu_72lgqLzhLjfzSPF__t1ipyTSxsfvjY8ClcSIRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=GaecLS8nD3Yaspfde9_UZDYLL6RVM3JovMWNc27TC869UhxB7mi0u9Gt6EwGn07kESgL_yX0UzXQp_u6ctQRzZHYFQUJMmqwDdKt14jtGO-QEe-b7O7D-yfN21Q4wN8IDzDBVpPlFfecugz5tcDwvFhWDHfR2hG9n-dpY4Yu8irCkXIHmmyg-dygUOwLSNnfjzMO1hCq7xU-h-Z7F5xuXo5pJ7C5sJwh76CRCBaWHt3R2BFivdmkYeCmIsk5PGkJZyD1rbX69X2xBOfnAs757GNSf2MULxSCWnHL7vFw5h21QhP3wjU528Jb5BuBahYLYXNZGnEPgJItIP6BJGst8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=GaecLS8nD3Yaspfde9_UZDYLL6RVM3JovMWNc27TC869UhxB7mi0u9Gt6EwGn07kESgL_yX0UzXQp_u6ctQRzZHYFQUJMmqwDdKt14jtGO-QEe-b7O7D-yfN21Q4wN8IDzDBVpPlFfecugz5tcDwvFhWDHfR2hG9n-dpY4Yu8irCkXIHmmyg-dygUOwLSNnfjzMO1hCq7xU-h-Z7F5xuXo5pJ7C5sJwh76CRCBaWHt3R2BFivdmkYeCmIsk5PGkJZyD1rbX69X2xBOfnAs757GNSf2MULxSCWnHL7vFw5h21QhP3wjU528Jb5BuBahYLYXNZGnEPgJItIP6BJGst8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=cjU4qyzA_dQKE0ilK0RtKufARcq5yRhmgPAHWtwglfp7-OYUHLA9EzHF17nf7VT0MmtXFk2xYz5Oe5FWuHH6Bja6OugaitMNW4Wgrp-Cxs0g7P627Z2wNrTTOVaK9qHx62jchhlyJgvqDkomqpCWj37xF8ursznGjLKW-MGx2ZqFLhieWzW_Q-eEOSOBIC-OqBfzXwnddKw4QOmUKiZT8KCk-RPAhGqymprrxfF7XeNNsdm28eNM-wEuZnsvDBxVUN-UVogHhHENf1f1ei-WSycAeJr6qHTfdiycBCE5GMn-4nAc2AvIcq1lXtfvGjzeIq-e-WMsO-UTzxPKKKx1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=cjU4qyzA_dQKE0ilK0RtKufARcq5yRhmgPAHWtwglfp7-OYUHLA9EzHF17nf7VT0MmtXFk2xYz5Oe5FWuHH6Bja6OugaitMNW4Wgrp-Cxs0g7P627Z2wNrTTOVaK9qHx62jchhlyJgvqDkomqpCWj37xF8ursznGjLKW-MGx2ZqFLhieWzW_Q-eEOSOBIC-OqBfzXwnddKw4QOmUKiZT8KCk-RPAhGqymprrxfF7XeNNsdm28eNM-wEuZnsvDBxVUN-UVogHhHENf1f1ei-WSycAeJr6qHTfdiycBCE5GMn-4nAc2AvIcq1lXtfvGjzeIq-e-WMsO-UTzxPKKKx1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=VgVk3itqoHIklUjNgG1AVdWQuG5vwcNApHI_eZH1Jiief8jfMBdPm5ml8Dzx_8neJ3nVgLGWhU2i1I06SR0JFIplw26LtsJAdk02pQme6Om_-3_bxKqzRx77GLiAuci20CtfqZQo18NXjC_MKPfpHeqmvu9jMoeOeJfZYX8fLQkGvfDIcjQerut8jSCLfPoAXSAOX2mwjN-Uh3nx-5O-eKBjiwF3j1pyRApqC19CfJ6GxKIWNUywRzW1mN21BmXlM0DWzpGgbxUBs7XWrZIkxl19xI-Wtd9dZRhgInPZeSmJUUJZ0dZ61dYuQYz5kU10u4natykRXGhQ4lat2lWNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=VgVk3itqoHIklUjNgG1AVdWQuG5vwcNApHI_eZH1Jiief8jfMBdPm5ml8Dzx_8neJ3nVgLGWhU2i1I06SR0JFIplw26LtsJAdk02pQme6Om_-3_bxKqzRx77GLiAuci20CtfqZQo18NXjC_MKPfpHeqmvu9jMoeOeJfZYX8fLQkGvfDIcjQerut8jSCLfPoAXSAOX2mwjN-Uh3nx-5O-eKBjiwF3j1pyRApqC19CfJ6GxKIWNUywRzW1mN21BmXlM0DWzpGgbxUBs7XWrZIkxl19xI-Wtd9dZRhgInPZeSmJUUJZ0dZ61dYuQYz5kU10u4natykRXGhQ4lat2lWNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=QgVPlHFEkB_WzYPUPlc5gfyh5y5JXwwaIDNI5tRNtEloyKryOz_fyRt5eahuqvNOm1BvOaPqX0Yk21UJz7Am9eFFZHCeL4S3F5_QYLppJmwXhFw1CxSY8ZoDtk8bf8J4TDEAueCaLs6zva6ibSVK4_d4wi20eKaivNxVoqdp9KuSzpk85VRntmwUX-mpPtYgRs4SfzleQmHpD3ZCYsmwnt6pfaJLoTB2pwz_iMUuuY1D2mY0BuBWBpcbcAO91m_bwRvgge6st2oPPmBGuhBVP_7YkJiszpG7fv6yavebjtKtnLLGot4NQ3yi8S2H0HWddybJpR_bWYn7YalyljT_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=QgVPlHFEkB_WzYPUPlc5gfyh5y5JXwwaIDNI5tRNtEloyKryOz_fyRt5eahuqvNOm1BvOaPqX0Yk21UJz7Am9eFFZHCeL4S3F5_QYLppJmwXhFw1CxSY8ZoDtk8bf8J4TDEAueCaLs6zva6ibSVK4_d4wi20eKaivNxVoqdp9KuSzpk85VRntmwUX-mpPtYgRs4SfzleQmHpD3ZCYsmwnt6pfaJLoTB2pwz_iMUuuY1D2mY0BuBWBpcbcAO91m_bwRvgge6st2oPPmBGuhBVP_7YkJiszpG7fv6yavebjtKtnLLGot4NQ3yi8S2H0HWddybJpR_bWYn7YalyljT_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7QwjIhWDtv7ULF0MHpPpMWayWWNrMu75rBhtNEtoPf8zn9h_WNcSDCHOx_vEl0XunI2s7rECj6SwSJWsTs0KP9ekEMjkGmGp4K4qxphn2cD_pJuD9izxBdGmbSB8Pn7Gt_Rhi63o7P7E1AWa6PO6utWN0my9NtKlwhjRX36gWDQEnJjzxHmmtjyiqnVcJMSlFDMJQE0VPJIpYzaROCQkkj6rrYct_ftRizc9XUIyLLhhjRtbmqmj6rnYEBIFM0VfrUOHSxz5tIboiLPmN6qdvuoPFr6-uFHClvipTmUOzwdkbwBRFiaznThCICjsQTl7ksCN200WvwqIcGu09ukWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=UgZo-rbnom5Lh-wEM6h2lAi72d8IPO7G6AM6LJY1ft3ebk7vXEeHCb8RQDMqKu-Bwf8-HyF46p8slOHpxl_jWfWZv0Bu_Qn6ukkONZaK8tjM0N72Y8ltxasfSuEebDVMaJEiTuI1SrpglW1mkJZTa1SQjQ6oqQpwpl5MLDTvrkkj0DdY70qiKVP3TwCnGiQrAzTwlKtw1C--qBKx9GEFFjHKuP1QlTW49UrPeqacA8xYIlP868025u3BIQeJHm6eqAW4zzK_8eVMKqH8yLmsSYEOsDvVpP6NHsr-BE8tC9NESS8MIWaIpQpaccy2KvXLldDeWVYUXD9gf7Vb14_y8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=UgZo-rbnom5Lh-wEM6h2lAi72d8IPO7G6AM6LJY1ft3ebk7vXEeHCb8RQDMqKu-Bwf8-HyF46p8slOHpxl_jWfWZv0Bu_Qn6ukkONZaK8tjM0N72Y8ltxasfSuEebDVMaJEiTuI1SrpglW1mkJZTa1SQjQ6oqQpwpl5MLDTvrkkj0DdY70qiKVP3TwCnGiQrAzTwlKtw1C--qBKx9GEFFjHKuP1QlTW49UrPeqacA8xYIlP868025u3BIQeJHm6eqAW4zzK_8eVMKqH8yLmsSYEOsDvVpP6NHsr-BE8tC9NESS8MIWaIpQpaccy2KvXLldDeWVYUXD9gf7Vb14_y8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=rEsyEM2QrC1FZBoBsOyMRtlPkORYDCMvI8P_Kn2o_T9kZuAL-8Bj24ppynDGVG1YZyyvBb7E8Ws5AP7LR8PJqCR5VfFBDIvKXF1CmRzFX0i7r8zBp2CLhnEVTpfLPPQfrQMuTdEzWSLx63UVs5nnJayj7Wg0YBFkRQ43-eqq_qC8yoqn6Qnrif8THYejJbHgHkhtkN02_1Ux1-3vqwu8rrhwpZ-zi8N9tsSp_cjKqjqVWtgX2cafNtJiq92pLZOxoj93b6r7x7I4zAjWkn4GopwhDjHs2WG6jTI09aHUcfIHnRXXmVjQDE2CDFQH__XcJXL_VNkx7iQIS-18J7VoLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=rEsyEM2QrC1FZBoBsOyMRtlPkORYDCMvI8P_Kn2o_T9kZuAL-8Bj24ppynDGVG1YZyyvBb7E8Ws5AP7LR8PJqCR5VfFBDIvKXF1CmRzFX0i7r8zBp2CLhnEVTpfLPPQfrQMuTdEzWSLx63UVs5nnJayj7Wg0YBFkRQ43-eqq_qC8yoqn6Qnrif8THYejJbHgHkhtkN02_1Ux1-3vqwu8rrhwpZ-zi8N9tsSp_cjKqjqVWtgX2cafNtJiq92pLZOxoj93b6r7x7I4zAjWkn4GopwhDjHs2WG6jTI09aHUcfIHnRXXmVjQDE2CDFQH__XcJXL_VNkx7iQIS-18J7VoLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=aur_Bwzpi28CNgiwo5246IuxpxOS4QoIw5e4641_hgEA42dU-iY53Zq1zO5-qO3go-irXIFjt3duYjzYIrkP5lJ9grsiml1lOJYitxl3P8Vmieb9xlR4eoJ3e3z-5u2Q46iohHe-tL6j0c5L1fURqxJGxdDlFew02hsFV4kyFXw0NuU-7a4Z10iyKbQ5e-dOGlfKG5cpz5y0XhJFuvnU13TgjoA5vz-XWuZNueLHikiGojpCUZbZCi7NqMbNO7AWwiVYe8ZHcpKurPYb9uAocI1U1OtPSWuubJLKJAk3A0tdlMAyLlki-EKTwO6TDBVEe-c3vhF7zliYCZe2iRrLqKSVWPbh1LT7cxpzV-M7F6MYwJN-drkqN20fVTKJcoH2v5V0XtVm2wXhb6ltCf_8qjv0sKXRrYor2EDpxRw6H7sVE61pcc0awtwPLSPEqxEePjYXOznkP2cV2RKi_IEe3V-zUFqVqXwv5j_WuvAv9NeIvyN9QlT9ktmMn3BZ_qW1gIwmrtAD_rHJswwsXQpQ6k_9MkFI8jNOJx33t_fp6vUKN9KnNqw6UV27Lxljub2Bege2zKv7JonWkHGFhM_bfiU_oMF_ciqaaxcli5vU1F8RjIb8zoVbgMCNfEMJy2m2rF_rafC-r-vhWVYLsIsZ_JoSWi5pBp7Eodn7AERUwkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=aur_Bwzpi28CNgiwo5246IuxpxOS4QoIw5e4641_hgEA42dU-iY53Zq1zO5-qO3go-irXIFjt3duYjzYIrkP5lJ9grsiml1lOJYitxl3P8Vmieb9xlR4eoJ3e3z-5u2Q46iohHe-tL6j0c5L1fURqxJGxdDlFew02hsFV4kyFXw0NuU-7a4Z10iyKbQ5e-dOGlfKG5cpz5y0XhJFuvnU13TgjoA5vz-XWuZNueLHikiGojpCUZbZCi7NqMbNO7AWwiVYe8ZHcpKurPYb9uAocI1U1OtPSWuubJLKJAk3A0tdlMAyLlki-EKTwO6TDBVEe-c3vhF7zliYCZe2iRrLqKSVWPbh1LT7cxpzV-M7F6MYwJN-drkqN20fVTKJcoH2v5V0XtVm2wXhb6ltCf_8qjv0sKXRrYor2EDpxRw6H7sVE61pcc0awtwPLSPEqxEePjYXOznkP2cV2RKi_IEe3V-zUFqVqXwv5j_WuvAv9NeIvyN9QlT9ktmMn3BZ_qW1gIwmrtAD_rHJswwsXQpQ6k_9MkFI8jNOJx33t_fp6vUKN9KnNqw6UV27Lxljub2Bege2zKv7JonWkHGFhM_bfiU_oMF_ciqaaxcli5vU1F8RjIb8zoVbgMCNfEMJy2m2rF_rafC-r-vhWVYLsIsZ_JoSWi5pBp7Eodn7AERUwkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=PoRRuVQJdwjjqRWLoHViCw4LafkXs0uQ5-7bDSG1_bHVUpZH-AyDtvkNFNzXA-jciAQ2o8O3K_CNw9RbDpP4eobQCYVnIrb0Dq8gW88YDlud8iE3MUX8KWknZrN-omL7hfqYvvNxpIKz7r4gLt4lm4a56uOkbdVjebayS2ZNpTE8J-X3CYUI9em7HhVjTCOGMgoYg14Y8vxmdhqv2-A5FKwo_ocKUDCoeIO4YnlyvQJT3ohkj_ZxpX02lpHqa6aYUxKUEFcpK2p51VZuCywlqfRdZSyW1GhL_bnN2L9GWxA5w72ohLks5Ouv4-mAmoIYiUSedPwOqpMiSD7HudsZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=PoRRuVQJdwjjqRWLoHViCw4LafkXs0uQ5-7bDSG1_bHVUpZH-AyDtvkNFNzXA-jciAQ2o8O3K_CNw9RbDpP4eobQCYVnIrb0Dq8gW88YDlud8iE3MUX8KWknZrN-omL7hfqYvvNxpIKz7r4gLt4lm4a56uOkbdVjebayS2ZNpTE8J-X3CYUI9em7HhVjTCOGMgoYg14Y8vxmdhqv2-A5FKwo_ocKUDCoeIO4YnlyvQJT3ohkj_ZxpX02lpHqa6aYUxKUEFcpK2p51VZuCywlqfRdZSyW1GhL_bnN2L9GWxA5w72ohLks5Ouv4-mAmoIYiUSedPwOqpMiSD7HudsZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=Ik6ruWZOmiolvQy5j2twXwIl3jkSy_bk-r4Nut69o5fdsTMjTJbWwL0OBRGxYyvyPKivtcoCuCgg_lWyWICJmgeYbpP1oT6aEAh7Mr_1XagkWUdOevZcdt0R52dKguBWeZ8v6AdluHZVWrSEI6ZwS3GWSICniIMNfHuCfN9GwZ4d7zWF0g2kQ2m0U6JNmxL6cLBq0M5uyqQiiQtV8E5Va0hwVQasxPZTVDDbFiqmVYQRQVz38LzMDV4-2qlV9c7Xjne5E87THwf2pHdfIHTCI2D7Il8Dc6qyzuDye4IhWzzaLs6QWKaRCMnQ6osHiX9BkbJqKbEMew7G-mSbER4BDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=Ik6ruWZOmiolvQy5j2twXwIl3jkSy_bk-r4Nut69o5fdsTMjTJbWwL0OBRGxYyvyPKivtcoCuCgg_lWyWICJmgeYbpP1oT6aEAh7Mr_1XagkWUdOevZcdt0R52dKguBWeZ8v6AdluHZVWrSEI6ZwS3GWSICniIMNfHuCfN9GwZ4d7zWF0g2kQ2m0U6JNmxL6cLBq0M5uyqQiiQtV8E5Va0hwVQasxPZTVDDbFiqmVYQRQVz38LzMDV4-2qlV9c7Xjne5E87THwf2pHdfIHTCI2D7Il8Dc6qyzuDye4IhWzzaLs6QWKaRCMnQ6osHiX9BkbJqKbEMew7G-mSbER4BDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atfm6uEd_5CHR4pqT0YjFNiBu0gxvsuGrLjUJB7p-3m-_aeIj0REUNhjheJKf3qMWYbJqyiCr5hg4H0WsqUqN_gbEMZmLeo3SqAz3zqn9zwd8XP9RpWpziYzSgQtHfIPtUOPjQMUeBhBULKFKC1bgbeyVB4z7q1venJLUB_jGUGuO-wWUq5tTwX8rWjHjwQ-r2D_mviORl6IAGU5j4xfyvQVCoLg8JWvzOa8ETceCnkdgZChSwFUKdmgOft8GboJ1a2YMTCZi7IVDDrGVv_o7inH2rkXiJy-P4j2sKXQxk1mHEIEvFxwPstjyu30ifwL7FCkjhHNK1UrFVPVhSmZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9NakuYUt-853aAWmsbjuctwqU89uJx1cpJOnHl-NNFmCiZPzzfg2OTKu1qbYjonqwoBnVHWctnAjOyxKJJbEnHbhMzeS5j3JJgVTR8fP2eKy2dHzVHya3mMW_JWcK2xj9tzjUk5iWcPOWEmfbu9PnxgINHQGOZlAh4lZuqysEqOAed7w-3kGZjW-uyn9zS2-rwSFY55ze1hINZw01S0i6mJm5I3ZrNup69NTMv5IciEhOo7D-s8tEWdKPFRQLNg7N9Z7xFqSKl77lQ6Y5SNEr86OJgZznwNtfOGlB54O0294Wc9FJ3KTkXUs7drdlkgxqtYdvvtRrQ2SN7PsZepRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=BVNSCTF5Rzo43H7iXy3Zk9xZB3AvYp8eamvhm0hnT9VJofLMfypNEfH594DZQldSVMyV7uSoR7lk-lPp9k_1DFXdcuqEI6i7vhVQOT1Zm3Ru_0rpYQyPE84PK7UBxip9n10JxH48zNXmWXxqhdEpJQwrrqYiHphEOY19fylsRx9AqrtgcRJPXkzQlbUqZQjRfxayihJ_cPamuVsmskGAl7tcyLm5bJa-yAsPmKFxEyidFSvXyvx3iWCQKv8EzS3SJ_EamgZKIlhNusFF-YTo4Sw0MX85EGEX8gXfNeQCAvVFuyTgykiEhEZZ-U-MViRyU86nR5FmYOSP7xEuWsl_RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=BVNSCTF5Rzo43H7iXy3Zk9xZB3AvYp8eamvhm0hnT9VJofLMfypNEfH594DZQldSVMyV7uSoR7lk-lPp9k_1DFXdcuqEI6i7vhVQOT1Zm3Ru_0rpYQyPE84PK7UBxip9n10JxH48zNXmWXxqhdEpJQwrrqYiHphEOY19fylsRx9AqrtgcRJPXkzQlbUqZQjRfxayihJ_cPamuVsmskGAl7tcyLm5bJa-yAsPmKFxEyidFSvXyvx3iWCQKv8EzS3SJ_EamgZKIlhNusFF-YTo4Sw0MX85EGEX8gXfNeQCAvVFuyTgykiEhEZZ-U-MViRyU86nR5FmYOSP7xEuWsl_RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRBSYJrRlwEO3G1dP-1EMMts-tgwflB3TXiFPZnienZY13Waj93oToFyLxJ_VF2YOPKKj-mexNyr-A_mAvId-gy73-vnlhnbYryeun20hygI0KqZTPbLUF81Cy0U5q-oSOm-LfYc-G6jAjFyMKLopmXCHAxLC1K4mSnA0Jm13TVqzevWRcr35XVzM96Y1x6MxxviUnWVFtnxdmUDFpg7ASL6yz75Q2NkMNHYwT0GVirrs8h_SzWubZpnmIlivksMInhBtv34TnEQjgLbYizCtrdM15He1j2hW2vmIXEfwJbkv7V92NIyZeG_gdc3cOnw6Z1Q6VsnIx2O3OU5wrvtjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLsMCN6MTCBapF9vGMq9pFAXynKtpApxZ-PzYCBwXMDDSMWxVlCS290aIuezcpnJ9f0m_TNWArpB9WQ_JZ3tkq4sMx5ZFlVQjeg0HlQc1-vDk7aHEcS9-SR3bHeCem44Ecz_3oB8m-EUxWhzkaliWU3CXYWF2cf3O1vVu_irRMzFqTTq2XIGVPubFSpCPG29YPHqAXrHkxl-2TNGruoF-oLS2U__vOnpB8aadl04N1fHO-QdfoRTYSmlgHz44VQFYelstLiXxnVQ7GFrWLsm_bBw4U3jTJVzvGu9NRZLTHhBqZiCBVKbuugWu2hpipTFxU64WB4KLgvvZl1ic5h5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCQFbXAgOXMzw3jeHJBlbusuBkWF6o03KseskDEH-dI7iRpD1tRDcThrcx2hz788ayduVqAUS0kYBCrdVmnj11s85S8KavrJd7Zt0CF9FIB_C8vxS4tRomaMRZOkjaZSMeajC3INJkNou4EnsefZZvqQ_34R7HA_KuwxFeO9ZlTzYZLiBRdR7AYzZFCkY89MvSj6AhRknrRfq20f-y_YlUzJRNNNNOFtBbHjx50aJ7M6mMNayQldAZtByfZSQhMolHKIfvQyPoU6xh33iO3cgjWWAjSTRgI-1XVXle-NsVU4rB2crDbYmmI_gN1eLq1rjvIm2VVzDqAjGKP0vfELyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0wWGuj2wD-VN4Oycn6bPWU0qi7CMMdaT9kZVVflA9fav6SNkiOIWtx7JoX_dED1fuvDxG_HYxLeiPP0vwxhON-D9KTlCEeWXPqKMX5Pwo15fSLFEui_yaEZLuNOLCKVMni33Eha0zUNuMaGEPMurNdEepn-eKKNbUXsunpozWv9LOpvzfIrGifXg1DOahbSSVGS-RLvaG5IElgNIkzD3Ckdn09DyIrqxoj5zJhW71KoQXJyD9k4XfxeQZ5Ocko-2B9QBgppK94L_fqOhHSzlLpi7_F-BYbXaFHhADx15mkP95SElZW6NWaBG4air2gFtkBAxwzd-Vq86sfDqVd-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=oVsPlN3D3e9fOHzF940sSZ26NfGNa5FcI9mAA2RgoUDsDrCkk0hCzR9yo7AK19H6GQVM3-Qv_N1J4qaitVRL7ZDDjbQSwikD3V9tZfyM8ct2yqj4UcR2YBaGfZ3ZoZTCu2L8p6n0zFHi4SgH3OdEi1K_wFnVxaELlVqBgaJ8VHd9Z1VsCqVLSnWO7x5XTRJ0iWUB4sOquvnkmtzzkprRTxNVd7mWS9YLESnvWYFv4bNIZaCF7a9OhIMUwkT0q3pAN1l_vVx1zcdIaVX5_FxTkz165bNMMkA_RYA392xMF0oBFxFCbd73vRx9xDfiK1RGFjz5vV-pyVxMsbtlkoLfDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=oVsPlN3D3e9fOHzF940sSZ26NfGNa5FcI9mAA2RgoUDsDrCkk0hCzR9yo7AK19H6GQVM3-Qv_N1J4qaitVRL7ZDDjbQSwikD3V9tZfyM8ct2yqj4UcR2YBaGfZ3ZoZTCu2L8p6n0zFHi4SgH3OdEi1K_wFnVxaELlVqBgaJ8VHd9Z1VsCqVLSnWO7x5XTRJ0iWUB4sOquvnkmtzzkprRTxNVd7mWS9YLESnvWYFv4bNIZaCF7a9OhIMUwkT0q3pAN1l_vVx1zcdIaVX5_FxTkz165bNMMkA_RYA392xMF0oBFxFCbd73vRx9xDfiK1RGFjz5vV-pyVxMsbtlkoLfDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=CKpDRfaCxSAbIO_4_4ltfPduU0wDXw3YFRDnDYGHGP4HswVAFQiQAAwwWNvgcKTmonXtck54ZPmqmEPaFVVTdKNVk6neszYvGouY-xB_QgE94aRBkx9_TrTqJ7Sy-nWJV7szwq_AnXTr4ocenjWseYF0rpcQvJXXFXQKTBmxONWZavLy0LAQwCzjLc0Mswkr0aG12hz4jFKaikaCrj-BZ1xVNv5oLq8hbbow3Ho9wg7ZxquaBnUjtbYo5jKdT_5ZfbdMgRP8GTVWkld3RDbkxvgVdUhB8X6tk4o2HmLhmLVjEFcjXUrrtVIhxNKGfofeJnhkclLZZ1xzVlmRrtNW-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=CKpDRfaCxSAbIO_4_4ltfPduU0wDXw3YFRDnDYGHGP4HswVAFQiQAAwwWNvgcKTmonXtck54ZPmqmEPaFVVTdKNVk6neszYvGouY-xB_QgE94aRBkx9_TrTqJ7Sy-nWJV7szwq_AnXTr4ocenjWseYF0rpcQvJXXFXQKTBmxONWZavLy0LAQwCzjLc0Mswkr0aG12hz4jFKaikaCrj-BZ1xVNv5oLq8hbbow3Ho9wg7ZxquaBnUjtbYo5jKdT_5ZfbdMgRP8GTVWkld3RDbkxvgVdUhB8X6tk4o2HmLhmLVjEFcjXUrrtVIhxNKGfofeJnhkclLZZ1xzVlmRrtNW-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuMQrFT9oupdgFLC_LN3laTpRKDTmEVHfVjE-TNQ_D3cc-13-fzANBSje_c9IBF96tMLPtVy4j3ozULISkZckoOc3fuPvm4DvbFpLjq2nXdqhrCl7zNPGckgGSEjjznABeoRw6IG8yn6ZZFoLg9mTqIRIUdak7-a2A_Vv7YvdXEXZ8ppTkLKIjQ_EVXbjswfUzb3m_XPfVkf8sH8Ot9bUM81QGjgCzzkmQp6EskEtE25F2pI0GSUsRzfZaOENdSLMB1aRz_p1oCpMNOOxiHmijOgNOHVAtpY5Q7hpjqWZ2dhlgrlfNRzFqHLnVJRgvTof56Zhyj1w2n0WOpMPdEBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=PM0-NntPeOyG0KciJdzuUckMvuWXZgxc1OwIREVHDkhtZHasJmD9bTsYZ8R6jvf6gSblmW6LxeeXvv7oKU72qR8gAxaaesOvaVz--VS8zqNuFkNZ5BnBXOcJ2RpkkpfIvyHmgaANaBCeS84ex_7AdPxi0T95mpgTwVBa-NBDTvv8qVTTMdy-EsiILapATUfRxCJqNTAb8VD5tjo5G108X4tHPOcrVM-DYDU4O1TX31zvvXezTcnM8f5Z2MvkdLFTKAEv7YwP6xUq_agfrd-nMVbiwtgV1gnsx1_Yq9tmlYeDIN0eGCxldi_cBwV6zmS5ghvITVvaVspZwEfbg957kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=PM0-NntPeOyG0KciJdzuUckMvuWXZgxc1OwIREVHDkhtZHasJmD9bTsYZ8R6jvf6gSblmW6LxeeXvv7oKU72qR8gAxaaesOvaVz--VS8zqNuFkNZ5BnBXOcJ2RpkkpfIvyHmgaANaBCeS84ex_7AdPxi0T95mpgTwVBa-NBDTvv8qVTTMdy-EsiILapATUfRxCJqNTAb8VD5tjo5G108X4tHPOcrVM-DYDU4O1TX31zvvXezTcnM8f5Z2MvkdLFTKAEv7YwP6xUq_agfrd-nMVbiwtgV1gnsx1_Yq9tmlYeDIN0eGCxldi_cBwV6zmS5ghvITVvaVspZwEfbg957kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=BjwKF0VF-OUFzriilnOlKzawsunxFkY9BbZX7KU2A9wazFdLylkwxoamsbqMurXXrjTVIL1StZ0ezbEJVSi9UbTIbcjs8Jg3s17JmI9CKNOhDaxDymp7xFbBuFtM0IypgIiUdqn0y-SM8Rw3ghDKSjUdPSJy16SpAwGG-q164j0Z3Pwq9ZX9yZ2Iwu5v7V9GHJHDaJKsTesHwukdnWyaUoHDbpDmOmxRgfHI_PWTHFlAPFUYTRbh9IpaT5JeeMSlxE8xr3O7838DFDg4MRRWppzFsnV0E-5-2AoTrTtVFZCUx64KNRbnjrOTd3nAiTlKjxFn-JiUgdzTotxO1l7T3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=BjwKF0VF-OUFzriilnOlKzawsunxFkY9BbZX7KU2A9wazFdLylkwxoamsbqMurXXrjTVIL1StZ0ezbEJVSi9UbTIbcjs8Jg3s17JmI9CKNOhDaxDymp7xFbBuFtM0IypgIiUdqn0y-SM8Rw3ghDKSjUdPSJy16SpAwGG-q164j0Z3Pwq9ZX9yZ2Iwu5v7V9GHJHDaJKsTesHwukdnWyaUoHDbpDmOmxRgfHI_PWTHFlAPFUYTRbh9IpaT5JeeMSlxE8xr3O7838DFDg4MRRWppzFsnV0E-5-2AoTrTtVFZCUx64KNRbnjrOTd3nAiTlKjxFn-JiUgdzTotxO1l7T3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=KeoY2BgybDN8cFH-mMZxu5U5i8nu44IJYqBh8Sf3lBK5hAJ0NsK6dXn2IQHlHjbR18LFGzjF25cdvN46lfAiQuT6R3YE4lyMGo2A1M7x8yNK1HY-tmls8BCQ3_ce6H4QrGlzBkOxGDYQVNyC34vu08xn3X9O6wL_w1w0xHr_j7t6Dtjm0ep_xXsTBOhGu5jLsR7kSeF0YogR-rHMGzfRAwZGEmVtjdfaUN0-s-2-DThonaVbK7fm748p9Kfjjk_aUMdD0okZEf7C64iVsM96GrMc--ocDFru9ATdkyixyPmLsL167WO9VTsivAiOdVlniUs80TzGeOiK4bGO7YlssQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=KeoY2BgybDN8cFH-mMZxu5U5i8nu44IJYqBh8Sf3lBK5hAJ0NsK6dXn2IQHlHjbR18LFGzjF25cdvN46lfAiQuT6R3YE4lyMGo2A1M7x8yNK1HY-tmls8BCQ3_ce6H4QrGlzBkOxGDYQVNyC34vu08xn3X9O6wL_w1w0xHr_j7t6Dtjm0ep_xXsTBOhGu5jLsR7kSeF0YogR-rHMGzfRAwZGEmVtjdfaUN0-s-2-DThonaVbK7fm748p9Kfjjk_aUMdD0okZEf7C64iVsM96GrMc--ocDFru9ATdkyixyPmLsL167WO9VTsivAiOdVlniUs80TzGeOiK4bGO7YlssQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnnT3B6a8gcRinHIuQsGIxrUqgpRcbLJsYuBnPJqDru8QQzaSxbClfxAP2hLcnxkw3c77AqXHI22orHHlBrBzA6BlpyVq-Hnns6_XSM6zgOh0iZtr9OnHwcvPXmmnbB5zw6tAb-sVWtCqMeePMkMHA9UUuUPcGGXKm_cvIhhXpcAO6mcRKUW_q18PHK9SthTYgHCaHvbSGCtJqo7bbqqjrPoFxke4zk9jmQdHbYwr6KrzEjhgx8VaO_yE6xCs-akVlDDidghD1KRWGdFHHQhxTYD-WdvnqOO1A9jhchzAJqcfHn8e-fLf5U5nvP2Z1yOYyv3scTTXl890Fp-RNtLGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=esiJIb0YxRjoj3niryK9oWctKGzY7o9GEsy87wJMTAuRBFUPcVmNCupkMttpZCRU0rLr_t_BfO7j-ioRrEgWm0-F3VBjGvZuxR-tJR71ZInflS4eHRKVeXDA802q0zRqQN2yyfDAayBpQOPnDjT35uJ0t05kWSattTeZIDHumwlyk-NweJoHq0tB41zwKN42A8ugofqzc35x_5LrEjlvRYg0tfEZEeKtUfhhBU3_cz7s4gQoI99ch8h3TLTdKwA2LsU-0oh5qX-uPJb8Cir_jTc7o0fGNTScT5sOPVJLcDFh-Fpj_nW6SpduPcRBr3-r7YCsm56e5fHY-yPKrzDgww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=esiJIb0YxRjoj3niryK9oWctKGzY7o9GEsy87wJMTAuRBFUPcVmNCupkMttpZCRU0rLr_t_BfO7j-ioRrEgWm0-F3VBjGvZuxR-tJR71ZInflS4eHRKVeXDA802q0zRqQN2yyfDAayBpQOPnDjT35uJ0t05kWSattTeZIDHumwlyk-NweJoHq0tB41zwKN42A8ugofqzc35x_5LrEjlvRYg0tfEZEeKtUfhhBU3_cz7s4gQoI99ch8h3TLTdKwA2LsU-0oh5qX-uPJb8Cir_jTc7o0fGNTScT5sOPVJLcDFh-Fpj_nW6SpduPcRBr3-r7YCsm56e5fHY-yPKrzDgww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2YE9KswEM22WT02rBR8NqzreYkGx8U0e8j1ulXQEHw6bdNTf0NFFTkkNgb7xIx6gcvMNKRYZDmelzXjLHqwc8JaQhEgBxu6fZWhoNsWEjRSCRw5iAovNca3Zn9fih8TLjk88kIf8jHUX28V0FeCINKcihJmgOfzkhI2lZAQtbSYHiUgH_pPEA5zYYz3Be4zqarzLD7yz-DoXEf2oYvd8BkFsBBEv1shNPWVyzWeNbzON4CQtVVuXREHIobp9RzbvM3tS-ywJMo8FINcq2CmG2A_LkFomi7e7Ixxvk6Y70nfbZd6VjEm3I9M0sm9-S3y6NczCZoj8THoI7m8Ah5tIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK8NMGHL4niAh_rw2NuEWYnMA06A4wjW7Ah7fJuNtKt1hpyh_EGvt8AOA8Q8EL97KIRZvawzXco2x-u1YioPfVixxiqlQ7PRTIIaeWTpNj_dI3uJDfPTwk7ShBo8bbBBmSsYk9Ose5pLPUtO1EVfeDkaRiL93NzCegoF6sADLH9lfADbwCE1dxCUOJaHAq0RANhz79nVG_BAYns7QRtEar_Cu5uPw-3F4n6SZ3z_rC84zEZg7sLGXEEi6kSmSrzBhKCHuLfb7QKYo7keMOLFy-agU1rNTxHbicZ0fbXT-ErvUflVGPPlGA4Y3S0Ds2S4n4XWjrBRuDCRHxMG6xkxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=bCnQQPN6dYaCnHWuoar0FljfRr2cSKW-Rl5Gm2UMhtR6krRwt3eN2ymVqr0eO9k54RNFe2sNlV4oNCa1DF3jiLh4NruTanlHZKNK-_col9dhDwYOU6ikOCFrBKeuIrjU0aC8OaBZ7efR9_lVVwnXf1KbJvuPfVKhrPxAzNCRRDKyu7QLj5TYper3VQW5z4WKwwOO_bwCHr2NdnMxxRemh1GmQ4_EwFR1NZbRtgoiM1LHGWtzltRqWnpKqJZzgwfISqvMIyqIbPq53GKZOqEKnUFo3r6iM9DbMY00MSWY4rL_w6Fbx0_yEjmuzlODKK-gd0fqeBbsnIL_9C9nGCxEww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=bCnQQPN6dYaCnHWuoar0FljfRr2cSKW-Rl5Gm2UMhtR6krRwt3eN2ymVqr0eO9k54RNFe2sNlV4oNCa1DF3jiLh4NruTanlHZKNK-_col9dhDwYOU6ikOCFrBKeuIrjU0aC8OaBZ7efR9_lVVwnXf1KbJvuPfVKhrPxAzNCRRDKyu7QLj5TYper3VQW5z4WKwwOO_bwCHr2NdnMxxRemh1GmQ4_EwFR1NZbRtgoiM1LHGWtzltRqWnpKqJZzgwfISqvMIyqIbPq53GKZOqEKnUFo3r6iM9DbMY00MSWY4rL_w6Fbx0_yEjmuzlODKK-gd0fqeBbsnIL_9C9nGCxEww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9YBMmqSGqdtRI1DjsHG0hz9sScZQkfjj9vDYkZWpTdjZ59LNd1ImJPa83umMyX2-OKBfFOzM9L8g3elIoaE_fxYCXpzNlKLofPrWCKmAK4_XJvuBlaeHOaaS2IrBH-7_tAJAjZtKDCHbIJAUJJPqtnZekLuTSHYOEEK-ELXdE1zr7XB4BORzT6TUV36_fde-AGluQ0spY7MhUkKd_REKZ3yNWW6iSp5Pq3s2uuxUhnbDw9inZdrLZMfnp6N9xSVYM0UbSXunTwSoirrDiVsGZIB6Irf7Ib7DVQp-miWnO-sGYInve9Hme2KEYT_ZdCd29o5NCK-fp6Axo26q1ualg1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9YBMmqSGqdtRI1DjsHG0hz9sScZQkfjj9vDYkZWpTdjZ59LNd1ImJPa83umMyX2-OKBfFOzM9L8g3elIoaE_fxYCXpzNlKLofPrWCKmAK4_XJvuBlaeHOaaS2IrBH-7_tAJAjZtKDCHbIJAUJJPqtnZekLuTSHYOEEK-ELXdE1zr7XB4BORzT6TUV36_fde-AGluQ0spY7MhUkKd_REKZ3yNWW6iSp5Pq3s2uuxUhnbDw9inZdrLZMfnp6N9xSVYM0UbSXunTwSoirrDiVsGZIB6Irf7Ib7DVQp-miWnO-sGYInve9Hme2KEYT_ZdCd29o5NCK-fp6Axo26q1ualg1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=u3AGOZrYUbyCt3NV_zvyV-QYKzjbQIWTbyd8L4hdPXuMR5xr_tFGRCmwKEuDC1hVYmR1kH52yF7PANvjIeBaTCecWkPuPJbSq1jVVPwJlqh_bAyUj7rI7wdlGcVjSEiYTPwHn04dLBoBmpJNGGViIB-TnWvzeDJB4_perWgT5ZEynXiwjfvDrg-SxY02MLmiMpF0w8fr2VMMt99o7GAdfyJtb1XuYvRRGWEfhnQXReMF7D_jOPNl9sZh7B6NyY8Rru4GnU_8v9Rt7juWrsJrjB68KI5kCsIdOCW4TzbM0f8oIBlaAU4pJefJ4ASXaDWmQdKU4xbXleZDbWbXy0RK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=u3AGOZrYUbyCt3NV_zvyV-QYKzjbQIWTbyd8L4hdPXuMR5xr_tFGRCmwKEuDC1hVYmR1kH52yF7PANvjIeBaTCecWkPuPJbSq1jVVPwJlqh_bAyUj7rI7wdlGcVjSEiYTPwHn04dLBoBmpJNGGViIB-TnWvzeDJB4_perWgT5ZEynXiwjfvDrg-SxY02MLmiMpF0w8fr2VMMt99o7GAdfyJtb1XuYvRRGWEfhnQXReMF7D_jOPNl9sZh7B6NyY8Rru4GnU_8v9Rt7juWrsJrjB68KI5kCsIdOCW4TzbM0f8oIBlaAU4pJefJ4ASXaDWmQdKU4xbXleZDbWbXy0RK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psTloHtGF9RibFvdVMlddAlcWaYUTrjhpJ9ASzBSsLSsB0LM4mUxInVfTdy0sQBHAg771BP7aBmvrirjcp3lkXWaRW-ius9JzuigqgamV6GNKh8QM7IYJIV5lOKEDYWSUzV68TIt2Ty-I2S2T7xjI7T3gDmmJcrfAXR_9pBTX-sk9x3BRzTonRwNhkbjY98KdBFeP2v-BwX_z58ZQ4wmd7av-2LyWtblxJPgCMMDui7lpm6dmglIcg64CckAr3X3Nd8e_gZcUC8sh-jHxREoCbcjxDophcvvwr564q4VfmFPp1adksgj7HX6pZg8EIZI-9Q4acn2GFe_5XQEt86KAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Ke5W2WpnT4fKHEO5u3jCl7elvdeWoek-3yw1ycrZWJHrGUKBeJKOM2KedJ_euEseYb6QNPTiWmYEKwFkicrACJwqoOHo-Dqo_WCZTyIobX01hLmI0VcQ9IfC36rVSLxbLV57r7CPyi9jvoDGncyh4oO5E3oTgeK3SJJ9AIDdkhXq9c5ZcixJS5F2iFsaHq_d16_dU4LvjWpddTJGDuTlK6TWMrIAqqYpE7glnKV2kXdtyYXi2Ii2WzDfI_osauM3tsCfU0Pkwl5aCONmzf117qj9StudbRNQgjFy8ALPUfKyvHrOLw5_Drtkj_Ir8GlV1YsJRWX-nb_LX1hFd4Gdlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Ke5W2WpnT4fKHEO5u3jCl7elvdeWoek-3yw1ycrZWJHrGUKBeJKOM2KedJ_euEseYb6QNPTiWmYEKwFkicrACJwqoOHo-Dqo_WCZTyIobX01hLmI0VcQ9IfC36rVSLxbLV57r7CPyi9jvoDGncyh4oO5E3oTgeK3SJJ9AIDdkhXq9c5ZcixJS5F2iFsaHq_d16_dU4LvjWpddTJGDuTlK6TWMrIAqqYpE7glnKV2kXdtyYXi2Ii2WzDfI_osauM3tsCfU0Pkwl5aCONmzf117qj9StudbRNQgjFy8ALPUfKyvHrOLw5_Drtkj_Ir8GlV1YsJRWX-nb_LX1hFd4Gdlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=cP2OKt8eW72YltTIi8EVoN7S4PZYPwTGwvjqFcci_FmzCGE9nBLGuP39knXBQSe8xGUKoZL3k7u0PbHUWKqeSB2t2kYhAg_Nig7OkPJN8r1Zx_VSQXeB9M69ndVo6dKb00zWGlkn0YQOar4kKS8a8qaCPYCzEwAojIvYor-RPtUEWCIR-ZhiLz7k9BcsEmscI4ug3BDSK0fgk1DHiMiXRoTu2Fu7eaVNiBYsdJgBPA3Lzrnoma44qO5WzJtjEIg6BXcDn4ALBnbTOeIiUnmWqiznwZ6BzJL4BbMmb0HqNJ58_nIbAE879hKpCHhyt7eNYkAG6bCB6pgVjFxM9LzA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=cP2OKt8eW72YltTIi8EVoN7S4PZYPwTGwvjqFcci_FmzCGE9nBLGuP39knXBQSe8xGUKoZL3k7u0PbHUWKqeSB2t2kYhAg_Nig7OkPJN8r1Zx_VSQXeB9M69ndVo6dKb00zWGlkn0YQOar4kKS8a8qaCPYCzEwAojIvYor-RPtUEWCIR-ZhiLz7k9BcsEmscI4ug3BDSK0fgk1DHiMiXRoTu2Fu7eaVNiBYsdJgBPA3Lzrnoma44qO5WzJtjEIg6BXcDn4ALBnbTOeIiUnmWqiznwZ6BzJL4BbMmb0HqNJ58_nIbAE879hKpCHhyt7eNYkAG6bCB6pgVjFxM9LzA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=IZV5W7fHU3aqYtCe6I8RJ_kZpchX4WXxlSMfV7vmCceDzkPpcww8QGyHR3td7RXSLcTGdOCvkrwDMAvEQI_FhF7SsL-3RMxKmgAK56VKQhJ0X48aOgxOdwscCvz7ccriJMyy4Tvz84JtPzC75tghXviOq6LDR862KZp0tyPPgMHB9-6LMusrOY2f3BsuI6PYJopvmy35ZPnOCPPk_mM0RlRStl8dPeUiqHaD9l_IbUTILygFRlBGkyN4i9PDUaMA9OxpaQz9vcktSvSF_U-72L_viPyQoKcS7illX9ia-vQMOpAjVR8YTACVM5SJIzVUfgh4sKTjhPjtucgNQE6ISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=IZV5W7fHU3aqYtCe6I8RJ_kZpchX4WXxlSMfV7vmCceDzkPpcww8QGyHR3td7RXSLcTGdOCvkrwDMAvEQI_FhF7SsL-3RMxKmgAK56VKQhJ0X48aOgxOdwscCvz7ccriJMyy4Tvz84JtPzC75tghXviOq6LDR862KZp0tyPPgMHB9-6LMusrOY2f3BsuI6PYJopvmy35ZPnOCPPk_mM0RlRStl8dPeUiqHaD9l_IbUTILygFRlBGkyN4i9PDUaMA9OxpaQz9vcktSvSF_U-72L_viPyQoKcS7illX9ia-vQMOpAjVR8YTACVM5SJIzVUfgh4sKTjhPjtucgNQE6ISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=E-R8ab_p3UmajSY1s-p0kIVm_c3-b-2AEGvC4O7T3mNcr1RyO35DV1h-shuS7EMajWbfcVyGUQNf94Y4SrCcZbsEPvuc90iivRRmm1KtJAmHosC0_1vh5EBiaELHgVZZRMK1yiZvcgOFxhUE4S8Ptq5XmvYCI9WVi-9aZUxMKCulf8r24upmqYApVr_HyOLbcYMD0PVPVVUrf989CZDm5qbynbhrWLyiplOZLc9P-b8Lr04Gqe4rC-a1EwC7NGzTOZCEgML64Jumv73R8iXnLf-rsDyEkX6H30G7lWWsfiFOGjZe8l_WHBLgUlUprKPkrFrpBuXsxwNgZ3i_4d0JHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=E-R8ab_p3UmajSY1s-p0kIVm_c3-b-2AEGvC4O7T3mNcr1RyO35DV1h-shuS7EMajWbfcVyGUQNf94Y4SrCcZbsEPvuc90iivRRmm1KtJAmHosC0_1vh5EBiaELHgVZZRMK1yiZvcgOFxhUE4S8Ptq5XmvYCI9WVi-9aZUxMKCulf8r24upmqYApVr_HyOLbcYMD0PVPVVUrf989CZDm5qbynbhrWLyiplOZLc9P-b8Lr04Gqe4rC-a1EwC7NGzTOZCEgML64Jumv73R8iXnLf-rsDyEkX6H30G7lWWsfiFOGjZe8l_WHBLgUlUprKPkrFrpBuXsxwNgZ3i_4d0JHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjJ1xdkwS7ABHjMVoKhC6PUsAx2otVgbBHAhv8Nhz09xID0cxiSqNTgXgJRag_ucLSG3pIP2EyGuleDhyFnm6RzaRkVqIN3cYkV2H6v3S4b_JOYqqepqJMmnQpVU8h3UTxyl6rqSnkJYO_cf-spVd7djo3r-60jXfVoZrd4NqQHlgaofUJm9ru9EErbmQfTV1rbCLSPy_-VGv5YntjMhOeM0YHGzZt94bZ45T2YmCdPJs3DR-5rbf7gaO3WN084BeOzVTB9l7kddzg2ZOP26ywQxewbbcQfgF5IW7Dhqc4t0IRi825JUcRzX1GsfS10gdEREdoWxUBoQjJImqDvceQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=VPNm285DATfvqibaESHIKS0_74k41Q5yXHh0D79shjaQpb_1ht00Jhf10DBxNm1NRZ3cVpSmq3RHDsh7XY-SLxyB91Jt6uCFZSuTtgKbtvqEJmGJqhKL0MS6RvNlqnOGjs_SHP_PNIMWyYQHlqC5czyLwdDOVCnRpkphwmxHuWML8H0exwQ2rdaEDSclPVxqnF0elfbldCds8Of2kORN0joafK0mfDJqnP9hdRFRTIZQNHeLylL1RZ6IgVI0-j2L2b09gISkbAXN3jjgKt68Vo3FGeQHyGAgwoTNH9WML3nRINlN0kiKSdb0YpspxPMPEgH1gISfEvlloteYTZTQWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=VPNm285DATfvqibaESHIKS0_74k41Q5yXHh0D79shjaQpb_1ht00Jhf10DBxNm1NRZ3cVpSmq3RHDsh7XY-SLxyB91Jt6uCFZSuTtgKbtvqEJmGJqhKL0MS6RvNlqnOGjs_SHP_PNIMWyYQHlqC5czyLwdDOVCnRpkphwmxHuWML8H0exwQ2rdaEDSclPVxqnF0elfbldCds8Of2kORN0joafK0mfDJqnP9hdRFRTIZQNHeLylL1RZ6IgVI0-j2L2b09gISkbAXN3jjgKt68Vo3FGeQHyGAgwoTNH9WML3nRINlN0kiKSdb0YpspxPMPEgH1gISfEvlloteYTZTQWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ngn6QHGhG7gSy3L8-mCCtEvFljzaT064CUwmx4lDMqVgNk6q3t2xWjtf56hg0WVXMj89B9c9LRHpVZs9hWhxMUlgmlwGR5MeJsThLW9rk7GxTp8-u7Jv5tEUzSlrelQca5U02UkONqGVJhBBL8BZ7i5yFoU_ruqXqDfn-55-88rjL8ZaiwhpAi1_t7iDtooF5HDbZYYzA2RdwpiTyXbPHQkPza5t-3O_IWmOS8bfBN1naeaYXAdRE8YoUG3VsMntaB8ZWRdm3ZZHMjGlkou3YXkAhl4-oUrZC9odZT-x2rAC37D5ghOJ_5b_NzLAlnQ9xOjmZMD8Hvt_-kdQI7-9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ngn6QHGhG7gSy3L8-mCCtEvFljzaT064CUwmx4lDMqVgNk6q3t2xWjtf56hg0WVXMj89B9c9LRHpVZs9hWhxMUlgmlwGR5MeJsThLW9rk7GxTp8-u7Jv5tEUzSlrelQca5U02UkONqGVJhBBL8BZ7i5yFoU_ruqXqDfn-55-88rjL8ZaiwhpAi1_t7iDtooF5HDbZYYzA2RdwpiTyXbPHQkPza5t-3O_IWmOS8bfBN1naeaYXAdRE8YoUG3VsMntaB8ZWRdm3ZZHMjGlkou3YXkAhl4-oUrZC9odZT-x2rAC37D5ghOJ_5b_NzLAlnQ9xOjmZMD8Hvt_-kdQI7-9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl_-J3t43OApA6b5FRbLk70Knv3dHb_8R2lS_X-B0lQDge2gLyR8JdUwoKK580yH3Aa278FwLHpS1qYgRDwviaNCenUdfg2r_oNKM3htD_h4DLiZdDbjH8TxFB3vA-FR1s1E4jKzbG0bZ5D-epp-GJ9mZx_onnJSID5U2TUplwceZW0O91IQgpApN00YQzRF_9ITLQ-IMMKF-gg-KpHBYddeKZHRKvL1cX6M2am0A-HBI0hTF2Qg0PwKTUE9T-Clmk6gSfamP2jtory-3LXUWKslBY_KKmpqBOs-FY5Qtja_6-FPdmf1iAv-SLiXBcUMIbRsl29p_u9QqJB5udxysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=FFMgrMX5Z_eH6vidMob8h2L26b1D86RuzRvTpevBkb1Et2eR3J5bxbwF0xcMyuXI13QHMGt29jvE8X7oeMFx0EU_81OGew2s5tbUg2jm8RHVj--_DiyFMy-suCwp2mw9kR8iDZ1beh1hxMZarIo0t09S7aaDhckrYhKePX64nh4Y-UpBHi6f7GVTo2FmVg8UlU0Q6PJuiulYQYkQB-utw7L9HteMremjrTbYunZWAC2T_MTZU3gi2kVGb5Oqixy7P-x4g-n8SD1NGk7LHgFl3Dj-sTGmpfeUhTqEaytC_U1bJ-cRx6tLu_w-ryWCn3vFLDPtIuTju8yRol6FV2ynrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=FFMgrMX5Z_eH6vidMob8h2L26b1D86RuzRvTpevBkb1Et2eR3J5bxbwF0xcMyuXI13QHMGt29jvE8X7oeMFx0EU_81OGew2s5tbUg2jm8RHVj--_DiyFMy-suCwp2mw9kR8iDZ1beh1hxMZarIo0t09S7aaDhckrYhKePX64nh4Y-UpBHi6f7GVTo2FmVg8UlU0Q6PJuiulYQYkQB-utw7L9HteMremjrTbYunZWAC2T_MTZU3gi2kVGb5Oqixy7P-x4g-n8SD1NGk7LHgFl3Dj-sTGmpfeUhTqEaytC_U1bJ-cRx6tLu_w-ryWCn3vFLDPtIuTju8yRol6FV2ynrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=sLUzwnXH66R-1NfgW3Agkf_o7IYLHtbr2wzyC-yNVPzpYCZEGNt3laEneC4tzQyMMdCw3Kw15K5A27iWfuNDVqI8C76wDQjACrQ0RoeRPI8S1lYMyK6jkd1U6KpqRhSnyR9XlnKKDTy1e4d97MhY_31jSxQ_yyI6xpvCjIK0Dr56gIHp_v4yWObvSJvkeEjoHY1ZHOXhfimVi2yexA_3erg7YdqLbh5hdixfYQgoQ8JEmS5s402xitkZ6r6unrU23VU1bzFPyQbZZ4gJ93ASQWrKUnLnDApiNRrMbO5s3dyxOQyPgoxoQQXxv63mm2Xg7OdhR36FNWiOjg2qpI_-Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=sLUzwnXH66R-1NfgW3Agkf_o7IYLHtbr2wzyC-yNVPzpYCZEGNt3laEneC4tzQyMMdCw3Kw15K5A27iWfuNDVqI8C76wDQjACrQ0RoeRPI8S1lYMyK6jkd1U6KpqRhSnyR9XlnKKDTy1e4d97MhY_31jSxQ_yyI6xpvCjIK0Dr56gIHp_v4yWObvSJvkeEjoHY1ZHOXhfimVi2yexA_3erg7YdqLbh5hdixfYQgoQ8JEmS5s402xitkZ6r6unrU23VU1bzFPyQbZZ4gJ93ASQWrKUnLnDApiNRrMbO5s3dyxOQyPgoxoQQXxv63mm2Xg7OdhR36FNWiOjg2qpI_-Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=svzVtX3bjL6eJ9JfsnRQuySZmdko7DX-YsoG0MxjNKijmeu08UP_2yXy-Ha7xdg067NeVYV6n3AQt79Ujp5kjRoKBaSXh--pyl4lIsi0WLmO9ZQwNzieAkSueyROpgqxGfaeKuUL2skSy42C9yOwsfNtVV75vBVTGxDexEequGZUJm55lZYAUTzdeuW8-BaLeyaosUi4b58RLYCFnQ0xpxH3VRvdS1k8zBXQeYXBFhbfqzhY7_tqZKn3N3R49cJkS7xwmv4_9N0Yfz9dssb4pZASq3Ph_Oas94jDkAH2wpNSqcUyJRDvH_YI18Q8vOrb8PGXNd8he9YSMCpLvACSpDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=svzVtX3bjL6eJ9JfsnRQuySZmdko7DX-YsoG0MxjNKijmeu08UP_2yXy-Ha7xdg067NeVYV6n3AQt79Ujp5kjRoKBaSXh--pyl4lIsi0WLmO9ZQwNzieAkSueyROpgqxGfaeKuUL2skSy42C9yOwsfNtVV75vBVTGxDexEequGZUJm55lZYAUTzdeuW8-BaLeyaosUi4b58RLYCFnQ0xpxH3VRvdS1k8zBXQeYXBFhbfqzhY7_tqZKn3N3R49cJkS7xwmv4_9N0Yfz9dssb4pZASq3Ph_Oas94jDkAH2wpNSqcUyJRDvH_YI18Q8vOrb8PGXNd8he9YSMCpLvACSpDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6tRsuhpbCi74yWi2yNR9ZM_GOinbQmZPZjcVYQDeV2KIYG-CSSYGzHHCT_k8Fa1yF5NCk9W2KxovEeIP-p5rjXhQt_HmlgM4noeu-PZexoJtPYbEmmdXbLIxYXbIe-h0yLk3slt2jgxkDP9bLPytRr33B4onYUkILfUA1PmL0saPTmfWjvEJ9p2EaavKOjrO1pwc0aTS2V09Frks-ajmqF9_nc3fRScE8uYMYKRs2XN_jbZjT9YwWGuMpEpeWE4Zo0jPBuVYDly1dNQ4IvX-6-Eonoi2u5AhGEeIO-dgNnkzcpY5vstlw0cNSqtasbBuTL1gzPzhm0Vhu0MS0LZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLhcUURV6RfzrpXk39te0XavrkhEK-F3a-O6SpJrlpfQuV13qGmCoHmxT3Aptncu0wV9OS_zqmTHsfvw46Ffji7MTTCtn-oas4In4nT5ak8bpKGEb1mc4z3RQCATYuZDhiMzy7UfEEYbb-b0NwewTDv5zKBQpi3e2-o6MnY30xY2ZSRN99xxVfjfAjtJwGuBQG67CI9m3mzY7MPOm9I7GIJw4s4djBT3XOu8xXPWLKyWAJXjL4wWzObdVMumsBEBUyIfqfastZQ6QfpYe5FZd0eorONh1puPwelGM2nyCxtB-AGbg4jiJSqaYR8CBN5ncbBeXzFUeGzO11bnd4S-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrCaX507X2XchiGYx0lydxKjTDwPy7_hENz2PPbkUC0TYQfJXZ2RY25A6mWp4BRd5-OHEBnQsITy_4aq6saQ9WU8dDRTkAKLMYOZMju6JhPkFBosF8FY5KJJWAmLL2li_4nHnI-hAvhzPg_xuzdZ39AfAKUxdzh61geHlqApxcH6fMMTvgeXjikTuuhRKuwx3-VTb-mv_ywsfPC1WlKCMehC8awKHw0aGC0TY1imJ48dR8_bXYPz7h8KDoh6tTSdQqsmT2X2RnmMUBAu5zFNsIRw124X-EjUOhZhgFaLEZebGlDYS_E5yPt-nurCRVIvgqFw5V3NBefBxpeVTCEsIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=ujiJbc5iHKrfLLbfOJZo8NAA7fGjsLKJSjFpCLvDQ6iv3_LngQnsy4X0ydzU-PBaRjQ5mrpNOc60bQvAO_5NHoL3hwjVUe9bgOa9QdTItkCNP_EgfYhk_73SAJXnGuSaNv6K1JMWDrgQMfAry8ft3YGeVkapy4ZCNjIu8EZK65Qi-dsevh3buqbUfjhtxPVAq0kwrBeBTG37upRTuw1PkuR2ZgkN5qXBWmQhpBdhJhe5UQUTFPcaEUMQuvL6FCxkND8yYAEBJ33NDDG0a-kc5Ek1MuVKT0y_7AX9jNNj577pKJZ_VHqvRkWua5xCoI6w_KN5AVayr16DvK0s53NSnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=ujiJbc5iHKrfLLbfOJZo8NAA7fGjsLKJSjFpCLvDQ6iv3_LngQnsy4X0ydzU-PBaRjQ5mrpNOc60bQvAO_5NHoL3hwjVUe9bgOa9QdTItkCNP_EgfYhk_73SAJXnGuSaNv6K1JMWDrgQMfAry8ft3YGeVkapy4ZCNjIu8EZK65Qi-dsevh3buqbUfjhtxPVAq0kwrBeBTG37upRTuw1PkuR2ZgkN5qXBWmQhpBdhJhe5UQUTFPcaEUMQuvL6FCxkND8yYAEBJ33NDDG0a-kc5Ek1MuVKT0y_7AX9jNNj577pKJZ_VHqvRkWua5xCoI6w_KN5AVayr16DvK0s53NSnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_099qbRePSkq0Z7i6iffU3Khcika4W0ZWwsdPVNk06zgIUhgBPZodu959U-YrSy3LrbM9FmbM3-MIURkyuL1Bh7Yf8MOG_qPr0ZNGJGPN9MHl52lNHI_0hN4D2-59pZtfm11oOMHpeER6WkxNG_UkaUzpo0C93hYUVpmAIvMK0Sq_Qvtbj27bbwqpBHiGU2UrzBj1vR_NezJTvrT9i9PVvtYD8FxXuHLsqOBb1E0p8vKezmSoL9JZO2Jn1wcTv5Zv__qyYQLS1NRiFamEhamg7SfnFy8peUy4DiD682_fJcQUegyyv3PQGYF6ym5AlMz-A9i7ZIWD5khVvV6BnDkflA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_099qbRePSkq0Z7i6iffU3Khcika4W0ZWwsdPVNk06zgIUhgBPZodu959U-YrSy3LrbM9FmbM3-MIURkyuL1Bh7Yf8MOG_qPr0ZNGJGPN9MHl52lNHI_0hN4D2-59pZtfm11oOMHpeER6WkxNG_UkaUzpo0C93hYUVpmAIvMK0Sq_Qvtbj27bbwqpBHiGU2UrzBj1vR_NezJTvrT9i9PVvtYD8FxXuHLsqOBb1E0p8vKezmSoL9JZO2Jn1wcTv5Zv__qyYQLS1NRiFamEhamg7SfnFy8peUy4DiD682_fJcQUegyyv3PQGYF6ym5AlMz-A9i7ZIWD5khVvV6BnDkflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=DkBpK6cnMaKMDBV7wg5G6U99CfJ30eWvLLm4hyJ3ID53dasbnKzF5SVnE72ZQ-4KSa2TKwTnGoWnBg-DleY3VUjczsuEZZxbpGe8dxanbXt3JTTbT32Y_yaC7fNf9rgoMnGHP0AUpSSqNlM4VKGDBjTStZ4UPh4-VQESirVOxNW7K1CQUVz1QmYqnmY41E4skDrMVb252hHyWBa2w9zhFYYnLoAlMSZn8P_bmTxo7t0rJ3mG0oToOAhpVwYrM9ntJp3dk52x1TFoYit0ZXqhp_gXQMAYMm29n3cG8DOJyUnMHnHqOxSw-RGv5nAeJR0mOLCZQE8a8pGWVFS1iNS7Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=DkBpK6cnMaKMDBV7wg5G6U99CfJ30eWvLLm4hyJ3ID53dasbnKzF5SVnE72ZQ-4KSa2TKwTnGoWnBg-DleY3VUjczsuEZZxbpGe8dxanbXt3JTTbT32Y_yaC7fNf9rgoMnGHP0AUpSSqNlM4VKGDBjTStZ4UPh4-VQESirVOxNW7K1CQUVz1QmYqnmY41E4skDrMVb252hHyWBa2w9zhFYYnLoAlMSZn8P_bmTxo7t0rJ3mG0oToOAhpVwYrM9ntJp3dk52x1TFoYit0ZXqhp_gXQMAYMm29n3cG8DOJyUnMHnHqOxSw-RGv5nAeJR0mOLCZQE8a8pGWVFS1iNS7Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF9m8K1pJ3dKBYa5eYO0XOT_wXfl51rHWzjNiNc6o5jtR-StutIdRGDu7CVfmVV-WbuoK7AA6w4UasXXbbOxMfGgTnA312F7qNOKhUU56GmgJLmJ-d5mJNi8CC2IPpkhH_GuI3yn487kF6x-ygNwQoNBTbrZAVdWq1SpxLTk6B6ZlZv9N5xARsKvxoC0-PzL988iNC9syorsbc__VFZKJrq1qpv32F3UMkuBEd8bohMge8EIlJpGNlYBgPisP3BKWz2ds5TA0OKoUHeKDFZegRBMwzMfZGlmlKv-kZ6G0gM8nVQTN9Fzsa8i74Mc-GogC-dLPmFg4MuWp-FKYg3eIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTqTeFsqqFMbw1tT2nQlZm8PPfEnDuJYmG-ZGgUfhcmkPDon7ryxqlz7PSBmXVhW0uooVE-B4TL2CNMKEzGIZA9OswkWvWvlYDkGJpK4OdktwJbI0jy-1hUp6lWHKU0F1ZWtcZ3xK75_9w7f3s7Dm86P7kGoxsa5kCFNCvjRlbEkc-nnUelLL38qMyAouEyQkunVamErOxYgN3AlHYgPvaF_8MJgmfqAPHiBBh0DuDfJXc4NzlkGsgpLeMYP5Vy_b8fy4VAGZYclM6yy2vIDSCW21-d5EAvt5QLRG7yrJ3qvojcaWDCJ55ufLe0h9MKRoyxulffyxvhNgS_OLGeaRFxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTqTeFsqqFMbw1tT2nQlZm8PPfEnDuJYmG-ZGgUfhcmkPDon7ryxqlz7PSBmXVhW0uooVE-B4TL2CNMKEzGIZA9OswkWvWvlYDkGJpK4OdktwJbI0jy-1hUp6lWHKU0F1ZWtcZ3xK75_9w7f3s7Dm86P7kGoxsa5kCFNCvjRlbEkc-nnUelLL38qMyAouEyQkunVamErOxYgN3AlHYgPvaF_8MJgmfqAPHiBBh0DuDfJXc4NzlkGsgpLeMYP5Vy_b8fy4VAGZYclM6yy2vIDSCW21-d5EAvt5QLRG7yrJ3qvojcaWDCJ55ufLe0h9MKRoyxulffyxvhNgS_OLGeaRFxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC-oKSbh1gmDP3WxYOvOb86Zy_HecS-8uD2j0RqHZvRYiSds3Gn8zH72fo7TxmlbvG9p7mItw4z-SSl2lxur-E1uFETMsA5xj_vocMyGEKRN15pe0V1Cgsyrc2D17KyKpyqgwVwo-HPBUmRA5lpquUeQaKCQJ8SvtiFMI83cPQHoxpmJIPtuHeb2pOGzym8bvY36p0v-BUwV0Yjuqx1QhK-hv7pingU9k3CK_2u7VmveaVoXfarZkrNw_gA3xJ_HZuBdcjDong8TYokpsFNuZjJGa5UMpXOguK2iVB7ZS7DAbiYVR5jpyhhF48KdvfaudPbSgKPaiv1NIopZPi7zNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=RpC9nk4xggtE9nHhZytMfVa-QbqlVfb95DCmDzzXRpzNM8uHMABpyS6JPEsLx5w5Hi9J7PL7uXWg60m5oPK1O132DIdWJsY8g_d94P6u393SU7BZtHKVPrUoP5XjytbkUtB36XFQf3UbSVnppyKjwNCJMgy5rtP6-h8MBRE1LzOoM04EeKkOhLJuCb3EUxvKT8qe26R9Jq22UB1NV_dQSUkMhG0-wZsATEeP2wC3d7OF55Q71f8XkcVLjtSCF5t5Z7ywMrOJk15HUaHJ0bCK8B-wlT0ibI4YRZHleB5ikOt5E8MhDEJQ90JXexZz5WjFABAm81kZOUHhOZo4UgmSow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=RpC9nk4xggtE9nHhZytMfVa-QbqlVfb95DCmDzzXRpzNM8uHMABpyS6JPEsLx5w5Hi9J7PL7uXWg60m5oPK1O132DIdWJsY8g_d94P6u393SU7BZtHKVPrUoP5XjytbkUtB36XFQf3UbSVnppyKjwNCJMgy5rtP6-h8MBRE1LzOoM04EeKkOhLJuCb3EUxvKT8qe26R9Jq22UB1NV_dQSUkMhG0-wZsATEeP2wC3d7OF55Q71f8XkcVLjtSCF5t5Z7ywMrOJk15HUaHJ0bCK8B-wlT0ibI4YRZHleB5ikOt5E8MhDEJQ90JXexZz5WjFABAm81kZOUHhOZo4UgmSow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=nUvQA8Wmfk5czLPebxKOjBekkmTff2vgtsS4Gd3MLduH0cKoKaZWA3aznbRZhVaWCtIhL_y9zfUOcAUv20Em-ON7zDu4SljukkG3VmzqFpPR8Lh25vM6NyG2bqih8_ilYARjALKI29QC_mBrvjpWF4ax91ZeYVKZ4rB6efdqyZdZ60Sg6fJb24qNVwSw2xSUDhaegjiYFXlmu21yN79MeDcn9O7OA2rslFLmzaeaU5tBLJ_YMePZoBVwGN8rz0f8vNoYgwrmwAp3q5Ux-IMvN6RnTLt5Be6wHAk2mhemsAb8H1sRhyoNd22V5JLR14jvfsf2ymhdM5UaAAFIa-PWpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=nUvQA8Wmfk5czLPebxKOjBekkmTff2vgtsS4Gd3MLduH0cKoKaZWA3aznbRZhVaWCtIhL_y9zfUOcAUv20Em-ON7zDu4SljukkG3VmzqFpPR8Lh25vM6NyG2bqih8_ilYARjALKI29QC_mBrvjpWF4ax91ZeYVKZ4rB6efdqyZdZ60Sg6fJb24qNVwSw2xSUDhaegjiYFXlmu21yN79MeDcn9O7OA2rslFLmzaeaU5tBLJ_YMePZoBVwGN8rz0f8vNoYgwrmwAp3q5Ux-IMvN6RnTLt5Be6wHAk2mhemsAb8H1sRhyoNd22V5JLR14jvfsf2ymhdM5UaAAFIa-PWpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=sKMLuQ31glByWcgJCwytnwWH7CNI8CFIlGhiG180f9iyN68qbBTxq6lu8-qLn_2-FaPfVc0L7KdLWzUe1r65IN1giz4kibt2GcqwZte3dA1DWczjNnyfbU27XFc99v7Z3VaPgMNEQuXkQ3NO0Pv54ulx8OV7ZnXijK2RUo6UgkYYa-L3qmsC8RcSpivQUzFDnvyrduUUV_yd_5O4SOoBg0UgCBqeSWom6wGHP8so6qqKTqJVT3rtMLWpZGctuI6PDNDhYkL-Ym__8agQ0us_L7GrOfIGCh6bNYd-nhOrF7WEGoDkuq81Me4yIz4CVo5uJe4YuEWVYrN2dZEPJvkcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=sKMLuQ31glByWcgJCwytnwWH7CNI8CFIlGhiG180f9iyN68qbBTxq6lu8-qLn_2-FaPfVc0L7KdLWzUe1r65IN1giz4kibt2GcqwZte3dA1DWczjNnyfbU27XFc99v7Z3VaPgMNEQuXkQ3NO0Pv54ulx8OV7ZnXijK2RUo6UgkYYa-L3qmsC8RcSpivQUzFDnvyrduUUV_yd_5O4SOoBg0UgCBqeSWom6wGHP8so6qqKTqJVT3rtMLWpZGctuI6PDNDhYkL-Ym__8agQ0us_L7GrOfIGCh6bNYd-nhOrF7WEGoDkuq81Me4yIz4CVo5uJe4YuEWVYrN2dZEPJvkcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTO_eKsVaXSO1E57pTHiBplzNNLR1UuXZNxEwoy8sDVBgChan_-zxJwhJll4FR1ZyQXT_-DVyl-O9brfsX0Z4f4kU-rcMF679zUsWiERTIOnVIy3VFV68L5gwKYo5SVCkwCGT2vtWNX1rx5iSI6zm379wBa1XURX2KmbpsYnryAxw_YgarAisn1p60O5RUNtaAydpiNOUlueVZj68AHhyk0DLpk93jrpCevRQC069JJ6m7G1R6OF6wHYzIMMfNJXV9Ygh7Bt5vn3zPfy8f9bXsqZJOLU7g067X2hsimAlAmcfr6u7jEOa4YpsOyuKw4OYn_p1vAUc8v-9_usTTLF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0Hq57MQ8zAx9o8uSIziMIOo7AKXP8dUht51isSko3K4FFp_8dGycTYpIZhjvTS2PwG2QEmYEOxoJJadFp-Q9RMKbvht-ItwgByHdIqwR6MRLflsY1lMVcrVLU1MK4cj-fAVQ04jxYn_xAkHJtJVnprypHb1Wz3hqDb5ygQCfGbsLnXmVuBWdmsqVHSlJ94c_NRDrj5gay4boVEJxG_zraDt8EPagd6WBlgmAmW-D6RikvAsZcC2DQqJxNZ6TRk4-y9PCBHbFhChMCV4mjX6ZBwMGoLIOwpgAepX0WUStCgusSsYhElQfD3v0TA2wtl6dbFcy_ed8yx4RsPI3PsU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=K5kG76iZ1yH27Tu-UzbzvfOXYRjPyYgHb9Pe06_c3bF8C3quFxr1sbdzA0ml2z8z2MGFGMtJdqAed0Ne5acI4Exa0K3lMmHZPeXsgTi_7d57KSRzEAE1xMnoowgEYxYhhxJfV3F-v7IEWyTQv3uzPNcyscHHeAPUQUtoH-1M_cRR3XHRG19gGQU_6kHptYcddFky-OmYvytJO8uJzSKUvgDE4B32SvtZZog-Q9Y-Eo_nC4ZgHmqmbqs-VbFe04LqY2_UQRySoxFeVKoKxXTwSS66uq1wXqTP1iYgC8zitrZ4plOo2jV5Yo_2XVC1whoSuaRdC1F9g4eG_Hku8yWRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=K5kG76iZ1yH27Tu-UzbzvfOXYRjPyYgHb9Pe06_c3bF8C3quFxr1sbdzA0ml2z8z2MGFGMtJdqAed0Ne5acI4Exa0K3lMmHZPeXsgTi_7d57KSRzEAE1xMnoowgEYxYhhxJfV3F-v7IEWyTQv3uzPNcyscHHeAPUQUtoH-1M_cRR3XHRG19gGQU_6kHptYcddFky-OmYvytJO8uJzSKUvgDE4B32SvtZZog-Q9Y-Eo_nC4ZgHmqmbqs-VbFe04LqY2_UQRySoxFeVKoKxXTwSS66uq1wXqTP1iYgC8zitrZ4plOo2jV5Yo_2XVC1whoSuaRdC1F9g4eG_Hku8yWRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMwEQgdXYl2rrIe7Pg9NnyFunftFhtbVuM0SKp-tgSGYMGu73Rxw7O7D18KQHkpDsxGtb7PcOdTlOKx1gbQrAL8DyBvRlr2ufhY-8Lam-bJOKaUb_WPqdGpQGeczFeHnOK5DJmJ1tGDPxIXIDKx8W5c_KWB3zWQGsEw2xDmJz1HEpeysv8eSO9WlDubN5m5gm1SlFajZ_fXWBAOQS3JMT5gl2cfyuU6i0TPu4bDW95WJ2apJuB7b61jPOQqkRr9-oTfj5milWCOjR4soNvfkc1-7ngo1yDk8aUVDFR2zASrWY2fn8Y7BNiMq4cYWtBwQuLw1RYMPlxoHnqt8JjblYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0wuHvAAOC0nK86HnVD1gMFR2Kwl7fW0dMYLQxesOgRa6aFMGGX_GESaKfozm2AMbe8u4Gl6WsZWj6f8qj1uWf9dD5f7UFOKn-6r-jgLfBEVxlmKKkJlz9pG105ZztGjeVeK_cpDKkWTpggyjW4BYqhaAEMk_6dOxMOIE7SrQsfPV7tWz57DWG7pBGsCeffvLgHXfDuAG91ZP0yi1goRX7w6GdQ-ZvUbYrTmJHW8vpv0HGEcUSdcs6Js_SfZsUFlHndYH0CNCkQAHzs50zoqp6YGbaKDqE3gOu5-7doTO-jIwpqIFn_16NWEAQH5AcqUhkTi-CMcbHruWuXPZu9JcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=Zu97IQxC1mJv5Lr9zpicmp6kRF5VfnsoL9CldR2QvSoeQy5IZ0EnG_29buZ8ixS67kyd9jnAVoTxPwnFTN2JcDjYJuNlaFdsTgeYSColxFXj1v3_rxwPcJNlBAAcwvAjU1bym-iBOBryytems0kCZWJzzINXMR_N2OM-p-sqetIuHvRBIgif2tj5A7KJu4VY7RBEHjBT7TJtVl7z97SWnwizvN1DIuSprOzCrtsL9L3VExCnsWSgx2BxQVONUuXchEkTi4stTKXeXN6KuG8vr6kZJZmSe7z-pw0E72yBu00UPr_8HaQ9TaQnvEkh64fRNNyXUZeLeoak8VgmqucO-AkD5TCqXKf_HXqWDWz9I5giNPbC6WZJW83pccUbStbCxDsZuRRz8bVBGfszOS3J78dduRWVgd68pD5wfyRj8AkOnmXeJmtZxf0CYvJW9jy5On6ooWvpQDMx2xewZ4k984Y6PEG3jhNn9t_l6bH5CDAKABRoP-Gt1lqDrMg0_vn6JsGITxXqUDzdFIqUao1Wk1JDFUjB93FRUB3HH42n53dlL6E9s_7lAOVrpzKwhzmd-rP36ckKBph3T71l3GVpzzlB68ztz9xzGeTwC1W1ZHi5vH7u3QScC1z3raAdwYhWL3VDtMqrMNlgkLSSzb8CxlLy6XtxCrQxbK_-9v_6oXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=Zu97IQxC1mJv5Lr9zpicmp6kRF5VfnsoL9CldR2QvSoeQy5IZ0EnG_29buZ8ixS67kyd9jnAVoTxPwnFTN2JcDjYJuNlaFdsTgeYSColxFXj1v3_rxwPcJNlBAAcwvAjU1bym-iBOBryytems0kCZWJzzINXMR_N2OM-p-sqetIuHvRBIgif2tj5A7KJu4VY7RBEHjBT7TJtVl7z97SWnwizvN1DIuSprOzCrtsL9L3VExCnsWSgx2BxQVONUuXchEkTi4stTKXeXN6KuG8vr6kZJZmSe7z-pw0E72yBu00UPr_8HaQ9TaQnvEkh64fRNNyXUZeLeoak8VgmqucO-AkD5TCqXKf_HXqWDWz9I5giNPbC6WZJW83pccUbStbCxDsZuRRz8bVBGfszOS3J78dduRWVgd68pD5wfyRj8AkOnmXeJmtZxf0CYvJW9jy5On6ooWvpQDMx2xewZ4k984Y6PEG3jhNn9t_l6bH5CDAKABRoP-Gt1lqDrMg0_vn6JsGITxXqUDzdFIqUao1Wk1JDFUjB93FRUB3HH42n53dlL6E9s_7lAOVrpzKwhzmd-rP36ckKBph3T71l3GVpzzlB68ztz9xzGeTwC1W1ZHi5vH7u3QScC1z3raAdwYhWL3VDtMqrMNlgkLSSzb8CxlLy6XtxCrQxbK_-9v_6oXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETibuB3oD3VggTMRJ6UTd4a9JyjbZfrlF_-jKzzj_ocngycHQSiz8mDCmdPvxIK6ZXqNMKnsjGcL8imNUm-Ew4hqPoG6SQm_3Z3GLQTfRIyBxyFTlKBWLRdCoUWabpJv4piiWnWjbAoQZX19rrnqX-OeDuqN9FmeLlu7ztkKfkXEAtZuM0EvGFJVTR66FfQLVM5vqVFTJM590AOWCtaoX3lTRFb1pqv06_I3OuFVcPc1ReO3tirvYXmRJ6X21v_yHxUOKqWLipX4u799nEq-lDbA81MBXGg9CqnDffFhpjPGx9r8SW0ORq37Yz-Hm3IhcW-CMsI4sAfyPUMY_onTlGgo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETibuB3oD3VggTMRJ6UTd4a9JyjbZfrlF_-jKzzj_ocngycHQSiz8mDCmdPvxIK6ZXqNMKnsjGcL8imNUm-Ew4hqPoG6SQm_3Z3GLQTfRIyBxyFTlKBWLRdCoUWabpJv4piiWnWjbAoQZX19rrnqX-OeDuqN9FmeLlu7ztkKfkXEAtZuM0EvGFJVTR66FfQLVM5vqVFTJM590AOWCtaoX3lTRFb1pqv06_I3OuFVcPc1ReO3tirvYXmRJ6X21v_yHxUOKqWLipX4u799nEq-lDbA81MBXGg9CqnDffFhpjPGx9r8SW0ORq37Yz-Hm3IhcW-CMsI4sAfyPUMY_onTlGgo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
