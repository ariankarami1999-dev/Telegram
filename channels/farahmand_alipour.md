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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 00:56:25</div>
<hr>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFAKKtADXspnczadcDCULO632uV3rT8mVGpdjj6p4tdnPDgz6HhiFgL8Ow-ZfFk437V9BfRkkmKOaXv0GVYlpArZya6tuxkmnrBvIsSFSfVlnYZuKHYk-4TqkxD0YYUwCIZ7o6TghImmMdkYt_plAAX4rTIDMSdVLZuBT2WrEq-2jIGCPv0vNbPDl45z91rlZLuhKaMwk4o-a8ZGGASFClgVNXF-XsPDVPck-T4CbmZDjG95M11LcH1DrFyqKd7vCtb34jtHx8Iy45i4JCMK2neWAWCwsG8_U8xQnlPwSA8j09mKDLqjmSl1OYJfFRwrxR7lNMn_NSc7_DtMkLeFcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dziOjx5OoNhD_-9DwbyrRpH7HIIgqiQf-louNM7RwEiviwUiQj4ftplmKgHL7PqIjB22wtTte_F3nO004BDYShcipYIwYBp5Qvvab7eUtp7Fyc-KmgZHPvC42u29jlay76yMSC21BHMXP4_Uw84FmsqiqR7BvFJljsbyms6zfJGhVmssZcLpdbKWNyt1mGxy4QgLP7Q-ZYIXeJa8Wr8JVedkGEvnfTE5vHxO83Iwd-UT8K1FvV0rlkBbT-Bs8mfJygFLgEWJeAIRx80NYhtHNwhsGZcdsyt3Hkg03kpDYMGVLX90Ymfg90aD0DD8knkaN5PEB16YH5_jXTimDFrnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=MHmsdgLrhKxdZvuuoy2swwhjUHz_nL_rdYPLT_v1LVd4lafHrAqbiVnJ0VFkQ5kS3E3fbzuL4q_Kc6G79ARVLVL909k4izAjch_91ebElmcmApV4qPKJHcH64qA1XhPACshsH5JKEUsodrQ_7Dgjyv3OVfu4l6ugkWgJoVXDAJfJSPWgihtG-XBqlj3VJd74hTk5vYCeu8yGbatoD0vnEqZ2tYxyoCTryXI8mT5fJdGLRvvkYpJItntVhPoXUfANtacxNbr5cYksCky-bzA6yUM1QjpKuYUj2FlSV0_xlbslM6DYcfagn5omZ0oLqnYxcqHzsAffjNZvEa6rzj9NDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=MHmsdgLrhKxdZvuuoy2swwhjUHz_nL_rdYPLT_v1LVd4lafHrAqbiVnJ0VFkQ5kS3E3fbzuL4q_Kc6G79ARVLVL909k4izAjch_91ebElmcmApV4qPKJHcH64qA1XhPACshsH5JKEUsodrQ_7Dgjyv3OVfu4l6ugkWgJoVXDAJfJSPWgihtG-XBqlj3VJd74hTk5vYCeu8yGbatoD0vnEqZ2tYxyoCTryXI8mT5fJdGLRvvkYpJItntVhPoXUfANtacxNbr5cYksCky-bzA6yUM1QjpKuYUj2FlSV0_xlbslM6DYcfagn5omZ0oLqnYxcqHzsAffjNZvEa6rzj9NDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=RE96rI0MnW9fWEBSwrTqHKGolk0NYXLOEP2cYpBC68xnu3vomVste5Hnpti3BKhZRV9D_PS-b1Is63e_hGSOegrV0YUVB14-gnvgAG3j2lqsNIJQP917S4ecN-58xnsyxG9kaHzKdGcevGU-nJRsMKk4ebDTNShTdSmnUq-3yb1p6VPklnTYvZZPvoS34lKFR4xwtr5BemW_L4RJB0YkC_YYBQJyqcLoBhY1XshogSKGb2IOUmet4kUqC4V59Z7JGo15Rmy_IZ-ntBh5A3v--LLdPsV5MqJ1NOfs_zqO8QunTwnkTiRXXjp6oAbmQEPuOhaXD9akiUC52xuuZmFQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=RE96rI0MnW9fWEBSwrTqHKGolk0NYXLOEP2cYpBC68xnu3vomVste5Hnpti3BKhZRV9D_PS-b1Is63e_hGSOegrV0YUVB14-gnvgAG3j2lqsNIJQP917S4ecN-58xnsyxG9kaHzKdGcevGU-nJRsMKk4ebDTNShTdSmnUq-3yb1p6VPklnTYvZZPvoS34lKFR4xwtr5BemW_L4RJB0YkC_YYBQJyqcLoBhY1XshogSKGb2IOUmet4kUqC4V59Z7JGo15Rmy_IZ-ntBh5A3v--LLdPsV5MqJ1NOfs_zqO8QunTwnkTiRXXjp6oAbmQEPuOhaXD9akiUC52xuuZmFQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV272CHPywM3jIcUHJqX4D077wDvMSjJtaotmRY9qa2MEDtTOuPxn6vNov3p0i5JZgJ4oSuBXSQo0EiwXoP56NsehKg24gihVi9PcXqNsMq-ZbyaQ6SdNFNpw3NSNRWB7x-gQZT7CuGxKigcVV_AFpCEdoFg8gDIxI1lGO9qD84TSjdUPEqBuGy_n-kbQcDKBKFXc8mguqTopYiKqQyHwjGHsRzc3tDRviq0rFhhoPMLrWiQuky6p997AQXStbD-bifGhCOfGym3w8SNcDWSvPH-YldIaS4kJLvNQmjE-JwxBA5Bx4mSDCF-wFmbbGJMapbqzP2b8tsXGw-AtNtYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXwBWeJjEfp1c5tVoMv2iZjd6nuPTni38AQALx42AwDGWT_tcFsilUH0o06aa8uhqqbbmOdcuuLMDR55a3rpJszNCljKbN0_OPVjn73a9y5uPIj_pzdz7Qfx7XaPU-Rw7PIQZHH3wCVsqVhrSM3rU9u9Af2ers9tZ-N3MBHYh9h-3nsJmWDTls8XXUYqHVHR0fwtxmMvGNPc7sO2WMbsmx1p3wUUVVXMlp0HcDMp5XUir1rYd2jDPe9jaHfYvg-jS7H0rWlAn0hecOFdPbXzXwptLSBKlRQk6sQnWQNy1WiVqvfv36BPrs3mJ8fJ-JY0WlP5_UtHMQWCIFwUkOCA3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGrIpk_Etm4dzg-svBytSN2pxImgZnpDhIYn4fZCui5RO1RgWCvrHlWcQvi7BcBr9ZQt49IaGZg27fJctT5YtZLKH72NJ4IV8G6oUJHzGinDgfGk_A8_JazE8y5amXgVaU2OHl67p7wnyFxx_l1Azla1UUIWYHU3s-ntqHZW52eFl3JMAC47TvzZDROizO2GdsTlHWld09NczuoHoWIEAkPwUDJn2AP8Pn1cW27kQpFU5h_-xMpbeT4ICShX1WIE8dySTAfDkrrRMsiF67OKBrR19XGNxPIDlZNgg5DLN-XU1te3R9d8ec6FPePxfPVKIdZjLeg5KQ1Z9IxtpzS4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxO4YMf9LAWTomk9K4lr4HBVfmWMZ7_wrIcqcoYSyQVO5NwyCFV9l-EOAQFit6veonK7Sg1nNGzr2icf9S287Jk6wWntR0_lgnQTBv6dl1rTc-uz3loQlt49aJ6fljmH7fSqjb_34OvDtWrfpEbjO8ZJOtVx4gY_pxcQZe3belP-hYI8rsnUKIBR7sLD7x5FvXnYPqqvv6CkCtVVHOf9vVHm8POgSWdNRkzlyosWkBxN3rlCUWRRRP8alml_IzxcgJlvC33zDrBDywpGTm63U3obEoTjvEjgKgoO7q1ystXgvYxg7LsxsutVfhO1hRmsJbenBu79Gs-075JZc6vc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLufM6Iwm2EKKFZUMvebshfFGGQGKR-AlQwdmQV7fnPTH_Vt5DFvg5fQPyyAuhwYYl3tMnVVQut73H0wlbXJwRAeoIHoiNCKXmGQs8WOlz8l5gafKve2X5LzV_3yF-UqKpFRkz8jX_H5fAT6ja7bI4CctYlvGBlGWvjCyiW6LUbqAhQZfm5Ouji5_EgVDzvCwdLgR9UHkO65PiAAIbjLVt4IA8UpouJdiB9tnkWO4C0aWPe5SOU7XKxHe20WBIphZd7KPv2ZZBIRROhsT3WyNu0VRTJQGTWfIHvj5t1p159ppRR7JWntLZl0-z2UsEOoPy5MsvtfCK4KqTfCpR_B5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv6BJ6m0zrNGM1Ocpfb2wCd9HzByXfiukXW1prX68tJxBIoGwAuwBh6zThxR1R17t6KKfB1IxSxPAAt-ecTT9rOGwR8gOEmtUloWfDrShENuomRKp12jUZHUiDhg8kNq14a-4Gh2Tfn_IeRAyRzeUbgYFM8hWnQ9om8n9DEX88Iwc40Gf020kUIfCg1LA6mMG4ALbaIbdRPE9h76NiNAUjnm-AjNa-L6r_39jFQcag8D2RCzlbhXV-48Fb8IuUu5WF1vS9LE2LL6Jse2xV-hf_fZAAGfyulNHePxMLQZJLbBatJUnb23_PD_CcPO-eeAHm5T0bpuicPGez7Ty0t56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgHi6INfOASN6nYQCWbLojP-MlIWjtRIQJPV0l-N7cZPZ95H1mRwWvBXzMqlWr6BH8FHHBq-eSEI2ZIlsgrCEt0bXqSJNCbVNTdly9huolAk4RyDagTcCk7EYlILGVDKWsaO2UuOqfw1UO3_bLkwbSMV_MEQwyW1coQhJdXhzzxCHifA8FR2HYN3jNXcF67m41cB9ZqYwby836qjMCCuCwCC8QpcD6NzmGOWtsPFijnwdUhYzbFBRLqfaGvVqLddI9w55EtHbV-cMb6SLAKR_tX0k_1tHMmC82krlUocaSABvl_4qq5TacaO38RfaCQXL0WqR2bio5ORI2WeKrFMEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqUIO42hxUjb-VDJVVASjKFjOMHBCVPlO2NuSxQRIyNpjF1ijoJeQ_4tlysiLrSn_W7WdSSmmenNmSYMo7eVFdYAb4KsvT48Jy7aoF7neaD9GCitGEVwsXxTsPRdHa3hiheT-Hq1LghtBVY4V8LP9ePHft2Tx0QKAXxuhMljF_UlLaYkBXcO6FWOmDAgS9BdbDukJ0ILo7hqdbgmmfm0CxV7g6U_SFWBaehvtFEX1YQBnSbzPqFJwcG-lDkvebBa6QZ07iHenUks1NqX3MojYy4e5_XWMLG32FPajIGIH9N7PZ4PypYA46rw4DZUNFT0e89cWDMEoQwhU03mMuBKSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ty50yt1Z0P8p_xihzRZftrxKC28l6mPvuURX-tfEyMcbMzcXIOWxLbEG67ujO5YaFpK6vgO53FhVgbeLahkhOA7spLDVF9O4F8XvCdjhUyRlDOR_MuSZUrfPRwK8JJqLbmQyUNhqbvKdc_JLSA3iFGdhtMkveKVUfbWq_r4G1UFHx_VQ2s5iWqg1JDBs464AIwUui0HIPQrkrEZmOxOIBetY553lNwCQ3ts32RB3o2fvIptcKdJ4qckiKA5MEP_TrdZP6Fn6bT3xX0OZPVTY-VCom_ycYSsX0DP2uOIgNn7Mq_wd9yO8RK6puMncvi3dVc4LWlkm5Psx6FwGDLL0xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdSHWaya7L9TbMSyUGuyWo1riOGGqx8VYlEaqxMG65uPIqV6D4815MDDcCUoXqADM6FlIayUsUm8NoF8UY-9kmcmmCAETP3Z0aTpvxEL5P3wqgcGNWzmDyeXcwoQu9rpiuYpZS9A7m-5NW_rSKIF6taJkMNqJAB44tMNa5ZcysbAoE2gB9w5RhHQ4cjtaxBKFSY2BUg6zn10fg7aEVfLBd8OGiuMreX7TmTRCHBY0KCXJ7kgAviw9v-pBb9zq_DUEBchxo50sNYwfpsB2fy2orf57odbXLuD0GqJBJ4VqVoT4E5YhNzlNqioISAZGGrGQ8O_OyMCTNiMTGCqOjlJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQlo7ivYM0zDLWKwoyyViwkNegL-qJbGZMUGgeooAO3w91g8uz-gv9tfrY23RE2__rrQ79egisBttobPlm3z4N4_9zNAK6FxxD0NuOC1OHo_hGVHfyuKLgoAbMQ_BhJFMeYeqMzFmuEBiSqQ-zwoWcddapTiqD3Fg5qiDHV-J_A1r-cU-djWv8hVSbNrD9iRgjI0CDAW7NUJuJyfbmjHqMQgkDKIpuzwWAD-EIHYrk3EVgt6ftOy66YsGYPpfAfCyTM4W_byU987RNNUVFtRF6-ZayuKMJ1Nr7A5d-eO2NT7NSTojtiZhv8aF3TP9wtxQGNXvlHXkccx6YPWdw-hrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=lZg-94e4eA1yOil0mBT2Uq5vluUGtA-nFNqiLC_punxjbjyId9aPd5Cbw-UUWyknEs1zLgzximO_GPRfb3C6RA7dM3uvl3-2ZwR1Bk3_lxCwDwtw_qnThjw0HIESjP1YqhLBTqDIUTYSwBe5w1veOXX2-awQavU6Ye4ifCIZ_h0eSrQZ_kfagtIyJcmcgbbdY6KCg1U5txyJ26iuuqksitOuPOgs4zOUMFTCpcSsvF3tli8pkKGYzHZ1tVZMN7q224SBrcuBW8rA41VUOvjvlb-QriGSLNsy-GB98H98wC695l8ggM1pI3IxBzr17gN0pXDUxDnADIMOE2e0-_GAxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=lZg-94e4eA1yOil0mBT2Uq5vluUGtA-nFNqiLC_punxjbjyId9aPd5Cbw-UUWyknEs1zLgzximO_GPRfb3C6RA7dM3uvl3-2ZwR1Bk3_lxCwDwtw_qnThjw0HIESjP1YqhLBTqDIUTYSwBe5w1veOXX2-awQavU6Ye4ifCIZ_h0eSrQZ_kfagtIyJcmcgbbdY6KCg1U5txyJ26iuuqksitOuPOgs4zOUMFTCpcSsvF3tli8pkKGYzHZ1tVZMN7q224SBrcuBW8rA41VUOvjvlb-QriGSLNsy-GB98H98wC695l8ggM1pI3IxBzr17gN0pXDUxDnADIMOE2e0-_GAxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=rTyl4bPchPr4K2EMiMrDsSb5XNKyLsjR4EfQdTkCOMZFOw3RbM1SX1HKiZOn-v2UU3rZS9E4WGjSQxkP6wWN77fmnghFY6DsAq5dLF618M5X0bfBX7TCxWx83DZFaiYosiH3dQxLrfsAs_3BFTiMCJsxUD5OMgbuNUhcCQwUwxft1IIPjPenSZQh_Q1lews-sotoDvQC3E27jI9RG0_aObSxy_yZTep6tUs58LPJEfnXyHBwMElZ68xJ8XUKZRkKfwVWKG_Q38K_0NsBNt00suWmcclmjy536tyPkMLWQxsBoB29VkZHVC-cfxzE0LsCmH2NH8E_4EF2CRrhbU8pVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=rTyl4bPchPr4K2EMiMrDsSb5XNKyLsjR4EfQdTkCOMZFOw3RbM1SX1HKiZOn-v2UU3rZS9E4WGjSQxkP6wWN77fmnghFY6DsAq5dLF618M5X0bfBX7TCxWx83DZFaiYosiH3dQxLrfsAs_3BFTiMCJsxUD5OMgbuNUhcCQwUwxft1IIPjPenSZQh_Q1lews-sotoDvQC3E27jI9RG0_aObSxy_yZTep6tUs58LPJEfnXyHBwMElZ68xJ8XUKZRkKfwVWKG_Q38K_0NsBNt00suWmcclmjy536tyPkMLWQxsBoB29VkZHVC-cfxzE0LsCmH2NH8E_4EF2CRrhbU8pVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=Nf7XfOkN9z_GymKA9Ns8Qc_gNl1bX4gXucPv7-Aa5S_eWGrBTTtqVOBiJtS01paCTZ755EI4eSkQFRD1JckN7Uzty6uMc2UphO1alCX6u-WvuOUUOSYaMaQ8bYcHTbl0ZjyBncdP6E1v0JUgv-_maJdTtmrwLsjG0I6sEM1hnvzcPOPqA-zm_K5YIc490Ot9HyyUS6eKpPkqJhPaYXKxsm9CrOixFwOF1GRitRHC_qhfCHrxnEwztvRCkdlnYRn0IBn4ycdm5gFtIioft3Hj9dlFqJ7T9i10fFhCXiLzwxJu1CypvFo2gZ7hjrNeBBY7B_bQQDwb0EfMIw0CB_nOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=Nf7XfOkN9z_GymKA9Ns8Qc_gNl1bX4gXucPv7-Aa5S_eWGrBTTtqVOBiJtS01paCTZ755EI4eSkQFRD1JckN7Uzty6uMc2UphO1alCX6u-WvuOUUOSYaMaQ8bYcHTbl0ZjyBncdP6E1v0JUgv-_maJdTtmrwLsjG0I6sEM1hnvzcPOPqA-zm_K5YIc490Ot9HyyUS6eKpPkqJhPaYXKxsm9CrOixFwOF1GRitRHC_qhfCHrxnEwztvRCkdlnYRn0IBn4ycdm5gFtIioft3Hj9dlFqJ7T9i10fFhCXiLzwxJu1CypvFo2gZ7hjrNeBBY7B_bQQDwb0EfMIw0CB_nOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=cYKTgi5ygIdpOND17ah00ywSBSWp7EAfXZpl5GgrUOQI8xaopZbi7yH81fPdx6qJmtKBUlH2vNNWRLzOfjnh3B8ybiMc1zk3V0CnVicvJ7zorR8MfiF7Ab4ErmKpjgKjVFR1akeYDg4fbHO9CgzyCFjNdnlpMAJgFCIhMsPF8gQqbgfsPSJGi6LOsYNGeYwA11s-BCgncksZjGJ3DM3VwO_-sFEbfKXk1Vuc_JFS_ye3w5cNgtPclRItWPU9NqUAo79ion13KEq5L3wHPFk6oUFUR45x8apU4tUPw71u9McVpFBa_0xL3d7tWLR3e0V70VYaNQxvUNEL51VAAQ09Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=cYKTgi5ygIdpOND17ah00ywSBSWp7EAfXZpl5GgrUOQI8xaopZbi7yH81fPdx6qJmtKBUlH2vNNWRLzOfjnh3B8ybiMc1zk3V0CnVicvJ7zorR8MfiF7Ab4ErmKpjgKjVFR1akeYDg4fbHO9CgzyCFjNdnlpMAJgFCIhMsPF8gQqbgfsPSJGi6LOsYNGeYwA11s-BCgncksZjGJ3DM3VwO_-sFEbfKXk1Vuc_JFS_ye3w5cNgtPclRItWPU9NqUAo79ion13KEq5L3wHPFk6oUFUR45x8apU4tUPw71u9McVpFBa_0xL3d7tWLR3e0V70VYaNQxvUNEL51VAAQ09Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=LUAaVSMaESBTHmm-_6tFJCNZ2Yfx0EzC4c9omNaVc-4uMLbcYL4NJVWZO2ZAOFOMGJzAhADkikUIt0OAOA_BBxcIrOf1wBH1rhVzCKFxfTs4PgMziwVUfc9NzdiIEvEvlnajqEm-lGbnxD_EkRHHVYrsZLbF0F5k3kTycenwfNhGTmXSDHZetCqSXEBnYlOzF6GJMBNVU6HZvRs2CR6Xhcjzq5Sfp1zYXRIqjs-KUD4yiR-xFgkWfannuwv77fwTgxv1dS7NQSd7n1ioSAzvP62J68kyKPJcf9AA0gs4CyLMLurmzpPqCmnWOBjB13NUTatClwJzVB2Nl05CzwUNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=LUAaVSMaESBTHmm-_6tFJCNZ2Yfx0EzC4c9omNaVc-4uMLbcYL4NJVWZO2ZAOFOMGJzAhADkikUIt0OAOA_BBxcIrOf1wBH1rhVzCKFxfTs4PgMziwVUfc9NzdiIEvEvlnajqEm-lGbnxD_EkRHHVYrsZLbF0F5k3kTycenwfNhGTmXSDHZetCqSXEBnYlOzF6GJMBNVU6HZvRs2CR6Xhcjzq5Sfp1zYXRIqjs-KUD4yiR-xFgkWfannuwv77fwTgxv1dS7NQSd7n1ioSAzvP62J68kyKPJcf9AA0gs4CyLMLurmzpPqCmnWOBjB13NUTatClwJzVB2Nl05CzwUNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=rIfCgUUJrYSSXeWY3EOMVgJMmCNK2IO6mPI8YEJWXreKb2icY-Kf7mD1TJSNm5m6hkSk3QbA9xpGM1SR8siqNhoprdRAVFU7hynSAQCDIH_jMgKlE5pMf1z0haBrOTckhhtXIlJ-Su3xa9ozdIYHPBYWaoEUF4vMq4JBMqUaDXu-OVTeD5nMoM7bEAn-ysmruajAwXtFm_CkpK_b8ihzLrPlU_itbq1fLI0S8ZKeASgz24q-6kspiz4RGe2KDGSjOo4-pUr5ts5QNMZv_Nh3D3yBHB6PVZxGK1s14qDePMDvzolyv-h7xyjeyBU42toyJfPw4lplz0RJ8G0Gh9BwLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=rIfCgUUJrYSSXeWY3EOMVgJMmCNK2IO6mPI8YEJWXreKb2icY-Kf7mD1TJSNm5m6hkSk3QbA9xpGM1SR8siqNhoprdRAVFU7hynSAQCDIH_jMgKlE5pMf1z0haBrOTckhhtXIlJ-Su3xa9ozdIYHPBYWaoEUF4vMq4JBMqUaDXu-OVTeD5nMoM7bEAn-ysmruajAwXtFm_CkpK_b8ihzLrPlU_itbq1fLI0S8ZKeASgz24q-6kspiz4RGe2KDGSjOo4-pUr5ts5QNMZv_Nh3D3yBHB6PVZxGK1s14qDePMDvzolyv-h7xyjeyBU42toyJfPw4lplz0RJ8G0Gh9BwLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=UcicBSCwy8htvBvbEfJSR8IiasA_ifG1UHVgqF2nFO6-DyE3rR-efiUf9IpwONnSqxtXcvTUDyh2wUwjVt2WNDVoVVd1GrN7MiKtJDz6d5uHUyTHPfrP75gfqkBuYrbgUWNjlK8APUft7tRJPDT7SoH-S8PhUvjLTFLbtMpxsZJn9gHebQumfX3Bf0NcPSSIo-14xwG5mA7bc3ofp7q24N4j1l-yLbIxVN8vrIdEjsgJaaAfVy1XK4J2rhAbEh6Z3HBPDC6JfjM8nMRUDRVr6fVf3nq3hPSwe_IRfkXQfuVONj5i9LgYIidegXhXlOmc6-jjQTEzT4Zi6WAQa0uaIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=UcicBSCwy8htvBvbEfJSR8IiasA_ifG1UHVgqF2nFO6-DyE3rR-efiUf9IpwONnSqxtXcvTUDyh2wUwjVt2WNDVoVVd1GrN7MiKtJDz6d5uHUyTHPfrP75gfqkBuYrbgUWNjlK8APUft7tRJPDT7SoH-S8PhUvjLTFLbtMpxsZJn9gHebQumfX3Bf0NcPSSIo-14xwG5mA7bc3ofp7q24N4j1l-yLbIxVN8vrIdEjsgJaaAfVy1XK4J2rhAbEh6Z3HBPDC6JfjM8nMRUDRVr6fVf3nq3hPSwe_IRfkXQfuVONj5i9LgYIidegXhXlOmc6-jjQTEzT4Zi6WAQa0uaIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0jVOMxE0KqwYNyPFR3LU0C4USNIspmW4gW5DqQoy_x7sBzz2XSX8ItowWCSpp2HY2HH3YPoiPhdOKnfSqGyWmzMBAPsYCvC9h0sTkU4Uet8qyYoZXTGlxNuZMUyV_SU_VnQv6Pm1oDTgSp36qwfm9IuaKBSe3bko1E6w4MzK6NRvi68ndGkn3jgILaKyn1HZJGL1rLaDa3bo5UQBAx5FJykj_lXGilbtj6aRHfLylFwV362t_MU8ki4QCPZ5HbbMb0JwId6zTqb196KsO-kCCWUSx0le6KR15XI9HiecKKGCnxnMQFTl-LwcFNHVR3ffCITfpqS2U0yDSicv6OK4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uAHR4kSjhehnBs-ScajVOsr63k3Ips3ZorJRO2XUiFc-09bxUtiMV62mkV-ycMMZfalq0xbCahPAo8KOMmy0ujvoiOAGKpICaTgFiZjYXXqMJoTd6WhSBn3FvoFJ-iVNqqyAsRWSIYcQJoGhzzipptXXASgTLoSEtT4iMB4yZoAvz_4NLR_bQ27n2Y_mYsYbDSokYYgeH__5OIWZOOBYtDfJXh3H5D2-eEfFcMeKDADSrzaF7_u1mYP9TwCrK3JalTEJPYdx-2NzXyyZJEnS9cKs_LIE0rWlxAHhswBGg4VY7VjX7qQQ-1Pesgxx2XAkvPKUX4HH1yQrCvpbWXVtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uAHR4kSjhehnBs-ScajVOsr63k3Ips3ZorJRO2XUiFc-09bxUtiMV62mkV-ycMMZfalq0xbCahPAo8KOMmy0ujvoiOAGKpICaTgFiZjYXXqMJoTd6WhSBn3FvoFJ-iVNqqyAsRWSIYcQJoGhzzipptXXASgTLoSEtT4iMB4yZoAvz_4NLR_bQ27n2Y_mYsYbDSokYYgeH__5OIWZOOBYtDfJXh3H5D2-eEfFcMeKDADSrzaF7_u1mYP9TwCrK3JalTEJPYdx-2NzXyyZJEnS9cKs_LIE0rWlxAHhswBGg4VY7VjX7qQQ-1Pesgxx2XAkvPKUX4HH1yQrCvpbWXVtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=LhTkJ4xAjiYK9_QWND9buAUjDkeLyQ_JIY7FPP6Absrkg5cIh8cOk6vw8pwA2_6Z90ciBJ9aYLB0ITz65CHWoC9A7WapnY6ZLxufGRmNP5NY2r2nLx_WjscC6K0ilffkjfcDaWoDLbDTgDt6xrs8HvGkaJCDQGXbcQ6PWQ3Bx2OHutDixmQkjmzRHFuGEzXA5A7JDQCF1FONRycYgt4-VCrDqY53IUO-A5mHo2iPECyRZ0MBxJJG7IWU3EiMSLYVFYyBt_5UiG3AEe69IojAVA61o0U7dR5Or1vaWwByW8SPP66sb5hv-tOrM4vsrMLuZJowsvWfwFQv3Y4MuZU5hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=LhTkJ4xAjiYK9_QWND9buAUjDkeLyQ_JIY7FPP6Absrkg5cIh8cOk6vw8pwA2_6Z90ciBJ9aYLB0ITz65CHWoC9A7WapnY6ZLxufGRmNP5NY2r2nLx_WjscC6K0ilffkjfcDaWoDLbDTgDt6xrs8HvGkaJCDQGXbcQ6PWQ3Bx2OHutDixmQkjmzRHFuGEzXA5A7JDQCF1FONRycYgt4-VCrDqY53IUO-A5mHo2iPECyRZ0MBxJJG7IWU3EiMSLYVFYyBt_5UiG3AEe69IojAVA61o0U7dR5Or1vaWwByW8SPP66sb5hv-tOrM4vsrMLuZJowsvWfwFQv3Y4MuZU5hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=crtDH02y5Ey9o-GacbzHIayqzWjFvQ749J-FA2HX6TCcNKFPj9wlflhShfiv4kouK9WL_dU08nZ1wt51-p50Mxkldg773lz8g39XKTbzqQu60ooAUKOrPkbcZtxQjBUolWb1ARE3oGD-mZlIlMmv3mX4JtK1Eym1Dus8zwgy8BZFi49RxQqFn5CDj-mR8X_7U-RGw_mkEcHQC6r2-r5Jr3j4z-NzdiAftI0Z4tTBttr_ggAZ8RPpD4rU1KKhQm9RR0WmSQRG7pOdKpqJ5ZBzcSjthrYDuxa9ocK857ztRaB_3L3qqeBViU4NE9KO8pwTIN5IGYPoEIlzTiHe60lsvWOvr09saHxRT8IdCWXd7tshmjbVeEDpH2KfcLFTrzLCFud3FxPTENGjgF434oiWQN_4_RRPZV88-pC0IpCOtZVfLYyaCP6lfAp-XFJvCeILR1kUV5sqH98djcBliVb0UB9v3SGYDFQSW89ewx5OfaD_VLdEcAWGdBbnbpAEZWiodhauY-l0Ne6VDV8YK9vPa4cgb64-qMXWB3TLS8_biQUZZ93JKXsT6WhuB0GJeltzwpcpcPGT_G8rWpfzbsBo6WFkNNkkj4NMtX76AUHVkCJvhgqiaWCWOxBW3oSsG2HWDdtKFeEnSgeBzwvCbxRnVJuPzk-pnU1zJdjglt0nyik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=crtDH02y5Ey9o-GacbzHIayqzWjFvQ749J-FA2HX6TCcNKFPj9wlflhShfiv4kouK9WL_dU08nZ1wt51-p50Mxkldg773lz8g39XKTbzqQu60ooAUKOrPkbcZtxQjBUolWb1ARE3oGD-mZlIlMmv3mX4JtK1Eym1Dus8zwgy8BZFi49RxQqFn5CDj-mR8X_7U-RGw_mkEcHQC6r2-r5Jr3j4z-NzdiAftI0Z4tTBttr_ggAZ8RPpD4rU1KKhQm9RR0WmSQRG7pOdKpqJ5ZBzcSjthrYDuxa9ocK857ztRaB_3L3qqeBViU4NE9KO8pwTIN5IGYPoEIlzTiHe60lsvWOvr09saHxRT8IdCWXd7tshmjbVeEDpH2KfcLFTrzLCFud3FxPTENGjgF434oiWQN_4_RRPZV88-pC0IpCOtZVfLYyaCP6lfAp-XFJvCeILR1kUV5sqH98djcBliVb0UB9v3SGYDFQSW89ewx5OfaD_VLdEcAWGdBbnbpAEZWiodhauY-l0Ne6VDV8YK9vPa4cgb64-qMXWB3TLS8_biQUZZ93JKXsT6WhuB0GJeltzwpcpcPGT_G8rWpfzbsBo6WFkNNkkj4NMtX76AUHVkCJvhgqiaWCWOxBW3oSsG2HWDdtKFeEnSgeBzwvCbxRnVJuPzk-pnU1zJdjglt0nyik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=W7uCruUaLevMlU2ZwqNduChdBZsj2ur7Oyo_YZb7SOBBQIZno-of6cFVKgn771BZ6lM_EFiOhktORy5IWK8ymmQCjv_4t8j4N_tw9fuawzJP20HtL9SocjDpfipajgiX3v9D9bL4XbZiGdwFOU9QF1Nl79E5wAQ0A8fiYq6GTTjxYkITruORaX5ATcSpZwZ-2ShPTaQRAmkbWBB8vyYyIIPPQCujpMpdtMobCYGZkY-GvQA1SdXvuTjI5UqM2NdHhiRthyKpH7L_QDfrRy12pjpWfGgN1KRLfhHr944APJ5Ig9gi0xunnPKd8SOGS9Fmmj0Ez-nVVuXJMDiz_jw4Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=W7uCruUaLevMlU2ZwqNduChdBZsj2ur7Oyo_YZb7SOBBQIZno-of6cFVKgn771BZ6lM_EFiOhktORy5IWK8ymmQCjv_4t8j4N_tw9fuawzJP20HtL9SocjDpfipajgiX3v9D9bL4XbZiGdwFOU9QF1Nl79E5wAQ0A8fiYq6GTTjxYkITruORaX5ATcSpZwZ-2ShPTaQRAmkbWBB8vyYyIIPPQCujpMpdtMobCYGZkY-GvQA1SdXvuTjI5UqM2NdHhiRthyKpH7L_QDfrRy12pjpWfGgN1KRLfhHr944APJ5Ig9gi0xunnPKd8SOGS9Fmmj0Ez-nVVuXJMDiz_jw4Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=W0hvSCUDhUr-KqDcrL2zAjHZT2daeMHmb1F7YjYN4DCFOKiSBlEWbWJ9VuYQ2sD3d8d3x-JFyjnwxj302TfCnOA0UQet6wPwEYy8vRn_08xfnOteM3VM31-FYEQX5km53Y9sjiXBwGnDp-en3XfTMA6KlX9i_IYEfr9iQXo2Zzn88BS8dKHMXmLVpJk-nPrTwizB6p6wcEvvoUVL1Ssy3Ee7U0FnrZpwm9nkwHcnI9aVhvf1i7ntLyDS_mhx3NZaFrXB8u_2hJiiFbr4WXky0GNMmBePKKs7NUcC_3a5Uy2iuCSnv4BPm7thUVBmpZ3jRcmlUySwi0IL1Iu2Q2baXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=W0hvSCUDhUr-KqDcrL2zAjHZT2daeMHmb1F7YjYN4DCFOKiSBlEWbWJ9VuYQ2sD3d8d3x-JFyjnwxj302TfCnOA0UQet6wPwEYy8vRn_08xfnOteM3VM31-FYEQX5km53Y9sjiXBwGnDp-en3XfTMA6KlX9i_IYEfr9iQXo2Zzn88BS8dKHMXmLVpJk-nPrTwizB6p6wcEvvoUVL1Ssy3Ee7U0FnrZpwm9nkwHcnI9aVhvf1i7ntLyDS_mhx3NZaFrXB8u_2hJiiFbr4WXky0GNMmBePKKs7NUcC_3a5Uy2iuCSnv4BPm7thUVBmpZ3jRcmlUySwi0IL1Iu2Q2baXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rit2AeNbEXo22QhRIQas388ImLicwgpwrYq2yo4m7Xjoe4a7ug5XkyPqR6NN6xjIytlcSp2Op5b3NWRN5SPab7A9nz8r5CZCEoRhmzW4mDRHA2CT9XMLKFDPfrFeJ2yN3e8nlZhMQqmcoUScm24gCpqfGdDXkNwzRrzfr9NVSsCtXEvlLO844e1dTv0QkIq8y2xxvr7lMwMT7gn-uy9USPk7CcU7jzMuegcsxdwYc87U1MC04FK64wboGDJEGKKuxVhO0TiPgM9ABxlFG3d1jkX4nZ0Ai7jltOEgJn5qxA1FctRvFCuieI1Q6n1fDoHjfmzXAEDnUqiJLEhmOMb7UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTj8p_CqNXNq00sPVs568R7R0tRDhH9Fj0977wWkuDgU87fruyivhcd92pOrSJS6wGjEXgo1fDPLOvFaxw06LLKfv2eUw6SdBh-pwrce6w_mlVlAP6XIA5RlCdpFXHGhl9MjFpXrUs9E2CL3taXdpVUUMUcn7hdzPnuuxjFVBiu1gMZ5rXOxxYGfcywcsNSIGyZKpj96zjP_Dx28kRrqKRc4P-87H6sAR1cNYOvtpBhTfVoIL4itkKuRG7Kz5I-0Qtx99dbhhlEhbgOqOc5WtV-6ID04mVPQPRn_URfyqyIfUx6JZKRAn-bTVBmAlO1ASe8bo0-198OYxPFznLkA7A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=i2mbK-M3J0zYjm3sLULADsDBFrhtkY-MzNHjpbqVgILCSdwx3BJC97ePlu-37_FncPUnM8LcOC4Ayrt1VQKogriYppluviME9ng3xmjpzDWRPkbk0HGW5U5LD-MzkZebfyF3MyNLPZj9g1taV9MD-0hFnjO0eO9q1pu81r2x-6a0YAXzbDLoD1eEWCHuEAPlKqdaIuO2r44eirBwg3u9W8NOLgrkiZSyKwx4-31eMTz6r3XkcrckY1OPDHBN9HB-Dr7_U8OqWvwiPOikyKDza7J1giOsxRiiJs2_mrB8efpCEqnHL2e0BdzUjC66BA4fYe9p9skJDRX-YSq5T6-wh4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=i2mbK-M3J0zYjm3sLULADsDBFrhtkY-MzNHjpbqVgILCSdwx3BJC97ePlu-37_FncPUnM8LcOC4Ayrt1VQKogriYppluviME9ng3xmjpzDWRPkbk0HGW5U5LD-MzkZebfyF3MyNLPZj9g1taV9MD-0hFnjO0eO9q1pu81r2x-6a0YAXzbDLoD1eEWCHuEAPlKqdaIuO2r44eirBwg3u9W8NOLgrkiZSyKwx4-31eMTz6r3XkcrckY1OPDHBN9HB-Dr7_U8OqWvwiPOikyKDza7J1giOsxRiiJs2_mrB8efpCEqnHL2e0BdzUjC66BA4fYe9p9skJDRX-YSq5T6-wh4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k17YVKIu4gTOpUCcc4qu8OKxo4Lj1aShQfcFCB_x6j2ZvveUZvEfZJkgZHxTsitSh4yqyrhq2g7slNBzA5NvVBeJjvuGxcTGXFHXXh0xn1hTWOjmFNj4_bBPIfGB3YSm1g7iLiPj327rfV4vEfGerrCsLG_7YymLQCAidAFY8G55KK4tUfegBXdKIXU3xOPwWyrhx-fV6Ql9ix4LP68oLD1DzVt-22zmeWrVxd7H2KgktmB63mNFupHoc9FZS8drgHGpq7wqXN4okhIATsS3YKfl2GsM1H2TFjBxAm22d9AYxdUaViDmGEy_jJqgRKjQ5XSgxzsHTiu_ZW4GAcaTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuXgS_ZquuHc8jb70SmkYZUcv3E-x8QBBN9d3yfwLsuAIdar1ilDspZeqy6lMAutCFn7cy1oWHKtDbtbPAT-4muggIMfiiyZkjHd0DJVzir3FZRB5hMb673zcq1gN2AO9Z98ywb1nzwwjldNqoJdOgiD2gPWkELvTXzBShS5RfO9F1y1PJB0tFU6yj989dSuDvLsI3yRxFxwlfH0CBd-62rsurH07FsVJmTsxKDsmtpWXyqUCvntRx_Y7AZA4z73ZOeh0jAHUh7vWtp65awp-MHGjZyL48UakWv5siQj1_X8OUpkZPLmoVUOEnWJPyRnZsbl0kvqG0S-p5RDoX0dBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aV7dbNWSa_wTGQj1IiKATlRelU8L-1EtOurNpxoallWUSYUGWZvLOko-WBwBiW5JXggxE2ypWRwAJLqthHHH5dr1y8QCFCkh5rnNKakEidYZ2g75iEZKI9kpVWLdqdKzj4oUOsNG9h8tGVe9DxTpnX2GV_hRSmejLJUTofGomCuNuhB1w2t7B8E14dmeXO5UJpJtq4QHcHk_RI8q1hubkCuABiA4pkv0f9WhArGF54cbZm3JaEWZ6VzdAm14gaw3aZqWOjg6sXfBnETkHK3FK1987i4AmaUWp8QpnHdakX8__OuoOVGJdgc_3SqEdQ_CrXhKfODdg9Z1wpAsqw-2lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTf-heX_tKQdoAlvvGw7Vvn3s_48ibqevLcas21YCrtBNJsYzL1aY9yFT01WVj-fM0u5a4wdVY3BKpPh-zLXlcSUsCMhfY352K7O0gkDlx9Wi5lvYUZycVjTGReXMUcWdA5SeM8TKO6ffo-KCuSVgTaaLT_rnwCMsSSjtQIq15tJtT7mu4mJWOL9ClJdyY0DgjOO9sgFEXnwPg-D0c7xAN5GSux_00bbSieHaETKDe_nT5TznDZuTa3LSAvGcow6tVyIKprpBcINYnRDkmuzn3eIBqHsDLvnOnDqwweATZV36XcLy1-e1cm3zIcBeSfah2qofOFjCBrn1E_oBwpOkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=h-LXpXQYID37QD1hyJW73Pcbc7z_OJtKtNfcj2-GTnWYUV068sMKOh0HVwsmyI7gOzRiKLxZSK3s-46r44KFQ_b3xgZeVLtE8WesHzjyWohvBK3CqHOVcNbZVy0ZYphl7ZD4iPM9Mk28JCRMwTVsxt7dToy2cfYebKjDuoWRYUtf8EWOwMOaZtIVF-tFM0MBzuJvQMI-XLTcfUEDoIDP2XfanglBIPNPl0LnVgW5F1T2E07x4fdLOo8X8JqQ6RdEhPfueECUO1Y7vCLtagmytuWk8BLjq_c2tDTiiUFQ5mxQsnm0RrUxEIwbjzCYpAdVQIV32Ivk-PqkigMnWRGSeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=h-LXpXQYID37QD1hyJW73Pcbc7z_OJtKtNfcj2-GTnWYUV068sMKOh0HVwsmyI7gOzRiKLxZSK3s-46r44KFQ_b3xgZeVLtE8WesHzjyWohvBK3CqHOVcNbZVy0ZYphl7ZD4iPM9Mk28JCRMwTVsxt7dToy2cfYebKjDuoWRYUtf8EWOwMOaZtIVF-tFM0MBzuJvQMI-XLTcfUEDoIDP2XfanglBIPNPl0LnVgW5F1T2E07x4fdLOo8X8JqQ6RdEhPfueECUO1Y7vCLtagmytuWk8BLjq_c2tDTiiUFQ5mxQsnm0RrUxEIwbjzCYpAdVQIV32Ivk-PqkigMnWRGSeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=DoM9Ybvng-xwZ-UEE1jX4fsPq_gUPq_wFGWxnGvbNTkJhOHoHvUzujQPBEMSzuaCae28ZASiGP19NYg-U_4xTOtJP8WSkgMpANRZZQAegw_YC_TsUMjm1BagctwybyJMZQGmadaDx5INXiBUbqms7HyaVc8RPDe-6EE-aM2AkSb2JV7a7MfjPL7QPgFO3UqU8xTEpQKpq1X0PPjFweLyY6QdGtl1pr7gyocgmHKb8JxOsqnIgZrs_41w8mSsAU-KpKRIwA15nZm9tE-Kwf9Ydt8Flrtb0Zy-7Wobqh69mec7XoEdLZfVkkG5nDUt0EnoA9WTKmYXZRCG-_YvZfvETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=DoM9Ybvng-xwZ-UEE1jX4fsPq_gUPq_wFGWxnGvbNTkJhOHoHvUzujQPBEMSzuaCae28ZASiGP19NYg-U_4xTOtJP8WSkgMpANRZZQAegw_YC_TsUMjm1BagctwybyJMZQGmadaDx5INXiBUbqms7HyaVc8RPDe-6EE-aM2AkSb2JV7a7MfjPL7QPgFO3UqU8xTEpQKpq1X0PPjFweLyY6QdGtl1pr7gyocgmHKb8JxOsqnIgZrs_41w8mSsAU-KpKRIwA15nZm9tE-Kwf9Ydt8Flrtb0Zy-7Wobqh69mec7XoEdLZfVkkG5nDUt0EnoA9WTKmYXZRCG-_YvZfvETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dACWOVDaLxaKlFM4NlmtPrsWbAnhh8JwrpW3I8-iSXEcBQcBSWYqDAHvyePL6cBFNUDfTSUp3X7SLgLNHz2CRx8rY3kxEFiwkDFK5QAFvVRbCZIMPQhEy7ZO_9scHf6kZsHCafrGh-Oqai15z9kIuFH9AdJpVGZcybQcgGTKV74wTD0yRJ0fNjpUDUZkqF6Vqd8lNEHwpytaIoLRES4sRQffY9pwWgAe567kJvMLvbS5a-L5drR-_wVISrQy8FT8mTRyankOytQF_uUqwVLRG--Dg-9pz2gvektXWhQ2n1Phk-Sx--WueDV9618Wu3TC9_dp8WSqI4qL9F_3cbqW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=n8Izrn4UuPsT7dh9SwiXLxea-Vo2xDcIAQbTmu2Z0xbCIyPkDKCQ_8jEpZwGOv7bNVTIycfs58HFp-4JEst2zwErHzZV-rWP_ILUulfVtowGbhqoIpvN856FoZJ-PbZy_G02sW0RvgzdjcXk2KIPEZbKAFghKVdzkVRj8IBV9TcD7yYiT-3UjgQfc-CRnu7p9ycVbc2LazqF_f1ZWqpKME0m0wcRkcc2Z0rKvq8KDEPLvhfFOzROSUcCCv-bVAHTZp14o-Cq65HZrIzu2qp8oj7ly2pJLlIYH4ESLO3T2W6elFFcKfTs9MKE64by7PGvThUjMMZhsIQwsUIM8wZhqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=n8Izrn4UuPsT7dh9SwiXLxea-Vo2xDcIAQbTmu2Z0xbCIyPkDKCQ_8jEpZwGOv7bNVTIycfs58HFp-4JEst2zwErHzZV-rWP_ILUulfVtowGbhqoIpvN856FoZJ-PbZy_G02sW0RvgzdjcXk2KIPEZbKAFghKVdzkVRj8IBV9TcD7yYiT-3UjgQfc-CRnu7p9ycVbc2LazqF_f1ZWqpKME0m0wcRkcc2Z0rKvq8KDEPLvhfFOzROSUcCCv-bVAHTZp14o-Cq65HZrIzu2qp8oj7ly2pJLlIYH4ESLO3T2W6elFFcKfTs9MKE64by7PGvThUjMMZhsIQwsUIM8wZhqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=EvGWCf5WPN2AmbJUwEyVRgjXJvRarEzmNPQSAWgPkLgs9k-GOlFkwPwqwBg80oxmJtafnk7biG8Zc7zI8diEYM3Zj2_gmoABa26EHwXxrz6xezD7GpGQHUm8tCqlrs4WYxUL8wvCy6VZQbUj-faIvEpVtqZdvpKIV3spDRGIWyujqZKfD2sqD7JBZCEjfGFWxO2-MySuOYtjCQVM2ZgB9ro9GCQFpmS-3bnoavqBedRsDYZsR91tKhipNZA-r90KnxfqRpdz40QOPgCk3eoBe0L-8XojdlHZCKCmFlcPj9HVj78AHIFJy_CfVR00n9M84YHT4Gz72dyDchhKVBAhDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=EvGWCf5WPN2AmbJUwEyVRgjXJvRarEzmNPQSAWgPkLgs9k-GOlFkwPwqwBg80oxmJtafnk7biG8Zc7zI8diEYM3Zj2_gmoABa26EHwXxrz6xezD7GpGQHUm8tCqlrs4WYxUL8wvCy6VZQbUj-faIvEpVtqZdvpKIV3spDRGIWyujqZKfD2sqD7JBZCEjfGFWxO2-MySuOYtjCQVM2ZgB9ro9GCQFpmS-3bnoavqBedRsDYZsR91tKhipNZA-r90KnxfqRpdz40QOPgCk3eoBe0L-8XojdlHZCKCmFlcPj9HVj78AHIFJy_CfVR00n9M84YHT4Gz72dyDchhKVBAhDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=bF2YiUbjTtUd6Byzym0UQDwTXGwQtM_irvOOIeniKp1kSTR4xFPviknZPgfx52UbBYjmoXLgTH2Vu4lPYZ9rPMLbWyQPFw1FiLUZ8FaZOGqOpzahpTWZHWk3_uTAG1T22M1WgYXWc0zGe4z0u6fWvFd4ho0t_bBHfQcdxUcvOc7_IEFeiMrSQLnsiWeqQUNN0WFutPiaZUeKei2JjtUNARJD4VJ1voqcMBkI00n0-rL8XqaXh2c5aUfGk9TEVZElAnkMfnRqJfWrSJXA40HKn_bEkiCA3EBkY_9dtWoxvi1szU2lggddh4Jo_j_3c5DNJsxI6dVU8zsWgwo2wNMJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=bF2YiUbjTtUd6Byzym0UQDwTXGwQtM_irvOOIeniKp1kSTR4xFPviknZPgfx52UbBYjmoXLgTH2Vu4lPYZ9rPMLbWyQPFw1FiLUZ8FaZOGqOpzahpTWZHWk3_uTAG1T22M1WgYXWc0zGe4z0u6fWvFd4ho0t_bBHfQcdxUcvOc7_IEFeiMrSQLnsiWeqQUNN0WFutPiaZUeKei2JjtUNARJD4VJ1voqcMBkI00n0-rL8XqaXh2c5aUfGk9TEVZElAnkMfnRqJfWrSJXA40HKn_bEkiCA3EBkY_9dtWoxvi1szU2lggddh4Jo_j_3c5DNJsxI6dVU8zsWgwo2wNMJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=CxK6bP868PuLj6A8ZaVCVD7J1WlrUU55BfT_6dzVUf9S-BW3z_DCzkHoN6sWZ_t04JcLPWRO43ErdvcTIkE5hi9MwwQWgufvz-AJdohxx7wfIdGKF5ihbbe2vnirtyykqh1AD5eljC3-Ya1fYjmJ6TRagBBH6qWbrmfMGzJj9B-g-3pNwtHJ3kkE-ohGeEqtR8m9-qZOr_bPkq-XkwClYYXQI5MeWrfrpVXJzFcVlU1pXC2wcHjmuSJFeg4ArNqmzpQoZzfsZmFOLy1dXJt5PlggyWgnvczDSInvq_6fa86IRC80eBE7bte_cleBgiY15W9rK6zCFwRMIhQ0FeR0fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=CxK6bP868PuLj6A8ZaVCVD7J1WlrUU55BfT_6dzVUf9S-BW3z_DCzkHoN6sWZ_t04JcLPWRO43ErdvcTIkE5hi9MwwQWgufvz-AJdohxx7wfIdGKF5ihbbe2vnirtyykqh1AD5eljC3-Ya1fYjmJ6TRagBBH6qWbrmfMGzJj9B-g-3pNwtHJ3kkE-ohGeEqtR8m9-qZOr_bPkq-XkwClYYXQI5MeWrfrpVXJzFcVlU1pXC2wcHjmuSJFeg4ArNqmzpQoZzfsZmFOLy1dXJt5PlggyWgnvczDSInvq_6fa86IRC80eBE7bte_cleBgiY15W9rK6zCFwRMIhQ0FeR0fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGbhhRk_5nu5xmYutzakbt4OEZiG-UfdFH8-dTLEG83ib6sVr5G6Xpy2JtfoCcLSa_Ra0EYYm341YgQWdV2NMheuERXLhsAZ8FW6GM-S9QwgSUJm6ogS1XSlPNUwhxQuHiobu2mgxfthVe5l_MJEEYo_A0eDekV6QNYKgW66AXvjQkCRfMpDHXDRrrjCTHYx3HQlBgNciXCa615gw52HpeSb6iL5RZnaIWRkbm668KQj49eDAac_YV4PGOHgEpFQfEJA5gIg68xH4Zb16fuvoIZaB4rQbw8qhOgpP1ePdEC1V797O81QQvQUATmSXlnLBsIRHXVYRiGNiVP1dUtbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjAxCqgsnW048f2bLMeJ1NlI4GTPCnmqHgEaicdMWZbD1FTkHm_oDnLxAjh97f8ZWcSyGkJ_YMEU8edhBTvHnOk7_rc5El4XB1-TXWYStv_qE9wKdvptUEVC9C9HQGi73bxsZ5-QbaPg1BdleigGX9bhF_qm5sbAn77u5ZqZBu_kytVWm7oHxr1PE2fGprSsqB-PIDbPOw4f2q-NZ3eC67hHxqXaZ634DdLVm7S7QjRur1an5sUSsiFc9a0QbhSr80WivEiA0LzoDNEl8JFcmMJ28O2LPQ2aTcBkL_tS7PjvgJAK0gsoOV5X8HfV3md3Mg6-3o_8Knv4Qv9ma4wwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=eKznOCYQp_bocquEroEq86nZYSrbrqIZ5ocvGGSAws31i3_x43y3SP00094nSt691L5HMr-45qexfwient7ZnFLPfUHFOfbD3BfMznK_LRuz5a8Wwl_9QL0AWpBc7QCrW-veWQwZZB2YlY-Dn6PZvweDf9LDZvi96BkXpYwmR5tP0D3QgKa5wC0fKdssu_xv_mqyJAqRrRajJ3ODid9pVG6wLt_vP5b7N0UXZe_DPkFvkKKvSS5YalYI6vfF4IRQMB0U8xPpltXosx7ufr8GNAM7aazeOc-ky2Rhvh10VpF8P_6RlNnHW2eQ6Gu19viLofv0G_5ukduJBCQe-MUQzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=eKznOCYQp_bocquEroEq86nZYSrbrqIZ5ocvGGSAws31i3_x43y3SP00094nSt691L5HMr-45qexfwient7ZnFLPfUHFOfbD3BfMznK_LRuz5a8Wwl_9QL0AWpBc7QCrW-veWQwZZB2YlY-Dn6PZvweDf9LDZvi96BkXpYwmR5tP0D3QgKa5wC0fKdssu_xv_mqyJAqRrRajJ3ODid9pVG6wLt_vP5b7N0UXZe_DPkFvkKKvSS5YalYI6vfF4IRQMB0U8xPpltXosx7ufr8GNAM7aazeOc-ky2Rhvh10VpF8P_6RlNnHW2eQ6Gu19viLofv0G_5ukduJBCQe-MUQzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0hgw9fiAK0qJBH_AkWtGFT29sHVCcbWbzpR5GFGWoeDBCIa4zbYxRyalOdZ9O-mSfnJ_sS7OJlZ2X59z_MPN4gDTrb7qNG5V8jjszzfgZ2ljH2u6DlD6JHtfs_p8JLtt7m2RRw4_w5-fGUVzDXyeZ1TTdHiGX4k1swP0un7DBvk9WoZU4OhQyP9mnGZ_fdVe43QW50OpMhkTyw5HIW6OKsk6G62nBP8uxYKi_KdQTXquZzk6hYAX79P6oW14b4Z1KiM94w9cVKAtcXDRt09FSFvCehB4eXRuoWIGjYS0c7tAy23O7CnGaNn_HD3TBMWHlZbWzMEDbxiPNv3iHBgSZfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0hgw9fiAK0qJBH_AkWtGFT29sHVCcbWbzpR5GFGWoeDBCIa4zbYxRyalOdZ9O-mSfnJ_sS7OJlZ2X59z_MPN4gDTrb7qNG5V8jjszzfgZ2ljH2u6DlD6JHtfs_p8JLtt7m2RRw4_w5-fGUVzDXyeZ1TTdHiGX4k1swP0un7DBvk9WoZU4OhQyP9mnGZ_fdVe43QW50OpMhkTyw5HIW6OKsk6G62nBP8uxYKi_KdQTXquZzk6hYAX79P6oW14b4Z1KiM94w9cVKAtcXDRt09FSFvCehB4eXRuoWIGjYS0c7tAy23O7CnGaNn_HD3TBMWHlZbWzMEDbxiPNv3iHBgSZfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=pWo6Ouv7L3NPq1PWZzIWlmfHDW9fAGwdZ4sqOmWzBZXO0NnBR3m5jKiP9xdNuHxMDkakjmakiuLLN0jGesSSgsSiSzyg7P6phgdzyp4B9HMlhlCOlmFR0rnM7lYTRch8f2qGcBXh89DISrYTvadfQ8zNXbfNteHjWE537q9OkMGUPVfqN-S_twxkR7RrPSfSeVMvDsG-BGjretw4JJ1I1D5eHs-03GMEZ8ZGUAIoT9BgMenkG2ojGia_E9NeMfv0sPBxhzvnapaucNNcpXfIsAqVcXnAkmKZ4553DDU6P_zQyUpm6sEoD9h8OsL708YiZQiShkvfgkHIY_YoWr47CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=pWo6Ouv7L3NPq1PWZzIWlmfHDW9fAGwdZ4sqOmWzBZXO0NnBR3m5jKiP9xdNuHxMDkakjmakiuLLN0jGesSSgsSiSzyg7P6phgdzyp4B9HMlhlCOlmFR0rnM7lYTRch8f2qGcBXh89DISrYTvadfQ8zNXbfNteHjWE537q9OkMGUPVfqN-S_twxkR7RrPSfSeVMvDsG-BGjretw4JJ1I1D5eHs-03GMEZ8ZGUAIoT9BgMenkG2ojGia_E9NeMfv0sPBxhzvnapaucNNcpXfIsAqVcXnAkmKZ4553DDU6P_zQyUpm6sEoD9h8OsL708YiZQiShkvfgkHIY_YoWr47CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV-sXsXFFFf9qRqd5KOn2uR6C3RG4cXj40CF4k1F3uFjyu9Ihtep0B5OkcP5JD2hF3mJpbAV-wOREzWzBHDfiyIrR6OipiHkKz2f4wambKakeeygokn5a1CJuOn-bz8no-xFWoQx5sJurhkXvRwwSK-NEu5QG-tHSIQwsIDVqNrPzS3OIJ7veqxzG8yq2pR4CkL1tk2PHCuNrELRVbjroI1uaV2LT7tD-uEe25tbUHKAVnuaK_BcQ8Eu3-e--Mu8HPEOexWyDRv6_89YkqYYuHxJ4-uD00YeKuOh9zXaPKSo97GBXx4LvF4zZq0PF595F4H9ZvOJOkNF5rSiTumu6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=gdLVsKSdWVeTPYE_Rdjr0skwM3OZntNdxpYUAODHMSvgDBh5-yPeMsUfNhjCSNaX67-b39RDZW1h3_FljmKbv5GXW9EgxKZPJSJoAtmIPpi2hA7y-N2FzFItPS5cmjyiT5hpYNmZUeAKvJZqUpwRYvqzsq8Mo5VJ6k0u_i8NqmjcI86aPDm0AfsIO7ycnUIeWpi6Q3KXmsd28JpMJwMw7wQxcZF03e4y8qPODltFpatTwxTzVecLOjLnSQ1VbXCubsRJVQDD5j4Z6VeuoOoCKKc7cOfc2NNEsnj6PTJnymOJjNksd5cFQaTBYAYXwSeIFlm3ap7TbZxduv9jEabILQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=gdLVsKSdWVeTPYE_Rdjr0skwM3OZntNdxpYUAODHMSvgDBh5-yPeMsUfNhjCSNaX67-b39RDZW1h3_FljmKbv5GXW9EgxKZPJSJoAtmIPpi2hA7y-N2FzFItPS5cmjyiT5hpYNmZUeAKvJZqUpwRYvqzsq8Mo5VJ6k0u_i8NqmjcI86aPDm0AfsIO7ycnUIeWpi6Q3KXmsd28JpMJwMw7wQxcZF03e4y8qPODltFpatTwxTzVecLOjLnSQ1VbXCubsRJVQDD5j4Z6VeuoOoCKKc7cOfc2NNEsnj6PTJnymOJjNksd5cFQaTBYAYXwSeIFlm3ap7TbZxduv9jEabILQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=IlpsD5-ZH1IqX4k795WUDHAvJ4BsnQksYfUn-WJOMLoJ3lP-D_8uTvi297UQiJ8utGBiBpLxWGt44RVRB4mR4tX5vzQEDdTGUz-jDRp-DLZCoUwcCEn5TyP2Yk0zY87w8X92_EzDrZsRqp2-l0ggBhCvoMVIuXqYQipm7MaEqShstwHUPOyAa2ddkVm7mNWsi_pnycmep3ORaQEZFtfl7RrxCALW_LAZ3CFd3Ui4NwSgV5b_VTTSQODstSUwwRcDW22N7CVBxOmDnKg1W3F6UtfBNcrnVNHbccGV-vRruIFJEvaucW7c7RcXMsbHTrDRu9G7ZSONvEHsFMzmLIq1kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=IlpsD5-ZH1IqX4k795WUDHAvJ4BsnQksYfUn-WJOMLoJ3lP-D_8uTvi297UQiJ8utGBiBpLxWGt44RVRB4mR4tX5vzQEDdTGUz-jDRp-DLZCoUwcCEn5TyP2Yk0zY87w8X92_EzDrZsRqp2-l0ggBhCvoMVIuXqYQipm7MaEqShstwHUPOyAa2ddkVm7mNWsi_pnycmep3ORaQEZFtfl7RrxCALW_LAZ3CFd3Ui4NwSgV5b_VTTSQODstSUwwRcDW22N7CVBxOmDnKg1W3F6UtfBNcrnVNHbccGV-vRruIFJEvaucW7c7RcXMsbHTrDRu9G7ZSONvEHsFMzmLIq1kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=QTpTQifRD7McMZx9RvjwoOELPAcTBIm4--6soHPwi7PL__TEW-jAbRs0diX9d7oFlHIsGRIpKG1Pis20H5FTwaiGEMlOP8dzluT7E5XuucgWPrzdt1u999Ay7wXXLJboLC3ceR50kgQ7HZ_oeUUiGpVl8UCiUp9TZs5RRtnyzNhc9ICN4VZdunKzX1LM7-xw3WWefMDR9yQP5fxEfZ_l2nsPVXqQctJ_SWPQCLquhoXN_aezr-tBctI81AOL3MSVqt3UBEldHbWx7VMDs7l_WAZ0PoKfdqLPMAXeYVbGbszfBn40BU0ph5QoSSEC0WW-bdA27sd64-EPtRv6Jidp1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=QTpTQifRD7McMZx9RvjwoOELPAcTBIm4--6soHPwi7PL__TEW-jAbRs0diX9d7oFlHIsGRIpKG1Pis20H5FTwaiGEMlOP8dzluT7E5XuucgWPrzdt1u999Ay7wXXLJboLC3ceR50kgQ7HZ_oeUUiGpVl8UCiUp9TZs5RRtnyzNhc9ICN4VZdunKzX1LM7-xw3WWefMDR9yQP5fxEfZ_l2nsPVXqQctJ_SWPQCLquhoXN_aezr-tBctI81AOL3MSVqt3UBEldHbWx7VMDs7l_WAZ0PoKfdqLPMAXeYVbGbszfBn40BU0ph5QoSSEC0WW-bdA27sd64-EPtRv6Jidp1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=veobnM8Kj4VdkSiTOTsBZxm_Wy2vxYUVNfq-6D44lNV5wclRdDA1j9lsYJqJCF3uvMuwYhk21rE9HJflH6FL6RXQ-gntdcj885r23yCKuJIyDW8iTnaaw_4Ev5ioYf27qeR5xolceekp1LHox_y0LlvDhFzEb7IqZFAEy1GIUoHa_40ryeGB_HE-jk3CGOV7GgTZJJ3Bwzen9T3RYabTaM2E3ISw2UiJg7Cdzs5rRoyHuTZDkZrNDbK_Ju7Z-ZAB3a8qjU1Se8yLAKqgRJUFSYhGCBxDmf3wV6y1Q-fWripH8Lf8QLhKCesKxJigf326xwhXrJfctQTXVnvgvnjv5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=veobnM8Kj4VdkSiTOTsBZxm_Wy2vxYUVNfq-6D44lNV5wclRdDA1j9lsYJqJCF3uvMuwYhk21rE9HJflH6FL6RXQ-gntdcj885r23yCKuJIyDW8iTnaaw_4Ev5ioYf27qeR5xolceekp1LHox_y0LlvDhFzEb7IqZFAEy1GIUoHa_40ryeGB_HE-jk3CGOV7GgTZJJ3Bwzen9T3RYabTaM2E3ISw2UiJg7Cdzs5rRoyHuTZDkZrNDbK_Ju7Z-ZAB3a8qjU1Se8yLAKqgRJUFSYhGCBxDmf3wV6y1Q-fWripH8Lf8QLhKCesKxJigf326xwhXrJfctQTXVnvgvnjv5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brYhD978gCGn7QtGZfp6ZfziLfRod005f0kpgNttbVW7o-b7D7cre60bEW059y42u_wVIeEnJ2B8uAL3sK8rImIa_DEcgsXU1VCBpYhQhhfJPmXP5pYh_fSQ_y2cW-QDsMRbcHJWw8K3gqOkzQ-yocm2WWD1mWrJxfsFvUgX70N_unE9F10wU0mqFWEgRTjS013lHD1_9JV8fm_vF34V5jWZdB2tQT2mjSPUIOIkTBY0XhW5vTVB3zoru5OTla47XTt0w8Xgvdy5bdRzoKIOhIPD9O0GW26fi05utVw_HsO2Dk6X9a1vKuY40SD9bivEoFxqCu4OSyGxF-uvbvmClg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=rnM2lbg4PBoIRRuGrFTiUxWrfYqcoWbywYvi4-jf8QY61t0I2wVM_s6SrpNUbhqQ34rwJ5mahsEOD5F6_-GabltTjpc35QQMnKIJlbk-_nSqIPl4njvxqezZDk3_SURw2WZoWw1tD8LMLez5BHncjUcOaSTBWf7EH_H6hA9Mi9ITsMNsKjM0kSSBWCSZIjEkdghYX3NZO-u4T1DtCE4Y9TxXynwwe_htviw0tBgPiwogxGmvol7movPcA7BeCQ8csaD1ibFhBSCzqveJwEBhhiZd3nPev1_QqpZFfHS8oeM1I1D75YKIdwO7tPeobsBE9KDlpC4RRCF3yNCZHFznlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=rnM2lbg4PBoIRRuGrFTiUxWrfYqcoWbywYvi4-jf8QY61t0I2wVM_s6SrpNUbhqQ34rwJ5mahsEOD5F6_-GabltTjpc35QQMnKIJlbk-_nSqIPl4njvxqezZDk3_SURw2WZoWw1tD8LMLez5BHncjUcOaSTBWf7EH_H6hA9Mi9ITsMNsKjM0kSSBWCSZIjEkdghYX3NZO-u4T1DtCE4Y9TxXynwwe_htviw0tBgPiwogxGmvol7movPcA7BeCQ8csaD1ibFhBSCzqveJwEBhhiZd3nPev1_QqpZFfHS8oeM1I1D75YKIdwO7tPeobsBE9KDlpC4RRCF3yNCZHFznlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iWRxzJRf24MfmnVknUOlU7EBQ27yG6ddRH70m5OAgXzikMGP-9-sPSPeb1xCkRcNBdbZ6pU8LyN1zfrIHfMceAqmoFdP6QS1XfB_h3EKxmIuEOKS-dYO-RrCYGrWGBQju7h4f-0AAnIoCjyj1N2XcV4IA5yJ1RfX5khyf4cfni5v9eJFpLTTv17iZJzN4ftFsNN2NEfaGxjF4AfiXXuMASRy4ZMLqGh17ybYKG_j_63Mce4eBEXYMyVfco6xQR23b8zed5o9iaCK-10SbBjAcxMiy75c8W814CC-HcybqR3Rwdp6g2b5guRNM1twDOUopHsXzjz12e0ZJOhKRcjp_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iWRxzJRf24MfmnVknUOlU7EBQ27yG6ddRH70m5OAgXzikMGP-9-sPSPeb1xCkRcNBdbZ6pU8LyN1zfrIHfMceAqmoFdP6QS1XfB_h3EKxmIuEOKS-dYO-RrCYGrWGBQju7h4f-0AAnIoCjyj1N2XcV4IA5yJ1RfX5khyf4cfni5v9eJFpLTTv17iZJzN4ftFsNN2NEfaGxjF4AfiXXuMASRy4ZMLqGh17ybYKG_j_63Mce4eBEXYMyVfco6xQR23b8zed5o9iaCK-10SbBjAcxMiy75c8W814CC-HcybqR3Rwdp6g2b5guRNM1twDOUopHsXzjz12e0ZJOhKRcjp_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7DLmciksk97fjn_aDy90cWDz_LieyRvIAtMirCByQBUXEzS1YocmLAyEFHrCbMTHoaKjVna_gA3iQuk52VFe4A9k3P44NaiizIlLVQeqccP2Gv1xyT5HAs5GtSAJ8pSEz3NxT44fYH5y3tOYJUJTzayRsioCkfEAVhbrmd9EmHW_BOLG948Pok6Nv1ofhmV1-zYXyZVwux9QhiAE5Bk1OeZpDsFRPttigub4PoblkLblzf046GCNOUgNrJnmikxiZIUImeTUdaTI8onZW6KTRHnnMs4Wqf9CO6hVTWyF_fsECD-FBC4Ki_73FXXgjwsG1idK_M3CGz546yB0ELX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=TCSdoujB-PmuKLLaq7vTAu3c3z4ycQCvZn-JVjWJSVn2vEcv9QAjhyqALws0kyy4qwxXRGuRcR6z2bNSS0N5056MRtQ4lU0EAIwBWPuVRobZ4Hgee3e2kpbWDbQULR-bqmAwpHgL7iD4-gBMAkS5dWIphs9lKeeBvrMC3tqphwHZwxDeqBN-URsPqFV-81Dcx72wXG-Kvsk8AmP7Uhdy-LQM6qhEgvHyY9zYZxxFbSill6_Y4b1iT2GpzWy1KHqqNmX4plW9rfeMdSZGhddO5mPRk7bCrCOWmcvtBrWDp6YqbyUtrJnV7_h-QntzlNFBCUrEY7dhc3sXY8RO5ibbZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=TCSdoujB-PmuKLLaq7vTAu3c3z4ycQCvZn-JVjWJSVn2vEcv9QAjhyqALws0kyy4qwxXRGuRcR6z2bNSS0N5056MRtQ4lU0EAIwBWPuVRobZ4Hgee3e2kpbWDbQULR-bqmAwpHgL7iD4-gBMAkS5dWIphs9lKeeBvrMC3tqphwHZwxDeqBN-URsPqFV-81Dcx72wXG-Kvsk8AmP7Uhdy-LQM6qhEgvHyY9zYZxxFbSill6_Y4b1iT2GpzWy1KHqqNmX4plW9rfeMdSZGhddO5mPRk7bCrCOWmcvtBrWDp6YqbyUtrJnV7_h-QntzlNFBCUrEY7dhc3sXY8RO5ibbZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=GqccwICCkLW8LzDi213PTJQpYDPf9HAjUJHZtOHkZaMXeD8fjJhekyZTmppVoajdLhmXh5P78YTPxYSVeJP59cWO-mUPoz1uU30izWWT_JBC1n1Aq6SB_Ru2ohTsjUO14SBVUsj7u2f8qudbesabZ2nd8gSIHyMlZL64cllS1YMfytRwtbSvlFjY31BSyq-Ezwz-yRT4NAlFOfGRgJufbS2dEWamiOy54NOxgUInJTgjAumCHTeW9qOff3BCmD-eremT1piLgkyA8iSDwwUIlBkwGDTis14SJOIO4it2gvQd3o4jCiBpOdUWkBPsDd7GqoOmC5CdZMQOZWjfC2VphQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=GqccwICCkLW8LzDi213PTJQpYDPf9HAjUJHZtOHkZaMXeD8fjJhekyZTmppVoajdLhmXh5P78YTPxYSVeJP59cWO-mUPoz1uU30izWWT_JBC1n1Aq6SB_Ru2ohTsjUO14SBVUsj7u2f8qudbesabZ2nd8gSIHyMlZL64cllS1YMfytRwtbSvlFjY31BSyq-Ezwz-yRT4NAlFOfGRgJufbS2dEWamiOy54NOxgUInJTgjAumCHTeW9qOff3BCmD-eremT1piLgkyA8iSDwwUIlBkwGDTis14SJOIO4it2gvQd3o4jCiBpOdUWkBPsDd7GqoOmC5CdZMQOZWjfC2VphQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=da4m4-yc5fUh63_yNOtUPUt7y8GH0nkliPJe03tbZyX14U4Z_fn21XonSsqTmSrD2HzfPW7O8Os8dS2l7jtFyfNQVxw32Ba8RVEV6VGd3saMrxs1lzeILXNpTQr50F6lAbvhvo5E3KO65IndlqCfCs7zrF49qVnTWnekXwpgfZm99ZGVxaVgMBvzHPl-1eGQg86OhaHhx3qcho_q_9xnWFRb3WgR_lz_GZIyqzAFTZAGwmEnY9l5TabbznbQpnNYM0iTxE-wjcc5gvPkDy2LdzFG6VJS2DN1BjfbUvCdFSbUCHoOCKGCA07PuZmE5n3iG0-GdnJYd6aaFuRjnFJQMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=da4m4-yc5fUh63_yNOtUPUt7y8GH0nkliPJe03tbZyX14U4Z_fn21XonSsqTmSrD2HzfPW7O8Os8dS2l7jtFyfNQVxw32Ba8RVEV6VGd3saMrxs1lzeILXNpTQr50F6lAbvhvo5E3KO65IndlqCfCs7zrF49qVnTWnekXwpgfZm99ZGVxaVgMBvzHPl-1eGQg86OhaHhx3qcho_q_9xnWFRb3WgR_lz_GZIyqzAFTZAGwmEnY9l5TabbznbQpnNYM0iTxE-wjcc5gvPkDy2LdzFG6VJS2DN1BjfbUvCdFSbUCHoOCKGCA07PuZmE5n3iG0-GdnJYd6aaFuRjnFJQMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TO_IwlsqF9h0CRvbhsyepxINUWZpfICe2uD85Dwzl3vxvJVL9rpGdLHZYrDjnJJ9a1PCI3WK3xoSbTcMoj7z9QI0XWeroWURJybQ-mn9FsAgx2Vh37neUY1Bhb5xzzTULfil_htM_XotZOAJjyRzELIHyDdkZakwUcJ4is68Vte0_NFMVfAnL1FoCz_qa6J_ksMT1POsbEAehOeomqIVAaqqmOFAjNiChEIBha4aaj6jx8OlybG5kluYPy2eoWvLwyIeqpcnDq7zVTv-YpcKTC4hF5L5KtKpqka_PMczlvo9YkJ5iW56lGGlX25rnFNejrIUZdinZ5qFfkz-PmEjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hO0iWXm-aO8H5w3MVv1BAU4UAUunB-Ae03bXiqjAbrhBzOlX5FXSFBnTKINGm-xDiD6bMLRjueR6qTLVtu4_KdC1Ij1Y_tFv7ph-QjDg77O3ZPIlF4cq1XjUp4n9FYz3mg07gEPqO4uEsgmLyBtIf-9XujPbRV2SMCVxaZlITYfW5Ez5TqojGOTGJwpiIWoeOzXaLBox-Kx3OkCHSC_RuQIxtu3ASCZwMgi5yLDpSliYJjUDvNl4Fb2w_MnnvTjG-R9Ey0m06xhUy3Za-JJ6WAGW-tWRCLkuSlxaP1PCIKyZxK8I9WIyoYQIqPyR8qlz53JdjrZMddcceA1s4QrMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMEq9vzgAQQIJLhKFkHB2c9KlfIuD5VnkUJ77FDIu8MOVFA_9hg52zFBI32s3tLPPl1_OQ7Aq12Y9YtlZXl2C4fNi1-5wXL5XiwgyWhoioZc9Ywb-W-QkMV61lMWMcCIudF7pMmpQnfm2j4ohjtQHdSn22_aQQvQWua_BQ_kkGQSXIY-P8M1lrQE2fwdpHPQQ4JfUd7GjsppHAS8vBMQ5oDD1pb8a7ld0ffagGTGFEaSwnu0FTonpQU0jpBU57EeO-MgVR-TQZWfp-r_mJuIOWpYJkqJWTA3MjFfmotB20Z8XWWaf1ZznnX-VvF2HRd9AksK0eAdwq6Ce9kxV9SAeg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=BH2z1VuXRbzn-ciRJ7g12t1Ux6rSARP-MKFxAUwx_6cVj0jNy39dtg-tdU6LZnuiOjgumHwyeUPud_peOeqXJAuNoJ3WuktZ5aTjcqjzXxXGBF4gKBm9r0knSHOIT--SVItn4k4tzRzJx4_HxL_gwTmVe5dJEBk7CHnfh8qGiFjhu4COhlAGHYnvvgOLEOHVjupVp629EH3h5Ztae30LD3rob0uMvPPZ3D13Xan3bC7_6_-7JutjTEQxjdq9XNm6yakPMi6HGGZhu2C8PovrwcK2VkzcZEueI4gf3N7MwK0k88v20BULmB3iR_zWXhEEbkOEAq716-m3YyV1C-wXeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=BH2z1VuXRbzn-ciRJ7g12t1Ux6rSARP-MKFxAUwx_6cVj0jNy39dtg-tdU6LZnuiOjgumHwyeUPud_peOeqXJAuNoJ3WuktZ5aTjcqjzXxXGBF4gKBm9r0knSHOIT--SVItn4k4tzRzJx4_HxL_gwTmVe5dJEBk7CHnfh8qGiFjhu4COhlAGHYnvvgOLEOHVjupVp629EH3h5Ztae30LD3rob0uMvPPZ3D13Xan3bC7_6_-7JutjTEQxjdq9XNm6yakPMi6HGGZhu2C8PovrwcK2VkzcZEueI4gf3N7MwK0k88v20BULmB3iR_zWXhEEbkOEAq716-m3YyV1C-wXeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaV8lwJ7wqgBBKMPcinuW-EuqG9l6_4PlvJrAJm_v2iEq0EL40qugBnpvelpTd_5-cnBZnZGgsDPcsYHWDdKFNO1llTmMnOHFJJ88f2ewjwe9LsvDvT-Et9g9sGo1zKeS6tIKkECGSuiWIdApUtokVgG99dEN5YH-Qb_dh1Eswg07qnxudhodGK2iB7YZof0Bw6izo2N9MEvkJdGBperIBK2C2cmGRq4wlXES1kw7xOlnkVDs7FAiAOd5Igp8mir_VKuSs-R-jp_BzPaaJ-XZBCpMgPWpxy0ePpjZYXCSEav4uutj1ntCfYOCLfcw73BEeOCUjQvKpA4zJx1E3KWRT0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaV8lwJ7wqgBBKMPcinuW-EuqG9l6_4PlvJrAJm_v2iEq0EL40qugBnpvelpTd_5-cnBZnZGgsDPcsYHWDdKFNO1llTmMnOHFJJ88f2ewjwe9LsvDvT-Et9g9sGo1zKeS6tIKkECGSuiWIdApUtokVgG99dEN5YH-Qb_dh1Eswg07qnxudhodGK2iB7YZof0Bw6izo2N9MEvkJdGBperIBK2C2cmGRq4wlXES1kw7xOlnkVDs7FAiAOd5Igp8mir_VKuSs-R-jp_BzPaaJ-XZBCpMgPWpxy0ePpjZYXCSEav4uutj1ntCfYOCLfcw73BEeOCUjQvKpA4zJx1E3KWRT0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=IFfOMAP5ESlIXt8a-EPpakyl92ZW682TrX5Lo1C2hwPXIN_S6_rogxxYACQV_7BtVXe2tPYaqduHK5nEHPIc3VSOzskd-dVXW5qo6UY26aja6RR4uv184jESI_14AV-wjAm1Ug2W_fDd15gRL94RXNUNkIeLDirHvGLnF1ujo2A5xfg8cJjS5XPwjywSHGqSs2KzjUhOWM3GkVBObYuVV1qoEIvoHdeIYlQDS3by8svr7y2YGBg99KURSoay8qjxKo87fogp3G8yGQScSTjWg4uvYy2H84SQTKReT97TbTzLpxIK2N-hcgEUAuZPv-_MDzAdCeXgAhaRzazQqmcxIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=IFfOMAP5ESlIXt8a-EPpakyl92ZW682TrX5Lo1C2hwPXIN_S6_rogxxYACQV_7BtVXe2tPYaqduHK5nEHPIc3VSOzskd-dVXW5qo6UY26aja6RR4uv184jESI_14AV-wjAm1Ug2W_fDd15gRL94RXNUNkIeLDirHvGLnF1ujo2A5xfg8cJjS5XPwjywSHGqSs2KzjUhOWM3GkVBObYuVV1qoEIvoHdeIYlQDS3by8svr7y2YGBg99KURSoay8qjxKo87fogp3G8yGQScSTjWg4uvYy2H84SQTKReT97TbTzLpxIK2N-hcgEUAuZPv-_MDzAdCeXgAhaRzazQqmcxIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqjgQF5ce_hV_1-wduakEh4nyEe7yuAwCHGkEt5GAOmc9qZemo2_SJM2e_OCH-nkr3rxYTW8IbVxv9BaxZ7i0WGBATmo3syZxHYTiabllHssSPzdoUCh3JqKBpkxUOZXX3gMQGEGeYTFK9pv7WtgqoNgL_kb_-f0pQurh8tnAexBKBvfqHC5DwLn2vN5ByWoSE0X3i6gLZnNl5qiU5YhgNKZyd4P1z0EcOW4kd-FnomWYGlu0FVxWGQpv-CgEznLIt1Zamvw6o3eYJ6BqRL3YwBpjKW8VGg7mPoBUT_WwSzAHS_2YnAdzbNdGdT_TwzNtzCqBWGvtN-wvYxIf97cSw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTrHqXFy_xlrnqBGbvSRtE02FrJuRGaOoObH10QC_fRl6UzeDc2KSPf8ogGKmc9mnR-yiYKQ71rD4fx6TV7JSzAQhjaVz1LuE9JwypjF-m8x959ist_YyiV7vVB30URTOJNBE2ZJbmMQ88zUflKfDNO8qOxycqm-jWxQvqIJ68GMhDq-GZ_nYXC-2Cl10fRtEYGExOIzYRhQGiNAXEgEdP0lzXUs96ehjwS_y0dMTsaFuxS4fV8GXqvpYZLbtWuNSTWdeblZuVB9nzAkWH6RimiPilSf8B9pAr7UPwk3BXeYh54p1EBBQg4BnjZ28cYbKg04Egmusk4wzZEfuAI0ueRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTrHqXFy_xlrnqBGbvSRtE02FrJuRGaOoObH10QC_fRl6UzeDc2KSPf8ogGKmc9mnR-yiYKQ71rD4fx6TV7JSzAQhjaVz1LuE9JwypjF-m8x959ist_YyiV7vVB30URTOJNBE2ZJbmMQ88zUflKfDNO8qOxycqm-jWxQvqIJ68GMhDq-GZ_nYXC-2Cl10fRtEYGExOIzYRhQGiNAXEgEdP0lzXUs96ehjwS_y0dMTsaFuxS4fV8GXqvpYZLbtWuNSTWdeblZuVB9nzAkWH6RimiPilSf8B9pAr7UPwk3BXeYh54p1EBBQg4BnjZ28cYbKg04Egmusk4wzZEfuAI0ueRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDEoyV8wMegCivWdS7f3I0mzcuwOSvivWBYRx_USdIcsypJS-k5bMyQ0oogsoQG8fspmQHcqy3DFDcNu1Dkel0a86dvfrwOXBqnZWfPqD6DFKLiDGBEIV_ZcWWjzuwepmXJGLBrkHjqT99fnpSPWQn6T4MaOJU-k0ImNXl-fH9jcOG0UrPAH_Qe8xPAEcLZVtm6bHCAYPvmLe2L2eSp_OSxpdegW5OODDVnvTuZNfK_COqDYhUwcXWkDEAeUZ4a1zLk_gBXtzjyRrKW_ztR-QRwDeg1_wdaIV1Pc_HW1KdpWmWHjgdwU6ZmBQxtX8lGUlnycToZ-cqGgKduJEs_pnQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=IP2VHhyGoqCLecx4gkzVEAelQPYumYNxBraLL5JWoNjlkhL8IaJ1afEt-8uQ8NRemDeG0N8gySHtg9RCfIoKh85oxP0TGK-5fOaNga4HH0dhZO4GwskuJM3Eg-VkIsFeZDvpkZIdOqTlqYp1d-pcI74SbgL4x1N6xHLmKOA4eW1KqqQepxkwmRi8qtGy5Z8iGXzDLDmrHkx-ykFRFeXak6vtLpYYrdwjl5PUkmfs28IEqHcmyMgF7hdICB13ndebpsTpjD8aojpmZnBkU11F7cEDrKC0rTxqp44r8UvldHb6bF98lICBkElShu4hV63YIXzLgsCMYVJ4iYllMXmrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=IP2VHhyGoqCLecx4gkzVEAelQPYumYNxBraLL5JWoNjlkhL8IaJ1afEt-8uQ8NRemDeG0N8gySHtg9RCfIoKh85oxP0TGK-5fOaNga4HH0dhZO4GwskuJM3Eg-VkIsFeZDvpkZIdOqTlqYp1d-pcI74SbgL4x1N6xHLmKOA4eW1KqqQepxkwmRi8qtGy5Z8iGXzDLDmrHkx-ykFRFeXak6vtLpYYrdwjl5PUkmfs28IEqHcmyMgF7hdICB13ndebpsTpjD8aojpmZnBkU11F7cEDrKC0rTxqp44r8UvldHb6bF98lICBkElShu4hV63YIXzLgsCMYVJ4iYllMXmrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=teJb4gbMitJAbY2b_6J2Mx3BQ30tgY6MibgY22ZYK7KtRcGiLlBxEFIhChJw18P4K-lbST4K_nCn0EZr6cFJP4bWZXZ4ckbvmcsL8uZh1C5Xeab9lPbhyF2Zx8Ifv4zuJgBvcZDiEZO344HE8dHTmUfgX5-wKalCbyFPu5cWEFT-vJaGNVFQ9aNT-9rzQxnEw9CG1OBam7L8FoA5HycC7iM0hCUOAdlbt7zBWzJbZ3hkk5Fv8l-4Huh7D_ZXND5PXHBpRjBaegbzk8hyJTQ9-hrAc_ovHiK9if_U9dTIgSeeMI4im7nDxYOWuQyUhsNLZuPdGHtDY6OsPTTNQUdBjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=teJb4gbMitJAbY2b_6J2Mx3BQ30tgY6MibgY22ZYK7KtRcGiLlBxEFIhChJw18P4K-lbST4K_nCn0EZr6cFJP4bWZXZ4ckbvmcsL8uZh1C5Xeab9lPbhyF2Zx8Ifv4zuJgBvcZDiEZO344HE8dHTmUfgX5-wKalCbyFPu5cWEFT-vJaGNVFQ9aNT-9rzQxnEw9CG1OBam7L8FoA5HycC7iM0hCUOAdlbt7zBWzJbZ3hkk5Fv8l-4Huh7D_ZXND5PXHBpRjBaegbzk8hyJTQ9-hrAc_ovHiK9if_U9dTIgSeeMI4im7nDxYOWuQyUhsNLZuPdGHtDY6OsPTTNQUdBjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=q4pe1jSVM5iCFW9pZfhajDgM_jNcxnaJAQ5sUA1VmiW5CF5dIBRIVr4AafbXLhCtw9C8en_EEZyRCqFoF1ABeOzvtGkPzfsieMCk3VH9g86nrzIClh9fJZ59upIvhrB3-34Aw8-Lp7jSDa2CnJH7vugHX2VS_QgLJ3PlkhqqzSmFrilWhpiALND7wynDXoHM5fZ37B_qLbiEBWfQVgHfZl9ZSun7ZT_nFJrQTVJ_jKc-zj-rnQrD5TYpHQGk9s1C2f-XYUkghs0vVU_ICMK2PXWyIJbw8xwA52FuQ__e7Bo-XJJUMzTcOSPJDhic-0byTZQoZ7_SHOUWT9Hn-joPHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=q4pe1jSVM5iCFW9pZfhajDgM_jNcxnaJAQ5sUA1VmiW5CF5dIBRIVr4AafbXLhCtw9C8en_EEZyRCqFoF1ABeOzvtGkPzfsieMCk3VH9g86nrzIClh9fJZ59upIvhrB3-34Aw8-Lp7jSDa2CnJH7vugHX2VS_QgLJ3PlkhqqzSmFrilWhpiALND7wynDXoHM5fZ37B_qLbiEBWfQVgHfZl9ZSun7ZT_nFJrQTVJ_jKc-zj-rnQrD5TYpHQGk9s1C2f-XYUkghs0vVU_ICMK2PXWyIJbw8xwA52FuQ__e7Bo-XJJUMzTcOSPJDhic-0byTZQoZ7_SHOUWT9Hn-joPHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qkwt6XcMqo6kYQadQ3vdnE62-iFUeNgMGjluWFm_nR80_Tm4qYYGNq-JL3wBN9F0IEzqOWthatTPMOZOp3oMU_J_rrrLqWncU8Lc6t4zUEBb72ruwWd1DnIerSTK6-eJ626_KmTKa-nnToHCwXCEGkm_fUPb5FkmH4Jv9d9s8T98fFQun_dDPj8HugoYH0Bo69g42vwR6AKeUa0lEEO4bAdlYbNILRwRqLnEZ2iA9N2vj3nGYjiIsdl4GZHMgxgZ-_ehkOsTGdaC_NDBzwxFC435791wvqVQ6NtKgcQTlmvs5eQgYraq3WoVYaxOUyRe1S5WEY-8xmYtTsHIu7BxNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
