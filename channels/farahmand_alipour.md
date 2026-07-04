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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 15:31:30</div>
<hr>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B46qcDMo6RYxaj-UxKkLkDM9oJWBs4YdTd2cuaciChQGftegZ2ON8BJtsJAhtasxb_TispDy_dF4vlsAxgRb33WoEDrjXyUBqJ8BxnlDp2H2oFkTzrHIqWMdib4LgGOj5clIVEBmaFu4Q7kLi68wAi26jSQ8eMffr-c7UCQE3nKGaMHI8IkH8LCUhAyLf_BA3xk6NYfFPVRAvyTp3KscA0XUsHscs4AwFq_HSOGCjQwO-Clks3Z9Q9Silb_tVWsCsf9IVvFaV9fz1KuE_vMoXrCHggX4OV9FcDePd76m4-o37QuF1WD6pN1Hc8y7nVqmAnyqK0SdZlJmKO5ZdGvRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuwvQxP7MWyGOP7Jy4AhvuaJFv9Hb61w4gpKTyBcBF6F7t1GtOXMxj-_GiBON2JVB_wwXTWfP6bDTk-g_9EMrxsq7f4sDpL2a4Ire73jXSh8akgW3hVulH-y5j7B9FXJNW4ZVZ7cqiROawcm3MNzNXVeyOxLhOmqjCm07SuFHzf82FBA2w1esHrBZkXggWWmJ9P0dZLCHUJ57ZK_1ha-X15pOKZ0lwfDLvSGeW2NbXdhMJTfg6gC3wj-OZwe4gOjgAFOTqQGiLWAjQqja_cc_2EzaMzNJ5E7jb9R2gIRvXHXojHyD1dPDBXB1vtrX8BWLbCyesP-hr5B6dBsgfy57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=MMG0BllQZBiM_JP_CWbdyZXFIG33aiIkGvrnv_Rmuy-vQq0TxPv08oAmG9ETFfwU8_M0zLBDS4C-NpkN7rOJAHk4V4YTaMc9tZQGveqv_OfD3fF3twEh9_qSX0Ptxpo_Gwu8VKmoPbt3gYqeWFQ7qtX-m_9rLr9z2uY6iWkHmQZtwHbNxOQH8L-fkwLxRc3t7LegyFIq-sOqyUgnhZ79-_mOwoJk10jPJeeBxsDYMmGsx6_NfL5ZKnd7CCOVAc2XOcyyRPrX8KbJbWdVUtOqAbF2ZLHQ7u7SkcyaoJ51rFXOlil029JUs4V7z9_bBzANnVun5tqYMwWdPerw0rbkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=MMG0BllQZBiM_JP_CWbdyZXFIG33aiIkGvrnv_Rmuy-vQq0TxPv08oAmG9ETFfwU8_M0zLBDS4C-NpkN7rOJAHk4V4YTaMc9tZQGveqv_OfD3fF3twEh9_qSX0Ptxpo_Gwu8VKmoPbt3gYqeWFQ7qtX-m_9rLr9z2uY6iWkHmQZtwHbNxOQH8L-fkwLxRc3t7LegyFIq-sOqyUgnhZ79-_mOwoJk10jPJeeBxsDYMmGsx6_NfL5ZKnd7CCOVAc2XOcyyRPrX8KbJbWdVUtOqAbF2ZLHQ7u7SkcyaoJ51rFXOlil029JUs4V7z9_bBzANnVun5tqYMwWdPerw0rbkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=GqzkH6FKXLh-i3yJVAdsuqggsAXmK5HqP1SM9pF9LeA2r48LjaUx4uRZTacm37HFMioQ7EgggdF0yW4GiQKtIZOJciERVU8dw7GdNCcLzPvgt3Mc7c1GbvjnaV5z-6FsyAf3bOVbALkWF5dZkvcO3iodYsbIEMaNp09ZeP8Gl1N4XwIwO8oOGyv_QYhpDDgLBmMFgB2q6qZXaV1H32UTHGwJXabq9WrWtNpzh6LbDsqaJ8A9aInLXKHxhnkQ4-QmmTtT4_QUAI9ecD0TbVcaJsd6hRnt8_eXJMl4gRXbifFjQnozEHQMFkbEQROR3cigwSeucdl21L5ff7Pl0_e1bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=GqzkH6FKXLh-i3yJVAdsuqggsAXmK5HqP1SM9pF9LeA2r48LjaUx4uRZTacm37HFMioQ7EgggdF0yW4GiQKtIZOJciERVU8dw7GdNCcLzPvgt3Mc7c1GbvjnaV5z-6FsyAf3bOVbALkWF5dZkvcO3iodYsbIEMaNp09ZeP8Gl1N4XwIwO8oOGyv_QYhpDDgLBmMFgB2q6qZXaV1H32UTHGwJXabq9WrWtNpzh6LbDsqaJ8A9aInLXKHxhnkQ4-QmmTtT4_QUAI9ecD0TbVcaJsd6hRnt8_eXJMl4gRXbifFjQnozEHQMFkbEQROR3cigwSeucdl21L5ff7Pl0_e1bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=KWBbwK6y6rUmUAoxfRm0kBV-pz2Pq3MlRIpKi784OMJJwV3kgJiwkRlMo-iSQHpE4KurN0dr1KEAWtaa_WW3DpmeeMVilhhcHyBrwdZzEVV7lLf5h1cD3nReiYQRrEPB6MuV3b-1ldMywK63WVMg2PefEBZvT9fslrGClzZv4FyY7u-atkTmH5RUxYLzACQOXfpnEzg6724qGdxHAHmAk7XhI8xKtTAjajyEhtZGLPqRTI0HqYaN1l1S66IH-rWgXqR_0Tm8e3FHNdhgzLWLFJ3xObGiwRgWaaQRRBue5W03Z7NAg5JQEmDW2u7cjXfe2TVG7y4yU44IUTA6Eggu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=KWBbwK6y6rUmUAoxfRm0kBV-pz2Pq3MlRIpKi784OMJJwV3kgJiwkRlMo-iSQHpE4KurN0dr1KEAWtaa_WW3DpmeeMVilhhcHyBrwdZzEVV7lLf5h1cD3nReiYQRrEPB6MuV3b-1ldMywK63WVMg2PefEBZvT9fslrGClzZv4FyY7u-atkTmH5RUxYLzACQOXfpnEzg6724qGdxHAHmAk7XhI8xKtTAjajyEhtZGLPqRTI0HqYaN1l1S66IH-rWgXqR_0Tm8e3FHNdhgzLWLFJ3xObGiwRgWaaQRRBue5W03Z7NAg5JQEmDW2u7cjXfe2TVG7y4yU44IUTA6Eggu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hLVQm0BHqiI2Tq7fGrDCFyKSffr8z1kXF1SJRdoaylvgwQZoZZxSua6maAY3gdR3I7Slp9cI_Ua1miJ47UvNS6E7MovRhngw6hWXfL4j_mQ4aixz-Iz7pwerQUUYGy35hHrCRjyMc8rRWkFyrLwkklr6eSg4TR1YhRp0qOoGbR9pxMt-cj-cSSr309-wZgEV65a-Go_rVTOcfOGGl_XboLIBNqzy26AxyPxSunzzyC99a1xeCXAsMFLc066lOr1XtEUpXeCM5PvyVxXnh5mvhMYVojFxJFPRLCKlgz_aHLLhGOENqdsXYu-aiDZ_lemUFi_ok3on9-6Hj7MDIDO8nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hLVQm0BHqiI2Tq7fGrDCFyKSffr8z1kXF1SJRdoaylvgwQZoZZxSua6maAY3gdR3I7Slp9cI_Ua1miJ47UvNS6E7MovRhngw6hWXfL4j_mQ4aixz-Iz7pwerQUUYGy35hHrCRjyMc8rRWkFyrLwkklr6eSg4TR1YhRp0qOoGbR9pxMt-cj-cSSr309-wZgEV65a-Go_rVTOcfOGGl_XboLIBNqzy26AxyPxSunzzyC99a1xeCXAsMFLc066lOr1XtEUpXeCM5PvyVxXnh5mvhMYVojFxJFPRLCKlgz_aHLLhGOENqdsXYu-aiDZ_lemUFi_ok3on9-6Hj7MDIDO8nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXxSDLlUePGQsu6_bHEPLaz7rerSO839oNpE5JzXuURKpLtG1ehiTDDqAI58tbtaezQTzTI0YvGWknhYJxP3cv43t65JSviH0rhlDsupU8KLRifmakRQWpOwabJAa-IL86VCvUEoH_2nPexnOeBjuo1s35L7ysIWf5rT6mRjUxac51Q4vtUrfberdinlpAGEYDWKGyGdQrAKhijZGz_HCyTtKtFBIYUxR4r-F1QFUiSUYAFjRPPJzcP5PYSbNbzESqt9fSL_E9CGprvMjo590bxhismlq0oVl3ySAdeEuLt9mCNfwC2Mx31TyFrVAWqXAibFiqem1K15fSRaux-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kH_f29z25SSN6ZiSKx982dEhznngLNMZlbmC04Q2QJ3NkawbyLDliRKp3qBQicTr94acepklmSK6QHTjk6If6rnQmftfPcu7iespMIWrxJ0hH4hbK8GnXx80JQJeAlIx6Yh5_ujvnwHdVNgCjmcCWAo7Gsg44scBnuiliUY_FBVgrqlcG8uQXOGYAiNwVHLhuSzb5qdH3MZj6idjBG0JXM5awIeTUixuJUGLmR17Iea_xpZr8yRIzhA5pc166iTRjvBCQL5ZuUkq3dXO6W8D6Ymeyaol5NjocT4LxGnpm1P2q0bVK0scxZ0RIfggGwazSz9xApwnvaA1725I1pkkmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOpDUgL7BgRgOkqy4jb7QdzAU7mFEjK1zKzusFAPf1p998ztN0LY6YyJ3f6pUuKcTPB7Ce9tit4vQpzILhHll6ybAQad_QNR0nkA-u8sY_dUY8tegmfO-tNVgNoYukMKWiL9QePkZ6GpP7wrUF-TEBwL-Fjxjo81LYDZHM8s9-KFtHvolKuB-WWuwU5lZrwj2Z7J2iH8BpOK_Ec6x2Dbw-wW4fap7reuAhxcQAb1i2gM88er6MGA1wL-NZaV4cP3q6PLTKOoFLEuuqFPD4gV8pEutgHU0YW7m4hHTHKAwcTTZOyWIayw8r9LhpzpNfsWVa0mUBiLORvQszZ7Ht0NVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nubrDYjzG2V7EqWJ_0bmKmjUxYRSeEp1H5sj0yRa9CqginF-2q5PYzWh8hWoD9cwXhvFcouhyzlO8dHTJjEZGA2_MPL_2IvFpivYrTlaKfjCKbdLkoHPd-6ysQRWS-JlTx0wnswNG-gAV9BGxwFfjXZcmkTk5zQ_IW1tUhTkHV-Ywzg4r_ryVi6oYL_8WOqYXgpGoyFNkn_p8_EmnAWqdC5EQIGUOdQN42c0_DZ8tiV9TuCJ0gkvVFgH1b9aKDKWCVD4zQaMpaOicyZDIbm7iGv7b227B5t00wFcczT88RzbkZHwjAUoD8bqOO8Iu-t6O2WW_Nk7ZajmiwNWsNQ2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1JCzqfnvjq27kE9BaAQ2Qht3JF-LlPicYwXIs2GXHRbgvrsWdeWrRFEZGEXJTev0-SlxGXr6PeyBDo6PWtsWFsHtzIrA0L5gMJIxhEzPzKVLiV1wsZJuxOO4EhkeWHwp0KdA1-krrabP_Z0_2QaTlakKus621gyWeqaVReVnAY5hhGILZQOKdmZdyN7Rcng9Ade5w2RfUlvGL2K7Mt8v0N7xnH9wbHoinh_Q2bUnmb64f0KGANGjJDl58d7Txq_v9oJnRVz4joNzuz7zKUzX46ZbeaUmvRNjBlb_tEo2sCjjsFxXrzPDSVc6ByoNijmoguT1zoOvNWkwsGPdrsg6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVB-n45NGvcFpWzRdxdBXQYcnhHxa97b6KZTKcim4lkHM_1OwiI4v4BEL6m5kyVcWhv301yKRUflakeQNABZ_6S1Ak02w5eSYgwyW4DEYf6gfcQs5-voiZxZWbFoptHanJHvjW3c7-t4e5ZQajjlDlWoJJMVFYdexorVUAICQ_UyVZu_Gmuv-s4tYVXMWdeA1iRP2C1PLebsrDqCBvtHIMY9Gz-vOrGK1mfJU2WaxQKrj4U01UqXhuj3wdBCycFsgb-cNRtm-z8IpihoKXGD44KXAKhyuxGfY7jg03a3rtPoioL4D_yE0VqQfq6Xl4va-P18nOZlwuLJoY29tyoAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUQ87jqawjvN3lDwrmDS4YUhjOVc07HdHBOyeTsUpcZQbnnqnjuPNHzQPYVMYFmcM3Udu5J0IDGUXAx1M4xyidGPKQkiNSmKDciJkPdUE2p-dZpsSE9BkGLxwX3ohtgKIYkmXWa3tH5UR6iLJNzdIDsLmoNzmFhRAyfsgo_0me9L9p11v04VxEh4QwcR1HfH0O_YNN9FFw59uQqeKIhMJmkMetWcZGCV0AiRaUHjUsv9TsHBm1hJ1yav7gpEgxnLDw3xpvMl5r4VeK_GStiC8Zf6LW9lzcTsvTC0i3YFCDP3qDWA54XEpiNkY5A9c24mVMfnllnrVM-YJ6n5ofkD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPcShgoRlXKAu8_pxPEmY9x0b141ij-XrYhVMRmO0kDoI5Lhfz6JvnSDs83TmNYAMEHr3_gJUiX5vakf0iuKsc5cShCsETTJZNkL-gqw-UU0AFVapxKhfLl0xdCM-nZBwoR2VNDG7Am3BI7kd56v2BiT2_aLSSnczXGdHpdNSq-bX4a5ob9wctLNGjcCLnGLImiaIl80br8pDKz3ukEMsXRunycVBkBqV8R8Ijbox8XlblhomD1ONkcVqiIjfn1C6YDr-YL1O10pZwPAYxWDH8n-buLTZ-K2d5CqWppsIKQ7O-lfAiJZ_UyLG-uGoPDx6mDFFP68p0HG6ZQSxmIdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLBrVHUotH7P7il9LlRNgaxw9sbOINBrEz3uQQi05VCnWxKwB9hL0JSJkwPBXnWnmBcuKnV2G2V9ws5PJlDe3hHgUDVHOyuoVsUMPIkSJoV7qALxauzDx8XP-tC0R2xiV_rSpmUEgskYRcS9NL9Su5-SjIlAa1dZXzr_0T2ZokR1gfGOJtSnvZL6K1STDJp5TxU0X6jEeHTu7qPRgTD-5Y23Kh3iwLIK8LSn7oeprWSh3BThmpFWU27jKKrVXnLjrF1sXOEN7exiE3Ve--zbhAbjU7GzOgYby-2DKRBoKZ1ljHEiPCFe11BFpqZP5WG0ILy28sKshEbKnItEn2cexg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=nbcJXGY7raS7hDoFafi-7jSX0AXy1RcB760qw_i3eJ7DBVpFYeOONEx77QFXt-qPvhp7K__g5Kho8DLEM6hc1S73ocqiokBl0VD4EWGSZOMTJzHbNaeyepxvJc3aLby_qv48v72u_Mx4wVDHP0rAAviD2-tzl1bg-KCStRj6DbA18IXFDaKLOivN3nxAcpsFXs59VRXrPfqd2OxgqoqkBRAM0fMqWpgSTlQvwomx9Ycws0CDd0vuuGPwtfj1k5c3E3Uo6qH6_UsGQG07ha_PIfdnl_ejSvdPxzwAounbgasitPsGBOKxsngCj92jwqELED0xbHEWGIZLOlrEUue0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=nbcJXGY7raS7hDoFafi-7jSX0AXy1RcB760qw_i3eJ7DBVpFYeOONEx77QFXt-qPvhp7K__g5Kho8DLEM6hc1S73ocqiokBl0VD4EWGSZOMTJzHbNaeyepxvJc3aLby_qv48v72u_Mx4wVDHP0rAAviD2-tzl1bg-KCStRj6DbA18IXFDaKLOivN3nxAcpsFXs59VRXrPfqd2OxgqoqkBRAM0fMqWpgSTlQvwomx9Ycws0CDd0vuuGPwtfj1k5c3E3Uo6qH6_UsGQG07ha_PIfdnl_ejSvdPxzwAounbgasitPsGBOKxsngCj92jwqELED0xbHEWGIZLOlrEUue0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Xj67JIrwEaDx1kCqGj91RGukzzfngpKq98DTXiLT_XcqMlLUw1AR90k4ZaY7QQoHMC8-uPgF40p7gp2cWVRrxxfAxa6RGZTfOpjGA8bBXG_izg4xGqfyeWYfKV9Db6cLjQC1Rx8qv1gxVVYZ7jrxsBbo_7wedYv0AIPHV9LMoCblmtX0cb9BEw28qucA2XOC8veFPClGaHDBHVPxpPr3rk0TEcG9kC_5cCsn-jjaIzBHyzgH1q389rTFJ1vSHf0761tyQO8MEiuVHiKTGBOMfRd6Zx0NQyBfsIMpJzGAB_6blQvLsSm-AzUOu_MlseGopll4YWyIsF6p6v4JAA05qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Xj67JIrwEaDx1kCqGj91RGukzzfngpKq98DTXiLT_XcqMlLUw1AR90k4ZaY7QQoHMC8-uPgF40p7gp2cWVRrxxfAxa6RGZTfOpjGA8bBXG_izg4xGqfyeWYfKV9Db6cLjQC1Rx8qv1gxVVYZ7jrxsBbo_7wedYv0AIPHV9LMoCblmtX0cb9BEw28qucA2XOC8veFPClGaHDBHVPxpPr3rk0TEcG9kC_5cCsn-jjaIzBHyzgH1q389rTFJ1vSHf0761tyQO8MEiuVHiKTGBOMfRd6Zx0NQyBfsIMpJzGAB_6blQvLsSm-AzUOu_MlseGopll4YWyIsF6p6v4JAA05qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=VCqlJopigU54Z5Q3cdKiTGGOPrEiBIQm3oiX9VADbZPYpHrR78NNORe00KRBoCPcuEupUwnbrfVceeG0GkJmaFWiucDCExTjwev3nPl5t70QcGLnpwrzQgvo0zeOC02c06EP3Ox88y3Gw-NvY9eDMKJmnpcpGKDo59kSZx0Sv234Pp77XhE7jZ_fzR49MmwtCgA760HIfZZGsOa66iJMiAWtyNFHlmlihG4RVzYMQwGVJGHxp_XXiAtrrKiWkRTVecO-QzDhycU89bO3FEpNU9fFrQhsof836c7K9114yYRY9ZLSDbIdwscANhAxzGDVlYwelN1V1thJ2t9V-qFGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=VCqlJopigU54Z5Q3cdKiTGGOPrEiBIQm3oiX9VADbZPYpHrR78NNORe00KRBoCPcuEupUwnbrfVceeG0GkJmaFWiucDCExTjwev3nPl5t70QcGLnpwrzQgvo0zeOC02c06EP3Ox88y3Gw-NvY9eDMKJmnpcpGKDo59kSZx0Sv234Pp77XhE7jZ_fzR49MmwtCgA760HIfZZGsOa66iJMiAWtyNFHlmlihG4RVzYMQwGVJGHxp_XXiAtrrKiWkRTVecO-QzDhycU89bO3FEpNU9fFrQhsof836c7K9114yYRY9ZLSDbIdwscANhAxzGDVlYwelN1V1thJ2t9V-qFGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Sr8CnavAEEq8EceHGeONmaY7oWkgpMeMZvhoSoOFhLz_AjjEy41NcyUnMgaNRGXXBujRNhqU1m8KiAPoUyV_9NyF1whgpGUhU0Ay3T1NKRwMPEw3dobD7ZJ7Klipn1cwyfnW4Xc_QaxHIlzVJ3Wn1db6qcrJNwFOI9oYC8D2Wo0qzw7DsYDHtanC3TqlX8EUyzcYQdUx256TXUB83vjeEDDp7EtFX26JIecERjSquFw99k46Ya29kCjT-_X_dHJah8OHnrIKugI8xX7fDebNkEC2zrWc8LCmzkv25zSoOzJRM0YC5DLYDdx-TduXiHjEHrt5vkqIT4NZeDftYX_ONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Sr8CnavAEEq8EceHGeONmaY7oWkgpMeMZvhoSoOFhLz_AjjEy41NcyUnMgaNRGXXBujRNhqU1m8KiAPoUyV_9NyF1whgpGUhU0Ay3T1NKRwMPEw3dobD7ZJ7Klipn1cwyfnW4Xc_QaxHIlzVJ3Wn1db6qcrJNwFOI9oYC8D2Wo0qzw7DsYDHtanC3TqlX8EUyzcYQdUx256TXUB83vjeEDDp7EtFX26JIecERjSquFw99k46Ya29kCjT-_X_dHJah8OHnrIKugI8xX7fDebNkEC2zrWc8LCmzkv25zSoOzJRM0YC5DLYDdx-TduXiHjEHrt5vkqIT4NZeDftYX_ONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=oyddRdVFF1T_eAYVwCHx5t4e80kCU5Un_pniP9EtXXSqOf10BpSckLgdlzYnz6-RFOqVzhnpDq59LXjPv_0mq7bxy54qDMk_Sy9jxnd-5d_Pf_z2AzHzGmbGtH6okD0Lb1otCjoJuqFJ18hEdFoyPGeCYkJuRl77Ok3VhgFXwJYWi4uEehwmJi3l_IazrwtYwbu1a5DjdWa5vDoebj-8lgIf2Q1fa037LjyLGyuTJN3_ndBwIca3y0xaj8USdnkpDZdLM56DqZrU6cPRaYzE69bMx5QybYg4h25iV2JT2hGXrjBwDol19mAAx7jBVJBCLgwIOYBGkE1JAIbkwj4EZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=oyddRdVFF1T_eAYVwCHx5t4e80kCU5Un_pniP9EtXXSqOf10BpSckLgdlzYnz6-RFOqVzhnpDq59LXjPv_0mq7bxy54qDMk_Sy9jxnd-5d_Pf_z2AzHzGmbGtH6okD0Lb1otCjoJuqFJ18hEdFoyPGeCYkJuRl77Ok3VhgFXwJYWi4uEehwmJi3l_IazrwtYwbu1a5DjdWa5vDoebj-8lgIf2Q1fa037LjyLGyuTJN3_ndBwIca3y0xaj8USdnkpDZdLM56DqZrU6cPRaYzE69bMx5QybYg4h25iV2JT2hGXrjBwDol19mAAx7jBVJBCLgwIOYBGkE1JAIbkwj4EZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mNA2hRa1rYyxHJ2a_BdjIb1-CosqKtC-gkzfaQvz_KaQGK4OlHbeHC62gV6HO6i43vQiiAIGlvdS01WOVLJq-T91UTo5Z0eerEvuWXkI2ZcLvvW0VPBeKrE5tem9qeBhAAB8IKvV0uye31Cgax9elVzL1mMDgylP3u5VX2s1RApoegVdhbQ_5yEkUc6F0i8PFJeju8L4x7h5d8AqkYrBnA_PLfTIgjdS3-W-Pdv1dbvDR6ZMOeG7mxfH_QqixdvFucQBJAdAKxRzS4iLVscze4_OcGieA5v3sZjtoopJpPCI8sszU_Y2N6NSI0-diF-owUaTRuEP_ZDh77a1VC4Kyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mNA2hRa1rYyxHJ2a_BdjIb1-CosqKtC-gkzfaQvz_KaQGK4OlHbeHC62gV6HO6i43vQiiAIGlvdS01WOVLJq-T91UTo5Z0eerEvuWXkI2ZcLvvW0VPBeKrE5tem9qeBhAAB8IKvV0uye31Cgax9elVzL1mMDgylP3u5VX2s1RApoegVdhbQ_5yEkUc6F0i8PFJeju8L4x7h5d8AqkYrBnA_PLfTIgjdS3-W-Pdv1dbvDR6ZMOeG7mxfH_QqixdvFucQBJAdAKxRzS4iLVscze4_OcGieA5v3sZjtoopJpPCI8sszU_Y2N6NSI0-diF-owUaTRuEP_ZDh77a1VC4Kyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Lx73JEnCyA0B1iPVvmIua1fPhfz2sKM54_nn7bXmivfodZnLWx1VZGpnzgEuLCP6CR4mK4ua6x6fjGg5zmBxM2TSRQ8w-wJujGlanKA51F-q--AAKZTsIB2mEK0EE-Ud3IUA7Z4YtKf4ytvb5QZI_5coXtxOCTjTmPS0zKicoNX2_Qx0NkLhqQS7TNe0-aQ-ho4CItJDLHLBadgCv1qksyCw-q7KFrSmpBs1W2kSyTldp0U4ZK2oQ9CaHua2Sp2KTKUsl9LasC58mUuEpqHC57pB-bFYGAX9mdKQiqj2hO52qya7eXunVdDcC1fzZa5Iu7k3sle_XX9hALOLxqdh4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Lx73JEnCyA0B1iPVvmIua1fPhfz2sKM54_nn7bXmivfodZnLWx1VZGpnzgEuLCP6CR4mK4ua6x6fjGg5zmBxM2TSRQ8w-wJujGlanKA51F-q--AAKZTsIB2mEK0EE-Ud3IUA7Z4YtKf4ytvb5QZI_5coXtxOCTjTmPS0zKicoNX2_Qx0NkLhqQS7TNe0-aQ-ho4CItJDLHLBadgCv1qksyCw-q7KFrSmpBs1W2kSyTldp0U4ZK2oQ9CaHua2Sp2KTKUsl9LasC58mUuEpqHC57pB-bFYGAX9mdKQiqj2hO52qya7eXunVdDcC1fzZa5Iu7k3sle_XX9hALOLxqdh4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFO04IvdDlqG3V0FGBMJoku_wdWwXxjJFXCn6FwoN0tQTw_5LZ5KDJAMe-_UY-Idyot5j18GQpdz7FW3AAVHEI4j02w8pHqpqUa9fc4DQrHZ3FEDcZ9_euWjo7CmFFp6QPlkaHNn9wZrsj2oeVefCWapW0cJ2D_xvL9P_tZPTGmheOEOBLZEj7y3ERKPP8ok2NBRhV5_AFZ-v6PIb9SZMgabb9JDW5B2XMnEdg2SeoRyMY-85Zb81VssisV81DV0BjMVBZvT9qO83clqFkqhi298scu0iYtGI2zTwUV-Zw_LLR26jnFuawoaPaiqdlFDWq52NYhNNjXPXIDhlBjy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=pPYl6s_m2aACCFw-K7NwxAZi8w7rfpeVvDOpNvKY9O8N_Qlp9YaATPIsPUSjO2oHNfKwz_ULnR5Uqkp3oDrf7w7D-bdolnVEFnLLVMBrYoHhB3mABbqObbmE8QZfON6NA9Dr8epfCRk6ty58kxgTII7BYhTxDLkyGcRAEXV_B4WVY9vVuLaNi_TLUxSUKntXS5ISREQr5S8da50CPjwmzacxjkQgEvp4Xl5IDj4iDqu3ksjBUX0cAXtAacb4Ako2qR_uJqbbkeEyenvrWucWuvWYiQWZWR8nDod2zrztTzKayk-jTx-r2iNMkobAyrsA6i8uM8Ol5zp67Z6KQho_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=pPYl6s_m2aACCFw-K7NwxAZi8w7rfpeVvDOpNvKY9O8N_Qlp9YaATPIsPUSjO2oHNfKwz_ULnR5Uqkp3oDrf7w7D-bdolnVEFnLLVMBrYoHhB3mABbqObbmE8QZfON6NA9Dr8epfCRk6ty58kxgTII7BYhTxDLkyGcRAEXV_B4WVY9vVuLaNi_TLUxSUKntXS5ISREQr5S8da50CPjwmzacxjkQgEvp4Xl5IDj4iDqu3ksjBUX0cAXtAacb4Ako2qR_uJqbbkeEyenvrWucWuvWYiQWZWR8nDod2zrztTzKayk-jTx-r2iNMkobAyrsA6i8uM8Ol5zp67Z6KQho_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=c4HX8Bol4p8zzmwKqiLoUodWrkWhnysqQRTk96rUBgBCKyKJKTfsOsma49NBxHab9JY7Ibw44faUE1YB7DU_Xdz8Tz_dCOK7_DOpQ6nvPM1Lhpuy7itn7k7ClhFXabqVoEIbkoK7difzr0mG29GGJgpkhIa0mBDKH5apu8DnSdz6UDDl6TacVEMO8AR2dzr8_0XCXC9BxJXsKAq6fAyuhjy9ms2e7GFC78oXVF_L86bwFj1Wsr6q1-3pWIQ72HdmmBYX4te2uPNxLn8fSlXKK3xoQFqhf6FsZ1nrS-OCX53SrLRo03ty75GfaITiBHsARqYmy07PoImvtoeRW1MjJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=c4HX8Bol4p8zzmwKqiLoUodWrkWhnysqQRTk96rUBgBCKyKJKTfsOsma49NBxHab9JY7Ibw44faUE1YB7DU_Xdz8Tz_dCOK7_DOpQ6nvPM1Lhpuy7itn7k7ClhFXabqVoEIbkoK7difzr0mG29GGJgpkhIa0mBDKH5apu8DnSdz6UDDl6TacVEMO8AR2dzr8_0XCXC9BxJXsKAq6fAyuhjy9ms2e7GFC78oXVF_L86bwFj1Wsr6q1-3pWIQ72HdmmBYX4te2uPNxLn8fSlXKK3xoQFqhf6FsZ1nrS-OCX53SrLRo03ty75GfaITiBHsARqYmy07PoImvtoeRW1MjJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=qhwohSF-wwjEKe3WHkmCloDa9t5Rwd1PZl04w_nHbkNWN1obFVLHzco9HSakSKRZ9_61KggHs0zl7F5QluMYcwTQdPOBGZ3xKTCQcCFtl298ywip1TYCzQCKYqnxSj0zkUqvH7KleaOv8Qak6ZxKp1bjTdVzp8giRY3s2G-E-vMhxhqzY0x1zwddjs7s8FvALKno-DqBIpue8U9SI2hOtJmXeOlH-L8G4yFGBUZ9p43zyQrhjoHFqIGd7QbebkEqUE5N11Qih5Wl72Cl0XSLfKb5bLvzXV-oRzcOl0ln9lk6p0Ez3_3Ss4Q3tHNNxXM32E0g6qF0yGeEzjBnfAi2K0IVELCFZo_6SAiqPc3Bzjnt95vt-bXnAZTCnDnDGYsOk5LQKvlwpj6iiFYQzJ1Mfwz8CovsbwlyFixoQ785xYL_feTrpev-5nIG1_Qf_weoNRXdO2Oo-VYYwVRphSGG9RfqmLXEpg_8WMesnhmM6eZi3OqQgQDxwBvvqFLOQCHKB7lCHMzuTK9ALq7L7u02wYVscr12A9Z7gLLNBPSsOqbc41BneuVa9iMCGxUIT2wDgpWCACQRMvkOgmvm-LJ2ZG7Ax4od_oGgLGmhNDlQ4QC_SI5Uq4P7xy88ZiciTvNFlgBNHkor3jlH_IxstwQ9ODksX5-dhPmQ8LUyWVb8X0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=qhwohSF-wwjEKe3WHkmCloDa9t5Rwd1PZl04w_nHbkNWN1obFVLHzco9HSakSKRZ9_61KggHs0zl7F5QluMYcwTQdPOBGZ3xKTCQcCFtl298ywip1TYCzQCKYqnxSj0zkUqvH7KleaOv8Qak6ZxKp1bjTdVzp8giRY3s2G-E-vMhxhqzY0x1zwddjs7s8FvALKno-DqBIpue8U9SI2hOtJmXeOlH-L8G4yFGBUZ9p43zyQrhjoHFqIGd7QbebkEqUE5N11Qih5Wl72Cl0XSLfKb5bLvzXV-oRzcOl0ln9lk6p0Ez3_3Ss4Q3tHNNxXM32E0g6qF0yGeEzjBnfAi2K0IVELCFZo_6SAiqPc3Bzjnt95vt-bXnAZTCnDnDGYsOk5LQKvlwpj6iiFYQzJ1Mfwz8CovsbwlyFixoQ785xYL_feTrpev-5nIG1_Qf_weoNRXdO2Oo-VYYwVRphSGG9RfqmLXEpg_8WMesnhmM6eZi3OqQgQDxwBvvqFLOQCHKB7lCHMzuTK9ALq7L7u02wYVscr12A9Z7gLLNBPSsOqbc41BneuVa9iMCGxUIT2wDgpWCACQRMvkOgmvm-LJ2ZG7Ax4od_oGgLGmhNDlQ4QC_SI5Uq4P7xy88ZiciTvNFlgBNHkor3jlH_IxstwQ9ODksX5-dhPmQ8LUyWVb8X0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=XI8DFDsokaonUajD1JRaAjqvEgnhv9J67F2CD1Xj5FMhmQC4ZmI6l0aM8yzVAtIDt8JcdOudX3PxZDQVUOI2oFDCzfBcSY5Wgycih4EJyNFOAhGqefysAnw3fIZJYJiG466SmODXi8wqxmS2hY5H1FFAmjZt4B8JaWLPHwytaGLuk4AJZXN5pRUQQQe53ZbRg5g_LQaTt64wxU3nJE8AVMhtxCTiNqgRo_ovjzKIarLWYOkeNZv5NnXvHBcwwRHO0llXWT9R3fmqQ9AfuJWKGpUoLA5-eJodlbimPuPmX4lY28_T3PBu8NMKOiqrWPUNIKwLsOo6s5BW6GJJpgQ2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=XI8DFDsokaonUajD1JRaAjqvEgnhv9J67F2CD1Xj5FMhmQC4ZmI6l0aM8yzVAtIDt8JcdOudX3PxZDQVUOI2oFDCzfBcSY5Wgycih4EJyNFOAhGqefysAnw3fIZJYJiG466SmODXi8wqxmS2hY5H1FFAmjZt4B8JaWLPHwytaGLuk4AJZXN5pRUQQQe53ZbRg5g_LQaTt64wxU3nJE8AVMhtxCTiNqgRo_ovjzKIarLWYOkeNZv5NnXvHBcwwRHO0llXWT9R3fmqQ9AfuJWKGpUoLA5-eJodlbimPuPmX4lY28_T3PBu8NMKOiqrWPUNIKwLsOo6s5BW6GJJpgQ2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=HNO5KDrePRSrLqj2ODh0iiILMoG33zxJJ1JgFM7ypdMpN6olNI1VSymKYisGqyafVgb2tRhbK9U_yN0pu2nyBUXuwqNvzcLNKj13KHHk9oXKE0IHZQ5-cHB9FKjNDCoorPH2x2NWx5ssW1zCcU97jHTQ6vGRNBG3aJpK0WT2gA0MY71iiLZ4OmbhDYyKKKqTv5blAo93Y59NViyQTDJ_PivbglVhFo3K1bj1ci2vtww-eMpP8uBgHXlEXclWBbrGUQCuq4Dh-aHbr6c8roj0XFvA7kEprLiCGIsjL-1_pA5-0OFLR-gC-3fhY1HQSMkUx7IbPJqshi2vzo5X6UlB3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=HNO5KDrePRSrLqj2ODh0iiILMoG33zxJJ1JgFM7ypdMpN6olNI1VSymKYisGqyafVgb2tRhbK9U_yN0pu2nyBUXuwqNvzcLNKj13KHHk9oXKE0IHZQ5-cHB9FKjNDCoorPH2x2NWx5ssW1zCcU97jHTQ6vGRNBG3aJpK0WT2gA0MY71iiLZ4OmbhDYyKKKqTv5blAo93Y59NViyQTDJ_PivbglVhFo3K1bj1ci2vtww-eMpP8uBgHXlEXclWBbrGUQCuq4Dh-aHbr6c8roj0XFvA7kEprLiCGIsjL-1_pA5-0OFLR-gC-3fhY1HQSMkUx7IbPJqshi2vzo5X6UlB3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-8DkBGzcpNMkGhKjVhQCRqMDebbisVoPi27mrETX61F9-7YyFGYGen7zHlJqTDN_RuV3UFGMACDVX9WBELXHCkGfLMvMT1-Eqi0lDmEnrGKtSC200WnL3U1QsEGyVLUCUUGLCmp-iw55mvemEsMMP0XXKpMQKoyJhF0HdZ6R-WdIzaLtvxk4Rp7l36No8kPtmlMmdRQojHTmorZSm4P1_kLhpSelbjGnbgam6Wz5rrYyzm9q7NRs7XkhlnX1Uk9wiOQUv4prmM7HjW7Z_iLN29pMfw7TQJCSIVK5ENkdLk0VCtFIemTsjexayxyWafpZMAtXFEEtcxvoa36bFSWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAQnDafJB7mAg11UVfQ4rs-qd-UcTsxO-R6GqnDuFp3sPCoaCn6B_RwGVS5a-h7yhsxIjeR2cSJQDA5onBWxRa_rb0g612JngC6RB9OK9iJ3e__CWNQfyIoUgIgYL-vnHsFen4ZAnAAuIa6BrDGsLVtBljHEM-btoak1offuPSBfnUmG0smHSqcpx5b1YwMH15n6wzqRk3_ZwYg6tDplwz4wHh8WN89oGbl3eKBT4jTydEFX8DvjBeQTXtNLBPavWVjbZ_C2YVxKTIiR1aLUH-jCdHImbTShJfyyo2PD1W9wtd2gaBSiwZAlHmlDXnscc0nku4JgjT-3CSbpaWTAIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=T7S8k2kbsThsYv1_oSiFJO8OAan8wsANA3SmLLKU_6uTcjy-FFh8akaBs_NjZZeuIZL20lRR5vwpYublM23wYtbci0-pCNwAxTPMDi4rEsHnTIWPnqYno_emMh9swvfOMiTbIXP0MvrI4xHIIdm7uElMDZulJQO0uyG-sVKJ9EopfEEzh0zGUAE94agzY1Kz7Bzm_07W6P3ShoOwVfcjjfUYCHXDzxQ4HbS5R7E_VAQzoXV9Y0RgbJQzaq2vmyzo01bZUdHRpoUT5F5Z40726l6_aidKn-LrIoVyQEGyM21RFHGeWPqR4jW6c0yUXeI-N-RMkf6QI5lkTK8a9yU-yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=T7S8k2kbsThsYv1_oSiFJO8OAan8wsANA3SmLLKU_6uTcjy-FFh8akaBs_NjZZeuIZL20lRR5vwpYublM23wYtbci0-pCNwAxTPMDi4rEsHnTIWPnqYno_emMh9swvfOMiTbIXP0MvrI4xHIIdm7uElMDZulJQO0uyG-sVKJ9EopfEEzh0zGUAE94agzY1Kz7Bzm_07W6P3ShoOwVfcjjfUYCHXDzxQ4HbS5R7E_VAQzoXV9Y0RgbJQzaq2vmyzo01bZUdHRpoUT5F5Z40726l6_aidKn-LrIoVyQEGyM21RFHGeWPqR4jW6c0yUXeI-N-RMkf6QI5lkTK8a9yU-yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJsRr9Bn09QvnDKMvFUm7HMTdvTe1nY4vWr5ELNQi1ZpqtvugxKkYdOGtYIF1DoXL9_BJLYMf7Uv15YfVs7_gJ8hnNJdbEZHWjkooKJwTWtt0_R1-KMByhJn_--xB0nr8NmGAk50z3luUwmR-VSEALoZP4kb44nXMZYoji5kulINR2MI_2Vx5Ko8poTitlqQHFXY1fQOnv-NfYIbrrbZhFoPZ8WkuASxomw7LNU4jQGIOv5zrl_VYHkrsxT_yeg5J0Juov_j25ethH5BIg15_mAi9bJdq0BsMl1TmfvSVnO37QuVRcIm9EUnrfgEUnp0JTQ0tJj5SKV3xHGiHQax1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCNKVMGBhNuUO3FuMJJshQDfaNaVvfbDbEaB7PiabJ63S8q73IhRGuDRkPVjj-0XKPNXUXcnDbbfPOfG3KWxHUznJwaq_7mPq131diOm1zBC4DDnoJ6vj_4YbWFIq-M-YwARGddOZN5ChIo0lxcIw4dAUsZw2wdLXz5qCJrhvDsPQBL45UicGYpjXR1Q963wWvGRJI_l9oyAom9hp8u09sYWMj7so_8BbVxIAkg5C5Xn5aOTN_2wzEqcPjD1Mxuw05mxQP7VN5DRX4SoU6VkkhDAZ2NBy6k5Q_SmQIk5EeiZRvmvF0AbRuJ45fT3b7SxDCN7VYfw22-Dfv0vQrzTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJfTFX61z1x02Z80S2SwkkJjdhX23sHnDEfDIBWITUk-dW0qpx-0hzCGIt9gjHLjZfpMl_99pZ5vGMUuTzha0Cj2Wc9j3zL3iBSj_RTK_RuZ78iEkanC8cTBCF8Eh_HprWz_IIHi_2-PIEvtYQNb9hxkouMjbcd8ZnyoGH8Iew_61wPG0kT4k7Pvj7QmEtNC9RmVQ662nuOrLM_LHttciXr3Lp_Xqa6SW2HiSiCNi5zMAQDVqAdT3dW7V-fsOt2xp9sbqBxQlCCL776uCYGFkPn_-3VebSf_fWpI5PXGr6T_s8WrESGboK_d3kR7w1GXbwtyj4on59z9tXrVmxQKHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RePJSH1Y-Gf6lSxnlrQ9UZkOAg6SOlWLHlxXy2AJQWe6maOo8hbV0sEcfwJMNpcpoy9-J7kg-Vci2ae2T35hZsm-n2F7xZCUxBJCS5LWdJT5csPXD0ZAYCcB3kAKxsgHbm3YbGbvfsMnzyLCKn6DdmLxoGpKShqCsaC2IUllSzW_cKcLS8oV1Ikv1pIYUnHJ9eni5YrqA28Whh7z6bq_Aq-nyFpzZSaeUyLW0bfhsmI_jxFF3Kf_jE96IBKd42oj0BR7Al8cINUAQa7PGpohcj1-KFMcyh8-M4Hixcv9Jvs9_9Upw65-_fjpsPv4N1yXBeuXHi2Pqsx-dLASAgZEZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=C1ZtoDPL_T8zLTh0vnPRkfQ4YS0jo6Ia4pVTG60NXuh5DfebslG4tzcM9T5ORLlJz2tWk6T_8nWe0DbsgX_iqdzTArE_7YttuSVxKzXWSI9wKnCvON8euzG7d1kc8T3hir4oD1l9P7NOaGGgwylQBW4TF5bVGaYV_98oWRS_A163C4Mvw-81W3NufY-XdSN-Oab3GML5CqY1HqTVDTe6ouaHLLMcIWmkeLVJ-qW1kdk0kBslRTRLUoRoD424IiS60FxkEdXvHNd9O6CsJxuoujcigMGU3p5cmJcJjRuEfV-_SWdJjiT0dz9XPcV0MlG4yYTOz3AV7Uu3sVRJi-wxtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=C1ZtoDPL_T8zLTh0vnPRkfQ4YS0jo6Ia4pVTG60NXuh5DfebslG4tzcM9T5ORLlJz2tWk6T_8nWe0DbsgX_iqdzTArE_7YttuSVxKzXWSI9wKnCvON8euzG7d1kc8T3hir4oD1l9P7NOaGGgwylQBW4TF5bVGaYV_98oWRS_A163C4Mvw-81W3NufY-XdSN-Oab3GML5CqY1HqTVDTe6ouaHLLMcIWmkeLVJ-qW1kdk0kBslRTRLUoRoD424IiS60FxkEdXvHNd9O6CsJxuoujcigMGU3p5cmJcJjRuEfV-_SWdJjiT0dz9XPcV0MlG4yYTOz3AV7Uu3sVRJi-wxtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=ZCWuYxBNcNJiNqgjIp-6gJVkfjZVJjOIEwbEfsLplZlsKuisu6HMvSbx8iSc8ie_sUe6B7-GESqTv0t5NUb1uPFu_z5o2JzVSq9CmnGzRMOJ11fCNzMJ6y89W4KcOwKYWuU02w9jrXD0wM15Cd6jyzwXLNv2QMrpGLWn6mSLfjwgGMroFAz69h_4U0cs0ZkdHv9fDUtdnQS_78wvliDeAJTHO63m5b4B8oeIuo0Wth8EuCd76lWQJ9fC9exSy5TN-G1A25MN5YzRlqsJN1vKi_ffXGsI6jcrRM40v_hEhK86VU-L_53FE9P0mkZYouw-5KBTKLeNpE5i6bZX570V7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=ZCWuYxBNcNJiNqgjIp-6gJVkfjZVJjOIEwbEfsLplZlsKuisu6HMvSbx8iSc8ie_sUe6B7-GESqTv0t5NUb1uPFu_z5o2JzVSq9CmnGzRMOJ11fCNzMJ6y89W4KcOwKYWuU02w9jrXD0wM15Cd6jyzwXLNv2QMrpGLWn6mSLfjwgGMroFAz69h_4U0cs0ZkdHv9fDUtdnQS_78wvliDeAJTHO63m5b4B8oeIuo0Wth8EuCd76lWQJ9fC9exSy5TN-G1A25MN5YzRlqsJN1vKi_ffXGsI6jcrRM40v_hEhK86VU-L_53FE9P0mkZYouw-5KBTKLeNpE5i6bZX570V7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyEvFBD5kaZLLa3JWyR7BUi_mX4QScJIkUPTEbcXWX7A4iy3dJed_y2vrUhkArGUURFT4_DvBy6lh8SKy6G-1I6fu0z5PPT8DbwAY4IiJa_BafP9g_Dj3wFyjxm8wtrDu8Ctwbuf6jVkxnNm1WptaoUOH5h03c1OHY07A1VAfFHPq8pH_E-iersC68DvkCsrRCdBgz7JXDgjhKXmYkfR6ipoZLOFNA2gM4WFbPOBdP5CYbDhGH2w1ESiXJiueiFlodaRZbGhweuXNli78te6vIU3vBJRkiwTs9Jm-Aax0_NYtC6x8UzBolGhegLwZj-kTaO11o0QN75ZYFkSr1poFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=bfkqqDjh16BgXvYHZIvLP0y1lOgGHwFjpm_FrZu52QAMeMc-L16a4lr5khQlbdLjmZ2XzCaHI6Ja5nW1sJP5mrdB2FoQmuyNEnLm3_0W81pLNYXRFRZ5UC1K949JEFPampC5Kt6kM7e-G_FM8xl4Tf8IA4-ylmow442_xtMgX4Ud50NsR7KwDvpgdqHpr0GLZOTkOOhCw0_d8Q6TzxcxZCSnbV6-rddJGbSlndjUgWoQlgD8VFw6Ttz4abWVxMFADivdpIFvWYaQJMdBMMlJuhfHg5OO4IlgGC1Saxvj0wCw-LowSd0KJKrujcWSKy3HDYzJQhfI616oiP8zsol04Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=bfkqqDjh16BgXvYHZIvLP0y1lOgGHwFjpm_FrZu52QAMeMc-L16a4lr5khQlbdLjmZ2XzCaHI6Ja5nW1sJP5mrdB2FoQmuyNEnLm3_0W81pLNYXRFRZ5UC1K949JEFPampC5Kt6kM7e-G_FM8xl4Tf8IA4-ylmow442_xtMgX4Ud50NsR7KwDvpgdqHpr0GLZOTkOOhCw0_d8Q6TzxcxZCSnbV6-rddJGbSlndjUgWoQlgD8VFw6Ttz4abWVxMFADivdpIFvWYaQJMdBMMlJuhfHg5OO4IlgGC1Saxvj0wCw-LowSd0KJKrujcWSKy3HDYzJQhfI616oiP8zsol04Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=QMjZKxKP3wEvOeVr9voMFfY2YLXgwCc49Vyt6srCFQ5O6jr6bbScfvktLXcaWXWNM025eRZf-oqzmOVstUnz8_FlHLWBVEkMUk8lhIOPDHZvobTPpLZ0KYyPKyvXNjihtNvXRo0IPIPy9-97-XGEN8hhrSPVF4hROye-PLnU75GHJIMKGi2DBn6itiGUGzEbkTlYekFJ0tsGvlUZoLLPeUFzG195-B-_QrVpXfGxcdNT51VL05x_DX1NbvhvBQTjsPsMvXp5JRPBFE4ptc6ka_nv_6FXB6GCirtnLuI1Dqzcz8KJMl6G8CNdZWbOBwCMvb6xvEi39H1PRumEXLtSgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=QMjZKxKP3wEvOeVr9voMFfY2YLXgwCc49Vyt6srCFQ5O6jr6bbScfvktLXcaWXWNM025eRZf-oqzmOVstUnz8_FlHLWBVEkMUk8lhIOPDHZvobTPpLZ0KYyPKyvXNjihtNvXRo0IPIPy9-97-XGEN8hhrSPVF4hROye-PLnU75GHJIMKGi2DBn6itiGUGzEbkTlYekFJ0tsGvlUZoLLPeUFzG195-B-_QrVpXfGxcdNT51VL05x_DX1NbvhvBQTjsPsMvXp5JRPBFE4ptc6ka_nv_6FXB6GCirtnLuI1Dqzcz8KJMl6G8CNdZWbOBwCMvb6xvEi39H1PRumEXLtSgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=sKWTH-1zGys1GV0qC5fYod5eQ95F4FgTuVhx7UbMVcST_vTynfcJEWwVSREwSifK2sCYG1rmCKiMtvq5Km0MbzhNAAFwwGIMICUBX8YJOE_25ObD7WQ079A53eCZDGBf9CPJ2-qVt6KaOkhJ6K0Ik6HZXxAm8UX-bnSjWYUFaDk948RO8oSwiqSkFKufs5lEq8UkPYmj4d6GbJ76Z3pLGYfHlIb-ZO-TfGz8B9SV-eXANsdPm-YvCQiSblKvG7RyLvFWlp7ebFY8uYrP4tk4gdZnEhGL1MbddcnJBmLaaqJc-TDXC831y45pwu8IGS-RRfLDXlTLUsA6W_4uukSxAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=sKWTH-1zGys1GV0qC5fYod5eQ95F4FgTuVhx7UbMVcST_vTynfcJEWwVSREwSifK2sCYG1rmCKiMtvq5Km0MbzhNAAFwwGIMICUBX8YJOE_25ObD7WQ079A53eCZDGBf9CPJ2-qVt6KaOkhJ6K0Ik6HZXxAm8UX-bnSjWYUFaDk948RO8oSwiqSkFKufs5lEq8UkPYmj4d6GbJ76Z3pLGYfHlIb-ZO-TfGz8B9SV-eXANsdPm-YvCQiSblKvG7RyLvFWlp7ebFY8uYrP4tk4gdZnEhGL1MbddcnJBmLaaqJc-TDXC831y45pwu8IGS-RRfLDXlTLUsA6W_4uukSxAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnnT3B6a8gcRinHIuQsGIxrUqgpRcbLJsYuBnPJqDru8QQzaSxbClfxAP2hLcnxkw3c77AqXHI22orHHlBrBzA6BlpyVq-Hnns6_XSM6zgOh0iZtr9OnHwcvPXmmnbB5zw6tAb-sVWtCqMeePMkMHA9UUuUPcGGXKm_cvIhhXpcAO6mcRKUW_q18PHK9SthTYgHCaHvbSGCtJqo7bbqqjrPoFxke4zk9jmQdHbYwr6KrzEjhgx8VaO_yE6xCs-akVlDDidghD1KRWGdFHHQhxTYD-WdvnqOO1A9jhchzAJqcfHn8e-fLf5U5nvP2Z1yOYyv3scTTXl890Fp-RNtLGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=aSYHH90BRCNjFoFO4K3BjC6J6IEE0Q4q_u-LUrI_srZ_Ms-iAnHM-x0rYHQrjZO8EWV6notNv7dVfqjY_UvUIbQOK7QZ_EoAogjG4q-jL3noFxPjai9_NAX1Y4SOxRgw602MztxekEt-U44Yt1UdoyXLeXAkFco2QIoRCLP-tiAdw8VlwAKFx1VFJuaVQTvXunog0UkikUdKth3kRJPQidatDwLzTur_eV1cGqA1wyrHg8H4aEOZXBwBCcpb5eJ12HfcmUMRdL6DjqvFh8R2A5HIlE2d64Pb0EiwwMPKDW1gmt5TXVZ7uIuYzIZH5E2E9_QRCXGTf7aYOxIVTzm0wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=aSYHH90BRCNjFoFO4K3BjC6J6IEE0Q4q_u-LUrI_srZ_Ms-iAnHM-x0rYHQrjZO8EWV6notNv7dVfqjY_UvUIbQOK7QZ_EoAogjG4q-jL3noFxPjai9_NAX1Y4SOxRgw602MztxekEt-U44Yt1UdoyXLeXAkFco2QIoRCLP-tiAdw8VlwAKFx1VFJuaVQTvXunog0UkikUdKth3kRJPQidatDwLzTur_eV1cGqA1wyrHg8H4aEOZXBwBCcpb5eJ12HfcmUMRdL6DjqvFh8R2A5HIlE2d64Pb0EiwwMPKDW1gmt5TXVZ7uIuYzIZH5E2E9_QRCXGTf7aYOxIVTzm0wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNcDjMccux-xAN-6bQ2li_Py85wY1guNDsWtSKXPXI1HqJgT_fknkOOa-mCemeF9pgbEhNy2DFwCGoG51yKPbUFAURuckKX0QRrXToFWmegGeUd4kHvhJPyrPtfJuSapDKXZRrGRasUnFdtcHwavEMGCMXJZ768722FW_-I3s-24SNTD-fyvR23pet37N8KsTi9d02badOURqO9ASSMND1NnND4XodYO3ltXIbcvHlzxacBhRyR7uxQl6KKa9TXn3a_oUoOnNTtqBZ64cBMYuvcPYii1md1Z5b_0eoXSPQ6u-bceXKL1LiKV4lyjTTB7ZH8VoZtNWV8d1j5sFNA7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyT_ocnsPYHs7IgWKKRHEA-9zVG-q-qCiwoLs07MFrVMzw3PbCu9cmdkIr4DtrR-TqyPAh55wG6GcPM_ojaQdqPEsQE5c4Q0qhYLIj81dzQy-Xo2B2lVjjKQ7VkWnZFUtI3LdBssq83nMue2VFoxZ09e7WHiXMo2ppKfckEmaqz3MUUUwi2MIWo0CPYnQOUtO-rkB6GMew76k1_GMW2mtQng0IwZzdYjUxNVHmmafO4eTrwM78Ph5Svwq9Afu2kayEXnTsy5OG6R9ZjhNMEBw1FSZiGDO4kqYmeWpUWRVSTYAcXrnCrxaGZfXdCE69I2M3mCkwfTJA7F6zYBw1uHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=tS8lEn9XSG2x37b74TcM-Ig9rqyMP85x77J8GfNmPchCjZfSfiP5hJH8D9KD57kaqhS5If_yClo6POODoN1wsu4QFVX-XsYmVOUrg-e3VbDPLmvdA3mXyz9IAl_SFIbnu75boQ7eVbblZunevz_CDIEZwD0c-S_tEGUwxMZVy1rWCTft_ySZBJlCprEHJPgI4XEYbrSYGlnIBbLlAcq1uGnWp-dNubAbZlh-rHGLSgtdV7-1KKtR4TnpLx72dOEnhEgxVOLQgFWTcubObxYCA2eH5zg5Z6_unIsmtNPO4CSuS9pOTuSp_3MWBooDmKCHxLUvP9BjsHk-JBZ83T9mMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=tS8lEn9XSG2x37b74TcM-Ig9rqyMP85x77J8GfNmPchCjZfSfiP5hJH8D9KD57kaqhS5If_yClo6POODoN1wsu4QFVX-XsYmVOUrg-e3VbDPLmvdA3mXyz9IAl_SFIbnu75boQ7eVbblZunevz_CDIEZwD0c-S_tEGUwxMZVy1rWCTft_ySZBJlCprEHJPgI4XEYbrSYGlnIBbLlAcq1uGnWp-dNubAbZlh-rHGLSgtdV7-1KKtR4TnpLx72dOEnhEgxVOLQgFWTcubObxYCA2eH5zg5Z6_unIsmtNPO4CSuS9pOTuSp_3MWBooDmKCHxLUvP9BjsHk-JBZ83T9mMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0pPPnLUqzD1R5oiz2TdnxlKQK21pa1NUtPQy4XLYw4elHD35z37UdsD14R0QrHoOdIOm-omyuNrWqd32Q_LRJXQwA3a2gF5mP8HAnDrdWki4sltsSSuTS9MmKLzLEKbNR3oYOag17jvIQ_iR34oh1ZZSZwe93SNI4GKnJK_eWki3GXPEGOUkqjyTMJY98Nq6dIivIcKCiZayFb_KGqVP8mh6jSiD81QYOtIn6MjlDFQRy5_CAntb7dx05g86EPp1m1Tuc_O0RvsfrL01zkdmC0uFAX41Qr96354TulqDpxZ6sPgdSGYGt6hpw8PQp5cLBwnPwM_p_CHDQgzIKOEiUhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0pPPnLUqzD1R5oiz2TdnxlKQK21pa1NUtPQy4XLYw4elHD35z37UdsD14R0QrHoOdIOm-omyuNrWqd32Q_LRJXQwA3a2gF5mP8HAnDrdWki4sltsSSuTS9MmKLzLEKbNR3oYOag17jvIQ_iR34oh1ZZSZwe93SNI4GKnJK_eWki3GXPEGOUkqjyTMJY98Nq6dIivIcKCiZayFb_KGqVP8mh6jSiD81QYOtIn6MjlDFQRy5_CAntb7dx05g86EPp1m1Tuc_O0RvsfrL01zkdmC0uFAX41Qr96354TulqDpxZ6sPgdSGYGt6hpw8PQp5cLBwnPwM_p_CHDQgzIKOEiUhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=NvhbrGU-3CkI_g-wyH4545_TNBEw89iKYInuigErkJbBuHmbf91LPzThdyQHnDvM-F59CXuJBuvv2f7HafOJ2CsgEXac7dTQLjbTCwhWv3I_gaT8AaZyKl7xw67sGSVZSXFKDPhT7PBDyjqzmggA2okhTWaUxxCmni4B7mzL_MSemDUzKOgBXtgfMQdhlAPDYr_AzgPMHTQDxsnLpTNMK7pv_XBYHAOtKt2V1IZ2UQllKTndnv0WpEYKf6hNaQE24HGwrUTN-iLWLovcF2F3N9_qHWArfoRgT52B0sZWmifzd2bODAL6Ed3h7oOt6EJBvgVZpd5E9DdwvIEPVFHuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=NvhbrGU-3CkI_g-wyH4545_TNBEw89iKYInuigErkJbBuHmbf91LPzThdyQHnDvM-F59CXuJBuvv2f7HafOJ2CsgEXac7dTQLjbTCwhWv3I_gaT8AaZyKl7xw67sGSVZSXFKDPhT7PBDyjqzmggA2okhTWaUxxCmni4B7mzL_MSemDUzKOgBXtgfMQdhlAPDYr_AzgPMHTQDxsnLpTNMK7pv_XBYHAOtKt2V1IZ2UQllKTndnv0WpEYKf6hNaQE24HGwrUTN-iLWLovcF2F3N9_qHWArfoRgT52B0sZWmifzd2bODAL6Ed3h7oOt6EJBvgVZpd5E9DdwvIEPVFHuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTbHISPgY0XYbDMBKiaYSsHC0kp1oqEOenee-fp4nugRGoBkwRl5CvHsE-zmDpPEzBRp5CM74F0UNrygIfCw8NsG5yHb3oRER6dAgF8OpGJjqvz-_jfQx445wJ0ch4i3KdJlqK9FLlT8uDWxdI_uRqroR7LxGsXbYE-1CSImLbYgzij0TEF1xW7LgElI5V4DHnfDrXeUyte6yH2X1dNkIG3GVEnrFT9H3KTLDHEZFIykOaF7stKXhUlmrgSVpZtO-dWwmpEwdL3IBdAEsvtiIXLtDYLlMNuJ3hk_TPROjygFjDaPA7btvEx_WB05YQQ0HSHJDaXbzobKcjq7-L8q9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=S_aCpwbUM0ecS8aufBUIG2WEmtiruDn9uCpn0HGwOMsKIDNOZNfy13JDAwvm5s5WdLmsFSH_B_g7Oxk921WgvxBqPzXm3XTPeqEnhC-JGk-9GN6yswGY4xdh3asPLAJkjWXecAu3RTJwvRRfBkyQRaUE7KMP6w8kt5JzdAvYCQuqCMgGngScq-v0XShzHKzlWJaJry7NCoqFcqD0cwtZ14D7f97yo2IqXr5MtTyQKdTG94Yh5uz2IZyuIFRuniLgvnL5Wse-4MWlRazsuMSGmNls5iLRTTGAJNDlUuzMEZraIRFyiucpAIJc1akXL_sISWrQ6XdEo5kQMNA7RurgFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=S_aCpwbUM0ecS8aufBUIG2WEmtiruDn9uCpn0HGwOMsKIDNOZNfy13JDAwvm5s5WdLmsFSH_B_g7Oxk921WgvxBqPzXm3XTPeqEnhC-JGk-9GN6yswGY4xdh3asPLAJkjWXecAu3RTJwvRRfBkyQRaUE7KMP6w8kt5JzdAvYCQuqCMgGngScq-v0XShzHKzlWJaJry7NCoqFcqD0cwtZ14D7f97yo2IqXr5MtTyQKdTG94Yh5uz2IZyuIFRuniLgvnL5Wse-4MWlRazsuMSGmNls5iLRTTGAJNDlUuzMEZraIRFyiucpAIJc1akXL_sISWrQ6XdEo5kQMNA7RurgFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=VX_uE9GP8UMJyAMkvrMnK7Vn89g1cClR-VU7hm-DXhzk5gS86kuPqOXStj0CbTqRH5xU5OyxGWRUq9yOq5QQVEl10uRrAzkNfIGtaPL5XACjuWD-Xm2NHYJMuENTzW4aLF7AHlwH93szdVovaniXDBPsf332-xwqoQvqxQXjNMsA5vFzKel5mnTm8MZzaaA1J_n83JqkVQ94UDLbHITBgKfnZNS3Mp2mfYO70OcwSnV6VDGs9l-mrQN6YhbU2W02NP3JSDI5dhsZJj0hDJSarnHjre-3t9j7oMYRi89k95C8QGrQAGpe4PmoMgxDv2WSZeg6j4ifon0A_7Uy-ypCVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=VX_uE9GP8UMJyAMkvrMnK7Vn89g1cClR-VU7hm-DXhzk5gS86kuPqOXStj0CbTqRH5xU5OyxGWRUq9yOq5QQVEl10uRrAzkNfIGtaPL5XACjuWD-Xm2NHYJMuENTzW4aLF7AHlwH93szdVovaniXDBPsf332-xwqoQvqxQXjNMsA5vFzKel5mnTm8MZzaaA1J_n83JqkVQ94UDLbHITBgKfnZNS3Mp2mfYO70OcwSnV6VDGs9l-mrQN6YhbU2W02NP3JSDI5dhsZJj0hDJSarnHjre-3t9j7oMYRi89k95C8QGrQAGpe4PmoMgxDv2WSZeg6j4ifon0A_7Uy-ypCVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Jpn3GLLOCNveLIvE14PP2HvOK4Stg4zj9RKYmUgGudp2dsKrvDNSm3Xyb4BAi8TU4AOVuu-BUA48s0Mtop_Fgdr9np5GSO0IwYWEbSXE38K1JoIGrQ2eIuY3lfyE0byvtAUHEvdsN2YcMauhEDt4KjLRj4DjXcphP2YHXmmbcro_xYGX21hR_9wqTgadLQFef1QnEhPdJ1zd5BRuga4QomMANNpa97LmafJMmVlUQscbkIOBxyTAJgwtA-WtPAvpBQEdAvKiYS-Ise_SzuuEwo3FajxPZEcxV3vGH1ZlIah8DBP9maqt_ScXQhXYo62OyQQdkyfW5ohr5MBBcfW0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Jpn3GLLOCNveLIvE14PP2HvOK4Stg4zj9RKYmUgGudp2dsKrvDNSm3Xyb4BAi8TU4AOVuu-BUA48s0Mtop_Fgdr9np5GSO0IwYWEbSXE38K1JoIGrQ2eIuY3lfyE0byvtAUHEvdsN2YcMauhEDt4KjLRj4DjXcphP2YHXmmbcro_xYGX21hR_9wqTgadLQFef1QnEhPdJ1zd5BRuga4QomMANNpa97LmafJMmVlUQscbkIOBxyTAJgwtA-WtPAvpBQEdAvKiYS-Ise_SzuuEwo3FajxPZEcxV3vGH1ZlIah8DBP9maqt_ScXQhXYo62OyQQdkyfW5ohr5MBBcfW0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YmtqiDsNVA1FPPzuwaaDVmIV6Jl65QaZMCfERiPg6rwPQDOmzAlHjucuKz_tTBtOW3_HLVv9c5Z8wCTZoarx2fLhbZN3gZ4MAc2CsJlqyED97b4L4ZCTjz2yxvu-lZeU-_izBgdh7Qi-eWzZZg3Elhzzx9Xy-R3yNBM6r317FLiAAGGMgOTnI9JaPF0MtRHRttb-Uzau_PrTHfIt7uDPCPOqZ5cYL1Nsflq666q-5Muxn-uup6QKxaZkqzc93obC22Ud0PRrXWEEkycu5PL7tGKPvHgpGESAk385HfWFyG413-0vyRIA_zURpmmpmoBovWLvMSK0kOL4q1Pttin0Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YmtqiDsNVA1FPPzuwaaDVmIV6Jl65QaZMCfERiPg6rwPQDOmzAlHjucuKz_tTBtOW3_HLVv9c5Z8wCTZoarx2fLhbZN3gZ4MAc2CsJlqyED97b4L4ZCTjz2yxvu-lZeU-_izBgdh7Qi-eWzZZg3Elhzzx9Xy-R3yNBM6r317FLiAAGGMgOTnI9JaPF0MtRHRttb-Uzau_PrTHfIt7uDPCPOqZ5cYL1Nsflq666q-5Muxn-uup6QKxaZkqzc93obC22Ud0PRrXWEEkycu5PL7tGKPvHgpGESAk385HfWFyG413-0vyRIA_zURpmmpmoBovWLvMSK0kOL4q1Pttin0Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eum7lJvJfacMtsHrsgTaG8eazCrTE8t5PvYgASD8MotF9FGirdTDcmEjIxEC2bjK9VT_wKjbZqSdIletUu81xCx5fU9QCZ0-UiylDs617Tg_WqI1Vn_rRTZdIQwMMIC4uinKWykwnn3HYkI-4KLGeHwWzbz_7QyJbEVWyvu5rab3BIGgd-XD9eA7ZAUCrFhkeSDHDx4qJYCj9DOIS0vskb1kQBz8d42DFJ2FyrymGrV_GEvVo3gvsl-cLtVFYhjmKHXnE_-T4C37LKT-EYmmDeT7qgugyaHgBdMrbw5oi6yy8yNXtmeLnyEmMtvCanGsEjTno7MNSEpdIo8fg-ogXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=OpH-dLe2-1NMqAVlRS9HuDCUO9F1PCKUjTnrbDuX9uEorUA7q43AaRj55AX92YY8kZCad1jCcrtrKR8aAqnx9sAUXjry1zcWeScc_fD0ZfufSsoBR4XktCRbm305NvyrkLgK9Qi0gZW-qTdagL8nZP-wQ1Gp0cdLyBf25LCkTSA7E4dhppXCDpQEsVnI14MvAtxsbio3xihEJm_PpChQHyIIwOrjZx-8YSoZ9o8bHEtdb0uaiuPf_YIbdMZ4CXJf_LOnxj7_bJnNq__Zx6zDN0yRj8DzgDFItOAF0qZd97mhPZ-7S0xRFnP0OsxqTH-jaIdusppUNb15Lg-TCgWr4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=OpH-dLe2-1NMqAVlRS9HuDCUO9F1PCKUjTnrbDuX9uEorUA7q43AaRj55AX92YY8kZCad1jCcrtrKR8aAqnx9sAUXjry1zcWeScc_fD0ZfufSsoBR4XktCRbm305NvyrkLgK9Qi0gZW-qTdagL8nZP-wQ1Gp0cdLyBf25LCkTSA7E4dhppXCDpQEsVnI14MvAtxsbio3xihEJm_PpChQHyIIwOrjZx-8YSoZ9o8bHEtdb0uaiuPf_YIbdMZ4CXJf_LOnxj7_bJnNq__Zx6zDN0yRj8DzgDFItOAF0qZd97mhPZ-7S0xRFnP0OsxqTH-jaIdusppUNb15Lg-TCgWr4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=Qz2A7psJASJC64eFcgYzuD6eD5AqD8dFjWGS_OLqwglts_HtWldTBM3VzWYcUmYaG0Jn1cQIrHDrO475bERBAD23wzI23g1C5GHgLIACudSEhapuX4xr3wLCoau_nYjTfG_AQAXGEkrPQv0tBPy6IWQz080nMM5_srB86N6H8u9-ktMkHM8QEkp8M6MIs6QiZBHgu-rumSABEa4gFSQr-zj_B1QmLe3Gy8cDraMCEyCt2_9nx6j8V5AB_74oAfleMYu7dUVvt5eIPf4WYZk6ZGDyp-RhzGMhizQSM7t6VtQ_lJmQzSeeyCtemKacKyWRCp5CV7CFQgSTuZ1x-PJPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=Qz2A7psJASJC64eFcgYzuD6eD5AqD8dFjWGS_OLqwglts_HtWldTBM3VzWYcUmYaG0Jn1cQIrHDrO475bERBAD23wzI23g1C5GHgLIACudSEhapuX4xr3wLCoau_nYjTfG_AQAXGEkrPQv0tBPy6IWQz080nMM5_srB86N6H8u9-ktMkHM8QEkp8M6MIs6QiZBHgu-rumSABEa4gFSQr-zj_B1QmLe3Gy8cDraMCEyCt2_9nx6j8V5AB_74oAfleMYu7dUVvt5eIPf4WYZk6ZGDyp-RhzGMhizQSM7t6VtQ_lJmQzSeeyCtemKacKyWRCp5CV7CFQgSTuZ1x-PJPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb2Ydfk7uVUgsTQA1gCImb-eyi93o5lrGeak0NAY6z21Yl4KOP3horDa-Sf010mLFiJaWHSXdVEjvRkIjCJ-IyU2j7GT2NMDOB39vy-63D1RzCz9pRj57M4HR622xjEFGmL2kxbLInxtsUV8lKS-7EoMCh8KVsQGoxe8QV_vQ_vtyajFjS3K4veQmox4bqwXCXeLJxPJuu2FYvTxBtKgtcxM_hLRd0sBvvEoVhiFRvC606FA1IzuqSksQff61WIqZ_rH46d1GVo7yoUv1IqdRCMlv-braK1KSGGiDRC09DawSkg0iXoVnsFYhNUewsQGC4LEyKSPPBpQMas-8qg2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vNNyv7dg2Lx5fgq-qj0JX34Abhby1zemfmrxbHiIDil7ZuVUQqV9-iDlPZvd6HhyEh0wasWNMQPQOo-kvdfhhQL9t_3zzljIjmEHqZmqye6Jn9z2oYlU-UK8czWXrI9sZqJ71JhTrzN-yHa4UlvSY49XWzZjiZJDAQJ880eslBJE7SNWVYRQO5_KhLP8m9hesng6M3AzXmkxOXgEUNm7yZrJ3OLoD8wv_nHvbKpCXUMRDoq-_ot4vrzeJ2UmlS81qLv2NJ-jYTuQxisPVoCdimFGCl2x5VQzZYuT_X516bo_u5cRarjHa6UMsp3WuXMyOvBemuAOWrhQge-3yOyfgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=vNNyv7dg2Lx5fgq-qj0JX34Abhby1zemfmrxbHiIDil7ZuVUQqV9-iDlPZvd6HhyEh0wasWNMQPQOo-kvdfhhQL9t_3zzljIjmEHqZmqye6Jn9z2oYlU-UK8czWXrI9sZqJ71JhTrzN-yHa4UlvSY49XWzZjiZJDAQJ880eslBJE7SNWVYRQO5_KhLP8m9hesng6M3AzXmkxOXgEUNm7yZrJ3OLoD8wv_nHvbKpCXUMRDoq-_ot4vrzeJ2UmlS81qLv2NJ-jYTuQxisPVoCdimFGCl2x5VQzZYuT_X516bo_u5cRarjHa6UMsp3WuXMyOvBemuAOWrhQge-3yOyfgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=HsqHyp4JNsopiP2-Cq7DkKU8GId0h7yc3pwIOxHr_3vAXZuKylRtPW8KUfz1nVMLGKLx8jO7W0QN1vQZi0lh9sF7QZCXWbZ488aC_HvkLcwDwpF1MjGYfwr56xgZPv8PtO96fb01W0SuFhVKxpHIL4TwkgdVB95clYxp8aRdXGwkpu9rRK7rspd1cm4e4j5l5jsoeoNKK7q8WwnWgYogcX3X2oWnyR1WVjME78Aac8Qfwuhc6QzuNtFJQqZqaJB3IFFclUhiD8kJog-_KJGdiAymJfXbjwCG6rBn_g3yzgKGYPnfV6a9wXHfLVT25-VcjVcQ7UJ_LqZhbESJ3RPjew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=HsqHyp4JNsopiP2-Cq7DkKU8GId0h7yc3pwIOxHr_3vAXZuKylRtPW8KUfz1nVMLGKLx8jO7W0QN1vQZi0lh9sF7QZCXWbZ488aC_HvkLcwDwpF1MjGYfwr56xgZPv8PtO96fb01W0SuFhVKxpHIL4TwkgdVB95clYxp8aRdXGwkpu9rRK7rspd1cm4e4j5l5jsoeoNKK7q8WwnWgYogcX3X2oWnyR1WVjME78Aac8Qfwuhc6QzuNtFJQqZqaJB3IFFclUhiD8kJog-_KJGdiAymJfXbjwCG6rBn_g3yzgKGYPnfV6a9wXHfLVT25-VcjVcQ7UJ_LqZhbESJ3RPjew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Cbsqu_A05CEHO7lMc5B8bjG9woe4ywOw6HawLtZ3WVs-B665LNdnN1XWOn6Q8uf6X53yO9nAe05uaQcsJ0eYfvwtGvA7cgSYHQqthABccMKOOJmaaosA914UvddbLb5Sxo4aaEdCdCylN3YTFqiwWGsr1pZsAz1VmGCt6kQm-f1YAMSj4wGUU0L4W4FzelqRL3CByFdzNnCVAFT0RWz2W9rsWDer1i7uyp0pBd7LE9jRcpGElS_WrIVyDTi3G4uzaEp6b-KGImvWngmOB8DYcinTOIMIZHKrmXYIY79oc_KWH5YXKvlf00bqdtCj_xsvvnTPzIw3yRoGvE-ybgtoIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Cbsqu_A05CEHO7lMc5B8bjG9woe4ywOw6HawLtZ3WVs-B665LNdnN1XWOn6Q8uf6X53yO9nAe05uaQcsJ0eYfvwtGvA7cgSYHQqthABccMKOOJmaaosA914UvddbLb5Sxo4aaEdCdCylN3YTFqiwWGsr1pZsAz1VmGCt6kQm-f1YAMSj4wGUU0L4W4FzelqRL3CByFdzNnCVAFT0RWz2W9rsWDer1i7uyp0pBd7LE9jRcpGElS_WrIVyDTi3G4uzaEp6b-KGImvWngmOB8DYcinTOIMIZHKrmXYIY79oc_KWH5YXKvlf00bqdtCj_xsvvnTPzIw3yRoGvE-ybgtoIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEuZ1FsncLqH4OaK2TvU3uRvjVHO4WwVDf6Q4z8j_9ysq5P-3pRPtzuw9jAj9uG2MCYvNU58u74_1z7Mpl5IpsIg9Om-uTegNvxD2TFfEVNGKEZUS1SPyWpd1qy4JqRv13nm9buB1nAaJqbKRYZhbl18u_jvW8TVgJfTHfnUKcX3CulGEVzq441Giz4k_Q2uDXENlj13xex4AYF3OyPMFU3JSuyH2uB5BxAKaVJ00FRyPRRt2nIcBOTRPWm6zR2i5zPg3l9jeedAsuYg3xOuU4rQW9j0wnFFb7ntTPHVjAuGqwNpVKfwPdoqJWeIA0vwjR86qnmb-y2VwqL-AMXXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAhFE5YSJfv8ozX78BaMyfLjrUR84HpyEO4UqN_JjreuqegDptOxCvo1srEpIcPxp_TF75NQU9WYJhFSddA5mxwM-2KucHm5SKcB9l3vXPhjJPfymVKH1wIa03D9kXrcLdBtZBVamKApuDbbHbW90idpFaQ3hHRXbVtoc0hB1T9nTjfzP_hU75BZWlttbaMkvAR8obMQjafxfaHR3g0038TErRV17H4pzwE8MgyLvGOunFhvN2iQifaxYrquG0X52EVeQvll71LLiRqwJuDXCaU6JHUdBOv9NINMbZdL0xiKxtzb7xs5MtkSuegFg7ejHe91ZWmF9m-_FxoKZSluqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXilak2J36k81Wasn-nl6eK4ns6h_HE8Fz284sJjXqy1niMXEjvkRHQPHl8wk1u3yuh003TrhTtN3n_i889Sfmsv9a67WxpCAvci7tXe6FpD1nTBWQGGiQmtSgy0UTknes3eSnW1OLf8f1PjYYKarmMeP7eF9lhe0VePvwIO6Yen9DB5KqvFR8571aqEKoEfBcxaoChtxuKi9ahCgVatlYkPTl072FNSuqYQPplQmGb9-8hlJe4z8nF-tJeTeijj1lFCgtuHSLdkoQvq9NciiGYTZQy_GZafipUlRPBlaKxSCx50RlVC-KBDuQJF0nOleM6rSV5Q472NossuG6UVqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=DsmSXzHuAGih4KGdADap5M_3f_F2hfoXtK_n110dcPN6oI_hOB6gvsAMUK9b1JRVAHVOlnQLdt-jSNvC0o_6SRyN5yqqMZxED1VVQsMDq80JiqCBVCK7pU7NA56qrLxOMMZIh5LwitiUYU5uSfEgGUJB8i99ZC4TwlMed9Gjsxoj7WqD8LawT3qrXgcxmQxMckC8jE96xEQGZ4wFKlBy00W7zBk8Mm4EceLxEFacPqUGma0jntYE9j-CMnBATWVl42Z9ed74WO0h2BEM66qFgxYSWM5WWiXjehp2NajZPCVqdFgPn2ZwntjOcMeXSCnk8F5xeZD4_GcKlbXNYo9htw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=DsmSXzHuAGih4KGdADap5M_3f_F2hfoXtK_n110dcPN6oI_hOB6gvsAMUK9b1JRVAHVOlnQLdt-jSNvC0o_6SRyN5yqqMZxED1VVQsMDq80JiqCBVCK7pU7NA56qrLxOMMZIh5LwitiUYU5uSfEgGUJB8i99ZC4TwlMed9Gjsxoj7WqD8LawT3qrXgcxmQxMckC8jE96xEQGZ4wFKlBy00W7zBk8Mm4EceLxEFacPqUGma0jntYE9j-CMnBATWVl42Z9ed74WO0h2BEM66qFgxYSWM5WWiXjehp2NajZPCVqdFgPn2ZwntjOcMeXSCnk8F5xeZD4_GcKlbXNYo9htw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZiJmhvXIXfY4ytDHHp6NSAZT2E6mlIRmggO9NUc0GHpDwy1xeWbgHVR_vlnFp5qHJCh62HfqdAXO_uPj5rNtikYiSxzR-tlZ7i2d_64z0Z8CijrwlQeTfsItZ6qTs3qpRfFGM5obFY3Mg35J9h5i1jz6g30u2RsrM1L9GcmD-lQqsSWaS2nrmllvBSYQVaRkZBJkRRkKeDyhv4HleA7UgLRtnHxWaPSTDcaaNqVcig52uadz4QQwHmDL1UhmiIcEtBzmn2Sp0xvGHtp6n36t7vko6l00FbyvrexzZQJvjX9Im9C0WPfVyH2NtNvEOU2Vz7GJX0YOaYx7ttBKdEEhPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZiJmhvXIXfY4ytDHHp6NSAZT2E6mlIRmggO9NUc0GHpDwy1xeWbgHVR_vlnFp5qHJCh62HfqdAXO_uPj5rNtikYiSxzR-tlZ7i2d_64z0Z8CijrwlQeTfsItZ6qTs3qpRfFGM5obFY3Mg35J9h5i1jz6g30u2RsrM1L9GcmD-lQqsSWaS2nrmllvBSYQVaRkZBJkRRkKeDyhv4HleA7UgLRtnHxWaPSTDcaaNqVcig52uadz4QQwHmDL1UhmiIcEtBzmn2Sp0xvGHtp6n36t7vko6l00FbyvrexzZQJvjX9Im9C0WPfVyH2NtNvEOU2Vz7GJX0YOaYx7ttBKdEEhPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=RIJyFyCGLHbpSUFKt-QWTcOuWFrLLYPnlzUzyD4Gx0m8VMc26edXDySl0ra7IduAhrRyVqgVDoi6I_q-PiGh7nEH3W0Ik-CFOeHGSMy8gnUvLrdvgUhXVjl4feg-0gZFltiDViL_QL2zBKqw84IsRbEjwBzHGn8v3qP6UtGWI_DeXnzKDaur9q5cOFmI2zBMoLMQuyjdQEu7he0YST1Dt6AYqXELnwJpnNFitUb61BJq7_9wat8M27VvuaF5OxA9qEei01Msv9pirJv15EK2JspAFJ8E9qu_zr-gYtXW-DVheRK552OmXu90COhslEjHKkMaZQnBEr9o8B2MHCnSTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=RIJyFyCGLHbpSUFKt-QWTcOuWFrLLYPnlzUzyD4Gx0m8VMc26edXDySl0ra7IduAhrRyVqgVDoi6I_q-PiGh7nEH3W0Ik-CFOeHGSMy8gnUvLrdvgUhXVjl4feg-0gZFltiDViL_QL2zBKqw84IsRbEjwBzHGn8v3qP6UtGWI_DeXnzKDaur9q5cOFmI2zBMoLMQuyjdQEu7he0YST1Dt6AYqXELnwJpnNFitUb61BJq7_9wat8M27VvuaF5OxA9qEei01Msv9pirJv15EK2JspAFJ8E9qu_zr-gYtXW-DVheRK552OmXu90COhslEjHKkMaZQnBEr9o8B2MHCnSTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo_QljV4397JRlmIhD-zZW74O-dNx_J33IgRJtrxgv37Tfd58ucYKefKeCr5DlsZSIPFZ2EngnAENfc_xuEBPMZFzIqPhr-Jp73A8a02Y2JnMyFyY2WlCuIdxzXaCUyn29dKkpecY684gn9B8ng3_D5V1OzY-xTn1xq6B6KEXUYYAkD7WGTUiO4RzFY749OVg6acx0Mg-6AZ_dmrCeoaGFo8K-6UbDgFyNPtFj527kKeHRnNuvJeWG57LORjY71dEyjryu5eYfmavkBk5uHtj-YdZE_mYSP_RlxyBUqocZfR5blsf6uqu9uNVgb8MINpT41CqqB0oRCicq0MesMjDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=gg8eNIRMAYNLmaipkaPrT-DSaKMmOXK0dvMBI07IF8b5H_KjxOONpcaGwYzbyAAMndbTu6NVqz8TDWPxKzSNiE5LjNYjbVh1MGHVfitGddSaswZdSE9PQn-jwNlGD1TxGGdGqHXNNdY1YsPI9dzi-A84MoxZx55MVqeyr8ZH_8m1W6ZTG57GYAe61MkslOz_AJQBJj1OmWIJppOqjpmTrVogwtMXpnQq5aABrS9J2xdCiOiBhKtQO6WNLAO6l4tJeNBLGnMYuuRdliKhhGpli-FdEErazupAH_qr8i2eR8Noh46QHb7luIOVWyEdhl6Limue1g9kMUcixdp0NvHdaYi_Fz_KN3bKwngQWFQgkvYgOeowjEcSKrP5kczRIDtZ62hWwSOI9N2SSd-z5VuZFzG-BaC9de7DWK0KK6aDirPbg8F7Mw9xSFNEXJoqWYqUlBbtlRkxrWN5NI4PH1GsW3La3k21iqMhgRh_JZQV4pp3uliRJ0fELetDQI5Po8gWWDD1NTAezAL2YUeNbiGUwsUMqgPQgrCTsqHzCW5vmOWIWU98O_CUvfm5T0WL6wXj-QTwbqElOoTequ0rrncDcoArUGUr4ujAux7SAhqaZMTjOh2PG9sHhyGHUSKCtswAthQXZGutPDbefWXLyEykxC-_3h9GNNoJfoCStYQCW08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=gg8eNIRMAYNLmaipkaPrT-DSaKMmOXK0dvMBI07IF8b5H_KjxOONpcaGwYzbyAAMndbTu6NVqz8TDWPxKzSNiE5LjNYjbVh1MGHVfitGddSaswZdSE9PQn-jwNlGD1TxGGdGqHXNNdY1YsPI9dzi-A84MoxZx55MVqeyr8ZH_8m1W6ZTG57GYAe61MkslOz_AJQBJj1OmWIJppOqjpmTrVogwtMXpnQq5aABrS9J2xdCiOiBhKtQO6WNLAO6l4tJeNBLGnMYuuRdliKhhGpli-FdEErazupAH_qr8i2eR8Noh46QHb7luIOVWyEdhl6Limue1g9kMUcixdp0NvHdaYi_Fz_KN3bKwngQWFQgkvYgOeowjEcSKrP5kczRIDtZ62hWwSOI9N2SSd-z5VuZFzG-BaC9de7DWK0KK6aDirPbg8F7Mw9xSFNEXJoqWYqUlBbtlRkxrWN5NI4PH1GsW3La3k21iqMhgRh_JZQV4pp3uliRJ0fELetDQI5Po8gWWDD1NTAezAL2YUeNbiGUwsUMqgPQgrCTsqHzCW5vmOWIWU98O_CUvfm5T0WL6wXj-QTwbqElOoTequ0rrncDcoArUGUr4ujAux7SAhqaZMTjOh2PG9sHhyGHUSKCtswAthQXZGutPDbefWXLyEykxC-_3h9GNNoJfoCStYQCW08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfUCB-r11-WVGzdnQJaoVVkst20ZanAs9ANczqBgGWwJFVUyujcOxzrGxNHkesbx913SPSgUNCQBqXtvxh1n5k_NIOetjTlsuOSxCnKYN-wdsENl-SrVUIq-FCuqxRnVDqasLEfhXJDl-FAAatAomp4iyeQC01ZflTGmG8ZEGZTi2ZRLD-saOwBpktZOVu9LqT8wdGmhNNKN5-5zSXNPkh-mN2J0Q9qzkkGnG_SachFPxVpmARRWW0NN1qLTjFkELFmYXUwp1VbsyE1pltzd0r1eaYi67mPNa1RsGex4_Zzrjm9Xyk5FXs7Uvva_G8LhzSXd__uIgy_3WaSH_WcoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=fCCnpdVa2XiDpwPy65IynwHoJZCeAiJr3_sva7hPhV63KVv0eR9HSYbtD3Cqk2iA3V0d_q48UD4c8XsyS2lpp8OSIY8qx8dUDZYnxu8kjkIfUKVaaEU_tTNRktpUYCz7-PqurlvBVFNEtjlCgDvxde5BNjw3lfwl8RhOVWg4HWOF-h1e3cAwQrrwaNfcxwEMfhAQuCPVqqU6x1Zj9z8tV1HSIdlaUxcc6CHrhL3SflyneDQfprvB9V9WnnjqoEQZ6fHe-evt9zBfGqxwl543JT2AECL5AI22fq_BCZLJtyR_8OdBMRJ9QOgJVH_FXXpGpn9q6R3j_A8tDYOLrWno3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=fCCnpdVa2XiDpwPy65IynwHoJZCeAiJr3_sva7hPhV63KVv0eR9HSYbtD3Cqk2iA3V0d_q48UD4c8XsyS2lpp8OSIY8qx8dUDZYnxu8kjkIfUKVaaEU_tTNRktpUYCz7-PqurlvBVFNEtjlCgDvxde5BNjw3lfwl8RhOVWg4HWOF-h1e3cAwQrrwaNfcxwEMfhAQuCPVqqU6x1Zj9z8tV1HSIdlaUxcc6CHrhL3SflyneDQfprvB9V9WnnjqoEQZ6fHe-evt9zBfGqxwl543JT2AECL5AI22fq_BCZLJtyR_8OdBMRJ9QOgJVH_FXXpGpn9q6R3j_A8tDYOLrWno3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=R8SOlWT-oVBGJaJyXsTnQDNpt1G91KgkBloogUFOTBo2QrNDpAZEBrH1bknoTesoriydTtFhLS4ydf3KsSOV-_RJPd2vgJHAvYm9ruNDlnAKMpa2f1_2-KlF5LgBZlncg5b84KvZakARGS84yJY2wI2pXANxPmTCjaJstIV9I81wb65MPbzxYoxQPiFbPZgfDkoBT0YCUt0If0t33kThlx4rioLvTZwBJU8FNrbvo9xDyGJaH4H2Xdl1f4cnAe5Dao6RWGWVZWX8iw1rNP4LhOB7aCKkXSf_-z9qEZydkbiIuLapNDtcrZ-8HYaRfznl2GKhwmAMN-gY1PTcA_z8-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=R8SOlWT-oVBGJaJyXsTnQDNpt1G91KgkBloogUFOTBo2QrNDpAZEBrH1bknoTesoriydTtFhLS4ydf3KsSOV-_RJPd2vgJHAvYm9ruNDlnAKMpa2f1_2-KlF5LgBZlncg5b84KvZakARGS84yJY2wI2pXANxPmTCjaJstIV9I81wb65MPbzxYoxQPiFbPZgfDkoBT0YCUt0If0t33kThlx4rioLvTZwBJU8FNrbvo9xDyGJaH4H2Xdl1f4cnAe5Dao6RWGWVZWX8iw1rNP4LhOB7aCKkXSf_-z9qEZydkbiIuLapNDtcrZ-8HYaRfznl2GKhwmAMN-gY1PTcA_z8-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=aI3gtJaeGfDmo-wlVl4L7HSVOzE3zJ2l8i0afHY3SvWd7VMCP5lVh0ziGhtsDC9TFS78xW-FHfWblwHqM7RFj_sR24YJ6K381dzGFtq2xs9E48uGDtCN4GgFr1mlo5nkGaJMi953RLgPOM0lK6INV9IGbfyQZR8K_t_4G7GCZtXZ7cGjQtL-X6jqqJcRlmudCkTr2849D5ChxZ9gczhHkKTlpytGRMEBqH_lBTlFEEH2W7f2wBH8Cax1jOdZTNL0Bxjo4XNDdIsbjYZJxtwNbKhqzzjkXIfYitdaD2kDQ-3gGoR1dS0UX8VsKD0-v1_aXuJjArDHYbLREk0cFKID-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=aI3gtJaeGfDmo-wlVl4L7HSVOzE3zJ2l8i0afHY3SvWd7VMCP5lVh0ziGhtsDC9TFS78xW-FHfWblwHqM7RFj_sR24YJ6K381dzGFtq2xs9E48uGDtCN4GgFr1mlo5nkGaJMi953RLgPOM0lK6INV9IGbfyQZR8K_t_4G7GCZtXZ7cGjQtL-X6jqqJcRlmudCkTr2849D5ChxZ9gczhHkKTlpytGRMEBqH_lBTlFEEH2W7f2wBH8Cax1jOdZTNL0Bxjo4XNDdIsbjYZJxtwNbKhqzzjkXIfYitdaD2kDQ-3gGoR1dS0UX8VsKD0-v1_aXuJjArDHYbLREk0cFKID-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3Qgk9evqIxmpGbsiR4qdmnp4WYeKInxqHGjG_fiovfklWnq6G4Y3IHkZ2XFSfYqKaOwGNJqZ8fL_EtluP2gHddOW5McM6CrvyPTvI1KfBJ_xgWjiomxSFV0fKf3ADfCvFU--hBDaUSLJ04XxYb9TehJzlq9PGUwwjSF0iInJn02qUwsJ2-LUuRFojDGI6P3ZX8VwsMqgkZUcbNb71ylA7HRtQpCdAhqOKxUopv1oTazUwxKbgNTyl8UPPr0oooHXmpeh8KONS-iIMcE_uv1p9JOovjOgRlaMvPTY9lLV64irrcvevGod8s0QEIpxzJr9R0X-GRW8tEeGtNKMSn01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAhS5KE2OzDKSlWAyCnIfO_dCm025Rql8gT9g1IwPfscrHpCeKYxLP6qJ3DPGTXRF_7FALe_9UNn7aYj2VpDak3Bbhasb28PYqII1DYufs6GlfqElo1zwioyCisPH-n6fZWrJONb6vXofBJsZyQAXLByIT0H-xLTgwS2LPQDbuYPs7bpVngMFGQPkMDAEz3t_navdxDysj2YaKccRX5wVUMoXsF7ngTnjmlqerRhxg4ESOl8Gpacazcn-KVbVSTdodcxJFeqZw9hI5EAAr49bQ79deN2g8wWKTX6GN6ZLEeQSbhs5rnjxIyGa9XEt6qJ_RfNyD0TaVy9j3oZvjYnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=puWsaEpt3mjTnWmdcqY-aIOOH_roMWJnNFFrMSaHki4gehYzX0qEnhLYpGox1T-wWkw3wYD4jPao8D_c59DyQ876p45c6NVvQOgx2cQRrLJsucC7SXKk8dZb4ntjBWJJT4b1sTAH0MXf7T29NivU8l5B79YeMPgnBToEFcVdrA_Cxg6DJpFk8An4vhNHd-s7L3bOENnjL69GoQgWN7euGtka8Bt-UX3eiNlfLnohnZe8S7c1CRp_53DnHgvt0kD0yUAuyItGCu-YukArIBFOOjqyq6Zox4x9F4gPaCpe9q1eE38Uxb4glXdc4OkXOgeXKnE7xMs5X8VdsPY0w8v4yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=puWsaEpt3mjTnWmdcqY-aIOOH_roMWJnNFFrMSaHki4gehYzX0qEnhLYpGox1T-wWkw3wYD4jPao8D_c59DyQ876p45c6NVvQOgx2cQRrLJsucC7SXKk8dZb4ntjBWJJT4b1sTAH0MXf7T29NivU8l5B79YeMPgnBToEFcVdrA_Cxg6DJpFk8An4vhNHd-s7L3bOENnjL69GoQgWN7euGtka8Bt-UX3eiNlfLnohnZe8S7c1CRp_53DnHgvt0kD0yUAuyItGCu-YukArIBFOOjqyq6Zox4x9F4gPaCpe9q1eE38Uxb4glXdc4OkXOgeXKnE7xMs5X8VdsPY0w8v4yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bq1Z48UpEnsYlSVx93jDM1PKq-hgQx9V6rknrgq4Hebjpp21v0E7_l_gtHVA7zLdnClNRwFm_Z4FHeJsWq0NjY6rncXgGpm627brk-NvBCV9ve7IqpWlxZapQUD4_mWb9_oBOPgEtQqKsuuNPZjuWQcVMlr5XoekGyxxi5PAUSMr5c1L54dHEElLqrwioqmZc6rMYCH87Dpm9pJ89V76E5S35ZQRkEB9CSf7r4rrU679lJfhxzgti1iu7HOtSS5f4Faiju1EIYSSx0AwesE19OzWAVsx9ZYt1R5CiM7fbxIeiSqOi0L5vp9ZaU1SgSRGWDOSyiQkyL4jLg5n6r4peg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX2MNgHkkylE-aSTpInfAN0zFY9A0_rvuMREH8jjlyO-17C6LtbJETZrFJ2WY-xj6aXOAKNrqVaHJ2w4WN5qDO7JLTTuDgZ_MxTpuT6l0Yuz5WRIL5TO0M5rJz37LlQEFzRQdikxx9Pb25hqPlmnKjaPfngnuMfa0K7FshKLLMp7Hkl_nySo8u0Tg58WssJ1kRRPSwFJ6zxWyVVF6UEiMwkFJZow8eTp_H2j78MoF2ISjEkUjwWPwMX4Sc2fF3Bb_pcDhmtOvR5V5Hg6i9iHI7dePhmL7NBclh9nIWwc2hzH7SY4RE0tdWNH7uOrNBGe2NMBk7g59W8AJgVJKKYRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=ZwcLCjHDO6F7ndODGHVQ-nb82sBI4BYulznTssrAnk-UemJ3BqP4hAx3DCftv38XkApGVbN61uHTQZ4J2eYjN2aZ01FCt9t2sYIObBIwVzH1vxEbheXcf_1AKIEfJL6_dl0TFgxLIurKppYymt5c1kbnNq8CoWjG9d4SF4P92PwNE-l_u7JBn7_zO7OrOyPKnN-UZTXzGOnI-S6zt9tMVN3WzRW9mvTiDHmI6MBDm8iS63H0kl2XTjtGhLnZJjJUP2ijpSYOIkKI6bDLxlaGUNKgbqNPfxHPETd2JWsv_PmqniPOPDbnj8700PCx5sKffbnHh0t5pQCTpAdQ38G_v3ENGhRGDeq9fB3ndsygToA1XUS5KbmFzqfwTcSa_VRyFY1k6c4B6kSxNIlnCTs_Idw3j6OPX0XpREJO9nlZ0D-v66kd1SdiHyiecpOzL38RDYsy4S2YiyroXml7P9Q79JfMNxP_Unyooz7ZSmZUV69dtwk199gP7svbHtWQCp3cHaG4tI5YVyLJoI3GQyeARZWIsHRFGXOE7nhoBTcyMOkXwzs6W78PtEWS0l4Fb459nZkjHWVX4XRlg_kBn7LeXj2iNo6WugNtpsExaSVTFygVIExqkVUtg7YZ1BKVeZ7o-xv4SlIVIrVQ8n2SIppwv4iwml2t7ZO_T8BUSvq-mZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=ZwcLCjHDO6F7ndODGHVQ-nb82sBI4BYulznTssrAnk-UemJ3BqP4hAx3DCftv38XkApGVbN61uHTQZ4J2eYjN2aZ01FCt9t2sYIObBIwVzH1vxEbheXcf_1AKIEfJL6_dl0TFgxLIurKppYymt5c1kbnNq8CoWjG9d4SF4P92PwNE-l_u7JBn7_zO7OrOyPKnN-UZTXzGOnI-S6zt9tMVN3WzRW9mvTiDHmI6MBDm8iS63H0kl2XTjtGhLnZJjJUP2ijpSYOIkKI6bDLxlaGUNKgbqNPfxHPETd2JWsv_PmqniPOPDbnj8700PCx5sKffbnHh0t5pQCTpAdQ38G_v3ENGhRGDeq9fB3ndsygToA1XUS5KbmFzqfwTcSa_VRyFY1k6c4B6kSxNIlnCTs_Idw3j6OPX0XpREJO9nlZ0D-v66kd1SdiHyiecpOzL38RDYsy4S2YiyroXml7P9Q79JfMNxP_Unyooz7ZSmZUV69dtwk199gP7svbHtWQCp3cHaG4tI5YVyLJoI3GQyeARZWIsHRFGXOE7nhoBTcyMOkXwzs6W78PtEWS0l4Fb459nZkjHWVX4XRlg_kBn7LeXj2iNo6WugNtpsExaSVTFygVIExqkVUtg7YZ1BKVeZ7o-xv4SlIVIrVQ8n2SIppwv4iwml2t7ZO_T8BUSvq-mZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
