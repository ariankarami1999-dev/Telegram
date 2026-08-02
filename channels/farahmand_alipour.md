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
<img src="https://cdn4.telesco.pe/file/fbIiqgv3pg1s4j9uWSr-UFKnstlmQ3nlvj6AUWjMygjYexED5GJwlY6nRr5in-gFmaFyBZUaJyRAAjRCcHLVcrA_aw-Uk0iRMNGNK-GRYvMKxb7zk8z6yCmiWldVHbAQZZgEPYX7DZ2Vk4Q1g4tMYYAJaKrXah1EDNHIiZB7EJ2NJZyWI1LlcBdfF6vEvPR-howDOMlHMRgYNNn9x_IVLlF-J_fPqj5zZBZjdVuBpLNZFTJ4U4HMbdUmb3CK_qK0UQwCz43dSktXKePaS_G-e7vXZLCCJxJP0MNQnvFQXqa7gqevXKXM3CnQWmKwfaowB-knrD8BA4RhQSp_tJcBkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 13:01:52</div>
<hr>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e18V3Bg-Uy-bo9ikhRI0ztV_Z2nDVyHXyMnW9nG6K0TxMznHD0rcUCZKC8bpW91Wi7oUyLfbE4b7zZzvjQ1CBgGdhjWfeqPDznc5DxCHNy7wC_TvNVSbzahUQhl0RqLJiIn8ijtw2v2X7YxwWwHc2abfIGvwqxd51n3CsFGqO6znkVEkSQgkry0GMCPli_rSy4PBCdSjCwluqoWE8gUA2xoaQx43eMagC36ef0x2bL45tycuf06HG6581-ZHGiFjpxgDuFgeBeE_Azeb9lQLoaHlykgHNtYlZJgjVmD0Qag3-ZYkTtnzC6cYoEsnQKYn7X7FzkvPg-g44o5Ir-1t6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct7ma52ttEcB1SPI1sXDrLV0ImmVQwbFIscb0v8r7ImER-Sl-ZQU6he43rN67jPMWxTMHGevUmsZAqIweLUunPqlRP5B843UzpeWHVjT-kSdYOombDc2Ns0rwhLygOrzNYFZCUzS3wmk2gXr2nZq3YsW00LVUts7qfj_jJfhgUDrnWeeDDP-iwyfkiBcMcoI27uUBA7bJCxmiaRyrUt_8C0qdo6r4HORUm3l9iaZH44CDq9MZGyKAkjAIGspmmKFGiUWabZu8CBlOkjAnAm2hrCUKT4mhOKIbF1Oz64EO50x5zy_pRt2v8wXqAj5QVjvahRASo4jkdkQjjfEJt4edg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcHrcZwJ3QjDmpcqSCYCA6Hwu2XC2rG9CoiCFaFGiMLDqW0Jl5GYIgOItzigcbbG8X9PcQCfkoDybWXPv_5FzGcW3Ka6rT5T2bV6CyEqD0vn9gTDx4eu6RWwoMz3TBZGIor3ZeGc39thl-PgEinmxXvkKdoypD-l608DFqJQOnRnkuNCBj-z9jJShgSGx-GqdGDZ1kqVceOoTxyPY8EbwrGeIesVmW3QZFSqw_zb_kgZFUI7mD4FP0_LyVYN4eNLf8uzW4TG3cKIuGrdtzGmzvWSRqJFJvetbBMmRwA7ENDC32Ggflt-Z1FTe9GkCT4IzxpTkL7up7aad-uy4KSYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=m76Me_b3qC6orRKw8pQV_Z8AVxH0M5X2c1WCCl_Aez5P8oDogCd0JQxwBAYAjTxzTsd8XBAN2nB_030CYTk1tssaQrh5UMhWt6I9zW4F6_k_rIpja-y3d5BWeYWAxNZcP3OzNG6dJ-lIKI3edopur4spffv_yOR3H90FXUWq1hBUabpLk73_IEB7QhC9zRL6g2pz6U4g-WsSLSCYFktNE5vnJ3FD_FNKxCGR_Ak5BYRDAqmBcJgfqbAPc0jo3M_ZnAR5VJnSEnNjKiUFWD_F_PBEhWsbKwp0w2hfnDkqYHYYt1NYmRwhRJDzQdjRYruq0oGhq0XVb1BSJY9wps_G1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=m76Me_b3qC6orRKw8pQV_Z8AVxH0M5X2c1WCCl_Aez5P8oDogCd0JQxwBAYAjTxzTsd8XBAN2nB_030CYTk1tssaQrh5UMhWt6I9zW4F6_k_rIpja-y3d5BWeYWAxNZcP3OzNG6dJ-lIKI3edopur4spffv_yOR3H90FXUWq1hBUabpLk73_IEB7QhC9zRL6g2pz6U4g-WsSLSCYFktNE5vnJ3FD_FNKxCGR_Ak5BYRDAqmBcJgfqbAPc0jo3M_ZnAR5VJnSEnNjKiUFWD_F_PBEhWsbKwp0w2hfnDkqYHYYt1NYmRwhRJDzQdjRYruq0oGhq0XVb1BSJY9wps_G1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rie3AQP4dmNq1HVw1llkQzRxdNmR1Y3dFfJw0LD_2_mZR7Uenv1IHplnKxMPkzHBUtdCDzC_PJ6xoeZ_b5keL8lyEqfOAqFtc06P4WNufx8Hd9oHq9IOHNOIL8ALlixE_kyvXX4pmRSsoUuJSvkAp9FkZkm0UDoETCcp3x8fOrGNgRSE6ZaMcrQuhZXhFexJrYXkarR6pzvm0O5NH0KNaJRheqhC2oF6z2XCgJV7UDX2eMeHXFho4EK1JmOa0lUxqvBZVoVDL3lJmDkae46WxQz3faYY1FaoiBXzLntBscRAJrGBqGFp2eJnrNTmyyinDldq6RF4D4NUBaS_8dYVPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_MYiELFmaCuRW4K5t0iXHsssd2nPiMseMwen1dgWTGx0m971qi-AcVBeISstXpS2AyhnVfeeXj43LZfC1a-n6iEhO1pLR5J8AjQeVBRIDzE0hoTO035zhwm40ORszerLXQ3R1EB7bdLoaPRi7z1gEHLYz1yPvQOeylFMUoWTsNdB-Wyj9WO6Lh_cKCtDskntTuSWGzhc64DTBaWW5NU6x0JofnTmwFHfCG8oI5v8NHEnW_23l3seiHCmfb9pwqZPsieW01qN7cWJ0SZVmNsxn58HBGoo7_XYd6Evpn52kw2uv84qYS14b1-kwxyfc2KIq2ogzrCXocJdHYsfBoUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg-Q3oMjNfneqGUWi4Z_1_MstfPfS4pGtLE4XIZUqBTrmlAEex5yamJ31WsLEbXUrJ-nvHulM5RyQayp6mY86zJcCG1upFCSb73SL8oMMmL_gudu__Yp3pqb3B-yyyfSCmrvmyP7wh-qerG7BMWcpRj2OHKl5Bl4g4bsa4IWs-nctM8EAgN2_DzbmkRtxe55kTQHaNeGyFet8H4R_GH-ka5iV0CRe3tuFntWAMvdDR5i1Ye3vByc9Wpgy4pUzgAuQbvLIIIZLZLOLofizDGc1LpDMGi1iOGo4m_gAvYvCBrrG8cOKcwv39kS_9hwyAh1KTughUDl2IpdIsjU-XK8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9xy71n0rwES08BgRnS5CI06Imk1wO2CPfDhIZIuzvnWkQ1nXvfFgVnD_JqtWO_iB1WvzvKHQkDqSfEndC8xyRQoTr0qqe2E6XaP9tyHScVso9z0XOrY32wmeZ0iL9hyx0ZJJcAtd-hLXEmsifIKBIWnT5LECtqfuVM-7O-6qAfVbqFEaiPYgrnI2A0the7NodDcboTKWWy-l6PA2gDiTp1kxhBmPYpIeMeJQuDMpUmCKUZta3wKeQL1omHIgHcvDG4uvDkL6FhhucJjUwAX4cvbP5Fn-jPt-Yi4zG9Yf3MbB5B-3jhVWYD2rEgA9tdhbS3w4fnijPPxnOjJRYJKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lr6Q9Q4t2wqDhZs5gIKwFGXu9wj01NGC-swW3Ey8KJrwjMLiEF7ui5J-GMU8pb1mMi7f9CN-IeeMxyeumxXoO1LDN0PUcCQtaaSZQqnI2FuEmZ78yc2fOjL0kniwqgxJCIekC8ogLDTL6Lvpv5uUOdt5Bp1jUh2ETfHmILyAjNqkXNLNYzwbKt_0w8wntxLMFr2Fo76HvDux8njnUjbfPS7wG9qO59g9w06WsvrVOpmbT1jd84b64M63tsuUI8_IpxGQxJwEPzh31DbfntGBh2nmO2mWLNy6Sj2f2ljvjthmgtqM5F3fSlJtc8UhQnm9N9DI-1QvAkMIv_RhFyfJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZWXiG9Pm2zdfjszEwuYn5iU5V_EP7mO1aAFznmjNvBb4vK53U9R-oc_LyVwBBrHhHuR-sBwCy_jc0Nea476C6z8iHttZJMPGlvQDHTrIYkiCVt8S2P-rH09MTF1o4g2cIp_jW7QQ5Vq0oKEl-WaohwfhDfBBVgP1uPt5CvybKOE3aKnxLp7jEBWCjbfLFsUoHaxeC5rgQ9eNgdhv8wSn6CO7_muNTtjWMvoU5HWziOdqHYqVW_g34aNwrjnYbmYRYGEoaLV4e-cpxhzDxThA1KlocF6jW-Rle3XzG_ji0cCRQd4_grYiy2z9D3A7SqjvHvn3ptLnRPiI_30yogJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo_IqMKFX8OgRbLEyw8rO2mEHMGLx_WmMsGQDl1n5_3kN3eSCTlCD11f1NHr7rnYvypYaGN1AXY05fm56NvWd9FF5Q-49tQZLNAnxGKdOArZKot470ndZRggLwjgbOmeEom13tvgoCpOC6eqMoPNrLYoPrijUXuqcUdC8jo1RMpKR_YDklvUL7PlFaxj0_QsnMKXaaieAk-juF6zrsUhy24-t9KH0iWUrPnGtQ5uIuXBX1B9iFrtbAqaqULCopqrLPROUPcbSSqaq4EoapGn8D2s4_Hd2ZXbzNYR8C7y67bUAF3aysWc_-uNoGDmPO-1MlT9Zbpko4JymG84l7IQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD9ZlWx9cVj_jEsUeEeF9DP-nqMt96Gk8HGEqi6InLVrmhwyynXOv_qwSC-_FVZpUnpmUo-ZPu1FAn-AKLFayMq8iKJZ5Cmc83tEyHdKuEkUNCFLBi96XJw08YimuBBP1jtuuqLIsdUO3ZrxfyL4Mi9lk5aMG4iHq8lci_vhP8LXmdUinvQ0XCcplh8IBVVbfAUGOKKSZkVHi5EWJ_EpzBR2M3uPk5Mzt9vpxumB9kwiLfPL9Di6Fy42sBQlR4IZzSmpXGtD9YkKePEUYXmnQmVrhcOBUISAk75ruzcbcMhrTgI9kIIACX6WmfzOvm2b8QZsObCSyGA0qw5ENngmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=KdJGnGjofmO1YK1ZR9o8o7Me8-W-cqhr90nL1hHKsLlpu_Z0ek5Y9adT7NdSfnxGeFPHzqz7AJuNgvuFxxZpMLYL9JVOG8wIFQVMjlzmI4v3G55Ez55UvfnlU2Pa9STmiCWfoGfGhzvAqdorx5UVU8t8BB1YO89wUEBJ9LA1EMFSHG0yQpFmsJKNdz3Vb8aohbXZimAXrpDxPfRshEFnKWDFFfWesH8trdnywMqKB0kI7pICPoq4BG7AJZITFVlpIRd7Mzat0sgnUZpmam6WBX1uTFeu9rYqUjYATCoMLXcG3ErrSCkzp28HRmJVPIWWCQHQztl54q3IuRSdgz8qMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=KdJGnGjofmO1YK1ZR9o8o7Me8-W-cqhr90nL1hHKsLlpu_Z0ek5Y9adT7NdSfnxGeFPHzqz7AJuNgvuFxxZpMLYL9JVOG8wIFQVMjlzmI4v3G55Ez55UvfnlU2Pa9STmiCWfoGfGhzvAqdorx5UVU8t8BB1YO89wUEBJ9LA1EMFSHG0yQpFmsJKNdz3Vb8aohbXZimAXrpDxPfRshEFnKWDFFfWesH8trdnywMqKB0kI7pICPoq4BG7AJZITFVlpIRd7Mzat0sgnUZpmam6WBX1uTFeu9rYqUjYATCoMLXcG3ErrSCkzp28HRmJVPIWWCQHQztl54q3IuRSdgz8qMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUBX3Qdqcbnf53lQGgTXV6dCFAb2qOwnIby2Q4oHGqZ7yEML1YV9gNozBzoiax9MY_dmkiPhtsiHevAIvLSWIzYFgZsP6fwjVCvsZ213RFFZWNOkRlrhsU5h6zQ8IQZgtPpD5bgmOHqQWxOlYYLM26WaPV-YJKZKEB22U72w4fa6tFsDLuFsVeZJPSJaRQEMvrkF6lB6CYCsDYaMybIhKyDBBSpegFNMxBtmIOe-H0SRu2FWZxzhdHPCw08tS6sWPf0q2wqTBmHXOhf4HaOC64CqC0-UhbQ66Z-vExq4HjJmkR9EwimULFg2EhzMJis8fyglBX-PPP7KvytCZgilLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-kOBSioRoYtMGTqcY-IBM8rWqdEzKzh872WkLXQ7m2MVmDG0U1JmkJpKriqo8REoTKUNlihb7IYSP6rI_SR3y6fYWu1KI_OUsZEo13y-l2-dqHYueY2p7EkcgXN2KUd6nGlLbRgXnIlXA4XnFxMIJSX9r9qNFadSzzi428XVl2eC8fSGLyesYa-Y5PFzW7nKPxvqKAvUYZzNzR0O_wiuytBcMkUUNOYDkrJTyHHNxIafbXoVldFCQmVDuLrsiSrA2GyyjwFfUnQa-sms6kaPpScnPH15M8Icp2n-zDCvJ1-JC5XECjVMKoSzohZY79RnLASckoa5v3_2jiV4y8XbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgINaJIP1ZyAOPM3iTC1tLCFUVXkU_UlrWgn_cZDyZL7_JzY9rS7m-fg5YDxm1gqhfnEGab7we05E5HKJOTVQj-Lopr8P20f2JK8NwhoPLa3F2a9aZ5tCG1ONZNmLSzuIriy0ZK2KaBOJellWmjkKPx3_rldj7d0HM2crhcZxQEiloDan9ws0bFigfGZ8jDGtwJg_PKqvF-tcMuIkXaFbHUEPkiDTsh27Q6AFlJ8AFkNGs7Srm3NIs6CH77cc5VxBVuqWr58DSeI42rac_feM9Qu6IOkF7nUJlTVDYLJ5jIGq7n4kJe9MJMzFBQG0zNaSDPmHlvUnOCmrYXykYs01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm_fHN1nHjyvkaB-7tPOtmZceBjRoGHp3L4iX-tJZ5cMg2Kff5fgtMs1QiL0miXEGA9ycrJI9fFPON0ejXoAQBYMmlAMGA3JkN35ATa9LLfUljVrVdJ0jKI4ktTYju9lIYTzE-VodFMmxet1tBnwKkn7m9r0IE2pqysKnN6kyWjrfmqRhLNeC_7KHKAmQWoFc5CCqnSlPiRgZ2Z6s7YMx5v7eaTR2b6sNVde_oGhI4z5f-w8kpFIe-CCE1-CrsMY8139jkzD5xAbJfWz6_reCBBTdJyeN_oOFHsO_2vF0IvoUhzMWf09AWMlg-Jbw8yF3Pz2tygDA7aU7NRQt9Y2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIxgXCS3nkDfswr-Qqs8xtENfHaGZTH95dgiagCmBM7KPacsiS3Ws6ZMPH-YjoeYzaCiNdUS9ZNiy6btDeEemrUuG-Gm4Ch57QMz6bEP4PwoE5rZP_l4njZzhENabcBe91dcPiwnF4TEdso4W5MpUvsLvtlRZZbSEjGuFKH0pFC6GBmZXdz2h267k6YRDvOr5IpNSqC6mgxIqfnDHZPQbwGWhP4ioOmQ6IkFkjpsIsOcIBcSG9Sxmo9_7S2CZcotrxEPW7U9WF-QX9WXoxS9R-GEF4hcaOtHW5mabtPnqA3zbFABr6WPZRIMBE0X1XdkJsbsoFqLQevv0Y7OZF7AaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss5LsYsSu1bTIb2UxXMd3N9qkH5zx22In_lszP513GGWkQaaaJJZ_Fmym-A_BHX0srIwHm8db2shPuvTVgvLfJCZwxokozeRNnSa3toSS8-2P0Knx5_QnSJPdBdcX2XAiZijT_I6G05RcwAqBuWfSyyExSBX5zzwGWYwguXHVRQndZaDynooC6zlo8PLC_xojC5Nk4Buwdpd-8cw__VSYhmvSXlIFGq5X80iocmT-fA4wsgZdoY2PwTZ9iQGnil0Keu1gPFDiLOWwN4Z_kC4DVkwd4js8Cc1ms85wHe1bFcRm9bnM0UvalOKySJyYhKD7CL2rkFmPNEgwkgaSU5Few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW3GqkA_yUw4ZJ97Hniq7n8b7VY8gqwn48WozSD7BqYIdsRSSpphKzfvIFc7S46V3dybYUJcpIP41qqDdMol--i6s0PbeA6c1m1WF97JrpaqYRZq2B4nEgvbhhxkfJwkMQAZc1_fMTK3maKAVsM3fxWV_10g8m-f0gPEGz59tOkAaqa67BCaBu79NNqvrFg1yamaWyZDeKSjpb-s2sveUsE4ASK9ML0jwDN5pvHeXaiMxCviYd652yecRdQdIbEjRjI8J4RallO47rsSageC8jzbBDO2Yerb9JzIVSoRYNIsILxSQpO8Cn9AiM1DUn3d26Ev96Ow8iiPCuu0F0Ylxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=N5mywHFzr7_h-pyhASENY51XaNWTwLfOU4ArxsSsslzZ-XVoKwbpdmzVvNpLweky9ZzkbMSS92lXx34UhIqPs-Q3Q4xJEbgaLBam0VGKkYM2Qz5EHL060VfSlf4eXvL3avwRCBoWkCj8ampczptJ8l28LBAyt14Xt5v0cJurY1Cn5Mw4aiRZ6zGb3Lw19IzVUsRYtEUw0idUbv-4oojmYAt_DzUzG1kRoaBaYH8Rd_wXN0G_SqD_KSO2coN9p0k5FU9hbMwME3g0gsg_aEJbUElzVMHn_aCU76NSBHBJx-rsc4nGf_unMUOQcVjHmiZcNn2MzkhoR8aa_okp0yLCmzr0NFu2QJgF8JpMh2bUp0BkWiRSWzKWosrXVrEj0Jg3jPUFE7lg_tPD9doPQ_7UujAJpi2k6dDQXvhOMusSwF-wYxTQcAspo22inP5LmUJwtIcc5CrmWRN6wF4TeAnsFTuKnYUWaQTR7vKNIIfwoXjXi0fuDg5llyqi4mM9wTI0E4M5if6qCHmuNHksLqD0nI2qlEU4Ob54K3H2HDri7hvHH1WuRkUHWVtxFTKG5pMSiX5dGtyUIgjw0jO99hnziyd6uSAmiVz1p7dtqqtDGLbvm6wFVX6Xh-DBJLOLOmUPNV1V1R-rjBrwNzOalKxj3vpHA8d8zFvXpcgyo6E4Wl8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=N5mywHFzr7_h-pyhASENY51XaNWTwLfOU4ArxsSsslzZ-XVoKwbpdmzVvNpLweky9ZzkbMSS92lXx34UhIqPs-Q3Q4xJEbgaLBam0VGKkYM2Qz5EHL060VfSlf4eXvL3avwRCBoWkCj8ampczptJ8l28LBAyt14Xt5v0cJurY1Cn5Mw4aiRZ6zGb3Lw19IzVUsRYtEUw0idUbv-4oojmYAt_DzUzG1kRoaBaYH8Rd_wXN0G_SqD_KSO2coN9p0k5FU9hbMwME3g0gsg_aEJbUElzVMHn_aCU76NSBHBJx-rsc4nGf_unMUOQcVjHmiZcNn2MzkhoR8aa_okp0yLCmzr0NFu2QJgF8JpMh2bUp0BkWiRSWzKWosrXVrEj0Jg3jPUFE7lg_tPD9doPQ_7UujAJpi2k6dDQXvhOMusSwF-wYxTQcAspo22inP5LmUJwtIcc5CrmWRN6wF4TeAnsFTuKnYUWaQTR7vKNIIfwoXjXi0fuDg5llyqi4mM9wTI0E4M5if6qCHmuNHksLqD0nI2qlEU4Ob54K3H2HDri7hvHH1WuRkUHWVtxFTKG5pMSiX5dGtyUIgjw0jO99hnziyd6uSAmiVz1p7dtqqtDGLbvm6wFVX6Xh-DBJLOLOmUPNV1V1R-rjBrwNzOalKxj3vpHA8d8zFvXpcgyo6E4Wl8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=KgNeNI2JElr1uHnpOMdzzNy64mlohQE9u3tbD7lm2QG8WtQxRnbjpvJg4bmTnYUUAEl9LHAdEzOeifSo_TLd1TUHA1yu_uuvvRnrquKDKpUNpL-oJSc8El3ejfPSBtAWwkbWVH-KHuI7NkZ0wcqJf8mwtp_WOu5--JlrBEDUBNeu5Wj7-jeH9ZoYB0UquMH7_fTLWhK4t0NpR32JsUqO9Eno3JhPIAK81KHUO0jCuc_-sJQBIqP7NDCqv6fafbcdVQO8FvLX8SY2bJlZXZ0OWgqVK5AoOElyc6VrhHhWnDtuBs8VD8Zl_ZzoSjRYXBcLH1lKdJ06O0xbFB_MXnmJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=KgNeNI2JElr1uHnpOMdzzNy64mlohQE9u3tbD7lm2QG8WtQxRnbjpvJg4bmTnYUUAEl9LHAdEzOeifSo_TLd1TUHA1yu_uuvvRnrquKDKpUNpL-oJSc8El3ejfPSBtAWwkbWVH-KHuI7NkZ0wcqJf8mwtp_WOu5--JlrBEDUBNeu5Wj7-jeH9ZoYB0UquMH7_fTLWhK4t0NpR32JsUqO9Eno3JhPIAK81KHUO0jCuc_-sJQBIqP7NDCqv6fafbcdVQO8FvLX8SY2bJlZXZ0OWgqVK5AoOElyc6VrhHhWnDtuBs8VD8Zl_ZzoSjRYXBcLH1lKdJ06O0xbFB_MXnmJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub7H5bICdkFtgUF1Zm997D52JP6VKJeGC9_mPNPi1em-hWyuW5uV27QY0UjSXeCfmpU_4gEF3beztRUVBVTj8uiRDopdLnPmdyJUtUrFf2GB9ZOo51F0iYZ_eqe26wjZ8BywmhedRBvpmDm8Jf39rovjTCwKiKCxM-C3H7UxLsjuuMmDlIIttjvwSZpRuqxg7Ia0pmQfZ48vsNOTj1TzGElFayOGQerw2Ep5hezysotI8pgknoS1iS6HdOZ2C6yP8kiR5vM-xrC9d0rUQ6xYW3es8zVNyJKf8Q1zm2vJyKKHDxeLmurwQYFvFiC5oh_2qHcymUB4QQGiyH6gGJ93dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFDRkVq0Sm0cAonXpDNE3zxvl1f41NgsViATTXFwBf2sLcg4wfAH32d1AfC-UPT0yUGmDYE6R5andBHCYqNvVSuvUAUZOGE2J88BPPnE1RzsU5Sf8kWXyWDbRrWDMEQ4_TpO1d3eu7mKIABIWj7ZT6LCedCQ8J3GE46fJVfJaAaXDJZAPI1oYL4rT8ru8fm8iloa8FBn9_4kAntIkPIEzDjaMLIxEECDm8KdmWbKHfC1J81FmPS-9r8UZDPBDNbxBSHxiIE3ahBA0tQjoPB8V5lkAw8DbsnZx0UQxdO_xePpZcbyM35W8TxhwjLnhqx7ifnTTmegCE5F2CkFOgHKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=sFkUJViOxGQGjoC9AQC1HeWHuHm70ukdr49C20B_xJfjUh7JdnECTiTDdULr5SsWIcfgd1RWHSvU-XDCNmNILIIvFDrPr11qgr1bXUWShf4mTH9EK6BJq1Yh1HIcEV4xlxJDuHV9o0kpKDcjELm7A8sQ9g5_Ay2mVSIDw2_ZHsBrowLqnCml7Twk3AHtocIVtAAxSJAbYuuueCvOgRkDIv5kS1ccmSot4eVSytAh0wxHSFe6B7Igu7gpmf3WZ8HiC9eAFbXUFTTFkFaO8wXKAUvBajEclieEDq3e-wUr6ryEpGIVXx0Qe_ATZKnHlq0DG_QZK9Ktoit0YKEae9GyTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=sFkUJViOxGQGjoC9AQC1HeWHuHm70ukdr49C20B_xJfjUh7JdnECTiTDdULr5SsWIcfgd1RWHSvU-XDCNmNILIIvFDrPr11qgr1bXUWShf4mTH9EK6BJq1Yh1HIcEV4xlxJDuHV9o0kpKDcjELm7A8sQ9g5_Ay2mVSIDw2_ZHsBrowLqnCml7Twk3AHtocIVtAAxSJAbYuuueCvOgRkDIv5kS1ccmSot4eVSytAh0wxHSFe6B7Igu7gpmf3WZ8HiC9eAFbXUFTTFkFaO8wXKAUvBajEclieEDq3e-wUr6ryEpGIVXx0Qe_ATZKnHlq0DG_QZK9Ktoit0YKEae9GyTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJoUjNgQ-7CKFEnASY32Ja2LIJzZT5rs576gLmH-ExqwKY1m_n1pZnvDGczyFH2KLc6TE6detZ5XlaJGqueO4PYgim0GqBGVK2BX2gmG0TN4YQxWTL9r7Gqckg1uTS2E-dGYk96VW30Jiu8SJYp4c7AO4q6VNohYaBCGHD97mbkU_vVXwef2Ldfoqj_OXScY2lQUp9utgrkBKJAX9VYNemrVwcMWR1sJPblB2krNiPWg93W6CmLAq84FDnc3vWzuaaQtlRkM8GkguVnmIw156rmzf-2cB49iRPRZQ2FuNjsA3V9Llwx5jfytd1XWg2R-pD0_m-IQZI6bUGIXrREpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9nOaoCH3OMimzDvUc-DnLaQAXZbzCUv4N9TKJjJ7dP9K559GpmEwIn-mytpEao2lBSQNchGyBG2N7UM--xh2QtK-5fQGiV0tOoJdDHpobZb7ZjZ34Vy8inZSt-P0oXarXxWwKpHdKLMav5HSyZifmJhGvka7wmaZZdqZUgI_fFHixsZ2KEqAhEUK9tZ1chU8MsgWayQ9FDBPeWKPIJxF-hdtHA1valYTc5RKtR2lBe8v8QMyiI7pBNAvdhaGCw4P0LSH_JJPfFpwi5ZJ-ovGrlquB83VK_kYObUtHyrdRhquJaishHkhPm98v3Yb2Uorg4kYjiVW208O-p84gIoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8jRAKPd303j_rXAgXEekpSidjPB1L3aOOBlsTRt7HKKd7y4QhUSSv4E91JFD6APDWyOhAx7WkcFyP2XPRxluWasBgIizZbwVAdsVQ4l1p7RZ2vcvXCKIrWr5wCJLe-vfS_oewppbM9D1LL7aSCX_-afprKYcYWaERPNkO5QiuM2PHI1_xtCnUBJnC0fPAL70b30yczJY_sWBXd-CTGoJ5l1UQ0MxKDy20l6lktn4HnlTl7-kmH6QLsHDnvbtigsgX4SNaQEsOu1kdXqoF8TBJ1u2M5vWpkvjCo66ourDqGS_ZOxRAqKbfT8nJMq582ziCPI9ORraEobVQJcFTgHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNbsq_CXcu_KXt3IgptOYL1lHAhelYV5zkidmP572VWRo5BKwuHj4C6EFN-Q9Bla4O86kDPAkGDAv2ktT2WucZ6HRLmblY3m029RCy-Vk-XoRJh0qkoCP5xNq8XwhyJw7MGnx3qwvobKvlJJDjFs5Rz0OgwHBD08Z646Z6EJW-NK4I-uU2eByafyvyPWOsRQKstrkeXVBHqDTWl6Vhn9TTO1PuTA3pwyMlrC3QakeeOtCP793mMl83DzUOIbaNqXjPoa7HkGIdPWAxKWYvcbAzGFXrNE7KhSJBKyOzpkmKwbfUjPWSyq2bDqSTEPStSt2fF4nxs2DPOAxgmJeqdPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7s39u1fR2JLlCceMQ5_gsavFn65eCMb9NINsfjzLWuh7CmEbWkgm0ayYjb3yMRTpag4GogpX--tOSwoP8ZsruQNJC7yHfaph-_7aaf9N7LF4QBJ-GqTuGbBY4SYhK5JvMx1n_HC2dJxreXwNXXP4SjdxbIefAwRMoAp66Lvyl3NgntaRVPHBywUdQiA0UcujXQLU7eMFzC8QhslhqJdKbLDtbNXRu99deBUxMvn-w51tV4-A71LoTtRxoa8ChCd51BOEl-hYRQyaIiW7U_UcVrqmCNEvcW1jl9uXL9FyuKLnV3cLU5AxR4CNYDlAU4LGl98tFucyQTVt3mD_HJ-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJa2LdCEahC65VjOpUlH9lV4hw1kGUXSUd8XyD6aHZQvVq9ttulp7uPyU606vIStqIZ1P8S6tFPj7JZkUvr5cQlMUnBAIr_Xx1dm9LfjAe7GdTnBd0a2ZfRA1ii7msDEPVJVahV3lUfxwEqysDHEPJJuhhh4vacllmcb46NhGekQOdpRlDbk37Wr5o9CWosGcBYSc_9KQOshrsX0S0QrIsg9eGi7YTRHcuNah0-Bx6L4OSdz0yH7mdpcS4k6gR0MdzhoUp2RshYh_tmZNwCcAAsVwitLxA9GMlMF7HU8LVMJQNZ5JrIWR3Dlyl6pUtkLDqFIXDmjZCZefqpGfxFSeQgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJa2LdCEahC65VjOpUlH9lV4hw1kGUXSUd8XyD6aHZQvVq9ttulp7uPyU606vIStqIZ1P8S6tFPj7JZkUvr5cQlMUnBAIr_Xx1dm9LfjAe7GdTnBd0a2ZfRA1ii7msDEPVJVahV3lUfxwEqysDHEPJJuhhh4vacllmcb46NhGekQOdpRlDbk37Wr5o9CWosGcBYSc_9KQOshrsX0S0QrIsg9eGi7YTRHcuNah0-Bx6L4OSdz0yH7mdpcS4k6gR0MdzhoUp2RshYh_tmZNwCcAAsVwitLxA9GMlMF7HU8LVMJQNZ5JrIWR3Dlyl6pUtkLDqFIXDmjZCZefqpGfxFSeQgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnI-Eu-oYm7fDAnIlZm9wl5OaBDNjEZyH8gxlC2NRJI6-3-aRRm_t9X1K4WcBxhMUkFlfjDOeWCCOzdQGTgaWcufRd_DxtLSY_iHtc1aAOZZJAgp43KkboW9XgsDdQseP6zwQASlyOgEoS_kRQvEwUq2l6uD7Xl1TvcKAwV13o7HX9Z7Yo-gz7ynCuxChKvAUGo24PG1rCcSnLGz8cy_6i-8GJxutAhqPr5muN-AoLOXLmn-mhBtUMNFX19FdA0ftwtrV7MCSrOrwrzrGTUocJG-F1klVxMcbv5-VwSQNB9W_QHEus5sysCT2ATBQaBgcHx0WEAfqL1OlcUJkJGroYnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnI-Eu-oYm7fDAnIlZm9wl5OaBDNjEZyH8gxlC2NRJI6-3-aRRm_t9X1K4WcBxhMUkFlfjDOeWCCOzdQGTgaWcufRd_DxtLSY_iHtc1aAOZZJAgp43KkboW9XgsDdQseP6zwQASlyOgEoS_kRQvEwUq2l6uD7Xl1TvcKAwV13o7HX9Z7Yo-gz7ynCuxChKvAUGo24PG1rCcSnLGz8cy_6i-8GJxutAhqPr5muN-AoLOXLmn-mhBtUMNFX19FdA0ftwtrV7MCSrOrwrzrGTUocJG-F1klVxMcbv5-VwSQNB9W_QHEus5sysCT2ATBQaBgcHx0WEAfqL1OlcUJkJGroYnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=NMj62a2I3M-VQ-kEDh4gEvlUsmxTdywgkwd_ifvh_ew9Yo6Q58_tpeY7lDucaCweHWh2_175g_1Sn2YakbkPeV9ijWfB_RqRpTzGGZ3IZB-gd0bbuav0EoGnfYYB7TVlCsPUe7t80Eq1CKY91mBUnCxYbG4FR6vEtcgIvjJx5JdKIg1B82iiNJWTOdsLvCcvlDbA0lP3P7sLrjq7lmiCoUmjx1ygpTJE3q1gdH44AYqOQzMo692G86dgP1-CVzVw_gjGeAjcQKAHlNUmYUO8DQC6SwZwxuWI-I9IVNUNLlZoTfVPUyWkN6Zruh-kcXPDwk0goYP2YHhCnl44MgNF8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=NMj62a2I3M-VQ-kEDh4gEvlUsmxTdywgkwd_ifvh_ew9Yo6Q58_tpeY7lDucaCweHWh2_175g_1Sn2YakbkPeV9ijWfB_RqRpTzGGZ3IZB-gd0bbuav0EoGnfYYB7TVlCsPUe7t80Eq1CKY91mBUnCxYbG4FR6vEtcgIvjJx5JdKIg1B82iiNJWTOdsLvCcvlDbA0lP3P7sLrjq7lmiCoUmjx1ygpTJE3q1gdH44AYqOQzMo692G86dgP1-CVzVw_gjGeAjcQKAHlNUmYUO8DQC6SwZwxuWI-I9IVNUNLlZoTfVPUyWkN6Zruh-kcXPDwk0goYP2YHhCnl44MgNF8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipLB6t2XbEWtNbexuA74Y15sQYj86eDIsuaNp3djZe5c9zfWG4JRKnfpl_auqmng2gQ1_Vlqjqk48dI3duLKZ7ojonQy70N85-w4rewF6J2gmHl9qhXeltnbRiJV9ekQ3JOr-0FL8KXKHxFct0WfMXuFBakmX8Ro98J6m1sSEFcWQWqRCr5FP9Ts_Cjr15SLeCfzXchGllcnIJ3AHIPKf6TUFgjJFIKHiv7bVm0t5Vo2-I2HtoimxYxqej66MivPxO5iCGF5X40bOvU_l8qQfThkWpKCk82TtTHqYN8FFGODHpt4KE7gYKpRKFlEhUZyLzhGdhhWac7FQnl_5BoL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc3ALf5BENhWsJSttrb-pb8-A9Hd3WStDh7X8Nuezwz1jcUB6101x-L-8IJeMRhTmULXRqOxdmG70OzaLZB6T11KT6aRv8R8VvHzm45_w5Hm5VnRTLSqKyM_R4LXz8qQfcc3Eiyy9z7SaTBjixq_4kkwOLicDldfGKuNm4a8vI2E3THm46RsjBq7Ak0od0SMAbFHFPW9F5p75D3eIU-8ekZ-rcZrKry9mMoBXzXxL814T_6yoCxktEmrufTe-yo4gyOdjytMiNeNBLvhQtlJzV2NtPP389FCJhhwxnjWjhcZSvyrGzfGSe7uu4sJPhFE2yfRv0EV8FjTksS_Qfy_2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=meRlo29_iYWPOqAQP1EyuUaGoouvMH1lN279UYNZasGbfxCzHk7EeR4hwuDFUfHjHdxr5ELJ4-YOkpRajG2fiiLsx531o1uvrbPBix_6zPLg7l83jYA8_3xxyQmEI5LCkzcGFKLMcBBLSmFwSnBBtlbmdLiNm8tI4BxQ3j6sWCfvto1zx3Q21ej_S-RoF2NfWHrb_itr7pciTMB58e_UVkhdK6susAj2eN6A6VQA6S2H5big2phyA02LnBxAGGxpAipB3-QytLyaKAQ_qaEdgWnPQxL1XFES7kzG3EJ7A3jklgLk4A5VlcP3874xQWsSg0DEAj27nRXDbZ7a1gspmYAL3JmHnXNBRJgPRDtLJBssnKAt406BiSAWDh_Zi_atG-wIeLYDZgbXQ6NlKZYOPrQO4e3QWmQjuh4y9fkrur7B52re2vH_quY2LFo48WmoCly2yOoOOAlTTBHsFBLSwj5A6TROFDsvEoEGnGY1zmrYHGx-DutJaBYpj4T-pDpNy73HRDZkcG5yh-pWiD67VrLYcq8eiGvsm99BefEblOM1vDj8HO2DTuL75nzuSX1kFQkvvg77kImSwr1R3MyUewJg7jZax58AqPsP6Z-vubFa9OIehTnL3LULIqtTW9fchteKHLUkuE1slgk-FBq7Cv66p3d5VJu1t2zKLVbtLGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=meRlo29_iYWPOqAQP1EyuUaGoouvMH1lN279UYNZasGbfxCzHk7EeR4hwuDFUfHjHdxr5ELJ4-YOkpRajG2fiiLsx531o1uvrbPBix_6zPLg7l83jYA8_3xxyQmEI5LCkzcGFKLMcBBLSmFwSnBBtlbmdLiNm8tI4BxQ3j6sWCfvto1zx3Q21ej_S-RoF2NfWHrb_itr7pciTMB58e_UVkhdK6susAj2eN6A6VQA6S2H5big2phyA02LnBxAGGxpAipB3-QytLyaKAQ_qaEdgWnPQxL1XFES7kzG3EJ7A3jklgLk4A5VlcP3874xQWsSg0DEAj27nRXDbZ7a1gspmYAL3JmHnXNBRJgPRDtLJBssnKAt406BiSAWDh_Zi_atG-wIeLYDZgbXQ6NlKZYOPrQO4e3QWmQjuh4y9fkrur7B52re2vH_quY2LFo48WmoCly2yOoOOAlTTBHsFBLSwj5A6TROFDsvEoEGnGY1zmrYHGx-DutJaBYpj4T-pDpNy73HRDZkcG5yh-pWiD67VrLYcq8eiGvsm99BefEblOM1vDj8HO2DTuL75nzuSX1kFQkvvg77kImSwr1R3MyUewJg7jZax58AqPsP6Z-vubFa9OIehTnL3LULIqtTW9fchteKHLUkuE1slgk-FBq7Cv66p3d5VJu1t2zKLVbtLGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=ZUfH7Eomwf1qQLw4JwYZh2H9ehi7xrDMOzbo3Wqjke8Ate_95QQLDKaffB0jYM0-EAkUxBeN4NiEI8nPox3sI1G1va1HBvE8APs5_Qb8esoq4SM_gzYcUCrg_RIuCJ2DzfxIiJc9yib8HSpHkkP6fkd7PgRHAkgo8L7dEFmOKhlUNMIMQUmpRcpRcCRO86VMfl4Yr3fzwaGTqbLuU95IZQi4AXMiNRgD_u18hgKW4KUx88DMKR6_N-5mtrcnUlj5hfLs2_epFCC_K1ppWGVNf8h-DrKB0dzlOxaDv8CaK3gx7ZmeD8zTsKThXGBY4J2Lecx-QFM58AiiKtPnEhBQUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=ZUfH7Eomwf1qQLw4JwYZh2H9ehi7xrDMOzbo3Wqjke8Ate_95QQLDKaffB0jYM0-EAkUxBeN4NiEI8nPox3sI1G1va1HBvE8APs5_Qb8esoq4SM_gzYcUCrg_RIuCJ2DzfxIiJc9yib8HSpHkkP6fkd7PgRHAkgo8L7dEFmOKhlUNMIMQUmpRcpRcCRO86VMfl4Yr3fzwaGTqbLuU95IZQi4AXMiNRgD_u18hgKW4KUx88DMKR6_N-5mtrcnUlj5hfLs2_epFCC_K1ppWGVNf8h-DrKB0dzlOxaDv8CaK3gx7ZmeD8zTsKThXGBY4J2Lecx-QFM58AiiKtPnEhBQUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZwkhGbzVnQmoBQeuneEoilBP7GICRK3NsscDhpznRtYzyufvDSiFKDpg_WXva9aPDXh0VlEMvnBJ2uAHxNTr6_UH4-i3aLXcAZlyKW3PXiy-ZRbL99ChpDP8BJhNdzhj8XmSowSCjpRG0JyeNfzwsRrc7OW8t8zqoGCe5Vy9_Rf4jjlJ_MtEh8UOflP2Ivhm1SZCfwOnWJQEYh-0eITTSsxxJxrvxnwFS1i-ITRPK-CEDoL5dGM12HuAsB96wyayKpRbgM1lY1zjUW-RYAq_jdDWLB1Zd1iv4CBf4YVU6BaaNTUs2K34LkD1ukL50am5QiBjP-ZXUOiSu_VVdHBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5pGbsMN8vPlNGibuUenrG7CfB7R7mBXNXCBSmzQLrrFDqLKsBh9YMfl30s5gVn3_k6OvDpRR_q2wEpXQ4yx516ITAMrJrldYL-u0ipcy1IkoguelhsxNSPPrTwoETtVqfN2pPxV2zlQsk2bs5c4sFanxYrd0ULhJE7LimCm2q6pW0SwjEvk22vKWeGPjtmU_2g5AnS5ouoNW9Q6bxSV3TWIOag3q_QFHxhTgNNj2NyxN3E3-Wz-r81jt-RtG1-WUCuabJV074a64-J0ms0Zxiv6TgHe1X2Eunj-ZmQAqhrtZB0i072dWoJMO1I12dWxhpXeNWbD8S8JKF9lF9aeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1K5t7Oj1QqPuCGWdrDlGWH85Mtmwxvotl-3paNp60l1XQydo4cYvIZlikVy-U8MskQ85G3tRxcsEBRI1hOBVkV2QzID8sa0Vh-2BDw4Cl0MJZdvq_IPF4gZWfklC7ijnJz8IhJh7cvBmddr8HRHmFkAq5ajh1SiiY90WC3CDh4H_cTF-SDIDutpIPoQfjKxWAQcILfiFQTmDPhzeOC4H999qjVTMxkwt_uYFqk-UIW5vpFHDFScTJNveP7OTXi3Hia1XZy_JZVQ2NuYiVQBMSZns9p2KIe4hMA2LKJswnflHa8zKSgKTY8JO9X6kS3LRJvF9SZPyldsKiQWhiNrOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=NUAwxzKlmcwtfnSYyOidEnLbFv7q5E8x4u65VdggR3tZpO59OTmGEmnMs5Eoq6iIYyB49I8xsin5ULgZVwfLg7vf2GFY9QxoE9TcbPgRS4OFW1doNYXyEShxqqCfGqkHrbd__9_Z1hZgTckHjQtDCyY5jSbpBhrPRSdZ1yU8jw2JDPS4Xaj_3WsM7eoK_3XPSUIjmWFld2GuOfREdDxb9_1Ux4KDa8WV2x9fl8AwjJlXNR2edE6FptvXcyJCPrSYYR4MJBKYBbk6U5F97XuTeQVTB5MsGFXPDsfYuPCpCgBpdWknVpm6iPYXDY_0UxZ9LQAuJ-sBcmq61wQ1yPhFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=NUAwxzKlmcwtfnSYyOidEnLbFv7q5E8x4u65VdggR3tZpO59OTmGEmnMs5Eoq6iIYyB49I8xsin5ULgZVwfLg7vf2GFY9QxoE9TcbPgRS4OFW1doNYXyEShxqqCfGqkHrbd__9_Z1hZgTckHjQtDCyY5jSbpBhrPRSdZ1yU8jw2JDPS4Xaj_3WsM7eoK_3XPSUIjmWFld2GuOfREdDxb9_1Ux4KDa8WV2x9fl8AwjJlXNR2edE6FptvXcyJCPrSYYR4MJBKYBbk6U5F97XuTeQVTB5MsGFXPDsfYuPCpCgBpdWknVpm6iPYXDY_0UxZ9LQAuJ-sBcmq61wQ1yPhFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=NMqLQjtcMMw6GyNlmZO38uVLc-RPPQZNndmj8co3qwrOre6cJolSiT-Y6cUN-TqaNG0XPCNqC8MYDkBJlJWZq8ipj3_n5Q197irQRJexupfrfgNpk8OpoXS04rxkQgkytjwpWVp3qv073_dNijTmTohLWPhpkm24AdFpLa05U1PNBKfYGgJI9jM-HPTrVD1riNgN3g38eLaypP5OFotTKccHu4-hvJA-b-FDdD8vkBkcfQDOhfjg8Bd0rZWUdBgJWP2Un09WLJaEvG6idb8SnXQYKo9_wiNealX0JBsWJA9bE0FpWNUVc3l8KyYe7qIDl2S49CGs7XFwxkE9kbwbxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=NMqLQjtcMMw6GyNlmZO38uVLc-RPPQZNndmj8co3qwrOre6cJolSiT-Y6cUN-TqaNG0XPCNqC8MYDkBJlJWZq8ipj3_n5Q197irQRJexupfrfgNpk8OpoXS04rxkQgkytjwpWVp3qv073_dNijTmTohLWPhpkm24AdFpLa05U1PNBKfYGgJI9jM-HPTrVD1riNgN3g38eLaypP5OFotTKccHu4-hvJA-b-FDdD8vkBkcfQDOhfjg8Bd0rZWUdBgJWP2Un09WLJaEvG6idb8SnXQYKo9_wiNealX0JBsWJA9bE0FpWNUVc3l8KyYe7qIDl2S49CGs7XFwxkE9kbwbxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehcOaNfA6GWcgI9wGj5VWbIK_6iiROHq5F9H2hC37kshOUtNwPI9K5VNf0weqnZIMIxY69Wam3hE3oxvU76udNZgGrHYTuOJEKQ_wVFYJDLXj604sjDwmShQ_WLiW4WrDhyn2baJPlbP5ubl2Udd7arM61FXpo14XVC50uqmJKXYTAsfpo4PWQY4TpG5sgQf7kD5BjjQA51Oi8YhL343-5VAlB7BJoMbNE1kLI0v-GH5a1Yc9sWgrxL7hKo1PLpnNLTaNIVBohPoxpAjbYoMJs1XBsU8vR1Km0TqRMOTSDSWCtegmdNB-i8UBS2Y_XYeZbcbI4XRN2QNHIAiGNCtAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KODaGo6MyI76zbCFGPg7un5XiiL-K5nZNCY2KkFDMwsyRQEMbnpa6GpgkkLGKsRgavzaqb-yJY0beZXQO4AB7Ct--Sf4MvCGOwC6r5REyLCmAiI4Qv3FdgXRLeiLY_DxDIAqraoUyp8VVmKEVhiW0OgH9ca3eYXG09DZoFbAOfYrj8LSZhQ7P6IdDbsY46WN-hPAmgE6Hut7sghy7VKYohSZ9YMaF1aaSKtR5bvSTFcsT-iRld4c2STcAmgtureH7YJ9i4LV5PiWeOwc6chv3n4KBPrwVL6qvaNDDQqXRROmJGHyoIJPwbQBIy1OZuEIaMZK6UEOaTWmcHw5W6LIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=iPxdmO0RoXL3BXsEc6M8JVr1CFuGogQr0i64CpsN5trKbtPKkAF3C4A1o10vV0q9EALg6whaVv8-XOaw_MnfVwbYZrku7MftIpTwwKMrwo7hMlycAIgi8VZ5XUDWWJRnLheZkECVvQBvY18Zssa8Zzc7xBg1uiLHOMpkaTMUV8_M1GUXm_Sc0vgWZch6sUE89-HgYA_NfpOptO8o8EMqvTykLVQE2f8TfElJwsdQsnF8jX1xXpNsHx0SlowAzKhpMbIiqLu-3XCozjnGNzCOJkBZoFlmobmfhNu3ZrQS3wa8OlNjix7nBAImHBtxXFtTjnBKuymt68HMDJjfCLXYFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=iPxdmO0RoXL3BXsEc6M8JVr1CFuGogQr0i64CpsN5trKbtPKkAF3C4A1o10vV0q9EALg6whaVv8-XOaw_MnfVwbYZrku7MftIpTwwKMrwo7hMlycAIgi8VZ5XUDWWJRnLheZkECVvQBvY18Zssa8Zzc7xBg1uiLHOMpkaTMUV8_M1GUXm_Sc0vgWZch6sUE89-HgYA_NfpOptO8o8EMqvTykLVQE2f8TfElJwsdQsnF8jX1xXpNsHx0SlowAzKhpMbIiqLu-3XCozjnGNzCOJkBZoFlmobmfhNu3ZrQS3wa8OlNjix7nBAImHBtxXFtTjnBKuymt68HMDJjfCLXYFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWTgu_eCD3bU6swBCXW2orOZ6mEdB4IohoT-qvy-d5g-AeltecB3UCRadGJmNG7WSFtilrqcCitAut9z5UboH2-L1stA1X1ZtQmgfvTn6_u3kXLXw8QQpanzJa8NAca8wxFVNOFvVucs3-NleDjkVrSHS1HhRGP8b-f1G5_-fGirmURUYfdMIfYEXJgKctygdomJJdUr7WKu3gM_5FSlGRpAblpOwlGdhxTfctjLLFUfXMeVAUk9xGZ9d38A_eVxcgfgIp4j0R15UoByV7Iw43CkXTuBJ8v_o6APnuv-yIIIrvHyDnWLI3ukmaYpUdC8CT_CMeLlDwYLzC7K_mvaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9a_W0MfbPJ2ZWAM52XPEO5o79DIH3F0oADmOz2wnzNdePKlg_AVsrp5tcgKo4Aj62IF3wBfPMQ9MgKzKBVnJCYYqipr2B2dstNRebsZwiGjHQPmi0PCiDluSvbVdEb3ZKY9A6NCWSlSzp47JFnN2yZr_iTjYvyjxT-rqsc_zeIjViwbSX9Xb2gaEVaDow3sILkuIFWMfm-Hy8Vxh_WYlf_6Fl0VEtO4IiZ4cMFN4apu9HM47xHWJcjYCFn1qy76HAvBbcgmbiRl1viElfv7JP8Nmzj5_JAtYwWu58bV_oXFeczWRJMQ3fEOqm1eI-aYokL1j3rnbVKjnSFiIvU9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obtOeJy-_yc91DW7kyFPHE6gy8d77ueme-a_b9Xt2QAKUWEeDZdYsb06zzQ6hHjJsRO4VwciC8gZUedXWZXGSpAb6RI97ni_BsTgDQ_zrJR-l5Pyf5sIkS2fNpkO9nu7pCpH8lm3gzWKR8QivMSwIqqEFHhf8GHNl81FvMVDF-t2t6XaeVR29V3ZY20pxFYgTrv7kd6cyZ50dqMWft2WOZM_bKZNTHtEK_K5zBrz2XBAnk65rGM7Pe7UrIeBNS99VQ59bDOtmCXYORw5k-mFT8Vj4Q4tqB1Jk9YmJa8p3UPUPCf8Z8et3N0TzCHVAL8GwMRkRhhL1mUG12T9aUls2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5xJMQBNSaErlmGiqFJZmVDyZhEeL7rc4dizObmkL25G2enN2AwSywrkHftfMGMioLqfiIiy_a4jHEW1F63UrwlPtV_Ugi1uWiINBRB2iB1zcNxLftDLm5DyassiGl7qQejVF7CsVzq5YmqYo3Bbf1KcJLe3X2GqxW98dKkisktvSW7ikusrNnIGF3SuKg0xJiH-We0UTP5ScY8PmYa4O40ykBDJzLp0ZZM0U_I6CvtmVHp9buZfb7QOPZc07-FaG2dYT9qedekm9iggZx95sb93-UOEVPTI9yoklyMdQJPpfPTwvBH13TONi9BQK5gzCkZFQwfqy9hJooectLqvGTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5xJMQBNSaErlmGiqFJZmVDyZhEeL7rc4dizObmkL25G2enN2AwSywrkHftfMGMioLqfiIiy_a4jHEW1F63UrwlPtV_Ugi1uWiINBRB2iB1zcNxLftDLm5DyassiGl7qQejVF7CsVzq5YmqYo3Bbf1KcJLe3X2GqxW98dKkisktvSW7ikusrNnIGF3SuKg0xJiH-We0UTP5ScY8PmYa4O40ykBDJzLp0ZZM0U_I6CvtmVHp9buZfb7QOPZc07-FaG2dYT9qedekm9iggZx95sb93-UOEVPTI9yoklyMdQJPpfPTwvBH13TONi9BQK5gzCkZFQwfqy9hJooectLqvGTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVB8j0cZz-0W8AvqprkioE2RhTsK1EgOzHKPneCaKQ02Yk50madHka5l-StZMAXXhK6IOMTjCC4pTTWkQa-fnhBFQvidnLMJcAj52JkSy5QUah1Ikyj9jb4InRUzZ2crE_ReN81KfNDbUXVvpI3tvoU37BSzU6_ljFp5YsUNG71NHiYrvNLplNW3Ipk5MAY8-4elKO4n-JnXbcWicY__Dk1J7cC5OQOkOKKt4gBsf0sEQWXC4RdGJmuuGf-VxVwjvhtCW55IWl8C8XDjvgpl9n2g_A-v7LX2eHzAwmNXhakWfugc7BdE7pmv02hrLdQ6kfZWE6_MviP9plRLQNFCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFT90zK3r69mP0NgUMxJ8EMbqYjpu4Drs07-5hxryr4gyzFdSKwY0ELygsy3CC7oUu2s5gqCn-4NL4gzAYdJU74ODZvvrSEtxKw0AY3DlC2lRFlW-w_jK89JZvWUuWUSvhzP90eW9AjiaTiHeUqzpaJgApZF3DR4kuLUpl_XSFADLJK84eQRNe9si3eHABXYjFBBYY9JR2kmIvljYjSrwLcOfzxIjA96ougc7RWmvwa3C6gPS-W78z5AFx3k9YYiJiNLA6vH0AfkMlHPA_q8We8sIlU_da1rQNYPbkLoxr2hk-CBWSXwQIvqmOMA0e7oSMhKc2hUFn6nHjbPlJpOnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=rjE7m9RIzrk0lkYQnAkpkDzF3GbdI-q1HANegLZ57yVELeEgsC_7JexZoUxdOeV91QT9nPASPIEiT_TJm4PEvk53OJgYaLIshXkQTvtS0TaOz8UIBz3bR8lWIwV0WnUQKZIwLG0gHJAVs7qN6MLSoTfwA7n_TT7gbkEF1eM19eBnf34OfZvE8sVUO5ooQnAXOUbJ50NqMxb6wrciIchsnZM9OlHFSOhsTJbKOXk5Cyr759UtypgyZNKK09OSm5sloDFtLWyEa7NaxZp-1IXpozN_eHuNsu21DgKc70-IPJZ26tDLBy9VPbT53ELyKXfFYGp3rShJ90j-tHxEOPwBLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=rjE7m9RIzrk0lkYQnAkpkDzF3GbdI-q1HANegLZ57yVELeEgsC_7JexZoUxdOeV91QT9nPASPIEiT_TJm4PEvk53OJgYaLIshXkQTvtS0TaOz8UIBz3bR8lWIwV0WnUQKZIwLG0gHJAVs7qN6MLSoTfwA7n_TT7gbkEF1eM19eBnf34OfZvE8sVUO5ooQnAXOUbJ50NqMxb6wrciIchsnZM9OlHFSOhsTJbKOXk5Cyr759UtypgyZNKK09OSm5sloDFtLWyEa7NaxZp-1IXpozN_eHuNsu21DgKc70-IPJZ26tDLBy9VPbT53ELyKXfFYGp3rShJ90j-tHxEOPwBLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=NkQ_K_fIpMzrzd-yiM-jkbqs3OFyQPfL_wt04a8atbZbvGd7inUVySZ6mxMfH9GLanpe08nVqb8f9zTvdYe2alfgynV2X65lQG80SJ2ITludX3lxPU22NtVzlZByl8GLguUX0b4nF6Pw1-1rQV2SqO0Mc2UYAk1zd9vrbVQ6v_SU3CLh55l8jK7zXMZXrCudpQbexg8eeMmbbGD0G68map5FvoDOy-JBjHqpN1BjQbAv9Z4tUH3UUk3Hs8kohJ_LOtSKXPy0z5MWrUwnm3HmZx56lmv7l7JTszerrYYFWcGyGmq4WXoMP0sFYwim24V1sT8k79CW-lCx0Gvzu16yuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=NkQ_K_fIpMzrzd-yiM-jkbqs3OFyQPfL_wt04a8atbZbvGd7inUVySZ6mxMfH9GLanpe08nVqb8f9zTvdYe2alfgynV2X65lQG80SJ2ITludX3lxPU22NtVzlZByl8GLguUX0b4nF6Pw1-1rQV2SqO0Mc2UYAk1zd9vrbVQ6v_SU3CLh55l8jK7zXMZXrCudpQbexg8eeMmbbGD0G68map5FvoDOy-JBjHqpN1BjQbAv9Z4tUH3UUk3Hs8kohJ_LOtSKXPy0z5MWrUwnm3HmZx56lmv7l7JTszerrYYFWcGyGmq4WXoMP0sFYwim24V1sT8k79CW-lCx0Gvzu16yuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMhfnOR06jbZr9nAKIzW0yCPLg-2BEWfTcjeY4l2dprlQt8sxuklCKdba8GRQBE8d6aHk5GA9RsPBd3Ny-CrxiWlzautuhrrujLNehfMAjAiJ3aN_vtFjWInN5nbea3STvxHss40g0jun19EfQRFfQhhUQCcQnHZZ7QFHGf01SmI2sJXa7XRt-N_Lm6QqN8Oz0MdPHylvKzqzw0Pe1z4kf_ZAxD7rH2_BvxJ6yXKy49vn36MBzsWV4dNcFzyQe-xHr0mVJYWpt1x28A-SUV2Rr9hNIodNoSbipdrncst3LBrQpWN5SkdyXUT735BXtogmdMkYMocKJPmmVrkJGuZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS5LJVWuhegBXKWctAmHTveMQF1_l5q89q8HCd2UGu8jiOX0gQxG4rhy129kkRwvcm-y_tzpsqUdu2P_7hOSJdzvXkE_oWOMehXWpo1J4yoORoacVYmBVL-OpXyNSnC3SBMgiQKqSnnR3f6MDdNAQ9uWx_fKu300-uqLMxw7O-F5feAurdIF8WWis2Rp_3ylmtaSnrZOO9g6VYYg7_ALIKjNEHiumx6ICOYnz-yBjqSn_gDDBdHwdEOITezP-_xNksivB3csJzKkHLLpTa8ZAReAsvZg-exHMyx1C6O9eZFSwauGu4adF9JDiyFkWWlAKJbu-lkdzLnZ6Rq-WVaxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IDMu5-Nc9gDQUGsKITj-80FLavBcKErJ59srpIAAGWCod2G30TakbGPWkDrvKku8U0P2QDzZ-PBuGuYGn0VC1NfNAik14GF23G45KCU8yfxWaZTKnqXpgTpdribZEDO4Vn33OF5Qx9FUxeq-ZV8Yj0as-4yPh4oR7m8gvPzQyY3QCAJYQMoB2ku6_VTzft6wz-x1BsdqGMPqgXRxmPYXwEWuRiWmBdBDJcbT-LH4AM91trMwy-XKVDS6UaOoSKhkLyUZctPJQ3G86cZS0W59cUvJbwoQGoy7hfaX0qsZjEBpegoRtOu2V0MWv146SXRBnJNnM8RREpEqxRuSVtfffQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IDMu5-Nc9gDQUGsKITj-80FLavBcKErJ59srpIAAGWCod2G30TakbGPWkDrvKku8U0P2QDzZ-PBuGuYGn0VC1NfNAik14GF23G45KCU8yfxWaZTKnqXpgTpdribZEDO4Vn33OF5Qx9FUxeq-ZV8Yj0as-4yPh4oR7m8gvPzQyY3QCAJYQMoB2ku6_VTzft6wz-x1BsdqGMPqgXRxmPYXwEWuRiWmBdBDJcbT-LH4AM91trMwy-XKVDS6UaOoSKhkLyUZctPJQ3G86cZS0W59cUvJbwoQGoy7hfaX0qsZjEBpegoRtOu2V0MWv146SXRBnJNnM8RREpEqxRuSVtfffQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=h897D-nTHXFaInMR9PoEtomr0L81SnFVpMjl0NZXD2O0as29z1Oo3_sKRbyxuSzpOZ8PMOU6Qi2cLGlE4eFv1pkAJN6ipAJBsvPkcmFVYH2IIygrFw-PziR_KsSdHnsvD6o3FUtdCnwahefru6dEwI2UT2hxDGhc7IjZnNr3dA9YOFKOWsesNuzsqP1dl7PwR1sIhAUgFR0wfYucr6fI74s3NKx8lVEYqkClGBnFGuWCx2Zkj5_mhTO4xoVqowkA14tMVGPGtHKNQbUUcT4Wghk8bWdscLyoX2fTt3TbZIMZfWdArg2DMOKWXBbSGDgzO6B0yB67TN0i-V1-nFEzWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=h897D-nTHXFaInMR9PoEtomr0L81SnFVpMjl0NZXD2O0as29z1Oo3_sKRbyxuSzpOZ8PMOU6Qi2cLGlE4eFv1pkAJN6ipAJBsvPkcmFVYH2IIygrFw-PziR_KsSdHnsvD6o3FUtdCnwahefru6dEwI2UT2hxDGhc7IjZnNr3dA9YOFKOWsesNuzsqP1dl7PwR1sIhAUgFR0wfYucr6fI74s3NKx8lVEYqkClGBnFGuWCx2Zkj5_mhTO4xoVqowkA14tMVGPGtHKNQbUUcT4Wghk8bWdscLyoX2fTt3TbZIMZfWdArg2DMOKWXBbSGDgzO6B0yB67TN0i-V1-nFEzWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2_Ntj5qL4R4kiEV8EVFHl-46LEQqLm_-DU8qBN66qplvTJ77V-2YnAkKvMAdAuwZSOcpIFZxLOjLsWVs-CQf9arGIspLVGwe2y_jpCB_eFr2LwL1yQh2SNuvGDODKjh8WUJusqe2b6Ah0gKr4M9ORaNQGeikbGYbNfKrw0FnYyngnTWBred9JAQMjmoYTc_NQMuoO_kQXxMuIOrPaUCFINL1SS5yeWNBWq9C7im2UBsBxDtnytekwlGpxL9jAVh2ZdK-FjpAKdfZxrjWtLpH5zN6_tyXth8_uaJNTUfsRr13jW4vbrK38ptsC_a81Yran6hbpRcxOiHpsMiLrVr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzCwJY82H9NRh0k_UzJPqjVXcAvjiJ4B62DXeAqoZ1TVKP5fYgEFaj4TtI0Cnuo28q82nN8j0sCEplYQURz5_w0IEMsqDHkbMZAyzb_LNr-agfKgsFOjID0zlgcn-DYKdoN3P6n0h443DNX6Ez7FlwvPlN81iJCiG8DH4ttpk1chI6u5Ot_-3GFMXktK9X-uBb78uaWMLHvb7ACf9N5dg04Z-x_Rw5RT6WzJPB8GwQhd9fK1gM5SDPsbo7S8s4jbkbFVKa1W-p5L-4vJxJvwV_GHUZ-Y4xRwHEsYyB8BElatFQVAYvTmvWisLPwP0dYC0kOXpvAtmU7Z6f0GKSjqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhWWTOYs8UV-nl9sd0eJ17vJO1U-nlfbA8Jn3CNjA-Kj00G1wt-bdMN1RMQuD7mrUWWH-qwjDf0gx3aJp1TobeaqBvg4nwMjQUk0ohIQeAmnoyxVONtjqAMagS32cGzss_4ST2_JQ8DOhHA_AsT_1VfZQsb211OYWl2iYtENVQEaFqE_qLXZ2Gzr06OCyvcAAHxAqMs-czCnxjDlomIERNbWDohK4Jg4yX580zqIkCtaDhtPmRz0VvcPlw3n0O3CxNNqsq8Jna-CD-ETi7nKOo9ffrO8KBKhhsb5ATMxzMSlOWtt15J0M-6P7_bESMNzFMubISsstrW_prdwfwLN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiV1qPb2FMJs6Zl_UVvzT0B33-6BTOJxJUSH28lgC1cUfGNyfcEfewqdGVJqfLKfUa8Uu3jBytAXmlAGarkjjlOP_fOqEM1SRpSCPeTLzL-L0ivJEoF1ERacxXOlD8BZo8oK3SpjlgZHtez3wbtysTXNmmhwPDuEqmDWYYQkQTANXdkliFbMUOf3afESGYPuI44i5H_j1Y38wEQHA8l8ItiRBimuOg5Hnysb0aDLAosN8V2rZ4e31ROSNEhZ2EJyAJiPNsLDT6WORJqWrFPCqmQ8F-rGfPufr1lxf4Ntz0A4A2hhhgcsc6sf0ifPKtRVRW3D7ZCp19Ag_1gpFdvftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkAsDx_ODsobvAQMqZfC7V7amhiq8Ea3GOTFa91zSFJ-ynI1_lKJmG77H8g7xztCYTDzx_ToizNa3cYocQJI06AHlOh6G8z6DlRYiib4K7vtN2R2mdH9mS_xDHH6Sj6bKAzJmZLkASFcnLit5Nm4ahvH76Ky6dTCTjhYOtt1uVawvXcjAVw7-SmAhCYVidQ5tkYkb2-vSH7Rz4YF2tX5YZogiaulIaoa-RNx-a7ieHUW90yGvMYby52JJ3cWxUvh7DrDWNPXubZ7RDhma1g7RULs-dPtSgOgBn6msaCS4oBaaKNzlDfmOQYp8eqIVRi2Ju7p0PY8pG4-FVtNsKmU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YP4-8Jxz3wBxQkKs5RnGnfM77h-KNiMxTA15FGvoCVJR1vZ12OFK4x8yK9qt9t_XcL3_sIvNM2dHfQnXE0n9pZeEIIa2KQ3JWQCUBlT-z8I4MiEDJwQ1T15GIWvMU2nmhGIZ7h8aGP8r_k77R4CU6fHPe5fRZna1_L_atw4y09SEyhcOrGUQPhNA7K5ne9ktLVGYem135RXCdKtanKytOayO2G3OhOsy0hsvK3rDS0IQVO7lLIg8axBpZIz9G_rubp8eO_EAFE1Dz8D3ND1tOtaerQ8K5IZxivZ0Qwzy2fzaGZJ589tZ5Og3cRR3w19_TEEI0x4rVNrRgxNs-y-onQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HktCgFW9Cy1VSByFdGYfOHhEl5jbJgqieOdRUVXI4Lpenbg6q-E5w6Fi6lZw89BUBguQQToth3fyqA0z5bDXRptmvy8bRVWUnZGOBK4Aj0shJybOBzsDSA59-eu0UHy1t655VeHvx3N2rmut-Jros88B4fYgX-y6kW5JI0UkGNFIV2L2zgtvae9Z1PyC7q9V2vUIEt7YS9zf6zOdu94kdCOz-MGAb31A365TkELg6cZ5nMSpKs_CQW47BwAnNcQan6NZhaOzipHyw5mWWZP1ngOOHzr0PhCMwfmWSsC7zJKwEeWd6_OOh4XYPNdKkB1T4sB-1Cxrxf2h0ltAVf7W7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAFBYv8OaJ0_lqjN8vn3yWs407AXoeNEgxQt6xCm2YpmmGBPA3pkPeM0yr0cZQmq71SQVT9tXx4gMUPO7Nf6_dZJcSN6JifLEsDpEEQ8K_9F7OnKE1mnn-OyAQdIlIHusDCGVPBteclEi9zy70ClZGuG4RmcRL-1kCdEdv64jNZ83Y-nC89P8k3JwEndMv14lp7tCzQM9XxtzpBEQzG3Gtf-xN0zryFm25kr1_5WZMTrTxsVBhbTaNQHQ1nvOny5bDhbjCYFpZKkZCmn4WxMNEDuXXyraxRtlwTCdvb8TpE8QBkaNodyqbPcp6nKs4HH20qbpGBbuMrPUQXYaNu8Uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3Rzu_onZdAsDYFWpQfrt5OXzIB2ugd1hT9H23lhqEe6ZcEAzEH6x-EgTl1RBTtgbFIFC80MGV_WmOJtj8Tng-lqluk-AuCiGsRnDFkT2uxiS5WUvg_bDmzdWlVg-eSZdlKkGYGaNOPhnroz00alxVent6fOLzwzuLfCljklsy5iOoqujJ7mFYdzXZ-W7faYY_FIdtEDGDSL90oT70dCyV385-u6pXMbrMaIsq-vvJD2vT30xsIjZ4fRceILheFP_U5vjHVveRiclokcIEIssg0WpYZzSdZ2DnU_Txma8rExhT5yIrfa25YoWuvM7nkqz90hh2kt6JMyApmofnbC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KppOXs0uT-SjEfPfA8A8pSAkBXDt11VfRn_9SuCFPKmE6rCI0EkgZtPYmOZhhHNaueoGxA_sobyHi7U7taZ4Qh3pavX04UFDQNy0sJCayw6FRvaio8pVCqwzRpl1KzO-87S2VCWwR38rbB1oSCvldGIC4CIRB7pXgCwfaihW4S5nhZefAoFxxT8ApJmENKgC16TERgEpS1MeyN1ng1pYr1MJGcgyejmROhQQgbZNkTAv-Rbl0iAh1bP4kEiKBT9v72SbNIsSzstMOwZgl1NE9x3zBT7JOYA22yVOlet4Bq3m28BsRLiE5jj8h8XcN067jAVlEQaDqI3ldJiPSIZggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=N1E6BTAHc3oeZq8q2Wsxc4UwJjIqjXynfcwLZuBn-9n3meO9vqTTDKN32eY4M4LgLDHvbxmMB0s1JDp1BrcK85iF4Oui7NT-4ZUEbJnJP6XImg_JgtiDDkNkYtKIYhcnmcku8r3X2e6mD29mucQZ_jVts7TVcfFMFaac3On9f-abEpW76s0FClDmGGQaQ3lN6d19TfsFzSVYCE0HBF5EFKplthbAzw3504J62Zd-TDXVntzVF80DYlflxfk16wvxPtXW0AHZdxzdEpc4LbFhrzH6DHpPQxfx5yJLMozh5U79puTmV2o6K6TNKALqbRp8b4rjMTyHMNAloQbY8fFJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=N1E6BTAHc3oeZq8q2Wsxc4UwJjIqjXynfcwLZuBn-9n3meO9vqTTDKN32eY4M4LgLDHvbxmMB0s1JDp1BrcK85iF4Oui7NT-4ZUEbJnJP6XImg_JgtiDDkNkYtKIYhcnmcku8r3X2e6mD29mucQZ_jVts7TVcfFMFaac3On9f-abEpW76s0FClDmGGQaQ3lN6d19TfsFzSVYCE0HBF5EFKplthbAzw3504J62Zd-TDXVntzVF80DYlflxfk16wvxPtXW0AHZdxzdEpc4LbFhrzH6DHpPQxfx5yJLMozh5U79puTmV2o6K6TNKALqbRp8b4rjMTyHMNAloQbY8fFJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=EBWrX1fb8yBWJQw2WW1WbMde3xTv4UJHwaJ-KfHecxQ_kbHKu2MNi-hUuB6zd-ptAVIGNVvf5udrPs-eLuwbWtNk373bZ51aFv0Gvp8jiNQIw5F8loKL-OTNaap_QNEYXqOtaXAys1pGq8nbqAKpH8Xeu-7PCgNOB5QlibIpRh2nhP-PwXAXtZh4HML6AHqNvH8MCF5qiCMH7QHs6TQeyhyE_L_CCRWJ2FJlo6aG02TFeyKkiGRRKJTdnEEdqTKUV2qTUACa5L6raxK2qSojBD8D2pZpTKSGVYorYCdl-dw37c6dOjWOMx1q3HQhLMns52vddutcEqV7ip1MoC3i7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=EBWrX1fb8yBWJQw2WW1WbMde3xTv4UJHwaJ-KfHecxQ_kbHKu2MNi-hUuB6zd-ptAVIGNVvf5udrPs-eLuwbWtNk373bZ51aFv0Gvp8jiNQIw5F8loKL-OTNaap_QNEYXqOtaXAys1pGq8nbqAKpH8Xeu-7PCgNOB5QlibIpRh2nhP-PwXAXtZh4HML6AHqNvH8MCF5qiCMH7QHs6TQeyhyE_L_CCRWJ2FJlo6aG02TFeyKkiGRRKJTdnEEdqTKUV2qTUACa5L6raxK2qSojBD8D2pZpTKSGVYorYCdl-dw37c6dOjWOMx1q3HQhLMns52vddutcEqV7ip1MoC3i7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=T9R2HVZu5X-xVw8YEfZ2jYsjJ2ZeV8y4rP96kXvAwpOfM-cSQtEyX90GgZaNVuEctpfil3PMWqe5vh3g2ARno2L76ATgNAVFiGOoFh5mX0Nq685Z-hY-SO01DPP_Bz65o63kXPzUFY2Flnjc4AkfvKGOrm8mPmb-81q9zLff0HP2xCnvmBl_BtVVlz4PVtK0btnOyla3V91BN7goRt8X-pEbetRJ0G_po3GbKiXvkUJTY1MRyrCWXPVuojNpyoHZkbaCEvA-rZYuqwivtCaor-JiTzZVJgQHgLDWukSbfTVzh9wvH4gUxUY-PhM5chCqKQqEdCEQqLJd4IJ6xd724WM_tNYeN2mLb0Sd65xpW2afo9BfhtYizamiYIKWrotEfKd0xwnLXCgi_d8HEq4J5k8SC5j5W-e2PhSUK4tK64UpEor1INYFFo9Deehzmf7R12H7LzMLLeHQommGCXb3nBCUCDfIC_ebks498RUofZTY_feYRSNzncviqKo4JPyI9qB6-F-YKe4U4B6f2_-ADrZEEQZrPabCMJlPucLpan_tQg27D9LrBywiwSTam_eDIFay25eJWJYCDgN1pbUJ1znfWx70y-F8sej38fGYo7C5YhqB1ycZ_pzjpBDRzm1ncklTeXYYTVCqR4rqA36o-NYIErpD-W2WMeAjRyRQZF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=T9R2HVZu5X-xVw8YEfZ2jYsjJ2ZeV8y4rP96kXvAwpOfM-cSQtEyX90GgZaNVuEctpfil3PMWqe5vh3g2ARno2L76ATgNAVFiGOoFh5mX0Nq685Z-hY-SO01DPP_Bz65o63kXPzUFY2Flnjc4AkfvKGOrm8mPmb-81q9zLff0HP2xCnvmBl_BtVVlz4PVtK0btnOyla3V91BN7goRt8X-pEbetRJ0G_po3GbKiXvkUJTY1MRyrCWXPVuojNpyoHZkbaCEvA-rZYuqwivtCaor-JiTzZVJgQHgLDWukSbfTVzh9wvH4gUxUY-PhM5chCqKQqEdCEQqLJd4IJ6xd724WM_tNYeN2mLb0Sd65xpW2afo9BfhtYizamiYIKWrotEfKd0xwnLXCgi_d8HEq4J5k8SC5j5W-e2PhSUK4tK64UpEor1INYFFo9Deehzmf7R12H7LzMLLeHQommGCXb3nBCUCDfIC_ebks498RUofZTY_feYRSNzncviqKo4JPyI9qB6-F-YKe4U4B6f2_-ADrZEEQZrPabCMJlPucLpan_tQg27D9LrBywiwSTam_eDIFay25eJWJYCDgN1pbUJ1znfWx70y-F8sej38fGYo7C5YhqB1ycZ_pzjpBDRzm1ncklTeXYYTVCqR4rqA36o-NYIErpD-W2WMeAjRyRQZF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipAtHQgksIafqvni4TCxqxyyXGbUfBjdpRHrJe3jdxO8S6hudKjBzTPc9R6EvuxA513jam_UsWV4Lj3b6P30Xt_yN67TFy3L-G4x1z648hm9hYrTWe7f0EOQlyjKW1MJLruzikZw_FebLpKOFiZYQkbQhtGmtfmF78cnAELQeLmCeFwdKssqGAsCgdfWdB2q_WONnkHJSn8qVxUxIVhLnVKB6SCBvbh9uJZXPaS4LrW2NZpFpPdnfA_OPOsAAn9ovj1RUmhRxAdypvASaorXZWIRWDnhq7BOBcOrY96JurNSY-8tvOzxdlx-4EkkMxkCNjXZLFyD2k9YT04wSY3xAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=kWKbEf73AgzLJvJ8TJD34cBeNeJfFg7xowvMY5JrG41hzCXyS3OinbMFHuNslc3uHMX99Ou8eH-p6iHcqt2ilgkpeDSs17jjn2z2Gy01n3KXLFLwYhgc_rfPLrnF1TQGKi7J26z2QwhzEWSyDDpJdFo03deC1ztE-bGlMBY5oJObnMf_tv1REpiZAMegEBwbR0Kq6dcE8lB38JnvflIelxT_A_mCrL_qf8HZ8mVl0vx9X1SUGwfhtywdZ0QKfFPbS6xAwBpTB2NTfYnweK4StAo_IOcZGUV-Kq3PdOmVblKORz-lgauEBNNB-gUxoe5fwRQvYH93mC-yasJdjTAIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=kWKbEf73AgzLJvJ8TJD34cBeNeJfFg7xowvMY5JrG41hzCXyS3OinbMFHuNslc3uHMX99Ou8eH-p6iHcqt2ilgkpeDSs17jjn2z2Gy01n3KXLFLwYhgc_rfPLrnF1TQGKi7J26z2QwhzEWSyDDpJdFo03deC1ztE-bGlMBY5oJObnMf_tv1REpiZAMegEBwbR0Kq6dcE8lB38JnvflIelxT_A_mCrL_qf8HZ8mVl0vx9X1SUGwfhtywdZ0QKfFPbS6xAwBpTB2NTfYnweK4StAo_IOcZGUV-Kq3PdOmVblKORz-lgauEBNNB-gUxoe5fwRQvYH93mC-yasJdjTAIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIYQd8GwdAvTONKdDYA8rIsPjhKI-qduWTrxy3YbVTuY5fxV9NmwvuH1fESwXbmbhkxadIFznPJ8KFNhKc6pLpFkhDzQZ713mKMxIAD8SJd974ku3Gvw0CAUsSP3ddxfTmCo80JPBVY8Z3YXCcQPA6aSGYcGOdeyNdSWKu5RF7k22nqL3NDMiTMHu-7NN6F6cju1Fwbf6W4_Vs-QboUygaU_io5gLczTylEDWW6OQ7ql7lw1R6EFdu4MGpJBUN3UWyB4C83r3Ml49ZNrHASYShZB6WcNB1ZCQxhm-oeWVEf1Xz_h-ysi-jq20zbTjbIu4oHcoJ92HpbCDaDafCQsiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plUSd86MJunw55HvogxcQzudm7lWSJLYR55WErK8ZuwWBmJ8Eg6n6ubddwlZclcEzw6t0i3gw70z9Hi2gDFLj8Ic_pCqqcEQJLsehmmnPsUVaXO0bXlXSyAljbaMddYzj-hqy25IfHn737JXVAVWGb8aLwXIEPn6p-AjpeuZHyckQhgQHbrEBbtNDPXC_zpFJGZZk3Ry1MLCXzNUKdZhAhTbGJpiN8PIHbiXRvprNIJvihi0njZds1PirSSdzI4YBO8Zf0j7ZfMBnitzDJ8gCQ9Dl-wb_UV5IFVmJX7k3EHaP2KexajwPSODRnipyHqoUkbcf9MseRJFYbHxGTiIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clTtsx0k7i__wtyc3o8R6aS2cateL8XimwJryxwjzfTHb-kI2hdcoOAZVTGOGU0ZLyiw73_FLoiLcHuW-OChLcWczADWR2raZlTqTBwmmnws8mSaJ700TYfx8yrdhFLrrQkL-gjtx-k-LEM1soqTQZVyFDYxnNpuWItGs2epvMMF2ERh6K4dmThP_pOBkHxoWqWXL9JWLo_lE13FOhPOG-EQnMKlQSb-_CydMxSgdXHvbPnKb1kXma_f-W7aVSwjlLmsX-5uDUx5pwCAWfPv4BoJOridxWNrdjIUeohDXRU2b4LaeYhkU5OYlzJo07iJilfIBdmnCK3oxTxNtq2LtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkzDnLae9zhhUcwB-ODckArnqEnw_CVYThMl-ROF-GZuFlmKaMhCLJYGYfNZpGUIGooeBo4yQ8BW5_PbTrrzWjmTvqGzoFDBGXNwmG3ooADLvh6_j5UCTfhsC5CRpgL-Roul1HN-oscbwIW9sQAyU6OjDN3w4VfRpIJ7tzCmJMDUZaTZbL3IhWf3zmmqjx6c8DjfJhvQsWP8U1XEjj5hJKddbaenMetUz_517oS3mj890aKjDInIjDZ_dRle7lNZBX2iNhmGF3mvjsDgIXc08njQRaB03tb_4V6B8AzEne2S3lEqBZaNXdNpo4Cdir9PnrcRUI_7LSVrpae7GdQhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOyDYdIkD_0bc1_PRDlpoc9FHpUpnSD2BlXm-Oj0pzM-IlUF0Ga-rZRDp8J_YyKMMep3aoOzb_fnjiAl8fcFMFe8mk-1wPJDuRBght60WZAqa3oQxc7aKxx2qF5e1E58C_zQEnkrzKUVGn1Z_mCh32VAoMJ1aUoHfPjSjv2qtsADCaES9oaa2iV2Q-oVloxj1RQUQ6OufeOVYVnCIYg762m90rfKw1ZMRQYU4cpu4QMgG8l4C9M4-PDIgqggikOFD3za0MoArIbX4Eqep1Eovt8xR_GLscG-eIRX-5BewCWC55mX7OReyCMC3bJSKBuuEKU5imIp_ZlaeC8hmfLhVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFfFuOQBM6qQ7iI82989lOsw8DhQokms2wiqwoVTPsqUnDoITn7pRcdYlLHLm8TZV1s3ecKsHaRuL-iQniTWhaxqivXDYU91Lt9_aw051lyIEY939AnTPwl8ETkXZPrJRwI_lqK0DP2gHCuML29z6RSyBDkREnP8D6Uo4dmJx4dIkBKWK8FErGLUnvaqAaGWcH8849j0ajXkV8cXRamEx7ImjT-S5iniNenSgQ5wiFAqbYYOUA2zh64LWEx_JsbvSFgPEb_hIpRqydWxePm85thzmJ2NDdKNTyRzd7wUT9qFQjNOsVVHAfPA_8mb3T6KQbZ1Uz0r-t2aJ-2NECDUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/II7L4W9aoAzGcrlOrNZB_PlROa4HlBHZ4F7o3JMmuMoM0gDmO2sUTPaoxTGHiPeGRgDGTE1jQGT0bOiknkNmRlUUVMTwOr2ZAdkspj4yNUXUEyEb9eRxzYxhtHPQssYutC36IJbu2mTSfrP33bafgplM-DRuxr8shI5BPojTol9arWjwj2Bk5XUD7k2yVhZ3Y7NRVSrctSOJLxZt7Ec3yj4JGmObaP2TMZQ3fddTFoEkUs14MGD5jHxIxpWk0gSuesoywtEMGSBGqtV2jhV8AFxmCFtfV0CnHRj4ECUhd6C5lvRHAp0y_gXNaI7jYU-gSZdSm8tZn3coYVUfalMkEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPhay-4hYH4g9VaeniPnIYrdGSonsZTR_rXglvdLEZhnBsjZp_YRJ3ZqzmxCLjuGrPTKJEuxagBtfjt46VPZ9KEPrhMQDgoJwmJpb9ZCRv2G4RsKjzBPR0VX810E88pJLWlzn-rCzHCVB7j5UQUA9MrspEqoxZa6AL_2HpJ44hClvu1srS1q8V_rk083SrX5AE40_O2GxDQMvd1zDEDKnKoWJPbQo2PTCq-LQG-Cy48ACcOcGD3TweMFFi10otdEpjkKdU5Bhi52aPxWwbIPrFqkCuLPD654I7w86i-96EMgxsXeZDkhCYk-BZZ_VSdPr9ZVq99y0R7IGy2gHh7BPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OI2KkPYflq88oi18JEITly1SDCsWm2a9M6NmGJQckZGuPHF5ZkJJnmixhK1DWcgDFkhTPi2zcDkALZOx_DAa_CbguHIS9Br4XU4KOmo7gguEa8NwKjZh2vtU3Y-06F8OwYM7vHZaIL8nohDBm5IQ2S3R6EUS5KF3859nSCvHn14daKizjR5aK-daae1blyFAQIeNDIOe1SvtoN1k3s2E-50Z1GOqM3WszqtFSasTvW8oEWhH6Oc-Qqqass7NqXf1PKVWQXpP5DUY9sdGNMchf6v0PIi1dCBVpF2He3rHfv7pA6_ETpK59QMohjsCl-mHb42e7Zf9fXEYLFAENZTQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWMPar2WaqgFRmASdXuSi0y8DWGvFIL2KKipFSaf3E49An9sVX22qucTJzsPBzN0fWmRy7DzIuYivnHooijxVT94RBwZi6PEIiVafxoMNkgg8wyZFfmqWw44BLxtLoNCDSwTByn2IIuPuT7PGt4j9iz1ZozKNMktHkSEiUBT-lsme-DtNC0mRIvcNrqkWVMTdLnlVD2Xhtf1lTuVgOFznlzFRkXCb8mgh-W83mlKXkn8lNBTEm_MDv2iNib9P2PU2WaCxP_9pQqkYqGAU3Rtb_bzoVMbFvLEYNcXlZGkJvcWZayQAaLEXRNVPd7OBE8_J-7PosvZj-52vj6CecQEuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Casq7WFo4wUaTqS1U7Mmjs-BV2sZev5Kz8cU0KZ4uhczY2X3zGze5BIgI8VWq0Q6sTyFBebGtriZ-kwpoepgSOnkSMTuxZd2gBPSafi1ACE9c5i94zgfOD24PpOQbk7OXyLq4WTz652ioPTAB9aOaFtJv2W6wvkzY1NA2Tnk5gRRO22aW6q1VgecjpScbPxqAR66tfmj7ArRq20WI3gRW_6ZAPQpmwt5Sn0qPi8HroiaX7o9MywmsUY_xLjJ9b4HUzKIKBpFr7_xCIcwclibRPB4i72B2v4VGQnskJIigLXzqd5dySzA2GKQvrayIM-xXLctt-fqMn_TDDwp7OifoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzBMrQBwOFcSwp-5rCqZuwVTFV3QgP1DLA6aGAKWnxDEklHy09Coo5lY7PSvOod-dA6jkcfrVcfRTRd4vLuzMH4ocdfJOmpSUR4R2zlsLe-eyt-iCl3pzwvP5oP7_9lrARyuAlE-qcfTBp2h_ZYj9YcAMKRZm_Rf4JD30q8RImHU9A_nw9K8DRZ_WC2QHLR0nPdE2_uHDsrhRuYZGNASJNvYAeY2jkO3Rkk4Q4USf08ggGjKMw1TsqtnI7r0HsV66jFUClpNBQ7H03Tx2jt_RobiN6Iq-x2HuVFota25uOakO-QR86OBYTScFvHtm_2_NTiWoBIHin6qsaOO8RxJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
