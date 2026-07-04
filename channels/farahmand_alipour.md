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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 17:36:18</div>
<hr>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Sus_ujqd4ki_ko8ue9jRSf_Zg9EGjIU4IwL8osyV04M9qQa40njge44ukGXPbYSMJssHNoBg-16z1zSOmdfyiSCNnzSJV8jDyf10355qHdYZX5krOAxkrrMkxIsw6Gu4O3DWLgha7Q_M_XoivS2FPLoFsNo5q-jtoumkSWHVHNoadCFKcqG5yjZUxZugG-OmCHoZi8ZKTWmwEttfuwgZmQOoi860qktuczpVXqlqQ8admBCwNPeusk9fRp3H9T2efQeJXFe4VLcHwU6p80schnJ6ckL9Nv6R3XPW0m8uqAZBAmxHsjB4PdSULN8Q60_vbXn6wfFT6XTXKDUt3ukE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Sus_ujqd4ki_ko8ue9jRSf_Zg9EGjIU4IwL8osyV04M9qQa40njge44ukGXPbYSMJssHNoBg-16z1zSOmdfyiSCNnzSJV8jDyf10355qHdYZX5krOAxkrrMkxIsw6Gu4O3DWLgha7Q_M_XoivS2FPLoFsNo5q-jtoumkSWHVHNoadCFKcqG5yjZUxZugG-OmCHoZi8ZKTWmwEttfuwgZmQOoi860qktuczpVXqlqQ8admBCwNPeusk9fRp3H9T2efQeJXFe4VLcHwU6p80schnJ6ckL9Nv6R3XPW0m8uqAZBAmxHsjB4PdSULN8Q60_vbXn6wfFT6XTXKDUt3ukE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B46qcDMo6RYxaj-UxKkLkDM9oJWBs4YdTd2cuaciChQGftegZ2ON8BJtsJAhtasxb_TispDy_dF4vlsAxgRb33WoEDrjXyUBqJ8BxnlDp2H2oFkTzrHIqWMdib4LgGOj5clIVEBmaFu4Q7kLi68wAi26jSQ8eMffr-c7UCQE3nKGaMHI8IkH8LCUhAyLf_BA3xk6NYfFPVRAvyTp3KscA0XUsHscs4AwFq_HSOGCjQwO-Clks3Z9Q9Silb_tVWsCsf9IVvFaV9fz1KuE_vMoXrCHggX4OV9FcDePd76m4-o37QuF1WD6pN1Hc8y7nVqmAnyqK0SdZlJmKO5ZdGvRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWK3YjDqeqzxH3Ej3bQHsf0aynQAz8V_pUfw0zUuRadJZ8fHzejokSynMVkLE-AaMnL4_0y4tleLP8d-c_JK9PQZdgTwluUmoLnTbeVujbMICREhNwuJe0EW6xhieWoguPycNjbh_oXT9G4VWOdbmNZtSnAMze5-MPaUX0B69KOJzRbUpLQD5TDNGrTe-6_GVYiFiLGS-zJsnEhc8Bu80R3zg2QCE1ZhK8AwassKtYwXikjVSP9UHSLFQpcAAGpvoQZLlxdpAljPRd5q-XLKEJJmM7nuL7UVF9uZKQOtlG27J4OtXW0ABRZQn3W0znzkKBdYA0R9wAXuF6hpooiGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=WQslslzo9WDMA2DkcajEDU7rtLwTmWAXcr_hhXSWYjeMR4mZvTJlESwl15N6zpeGM-c6P3NVyj66HBkD0SKa3BiA0t4MyKuFwclHNMW62VryU-RyRa9XOgr_dIVS5_71S3vGDl3291qdtu-nqut2xE3nWBhCJVnrfmBAEgcVPEm3fIz5yZu4HVNScXpjW636d97DoI5e1QpUNONIKJRfrIn5JTwCXRbStDHli2cS5SnfphLd44wzDx9wpYPQLlPiOBBBPwcKi55oOWjrs_1lYOsf4Putm4zpS_Nwo3ao5Ss132HE6F1MAgGJIcyEznB_GvPX4oZQYsdEUBngmJFOUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=WQslslzo9WDMA2DkcajEDU7rtLwTmWAXcr_hhXSWYjeMR4mZvTJlESwl15N6zpeGM-c6P3NVyj66HBkD0SKa3BiA0t4MyKuFwclHNMW62VryU-RyRa9XOgr_dIVS5_71S3vGDl3291qdtu-nqut2xE3nWBhCJVnrfmBAEgcVPEm3fIz5yZu4HVNScXpjW636d97DoI5e1QpUNONIKJRfrIn5JTwCXRbStDHli2cS5SnfphLd44wzDx9wpYPQLlPiOBBBPwcKi55oOWjrs_1lYOsf4Putm4zpS_Nwo3ao5Ss132HE6F1MAgGJIcyEznB_GvPX4oZQYsdEUBngmJFOUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hLVQm0BHqiI2Tq7fGrDCFyKSffr8z1kXF1SJRdoaylvgwQZoZZxSua6maAY3gdR3I7Slp9cI_Ua1miJ47UvNS6E7MovRhngw6hWXfL4j_mQ4aixz-Iz7pwerQUUYGy35hHrCRjyMc8rRWkFyrLwkklr6eSg4TR1YhRp0qOoGbR9pxMt-cj-cSSr309-wZgEV65a-Go_rVTOcfOGGl_XboLIBNqzy26AxyPxSunzzyC99a1xeCXAsMFLc066lOr1XtEUpXeCM5PvyVxXnh5mvhMYVojFxJFPRLCKlgz_aHLLhGOENqdsXYu-aiDZ_lemUFi_ok3on9-6Hj7MDIDO8nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hLVQm0BHqiI2Tq7fGrDCFyKSffr8z1kXF1SJRdoaylvgwQZoZZxSua6maAY3gdR3I7Slp9cI_Ua1miJ47UvNS6E7MovRhngw6hWXfL4j_mQ4aixz-Iz7pwerQUUYGy35hHrCRjyMc8rRWkFyrLwkklr6eSg4TR1YhRp0qOoGbR9pxMt-cj-cSSr309-wZgEV65a-Go_rVTOcfOGGl_XboLIBNqzy26AxyPxSunzzyC99a1xeCXAsMFLc066lOr1XtEUpXeCM5PvyVxXnh5mvhMYVojFxJFPRLCKlgz_aHLLhGOENqdsXYu-aiDZ_lemUFi_ok3on9-6Hj7MDIDO8nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXxSDLlUePGQsu6_bHEPLaz7rerSO839oNpE5JzXuURKpLtG1ehiTDDqAI58tbtaezQTzTI0YvGWknhYJxP3cv43t65JSviH0rhlDsupU8KLRifmakRQWpOwabJAa-IL86VCvUEoH_2nPexnOeBjuo1s35L7ysIWf5rT6mRjUxac51Q4vtUrfberdinlpAGEYDWKGyGdQrAKhijZGz_HCyTtKtFBIYUxR4r-F1QFUiSUYAFjRPPJzcP5PYSbNbzESqt9fSL_E9CGprvMjo590bxhismlq0oVl3ySAdeEuLt9mCNfwC2Mx31TyFrVAWqXAibFiqem1K15fSRaux-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiX5u_G8rLrpqdvxjXG2aS72s8LUjOoZ6wuI2HHTmdra86VXZ-QjzYuhyWJsPwQTTlH-t5CxcKJVe8VnKHyteZ1Ovk1qsiN54bpjIS4cO7v6D5v1vyuGdajEhYG7bTNq4lI_VOc-z8tpJfR0Qlaccbhed5I2fY45KBXBZ0bDvMXFoM7VIxFuz5Wxo8yrnlVoLOlEM3ToiadUfKZSRSyqHrKoV5MVHPgq8KQIQu3orj0MFqIDJzjGJCe99NTOWw2mT5KObX8sbhFxmHRV0Bep1DOHKpjAw4L0JqhLMvFohohwFFJ4lj7dFG5iAUCm6XDu2i3PLRVaudMPncSXcoiUuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kH_f29z25SSN6ZiSKx982dEhznngLNMZlbmC04Q2QJ3NkawbyLDliRKp3qBQicTr94acepklmSK6QHTjk6If6rnQmftfPcu7iespMIWrxJ0hH4hbK8GnXx80JQJeAlIx6Yh5_ujvnwHdVNgCjmcCWAo7Gsg44scBnuiliUY_FBVgrqlcG8uQXOGYAiNwVHLhuSzb5qdH3MZj6idjBG0JXM5awIeTUixuJUGLmR17Iea_xpZr8yRIzhA5pc166iTRjvBCQL5ZuUkq3dXO6W8D6Ymeyaol5NjocT4LxGnpm1P2q0bVK0scxZ0RIfggGwazSz9xApwnvaA1725I1pkkmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOpDUgL7BgRgOkqy4jb7QdzAU7mFEjK1zKzusFAPf1p998ztN0LY6YyJ3f6pUuKcTPB7Ce9tit4vQpzILhHll6ybAQad_QNR0nkA-u8sY_dUY8tegmfO-tNVgNoYukMKWiL9QePkZ6GpP7wrUF-TEBwL-Fjxjo81LYDZHM8s9-KFtHvolKuB-WWuwU5lZrwj2Z7J2iH8BpOK_Ec6x2Dbw-wW4fap7reuAhxcQAb1i2gM88er6MGA1wL-NZaV4cP3q6PLTKOoFLEuuqFPD4gV8pEutgHU0YW7m4hHTHKAwcTTZOyWIayw8r9LhpzpNfsWVa0mUBiLORvQszZ7Ht0NVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nubrDYjzG2V7EqWJ_0bmKmjUxYRSeEp1H5sj0yRa9CqginF-2q5PYzWh8hWoD9cwXhvFcouhyzlO8dHTJjEZGA2_MPL_2IvFpivYrTlaKfjCKbdLkoHPd-6ysQRWS-JlTx0wnswNG-gAV9BGxwFfjXZcmkTk5zQ_IW1tUhTkHV-Ywzg4r_ryVi6oYL_8WOqYXgpGoyFNkn_p8_EmnAWqdC5EQIGUOdQN42c0_DZ8tiV9TuCJ0gkvVFgH1b9aKDKWCVD4zQaMpaOicyZDIbm7iGv7b227B5t00wFcczT88RzbkZHwjAUoD8bqOO8Iu-t6O2WW_Nk7ZajmiwNWsNQ2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1JCzqfnvjq27kE9BaAQ2Qht3JF-LlPicYwXIs2GXHRbgvrsWdeWrRFEZGEXJTev0-SlxGXr6PeyBDo6PWtsWFsHtzIrA0L5gMJIxhEzPzKVLiV1wsZJuxOO4EhkeWHwp0KdA1-krrabP_Z0_2QaTlakKus621gyWeqaVReVnAY5hhGILZQOKdmZdyN7Rcng9Ade5w2RfUlvGL2K7Mt8v0N7xnH9wbHoinh_Q2bUnmb64f0KGANGjJDl58d7Txq_v9oJnRVz4joNzuz7zKUzX46ZbeaUmvRNjBlb_tEo2sCjjsFxXrzPDSVc6ByoNijmoguT1zoOvNWkwsGPdrsg6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVB-n45NGvcFpWzRdxdBXQYcnhHxa97b6KZTKcim4lkHM_1OwiI4v4BEL6m5kyVcWhv301yKRUflakeQNABZ_6S1Ak02w5eSYgwyW4DEYf6gfcQs5-voiZxZWbFoptHanJHvjW3c7-t4e5ZQajjlDlWoJJMVFYdexorVUAICQ_UyVZu_Gmuv-s4tYVXMWdeA1iRP2C1PLebsrDqCBvtHIMY9Gz-vOrGK1mfJU2WaxQKrj4U01UqXhuj3wdBCycFsgb-cNRtm-z8IpihoKXGD44KXAKhyuxGfY7jg03a3rtPoioL4D_yE0VqQfq6Xl4va-P18nOZlwuLJoY29tyoAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUQ87jqawjvN3lDwrmDS4YUhjOVc07HdHBOyeTsUpcZQbnnqnjuPNHzQPYVMYFmcM3Udu5J0IDGUXAx1M4xyidGPKQkiNSmKDciJkPdUE2p-dZpsSE9BkGLxwX3ohtgKIYkmXWa3tH5UR6iLJNzdIDsLmoNzmFhRAyfsgo_0me9L9p11v04VxEh4QwcR1HfH0O_YNN9FFw59uQqeKIhMJmkMetWcZGCV0AiRaUHjUsv9TsHBm1hJ1yav7gpEgxnLDw3xpvMl5r4VeK_GStiC8Zf6LW9lzcTsvTC0i3YFCDP3qDWA54XEpiNkY5A9c24mVMfnllnrVM-YJ6n5ofkD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPcShgoRlXKAu8_pxPEmY9x0b141ij-XrYhVMRmO0kDoI5Lhfz6JvnSDs83TmNYAMEHr3_gJUiX5vakf0iuKsc5cShCsETTJZNkL-gqw-UU0AFVapxKhfLl0xdCM-nZBwoR2VNDG7Am3BI7kd56v2BiT2_aLSSnczXGdHpdNSq-bX4a5ob9wctLNGjcCLnGLImiaIl80br8pDKz3ukEMsXRunycVBkBqV8R8Ijbox8XlblhomD1ONkcVqiIjfn1C6YDr-YL1O10pZwPAYxWDH8n-buLTZ-K2d5CqWppsIKQ7O-lfAiJZ_UyLG-uGoPDx6mDFFP68p0HG6ZQSxmIdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=nbcJXGY7raS7hDoFafi-7jSX0AXy1RcB760qw_i3eJ7DBVpFYeOONEx77QFXt-qPvhp7K__g5Kho8DLEM6hc1S73ocqiokBl0VD4EWGSZOMTJzHbNaeyepxvJc3aLby_qv48v72u_Mx4wVDHP0rAAviD2-tzl1bg-KCStRj6DbA18IXFDaKLOivN3nxAcpsFXs59VRXrPfqd2OxgqoqkBRAM0fMqWpgSTlQvwomx9Ycws0CDd0vuuGPwtfj1k5c3E3Uo6qH6_UsGQG07ha_PIfdnl_ejSvdPxzwAounbgasitPsGBOKxsngCj92jwqELED0xbHEWGIZLOlrEUue0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=nbcJXGY7raS7hDoFafi-7jSX0AXy1RcB760qw_i3eJ7DBVpFYeOONEx77QFXt-qPvhp7K__g5Kho8DLEM6hc1S73ocqiokBl0VD4EWGSZOMTJzHbNaeyepxvJc3aLby_qv48v72u_Mx4wVDHP0rAAviD2-tzl1bg-KCStRj6DbA18IXFDaKLOivN3nxAcpsFXs59VRXrPfqd2OxgqoqkBRAM0fMqWpgSTlQvwomx9Ycws0CDd0vuuGPwtfj1k5c3E3Uo6qH6_UsGQG07ha_PIfdnl_ejSvdPxzwAounbgasitPsGBOKxsngCj92jwqELED0xbHEWGIZLOlrEUue0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Xj67JIrwEaDx1kCqGj91RGukzzfngpKq98DTXiLT_XcqMlLUw1AR90k4ZaY7QQoHMC8-uPgF40p7gp2cWVRrxxfAxa6RGZTfOpjGA8bBXG_izg4xGqfyeWYfKV9Db6cLjQC1Rx8qv1gxVVYZ7jrxsBbo_7wedYv0AIPHV9LMoCblmtX0cb9BEw28qucA2XOC8veFPClGaHDBHVPxpPr3rk0TEcG9kC_5cCsn-jjaIzBHyzgH1q389rTFJ1vSHf0761tyQO8MEiuVHiKTGBOMfRd6Zx0NQyBfsIMpJzGAB_6blQvLsSm-AzUOu_MlseGopll4YWyIsF6p6v4JAA05qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Xj67JIrwEaDx1kCqGj91RGukzzfngpKq98DTXiLT_XcqMlLUw1AR90k4ZaY7QQoHMC8-uPgF40p7gp2cWVRrxxfAxa6RGZTfOpjGA8bBXG_izg4xGqfyeWYfKV9Db6cLjQC1Rx8qv1gxVVYZ7jrxsBbo_7wedYv0AIPHV9LMoCblmtX0cb9BEw28qucA2XOC8veFPClGaHDBHVPxpPr3rk0TEcG9kC_5cCsn-jjaIzBHyzgH1q389rTFJ1vSHf0761tyQO8MEiuVHiKTGBOMfRd6Zx0NQyBfsIMpJzGAB_6blQvLsSm-AzUOu_MlseGopll4YWyIsF6p6v4JAA05qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Sr8CnavAEEq8EceHGeONmaY7oWkgpMeMZvhoSoOFhLz_AjjEy41NcyUnMgaNRGXXBujRNhqU1m8KiAPoUyV_9NyF1whgpGUhU0Ay3T1NKRwMPEw3dobD7ZJ7Klipn1cwyfnW4Xc_QaxHIlzVJ3Wn1db6qcrJNwFOI9oYC8D2Wo0qzw7DsYDHtanC3TqlX8EUyzcYQdUx256TXUB83vjeEDDp7EtFX26JIecERjSquFw99k46Ya29kCjT-_X_dHJah8OHnrIKugI8xX7fDebNkEC2zrWc8LCmzkv25zSoOzJRM0YC5DLYDdx-TduXiHjEHrt5vkqIT4NZeDftYX_ONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Sr8CnavAEEq8EceHGeONmaY7oWkgpMeMZvhoSoOFhLz_AjjEy41NcyUnMgaNRGXXBujRNhqU1m8KiAPoUyV_9NyF1whgpGUhU0Ay3T1NKRwMPEw3dobD7ZJ7Klipn1cwyfnW4Xc_QaxHIlzVJ3Wn1db6qcrJNwFOI9oYC8D2Wo0qzw7DsYDHtanC3TqlX8EUyzcYQdUx256TXUB83vjeEDDp7EtFX26JIecERjSquFw99k46Ya29kCjT-_X_dHJah8OHnrIKugI8xX7fDebNkEC2zrWc8LCmzkv25zSoOzJRM0YC5DLYDdx-TduXiHjEHrt5vkqIT4NZeDftYX_ONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=oSzfoaO5JblR5YwnkmR1pn2EjklTC782iYB8OxC5w9rNqQ-sEpcoZMGPf3vcZnzYZTjqzFtrF_SawMRX7L-4wvQvpEUz_rjO4-jH0dYsGDKhgah3-PRhwcVqHJlnqPH-jX4YwCzYSKquRw0i1FpDXU5KeBAoSr0WGDIPVesxkyaDRwTfMoY9iXc3ADL-TuBXqM3Wy60QW418hJZNck_xzkycyPlI8HFnjUOOx1TU66lDQ1CdrzueYBYzNxsUVNTiXXLvucwUI7iGOh9VpvTNsbjHnpX3CJbW6UAt7jOqx5LN3qVidp5kuglHSw7HPniDe5RHJnxbrvaTc-wskUbARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=oSzfoaO5JblR5YwnkmR1pn2EjklTC782iYB8OxC5w9rNqQ-sEpcoZMGPf3vcZnzYZTjqzFtrF_SawMRX7L-4wvQvpEUz_rjO4-jH0dYsGDKhgah3-PRhwcVqHJlnqPH-jX4YwCzYSKquRw0i1FpDXU5KeBAoSr0WGDIPVesxkyaDRwTfMoY9iXc3ADL-TuBXqM3Wy60QW418hJZNck_xzkycyPlI8HFnjUOOx1TU66lDQ1CdrzueYBYzNxsUVNTiXXLvucwUI7iGOh9VpvTNsbjHnpX3CJbW6UAt7jOqx5LN3qVidp5kuglHSw7HPniDe5RHJnxbrvaTc-wskUbARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mNA2hRa1rYyxHJ2a_BdjIb1-CosqKtC-gkzfaQvz_KaQGK4OlHbeHC62gV6HO6i43vQiiAIGlvdS01WOVLJq-T91UTo5Z0eerEvuWXkI2ZcLvvW0VPBeKrE5tem9qeBhAAB8IKvV0uye31Cgax9elVzL1mMDgylP3u5VX2s1RApoegVdhbQ_5yEkUc6F0i8PFJeju8L4x7h5d8AqkYrBnA_PLfTIgjdS3-W-Pdv1dbvDR6ZMOeG7mxfH_QqixdvFucQBJAdAKxRzS4iLVscze4_OcGieA5v3sZjtoopJpPCI8sszU_Y2N6NSI0-diF-owUaTRuEP_ZDh77a1VC4Kyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mNA2hRa1rYyxHJ2a_BdjIb1-CosqKtC-gkzfaQvz_KaQGK4OlHbeHC62gV6HO6i43vQiiAIGlvdS01WOVLJq-T91UTo5Z0eerEvuWXkI2ZcLvvW0VPBeKrE5tem9qeBhAAB8IKvV0uye31Cgax9elVzL1mMDgylP3u5VX2s1RApoegVdhbQ_5yEkUc6F0i8PFJeju8L4x7h5d8AqkYrBnA_PLfTIgjdS3-W-Pdv1dbvDR6ZMOeG7mxfH_QqixdvFucQBJAdAKxRzS4iLVscze4_OcGieA5v3sZjtoopJpPCI8sszU_Y2N6NSI0-diF-owUaTRuEP_ZDh77a1VC4Kyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=p00LO5-XhY3QtVDXMcOxh197GdY2QgjDWgIyeNEHYgePfGZJAr1uR64w0lJ97ty1WVmuJewNIi_uR_p1vQaPp80X3LppjYhONjltcgC7JO5N7GKJF7EtsMsU_CYRDhUaiKtyCOg_P86qIU2Y9A_Tkkuol_cuKyT2ynR845oC3yqczovH9srdZzGWH347354gskCNQ64cBeVVt7tVd2jn_z9jGs_gwN6pJGCfmrIo2yG-HSfN7knsB7RbMGObpLSSdDhhO_kaTszz_d_pYoXbhfiaTJnZDGoLq_ARBEhraM1LbUfAGIAvDsQuf8ZvxZocEn5r3NBBEM3wpmhqvDhmVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=p00LO5-XhY3QtVDXMcOxh197GdY2QgjDWgIyeNEHYgePfGZJAr1uR64w0lJ97ty1WVmuJewNIi_uR_p1vQaPp80X3LppjYhONjltcgC7JO5N7GKJF7EtsMsU_CYRDhUaiKtyCOg_P86qIU2Y9A_Tkkuol_cuKyT2ynR845oC3yqczovH9srdZzGWH347354gskCNQ64cBeVVt7tVd2jn_z9jGs_gwN6pJGCfmrIo2yG-HSfN7knsB7RbMGObpLSSdDhhO_kaTszz_d_pYoXbhfiaTJnZDGoLq_ARBEhraM1LbUfAGIAvDsQuf8ZvxZocEn5r3NBBEM3wpmhqvDhmVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFO04IvdDlqG3V0FGBMJoku_wdWwXxjJFXCn6FwoN0tQTw_5LZ5KDJAMe-_UY-Idyot5j18GQpdz7FW3AAVHEI4j02w8pHqpqUa9fc4DQrHZ3FEDcZ9_euWjo7CmFFp6QPlkaHNn9wZrsj2oeVefCWapW0cJ2D_xvL9P_tZPTGmheOEOBLZEj7y3ERKPP8ok2NBRhV5_AFZ-v6PIb9SZMgabb9JDW5B2XMnEdg2SeoRyMY-85Zb81VssisV81DV0BjMVBZvT9qO83clqFkqhi298scu0iYtGI2zTwUV-Zw_LLR26jnFuawoaPaiqdlFDWq52NYhNNjXPXIDhlBjy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=pPYl6s_m2aACCFw-K7NwxAZi8w7rfpeVvDOpNvKY9O8N_Qlp9YaATPIsPUSjO2oHNfKwz_ULnR5Uqkp3oDrf7w7D-bdolnVEFnLLVMBrYoHhB3mABbqObbmE8QZfON6NA9Dr8epfCRk6ty58kxgTII7BYhTxDLkyGcRAEXV_B4WVY9vVuLaNi_TLUxSUKntXS5ISREQr5S8da50CPjwmzacxjkQgEvp4Xl5IDj4iDqu3ksjBUX0cAXtAacb4Ako2qR_uJqbbkeEyenvrWucWuvWYiQWZWR8nDod2zrztTzKayk-jTx-r2iNMkobAyrsA6i8uM8Ol5zp67Z6KQho_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=pPYl6s_m2aACCFw-K7NwxAZi8w7rfpeVvDOpNvKY9O8N_Qlp9YaATPIsPUSjO2oHNfKwz_ULnR5Uqkp3oDrf7w7D-bdolnVEFnLLVMBrYoHhB3mABbqObbmE8QZfON6NA9Dr8epfCRk6ty58kxgTII7BYhTxDLkyGcRAEXV_B4WVY9vVuLaNi_TLUxSUKntXS5ISREQr5S8da50CPjwmzacxjkQgEvp4Xl5IDj4iDqu3ksjBUX0cAXtAacb4Ako2qR_uJqbbkeEyenvrWucWuvWYiQWZWR8nDod2zrztTzKayk-jTx-r2iNMkobAyrsA6i8uM8Ol5zp67Z6KQho_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=qKY6M2HBazsnX6joViRrhN_IXxCOsNS1n-N198OssAdnZxpaBIQL5SBVj4GJ2450FIoHadFHKa-DmYmDAdxuNNs04JFB3Ak8gRb3jAjcuZK6QfS9L2Vge-ihEYJCfkqV9YfYovP5lR3kFnmRcU1HZ6x1yC-wHcV1mxEDoEZXOVGfDQqgVXaAulRFOqKL17qlCQb4tMb7V3EFzTy8gDbCUqWlNpPvRi80mh91LU7NrQaRL04c4G39Mx9JpS3EuVGV7oHNCpC63qTgNr5PNFQKi5b48pEjEKc0pNO-tLBTLbihXYNr5T6sgtw7CrXpLWR1mrP-ENj38qqzcDnfHTIX4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=qKY6M2HBazsnX6joViRrhN_IXxCOsNS1n-N198OssAdnZxpaBIQL5SBVj4GJ2450FIoHadFHKa-DmYmDAdxuNNs04JFB3Ak8gRb3jAjcuZK6QfS9L2Vge-ihEYJCfkqV9YfYovP5lR3kFnmRcU1HZ6x1yC-wHcV1mxEDoEZXOVGfDQqgVXaAulRFOqKL17qlCQb4tMb7V3EFzTy8gDbCUqWlNpPvRi80mh91LU7NrQaRL04c4G39Mx9JpS3EuVGV7oHNCpC63qTgNr5PNFQKi5b48pEjEKc0pNO-tLBTLbihXYNr5T6sgtw7CrXpLWR1mrP-ENj38qqzcDnfHTIX4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=KRfODJgvCBKA5PrJ8s9lbNNFdWjEsZXMEhrVnGoDHj5j6ygM8fWm_3rzW692liFXM0SVz_wjQyKZrxHk0usgw5Nj4K8xY-j56-HvTxHGSw7O_qU5-9cT18kouVrZP2Hm9q-ibU0qNvwV678KLibOm-4EhCacpe5NLDebkFde-cffi_TSt7aDJJ7AAOgPWOKrGXVqR7-k-66xrYxo_6AFxxbMTbgpUS3WzdS5KHB31LDW5qvlnugPM3uA7gZrNHlfYYQZ0WWTY7mWZLZS0asO1i_xA8TTHry6q02Lgojq6xvlTm0czYKjl3XljPsDZRxa6-Rgoa4gF5otg3PKpupAfEjd6GoQtDrW6QCGZdW0vOliosYTgODwF1bzZedJRPsjyyBxvix6PsFNZ1kUf_WfuapGfw7Xf4NifQDUEc8ewilQWgpV9rIw5eP2UjsytzBvi4BNJwqFOr9Ty8UpXY-ZSrsgyfOnsMlS-CaOYpRRuYkTZKSt7dGSX70MBDwBtDuIgwUR3t5GoWkZPpIOgC_l6627-I0pMKbIXo4tuXKvMr0Pkzs94_glYO5Dsn-d5EjrMStX9um9Mq4aX8kSH1qVyh1JL0I97X7inyNUjYEkg6XaElQRs1SrII94CqRSb85MrPWkesEEvTtgaYVbYYh5IEOLdHet0vU7j72gN5RJ7Gk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=KRfODJgvCBKA5PrJ8s9lbNNFdWjEsZXMEhrVnGoDHj5j6ygM8fWm_3rzW692liFXM0SVz_wjQyKZrxHk0usgw5Nj4K8xY-j56-HvTxHGSw7O_qU5-9cT18kouVrZP2Hm9q-ibU0qNvwV678KLibOm-4EhCacpe5NLDebkFde-cffi_TSt7aDJJ7AAOgPWOKrGXVqR7-k-66xrYxo_6AFxxbMTbgpUS3WzdS5KHB31LDW5qvlnugPM3uA7gZrNHlfYYQZ0WWTY7mWZLZS0asO1i_xA8TTHry6q02Lgojq6xvlTm0czYKjl3XljPsDZRxa6-Rgoa4gF5otg3PKpupAfEjd6GoQtDrW6QCGZdW0vOliosYTgODwF1bzZedJRPsjyyBxvix6PsFNZ1kUf_WfuapGfw7Xf4NifQDUEc8ewilQWgpV9rIw5eP2UjsytzBvi4BNJwqFOr9Ty8UpXY-ZSrsgyfOnsMlS-CaOYpRRuYkTZKSt7dGSX70MBDwBtDuIgwUR3t5GoWkZPpIOgC_l6627-I0pMKbIXo4tuXKvMr0Pkzs94_glYO5Dsn-d5EjrMStX9um9Mq4aX8kSH1qVyh1JL0I97X7inyNUjYEkg6XaElQRs1SrII94CqRSb85MrPWkesEEvTtgaYVbYYh5IEOLdHet0vU7j72gN5RJ7Gk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=VgqPCJuJbMjgaceZ23DkrQAu_uBF9-Noatk0kLZKb9YRQ_53AbvD5xTK2_vEiSYTh5aMzK_7_yKTMaPh139KGFgodUxMnMDbZrxVzvsDzqzaNfoUwkJulc81l__EKAOtVGA5RCwrijgvSK7Tv4n5pp1_hYSrVR0SiUom5c4x2VYgTeAR6E5IEBbrU6lekfxYOSd0bDps7ABieus7A7Vr6ey5Ka1KT0-6feShZ14pLjlBIgX1r0NyvQP9yZRhj2PbYVCO8YXPQhJwT0L4ZC_wCK67E-hukms4gDme9YNcVqlqOLYs6xutKCRI9Bv9JfZ3oqiiaofAhg1NQELlds7ktw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=VgqPCJuJbMjgaceZ23DkrQAu_uBF9-Noatk0kLZKb9YRQ_53AbvD5xTK2_vEiSYTh5aMzK_7_yKTMaPh139KGFgodUxMnMDbZrxVzvsDzqzaNfoUwkJulc81l__EKAOtVGA5RCwrijgvSK7Tv4n5pp1_hYSrVR0SiUom5c4x2VYgTeAR6E5IEBbrU6lekfxYOSd0bDps7ABieus7A7Vr6ey5Ka1KT0-6feShZ14pLjlBIgX1r0NyvQP9yZRhj2PbYVCO8YXPQhJwT0L4ZC_wCK67E-hukms4gDme9YNcVqlqOLYs6xutKCRI9Bv9JfZ3oqiiaofAhg1NQELlds7ktw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=NlngBG7PwN1cCJCHWehrITrXhz8MiXaxgI9hbiCr-GBhQNR-do_o6W-NBD5j3F3PikFqd8QqgEdK7IaImZB4Hc0dsLXtBVOTNBY9bzBMIEGwsNvmmjFJqMmWiwSZaouwRJJj5hWpJSNkPv8q9QjzHw9HxZRvGyJLavqOn1Ox2UcbDCPUPIGHGGvjfCDo5Q33Sw85FMNO7o6mZUbo8Oc7aHJX0tYij2vRJ_pZMv-zLGsqj8Wr3s2WzCsMhdh3F3pKAzdnJgVukPvg3egbP21N8vUInRjgVlrVNIwlYLt_dS5841IQtJ9uJCKDJKfz83REqmJCfkWV2DRhVexh9qZMYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=NlngBG7PwN1cCJCHWehrITrXhz8MiXaxgI9hbiCr-GBhQNR-do_o6W-NBD5j3F3PikFqd8QqgEdK7IaImZB4Hc0dsLXtBVOTNBY9bzBMIEGwsNvmmjFJqMmWiwSZaouwRJJj5hWpJSNkPv8q9QjzHw9HxZRvGyJLavqOn1Ox2UcbDCPUPIGHGGvjfCDo5Q33Sw85FMNO7o6mZUbo8Oc7aHJX0tYij2vRJ_pZMv-zLGsqj8Wr3s2WzCsMhdh3F3pKAzdnJgVukPvg3egbP21N8vUInRjgVlrVNIwlYLt_dS5841IQtJ9uJCKDJKfz83REqmJCfkWV2DRhVexh9qZMYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_nZ1DAXh4SdDRZoQ9MwomDLg-G5ZmE9BRxqitboERAuH7Qn2HmVfwxdMrAuLbT3dh27N_oQCbLtYcbCdg-ZKzr9iLour8jNvkQ-j4CUuiXttyu5FksJjbwaPN9xjNomRQ_8zpGzSRcmcwspQX0rjjugDyLC-P46Ta-6tsSIU2sH02zkqH_eDcz4xuIMGJGpkt2uF_68PXfSdgh5MrIBlmg1i1GxBQnG4oZMIcW4Y-JeH8F-ht-9WbSyv5-SobhRn3niL7fgMLLxrdS7_CLd4Y5OGOTGwawG9OkKA9PGgL5XSaoNnXOyJ5Soqt2YdS1jfnVBabRjC-GJwSMsRjCFRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iO9zlNJclECIIOLv7F7aXcpRUqkE1G_vWHC2biB8uPB0rw_gUV2EVz4rUzY5Qhs9Fh_hopVL2g933GRDKAoHRzxeofttDEwk_8ozH3_LGbptyMFLAVue7TNeDlciwUUOZUm5xpQahdj5nb2GsAfY-ysxW6Y8MPRlL5mQQdHQBYGPQMFBxFvwi7-hVVNAmmPmuD2IuaSoVDWFCiywRapdf8InpDFx8P9CCazFFjGbvXgR2_wokld0xh-WNsN0p4b2VO8Q3AbekVh9vSK6NW39oeiRID4Va9noRa3ULbjHwD44SVrFKx0oRN4felDrSHPbSG7-MZy7FEDEFAfKXuDZCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=pRMFCgnTFSBJQ91JfShFGvtTueoNlp-dZGtq8pCDINCIGPIPAlmTGEEBiye6P7-ligx7Fb7zzNQ007XV4npXcat_pFbf_uBCDBh-2dObJvZQiFXjt7rHfJxoPHJMdOnVnOnguVDvfyLVnIaNeSnyQGs4S_6Nt4AlowbMnfcHiSE3mSwixpe7pkX6iG-h-yuQ5I25Kc-Bv4ijgaAxXrvfHtSy1BiZHySW1G2FtmQ2NQnJRLgMZ3jdKeho0p_ixW81g_Vz0tbUEYogWn9YH6-Cw-44XQ_ZXHXgycZ1ZrxMvvxnb3ENN0IQd0n_czsA4ylbjqzIEc7EsjETWeaf14o5wIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=pRMFCgnTFSBJQ91JfShFGvtTueoNlp-dZGtq8pCDINCIGPIPAlmTGEEBiye6P7-ligx7Fb7zzNQ007XV4npXcat_pFbf_uBCDBh-2dObJvZQiFXjt7rHfJxoPHJMdOnVnOnguVDvfyLVnIaNeSnyQGs4S_6Nt4AlowbMnfcHiSE3mSwixpe7pkX6iG-h-yuQ5I25Kc-Bv4ijgaAxXrvfHtSy1BiZHySW1G2FtmQ2NQnJRLgMZ3jdKeho0p_ixW81g_Vz0tbUEYogWn9YH6-Cw-44XQ_ZXHXgycZ1ZrxMvvxnb3ENN0IQd0n_czsA4ylbjqzIEc7EsjETWeaf14o5wIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEaRkcsI3QWDVO3CXhndpRKnGZOAaRYPiZoJCk6OfXpUOv1gipu-Qhr03ObHRJF_R9BNI4qcSDHHbwjAGKEY5vL2mv8uAxK9DW-J29iQWj9Xw0EPl62mUmqwDVcSP5ahPypkr5ACwK2qokJKOC_AI04ZOc3yPI7o80qLNt9E_BXQ56-SpVg1lyJrjDFPruXGjjZlJG-DT7bEP4jzPoEET80Ne9FNPxCIf-2MgJsNmJs_eszH49udL0l4D26HOelfzE2e8aS84_MFP1Vhi2xRs_Cy5F4NETah2SRclUYVbV6zwS_RFN-ais8DUGL3PuxegDVNe395jlwswu2chq9YOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWwsiBh8lWDIZ8DwzL4dIHZ8g4FnZsACJ_99PKj4vdm6tRNfWkq-gRFiNlJzdSUemu2W3z2uIFSWREyFSuCmbzN9jnvm9w3liXqBpZ1Vb2NIdgoWzxPwP_PxVavwOK8pUbg3IqmeZG7Jif2IMbQxg642xsQv9cmjvkZkhkTcdBPZbfBXcsIhFqPACpWlqrVSLtwFA60bC5fSgdsTF_vIE8jeTJfx6pEv-hEQC9U2KBcZwNvjY4t6TTIroDfcAjzvGRQo82kzEXOP3c9Y7RLsq-Gr67Lg4ZZ0cr7IkCM4sm28b7jYDjusWgThW3RrBABjeQMZYCGc4hRmUrcXFDOuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTLx2OBkNanBeB74htUe9pzKT55PRoHf7rKXUJqbonbajgBbE_uKWT_LiJHv5-GRxQrm3EErWykYGy3aaQ4SgcqafqbukPh-juwyqM2VYfoZmTpvcf45cdxbn3lK9yuCeKEVD-G6yjoGgx9Q7O9-QyjVtpFmRlwP4Ka0_GysRVw9DGpf256rfNQDwPJiCRn1malnTPyUtHtaZg2HVXZTW1ieOqVVZyjHG_Mpzt8cN4Qsw63fGiSN4kJB5XEF0pEcSM9XxxObgwwDFspaFtVzQ0ZAgatWzEjWhIXATHrxFXF3wO3uDc8F3ggYByRL0KkPAvbqSaStGP9BuILg9__iaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSl11UyVLqTYuHSFxYqAWKZpp8KZj3nmt0z1pK-CBPXqL9tSKyQvecQR_ow5zrU27GBbXjP2Zm6U1wna-BTlGbpsX_h-4SrVkxxgqou_coux-DP4eS5WlfA_KSTyRWuowHUv8b_JRqY0u-XypoxTsuFT3W_AtaXYPdA_fynAyxqFD93x5Y_BITd-fHRaLzou7aMGJGWRh5upIttzYZqMjVlVqvmvezS5-F6y_hKP23Ajc0ib1Gz_Wd9FmEaGWebsRPk4VWvGn2KSHr3ASdyht9RlNtiXGnqQNQpcBIPhhHPjiISvxRL-lN40h_C-mT4P4kQc9Fe-NqB8uMvCacQ_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=O3x_0M-8Sdbf3ogR8KCw6VUOTc9o7ZDodiS6cRxeYm2fu7F2TGUyoS5IxuWz5ZWW9rOw-RwAjETX7QxUnd9pPBeXEBurVGBCKTMF8VNsell6fjv2A6ICZift-WvAKy9ZWsCfytglFtaUlKvtJCif7nscUp2k_C38zdA6dLRb0E0tqpMcUEJiKgupq-tx_aL6G9mTO4yOeVPxPLNjTmuJljorcNg28o6hR6RbgcB1njtzSkdCZnkqkmORz3_6JvM9IcVLGqyG-hHphkXTUf9x2-2CgeFwL-cCXV5BkB9LQfsvcNSVOso_xXiipOoik3f0-Ns1OqD7QRbkwV8qiEiFBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=O3x_0M-8Sdbf3ogR8KCw6VUOTc9o7ZDodiS6cRxeYm2fu7F2TGUyoS5IxuWz5ZWW9rOw-RwAjETX7QxUnd9pPBeXEBurVGBCKTMF8VNsell6fjv2A6ICZift-WvAKy9ZWsCfytglFtaUlKvtJCif7nscUp2k_C38zdA6dLRb0E0tqpMcUEJiKgupq-tx_aL6G9mTO4yOeVPxPLNjTmuJljorcNg28o6hR6RbgcB1njtzSkdCZnkqkmORz3_6JvM9IcVLGqyG-hHphkXTUf9x2-2CgeFwL-cCXV5BkB9LQfsvcNSVOso_xXiipOoik3f0-Ns1OqD7QRbkwV8qiEiFBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=AlPn6-Xy0BWzTelKZ5oZhA7QVknVO5JOPruqfzg2SshdxushO6Vh8yrOlNkxZXKLHL2vMpBOOxS_G0B5BgdRxOnReBnJvVeZrSM6B82jMlt7f-DX2rKkKuxG3SMwRsMWadvwxRDQWBYomrCjItvvFfZPNA6YzukkB5gZsApdTYnsehr-WwuNgrkRfVttqyB46bV9AHemDVwwFaGblzG_j9tIeZiicQCFg7fiTySWVa8QaGbwp9EcbtaTw50kOwGpefDHW5Ylr76XNEYJ6XIGAyud5qcrV1DH3at2jUh-PWz0RXVjoG7CLlkIrZv6q1Kf3FM9TJh6nusMn6vxKcQrEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=AlPn6-Xy0BWzTelKZ5oZhA7QVknVO5JOPruqfzg2SshdxushO6Vh8yrOlNkxZXKLHL2vMpBOOxS_G0B5BgdRxOnReBnJvVeZrSM6B82jMlt7f-DX2rKkKuxG3SMwRsMWadvwxRDQWBYomrCjItvvFfZPNA6YzukkB5gZsApdTYnsehr-WwuNgrkRfVttqyB46bV9AHemDVwwFaGblzG_j9tIeZiicQCFg7fiTySWVa8QaGbwp9EcbtaTw50kOwGpefDHW5Ylr76XNEYJ6XIGAyud5qcrV1DH3at2jUh-PWz0RXVjoG7CLlkIrZv6q1Kf3FM9TJh6nusMn6vxKcQrEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsbuMyYyNEZ_4bDtobVqAZVPJyo9s_cLGQSrXKbbaeWG86kKRtX0YYM-GEbBJDErF-3kJapmBrtDNffnXJdPz0v5KmDJOskOmwWq2UtBrnhd18JSl37K2PMyOGj_rXkEbG6COLL2-KRY8b7J1moIY-r6oJ-uZKzpma9NrmwalM-OORhGbRQwDDWT6PSBmhvL5tKjxgjRL3KeYL-5IIxz29_yTFasLV007hWIuMfgIDDZzGHuqLsv207faG16vKl58VDTBrcfXNyJUAafHQvvjCba-kaxHQujn0t1I7BQ4M1K9SxQr-4LsSaPF1xv6f68haOGoFb34SuaG-EkqCyO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=jt4YISMGquUV1gG0J4rUrQ_UtmTL0GZTQZZCVWHKunlEB6BDe1JXbjl9TCIEV8KukJJ1nuMyfGrCHPlPUowWc-HARz8_zivcaxb0VfgQGTm2HAVaWXLTpXz6dQQXVNdiADdOpDLdyAz79YfQnHQOnCXu94OgqG-AEIBRdZU2ASH0nisR5KJAi45uGMYTIsYw6hGV3l8sUtRQtXkawL5kGGIr-6fnXuc8MskgVHK_kazuePSkK5rzGVgs3EsurivLQ4IHzS1Dayid3rRaF8tpdO1U1Y5TLDPx6kMfBOZoXvCY597VOaSj3xb4uUswxWw53wQVh0BmVjaz-C6VWe-6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=jt4YISMGquUV1gG0J4rUrQ_UtmTL0GZTQZZCVWHKunlEB6BDe1JXbjl9TCIEV8KukJJ1nuMyfGrCHPlPUowWc-HARz8_zivcaxb0VfgQGTm2HAVaWXLTpXz6dQQXVNdiADdOpDLdyAz79YfQnHQOnCXu94OgqG-AEIBRdZU2ASH0nisR5KJAi45uGMYTIsYw6hGV3l8sUtRQtXkawL5kGGIr-6fnXuc8MskgVHK_kazuePSkK5rzGVgs3EsurivLQ4IHzS1Dayid3rRaF8tpdO1U1Y5TLDPx6kMfBOZoXvCY597VOaSj3xb4uUswxWw53wQVh0BmVjaz-C6VWe-6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=b8JFRawrmtWhOdKsmsbXFn-SFfkGs-lUzu2UFTirslWHWf0oh0PUBi7OSc1ZjF4FNutvoC7qcSe7DcYGqOD9-w8_u2QFBOTwJEVCVzlhzTRgHwx2ZHe7mUAgEwbfX1punn_XK4R-H-eq_dj0xS6_vLgaozhiqH04yhtswPTtNzxsgThATSwV5FpPnotvx5k9ac42h9hgzSQIf0CvCxljVhKtxCmqMhPQLKc4BbbfuJOhyfU8pstNaz1SvxXB7zg0Omk_X6UACzWijq1pXl5VEGrMFjRXF66d6Za1DWW0QkqXqdn30FR_Usurq6ff8sAJKG23Pk4oR0mLbc5ADeuTVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=b8JFRawrmtWhOdKsmsbXFn-SFfkGs-lUzu2UFTirslWHWf0oh0PUBi7OSc1ZjF4FNutvoC7qcSe7DcYGqOD9-w8_u2QFBOTwJEVCVzlhzTRgHwx2ZHe7mUAgEwbfX1punn_XK4R-H-eq_dj0xS6_vLgaozhiqH04yhtswPTtNzxsgThATSwV5FpPnotvx5k9ac42h9hgzSQIf0CvCxljVhKtxCmqMhPQLKc4BbbfuJOhyfU8pstNaz1SvxXB7zg0Omk_X6UACzWijq1pXl5VEGrMFjRXF66d6Za1DWW0QkqXqdn30FR_Usurq6ff8sAJKG23Pk4oR0mLbc5ADeuTVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=d0m1d6SneXomq_N0SadrROc81zbi1T2_j6QTIlTKbTM939VKUrwkgYAs5mAvI7ZNinj4X5UT31YGEdDmACQscbb0DVgs__kq5VZYLQlUvBsO4ai_fmz2hmPfhyQffsALvVivpWylVt9PgGdMyPf3reXs86bF_RY2KpSvuU66uJ3rhRXegnH9XPc4r9kBRyRddz_JTPQHzumZU8D2Sr2uzwLx3UTRHqyNf7BFvU56UFCOsJ05tw_JVS4rZbh6zPzyGdoEGSOJWkqK1enB-XvoJSE7nRIRrfkXN1umFVOU5caLx3nmaTCtmXf86pEw32s6DkOfccFyLapvW0KZ4as4zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=d0m1d6SneXomq_N0SadrROc81zbi1T2_j6QTIlTKbTM939VKUrwkgYAs5mAvI7ZNinj4X5UT31YGEdDmACQscbb0DVgs__kq5VZYLQlUvBsO4ai_fmz2hmPfhyQffsALvVivpWylVt9PgGdMyPf3reXs86bF_RY2KpSvuU66uJ3rhRXegnH9XPc4r9kBRyRddz_JTPQHzumZU8D2Sr2uzwLx3UTRHqyNf7BFvU56UFCOsJ05tw_JVS4rZbh6zPzyGdoEGSOJWkqK1enB-XvoJSE7nRIRrfkXN1umFVOU5caLx3nmaTCtmXf86pEw32s6DkOfccFyLapvW0KZ4as4zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=gpvtUZomPAfnN_blWNsHMBW_zbji6Gw71h0vRukCm8fDft5clA365ktvXDFGsqmxjYOlXaZb8RDNxVabidvV4XP6eU48lg052aIrPHeXlYgxgCevaoGuA-EYPKrCQj3plh7R1ckCcFPm-CfdZf_BCszq1uwugl1OmcZkB420L3GgHvIsRff99mJrN_6WfSu0b2DmIjD9UWZENgrRe7Df8GPr19TtXYNtFS1FMZX_87W6em5h7SvpUz44DE6MdZ3zHN-0uuTFIcT6kXdfUfSDgHaeWm4znZ5ZmEmNTEAbDpbXJVIPfJ5XGc11pa6q0VSCywcqUGlPsK1L7x_cnlU3Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=gpvtUZomPAfnN_blWNsHMBW_zbji6Gw71h0vRukCm8fDft5clA365ktvXDFGsqmxjYOlXaZb8RDNxVabidvV4XP6eU48lg052aIrPHeXlYgxgCevaoGuA-EYPKrCQj3plh7R1ckCcFPm-CfdZf_BCszq1uwugl1OmcZkB420L3GgHvIsRff99mJrN_6WfSu0b2DmIjD9UWZENgrRe7Df8GPr19TtXYNtFS1FMZX_87W6em5h7SvpUz44DE6MdZ3zHN-0uuTFIcT6kXdfUfSDgHaeWm4znZ5ZmEmNTEAbDpbXJVIPfJ5XGc11pa6q0VSCywcqUGlPsK1L7x_cnlU3Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7j6CUTiGEntIOpezAt3-3bm7V5T_jBLstEhq4-pZsBqbUdKQYcJkq_3BAglB2mNOCeqKaMC4AYxDLvgYAazwSo4l3n8wU37dBj62NUrhVNqJzwmfpAYiuhwjpviYaTpbbgYwVHB14sy8YyaCVo9qcwubnnTAu1ldQa2Uzi59Ag9Oi_gNAh2FDuA2GXhbAUu3CYSDAS331HmGc3BGl0tCxeC1yMZJwB0uLuFTyqgNbhTlFVCYTy76ZR0J60sIJAq79R9ZH4_N-GtfIQbD9pFhb5HwSatOUSaYl6STDgsVnUwYESPt5ulv0cgNOfjzNL9AUlg2wkhH2oATJu-C37-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRZtRc8t6Bb2Zs2hLGPav2trY-eHRh67qLqLeVRRxEbcY2cqT9hW9Zf3zn6YEuxzuMinZGJI_niAqmgm4hgqpw2p7pGwYmB_7NT-9c6MULpd58yMjUYjnhoajMlopfPWZmd9ttMk4JMdPivQkNdQ3JxZncAkyt6mrqPSAzr1vwqUZPmeR9UTWzC_AGqITF1lyg3UoZqZgfNChGavmHdv3t8NnqXDYT8KfkNKHP4X9yFexLzvHdyoECKexqRSd7amiV9LwpGtuFDnPWNf66DVNkeZn1hx9VKtU7tO4ALcxj-caDvJdsY3pDvkYsdeKXgTJN3YN58VqvpW5QBrW2RuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=fQfZwd3FMy1M9IvysWCguckxFi6hUk0NVgfPyzQNXXOLGKK2tyw-fDXY6Tqw5O1MQUQaAOjzlE7bfKtM_4Go9nVNyzlpdVL2ujnLExJrNWZiZVMssdp5lYq51lui2lls39aCWyG8fvlj5uDeX_X3MndTyVDTOxmRjRK_h_sw1z76OK2el-DGwfa6ryNR_hmB4uJiXpe9VryOmY2WrQwclEScXOv2WwqrD0mWjvd8utOPvGAROqRay14VQ2vhKCtPFUTBnzbP9Hd0uVG3H-Y9SaDsSn6To6hGW4arEPVZOG-hYNnL0XXMSxGgMY2B5-eL0dXgd75QHc7CsiiIAiA-8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=fQfZwd3FMy1M9IvysWCguckxFi6hUk0NVgfPyzQNXXOLGKK2tyw-fDXY6Tqw5O1MQUQaAOjzlE7bfKtM_4Go9nVNyzlpdVL2ujnLExJrNWZiZVMssdp5lYq51lui2lls39aCWyG8fvlj5uDeX_X3MndTyVDTOxmRjRK_h_sw1z76OK2el-DGwfa6ryNR_hmB4uJiXpe9VryOmY2WrQwclEScXOv2WwqrD0mWjvd8utOPvGAROqRay14VQ2vhKCtPFUTBnzbP9Hd0uVG3H-Y9SaDsSn6To6hGW4arEPVZOG-hYNnL0XXMSxGgMY2B5-eL0dXgd75QHc7CsiiIAiA-8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TIfRa3dhUaThQLtwdxYdAU7D-vaj62j1LWWQ5ho4K4n8Kych-jA9lPiiHI-lbhq37s8p4-7UYx-Za3keoAlarMdS7QRoK0pS8czDdrUWu09O3Zq_vcAuTftlagyMspL4fpNz8m40UQHhdf1pbvTyfLVI0sN6AnxTvefpt2q4vK33aDrK4B54VWXEqF1hk_E-ylfkMRpTl65Nt9L_gd937Y2CIjJYs87UvXnmcZnexngQ6OXNAgMoTG3QagoH8U-fdakchv-eCu-JmNCum2wfvAHVE94i6TfYkg5rtXWAUXSH3YSOB8ijIJO3STsVALWHJuIRBS98d2MFgE1g-SGZMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TIfRa3dhUaThQLtwdxYdAU7D-vaj62j1LWWQ5ho4K4n8Kych-jA9lPiiHI-lbhq37s8p4-7UYx-Za3keoAlarMdS7QRoK0pS8czDdrUWu09O3Zq_vcAuTftlagyMspL4fpNz8m40UQHhdf1pbvTyfLVI0sN6AnxTvefpt2q4vK33aDrK4B54VWXEqF1hk_E-ylfkMRpTl65Nt9L_gd937Y2CIjJYs87UvXnmcZnexngQ6OXNAgMoTG3QagoH8U-fdakchv-eCu-JmNCum2wfvAHVE94i6TfYkg5rtXWAUXSH3YSOB8ijIJO3STsVALWHJuIRBS98d2MFgE1g-SGZMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=KC1kD6eCVSXTDM95DFbl5k1hKbloAyvPw8TL-4PBH-b1zaznY364k7bifZNzVMsF2wvLpKr0BY9PlGE7DtOlWUdZ4j4G02iI_48Y5N3rW-0_X2TrOJJuu9wmSCaWuyyLM7Z_SKM2JbH39yEeLG_BGlwdS8zO5xDOL4JAf0V3euCn9w7tXCUCU7AJ5gIM0YheNP3xVt82VRRyK1_Rm49agOfpZEtXE4TWUlh29JuUU-2PSwMby1NtCphhBpvHBLivAY8MHL4fSaKzFPKj9TNJG9XhE7erWP4eGBp_x7i4eJPJzyGBx003PCI-pQoeCyIFSvxWQGcwwYTNd6bifW3EFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=KC1kD6eCVSXTDM95DFbl5k1hKbloAyvPw8TL-4PBH-b1zaznY364k7bifZNzVMsF2wvLpKr0BY9PlGE7DtOlWUdZ4j4G02iI_48Y5N3rW-0_X2TrOJJuu9wmSCaWuyyLM7Z_SKM2JbH39yEeLG_BGlwdS8zO5xDOL4JAf0V3euCn9w7tXCUCU7AJ5gIM0YheNP3xVt82VRRyK1_Rm49agOfpZEtXE4TWUlh29JuUU-2PSwMby1NtCphhBpvHBLivAY8MHL4fSaKzFPKj9TNJG9XhE7erWP4eGBp_x7i4eJPJzyGBx003PCI-pQoeCyIFSvxWQGcwwYTNd6bifW3EFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6LAqU2iQ6rRq0o2g0sP78U6ZIcuaalOWq2o0HEh8BCS7sdUhsq8wcDF0OfKSQEnGhO2lUmlOvMVdMgpupi5tPTxbcKF3rNXCD8mDM9FQ2D9j89SH6Vc_ne9Hv7R4KPF3YFF9WlC4514SVR8lwEYVcZVkoXVOHmV3bONCaTtr3YK1O8gCN7u21addx_MNbVmuRLRSrQXUnEd9_-wEJ7VFi9RDw-TApdBsMFYgL_RxCXefoN4a4FQeWVrWduoUhnPNUyU7kRKAafm8ubXMlcUaoirL6jnPgFCFYgHfnp4oDTPHp0vHuGsU5PYvE5xyyZzfm8SBWUV4v2nf0zqy-jI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=hyiSOva6qw6Fb0AAr5wRhkiBNzng4UIQ_ZbCS2AMYaWyxrJHrgJkVEUPiTjUlgyH9cN7IhGeGd8ikApkL6PPTAidFWQOaY5suy_t5B9yL1Oc3K0YaHtCmiWv0ChU41k6eVibeA-eXIhiF9W2yiY_E2WPhzAVDE3m9KRQlGYFIcRYLBN1Jwmu_-i5g8HJr8beGMUFBgRzTnZYNMNrz90CA8GxqyrfCiu7t-OoG-9nmpYSmIOyAYpN0zAlq-jI9w9ZdX-fw-9ms73q2hhShP2i2hoFkkHOM1OsHvaCIcLiaG6SZKRrG63E9J216M1dNg3Yw-zishFdnm8HaqH-wKt9Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=hyiSOva6qw6Fb0AAr5wRhkiBNzng4UIQ_ZbCS2AMYaWyxrJHrgJkVEUPiTjUlgyH9cN7IhGeGd8ikApkL6PPTAidFWQOaY5suy_t5B9yL1Oc3K0YaHtCmiWv0ChU41k6eVibeA-eXIhiF9W2yiY_E2WPhzAVDE3m9KRQlGYFIcRYLBN1Jwmu_-i5g8HJr8beGMUFBgRzTnZYNMNrz90CA8GxqyrfCiu7t-OoG-9nmpYSmIOyAYpN0zAlq-jI9w9ZdX-fw-9ms73q2hhShP2i2hoFkkHOM1OsHvaCIcLiaG6SZKRrG63E9J216M1dNg3Yw-zishFdnm8HaqH-wKt9Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=RiS4eNA2DCzn7CPa4WxyAv3NoQRe-Ejx4_1PDd8fw_49vFyq-XoaHOBrCtQLT5otOfpe5la6THDIj4loJ13qENBeISkEsiu5JX6wW1No8DAdxY0YmwIuS3_9Ev8TbcSwK7oqQkHN615VaDQ9_1lMD5ZeSRqy59YW8mei0buXqJTBwRMib8n15W_D19d1VznRfIvkJ9sm5GwYacHVuX5kG9kSeXgG-dQ0j2U5gF8rnfrOwclhTJjO-51ngBXinvjgecYpCpoV45-WBKs3NekFRpoN1PwceA9pFEj5FOI91ZenCyZcpFXc_fbg7aqGUow4-ZpKcemN0HfTy9TRW_GiHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=RiS4eNA2DCzn7CPa4WxyAv3NoQRe-Ejx4_1PDd8fw_49vFyq-XoaHOBrCtQLT5otOfpe5la6THDIj4loJ13qENBeISkEsiu5JX6wW1No8DAdxY0YmwIuS3_9Ev8TbcSwK7oqQkHN615VaDQ9_1lMD5ZeSRqy59YW8mei0buXqJTBwRMib8n15W_D19d1VznRfIvkJ9sm5GwYacHVuX5kG9kSeXgG-dQ0j2U5gF8rnfrOwclhTJjO-51ngBXinvjgecYpCpoV45-WBKs3NekFRpoN1PwceA9pFEj5FOI91ZenCyZcpFXc_fbg7aqGUow4-ZpKcemN0HfTy9TRW_GiHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=r-hMDFR3n95r6ZWKfFtzA94fia7MC1PRajJNEjRP-zsaJhnbU-XFUBAiQ6ipG2DqTHlSVsY8uWzZJL1x7__qTcllCoMa5QhPPZYLDXF4T1ZBZJ8jjAyX-cnXgekxkcTdzu9edIp-yBOZYueF3UxTgYZJez90a6tNJM9oXeaHW-HhGPOCIQoPkcqPqlef_xqx-vepkQ-LOQjCkHPIMSTPVfmhxCp130H9PeFDjojr21mmmycOqBT2qfA6lI2b_0VcE2hJU7M9aUg28znIKWvPnosAfx_oViRSVljBdJqnieD-594VkC00cAecc96AoM0fkUGbBA3ApwNmyDYZXRq5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=r-hMDFR3n95r6ZWKfFtzA94fia7MC1PRajJNEjRP-zsaJhnbU-XFUBAiQ6ipG2DqTHlSVsY8uWzZJL1x7__qTcllCoMa5QhPPZYLDXF4T1ZBZJ8jjAyX-cnXgekxkcTdzu9edIp-yBOZYueF3UxTgYZJez90a6tNJM9oXeaHW-HhGPOCIQoPkcqPqlef_xqx-vepkQ-LOQjCkHPIMSTPVfmhxCp130H9PeFDjojr21mmmycOqBT2qfA6lI2b_0VcE2hJU7M9aUg28znIKWvPnosAfx_oViRSVljBdJqnieD-594VkC00cAecc96AoM0fkUGbBA3ApwNmyDYZXRq5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=JHsLBA9KZENnQHhrEbW_7GDqkuqHsO5TCYISSO2VRGdH2E-xlmec_SvDI_sj4IzLjeiTjbpCd4BhZl2-Y5vbughS9amO4GcKImMT53PWH5JRBFlmO63gzJY8KafC7RjxML4_erAzJqU_HqR40vLe7eRBB4t04gVLxWe20XM8jbrmC5OX5f613bclfMieG9ptxMcbVPd_fa1YAu9VmX-B09TMwa2q-YiAWOifm042b8EgmOck2ou3q1HmmpkPWYNXmL9K-KHerxnOTkIkGglrD_jOUYGImUve7jxbrkrQvcAyDaK_OrJjqsA4JdbPW4rf4sYy1gZDMIKwSkAhMItpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=JHsLBA9KZENnQHhrEbW_7GDqkuqHsO5TCYISSO2VRGdH2E-xlmec_SvDI_sj4IzLjeiTjbpCd4BhZl2-Y5vbughS9amO4GcKImMT53PWH5JRBFlmO63gzJY8KafC7RjxML4_erAzJqU_HqR40vLe7eRBB4t04gVLxWe20XM8jbrmC5OX5f613bclfMieG9ptxMcbVPd_fa1YAu9VmX-B09TMwa2q-YiAWOifm042b8EgmOck2ou3q1HmmpkPWYNXmL9K-KHerxnOTkIkGglrD_jOUYGImUve7jxbrkrQvcAyDaK_OrJjqsA4JdbPW4rf4sYy1gZDMIKwSkAhMItpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4uxdnzsshmZe71f1cESILo0xPgRXjF7f7b0yhOzRw0VyNoX_tgZ8EIFbAuoTNjOJBKPoefYEgppl44QNKmxDt3QOMTNFPtrzO1DfHLAOuJqMSG0Myn1IqC_UxXVzf0qCv6SOrqSTy6CiFmEofP5570A1Xbs-uZ-ME_BtVsFzquzuSJK8EHxD6QcJ3CFG4446IqMT-v3kPHRnuYPT7G7AdKdueyA32LOnMJeNlshLCr5pH0aZbboXbQf6EyoqNEM6fOTG8zC7cH4A2y5laXMRwrmW2bcfJGeRaTKnHBE9GeOZX8Tac3sGyNm0WhUvRLjfboN-JNS1OI0fRXRqAizDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=hlvARuSsR49UmA5u8R1HIV5_CuxEe-SOZWzosQsn-OlmFe9rtxfbGaMX4ouykKif1MYuoGBVz4pm9cgTNS7wUWppCnQYHL0RcdOvtOWu4YMFptnxRChyQoO7c8rAjz8WU7iXY-BvUfnXLrvLxZY-zfjYYTmarRWN-5Qt2aoqmwNZYGO8EedZyiix4QaooOqpP39AheFIoLpzKgyV1hXA0bSjATVE0keFGIQG8ag4YfMNN92_1Wi0JHtoLnxPOpqe24vDwDVOBlJ5GMGM1L9u-jPibWEzqJ2f4mVdrJnNbBQT5teyOk1sUjWtgLhO7uCy5k9vL1YJjqOOsntON0lgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=hlvARuSsR49UmA5u8R1HIV5_CuxEe-SOZWzosQsn-OlmFe9rtxfbGaMX4ouykKif1MYuoGBVz4pm9cgTNS7wUWppCnQYHL0RcdOvtOWu4YMFptnxRChyQoO7c8rAjz8WU7iXY-BvUfnXLrvLxZY-zfjYYTmarRWN-5Qt2aoqmwNZYGO8EedZyiix4QaooOqpP39AheFIoLpzKgyV1hXA0bSjATVE0keFGIQG8ag4YfMNN92_1Wi0JHtoLnxPOpqe24vDwDVOBlJ5GMGM1L9u-jPibWEzqJ2f4mVdrJnNbBQT5teyOk1sUjWtgLhO7uCy5k9vL1YJjqOOsntON0lgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=tPyzVS_m2MxHmEFVzK85do71dhIqSMrwyMknGItG25TM9li6FYLABjWKDj0W-pARk-8LP8plWrzsNg_jGHaJGw2Dk0UqFA_AkM-S8KiYREOm31E_Vr5RumTmVu7Pg7ENlzim2oFtwLGHwUbc5Iv-T4a7-41NGqXiS2iEyLfzuPiEQ62A6Y24tjHnl-JbFH1wbN8YuHn_PeIFf2xrxlP_gnAJds8-EtvZQ19fcT9cd9mohLHkGSp2TQg_VsI_hkyQcWoBnqQtsnE82G1u67GZ9jVQAINCR-ECh5v5YkRULa4EPZN3sMqjaqm2I8BVcc5kzM3MnA3nPtEmgoXtTYN0pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=tPyzVS_m2MxHmEFVzK85do71dhIqSMrwyMknGItG25TM9li6FYLABjWKDj0W-pARk-8LP8plWrzsNg_jGHaJGw2Dk0UqFA_AkM-S8KiYREOm31E_Vr5RumTmVu7Pg7ENlzim2oFtwLGHwUbc5Iv-T4a7-41NGqXiS2iEyLfzuPiEQ62A6Y24tjHnl-JbFH1wbN8YuHn_PeIFf2xrxlP_gnAJds8-EtvZQ19fcT9cd9mohLHkGSp2TQg_VsI_hkyQcWoBnqQtsnE82G1u67GZ9jVQAINCR-ECh5v5YkRULa4EPZN3sMqjaqm2I8BVcc5kzM3MnA3nPtEmgoXtTYN0pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kht7_MaFqgaZGnhwY9R71btFk3diNUqbq6Y6ypgaFAFU0O8JA1gX0sw8vbUH0RDWayD56oq3Q4SWO3S_gQQjrnq8KpzviLdGeNnXCmQy-aQKay5w9ppYU4slQhiiw3Ogb0cjx4vPVkqy59O8x06Yr3HqPfh7bSQSj1GfxXZwBxlCojHRjsyhpSK-1UcASY8MKPRtyo6-DKlvUXn5jFoXmcCLMgQWyOMH4S5XCw9xdLZFsfKl1CxyDNqFn8zV_-1K5h5QxitkIJUhb-6-G5dykOKyDoe42_vXKLYBMUTFqsnst1H63qnmbrU8PIAIZnZJVRRS39eb6t1xkzkafMibZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=g62TmIqiZIENKuhid7RDeE9gY38Q-x0Nx-6KohmVEbXI7JjNQp-E6IwsATo-1JhRmV_XwCsHb4ZNFoxzK2CT6bo4yzyDDxVM6rVLNxNiVAtCEEllloSgvx4fMB843a_TL5OruJbbmGYWN_PC4BDbXIr5zJvhCAC2ayVz7gNV7oq0ZAq6dmB2NlVN9OF7OWlIiiI3fVVgivoT3M4I1fWocPlYBCoWI0zSX7Rdqc3pUGk3S1ohXMrfs9f_MmdkZk5zEAjRFdd6Dgz65xfd0611t93x4fx0hTfyznw-S1VT_pyRhKc28kTXxMSbkz3TfiY1h3iQNdXshErXxvVcOW0oyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=g62TmIqiZIENKuhid7RDeE9gY38Q-x0Nx-6KohmVEbXI7JjNQp-E6IwsATo-1JhRmV_XwCsHb4ZNFoxzK2CT6bo4yzyDDxVM6rVLNxNiVAtCEEllloSgvx4fMB843a_TL5OruJbbmGYWN_PC4BDbXIr5zJvhCAC2ayVz7gNV7oq0ZAq6dmB2NlVN9OF7OWlIiiI3fVVgivoT3M4I1fWocPlYBCoWI0zSX7Rdqc3pUGk3S1ohXMrfs9f_MmdkZk5zEAjRFdd6Dgz65xfd0611t93x4fx0hTfyznw-S1VT_pyRhKc28kTXxMSbkz3TfiY1h3iQNdXshErXxvVcOW0oyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SdffKCVqHGnGpmJJnZFWz4GH0m1T8hihBVkUA04J1d46sco89Xr9Ic97G1HUsLE3lWKSKKIzi69WLtjdyD_vUwr-R7z6lVl866Ap-Dj5G8AN1Cq2JFbMuf0oQR2p-XS3pTbdCcPs2BhfTgz73A9ZeUfeQQCEbgvVs5MWWVHD5pckiSxpU3-JfFj4--1p3vFVAu5lEzeuFf06c3jRFKlGFvjPaQMPUURWdDtsCSg6tak7e6S_cra7XraJay396MqRHJVxlIj7hJCp3BaxQfxXYKpXkMoembXavAr0ezPJtqO7RewwYyaX5QOeirq18LR1GPmMlh2PocfzMshFGAQ_Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SdffKCVqHGnGpmJJnZFWz4GH0m1T8hihBVkUA04J1d46sco89Xr9Ic97G1HUsLE3lWKSKKIzi69WLtjdyD_vUwr-R7z6lVl866Ap-Dj5G8AN1Cq2JFbMuf0oQR2p-XS3pTbdCcPs2BhfTgz73A9ZeUfeQQCEbgvVs5MWWVHD5pckiSxpU3-JfFj4--1p3vFVAu5lEzeuFf06c3jRFKlGFvjPaQMPUURWdDtsCSg6tak7e6S_cra7XraJay396MqRHJVxlIj7hJCp3BaxQfxXYKpXkMoembXavAr0ezPJtqO7RewwYyaX5QOeirq18LR1GPmMlh2PocfzMshFGAQ_Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=K1TEyIr57J4hu1GqweUC4nf1euasADknbqro1g9297UknjIX9uDreRPQVwSvGt4aoiuOd_cosvd5nN_P49Aal4dErItwEyN5OiL0UdNKDw2oN67sPVdG-HCCXNCY2-_To7A-Y1L9_0wwmCBOQFqayqxVK12PjXbkvTYERctPOjfbDxczF3_K8frEghBsTa-J4UQLuqPx7y_QSLClb9_grEyLu_4puE5dnAmfmLX2KpR0cOmILkVMmhwTjuAkmXk-p4YLgcL7dZvhcAQ4W--8i-73f7wOZzgal7tnbXTRRu2br0ZHK6OGzmBz6sq-sv-K_nWDbbPyBAdxKeRFMQ4kZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=K1TEyIr57J4hu1GqweUC4nf1euasADknbqro1g9297UknjIX9uDreRPQVwSvGt4aoiuOd_cosvd5nN_P49Aal4dErItwEyN5OiL0UdNKDw2oN67sPVdG-HCCXNCY2-_To7A-Y1L9_0wwmCBOQFqayqxVK12PjXbkvTYERctPOjfbDxczF3_K8frEghBsTa-J4UQLuqPx7y_QSLClb9_grEyLu_4puE5dnAmfmLX2KpR0cOmILkVMmhwTjuAkmXk-p4YLgcL7dZvhcAQ4W--8i-73f7wOZzgal7tnbXTRRu2br0ZHK6OGzmBz6sq-sv-K_nWDbbPyBAdxKeRFMQ4kZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdLgmJ1QgtgPdEOvFJxJmicchH9TMiuApvNy8UdEmMg8OAn_ZsxMgGTZS8dhhckluT2XBBFw1_e5kIfWw7_FWYl0eMXeeOp4-oACS5AVsIjbkh7Zr68c6m3xiyPTlrGQfB59yyWO3veezl2EjYTWcU6J8IJvftzfzRljoiga5ebp6189UVsm7G5FWdFOE72xVCH-GoG0wx_SyJZgNdJIusJ1s4XKK4irbtZAAnXMJIYqX06PZEDIBCUMPDQrTpfHqpmajBLB_SkyXSxNHgOkwOZojrVxJY--4FUIq4oUG9G1RHEIxM9K7UUZlAlI0V9zZKzXtxD3DU4JXn0-3eRsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sh_PQwXW4i4crmuLW-OJvGrGaGiT7riswnOvw_sAknmRYu2-AZsfe1HZG3CBS8WtEcYHZNFBaEE79l77CKyN7xM36xuNm___vAmm_PSPbjSNalt5H8BxFFvT9ZK3eVX7rk9o7M3GrcN1xUtbP60Jooif1_5JKU4xT8LvLyHFTjpSZq2usKwI9Rdu0hy9aO3Pw3eQd2Z63R9k1pteX0X1JyhCwnhXVeFEl31oFoRa98iA6O0xtobIqemM_SNlQ-JX1yD7XWdejIfDRihNeinXl-kwWPO5XNudo5Qsn-1NYvVOrd4aGFWizWQ1XkSd8AM7VvnwA1Kav0xHVPiRxcECxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVQD0ja3Yeqm0V6lr-hz2vuK6QMqj73oCj_1GQmcXWFsN6couJTpRCLg7HSvGD-nvnhZFNbKY7twIk8KC57CqxxD3w13IJRqawbGN3JL2dqs3NWRwVAvefVBhw7mbt2MOT9sGV9LnrXeX9vrMtt9dFdwYf2odCnI_5Bbkli8ve_qU3TpXcj5RTXf2ugcYYFDRifECX1_oIhA21e8ZNF0wbHWvFnwRy2WboH42c6Vw0IQU9EA43VEngYgiBwKuQqolBFbz2oEG9zIi6PiWbuyhXpaFVGmj5EhoFaY95-skBwAGjbFHZix1KbDP9Rf7qDM6EBdhwewo_6mt4yH7ffZpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=AVEp_fgfLOcEOHS-oyjMXgaSt64Wkzn7CjHj5LMJPhb71jrVfGRBcqOOmVWG7ehk-TJj5k9l3BF_WtJNGIkcf4UMt2ZZvjJCFkqcRYjUhLWlWVgjqK3Ya9rwJAULk9qS9sXLxoEHKggYdZYFLE9H9bKlrPudWeETUsMBRhPp8VNiXhDCXFCmBQrkslUfqk-65QbHebaLFm-MkurzJ4zpv3zxe5Z6IjcCvZBDBm9910DIKr75007JAV9dtTO7ZkvcfQQgbtCgaYbh1_emmOtI5kN80Dewrnwx0wVLEUY65mcLrbIfJ4K8AnpfcPAw6dYZqYluxQxWJrNpfhX8whCKmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=AVEp_fgfLOcEOHS-oyjMXgaSt64Wkzn7CjHj5LMJPhb71jrVfGRBcqOOmVWG7ehk-TJj5k9l3BF_WtJNGIkcf4UMt2ZZvjJCFkqcRYjUhLWlWVgjqK3Ya9rwJAULk9qS9sXLxoEHKggYdZYFLE9H9bKlrPudWeETUsMBRhPp8VNiXhDCXFCmBQrkslUfqk-65QbHebaLFm-MkurzJ4zpv3zxe5Z6IjcCvZBDBm9910DIKr75007JAV9dtTO7ZkvcfQQgbtCgaYbh1_emmOtI5kN80Dewrnwx0wVLEUY65mcLrbIfJ4K8AnpfcPAw6dYZqYluxQxWJrNpfhX8whCKmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_yT6beYTKts91QnrNgupDZBAl9NwBlXauUchU4Bo_lhXUnLn4rqzGb_AoYIR_f-gQuOjKSObMC_LHMy8MyjM7XE57cD7ZAQjm3cyl2XIkDR__fQOHvNYCoSj-mHe5Ru1MIQyu9nCXJm3ryWDFS4-Wlgb6NmTpqbGIZNP7bfynp8fRoujU1IxMXx3rG5ij02MKuKZrOPJCLmHAJDm8LcpUUrrRxC3JmL-8-Cj10lwNHZwTkkPEi0hH_wWwa_SOe8gLm3Jxm3sMZHwtBR43fOFuL9Me9Ho97GPhY0x1SyrDFbSoKHZYxbUySrIAmOJqi6x-01eSOLR2PwQ3_t-zTp06yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_yT6beYTKts91QnrNgupDZBAl9NwBlXauUchU4Bo_lhXUnLn4rqzGb_AoYIR_f-gQuOjKSObMC_LHMy8MyjM7XE57cD7ZAQjm3cyl2XIkDR__fQOHvNYCoSj-mHe5Ru1MIQyu9nCXJm3ryWDFS4-Wlgb6NmTpqbGIZNP7bfynp8fRoujU1IxMXx3rG5ij02MKuKZrOPJCLmHAJDm8LcpUUrrRxC3JmL-8-Cj10lwNHZwTkkPEi0hH_wWwa_SOe8gLm3Jxm3sMZHwtBR43fOFuL9Me9Ho97GPhY0x1SyrDFbSoKHZYxbUySrIAmOJqi6x-01eSOLR2PwQ3_t-zTp06yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=u0KZRfUVf28pr2rDQ2mj0HHlR72V90rkgmTl7pE0IRSMjUmoHX6pTPwwBnNBqbobKBymMyw__YtDLCnVzrB1_Lw-UodGcDl0Gtd11xAf-888iptlE24QQNFezT3wo5T8Rk0eIQZwymKNckQQXRi0s7EicXOAd1TY4qHZ1ah9ss98lCE8modLGaPKj91rngyUGktig6LHszx6LMop4q4xvczMQnXDamhMpi_3zOeoFLApVBJRJGQamPetU9fdPvfkcBfXqT_maKjesCLBN7ucg6Y95RAzKehBbGr0rWDcyzvMZZHmXQx_Ov6ePOWg9eT-iBJSK8pSAR92koUKtcyu5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=u0KZRfUVf28pr2rDQ2mj0HHlR72V90rkgmTl7pE0IRSMjUmoHX6pTPwwBnNBqbobKBymMyw__YtDLCnVzrB1_Lw-UodGcDl0Gtd11xAf-888iptlE24QQNFezT3wo5T8Rk0eIQZwymKNckQQXRi0s7EicXOAd1TY4qHZ1ah9ss98lCE8modLGaPKj91rngyUGktig6LHszx6LMop4q4xvczMQnXDamhMpi_3zOeoFLApVBJRJGQamPetU9fdPvfkcBfXqT_maKjesCLBN7ucg6Y95RAzKehBbGr0rWDcyzvMZZHmXQx_Ov6ePOWg9eT-iBJSK8pSAR92koUKtcyu5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6NIX9ps8ILaUJxTcozBVOmwKPCKSa7sHnx2btzr8PMh_RUHoV4e2i8ZgtDjViCbTnietfSfxhwI6tBbo1Ybn_4Nk15dXb-N-3wgkVYpK8P4vUyjhfTJYlyOMQ0GVuh5AD_Q3cMVTp33C6_dZu8ls3WBZ2VJvfprqX1bYPXa1LTWeh6kLB3bIP8uxsepoGp9WX8Q1WN2skwiXDtVaHJGA-eWFPK6VK-rI5vdVwGQMBEMRTkDDgP-j0WLtDdakNjc10lUy6QIrPG29Ax7otin3ZESVf88LHMpvd8Ylz1wF_2fElk5iOgEeCSaYu6h5cRX2VqAH5JeCqzs7hAS8SLrsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuToT7U8IIO0OWvTcLSnpJUPTxUuA8uLwmNnArafWnKgs5Jg3sdBb6YMwxfY4WxzMc9VrSXNmKy-KtU7KqM6N4vZ0Wa9dSHSypVLUNuH_EzNVRIRTQ4Yk-JnfKBflNXeiQ23LHlTltHkNRGRkp9emqAnVYBXgZWpnEqASc6QiC3RNwv5GfcCM6lblacalR7kM_xzXKkow4HBftVqpzJlOq_tHk2ejMwNdNVyLunALEfBvIFwI7crk2ptq-q11QOIa8zi9a-0FjinHDgsLBWWNIr_dGBeoeuyyXrdumrJO9wVtU9g-a-2JTUFhy-jci7kAMJNoceqT0zhS1Em2GjKG8bGs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuToT7U8IIO0OWvTcLSnpJUPTxUuA8uLwmNnArafWnKgs5Jg3sdBb6YMwxfY4WxzMc9VrSXNmKy-KtU7KqM6N4vZ0Wa9dSHSypVLUNuH_EzNVRIRTQ4Yk-JnfKBflNXeiQ23LHlTltHkNRGRkp9emqAnVYBXgZWpnEqASc6QiC3RNwv5GfcCM6lblacalR7kM_xzXKkow4HBftVqpzJlOq_tHk2ejMwNdNVyLunALEfBvIFwI7crk2ptq-q11QOIa8zi9a-0FjinHDgsLBWWNIr_dGBeoeuyyXrdumrJO9wVtU9g-a-2JTUFhy-jci7kAMJNoceqT0zhS1Em2GjKG8bGs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1EGc2YTFKabGZkmEoKVLatC__UXDbLUWen5AomLe1nzdlYSV7OKJGRs5YBWNTYctgY28z7PaYuT1XD8gQpvtYHD3GX9yb2ftthnCMQ4ThIV3bL0kPUho6LnWiwfINe7Tw8WfS0665RDW6jaFFrbMPr9fjOZZzntoCgEOBvxRWwvI1aqSa17gEh51FXc6URc45FpPLpl-Xi6wmktMc7CPmje3w0OvMhidBc_BwEjD1MBPQfvfcYM76OWgMuubUcC74pZmPfXIkzG4wOaW-unUXLYGQDwRuRW_8rGR_xS8o5el9eWni6yG3mbP64-9hZ9h70eIILuE-9wF_k3ps2h_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ti8cjl_y-H-_O-z1ctIkUVimods0ETxeqjswUHVAEThB9HaVfdCdE29GnGvHbeeAguXwAEO5ReHELhWpIvvINz0UrA4Ztg0ZGYi66zDWinu6zhucVxPAghFLqzDHpZdW0h5Ahhcu9a4SCFZwZwLalm6yoJkRP_XQe_WYLwigGPaAumkG9baeLeLWWKGq4bsHvMi0XYr5rjmuVRlfVVdWHoJKKP2fiQkOD3W2VXRYxK_fmAyMpYgyM5z3kLMhsuUerQTC2i_bsDdc7yPGL2H0hfhGaGiHwz4Tyn67yHlTN-nLzCApJ3sqnuFWY1LKrbpTh0kKxeG_3p7_3ZVh_7eKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=ti8cjl_y-H-_O-z1ctIkUVimods0ETxeqjswUHVAEThB9HaVfdCdE29GnGvHbeeAguXwAEO5ReHELhWpIvvINz0UrA4Ztg0ZGYi66zDWinu6zhucVxPAghFLqzDHpZdW0h5Ahhcu9a4SCFZwZwLalm6yoJkRP_XQe_WYLwigGPaAumkG9baeLeLWWKGq4bsHvMi0XYr5rjmuVRlfVVdWHoJKKP2fiQkOD3W2VXRYxK_fmAyMpYgyM5z3kLMhsuUerQTC2i_bsDdc7yPGL2H0hfhGaGiHwz4Tyn67yHlTN-nLzCApJ3sqnuFWY1LKrbpTh0kKxeG_3p7_3ZVh_7eKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=alm806Rs4HBk0ZnUC_UqDA20eFnAP_BT0AqNJau3hdGwsFsmQfg32tFxJNGFrMpqhxbAKgQ0tNMUBsCqC7fOBmrATqIbB3jxTAdzfyH3VIJADec70nYLQKhgFzKr3ZOumh_ZDZ1DbdwF5gKwvr5he4TKR1wvsoAP0SXHsDFpocIZzf_WVzPdjLuCCzXIkRmM6n5Oxvo1c8eWyq9H0B6j25uOi16KdwUVkbhiEBLLL6U5ZdkvgCD1orobj5zxLjVlw2ogV2jnn9wChenHgjjXFsgY8tRd4uhbmnFMcwKTVo0IdJzokCueYlXyqzI9e-y2VmnJLGAP3B7XWoPbHhLliA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=alm806Rs4HBk0ZnUC_UqDA20eFnAP_BT0AqNJau3hdGwsFsmQfg32tFxJNGFrMpqhxbAKgQ0tNMUBsCqC7fOBmrATqIbB3jxTAdzfyH3VIJADec70nYLQKhgFzKr3ZOumh_ZDZ1DbdwF5gKwvr5he4TKR1wvsoAP0SXHsDFpocIZzf_WVzPdjLuCCzXIkRmM6n5Oxvo1c8eWyq9H0B6j25uOi16KdwUVkbhiEBLLL6U5ZdkvgCD1orobj5zxLjVlw2ogV2jnn9wChenHgjjXFsgY8tRd4uhbmnFMcwKTVo0IdJzokCueYlXyqzI9e-y2VmnJLGAP3B7XWoPbHhLliA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=SPeFKYs-QyNXi9kF4SxVGOt-rM0GhrQom4VlJNNXEgtj5hjQ4WrGkaifZDvCYt6rWmb3-VBcfS5s4f23PVNEDX89uJZWEkoVyw5cy88eI5XnFSQbo72P4xOdFG7q72sR_27C83HwoPrrvSfigY3T9r_8fe4Y351Jj6ibjMxMt-1nVYII6DSzCbKbaxNuJYVS-LG4MdNkkViClReJGifbQ5vD1gikuxwEok5mQZqP8e7fFQ5yBB-55KcRtsyI_cHPe7-XI0YkK5Xb1e6_vAj0mC7yHeVoL0wCB8E_ZgTxeuWCYYhCFoM2_d3K_2enQN2NNt-WqGK4BQaEPZslhWkiXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=SPeFKYs-QyNXi9kF4SxVGOt-rM0GhrQom4VlJNNXEgtj5hjQ4WrGkaifZDvCYt6rWmb3-VBcfS5s4f23PVNEDX89uJZWEkoVyw5cy88eI5XnFSQbo72P4xOdFG7q72sR_27C83HwoPrrvSfigY3T9r_8fe4Y351Jj6ibjMxMt-1nVYII6DSzCbKbaxNuJYVS-LG4MdNkkViClReJGifbQ5vD1gikuxwEok5mQZqP8e7fFQ5yBB-55KcRtsyI_cHPe7-XI0YkK5Xb1e6_vAj0mC7yHeVoL0wCB8E_ZgTxeuWCYYhCFoM2_d3K_2enQN2NNt-WqGK4BQaEPZslhWkiXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFdGdAXOE1Dz_4zEjJi11lOsIk1j1rN0E54bQQ8KHXxrbA49ApyYTqhNOHGK2t0ohfw_Us8nsjz4EzqkUmZz-0thEab8qtG3RPMHcU-5ussfonOsYLzGzzTpqPh3CIuYF4iIX2xLBcnb5jYg5x-YnZRxswnM-iP2C3PbDHORSoGDlcGSb-jIcEPT4WNyL9tyrTlJWkx6E2WUKUbR8rm-UFdl1kAaHL22zzBTFcRpEba1LXCRJA1NdvqboQwpgOB6dKDxkwz2rZHW5gvOsd3aAsPGqSdU4HttJz7zDbo37SK0C9HnqX0Ygsg1sD700rTqlXe5SV8P-Ow-EPZ_HlVZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQZXwmz-7DK7Zxt6XSyzPizKnv9Tf7zvOOIrzKnDPMKuAkG7BUUQaHJJsB3cCdZuf_5hV-rGFcqIHK1Ot_Oj7afRwJb5QCrXCc1q1iGWO0i0H-WvtBXHIqEdYLmorcK6WpVsh6qlsy3f5pTQk3VEODUbtoykoBmO7L2LHcdGBfi13y-DXq3MlVpMK-olsly3H-B363k52-gzyeDesPT8AfsqkB0yY2thtz9xpVVaqx0xcN1x5ujVaQ8PVE3q9fEi4dDiJtI-uZoqsyyBkcD71oCSbEH4NzZfmrWfW0eF_6h2EOM8OTMhPzALfcqrHbs9mtpxn7NoLMoIRg-1A2rvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Z6kNhx7yi493UJHyQQKCtPBYSC7RNKom8v0Bug0SzlirL_M7Xs3JkS8btpbDO1MtUF6lfYpZ3NJJ_Gve49od7wkcWkOjk0Eq5KTvAnAR6zrXleRaj9F840YYxjUOq1_Gz1LmcwW7WcjW-u3TCmmBLiYAPb1uzMftcI4VTvO2CznRjkwx-BoTy4NZ7FHcnO62BzYDXicZoA41ms0PMZ99lEG7L9DjlEhJC9_0qK0DBwvIiv1UZ9CTzYgOyvFhhoX5l4U8CHKrYw2HpQJB10oFocFohyoz1NVSAn6frb_4m_mbYyrK90xVfNCbedU-8MN6CVAyd_Nz2r0fh_sWpCN8iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Z6kNhx7yi493UJHyQQKCtPBYSC7RNKom8v0Bug0SzlirL_M7Xs3JkS8btpbDO1MtUF6lfYpZ3NJJ_Gve49od7wkcWkOjk0Eq5KTvAnAR6zrXleRaj9F840YYxjUOq1_Gz1LmcwW7WcjW-u3TCmmBLiYAPb1uzMftcI4VTvO2CznRjkwx-BoTy4NZ7FHcnO62BzYDXicZoA41ms0PMZ99lEG7L9DjlEhJC9_0qK0DBwvIiv1UZ9CTzYgOyvFhhoX5l4U8CHKrYw2HpQJB10oFocFohyoz1NVSAn6frb_4m_mbYyrK90xVfNCbedU-8MN6CVAyd_Nz2r0fh_sWpCN8iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5yhW9ONRvU4FVNXCMIEoEHjFBkCqKZaI-mV-O-ulU-INetqOzY0bp9IZP8R766V_7vBV_fFavbM69-G_bmzC7VXJ6tj2BSGZqdqxScVhHMC4VrLtcWGONyrJ84Qeirp18_8Zw2DNP1TLXcV95cTEIs8LrobVuRM5s3BTZc4e6q41-kZ0jwXELp4w4J91jd0TylB-xjwhcOkKPJUvzWSBQe_KTRqzj4BX1UQ_t7kL1_iWDHGyzS23mn_3H_T6ktetVHiy36HY_ep8zQ_qBnc9M_iRSV25BrTKeqS1HLZ2zRvFzVg1-GbCL9tMBn1d1LDusLUzOvKP2y2AItA3_UNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC-RoygzksZ5e5oA2_EW3RNMiRh9CovQeocuqzu_N0yTprKAduPcRurVgQFVgDzwmkTKjCxGphskciwQ34W5m2Rf5u3UfUNdB5sv80FOGakw0oqAZb0DPyLtQXLeNEBSGC00mOr7CDLYhxVlvXtwhRRhdlSh1mlL4MevbSWraF5oCDnvshZ49EBlXOvEOabR1vm3PNBP_HFrD2nWRNYIQnpQ6iCZjA4pFfw-WNJ8dvIL0KEQvCq4oCArDNuChJi4Ltn7VkhGrcDzYkL5OHsKV-J50yIiXC2DKGp_OzC8hlFSA4gvFEtQDd8luv14zE1TI0UImNm0NBZ5ODOxFglMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
