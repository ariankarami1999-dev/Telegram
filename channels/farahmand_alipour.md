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
<img src="https://cdn4.telesco.pe/file/lk9nAbz9cDn0Ek948hnOI4XKAMDGgXn678-DZbg0N74Azp_eWdmiaJTHB7bmkMDOALOapS5GGGbsT4ha1WJGA0REkIg8y2qBWMWlPjLPQscxmemO5cOi5VP3o_2vQNnH-JPuXIAONhMJ1wvPni29pxFmffmWNKRro46c00wP78VGnk1YUxuqlmfLjXhCDST2VDE6JLpn5DdPQJ7Sftv2pA1b_jeLqfqtH95xZd-FEvWKY5KZ_zlA3xC30JlKKOvILASM5xC1nslc31pAJuOeV8jKURa3xq3uQF7teWIFBZkc_pSHLSXsh9OnA-4OoAgPCPIvok0Ubm2tAuNmI7kpzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=A8uFMRkQpBki5xZH_HjLS8Hxhs1NZhqKiQ-igP56kWc8V5HBC5JEML_U_NpWIJ344bpwcPzkoqku5hJ6x02JYsG133awg93KCBrz7Wo04dU5vyvEGyyPZjKxx-RouMvc_qG52pp_pN-S5fNMObAg9TImDta8BPVA_3v7v8oyTi1o3O4298CAaatEciKgNxdB-XckzUuEDKUIk7dq1how9JPFTPJ2QGDE-Jv0tnsJpDXpOQSoj-1ZDs2olMcX2h4RsLk4Na8730Y4-z5KFvkF9c3q4CVAbShRJKv8M7RO8CyNoXE_SLgtQd-LTHL6rA7JGfjC02op8hRFsHzcveFitQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=A8uFMRkQpBki5xZH_HjLS8Hxhs1NZhqKiQ-igP56kWc8V5HBC5JEML_U_NpWIJ344bpwcPzkoqku5hJ6x02JYsG133awg93KCBrz7Wo04dU5vyvEGyyPZjKxx-RouMvc_qG52pp_pN-S5fNMObAg9TImDta8BPVA_3v7v8oyTi1o3O4298CAaatEciKgNxdB-XckzUuEDKUIk7dq1how9JPFTPJ2QGDE-Jv0tnsJpDXpOQSoj-1ZDs2olMcX2h4RsLk4Na8730Y4-z5KFvkF9c3q4CVAbShRJKv8M7RO8CyNoXE_SLgtQd-LTHL6rA7JGfjC02op8hRFsHzcveFitQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMPBtqaOtaiRMApZXl_vXIJlLK9tl7hjDM7I_6x-HEwFq5Gp-k-TfR_TkGqVQxNrz61l1-InDzVwWD4oouL2PNhzz63sqOhG41d8FLE2YuQ6eT3wEdTr6GMllIwWN9IsSBq-ELmGxdHYTmlPwlgpqmhzm3zBm-oyN5sDwprIa2ZxBi0_3rvtSyjpwOi3OHYNVvumG3exUqQoDHs-Cfrd3vuw1yxrXHV-e5T-t-81bpvo4wjZQZg5Di-AABhnkgBTKFKUaBtqfbtoZseSXZ64nYBk93NW-uXFilZzCC-WFSQxwIeEkQgTKNd41Kj9Pu5Kifj1qvZlKSRZAIO7jOlEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3bW5-znPUbz7T_mEDYd2u34_9RLx4tJs5lx_UZLZ7157rPzqG6sdXxE2NIZpOKh4Kq0279xNU5Ph-uRr-kXi4gLYbhWr5OfDzBssxAjDQb2cosaVWmVbUXMkBiEcUITjqwsZld5Mu7J6KgjL9a8THz3jNRGQ2Fc33y3Pz1EtH2HAQWDALmncL6NaDO_MjYfg0IMR2989zIUeqwHDxzjjj4DeobnB_-pMoyQPogMJf6ozbumqfmq32CuVquLDhHrXS0qrOwXEUz5CcNxR4W1dbUhmSeDxNVn5jbojfWjY0RJ6u-7HmRbQIWFM_mQgf5_AW0AMXMLGaLlkVC8E3qaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvlyJ8uC6t3SzPtwYFdFwkfNQ11cYhD1SN-g5ZOXQh59YKzFG_gU_u78Qfa5HtIVO0-AjpTDnWNIka4wC9MnTPYANCQBwqYDzBhAjiUO7kHkpBau4Nx08SfudOWeTsCDy1o13GjIZbeo03bEzLuZ5I16uBpD6sge8_wnhgavG4D6XDeqxD8QIT2o9NxvFyHbtJY6oR5kQSF74yUgdaFrT6tyTiWAxkYGLpxWPe8_Ad9ARHXsNFkQDy-g2ItCz6udqiXqb6v2rvvK-gTjx82UnOLh4b4SzudLnE7F5piWNLR8n6DglxayQw9S8TLnYN5NIcs5UunfW5UhCAJOP5kKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btJvpq53TuFLqFLcPFEWQzZ5BmWzTeHub4R_sIb5TV9Flme9zlAeGlwO8MtRoNVtsqlGf0GVikyR7CaVhT1eR3UResWxl-3UYJfx7x6ZU1-9gqlMoXWL47zBaVGE8vuOpKboqUGwuxIImbWZFXwJeImtFjgV5jRGCWeD5OrSehOPqG_c4iXjdpUHCojxYIW_MzKOMPJmI9hwk-B43R0XPPGcFFayi78TgnMjwA8CS-XU2FbSWAynrhlKOuLE4XaJ1V4nmzjNUafL_ZM6itAWXFw-Mr2O9c376cF9JSLybLB2Mnuv0KUBp0tg4eILsYiUc9RJDJfdn8-7pKiUwtEXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=nbnWplrITpTJSizK2Wv1HnADWBxQuyQDihxnDNyvMV45pJdK9pQgovuKywL-ND8vdZIQ3JClYv8BYQQ1Ezkj2xsjs5_y0hzbVXaHK6jKPUv16Ny2fuQ91IkGklTiXjz-d0IIbcQ-za6ZfEQt5n35sOlJK76zdNuY_a9rgf6HGI6wpVCD4VsdpTJMGvEbBSyJQekSnYgoO8_HEB5E2zllV0n3CkdSOJGChQ9Y-MWVDzmBimGhQiMXKd85eU9sgq10I9o9uiThAhRk09w_d8vjwjmE6h1UMLLMHIbxjac3wiqB9bX4Xj0RLxOVBinye9TO8aiyosBqSUwaMkN3be-kaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=nbnWplrITpTJSizK2Wv1HnADWBxQuyQDihxnDNyvMV45pJdK9pQgovuKywL-ND8vdZIQ3JClYv8BYQQ1Ezkj2xsjs5_y0hzbVXaHK6jKPUv16Ny2fuQ91IkGklTiXjz-d0IIbcQ-za6ZfEQt5n35sOlJK76zdNuY_a9rgf6HGI6wpVCD4VsdpTJMGvEbBSyJQekSnYgoO8_HEB5E2zllV0n3CkdSOJGChQ9Y-MWVDzmBimGhQiMXKd85eU9sgq10I9o9uiThAhRk09w_d8vjwjmE6h1UMLLMHIbxjac3wiqB9bX4Xj0RLxOVBinye9TO8aiyosBqSUwaMkN3be-kaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkQFqqRcsKfbmtLiXb8yeuh1buDJXGpfYy6oU3T-cemFomf-K5owK8D0oC97TxIU0v2nhfKXehHTr8MtmnvXs31kTctCHUvftIvS-Ioeh7jGKyM0MS80YuEoLsoApESMdcJGmc8aioVg75OUmQZmJDyT0bKEtCttIqMhCybsPVAllKyt5UzDGrdzDox7Re80izfZ9cSYVTj2AzXzi6dOc9Tr3lyY_2v-IbyzfR2DVYNWMec7eUOgWeTuIgICeZsJNAzf0XQ8lkbIQ8T8tL7PueuCp3-NaCvmcjaMrwAuTrz9Rw1gf-bbhv32EKH78wZMCmKyOMX5F2xEqv4ERUpTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhz-5BnrPY5To2QcI4rTr42HJWyZdnFzkMR6L8tIk-ZlEFfvgp4MwjovRhsSqF4faseXwea5MvzjtXV2v3pcmpfw66Uax1JHoudZuSSJnwfyl_e68rXtZfK5F-ANyWoPPOOQoRF0tQK9MSkLThlVNDQYO0dLpNgk4TYyhjbZMmqdYv1WO09uJ16u5GwFm9zZFqEZPqNx_NuulItjKlVn-HD5x4oo1MqCNeuQItMCDVc17kcwmhQntQhHKUe1oZYOtkrs4T_KNtgDA27_9qab2c-L_xD3pm3GqL4xIGjRJrKLcZuBEtTTuJ9rkSPaMY_p3-Ws9OqfrscvfuDk9bG3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=Fd-c25WxiOmbKb82CcvNmnEJEsiiTnLXIBtrDa-LbQS5QU27DDXQnRa4lpbpzWPyNb8ybXuaMRNxeUjKpSNGSQoItlUyM1iukilba0sDAxfGnWB0Hve8tHOFnyMNI5gDBnAAW1EnLj2mkL3FahhRBSfv-eZmU8hZGH5BuqABXFDw08quxdbV8azt6mTMG2XVvhPm-F1dJtm5p1NkPtC83v8OymZPPOFmZ5Wo0wnrE8vJCLqilLsBV373HJjOfOWb9pn9zB_34gN3u1xICW-DblYglWZHywINbSZjYSRc66LS8nqXWrh06TXALMJwmj_Ji7itnUwB5HJjzVP3imnWeE3R-Arm8k2yxur1GXGzmZwTdF7gcSeLwLpaCPaL-UxTYpQ3VFzfVJpsxuB0F2Iu2hl2-rKnGJyvWLncq2O7AnDywXvu6qaMxORMVHp9NMJga8ZPv0dUJMrWDmb0RkWceWPtBnKONbDY5K1v1I0zqhHWGtVmT0V3KYCNJ4szWjMMnh32SBrDWlpEucjsAx8YrccCz2jTjMRJbrjb_CU7sTqI1HOYrq1vuJ4f3RdCmArcxa5aUzlmcqYNQI8MthnOhEnshrG2Jfb9ivUZz7elYa76b1EPCXoVvHi9z-snDhDmHBsaKE4euXKpMpd2avV-xegPKPxMQzMgZIUrUto8I8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=Fd-c25WxiOmbKb82CcvNmnEJEsiiTnLXIBtrDa-LbQS5QU27DDXQnRa4lpbpzWPyNb8ybXuaMRNxeUjKpSNGSQoItlUyM1iukilba0sDAxfGnWB0Hve8tHOFnyMNI5gDBnAAW1EnLj2mkL3FahhRBSfv-eZmU8hZGH5BuqABXFDw08quxdbV8azt6mTMG2XVvhPm-F1dJtm5p1NkPtC83v8OymZPPOFmZ5Wo0wnrE8vJCLqilLsBV373HJjOfOWb9pn9zB_34gN3u1xICW-DblYglWZHywINbSZjYSRc66LS8nqXWrh06TXALMJwmj_Ji7itnUwB5HJjzVP3imnWeE3R-Arm8k2yxur1GXGzmZwTdF7gcSeLwLpaCPaL-UxTYpQ3VFzfVJpsxuB0F2Iu2hl2-rKnGJyvWLncq2O7AnDywXvu6qaMxORMVHp9NMJga8ZPv0dUJMrWDmb0RkWceWPtBnKONbDY5K1v1I0zqhHWGtVmT0V3KYCNJ4szWjMMnh32SBrDWlpEucjsAx8YrccCz2jTjMRJbrjb_CU7sTqI1HOYrq1vuJ4f3RdCmArcxa5aUzlmcqYNQI8MthnOhEnshrG2Jfb9ivUZz7elYa76b1EPCXoVvHi9z-snDhDmHBsaKE4euXKpMpd2avV-xegPKPxMQzMgZIUrUto8I8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=B5fnVtnz-zDq_qaGHzC9YM44M4_7atKagBNH1UJH035cpEy1wP6DYKK09waQJxKbsUk6ERjw0yXwXemA_DCeCxIRFMszgzJ_x1K35iQ_-80WN2NBxf3Kj2-H7Mt9eUD1DC2z8rH3bUhoOAVa_2bCDQfbobS216U74v3ShPLFrtq6CemKJSrTea1mZaPWgJgvrSdBQon1sSWYtusPmmjBMjt2M8ABJrrMaTfzLhnJig2XnVbh5iFobd4n5lagx1SM9DOCUvUOlh7y1lCpYINaKGXknkYeJBqfSz6BPn0wR7O4JdZlsjGgPBeen-IQ0-peiqSsYjoZpSUIUKqdRedEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=B5fnVtnz-zDq_qaGHzC9YM44M4_7atKagBNH1UJH035cpEy1wP6DYKK09waQJxKbsUk6ERjw0yXwXemA_DCeCxIRFMszgzJ_x1K35iQ_-80WN2NBxf3Kj2-H7Mt9eUD1DC2z8rH3bUhoOAVa_2bCDQfbobS216U74v3ShPLFrtq6CemKJSrTea1mZaPWgJgvrSdBQon1sSWYtusPmmjBMjt2M8ABJrrMaTfzLhnJig2XnVbh5iFobd4n5lagx1SM9DOCUvUOlh7y1lCpYINaKGXknkYeJBqfSz6BPn0wR7O4JdZlsjGgPBeen-IQ0-peiqSsYjoZpSUIUKqdRedEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5kACutvpkyY3sNxAE17vhfygDp0_U4Gpk17VX9ydYMbkReSlIEumOIdAGajs6NqkqrhyuNrJgqu8q30stWVyv0-v5r7Fdi1oQEqELbiun0h8U7pM01qXsf6PLqlHJ8zr8EI5rsPGJ54MytzEIEIT9Wmiu47yWv_vaFBMjjQnyjgD2nRFkyAKCk3uYgUThUSIqB3KNIpme_38c4rdFfFuZhqW9H8j_fYDTFw_rqfBHh83qd3GgRY0q2JPhElvPd-dEhv3opYyt9B8zAPt5p6m1GQsKq_b2tAyMJ2QpMVP0EKrdhcJzdL59v5EqqwDQW9gRfUjx_Iwi75591lhfJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=HGeqA06ATJezy5ZoHCQCoBShwS1dmQ50SHEO5KvXcQ1Gyl-0Wx3nAKHRajlVeg9jhl_4jvp1DrjICughROc56PwHC8nJCt3dYvnEX6piz1FpVL_31LDM-M7BF57tMJvwWCmA1gcVypvHEH5M4a0jEZZkpeGuncL-kstA-xlGiREYRiJAPAHJ1TukEZHNgttTk_tj3t_IWlWDC0goH9UrNARsmyr68CDLBKcnMcpQptZnrZbHbyhw2PjjwYT2LL93wF4AmCgVXokfBW-AEPPD-gtWjOYImFXZ61_Ell5ictNHvdDelZ1bCS6B-Et2_ewIjlX5QJKNI8O5DksRdVQ8bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=HGeqA06ATJezy5ZoHCQCoBShwS1dmQ50SHEO5KvXcQ1Gyl-0Wx3nAKHRajlVeg9jhl_4jvp1DrjICughROc56PwHC8nJCt3dYvnEX6piz1FpVL_31LDM-M7BF57tMJvwWCmA1gcVypvHEH5M4a0jEZZkpeGuncL-kstA-xlGiREYRiJAPAHJ1TukEZHNgttTk_tj3t_IWlWDC0goH9UrNARsmyr68CDLBKcnMcpQptZnrZbHbyhw2PjjwYT2LL93wF4AmCgVXokfBW-AEPPD-gtWjOYImFXZ61_Ell5ictNHvdDelZ1bCS6B-Et2_ewIjlX5QJKNI8O5DksRdVQ8bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5ycmA_WnOurlrL4y24QARfzvxjHj3B-CvUcZBZ5dxFAxXUVqcfPiqhkJ6SfMdbeGlxH7AQEBF1jdwXTiAMus2wK5d1KPgpsL_cXp5RzfNxUpqjOHRHT7QezKgMhlB4G-CgimUC9gbqGKLha5so3J7DHqFN10FBstf3xYITgXizr5P5azyf0-m59HI2ZROcrsRoWav9n-Mk7gsEK7PRMYRo0F3z9zmNWMLeUze0Aah8py2Lf4UY8OrlZTWeiXQSWnGsqR8kVKVdYhiUk1xeYLa1keKEphTa_BQwNx4E-FAtOpowVReCJMVx7lPmvO-vCxAa17cTmmWlrc1l_mW85IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=tm2bcvQLJoQJHhw6g_5QtoqvPCjla7NVCSHoGI5PYUWOCRMsLFFi9hIuQqI4nbkvyLmoAivVnIXYqscKrbHFcdoxJmjRJBr1z0VoccZgLeHkkLJE5AScl8F-mR9e5SdLgxQj2K9Tnfz6uVS9fYSRoV4e3ZI86qOw0DOmzsJ1v0DWPXU94QYVk0_UVZ3x8JRPgGpJS0yvTtSqVffZg--GGjK_kzvURLcnTTuFHMLD1ixWsC49h19yCCT0yLVlirzH8xdGG7sk5Ae4QpU_nr_4ROQqWxQjLLUX9YMJ86zTMA5nNxGbi-vIG-mffTOdQRDbWuwJdbm_AeZmQjM8I3Gt0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=tm2bcvQLJoQJHhw6g_5QtoqvPCjla7NVCSHoGI5PYUWOCRMsLFFi9hIuQqI4nbkvyLmoAivVnIXYqscKrbHFcdoxJmjRJBr1z0VoccZgLeHkkLJE5AScl8F-mR9e5SdLgxQj2K9Tnfz6uVS9fYSRoV4e3ZI86qOw0DOmzsJ1v0DWPXU94QYVk0_UVZ3x8JRPgGpJS0yvTtSqVffZg--GGjK_kzvURLcnTTuFHMLD1ixWsC49h19yCCT0yLVlirzH8xdGG7sk5Ae4QpU_nr_4ROQqWxQjLLUX9YMJ86zTMA5nNxGbi-vIG-mffTOdQRDbWuwJdbm_AeZmQjM8I3Gt0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=d_0Ma4nFrOstLPlwWYH4p0d7rAUXcs2MPw2HDNrnAirM-RP0kSz-s3O8Q2OXmizkOgHfJ0qNfor6Nz_OupDu-AE9rLU76BZZgc2MvyNiDDq2RuBP9uNWUWI1PbF8Hdr0GBh8Bx2KheKjBlh0vo7Y94ac2gX62DaCyNKb57E-SFEusy4Gq50bZIe_mGrxRdTML_bwrXDP5uINtkVfvXP9K0FASR7bkedc93JKzRR2zBCvzTzUaPQlfPQLlkD_JvIvtFZQHs6R5ZbBjzrziNDhpUBpt7H47HoL5IjHritGpxFjiIDUDZYjsxBrix2N9EBvP6CPQIcCPvEMuXbphBkVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=d_0Ma4nFrOstLPlwWYH4p0d7rAUXcs2MPw2HDNrnAirM-RP0kSz-s3O8Q2OXmizkOgHfJ0qNfor6Nz_OupDu-AE9rLU76BZZgc2MvyNiDDq2RuBP9uNWUWI1PbF8Hdr0GBh8Bx2KheKjBlh0vo7Y94ac2gX62DaCyNKb57E-SFEusy4Gq50bZIe_mGrxRdTML_bwrXDP5uINtkVfvXP9K0FASR7bkedc93JKzRR2zBCvzTzUaPQlfPQLlkD_JvIvtFZQHs6R5ZbBjzrziNDhpUBpt7H47HoL5IjHritGpxFjiIDUDZYjsxBrix2N9EBvP6CPQIcCPvEMuXbphBkVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q66ai6HpeIZV-QaPO8F5WQvvdeZg57x6uLmKlXf0NlCsR206YmMrqIdl7EcMF7lxa-zo0d6FTvvYVgyzrwbHdcHLdvSCkyUauJ6vaCHmkutKbmDSz_JREHw1agLbsRa5nR74an5MJytbuvEM5seAuNTlyfzihogf6crTWFvRGF32zPRseEnGKs0eBnqh5l-yF_ZDUpoqoUqadEOVCR9sjEaVYV0jyWBDuc33Oo2i3u_jVqHqU9D3SmDt5kNoAU8PdSjobA9XiR9npfchwAQrsirnoh24RxAcfqkOtp_3GE1VWqvgU6VMTSIxVME2cJojhkiY_bYl9IO28BKGLgUCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=UDDIrcKtUREsttOvr4F3AEeVIbyr7tFX02h0C5Oak4eJU7_pRXNzTzYBTb8V4JG49e_P3PYZNHfHIdqEzOaiusaTynqMqAKJTOlZhQTf2YFuknk0WxAMSr1HxSOfuB8ZgR_KbJ8EgRYvMoXAza0rzv4erkWmcPnld8VmZmXMuNochqLEU9MrzM1Pj3nYtb6FTEm-aiI5p60-dZx1KOZb35kAvyrq2Am9chWu47rb_gQkZ-phT8CwJ9ONEjbkCodB7JZlcSnlA1nu61UvVzEKymrso7ZFF38kUYj_R8JCs7ejalYZyCfQC8jkL1_DR8tDYvpYNrtCNaveQ--RND7VRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=UDDIrcKtUREsttOvr4F3AEeVIbyr7tFX02h0C5Oak4eJU7_pRXNzTzYBTb8V4JG49e_P3PYZNHfHIdqEzOaiusaTynqMqAKJTOlZhQTf2YFuknk0WxAMSr1HxSOfuB8ZgR_KbJ8EgRYvMoXAza0rzv4erkWmcPnld8VmZmXMuNochqLEU9MrzM1Pj3nYtb6FTEm-aiI5p60-dZx1KOZb35kAvyrq2Am9chWu47rb_gQkZ-phT8CwJ9ONEjbkCodB7JZlcSnlA1nu61UvVzEKymrso7ZFF38kUYj_R8JCs7ejalYZyCfQC8jkL1_DR8tDYvpYNrtCNaveQ--RND7VRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERM_zUja8WTR8Dehv6-m0_w7Ek_vtlq-JjVoEuVwjkfHw6oiYquRXIbZb78AYZ6dzLbA9dWB_7y68W4M8PbeS2VzEsngMoQQ_hi9nD6SnCC-2rlnGWHEpVZJ_cvjToSCvoXLzeyi32ceobr2S7i-Q9UN21fYO48lte-upYuan8Ox2EgeAsdJFmBwongnL1oXYCW2NkqmrG8uNuGCEd4HjFFolO3xW71RO4IHA0XYRYKoS2d-iM8XgGfkeKSdhgWMbpFIZkILdiY8_2lbprUnliGUUpW-3VxqfUBA9PvKTnCOLmv_PqKd6Ddyg6ZAJQAFBC4lPLUU__sKKXvlDUwIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCrdeQo7qW9R2yiDrrlixbDQBk0p4JGxiZSHXPJ4Pg3pNk20J4bxfSvF2NxCVJIbh9lhXocv7mqiav3gTLyGSCGM2ohMiT5GFaG_uwWh9Bde23kRQgG9TBt4lGwPN7PjEGK552FnhV07CXJZEn98sQJGDfqzZbP2aU6kFrW-Yetbr7YTEtOjge53cJOkzGtK5vMAXjhasvhScFw0YCmV2BUFEAEyX4uK3awFkV3Bj7VSRKZH4n-YSblV-nFwqbruySnKE5QIGbMpySwofPzKV_jQaR4eOcWMiZaAyRlXk4F5I692AGeuD2ftaSIr51gRG0Yi7UMJ4hXhFmHG91zT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ec2-UDCINoPi8QEKxBP_EEMV6DtaIWzNKYwi0-R2p7wbkcVJAoYXugfg2FB8jgVS2-VdPWrxF6robjNLdNzGcXPPw-J8fuF9bQO-A_TBaHzxR-1A38vEDKhyPrhx4cqVR0FPGzW9kCm6V0hBgAK9vdJr04SMl3qX1P4IPYROLvBSHY2pbnAHqF7ZLx_X40yncGdwFy-MBxtaxeR67UPWPO52dA0tVqxv3-ZyRWUiyOef1P7mbFQ4S1vSnOL4Rki2gS79sEnuiAeNr_Mn9bxEjoOBAixyqCQToalbj8J3CHbxKDRx7oEqis0xc8JhQ8xhAHPVleOpKS_-oykjZRCtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAA8S3fFwLrHsUWSR6NOj3Qdmufv9uKN5Jo4BdIS_zjnkj5QGSTjG2_z3fZMk2GUlzDqBRyY3unaGkAIglR-ZQsQ5K1LO8w7fxnB_xikkLHedTyRl8GBKA_vv5OuO-MzaWqac2btkX3nR3xU4CdKG33omr4LF3lGaOIxnm3VpzEBNhLuCa7DoYYBJzjp72Q8rZ2H570bYF7ZzZYMvmtnnodyOQlPv52CyjGG_0ihT-dr0mZWDOami7YVlNrHPOs8c27MTWjmwiwsJJH7oHLlq6440a_ry6jjycMcL0jaHukFtr5uOJ7KJcSjphGkKsq7jUIhqzvLycY2KGfEep8Rbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7Pn_dK9W-jhByFJna0uhB3T__gKpSceGtuv9I_nCW5QEDyfzC_-o5WQHQcHd0YerOrw00pXADM-w4ozizctyREme9R4TQnZ9SN1QVyhbrgtkrQ4XEyRX7UChsg9OHKNo68Y1svf-5uL2pe6Gjnp8StOFbLp4skIC8uMwbx1BkjaxdxBnQLd__TqyeIUT6tHZQnIRxS-dLZG9Nsafl1LMAl-ZaaXoEpgWt84t7bkrUgmiQZHlbHBBTnxfNu2mRYRdmVmhYVYIP0NG3QIqGLKnsD3tWECEWdXaTqqsub6ddKgRIyxpRdbsbUciEZepAKr1etpuPqjK5jqLnz_ztVmPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeM0uvLjFYCBWzikH_rl_kERYw-AivajMFMArCcUZay_wESTfWeH1BD9sqXZZI17N4_-uAETC8EXrijYrm2MOgmlLsT1UaG23BUyuCk5QWm2_HwUIDMx-7Z7hNrqNo9K_jBdkFfymAQ1LPBW5Ssdyp1igS1yY2AUdMNBOQWC0DEFGxNaroN1Q1QkbwyF9_jmjZzQN49-yDHfEyTTsNGYyrF8H47StqdlkHBSDJ_E9JVbrNVXpQRwRH6G2mVE8sZj77FIbmfV_7d7GaUWYSvdlvy0dTYoiWCIqf5wC7BUdp4dzMRM_f6-4hRkI7_REVJIwRLn3GyHM-69c-BkicPfIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=VlSAgo5rbKjhz7TcjxcM6gzwHmSkQjWUG09OIIN2fKE2kCuUmt9dc693KRh4GZlPHuWiweGtQ5Q0fmMIlZuLZfL5w-_GLrVLjKTLa2hDfRbDvtYZDOL6bq8mIsX7yZBnDkAVOD3U0jktxNTucQM8dfe9OQ_GbmvGc8sWbo1WHfR-HUfthkDX-FInI51SCzKFh8Kod8vSZ-3cIzN4jqYd9HbBgZIRAC-qOi6pr-BciQ0G9fhJOvW3MJNpk6Wgfaw0RJA-2gFxaLomekKWzZBpblvCkqDjqjTAONduv-1vcZCDmGj5b0bd60aHbbNyyLBDkRg-xSHttdFy7pDY88EHNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=VlSAgo5rbKjhz7TcjxcM6gzwHmSkQjWUG09OIIN2fKE2kCuUmt9dc693KRh4GZlPHuWiweGtQ5Q0fmMIlZuLZfL5w-_GLrVLjKTLa2hDfRbDvtYZDOL6bq8mIsX7yZBnDkAVOD3U0jktxNTucQM8dfe9OQ_GbmvGc8sWbo1WHfR-HUfthkDX-FInI51SCzKFh8Kod8vSZ-3cIzN4jqYd9HbBgZIRAC-qOi6pr-BciQ0G9fhJOvW3MJNpk6Wgfaw0RJA-2gFxaLomekKWzZBpblvCkqDjqjTAONduv-1vcZCDmGj5b0bd60aHbbNyyLBDkRg-xSHttdFy7pDY88EHNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlU6awCkakH8EW5NKqoAbrCdPiYyQMiuhBIkuVHIoj0BO96hEWM2RBQEuOiAcRn_ioz1N9pQavfb_J6eZKWT6IF95U3gEUKC2OpvTIXXc6iJkUJmkxwF3VWcFv6SsOo1j-cdIhWYrwVd0P-MCAFL303i1sCPBOD3OhLHBLSYErLsdSigJDTiMKfvvnAuSqKtQvfmJ999AnRN6DqFocVvaptD1e9Dq6zXflE7njL919Lw9ElLNoXt7UAXBdjRGHkHJf4i4E63u5rv74i1fVQExSxT93wG2KHx-3VNZ3ARg5rzm9oPBInI704Gc0ZHtlaWLP5yJ2-JoTc07YluKGaNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY4UaQP15OLvO_y2PRtMKo7VM52moo1mLND68GC3ZQ_i-7TUx4h-4rKs8tQHacpJ8K6JXuOwKkB1iI6vCjXk0SEqgnm52V-JLJaY39CFecp3u1Sbxt4GrK2gDR2NnNPB8ocFyRUdl2_YmB0iERFEzUpTR24V8EsIxqGR2UICTi_JfPv6PYlmWYhY8Qd6w8_Gi579CKmaA5QCxxI_0HWyU5AvaK56_UzYX9UQAVInuZbUkTzOhLTppcGfeDxNPU6teaGzq3ZTe9P8ebjzg5K5FVWlpTHxQOaMVF_uWc8SI8V4CNSFW7aiZnCmOdlaTdYuJaruxlfhIem8MvLoYRhqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imw4L29LObmynshDQ5SJHTWr7CyI-rUp1VddKxbzEYvFqTqXgdSFeGgMi2XTy2NW2GR7_NDf8zk5hgaLSD9ITn_GufGJhgHcp8rRJ7BZ9bYF-rZcDQAPSAhg5U1fbgeh7f7QhB3aAR8LU1Mjqf17JoQeEPXjU5ll-cG9qiXEdHIGmKORkssrucnoS9oc-MQhKhkjPvhA90aLn-840YJtlNRmDk5nMHsd6ysGhTF0K6skfK8FQLks8Xbo4iwB8Q0TNHAbPunhsSjobu_Lnxg1vQrrXH2RnYDREYYcry-GfuTG3n53FvgU100Rw1ql3NieYAZvmbLXWheQNdQwOeYjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijtEmXxdGm9SAUKti36r0L7khLa0raajBSQTlrkmz9HmN00w9brs8b3tb2DpDOK4FIMoPzv8Mr897GpmK_I0f5Hid_Lt8sDozUrfMwf_uvdN48W6wu2esj5MxeIYTZSrlQ3Hjl3ZiHnJHXin79Wb43M72KFwRpmSX2WeVqNMBIdE-o_8xQ2H2qbRiC0h8jTNrLg5Bv_3VRhQp1FqTyOLjhZb0qaIDajIguu2vN416t6kbF45wCEdbfmVJiVj9kBu8h6Ct_t2IsgJtsXPzGFbDnvL9fLRLLOn8eZr1lEJsCpKYW1yfv9u_MgZ4p7kM8x7QkPXguhQ-aoK7xnMt30HNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=VC3yoyKmBmx4GWSwnOOvL82yyu8tpXXuIhPkhjlQJl0DJoB8U5VyrxRM9w1D3OKzrj_gfHleSMnQ9lvBOnFXl1xHrp8h2NNDRD7ij38Z1pv3iorCgBSEBnutkqQYwdELDAyZfksWYha94KzfI-0LEQICUj4wn9R0T4tbk-Im17gg6xftahz6c_b4gS4nWNph-6piLdCVebdvfCEUg7qITejtxuXCz3XrwMRiH2A7GVL2ibflFDI_KJv3xB3PLO4QamoJlK4IxYOteBNOra5UsS7o-nR3jEhVaZJmsMwKOgQsGpNF8eVOi8RNZ8xAfZSUbT5vn0eqTmliXlS9nq0JjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=VC3yoyKmBmx4GWSwnOOvL82yyu8tpXXuIhPkhjlQJl0DJoB8U5VyrxRM9w1D3OKzrj_gfHleSMnQ9lvBOnFXl1xHrp8h2NNDRD7ij38Z1pv3iorCgBSEBnutkqQYwdELDAyZfksWYha94KzfI-0LEQICUj4wn9R0T4tbk-Im17gg6xftahz6c_b4gS4nWNph-6piLdCVebdvfCEUg7qITejtxuXCz3XrwMRiH2A7GVL2ibflFDI_KJv3xB3PLO4QamoJlK4IxYOteBNOra5UsS7o-nR3jEhVaZJmsMwKOgQsGpNF8eVOi8RNZ8xAfZSUbT5vn0eqTmliXlS9nq0JjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXZhjKiuVkfm7zf7Mjj6u2ZH1syNRKj81LaWRvkQ12lokuK2H-moSxGkglgf88txREQKW9aKJPnRTSbyj9_auxIuNnISOzZ8cKjjY3HZWHxswdrw28mu1t6tD_gku3A5NJjeRfB0CBQ3QsvJ_VHg-dI-tHA5cnIHYJOOCcNPVRFVqz_GIDxEiRdTOJO9z2ww8C4wnqVnaAF2W-hUlCO7b2dzgEo2KkWuGmu9OL_Irg2KPNWD7cjcPQtBcz0RMDjkxk7J3YSjYLZlxudx2xSxIpvz6kM-Wj1mBhuQ0YReon2ZXc1Qc0BMufzqKy8ZrTqSQq5wq67bkWWI5pM4xa7KXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2xA1pnTgxq6ND-Ct6w4Q8uT2AYfTVAYs3Dk_ZKC26FX_EdoMi00_-r5_FEv_OfzeiGLjkqfZYLDplne5gJwqb2eEqJ8UfOnB9M7_y-hrQyc9IlGG11BELyKSY1FePxznZO-Gnw4bW6gKcZjE66pf-wI_S3jxZm3LAiZLwvs9lCektxvBf2Z7guaVH9V62rL_G5KpEEpPh35BC6uYdybP_taJb7huYaXciqKzD5Z4Sw8AFWHHuAztlzZb2BcUp-TOmKhnMKTBj-Z8zUtzJlO0BGq3jOlIeleLcASyqwgLy_tHQveN0Ty5qUKMiOYNOfKBVKb4AVrgN3PvYd-9RHR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNVi4cP-_wcvmBQCIUNnIQJR40hoWm0C3QX99Ed2NReiccq00T-n-yWSBFmhC41xkBhZsP3cElfMULevWc_hPK-pUrxXpAGgysJuYW5NuQFsa21LlBl86CWLXjlkFMRaDPGn6O6tAnF3zfLkGGYBCPYaY7elJCHxP9c_yD7qsGcKdfj6OhNbC_SGaBG3_iiBSRc2Ykmqzq0JM0eJu00wkPmgi911oPn9pstT3Tlq83DhG8zFCqT8AxrV_naz7YUzb7d3yJ1eXwLjo_Iaiv-LVeAalRYvvBaAJux-3oeH7stB1mAAT2QMYJiz9C4TDUTM2__AnL2LEA92rCCQa3l_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiscviuuxfannmYkiwEvYj4fcpkaKTWm9_8KAJ4IxL1gg5nn-mGbt5DbU89bLbTfX76qNaKjWKZc_y7CAbaMr6zjy05k81eF9dGGo76cy8DbcTBT66YiNuVJB6UE6TREu9LlDlK742AVuhDpeSUTOQD5-xXrLl3yGcX7WqG6ZcLb5i-_T-4qqpyYj9AAI8f9in1rwzaMZf6QPsK5OxG7bB10_KEXBOn-vmcQOf-Dt3KEn-JorQFjLv7PDWp7iaicWCXeLFmcQxfNl5ZlHP_XTDKRuf_ZNZPsCUq6gYIGNVGtSyYWFfrDvHqmSlLHk0-fcs0-s6i7SgfQFtd97VGcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYPm5JVRTdRPHTmw7axibTsk9XLU7wfRgvR4aAIFab9R7fhKIRXZKF3FodqOArN4yx3xH9UUp34FK0oR_OZqaayOyblLlf9zKQGxiYoB23dGITpOvf3Enk0Zy0fTcmETznuPTd6VlZNNEjShqxeKIzsTkXIn-pvPgvViBmAWuZnpDDpRdmrnMb3dKyZn1fIoV2a48qIbRuEUumtHQdOP5eso7jspofd-J_s09Dc_I0Sooib01NfqF0cV6Ka2lROgxlvYLBJptg5jbR7BvnIGBoFE4vfm-Pe1FRzxtdxwiaoXG4xy70m3HffEk9j3-IqihyLlKKohtKo4TPs9QVJp8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxHBc3cJ7g_CmUJ7QIcDNzwilcmBvzWqGCK7rnTokVbcSQ7bCcXOMfwrldYVrh1BQzkQAL3EY7bWAIIO3vlU1EC6BTqL_dPhEgNNFsN__YqQJGNLossK86IcnRV2JEi6eIUpnm73997-2syQ40pRq4BKiu6wDNfTrUDeHbBVPGx8C8b69_NP4ZSdNGomtzd0WNj-CqhUjowdSpYFDNJhblfzhWhaVPA77vHLFR6mt83pczaR1XtkHi7RGuV8rdxfDDoSgYcKpjO7CdwsVcdTUEJJuOeUUYaUQGXoeTravNXnIsDpivs9wgvqYivM94QQBzctRI75Cp1IUbv7MB5nKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8ojYUFCvrX1COKkBoC8pLap4ohT_nyR8537Ut7flWkxgDTJCGvHHy_8Wv0NvA22IZZagEWzdG5YMLlTMvmOezNMT_kAfbIdnnyJRORs8eI1PH3XxXkJ6UgK4XR9C5rYAeqnHIT3wH_e4ZhyIrNeirVN5-ldD12L5P3djW8WNIxGbmY5iWyuvgaaKw2jtS5FukbfBV9eQ_FoorPIB1wbMxdfx1y1o0Pk6IL5wu9Q0gxPQp6vLWbeUqof2R34ECPdxJpbw_NDM3c3aQDKsYDEacIOpV1J1ufLRNAOcJHsbx9IEkTyzUmDswMPcu_STeWBekIsAJVoZt7ryZS-ikS3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W107qqgvEsLytbiyf_pym8dSlq1meLARIClUTSHQJX5VX4UGBvHCmIIIh_EH4hqCbX-Mz5TlYOWpBMOsJzAVBcCJPph158Oca3RfyBFL4rbAuGHAHzSf839iyWQgXOdioOTOmSqyFArgyNpONEmfROC_4o9J4TKHzWaujTs8gLCb7C0ZGf9cAWThchmq9WKSwWEUdpREbaa9RsgpygcooKF2zMitRbPsupajUWVdM8kfHeyR7JM6YjNlXGxpNZaWmYsLJ1Wo-0CmVrf0QFYd4oubKF1JjSbsPirhZD9wjHdIVQI3UNJeYXg5ciwHgD65HzmOBHWAddYUCyrC4mhvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXyWP9V2Q6NewPtZ_iCxYh9e3yZhaZgH1UTwhAq_y5rRQdUb5E_8BJzzvNNbSKXv42b9DtuIFML9G1rU-MclUfRm8l3EPD7nhePYd-e8PGqENueu40WoL53SuwUtsSCRsZ4q9skEQ-vndHZojLA-r1OSqxxFPGQH7Wk2Lx46Vxca5p_C_pPa-f8lC_-RIcuBDXFT9z-3-tKNq2U1DSWxVxFBABpfLCbDmzjXEjkWysO9rNNuq4Of_o1ZCprjBl0pHLPW4WKsLj6xhFyNHWjVeiTnGi-w742pLl2me3z1NfuOcOc7nQo1TWnIJfIsPRQaBl9Pi-Jz5sJG-wBQVeNTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdJ7Wjl62i_7xGyg1oPSUsrN_QSHHPwB2hLnMcHkIYQu_U1lt-dYHsDfbeUkwU8Jcwjbau4rHmfAiGswUZBBK83-i6aQA0mVVGxdLdE_KFlTqU26cU1LoypyF-19X9xv0gf5yv1XOwk_9cLAyUEdveGWWddx74wYEWo5VtQ8so_WB9z4qlMNBhv1A8ggm74zApQPzr0WoVSBggjAVBVFpCgCxk4w8AHP3UzU6BHCyIDMriTQDsj-Mae9J_1tXHXmaxB7IVEdN7XAlEuk4Kjj4u5kPSIE2IW9gV6ssYP_I5sNIjgYSzgBCkq779gbI4t8NkdCX1AbpEMp8qS79pRZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=bYdv8VPFuCkIxW_D52Z4L87TZvnJ5xf4PQWWlWU15OaGxEBCqBlqO2gZqUB6NxpaWmuiAb2dLUi5VJq2p6BTiuWM3ZkAGPPqlaj8Vx7mTysJKKh_SyNby1wtYBzorrWBPSfP_zNmSQU7VuXYdSo4SIiT5W2by8SK5lz-jGTo_hxegd3ED1Rd83cDeL0clOKOoHoRsFGj3IP5DFYesHAvw9a1QPXx_wx8ExdiMOyG0rfOX8-SjzqDjTxBLnBG1knr_hR0BFrMqC2Dyb2nQeJs8RYQti11dLXCW4ekOmfdfXzlCPUDi0PdqJpPw6NojlSf-bC2jighZSI39p_a0VfIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=bYdv8VPFuCkIxW_D52Z4L87TZvnJ5xf4PQWWlWU15OaGxEBCqBlqO2gZqUB6NxpaWmuiAb2dLUi5VJq2p6BTiuWM3ZkAGPPqlaj8Vx7mTysJKKh_SyNby1wtYBzorrWBPSfP_zNmSQU7VuXYdSo4SIiT5W2by8SK5lz-jGTo_hxegd3ED1Rd83cDeL0clOKOoHoRsFGj3IP5DFYesHAvw9a1QPXx_wx8ExdiMOyG0rfOX8-SjzqDjTxBLnBG1knr_hR0BFrMqC2Dyb2nQeJs8RYQti11dLXCW4ekOmfdfXzlCPUDi0PdqJpPw6NojlSf-bC2jighZSI39p_a0VfIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiUBPvnxaW7ju1ef6dnzlLnMQrpNKnmXGBvKe3V4Vj_yHBjNHkywAqYRAjebdJHps3Kf-9GoRjSphtowhA4Bngb8ZJajgvoRLeUDTteLe1p2cxhn3eqt6AzWj6S2uVkTlz6wr3jorVSrGVTxeVybNS_5MBNFiXq6WF_yT0GPuf8G8-jmm5fO5i6SguTcjwDitL6q5lwxE8hletjZZlbuA_HsAVz99wok9CczfC94a-Z9Gl8jsAaonwpSCf2BfvdUKrEGCVKUSfl0y6bpXzme48T4Yk58Y0qjeFid5c8zhy3KfKqS5rWxSXmRxxKgneEBukjOby9nDQAPDEi8K8UO2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvUiKwsZlgR66ROThqfPTe-bS1CR5wh2ZgQen68fDZVomq2dHlGcBTWsRelbKJ8uvAk3SmCEoFARM6CwRJtmY6BGGJW9Olduv2M0WVMTHMQJnLTTcYtXjDaMMciVZFxuXrFSSuCKtFPOCdzwCgoyd9f5iLioCXTBQTIqCow9PYHtAcPaEd5X-HLsQmpIxeg6tZObPQL8lbsMifk5EaBDczdxzbA4pK02IZZpyf8Y1alKn87BK_E8J2nd0b9q-kl6Ae59qO-9RhRcyXQXu0qaAvOCP0Y1N4JXbZ1sFegEpITqXGJlj7tqphMmskkZmHsyppiPtdAnDG9Gkox4L0ZTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=LQBoyzpsVyo-P0Lg8S7-qCjtwAEGvcTg5_Y5QbIG6g-MjVLpB4kwiMU77R8BmbhKQ2TAWHfIhyT2Ufcwxxx5Z9RM_7lDnWEFMtqP3l2UBYpjacf__cM0293c9LUIcPBA2kxOHL9IdE8bbPl-ml2-8Y8dkJ3IpkXrRt7gAsjV-hIojp6R0aupk7D8NVcCr5jinOgmSNcktHl-EkyyT5QGsehUW01JeKz6Vg4zukpZpYC-qiW3EzeKcacf0fjokqtGjVcvdwiqDcOruABeB1jZY-uknZPnpWsUxi1x5aipkOhVM6KEMpz8yrjB3LqTDg0bjBZ-mHD86O4xWxxfVNX-TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=LQBoyzpsVyo-P0Lg8S7-qCjtwAEGvcTg5_Y5QbIG6g-MjVLpB4kwiMU77R8BmbhKQ2TAWHfIhyT2Ufcwxxx5Z9RM_7lDnWEFMtqP3l2UBYpjacf__cM0293c9LUIcPBA2kxOHL9IdE8bbPl-ml2-8Y8dkJ3IpkXrRt7gAsjV-hIojp6R0aupk7D8NVcCr5jinOgmSNcktHl-EkyyT5QGsehUW01JeKz6Vg4zukpZpYC-qiW3EzeKcacf0fjokqtGjVcvdwiqDcOruABeB1jZY-uknZPnpWsUxi1x5aipkOhVM6KEMpz8yrjB3LqTDg0bjBZ-mHD86O4xWxxfVNX-TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIjKPSpBDP0fQ-vkLa0Icrp_IP8xRUGkNrJIZ07uotCfL3W-630RYJaAul2PS_EtxCkHIjtrvfeo6RRu8-qPhmBPGUHAbbO69Y1urHZh0bvXlClLQbcgs2IxOMATgvDjoSjiup36ABH6FadQFJQuStV7E5zHJ51Kjqn9hwbf8Ef5cklQHvGEkf2lla4cR4yAmHjMXXNHMYxBfZLE1JAxithaxtPu4fjrEr6BxjxIW6tV_q_5wTTfEi47sPEbvSk8QAMiwpF4DQDBAYXHnxD7bD9GvQF-XBp8I8_5YGsZTM1gyXy6KBphOqfLRb4y4HbP-WJumfjdRsMrhm4IgM-Sew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJlvuOjTorSQrrwDW5A8XRZOv1bdYvl718dptLEfWacmKo1Lc5EOvvmFoThEAr9cVtMa9WIACn991XmHs6w1r60FPsXNHWddHKAC1UsygNtvqn8DmmJBPt00RJtwf5j17DmAR8-91jUYJ5idtuMD0vP6qEt7-5IybehS9CEFo_nvTQZnGt1r1AoUDslO_y3WN-WH-Ck5FJepMEFvNDaJTan9LQoMZLzC1qj7kRwyBQIc9dnLLOLdOZqtSTli3wmSJJ3bbOiNlX2yOfNC_Iyp-GN1YtzMdZGAelO-kGO1M8dFv0gQdQn-OufhduqNXI7Z3KyIQp7t_yNUYxEUOdHskQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=YzmCYfFE8nJ2tuRhy2aPeS5fOQRd4qb6UwrPU1TaqiZgQBQYQuldor8ZpMsqy7tlQ7go7dyHdFVoWZXJFrEXXLUC-Dj0VM6EGkeTtfuQAHEgOzS9htqSf5qiVNKmCSX9Fpfn1TM-nBjxITPlpdWRcsQ93ShNxm4tOgvhyLdw0YKGElrIvt56xff5VYib3Oql7bhXd68DGcAbYqEG6O0KjdXhwzrzCGE00SbgL1DydQEfHfeRUYCmatp3bibc7vSBSQlhe-f20zjHi7OkynSIA_SFis-mCB2uPHTH532yPbdvlCcoT76k0o940OHr9fPhzFID29OIO-REnpDFxPV6Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=YzmCYfFE8nJ2tuRhy2aPeS5fOQRd4qb6UwrPU1TaqiZgQBQYQuldor8ZpMsqy7tlQ7go7dyHdFVoWZXJFrEXXLUC-Dj0VM6EGkeTtfuQAHEgOzS9htqSf5qiVNKmCSX9Fpfn1TM-nBjxITPlpdWRcsQ93ShNxm4tOgvhyLdw0YKGElrIvt56xff5VYib3Oql7bhXd68DGcAbYqEG6O0KjdXhwzrzCGE00SbgL1DydQEfHfeRUYCmatp3bibc7vSBSQlhe-f20zjHi7OkynSIA_SFis-mCB2uPHTH532yPbdvlCcoT76k0o940OHr9fPhzFID29OIO-REnpDFxPV6Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHp_NCsy1u18e4U7kN8pNp-fr3e-XzIatbig3juNrQa1xkgsnYEZ0etVnRcVfJHpK1Tgy3VEYfnvN_oVvEcxhb_4e03A0pwv7p6w5Jas-8m9Kqbd1rOwLo7X7laJcq38CTJTFv0_TShT8ZgHpT8qS54JeavIoYzTaLDl1Iy2xmZgbZ5k7YO7DBIy-i3OzQWECQF1xixGF4fMV7NdaDyoIENNfiZiPtRIMAgW6FcfiK7c4B-V5MpFHBu3nOn8GGrrYDb9590Cq3Ga1v_tq2NAoMZl_oJ2Z-Ib1MW-i-j-LCRxKWC5yUeObWaovubNcsOuCVw6zrAZeyVtLxfLoZzJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIJFAN-ZmNRs-hziPOUN25H6AsoJRF-5cHY-0HFght9tVlT1s9_jpmLSqa9CE2jcAHVMQ-MIwkDlqLKkiI_a72aFFjUcbb-eVB5a8EVBCaNMyQ1Qjui1ZV32_CKGgynhh9HNf0ReEP_XIw0G1D8308tp4fmPsmZVfgCcWceNGYS4z5AsUNwnv22IWloLkyOlm2NSShR2eQJansBZbJqQ9pY7wNae_yT2Vo1yNni_VDh-x03iY9zpPt4kBZbJOoHHLdabWODuIYFjwxLQNF_J7sc541m2C0dtYuDSJZ8LNp_amxdofr3kHEsyZYXmVKwE4qGV5OoP0YF4ZmVOJgonAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=rYDOzBvbWxDrCgakxRPgtVpyVM5HtOq9EFL_7OZLUu68NZCQ_zPURi_2W2S5hJAnMFx41fWWyIPzRq08ttd0MzNHMGr-QNda6BsPdYGeWIInYNwYvu2FP76kIaiHVX9HhdkDmrq9eSzMljDG5XyelE5YnUKg5UsqAuo9ho-MwfpROxKaS_YD9kwiPIJy8lYVOVYjLSCw2zoR5AOts8S0Bz0NL4DduF7G0WgaQktbH_fZCQYrBrza2zk1eKdHy4dmKU0obr7IEGZlUDagiOs1JOmiD6i6O-nFX1WpcSQy8_eZJYvOu5s9ex8mhPQO4ii7PEw2ExnuFSqNGyRnVg2Gcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=rYDOzBvbWxDrCgakxRPgtVpyVM5HtOq9EFL_7OZLUu68NZCQ_zPURi_2W2S5hJAnMFx41fWWyIPzRq08ttd0MzNHMGr-QNda6BsPdYGeWIInYNwYvu2FP76kIaiHVX9HhdkDmrq9eSzMljDG5XyelE5YnUKg5UsqAuo9ho-MwfpROxKaS_YD9kwiPIJy8lYVOVYjLSCw2zoR5AOts8S0Bz0NL4DduF7G0WgaQktbH_fZCQYrBrza2zk1eKdHy4dmKU0obr7IEGZlUDagiOs1JOmiD6i6O-nFX1WpcSQy8_eZJYvOu5s9ex8mhPQO4ii7PEw2ExnuFSqNGyRnVg2Gcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBR7I62K8UsUs3ZKnWrLibVz9y_M7aiG7PsMAoEcvfLDrHfblKIpWGDejulvPX3__2_jJ6vJw-di-FkjrIjrxktEdqYYcsQYrRUwuhistPXY5x1c13uQYvaKKBz1TT2Xfw7LyZlRLPdYy5slFjG4q1SJA2AK19UlGrag6jT0p-yODF5zaCWl3lGaKwc9yJn1HiPEsSxHGe-s81fAx3C3_Su3-_7yaqIfPPBF5_BcZOD44kwxjfhFkuisvALo5REosjPM2KEcG_t3Sq8nTmcI-po72jYnc1xGvsclM8IkrtJDmZgwcWaaDpTYycoKeM0xo5NRvnfzvhasZDFxmtG2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW-RD1OUvS3yaMEK4guIrVEoJBXSmcd-wFeDG6rvoQjKjYGnHswqinfeXMmcSUq6YceiFKiTp7SRVH_G1Mnkq9N_inthy033Xu8HqYVnIeAEv4QBkWYL_1fq9Heo0JSkNPzoxuI6HdymSEdH4RaymkGJF0EAP-PJNmL_zw1p99DI3BhsOPabzANfQXuQwacuZ5PqqEw31prlTVgoZkRSfkXM74K62J_keeR40oXcd3F_p4JwsycJoFirUvlOt9MOKsgAxl1J4EoLHZwYOVQPHWr0QTiBXdYYVo1A1LrN6xCALGD6S_ewLlvLFzcyM59pD0TeqIvhhHPpCRzcAekqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcYMVW4xmcviZeVqEZr6gk7tokjp07LpDmUDXW-_tXdSI9fTB4Rc9mQCSrnh42EnZrUh7qpkv4_Tz-OINsvJQ7MFlL3UkwvLZCpifjO5m65tm6J8V1BTm-1yGmDlt1N2BtwqW3_7oG-__QLw6qzdY0AiGMUciCF9sl7Hy6AP8TVeah_KeeijOalTHjCaMM7WY6Ry2pxk4SS9Scz0QsjC6bZDXQL-hgeE7UPLrnYNi1TVyF9UrJKkZr06NQYbpIar5Fz3zrskToTxNW3xDjIU1iM4IbCb9QjWpBpIjNcgECptePxbjRFioLCUwzpIvf3rOJgC9bhCkQcE8dXCDDpPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMPBEfz9ZCrCRmJhmMUsExgznU_ipPz1m_CKY0UtGwxWkkPQ2eW9it9MVYyJ7QprbM5ai08k5kvHpjzogGQdwj7Iic56PcF-d7ExYntaYtlEfMRymr_Qk5KFr4nLbf6JVCuay_pxZDTyhHJGF2WGDnuiniT6Z1QcFrocoF_rTaJS1wjHFXrJdsW21GwHP5MaMFx4fo5ZGAR6s6G_0nL5-VLu8gRqaF2Z-sQ70ppxZ5ArCVvlj3DYiSzcGpQKi1hNGOOd-nNDc7Pj8Ub1shDhy9YMfHkJrUO2QPHiN2BtxG9TP_FlM5uVOMsbe7iKYUlFL4Iof8tFmYiO-OrTkca8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MX22ikhc0uBo2jTT2yYbxuOBmztDS2rD0h45psrfZKjvsSrJ4WlrFhKOv3IV0JHE6cU3TSaUSeNSNXEMpIQyKoBUKUGXwPK7vgUWsCdNV7719K7_CLg9t6ae_0HSdq8F2xZe4RPgerjuACUzo_nAUqsV9Y5MpeWjilJQN6zYb6ZtsKW_86ztubCsTBJB6QEI9g0Q88Ku9jWVehDH4rN_kG1CaXes3DPSH6mdB5bvoCyIEipBgXc9IFJUErdRnlubNCudtvSsMmC93I5V-0Ckh8GmPSWAaHXQNUhB5mVR5b2M2A2K4MIH8NTXM7Gr4gFgsIM5Ss3K_3DiWUEXDccxBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7SDYYWWzhzBVCWceId2C4foEgyVdM-5zYrswJfPEGHON2Dwi7QqIeodLSB4KctjNLiCd-lYeLHLaDnh8fv2K4ey6UBzaZcOn2KZaP4OXJVOAlNg3bE5VlMwTrFpLBybOLCdQJ09Y7MX1d-NT4TnDDaR4_e6d0rdYRTQbpEoSwY4t3nczd-MsEUD6OV8dpqAs2tayOmNt5cj9fUASAg41AFGeRzoWDK1hjRxvmbToVcQ_Sc7nzfnsNeL2wtu2zr_ldcyEftl8hDgPDyO1e6RwB-VXr-zhmXbO9jquHK4bP26vfn5_2CXYzLL0qp_LaFK2uGL16YPAAFoZH_SgzSAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceVr33CKBCmtYbnns3mvRt1l81bZTEMRpusSuhXrakWwAqITODzzqmW4QGcp46q52WJyqAi_KmMFSH2roy1qSab95XbrRl4QTZFPSqKZfGDL8UCIJ3R-j3AvBzpUDBLkTT1CpItUFeL-SHsQfpyqTBQ5hoDU5rh8iVRHV1QLgnZy8hk0AZL4rL586M9U_8_Fi4uhn2wzb4-MjUJsRJBbkPYe-2kFfuAfrztRnxK0LwjEK8RoEFBAZqN2O_-Vg3Zd_-T3QSgLgOMyOUAh7QoSTiTeLkghdwevuqiTzGRzU7-7DrmxnqfFK0x_Ow40VOd2RiIb1JyM_rBKq9teH8SXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
