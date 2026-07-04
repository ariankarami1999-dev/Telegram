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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 20:24:41</div>
<hr>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDASMZcBjsX8pVC29QjL_4ztCNVEGcq-yvd1QJzDoaF342OTBcBoFk2NfIR82XbQPsuzZjkT-C9FMf5xV4E_XXZApPjGyCKKvikvK7Nu9it6zzBTF54fLKqvxXaMkEfE-PIc-oJYGevsUK6kPUpp2pFXPjH7hBFBChTTHFO3CjP29B2FqF4eA5MjmDNK15ZD-qW7nHZS25UdutvHn05XYlJB-B6li_suQiXz_lXMcnu80AecHCIDEPjXqpBDNey_D8CxUqxSyABr9IYdu5oIptWTgQgYEnkU5iKxnjtm8T-ildHWHbsid4K3-FKQNabSBf3w_uUM25_4jQVdXtdXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W97W8F82Y13uKVNgDMtr0oex3CKAzhi4MIkI0Ktfb8RTWlLzXHpg9YFxZ-tNHd9OmJiHOuBrj9vhn5L-1FqQeOVzYzJzuJhj9YMxM7gLWrk1J8AZe9o5zlyTwApr3TIIP9cXT86OTd-h9yp5cB2TI21an6tRrPUq0gRNQozYa6YbACDkpRe51onDcQBcNitKPHgz0adqYzgrOkbc27-1CgnABWVewDhRDtchIHfwEanbDP_xrdOcKAA7vbhHGACM4mE5-ITmHVI9qPc4c_wFTvI9FAfJA8KzE43fae6RldLJGrysFUy9Q8GNnDrDx_lyLvNUmmBVek4ePMMmWxMX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8uiay5CQ6sA4NMc56qf_NOpv-Ne8jdTf9saZuJ268KMcg9hwJqh2UqBe7HzGLqLYFbbAFy6-VhBduxhLlAnmSgn-Z3OvXPOjhlHS7xK-8gEGS4C4wXgSkmzSTq9s0Z8EskVYR_TfY2C_rWPHGhfxKR1KufZa9yEbdeL0IAKhcyv9TsZAzoVZjWacVK15d363Mi5lnycHZNHuRCsjqP8QsyzaiU1TRy8Ba_UmLpDINT5VnPA-VFJ6xfoIQ4w4R05mFa5LtFMXt6LvEDIt39JQVMb6t-4VOJOYZ--Wrvwhut1-OocxribDH6KMQ_lrf66IE_kWacGonGrs85rv_12jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5TWc-vGDHZ67yrpwin2mUo36Vqdc2Tc8Tx30lMjD4NfdI8w-_jamsCJ04vfWdAC0LS_jx3yIulIhTCkIE20vDk87DUHrQQX5ETjn6TKodhiAE44KR6Vn2ZZWhhY009UFwSCM7ulqhZ6eaeva6_2nizoDl6AHrWvWpSn5kCepmoScDimTSiuPQdzXZAZXDzcGcjnzL7SKcV_Y1r-xnQ5wDrma1QdsUt9iYeHEGGd6SciMp_GxCtUPS-zRfeooVop7EUy6mm0W8idtgFsQ_UoQdCiSLAe_ILYyZ2-oANJ05V6Op5tCMhlPK-qQkEQ1UAtqfkgqZie4q2oyLJAHWKKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP_8nvFhLRM3DaFUUS0Xi-ExTwy7llwc6MNBYCj0nwkrc519PEMzU7o3yk2HsyX5lFDTCoN-zfjiLkNbHX4WGecI59y-B-4u4DzZqKajyCWnRhj1z98LvnTjEGmBIwRNwiJibsAHfnYMhF_fRFN9qq-286MDDb5M8Ta-hSN3sjs2OdDsC7Nb18r13zI3XPz8ORcGXQlly56f1_KccC7nRxV0WMTsN11WhCDJ9rCweRuvnIF12tRRX2ZMeX0JID_gBFX2_tqRpZOweaEcNvqqTej2mIGN1yXX7oX6L5D4Qfe32HTNfzHe-3RmWt92oG6LLfyB8ujR-HobUyWwl1seSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DehDnHEQLxKJViIQHJJ9thHBSBglHjatbEwxynhVs5RZVNF7LP0Exg_poMyR_ZU8RQthqyzYcGvQjPz5CNppEa4fnsFBZZDLnWHZ4Y2Uz7gozzzcOK4d1lbE4YZTfNtkHmfYK1SvweIdGJyotS8XDptFyHCvQDKgiEW1ZrjL8XYxDBfv6-GXb6f1Y7i-LWj6DmRiEmiQlDMkVFn6rIbS6MCiY7jIO5PYcINprEm1zv1LfjO9pstuFdS5WOQ6JMTLECR3WDasvr6Grf1q_wAuB5aaXWZBiAZ0RYC0d5NGUmzFcoho8torevHEEjYZLn6Q9ZzjlEkNTKaIi7rmYxtagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhYa30e0GmP8bk_E3znjbCYXOAhnGF1elybGYwIB2MkVBJU0O-7p3WpbEYzGlz6xK_bFzZdt_xce5lSlgzBWlKyagnOu1GszMw0bYKZkRIMRH7OMgjCSHoYjFgnXiaZeIPbywoZbdy8dKe7-aWt9tc3n52ZTbwXAT58xu79AFHYpNyMGo-oFWGFNshU0-6tpU_e4-tgnhHms-_pHptm1ekO8m_mhMK2QIoS_y0aWtj6qUVa-hgTV5TyKrUcUyKE0zDoNgkpT3NbbSV_ygru_xpJ4wGQh_pogC08ngr0zQ28zAWN2SdSAlvYSqbNKupljq-7dNaXF_lJcJcQPAo_4qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFt0TpODGR43HVLibtHtlHY9cjTX8EyvIrE3Oom-Zfz7u-F4qfTgNVTmMUKKSf0q50JCcFUaQIHfLKZ4jRAJRJWTyfHQ0IWx-4kHeV32m_f9ZZudUYZCeiqpOz5kitcO9hRapS-wiWIOfluFp_Cu-dVrTOm-6j3IBmDHorTN50ua-QNTXl-zc0N505BYm5x0guDP8AA4SjO_HXcA4YDXZOyjg9sChl5nc_kPJU0QPWEC_ca5rjCTjZhKw19nYSaihi3lJ_eVDJo-p8WUUegvv5I3M1f3Dvz9p5sDf8eedK9pIFqhm2FJJ2U1DgsgSsMiLHIpdRcH26BQYr6pXdPV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBXhVmP-e0U9Xk9teyNWUEYXnCHSnSZSKCXhXD-YN7L3lZlUwEUlvsJoLf1ctPBxO6vhi89b-WKyXk5sgCu2qyKYh2P9geQ26vpRFG9aUwBFbcOk-73f94uleBXPxcOqELB1Jcg-9UrAXywzf5wvFfk-zBxAKGQqeZPA2XAPTh3F-aofSuznqIl-rBHzjg3FvXXCX8lWmQFzVi3IZRPAJTQKujKnMA0AUEar4sS5p1QRVADUT5W79dWZuE0kG2LLDW8QV6aRztq14aGGJAtTXWV9fcW9oK_uLGb_piek66UrPudOjfi2IMEj7MdrVdaqrNM37Hvlg2s3XUgmOFbRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsQ1s3Nv__Op1Yr7-c47P83H5FDTQPZS3BGQ9XaNe1SlmdhpIWngxojMV7FS_aHtOo-NhQcPzYdBJ1nwz-s8QdmfTjS26esgtNtRlC4r6kn0zdHL3secI0bUB1ugEUB2pTVkabWWJSU-cT7wYkENazHBZWIZl0REIdwHXAidE2rtbag0QjzErqX8VbBe-oG_GOFk9rk-GloQg0_rrKFk6Y6Bvj2k2bbrnECEBf21bAZ0Sx1yRAZSKBHF_aESjon5IyBl5XEw1Pk3S3od7X8YmLBwWk0_Pdaq0JyMR_z5hmM96yDeyhDTvj4puV5mCj3jn9mJUrFh31cDwXVplnuwJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=JwuLnc-uwXoFcF-GtF9HTRrU5rhX-1LHyi8JAGdl7J3Mq4Y5C6aLpANGg1IJDtTfrXhJLYjSXbGsti7qq_kbIiskTfdV9qhZOb4OxKIe9FT-X16xSDkQ1LX8hPH9Vny0IgG588sc6x3IRgVCHqklu-H60zaRnLgKyubtuwi6zBoD4Q253F6ymeP2MJ9r0ZKTTr8t7AU08erRTeqb7MOSVMw1dQ5Li3uGiAvfjWOWOnDcjXGbJbSCkUGi2m2Fwa7ZVjUTddnjKVz7Zaro4GGsAVLbjvoyLKpO3z6E3ztKgjEbNQtcn20YZuONHvAvsNRAmog8Ol_vkExqgJXX8bRUDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=JwuLnc-uwXoFcF-GtF9HTRrU5rhX-1LHyi8JAGdl7J3Mq4Y5C6aLpANGg1IJDtTfrXhJLYjSXbGsti7qq_kbIiskTfdV9qhZOb4OxKIe9FT-X16xSDkQ1LX8hPH9Vny0IgG588sc6x3IRgVCHqklu-H60zaRnLgKyubtuwi6zBoD4Q253F6ymeP2MJ9r0ZKTTr8t7AU08erRTeqb7MOSVMw1dQ5Li3uGiAvfjWOWOnDcjXGbJbSCkUGi2m2Fwa7ZVjUTddnjKVz7Zaro4GGsAVLbjvoyLKpO3z6E3ztKgjEbNQtcn20YZuONHvAvsNRAmog8Ol_vkExqgJXX8bRUDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Ji7N9enyNgk-3uEzCn2hHB1_q5XqsOHRwMGcmcUZ4G6Rk8nAjG0O7L2x6p2e7YNpGMpM3fTYkgoRa64km_jbxjbSrbLjQyDRUieQtXnIDmJKACNFJEHC2-7dmlq_K2w7oCojhESqkOJA__A-00JZGBbW46BbR9Ntj2_IKT7-zQXKNy2F2jQ3AoCelLdbmXFv0z1az43vrvux_WK3CXGSabqYOKfQBVJxg1V1dkHc1tLIRbkci_FoFyoE4yVr82fKo_6JBmpx0LqokBsVd4lseeN4pgLhcCAZSpBnKw_mrvU3R18OfjNkbYIaBm1or6-TUx85uO_nwonAhdsSNzHGCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Ji7N9enyNgk-3uEzCn2hHB1_q5XqsOHRwMGcmcUZ4G6Rk8nAjG0O7L2x6p2e7YNpGMpM3fTYkgoRa64km_jbxjbSrbLjQyDRUieQtXnIDmJKACNFJEHC2-7dmlq_K2w7oCojhESqkOJA__A-00JZGBbW46BbR9Ntj2_IKT7-zQXKNy2F2jQ3AoCelLdbmXFv0z1az43vrvux_WK3CXGSabqYOKfQBVJxg1V1dkHc1tLIRbkci_FoFyoE4yVr82fKo_6JBmpx0LqokBsVd4lseeN4pgLhcCAZSpBnKw_mrvU3R18OfjNkbYIaBm1or6-TUx85uO_nwonAhdsSNzHGCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=gbubGP6fuVRI2ga47kb_gsK_ADuvz-2r-NcG9PkOzj72h7i8IM42hLbhvEgUfMDV0Zr7kSNMD6-Hv04gCrYIgv1mUpBIJ6U4Os91dffIEpopWdw2MCkpNSFZq6LYo8pgJAJSdRij2aHdZjOkrESI_EjKfPhLoosmGgfGkgRdI2iJm3jPEH20neHS3kHJ3LeZHxbVkcljgVcwCyZij1QPd9FpqvEN5GsxDQpoqlNct5SgwHAf7QKGdhbzijiIhg8vqA-GDRlZNu_uvlHCIV8xPEq8g2Y79giPokM-khKZaT_hRdrsZIM7kPtByUEXVhlIWokuA3q9C3iECiEpA1BLVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=gbubGP6fuVRI2ga47kb_gsK_ADuvz-2r-NcG9PkOzj72h7i8IM42hLbhvEgUfMDV0Zr7kSNMD6-Hv04gCrYIgv1mUpBIJ6U4Os91dffIEpopWdw2MCkpNSFZq6LYo8pgJAJSdRij2aHdZjOkrESI_EjKfPhLoosmGgfGkgRdI2iJm3jPEH20neHS3kHJ3LeZHxbVkcljgVcwCyZij1QPd9FpqvEN5GsxDQpoqlNct5SgwHAf7QKGdhbzijiIhg8vqA-GDRlZNu_uvlHCIV8xPEq8g2Y79giPokM-khKZaT_hRdrsZIM7kPtByUEXVhlIWokuA3q9C3iECiEpA1BLVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=gu0FeHG07LyM3BDzP55INRHV4mRfXBTLIjGw5PQr9UZhI0AWK_Xy0XGjWK9LjsBR07ICGIEB6z_6Pvvl0p_TtOs731A16s2-0A3Ys3TnouX6ITi2ftZnWCQq1ZoAKgd03cg_X0bNf3P1DPog84gUjljiG3QX9Db5emS3cA_zaMkPQDIjOSg_r9xrWVprzkLzMQUkeckNAo6vRzYUHTHGms_5aDkuRs9cPY1m5gMvtp_Xr9Tv2bzsxAh1OaJH3ATaNnnbOjn0uU3gPryjzSRhDJhrgsWpSgPQkp7U47xPAhtnt14lWVHnQAS0z-szYvUaNT6aIUzP3ab1jKI-ycGGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=gu0FeHG07LyM3BDzP55INRHV4mRfXBTLIjGw5PQr9UZhI0AWK_Xy0XGjWK9LjsBR07ICGIEB6z_6Pvvl0p_TtOs731A16s2-0A3Ys3TnouX6ITi2ftZnWCQq1ZoAKgd03cg_X0bNf3P1DPog84gUjljiG3QX9Db5emS3cA_zaMkPQDIjOSg_r9xrWVprzkLzMQUkeckNAo6vRzYUHTHGms_5aDkuRs9cPY1m5gMvtp_Xr9Tv2bzsxAh1OaJH3ATaNnnbOjn0uU3gPryjzSRhDJhrgsWpSgPQkp7U47xPAhtnt14lWVHnQAS0z-szYvUaNT6aIUzP3ab1jKI-ycGGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=sQcoUlwUwOTfeDifsnOHDgg9AjH0rOxwcxvochWkkW4hnp9ppMnPxA9ra1j46mKO8ZhjEtic4YsvEQRBVS2GX8-j2JKah3u3mt4auJXfAqkwex8lNJi218gb_zysOiUdTMtuoCLn8ESc3FKV8u-2bcsF9ul5nQ_Bp1YDUXFAZi_2xopU5tgFAGXEj1BtEgFY_9Jd-80EwZq5zxoykpTdk3ynaDOz6OJl1sydWhabU5fPU2nDFoGuwc-QjJypgC7RtbKpLBm3xsH-IuLD5RBvVObzKbyjK3oFWIRMKtnI3iAhiN1uujytQrQTKU7vU546dDPP37mXyrU20LkpGkyKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=sQcoUlwUwOTfeDifsnOHDgg9AjH0rOxwcxvochWkkW4hnp9ppMnPxA9ra1j46mKO8ZhjEtic4YsvEQRBVS2GX8-j2JKah3u3mt4auJXfAqkwex8lNJi218gb_zysOiUdTMtuoCLn8ESc3FKV8u-2bcsF9ul5nQ_Bp1YDUXFAZi_2xopU5tgFAGXEj1BtEgFY_9Jd-80EwZq5zxoykpTdk3ynaDOz6OJl1sydWhabU5fPU2nDFoGuwc-QjJypgC7RtbKpLBm3xsH-IuLD5RBvVObzKbyjK3oFWIRMKtnI3iAhiN1uujytQrQTKU7vU546dDPP37mXyrU20LkpGkyKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=sJyl6uks-zo48B9l9nZdyABYqkRruIAG-d45zSGVzjQPegcjl_JLS4HPfK--tWZG0msSEatc318Q74Lj7SNEdd25M4SeJ0b70CnukUIV_1JXPIJz4dJQU6fJIZW1fLViOWGy3pUthweBgQSIIakSWOEtjomLHGYvJXKMIcxR7NAfCC_JvMc8muqH1YdmPzlYJa23xMH_un2WctUUNijAIcPWVaXBcH1a77czzEkFu2VgkwyENEmektF4k9AYiV1mPKPb76zZ_DLRfsFWcxRs9Jx572-bEBEYSiGZKVtg7ctlpC0h5B80wm9vdVmQ2Ze9f515VHRlUZUPbHQ69uhhOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=sJyl6uks-zo48B9l9nZdyABYqkRruIAG-d45zSGVzjQPegcjl_JLS4HPfK--tWZG0msSEatc318Q74Lj7SNEdd25M4SeJ0b70CnukUIV_1JXPIJz4dJQU6fJIZW1fLViOWGy3pUthweBgQSIIakSWOEtjomLHGYvJXKMIcxR7NAfCC_JvMc8muqH1YdmPzlYJa23xMH_un2WctUUNijAIcPWVaXBcH1a77czzEkFu2VgkwyENEmektF4k9AYiV1mPKPb76zZ_DLRfsFWcxRs9Jx572-bEBEYSiGZKVtg7ctlpC0h5B80wm9vdVmQ2Ze9f515VHRlUZUPbHQ69uhhOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ocatlznq51e7_EMV9L53YYZYvZ0MlVcTOEX-UsIPFNqIZDST_QhjnnK8d8yBFyggVFQP8O9ACeoVwQA4ioe1TQYTAoCH0akxxtSDAXlfGCMrXBTSjtb-0VO02kERsZBJTLMQBa5JtVM5yIEyoHQ_QjAMHPYj6zJkbSUg1vXiYzIk5MHli2IaIRjChzwnFKqNvGJBsXannpZp4a7wRCFFdScEijLJRFT9EUS9p0ewHdiAwsE7AsxK_wO81Eho4YUZHeof9g3QfZ1Wr3muPe-IP7wUW5zf8nddPz2N1FUyo6KdtM1tNaTxVhKF86a2RdYVzaaEgs-33_jA08QhcFwK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=AfUT7M0h4u6-ZwD2de8lsSWRf-nnGo0RqFIzSrptwHwHG-qVNsw37epX3g86v-5r6yxxES1lfW6-iBzdPQPZuoMS9xs-drDzXSrZRMu2jAdfP5jaHsV2bTh6wHu8QcauHyJ9dVF5SC3wwhlCprsfM_jBBUP_3oobd-TI_6UG7SLwMZc_4bnNbjBoSFEp-fErRzeGwVi8j1uFjiES6f-Dnf1wISukcqU22MMtdX_a5jFOh7OuwAX2y2mZwt64-_7op6b7eZqGOgrVUoU_ZJmSLH4fzgqeLoyEvEaiZgr4BExmBSfHafTgV6lzqo5FbL9lnbUWMd66lRM8A-4FEEgn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=AfUT7M0h4u6-ZwD2de8lsSWRf-nnGo0RqFIzSrptwHwHG-qVNsw37epX3g86v-5r6yxxES1lfW6-iBzdPQPZuoMS9xs-drDzXSrZRMu2jAdfP5jaHsV2bTh6wHu8QcauHyJ9dVF5SC3wwhlCprsfM_jBBUP_3oobd-TI_6UG7SLwMZc_4bnNbjBoSFEp-fErRzeGwVi8j1uFjiES6f-Dnf1wISukcqU22MMtdX_a5jFOh7OuwAX2y2mZwt64-_7op6b7eZqGOgrVUoU_ZJmSLH4fzgqeLoyEvEaiZgr4BExmBSfHafTgV6lzqo5FbL9lnbUWMd66lRM8A-4FEEgn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4txVFOAPDTZaned2BStyp6LjYyC7P7d2trLsfRzZRCBizbTJaH-gvzF26WgjU2mduXh1cAEY4eDc-JpIgeCM87HElunNSdL77XFLcezbY956TOd-uo-u6bw4KndC84fDT4xa5r_R70qYbr8qxM28Sjh96O83ORABiM3nb0pX9eEJtWhiYRJNSjKbukUQzKselBooG0ct9a7xd13gVBsOpOeuqQHoZTKN__ccn_qfAtFQ9YP0ZLKXqtVmxnpg-5OAEN2G9MJmVMNj7RHehfm-16piZK2jrvhNH9eyUCfUyoFnZLJjraYEu2UZAE8YYVDe7N5EU1EWHF3YM2-7bhpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KC1plRuzVMyzGrbDheqweubDpaSIAx5xjF3AvSogqGbQ6b3z9MP4A1-2nnoZ0LFyHkLVazeKnPfDmq2VfqP_e40IQRrrnoB5SKvIiz2E0A9_LejKTc7soLowlaegfbw1772ir9xVEjC4_omKlB6fEIMgkJa4e4O7bF8BhHEDQcTbBUXhrwCHx5oc24b0blNQfciDBqr6dBclk10olwxo4Zh4hBRkn5Q-sXhn1H0Z_mnmxWhj2vFklk0PmZNUvHRBN-F0lvs--Uk9gxtBKnOoXzUuwWKOIg6XX1gIIuIKQreYYuXXw99MlAXxpS_8ScNiW8ZJ23MaAvneA74wS2VWng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiiPxXcgRRB12Lr7WgCb2nmMwRSyvlz6qJfIlX0-OBLOVJfiRQCtIy54u6lIIXqzpKwtkeBWZVz3hsYEDKLE1jXhKGcP0hTXHMuY4BwIewPekeICgicQfxKSsNUz0eEtKXfEaYq1mQED0sKcstodffn96baBNWfv9ieFw059EuWjW4VVdbEREXtvQg83K-5Zv2C88VBxFJLu9BTad8Dmccz7EIRpVGKVe_SnkfoSAfLmBjXBNpuAUfKL_pd1BEJXMg9hhHxV7tcdVu8okfXKmIjGrRqcH0r_E5mLWNDmideY0yllaENvDzfB9e3kAHGQ73OED89qYS4tgmW1nYfjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHNprl7CT8wswa9GPrCSljKv0jA865FVkUwTxqwAQztn1iFZ0XiL8BXrICTDfu0oqo9hC4b6XIu1Ouu7iuinHGMJChjV_E8BBhsWjs-nGfjYu3tHLcIk6cODvzhsVGTCUIdDVNNmPk8VD9RkFbta_hBIfziRywzWG8_oOrTVbvG8Nd_tStYHVZj-KaSuSR2nVthHWvDAw_Zz80LfbxnHGyKmyjKNImkO3vD6cQ1DSXdaAGMxYhA7LqccKzTsMjU5_PK_KHK1cjj_h_kBD6eaGFsD2Wq3kfcTPbbGRP7xoh9XiLqscy-AREA2YnyD8CdYRGfw_fC3ETTfpuT0znYEXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUd5aIMpKMwmUz_hLBBdB__oMREx--s6UGlal2IFY8EB2ot9UpAia7wpHONYfFaYpA4zDfVxRW8L0Nwgq0yh8j3bpRTKVW0EGg4f4nXzRImwvuJljrKO_434SyFDJ3jvOOYNPs-DNRHvIaj_iFbrJbscVteDI5aYoEK-2HBtpNCMlZzk39kFKZyBuQMrkuiHgEk3YJ02VSy21DpFofIjPrAFBGZqzZP5JwqUurTWUTqY2vvS15lpAqAeJll_8Xfnv1OqPT-RnVLtfnxGLgiD8Hk8gcVcScGtgIZPcblQZN8-g7zP7b7cSfY9eb8VvNxwHhhNytc5O1nFYySZcXMAcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akO9SQ9K4IVGQSgp2NfY3djEVlio0NjvcNowDZSAuPAilyffs7tqhCyhsZpE8ttwuv-k_mRXEtSLBxsY3biqz5pAYSnDS2uM_oWiEjILXFbeXrtGO-EHZuubTSjftNGwgPf3JzS1ooKL2G_tvOCkwtrKc-KfhHp4OXWvtqfvkn__HNsEmO0VvHPo0Je_5NnT07ECL9oqgA-B23K6jhXu9ZrTfQoSwOkGi22WcaPtH5XzZg1xfw6xA5T787dDCwvrOiWl4vlsDCn98OUkY6wabfgKC9SGo5wwN6iDInFU1bl5zcCKItSD7NB1t3379JXIQhHbqS33NJkOjuDE_xKvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=uZhgmhcaHQdj7E1SdXd1Lif3D6H0yIwh5AuV4EhsEvxZsWwMcHsD5ry91Gvd3SDyL_X29uNmtZzGBFWqHsHjUBieTSWkXO1j7VYQMFBbYVQiBdS4c2fBbzZgkmEf9tawjMuzKciDdxVYNpmt03RNqTKD2i_Vi47GbnKuyASTRvBHKMsAPufmYSWaVnFjIi5iyuExtAMnBv6JQgBjq68UEJlcio-5PVN9E8Q0jtfZT1KNFt4tCb_OkBg1DXzHp4-QhsWOZ2hOXNf78jKsOHfuT9Gts9ZRN_58Ev5nP-hn1ceBRGb0o2ikpayDSEq2yfHMMQJQ6TP8bMWOGD4QUUyVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=uZhgmhcaHQdj7E1SdXd1Lif3D6H0yIwh5AuV4EhsEvxZsWwMcHsD5ry91Gvd3SDyL_X29uNmtZzGBFWqHsHjUBieTSWkXO1j7VYQMFBbYVQiBdS4c2fBbzZgkmEf9tawjMuzKciDdxVYNpmt03RNqTKD2i_Vi47GbnKuyASTRvBHKMsAPufmYSWaVnFjIi5iyuExtAMnBv6JQgBjq68UEJlcio-5PVN9E8Q0jtfZT1KNFt4tCb_OkBg1DXzHp4-QhsWOZ2hOXNf78jKsOHfuT9Gts9ZRN_58Ev5nP-hn1ceBRGb0o2ikpayDSEq2yfHMMQJQ6TP8bMWOGD4QUUyVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Q4kONRGnfkZGFo904_HQSTWaKnh4mqXzWmbsQKEvpaVJXxcMWf7_NRa4n5G5AUG_nrEKbOtmPI3LdtOllxSn8uq127GhdNmOmXOuLHFCzBFDvZq2LSlQDQyMu9C4qcIXoSrmNqKzCmmJXknJ3hNslqYB0PwrwkoUQGoERL-A4OS5LTwQVzq-OauE71K2x3SITNuSqkTFRkUdGWnAp6IUF37ZWRZdu3Un39fjiXeMQtRYWEx9aecFeb_8jnLcONPar8edJQZuKxcj9QO3KphJel5YU2yYDpJn8IGVXP1T9vSs4jV-ZEvX_JYZ2J2ACINoI7jnKJg3D9MdUb33k3k5tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Q4kONRGnfkZGFo904_HQSTWaKnh4mqXzWmbsQKEvpaVJXxcMWf7_NRa4n5G5AUG_nrEKbOtmPI3LdtOllxSn8uq127GhdNmOmXOuLHFCzBFDvZq2LSlQDQyMu9C4qcIXoSrmNqKzCmmJXknJ3hNslqYB0PwrwkoUQGoERL-A4OS5LTwQVzq-OauE71K2x3SITNuSqkTFRkUdGWnAp6IUF37ZWRZdu3Un39fjiXeMQtRYWEx9aecFeb_8jnLcONPar8edJQZuKxcj9QO3KphJel5YU2yYDpJn8IGVXP1T9vSs4jV-ZEvX_JYZ2J2ACINoI7jnKJg3D9MdUb33k3k5tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=KwK5XuEoOaIFQNKaq5qeT-kVTODrU9eXhORtDM7zfrnYycdHu3lZdbC9dJYQD2-CMmY_Sf1X7WtnrbKqRAXehowZ_tMKdRvR4Bk4s39t5PTBjvKvEOPyAmIfpufoZkVUff1jAxzKBXXDVoulOI2Yw7z5MEQCc84ZgH2PHOsyZTiQbXEQOq_cJ5DiLdstIS-CSAZ0jOTjV_De2Gri_b06bcV8uo-z3AQ2dIJ0Gc9WlouB2WsApincsqa3ULUEdPlMJZfuOnVrqvVvBAAh7ruRgZgyu_D0oLocSHmikZQbpepY2GDT9gZaFEWIFOwjbnD5UlbPCFIQPebNvXNzThV03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=KwK5XuEoOaIFQNKaq5qeT-kVTODrU9eXhORtDM7zfrnYycdHu3lZdbC9dJYQD2-CMmY_Sf1X7WtnrbKqRAXehowZ_tMKdRvR4Bk4s39t5PTBjvKvEOPyAmIfpufoZkVUff1jAxzKBXXDVoulOI2Yw7z5MEQCc84ZgH2PHOsyZTiQbXEQOq_cJ5DiLdstIS-CSAZ0jOTjV_De2Gri_b06bcV8uo-z3AQ2dIJ0Gc9WlouB2WsApincsqa3ULUEdPlMJZfuOnVrqvVvBAAh7ruRgZgyu_D0oLocSHmikZQbpepY2GDT9gZaFEWIFOwjbnD5UlbPCFIQPebNvXNzThV03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=bJfYwbQF8pVGZWVxsQkZHo9jfsPnc5mVlybGqEFuBvd44wHC3nMc8FSybBDuikSxCRRvnWcflrQB9N2nExUbxLNShhDgY3pwLHxmHHiNgTlyRfrUVTkV1iZBHCBsv_pRA0LXs94JUFEYVLJ7hDnCkDNjyiq13xyc-rlatcZohjcnunHP-vkSgI9m4UcVa1tXFHgfAlaFnIRqYOyxABY94_Jd4dRGwnBx8IuAa0anBpljS6XybY4Q_J-JI5-EWu081EbIEVAwiPMYOI8c6frOP1eZPQzX6wuHsZ6AYXo3OeO_SxO80YZJUP6NvGiFHkOQuf8BcZZO6vlo4VQxkWqtcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=bJfYwbQF8pVGZWVxsQkZHo9jfsPnc5mVlybGqEFuBvd44wHC3nMc8FSybBDuikSxCRRvnWcflrQB9N2nExUbxLNShhDgY3pwLHxmHHiNgTlyRfrUVTkV1iZBHCBsv_pRA0LXs94JUFEYVLJ7hDnCkDNjyiq13xyc-rlatcZohjcnunHP-vkSgI9m4UcVa1tXFHgfAlaFnIRqYOyxABY94_Jd4dRGwnBx8IuAa0anBpljS6XybY4Q_J-JI5-EWu081EbIEVAwiPMYOI8c6frOP1eZPQzX6wuHsZ6AYXo3OeO_SxO80YZJUP6NvGiFHkOQuf8BcZZO6vlo4VQxkWqtcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBJ0peADZY5r-JXWvRjpTP5N-TeOCODLwgEEx43GSOFWJdndur9v8GnaD6Sy4-F4qwYqBV3bmimCrkfgZb_7bHEV0_1ghpqu_591AsIkzKj6FP530RxIPyrjG4hmRL9twf-PlnetpEjAXpmsCJ7DnEInuFLUpiTeMXIpUzRrXngUkJpBomSvbZno5bUHnqUsKYomX9XalXeqTkZF1n_KZC1p3fOEnBgnby80RcBgvJ8ByplglIWIpiL3TlJS0w0iCzGfWm5nNQZDOOfLHGtXtn39SmkgdKW3lBXkVHZYbJMhGTBgrFL6WkKnZW_fQfjeLAylDGLIgfka5piI2GVdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRfvEz9VcW2ZTExlR4UkvZ3PgfKXiAZ4w0nEpuRwiRGQxn0kgDVPggq50ZDioyWu27LPkdMnlNCyvLnd9MPcbVSt378JDDHA-FEblr7lO-aExCOnO9sNbKDVb8a2fGa9qB0vZ1KTywx_cyym225XLUNyR370YSOY3vGSa7aV4mOzFRIlmy0CcDHe_OFtIpKdGt1NajNHC1QcLMsLCT4fBUfUfZdivwtvFUMnrItiOwb8MuHtMHofTbDjbBQU3WxK3N5E_5YyE6cslhfx2HhHb2rK5vcdSSjtHSc0z32PyvRonK3-sMfNYgCtG5E0k_jTtQId-63gS_vaiKZ-Dpa10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=M89z7tcxKxPed6-mDjICRdSMM2iFTUBzQML8Hdn-AGNuh2-4-e3dsj7RH5NGL4xfKEma8aCWBrtoxdAlOTBu45iaAFO5_Qv4sIhsdhT-AIFe67nVZKdDOL4In-m11oyE7oI2qkn2-TM2i1GcyvuYX0Bft_BVlzmQBIGTcMSZOQ42I01UNahsI8MGI4hE1P2CtDYp1T2N3yzuAlCBH13pL_ARVw_VVgyAIthZk6xUYChZGByrz6UuL4OOGl_Qr0OubxZtFV9WoUGPzCFiQHF8TTJ3JqwTde2rtK_OewIV_jJrWc5Eerh38X1J9bMQtmsao_e2IFH-ac76jXICYp5uqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=M89z7tcxKxPed6-mDjICRdSMM2iFTUBzQML8Hdn-AGNuh2-4-e3dsj7RH5NGL4xfKEma8aCWBrtoxdAlOTBu45iaAFO5_Qv4sIhsdhT-AIFe67nVZKdDOL4In-m11oyE7oI2qkn2-TM2i1GcyvuYX0Bft_BVlzmQBIGTcMSZOQ42I01UNahsI8MGI4hE1P2CtDYp1T2N3yzuAlCBH13pL_ARVw_VVgyAIthZk6xUYChZGByrz6UuL4OOGl_Qr0OubxZtFV9WoUGPzCFiQHF8TTJ3JqwTde2rtK_OewIV_jJrWc5Eerh38X1J9bMQtmsao_e2IFH-ac76jXICYp5uqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9QXkj-XJvDW35abElEGPCYMANut3C9gEwHJzHmxW8u-F2RdvCMjnCV6grVbP_LYNWJkVBEcVBeA8sFOFwyILt98_I69pGruuDyJtYoqHaa1KRtSpq8L5-j1WNSnJbC3OinHqPm6ykH2f1RjKQ21WXzOUZquxIUz2P6sT3MgTDIly989gGghwaPgT_fWV9nS79oR73PUbY5yLl0gQuYEM_jMCjodgqp35B5swK55A5DrPfrB7H3Z-0a5akzLlWOA6P2F9PFk5hrilK7PM7ess9zXteZ3hTE27kuXsR7EE45n6fCBJk5Q9kf2euBSTRczTWpnHFcW0lKIc8MhwKWvVDG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9QXkj-XJvDW35abElEGPCYMANut3C9gEwHJzHmxW8u-F2RdvCMjnCV6grVbP_LYNWJkVBEcVBeA8sFOFwyILt98_I69pGruuDyJtYoqHaa1KRtSpq8L5-j1WNSnJbC3OinHqPm6ykH2f1RjKQ21WXzOUZquxIUz2P6sT3MgTDIly989gGghwaPgT_fWV9nS79oR73PUbY5yLl0gQuYEM_jMCjodgqp35B5swK55A5DrPfrB7H3Z-0a5akzLlWOA6P2F9PFk5hrilK7PM7ess9zXteZ3hTE27kuXsR7EE45n6fCBJk5Q9kf2euBSTRczTWpnHFcW0lKIc8MhwKWvVDG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=QgqfKfpV58VZSo8BholJgPBs-o-urw3PJ1vh1fnfmgkkzRtW5mXFNH2GWnLFjapNK7HCBtmv6uOJ-cE04OYt1kjpMvjG2Xr1uLZrsh3cgGoqNj7rHyDK_ikW--7vZiMifpdd8sVXybTLQio8RRmjlw61nFktN5SjqcbvcvXcyWRECTTQ07sz90SL15MU2RGbZL4QmnGxmaeC52T7zhdwHkZ8tIolQHZyMN-BlMN5d4JxusPMAcj2tjQJ6_Ul2B9W4RF1aROE7RGG97s_P7uvHgt1JqxW5qFrbdrTJqik_oCnJB05dpWxoguqfy3cgUXRhvIrdb29io72HrKkP570yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=QgqfKfpV58VZSo8BholJgPBs-o-urw3PJ1vh1fnfmgkkzRtW5mXFNH2GWnLFjapNK7HCBtmv6uOJ-cE04OYt1kjpMvjG2Xr1uLZrsh3cgGoqNj7rHyDK_ikW--7vZiMifpdd8sVXybTLQio8RRmjlw61nFktN5SjqcbvcvXcyWRECTTQ07sz90SL15MU2RGbZL4QmnGxmaeC52T7zhdwHkZ8tIolQHZyMN-BlMN5d4JxusPMAcj2tjQJ6_Ul2B9W4RF1aROE7RGG97s_P7uvHgt1JqxW5qFrbdrTJqik_oCnJB05dpWxoguqfy3cgUXRhvIrdb29io72HrKkP570yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGdLesgLcLHBRs2yFzFprKHU97a2O_uEA3j59ZfM-vne5Rt6Q0V3nKsu4M_oL6UsgVQNzRQMGMYuWA9rLgv5NXaxE2rLhk2uF2kSuuOHKhvTUpv2I3oKxeJq14omxMJgsbOI3mJI1e7y_z4ol4LhfIT3GcvcouJrG8n1J_NVY47IeX5UNlwMenMuE0EXupu7-m8k98LCfkuikxMrNUXuEFxapbBhDajYzHeTBuyz9MrV1ap4qQ8thznHeIw5Z8nmDKfnlQ_Ap1y03dMh8fkI8ISor4nzu2KKu_rPTT74BjB0_S1iSQk6Ijqau-0JGXeR7o3V-ygqph7eKpl8-L8cuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=REmtXuqylVYvSkfgNkv3hrOl-YHf8tSiMVmezzpPj91Fu7D2hFzkhHeOlbOGOyYxXqzzJL_4fgPVyKOLeF0s0gvHT_C0__mqNYiLgCFM7pfACS_fSj8CGIT_jnoMOu3hI9XSWx3gVrSUw4Q_cInxhQyrue1FlDF2FM6HmhCCX5nxYmmLNLBmREX5aDrt8HyliqT_aGLHScjKY6aKfbUBo3h_1HXMbskALDsKMoyYVL5NobH2Xxmg4V-ZUmT6JC8Ngzjmv8IcNpSA4UAkX2j1S5OsP2YdNG3nBttOvBfE6oayzpJ3BJvM3SPvGNyzH4jidvjLJ1VctfuCZBeb9Uyt4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=REmtXuqylVYvSkfgNkv3hrOl-YHf8tSiMVmezzpPj91Fu7D2hFzkhHeOlbOGOyYxXqzzJL_4fgPVyKOLeF0s0gvHT_C0__mqNYiLgCFM7pfACS_fSj8CGIT_jnoMOu3hI9XSWx3gVrSUw4Q_cInxhQyrue1FlDF2FM6HmhCCX5nxYmmLNLBmREX5aDrt8HyliqT_aGLHScjKY6aKfbUBo3h_1HXMbskALDsKMoyYVL5NobH2Xxmg4V-ZUmT6JC8Ngzjmv8IcNpSA4UAkX2j1S5OsP2YdNG3nBttOvBfE6oayzpJ3BJvM3SPvGNyzH4jidvjLJ1VctfuCZBeb9Uyt4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=jOCvnO04V0ZRV4DzCfaLiy3ZJjxXqAjITRBYKmK6pYbKRCSvWLowcXTnQfnPLO1_sMxoCTuH3SSOfOZQgeiF6bCBj-0QjpUeoBhhudPFrSAle1wGFp1qbYsuE3k3cjh6XPXzVSjF8i01SMIi2iC6KSYFHhp8BaC0xFOGxh1WS8UF9JFtZ12rEv0OpAMz9ZNMdzjSv-_EYxAIlAf56BAG7Gb_SnDFvQGnqKqIoc1qtrT1l74EAn0pFJkSSbB1iq0eiJ-tZx60-eVhv_AEkbC8P3syCJuwDUKdoq7Ijb9wCcnvF7pn81WWnoUl8gTqUar1YvBsWFL3DrN46Qsv-d0rxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=jOCvnO04V0ZRV4DzCfaLiy3ZJjxXqAjITRBYKmK6pYbKRCSvWLowcXTnQfnPLO1_sMxoCTuH3SSOfOZQgeiF6bCBj-0QjpUeoBhhudPFrSAle1wGFp1qbYsuE3k3cjh6XPXzVSjF8i01SMIi2iC6KSYFHhp8BaC0xFOGxh1WS8UF9JFtZ12rEv0OpAMz9ZNMdzjSv-_EYxAIlAf56BAG7Gb_SnDFvQGnqKqIoc1qtrT1l74EAn0pFJkSSbB1iq0eiJ-tZx60-eVhv_AEkbC8P3syCJuwDUKdoq7Ijb9wCcnvF7pn81WWnoUl8gTqUar1YvBsWFL3DrN46Qsv-d0rxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=F9U7a6wzCkv5DlWImpVDgXz6DYhnhP-y6Jy2pnRdinwShHMoJjnBGbqRx2ihpJ5sRP948_jgUgJh1GAGl3ssR7lmb1NXnDiYaJ0u5ruuVLTayPyT1eDOqgUOms3X8LpnLNlS8CmZjvCg4vDyfRmsOeEln5xCeu1OLW4ABRJPTv_pWFEay20I8QYICRnkUNs19Njo8qSf9danagjp6GpqNvNsV7TQkDPinxxpCKLonP8x-bGwAOiqL0SRYQJvWhv6b01CAt9IWnWr1fYWsaWGQ4HwZGjZRPzSS0hzZvbbLKtbPR6N8uhE2taHWKEPKA6VmFhLbgO7WBpNynlNMpRvkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=F9U7a6wzCkv5DlWImpVDgXz6DYhnhP-y6Jy2pnRdinwShHMoJjnBGbqRx2ihpJ5sRP948_jgUgJh1GAGl3ssR7lmb1NXnDiYaJ0u5ruuVLTayPyT1eDOqgUOms3X8LpnLNlS8CmZjvCg4vDyfRmsOeEln5xCeu1OLW4ABRJPTv_pWFEay20I8QYICRnkUNs19Njo8qSf9danagjp6GpqNvNsV7TQkDPinxxpCKLonP8x-bGwAOiqL0SRYQJvWhv6b01CAt9IWnWr1fYWsaWGQ4HwZGjZRPzSS0hzZvbbLKtbPR6N8uhE2taHWKEPKA6VmFhLbgO7WBpNynlNMpRvkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ZBUE95Ez5SjbSaM_nZvpd-10jjUTfohWcbRYwtwyi6tuDeWJrPLFwQTgVkRQY9spUcT_3wrf7almUKIEw9hBYVVKpIaRPtn3GNBplmAMq0IuwPg3Cr-moATnvNzViKrYuE9Sr5ofD6zqYwEqQzrnLGUrukRPcMF2lxcnc84hKxC8EjKhmI-Ra9xiVvASo5e_2gKK0OOweksJbgrWeM4spwQrOPX4eJ19sNNOi_I0gaMVzcKJmHabEJ4jCdXXje11jkODbBubhGGqsPvv7EOABj10pMkWjRavsOLjn7kAfB1yb7LaV88NbNpZoItZhkaVR-LvKr_8AGTbNAYXDTAI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ZBUE95Ez5SjbSaM_nZvpd-10jjUTfohWcbRYwtwyi6tuDeWJrPLFwQTgVkRQY9spUcT_3wrf7almUKIEw9hBYVVKpIaRPtn3GNBplmAMq0IuwPg3Cr-moATnvNzViKrYuE9Sr5ofD6zqYwEqQzrnLGUrukRPcMF2lxcnc84hKxC8EjKhmI-Ra9xiVvASo5e_2gKK0OOweksJbgrWeM4spwQrOPX4eJ19sNNOi_I0gaMVzcKJmHabEJ4jCdXXje11jkODbBubhGGqsPvv7EOABj10pMkWjRavsOLjn7kAfB1yb7LaV88NbNpZoItZhkaVR-LvKr_8AGTbNAYXDTAI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYNyn9-nW69Pz3D_QcuzfNwUQZitdxJ-1FQqANA5dZXnYiaacZpZsggLPLPWY5DB7hWlBGzCnHNGE759RyMcLlEPRsMgd33FU9BnQub6gz9eCJ_tJIF0zPuERpjNRdcYmN2L5ElywClidGZndBVSEYqcWpaMBHoSwsTSJWgkx8U77SGJ9jp1HiATmZHNYZMK3saO3tVJCV7QwsfZBGc3pK7vTFbRka1k7cnG1kUtXdzqtY_SerfqqszPoczIp-BxE7OfrBB1fxHhRVS7lXvEmCbkMum2wzgM8o3mbamNNr4M3L9LY_EiIGFsUnyeEbVDE04lQBcfRfTSBj8w-yb9qA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=IFM5xO7s3hc14qpIdFXEMoCXTpRJtjfY3BY1Cl6z96j76rcLjkNP3OdKknFtkjzEUsRD33fJBti5slbGXDgSezjF4vkg0G8J8AydUmwkG9-NRtDb5lezqKtvBF3_rlCVcTrbLRmE-pvaB3nB4J55jIsrIuIkFJFUIjWX9Mnoz8HZp-q6ZuaWJGA5KLxfWF5TJALUQ7jGrfV1JsjmbQZUIKYHsxgXqWZTiNrcCalCjeRs7ftuJnPcdhpSgt9bjmMJBehRc68tK0VjUad-bXhhN0MZ5mpPcpCZbNBAXgvlJ_qLT2bpsKxemP7a84oRyMWMEqpDtRfGZU3QvgFPslt_kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=IFM5xO7s3hc14qpIdFXEMoCXTpRJtjfY3BY1Cl6z96j76rcLjkNP3OdKknFtkjzEUsRD33fJBti5slbGXDgSezjF4vkg0G8J8AydUmwkG9-NRtDb5lezqKtvBF3_rlCVcTrbLRmE-pvaB3nB4J55jIsrIuIkFJFUIjWX9Mnoz8HZp-q6ZuaWJGA5KLxfWF5TJALUQ7jGrfV1JsjmbQZUIKYHsxgXqWZTiNrcCalCjeRs7ftuJnPcdhpSgt9bjmMJBehRc68tK0VjUad-bXhhN0MZ5mpPcpCZbNBAXgvlJ_qLT2bpsKxemP7a84oRyMWMEqpDtRfGZU3QvgFPslt_kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=qR_cDiNWq9SaGKmoc5fiY-5EIrjJsQGCnE13-icnS8TvTInnftjqppu0oERveGvStvukhGdquDuqH79nMDrXLJM05TYJrqO1QmOMimLr0B3vgZy6PEesc90dKZZZFb8qX2hdkTZLZW7wGRrxaPKkGdxgoKy53bFZM3BfHrDNBFB1aj7QY2egbPLiY-6g1yiwLgI62woEuiHO1WmTE7FUGRc-xJ7DysF-W9TnquHxdBrjwNwpeeWVC3Ld0D1_qkkkxUWUNi1l0M-vDzwxjTQBup8mYooIq8uJ5C7JvLJWIPBCiwrlV1Flx9MBP3aD4mnoOoqgAjIyMTanVMHXVLO6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=qR_cDiNWq9SaGKmoc5fiY-5EIrjJsQGCnE13-icnS8TvTInnftjqppu0oERveGvStvukhGdquDuqH79nMDrXLJM05TYJrqO1QmOMimLr0B3vgZy6PEesc90dKZZZFb8qX2hdkTZLZW7wGRrxaPKkGdxgoKy53bFZM3BfHrDNBFB1aj7QY2egbPLiY-6g1yiwLgI62woEuiHO1WmTE7FUGRc-xJ7DysF-W9TnquHxdBrjwNwpeeWVC3Ld0D1_qkkkxUWUNi1l0M-vDzwxjTQBup8mYooIq8uJ5C7JvLJWIPBCiwrlV1Flx9MBP3aD4mnoOoqgAjIyMTanVMHXVLO6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1L9DVTS-AiU39WrQmGeOU4_ttRkKtt6-PIRY3dV5r8sjo-8WnEiBR7kV0rYvyjhR9rC9_kHXgo1gNueK9z6R4nInkqfYrUluXdTzyZr0PPo9NULg64W0_NClsWz_7eqhKPTxfeztZcfQ-ZSu_FbQpMP7QQ2lGCvXhpt1KzzHNnEX4SDNRz7G0TKzDi5qnNonz7KN1S1apha6OigxoG-Cz27141PbS4nvuzmmWbL2AXrY3iaY2psJBJThjr5JKgf_458uCt8XiKrLd6L9gB48uXD23X0Odlq2w82AQiluxLfBKjQ0BUvyuJWI8R5lAYM2QcyhI0L-FqkUNxEV75mPg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ru4m-ZfmgxVLxrNFdwKTn9pTvgPmVV8HsUKEWMgUQHRNa_58_ItbpeuQBLDOzxDQOsvj_10EVSLTHBNrUKWZqz_P1XuKXgAoPrA_lKn_EkeRy1hUCdtY5F7fbctZM6bgKqHfxWtdiF3AAj5WfVvhbph91Ftg45HXC2jBeenKqdF6Gg9uaPfvfRaguUgRL1EGxZb1Ih8C8EDzkRWP6yebph0UuppLr7R21snNkp3qoFF813kY1kxmr3HQlN2Z0e0idBoKx9310DttfIwCHlxPOk4lUV3j7XuFP5t7Q2Y4EqhDdw3G8lIpaAmNXNwvGDutaAKamiC4flCHGSFAnWtV6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=ru4m-ZfmgxVLxrNFdwKTn9pTvgPmVV8HsUKEWMgUQHRNa_58_ItbpeuQBLDOzxDQOsvj_10EVSLTHBNrUKWZqz_P1XuKXgAoPrA_lKn_EkeRy1hUCdtY5F7fbctZM6bgKqHfxWtdiF3AAj5WfVvhbph91Ftg45HXC2jBeenKqdF6Gg9uaPfvfRaguUgRL1EGxZb1Ih8C8EDzkRWP6yebph0UuppLr7R21snNkp3qoFF813kY1kxmr3HQlN2Z0e0idBoKx9310DttfIwCHlxPOk4lUV3j7XuFP5t7Q2Y4EqhDdw3G8lIpaAmNXNwvGDutaAKamiC4flCHGSFAnWtV6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=ijm2NgeO3aFZpv3iRlbBXASs1jsaIoh18l36V8ah-QnJOfyrdKMkrkKIxWhb1QlhlAMlLiOBeWsav3QqbhwjT_K_hND0uGQO0JA7IuOrP4oHRB4_RAIypaXeZXmHK9ZNBUVQWVXS9DACQO73khvP0NUNBQvJ7l338L1YjsbnZFgim1SF_4S9DjMH6ZJtjP9xHj8eV9shihQVBqFPLaX5DaN3mRU0ghfAhmo5-l7B9cfrATvrjiI3jtzpeHuR_ttU3A4tEIoSR4-3Q2y_mElT6NoGhGFUr3B3Y5GZgCnF5SMsK7L-zOmx8LUmOcILwQnsUhouYbAncG6Q32eQIgTg7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=ijm2NgeO3aFZpv3iRlbBXASs1jsaIoh18l36V8ah-QnJOfyrdKMkrkKIxWhb1QlhlAMlLiOBeWsav3QqbhwjT_K_hND0uGQO0JA7IuOrP4oHRB4_RAIypaXeZXmHK9ZNBUVQWVXS9DACQO73khvP0NUNBQvJ7l338L1YjsbnZFgim1SF_4S9DjMH6ZJtjP9xHj8eV9shihQVBqFPLaX5DaN3mRU0ghfAhmo5-l7B9cfrATvrjiI3jtzpeHuR_ttU3A4tEIoSR4-3Q2y_mElT6NoGhGFUr3B3Y5GZgCnF5SMsK7L-zOmx8LUmOcILwQnsUhouYbAncG6Q32eQIgTg7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fy8HwKbFiB6eE1XDGwf9VJ2tZ_hPvvdoZx83TkgQzcuXHnPQzmlR0u9y9zIIh2eaBFzd1BcMnIKEeTZmfRVri-HtkDOhXP0HPBakHUwt77ICVYSwVYXkTq4ZJ1li3Sjd-GomePfK-CQHhZHQqfWTk09N0d_1z9hZsjazmqZluIbbvDq1jqZxxu8lr7L5zq6bFbvIsruueqtTxenKdHSdt5uHIexlwlC0426l4CXPY4_sETTIdZRDdaqv-odpPr2ne_gfxfuUzGbIifHsRVqIY9S-rJTHo_61iw7hR1KqtpGMjlE1ORF1X15uyUWfjo4QbzLkocd-Aig48iy6nCQOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2XTP5yq3ZHnuqEKtjU4FZVNtZYkoFldsIHBHruSHdn1Cl-1jyoVu09GhcIJ0q3XV1qgGpWW1VF-yyh5NeJsp6Vh-eTpg8Z8KC2zR7GP_hrGX3RP-5gAuwyBaQ3BsBDjWFcjYd8hptDlVM6nWIMgsDHXPR8a5M5GHgf9oLCOcuMvv-JQ9l-di8s40jDVpZbjwjqPrhXdt1cnZSrI5c5ubzhhDADuA0QfsNwV9oSDO2-b_5vJshNHWtMmsxSke7n-_U_Cb2-EGySCg_-KOL3Q9l4_DxPNGhnyXg2MAStaioocPIkbr7l3--qzfR_WtNchjO2zZaxh3LsbvBsSJFgLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vy9nJtAsQ83ewVSzR_DDvc8sHnlzegpv7Qcs4w-ugsr5MdJYGnCTYf55oVtN73UhL2vAKfSfdcPMniAjGyS1JNnEVXtSFyebdzsIX_2IqUdm_4KccdhXYHfrZj6Nux-bKrhLdFmFSBahF_Zv_oRII0vMdIKZKcf_STnOk9oNdf9WiJN1gL9nx-68nryukft06nWRvL0tcW_uissS9aPVQIojs8eLTpZuX_5zO3ZZvzu0sk53pru8dBTp0j0fBnQcshGADhJ02Qzz5OcmrVXFCPRdGk-xfnRY9GFQxdIJcsZwN2GYib81PDk2MB-ZhNuWdqzufuLNkxPJZfN2JCdwww.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=p2kzP1KX86TTOge8-GtUuJB-rTTm2qumljNkFHA52B1QVUNRUGS3VMHlen-QURvsUouyCqMaNvM9nUpTXjhgsdBO2wAyG0r25VnSrTrgeYm-wS5ROmDpI-ha3iq4_CurpeLXncsvLI81L0qpi4jLjovx9kzVikjzQF9IRvE47TWKezI-z25RTSoVPrCUWegMWvtacWPny6Q47uVdicqBDVyNp3BgrAP29Fgiqpn6tjnJJnyQe3AIJV3OUgvoZBZ53tO5nZHkRBBjdRdHy2xDB25RlGgkXBtWvpd1T5KFsn6QS-ecAHSIX0og2IupoMNjBcNDKca3snGdAyNZG3Iltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=p2kzP1KX86TTOge8-GtUuJB-rTTm2qumljNkFHA52B1QVUNRUGS3VMHlen-QURvsUouyCqMaNvM9nUpTXjhgsdBO2wAyG0r25VnSrTrgeYm-wS5ROmDpI-ha3iq4_CurpeLXncsvLI81L0qpi4jLjovx9kzVikjzQF9IRvE47TWKezI-z25RTSoVPrCUWegMWvtacWPny6Q47uVdicqBDVyNp3BgrAP29Fgiqpn6tjnJJnyQe3AIJV3OUgvoZBZ53tO5nZHkRBBjdRdHy2xDB25RlGgkXBtWvpd1T5KFsn6QS-ecAHSIX0og2IupoMNjBcNDKca3snGdAyNZG3Iltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_yPr1lRs9UA2Pva1n7-87OOjfDVrrtizFwxifgWu7YdT4E6JNT0PscI__lpOw_RPlFSswtnbAa1SKt--Fjx1a3WTgf3n7PuwcqarPeWnk6vCsRVwrDZqUSIUFLEYFvnt2RKqRc1UhyVnk1jJde-dTV6NQFCyh0OxoLDX2a280Y3NKg9x-e-lihPV_IZ8vz6pQyl-ZEMKN_L8osXxKcqzFrB6rZAu5ayOAziI8g1kOOD-gWQmfZ0u1XWFAe9r2gxUXtjUMdCZSxXsSoyPlxPhg0Ktrr90_71HECd4NZxL6klZB0vIaPGr9608QhuGHFOc_0Yk6apDehHMzNjut_7dUOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_yPr1lRs9UA2Pva1n7-87OOjfDVrrtizFwxifgWu7YdT4E6JNT0PscI__lpOw_RPlFSswtnbAa1SKt--Fjx1a3WTgf3n7PuwcqarPeWnk6vCsRVwrDZqUSIUFLEYFvnt2RKqRc1UhyVnk1jJde-dTV6NQFCyh0OxoLDX2a280Y3NKg9x-e-lihPV_IZ8vz6pQyl-ZEMKN_L8osXxKcqzFrB6rZAu5ayOAziI8g1kOOD-gWQmfZ0u1XWFAe9r2gxUXtjUMdCZSxXsSoyPlxPhg0Ktrr90_71HECd4NZxL6klZB0vIaPGr9608QhuGHFOc_0Yk6apDehHMzNjut_7dUOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=ozDIntypxL5py_sVA6-87XVxSnFpQhomJHkN1CQQfcd0DTO-2ZvuXE3F6lcAhtkaK_4_0yAWbL7fyodBdVXpLwtKLc0hDK2Jcrw1cx4NTgK-5QjnSwfkkDdx-uf7Q_POi-86qpOsJbvY5PhpeOi-qyv1taTUw4qhBYbm9ln7FXQA0wYPnQDQdqyNOiWpXIos3YE2i0pdNeCQpdsrimXmE5-W_aMQ3HSePzTZf4hGfyH4FQmG9Z0vikZYRSkarWbTjdxGKqMeJgzVWKFxHqLvf90jpWOMtJJ6GheZAHq6lOgb3P-4nrxiOV63Ur_ExduZkG1TwKvG9HdLn4QngwhFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=ozDIntypxL5py_sVA6-87XVxSnFpQhomJHkN1CQQfcd0DTO-2ZvuXE3F6lcAhtkaK_4_0yAWbL7fyodBdVXpLwtKLc0hDK2Jcrw1cx4NTgK-5QjnSwfkkDdx-uf7Q_POi-86qpOsJbvY5PhpeOi-qyv1taTUw4qhBYbm9ln7FXQA0wYPnQDQdqyNOiWpXIos3YE2i0pdNeCQpdsrimXmE5-W_aMQ3HSePzTZf4hGfyH4FQmG9Z0vikZYRSkarWbTjdxGKqMeJgzVWKFxHqLvf90jpWOMtJJ6GheZAHq6lOgb3P-4nrxiOV63Ur_ExduZkG1TwKvG9HdLn4QngwhFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmC28c3hpumYjUhJomd9Ln6ow_d4Wk1uJ3-h4jm-E8eNgNHvh_hz7hEqL19iYvh9GSyQKT1GpcKTfUXHtXKdOTDoQ1IRAPW9kNzQNpy9Vb5jaDDlmTAGnnryKkNEmltiG-udhAgTh0JPLs6jaf26-H06ydZHYLIukJ6V5n6spw6irYDBNmZhNirCM8n5GEHFcw89wc1Rdv2DUtQlbupR03Hsf5FJI2BJzF7oLs5sK2k6KqR6kR8yTnLd6C002UR-7s6fPEHP6iU7paJtnVsRNknrWglTD_Lg224mOplIUFlidvIm1aZL7RFPODPpwdmx_JTKWK8GK5EU9W9uJ_DtMg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=InWsMhDIOLPr6pVAtrO7z1h7FekNOFd2zuey40mqg0QX7ELtLBq-aPSWC_7-GDgZFLD85Wp_r-5nLrmqNsjh0uB9K1XAQynwk9SAEM1FqBhZp6-5HGMpwuVueaDdRP6lRCAS8w25EcjaY6wttBEDyZT25Njn0XRCZTYBapu3ypID63-A33dhlnem4ZauW4EOTH0PjRJkLVqNC7E5xtm3p7YjEMwLizZAkJweC-QeMBiL1BMKVdtVoLSEI-RR_Bn07BlUGW0nG8L4ifRX-U9rW3yvmjgZUEqDos7K46SN2-r6Nl4Mk4IxMsV_yWFDcmr5bYRM4bjKUpAVLBvi3jqVRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=InWsMhDIOLPr6pVAtrO7z1h7FekNOFd2zuey40mqg0QX7ELtLBq-aPSWC_7-GDgZFLD85Wp_r-5nLrmqNsjh0uB9K1XAQynwk9SAEM1FqBhZp6-5HGMpwuVueaDdRP6lRCAS8w25EcjaY6wttBEDyZT25Njn0XRCZTYBapu3ypID63-A33dhlnem4ZauW4EOTH0PjRJkLVqNC7E5xtm3p7YjEMwLizZAkJweC-QeMBiL1BMKVdtVoLSEI-RR_Bn07BlUGW0nG8L4ifRX-U9rW3yvmjgZUEqDos7K46SN2-r6Nl4Mk4IxMsV_yWFDcmr5bYRM4bjKUpAVLBvi3jqVRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=NJQvOhD9ICoSzM80FVp_t9pSKt0n_E7JsK9t9SA6wS2YVNf3sH4jnoBBYjmHs2qDVe7OsLmlQDBFr06DdXHYhkLrOJ0EcqJSdJ0VL35-F8Ydxi5sYmN_HimFGlJ2QOr-G6CQurKoINlpy-VqdH9C0kvpgAGDVnF7OKm27WihJsB5yuap-L_t5gSQb7CHmeivl91c3o4ptcG4EQligQ78jwO6CdLNgFD4BxLxylJb7gUnqxB5o-040B6ub-KJD7VhKQyjUCtYf5PxeEd4gDGqFU3z8-Ei_1WbA-T6zgVA_BCRUMULA2tbFlwvGHj7QYN_t6vMcYQwL8hykDvGAW3fYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=NJQvOhD9ICoSzM80FVp_t9pSKt0n_E7JsK9t9SA6wS2YVNf3sH4jnoBBYjmHs2qDVe7OsLmlQDBFr06DdXHYhkLrOJ0EcqJSdJ0VL35-F8Ydxi5sYmN_HimFGlJ2QOr-G6CQurKoINlpy-VqdH9C0kvpgAGDVnF7OKm27WihJsB5yuap-L_t5gSQb7CHmeivl91c3o4ptcG4EQligQ78jwO6CdLNgFD4BxLxylJb7gUnqxB5o-040B6ub-KJD7VhKQyjUCtYf5PxeEd4gDGqFU3z8-Ei_1WbA-T6zgVA_BCRUMULA2tbFlwvGHj7QYN_t6vMcYQwL8hykDvGAW3fYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=LSJv83SCtqaKpnBsUbxxB7h6qq7AJ59X1khbUDD41zolZFDOooQHFmxvwRQc8h68XsY2wcYxD7DOaZUFIt_KA0wxSEOUFTm1-FV2YaZP343Xt6KqVIOe8qEDOKUqj9RybZG9JwQ5jSEopsLT6QKKht-H-e_wV1GXF1V1dS8cn8J1KsWccxbQB6K67N_-Jg9F7cKAcpfpS9MxiyUeQmnrI0CRqGshcgWvRdvCINJmM5lN4PlZVsSBim08Lw-r83aAKRU5GZWN8yqZM9lIS_fMnGhr_nvsiY9iVlF0iRejLACPeuATkIz0txsoZqm9twxLeVt2BUWZG0Az-ONQe_m8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=LSJv83SCtqaKpnBsUbxxB7h6qq7AJ59X1khbUDD41zolZFDOooQHFmxvwRQc8h68XsY2wcYxD7DOaZUFIt_KA0wxSEOUFTm1-FV2YaZP343Xt6KqVIOe8qEDOKUqj9RybZG9JwQ5jSEopsLT6QKKht-H-e_wV1GXF1V1dS8cn8J1KsWccxbQB6K67N_-Jg9F7cKAcpfpS9MxiyUeQmnrI0CRqGshcgWvRdvCINJmM5lN4PlZVsSBim08Lw-r83aAKRU5GZWN8yqZM9lIS_fMnGhr_nvsiY9iVlF0iRejLACPeuATkIz0txsoZqm9twxLeVt2BUWZG0Az-ONQe_m8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmtpAVOTBf4kFTe6J4N1JLzwlXyCT-qtKkv9J9eVEG-UO-CpHuaf6QjDzodC0HPpmCqeWI11xIURAXPmS7gvrC4G-1whKM_7Qsh-kquJQl-RDZ_2o6dwMppSFaxd_QXpgMpichscR8Yl-E53A8zKHxCZ6L6-EHtgHP3dLUdo3aiNScmoH0SkLphvBqWomg7eYwtjGvp3JBWH5cQuoccH5JnUi70RoByzFWxKMYRVH5MY5qnnS1sXU61gNWiBMm0ZNgpiEEdiZokBPKeXMxoAFuudumtr28FhCFNRZQp4f3ycrddBcMYqML1pijg1OL4Wil3g8kfbNMA3xdsSXqQzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
