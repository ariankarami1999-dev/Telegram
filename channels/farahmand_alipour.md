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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 21:27:15</div>
<hr>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfJcmnNIrdROT93jUDFe16HicYX-kbjTEaLzBUWy0R_QbLUNh4PJliyZ4kXErbfaW-VIqicmP0PHKHP6TE_n-1dccalJvzeBTt44asoXAA0sglWaxMwPvYqZQADAoFp_vcWiaDlsnNoIg62hiDFY0FaYAL9-ESZ3Mzi-cl_lWXJMjZNSdJ7lLY9-63GFakJM-7xIPFdMgf4f4sCUplmCe5hs3I2pBK9pzBBtqWHWFh7Hdhopa6Vqe28JYG4Vnn0tABb71hDEogzns-JqNQuheogk7yxSVCHcaOlzH0oyXL-LabxJnReayoynf1qlZV5kxlZIyv0h9gLKmCeXQkO9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B46qcDMo6RYxaj-UxKkLkDM9oJWBs4YdTd2cuaciChQGftegZ2ON8BJtsJAhtasxb_TispDy_dF4vlsAxgRb33WoEDrjXyUBqJ8BxnlDp2H2oFkTzrHIqWMdib4LgGOj5clIVEBmaFu4Q7kLi68wAi26jSQ8eMffr-c7UCQE3nKGaMHI8IkH8LCUhAyLf_BA3xk6NYfFPVRAvyTp3KscA0XUsHscs4AwFq_HSOGCjQwO-Clks3Z9Q9Silb_tVWsCsf9IVvFaV9fz1KuE_vMoXrCHggX4OV9FcDePd76m4-o37QuF1WD6pN1Hc8y7nVqmAnyqK0SdZlJmKO5ZdGvRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWK3YjDqeqzxH3Ej3bQHsf0aynQAz8V_pUfw0zUuRadJZ8fHzejokSynMVkLE-AaMnL4_0y4tleLP8d-c_JK9PQZdgTwluUmoLnTbeVujbMICREhNwuJe0EW6xhieWoguPycNjbh_oXT9G4VWOdbmNZtSnAMze5-MPaUX0B69KOJzRbUpLQD5TDNGrTe-6_GVYiFiLGS-zJsnEhc8Bu80R3zg2QCE1ZhK8AwassKtYwXikjVSP9UHSLFQpcAAGpvoQZLlxdpAljPRd5q-XLKEJJmM7nuL7UVF9uZKQOtlG27J4OtXW0ABRZQn3W0znzkKBdYA0R9wAXuF6hpooiGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hLVQm0BHqiI2Tq7fGrDCFyKSffr8z1kXF1SJRdoaylvgwQZoZZxSua6maAY3gdR3I7Slp9cI_Ua1miJ47UvNS6E7MovRhngw6hWXfL4j_mQ4aixz-Iz7pwerQUUYGy35hHrCRjyMc8rRWkFyrLwkklr6eSg4TR1YhRp0qOoGbR9pxMt-cj-cSSr309-wZgEV65a-Go_rVTOcfOGGl_XboLIBNqzy26AxyPxSunzzyC99a1xeCXAsMFLc066lOr1XtEUpXeCM5PvyVxXnh5mvhMYVojFxJFPRLCKlgz_aHLLhGOENqdsXYu-aiDZ_lemUFi_ok3on9-6Hj7MDIDO8nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hLVQm0BHqiI2Tq7fGrDCFyKSffr8z1kXF1SJRdoaylvgwQZoZZxSua6maAY3gdR3I7Slp9cI_Ua1miJ47UvNS6E7MovRhngw6hWXfL4j_mQ4aixz-Iz7pwerQUUYGy35hHrCRjyMc8rRWkFyrLwkklr6eSg4TR1YhRp0qOoGbR9pxMt-cj-cSSr309-wZgEV65a-Go_rVTOcfOGGl_XboLIBNqzy26AxyPxSunzzyC99a1xeCXAsMFLc066lOr1XtEUpXeCM5PvyVxXnh5mvhMYVojFxJFPRLCKlgz_aHLLhGOENqdsXYu-aiDZ_lemUFi_ok3on9-6Hj7MDIDO8nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehXxSDLlUePGQsu6_bHEPLaz7rerSO839oNpE5JzXuURKpLtG1ehiTDDqAI58tbtaezQTzTI0YvGWknhYJxP3cv43t65JSviH0rhlDsupU8KLRifmakRQWpOwabJAa-IL86VCvUEoH_2nPexnOeBjuo1s35L7ysIWf5rT6mRjUxac51Q4vtUrfberdinlpAGEYDWKGyGdQrAKhijZGz_HCyTtKtFBIYUxR4r-F1QFUiSUYAFjRPPJzcP5PYSbNbzESqt9fSL_E9CGprvMjo590bxhismlq0oVl3ySAdeEuLt9mCNfwC2Mx31TyFrVAWqXAibFiqem1K15fSRaux-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=iQiJNm9TBbQFsB8iS3TZEMmSOI29VywwiTDnmMLk04mg0du_ORXkuFhxtc-11wTPDUmNDHkWQwbepO0DcWlSHE4cKq0jsaW8UlATDnq_8EAJvyAFpzPxbuzpKztvfA3WU3pcTmCIMpIlYLQjkw011k-QIF8OSuyJey5Xpa53lQ2vbOvEPR2JUSnOYhMJjOBdL4WfNw2QGKtLyTrR6RWiNQoZIQymywx3lqXwsSEVTjUTYqheoM70AJNI8D6JnkdZ7q1dXsjTn-Lazgt7PAfddF8X7_DZygVxnlV2AzcLaFSilvX4WO9t56r7qn2yZVX-EbT1TR1T2IHfK09jzXb66A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=iQiJNm9TBbQFsB8iS3TZEMmSOI29VywwiTDnmMLk04mg0du_ORXkuFhxtc-11wTPDUmNDHkWQwbepO0DcWlSHE4cKq0jsaW8UlATDnq_8EAJvyAFpzPxbuzpKztvfA3WU3pcTmCIMpIlYLQjkw011k-QIF8OSuyJey5Xpa53lQ2vbOvEPR2JUSnOYhMJjOBdL4WfNw2QGKtLyTrR6RWiNQoZIQymywx3lqXwsSEVTjUTYqheoM70AJNI8D6JnkdZ7q1dXsjTn-Lazgt7PAfddF8X7_DZygVxnlV2AzcLaFSilvX4WO9t56r7qn2yZVX-EbT1TR1T2IHfK09jzXb66A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRse3N2V068rU9beGyIY5T5n7JUj9rbI1NkoSejEDN-6CGG85EdkvG-zZnz59sbrSvEFfjVciVVuRS3WfFJ5WyfTUgC9qmUA7DcmniB4Guexax4291mW5WpoUwhnOxiyZvdJJY8qac31tMsys-hkNHhMPBZtN6mOHrBtiTwJZk7VLep054T8_oUQr1ze1fUNvmwmj6X-aG7liEBh3Eejf9scxFDLDPg3a6rC_lrEuelzNiMgCLcFZv481u5JAbTGvdQZn08eGAmQyTRh_nAMRr00OFHIE_ydTo0aFmM0dcbYXhPDgJz-t3Lvm_tQ_q88AltmVncGcEEO0iBgNdz91Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byZWSy2eymf3zD_nBp30Gi5zBoRpl51kY8R3-vTqBeSFvzjBQDQQ0g-tyXd1PuV_rFt5nZohQIQsvqwsjAexq3aEFeMdkLJRxcGWi8hRDsiNFEVI2maynJZDbd0sc_ZZzVvH4wrVYJ9vVD5W-FPHBxrmLFsQMZW1sL0Eb_m7-ajmSUFzs7njdlqPChHJ_Hze7tgTXMnNJ2H1NVCWy4qsUQeee27VTPjRxnQVSXWgyxK9lOoRQKiT7ssB5NknPgt8NOA7ogjSMqAKihXDi5anYsUlCD-Ha9gj89pRsfKrk-_FCENrhUj0Wi4yzHZc_eoOPN3XNgMfjoWW0RSSshuWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7a6wz4nHPALt5au-rFXhKdetJpBvDAdzYLACy349VAIL52l-yOMXVpGgqfp9qdVkvaUOXBCfxhiUbXm0Oxa7TJDE__0AkOQLX-nFEEZOgvFGcbuu4SN4Rf4nq5mcUzObVrjz1kW7nBdLhKTpQkTmfzI8ihurkyX3p1YePWYUulDsXvHPGzzcMIZoh27Ro-72USIPHMZ0PK6xm_wrvaNmwRUucjZDeyvPknR_F8wP3cGAsMe43Sud1NvSxc7ceb0Vtkc_oBLxxU7yk5JD3IFwW5H8yoOSDAG0fO6SaxEU-0fI0ISqcrXovqL-5GYsJRCw1ZnMfIiSMfDN3NUpiWMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILPrTfSpEk_IQJkqx3fVi4ZmEZLZBMDclJsMqFzFV-tiEYs_rAPf0eUO6fMkXXtp-6EgpIyh9WQ9emx5xTPQIMEYBdIkGHLdtzcMkQ71LCISZpu6jwvwtmaEOa0bGfbtFwGVJtFN3-OgIGh3z9d0W7UsQ3BWkZJ91Mnt5sSnzZeQJpqnDZNEnlcF2iwCFNbHXl_ww8a8M7BbVbR15w7z0_rzuLBsp2NOZAr8cZNFX6tTYNEgXiAJyN4-fTDQgJiXEbLs02dQKvqkDPPCmvJkeoDj6yVwL8g5gDSDvo0l2p71Q5ARFlVZPPmmNSd1ds1T8edI70F5BTooiFTBUkVClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKjobx8Ln2V_ARBpYErBnkW_YjDR0AB3-mWFCy7NcxwZkZNJIh1_wkDvGJ1HGG_j0a3Lk5xyfHFzOBpQI_XHYHjD2HrFRg9le_qEidlfcqOU-Yz21dRcIcNFcZe6445cG6oT_-EzifxIAbKbPotZXMPN8WDTo1JvTKodbaUlfcun7JiEM8rMl5YPGozpIkXhv8QdI0nJboSZIC9fq1vjtpV37K9UDXabl2tP7NqpkDAUeCuL-VDkZ9wq1npG6u1bEYZa4RkWgLcNMBJpKXUZ_sF8KX6vuhdGlJdPQEbqmz8FJffEmWNrX_jX3Fu1s36Vr5G-7J_fh1ZMTEmI5g4KZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfTIrcZ663Ka1iE2_uTHDwE_TEkZVSGXgby3a-LiYpddSZdgiIACr7__R04P3rwsPsFS5mNVOQtjGChM9p0ouAMHeWmEUSmqNpHsjxMyACkN7OlPQPgC44E1BcnlUHXLBCIg3jf9fcr1GD-3qUhP24vIjSUHSehmkmKswKrZG8it-pevDwDMRPjh75bevBiLH6Loj1kw12qW-nHqclIYhWRHwmQsEX5nhiVPm9tpua4RbxOYxxEFfRwn0e1Xco-Y1XgLZXtfeYTPLLPUKJM8sXbEjFQ9DiInoF2zkWiRvGhTT20fFHhXQA0rsOF6IaIt7zT5O9wTFz962k0pTiN5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TW60y95v_XzQXA0Tnb7BZLV1eZlK8sIF7ex5maiUccP2Pd9_ut5WJDUlPQSJFI5SofNqaTqMd8blh0eBEkBOYhV5yNzL13cI8-4BbcAX8SgmL6lzbxzRxpmXNz_L5OL7CGlsUI4oxn8c5phAbX_CXIzEGX1vwM97nn1jC2gRGQyuNGRgHlfApLqrL51XVun7A3Au_aTKRgmQaEqnrQxkDv-he84WV8AyjMyDVKNYy_2AzY4THwTQWJvatxK0OEObTTVOn9Qu5-91FWOJDc1HcLovU2t4RPTeRgwOtPfbygEcFKkPSiHZkqLhw4TyDkoGD5M9YNhYkGXUzxR8xgiSvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLjwiRvp-UqJh7wuJZKvfpSbipsqogLtk6nW9ga74csnou_s47i1EWp17N3Vlc4pytNZz24bfch77-MrP1W_5UZMOhjvk3aKt721gRDn1aMpVy3zpQ_Dp7h0JcHuFi5Lq0D_r9eIpsMvS6UTXzlnC0G4zEfjUKfRAixpa374Ou9qCL_TgS3RO1Wu6Uxs-9jVgmMNymvQmQnLJnfQeLEn5mzJOFsxCxHCpsX_A22F6zqrM4apqHnS_HzLMj5e7hEKpVVr9e1VHhwUrcht_aR8qoNfgmwchIfdWK9mTx_hPgOhl8AD8Y_RqeeRAxWhsqvY97j4Gp81paeZzSElqMs-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7imh_ZiOyquxlEhYiAYJzIA1W_jrQ5WzeC4aXvKpzZNiTuuWQhvB0h1-SiZdpJtQ6ZiOZNMAbeo1V2FnTrqm3CqDddG2jKCj_ruMJg7oMhMIs0DmFr6Sp8h5T4pG7fNp-usObI5x42MUW2bJlclXHjJWhkKeO2dS_k6gtB4dTs9cuJaBl8sNIDpjo_xDR_HyDJlhiiaAh_oEEBmuRr8DCA1XRAyoC1BR7Ky1aQRRRG4hQr6efKtNKY7ppb2Z9TgJE5ImVbfJe1X4XxcCJQ_y5tHlFsDiaPETT47mR70-Zm4YEGxJi36XCo9gAoOoG9A5U1NLaCUSrJUI4vVcHpjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUpmeIb-pNtNkUI_8qwphn-hTRk5LHwETheSFwGB25BoB-7dqR9jguWCmrXNxcsmpSl7DS0nwas5puir-yNNNtXoi_XjMCwJY9O715CpRnqNsWYKaUv0vhKAa6CnoQAsq7C1rOUFqG8vQxk9BJ_MCnREo5pYmzO9r6F5DQsnP2aTy7MXZhssW8WFeufkCqjyIfss0i_p3OqDHPCcfZ9PvPT7AuvC_dBHNLb0xn4PLTa7cpXzjW07jNloWI-eR8foTBNE51Jb6irrURKwvBgFyIYmYRcRCeXJHqc6lOl3HqTveWiyrBoc89PQ1Gkm4m6KgTwwQtpTBAR8p4iT33ECyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AThcqON36UJJmPrHqgOjKgPFpk_pl8TnczusREJB2kk46uVBGSA9fPiiD9jNljO5GNO-wVO-OmL8j8fxzOn_n-og1lKYoIP03OrNjecevC1JdHEICZQKRJarb6r8uPYMGEbtr0SObqjDASZnm026gsT8RsOsfrmb7lWoIvuezhgd6zm2vcGesHPgd8xokVpVovam9QtoswgNI2tSun4uF6NqIJxYmXyybLpfbc2fg1XXxcK5j2C3xTrn6_XQxmJxYFE9YI1cJ2IfGg3mDn3YOI_ARLw07n4-dqBi20wbpGsdnN3B4kw9LSql9D9Tsbz-6_40do-KxHr743QBtkibQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=JG6VUd5Oj9wL49_t11ApcHT9u0hpAjfynS1QYBY2l9rRJql3IIQ7lZPJa_UnSsRgj3oqbQyM3vPjCWuWlp-8QaFza5j5wN9Yl2VeqGgzRhvBJRWIqfWQnSYLRDQ_V54fciz7E3qegMHxBxs37Nx236W6SAxghfBa9szPof_u2rj4AKc8fmPcpx6Jdv7h8GDHp5JRAXQZavUIVs1eVmITfmXgFHfuNzxYWKjjuQKfHMSSkZpzTr3legEHxfg5zx8xV1Qmx4zK5428ZiLD5F-SyNa3V23fOUurfgXRJl1NTd3JxN0RcgO2vPJKe97aIPlXMz8Vh3HCQVb1LLVYq-DMnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=JG6VUd5Oj9wL49_t11ApcHT9u0hpAjfynS1QYBY2l9rRJql3IIQ7lZPJa_UnSsRgj3oqbQyM3vPjCWuWlp-8QaFza5j5wN9Yl2VeqGgzRhvBJRWIqfWQnSYLRDQ_V54fciz7E3qegMHxBxs37Nx236W6SAxghfBa9szPof_u2rj4AKc8fmPcpx6Jdv7h8GDHp5JRAXQZavUIVs1eVmITfmXgFHfuNzxYWKjjuQKfHMSSkZpzTr3legEHxfg5zx8xV1Qmx4zK5428ZiLD5F-SyNa3V23fOUurfgXRJl1NTd3JxN0RcgO2vPJKe97aIPlXMz8Vh3HCQVb1LLVYq-DMnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=qt5TaDvnwZAVrJDBW7eYH5JRsksPBXl0JoFKQpS-9YSnO7IRuty6ADp9cXHWO8EhUxk6RRJyiGUEgqx75yrcIqZDUMFJ_Uj2aSwGJd32KQZo7mFAjS_0YtbBhxRPZxuD7hReljwpuHdCP3g2iL9Y-FWDlxhCC8dBVKf-w_8QHv3A9gjlHUd8lZQgPB2YoMq_1kbVXfNgEY9qIuKoOGQzEq6YNdySzIqv1sH9dwjEfFr13dS5zmNTVDIxfwMk0RaU4DRwgCxUkVwpmoYzFGhPe_C8KxXV9lUQwVDmQ-RyC7aV9oY6B_v7nvYGxn10psSt3TOmj_Dl_Pmo9IBh7LuQ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=qt5TaDvnwZAVrJDBW7eYH5JRsksPBXl0JoFKQpS-9YSnO7IRuty6ADp9cXHWO8EhUxk6RRJyiGUEgqx75yrcIqZDUMFJ_Uj2aSwGJd32KQZo7mFAjS_0YtbBhxRPZxuD7hReljwpuHdCP3g2iL9Y-FWDlxhCC8dBVKf-w_8QHv3A9gjlHUd8lZQgPB2YoMq_1kbVXfNgEY9qIuKoOGQzEq6YNdySzIqv1sH9dwjEfFr13dS5zmNTVDIxfwMk0RaU4DRwgCxUkVwpmoYzFGhPe_C8KxXV9lUQwVDmQ-RyC7aV9oY6B_v7nvYGxn10psSt3TOmj_Dl_Pmo9IBh7LuQ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=qIFuhwalKHtXj_2SAo_AGRaCRYL04xoTwjH6gfMPFFF27_WG7n682FlpbfETqB0ctCNJIxcRUkyJrRbtcx_cmMo76Y74ZqalEwS2n0WdAzoDwG6WSUJgDKapXB9dnAaqemtOSUQd1mNtZr-K5RGIAmqbJlv7zvl7Ghsv99t3_6VGNQrlgBS1EBNlTqHCdp3fw2Gy4QZFGniSXHtRzDwj84NOaB33sEyCXZY6IANhJFZipOkhQ_oIstCFymG-g6mkdVu6HrxRgUVClcd7bnBuHuXvfoXhJVZiXO9cFC7AB7S3Wh4rXbqiMIv07HS4hbHT0jTeH0uGIi-InRv8AbBaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=qIFuhwalKHtXj_2SAo_AGRaCRYL04xoTwjH6gfMPFFF27_WG7n682FlpbfETqB0ctCNJIxcRUkyJrRbtcx_cmMo76Y74ZqalEwS2n0WdAzoDwG6WSUJgDKapXB9dnAaqemtOSUQd1mNtZr-K5RGIAmqbJlv7zvl7Ghsv99t3_6VGNQrlgBS1EBNlTqHCdp3fw2Gy4QZFGniSXHtRzDwj84NOaB33sEyCXZY6IANhJFZipOkhQ_oIstCFymG-g6mkdVu6HrxRgUVClcd7bnBuHuXvfoXhJVZiXO9cFC7AB7S3Wh4rXbqiMIv07HS4hbHT0jTeH0uGIi-InRv8AbBaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=sd-HWTw2L75iSlTFyKB_Cwsp1imd32kQGSsUfJVPqA8FkhaTcpc0Uxjz2y6qyuq8WOHCz6ctgwAOKxSkll7K3mrFaCwtrz2Rxt7tzz_JBUbNOcPTJ0NNuFsHz-m57AuM5KNhyGCFUvClVxmaF9LBSQoVgPu4qRE9LRiNvvNMf1uutY2dphh8ke_e41U3jqqyEh978Mw74B13_hvGCWbpHNNgYv2Tb7nRVWdzSMpIye8mUhHjFT0asfeO4g6SbUidMHbzSYuyY-GcTalx31OyMlNz8KkVtSSLUuRr98mwlfduenXvDPUfXyRK-wsntUy8iC7ho-WB7bN-3uRN_R9vgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=sd-HWTw2L75iSlTFyKB_Cwsp1imd32kQGSsUfJVPqA8FkhaTcpc0Uxjz2y6qyuq8WOHCz6ctgwAOKxSkll7K3mrFaCwtrz2Rxt7tzz_JBUbNOcPTJ0NNuFsHz-m57AuM5KNhyGCFUvClVxmaF9LBSQoVgPu4qRE9LRiNvvNMf1uutY2dphh8ke_e41U3jqqyEh978Mw74B13_hvGCWbpHNNgYv2Tb7nRVWdzSMpIye8mUhHjFT0asfeO4g6SbUidMHbzSYuyY-GcTalx31OyMlNz8KkVtSSLUuRr98mwlfduenXvDPUfXyRK-wsntUy8iC7ho-WB7bN-3uRN_R9vgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=Nh3_i9wn5yuIiZCPX3UfQwvubg37DVhPLMnu_jbkTtMKNMLIeKCOGhdE3b96u4y6FSv1U3mAg0udC0l1D1UXhFoV9aHkb_zL4W6xj8BFTnNXJDb5fzRwTDFlB4tISDX5WqlbH3C7Ma7wo0x-amDPSjQhxO2DJ-BJLOH8qcxn9RXk0H_FjwIPRlWpO8g3OQAht6lRwIq0gwTSizn-CGcPrbFFrUSudzzV_zWXhWK3LZw1RKgVN30Eg-rBKT2dkp9TlEeXfpuQehwRnlAFsp81RAt7wNuQTGxuyj5H97TV-mrFQ7RdbQ8Q0vO-mPiAlTcwJxInp7KbzNWQFgLh7XoBSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=Nh3_i9wn5yuIiZCPX3UfQwvubg37DVhPLMnu_jbkTtMKNMLIeKCOGhdE3b96u4y6FSv1U3mAg0udC0l1D1UXhFoV9aHkb_zL4W6xj8BFTnNXJDb5fzRwTDFlB4tISDX5WqlbH3C7Ma7wo0x-amDPSjQhxO2DJ-BJLOH8qcxn9RXk0H_FjwIPRlWpO8g3OQAht6lRwIq0gwTSizn-CGcPrbFFrUSudzzV_zWXhWK3LZw1RKgVN30Eg-rBKT2dkp9TlEeXfpuQehwRnlAFsp81RAt7wNuQTGxuyj5H97TV-mrFQ7RdbQ8Q0vO-mPiAlTcwJxInp7KbzNWQFgLh7XoBSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mqE1U4eJrOwWaVpb1IWL24DUTATdi8vg8_4zuu4b2UmcYxhk5OkYxNPG0spc0N8gcIWzsWxEE-3b0Ens3S9oouNmWo9iXbSEkmCXEaighkXKRDSJOTpsnprfGoOu7cBrtegtMClIh_1awnwQLr2aeRRa6BIf8KlqQH71E7pzHIixqIXy7lf7EcDPjsRwg1K-j7o3dGIWCjyV1Tk-sBftciK0_x2KvpCpC0wnQJ1p1mMMP7X006pzjs2Rwnl57uj7pkHzbB-mTXYpvyq8hKMtgRz2Lpj4T6dgp4f-1D0XJr53IcGiesHnSCRr2DmaKrxT35P2AZuchpxucrJsY9IvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=mqE1U4eJrOwWaVpb1IWL24DUTATdi8vg8_4zuu4b2UmcYxhk5OkYxNPG0spc0N8gcIWzsWxEE-3b0Ens3S9oouNmWo9iXbSEkmCXEaighkXKRDSJOTpsnprfGoOu7cBrtegtMClIh_1awnwQLr2aeRRa6BIf8KlqQH71E7pzHIixqIXy7lf7EcDPjsRwg1K-j7o3dGIWCjyV1Tk-sBftciK0_x2KvpCpC0wnQJ1p1mMMP7X006pzjs2Rwnl57uj7pkHzbB-mTXYpvyq8hKMtgRz2Lpj4T6dgp4f-1D0XJr53IcGiesHnSCRr2DmaKrxT35P2AZuchpxucrJsY9IvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=U-IGz_Z4c5wk2BG7GqSSky7s9gDGXFacJKHw_UnSruirQ-FQpqeSYEwGfeZz3kNhqv0KByMGP6YRyzWOzzIqI4Zaz4EII17STnxjSKmuze3QJBkI0YiarGyqsdagMsDAiQypD9qrNAnu-kZ7vDoDU8KCmL6DUtVEK_UBQze8_yBa_WsFS_gyVjIdnywwFbZeAnXsw9yzEClILsiATjiL8th9r-4dqYQ5s7yxz39z-msFEka9qWhVXSL50YbYF-l9NtyVQLxHtcfWFuj-uft--Xg4D6I2auJQYkgnHBuMKs4HDcMFbi_F3ZGH8km0mKuMgtOCIlwFkrXStb0pTrX_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=U-IGz_Z4c5wk2BG7GqSSky7s9gDGXFacJKHw_UnSruirQ-FQpqeSYEwGfeZz3kNhqv0KByMGP6YRyzWOzzIqI4Zaz4EII17STnxjSKmuze3QJBkI0YiarGyqsdagMsDAiQypD9qrNAnu-kZ7vDoDU8KCmL6DUtVEK_UBQze8_yBa_WsFS_gyVjIdnywwFbZeAnXsw9yzEClILsiATjiL8th9r-4dqYQ5s7yxz39z-msFEka9qWhVXSL50YbYF-l9NtyVQLxHtcfWFuj-uft--Xg4D6I2auJQYkgnHBuMKs4HDcMFbi_F3ZGH8km0mKuMgtOCIlwFkrXStb0pTrX_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKmhBvYfZw2J-Q3VS0aAHMmlA6C66UxJ6edfMKmHDNxmjr0BKQSZfo5hZ5i9O2b9pXIiny_ZwgamRrCRudsahVe54CVUQ9E2ah0owqL3yQ-Qx9gE9O9f5uMxQpvRYkVGVfyk-oTOe_Sp0ZGXiV9Ol4KlohTFVMZJF1KGn2ENMflE-STuu2_KcSwBEan754jeIUGf_QPmH5sdK_pNjfFUYtRvtK15C-Kv9g8OrUGbjOOpDUb6NZzPF3LtpLuept95wBY-_SjF1rekB_PWWbFEtwGb7U2_zO0mD9QkXrwka2OYuFhFClveUM32X5-t4a81RKLFu5lGmstOGdniOx9bKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uShDseHGNvOiKJRWL5AqDaFtsCHhifz3OYIg6GAOq_phelnkfdLpkUwh-2HQ0NMuG7nBiIFrIPVygWrD-6o5EBSRqBQbbkZdISooTkymlOiJrJNTpmzboCmOiRz_0Nml6AGfcPFCGP8XMt8k2VVbSylOQdPPRe2A_pX_AKyZsENMEGrrRMWOT7bDZYG1kDt0b5vNvvXqq87oROR8nXG_OSxhQK2o9sDTawqVWTNg5NchCPeawM7UdHlZ7lnzbZluKxFSzzQJjxRsCoDkFaqR3OG1SYkdzdesKE8zp3rYQDtg02rcL5CtpSBETZjHHg0YkWl3nV_Ul_MOsaNX-vqcAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uShDseHGNvOiKJRWL5AqDaFtsCHhifz3OYIg6GAOq_phelnkfdLpkUwh-2HQ0NMuG7nBiIFrIPVygWrD-6o5EBSRqBQbbkZdISooTkymlOiJrJNTpmzboCmOiRz_0Nml6AGfcPFCGP8XMt8k2VVbSylOQdPPRe2A_pX_AKyZsENMEGrrRMWOT7bDZYG1kDt0b5vNvvXqq87oROR8nXG_OSxhQK2o9sDTawqVWTNg5NchCPeawM7UdHlZ7lnzbZluKxFSzzQJjxRsCoDkFaqR3OG1SYkdzdesKE8zp3rYQDtg02rcL5CtpSBETZjHHg0YkWl3nV_Ul_MOsaNX-vqcAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=eINxLMjff4FIdYkUItDZWiD48fM4GF0sFpC1Qgxh9L4jwv-fiVyJ5VUTbelG-Y8JImksLxpL-uOcDZHJNh9iXD8cjC6GkktNjTh3dMj83f_LHSylvpiBhrdSNmQeV0sjc2Zli0kzOLIkyXk5HlGSwucRenoiqyLQ1rAWbi44bVKaUKPzP6ruJA-N8g7nLeiet0uBTqMsw-Ex3sYi0L2GEbG9DiCyke85TebAjob4GC_quCkFe_0ZBuvbt0FI_z2AQCQyTGrmDpadX2uvOpn-GZcK_WATcuC3BAH3DQsRPmI2vaOYZfCTwPF82t8aU8cRdyyghhZM_JXf_5sWiGemTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=eINxLMjff4FIdYkUItDZWiD48fM4GF0sFpC1Qgxh9L4jwv-fiVyJ5VUTbelG-Y8JImksLxpL-uOcDZHJNh9iXD8cjC6GkktNjTh3dMj83f_LHSylvpiBhrdSNmQeV0sjc2Zli0kzOLIkyXk5HlGSwucRenoiqyLQ1rAWbi44bVKaUKPzP6ruJA-N8g7nLeiet0uBTqMsw-Ex3sYi0L2GEbG9DiCyke85TebAjob4GC_quCkFe_0ZBuvbt0FI_z2AQCQyTGrmDpadX2uvOpn-GZcK_WATcuC3BAH3DQsRPmI2vaOYZfCTwPF82t8aU8cRdyyghhZM_JXf_5sWiGemTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=MlNWb4bemFhmHjbrmfiQnHEhXuwPhHAypOQOOkLtXT-hQnDroV4ksbUb3O-wwyLILnGl-PVp_ruBlMW07wiX42pOfU-v7SWc_8Z3rl0v3F69L_Y8E3Ib5apqIrE7m2l7_3Rfg96vAbLjm2t14rB-mWh7VNZI6OKm1NeGrKCtvuZ65pE9AwC9XRgejnoZWYJXAFH5jiEqeWkVk7ymr8DIV8LJOenwgU27L4-Kt0-efD3mtZ_2FMHXwMV0UsTFWkwCzP1z6kITTjx7yUpl8oh7BYSDVwTlgAfot8v1k2rdReWts_DHPBfeRSWTE7QD33-g2llTPQmP0Elh3nV1cp-BQnAXpnv2t7HiB_GgmLLOVBfXVEdEOT3p4TEVxyUW3qpymy7MWawaJaL05GZIEA9UXg2lMYXI8Djec24OGYDGT6u6uu_7WH6ij8e8bqJyxyVaD5C7t2laEMjYCa_RoaG-nVurwIvbqjZP3hVQyTumvS0-Jg-PDOtWs_6jl0naJG3VcAz_HD5IaH4o_jk9iYTqu1U27c1acPBkJzLg4vGCJNsSG1u_b2XHT4NTbxbQgmjJiKfKLblWkmPXbdNT7KD4CspttruHqbJkEqfW_tIUNmND2IlZh-oMjJwmZMyE8K3qxjWgQ4ncimKR11DkBgu2Qnn1DfAVIEg6pxaJ2Su32wM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=MlNWb4bemFhmHjbrmfiQnHEhXuwPhHAypOQOOkLtXT-hQnDroV4ksbUb3O-wwyLILnGl-PVp_ruBlMW07wiX42pOfU-v7SWc_8Z3rl0v3F69L_Y8E3Ib5apqIrE7m2l7_3Rfg96vAbLjm2t14rB-mWh7VNZI6OKm1NeGrKCtvuZ65pE9AwC9XRgejnoZWYJXAFH5jiEqeWkVk7ymr8DIV8LJOenwgU27L4-Kt0-efD3mtZ_2FMHXwMV0UsTFWkwCzP1z6kITTjx7yUpl8oh7BYSDVwTlgAfot8v1k2rdReWts_DHPBfeRSWTE7QD33-g2llTPQmP0Elh3nV1cp-BQnAXpnv2t7HiB_GgmLLOVBfXVEdEOT3p4TEVxyUW3qpymy7MWawaJaL05GZIEA9UXg2lMYXI8Djec24OGYDGT6u6uu_7WH6ij8e8bqJyxyVaD5C7t2laEMjYCa_RoaG-nVurwIvbqjZP3hVQyTumvS0-Jg-PDOtWs_6jl0naJG3VcAz_HD5IaH4o_jk9iYTqu1U27c1acPBkJzLg4vGCJNsSG1u_b2XHT4NTbxbQgmjJiKfKLblWkmPXbdNT7KD4CspttruHqbJkEqfW_tIUNmND2IlZh-oMjJwmZMyE8K3qxjWgQ4ncimKR11DkBgu2Qnn1DfAVIEg6pxaJ2Su32wM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=QMw1I4FHYrFo9c_ZsWS7QR0I4X1XAQOZ5AnZlx6aMKqPuYYnK8iiXSZVPShEPWhzzZNxeZWoGHwlOHJsxuWmMhU5kO6dOH1L16lTchec7jSSeEP4mkzt0mlyI555_cPS5h-H5QYIgnqyn9jMadmtGr3C04O3_lHh22dMoppAhMWU5Nm10K-jzgEGjP7_kloxNUEgcN8BeHNehRhKZrm6GpHlAkqjQtHgaVDrUSoy7_AmFH3GH5oaEoGyTXaOSELG70JtwXhO5nwl8B1AXr9F3lCxlG7-Fsh1cIeDNaa5X07aZLPVMjbeqaXTWUnSUqCFPMHpQjQvMymYwvf14BuSYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=QMw1I4FHYrFo9c_ZsWS7QR0I4X1XAQOZ5AnZlx6aMKqPuYYnK8iiXSZVPShEPWhzzZNxeZWoGHwlOHJsxuWmMhU5kO6dOH1L16lTchec7jSSeEP4mkzt0mlyI555_cPS5h-H5QYIgnqyn9jMadmtGr3C04O3_lHh22dMoppAhMWU5Nm10K-jzgEGjP7_kloxNUEgcN8BeHNehRhKZrm6GpHlAkqjQtHgaVDrUSoy7_AmFH3GH5oaEoGyTXaOSELG70JtwXhO5nwl8B1AXr9F3lCxlG7-Fsh1cIeDNaa5X07aZLPVMjbeqaXTWUnSUqCFPMHpQjQvMymYwvf14BuSYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tM7irg9HUIXsXuYb8sPUplEdrj4ixoT1zwz9Vkp2b1RG6eXz351MgS57WlIkJ7YA3B3vztCdiviNFz4HLPHlCQvmghYUFEl652qnZSxU-2yCOLS45UrU421sxYiEXTJSoXqkguOyuHKkzNPlwIL40o8hs4hUKxHvOXXgYVwGOh8uiBrlqyVgO2fbOoNdESwPVzXdqERKZrUSvDvaQ8HeFVeL6z2VfXVK-PzGODJ7SfIysLSdInyiBVWlm3c3DpKSbh23VgKExwpT9d3-IqtLBD5R56yc5kzjmQ8-FEOp0gj376CqGQbfg8Lyac8rJUrEedmoaiH6N8DcDGLyhnuU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODIk9t_DYAKru0pjRdXAqXpkcM4NBTyX9NjG2pkEb2EHGiwIw3qJxkmwclgo3VqwaAfGOsv-9gxSDSBZ0L0eOg6C_298cUNbNmlnQqXnCgq0iJ-kW2jLJE2PByt5EF-x3s8X-ckir-iK9WqTTsi3HObRT33iETGHWpkh7dErxOCuxJ9SeoRUKnBlHPUHbl7Y3NPB4KRXiiLQ_V1byZ7izX4m4RWylt6pTEC_lCNNPMF-69qwRajwG17vlEpA6fQZmeA2hd6NoqO2ZG64UN_kFTkKoylEIKk5dqnquzOxGmyEptxaKo_-WFbavmGd58l6sugS3TJ93VUktLVndARQEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=k6VnRRfwhlmzCDUuNU8-13o5w85pht8guPP2ooACg9c7E25XfvoRa3g1L0AOCgIcEJahzyw3guZxJZfhp9m7FQJywy6gRmEqG1JwlugEBwLRoeawjcnonhzGT57btveAAQglRaqowkCzfzgGv_XNd8XQiNxaldQJNJl4L--TrRQHqVaLgrb5l_8vMy7aIAc9es4XuqmoYJyklpBIQdFk0EVPFllzzm8Yqnfbwt5iPfNs6CKIfaRvO-n0sX0sYth72cMiB3hnaWqw1ahJHTumh_g4YJurJPhbNOT-LwoVhr3qYkRAmhtRbcFqpr0jeRr3mI3-KqNzvf6oaMNUiasgTRKyul7Xr7gQfD-Ujyh6gGK9TcxwtCsbGbCf7O9FkOmL6vCXKNMXBBG_AstJLVroOYTax3lnyPzz5-q47Z0wxxuQzH2v6-uD1sYCZ0iKNDqLel1eLRgJk3BdGo6Yo8_3a0BhLRibTTXHDE_2B5BD1jM82fFRi_HO9u_lNKfZdPtAP-MQy16uNUxTp5P8Jo4I7gqusQ5OoTRwPLDpUM2l9r-kMrbk0sh3D_fuYzkU0I-iAo7M6rwovElSLePmydlQ1Nr83E051Rycn0p8qTAisP-hvWacazEO_phXgDYW8GnM3wrZ8gReqTlSK89IZ8w5yeQOCEgBZQoNuqMDg254NgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=k6VnRRfwhlmzCDUuNU8-13o5w85pht8guPP2ooACg9c7E25XfvoRa3g1L0AOCgIcEJahzyw3guZxJZfhp9m7FQJywy6gRmEqG1JwlugEBwLRoeawjcnonhzGT57btveAAQglRaqowkCzfzgGv_XNd8XQiNxaldQJNJl4L--TrRQHqVaLgrb5l_8vMy7aIAc9es4XuqmoYJyklpBIQdFk0EVPFllzzm8Yqnfbwt5iPfNs6CKIfaRvO-n0sX0sYth72cMiB3hnaWqw1ahJHTumh_g4YJurJPhbNOT-LwoVhr3qYkRAmhtRbcFqpr0jeRr3mI3-KqNzvf6oaMNUiasgTRKyul7Xr7gQfD-Ujyh6gGK9TcxwtCsbGbCf7O9FkOmL6vCXKNMXBBG_AstJLVroOYTax3lnyPzz5-q47Z0wxxuQzH2v6-uD1sYCZ0iKNDqLel1eLRgJk3BdGo6Yo8_3a0BhLRibTTXHDE_2B5BD1jM82fFRi_HO9u_lNKfZdPtAP-MQy16uNUxTp5P8Jo4I7gqusQ5OoTRwPLDpUM2l9r-kMrbk0sh3D_fuYzkU0I-iAo7M6rwovElSLePmydlQ1Nr83E051Rycn0p8qTAisP-hvWacazEO_phXgDYW8GnM3wrZ8gReqTlSK89IZ8w5yeQOCEgBZQoNuqMDg254NgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwlazPgdNNsKnQiZjqhMYcc965QiY2XWxsgKmEp9HjTBLyURVP-wpzRXxycgkiVMCD3ax9U0fUhxthOOXQe4ZWYJ_hw4lLh9JeXb7LJ_vMEvvSs55wEhX4Uv8qkeD3s8d1OSWO5LDq_tsVCQVk14Wj8CvuSLuA0aYsYMblZEvr1kjMDNELkpZHEev0xWZUb8iWKld1ProM1u7OUQOGlwoiShTcOOPwhJ0ZYqhsYGif1ax8BRb0XZE0n1wiz7mjLARPAEuS1dTIGjw4VyNm3JEUUYw_nK0H3zNeMGQk-udDS3zvGIJxoBHr14EHrx6_su6UX6ybllvG9xFQrQyYDcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5aBQeu5--G5FgfRob9bJIBMxYfxKCB7Rl_YjuPl9j62PK2Jo1cv6AoLbrchun9ql1rBEwGQWFWyjeUw_D7xClPdFn4O2gDOFv1F-dUfhb041Y3nnc0vhuPfyc79AnY7k8NLY7GLHVwITTlf7kFUQdi1qWIXDPYiQ8mBaNY8Rs5_gKkshz6gwjfpD8WcicKZ6IVIRP-pPYUdhvv-Dvf02M7rB-eL0Q5pFZZlkGMWZIAwDw24pXUzKb5NydOqcMLMZxuOtymeDlCs0bobj0rU4kYN1b5ESXonE0LMYIk-0pFSnRuU7U46QfJumBB-gPLdfkJyqSp6h6yazscQwyQr2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENBaJipXDABbELlzMk_PyXtx38ksNyFXqFhk2dFE9gOlOFQJtsDHDumytO1kRTKODYcQWaGqyW4tERoyOc_A0rKJQzCWCXzReqy7Jl02ft6TeD2gPT3YXfHDFiA4IVY3I8Tiq5drDAmjhApnH1UNkpVdGhBfvmqMA-cKykIOMyS2g9PoAaWCKHaF_aaJObA0mkKWbv8yFNywUQeOsCBObY2jTCKk3XBSUfJIYizm-jr-MvXrrdBYSXQ2MIwAE_hmcv8lDQLZtmmxxqR1bA4l0obmoMT_MrbJ7VV8TNwg9XJJ9o-Ofu9zkBE6kIePlcKBqJP9DtDxMcx1Tuc2VeuK0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIqanxNFAikUf1IYVPufdZcVQk_C9NkC5sgPDdWpS7NsNJoSnBsUC0CgfaJ07LdDl_L6ks1F3E0N7iio5ZUYyDt6SL5fsx6IyBTosoL8SyRGxtNor3RMiBN0dgIJgzXHfrAvxn_QJ4ErA44JZVtAj5ZatQNeApSi9uIXEhRkfh6p32OSO308TsBAhFD05l_uOCxvInpDHwIugCyLeznqBnnwyAz2jlqxFlz1HeTsLKdSxoQEmCwnz8XlWbj7I36d5Hg4uAPN2PndgCfIg_QEAJe3TckMZtZwzA_eY7UaFdY_-fu_VQh1V1strvpwmS8u215Xu8tnu8WGlm_jIt2_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=TSxo59cDJtS7h1U1Xy5jR81Nbtd6_d0iG-rEWhcRJBcGo0DyltSEQ35bS7WmjeMx8mq6XemEU9H569bb1eBkmTvD6T-MfIVNy4PPQ5lg6XwITJbHvBdnxhZ4LcyFmDHvSGKhGn2QJudW3mzwxcVQXlsiea9iH2bouEzpiBbxzTWrbMe0KGzO3XWwIyF5z4a1ft7goOG0r11rrGc3GRqzafmgyMl4de7LzgJV9_4rlLd3dVoUEmGNAHNQBwVomxtsVfeO9ShzxzXfj-kYIl4A9FwcG904AtRauJpcZ1Ae0v4Zm0uYjnp1NbkuO4t_Kwd5ftRVGvbowlvQXzkdgij1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=TSxo59cDJtS7h1U1Xy5jR81Nbtd6_d0iG-rEWhcRJBcGo0DyltSEQ35bS7WmjeMx8mq6XemEU9H569bb1eBkmTvD6T-MfIVNy4PPQ5lg6XwITJbHvBdnxhZ4LcyFmDHvSGKhGn2QJudW3mzwxcVQXlsiea9iH2bouEzpiBbxzTWrbMe0KGzO3XWwIyF5z4a1ft7goOG0r11rrGc3GRqzafmgyMl4de7LzgJV9_4rlLd3dVoUEmGNAHNQBwVomxtsVfeO9ShzxzXfj-kYIl4A9FwcG904AtRauJpcZ1Ae0v4Zm0uYjnp1NbkuO4t_Kwd5ftRVGvbowlvQXzkdgij1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=nPPAJ7jlqxhUzieTyDdi6lXRJZn34Bo6MmM4rYtg7q2KPn8cMnJrf5-ZLUYeQ0omtsBuB2ImWiSHEniI0fBYpXN_AkuzgxW25nkL0E0pvGlHlBtNLJxojFbVvXyPNf26xK2_8wHWOvkKlHplTsxW3wBvigp31Sg1_O08vdz_vhJb94xqtzeovzIbjNhrSV9KV0A1lwiFeBS5lc05D1M8VpfKquAZ3a1huZELZu8mzvo4n544KyGjydcIjHJpROaDQSGPH0fotRWwpS2Ws8Gs0VHPRbnynjiZgUMzvv4sZRfjdq-EI-pJ-QNAmnR5Y7RPTIYgUsEgMKObZTRzQ7tnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=nPPAJ7jlqxhUzieTyDdi6lXRJZn34Bo6MmM4rYtg7q2KPn8cMnJrf5-ZLUYeQ0omtsBuB2ImWiSHEniI0fBYpXN_AkuzgxW25nkL0E0pvGlHlBtNLJxojFbVvXyPNf26xK2_8wHWOvkKlHplTsxW3wBvigp31Sg1_O08vdz_vhJb94xqtzeovzIbjNhrSV9KV0A1lwiFeBS5lc05D1M8VpfKquAZ3a1huZELZu8mzvo4n544KyGjydcIjHJpROaDQSGPH0fotRWwpS2Ws8Gs0VHPRbnynjiZgUMzvv4sZRfjdq-EI-pJ-QNAmnR5Y7RPTIYgUsEgMKObZTRzQ7tnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE5QO563BFsDg94NDmoCy58p4j3J08TWTkn497qs-s3xs2zQPziLwFBpcPKO3o3qme3yAF-g066BdgZPonooMKFKLFrjGRN-_pylBMvkGyK3rlhIwye93dn2vpNVZcZaLEwVT-WkfplwlomPd4aYCHJ8R_KG4jXtx-NsF6EtvkRmr_Xvdil2N7XifMHUwT5-xpEB-49VcNMt1iwh0H_mHXvKS29jBVQ-eYUtoo_57O1jUtbNz4eWPuBML2QBAvr9VM1BM0VVX3NYG9lY5JuWlNKhiG-D9W8vTfmj3_pa9lfcbaPddfKshhvHVXXJ9UVQ1bJ444s0J6LGFNERu3uCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=treIAdofkPXqHV8lr6oYRY6SM8tMYZDgB2AlYcGrU-2kqRAbXLLPAr4Czp3X8rGSektHazRiiwy2lMfyNmK9UiRBG9k-wIjWYiKEZ2ArvSDTFxX1XIoDSUNiCa--vTBOcAq885g1PlYxLWYz4g0i6gPR8qWymPY5temD3NoYhGAMeHdyJfnSDjfiyeeWUMAvsGowHUgY1Rf0CMgUTkFynNyPtu_C0ry4hT2W2zBXVIzIltHLFc9nrvEuX7yElh1A3chmkJFfk6-PDgHkFcfl10i8wSsUPtUL8MhNx0EY9jLXRqbUKCZ59Gusa6xVgcK6wUltsEKcwU5D3pMBT1j1BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=treIAdofkPXqHV8lr6oYRY6SM8tMYZDgB2AlYcGrU-2kqRAbXLLPAr4Czp3X8rGSektHazRiiwy2lMfyNmK9UiRBG9k-wIjWYiKEZ2ArvSDTFxX1XIoDSUNiCa--vTBOcAq885g1PlYxLWYz4g0i6gPR8qWymPY5temD3NoYhGAMeHdyJfnSDjfiyeeWUMAvsGowHUgY1Rf0CMgUTkFynNyPtu_C0ry4hT2W2zBXVIzIltHLFc9nrvEuX7yElh1A3chmkJFfk6-PDgHkFcfl10i8wSsUPtUL8MhNx0EY9jLXRqbUKCZ59Gusa6xVgcK6wUltsEKcwU5D3pMBT1j1BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=RPWJUULLOpXbPtUnZAkHi-jcfGICOffg-H9FTHCUTtYDkFkWdlv0nIuiH0_LFyGJJYrtCW4czvsQzTfY_dl2UbSkk6dn31j7ELjY25vshaxN2D8WNCn21Z6G2qdEPiFZSpzOYob_WEefA0kvJxY4ZMuCF4crCktvU3sFZMHeoXaehkKWkTdWgHN3oQv8_OR4TR1uVHzWyq81_x00PA2wGmZr7cM3Ew9Pc_h5nJcGMq70ggLQr6xHbAh_EtumOlCI3Znb3kSA0str5B3Y3pmP3iV282UdQroQ5UWfVJvEe-qzCf80jAJ6bBIqa-3bEqIpyrfSFZwM8ww1R67O_j-JgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=RPWJUULLOpXbPtUnZAkHi-jcfGICOffg-H9FTHCUTtYDkFkWdlv0nIuiH0_LFyGJJYrtCW4czvsQzTfY_dl2UbSkk6dn31j7ELjY25vshaxN2D8WNCn21Z6G2qdEPiFZSpzOYob_WEefA0kvJxY4ZMuCF4crCktvU3sFZMHeoXaehkKWkTdWgHN3oQv8_OR4TR1uVHzWyq81_x00PA2wGmZr7cM3Ew9Pc_h5nJcGMq70ggLQr6xHbAh_EtumOlCI3Znb3kSA0str5B3Y3pmP3iV282UdQroQ5UWfVJvEe-qzCf80jAJ6bBIqa-3bEqIpyrfSFZwM8ww1R67O_j-JgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=WnQYVDQBg2It3SVs6sNja7Bat7dBcg1G_sV9ZOEpXDT0_Qm4l-XXTwS5DK4s3i8CMyJKmGQBzeTvy7_mmLmRXoAbmXFf4IdnQbW2NQsczkgTSvetY2y0lTxpS9o6_krJ52z0KJksSX3FV2rclo5p227MeFG2_crgFd2uZZ6lNbB8wT-QG0YXxwbPUeGV7hdjlJVpCn2hbN9hSMd-jdK_7NiY8FOjIlIeqZORL6ao3GBdVO2ZcplCEhV-gAdKOOxAgPHDM18knfCSCWdEDRWbks9p6V2r-xFIiYYnbf5r0mGNNZLqOqDzJ3x8eDXvC7QDnwWhKg6RbM0FTcsn6_yCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=WnQYVDQBg2It3SVs6sNja7Bat7dBcg1G_sV9ZOEpXDT0_Qm4l-XXTwS5DK4s3i8CMyJKmGQBzeTvy7_mmLmRXoAbmXFf4IdnQbW2NQsczkgTSvetY2y0lTxpS9o6_krJ52z0KJksSX3FV2rclo5p227MeFG2_crgFd2uZZ6lNbB8wT-QG0YXxwbPUeGV7hdjlJVpCn2hbN9hSMd-jdK_7NiY8FOjIlIeqZORL6ao3GBdVO2ZcplCEhV-gAdKOOxAgPHDM18knfCSCWdEDRWbks9p6V2r-xFIiYYnbf5r0mGNNZLqOqDzJ3x8eDXvC7QDnwWhKg6RbM0FTcsn6_yCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnnT3B6a8gcRinHIuQsGIxrUqgpRcbLJsYuBnPJqDru8QQzaSxbClfxAP2hLcnxkw3c77AqXHI22orHHlBrBzA6BlpyVq-Hnns6_XSM6zgOh0iZtr9OnHwcvPXmmnbB5zw6tAb-sVWtCqMeePMkMHA9UUuUPcGGXKm_cvIhhXpcAO6mcRKUW_q18PHK9SthTYgHCaHvbSGCtJqo7bbqqjrPoFxke4zk9jmQdHbYwr6KrzEjhgx8VaO_yE6xCs-akVlDDidghD1KRWGdFHHQhxTYD-WdvnqOO1A9jhchzAJqcfHn8e-fLf5U5nvP2Z1yOYyv3scTTXl890Fp-RNtLGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=T35K4F1MmNHmvRl2AKeTxLAN1TwCai9fGunLIziapUnYW_5tNGtvbP8NQhlme9tijNg3XXjZA7mGSyZQ59GWG_eG554gkqUfH134bB9AuAjwlNUWCACKrLgSpd5VBD48TLjCRfi7Evy8xRNXOT7eL59o_uhFlh3qU8oEisNYH5cKHiUCHkqFx-7I-tmSd6dzdynLnvGR0mUaaWxIOJKPD_5c19yuJbRyarG0BANJH03IZGwd7ZSXC4Fhn1ykbU1Y8sUA3BU6A1_chqTYeBt4qi4N4pNRZM9IH8t8PS2WaCdAiZbwcJb7QkbAkejQDsaxMgFD8Ern_YgmhE6JFP0tjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=T35K4F1MmNHmvRl2AKeTxLAN1TwCai9fGunLIziapUnYW_5tNGtvbP8NQhlme9tijNg3XXjZA7mGSyZQ59GWG_eG554gkqUfH134bB9AuAjwlNUWCACKrLgSpd5VBD48TLjCRfi7Evy8xRNXOT7eL59o_uhFlh3qU8oEisNYH5cKHiUCHkqFx-7I-tmSd6dzdynLnvGR0mUaaWxIOJKPD_5c19yuJbRyarG0BANJH03IZGwd7ZSXC4Fhn1ykbU1Y8sUA3BU6A1_chqTYeBt4qi4N4pNRZM9IH8t8PS2WaCdAiZbwcJb7QkbAkejQDsaxMgFD8Ern_YgmhE6JFP0tjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfvSccpaJx_dt6onhKyR51U0KxiJnC3jMeHMSjSnL4EcBq7PYIMo53-FRE8khpnqo8LQHeyuf0p-BYORdgKb28S3w58juGVAGvwZ-HcxYu6zIQv9XzSuaoVhf6JAFeqeaId0CXiitIT014sR5XcJfFWnuTZcQTltLFrIsOhNl4xPnzt3snU24qhGqIkVWXiPvEe2FUU7FktxjVKB4mQqyxInuGOJSxSv9y4nX5vjkWBVw3_gCIVzAUvnBQH0FYgqM_xLfBU_w-115w9tcxFzRtte19wjESMzj1L1I860tckV_ckjyu5ZkelWGtBuc_n6SjHPvDTuWi8U1wNYb5DKUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDNQ0HKg719okeZMbLm8rej52Jj3naT2hUtY1dsnIXqyOXtm2jm79NOEN8plgdoXC8HFaaboGzV3ebCoC09zR-ul1aELASdYjJoayVstH-ju293vBIBYol2XIxpjY3XZHUBQmvkyHTTxVEA4bVLJzr3B-_6u6mgvjEnAPILOPHxLjiiCCmWaFzHYki-kfEcX167NsLrxw6Bmw9iKAa6Ots8xoxW7xZmPN4l3POrY0HdoPsF6B1kMTu2qwBM67d6taDRNysBYBv0mKmLC9mQo4qb1661hrnraDn6o5hDxM11dqsR9vIJW046Rhb0NF76N7370saH7VQVshmWfP62ppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=spK7Je9fwnmd90NuBBpHfjvGhqerJG4cfqXYQo1ANZ8knksz0BL1nV9llIZpS1DDn0QbIJX5wdmroIqhSCWHsKcG3Ar6c60jHcg7nuFQsyBfXXPZ_TfUqCyYNOGDsL9wyZZbKsmx8bLCB8Y-R0DlJa1gGn1e2rziA2r-T6LqM_YJyPA9juqMmcVNJVIJfn2vgNH-dQ_EIAlvSD3ios0dfy7p_vSTLDe4QlcH83hPO5f4OH2SSKDNPceHBgUPwCBgJ7gyf6bnLqcjBxF0RUhP1KpZ0BDTX2nL6z9LMO-pdmNSkP78ALvE-S12VaSaTkBN_yJFm1tRdyIgdzme0mH52w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=spK7Je9fwnmd90NuBBpHfjvGhqerJG4cfqXYQo1ANZ8knksz0BL1nV9llIZpS1DDn0QbIJX5wdmroIqhSCWHsKcG3Ar6c60jHcg7nuFQsyBfXXPZ_TfUqCyYNOGDsL9wyZZbKsmx8bLCB8Y-R0DlJa1gGn1e2rziA2r-T6LqM_YJyPA9juqMmcVNJVIJfn2vgNH-dQ_EIAlvSD3ios0dfy7p_vSTLDe4QlcH83hPO5f4OH2SSKDNPceHBgUPwCBgJ7gyf6bnLqcjBxF0RUhP1KpZ0BDTX2nL6z9LMO-pdmNSkP78ALvE-S12VaSaTkBN_yJFm1tRdyIgdzme0mH52w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9ZnQyEfG7Lwv-nVAC-pdVqHP9mA-WzZ58cCZ9X8ZhQ76lRzmg1Ho66s-XkqkgrL_y2aHRY6lCYqzzephrLF96QrILH0gvPeZTeoyxjb9XsHY-ZN0gUswTUoTbDKai6XE_hu_3r9mLA5tLTmJKhDaq2OzMtmignECqczay_C7pZtFD-_GYvajL20K6ImPVnkxHYnbDgPJTyx2nfhAt1s8WCUT3aE_vMI06AOUblcUJYyzCsUWoSUsR3Op6v_5-4SSbX1A2oFGPO1hXjJV6xPoOMi5wyWMuTnskdSLNcw62VO1DyTvpm9_EjsQnCvdMlyUvG8G0uC1uZAqvlfjt7np8yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9ZnQyEfG7Lwv-nVAC-pdVqHP9mA-WzZ58cCZ9X8ZhQ76lRzmg1Ho66s-XkqkgrL_y2aHRY6lCYqzzephrLF96QrILH0gvPeZTeoyxjb9XsHY-ZN0gUswTUoTbDKai6XE_hu_3r9mLA5tLTmJKhDaq2OzMtmignECqczay_C7pZtFD-_GYvajL20K6ImPVnkxHYnbDgPJTyx2nfhAt1s8WCUT3aE_vMI06AOUblcUJYyzCsUWoSUsR3Op6v_5-4SSbX1A2oFGPO1hXjJV6xPoOMi5wyWMuTnskdSLNcw62VO1DyTvpm9_EjsQnCvdMlyUvG8G0uC1uZAqvlfjt7np8yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=rl-BMZaRX-6tKKsGPRRc0Sy9cB1BJHDuWxvi3rBhTRmKJmDx8EIJBGBiawENYEsfgCO2LpR9MEGWP1u7P-UrZTLiNdXTjDDPxRyH8bvpwNaHFh0U-hD-DmqT1fj2R-PxrhnLO4ujYuziuH70UuTZl44OZ3FVIBmoDsVd3GYiJcjiSjdxWUypXnW3KfaXy3VjbqjYC-Yu5NcDG-GGXEj7gNsmF6ZhyafiCgMRZzgzRL7XjmC7GcNyNMnwk1mCQ0MZKLOuqRV25Whkr_8EghyEF29c1kuDgk-irNCjt3KmXFNxvPtijVPtjfd1X8zuuG8nJuswn60uziKqy6w0B0oF1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=rl-BMZaRX-6tKKsGPRRc0Sy9cB1BJHDuWxvi3rBhTRmKJmDx8EIJBGBiawENYEsfgCO2LpR9MEGWP1u7P-UrZTLiNdXTjDDPxRyH8bvpwNaHFh0U-hD-DmqT1fj2R-PxrhnLO4ujYuziuH70UuTZl44OZ3FVIBmoDsVd3GYiJcjiSjdxWUypXnW3KfaXy3VjbqjYC-Yu5NcDG-GGXEj7gNsmF6ZhyafiCgMRZzgzRL7XjmC7GcNyNMnwk1mCQ0MZKLOuqRV25Whkr_8EghyEF29c1kuDgk-irNCjt3KmXFNxvPtijVPtjfd1X8zuuG8nJuswn60uziKqy6w0B0oF1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBE2G3yaP_AxkQ_KGv2BfJLPGqe5ZBMlu0sSmwtP776Bcy8YX3Q5f3sG4ebV_4gYG9dZx79EPIKlZlouHQF3ZEdWYd5-Dx9MHEtKjnyrXzqaEQxGMJ0IXYlPAT1SOhpBUAMOd7RsaSx7gcnsMwZzzzLj36nUfKnw96NicA6Y8ahS76n0a7pYBiRveb60P6GGtoyg5A1jsRbW42bFrRLdWrduFoY6rAl8NmjoThG9EzVNYrcrpKyz2nweN8nLZKVdPAFEqNcCE9dnBYAUGYklt4DT4852_Im_6N84y7vY9OZHyV5V8rgKHOQhsswpmNQC5Dfs-jlC0USPh3O9vgU1xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=hUwgTfUFwvkPv4ZmlZXA_Qj4URE7JSpX5myL3WOmZKAG1wKfc9FGQ_yrLm7N_bck23av3Z-wcrZFCxaOlhGioxRR2ZYsFfU0Zry0DP-9T9moX4Xk99h7_JzOPeCiT9bJ6MeKPaXEjSVvL9fJYsSf_D11lDerU2u5Y3QfDbMQmlIA4uOX_FzIVtBXmWp1PXwss8gmmNMmZmHGSP9XQWE2If-8x_B5rGLzjYBk6HP1NgjhXJOx8ZmbXygW19DUDXg7fUKcP3pVnxl8PM6kprpDsCx7igQ_9gZZ1gg25GjXXu0LIue_Hv2kwYIh5HA_xehGNRBJLXHXhelGSntFG_b6fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=hUwgTfUFwvkPv4ZmlZXA_Qj4URE7JSpX5myL3WOmZKAG1wKfc9FGQ_yrLm7N_bck23av3Z-wcrZFCxaOlhGioxRR2ZYsFfU0Zry0DP-9T9moX4Xk99h7_JzOPeCiT9bJ6MeKPaXEjSVvL9fJYsSf_D11lDerU2u5Y3QfDbMQmlIA4uOX_FzIVtBXmWp1PXwss8gmmNMmZmHGSP9XQWE2If-8x_B5rGLzjYBk6HP1NgjhXJOx8ZmbXygW19DUDXg7fUKcP3pVnxl8PM6kprpDsCx7igQ_9gZZ1gg25GjXXu0LIue_Hv2kwYIh5HA_xehGNRBJLXHXhelGSntFG_b6fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=VWk3FUlMvTZO9Ndb46zNG_oVvCPgixiLfuUP9cf0EZy7gYXhIPYHBFqn1RU_sWu8cJ2Hh0Ix5pssLz3JaF4XFyrmYfylVDXRIdpJ2UgnYCDsW0AJeu-iL-UvPQplXKt5XD1QQmvm92gMSj_-te9nDxLUoB6VUboo6Q95P4XQFCPZ5WISAhRlFT5td81iuC6BFoeMrbWM__8FRL4UdqTbYrvf13cJ0gsHq2dlI0lP3qz_obY6Lc9wrVzdbrQVpvMkfl1KgOLzKD2RjUyVTuxmgvQIbFKVtGMXwYk2Gss6376S_PcL_XkFTcFg6hXWBat-rvupIDUtDzPhxxQmyMIo4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=VWk3FUlMvTZO9Ndb46zNG_oVvCPgixiLfuUP9cf0EZy7gYXhIPYHBFqn1RU_sWu8cJ2Hh0Ix5pssLz3JaF4XFyrmYfylVDXRIdpJ2UgnYCDsW0AJeu-iL-UvPQplXKt5XD1QQmvm92gMSj_-te9nDxLUoB6VUboo6Q95P4XQFCPZ5WISAhRlFT5td81iuC6BFoeMrbWM__8FRL4UdqTbYrvf13cJ0gsHq2dlI0lP3qz_obY6Lc9wrVzdbrQVpvMkfl1KgOLzKD2RjUyVTuxmgvQIbFKVtGMXwYk2Gss6376S_PcL_XkFTcFg6hXWBat-rvupIDUtDzPhxxQmyMIo4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=CMZ_Y7xk2LXPsfJCKAnejOARNw8SE9dxjlP7jJG1TNO6lriFqDllWq0iiar341KtftP3WNtKka0uNXKIUK9wu63Oukin1aTTWQ4CP5mIrMPOXJ4uO2yYgVWG8Eh7bpfLvw3ICFLfRhtc7hBlNsGlMr44FoMK0SiMhnH6YHxfOyzIgmjiJ82K3T7s0yKTHe7nRa_pkQ3aEFQu752fyhTLxhVZRqQ9v1sGsXpRYD5mZ_DTPGXoKdMvC9444990fwPyRN0uvaQ55GeqvafUSw_GLUDfNoeIR1aoarB4diuUqoxg7rhgGeZJeGrkyQciuPO-a0mn9g8DHtzbikK062SRAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=CMZ_Y7xk2LXPsfJCKAnejOARNw8SE9dxjlP7jJG1TNO6lriFqDllWq0iiar341KtftP3WNtKka0uNXKIUK9wu63Oukin1aTTWQ4CP5mIrMPOXJ4uO2yYgVWG8Eh7bpfLvw3ICFLfRhtc7hBlNsGlMr44FoMK0SiMhnH6YHxfOyzIgmjiJ82K3T7s0yKTHe7nRa_pkQ3aEFQu752fyhTLxhVZRqQ9v1sGsXpRYD5mZ_DTPGXoKdMvC9444990fwPyRN0uvaQ55GeqvafUSw_GLUDfNoeIR1aoarB4diuUqoxg7rhgGeZJeGrkyQciuPO-a0mn9g8DHtzbikK062SRAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ep87L36ix_waE_nHxPizsAn3A-Vzs9O28-UVGKzFabC98SZBOVmjkidI5k9fefYjHs2OR77RAC85LKVTpIj1Ggoh_Xxvjn3ILdwNXEwBjP58wv6phhdZjNayO6zwm2fW3y7tTHNSU2Dfbgbl02bdT6-Djm3IgF2j8RbI1CqaXZT8a-_zYHvEtF_TurX-elHZZmeNCCqFL1Fs9i-tjs8V42UMbm_cgfV5TUR-JeyRoaXu64CZMtOj6pKWvPgnQgkg1lv3XUDqlys7sV0TcfVZDGzkFRnK3NupN7dZPOHUkShAtCXAc9glJM7WmUhpKmzVI_7F5ecMDtFvtla257CXxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ep87L36ix_waE_nHxPizsAn3A-Vzs9O28-UVGKzFabC98SZBOVmjkidI5k9fefYjHs2OR77RAC85LKVTpIj1Ggoh_Xxvjn3ILdwNXEwBjP58wv6phhdZjNayO6zwm2fW3y7tTHNSU2Dfbgbl02bdT6-Djm3IgF2j8RbI1CqaXZT8a-_zYHvEtF_TurX-elHZZmeNCCqFL1Fs9i-tjs8V42UMbm_cgfV5TUR-JeyRoaXu64CZMtOj6pKWvPgnQgkg1lv3XUDqlys7sV0TcfVZDGzkFRnK3NupN7dZPOHUkShAtCXAc9glJM7WmUhpKmzVI_7F5ecMDtFvtla257CXxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBRj6T2UXcstzffB4j9PIbEj-9_sFDh10yf2_qILXmZuKqwOcyLCPPjLNvzmE9dY2ffxY1iXEw7_3UXXtDJbTUj5GTopwz2E_vknHyXTQxnzIULhyVLByaOrf_DIYcQ8XHaSo_AlVrexam3lwXoMo37xH5-k7FizExwMO7weztSDIsilmKpJvL3ZoTcstWpx2-ogme5JfLnkcCY4WzjZP49lelN5YzRZcn4gpLcqJ-Ze3xCX58kN-LvC5-Dsjy4pH3eD6P6K-EU7O57mdzJ_Z6nFL3l4RVYLd0KEnl0kRfBz6oH_ybC4nZ_n6FapussnZwHBHrapwegxdDiohSl0Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=oGhlKTtBx6o7WtZOtmnhaM8hYOUqWtIdaBc-B00HdwEkKKkhI4yokW81Zau_EateuQ4dqkMfyLdQclEPqs19tUqz3IzHvvhYFOuX1eXgbY_NzdDG-M37SvPFD8utEJArESJ_3R5HAkfEtgD6zKJojAvdxj3fXpHUWIRW343QTz1-deObouwfX3vHJHctWBslPYhtoDBx6ZnOQRtugNaz1Oonnh5BoKL4RaJSZhDnx3nEwSGwoddESxBdtH4DdSBUwrJcrCPUvIQIiPQmgO361wBEgoJz1eHi5w2CS6YtANR2v6DJ8kj0_HYqASFQz3XLRD52CoSZHmjr158m1TAttw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=oGhlKTtBx6o7WtZOtmnhaM8hYOUqWtIdaBc-B00HdwEkKKkhI4yokW81Zau_EateuQ4dqkMfyLdQclEPqs19tUqz3IzHvvhYFOuX1eXgbY_NzdDG-M37SvPFD8utEJArESJ_3R5HAkfEtgD6zKJojAvdxj3fXpHUWIRW343QTz1-deObouwfX3vHJHctWBslPYhtoDBx6ZnOQRtugNaz1Oonnh5BoKL4RaJSZhDnx3nEwSGwoddESxBdtH4DdSBUwrJcrCPUvIQIiPQmgO361wBEgoJz1eHi5w2CS6YtANR2v6DJ8kj0_HYqASFQz3XLRD52CoSZHmjr158m1TAttw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=vG0qyGxgDHloTGHZ3kRQpBpXqAsBfx_dOJ3wOmP3nc3_IeZAAKdNCZWR3H5e5TB3mSjd1xaQVWVlFGyfkOJO4p17QoDqiGpuC_TGT5FK8TAkNGw12LS-_Klmou07-QoTPzrP0vViiXkN-MSwBpa-0_DZ71hnL-6utilE1-TbtnfFuT34DG6NG5tHuddCtincF1JEK6FcVUk6-IQ-QQKYvSkovBNYApGW-9PvfN2Uk_WEqfuFmbSc4NkOzqgNKPgcemUZmurrO8zU5XW7QqrYBJ5vKvMsAnUXGhyfABFeGk_ifdrO0NmwVddCFStDKTajhIXtTXlFh3rgkBvaVhKUdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=vG0qyGxgDHloTGHZ3kRQpBpXqAsBfx_dOJ3wOmP3nc3_IeZAAKdNCZWR3H5e5TB3mSjd1xaQVWVlFGyfkOJO4p17QoDqiGpuC_TGT5FK8TAkNGw12LS-_Klmou07-QoTPzrP0vViiXkN-MSwBpa-0_DZ71hnL-6utilE1-TbtnfFuT34DG6NG5tHuddCtincF1JEK6FcVUk6-IQ-QQKYvSkovBNYApGW-9PvfN2Uk_WEqfuFmbSc4NkOzqgNKPgcemUZmurrO8zU5XW7QqrYBJ5vKvMsAnUXGhyfABFeGk_ifdrO0NmwVddCFStDKTajhIXtTXlFh3rgkBvaVhKUdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWA3EqNtrnl3Sk7XzRHMWUhALurUzFsnNsnf-zidswtVc_A5EN0lkZv-Z3Bpw7pGKBHTfN_KBgfWMI_3MnaZ3sGZWw5Z8Y6X-GxSyF6hE1AKzA-DlN8kOVwJ0DEfJ2Wv3skgvcJTxFDKqq1reYiq_xDV7xuoqeFw7_7TSaglB5yGKCd7FQ3pYyCMTFnjGRlFAQYa7bxLoIQHmoTxiEpWBUwj_rMhhA5oGFHhCVxZ-gtUlyEavhWydbDVKr2pVyZ3twHdZv9RTbLStQF5T9c6-EQPyhmimOdHklaPjk2n7L0sxBzhdkLTs7BT-p5blriuvSJGCLmMHix_X8-5BGFkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=UF6YBsLDdJeA45MZEuoR3pJNLlLXrHG0dNBBSY_bRXyp2ocErFEJbjQ-oxQd9iTigyG1xUewH3iNFh9PsieXbCsu2aqJdx6POLdUwlqVPwYxldJYKpfzGkD1a2tNzBO3zNa6rZ_NjvTkLinnVE-uy19u4AF8jLQxW0Mp0YA19Go5MxIoOrqbGtuOmjc0yiOhLeIcDvJlOlZhLSqn7_-osPgbwsthfSnvh41t6XR0kGXy39WdC4OtTXQVjp-ha8AmX-iSfMTr_c4Qzx3_oFGN5Y5v7MYbDsqqsLVVnHcbfsVJ6eFFLSgTppQJy0fudRMzMVWOe5OHt-AAW0K5vXfBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=UF6YBsLDdJeA45MZEuoR3pJNLlLXrHG0dNBBSY_bRXyp2ocErFEJbjQ-oxQd9iTigyG1xUewH3iNFh9PsieXbCsu2aqJdx6POLdUwlqVPwYxldJYKpfzGkD1a2tNzBO3zNa6rZ_NjvTkLinnVE-uy19u4AF8jLQxW0Mp0YA19Go5MxIoOrqbGtuOmjc0yiOhLeIcDvJlOlZhLSqn7_-osPgbwsthfSnvh41t6XR0kGXy39WdC4OtTXQVjp-ha8AmX-iSfMTr_c4Qzx3_oFGN5Y5v7MYbDsqqsLVVnHcbfsVJ6eFFLSgTppQJy0fudRMzMVWOe5OHt-AAW0K5vXfBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=pHWdWfxSDjPLAome-vf8LLZX3FxIQ6ZlfWeqQrNgaCurHMlLfnYdo6QzFOeFEenf1NLb1lckZK5pWbwakvEcZBgBiHd5s0hDHd3t_YgcDWuD-zAw8qNP6mqKxs3OuAA5YWCB5An3shQgtojlm6B0jnASzCnYTJrZjUmy54lTQCKE2L7RxqxW96BcrNEdMkd3wJLMJtDfhS1_fstys8oBKwZHgooaa-PNWz360N-E7beZtpWLXurj40_C-davsfLF8pj8AjLX_ykfoALnfFE_Jbt97OEz4HlgNsTUpJKHPlio4DHtmqev_6p_eEsk6D434Xv9_BwFpeNkWNrBwWxpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=pHWdWfxSDjPLAome-vf8LLZX3FxIQ6ZlfWeqQrNgaCurHMlLfnYdo6QzFOeFEenf1NLb1lckZK5pWbwakvEcZBgBiHd5s0hDHd3t_YgcDWuD-zAw8qNP6mqKxs3OuAA5YWCB5An3shQgtojlm6B0jnASzCnYTJrZjUmy54lTQCKE2L7RxqxW96BcrNEdMkd3wJLMJtDfhS1_fstys8oBKwZHgooaa-PNWz360N-E7beZtpWLXurj40_C-davsfLF8pj8AjLX_ykfoALnfFE_Jbt97OEz4HlgNsTUpJKHPlio4DHtmqev_6p_eEsk6D434Xv9_BwFpeNkWNrBwWxpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=IejGPRILn6fjQruUpr0DOBoMC3WoBnkllMoRYjAgtc_Y9f56j14EYTOhnavzsCVSs59EeESRiQuk9atm5XZg_DXdTHeHzwjuwqG_REqHe5LMMwrSsMEusCwIiVFRgpyOuVzPy0WmoTsEJjbh6xP8oEqe8JZ4wOhgsYb1zq5J3z8udilkXv7wi5VuG3vDTT9y15-PDPbcqXXy4lDhtXOg25-NqjPqgYyLll9aen0gXsuS_ep4Vgme0vJ0noT2cTVXdZsM6oM8RxpbGQvfwtqokzTARQBeM0WA6HJJM-bg3B6JQHCgyXnyLHLtt4e4CBX1P3wWgZHVv8Vl65XlxFGlCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=IejGPRILn6fjQruUpr0DOBoMC3WoBnkllMoRYjAgtc_Y9f56j14EYTOhnavzsCVSs59EeESRiQuk9atm5XZg_DXdTHeHzwjuwqG_REqHe5LMMwrSsMEusCwIiVFRgpyOuVzPy0WmoTsEJjbh6xP8oEqe8JZ4wOhgsYb1zq5J3z8udilkXv7wi5VuG3vDTT9y15-PDPbcqXXy4lDhtXOg25-NqjPqgYyLll9aen0gXsuS_ep4Vgme0vJ0noT2cTVXdZsM6oM8RxpbGQvfwtqokzTARQBeM0WA6HJJM-bg3B6JQHCgyXnyLHLtt4e4CBX1P3wWgZHVv8Vl65XlxFGlCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2fcHo-wkfxuCUxZig7ZawdD5pEgZKHq9FaCyrAHKkdXqKBqerczKYKiNcriAspfseIw9DLYIuFrtrfy-KJ7VR9iPhq0j-rt7sCuKj9sJkzQgVOroHljj4Tavd_UUuEdhTT4P4wYiDwKvOpzm8Uoshcg9pHlp1R5cs0Hacw8O8en-BxLhLBMdlvpVKS6aPA-RC7N79XSyi9crUU9qk729-ennUU5xMd7WLn37Pruj4E12tQ5r4Hno98c0_dtaqmjhLUtWrEX4n4s8MM3pQTBbEOLuJJjoCCCujWEaTZsC80uZ-VWpu_kWgCimrRmm5aejzlDauTf-Yf3IiRPI2pNLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9WjKaWdEYT6WKCZ-EnI_7e_gH1ipQeKnTD5aowZmybI2kdZkCOCGVgseQ5tzWJ0jGfgptE0yyfA_-k5YdDXnD6SplgSpBOSJGDoQtm4MmPc1nW9pQ-ZPquHyOh5KeHS2uvv-YWA__76KOnfUFRtrD62V2VN1s8sfKh3Fr4L38vqi7yVMlXpJYg6hflmw62lapLki0JfFYV48yRuwrMgswVU1g3w-qgFEBBAW7-dMlCjEst-hsFoRWo062m5pEn0xLTd1HTWnJAi8LD3aNj-MIbykxHGmtzNAdh-jdZkCaPdEzUiHs2XECs_i-h3ct_VryoZeUR0aSU4Cj3vwCvDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Koaa991gSOACNZVZa7M6FbkOn_DrWqLKzTacUobHGz4Fpo69jasT1z0WvDtSIIk9v9sqifvgH0wRMj91bLdldiQFHtGnNPFEDG2nV3pY1cE5MXa9x514MkXX8vFr1CsBiIrh0XmVGBGAml8NB-g_GL8Hiip84UjrfkqED3oYnxVlsYBtA067NyBZQksYwcFOLAufG5VE45OzlW0DDO_5nVRrrGcfXKxpOZJsAkAND-EOk03_o_8kcDE82hcnD4yAGUv-UKDIlDlqBR4PAfDslsz8WRbLeFILKemU7cIfpBMgaNo-Wm9GVLh13NQp2xeor7dW4ikRxT4YXs6nxF8g-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=tqPAIHS7NKzx5daCmlyjP0zch-jG7JzWHLSC48Ms3MTRD_XMfrVUt6Bx2UOnPxrZp4ulDmI5lzevVGOCyu928RHrFpkIAiRwu5iF8xLaozepfo7mu6Fbq1tOYC4pKs6_dIWyEQEQm1aHN-mNsTY4eaqYGEsmzb6cPsUhJ-oftlkhdi96DzsQKS0j9wNOrzbv-Q4Wxuej7BfXkzRt65K-yZy2Id5tbm5THum-SjuJun4_osISYZEmI0n_VxXiY2c5WwyQQywvrmkHOs9PBENKA6juCEiS1m4pIpNIxp4EmH2y0_PNvpe1uzKHRZY0QpyAnUzoTlyJ0n1u-QeQtgfZdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=tqPAIHS7NKzx5daCmlyjP0zch-jG7JzWHLSC48Ms3MTRD_XMfrVUt6Bx2UOnPxrZp4ulDmI5lzevVGOCyu928RHrFpkIAiRwu5iF8xLaozepfo7mu6Fbq1tOYC4pKs6_dIWyEQEQm1aHN-mNsTY4eaqYGEsmzb6cPsUhJ-oftlkhdi96DzsQKS0j9wNOrzbv-Q4Wxuej7BfXkzRt65K-yZy2Id5tbm5THum-SjuJun4_osISYZEmI0n_VxXiY2c5WwyQQywvrmkHOs9PBENKA6juCEiS1m4pIpNIxp4EmH2y0_PNvpe1uzKHRZY0QpyAnUzoTlyJ0n1u-QeQtgfZdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZkTyapCpRUWxqu0KFIy24srjPiXBixsus3HJE6NdNGsWUkHXvDYnuwGDGLcpWObKcZkjPsPMbJDfdflbitAjY3u175ncAMB4o4LXcOmhiGnUNdJElptPgf_ZS4tk5NqY4cDfBAn94e6jBHc7aQ4Y804Ocov_w7nvqa9j-VBE6TsLSA0WaPGQfseTJfetUYSkvzt9dI7n3bGPuqd7bwHiFUDcKwKgdFKJ8Opu4X55mBli48id78e0G45C-2ntgZWej6iF_OKswHbbkykvVUVeCftVeQ9DLg_MOigGbcvrQq88ASaireaYGAeCeh_761hRsx2Nj5SW4CwfoYcHbLZLbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZkTyapCpRUWxqu0KFIy24srjPiXBixsus3HJE6NdNGsWUkHXvDYnuwGDGLcpWObKcZkjPsPMbJDfdflbitAjY3u175ncAMB4o4LXcOmhiGnUNdJElptPgf_ZS4tk5NqY4cDfBAn94e6jBHc7aQ4Y804Ocov_w7nvqa9j-VBE6TsLSA0WaPGQfseTJfetUYSkvzt9dI7n3bGPuqd7bwHiFUDcKwKgdFKJ8Opu4X55mBli48id78e0G45C-2ntgZWej6iF_OKswHbbkykvVUVeCftVeQ9DLg_MOigGbcvrQq88ASaireaYGAeCeh_761hRsx2Nj5SW4CwfoYcHbLZLbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=l-6FdZEYwjN9mMdEezQyonCM3X19-V9sE9slCb7bAZMJRsPx_jpISp4d0nihu3KnNUuoPuFfQyk12jKlsdODNxdjlEkQrzT06_pydWcHnMhQ71usipnmoyOvYxcKDtHKIVmt63Rc8A3VeXpuL-J-YHTk3GRJM8dp5XSRipc7wSRmZVxIm28RnX9MNfuVRSVerpaDQEwdInJzIzw6iIwzx5bouQAkjAOeyXM-ZPFPJ6qJzL8Aa-kKx7Eh_9qzvtxF3BBjLE9TrMYsZbNibhCQoWijJzXY9_dM4u9sCgwwe9H82h30bFUMOe3Ng71tq0UV1ZjmStN1acScSKyOkDsppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=l-6FdZEYwjN9mMdEezQyonCM3X19-V9sE9slCb7bAZMJRsPx_jpISp4d0nihu3KnNUuoPuFfQyk12jKlsdODNxdjlEkQrzT06_pydWcHnMhQ71usipnmoyOvYxcKDtHKIVmt63Rc8A3VeXpuL-J-YHTk3GRJM8dp5XSRipc7wSRmZVxIm28RnX9MNfuVRSVerpaDQEwdInJzIzw6iIwzx5bouQAkjAOeyXM-ZPFPJ6qJzL8Aa-kKx7Eh_9qzvtxF3BBjLE9TrMYsZbNibhCQoWijJzXY9_dM4u9sCgwwe9H82h30bFUMOe3Ng71tq0UV1ZjmStN1acScSKyOkDsppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLlyyut4WtevidE2YlueRcQPcQyFCJf0mZpHihxR5P0Yt3QSvbBPWfc2q7r0nXuIw-h5YY2h2wU8i7NzGUGoYOhRwup7wgY4IF5HuJtApU4m-C2fw2EQSpFjbX2D5VvO44E32dTxbvfGvj7eR8n897_GPsBEhrpCUsesWHTESeR6imJ__6ga0cs3WqYB1hDjEX9kTGtmvGo_vNguts_L-qv1rIiOQp1lCDpWAaPCpHx0Bv-adzV0nFfhcGybpFZzGF1ulvo4ldpoopN3CvuY0XZvYCCaI5Fat1smDwqjni9IDxbWgpl1URP_lROUxcP0YJ6Pe-xlu6nBo399aDd0ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTmiKzPGxSqCq46AIUflxMBKvQWgv4B_3jjHFo9lA5NJNEvJWdN_ZbJ1OcowulBqC7bbVtr6-zGk4FszR6vvyBlc1iP7b49yFg22y1SxanVU6oO8NWoDAvvLi7mBAWcnWcO03pUcPeJqnElA7Zsbm_7-gz4AclOVfaWYyXoe1g2Afa-AAJVQULzWyv3Ty2rYdzSQO9UbU0xMLu4qMP1liYh1oEQZqIq-1YG77-pRzn3AtJZLCLCctssPdQvbtaJhnD3MKI1bCDWGxDAdD5rpu0eZX9WoxH8SP4MdFCvwWCGaaQvERs-14uGSp7Trw4DrACn-VtyJNPY15DkDY0lSHVsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTmiKzPGxSqCq46AIUflxMBKvQWgv4B_3jjHFo9lA5NJNEvJWdN_ZbJ1OcowulBqC7bbVtr6-zGk4FszR6vvyBlc1iP7b49yFg22y1SxanVU6oO8NWoDAvvLi7mBAWcnWcO03pUcPeJqnElA7Zsbm_7-gz4AclOVfaWYyXoe1g2Afa-AAJVQULzWyv3Ty2rYdzSQO9UbU0xMLu4qMP1liYh1oEQZqIq-1YG77-pRzn3AtJZLCLCctssPdQvbtaJhnD3MKI1bCDWGxDAdD5rpu0eZX9WoxH8SP4MdFCvwWCGaaQvERs-14uGSp7Trw4DrACn-VtyJNPY15DkDY0lSHVsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXinKCW4He_C-H89MN5Ysz5-rvjkMUqqwDw6K06RxUOJOFApOpm5FrX5BTPJWBfRa0gFOMwMJE38cR7F3dW1Mqdw18AFGWHgoRMomFk6vM3jQwFy6yXuHdW645sL1VZZposM2M_DTZ2ZkV0Z39lKAQVJrRCdPpScMUsmRpJtq7rEgNm6pYWR_5Bnb4QfA59lzIL6qHo5H9Zyn515EKhy0kTHLXoOeqwLBiDmDoh1-EvBEzJLdo0_ibBCCgg6SsmM_CZr5-jGounsfNR5zohLaEnQXHrxKZiF613B4g4e8tK8dGtcdGrgddqoGySOwo4qcHjzvATXcZEAqrAjz6rZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=M34xgOtp68rYlrwBjX9J3Ce-HOwJNDV2KaZABMD_S1gCo3ok0E7Ec_iAtRVQ8oYpHuGDTjyugLiK5MiEjlledpDKYrBW4Weo6Ru_NAtt-Wk_v21b1n6PVfVWzV_STvdytchRQi0EG-Xn3eqL0iojB5aLQLKy3adpBZ5liWLqrD7aLWnrdo8906vbxgbBzIlo4ItzcbxLEJpCynqXcyDmGCAEu3HoPvWNtsjULeTYtq60bWF_vQ2z-HCGTzXtefqw3DVVaXToRJCmJb7c7-jox7CLaL9uzJqFwANwCYDRveg2ZQYjS1x7E1cFBIaXer-3_SYnxKvgEURkm4opO9G3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=M34xgOtp68rYlrwBjX9J3Ce-HOwJNDV2KaZABMD_S1gCo3ok0E7Ec_iAtRVQ8oYpHuGDTjyugLiK5MiEjlledpDKYrBW4Weo6Ru_NAtt-Wk_v21b1n6PVfVWzV_STvdytchRQi0EG-Xn3eqL0iojB5aLQLKy3adpBZ5liWLqrD7aLWnrdo8906vbxgbBzIlo4ItzcbxLEJpCynqXcyDmGCAEu3HoPvWNtsjULeTYtq60bWF_vQ2z-HCGTzXtefqw3DVVaXToRJCmJb7c7-jox7CLaL9uzJqFwANwCYDRveg2ZQYjS1x7E1cFBIaXer-3_SYnxKvgEURkm4opO9G3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=AldZKmqbI4m5vZoUGtgc7-zJFtL63rDoxpg41ZwSCUMVICWnopqVAtezZxSVghAiPxKSnYAT0-xjAbfApoLj1dqQjyePJe3ITlSopqT9UayPqKU56TSS5ldOfR7XJMz_3QWEH8YqbUqJrDCyCZ161tPpP5RzJEZ4l1oNdaxawR_vMzcAvqFme47cZ3ip96ly_UXi7zQUrD_5SIklyYggVitRTbsL-ByOENdYVMSymNTfBX_BokBcAddnnBymLpuFjr9oKFqAGeuFHT1UuMPWxk-njVISxlGx7OaXhNT-l0Xb3U1ukwtlDV87pYiB6m7zhqzeo2ma0kxL-4WnrgHWUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=AldZKmqbI4m5vZoUGtgc7-zJFtL63rDoxpg41ZwSCUMVICWnopqVAtezZxSVghAiPxKSnYAT0-xjAbfApoLj1dqQjyePJe3ITlSopqT9UayPqKU56TSS5ldOfR7XJMz_3QWEH8YqbUqJrDCyCZ161tPpP5RzJEZ4l1oNdaxawR_vMzcAvqFme47cZ3ip96ly_UXi7zQUrD_5SIklyYggVitRTbsL-ByOENdYVMSymNTfBX_BokBcAddnnBymLpuFjr9oKFqAGeuFHT1UuMPWxk-njVISxlGx7OaXhNT-l0Xb3U1ukwtlDV87pYiB6m7zhqzeo2ma0kxL-4WnrgHWUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=spVrRwzxYH2qQEu1rGHBj4kZ6SeNzIJkIrz1EKBb7wW10MyhwrPKhuE8_5vQn3KPAIrOd8UAY-7Xtc7ZpWEVVhYOi9oiTEVle7LXZayocAxc6rMEJW2tyFp-py1RjOXf8XDadDt6d5ik4hMMzl5TwxFLRiaKMcpTdln6M013u9911yj4YB7MCSVRS5Il2n7WZcixNu2AMbv23FWKFbmmmefNgkCSO6sHcjb8_A2bwrphnbOmlYvPzXdaiN1JA2kDMO31TItEVaKqDSRQKjBbaapR6Z6nyoaFMjVx2xNmL_8OZHgTOPa20eshi7tO7IS9VKhFxVMWlf_z6itLHBrN6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=spVrRwzxYH2qQEu1rGHBj4kZ6SeNzIJkIrz1EKBb7wW10MyhwrPKhuE8_5vQn3KPAIrOd8UAY-7Xtc7ZpWEVVhYOi9oiTEVle7LXZayocAxc6rMEJW2tyFp-py1RjOXf8XDadDt6d5ik4hMMzl5TwxFLRiaKMcpTdln6M013u9911yj4YB7MCSVRS5Il2n7WZcixNu2AMbv23FWKFbmmmefNgkCSO6sHcjb8_A2bwrphnbOmlYvPzXdaiN1JA2kDMO31TItEVaKqDSRQKjBbaapR6Z6nyoaFMjVx2xNmL_8OZHgTOPa20eshi7tO7IS9VKhFxVMWlf_z6itLHBrN6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIt0CtwxD-2eHAYy4wDrDLmHsV2c5bB313Vic778HY6xt9ORX9s6s_btfANvbqL4P3Ku0JEmoqXTVQk7pJjeEEi3N3n3MHIevD42TAY7cjLXd0WU1XbIW7kA1G7Mw1V8Jnfz3OTJ2zbtbTO7WAsl4HewDAEDZHRj1SzgpbvYfSxEjHmKK64uP16ryAIBQD5atZ-uB2HFnZZoQM8WaGmoVzU8WJGmh3EYHnULR2zYgMlU3Ka1UhXhHYEfF0JYi6gMlQvS5iRmF8awJ6CdgHJNN0R7aY8ntxyfZkHFU3XkGWZWQQ0dOm4GazyehElO4UzpaMdiSuNhzGoXOUNnTz5mJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
