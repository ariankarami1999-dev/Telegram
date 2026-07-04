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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 22:37:13</div>
<hr>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=YhiS8EW4ZqH0MDnuWTeaGgZrz6jle8b-y4r5svt32NQ_X_dXrf2ygVVWaf4PS4KGdoKQ1nX1Cy5LEgDBBj2MSELPYc8zU5cpMm5_l2E1w0S-AlY8vuU13rU7umlZUrYXey3rr9PAGdfFd73QQcWBM8H1gP6UamN5wo0Aj_W2Rk3brHumbtm_pYZB6ZrF_Ixb0EoqGKYN3HIsr3fDDcvGkDjrxFYf4-XiQhnc9viFx5saVsMgvBhEoObTUJA334LbdCSRRohRADXWXdBr7zxHdj8n-GpxP1okbQFIt0PpaOXAEyMYUtq-hkEc8BSyp9KTYJVoGsK28EXAJ6AxK_KuNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=YhiS8EW4ZqH0MDnuWTeaGgZrz6jle8b-y4r5svt32NQ_X_dXrf2ygVVWaf4PS4KGdoKQ1nX1Cy5LEgDBBj2MSELPYc8zU5cpMm5_l2E1w0S-AlY8vuU13rU7umlZUrYXey3rr9PAGdfFd73QQcWBM8H1gP6UamN5wo0Aj_W2Rk3brHumbtm_pYZB6ZrF_Ixb0EoqGKYN3HIsr3fDDcvGkDjrxFYf4-XiQhnc9viFx5saVsMgvBhEoObTUJA334LbdCSRRohRADXWXdBr7zxHdj8n-GpxP1okbQFIt0PpaOXAEyMYUtq-hkEc8BSyp9KTYJVoGsK28EXAJ6AxK_KuNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=dBZtCl8BDArpFCqwK2zRkfAEgWsDfhJ-Ejz8dBBVytQj3M_3z0LO0jMJTpeLFORuAOLJ3hqFJro0V8PNQnbcR_-A0ayAq0oZ6ndzZyjvj7G6rxv-hLCuvIaru3bE1pzFiJYz8ZPgYAIuFuUsklBNsg6sIH7aYpSJSeTXiQ9_-l23lXUaLqyNrLqd6pR1IroqqBUQnvH0A-PCGooxNaIkzIwh7VCSDIk7z3ze0Jlv810IFu8XsO85K5VCK_YNdCrgrh-F7iUdN8Q-APpwzGuZI-8VVeS0mScpqW65NM9HVt7mOeJY682oASovLPu7N181Cky0upOrPubXXjrSi9yhwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=dBZtCl8BDArpFCqwK2zRkfAEgWsDfhJ-Ejz8dBBVytQj3M_3z0LO0jMJTpeLFORuAOLJ3hqFJro0V8PNQnbcR_-A0ayAq0oZ6ndzZyjvj7G6rxv-hLCuvIaru3bE1pzFiJYz8ZPgYAIuFuUsklBNsg6sIH7aYpSJSeTXiQ9_-l23lXUaLqyNrLqd6pR1IroqqBUQnvH0A-PCGooxNaIkzIwh7VCSDIk7z3ze0Jlv810IFu8XsO85K5VCK_YNdCrgrh-F7iUdN8Q-APpwzGuZI-8VVeS0mScpqW65NM9HVt7mOeJY682oASovLPu7N181Cky0upOrPubXXjrSi9yhwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/od-axk9G2VPHukBgFiNjNyBxDEkqdX1imH9cFxYnRCI6vB-HM7qLxiTFbm-lrupgN-RpxRp4VsoYDtwha35oetwNMm_yMQpUNVuc8HyDoVvykvaJ8w2uncCH1zjGG7p-qvy4JX-D-GlGyi6JETT2U6Dy95-YrhWKLQ3bbuw1tQQ9R11Qr6w8kNXVtY43fxR3jqkucvTLT7uruOXWqiQkqeBfNiWxlWWPiNVtZ8V6W9R3Z96mYwPMyIf8jiZzPVB32CSxmnKUA8-dEVAAU4zulXZHef4rEj5zb2VcqRN1OKrKQeXEk35MRN-XHbc1wWmJajqbZYKBMHyRcOLdMHuiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=gvhg9YpAHT6ZlT9Sg8V7CznH4hQAYJFyGn-W18GVYmVeghnuNPydp3XP4rVRg2XO5lAqcNDm3H8mMW_VzSjY13KhGcSl790vQBFQ7fNVY0PKkosH8wFyacUNESOvDNxs2gZjP319j1TJ4Jv5BIsQsVn7olRGO0y5-_Sm7GuA7gT7m5cvs0r7fvHjWeM2qkhHykRSfINq3qbJVtWqs1_BWCcjAu-lrw-4qoutXYnCckPdKdK21kED3eiqTBzd05pBSU8cUlHF3rNx-qEDCFwncapypWNqSHRfkuzE7ryZh9nNCprlJbGRrpaAkfldjSgiAmUIwpfZjetfa8D0Ww757g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=gvhg9YpAHT6ZlT9Sg8V7CznH4hQAYJFyGn-W18GVYmVeghnuNPydp3XP4rVRg2XO5lAqcNDm3H8mMW_VzSjY13KhGcSl790vQBFQ7fNVY0PKkosH8wFyacUNESOvDNxs2gZjP319j1TJ4Jv5BIsQsVn7olRGO0y5-_Sm7GuA7gT7m5cvs0r7fvHjWeM2qkhHykRSfINq3qbJVtWqs1_BWCcjAu-lrw-4qoutXYnCckPdKdK21kED3eiqTBzd05pBSU8cUlHF3rNx-qEDCFwncapypWNqSHRfkuzE7ryZh9nNCprlJbGRrpaAkfldjSgiAmUIwpfZjetfa8D0Ww757g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=LeIRvgOZnBpCVyduk8iSD-Q-V-7kmzB2jl0W793k3laDsMOb9pcuPfkQphVWifDuhpsBMcInGuqQRKMqP0sg1pCxWAEHOWnbPlFFnuPY2veczayqnVdWu1vRbbO9bg6PswaLcfIWK-UpawjBitRDnEqwakYdKY1R_EV_hOoc9Qpims737Rpa51iqFKJ64hfyvt-umGbBxcHh8sUxFRS6jrtKZsvpBU-OeTwFj-rFpbMKMjyir6EXev1LbpNcqxv7DTgw64I_093Knf8LSbG_3X8PNgfWecjRt6M4vm6H-h63VSPUkX1XfQYHp1rQMfv0A8clsAjW0bsM97-xc0PWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=LeIRvgOZnBpCVyduk8iSD-Q-V-7kmzB2jl0W793k3laDsMOb9pcuPfkQphVWifDuhpsBMcInGuqQRKMqP0sg1pCxWAEHOWnbPlFFnuPY2veczayqnVdWu1vRbbO9bg6PswaLcfIWK-UpawjBitRDnEqwakYdKY1R_EV_hOoc9Qpims737Rpa51iqFKJ64hfyvt-umGbBxcHh8sUxFRS6jrtKZsvpBU-OeTwFj-rFpbMKMjyir6EXev1LbpNcqxv7DTgw64I_093Knf8LSbG_3X8PNgfWecjRt6M4vm6H-h63VSPUkX1XfQYHp1rQMfv0A8clsAjW0bsM97-xc0PWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=D0jHbERzTi23i3u0zi4yB8kfoebFE6SCXNpFMdzJqJjq9W5iQzCp03aGrTIrH7LCIXsQ1-saHCOtayVyj6nBkPFQMsQpaYVFAeR8OfXjDTDBHwWyxsYW8RzF961kue3Sg_Hfqi1PQlfnpO_AtlubmgUh5i9L4474KMlb73I2777lYp0xJFhPW7G1S4OkrTHn8qUeMsrqLr6it-ZXR-jzNfeE7knRl7h32nTN8aSX2WkvjiCgm0zXc2t43HK5XT4HWGuoCA9t9-jnkWhGmCSvIAOxJi0cl3pPPCBBXKK_qdR82S7o__OBbukLKgON6MokhvMFRyZ-zoAMYqxPqUeV6ztwgi0pnEno4DhX2Ahhy_lZhkJ1_wLMrnK6QlINAW5V5qZG1fpC62IZW2ayJRsTiaJrCbvUqzKm_Y8aMf3Hsu66SJ3A12YGef3O8MNh-_jQX4NytvGhlQbPJ6OA9nMHD7szvcCwwZKXdsjDQRZok4VQc17yZi57mgJlGFvDZaMd0RQigACYeoMCGJ-XhyGcdJINlVmFWC_tITJc9r6cgWxuIBsg2BDZ91IVVtm2o7btfMFG4dZQ42StQWHgkEhoRZ4iVGVaGCm1YWMtpgVzsekZh54Wx5TlMioJSu6ofBCqokT5Bvw2e3ZAdcn0GiqUTxvUNEuoIUklfSk_-teQW1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=D0jHbERzTi23i3u0zi4yB8kfoebFE6SCXNpFMdzJqJjq9W5iQzCp03aGrTIrH7LCIXsQ1-saHCOtayVyj6nBkPFQMsQpaYVFAeR8OfXjDTDBHwWyxsYW8RzF961kue3Sg_Hfqi1PQlfnpO_AtlubmgUh5i9L4474KMlb73I2777lYp0xJFhPW7G1S4OkrTHn8qUeMsrqLr6it-ZXR-jzNfeE7knRl7h32nTN8aSX2WkvjiCgm0zXc2t43HK5XT4HWGuoCA9t9-jnkWhGmCSvIAOxJi0cl3pPPCBBXKK_qdR82S7o__OBbukLKgON6MokhvMFRyZ-zoAMYqxPqUeV6ztwgi0pnEno4DhX2Ahhy_lZhkJ1_wLMrnK6QlINAW5V5qZG1fpC62IZW2ayJRsTiaJrCbvUqzKm_Y8aMf3Hsu66SJ3A12YGef3O8MNh-_jQX4NytvGhlQbPJ6OA9nMHD7szvcCwwZKXdsjDQRZok4VQc17yZi57mgJlGFvDZaMd0RQigACYeoMCGJ-XhyGcdJINlVmFWC_tITJc9r6cgWxuIBsg2BDZ91IVVtm2o7btfMFG4dZQ42StQWHgkEhoRZ4iVGVaGCm1YWMtpgVzsekZh54Wx5TlMioJSu6ofBCqokT5Bvw2e3ZAdcn0GiqUTxvUNEuoIUklfSk_-teQW1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=bCiPnH3cRdrkAzaOCfUU4-UHog_vv2uExTqjOmOJTX5Rd8j3hStfe8D_0eluqkShIGkxzCU5UgP7sQJi4kIQs_aXSumOUBpFhQ5tT7-5j7LQXE0b-NI2JPVcEhmdnpxW2bsa8G57EGYe-rGJ5JrOsVHmAEvAOD-MbdAWvOqGmwji5fLS52yGmaLnWLA00DD2qqd7EUUbyBdEwnzqCuWMwMo-pRXUfYeVrrw64CD3lKVwmkvTtqYec-ginWUi0f-lXK9TptwPjRpdvcJITRljWemsiRxhy5cyjJhBnh5XRGTT6BxsB-X13PquhPaGGgzcharSnU7tmivV4lYmeNFwaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=bCiPnH3cRdrkAzaOCfUU4-UHog_vv2uExTqjOmOJTX5Rd8j3hStfe8D_0eluqkShIGkxzCU5UgP7sQJi4kIQs_aXSumOUBpFhQ5tT7-5j7LQXE0b-NI2JPVcEhmdnpxW2bsa8G57EGYe-rGJ5JrOsVHmAEvAOD-MbdAWvOqGmwji5fLS52yGmaLnWLA00DD2qqd7EUUbyBdEwnzqCuWMwMo-pRXUfYeVrrw64CD3lKVwmkvTtqYec-ginWUi0f-lXK9TptwPjRpdvcJITRljWemsiRxhy5cyjJhBnh5XRGTT6BxsB-X13PquhPaGGgzcharSnU7tmivV4lYmeNFwaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=Sn_c9NvKu-bHHlg4A1JtSt3H_o-Fw8_C-Q3SgvtZ8Sqp62ANRnCq_JWYafvYG2bySrtCXntb8_gTSV3_vvmWxSDUN48l4LemUUovh4Dk6PgPKRONykcfA1J0px6BzUhz-KJTxtaw2a6FGQqDRcDl1oMqVVeVyLL0WCyQCVrsMeEkkrhl6WTXdwdDDuRaGT9ag_1L9esRIyMsybAuFhXSQoudsaWR-6dfejJEE6Y2P759J8XAT0fJjoCs6hCSzGxH8HFV39Od5-i7Gl6sX0EEQhFbMqNm4mINSq9Xld09PZ-8uJpwab2eH8Kk06WBC-F8seVMOxBmdhYHHHCM2m9U3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=Sn_c9NvKu-bHHlg4A1JtSt3H_o-Fw8_C-Q3SgvtZ8Sqp62ANRnCq_JWYafvYG2bySrtCXntb8_gTSV3_vvmWxSDUN48l4LemUUovh4Dk6PgPKRONykcfA1J0px6BzUhz-KJTxtaw2a6FGQqDRcDl1oMqVVeVyLL0WCyQCVrsMeEkkrhl6WTXdwdDDuRaGT9ag_1L9esRIyMsybAuFhXSQoudsaWR-6dfejJEE6Y2P759J8XAT0fJjoCs6hCSzGxH8HFV39Od5-i7Gl6sX0EEQhFbMqNm4mINSq9Xld09PZ-8uJpwab2eH8Kk06WBC-F8seVMOxBmdhYHHHCM2m9U3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hiwenQT3DZrI7c_La5G-w2XeKGHlrrideOvF_gGnNOWRTcHmrc_Tvqe67GCQPlS-LRZ7KKLUkrSYJhUr-2oA5V-GBdF0o8kdjhJu-EZKXgp_6ue0-JBQqDBi_aET7wUQsEfsP5XeVZ2ij6ya_XtCF53s9GqMYl2t0XqKj-OUzg2ryUFGDv0TJDyu2NSEo1fiFio2D13ZdHVYB9W9pZf_U56zz57LN25JFE85QC8YCyHgzbsZ69NHYhpkR_wfbuX9nndKTRGhgVt0InLqb-Je4XwlXgbPp7n9eknmK6Ldhu-hYQr4NYBHFDdCmHq-WzbjB-Ks6mH-4m6V4TwD7zGQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9T1RfVqRv7_t4JZHA21hY5SHPLFHPQr4ru_UndfiSXynpX9e01yo4GwK8BjLzFPoVBqPbtB1a4-GvsyyJUTQTTeSRkwa1dC1iBPyEvUn-VJaPluSVH8LUqhTTLkC_yZLp4wQzA429Mhe7ZKZjB8KFyn9bX0pAkzof9di-ffx9hJ8OKHwS0w-jEt5aiAE4dSp9CsRPLQRqKI8G5WG2_5KCIftONYobiTGZJELelliUYQBjWYrqCzrULSExaXYVdphTBlEaBOc6yp2AyVMMRRGxZ-XegGp6h-LEU8kCV3srOygrGlEJAmDZidraqIQjaBzWheXcRRERvQ-1cd3NC_mQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=WzfPOOpA4GwKORpq4ZkDKvGx5oNLKnkHpYwrUw_dp6MAaaIRtajyVrD4ANBAsuwDC0dtSe4uv_JzQPDHrRmhR06nnmFBmUbIb-XqKl6O3GKtFUkJ7zu7EiE80HJ_O4qjL0aJHLMx9079PNYheLP0Awuahn59nzgsaHy4cVhyg9ClWhkq88mGarftdoZ9TcXp6DT3eWdiNi6o9fsCN6ySR2FgMbN7J6EIMRpLoq_g7L8SUmNdX2aTCjyfqFVj1NcV-lmx7Ov0rSNlxZQQ5jY_6OGmLfmZZ6mGgYdD-JFjTuDtaket1ga62SdRIsY4SnGeEQPasguHG2Bej13FeqS50YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=WzfPOOpA4GwKORpq4ZkDKvGx5oNLKnkHpYwrUw_dp6MAaaIRtajyVrD4ANBAsuwDC0dtSe4uv_JzQPDHrRmhR06nnmFBmUbIb-XqKl6O3GKtFUkJ7zu7EiE80HJ_O4qjL0aJHLMx9079PNYheLP0Awuahn59nzgsaHy4cVhyg9ClWhkq88mGarftdoZ9TcXp6DT3eWdiNi6o9fsCN6ySR2FgMbN7J6EIMRpLoq_g7L8SUmNdX2aTCjyfqFVj1NcV-lmx7Ov0rSNlxZQQ5jY_6OGmLfmZZ6mGgYdD-JFjTuDtaket1ga62SdRIsY4SnGeEQPasguHG2Bej13FeqS50YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8FBWCZElXMXLR1A7YvIjxtg-FEiKBkG3eUSG0VwgGpFPsi2J1Sx7OmVIfpYJ-SETfDOMVpz3nK49rrQGNo_tlhE_iKDRVXzJnAuJW8hej6iEFOisNtFBByZVQkNxau3AXn8AnEEAqZtE-uhqm5K4zbzVzVbetDSbAPoNWMo3weHidkoidnJsUzNymnmgkekOZHIWzprMc6rq4JKrobHpeTBKQhCuAoKteAaVBukZvzUGXdppGljz043ZMhvp51beHvPFOX88g7D6obscnMrXiHu9gScvDmG_GKFw8m_51FOTGgOfRuH4WFPZMhmLomAH6j6M8KQUyxZAVY3PVsj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tU0u2aGYxN8bPeGgFDbd4ntP71Xtq6RGPfx0DzSYdtdtYn29Fe1po5luNqWiPip3jbuP9t7aBkkv4jOxcARf9GTFpu5dQYL3tb60D05R2wkW2Pc9elkQ3rPU7IKb7hBChaK1Yc2pVy7syVOZl-szk3dW-sIupba3USqaryeAkGAmZYWr2gbyO_96Gwq39zwdA7ahcG9CbBgbQ8rLvb-3WI27vJrIx-VVlVqf3k-0lGCOpYu77JESxuuiu67Y_ADh9HU_jmyKeIFYNNsSh-wKBECxMoQ3NI4YrAmLrLwn6VhXKhCWe9eOaqO_9IL5UKbSkqPsZnROIp6_L8bOdOS88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEYTDWTczU7JDPDQp_EbPmsN6ycDqJXrXJToWfNiR5-pU6MTIQuvKXcbrLNAi_q0daeTUzFNFi6Epx4zkqvVkFibELIjwE0Z4ivnNTRkkj7mciAs9WyMcRFYtNTjdbGhXre48uwEjY5CCHZp8PdNXsfVc6rrARcAiFZ7L8kKGZAwYsIp6-udzoRKgQ8Kr8wDcu8U15P6U0MQ5zx0mxTir2ychGXb0IPi7CX2DMLVTysvTa30FOi_cym3LabfvHU9YboNPNpj-rNnGdVv9c3pqJ21fBmcpv2FHYYavROeowGlacn9ym9PXd3HXXaXxdDxUVAHaxRR4VdaNgLZL8WYBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvSuEWYLNU22UslU95fZVwPrUxDWXzB7bT1XKUu0335Wc5ymZ_1JIGkLhSQGqRyCiXVtPGPkT7Q-d3QyyTjWH33xJpSSI9ZHyjYuybiyWm15OdJcFy14EyUAmflHRvmgAlcLz7NlALuD62b-gbDWZRQEovpe-y-FosghhfVM-LNh-GV38EFi4CUHwlPtZVjcUjiy4Ditmt50RUX4cmZvrWCoYD2vFnWfsZK6Lmdam3nzOQUkeK7CaMnxt4o-4-4lJf7ab3AYnnOQYyPxDsJg4DwSD7mRvQq_7J_X70rMMHwXnWROOWuLUuoXQ4jd-YIRIqmdEO3YyVfhXSek3idYcw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=wA3cokcgpFedGBlvohGNf-f8rb6QCsB5M3lIySwVpsY1tf9VY4Fqb86rkBd-83fvnmhHgVu-EzY6VCLXndRSkzbAlqLSleXzzrvkaTh9eLaHPagbqPXXXuj7sHglUgqu1abuCoLZF4crzBStQX57Ew6eD0xyPwXkHXMX-dvW0fmvjNoQPINwZ2z-URgDpv7kQIEofyZaSqeytwgYT6XDFPUJZrhU6mxyWiKBuNZAqc0fo0mZ0lIShdaon-1ac3bXOQE-Rzk409dZXl0KNDO0jscjg-JfnuLq5f9Rx6hf2HVb-e4Qu1rhJzqDGNo1TSWVRl493otDD_kIsQq5OHO4lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=wA3cokcgpFedGBlvohGNf-f8rb6QCsB5M3lIySwVpsY1tf9VY4Fqb86rkBd-83fvnmhHgVu-EzY6VCLXndRSkzbAlqLSleXzzrvkaTh9eLaHPagbqPXXXuj7sHglUgqu1abuCoLZF4crzBStQX57Ew6eD0xyPwXkHXMX-dvW0fmvjNoQPINwZ2z-URgDpv7kQIEofyZaSqeytwgYT6XDFPUJZrhU6mxyWiKBuNZAqc0fo0mZ0lIShdaon-1ac3bXOQE-Rzk409dZXl0KNDO0jscjg-JfnuLq5f9Rx6hf2HVb-e4Qu1rhJzqDGNo1TSWVRl493otDD_kIsQq5OHO4lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=OL3UG15FJwDX4OnUhPOEOotJg6HH1sdHTlb8xXjWXiWhS_8k68D6wWL1B9w2Xn_qUujRWaUjAsSLbEzS-jSI4oOc5-x_pMI9jl6Ovfj-DqtMsHm3BMIIlJukWkEAwkUmS0UbXDU5_Fbqgi-W74e4HglwglQUGUvoXOhb7bF0a04GK2Gz4bC9Hm0x2EDCkaXyhbPM-ehb0GBzdGVYYxhoDbytbvJh7Re7o8AdRYs_U05QqkeqO7sjoS_k7z77Xftv-8eVDXcWzUmFqM_PduyBfbWOgXdW6_Pc5mK8FaosH4PjaTIsIrcaoM7GMWldOzsvoj7Az6lRRPUQQxal7E9DDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=OL3UG15FJwDX4OnUhPOEOotJg6HH1sdHTlb8xXjWXiWhS_8k68D6wWL1B9w2Xn_qUujRWaUjAsSLbEzS-jSI4oOc5-x_pMI9jl6Ovfj-DqtMsHm3BMIIlJukWkEAwkUmS0UbXDU5_Fbqgi-W74e4HglwglQUGUvoXOhb7bF0a04GK2Gz4bC9Hm0x2EDCkaXyhbPM-ehb0GBzdGVYYxhoDbytbvJh7Re7o8AdRYs_U05QqkeqO7sjoS_k7z77Xftv-8eVDXcWzUmFqM_PduyBfbWOgXdW6_Pc5mK8FaosH4PjaTIsIrcaoM7GMWldOzsvoj7Az6lRRPUQQxal7E9DDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRW-LnoB4H1pw7zdcdrrTwJ9cXD5B-V0zWFXNavC5mfMJPavabntz7G3WQPe4kNGViON17OfJifaqga05IVa0Iqvexn7EhIUlNf6220oVoGEsJ0F5BbT7Q9j5CGATBJKQTfYeseVQZSlZoAdFrBDgMKyIF6WgTQ64P9MsBMoIIF4cJJF6mQiCosT-sOV0YLCp96C1zqRrW6CS31oLTqmLkSw2jpQKW1IY1kzzFM9wwFyl4F7ZM3W2VU7U6bYCvPdCpTmekWYfXXNyq3vnQGWY5ZEaBJkJXhjQAl-B325C3E7zKsQd6sEZT1kOXpRfcSKrNX0wJVy_ophoI_cHaAdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Kfu9qj4mSML-TOv6_Q3LX180AWI5ZR2YrGli_bWNZvXa97QbWgmIZR7fkzdv9wUKI7IKYRZTQDFprigtCCiyU5C3W_KGWZwuxWfV-cdVZ-ohxw6n2s87rtvVpWuc0v1spRLP24iYkSB4RHjFLntDWTwEGz179J5Bi0T0cr8rsa6rLJ1mNpl8infRdMr-MIbMxB_KuMB5qNay0HrvvlwuvvcA--Kfg1Azh94jspgu7y1f-vG-AnNPHZNkxcSygaZY6HjIVHsKLj3NXGIIb45apuo9iUyV6BsgGqe9EuJqmxX1jJhQ-vgsIBka5ryNInkZaDsj-pyTKNB2nqyreDQDDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Kfu9qj4mSML-TOv6_Q3LX180AWI5ZR2YrGli_bWNZvXa97QbWgmIZR7fkzdv9wUKI7IKYRZTQDFprigtCCiyU5C3W_KGWZwuxWfV-cdVZ-ohxw6n2s87rtvVpWuc0v1spRLP24iYkSB4RHjFLntDWTwEGz179J5Bi0T0cr8rsa6rLJ1mNpl8infRdMr-MIbMxB_KuMB5qNay0HrvvlwuvvcA--Kfg1Azh94jspgu7y1f-vG-AnNPHZNkxcSygaZY6HjIVHsKLj3NXGIIb45apuo9iUyV6BsgGqe9EuJqmxX1jJhQ-vgsIBka5ryNInkZaDsj-pyTKNB2nqyreDQDDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=VE3yrjWVfPXMV3W45I2SOFUtP1Q2q1gQokoZzd-oe5oFANDjffUfd_VtXe27JPQa8LSF10Ej48ehFIeWq5507-gKCLbjxkfKk4-uMjf-S71bqlluz_nE7yHqfBFy9W6QqHrA-f3nVQlM8mSCl5wGGKdN1qLtWXeCZJvlVnvYGbYvDJSzkYYVbNfavx1e_ohJn8HWo35tycRCdOMesAYsjwyzTdA9bk1KN0LyTFpqqcy-Z7Szculq9eTNJd8s1LWLY1U-YpXxoMwTfpZ0BMjTc0oRKyLVUvIXexOht9XWBtKU4idb6C-x3d47jMYVM8SNY_GMu0uGFDF9LPCSYZN9Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=VE3yrjWVfPXMV3W45I2SOFUtP1Q2q1gQokoZzd-oe5oFANDjffUfd_VtXe27JPQa8LSF10Ej48ehFIeWq5507-gKCLbjxkfKk4-uMjf-S71bqlluz_nE7yHqfBFy9W6QqHrA-f3nVQlM8mSCl5wGGKdN1qLtWXeCZJvlVnvYGbYvDJSzkYYVbNfavx1e_ohJn8HWo35tycRCdOMesAYsjwyzTdA9bk1KN0LyTFpqqcy-Z7Szculq9eTNJd8s1LWLY1U-YpXxoMwTfpZ0BMjTc0oRKyLVUvIXexOht9XWBtKU4idb6C-x3d47jMYVM8SNY_GMu0uGFDF9LPCSYZN9Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=sZ4PXSmUIjV9THDZi1ejXX8Mol-Kxe_Z9wYqoMrqp8Pn63ZcrCuhBF2rZKz8lre0BulrDIfJh30siFTaperitC7S6f75ZB6luCfius0kVPqzN844ObnOWiAPxGlDSRVGRc_KRYpMW_YYgaRQgI3jn9n4pG5zluYN2DkoRksAsESlqK8vbGMSX40dOCuwzBjWDDI-8aig4ANoAlBNuhuAR3tufQkv8CItgr87DYzeoKJgnkkbBjsDg8tHSN4Rigo_Lhwn-fvkqBOgHz9HDd105TNPQvpc_Lj5YNracupbRHddGone-a1nbgLplGvbst1O1qVQvahEieZyPI2TbJt3yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=sZ4PXSmUIjV9THDZi1ejXX8Mol-Kxe_Z9wYqoMrqp8Pn63ZcrCuhBF2rZKz8lre0BulrDIfJh30siFTaperitC7S6f75ZB6luCfius0kVPqzN844ObnOWiAPxGlDSRVGRc_KRYpMW_YYgaRQgI3jn9n4pG5zluYN2DkoRksAsESlqK8vbGMSX40dOCuwzBjWDDI-8aig4ANoAlBNuhuAR3tufQkv8CItgr87DYzeoKJgnkkbBjsDg8tHSN4Rigo_Lhwn-fvkqBOgHz9HDd105TNPQvpc_Lj5YNracupbRHddGone-a1nbgLplGvbst1O1qVQvahEieZyPI2TbJt3yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=ENS5nmdoNlSWMSmfTpmvzLb3KBDOVRM6K3EvpqvzzGWxvutLv2o-b7y2YHIoBmRCRGN2s42dv_g7kK3A8pv7H_ovsmSgVx4vM-ff91Z3ImQTjxkGHZwVyeQxcC5frlGq3M-shB_FYRu-kghxjJPewczz_VOJ3Ra2m7wDzwkDGnHanmpHPHaNCbRM_LwFTRMHV3zuABCk3qR-W2cvAUhFLZo5hHarSiXEOA9o8AINn0V-5UE8JrHf_9sMfPyXfWoyRoTHK55UErZUWd9j1L06wI6PgBsyrYR7_PdQ0poDa1N6ldNgpNCg_P8fovAJuS_UMCfiVIVUX3sIlTZmCI3vjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=ENS5nmdoNlSWMSmfTpmvzLb3KBDOVRM6K3EvpqvzzGWxvutLv2o-b7y2YHIoBmRCRGN2s42dv_g7kK3A8pv7H_ovsmSgVx4vM-ff91Z3ImQTjxkGHZwVyeQxcC5frlGq3M-shB_FYRu-kghxjJPewczz_VOJ3Ra2m7wDzwkDGnHanmpHPHaNCbRM_LwFTRMHV3zuABCk3qR-W2cvAUhFLZo5hHarSiXEOA9o8AINn0V-5UE8JrHf_9sMfPyXfWoyRoTHK55UErZUWd9j1L06wI6PgBsyrYR7_PdQ0poDa1N6ldNgpNCg_P8fovAJuS_UMCfiVIVUX3sIlTZmCI3vjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuX9ec8r0RPnrrRducDqa7bMfnT_roClxDxz5TgVUaIF1exHfqbpXHTjxh49O9IiVYUgmZ2UKdl5ozEeDHilL05eMmY__WJO4DMl1ND_lyMh001DrAlrvBvoWzGTP43zc0EUoukgBvTuHQlUhY9v6HBzKJwxpfSp4ym9sErWdZUZkxUKJ2aTlXz8inWFUVhYnSTpR8TR2s4aTtVhJTBHOdnPTl5LJJzPjicRS-WNcqO4hEIC2fxTjm-6okXy8LIfLWlqIJ2CJwoqzshLRydgJUvQbW7IzR618FykBR3y4BiWAHcIEOzUlGO9UwtO1I2apkO_ZVYIh-UtZcFWLD3BAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aArwz1ho8KLI5_iiqXS-XgwFTi_IOGdbjsJx9tALPnbmwDAQ2UGQ-iw-hTDru2Ip1zwdD744lI-2khR9RZIrDsdTrd9PA3y92j5hrvycronHKrrRAl1ehuI_nv6Lak14OONksaj6obWxZAUezp_Uy9AmQb3IOKcSDjTUn_B9FWQkXdvDNXFtVo-sMoXBWpT4IpQMK_eqN6_ojWAPhDCUKN15VedHL3Xwcgax49XAOaVbkAmPJqfIqwRZDlbSJAsn2AWN87x0A8kz2EXbVyc9bFXXSAcTA9DUIBVVrPNk-cW-anvZRYIIcg6Jz27GrVDkd4B75b11S8LC9kLViL-B4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=eXWumjAGtujsp8e0K0wPrMHaaq6Mq3k73Vh0JTRvQA6Bft_1fFHUTXGqv-e7gve4ZL3EBy9AC1KtQM8bAv3z4YvaQyMetcTQfAO85D8cccIsSmmRsh0aCMA_VfpQt0EA-7XhPgmBQIdOlHBOGMSKT9etJmEgdsnXsPLkPXYabzrsdSTUuaQfwLb5DQfA1q-LckFGajaDd4hLJzhrymDzHbaw0qTgCihEMkr9eqbDHvmRKR_IqFbCd161n_bg4tpLecBtlLI28m6JUcuyf5h8FvkQuhbvbvjFv802NCri7JRj6kOV5MvU5spLoYOZL4Zxuud6MlImfUk5esxKg1M0Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=eXWumjAGtujsp8e0K0wPrMHaaq6Mq3k73Vh0JTRvQA6Bft_1fFHUTXGqv-e7gve4ZL3EBy9AC1KtQM8bAv3z4YvaQyMetcTQfAO85D8cccIsSmmRsh0aCMA_VfpQt0EA-7XhPgmBQIdOlHBOGMSKT9etJmEgdsnXsPLkPXYabzrsdSTUuaQfwLb5DQfA1q-LckFGajaDd4hLJzhrymDzHbaw0qTgCihEMkr9eqbDHvmRKR_IqFbCd161n_bg4tpLecBtlLI28m6JUcuyf5h8FvkQuhbvbvjFv802NCri7JRj6kOV5MvU5spLoYOZL4Zxuud6MlImfUk5esxKg1M0Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9WIcbdZRhxztS_eZCeqcd_RqEeEJ8h1a2NqOIwoY1aOYWKfuXOp2uEvLKdeuimEhXu0R9xrcNw5fRDyoY5y_JTAWLhWjw58UpCNf6BIMb760MoxV9l6mvkeXe9eqLQ-deCmdEy7Y4GCx1GRz_dpsZ0bfWgXyl_cID4tXWQSgGShviSPWRd1DRUJIYcaSianGMFs6dxqBHSzALitYwAUmgW8pGDt9kyiJvt4fJz4oerGlW4YQ99OTrHgggOXIT_qu1hhqbEDP2tsfrkThIbcVtRFb31BeVte0N4ge7u7v0lTV3g7znYgy8h-K7RqhZmy6JpfnFDEcGHt4VhuJfEF7OhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9WIcbdZRhxztS_eZCeqcd_RqEeEJ8h1a2NqOIwoY1aOYWKfuXOp2uEvLKdeuimEhXu0R9xrcNw5fRDyoY5y_JTAWLhWjw58UpCNf6BIMb760MoxV9l6mvkeXe9eqLQ-deCmdEy7Y4GCx1GRz_dpsZ0bfWgXyl_cID4tXWQSgGShviSPWRd1DRUJIYcaSianGMFs6dxqBHSzALitYwAUmgW8pGDt9kyiJvt4fJz4oerGlW4YQ99OTrHgggOXIT_qu1hhqbEDP2tsfrkThIbcVtRFb31BeVte0N4ge7u7v0lTV3g7znYgy8h-K7RqhZmy6JpfnFDEcGHt4VhuJfEF7OhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=hnx_IqEfrVaHcEDRYkwLT3xluUAL9rbBG9b1zqPjUDDVQ4P2kCgwpH5Qku6mDb0uAUfFINYGBcre_zhdIfZXDkwz2u9vs_8vZWjPpn2yNCX3StUkDjp277PG_Kgw4bQILFsCXYIsXbW8q5pX_yZSwYcLDVlz3v4-lvHsSBLYzQ8xmRcTYUk4DdHDB9_6q3-WmRJ4nUy-KXSeV-u451JPP-CWEWf2xlzktlch5SCiHcPXtCsLvn7lfYUyit1mQWHPD9AeW17NCLJbM6KVPZ0821pWlO_851vVE_plly153CAnWrqRv3AlvHIEn65BvJdSbtysqn0cm1imnr73qV1j9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=hnx_IqEfrVaHcEDRYkwLT3xluUAL9rbBG9b1zqPjUDDVQ4P2kCgwpH5Qku6mDb0uAUfFINYGBcre_zhdIfZXDkwz2u9vs_8vZWjPpn2yNCX3StUkDjp277PG_Kgw4bQILFsCXYIsXbW8q5pX_yZSwYcLDVlz3v4-lvHsSBLYzQ8xmRcTYUk4DdHDB9_6q3-WmRJ4nUy-KXSeV-u451JPP-CWEWf2xlzktlch5SCiHcPXtCsLvn7lfYUyit1mQWHPD9AeW17NCLJbM6KVPZ0821pWlO_851vVE_plly153CAnWrqRv3AlvHIEn65BvJdSbtysqn0cm1imnr73qV1j9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjq2qOfCy8_tvLVDnQQEubFWYpDFQMCnoaBtGkWg0kz3SdYj9iPfXavksIMyHQM_jdM21Pg2DmuRXONAdda4cNJRqwVw_qL-VT8iqsqGnTXNM6_w75gcKT0F3p9L3bz794t4cmZqN72b9p1cos2tZjcAq-FIbQpv1ijbyMXf9mQAQ5wdjTeOI7aaNAh-YiNhvcvZj0aOIkyekoTVhMas9B-XKIbpIuzR906_VwbUQtXaN85S8N8huJ9GV-sji7JREvCqOVopIfx2Ez5qHesCzeGzlxr9Qms0Bux7Dvigzr1aYuyb4_W2Rzugx6knmteOOakYOtajb1dkdmve1bycuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=PN3GHI-tbpU-Eq7ZHYGZL7W6zBC3UMExXw49OVfUv2rOer94a3dje2LvP3xW1nkrk1cxyyo48FdBqBAaB4duoMOYj_jPsDnADgcRvRZXLh3-nThukDgDt5YyAshQ1Qdkks1U8HVHwzbTD3Oldr4WTPR9ZJSq-QP--7N2boUv0Z9dlweSg2MYueYd5WBJgpgpCDU-d2Fhk6FIaOWokYD60FJJzaMJagqQeDa9nwuE-8P6j1skH29ZlreMCpEq35YlxKFXLQ5vvEIQLyQNlZAaL_EixHmwD6iOOK0lIgw5Lxap5rWy8eXuBFwa3YDHprkhITbk-vkbAe0uBY71eJIXtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=PN3GHI-tbpU-Eq7ZHYGZL7W6zBC3UMExXw49OVfUv2rOer94a3dje2LvP3xW1nkrk1cxyyo48FdBqBAaB4duoMOYj_jPsDnADgcRvRZXLh3-nThukDgDt5YyAshQ1Qdkks1U8HVHwzbTD3Oldr4WTPR9ZJSq-QP--7N2boUv0Z9dlweSg2MYueYd5WBJgpgpCDU-d2Fhk6FIaOWokYD60FJJzaMJagqQeDa9nwuE-8P6j1skH29ZlreMCpEq35YlxKFXLQ5vvEIQLyQNlZAaL_EixHmwD6iOOK0lIgw5Lxap5rWy8eXuBFwa3YDHprkhITbk-vkbAe0uBY71eJIXtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=jmjmXyTzSkcscHCLsMb0wKpaZmr7ShuHoK-i2IjScEaIv-bSsw74oWZ5_pvRI1LThAIqN5uJjnNFGQS7HvdW3bAObSvAhphD0GgHsVQUE-kCXcAv_as-ShbCbiuQYwqeRG5VmadpXhkTYR45yOJZULeIFhjwYR3szYuPL4lx4W_0NM2y6QJ_2v1eJvl3opakXMB_ksT95elzwL4sjM33sX-cwaJ6gysIlfjYTcQLo7XhM-viNqnqoyh5K7YSbfn-SFW7qCL3Wu7WZN75P4_FXgXNNs8O9dA1Ea07RJpPFJAIr-N4xbud96TW6BINimBKwptppmHxgRM_xIp9_SXTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=jmjmXyTzSkcscHCLsMb0wKpaZmr7ShuHoK-i2IjScEaIv-bSsw74oWZ5_pvRI1LThAIqN5uJjnNFGQS7HvdW3bAObSvAhphD0GgHsVQUE-kCXcAv_as-ShbCbiuQYwqeRG5VmadpXhkTYR45yOJZULeIFhjwYR3szYuPL4lx4W_0NM2y6QJ_2v1eJvl3opakXMB_ksT95elzwL4sjM33sX-cwaJ6gysIlfjYTcQLo7XhM-viNqnqoyh5K7YSbfn-SFW7qCL3Wu7WZN75P4_FXgXNNs8O9dA1Ea07RJpPFJAIr-N4xbud96TW6BINimBKwptppmHxgRM_xIp9_SXTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=bQyryct-lORE4zSmWSH_34fYPGWd331OoAyUSjNBOHXSmli2sLA2o9VP4VCeCsluctjz89bRQ44tTqRy_WPDt_m_wRdIUnp56lAxaMl8ETTX_kafd_J8Uo15pjtvqeYi8pprunV29Xk6fzTl-WqfMB2k3ij_bnSmP60_LvmmFOs1S5KqHFCGiieUvzZUCU37PAOy5y5RCpTV3sBAwSTXycDPbr2ErXraLfLxZnBOC04ljIOhax_uaxyxtkp2tSaZJC1X3abh9FXZKQTH4tLmxS9euhiGtsK793HbWXfCSgEQWynif3HfSv1g3Iqlsh5Abb5e6UNwegS0ETYRo8nITA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=bQyryct-lORE4zSmWSH_34fYPGWd331OoAyUSjNBOHXSmli2sLA2o9VP4VCeCsluctjz89bRQ44tTqRy_WPDt_m_wRdIUnp56lAxaMl8ETTX_kafd_J8Uo15pjtvqeYi8pprunV29Xk6fzTl-WqfMB2k3ij_bnSmP60_LvmmFOs1S5KqHFCGiieUvzZUCU37PAOy5y5RCpTV3sBAwSTXycDPbr2ErXraLfLxZnBOC04ljIOhax_uaxyxtkp2tSaZJC1X3abh9FXZKQTH4tLmxS9euhiGtsK793HbWXfCSgEQWynif3HfSv1g3Iqlsh5Abb5e6UNwegS0ETYRo8nITA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=DBfsm_9sNzSj-ag3OgLTnuKWqKDDwqYWpWfA1ekGcqC3iD48bwFiFgDU6GMNMm6JHGtZoAoJvJGOejwV21gkHzWgaFhgY5u65H0r0XVKh8Y8Y_t3pJF6z-Ple-1UUjN8J4s7zbQM5yX5dgxiZ763ZKCpICfUz4wp4tkrJvjeBFydVJynyXurM5Ca9-kGjgeO_Aj5kjun8UpIebhpJcrbf7N5phQsKEOwCJYctQHIwG8AGMBjcdIpirG3B6NEGPMniLhXFE-Ye9sg8qhpPJOmET4YMgDTiWHJlLUELYMRThK1_IBidFeK1Tl_0LThgpBb-V6NCL465UBCVVAKcvz8BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=DBfsm_9sNzSj-ag3OgLTnuKWqKDDwqYWpWfA1ekGcqC3iD48bwFiFgDU6GMNMm6JHGtZoAoJvJGOejwV21gkHzWgaFhgY5u65H0r0XVKh8Y8Y_t3pJF6z-Ple-1UUjN8J4s7zbQM5yX5dgxiZ763ZKCpICfUz4wp4tkrJvjeBFydVJynyXurM5Ca9-kGjgeO_Aj5kjun8UpIebhpJcrbf7N5phQsKEOwCJYctQHIwG8AGMBjcdIpirG3B6NEGPMniLhXFE-Ye9sg8qhpPJOmET4YMgDTiWHJlLUELYMRThK1_IBidFeK1Tl_0LThgpBb-V6NCL465UBCVVAKcvz8BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXu3CfWcDVS0GZFns2D93jSIF27wAnoO8JN-QPiVNSYEneuaz_AE1wL_UjPuk-QuwaYSof_4uXUX5HnIfglhv2CfU-hkz-uPrEreHEFcGH1DDaufG-OkebTodAz5tfOpUQ7xNkcrRCBsicjTmnuhf_MmNBome_JVEn_8emAI-29tnYDlxXwbOXzCQfaktNDA9lQT7U-ps75jIvKlCRa1dxTWvKJ63Gh1U_s5g7SwkfuZKQYga7GxBb-DRGcRIfE5kgHaajRMaDODyQaqTXvH0MhC4rap4ezPMx4Ccaf1aHT7Nw0zMLarP5t_iyrwZ-Thz6WhKuGCJJsR0Je6DyPjzA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=kK8h99St3XRoIcwdcqGHSrPcth8yXyBd892GaWpk4b5PKSymBGidppmTID2LNOult0OYocLT4iEl1-HVE9qYHhZk9nswj6XmHf3D7nxElo-y4lgGptr1R4-5RXNjT9Gy_BtAaitDVS1F0UYVXnUPGEJm7t-mCuiWqCHRPeVDDB4dNHL9dgX7EWDjs9TO7oxOW8DCcfkeil4IFffSR78M8hy1y-9E2H_O-HivGcddaxQIvIRPlNJY8zY3HaxWpbRcYTYFkJ4JfpN97m25ba-Rysn2x0o2rUcu_SULC-zDsBG4YZaQIQ9pScaescvsvJRivtqmp6AyO77an4WdTtpCBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=kK8h99St3XRoIcwdcqGHSrPcth8yXyBd892GaWpk4b5PKSymBGidppmTID2LNOult0OYocLT4iEl1-HVE9qYHhZk9nswj6XmHf3D7nxElo-y4lgGptr1R4-5RXNjT9Gy_BtAaitDVS1F0UYVXnUPGEJm7t-mCuiWqCHRPeVDDB4dNHL9dgX7EWDjs9TO7oxOW8DCcfkeil4IFffSR78M8hy1y-9E2H_O-HivGcddaxQIvIRPlNJY8zY3HaxWpbRcYTYFkJ4JfpN97m25ba-Rysn2x0o2rUcu_SULC-zDsBG4YZaQIQ9pScaescvsvJRivtqmp6AyO77an4WdTtpCBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ZN1VB1-CBJcDp_HbcwVIEouSvZis9ysFS_PA55v8FbPPiNs_Bshx1Jse1TmlUvarx5bD69PdMYm7ANUg-mK3yMUX6zxeP59yQ-g7LPTGvim6mi5tzNOhyeC4WN_su1Z1GV1guXugs1q9m9INNXc93L0tHKkwkG6WVVGmSeedfVpReWeGEg3SR7lBGSWkX5ZZZsjLM9NTgiNxGmJztslOvyH1p_7XZmf6YdWu8BG5b9xYthJ78IR56GgyrVXVv_RNHdwYEKx6S8OmrPTsaGeh6pAlFu44EdD1D2dDhejLPpamGTdhcxD2sTEzQj8XQ2F5Bv60gqn8P1Cyertd4nK--w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ZN1VB1-CBJcDp_HbcwVIEouSvZis9ysFS_PA55v8FbPPiNs_Bshx1Jse1TmlUvarx5bD69PdMYm7ANUg-mK3yMUX6zxeP59yQ-g7LPTGvim6mi5tzNOhyeC4WN_su1Z1GV1guXugs1q9m9INNXc93L0tHKkwkG6WVVGmSeedfVpReWeGEg3SR7lBGSWkX5ZZZsjLM9NTgiNxGmJztslOvyH1p_7XZmf6YdWu8BG5b9xYthJ78IR56GgyrVXVv_RNHdwYEKx6S8OmrPTsaGeh6pAlFu44EdD1D2dDhejLPpamGTdhcxD2sTEzQj8XQ2F5Bv60gqn8P1Cyertd4nK--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSEHGkYaoMu6zqwp-GBRwR7SRDAI-Ygp6egtrk3oOWTgOJJMxjw6nC9OvsL2NO06oW0D_LgIhHKpaYpP4X7OgTICZNXaLL4w9c2Vt3FzKgcJ7ARKWfahlIQ6hDcWMLZnFy0URrzHeNZx09k9L2lQnniY34N33QXxk6WcvGNEpO52FkvbLWsc5PZrCywynXkcVuC5IFu9sq6MfrIuTmu0-SlqrShBeWZzt0SilG01rU4x6-5bmbZ5E-bx7YoJW_uBb0H8R54LW6YyWe3UeYk9NrisKAWKl-CmZpfkaRdtnLNRQHtSCYGikmUQ93TzB4pX6cE9zyFLb7ijNEh5ZHi85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=FBSKqe-N71kXwMWZkxPc_Lbip2Fs1uOxpX1WNNwPOqDzNPqgTvqoPWKpCi16od-M9zcNbe2UrhORjrvuJeKJAZ2GDMcgqvxFhJAe3qxN2Sm1j5AhKU7IYqL5Fiv2FKnSThD-7Lm471Bxf-qvUGpecWHTYwpsST7iZD2KznvUrWGBRv3gsFbnwLQ3tTRPgoF35_CKyHmMlQ5snX_Sog7Vhug62vRaTtKSkAP-Q-Im_m5BZMNulRf0Ej_qFxHL5h7XVtNsLyzzJxSMfxkWoi-xZWz1Dhid1h0nUDkoO2XD1DHasDkBGwJxDpFnUN_cu6M6aE-7WtaMv90j2eBq-PsMgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=FBSKqe-N71kXwMWZkxPc_Lbip2Fs1uOxpX1WNNwPOqDzNPqgTvqoPWKpCi16od-M9zcNbe2UrhORjrvuJeKJAZ2GDMcgqvxFhJAe3qxN2Sm1j5AhKU7IYqL5Fiv2FKnSThD-7Lm471Bxf-qvUGpecWHTYwpsST7iZD2KznvUrWGBRv3gsFbnwLQ3tTRPgoF35_CKyHmMlQ5snX_Sog7Vhug62vRaTtKSkAP-Q-Im_m5BZMNulRf0Ej_qFxHL5h7XVtNsLyzzJxSMfxkWoi-xZWz1Dhid1h0nUDkoO2XD1DHasDkBGwJxDpFnUN_cu6M6aE-7WtaMv90j2eBq-PsMgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Ul4MC-u4FdZPNJIKUJ1HIDcev8E1SujKyQ193kFpWqg83y1rM77qPgsl4zUK2HgXo211GsCoFjMPZHPs3mAf5xmBTHMBybLvggAXjb7e6IMtRZc2NfWLXD2sxVsJXm6j0ziUEyxQbjhUrveE1mBTW2umNDCzMWx5r3RGz-m6bFsmnAvYVcw4cb_deMAwEPukB4n8NN4kp21BVeaMkgaY20MTXguasq61q8sGhYXxxYb-_kZ4VES14ewTSsVx_xquqmY2ODzdP82rQ_jH5nMr1HQF7asQv8K5PH15ZKiAyJ8Ks21rUxuC0rdONYJLJByXiCNcvu2724bDyJurDVk7Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Ul4MC-u4FdZPNJIKUJ1HIDcev8E1SujKyQ193kFpWqg83y1rM77qPgsl4zUK2HgXo211GsCoFjMPZHPs3mAf5xmBTHMBybLvggAXjb7e6IMtRZc2NfWLXD2sxVsJXm6j0ziUEyxQbjhUrveE1mBTW2umNDCzMWx5r3RGz-m6bFsmnAvYVcw4cb_deMAwEPukB4n8NN4kp21BVeaMkgaY20MTXguasq61q8sGhYXxxYb-_kZ4VES14ewTSsVx_xquqmY2ODzdP82rQ_jH5nMr1HQF7asQv8K5PH15ZKiAyJ8Ks21rUxuC0rdONYJLJByXiCNcvu2724bDyJurDVk7Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=A9qVbuG2R5R7ruSc2_wlDfmaZSd1pxjpz3AmvK8pNy19lVCunbFCnFowImx0kKVt82v_GYN2VK5oyqdVJhjoxafupU63-yerGi_xuFhI4DYhTxsEaziiA1EmUOqrTvlUi7n_mofUE5l2sHRhmxtwSk62ERrkll9gDlUcbRvyKXV1WNXijwhrBeYWcBoRQjIRhy_Ig4hm-VB0VYwmYpxmrUO4SjLPB6w_bHjZc2zXTFFn_ZWf7MeAs37XF4ORn7GbdW1NTRd5Ij9pCN1mzlevOgZKwiXNU9_13lb72KIyFFt-IuCSTCYbdHKXNjcAof5stgMEnlzd0iQIqdi0jpTfBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=A9qVbuG2R5R7ruSc2_wlDfmaZSd1pxjpz3AmvK8pNy19lVCunbFCnFowImx0kKVt82v_GYN2VK5oyqdVJhjoxafupU63-yerGi_xuFhI4DYhTxsEaziiA1EmUOqrTvlUi7n_mofUE5l2sHRhmxtwSk62ERrkll9gDlUcbRvyKXV1WNXijwhrBeYWcBoRQjIRhy_Ig4hm-VB0VYwmYpxmrUO4SjLPB6w_bHjZc2zXTFFn_ZWf7MeAs37XF4ORn7GbdW1NTRd5Ij9pCN1mzlevOgZKwiXNU9_13lb72KIyFFt-IuCSTCYbdHKXNjcAof5stgMEnlzd0iQIqdi0jpTfBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgmXlm6D505UEbE5mzBujs0eTIWgkYIuqMwxfSvd8dgOt0WzYTNTXa-kpCkU3xAlEdSnqTgGtgfLLnzj2qNupKv8hK7Ibe1TBuOay7oNISAU7Ms1fFxpj-Xre-cBW9z9qaoawc2IU6zclRcgHF6rLpJBt6UnQKg7DOdvkV41X9fO9Iy3P0dRW65XVQmK3_55r5dDv8ZMM04At7MKbErvcpKPB6dwGjm-Y_N0I5yt0iMoRy4EQE1f6N-UfN-bEsqUJSH5HExzMkOmtmZ1srvtUGDbNj_-EinpGWFaimFcV2TposceLoFFlJRFqvcu4IXrNs2TYWPpJJPCqYWCa1FYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLsboIrAjCCnYa3CBbALe1vd952BDlbu0rZ2YWQrIXSUkpkGSB3PqnngYKZUpMrhVCTKr5QcoWnG5xFb1-zS2NwxOUVIkqEsJdCk6Ko31Od53tMf80AsTvUFldEhqKWqnI788QdPEfjkv2-2O6iKXGDdFugcSWG2-KpPHsEmVhCWgBctSlXqtUcL3TJus8jMlxivtxcC6l0_JVV07EzpooaCAn0TUVTnhFkHkboAZFx6BLnLIpIYEyz5aCExrzxGm3hgR5omn_1VgCNUvYlwAAWL6BOexqDwTyyObnYdhvnB5s55LVGiMSGTXnmp9q5i16m1OHFDHZZfza7NKOdUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZuFr3tAqNLLRp84stSzGMF56Y17KbmtL63NlQBEgxETkRf1DV54yC9m4gh1yFtKhQFqDoR87DhESio346HRi7BsWeKDCM4_IttsqUwBp3JywPt53Z1W4qNVDxi4iWUkiSc5ks2g48shcYIXTB4UyEm2fMcos8_krhP-YCfEZ_4hCQCAXh-hbK5DexJ01Lcq1teWaey0UNHVsKOrh378HhTtz_UByfLTbUwsvEO60rYFWcHE6fvGBvMm_avVEPIpmLTgI3cmnOz_J4pJAM1DtCIQJqY0q0EYpxeimQbjpR532nc9XhXtzg1Up_tqleg7ObR98ol6q9GVQZV5g4Bchg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=bNCTeR6SmK4T5g5-7wGxE2lFWbIXxe5AH8c2jdbJMa_NiLbrMrLSP-BzKgz7_KXIa-nOpHXxhEr4Ap5V8eIX3jL2-0qjrTv8kOm2FKdmXm-A3uWWkgv_jrHXn6rBLDNhg_UppkXiifvdqd-q-EAlme6_Ab_OeY_7-K5mHg1qrCmW6tKHbrEh4nRCkEC_kIUq_9g0cpl8bhNIJZaZk4c2Ei4fv9pFwp9udm3BGg2VAZXOFKCbbY7g_U7KufC5BVoQUdaPqM-VqrliHQ9-8x4bfjf13iEtUAt48iOLg40c5U2EdDhqSvga1PNejlGQ7DOIuspGvQa-8NKfP6qPgioxyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=bNCTeR6SmK4T5g5-7wGxE2lFWbIXxe5AH8c2jdbJMa_NiLbrMrLSP-BzKgz7_KXIa-nOpHXxhEr4Ap5V8eIX3jL2-0qjrTv8kOm2FKdmXm-A3uWWkgv_jrHXn6rBLDNhg_UppkXiifvdqd-q-EAlme6_Ab_OeY_7-K5mHg1qrCmW6tKHbrEh4nRCkEC_kIUq_9g0cpl8bhNIJZaZk4c2Ei4fv9pFwp9udm3BGg2VAZXOFKCbbY7g_U7KufC5BVoQUdaPqM-VqrliHQ9-8x4bfjf13iEtUAt48iOLg40c5U2EdDhqSvga1PNejlGQ7DOIuspGvQa-8NKfP6qPgioxyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaafAppqo3cQd34RXNJvfyOooFy8kB9mbMU85jGZjQMyot2qRomB50M7vhKdF0q18AQnZ7hfVp6JYNXRlKhA8MSOkNCzATIHiZY_zKdb6n5sb9S3-827nfn1u0dHbg5xqDryNXsPeSDNewme38IX0anQwbSFXTGQEkdCnDRbTrSJ5aChDPT096UjT5zYlNnDi5k6BlzlVJYvYatB2bJDVS-7RNlk29efOiH-xfw3g-JPZGX4jQbQff3u8kNR2-RuEC0vZ7_0vP9xZgIIaRuM3LUples1epJUbyFDvtxZ2H2tjhIwW9Wcb9K-z4eULxlwr4FCHC3yj3tDMaaWpl1Bm7UM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaafAppqo3cQd34RXNJvfyOooFy8kB9mbMU85jGZjQMyot2qRomB50M7vhKdF0q18AQnZ7hfVp6JYNXRlKhA8MSOkNCzATIHiZY_zKdb6n5sb9S3-827nfn1u0dHbg5xqDryNXsPeSDNewme38IX0anQwbSFXTGQEkdCnDRbTrSJ5aChDPT096UjT5zYlNnDi5k6BlzlVJYvYatB2bJDVS-7RNlk29efOiH-xfw3g-JPZGX4jQbQff3u8kNR2-RuEC0vZ7_0vP9xZgIIaRuM3LUples1epJUbyFDvtxZ2H2tjhIwW9Wcb9K-z4eULxlwr4FCHC3yj3tDMaaWpl1Bm7UM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=nqVG9Hhu-3F_OdoYbwSO_lrtMUTAnUIOMQLuLkySzaeDdGNp6MNaDyqHWATgnwNhd2c5s0WRiOtOVR4ythYleuN-3h9fkKG_pVV2-zgajg3smM2IHagCv9W-wa84wN5XNN6orRHxacxCNltMTKHolBPSdT7yq5UBaOOUTfX59-gEPagOMdHxYn1CU3ZSFFAN4LYesN4vX0vVezia4-9JHaiEE7cebpMZgntcIYU8svvEc-8G4z3E1iIHQh3okCjBqUMMYW7HGdFecZB4EAu3ouD5x70WBcMrGRXFPtiWcpPlC3Ow5Ih9qZIycmViYUZBqQ0SMuzjjS5aP7pD0Ajjcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=nqVG9Hhu-3F_OdoYbwSO_lrtMUTAnUIOMQLuLkySzaeDdGNp6MNaDyqHWATgnwNhd2c5s0WRiOtOVR4ythYleuN-3h9fkKG_pVV2-zgajg3smM2IHagCv9W-wa84wN5XNN6orRHxacxCNltMTKHolBPSdT7yq5UBaOOUTfX59-gEPagOMdHxYn1CU3ZSFFAN4LYesN4vX0vVezia4-9JHaiEE7cebpMZgntcIYU8svvEc-8G4z3E1iIHQh3okCjBqUMMYW7HGdFecZB4EAu3ouD5x70WBcMrGRXFPtiWcpPlC3Ow5Ih9qZIycmViYUZBqQ0SMuzjjS5aP7pD0Ajjcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy8iLcb5crTzpDtiJcw7G2sgvBsx_OOYpTyeVvOZgJtTW5wzLkdVPSbIb7h13vStl-lxb7OMl86W5sWHRCmYNV-mKhQ4hsTWfCt6jpWNSmdCkyL8wVS_a1k0I0Y7gTLHwANAZ-KA5oSdpkVKYta4fkxN0iWB5Fvzo9jNwbdybgUnYRxcDQoSB9CvrjNg4vgpcz1MT5w5SI4b_0Wzz2WP7pslbQtx79qvXZEIzj2Ua0Q97csgRvjTY5eCPNyrIo5qp_35l9lksnEuXXC-oYlXAtNb4JPdd5meXUGvgiii8y47LXrVQdzm8g34rbW4CT7mTKewzzBFXly2npL6RX-jQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHHK1ivRU8b2duwlG_37ZteIONL3ZMm-S4L6lvnS5cBs6AVFZHumHUBfkZTXdoDbT-2aNnPDxVpBAGdUa-wQSuWRiWJzmi2ZBGLBVNGfHIDOzZmeDX2s-W4SrEzjAEZE8zELZZDGJhvObXvUaS6CVp4ypY9szSurGYPdLRBmjh-sC28bWhDKZ06aYtlc_KKEU5w1DCljpt2OrLp2vKgInq4vc9BhMCz--MOwv3L333As_1Fx9GR6Q1hiIlqnBUrcPXrM6j7-46aAjWkeF_3yoVBX7wiOlAW4OiNATE-08iERT8w6hQP2AELz_Wi89L3hHPRNpphPXg6Hut4b8U4-zAwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHHK1ivRU8b2duwlG_37ZteIONL3ZMm-S4L6lvnS5cBs6AVFZHumHUBfkZTXdoDbT-2aNnPDxVpBAGdUa-wQSuWRiWJzmi2ZBGLBVNGfHIDOzZmeDX2s-W4SrEzjAEZE8zELZZDGJhvObXvUaS6CVp4ypY9szSurGYPdLRBmjh-sC28bWhDKZ06aYtlc_KKEU5w1DCljpt2OrLp2vKgInq4vc9BhMCz--MOwv3L333As_1Fx9GR6Q1hiIlqnBUrcPXrM6j7-46aAjWkeF_3yoVBX7wiOlAW4OiNATE-08iERT8w6hQP2AELz_Wi89L3hHPRNpphPXg6Hut4b8U4-zAwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c--3oUJwmP-CAos63L1d6baI2NWbdHfAeICbZRdl6wkPCqXBoDwYATI6CSpD9wloffM8CU3XjQ8aO964km-pNV2taK6cgnYZZI1MOsmUyTQsmB3M6S-fmMmzXjGFe26NcHOhMlbrj97IZltjjGZh4xJ2dBUeYorIwnIsWn4lh8NpAedGhXY7U5nfht8Hch9lH1YaOINnDdpxCgznqJycX0DaryGzw_FCXrVcNYZy9CPVVyKy4Cx9Jsaop2ANgVms5bi-fb0M_UsrxShCLznId4-KwnCUWCErOeLswH6mNUTOw2EIYLPzkYdLdDRTpV785mjcYi9mQeY_p1pXRIS-Jg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=uzZpCMf5BsKoL7tJ7kwsWnYrL7-zpdpzI1J8d7szfwCapjD91nCmTYl9kfINcKwqA7V8Sol2AbUcCzXKilj2g4y7UFe2t-ZiDu5KDca7iFyKTAfubw9cB2eGscNoAgwEX1itKDF4SzMAt56HX9fff2yPaSochA-5kkTwHMIdkvb8bC0tse0MqBWLZ7ed9YvrDiCII4exSdviRIeAD7Lrro9hoIF0X3h1wacgmdj9owpW-psMxCXeiUNnYx_VI_vw-lEH8M75BLXAvNWJsfcrI3cZRzqxJYbdpxEMEm5ysOcRQ_VeVjNaZexZGDdIyw4w5aKHiQHG3bsNZn1JyISHIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=uzZpCMf5BsKoL7tJ7kwsWnYrL7-zpdpzI1J8d7szfwCapjD91nCmTYl9kfINcKwqA7V8Sol2AbUcCzXKilj2g4y7UFe2t-ZiDu5KDca7iFyKTAfubw9cB2eGscNoAgwEX1itKDF4SzMAt56HX9fff2yPaSochA-5kkTwHMIdkvb8bC0tse0MqBWLZ7ed9YvrDiCII4exSdviRIeAD7Lrro9hoIF0X3h1wacgmdj9owpW-psMxCXeiUNnYx_VI_vw-lEH8M75BLXAvNWJsfcrI3cZRzqxJYbdpxEMEm5ysOcRQ_VeVjNaZexZGDdIyw4w5aKHiQHG3bsNZn1JyISHIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=kYIei21VSozS-cOrscYX-h5f-yhby_Ve7A0hJ2VKhDRO7_vEFRHFRvwCj3TTFuWF1IyPfmb09p6iWJDPO1goqEUkDSFJY0-qltcducRmkA6mH0YiC-I0hp0ykWBaT_fDsbp3dQwV-GWSEWGbsqRLVzpkynwKFrwyg7CdP8B0tUgtcuCjGG9pWVqSET5t2P-3E-r4_P-KlV4J-kop2Ki2xeR28-CsyTK_go_YmbYOep53vmElaZsz2reUAHj1wtLaZZAoiyJYFFNGs_QUuz9G6PS-_d1lfY7ARZTdqYBjpSP9lxW-JhUi1L6aZu5VpggCIJWgx4SosTuomNTg7WGaTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=kYIei21VSozS-cOrscYX-h5f-yhby_Ve7A0hJ2VKhDRO7_vEFRHFRvwCj3TTFuWF1IyPfmb09p6iWJDPO1goqEUkDSFJY0-qltcducRmkA6mH0YiC-I0hp0ykWBaT_fDsbp3dQwV-GWSEWGbsqRLVzpkynwKFrwyg7CdP8B0tUgtcuCjGG9pWVqSET5t2P-3E-r4_P-KlV4J-kop2Ki2xeR28-CsyTK_go_YmbYOep53vmElaZsz2reUAHj1wtLaZZAoiyJYFFNGs_QUuz9G6PS-_d1lfY7ARZTdqYBjpSP9lxW-JhUi1L6aZu5VpggCIJWgx4SosTuomNTg7WGaTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=p7rqtmnjZsG9_2swkGo5l52-HnGzePHzbLCex6MG2-GjSMs_VXDyEIDS8YHquotcjHHpNDNvnw4G3Tsdb-S87obaSYVASMmIoV4shWs6ttmcZDMUu2Pfh2_glfJb83xkzAaTCfSCzzCL3tTFC3u9Pi-StufLYUx6fukRGGCJw9ywLO-i1BYaJPSaJ0Mstz0KZGwbmoRZVOj_XlUewWqpo8emeX2mPtfsGTBuQAeBUYpzb077HfYpaGFRG7G0RKo2_v9i41-XejWT703AauJUu-H9OS7EctORUw_5Um2jBpCqrIKNQqQyFHw11s_Y3GSXEYhWSSiivmg47t4gpVBRCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=p7rqtmnjZsG9_2swkGo5l52-HnGzePHzbLCex6MG2-GjSMs_VXDyEIDS8YHquotcjHHpNDNvnw4G3Tsdb-S87obaSYVASMmIoV4shWs6ttmcZDMUu2Pfh2_glfJb83xkzAaTCfSCzzCL3tTFC3u9Pi-StufLYUx6fukRGGCJw9ywLO-i1BYaJPSaJ0Mstz0KZGwbmoRZVOj_XlUewWqpo8emeX2mPtfsGTBuQAeBUYpzb077HfYpaGFRG7G0RKo2_v9i41-XejWT703AauJUu-H9OS7EctORUw_5Um2jBpCqrIKNQqQyFHw11s_Y3GSXEYhWSSiivmg47t4gpVBRCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDe62sl6WNaE9OLerXClyGamsrFvpl7KLmkabwFwuieY3MUtwNYTBJGlGreDjwSenIgvnJ9Y-AZetxwPdopo7VJPjAWtIEuuGtDd4_RB8Uh19UBd0Zffk1ACKGd1ZPQ41nkueQqSp5UnZNE11DjFgA8aN5mtWCdrppTM-jyz8s-piSkGDl7zVQWyrcf3s-g_Tx-v3l900HLbNfpALoL32U5-OsOQKB9tTweOySbjU8U8zKo4WZBsQDuPXsfEZKDSR0rucRPsv41YPtBdR7ghy8WFDiv7OdfXpI8hZ4rTUeFcEB6obUmYqVx1Kt6I4ar6scRHRpjBSCRv9rHlY9tpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
