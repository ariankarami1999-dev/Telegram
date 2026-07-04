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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 23:57:09</div>
<hr>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dziOjx5OoNhD_-9DwbyrRpH7HIIgqiQf-louNM7RwEiviwUiQj4ftplmKgHL7PqIjB22wtTte_F3nO004BDYShcipYIwYBp5Qvvab7eUtp7Fyc-KmgZHPvC42u29jlay76yMSC21BHMXP4_Uw84FmsqiqR7BvFJljsbyms6zfJGhVmssZcLpdbKWNyt1mGxy4QgLP7Q-ZYIXeJa8Wr8JVedkGEvnfTE5vHxO83Iwd-UT8K1FvV0rlkBbT-Bs8mfJygFLgEWJeAIRx80NYhtHNwhsGZcdsyt3Hkg03kpDYMGVLX90Ymfg90aD0DD8knkaN5PEB16YH5_jXTimDFrnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=mdb77CWZXgP4AoHICMCfntNpPvDlo69W8ZChkQ3N1uXtIM299gcMKKCfsdMuYd0AxHkLbjIqZvBHH5mNZrZ-wmarmHbV69cUgpXWkgF9RGmXH6ieYJqljBzN16PvCgDlbSKsLn9SLsBTfoR_QkT-why7aMC3FJ_ix4TGSeAasoQxwNbH4qVFovKKii-bObqxAjXbgonRRypmudJkPrTcMy6_DnMRMoAGqHcrIe0aPNShndphf6w81i9uqloIQJFS-MfcxeftO1bVlyImTol1m1WdcNM0s7_hxxNzA-CxRYcp8re0r_pYIVoRcW-4O0tLVUo3euTV7bSUR5BjOoQrKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=mdb77CWZXgP4AoHICMCfntNpPvDlo69W8ZChkQ3N1uXtIM299gcMKKCfsdMuYd0AxHkLbjIqZvBHH5mNZrZ-wmarmHbV69cUgpXWkgF9RGmXH6ieYJqljBzN16PvCgDlbSKsLn9SLsBTfoR_QkT-why7aMC3FJ_ix4TGSeAasoQxwNbH4qVFovKKii-bObqxAjXbgonRRypmudJkPrTcMy6_DnMRMoAGqHcrIe0aPNShndphf6w81i9uqloIQJFS-MfcxeftO1bVlyImTol1m1WdcNM0s7_hxxNzA-CxRYcp8re0r_pYIVoRcW-4O0tLVUo3euTV7bSUR5BjOoQrKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aof7YvyXsxZH5vZf1lsp_t640seTMxi7pcbCeR2PbIswmD6TCp8im0T00JSuSd-eKRktf56GD8gxEIv-DzHpnEQwzispgTxyfLbx2zSCfPcAmbnxqrwrBk516g-Bn0jNnaJwqCx39QW4VG9nrzC4v2qrsfaqL-JM8J-gkmfZ6rHdqAvk9dcqWVOflVuUGt27W6TW39MNsQQH6cieIfjaubWCQtQZzEURuJ9b2jtTNGCbaZgjMMMQEjaS5ZJyhBXshXAA0OJrFFPMHh515eOsI30G-oSSgHAswquzlSoAVIYSN5JAtFLkT8j4lJo4bVhjrR1_PW7_RXtHHcE3wYkthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovvPTA3_pdmjYnE-hMfyd9cE3C6_j0WAdx7WL27o0yDlgyl4MKB3_-HfC3cFS7wi41A5Ftm1ykDTfC_vBpfqpJ2jPHuOATpDD-TAigXS7ilyoKeDdNogCMUhbMmGN1pFjMo2mUlIjelUF3yD4i5JFAsttlg6-GrMznzlWjA7igEHfzKUhrP_PHCRT89TKWMmojFz3W40l37KVXAZZpk0j4EUxYONoc_-WrN3B0ajMnUyvW7cBlrUvlzDthFlkxxnkcYbuJvs2tuDMN1pwqBjXx--IfVIvAg4O_HUdOHixXNVXdh4F8_sdh5JF9-h3yBWTfxcJ8Flap6KvS4o9pVeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biB9BrtoUKZnlQZ8OxbbEAxzgm9ifQ3XFrZbz1CxXcHtZUF7pQTBmP4GV07GRl0TOK4TPZuxWBL1SvrDK0PY1afeXopJYOsIRsQI-O0I5IAR7jVZi-XJ5paoSU1YZQsqt_5j8m7rg3nYTZcMO96HBlmrQ14jD0JlaZiYvtPGmZuaf7GudQivU7YTMnlFFQT0JnNsXY5LpK0fNyLyf0trhy_nmeeUN0trIlGzh3dY7ra1ocVzGRsPnJCzQfSfijvBuwR5alYMDiLn9O1UST-jU108knslJnxAmTk66iKoHojaunDL81VUzl7jANFRLyCoe3fg7WofDJS6oD9Eq3-EjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r37LBVEBAGIRIznRL_Y1UcT54vYlT-MdJ32X_Vkt8qr2XKmDEp5HahWp89hXMRpExA6zaxV5WtjTvpg9K28IEsz-H5r4KwMj6hz77iLl4djTJSsuqVPauIbU_D0ntAJw2ECUSBqCn9yNy7nvc26HrDbDIGlm8ICohheCCDwdaKxJPtMYl2RrR42XanKDY2MN4Moz9SaF-rkuCmMZZ9zs0ZbhrB8tDAGZD-snldwmcL2IEc19uOD-7u1GG9mmo7uBiA9sXWRLp1xC_CeK7vYr9kUEoujbehSims8R9gP51F4erb0c0Kxzo5ocqT7k0fLkjWieR_sSc-d1iCdzasmQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxtiABC0KbLWZWmvmqPeYSLcYXtPC2rPFzc255tihV7wcNWNVVxZ8yZL0EMz7At8sAYotz9sBn1JHn9DF2dfWmK0_lTFqDn7TYWy7GTa0yg8NAV7oHtEkBufAeRJy7dkCFm3eHGJcjjxiLUkh-lOnFJuLFQbxbx3u0J3ouOZrm34rXfM2SdpY_OGPLQ2bV5CIDroGXREWAme8WQGuF2TOyELz6EXoi1sN3q7-lLu-BbXnbuPu-mCtgVpjC0BXKZ37lJUJYioiFcRuY6jSd7z9ViGkLF63UDNsT3egK-Lhz6qsJMbod75ZU6UdehdSHOz7u9uTMETAYOJR8LadJisvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV4lkHxIUEUum7bnX6CxaY-41O93lR8yaQTZo3cyGrbtVehTG_aM1lGzZWXFlxkV-J3AVA7lRC6khp351aDDaxxBQMKsKBsq9gp06qAD3I6ckzkBXWRYab0N2igwwdjgdcT88fuf1sNjExpIQ03tjuVRzLwz-fGb-mAkgyXpfhf54Id4EJutkMT-jID86dNQ8feWG5hQnNuZeK0Xa8yW37IdB1JAiILhX8-BBq9NvvDRCzp1KWzfrLGJdsMzpv4VZMsPxXxvwgsKTHiJtldKWbw34KoFJJpD0XWo9hDM5eG1YEyB1RjWsHx18WJrSksAIGIORgzRK-GhLPMCNEhtgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGGVttTDODAbcVQsbhP2AxRD1o1D_ON5rkjUWcwkh2quNZip12dqdgTZxqHyHR2tHP48D9puHbq-r-r8thipbVx-CojpLYfdQEr5ZSRLtfhEe6C655MT1-e1ShGK0v0prfptAM39KAHf7tFpAY969I0MauQqGHwsxiZOdjR1cug_PacESG3iHX688zoJf1j2GmAbgfvOxkKBTEzn7X7BGZn1J592VwyI2Ac16Fai5qcKKojnqLoiKjk6Z6e3w50NtmzRopUM6dC1DyLAPXhfhdiPMDZbxM4lNOh8krm65qonvsfKARh2Bxq9B1aOiRplQNYXSxjKmbPvC7kLLs-URA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3iG-8ZfQ1EoHVpjsjb_9Gst-7dZGhW65DpZYIaDUMfiqOo6ukKkSlM4G3yJbgGgdAAsxy-nNbrAtUT-NkvK6pT4EhG06UWXWarX5e7oAdz73c5Xeu0RvvVstZ-P6EDMs94HGd2iFpgcair4WNEcKYfjW-c23g8o9c1QbgzwTnsn9UZE0KZws4AgOdkTMTbsdIL0TGsJknrwHYRZjkhB1GGgcMY0zWypRA5dIx3eqftjtZHvii8ADl_-j92mwx43u1f8eQZVNMMbiaMCyLoqhMCNfg2te_P6h3FrNWWEJS-2e4JvPZaIlYixP77ACnnn47y8Jd7XzYB8nKk0TGMkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCKnWhqq_8Py91Qqg8uMfqvHQ6vu_BLnS2iMrrHaHsXYTugytkHtSFfbUKDHBttkFd8qqd_DTfKF7HUesEvd3BkTtUVHK5Jp-gvvxW7OwvpYbjOtGi1G9B7pRXrW1PDflhQbG0M6ZcgwvDd0_Nyr7iA9ZFdBOULy4cHDuzMD1ibrow_YH64J3-Q7CzJECxxzNmw9LJavh3lgvWyFTkCUCZR_sugG1cPWpszlkSGWaRIDXMcVoYrotWIv5Sdquvzt2tVzw3kMrt97ZByltnkjrH5AGQSOxcaDGt63StwU0TvTKttZAwRfzEPy3FQkvTMwi0tF4VNLuK36RnEPGvxx3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8tlRp_R1F5ZtzgIh12rwHt9GxVkEWlfgEk0sMqzkFUNPw7bKYSpQ9HocX-oINWmVKjqaiLKGEVmHpbQBraKLl3tB6TuBNuYvoHPq3eXqKjf-esJ25lKqevvLN89eJf8nDhbTQNzTt_Z6It5fqYclhBNho6WHzgp_6I8Vn5OGy3wJLb6UOWLox7Sdp-U6v6AaUatgzPNZB24QYl4XS0q49UcdJkHvI800mktc6_OebtTNLWiq2wbnWodDJ6SZwHUdHE8wvU0VF7pBOAWMXWQaMPneu7dIUsvEoK0ek9E7LCl_brT1sq9R0xPQIM2Px3vfhOoreG2HZfMh1Sz3vAXsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzu8p1JpTvAu2-IyObz_3w0APyRvcsQQZVhWuoUITRlxEb9Ofvm-Sw3zGgQO9IIltsmr5efOJQ-CL2kGdJDIj5cgja8grIY4lSymZZrXi1C9_RpQ4Qkj_OZTTy3FlXMMZ7cXp5J_IXDPJUjp-5foT_CLj9cMU38Y_M7XCxHXPD_lSSYmwuWf-nra3bYTH7iM_CQeYs5JXfQacTOSKLuhDNccF26Cq76SddAxC7vsBhzWsBKzFggJ-Yu3mRCd12HLpk3sH1JpayFpavO19QNkFTX4YWGS0K2xoGQiJBOEhJsflzqvxf0YyGhwisl6H4nqkR_XBIb7-EtQD67JDiDZiQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Sar95u6VVIRxKu6MpYvS0QHIxaoSWzX9D9NZ0VJa_SPEb4GJr0GqdgLRjWvW8XOufrjFJV4-O-Nm2EOs2uQntCqbJMk4OTlzda7ovsN6xyHSOOjb7T0ZrHUF_LJybnP9ZS3t7KMW_QfHlVAFVqKrq_qbwc-lYt1S0SYwS2R-io2N-Ch4WlZG6fBmGy6eOM7guv3UlMK8l5jq2B7nI5GSThC4W744UsNZeP-J8nMBsm8A4hdSngS6Ri_7qjuoxqEByTuP1M2NtQuUnljEOFHBCvVGgf0SAvlH88AyXTAm4-BeL67Y2_TahuZHd6K-M8IGQzHpjgu3iVS970PTAXt2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Sar95u6VVIRxKu6MpYvS0QHIxaoSWzX9D9NZ0VJa_SPEb4GJr0GqdgLRjWvW8XOufrjFJV4-O-Nm2EOs2uQntCqbJMk4OTlzda7ovsN6xyHSOOjb7T0ZrHUF_LJybnP9ZS3t7KMW_QfHlVAFVqKrq_qbwc-lYt1S0SYwS2R-io2N-Ch4WlZG6fBmGy6eOM7guv3UlMK8l5jq2B7nI5GSThC4W744UsNZeP-J8nMBsm8A4hdSngS6Ri_7qjuoxqEByTuP1M2NtQuUnljEOFHBCvVGgf0SAvlH88AyXTAm4-BeL67Y2_TahuZHd6K-M8IGQzHpjgu3iVS970PTAXt2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=QWfWfgcePRVKnfxK0P54EWVj4UM0vgjBmMTyzlQkeu8mM9MM5UmwEmjERm26fhdKzkB4J3gH-AgkGCwcOVhiLv3xzQ2YUZfw_BuitNHKsQHMMzQsfjNaavOI0aVVr4ZjuAKE3kYi95cy9KOFlSlhTDkp6tINSaua1wQoDi6l8yXJ04nr4dYj8tiSFq1Eym2x1FWWLMyD4iGnRf8coEAXIYkooW-8AEm05yDdJ-nHGImXEUngpDZ-TSbWEwu1_pRBQYgEo1X1do3-VjThxQDD9evY-o2WF2rOI_F6GRABLZGaNrZZhxJwCs-bPgYQVMu-7TZcKxakG_10OBDN9OiuIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=QWfWfgcePRVKnfxK0P54EWVj4UM0vgjBmMTyzlQkeu8mM9MM5UmwEmjERm26fhdKzkB4J3gH-AgkGCwcOVhiLv3xzQ2YUZfw_BuitNHKsQHMMzQsfjNaavOI0aVVr4ZjuAKE3kYi95cy9KOFlSlhTDkp6tINSaua1wQoDi6l8yXJ04nr4dYj8tiSFq1Eym2x1FWWLMyD4iGnRf8coEAXIYkooW-8AEm05yDdJ-nHGImXEUngpDZ-TSbWEwu1_pRBQYgEo1X1do3-VjThxQDD9evY-o2WF2rOI_F6GRABLZGaNrZZhxJwCs-bPgYQVMu-7TZcKxakG_10OBDN9OiuIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=N9ipEJdED_seESltaH_36JYqKHtX4pJYWliicPW3CW_VI-lhyoi5mPpeXkhVxJ9F5NFeIOptTgRog2kiRSf7JLu9-PVSMcchCK5hDZy6iJ7f8yWa9LyxH2Y51jm_lM66-mcdjv-Rl6gRDrPImB_AFb5e7YMtOmUkUYKCIt2dofYZ-kwzduzlQtBcrWNVBC8puXNcic-CkXp_0Jq3EqKk3DF8CDfYHq5S4HKzJdXP1oYREcGCw8A8w_zMvUGDsT8ve5xsAMsRIJY7SoEMzkpfolv34LthViyvkjjSbM9XQeyrCGUdGKe5VA9fp-WsC4Wcve4TJ0Gvt_v1ZGqUnjHZdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=N9ipEJdED_seESltaH_36JYqKHtX4pJYWliicPW3CW_VI-lhyoi5mPpeXkhVxJ9F5NFeIOptTgRog2kiRSf7JLu9-PVSMcchCK5hDZy6iJ7f8yWa9LyxH2Y51jm_lM66-mcdjv-Rl6gRDrPImB_AFb5e7YMtOmUkUYKCIt2dofYZ-kwzduzlQtBcrWNVBC8puXNcic-CkXp_0Jq3EqKk3DF8CDfYHq5S4HKzJdXP1oYREcGCw8A8w_zMvUGDsT8ve5xsAMsRIJY7SoEMzkpfolv34LthViyvkjjSbM9XQeyrCGUdGKe5VA9fp-WsC4Wcve4TJ0Gvt_v1ZGqUnjHZdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=UY4wPuLsNYgxO-yKrVC9X9pMgPkmPNU8d0I5BmiPX3uJrm_sc-Sit4syxD_Ay8M0rPuGXwuAMnuMO4D0Nz_ZadkcxGN-t8i3jcaZbL8-vgyp8uk7K9yzDGXUibXFI7Wvl8iu0u20kjawPd5pULF_FUDYhrrdesdblXhTNosPgtQqpMkzPtvaE1xc0bUv_jySmDgbyPpRF8zKON1LtqQSayOmL_YhkEppYBdZNBK8W9AsnxanP6ZriBTFGqO3oNORxqvFwxtMWZzFh6Bjzui5u_rP_llwsdrZFE77v-IRZQPz1USY4UMuzUpkOMiuhcFgzZ7XkAjVpDgZBmcIu_1Stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=UY4wPuLsNYgxO-yKrVC9X9pMgPkmPNU8d0I5BmiPX3uJrm_sc-Sit4syxD_Ay8M0rPuGXwuAMnuMO4D0Nz_ZadkcxGN-t8i3jcaZbL8-vgyp8uk7K9yzDGXUibXFI7Wvl8iu0u20kjawPd5pULF_FUDYhrrdesdblXhTNosPgtQqpMkzPtvaE1xc0bUv_jySmDgbyPpRF8zKON1LtqQSayOmL_YhkEppYBdZNBK8W9AsnxanP6ZriBTFGqO3oNORxqvFwxtMWZzFh6Bjzui5u_rP_llwsdrZFE77v-IRZQPz1USY4UMuzUpkOMiuhcFgzZ7XkAjVpDgZBmcIu_1Stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=dogDWivF6QlfczWYO0ARTu4bkwvfxhwtFkveNdJy7nTZHd64sgN2mdQcceEOWtbt4g_I6MMHnPvTbqfVrUz0xC_KbeoON_0jug1pMbkF8JoQmGVbY8jsSBbQeN0c8c1UbwYAf9m9gjY404HfJpfgtnX011vwl1-e5OG2S4aEU7L4jmD2_g6TPCgI-KkP386b-Pw8KehZSnZVrjlZNDJXZnQEkmlkVX6TGK0rF0Juo57t2O3GuZhGMDqmLNzkEO45mOETbk_VIiMG6e-jI9zWfjINUFdcigOHnjzSRRm0RaQPRBHjQ90PwXv_qkbk1Lgy0cAqMSXPYUqgSkIxF9sI9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=dogDWivF6QlfczWYO0ARTu4bkwvfxhwtFkveNdJy7nTZHd64sgN2mdQcceEOWtbt4g_I6MMHnPvTbqfVrUz0xC_KbeoON_0jug1pMbkF8JoQmGVbY8jsSBbQeN0c8c1UbwYAf9m9gjY404HfJpfgtnX011vwl1-e5OG2S4aEU7L4jmD2_g6TPCgI-KkP386b-Pw8KehZSnZVrjlZNDJXZnQEkmlkVX6TGK0rF0Juo57t2O3GuZhGMDqmLNzkEO45mOETbk_VIiMG6e-jI9zWfjINUFdcigOHnjzSRRm0RaQPRBHjQ90PwXv_qkbk1Lgy0cAqMSXPYUqgSkIxF9sI9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=qydm-ghkgPIAaQVh-U6C30rDB9XMp7V1kAX4wkZu49tt1CA3EHkgwDkbQoonpRuvj52isqAm0zxqa-CNA08MjOVWYk9aUs9mHypKhsplVlxKsqSYbuZ5xO1l8fAMSOcl_9MRdAOziWzJmofo32IWK1cy8DsoeLusa2YDk4YaPQjj3FvMqQtrSMNGolSWFYJkhNbnJ2LkbEpIWcH1EeVUrtQuky2RiKxOUASL3lwJ4ocjBbwpsoOBw66imKs91ZMERk33KCqN7oDyAVkgqcijJ2hYe2_A1Mk5NHlxrzFxjrlyVyfCeuM4rXRo0oXW4OEmZloL4R4TnpO8E8XcKbM04Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=qydm-ghkgPIAaQVh-U6C30rDB9XMp7V1kAX4wkZu49tt1CA3EHkgwDkbQoonpRuvj52isqAm0zxqa-CNA08MjOVWYk9aUs9mHypKhsplVlxKsqSYbuZ5xO1l8fAMSOcl_9MRdAOziWzJmofo32IWK1cy8DsoeLusa2YDk4YaPQjj3FvMqQtrSMNGolSWFYJkhNbnJ2LkbEpIWcH1EeVUrtQuky2RiKxOUASL3lwJ4ocjBbwpsoOBw66imKs91ZMERk33KCqN7oDyAVkgqcijJ2hYe2_A1Mk5NHlxrzFxjrlyVyfCeuM4rXRo0oXW4OEmZloL4R4TnpO8E8XcKbM04Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Nq-4atNL76sry3iOiV2yFsebnL4M8da-zN4rAHCqr5P2Dg_2ZDx1ntH6FPLieNd-tr-iYcRlWGqvBmYb-Ivgp2lxD1WTOZStQeCFTTjpapHcgNpayoYD9jFDCCcpVdkv8J7vwHZf-V1kZoouQMcw7iBmoL5HIOqv8x7yQINahxf4Ry7NYmxzA3mhNCdLOwsto2oJbiVPKkxLnci9sfxvCXFzAKCVu6M6nNV0R39ZtEd3e7BsbjHFlw8q0P5lKmCoYcK12tDiyHyxS9_XCYQ33emfjMyDcr5tdSj8SG6E0XuuOc7MMHeMANBiLpy1GqDQfRWne2DPU6sfMCqT_VTbyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Nq-4atNL76sry3iOiV2yFsebnL4M8da-zN4rAHCqr5P2Dg_2ZDx1ntH6FPLieNd-tr-iYcRlWGqvBmYb-Ivgp2lxD1WTOZStQeCFTTjpapHcgNpayoYD9jFDCCcpVdkv8J7vwHZf-V1kZoouQMcw7iBmoL5HIOqv8x7yQINahxf4Ry7NYmxzA3mhNCdLOwsto2oJbiVPKkxLnci9sfxvCXFzAKCVu6M6nNV0R39ZtEd3e7BsbjHFlw8q0P5lKmCoYcK12tDiyHyxS9_XCYQ33emfjMyDcr5tdSj8SG6E0XuuOc7MMHeMANBiLpy1GqDQfRWne2DPU6sfMCqT_VTbyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQIqYsxOPQP1u1R4Jk0D2sPjkmlrY7FLpCZHDtkPXhJgjByZlr5FT5UVW3UZ7AzfYdh2EZxnPslSb0LSqjtEAzcOyOX1dLGUcozWIeZylZ8oG-F8MKbp5yAQ8kHSV4Smlw9uGOUWMROPh7X8i7o0CBdvHNHYqFV0QayHY6VKdVYvxDr36iiM_gJROB57EsrgbPdsgJGIteTRMFpjU-UgXgJV5gbJGeeo-SED230Og76IlD2lsWKVJKyJQFnziF-6dOpnlqH4HmiexFGsaxL4cyLou12cg72nJww0nCRUJR9ncmkd5f5Y-aFR-s987xlUolGeVsB4GP-0zbPn-ViJew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=ZPKqHM-UDs42k20XSknN4mny5ada-8_TGPIJNfprHsik82Kt5OYD-vZvTOKrdMmUBJSkn5mFuGdNX9h_H1PwuoITcn1tkiKcB-gyOWfMHANZk3cyauy2ZphaSp5MnSie_-paEc7wCqhjbNoZXCVMSSpI2GOFdD_IlacsibdulW08S5O1KgM5hDf9mvgAryUuqGyr49q_ZZ_Dp5R-yP6hwDoxEAjPddcGFA5bbqv4fkIHU64miyvlI5fUJ-6IXtCtrGIC1WW7QC8HXSnCewYqj-WQWSp8IJ2WBZqbd5KEpyauWZTM2x_Pxj9zaApFPPCnlHroWc1YD2ctGDkOkV2jAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=ZPKqHM-UDs42k20XSknN4mny5ada-8_TGPIJNfprHsik82Kt5OYD-vZvTOKrdMmUBJSkn5mFuGdNX9h_H1PwuoITcn1tkiKcB-gyOWfMHANZk3cyauy2ZphaSp5MnSie_-paEc7wCqhjbNoZXCVMSSpI2GOFdD_IlacsibdulW08S5O1KgM5hDf9mvgAryUuqGyr49q_ZZ_Dp5R-yP6hwDoxEAjPddcGFA5bbqv4fkIHU64miyvlI5fUJ-6IXtCtrGIC1WW7QC8HXSnCewYqj-WQWSp8IJ2WBZqbd5KEpyauWZTM2x_Pxj9zaApFPPCnlHroWc1YD2ctGDkOkV2jAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=QNaQg7cPr2sx8JmiCGXk-dbEn7OwToRkDDy6WBY1p43-ZNBItxbrHcwXPKwIW6TBO6ekkFvw4PdYGkDBfS6uNKAwdjzVV8TOrXxUo_7qmU4saXTK8r8HJlibIMs9z4FQvhN-GCJSpGKUBHwP9l6KvDxxHtZmPSOmz9GAZdX7VH-32hO0tW_wDVSsuvnjEJ5fZ_HhWBvz1lndPhhWk_9fVV6dX7jIkaVusJ0EtiOVdeSTCqa46M8zKgQqSCvakgs5ujhSRAMp7YdJWFu_Ho27VPGp7IsRbLVdP1_0AQR1ntcL60frArKFi7tTZLjTw7aMl80jlgPsI8Lt7Tmky6VW5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=QNaQg7cPr2sx8JmiCGXk-dbEn7OwToRkDDy6WBY1p43-ZNBItxbrHcwXPKwIW6TBO6ekkFvw4PdYGkDBfS6uNKAwdjzVV8TOrXxUo_7qmU4saXTK8r8HJlibIMs9z4FQvhN-GCJSpGKUBHwP9l6KvDxxHtZmPSOmz9GAZdX7VH-32hO0tW_wDVSsuvnjEJ5fZ_HhWBvz1lndPhhWk_9fVV6dX7jIkaVusJ0EtiOVdeSTCqa46M8zKgQqSCvakgs5ujhSRAMp7YdJWFu_Ho27VPGp7IsRbLVdP1_0AQR1ntcL60frArKFi7tTZLjTw7aMl80jlgPsI8Lt7Tmky6VW5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=gTORIwxsKmIOJO9gu2-VVVy3CiipfM0zOg38HO27aostVPSh8MUvTRnTaN7e9oryf9HWiGtRLV1jRGMe0NnDNow1R9H49EmXpnZD3cotxXgxXDax-8Tgi3O9NZ7q_wlFr3UQmhqOZGMbjA-1jm8Bq3JVhQccU8S33RmOTD4R_4KQtTptycYEEJaXDK3FmCRNBDx0ail3EydzHQp2pUch8Zet3IK_x6C38E2Q_yu91Xsc3ZGAbflatwJJ0ISzgdn_7u4njNVbnEfk5g4PQymYgzTLEgh27LJvkmtZX3eV_7VLYjirmROxtfVrz1kg50XZzYuGvWZELggSQaj-rqIxEIgONva6vIO7_eYBje99uck6yja0T2mxtH24DqKsWJfEs3QJkVB_u42GXZa9bdEmGetPE-4SYh04Ay_JDdTmpJhJsMo3cji5gy0QPlc3iWki0MQiHPoKjVaAYP2w8wze3J7EqKobsP_TKdcg0wDxm3eHeVwWCpd1B8GrlWl2GcvISlaVJ0PzvI6ghkx4na2yVb2rbkOFJzzYeIzr0mxrSCkO8DOswet-oG0s0OAGHmshnrKV4leRDxQR-F0IUffowpfqIe2enS48E1icAK60mrkonTz3PXZpx6lg8zi--bRLOx9TknF2g4XlAtFzg8Sn3smO1TGz3OMGI41tF4SEQjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=gTORIwxsKmIOJO9gu2-VVVy3CiipfM0zOg38HO27aostVPSh8MUvTRnTaN7e9oryf9HWiGtRLV1jRGMe0NnDNow1R9H49EmXpnZD3cotxXgxXDax-8Tgi3O9NZ7q_wlFr3UQmhqOZGMbjA-1jm8Bq3JVhQccU8S33RmOTD4R_4KQtTptycYEEJaXDK3FmCRNBDx0ail3EydzHQp2pUch8Zet3IK_x6C38E2Q_yu91Xsc3ZGAbflatwJJ0ISzgdn_7u4njNVbnEfk5g4PQymYgzTLEgh27LJvkmtZX3eV_7VLYjirmROxtfVrz1kg50XZzYuGvWZELggSQaj-rqIxEIgONva6vIO7_eYBje99uck6yja0T2mxtH24DqKsWJfEs3QJkVB_u42GXZa9bdEmGetPE-4SYh04Ay_JDdTmpJhJsMo3cji5gy0QPlc3iWki0MQiHPoKjVaAYP2w8wze3J7EqKobsP_TKdcg0wDxm3eHeVwWCpd1B8GrlWl2GcvISlaVJ0PzvI6ghkx4na2yVb2rbkOFJzzYeIzr0mxrSCkO8DOswet-oG0s0OAGHmshnrKV4leRDxQR-F0IUffowpfqIe2enS48E1icAK60mrkonTz3PXZpx6lg8zi--bRLOx9TknF2g4XlAtFzg8Sn3smO1TGz3OMGI41tF4SEQjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=iSo23cwQKW0KsPeVS5CRnOcWpv-0UPU5BdxOnGvOnoc_5lgeBr0m3OKLOnn55Xd0BSq2Ihzo_Sfv0bvAtCqaVE0GEpHV-VZSUaKa9dFv39Z24wdbhjPFrd8g7wYw65BvY1n_Z97ueO5GqS4h6PlMxb4l334SstSBDoK65JSvTNNFw8sXobSM1LR6uLvKeOe5A065G3CXS6pxi6Pq432Nt5whXrwtQ8TJ65JQlL9vqBw8LfH17ugKgSIphiBOo77b3Wv2Tgu0PjXxENPYvNFdajvTOqTJoLtZXJReVAohZ664fxU3cldnxB9c1cZ3DJK_hYB8Au2DaQNB9HxNKkUpUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=iSo23cwQKW0KsPeVS5CRnOcWpv-0UPU5BdxOnGvOnoc_5lgeBr0m3OKLOnn55Xd0BSq2Ihzo_Sfv0bvAtCqaVE0GEpHV-VZSUaKa9dFv39Z24wdbhjPFrd8g7wYw65BvY1n_Z97ueO5GqS4h6PlMxb4l334SstSBDoK65JSvTNNFw8sXobSM1LR6uLvKeOe5A065G3CXS6pxi6Pq432Nt5whXrwtQ8TJ65JQlL9vqBw8LfH17ugKgSIphiBOo77b3Wv2Tgu0PjXxENPYvNFdajvTOqTJoLtZXJReVAohZ664fxU3cldnxB9c1cZ3DJK_hYB8Au2DaQNB9HxNKkUpUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDjrcSa_ubCK_Z3qUBDV5QJdVI8QYB_4Ey3nltp7nmoa5BHj6lxLRx8D7zqvj-Zcj2ZuLAadJ9PrcBH4LtX5tpaaABgXBMbuWCyP4wkh3TANMbndcmYHK5ZSbkkk-Twu-e_Dw7dYpCZtqLRExy5UNG5geg04-gWv0348htLXWguBVz9CvoqTJqjI6uk6VFMjdVUiP8hywOIw2kv9bwiaDcQG8daAwnk7IxMwOjanzjxrW6PS3qlFbbkG2uGGK7RXknKGwaZ2rhG6DYoDmRVqcJZJeSCekJoY_X1yj9LFqQnAd2VyaqXdAp_v_GejZxR0fn_Un3zpqej4sQgVwks7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASweJc800lWgtW1H5PU4PadcbOxMRS-RY3snJUKaU1O0C2Cd_WEBGAPnMmDhexN1Ey5gou0kEnfkXVJ8NIoPCvkUs4OpmoUVchaA21ocUPsSGyWFS47iF36goeaT567cubo9-UBJk9iF9oHCeIpyw_jzU9Ft-Ucpc0KFhGmhefvZpdKESE32M5ANVriFLKgWFQzpaOMq0he-ExbKAKdCOfZWa-AjJKuj04q9VGampRh5E_jmDcgZpeWDtN3__NDOtDu3gJ-H9Ow3F3P6OJKsLjmrvYBsXCnKNKj2L6dUGpEQDcEwwGUrn0roeM8Yls_BUzeHIU6K-dI5skLpB-hf8g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=QJZICC22L1NKcL86yMX_v-u-NYvIq04pR1iWvGWV9NaQUmCrvG4eGTKzKwguAEbch6Nc_ncsKehQTRKgmweRXbf1zmjt8eMq_g3unx7MAZnSUWuocWYdrhoNRCWexjAH5DdNKMtZZ3geItpadnxFmAezpBXXPk2_CSmUxEc8PsVktF2hMmcbd4K1nau99FUGE1e_kcLybi11zYfm5CXhebmAHMzSlAKssrFKQ7qpoRWaNfI3uKzVrhq9nHxEoN5onESx6i3jCEf3Z9pBXW5cESvnSMmi-EzmfvSs8JjN7LL15PO1h7mD_R8fm13IhvWaPjwz3_yyYVtDl-8Vvt-sj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=QJZICC22L1NKcL86yMX_v-u-NYvIq04pR1iWvGWV9NaQUmCrvG4eGTKzKwguAEbch6Nc_ncsKehQTRKgmweRXbf1zmjt8eMq_g3unx7MAZnSUWuocWYdrhoNRCWexjAH5DdNKMtZZ3geItpadnxFmAezpBXXPk2_CSmUxEc8PsVktF2hMmcbd4K1nau99FUGE1e_kcLybi11zYfm5CXhebmAHMzSlAKssrFKQ7qpoRWaNfI3uKzVrhq9nHxEoN5onESx6i3jCEf3Z9pBXW5cESvnSMmi-EzmfvSs8JjN7LL15PO1h7mD_R8fm13IhvWaPjwz3_yyYVtDl-8Vvt-sj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUUs7btdhA_AW00OE5ZeLmplBfczotr0oE0CYM14XCCx9cL3i-u-HC6c2yY1rAu0X5g9xaQjmk5aGPlmwRqtTTWsJ9BjZUJHxvD5MsobQj8_EgrhRM3x84sf47znpWMpGacfBXvBsSnA3teTP_4MAhqbE68DrNtHbL3EG7WnEh24ul_gvbOA8-g-tJITZDJLtp0uFfLd5tuyk1nZmlEXJrzLKHB-4NDBua2asdkKHYjBdHOfrkgkzZXn5IWsTzddIj4xDmps1Ee4Sz111T8koaE2bJbmSlQs_l4XvopozvcEqvjOHw8BblBBqzw3SbNX6fcs2zCVHxlDJohECLUrqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mICDX6-pKNcKSpY2aInDqj7VZegVn6voIpfvfd56fc8LtxOltIMVzVClMOOxwuQ8yihQ0u-___qyzn6e2CF--sfTcCQhs5ujVEct8P49m_iQNss7JpwYhnFYSlynVbdSh6J4xESqbAP1pDgofmHustxcbKrkWh2DW0uL-0LlUMAHKSUyR1LM9dP10KCqTeTPWw06gyCgWpG3097WtaHqiYoV9QoWdsQg6IM311HV_nKsE9X2H6UJZS5IDJwc7d2SDSmuP_xU0BRqPk1G7jXjuM7L3WncHFwg2hBwr_Fh0c0jOCdIsoqblJNKtQMO2EkIuFUFwgBf63s0wx5d4wWm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yq30Ms_UFtDxzfJedwUeyz8-fKoqfiJ85hLdISSlZBY1D59MAN9sM9htF6FOPD-k_4XN0bLhqOTlPV1xd8sXThlanapQ2yfQKFHYs7GH5sL4uwXDIrQs61_-_kdln7Ss6mjWNCW20rcdXmNTdSagCx38Has_DOnsOQ5O488VCBXYFIGO5c58yKT8Bnq4GVDzIYHIoWC0-0zkrupdsoQMqiLSvBGR8YElWq4kkVvEuR_BQVBdkFRKW7T8su6JSN_UIFUxhJIsnwyS81QzPVfrxlhkqeYYAuoVeRMKXp5Bi6hwwZJjrbjiDf76IMQ0XrgypWA6q8l-Pqpje08XvIYzEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZfVvot8U-cugr7cPC1JPBh3lH2ck_zYnhaYJpY26zwCzuayvV2Ngff4zjJN48JUDRcWKTWHiLEcwaks-eOpZjbyqpiaBfvpjnd4AARDrzanbR-462DzHEGE-iYqWA8vH68LiTZ4lsdtZkV6EPLhVNalb0_sknv0sCkdpohNxyNvq63Hs1tyKY5uV6f4TXwRrusIiczpGsPAHN6KZTWLF4Aen67-Ba7fzhQOPATbeo9gco68hQ8qkNMq7irIBL7i_hkicNAILlG8c8UVxnTk2BFXNPXKgnn3hJphH4oKhJlFzaSFNukAno28RlXZq5QJbqEVQkDR0PoVzBgn3KEs3g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=VlFAUdLM9LuPjYHq0KNQy69X1p7S308tPmfvcekas4HfQeEF1L-p2CmXSxTH5_uOMMS7dfMtMD1suB5pne7moNeHOX9EbM4oKpMQsuoMoEqPQlt-u86hDKjLl73MOl55UhfU1LsnkBMMrivU8TAP11UREOBC57QYBu_taLGQttFwAInExrIKO5vGhcKBP4MoEbrEbaIefInRHtuwLy6AzEIVHy1psLe6REeiS5UrM_nSy5Q-vQyqebAD2QMC7lpmEWDoHM2QA-BkgKCpnjuYOMahxgY3oKLAWmVn8uPmz01SCJRazg8VU-ZNM4z_u56uSM2QiQYvxBN9yoMXUxBcmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=VlFAUdLM9LuPjYHq0KNQy69X1p7S308tPmfvcekas4HfQeEF1L-p2CmXSxTH5_uOMMS7dfMtMD1suB5pne7moNeHOX9EbM4oKpMQsuoMoEqPQlt-u86hDKjLl73MOl55UhfU1LsnkBMMrivU8TAP11UREOBC57QYBu_taLGQttFwAInExrIKO5vGhcKBP4MoEbrEbaIefInRHtuwLy6AzEIVHy1psLe6REeiS5UrM_nSy5Q-vQyqebAD2QMC7lpmEWDoHM2QA-BkgKCpnjuYOMahxgY3oKLAWmVn8uPmz01SCJRazg8VU-ZNM4z_u56uSM2QiQYvxBN9yoMXUxBcmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=bbUdeudmTp6oLy73h95J5S3nDMQMb7rTa35xxEwBq4jAuXjaBL7Deey1yjkrKpYF8A3f-3qeVpd-3V1F2QHzXkDxoVoDxqL0VoAELIZiqHZcTbKx2IXna7Fts1uUWFAoPL5nrM4NXQyEtY-_Tc8yF4zo6ot3P5WlFx9bMkxZJbDmsO17jBoYiV0LEci5VyOXTXXOa2PUT47sK-a8widzjikGdiuMFmWQQr5m9mK2jKaTn5B_WT2nIg-fmRucWkspUoeTJGsSvJJp6Cx2ilGo6NqJ0n6-eVvQ_Xj-avUqi8h9MLmU81WWRCXdCcpM_Jt3ZPjHIKLGbBe6p6tKGkW7Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=bbUdeudmTp6oLy73h95J5S3nDMQMb7rTa35xxEwBq4jAuXjaBL7Deey1yjkrKpYF8A3f-3qeVpd-3V1F2QHzXkDxoVoDxqL0VoAELIZiqHZcTbKx2IXna7Fts1uUWFAoPL5nrM4NXQyEtY-_Tc8yF4zo6ot3P5WlFx9bMkxZJbDmsO17jBoYiV0LEci5VyOXTXXOa2PUT47sK-a8widzjikGdiuMFmWQQr5m9mK2jKaTn5B_WT2nIg-fmRucWkspUoeTJGsSvJJp6Cx2ilGo6NqJ0n6-eVvQ_Xj-avUqi8h9MLmU81WWRCXdCcpM_Jt3ZPjHIKLGbBe6p6tKGkW7Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO43S0E9WGP4DDy3Fs293QfrZzW7KdOQMm9YtrdeEV33mM1fb9zRmp3QuuLxM6XUFG6HtPyUE2xnZ_CECMtEeKpxFmXlE84QFk9scVuEzcnCQw2SIqwJdSHPiEVXWNuwwodJBJHuf2O0QgQQYSx3t8dVFIzrgJwAbtELkRK3yJq-OJXKUP1_SpI-EbfSXHAHXk25ZylsZ0gCsdpc3W8ELvcRQKwESRR9qibrzytnz2WEnTboIXpGgKMRs2eds_j94ZsB5U2wicvBvPLs3qHd1RWko1tX2WAXL49tmH0h2bhtRscLK2FjQEtgkZC4SmoIgy7FUvzJJEJYMcR3MbM4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=YaRz7htvmg747TorkzoguBUJwsgDDZcFN5u1x1Bm7O6BI11aTNHngbh2ZFDk6bJNm9CA1b9bdHy3J6u44JXCkw0rpVugtlmhXIFLfXQsMY6WovrN3z4wBImNF4A2drMxRdngy8Lf4cai2Sos1qJJM2Vf1hM_Ba96HspZub694ufCsJHlzx-b0YWyi-dNXoJF01F5f76-JgWoMSbdEYYEOjuvwEQn7p_l5BOKUcGlwmADJK-fg_pkh-jLt3Rkepe3xHuoj_CVWN4qTSgL21c2tK8ce-SD8GsYy3jCdi988pVv8pQ6BaQemAropyEMIwScf_GNxaP1iU-9b56Vq1-V1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=YaRz7htvmg747TorkzoguBUJwsgDDZcFN5u1x1Bm7O6BI11aTNHngbh2ZFDk6bJNm9CA1b9bdHy3J6u44JXCkw0rpVugtlmhXIFLfXQsMY6WovrN3z4wBImNF4A2drMxRdngy8Lf4cai2Sos1qJJM2Vf1hM_Ba96HspZub694ufCsJHlzx-b0YWyi-dNXoJF01F5f76-JgWoMSbdEYYEOjuvwEQn7p_l5BOKUcGlwmADJK-fg_pkh-jLt3Rkepe3xHuoj_CVWN4qTSgL21c2tK8ce-SD8GsYy3jCdi988pVv8pQ6BaQemAropyEMIwScf_GNxaP1iU-9b56Vq1-V1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=bchrk3Gag2wyTYRCnvMp0EeMjt9PqcHPhzIwx4DOoBKfX8YxTWtAcypz20VJbXs5e0_4jeOP9HbrdZF4Wt7sKTcS3_AJPhwkJjSa4LMuusDsXcwVamzHBwsFNdxJAjCNg-EqwNpYO-DivVCo16Egu6ZusdFa9YEgm783G_z32YfNgasiNtFQdbSJU6_oWYnF1ci7CiYCd7eGCfLq6Ug9EDkCTvHlAmxNOOmrVim64p8qBAndKL1g0p0jZ5KfKTeaYilp3NVJW14gFFmkiGf9cZgkEbKg23TBcFMjrcyjEzuA-iL-q0O3JCCSph8iO-pkoGIGSbT1aLTM-HS-0FfCdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=bchrk3Gag2wyTYRCnvMp0EeMjt9PqcHPhzIwx4DOoBKfX8YxTWtAcypz20VJbXs5e0_4jeOP9HbrdZF4Wt7sKTcS3_AJPhwkJjSa4LMuusDsXcwVamzHBwsFNdxJAjCNg-EqwNpYO-DivVCo16Egu6ZusdFa9YEgm783G_z32YfNgasiNtFQdbSJU6_oWYnF1ci7CiYCd7eGCfLq6Ug9EDkCTvHlAmxNOOmrVim64p8qBAndKL1g0p0jZ5KfKTeaYilp3NVJW14gFFmkiGf9cZgkEbKg23TBcFMjrcyjEzuA-iL-q0O3JCCSph8iO-pkoGIGSbT1aLTM-HS-0FfCdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=Bfy14AR7XVWyD4PMxwMqU92gfKJd20oTTE3T-1IDSc4m5zjaT6RYUTUyUuR_--IOtVIJRlnWQ-mwaEhv0qeXGwk31egyJdE4NSXjE7WHRB-Xy0l-zsl3BZk9QT9aaeswllLzczYLqmej93NXLIu0NU-fKDpj1Mjme-Idabg9NENxdY8yQDNBx12Ca-LXVACES3rd7HlU6H6u9dSAaOQoVn2mvwZaiizmYpNI2sSPAraAJ6GOTxJguQ-_o4Bp-MAYvn-pObHMeI20GvRCoycyUfxSMsSjIoHX892QY0JeT8T3XLWKjMpIQ4mWKQFNhSCJ5a9VkmNZIl0JQ3_CEeJD1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=Bfy14AR7XVWyD4PMxwMqU92gfKJd20oTTE3T-1IDSc4m5zjaT6RYUTUyUuR_--IOtVIJRlnWQ-mwaEhv0qeXGwk31egyJdE4NSXjE7WHRB-Xy0l-zsl3BZk9QT9aaeswllLzczYLqmej93NXLIu0NU-fKDpj1Mjme-Idabg9NENxdY8yQDNBx12Ca-LXVACES3rd7HlU6H6u9dSAaOQoVn2mvwZaiizmYpNI2sSPAraAJ6GOTxJguQ-_o4Bp-MAYvn-pObHMeI20GvRCoycyUfxSMsSjIoHX892QY0JeT8T3XLWKjMpIQ4mWKQFNhSCJ5a9VkmNZIl0JQ3_CEeJD1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=IU-B7oQPEkWym8uc4b-wWjEs3OpP65RHqIz0jnk7cJIl--0T9ZYJx1kknqlHBgSgFwxQZMFW8akH0N7rcywemc3xMG9Eu-CUEy1tiLVqhuOOUbzbtyfhydmbWqKDc6l4GmV1CZdlLXJUoAIfiJD7LcKBzxxJtnffQx9ksnAM_XFXurPD2LulQJBBthii6CYVWBaztl9AKjH6uehE7yfLwLPFR3Lr7Lvb0F0ZhBFnXIFY0u_x74hSBbjqj3SljbZ6ATcgew1cknfPkc1vQBq0Yc2HfJry8mhSXI5ixSnEoUdT2waPmBfI-XrNyWMVFkFwSWhmEtiDLV-fJYmA_0dAYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=IU-B7oQPEkWym8uc4b-wWjEs3OpP65RHqIz0jnk7cJIl--0T9ZYJx1kknqlHBgSgFwxQZMFW8akH0N7rcywemc3xMG9Eu-CUEy1tiLVqhuOOUbzbtyfhydmbWqKDc6l4GmV1CZdlLXJUoAIfiJD7LcKBzxxJtnffQx9ksnAM_XFXurPD2LulQJBBthii6CYVWBaztl9AKjH6uehE7yfLwLPFR3Lr7Lvb0F0ZhBFnXIFY0u_x74hSBbjqj3SljbZ6ATcgew1cknfPkc1vQBq0Yc2HfJry8mhSXI5ixSnEoUdT2waPmBfI-XrNyWMVFkFwSWhmEtiDLV-fJYmA_0dAYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsIjdGMIBpvEviCozy5TfCGdy2Q6l_2Bf7fulNgXDr9sROBHz3eRftzPW3UGgpxBq8DO4_PO2yELVQrZn5xD8gwyysM68GBS_q0ghJsGGPMzA3f2CJHldGdCdEC_kvy73cvuswWev9828Zn0kGUwJYUnPj7d6SXeASUr_F2nK-5pFexKY1RZmNvTRjw1UE0CDiLwb7FPRDE2pQEHN-ruu7Jsz2fZHb31QtdibcEUeIXSIx57-srS9y7nAEOZdfHzPB26OyXnKnljBC2FmnvATFv2EbrzVMyWmR324zI4Ndf1gAPTTfUs7gjwh-jPEBFGANIY_PRIIU8q-okYAKI2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV0WcuQulvZQA-u01OIjW5dpgokk8aCZlNKzoNZjNdF1X4KbIw9rqJpP5daHi2kLxt5jrMWUUSZLTn94wrubg8V6ANNtrQUxKb0vLlLcRdbdJ5LNiI54a6HcsmCKf9XdBpzcuMP1OZgXuNKHAmNGV5LgbZ89-FKsxThE87ZdmvJiWUlrN803AsXYmAMjsJ2q6ta3b6XlI1KtH_BKN8hTxGWnP4jhOuLUZvQOq--zLXaSybqOQ8Cky1hk8_5gtpixVAw806appqYwgw8jyjUDm5D5Ja9atHAwZ9fZPAwoasNRYVUZDUXgM75s3h2foeiJm3F5uos8DWiPb-MrsO-BkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=ekmf5DgHUyhlA8JyZvQtIgq6Mn9oNr5_yFXhBM8dWUv5s5owSHJF7d59EdHohYLQUlzaYgx-tzwR333n5knRpNop2FODTnXzbBx3XwoIK4gk1NchWIuXDfcXt61yLORpGRCItv8-PeSNVQhtloK58woX2OJfqAhYsyBy3sGWWL2MqXq_D_Lo_EEW5zFbYVFjfQDTVTuhoCAb09I2tcP529M-5YbUpdlmOTNPq34M_u1YN072USWj78Tbqm7uBVpSp2GJd9SVn20axL3HttyElqPpShyOMdaPVn1E2ifhGwVDgP0IQmQYjTFxQ3JDZyK0krlXmb1Hyst-sO4mnvD1UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=ekmf5DgHUyhlA8JyZvQtIgq6Mn9oNr5_yFXhBM8dWUv5s5owSHJF7d59EdHohYLQUlzaYgx-tzwR333n5knRpNop2FODTnXzbBx3XwoIK4gk1NchWIuXDfcXt61yLORpGRCItv8-PeSNVQhtloK58woX2OJfqAhYsyBy3sGWWL2MqXq_D_Lo_EEW5zFbYVFjfQDTVTuhoCAb09I2tcP529M-5YbUpdlmOTNPq34M_u1YN072USWj78Tbqm7uBVpSp2GJd9SVn20axL3HttyElqPpShyOMdaPVn1E2ifhGwVDgP0IQmQYjTFxQ3JDZyK0krlXmb1Hyst-sO4mnvD1UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0nab71OZSw3n_6aQVSdepzvFPVfaJhblwx9ifJPo8UC2KJd55fJoHqiLLdZ87ugRkkUzlw4zGjhrMzRv9vXjFOnHDosFaCy4vpaMcL8zTZ0aZ9IVFJhBG3SxYBs_ouI_yW7E_aVbCe9EXvqbkOUjwqm3_MQjS7L6rMMMa2t9tl7y1Eml4R6NjE3YX5xAFttRhk_LFWKj4E9IyPAmzpTGMgs_XZ929TiixP3t2wdtmZ8lIo_6J0Sryo_kewJfijCBtW5ps8gZmmlbrxqOYTo6i5CUFQ7TzIpnv9KNcnEsZbD5bgNCkDb9Hhq4yf4ut99BqhL8oqJVByoVOt6kvEFYNok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0nab71OZSw3n_6aQVSdepzvFPVfaJhblwx9ifJPo8UC2KJd55fJoHqiLLdZ87ugRkkUzlw4zGjhrMzRv9vXjFOnHDosFaCy4vpaMcL8zTZ0aZ9IVFJhBG3SxYBs_ouI_yW7E_aVbCe9EXvqbkOUjwqm3_MQjS7L6rMMMa2t9tl7y1Eml4R6NjE3YX5xAFttRhk_LFWKj4E9IyPAmzpTGMgs_XZ929TiixP3t2wdtmZ8lIo_6J0Sryo_kewJfijCBtW5ps8gZmmlbrxqOYTo6i5CUFQ7TzIpnv9KNcnEsZbD5bgNCkDb9Hhq4yf4ut99BqhL8oqJVByoVOt6kvEFYNok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=aw5uHaseFKEw9I75wFebFZz7laLShw0L1xYTFKjo-3MbEygKqSOFWtYptOILU9lbSq01Uk9wlHGm90llC9CH_FBmQTa0ZoNo5o8m4SH99qV0lNianAG4A6ONqGOfQqEFXoddxbGDyPV0SJEX09bWW7oDVwJDe_YRWibRD7tdzH0nW2w2L1XCtbptJ0mZHKNz1JR0P_J8BiVgK4yHZrB7W6eL7EdpZUmCfavStnpWdn5TXS0Iqd8LkU0n3gnGYLOv9_53d_qkH84zykSqVCSKAAb00l-NoHOWZcYfIoAxqZdR4Mus1NCi0LFH0o02AEp4d29dD0gGL7r7c2EkVLXBqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=aw5uHaseFKEw9I75wFebFZz7laLShw0L1xYTFKjo-3MbEygKqSOFWtYptOILU9lbSq01Uk9wlHGm90llC9CH_FBmQTa0ZoNo5o8m4SH99qV0lNianAG4A6ONqGOfQqEFXoddxbGDyPV0SJEX09bWW7oDVwJDe_YRWibRD7tdzH0nW2w2L1XCtbptJ0mZHKNz1JR0P_J8BiVgK4yHZrB7W6eL7EdpZUmCfavStnpWdn5TXS0Iqd8LkU0n3gnGYLOv9_53d_qkH84zykSqVCSKAAb00l-NoHOWZcYfIoAxqZdR4Mus1NCi0LFH0o02AEp4d29dD0gGL7r7c2EkVLXBqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2M3Zwql6OpTIGTpQ3wKwNOPEbXWMUjnm_dsqXIF0FsMMJp5hKwBfN95MrbfaXxpf5sT7iK2IhgA4O-YED_TqFK2hsf_uMCrC2bCGBZegAgmCmWnV4cvFYJE1qCrQEx8DPVWbr-O3kunnkdnlU7to-F-RRsulSXA-6CRfvo3wEtbtrBRsBboz5hav-2VJi-KLlKe_d42gjSXOxactVMqsw9hJw2pCU01ta4uzOepoPPjkYlUBR8M_C678m7LXH_GFe3Is_FPiaF-MEQaPk9z3TnPWbKwTumvXX3r0OLCFG5KgjsFWNCIONOjzJ0tB56YSkab9fSHI9n73n54cX8wwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=YVjaDdHxbYCoHHUEPpeZGXoE4t2ANq8x-XBF_YQ_JF3IRhSWn7ahZdCg-hE2-yhLnFi2ionOCzD8poe--fiaUHZvTbe66aMpIaZdzsUxMMSPbnvBkLbYU6N4WPvylHtW5XeQmhSfLMK_EYLBUtunUPAx36yX5NR3GP9t2Qvb35eFD44VxoKAzu2kwf09QK4y3EfvGc2C7vPlNgCJALEILAkSJiEuVwcLFJJBpo4PKFatVPTbUgpbGHXaaXXta2ptk5G1nqfagFuk1L3FMv_N5RlDMkLLhajhjHbQX9_k3IjLECxZlL8Yty4Z2y6GQOTK78e3IXouxH44fZHBIK5riQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=YVjaDdHxbYCoHHUEPpeZGXoE4t2ANq8x-XBF_YQ_JF3IRhSWn7ahZdCg-hE2-yhLnFi2ionOCzD8poe--fiaUHZvTbe66aMpIaZdzsUxMMSPbnvBkLbYU6N4WPvylHtW5XeQmhSfLMK_EYLBUtunUPAx36yX5NR3GP9t2Qvb35eFD44VxoKAzu2kwf09QK4y3EfvGc2C7vPlNgCJALEILAkSJiEuVwcLFJJBpo4PKFatVPTbUgpbGHXaaXXta2ptk5G1nqfagFuk1L3FMv_N5RlDMkLLhajhjHbQX9_k3IjLECxZlL8Yty4Z2y6GQOTK78e3IXouxH44fZHBIK5riQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=R3G2RMVVyq5ymam_kyxARpb6NC1F57iMbH11aRDG8EXO40CpYr6KG5fSTx5nowR5xd-JSAC_LvcxifuML7Miw2WeEuzQxYXKTuVTnwY24dy_-PyjmttkBJOVRIzhGYV7Fp-BRz5x4gqGrx9vYnrkbX1lLQuEqQ44modEWZ7GcXMYnFzT70tVv6WDAKbAml_ZmYlZnMaIB5BBRNdeM-bRcdD1IMtq0rCcoMee-D5Q1KasOnujc2ZoMrdf4TkYf6hjozTQRbQUZur90thfScLuIfaGmZ_XTkaO5uwfJDbnPdEbBRfOxTBx9G_Sxv3TKvlrya1N9m5hnUUKl_8UgK0lxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=R3G2RMVVyq5ymam_kyxARpb6NC1F57iMbH11aRDG8EXO40CpYr6KG5fSTx5nowR5xd-JSAC_LvcxifuML7Miw2WeEuzQxYXKTuVTnwY24dy_-PyjmttkBJOVRIzhGYV7Fp-BRz5x4gqGrx9vYnrkbX1lLQuEqQ44modEWZ7GcXMYnFzT70tVv6WDAKbAml_ZmYlZnMaIB5BBRNdeM-bRcdD1IMtq0rCcoMee-D5Q1KasOnujc2ZoMrdf4TkYf6hjozTQRbQUZur90thfScLuIfaGmZ_XTkaO5uwfJDbnPdEbBRfOxTBx9G_Sxv3TKvlrya1N9m5hnUUKl_8UgK0lxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=DXRdGqCOW_ZD0HCtthLKoGJoLykrj6Uqx2HbR_gkY-hIqhlDxvf_lY62qDhfgBh_3Mvi7ct923w9ang9rJ0NWa0Ccce3qJfWRAYbbRy8XwtVZooXr8n7oQN7K_VX9F6FIKMI4g4WbQYExcPdV8cuSfCV0Wfe6um6abgBTMe0gA9z7pu4Lp0oMIHDAg5QlLskhmf1IfKgAooom1MMZruntaE9oClAXKDV9eBE45onQ2Xsri9XxYn9nLUQ-NZ_S6JNQobOzIBHXco3UhOvxszUtA0wOJ90tHO_xRx7vH8pRcamITauzXrFsx9TU8b8kTlhZT2Hknqz-eLbNOCBxIarGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=DXRdGqCOW_ZD0HCtthLKoGJoLykrj6Uqx2HbR_gkY-hIqhlDxvf_lY62qDhfgBh_3Mvi7ct923w9ang9rJ0NWa0Ccce3qJfWRAYbbRy8XwtVZooXr8n7oQN7K_VX9F6FIKMI4g4WbQYExcPdV8cuSfCV0Wfe6um6abgBTMe0gA9z7pu4Lp0oMIHDAg5QlLskhmf1IfKgAooom1MMZruntaE9oClAXKDV9eBE45onQ2Xsri9XxYn9nLUQ-NZ_S6JNQobOzIBHXco3UhOvxszUtA0wOJ90tHO_xRx7vH8pRcamITauzXrFsx9TU8b8kTlhZT2Hknqz-eLbNOCBxIarGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=E-eme8u-cOEUq5gVns0AfkwYdi_1PZHJPiodLOwWl9BtWMpd8Gotgbd18eZ59WrHH6zF_kZkLujqFQ26KX_Mt_sxrA3NOjN5A353mxqrEteffpTktRpef5oCQX2dt8HHl6JGpoYX3mCqMrtgYUdXEE8GLE8NfBEddNFEFxZtcePSBs8pWHCDZ00_ahHCfrSqtF2pHbAzkIky05m30AszLDisr43GUTfeTWTkfjeFHEFdRnwGdoE2zTKFoB8i-U_JZfT6quRLFCDJdoUGwLc7HVkWf0uhvoTJfeYOENxQeHQgERXk0bIAbwR8iUH7p4tnLshIKJB2JXZS4MqrR-toAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=E-eme8u-cOEUq5gVns0AfkwYdi_1PZHJPiodLOwWl9BtWMpd8Gotgbd18eZ59WrHH6zF_kZkLujqFQ26KX_Mt_sxrA3NOjN5A353mxqrEteffpTktRpef5oCQX2dt8HHl6JGpoYX3mCqMrtgYUdXEE8GLE8NfBEddNFEFxZtcePSBs8pWHCDZ00_ahHCfrSqtF2pHbAzkIky05m30AszLDisr43GUTfeTWTkfjeFHEFdRnwGdoE2zTKFoB8i-U_JZfT6quRLFCDJdoUGwLc7HVkWf0uhvoTJfeYOENxQeHQgERXk0bIAbwR8iUH7p4tnLshIKJB2JXZS4MqrR-toAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwcpekjq4a5sYCryFwMvtQXcHHeERYDRcS8uNpmBZu-TvllBDw02y-II0SdH020kRJy6B86txtglsD-b8j8uQ_euFBdVlgddC5HfF7uwrCqf-NER9ZO91EOuhf9D5exZ3C7btlvFbJdGNZcfUXgWzTagYZD1iZ8jm3BhQdceSis0ccR1pPzfQKBjxl1VOqm1yUrWp-9XWTWNC69v-lbWL_cJ0CiAOlhIvReLcMlJc2jK4-UXwA9ujo908XSGJhMosvBZ0FIUgzDoDz6RiBYheULcwyXrymKYF8kY-Zzkh5i9IgtTm9uoUqEVHvNYskQweKDSvsAg5yZxxYgqg4zhNg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=pAkPj1nbPf1qGtY3nK3fA5LwD2l_9Ul3YAFIfujnBCQtHkDIghT68WC2Hw2YiZwNnGb8KPDr4qOsEhmUwsRgx9ezc4188n40DcLvnN7IKkRhYccqZMGXnDP6ijRj-NHa_0qD5sHJJlQJoPI85aLQf9c15Dukfkn-Xj0RulaW7D-PqK2Qvng61qY3_VBgcAtn5j4oPdLXLFoqwbz_DE_e2A_R6WFgS0Ayy7B6YCT48_h4mYXlrVpvbUSGilon4cy6B0Ay_gxlyeulaZswPaZoPaD0a4ePxC7mFecPLQ4VkuE8vMvGtb0KtdPmKRB-WCKZev6FWmNm9jc4OijHUAk7GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=pAkPj1nbPf1qGtY3nK3fA5LwD2l_9Ul3YAFIfujnBCQtHkDIghT68WC2Hw2YiZwNnGb8KPDr4qOsEhmUwsRgx9ezc4188n40DcLvnN7IKkRhYccqZMGXnDP6ijRj-NHa_0qD5sHJJlQJoPI85aLQf9c15Dukfkn-Xj0RulaW7D-PqK2Qvng61qY3_VBgcAtn5j4oPdLXLFoqwbz_DE_e2A_R6WFgS0Ayy7B6YCT48_h4mYXlrVpvbUSGilon4cy6B0Ay_gxlyeulaZswPaZoPaD0a4ePxC7mFecPLQ4VkuE8vMvGtb0KtdPmKRB-WCKZev6FWmNm9jc4OijHUAk7GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=OsUCD7RRe_lxsqd42NNM-s6jQd32mM0HgXxl_CIJkI07kpBarN_ZKyNHhFovd1_2SHdk90K-9ioXUDaGAkCxoPROwvw4r6W_VBEqr4Ur-Lwri2jJVthRWb8jKBKoqwJsz589uWCfYodc9okHdiCQ3PFPPNNRJIhRYDcu_LtHY6K0TZZzQo5a19vyAXhC_h-UMD-NDfs8AvqHpDzSiV8so4FPCCYK_lVedCjioCTzzpDZb6WHSIks5sZnpZo6MpxYE0sSs5MaSbuaog3jBUejAtCX5MH5fpeHUwGtMgaoxQS4l6B1yTE1dp-WfxVz8m_A9KoxFJYFuJmaO-mUnqMU-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=OsUCD7RRe_lxsqd42NNM-s6jQd32mM0HgXxl_CIJkI07kpBarN_ZKyNHhFovd1_2SHdk90K-9ioXUDaGAkCxoPROwvw4r6W_VBEqr4Ur-Lwri2jJVthRWb8jKBKoqwJsz589uWCfYodc9okHdiCQ3PFPPNNRJIhRYDcu_LtHY6K0TZZzQo5a19vyAXhC_h-UMD-NDfs8AvqHpDzSiV8so4FPCCYK_lVedCjioCTzzpDZb6WHSIks5sZnpZo6MpxYE0sSs5MaSbuaog3jBUejAtCX5MH5fpeHUwGtMgaoxQS4l6B1yTE1dp-WfxVz8m_A9KoxFJYFuJmaO-mUnqMU-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZKrBswhYZTmhIlkLJ9qIS-5tiOzhjSvkesD7Q4GuRWiZK1bm5GiYf2nCb_TjzzYv8yj9aA-3FyuPslMS2XBQ-GlTUWoMGNOnhXI4Ns3JMBO-6ygStrokvTIG6AZxYjV8SVNz12nNAUAbVh3mecCIjVxNDE-C9nUo2RfWFCBjn9bM9ShWIM9L0M4JZT2uu1yqB8DSVLha1spytKBjExbRt968klpInXa5mpZqWqV4Yo_sjItPgYm1hbaqhBmhPwJ7LG4WL0UVpZx4P2VM98eoGhuE5VvbcHkj8bI1O4XjQWQ6gi7BnQbG5YHCKjLF0pq3q2YiOlWCO056HJS5GL4kg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=HUk0TzXndZkcg8nNxN164rywN-iM1K3hzPOQJkxZNL8BJDaSaAsCW_aWYfQVTbfenO4snTF_Pr0ePvaMj3uwS3RmEuvENOUqQSCAi95oh3fQgkzUTHjb6_MeICLHLQIgjQjQfDVIL3IDfNhVQFtPkQtQDar-o7KU-E-JLOBZHfEFrdVSp5vOFf5IgF08J-R3BbX9ZymlpHr2R69VOz1hrg34VEWPsgqgy4JFiwCu7VW_j9fTBXueIDhBiNl-PAKCr6weG1YzMRY5MpUxkVoYqBafV0fRw2CTwboszJv1WLXDNiphG4KgJ47bt4u8M5KjAQ1xudSatKXApmN1wRqBoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=HUk0TzXndZkcg8nNxN164rywN-iM1K3hzPOQJkxZNL8BJDaSaAsCW_aWYfQVTbfenO4snTF_Pr0ePvaMj3uwS3RmEuvENOUqQSCAi95oh3fQgkzUTHjb6_MeICLHLQIgjQjQfDVIL3IDfNhVQFtPkQtQDar-o7KU-E-JLOBZHfEFrdVSp5vOFf5IgF08J-R3BbX9ZymlpHr2R69VOz1hrg34VEWPsgqgy4JFiwCu7VW_j9fTBXueIDhBiNl-PAKCr6weG1YzMRY5MpUxkVoYqBafV0fRw2CTwboszJv1WLXDNiphG4KgJ47bt4u8M5KjAQ1xudSatKXApmN1wRqBoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=TPcjfliT2TbmcC78yeJgHASr0N9KcjqU9FUb6zHhQWxDNqffP4KUkKZFJo9FHmQHrZJt_U_6QxRoiID2IHuTgquQomgN5vNcxuTU5qEvNXq-K7rspeHVc-pgjRLqjlBeKwEWHBw2-H7ApPv_pG7CTBeshg-jTZBB7Dhf5m08inH61ror4ArvWBDRpHi7MkDauoUpuazIxWEyDh8uwnFtPpLEB-r_HFXF0w_sb_4d4WnqTziMOnwbO3G0Pmedq2saOacnEojhHvM_Y4UP0rZx0s-z0z_aZf37PDBtmzpn0nNj8iEuzBYVmjT4zjrV0-4kh0dTSspT5V-AwLyf4udvXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=TPcjfliT2TbmcC78yeJgHASr0N9KcjqU9FUb6zHhQWxDNqffP4KUkKZFJo9FHmQHrZJt_U_6QxRoiID2IHuTgquQomgN5vNcxuTU5qEvNXq-K7rspeHVc-pgjRLqjlBeKwEWHBw2-H7ApPv_pG7CTBeshg-jTZBB7Dhf5m08inH61ror4ArvWBDRpHi7MkDauoUpuazIxWEyDh8uwnFtPpLEB-r_HFXF0w_sb_4d4WnqTziMOnwbO3G0Pmedq2saOacnEojhHvM_Y4UP0rZx0s-z0z_aZf37PDBtmzpn0nNj8iEuzBYVmjT4zjrV0-4kh0dTSspT5V-AwLyf4udvXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiGjw-6U_38YNc_3mjzgFTKg0QRB2BzUuuxyWooztGx06T7dXSrY4K-sKuYsyB0guVICFZBWEVJMJbFhCB4kZ1Gzf12LhPCU3NES3Bm95YanBg-1BDHChOwGRezmsSPX7APUV9mTORELnD10cYMu7tjEGuP_jJEnWDTe_2uBZMDvXfdqjtf9f7uME4l39zRSMZIa15PBITbqxwis0lcT-0J3xm2b4G2ELQkUHBqmUAq-jfAQNx1TCCLAQabNSV1UmIQhLNEejkWK9e8Y4D8JLOulKeU8E_sAJID9PVSBDBwjYNbX1TZd9loWIF9Hy6m27MTab9onE0_3zUlj2M8SZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5oZbuHYIS-Q9ko8DkXtvU55N5gfJjjjZuG5NallCrS-gpv4HVsCIVOMXWuSyF_pnx7e1wHVepZp5P7MaPKsNEt8hW1wjnsALb7e0hmCgu2BIuofwdwPwLeF9jVLjvNG4AGK52oNA8IbiEhwMnLOT6vn2tbEXb32oMtt_FrDaOvJHJSNsPs8aGciHbxQb3R7LDge2y70QOzAfy51aOmo80-M1rKvIrxf1A6_Im6taZe_ADOUpKrsqbckUuFDGPr0glifoYMBNMRDr_9rguhu6vyjD01P-2UyPIEK0hllLMQVhYk3guYabkNOgsiQvV3JRp5y641Eqh_B_yc94xqjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMtR75wQUsImT0XdvZJ2HGrQJxYqiAV94hsIZx6ytZdF1EoLR0wZOta12-j-HyMlZBn5Wr8YA2GPOu2n0elGsnt5r6PjJV3wkmpb-ykZtPEvW1Xjxy--XmOqI5bP1Xet8PUgjYiclbAXZYQJfzpT5IJDSzKMMSZpBHrBFAPPN863bUSlXYJI5ILHkPePI8Il0Z9i8oVst8VpZ5L1CO87Jh7ZkPYJ41Fi-QQ6hEDAgosBn1DOSATXgPaASVQYxypWsEXIm1Lm9Mxv6rIc_Kwtq5sSK7zxlmgehGX6maKvbfvMHQVf0_-nLjWVgeIcvPVg6oWRWP3tsqrUAr0fcKR88w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=i7LrzzPqQtu6nDeBotXM19TLpukBmqxotqv1g5ZwzZER1140l16nMNj9c7nx42tB1XxOAJxSeL4ZoacbxfUQZSnUgioWg0Njchr68hhYlwZm_BB-X72MMgqfVKd_CJSFzI6k6Ndaq5v_c2Ro0PGU_2BhTuI5lqVQtkBeIRZ45DWqIWYDId9fx4u23XjJcvCWawBLXXJyburZ25Xf0drcQFCnqe1j9NLpD7h83unxASuxW7SXEaMO1W8Z1o366OtxUVfQrtJZgIjuTqkiU_nkg2zhdF2o8rDS375SA509s13-Z5nswFQl_KqOSRxoureDv35XfNW1fYzzJYfOeh4QLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=i7LrzzPqQtu6nDeBotXM19TLpukBmqxotqv1g5ZwzZER1140l16nMNj9c7nx42tB1XxOAJxSeL4ZoacbxfUQZSnUgioWg0Njchr68hhYlwZm_BB-X72MMgqfVKd_CJSFzI6k6Ndaq5v_c2Ro0PGU_2BhTuI5lqVQtkBeIRZ45DWqIWYDId9fx4u23XjJcvCWawBLXXJyburZ25Xf0drcQFCnqe1j9NLpD7h83unxASuxW7SXEaMO1W8Z1o366OtxUVfQrtJZgIjuTqkiU_nkg2zhdF2o8rDS375SA509s13-Z5nswFQl_KqOSRxoureDv35XfNW1fYzzJYfOeh4QLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_4vvkldPxCsV1jHls0FKoyN7dS69QusevJZXH3fxwawhjS3F2zrf_T7znxs97u_BOdkn4Xw1g0YVZaLpE6WGv3TyKdiffJyUUaY_eJsHgF_zhhjJxi98byAPVsFV-sc-mC5TtzAZA1bmTg3aouh0HQqKL-dMZjUVv6Om0RfYZIOTpSt4oS2U_YlSvFYYq9W6nDKVROLEMfXNxJvzinGUEvqVVD95T7m6VQsuhbGo-MvgKYkFH_21x8UwuXWBqu-G8T9fnTpetk2pcvoxZ3QZnzwoTiMs49TGnVtW8NgdyUIV74BvL4at_k27SrWDVP-D_fuzL186f_5JFGk4mIE3IXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_4vvkldPxCsV1jHls0FKoyN7dS69QusevJZXH3fxwawhjS3F2zrf_T7znxs97u_BOdkn4Xw1g0YVZaLpE6WGv3TyKdiffJyUUaY_eJsHgF_zhhjJxi98byAPVsFV-sc-mC5TtzAZA1bmTg3aouh0HQqKL-dMZjUVv6Om0RfYZIOTpSt4oS2U_YlSvFYYq9W6nDKVROLEMfXNxJvzinGUEvqVVD95T7m6VQsuhbGo-MvgKYkFH_21x8UwuXWBqu-G8T9fnTpetk2pcvoxZ3QZnzwoTiMs49TGnVtW8NgdyUIV74BvL4at_k27SrWDVP-D_fuzL186f_5JFGk4mIE3IXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=jzKK-RN0E0tROR-742FtahXoqJFZ820geRctI6FrAncQYIiCQ5KjfzbFEmmsJYh4WQSkL40rHBkWC0WkNLkjmPHeCHro_Q1HOZ09Gr6xcL3qftxFRgpTqxWL6Ql4Bll0yyx6Dp49pBCE6RWXY8py7db_9Xv63N8WJ6eieAOUOPkpFPrKR8Hdjd5fDHoLFv_ddyRcHS23U_zsujWlHkGvY_m0WEFxhU5FXq57FQdYRAebM_UHdnAV9ONCVItSUE7YTKlr5p1FLDH8oCHK92hgOuKXq5Ad3TkqGzSJx9FxHgsmMRkdEf8VYRD2cA4UUZz6WH1biaT7Sgaq6cArUbpaRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=jzKK-RN0E0tROR-742FtahXoqJFZ820geRctI6FrAncQYIiCQ5KjfzbFEmmsJYh4WQSkL40rHBkWC0WkNLkjmPHeCHro_Q1HOZ09Gr6xcL3qftxFRgpTqxWL6Ql4Bll0yyx6Dp49pBCE6RWXY8py7db_9Xv63N8WJ6eieAOUOPkpFPrKR8Hdjd5fDHoLFv_ddyRcHS23U_zsujWlHkGvY_m0WEFxhU5FXq57FQdYRAebM_UHdnAV9ONCVItSUE7YTKlr5p1FLDH8oCHK92hgOuKXq5Ad3TkqGzSJx9FxHgsmMRkdEf8VYRD2cA4UUZz6WH1biaT7Sgaq6cArUbpaRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtxqnxHisIQVHL0F6NG2rmWGyb7YmJWvQGdm4Z2szn3Pl1qpXf4fS6Hg4_BHAHXIgoXF3_9RfgQix4o55L0wSMemNdftBKOTc8mJSfAxx22BuhwCvg5phiTw1If2lIB_rViYc0PK9upSt9rWWAyZv6cpYcMz7ND6B2Q73N4M7T0ho6oNoA4yZJc5Mce9Z86gd-GKwn8EIbQrAAVP-vg1AVw3dwRh2iLlqmDrsxWzwR2hNIPM4Bww9eAIkkkoJpjz9bknxeRM-JYsZQxu8Ro7Mrphg3hOxjlerPYYI3YyiusM5fXqHKjQRWK1uOHNLh0ljozf117S7HjuyumjGGEQLA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Rl9wGKe2tPFnjyokhCALdbf7SS5tRcaeP27nBzDdg8lEKtTJuC_XpXbGzOqImbGw76Hyui45yfSBbs8Mk25kHJ08xLbAS_GHQFmyLUDfvxSy8BKA7SUbydNghqDEO2DkEAPSdcMxMAEDWIH6kLYtC7DdQgmh5JWErzRlesWU6vlvGc79k7QbqG8hG1Jt1FkMMZJy3BwflFYuwWs7AsNHdKENx2TKsBCppTSH3an8tWMHVOMcK8bO8-h9vphpRm8M8-AdT0tJeEPA9Z4Gpc9d0PO0jh5g0kkoCITvupSBfz8NBF42e_8I0astKNjH0flQ8Enc3MQGs_hFmCz-1A_DPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Rl9wGKe2tPFnjyokhCALdbf7SS5tRcaeP27nBzDdg8lEKtTJuC_XpXbGzOqImbGw76Hyui45yfSBbs8Mk25kHJ08xLbAS_GHQFmyLUDfvxSy8BKA7SUbydNghqDEO2DkEAPSdcMxMAEDWIH6kLYtC7DdQgmh5JWErzRlesWU6vlvGc79k7QbqG8hG1Jt1FkMMZJy3BwflFYuwWs7AsNHdKENx2TKsBCppTSH3an8tWMHVOMcK8bO8-h9vphpRm8M8-AdT0tJeEPA9Z4Gpc9d0PO0jh5g0kkoCITvupSBfz8NBF42e_8I0astKNjH0flQ8Enc3MQGs_hFmCz-1A_DPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=UkTRW7E79Gr7I2RMrbwfCAi9MlrBqdTk5qHC1IrPXnL5ssV-L2RR3fq9_bHgdNFXYCGcxU0s6ldm1bIem4f9dRJvH5fxcqA3jZdzQl826Ivm-Tbe-7cYPe9YH8_ZBPSd8NlZg-uUewo7PBeoRMbHJhCqzgBerDKNwZgb2xR9m2J6y1gxpnXy1GejBBpDx_mJUuHwHtMbjVsAGX9UW1tFOhE2vYeBU8ntHpXZeNeEjmpFV5WbMIzoBP0v7L7JpXC-C9gQ1ZvGdjSlzMNCqTKh-3ga7brQPiMzDF9nRoBZ3LZUwY9LerdMTB-z058msQz392egOFJdC0Nfp1qWUW__TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=UkTRW7E79Gr7I2RMrbwfCAi9MlrBqdTk5qHC1IrPXnL5ssV-L2RR3fq9_bHgdNFXYCGcxU0s6ldm1bIem4f9dRJvH5fxcqA3jZdzQl826Ivm-Tbe-7cYPe9YH8_ZBPSd8NlZg-uUewo7PBeoRMbHJhCqzgBerDKNwZgb2xR9m2J6y1gxpnXy1GejBBpDx_mJUuHwHtMbjVsAGX9UW1tFOhE2vYeBU8ntHpXZeNeEjmpFV5WbMIzoBP0v7L7JpXC-C9gQ1ZvGdjSlzMNCqTKh-3ga7brQPiMzDF9nRoBZ3LZUwY9LerdMTB-z058msQz392egOFJdC0Nfp1qWUW__TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=mNhDavGE_U4ShSKzqmPq8PH5P9ZGiovaA5A54Yq55nsbWq1V68dArmR8EXY490ZLIbnI8eTq6tcAuwJfrFmAWjz2AL-nd-Sk3X4a45sNBelcfE69s7IQFugi99hFNYaDOVAwtTX8HtaADyKMhwzAw-GfluqawTbFYqjOHLIhKGIG4tYGrDtukXgoM9k17FPeEc6ep4QE0HoAXRDiOg2WLWvPXdON5KfxRBOp-nBPs4zYKVTJlJvLZ7rcDVQVafgpcRScidVmd60rrZ4lx5bE2P131E2QWvgZD1aErt4S_LeJm3w61Igpr_9ZFalg_K3D04jCbKshcbhx9pqE0t-WcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=mNhDavGE_U4ShSKzqmPq8PH5P9ZGiovaA5A54Yq55nsbWq1V68dArmR8EXY490ZLIbnI8eTq6tcAuwJfrFmAWjz2AL-nd-Sk3X4a45sNBelcfE69s7IQFugi99hFNYaDOVAwtTX8HtaADyKMhwzAw-GfluqawTbFYqjOHLIhKGIG4tYGrDtukXgoM9k17FPeEc6ep4QE0HoAXRDiOg2WLWvPXdON5KfxRBOp-nBPs4zYKVTJlJvLZ7rcDVQVafgpcRScidVmd60rrZ4lx5bE2P131E2QWvgZD1aErt4S_LeJm3w61Igpr_9ZFalg_K3D04jCbKshcbhx9pqE0t-WcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npi4cTXY_3ZJVVe4Dl0XZj0yZoIxjJT3t8OCHWwpC82i9QlvDfm4ThKjTib0QuZ_TAX4eJPyFhX-qAXCpstDpQ11wGNQlKkN0wYtww3I6cW7HiQJkKd30kqHMFxwYQBwTbCZkdwmy6yCIzQ9ARbogVTFDJcAWHmOPcDpZYf0pKvAeMG5cgeDU6CoRJMRlPXqSvAKIVLUuGx2bBXAIKL6TWA3aWhWufkf1A5i3eRdIJumauzWhc0LWfzT1_TDtVv5PV9oAuvu3m-Zp-1T4MYEBL_U31q2e1_GuzbDU_zDj1RdMZxgmBg6UHrXY4Wpz3YKgXqQ_1yUSKa0CNej75Qqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
