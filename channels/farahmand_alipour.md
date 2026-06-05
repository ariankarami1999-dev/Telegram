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
<img src="https://cdn4.telesco.pe/file/NQvxoefCyNHsxAdMFoSUUiQn7dEeOULtu6x-5LPzHeJdXXyQZOgefg67Ms2O7RIY8CAwShz_XwFsHCKkJrAnComUeu6E4hGArWatRH6gkx-peJm1iCfldMTsfQ1xONhjhfj0XSe0OuTCwRlE4XuMblB_XxQBLJ0EQb_HcVCqJ0pzhbxe0gFtQg8F2ktWG1vPJdmRm71z_fCqY7bS-zRxQcJy4FDBjINU88YQhvyloydKF1ndIUN6SphBt0rSEkxIlRF-609khjJ00THT-X9eC-H4pUIH6k5K0_KBc9OPTtP5oIlDK2Rovcycf7IpvZF-VEng0oMzpfQYAf1_j6mZpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 20:29:14</div>
<hr>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY99gAqmpfiE2H5fH1NbbcJdbCNKU1rLFCr6H-ZPrh-jxzqYliRgE_9fKPG3oPjiT1tUqu-sZ4yegwnJrr2FQCS2xG75FeV04OPOXvb0i0nP932ie1QqKYbDKygi_JNHPkVqncZoIp1Pp2yunnGYmjnSotn78rLxXn03YY4G3JJtYF_Yl1pG2vfr6KkuWpsfMc5SV6yRxXGFd-ZErHFnGPyTO4TxIxFJ_iPgJPq4MX6gwxgHr1Re6YmWMjEFswPjZW06wXgIdnItb_BpRVBz7EU-yxhs37xMI9jOcgzHm_TV4ucJbeALFQrhKE9SrLAlpi25jB_RByDQwjrfyV7V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TmaYvA0vaMIHGmdW3_JhFhcnVZ_G09WRy5NQelnzEFkgXi8y7eU8ttmlRd42UPwIcM6-1VgDaySv4rXCtS8Z_iAIJ5tQ0aPEmeW-D7gIcaSrvPB74P2m8f0CKE7Sre4YlREw_B6HcHW1m8S5HncVcxQBctyCqothvpdt6ntP8HRLLffd4p_mOrk0FyMRBSrsJdpyCXyE6mCXPtM9tgGiFoJbXaPLFXqodEbYliUqqRnzmKZARIfwC4jmzrg1ksN6ZjA66LEPK4Y9BepiPS3CY3FZVCf1x3g4uZKMHUngxlGIwBaL_dVcgnrknA_YcvyH9XdiRtVAmD19zZZqKDZevk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TmaYvA0vaMIHGmdW3_JhFhcnVZ_G09WRy5NQelnzEFkgXi8y7eU8ttmlRd42UPwIcM6-1VgDaySv4rXCtS8Z_iAIJ5tQ0aPEmeW-D7gIcaSrvPB74P2m8f0CKE7Sre4YlREw_B6HcHW1m8S5HncVcxQBctyCqothvpdt6ntP8HRLLffd4p_mOrk0FyMRBSrsJdpyCXyE6mCXPtM9tgGiFoJbXaPLFXqodEbYliUqqRnzmKZARIfwC4jmzrg1ksN6ZjA66LEPK4Y9BepiPS3CY3FZVCf1x3g4uZKMHUngxlGIwBaL_dVcgnrknA_YcvyH9XdiRtVAmD19zZZqKDZevk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn4rctaDdCBmGggT9sFib7X1aYnGvMuyw-58TkfHSN3H0qxf03rRMgsCgptYbw1uAGnpmnk-1cfVMcXkLKOB7eagWV3Cu5GnP4Igwpa_LmkVn9-SSy6kykNn9RmdyAf3NUdMqrjKEKZyxQArH2IY41UM8v4L7mw5p01Y1FmBm4PBAGi2gj3VC8YnC0F_zJYEiqN2MBFPO565xCuopu_GV19NT65jW_Bnr8TR6x9Nb0jEoZj3Ra7Q4yV0of-r8oHK4mHtYd_VWu2y4ZF8oPlzVidaXPA6VSDn8pUDdVndSKYj0pmLWVNJC95Ns3BImZ4mrYvzaQ6FwV6NEnCu0h0Brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-t4WT33XzNrlUV5DtzjTHNuWzOwx_lTOgpD2L5QMw-Wxsb3gj3DjWQXKXsPgF0D20YKN7krXzqBcDAIPpibXVtZuwyReefdzWobhDNr3OP8B5OTby4G4GvZ_8Pp84uxCHXUYjemX2OER3bJd6eMHtqcNX5jio6Q7CCyFfc0ZYZSpHwV9McnAi0JP4Rgx05ZXqEj4N9qBMB7tKcrcEMIGLU0XOOU_gLDVsb8hUTChnHzaH0u3-6alcFbTMOKO3JoO7AZkCmTtCKZ84BtUrWjLBfvyN1CP5UjxVDK2KrlquVUMS8VI97k4p3gRqZVyVAIepzm9V4OmMeq7XFV6ffWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRcepXoxx_9gwFjZdTfHPXcsUjHHg_L1Ce_LnoiOeRDWdmLT07fcmHPLEho_-eWN2CxUuLstnEAgAjO4PKhRATOYjZ_YjAN8yRaY51VP6VP7O1YMg7wSHXiYA5Wtr5HJlbqDmwFEvMPI9LIBl3tPWdhnlHve0JAPXLGSvu83sr488GJwilbD0d16LmQ-tNxko8aQwYH_V7vy6td3l4J0iTYzleInsbEP4izVLO9p6d9Pns4lCZNGLCDcd3uZbVMm4ZkI4CoxbUMG_JoHwjp1bsojskGbjqOQc_y2n419-6B2ssY5tvZEGxOG0DmMF8L2OVLgY6dL3A4aIMRbcPAxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDLAmLMqntkWAq4FiR4rftfLoSrCB-Y0gRVwASiMkYwNmoN2HtxDA0h8969Q0pEz_yXE7XzwgA5cLy6SaDdKIfxpFHBUf-xm_fLJuAFGfwfnfuBtAm6qT3sAn_7nG2oWl8Ps6hcnCji2nWrX9YCk4NHDb9jq104sfye91pbNRCGfdiDo8nw60xfPsjiyMRNmnoadADlvppFLNLvyEjcQYOTLgthuVpMbhEu2qM8T-49_H9GV_k7abPe_wHF_QCDpzBBv2KZBef1XQigbehFX6sle8iA0FOBoRwZvebejUFfjyRkLQgUaS1JLl1LnPZHsKJqCUT7aIiVbxdAtXC__6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyPPFuosB7B7NFMW16cRyhpD1360JavBG1BGsedE7lpypkZRH_ZFvDygBxjP3004LCec-rW2D4tSGiZlt4AZPh4oLTAaDtDotz6us-ts3TVg0GKzWD88fJ6Cvr-2LZmQI6TSRpnXKh29pk0rjKkNXuo6tECw_pTr1xbjadXymp9R0Rqb0re-_mMHA1FGWxR-ut7-Y8pc4qDQUhHQZ1AfZBWlhKzNBgPKY2VTqMcMUI0_uF9zpL7svUdL6Gfn9988RfR3Vc-hKOhPW1nl4xVaoVKZ0wZrXL6zEJb02r5eqF8apy6bTWxld5hAhypgb5P5ISYWeBoLeEIl8t63iISMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXAg4d9m3z2fildsIFEeiF_hxvaCXPfhNuCe1kpgf1CtsIur_c-10yLssnoGsAllr2txX8Nib4gl_bmXHLlYsoE8DRgsrRPiOi5bQYoL93M_dD0Y55vS8FEPD1owpetQ_0CjpnrOS0mQYM3BQ8CxxuzZ1hbZWo2lLCeJgirtWh-xTdJa2CmkLOHWI4PDleBXQzSy5k1YrQua53DMGPzzPoKsiXdubji8yv5sGS7Ji5gqpPYEb2E-p6oeJYhy3Lt61pNJkUaoWiD59zolz3i0JNUAVrR2dnWuuz1Gcab5haxgivDgnbky6PqOoPmHg3_kDRvh3CaK3TAOvMDanjGdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1734ESwsqR2o5BfnS3oqPFzI_AM7D9UotvMeaNmmjDKK4H04dH8YztKNgBT-0Q5MarEpOhBSYlxJuZmatt1OlKfKrrswm7XGShks5gbHiaga3G41Pmsh3X1EQgBGwVwxJuEBniWmEWfJlEwnIY2CrnbHdERtBwPhhhhVSMXJUxZc7yDMwlGhkrwvsCwJuK1Zl5xUtZiuCDsJ75LbVvu1Nri55Wy13HJU9R0t9NNMMyPB7z5oCbKMWbsPuvPufs8fI7f4TSaPPhE7mAhzFlIxR4hiQoHXnj57gMwZ0MVYytEufX5TrBo1OkVLlzF6-eXBq42lL5hqHIHf61zuJUAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQg9UrjkJUsJkot8EOtdanfFoBF-KAJOxXJX1hUv-2uWDUIeNIQaKdskVhAraneTbP7JL0EMcSbvVGtP8Y8WMkXgepV-I22IXgSLxd3ptcfZ0XIE6Cu_Xk7KfLxipqgL-zZRZd5s6FYoTS2sUOt8t_ghSY6bRkg3HfTtKIqHcCWtKPegkzEfRe3vBUq8n13QsGFzZ1m1dpTCz24jflgdowjSPtiz3s23AxOEcBHKBwd8MZl2jOz6by0wIDtMT2d1io3Ueuo8uhXS9jsfvxuWuhMHdIc-xh3uEOP_DmYeeow6Dc6uMHzVclCFPKoBWB9NCCWq8Ito7-_5GLypEXGFgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=h-2Khub8dwuLU0mtdtQybAEMgMcGadUHctvcwaA00FjjAlN1tPXDzsbV2LSDlBZFqajGnJkH0jkAJi4ZvHOt_X8fCM_KLQUUPHCe5kNylJAwvBXfQLHjzz_nuPXcKzYRos9k_7ZzU29lZjE_jnGqIpVSMN6vYApZz0u4--2Qmxr6HH8O4ejUfsLiBWC5Rhw_Fnqu0DxPE7-S-PFrSRw2pY0GAeK8GA4nfbII8B8thjmv5HEhIxmZeBvh-Ydv5tGuw8jZiSBJXe5DmkhfvkfFMni4qNva3-dTgFiRXTjzg1vK0KsLXg8DVY8HMIc8PLOKTri__U7Rt1Jaq6Y5Gi8LpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=h-2Khub8dwuLU0mtdtQybAEMgMcGadUHctvcwaA00FjjAlN1tPXDzsbV2LSDlBZFqajGnJkH0jkAJi4ZvHOt_X8fCM_KLQUUPHCe5kNylJAwvBXfQLHjzz_nuPXcKzYRos9k_7ZzU29lZjE_jnGqIpVSMN6vYApZz0u4--2Qmxr6HH8O4ejUfsLiBWC5Rhw_Fnqu0DxPE7-S-PFrSRw2pY0GAeK8GA4nfbII8B8thjmv5HEhIxmZeBvh-Ydv5tGuw8jZiSBJXe5DmkhfvkfFMni4qNva3-dTgFiRXTjzg1vK0KsLXg8DVY8HMIc8PLOKTri__U7Rt1Jaq6Y5Gi8LpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=Lr1ROb7msXrQXpyntWm4JY8JNEtdgFfBrRdW6ij7WLcxpalWZNxxnenV_okpWVpVuwcrUdn6yjy1OBVyhWv1BZAY9hqxZBAo1AlE6VxLUbL4g51r8qrSF5fGTv5VoRhHHFtvC4PoKyITg_7CjTGWUEKK1zocrShIvF78i8Bk45lWb8BuQ6zGcdr8drbAlpeY8exftXYkofH2aURb24Tmpw1Heb8pyLh25IzwIZlBYStVWjvqR5i5CjuNgFK0nCZrcxdS0k-IU3eAeozTW2t_8O3r0lNg5vQaIpBr0aBLiV2Tzu8jCAq1VZTTaIBODOPH3CKYTdJza0WonKbauktR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=Lr1ROb7msXrQXpyntWm4JY8JNEtdgFfBrRdW6ij7WLcxpalWZNxxnenV_okpWVpVuwcrUdn6yjy1OBVyhWv1BZAY9hqxZBAo1AlE6VxLUbL4g51r8qrSF5fGTv5VoRhHHFtvC4PoKyITg_7CjTGWUEKK1zocrShIvF78i8Bk45lWb8BuQ6zGcdr8drbAlpeY8exftXYkofH2aURb24Tmpw1Heb8pyLh25IzwIZlBYStVWjvqR5i5CjuNgFK0nCZrcxdS0k-IU3eAeozTW2t_8O3r0lNg5vQaIpBr0aBLiV2Tzu8jCAq1VZTTaIBODOPH3CKYTdJza0WonKbauktR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxE1kr_LqiTq-rqYGLFVzRdYIGgUlHtuF5vMy6iz-yelMbYrTklh3Xf9kxQgPsPgu2EtcVi6RDTKP8W1_D65vGzSsoSiUWR_JoZu8x9DV1YOJmlAMCtL_j2vEMV2P3N4jW7HBjyVTy3WRCQ4mfLYm1GXtMsRbZO10lXKUSekt1N0T5sftZfba6m10G-RxTRP_gWLqrKjg_3iMm2EJcpTFUCaWnNqOxKpydn4P1tX-T3Oj5m8gt_EkTUpW-zxjDdikWYwx6RsMPGFlVXD-Afe37dE_cGtjorEfXmVx8_JLe-Nx_T3FNLbOaiQeGVvAUeyG19dLqTHKmzFNjRUXTJ7u7YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxE1kr_LqiTq-rqYGLFVzRdYIGgUlHtuF5vMy6iz-yelMbYrTklh3Xf9kxQgPsPgu2EtcVi6RDTKP8W1_D65vGzSsoSiUWR_JoZu8x9DV1YOJmlAMCtL_j2vEMV2P3N4jW7HBjyVTy3WRCQ4mfLYm1GXtMsRbZO10lXKUSekt1N0T5sftZfba6m10G-RxTRP_gWLqrKjg_3iMm2EJcpTFUCaWnNqOxKpydn4P1tX-T3Oj5m8gt_EkTUpW-zxjDdikWYwx6RsMPGFlVXD-Afe37dE_cGtjorEfXmVx8_JLe-Nx_T3FNLbOaiQeGVvAUeyG19dLqTHKmzFNjRUXTJ7u7YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ojx1l6rTbKPWThfGt26wdVvjkWapZIH-e3i7eVFG5IhZ5CLJCEl4D1aHHjWEFazOoSSKuQCE4cKv6iFqMXdah_IInjI0_LyKdcAAKHDQt1v9_OBcPHgDVXlvzN8Yy028Gt3ripCq60L-IPTuo8xMNBzB6Tgzb4OBnUF7546IpetejZ3l4jr2y8uY4H4lLq1CXsTwSoGFJqsHsj6QlNzGPgHWBGKEfasRwck4-kFFHCAtbTUpV8bRIpogQkWYCoOXLrOpgrNG9H0JCK1ZCSZpokq5s2clscUC6d1i3tFUY7wHrZEsR-K2g10kQ7JqsPmfdzSEKpuM6ddZIFA2la4YIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfiL5Z5RpYRHvDfLcM8KfbbnQ9M7_TU3ib8t-r23WihIZD8AOYmVFWaWzRkbeUjyy-4l5UyKkvUGG0OyuNUZQSQNRBKMDBDieWuLQfB3nvsc8zMyIQtGan5s7DX_zT3wuJAtUvrEzjo3PioJUC0EmtNck0tW-JYfzhCamvdYyXuC1jot3guGVKm6ANX5oaSJ3N6xDL6AmhSogReD9Mo2kEwduPvgJkxkqlwlDI-lOtTX8sTKeXbIM0GR52rn2fGMDwNaO_uhe6TEDpiPXVtEjRPyNi8vizmfeRakiS3rI9NwirqnXhcFemdqLYgtKRrzzxlfto1-WLHYrW1UYsBqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=jZorqj8OMOCWzJwb6qSIedUd6Ad11LwgF_wpd-njD3jx90BTg6LK8ff-5h1jDYoBJTRlvomHU1pYSALrg63_CqcVbfvE8sAv5cF4f2n0qN3IiAv_MkLMnPknfCRDOFI8kdpLFAbkR64lxLdNmfTMbe3NLUOfPeDqUN6IMrRyRhTu1egbRr2-nfEGY4IQjfge5gNnpOWvHM623t0VZGTwW5B9CMrzmqQspwXte2lIHUQyp5PZ-T2aKBopYTWUbvcmeZU7Q6RRy4_jd_il4O8JUH97tNHMHMxRIW-KFz438j7_Mh3uq-k0UtiDNJX9FRd5gdj_Yk0sAHCbWHJzus9CpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=jZorqj8OMOCWzJwb6qSIedUd6Ad11LwgF_wpd-njD3jx90BTg6LK8ff-5h1jDYoBJTRlvomHU1pYSALrg63_CqcVbfvE8sAv5cF4f2n0qN3IiAv_MkLMnPknfCRDOFI8kdpLFAbkR64lxLdNmfTMbe3NLUOfPeDqUN6IMrRyRhTu1egbRr2-nfEGY4IQjfge5gNnpOWvHM623t0VZGTwW5B9CMrzmqQspwXte2lIHUQyp5PZ-T2aKBopYTWUbvcmeZU7Q6RRy4_jd_il4O8JUH97tNHMHMxRIW-KFz438j7_Mh3uq-k0UtiDNJX9FRd5gdj_Yk0sAHCbWHJzus9CpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYXpLWATYZmVDMEcY3xve2ScZ0SPg_c3QQ-Ua0DLUz9b0vfCE4h4K86Ql5xosFekwxcep8LSGwTmVmvrpFJf7S3wps4JC9vQ4QHh_yM2703dy5QKt7MkhaQ--UQqvGpsM_yaF8yeMPPu5OHwKQZQohhWwQ_OerNGFt9vnLLFMxRQd9kBV7hecNy-rHzVoDAvoq8s_BklZJ3feFi4Ldu0_KuicA8TWXbyBKfnJEwS-d6QX4QF4lGbHNqbt4l-6lOlcP5657l1pEcrG1Qn46DuEofYfhHAJdiOZxOpAVb4ppEgmQHcF5JTPFhzzR1LmLIn7Ql0bDRmGqiyBTs2OFYOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=hvcUnP4yqaoQDBLOZVI3mKUcTFbSaUfIskWu6VAn-ZNmhBhfOSnmtxHa4cDhcwUozE_1nwdnQpC9b9ZUQAOVeeUF-fTlT3Ziyqndeexk97XMfHRfPZosUR28zcXnykMKkYq4RGa9kmoWKgV8jySS7MiSSDNwCLXWvsbIaeT0yj4Fercy1G8xdcTDWNYNrcQKoITAQD4PkiOsFYm5f5Jc-sCh-VGvwPelTHqFgJPzvS5ptJl53XTHAU52ls-zLeDbhwKc0aScYAaw1Obbd8SM6we9YAWm1w6ysDQNPQ4PJ-y6LRuZFV86Fruu5IreWJk6kDC07CaVpOGNKI7O3moi6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=hvcUnP4yqaoQDBLOZVI3mKUcTFbSaUfIskWu6VAn-ZNmhBhfOSnmtxHa4cDhcwUozE_1nwdnQpC9b9ZUQAOVeeUF-fTlT3Ziyqndeexk97XMfHRfPZosUR28zcXnykMKkYq4RGa9kmoWKgV8jySS7MiSSDNwCLXWvsbIaeT0yj4Fercy1G8xdcTDWNYNrcQKoITAQD4PkiOsFYm5f5Jc-sCh-VGvwPelTHqFgJPzvS5ptJl53XTHAU52ls-zLeDbhwKc0aScYAaw1Obbd8SM6we9YAWm1w6ysDQNPQ4PJ-y6LRuZFV86Fruu5IreWJk6kDC07CaVpOGNKI7O3moi6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=DKW57lL0hOVRFl8-RlnW-rHmdJgxXwxG8xOsIK3gfrhnKmWgAbIbRxGN8sFDzKWcKKwZqzDF18C8wjVtd1AsnC0N5PplvZvf9MF4FepnQ0DzWykhh5-IVRrFTMrrvpd0HUpMyrnRPeGFOCMRbJrMmZlPv-T24Gg4smPAwmc1N9DE2e8DXIbz_IB_tqBMqZHBeXQPS5lgg3Bf0XHokKUXrEkJbdn68tFQZ5e6q1hVbRwiQbDygg9vTvP-8-QaTvNuyN3GF4MzId7TuoRex7R_QqqekKXUieeroB_RCe20E83Kh8-AYNJbU84gVlHyr9MN2YmagqXzHH0pjxQGPb6q9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=DKW57lL0hOVRFl8-RlnW-rHmdJgxXwxG8xOsIK3gfrhnKmWgAbIbRxGN8sFDzKWcKKwZqzDF18C8wjVtd1AsnC0N5PplvZvf9MF4FepnQ0DzWykhh5-IVRrFTMrrvpd0HUpMyrnRPeGFOCMRbJrMmZlPv-T24Gg4smPAwmc1N9DE2e8DXIbz_IB_tqBMqZHBeXQPS5lgg3Bf0XHokKUXrEkJbdn68tFQZ5e6q1hVbRwiQbDygg9vTvP-8-QaTvNuyN3GF4MzId7TuoRex7R_QqqekKXUieeroB_RCe20E83Kh8-AYNJbU84gVlHyr9MN2YmagqXzHH0pjxQGPb6q9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rq0aD32EzhBiZIQTRsDeuUPbBPDuOYAkof8SLcxebdia_FVj3EtCTJKVx-9kmh-GOiI-OBrvcsflqkPXSjpYLO9_cQhaQbiAWpmq1HqzTLPUfmAR6iZKjHzJcSrjGpanJ5k40Jb4Mk-NysLvLg6XhigJzU-xeIs4uA0mSwfkmagRC3fYLHFhgQ1lK5JoZ-Vj-aT_7-DFXnYBEJVgHSXgf-_mDjamN-dkyvRNMnwoAOYTeYmB0pARoVX7BUps7SGp_vkqLarHVjZgTw-YfWMqK9m3QaUnpnLnucqdsfdEtrHu84dyco7HqQ2nG4BCdCAls6mvXAp8HDDUpbJepFyigQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rq0aD32EzhBiZIQTRsDeuUPbBPDuOYAkof8SLcxebdia_FVj3EtCTJKVx-9kmh-GOiI-OBrvcsflqkPXSjpYLO9_cQhaQbiAWpmq1HqzTLPUfmAR6iZKjHzJcSrjGpanJ5k40Jb4Mk-NysLvLg6XhigJzU-xeIs4uA0mSwfkmagRC3fYLHFhgQ1lK5JoZ-Vj-aT_7-DFXnYBEJVgHSXgf-_mDjamN-dkyvRNMnwoAOYTeYmB0pARoVX7BUps7SGp_vkqLarHVjZgTw-YfWMqK9m3QaUnpnLnucqdsfdEtrHu84dyco7HqQ2nG4BCdCAls6mvXAp8HDDUpbJepFyigQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=b36lk-8dMoYaKFeCPNFpYTlCA4wABP9uqesW8Xtlhd9vH6Cwg228sVZMu7BK8tURV6UyYfcpWyA41qUJotu-sRnj3czrKXXXqm883lsI-_gtZ1_o7aGuXzx4URZIMTeldF8vPgcAdKm0xSrKWMpTYbidmTpZJRNYUsWYK5Z5rrn5ZIN1q8099yQfZH8Ne4e2dQssBwHnyMp_cRP9Qq9TrtjaZNTq6HN4-JENGH52CY9jgu9DbuMcTUsCqhjUXkPH3DwOaSq78vapQkRWmZdSngvmjXouFjOz32EwL9qCeo359IExBdS_hUfLaR8zjrStnJJZ3pbPinM_61Nt7wc5jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=b36lk-8dMoYaKFeCPNFpYTlCA4wABP9uqesW8Xtlhd9vH6Cwg228sVZMu7BK8tURV6UyYfcpWyA41qUJotu-sRnj3czrKXXXqm883lsI-_gtZ1_o7aGuXzx4URZIMTeldF8vPgcAdKm0xSrKWMpTYbidmTpZJRNYUsWYK5Z5rrn5ZIN1q8099yQfZH8Ne4e2dQssBwHnyMp_cRP9Qq9TrtjaZNTq6HN4-JENGH52CY9jgu9DbuMcTUsCqhjUXkPH3DwOaSq78vapQkRWmZdSngvmjXouFjOz32EwL9qCeo359IExBdS_hUfLaR8zjrStnJJZ3pbPinM_61Nt7wc5jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEXZy51kOr-us57faew_ixh-6gh8QX3Ne71MiHukTkyxHYtcWjXvcm62vGQ1raBPhZqjU9WyTC2oQofnPlNs4ewU6ZYPd6OYeU95RT7Nxgrjo6pqCHulGiz0wKTvrfoY2av3R07at5BZretYPr64cv9C7sx_53y6B2Fs0BB65yoyVQoohT60qu0J-MoIR6p08oSBkjGbWfeSbuHyM7ZgCWm5ZRSNxKTK7nHIO1t48Qv5Np-vKt7p1ebNPnCMKI5BXP7pRP1WMFEbT-h8YONXHFivA7do9xcFvdmHwNgqdFwKZwhKb8GsyTov9XBNK3g_FVB_dMD93Pcjb6cTGlf-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exm6VvkmHT_dhvY2hRav7F0AJHf4MO8Y9qW0X80sTuoz6Cak7Y0E0eZ0YvvM0LHTN0qb54Xw0T-_ffGfMRfW_G6PB44MRSyLXfV1Jq3pfI_TVAKKyp7Hdi76sneQ-Po5hw_EXDAch7XJdBL96F33k3YS1XktbLaxzwOTMBLjz1pwPjx2HcegKd7ihdWDrsdW3Apc8hLBkpYK_mDvnKxKa0GpoiS_tUoVascTPPVdHoX0R_9snZllECnApDVuQWn2gUf105_fjFiQWsAQwPkJ21Sm-9jPU7TGw3jn8Hlz_mUFTrB4aX348et3NCFZKHLIqJS2GcMqFfu0jKGz3Ke2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr_SxmtI1bkjmxx46juBDIIkVa0LKv74TTRAp5D4DEzji9nScwUiJiF-ZNpWqFveIXtOh5Cnww_I8vmrEte20ImUZ9Ey9C_vdUpr9VYDaFnCZ2NxZd9IzdsVZqrm_pyIv8laxOtB1wjlCKt-wC1CyqO38zagxCuwYoqsFcQjQ9NUklJGNQFNSscvKJjdrNB8AOLLIC4qOCG_bo6JcCmqdFq3fyoiOsFiyHD1di-MPTVVAniZFFC15tfjVWsYDYdjUS45n1JB7s74oSt9N85VjmGd2v1ssVmZvYWOm6PQJ7wbNWKylM10n0YxEhdClsRbyrP0s6PWcRcjeVLE3cid7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKu7Jg1ITFEltjsXo1K63aCzQupFc1BLkT0oosGkc2z4BidNb9j1UKJD1iXDZDuSFGK4kAA9IOG7v4w3AGqQ8W0sh8ZJESpyMQ4-h2xpPtxU6k38n7R1hhwqzvga_vTkiv0xIAbpt9QX8AoD_T-e2TNSJh3C1zC1W7FYMbXnfZdVOgF80whjWfqX9TOIpHpJkM7VV3V0CEarQb6lXpfgM5AOVp93lOc1XUM7bwraevmK91nr0lPEnf0cbtpymB0Kj4DkEdwwl9TYV_QON_fdd-dTQ-zWENEqD76fdG_r7-qaiFG71wrAm67KhyTgZbx4VzQkf3WL7s_ngtpEJYAiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVl2bm8b2CCcNLvZGxG7IFFVdhTIsewQm7Kjr-9OWL3fkKcdvrR43ELb7jBJ-JsDMTqj_rIfHu_3tRPpBCr3bqelIsLMGjAYw5hCHiwwxnrehmoarspBfVECZoJ-Y9SR6EyP-jiXVk56c_e1VVOujriFv9H-L0qTQ35JNKgVHf4wFJj8cgiVFLtkSNFMHVKiZprWnP8Q1XZOTDDb0G7oY8_etStqZ50p4ge2k-RvwDt-upTOFqY6P_kSDAM7FOdAb3yiZioj2LmEXeMqaLn7qnwGcVLWpg80y6XCS5Zj34LbJkWZ-l0-lT7o9I6e_uLw4_AEr7MSRVGL8LqS9jUo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyC8DAHzM1q58OOEqS2lM4yfk0tBaIzqwva_nNHjpqrJdpZSYXxmGl7YCKtCe1jygx20qMZU0Mtpr6NPuIKiJZN45T6PQOk7MHT14_J4Wlt1OBoa6uAFEq7ol4C2kkRx6ECJlpu_81jRj9peF34WtlwKcxXc6yVkpLl9U_0qI7a1eduwVTpUd1gJIWOj34rUvec_RniSH4Jo5TFg4SXOKBkaKRrCmNEnmVOhRgtscLDmSKK3HaN2Xo4XT1EHF_Fo_RlpKVG6tJhVvWu3W6t499W3fo25Owld284Ws2taefO23UD_cr8PAPk4K1l6hjnDeOAiQjB8HOdiqdjqem4rTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVXgyQgq3lmQm9NoymillvsSkvTLZxRL-qfNiwl-eRXuXlNvohHC9zj-d4ZcfaJBLYua3lO6UByd0Z3yz6ojLY0BDzQI2vjc5VRu9MesHBZ-FQ8AXHCB3KL-Vs0MeNqt3hhccdQ02yhl23y4SpJlPPcFSW9lfIJ4d5roJ3Ll4l_kJ0EYF4qaXx9rJOgpEEGP5VOYyKIzBE7u3mrzEulrrRRsuCfg3jn_1wIzx7iNiM2xR3BmS1YZGb_WPRKmPOTtPfOA3ddEiOZvnGmIww3c9meZvz8LfBnJFJwDLgpwyCtb_pE8ETbUZ3bV1XwaWj8UEQ00QS3RligKuwAYIpFA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=unOZWTjm-C83w812nPVjhWY1CqGUzGDhdJMwp1xmecrLtNvjZRrvx5uJqD7GRPqrJNMu6e3YpYWoxbdpPZA9Aeqk2SX_0M_yhAvPCF23WAzl4lHyAsuwUo_O4Ku0QgWXNL14n7xu8NTfrvDyCKwQ7yJWeNYCmmxaz9HoPww2bxNcu4JQSuU2sX_XaUZ3IgS5ig-KkEhSME5Pi8tZq7TQGFaGGx453iDBfqBR73l-cq16emvxN9_LJv09lz5XmuP14CnQqCbLTEPmhfxS1DRrVLfq3NLJqHAnZNrpQfwHWhZTp63GX3S6NK6IJlaerigdjuCyMnd_A0wdbbW7ysEjFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=unOZWTjm-C83w812nPVjhWY1CqGUzGDhdJMwp1xmecrLtNvjZRrvx5uJqD7GRPqrJNMu6e3YpYWoxbdpPZA9Aeqk2SX_0M_yhAvPCF23WAzl4lHyAsuwUo_O4Ku0QgWXNL14n7xu8NTfrvDyCKwQ7yJWeNYCmmxaz9HoPww2bxNcu4JQSuU2sX_XaUZ3IgS5ig-KkEhSME5Pi8tZq7TQGFaGGx453iDBfqBR73l-cq16emvxN9_LJv09lz5XmuP14CnQqCbLTEPmhfxS1DRrVLfq3NLJqHAnZNrpQfwHWhZTp63GX3S6NK6IJlaerigdjuCyMnd_A0wdbbW7ysEjFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po9EOCyd1EBY3I9uSdrkRaCDjYmOiXlDf1mZU-II9nS3fIu-3jwNJbcTr9DQxf-UNWt6iTOWVa0OR_kiWZ6yWYlMvxVCqvGkTr_ZIiE7TjLRV2q9UUV6eU_b2ZMrvJ2xBsQ_clg7Fj8oE7KMzFLFzz-zoBZfq3i_V7T4yyzstqhls77Vdjp3xOB63iY-Deij09iPx3L5bxHYH8zBnaGoHdiKvjlq7dWTmrH0f0fwcrJPXX30d4wOIRYjCvH5Wujvm4bQkXnuB5Bb20IH7Cy4axsKskZuxjdWp3gd_KIfZP9k9IHYv7-g27gkYBkhvDmtnbHvDdtHhR3uDqzgFxNotA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2X25dYy3EMQncN3AdCNvJIhLXvgcGFnIwL7i4GpukYAIc6EzauQRJzOQTs6Iqj6uhS3A1i1iR1_DZMkeIjP4FNIBxHOeGygAuSSw9oiywEVbGpjvQ5PH8k67HpWHLuDRvIHib4YdHhdsUol-8-XirdTmmQVSxU85D1BNUHOx5s5q-Prm0KqJ0fzNlZWd1Y1ytB7isQk_xv3dt3X7MwgbDBTcf4Q4ip81Hvr6E1hVpLunxcEUjoNTqceeXg7zG7I1peFNmbYCiiwhktRo6IJWnaFIzsLSxHTP1Aj5POX4HK-NmXZjsFrV-LWllvLvAkSOlvNy-4dcmxcMrtouP0xuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwgxyJX3T9-DJSgPVpdtEZpCCv7au9yU8NurwPOg5R1wyyMzcV1AG832-6QKzkPKLKeSBW5px__x6oLW4T7OxctWgnLnwA01t8qeRmfWHuNAg9R8s5h1AxQAgOzCMEfSOSc5qfuDWLpYiCAp_pOuMWKrrWWGoG1Lu5aWpBu0Mc2yoXzVWKG9-YUVqe0UpPK2OAwOQzD1jMeJBXVCMmYJuNSJovlZ2BufDsvl-bbrdZlZPbbmWNWQPyub26TOZ7X6CPhkpS7NMo7u_PE1JYjmJpUvhnKhrFvGcwIjdbaKqyirqIzKvYSB-ckzid2Om-dNeEHD_5qfX5aSV7TPlclAYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQd51-dGUevpHhQ3D4r2--6dAdETFgZwhmAoH3bdTePolXRKqw3GWNofWXJ6wh7eNwTt1353k85wr16HIh8eXiZRiBx-vnU0tp9L2Rwhq0JXGRgYogoeuRFrKwFK4edTdHi3SZ9fvznUUuB30mPKXJrQHJe0-vS8KcKbTD9t-nb6PPzUP6yewOaTub8JdqOD_ssTYhSUVnZwUC2d1KUOXTYKJforvsUrbLWPCV5lej8_zvvBKwV3ZXGtnjkaadXwGtTnTV3H8QUPVh-cJda43JrUQ3t7QL_m-J8XcF1cfo7viYE8mg331EgEOe2dYHKJdtw73rBi_JkaETWiU9cGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7nDiwQG-OikfeLPpgLzyr0hWsCwyzDpO5bo3mzzbv8RUnx0HtOpui706cZODZb7CFP_yyPSjhPN28MPg2k-rcPazAk_cS8HFdye7w7yz-O_QM9DpGs5qf1r8yl_i4DcAhU3U2fq6V8Nsdbgb1B9-31Q_di-63Yxx459AEo2LdXesOlw534WF3KVTXw6lo052FmHakPzJvN7k_mRoYpGJ2dw3CXRcRUCLaNaCn8m775c4wuf0ArikQ5AH2Mq0riK5pmltPJwvuXzNkv90MEEW8NGS0uuPD7354aGOG1RkcvA2SUAy1AZR6Bm8MAymkeZUDSZSbvj-VUprgBP2wg8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXbJz6OsaCkRvr8jMrYMTqT9_QaRO47EG1jrkVHciPrnTX1kj-7F1bfryu6A_w6DG_DxBTgoveohkP_CCk7X1ZNaFmv-25U5M7LH2EQbuxycDBwNfL92pkh41jQVp13oCnTHS6-oJWGTfuvE7N7fCKGImUR54rR5PhoTTHb7bHAY9wKlNyLj-J8rmiB2z_SSNF9Wnlx55QxGtGehQ4TZt1E14G7I2yJ5D0btZoztsF5GzdjBjuXPCv_3-FqLLlDF-mMaOz2tWir8OsYApnZrwe_wntEunWSkGNFY5mYXg0HGWQysox69QH7WJr6me3I_6oSlf7rIXc0UWUq39Iqp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sgj7XtctFXB4a-YJnsQ2dRFdyyqkNy64iLeOsXcGEDplk4MdNjgjIMpU3mYXXi6jFMxeYX5YG0tFRYo8KJptRTFhJ-gk66_QBG8vVtM2cOwS-xNrqMzE1s37bNXGK9_weFO581fxB7vKOxdeRwZKPCC7EJvfM_UgoyF0oq-2vKBZDtaMkL6gGCTX5_qukHjHF141BshXQ-Ohd7xUNG6q2mTrzeS1sIQflyoBqdhdPQMitJNegtcA5x44cZhrSqBub34hlELi2yU0jHRVTn7UsqgY_5j1TkuxK1EqlGan6PyZOCBsdp4FbgFc0CuBd7uF_wD4_VTsX8C-tI1G-x4s1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3JtkbsABKAl-17ERXq_PUf5ONcvYmGSZjmV8u5io8Q7Rkj0hXiACxBC9KjA8pYEH2_n1zDOwdogQRZb9VAmX1ppM7dDpsybfxGThmP7COsYC6eYe4aKLYK0TiT9Ly2OYEWfS3FEVprS_6kzYtrU_5JYJlv8fKO-22RrZzIwU7uQ7nQ2CLebg6R27aMwz2VE6CpDrHxKwor6_amfYeD1wKD64dzJbkrZKkiTl2n4HmpdNC673TLbpsnd-h8EZWVkQ8ucgMv0q0BbPyCtK6DfveCg1OBhjIwbPmISZzUml3n1TY2XrEmHtbKVOTUzoR-zW-Td7JdbRyZzmfCHOFfdnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=jCpSDihrqoDkHzb6-IcvG-bWios1mnSBA7YDfGhCqmNxyEn053Z3nQ-ADzaSkEdYKwOu_jNyYqNBTRDNvWvvlVkSZonN5pclaas0sJFJK02xsCdkt4lHgmoe3pbQDwaGx8WDl6YIk1EcPYXe-CwKCOJ7cXSYeGDF5B2LxwhdTgY84CmFrhLpcHVae0TbI7Ukgd6xWNkaTK87hMMwXcUi5qQYsLT5h-hUwDzqI7B-PIS67eQdTTFTRRVxJygHmqwnN1ItNhgcOYBmMFJ8zPWZQ9Nmfo-R-cOHBtQ1HLDztiRyYR4y4wPMbSwZ4_liUqN-Mt85mGyBbG7DSo_QXeMZYFu63UWh3ujMe1dGvOWVxYUTJ9YdeRX3ScUExSZtKWCKeCF9LaQZCYG0JiFZBjCi5eKx5V5ji-1xCI5UgirAbYq_5bGQwMcbeJ8ZX4FyIsCDS4XMoH2rq1E9rkNin7c7vtOte2KQiaWhvh_MqlcB2Fiq-A902EejFeb3rDqLiRdyHW0is5_BZZBwzfZGOqFgl2e60CNoRo0ottXFJzm3qJQDSdhSqHCXVMZRsciR5gQfgy_XMIysjBeTKb4xXy5I4_rBNyQ-cNk7LKeABzxk5H81nvmXy1qkzz4WWDxzWymEjzmGaCRr_wFWEy_bDT00gVci0zNzUEGwBPicRntk1Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=jCpSDihrqoDkHzb6-IcvG-bWios1mnSBA7YDfGhCqmNxyEn053Z3nQ-ADzaSkEdYKwOu_jNyYqNBTRDNvWvvlVkSZonN5pclaas0sJFJK02xsCdkt4lHgmoe3pbQDwaGx8WDl6YIk1EcPYXe-CwKCOJ7cXSYeGDF5B2LxwhdTgY84CmFrhLpcHVae0TbI7Ukgd6xWNkaTK87hMMwXcUi5qQYsLT5h-hUwDzqI7B-PIS67eQdTTFTRRVxJygHmqwnN1ItNhgcOYBmMFJ8zPWZQ9Nmfo-R-cOHBtQ1HLDztiRyYR4y4wPMbSwZ4_liUqN-Mt85mGyBbG7DSo_QXeMZYFu63UWh3ujMe1dGvOWVxYUTJ9YdeRX3ScUExSZtKWCKeCF9LaQZCYG0JiFZBjCi5eKx5V5ji-1xCI5UgirAbYq_5bGQwMcbeJ8ZX4FyIsCDS4XMoH2rq1E9rkNin7c7vtOte2KQiaWhvh_MqlcB2Fiq-A902EejFeb3rDqLiRdyHW0is5_BZZBwzfZGOqFgl2e60CNoRo0ottXFJzm3qJQDSdhSqHCXVMZRsciR5gQfgy_XMIysjBeTKb4xXy5I4_rBNyQ-cNk7LKeABzxk5H81nvmXy1qkzz4WWDxzWymEjzmGaCRr_wFWEy_bDT00gVci0zNzUEGwBPicRntk1Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=WX99Z7WfGLrMgqmfjhH3EG3DS5l66988bdy8GSY3yXuJGqBj92c4xjJt9NFDwPruTiEmsjnYUWSjCsPt4yPmPzVbG5sCHd3qrDIbcgBRcfT61ctxEqRuD1PgV2kWoaQmvqGKp9iHbYwRaPni0EDXobFH6FQ43e5HPuM9NiJx81jD8qXy_RoOd8tNKiWUQxZAt8SIpgG3X-DK7NFaUsJI--nNM_g1fu8dSbZFpA-5tecnA-REtpi9kPInsGrSIus_MiBzxe_6R-2hSgagO_gF69cIfIVo5dsh4d9bWGp-JHTi6CcugP4Q-h-yJFxZNT7tm6pkn4qMF4CDiOdU1Jg1Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=WX99Z7WfGLrMgqmfjhH3EG3DS5l66988bdy8GSY3yXuJGqBj92c4xjJt9NFDwPruTiEmsjnYUWSjCsPt4yPmPzVbG5sCHd3qrDIbcgBRcfT61ctxEqRuD1PgV2kWoaQmvqGKp9iHbYwRaPni0EDXobFH6FQ43e5HPuM9NiJx81jD8qXy_RoOd8tNKiWUQxZAt8SIpgG3X-DK7NFaUsJI--nNM_g1fu8dSbZFpA-5tecnA-REtpi9kPInsGrSIus_MiBzxe_6R-2hSgagO_gF69cIfIVo5dsh4d9bWGp-JHTi6CcugP4Q-h-yJFxZNT7tm6pkn4qMF4CDiOdU1Jg1Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQTiVer46fjLcen9K5WqRPnipu6Jn-RPeC1Jf3dhrj08VwcCdRmfKskrsy_lUKwk2NZOr-Yyc1hxW_XWYXfru6jpn67nWABUFnn7fLLvfeMnNJrFNy8Wm0roL_uLEtFq82kIPXIU6hOLa0joerEpm_ef393CgAIPANZSB_Zq3TCC7j7y5h1lNaV7gINZ5JxvMMY4KrPAqRk3t9mz-DY9D-Sc2D0FR6ETK-XihT9LgGPoX3V_9tYCJUnkt2dokB7g4a6MQpHxV9_2z0dq11kiKorwzRANFq-piibq62IZLvfbD788ddrntSw7Lsba2DQPcDAqo6s-OuxbUUP3OrZEPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAabJDUDg9ib1tPQ3--wiWkgz5NEAS-hsO6Zsj7VRARInnuUy-efwMLuneFatnlijGFgVN_ty-B8-CyYGb6c9Tdz4knnmVQzmuich29Qh1k2O_S46dQtyzpjgw2IaRUBRm58lUQpo2dHbkC214YVhQVoIWDSRFA5hfA4it8H4CBfMN5KAtaejn3-kOa01Qp6QES_tObAYTudwWvTdcGZVxiAb7NSakTakbvFnmI3rNtv-WfBZHWiz5fp2i2zDtDDVzO_v3G9-eA3gDnN8hbVXqFCsdXF7fKRUCDu-aksx6GCMItUe9zXLI4xA8KJYBxBiOONeYt7HaFrhxOWHZqm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AILGfmVj76s-et0hg4B0grtOJbViFBG9Xih0zX2FzKGnbt_ZoQ9bb5-hD3ed3Z3C0fys9fWeVDTAt5lD5EKBaSFHO96BY1LIX21QHdXhSbp0QPZwRh6qSIE_pfTZ0jXO_r5Li5KecPv0EILioszxI3xTxnzeUhKkx9Ujs3o1ZBdJRLMaqDij7t0ydccq_7MULYPf7dHDI62MTNdQYZYfTyFNqFlV296e3QxOnl-e1bl6CepeJgMK1j034nZDYWazAW8SfI0gQyYvQ52Vl4smjohQ5E0cCJrdz1fXQQbHfQcnyrGOdL1ulGijUZjqkSGG9uGJKR1XNSNJcdiPGbtKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj1IZMgKMyRGTJJe6dtPElpfYzgdAP5vvcV7JS3leosjkVXj7mCDcDP-5i7P2ztBUZ6uJqvTZCtgrfo2tEuWi5w1sbrdBXNRnC4HSWn92q3f7asfC7RSZ8ODoM0tCsx9U7CNo5bEHQiqAVR_x1xqJpl7Bl1g7U_7BHHJbTBt5DpgHd4e7ynnfZebrCJFETlE8TmJOPRieUEu5TlM9oeCA5t8zQHLwrarqiitOvf0MEcj14IbsxKli2m7umfrWqv86JiWtvgraer7wg47eHzAiLYEQHn1474OdURkRYGlUPgFb9lx0HrU8DwEhd06E3CDi0JuQ_tAgImesvXOZDvowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVAw_Ea7CuT6tWPWJlrOYmUPkdv0znI8-0G5JcQf03deCd_7m7tyDXWTKPamxJqzo4CF1cy5USB272ljsVyFZHqWYX6a4Q4azJr1rBY4okLRyODntJ2a5V8fjA51c1Ou--nIjfyGktcIdyuH23acl9F208w68thExW55Sar-rMNhBckyu_IT5TJ1xK0i6toPDo83MHbPNKrji_GA6Oz_ZJ8lNnw8xYc3IyXxxOW3Bo6RUyNOw85syvDX8DZ21mjnMryUATN5YW7SrjbqJJffOZGuUeEGgH3efhDVDQdrPaFAbrDAFgHBTgLILrmMk3AVZFCNHRzPfKwOTNqglf6V5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBNEFsipksONeoC7O7lSBF7fqpWweho8XBNGb6Q6zdOIBV_URfUz1Z8hsgGEJW7hlhUyF1Hxg5QhGgO3eaIWpn7HJzqw3oQ3smnVOuYL8O5n7socp-9lf4gUrJ13NQ2btAc7q0nr3sNogCnBdRZIxjAdPn4PZBOr63iyngkjsQyFgEiSnPZMnDysdIvu4MaLLQWetKgRFR5hGDfBJvCsuLd8MfG3VXdfqkLZHWfSwYFhbD4o5RqekyrSUFB-nR8yFLqVUWAQrAsk8Vt6EsDJu8Jp0AZQFgq23UT8XkcB9zoiqTvCQUWvr_iyoU8JfaTbcYfA22S15ew4W99HcTWC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd6KSfxKtyVLCztWoPOk1kKnhihY-TM4xcAHF_bb3YYmS6-cGzcscuBmf7aNTXW6xeyefj8eSab2zZj4ctzJE28LuLRARSaqYy-KjzhLNxfY2V0EvfdUBBivjkOLleasmCtKBEIb8yvwOzTr2FX9yqJqxhk1DS-yM1ukaMz6mRWJQZSKwdpYKFGyIlVcwezlGvsZNrpeRWa9EsYDFfzZFMylfoDfCCR9iTaeppTUODOSvri7yeOtO6Kz7PYdjHBt1Rzsgmg9sDVV64iMYQhNG5hGzs6GVE7iEBQY1QheyAaiPVHnb_GXdw6CrTDKuzF_bUUIsOJYR0Mu7dMIchThCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNYLRzYuLGeUTo8aevyoOLF7tOBYTjpwHHWeR765ozO1SPXW2OAGhaZk6MgqmwD7bUr5A6T_OihqSS3yU5XmmiK3-IUZWVfAflvBvWs001xEHCSKsl4pRSXVpHTAqCIlmwQ1-1G8z5s89j8PRazurV0UAsQA4xEyDL7jLpkqnvjwbIt0uQ4fYSunTnrbgj3mhgq_v52P43ERMdfjY_7l8QRbsjMyd5s2K3CqNfAyGrylMeKePTxkFdIOSUtH69lnidfWs_B82EZOcjPi6OaL989oj8h32diw9hjRnXtUXfdHx_vdU3yNTS2uR9KZ0BuNLy0nNG82EjWaDQ6V_eZd_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcMeLhwZxpnIGP6Vu_dzwga0Ya5BukjwKNbZxgmuxTFG4AmOGEKc4pRf9Oq8hgIUpjlXxpgRqUxg8ZoFzCUvSUI4VPopYiV7Q7G5mbPchbdl3LqkfpWlqcpthyX7SSEj4lndB57FnzT-OsRI5Ot-5adf1wP_i6DwleJdtyiVs3LGhKKEhIDuptVGzWvOxWQqObv2szJ_wgwqJm2nYmNqRdpUj6WKy1RhmlyeiDDOc34OhfQf53A-eoURsuwdzd7-tEkP-C7HoOlL2jQb-B9hhkffF0In84wiwV4Lyx5DlC9DbRuxsv23jwkxqZL8T7kCdtt0bdHqPVl-R05BrzPQiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=C4pZxdaA3dSTaIVoXNTp2gOdE0VuoguAodoLpQ6pjegxjCyl33I-9lg2aPfNgk-aN8nhZkBPmt0zM7zVveU9Pw_s-MI9gSMLi5N1cH-_nJvawbxdQAhprvFt8Eh2yLVRnqiyoUgvAswEOIdCYhX8cZojMRee1ct8_NMAfOniiP80I8kz2iNdj47g4yCIT7TORWpNhi4js_fFmjZFdgAueRWUoEeKI0qbk8m-JCeZwk6lcEf_S-xjULqUZWndOVINkPnvc6PLAV9d3QG0MOWrevIsa9ncJXaOS-6ivrYGfK7eIWsvZ_Xh7AHoClooKlMHXYskFuQwX3boABRIW7oDTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=C4pZxdaA3dSTaIVoXNTp2gOdE0VuoguAodoLpQ6pjegxjCyl33I-9lg2aPfNgk-aN8nhZkBPmt0zM7zVveU9Pw_s-MI9gSMLi5N1cH-_nJvawbxdQAhprvFt8Eh2yLVRnqiyoUgvAswEOIdCYhX8cZojMRee1ct8_NMAfOniiP80I8kz2iNdj47g4yCIT7TORWpNhi4js_fFmjZFdgAueRWUoEeKI0qbk8m-JCeZwk6lcEf_S-xjULqUZWndOVINkPnvc6PLAV9d3QG0MOWrevIsa9ncJXaOS-6ivrYGfK7eIWsvZ_Xh7AHoClooKlMHXYskFuQwX3boABRIW7oDTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6A4aFZLNiq3GbqYV7ZfCGAt0Qw_twKYcB7Smuh__edrgkKKWpOZiGPxwnPWozPIvqVa87RphOApjxOFGMln3Wdn2ud0gnbs75aAd9LnKXuYopNFtXCEeDAc5aRZZkD1KZ178wfHiwXGk9GQc12eu1Sg-b9Qthm3y8uH4qTZVx7Iew-ZLVoOEUaDkmPt2lrDYs0H7is0Uy8NfzA4uu-OF7F5a8-kzhAlevOLGJd2y98whgMk-TO8llTo6ksHQK-A8jpokECepil8PfjaGz9T-XIe6T-6D5JrdbX1p1doe4MW8yIBUnC4EKlsxu-KBl1T8xTHa9bZJdd9dTF50D7KFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=USE6bx5dHh5iMlZbmxVfuFmhW6egoPVvLOSAUllGCFGNP7rB6Qp465R33j2w31OL1YVhwa1f3IdprQaPloofQ2_6gKKCuNc6jaEPiM_hUhlU6-wSDG8nCmkr34x_R7024fJmzVaiCQaVO9QDY-najbF_L8OVk5jjvlExNXir1ixlmLTb1HZrhR77TXV5-u5JtyRQ1JuR9lzXjj9dZBYEBVE6kSy0ik9JfWCwaowrgZFbZBK_7cI2h9gtVKmqwA6TF1k87-0CrAzbIWFDTL42hlde6Q1wcQkvUklzfdDPWsyMJVSDAn1WcaUPtZsAzK8ox-YMKGgnDQsE-SQ9yAI79g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=USE6bx5dHh5iMlZbmxVfuFmhW6egoPVvLOSAUllGCFGNP7rB6Qp465R33j2w31OL1YVhwa1f3IdprQaPloofQ2_6gKKCuNc6jaEPiM_hUhlU6-wSDG8nCmkr34x_R7024fJmzVaiCQaVO9QDY-najbF_L8OVk5jjvlExNXir1ixlmLTb1HZrhR77TXV5-u5JtyRQ1JuR9lzXjj9dZBYEBVE6kSy0ik9JfWCwaowrgZFbZBK_7cI2h9gtVKmqwA6TF1k87-0CrAzbIWFDTL42hlde6Q1wcQkvUklzfdDPWsyMJVSDAn1WcaUPtZsAzK8ox-YMKGgnDQsE-SQ9yAI79g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=SMsyBSbNbK7g1PZDclstvzsbLYTTW9vqsGGjXhGPcBonhU43uD9S4MrvXY8voNLObGoMaZg0XUg3zNGGgMcQDBECbl7A-aCGlE-5FIJ8v3s4n3ZMYauPJCNK27jVD68PHMrEBtPPb5ofYshadYqJ82yPS4VlRn4GE8QfkkWIX9kUJiCBDokZxmOq_aylN81X_6xmf3yU_Lu1ImFY6H6esIYUo0dqu1HTLR8hETg9GBs2ntFFh32czioeui7MbMbz5HMUs_mm2H4yBF7FrZowm9_ORoUSpgQupuEG4XQJMTdJ1cC22G8GpxKUXoPvTXRONEXXDotLOhl-ZyQLRMl7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=SMsyBSbNbK7g1PZDclstvzsbLYTTW9vqsGGjXhGPcBonhU43uD9S4MrvXY8voNLObGoMaZg0XUg3zNGGgMcQDBECbl7A-aCGlE-5FIJ8v3s4n3ZMYauPJCNK27jVD68PHMrEBtPPb5ofYshadYqJ82yPS4VlRn4GE8QfkkWIX9kUJiCBDokZxmOq_aylN81X_6xmf3yU_Lu1ImFY6H6esIYUo0dqu1HTLR8hETg9GBs2ntFFh32czioeui7MbMbz5HMUs_mm2H4yBF7FrZowm9_ORoUSpgQupuEG4XQJMTdJ1cC22G8GpxKUXoPvTXRONEXXDotLOhl-ZyQLRMl7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k67EAoa2DdYRswzl8IgKAFi__R6RUMV8fr9RBmAg9FPZzmmWpd8soA4QNh_Txw5vilfguM6O2PvdHJncTBEOnPEFrFBgyekRrdUkCK3WUFQPLtnYS3-EIRCTUGSrce1GOKc8-iWYwkqgfLduZMK2FN20fCKQEbqtlIpmEICyPJ0tzpY7mByB-BCdk_LuPIT92ooUkMa9u4Fou2bUuD3sk3WH_NJmNNBBUY9R7vSOHLlKRVabZmJtN89Oj1LCtyCCNbhdLYAAlAXw8LNhrseEXCwIhx76IG6HWKzA4FKvJwYI7NppWorvyKLbIKnwVM4BSJREBEc-d97irfoeKWoZ-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=opt7Y9g5PCJBOTb-0u6y1Orho4WIi-AD95rRFIHWgrGs45SmGTYvAIfgqp7IXh9sK0moVHI3TxsY0ZURmUhDI789-Z4KxNWEq-KoDm9rBzUx_GWmypBOwJf1Bb9hvPkpDtqdEQ-vgCFEChP3vRMUiSM9ZCEwCQkKm4kD1axqU7Ai9TpwQCy0pTAYQxxelqiA64Njclioay_ICWbxmWWaTCh1ZwRTsHW_4UlebVZAHnAe-YXVMXjnp691ClNS4aRKnDH2c0Gv-DdANmG1YjyvX8xqHBiU9-P6KtSxHNp_mGcS_FAuy6iHF_GKGAGwVwb8EP7HVJtlRTwTqi-ID0b8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=opt7Y9g5PCJBOTb-0u6y1Orho4WIi-AD95rRFIHWgrGs45SmGTYvAIfgqp7IXh9sK0moVHI3TxsY0ZURmUhDI789-Z4KxNWEq-KoDm9rBzUx_GWmypBOwJf1Bb9hvPkpDtqdEQ-vgCFEChP3vRMUiSM9ZCEwCQkKm4kD1axqU7Ai9TpwQCy0pTAYQxxelqiA64Njclioay_ICWbxmWWaTCh1ZwRTsHW_4UlebVZAHnAe-YXVMXjnp691ClNS4aRKnDH2c0Gv-DdANmG1YjyvX8xqHBiU9-P6KtSxHNp_mGcS_FAuy6iHF_GKGAGwVwb8EP7HVJtlRTwTqi-ID0b8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfQ9zD1sSaJcOXSA9fGWG1GttGhaNKfl_-YsEPK7RcXoOEhx7KAqJt1xEcX_SyBd6pa6vWSKOeSocPJyL2s92otkNFQpo1oOtrvdtROsnN5D6ZYT-ADKZfAPnHTs9xQTRBmKW1SImGTM0DBmIyJygZuICA1Ag5nkkFx7Dpx3yhEBA7bnjVs6FvfRg7HFulRJZOB4D21EHnOhzrD1jRc3J3LznQ6CHOiXf4Lg8ZmBS5r1xB29_F8UsMDmzvLkuHGhjEQ_MXdmVWqY2WGR-SUyFgb64_4WeOcIjTh6UPJYmOANZwKAFDw0pt2OCf1J2mUkCHw2iWq85fNIHohg35_Vdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp8g4l5hXH7SHItbzu2Wbl0BAgTgFKXs1Yc0PSnZKj5olOZr_vzlg4jWOZTHipc7VihHz-qs656ae9WLTulKOOfqMkv0_Sub_jmKLtN6w-ZeXOUAD2Uuq-q3uLnjKWTK905N4sswrKi_eRGLaKKljD2-_4X1YhO6Hp8JqapuJcbggtQJ7KNsYr3f2uEYT90UY9nP4oy1QrLeBuOgJse-noDdniWG9tcdnQzrjgviqh_cl1XewF46hxRY_s443GZt6OLa0u1EOD4tRBCWHdoA-GoUaiSmLjYcxGBoSwPD_WnO1K2SwshNTp_D8q_DMPWUIkQM5ROW91nQf3Y04TK_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thUySEX57QF7apdH2T0UQt_UtNUnI8y0hGR-BiN9UOwzKBBtKNIt6-SM6K_BNh6u8vvQqAwdjtz3okysMLNTdI9ns0ePrUPuuPiP1FGxjYXtj85Ql5Y8OcqkVvLrK5wBFqZAOXxfuQGTDB4hXmd5HgU7J9EsbB650ApLI5WE-_RkbO_t7yU5WQo9euwcyaTeByrKS8c4hNprfsiW_iQaXqRVD3dFLwHw7xKXr9v4ETAc19jlaKCdUByconhsQOh4U9KMNxSXXVWqFDnv15ogU1kfyQFuVYfycRWJFDdE2vD4Iis3BKQ_hIY7PAdPuFljk6bX7EgRs4hoLNLXcF89mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTX0F_sAf5Nk0NfPIOOzLZFdArZmDKgH2u82Mu1cc40z22EmQDpQ1zqluMnfu3nfwVesWl99O6-xOG4HClNxxZ58qV-L-x8Uu5MhNAtey4fuAENIEmdkT72jsJmqhfutzWm9YEDOs0K6svM2mAkeM8mvTBO6sVqnZ-dlCX1jbmcyu4hgUCmTMuQaiHAdFX2jqcgvDjgg-fQsVnvykB4V32jDu5z3_yY1gSpBxa18b4G4wqTKxgYj4vjOstxt0XSoxOjaHzGYKQQwpdCwHfT-XlOPBTQ6D-ulyvhC-asizAIKvPyARKDASuGPHcVnQjEWkfKTaBCEh7uUxpX2UhLeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DA-pj-bNzxvUNlC0yYAX6MFtPu0Yew9vixmvEo6mvdbUWJju3E41lw3WBmfNpHGEk3ttvGuLmN8D89ILR2kIH5VbtdNojiSIUkf0qAWng6VH1iRaIjWAYYCWuynxmFKc65oA4VhxLs3grDIKqS4n4ewMh1fELmFhMQFIlULct9PAOoedsfwAykTZvwRlIcNYerKtsoD03FNHnJYGP535toeusKdIq5ztb7A5J4GHzaDKKN3R9G5WiK3g1cB4EsueYUDzJHt3fI0vHpK3r3KO8A8PWabDIfN7mghAVeZV1noZWFSJnxTPTfgxiEKjAu3pxZ8vyK2hGny_C7m6kcB6yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ao-qP5b9eEXrGzJRLnLjqqlJdid2rOrWJTbvCTG9HLKt2vOmspjRZa_V_3DTKAh_jiZ_33lmZ89ilnc6DJmX-KlKC1ScxAomUolYfHwwtwalbeNKS6LKMMRLnXjLXur9j4hNKEWhBEPMmb13sOFZTnrpKG_umyR31S9a7APQGpOBjtto_hrf-WGVKieeymigNMt63I29AwiZLQbJeMIZ2eqhOZBQvyW29L_AAGbkmyYbITzXpXI0ys3SqEouXVpuzmaoNTObG5TlHRN-z__cVuBrGqemjXx3wAAsiecS6CBYp_0C6ijF5afIWQVBfZfOe-0KZQnjnVOAg2cRIaFLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbZlAYMVlcjo7jwrElEtkUWCPZihClU180fPPQ2Qs-qhbsFM4VIgqW-4HJIEjJc6jGAWzX-05K_UlG70IKJ-ZoQnTy5XKv9R45ch8qEyDXmeY5rru1V5P1_iGN8O8F3CabEmzbnPMA16wKdegpGAXtkirTe9aJ0u7w7KTIcQwmLKvtzi30t51s52FQEOGQLIvZVuise0N38ge-rHOycDHvC8PCFQdB8KWBdlbyXkcE0wc3VTjzUgfSwq_crc9SLelGDOCgv2qyPcBCFVxIR6pqbqXVNmfxqIeQ56OQGp7-Mz7ggZBipEiU771O9tvUFG2T83p68LbJMXayS-AyMpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrYo_IqpffS_MntZ2eD0U-FiDo9ar6fYFv2OcJEWWmF_b6_xuYgRF7471-GQoh5MV3weppOINu_pinXLxwdm7GahrqIvZADxzKireFM231wNtlUG9caRQOdq-ZWeLzvahglhCvWjnXZTu2bw4kof5Md-ACKtqjWLuNcFNxakUTWGw2xpThlkImJFiKARDL08NRhGn4AXA07D4xlwK9rBa9PtmZHfMmFYfpWLHbfQXhOHHtHC0763IvpIL41nPLFUinO4dREdU-r9xZ_C6EfCHnxx555WOy3epUZX3n9wSWqLQpmjOrRuP7bkjXz9ozvlt-3pvrvF2AnfhE6-X7sp2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=h2f9_dFINKbX__9zjZWW19FkyiITvVHeZAkq2lh9PuY3iJMifX7XTsSmvAa0od7UsyPUEaqnl6VGiJFGN10Gf6KhrmYqPrk4FOud0tOTSYR_YhvsDrv8TBemrCwXcE399bsEiqGs3iyW3BsD874wylkNgt22I19jFSMGveBBMsps5WBR0wsc6Y6k_mJaS3_WsEkbfm8rafjuI3b1t5d2Mh6zueGsJrqW34tC-743Jqaf0MjAWbd0QRgsVPow6SG3Uw4J73QidZstjqkcYUAkWfuiPi4Is5L1DL87YNaZ0uD83thzm_1R3woTUhOuU2sY3HILcmpk15XHBvb27oSwhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=h2f9_dFINKbX__9zjZWW19FkyiITvVHeZAkq2lh9PuY3iJMifX7XTsSmvAa0od7UsyPUEaqnl6VGiJFGN10Gf6KhrmYqPrk4FOud0tOTSYR_YhvsDrv8TBemrCwXcE399bsEiqGs3iyW3BsD874wylkNgt22I19jFSMGveBBMsps5WBR0wsc6Y6k_mJaS3_WsEkbfm8rafjuI3b1t5d2Mh6zueGsJrqW34tC-743Jqaf0MjAWbd0QRgsVPow6SG3Uw4J73QidZstjqkcYUAkWfuiPi4Is5L1DL87YNaZ0uD83thzm_1R3woTUhOuU2sY3HILcmpk15XHBvb27oSwhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=aLi_SWadafDkc_L2Eld_fWFd9D29cXySinS4Jg7I-LtnkB3ib18XmIuyYptQQ7VGK27uXI5OESD9K6zu_lN0T3sv9j-KlwvCcqkHE8OIPFxbxHfp90EAyczevtVq0oFobnsptE9Df-c5Y9iiqunthXNPh4T63vdqrQgFg_jX9T14gM1Kk9GZV-J7817cJZD1QtJ9GYgnAMbj8rLMrvhf1Eei2q1QCGYIDLshDHENEMAMIe46L_ERB-adcaxI1UyYVouGkFoaV3i18gQcQZ6w2Zjnz4Va-SJwOqxYRw9ftYqSoudvhaaVtct-RlGXCLUunlu_eVW4GoCPctwucL_ajw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=aLi_SWadafDkc_L2Eld_fWFd9D29cXySinS4Jg7I-LtnkB3ib18XmIuyYptQQ7VGK27uXI5OESD9K6zu_lN0T3sv9j-KlwvCcqkHE8OIPFxbxHfp90EAyczevtVq0oFobnsptE9Df-c5Y9iiqunthXNPh4T63vdqrQgFg_jX9T14gM1Kk9GZV-J7817cJZD1QtJ9GYgnAMbj8rLMrvhf1Eei2q1QCGYIDLshDHENEMAMIe46L_ERB-adcaxI1UyYVouGkFoaV3i18gQcQZ6w2Zjnz4Va-SJwOqxYRw9ftYqSoudvhaaVtct-RlGXCLUunlu_eVW4GoCPctwucL_ajw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=nbTUEP45eekCJRIZPt7DZ1CrCuBKxKxtG-2CqxAYnNUWPv6Bg-j8DQ6n8P0XxwIEcHs-hWs2PLKT_l61wauBpSapFAGchzwVL_D9XSar_GufUyBThi1vutifDGoezYas1sQEFdIzJyX43iGqA0J_xcdo1GDdn2N0TQ9eXWD-kfNBuL9EHIlB1T5Y90EcPo5JwwtWdNC14QB3oqTUQ-R7K5bms_6IIb5FPO7e9IN9vhhEO9ZkYjTo233G93ahShi5JHpCgDRHwU3N6dG5zfN6iRvemU10A0bSNCqofNoNxqfeV8tuVNb6zfWTofppTVsi_8prZ5f5fZAZCVj4M-rK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=nbTUEP45eekCJRIZPt7DZ1CrCuBKxKxtG-2CqxAYnNUWPv6Bg-j8DQ6n8P0XxwIEcHs-hWs2PLKT_l61wauBpSapFAGchzwVL_D9XSar_GufUyBThi1vutifDGoezYas1sQEFdIzJyX43iGqA0J_xcdo1GDdn2N0TQ9eXWD-kfNBuL9EHIlB1T5Y90EcPo5JwwtWdNC14QB3oqTUQ-R7K5bms_6IIb5FPO7e9IN9vhhEO9ZkYjTo233G93ahShi5JHpCgDRHwU3N6dG5zfN6iRvemU10A0bSNCqofNoNxqfeV8tuVNb6zfWTofppTVsi_8prZ5f5fZAZCVj4M-rK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKXROffuUdqJy8GqJAcHO4RTUe0AqZVT18KdIQtYObbKilsplDGIqdljklTZZRB1FE8MBfB5qgOWhvHu18pBcvBA2J7KOv7I62aRt3j0BxLq_fFDIgky7sUQM1TjLq9h97cH4Cb3phL9VWlEkkp4KK3kSPZBBpW-GPXn8EW9ojLJTazvsh__OXQK2lCN7LO0TLZzLpGFL_3NkC0-yEQoj3VmN5xzRJUAE2sya-7ewc78yYs5dfO0OoHIzMWE1RXk5VvhaU5QJ4S8cqLR682eJrouMNHcdbx8eqBm4EAvMzAsEHJZv1fNc_SOUbTegHQdC5zJWGZRVDJqAUkxHhkg5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb7f_3qBkJz1hXb5W_q_90XsBcxiSKLEcTMfO28fb3aQdF6Y6ijT1kpN7gORom5ELbbNTJ735F2iHOf096UH1a3j62Lh_UZyinKCPBcTLyvZmk4EaMP1FlQ2lJOJ5WE8_O0Y-oZiukm7FEZxaGssIf7EXjOXDnhzxgUkxNkgNbvFrnKjRP2bbeXRQ9HQf-brs0cwJ1EWng8YVvwdbUZxw4qPNKvbnheg6__QNHD0wfbIQyzcrQ0dxwcktZgMUzZmcdeWFBfylkH41S4u3_hkjv6gQJiEnug0pV3a_rBL3a57Vh98eNHqUlEOmlUvOwqC3acAxhf686NhMvX1EdSr2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvzRqtxrs9znjgvFMFfgH7bjavwxiX6OtzACf6xyyN8qWXqy6ikRv_x5lfYkcH3gr_NPdgckpdiEtc2blMF9eL5rMWHZ_spO1ohs9JHkxQDaWfcIZALj3lCHel5krQEmL02zyH0xYIUKDseEYqvuvS8MOia3aXZlllywXhbUwGQNmRPjpN_qB4B6T5eJa6uum1GenONJ2gUP_gbUxE4koyF-8tI35djHY8viH2L-uAQGfDwmQdmg3VLg62PNQNErm8__VjVMe5aUqZdrnkEx9r6DqMQ_Pj6PuCT6X03ARCdtPHBQPthHTc_IYiODArZ6EdhflGLhxcrDjwNWACg17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgV7fecrYGsDrXcZzsLws4CXC0DocUBiywfPTPeuowliH45qxyAopi4nQsTHX_sWfH2HSuMlG4vIANwkgvISkQ9CvmIFxhVGpQYnRCP_sj2PXpWdNShUf9QgMHidr3vwxCffCNKGKlqgvsZh7Wl5rz9xqIl5mmeq5oUCMx6TzAuz0-thQWtNqSy9Fvm4fRAAvrXNKPrtJY8CWFj8ywjkKEX-XebDOTDnfYBAohzkRoLbL2x1aojVKq_xRnQBlIBAjlM0G1-rG5qBLWyiBL7L3CZM2vaAzy-_FxGh0cU3ylFxPfGB3oJrTK9lwVXOIuXa4szvyMSuv4Z7CRlqUMqnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=LplHKmWX0AUuV8k-R9sbUraR66EHSloSvc3L0yHGpNQQzef0RT0fqbUNrlFijFWL7Y2u3girg3OgtjKwLVPLd9-tqlaofUIFZTRIj38kO8vQV7aolSVigmGmOeb1fSVQarCsNs3xMmL-aFoTUiJgAJMGtan89oB7QehmXFY6WYIbo4wjMcUu8BbDBQjJDE37-1cszrVJ3nNgnYi3CDmqcN9dHsBsDOcYl9FMnui64nY-Mo-nHDhvDDMg0GByirPZ7FRp8Q3ivR6KZrQIHZmb7zqqldDOo31Inu4PKrLzJSC5BvBLAHYHCoC9g_Fy2AhDeCJbRDiO8o18Y5bVdFsYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=LplHKmWX0AUuV8k-R9sbUraR66EHSloSvc3L0yHGpNQQzef0RT0fqbUNrlFijFWL7Y2u3girg3OgtjKwLVPLd9-tqlaofUIFZTRIj38kO8vQV7aolSVigmGmOeb1fSVQarCsNs3xMmL-aFoTUiJgAJMGtan89oB7QehmXFY6WYIbo4wjMcUu8BbDBQjJDE37-1cszrVJ3nNgnYi3CDmqcN9dHsBsDOcYl9FMnui64nY-Mo-nHDhvDDMg0GByirPZ7FRp8Q3ivR6KZrQIHZmb7zqqldDOo31Inu4PKrLzJSC5BvBLAHYHCoC9g_Fy2AhDeCJbRDiO8o18Y5bVdFsYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Aq8tTXDx79LuE8r-7RikbEz9XQq8gNkZSe7N7h0i5oCJad30_U_G6LOs3Qme_qa9C08Rz7X_bwBIAAE462qqxIByuOa-8wXr9-ryCh-bw3bfjng8cKgQFEV61Jq711DL26qLK_np4J4Nm9VqcgaQZ4UebJabZxzFwWpeohfZVboDS5P7D1Eo8NSz_tpIMoLnBD0XPh8TxEmIVBhJOW5qHy35rE__jNs7FNKRMVx7l8p0zSY5vGOgGl5k1snUr8px5BxYFMLCcckdIxoZTVEf0lCjwAfRN-Fj4_cidJ1c7mPwmt9HXftVLhpO0ZYGLoA9ivdl_LNav_f31x7rF4JQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Aq8tTXDx79LuE8r-7RikbEz9XQq8gNkZSe7N7h0i5oCJad30_U_G6LOs3Qme_qa9C08Rz7X_bwBIAAE462qqxIByuOa-8wXr9-ryCh-bw3bfjng8cKgQFEV61Jq711DL26qLK_np4J4Nm9VqcgaQZ4UebJabZxzFwWpeohfZVboDS5P7D1Eo8NSz_tpIMoLnBD0XPh8TxEmIVBhJOW5qHy35rE__jNs7FNKRMVx7l8p0zSY5vGOgGl5k1snUr8px5BxYFMLCcckdIxoZTVEf0lCjwAfRN-Fj4_cidJ1c7mPwmt9HXftVLhpO0ZYGLoA9ivdl_LNav_f31x7rF4JQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcvQpyGQxudj1fF6TYVo2vCGCXSlVW5ReNFYJDtOIKMcipKyktn0DwTMEkNKZLN9qx0GMU32sJEUu7sdFFhfNFLxjsaj5vFDxsivzjqqSDs4A42ckb7RTXm84Nssdoc5EYbPzRAkkfw0ZO2OYBT2nzuaxWY5JRsmRbcr2WKzxRBntApu6YlG2qeUzGBe1tljuZbNdVyQWk_lhiqiRu8L6w9nL8nyHHeCLDYNIbMNZ9iI-cj-zp3QpGN9vZVoQmMPCiJ0vFRjHc7u8Kp2aHVH--EJsV2dMfj3W3Vi2WgYgrRAS-zj8n7OeYaWIPCChiwGswYOYfzB00me-zDfCJ9yrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-EaLRIMbbNdWnMpT1kh32pYJFYvRhO3JHcLkwuF36_7iMyP9rIoBKAhb23qhQKRj5vtCwfkkpxXS4BUWWBESLY3S-JgG9TCIJbdVENbjwo46tTeJIVrpIBPE2d8a6zk4W7yTMMmVJnqmSGEFjFRT7RR1O7X5M00mYm8cREEfSbPGBUYb9wow5M_Y6-rsZJqwZeJ57fo5UzmOM1seTfhd1iSAvI2FHyCvy4d7-4C4h4oHHWPEd92ME7fCnSls3jCdrGm8Z3RRCmN-CC9XpABwFmQPYBUlRCTp2IamnCmjIxaY8pp0-2HggaSHxz4mc8ocMCLiDYEf4EiNxIolZCBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRcjus6D_bEsMdO_JC5c-dnst0oFlSR-F2ZdSPdgvy6nj4l3QLweAo9D2F6tqtb6StfPXCpXGad5QTieSMr_jOOaD4ydE2IsoAfUSGUkCXvI2xIcTLbydoke2uUemLO7WdMdL0RayyRp5pMvRP67CkbnSkqGRDg4929UBFDgj3UvpgnJ6_FPnn-_-9eouQURxRT5ua0FCXWJ8j6nNDEGr7IcnyruyswXLABFgak6VAFrMtL79osq--Y_yE1glEFM-c5ra2PdEHPAZ0EX6h2IGCF5FtBJDBMwWubX1RzoUGS3pBv6PLzhQOcyS7z-eBX1hNfV3qcM_zTEafYgWk2TXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3Voz5bjL1ELf4yjstH3XozXfp5ba5OJ6VvWt2Mn7MKwEX6fjI0O2ZIUuKij8CT67a0eeJMuoY73jWo_wZXNT7du-2Uw50arf6Rl4kb6CT_GwcJN6FAhtfw9wDFJsDHCcCfcUyvAMx595vWVtExN08QX2Alk8nAGMABQs7FMWBGzNK-IIJd8HfBQ_ZJsSVPpQ_szkX760kXdEgQN-aDYd8-UEcQ_KAEBWUueURWghCA3i3_0TvsRPPExxrYnwjSvlTPNR2VfYJvf6S7KaoxVQNQBMRqp4omt8wWtkJcyUHt12z-SSURiFhhX0f4TObQMdwU4fhr1OvEESjlfjUrLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErR5RqejDvlgnO7JtIMmbrfn2KKTYEGcQBjcwro9IXwZK0hPkdgx6yoQJilWlD9edMdUe7xldshiyAigqRBaig7JJqMIvQl_PVNbwJI_M2uB5Uo-U-Oa6jE6Po51GT5vISR3LSJFMPhmEPCeAAVChQOzMChJV4ZcsDmIFgtmmvcaSvtIWm7LyJ91DAL1IviZu_im3ZOG1HJNXBLhN5SAj3RT5V_TV1XKkNCR5WDfjfL1I9516Mg_60JdRd8fuIM8mP66dIllPmkVulr14eJ9VmZrZLnkNuF-nyF96VHyBbk8TLQxg_TFW9unf69q6_iFNPLOPq8TBG_h9WYF0roaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEvkRnZQDL8pmX40SUku8KTy_e2g2RLBBxiqmr4z3TJGEu_4HPE_1LDmkNhJyYm3fNX5Ong7bt2AHb_JXHtQXNmHDZPuPMcesKd__3MXsCN77zLuqXJgpFmzZBTwg2cT97_Jrj9lwcwNea_rzGV6JdEkWUKMfdfYMZ9qeI4__jfCbYXYck0CctT6EJYG60gPuuH9D9IMq3oF-W1WJ4r98nbjBy41XfD7wIqaQS9j5k3CIqQCNimdtldHhnhKt0WKCrPBjPUTQKXNfGMhfgQrR3NdJtqt7SqXR6okki_XTZNXO-qh8KqvZp9eEzzTzCtjrcY02NFNZ3NqnYKrXPNtDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ER_TMG5AULWVLWE-MGJ80WVRiYjoyMMMQnmQPVYhUMkKLAaSArayE2H-rCmx_TCFo_MaGe4s-IA231n05Ip061R_WJCkjPqIQXA7EzQScgtc_jieKnoHAviBkaiianXczKA4_38r5-Ly60Hpb91dlCjqlKc4N4vYdGk5NwSfeWyGFMLktMth65jr9va-X6vGhsXG5Q_SlooQQSfQr3Hd7j_0wIqZMQLeMMzPFPZxuSu_u44cibvosgC8uoJmasxUoaC_o5W8ZQh5aiBU7RXRf30N7cM2tvI9IkisDTQVNkicCeIl1LhcjiFKR-vZC1_2yQrXZ85hnqysb4JT4x3hHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdSAa5gmfvta7_zrKyqor2AhD0sKC5UGdeQ4I1-3HcI3F0kPGnsLOHGeu3nzJlnQzINvG_FgmZ5xCg4Xa0fYSzP0zYakvkFOUIZPdXwiU3UyC9k87oAI8FEE7p17SdoA4FRbcmIbap_sPbfT9Sdf17d20idxoFOpJOM-XRfuX_dX8k5Afhmy40vU-ee_CVquTsMqs9Osk9aq2CHDSg_03_jv2-3eJGI3mkr11BxsdJvflyj1NSBDa_fm_4HiI7s6JrBVNnjbqeQwD2dOep5YmLnLJsidawyJhatoiTIvrOl2CQlG6QyNFlJbpK1iynncFrVSL0aqCfFwsK5mWx3WSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=URoqnvyUbi6qjTbevRDWy3wEHKkc9LaiZf9C6btSJMq79VM2FO2-18vBN3Y2wrkFAsQULEnPimFl86YHiwqIroKzEjZu2CYQ4SX1-67xMPdlQIQ-eJ8byZ7GWckK_9ALh7aK-Le_aNy5GrpEG8Lj_n6kdDL3Yd5Z04a1otIzKIWKW--g_88mnWdwcIRAqGHxnfP1orBNAVupT3WP3v3BSGpbkEby36YXcG-J7gEt1S9AsfMzWSacYVrTumII8yOxV2iqn1oxbqLPDBziyFJrRhWt3jEM3mUgC-W_puAdm5sOIoxuLpaD36a3JIU82CHi9tpYNiwYWSsjVIxUfnec0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=URoqnvyUbi6qjTbevRDWy3wEHKkc9LaiZf9C6btSJMq79VM2FO2-18vBN3Y2wrkFAsQULEnPimFl86YHiwqIroKzEjZu2CYQ4SX1-67xMPdlQIQ-eJ8byZ7GWckK_9ALh7aK-Le_aNy5GrpEG8Lj_n6kdDL3Yd5Z04a1otIzKIWKW--g_88mnWdwcIRAqGHxnfP1orBNAVupT3WP3v3BSGpbkEby36YXcG-J7gEt1S9AsfMzWSacYVrTumII8yOxV2iqn1oxbqLPDBziyFJrRhWt3jEM3mUgC-W_puAdm5sOIoxuLpaD36a3JIU82CHi9tpYNiwYWSsjVIxUfnec0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=fRc1F9fTDszovdine7XOrGF0IF-onxKz-cv3kaXcBhnLbkOIPb-FkX9c6ijNF0G--_sgJLU1eQN3BWq_mXGbreX-UTZjoe8ci7k65P4_r16L2IUbNqPcZj6uCWo3FcDWGF5rwV3XUi_1FvYBc_sziZo-oqpRbwoCvSyXom_o479_ig8Y9sAS29X_hv44bkX0I7Bwfb0wrIhSyEGZSXfFLS46_hJcUlthrav8VUfaLBcbFxS8atWdg2DlpGDACA9cxDWH6bDtVskPBAPPtxPBgJ62VE9hY5BN8Ou1B9fa-coQn6n1Pr4GtifUmi44uOETEHFtcaHDHzuF0YOWyVMWLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=fRc1F9fTDszovdine7XOrGF0IF-onxKz-cv3kaXcBhnLbkOIPb-FkX9c6ijNF0G--_sgJLU1eQN3BWq_mXGbreX-UTZjoe8ci7k65P4_r16L2IUbNqPcZj6uCWo3FcDWGF5rwV3XUi_1FvYBc_sziZo-oqpRbwoCvSyXom_o479_ig8Y9sAS29X_hv44bkX0I7Bwfb0wrIhSyEGZSXfFLS46_hJcUlthrav8VUfaLBcbFxS8atWdg2DlpGDACA9cxDWH6bDtVskPBAPPtxPBgJ62VE9hY5BN8Ou1B9fa-coQn6n1Pr4GtifUmi44uOETEHFtcaHDHzuF0YOWyVMWLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
