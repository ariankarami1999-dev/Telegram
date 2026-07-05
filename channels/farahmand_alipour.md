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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 09:00:04</div>
<hr>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPDxktuZ-uwY0rFeL_Y1JYvcSNwTOnyzqi5c-LCUNYOP_ILezA0yE--6L36nBXEQLN9Da74xpdtFrEDWr-t66OOmmBDanZOsecU_MGlp3f08appH_tWYxz5qCAgsjz7fetbGKs_00FwcJE61e7oerLe_dzN4-_6kmB6sQboAbl6v7ZXwtnYODPiWfJCZ_8j2D8K_tHx5SGSSFfeEmhey6oaep8yDdJAvBgoq-FHQGMV2_TXWzleK1T06-ElmtkkXhssbcVtHOGjEM-CbVDWJS-WRQuPm8T5c1nx9ZID0LAPQW_UuXNVuwMs5ytPr3NnqJFCGD9UCjfKf8cnULxV2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDSowc4ggUBALmxYgg4sKCbqdHKajDs2N209yKJpJ6AssUdzygUj73AIPKkvobWGuD6viJwPyxq0G1mWrA9vs4PyRdDRS4_84V9xhro_fbsXS9OR_kcS7Ft5dNQljeAzLbjwDYvamHol7zYECxvUsBL-kIuOIOMEVwRrRwrsxsjaYvDrh76e9EM9DWm1Zts6xPNuEpszc-JAHbBg6xJtFdj8sY2t_kHWIOt04EThP8ynrOxwsxQldezUwvmQpCUfkbTuWUOdMzsOoZZF6YsEzl67YFOpbAgf6lZLzOdBVKVcnMKKXfrJHYHAA42ozhv-fSBkkKNRpIOCpHdM3f0l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6PsSqjmFeZRsqf46V95_yVJOmFrY0__NU46mh60V6n28CMvFmdD0kivUDo2yMmapQs0Yvs2fM22f3Wuv2dYilegoK4I2aKExwRMSuiNGqk-_XRUX12xyCMTM5NhOPk5gARhqHs7j9UgE5f3FVdET5MfZK5hHI_NrAHfoXYEAUc8iO7dKCqKJcAlzUV_KvucHtf5VUq7ZaEhDkz_l9FykrQwDEo5XkhhhINl1V0GrlQlriyKHqAT-iJaLyBmKTEwd5vljmmvLBkxoatNP3RPpymxeiSTn8FCXkUcO3SD92EIbyzYw78ygGjL9sQUVGHDB8fQVz7oELMozd-RKJpW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV272CHPywM3jIcUHJqX4D077wDvMSjJtaotmRY9qa2MEDtTOuPxn6vNov3p0i5JZgJ4oSuBXSQo0EiwXoP56NsehKg24gihVi9PcXqNsMq-ZbyaQ6SdNFNpw3NSNRWB7x-gQZT7CuGxKigcVV_AFpCEdoFg8gDIxI1lGO9qD84TSjdUPEqBuGy_n-kbQcDKBKFXc8mguqTopYiKqQyHwjGHsRzc3tDRviq0rFhhoPMLrWiQuky6p997AQXStbD-bifGhCOfGym3w8SNcDWSvPH-YldIaS4kJLvNQmjE-JwxBA5Bx4mSDCF-wFmbbGJMapbqzP2b8tsXGw-AtNtYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY1083gPgh9gK70whojAqH8sGNCmqv__IXz2G8hJJJqo25P8r_terY0KbRT3L5fsoyx0IL3-PDmIvLt8guH8jc2s1Gmnv-jWnYtxV6_Y-zrX7GjdR03nmOIiQziT34AQg47rGjhU0tUWR0WwPHVXog3jpnX3J5SjKXqNVqWi2YjsyjMgxctaLWBsU6d1_F707_3adxiupH6M2mHY7DxK2hEqbZjxtl6v_MSX_6kOJy9on3ERIG2x-4oUYtalNFZ9nP10UiU_kNV1UMBDapCtK7Kx9BWTXH2tbs4DVq_saezeaGG-KtWMyoiMzCPv-e85m1_e-5cuZaFqPqm2EBIJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dixa2aiujy4DwDPyDRVZD6IJnKKIIvY7xm3CJ9hhijfHaB10NPWuTfABgcGGRNsrDKwQXT_ji8DCLaMGKXeoJPfyh2aHx1Huglm0Gx2nlBzcLgJLnyUWxYA_Z721KU9JGcUVKF6CgGIbJ0H99efa20LriPDnx8PytxO5-NMyWIzjd-CBcEcNwFUI-IF5Q9eAMtKAcUB_fbCaaH5A7N6Dm-_ogcjkIIc-jR-YqKM71q1wwS__SHuyNFECT9fcqeh50Qe2YIX4QOZCsiUZuk1i-YULKWeu6NXQ7xiyoXShD1VRYPG28dDXCiEcAsovEkr0gJpJN67zB0w4AgYe5RA9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxO4YMf9LAWTomk9K4lr4HBVfmWMZ7_wrIcqcoYSyQVO5NwyCFV9l-EOAQFit6veonK7Sg1nNGzr2icf9S287Jk6wWntR0_lgnQTBv6dl1rTc-uz3loQlt49aJ6fljmH7fSqjb_34OvDtWrfpEbjO8ZJOtVx4gY_pxcQZe3belP-hYI8rsnUKIBR7sLD7x5FvXnYPqqvv6CkCtVVHOf9vVHm8POgSWdNRkzlyosWkBxN3rlCUWRRRP8alml_IzxcgJlvC33zDrBDywpGTm63U3obEoTjvEjgKgoO7q1ystXgvYxg7LsxsutVfhO1hRmsJbenBu79Gs-075JZc6vc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hx2bwP2hKRh7KEiyJZNCIWxUMOEGqv05QVSlpILbyDXjv48jduQtDvicWGCpiag_eUCyY8y5C7xoQVXn3B5kgD2gpGd05VpU7dG9_JKdHToiyardLDQoF71r-7OObC00MVqixc-BwbEUvxxhJ_0Ij30cKRq4wgY2ZstX_2jQFNuXMaCZQPRUbQlnhL06EDYrYI8h4_0dD87khExYhwBu-EZVNjNlCGrxFBDhN_X3J8ZWX5kgQRer02gHoyzA7FtX9JGtSkXg0HIJBn13hhmB5IdCKvELYniOBsIJiauvjbSHIGeorOswh6jRbXunI9tuaDI-bFaddNFbq0gVV_20wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv6BJ6m0zrNGM1Ocpfb2wCd9HzByXfiukXW1prX68tJxBIoGwAuwBh6zThxR1R17t6KKfB1IxSxPAAt-ecTT9rOGwR8gOEmtUloWfDrShENuomRKp12jUZHUiDhg8kNq14a-4Gh2Tfn_IeRAyRzeUbgYFM8hWnQ9om8n9DEX88Iwc40Gf020kUIfCg1LA6mMG4ALbaIbdRPE9h76NiNAUjnm-AjNa-L6r_39jFQcag8D2RCzlbhXV-48Fb8IuUu5WF1vS9LE2LL6Jse2xV-hf_fZAAGfyulNHePxMLQZJLbBatJUnb23_PD_CcPO-eeAHm5T0bpuicPGez7Ty0t56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryufrieKnKGguteyPD4xEOHXf7TlTZukPQAC3ZFzuGM87M8i-VVVLPhKZ0KS8wr-54V2RDUd55CmXQmrScGColVsEsB2_FoXA76WT3Xqv1nxhGN5o-GX7OOcBTG-ZM4I5fs3gaiBW7T8FWNewZncvEl9wwPYxIMKa6IJPvyvnE50mRB_9LGEpnv5DSSj2ozJ4_Xhcq_GifEGcIoscDH603-xx1dydmYkSxvkgBdpZxk7lF4UrhSkoaJAtdDSBHmGHa0EX-x4OUm5HFBsYG3QVKheECcRgqB3mmRZzr5x3bUCxZtEsvFi6ZUeEGSz_YRBoAyECObd99EyK7dfLwTXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9z1MuEqgpKX7t0uxtIWca8IHhr6RxbBpAhUHBDy1_du8iuhOV15fCNjx5711d5XtfwXCcxwMWXUk1s17pEyKIbF-6BJzywSIPWU3KddIUigowILPd46KmHDD9Qjii0Doihk6uBmrFxTTto8IzmQL4JV8XBsWQLBzr63l4gfsEBuJFCXi-l5p1rIsmT_9PkUR8w8WJW0MNPLNV7n0GojfH06I5apvy_7JJNJdfioXLd1MAXVNDeBWJwIeQxUvMeMqSIJv4wEDAI3WuFl9nnEDA3tpg6cxZt0WNLRYQ43e7UyLxAs3H0wOjqZuYnxJ8caYYo5Qu-6Eaxp43QuWSg3nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gchLCUVW9s_tCcrmS-uBqjDpuNXHFgo5CnP6YnF5hL4SUaH-G1fabm3ic3bmpcTcPrIlO2-iKsOOBrW5LV_pIDOi3hlBnQNnnizHIt4pBG4KCnW_c03D2d_TowIrx0NGmoz1Zv9KuGtiLlDleZGvgdzXZjWsjG-EhYIoNgPJTOmo9YDGKmNS5V4qRF_GwyQMzysAdlxsbpdG26kQ_N6Ws71_AFufCmcFo9jjXvtg4avY0vqtd0Dhjbh6VJfDIJAoEYvwF6mNy4_9h89rJsIGBZQT9Z631kwuxZUUqha9iWbZocJ0eP1jjaiDQj2ABoP-5h9EJDe2VNcpM4yZ2WVJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV1UGiHxtlZbARWNvUVxiM4Xy5cNipxSPbFZeS_C5AHzfpJgdJzIkhoQ_GdDhAzYKbDVawKa8JkRpQHsZtZrlqx0sDhDqOrQKOfMAky-Ei5CQrEEM3qe_HRi2XMYuKciernDtl43H20YnnI088_WZV3k2ZfFhKMoe5HSm1IqYJUmpoBNa3i8nRbT6Px-WDeGmkPzQfbSWHt-lkr6AClb7ydn-jFXvfINNJfzrAFarOm1eiARwxcIntanwpmg1VpzrtDBp9FXQVzIYfjIKKHZmMTugTly5_jCsaEKBuqHMyUptGUHL5Pgek2VuKT0KoalVLf6IfiswjwKVoJTbjJhfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdSHWaya7L9TbMSyUGuyWo1riOGGqx8VYlEaqxMG65uPIqV6D4815MDDcCUoXqADM6FlIayUsUm8NoF8UY-9kmcmmCAETP3Z0aTpvxEL5P3wqgcGNWzmDyeXcwoQu9rpiuYpZS9A7m-5NW_rSKIF6taJkMNqJAB44tMNa5ZcysbAoE2gB9w5RhHQ4cjtaxBKFSY2BUg6zn10fg7aEVfLBd8OGiuMreX7TmTRCHBY0KCXJ7kgAviw9v-pBb9zq_DUEBchxo50sNYwfpsB2fy2orf57odbXLuD0GqJBJ4VqVoT4E5YhNzlNqioISAZGGrGQ8O_OyMCTNiMTGCqOjlJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVBKuDNSjSRrlT0BLrm6e7jkQb_dYYoXJAroAqyeHwLL3hIBc3xUjk69fyiI5P0xXOSyDRQnOwhjJYODs1-Ej4ESXza3tlIXZXgUqjuKqDGMHWmOUzQGWqv4fQ3DDL3HDTqbPBlqLT9PSv-kI67o9Jm3ePLcW1RLcKI0q4dgp0nX3LldcjMCAFEtJwl6BRcRAiXvMprFDQ2t9tYiMP6Alr4fvGfVBLuAVYxmzjEy0hIz5Sm27rOl4IMegT-gnEGGfQLGENw0Gtgix62-uqL1tHWLlfvxx07s7PFbiq7ZzGooC-hE9T-Hr2u1vT_z6EvanC4ulQ3Tc9hXw6fL6a6ksw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=ZRDsek5Vuv4Hz0yOwu9ZoPtOtuZUHo-ICAfQ7LSCAV68oGshGt_bBp_qwcxqlPLp93FGDm-Qh66fpvgYyyBD-4Pvoccb6TFU0y4UQE-I4Fl9pgI6RKgxDuMzK68rPovQasizpyWzx7U7_NW_6MmMrlw44G7EmJCj6NklN-SPVfCryGxFmiG6KGIUFyPVy7Hfzg8QYSjeO8KudVZcfvlJIXIzdkcl2A8K7ntM_bD2WKEjVWMvICje2tb07ULSTXW_l8m2rEPq5SMe-lV1_OE71bxKPR2eCozH4noS8l8DV7lw7SXM6Sz_OWNNrVB0mY48Vv-OtLudVs24sv2142OslA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=ZRDsek5Vuv4Hz0yOwu9ZoPtOtuZUHo-ICAfQ7LSCAV68oGshGt_bBp_qwcxqlPLp93FGDm-Qh66fpvgYyyBD-4Pvoccb6TFU0y4UQE-I4Fl9pgI6RKgxDuMzK68rPovQasizpyWzx7U7_NW_6MmMrlw44G7EmJCj6NklN-SPVfCryGxFmiG6KGIUFyPVy7Hfzg8QYSjeO8KudVZcfvlJIXIzdkcl2A8K7ntM_bD2WKEjVWMvICje2tb07ULSTXW_l8m2rEPq5SMe-lV1_OE71bxKPR2eCozH4noS8l8DV7lw7SXM6Sz_OWNNrVB0mY48Vv-OtLudVs24sv2142OslA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=IO_sZUFChBzy9aMUjYwVlyOMcaSKBDUQw0Ygs3tBNyD3FIVk7rANdopq9_E_I_rttKhJrczsmuTyjck5hoc89nv4rFyOyWFghRpBArTIrRlr5CNFasPQF2P_M5vtBLHHPz5RD5grJIFYYO3tD8p03ewKXjQ_sWExUUAwaCdM4anj-GIdAqpZbjvkLOwkmbwUY2xs7F7eoxYTrC9ShdCHyfbosOzBNd7qt5WJC19g_cjETuARJ438R0JVkYKP4wSqrYystA7Dz8FL7vmvJT-lZdgN3gV-4Ys9JGZ9n74mFjyfeK6PqbOF3REmd2A6gw8wrOjiamQVAIfUZek-ieZ0jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=IO_sZUFChBzy9aMUjYwVlyOMcaSKBDUQw0Ygs3tBNyD3FIVk7rANdopq9_E_I_rttKhJrczsmuTyjck5hoc89nv4rFyOyWFghRpBArTIrRlr5CNFasPQF2P_M5vtBLHHPz5RD5grJIFYYO3tD8p03ewKXjQ_sWExUUAwaCdM4anj-GIdAqpZbjvkLOwkmbwUY2xs7F7eoxYTrC9ShdCHyfbosOzBNd7qt5WJC19g_cjETuARJ438R0JVkYKP4wSqrYystA7Dz8FL7vmvJT-lZdgN3gV-4Ys9JGZ9n74mFjyfeK6PqbOF3REmd2A6gw8wrOjiamQVAIfUZek-ieZ0jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=upuZGAXyfJZDDeOCjeFAsTMLlr0kfQVWfINPhmHngTfa4Cw3uckZ4SUfQEho7rg4FA-WyAd2JWypvYKI5LIO9VmMR3KDgnkg3i6eUVryVbeMnSZm1HpLZjoTwmhJp0zcwhbxWqBQHxL_Xj2NMui_vV5KgQx-ULDAOIG44xTtsYy3YWBE-Hmcn-iZDFzinU9FZHRlBeInekdukf2ZROtDCkBRS-LGVn3BxJdk95Iae5kHuVzEmU-DivspDFNEGLUWIIngwnC8pM6LHzeBF21x08JD48uw-Z303mzke-ChZZxlEt_pzeXRixjOk5HF5Bqv2PHGKJ1a_0bNM4rS0gM-NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=upuZGAXyfJZDDeOCjeFAsTMLlr0kfQVWfINPhmHngTfa4Cw3uckZ4SUfQEho7rg4FA-WyAd2JWypvYKI5LIO9VmMR3KDgnkg3i6eUVryVbeMnSZm1HpLZjoTwmhJp0zcwhbxWqBQHxL_Xj2NMui_vV5KgQx-ULDAOIG44xTtsYy3YWBE-Hmcn-iZDFzinU9FZHRlBeInekdukf2ZROtDCkBRS-LGVn3BxJdk95Iae5kHuVzEmU-DivspDFNEGLUWIIngwnC8pM6LHzeBF21x08JD48uw-Z303mzke-ChZZxlEt_pzeXRixjOk5HF5Bqv2PHGKJ1a_0bNM4rS0gM-NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=MAb-sI5zVLOOIo3SCPUp6fH-4LfV-blJgoVX5DqzN6HRF-j-yKfEPc837K8SorFddWcVH6MrmAGIvbrUnw-3YzIuGFTGlJXLypJasrE03CvR_tiwwzWDq0LbxeibjFdEmJcLAwRSw6UHWb8vKDu2hrZFPTf4TtQPer2TzGWl-vAvoqxsPCrYgiUNLrm25hFyEXqxJq2KuHe-7Tb_mSiouFpLuHBKNR2ThgsvTHFqXtzU43wCpywH8fSJvY-43Ricrk3DHm0BnZSYUcQbnfKniwCNsNffEptxONZOtCbpEIjp-Vgyo1Hpn_OG9_YPPeFM0skj12Jj-va0puVOLPW9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=MAb-sI5zVLOOIo3SCPUp6fH-4LfV-blJgoVX5DqzN6HRF-j-yKfEPc837K8SorFddWcVH6MrmAGIvbrUnw-3YzIuGFTGlJXLypJasrE03CvR_tiwwzWDq0LbxeibjFdEmJcLAwRSw6UHWb8vKDu2hrZFPTf4TtQPer2TzGWl-vAvoqxsPCrYgiUNLrm25hFyEXqxJq2KuHe-7Tb_mSiouFpLuHBKNR2ThgsvTHFqXtzU43wCpywH8fSJvY-43Ricrk3DHm0BnZSYUcQbnfKniwCNsNffEptxONZOtCbpEIjp-Vgyo1Hpn_OG9_YPPeFM0skj12Jj-va0puVOLPW9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=DLYJcW2SSCfpFAtvP2_TQYElBtyCE1IM72Q4OTU7fHLd0vAD5oMWk0yObkCx4ZCMUQU0062Z3oJz5bAJhq7G9QsBCqPQJhuCu0UMu_eCFTdYcaLdQmYF1hdEqxRIb05ErM-VuCjn1TUo9tVNRZBXPnNY9Hwqc-g6bqY8Yx_IAMbrQs-KR0vHjES_j8uIdNQUZUPBHWwSIJdb623FP7Zs0x75GJXt9S1OCZBmb96aK3EJly8MUQIkEOvzNfK69Eje2lYbiolND0_OwUaceL1hMRdbvvJle0tSvqc8fOpT4ip5RLDOlzMbGCjfAnYKxtCLyrwQiwWo7NmgJ8R4mPn4ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=DLYJcW2SSCfpFAtvP2_TQYElBtyCE1IM72Q4OTU7fHLd0vAD5oMWk0yObkCx4ZCMUQU0062Z3oJz5bAJhq7G9QsBCqPQJhuCu0UMu_eCFTdYcaLdQmYF1hdEqxRIb05ErM-VuCjn1TUo9tVNRZBXPnNY9Hwqc-g6bqY8Yx_IAMbrQs-KR0vHjES_j8uIdNQUZUPBHWwSIJdb623FP7Zs0x75GJXt9S1OCZBmb96aK3EJly8MUQIkEOvzNfK69Eje2lYbiolND0_OwUaceL1hMRdbvvJle0tSvqc8fOpT4ip5RLDOlzMbGCjfAnYKxtCLyrwQiwWo7NmgJ8R4mPn4ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=u9Bau5IUhFft3RoUzgg3tJ1tMydlvrX79ttuNrtPFnAWJ8QUS5Bnz7Fz_ngapqgR2ZgvL02oMf9sDRabvuFE_ay9NIS011VGDp0k_PoDluTOaA--6dn3Jz2mD5YhROWNLKrZ7yHi6RvDTtijRZy5XiBaqSoguGTwacgFxvwJmB0XToY3agCrnpZrvnNZ1USJIZnNBB6sr648okil306IhpgLWtSDhPc5IY_w3yq7tiRkRWqzA14oSg2B2qsrMqEpOTTWEpvVcgVvvmK0RtLN7IjFvsRMhidAWYTzVBXrsp_xjXUpEk8q33sEZsRVhXNmuZw0vdqRE0EaxoPGcY36ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=u9Bau5IUhFft3RoUzgg3tJ1tMydlvrX79ttuNrtPFnAWJ8QUS5Bnz7Fz_ngapqgR2ZgvL02oMf9sDRabvuFE_ay9NIS011VGDp0k_PoDluTOaA--6dn3Jz2mD5YhROWNLKrZ7yHi6RvDTtijRZy5XiBaqSoguGTwacgFxvwJmB0XToY3agCrnpZrvnNZ1USJIZnNBB6sr648okil306IhpgLWtSDhPc5IY_w3yq7tiRkRWqzA14oSg2B2qsrMqEpOTTWEpvVcgVvvmK0RtLN7IjFvsRMhidAWYTzVBXrsp_xjXUpEk8q33sEZsRVhXNmuZw0vdqRE0EaxoPGcY36ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=he-TvTsovVSU8LT50JmAm0Zwtu_WWxzdOwccsepPtTlF1bqyqTGaTGSyVRszEXAd6gZZl2nZRWKrSj-lE2sxTSRlX0WCzneZWuWZyrUUYq9kDJXNPviIQqW1oNACmGmDOshkq9Dju44aCV-7LThQPHydaYdrghySkCWuXmBpT9zycq3DYdUJoI41ujIALqoILYTdrTBuoYutsjMd0xR-LpL3DZyXvx_0CnJh8GME9P5pnltbWSbOCenekVzomnTT-s5v4QnX2ThHEuiWSQZRaKy1MRi6Wh1RLESzSddN7oNrPTNLk0x7f2_gMYPqBHuj-PBGGoCaCZVdvyNHRWCrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=he-TvTsovVSU8LT50JmAm0Zwtu_WWxzdOwccsepPtTlF1bqyqTGaTGSyVRszEXAd6gZZl2nZRWKrSj-lE2sxTSRlX0WCzneZWuWZyrUUYq9kDJXNPviIQqW1oNACmGmDOshkq9Dju44aCV-7LThQPHydaYdrghySkCWuXmBpT9zycq3DYdUJoI41ujIALqoILYTdrTBuoYutsjMd0xR-LpL3DZyXvx_0CnJh8GME9P5pnltbWSbOCenekVzomnTT-s5v4QnX2ThHEuiWSQZRaKy1MRi6Wh1RLESzSddN7oNrPTNLk0x7f2_gMYPqBHuj-PBGGoCaCZVdvyNHRWCrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwFRSrq16r7s1HNSM0mxeA7cpsqO6xyL7gqgJlTF7NERcG3NU4i3-9NK-JjTmvbf7RihAAYrM3tMxHkktTfC-YQZvuzO8uFFvZwrTjAcxpEb5RbUnDMXBlp_Ufc3UsPT5FSAtXbqOSr4JfamgNcDmw3vETUC-xrh8ph9g0Z8ImBctB6JR3waPxNbzWd6DCJYnLTrtjyFTJJRYZUs4nETqhpB62LsySF3IuQoVZSzcelumewio8lGcRHx9Pypoh8i4Gm0nySwARjIx325kE9F_bZp1jNC5UPUuSFoJzUnZTmiW5Ge9ld4T2u4gmY4MlKKJHSoo3Ur4Lvi1NuoXsqu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=SyLfZtIFBMM33K3rE5H9qrAkmKCfSWrGazow_ci4FcZhJ6_Qui2e8cCRajXR9k3uO9UDxwcnfSdNHqt6Hgxw_qcLH_GYksnDW9TSs76KJN1ajDutNNPtDm-L5_kTfN7GkOJtAVhyNIWI_RPW9RwLg_5KFo6xVnxJeZ_lxrBAKqgAMQLpbvbDI8iqBicwZaJrh7crSQTntrDsM00ILWJGavm_cn77jXlLbWzr6PpUPmfank9A48-vVm9GjMarHF773mssPdFZvXzLoJQUyQ7q7E8lq8s6jvfYfTeUUWautfVkTKFhTfjon2z5hWD_99LkqLH3Dv_Z5P2VZoL6fe4WLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=SyLfZtIFBMM33K3rE5H9qrAkmKCfSWrGazow_ci4FcZhJ6_Qui2e8cCRajXR9k3uO9UDxwcnfSdNHqt6Hgxw_qcLH_GYksnDW9TSs76KJN1ajDutNNPtDm-L5_kTfN7GkOJtAVhyNIWI_RPW9RwLg_5KFo6xVnxJeZ_lxrBAKqgAMQLpbvbDI8iqBicwZaJrh7crSQTntrDsM00ILWJGavm_cn77jXlLbWzr6PpUPmfank9A48-vVm9GjMarHF773mssPdFZvXzLoJQUyQ7q7E8lq8s6jvfYfTeUUWautfVkTKFhTfjon2z5hWD_99LkqLH3Dv_Z5P2VZoL6fe4WLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=UEpEM-MoTK0QPuwylaGAKZHg-b7x8rF_4ueEBau6pNfSkEJr00waNnUFtoozBlRkNxPMwM_W5EJPDiclD7H4GJsciNVMObBPqeWB9leLt56mQy4mk84pXSCUt1aATqidUMlFHammBUfgcdZYh6aWXaC3yMgp8jzdyj2ddPAhJxh88LcjEvfuzkuSaULq3DYE_LISVx37wY5cP7bBFww6a0XmM0O3OOjyLtYbVsLwsh3BFqAmeCFldSRBPhXlnM7HPk8HdR31YErlSDFKdAP4BAoUOp6ste824Sro-22ovkkceHXbi-aXclttXghsoZo56yHsJeoslKpTeU-cZ3r6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=UEpEM-MoTK0QPuwylaGAKZHg-b7x8rF_4ueEBau6pNfSkEJr00waNnUFtoozBlRkNxPMwM_W5EJPDiclD7H4GJsciNVMObBPqeWB9leLt56mQy4mk84pXSCUt1aATqidUMlFHammBUfgcdZYh6aWXaC3yMgp8jzdyj2ddPAhJxh88LcjEvfuzkuSaULq3DYE_LISVx37wY5cP7bBFww6a0XmM0O3OOjyLtYbVsLwsh3BFqAmeCFldSRBPhXlnM7HPk8HdR31YErlSDFKdAP4BAoUOp6ste824Sro-22ovkkceHXbi-aXclttXghsoZo56yHsJeoslKpTeU-cZ3r6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=QXHTOIMSCkIInOVVTlnoh3gEfjFX40ga4_FaZk97p4TjlJVfAbCrme23IsTyv2Hdzli9XTGRB-tKaar-T8dyOUm0XVMzNPaMdZUR_K4cULUlAizy5cjgmu0d5hlrNAwTw6HhQd5t8bNuxM8eOvQfjoE_BqR8D3GSAUZiKk99sFYR-dy_zc-tuw1eNUaF2yvshG2Zh0ILxPKZAlv6EDQbi9mS4GKBJ2NHr4gzOZ497kghF16tVoDkSPDWFHl6S4iPeCsLctlSsSBaFbFUn8PhqW5hRKbH1TjwidIRyY_johZ4UgWKoYwIzgmZkDbEQ6KJpuVpajMamkSdC01AcGLAHwmCT5wioqvrOpalYVFGY_t2yXjMWV1zavbF0HjDgEzl0A8bKoGfwvV8N4YLN0RJjoQe24Cgr2HlEzqXGwQ-GzxFyY8QBU-SsFYSXCwZbBu-fUmO2-NXjOPW0i_sRwNZgmJTz8ZoFuGfnp6zp7HwBmw62mqgFajzXBtra3J83CvV1shaIjAB9P2Oi8jHjBpNzVARyi-ZYPWXPAJShYVrWu05uqTFY66O2FG-B6v9_2uqE3oV43pQgh-qNB0NI9wn-J857ETG9gPI9lhTgVoCO3mMpqVkxUEKHifgQKCp7ULOBmibt3Mmi8_Y6oGibwKs3R7yot0G9TRyJP8eAQO-Q8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=QXHTOIMSCkIInOVVTlnoh3gEfjFX40ga4_FaZk97p4TjlJVfAbCrme23IsTyv2Hdzli9XTGRB-tKaar-T8dyOUm0XVMzNPaMdZUR_K4cULUlAizy5cjgmu0d5hlrNAwTw6HhQd5t8bNuxM8eOvQfjoE_BqR8D3GSAUZiKk99sFYR-dy_zc-tuw1eNUaF2yvshG2Zh0ILxPKZAlv6EDQbi9mS4GKBJ2NHr4gzOZ497kghF16tVoDkSPDWFHl6S4iPeCsLctlSsSBaFbFUn8PhqW5hRKbH1TjwidIRyY_johZ4UgWKoYwIzgmZkDbEQ6KJpuVpajMamkSdC01AcGLAHwmCT5wioqvrOpalYVFGY_t2yXjMWV1zavbF0HjDgEzl0A8bKoGfwvV8N4YLN0RJjoQe24Cgr2HlEzqXGwQ-GzxFyY8QBU-SsFYSXCwZbBu-fUmO2-NXjOPW0i_sRwNZgmJTz8ZoFuGfnp6zp7HwBmw62mqgFajzXBtra3J83CvV1shaIjAB9P2Oi8jHjBpNzVARyi-ZYPWXPAJShYVrWu05uqTFY66O2FG-B6v9_2uqE3oV43pQgh-qNB0NI9wn-J857ETG9gPI9lhTgVoCO3mMpqVkxUEKHifgQKCp7ULOBmibt3Mmi8_Y6oGibwKs3R7yot0G9TRyJP8eAQO-Q8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=bVZZ7SRoiZTZPcP1edjL2WG0xKKENJcsxX1sWIA-Pk4nmZ4EA0VDmwNImlx6Y0MSWsIKAnrFV21hWqWhI-ubQt2ynfn-NYMZApeGr4IXaKWyH0h1PFrVHroNASRfvpyrTNVBCAI14ReMJeZDHKOwcNWBNfrR07qzw9zAKGnOBCkByjWlY8xKFM_u1L2pZcXJg5HwfhxBbm5_jY_5no5G9Yo0ZtvgB0DYFrXoF9S24vpPOxwJBPRkV6czgR9Vqpgi2Wm9PvOgd15UnDWPYeFUB2lBtnJqFtL--LvamX76j9oVHGMnOAnKql8uLjI4b50enLVdCXPHdTxkG_yhdc7DVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=bVZZ7SRoiZTZPcP1edjL2WG0xKKENJcsxX1sWIA-Pk4nmZ4EA0VDmwNImlx6Y0MSWsIKAnrFV21hWqWhI-ubQt2ynfn-NYMZApeGr4IXaKWyH0h1PFrVHroNASRfvpyrTNVBCAI14ReMJeZDHKOwcNWBNfrR07qzw9zAKGnOBCkByjWlY8xKFM_u1L2pZcXJg5HwfhxBbm5_jY_5no5G9Yo0ZtvgB0DYFrXoF9S24vpPOxwJBPRkV6czgR9Vqpgi2Wm9PvOgd15UnDWPYeFUB2lBtnJqFtL--LvamX76j9oVHGMnOAnKql8uLjI4b50enLVdCXPHdTxkG_yhdc7DVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=heiBohUNMyFKZ2Zeu-8nY-TF54-9E6L-YLDkoLSKrQi4IFQbzQBi8Myi5EGisHz9ewpurGItBKR74o8O3lxCEAOS6ff5EsZhoctOun8OYK0_4V97_sTcRHH5mp7muIyAVb7iKOxIfT1yJlMFIa_aiOMaDFITYPbh43BjDS_dUXltsfB7NOaoby--10VQRmb3xiZO0AE9B89i0vzmqsTkAjEjxYoeUitdInGdnTzNpqqEcUYiB8wT5qnu67kpiiT4PyNSXhFoBzY5JASQVzG4m-j1KDf6pEohKqueLvHvJ2Rs_tz1W5kv19btMkvLFDnlpB82Q5xU23wYJw-tV4_1cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=heiBohUNMyFKZ2Zeu-8nY-TF54-9E6L-YLDkoLSKrQi4IFQbzQBi8Myi5EGisHz9ewpurGItBKR74o8O3lxCEAOS6ff5EsZhoctOun8OYK0_4V97_sTcRHH5mp7muIyAVb7iKOxIfT1yJlMFIa_aiOMaDFITYPbh43BjDS_dUXltsfB7NOaoby--10VQRmb3xiZO0AE9B89i0vzmqsTkAjEjxYoeUitdInGdnTzNpqqEcUYiB8wT5qnu67kpiiT4PyNSXhFoBzY5JASQVzG4m-j1KDf6pEohKqueLvHvJ2Rs_tz1W5kv19btMkvLFDnlpB82Q5xU23wYJw-tV4_1cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLvA3WYeFU05soMDYhXvq02a_wDcKbhQqu7bMwaPeBiR1Yuslaas24lc-dLvgLthObAw_11p97wASBrICTufAAYfNtMCCkm-H-G4HyP0JKP6LlsXUoiktoEwctiCZuq_Fbqs_0XL8zhMvP95OJ5wffRxpplHpX2y6alx4dND0Atc2fKg9MR0ANsa_r1kd23x5An0zByqHNSDK2bI_BqqA5Kv7qn7BdMMuJTuuKmvIb9cc7ux3zWMwJ2hfu8stJ6LOlpCdoqqOMfEPW0NgNSd3fNz7jyBY9pU6bp7J0wII7BMPSdzaJeHtlUZHuZIc6zGuU3xkaF9j9neagh2lHVLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OW_G2kqzWORns2US7rfxXbs2OZvb4VGa9xQ8XdiRVQgYCvDUg5a-R5UUXocRMY2ZLi1DpFPpiCp2MzgTW9Z7hMRipl8yemr41Sl27fKLNsfOuAyYkw9eJ1WTER3-M5Zqjkh0YC2FhTZKFkE1LEOyhyXNDo6JWty1LfZ9doX_vgkk3_bXrQgvlw0_UpxFHEqOfa0Nz0uWpkSUGWofvSy0LTE4j4KCHYFZbtYkBNrkBD4_AllxlGU5g5eI38_IS4T2imhvRnHUQtd-GQ9Zz8bER0OhmtiIMos2qlRuHdJPMsZdY0AfTUVXGSi2zwAfDJ1-7PWhLPglSmJPXIULT6cgyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=r4N38DKB8E6aLNqjDuV-8cgd44U9V7aEbNze_qB4JUO1isLt-eh6hRZW1QfaUGAVYuzabJGykU-Qc5P1cEpBhdqL-M2-A3wKEt2BpIFadwbfy_qzGYEd4OZc6oG2AO_uzCdncXP1CjPGuHkNDmc7RlHjVxzchRG6PFZrfu3RMn2QWY3Isby7wzD9xP05ugxBIx1mvu8fBn-9yFkbJatr0gwtG-L8-z1CO3-49HMPx3hjNupseek8PNGHyuPcBrNKx4Rzw8WA458OznwUp9M1cbTesTVtnT8oYN7Abm79Wsjg4qKVyUpeIVCh9sI6lsqpUL6ovcs3Dvig6Ul-0tlbg5zjxKkojFddQkQo3VkZzJsWKEsclzTC_nXQS8pGs41SZTaORwe4i3ziZThOxpPiay7-kPukluEsJpP54tSosKMprijIecFOIqT7OFB8vUOp1oBC8O834a1jiQXKVCba7KVfYm6vzHPnSHSX1PBHdF46UfQAgS2HnU0El-yZD-1F_W88j5VO09iH9YdlAXagan-63xUvuf6cKIwSdJFWFpy06Buvw60UxHM3jeBg83kY_wYitm7eCHunJv6Yy6RZ_NM8RbTPksuUU49K10zp85iFHA9ZXTqLkytX8_LJarSrPJgLYp4NsUuqBw4kfaPKMF_TxkUWXMm7ciQn_DVvInQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=r4N38DKB8E6aLNqjDuV-8cgd44U9V7aEbNze_qB4JUO1isLt-eh6hRZW1QfaUGAVYuzabJGykU-Qc5P1cEpBhdqL-M2-A3wKEt2BpIFadwbfy_qzGYEd4OZc6oG2AO_uzCdncXP1CjPGuHkNDmc7RlHjVxzchRG6PFZrfu3RMn2QWY3Isby7wzD9xP05ugxBIx1mvu8fBn-9yFkbJatr0gwtG-L8-z1CO3-49HMPx3hjNupseek8PNGHyuPcBrNKx4Rzw8WA458OznwUp9M1cbTesTVtnT8oYN7Abm79Wsjg4qKVyUpeIVCh9sI6lsqpUL6ovcs3Dvig6Ul-0tlbg5zjxKkojFddQkQo3VkZzJsWKEsclzTC_nXQS8pGs41SZTaORwe4i3ziZThOxpPiay7-kPukluEsJpP54tSosKMprijIecFOIqT7OFB8vUOp1oBC8O834a1jiQXKVCba7KVfYm6vzHPnSHSX1PBHdF46UfQAgS2HnU0El-yZD-1F_W88j5VO09iH9YdlAXagan-63xUvuf6cKIwSdJFWFpy06Buvw60UxHM3jeBg83kY_wYitm7eCHunJv6Yy6RZ_NM8RbTPksuUU49K10zp85iFHA9ZXTqLkytX8_LJarSrPJgLYp4NsUuqBw4kfaPKMF_TxkUWXMm7ciQn_DVvInQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkUSJsCWMfGO-dTMsRqIPHc_uGT4KfW9mVrgI7gOt5y6SZKh7QR1wuksVn6WEYTHQxbSW-BstW0yDRzn3ZmWNiLcEYvwYQ2B3qw32bs2LCZpaUXkF9rEref65F9OoEOyS8r9q-IlPg_oBb8vx23botanq7eokCSZJOs_UESJgmNjWtd-N-s6XfGv_79HXEbFxKrsWGOFdY2yM3aYntpCVdrUBRLu1PUELVKz3KkCNRUebYBbERUwPxOJgeE5AvrRmSzNDV2FFqx0opag6Ck4uCbtf9ZEfp6_wI5Y1QGy1IL4SqDrdLNSXNoD6FrQ8iNn8sd3OdnwuQhi9owIbd7SnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eb-ILzfESUaUdS2UCZrfoat5kdE4PwPlfowRjF7zwxZW3tCzxn8UsO2ROMZ9SdTOHpcGEiwdhOy41C2vmH2h3cx3Hiw7ObSCeqqrZ498FYFK0M8FvJzDhM4FDu6S12NmUw4p-bvdLaWxHK08xoqD9krVLmnFfIghv_RXNRod_-qw1XSsNkVLCeqCVBoTiaiQbn42cu_T10ulykJm2U6fmWRmdejdOTt_fbB0-ubY9V7XAV_TyAKAlMhCmuNRIBIrHwGMYddlcXQuVPbfzaLQASnkGSUwE-rPwszbtArjZzkUDMMHIwLfWT9S_OEejTJTtnFHjydWtbGLgjmYhwtLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdfHX4APgvsEwgY-MgwVBofv8tIj0Uvg01rKDY18n1E0bw2sUURO8tSzuYsHrdYWi7iawOvnvf0YFfAVH93kckOkD0-JmaJ45bGR7OA_xfXdIYSiu-46iaQvzQuv03_fzwyBH54LyzQTesZiuCDV2JlY94LquPCrvlU05H-l2mFES3A5127YfO-CCJlBKoLgis6CwNQ7A0vfge7E-sqXdxQNunKeuvoXxb9xvLrLG-g3pofsN4IosUEidMWi31Mss-KW84kxdXCU5Tcvo-Ryl2Goo_OCt9WwJQUHRu4ss9GJZTlJoXh2cSdjX4JOpnsMGFZdZTsENIMnhxIfcVRf9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ9k5DMrqwpAdWr-L0AJe4EZbSvig7vOTK06L78L1rtJRAVBhnDh_Hy2aowLPs3Ej2zBEzY2KLCkLxLwtNgtHRNCYpyUthU7wqiXvDcJSvwzIfKMMMKo4APz78KOkeZ0CknNXnvJwX1Y8gilFBXjGQle-OkcOyzktW9PdH7BrNJZMNIm127u_ggK3n9RjCRNCQsLkL-FVSQ8ygtMEdBBSm91TXvF9DSMMi2YBZae2ChWNIO2uH4-eOzW9lz3no8bMdTUx0bzwB2xpQGQdBDDTM4LJLvffs97h2hnPVS9R82ZoGT0XZW5aVQZTTq2vpsIdtohE03dUG0b2BXengKPzQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=upImJacH8q9m1EZbE0dPk403LynDpl-zJ6kYk-cH4yyWiDHlnXZpYUwTD86kZiye80Iycs6xFdzkbI2bRCQEYJnU75GBot7KuJ6BhL2lF2WEvW71TJJ8WPGg2uY8d3Z9Qk2k9URTsLea9VEeSa_6MV-gaKqzoUOehz4l411PSt05EN7remJaKWPVu3IA8FTzQSq7LTM5W1ukMUka3IABJG4hYiEGe0nmJXSnkEV_zrWqS_PK9_EV2_goH4ZUV89T-Bv_J6n6eY1gGH6bUWHQeUoBwy2rpM5Ma6PIT7qt3m52CD9m6l4Ss7Yrv3nT91LCigSISAoBfD-cBsHCaAoEdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=upImJacH8q9m1EZbE0dPk403LynDpl-zJ6kYk-cH4yyWiDHlnXZpYUwTD86kZiye80Iycs6xFdzkbI2bRCQEYJnU75GBot7KuJ6BhL2lF2WEvW71TJJ8WPGg2uY8d3Z9Qk2k9URTsLea9VEeSa_6MV-gaKqzoUOehz4l411PSt05EN7remJaKWPVu3IA8FTzQSq7LTM5W1ukMUka3IABJG4hYiEGe0nmJXSnkEV_zrWqS_PK9_EV2_goH4ZUV89T-Bv_J6n6eY1gGH6bUWHQeUoBwy2rpM5Ma6PIT7qt3m52CD9m6l4Ss7Yrv3nT91LCigSISAoBfD-cBsHCaAoEdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=btvF8KLOQzYenNxzrH9OL-neV7godeoYQX4rMQdjeuVpG5I9j5g3RvxdgnpG3DhVBG1BXWUcxZbImvQ-c0Dp0GRL8STSvVChtEWpr4AIMHiFSBhEuvFEQ8fiyH2t8m5YOCVSigb8KsiWwQoyi4_fGt6sADrqVszOQnhtJXmKBdExrN1RDl-_78SvxYEdKo2d-rzEQ3n7zxvAl2XDLytbJ3S85ZxYWZk16msOLVpIb5OJvRB9z3Fo0GG0OtT9VnSXHYZ8ElWM816i992T6uRbuchjJ62S_2mjQuuT5aARIPBkXR7puRslN5gSDf3VmWi7pGxpfRudlxxOQH58fg0RXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=btvF8KLOQzYenNxzrH9OL-neV7godeoYQX4rMQdjeuVpG5I9j5g3RvxdgnpG3DhVBG1BXWUcxZbImvQ-c0Dp0GRL8STSvVChtEWpr4AIMHiFSBhEuvFEQ8fiyH2t8m5YOCVSigb8KsiWwQoyi4_fGt6sADrqVszOQnhtJXmKBdExrN1RDl-_78SvxYEdKo2d-rzEQ3n7zxvAl2XDLytbJ3S85ZxYWZk16msOLVpIb5OJvRB9z3Fo0GG0OtT9VnSXHYZ8ElWM816i992T6uRbuchjJ62S_2mjQuuT5aARIPBkXR7puRslN5gSDf3VmWi7pGxpfRudlxxOQH58fg0RXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgTx4A3FO-OF246FUX2CqTI8Rm1R_s4PhGWjbdVz_1UA-2IGr0ERZA_vdO-SxwtSaUqaaZnfVlo-cemJO3ytlMzyYqTPxpOfyS9EUhduLOD8FzEahpOMA3YnMeg6cXE4aTnaCVBTU0SEfpNt1dtJ_6iDFKO6EOCJJACyYdU167VHxf_0qcF0ryn3JSXeFONYxTC9-txzKC6qhZ-oKNM6-9pcy6nKbvu6JRMhreTykkZCyNaJFQ6oufqS7gNCrbeJuvPTKKkBg7q57hcDmFwb2PNeYszWMQxcXzLQBC_BlFg-wQ-cNf3SQ-FYU33NLZCkILIVi5c40yr3C6JDju4Gjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=vXJdZuDpjnkQUt1c3lDJX4z8gq7eqfgG8HWi0fHe-9qLt_a2tsi1mBXYUfWWdlKVOHK1jIP2PF_NAOy8W379_S2rJwviiEOiQNV1GA5ATvIymmYifQASLRb_sRsAW94rsJfctP114yS1XTpxeJEorZ6SxShsSNRBdMrfOc6Zf03qfdDSidN8Mu6KsHCRDo8h54XE0su8moVTFlACxZtXWHIw2M2Yt48MS98pUVyMKM2p78VBuuIjYWZqUGOiiB__8DDA7ay1WIuUuw59tTXa20Jk7Nd364P5Grh0wvYOfwpWyA5dPu23h_v6_uYeDsBE9divdywR2doEdm2-X5ILAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=vXJdZuDpjnkQUt1c3lDJX4z8gq7eqfgG8HWi0fHe-9qLt_a2tsi1mBXYUfWWdlKVOHK1jIP2PF_NAOy8W379_S2rJwviiEOiQNV1GA5ATvIymmYifQASLRb_sRsAW94rsJfctP114yS1XTpxeJEorZ6SxShsSNRBdMrfOc6Zf03qfdDSidN8Mu6KsHCRDo8h54XE0su8moVTFlACxZtXWHIw2M2Yt48MS98pUVyMKM2p78VBuuIjYWZqUGOiiB__8DDA7ay1WIuUuw59tTXa20Jk7Nd364P5Grh0wvYOfwpWyA5dPu23h_v6_uYeDsBE9divdywR2doEdm2-X5ILAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=k68S3_9FN4U6SLovo6EJrHBn-XfRXxB7rJdpY9qeauj--PGmn8gO7FyOWgZa4xyAsTIuocmACoCZ7-VEOPmwwjeLpoZfloQaKY-O6aYgpayy8h91xXYxVxtEgLJtWaburvWMtrzCWmXJnLx5y3oUKCZDmLWYgHbyKwEraIe3pLFby2PtP2-Gty0s38uKmuiJC4ctkLptsVfBhPN7oNO6hG-CmmfFvTBDspa7E_gA019uREdAuzEQi9xu4JOf2WCJI2XnTBREt5zJYvieE2fgenOtHQ0p6qZqBejvzGht_bO6N_8uhORoJHZ3Zxi7jKHkpFtdh97tTm2CqQy_ll947w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=k68S3_9FN4U6SLovo6EJrHBn-XfRXxB7rJdpY9qeauj--PGmn8gO7FyOWgZa4xyAsTIuocmACoCZ7-VEOPmwwjeLpoZfloQaKY-O6aYgpayy8h91xXYxVxtEgLJtWaburvWMtrzCWmXJnLx5y3oUKCZDmLWYgHbyKwEraIe3pLFby2PtP2-Gty0s38uKmuiJC4ctkLptsVfBhPN7oNO6hG-CmmfFvTBDspa7E_gA019uREdAuzEQi9xu4JOf2WCJI2XnTBREt5zJYvieE2fgenOtHQ0p6qZqBejvzGht_bO6N_8uhORoJHZ3Zxi7jKHkpFtdh97tTm2CqQy_ll947w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=oW3jePGhOGuHVoN4Zf_KKQQDwc9icohoJF3vgQszmo51VG5IVuO12b8BnRs3kMLcUZHIeh0202VAgGXB01d6eQxWaVFXJMTw6NzRbSX7IdXGoYoPbLgRDRoM922c4LmhZTjxKbmJoiVDoyHSEQb8YEpnijC24iM_GVtY4iZ0u7_-4q_XVEJc8a6im2f4YZpZW8uVfdqJnPgdoq2zl1SmO3I60hWnGS8IXE7JEqUlXuUjqSy5CydXgwPmpNEDyIwLVY_4AFZiRRlB-KbsbCdR9lrCOfQXBuAbxwKWjW_KjYKQr-AUeMYlZCGSn-pxalIsG-5om7yNrDj-1NGj3ev2AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=oW3jePGhOGuHVoN4Zf_KKQQDwc9icohoJF3vgQszmo51VG5IVuO12b8BnRs3kMLcUZHIeh0202VAgGXB01d6eQxWaVFXJMTw6NzRbSX7IdXGoYoPbLgRDRoM922c4LmhZTjxKbmJoiVDoyHSEQb8YEpnijC24iM_GVtY4iZ0u7_-4q_XVEJc8a6im2f4YZpZW8uVfdqJnPgdoq2zl1SmO3I60hWnGS8IXE7JEqUlXuUjqSy5CydXgwPmpNEDyIwLVY_4AFZiRRlB-KbsbCdR9lrCOfQXBuAbxwKWjW_KjYKQr-AUeMYlZCGSn-pxalIsG-5om7yNrDj-1NGj3ev2AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=gqnE5X2chOtduvfO1GoY5cr9EbGwYHyJvaMyNfpWln027e9d2SFs9ibg9Ex0ambHxtk0WYyh-0qFzxFTb0Rhrg2CxbUUJAYh3d_F6ovQJK7LX2Isha7vcdKW9zvfslJ-hCR5pINZjv9ts_j7V_NmHJkUsItxzlk1ei0KPK8ZfunfxcH4WB2qnwxJfnSvdFfOZ-Wl8P7UOt2VMTN0RWS32Nh-pFd4SBRHlOj8jzLXZea8uOa66p-HjigIROCU4UeC1hHwHZZH0PTkjYAx9A9bW3w0AmzjssrmCowiozscks6sqAaM5UcFMCeKvFvVkjAsEFvbEfjlNsqWI9zWcMe2ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=gqnE5X2chOtduvfO1GoY5cr9EbGwYHyJvaMyNfpWln027e9d2SFs9ibg9Ex0ambHxtk0WYyh-0qFzxFTb0Rhrg2CxbUUJAYh3d_F6ovQJK7LX2Isha7vcdKW9zvfslJ-hCR5pINZjv9ts_j7V_NmHJkUsItxzlk1ei0KPK8ZfunfxcH4WB2qnwxJfnSvdFfOZ-Wl8P7UOt2VMTN0RWS32Nh-pFd4SBRHlOj8jzLXZea8uOa66p-HjigIROCU4UeC1hHwHZZH0PTkjYAx9A9bW3w0AmzjssrmCowiozscks6sqAaM5UcFMCeKvFvVkjAsEFvbEfjlNsqWI9zWcMe2ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE3jRojy5hYNE6nLC9qbKIS8pfoDWY-9NhAJxfCXfutNI8DGCQ8wpQTVpZkZUTbJicpIoQsLVr61bY4As7us_MBSsIO29aQKSCQjplRRHb-o_YN5ASCr_YfGiL7urPiOyEJFnYuMB7kawSCrGteRyxGsJeHlpWCOV-ej_bzmByRDEE0RunXLY4oDHrCHHFODjzZuXiFQ9UW-aYcyQWn0BbaQGYN9k9wezDwd52GgP4H2P7WE2PvKz4dnE7JCwFDAHwlcVI2Vugo3AA0guCmrKS0bJCpJj2ckgYKV0HNWHyOm8V23fuGWPvH2S5dPKOJHitYcFMML3sM0j9KSSwGvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxqGie_PI6Gb1J21zwj4jMKzGfJY1PegARBt2vrY_B7zrAF9qCUJ0I6AggZoBlDpSFuR3Uz-pNJDeQmt8-hFjqMUmr2bRQDmNtehS6DyJ2RZcz9d8bzh3a-rXh8kluDb8BANah-OswgiBmmeDnniZMalXOiXVGt6AaYc6IujBrZiXYM_ETUMgUS2CgAUa1oVuKbpkm7KLmnCaRwbb49FVsQ4zOrClts-31xWmAeFfPTHkSPI8odUTXXbIBbyGNU2u2ifA-Y7EumRnsPwCe7DG5BvJfzhRwQuM1jmSvXCw4qcQOmOIJuLM3dfyKhZJ5pkE6Cp8vO3RCyySgtkXO5JDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=FKlBSltLaWd4dz-0LhWuX8KHggGySjCbhhvFOszw40ucTWIUXRpyll_kEFb3QeW5ylId-NsfbEJe4VLrKJMhhpMd5y4yKEmD0ggsrA3vKWQTmKqu69JUagaENm3iMFtzIIp69x6KN7qkOXgBYOgZhnEFVE3Qq5WyfXGiikLUQvrIbpl80nh1qvQ_EI-meBMEbeWkqLsEHwVJ4cX-y2Os7bEeWyiP4bYRA_5CFYwiFhrzL60pKLZO0LVHLA4bzrbdHQnd_MICbZNiiG0hhAzpOaa-8PuC-PrOcWO2QsZAT4ILHwVut50kxyNtAafD20dZ7jxfhq6Ro9y7YnaVETCxMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=FKlBSltLaWd4dz-0LhWuX8KHggGySjCbhhvFOszw40ucTWIUXRpyll_kEFb3QeW5ylId-NsfbEJe4VLrKJMhhpMd5y4yKEmD0ggsrA3vKWQTmKqu69JUagaENm3iMFtzIIp69x6KN7qkOXgBYOgZhnEFVE3Qq5WyfXGiikLUQvrIbpl80nh1qvQ_EI-meBMEbeWkqLsEHwVJ4cX-y2Os7bEeWyiP4bYRA_5CFYwiFhrzL60pKLZO0LVHLA4bzrbdHQnd_MICbZNiiG0hhAzpOaa-8PuC-PrOcWO2QsZAT4ILHwVut50kxyNtAafD20dZ7jxfhq6Ro9y7YnaVETCxMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0p8WtCktopzcDwShdLBLdkaYzbB0FcDYenzxm2Qpz2TuwpUOr66_JbdoWFtMWbtjLMYqbpue32LOkyydmL9PVybsZDdWVpXwlO0yDVVE0ZSNTAdhiu1Oo0Xeyuzt5H16qcW8jQZ5WmKSMNrqrpvFkrKT-ZMumCZXGfA7sqSRDLuVpIr7nP1XVZtoJ9ZTAaPjDEwC2HsWnlqc25Dzu7cHG4-ePFVLxouEByhviPB94687EjPDQvHk28glq1NTEA3Vdd6MHp0uiQsRkPi2SXKNUCdgNv_5XKP77vfkb7lLqrSkExjV1jrBkp1CgsJvISXBAa2_QbCBZzg5TF-Md28C3t8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0p8WtCktopzcDwShdLBLdkaYzbB0FcDYenzxm2Qpz2TuwpUOr66_JbdoWFtMWbtjLMYqbpue32LOkyydmL9PVybsZDdWVpXwlO0yDVVE0ZSNTAdhiu1Oo0Xeyuzt5H16qcW8jQZ5WmKSMNrqrpvFkrKT-ZMumCZXGfA7sqSRDLuVpIr7nP1XVZtoJ9ZTAaPjDEwC2HsWnlqc25Dzu7cHG4-ePFVLxouEByhviPB94687EjPDQvHk28glq1NTEA3Vdd6MHp0uiQsRkPi2SXKNUCdgNv_5XKP77vfkb7lLqrSkExjV1jrBkp1CgsJvISXBAa2_QbCBZzg5TF-Md28C3t8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=sISAQvyPs1USiN-lxKveV4vg4Jx86_KL7d4aRdYZshTYf2EAQK7yNYUg-xbuQapoKTuenHZE9wam-cOJ4UhgqIntT9S6mecCsW-gyI1tWnUG_O2sBvYQ4K_zs_dxADXoBgW4UVVneZLY4Gggrn-L3mIlrh3qS_jepiN9Gr2kHTgy0atAbpdcGxryGcHCDTHyJZAR4xpnbdqUWmXcHr0xqlW_pWumeCEHX49pxi81tOkBRufNz8aUUAOCB06TPMRepY1xfQyZYBkp77uuzHfA1Nw9TPJsCI7jFrUYNucr3P2Damodev7KQu49PVlUlhBDv87783DimY8aVxQxSWYXFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=sISAQvyPs1USiN-lxKveV4vg4Jx86_KL7d4aRdYZshTYf2EAQK7yNYUg-xbuQapoKTuenHZE9wam-cOJ4UhgqIntT9S6mecCsW-gyI1tWnUG_O2sBvYQ4K_zs_dxADXoBgW4UVVneZLY4Gggrn-L3mIlrh3qS_jepiN9Gr2kHTgy0atAbpdcGxryGcHCDTHyJZAR4xpnbdqUWmXcHr0xqlW_pWumeCEHX49pxi81tOkBRufNz8aUUAOCB06TPMRepY1xfQyZYBkp77uuzHfA1Nw9TPJsCI7jFrUYNucr3P2Damodev7KQu49PVlUlhBDv87783DimY8aVxQxSWYXFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTB0cPw_p2De4VoXFOobw5zWoIvx1joxgNEPU9s5vRC6Ah1dX9nFJ0aa9slumqyZUb8WvznDN0BPigBBiybhNRyDTePbatGjLNpNN360wGJZtNjSn6BJKLdAVT2PwJTVmqFO6KHdO-zRKqoU3CwKpGF-ZIGVECQW647vGeI7u9-87k44keNXz_OwPRJp74rc88djPj6uI4FbNBkKCenQ5DIM6HGjz0Rlk-3vVhLP2AkIXB4MjRIvLDWp97bWjW0_1osNgunhp6GWeX5Z_H7wrTt-6NRkk4kRmh-VOqm-NlM2aGJyW_4K4Qsdg4lsUJDrkufmPR5oVYp_q1EoKZueXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=g01Brqlzsrq9IQqSj9TwEKr0IkUaMElzaGr4GlPqg8oc6wi5tvpOcB7tDQYBZkNuopOxFjYEFVSbvGwULDxxpAPA8OjIMxmpWTVRpwxaSawZV7Ah8eVQKjK1NXmsBUqqwG0qx04J-fAVIISEllfezLVrQX_N0zYxMsfVEUicM_J86IZdohmiu5NyNRDZ-huqcloY3dnN6SizEMbNOQVYcmInJXp3jF0eB4j96I4K9EAXvSoSMcm0c3GUn_eon6gHGPJPYzaTTvRtCzd-Ma2mxI2Y_4TKGRQsMEQb3U3CDWa4eeHkJB1hFZN6FrrXXwj4jedq5OVjdNt2WJJCINIcmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=g01Brqlzsrq9IQqSj9TwEKr0IkUaMElzaGr4GlPqg8oc6wi5tvpOcB7tDQYBZkNuopOxFjYEFVSbvGwULDxxpAPA8OjIMxmpWTVRpwxaSawZV7Ah8eVQKjK1NXmsBUqqwG0qx04J-fAVIISEllfezLVrQX_N0zYxMsfVEUicM_J86IZdohmiu5NyNRDZ-huqcloY3dnN6SizEMbNOQVYcmInJXp3jF0eB4j96I4K9EAXvSoSMcm0c3GUn_eon6gHGPJPYzaTTvRtCzd-Ma2mxI2Y_4TKGRQsMEQb3U3CDWa4eeHkJB1hFZN6FrrXXwj4jedq5OVjdNt2WJJCINIcmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=IFZFA7GpNOTFc9gT0nvME-M6urXCqTi_y_na4yLIAK-Ca6AGJOv7qY8Frea4nXiN0ZDx-v3R6h3XJ-yxLRaxXWvoXHgh9eahOA64XvDG_VlYSoS7ITPSqWqwvIN1dLaclh4UZnXOBMbN4NA8CKATkEUCf-XQne9WGK53PM2iE3yFBTY1-zBUYFHhOOCsukzfWyKsbaXi84Me57PCdxizIgiv6W4RZT7wlBXfd6sdkJhSWoPrkNAZYS6fChNADi2N3Ze_Col-so5Se0IRSGDGPJpLElQEfFox6EIZCbG2WqtbHo26OgET8h0SSjPrLkSxHn5q5KfwymlJ0kS2N4ZG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=IFZFA7GpNOTFc9gT0nvME-M6urXCqTi_y_na4yLIAK-Ca6AGJOv7qY8Frea4nXiN0ZDx-v3R6h3XJ-yxLRaxXWvoXHgh9eahOA64XvDG_VlYSoS7ITPSqWqwvIN1dLaclh4UZnXOBMbN4NA8CKATkEUCf-XQne9WGK53PM2iE3yFBTY1-zBUYFHhOOCsukzfWyKsbaXi84Me57PCdxizIgiv6W4RZT7wlBXfd6sdkJhSWoPrkNAZYS6fChNADi2N3Ze_Col-so5Se0IRSGDGPJpLElQEfFox6EIZCbG2WqtbHo26OgET8h0SSjPrLkSxHn5q5KfwymlJ0kS2N4ZG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=mut7royvf-iJvpUCuVHKHu67o4TivoulwQDCTJBdUDd4KzbiUzvL7uDKSNwr9x8Idhy1Y3SL_bB1TO0EPlZWs-u-X5-YnDjqzDU1sYxu578O9Kqf-Fyl9l2oiYTdD_x6avJQn5003x-xZg5pAQK3ZIiKmO2e7gy4cb9XXNyK_P8ANkbBzBuCHV4VMID_hcFrifL_DUCJL0Mk7GnyDm2usftKGtH3a7GskELwnSXuWVTCJsUocXcfKjY5KUVDa0iywFaz2FzuKBOYyo0CetLQLDDr1as288xMzAkYGQmg8DJiSGtoYA4V1SaLyWAmJ04zSk6Ha8MOQ_F5ww1BSVQQnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=mut7royvf-iJvpUCuVHKHu67o4TivoulwQDCTJBdUDd4KzbiUzvL7uDKSNwr9x8Idhy1Y3SL_bB1TO0EPlZWs-u-X5-YnDjqzDU1sYxu578O9Kqf-Fyl9l2oiYTdD_x6avJQn5003x-xZg5pAQK3ZIiKmO2e7gy4cb9XXNyK_P8ANkbBzBuCHV4VMID_hcFrifL_DUCJL0Mk7GnyDm2usftKGtH3a7GskELwnSXuWVTCJsUocXcfKjY5KUVDa0iywFaz2FzuKBOYyo0CetLQLDDr1as288xMzAkYGQmg8DJiSGtoYA4V1SaLyWAmJ04zSk6Ha8MOQ_F5ww1BSVQQnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=Cc2cmadPoaWLDOsBinZ-4Rh264d9k8anyzNyW0mo74vKTL8XVRyUCM3sv35YYgDblNq0M_fkI8KhYiiLONUQfWssyi1TYL1xfwiHV8-IXLIp2y4marWekwNBanPemik4xNmNQcauMyZcmPN2qbcgtRgTWVN_3yMZWbXcAkAtR3cgJg4hvguCnyXvqVTo4FMY0TUlKRLAYCHd1Iwia_hRcPTchpfBiyBfXS5xzlU_P12LsyjtFYZ6c3XFFcn3Bm7HFw_agWG6YRGkWybdRaK_dHjvm87LHLEOYokV7aHImshmAgU9FTkFL4vAKOgVjyuzA00PPp_ubLH71DRzW4sktA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=Cc2cmadPoaWLDOsBinZ-4Rh264d9k8anyzNyW0mo74vKTL8XVRyUCM3sv35YYgDblNq0M_fkI8KhYiiLONUQfWssyi1TYL1xfwiHV8-IXLIp2y4marWekwNBanPemik4xNmNQcauMyZcmPN2qbcgtRgTWVN_3yMZWbXcAkAtR3cgJg4hvguCnyXvqVTo4FMY0TUlKRLAYCHd1Iwia_hRcPTchpfBiyBfXS5xzlU_P12LsyjtFYZ6c3XFFcn3Bm7HFw_agWG6YRGkWybdRaK_dHjvm87LHLEOYokV7aHImshmAgU9FTkFL4vAKOgVjyuzA00PPp_ubLH71DRzW4sktA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvnCv7fSxXr3Nakc3jCniCNfSM8uzSs4L7vYRa67lO4eywrX8RGHi-9TIu1tQYG73gcUctx1FXpRtACax_yhV0Pk1jXyA540OvX1Hqo1cABznRPH5369s_weTSOt72DAylr-YGo6PKGerytTx8BQQq111pPfZvY8SNewvVk_QWWHrHLgbOvEsjMAN39DcgeTC3txjViqKG79gouYSSCrrICkywDBCbAF_rG9QsNltuEXxaz55qxCz_4sZcbnzFGyHtlUk61Wjo0xOTPEMgI2L6nK1c5ERQlgXO1By5mbiq-2NxEM1JJHbpKQenFh05R6A1N6IrUIwcn66OrkIAf8fw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=NmWBsa2p-khAY6Oxp3cQ_BzAgDX6f2SzGzPpwlxLqiefrgKRY7V9AaXzMCtEvTIkvR088vemZkZQ7lHhEN0w034KGkdOWjPiXLwBhCyDrHKzaxtpAnqtMK1b71pIdm7SK7iz_Q1PSgI9PEKERSEH-TbxRWpHZUvIOgrmxZ2wkrGONNZW1Vl43wM9vUrVX8LFAqUwAJ4ZOsyD7wl-_ohmgJLU9xhM87mTv-r9PSxJcxVQDT4tlGN_Wx6HZeVDtXLNWjaJjexhW_o9ZkeP7haUj0x-1U1t52vzu0JRfl1mgI2M5UHNVBSeO63H7SEjocJFSKHtjaje5VI3wzp6h4Jw4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=NmWBsa2p-khAY6Oxp3cQ_BzAgDX6f2SzGzPpwlxLqiefrgKRY7V9AaXzMCtEvTIkvR088vemZkZQ7lHhEN0w034KGkdOWjPiXLwBhCyDrHKzaxtpAnqtMK1b71pIdm7SK7iz_Q1PSgI9PEKERSEH-TbxRWpHZUvIOgrmxZ2wkrGONNZW1Vl43wM9vUrVX8LFAqUwAJ4ZOsyD7wl-_ohmgJLU9xhM87mTv-r9PSxJcxVQDT4tlGN_Wx6HZeVDtXLNWjaJjexhW_o9ZkeP7haUj0x-1U1t52vzu0JRfl1mgI2M5UHNVBSeO63H7SEjocJFSKHtjaje5VI3wzp6h4Jw4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=fj6sYc3oZHA-VhOmklqZu34fPvrMe9mbKqeeiGiUqJuCRWVyHQNyJ3i79Qzra475Ej7WrFX2b2rVVTCq-CFr5qUXWqmjizQeo7XHNF4hhTQT1Rp9V4JAF5JFEIBM6F1Mf-HVAV-37vyM7Dzk1YZUjKlS_TyfkEA60w0HlJeVcCtkMxrHKxMjA2rWvNfLfjzB1NtTzXQ8Ac56_jjyytDBLOLWUEwl3CUjJ2t_FwqnpKTC121J_VTIN2etI_ZhsAFdhNsuX5ll0mvt8sd-8_KulZNYNMPQFCet0-neu9_2PCVCcltffEcZezluPr7C9BcUx5WUhzvIr-94Xy9V9Enr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=fj6sYc3oZHA-VhOmklqZu34fPvrMe9mbKqeeiGiUqJuCRWVyHQNyJ3i79Qzra475Ej7WrFX2b2rVVTCq-CFr5qUXWqmjizQeo7XHNF4hhTQT1Rp9V4JAF5JFEIBM6F1Mf-HVAV-37vyM7Dzk1YZUjKlS_TyfkEA60w0HlJeVcCtkMxrHKxMjA2rWvNfLfjzB1NtTzXQ8Ac56_jjyytDBLOLWUEwl3CUjJ2t_FwqnpKTC121J_VTIN2etI_ZhsAFdhNsuX5ll0mvt8sd-8_KulZNYNMPQFCet0-neu9_2PCVCcltffEcZezluPr7C9BcUx5WUhzvIr-94Xy9V9Enr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u42IT3IXT6ypXVdA8s7hKXdMBCIhMUQgG0ZZZH95GbOKiDlgaHjw07HKiMK0dgzVRZG5FliF54ypaay0YLnWu9cCh5BfvNw2_lM3kwGlWVGzKiYoPyInWkvYYhOVP87fDrt22ZqtQAs6AvY67CrISfpEbkOLLGg-nmDf9mVjOhqYbvJCTtkSoC4pWuLKYhW7JTYdDzj9Cvmg5rOc9iB_c12YqXQ4COgbz3ZmxETUuB9LDGv7_XsCsMmaB8tqvcTBsy7cG4kpMVZA0zL6srDFanbxCTZ4FNHR5WJ9OEByK1JdPzvHoJWkcG7Ywo0Y73iRwLLR5oAom9HqOXdk7qY4zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=RWZVn8L2jJJLrOdmBEEgW7fFp0UGryvt0MDLUEX08GaVe82W81ovyNyv6MnElXiy1GRG8bf4fPzzcEsZPRx6lG33gVA2EgsIL-LVrBKsI_1DLEFuZ4TBzcpgWdBNZjEt44zrTUE_V0MBn-5-k4pbRaFPvXi4XOSOZ9g0ehxOd5ey-KB4DAhaYwNnbueGXaSCj9zT2CElRlVcXh5x6CvptB_5xY2pB3GOUPVo4QFJHMFGaswtHPcJsXiD7tYTfYWtU4-iEC4IqLmSE86Jz81nvrLETrBVU_FrOHEE4do3ASinrdA8PKcV-6CrMAU4X2xGJbc-PEPDC2IvX_GOevzWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=RWZVn8L2jJJLrOdmBEEgW7fFp0UGryvt0MDLUEX08GaVe82W81ovyNyv6MnElXiy1GRG8bf4fPzzcEsZPRx6lG33gVA2EgsIL-LVrBKsI_1DLEFuZ4TBzcpgWdBNZjEt44zrTUE_V0MBn-5-k4pbRaFPvXi4XOSOZ9g0ehxOd5ey-KB4DAhaYwNnbueGXaSCj9zT2CElRlVcXh5x6CvptB_5xY2pB3GOUPVo4QFJHMFGaswtHPcJsXiD7tYTfYWtU4-iEC4IqLmSE86Jz81nvrLETrBVU_FrOHEE4do3ASinrdA8PKcV-6CrMAU4X2xGJbc-PEPDC2IvX_GOevzWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=m02nmfVH4Q30s-OXWAEV93xAQxsf4VG4Ck3S1wOsd5gNCSk8QsZwTJknGjKB8EcTaiF3D3vyAALccoYOWFJ81Tm-Zva5FOzzBQaBkkakmJXo-xP3MCJvrpQHf-BVRbh8oMpuVk7UyhlgRq-VNgLDdjgumBKi3fSwimmBfefqYnacIiGkLrSSmNRsA0hsuNh8BlzljoghIGFVJsIc7tkQA1u3ryLvSyabz3Y8KhOjwH7jrjiD13-ICfOCTJdUjI2cAy6jyQMf_1Mx042zgCSne9sHXhUXingJv4PYeD9wtllmDmhnREqGoS-Qv7ozG_OYFSCQVSkOXN9dWAsF8tijJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=m02nmfVH4Q30s-OXWAEV93xAQxsf4VG4Ck3S1wOsd5gNCSk8QsZwTJknGjKB8EcTaiF3D3vyAALccoYOWFJ81Tm-Zva5FOzzBQaBkkakmJXo-xP3MCJvrpQHf-BVRbh8oMpuVk7UyhlgRq-VNgLDdjgumBKi3fSwimmBfefqYnacIiGkLrSSmNRsA0hsuNh8BlzljoghIGFVJsIc7tkQA1u3ryLvSyabz3Y8KhOjwH7jrjiD13-ICfOCTJdUjI2cAy6jyQMf_1Mx042zgCSne9sHXhUXingJv4PYeD9wtllmDmhnREqGoS-Qv7ozG_OYFSCQVSkOXN9dWAsF8tijJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwhsrkwH1wNB7rWNHQKd7gv7wDD0lFMQovFiIaBO569j7gfO0-QVx4KfgiUhyhaFl2TmD0L9gqjJ2mTF0rc0ceN24ePk1Gne5blXzwTh9hJhLm6_qtBziHziaE50mT5ddEmURghDocG2L9fzZs2o7UJvfdHBSNuE_ibnOieyBKWlpc-ZcMFjoaewTQ4AG-NHApy33wVLx1MkN-g5pZMCKhqFr62Kk1fuSo9K4LvMmZ6NK0hVO26RhSwvIUgDWQFRYhGm_6pkE70Trfp5Fs7XpGImIkJy3HMmMcibCF37wJt5Uh-TyoOob4Einmrxo0-OGsYqF9ID3C9Qa8WF_hWmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNFdQHUJNDp_vN9HveGYh5YIekLxRwPuu8TSfrhNHTQUP1QVyTj0yeSDPkEPIikXJYr1K8UsZSdyeCSqb3alkJxVB1LFd1nAsHjktsCTj8csefHntRWmTyWT2AoU8XjtWFDQ5xhbM0RlBpN0EAkSQ5kom4mxXQSofqi-GUQmvBRFs8DvlOx4Au4_dpi93F22_F5HXons_yx05EDlx2HL4QXGan9l47bOsAYBOf15zDco4Cf1T7HFdeAtj9sF_Ns1Horwe_zD4TE0W3YiTuDT0c42vF1YXQKqaO07m8ZhzkQZhFuIFIipjfR91_AClw-pgV-QXcXrFSbKN90lXnCw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0MwWQb1do6MclowJQXlv3ayfYSft9LLf24xoQ1gVB_ly9l7r6e4FLR7il8tO8OjPm7Rf92mUPmKHa0lGa-YZ7235BljyfkTcvSGm_iFRCOmWbTvq4O1UvwO4bu-9ErC9GAWFkL3TDaosUoqEeFT_ut5CGipagLFCKqauCnO-RTV3AkcfuQfGExn3NfvpYukLcawkbdPpfhACgJDgbjJQ3-cdTRiFELwXyt6vAw58mA2NsJSRS8ceY4uzB6stD5ud_RdldNeGCU3cWFTAMYtkOcE3ISDNEndbUjWyV2jfpeAT_-1R_7u_qRdX6WISMqYmGKnEC_aCS3lsY-oeRt-Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=XEoyWIrEuviJTySGV21nqHxvrMfp3pw5iusoEiq_g47jjvQdbAuAmY_9iTkJWcK0NIJeyCVjAZAWTs9c4pV2BbGSqArCJUkfgqCxNrJhaLo1gaxSnXEGljYL6oFTmolK15aomTlJCWEisunwPQocCLE7LASfApFczeb-prk5gwqZftTQDC3oNi5ZxzKX0idXx0m_5fKwOKWb5Nou2igoACv3FPBd3QW4oczJr_Xoy8qhcjOSlvDCwhXdj-KZkBS0LfdUvwyGOjDLFqZjIp4A8OLMMtI04UK4xYIihV346AzzmSth9PyGpqzuvWrI3HGeABwRiTeXml-laHrxTZBLEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=XEoyWIrEuviJTySGV21nqHxvrMfp3pw5iusoEiq_g47jjvQdbAuAmY_9iTkJWcK0NIJeyCVjAZAWTs9c4pV2BbGSqArCJUkfgqCxNrJhaLo1gaxSnXEGljYL6oFTmolK15aomTlJCWEisunwPQocCLE7LASfApFczeb-prk5gwqZftTQDC3oNi5ZxzKX0idXx0m_5fKwOKWb5Nou2igoACv3FPBd3QW4oczJr_Xoy8qhcjOSlvDCwhXdj-KZkBS0LfdUvwyGOjDLFqZjIp4A8OLMMtI04UK4xYIihV346AzzmSth9PyGpqzuvWrI3HGeABwRiTeXml-laHrxTZBLEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYwPgMxoY9rkHMwZKYGlYu5XYH4ucfTD17XSlJRob4oakHyTZrQ1qnE0hsjOgNhP_v8EWW0Z_e4LM2w83k4nezDiFnnZux35elZgEZCwZpRDJ1qV85JQ4Ts1XEz04TJkTZJo9cwOBkHHpxCqIz3Tcxjzopwu3wKB3ms078zsek58OMZCICRPhU9Lmu57kqGhzITUuF_qEH3Q-8-FF1Yha0qnYexcUwyjZeg-pmiblzO-U4V8KZXqTc6BoCU1Xy1th591Rmk8suGit86d_zBU21oigYc678QCNigTkiTot5hcLxwKulIKofpv1uw4YNdoIY-NP4UrFHnu8ww5ws5TqVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaYwPgMxoY9rkHMwZKYGlYu5XYH4ucfTD17XSlJRob4oakHyTZrQ1qnE0hsjOgNhP_v8EWW0Z_e4LM2w83k4nezDiFnnZux35elZgEZCwZpRDJ1qV85JQ4Ts1XEz04TJkTZJo9cwOBkHHpxCqIz3Tcxjzopwu3wKB3ms078zsek58OMZCICRPhU9Lmu57kqGhzITUuF_qEH3Q-8-FF1Yha0qnYexcUwyjZeg-pmiblzO-U4V8KZXqTc6BoCU1Xy1th591Rmk8suGit86d_zBU21oigYc678QCNigTkiTot5hcLxwKulIKofpv1uw4YNdoIY-NP4UrFHnu8ww5ws5TqVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=CyZ_upZvgr7Ic0XIoNYG35VwqgZB_eWdFf9ibGeXo0SEOvneU0-TuFh7e-Xk1uCO6KOfU8GWUg6BEgD3iZKqDzBaTD-3_iyklVYTjoULMeNm5qHiz4iyeBRa4EXeA6kQqc0KpPBH4zpaLi0GEP9uV4K2gQwcELKA5GQNDt_bT4XgrjeLPkFlzvUaZr0VnhTk5RXMPKm2D_7ml8fSVJHMx5HxLa7E8XgK_2GwZv14IZXr4i7GXb24LXBhIrpN5oDdJ4ayghPlzEqpHdsLtcZrrbHLV7rvMXltKvGMIREfUI21eb2KrpDvpHRFfLZ-c-ENUX62l38eTquVAFXxRA9NaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=CyZ_upZvgr7Ic0XIoNYG35VwqgZB_eWdFf9ibGeXo0SEOvneU0-TuFh7e-Xk1uCO6KOfU8GWUg6BEgD3iZKqDzBaTD-3_iyklVYTjoULMeNm5qHiz4iyeBRa4EXeA6kQqc0KpPBH4zpaLi0GEP9uV4K2gQwcELKA5GQNDt_bT4XgrjeLPkFlzvUaZr0VnhTk5RXMPKm2D_7ml8fSVJHMx5HxLa7E8XgK_2GwZv14IZXr4i7GXb24LXBhIrpN5oDdJ4ayghPlzEqpHdsLtcZrrbHLV7rvMXltKvGMIREfUI21eb2KrpDvpHRFfLZ-c-ENUX62l38eTquVAFXxRA9NaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOx4fSJ0kIcRlw0mGnFTfCxqAd-NKzJk3Gx14B69ogrPC3vN33Yu6xdx4ALPSw6bcEmH8A1h7WqUMRvnVw2HvqhH7PDhoeG1wptMcOhLuYVZpISnXYFAbjJLOmnaajozghBO-QZZo_dQvUOv1ASA-EJvJhxrOekz5tZ5J4DdTPPOEocswJKkFEZjxfv6S4HyAayQ2wzH3G68zA-SbqlUJhaWyWMUUEloKs_vM10hYl9Bq4ik-qRYxp_eqvwvPy5utif16JI516eXCyj1C9l-u50c0w3CoKcZfc5M7XwZnYWh_NOGpeCoqkfjnKPMMz-NFHjbLTS5BK-jpvoXu851Sg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnsBSxxsiY8uBGILk-KXd6Rn4NT0Tp8yzXgo6RYb9pUnWL-7lpXLRIEsWsjI1kMcXUIK4JFcckK8HpPZPsaLL_KQ0LOpA7SPa_vRrg1IvctxTjxe0M6j4i2ceUt2z4rNAm6_G1IUoVhuPFZe_Wvsy-4fYWXxUo-8mAKUijXS5Q5AJelmIrhwPd90b1KYcRF1xTK78sJsF8fKJyZgvC9DWlLkqmO27l2bato4c_0ckQJ96HGLYzfNXW09fSrr0LnuNpzYKMefUEiWcp1M6VxN_KK82CwAzB6aCBResjsp5sOK1KVKw8vrSAi2YMMboi1RZH_fmVRoyDheFFkRroxrtv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnsBSxxsiY8uBGILk-KXd6Rn4NT0Tp8yzXgo6RYb9pUnWL-7lpXLRIEsWsjI1kMcXUIK4JFcckK8HpPZPsaLL_KQ0LOpA7SPa_vRrg1IvctxTjxe0M6j4i2ceUt2z4rNAm6_G1IUoVhuPFZe_Wvsy-4fYWXxUo-8mAKUijXS5Q5AJelmIrhwPd90b1KYcRF1xTK78sJsF8fKJyZgvC9DWlLkqmO27l2bato4c_0ckQJ96HGLYzfNXW09fSrr0LnuNpzYKMefUEiWcp1M6VxN_KK82CwAzB6aCBResjsp5sOK1KVKw8vrSAi2YMMboi1RZH_fmVRoyDheFFkRroxrtv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=gjkISf-xTP0oSF6T4Zm0nkLoBnJQFpPF-NTqo5rMPS3qcnoz4IIfQa4Uo5GHiYVJrJt8e8szbmeU94GoqLpZA0pQjVvNJ4fPTxraIfyL9ISEpwHIf7KjKuoA3hX8EsEWYMEdonZJmQnz0X1sYYKtuwdErGDoVZp_GU4NKXIg83sBRlQ2rEJKysSPay3Apho6dB3SlYuJG60_09maQ51TjMIALZyVHvf-nYOz5AfSP2jiKAK4_aEFvcYKJVlOFDsZKBGr3WoWzyUQiQZg17CniVfVbepPixUI3nhCAUo5vLCQJPzkJs9T45Gmr3MyccpO1kd67Xsdm8AjKJli_1VS4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=gjkISf-xTP0oSF6T4Zm0nkLoBnJQFpPF-NTqo5rMPS3qcnoz4IIfQa4Uo5GHiYVJrJt8e8szbmeU94GoqLpZA0pQjVvNJ4fPTxraIfyL9ISEpwHIf7KjKuoA3hX8EsEWYMEdonZJmQnz0X1sYYKtuwdErGDoVZp_GU4NKXIg83sBRlQ2rEJKysSPay3Apho6dB3SlYuJG60_09maQ51TjMIALZyVHvf-nYOz5AfSP2jiKAK4_aEFvcYKJVlOFDsZKBGr3WoWzyUQiQZg17CniVfVbepPixUI3nhCAUo5vLCQJPzkJs9T45Gmr3MyccpO1kd67Xsdm8AjKJli_1VS4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=CeAn13g80Om7r30Y7EawR_bcnN6bXsaD7svn5wln5JO3JzqMDJL3P015IXWR9nMVaZIZiPFFME222JDolqelzOZ_y65ze87q9rv6d1y7Es_u0fQ545HvENLpgadosGvSU7RXxkaGSG5iA5Ew1yY2aZAonHbFj2vQLCog6tTTtX5TCh_505CiZtwllaJHsU-xsp7SX9YdFlnPUTkmuyxdbP1ppwCoDh7RrvN55VphHABobuox3IWUpVaJKqQsZSJkixBVHsdsUOVmkf-HF8aROe3OfinWmeLNle9IT1Ye3N7oYDiEfW1z_h050olCpSdedxEafNzm1g_pzs5OXLH5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=CeAn13g80Om7r30Y7EawR_bcnN6bXsaD7svn5wln5JO3JzqMDJL3P015IXWR9nMVaZIZiPFFME222JDolqelzOZ_y65ze87q9rv6d1y7Es_u0fQ545HvENLpgadosGvSU7RXxkaGSG5iA5Ew1yY2aZAonHbFj2vQLCog6tTTtX5TCh_505CiZtwllaJHsU-xsp7SX9YdFlnPUTkmuyxdbP1ppwCoDh7RrvN55VphHABobuox3IWUpVaJKqQsZSJkixBVHsdsUOVmkf-HF8aROe3OfinWmeLNle9IT1Ye3N7oYDiEfW1z_h050olCpSdedxEafNzm1g_pzs5OXLH5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=YFAwgzPqeY1-BGD2ycQbU5uMTFOuWnTnzHq8MJ0egbGPEIutZ-vVk1Y5HAUxRXkP_MQP09shOUUVCuzf74DCFsWT8K0ZcMZ2rdsyqgz-y59aqFbXSPK0xUlJSWdbMLOyizXf-aVt4NGxYCIPynwnPabuv_IZpkGxUADn4AG7oa8gZ4Msg80UB7D7OqRFvHGCsMpJIM1tbYVRhaACGuG-I_Tjskd02AjJ6GxGrr93KEvD62xqTCtP5WiPfYSGUzmh7rQ7LEtaaPpbBtxiiWM-43KMXIRob1aCDDgvL0pvenF9d1Js3Sp8Z0gCJdQTkAmJMQ5u--Lp6rgKOF_OdiEt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=YFAwgzPqeY1-BGD2ycQbU5uMTFOuWnTnzHq8MJ0egbGPEIutZ-vVk1Y5HAUxRXkP_MQP09shOUUVCuzf74DCFsWT8K0ZcMZ2rdsyqgz-y59aqFbXSPK0xUlJSWdbMLOyizXf-aVt4NGxYCIPynwnPabuv_IZpkGxUADn4AG7oa8gZ4Msg80UB7D7OqRFvHGCsMpJIM1tbYVRhaACGuG-I_Tjskd02AjJ6GxGrr93KEvD62xqTCtP5WiPfYSGUzmh7rQ7LEtaaPpbBtxiiWM-43KMXIRob1aCDDgvL0pvenF9d1Js3Sp8Z0gCJdQTkAmJMQ5u--Lp6rgKOF_OdiEt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgO-N6jF3oGKW-Zrusfjo6g8jr-E8p9YbQ54Y8Ix7YeHfvkMHmtvNV0qI3x9M27knYmUKb4-cfwgwH3WZTZMYIiy-yk0TB0hMWwoF5QcUs0NIe64zAmi_LgRlypkRNyy20NsmGGR0nJ74yOT9ReHUc77n8DSKNX1jJiwLAQLbzY-glLLK8zA5yMQpCpWDTEv5nyCYZpZbtLJkjH9zD49zhXtozvws-jg4Mu3O3bD6L_CSu1-J3jfwoASjljs_C2wvOIjiXcX5eCoxe5v5RNdWQP2aeCdZUBY0QeA2STuYsVXgJcBhoVq0-58s4g8KO4q0fctnKwuT6eIKiRZzgynBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
