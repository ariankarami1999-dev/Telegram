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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 19:08:54</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXxSDLlUePGQsu6_bHEPLaz7rerSO839oNpE5JzXuURKpLtG1ehiTDDqAI58tbtaezQTzTI0YvGWknhYJxP3cv43t65JSviH0rhlDsupU8KLRifmakRQWpOwabJAa-IL86VCvUEoH_2nPexnOeBjuo1s35L7ysIWf5rT6mRjUxac51Q4vtUrfberdinlpAGEYDWKGyGdQrAKhijZGz_HCyTtKtFBIYUxR4r-F1QFUiSUYAFjRPPJzcP5PYSbNbzESqt9fSL_E9CGprvMjo590bxhismlq0oVl3ySAdeEuLt9mCNfwC2Mx31TyFrVAWqXAibFiqem1K15fSRaux-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOCtdJFLrQqXtr5SufvaJj0lqt5eedm_WXk1wouMVONWT8ZYJ1Gw2EI1pBPuKr0n2JPn7KKjJ5ozC6ALmls1DvjHblejDMLNPvaqCtMi098-s5paOlgEWCakDJNCVxKXRfguGBvASqEkq7gBBlYA1UFK1-KlHe8QyvkVtdrQVpvZx6exRjnRrcuqdHof45ECV-yO7OVBBWyoQAVVntbeHFCXBZfUdHVKHi3yJunG5QsplaK3Ems1gRl4MN_SYvv2FKLayxeEFBAMnBib2DbYYQM-i4eda532XrlEmTPKdMuzGvcQ5sSyPuzvWd-LjFl73Zp7eLh9sCCu3-WiF0ZgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGvV-ZxXox8uBdBDX-aiRVo_EkpXo6B5mKz20Fp9-JI9e9iVIa9P88-cz8Uo_gWx3wRWreqrrvS-xm9OpqdUzoy_rPCxvTDkODxR0qG11z-hf9TNIqlJGLNy2CaUvgUhz1qxFFxFBSEA1CWxBQN18D0kOM2U7n7vU_ODylLC6vQ4gOFr5D7vvz9QDIneBh1HzSN4eWgsbCvdMMkzFXY7Ko93TnuIDoFedmVCmRBlx_5_O1ZEWK2ZBKfjFTcnxky6lVZXh-i58_1mS1pOybDPZzs2QzaLAWcN74pFJQTqPI1OjvRcuMfL18bdXB6FUsZHFw5pxSmrH7bEYvOA2ZVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmvYvwNrkKmD_sh8au1AX_xB9Hnrs2YvFi9hQTK27aXX3D9-nZT5OfgXYq3P2hqz_udCEIzOzUHOM-R6OHUhhiDY0Nc7-3ppz6p-VfYGA-Eb7gSgQGEPwEpuSHxr-FYaGmAaeTn5arGNxrhEk7TbDpmSixtxOAmiH4QL4eaeH11xJpAVNRWtxh2PBqqh3CQwwMB0KZPn2m-FjT6iGlDg0wpZsErW5GE5kkY0gvXdTAQtjDRjzwkLhMN0q7wvlchD1TO1nW8a8l5tUM4DVkzE9WJu1ag7Bp709tdYhsVYQkA2wC8-eBsltGub9VoeWD1AQZimSn9a4tJPOcddRY9kWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5TWc-vGDHZ67yrpwin2mUo36Vqdc2Tc8Tx30lMjD4NfdI8w-_jamsCJ04vfWdAC0LS_jx3yIulIhTCkIE20vDk87DUHrQQX5ETjn6TKodhiAE44KR6Vn2ZZWhhY009UFwSCM7ulqhZ6eaeva6_2nizoDl6AHrWvWpSn5kCepmoScDimTSiuPQdzXZAZXDzcGcjnzL7SKcV_Y1r-xnQ5wDrma1QdsUt9iYeHEGGd6SciMp_GxCtUPS-zRfeooVop7EUy6mm0W8idtgFsQ_UoQdCiSLAe_ILYyZ2-oANJ05V6Op5tCMhlPK-qQkEQ1UAtqfkgqZie4q2oyLJAHWKKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTaRLQMXiyVT_26SjZLnoesDuh9N9lULzv7wUov-dDWvaqit1yfMfwD_bTXXZRqCOdZofnLsxdjlFH4QXnXbcp5Yt4X208O-Lin3-2wlVEAGzW-GB3RY7ZQHHwcUDTPhSxtnKwaiADGwyc-WQuFj90DY4_6dHnneD15iGs5ta56SFz_TLOhFQegiy8oMjGWFRx8wT7KcHt5Ia3bRHp0l5oxVZN9HrLwrmU6l92qpoQpVZgEjCUKXJiMXvUcqgUgiZiIeEuMXmDpCinEVwTCkGL21THPn4AiN7WSMM2m-hwteh6FYRNfn1wXRc4wua2-8qcNuAGRQlt_lh1HRlMeeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DehDnHEQLxKJViIQHJJ9thHBSBglHjatbEwxynhVs5RZVNF7LP0Exg_poMyR_ZU8RQthqyzYcGvQjPz5CNppEa4fnsFBZZDLnWHZ4Y2Uz7gozzzcOK4d1lbE4YZTfNtkHmfYK1SvweIdGJyotS8XDptFyHCvQDKgiEW1ZrjL8XYxDBfv6-GXb6f1Y7i-LWj6DmRiEmiQlDMkVFn6rIbS6MCiY7jIO5PYcINprEm1zv1LfjO9pstuFdS5WOQ6JMTLECR3WDasvr6Grf1q_wAuB5aaXWZBiAZ0RYC0d5NGUmzFcoho8torevHEEjYZLn6Q9ZzjlEkNTKaIi7rmYxtagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhYa30e0GmP8bk_E3znjbCYXOAhnGF1elybGYwIB2MkVBJU0O-7p3WpbEYzGlz6xK_bFzZdt_xce5lSlgzBWlKyagnOu1GszMw0bYKZkRIMRH7OMgjCSHoYjFgnXiaZeIPbywoZbdy8dKe7-aWt9tc3n52ZTbwXAT58xu79AFHYpNyMGo-oFWGFNshU0-6tpU_e4-tgnhHms-_pHptm1ekO8m_mhMK2QIoS_y0aWtj6qUVa-hgTV5TyKrUcUyKE0zDoNgkpT3NbbSV_ygru_xpJ4wGQh_pogC08ngr0zQ28zAWN2SdSAlvYSqbNKupljq-7dNaXF_lJcJcQPAo_4qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NreGk7WZzrDQQDw1ZIetjmkra60T0pqcL43xpuCwD7asj9qNKPDOpXFYloqnXnsHp0yQxGzWVZDjGWH_HgTJawN0wvoC4uH6j27lMDdsNHzrbuqdgvxnxsIYaAhQhgK7YpVJ-rl_Ts-NBJ29jrcNguaVUGL1xLrV3lxXMlhpTqMNSDSH_C_k6wfvEA56TgpdsC2FXKDkCgA-W1jdO61wjxxGKj185VxfM3KeXFmT0bE09XMh8nyKZGq_wCR_o8TKeQpMFGGvziLVNWH0w7qeA07njlw4GHdyKpiIpM7x480FPmFuPhBryju25jjgTQf4zDnsVz2Kjd0UvQ5MtJQabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBXhVmP-e0U9Xk9teyNWUEYXnCHSnSZSKCXhXD-YN7L3lZlUwEUlvsJoLf1ctPBxO6vhi89b-WKyXk5sgCu2qyKYh2P9geQ26vpRFG9aUwBFbcOk-73f94uleBXPxcOqELB1Jcg-9UrAXywzf5wvFfk-zBxAKGQqeZPA2XAPTh3F-aofSuznqIl-rBHzjg3FvXXCX8lWmQFzVi3IZRPAJTQKujKnMA0AUEar4sS5p1QRVADUT5W79dWZuE0kG2LLDW8QV6aRztq14aGGJAtTXWV9fcW9oK_uLGb_piek66UrPudOjfi2IMEj7MdrVdaqrNM37Hvlg2s3XUgmOFbRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsQ1s3Nv__Op1Yr7-c47P83H5FDTQPZS3BGQ9XaNe1SlmdhpIWngxojMV7FS_aHtOo-NhQcPzYdBJ1nwz-s8QdmfTjS26esgtNtRlC4r6kn0zdHL3secI0bUB1ugEUB2pTVkabWWJSU-cT7wYkENazHBZWIZl0REIdwHXAidE2rtbag0QjzErqX8VbBe-oG_GOFk9rk-GloQg0_rrKFk6Y6Bvj2k2bbrnECEBf21bAZ0Sx1yRAZSKBHF_aESjon5IyBl5XEw1Pk3S3od7X8YmLBwWk0_Pdaq0JyMR_z5hmM96yDeyhDTvj4puV5mCj3jn9mJUrFh31cDwXVplnuwJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA2cwybmatgras1PhbTchY9W19Ha_XUw6Ah7SHPF8fXz57XYKvW23XKnOXn9HRmEG4ez2hLGTYuggMrUC-_WpnUIGd5EKqzg0imzcOzf3XZFSitcWleZVPXTtVrcRc8Nam-v1PkxvG39XQTdTC85DjmiQ4s0Dmkp-2fNmZX5JwAbot7A8x2JEvp6YenmUcKx9lR9YhY8daCLR0ioUPTc9h6L29ZKf8Z6hadocOrZSDPnJg6yh1JuzEcGSxD9Mf3N89eGwXSh1kQacQsatNqcSfoulR6KfM3FQ65F4QGsJ16X24pkGHB6TjpI_D9-DAzJX9F2PxV6ZiHJ9eGyxCH1Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=qxR8w-d38_g2mrLoFD3u_96Aby7Ug2XnGfRI5-s9OT1Ybw-3JQf3hcClbXNUJxgI4NCBYQ1jI0vapBmrbNbelIgzV6J4_qKWPju9XeJntxQR86HfPGGS6VJYb4gjjgLGm08sjXtrY5bFgs-XX4scn1O9qieEVUCoRmEqlzZ5znwP4qaWwxByIz9UgBC0oVYJdGEEmzJyFEvmfxX3ndhLj7tGyC9esIyyPjCxfkjUG_FPYLkJKxyV8Owqgmo5BDRFLAuxU4t4MLa7bDP9SJkHiCVEy7C38VL1fySQPuVBMMNYh7AzIeFcc5e33NWjC9-FN2EUxNyJFyRLQT2GTbEosA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=qxR8w-d38_g2mrLoFD3u_96Aby7Ug2XnGfRI5-s9OT1Ybw-3JQf3hcClbXNUJxgI4NCBYQ1jI0vapBmrbNbelIgzV6J4_qKWPju9XeJntxQR86HfPGGS6VJYb4gjjgLGm08sjXtrY5bFgs-XX4scn1O9qieEVUCoRmEqlzZ5znwP4qaWwxByIz9UgBC0oVYJdGEEmzJyFEvmfxX3ndhLj7tGyC9esIyyPjCxfkjUG_FPYLkJKxyV8Owqgmo5BDRFLAuxU4t4MLa7bDP9SJkHiCVEy7C38VL1fySQPuVBMMNYh7AzIeFcc5e33NWjC9-FN2EUxNyJFyRLQT2GTbEosA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Ji7N9enyNgk-3uEzCn2hHB1_q5XqsOHRwMGcmcUZ4G6Rk8nAjG0O7L2x6p2e7YNpGMpM3fTYkgoRa64km_jbxjbSrbLjQyDRUieQtXnIDmJKACNFJEHC2-7dmlq_K2w7oCojhESqkOJA__A-00JZGBbW46BbR9Ntj2_IKT7-zQXKNy2F2jQ3AoCelLdbmXFv0z1az43vrvux_WK3CXGSabqYOKfQBVJxg1V1dkHc1tLIRbkci_FoFyoE4yVr82fKo_6JBmpx0LqokBsVd4lseeN4pgLhcCAZSpBnKw_mrvU3R18OfjNkbYIaBm1or6-TUx85uO_nwonAhdsSNzHGCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Ji7N9enyNgk-3uEzCn2hHB1_q5XqsOHRwMGcmcUZ4G6Rk8nAjG0O7L2x6p2e7YNpGMpM3fTYkgoRa64km_jbxjbSrbLjQyDRUieQtXnIDmJKACNFJEHC2-7dmlq_K2w7oCojhESqkOJA__A-00JZGBbW46BbR9Ntj2_IKT7-zQXKNy2F2jQ3AoCelLdbmXFv0z1az43vrvux_WK3CXGSabqYOKfQBVJxg1V1dkHc1tLIRbkci_FoFyoE4yVr82fKo_6JBmpx0LqokBsVd4lseeN4pgLhcCAZSpBnKw_mrvU3R18OfjNkbYIaBm1or6-TUx85uO_nwonAhdsSNzHGCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=mf_6SLFF4v0ahKvO3uDuuJeMBs1_qr65apctO-AKm9B7Dk9_YYtf46Ncy5M_MIq3PtGTcuZvCVhC7dMCpMgXrXS2QlAVLhRlDjCaA-8G4q5TOcVxOK21YKwVYUtCtVLVFwb5vLXMr7HS1Yahscmmq1sCJDSK_AgAOY5wcVN-Ld3RupEAEhEC8PaoD3BeZz_c_nVQ5hUPRn9aBrUT5qwilIbPkYOJhtIQ8ZFZnCcX5L9uNO5V6WWF_BZV_GH6CYCjAZf0Y1avakSL5if3uztLK9sYHNo2QgmriXJiAs0fgauzzwOrI22RSxkqCGVnmK5FEAqdQ1_AZetwkGN2PqPC5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=mf_6SLFF4v0ahKvO3uDuuJeMBs1_qr65apctO-AKm9B7Dk9_YYtf46Ncy5M_MIq3PtGTcuZvCVhC7dMCpMgXrXS2QlAVLhRlDjCaA-8G4q5TOcVxOK21YKwVYUtCtVLVFwb5vLXMr7HS1Yahscmmq1sCJDSK_AgAOY5wcVN-Ld3RupEAEhEC8PaoD3BeZz_c_nVQ5hUPRn9aBrUT5qwilIbPkYOJhtIQ8ZFZnCcX5L9uNO5V6WWF_BZV_GH6CYCjAZf0Y1avakSL5if3uztLK9sYHNo2QgmriXJiAs0fgauzzwOrI22RSxkqCGVnmK5FEAqdQ1_AZetwkGN2PqPC5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=gbubGP6fuVRI2ga47kb_gsK_ADuvz-2r-NcG9PkOzj72h7i8IM42hLbhvEgUfMDV0Zr7kSNMD6-Hv04gCrYIgv1mUpBIJ6U4Os91dffIEpopWdw2MCkpNSFZq6LYo8pgJAJSdRij2aHdZjOkrESI_EjKfPhLoosmGgfGkgRdI2iJm3jPEH20neHS3kHJ3LeZHxbVkcljgVcwCyZij1QPd9FpqvEN5GsxDQpoqlNct5SgwHAf7QKGdhbzijiIhg8vqA-GDRlZNu_uvlHCIV8xPEq8g2Y79giPokM-khKZaT_hRdrsZIM7kPtByUEXVhlIWokuA3q9C3iECiEpA1BLVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=gbubGP6fuVRI2ga47kb_gsK_ADuvz-2r-NcG9PkOzj72h7i8IM42hLbhvEgUfMDV0Zr7kSNMD6-Hv04gCrYIgv1mUpBIJ6U4Os91dffIEpopWdw2MCkpNSFZq6LYo8pgJAJSdRij2aHdZjOkrESI_EjKfPhLoosmGgfGkgRdI2iJm3jPEH20neHS3kHJ3LeZHxbVkcljgVcwCyZij1QPd9FpqvEN5GsxDQpoqlNct5SgwHAf7QKGdhbzijiIhg8vqA-GDRlZNu_uvlHCIV8xPEq8g2Y79giPokM-khKZaT_hRdrsZIM7kPtByUEXVhlIWokuA3q9C3iECiEpA1BLVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=IYxaPnl0YVpQ2TaEnEhUi1EUOyuQjtop4zqBYZ1iXHXL4WP9Hqk7LBgyZpqJaEA6J8qZbNMUuSZSzXsM77hcoIkqL1_82BPlvVKSlKa3gzkQaF5ydTXONMJfgks_ep-LBQSTeQDqSMOSTNMtOeosq50YudofQYHu-Qyi2lGht1h7PWcHKUfxsDdlhNogLzzr_J8GTBkRcN6JGOAXWqYQNWHOLXdtxcPnplb5nA8vzx9c1qy_UvMkbXVd6BgKl-O9ogudxRJ_6qEk4c1dTdRcBtvFIvDYWYtvJFd5gDrQvQOJZo49x44gCpZNkSJia8ofqe_ZT3MzYZYupBIjRXfAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=IYxaPnl0YVpQ2TaEnEhUi1EUOyuQjtop4zqBYZ1iXHXL4WP9Hqk7LBgyZpqJaEA6J8qZbNMUuSZSzXsM77hcoIkqL1_82BPlvVKSlKa3gzkQaF5ydTXONMJfgks_ep-LBQSTeQDqSMOSTNMtOeosq50YudofQYHu-Qyi2lGht1h7PWcHKUfxsDdlhNogLzzr_J8GTBkRcN6JGOAXWqYQNWHOLXdtxcPnplb5nA8vzx9c1qy_UvMkbXVd6BgKl-O9ogudxRJ_6qEk4c1dTdRcBtvFIvDYWYtvJFd5gDrQvQOJZo49x44gCpZNkSJia8ofqe_ZT3MzYZYupBIjRXfAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=sQcoUlwUwOTfeDifsnOHDgg9AjH0rOxwcxvochWkkW4hnp9ppMnPxA9ra1j46mKO8ZhjEtic4YsvEQRBVS2GX8-j2JKah3u3mt4auJXfAqkwex8lNJi218gb_zysOiUdTMtuoCLn8ESc3FKV8u-2bcsF9ul5nQ_Bp1YDUXFAZi_2xopU5tgFAGXEj1BtEgFY_9Jd-80EwZq5zxoykpTdk3ynaDOz6OJl1sydWhabU5fPU2nDFoGuwc-QjJypgC7RtbKpLBm3xsH-IuLD5RBvVObzKbyjK3oFWIRMKtnI3iAhiN1uujytQrQTKU7vU546dDPP37mXyrU20LkpGkyKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=sQcoUlwUwOTfeDifsnOHDgg9AjH0rOxwcxvochWkkW4hnp9ppMnPxA9ra1j46mKO8ZhjEtic4YsvEQRBVS2GX8-j2JKah3u3mt4auJXfAqkwex8lNJi218gb_zysOiUdTMtuoCLn8ESc3FKV8u-2bcsF9ul5nQ_Bp1YDUXFAZi_2xopU5tgFAGXEj1BtEgFY_9Jd-80EwZq5zxoykpTdk3ynaDOz6OJl1sydWhabU5fPU2nDFoGuwc-QjJypgC7RtbKpLBm3xsH-IuLD5RBvVObzKbyjK3oFWIRMKtnI3iAhiN1uujytQrQTKU7vU546dDPP37mXyrU20LkpGkyKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=cLgDNDGUAIemtPi6wO509DGyyimgnMjX_35vzFSHQtNdkMmyAwFgEHqEcp9G8nAAIzDEWfntBTuS9PVFEkVjyMI1Oirw2wbTCmoAwKxsn-Fcn8LB52MWcLzDJWzrGoF37GNcSLR_TSJbPzZ8pxnV6Pxx3gJkwrNC7kDdppT_Aes0FxC1JpV0237T6qpFzxRc2OnjUACGTbGsq5N7-gowhkWHbuUykeL56hBOS08ox9J1CjT7INOJMqern9LOGD0XAuLv79HHHe6hIgq4_2R6_4_ZaAk2fFkAKFINJOzNXz1t4wh3K-nKzkYuOFKNCKGaFxSj9S490fbLinMeT8gZ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=cLgDNDGUAIemtPi6wO509DGyyimgnMjX_35vzFSHQtNdkMmyAwFgEHqEcp9G8nAAIzDEWfntBTuS9PVFEkVjyMI1Oirw2wbTCmoAwKxsn-Fcn8LB52MWcLzDJWzrGoF37GNcSLR_TSJbPzZ8pxnV6Pxx3gJkwrNC7kDdppT_Aes0FxC1JpV0237T6qpFzxRc2OnjUACGTbGsq5N7-gowhkWHbuUykeL56hBOS08ox9J1CjT7INOJMqern9LOGD0XAuLv79HHHe6hIgq4_2R6_4_ZaAk2fFkAKFINJOzNXz1t4wh3K-nKzkYuOFKNCKGaFxSj9S490fbLinMeT8gZ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ocatlznq51e7_EMV9L53YYZYvZ0MlVcTOEX-UsIPFNqIZDST_QhjnnK8d8yBFyggVFQP8O9ACeoVwQA4ioe1TQYTAoCH0akxxtSDAXlfGCMrXBTSjtb-0VO02kERsZBJTLMQBa5JtVM5yIEyoHQ_QjAMHPYj6zJkbSUg1vXiYzIk5MHli2IaIRjChzwnFKqNvGJBsXannpZp4a7wRCFFdScEijLJRFT9EUS9p0ewHdiAwsE7AsxK_wO81Eho4YUZHeof9g3QfZ1Wr3muPe-IP7wUW5zf8nddPz2N1FUyo6KdtM1tNaTxVhKF86a2RdYVzaaEgs-33_jA08QhcFwK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=j7rpXeawMdSL5uo9x-YGWOLyFUaBOqrr39v9c0m_Ge-mUfcPuBC92cHByy144fORXD-viSG5iLX7W5ncS0kEREqhrJn2JouUXCaWHqYSAtdt5LLdpTznfo1MxuNJkyBgTEPsuR19RuXAHnspN5t79Ks8wdh92y9sq_yPV8ryubNye5WxPlfKwAEsIEpYLLF4Fey3PzVXWJSNfN8Gbym3kR2NfTSeU_3CL44Z_mzFKW9HKKWRPwx25njsfEprIAAkZ0IhsZIjyZ747L6v3pA0KYjIdR0tUdz3Xk2QX6xtoRqK9u-P-4CGgnw1-26m9MaVnh4ZulLeJczyKMwmtvD7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=j7rpXeawMdSL5uo9x-YGWOLyFUaBOqrr39v9c0m_Ge-mUfcPuBC92cHByy144fORXD-viSG5iLX7W5ncS0kEREqhrJn2JouUXCaWHqYSAtdt5LLdpTznfo1MxuNJkyBgTEPsuR19RuXAHnspN5t79Ks8wdh92y9sq_yPV8ryubNye5WxPlfKwAEsIEpYLLF4Fey3PzVXWJSNfN8Gbym3kR2NfTSeU_3CL44Z_mzFKW9HKKWRPwx25njsfEprIAAkZ0IhsZIjyZ747L6v3pA0KYjIdR0tUdz3Xk2QX6xtoRqK9u-P-4CGgnw1-26m9MaVnh4ZulLeJczyKMwmtvD7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=Ltz9LQ4UZZLapqmIH8eOpSXPraVPC5D2DVKeg5vfzvJhskKGfuW2bezmoYd_mhLbOocLzlPPcYr4suKkojRZEEj08Jsmfw93pOFAJlNEVs34gihNowdT1Q4c3UfCi9pa0N-ORulONS5CJ-3UTTC666SKKOvnyXT7NDZFgIQ_DGFvVi6CIlCJ_hUD3TG-Rq1gWVEs51RjmZ9Z3am81t_l8JuumS7zUY_OH9ZQob9vDrkKaD18-NfLLRcEpnypGgGymWr1xOS3jLLJOIBfvIicePClFgThFPLrC0irIUd5oxDc0AsKGsuDie9qOJvs597MixTyjMBzIeLNqfPE_ou7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=Ltz9LQ4UZZLapqmIH8eOpSXPraVPC5D2DVKeg5vfzvJhskKGfuW2bezmoYd_mhLbOocLzlPPcYr4suKkojRZEEj08Jsmfw93pOFAJlNEVs34gihNowdT1Q4c3UfCi9pa0N-ORulONS5CJ-3UTTC666SKKOvnyXT7NDZFgIQ_DGFvVi6CIlCJ_hUD3TG-Rq1gWVEs51RjmZ9Z3am81t_l8JuumS7zUY_OH9ZQob9vDrkKaD18-NfLLRcEpnypGgGymWr1xOS3jLLJOIBfvIicePClFgThFPLrC0irIUd5oxDc0AsKGsuDie9qOJvs597MixTyjMBzIeLNqfPE_ou7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=gv1C-qBRm6M8pKq_gZC1OYP2cYG9NKBxPf-W7t8c6DOTbgBiuByfz5qATBviCcXTcycGvG9oQsjBjJRxhNCygoQ4cY2axfZZ-KNoib3KuIYDRvlO3W3iN3tLQ3xZLWB0tNv0t44gdw1uLE5fetz4BQUJGz8-LX8ryKQmk1i2V7Ycf-e8Hdc9DAqdv5jfYc81KgCwoTLg2Vs10bxPdkWJJnTt9DXqvLGt1X0JcqKmPhGSXTHBLW5xAmvijQP3Wgw3v2Y0YDhjQhX5wBJ-cJAXO-G02Vq-Dp3mkDsQH4RCUXP5kz-RgNB4fGgEji2pUpMIwAh5knh7qqWhK0Ax9OqIIAf9KKZR6Tix_0FrkcGFDXro1SyNdDeUKYEMI_X3RkDVlPdjrf4CioBOBO6ez8NUlrbAUc-KSnumrWhFu-KCO08M4r8suu32TsJjjb8jaO3XrElvBYt_46A7rVfyQ1tdYouUnIsSFKLJBk2JHgUoN9MCGM5ggJ9limXUssyDbRmUoR85tI9GONTKoiwQho_egsJgN5VFNkcv9lPqbNMMnmdagupI3xtrKTbXzer-1B1XO6cb16ymIjaBIjNYqqet9sXDFYiBWvPdpPLPv9ruV85BG5nB7ZU4gzqq0UIcPVbl56hASxofR2lr-Etp_cTFWzaSMDK2bJqEExATKL1Gwzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=gv1C-qBRm6M8pKq_gZC1OYP2cYG9NKBxPf-W7t8c6DOTbgBiuByfz5qATBviCcXTcycGvG9oQsjBjJRxhNCygoQ4cY2axfZZ-KNoib3KuIYDRvlO3W3iN3tLQ3xZLWB0tNv0t44gdw1uLE5fetz4BQUJGz8-LX8ryKQmk1i2V7Ycf-e8Hdc9DAqdv5jfYc81KgCwoTLg2Vs10bxPdkWJJnTt9DXqvLGt1X0JcqKmPhGSXTHBLW5xAmvijQP3Wgw3v2Y0YDhjQhX5wBJ-cJAXO-G02Vq-Dp3mkDsQH4RCUXP5kz-RgNB4fGgEji2pUpMIwAh5knh7qqWhK0Ax9OqIIAf9KKZR6Tix_0FrkcGFDXro1SyNdDeUKYEMI_X3RkDVlPdjrf4CioBOBO6ez8NUlrbAUc-KSnumrWhFu-KCO08M4r8suu32TsJjjb8jaO3XrElvBYt_46A7rVfyQ1tdYouUnIsSFKLJBk2JHgUoN9MCGM5ggJ9limXUssyDbRmUoR85tI9GONTKoiwQho_egsJgN5VFNkcv9lPqbNMMnmdagupI3xtrKTbXzer-1B1XO6cb16ymIjaBIjNYqqet9sXDFYiBWvPdpPLPv9ruV85BG5nB7ZU4gzqq0UIcPVbl56hASxofR2lr-Etp_cTFWzaSMDK2bJqEExATKL1Gwzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=dlto3Dg2u7Z8CScr1-49QFjz9LdNo_ThXnbyCqwa3ouDciBFOBu-jHNOyePWtJgqAqDIDxSQ3tWTNfCRFcIufqj1EkWA76ofCOvWjOBhGbpktS4zAz-hlqvxkrC_yxg4NUQ_vs9PXn20oNReZ3FSANvljnVKofckvzef3SJrMyK9GadnMIBmwVYsIC0ZPzVpSXV1Jtiv6An9ErYL3suCc5O3Zo2rFgsdcSTCj3uRijY73WDYLS1nA00mazEBJpyNU3OGxB0tqv-QFJRUC_b31sS-ISRSKiqMTRb7oMhcE_-jOynV3CuI3xle1CsHQYTQWeYVoeiRE72cfCl4e9-4Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=dlto3Dg2u7Z8CScr1-49QFjz9LdNo_ThXnbyCqwa3ouDciBFOBu-jHNOyePWtJgqAqDIDxSQ3tWTNfCRFcIufqj1EkWA76ofCOvWjOBhGbpktS4zAz-hlqvxkrC_yxg4NUQ_vs9PXn20oNReZ3FSANvljnVKofckvzef3SJrMyK9GadnMIBmwVYsIC0ZPzVpSXV1Jtiv6An9ErYL3suCc5O3Zo2rFgsdcSTCj3uRijY73WDYLS1nA00mazEBJpyNU3OGxB0tqv-QFJRUC_b31sS-ISRSKiqMTRb7oMhcE_-jOynV3CuI3xle1CsHQYTQWeYVoeiRE72cfCl4e9-4Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=Nc8uSo-h-_xUBMY1mAD95vwjASOczUd05mOOE3qFgw6NCamxLQ829Qdhh_uIVG28U-swR66afFyKdrxyNJrapfPhsnXWBn-NrnaE38urhQxlybd6kZRgSpXboMC_q6fMoGxtrY7RIPshS4ZTHUMlCpEKLB1spUIrs19ojDYs2x76NvjOj6icaU3Gz0tUUUI89b0_UjWWz8jeI6shw7j5IXsmCeFB5oKWXYr0PnVAtegTR09jOtNPxOTPuFi7T-b63RCoJTppDOr_xS0OiPAsxYoDUYGrPehkH1-sTHe8wgCHGxgxDfXjZOIHhJY4mJOSURmV-CtTunxO2iDCOXh_xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=Nc8uSo-h-_xUBMY1mAD95vwjASOczUd05mOOE3qFgw6NCamxLQ829Qdhh_uIVG28U-swR66afFyKdrxyNJrapfPhsnXWBn-NrnaE38urhQxlybd6kZRgSpXboMC_q6fMoGxtrY7RIPshS4ZTHUMlCpEKLB1spUIrs19ojDYs2x76NvjOj6icaU3Gz0tUUUI89b0_UjWWz8jeI6shw7j5IXsmCeFB5oKWXYr0PnVAtegTR09jOtNPxOTPuFi7T-b63RCoJTppDOr_xS0OiPAsxYoDUYGrPehkH1-sTHe8wgCHGxgxDfXjZOIHhJY4mJOSURmV-CtTunxO2iDCOXh_xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4txVFOAPDTZaned2BStyp6LjYyC7P7d2trLsfRzZRCBizbTJaH-gvzF26WgjU2mduXh1cAEY4eDc-JpIgeCM87HElunNSdL77XFLcezbY956TOd-uo-u6bw4KndC84fDT4xa5r_R70qYbr8qxM28Sjh96O83ORABiM3nb0pX9eEJtWhiYRJNSjKbukUQzKselBooG0ct9a7xd13gVBsOpOeuqQHoZTKN__ccn_qfAtFQ9YP0ZLKXqtVmxnpg-5OAEN2G9MJmVMNj7RHehfm-16piZK2jrvhNH9eyUCfUyoFnZLJjraYEu2UZAE8YYVDe7N5EU1EWHF3YM2-7bhpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VdfLCVSkxSkyfZqbqA4zlRXC7dl8q1VdI6v6Iz116vTKnyIC8Lr-td7MzjjWf68_-DpZ-tUpT7d2lLkFXk_KMr2jKKZX3R-blL3X-FGrGD1sMT2CIBoQEAtWuWsClpFQH5BcVoQRtaEwRkO7IT7yw7KH6FXLgBipe6jH3H9-oCsjvay5-pk7zZvOeB0efu7tqS2Eb9RWWQconoAFnTvh5o7CMjBFiWpwtk6iCxf-hYQXzpB_h-zR6rpokY2YSQtLaTy0U118sJHFTGCVHQHmURPg5u8sXt53wpG1IMxbQ5QVCCXqJPiS8b5WnkaCT8uAGIJ8x0SqUfAjWTKszanzCg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=tGx_zroNjQ3Fwb3STCGEjmmNGWQmYswSG15QR4yrthe6fC_68mqFBCoNgFtMM0WGmOPgfubkLkCEo0yCt_g5NAQ7T4GbcP9oQaz4D5K7HTf8wf3OfD_T_MEmo6mQj7SxrLf78AofoI_xNShIbP6HJNA6D9ksPYR8cVKSr18pdxBdE2VtJkuLm8PdDDea7gB2brdVGtyKE5Vgu6dT6s0Xduysd5BKAoRh3hWjea8EvlMbzSpGqzSwqqU60uW6rbNuTyxYbmuy3nS6AB1QvsIhuAlsqWA0sEZqesXFFfW-39FX5pFABRmYZz6hIWT6SwmBHA3fks6_Hx_NPjJnKxA4cFGk40Tn3QuETP6F6wtgBAb5L15Oj5U62Vew1pwo87CSw5iMwNl65qNr_Sd5KeQ9BmwpStpAhFoKy6W1v-K_H51LQWZdtDidbzZz1zLGLk6OpUQ1WvUcYfWcIF6FkSs-Ckgs4E73R7r0fq3iM-ICvcMjlvABIs9AGScu5XIUFi8OafG0PHFJtMV6heURntBp1p_tDuBedM8gyUGbnb2916XAgy1aGTs2X6zGKPOORCTDfhMk3ZXY1hq7xY8WbMREjq2qjXZjncGcgnb8-sWD07TOH_tNf5QNpcQkW8OOQPZaFR9bHWoyjtId11b7yCPWR1T1OFoXxsBXL24b7fwLJP0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=tGx_zroNjQ3Fwb3STCGEjmmNGWQmYswSG15QR4yrthe6fC_68mqFBCoNgFtMM0WGmOPgfubkLkCEo0yCt_g5NAQ7T4GbcP9oQaz4D5K7HTf8wf3OfD_T_MEmo6mQj7SxrLf78AofoI_xNShIbP6HJNA6D9ksPYR8cVKSr18pdxBdE2VtJkuLm8PdDDea7gB2brdVGtyKE5Vgu6dT6s0Xduysd5BKAoRh3hWjea8EvlMbzSpGqzSwqqU60uW6rbNuTyxYbmuy3nS6AB1QvsIhuAlsqWA0sEZqesXFFfW-39FX5pFABRmYZz6hIWT6SwmBHA3fks6_Hx_NPjJnKxA4cFGk40Tn3QuETP6F6wtgBAb5L15Oj5U62Vew1pwo87CSw5iMwNl65qNr_Sd5KeQ9BmwpStpAhFoKy6W1v-K_H51LQWZdtDidbzZz1zLGLk6OpUQ1WvUcYfWcIF6FkSs-Ckgs4E73R7r0fq3iM-ICvcMjlvABIs9AGScu5XIUFi8OafG0PHFJtMV6heURntBp1p_tDuBedM8gyUGbnb2916XAgy1aGTs2X6zGKPOORCTDfhMk3ZXY1hq7xY8WbMREjq2qjXZjncGcgnb8-sWD07TOH_tNf5QNpcQkW8OOQPZaFR9bHWoyjtId11b7yCPWR1T1OFoXxsBXL24b7fwLJP0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiiPxXcgRRB12Lr7WgCb2nmMwRSyvlz6qJfIlX0-OBLOVJfiRQCtIy54u6lIIXqzpKwtkeBWZVz3hsYEDKLE1jXhKGcP0hTXHMuY4BwIewPekeICgicQfxKSsNUz0eEtKXfEaYq1mQED0sKcstodffn96baBNWfv9ieFw059EuWjW4VVdbEREXtvQg83K-5Zv2C88VBxFJLu9BTad8Dmccz7EIRpVGKVe_SnkfoSAfLmBjXBNpuAUfKL_pd1BEJXMg9hhHxV7tcdVu8okfXKmIjGrRqcH0r_E5mLWNDmideY0yllaENvDzfB9e3kAHGQ73OED89qYS4tgmW1nYfjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TeGj0XJHsQOfitEl2LK-IR1KbecO1uY7kEaa7RHlI9bj9-K-MYOCWbrcg4eGq26oX37kQy7B8t2GpftQgS4jVJV7W3GBfuftZLoC0DbGYGpe2ZPdDJltm8tZWuGRLHBTKT3-zZlgrsk6U3ZkG5m8d72OFtUnZ22Jnd2n3qoTRw9MQUGwli2VOLvAac6Bwq9_hQlWZYdxUClhce4ryGvfT_Rxcsozc5tDufxe13hT1_l-mFnakOz7U5B5jNRJZM3X6hP8U5SYwXBL7tTv0QUiJneLKAgFkim9wqKIbnvpVRMJhe5EJ_YJ9gLwydqGBFzT93D4Zx65KbdNCbS37gaHqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6jSFykTS3adc7wOP75irg9Z_C_zwLrcV6NwFyEXM9KAAabJAiL7PtgNyCWkdmYacv_YyYzObiI-xW539AC1JgN6AxUSR0Oy2_2eaCoJccpP3Mshj2A2WlIW_b4BqXlyDQ2zXtIOrII-zrZWDh_iczFfyMgsebV7Ga_dopcLcozuLwyuNnHxCG2_641xyZjgbMDjmMQPtw5478NHCuvBcfozkc1exGFoQH7e5EEVZq6rUT5wv11trD70j5qS3QqDAB3a1xxwOIsVUxFaMPhP3kAuvbB895g04OgzS6yoX35BYOePMKTvJA2-4tVUkWnwDcPDkHJmVTWTdzk2NkjJaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYgOE0qzIfv6Ij5iawxtdL3RnQ1h9jli9XxwcrghXJU-jG-Zs9_FWHaZ1xbZlphLbGsS5cUFPbQKX0ZqOzhj3-5VT2ksu2BCpkXL_isXzK9JyNx01xX4908SyaAtMXzIECdpYvRnPwXz3ctaoPnGvl2jJv5OLTI5A4Gb4twQIxnUPAZMElKKBzEaOTtHY8mCMm0JUuX5fd8ha-4C31N2sNEjoxM5iZhead9cGhxFvYjb6c3MJtMaUJMsptAdite4Nd30l1g4ghL06hhNuSrEdNyMEy6O1uy5--SAcAN52UN_QbxyfXi91-nEziRNEiUhNsHXUdkDzKSx_XKVn-jchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=NWe1DnnAjhoc05t49DcrNKy-pwaq2pmrSFL0Iwl4HSr6rc7HquGklI0MWffIHVe0yK5LT6jn1OM4Vw-xCbZZfQpE50wUMBo09pwYayITfBEKWZzXe8_HYzUz3bGIPUXLgJxquyUkv0jYBdc_zh1VfjkR2ZxglFHfMWI3A6As2lpxeFlsfJt95CFyenXrifdukqk6bkIDqKPn3blBDC5fjufzTkB5jRP0ohZ_p5tn3FT9CrDMQRcPDWI4CLIjKjwUkczum1PnkgwmrVOOv5EpyzLccyV5QVe2E-_uGt5ntK8a5NmzYlAFh7SBsAqPJqwrKSzQjkj0QYiNXPEZoJnfcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=NWe1DnnAjhoc05t49DcrNKy-pwaq2pmrSFL0Iwl4HSr6rc7HquGklI0MWffIHVe0yK5LT6jn1OM4Vw-xCbZZfQpE50wUMBo09pwYayITfBEKWZzXe8_HYzUz3bGIPUXLgJxquyUkv0jYBdc_zh1VfjkR2ZxglFHfMWI3A6As2lpxeFlsfJt95CFyenXrifdukqk6bkIDqKPn3blBDC5fjufzTkB5jRP0ohZ_p5tn3FT9CrDMQRcPDWI4CLIjKjwUkczum1PnkgwmrVOOv5EpyzLccyV5QVe2E-_uGt5ntK8a5NmzYlAFh7SBsAqPJqwrKSzQjkj0QYiNXPEZoJnfcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=JEh9i-S88y8y6he0ZrnXVvXeheMoS-RdMqTlHjUvJDaGUrIwtUrtcQ8PqTJ64NJSn_nhmSkTme-mCBrRmjlEsqNxaRT-Q5HJvBilmSgJsBUjVe8-M4Asn1TdK3XSuOgzPY1OjTKWodgS4dKpIXE-8rOZUT97oefferVwwO184_JzVevc9AzQeprNN_4oYakibDy9SXb9rbQpQ1b_gweubSy-E4tF0vugG9JHRqjnJbep-tignYULOB_J72xMQoLISdeH1S2uDf0JCdxuel41Zzp042hXFL0c2ozr_rwwaGJTLDdTTcBlQUvSwevIKqnIK0wZVN8PorUVtWbFX5SMYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=JEh9i-S88y8y6he0ZrnXVvXeheMoS-RdMqTlHjUvJDaGUrIwtUrtcQ8PqTJ64NJSn_nhmSkTme-mCBrRmjlEsqNxaRT-Q5HJvBilmSgJsBUjVe8-M4Asn1TdK3XSuOgzPY1OjTKWodgS4dKpIXE-8rOZUT97oefferVwwO184_JzVevc9AzQeprNN_4oYakibDy9SXb9rbQpQ1b_gweubSy-E4tF0vugG9JHRqjnJbep-tignYULOB_J72xMQoLISdeH1S2uDf0JCdxuel41Zzp042hXFL0c2ozr_rwwaGJTLDdTTcBlQUvSwevIKqnIK0wZVN8PorUVtWbFX5SMYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR6ZJIE8cladfQ-hl05j1gXfNGXfFX9eCUIX8uullLtx9zv3l0yk5kiQQH_mcS9DKyLTlW7N1C4wQJZ7a2GfEo2yxbeRZTFN1ko6LnTUjZ-1H1dPLGhFkD2E9Sy803GeUI4SzuAsifh2NRCn_cR2FtFj6GCcTxzfU1gczoidHr3NrcqAOwqBvFEt6V8YAGLtWEz5CKjUdI-CaoVuzw8DLkFQt2zyzSlUGIvFrqNFfAT78xzZbhVJxxh1JLZ7uhI1-3s0n0aLw9kRStrophiistgazmQNGriha-iEgsHz_f8altzXSwYcP82nz2uHA-Rl79K7o6cvdjH7WXkr8XmxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=GfDwxV5Kyj6ClplDZcrwMlC-AFUSeSz2vOlGO7cXhucthWnEkBhKbMSnJ1ZWc-FJoOd4zIINwl5V6vx1seOUMlBf5NjCvUfpan4erOzqpLh2BtuN4k3qqKzEa-pLYNKQun4qeJOYjwJGtUP1x5gvy7XB3kvh6SvU4STByAcwqo25dIJX-fWj619tpAgOegLcNqFHIiTlMtgp9pqtO973IO1w-SzOlp6bfwUd5mBSNfmCO66RAvB-tnyym-sGJHtrNmPlS8RXwOlo_Ah-BvOt-UXygI-gB_Bh0_z36ivXC_Gaf7VDoT-NKDczyCFdQOj6TPsNpY6mbPMJqshTjljV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=GfDwxV5Kyj6ClplDZcrwMlC-AFUSeSz2vOlGO7cXhucthWnEkBhKbMSnJ1ZWc-FJoOd4zIINwl5V6vx1seOUMlBf5NjCvUfpan4erOzqpLh2BtuN4k3qqKzEa-pLYNKQun4qeJOYjwJGtUP1x5gvy7XB3kvh6SvU4STByAcwqo25dIJX-fWj619tpAgOegLcNqFHIiTlMtgp9pqtO973IO1w-SzOlp6bfwUd5mBSNfmCO66RAvB-tnyym-sGJHtrNmPlS8RXwOlo_Ah-BvOt-UXygI-gB_Bh0_z36ivXC_Gaf7VDoT-NKDczyCFdQOj6TPsNpY6mbPMJqshTjljV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=AyJQiVy_YfHDc5ElTsaPB5fI4IWS14dVXcwBVe5CDTTR4aDpj81x6OuaTYHZFAvWDmhTsW5ZUU_QJbGSlWUZaMJxgM3529_5tCyyNVxty0vq-h6I0qAL5yFH4woWJPH2p8VbkUTzoOvRUcYhIrs0fr9c7J3Ro_I7n0SrJCSYfXJMHUSB19oVLTbhWt4dRALBzN7nGbND7fbiMy8eCamF6FuBU6CmbT3QONZLPQ-vivY56G6m5oWSbNtnOOoJVunEgLT8JOwG2vsFywxn_oKYC9ykvHJdAg4r5n72G_jm3ucDHt2iwUTa3mimES6MGtQMEDJWf5MEbwzyG-mekotP5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=AyJQiVy_YfHDc5ElTsaPB5fI4IWS14dVXcwBVe5CDTTR4aDpj81x6OuaTYHZFAvWDmhTsW5ZUU_QJbGSlWUZaMJxgM3529_5tCyyNVxty0vq-h6I0qAL5yFH4woWJPH2p8VbkUTzoOvRUcYhIrs0fr9c7J3Ro_I7n0SrJCSYfXJMHUSB19oVLTbhWt4dRALBzN7nGbND7fbiMy8eCamF6FuBU6CmbT3QONZLPQ-vivY56G6m5oWSbNtnOOoJVunEgLT8JOwG2vsFywxn_oKYC9ykvHJdAg4r5n72G_jm3ucDHt2iwUTa3mimES6MGtQMEDJWf5MEbwzyG-mekotP5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=SjxFkapta4GOSFh0tRNzoyU3xLfoTSUdIR4zKnj1Gd2kyzgzbAuHX1iQAMOBYrfySRGNWEzh07_OeAwMqJBMeNnCCZ7lZ_zizZXE5XmfKRxAre3FcVI35TRgOCVaHs9VIPRysJqt9CMVnbig3RXBGMGQyYboextBavmmgWuH66LkFIQjPjqDMbcPz-3TqoQOMh8dfrHPhrYUEkUIN68MuuB7yw7vk9yO48zgnytgWaBNCHphSjPiXFVwK-egSMyVkxDa2v8JvAWSms6Rq7pEgWk3Qxnmgy0Tcc_IwSEdelquu7BR-rKNW34CQzoc-6vSW-oT30XOmUGQksfBX7PP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=SjxFkapta4GOSFh0tRNzoyU3xLfoTSUdIR4zKnj1Gd2kyzgzbAuHX1iQAMOBYrfySRGNWEzh07_OeAwMqJBMeNnCCZ7lZ_zizZXE5XmfKRxAre3FcVI35TRgOCVaHs9VIPRysJqt9CMVnbig3RXBGMGQyYboextBavmmgWuH66LkFIQjPjqDMbcPz-3TqoQOMh8dfrHPhrYUEkUIN68MuuB7yw7vk9yO48zgnytgWaBNCHphSjPiXFVwK-egSMyVkxDa2v8JvAWSms6Rq7pEgWk3Qxnmgy0Tcc_IwSEdelquu7BR-rKNW34CQzoc-6vSW-oT30XOmUGQksfBX7PP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=bSHiWXCc1ulxOFC3X1hN3B8LLjq6HqN7Emte554OgDjUHAcaOynsBkHSMfznyGj_saIVwjaDrrGgDQUuvHRKEg9rAaK25N_jU2E_2MteW-8gchdBhS1f49izHWjweBAv9l0FSv1Xkh344rIJN9-Q8s62h0JR4JlKVxeCxrfxVBeKifgqxwNpI0lvtVzKeXkPMQVbRkdJUxr6BlQB9gvXdUA2RDRvqzZyAA02nycolqrQ3Ys3yGVQ0LaOzSzjG1Rph0faIBKgkc_S9GvwNUn8iPV7kbzJno7r3SW1Hw6uc73-TI_BT3RcagsVt97u20XYjT4CHlqBYzrrrOp912iZjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=bSHiWXCc1ulxOFC3X1hN3B8LLjq6HqN7Emte554OgDjUHAcaOynsBkHSMfznyGj_saIVwjaDrrGgDQUuvHRKEg9rAaK25N_jU2E_2MteW-8gchdBhS1f49izHWjweBAv9l0FSv1Xkh344rIJN9-Q8s62h0JR4JlKVxeCxrfxVBeKifgqxwNpI0lvtVzKeXkPMQVbRkdJUxr6BlQB9gvXdUA2RDRvqzZyAA02nycolqrQ3Ys3yGVQ0LaOzSzjG1Rph0faIBKgkc_S9GvwNUn8iPV7kbzJno7r3SW1Hw6uc73-TI_BT3RcagsVt97u20XYjT4CHlqBYzrrrOp912iZjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgzdCEwC13iAKm8kw90I7dAlHMFL-z5SjrkW1XVM-_r5QwbwGh9QGoEAVV4VX5grdH5SmjpxLa_aL56tpE-sMgo52qgxWZdb6re4teLGIUKt9eajSor3qMzxpqzCOSk5rCMED_nBky3chj2Q6jtjOppIdH8h8BTZqqSHWEpULrWRsolZIBC_1WrtZZQC95qJVP_ixRfUlSf5tpyvuWJpfRMMjzES5FGqeQNo1f-zXvlKBKALGR5Cm7-N3A63Q89yyTU9JuWeIGAVYpU7SPgyHMDcTyAJcTHvu0aIfWaxoOCzz3VuyxOqQsMwUQe7VkrRvILUj6-btethdAIUR1ltaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttZBYFt9x-rF-JxphzGFIXjhZ-kpabKippV89yVnjVnIp0z5vFmpGnyr1g8R_ICkIqRiBIThrLsSdOxRGjJNb4VIVrzDLeuEr4eCP8MHGFJ1czD6PFP9L2TyNcxysSrM0ogzKCgF0U6LLtL9YWoyRsC1KRE-hve2NMp_NgKdOCpFXCcos4Np6SuClkDgLmUxKumIbR-3uM9dmxRNZ8u6bd1qZlxtI5198l8YMYby2bLI6e-OK_zAXo8MYxKs5URkUDy3sA9ty2s2czMkEaw-OOr3wE4ROOao5AuE3p1lfKm31JwtiheXkTcEIcNoxH_zmv6i6iVCeJZLlA2xCCo4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=X018JDYacxoID_MW68uX6I5Hgdi5Rxc30HRyT5Zx3SvdjXWqMdVwUYaaqObBNvWjaoqfrSSENm5GqrHJGfGTspN1KoEKbYy7HMlFuMKQvfJ5WqQ-q68wHxCn7xLGCzdCwKilKZPnmCSrlCLyB9OvcWshdVkZ23O5eWCMJjB3t9RQKZrUsET2oq9s_IBGZabodn_XmuoqmXk_7KM-HLHf_NnwZSFdW1Oj1A6liMAZHGKLP4yxn1dSkatYOdw3QEgM098tIAAC4yk70vFKjMtmGLwpuaZofMLytahqPLCJs5DPufYhs94MCZmSB1eFMEcyZVRwCwyKbDbdILV0bvmjhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=X018JDYacxoID_MW68uX6I5Hgdi5Rxc30HRyT5Zx3SvdjXWqMdVwUYaaqObBNvWjaoqfrSSENm5GqrHJGfGTspN1KoEKbYy7HMlFuMKQvfJ5WqQ-q68wHxCn7xLGCzdCwKilKZPnmCSrlCLyB9OvcWshdVkZ23O5eWCMJjB3t9RQKZrUsET2oq9s_IBGZabodn_XmuoqmXk_7KM-HLHf_NnwZSFdW1Oj1A6liMAZHGKLP4yxn1dSkatYOdw3QEgM098tIAAC4yk70vFKjMtmGLwpuaZofMLytahqPLCJs5DPufYhs94MCZmSB1eFMEcyZVRwCwyKbDbdILV0bvmjhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9YhCgMOFO0dB4wignUFiS6RgVLdthWRTG1P6j01QuWH89LWWixTc37uMG6XaAsuqjkFPBgWNa1G4u0A07wTAKOBcGcAuvXJOBVh1uo7BlfOh6CVdQYF8CQvilIKEQN-KzYjjzVJh6DBETDimi6f27L5xZqMd9BOPHhy99pGCh9pk2hlG2bUWLaiaBCyfurZ5z6_IqpjgS-LncK8CtI8HDxFupc2LI-mwH5dejSA5IbN0NvDVY82vHWlYAcSlyr_umnjDZN8iZF8mDeWWJVBhzY3BlveG2YKzUDvWS5mGeChAy-QmmBwxYzHfL3OxFXjOax3RfLoAXELgGuu6nBpetTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9YhCgMOFO0dB4wignUFiS6RgVLdthWRTG1P6j01QuWH89LWWixTc37uMG6XaAsuqjkFPBgWNa1G4u0A07wTAKOBcGcAuvXJOBVh1uo7BlfOh6CVdQYF8CQvilIKEQN-KzYjjzVJh6DBETDimi6f27L5xZqMd9BOPHhy99pGCh9pk2hlG2bUWLaiaBCyfurZ5z6_IqpjgS-LncK8CtI8HDxFupc2LI-mwH5dejSA5IbN0NvDVY82vHWlYAcSlyr_umnjDZN8iZF8mDeWWJVBhzY3BlveG2YKzUDvWS5mGeChAy-QmmBwxYzHfL3OxFXjOax3RfLoAXELgGuu6nBpetTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=ioBmN8Q3Ak-e28doWy1-tCJf8QU1KzpgJxG0m3golP5YZDkmn6rcd_HejRe6xyomJylm2T9tGZz55BAVA1Boe3xXq9JU7hchNzOKr1oVPLkyzM3CSalIcnAHdt-9NG73Kpfd-9jOsT9wnYtAvgTwF_wO5JzZqRv7qX2Yaxxmabp7FmnGW8uQxNogYmxsvaDq0kVprdhwIoTdovL7FOn4oMbo8z0geHATOGlrNqOwYood-ywNzf6M0bG54YOjyACfUKcu96bwA-tVzdlaQCK92xt8kA8S4pNLIplq7AfXjDhg6Hyb3W3Qoufd9FxvuVwMngV7C61O1HZDuEnt5quQXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=ioBmN8Q3Ak-e28doWy1-tCJf8QU1KzpgJxG0m3golP5YZDkmn6rcd_HejRe6xyomJylm2T9tGZz55BAVA1Boe3xXq9JU7hchNzOKr1oVPLkyzM3CSalIcnAHdt-9NG73Kpfd-9jOsT9wnYtAvgTwF_wO5JzZqRv7qX2Yaxxmabp7FmnGW8uQxNogYmxsvaDq0kVprdhwIoTdovL7FOn4oMbo8z0geHATOGlrNqOwYood-ywNzf6M0bG54YOjyACfUKcu96bwA-tVzdlaQCK92xt8kA8S4pNLIplq7AfXjDhg6Hyb3W3Qoufd9FxvuVwMngV7C61O1HZDuEnt5quQXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjDVLPkM4Ue7UJmMws8sDN9pHGCnqOBpCGJr3xokPVrjZLquiQECLG0GiGPiOqZ63NSBsPG41KQ_-knDn63iZbVEs0MMrRCd-7RjmrbT7h-2KhnS9gf9ua00hK75e5rLaMVOzdKBFwk9b1w9bWgm1B_rayipKJ1ERYGgzGAndGTZGEWhfnG_mH-ar3mAKmU2JTqNpQRIE9qeHy8movF6PtkkOgMOKndsZcIGNMzFUfDflQJGVcACiDvJotKDbmncxqwuXKiLS2G8On9nE_tsGJPdWnwy-N3FweZTOpdpUJO7IP5uwAdJ92PtYB8bpIyunmUoTiv952hjDAV2bzZy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=cnvq4NwE2lK1LYwF9qYOK0S0VKmNWn50A849NprwhF_p6nIxQDVrZ1pxByMttsozcYrqFmBN7nx1PlTHSjOvt5t5tFOjUJUMZYJC45WcZw7GYOVTI2Q3WVqxnTWHC0GenGpjD1Ih5EeEWdXge26x93RekILhY3RpRn3l-AlkQbkSEghWK8r0vtMDLCmjkkg6ymgW8GPaG_nOUZdk71EJ6BLk1HAyzbZyG0QWEFX9tErfGHrRT60nvdKuLEwFhzP_PYRiXsPu2HJdYcvHHFsh_FmgRL2gxcoAGOk4BrWvI5vHpcRsBPNTFzzeNyzoLUiMxhyYZubRj_NIq18Wj09blg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=cnvq4NwE2lK1LYwF9qYOK0S0VKmNWn50A849NprwhF_p6nIxQDVrZ1pxByMttsozcYrqFmBN7nx1PlTHSjOvt5t5tFOjUJUMZYJC45WcZw7GYOVTI2Q3WVqxnTWHC0GenGpjD1Ih5EeEWdXge26x93RekILhY3RpRn3l-AlkQbkSEghWK8r0vtMDLCmjkkg6ymgW8GPaG_nOUZdk71EJ6BLk1HAyzbZyG0QWEFX9tErfGHrRT60nvdKuLEwFhzP_PYRiXsPu2HJdYcvHHFsh_FmgRL2gxcoAGOk4BrWvI5vHpcRsBPNTFzzeNyzoLUiMxhyYZubRj_NIq18Wj09blg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=SuyakjYl7u6ekXZwrT6tbwY5viz9dsRG8X3ynHyOhfEWgrplINo5z3z0-qXfXQH4UFjCq-hwkjk-Veh1qWU2iO4ei2AmT3SCaU3O_lvHOJVIFWC7eogF6kRVyosSe28ITstCADe-KHWw6DkfZMZJtlwtb5MpstZxn6LF8M8suWxRYx33X3QtFbcYkcedDkq-rrzdrW0MvrhR0Ijp6dlGmOorITt4ItaJLjs_Zsg-0S86Zpr0iilEWjhKEOwXOo92pVIMPTjQrXLZ-SUlqOesXMBoeA_hxyHz2mDhMYlIXbaflOkFZeMHzptUfmkXlKaL_oY7aSQotzkPh81qlP3EZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=SuyakjYl7u6ekXZwrT6tbwY5viz9dsRG8X3ynHyOhfEWgrplINo5z3z0-qXfXQH4UFjCq-hwkjk-Veh1qWU2iO4ei2AmT3SCaU3O_lvHOJVIFWC7eogF6kRVyosSe28ITstCADe-KHWw6DkfZMZJtlwtb5MpstZxn6LF8M8suWxRYx33X3QtFbcYkcedDkq-rrzdrW0MvrhR0Ijp6dlGmOorITt4ItaJLjs_Zsg-0S86Zpr0iilEWjhKEOwXOo92pVIMPTjQrXLZ-SUlqOesXMBoeA_hxyHz2mDhMYlIXbaflOkFZeMHzptUfmkXlKaL_oY7aSQotzkPh81qlP3EZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=sPk_i0fjQ08HjoT4YJV-cGgH6qGcy8CzXnERQw8JZtL1gqgY9bAJbk5uyJYoUl2P4HZs8ZqydaU_sSbwMD17yJSlL8ard64ML-ixx77M9-7j9rnBL7N7V7GoJWQnjL0DyNBriBLb88PdQrf4LuLtXCkeNe2mA8d762Onv3ibB0cuL6-L6waGjJ9BWJUlL5JbvgcYWyI3glmnSuOcIIjUuY--pwFt1V9v7hiNoOMHNxpYFbbcOh3dpRsA0qLiitIgjUl6Q9lBqMxaQCDwhrG3x_2MB87Yz1xa2odSIq-aGFc1PEuWRtOW4ZuKkofmClDGSX1-sq6eNl4yUcZqN9Vx5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=sPk_i0fjQ08HjoT4YJV-cGgH6qGcy8CzXnERQw8JZtL1gqgY9bAJbk5uyJYoUl2P4HZs8ZqydaU_sSbwMD17yJSlL8ard64ML-ixx77M9-7j9rnBL7N7V7GoJWQnjL0DyNBriBLb88PdQrf4LuLtXCkeNe2mA8d762Onv3ibB0cuL6-L6waGjJ9BWJUlL5JbvgcYWyI3glmnSuOcIIjUuY--pwFt1V9v7hiNoOMHNxpYFbbcOh3dpRsA0qLiitIgjUl6Q9lBqMxaQCDwhrG3x_2MB87Yz1xa2odSIq-aGFc1PEuWRtOW4ZuKkofmClDGSX1-sq6eNl4yUcZqN9Vx5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YYxvuK71_VFjTJQLD0vnydALaCDtWBlFOgeVZMQuUMSjkD90hpPQAjyX8Jnh2MMeTo1fXCLox3K9YFyfPEbyuhdW7jM-I1-ubXaPiOyz_ikBnUUGA29ERV1d7IiMDpCfjo8jdTqbHayg5y3oq3g1kwNhSwxTFeip3H3KJ12VZFOEp-caMMvUsd7Qi5wst_OaBp_ez6gMS6xgE5BOIX6q95_Ckg9vJaJpWTV8acUFJzQufuLxTiOEUX6ynKu7OJhhCD7YyDGYQz9tC1ju6DE5mms_OrMxa6kwyCr2GbcukD9Grbg1mC27EYy9gYOoNkjau_v5hzV_1lhvA_HbAnSK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YYxvuK71_VFjTJQLD0vnydALaCDtWBlFOgeVZMQuUMSjkD90hpPQAjyX8Jnh2MMeTo1fXCLox3K9YFyfPEbyuhdW7jM-I1-ubXaPiOyz_ikBnUUGA29ERV1d7IiMDpCfjo8jdTqbHayg5y3oq3g1kwNhSwxTFeip3H3KJ12VZFOEp-caMMvUsd7Qi5wst_OaBp_ez6gMS6xgE5BOIX6q95_Ckg9vJaJpWTV8acUFJzQufuLxTiOEUX6ynKu7OJhhCD7YyDGYQz9tC1ju6DE5mms_OrMxa6kwyCr2GbcukD9Grbg1mC27EYy9gYOoNkjau_v5hzV_1lhvA_HbAnSK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCASUb_8hIi_kROaKn9YxyUuS-jmc3cdN94YiB8-1EQwCLFvHRqAeijf9DvYYY4wop8ZdIhK0Mv3YMqu6PrvSUAeUCduO4mfNUBPZ0YREP4G-Jj2kNlyjdPMQFB3MCxeUHqsHUlTX5YSLkLotgyQBv1qDlxVmfNajv2ckeapSVulY36lgek23bb7I2xINzhBjL5ElwbRX82S7gNuvt5NJ9gaC_8W03wuRV_4v8BeIh9QLXrHmUa6AswtKYUyrBcYCCR_OU0nS4ZZ2gehaec5jHFKKOXDcOLkQK4ayAz1C81g131bqdSxjjkYEDnWdBV0Q24S7w2PyAh6B9MgX86Tmw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=XdX_t162O8Q2-gHTzwO0DmVhFLssgM-HTNfsSxDRP6b5wpwf5msUaH9_knoxjE2XsIvKVn_TuUbolzybNfkemXCDx_RdBzPoJcFqsoUx4EPauXKO0ptRkALnSuBNRV6CcWeWhTda2fYGauAH2Bg42UO8tA7y0o1u-Sj-vA6xW3Sc4w7akA8eJmTosKA4T_2AJalyWb7PwEcrFQAhEPpjZGM36b8qsLirxawuneTViVP2wc7lIAGoVrmYBzdFOJ1Wjlrz_ye_fmcXgRiENo_dovcISP4LXe1ngsAwE2vqs47gSQR2HZaxnKp4n1duCPtVacywcXuGxFb4MGWEztMwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=XdX_t162O8Q2-gHTzwO0DmVhFLssgM-HTNfsSxDRP6b5wpwf5msUaH9_knoxjE2XsIvKVn_TuUbolzybNfkemXCDx_RdBzPoJcFqsoUx4EPauXKO0ptRkALnSuBNRV6CcWeWhTda2fYGauAH2Bg42UO8tA7y0o1u-Sj-vA6xW3Sc4w7akA8eJmTosKA4T_2AJalyWb7PwEcrFQAhEPpjZGM36b8qsLirxawuneTViVP2wc7lIAGoVrmYBzdFOJ1Wjlrz_ye_fmcXgRiENo_dovcISP4LXe1ngsAwE2vqs47gSQR2HZaxnKp4n1duCPtVacywcXuGxFb4MGWEztMwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=pBKhbpWOr4DVWrBnfi08njmWxxFp1Opi3ktYdNufwkOQeuFi73fbwlH74tG-PH4JHCi9qpKICMSvjN_rENrA_QcMowM98g3RG2DtFtM1gG2teElbQNOh0XW_2HCQH_ajyDgvekc0FZ2aOUW7EadWofjWJBpPNB8W-8d5Hw9DO6HXdA3gjNXY_HazHxnt-T_0O8CcUCUIcg2eleLYSSyNbMGRDMM62-JrbdWptMOVU_VO5wrOQN_zV_9-vPgmASVZ6nyQ6QhmVbHkHT9dMFN8zkzIRTrwAqfl-hzENjjOG_Pm3DiBPmyATSlZb9_aeT9qDtaYVwpQJDc5VrApu8CnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=pBKhbpWOr4DVWrBnfi08njmWxxFp1Opi3ktYdNufwkOQeuFi73fbwlH74tG-PH4JHCi9qpKICMSvjN_rENrA_QcMowM98g3RG2DtFtM1gG2teElbQNOh0XW_2HCQH_ajyDgvekc0FZ2aOUW7EadWofjWJBpPNB8W-8d5Hw9DO6HXdA3gjNXY_HazHxnt-T_0O8CcUCUIcg2eleLYSSyNbMGRDMM62-JrbdWptMOVU_VO5wrOQN_zV_9-vPgmASVZ6nyQ6QhmVbHkHT9dMFN8zkzIRTrwAqfl-hzENjjOG_Pm3DiBPmyATSlZb9_aeT9qDtaYVwpQJDc5VrApu8CnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRVyoFUNYjqNsYNJ8KVh_JPz13rEWHO7N5TN7g-4v-sx--7z-BDOR0YwJqebuG3oonlUfGK107ZZXmUaImS20NS56Ldo4RZmHXbcNtLsOvPOQCacxBDwVOs1jK7cHfvD38hfGgosFPLmI_A8Mf6WbWvBQyXXfluqIccVlqVOQTkcoI4gRgMFoqrq0UTbLFsirsKVZK933KXK0FgUn3qk40gW2IQTSnSuuxNOS2QDATaLZSshpeXAHceZ0kpRGHLw_4GK9ONqnaMiLNu6LE2ge-6yKgBVRh3JRii0UucTiLjtYbPpHiw2vVVUqED-s7Ej3q5Jt-h1l0ySwfk0M8pqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=LTVhsFZE4QIVoN7us58vt5JkUZtq3WDxjL6LW2J6HUsc_3sNNPH9jqBT0KjDA-wDeSGsUFeE3Tii41aUp4V1YdVLAKvFA7Le3QAQrIYvd0JhCxJRioX8qqRDhOqWcyt3lTAnGpjcbnw0sE93pkg0ttCZkyZQf9g1P4LTiS-cRj2cApxzzj5wyACldoQMVO8uojUI3EzYpoL5w9ykxQXSgOm3DHpdyNA5zKYzgba7kT2pxaYIxkyGHR3mV9s5fAeayvFuZ9MK4vu7KXefkMEejjrymCvADjAELKkCceJw915ehDQwo6MlPd6FN47T_OSKnTasmbmQPv0Cp3s7ngwsHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=LTVhsFZE4QIVoN7us58vt5JkUZtq3WDxjL6LW2J6HUsc_3sNNPH9jqBT0KjDA-wDeSGsUFeE3Tii41aUp4V1YdVLAKvFA7Le3QAQrIYvd0JhCxJRioX8qqRDhOqWcyt3lTAnGpjcbnw0sE93pkg0ttCZkyZQf9g1P4LTiS-cRj2cApxzzj5wyACldoQMVO8uojUI3EzYpoL5w9ykxQXSgOm3DHpdyNA5zKYzgba7kT2pxaYIxkyGHR3mV9s5fAeayvFuZ9MK4vu7KXefkMEejjrymCvADjAELKkCceJw915ehDQwo6MlPd6FN47T_OSKnTasmbmQPv0Cp3s7ngwsHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=VgH8i2jBPUZsWEEknm8qM3REyAvPTIJ-qWxrdcF78Wmil3kmee_DH-SjUdWce4BumJRfuOT8akZuqE1vqMuphH46lSMwuT_Rvl2iLdn422UmhAC2351FWjdkjA3PFsP5kFABW6qToR7L9TGSOpzFKOZkem1ahyNv2Zc6r5LO8080dEaZbsckJ9la0O4rUg1LVu5lulf45nFO_VqPMERzqvE9ZO0erBt05ETAvWHAvmUOf_aVQWGOM0GHBDgCCb1JKpIb_ZvuWht4imjjpAjXi7PafWCX4SHbWCN2wvDotczR5hCCkbYgpJXU882WJhgLNp9UGi12rqr1LYu9E8wC2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=VgH8i2jBPUZsWEEknm8qM3REyAvPTIJ-qWxrdcF78Wmil3kmee_DH-SjUdWce4BumJRfuOT8akZuqE1vqMuphH46lSMwuT_Rvl2iLdn422UmhAC2351FWjdkjA3PFsP5kFABW6qToR7L9TGSOpzFKOZkem1ahyNv2Zc6r5LO8080dEaZbsckJ9la0O4rUg1LVu5lulf45nFO_VqPMERzqvE9ZO0erBt05ETAvWHAvmUOf_aVQWGOM0GHBDgCCb1JKpIb_ZvuWht4imjjpAjXi7PafWCX4SHbWCN2wvDotczR5hCCkbYgpJXU882WJhgLNp9UGi12rqr1LYu9E8wC2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=fpVfy3N1t1gt_Z6ZDwDbSIlJobCOPbZiSpelkTgwYo0gJjcHNLK1MnpkADzyXANlvw2hseMJegEN89JFGKHyxEFISzEYoYBdADLcOPNXHNktSr1unfEzYtu2sNAnU-Vnsi3Fj9ejVnXPirT2U8zS7Dxrqj7XsxmOIUl18A4xtuJL9_Hpp1fdRuFwlOacZNXgSeFeUES07RrRYi15bE0seTxTySNxFx1OCrnyghExe3u_XD_kJJ3QHic0fChaw93Go64Srd45FEA4hUB2PPEOINzPbsmDmUZbDgzt-gY5CkVAqXYyCTw6Tv7WscfT1NAL_-QbX_uGeyaIaxH7MquAb4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=fpVfy3N1t1gt_Z6ZDwDbSIlJobCOPbZiSpelkTgwYo0gJjcHNLK1MnpkADzyXANlvw2hseMJegEN89JFGKHyxEFISzEYoYBdADLcOPNXHNktSr1unfEzYtu2sNAnU-Vnsi3Fj9ejVnXPirT2U8zS7Dxrqj7XsxmOIUl18A4xtuJL9_Hpp1fdRuFwlOacZNXgSeFeUES07RrRYi15bE0seTxTySNxFx1OCrnyghExe3u_XD_kJJ3QHic0fChaw93Go64Srd45FEA4hUB2PPEOINzPbsmDmUZbDgzt-gY5CkVAqXYyCTw6Tv7WscfT1NAL_-QbX_uGeyaIaxH7MquAb4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuS9clrpDXTOTkYXndE9OQKhxF1yOMwNeslc-41vwAPET_ckLjdcvaoDUoQWeBEwa1Z6JWGObD2XPRwFXEMzFQFnjNKsuHVEpwX_fHLiepp_Mds9sRvQ9Qzv6BvTcyT1BQGIz4ZhaE8gbtzbUESJ_J_00bC_9gLojjAatALamAjrgOtF7RDk9Asn6jw0NEYIQnjAJLJTobDsToE4NfFAbz-kNIe8mcfQKFmHARrH_VwpdJ3VYZeEo-ZPTwpj7h2ZsIOa8zpzHe__I8lzoaf-i2S5lSnGMEiZ_PN4cM89YZ0LMXJWQjjSCynOugH8bu7_SrcDuS9yQHP9NcIMOSNfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8AYBKxqcxVa4agYJcNAFDj0KUS37_L7c4JvRQ-DbuCgo9kyMVQuNeYTXCmpPy0Vd2FW6hLA9FIuopHM1xiPdBv481TmRn0cdSBf0nB9cemL0KHQe6jl5D17APJa-ODnxm1hb5DLfrxjuHuGNjFriNVOt4CGC6XOyUsyw9u10PrTQmeN5U29OKsuwIQG5L347OmrtW0U46IzzaD1hpINPZDjS_42p_bq7steztYP6pIA_Tl9ebAmXGKhgbb_kJF_RNOFD8SkiZvGX8S4IY5xme8FydI2HLEdXdxelylz_seUFK1kTDE_E33R57TT651Xn0k3KdwVUFMoSmOV2W6SpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eo3irDh4Yx8CCnXgOrsQ71nJIGVJ351B4N27879Gf43UutMlFeATtAN1xLFgVivnvXBAWoQrUPHEERouL29cuTTy7DdzhA8xXBbzr9VyuyE4zJZ2535gFNllV73DiuIrF1J-aQu4e6LH4RH7Gu9vH0gVeMqlOzpSRyPfvhoZnLEISOXtHG49jCyyojZ5bSdD9XqGqT-Xn_Fpug_x8gDfgcRSTmN7NWknfy3RncLhfMkrqZxlhfBfxrlQ79G9R3Xk9iUC8Yn4M87KsuycAIFIbx5kI6iKEd349jeZLmQ4RcmPzsfLoGVyBDQkO06DiYm_hm54Ahp3N2hOY1F0-0PvbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=S-Gxz1Hxe43iDhkCGsrwMqlu2lhFG0NtchVpCV57a0P67U13I8ooOqTYTUOY1f1mzA51R5Vz1zMfyoQjXSac8J-E9qIV29Ix3AA6n6sHpy3u3BYJcn7QTh176RtnnwLYa2IUSmMvajgqW2HwLRuFcjPKHXCPeg87I5mCIDezf1egqJzNMzT5y0APECb8LU6KUU6W4kbFftoPMwttCdDILujijXMZ2xvt6GUS8iSIf5R14NTKV3-0sJCpaWiLi1CfVhVVn5hv_NqtQ_fVuDupuDP-Pgv7gRI1qGe-ILCl4sF3toyGzlWP9J7TFX81mdLFbwG9T_cfN2Kw7wO8s07PgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=S-Gxz1Hxe43iDhkCGsrwMqlu2lhFG0NtchVpCV57a0P67U13I8ooOqTYTUOY1f1mzA51R5Vz1zMfyoQjXSac8J-E9qIV29Ix3AA6n6sHpy3u3BYJcn7QTh176RtnnwLYa2IUSmMvajgqW2HwLRuFcjPKHXCPeg87I5mCIDezf1egqJzNMzT5y0APECb8LU6KUU6W4kbFftoPMwttCdDILujijXMZ2xvt6GUS8iSIf5R14NTKV3-0sJCpaWiLi1CfVhVVn5hv_NqtQ_fVuDupuDP-Pgv7gRI1qGe-ILCl4sF3toyGzlWP9J7TFX81mdLFbwG9T_cfN2Kw7wO8s07PgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaasNoC_rcTEhidwSG6EeZcZ-7xTHORi7vcq9HKgbxp9yaz_mii8re_ckBMaPTltclKVKE494Ttc9QroJqoPDjrZ0c5yUgzi2VGDViacsxNNqwkeqh9HJVDnqIV4n9AP4wYFQlL6uhL_CwbEjEDQOvEBnJZYVfksAvf4ZZj9tX58phThdapKLkJV5ucQ2KGIMLco3SRUCK-CHBQyF8yXswtioGFPAaKsw0Am_RyXbWTK2GwnP4iwRrcaCDTuNTqIplHVV_mEDqjLSDEW1e7VFKhRIZUJ1EZ4yxYToL5UG8zn1Y6EzRYU9_mj5LE9b4oVNbbUI-7Un-yzL9WbHOHbFgsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaasNoC_rcTEhidwSG6EeZcZ-7xTHORi7vcq9HKgbxp9yaz_mii8re_ckBMaPTltclKVKE494Ttc9QroJqoPDjrZ0c5yUgzi2VGDViacsxNNqwkeqh9HJVDnqIV4n9AP4wYFQlL6uhL_CwbEjEDQOvEBnJZYVfksAvf4ZZj9tX58phThdapKLkJV5ucQ2KGIMLco3SRUCK-CHBQyF8yXswtioGFPAaKsw0Am_RyXbWTK2GwnP4iwRrcaCDTuNTqIplHVV_mEDqjLSDEW1e7VFKhRIZUJ1EZ4yxYToL5UG8zn1Y6EzRYU9_mj5LE9b4oVNbbUI-7Un-yzL9WbHOHbFgsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=dSh0vhPTKDs8twT5VvxZTpQ8xtag-TA7SnPg2-Aj5quoQPMlH1Oj7XX9CvaN5l1eIWulQuouaBY3ZUeh70SQtI7NqqkiXCkDL1OhypAWHqVm2JOJkZDjKuVk274-vPHQrFiiYaAXal6NdovxqAHxGvBdNMSEJDXn8xThVMsQHLYUAZPm5DNiftKLiqMc44cr5_hN_UiKxP4W_GRQ-lLYxolKXdNg9Q116UJY6COOC56jiz_Es1FQLlkYTCvwv-cvu7N05e-DC4e0XCA4K92ywfASy95YdMlmFi1EuKrJqwZgUQNVRHqwITkQ2QR4Yf5aLBWkwuEj8X5XkvHnF4rDhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=dSh0vhPTKDs8twT5VvxZTpQ8xtag-TA7SnPg2-Aj5quoQPMlH1Oj7XX9CvaN5l1eIWulQuouaBY3ZUeh70SQtI7NqqkiXCkDL1OhypAWHqVm2JOJkZDjKuVk274-vPHQrFiiYaAXal6NdovxqAHxGvBdNMSEJDXn8xThVMsQHLYUAZPm5DNiftKLiqMc44cr5_hN_UiKxP4W_GRQ-lLYxolKXdNg9Q116UJY6COOC56jiz_Es1FQLlkYTCvwv-cvu7N05e-DC4e0XCA4K92ywfASy95YdMlmFi1EuKrJqwZgUQNVRHqwITkQ2QR4Yf5aLBWkwuEj8X5XkvHnF4rDhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU4bS8sz_JpQoypnpFzhWZK4rBiVcp0nCIu4OtetSkC_6aDZvR7VfPk2AkSxjABI3M0s8T68egk5l2dX5TCX4SaEB0N17AFk3J6hompJOSnyaW6n8JCunmei_xC6LidZKzltwu8iEHysFtsTNa1GN4vE9exlNffIkiKSMeArli64qvkX0_fbh7rTEsRioCswZw8lq5UGYtroGXLYV3-zl_oJ_b4ZgNNJJhyHz7GrzniStLsNWGEED7qb1r7IF6VTEItdH9REmYT6aOTfOQa48fSG38mWUEEpVFsOEz0JR62AWTd4-7L1pGCump6XMLxMYe2oADbwgF_hJHgOU9gnzA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTiT9JTRpB6ghpp2EvpPx1o0R_bYd9CXAIq3RVjNq1vaEoW7g66UPR4f3Bhet72AdRiahTi7l40uH_pTcF1nsuZxDckB_chjHH0xOd2EP4jzafywI_7bPjXW0tfTo7ydxNpeudar3I_A7ZK5yiG8Al8rmEUme100LdzF_eNJ5eP2BRbdrlTyDK7001wz7t6PkMfmRERZDOejqxuafC0Y-eRQy7jKFMq8JG5_pqhkckWkc7UWGriwyVp2J7vjQIO6QX-tIoh9Y6-Gr3UGCSyv7yIBUwW5br-wdkougLMWh70AzE6bnQPKgO0PpWL-Dh5-3RlAzKtgrA6dMpzDlMxK2UuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTiT9JTRpB6ghpp2EvpPx1o0R_bYd9CXAIq3RVjNq1vaEoW7g66UPR4f3Bhet72AdRiahTi7l40uH_pTcF1nsuZxDckB_chjHH0xOd2EP4jzafywI_7bPjXW0tfTo7ydxNpeudar3I_A7ZK5yiG8Al8rmEUme100LdzF_eNJ5eP2BRbdrlTyDK7001wz7t6PkMfmRERZDOejqxuafC0Y-eRQy7jKFMq8JG5_pqhkckWkc7UWGriwyVp2J7vjQIO6QX-tIoh9Y6-Gr3UGCSyv7yIBUwW5br-wdkougLMWh70AzE6bnQPKgO0PpWL-Dh5-3RlAzKtgrA6dMpzDlMxK2UuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U17ItN8vR5UtsE2lIHa7g6MW_HYfvt6X_461whG9NHyCUzkh_c_fOY1PyJ_WJduvumaZHF-ptaXDanCRErCTr5VI8QC2sxHbgfRVj7vMEI940pMu7665r3tXq5enRVyb2uLAdi1Kh9ExOkc4B9fxOqPyx8bMi6pyflNJKAbfbqGTVdlZmCVHfe9RzamdPPhq1S3K51jkiop_IPmY48Maf7SeyDsrW1pDh5tTWqcqSA6mLNmxG_0nDnRxlZSUz3eZ0Nwe_4VeD__s-jlkIpIw6RpfHIV9vB9TA1dxE1v3sdNy-UbNC70xkFpj424iJjNGYfolPYmELQBi740tnE3PDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Yy5yvPYT4mH52t5lmdliccID0_z4y2tRr6GkdDQyZoznO2StEfQXYnpbko1otfPKROJkar6FfjiwyWJnibNZY4k2InxcpneX8n7ZCgUvtP9HGQqw7vi6GLkgjbGAH_aHyS2jmQ9S4YgK86AEst_8qYIzK98D_imxM7dDOZh2AtwWKYjr1UZq6slw3wf10M_2TjzumlK2khAPtrI5Vb0XoJ8bWlN6hKYzQvQle4PadvxadLBNIQ__1OBJjMIYwuS3Mum-kVj3LOQs8L_-4K_WgkKJJfhnceb4XF8GzapuafDHkVe_UIh6Ay-liaFxHLO6uF75lCIJVIiPLOC3hh2h1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Yy5yvPYT4mH52t5lmdliccID0_z4y2tRr6GkdDQyZoznO2StEfQXYnpbko1otfPKROJkar6FfjiwyWJnibNZY4k2InxcpneX8n7ZCgUvtP9HGQqw7vi6GLkgjbGAH_aHyS2jmQ9S4YgK86AEst_8qYIzK98D_imxM7dDOZh2AtwWKYjr1UZq6slw3wf10M_2TjzumlK2khAPtrI5Vb0XoJ8bWlN6hKYzQvQle4PadvxadLBNIQ__1OBJjMIYwuS3Mum-kVj3LOQs8L_-4K_WgkKJJfhnceb4XF8GzapuafDHkVe_UIh6Ay-liaFxHLO6uF75lCIJVIiPLOC3hh2h1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Tn-iU7Q_pupKKC6pZY9WNwE6CpfYa-N2318PC7RFpja7fR1utahg9EFUJvsxu3sgwxDV6KJUnIR52GBysYTWlOSBZwWoex2SeUQqQmNmYjeYKfuKicNRrlHDUbdfuvvGbYLA0GyF_U2i4MbK6YEUG_9ednFn5ZIHZ1qEBEnbDKbANPqa59T3B2NWkXcy1QVEMp0vgG-H8tzqoEpwbWNh1vKuDy7sKbaqlFI2kEOvgCVnMj0j0pWfKW2uiI2QB4zGHpdY-lcTvb0jZe1Cl1huaMotG4RmbjvkhMTLuc0YQTN3b_T69cIMz7GKLZg1K9hFcfAqtKP49VIhA3NHqSw8lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Tn-iU7Q_pupKKC6pZY9WNwE6CpfYa-N2318PC7RFpja7fR1utahg9EFUJvsxu3sgwxDV6KJUnIR52GBysYTWlOSBZwWoex2SeUQqQmNmYjeYKfuKicNRrlHDUbdfuvvGbYLA0GyF_U2i4MbK6YEUG_9ednFn5ZIHZ1qEBEnbDKbANPqa59T3B2NWkXcy1QVEMp0vgG-H8tzqoEpwbWNh1vKuDy7sKbaqlFI2kEOvgCVnMj0j0pWfKW2uiI2QB4zGHpdY-lcTvb0jZe1Cl1huaMotG4RmbjvkhMTLuc0YQTN3b_T69cIMz7GKLZg1K9hFcfAqtKP49VIhA3NHqSw8lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=h0eRyu8yT-mUr3gDnqS-ZZV4O5cUQd8XPkJV-bxwYOykG19zIih3zFXM_SQoDkRiFN1bMm3kYMeFZ7v7UkL-rlHnqAPzNASgMUK1a0WKSak_fUFVB4gdScPxhgx5Ro2hqwv7NxcWMqk7fV3EDi5k0vAjgVefWFaFdCOKNxlDdFBWiuSbbRPiQE9mi22cD0dBl1p0e8dQC03hBC5k_xVWagsc0hAtq_OJaM_9jC7MVkHF3gXUxNEEan4pN33Y4KuPjvzW3Mdi1F5pnnUhZ_ufBNNSCUrcwRcBduQgUYtcXSOpiMCdQEwSWGiWQYte0lyR4FBD6to_YTxfQzu7eMtNwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=h0eRyu8yT-mUr3gDnqS-ZZV4O5cUQd8XPkJV-bxwYOykG19zIih3zFXM_SQoDkRiFN1bMm3kYMeFZ7v7UkL-rlHnqAPzNASgMUK1a0WKSak_fUFVB4gdScPxhgx5Ro2hqwv7NxcWMqk7fV3EDi5k0vAjgVefWFaFdCOKNxlDdFBWiuSbbRPiQE9mi22cD0dBl1p0e8dQC03hBC5k_xVWagsc0hAtq_OJaM_9jC7MVkHF3gXUxNEEan4pN33Y4KuPjvzW3Mdi1F5pnnUhZ_ufBNNSCUrcwRcBduQgUYtcXSOpiMCdQEwSWGiWQYte0lyR4FBD6to_YTxfQzu7eMtNwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6vyxmnXAeTgsks0-AwIcgn2Ib4qfLgAG0pAc33RdLRMLsVwEf63wrbcDdMnSH9glGw9_vaZ6kDy165asIpotNV_nn7ztGYtfWlAIjmcsO4shrvbbwFlDo7Txy8cxcYmtGqBfY9iF6VzcQw876z5JudNSAwHRnQ9KAY-12Hp0boqXAjzI45TTO2gzerxY_BC_fdKXCYxzUTEjnt-K7yMMJ-O0cPocx4or2k53sr54dgpyEfiAcugTgewLtXXtqePathmJbFWcfaOeEZylZagfbxBNPzqVnIzNiAIDCP6K9fCwr_jUnhLnvXQp7rsmNNGbjz7zeiAw9PyQZUrnFAQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKNr9X__d7PKMLqodDojUiuvSsK_STyzdEIMQX-u4yrNaYbCdTdKV4sXDl1GJwLe9HxIPKavbLDVYODVsDoUw7Y9ZCKgPc2LYvgK394_vgJxgXjNBuCe8Y4jV3h4eHa6aJTFfJNmWfPxPhH2iCcGILAiRdAI-K7us5uu74LAMAN6K8VWNEPaJaiT_Feu-zNfl70bziHoxkCraiU3RAF5O6Jxdnz65M0UkbSGCqjpnqY8goxaAYprW4rw6MT8ZgEe90LmpVU_3Eab1GyinqRGIfvQmjepHElJLwauO5h1UogAYyc6_VMj_eumWvAJOgnxmHYvrB3ZSkzg-IP6teqtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Lh_M5wm8m5POrEhaN2copg5bNj71opI8srYt2tE_Z3cQY2sTQvlCeLwB3XBQkVbM1MpVG_o4onoqBJP6HZAuynZpO2qlvBnQ8qGjKjTI4Guyyv2aEBWrkk8Jeb4yXCDB458TH150wPwfh5EiYorhLtd7p7jyXztaLMMj015VfiG8sLXbOJn3xIwKQ9E2Fwh9limUge6psFVppKo66DY3fRmd91Gb8GqfF9WiyNdrve4Lg9q3PNXJOHQMy5mlel5zR-WEgSNHbicevJY7PRchjUgClF_55OIgcAmiURtnER_94HcNDh_EDXH47Wl99b6KdQZazyjNdKLT56o1Tm3zRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Lh_M5wm8m5POrEhaN2copg5bNj71opI8srYt2tE_Z3cQY2sTQvlCeLwB3XBQkVbM1MpVG_o4onoqBJP6HZAuynZpO2qlvBnQ8qGjKjTI4Guyyv2aEBWrkk8Jeb4yXCDB458TH150wPwfh5EiYorhLtd7p7jyXztaLMMj015VfiG8sLXbOJn3xIwKQ9E2Fwh9limUge6psFVppKo66DY3fRmd91Gb8GqfF9WiyNdrve4Lg9q3PNXJOHQMy5mlel5zR-WEgSNHbicevJY7PRchjUgClF_55OIgcAmiURtnER_94HcNDh_EDXH47Wl99b6KdQZazyjNdKLT56o1Tm3zRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2Q5lN9cT01VoVOJA80n9ncU3IR0XhX6rpQ3u7Pw3YdWq7Dfq_A_604Jfq-njGP5h9bMcxHA3bxFQ_2CYqlmqRKI7fNF6n_EaKE40fGIipuLV1oDfTM2ZkKm8EOFuUdP1HKlp78OJXdc2lcWTM1h6lqRhmi8jx0_Pj3wNDulD72rET0JEqNBh_xl54PP0XcfaKp1m2LrzD6MRaXch1UxLlp3jyOYpMAdX6iEybvljgbCW_PMbzmkVIjPmWlF5NoARr1oEIhnTAzx_r4AcSa1mqm-BZJSavQthuTrYfkyTizLmMYQYKRNti7vFn710AQmx8-jHVS9BrsihbuutmAFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnY3AwhKZGlS09399lyTRYmZiADrsXmqKEMcwB-WEHu1RMX3hDuM8TZX9iExHpSXGiX4uPfEFDRMT3iNqIuV5BMCLgvTkbK7iMQYD7LZ8kjRWbcO0Ycs1sKZ0dPb7Z5uY5zuKyx_ZXCi-zwSff3803RNv-EZf2V625vPz3nRm1fnLSST8t0LwwkMccZ8Qq-pPDNs5hR3Eft8y4BAKlmtKIMKgQ8WhOGyBFphlnhSsUurhTDQaRrEh1LC5C5MlHvrcCvn81SZpxeAkxKEL__LvZ4PmOAIFQ6Ct2s6tjwwFIpwh2thE7_iCYyjsVG8kxpPhsbhP-YD_MjnHWGySlswJA.jpg" alt="photo" loading="lazy"/></div>
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
