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
<img src="https://cdn4.telesco.pe/file/HtnMrrJ1lQeqaBJfVORtEqAYD1FzMl5-eR46MYMvY2NoziFLXbZyteJ5aV3F6m7RWX99xkXjAlMzccdjhd3sOiNZmaSezJDjku012F-lBnqk216XSOWqECb-N8-6Fla_3b0ybkf1TksxBx_PzePtgo08ACORPe3bn-VRZ_99DqvuxbSRUUvrVM6bztzx-pev0a9VBcaSuIYYqbCIUHzrNeRpRfoHhnuxPwz4tuOhR11v1dMHOOSsvEtIfY61rcHxzjcLbMYhNH15tO0MaMjgoHDn74zhdts16ihTwN4W6G2TqZ4EpQ8MGocn-dKt1-hQjsVH65wLeCGQsnTbH6yUcQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.19M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 03:25:16</div>
<hr>

<div class="tg-post" id="msg-664809">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e56e13416.mp4?token=DpBWMFqW3M_tWo76YhVUf-zw3VeojH64YAaxQrwfZdcyutcCa3Z3mL5Y4NuI6NqKd7Fg-kU6xsBt16CxLg25d4WZPpkmQBkwhaJYf1W_C8vfinOtUV0t6jTtriMRNkz7DMtVTn-GTfImOF1lr9UFc45mwFk1GQWwKQWwUErv12m4qlCd_7lBCmAbuNS_oZp2ExMnFwP37HuZGK0nyW_JmufwgqkfJGgSbQjet8zYhUPcpQdZGqBWdrkqlew95agqLyXdWDsD06YcvpxXCs1738zFIpiKX2DedmqVDrWoY0ShjR_IEX5vBBAKvgyr7ZIP8mZiYzD8qoJSWNA3f9W9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e56e13416.mp4?token=DpBWMFqW3M_tWo76YhVUf-zw3VeojH64YAaxQrwfZdcyutcCa3Z3mL5Y4NuI6NqKd7Fg-kU6xsBt16CxLg25d4WZPpkmQBkwhaJYf1W_C8vfinOtUV0t6jTtriMRNkz7DMtVTn-GTfImOF1lr9UFc45mwFk1GQWwKQWwUErv12m4qlCd_7lBCmAbuNS_oZp2ExMnFwP37HuZGK0nyW_JmufwgqkfJGgSbQjet8zYhUPcpQdZGqBWdrkqlew95agqLyXdWDsD06YcvpxXCs1738zFIpiKX2DedmqVDrWoY0ShjR_IEX5vBBAKvgyr7ZIP8mZiYzD8qoJSWNA3f9W9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروهای زرهی رژيم صهیونیستی به اردوگاه عسکر الجدید در شرق نابلس یورش بردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/664809" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شهادت دو پاسدار در درگیری مسلحانه با گروهک های تروریستی در پاوه
🔹
به گزارش منابع محلی، شامگاه امروز یک درگیری بین نیروهای امنیتی و عناصر تروریستی تجزیه طلب در شهرستان مرزی پاوه در استان کردستان رخ داد
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/664808" target="_blank">📅 01:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91cbf495a8.mp4?token=Qla8ABc6DRflUc4AjYkSg1SRp1FSBvxkIMqs4IX4Ua_BVyW2f3PH6nZjJpd7Wb6q43P-uwDBhJMeo3EkhY9lbUtOj-aSiIsV9GxS0AeS6pZaKixtOXXMGP-xYurb4hlsQswVhokXzSXyoBEampI3Pk7pgGmiVADNgGuox2jTrkUxQG67HNUedjY7F3tvWdKIV_Gnx15u-G9AGupRzJUHN3GAfbXXoaGwfcmYWQBM4X-1R1tX7_BNFOnDtnnxmthy39O8DEaoz00JsmdA-ofgDtf8p3FNTvac4sF72vqNIn7KR6jpO0VVHX0FNaTBzVDITNaEeqXghS66VatDCpDtMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91cbf495a8.mp4?token=Qla8ABc6DRflUc4AjYkSg1SRp1FSBvxkIMqs4IX4Ua_BVyW2f3PH6nZjJpd7Wb6q43P-uwDBhJMeo3EkhY9lbUtOj-aSiIsV9GxS0AeS6pZaKixtOXXMGP-xYurb4hlsQswVhokXzSXyoBEampI3Pk7pgGmiVADNgGuox2jTrkUxQG67HNUedjY7F3tvWdKIV_Gnx15u-G9AGupRzJUHN3GAfbXXoaGwfcmYWQBM4X-1R1tX7_BNFOnDtnnxmthy39O8DEaoz00JsmdA-ofgDtf8p3FNTvac4sF72vqNIn7KR6jpO0VVHX0FNaTBzVDITNaEeqXghS66VatDCpDtMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین روش برای برش میوه های مختلف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/664807" target="_blank">📅 01:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664806">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c4b3af88.mp4?token=mYUuRZpGT7doAUh0CYCa1SS8PAL34x_H99SGz1GV8Gx1nKIPYFfGXh5YZh0u_MLeg4IZmSnvyq_gNmxZRJnB2drJnXhtdPlx_33g1VZcp1VndXNfbhoLeA3NbR5KMBrfMjMiJZSngq_7L5pXjZZjVbsECOkoAw8upFQTDL1p0NYCIE2kXmbfMsn9s4zdN62orjnzFfgdsaib0NhVCNWv4zsUZPTmSUXLLt1udwR7M5sXkjnbrRoHCZoFBQS4fLl54KOHpOGDEf_xvF6QDR8L1ubWamlCHAxx3HEqiLEa0BnzvDmZi9BOiip4BO_DzWF_ItPyZh2McNVWuMAZjZmBnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c4b3af88.mp4?token=mYUuRZpGT7doAUh0CYCa1SS8PAL34x_H99SGz1GV8Gx1nKIPYFfGXh5YZh0u_MLeg4IZmSnvyq_gNmxZRJnB2drJnXhtdPlx_33g1VZcp1VndXNfbhoLeA3NbR5KMBrfMjMiJZSngq_7L5pXjZZjVbsECOkoAw8upFQTDL1p0NYCIE2kXmbfMsn9s4zdN62orjnzFfgdsaib0NhVCNWv4zsUZPTmSUXLLt1udwR7M5sXkjnbrRoHCZoFBQS4fLl54KOHpOGDEf_xvF6QDR8L1ubWamlCHAxx3HEqiLEa0BnzvDmZi9BOiip4BO_DzWF_ItPyZh2McNVWuMAZjZmBnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از آماده سازی محل وداع با پیکر مطهر رهبر شهید انقلاب در مصلی تهران #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/664806" target="_blank">📅 01:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664805">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حمایت چارچوب هماهنگی از اقدام دولت الزیدی در مبارزه با فساد
🔹
«چارچوب هماهنگی» بزرگترین فراکسیون شیعیان در پارلمان عراق ضمن اعلام حمایت از اقدامات دولت برای مبارزه با فساد، آن را گامی ضروری برای بازگشت اعتماد به روند سیاسی کشور دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/664805" target="_blank">📅 01:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664804">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
انفجار یک بستۀ پستی در موناکو
🔹
در پی انفجار یک بسته در مقابل ساختمانی در موناکو، سه نفر مصدوم شدند. به گفتۀ منابع خبری، مصدومان تبعۀ اوکراین هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/664804" target="_blank">📅 01:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664803">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
چین: اسرائیل باید به آتش بس در غزه پایبند باشد
نماینده چین در شورای امنیت:
🔹
آتش‌بس در غزه هنوز اجرایی نشده و کودکان هر روز در غزه کشته می‌شوند.
🔹
اسرائیل باید فوراً در غزه آتش‌بس برقرار کرده و به قوانین بین‌المللی پایبند باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/664803" target="_blank">📅 01:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664802">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439f50420e.mp4?token=jTOxc-bR06mCZ8r6P_c3JH0l3NMqHqs24Hxd6n104_VQpCI08shBnj5AbWSZOhE8lNGqun8604amaD1LytY8v1zlAXrf32Hu-77nEipU0PJVXt1DRK-z2GChyOX2PEuq1b4VDblGxAP9XnivanVgUt3hnr8UG1LNVbX5e3-uwpuxDWZiyGnp21tPdqBBD_JHy9bsYXM1lZXVxgRDVxSsXvcEReqlDp_RW02dAkCDi9u1ftRxlyHMmATcw770rpGle9nKPaha8ADTZbaEIPsT9-1p5qibfv5Sijl0IcX5C3MIXdZaHcgVaZcgsApBvSbFFz5GIZ1GNE1_ywp5cWsMWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439f50420e.mp4?token=jTOxc-bR06mCZ8r6P_c3JH0l3NMqHqs24Hxd6n104_VQpCI08shBnj5AbWSZOhE8lNGqun8604amaD1LytY8v1zlAXrf32Hu-77nEipU0PJVXt1DRK-z2GChyOX2PEuq1b4VDblGxAP9XnivanVgUt3hnr8UG1LNVbX5e3-uwpuxDWZiyGnp21tPdqBBD_JHy9bsYXM1lZXVxgRDVxSsXvcEReqlDp_RW02dAkCDi9u1ftRxlyHMmATcw770rpGle9nKPaha8ADTZbaEIPsT9-1p5qibfv5Sijl0IcX5C3MIXdZaHcgVaZcgsApBvSbFFz5GIZ1GNE1_ywp5cWsMWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت به کره در حضور انبوهی از معترضان
🔹
هواداران با کوبیدن طبل‌ها، شعار «هونگ میونگ بو اخراج شود!» سر دادند و به سرمربی سابق توهین و ناسزا گفتن #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664802" target="_blank">📅 00:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664801">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
حدادعادل: رهبر انقلاب دائم مردم را به حفظ وحدت دعوت می‌کنند؛ از «علی‌الاصول» برداشت غلط نکنیم
🔹
بیانیهٔ رهبر انقلاب باید همه‌جانبه خوانده و تفسیر شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/664801" target="_blank">📅 00:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664800">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750487189c.mp4?token=hgkwPdXL8KkPMJ_vDFmDrPCZH6vqgy7GxYKmMNqO4NPL1REKHSBvov2Vu2-aFI0yVyqujGy8gcEEUDQU4VGqnf4GRZWEpctKewOevFBpT5xxuO9nIbrecKQN5xRCN4dyhgSxtRfsYbrVAPXrUhPIy9oinxuqN1nnb-X60hanZeVTeLjd7rmPEbIrXplUqXc3PLBlPK3aXfqDZoO5bHlC8nmvfP0pKv-1w7Eo56QdvecQe33b0q06vloGBHJwhAX_YN4ilQ9z060gjn3n4lorLqmIUCVlzXzlKO_WSPJolWKf79YpOOaPBmvQQd7Pf8e4ejAp2zmkdxpzgAosYGOfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750487189c.mp4?token=hgkwPdXL8KkPMJ_vDFmDrPCZH6vqgy7GxYKmMNqO4NPL1REKHSBvov2Vu2-aFI0yVyqujGy8gcEEUDQU4VGqnf4GRZWEpctKewOevFBpT5xxuO9nIbrecKQN5xRCN4dyhgSxtRfsYbrVAPXrUhPIy9oinxuqN1nnb-X60hanZeVTeLjd7rmPEbIrXplUqXc3PLBlPK3aXfqDZoO5bHlC8nmvfP0pKv-1w7Eo56QdvecQe33b0q06vloGBHJwhAX_YN4ilQ9z060gjn3n4lorLqmIUCVlzXzlKO_WSPJolWKf79YpOOaPBmvQQd7Pf8e4ejAp2zmkdxpzgAosYGOfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پاراگوئه به آلمان توسط انسیسو در دقیقه ۴۲
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664800" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChtFv6y6aE3XnoaSxxabdEb1ReKOuAv1wzVdwK99k_99-_84GxgYxlAghcyVjyEyMti87HV7KImauEnfdPURSF3dzgABL66YPdfr6nZw_RLEqhtw_ieVaLUOP5CrHEHmEJJ9HRO09RHKlUEDU1sII6E1LzG0xc8tRKrV6e6yBgAaQQg5RUgtQ-n-z1yuP9q6w4RTcIV97uFGafGTkyNNTWSNLmncFtYcgNWAt2jki_SqBVJr6CYK92OGMaE4XJ428KNNIQf8cYO44yy_uB5GcICSfW2DTuY-dkpuuJOP-CpTnrk9GYofEsyOzc3VaDo4iCXKEBcQIf5-tdSqlv7e9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVpcgOZKKyOIN7yMYWgLEkq5mOI9QSgjRavhpcmbYmLnyA4XyqveMT06aKrxb8GUptBaKgsMKipD6k_TZ3-e423chon4AN-8NOTRiVLwhLnR2xQulIUXsnS_BM2MTxJIDBntwk86IeOwU7f3y6firdXSH-979CN3wDT8JbekIMdWkeiqR3WpY2l6TdkggLiwW42LYqLVw8iwbCVKQPBjQ6xsQsa_m_ICHgAja63UrgUnW1Mong6D9zwJbC5lAdcHe_WGV7vS-D7UukjIk1uP2_NBsyQzD8InIaBqDOTvOsw6R4qijgq2W5yBB4lggB7qOtr426N7ggzp8N-0Adio3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3HSODwJ2yGO0bGPMhmIBDpOAOrfztlMTBYED7-bZ61pDycoK7Kx_opfe562Kx4BN0-vKs4Or5zdueSbZS4pCnGCVrIsa4VzF5pxs8E63VZjn42qOnYLt0fyTGEtC2DqC7mgYt3WyGxTAwZGjKmkWu3gYpxiksNpQE0b65JTm9IzQxbGxTGhz3GYlyHkkW-TfsbGNPlafiRCygHycyZkYPtBFO4g9Shm9hLYQZw6tNfJ-A8IY5s7By-RfbcpZnD5u979Gh6JSu4PNVaE8FUf4CllIQSG1V0YrVGlohxMRNNcLshWnoDue5Qs4eKUc2g_PNW9Jo8_hHz8pVPJec57sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر زیبا از ماه کامل در آسمان امشب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/664797" target="_blank">📅 00:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTZEt_Qi6aQjeanTmt9ZWPbkV2KLot_hOMn61o-799rRzbXE8rWBKOO9YSbWHgXGTzmpUooqPnLp_LxzVU8T-TG8DFHGkbwS_SSkJe1b6sgq7-qkmREIMQMd8p4s5Lkw-epHIeS0vjNtmmwbccE8CKG_H32qtREv1WDvKWnjzgoSLVAirLaP4v7u3dBjABAmzSWG7Yb0rYOMeMNqTOVpudjTabi0YpKsXUAdkko_Wqu43efvK_5Kke6FAhDs82sELpu5wfGjLJVI2tgd9RPq4gdjoszW9HXdyU13bp76a9HkDbmkUS3OSrmMf-vHo79dlz0Da3r1cjD0vr4urQSb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت رهبر انقلاب، نه یک اتفاق سیاسی، بلکه فصلی از حماسه جاودانه کربلا در حافظه جمعی شیعه و در امتداد آن است. مسئولین نظام جمهوری اسلامی باید بدانند خونخواهی قائد شهید، در واقع  خونخواهی سالار شهیدان کربلا است
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/664796" target="_blank">📅 00:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28149bc86.mp4?token=S_0RJjd4yp6z9JVndvOkMeUHgFvLqusYONgf-fAQ1DsQJKWoCdNiodKyVimmo3LVV_C-U9YW1jrzF8xTMrA9GVYr5iLT__XZD6dTt-RQj1QGNkTnBmhYJcso2YW5U6I-fVSNJXvDV6PTq7T5rCB84M20JgtQcDQVD1v_7caPoI3mOfeQH2VOqApNMOdmuJfSuK6npIGRayGaimahMSIB4XZIDXMa6iez76xgn_TdXPJHv7VtZLBmMzXm3F4Z4oKyireUbSKamapgDlnLreSgVqg6R9CPkzbIf73WpK1ERXZRWsHfFh7O2LQTuMNMwC0wmXaOxskK3vYIdgkRV-0wFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28149bc86.mp4?token=S_0RJjd4yp6z9JVndvOkMeUHgFvLqusYONgf-fAQ1DsQJKWoCdNiodKyVimmo3LVV_C-U9YW1jrzF8xTMrA9GVYr5iLT__XZD6dTt-RQj1QGNkTnBmhYJcso2YW5U6I-fVSNJXvDV6PTq7T5rCB84M20JgtQcDQVD1v_7caPoI3mOfeQH2VOqApNMOdmuJfSuK6npIGRayGaimahMSIB4XZIDXMa6iez76xgn_TdXPJHv7VtZLBmMzXm3F4Z4oKyireUbSKamapgDlnLreSgVqg6R9CPkzbIf73WpK1ERXZRWsHfFh7O2LQTuMNMwC0wmXaOxskK3vYIdgkRV-0wFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌صحنه داستان اسباب‌بازی ۲؛ شاهکاری که نزدیک بود هرگز ساخته نشود!
🔹
در جریان تولید، بخش بزرگی از فایل‌های فیلم به‌اشتباه حذف شد، اما یک نسخه پشتیبان که روی کامپیوتر یکی از اعضای پیکسار بود، این شاهکار رو نجات داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/664795" target="_blank">📅 00:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d58b8227.mp4?token=c4hYzOYY3JAcd5Gx97P0MfYwgmHq6clBoGt88KODYA71vV7Ku_0d0Z6rAhvkjMSE1dziZmZLdUjOmwaCTLuhyLvzXWElEgOEACJc1rZbrc1QoHJZd2BxFr9YNvYjnWz8RWd_ekwSheUPfhVJA2h8UJheRX2TK-aTTQJU3eCFCFTNIn_g162NXwAraKQr7p4_Z8xwAeWEKQHQ2ZMGdv-KGclOgyoS8uHxq0j6srtTZSRbRM3ns7DNPClMEEYnwEOxNgHeSemEC6goZuDA-SCwbvEgOkcebE85OWxZcF8e7saRdG4gET_s-M-7i7QqcAG3_GuAH9bLJjhHhBGBlqIrSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d58b8227.mp4?token=c4hYzOYY3JAcd5Gx97P0MfYwgmHq6clBoGt88KODYA71vV7Ku_0d0Z6rAhvkjMSE1dziZmZLdUjOmwaCTLuhyLvzXWElEgOEACJc1rZbrc1QoHJZd2BxFr9YNvYjnWz8RWd_ekwSheUPfhVJA2h8UJheRX2TK-aTTQJU3eCFCFTNIn_g162NXwAraKQr7p4_Z8xwAeWEKQHQ2ZMGdv-KGclOgyoS8uHxq0j6srtTZSRbRM3ns7DNPClMEEYnwEOxNgHeSemEC6goZuDA-SCwbvEgOkcebE85OWxZcF8e7saRdG4gET_s-M-7i7QqcAG3_GuAH9bLJjhHhBGBlqIrSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کناره‌گیری سرمربی کره جنوبی پس از حذف از جام جهانی؛ تلویزیون ملی تصویر او را تار کرد
🔹
کره جنوبی بعد حذف، سرمربی‌اش رفت و تصویرش محو شد؛ بدون توهم توطئه، بدون تهمت تبانی. فقط پذیرش واقعیت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/664794" target="_blank">📅 00:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664793">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYeMZn2r6VRIV5cplZHb_o7LeNm6Tz5cLryrmPmrDbvaxmZv4K7FULJyGot9S3jIxQoaUAzxzgtGhYjpIU1xpUVTFoGqCVJhnGFcXJe1cgc92eNWJ4lOywubsiseScYsrT8glmMX2dMwldHkHf000sXO1QgYPQeCO5v38kLXLLCiT3DggRAluocBJdZoAcSc8jx53KlM3p7YrVoPMm1Z-2agPBfQQ5-qbWn40L2q28uetXb2lpBbyeAXPNKoKphINPgoVR0b8ubKpvx_MxOmhBFS4wekjjtXEjwH-MjSHoHwbXHwTQSn7UsI_TMzftrahQ-jGCZEDSvQt5Q2TfB_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_پنجم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید بزرگوار مهدیس نظری  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/664793" target="_blank">📅 00:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664792">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5214eca511.mp4?token=iy6PVcTBo5klERhGpKvkAwj28qLAoECe0XJI6F63ulgVOgpxJmolJdPLX3JHzoqnS6P1EJWR-tsyNHqgsJs-toDOu50jXqptGmlCi59nTwmcwkqUsjhkvn48Fa_s7OHPBr9CfuuFNDha1SlRpcl__IfAB6PumPlDb5CugHzOUCWM6zlyRUorOaHtkTYIEq--M7uXOMAvRnERdrwcxOD0QefJHJEN56XFqo2XV21CgM6SP9gpAfPGPFSrpj8fMbQlfsedVmcikZPQkyvS5ytE7A0v6NqK5gmzUCxEOcGw_6HwQkPwvzkBd7G54YkFBnAMdeI2pYmx-pSKKRobFdsTag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5214eca511.mp4?token=iy6PVcTBo5klERhGpKvkAwj28qLAoECe0XJI6F63ulgVOgpxJmolJdPLX3JHzoqnS6P1EJWR-tsyNHqgsJs-toDOu50jXqptGmlCi59nTwmcwkqUsjhkvn48Fa_s7OHPBr9CfuuFNDha1SlRpcl__IfAB6PumPlDb5CugHzOUCWM6zlyRUorOaHtkTYIEq--M7uXOMAvRnERdrwcxOD0QefJHJEN56XFqo2XV21CgM6SP9gpAfPGPFSrpj8fMbQlfsedVmcikZPQkyvS5ytE7A0v6NqK5gmzUCxEOcGw_6HwQkPwvzkBd7G54YkFBnAMdeI2pYmx-pSKKRobFdsTag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس کودکان به شهادت رسیده لبنانی در حملات اسرائیل به لبنان در دستان کودکان در عزاداری محرم در شهر دیر بورن ایالت میشیگان آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/664792" target="_blank">📅 00:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664784">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnlNHMMsk7G2CO6L3diTiiX_Yu8iad7t-0GTYaJoPF72ZKKTGc69ohQPAK9zW5jN_JnmIDVmtOEJu6BXpD8Q0y1-knhfVaaKTDCz_GzHaPbViQ5t1DjKfNwQS1vNyB5zNz1ZByfqGj2eyYLFtfHwHXbqNrPHdSRAj1FSut94J_X64tEo3KwJNIYr-ouaat2XVP-PNk1hZ24XK8z4EPcMJTCVhBTCZcEOn2ombM1EtLQ30nRvxCJgLBcUTaWwSYR0wByT_cIhKbWPgAHABxogvMQFv87OaOTwIipUQXKiG80vJ3Y4nTJxE0AgRqp_MPR7e8OUUNwRzpNKZjr7pM7SnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-UYWlvj8yPgfIYp6DoMr5LoetSApTYcLYzb0fPodRz6uNLDstZ6_v8XcvsFiD3tVvr9LmcepSHWn3UyKNHQ_rC74R4oE3G2wqeUruvlbAUyo1yocWSJXG3bRFsmLwqr9_XCbEPxAK53KyVmFjKnwuhes5AqdeEO2qSA8TTOPEYfeFHNwYVsizCMN3E6qj9z1Y8i8dq6mfhd5KwBtLT95Kzr8aBpCboOaOpwM0WokoecNdUKK7MMQQ9aEWXwMED5qMl4NhxH3nhdCgNrk-zYFhhlvnsRwPMCpn1yUPQzyyFVpEA1wXpA7NFh2KeuRwvy9kOFMUOoZJKuDnPxbBvKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNBcJjMzTwBpkgtqLAREyCmDqqhJYV-1yLUfF9x8hCLQVVz7MRBckMFE6mgNFepNXMaLeP1E_XDT2Fzc__DrO1UHvScpcSM8do6ftGEKdTJF9ojHNPezgezUD2dNtbnvK5BpF0OxkjkBaIqD2Tx2hEWgfPwoOuBi4Aso6shJkhaA43OtgfiW4vpPQRC_dS9VCon49NlE2e6mw8Qz_KVKdMbkqNJ3774PuMKt4iTJ6uIxEeLjiEXka25Crh06KZ9DGXPx9fYJGY4XPEvnNWVa08PoT08bX6LLC_erw8G9O2vQD39nQZ0kW-WDMvYUMmBgY3FxE1NOlEIvAm7K67Xfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diTeBKWe70pfr4hsLJ05PBjdJfqamlzrJQD35fyq09Zpj-Y07f3Ndjum0uxuoszYr4Lpvcrn-7CrmxxD1Wn1RROdSvaM_3ku1BMjAirGTCOXtILvCpIwWx7SKhFVIRIfMms6DW39roHpr1l8l-En35uqzAw6C7iFlSbGB2p3RGN6buBoQ90T_oZK368C3LYhh3pJlA8ifU0HCtlq89P7TasVcxk96QGwGX11FCTN8uVM3dEv9tuVD2Nt2Te19aYSZH75HhlAIebbCc-Qza1Yv684SiSzUMfat-Wt8payOTyrZXtuDNuBWSijZ1XLhabUqdzeHT14GXjH4bwxpO6Fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2e6wNltHelZIJQ5-k6ZauvgwIons2Qom4RwmH50325TWkNrvK2IqGx6iS6_-E4SRJfUc6qxEkyiZJEawgHiWhMLrrF5L-EfQCaCB4Bb9TH0w4tRsXZ5ZmxWrltT9UOnUBPKM22uC2EQNNIonmjkLY9-ZKS6ayldKwaJ4IJ05h85cz41YT1gWtp1_1E9GR9FA1x9m93rTCEB4jRLu81XXOA-UhV4MluNdKHq_0wbVarwDK1vmosDpXHxa9EPstf4aMvQdjf3KCd_An2IRCMuOBskxh8TtY-WQydA9GMa0ZaFgA4j6y090oIbyXdyNhMG7YBcgPj7LVXittTzt12f4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUqGnmDAi_wRJLetNQsDluCXgZfspLVZUXBoI11E3-lMPr8XCNOkfdXKk_Q7yDFKoJcxRLZ3EcjUtd1Ye5P65Wb66EI7Pv--4rH1Zmj-_KYZAaYyjaxYTzsmPuAWmdxatnWDAEh5wIAlz4KevMMLB-kFhcGZGlIBMsEHVALDnI_iS_FRy387LPy3fJFlEK6tTERKEHWzso-gBWEXodmGomKvN3k4WQYEbhZscWCUnKEhYweLqVQdqBBxzW4q-DMgToqOUFl62qovEbNrMJggX4Re8P2jQU0GdtIFG8U23F1TELYonT943m0wz9-7PsaYTj6uLlRA5BaWQ52HZSMOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCUhamKJDdoReQbe5h8AEOrfOgxnwq-RyhPK2OwFB7semQa6phHbVbC3cofB_61d8Zwtv5Wr9qxDAh09WugKxx7r1Ela4XRQUJHbeBjcoCtmCTDPmqV97RrOvWh8ag4s_W42iRc1fHBJbGVDqAW8B4ES8dNMWRvJn9tIMCrelDrd8n4FLti00dpnYEsMqhXH7HExjICqAZmQ8O5mm_LSQo9OzQ1-Uvswf7spOJ-_gMTGxJSOyJvowp2ZYQxx1ls1nwrImQiaXhTNjzh4BXKWVSRXIO3LBRPNUDQcxiAThYPJmYWHQS30lHrxL7O_ZfDSMRTVD72qJG1i-Qt8kjem7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDZijZMdKKE0w2s3piPTnel9QneNCwwhAPyAWiUU_igY7Nd8w1AIGarhF1vCOch2Zg_cPalkMaUzpXiCCmNYrllQTUrEsa4EwWoJDoadX-BcAxMa0bTDOP5WmTElrVKfIgMq67PUdgbej8t0MX1NfJ7BDziCQWRVjRMxC-AcvAPlYPHdMcjZ6cAXvK-peUiyARKa8_HNB9hmOLmZ2zUtqMFrwKjDDiyZVlHLa_3kqRZ4QqeEJDg_HiZCsbqycuJGzgPKPBJdXs4_sUPLvQrdHpj73ObdTqrZQGvPObNPgxJlXRI3M6gWq4LxAgoC58EBSY_lobC3oGgpXbqHYMHozg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدام مواد مخدر سریع‌تر اعتیاد ایجاد می‌کند؟
🔹
سرعت وابستگی به انواع مواد مخدر به عواملی مثل ژنتیک، سن، سلامت‌روان، دوز مصرف، روش مصرف و دفعات مصرف بستگی دارد.
🔹
اما از نظر علمی، بازهم مشخص است که برخی مواد افیونی با چندبار مصرف اعتیاد ایجاد می‌کند. در این اسلایدها ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/664784" target="_blank">📅 00:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664783">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d4be0c04.mp4?token=jj0MvcVV-aNfmkSI37bDxVoyUooxo-mQ2oXc5Ap3Xwvvh80snQq6Td6c1qeP8NfaO2HuWvukcYtA5JMaAp2NvZ7qUTaLKeiWSqfLIgmbwTSB_J2um1TkEor-T0k-qIJX-rI-1JUeP3BaEaSrHoOGEmGe7em4ECIyh8urnW29ekTpHoea7ZdjgXrY9gd_yZM5OOH03sQpL_9EyZr0sLzZYgPzcxrdIxN9lHiGqWpbV8hQt_3BJOpcVnKW60ZcI-eiYVjrM3y4ux_UjeEA5LVKHT6jAmkSIis6qDTdlrx6rSfJjgBiGSgSXu6MlIz-veCc-EFa4djQpXN3XeNO_2Io_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d4be0c04.mp4?token=jj0MvcVV-aNfmkSI37bDxVoyUooxo-mQ2oXc5Ap3Xwvvh80snQq6Td6c1qeP8NfaO2HuWvukcYtA5JMaAp2NvZ7qUTaLKeiWSqfLIgmbwTSB_J2um1TkEor-T0k-qIJX-rI-1JUeP3BaEaSrHoOGEmGe7em4ECIyh8urnW29ekTpHoea7ZdjgXrY9gd_yZM5OOH03sQpL_9EyZr0sLzZYgPzcxrdIxN9lHiGqWpbV8hQt_3BJOpcVnKW60ZcI-eiYVjrM3y4ux_UjeEA5LVKHT6jAmkSIis6qDTdlrx6rSfJjgBiGSgSXu6MlIz-veCc-EFa4djQpXN3XeNO_2Io_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من با مسکن پول زیادی درآوردم؛ دموکرات‌ها لایحه حمایت مسکن را دوست دارند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/664783" target="_blank">📅 00:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664782">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
حدادعادل: رهبر انقلاب در پیامی که خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا داشتند و با بیان علی‌الاصول، نظر دیگری داشتم، دست مذاکره‌کننده ایرانی را پر می‌کند، ایشان تجربه برجام را پیش چشم دارند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/664782" target="_blank">📅 00:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664781">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
فساد بزرگ در وزارت نفت عراق؛ ضبط میلیون‌ها دلار اموال از یک مقام ارشد
شورای عالی قضایی عراق اعلام کرد:
🔹
در نتیجه تحقیقات اولیه از متهم بازداشت‌شده (معاون وزیر نفت در امور توزیع)، مبالغی شامل ۱۱ میلیون دلار پول نقد، ۴ میلیارد دینار عراقی و چندین فقره ملک کشف و ضبط شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/664781" target="_blank">📅 00:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664780">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYJGobtNO2v3oGfrrwUWyszuvDI8CtjBr9nq_qZsZ__D2XKXEFcrymAa0Gu4HBIaFO3EKHjyPq82KWjQSdNmDnssPDAVuh2auQL9FbmkOLnyU0ODOH8dFOvgTP_Qk1-xANiNoSZGSNjif3IUiACK9VxUPw1MifDr8f9Q9RE-TKU_D8uDeGjDZLl1R4kq7mZuTwnd3lT2oBt8l1BVyfiKisCWzcHYvjzEca6N0LfGR8ly5pyz3O_gwM_7ZtB5NZ4uTeaXIHotq5dR493FuhEy_Nle0njta7Sg2-qIURbUzus9eFzCXaBmMcpfSLTJKnjLWFSX5XE7XVaODnqAsbNRhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار حسن‌زاده: تا حدود یک و نیم کیلومتر از مرکزیت مصلی ورود خودرو ممنوع است #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/664780" target="_blank">📅 00:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664779">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
معاون وزیر خارجه: ما ایمنی و امنیت کشتی‌های عبوری از مسیرهای موازی در تنگهٔ هرمز را تضمین نمی‌کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/664779" target="_blank">📅 00:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664778">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbr79gEzP1j8JbF9RwttCXAHIf284KBPMKKwM_NafUswxTe3iXt4rVeds_2qfSvOAno_aT_rPbL51xLvbNgY5IHgm5SDBGpcBJHr0FhnxAT7-St7AqTcv41tivGJvabP1Rapbnsk0PMdG3WS2qVZHSjvbntFGTfAutSZbjxiBTQDrlFrUJk_glX42VPwsLuURv1quc_r3TJXevt3sOF7c5B0zEO8DVeRYY3LNFZ56diPC-dZbzfI5s0ZEoj6kcHfYi-fFBjVkrJ-TQLUk3VqtcCYf-oWA_KjTLDBa9rqyviWecygMwGFjIZNuzePjfj719sHY6JL_v1RbQLojHUQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/664778" target="_blank">📅 00:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664777">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFKgJwe4uQhCG5KBd058H-bT9yqkpgjlwj230BR-Jb4EXV_m4Ng3jpuTsLVwOaQAkS_5nrn9OLDcI7YBpJYAUp5B61-gvFs7xnQSfMImd8cXc_GtteN-yUtv4Cvd1tqZUnu73O2Od_QHoBs6EdIxtKPoq3fMrPD7cY2URmimxjM7uBnRmN6lwnrtYok9G0jsam39UgucOBB70gyzDOBMpU6fQ4BxvayuYZ-qsUK6YkrMh5Lwkz2BNeZ3s9hLCfFwf_1bs8pK-EgCHDQG0OYDgqRRO8rANuFxRVhgjyWqd_Ba2kjpl7zFrFkhf7KVMpAyJIjOyAHx4TEGhLQagvwS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: اگر طرف آمریکایی به تفاهم‌نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/664777" target="_blank">📅 23:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664776">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تشریح جزئیات برنامه‌های ارتش در مراسم بدرقه پیکر رهبر شهید انقلاب
سخنگوی ارتش:
🔹
ارتش با تاسیس ۴ زائرشهر در داخل و اطراف تهران به زائران و شرکت کنندگان در مراسم، خدمات اسکان، پذیرایی و بهداشتی درمانی ارایه می‌دهد.
🔹
یگان‌های بالگردی و گروه‌های امدادی هوانیروز ارتش در مسیرهای پرتردد، آماده ارائه خدمات به زائران هستند.
🔹
بیمارستان‌های شهری و سیار ارتش هم انواع خدمات درمانی را به نیازمندان ارائه خواهند داد.
🔹
با گسترش یگان‌های نیروی زمینی ارتش در مرزهای کشور، امنیت مرزهای زمینی تقویت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/664776" target="_blank">📅 23:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664775">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
غریب‌آبادی: راجع به پول‌های بلوکه شده فردا و پس فردا کارشناسان ما این مسئله را در دوحه پیگیری خواهند کرد
🔹
یادداشت تفاهم در برخی بخش‌ها دارد جلو می‌رود اما در خصوص لبنان شاهد نقض تعهدات هستیم. جنگ در لبنان  باید خاتمه پیدا کند و نیروهای صهیونیستی از این کشور خارج شوند.
🔹
کارگروهی را در ایران تشکیل دادیم که نظارت بر اجرای یادداشت تفاهم دارد و تمام نقض‌ها را مشاهده می‌کنیم.
🔹
اگر شرایط  لازم فراهم شود کارگروه‌ها مذاکرات را آغاز می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/664775" target="_blank">📅 23:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664774">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
روایت حداد عادل از نحوه زندگی فرزندان رهبر شهید انقلاب
🔹
فرزندان رهبر شهید انقلاب در هیچ کار اقتصادی دخالت نداشتند، در هیچ بانکی حساب نداشتند و در هیچ شرکتی سهم نداشتند و به ساده‌ترین وجه زندگی می‌کردند و شناخته نبودند و جلو دوربین نمی‌آمدند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/664774" target="_blank">📅 23:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664773">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dff1JCuaZ4gr2vza6Sx100_Jv90TKWb6fJ_LPRe17Kwtdtef5x4g5DriBIH-XF6UG10XkSELXwtaHWhXVXSh1owLuLaPnGcCyQqKpjs0cKXfjId7yKR8_39biSr6H7bDDUaAD-eWmk36OMHppv4s5RoyYW36P3OUmadFsGVmkhFX6wiLFDdaUTqbgUkpDcft8-oCgm01zNPqLtBYmmI2zPZVstkA0lJlkfa--kJbr5TKT0CKuKAKcEQGyopiCvT32h33N6cDhymx_vOsUpR4cUkPM4NEjVp5OuIFRYZ8uQryU-y5f92IjI8KixNwyprGJY4vEygtrvVaFr2kUMwBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام نوع پسته بیشترین روغن را دارد؟
🔸
پسته آنتپ ترکیه با ۵۴ تا ۶۰ درصد روغن، بیشترین میزان روغن را درمیان پسته‌های جهان را دارد.
🔸
پسته فندقی ایران نیز با اختلاف بسیار کمی از پسته آنتپ در رتبه دوم قرار می‌گیرد.
🔸
سه نوع از پسته‌های ایران از جمله فندقی، احمدآقایی و اکبری جزو چرب‌ترین پسته‌های جهان قرار دارند.
🔸
پسته کرمان ریشه‌ای ایرانی دارد، اما به دلیل اینکه تولید و صادرات جهانی آن در آمریکا انجام می‌شود، در بازار با نام آمریکا شناخته می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/664773" target="_blank">📅 23:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664772">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سردار حسن زاده: زائران، فرزندان خود را در مسیر حرکت و وداع با رهبر شهید نبرند چون به دلیل ازدحام جمعیت احتمال آسیب دیدن وجود دارد #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/664772" target="_blank">📅 23:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
جزئیاتی از نامه ترامپ به رهبر شهید درباره حمله نظامی به ایران
👇
khabarfoori.com/fa/tiny/news-3226668
🔹
درگذشت معاون سیاسی نیروی دریایی سپاه بر اثر سانحه
👇
khabarfoori.com/fa/tiny/news-3226700
🔹
شغل مداح مشهور چیست؟
👇
khabarfoori.com/fa/tiny/news-3226671
🔹
دو هفته اختلال، دو هفته بلاتکلیفی؛ بانک ها وعده می‌دهند، مردم هزینه می‌دهند
👇
khabarfoori.com/fa/tiny/news-3226665
🔹
ویتکاف و کوشنر راهی دوحه هستند، ایرانی‌ها هنوز نه!/ تنش بین ایران و آمریکا در چه سطحی است؟
👇
khabarfoori.com/fa/tiny/news-3226479
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/664771" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664769">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cdecd7bc.mp4?token=FBOMkRnpRTYX3LBPDeTqwMtSgBHDciochcoa4rvWb0OZXS-Fcp3iIhSQx8iy0ciUrDVpd0Jfc0ZslQl5n_8IjEEoPHgVbxD-3a4xHnGygjF7iTMB2XIRH7-Ps4YJTTTbIWPsRf_M65hoJBAXo7flglPYwEPCcZ0ofURegbV_UhmYBVryMcUAoGF6qjAAal_GZuDtmm5ekFYv0HOXm4BCLJ38A4SC6hkd4rwd-IPrDmoXzLHAkZoYw7OOzCouMjog912uyrrSUYQFeSNjGQVZQaWnmhPTbn3BjeZ4nJnmgoXkJ4od-GfFK6AQBn8Exaf_6VDggZFqiocugTTkyY_CsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cdecd7bc.mp4?token=FBOMkRnpRTYX3LBPDeTqwMtSgBHDciochcoa4rvWb0OZXS-Fcp3iIhSQx8iy0ciUrDVpd0Jfc0ZslQl5n_8IjEEoPHgVbxD-3a4xHnGygjF7iTMB2XIRH7-Ps4YJTTTbIWPsRf_M65hoJBAXo7flglPYwEPCcZ0ofURegbV_UhmYBVryMcUAoGF6qjAAal_GZuDtmm5ekFYv0HOXm4BCLJ38A4SC6hkd4rwd-IPrDmoXzLHAkZoYw7OOzCouMjog912uyrrSUYQFeSNjGQVZQaWnmhPTbn3BjeZ4nJnmgoXkJ4od-GfFK6AQBn8Exaf_6VDggZFqiocugTTkyY_CsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدگاه رهبر شهید انقلاب در خصوص واردات از آمریکا چه بود؟
رهبر شهید انقلاب پس از توافق برجام:
🔹
از وارد کردن هرگونه مواد مصرفی از آمریکا جدا پرهیز شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/664769" target="_blank">📅 23:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664768">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
روایت حداد عادل از نحوه زندگی فرزندان رهبر شهید انقلاب
🔹
فرزندان رهبر شهید انقلاب در هیچ کار اقتصادی دخالت نداشتند، در هیچ بانکی حساب نداشتند و در هیچ شرکتی سهم نداشتند و به ساده‌ترین وجه زندگی می‌کردند و شناخته نبودند و جلو دوربین نمی‌آمدند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/664768" target="_blank">📅 23:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664767">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_a4qtW-tfv75IdD9L7h7p0XfjH5hsB-3-tlcH67Wl9zIPFgYlMUizHtb7QFDsv2rh4oJoJgr4JyR_zaRhqY7XEDqQ9cQ2xAXKA-NvE7dK6ObpMyIkrVK-NM3kefcYKb9HgXzHlWBZx7QQuWsnmFHjz3nr1wUMIvd0hFaNALWUzpu9YE5cbhnei6rf8miRfSa6hgMwTHfXiUKAB_CE2MV77_wmGBv_36ehslwcEYKv3Rtv5MMhT_VrVA54tJ6ctuDxHFG1UI85gN5w3wb-PQN0XUt0jySduXsuunQlt5Lpj-67zmfUcRqqGYfiU0c_7c-9m-KlBidP5KjT9dV5uzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولتاژ بحران
🔹
با آغاز تابستان، بحران کمبود برق بار دیگر به یکی از چالش‌های اصلی کشور تبدیل شده است. این در حالی است که وزارت نیرو پیش‌تر وعده داده بود با برنامه‌ریزی‌های انجام‌شده، خاموشی‌ها به حداقل برسد. اما با وجود معتدل‌تر بودن دمای هوا نسبت به سال‌های گذشته، بسیاری از شهرها بار دیگر قطعی برق را تجربه می‌کنند. هم‌زمان، وضعیت منابع آبی نیز نگران‌کننده است و نگرانی‌ها درباره تأمین آب در ماه‌های پیش‌رو افزایش یافته است.
🔹
تداوم این شرایط، انتقادها از عملکرد وزارت نیرو را تشدید کرده و برخی نمایندگان مجلس از احتمال استیضاح وزیر نیرو در صورت ادامه این روند خبر داده‌اند.
🔹
هفتصدوهشتادوششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/664767" target="_blank">📅 23:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664766">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85b1a0a04.mp4?token=VnKJeHv3NC2_IeQWUM5-UGVfu4YeKx26sySp91UzrdaeTmgQ9NUqCgDZSz1la9lT285cP7maJNyzEd_nZoyvKFq2R__fFPkwYBficzSkyH0LJ7L6nQFDdUKkhXGvO5YnxLO0TF7Di6qPPnd7X-yTvrQhrbcPC-LyhAsW-1TxrR6G4fpGvHiO_t_l_-rRDOtUHROg6MCG66AYfH_Gch6Z6RQ5MbrEcfy2-6HvWo39Ods_WsXNxi-jpGTRFmr_E7S3jUO09NFHXOz9rmOyf9W_ob5xlIwxqqCFI9j1m4mElE5PUrN_GLPpt62xxPYeGpbiSw12PCUn7gDEa1O2h5idBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85b1a0a04.mp4?token=VnKJeHv3NC2_IeQWUM5-UGVfu4YeKx26sySp91UzrdaeTmgQ9NUqCgDZSz1la9lT285cP7maJNyzEd_nZoyvKFq2R__fFPkwYBficzSkyH0LJ7L6nQFDdUKkhXGvO5YnxLO0TF7Di6qPPnd7X-yTvrQhrbcPC-LyhAsW-1TxrR6G4fpGvHiO_t_l_-rRDOtUHROg6MCG66AYfH_Gch6Z6RQ5MbrEcfy2-6HvWo39Ods_WsXNxi-jpGTRFmr_E7S3jUO09NFHXOz9rmOyf9W_ob5xlIwxqqCFI9j1m4mElE5PUrN_GLPpt62xxPYeGpbiSw12PCUn7gDEa1O2h5idBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرکت بزرگ و مشهور انیمیشن سازی پیکسار که در آمریکا قرار دارد ، دیروز یک انیمیشن از خلاصه بازی تیم های ملی فوتبال ایران و مصر در جام جهانی فوتبال ۲۰۲۶ ساخته که در آن خوشحالی گل رد شده شجاع خلیل زاده بازیکن تیم ایران نشان داده شده است
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/664766" target="_blank">📅 23:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664765">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e3d25120.mp4?token=P_1Y2Lp30kLqUnEea3thV-ydjKTHLjOBCcaiQVtdbDA2CNUW2Wk4wlSugS67ewQSDh7euMzXKIoVJfPHNfrJZ732KI1e3dtJO4tV5yVHb29gdEUEyrc_Rqbnidw3_k_WRkAkPqizt5HdQhgq9eOgehmmLD2s4_SeyC_FsACWfEuy8aBTVl5ad3DnAZ_R5yFRoFOpQCP0y4habsgOpCoNj5o_ftfUUigj2ly78Dc2QwQp9S0Z6TZL4AkiMewJqFPAkBzb2rgR5ohDUqyx85SFkBSZHK7cTTsA-3VwspWRIJP2EduOVRVgiW_gOU6L14uF2oAnqSCq847Z8NMnJtofQ2NTOH_vwup9ZfNR0HJl-qSvtYZEUd6V8F-icqt7NQQdtLyFXuc56KONxm1LWb0lEp99NF7lL7g5LDi1iFJVxd08n6Ze8R20FnVa12PSRAJQIW5FAUQBQnm0Wp7u9aQPjqfdTpEdQkyOB-mD_OsmOSyMDbiUpcRTWiUSADyoe1d260N__5mrNCqmlpXq2BuhxZRAaAj9VJG0JT8-BJ4o1Z2p8rXKRZKZvJ1t6BtV3i7yWqHQFNktI03rQ6N5AbJZ9T77_yaeMzV-gZS5ipd4HOyuSZTWKZgnOg8CUf61I35qmA-NjXTQpbTWgw6eLEtokx9KXKKIugLfbxth8-qiIaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e3d25120.mp4?token=P_1Y2Lp30kLqUnEea3thV-ydjKTHLjOBCcaiQVtdbDA2CNUW2Wk4wlSugS67ewQSDh7euMzXKIoVJfPHNfrJZ732KI1e3dtJO4tV5yVHb29gdEUEyrc_Rqbnidw3_k_WRkAkPqizt5HdQhgq9eOgehmmLD2s4_SeyC_FsACWfEuy8aBTVl5ad3DnAZ_R5yFRoFOpQCP0y4habsgOpCoNj5o_ftfUUigj2ly78Dc2QwQp9S0Z6TZL4AkiMewJqFPAkBzb2rgR5ohDUqyx85SFkBSZHK7cTTsA-3VwspWRIJP2EduOVRVgiW_gOU6L14uF2oAnqSCq847Z8NMnJtofQ2NTOH_vwup9ZfNR0HJl-qSvtYZEUd6V8F-icqt7NQQdtLyFXuc56KONxm1LWb0lEp99NF7lL7g5LDi1iFJVxd08n6Ze8R20FnVa12PSRAJQIW5FAUQBQnm0Wp7u9aQPjqfdTpEdQkyOB-mD_OsmOSyMDbiUpcRTWiUSADyoe1d260N__5mrNCqmlpXq2BuhxZRAaAj9VJG0JT8-BJ4o1Z2p8rXKRZKZvJ1t6BtV3i7yWqHQFNktI03rQ6N5AbJZ9T77_yaeMzV-gZS5ipd4HOyuSZTWKZgnOg8CUf61I35qmA-NjXTQpbTWgw6eLEtokx9KXKKIugLfbxth8-qiIaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ر
وایت حداد عادل از نحوه زندگی فرزندان رهبر شهید انقلاب
🔹
فرزندان رهبر شهید انقلاب در هیچ کار اقتصادی دخالت نداشتند، در هیچ بانکی حساب نداشتند و در هیچ شرکتی سهم نداشتند و به ساده‌ترین وجه زندگی می‌کردند و شناخته نبودند و جلو دوربین نمی‌آمدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/664765" target="_blank">📅 23:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664757">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z05Jig37ucz4jojwBFKYRAMPHRdZeb4ixVrEHTFfVL2f2TNZQqSQfjZR93LEJ_7koHML-ZTK9SSicBkSPGqiPOqyfPFCq5zwnFFhGvddnypI09l7CT-Su2piLU8u8Q41PULRQPBaayInXWwKYPcl00LPWR3-NnCWFgBoGsgcM2CzmTqS4svIFia3vZBGR2ooHU_VCi6JaolVsPYMkeAnV1Kd9rCvMMqX6pQ6BPSsQG7MhxC7RCuls-L-iAXyZiQPy3VHKx-yfUbOPAc8-MVcFZ6MqnZWj85eblJlH8ZHl9sIu2_EoUvveLVmE2o_Koz-4ryDAsEQo6jAMFODhuf3cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taHCMtW6XXP7wr9vGnSdxWHvLXaak5MorJ91RLNv0UQgdO-_geCmIc7gscGJqq1VIkRO8746yachFX1OU4VUVD-XbBPwdCG7pOCA3cjyQiMPsf_e-xc4RtHhDU1dJOq1TdOel_b3tqEjKaURZr55pMt9Jm24IGG4xT6xLNkRs2sIP9X2gD9dBMTIAR7E_q4eg-MolwWvLt0ghPOt1-xKVlX0HFBObBomxsB6OEifY3DxdzlfFOG8uVMr4WbiT7BjjGpN2Xfl1OxTUVR1IzbpGkVHoALvNbCdWPFHAFPN-yrSeb48CvTgrU1BX-ACA-JCs8O9IzmusyTpaeHU1neRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuQbrj3E-i1mX-In1tugFyT8DJGIX36VAxJrorVbcQ87I_Vh01_k16zh539luhBDzfxuSwU7ThVHbVlrwY439-zVoDidA4OgRTEjDwV7pjq-WSVbVJHZj8Kn0GI6KwdDAYiIR-3obV7mP9dvfWdmCucfSjQzbYTdlGXRQOivxAL1Joq-yTN6T-lrDrCzEYb05WfscLwc3SuV7itBmqfaD-8IkiCV8ThuZmzO_NSYHQh4jKbrBJhMPcEg6u9FsTBnFTHnK6K3v4NPCf2ez_z3ZFvfdPSUDPCpitKVAJo3GfIOCWvcYl1cXOalTMjcBD42pGL6wxmFeirh_1JFUEVJ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9486bb21c0.mp4?token=j6dQNjvARBrInnvWZvvcGaNKWrSE1HAuTvVN9ORSXtb_IwhWMgHB4P6jrjDp0FXpmiWLMS0eE35Jc80ba831dSTCr6Ljk2yyD9tnAfOhTU0-wYFqdd0c2TPuOT10YGhoAxnAYuyK3Kjx_VT8t1PA0AQoyXhX14YkahMmTw1FjGXH1-WNDt2brV1MUKfhKq3kmdnC3cQ7E-tUop27L6P8gGUuEb2vd9tJWlRhrDrv9NjukguXYrqeNE2Ulo4EcOvXLD1vySncv7D-ci1Js5gilfGIWS6UFmCgV_w_1AViMUYOSHB7d1vR-N6yvaaJtsKDXJtZZQdYk0wVEKnkBs00LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9486bb21c0.mp4?token=j6dQNjvARBrInnvWZvvcGaNKWrSE1HAuTvVN9ORSXtb_IwhWMgHB4P6jrjDp0FXpmiWLMS0eE35Jc80ba831dSTCr6Ljk2yyD9tnAfOhTU0-wYFqdd0c2TPuOT10YGhoAxnAYuyK3Kjx_VT8t1PA0AQoyXhX14YkahMmTw1FjGXH1-WNDt2brV1MUKfhKq3kmdnC3cQ7E-tUop27L6P8gGUuEb2vd9tJWlRhrDrv9NjukguXYrqeNE2Ulo4EcOvXLD1vySncv7D-ci1Js5gilfGIWS6UFmCgV_w_1AViMUYOSHB7d1vR-N6yvaaJtsKDXJtZZQdYk0wVEKnkBs00LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای امنیتی عراق همچنان به منازل نمایندگان عراقی میریزند و حجم زیادی پول از خونه ها درآرودن
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/664757" target="_blank">📅 23:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHpJ1sQGSitmrVFbO1q3993Z6isEji77ZpNIeN0-lSJxKh87kek39dKhL7dFNz0wxvHV-BPKVixRhQCtViRK0XTARO_zxbxFJT6AgC8mfnTj0PW-OiSdsLR3vNDlDo4LDH1qRNgyyTiAy7MNvD8CTDdszPFm8AsRK501BTQYUbozuL9XxQoaaRux_WQMKgCb4PCReJiir5I-wyXsplfOlnjkAhXXOqcc1gevnqB2-xl9afrRLRTAlz3kZcRQMGOMBqPHYIAUHD6HkV3Nx9co6KvWh-Zfhy07GgVHshBSYBhsEMbUJg_YIjOEJfR-ZgZIqIXRcjnyFOmgTP3uO8Us1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پوشش_بیمه_ای_زائران
و شرکت‌کنندگان در مراسم تشییع رهبر شهید
صنعت بیمه کشور در راستای ایفای مسئولیت اجتماعی و تامین آرامش خاطر مردم، تمامی شرکت‌کنندگان در مراسم وداع، تشییع و تدفین قائد عظیم‌الشأن انقلاب را تحت پوشش کامل بیمه‌ای قرار می‌دهد.
به گفته
#موسی_رضایی
رئیس کل بیمه مرکزی، کنسرسیومی متشکل از ۷ شرکت بزرگ بیمه‌ای (ایران، آسیا، البرز، دانا، سامان، نوین و آرمان) تشکیل شده است تا پوشش‌های بیمه‌ای لازم را در چارچوب قوانین و مقررات مربوطه عرضه کنند.
#بیمه_مرکزی_جمهوری_اسلامی_ایران</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/664756" target="_blank">📅 23:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk36JGyUWu0-JuHroOsSmQ9ZzJA0-t4Ul_upxrSahIZMj7B7PRFQ3l95GL9r30LNJNZ9owEfo5Zr7N2IPQOmjTPMJKIhv8lYJPl6szqY8pZ5pE1jSOB9CA-fy2kadYG7s_NVNtBL9CDf4vzWtLMjPENtZRsm06anPskPHZNefR3Jyu--it05Cbyq3LG9kRXXRVHSDK9WzaosfaWLvU_STl5hGgEPIendZ7dis92MMgM9NFoNA6ErzKnoq6RTmr11zm-6jgxs2_dmA6pkvP13-_39V2pY0mmJ_SbAi32KLHqKl1oL-Dn6zUVY0F2navYQcCdXYnazcwZOScVgdMTNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جای نیش هر حشره بر روی پوست به چه شکلی ظاهر می‌شود؟
🦟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/664754" target="_blank">📅 23:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EICh9_ixIls5u6vC5stgkgXgf-nD-aPYyr-xsPdk4q4wmMUgFOynaWJBJMWSdyHC-IlhPegIdxNjay-aLa6G-EtGhXkIB_mXLJGOQHaEzLynbaCy1t9WGH-N40wnpERC_ER_aQGSumZEZazcT6vp6xwUCFqtKboDE58dLwxlGlvitLceP1XUWR5ZxPLV-3rCxTdNigeVPTpCR1zZWCVhdU05UBKs5uB5_aJQ6efNgUAR_gIFBt8IyTdZ3J4N8EaD0pRsSW02bSaermD8f6dVau2Vmv8uB4DEqSyjspJ2Zbc9niia4y7iBGdW-ub8Tiej4lCW_0hHGMsEvI5oSJcG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد رسانه ورزشی USA TODAY Sports از نحوه میزبانی آمریکا
🔹
فیفا با اجازه دادن به رفتار شرم‌آور با تیم ملی فوتبال ایران، سابقه وحشتناکی را رقم زد. اکنون میزبان‌های آینده می‌توانند همین کار را با هر تیمی، از جمله تیم ملی فوتبال آمریکا، انجام دهند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/664753" target="_blank">📅 23:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H93PwDth3_7Yi-3MkVB06fb5hC7sRwhlEbNYp8xPJqgBqJwyDCtkBWuNxEBmmgubXfrDW1XUirsiQKTkD2kkBGcYfXvkyEX3dsX_OGrmBBYmb8Mo7x-wKu7AVJ2JtIGw3AT7r43KQSybz0vDsmgRoWdl2NboA_zwhbLFfKTqOvHHmRaACWoisdKe9bKt6VkRdsebUSW9z5OE1K7EZ9qZzS_O3DW03WgmKvoWMOK9lHd-jQa2jKBCj1P5dZGoXCnaSWn8ZW05FG1RWg7b4md5jjnxkFJYKYY4D4snirFjItzKNYj2S-dYNTstCpwiblXd7TgQrjDi-qSXyYw-2SjvZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهره جدید آرمین زارعی ملقب به آرمین 2AFM که در فضای مجازی بحث برانگیز شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/664752" target="_blank">📅 23:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
خبرنگار آمریکایی: ایران و آمریکا در قطر با واسطه‌ها مذاکره می‎کنند، نه با یکدیگر
خبرنگار نیوزنیشن در ایکس نوشت:
🔹
یک دیپلمات آگاه از مذاکرات به من می‌گوید که فردا سه‌شنبه، استیو ویتکاف و جرد کوشنر، در دوحه با نخست‌وزیر قطر و دیگر مقامات دیدار خواهند کرد تا در مورد مذاکرات با ایران گفت‌وگو کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/664751" target="_blank">📅 23:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d42e15cf.mp4?token=v8klMh0nG_-SSiIAvIZz2ya-2-E8yMZfswEjaWTk9N0Ay6V8LSmtw2-gxBpZgsz3B3d77XliFurFYOnJ8JbF4K3dYvhIX5O3olIogkBeUaRJgHzHJ0BZSSl1HaxsNjGQcd9B4NsFtDFTugg8pQS7Zwq776Dw8qjC18lLXTcNxJUnaoFzEkvntQerABbjKQMCWkwOmAxJXyolOwUFaMk2eZNciYsd84188pIsf1vhEwmPkFFC-1VSV5dwQ-uhR5CtWZLprO76BHmbu9Nody8T65p0goDkMZKVzDK9F89FzsgStZ-QKAdKhAcxxJIX_80EtnTCf1v9VFxWZjz7bIjrTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d42e15cf.mp4?token=v8klMh0nG_-SSiIAvIZz2ya-2-E8yMZfswEjaWTk9N0Ay6V8LSmtw2-gxBpZgsz3B3d77XliFurFYOnJ8JbF4K3dYvhIX5O3olIogkBeUaRJgHzHJ0BZSSl1HaxsNjGQcd9B4NsFtDFTugg8pQS7Zwq776Dw8qjC18lLXTcNxJUnaoFzEkvntQerABbjKQMCWkwOmAxJXyolOwUFaMk2eZNciYsd84188pIsf1vhEwmPkFFC-1VSV5dwQ-uhR5CtWZLprO76BHmbu9Nody8T65p0goDkMZKVzDK9F89FzsgStZ-QKAdKhAcxxJIX_80EtnTCf1v9VFxWZjz7bIjrTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ارز صادرکننده‌ها به کشور برنمی‌گردد؟
/ مدار
این گفت‌وگو را در آپارات ببینید
👇
https://www.aparat.com/v/jmrz2dg
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/664750" target="_blank">📅 23:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c9d96687.mp4?token=u4CfzENRlZUydwqL5KR57ROhoc4RZzFfvl_T3D4g5rnKQlkfJkSafH1dHDeNOvNh-4WjdyBszKktKK4Pmm62telPHInU5ewAOqs89YtwHJ_Z-UlHX22r-6x70Azj80UEf1BHsxRF7Mhjv-qCGFlVE-Ed2yvu2D_G1r2DpMEnXjsNm48FifvRHKJU19RfjyX2JS7B1RI-NnZVaxi-xlCdawgNSJja2n4XAvpw2NlAK-0tOY7A94gc28h-WUwo3MfLpXOaCMKeKjvqsWqrOHfI6O4YpL-DmYhZxG17prfmCNjoqi4-ETFmB2x40NiekCwu-OG9hZST2df4vqgqf2TqIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c9d96687.mp4?token=u4CfzENRlZUydwqL5KR57ROhoc4RZzFfvl_T3D4g5rnKQlkfJkSafH1dHDeNOvNh-4WjdyBszKktKK4Pmm62telPHInU5ewAOqs89YtwHJ_Z-UlHX22r-6x70Azj80UEf1BHsxRF7Mhjv-qCGFlVE-Ed2yvu2D_G1r2DpMEnXjsNm48FifvRHKJU19RfjyX2JS7B1RI-NnZVaxi-xlCdawgNSJja2n4XAvpw2NlAK-0tOY7A94gc28h-WUwo3MfLpXOaCMKeKjvqsWqrOHfI6O4YpL-DmYhZxG17prfmCNjoqi4-ETFmB2x40NiekCwu-OG9hZST2df4vqgqf2TqIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من با مسکن پول زیادی درآوردم؛ دموکرات‌ها لایحه حمایت مسکن را دوست دارند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/664749" target="_blank">📅 23:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای کارشناس انرژی: نزدیک به ۴ هزار مگاوات نیروگاه برق، از مدار خارج شده است!
محسن میرافضلی، کارشناس انرژی در
#گفتگو
با خبرفوری:
🔹
۴۰ درصد برق کشور در تابستان توسط کولرها مصرف می‌شود که حدود ۶ تا ۷ میلیون کولرگازی در کشور وجود دارد که بسیاری از آن‌ها غیراستاندارد هستند.
🔹
نیروگاه‌های فجر، مبین و دماوند که مجموعاً نزدیک ۴ هزار مگاوات برق تولید می‌کردند از مدار خارج شده‌اند و این کاهش تولید شدید یکی از عوامل اصلی قطعی‌های برق است.
🔹
به دلیل خروج نیروگاه‌های کلیدی از مدار، بخشی از برق مورد نیاز صنایع از طریق شبکه خانگی و شهری تأمین می‌شود که خود فشار مضاعفی بر شبکه وارد کرده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/664747" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e6a460ac.mp4?token=f6bPGHWnauTE_Hy0tbH31qmkS83eXoIHQlOwUusrGqzCBqzqzgR4-_hkxq_T-r1fdcyH3PTAtaS1yX88WmrApF8_KEdm0A1Qoty-xYtUfWz_vCyqnbtrvI_UySl0KZDhY_KNqogSRBk-tvklJAvM9FlkhmDuUSPUsvcnOKvBT0fvNnCn4TlIAjKlHjwxq8Yphdf_jUjtszlyjjfIv98ud58qTz4sovdHHJtvjHsnPxt6K7PZlpxpk_jzUeXCLgGaIqbZn7n8Q-EK-K9WxmypVocatl5CNTFd53NcjaDdnS-lUwf7UcO23jU6lXAfWgdOS9sZ-M5sM938doWyqy-oTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e6a460ac.mp4?token=f6bPGHWnauTE_Hy0tbH31qmkS83eXoIHQlOwUusrGqzCBqzqzgR4-_hkxq_T-r1fdcyH3PTAtaS1yX88WmrApF8_KEdm0A1Qoty-xYtUfWz_vCyqnbtrvI_UySl0KZDhY_KNqogSRBk-tvklJAvM9FlkhmDuUSPUsvcnOKvBT0fvNnCn4TlIAjKlHjwxq8Yphdf_jUjtszlyjjfIv98ud58qTz4sovdHHJtvjHsnPxt6K7PZlpxpk_jzUeXCLgGaIqbZn7n8Q-EK-K9WxmypVocatl5CNTFd53NcjaDdnS-lUwf7UcO23jU6lXAfWgdOS9sZ-M5sM938doWyqy-oTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ متوهم: ما تا حد زیادی با عقل سلیم حکومت می‌کنیم
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/664746" target="_blank">📅 23:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664744">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4430f5d6.mp4?token=d-rYdy6nov3SPq4fxi-k8kgZZFmpO9yX5BtV1TFOGhDX0apAAKd02tSA41fh2a8Qu6CIXdcCeB3ColvS08KnBXe5ala59M_LB6_3TTKxIQw0L-lZCl_y_HWu2EdUG9bdeTvl0jeyEbWl0_yU7SGKI0RqwIvtLixWVv84IPjlH7sMAAg_KUE0dbq62cf5_HC8SK_dDmkXiTh27U_vaxveG61gFWJLMhcSs0Coe8g4z9lg5Y-pp1emsl0ghf3JowFnMVOdMZoPYkOfkllQbNEEBWEiWN9ccyf7nIcpzfDU4dDLmkyTTyYqb2oEZkbniiO_xc1fzXQM389MLlP5vV1KTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4430f5d6.mp4?token=d-rYdy6nov3SPq4fxi-k8kgZZFmpO9yX5BtV1TFOGhDX0apAAKd02tSA41fh2a8Qu6CIXdcCeB3ColvS08KnBXe5ala59M_LB6_3TTKxIQw0L-lZCl_y_HWu2EdUG9bdeTvl0jeyEbWl0_yU7SGKI0RqwIvtLixWVv84IPjlH7sMAAg_KUE0dbq62cf5_HC8SK_dDmkXiTh27U_vaxveG61gFWJLMhcSs0Coe8g4z9lg5Y-pp1emsl0ghf3JowFnMVOdMZoPYkOfkllQbNEEBWEiWN9ccyf7nIcpzfDU4dDLmkyTTyYqb2oEZkbniiO_xc1fzXQM389MLlP5vV1KTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناراحتی ترامپ از حکم دیوان عالی
دونالد ترامپ:
🔹
حکم رأی‌گیری پستی کمی تعجب‌آور بود. این به مردم زمان بیشتری می‌دهد تا به‌طور غیرقانونی رأی بدهند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/664744" target="_blank">📅 23:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf7UF19uqj0UWOTHpWtM9p8fEY8V_0vo5kQrFBEzSkENbYK0myCNWpwkdUwcWbNHm49qtonex7NZV5rru2t_PMk96NxL8D8ucAKXaxiwkpBCy7_JRKqdcvfx6tNCt80VQRsR9s4tCA_SAv8Bu4o4S6ipqtZl8zlPO5W8hBgCZ3-aF0XlWPmFypBae75qX6Ilta55xvtdt3cY53aU6tsPw2jWm25bsiaDs479ln9tiIkfuzaXQeVwYzx1DPCdwHLbFH2O8O-2_14mft42rUtRL_irsEEqS6uspfXkUzTF-saUkGIMJ5vJ-LKOqH8mi40JdZ4jG2CB3yqy3M_ZPPc_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gG6wWUig92SzDedKyU-4CJqvGIAhyft_61SyPKo-cxJK9JHbDtHyaB-aPSzLfnvWBAyj5lJktjT2Mc5iOZ4qth78X-naokWuK7LIVQUlNT8-kIxfgGE8ucx77ScfupAn80zz0Trfr39S_VaK7wSLkzMJRcVgZXG7K858qviL9oHEHarpCpXFBoSGt18gS3SawaizBFIJi7EBzZ1M43JL_V89fyJjEQf9GsrHi9DEwapyWsAut-a-m1-r4xTBGE5i9yxcU2uqXp0sYV7ln-PFkbuOchPhTMuZYg_WJVtdkWZEmIRygz6oM1BRXoKNpoFfWNw_-3zqehPxsH_OyW1QoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JedtTP2nHmV6enyleidWZQl1HlOts944ePHddhAwl3VxhDra-uDcBtLjSbhm7RCNChuqfz0nq34ZXOMfj6a1wAR7EDDD8YPqSecR5d2D1i-SNhYW5rP4YtBrUIKW74cG35VLPzh8usSNW0zDNgL2qIrj6fs3LrEiKMPNxsyFY7mKGbxGNSXbRczs2WHpaRgjFMeYemL4SVgL6p7x0TlIlC6rwwXttfrn4RyBQwXaVcdwt2RaywkFL9iAtyPpNqbCPdy7OIyt1aFEXg90dA92GzhepAiIuSuSshoThDoAtqxv7DzQgMwBi4XVBMoQkf0YIL8e7SXw9qFXVM9e4U78Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRKPy9NnnWjM9nlONSps7jIams4D8loiBT8lhp-M9kFRiwQZis821kt0eOF8N0ip2wfRuc5xgZkPYzbKNxGzfC1WQWUoEFVrv3F6wy547Z8II3mU6QL-fj0vDWF9KzSUzIFKs3m-HnfYsrIo8K7nEIjoNzYRPuDtNiGRR2KQINRC7BNl_xbqki-k5DFonmeb8ITpFhDt9rpANkWAHGDt-pzNMVlKvwHbQ_7rLUQJ4FCCnmRp-TMydv5JoWYr8nkztz1HfMW4-0clDllvJicnoUKJOxuFpKIDefdsPssXvzWTKtozaQwLlTWonLhwjWfxJhUTcTts6nZYSHxrig1OJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXrfxo7rXeQVqd_I_N7b6s1KgFTuH2lfth9_tJNbKSiSsTotNSa4hQu0lxALC1CtrZb_l6K8gJzfdy9CosyQ7qnWRvQ3JAog1tLNwlx9fkLNJ4_nMh7TJ73df7DVS7sfHM-hgyAtel94RR3ZumfJSzA71ZjUyZDMI_9BGq8vn36k1rLbzps6Hf_ApzLB3vRdcnHvtDY32tjj7YMpX_7Tr-DUfEeuS4FgpeC1OgluHGM7tQdMhJL6LdiDzkbT8f-lmSFs6t4jiGN_cGsVEFnwZxIyCghXtCqgMEdfEU2eJ7vnBNkwdJl60KZscUy0aGzmNSqouXD8eO8qHpLvoY6swQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNnu5hT46GetxDWrnaNo8MbzP9tdPdqjolJwad_ikVkt3tHmzla8_vCiN3OYJm3fT6MIs9Nyfms6ydvVZhil9eXQjOrHst2dxWb3VLu-zzHjfVQi-xr7UI-2VRJ-Budbhniv9lM60EGhG93tppnAFCBWFAufZx4bAJriJBd0LYIMJu81ZtWlkTgfecUf98P_XnOJbCb3-n0CMijhsitXb5O8BQWMcP-HABg5hPLyPwStM3cdTE3qRUkyS-kej1OUuL7pwZFnjy50o8c66zYP8Ofk5eeF59bvn19tlaJCxk7pLja6npSzFokqhMdjS0v2yVRpnbDU2PSMDa52KBIA7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ebX1TFKJUrqYaqmNP-8VyNeefNYTur05FGX-Gm2xLbODAqBb3kAoezNpcLQ2fnYh8VgLL68X7hlJra_MjV4qjCyHZvSEFXcR4KwNUlvgT5VzvBn6W_xAjikDc1UVgvaAGeyJkmlGLoSMmj5gynyV9GFgY01WL6vgaKEbvNY7HYb6gX5v711MdQmmelmX1RvY0VX4q_Uvck0q14FBuvh6Kn8QepQh90cemWrZ3sc0jK7dx7ebZ2KFLRS-wDP_CB0bhmL3n5So9ymp9TZOFBGb0FU-Rqk5yb3PlA-EJsES1ycL7377g_yhfrAwY7b2twknPvKDfPUaNEQRI2erZMSAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EG02L5JH4WCztBAeSk2nwjVrsvFCg_mWXM5ZIalwkLdqH2c-uNxZqLTGITh87UKDqiXVtdTg9l0ZLX8cSp7EOZgTaiPSs1oDkCU-2tMmgBjxErmrTxwIf0ghcLgis0T8CCQpPPZ0oxNiBxYIx4L74CBsNBthw_ws6TZz4CD-G5RP6sJfPDWBbVxl3qnw6ZqDXxH4Xa6zl9WKM9rRmpHZM5l4mEs0odofYFfqfIec6Yu9d7uroNJo6Iic91rq4njF0GTJDyNCy3zY9gSz13Eh_9cqFjuzivhGecelFvJ7JQbJHLnyoXvdxOx3TxH8gYFADlVnnF0-NX5kUkVYAAXorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOTqCPkMi7zoKJzpO0O-vfXuxU5i-lstJ2jD6-HEvtNIetVrOM_LHYzaO-JTDRYf1aKPhLQEckFI09UhqCjAqW4MmVCT4WQIP68CHZz9QGqk3hsw3F5yjy3CypDMl3VGeoDvOb7QP975AWRNGcWL-f-KhAIOm7y4ugQJD1yzJBKJQs89hdtjbs0HxGyZpnZzjd2_I3BIs27-3X0M22suPvvdN2vDffmXkD6xe0a4U2snzT7BkyByJ_KOasIFmsOtkeKJVpazZ9CvbvlUUfaFZhlg0f2rWAZ62iJV7Nzs8YDLXKDZs6luwpZ-waL-TLVjt4Fhua3kJYAwxGwyp0wERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxZrhGio-NKJGbFL0R4MhWIKkBrfnkHDUKE638K2RSvdzwMbfETEq6yQSlgJY7ul-_SyQVx2a3ViVJQi3LiMIMm_repj5oh-wK62etZEYEZpL7T23OqxPwcqvQVr5ozKFSkM_VI2A8mMaSqN6q1yslLM08qg9bLfahan64s7vxPBq1mRotpiw4OR-4N7XoZidLEr5LDFR0lA5o_MponXITqJRivZ9iKVQYhR8LQhmx2jmeH_J9g2WlYXwJQOElsNvXf1EzAtSjTUExiyOH1aV9b7580blOIhykJG6au3GDXqX36lnjcvx7yopTlMQONgsuxoE5qn9ZOQpasLT65CNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منتخبی از پیام‌های ارسالی مخاطبان خبرفوری درباره اختلال اخیر در بانک‌های کشور
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/664734" target="_blank">📅 23:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سالیوان، مشاور سابق امنیت ملی آمریکا: طبق یادداشت تفاهم، ایران بعد از ۶۰ روز می‌تواند از کشتی‌ها در تنگه هرمز هزینه دریافت کند
🔹
طبق یادداشت تفاهم کاملاً واضح است که ایران تا ۶۰ روز نمی‌تواند حق عبور یا عوارض دریافت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/664733" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664732">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8934d1061.mp4?token=bOhm3e7P_OYsoRIY3yL2nsh-YNPP8B2MoqsnJDBT8C0FqPs1JHGrrwjUmyDQtHfQeK9867QThKUxzPd3A44h0iH-pE2Ep7PAacB2qsyY2xVDuPF9zbiOaT1lCE5a4NHBgp0XiqJ8HmgxVkV54z6I8Z2CodFHtGMJR2LNhbYgwUCvgLwWpnOS9DTfIgAYyPtKvDauulsYKyHFSyHUTPdma3katGJnzcROQWKYQHnOVygA5pIFItjsgOL87O9UHTf_7vZLB479L6InmFGWNTfoyF9bj5t6uSJofS32wIxmJL7B1Yk-W408KaUmaxcOVSpSz7-0mJUh7DP269_sccoRQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8934d1061.mp4?token=bOhm3e7P_OYsoRIY3yL2nsh-YNPP8B2MoqsnJDBT8C0FqPs1JHGrrwjUmyDQtHfQeK9867QThKUxzPd3A44h0iH-pE2Ep7PAacB2qsyY2xVDuPF9zbiOaT1lCE5a4NHBgp0XiqJ8HmgxVkV54z6I8Z2CodFHtGMJR2LNhbYgwUCvgLwWpnOS9DTfIgAYyPtKvDauulsYKyHFSyHUTPdma3katGJnzcROQWKYQHnOVygA5pIFItjsgOL87O9UHTf_7vZLB479L6InmFGWNTfoyF9bj5t6uSJofS32wIxmJL7B1Yk-W408KaUmaxcOVSpSz7-0mJUh7DP269_sccoRQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دربارهٔ ایران: نشست دوحه شاید مهم باشد، شاید هم نه
🔹
خواهیم دید
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/664732" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664731">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4KP3le_DJIv0QLv4tapIPtHJ-a0_QGI8q3OqLbdWdFCjR7EgzDUpl__k3vnwLSBG_MwBe84ry7GpDoI2e1p2DCxm56cyJhZ800bt96LXKHW7kW17pSN11vKOcrSmoZGPiRPZ6cDZrlFZZGTSbR-CFpk2i6RZ9mglZ6i_mGRhXx6bXMMOl0PI-4wsgSg3BScmwMrOn8YBkz7ofTL1JLlXqYK8keg99p66o70cKVEDM3SG1sFAbD7o663geu977Ky73newwVnhtU_KR2wmHJo1Wuv43Ql1j96CeT3ULIzrgU47Au6VsvNKK9AVcfRywONixucIeUNvU1Uv7KEFKKL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
سفرش با تــــو
چمدوناش با مــــا
باروبندیل رو جمع کن
امکان خرید قسطی چمدان با
اسنپ‌پی
😍
خرید از سایت
https://baarobandil.shop/
باروبندیل</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/664731" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664730">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyK-61kHQTbn2ZmG_5VhaJb0p06Y9Wo7WODHpPprQ32dfNj32ewZfo0od1ZNWNPEM3Qn1TQ_c5TVyq-K2j-7pXmxfTlCAikvr77a2oh-YPlwLZxA6kAcQCiJX4N3PO81WRaTZchCBrJ6vTE731WW7wmbE21TMUvyuiV6ZjFT6wtdteMa-TldWJzXwvLeswGPEytU9lKOu-ff6n56quzAr9DEz38qPm_XnOMr7ByIuJ9CnorIbxbE3oLZDE3pdGjGWKn-mgcMyAaBtdX8v_2ubPEw-0hW0QXYzkF5EP8zlOonXCK_CkeeLSZyGH5zqKbJnxvAgZCGSl-9aZhg-HDPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داروسازی دکتر عبیدی از داروی جدید ترکیبی کاهش چربی خون رونمایی کرد
به‌دنبال ۱۰ سال پیش‌گامی داروی روپیکسون (
®
Ropixon) در کاهش چربی خون، داروسازی دکتر عبیدی از جدیدترین راهکار کاهش چربی خون خود با نام تجاری روپیکسون-‌پلاس (
®
Ropixon-Plus) رونمایی کرد. روپیکسون‌-پلاس (
®
Ropixon-Plus) از ترکیب دو داروی کاهنده چربی خون با نام‌های رزوواستاتین (Rosuvastatin) و ازتیمایب (Ezetimibe) تولید شده است و باعث کنترل موثرتر چربی خون و افزایش پایبندی به درمان به دلیل سهولت مصرف می‌شود.
داروسازی دکتر عبیدی از یک دهه گذشته با عرضه رزوواستاتین (Rosuvastatin) با نام تجاری روپیکسون (
®
Ropixon) توانسته است به پیشگیری از بیماری‌های قلبی-عروقی در بیش از 1/5 میلیون نفر کمک کند.
برای مطالعه متن کامل خبر روی لینک زیر کلیک کنید:
B2n.ir/zy8686</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/664730" target="_blank">📅 23:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664719">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a4caf891.mp4?token=Q5As_dOM1fqfhmL4WjxnNkVZFmyEVb2EG8iqnYhyUr7NgEJwtt7LSQMGxpEWdDqzYX4x5eBxAxgxjd7q8DkVsQON1Q3Y0fj6JsC3HpMPDk_3Ngd6drXJm60c924OrteYQgnEJRUIkLok6eaKdnGYLAHqj7O-5zDjB5YxYZAkQ-8iHT3MPLQEc-sK8OTPUleehC7FddvgLl27H2q9KaTGk_o5m5wJKukIUqm8Ir1NDk4Af--VJgOMlQYNM09ay_0aOYDtHgvKXNNG45tFlCUn6BmcDkPx6rppgaKPZwtZ3N6m8PapoUe1NzpM0uFH2GB9BYZtgg8uOpnj2jOuIBBG_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a4caf891.mp4?token=Q5As_dOM1fqfhmL4WjxnNkVZFmyEVb2EG8iqnYhyUr7NgEJwtt7LSQMGxpEWdDqzYX4x5eBxAxgxjd7q8DkVsQON1Q3Y0fj6JsC3HpMPDk_3Ngd6drXJm60c924OrteYQgnEJRUIkLok6eaKdnGYLAHqj7O-5zDjB5YxYZAkQ-8iHT3MPLQEc-sK8OTPUleehC7FddvgLl27H2q9KaTGk_o5m5wJKukIUqm8Ir1NDk4Af--VJgOMlQYNM09ay_0aOYDtHgvKXNNG45tFlCUn6BmcDkPx6rppgaKPZwtZ3N6m8PapoUe1NzpM0uFH2GB9BYZtgg8uOpnj2jOuIBBG_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقض دوباره
حمله هوایی رژیم صهیونیستی به مناطقی در جنوب لبنان
🔹
جنگنده‌های رژیم صهیونیستی در تازه‌ترین تجاوز خود به خاک لبنان، مناطقی در جنوب این کشور را هدف حملات هوایی قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/664719" target="_blank">📅 22:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664718">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نمایندگان مجلس کنست اسرائیل به جان هم افتادند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/664718" target="_blank">📅 22:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664717">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2jbdM-jIbAkLUrZpkq_1JoYL2cqFTn62X1pcGJxMkD7Z1dYHaLhOqCfz0rA2Gr1ONCw5n68SwJUXLUmhNc7MdB_CiUMUlknZAat4Bt1rRhRjAhFGqGXPX22P1TIgJ85eZSx7V47fEvixwQvd5lZWtDkrhKBfomWzCiNCN8LsIXioQ5IdCgXc1uAuoZ8dVQAPnmvXQ2aO9kWGT71iWBd_R9t2_7Hu6UXdr4xmJHM2FNMfODj4Wes9zCiVoKhP5WoVnDf3YspsCi-4sdkf3vaprElwr4k0eiSobCvZC88QMHLAxtXaSjPzHLSJoBS7J4voKIU_-FH1BTmjgBSSpz2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سکوت، پایان ماجرا نیست؛ آغاز مطالبه است
🔹
مطالبه مردم روشن است؛ پیگیری، پاسخگویی و اجرای عدالت.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/664717" target="_blank">📅 22:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664716">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سردار حسن‌زاده: امکان ورود ساک یا کوله‌پشتی یا وسایل حجیم به داخل مصلی برای مراسم وداع با رهبر شهید وجود ندارد #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/664716" target="_blank">📅 22:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664715">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آغاز تحقیقات دادگاه لاهه علیه مقامات امارات متحده عربی
🔹
دیوان کیفری بین‌المللی (لاهه) به‌طور رسمی تحقیقاتی را درباره تعدادی از مقامات ارشد امارات متحده عربی آغاز کرده است.
🔹
این تحقیقات در پی اتهامات مربوط به نقش این افراد در بحران سودان صورت می‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/664715" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
برنامه‌ریزی مجلس برای استیضاح وزیر نیرو
امید نصیبی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
قطعا مجلس برای استیضاح برخی وزرا برنامه دارد و یکی از آن‌ها وزیر نیرو است و توازن و عدالت در برنامه وزیر نیرو رعایت نمی‌شود.
🔹
عملکرد منفی وزارت نیرو در بحث سد پارسیان موجب بدبینی بعضی افراد نسبت به نظام و عصبانیت مردم شده است.
🔹
علت به تاخیر افتادن استیضاح وزیر نیرو این است که باتوجه به حضور او در کمیسیون‌ها مشکلات برخی نمایندگان حل شده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/664713" target="_blank">📅 22:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
پزشکیان: برخلاف برخی ادعاها، در مذاکرات هیچ امتیازی خارج از چارچوب منافع کشور واگذار نشده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/664712" target="_blank">📅 22:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9UFeAmNtze_H6sEv2W6STch3QroMxowRQ1EIg5hiqkIL1XOuJOFRhL_x_3VASH8t-w0FXCDswmYin62A5NkyH9ZC7gcnSTE3pNfsHyXPisOGmPHDetTUw0DVB21JjqFxpnXuWQEC1JGR5msd74ps06iFtol3wVhf-H6bINYu6DV7HEZT2A8FwTUKkfvXoN0fr5xKWoS7-v0yWO_vVD-_GJNlDqZnrjDO5aJV5ffcHhptfN5_xC3GZvqAEQ8Xuj5WUa35iSt6oqQI49wI6ZxIKZtHJJXX589A3CkSAnWXZMPAreA1Q7ULPSJHFZn1sf6Bl2hZI9tkPB1i0A025u1tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
سردار حسن‌زاده:
🔹
طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
فرایند برگزاری و اقامهٔ نماز نیز در این طراحی دیده  شده است. در واقع، این طرح، طرح وداع و طرح شهادت خانوادگی امام شهید و خانواده‌شان است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/664711" target="_blank">📅 22:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664710">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
بیانیهٔ مشترک عمان و فرانسه: ما بر تعهد خود به منشور ملل متحد، حقوق بین‌الملل و حقوق دریاها تأکید می‌کنیم و بر اهمیت بازگشایی تنگهٔ هرمز پای می‌فشاریم
🔹
بر اهمیت حمایت از کاهش تنش منطقه‌ای، تأمین امنیت راه‌های دریایی و مبارزه با اشاعهٔ سلاح‌های کشتار جمعی تأکید می‌ورزیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/664710" target="_blank">📅 22:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
پزشکیان: برخلاف برخی ادعاها، در مذاکرات هیچ امتیازی خارج از چارچوب منافع کشور واگذار نشده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/664709" target="_blank">📅 22:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
کاش پاتل، مدیر اف‌بی‌آی اعلام کرد که از زمان آغاز جام جهانی فوتبال، بیش از ۴۰۰ پهپاد غیرمجاز را نزدیک استادیوم‌ها و سایر اماکن ورزشی رهگیری کرده‌اند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/664708" target="_blank">📅 22:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664707">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
مشاور سابق امنیت ملی آمریکا: کشورهای منطقه دنبال توافق اختصاصی با ایران بر سر تنگهٔ هرمز هستند
🔹
جیک سالیوان در پاسخ به این پرسش که آیا کشورهای منطقه ممکن است دنبال ایجاد چارچوب امنیتی بدون مشارکت آمریکا باشند؛ فکر می‌کنم به‌سرعت درحال نزدیک‌شدن به این نقطه هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/664707" target="_blank">📅 22:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d91e5c60b.mp4?token=AAfKNzCZB1ggu-UkclPVKgwTxTYJHOaAqnW_UXPI8yjIDaBd2FxWQ8sU1vAcy_kTLCYbhlbgySGyUZgIvDscMaAkQlIrsH255ExbvQSJtRANswQ8IgnmwGXwO6OzACyE_NhqC3sUFH-smoe76_7TN-fpGzciYn0RHEOZuRX1sXOpvxi3WGd26CraG8gngpbQecoTfZ6AfXqlSvvmJm0oEpprCqN9J0tMCeaGhLhQAYTY6PNtYQ93RELVRovZP03a-1-ZUhkKFQXawxkJLYRbm3-BPfBQmJhDZdTA8ogPgRmYKMcm_fn5KKrLDWSKvzf4eh8kx2cqVmUmPdOxY5fqQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d91e5c60b.mp4?token=AAfKNzCZB1ggu-UkclPVKgwTxTYJHOaAqnW_UXPI8yjIDaBd2FxWQ8sU1vAcy_kTLCYbhlbgySGyUZgIvDscMaAkQlIrsH255ExbvQSJtRANswQ8IgnmwGXwO6OzACyE_NhqC3sUFH-smoe76_7TN-fpGzciYn0RHEOZuRX1sXOpvxi3WGd26CraG8gngpbQecoTfZ6AfXqlSvvmJm0oEpprCqN9J0tMCeaGhLhQAYTY6PNtYQ93RELVRovZP03a-1-ZUhkKFQXawxkJLYRbm3-BPfBQmJhDZdTA8ogPgRmYKMcm_fn5KKrLDWSKvzf4eh8kx2cqVmUmPdOxY5fqQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انار خرمایی
😳
🔹
میوه‌ای عجیب و جالب در بنگلادش که شبیه انار است که داخلش خرما است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/664706" target="_blank">📅 22:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70eb4993d7.mp4?token=LsjZ4aReEMFkG04sIQK23M5yQN7dojbXwhhx6zyG-BQcaIzg3yibhL6qZD-Z17j-nyvgcmKtk5D49RSOm81_6hLUur0pEd9InzHaUkc66SPSVA6ztn_-ULX-JwUz7vLsHctqlkXOidZ42UUwbnZrPnauCBBziVYo9rwWZt_2ZoH4DM9XXPC3dvABGkK7dpwzgWXKptzt5DDmidStOXQbjD6HvHx_fJeXREH59ctI9lOfv_Iokfpg1XXvfRjWisM_ac5reTXaoMPmSjqtdGL_3RByiSqykxRDsCN_-j-lN4Oehn7-znq84VqM0jL96RdM6E3jAw5SlSexnswh6ObYxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70eb4993d7.mp4?token=LsjZ4aReEMFkG04sIQK23M5yQN7dojbXwhhx6zyG-BQcaIzg3yibhL6qZD-Z17j-nyvgcmKtk5D49RSOm81_6hLUur0pEd9InzHaUkc66SPSVA6ztn_-ULX-JwUz7vLsHctqlkXOidZ42UUwbnZrPnauCBBziVYo9rwWZt_2ZoH4DM9XXPC3dvABGkK7dpwzgWXKptzt5DDmidStOXQbjD6HvHx_fJeXREH59ctI9lOfv_Iokfpg1XXvfRjWisM_ac5reTXaoMPmSjqtdGL_3RByiSqykxRDsCN_-j-lN4Oehn7-znq84VqM0jL96RdM6E3jAw5SlSexnswh6ObYxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیرخلاص برزیل به ژاپن در دقایق پایانی؛ گل دوم برزیل به ژاپن توسط مارتینلی ۶+
۹۰
🇯🇵
1️⃣
🏆
2️⃣
🇧🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/664705" target="_blank">📅 22:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664704">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
غریب آبادی: ایران به هیچ کشوری اجازه نخواهد دارد که در فرآیند مین‌زدایی در تنگه هرمز دخالتی کند و حتی عمان نیز اگر بخواهد این کار را انجام دهد، ما اعلام کردیم که کمکشان خواهیم کرد زیرا مسئولیت جمهوری اسلامی ایران است
🔹
مسیرهای عبور و مرور توسط ایران تعیین…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/664704" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664703">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تلخ اما واقعی، مستمری معلولان حتی به دو میلیون تومان هم نمی‌رسد!
علی جعفری‌آذر، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
با توجه به نیازهای معیشتی و سخت بودن استفاده معلولان از حمل‌ونقل عمومی، پیشنهاد شد، حواله خودرو به معلولین تعلق بگیرد و این امر نیاز به جدیت دولت دارد که تاکنون مغفول مانده‌ است.
🔹
همچنین اعلام شد کمک‌هزینه‌های ۱۰۰ و ۲۰۰ میلیون تومانی مسکن، با توجه به تورم و هزینه‌های زندگی، پاسخگوی نیاز معلولان نیست و برخی ادارات نیز به‌دلیل ناتوانی جسمی افراد در پیگیری امور، حقوق آنان را نادیده می‌گیرند.
🔹
با وجود افزایش مستمری در دو سال اخیر، دریافتی بسیاری از معلولان همچنان به ۲ میلیون تومان هم نمی‌رسد و پاسخگوی هزینه‌های زندگی نیست.
@TV_Fori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664703" target="_blank">📅 22:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664702">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هیات منصفه دادگاه‌های سیاسی و مطبوعاتی، خبرگزاری آنا را مجرم ندانست
🔹
رضا توکلی خبر بیماری‌اش را تکذیب کرد
🔹
سردار حسن‌زاده: پیشنهاد میکنم اگر مردم مسیر طولانی را طی میکنند قبل از ورود به مصلی، در زائرشهرها استراحت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/664702" target="_blank">📅 22:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664701">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa35e724dd.mp4?token=kbajuiQ-6BFO7RZRwvIb6bd8dahwS_3F_yTQhHpufPrvzjaMVQkwMvg3Zn44-9Iw8vWYNfCZttWBKGjztI061e-uKtzCUQPnSRxmx-Y2GUaU092i9_E65gULGRiCtLk2riluHBBLG3Dr8eZFvSiPhNHLZzWIwQ8A05k8m30Lwo4XGVy3rutMV_wv4TxDolEERTfUvQ9XxNIPFcIE1HfYb2Mn9suHW6-DU-1w-oaN1hFI7fQ1JdbXyMJQLdRsMfRdzjJPzFK-rnjmWMzTTY8hjdw-NyIQnnxT7fYqAoPUKBQsZV26Oe2rLfo0VWk4TMk959L1swLyYFBNPHar6sbZSaop1towEOEtCkY9P4jIsGWfGFuIqO0L8J9DSj_b7-D8MZUUAahkGaxBHIp9V3adC-ZY0eze0ozPcmmYRzVKKkfAXihWen5Xbz77si9oYBztPUahIAZgDyj_6Fz9Qh_ginO-NF9tVN-JLhSLt-nInzUXxNXkdaede4O-fUVNwa0T3aubW8Qd18ECxQ8tFO37vBkeBgBMyR1UeFVQ3zSGqDGvDGwZy5jphb2SYbci85-pn2bQkCaBSXH1yElDNPBBPw5CfEkCGGyaJHH1pot14EJN2azLX0se3JZhvOVMjeeTqrzsppYrw-8dn-8F3rkzQMwI020pxWTtbKm6JG6QsX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa35e724dd.mp4?token=kbajuiQ-6BFO7RZRwvIb6bd8dahwS_3F_yTQhHpufPrvzjaMVQkwMvg3Zn44-9Iw8vWYNfCZttWBKGjztI061e-uKtzCUQPnSRxmx-Y2GUaU092i9_E65gULGRiCtLk2riluHBBLG3Dr8eZFvSiPhNHLZzWIwQ8A05k8m30Lwo4XGVy3rutMV_wv4TxDolEERTfUvQ9XxNIPFcIE1HfYb2Mn9suHW6-DU-1w-oaN1hFI7fQ1JdbXyMJQLdRsMfRdzjJPzFK-rnjmWMzTTY8hjdw-NyIQnnxT7fYqAoPUKBQsZV26Oe2rLfo0VWk4TMk959L1swLyYFBNPHar6sbZSaop1towEOEtCkY9P4jIsGWfGFuIqO0L8J9DSj_b7-D8MZUUAahkGaxBHIp9V3adC-ZY0eze0ozPcmmYRzVKKkfAXihWen5Xbz77si9oYBztPUahIAZgDyj_6Fz9Qh_ginO-NF9tVN-JLhSLt-nInzUXxNXkdaede4O-fUVNwa0T3aubW8Qd18ECxQ8tFO37vBkeBgBMyR1UeFVQ3zSGqDGvDGwZy5jphb2SYbci85-pn2bQkCaBSXH1yElDNPBBPw5CfEkCGGyaJHH1pot14EJN2azLX0se3JZhvOVMjeeTqrzsppYrw-8dn-8F3rkzQMwI020pxWTtbKm6JG6QsX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای درخواست آیت‌الله سیستانی برای برگزاری تشییع پیکر رهبر شهید در عراق
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
استقبال گسترده‌ای از برگزاری این مراسم در عراق صورت گرفته و بیش از یک میلیون نفر برای حضور در آن ثبت‌نام کرده‌اند.
🔹
وی همچنین مدعی شد بر اساس شنیده‌هایش، پیشنهاد آغاز مراسم تشییع از عراق به درخواست آیت‌الله سیستانی مطرح شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/664701" target="_blank">📅 22:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664700">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تردد کشتی‌ها از تنگه هرمز با وجود نگرانی‌های امنیتی ادامه دارد
‌
آناتولی:
🔹
داده‌های پلتفرم ردیابی دریایی «مارین‌ترافیک» نشان می‌دهد با وجود نگرانی‌های امنیتی ناشی از حملات متقابل میان ایران و آمریکا، تردد کشتی‌ها در تنگه هرمز همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664700" target="_blank">📅 22:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
چادرملو برای اولین‌بار به آسیا رفت؛ چادرملو در ضیافت پنالتی‌ها سه‌جانبه را فتح ‌کرد و به لیگ سطح دو آسیا رسید
🔹
چادرملو(۷) ۰ ــ ۰ (۶)گل‌گهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/664699" target="_blank">📅 22:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozJt6_BjkYhYZCJuZ7mxKYEWDRiYu6ClhMJNP3uWYsuDK7vKCcJHoKfQpF2-FrxvAUFvFvFznfT2M3M33_3FR8R-3rkq-bKvFfBj8jklrLreEvPDED9G9j87akhRKooKKkgLFOmLS732fyqWQQTQyDRHndMlmHcH_oiomH8YKPy5Kgcf71m3eLzubu_kq72CBHSErOu9_eVNUaHz1AcG0JCq6Il3X39CY_2fco6MGVLTB6uWb0-migIm7p8IVuG_V93Z1SY1LgaaPxXVbC0ktU5NIYTZMDOeiokdoyA3l4ugc3VimKY2P5E5wYewETTj4-tMx-VRBydK2HKy3cFA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عدالت برتر است یا بخشش؟
🔹
امام علی(ع) در پاسخ به برتری عدالت یا جود فرمود: عدالت هر چیز را در جای خود می‌نهد و قانونی همگانی است که جامعه را منظم و شکوفا می‌کند؛ اما جود فراتر از استحقاق و محدود به موارد خاص است؛ بنابراین عدالت به‌سبب فراگیری و نظم‌بخشی،…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/664698" target="_blank">📅 22:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004d499b44.mp4?token=bP3dO2yWrjhIlrrn5oqqXy6llt3nVp5dKhKtsyYYXXWR27BkNxotSM9y5_CNHjKNvFQundVA7PjKTmG1dusoeBVFFgzw4-NmHfwIBnB3UT_gI7-VfSnZXzgaPyMAqBvSMuYtA3cv1OLu9-ucs03DJuwPtc29kj4bR7JgB3Qj20dtn48YRrsiaejRd7-S7smWv6p2iDz0wFtbEG6AZBuaTDe1hLt5a8-e8EVTUJzR56ckyog2dfb1A0-OT4_KvGt53kAS-5ptGNs5hM94XqyGYkc3ZGtzQe_X5pz08esX4dyKtFby-reYzSQPe0r7AoPjoCDnyv0E_nwulLX-_wRW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004d499b44.mp4?token=bP3dO2yWrjhIlrrn5oqqXy6llt3nVp5dKhKtsyYYXXWR27BkNxotSM9y5_CNHjKNvFQundVA7PjKTmG1dusoeBVFFgzw4-NmHfwIBnB3UT_gI7-VfSnZXzgaPyMAqBvSMuYtA3cv1OLu9-ucs03DJuwPtc29kj4bR7JgB3Qj20dtn48YRrsiaejRd7-S7smWv6p2iDz0wFtbEG6AZBuaTDe1hLt5a8-e8EVTUJzR56ckyog2dfb1A0-OT4_KvGt53kAS-5ptGNs5hM94XqyGYkc3ZGtzQe_X5pz08esX4dyKtFby-reYzSQPe0r7AoPjoCDnyv0E_nwulLX-_wRW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: امکان ورود ساک یا کوله‌پشتی یا وسایل حجیم به داخل مصلی برای مراسم وداع با رهبر شهید وجود ندارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/664697" target="_blank">📅 22:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
نظرسنجی که تن نتانیاهو را لرزاند؛ ۹۲ درصد اسرائیلی‌ها ایران را پیروز جنگ می‌دانند
🔹
نظرسنجی منتشرشده از سوی الجزیره نشان می‌دهد ۹۲ درصد از پاسخ‌دهندگان، ایران را پیروز جنگ اخیر می‌دانند. همچنین ۸۲.۹ درصد معتقدند این جنگ امنیت اسرائیل را تضعیف کرده و ۵۶.۴ درصد عملکرد نظامی اسرائیل را «شکست‌خورده» یا «ضعیف» ارزیابی کرده‌اند. ۷۲.۵ درصد نیز به اظهارات بنیامین نتانیاهو درباره جنگ اعتماد ندارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/664696" target="_blank">📅 22:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664694">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c4e4404a.mp4?token=k8JqfpD0Nj__KatFoRUCwmuMnKNuOFafyhgj_fapwOO-Pttd5oIH20ydVh3jneEzl2Ocfgc3PFAF1RgRNu5dLne3M5u_plBCm765kbIvJ9h97HndSqV2qTRBVHEaeCnbGi4xNKE9QHc5M0PiHkA6hqBNIf-rRVdv_WkRzDXM4U07FKIk-q6MjBCGfrEaAaMe9WsK8Bh4GGghlwDpLSDJcf6e2Nai5OfrJu7smJ1w_j1jiBBvSGZjeCsxdBMgBhNA3Zoj99KNU08kmRZrT1ttLbHRGelduCfrhNB4n4z0hlPsxsYswwMFzTLPxahh16b_wTXjpPvOmyYbv88mGrpd4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c4e4404a.mp4?token=k8JqfpD0Nj__KatFoRUCwmuMnKNuOFafyhgj_fapwOO-Pttd5oIH20ydVh3jneEzl2Ocfgc3PFAF1RgRNu5dLne3M5u_plBCm765kbIvJ9h97HndSqV2qTRBVHEaeCnbGi4xNKE9QHc5M0PiHkA6hqBNIf-rRVdv_WkRzDXM4U07FKIk-q6MjBCGfrEaAaMe9WsK8Bh4GGghlwDpLSDJcf6e2Nai5OfrJu7smJ1w_j1jiBBvSGZjeCsxdBMgBhNA3Zoj99KNU08kmRZrT1ttLbHRGelduCfrhNB4n4z0hlPsxsYswwMFzTLPxahh16b_wTXjpPvOmyYbv88mGrpd4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: مین‌زدایی تنگه هرمز فقط توسط ایران انجام می‌شود  معاون وزیر خارجه:
🔹
ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند.
🔹
طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام می‌شود و نه هیچ کشور دیگری، اصولا اجازه…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/664694" target="_blank">📅 21:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664693">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ad4624ca.mp4?token=u0qq9hiWa2Tbstp4OHQ28VkDqpB0X8QR4B5YEggn8tWvlEJy_MRsNO90hfW8VapOO8rEqPddp2qfiHy-tRX6upCC5LnOvGNjEyhHngq4xSjVD5VsbFbg8OOLFAN3SL-4cG3KCUbUYuk6W3E8rviiJbI322ryWWo_rLsOL9kVayJgOA4O33meJXtVt1eGYT0bPIXLnRDd-8OGfjVXyfYZA63bFXWuhGQgRMS795muGi5pcU4Rjjv8fTwRE8yWXEq2fViHGOspJvbKRFvRiZyhU8zWS2DgQej3kd2ydSvl6sg_cMvpQrGHTX1eEokgiC8DCFkUT_8ImBJ93j4yf57fHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ad4624ca.mp4?token=u0qq9hiWa2Tbstp4OHQ28VkDqpB0X8QR4B5YEggn8tWvlEJy_MRsNO90hfW8VapOO8rEqPddp2qfiHy-tRX6upCC5LnOvGNjEyhHngq4xSjVD5VsbFbg8OOLFAN3SL-4cG3KCUbUYuk6W3E8rviiJbI322ryWWo_rLsOL9kVayJgOA4O33meJXtVt1eGYT0bPIXLnRDd-8OGfjVXyfYZA63bFXWuhGQgRMS795muGi5pcU4Rjjv8fTwRE8yWXEq2fViHGOspJvbKRFvRiZyhU8zWS2DgQej3kd2ydSvl6sg_cMvpQrGHTX1eEokgiC8DCFkUT_8ImBJ93j4yf57fHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل تساوی برزیل به ژاپن توسط کاسمیرو
🇯🇵
1️⃣
🏆
1️⃣
🇧🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/664693" target="_blank">📅 21:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664692">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: درآمد حدود ۴ میلیارد دلاری از نفت، برای ثبات در بازار ارز کافی نیست
جعفر قادری، عضو کمیسیون اقتصادی در
#گفتگو
با خبرفوری:
🔹
پول حاصل از فروش نفت کاملاً در اختیار دولت است و به حساب بانک مرکزی واریز می‌شود و هر جا که دولت بخواهد می‌تواند هزینه کند.
🔹
مبلغ فروش نفت که حدود ۵۰ میلیون بشکه با احتساب هر بشکه ۸۰ دلار است، درآمدی حدود ۴ میلیارد دلاری دارد و برای ایجاد ثبات کامل در بازار ارز کافی نیست.
🔹
تورم داخلی حدود هفتاد تا هشتاد درصد تأثیر مستقیم بر قیمت کالاها دارد و حتی اگر نرخ ارز کاهش یابد، تورم داخلی همچنان قیمت‌ها را بالا نگه می‌دارد. با فروش تدریجی نفت به تدریج قیمت‌ها ثبات پیدا خواهند کرد مگر اینکه مشکل خاصی پیش بیاید.
@TV_Fori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/664692" target="_blank">📅 21:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664691">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
غریب‌آبادی: مین‌زدایی تنگه هرمز فقط توسط ایران انجام می‌شود  معاون وزیر خارجه:
🔹
ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند.
🔹
طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام می‌شود و نه هیچ کشور دیگری، اصولا اجازه…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/664691" target="_blank">📅 21:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664690">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
تروریست‌های آمریکایی صهیونی یک خانواده را در سراوان به گلوله بستند
🔹
یک خودروی شخصی حامل اعضای یک خانواده در حال تردد در شهرستان سراوان هدف تیراندازی افراد مسلح مزدور دشمن قرار گرفت.
🔹
این حمله توسط گروهک تروریستی وابسته به رژیم صهیونیستی و آمریکا انجام شده است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/664690" target="_blank">📅 21:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664689">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpbjrwX0ci-wAnzaY-EGYFhV-soBuOBnNoeWuzuiAK2YCRWEcAukGTrcStRb6I5R2ulj4TQP47qx9lS7x5iNgVhAG0V6qJlkDJ-xJvvYgryx3LxVFWxWqbI2xDTqN6iCRVEupF3b0TjUvrTcSj9lifkewP6d7WGc1mXmGG3DCOYYg9TQBMt-_zH2a_Oz4VhzMf7Ct8oCtz3LeUlkHDyXU5u2Nbr8RnkXcpEqG9vq7bTKRSv_aMhxVWrhQbD2kSv3b2h79IubRboxndW_gRR4JQbI8ZAtquzxZMmaXKhG4Sr1ZiI6HHn8PI0Lc9cEFepBkk_-tqIG6uy0Lf3fifRUqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پخش زنده مسابقات جام جهانی ۲۰۲۶ در آیگپ
🔹
همزمان با برگزاری رقابت‌های جام جهانی، کاربران آیگپ می‌توانند از طریق بخش «خدمات» و گزینه «پخش زنده جام جهانی» مسابقات را به‌صورت زنده و تنها با تلفن همراه خود تماشا کنند.
جزئیات بیشتر را در سایت خبرفوری بخوانید:
https://www.khabarfoori.com/fa/tiny/news-3226605</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/664689" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664688">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
غریب‌آبادی: مین‌زدایی تنگه هرمز فقط توسط ایران انجام می‌شود  معاون وزیر خارجه:
🔹
ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند.
🔹
طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام می‌شود و نه هیچ کشور دیگری، اصولا اجازه…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/664688" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664687">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دو منطق آمریکا و اسرائیل در جنگ با ایران؛ یکی دنبال امتیاز است و دیگری پایان!
🔹
اگر تاریخ جنگ‌ها را با نگاهی عمیق‌تر بررسی کنیم، متوجه می‌شویم که بسیاری از آن‌ها فقط نبرد نظامی نیستند؛ بلکه نبردی بر سر اقتصاد، منافع و قدرت‌اند.
🔹
بسیاری از تحلیلگران معتقدند بخش قابل‌توجهی از جنگ‌های مدرن را می‌توان با منطق اقتصادی توضیح داد. در این الگو، هدف اصلی نابودی طرف مقابل نیست، بلکه افزایش هزینه‌ها تا جایی است که او رفتار خود را تغییر دهد.
🔹
جنگ در اینجا ابزاری برای چانه‌زنی است و وقتی هزینه‌ها از منافع بیشتر شود، مذاکره دوباره به گزینه اصلی تبدیل می‌شود.
🔹
اما همه جنگ‌ها از این منطق پیروی نمی‌کنند. برخی درگیری‌ها ماهیتی ایدئولوژیک دارند، جایی که مسئله فقط کسب امتیاز نیست، بلکه تقابل بر سر هویت، نفوذ و نظم منطقه‌ای است. در چنین جنگ‌هایی، تحمل هزینه بسیار بالاتر است و پایان آن صرفاً با یک توافق سیاسی رقم نمی‌خورد.
🔹
بسیاری از ناظران معتقدند تقابل اخیر ایران، آمریکا و اسرائیل، ترکیبی از همین دو منطق بود. آمریکا عمدتاً با رویکرد فشار برای تغییر رفتار ایران در موضوعاتی مانند برنامه هسته‌ای و سیاست‌های منطقه‌ای وارد میدان شد؛ رویکردی که در آن محاسبه سود و هزینه نقش تعیین‌کننده دارد.
🔹
در مقابل، نگاه اسرائیل از دید برخی تحلیلگران، امنیتی‌تر و ایدئولوژیک‌تر بود، نگاهی که ایران را صرفاً یک رقیب سیاسی نمی‌بیند، بلکه آن را چالشی راهبردی برای آینده خود تلقی می‌کند.
🔹
در چنین شرایطی، صرف‌نظر از روایت‌های سیاسی، آنچه قابل توجه است این است که ایران توانست در برابر هم‌زمانی فشارهای نظامی، سیاسی و اقتصادی مقاومت کند و مانع از تحقق بسیاری از اهداف اعلام‌شده طرف مقابل شود.
🔹
به همین دلیل، از نگاه بخشی از تحلیلگران، نتیجه این تقابل را نمی‌توان صرفاً «شکست ایران» توصیف کرد، بلکه باید آن را نبردی دانست که موازنه قدرت و معادلات منطقه‌ای را وارد مرحله‌ای تازه کرد../خبرفوری
#سرمقاله
@TV_Fori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/664687" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664686">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
بانک مرکزی: انتخاب شرکت برای رفع اختلال ۴ بانک، بر عهده خود بانک‌هاست و ما نقشی نداشتیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/664686" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664685">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
کدام بخش‌ها در جنگ بیشترین ضرر را کردند؟
🔹
جزئیات تازه از رشد اقتصادی نشان می‌دهد بخش‌هایی که بیشترین آسیب را از جنگ و نااطمینانی‌های اقتصادی دیده‌اند، بیشترین افت را نیز تجربه کرده‌اند.
🔹
در زمستان ۱۴۰۴، حمل‌ونقل با ۹.۶ درصد، عمده‌فروشی، خرده‌فروشی، هتل و رستوران با ۵.۸ درصد و صنعت با ۴.۲ درصد کاهش روبه‌رو شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/664685" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664684">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم
🔹
اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیئت ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله  بند ۱۱ انجام می‌شود ندارد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/664684" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664683">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYffmTtGKALVdjI_S96596-Okgk3NpFJfMV_tFlC50xZvrDHv2iXZ5fp5Hk4REizxoFJyZC7OtAWaoc1uq4gXYM6mY6IpZxcBa8r4CKUkLcBqJLV-csSOauEZ_vfyYMKFxjKbVUHwENjWoBZjOBRiTcqQ7nNpGfnEsAnKsrczG1zZyZTvQPM7s4uE6JwDNdtVfKWKbe7x6b-s6TgQNKwp_fWZWV7-370W2MTxrKIwzhrNXhPWi8jcC_3wdPJRAxvj5w2gg3FVOwE76Il2KGLqzpKHBQITnsUHrXRLwp6w90Neyg9fkx0b3AEbrzHjKwP94CGE4d8jAqjqHypjJFAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی احترام به اعتقادات، از اسپانسر هم مهم‌تر می‌شود
🔹
جایزه بهترین بازیکن جام جهانی با حمایت برند آبجوی Michelob Ultra اهدا می‌شود؛ اما اگر برنده یک بازیکن مسلمان باشد، برای احترام به باورهای دینی او، نسخه‌ای از جام بدون لوگوی این برند الکلی به او تقدیم می‌شود.
🔹
حرکتی که نشان می‌دهد گاهی احترام به عقاید، فراتر از قراردادهای تبلیغاتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/664683" target="_blank">📅 21:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664682">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0GvxGPpy1HH9ze8AcO-f9X-ATOLnkgN-9FT6Cz9Dn_PpNzCjOSXBqsR6B3eWnxTOhK8A2ceAR748zq1YzXdnMHn5wCkGuQVym7vDJPBtWJQiHRtaXm1ZznFV0JqZYPmySIH-xAtacAxMsyjJGT8FdPc7LnSnv1Sn4aw6JE0XdjQRH54pYDdzuF0mt0kPdWDSEHoES5FO5BTfZMzufAqJt_yh7PO2Y1kYIa7pC5MLv1gk9gBcn_896h998vc2saipV1t538wB1S8DZi_jDAmn8UHGqJyv-UG3_cA1CQngyRI868gRaLjdsGmxBp5hlOoGpozyLMDGGaSC9mJD6BTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تماشاگران ویژه بازی برزیل با ژاپن
🔹
رونالدینیو، رونالدو، روبرتو کارلوس، ببتو و جیمی باتلر ستاره بسکتبال NBA
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664682" target="_blank">📅 21:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664681">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27739e3f1c.mp4?token=WmDdmi-6aLek9gQp0I7C8-RvYVeuORRIYICIld_J3NQYhFoHX3l_KiemZDAfywmNGIxmcCTeQXS-goFx6TEgGrMqrN_OxPQrOB3n_wbvZn6c2S10UXU181PRKVTmYYNSWqG6gE4JhfSbhMCZGDj9r_5klpsP5FOl7wpQADHVgspcINT0ricYbBeycr7XPty9V8FvBNsjRT7-TaMyylN9QMDj1Mcczs0f1jpIlfsLIgtQNAW1JEIBswqOicrw8TexZlTQPNCwVnE6N0t7kx56iy5nXfnVijfflb4vJmMQ-rE0oo8yCnJxHLwGY-RERwkj5_xjmYa8N6odIEQIwwpL0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27739e3f1c.mp4?token=WmDdmi-6aLek9gQp0I7C8-RvYVeuORRIYICIld_J3NQYhFoHX3l_KiemZDAfywmNGIxmcCTeQXS-goFx6TEgGrMqrN_OxPQrOB3n_wbvZn6c2S10UXU181PRKVTmYYNSWqG6gE4JhfSbhMCZGDj9r_5klpsP5FOl7wpQADHVgspcINT0ricYbBeycr7XPty9V8FvBNsjRT7-TaMyylN9QMDj1Mcczs0f1jpIlfsLIgtQNAW1JEIBswqOicrw8TexZlTQPNCwVnE6N0t7kx56iy5nXfnVijfflb4vJmMQ-rE0oo8yCnJxHLwGY-RERwkj5_xjmYa8N6odIEQIwwpL0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تذکر پزشکیان به مصرف غیراستاندارد برق در سازمان استاندارد
🔹
در بازدید رئیس‌جمهور از سازمان ملی استاندارد چه گذشت؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/664681" target="_blank">📅 21:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664680">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/659dd30758.mp4?token=eQH1ypIHXbJgl_TTOmldIyNEwoenM-VphMlrTrDe7ajlga9bfNxjXoTj8aMx1ZXX0_OYcWCMezZxitMx2SJmw5WTQZkjZ11mHXxBfBuV1vWBZ5RjbSV6XHCj3ov9iQnd_-3VRDlq4Z02l1n3C5aqdO-pysl2GjRljdpGLdvlb0MgSi1oHTN__HBO-FWYqeg2bmz4Esj1KqP1oUo8msy47wGjl2GiyU7AUP6LZWgJWbp65bBsTWqVZkfPmaWiXKlC181MZ3OXEfofxjBoxbFkFGV6OPS9VslUf5J0nek6I1d6kC8-iZ3AjJt6suxeoDnr0YDk0AG-Mwgxx7Jnoftzd4T7Qk_dYES6FDl78FuLD0sOHNPieBgSU33su5wt423Fhf4aONGCJJtFLiqhIu9nKo3K2miWxXMpqRTbJz43Ui3cZgl-bxUvjfrzDxCD7xTQ92hhIY0cnwdAz1zA0r2IhMmQVVySbs_2AhXMNrib1RBck8Rk6n7OrivsCDvmyOaqH-W9hUG-gWbiCwL4OHm9xCdlckzgpCBWBrO_qlp9VBWxXVCNI6PFAV_cRosJ-Kkqmoj_q9Dv33cNoSJsceWvM0j8oO_6yEAgV5AXdTZ7GI-RNfbtfMz2hmEtEoTsvZnfkty6mfNwLv9cO7uxFOb1xUBXRak18Ka0-qiD7lrQHMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/659dd30758.mp4?token=eQH1ypIHXbJgl_TTOmldIyNEwoenM-VphMlrTrDe7ajlga9bfNxjXoTj8aMx1ZXX0_OYcWCMezZxitMx2SJmw5WTQZkjZ11mHXxBfBuV1vWBZ5RjbSV6XHCj3ov9iQnd_-3VRDlq4Z02l1n3C5aqdO-pysl2GjRljdpGLdvlb0MgSi1oHTN__HBO-FWYqeg2bmz4Esj1KqP1oUo8msy47wGjl2GiyU7AUP6LZWgJWbp65bBsTWqVZkfPmaWiXKlC181MZ3OXEfofxjBoxbFkFGV6OPS9VslUf5J0nek6I1d6kC8-iZ3AjJt6suxeoDnr0YDk0AG-Mwgxx7Jnoftzd4T7Qk_dYES6FDl78FuLD0sOHNPieBgSU33su5wt423Fhf4aONGCJJtFLiqhIu9nKo3K2miWxXMpqRTbJz43Ui3cZgl-bxUvjfrzDxCD7xTQ92hhIY0cnwdAz1zA0r2IhMmQVVySbs_2AhXMNrib1RBck8Rk6n7OrivsCDvmyOaqH-W9hUG-gWbiCwL4OHm9xCdlckzgpCBWBrO_qlp9VBWxXVCNI6PFAV_cRosJ-Kkqmoj_q9Dv33cNoSJsceWvM0j8oO_6yEAgV5AXdTZ7GI-RNfbtfMz2hmEtEoTsvZnfkty6mfNwLv9cO7uxFOb1xUBXRak18Ka0-qiD7lrQHMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماری که واقعیت تلخ تیم ملی را در جام‌جهانی فاش می‌کند
🔹
هرچند به ظاهر بدشانسی یکی از مهمترین عوامل صعود نکردن تیم ملی به دور بعدی جام‌جهانی بود اما برخی آمارهایی که در این ویدئو می‌بیند پرده از یک واقعیت تلخ برداشته است.
@TV_Fori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/664680" target="_blank">📅 21:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664678">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978f228826.mp4?token=gtNo0D3ggxsz9zkqOkzHsjQzNllGX6xhmchNoj5aXcUrDTQtIClpkts2h1YaXjfF41qmrQ8Oju8MS6jtp4Hxph51JQj77T5qE9ZUxozXr2BIlhqGGDHO_6AViYLyQiMINNBYHmC8VGFvknP-UEz6qwzb2Gpcd8qbEcD2HVHOtdMuTsmIW98BTLPeERvjtwuYal39TDr-0cyTJgp9bDEsKP8g0DgKhvPiyc-O6y0Zkv6iGhKnfWGqvMk5WIwtXMkkuH7G1HG-OsODgvFAmdPsFq24POWFSfEqUXQShacliV7h_rD8xHJe5L0TXuhVrho0XRBz2z3l0u__EputemOqZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978f228826.mp4?token=gtNo0D3ggxsz9zkqOkzHsjQzNllGX6xhmchNoj5aXcUrDTQtIClpkts2h1YaXjfF41qmrQ8Oju8MS6jtp4Hxph51JQj77T5qE9ZUxozXr2BIlhqGGDHO_6AViYLyQiMINNBYHmC8VGFvknP-UEz6qwzb2Gpcd8qbEcD2HVHOtdMuTsmIW98BTLPeERvjtwuYal39TDr-0cyTJgp9bDEsKP8g0DgKhvPiyc-O6y0Zkv6iGhKnfWGqvMk5WIwtXMkkuH7G1HG-OsODgvFAmdPsFq24POWFSfEqUXQShacliV7h_rD8xHJe5L0TXuhVrho0XRBz2z3l0u__EputemOqZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوت دیدنی؛ گل اول ژاپن توسط سانو در دقیقه ۲۹
🇯🇵
1️⃣
🏆
0️⃣
🇧🇷
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/664678" target="_blank">📅 21:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664677">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI-XgAnt32ITg6s7yceNTaqgPIU6PBi67fc1EWUlslhDXAqbT7XapFOOHvMbqYYFxYKElcNmH2EHAYVWh51iiIx2bGBo1BEOKuZlaEoEpXdgNb_jm2-EKlVLfELtj-5VDUiPJ_6EW5v3coSNX0md_P-PqVCqhZE96JyKyLbphx76yrmFz_HQNKY3JcUUwWHggHSaDZS6OXxFLneq0xJwq1jS9ZcKmwFZjGwHPJnUEAELgTEgGEJ2HPsVI0O8bR1CYJPogx6WvfQ_BP9bG-pO1Y7_V8IEXPRZaF740ieU6Tw6FH9cM4BWxwIIfcWieNwByAekAY-Q-MUypaG8NS243g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: مارتی سوپریم ۲۰۲۵| (Marty Supreme)
🔹
ژانر: کمدی سیاه، ورزشی
🔹
امتیاز (IMDb): ۷.۷
🔹
خلاصه: تیموتی شالامی در نقش جوانی جاه‌طلب ظاهر می‌شود که برای فتح دنیای پینگ‌پنگ حرفه‌ای، مرز میان نبوغ، وسواس، شهرت و جاه‌طلبی را درمی‌نوردد. «مارتی سوپریم»…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/664677" target="_blank">📅 21:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664676">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: هنوز وارد مرحلۀ مذاکره برای توافق نهایی نشده‌ایم
🔹
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آن‌هاست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/664676" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664675">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/664675" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664674">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های مسدودشده ایران، نیز فرآیند اجرایی‎‌شدن آن درحال پیگیری است.
🔹
در این چارچوب، همین هفته هیئتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/664674" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664673">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664673" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664672">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ae4c4e4d.mp4?token=iMsGHXQdLAli6DUIQjoyMHvUVibO_Ppd5RHakcL7-6e6eAF17_k1rs0N7LcUUvElcYAFJ6G0LWS7ruGlRT0ia3RK_0vqUy6gC0zypRGs6y8B_II94jYBedwvIq2xLPsS_kPzV4-B_6IU4O3E0g2calr8eQGhJIcY4KREk_oaWqHX6aNVbThTwFlGkJKn2Yzs_jWjkSAFDWWsj2F5umpLaAoZyNaCYhBj-R4BbJqys7HOCmYV3lf1RrGhKycPKY3RfZ6Q52gqiISx1uDvqHl5HL95Is5694SwhGkTPews3XQT3SCm8BDTtjBCbcoZDnGJJBlIWpC5a_u3cxmMXLNfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ae4c4e4d.mp4?token=iMsGHXQdLAli6DUIQjoyMHvUVibO_Ppd5RHakcL7-6e6eAF17_k1rs0N7LcUUvElcYAFJ6G0LWS7ruGlRT0ia3RK_0vqUy6gC0zypRGs6y8B_II94jYBedwvIq2xLPsS_kPzV4-B_6IU4O3E0g2calr8eQGhJIcY4KREk_oaWqHX6aNVbThTwFlGkJKn2Yzs_jWjkSAFDWWsj2F5umpLaAoZyNaCYhBj-R4BbJqys7HOCmYV3lf1RrGhKycPKY3RfZ6Q52gqiISx1uDvqHl5HL95Is5694SwhGkTPews3XQT3SCm8BDTtjBCbcoZDnGJJBlIWpC5a_u3cxmMXLNfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار خرس از گربه که در شبکه‌های مجازی پر بازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/664672" target="_blank">📅 20:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664671">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
عضو رسانه‌ای تیم مذاکره‌کننده: تا الان هیچ مذاکرۀ هسته‌ای با آمریکا انجام نشده و تا عملی‌شدن شروط ایران هم مذاکره‌ای دربارۀ موضوعات هسته‌ای انجام نمی‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664671" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664670">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyt4SePEYe7MGg34q5Ph_NkMLBj_uYwG1gT3UNUma7coYIZ6FjDywt7TJIC02peTljUn2j-ECC9JUUOThmKyEmG--HJ74m7sPtMuaNQzFr_M7r2Aec1JKIgBRouPA54zA5Tfq8mpMm4XK0saRxTUOnhr92m_YTmKAccnRJSceo1mETrhWHyPAFXM8Rc--T63NUNsZzymSDKak1UgD6Y_u_S4W4sX8sWJHkdmkSBSCFod9ElKEyhel1bQ4HeFCZA-ikhoAW0AAQbiSKKkfhfW9mkwkpIse9qqUFA9sw7IlJBC9IHBXqzYaX0H3i6y7DeJBWtodP3gvIN3dfA0EqJ8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینوستوران از مرز ۱۰۰۰ میلیارد تومان تأمین مالی عبور کرد
🔹
اینوستوران به عنوان بازوی تامین مالی جمعی گروه مالی پاسارگاد، با عبور از مرز هزار میلیارد تومان تأمین مالی، به یکی از بازیگران اثرگذار حوزه تأمین مالی جمعی کشور تبدیل شده است.
🔹
اینوستوران تاکنون ۵۰ طرح را تأمین مالی کرده که ۳۴ درصد آن‌ها در حوزه‌های دارو، سلامت و امنیت غذایی بوده‌اند. همچنین ۵۴ درصد از مبلغ سرمایه‌گذاری‌ در طرح‌های این سکو به طرح‌های دانش‌بنیان اختصاص داشته است.
🔹
در طول مدت فعالیت اینوستوران تاکنون، ۶۸۱۴ نفر در طرح‌های این سکو سرمایه‌گذاری کرده‌اند که ۲۷۶۲ سرمایه‌گذار منحصربه‌فرد حقیقی و ۷۵ سرمایه‌گذار منحصربه‌فرد حقوقی در بین‌شان بوده است.
🔹
اینوستوران با رویکرد رشد جمعی در تلاش است با توسعه تأمین مالی جمعی، زمینه رشد کسب‌وکارها و شرکت‌های مولد و موثر کشور را فراهم کرده و در مسیر رشد و توسعه اقتصاد کشور نقش‌آفرینی کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/664670" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664666">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
روایتی تکان‌دهنده از تجربه نزدیک به مرگ؛ از دیدن عذاب گناهکاران تا چشیدن طعم میوه‌های بهشتی
🔹
00:06:00 حسابرسی نیکی کردن و شیطنت‌های دوران کودکی
🔹
00:12:40 چشیدن طعم میوه بهشتی، مانع خوردن میوه دنیایی شده است
🔹
00:24:00 اطلاع از زمان فوت دوست در کما
🔹
00:29:00 سفارش به ادا کردن حق دیگران
🔹
00:35:00 دعای رفتگان در حق بازماندگان
🔹
00:49:20  بخشش اعمال در حق‌الله و برپایی عدالت در حق‌الناس
🔹
01:05:00 کسب معرفت از محضر اهل بیت در برزخ
🔹
قسمت بیست‌وپنجم (طعم میوه)، فصل چهارم
🔹
#تجربه‌گر
: عبدالکریم حاجی‌زاده
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/664666" target="_blank">📅 20:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664665">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyncNvNjnkBg2GoNvYB_CeVal4GNBv2kSOX0F0qzEAsdgXgcRnB71BP2w36dNTKfCDDyfyQa85OByTNB_F17IOuYZ5z5yBWw8CzrJBgnb-xBLOZYJwCMOjyO_VshDF3RMDMb_VlTGpWH6z0SvUdpwe5Yu_fcWUFIQKQZKmmAbWFlVruCs7JZuVZv1sPM3_leKeaICaBqwmc8MwyzWdU9t5ZovxC-ZgAvqnhlRToepUyT0mAMJ2Zfy9wIVOHd2f7pudObyIQjQgC1Chlef6JGRfvsd_FNjR5BSiDXSz15ET5M_CyGAQV7ZFULMgIMjBcnlZHtyLA1cRJJS-Uy1Dm0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: مین‌زدایی تنگه هرمز فقط توسط ایران انجام می‌شود
معاون وزیر خارجه:
🔹
ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند.
🔹
طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام می‌شود و نه هیچ کشور دیگری، اصولا اجازه چنین کاری را هم نمی‌دهیم.
🔹
شرایط حساس و پیچیده است. توصیه اکید میکنیم فرانسه آن را با تحریکاتش پیچیده تر نکند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/664665" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
