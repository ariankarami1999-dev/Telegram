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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 17:57:44</div>
<hr>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn4rctaDdCBmGggT9sFib7X1aYnGvMuyw-58TkfHSN3H0qxf03rRMgsCgptYbw1uAGnpmnk-1cfVMcXkLKOB7eagWV3Cu5GnP4Igwpa_LmkVn9-SSy6kykNn9RmdyAf3NUdMqrjKEKZyxQArH2IY41UM8v4L7mw5p01Y1FmBm4PBAGi2gj3VC8YnC0F_zJYEiqN2MBFPO565xCuopu_GV19NT65jW_Bnr8TR6x9Nb0jEoZj3Ra7Q4yV0of-r8oHK4mHtYd_VWu2y4ZF8oPlzVidaXPA6VSDn8pUDdVndSKYj0pmLWVNJC95Ns3BImZ4mrYvzaQ6FwV6NEnCu0h0Brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-t4WT33XzNrlUV5DtzjTHNuWzOwx_lTOgpD2L5QMw-Wxsb3gj3DjWQXKXsPgF0D20YKN7krXzqBcDAIPpibXVtZuwyReefdzWobhDNr3OP8B5OTby4G4GvZ_8Pp84uxCHXUYjemX2OER3bJd6eMHtqcNX5jio6Q7CCyFfc0ZYZSpHwV9McnAi0JP4Rgx05ZXqEj4N9qBMB7tKcrcEMIGLU0XOOU_gLDVsb8hUTChnHzaH0u3-6alcFbTMOKO3JoO7AZkCmTtCKZ84BtUrWjLBfvyN1CP5UjxVDK2KrlquVUMS8VI97k4p3gRqZVyVAIepzm9V4OmMeq7XFV6ffWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRcepXoxx_9gwFjZdTfHPXcsUjHHg_L1Ce_LnoiOeRDWdmLT07fcmHPLEho_-eWN2CxUuLstnEAgAjO4PKhRATOYjZ_YjAN8yRaY51VP6VP7O1YMg7wSHXiYA5Wtr5HJlbqDmwFEvMPI9LIBl3tPWdhnlHve0JAPXLGSvu83sr488GJwilbD0d16LmQ-tNxko8aQwYH_V7vy6td3l4J0iTYzleInsbEP4izVLO9p6d9Pns4lCZNGLCDcd3uZbVMm4ZkI4CoxbUMG_JoHwjp1bsojskGbjqOQc_y2n419-6B2ssY5tvZEGxOG0DmMF8L2OVLgY6dL3A4aIMRbcPAxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPQwDsb8e5BbH1hHBk83pdT9vAG1x79B7h0LBynwZ8NPcttZT5t3RZopf3hiWBBIv7zpMES_kv-3AWxgm-ma703Uu2nAx4--3HQ5b5KK8QyprJYZ9Ft5P5S97-VAKMwUo-QsunXTOQ7KcmsjlmuzbaVXvSL1sfB4EfGoOvbt6jf_AiZTzFWg1_G0QFq4aDz7AkSXX1ynXd6PIOxsZVA2dbUQrB4xdLPIEoldADTVvkmYTF9u6DhTZmrAR6os34aoVIF3XBtbtST4oRCo3oUSJlUc00N81jLobAJ0zjLd2Nj7V9Xw9yrxeItMrKQxrMm4ynMaC8bhmRAJY5cnOCQO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyPPFuosB7B7NFMW16cRyhpD1360JavBG1BGsedE7lpypkZRH_ZFvDygBxjP3004LCec-rW2D4tSGiZlt4AZPh4oLTAaDtDotz6us-ts3TVg0GKzWD88fJ6Cvr-2LZmQI6TSRpnXKh29pk0rjKkNXuo6tECw_pTr1xbjadXymp9R0Rqb0re-_mMHA1FGWxR-ut7-Y8pc4qDQUhHQZ1AfZBWlhKzNBgPKY2VTqMcMUI0_uF9zpL7svUdL6Gfn9988RfR3Vc-hKOhPW1nl4xVaoVKZ0wZrXL6zEJb02r5eqF8apy6bTWxld5hAhypgb5P5ISYWeBoLeEIl8t63iISMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXAg4d9m3z2fildsIFEeiF_hxvaCXPfhNuCe1kpgf1CtsIur_c-10yLssnoGsAllr2txX8Nib4gl_bmXHLlYsoE8DRgsrRPiOi5bQYoL93M_dD0Y55vS8FEPD1owpetQ_0CjpnrOS0mQYM3BQ8CxxuzZ1hbZWo2lLCeJgirtWh-xTdJa2CmkLOHWI4PDleBXQzSy5k1YrQua53DMGPzzPoKsiXdubji8yv5sGS7Ji5gqpPYEb2E-p6oeJYhy3Lt61pNJkUaoWiD59zolz3i0JNUAVrR2dnWuuz1Gcab5haxgivDgnbky6PqOoPmHg3_kDRvh3CaK3TAOvMDanjGdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1734ESwsqR2o5BfnS3oqPFzI_AM7D9UotvMeaNmmjDKK4H04dH8YztKNgBT-0Q5MarEpOhBSYlxJuZmatt1OlKfKrrswm7XGShks5gbHiaga3G41Pmsh3X1EQgBGwVwxJuEBniWmEWfJlEwnIY2CrnbHdERtBwPhhhhVSMXJUxZc7yDMwlGhkrwvsCwJuK1Zl5xUtZiuCDsJ75LbVvu1Nri55Wy13HJU9R0t9NNMMyPB7z5oCbKMWbsPuvPufs8fI7f4TSaPPhE7mAhzFlIxR4hiQoHXnj57gMwZ0MVYytEufX5TrBo1OkVLlzF6-eXBq42lL5hqHIHf61zuJUAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQg9UrjkJUsJkot8EOtdanfFoBF-KAJOxXJX1hUv-2uWDUIeNIQaKdskVhAraneTbP7JL0EMcSbvVGtP8Y8WMkXgepV-I22IXgSLxd3ptcfZ0XIE6Cu_Xk7KfLxipqgL-zZRZd5s6FYoTS2sUOt8t_ghSY6bRkg3HfTtKIqHcCWtKPegkzEfRe3vBUq8n13QsGFzZ1m1dpTCz24jflgdowjSPtiz3s23AxOEcBHKBwd8MZl2jOz6by0wIDtMT2d1io3Ueuo8uhXS9jsfvxuWuhMHdIc-xh3uEOP_DmYeeow6Dc6uMHzVclCFPKoBWB9NCCWq8Ito7-_5GLypEXGFgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=h-2Khub8dwuLU0mtdtQybAEMgMcGadUHctvcwaA00FjjAlN1tPXDzsbV2LSDlBZFqajGnJkH0jkAJi4ZvHOt_X8fCM_KLQUUPHCe5kNylJAwvBXfQLHjzz_nuPXcKzYRos9k_7ZzU29lZjE_jnGqIpVSMN6vYApZz0u4--2Qmxr6HH8O4ejUfsLiBWC5Rhw_Fnqu0DxPE7-S-PFrSRw2pY0GAeK8GA4nfbII8B8thjmv5HEhIxmZeBvh-Ydv5tGuw8jZiSBJXe5DmkhfvkfFMni4qNva3-dTgFiRXTjzg1vK0KsLXg8DVY8HMIc8PLOKTri__U7Rt1Jaq6Y5Gi8LpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=h-2Khub8dwuLU0mtdtQybAEMgMcGadUHctvcwaA00FjjAlN1tPXDzsbV2LSDlBZFqajGnJkH0jkAJi4ZvHOt_X8fCM_KLQUUPHCe5kNylJAwvBXfQLHjzz_nuPXcKzYRos9k_7ZzU29lZjE_jnGqIpVSMN6vYApZz0u4--2Qmxr6HH8O4ejUfsLiBWC5Rhw_Fnqu0DxPE7-S-PFrSRw2pY0GAeK8GA4nfbII8B8thjmv5HEhIxmZeBvh-Ydv5tGuw8jZiSBJXe5DmkhfvkfFMni4qNva3-dTgFiRXTjzg1vK0KsLXg8DVY8HMIc8PLOKTri__U7Rt1Jaq6Y5Gi8LpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=Lr1ROb7msXrQXpyntWm4JY8JNEtdgFfBrRdW6ij7WLcxpalWZNxxnenV_okpWVpVuwcrUdn6yjy1OBVyhWv1BZAY9hqxZBAo1AlE6VxLUbL4g51r8qrSF5fGTv5VoRhHHFtvC4PoKyITg_7CjTGWUEKK1zocrShIvF78i8Bk45lWb8BuQ6zGcdr8drbAlpeY8exftXYkofH2aURb24Tmpw1Heb8pyLh25IzwIZlBYStVWjvqR5i5CjuNgFK0nCZrcxdS0k-IU3eAeozTW2t_8O3r0lNg5vQaIpBr0aBLiV2Tzu8jCAq1VZTTaIBODOPH3CKYTdJza0WonKbauktR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=Lr1ROb7msXrQXpyntWm4JY8JNEtdgFfBrRdW6ij7WLcxpalWZNxxnenV_okpWVpVuwcrUdn6yjy1OBVyhWv1BZAY9hqxZBAo1AlE6VxLUbL4g51r8qrSF5fGTv5VoRhHHFtvC4PoKyITg_7CjTGWUEKK1zocrShIvF78i8Bk45lWb8BuQ6zGcdr8drbAlpeY8exftXYkofH2aURb24Tmpw1Heb8pyLh25IzwIZlBYStVWjvqR5i5CjuNgFK0nCZrcxdS0k-IU3eAeozTW2t_8O3r0lNg5vQaIpBr0aBLiV2Tzu8jCAq1VZTTaIBODOPH3CKYTdJza0WonKbauktR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj2QsYtbUQ9aJM0MvD0I80tY2sDysRMnJTu4SbZEamgZMYNtvWHscRZL5EN70lN2WrfUeM5Lrh0Xd1ufT2YmTh1C_cfMnVab0pms4x8aXa_mZp3iwEoMDtpXRdmdLyysNvPx7QhOOwCen_xxIXQwQ2t5X3Ho3_xy8jnIvH3rhW9e4YwoZPzlegAjRkK-sZ5DnUC4obeDBX_7-vUh8HHFx0zIaDdsygOAYZftpsRUI80UR-zye3-WDGVr2iiqCq0VhzB3LXNtV72EcN3UfdDe_Lw5isY7Th87ZFkvf0tv0FwrL35SZYWvGUc9F382BskIKb8JiitptAxEFmgGJWcdhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfML3hegPDXBGIPcYUwmki9YgBWlR_KjgKRCt1XQ-LA5LJ545thHr59DC3l-wTumEs_vROqc9Xj6Stmfbtog9tNteIpsXfYa_ju8HRFBLxEZHJOezQV3ZNlTJgRlShBH8C8Z2iyfsGDDy6dttNEr5HHEAECKV2-G2uFgiI0ct9O9CeFURCTaM9Q-OzAOa5V73OAJ9NmNkCv1rUHVwdEn5lius7oNrV0xGTwvu8It7SsvbZGID8ZF_OfS7RMhY8mQJcx_Bij9e9pl-4L-1h_N8tWZ6oaSIGeGhOCSGjSEQd9DRsxCCR9-_gu35PaaW8mLj-YGEsFOQsTK8_lcZdECSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=XG31I6HQ8bh5x4eyC6tDbHp_ZDw0Jba0ofDhNKNocD7Mpc3RtaiK0HO-l0ez9KBbjV2sgGGPD3GZ8IxwYlA6dN3RVJ0pMbAcSbyglEVi1vnJjeF0qXwNf7GpuWmMtxxZYfyKJkPd2kzHvbdwlepKuE8ZflQ3DLMUDSJ_aRawd_7sCfCQGdwHfcA-cpRKxsj33K-ieU5IdnGEb-lSu35Kcm__wZW_Jn1CiGu1Tm4ejC5I_R94iwfYQxb1MPME25i4mrwZv7lxHluiAymgUyR3WGUKtBWmYAD8VJ_hBfh2lXJ_HYK8E08ikY328R0UA8SN_iz6-abn_VQ3fGKuROWgYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=XG31I6HQ8bh5x4eyC6tDbHp_ZDw0Jba0ofDhNKNocD7Mpc3RtaiK0HO-l0ez9KBbjV2sgGGPD3GZ8IxwYlA6dN3RVJ0pMbAcSbyglEVi1vnJjeF0qXwNf7GpuWmMtxxZYfyKJkPd2kzHvbdwlepKuE8ZflQ3DLMUDSJ_aRawd_7sCfCQGdwHfcA-cpRKxsj33K-ieU5IdnGEb-lSu35Kcm__wZW_Jn1CiGu1Tm4ejC5I_R94iwfYQxb1MPME25i4mrwZv7lxHluiAymgUyR3WGUKtBWmYAD8VJ_hBfh2lXJ_HYK8E08ikY328R0UA8SN_iz6-abn_VQ3fGKuROWgYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=FOxCAp4QUvn5OVfYy5bG3wvD2GJC_gOpw1bgOwGnYDjEya1VBvD_pxfvFFs0LEbBI-wOz2eIEPCgtR9uh3gW88fxsWBr5lHZTNqG7d62lO8E8ZZV1FSSjNkZvceYOSYVBhPw7pQTuxWG7dEODaknLWkRK4SBKdIPOZYk3pTqq7jQsr7KsaBjXu33mesIlXbjdLhtJNWAcDUji5xtlr3zzuJ6Gyamt4BUEiU1UzRHfEaJIkwXf65PelmkgDezbJTzImQls2HFJhZKE40hyDQ3jDf4C2rZYYfvuucbJ2t_pUFwglZUCf3ecvQJBO8PuQDGbWkGHNf5iFZnm72mcdPQcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=FOxCAp4QUvn5OVfYy5bG3wvD2GJC_gOpw1bgOwGnYDjEya1VBvD_pxfvFFs0LEbBI-wOz2eIEPCgtR9uh3gW88fxsWBr5lHZTNqG7d62lO8E8ZZV1FSSjNkZvceYOSYVBhPw7pQTuxWG7dEODaknLWkRK4SBKdIPOZYk3pTqq7jQsr7KsaBjXu33mesIlXbjdLhtJNWAcDUji5xtlr3zzuJ6Gyamt4BUEiU1UzRHfEaJIkwXf65PelmkgDezbJTzImQls2HFJhZKE40hyDQ3jDf4C2rZYYfvuucbJ2t_pUFwglZUCf3ecvQJBO8PuQDGbWkGHNf5iFZnm72mcdPQcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=vSSqPKNJBbidolYc5yKAZpm_O4--nfuo1pl47Hxojlvz1Nr4LlecjGMi4pz2EmyaR5dpGUWuRGj8flG42hHwpZMZpOfTo94VHtNAGIcX-0pYOS6FfkBfHygg2UmP3927ZvSEriZbD0vCymWeOSAlPT6FOe_QzaaWIKiwVC_kkhAFaP6ffAXr7qtnwjg-fNntjWclVT0Ty7RkM1yxYMCzBDBPNoU00TeuqOM7Jx0zg4I3q1pw65BmDp2wpLK6XLsmDgCyb8JF_eeBuLsLyIq06EyWKWFmyrVUYYuaKe6zveGsT6cV_xAp1U3bPQ4c0ulGT7a_2otbnGF5AiZtmpHibg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=vSSqPKNJBbidolYc5yKAZpm_O4--nfuo1pl47Hxojlvz1Nr4LlecjGMi4pz2EmyaR5dpGUWuRGj8flG42hHwpZMZpOfTo94VHtNAGIcX-0pYOS6FfkBfHygg2UmP3927ZvSEriZbD0vCymWeOSAlPT6FOe_QzaaWIKiwVC_kkhAFaP6ffAXr7qtnwjg-fNntjWclVT0Ty7RkM1yxYMCzBDBPNoU00TeuqOM7Jx0zg4I3q1pw65BmDp2wpLK6XLsmDgCyb8JF_eeBuLsLyIq06EyWKWFmyrVUYYuaKe6zveGsT6cV_xAp1U3bPQ4c0ulGT7a_2otbnGF5AiZtmpHibg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=K49xgaxNo9G3O-eIAjKgiN-khLjme9GTu8HFrznTs3JoUFuWf1mlAeEVDIMGDWPxptkkNXMqsimj3u00PB_4qrF9hTSAcs8Ds_ER7Kee5Gq7NL4EcVzD6FUsJTPGV8_aYABd0ZtF9TaA2Ixk3sMkYGASmU4RJvMso6cLfH90Fp8D4cfHMHxrG39hnrQScvfR3ZcPHjWS8BpHwPLKPJkLuk0BORVtX22idBsSRrtSal1Lnh4doxQbp_d-T1RaysTvqH0MgYJc7i6TyO-BMHzy2O2G4oblZSaJttI-XLNsyY7dzn70dGYXvWbV0OF6Gu_ku2vlqphgo8iG5nYum7hzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=K49xgaxNo9G3O-eIAjKgiN-khLjme9GTu8HFrznTs3JoUFuWf1mlAeEVDIMGDWPxptkkNXMqsimj3u00PB_4qrF9hTSAcs8Ds_ER7Kee5Gq7NL4EcVzD6FUsJTPGV8_aYABd0ZtF9TaA2Ixk3sMkYGASmU4RJvMso6cLfH90Fp8D4cfHMHxrG39hnrQScvfR3ZcPHjWS8BpHwPLKPJkLuk0BORVtX22idBsSRrtSal1Lnh4doxQbp_d-T1RaysTvqH0MgYJc7i6TyO-BMHzy2O2G4oblZSaJttI-XLNsyY7dzn70dGYXvWbV0OF6Gu_ku2vlqphgo8iG5nYum7hzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4jyXYvcJqNK8PADK1MnKhn4Cxhc0R8d2nPgK-8iVAv7c3VVeTWIW-eeH5ENjLmtR1YcXyl4zC0vEmU9j62X7hDBNXkUHsNtvU2Qq4R79tvLMhUt3zA323HwdFsTtyPnbNOcEvtHLmh0UztJsvF9jG9Sg7ju85Cmq3Czt0aU0hSkRgKN8hqGi32YKf4yWkmv9L3T8iQ7C6tXZJYhHy33XNiX7AnWIKGT_9whrf-tc2dwsmvnUAL3tCIy4_YoT_PkUCpB22lq4HqxJtrclI0qomBGBvTb26ReyuSpnyEzz_mmfN7kLW7m5uI6_ejFu0tTVykPDmM4OvHAfdt_P-zssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGTP0uKpqe4879YvVyaLAgIr_Fy94aipD_D1O7ibLIN0tgxyHaSBBqQfQhR-De8hmAbSVE7ygSmmRG9WCUVfDwDNRoF8zSsQHAvTjVRWoM_o6tm5PovzZtX3cn8PssXBH5le2C505twOUyoreirFeJT67iFZAUVRphK3uWU_xpQg_UL07Urzn7pislHZhG8ZIWLo02Rq01adNg5G8zdHK3GTKaKRr3Twj6dzX0Sisg0CBDmWV6D6AVzInpIokUMFK4E0cE4NCz2KVZCBDpKvZaqXiLkQ1zgdzuVqOGu6fjiIRe1F6WY8PxSwe-Mf018raVCsC8sdkpGP73OI1UofvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUC-DxpfCh5duXjBHxkc3QmvsWUptzytQLDFlSHsm-xh1wF24y4m6q_QJMdvQ1GqgNggcfKBipnZRStPiBbX9jGWzpczOgyvgCfbf2DyboAwT3VA9stIrSKE0UF7Me8xG9Yk7uoFA6nsD69ljGCgg91kz0ROJuCA3_daCFZAvvoKjr2XTUEB4CnLvzVAnPU4Do6-oaHSDo0Z2u1eU46i4Tz6t4a1SiGrAoU1VFYYTEA023G2Vw0HIC1ZpjKY2-RNnkObg9eaeQuWRj4CVwPKWxB_5C7nRu27uU2MWTUMz2zB8534h2_a2nRyHCWCJXcRf-XrwP6CqXl74-uXazilzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STAlH2J4tFMp7bQj4vHzbOilkVhQRuvTtg2vfvl90KuuZJxlFQDSSuB3uQpaY_nBkAQEH3tJ6TNSqHpZOyl7BNshEA9JyKwAu_jG7dRySohW5QfGm_413JSeXnjAJHyGKE2csyhPUdAHvhCnzPO5j0uxtYrkrFoC0_gDPw0EkFj7XJZHI2nbjrIIFjlpWKn77d4l2WYoQHqsJ7puNy092LlF8LxoYRg3ZvsdFDPZtGcYU3K7uh9HEwdP22T25Fx15ABTkFUSfdVLa1T-m3-o-xy1qTp2Yvv9CPm6YnNgsiTck0bHFbyCu8M3I82SpHiz5D0OvqM-NHd7LG3fQloG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6Di4FcYDNqzhQ5s3Sez5elxPT7c-zx76SXeJ11Sl4o6pWSbyqaSJI5609P3lUwxjsZ5xQlIhxSpUQbbLOdg7DJoqH-O09NxRZ55HJLC9H9VgsHsXZfN_ilTXpXMM8OnZo_QxxuwMTbQRxRpdY4wqCR9snO3g2ZA1eELKwYaFH-efYa-XpSCq5oza_tJNZLv1fp0f0lVTIAXsMOAmELMcmyGygmYrTdoGoovMTGtFTLLXnwU7mRKKbBv9XcLtGbkjqD-rQQjLPVBO4QF-zLMxco8rV_WF0b4ZzJGVw6gcof7aXVFq6mTK9IAy5GY265oSgmIfsADcIECZh7YRGpgrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPIcqc4ECQ3OC4HqWVBDV2XmQrTD9We1WMqWrIt6X6q8-gxDrrSQOfWHfoCC0RkyXKEd1UMqwwV8fVfWwE9bdZ7tZQKNtVW20JAmpzA5SwgWixSQDKogJ0vpOvIktfYO3_82DCHbIHy3NwL7QCApxqg5-0DL3GhaWI0gBtSkv20R941GizP2GbA18SxYRi5ZImJt0tCVB8jGRlbLBH-X-DAywYuQzAVtq4WZJxEljC89CPqfSGRHDm0VmCoueV4vgnL0xjZFiQk2-Fa618tqyyentIqrkZpEOJKITcvQwyu5zTGOZDoU4KP60RK69rC3qLJw1pkHL9N9l7P8k2lQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elICMJrdCXNrNf4IJriNMUbMsjD7TJiMXU659NGlHOLYRZkQr48Pl6dF5xGRpGY1W2COEz3Pcd9Ym804eJa2k5PeXL-J1szS6arM45RCOhTtlEfD8rtZqKXEO1fpUKOcbgi6pe5w2TrUqSvOSyMtyS5uK0E6w6pe1hczvMKiHENHzoLtkx70c2k85xJx-t2ef9qjD0ECF49xg-vptZgKk9y-svKy6DrHm0BKFjh8fZXa8MMzRE-wOertQrLpt3uNneOffYGJNMA2B6aGKn7UQvN5LwXcn4O6LN5aBFBIqNWFsZlyg-WGWTyzBQ6n4gSYztZXen77R7j-Rv43kC3NKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=dKDZb9hdFiG2CdOL7v3kUyFR3orKWKblELKXQSfmwEM4HrL4K-OkD_AUX7GbIvhiRr_NBn7hciN7Ozl7KgVet5QCVxK8iQY6cNVq0rVvA-B04ijhMogvRZ59jjlP6wxF17W2yrSrAY0MIBR7VuZXllvbfQY0rX5sp_nYmmnwecZZhCA52hn9FekDo8PWjfjzUUTOxvcGNF_-TpkhLHyKOHEg_9zJy23BKV6xo07Ju8Z6Iy1viriHgMcHHpAj5xNSUuAw_fqziNwOpxsUMGL4ezrDxkSd6RYkccECM9FondhtxdfKBI31SMHuaRBbd9Dg3wnff-WbEMu0xXz2kW_dDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=dKDZb9hdFiG2CdOL7v3kUyFR3orKWKblELKXQSfmwEM4HrL4K-OkD_AUX7GbIvhiRr_NBn7hciN7Ozl7KgVet5QCVxK8iQY6cNVq0rVvA-B04ijhMogvRZ59jjlP6wxF17W2yrSrAY0MIBR7VuZXllvbfQY0rX5sp_nYmmnwecZZhCA52hn9FekDo8PWjfjzUUTOxvcGNF_-TpkhLHyKOHEg_9zJy23BKV6xo07Ju8Z6Iy1viriHgMcHHpAj5xNSUuAw_fqziNwOpxsUMGL4ezrDxkSd6RYkccECM9FondhtxdfKBI31SMHuaRBbd9Dg3wnff-WbEMu0xXz2kW_dDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG_Cf8QeHmIXOoR85nUjIfkSBTUzQz9QGWXt9HdxFeZoMLjVO_6HMzrJP-RvaKbKIK41nBvY-lo-Sxmbf6tMrQDMkC6qZlzTpMTmIKehNamua4ORHsTA-5jvfh1zzxSQtgb396ZHUtDCK8YBxjx6iJRTmQIt62YsgOGcQ9EA1Gy3NPKx9TmLPeE40v9qEeqovM-uu6kCWfR6VoaMC8eFPtJ0dahj7QMYPQJA2hKsdXlSasEkx_o3djcngMceY8WYwedkN4ITJGTV8Bf1d9BsZq1hHXRe4kqwYqmhrDssWxT19PcC3anFGRqZErc_zuqceetKKpl8NstNO_AJoiavyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sz3bCD0NBkbB06ZzA3uOZI-rrGfOzeOQ8fuVDjevZ7m6rRNTtxF82nDpJDYs9w20OzcN9T2cHAcxre496JwbD0pU6WjITspJNgrtuGDD2UiJ0bN-TVj1Ik8wYhsrEN4S1j40nLFpdHJJDsFVUCRs5K9LzSH1K5okDtOHqY_prCZMczWuD9gNlTvWfc4YPi9QWfGALTrOS7g_QkRtcnx1uqt5tLqUi-4t5M0laSItMPSrBtMcCQibU96xbh3a34mBZRgUrWC9bFnoAuKia1ru9rGJ8Gz9Tqj0oXNWh9vol3BWZ4alNsmwyVGHbG_jNaPG3BOoUSuWrAw6v98sZDCUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_YvVdo4VODZwzKE6M9fUUUW3Zjqatbz1TdSjlyIc3iBZR2dd_Jj9dR2J7WChX0zZN889hVNxXbVnlB4HjDUR6eZHXXkwKCZnsyZCmRV1rrHp-zwvSCge9xmfXXdaxbMVKgqnjDGWPcrYUCHBjTM5G_V-YYKPEWv91G0pDrWA-R1SrHie5c67kdjMU3Dk1jrqBLccUfVN29Wjr__U09A8MaLJxKmrpcZ7_J2AtLJW5yeikrUFcQvYPOS_qXcaDmyjj9wbKdo7SGgoERYKnvEqWPVmpQxcP0LcWyB907lDLN0R3ZfLIFtSY7xR7FuzKDw3_-g6jKwXNLcF9x1tmeFkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkqV9LDw_5_nrEPNe5V4X8bDuCP_p3xlNFtEgKUU2jYmbgOmDYlPh4oYXySzo76GDZq5BOULfiaIdRQDOtcz9AcdVtc0n9cfnEI0VjPvmMHsQ4wNfRiFA1aocStrKbCcXI4G3b-GVNyZ7k2D_GGNj9MGFP29P5gG6JoV5UpiHWsQI-dwF1LjgLLkGtKgCLdw7OD5L1gYhP2svEKkEbLHB9TuaQ2hGfQVvx5vKpNAz0cLCGJdN4yLGtuAvkhKMGddSlL5aNkdvnwXCHJwHEil4cuejJAxPbxuH5xRNcvXKR5HCMuXa-IqQ27HQZ15y0nI7tQRQFljNjcV51TRJiqdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHwOHwCzUrCJMpfsciObnNti0gu19SA4hxUlyc2n79FFb8rf3d2LPoyfxzlgdPoWe3icXH_xvh1urjiQOKS_MMzkJfOFuZwp2qJs9pd-UwuG_1ZnC59b_h9VkWBfeFbqs9QzvJFIPpvZFrjMZKByMUtr-uh9A1qgDTPU9D62cn2pD4v4Y16yJxh5IfIHP-_S92QQt3qZzgmhzYQCRpfJ1cIgG7ueOMLIL7E_x0PIBOXPTQweIY-al4YkIBeXNfJZreqxNra-d7CWP938SpF7IOkO1nI475nbiScbdOhWadNMCzJTdtvnM5aL6VTXC7UsBmvRamqscBUTVn8mn7dNYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCLlw5bNqw5aHghNozPj4NSA8W2B9k1BLB0TP5H-COqVGLK05e7YMpiwHqx4hxQ2InHcZA-PESsixwdzq0DdenxLWSsc9556Zu3nEVCEDJ2sb4nKdfHMtOxCGmMQ87n64y8M4FucNYNlh75npgMqSXGWUhSgYLVZ52wdOvzypE-igB-w27X9UlD5_7k62OmxGhyZ5cjSSQ4sZBOcpY4csqPSmUILdMHsgM50kiBGPQLPsas31PrW-3FCJq_XL-2bVoG6YXlRTuh_JRbYJY0MFDnY5rXVHQyatcmT2r7vo-HP4ZAZbX77ecKJblxyKfdcSOhv1p_uqieSNXKejudZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUtUtx0RJ-JoZf5zL2VQnmRjq2FCXnXGVydnYG4b9as9M5DdF7GwWHnwB4MP3rnYWmkAYqQxFV7Rof2nYuloi6jC6arEQABKAhUOL67chD6iHj5D_sF19sEUffRTmyEu984vpDuI3r_1Gywx6eqOAt2QXRiPwtkECaqIXo7D4NYnl0SG5a4ovd8fXRjvi8U9YV2C9utbrYm9p1elnThecoUaRbI7c00DGKHV1_mwiJ2P8e35qc0LPL8tEWrmYYgFBN8PFsw5nAKazajKhkeRyoaw_DaCaWUsG2uPfwLue8nw46G-0Bkgtv7cFmrJ7OgKYOZGFje58eyFeG4mK9tFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/koAYA3s4APJeZk01wVKcCLKbfsMpjfVEKWpLZ6CNKIpVlr2Vc7d88CqITDlcDph_g-cD1w16XoTTiEbeGWjAzaZ4NBcelPrV0NE73_Wx5UcQ7H5VqYEqXjLgHEMT6-oAbnY76iDmSr7qsw9ma57PCU4wGvX1VQqMYRKijlz0TEq8pXkZzg3tZMzEvW6-4QfXDtLIVOZ7yEJb7adzsNBsZytEaCO5P39F3iHViwK0kMowN1D1HimUiUx8uTGXVBKNZ5PSFLjlYR6qTA7jZ8hBxbH-GXJFVTum2cXThG7tOjurc3DMU8zrS2qqMEmy5H1uTjoCe56RPkA1seN66zAqQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=XObba9UfMM6_V8xS6xEJ3n9FOke58WOo724-CfMY4guf-cGOriojrNqbyPe-TLcrfGjKUeDH_scQgYFOlpeh3sQuVs4Ip_ZUWOIFxOt01wlDL0doEonUqUlQpf7gBA0dz_F6X370eMw9G95rVssfweghdCwRNkqGmsv2v0Tmy6PpuslUhtT8aEnJlvoGhsWAxDzX-4xWAiFSN449igX9VQTE8cM16lGmj9qAZAykyOOPoEXpOs4Lux71PqDj80ZF0dxJsKUNymqyXs-nxTLAd-E81Ej9YWjBZgF1f_QZckyRXPWWeesm3uHcSAYGZI_iD07dOkLp23np5DV4Qz_uiYMUdUb8DkQvouyFBZk78yQYGpW8vdpxHQR3Q1mIw6mjtoKqpUHWwMfH-qt_RWxDIUxO014mMu7QEkOy-ttztza6EaMqPyuUEVyH9sk_7xW1JP-_tVZJs128m0MAMasN4e8XuOCRKqc_E3-W9PbHF8l8f4YghA6rBqVYnnazW8iX4zeHlHpl5KArjBJo-QgU6kpShBiiSVMgbY_6ND921ES0Y011s_JaUjeBIWyXtly498STqhLaRugz80x6L--ZSpwMhsgbCAdCXkRqb6wHihxKioVEhlZf-wqtYWa7GHQRlIJiu54d53VkyStPyf4iTfMcy71vtafZg9Dm0ta5d7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=XObba9UfMM6_V8xS6xEJ3n9FOke58WOo724-CfMY4guf-cGOriojrNqbyPe-TLcrfGjKUeDH_scQgYFOlpeh3sQuVs4Ip_ZUWOIFxOt01wlDL0doEonUqUlQpf7gBA0dz_F6X370eMw9G95rVssfweghdCwRNkqGmsv2v0Tmy6PpuslUhtT8aEnJlvoGhsWAxDzX-4xWAiFSN449igX9VQTE8cM16lGmj9qAZAykyOOPoEXpOs4Lux71PqDj80ZF0dxJsKUNymqyXs-nxTLAd-E81Ej9YWjBZgF1f_QZckyRXPWWeesm3uHcSAYGZI_iD07dOkLp23np5DV4Qz_uiYMUdUb8DkQvouyFBZk78yQYGpW8vdpxHQR3Q1mIw6mjtoKqpUHWwMfH-qt_RWxDIUxO014mMu7QEkOy-ttztza6EaMqPyuUEVyH9sk_7xW1JP-_tVZJs128m0MAMasN4e8XuOCRKqc_E3-W9PbHF8l8f4YghA6rBqVYnnazW8iX4zeHlHpl5KArjBJo-QgU6kpShBiiSVMgbY_6ND921ES0Y011s_JaUjeBIWyXtly498STqhLaRugz80x6L--ZSpwMhsgbCAdCXkRqb6wHihxKioVEhlZf-wqtYWa7GHQRlIJiu54d53VkyStPyf4iTfMcy71vtafZg9Dm0ta5d7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=BP9I1oZqFDtCvkBXBMm6un6bY5qqeQ2oRUPQT_91wstPz5DbvoGuUNcY6cHoORplhVz0Z2FmnxRAQu_F67b68cb8WpXZx72sgOZhCSD8zAsNVkB_8DC8gaAKy0D0Ca-REg27SIwyXjxvLW_mPyNsb1-hf90FwjTOM-zRXCp5vsjmzohUyvV-c9imRNon9p5ufpaaUBYx3-Mkf6SFlcXp6IdFI91SxOkyLLudgSIkhvoURswLhAIs0DYNKt5nRZPmj5TUZUIcH42Zbc9zS8ovpZJwGP8RRvy3yf8Pqy5tdEbvb2UZYpygwWeJBJD6uADc_kDXtPANf63NViZjoGalbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=BP9I1oZqFDtCvkBXBMm6un6bY5qqeQ2oRUPQT_91wstPz5DbvoGuUNcY6cHoORplhVz0Z2FmnxRAQu_F67b68cb8WpXZx72sgOZhCSD8zAsNVkB_8DC8gaAKy0D0Ca-REg27SIwyXjxvLW_mPyNsb1-hf90FwjTOM-zRXCp5vsjmzohUyvV-c9imRNon9p5ufpaaUBYx3-Mkf6SFlcXp6IdFI91SxOkyLLudgSIkhvoURswLhAIs0DYNKt5nRZPmj5TUZUIcH42Zbc9zS8ovpZJwGP8RRvy3yf8Pqy5tdEbvb2UZYpygwWeJBJD6uADc_kDXtPANf63NViZjoGalbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVU8XFin0jXu70BoZxyoqWBIczJkuy-XDq9PNkOgx90ITkXKILoQIU0lXn3ZTQJ05kTDrp_mDq4CwAphAGkeyQ8iOt8g64bzMoF-NMV8rYZXDFjwmuP6NUCUI3FaUtHwRD4EvKMxN2mAVCLM1mPgexEY_w5U4ls3Is6ujVqdENfbi4M9HqLB18UAVlU95WsE5V3q62Urpvkz8MBgv0duWoOLF4qjdAGWad0V7jggdo9XJLizNF672h3Y9BwazG9LyvlOAfNPqMqO6ZgxBwLCa8ECENu-W7pyEKZKfE29TsvwzCuHQmgCbvy77Ud4HasWP2TbMz4-kvmfVwfkBYeaqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSdWmt5Sh15N4RB_AmXwA-5WBYeCfj76Lv9lVuQj1Pdjcwj4VuSqvrvHs2LthAcWyNyIeUI46ZwSwJoJJOHb99fqlCcV2ALumhMCzn2kYPv6G9geuSsdp3B_3yYbGHpp0J9hLmGZSjGj-R1iHpFGxexCVkPCfINwSlcd7YfbM4Pc5XYSps4QZOzKasA7buk82CfhiPSsAqNu2-NeRdZZ0UTY2d0am1XmoPqENNZtwJlR3KxI1cmwFNXEpGaN9Fs4LJpZZX1gAKPx34Jb7y6WDOYRJE5uYegJdrkdAbZBbxO2rT1KHnzaeWgfHOKyRu_Z5oWTYKt9sZrUp6xKU0t49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlCxH5tymb2rEWqRrcRPgmf4z14pecWidtPhNR6_6QkN7c0ADrIiZv8SqyMl6fRa9n-HyFi742cHwEAv5mjlAA3sM3Un1aYFx1m9xMhbzLO8vOkvUUHD5uXv_-oN7cyKPh2RO7COGt1XT4DNNGpmW8i2HE-tK0xjU5EKDZ23hwg7F3G5CYBrON63yaLgjM3gdLgN-o3H0-ePPnVFLFIFqdNKcbr6hadmqAEEMTJsisHClqjosIssX0YaOKH5SVrR4z6oenTAf3S4fTdCkfwJxF65nh0PltfSKHIwezwpaP2lu0t_AZI-MV8r2XCIRTGYs5O3kALNsusx5uNcjPaN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gywRKBsq176XGpvbFhL_scQNZrolGKdUxI1wB1gMWGQ4HwLHxyrocwULbsjtdIYklyY86LMpOrr81LW4ZsdX0JfpMIvvJJ2IzdI-j-4xFye9J8i77kHlfHnG-FOAEslMbQz1ZFYycQFgIHfsrtqcWk29uk5HYaDHvJXkOPTmtXyaMY9kea6TKmAG7fDCKVYsKZUQGQDKBNTpOFQZV2U4lsDQVqa2MEU2ks6bV8j9WYz7TvOLKbiUeTGRrmWqn7KDgfk2jmFFMLbbhWF7VTbKw6yKfnl8AuxspbZvbZ5Lk7eZ4z_53JmWDn8B0lViIDgHquw9ToHOcEGl7sQdFnB0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V18Xz3OSZoPD-KNnJfx2_SykvWDpgIOaZABdUMfoFqqWko_urTWZAoSTWNf-dJKch1bSsUAUfcOQYS5hmQ89zQeahOeDKPcA_AS2G9IbF1EA5IvKNu5k4lJxp2mXpwod0ks4j8p6A8njlPT1wzsoqsUTO6r_rN-0gINgXAaT9evdrA23-VEuYNuxn-Ra-tnGEqzITZaGqJn231KexJMuc5oqzrGX9XzrM_KqiLk4bqHUKdHd2hBYB7pmyQQvu7nGzlxDiIv3oW6vrZWc6TtMYz3FZW5on20b02ZVEfOh8yqDB2kNc5QOcRVle7vZ2HlBPx8xk0kb-xUtpGq5X597FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSO6_iaw0wgQ4XkxAMS_8i6t9KhgKhKbCaQXON5hVo49zKlYsVezDYK1W3hhcznwcUQLVT-mQ6iqst0d1NTuaHWQx8QrYA0YDDvlv6c9ax7MmE9KuO3JYWYpH6lQzIWlMQAd5Ct5Fe99wSvA7vL9SJltHYd3-l49OjvmDEWeTfYKoFQAqVVOVDZctmbXGD8tqCdyY4Dai397ulQi2iJ48Nz6K4pfbaCvq_kLTcVvzdQ2TZqeVzPuc5laefA8Tdx9kpu4x0AYoagwbngLDrkYYttxgJX6W7cDGNeKFNF5qdqAHkKT9qNuS0A9pBsMFLZ8846ZTJH4mEKjiTmnQ7VF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPKAjqDUHD4EMwZ6AFXJhFqMj-Ftwg7AWvcvWjVrOTtF0Yq1KJacGE1a_HdUtDkrmbkPHjRJwNfYSa8A8EFtOd7nlGuVYru4lCIJzytTxA7jcTpcBXjl8Q3kUyLKgoXpT5pPj5aecZj9nJJD8PmggSDAkAzJr4iMqiRB5vF4a_XyW0np1D9eL6ye4I8iopEG15cu_XyAjlMQh5RfIG7RWf8jogFAHKtO3n3ReiBCOibIgGtRZYN1uxX-O2dXgM8DdLKp2MlkOrV0uE4DuPPBrQFw4nwHWmW0AzranfBsUifrKvKz2ctMoFRrqs9s3694lUtFdR0DucNpGywLxOAwKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exlVzGI0mxGTF4gCzXBu9zpVnR5C6GrWXsVpb8p_HoBS7L4NwD9-LZkON_BhLxfhjSA9NXbm2neDanIO4UdK9HONWDEIlQGV8ZhyjXBln4KlDQPq39WeA4wzlkA4NigyXHS-VA1i-9uz7eIl1rvBaBoS8kXnnsuLgs0GbFSH_OK6P-vlGuHSccG6yIiB_abCVxe34SFkbF4jCLP-kq_Yvs9I9CjUXDRq4_vstwcFyoi6W_GFY_xq25rPj3FkjGfywm0i98fMips2jyrNGb1nq78ZVz2JuAX-f428QH2dYdnfDp-iF2U5HozsnduBmik5l7ZJkY0CaarZ8WwpNAH-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_pe76hb4oPsyWFV6qQ0wIGBVxMOCsDGAK_rEPq7NQpKEuBkSyKr4tPoXRV80sqweOLfMJRREtrbjZkCCuLZB0xYEBi0JbhGTPnh9aclXmMLMDBZ6qFrRjpCBzWiMQyuucsLZC-5nalQHc1kO83jmV6Q6KoGDFmE0Pn-p7QFWlpZt48ESr1zftwGJc_cpDzSoB1nfPYNhHZnuqxQTlrnKMivxoVcpc05F3KTZqKuC9hhXl4jAA0r71osRiaLRuqAct1bVvQdtJsw8WyOAOABjATB5yStMot5Pbg26OmRFmP1uu9ajdX0YAsJhasGc6JCzWV6Ms7PLHaJ-1nTBs1BFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=GSgWUSqf-aaokJa2-xIuMP75Z7ET8Yh_S_tYint4O9XLxTELbF0ycYKkzNZoK7gsbD4YAPl1va1MiOsv7ljRdocwOMvSMtRzISlw0SBPl7-9KJ3M0qAH3mfn5ny042FqgdFdLrX1obePmNKVhgar9oEq1buLpBA9WPbXGaWJ2hCk7QdD9ccaHZz3QSM-h50GXxwTpuVpRM0h-5RzmuS2lny7elQMHDd3J3fOK2J-8HTz-gz2xt7J2XvJJZHcHWVPuoBKy1c6RqANsINYjR4JEBguCMrFq1cYHSJvJGV37I0BuskuSaY_yH666InZSr2KrRwSXJs8aNYbGq_jDT9BBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=GSgWUSqf-aaokJa2-xIuMP75Z7ET8Yh_S_tYint4O9XLxTELbF0ycYKkzNZoK7gsbD4YAPl1va1MiOsv7ljRdocwOMvSMtRzISlw0SBPl7-9KJ3M0qAH3mfn5ny042FqgdFdLrX1obePmNKVhgar9oEq1buLpBA9WPbXGaWJ2hCk7QdD9ccaHZz3QSM-h50GXxwTpuVpRM0h-5RzmuS2lny7elQMHDd3J3fOK2J-8HTz-gz2xt7J2XvJJZHcHWVPuoBKy1c6RqANsINYjR4JEBguCMrFq1cYHSJvJGV37I0BuskuSaY_yH666InZSr2KrRwSXJs8aNYbGq_jDT9BBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOfy7yc3tTey3c4X-SeKq-PkOTilGrViZeqJKAKC4Niev8RsnHG1oc7KppZ7TEOSBVah4_oB5se4xYClyB07YxNQIdG0k2pzkNeS9Rz7SDOT7YVXl2pSIMS_HOapRwlqz3OzhuYfpUrNy4s14QrQa9m0CkPKSwxWyA83ue0eBRIPN_R4xeMn3kYMSmxNz6ZxRtKaIwTTABA9Q9cT_AlLPCwdpPXAXNg2dwdu_rczIsIbTcW6miQlS-K4ci05OKV6z4kQPquH3t9FwHCeMLmT4KtSoBAhkcLCUFvj2KTm8mt_V8Ry8ZsNHsT5MkFU1mjdKQdNqX28-13vxidTBEXZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=iuwoFO2U7ji9s2Ja2a7Xy_BTAe5hdCh3NT7RGXz80h_8mlavzGIld2Jec3MyU8CzAJshZC-y2jydj2G2EZPAj_fMrLm_YeSxON4yBulqBf9LA3kunkhOkoUInlAhIWtTZcJk0cLNmVmgVMLHHK1zS7ci6f9u3zz3AIljxSITyJa8lEYS4YSncIJlkdAJ77tu8MKX7WjLux603e038ri_b_ACTjLaV4KKVEqJT7YXCPmf5gfd59lAc1KsV0H_g8HIKIflq2vHjSA9xGXLvWXyKNNRvfn3Ie_-dQcQ3eWkoUxgyztUTuJMfBv_87lCsvE1zZ2wyBJ1Gh1n1ukRJa-nWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=iuwoFO2U7ji9s2Ja2a7Xy_BTAe5hdCh3NT7RGXz80h_8mlavzGIld2Jec3MyU8CzAJshZC-y2jydj2G2EZPAj_fMrLm_YeSxON4yBulqBf9LA3kunkhOkoUInlAhIWtTZcJk0cLNmVmgVMLHHK1zS7ci6f9u3zz3AIljxSITyJa8lEYS4YSncIJlkdAJ77tu8MKX7WjLux603e038ri_b_ACTjLaV4KKVEqJT7YXCPmf5gfd59lAc1KsV0H_g8HIKIflq2vHjSA9xGXLvWXyKNNRvfn3Ie_-dQcQ3eWkoUxgyztUTuJMfBv_87lCsvE1zZ2wyBJ1Gh1n1ukRJa-nWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=D3QsYRlWr7qPVV2ctzU_PTpjKSb8fjRRJCsgzuEPgc29lHh169cgJ1E1A7obdxxGjNvzawzc2k_iiBPofflAlgx1OOaKAKjQhEbUJgK2-BfiVa2RN_Z5PG3_0VEPGYvAVjpL0TEYmRA1g_uW93IKAvPkibdZh9TljIvRWtqnxpZHq2LtEP0HuTfyOYCRZD0hXBlf6CNN0vK3h3rzraMJIBvqQaqHdCEU1x9uGTdFpoJJ_q6fWSlxm2AdTOxX_C2cplnh5AKrZufmwL-Sud4qhYIG0yJ_P9DB1gHlQdC4UPVt4ocjPWCgEUL_a4DvDsroMMLbZ1E1BKBg8aa5xRxrOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=D3QsYRlWr7qPVV2ctzU_PTpjKSb8fjRRJCsgzuEPgc29lHh169cgJ1E1A7obdxxGjNvzawzc2k_iiBPofflAlgx1OOaKAKjQhEbUJgK2-BfiVa2RN_Z5PG3_0VEPGYvAVjpL0TEYmRA1g_uW93IKAvPkibdZh9TljIvRWtqnxpZHq2LtEP0HuTfyOYCRZD0hXBlf6CNN0vK3h3rzraMJIBvqQaqHdCEU1x9uGTdFpoJJ_q6fWSlxm2AdTOxX_C2cplnh5AKrZufmwL-Sud4qhYIG0yJ_P9DB1gHlQdC4UPVt4ocjPWCgEUL_a4DvDsroMMLbZ1E1BKBg8aa5xRxrOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwBNdFJ_WYiD-8fAldjNpusiMGPkec3YYtp9So_O8jaDvUvg-Ha8Z1Q3LgztOvBoULO3m8BB17RNGrboV0xq1KVrTZcEkZpACIhrhwJhynb42s9vDC-e602CZNXPHvQPTAiaiIecJRIzTECEK2WTCp_PMhmZKXLDcsdsCnqrhASY6TGmh3V_b3_iv9w8HUB_sw4y3imrVy2IkLS9W5gLhPRQyufNSJliOQmv_O7dQV20qHBfIHG_UrsES5Ww-6gyKJOFaqP85Li3oAvw3Zf2W18x79AEuyrfrS-mC3IpSxa6-ssY4sJD_hn3VMeZIpadAkOR5caLINsL5n9T3XaNvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=v24zLOP19SwITSLGxIC6cx3qk8EkluuodnSCYcYWRw9HsPm-aY0HGpsh_ayEnezhd8b-7g7y9Gsx9bW6JSt839Z_fdRQa8aTcaVSfF3oU3GOBCh7qt1YtxvvWTewf5TXCN_x_4nLK2sEHINbnt_2e64te-AQpEUFD7cojq1kEfZhL1Efq-rUOnknjl7Bmr8BdAHrkhZkdxrPjvyL0ucgmFquxoRr_I4JwfBYo1ltjeHYFFEhxtVueyD5yQWN1IHaqgp7Zat2ku0ekS4qo70kWlQKcA7qwkfxXvxjbNLI7xjtjpIq0EJf5TFU1FwUiuIIhrqw-Q36o-slYpJNe71eqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=v24zLOP19SwITSLGxIC6cx3qk8EkluuodnSCYcYWRw9HsPm-aY0HGpsh_ayEnezhd8b-7g7y9Gsx9bW6JSt839Z_fdRQa8aTcaVSfF3oU3GOBCh7qt1YtxvvWTewf5TXCN_x_4nLK2sEHINbnt_2e64te-AQpEUFD7cojq1kEfZhL1Efq-rUOnknjl7Bmr8BdAHrkhZkdxrPjvyL0ucgmFquxoRr_I4JwfBYo1ltjeHYFFEhxtVueyD5yQWN1IHaqgp7Zat2ku0ekS4qo70kWlQKcA7qwkfxXvxjbNLI7xjtjpIq0EJf5TFU1FwUiuIIhrqw-Q36o-slYpJNe71eqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NccoMW2iteB6zAtY_MFp6MF_Usf9W9O1ZAPFRq79NH9ICGFZ3dcidYmb6BwNRP8bXHu4PsDBrFcDZtT5qUCmCsRe9u1KWgQEg30TJK5CqfVTN61E-EMvkVWRi0e9ZQwJPURuaitrHxh2V2DmWsKQfzJ3qkNUGkB54AWddZtfzc5GrgfhFxBDzslLK22OLJlHrE6HtdDarxk6LqL4L70iVMbPMfDcAeP6HyV0yajb-wM7oVydkdstQyoepaQfBs71d-c7c2KJC1pIiAeIj1sK0RXL6j2oMk5hcHchT1t_9XhIiEG9CLW6MwAL7aYVaoCMrUhnPxWRZtdekN0F9XWI7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFx948xVMQya3h8DdaM4n1dH6ZSJZ3R2gBIncVyQilNCppglLa_PnuD5wJfeU1LoBnxWexNJ_EpRkGlm-QG-pz7RUhhZ-ETy1ozKYHIOK5_zMN41t09cLJjTQU530Z_v0Wg_eTcOm5i3xjzuKrrxEt1dYL_JxB5OG1XLotAF65C6gT9VCvEGmkoz0frNJprC9efwEgkN0kMZz1R3SRgj0xxc9-p_CXt1Os4Q7NaGEkEJoJDa7TtkjuV7DhwSIAlsLMVCqBc8_XPSSO1e_DpC8eHOsq46pIdnFE-iVF3vKik8H9PIqhN1mSgFNLG-ZsBF07RCuhI340ReYPdqJQQJPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkQ13PW9Zg5oggEh-HzDc4S5IJJUWZSssUwtA-tNPQKMPXLvTTQOYPkDOdK7hrXjoc9cXK2zSBy-DxV0ENh-01QgB9ywnc5kLyr1WsqOPzwIvB1OQc5h9wR3-EPbsCbTsfGglE6adr-oUARij7sB7UMVMvpeZe1LEIDRacv_biIpShgqcZhRVRH3tu-AF5kIgN0zWipPWz12uhTXd0CaM9JSxp8ZJeR0caWo-vilr-WVeAlAmls3gdMrRqdtLH_bo0J8zZCx0sM2hfkYbK83TJ3Z2FYwiN_I_ziTaCvHBr95djsYxe36hPrijaRXU1BjioF7LRmFaWhcpCcpAVhq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eR3w2XCzcDhVxcVWKAOm3RartEB0fl80GgvDejzgMjXWSRTs_Q9AB8hjHuNXqcUl_x6ULr8xKcCBfDTcsOrSRIb7PPpmKYxfnXQIv3gsiOu3rf1kmePuSHEFwgqEN4yAgkSb1xGn9ZB1p0rAyi_zZUnaBfoJYZzyrJ__Dr-6UXe5LhBl2_HuotG3z04s6t5N5Nwwe7N6rK-w4aMzTFVmH4eMrWC8_ooytWFw5iQBxr9yhXRVnaXGzN2SroWOrIZirKJpqUplcmBnfEn-XFf5rEF4Ifaoz5yAMMz_K7WaI_iql1DDVHd6fG0nbZBqrmFO0imXjNXx4izu1kgS545umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QbXJZqhDLdbMm8DAt2Fp_2FEhdo9ckNf6UpJjleaTOlljwo84ZgOLTmsnJdAEiMuOe_-or6IkHr67CyH1f2jr8ai4eX1q9wIEwBMfM0PnyZemWPa4puIpSjCHPfwZ3RcIdymUIvE9hc8rvE8P78M7PMiLEZdSIQcR1hGsRa7MNofiRVFsyhYAalReNLByFndCTJYJJKhQ7B1cbf0c2aWPeHM6dv_NtulDHQyoKE1vQ4xCXFeZuot7dy_Cbv1Z0UVbt-6llxn09MA7uXwDKGjGLab7YUkRISuEAmF91jpDl3vqZpKQx8XKQzWc_IoixnwoK3klmUbfaAgbxz8rfOTIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmrvLOzs-TrsEu4yDegNszBLLeRyqE9N2MbJOBjgscNazIgBnKA9ed_mGSqm-ikkA4Xlj8T1X4dRDBu5ZyYa0eo7PqIrl5QGHjLXGmFhv--PKe5VOgl_TQNTrfnRughM3AEZjQ3RSFa71_dGDljAJJDVzzONx6gUtasoQnc6-WPx0DTQf1Qsb9XVF6GNelRKGcGZHR3sA_f-6BA4lEF493EZOn9UGlbONZ54Wz1EA1pryOshjOoKn0ISZHEuEef985IDrFne4yparJifDJFQQs4arb1bL7ocCr3Dc63r6clszrj3JIBv8cPaNUztttTOLDsVrw50RTTiX-LAGwCDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1Rd_I1feNXi825neYHqoVDA9jCu0aNzkCLT2Ar3phHXzdyu6EnwVle9PFajhKUJtp7RTxucdejN_iRBDTUhnFVyop3_5TWaag9Wkk8dqwzigKtvpcTNTkyxG9EZ3l4x6ozKk_h0_aS4tHZ1GbGaX6ouhSozcOilNarYLSGE37ccCppMJrCDSJEG36vbqq7dY19qXOdmuBeDRfE7SY4UZ74dDlw5n3UfCGsPnyh5wjZf2NLtg9Qbx5DBhGREOLUhBlpeqj7bzzL6wopVwu__Q7tfLZdq9mQoTITUEP85djK7n4A2FRCCIklBrK2BuCnYQ2qQxzCgoDs5jKZEUKfpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TN7CQnZvJj3MSXj9C8kpTWfo-xq7ErGRCLC0YC9RMbvdpm3fvQgMMdQqA9Ej-U_hxohNlNSyX5uUmg_yQqW05E41E95AzIL8pGgMwUjdhtSBtSfdXwKDYOt8_rNhsGyqkebFzKGhVWy7KdIYYMneN3ToJ-jZ7iUZW16RSDtygQRScWmlY39gWYn8OE2J05przsIYsVWKVZ7XkX2tCfz9uUvp9Tkoosi8Lp0nvZbrzsISl68CqTLnNVsbj7rJW643_z9BnMR4tgzaBWaD-syR-8rsvdWTsJPbeYPD6IHzW5lUUt4pLRhMx8gaSAacZhUGLuUy6nROLYtkvjV1XH-6Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=S_kGs8VbcK4FyUZo4RyTbe05IXkm56Y0arJh7X2e7Vec-zGGpN46NnbGP92aYmei9S8AVFjyzTsBqovpozvngIBfcSMiDnKz_7g2RQwmw-lVo9OiQzVlU2K7sgUowAJYRhS_JcY8Kgge20yPgEhlEeirE0v483mzEGkUgOM35Sc_lxEeDV-3mxr2fmzQH7YCDfEY33ixpQV3kmYbD4UL49j3dcZpicETX-SN36pD8B1xnQloTnCYb2RKRnLY8dk616bJmx_w6UTZW35FUjg1N1AhEPaybGSaWDec6KwAW-BLwWYtC-_m3QR6ieN0doXa_PkaOiKswUcY1uzddnDAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=S_kGs8VbcK4FyUZo4RyTbe05IXkm56Y0arJh7X2e7Vec-zGGpN46NnbGP92aYmei9S8AVFjyzTsBqovpozvngIBfcSMiDnKz_7g2RQwmw-lVo9OiQzVlU2K7sgUowAJYRhS_JcY8Kgge20yPgEhlEeirE0v483mzEGkUgOM35Sc_lxEeDV-3mxr2fmzQH7YCDfEY33ixpQV3kmYbD4UL49j3dcZpicETX-SN36pD8B1xnQloTnCYb2RKRnLY8dk616bJmx_w6UTZW35FUjg1N1AhEPaybGSaWDec6KwAW-BLwWYtC-_m3QR6ieN0doXa_PkaOiKswUcY1uzddnDAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=hz3IS4WXumNIJ6Tk7I9DwQ_1NyZe6EXWLQfut1TkJ33RS5HntfV31i2LHQ6BztIyp012yUuQ6cp1_wXM3OlKPn6kwv0_FLSw1x5IcChmlH26UJDLLpdrfn5fg53sr1o1V7RJPdqs-TQjZXinIhXHCL-8LQiVcal_xqPG7RJwFSuSYTLK-hJ-O8o8BThVRgg8TCVJqOlaXSiIFMIrPGt74Pl8xAKkztP3YP9DVnp8GluX1QusKVMnmwzs3qupwKbCXImiixgA0mpBeOxfr5osWcrky3qRGx6uQPjXshpodf_s_zghFpyLMKaPV3cvmdP5_6fXTMgF5hbXdmc8VA3kNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=hz3IS4WXumNIJ6Tk7I9DwQ_1NyZe6EXWLQfut1TkJ33RS5HntfV31i2LHQ6BztIyp012yUuQ6cp1_wXM3OlKPn6kwv0_FLSw1x5IcChmlH26UJDLLpdrfn5fg53sr1o1V7RJPdqs-TQjZXinIhXHCL-8LQiVcal_xqPG7RJwFSuSYTLK-hJ-O8o8BThVRgg8TCVJqOlaXSiIFMIrPGt74Pl8xAKkztP3YP9DVnp8GluX1QusKVMnmwzs3qupwKbCXImiixgA0mpBeOxfr5osWcrky3qRGx6uQPjXshpodf_s_zghFpyLMKaPV3cvmdP5_6fXTMgF5hbXdmc8VA3kNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=QsSwv9SQ1nBPW4_PH99K0mhvwV9mLBtFYDBbvaZTLmHmAto2DXvEapnW83zGa5jSdcNt9eCyptNSwlPnrHvn5Gndymo7ojYHCqTSBbN_cVVRQKvnT4nbIWh7PoZGWQyYOr9D-qALMdM3itX9wH4np7x6ZNFnBxyFXhNBBm3JrcwqIXOuJBEYF3mq-sj0mMvx3UNuvX3X-NSzFf_y-62tKzhJYaYf1rnYpVgk6YGs4wyP0uutEvVQAmNoh-lQ9QRsZ09VqARRzr8seoH70rzkQvLe0xKNvUQ_VyKKH-J4Q3vXl1MiB8i_twPAjeWO-KSJzjYqchtM-F8sJ3PlEgEHLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=QsSwv9SQ1nBPW4_PH99K0mhvwV9mLBtFYDBbvaZTLmHmAto2DXvEapnW83zGa5jSdcNt9eCyptNSwlPnrHvn5Gndymo7ojYHCqTSBbN_cVVRQKvnT4nbIWh7PoZGWQyYOr9D-qALMdM3itX9wH4np7x6ZNFnBxyFXhNBBm3JrcwqIXOuJBEYF3mq-sj0mMvx3UNuvX3X-NSzFf_y-62tKzhJYaYf1rnYpVgk6YGs4wyP0uutEvVQAmNoh-lQ9QRsZ09VqARRzr8seoH70rzkQvLe0xKNvUQ_VyKKH-J4Q3vXl1MiB8i_twPAjeWO-KSJzjYqchtM-F8sJ3PlEgEHLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqaw_hqEXLzy8Y-n93_Td6aaZ4RPJLvBG1acZlM2qRx0BBx0KwDRmQPR1wYws7oxUw0t0lqtj2dcVagUd2LaxzwAwNVedi-ibGiWuouwQRs5yx-vISiDmJRbOn8-iPe4Ix1djlaC0HOwtfEg0adOffNP-AFctAlTM_IaDfIAfqHWdunMRe_MlkWsJ5U6-iVTxKGm_qmYkGPrp4roRNjKOwRj8DbOZON7EbFZSwHlHdEHWtDR49QiX_MuFRC65tLd1h6I_tE1cTIRRJUvhl2wAJqzdqG5kzQCNbU2Tfma1eQemzsRs9X3cDkJrBxAvUpcEhn3stRmwDPhHM7gBlfCdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9d69hX_8-tt1tQ9Yucv6dXSKbA7nsRRD5qM4o17dNy2ZqvR-i8dR6zZxbowX6uV-G9jZ1hJzsLgehzDpwCQp4m1zXPR-o3FF-KM-922FMb7lFqKezVsIBVG_qR5UhwiA1mqFS0lFxYqaNlyLzY4QJx2h3F6pYuJa7Wu6qCSY_lqXRmQuIw87mpqfYTavbFOzims34z0ZUTaLUEE9Q6mDOkC805pnak5rdi0B6innRD-8aeHfBi9LokIeZQT8HI00artfNrP0YH4nC0tmXNCAFSBTWRotHM591NriRHXyALvgLkkTxnoHGzjtQRxq9WH5pEN9C4RMbgkLfxOohvcBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2YS1WnMBA3S3X7lkxZVVFwDqUqgFH9wnIwZsblximX-jBd4hkyFL2xngSSojrvt1Rf3tCE8NZBku5Z9aen9oi-tc6K91ld2FsL76Hj2SDDXtWgjk0nZsdHnb5tQru6AvFywgTIorkxoj0S7dJ7aC577i7Z73dRVcwEn0Xj_hRncymkcFDKrMVUmVn3MkfHAfAZk0lLE85HPHrC4L7ORYCjhXNCD9v5Tp9sLZMIlcWRXCkZPMe5YSfy6_TJWBC2MR5QczVGwzW5_02GIuWzIf7JWVSElL4aTU_fOxJXRhWuHf5gxNhuDhoXuGPTSEIlDKrm8unTmGy6uf_x6HFMXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9BcqrnuaLXGGZKrcHWv_MHV0wvyA3CaZlzscqvp_NFDF8YypuqdgNTr9rtdkZ7GR9YvPeP72Y2KobKiPg9wlNW3-CFlRpyhBnQckyfLqzX6uGCNr0Wr0GEKLTpl5jHHvbGZq499HSaczn6xb6q4ikIoheY1k2SH_ZV29szD9C7ABwMuysXHJVWXTkJth-QNqo1JfDVvtdk9siYKB1tN6oKoQN7C3B4ekZAMSFR8L9a-d5cCMe0WOPKxkmhIBC6qqNONuVcLLo67OnYWDfwBWSKiGwjPaJ_KqjpGjh-iM3SfLIJ6Y9Mqys1r5MKnaIvPXOAdVgXTAm6qEgUengpfrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=cPKzzrJiwpPJ4T0GLK58aXtxjbRxvFppTsqMWsWfWyvfumlw9l9-BCT-njhK5GOqwz89iE6yVtm0sNMC007nUUPmPr6tp6QGf6sy3YCjiwRbOeIVutF7NWeNlsmOjQ43-pI_2gOnC_rA7tjElsaSNWRnf4VSPNLPTLJsLn2t772TlIKP5nvRO88W9GTD4lhAiV4ShjDdT6Om8jZt3pOSYFLt6FjbVopTZVZe_UvqHhBxE6lV4q7CNg3SzwZ9QhTdrmqtEWDOy1sHLIMnAJNSwuXEGATn7652qWJJmeY4Glo0vk31H_lZ621vpyHetU-FOskevp1zEiwgMmmCml-r4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=cPKzzrJiwpPJ4T0GLK58aXtxjbRxvFppTsqMWsWfWyvfumlw9l9-BCT-njhK5GOqwz89iE6yVtm0sNMC007nUUPmPr6tp6QGf6sy3YCjiwRbOeIVutF7NWeNlsmOjQ43-pI_2gOnC_rA7tjElsaSNWRnf4VSPNLPTLJsLn2t772TlIKP5nvRO88W9GTD4lhAiV4ShjDdT6Om8jZt3pOSYFLt6FjbVopTZVZe_UvqHhBxE6lV4q7CNg3SzwZ9QhTdrmqtEWDOy1sHLIMnAJNSwuXEGATn7652qWJJmeY4Glo0vk31H_lZ621vpyHetU-FOskevp1zEiwgMmmCml-r4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=p4EwHbMqCSMuMyJ7GSs3nUoykUQsGCqjj8R0MSwW6Kmi3rcAF4rNHUtzmFy_9Dly6VOaik5_AGSLaz4O5XJC0iLLV7m0wB5wY3BAIvf9EL7gUHdXkT2Q1Vmv93C5lX5If70MqvD1-mlg6qcN7VBQq9JtMQMU96eY5dmvR6LbDby_t3z5A2PFELmA6HeWKK3_lqHzMpIRu9ndqwMxNyxfKchmA0sQQUadu0f_70riCApCo7I8znpNm9lDQBYbRRDkYUlKB6jKJt5KytZCvQ3CzgAlkxG3zeLR7CyIr6NiwzAp4olXvYZyceSJ4qJ3VLpluAdpS4Uo1x4v_UtAturSLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=p4EwHbMqCSMuMyJ7GSs3nUoykUQsGCqjj8R0MSwW6Kmi3rcAF4rNHUtzmFy_9Dly6VOaik5_AGSLaz4O5XJC0iLLV7m0wB5wY3BAIvf9EL7gUHdXkT2Q1Vmv93C5lX5If70MqvD1-mlg6qcN7VBQq9JtMQMU96eY5dmvR6LbDby_t3z5A2PFELmA6HeWKK3_lqHzMpIRu9ndqwMxNyxfKchmA0sQQUadu0f_70riCApCo7I8znpNm9lDQBYbRRDkYUlKB6jKJt5KytZCvQ3CzgAlkxG3zeLR7CyIr6NiwzAp4olXvYZyceSJ4qJ3VLpluAdpS4Uo1x4v_UtAturSLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2yWzrc1S_sNRTAYT9MVGEpJlP1F_qNDRkIUs2CWk1vbTA-E7Frn-h93lTDQZqFsTLGB7-hruQ81zrfVaf9vsQfY-lsf2kYPYVOmB-4ZwlpFK6rK2F6lb-oyeasxZwReUPhYZXlPsAlO695eAW1v5oW7L1bTQO60DoKOK-uDwAjsakGgIQOlDPlMdQ-83BF_FjFjaFRbyfntG3BkCOdDHCkcVqABJCoVEbvgkZQod699bP1EQF3rwkH8HkeGtQzrL9sQgZRNnbHVJ7wIpY4NMsIZgjxVATucG9L0_fN6ZJ6uA7FKV2co2tZOFaZIdauIPu93fuLVEYDFVNTrDs_Mtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVJt1Mwnx9I7CJRMaOHTpq9E14-_9Uxz4IK3BSsi6uG8qq6uAz-iAXRHiIejKsjD79lAu9IjIqFK4tC_Csz7Q4L0Qv-CMWl75ztZu53os49duOPnjZBkwKRqEUTosvHy5Y2sp4-zwb6_F8BANy5hP6pJ5Z7KaFfDW06lxJN1ZqR7oWS2onZij2iP3Ixq34pVTjdJD9s-6ZrESqEoF7HZ1fJHEMfT2m7J51MNrmc8aRc3OkHDD2bNV8XxdwLZU_BYX-7s3eeCaHN4u2Qp4RZrBajFV7_mUV_NaYRDTWsY1HgDTBdWT8ZD0GhfmuPAEVORR5-MZtBTqOOyxZZoRqE_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ_52kPqAYYYdmvnrgrcKYTDN850bROaFBOQMLnzlCqujaenjTDtWv9fkEn6m8w2rK-Jxr4Oz6msgqh5_a2mXOrzSJs0hQEnDke3GXFQmadHcbUrj8cEVqs816g3XyrxQX6pTfM6xndyCeh1sLhQNIm27StKOzmFHhvoOMNFgq4-gtN5jztW8VYK7oAbU6M9NJaxqKnyGVIn2NbAjxrrjXfqgqHdtr6RoHRsWTMX0qYjN2VMuES1-ZVfbz8z3CMKFi2rpV7qShkrDmVgbzyQHXjG7JP2_OiY5S2CypMPXrHjGHgfsA523PiDo7iJ2iE61-yWFMhpFAm3NGjPR5Qb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6BUt5zC3nK0-sjdHeoYLeyd7OKfkvKqTlO8cFgyxLkUb9YvpSqo-QIzLKoH9cXm73XnsbeU9ux9OkUfvPDofZMy8k7n3vDZkMmPG1WpDfnH-vpEgTCex_fxjwHKUesTv9YNtXAHellVJ2aBN7AhcCrF4AwuakCU7G1u1cZvd_isYtSYsEj9z7a50sQWp0Fw10m1ox_QBlRRa0f3bzbZ3ZdXs2dUULUg9qlu4We66Sw2u7wSOMqP1eTd3h-3GNTPRn79JzswglV7Vbni3DxMLLFIMF5dN0WcGdtbzbfkXvRCBG0CH2bCiuTj13JWn1gir4mJpDltjRibRlDo5fTqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZ-Nhx_FpedAsImPfYbZjQAeUVKJHEi-aUH_9UzcXFKSyfcxLAZf2qgGVtGYYeLFHLeQa87ArBfU7wgymOsV1IaejYcxumPK1nk3dDAIovfeB6X0G3IQiAg9mQQqEx8w0qNGfwXxi49jgSaOBsKwOdulPjeUnMZlPFgjBYjqKvIJo8HykV4VguHww9dww8DVAvnpAW0AQdpzGdZDXNQ8w7I2ocm1S3L7UmD4b_-OmJnqNE_tF9Lk7GakQ55f-tvtApJxAkzE7zSW2Lt3udQxnDHKkeoAP-19yv0FE2a3pU1isO38MhY-PQClNfpQIrn6MCTNlI73urMzvNpL1Zf_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mamvxjx4IpCHYwjsxVLj4HV66uzWSSgwt5NyuRfakZS8x1KfqFYULvYBfIjfWaILakMuINGZOxLDT9_qDlcATRaRNKDU6WBa7FAz6yL9pr8TsgVlA9ZnId7gzGDRAMeYPLexXEw4DUFp_qnE7LR-7xqFxC8j__5vQbCWWNyR8NQmwswsEVvozSaC5bxx_WNaYbWU0dwcclWIN-6jJXbXojbxqkKwmM9ngSJIbMDW7GVU1Ts-IHHPQ4YkegFHw4N7RdzKeo2RDkhHOffgVmESMY8raGebtaRTQAP8QIbTHkDfI8pjnyc0yAPMsbZ-pqbDYzk9SeUnCTiNU35LD3LQvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYtKPvhcT3RU7cCLXeBF0blAeO0FH6ab52tbMwJYyC01fhu8r5G7j-vbyL3cO0BhL9pKetpeXaKXMY6ELbNhu_KnSvpeTrPkm67eFcE2dFG9fR1kYEemJcyFuxHauIekQWcoTI0WkvbrqEPVHWp1-QplrBFNHkcET89RGkW9WiBRLZK4P98abDsPoJf9PVvoVpXlPkcS2uSbfF8v63Zya13Yiw7wMDHLxlOSwVZxrOwucbh75dq7pSoiNMmKZbwIJQJQxZivAnNOi6-MR7qOA1YMWQ83vn0c3dx1qaZFH0Uta0Af5zQ-h1IKlfCSebLK2j39jjyDxA6sIsMMdAAa0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_N7eXTIHXRK2n4JO5AMYo_HlJ4RKsLL1drUgTi54gMhevE1CpfOoiiEmvFL0SsXsKi5PJ3cUCN4yt5v-ZFbQBRVSWklROQj8YzoOlBsTzEBRJozKvrErt5qR1b8iqknArEtHl1TEkcD_5lknskLVmNj_0O67bXBWHLOgc-6ydJTOCYIlUwkEiwOcSpAHM0NgF83UAHX8pdSA1K_PIT5sxRG_eqp0-zIzRgIWiQMd3BsVq0u4brSS0gPiP9zeqxvMXw__Zlr3vk8iLw3SyhnoqxTcplQcdpm-_Bt88FgkiHBH5hFJYTMS3xxjjLi8EW6AH2P3XzvB368g_WobbYDpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=GGFWnczVZc0y7HTdsYVvfl4SZ8HI5WlLyQSWiKRggorLPqLSoi9S5INvqbGgfOsW-0a231Oi4btFAh7ybgtK9RT45pnjWeq1jpELAdGLA9moX8cWYbuRqRATqrNN5Im6q1F2qaAGbe3opfb251BjugP0gKEp7VMiuMuFQva08SeDb_La2J02rOGGOnyq-rsBt1WKpPVamHM12h8PlAbBdRFOsTNWD9fo21KgAEUerICsXrwYaY5fb4stKlWc0W2xCw0TLDsVv6MY8rQ10caS3bmatDfsiKR5NUC6MPibHTGyUTvJfV9cealM3jHEX_8mlkoy3pQ8zDoNTNa572t2iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=GGFWnczVZc0y7HTdsYVvfl4SZ8HI5WlLyQSWiKRggorLPqLSoi9S5INvqbGgfOsW-0a231Oi4btFAh7ybgtK9RT45pnjWeq1jpELAdGLA9moX8cWYbuRqRATqrNN5Im6q1F2qaAGbe3opfb251BjugP0gKEp7VMiuMuFQva08SeDb_La2J02rOGGOnyq-rsBt1WKpPVamHM12h8PlAbBdRFOsTNWD9fo21KgAEUerICsXrwYaY5fb4stKlWc0W2xCw0TLDsVv6MY8rQ10caS3bmatDfsiKR5NUC6MPibHTGyUTvJfV9cealM3jHEX_8mlkoy3pQ8zDoNTNa572t2iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=ihgAOsPJoLQ8Gk3U0eXH22b3if7JcXoWFOP2EcwKZSiIYRAAkxgXNx9KJHlHT1v5OUs3lt1Cy5mx8ju7hFPK5AIpsz6i_8lP_o4Jd1H8jd-oVBLYcsCTi5HrQ_5Ob32PeT_q-IzgWZjNLICpXHRgdXmRKx3PrqFNGIxkXovecyDv4Axk_6w0JdXOC8414nxp_lyJTqjq1edtyOeNnmzCCW3XjAWjLseY9D-jyE6H8u5UUIN-DI3GrlaXUAnLzRRhLtz5VqiU2PYXqGylKp37YGX-ZbiI-G8JHUFn-sK2T-F7pisk-dbJ6pWj7-xSAbdVilh0dZF-dC_MAxk7OxhS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=ihgAOsPJoLQ8Gk3U0eXH22b3if7JcXoWFOP2EcwKZSiIYRAAkxgXNx9KJHlHT1v5OUs3lt1Cy5mx8ju7hFPK5AIpsz6i_8lP_o4Jd1H8jd-oVBLYcsCTi5HrQ_5Ob32PeT_q-IzgWZjNLICpXHRgdXmRKx3PrqFNGIxkXovecyDv4Axk_6w0JdXOC8414nxp_lyJTqjq1edtyOeNnmzCCW3XjAWjLseY9D-jyE6H8u5UUIN-DI3GrlaXUAnLzRRhLtz5VqiU2PYXqGylKp37YGX-ZbiI-G8JHUFn-sK2T-F7pisk-dbJ6pWj7-xSAbdVilh0dZF-dC_MAxk7OxhS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfz0m2y70ifg5Tk2a5Mg1wDyioFRLJL8VYFTdLHNzmJYbnlExAcSMFnvxJp5sbWFjWRT_ociIWsKQuFwiWwMtdeIUNypS2LxlDmgG0gsYNbpGOLJc5u8bSjnRvNmCtOjo07d_Wv5OGHIcqVTQwL4ZByX0NEVnHmIUczSOpcHY6HJZaqrKx1vhuBDmFrvvc6iHKPj1QGs-qMI84fOIgY3ZQpXe06YL_M7z3dZUUO1QB0y-EPi5IOaoxaKC7ASoz8WCdSdCF-9WLV3xrfFDbzoc97b15wmS25f_JvSySGWTH6KKkrskmoyoPVX8PCSzj60j2D6NYaaFgmhA716BqYfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrvj6ShaLAv1PQcMBA8a59PQQLqQswOw1yDKiJPPVT1RSOAElGRjKqEkapY8cwtC_NEHD981XERpBBOndIO199KGUDsC8E857aZl6FE9mJKbEghT3gTt7BcSTR9cNItCcnO8xpmkILDAYM3H2Q1S23EWZTs1uvIhMLVGblk0fPgmldWJH7fTdigHwks2ktJaOM3tu0rmEtp4RSCGlafwrY7oEreB2h-6uKaS-DtlCmcZDVzwgiP1XL8W-fOkmTiCE3TT2QyeWa53vh9nW7rm1XLcp3_IVb6bFrz2d-mOk_HlSGdliuuWkx9hqqrrA3o9WkbKDsNuulE3_QPglT59qQ.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
