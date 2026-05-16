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
<img src="https://cdn4.telesco.pe/file/EhWIzfUr9d2UZB7iUIN3URvZPXaewW8NaGdsiYzKrnLAWh9iLP1qaxcCL_pjcWeAW2oiSXP29ydfoReJLSifs-JR9zCkeIxANVLqYYqvFxQSSu6wwEkSqLupJPL0VDzwgRi2ir58EBmv9emOqgtMMI7DW53s7PU0GPpd4zB-zsvt6j7KxgcvUeNQG1OTekW-y7eMRT_FqIDnsmJvLNVAZnAZ3Deuz6eWWO0lkJHLXWAEU5M2J85Twq9HPksEOeXSrj8Ht5dp1ip6zne6F2Sb3-Sw20S2gtTrfbXIXRhUyniVbZWyo5qeCQZ4inw8EEfuR0EjtJQtd3QdZTZwnG_OIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 60.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 09:08:48</div>
<hr>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 596 · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=sP10t5iaXXN7EMGx9JjHfUa6eqGT0Ec1WPRTRX9SKugcZ5Hqq7jO_44nYl3pPq-EDD-uDJox4iLdet_ntKETxNM9IKigrdA8imvOVMX-ns0gB0m05742y1EXHDRsFTVB9uFjizMoKMb_xWJNKNqDstwrbQqntv-Cnim7-7GUtZnEDjohZufCX9hvTPmfsu8EqNxVGmimpd4TOAXlsjfqXB3vV4DUvC_4cd12ONvI6F8RdV3AFYiLCmaShR5qaQ5VB8irNj5xDS22BCCXQtGY1gwnMJyKDOCz6NrOgfCLBBPcmhjypxebvOW0VJt-pGNhJeJdsnfCMdZy9IcFIevpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=sP10t5iaXXN7EMGx9JjHfUa6eqGT0Ec1WPRTRX9SKugcZ5Hqq7jO_44nYl3pPq-EDD-uDJox4iLdet_ntKETxNM9IKigrdA8imvOVMX-ns0gB0m05742y1EXHDRsFTVB9uFjizMoKMb_xWJNKNqDstwrbQqntv-Cnim7-7GUtZnEDjohZufCX9hvTPmfsu8EqNxVGmimpd4TOAXlsjfqXB3vV4DUvC_4cd12ONvI6F8RdV3AFYiLCmaShR5qaQ5VB8irNj5xDS22BCCXQtGY1gwnMJyKDOCz6NrOgfCLBBPcmhjypxebvOW0VJt-pGNhJeJdsnfCMdZy9IcFIevpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۰ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۰ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OptsqDEuvyGVnFCgChF7KbOVPBzImpFdbpS2myD2wC1Sf9aTwpofDcduh8RfeLToaMcUw60fORtTyWXgL9UgJkniTGkoOE4HAI1Xpk5EE70JrFRDcwnDHar0v4FsXqDKqkh5-gFVBHqLwv6fETOREZQrKtWeIawNEdeQfgv2MUAQUA4jfAzd25YKjUallo8kVjZiot7xwL4OjNscadJtXkj7dnu9SwtXB0CxC8a3kI0pxLh_SOswkQ0UIR5cLf31UZEHEOwUcftcLiaWGmXdt-HsGUGBJSi6n9XL13BhDkmKViG-RYboKu1xh_et8lRVSqE1A5kIyNtyv0wXJcphKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8dNkK1szn1BNp25MrwT3wYm54cVhCBAxZtf0W7_M44izNpHgyHjuEcZJ0Mk3UcAQJCbB01HqmshDdtuIigAP1I7F4YSqquDfmBlGFqXO2UyPUKpxkldjY7wVgDxCrkRwfnObu65H7DVBw4vyXWNpDTlon6BZOx6ahVcTaq2_qpFTlMdfp3g6P3989B80aHyZ_fqlnstTAcC4EZo1H_5fiqDcbkbvEZ3NfuL1EpQUHPHN4O6lir0Oy8cz0d6F2Xcuugu8c23XX7oi0p_Co64kItMzznb6v_F2fZMMGNDrpXwiRUiAO0LVXik_uIogz3RdbOmaaErm9Oi3yU8QZJz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmxAcD4X6Yxk_l9zHaVoAmdIIXpORSZdJTRWyK931qDNqMFldSFp-a_llTMMWNld8ToI-4j0jxbR9QGnsokwwM_IC3UL7qe_ydsEu-wlA1-NrxdJc8X0-2T-6OxmPEbYwjUwP2Jo5hB7_0IuOopjGVBwqAzyx7IFfQC330AeYE4Shvx8mE1JSP2X9RWLYyjuGzyvejwfScbpHucMDfSXAboZIzILjlKr6k7n-jRZHAjD_rO_fSDpi3a9exriMAUyjGJ7Wsofia_qZFr-lXyQh5rUrfCu3jlLNQ4aCQfQlo7760raCekyFqEzLYaL7WWx3Fv8Q5VDk4yiBluG0pDv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqpYtXr54RW4RV9sWQsqxRf9YfEAgSwWx_lbPmHUzndkMXB44VYMWZQVMkAKJeBxD1Bc9Lhk0vf0nATb4Uuh2VeVwrrM2OAmiJgh0WtbM9Rk50V12TTW8AmoB0fwPPzkNePIU-FV89Bg_2SiU9sSM8m3rNr_qq2nrato8D13vLIlNLalW09A87APJhA9gdLt7pp2MuT_WeslJv_8Cg8RP1y4GxPCkNuixNeCWIiEHbL_fcYPfMmEm6nXhv6U7NS0BPoXVirmrWi-GteNMZx0AOZUfwc1eCbgF1EEhvFDlwDck89x4dcFlw9Zh9qJtVGl2nh5cD4fB5QVrJkFM5KcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=FXRalYcCLPysr8u2HnaRlRvpLP3XklWzlXt-N71dKhFK_663MPFK-wIKv7NEPodQH2GS0iInxqf1aabgVrZDMocNZtKYEu3W_lUxLteinsN8pgXBT8XdVmDxCV25CWiXCB1uxlJYQVM-uYmF1Ie3XGGg9PM_4n9zDyQwsEcrn0bXPqwrFw4HJfVsvO4in98OSCtjlquPUknIYrIVTkaJqwf8gT4OAySquI9-L1ujQ6wIOGtmS0jwhEfcopRb_GfstFgfL-KD0OEzgvAGq064u_895O9_qItgZgAdy8G63GAmsP12TbltF9I_GRib3_xEnsd2_H4TYSiPyKJB6Lx48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=FXRalYcCLPysr8u2HnaRlRvpLP3XklWzlXt-N71dKhFK_663MPFK-wIKv7NEPodQH2GS0iInxqf1aabgVrZDMocNZtKYEu3W_lUxLteinsN8pgXBT8XdVmDxCV25CWiXCB1uxlJYQVM-uYmF1Ie3XGGg9PM_4n9zDyQwsEcrn0bXPqwrFw4HJfVsvO4in98OSCtjlquPUknIYrIVTkaJqwf8gT4OAySquI9-L1ujQ6wIOGtmS0jwhEfcopRb_GfstFgfL-KD0OEzgvAGq064u_895O9_qItgZgAdy8G63GAmsP12TbltF9I_GRib3_xEnsd2_H4TYSiPyKJB6Lx48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdeRry5iNelidiegNTjVvoa-vI7TiEeZYLJZFlp2uhtuD_dRk_DeRB9K3lL8GHIvME1yPft0QJNG54J-vhKdevUyRU0egDJX2NaR_-s26hibT6ZLq0RebT6J4naYb7fedlTuwWNwYKDVmI2TWQnDy_x5fHsJB1cWAAn3l7IekUROLLA1W41W1o2i7pN3cchAGw91JA5Oczrd7IeLnPou1yY-l0ybCEhA26f70iRpo-LQ6MCGf5StOvjZOnV9jGoDj3IJL9yyyPuXumaMr5br9dA8ZUQlkFJAimDESnoqC2wO9MmsIhQf2I0abYmwQQZmSdd0Gfzp_QnJcME5WNxQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzL27c0ZJAyH9J09xoQJRA3DAqFNwDIQGYGgyclv5W-SGCDIGQMg9l88CD4hHDT37W0QNcUBOu4hN_K2DBuJZavVj2LcirQcfWbCgrSgmgPLrI7LGZ--037vbQIFlp8NUmwI0HNrcQmVAjJK0gB98_pv3ZE4enNKLPP0I68T6imsThr2a-vo7Wa8kGPTEfcwaveg9PMuL4F_yrhBQMC472J6sywaHt1834zEtGDdvtrRlkSGHobT4HdZ6rDhuD_NrkWGNB4jbjmzZqAW65-J7jhYjDV_sVQnSWKsCxhVwBkfvH-rskEzESmF4vf9CPhwiZ0mCuWbEOb8IoVmweEFFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYjwVfVhpGtjbLQq1oSzgLnWtrkOUuOd0WC-tZa9dMRid8TFXmSqHJH56n4Pp2Tai1xJGenWMas8hswazOdr-G2xTCm9gKaF_APIFmEid550Rmk5fHJYpAnzB2UdDRzyURcYCljqtbTYpsKMrSCyl93pyoNL1PDwt10BQpgvRjX1C-kdYgnlvyshcb-wyyoL3e0gvR48E_R26yj-F29f1DJq9K4R2neT9w5_iYFQHm3FkbDOntNTx6v0NTkceCJioy7RUY_d7zMx2QEoj4t12_NOvb_0aFILRv0oJ2UiuWBJexg66T5ZVR4IfHvLLubeaAijvksCc_9FAtMUN802vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=oj2-RWxkgwHH8bzlXFgXFp1cqkllflcUjpaZigWgwbKQoFqB1ElmL0UePDZqz38B-TfhZokr9qDrD-vpxAm4OE8KAcAuG4LNCdhvft7htk1l90fnn8vc3kZMNwD5wRppKeqVl0CNqdN96S1LK9Z-nmPmIZMlTZKMNPFsmjXMPj_4h--lSsUKEnBiky8OddSmDhDvrd-aWJh-MFYXm0PJLV24tO0cYRwNeJIRfGBHiuU1mKZjKVnW4k7EFGphiFppzaP6uhtvmlDwFWDxnDBCDBGuxEupcyBNr3JFoowAQrLnkSdWMAl_21DruQ4R0VP89NzyROHYAYrBcKzwWxVSihXS_FRjVxXsYdqatIVW6kyzOGj8uDxPvm--EgdETAWsbRsSNPRjKsYpD89Lt3ZGdpCnzZ_ewEwCsfBKmwaST96bLaLfPFzddlpJg_2zbhtt6cwyJmn56j-XbqCzirMnvfAHmaG21GsN9SXGXoLEc05JTb_ndm4YpayUnHtQOtfiVjPtqJEXvmFRyXHHR5bghbRzpuy66PQwlYat928lUMpaZAslZEq4LgUXjCjDF6InJREE7wEhyX4BIkz_JoSkCLZBd9D_oiWVojr6TlqpFzJtJqePFf9ilp37fAu19XwLdvJubDxZHJEzV_GZCPJxBV-0MhZVZPXs1fQvH9EbJCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=oj2-RWxkgwHH8bzlXFgXFp1cqkllflcUjpaZigWgwbKQoFqB1ElmL0UePDZqz38B-TfhZokr9qDrD-vpxAm4OE8KAcAuG4LNCdhvft7htk1l90fnn8vc3kZMNwD5wRppKeqVl0CNqdN96S1LK9Z-nmPmIZMlTZKMNPFsmjXMPj_4h--lSsUKEnBiky8OddSmDhDvrd-aWJh-MFYXm0PJLV24tO0cYRwNeJIRfGBHiuU1mKZjKVnW4k7EFGphiFppzaP6uhtvmlDwFWDxnDBCDBGuxEupcyBNr3JFoowAQrLnkSdWMAl_21DruQ4R0VP89NzyROHYAYrBcKzwWxVSihXS_FRjVxXsYdqatIVW6kyzOGj8uDxPvm--EgdETAWsbRsSNPRjKsYpD89Lt3ZGdpCnzZ_ewEwCsfBKmwaST96bLaLfPFzddlpJg_2zbhtt6cwyJmn56j-XbqCzirMnvfAHmaG21GsN9SXGXoLEc05JTb_ndm4YpayUnHtQOtfiVjPtqJEXvmFRyXHHR5bghbRzpuy66PQwlYat928lUMpaZAslZEq4LgUXjCjDF6InJREE7wEhyX4BIkz_JoSkCLZBd9D_oiWVojr6TlqpFzJtJqePFf9ilp37fAu19XwLdvJubDxZHJEzV_GZCPJxBV-0MhZVZPXs1fQvH9EbJCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=LflsC3QuXxsvG1hWqeutYxbA0hwuL-e4GNgFcmYYapPpY3IqMSogN_4bEt6hf_CHMZQbY6wYK_xVbLnl-qz9v9LJZjzeqFG6FVDGwPrkzXOzbisRINK-6tpmnYGO358RWoo4DS-qLgb3W74QmbgFd-OnxG_qt3b5qDdulf_DoY2v8aHviXD8v_DjfVaohvp3d8OwNgy4hfqggu9lv7gromCB9jyTLjhAuVUhA4t0aG2ey8XawbtUT7Kg1FIrM14GXHa2pHTn4wAi-3zyBD8jkkDc5kxZ-syEd8A2fyO9j4DhXKhPBHSd9pIl1g5qh0fbRaxW137y0VvKApNmv426eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=LflsC3QuXxsvG1hWqeutYxbA0hwuL-e4GNgFcmYYapPpY3IqMSogN_4bEt6hf_CHMZQbY6wYK_xVbLnl-qz9v9LJZjzeqFG6FVDGwPrkzXOzbisRINK-6tpmnYGO358RWoo4DS-qLgb3W74QmbgFd-OnxG_qt3b5qDdulf_DoY2v8aHviXD8v_DjfVaohvp3d8OwNgy4hfqggu9lv7gromCB9jyTLjhAuVUhA4t0aG2ey8XawbtUT7Kg1FIrM14GXHa2pHTn4wAi-3zyBD8jkkDc5kxZ-syEd8A2fyO9j4DhXKhPBHSd9pIl1g5qh0fbRaxW137y0VvKApNmv426eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=CHAI_XN8UG9Yo1TC_nVi1ifZ2oiR8WAq6gX1KfpPYbqpjTzHQMSYI9J757GrzXG8IldeJhhtJPMvD5BUuPAddcOG9W8imhpPLJiC_dKQqZnuiRDANvMHLW5zqzcAfSjL9_Ev5wfzAxU5pvFjUduJJCrHsJuxUS6Sp-ZKkgO3ifBGAtA63yCpgV_7NaghLwoHDKKwGjAZi79_EajydTWlsKCq0YlRSY83GhYQWT6BgciDsg_eCyoEeBR62mejklHTwqxt4DKz8TNQRr-l9pBqcczswm9cAu74v0Mjk4cXW3VagIwRFyhtYSjyau5HubSMWx6UeyZNnsMpF0J4K_2p5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=CHAI_XN8UG9Yo1TC_nVi1ifZ2oiR8WAq6gX1KfpPYbqpjTzHQMSYI9J757GrzXG8IldeJhhtJPMvD5BUuPAddcOG9W8imhpPLJiC_dKQqZnuiRDANvMHLW5zqzcAfSjL9_Ev5wfzAxU5pvFjUduJJCrHsJuxUS6Sp-ZKkgO3ifBGAtA63yCpgV_7NaghLwoHDKKwGjAZi79_EajydTWlsKCq0YlRSY83GhYQWT6BgciDsg_eCyoEeBR62mejklHTwqxt4DKz8TNQRr-l9pBqcczswm9cAu74v0Mjk4cXW3VagIwRFyhtYSjyau5HubSMWx6UeyZNnsMpF0J4K_2p5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=CMIf_Th3a8hKk4eRMpkNlTW2zumSTLf08iahw4qaMjn690lL27OucSiYRF7LdFxdEUrzc4hwHvxauc6o4TRCk9bkB6isL6GqjNnvBXzZ7li4DLqBlE76yqlCsOS9risvcN_L2WYC3OIUPWNhBRcfGmLw82FZbjcS_Xs6HPuGyDg_pHNDzQ7pqcSN1mTmK9Qtupo0xdnw-ZJudbQj9fGRFRJ14AY6blGc_3k25m1a0pCwqyRK70tTWjqU-FU3ONEvU4Hlw-Kgm-mIY74ZvHrPgDpGEOgqNw-GCbpDPkCuolQatE7UobI73KQpMIu3ZeUvc9XsPEcBM7YK4dObOUPM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=CMIf_Th3a8hKk4eRMpkNlTW2zumSTLf08iahw4qaMjn690lL27OucSiYRF7LdFxdEUrzc4hwHvxauc6o4TRCk9bkB6isL6GqjNnvBXzZ7li4DLqBlE76yqlCsOS9risvcN_L2WYC3OIUPWNhBRcfGmLw82FZbjcS_Xs6HPuGyDg_pHNDzQ7pqcSN1mTmK9Qtupo0xdnw-ZJudbQj9fGRFRJ14AY6blGc_3k25m1a0pCwqyRK70tTWjqU-FU3ONEvU4Hlw-Kgm-mIY74ZvHrPgDpGEOgqNw-GCbpDPkCuolQatE7UobI73KQpMIu3ZeUvc9XsPEcBM7YK4dObOUPM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فهرستی از رهبران کسب‌وکار که به همراه رئیس‌جمهور ترامپ در سفر به چین شرکت  کرده‌اند:
1. ایلان ماسک، مدیرعامل تسلا و اسپیس‌ایکس
2. تیم کوک، مدیرعامل اپل
3. لری فینک، مدیرعامل بلک‌راک
4. استیفن شوارتزمان، مدیرعامل بلک‌استون
5. دیوید سولومون، مدیرعامل گلدمن ساکس
6. جین فریزر، مدیرعامل سیتی‌گروپ
7. کلی اورتبرگ، مدیرعامل بوئینگ
8. مایکل میباخ، مدیرعامل مسترکارت
9. رایان مک‌ایرنری، مدیرعامل ویزا
10. لری کالپ، مدیرعامل جنرال الکتریک
11. سانجای مهروترا، مدیرعامل میکرون
12. کریستیانو آمن، مدیرعامل کوالکام
13. برایان سایکز، مدیرعامل کارگیل
14. دینا پاول مک‌کورمیک، مدیر اجرایی متا
15. جیکوب تیسن، مدیرعامل ایلومینا
16. جیم اندرسون، مدیرعامل کوهرنت</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=TPjLzBqk62LPIRporEAymCTqpiWuCvKNpgpw43pwVgTxWoLRiAZUUUBZCQ8ZiRmElJvHJEDgAlSZnVfarxyh7c-KF-9q2VqviQmNK9QqAbzGNEsIIpFcaplM_NSdDXVUdgiEwZaSotlPMaKBb6D_KBM62xLf-ka3cHY3SHuibhbjcgGx0fdCQTo9e4MUpPRNzmrBhDpbc0Z5PqjJQRDVr2_Xti_wsK8W0ExrcnP9Y5VuiD5-MDpzYbl4EyVf0fP9C-KLdzmNWZ5Jfd8dS0_Hr7yk_KEx_KcxO73XxugojXa4WcUXCKPyJ6w62PYXdmQPsuHtj3AwGOpw6wHetxb1kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iv11YjvSHjOA5CgHMjQcM0TBlZzC2k-D42vWUzo7M5KVaQTBxYBAyJqLKgDTfa6NdVh_Bf7dJlzKGHOaV5nIm7VceDZuMN54iPofG4GAZazfgkvGNUlaOyePG6-BnR3oznPcBKzvIZucL0CtKmPbt94fPGamfDOI50KPIcNIy-oZPi3KEN0Aauncu4sU_VZ2mRzi7aL-Jcj4S9SZ6vfWvARkGCYirfDqfZ3i7NBwqyiI38ybeDNtXZX8A21yI9JgbCxcl18y4TNw2hsQOVdCZrVFEpyc1gqhjMyXkgThkrNUuwWMHYsFJ6gbySkQ0WzVpKej5LfyrxV2IFzuEkoT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhrKbyiWSAycAOQ3Y61B5zRwlE7SGEmDuaCZk02b_ADFmNKoG15C7ZzRsGQg8951OJx9FCx0dqGpy6m1Rou3fAOynb9VQFIAOVHC8xV4X_nCyfbWXej8MmPjjfO7qdkrPjCydbovMwCEuNWige2MsQtitcPddextD1KNmvgjAv7KNwXElwXzFSGhAXPfvORT-OSZ2jf4Vewh-8_UcaSxDFVN6ELH1S-0-3Yi-QgLaj498v7_guhY0P-MHZ5iBEI5on_TycfMk9UuOmZLTaCP5a3Ov888NpoXJR65x96Fb7ZLcy9zsSr5M3Vz7cSXW8LWNsBY_h5byt493a7K0QXdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klwnGmS8NiHg2etzJjGPZVEftczMT74T6gacBO7P-4e7FJEo08dpoDpGFZjvhmhtUTCesAxZ1o3o_YO0iFappWLriLXlUgLz6kDRoG8-pXhB61tsARqW91P9_G3PAP0fMvgHO-XOE-xlAIxBpoiKJo37xVKfIhG43lVV9EVZoNdQsoLi7YVRuWrr5mk02TH8VzY_zM4dIq--S3icZUc6CA3fHFiftXq-0zihK6egLLCpieB3lGRmysMJeWo1dL5hffJ9yIyxk7Q4PgFVf8ChkSAmuzm4IKR4oToC2y1kpJkzks8YpsgDQ5p-40b6E9yPcbvaUZT8AnBJTWSNtd6EPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBfDvoSo2iYwpP-kRoorvxwbdSEWXRT1KDhFMNZLE43rxodDo5IWGkdPBTJm1o-KffSGnLOnU4pehx_m2XS2KHBDntsvhybj6iXLcQO91yGKkxG_UiVoEB4ao5rWeJ7mXFzpKeKQlC1TmZHDjr5MorlDBxgI5WctHlAIf5kAOxEG8AZfW1ttkr67ZeNn4JByQQ6zFqXcbySeOxRvv_7ubJEpBlz9afDnc5QZ36YGOfChc6sL928Re0OfFboqfo_mmIMdCmsAnc3GbC6_m9JLAbeP3YktcCxJrAyVYJhjILdpekUItJeKFgG76RhIveE_3Jxr_-Hw0z4JumliOHJ3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYOseJAf-Z6BQMVYyYCR4JD2vZxDUJSTQbP-9TT9bs10auM3ct4SkI7Y8KvUsCUynf9NUZymWbxgG8b7_-xfr7RwRKJEw64eun0-vmx20FO0Dycv7haHnTZU_xydgW4qQhz2_zgsE3ifPD2rOA43rXAOax7S_TqCelUs8Pf6p-Xpg22hm4KoH8SVb3Tr_HBUr9wZn8G364SkEcErtasvXMM4EMj7_TmYt2nYXNpMXNLeN-iKCO-SIRG4xzm31qUWVdbAXnLLTcH1TnXG3ViIcHPBL0qCyt6-97s0qsFQ5ie-zvjUQCOAXJLxkgxHdss0tO5BGDLwIh79gbtcP9pP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rD3v0ti-kPK9dMlv7tpijOpEhMiCnJvTtlaCuMd2IjfO5Hh3Mh34432so3B1hMaelKA7jICDU9Q1eHSKWG8o11Q3hxgSjDEcs_R3WVNBgFW28yr0JOeUzVB1XEv2ou6HlGv9o6E4_JpT0l9YvVyHTBueyL53u8VJrRoPQfiJlQwmE597tnH1DmSLNMZ0cE_Nit1iW3vAElxpBdsY7LjE7mEWgECQSCANQsMiECYoPyD2uZlYVla0sgAS_BRmHpckd0ARgmUq-7cOqFCxAt_QB7kZKLZ0tuL9v-eciaNSbX2wgINZBR8J_gzPMA0l_9WG1kTj8HfR-F7KiN_9ZTJc24w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rD3v0ti-kPK9dMlv7tpijOpEhMiCnJvTtlaCuMd2IjfO5Hh3Mh34432so3B1hMaelKA7jICDU9Q1eHSKWG8o11Q3hxgSjDEcs_R3WVNBgFW28yr0JOeUzVB1XEv2ou6HlGv9o6E4_JpT0l9YvVyHTBueyL53u8VJrRoPQfiJlQwmE597tnH1DmSLNMZ0cE_Nit1iW3vAElxpBdsY7LjE7mEWgECQSCANQsMiECYoPyD2uZlYVla0sgAS_BRmHpckd0ARgmUq-7cOqFCxAt_QB7kZKLZ0tuL9v-eciaNSbX2wgINZBR8J_gzPMA0l_9WG1kTj8HfR-F7KiN_9ZTJc24w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=WxSubDcKcj09n51kHs_b8m6HuDcMY-93gOezv3Ul9I7vdC3kY8ltrn9PSXDQJOGzPh5Y9SWMSNVzLNXDyUT0SaXe6EvdzyHzYkqisVi04ySZUSoxlUbHKGZtV3qRbeQQIvHPo2Ihm5b9gbOJU4GhhyO-AFON_ADAOqoDYt1FfwHW4ClszC829fSJKjDgxaI2BXRicRpWHBpd6W5Os7ALITKZgNyXwc7ck9CoihJsEZYI_SSNFHUbOMrXac2SoXeFqlS0eRcT5tJ8W0QeMSG7F1Jbxja3h-h4WN97epql1MT2p-oQ7a6CCK_l0RsIu-76b06it_Na-MFGn-4Q4VcBQVGqVduOMRltMiKO02gN3vzrSVXLmr5J_WM7pfKVwxZ6i7gQTqNrJRIqAChO5rhUqywKoWM1g9vzqeHfBkInQBqHHnQAeF69gQTbApAXTR5bEWtbtt4k-48slaiX0BIvV-mA8gFdVAev2t8gVQfGUkB-N6307oS4sl8RkYh-09E_5CTyk9snhi13LocqrJldYo_ZJ4JwPCT57C3djKirt0xA1svLIqSIYUpXTs28M5B79L7cCdx3ooNdjWd3PGstxAwjoAcnHxNJVg4HUCZZRMzPFup19R_7ExPFWSpJ8LPlhEhSjXw772_0WNpXzHQP7PVSvrKfUso-vpZfDBKiaxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=WxSubDcKcj09n51kHs_b8m6HuDcMY-93gOezv3Ul9I7vdC3kY8ltrn9PSXDQJOGzPh5Y9SWMSNVzLNXDyUT0SaXe6EvdzyHzYkqisVi04ySZUSoxlUbHKGZtV3qRbeQQIvHPo2Ihm5b9gbOJU4GhhyO-AFON_ADAOqoDYt1FfwHW4ClszC829fSJKjDgxaI2BXRicRpWHBpd6W5Os7ALITKZgNyXwc7ck9CoihJsEZYI_SSNFHUbOMrXac2SoXeFqlS0eRcT5tJ8W0QeMSG7F1Jbxja3h-h4WN97epql1MT2p-oQ7a6CCK_l0RsIu-76b06it_Na-MFGn-4Q4VcBQVGqVduOMRltMiKO02gN3vzrSVXLmr5J_WM7pfKVwxZ6i7gQTqNrJRIqAChO5rhUqywKoWM1g9vzqeHfBkInQBqHHnQAeF69gQTbApAXTR5bEWtbtt4k-48slaiX0BIvV-mA8gFdVAev2t8gVQfGUkB-N6307oS4sl8RkYh-09E_5CTyk9snhi13LocqrJldYo_ZJ4JwPCT57C3djKirt0xA1svLIqSIYUpXTs28M5B79L7cCdx3ooNdjWd3PGstxAwjoAcnHxNJVg4HUCZZRMzPFup19R_7ExPFWSpJ8LPlhEhSjXw772_0WNpXzHQP7PVSvrKfUso-vpZfDBKiaxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZkSsuqNNPRx_DjAiPnXw5HcDKCLSkaxr17RQP7EVnQmtMCgoDL06XFGGh8bkIWFxcoDhNhVGeVc4vMkUXEdLpH9N9yWESJHdCKUUYILveRk79gfizKhh65VLUPw3gfsYq74FTexoYCo3aIRciQSY7wE-9emXrqT5Z9ehEeakagyHEYmRFGeS6T02Wx7zCRGuVkLi6BnBSfnkzVTuWoixFz_qrTZBtivMYjqVCC8DKmm1VyWYyrtY4HEefo7deF9GgU5OMovXNhzvH5Kyxz_dGLP-mXzYTNSbNtWHoHT2HL7sQyXT6ZmFU8IfYVE0gRnCFuwDx-UaQoKBV3WNx194w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAsEFOHgd3uwo38fdUAaQlMfENsQvRIFFFWnond8GjgFL1rJsBrm8pFSAgr3gB2vFvqKvGhmSKJnF7zTBGJRLUHOqTHnohholSIKsKwgw_hGhj_U3XLUUyuO-Z9FX1Y0cH6-CCXSpTXG6kgSflCE8OddRZLb0HD4omyR_aCyeXyZpacPZJOqvKv7VE_aOz6sBYzp6Y5hKF83GnrV0UlZwRbMbsL7r27k_ApiLjDXTTEJuj5_DIzmwgLCGNcEK14zXZzCMdTlj5O-NhHFXoTAVjTkIbUiAIg94jXpWOSrGXKMfpzW8kyifc_DGcbsoOmIF80H28BcNlzUobtwK4jJFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNuBdCkm8z1KfUi1vdmWrCbBXkJKBBlokQclcU-2XSB4znnZVRW_gPWC-7R3ivOORKMYuMEDoRZZhH3U5Vi1YLdjmWphEaMk3vkxbHarTKeHXlDwRAqTsoW7UwMjOjD23TSFPNjUvGRS0n9bsoH8hob92RRoR6uPoK6HHacWBh1qQ9adbYe8lgaGZQOsk4JMLaSf1Sja3CriF05U8YZgOZvtEzXDrBYOCppseBR9gbD1lkHvWR1YMrawWyMpd0WEVQzN7BtdY3ZctYkCkgfRdtxT-ruV_94M0lqUhBJZIHHpfcy51fIV5KjLYXwQ2zVHNh7I-JU2Bhy75eu9l6ZDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egKmXKIKMCQL663wGr1SBy4fxLP6qlGDR-q2YFJlSF2aeFiv1z-dlBw2AI1uHRupXnNDkLNhayyVDQvBd9XlVXHZMKJY-2giFrxNH8ni30QLQfnt4_OnXNgdwMxNkw8LW0zG0JN6hmgtMtGNicsM2ZkoyYS_Mx5KcnMQpncfT3ZA3PtPMZ3woD8VyicbRdSUK6UFpOYKiXeoiXj3jroRcSjUR1M_f-u6S3xsEeE2lsM4QEaA7orQ5Lvvo8aMLB7EEfofhjhcvISAsizfvfxbOmge8P4-uJ3v54suB6LluAGPEofWd2ImKanPYrX_AnBUwxNzGAVHhBW-TlbJrsdgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2krvu5Md_ndi6FIKYYYcjI9hsyE74KJ4uR-pCNPQEkRLG7RxHwGU7MWhtCsJPTEkNj2Lo401mlS-fWeuTYqptm3swa3i3ikTB9LebkG3BwYtaz0POjMyHIjvp8GvthMWZj1la2iH2cIXO4eZkw0zrZXflWKOtJv99IAd1wFeUfBx1jJJOXdoqN5WMJFmQHLtA3KyukimvZDGupU7-tA7ND-6kaQxr4Pap0Ra25CYtY4T1nUHvi8_oh-3muEHg_uIO27jMWtehL90T5bmMWBHCoh9Zk1xnnTasvUVMBcuG3wbHwv_x9R7SoXxSgFee7tUaXHnTS0QR_fH1_ris42jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELCVL9-ohdoHlZpvwhtU_YpEo4u3Xkx_fb7qpfiJQW_-hjs2IzpxEiEog_EbZm_SSaUjB9s2ovN_3wtAKrK0sjL_RSaHNHDb-knYqK2p5djwOGA_IeYeJr_1PGG36NQsmLDZtJZC1CDCHeb2IDeQAx2SHksWMJ1cQbhcRQRhX6--T5Ny0R-A8rYVa09DAzeYasCKHNJtp3C9uOKdmvJAte2T4wtfOzrHZh_5eBoNJ9p_R3GAqltO8eoXYJbeFx077Z2wLeTb9id7ybS8swgBp0BcocDlDUVSExn6l1AQgUXQ1Wyu4rCQq1f4bFx8TUHSMALeQD4lQHUmIGSqn44qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPxW_Xw5RY3Ts0jSIca-JETylQR_eHBqnJKi9Lw7fVWkB1EEtZqQVenhufFS2lMdFLu_i0k704bUHlHT_bl1dyvmng1FfvDOh1WT-lNjiiafbe4Qi_5VZ8hhvSojXk6rg1D_mVYXPlcRR-bUifds31Vznmyy3IGGbtCYu3qv9brFC8cf7BKG83ePYkGXvgCdGidsP5H_HfX2mLJBCGYrYsXUhQa2nCzW6ZEN4-SfnVNYMPwgxKdThhV6hOyBBpJ1j66_yzuulw91vHaC33sOCyRlv5FmCRbQl9LeYnE52wdadFESd_EM6lJXk81KPEvW7BjKHjzn-gpKSRK51E-KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsD7QXLF5GbfIr0D8joEQZzIIX-OQFPp0K6E7E8ItBF9-pt1FpKcLbltJA84LPkUCvZ01jxn5ox1Nu1JXBgCGTWIO61OHsYayLitbhTKnct9O2NhTj9C22kubbEYjrofKiQ9RKP77MgdWzHLwSv4_i-rQ5JjprZL6v-qc9j06tdbYT_kOEGAHsNwE3VJNra7IvCjAQzl3FcLCnVXCaIk5v26SZs5Bclp81iGOy4buLraiwUsxSYILfGK1kTbAhDoj3oGxw10Yl_ud9pYTLmGvO5v5hmrQpQ2EKZA-MvDqXuSpnACn5-jEhKVmjbuMgEi3E4xofWejdD_j-JjhC1gRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT9usEEvR06lDakWOi1xPK5B17l96D7hgXtskwMl_tlAM7JCzM7BEJb8tQ5b119Q1CRl8sX395ypPRCCmH7_2DmGLreqAqrrz3v7ulcQi6HGRdOnZ8yqtpQ-TiDHs8lw1F-7gxWL8A0e1OTmnVpYh57rJmpyulnVN4Bo78okW8fsVqu3t1MDWLPhdSNj9wFFm0Mr9TIlUYC9mlzV2T-gU8YDfc-0MaOrfFJiLTQ_t9eCFzoKoTZCd4AxUrj3Y1sfDiY-Er9FYrMl0TSxKPmmSknkWEy0h0NsWc0Fs_e4DKNuLd38iOUXywm477io3HNJPHq4C0uhPzckIJrpzx4DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=QaRImqIUhV8wkZRetcd4fy7colhEf3zr8KxnGtw7m56pIaAmvsyXIJe5k-xZ9bSrmHFjXP2aYsBUZljUNGPEOOBiosE1CLeDGx8f88Fy_a2ik89orGVjEFm1owwAf9fm_FGn9-f1XwXlK9Q39ikM6fTUiwWBaofI_NHlaSKkZ2TApYgFUuCBu_ktd-hXtmuhSqJMlll_gZyti0gRPam3AlEYqduswLQ-O7eWkFD11sPZaU9wWr1Y9_RDcqxxWCQ44g0pLuL8sGxiJqExyA48o-TPDmEXUxlS6FU0t2x-BkvNCVMFeSxsPegb1m7Mnq2kAgwsznEVXqScAaA_5gT81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=QaRImqIUhV8wkZRetcd4fy7colhEf3zr8KxnGtw7m56pIaAmvsyXIJe5k-xZ9bSrmHFjXP2aYsBUZljUNGPEOOBiosE1CLeDGx8f88Fy_a2ik89orGVjEFm1owwAf9fm_FGn9-f1XwXlK9Q39ikM6fTUiwWBaofI_NHlaSKkZ2TApYgFUuCBu_ktd-hXtmuhSqJMlll_gZyti0gRPam3AlEYqduswLQ-O7eWkFD11sPZaU9wWr1Y9_RDcqxxWCQ44g0pLuL8sGxiJqExyA48o-TPDmEXUxlS6FU0t2x-BkvNCVMFeSxsPegb1m7Mnq2kAgwsznEVXqScAaA_5gT81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsMv2pM7wdxmX__GiD3cAV7tPIwLGWXWOJWVfTRci0-KDZbdff8AKPKpc0YQmq7CoNAdh7BqtJ21J3X0M8kvwAUCGoATWjXtqaTyp5hp50VjD5APs-WpppUwhp3az-NhBRJbHs3H6e9TLuQ2pId4dYgNqwKYZr1wkg5O0-rkL3g92wmgHoBpr798xYEsxuKUjeOq6A4xul-HoBAo1tsgKFMoWqdTWdLGhF09uBrVVMYL_M7zfZDGU0dggBWCeEfVQnnuHGJTIONG-R8v6vmsy5psVO79VNFSg6YZ2egav4uoWYr6bjkQ3JLGso5gRR__xJRuO-XPbe6kwPCzfyLIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YArHI78rt9CIcdTcK96sqwZZGH_gqhIhRQtdR34YODn1avLTccNTiaCwZK4BmnOsoiW7EC3cIfYI4XDj_jgbWBQ8YS5rpcsTrpHRpKi_XcutNOAiPFtNMh5rNxCEZdtsv7svaChN20k_5mnRTc3wWabDyPNTNzKgDFKBvZwv23LBWMtShkJOrBC5JrBpKW89n3CFD8qVEAw9qeZPNozR_3j8tq1_RnuHDBzSkv3W5UjD_mVDf4SvPtDdZEpKyU3c_5pSJYi3g2Kox4rBX2QcTfjwk1_OYx16hBl9QyLJYWatOin6Bfa8SB62n_7yNxXCBflKHARtxgPZmwRCqpyZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plTqGe3TnWrwZ1bQ45zIPqVTTLvxVpaEeoqs5O0pwu_EdDg8ay850dH4c5t18Pldo2ydEcWG5bU4Cd8RZ9WrnSJlRXytWmBaaoGaAGYiZ4laz9KT7VaRNYjTAXGueb2roS86qP237XYAztryBqQgVbo87lyPAgh-CjyZcx73IobDe5cRn_Z-qKBM5WvTU1NRmffmVV_DFJtss2yNX0C1MK3-G8mFQcWxixSGibO7dwavzKZ199OI1RFQly9oPVl3ODEfffZwUs_gYAFXcg6I4z-ZG3aTvGb4wJeK2RoFHtN67yu5itSgpANszCaxr2dQgPNXS5vXqF1x-wl9L4iQMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hn9hIVREtTJ4pz4s-jfN73DFXRt_rbVQFDgHhXl3YZBki6F-mj0B-T2BsK13oy3vaSWJqYH0ogBl-hVWemcZdDMCI4WJTE40cutB3RffWqOu6IKrg6pvBpWEiTOKsPfaSURZoc-uNmdtynZGXDyOIICbPn338BxGrSlbJvBvbPNHn8XDKdvHEmKWzHznPsL_4C2yvBIw_KrP-hVWxDjcUCCPt-jhleiu0EgtbIFZfow4JcXz2oVzB7rpHXebsWEN8hzPM8rD21Bnt1oMLQbtwcxBSeALpt1HvPsAGXV0u7wh2M3MnuwDCiAeVMI3U4tbjKg-3yUqkEiDCgwCP_rMww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ترامپ در آستانه سفر به چین: نیازی به کمک چین در خصوص ایران نداریم.
🔺
یا ایران مسیر درست را انتخاب می‌کند یا ما کار را به پایان خواهیم رساند.
🔺
‏من به یک چیز فکر می‌کنم: ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
🔺
با فوران نفت در بازارهای جهانی مواجه خواهیم شد.
🔺
همه زندانیان سیاسی ونزوئلا را آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5ZekermtUaWUKLAU1dKUYXwClSpm-FooWS1uUwqzqjm4rsgldr18s_vsoF-XY6Z3WFVq8RDZ0YVb1v-CwxglbMf1Jv4cPPpwhDS_CEff7GlnYH1T-qtxVn5qDBdIdAQjaHsw35UE5buPiJy9gweUkFL4PHFwKdbEYqUWhvJpvUig7obL24SVVMYLgOdStusqFkZsXxLErR9UnHxMg5ctHwemF4mKIxPOhOqvBx8RErcMgzMJ4RICD8ZiOTD51c87iaYt9VX2Tk1SBlFSwy230RtW8ucp7UD43ASeh-a8JlDBXC0h19Nr3AOul2u3MeULOyEJQKRgEqSGqy4DVxVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BYW3PqSLhUhryjfS9YwPot2dxHsiZSCAQiRz3ZSA9FAqCcF6J--V2rR4VuHv3iT5BjjE2Rk8S9eY3EbT4OGxYgWWBWAq8F9rPBXVmapATMAI8k8WmoM3Uf30shQ582Q4V4ythWRcxEIdW3DJ2Tq5id06Yy24dLAGLC97hsaGTQT__IO39EAaRpc-4F1PcmW4HQCV9r1iwo0DA2I4QAvpxgdwSXCXErfxvCbpfnrOFcLpz7cjfthRfpAxDl99wFTW-KJ-UiY_TUUgmDH6yKCYkWgUxEzpK39tieC5x1mb5q4LQYjHDg1rlQFMHREum_68__sTqWFD9V6AnN33nm0zgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای
رسماً جمهوری اسلامی  را متهم کرده که گروهی
از نیروهای ۳ پ  را با قایق ماهیگری
برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری
یک نظامی  کویتی زخمی شده است.
کویت که امروز سفیر جمهوری اسلامی
را نیز احظار کرده گفته که ۴ تن از عناصر وابسته به ۳ پ را دستگیر کرده.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdpMynKPdISUJjXuCkd0d9275BXv67vSYXO5zYLTFCxut4N9E-j0NcGkHtmZk6xKOn_gbiUp3srDVW5Z31yVnkVMOc8a7r-e1rD6jmAGq0AwVII_BFPMFmQcmn-vQDpj_Hn68rjHTRSPWkJdhYTrwTO6jZc4VDRjTdzLb7APh3X8m1oscskGa3SJuzve6oEGDgl1B8fq5l40AjvOF07z8MBnye6bABfm02-LVyDlJwApQq562EyUdsuzV3n4zLc_SntREcXO-B0wa0GOZh26ggDaPK6e-0IALDvMC5EFSkzE9Khv_d9Iwpl8dda5qutcCKJrXH7ArxpAICH28zBneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijUlPPX80j_sA0s0LI9acsbZjZ-AdTehciBHDcyU38jpxU9S8h4LDDXTe4rhmTGuD3p8tDE9-BESuTjOZM0WgbKXnndEsC-F-lnRW5e87YbmtHU4pwYpvQeg701PyZL9EE00DhorkEfkY5webYJVakgVBs4xeQbe0jilE4JVSWGMrOdPB4HnuKJU4oeuu5Wz2oKIoInFSnQGiBHehyXOTYuPNCuTjuPDPvrC7_PR0Lgc6I4Cf9pUqCUzDPruB-Rb6m-QYGpp6Wq5mJbE8gxaRuVWzJiIt23Gt2-ZY1Gl_NFFaALCqgAYa6XRj15tOx7Cv3yIsLpQ90AS724SkEFYtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=bTAzs8GKU4mxo6FI6lCKecjynTPNlIQXblGGjDUjlV5A-x230mHBQcoKR_zxt3_-8uYT40nnDq8QJcbWVYyh99IBsaAmz3uiCaqMl2bHyQ1APCiWDeZjDcxweguBH7U36ShULy5ZBdviRtlqax2xD9SaLibJQSaFv8SjM4vY9Ye1EtfDkIEyIovzOuUnyKnJlcuxBAZGloChWLU8967vguf_JhkB_QXXQ8l8MIEqAaFmWxc1F0CrXT2T7InVyO6vrlihl-cFvsAFfA70JFkX2NvLK7G7wxFQpnyVseIUmWtEPD0DunZ8ofPgWmc0PunIm5bBtNlQAdcQji1A6n5kKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=bTAzs8GKU4mxo6FI6lCKecjynTPNlIQXblGGjDUjlV5A-x230mHBQcoKR_zxt3_-8uYT40nnDq8QJcbWVYyh99IBsaAmz3uiCaqMl2bHyQ1APCiWDeZjDcxweguBH7U36ShULy5ZBdviRtlqax2xD9SaLibJQSaFv8SjM4vY9Ye1EtfDkIEyIovzOuUnyKnJlcuxBAZGloChWLU8967vguf_JhkB_QXXQ8l8MIEqAaFmWxc1F0CrXT2T7InVyO6vrlihl-cFvsAFfA70JFkX2NvLK7G7wxFQpnyVseIUmWtEPD0DunZ8ofPgWmc0PunIm5bBtNlQAdcQji1A6n5kKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPsjH52hUonGcvyQpWQWonLGCI506zijqF0Ikpx25R6g4n3wusG-iMADRQyWgJF4PVvzLfo79Iap7MWIQzmdzzqaCE2T7M6wicHqf4z887I_X61-dXYO1aIEn-f6BKvKU44RA7rn2lui9s-0cfvqmEy4vz-3vPKdLB0ic3Bis_rEOo2ViSxwzMQ9UcO8jMJw0vy2jtycmL6i_AK02B_DLn6tIZf8uSeA3CUiuKH6bzqTcrv2_IgTKB4gkv-LsooKzBUomlptFGzOJiMNiKMBvU6kqXrL5iHOUm01OOW1PPNtaA50H_cst-D4APFBC00GMou2DBpnM9ttQDdJn8Y0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW8t4c6ekKD4T-wfNY1sX3RCOR9K8HNLf3AudQ14mPvA6OiSA6hxyKurMdjRBQAqZDA4iwe8l6EevLO7tKvJ0XEAcOArEYxM6rWL97Tg01k2IEBY2exQe1nVADJaO0oT2_ZaTpry5GlJRyZ8aEaxlv4YfTFKCaUrSlb7cFafoIXuJhi1nqbuVUY4KU9K9EoNcTflfoNoAXxohTR77HYiBfiCZ6UZjrR-0vzqieAUMsaIUv2mR-9NAOeuOv34cmwbf0jUl-fTeq8quJ0lYOU9eJKpFN5oADZl4OYdUv05hHnFXM62V74GUZTij6Q6nHvyvPbGqhy55VnI7_e3qhYUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2CL2h4w1IBWu9OwkSrgg8g_xNQyI-Rc8QPDfIQ96GzhZHPjkkA6ii-Nr3GI7A4QloHLrbXGpD37E3OkkYBzsAT7Mchj6DFK_PjAy6JWXZ-lfi75YCMEUE09m2e34HbE7-IyeNxBBxpJG-U5tLbrpL7CcA1wazr7BN3unyniKmlGfyRd88QasbWgUd5oSQtQLQ7qDkobooPwrdYjphFbx-pzvbZtx87XWINWq8jewxgzTAqiOMIJlAWyoyfSiUFYk6fK6-hewcO7h0XFFCKoC9QDdwRJQ4rlMCYfK074gYAfgqkGtBVodcDcUOxC02IAaJ1Fku3eFn_EQnH2bzli1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8JIBiG6TRN6rjVquhQN1gwbIWg5bYW8JZmglMH8h2qqGjV5b6rXk5g9eJYwfP7zu_iE6TttRwLQWOuFPvhKjLPl0DV_y4hltgTC_Wz6EI-eAzz1hPgiPmZoyWgi9xchOO4tiQfuVAwCoEoV1-MCV-34ekuJKxf3lMNX4VGGFN3dlMYXLSjoohpEtOkuldCxvOtF8JCP6UiLEcBJUM0IFu9PaqjLesV_xnvgClhJgqWgNZEq1rjv6v_jp3iucNk2M2ZMv43XVB_Ajys0b83xVHXKBbnUHsCqryq2OIw30MzyvXb1hbv-jFXfMNTTGsbw0G9GMEmO67k-Qiwf5JJcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKmIJ9ad0Sd8ucxt5OBPNMmVvT81YJHr0VyuaDfDU51Xo9AdhuVeKsi25LWEbcjVGKYISvcTG3eEJLul3v99jRGX1w3XlsLt-hDn3NyWXFf-zuAhfWwf7CSD5XQmceLvkGJTq4QW0CxNkc5GkOJNcypuioFUhOBk-A0jyNf9yd5mwhL7GTRCiiOfWH-mzbG8i-hpDiTnAqFIlLRIuxdwdB-nONsQ0qO9NML50OEWCUwKnfE_ka0oE9wnqjs_G5NlgsDHoIn4ZHSIUM4CfFeefXsBAAVxEJ7f6ez-qc1ecuFaPLjYwNlDEaBeqaV-MNel6lTbeyXSZ-BaukuHZ9rcmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
روزنامه «گاردین» در گزارشی از ارتباط اسحاق قالیباف، پسر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با یک مرکز پژوهشی در دانشگاه ملبورن و سرمایه‌گذاری او در حوزه املاک در استرالیا خبر می‌دهد.
🔸
آن‌طور که در این گزارش آمده، او از طریق «اجاره دادن دست‌کم یک ملک در این کشور کسب درآمد می‌کرده است».
🔸
گاردین نوشته اسحاق قالیباف چند سال در ملبورن زندگی و تحصیل کرده و طی این مدت با بازار سرمایه‌گذاری املاک و نیز دانشگاه ملبورن ارتباط داشته است.
🔸
این روزنامه نوشته که اسحاق قالیباف، ۳۸ ساله، همچنین موفق شده بود اقامت بلندمدت استرالیا را دریافت کند؛ این در حالی است که کانادا دو بار درخواست ویزای او را رد کرده بود.
🔸
در این گزارش این پرسش مطرح شده که علیرغم اینکه قالیباف، از فرماندهان سابق سپاه پاسداران و رئیس سابق پلیس ایران بوده و به نقش خود در سرکوب و کتک‌زدن دانشجویان معترض افتخار کرده، فرزند او چطور توانسته از املاک در استرالیا درآمد دریافت کند و در این کشور اقامت موقت بگیرد.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsB9NQJzwc2IF6YcXb1lzK7eZ1LGyeoykqRzM_8l37XNXPIfgEfBpK1bpTFZG7HTbkSV3zGheUJg0nISzZlCSxDa0IziXI4dafXHZGcpOuL-iiIXgem1A6q13NA5qCkkwRYFAFPlYo6tAth6ndchLNOODWvZ2GXGs3wlP2i9Txe8tr6HmD_jODo2Nyy9p2R4jGmNXTGjki_izBDnhS6jbtvsHeYIYm_YHKsX8pWijyBEOWHCJJmM2mUZPCC2fgbwoPkuQSmV3cThMBOMCUGO4ydnCGoM8Xk1jE7q6mk9mHG7nTh5rj9yJb6vZUkXlW-tpYgRo_lOPRTUFVY5nB_12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpdL1-86TZMtmwqE3P5k-xnvAJIrh8M1L58-RwSSBkJYbIbY8YwFdIBhZ_T8XuZzTmd9jqJeYwqrBFdmMm4X8bCuDqYIZfNCRgtDgldR9mpolYNAg7FM5IPDzEOW5ShAVfbehzNYgLdGCrXUgULnwHb5Lf7v6bXFnTS3xvp0T1gAFaS49xnkM-LoTE3HkGYcKRL2gzAYl2Gys6MKpd24wHfbT2ZnS7aux8-nvf1v0OM5flFClmOCQzlCR_s_jVkxZ15bp5qlMKwSPj5021rm01AxgOP18yBeD2FMC88avY-jxfDIRpl4yfAYe8TS5efy46Fxk6wFu8RLDiM0hDyVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itTmTuya65aKGrJamPYVYELLTRhEysDMjCHuMKOwnB8yiccV7LidmT6NyD0m4MqZZl3U6KRnzRV0MYEBy0ELunEtViWenJxpfaAR-m4pn1QBr5dzetlLs4wPu_KaGGRReQaucuyWymyClM3XuB78xa5UiXfYSeEgV2gJI2a_yHIw-Fq-0pyGl3irkwAU0rCRnpn-598TZ0yDMHPnvmyk9mEmq3ElysYtvRWEJ_dzphfyPQoSSnQ9ofmK4cJ2bK4Xh-88RI0sH41i-tZ5e_wi1BzGS1AY3SwY4qg9UvHoiZFsLiBi8boaWiCIP3YhcsrseBNd8MRvCZAg8KE6kQ5OZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
دونالد ترامپ در تروث سوشال:
«
ایران ۴۷ سال است که با ایالات متحده و بقیه جهان بازی می‌کند؛ فقط وقت‌کشی، وقت‌کشی، وقت‌کشی!
و در نهایت وقتی به “گنج” رسید که باراک حسین اوباما رئیس‌جمهور شد.
او نه تنها با آنها خوب بود، بلکه فوق‌العاده با آنها رفتار کرد؛ عملاً به سمت ایران رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار پول، و همچنین ۱.۷ میلیارد دلار پول نقد سبز، با هواپیما به تهران فرستاده شد و مثل هدیه‌ای آماده تقدیم آنها شد. تمام بانک‌های واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند!
آن‌قدر پول زیاد بود که وقتی رسید، اراذل و اوباش ایرانی اصلاً نمی‌دانستند با آن چه کار کنند. آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید.
این پول‌ها داخل چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها باورشان نمی‌شد چنین شانسی آورده‌اند. آنها بالاخره بزرگ‌ترین ساده‌لوح ممکن را پیدا کردند؛ در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی.
او برای رهبری کشور ما یک فاجعه بود، البته نه به بدی جو خواب‌آلود بایدن!
ایرانی‌ها ۴۷ سال است که ما را معطل نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً هم ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند، و به کشوری که حالا دوباره عظمتش را به دست آورده می‌خندیدند.
اما دیگر نخواهند خندید!
»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFtaAPe_J7DqYmc5ojH3Le8drO4-MZO3ZFH1f-YDT9Y21y-Be2Sd7c-VLE8SDBsGT1KsnezU84qmK2JKutKbYWAzXsL5pDSveGDMI_Y9KDsLiAj6IU81hRhMxmKUzhX6yj1yIEUwoi-VmZC7p3g069skl2CrNbAAtYhSaLFH2aZwC7BxsOu0Qqz1Gzbljtis0LP3qKVv7lxIzRBShqN6eSb_NO-zPWSwSq-u6MkAwCYB7lCbXacU5GQMPij-FbRPdOOH53fWXKcNMay3oAplD4zikPpGAN0IbJWKz_vu19mYGwHmphLxzcA3ol1CiIp28ExmBBlu57bWeBxOi5tN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه چرا کمونیست‌های ایتالیایی نخست وزیر ایتالیا  - الدو مورو - رو در می ۱۹۷۹ کشتن!
چون گفته بود : «باید قدرت رو با چپ‌ها تقسیم کرد!  اونها هم ایتالیایی هستند! نباید مانع شد که وارد دولت بشن!  دولت ائتلافی ایجاد کنیم اونها هم باشن!»  کشتنش!
کمونیست‌های افراطی کشتنش و
گفتن : برنامه داشت تا ما کمونیست‌ها
رو از مسیر اصلی که مبارزه بی‌امان
با لیبرالیسم و سرمایه‌‌‌‌‌‌داری است منحرف کنه و ما رو به فساد بکشونه! در حالی که وظیفه  ما «انقلاب کمونیستی» است !
و نه سازش و شراکت با سرمایه‌دارها!
و‌ همین چپ‌های افراطی (در ایتالیا، آلمان و فرانسه)  که به خاطر مبارزه با سرمایه‌ داری به کشور خودشون رحم نمیکردن و دست به بمب گذاری و قتل و.. میزدن، بزرگ‌ترین حامیان فلسطین شدند (چون اسرائیل طرف آمریکا بود)
چپ‌های افراطی آلمان حتی می‌رفتند اردوگاه‌های فلسطینی
کار با اسلحه و مبارزه رو یاد بگیرن!
کاری که چپ‌های ایرانی هم انجام می‌دادند!
خلاصه ریشه این داستان‌ها و… خیلی طولانیه!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4899" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=WEJ1Q8dgfQswiY4ccYjkh_O1Y6sb43XMQ-gA9X3_t4ejWCFEhCznJRZyDDlVcT7DEG0McBaz77M59IRhxZEFZZVfYcB0gOm-5Q4CBrS6Ovw63LO4XPnrZeiXjuMb1-Ou-Aczf5BmRN55Ql7oruxvILanTUdzv109TgStUwmAbPmd3L6b8TDGJhL55FlcQEh8TdFjJEQh6fbZaohjgr-9z98MNOibSQvDkFUP1dH-eA0sZZu0QwYg2QfXmvoUCNda_AuBA-CqiRpPwm91pMACcLsPIffuqtD3_XJPM0hbfFMjrI4WbjQGun3vy071Sc0Teiu3arBYbYsOKswTKqGabw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=WEJ1Q8dgfQswiY4ccYjkh_O1Y6sb43XMQ-gA9X3_t4ejWCFEhCznJRZyDDlVcT7DEG0McBaz77M59IRhxZEFZZVfYcB0gOm-5Q4CBrS6Ovw63LO4XPnrZeiXjuMb1-Ou-Aczf5BmRN55Ql7oruxvILanTUdzv109TgStUwmAbPmd3L6b8TDGJhL55FlcQEh8TdFjJEQh6fbZaohjgr-9z98MNOibSQvDkFUP1dH-eA0sZZu0QwYg2QfXmvoUCNda_AuBA-CqiRpPwm91pMACcLsPIffuqtD3_XJPM0hbfFMjrI4WbjQGun3vy071Sc0Teiu3arBYbYsOKswTKqGabw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به مارکو روبیو در وزارت خارجه ایتالیا
سند و شجره نامه خانوادگی‌اش اهدا شد.
خانواده مادری او ایتالیایی است
(از منطقه پیه‌مونته - تورین)
و خانواده پدری او از اسپانیاست (سویل)
او کوبایی است.
در این مراسم گفت : از طریق یک اپلیکیشن ایتالیایی تمرین میکردم. همه رو متوجه میشم! (به خاطر اینکه زبان‌ خودش اسپانیایی است، متوجه میشه
و نه فقط ا‌پلیکیشن و تمرین ایتالیایی)
هر چی وزیر خارجه (ایتالیا ) میگه متوجه میشم.
اصلا نیازی به هدفون و ترجمه نیست.
دفعه بعد که اومدم ایتالیا، سعی میکنم که بتونم
به ایتالیایی هم پاسخ بدم و صحبت کنم.
باید اپلیکیشن زبانم رو هم تمدید کنم.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4898" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UflPuQ7VxaIFQvpJQqK5j1WuPPGbaZOeYcrLP11ZQ_qwEJX_tpJjMRao5-3osLfWHKgE02Wspj67fAplsx3AxEr-DNTbPuKVJ5XIEh8z5hClzOP6PNsSVdyyDDb2FiUK_J42g-o3guuB27sBcyWCUjuOQQkEUx_6k1u90fxW7p2ZEa2E0ScpcrpozhYSEBlOxU-2ws74yRFZ8ush6NMt9eH32jGKVpzaH9XiRkaiuw2oSZQ8PVhjOqqls6jqLQq4J7TLU-IsRirgUw2iowNjQUPfBNxP5vuJjEJnMJfxd5-BXeF8jgSh2vYJ8BeXrXZl95EXXfd2bVZeUCRzbnvWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArNsbuX9i2nkKCiLbgWroe8Lur0aRWjqmsl-KYqfi6Re3utd6rVvyRP2DwJOefeepF2Wkr9jkhu50oZEPfeH90Z0uvqAU0i5R4HT3M3WYSdl7gUIlg0kDcKmruvWdA4eFt3wew8VxOYB-i8Mh5kNQtnVc3p2MoX-NOYoLJIaQTBu3Sp7CiLpmfZuG3e1Y67A-R0iLlCU4nQ6YoZhzYuyfXR7DYb65qFxNqsGlm2xxkIY_cBmVyPZGcKqMBMdtIXmCJ26givcButVJPC7-DSfS0zrSuIy1y2NSZDYHPdggrh3pBEUe5loO92stidJVFFMZtQq2tC-p__uMYrHsVM0wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=QMbsqQ1gn2Tzz8to7mvcdQ3uNnmm0uzk1ufl03fGLFoENB1gnWub0Bhahh8eqdWGFdTh4XNGjd_ebzbxaYWEF7WMuQokg1s3pcKKuenL-TfgdJv_-2PwKsjwAAduDjBQNjD79OnhKvGDLnqN_7bpEQ_4SwaiSTNtehiyScAoFs6CUyd_DjcBOr6qzJGs0iyRbOUH3-lYSxpAGx9wXL6ViQpXB_NAWFxDum128PzZW3aVFBlIzzE5ok9HmlXYC_D0Yo216xWPCqnmm4Y7ZthGTH63v4lyZGTfrQyh5YebtzuOU6aliT_JpOCqXpjJSKUh8AFEpDRzL3uDlxov69aiZoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=QMbsqQ1gn2Tzz8to7mvcdQ3uNnmm0uzk1ufl03fGLFoENB1gnWub0Bhahh8eqdWGFdTh4XNGjd_ebzbxaYWEF7WMuQokg1s3pcKKuenL-TfgdJv_-2PwKsjwAAduDjBQNjD79OnhKvGDLnqN_7bpEQ_4SwaiSTNtehiyScAoFs6CUyd_DjcBOr6qzJGs0iyRbOUH3-lYSxpAGx9wXL6ViQpXB_NAWFxDum128PzZW3aVFBlIzzE5ok9HmlXYC_D0Yo216xWPCqnmm4Y7ZthGTH63v4lyZGTfrQyh5YebtzuOU6aliT_JpOCqXpjJSKUh8AFEpDRzL3uDlxov69aiZoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
‏ترامپ: «ما هر سه رده رهبری در ایران را از بین برده‌ایم.
ما ممکن است دو هفته دیگر به اقدام نظامی علیه ایران ادامه دهیم و به هر یک از اهداف تعیین شده حمله کنیم.
ما اهداف خاصی داریم که قصد داشتیم در ایران به آنها دست یابیم و ممکن است تاکنون حدود ۷۰٪ از آنها را محقق کرده باشیم.»
‏ترامپ درباره اورانیوم غنی‌شده در ایران گفت: ما بالاخره به آن دست پیدا می‌کنیم، ما آنجا را تحت نظارت داریم. همه‌چیز تحت نظر است. اگر کسی به آن محل نزدیک شود، خبردار می‌شویم و نابودش می‌کنیم</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4893" target="_blank">📅 18:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2L0WC8n33NBqp5qA__nylu5sU7va-0PBf_1Rj-iAx3KB8Vprcvvgy_0mr2ZQ85D3qX665WW-QSakeQrst8KPK41hldct-L9amOxmbble9t_DzLyb7ITgABT0VuZXgcqU8bLSEiIJtF0bNZph9OasdWnHdWHqi_IlZSJV9LG8jp91pRnJcA-dfHdsXaNgXWTDZ-h6Mxl0eUgML1voxZDgsPUCmQDdvsqN54us-AQY6Nd5TzZMeBOuLPSb0nPx-gbPv4fDNZtMGDj6mj_OFHl1PE-uJFqDE8-5-Br1hfO77ShcnrWHPKJ4jfr5B9POXUYkZlTDNA7KE9r-1jJSjdS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKZ2HMfowtJv9lGYq9ZLAXiDNjmFwzyhTu9XwF9EWXZD4cYAvVZx0SdmsIGTOGfI2zR_1gky1pl9yUNIPdgiIEgxrhx-8iu5QoxxhQxe1hj0xEnOSQBc3KHvC903TeMnPywRrpK60_jiB4-dt8fTHTikscXJh3PrfXq-AYT44yTmq-4DvNIIW6C9P61dnptYKboDarLhnNE6kj4WwYgkZbuydQyLBjFX8A8Xy378B_y7hZiA_-gWn4wYRljjZtKpS8QIAa2H5XG9-Wu4mPPRvLrXTUN9kr4HQupklEnOFWK-kqoPNnvrfIlwEOfuLOnb9ovhW_CjvM0PvBOXcg5zFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۰ سال پیش در ۱۹۳۶و در آستانه برگزاری بازی‌های المپیک برلین در آلمان نازی دستورهای خاصی صادر شد.
مثلا گفتن که دامن زنان در این مدت
می‌تونه ۵ سانتیمتر کوتاه‌تر باشه،
گفتن یهود ستیزی باید کاملا متوقف بشه
که وقتی خارجی‌ها و خبرنگارها میان،
بهشون بگیم این حرف‌ها، فقط تبلیغات
دروغین خارجی علیه آلمانه و واقعیت نداره.
یا مثلا دستور دادن، بخش زیادی از نظامی‌ها و پلیس،
با لباس مردم عادی توی خیابون باشن تا جو پلیسی و نظامی به نظر نیاد و عادی باشه و نشون بدیم آلمان نازی اصلا با تبلیغاتی که بیرون آلمان میگن واقعیت نداره.
حالا توی جمهوری اسلامی این چند روز
زنان بی‌حجاب رو ویترین کردن! و طوری وانمود میکنن انگار ما اینها و سوابق شون و دستهای خو‌نین‌شون
رو نمی‌شناسیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlRCoiJAHc6NHXIkknbuBudeGyiOgsMpL49CVDsr7y-mNSPC6St9fCkNl_bizlzAPmeZ4agApeyxSg_PfBF9PDdnKV1FbOf812_QlAmIN1h55jb-4PJJG8BZxVleCarJQ6vKbfH-53q6ibTuUTystKq4eHugEU8pNsbWc6tkBBRqvpP7YcT5KFZu6oTTWThWh7436kRMgyN7oeyXqKJj18md72PvV9c9NDJko3tI9NC4fgnUNzt03KgAlr4IRKdKCcCIplBe3akJtFkPpve7Vn7H9tQbazjqiYuh_k60zShgp8YQk-bHlMFREWlnVfoZJ7QFrx3dEwSYBZFEKXLBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFnvfZwDAbuZpdewdA0wDZ8OPyymlkl2c12qaPqqmseofn1mDqa5vD7k3u2IfXwPtFfPbDxb9WYdrVTdg3iobPhywuGhm_ykxpr4ZP6GcJaaOwNHvImLxWdnS8vTFzN20u2K99W63ZIzSAoNy9Uo_7KaM0eR8gG10e16MQHTfQy1-iNFth-0xRMq1U8Wip7vWhgim53DGGLQpcQiXqLeyoybNrwiQHTdR9KgqxjVIK1GYGIzxR3tyP7SCVHGC58vNNLkOUysg6av43sUNM5nh0r58lBWxRcwzFsp6Qi7KChjIVN9-2YkxiwzZfL_of9YrGD6yNlm81LoSS9Rw5qU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7kkbnZyiiOA_UDTvuhu2Hlqg6reU6cR4SF3Rc-FCv9bd4xS4_bJ19ueNJ4dphJyqktFqlfTF9FkhjRsA7bREU5zXXo7F-V1WRGzXCeQ7G-x7pxx7zG_zY4p4QDAKxX6jdi5NQXa3ZgU_pkIbfX8tJSsdjFTMtcuicOIOYXsuAbc0ERRsllmIixW3iWnlcZ6hywYAESsqAR1KZAfN8nYI1KGDdPoJHnZoTahww2gElOntMMOFdq5yMu8lNFTJayp6fj0MrxiI476iktpsGfj2OFnMgQqdA-lGvj8uYsWRboG_dUvc7YAaLHIo3v7sIDrVpWYwhXRmUzV-1THc21fiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ‌دست به اخراج گروهی از شیعیان پاکستانی مقیم امارات زده که برای جمهوری اسلامی تبلیغ میکنن.
🔺
امارات چند سال پیش یک وام ۳.۵ میلیارد دلاری
هم به پاکستان داده بود، که چون پاکستان
آه در بساط نداشت، هی تمدید می‌کرد،
که بعد از خودشیرینی‌های پاکستان برای جوش دادن معامله بین جمهوری اسلامی و ترامپ، امارات بهش گفت سریعا این بدهی‌ات رو پرداخت کن!
که یک شوک عظیم روی اقتصاد پاکستان ایجاد کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/4880" target="_blank">📅 12:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdZ_fyw96Gnafh1E7sOMw_ZAhZSzTLw7UDj0RlBRzI13O7H9Zm-iU-LvJn10B_dzqtFc-p-HSYqFtLh0GMWjS9-ohaVvn3XcjUE8DeMHYoGYeVr5lhQB1AURlVDqtCYJ7CYlxgxSG-ln8hhgEX9akgr-k_M3C--28wcPjUgRIh-TMmzB0_pTpeNsbZ6SU7hSPclLH_lgl7WXFLpGxhrbMkmuiz_ktL5yXxa335SZbCA5vAuC7CxZ6iuzQECcnhY2kCKxrYnQZ0P9QOzqkd_oy8hiYAYeFLDOKNQjKAeDMxmNlfON_fqSjKAku-JVKHZE85EWzOAytXtXaY8IlsvOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت «مبعوث» شده :))
این هندونه رو  این چند هفته حاکمان
جمهوری اسلامی زیر بغل عمله‌هاشون میگذارن!
که منظورشون چیه؟ مبعوث/ برگزیده شده برای مبارزه با آمریکا و اسرائیل!
«قوم برگزیده» لقب معروف و شاخص قوم یهوده! برگزیدگی هم از سوی خدا بوده!
اینو فقط تورات میگه؟
نه! قرآن هم اشاره داره بهش:
سوره بقره، آیه ۴۷:
يَا بَنِي إِسْرَائِيلَ اذْكُرُوا نِعْمَتِيَ الَّتِي أَنْعَمْتُ عَلَيْكُمْ  وَأَنِّي فَضَّلْتُكُمْ عَلَى الْعَالَمِينَ
«ای بنی‌اسرائیل، نعمت مرا که به شما عطا کردم به یاد آورید، و اینکه شما را بر جهانیان برتری دادم.»  بخش بزرگی از کینه مسلمانان به یهودیان از  شدت «حسادت» میاد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/4878" target="_blank">📅 18:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQsovnqS_mQSC7OoiEo8IPArjGgyiAcegQ5VqwBH7NHm5rR22Tw0ihMfRq0yyXbwyDJK_YBpgnPS11aR-4rzZfJCiydNjmaQfTAUB4owc2VFR_smJzUF3W93ahJrB5c1zEKWf5XR8_Z2Fe9tQ1iH8H7uvD7C6gWa1ldluan_1PAesvvYyavqCD1mYRfOtNrEiyOTrpNeMz6UFUwiNihOUd53asiwSJ4GQboYWCjZmA4NOGSc_65cF2PvP6qKSgHTcvB3wch-oPlOogtRZtAid1kWKPB313GyTIdBH0zwV__MaupVSG_BRLtnlgtTI0-zddaS0ISLMbz53TsRBb7SEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط واسه اینکه
روزنه‌ای متفاوت داشته باشید :
در قرآن بیش از ۴۰ بار واژه «اسرائیل» ذکر شده! اما یکبار هم اسم فلسطین نیومده! حتی به روایت صریح قرآن (یعنی
آیه ۲۱ سوره مائده
)
موسی که به‌ دستور خدا رفته بود قوم بنی‌اسرائیل رو از مصر خارج کرده بود و آورده بود تا «سرزمین وعده داده شده» (فلسطین) رو بهشون بده، میگه : « ای قوم من! وارد سرزمین مقدسی شوید که خدا برای شما مقرر کرده است، و به عقب بازنگردید، که زیانکار خواهید شد.» !
يَا قَوْمِ ادْخُلُوا الْأَرْضَ الْمُقَدَّسَةَ الَّتِي كَتَبَ اللَّهُ لَكُمْ وَلَا تَرْتَدُّوا عَلَىٰ أَدْبَارِكُمْ فَتَنقَلِبُوا خَاسِرِينَ
بله! پیامبر خدا، موسی، به روایت صریح قرآن ، به قوم یهود گفته وارد این سرزمین «
مقرر شده
» «
از سوی خدا
» شوید
و خارج هم نشوید
!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/4877" target="_blank">📅 18:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
🚨
🚨
🚨
خبرگزاری فارس:
وقوع درگیری‌های پراکنده در تنگهٔ هرمز
‏از ساعتی پیش درگیری‌های پراکنده‌ای میان نیروهای مسلح جمهوری اسلامی و شناورهای آمریکایی‌ در محدودهٔ تنگهٔ هرمز در جریان است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4876" target="_blank">📅 17:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEYqGiD9la8EcQIz_-Z2dRqt4dgzM_V9N3hGa2Ai-uQ4yXRXC19ivVEmuj3yqIlcoEUuNkHSES4Zp0XY7hShUp2FYehyXfdS0hH-IpWTJ37twxWE5HgtfCHukYoBK8rrG3eJ_TQpGt2C0-8ENCpXcBw6-9atxI-6Pnkx1kbDA0-N4iv0geHKjvgYap4sQAS0j9QZp6VAwU1ouGWqCd1xE81YYC-2b-kmgMLCqqENBfIh09BQHj4vEHE4b-5uuUaf9CtlHMCiHHvO9nUaLRu_WbPXeUqi9TZIay8dyakvNS-SZ5rC9EAk7PL0M3TzF03GZ4_4bkDYw-qaE-UKKbCY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
