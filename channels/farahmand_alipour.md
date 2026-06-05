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
<img src="https://cdn4.telesco.pe/file/kAyG8iFHCkRzAq93ck83Zy3JcYaUprpimvrD-o0m5yGf0zooCjBz2my6cx1eCGd-4d27nEgAH_2ZtxM_FIC_SiCCYbt4GuNjgDWA7-Hdxd_s01rTYe5uEOmKMyT3zaXe7KynCG3MAGeOFxscJYztXqCD0kEksRdGC-3cZjbuXfTMm4NB-5tPFkfxWsAfeiZYWBGHUIFHR1QG9Qnk94bzy7O47N4F_89YoVW4UaFnP__gx3Z9AmK2cw2TiHDSgcnW5mkauwEh9dif6eL4JNYlavS4cGePLvEN59vr2Do2HaOkWSp-oz8VJpYR2mIvK3mmqtnM5J56p_AuopbYVYqiIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn4rctaDdCBmGggT9sFib7X1aYnGvMuyw-58TkfHSN3H0qxf03rRMgsCgptYbw1uAGnpmnk-1cfVMcXkLKOB7eagWV3Cu5GnP4Igwpa_LmkVn9-SSy6kykNn9RmdyAf3NUdMqrjKEKZyxQArH2IY41UM8v4L7mw5p01Y1FmBm4PBAGi2gj3VC8YnC0F_zJYEiqN2MBFPO565xCuopu_GV19NT65jW_Bnr8TR6x9Nb0jEoZj3Ra7Q4yV0of-r8oHK4mHtYd_VWu2y4ZF8oPlzVidaXPA6VSDn8pUDdVndSKYj0pmLWVNJC95Ns3BImZ4mrYvzaQ6FwV6NEnCu0h0Brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq936ugl26sbwnyE8iB79fB7noR5SqHorlpTfEf4JWFcR4T8eaoDeYDG48FmljMzDqMRdMtFNeDSPO-OZuF9ZWCiPlunWVwEFQ48jb_HekziTxJDe8_xWOvuAoKcAPb1J_lZ3JmWM3F4ZXLbEccpXTzdxcw3O8Ykkk6FTIjNQ_wNYvvaawlMT0YMXXFwwD2PX-MScveol36gyZ1r1mGap2XVtIqv0MwGzLZvWo7DsOligRE2Af1fL4zaL5yYb37mvqLPOC-y3qfiEdAvsU--D3Wn10-8zc-pgGSo9zt1WJVytyvxbqwwYeia-8BK0elWrmaO8DheQlBRJhAKLBC24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHvkA2-Dj3tUl7FSvylFdSQv1bck_z2znJ81R_9TNImi1dwvK0N2dWN5M56XZWuNR5KL5eI5XaEDVKGzKqItANR5uJrx4hbjT8scl1Lmok_dU4vhXqdGk9qcAfGiB1VI14dE7nuDIL5xZ2u6DQ1Gc7G_D0_rsVZ8mDMBuYh_Yu_BwV88LSnYq1WdoBNwKgbOEQ6dR3peSyeszuo51UmWBQidFKy_ojrdPwyKns9-64bCparJVEHjh77Fi9k2InkzmelO0vfVUQY5Gh3Yh5x1DtPJPdF6BiUDisG6cnvgGzr2eyesoQSEQFrpwOjFSaq7Kgbf3kpN-C9XLD5N13jIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRcepXoxx_9gwFjZdTfHPXcsUjHHg_L1Ce_LnoiOeRDWdmLT07fcmHPLEho_-eWN2CxUuLstnEAgAjO4PKhRATOYjZ_YjAN8yRaY51VP6VP7O1YMg7wSHXiYA5Wtr5HJlbqDmwFEvMPI9LIBl3tPWdhnlHve0JAPXLGSvu83sr488GJwilbD0d16LmQ-tNxko8aQwYH_V7vy6td3l4J0iTYzleInsbEP4izVLO9p6d9Pns4lCZNGLCDcd3uZbVMm4ZkI4CoxbUMG_JoHwjp1bsojskGbjqOQc_y2n419-6B2ssY5tvZEGxOG0DmMF8L2OVLgY6dL3A4aIMRbcPAxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPQwDsb8e5BbH1hHBk83pdT9vAG1x79B7h0LBynwZ8NPcttZT5t3RZopf3hiWBBIv7zpMES_kv-3AWxgm-ma703Uu2nAx4--3HQ5b5KK8QyprJYZ9Ft5P5S97-VAKMwUo-QsunXTOQ7KcmsjlmuzbaVXvSL1sfB4EfGoOvbt6jf_AiZTzFWg1_G0QFq4aDz7AkSXX1ynXd6PIOxsZVA2dbUQrB4xdLPIEoldADTVvkmYTF9u6DhTZmrAR6os34aoVIF3XBtbtST4oRCo3oUSJlUc00N81jLobAJ0zjLd2Nj7V9Xw9yrxeItMrKQxrMm4ynMaC8bhmRAJY5cnOCQO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc7NeffMHacldACBXwHgF5KB9SWjsA0sz6BxNQeeGnJE-jIxQlN9t2ErNgCfzeUItF56PxYjnHLcBuelWVdoGpaz1osWXqIdC7EfeKEE5uwz1T8dONu3kkzI1TBluBsnmvHxLKqmiyauifcRfTzMUhcRTWmaWynDqTor0yBJcRh3JrIXAu8Pc-s0wEi7jxEIWhYsYErpmZwhHuX8CYUWGs8mQdF2qt9y-Oo-5BgiVAFlA6afJTyFra4MDCbMncbOYi8b6pcPSahlaJYSjrN77QaZhCM7H4bMRL8PcC3kVzeH2v7OI9iex9515vHqU-mH0Rvt7oZ0_c_FYX-z5VjIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=MCKgAEQguAIld1A_9WoBR8dvN1VLtRd3ZEjvPj8JTU0SzHrQtsIoJ20-LvvETRmDPEIHehFCwxt_28PMF2auIjN6CxqRO8f0jGDe3GiekRWTIGkFENiLq26TTcZ8W8kT2ajG8Ils91owdcmRGhiDbU-i4S-H5G8FgIOWqfVBtT5-6-zsoIFcRr_Vjy-XNTQ6EiR-xtxgtccrc3C7nz_j2skiUvYgA3gTgUbNqJsJBu9-oPiKwOpob1-oxa7SOMIaNbWAzj23-5ofvNwX6wNe56EasTY6tyyieGUtLHTTGCmpS5WN5k-jo1Q3IybXhVM_YyFD3QviT08eJ4z9-quplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=MCKgAEQguAIld1A_9WoBR8dvN1VLtRd3ZEjvPj8JTU0SzHrQtsIoJ20-LvvETRmDPEIHehFCwxt_28PMF2auIjN6CxqRO8f0jGDe3GiekRWTIGkFENiLq26TTcZ8W8kT2ajG8Ils91owdcmRGhiDbU-i4S-H5G8FgIOWqfVBtT5-6-zsoIFcRr_Vjy-XNTQ6EiR-xtxgtccrc3C7nz_j2skiUvYgA3gTgUbNqJsJBu9-oPiKwOpob1-oxa7SOMIaNbWAzj23-5ofvNwX6wNe56EasTY6tyyieGUtLHTTGCmpS5WN5k-jo1Q3IybXhVM_YyFD3QviT08eJ4z9-quplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXAg4d9m3z2fildsIFEeiF_hxvaCXPfhNuCe1kpgf1CtsIur_c-10yLssnoGsAllr2txX8Nib4gl_bmXHLlYsoE8DRgsrRPiOi5bQYoL93M_dD0Y55vS8FEPD1owpetQ_0CjpnrOS0mQYM3BQ8CxxuzZ1hbZWo2lLCeJgirtWh-xTdJa2CmkLOHWI4PDleBXQzSy5k1YrQua53DMGPzzPoKsiXdubji8yv5sGS7Ji5gqpPYEb2E-p6oeJYhy3Lt61pNJkUaoWiD59zolz3i0JNUAVrR2dnWuuz1Gcab5haxgivDgnbky6PqOoPmHg3_kDRvh3CaK3TAOvMDanjGdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1734ESwsqR2o5BfnS3oqPFzI_AM7D9UotvMeaNmmjDKK4H04dH8YztKNgBT-0Q5MarEpOhBSYlxJuZmatt1OlKfKrrswm7XGShks5gbHiaga3G41Pmsh3X1EQgBGwVwxJuEBniWmEWfJlEwnIY2CrnbHdERtBwPhhhhVSMXJUxZc7yDMwlGhkrwvsCwJuK1Zl5xUtZiuCDsJ75LbVvu1Nri55Wy13HJU9R0t9NNMMyPB7z5oCbKMWbsPuvPufs8fI7f4TSaPPhE7mAhzFlIxR4hiQoHXnj57gMwZ0MVYytEufX5TrBo1OkVLlzF6-eXBq42lL5hqHIHf61zuJUAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQg9UrjkJUsJkot8EOtdanfFoBF-KAJOxXJX1hUv-2uWDUIeNIQaKdskVhAraneTbP7JL0EMcSbvVGtP8Y8WMkXgepV-I22IXgSLxd3ptcfZ0XIE6Cu_Xk7KfLxipqgL-zZRZd5s6FYoTS2sUOt8t_ghSY6bRkg3HfTtKIqHcCWtKPegkzEfRe3vBUq8n13QsGFzZ1m1dpTCz24jflgdowjSPtiz3s23AxOEcBHKBwd8MZl2jOz6by0wIDtMT2d1io3Ueuo8uhXS9jsfvxuWuhMHdIc-xh3uEOP_DmYeeow6Dc6uMHzVclCFPKoBWB9NCCWq8Ito7-_5GLypEXGFgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=h-2Khub8dwuLU0mtdtQybAEMgMcGadUHctvcwaA00FjjAlN1tPXDzsbV2LSDlBZFqajGnJkH0jkAJi4ZvHOt_X8fCM_KLQUUPHCe5kNylJAwvBXfQLHjzz_nuPXcKzYRos9k_7ZzU29lZjE_jnGqIpVSMN6vYApZz0u4--2Qmxr6HH8O4ejUfsLiBWC5Rhw_Fnqu0DxPE7-S-PFrSRw2pY0GAeK8GA4nfbII8B8thjmv5HEhIxmZeBvh-Ydv5tGuw8jZiSBJXe5DmkhfvkfFMni4qNva3-dTgFiRXTjzg1vK0KsLXg8DVY8HMIc8PLOKTri__U7Rt1Jaq6Y5Gi8LpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=h-2Khub8dwuLU0mtdtQybAEMgMcGadUHctvcwaA00FjjAlN1tPXDzsbV2LSDlBZFqajGnJkH0jkAJi4ZvHOt_X8fCM_KLQUUPHCe5kNylJAwvBXfQLHjzz_nuPXcKzYRos9k_7ZzU29lZjE_jnGqIpVSMN6vYApZz0u4--2Qmxr6HH8O4ejUfsLiBWC5Rhw_Fnqu0DxPE7-S-PFrSRw2pY0GAeK8GA4nfbII8B8thjmv5HEhIxmZeBvh-Ydv5tGuw8jZiSBJXe5DmkhfvkfFMni4qNva3-dTgFiRXTjzg1vK0KsLXg8DVY8HMIc8PLOKTri__U7Rt1Jaq6Y5Gi8LpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=Lr1ROb7msXrQXpyntWm4JY8JNEtdgFfBrRdW6ij7WLcxpalWZNxxnenV_okpWVpVuwcrUdn6yjy1OBVyhWv1BZAY9hqxZBAo1AlE6VxLUbL4g51r8qrSF5fGTv5VoRhHHFtvC4PoKyITg_7CjTGWUEKK1zocrShIvF78i8Bk45lWb8BuQ6zGcdr8drbAlpeY8exftXYkofH2aURb24Tmpw1Heb8pyLh25IzwIZlBYStVWjvqR5i5CjuNgFK0nCZrcxdS0k-IU3eAeozTW2t_8O3r0lNg5vQaIpBr0aBLiV2Tzu8jCAq1VZTTaIBODOPH3CKYTdJza0WonKbauktR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=Lr1ROb7msXrQXpyntWm4JY8JNEtdgFfBrRdW6ij7WLcxpalWZNxxnenV_okpWVpVuwcrUdn6yjy1OBVyhWv1BZAY9hqxZBAo1AlE6VxLUbL4g51r8qrSF5fGTv5VoRhHHFtvC4PoKyITg_7CjTGWUEKK1zocrShIvF78i8Bk45lWb8BuQ6zGcdr8drbAlpeY8exftXYkofH2aURb24Tmpw1Heb8pyLh25IzwIZlBYStVWjvqR5i5CjuNgFK0nCZrcxdS0k-IU3eAeozTW2t_8O3r0lNg5vQaIpBr0aBLiV2Tzu8jCAq1VZTTaIBODOPH3CKYTdJza0WonKbauktR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJatbVr9wU8S7RSh7iUAlY03H1-MafY9RulTGe_ER08nppsb2zkslFHsgQ6HEBpwXUe9I4ZRPaPJwLtxJ8rTn03LOWyj41P5dpd0T-RQ6CV_1XYLVzldsck6bDc06CSLE-Uiq8i0hfh7uNZGLhfMdCVfQn8pt_SRxGdtPdIDYtZsK-FtGJUaE0crvgjjn686B9nNF48fkNsqBMLxXQkOZAbHbw4Qob-Q3abic6VzzEatUzZdrLlI_mhHArfbmEZ3LcGLWDHImM3MYtX_Hdk1dEEkJ-i-_I_Al66w8LMuH9WXwbH37VIpGXlfP01N1ZX-9xd0SSMOhNSQ2GnL34sB4QE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJatbVr9wU8S7RSh7iUAlY03H1-MafY9RulTGe_ER08nppsb2zkslFHsgQ6HEBpwXUe9I4ZRPaPJwLtxJ8rTn03LOWyj41P5dpd0T-RQ6CV_1XYLVzldsck6bDc06CSLE-Uiq8i0hfh7uNZGLhfMdCVfQn8pt_SRxGdtPdIDYtZsK-FtGJUaE0crvgjjn686B9nNF48fkNsqBMLxXQkOZAbHbw4Qob-Q3abic6VzzEatUzZdrLlI_mhHArfbmEZ3LcGLWDHImM3MYtX_Hdk1dEEkJ-i-_I_Al66w8LMuH9WXwbH37VIpGXlfP01N1ZX-9xd0SSMOhNSQ2GnL34sB4QE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj2QsYtbUQ9aJM0MvD0I80tY2sDysRMnJTu4SbZEamgZMYNtvWHscRZL5EN70lN2WrfUeM5Lrh0Xd1ufT2YmTh1C_cfMnVab0pms4x8aXa_mZp3iwEoMDtpXRdmdLyysNvPx7QhOOwCen_xxIXQwQ2t5X3Ho3_xy8jnIvH3rhW9e4YwoZPzlegAjRkK-sZ5DnUC4obeDBX_7-vUh8HHFx0zIaDdsygOAYZftpsRUI80UR-zye3-WDGVr2iiqCq0VhzB3LXNtV72EcN3UfdDe_Lw5isY7Th87ZFkvf0tv0FwrL35SZYWvGUc9F382BskIKb8JiitptAxEFmgGJWcdhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4JrqjdkAKLAzGyDSwTy0rpuTiXkMrBJ46imhkImn6--XE2dz-yw3EVE1Fd5ppRqGOtcfPsa7dgmJt3V6IW_Jhp00NEnPMdrLnjY1cc-4jH3xlH-TVlL8VOslbNGjhn2J1s4bDV8NBym4UJBImmCNI4rVs2wGcihEMsGaIf9x-SBkhB0-Js8MjmIsP8HLfhipv-5vnqBvWjb7cOOCRT-1DhLCkDCezfdIO8tsCe7U-uSrYItT81MGjCHQCwD2MbvAY7PfUQjSI1aMzFqOQ5qHdP_XzebcFEcEwZxed1U1eUTnMXcd9nVT9YZglj4LWBo9G8GGMVoXEFX24xL61MzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=dsaliq_6DWYE8KHuih0fQKmYhCROn_ZdOu-i6Rkvh9L7sfMSOJW2umkRaCQU7u2Ef-Snm5xxUp0yTc_Y_-AVzhK42KXumvAFrqrvlBMri-UOnoZXIvI2ZUGHe2ixdX8AEIOQAakWRluypqc7ghnvqXbTsp-iwz16_Lw_TiEb-MrLDPNUD7nNSpdqAqcrQ8R-mZBnsXx_dSNYHz-PWEBDDaVJfk755vGVUbyrw44Dzq2F8FO3_DREDHB3hq9IU9T-Pu85_ymKpnI_N2BAfJ_u8UMgMAUDueJgnQTBoJj0hpW-64YNpvYPR_hkctMnQyHwzB1b7V3k8cuJjrWMBDcHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=dsaliq_6DWYE8KHuih0fQKmYhCROn_ZdOu-i6Rkvh9L7sfMSOJW2umkRaCQU7u2Ef-Snm5xxUp0yTc_Y_-AVzhK42KXumvAFrqrvlBMri-UOnoZXIvI2ZUGHe2ixdX8AEIOQAakWRluypqc7ghnvqXbTsp-iwz16_Lw_TiEb-MrLDPNUD7nNSpdqAqcrQ8R-mZBnsXx_dSNYHz-PWEBDDaVJfk755vGVUbyrw44Dzq2F8FO3_DREDHB3hq9IU9T-Pu85_ymKpnI_N2BAfJ_u8UMgMAUDueJgnQTBoJj0hpW-64YNpvYPR_hkctMnQyHwzB1b7V3k8cuJjrWMBDcHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMP7UmUxNXlw0tKW5CW4Hc16WhpW_dFmejAOne9tM-7Gx4BNBbAphnUC9h4ljWcHoqeykpc1TPf70oBmw7VvSjjE1onJIbVJygfdSaCNsePQSRv2UCHwJoLPhw9z0QAR222FMqn_naBGNGJsXB6gZCZy4fNCftSB-M7LK6SUFpm64abHW-_e5xxzP2mjNbJdSdEROmVwDYN_S_fOM0LvNTZ1F5pIRzQacMU5yCyetUmkxk41CpAoMT0O4VR6IzCpvLdLq_R2FN50vI70kGVAtdGraDC7BRI_bZm8PCVWWmMPHEC169NCVTI6MrxKxDf1K3m9xUMiRvMjA9DbMuHf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=v5AFaM-C4eNNrg_cDLa_5hOYJ7_Z8a0CTwUY776z3811kqsfOtVpbF7RHevcsOzZbzxnr8dUkyeyqN1PeHtF2c4YzhIWiQ5URMCObXW2pdyNvuumOB14MeqLifBIi5KK3Q-mrTng8_Ajjj-OFsCOSBijkaZoGdTcZX7vlWZQAvzytRx8RQ7xY4TIVF-iAY78kW3euofrOm6V-tsnbgXuroB1ipuJagtdT6CG4sC4J8NDfrjPIN9yt7QlHqIhAoPeezesUHIdMut8Lad_BCLbR8LITE8IHuu2H9BrPKNtBQK2Uw1EdCnH60t9W8Pj82fOJKXCEADDsfXCRw6ChMa9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=v5AFaM-C4eNNrg_cDLa_5hOYJ7_Z8a0CTwUY776z3811kqsfOtVpbF7RHevcsOzZbzxnr8dUkyeyqN1PeHtF2c4YzhIWiQ5URMCObXW2pdyNvuumOB14MeqLifBIi5KK3Q-mrTng8_Ajjj-OFsCOSBijkaZoGdTcZX7vlWZQAvzytRx8RQ7xY4TIVF-iAY78kW3euofrOm6V-tsnbgXuroB1ipuJagtdT6CG4sC4J8NDfrjPIN9yt7QlHqIhAoPeezesUHIdMut8Lad_BCLbR8LITE8IHuu2H9BrPKNtBQK2Uw1EdCnH60t9W8Pj82fOJKXCEADDsfXCRw6ChMa9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=JXaMZg7P6cjAT2habvQ_JfQ42FxwWPqErCux9dG9oRGt-SaAz-4A51raFpLnH_eBywRq8nTAVAHNl5t257WZ2kQhOvQdIyY0wKW-Th4iWhZgwRo0slohFxhBWhIju1kkpxZfRe85QlPsH9T2jRsYOSrg2FjirqHD7IaCHEXp3hLcqgf2_O0r-xpe2lxk_TBh2bINy0TY73CSMgQGGF9s3DTq4eDSIE5XCKPw5tjrirqjTh2OGQj5vuZKVUrKxxGq_R4oYOLNcICXpmTEpINwoENmEVrLO2uFMefuyOj9b3makKtRCHZwxSs17ostm8JKu1Sd4g1b7d34YJpKLwPjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=JXaMZg7P6cjAT2habvQ_JfQ42FxwWPqErCux9dG9oRGt-SaAz-4A51raFpLnH_eBywRq8nTAVAHNl5t257WZ2kQhOvQdIyY0wKW-Th4iWhZgwRo0slohFxhBWhIju1kkpxZfRe85QlPsH9T2jRsYOSrg2FjirqHD7IaCHEXp3hLcqgf2_O0r-xpe2lxk_TBh2bINy0TY73CSMgQGGF9s3DTq4eDSIE5XCKPw5tjrirqjTh2OGQj5vuZKVUrKxxGq_R4oYOLNcICXpmTEpINwoENmEVrLO2uFMefuyOj9b3makKtRCHZwxSs17ostm8JKu1Sd4g1b7d34YJpKLwPjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=sh2yulm-D22WVDmijL9EG_uiKq3bVdROZ_fIO_ttJHiAjGNKdQDfG5lStwBqxAdVpOJ2VNZhjjFDjzBpGh9qBSCDB17VhOJ7vnIkL0CX_bcMBaasK-A2wZX9L_nYEsXptKaYRO5EN5c7ntvkAHkDaduXL09pIBOqUk1LOx0LY8vhETVZD_MrSoUe94hI1KSo3vPG2bZfPIk2JvDOxc4UeN2XewgQMPD_jbbr8WM5fuGSZN8oBuzTjbcQnCKyzeu6LQiuHdf_TBnoSsX9VA9_n2B3hT5QoPadMdN_kHw7fD2qV7JYSUaGR3b16By1NRlWjVShkVrqcr20FbNxP0KsjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=sh2yulm-D22WVDmijL9EG_uiKq3bVdROZ_fIO_ttJHiAjGNKdQDfG5lStwBqxAdVpOJ2VNZhjjFDjzBpGh9qBSCDB17VhOJ7vnIkL0CX_bcMBaasK-A2wZX9L_nYEsXptKaYRO5EN5c7ntvkAHkDaduXL09pIBOqUk1LOx0LY8vhETVZD_MrSoUe94hI1KSo3vPG2bZfPIk2JvDOxc4UeN2XewgQMPD_jbbr8WM5fuGSZN8oBuzTjbcQnCKyzeu6LQiuHdf_TBnoSsX9VA9_n2B3hT5QoPadMdN_kHw7fD2qV7JYSUaGR3b16By1NRlWjVShkVrqcr20FbNxP0KsjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=DgVLYDS6ckutIyiQ4Ap2sXfhnwRMRLzdzHlnCCKDgGjG-GeFeRMae8mjvzQlxK-SAKLz407GNqvJtY0qxk_XqAzPb2E8PxahRVvS_Rs3sQSBgeajXxf4UAr9Rd0U9dBc50Fi12kkWBFyQ-1HJq2CkO5MMxBM0W4M16utfbYPVJyqN6hLRrgmGl6n_BBBCO9u_UQu8a84eVP9YTF7UtcytHWcDDrGtVXlBHgsjd8TB33P4KP76a7F6JX93mQmc5oPh0ZRrbBMVBlM_pmcGHboDjAoR85hj7jugXDbMojq8MJiL8IYq7o_nFuPfCXZUhc6YoqqC_HMcuJBBFenyhxZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=DgVLYDS6ckutIyiQ4Ap2sXfhnwRMRLzdzHlnCCKDgGjG-GeFeRMae8mjvzQlxK-SAKLz407GNqvJtY0qxk_XqAzPb2E8PxahRVvS_Rs3sQSBgeajXxf4UAr9Rd0U9dBc50Fi12kkWBFyQ-1HJq2CkO5MMxBM0W4M16utfbYPVJyqN6hLRrgmGl6n_BBBCO9u_UQu8a84eVP9YTF7UtcytHWcDDrGtVXlBHgsjd8TB33P4KP76a7F6JX93mQmc5oPh0ZRrbBMVBlM_pmcGHboDjAoR85hj7jugXDbMojq8MJiL8IYq7o_nFuPfCXZUhc6YoqqC_HMcuJBBFenyhxZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGutFFGEIXQ6oE5cBlyhzQd6jfvTo24AHqW7SCRpFBNoO9WMrctBvjp1FLNL7VSv7l9xyceFN40IJCLM_zYQtbpzcViFFpJN_kb1iooeNS95urWlWO3QqnO6jb_TvBCbLmIxKnrsx7ZgvYPo47zcQO1PljakdxtxGYsTr0AJK4ZJdsvXB_MzCq1UGUI8weggz2U81Y4RQ90SAaLgMJm5XxGuEc-T-qn7bP5Ln-n5ftmlbzN-WSt6Y4gp0F87NuXVIsB37E2HCPr-I1Ed-9rCd-R387Qbds058ktLvxjl4JQgy6q6V8KO6WQsfL0ak0z2yQoE2GHaNg48QwXbHlOWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcC3Bp3jCGUSPwwXLdM5-yM7lgeATVJbLkU9tj7ifQGAULcOp58uJT2eQ54nOgqUAoCD_4KfNqxjLRrjI_spcsYUJcvF-ffijhSSNsVk21EQzBPavWctCj-q1tLQf9qPrk689Q9Tz2LjLHPdQdGyVfTeal-NsIf-EO-wCQYvABRAeSw9KbccaBbKf__8bDM8aYFs7RRmIfFiGOEZYUgEKGtfbY3qdMSRXPIdzf8QkD6jdX-6EGjMurs4qvBa1rPz_TwvMpkrchDyEfdBG82HOVp1rbTEEJ6DFMuj8NtVqIygJeHmy324ZhsyTG6vkJ1xt1zosM_aUyFN83Ukt5csUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvjYL9_jISq0BekdLf9ruUXEAvgH-hnElirmyb0CxCLEL6ovQTBKITEDyT7up0SvIul-KfUoG2BmYks6mIDNM3MDMmHAFiSjjq-28DS3gB2bzrKv7qC38jKQyQmU_pIr6KHGShLx7rWWPRZhVoyfMyjY8IJdfThgLD4rRFEnSLJwWPNzDlR_kgDcwRyU_SdBgyXd4VChxIfZ6wHXnyUHJiW5UINUzlk1BkK8oqeCncSnvdW1kyOFkyF_DWO_55i6dPLmLM5UD359O2q4-24l2GRBFMDryIo1E1C9nMv4CFUM2sfCIcKx_DuWu8Rp_jS7HUzX44LSvKSt58RjYT_H9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcRT_k1HRsm8OApKWHzHtqDHR2qGJwmRwShpkqFvgWBwP1CpX6-ND1FW4NXA8rk8Buyi_okz2vAWjKthX6w55OAL0eIonKCi_4Oli4UqmD6QpoI0Iciv39kXbMsh4bdGG5A9tEl5GEPo7rk3pTi96RlRIneD4SznSVktWbZGx1XcfvW-L1k6-tX9lGJ1VXwrgQyvVuJQM8qkcQ2yBPysjK1Obw-LoTTVRqyMye2K0AaVsZ3hGNkom7bmlJRGaI_bAd6f2mp9_TfxSNnqX3bnx4t6MWTJGCvkqWIzfGRrqAZfoFBSgz3seHtW6Yufl__2vM0ojBmtl-FOuGNeu3P9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjF8E7BM3_2jvT7uvwY058uwaX-xrvUR7c4CuGDQBn3dLlDDoaoS-Y7ogIHbVH3i43yhrxWiloBfOcO4otIswHDoUGuW7tt-KGYOgXjjr0mW0fBF6l7ZSfR4r_tvZoWmG6-Fbp_Dz4La0CgWWx6uQnlKm5GJP2V5OYeQ2qbqfqFeVgPO4KFy2f4Q2UbZT_qaX76dwJhQ90PcJtHWgWZP2-WC5cXVnkyFub69SSCkIAL9AlsPMrpQjVCPr-7c70q7aBGjzQHJErbFWMwTH4r9GxxPAeLQ3XPLrLa7E1evZybIpOGdBvtyw4UF1YAd6twUAbVTILxIY0rGGjLTtvjX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7_3UTAbCFrWAbf3P6MDI9saFZC15p4-CO94AAijt7mDJu8q7cysLTq_-6JnU8JOlGfzX7-8agWulRlPlaZhfl4xEcNENnIJrP9wgZ20OpdiTvcJwZ66tjuEc38p0b1OOJWPWzMW3_4Tt812gA7rzfcyhISONDWwWQDdSVWI3HwKxqaIuHJ2EIAN5JZmdZTGhR0ZQQXDB-3M_Doo7nOZPw-3etX-3OIORfRFr84AsLFodzNeyyHswqqhG8iI4sLNO5FC76qZujdJMBfEefjyxQpMK8KRtYNYLwcHRHXdp79_p9ry3BXmAKyTswEwfgsiYvnCulL5Eu8_ovHap5B-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wkm3ewsM-ZtMXIqdOLHOkoEK8Hpk9C8uGYfzV3102JNToe9FE7Md_DNvL1MxKilII5c2jaClE3_ruZWoabmhsfqEazxb87LhzAdrXmxQgVh49cOdm9D4uHw5vvMB_KgWgoJEbxdqwxJu0ZGb2XvmaZfTfmSEIOiNtLvekPmYbK-iQkYfVOnr5OQoiTTKVbKcwjp0IkxnujCE9qnfQoJJpn2IhjCut92G25HTHO3OPln5nFmXAsjvYsboaE1EowLzf2Ov3Z29upZiI-6BH-PzSt7xPe0EpI9J1akPqRoWaBhjMBiSvfxn9FXNCWA-zipaYP4zTrA8mhJDkUS3OSbADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=DzdqDjW1XceE5rPw1FQf4mM_gnR9hPkVvTGoaqbXGjfsl7r6LW8Jf0EFMuXcJWSixEXpuaJ5Q5uXngQ_ZsY0_--T4YQ_ExcmYbIqs2usH7Yxe_Iu9dqnOB0jw282g2FjjaeR16PVOZopEvnLIjfDm0Dxn8M8BMkIBFuehVE36Dg_ObsjjVTyWPB20vHJ7PVg4S7nlmvAN6Mpi2eohVN1nAp3ajxqnwkGB9HvHyaaIZklvQbY-qFyWVNK1QBPte8jGFtxRK2Is69kVaN7n4sr1gF3F0aWnsOQIgbR1jCzy19ovzkaS6umTIJpF4msDChRe8LjOR8hFQin3a98RIuDdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=DzdqDjW1XceE5rPw1FQf4mM_gnR9hPkVvTGoaqbXGjfsl7r6LW8Jf0EFMuXcJWSixEXpuaJ5Q5uXngQ_ZsY0_--T4YQ_ExcmYbIqs2usH7Yxe_Iu9dqnOB0jw282g2FjjaeR16PVOZopEvnLIjfDm0Dxn8M8BMkIBFuehVE36Dg_ObsjjVTyWPB20vHJ7PVg4S7nlmvAN6Mpi2eohVN1nAp3ajxqnwkGB9HvHyaaIZklvQbY-qFyWVNK1QBPte8jGFtxRK2Is69kVaN7n4sr1gF3F0aWnsOQIgbR1jCzy19ovzkaS6umTIJpF4msDChRe8LjOR8hFQin3a98RIuDdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwl4XAzMO199jzVMptzFqqco0BIuNej7r5nYRWfth5C0ekwv34vHO3zhI9GB3Up_I-Ijli46DbLF_56MvuCExA0_0ssJS1vbMhsSy0H_yCSxIMUNwc6PegC6-EzBpsPMM66ureeoaCb1DkBG6MmQwpjoETa51V2jDdtXuiArvF_beyZZUeD7IEz5OPe59ulDydYBAS7r51ZV7aZnlKccwLtvpZyldlJe6waUHV0e8DXHiakddP0u_azEZt8yBBF3AJ-f2hVBZxRUraSAf7j09Udd9iAoWJ301GMhiD6SeD3cH5Nz3e4uU0mFBr_CDeWFa_72XJ0_upV0MxQF06NCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/upNgWx9zM41jnkAVne_CDwakfll6esiqOC_YYrKjIgKt6lY2563gQe2iOF79fgzb8hP2LJjyzLgIJbgOMV8XO1y0opG7msHnzv7Txik5QXTi9rLEziJAyoReIjtUSwxucXIqSAkDw4xeVvOmMuhUbhfZtLqlLwIxlEV0_6YNDgyrv2MrnFY9jCk3R3tTKGety4CFeND7bF3x0pLBhCv3viJ5I4qCdNVeed3GvyTaMiEp2ShPBRTXUhkNBefJVi3k6ro8Il9EHa1NYIsfzEeDcR-VfYGmwGL45AaYhO0tD3N2RUAX7jF2CrGEztY_NSM2CSczJCXDeiMAUmyvMBOk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhM-6LgTZmCR9eQiclSQyimUrng1c-Yc6HsoC4WAlWly0Nahv3_6hHrHFhwW1d0n766kDvOGob8sv32SHprThjHWWr9PEbs0fLv-soFbQYhDCK9VhHGsDpPjomT2DtC_rE97pZai3NWaiXU8xGw8vYFvJw2S1RbHGluB8dBKbwPS57e12OyOnZkMfRcw2tgCNkqKdyAMkVv1doIKEN6Bsv9mtogszoBoLLYkw9YIrBdo2PjyGDayKjI25Z8g8iAntTYRsUt0t7azusOJSdESHaqPz0aiBynyucuKfijqdpvtEspgrFR_VY_a5mbb7K5lqtGIxcgwXyz2yEIUzFtsJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPJaFkB8vRNCsC-4mqe2vOAYrRyxzJMK7YcjrpFnLS4yezjVJNS0J3yCHjedxxU09b5M5E7-bQZdoAwIlC4IpMFbxA70wMGwr-0cSPdycCET_SSA-ZQ2t71c20xLs1mNF9T0sCusRqynEgR1vjYVC2Ms75AVF9i39dOSm0tJ1aPuzAQSYLSYTJSqpbdNJZdtuZFyPd344onwplt-XC9kciSb6unuutiA1PNYC8Tun8fKEccClOeat4AYZ33dVEz-svp6cDUWJe6b4ydM-WoYIVpTF9yHtrFWSXyHjZ0tweWDN2DpQB1E3-8bBH-1LYI7i3ZQnxxKb2ChVpAcBUueOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNL62k-RZBAQPu8WHmIPbXk4fsCfPv_r9zJ9Ax1UiiW1PbgdpurTzdcjQc0vkj4ru_fUHN_ZeMB8T7wTYHtO0WsnQTyRR-w3br99KSDNegYk4o7zdkzvl1EY_p9p5A8LBnparDhzfcrHiD49hjiSfh3bFXd4rLGy1J-t4vyXBxUqInNKnDNkTzIc5vF0dUqj7tbq1tnRK4vrtOUFl_HOjFFLgbU8PqjmFO8fxXUYrTnL4ZTVd58KZpZQtLwezjUut59uoz8cXuHn07zFIo3WzA_hBczwxQpaD1reuxF9Y3TwLkSlR6nsCo4ur1xr7iqYzyLVvHmtbTrRPw1z5U55AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AADCHi-OZujX26Qk9TiDFJ1b7DHdUMPdCditlEq2vD1wk2s-ucsUuO8P8GaGT1CkZZUv18wT7dklGxndC6w3w5lE7giWIxPIb5qExVJnHzoiWCAPj1xPsg3Ozm2QvDrwvi8jQCBa85CQybfAH6cIGpGu9bSxjEettb6s77jeWvaV9xBLlXNlc25KB70ECCh8cGfZa47a4KRAQADqcUjK-n1ftokeQhsQjYqG1_3kD14rQnePJMkDJnY_LLJZEfqpOPyctem7PWgKnfUegRb0P2rkbGKfxzgbdN0E77RowHE1VCTqBdmnNtQM8GPP532WCZiKmsohWFT0ZVBRDuJW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIDHM22tQNKLlkUtUubZKudoFTC8XNvm0qoSmcZgaOpEEBq7NH4PLCb1KU2c5WvVDY55fQEtYz-2CWcB3e5RBQ7hsmEF8OAzUIh5jX6wuStKxrdmGk_RUIRTscU4cEhRh8RwC4Fzwo3EViDRjTj22sdooj_xcUo7VSIupzQE3S7wkMSohvWhwgJFQs2JxlRALgWGjCbRzGr0xkkIGXM3UwWWSadZLyaTvCg_hwoJin7mN1TPtLOqAqh4a4iSmmutWY2HaFVFzQxFHS-n8er9SHOn4iq-Oz7t0eCIkgUvTCaYbHUbx5l6MGbU_p3aS48PJvaeaQZhWNja08fRUvJNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrM0tW5rF4Iv-IrGeQFA0y_a64x4OT5R3rBF-ichY9LIkeL5hZov1UcJdIjt7YVgCMYN2A6iBa5Q-4aWZPo7ncS-GyhSl4YuXimPyIBbA-PM_NyDb7zzjQtcE10lTK2ClFoXjA3BZ18fKKp7tMnir893bZ3hAQOqADD7oFxLyrL2t-_9LzOse1a5fbj7Ap7up-mIaS-fxWUL1DFNB2AWWILC53FqteibXcmmQ6-YxKKBeaU7E2sORq0tSbgAw0uOeISL_NsSbZq8PojdnbiWzIhjYcMH4LGoDf6FP7FBT3pMojel2sciED1tXoLCZdKXljoTl0kG4DOkMo7uDPOhHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=CVX54YgqZWabJte0EOHqDg2p0P4oAdu-1n3IVYJ_fv6j6mpiDwgYy2ERG4QyzbdZiZ2jtLcb1WmWYL5fPfze9xZ-miL12Qn6JBG8U6tvTvC24KNrzrvumx6e_v1zWEqx9dmBZWoGZgX9-Fn8S6HA5ak_cIl7nWXSzLunWgIG8YsZT64tAY1Q0yM9L39ajmvYkAaZbHdWJQH9dxw4VX-fqziedAXqDMJni3HxyEisKnH0fDRnNcuiOa6QDFUqcuSCasSmGm7PbaN6UvMIQ7haxfNn-Pf7bGMscoSAw5cd1ohBUqlTF2nB5m3P3bmVwb1mdev0CDOKdJ6DBcb4i6CErk1Inn2ykZ27NbNzerVH6MX7T9l73I5q5t5MwIdJDafghqa47VRo7xak4cuppegbN8Rd4RSk7K8RuucUPQLts3Ue9x-CImxTYs1cNwjJANGdwjrmFeW8udeVzt_yFi882fTVE8GPQzc1L39JJ1NI3ukS2QAJ8uQNMIwprlhYPUYPJLHWi-ewXa3zdKPKp0N1_eqV2yI2fQn2StxlexzrYOtOgzcWImqifMiL8-JgjgWq-KsKO217HbH4ONTwyQXt1a_uEVlPOXTnTsiYWPiktHpjUOEdPfdL_eAGrT2NpyXVTKh588ZW51r2rj27s4RFgTeneFMavQsblDJIZh6i8-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=CVX54YgqZWabJte0EOHqDg2p0P4oAdu-1n3IVYJ_fv6j6mpiDwgYy2ERG4QyzbdZiZ2jtLcb1WmWYL5fPfze9xZ-miL12Qn6JBG8U6tvTvC24KNrzrvumx6e_v1zWEqx9dmBZWoGZgX9-Fn8S6HA5ak_cIl7nWXSzLunWgIG8YsZT64tAY1Q0yM9L39ajmvYkAaZbHdWJQH9dxw4VX-fqziedAXqDMJni3HxyEisKnH0fDRnNcuiOa6QDFUqcuSCasSmGm7PbaN6UvMIQ7haxfNn-Pf7bGMscoSAw5cd1ohBUqlTF2nB5m3P3bmVwb1mdev0CDOKdJ6DBcb4i6CErk1Inn2ykZ27NbNzerVH6MX7T9l73I5q5t5MwIdJDafghqa47VRo7xak4cuppegbN8Rd4RSk7K8RuucUPQLts3Ue9x-CImxTYs1cNwjJANGdwjrmFeW8udeVzt_yFi882fTVE8GPQzc1L39JJ1NI3ukS2QAJ8uQNMIwprlhYPUYPJLHWi-ewXa3zdKPKp0N1_eqV2yI2fQn2StxlexzrYOtOgzcWImqifMiL8-JgjgWq-KsKO217HbH4ONTwyQXt1a_uEVlPOXTnTsiYWPiktHpjUOEdPfdL_eAGrT2NpyXVTKh588ZW51r2rj27s4RFgTeneFMavQsblDJIZh6i8-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=qlbFBocArpo0FFlAq4TCjYXYHaNoyhZvQn9vyeaYOUK-LvdZp9CTBkx6lXzMhuX4tdPtnY009s3xkOFNBztONK8lkcPgG2E9DaZ474Qkz3N3SJ_EpiWvUztvOA-xA2gZmW4eN2bvrU1u-XaHsZHKNtzki3yv42DQogqTMXpoCU7T-hzIG62Jzm_LeEHT0r3avvk8ykBfjg23LVJDerVaWR3Sej07iHxr3UNul5a7KlFSFOB3gfosuro4cCjmDeSJuYdHYmyeVIB5g7RlqCm6cyUtkqyI-eJEKtJre5e7_l49UNcnf0wFZQc_WUIYCDU-GV3qVsM1sBeYZBFlAK2CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=qlbFBocArpo0FFlAq4TCjYXYHaNoyhZvQn9vyeaYOUK-LvdZp9CTBkx6lXzMhuX4tdPtnY009s3xkOFNBztONK8lkcPgG2E9DaZ474Qkz3N3SJ_EpiWvUztvOA-xA2gZmW4eN2bvrU1u-XaHsZHKNtzki3yv42DQogqTMXpoCU7T-hzIG62Jzm_LeEHT0r3avvk8ykBfjg23LVJDerVaWR3Sej07iHxr3UNul5a7KlFSFOB3gfosuro4cCjmDeSJuYdHYmyeVIB5g7RlqCm6cyUtkqyI-eJEKtJre5e7_l49UNcnf0wFZQc_WUIYCDU-GV3qVsM1sBeYZBFlAK2CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7a2CNxoTKTV_q3bh3AdzZNfeG0YWVce_uR4o1eOqqRsQaTrnlFykXwxdKo53gM16dGIzN9GVTt6HkiudTcl0l5vGl-0qnMh0yDMsn4vLdmJ8w59T9_ai9ZC9-wZcXuhntGGj2eWgCpC8MrV3g7P2Fqp2SQ1LIBWGS5FBRU_lloRxYDnQ60GHu8zxt9mEmtBGljYKAUa0vt10-WENedVKHku-ULYN0QUpHXdtXMEZsxZWLWpi1uDlPcpYg9y6PJicqWAJVcaaXUHG9L__3CAAv_9wx7lGlVmbcFvKJFQAkTku_m_fZBWOG9gZReanNUopiK61wJqwHg8Iz-1N-obsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbMWhY9EjesMU1mPGNU6sFMutmrHVawlVYLFDWTuOPb01RRMyFk4BDUzlLPSUWb162CgYbtHXK9sSve_KomcHnP5L3R_161XQ8mycb2xvFuHgEexiJAKfUzpppaEc9V_qLJaPvBPjXez43EkJW8RMzYy0t9I9T6D9hykWNdU7wi3pV--to5uUuo_HocZIcKK9rzvfmkK3Q8f2jQKbzRid6s6HyAfAi8HQCwAg8zpifOxAecQ5IUWybPWUX2fEIxDo-OxaBSpIro1ZsGYQo2SE9oAye6zV2CuuAHH3KnTFMTR77hS_EPcsZCJZiC5cI-VTUkBF-1sSZARp9MD2FCtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwowq4w7R-LRHAE_B5xJLVau7NCMmV1LA_RkFrxYWvpzKvkGujx3N_crWFrc7aFPXWfwpqTH-oTSaogUk0EjnNwu43KAiDwjfYnIxQ9OOU6fPrhhImnlnsiMc7Oc1zLWHCL8ohIp5eQ3ZLB0WR8T-cqtyzbwqbsMEeBXEtet5LkFNqOkDH8Rk1Lqs3-I4WRtOMayeox_CEUROZD0yHwBpBO4wz3SkWSNCsLGuUKJ7_RuzWME3OEy5wlmlbi57Xj0T-ldQbukB95Zm2Aw1UkjH_WZ4o_DThIaOxKHzrTc7lfz10XGM_yVMZ129aXe35qVjtf6e60nAZMmacKDnpKhtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZohO0Zq9Fd1R-pAti5q8PL-ZZeM5UskrYY9LUfc_nvCmFPTZotlELI9UZsQ1COA8aQjNNy0UGMRaWEm1VsTK22sFG0FgOAnDlIe1Uj4mgvuZ9JTYiWg3joMb_z_GeG0tOiKnoNWh2uTchrj0hKzGXIaLtuUpwe6SkrqbbInU9sBFM-G9-HlEqYPMvXJRZK4UrU9HOcI2hYdqGzWA1h7LLYLq_rO1y-L8yyYmQGQOGFSmWAknudryozY65ww7FEwJo5i783RwkI8_ra1y394m4IpgzTGFLSUTSr8rMUFm-xKPysJ9a3578unLPthM2w9MpJty-jGy9Q7zO392kXrvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXUFpBMtmaChZ-M-zbzyBq5v2EbT1dhwQ5XKJ7ZliKBYTOg2paRm82403d_j3Mc6OcHEt-QsAwED6j5EbbMe7Nx6xr5L4BtxMh_r8okK9-S4Eblqm1zm8JYiI8jIDWhE_HN1IUd-iVWERhkV4Z8BJ_oD39r8YRuEw3dUDXh9NVcQrcaIJZ1FPjqb4wdrhhqN0m7LX9ESd6HcMWq0eRnDIz5P2mrSQuN7ZnDrhLeyOEpzH63mVne6r9-1ZvgFanyw_cNBTM7v48sjLvB7V6zw326_JopdigBHfH3azOeMXlPGfoOEBYWX2WsmwExbBVnXkilVruGZZ2dmLSvl7h1Alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoGnJvigbCsKSBk_OfILQGMUvVenlky_VZlZwLzAh9Vlrc9sVK6aP5Rlkid7l5NEub_PN-WMIqhi_fsf_Aa9sqB3_6WwAQ526sJHoy1MDDolBftWhNcLwqQW31KqP-b_ny0b3nhmZrE0I9FBIMqt4wjHeNEctbYFDT6Z5giO3CMt56AfJk6fQr0uajRdcguuss7-kPINb0orEEknmlO_671pmJjic6QUCXX0tmXnOnnUHW87XodPjQeTx-J2Qf3VUV1NBlvy_BC3i86iGtpHHpDtWGkOSISXhjpSDjTlIIsJo0UiAkq3nTAEPnVSQ4UsfaDi4mzfjBbIc5diubROEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHUld4a6avbgORT8UfeOufPGXKUOscxqxgDEUcyJo5azw6shYl0AjyP-5LUfubQa8r_2SM3KLaOWWmbpi0GX9_OIVPA85aTpvlto3b5dZhXzZWCEacJTRa7pcs_l9EZ7gzt5TIn_vfp9yldzXJIx6V6lKRuEN2M-Awzf7QwRDiswsC7k-gU2HtGu83A7RiR8aY6OilZYkkpz_5NTxBw_LwOjpqIQBhCkDD6QnP1VmOfSSkYObuISzYWUBPXv-P2fy0SMEWRQQBOCFAP9iuVB7azHanXdNt4ddGzc7ODkC0yZblWuS1uKFSaJjXZFGxIoZFD5cSybmPQqFdADxl4Olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klHzlEBc0IqRA9CnTqD4GNLnRUdP1YRWVZ3wup9rgykrxuRx6lv_SXzf_ZhddsIU6ra1ZxveqdPahljDrXVoj5RozFHmdxx8Lxx-3qPYodyk_Nbn4FPqwRADrhGEwOu2aC5UglINjgXzHuYBJFWHzODCyVLRS77fwhK-1c3U-JplqhAKIE5zYI3QhSdM0vJux9FE0PxWJUa3iqUm6x5Oejt27tkedL8xkoxlEJr6mXFMAtB9dn3KwakuO931hk4GkYJSEgxpH9xJLJwHiKABb0BQ2MnIcuCiXmKQE3kqyV-QaTtVnsb15R9B7_dc-xoF8fkU07LQsVuzO8lOQIhZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8mOQyAkLHo_B4dZC62Di0uMcHKnJ5nrRzg2g9D2vK-gJ7asgglpgjRQFO0zS6OdKcrY8I6U-s-QI2qh3TEtUwXOahGwvoD98bzC1bi7B7o9tUv9e5cdmp22Io9SnWVHoMOKmo6s09p7lKGWdl6hON0T-lsY9Syeq2xGTN-b9rNtIAQfG35owQrzXvRW3KhzB7YCrta64iQxS9Mps99mVLTvnfjxeP59Qg1TAgvlDmOsZ6NfeCXYZqxQb0uTRBvb6QiHmyQh-mvucoyYT9oWcd0J5L0LHdAH0MBKCf0cHXz1FdEPSCNSoaSRdDNPmrstumNP0lCgcX3UIuZKcRdhjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=jIPg9RFn8hd0g2hpcI4Qr17-778Cr9Toobo1o7CX0ly-aw1DiuOh2j0KDtM5uKIesT34QtB6PtPSnitlDIX9wkgcPqclk1FR4zHB6ZvbipKuHXHX3lBcCc2yQTJqViH_r3nMlWUhZWhzaVf7GYmEByeVkHP69XJOFsyyvsxvC9Y3L4_rhL4ac6wSl78JUiIHfb6q9as-spD66pU61IHAcerM-wQywuEHB6DyjEQDhDFnFtK8h2cCpVGGhKTfrJWwIqJ-bx6yF3vVfZ5achNOmzuW47KewU0rhEMIHBbi6Tc1NfZQp80tpiBno1xrnyYaaf0ZxbTtgaR1YfMrMlbjtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=jIPg9RFn8hd0g2hpcI4Qr17-778Cr9Toobo1o7CX0ly-aw1DiuOh2j0KDtM5uKIesT34QtB6PtPSnitlDIX9wkgcPqclk1FR4zHB6ZvbipKuHXHX3lBcCc2yQTJqViH_r3nMlWUhZWhzaVf7GYmEByeVkHP69XJOFsyyvsxvC9Y3L4_rhL4ac6wSl78JUiIHfb6q9as-spD66pU61IHAcerM-wQywuEHB6DyjEQDhDFnFtK8h2cCpVGGhKTfrJWwIqJ-bx6yF3vVfZ5achNOmzuW47KewU0rhEMIHBbi6Tc1NfZQp80tpiBno1xrnyYaaf0ZxbTtgaR1YfMrMlbjtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkRoQziIL_rrWJiElSDFN6ZzTF-4fuWEv140oH52w-UfmYf4GxYJhNUB5pQQj0cIW6bPVHMhwJW_oyoW1quADeQ-jOjffSKuZ1tEp7zC4BuwOa9FYopE0uyAtDGvAzszGUWqVm89wFQpdJLufxi3qaqwKp_qlGUtVsZnJqXvtJwAJeDVE86lLhvj9ypT0ZAml0AvWGotY7mu_GB3gaXmX63htAIpMfg2K4RNhmoKj9B8cN7Aevg2GM2ZAIgHWz_5zUPYE3TGSGpjO1jryBS1Rz8-INdLAFSL_p82vUArE16C2b3_vWuixkzZPbQouewmxyHlrJ47fHUa-jyn5d427w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=vSLMfqqJ_H5xssrI-fXw6bzXfPbzEjDPus8ZtZk_FyTWwKjIu0Or7OvIkAvXcuACvkj8gM4kEenHsySXmMJuMiQpnX65oPWU12jmAAKVLuOouMSBn8shFV41Qb_tR5093ukPnF_8ZwwqY0bU-H0HK19xt6jxe-Aq_FRGs0k0uoHJLAm8AaMgEYwzDKGUSk9cNbQCv8zyOHD0Fvi6OmG2Q2GAXYbvIDQWBZ8wS0xczodNCMaF0Qq4W5uxb1BduolmcUHwkGKEU9u6JDF6G7zry2LHq5iWINpJCZRJQeRvDnEVNpIRvwu-jzcxQDCtZWRMM8BtjSP9IesrAcVlrQLRDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=vSLMfqqJ_H5xssrI-fXw6bzXfPbzEjDPus8ZtZk_FyTWwKjIu0Or7OvIkAvXcuACvkj8gM4kEenHsySXmMJuMiQpnX65oPWU12jmAAKVLuOouMSBn8shFV41Qb_tR5093ukPnF_8ZwwqY0bU-H0HK19xt6jxe-Aq_FRGs0k0uoHJLAm8AaMgEYwzDKGUSk9cNbQCv8zyOHD0Fvi6OmG2Q2GAXYbvIDQWBZ8wS0xczodNCMaF0Qq4W5uxb1BduolmcUHwkGKEU9u6JDF6G7zry2LHq5iWINpJCZRJQeRvDnEVNpIRvwu-jzcxQDCtZWRMM8BtjSP9IesrAcVlrQLRDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=e0fxeEsZdZ2TMueAvbLbMliHuwfGvhNhuKL6EozQ9aNaskh3V68zfqdmCvt3iKKGMzrgqV__OOjgUzqCWp7oGupMjvDMLzWcqLcv1_euKJ9m0KXwlF4QRSl4E69A-Sk0mmAnMg_6FiGvlvdsISsuOKHWV20mW2pEiylLEXBUtFtFcyBROIxE8Zts9Lypk1WyqRqNr3fSEn9Wjsx-5xQtw4yO0wnjerZTPnekgKknKpRxawSrNZbqCrKCTZ_AMTKlXu6iBcMfFo3EZu-LJiW9B4dym12ZbDn9Q1QsoplYl0og4TNEhVBIKHWQpdOkdFE1DfWvMZuBLmSPb9L0geSqWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=e0fxeEsZdZ2TMueAvbLbMliHuwfGvhNhuKL6EozQ9aNaskh3V68zfqdmCvt3iKKGMzrgqV__OOjgUzqCWp7oGupMjvDMLzWcqLcv1_euKJ9m0KXwlF4QRSl4E69A-Sk0mmAnMg_6FiGvlvdsISsuOKHWV20mW2pEiylLEXBUtFtFcyBROIxE8Zts9Lypk1WyqRqNr3fSEn9Wjsx-5xQtw4yO0wnjerZTPnekgKknKpRxawSrNZbqCrKCTZ_AMTKlXu6iBcMfFo3EZu-LJiW9B4dym12ZbDn9Q1QsoplYl0og4TNEhVBIKHWQpdOkdFE1DfWvMZuBLmSPb9L0geSqWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWL62wbZP0hYp2wDDZdCzt35Jd4UajPCDVP8a3jtFTlYkQ20xE6nH76Lwkpjp6G1R2hOffBWR8KCD454mjPWvJ3lBZG3WcR0Qf6fvyl06pzZnly9CHr_y4cN2eFko6Ncp-FymX_YAdu8tTIb_YhGWRKAAv-9iEMmAjfROPii68m1dLeID0bk5h0dYoxkH_bcTA8m3zVW9Ego-5v8j5SbL51uPk3DnbNuZq66GuJ0miofy6_sZSE5-6C-fxsLWD1ug74d6O445xRdAf9IaWZv-qlH4aaXHPBer9ETmTUTH0vUIf1S8VIBNzJW4BxNM42xFJvjzQZuVSoWIdFfxb7MhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=iGHjMJjkhg_NoSFQIJeS06BM9PV_YkU_ruYrBXK9RRCnqZFRtHP7PTsatnyTRCCqr2j6xfzgpjyXhp9W1PnkRDDR_B2JZ067dpl8aETJFrD7YiRl-cXzfIVvt-laQrD68XgZUS_EOMjs5HTHxaWqwEcg18zrj9xUAKXl7VaNAqM5JD6mz-P12SuN5FucioP8Jj_XgYNmYRhN59EeOpN13JVROw83cvBO02K7OPNqZwMKLpqgIszVVxCDyMq28zsgIWgBAfTWrTDA6e0v6R2A0gINJb5Rd5HSeiz1gVvZKDyNPUgrg2EN4ecAxfdrhT629YYGbQSQkEF12P-W2Tyj-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=iGHjMJjkhg_NoSFQIJeS06BM9PV_YkU_ruYrBXK9RRCnqZFRtHP7PTsatnyTRCCqr2j6xfzgpjyXhp9W1PnkRDDR_B2JZ067dpl8aETJFrD7YiRl-cXzfIVvt-laQrD68XgZUS_EOMjs5HTHxaWqwEcg18zrj9xUAKXl7VaNAqM5JD6mz-P12SuN5FucioP8Jj_XgYNmYRhN59EeOpN13JVROw83cvBO02K7OPNqZwMKLpqgIszVVxCDyMq28zsgIWgBAfTWrTDA6e0v6R2A0gINJb5Rd5HSeiz1gVvZKDyNPUgrg2EN4ecAxfdrhT629YYGbQSQkEF12P-W2Tyj-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWfvq1mLdBQejqxJvnZ66uBHOk-k207kOK3c6qgP8T6UJHoAkyeaOee8hUMu9UptuL1ShAmNNhvibLvvxxHiT-b2sL3SXy19QdQObRimHtMT27aivz2UTrV1pyEl9tZ9vob-6uCu4RSjsirtjTKD0JMUfj_6hbgmG8GVvgdJAvkyeuUS3eX7jilue5UBzD2iSl6ZbhWCj9IOb3V0hDpVRizgmBLF-xAJHF_wByUbZShtK8ZzPtWYpkc2V2Ch7HrabKge5w2iaertZ_jTL_X6WtTpaaNkk85XatGjeggzU3IowGgiRfSnN5Gje2g-wAsoaNuK99yVVRBpVd6-hOOY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izkwlEo-fQRX1ZY7PIGsx5uE3NiZruTUsgcwd5T9301zDprSfm3Bf-YN_Svh1opFgmyN1mE7NIzyvTUEj5s9CyyZQxPG1zPhuFMoH0eWaoNryRS1XgC9M4VSB2nR6KB5czq5likEfMyiUxHIeD9kxaY_beoRWBk3BdjQftEcPh3IiAzFVTMUELbXj1REEKxOThD5_D3VA02QNgIWmCI2wvaQp_wQgBnSrDi9oyUGEcW6mJJ3F6CpZoSQ0Y1-GfUedS2xYBMIQU8a3oj-Yro2XAZBPvXSOC3UnVhY0w_jxNKtTX1d_IeoGmPgTjM9FznbmFhROpWGWfngWyxz2jlSpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U02G3QZpi7nh-zVjukF1_4JcBQiYg3DJSl3uIE5Qyq1dv2je0xFDy8rwHCWOwAc4mn7H9h9OaQDAgQCl1EDAg-laf97SXKuBsgBOe5IytdhuFrpm4NVnlpeYyEJUVCe_xPSvyWBYge5EVg9F0Wc7JhRV3Zrf713GqkeC5yVwTAVfmgsjXjdVOSvB_5-vCX-oBR40RkzierjOYHn6EN8BO9JGHovLMB2vEjzR1z6dVwiNH1cdLy5TQ-WpDO4cXN_miHqSZYJjxIaIpk2a9yM-56K0BGBFjSja6wHKKT5Vm5A3jT_lfGPMhK8xlE9audPueipA_phR8DeQlioWJw4b7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ir3ohFpN2dZfD46T4oy02aMmd1XjScBZG6BsTVXbOjNXR91Alyw0hwrrubv8DwcmxYTv2lF4oDSnXjy3E-G2fuaI2BfeQLzz5fGq48-t8xHQ-1Cvm5O9PjY2gJ1EnINxklk16ZweYfAh4b5HleK_8wliXmA94VUQL3Q4zhPWnYO3KKmiE_saE7-Fo8_ovfhC_54LgaRrhViF5KxCHIwchyZLYZNTr1K3AyQrYBhqznIKclsj0Swx0VbRTiFTja5aoL_l7IVVvAVVsIKsaNK6TDWBlZ_Rb2Mn7IkPGpAhgn5Q-UIriSsv5o9oqFfSnG2gf_mgLef17uzt8VBtPs5YNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KllUB1WzoGtC7hOFBtq245uMVF7dqoSB0Q1v126IeLnmG_yuJjsForwpKS8s1PANtJYlplzndoAdItw2fe6Q0VRw5KCdhay-D1MwQb83estYolz5RBYCFtcnyXMCr6D4-tt2zPmUppTQYx_6NMM2DEgckdkpIlw_CUHJ30fo1P7TyTkyoagXHUx2lBQ5rbfChMh-4VhyO_AyjfrnuXYyXXTqbYLax2YXEduOQtLa5xIKtNSUBaH4IDRKOum0cFcr9O3PTzd5_UExUyYQtVJ5OMe7elO73kYJdMaKh6mVh0Kd8R9Jl3IlLe0wsbRBvAIW4aR9O7JrQPCDFyD7r728Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwem0SSlu_01L2UGUTx8P9i8YYFVb0IYL1KhLKyFFj_Svtu_2tbY2bFLC5sxignoZXo8s4Imk9RO4eQ9Yrig8-SNAgku3JKcxXYrSSh4-cZTfHQy6yAXWaM01gsYLnGuuaCrQo9cG-E6tg5gQMBusjlmoJAfUX5A2p0QalvoUFirYMp_-5teTdR-bgonbTSsemhwO4n-arGkXOx3SMgb6iJ3ILcuAykFBPGqoR5YHK0QC2WZobXFkIX0ewWuEYKx93DOVkD0VybEyvgrcTJMKEES3f07XHTXjnUp-zgxn7c1LCtWdUO49GDJtr-TZ7JSsIl-nyYj4mvxgOYsH2S1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rJf3-Ozs98Ptu4uts0hlnA39OfJpNZ_j9XO8BRsGieonD0iqNPdX2q2vGYLfCkUT2B98f-OXRhy-0okCM0y3W6CnF-HKGKfqoW51b9bLEarciSeFGMkoxE3NEu2sVpn1HBFcw8aucPzSIDPR2BQDz39pV6KWa0tRgaTy0WWw-0Wu4RfvZSzHoj6Rt7Fep5F9NfTTzRo9i2vnjPPFAvIJWCWcKjSHh2krQqyj5SjR3YFj_1X5A2TDhsXeaUAIfno6xhvKEzVpfVUDJeOInLzmpjRfy-yhBqTYofZ6Y9pUOeOKM9OeqLjbMlFIvaDNcI992zgXGOohuss42jeBpY2kRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9mQoPgHZ5_yJge9Anaj4NPzk-6T1ZZP1C3UapZ0mfnZ0IAfe1BqikSe8TmuvCPW3NYn7BZ9CdD35bVWU1aTDvP46SwI3Uz6E-xJxnDPdTIJ4c3PovIpf_RhBaNa_o5Ef_pif9MB1WzkpuCTBWwhV6cYoruJp2cxYCMjFK6p_oR20NOSfsiyrGwMr0H7HGBjYsGtYsrh6-lahxeV6t9wVMLjmhMMNOwzICfioC1gjhUh6Emwb4oD8GEZ0PVh7TFaBXY7sUaTfdX7L96Ylq2aznIBVeL2cyX_aZLIyMAVu2XUGOwIeBRW2ddImLGlUDEkwCk8Bga_mB-bGTohfXEWAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=qDClGXzVt86AvKKbJKPEPkucrPciw07QrPgLqRcD2c2Fbx1gkpeg0I7CyvOKwKJCpRWWbFDUZkMdjQS8VaIPf-uaa0V5_Q5zInH2jM3palR1tVZ-m3RaktsXk4UBJu-P66nhRDpvmaoT2VJz9J9qtMt9Hp1WbozMtUT03kOLsWassdb6pxw65sjmwQV5mZa72Sog7e2i44H5HAX2o7hNWpQAbUSuixrMYXdrGNf6irXNSM4xx5tsaBaiYdyazg37xmii8iJFOZ34a6dlBu9geqPkSqIgXAUpc25tgszk02jJvQHUcAl2bEzQ-A0g6a0H0zydsSKLW8gUZivk043m9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=qDClGXzVt86AvKKbJKPEPkucrPciw07QrPgLqRcD2c2Fbx1gkpeg0I7CyvOKwKJCpRWWbFDUZkMdjQS8VaIPf-uaa0V5_Q5zInH2jM3palR1tVZ-m3RaktsXk4UBJu-P66nhRDpvmaoT2VJz9J9qtMt9Hp1WbozMtUT03kOLsWassdb6pxw65sjmwQV5mZa72Sog7e2i44H5HAX2o7hNWpQAbUSuixrMYXdrGNf6irXNSM4xx5tsaBaiYdyazg37xmii8iJFOZ34a6dlBu9geqPkSqIgXAUpc25tgszk02jJvQHUcAl2bEzQ-A0g6a0H0zydsSKLW8gUZivk043m9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=Vl9e9BaLYyJXBnGzDWrw-BIt22pfOIVubiaG62cZVNiFWXcxgRDuU85j_TDn9qDMo2kaj5cobmMmS9zFzFNa1s9mokJEQRr9kzBv809ONl8JExhJDebFYTfCH0cBMnFyjb9qmdQIfTF5txpxhRx--V6R6Necoye1wUZh-zh799tBIQHtoW-Li6skSXaXlKR-PQv-eRoiXdQvxEBIJM8hCD1N89fmGwjL1UtTyirGYLbEsLwb0PAn1UunKuBmMWliNdEQEzHdZPpO0uEQqsGf_0DVxT1YBVgDwNjiXqM2pBhRmhCXUuuXMwjSP4dgFjdY1uC1-iTa_9UkTQ9JniVrYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=Vl9e9BaLYyJXBnGzDWrw-BIt22pfOIVubiaG62cZVNiFWXcxgRDuU85j_TDn9qDMo2kaj5cobmMmS9zFzFNa1s9mokJEQRr9kzBv809ONl8JExhJDebFYTfCH0cBMnFyjb9qmdQIfTF5txpxhRx--V6R6Necoye1wUZh-zh799tBIQHtoW-Li6skSXaXlKR-PQv-eRoiXdQvxEBIJM8hCD1N89fmGwjL1UtTyirGYLbEsLwb0PAn1UunKuBmMWliNdEQEzHdZPpO0uEQqsGf_0DVxT1YBVgDwNjiXqM2pBhRmhCXUuuXMwjSP4dgFjdY1uC1-iTa_9UkTQ9JniVrYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=OUyGn7FN8EGZ9GGt-X-Jm_fo1fO2bhSSjVLrKpVy4XbYeOPLbHtt7Goi_8IjRJVTp7q4HvEWJFm2D3StJVLV6uAeiHRZGJCbdnheeO9I0TV2DQ2IXqxoq2D0gauFkEQS-zKepInTfEBw7dJTomKvQiZWaPfC_ndTkVLZES1aVR-6AaAQE12NSzQxe1821oKVF0Jsi5Wr1F_Z4X8k7f80VLwSc3vYCZZxeCxViDWFbt70Mqcc1JDVdI3ciueng3eidewaO2g9ynezrl182jwJmAQn1f2SomD-zZN7RwFmNyZMoCozuNCzIkvhRMR0En0BvgJfyH4aiS847EiJ7oBw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=OUyGn7FN8EGZ9GGt-X-Jm_fo1fO2bhSSjVLrKpVy4XbYeOPLbHtt7Goi_8IjRJVTp7q4HvEWJFm2D3StJVLV6uAeiHRZGJCbdnheeO9I0TV2DQ2IXqxoq2D0gauFkEQS-zKepInTfEBw7dJTomKvQiZWaPfC_ndTkVLZES1aVR-6AaAQE12NSzQxe1821oKVF0Jsi5Wr1F_Z4X8k7f80VLwSc3vYCZZxeCxViDWFbt70Mqcc1JDVdI3ciueng3eidewaO2g9ynezrl182jwJmAQn1f2SomD-zZN7RwFmNyZMoCozuNCzIkvhRMR0En0BvgJfyH4aiS847EiJ7oBw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBrGgZkfNfx1EDJq2fqQr-L4pV8K-4e-73aIrYDXYtnMjXyO4H9Nlx5BTiJw6QC2EWuhPLEzutq0cv0iimssq43juhFic9CKupOpMnyXmvhhSmQHfl8ILANu0BLKHLlvWh8W3gdcQZuj7Gnt7CTH7ObSWKnFAZ6XgoMaRuVQV6We4oeZkE2xVI48z035Kuew6llljhf7vrFQ3mgGtjdoQROrHOaVEbHQBq0JSXQph4wdp4_EDcrr8lCDyuOYCDdf80dQ7SbzEuuiX2BMyHfA-a49L8LqT-jha4ovhrtW7GVG8_PdeYRwF5cDlDwCesasuO2uA8VNuQ7QQi79KusQwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1CNJs8d9qTn_cMXO10rP3pR0MRXrahC1oTR4gYSRkWqxiTiqUe3nSHtAClzEcQtE-uNmJSKvJOyVXU2UtbcESksLtfmnvDYUWFIEJvW-SHwLF9HQDtY59ExAnU1j7D2dbNkNxPlTrSLlCuTXmirtxW1cTpjWxyZXJuvaoRoc1O8jl1Iv6z6p3EPy_wYBQ68QnBiM0-RX_lvjRU6hQpln5IKsYh6Jl0pVZxcewkngwNE2qYLbYtgKA89DrhZCP9QBuGDvtYvwMOGQCD5jX5ZYrY_MIGbcLrWIWuZDt9PY34S1M525D9icZG2Jj3SWY0cTr-ws2QwteRHSdxZdCTMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NI0FQg_XAiDcIltFczroqeUZHrbps5Wq22cMXWRyzsw7YIg44I4U-7hIeC3BlOWckSu73SxjkIx_8mLIbyKc-xOuMkLqZX2gbq9uP7iWA58Er7Ul0Z8dWlES4EMYpIll4AbictQHOp5vKKkdcPrRtR-qgISFdB-D9vQm_UauaBKu3eWfDaZgfLbba8hqe8L0ivuH2WodcwHf5Xc2JXAOD1PylUuRNA6Og2ddNUg5AKYyDYioV7GRTzON5Jb-PRJo1mGCT8BwVenN-Blb2Toe0hAVAbOLvlPAP-b5MvGqWKPvnMbJo7-NvTgnXL8UJs-PLtitGgJiG9jx2rUsTgJ5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQi5Zqjn-PYdFQZ7Qp86VD703wzBPL09w_aMsuW3PNJqyUqUamoPcZ1XuF4IKYuYijngZLqAsdPO_2x1n3D9b8norn16cLjetZcK1Lk65IzCr7Wf4yDGpvaWC3hxjNWe4WMP0cNV0lcIgqFiW__bgMDvqulZZC0eMn-dE9dbMtN_Iwo4qmzh-UaL8VnTOgl2__2gg5O2pBzfahi6_EGGlWspva_v1nSPJXQJdsd9akUSOANdhXm39MDjrompnHItV3kLJ9Q7SXsFcqD4467r0TRrPyac-hb2_H6BuxqAKnfww5IrSyZEw5FgJ8Pq4gxOApPtcd9gS8zOD70eIX3Fbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=pMNNUyGVfje6tI-Y0BEynwWzVKKQuDUWI9HJLFpoVe1GkUOnVRAianKVI6ujijrJ3vPc2FKr3rGe9cneZG67GNRZEEHI0x04fatrAmgfaXlfQMI5WKtOKgmu6_cQHV1RthK0ZA-V3xWVgA7HYOITD1zxkydK39WFpeGesuJDM3VHeOlmQ7j9Vxv8Kv5sRtmFIHNbwyTEMm0NywkFTm97htySlkEFMEcncWqHvu-RazNjjI3FwwAXAEOkBVof5nPDsctn8slS4S-hLqrcEYLBWNckzjs-Dn9dPPK2N0yCksudVFzaDwIEfTSQtLE2998ZzlnB5evTG0_v2YRCGBvm_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=pMNNUyGVfje6tI-Y0BEynwWzVKKQuDUWI9HJLFpoVe1GkUOnVRAianKVI6ujijrJ3vPc2FKr3rGe9cneZG67GNRZEEHI0x04fatrAmgfaXlfQMI5WKtOKgmu6_cQHV1RthK0ZA-V3xWVgA7HYOITD1zxkydK39WFpeGesuJDM3VHeOlmQ7j9Vxv8Kv5sRtmFIHNbwyTEMm0NywkFTm97htySlkEFMEcncWqHvu-RazNjjI3FwwAXAEOkBVof5nPDsctn8slS4S-hLqrcEYLBWNckzjs-Dn9dPPK2N0yCksudVFzaDwIEfTSQtLE2998ZzlnB5evTG0_v2YRCGBvm_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=gEiVspRkKTrrfCXPS-ym07edYMy3s6orT4c6HKObKgYkLzxv25iOpH3RcVxI3UhA2IFU3AVYV58vgzlcAPxruwH7GOGj1-Ej4o_mEo2bmGwIqclMkj7Zfge2yFbcj3grRcWglwbJmTvD99ZO9LMA_lL4NjhumbfQW7YirUi1xfJiGCtwQaBh4ZaSmmXK8x3osXpWHJDAlvn4ywHKFHrudJaBHQm6ZZrhgnHxQ4AGsmueskQGYSIiYPIoXr2cBNhYW7JsrpI9fFnE38hd_epn4bDXrtfSSTmsqkRlXwFIgJGhedDj0FTomZVyUeZW96c2AOUrmrNBE6c2ffVHc1mHiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=gEiVspRkKTrrfCXPS-ym07edYMy3s6orT4c6HKObKgYkLzxv25iOpH3RcVxI3UhA2IFU3AVYV58vgzlcAPxruwH7GOGj1-Ej4o_mEo2bmGwIqclMkj7Zfge2yFbcj3grRcWglwbJmTvD99ZO9LMA_lL4NjhumbfQW7YirUi1xfJiGCtwQaBh4ZaSmmXK8x3osXpWHJDAlvn4ywHKFHrudJaBHQm6ZZrhgnHxQ4AGsmueskQGYSIiYPIoXr2cBNhYW7JsrpI9fFnE38hd_epn4bDXrtfSSTmsqkRlXwFIgJGhedDj0FTomZVyUeZW96c2AOUrmrNBE6c2ffVHc1mHiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGejlsyUhvM-3ALWu6EmSovL8PGwOkLPiF7OMZdluP0zCpTd9fyWF6a0i2mxJ7i0cIt1GjtdjmoHUdTwfapD-jSsebxQnagc9mHhvzmyAlB8QmAzHArB7AFTBH0e0YeldgcRAJpftTwms__6AiXllkrlhYtocb1BjasTfoWJWoi0e5ZL82EPMN0IT6bw9lDg2iS-smWf_p47-j8vXXsEkW3uVGTPc89sTaPdHA84Xjeu_w372wx_fgeb3RZFF7EaC1fIbP6ekYZCjcEXXv0bU2M5AcnjrvrIg4cdaSszWQztfu_T0lHw8niNO_IVGfDjvgDp5vAtmyTtiVG4XYyzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjZjuM8XDYALOvUzT4o_ZnuG38F7NHx8g205Pwy_t_v05TNykvsF1RiNvDAcQlvFrsAsm2VOZHdjeCnOzER2LXkoTmISO4f51m686AWn3vqahymxWdWmxE82nZB5gw6kWOtZSjoPLUpObQ2bfBe5VAwMncp7GA_l1KfMPXAmYcSYQzAjVt67984yvk_Zqr-5ueYfR4IrvXjCsR4UzHSRQQc-4i05y650H8scyoHu1JV3WoOfsDtPsfqPGXkXZ_sGt2l4mtKzUEYrQKwOMIV1G4M_rUnx95ho14KoDcSOrTddtSpU7YwQ1CqUsLVcfLPov3OcB48SnRs4rZrQbPgtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpMvaOf6mkAaOibile6nZKCoM1LHkpcmgQT5rsvFOPZ3XJ_iMQOhfpjpEFb4MVkvagUyqbthj-A1h9oQAA4y87qNFs_VM8GQdqa2wK-YBxMtIcPPt6CzabN7fCSb86tjeYpVnWHfWgPK7maESlreHzJpYZMNgOUcPryM9klumAgfXOhMDNKskjDIiL9oSaG7ipdWgbmYK3lUOn16DsKKv7BnoJDFmsfY9gUj4N-vmuz_GsapExmZypxQFDQwbfsgxVdxHBBMnjt-66lykphEwTFZT2zqstLdTTrNj-CzjcwNnAl-fsl_05bJnW0gGm2OE_X0yldEFUVVHBBma8xk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyeBzogkPMoZin2gTml0cEs4hQ_Nllj7azgEWKnTkdZ3EPIC2PQgCYVAg9y4SvbSeXGlAT7L0v9rxLSVEooQSPs_SMVNR5zCZ-KVWBCGwdUffn5Y-9I5KNetYiSBUWldUStUNzbsluBhYcBlhhUXI1XHbQZo4K0inpo56PM07-g2Bva-xZ3bEskzKQuTmdotN6Au5cjihod9bTWdPaDPNJktRKN5GBYxLKNCEUOgm-9727CFTU73OPESi0WoJVDSBw-jWyhPaPBTG2l0eH4LxKwP05bk9mf7ys_MMSj4Iu-zpNHW63pFHTINtg0ltOQXhyravctxhNP_eexLyIaR9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fB5VXDoVXPgHfR7-1KK5IEkI35Zq7BwNL5XMbklbDM3SpwkxfGMiDw6cOZpnrzzB2if9p487TvjRaosuTgNwuR5y3YOgtG516zlQCrxv5rb83tgWOu3KIfE6EozQCvo6JlaY1Eu6DOaaAlouIG6ZsdbKj9z1cy7rKfY_dOduRzhYfNYeUfRhaJT3gXUyzx1Vgp_kW9nQAcUq5q4jF0gGF5ktNHWlO0Ow0ejnSxlXCbcqy6nhozqxgjDTz42bZVYKtr0g8TfwduFPRKDESd3VsRy7sa_G5slEEnI4sDKCccSZklhIPh0-rlEuPOpPoJS0vJeVn9VLHsi6LTuf8mjbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YE_zTkzihlarz1i5q1lQWDfLcMX8TtmcQ3rllg2MCX3dzWFfLLSqgHg578ss8-9lo6_aTRT78hS2X3JO7ahgBOAEKh1XMUyT7YoFIcN_sFxVIW0JBsvaJNOuhI0BtbQgYtHuwtA_yfuELPzcexfTgtwuxnUy766JuY-1sj1LDUnv7LHeSsXcjjzY5iQIluNGxm4Io21pKNSObiYhKrSeT2EZ7HcM-H0x9oSXvmxm869dh4IjQIDQGzBN3lKTwhpsWPAPRP9h7kTvID8Zl7xjlmFC3yjbi4vOhn82lSwSr0C6C6BeP4Tge3GwMLOleySyOr5C3vuaw--xFuGecKXOVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KspxqjnGrCHMj4IOLSiMh_Lcrp6bfkDTfzgBvemlX4jQWYtg2Lupj_3ot3SNqRih0MBlrPP7rWxuBX4Ahk4faaO8w46D1C3EvnXfj5yulgmkj4tCTCicJ8PaCfpdajNZNWPKghRc-dndSVy9iN4oxzUfg_q170lY1RINNKFtPwMSICxmH1-BJAO7A28qq5-N7d-9TGMGa1xykrZ3faAbJcR7cRmxAvoy_iQgPoW3gzh9ydoB-lbGnfqOdcL_AdjfjtIhksF_3X0MLhgrOz3h25AeMainqY4xEJYQfWzf_ZnHFKRLMY7EqAh6w7BFMZaNr2fq4blaUb5fCUJqy21eFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAEqSoG1dePu3x-mObFcV-hfXV44ekhA0Kug-GopHRhkmCY-1EIouGS8xniYtgSqI9iZ0LHfALJQ3qSyY0xsxx7G991VbIX-Fnu40g0T12UPnF7KXe4sA7FVUzCbeLZKFHxZ01zHNSUk-sz1aG7ktDQyw4_E9vhhhCty4E1eJoBpM5Q2HWVK58kt-Z5ejTHA-86YIXjJSqH5Vl9-uibYMAqcKEnYeZBuPNXOW0HkMYHrHL3pVAjUZmMIIuj8d5-NGsSNwkdp1oSXyMbIKUYNZ4UnJhzytHhJ40L_hexi06avg9cdALMrnVY7HVeyiYIeWueaoYSMz6l516eWJe_bBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=OJYgQ4aBMLrG09DDRCVGCsQTZOLU2nRZ1r8eg9KicSz67gIABzCZ3rKX8bbeJ0N-ISU-6mjeoX0bc3V6hfA4HLWcWcenw7FlrIQ8QZ4u8JcPTigqDrErVL_soe5a6baV9SY7ppbKJzmsuFdVLjXrePw0tL256c4cbvGOPxXFiVmmohA-npE3AziyXeRor9pk8i5pPPmVYQw-wolm--iRvtv0j2YkN3mimZ2Rif4i-VTYDfw6M_55VOWOgcn_pd-2EjwTcUmLfPwylVxWLm6ToAYniGU3NC3-Iexp_9xlN9yl-9sV2Vz7B0jk9CQuUce9Dw_ljStXFZK-cY2aHVtqcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=OJYgQ4aBMLrG09DDRCVGCsQTZOLU2nRZ1r8eg9KicSz67gIABzCZ3rKX8bbeJ0N-ISU-6mjeoX0bc3V6hfA4HLWcWcenw7FlrIQ8QZ4u8JcPTigqDrErVL_soe5a6baV9SY7ppbKJzmsuFdVLjXrePw0tL256c4cbvGOPxXFiVmmohA-npE3AziyXeRor9pk8i5pPPmVYQw-wolm--iRvtv0j2YkN3mimZ2Rif4i-VTYDfw6M_55VOWOgcn_pd-2EjwTcUmLfPwylVxWLm6ToAYniGU3NC3-Iexp_9xlN9yl-9sV2Vz7B0jk9CQuUce9Dw_ljStXFZK-cY2aHVtqcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=aZLBVSPfHmMkx8-i6Ur0RYsalWO7HTPwT3wozQM88DWsXs1RqsPRnD9YaTn9YnEcLyZQO-87pAAsDN9Ik1O893rzSdZKZf2zg2mmXdoB1Jzn-zw2mgEQx5MDS0thLw-CSYoxhN0DAYVe_a2Vp-mD_Q4eaAr-CBltDQYruoKFhqQBNdL1PKVA7cx45JYR96qbOE8Q1Ojt1HngBWqwrOyeSgf5ZIrARqLxnRlqQch5fxTlNuoYXhCmqTETv2bDCSDj5dex4pph_xQfR6sDUm6FI_H_CkIjX1OmUhwWgb_pLkOJ4WIF5y8bDAW-ypKUWKeQwdMWdT2R-9Rr5z0fT_layQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=aZLBVSPfHmMkx8-i6Ur0RYsalWO7HTPwT3wozQM88DWsXs1RqsPRnD9YaTn9YnEcLyZQO-87pAAsDN9Ik1O893rzSdZKZf2zg2mmXdoB1Jzn-zw2mgEQx5MDS0thLw-CSYoxhN0DAYVe_a2Vp-mD_Q4eaAr-CBltDQYruoKFhqQBNdL1PKVA7cx45JYR96qbOE8Q1Ojt1HngBWqwrOyeSgf5ZIrARqLxnRlqQch5fxTlNuoYXhCmqTETv2bDCSDj5dex4pph_xQfR6sDUm6FI_H_CkIjX1OmUhwWgb_pLkOJ4WIF5y8bDAW-ypKUWKeQwdMWdT2R-9Rr5z0fT_layQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVwecZw_ILKhvF5riwUHi2MjYVhRFe0dKNkm-TJxSp9_yhopfW9KphdG78PG90TkvT91FlwCDlehAifxCzE_Boty1BuCJcg9bc0EShhLq1fzf4gEuAUCZoKgZbvb5zTX_dGZ_zmm3ntOOj3WDVOdTzC3IHSEj1JvtjI_iAfhHHmJ3rrmy7JuJor5CWqO8LdSKKbC9MNUsP5hQjoXRR2S1YN2MWQ4MDJgS7-8eV48rNAcJ81HuT77cEpuejiXUPJ1NTWWBlX2dVj4wOpKwwdNhtzSze1O25kFELcvPxhqiLySs-R6HOVSQUfcX8bcyARaz6VnJqPS1DaC0q5ZfpAZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZD-Z7d40N_6UcFaYaYnxvuRycTK3ROEjWZoc8RCTix2NYOhNUVLpAHiODNH3dimHA9antp5_iNbDsocr0UHpbKcGPURNeRtSVX9VHGIsnVqYyTBs0mBoOj0Ug7XMB-nA-lhCH4vmtsS_xZiOX1iUKmyIcyamNFzonDFx1D1-czGLd5isHojjQBBPMY0M1ZZVVamSomcy9rHYWI7DC5jZq229NhsuqqdBNrumWVxmqrcCUkwAmdxNC59udzrFuGt8fc9MQCk40lI5aKCmE6WRdnZr-tbj-p6WVBddHxn8PjJvshTjRCqQEwml1zDWIHKIZZvrLRY4uOzf-vXgh-BoWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=iONkNCLk7VAT_qmtfz99738BCdg30ZylIA7fNnLTHR9nwox3HTJIlkkBbpQPc7oJpjlhnIS2n_1Xt75GLx3OFyegjmQu5v3KIRCnr9vKSV7JNDc9SfZPgA_oaITfjozxauWQvjEHT86HNg524g2WA3xVFWcvbdQMkBk78_K-86BD6DdWutsn7-zPYSOPBXgsh9jcHn6dnmH31U3TYEWHj2tAREzLMghdTkktiVj_NLEVs0qxXfs2okO_s_o9rdu-5199shOSZO1hcxYDfzZMohZ-zfTgViy9Tz2wUU83rEq_AmPTWSzGdG_JbvymgCzsa4fL5gwyrZ3yetrENQPenQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=iONkNCLk7VAT_qmtfz99738BCdg30ZylIA7fNnLTHR9nwox3HTJIlkkBbpQPc7oJpjlhnIS2n_1Xt75GLx3OFyegjmQu5v3KIRCnr9vKSV7JNDc9SfZPgA_oaITfjozxauWQvjEHT86HNg524g2WA3xVFWcvbdQMkBk78_K-86BD6DdWutsn7-zPYSOPBXgsh9jcHn6dnmH31U3TYEWHj2tAREzLMghdTkktiVj_NLEVs0qxXfs2okO_s_o9rdu-5199shOSZO1hcxYDfzZMohZ-zfTgViy9Tz2wUU83rEq_AmPTWSzGdG_JbvymgCzsa4fL5gwyrZ3yetrENQPenQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L91hF2PN3gx4XpbuU4pYhKdsfZgIb0VYS8snjRthrP4xTjxJ-iHfX1ubq3g2gWxUcKc9olcAk5XmWy0TIuaVbm2pI8bN_wjSU1AlFUQpgMw7xXtnsDf-O5Zqxwo5Kq0ZYuqXUy0A1V9enxLJAt_wtofJruzmLSS5I01Ds_qmYa-4Ytf_6bVdGsaJL7VTIIR7S3O9q5MGP3hpHTijPvUX_A0dHiSUZ5Ji29Q-aIKz5RJ0tjlKvT7dkl0KhzLMRUsStlELYimCSk5uAGJgRaNaUb9CaTuJzd3_c8LBb9tdM_hPX1YWtj-i4su8SCowZqfVXCO-6LIRJVgR5wq4Tu3txw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
