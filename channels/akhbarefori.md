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
<img src="https://cdn4.telesco.pe/file/eoeNUCF0Uvh3RCp8aQpxbBrAIPMFCLpXN8oZ1WYxw916wnxdxdNUc573-oOesFzKZ4hoQiYb34mm7mYypWOL8e4kap6xSkkqYSIz-GPk3mZ6BlEEd5gd0uERoycWGVe1K5Pai4YkTT38LWR490jXOuorxj0UxVC5-iB6hfFjnYJLPcmwzngT-AMCObtmDYY4gtggwIOWZNwlWHlG8rwH_csz8ZzLAWCVctzkBbEYnf5f2yB-XTyBFQVilG7QilJ15GkqaaZk8Q4b2PxxvEsqHJyQGxWxJLNP72dEOfyhjWtohOD-HAEJqFj-YVMVrVSBgJnCz9iZmyIqi50u90dR5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-693174">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تصاویر جدید از حملات با پهپادهای انتحاری به تجمع‌ها و تجهیزات متعلق به دشمن سعودی در چندین جبهه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/693174" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693173">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
انیمیشن لگویی هیولایی که بر پایه دهه‌ها غارت جهان ساخته شده؛ اکنون به وحشیانه‌ترین حالت خود رسیده و به پایانش نزدیک می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/akhbarefori/693173" target="_blank">📅 16:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
یک منبع آگاه: عباس عراقچی وزیر خارجه ایران و هیات مذاکره‌کننده همراه او احتمالا تا روز چهارشنبه در نیویورک می‌مانند
🔹
پیش از این برخی منابع خبر داده بودند که پس از نخستین دیدار میان عراقچی و استیو ویتکاف نمایندگان آمریکا، کارشناسان فنی از ایران به مذاکرات…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/693171" target="_blank">📅 16:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
اعتراض عراقی‌ها به توقف پروازهای ایران بالا گرفت
🔹
«پروازهای ایران را برگردانید.» این مطالبه حالا از بصره تا سلیمانیه شنیده می‌شود. توقف پروازهای ایران به عراق با اعتراض‌هایی در میان مردم، علما، نمایندگان مجلس و چهره‌های سیاسی عراقی همراه شده است؛ تا جایی که برخی هم برای برگزاری تجمع در بصره و نجف فراخوان داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/693170" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYoVqP0TgqQ2MYe-WnzINzlizoLVVJi0veZZ-fqfUNQzY9h6w6a2D6MW-uJFE5Fa0ymPoEvxhHz15ixoaDCAZoGoxK8hG-wJBuQoqI-Xry9NgrQ-9M_Rp6ZaL74455aM7UvD-B5AJQkX4n68h52avRZzZUvV7Hjc50-6Bbd-fuPfs1Zl8Y0VypXXWsZTeQHgl1xKS8araIaw3yEEc25ujN_vjCJAmmx8Oy9AIj-RrWjIf7QXW6p2l2_UAACr8jBUYZv4ajn6oRWeYIR3Pb6fUNi83ciYc_HAYJ79Sll08zt-t4WZlzohCf0-cxdIgUW_N2dfebRtX6_clo4gPzmAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت تیتر اکونومیست
🔹
قبل جنگ با اشاره به ایران:
ایران چگونه پایان میپذیرد؟
🔹
اکنون بعد از جنگ:
آمریکا کی از منطقه میره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/693169" target="_blank">📅 16:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سعید آجرلو، عضو کمیته رسانه‌ای تیم مذاکره‌کننده: آمریکایی‌ها در ابتدا پیشنهادی برای توافق ۳ روزه روی میز گذاشتند که محتوای آن عمدتا از جنس اسلام‌آباد بود
🔹
اکنون ما آن پیشنهاد را اصلاح کردیم و شروط خود را به آن اضافه کردیم این جمع‌بندی در کمیته مذاکرات در شعام انجام شده؛
در پیشنهاد ایران، از موضوع لبنان تا پایان جنگ، معافیت نفتی و لغو تحریم‌های جدید و محاصره وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/693168" target="_blank">📅 16:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJTo68GzHPsuXLmmU0CAr1TzWWkq2rmRRddnojfr7G0ga48IjhSOOY1Go30LR9COHv3owqwPz5zbGnfEekejnUY1cAvle45n0DqOEQg_Ot-6o-9NuJL0YvFYBpJI2yNMF4ozVKa7Rz3clw6AdQrj0w2-uKJYic26Jr5wn_UjMRTlWfz7ek90qBh5bkec8anDLP-dedQvQfrLR6SZ2iEVfZptWF3C0N9PPrsNiTzG7UBIDd080v4AJT-ZSJvm3Dw_ASj4bglOkyL3gvCQibcvZdOU839PTt8kAePtKrWUTn9d9X0qgGqUA-3NoX6uIi7aEL7v75B6KhOvzVpPOjBs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه دبیرخانه شورای عالی امنیت ملی درباره برخی اخبار خلاف واقع در‌ موضوع حمل و نقل هوایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/693167" target="_blank">📅 16:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
باج دادن به آمریکا هم جواب نداد؛ دلارهای عراق نرسید
منبع آگاه در بغداد:
🔹
آمریکا با وجود همراهی دولت عراق با تحریم هوایی ایران، از ارسال ماهانه دلارهای نقدی عراق خودداری کرده است؛ این اقدام به افزایش قیمت ارز در عراق منجر شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/693166" target="_blank">📅 16:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160941dea.mp4?token=kHZvI6yxDrdPMc-BcQZe4Hbmd-F-UYN6zAj0LiI6j_Iq-uOC-uX4I6fJ-huveQSEgzpLIabeD6zMWG-2VmBmNAfs3wCFuvLU7K2Y114TM95TnH3RXOhIuVDa9rHHAmGSbcL2wNcW948GE-y6oP7XITeXjzI_epyD9FjKSNXfUHKbBDB_rDgOay3t6D9z7kow3OEUkPu9NP8U0-UzthlUc3RtppX4RA51ua4RIOGprj0cWdgAehjMw6PFcryux0Q22eg2BD6CVJCNAH8F3zqZQwUJgAWAWtWoZkytNr4YQ2_nWNzQQARfvrQRvwgCYpfAPllTuGLQqRZYJ-Up_HZAyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160941dea.mp4?token=kHZvI6yxDrdPMc-BcQZe4Hbmd-F-UYN6zAj0LiI6j_Iq-uOC-uX4I6fJ-huveQSEgzpLIabeD6zMWG-2VmBmNAfs3wCFuvLU7K2Y114TM95TnH3RXOhIuVDa9rHHAmGSbcL2wNcW948GE-y6oP7XITeXjzI_epyD9FjKSNXfUHKbBDB_rDgOay3t6D9z7kow3OEUkPu9NP8U0-UzthlUc3RtppX4RA51ua4RIOGprj0cWdgAehjMw6PFcryux0Q22eg2BD6CVJCNAH8F3zqZQwUJgAWAWtWoZkytNr4YQ2_nWNzQQARfvrQRvwgCYpfAPllTuGLQqRZYJ-Up_HZAyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به روياهات فكر كن!
اولين قرعه كشى روزانه جوايز ديما؛ فردا يكشنبه
🎁
جشنواره جوايز ديما(شعبه ديجيتال بانك ملت) از ٥ مهرماه شروع مى شود.
💎
۲ جايزه ٥ ميليارد تومانى در قرعه كشى نهايى
🛵
١٢ دستگاه موتورسيكلت در قرعه كشى هفتگى
📣
و هزاران جايزه نقدى روزانه به مدت ٤٥ روز
mellat.ir/dimadream</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/693165" target="_blank">📅 16:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxZEI17BnpkWPHItxoc-sqXEHlglJ1n0HuWAA-VJRDm23cgQdOhjXS_oCQjxfZUNXVeJTFxAflYc914CEGTQg6i-Z_3r1QJAVIKLRLrPSk5wvr6GuI7GNnqx--tsXVkQo3unM5UG7pXVR1bucrZYM6tA0GLngFy35LpLpeEQBKuJwQ-xQ9RcswEVmxaIxlY5pyBx8yqUabrhBKegxK2hI7IHCGPXtDo0rC6aOg7KBMEca1-i90-zdRhexFfZT4XecYxo4LPkgh7orsEaaAZqtEQms-oYnYOGfc2-v4-ViIqlOyc6PVBRK86pOq0ln2kRnG0S3oKqCL61-4u8ENPm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گذار ناگزیر از بانکداری محافظه‌کار به بنگاه‌سازی توسعه‌ای
🔹
امیر نیک‌رویان در تحلیلی برای روزنامه شرق نوشت:سیاست‌گذاری در اقتصاد امروز ایران، دیگر انتخاب میان گزینه «خوب» و «ایدئال» نیست، بلکه انتخابی ناگزیر میان «بد» و «بدتر» است. تداوم روند منفی تشکیل سرمایه ثابت، به‌ معنای واقعی کلمه در حال بلعیدن امکانات تولید و فرسایش زیرساخت‌های حیاتی مملکت است. هم‌زمان، با تشدید محدودیت‌های فروش نفت و تنگنای تحریم‌ها، شریان درآمدهای دولت به‌شدت در حال انقباض است و نمی‌توان به نجات اقتصاد از مسیر بودجه‌های عمرانی و دولتی امید بست. از سوی دیگر، در محیطی با نرخ واقعی سود پایین و انتظارات تورمی شدید و نبود امنیت سرمایه‌گذاری، افزایش اعتبار الزاما به سرمایه‌گذاری مولد ختم نمی‌شود و می‌تواند تقاضا برای دارایی‌های تورم‌پناه مانند ارز، طلا و ملک را تقویت کند؛ مسیری که از طریق فشار بر بازار دارایی و نرخ ارز می‌تواند بی‌ثباتی قیمت‌ها و انتظارات تورمی را تشدید کند.
ادامه
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/693164" target="_blank">📅 16:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4tu-b-UAH_DtuCCNKef6glIkPmaZvtzvnbh04IJGOI0GKYcP0dMgKhlfLqcaHYGxC82HLcgvqfc3aOVaPWAclZOCCAiD2X6kebXJotfsqT0i1dzUeRRmeaSGUXOCmTKuuy8IzO0zCV5RwleD615bh49XXrydpl1-rkvfvAQlvCdJ7EkL0-yo7LgM7wyFPnUYu0_b57gW-hhapP1A_iGnSw17zHfAUFxx0qjwN4UGS507yYPb5QqI1uVRLIjesmMWtMYI2RTgo2_Fmu3H7tU4WvUzDneOiApC7vYvEX53ERIa1G1_Oe3jCecC7BPZJaBkjrRov04foYpiOiEtvzc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صحبت تکراری ترامپ: ایران نمی‌تواند به سلاح هسته‌ای دست پیدا کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/693163" target="_blank">📅 16:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693159">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0SKd5gIVqeG1ZXReTNbrw70Yh_XFqU3ArsiQA3bmAZgbzoyTtnfyOPUrFSOh_aD5Q7HXMdboy13uThuU0nO__C-NKfIMOuWez5uQhF6Rp29dIAYTXN8fUKzWZHFJBquNWxMz-02GhrzE6rrHKo2S15CIt8EXghJtcDTvqFkMj_zOVTlV25VIGpA-laSjK3Wl3A9vi404AIVmabTKLGRjbdNcorXc3bbdIo2r870x5YUe2tBJ0qa7DF2heC8yDgB-pUycj29XspuJ8a72JMBFoEZKpdOS02HCH1r3f9bNMeKWRYvyuqukc9V8EctxEyEHEfJK4dcV95yvFTW2yFsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y23KZlUAEvh_1iTe-4lyT-J00_M6ZPqMFMrxZ-nWZWbSPPBzAG1hOgJtYmfs16i8PXWcgPyczdCFirmKEDn4FH01UegOQsBE-uRCrA9kyXfg15dnFS4WOEX-KUqMXcH8PKTsvkhlrWMXo1xOMTqFA7-fHAZFDdnDSYmeEXaqO3l6YB6EVb1-h6VxYeHvi97gsOSJNP0gauREEwVVSZFbxy_AC4ofol_Q7M2w78f9f39uAYbZkAN7AaDbWU_Y3gZSkTtJLPB0U7SoPUeLvrlQIi-dAWwm34mOj0oJrv6HxjTcfpRb2JQUuKOZwIR4XXFETiAe4wQv0B5WXY13Q-kXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1L1YJ4WPiBaHJu-nj8oJhO5EKbylYLuL1ro6wjwiNDOZWQhcMPWYDkY0nSKlnUjxseTQG8Ld2_HgIT0XEvk_0wLp9otYTWI0e6KxX_nODQDjNn2xaV7Rkt_twojVkwwe0XeNBPD2lOhT1ZOPEaj_CQ6-yJIULCXLgfo77AthF1qAckKQrTldff6E6kDipHs3TDiGd8ycFFxrlfwLg5_j57O4XNeqxa414v5M_R4KMwcgrVxXjOlpHMRjbOPmmQq-BiJAAWoc15uQtOTSknydqoftyeMwap0cYSifcEd2BxPElR2lmRpAOJjlAyswW7_cJTTE3g8z4kYdKOYUQ7WgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYT76h3jzNy9g96KDYRh7Yyy9nx567qNYQjocs5ZQDB_EWHMEZ4aOVnCeJ6KwSoH8_C43ZsHaz1qSP8q7H20581Artgep-4HkL1d3HqDZljq44GLbQJ1lqh7ERnwUca6epPbhYhvd95bZECe3IexBfqzs6HuD7-MBuGblgdKg-tbnrd3ALkLEJm2yYVNc7rCGTpr0zmYXIbvIuhZgspUQugZFYZUyqt8xmAQXfGpu3-oRX_G-Sp9hfr4ropTOSMVUT-GaFy5zatoiEe5WbRIn9IJ08Q7lLD2LzaCxjCs10F0YON6ztwmmKMsax8W_Fn7hhDtTVRErdNEi0fOLTKmcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴ مدل ماست خوشمزه و متفاوت؛ از ماست لبو تا اسفناج برای سفره‌های رنگی
😍
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/693159" target="_blank">📅 16:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693158">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
صداهای انفجار شنیده‌ شده در جزیرۀ خارگ مربوط به انهدام کنترل‌شده مهمات جنگی دشمن است که از قبل نیز دربارۀ آن اطلاع‌رسانی شده بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/693158" target="_blank">📅 16:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693157">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ایزدخواه، نماینده مجلس: تحقیق و تفحص و سوال از وزیر اقتصاد در مورد سهام عدالت استانی کلید خورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/693157" target="_blank">📅 16:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693156">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
رایزنی‌های محرمانه درباره پیش‌نویس قطعنامه فرانسه درباره تنگه هرمز
🔹
به گفته یک دیپلمات سازمان ملل، پیش‌نویس قطعنامه فرانسه بر آزادی کشتیرانی در تنگه هرمز، رعایت قوانین بین‌المللی دریاها و عبور ایمن کشتی‌ها تأکید خواهد داشت.
🔹
این دیپلمات همچنین از رایزنی ترامپ و مکرون درباره این موضوع و گفتگو با کشورهای عربی و ایران خبر داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/693156" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693155">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: آمریکا از بریتانیا خواست مجوز فعالیت بانک «ملی» در لندن را تمدید نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/693155" target="_blank">📅 15:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693153">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-text">🔹
از وعده به رئیس‌جمهور تا عمل؛ پل‌های استان هرمزگان به مدار خدمت بازگشتند
‌
🔹
از گفت‌وگوی تلفنی رئیس‌جمهور با مدیرکل راهداری و حمل‌ونقل جاده‌ای استان هرمزگان و تاکید بر بازسازی و آماده‌سازی مسیرها پیش از آغاز بارندگی‌ها، تا تلاش شبانه‌روزی مهندسان و راهداران...
‌
🔹
۵۵ روز، شبانه‌روز تلاش کردیم تا شریان‌های حیاتی استان، پیش از موعدِ مقرر به بهره‌برداری برسد، امروز این عهد با حضور وزیر راه و شهرسازی، رئیس سازمان راهداری، استاندار و مسئولان استان به ثمر نشست.
‌
🔹
روایتِ این تلاشِ جهادی و حماسه‌ احیایِ دوباره‌ پل‌ها و تونل‌های هرمزگان را در این ۶ دقیقه به تماشا بنشینید..
‌
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
#هم_راه_مردم
#دولت_پای_کار_مردم
‌
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/693153" target="_blank">📅 15:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693151">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl8s4PYDaLIeH2e-BPUxeWZ7OJC3ilyuj5byIq7Rez_EnslMGlo4fqf3xVNHBrNuI4R7prxIrUAO__gTcl4BYaZLw68Nauy4hBwAVZxCL7Hi6cuXklcmbMFBYDCUbRvb3VS3S6joZHSb8uetmQgDvssaPSJ-sgWTWGY6mRXXeH24iLV31b1-6NjGFxbflelK4qdkLhvxmkz_TStiJEky31BDjZC1eMmCVuniRxpHflP6oBO9eYW8Lia09YtayxL77uBhuKFdHZJGnBc7j-_S32szThit4cLkf6LlpnKHCIXnhowoEE0CdaN3cyjedbAh2DO0yS2nZWV4_h2hf1-sQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40347efb99.mp4?token=cwkDMDAlNlUAe4aTfRcspssHQyuiwREpGrMBj8G2Oq6D0YqRcDqpx_DGfwxxl6Otg735VjokrXiLuWjqw2WuGQ2sfDqM9nuE9VTj_oVQfOX9YlMoclPmQtTq7kaF7R4Wcv9juDvG0SC3abLFELr01n6VEBawPQKbezdD9lxfN8Ix0I6i3_2uvoAZ1yv-n0TCTiNQ-Ncx9wkAW4TP1P0k0EKIIOpfcJjaea3-3-7csbxgbhic2tnEEbqKDRRb9J0S6FnOLceA1_XljEHs9YpeErKH6XgiVozHg3SLs-J-nCNO51EAnWBSshe0PXChpNTeGElwo1YtmiImWXeK05UOZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40347efb99.mp4?token=cwkDMDAlNlUAe4aTfRcspssHQyuiwREpGrMBj8G2Oq6D0YqRcDqpx_DGfwxxl6Otg735VjokrXiLuWjqw2WuGQ2sfDqM9nuE9VTj_oVQfOX9YlMoclPmQtTq7kaF7R4Wcv9juDvG0SC3abLFELr01n6VEBawPQKbezdD9lxfN8Ix0I6i3_2uvoAZ1yv-n0TCTiNQ-Ncx9wkAW4TP1P0k0EKIIOpfcJjaea3-3-7csbxgbhic2tnEEbqKDRRb9J0S6FnOLceA1_XljEHs9YpeErKH6XgiVozHg3SLs-J-nCNO51EAnWBSshe0PXChpNTeGElwo1YtmiImWXeK05UOZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چاه مکن بهر کسی، اول خودت دوم کسی
🔹
در جریان استقبال ترامپ از همتای چینی در فرودگاه، واکنش رئیس‌جمهور آمریکا به صدای شدید پرواز یک جنگنده حین پخش سرود ملی خبرساز شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/693151" target="_blank">📅 15:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693150">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEIl3zlPB63rxZTeKPwm40mGw_1YO9UetIu2fC4pJeyvSZ3YydRbqyFbF-QlY0JC3_dXenIVxw8Wqou6LTK5dD1aZCd21N4x8m_7CPW5c0eIBOOGyv5oG4zpe5RhW5kWq_eRGK-TkWwtrlcM0QUrQAlI82jXz5t78ccU-KPweg13Gk7KZK5P2zalmdJ91dl2LIXNPc1dTzY79fCA7Gt3aw4uS-0u8TE_ppURjH79F2CTBFeX75Hhg17UiFJMJqNr-rja8u15RzfAsbUWvQnKCSCyXvmBZcCdmreStK5E_c-r023Xkr1YOyrwwhiih4V3yim3Bu6xxKR3rYiv-U2GcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد روزهای پاک کلان‌شهرها در سال جاری
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/693150" target="_blank">📅 15:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0zjtbeWsSkd3XsKfQn9m47beMlunqz5gVVC_LLur0wBF8EY9qRwufFxNmVAaDrxPUUZIrf-VFfCrtItvJlAkruyKjtDBDv1uw4X50TgQqUlHAmTI8z-Qn9SUKvMmqDkFLG-nMeGhF8Ijw4LRMzvdVhrlxMaJuI_zYJh3LR4o_4aTNlVUIuG3ntS29HKMt0fvYj2ufMzWuuF99qdcw0yNzsbgAbn-G0WFw2yOrkWJevQa4cXVdP2XypFEHZQMmTCPAOVvleAdvZ60Yc9BgZpmNXLhlRxnQ0szS0poFd9iSnnf8rYLwyMHMrHowTuhz6dXBmUJepRAJi34ZcNKDkMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای هر مشکل پوستی چه درمانی مناسب است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/693149" target="_blank">📅 15:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حمله هوایی عربستان سعودی به زیرساخت‌های غیرنظامی یمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/693148" target="_blank">📅 15:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbPHb-JD-tduAlgl5MBR9pVQ4bj6AFlAKqb_Zpht1JXwraANT8t2kZBIoLyB1xB1CNiBUTOYdUrKUCpVwxWYq4244q_ruvCCSsbnkpebNy_BUXZ5gClEa3npaNK_0TPMfOA8I5zR63UWiW_GHoH2szwSO0uHlR6olQF0AOzwcZ8zT-M1cC-Na-DEAYmEeQbZ0Nh_tRPDPQpc7DkuUnxd1A-NGW4bCxckTcODae4hFNORaOt4FKwALCKr19r7ojflXMBCWu8Mv7KelvdiZQzJNMYFnHFjzW-5eST8xi_SYGJC1ot8f7VY5xWXD88LiqG-w6EoajTiXbs7LhCNIY0hpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/693147" target="_blank">📅 15:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QelY0bxNODLkvc8GQpDXgT2ujMZVA-jPDDPlOZnaFAeXJlpEqBIgUHev33dVyCakX-6JjTvKQ9nTrYPz9mnqRNI4x0WeLOB8BqG3I_gP6d37VRnT2GD444rboit087D5BYhEZkkObqb2XAbgVETQq2GBhuwONRyms3UIN4zc3PNeCXSsB5E5TrRe9j2NeMcSGrxUFDWYXugto-FGMMsS9q0u-yebe3eO3V4-BLw8X_FiJuqusGPB5wloKOneBD8gXUlu7UrHq94ADpwQ08EQjRZOnvH90CPaGIzD9u2rcVeQC3m5c1M_JIGoYdUpL86YlPS8dd4JQjZyAvWhvCEh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه میلی به شعام: مشکل نبود طلا نیست/ موانع تحویل طلا را برطرف کنید
🔹
شرکت سرمایه زرین ماندگار (میلی) اعلام کرد معادل ۹۶۵ کیلوگرم طلا مربوط به تعهدات این شرکت به کاربران، به‌صورت فیزیکی در خزانه‌های امن و بانکی موجود است؛ اما به گفته میلی، محدودیت‌های ایجادشده در فرآیندهای نظارتی، دسترسی به این ذخایر و تسویه بخشی از کاربران را با تأخیر مواجه کرده است.
🔹
میلی در نامه‌ای به دبیر شورای عالی امنیت ملی، با اشاره به مستندات نگهداری طلا در خزانه‌های امن و بانکی، خواستار رفع موانع و تعیین تکلیف فوری این ذخایر شده است.
🔹
این شرکت همچنین اعلام کرده طی ۳۰ روز گذشته بیش از ۷ هزار میلیارد تومان تسویه ریالی انجام داده و بیش از ۳۶ کیلوگرم طلا نیز به‌صورت فیزیکی به کاربران تحویل داده شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/693146" target="_blank">📅 15:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
مدیرعامل شرکت فرودگاهی امام خمینی: پروازها به ترکیه، مالزی، چین، پاکستان برقرار است
🔹
به‌ جز پروازهای لغوشده از جمله امارات، عراق، عمان و گرجستان هیچ مسیر جدیدی برای لغو پروازها اعلام نشده است. پرواز به عربستان از قبل محدودیت‌هایی داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/693145" target="_blank">📅 15:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693144">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
یک منبع آگاه: عباس عراقچی وزیر خارجه ایران و هیات مذاکره‌کننده همراه او احتمالا تا روز چهارشنبه در نیویورک می‌مانند
🔹
پیش از این برخی منابع خبر داده بودند که پس از نخستین دیدار میان عراقچی و استیو ویتکاف نمایندگان آمریکا، کارشناسان فنی از ایران به مذاکرات پیوستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693144" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693143">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
عراقچی: مهلت هفت روزه به محض پذیرش پیشنهاد ما توسط آمریکا آغاز می‌شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693143" target="_blank">📅 14:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693142">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555a41deb9.mp4?token=KBunO1HpsY7gkdkHYqyeMfDOoKNiIz_FlshVfPwGICN9kHkQmyN5Mu3Elw8GYhtznhkY87IQ01NkNz-XT4q0efQG71JLsMw1WIu7IQHBQQv7tDgcDjwLjds1RusUBPf7vc7nuZB6Svn8ATyC3tlpFbxD0aPlgCByveVSwPE1qmlvjuSy2JwK6-vsrNk304P2xzLkPgH-PoeD76AqR0EAWM2Dz48MThUtgk4nIyhTcq70yif-y6ps44a-IqLjUH8jQ0jMkyhHDyTgpJ961RH9gYXGQ4sLkGIsQABh06lwePKqyIhKCDqxgtKjkcveQzndneP6byBjHhYznEPzrEaCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555a41deb9.mp4?token=KBunO1HpsY7gkdkHYqyeMfDOoKNiIz_FlshVfPwGICN9kHkQmyN5Mu3Elw8GYhtznhkY87IQ01NkNz-XT4q0efQG71JLsMw1WIu7IQHBQQv7tDgcDjwLjds1RusUBPf7vc7nuZB6Svn8ATyC3tlpFbxD0aPlgCByveVSwPE1qmlvjuSy2JwK6-vsrNk304P2xzLkPgH-PoeD76AqR0EAWM2Dz48MThUtgk4nIyhTcq70yif-y6ps44a-IqLjUH8jQ0jMkyhHDyTgpJ961RH9gYXGQ4sLkGIsQABh06lwePKqyIhKCDqxgtKjkcveQzndneP6byBjHhYznEPzrEaCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه کار پله برقی از نمای داخلی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/693142" target="_blank">📅 14:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693141">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
درخواست عجیب «بیرانوند» برای بررسی پرونده پزشکی‌اش در کمیسیون اعصاب و روان
🔹
دروازه‌بان شماره یک تیم ملی و تراکتور، با هدف تعویق خدمت سربازی خود، درخواست تشکیل کمیسیون پزشکی به سازمان نظام وظیفه داده است.
🔹
طبق پیگیری‌ها اولین درخواست بیرانوند، ارجاع پرونده…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/693141" target="_blank">📅 14:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693139">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhThGCdNmLgqbOyubvZHMPKrO5Ic5KgTfFx3d85A4s0qnZOob1YUBVl6wn-xGEFbrf5yIFRVrCzAXzpwqAwKt2USVBK98CZ97F1a59h9mWw5ikQOQI9VjcYbcRLXvaHHqvDVT3TWw62Zjz80Jab9RLCq91zYeary4VL0_tWmDgBie793iSwAK-KAq7Clr7oxYSFfLE_ox-4l-WA7byHxiRAyI2OuZc0XhkKhOekSffbu622HmqnuRT4857m-41djIgZ-LCny-65ybMq-KubJRb9ggUIY2uvpFJfcnb3EYdRWlwwIecdKPDfMxZxh9NFugQI0aba0tVI8bXk9vgdz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZuskrdIxwBlElyrN7YRSpNOQ2hkI7Ozd1bKDNMMK8NL1CVyBedpWD9NWChFToMArRbrOxe8jsfs889JuUddNnbomohRF9Auk_Nfy3UALexW5X-znFx8BYtc8CHROOyJ_A7ZDTHtZ2C1tPovb09MoO7eyF2sT3Msm_lXWPZlC3veH4_ixF1Z0p6DgZjZxg3V8jnsvspeBnOKvRIGk-P9Xd10Pv80YTjLckdoL7CqiY4f2j5mcY9q5Hz2E9Vwfl7QG5HKxqT4sJU7wwrOTBDwntkznwEyWehqLTzbuWnSjtuOS8a9VKRElXzMWUCQxz-qFJdWbvlAMtcXKI8F-D0eqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شاید باورتان نشود، اما در این دو عکس هیچ اثری از فتوشاپ نیست
🤩
🔹
ابرهای نادر استراتوسفر قطبی - ایسلند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/693139" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693138">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
مکرون از ریاست جمهوری کناره‌گیری خواهد کرد
🔹
امانوئل مکرون، رئیس‌جمهور فرانسه، اعلام کرد که در سال ۲۰۲۷ به دلیل محدودیت‌های قانونیِ دوره تصدی، از سمت خود کناره‌گیری خواهد کرد، اما احتمال بازگشت دوباره به ریاست‌جمهوری در آینده را رد نکرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/693138" target="_blank">📅 14:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
پزشکیان در گفتگو با شبکه الجزیره قطر: ما هر وقت با آمریکا سر میز مذاکره نشستیم شروع کردند به جنگیدن و حمله به ایران؛ سه بار این اتفاق افتاد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/693137" target="_blank">📅 14:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858ef3041c.mp4?token=hLtteVciyRSHE7Odqga6lKDs9Fsl15v15ofHu0yfm3yfixR8Xk9Zl_O_80N20WiKnsJTs0__chLVei51zp9GyXjmCDPoAFEeCtAUh__zFNwcS6XHZ_N03qt3qGHyZiF5SIZao-mX3Z9pw2yfm6IXDJd75s1Z6blgxbSc-925WIMVbLoIkQ4MJi5uup9kq2PYdjYeAxJ1OWscX6Cyey2gFzxBDq_Ibv8sIbfkVyERLrFbrtLKarEEHt8ESwF18gGj2SRc2y-TrqIHOgkQo5I8EbHbn2gzFk3ILpslMv4daHWI_tMLUTei0l0qiVlqpyBElpYLEgGXJtrDLpGGqF6ztA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858ef3041c.mp4?token=hLtteVciyRSHE7Odqga6lKDs9Fsl15v15ofHu0yfm3yfixR8Xk9Zl_O_80N20WiKnsJTs0__chLVei51zp9GyXjmCDPoAFEeCtAUh__zFNwcS6XHZ_N03qt3qGHyZiF5SIZao-mX3Z9pw2yfm6IXDJd75s1Z6blgxbSc-925WIMVbLoIkQ4MJi5uup9kq2PYdjYeAxJ1OWscX6Cyey2gFzxBDq_Ibv8sIbfkVyERLrFbrtLKarEEHt8ESwF18gGj2SRc2y-TrqIHOgkQo5I8EbHbn2gzFk3ILpslMv4daHWI_tMLUTei0l0qiVlqpyBElpYLEgGXJtrDLpGGqF6ztA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: چرا و به چه منظور باید با رئیس جمهور آمریکا دیدار کنم؟ وقتی ما توافق را امضا کردیم، آنها آن را اجرا نکردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693136" target="_blank">📅 14:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl4CB8Ikf_I7W0Ed0grssp-UMPNAnmayL2GLpF5garF72pUR_weP7h_5bN_ywCrZIVBeUFOh8IlAwureVfeqc6A2zAg28EidH-_ktfYtNpl67dg32gaickxk5k-DDo75PIbxwpzHUN6vdJ_Mf3URz323qY2caksv5ANwTKWQ7pFd5N3FLFoTVIIQDre7ZT-7vxF5Kk_RyJS0dgYhuGbbU3JnziZ_B4g9T5hoSJgI4-DXrqNFGWuzRwm9gchPSERkm_Jbj6XSRjwaUbCLT-zwB6zgs5vPJ0csrpE_XvlJz5PIrB7AxcTmE3U02weF5DIPWxrSYbi2N9Ztf-8ZaubiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: با گران شدن گاز در اروپا، تولیدکنندگان برق دوباره به زغال‌سنگ روی آورده‌اند. پیش‌بینی می‌شود تولید برق با زغال‌سنگ در شش ماه آینده حدود یک‌چهارم افزایش یابد تا کاهش تولید با گاز را جبران کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693135" target="_blank">📅 14:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qr5UJjqjNiA8OZhf8fgNXaKyHJV5nE9uQEde8Q0OVCLTadAgHQ69Z-0KCQeI03DYbEY1lsvJ85kmtbYe5cDT1BwknhJVsvLBE3vpNVczj55aJKBL5U7Wl_XZ_dSnMrJllfxndWlOObWMCpElIpSFFaDPBjx-18frmjJ8bQUBuAP-uiS1-dU8J9cpBkesZfLTpz1RgJp4sLG2rrk2rvpNZWBADv1jiMuDHFvO9BbrNH_Ae3wiQsqIZBMVjWIi_WGTjkAPrq41Vy-WfYjvVO6fPz9ylwocOtcr3B9J-vDfh9ql9gpyuuZv6egWvjhOczLyz8Tymtm3e6Cpu-6OUOQhVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVU8nk7TmL_ETYS4M7adEG-hi0ObHuizSetK-1AlULdTcMlVuQVWrLSQbh2PmTvgO1PXEJvjieDdOl8iDx72LEBDXj9EJhDzCaOodfdWiFW7vDVfRJXYUwITr5BBf965hSkEmuE_vqLX8-XVBgmbywFSBT1yIqeu3cvl-vwS7n9BkC-pCFKVgm74TyNYVc95OZGxKFI0V_i7X97Y8Tu2qOv4_Yu3mPjrQeRfNsy6q7PGZsPg77Yk4dA7ZD7dsQVr8izA3qXfTVIoZFLBPiNqyUPdTSnMP8FHaq4f01uJuMraNrA7ELibL1F729znBO5xWb9efdHIt4ankjBi-0kKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bX3EBaN_6GUSPGxSz6qMMDc_FPrQBcwHJxvBK4hKVcLRYcpPfHutDeeRXiXkSJB8G8Dr8cJZUnC7d9XsfYml6tREehwjJFX4_wqS8JBx1aedMir4V-Z3rwfCW-TOCWA0OBaMaBegSM1laBB89tq81zfrGJiOYrFhf0qSB58QJY4E7phRzgGCbJTIRdbl8KtRkojdY9_WQhPuiQVHfwd0mochUw00w0b4zMFl1yFm5sn5A4Tsw7ZMJP5-YDGrZkyt_-oA5qqQBdct0zGsD-L0XoUsJ8PQEWDNF3IP_BoxtCjAqiTBgjVM6lM82flm8B2aiGXmDVhhUAy0cevQ2Q7QRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGmLoCUCjOueumPYp4jHslwBZ8MJTNq_AnZftAFO4dpyraL6VNwIxvCLI0l7r6dlV2AKwSyv9aMe0p6b4VEj1dbbzOFhlTPWVGRoqn02S8j8Gbur9m5s_xTrcs6f6VQRRPDsU1EfJlvOwh8fM-faZR_lmKr4iyaAPoEsHGXSAlgGRXDQQm2ou82vV2AKUrrAYsXXW7DEMjVQydLT_bYh4O57sIjZEd8zlK_9-3UjnycQDEK1j9bcf7ByQJOG55nurCLXpX4TgqbgDHfatr_5ZTQrWkRSw4jjzeciMfX9_L0b2aLQYVH6HsyvCZ1SzqFIWSNpjePoSgehgOnYWa5CCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmC7Fok6uwC1cw7Ds5J72-QWwOQ-dVZm8wzfYgOQuEwWE1vcj_TIKU2TqywKjMyq6wBmAVC23SIG1kxc6pusSIt2ZdDRmdvSTodLPLByyse1naOsX2TJu6PxY_mJ5aSHJK7Jp1jizmRdspSvpvaZ0fqWM0aPGVX-hBxNgAAng_va_h7Na6vUy0_QuUGyQ5I5J3Lk7XXYR9HWoAf1LbSDb0PfkTGNOmk9SywgzsqJc4nxTigUcXhH0kMsxWLuV5OnlmDKaeKv8u5dMeIR2WMz43WNMSPI4OmytuBNBS-9PV5Ky65kaDECtpuWNM3dAhjcd66TkcoVLvpLK-4L2wU9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkX1j_h-rB6w7IewhFacbVjgbX1Bzm1uTi12xtZV5PV9eQlFAHwqRRfoVr6X4Aq-PrAuOwe3mAcTdGGbCab5yz2fWzlaKhRfdObcBOP06oBhx-YW8aBK7EvbROVzMkwSCCDr31ucxirN2pbl8TMj_-YWh1yy31fHU7XVWTA9ZZeoqVUaqowk3y8eKvkSZBIASKNuOk_R4M661S10FTvFTHZSjdlmTm7di-_Oy_k2AAdTrsV8F9zC6gFOPiIVUk5NRZHnOyF6ZDtZnOSFQsBkJhIOMw_UTonx_hni6DvQ1GZihE5J56msigQHf-nTrAg_q7OuRXjCkigoUFBVSl6jVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
به هر صورتی چه مدل مویی میاد؟ یک راهنمای کامل برای آقایان #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/693129" target="_blank">📅 14:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBli2Vb_q0Bmm5Xk5hdEb-7Du3tUGn2KNpt5LiUP3ugJnfnA8ihVhymD1wPUKSskisIHevO_Y3AoQh9DtjF9vjrsYYaeG90jK6UsR3bMK3fcqNb2r0WYLCsRSOm58cUrzKaL7EeWeUeYPKvtaOHuCvxKRVSi3qR06bppd2lFl4fRzx8FeqoAkHr8avYcuYjBQKjk-TV7kK2jXF0xMWQKRYlViYQD97JBSI4YE7oiAehitGp1oSWR0EPX16JV_vJwrklR5IPL8rwA-qKwavGZWZp87YKQD16W4Ju7rB6Y4CKJ4LkQY71zR6lUb9_hVo0JYpTsnQyaDLbLGMxiPJW0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۴ مهر ۱۴۰۵؛ ساعت ۱۳:۴۵
🔹
معاملات امروز بازار ارز تحت تأثیر انتشار اخبار ضدونقیض از مذاکرات ایران و آمریکا، تغییر فاز داد و دلار با عقب‌نشینی همراه شد.
🔹
این سیگنال‌های متناقض، فضای مه‌آلود و سردرگمی شدیدی را در بازار ایجاد کرده است؛ وضعیتی که موجب شده معامله‌گران با احتیاط بیشتری رفتار کنند و خریداران از ورود به بازار منصرف شوند تا مسیر آتی نرخ‌ها پس از شفاف‌سازی اخبار مشخص شود./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/693128" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldkRmphFbaWBBkVXFiW0l1lXjV34mKqS0TEmi6Ic74Sd0RPkeE_sD9a5q0m49tg9elwmfVGsAS1jTcu_vLXXCdpxlH2FZjUTLCbJU0bUJHCjE98iDk2FvY04-qPyZmGSWaQhr2aIAGD992S3-N5EDugtSp4qt7hr-fF-MmDUxLEGxUL70g1ZNYLUSwMkHZWQGb1b4CyqHHLNmyvOc_iKf_jv19Lz5CIjHpyvsWSnNGKkhru5KTZoBz7xt62rICrmJ9sOOTZ7Uo8AFv3jk5Pafeq90fAX8v9D5JOipQzfhxcED8sgkCvcVqFuA2TZ71iLCoJ9rClz7Agb2F25agO3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان رضایت از عملکرد رئیس‌جمهور پیش از انتخابات میان‌دوره‌ای
🔹
جورج اچ. دابلیو. بوش، ۱۹۹۰: ۷۵٪
🔹
کلینتون، ۱۹۹۸: ۶۶٪
🔹
جورج دابلیو. بوش، ۲۰۰۲: ۶۴٪
🔹
کلینتون، ۱۹۹۴: ۴۸٪
🔹
اوباما، ۲۰۱۰: ۴۶٪
🔹
ترامپ، ۲۰۱۸: ۴۴٪
🔹
بایدن، ۲۰۲۲: ۴۳٪
🔹
اوباما، ۲۰۱۴: ۴۰٪
🔹
جورج دابلیو. بوش، ۲۰۰۶: ۳۹٪
🔹
ترامپ، ۲۰۲۶: ۳۷٪
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/693127" target="_blank">📅 14:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پزشکیان: من دو بار با مقام معظم رهبری ملاقات کردم، بار اول حدود سه ساعت و بار دوم هفت ساعت و نیم  رئیس‌جمهور:
🔹
ساختار رهبری مسئول سیاست‌گذاری است، در حالی که اجرا بر عهده ماست. آنچه ما اجرا می‌کنیم در چارچوب قوانین موجود است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/693125" target="_blank">📅 13:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693120">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZ6P2csVSb6xDGxbC5we2Zo166O3CjH7QPJnrElqc7RsOscXHGv0X7ZtW8T0tMaHPKDLUb9TUvlthzKFatkMRV1WLGfbAU5oICsIjllFXibnwpc4cth9ZJ5r_rGHDhDX7r7fMZQzRZ306YssQKQ-6MsrjjyoTCXuBzIMwuD4u9WMepd1Uqf91gki2J7uTGPgmZSOBzRw_SZc9RDhVJo_zeXUy8cqCt3yUHb1qSiNP8R1hknMzVcd-feQWvJUoTfxGvx0I_rl3nh0gr12KotL-WGFIwdkxrcPwTpPJ6GJiASJmtUABJgdOFLRcN4Cf9YxyeSQ0_nKcoHQUZq2vkQXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrwHZq5zrwh8-6EEnWno6fbz0NtrMSPWc10LggZEaf_Si1GOCFwV7z77b96Zae3opWwzfvEonUA9L5E4lZ-xEfCGnNTwUzZQ2f4CNR6euIXDdSEUotrzDsOQSbONKjjhJBBPxGeiuk7g6FX_nOTCd4g3pNFLHwNDiFCRK58GQKl2ce86DKkfmIzFsOoxxo6i3Fv_YIHCVdD7JU-9BKGtyD_PxmiIBOeWLWlQzyNHex455RoQtrgty1Fvbxo63BvWwYf5NVhz-4GWZwNMGDLdRCDuOLh5zxuAGAbI7RTrzLzu47jomDT6OuZKBeo6_D5JS7iMtffWoVNhnEaG9TOmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogWfSUnK5mxpDsWdjAYRWHvMI7E3tCsdf_vNq9Ppaty1qOn325U5Qpy0Ef-PoF8vv-yxQZImLXKgqIxJ3LNt6nPUg6oodBPYqU2acq7FbWlvGEKdGWyPXRqBWlcCPCuZgayDTdsRZOHX-cq6C9smiy4dZ5ES7jstZ51sphAErt3ydGueVbtPpZtvquDBs7Ym1s-OBBcLb-EYgUtv3ea9n595U_oQh9xcDNdsyMHxN7VGig6i_-nL1WJEWpYyuoj-X5BkOzRkHAnoFIjbsWAkhlhM2s7t7twNiyh7NkrE3JJsRLJVsQ2B5crxLuguvc1dg0FNMc-DtoL9wbfaoK_2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/be9g8zlBmsm-hVigyDIWtOvcjp8YBGuLIFtfmfx0dqxqqtON-Z2cuzV0j3gceWStzCxWSmFI64bKcXhvm1W92pTGXFNghkRdFDD9DKiAMKqLRPIRrLCvG79dl9Yb3TiN7Z_GvPbuoFXfKU2Pi5xCuMarPrThEKOC079eibywvxTeJtQqvhPaEBdJSO9icA6ioP2ndNUeJrLrWSpPn4oPL-ebNJ52kxPvarTRysuWGZwAvb79bCkbM29yU2-UaqofbMBXsiUM_EMyX2YpxM_DNmHLRouqRdHGGf0LxF6Y8uPIo4Bl7w_3124Ximh3SPjhfRrv2Am8s_APAeB5-dPtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjSLBUDa3tAT-8qppkmXu7r-VmMsj-5Tf45meLA_NchV2J9BuXSvdOq-yog5fSSWD9pVExVJRVDsWI9rhhfddD_ux_pPPFy0GBn9OIdXHEEay8RGvoVlspneKw0ATC5JH-6JC_UUauNHuvSgVSm2lXqavgxWnMLAZ-H5xw2ErRhDxAEwRPRGc_IFzR8-MfGHEaxANYYwe8z0BgzsBKJhdYgHnY-A84QiqdjrYdAYYF9YU1PoXgHaY6boueEPJsuZGMVT2Ysce5BHMZwjWYg7C6vKFb69UjHSSDQRq1QBYzPHIEGCeJ6Y22pn9BGyAi6bjVP7tR4IUGKMPtuaKKGNGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیائومی ۱۸ پرو با این وسیله جانبی جذاب به گیتار جیبی تبدیل می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/693120" target="_blank">📅 13:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693119">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTJct9kQlZj7I1euDGgl6dD8JuJFhucso3JNTOq1M7y53dJfuZPdEfl5K-uBp9GQRWqRsbr9bMSY-ZNinG9tjT7-Q-FWMF4Zx5MdusQFE6WCgJpd9Lcxluu2McQQvVzW3PLzQtlOn9diot9O4MrUIauKxSovi-G2SAsxrS7jdD_T1xDbqlZDcqEGFLJ-7V5Q9YUW0PNvVDQDlldlwX-MF9QAJzhnzKe2RfJnkAkKolShmtL4ij2HXiJoHt2K7ZVIkotrTUXlMQ2QYWwGKbw1NfSu0U7WUItIL3agnJ_d-GmOSiDsCl6iZRnqoU5T7E7lUVFxrirQYXj3__KFAM8Phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کبدی مردان ایران به مدال نقره
رسید
🥈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/693119" target="_blank">📅 13:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693118">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d806c987.mp4?token=Z_9U7XVO1awG72ptkmVxMMYoabC0RxMzWz6iHIqYqDT7tJuwNnzijCRS7FN0FoS-ae49MSBmB3oINzUplNs0vNDVYbxwB7ynvpeh8doz7IhhdWkcnMjJV9Ean0DUl9VN281xylbwhTXWDt1hvb7LKEfVel5WcsM_SarTSpkAUITJVj8t_D9myWZswituJRI80_3uJzIgF73Oa-XHnCroJbIrIvMGfYjonbEv-XlP0EyEALtcfxx1oaqA86JyCaOW3BurtkzRiQn6P-eVfAg-D8mfE6mk_j5OWg9NSCfVRlLrLee4_y_cRvP_bmgtpkW8fzX_zkQNl7sBtImWRhq2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d806c987.mp4?token=Z_9U7XVO1awG72ptkmVxMMYoabC0RxMzWz6iHIqYqDT7tJuwNnzijCRS7FN0FoS-ae49MSBmB3oINzUplNs0vNDVYbxwB7ynvpeh8doz7IhhdWkcnMjJV9Ean0DUl9VN281xylbwhTXWDt1hvb7LKEfVel5WcsM_SarTSpkAUITJVj8t_D9myWZswituJRI80_3uJzIgF73Oa-XHnCroJbIrIvMGfYjonbEv-XlP0EyEALtcfxx1oaqA86JyCaOW3BurtkzRiQn6P-eVfAg-D8mfE6mk_j5OWg9NSCfVRlLrLee4_y_cRvP_bmgtpkW8fzX_zkQNl7sBtImWRhq2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از دلایلی که نباید در طبیعت زباله ریخت؛ روباه فقط یک قدم با مرگ فاصله داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693118" target="_blank">📅 13:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693117">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
قیمت بنزین در چین ۲۴ درصد جهش یافت
🔹
قیمت بنزین در چین از زمان آغاز جنگ علیه ایران حدود ۲۴ درصد افزایش یافته و به ۳۹۵ یوان به ازای هر تن رسیده‌است.
🔹
بر اساس سازوکار قیمت‌گذاری سوخت چین، افزایش قیمت بنزین باید ۸۳۰ یوان به ازای هر تن می‌بود؛ اما دولت چین برای کاهش فشار بر مصرف‌کنندگان، افزایش را محدود کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/693117" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693116">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaSyYya7oWHyRBHSrJ6q4caRMa2AjWM1DduNYmu5wGN1eTeY1hRFneibilYUR_9rVhMjRa7hcaryoIDju4hi7q4w39gTn9hHWHw6sSJjL9_jcN9tFWnmWAFSyXm40Kh3osrGYv0WzGI4dW_LiEKBLako60j3PAWzrTatwTRph3-22EIMSKoJ2aBXwV1e-b5ge0eoVfIFwGI_jJSiVpvR7RQkO_02js34g4qrYS8PTtHkjg6BVRV0fnRzb-VVJB0G_9IWILaa-gbh56S1bCQM27ODuYZFuEgke1lFuuCa0hrZQp6yOIbeTurQ2TB7MYc5Rjq40nt4l6i_yXDYJt6VaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیرسایه پرچم ایران/ قطعه شهدا بهشت زهرا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/693116" target="_blank">📅 13:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693115">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پزشکیان: دیگر به مذاکرات با واشنگتن اعتماد نداریم  رئیس جمهور در گفتگو با الجزیره:
🔹
قطر و پاکستان در حال حاضر بین ایران و آمریکا میانجیگری می‌کنند و پیام‌های ما را به واشنگتن منتقل می‌کنند.
🔹
مذاکرات ما با واشنگتن بر اساس یادداشت تفاهم قبلی است و آمریکایی…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/693115" target="_blank">📅 13:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693114">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
دفتر نخست‌وزیر عراق: در حال مذاکره با واشنگتن برای مستثنا کردن فرودگاه‌های عراق از تحریم‌های شرکت‌های هواپیمایی ایران هستیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/693114" target="_blank">📅 13:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693113">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">💡
برق، سرمایه ملی است؛ نه ابزار سودجویی!
🔸
استخراج غیرمجاز رمزارز با مصرف بی‌ضابطه برق، تضییع حقوق مشترکان و تحمیل هزینه به شبکه، تنها یک تخلف ساده نیست؛ مسئله‌ای مرتبط با امنیت انرژی و عدالت در دسترسی به برق است.
🔺
مقابله با این پدیده، نیازمند برخورد مؤثر و بازدارنده قانونی است.
#استخراج_غیرمجاز_رمزارز
#صنعت_برق_عرصه_تلاش_و_خدمت
💫
با ما همراه بمانید.
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/693113" target="_blank">📅 13:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693112">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWc4EqA4OZMBDKWZcAW9d8SyNsWzEdI-TINs8hYxgiIp9k0qh3aQnHOEenJRnndolSs63btZOcYKRWhzbCwMa_Na5jzqXy0-HFrX1cktr3llmmg2e7jsWyA3I5ibQG8PgPpl7FiLx5CMjVmMvM9b4BTyu1QCFg9yRKasOmpzxyLe8tRTWN8G2sAGJNMlMhteLd4uA3OwsmeLIO4jCt2ofvSLQ_52tF16TxCEAD-e4sfOgJUc4itV2UKowMxuojzJk172RB_BvLT3ISg4Cwm9GrWXrCFXVTepn1sSEO_zPAo7t1K_aR7iPc5B5AEdKP6GT_j2Ch83kXP1-s3P8P6_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش عجیب از لو رفتن یک باند سرقت با حرف‌های یک بچه ۶ ساله!
🔹
چند روز پیش، همزمان با شروع سال تحصیلی، مربی یکی از مهدکودک‌های تهران از بچه‌ها پرسیده‌است شغل پدران چیست. یک پسر ۶ ساله با هیجان گفته‌است: «بابام دزده، تو خونه‌مونم اسلحه داریم!»
🔹
مربی اول فکر میکند بچه شوخی میکند، اما وقتی پسر میگوید پدرش هر شب با کلی پول به خانه می‌آید، موضوع را به پلیس اطلاع میدهد.
🔹
پلیس هم با بررسی موضوع به خونه این خانواده میرسد و سرنخ‌ها در نهایت به دستگیری سردسته یک باند سرقت منجر میشود؛ باندی که گفته میشود پلیس حدود دو سال دنبال دستگیریشان بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/693112" target="_blank">📅 13:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693111">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
پزشکیان: دیگر به مذاکرات با واشنگتن اعتماد نداریم
رئیس جمهور در گفتگو با الجزیره:
🔹
قطر و پاکستان در حال حاضر بین ایران و آمریکا میانجیگری می‌کنند و پیام‌های ما را به واشنگتن منتقل می‌کنند.
🔹
مذاکرات ما با واشنگتن بر اساس یادداشت تفاهم قبلی است و آمریکایی ها باید موضع خود را در مورد آن مشخص کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/693111" target="_blank">📅 13:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7017f8cf.mp4?token=mN8uKQ05PaPXiCkQ4GFJEC-zQnVVEGXLTffaQHG-L4s7qU7IVdJ8tA3zroPzp9ewk_WUyY7xj2VxCknzMaHD6Wcq7XK-2GW7cTVdchQSaJW9MSom7mBcOEgSKtO4U9OXnoDY4stwV5XmoXdeawlF3lLPqISYozsIX5LXqv9tbFLWFQE08LD4_umyWJSEKj_AE3gDcgKq7yOAZI8_j4-UHuu_bazmXQEc3wUayLo0qxuvgdRbqypoAJyO3065Kd8M7kOyVNTp73Y3JTccs5ycLURQ-elbBXdeYkjPZIuxZxXTTW6kJPCdml9geiasOk1qfljA2CrybVYURashXeP8wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7017f8cf.mp4?token=mN8uKQ05PaPXiCkQ4GFJEC-zQnVVEGXLTffaQHG-L4s7qU7IVdJ8tA3zroPzp9ewk_WUyY7xj2VxCknzMaHD6Wcq7XK-2GW7cTVdchQSaJW9MSom7mBcOEgSKtO4U9OXnoDY4stwV5XmoXdeawlF3lLPqISYozsIX5LXqv9tbFLWFQE08LD4_umyWJSEKj_AE3gDcgKq7yOAZI8_j4-UHuu_bazmXQEc3wUayLo0qxuvgdRbqypoAJyO3065Kd8M7kOyVNTp73Y3JTccs5ycLURQ-elbBXdeYkjPZIuxZxXTTW6kJPCdml9geiasOk1qfljA2CrybVYURashXeP8wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا حمل جیوه در هواپیما ممنوع است!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/693110" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8lGTNz3_U33I1QGL6B8TR4LiYcfG7GFail7VmoF0OkcwuyOWl7rh9fnCNuyAFGBpimjY9jXYzbcf9v9tRD4lxenwRnr-IpRqHI9thY9INJVpn_8uaxy3hhFFAySCHLBsBb81CjtxtxARDnYGbnVRenLYoY_EKm1OZRv-5fOC4D_hho8p_n4fEzFsJAALBXvgs_zdJ4Hql6Y2ccrZre7byAalCn27etsgOVLn2oiT3Ugf8MgtTDuN1S2nrcfkMfDW5QU4H_pDTe1Al9v43twqrnfs1YmKt07lOUcD5CCeBvMtDBbCFIcWaHvsi710onKMwcE0DnWrNQZeXidKvn8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهایی که زنان بیشتر از مردان به دانشگاه می‌روند!
🔹
بر اساس آمار بانک جهانی و یونسکو، در بسیاری از کشورهای جهان نرخ ثبت‌نام زنان در آموزش عالی بیشتر از مردان است و کشور گامبیا با اختلاف ۸۳ درصدی زنان در صدر این فهرست قرار دارد.
🔹
در این میان، قطر ۶۴، گویان ۵۷ و ایسلند ۵۲ درصد نیز شاهد غلبه چشمگیر حضور زنان در دانشگاه‌ها هستند؛ این شاخص برای ایران با ۱ درصد برتری حضور زنان، در حد فاصل برابری تقریبی ثبت شده است.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/693109" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693108">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f677f368f.mp4?token=kg2cYuTWX6BcS0oIIuPLdF0f6T40jTc_1Ogh9wob5jk6iNZskPU1PYrwqx7lWhCcLypkqvJDN8FmoscbIkPxzXVBOWQib3gKLxdtjcl45_GNxFoJ9u2V0cv7vJCe1SSE7W9gIDS8VdrHqF6VZQwaysyZeKkJRj2YYreX1XHdrHWE-2nsNSXbXPWFH9OkWbisJUUU0dlYNEV4KDWDGkD39rawIvO1Pzss2Y6LAoHhbe0EhwXEQks9e1UVNnwJcgy-AevFTBH51HmbpVtkW-UyRcYo0-bXINhl5Zk1KAmMHy9iaj5Y_hcVaFiccwI6d8jrvdno50kUhuj63AxpVu3OXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f677f368f.mp4?token=kg2cYuTWX6BcS0oIIuPLdF0f6T40jTc_1Ogh9wob5jk6iNZskPU1PYrwqx7lWhCcLypkqvJDN8FmoscbIkPxzXVBOWQib3gKLxdtjcl45_GNxFoJ9u2V0cv7vJCe1SSE7W9gIDS8VdrHqF6VZQwaysyZeKkJRj2YYreX1XHdrHWE-2nsNSXbXPWFH9OkWbisJUUU0dlYNEV4KDWDGkD39rawIvO1Pzss2Y6LAoHhbe0EhwXEQks9e1UVNnwJcgy-AevFTBH51HmbpVtkW-UyRcYo0-bXINhl5Zk1KAmMHy9iaj5Y_hcVaFiccwI6d8jrvdno50kUhuj63AxpVu3OXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیابی رمز اینستاگرام و جیمیل در ۳۰ ثانیه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/693108" target="_blank">📅 13:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693107">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce462ceb59.mp4?token=YIUqnuTJOP74Vn-oLpzOih35jGamAIv88i5CNGFCrEj2TXH-IOtKUg8zXN_AJJK0OGrwQjuyGOsJH0K0dNBGWdmdw3EmkWDU9OrQMJPKmlEpkeu1aXQY-4k4kFoRM1YL11rRdfG3G6njfxTtdAzUeZqFlE2WDSsbREYQef19ySr5i1lAMOg458q4w8GpVVlIap8IjP3E4PWETEM5IZgFzei414WGyldyN-5JSxsQgTfZYqEDhnddCsuQP_fjM6jP3gbi-vbEVBsaeEqKIGG0Ws6FF-NMiaxjFLdqZM-yPYFKVi3K5pBVkmF1-l4QXQh_Irpd0gHY5v7tPLDw9OakTBYzySx0LXRmf6eq77e8AUpVdFz6d9qQ56P3Ai9NXYMybaG8RkN--UM9CSfl7-O5TI2ih4ZDQAkr6MP60vDr5Y5vu6ycxr3gajDncPrIzDXQoVBNK3ndaV_JfePWe9f2hqhMePL18wvZrKnSdmF4YZCMWQyrR6nVC2wjGwHK_e8bN9azG04GzuUDEJKeWqVLfqTmYoagsooAri7-WdmI42f0QpKtPK69g3Kk77LrgJ-3VF0aLDQdtB-iXvJEoQJUuYJfBjxOdqjWjbnoF5z6KGZ3a-1MMaywWxc3cSGev1J_sTUAQwwhTNfcXs_ZiOetPZh5ZxIDV_O4VNiDUBP13aU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce462ceb59.mp4?token=YIUqnuTJOP74Vn-oLpzOih35jGamAIv88i5CNGFCrEj2TXH-IOtKUg8zXN_AJJK0OGrwQjuyGOsJH0K0dNBGWdmdw3EmkWDU9OrQMJPKmlEpkeu1aXQY-4k4kFoRM1YL11rRdfG3G6njfxTtdAzUeZqFlE2WDSsbREYQef19ySr5i1lAMOg458q4w8GpVVlIap8IjP3E4PWETEM5IZgFzei414WGyldyN-5JSxsQgTfZYqEDhnddCsuQP_fjM6jP3gbi-vbEVBsaeEqKIGG0Ws6FF-NMiaxjFLdqZM-yPYFKVi3K5pBVkmF1-l4QXQh_Irpd0gHY5v7tPLDw9OakTBYzySx0LXRmf6eq77e8AUpVdFz6d9qQ56P3Ai9NXYMybaG8RkN--UM9CSfl7-O5TI2ih4ZDQAkr6MP60vDr5Y5vu6ycxr3gajDncPrIzDXQoVBNK3ndaV_JfePWe9f2hqhMePL18wvZrKnSdmF4YZCMWQyrR6nVC2wjGwHK_e8bN9azG04GzuUDEJKeWqVLfqTmYoagsooAri7-WdmI42f0QpKtPK69g3Kk77LrgJ-3VF0aLDQdtB-iXvJEoQJUuYJfBjxOdqjWjbnoF5z6KGZ3a-1MMaywWxc3cSGev1J_sTUAQwwhTNfcXs_ZiOetPZh5ZxIDV_O4VNiDUBP13aU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی رسمی از فعالیت آکادمی آموزشی «آوید»/گام تازه خبرفوری در مسیر توسعه آموزش
🔹
در یازدهمین سال فعالیت هلدینگ تبلیغاتی و رسانه‌ای خبرفوری آکادمی آموزشی «آوید» به‌عنوان یکی از تازه‌ترین دستاوردهای این مجموعه فعالیت رسمی خود را آغاز کرد، اقدامی که نشان…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/693107" target="_blank">📅 13:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693106">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ4LKWT9b1L4xWE1DFaZYItBDBDqzB0QTQ-MmzIcoz-cfiVD0tRTzBYcSG-FLt2aM0obXd7jq3Cwj6QW_MpJsXSKpCloH-9JgjlPRfXQQXmrH73jhLWDyzJot5PSZkK8m-AYjPERkm_fd-YH97Kfvm3a53RtWBvrYyqIqnS7flK68s1MeLx56LlHML9HeURZ4SXF4vlYpdj_7uy9N3dzJ-oP6I-VdHE7BLI2AXkepLNg9JiWmAMIwzG9hWLTKFDCneUTzCK0SLqKGi96aQE38ZHjfFnWsqCn2P6Ahr8CJajF8Ji9JWko8pijrn6W2uBJ9PHdUW37-zc6A_GskPRz3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
و حالا در «مدار» باشید...
🔹
امروز «مدار» به‌عنوان تلویزیون اینترنتی خبرفوری رسماً رونمایی شد.
🔹
پس از ماه‌ها فعالیت آزمایشی، حالا «مدار» آمده است تا فصل تازه‌ای از حضور خبرفوری در رسانه تصویر را رقم بزند، با تولید، روایت و نگاه‌هایی تازه...
🔹
«مدار» با تکیه…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/693106" target="_blank">📅 12:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693105">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رئیس‌جمهور در مصاحبه با شبکه CBS آمریکا: ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد/ ما نمی‌خواهیم بجنگیم اما اگر بزنند، دفاع می‌کنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/693105" target="_blank">📅 12:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693104">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
حسن روحانی: اصلاً من نه کلمه رفراندوم را گفتم و نه کلمه همه‌پرسی را
🔹
بحث من، لزوم برخورداری «اهداف ملی» از پشتوانه مردم بوده است، نه برگزاری همه‌پرسی درباره دفاع در برابر تجاوز
🔹
اینکه جزو بدیهیات است که وقتی به ما تجاوز بشود، باید دفاع کنیم
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693104" target="_blank">📅 12:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
گمرک افزایش تعرفه واردات آیفون را تکذیب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693103" target="_blank">📅 12:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52665c934.mp4?token=bxK7w_KZ0UgOuBlXTn--xpZLuaV5CLFpdh2M7IBJTIQykON6x-HZUZrOZCSlFRZJSDCkgQjR8U73BDIwzVJG3_T4XofbvmS_YswGy0WHvuA-xD2-INdPWTnWd3sTzhfgkbMlt7xyuXzdnWuIlibIXBuEQlnNMpMHVxM7byvrJrSR_yLZnWoeOA_vrMk_L9TGU7SdVammys4qHx9C0YvC7BSTPSwug5irnuBvAG7DLLuuPD3vxu9L5PRl7xRTbPKTaWEJXe-CNoltn3q2UmeipqthVTM1ienV90-S4ng6q66Nf7JyXqMSimkg2142pF_AUK_S-khRacI1Ph00uUdtow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52665c934.mp4?token=bxK7w_KZ0UgOuBlXTn--xpZLuaV5CLFpdh2M7IBJTIQykON6x-HZUZrOZCSlFRZJSDCkgQjR8U73BDIwzVJG3_T4XofbvmS_YswGy0WHvuA-xD2-INdPWTnWd3sTzhfgkbMlt7xyuXzdnWuIlibIXBuEQlnNMpMHVxM7byvrJrSR_yLZnWoeOA_vrMk_L9TGU7SdVammys4qHx9C0YvC7BSTPSwug5irnuBvAG7DLLuuPD3vxu9L5PRl7xRTbPKTaWEJXe-CNoltn3q2UmeipqthVTM1ienV90-S4ng6q66Nf7JyXqMSimkg2142pF_AUK_S-khRacI1Ph00uUdtow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیل گیتس هشدار داد هوش مصنوعی می‌تواند آن‌قدر قدرتمند شود که خطرات فاجعه‌باری ایجاد کرده و حتی به مرگ یک میلیارد نفر منجر شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/693102" target="_blank">📅 12:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDh-55N8PnwLkUKWvDs9B87sRLVcVaMGEGfCTyCedKJqrJtjTFt9PkdJQt6TOzzsQS7BAqCleM5g1vKUVheiShNS2bymSkgyhY2K5HzWeY4MIJwZ0sHCdvxt7VCb8T7pvEixZIJ8kVJCKbuDb01tEkZZKZJpfWt-0YXsRuCRNEtLX19Eu2YqVefOeaUQCb69_glC7Ek_81nH5IjsP3ItFFlWC1FAqxucMdKl2F4yVIO_R0rZqsimDchaH94u7-I067cEpyZ1UY1yds5vShtlyeSDPOdFln2RN9VynBNBNrE-qTbpQgIyMpEhuquLGtx5kdMNEjGvd5hvO-3hrMBfAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/693101" target="_blank">📅 12:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ویدیویی از تجمع عده‌ای مقابل منزل حسن روحانی و درخواست محاکمه او!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/693100" target="_blank">📅 12:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
پزشکیان: آمریکا در دی‌ماه به دنبال کودتا در ایران بود و وقتی کودتا شکست خورد، به فکر حمله نظامی افتادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/693099" target="_blank">📅 12:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71aab458b1.mp4?token=Jg4P9UJuZkIhWYBBQqBB2_cx5vJFfo1KdmWw-eeqb93Db8c7p0nSbZrUJh8R0cU0k7LDvAVATk1Vd1qUcDBTRO-g52Z1s4UGR98Qlw3TSQuT5rv7MrDx5phcDUjjuLxBHxBbB6zany73W-q7D8vf2dpG0syJCfF8-4MurpGlMNuW1jyPbE_FQqk_JzZRTg3kHqkLVLOA8vDnyUqqh0ZlbDDxFP1oGbE7SChqvTwSuBXndFm-MahFJa9y04UdBIIhqpg0KiA9NegqWG7oA49EMThce99QOSGwqZKUTYBDcvZzn5d1ybhpjs1eRFXXIIwVIiNcUf-_HzTcJYeJu6qhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71aab458b1.mp4?token=Jg4P9UJuZkIhWYBBQqBB2_cx5vJFfo1KdmWw-eeqb93Db8c7p0nSbZrUJh8R0cU0k7LDvAVATk1Vd1qUcDBTRO-g52Z1s4UGR98Qlw3TSQuT5rv7MrDx5phcDUjjuLxBHxBbB6zany73W-q7D8vf2dpG0syJCfF8-4MurpGlMNuW1jyPbE_FQqk_JzZRTg3kHqkLVLOA8vDnyUqqh0ZlbDDxFP1oGbE7SChqvTwSuBXndFm-MahFJa9y04UdBIIhqpg0KiA9NegqWG7oA49EMThce99QOSGwqZKUTYBDcvZzn5d1ybhpjs1eRFXXIIwVIiNcUf-_HzTcJYeJu6qhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در ژاپن، بسته‌بندی محصولات باید تا حد امکان با محصول واقعی داخل بسته مطابقت داشته باشد و تصاویر روی بسته نباید مصرف‌کننده را درباره شکل و اندازه محصول گمراه کند
🇯🇵
📦
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/693098" target="_blank">📅 12:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsxZ7PES2fzVFmT1EUGQhui9GdlhhS4TT1cEZHlTXEw6JyEvfocGB-tNrINvcLFlLSc8bnEUfKOY2HHaWBwqlo3uymaYCRbrQn6gknUdHefuIhMPG-yluRPxvtblzVofwMVla216M7psor4O5TPmTWaNmPBYm6WYy9JuJIjI0MoPmABC4Qmv9nXEv5i5h_PTpDySYtvJA1qj_HVvWWNajbmbbVeLkwQawsvmk-aXidLl8WXWnVu9ogEgmQq9Pr8a1FpOgX_3xKEjLypwjIuw8UWh4JVZZbM6050vNnNyQpLmGo_zf3bhWfOmcxP2QEdNiQoRIr5GS5WhJ60UeNUIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متا از دو ابزار جدید رونمایی کرد که باهاشون می‌شه با کمک ⁦AI⁩ بازی ساخت:
Horizon Create⁩ و ⁦Horizon Studio⁩
🎮
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/693097" target="_blank">📅 12:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693095">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
پزشکیان: آمریکا در دی‌ماه به دنبال کودتا در ایران بود و وقتی کودتا شکست خورد، به فکر حمله نظامی افتادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/693095" target="_blank">📅 12:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693094">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا: قصد آمریکا حل موضع هسته‌ای نیست، بلکه براندازی جمهوری اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/693094" target="_blank">📅 12:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693092">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7efc4fe9a.mp4?token=Nu7CFDlyYOo9sAj8NE5eRhXFElbndzNq9ViovzlTkhEhNeRL3LJubX9Gm8KPtooWmj3kkuuD64nGWZgHLfnYqyR9imOq7cXBYhIEw_OAyFTvWoeJG2qE-DkdXO9Uk0rOA9wNI8ORjV8jia-_Ex2HHRV8h-yNL5DHOn15M9cXfYzmI6JwaHFM5d2sfchCKlcudj4zlLGhWAenlqxxTbvCEm9D1vJMPgGADLjX8VKR1q3oxwEafb3Qe_RYerCXg8OWgBBWGUIn405IReyZecYYwUx6b4Qm-lWQP8u-XegdXTyLHW9-9emXFubfxWM08Y66BohMNexSlP8RCotcS8hKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7efc4fe9a.mp4?token=Nu7CFDlyYOo9sAj8NE5eRhXFElbndzNq9ViovzlTkhEhNeRL3LJubX9Gm8KPtooWmj3kkuuD64nGWZgHLfnYqyR9imOq7cXBYhIEw_OAyFTvWoeJG2qE-DkdXO9Uk0rOA9wNI8ORjV8jia-_Ex2HHRV8h-yNL5DHOn15M9cXfYzmI6JwaHFM5d2sfchCKlcudj4zlLGhWAenlqxxTbvCEm9D1vJMPgGADLjX8VKR1q3oxwEafb3Qe_RYerCXg8OWgBBWGUIn405IReyZecYYwUx6b4Qm-lWQP8u-XegdXTyLHW9-9emXFubfxWM08Y66BohMNexSlP8RCotcS8hKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در تهران، پس از تماس خانواده یک بیمار با اورژانس و حضور آمبولانس برای انتقال او، خودرو روشن نشد و در نهایت خانواده بیمار و همسایه‌ها برای هل دادن آمبولانس وارد عمل شدند
🚑
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/693092" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693091">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1gJUOj5HRJFyj7JAS3JEzGnAN7cI8Em1cMGtAb6QjqtNoHiYuK1D02RPuUETM1ciRXooAWA8jXxk8Ah1ON5-053NEpueRnmd60a6JoikDvZ4Peo27bK0IedJ7_lKTohQMokme4ZXSJUuNiXbGdlHjZCvDEkUQou47PD64_TSWg2kgjvopQNLm1atZGq9l0jTgC5vkbfdLjMZVl90gsiCybxLSv9oI9oOBFBaTAcUbz7vdCItqADvOVe-NHVJoz6av9xQ6pmP6UO5T_GdO4HHuZuRlgt6bGcIL85L2LMWQL3y4SugeZGWnUeG2G9de7EewVAx6vtyP-BXRmWFjsRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بابک تقوایی، خبرنگار ساکن اسرائیل، مدعی شده است که منابع اسرائیلی به او گفته‌اند؛ بیست و نه ملوان و تفنگدار دریایی آمریکا که به عنوان زخمی‌های جدید جنگ ایران معرفی شدند، در حمله ایران به یک ناو آمریکایی زخمی شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/693091" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693090">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f451b032f.mp4?token=ojvsEYvzxXN4asphXNwo-TEB6DGRZX1b9FE01fqrQP10GQlIsiBlvLCOWhGh3VXEtcKKsa0CR0I1YgDM75nQFTwgW_9wL1dzejWxEzaoI3UV8zQGux_qqAt5ZCgVrXrcpZ6VXQFXCk4g7BY7kV0Ju6mY50jEhP-Zt7t1U7TveGA7kU8pZ0ukOo9eYW16s4mVUhy5aojooSi3cRsbHcT2f3hNdnbCquwyC-E8hft3vzDsFwJDWZQQhwsOBODSCv_28QuMpYymiWul2x6-0nh_tXmpx5asUTkXLulILc2fJO0_dp0QBtlhP5abXjTfKH05Me3hgz7klzkrjFrV5egukUpMXrK3ghL52UyZDzfUeX29nLxcqVfeDegEUItRWe4JaA2dJRjKjDy5Ut1Cf9w8nGesVKKMqH3JqGTns-GiOE1r8Q4GuT0iE6GAQLfnZGt719yIv0nTvu_UMH9jij0qOv8YDg8s5WW1RbHucK8IlWlwX80k9t5Vr1mXuWlYR8jV-ZQJzmTkqUgqGgOKGWSTDC2JkgGtK4da_l4Fiv5yocSFgET_Eg5EfyEPuMqCP0kLaGGndhYQUVSrQlBkL8OnnfJIlbe7VX-95WL9qlazCLSe-GS-D-GMthEqJOevk0h3C7-A5LknqFhGeq_GH9toUF3NtVwQN23jXXMmvwRezS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f451b032f.mp4?token=ojvsEYvzxXN4asphXNwo-TEB6DGRZX1b9FE01fqrQP10GQlIsiBlvLCOWhGh3VXEtcKKsa0CR0I1YgDM75nQFTwgW_9wL1dzejWxEzaoI3UV8zQGux_qqAt5ZCgVrXrcpZ6VXQFXCk4g7BY7kV0Ju6mY50jEhP-Zt7t1U7TveGA7kU8pZ0ukOo9eYW16s4mVUhy5aojooSi3cRsbHcT2f3hNdnbCquwyC-E8hft3vzDsFwJDWZQQhwsOBODSCv_28QuMpYymiWul2x6-0nh_tXmpx5asUTkXLulILc2fJO0_dp0QBtlhP5abXjTfKH05Me3hgz7klzkrjFrV5egukUpMXrK3ghL52UyZDzfUeX29nLxcqVfeDegEUItRWe4JaA2dJRjKjDy5Ut1Cf9w8nGesVKKMqH3JqGTns-GiOE1r8Q4GuT0iE6GAQLfnZGt719yIv0nTvu_UMH9jij0qOv8YDg8s5WW1RbHucK8IlWlwX80k9t5Vr1mXuWlYR8jV-ZQJzmTkqUgqGgOKGWSTDC2JkgGtK4da_l4Fiv5yocSFgET_Eg5EfyEPuMqCP0kLaGGndhYQUVSrQlBkL8OnnfJIlbe7VX-95WL9qlazCLSe-GS-D-GMthEqJOevk0h3C7-A5LknqFhGeq_GH9toUF3NtVwQN23jXXMmvwRezS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا: قصد آمریکا حل موضع هسته‌ای نیست، بلکه براندازی جمهوری اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/693090" target="_blank">📅 11:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693089">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
پزشکیان در مصاحبه با شبکه CBS آمریکا: هماهنگی‌ها با رهبر انقلاب درباره تفاهم‌نامه انجام شده است و اگر آمریکا به تعهدات عمل کند، ما هم عمل می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/693089" target="_blank">📅 11:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693087">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
پروازهای ایران به چین، ویتنام و مالزی همچنان برقرار است و ایرلاین‌های ایرانی برای راه‌اندازی مسیرهای جدید هوایی مذاکره می‌کنند
/ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/693087" target="_blank">📅 11:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693084">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89aad4192f.mp4?token=ZQ0k0x7YdXYEN4SBXO1us-nHWwWELsZMOK6Vw114PNWStKtsd5RU-HswiRKbKfGdHuuZLXep_5ddKQBh4Du6cEqPVeIiS6PcnM6LlkG1-rv7PhxMHrXVxy6u7aDweAWjNg3KiXdsHuNMXj6unN3odMteG70NcX439Z5SLfL2HQLmIH2UQXUA37DdBLpS8gn5MO6uzNq_f6B2WbXEm_SyRVyE6ANgorHfBiilsMDfOOuDG4bf4R7p5fheM4NNY7AoU9JQ1VQm8t39FysUQsq_CtTESD3kwfjZytYwiPoMWi77EnXIUNoDJFqMweFcDD0Pss9tRjGYm3BGqDRbvoFrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89aad4192f.mp4?token=ZQ0k0x7YdXYEN4SBXO1us-nHWwWELsZMOK6Vw114PNWStKtsd5RU-HswiRKbKfGdHuuZLXep_5ddKQBh4Du6cEqPVeIiS6PcnM6LlkG1-rv7PhxMHrXVxy6u7aDweAWjNg3KiXdsHuNMXj6unN3odMteG70NcX439Z5SLfL2HQLmIH2UQXUA37DdBLpS8gn5MO6uzNq_f6B2WbXEm_SyRVyE6ANgorHfBiilsMDfOOuDG4bf4R7p5fheM4NNY7AoU9JQ1VQm8t39FysUQsq_CtTESD3kwfjZytYwiPoMWi77EnXIUNoDJFqMweFcDD0Pss9tRjGYm3BGqDRbvoFrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هولناک از لحظه انفجار مواد آتش‌بازی در خودرویی در مکزیک
💥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/693084" target="_blank">📅 11:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693083">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07403de48.mp4?token=I25jpzkSgjfFWZgrzRBzaYB6YZltAvJzKWWqY7Wjkc_fO8xOCtSrjyuZH3h_ji1xwc_lLt-aTL3FWM1EyxEQN2jfeApWHUUqrigo8Mk_ze_D_DNEM7ENBwBzUy8VH2LiIiFkmerUvK3kjgi_blpDGoTBdY9gier_rITafxqewr9aR1j9QFVdCmoQk5gDDyYTUaZKIwRO5nENyh_tIWFWrURPczcedk-xxwexyGMhWTzgH_9LxWJ4lXx8IIsc8NPVRjjAUSIcF6FkEKhSUCt_1l8ULjXCZtyWiFC7Yjo8khQhKdDgvKp3kRexLcdPV91BwecBpwpudj1WOFLaFvufKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07403de48.mp4?token=I25jpzkSgjfFWZgrzRBzaYB6YZltAvJzKWWqY7Wjkc_fO8xOCtSrjyuZH3h_ji1xwc_lLt-aTL3FWM1EyxEQN2jfeApWHUUqrigo8Mk_ze_D_DNEM7ENBwBzUy8VH2LiIiFkmerUvK3kjgi_blpDGoTBdY9gier_rITafxqewr9aR1j9QFVdCmoQk5gDDyYTUaZKIwRO5nENyh_tIWFWrURPczcedk-xxwexyGMhWTzgH_9LxWJ4lXx8IIsc8NPVRjjAUSIcF6FkEKhSUCt_1l8ULjXCZtyWiFC7Yjo8khQhKdDgvKp3kRexLcdPV91BwecBpwpudj1WOFLaFvufKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار فرمانده سنتکام از پاسخ به سوال خبرنگار در مورد میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/693083" target="_blank">📅 11:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693082">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
نیویورک‌تایمز: عربستان سعودی ممکن است در حال حرکت به سوی ساخت سلاح هسته‌ای باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/693082" target="_blank">📅 11:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693081">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454c9358d8.mp4?token=Im6O3tBDghKrR8rQY1D8zjtEurS1JHfn_YHaxoMKO6B1NURhWhUuUYhDkEvP6bY9abKgoXhbJteU9Ehtb3NKpx51pJ4yRGRCVWTIIKU7J2BP1yUa2BjxsGmlfyYnQ67NPjfPcsEv_7ppbiKJ2787RZgNc8cyQ6g-E3LOXU5A4qOtr9T2KwbTaEY_AxV2uhnEmknAJipEzrP66JgFT_12_LudNJgdSj60uX97zSs-OGEb_LrzPQZj0h3Wm6rzs-pLUBJ7LUQQ0XdTDydZwzweVB9A7O1WQKOura9dHhr64vM2wIdiRXydO6SVhUe1a7j4WExCXyeWPmsJZL2zWuyyPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454c9358d8.mp4?token=Im6O3tBDghKrR8rQY1D8zjtEurS1JHfn_YHaxoMKO6B1NURhWhUuUYhDkEvP6bY9abKgoXhbJteU9Ehtb3NKpx51pJ4yRGRCVWTIIKU7J2BP1yUa2BjxsGmlfyYnQ67NPjfPcsEv_7ppbiKJ2787RZgNc8cyQ6g-E3LOXU5A4qOtr9T2KwbTaEY_AxV2uhnEmknAJipEzrP66JgFT_12_LudNJgdSj60uX97zSs-OGEb_LrzPQZj0h3Wm6rzs-pLUBJ7LUQQ0XdTDydZwzweVB9A7O1WQKOura9dHhr64vM2wIdiRXydO6SVhUe1a7j4WExCXyeWPmsJZL2zWuyyPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: هیچ ضمانتی وجود ندارد که آمریکا و اسرائیل دست از ترورها بردارند/ آمریکا و اسرائیل هر کس که دلشان می‌خواهد ترور می‌کنند، بعد می‌گویند او تروریست بود/ دانش‌آموزان، دانشمندان و رهبر ما تروریست بودند؟
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/693081" target="_blank">📅 11:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693071">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsBFCH0QTUIGVV1RN1VnLmIZvZmAucHzfa20c-sZqBlaLB-luRufEFtGQoU7AxCdavq_n47Ht7405KX5aPaaHFBBR5MDoDk-H1jFL48tjqw98Vbn6_P5YCs9ezRg5VHXcrkZ1I2j1wA2qy1EYwS-qspMbw-GjpLcKQXclmUPvyN5_f0BLg_OlzrZeedbC0oenJ5qVAMfs2Jzcyna9_EqiAkdhd4N9Nb0wI443zgKr_XJM7qzBzrH2oEGsAdGfEQrezIcwYdpY7nhBT69ZIO2RD1sqHIZNWwlCasCYdQaDZhm_L_1TtVhW7q29kMA27Jb_KS4k_exxAUdSyUoGpBZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yul5vecnKtmLAFPNo-Mtr0u6uUD7j5UgAdWXa6szwHBOGZK__ZWw9iHHzA8lUngiN8zQVTIkZDSVmyquwXlGzHTpX5NGds4qapZgQJiSDHxChx0DqgLebP2yIoPpgJOr6EPk0ZJa3FhpguD_Ueh9o1DtNErg3ixK2Ej0odFJTqCT9WRSD36YbIvgmx_fW-V-YyEEwx0hXHj02Tv4_86zmoRaMLEKvMkn39wFagoW8qxs-wK1GlUxNaq20fRYtJ75wfF1xPcZK-vYPJCz_xgq5DdFKpmGvQpee4Ub6O_W4tw9nn0GQcpPK5oz1J2Jd-xjPisOSvDwdFZFXUyy7JKNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCPrn3cVntozPfrOlCubZ7WxWdfexWXr37mxNRXCszSFiIkr9Nzi6MlP5zN94ssgazUDIJMbKYTyUEVpq080wZ3cTDad0VLrBpWEMtG2nhbE7QS5iVBmwBO7Z7dqcWZ1xvQhYGUuhjLM3Z2yu1HuKtMdPMCPntq_gqGCORJBdSB6AihEVnn7KLerCN8sJw6tjPMsE9wxizfN2j3aD5FPQdP6eAnOzeBFl3-LoWEzElYJu38FxBeILFNuMkEO7rVW10lI5VJUL6dXN0MNrVP_GFFtag9E6U2psiN33QBFFkrEa94-wANn3Tukc76Ofeh35yRaIiomLscjbSqmgz7zDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4z5hVNb6J1IoSyMaUd9IS_z7mxcxBG1ykkhBOw_wgYmfGeezmJ2r_EiEYujoVSiKVsw8LwJtbp0zmm3x31EV7eLtctQVnu8t-lew8j2e0KgMk8VzukTp-lO7YxFItDZjknjFEc0uK7cx5uA5iLryZ-HPNxGwfQ0OjL7VnqTURf4lya9uOG1gqdtS9mpk8oZGzdRzoKEKo-V0O6xuAlHLepej_3EwwoNPDWsuABrwGTJl2aDrcL7Q-RjLRyrtcjaInQH_2aN9yq3YrSwk8kMqDN-k4EZ2aYTFJ8qj77edf5sSpM83cBLNiNxKhi7nHYe_YQHHvh_rToz20WxYFiWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_hcp9shdoKGqh_vQjcDYyFHqZor6kRl5Mju3htsPz4oyJR9iGcp5pPkRrbHOWT7qwW3suHSeie7LblztqSuJPWjTL3Yb2SR_H6jXjPvNGphticfuBokNZNAd3yovcvVh42RNoF1ylK5b4BthyPCzEYpFCrZfCMSLS-Xk_4JRamqOv1T_8ztsA_B1zC_xjQ9gOF8a182me1zGCtcYhecLG_eB00HBZNRwRGzBEl4Df2q-lLxEehEAV8WNHUzQZy8DPMAqMNxlcoDlKtrOJIR60jJuE5qGgxIyVciaUSzZAtF9FB9_nJ9RsMYoxJuX8xEJ_ESQjXchZnt7JMtWNWD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEc4sNiRbL_vV_RVEY6aHJWWzkW1GwhxtWxMLCnFDoDt-660LXf1Qyw2MuknbAufxkN0H4mbAdxzv9ovTtIekvg-WPE3WmW3kc2cLKoAfX9zdnChBICMGGcuONgcp5oXcoUUsTER1kCjIH5JIC4ecyiUfEzavt9xaGgFV2EnbD-eVMlw--_9AdfHfgpZlG3XNsD7RwgQhupRI2PgQ2ta6obm0EPZv-JtJdiMF1Sf4yNznk6_tBkdEkXGeefP43k75RbrDsRbcnfOraMOJ8nh0kuXDN_waUJhBXljT5-ptmvIlM44HVpw1FqWRNB2QTOI5MJn25AFUWSRP9oTzoKe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnyisHGpDSoqDUhOSTlJNKHrdA6E0kFAdnp8L_y6IC7yYJs68RKxQQuf6dTac9H_jtw5lgBj2scltsTIYJOrl67_gIbhstGLaABH9DneaKE4dAGsjdEN86-OzRMHaJMJstzTi0ZYacKxBdu18B0LDnMQrf40LKOtUYLWKD6ACvr48wHqkhiRsWalR7zgJ1xAGkH4U5SXJ7SW2uC9aE9McA6YpCIN4gRskPCxwXZF5ZLR5tGprHfwcREfKhrJ7J64Fo8bFiaNH9odL1gHwlExLQSRWmTW5y3QQHs61dSWT7QZ5aOQJ3eg3z8V8Vbrz15pNo6HcZURpLfOgCr0_g8wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMSo6xT9-vzW-J4vgS4wlNgvC-Vthkc0LyW661uRIqB_NYditYCfriYWE74aulr6XxYrQPrgdSvYL0jSp76rM6og1RJBMQJ5d0EfeVyF1eFIESn67cSEaNQe8juBt5E7_D9AoMuT3brFzoXoivLXi0XTJEwQtrM4IDVhCnq9mkJsfEY4HAiZ3qvodKCne4q1OzlQQAZRTpGjfacPdImQrUp5bAL6sK_nO3P9Ogu5xSAtL9tXGhMkxjCo7WnYjVgf6h6Ly0SpSsa1UecajHHAioReIgc9Mzh3kgOPAG-VrXqnXK8fx_IVHQZkJTIDTrj1Rce1NtbicUr7YvLkoGL1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTrMFckhNSRbIwxOtVf2OMSp7uRZY62ooPv7Pv4pCGATl0QDJddvvhiI8rPJBE_zZjXar-wgZY9o6VbL7Mio8gKM_tkkPRw_agh-LtGyP9r5Yfmc4JR47rM09X1_uYF8IHb2JKooVKxayZE5SQaqk5dkpDZV_5-kZNWhv-KFQvP8-L77W7pzt1MYEEmRuGe2lfw1uYXK4j1roDX7kK-dfMV4J9BrDY2ZVODfGa2xzA__yg7jnyLOtKt2-mzYLWiDFp6lD1-AxqX97rbBR3lu2HtRrtTXvuATPViMWV0yxHgJL-sxG2QbzGJqQbDzYduJNt0VTUIL38UWDWRchvdtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5aok55hOVgRc7KHW-zoZLe2bfn2kHrCehLy2Gd_LDTFxkEVqw_aStTrYIsOSLDI_7AzdP7qIjX_f6ugCe7l_ee7pE4567tA333RLdMPHW2R-h3SXOSC9V7eX42b047q7V9wb228OWNaYph-MiDznqdGP3PkcoUyv2v9ZVNZFy8sqqC8TXbbgU7ghnCVbUiQMjPUXdre1Ni-AyaM3eCLPSN9QTeKn84_5e_vneGL7MHkOEsKeNyswDpEn5BeiXc7TYIm3okmwR6UBEm1dRWMpgr3JU7X4NoMMqfCNr5zsHgImFtScQag1hN4wrJXLHH5oBrJidv1YD8b8qVGAXqUzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حماسه‌سازی از جنس امید؛ وقتی مهندسان و راهداران ایرانی، رویای دشمن را خاکستر کردند
🔹
دشمن به شریان‌های حیاتی و زیرساخت‌های جاده‌ای جنوب هجوم آورد تا با فرو ریختنِ پل‌ها و زخمی کردن تن جاده‌ها، نبض جابه‌جایی کالا در کشور از تپش بایستد.
🔹
پل‌ها را نشانه گرفت در حالی که اراده‌ ما را ندید، بتن و فولاد را ویران کرد، اما غیرت سازندگانِ این مرز و بوم را ندید.
🔹
امروز هرمزگان شاهرگ یک رستاخیز مهندسی است، چرا که در کمتر از ۵۵ روز هشت دستگاه پل آسیب‌دیده بهتر از گذشته بازسازی شد تا به نماد شکست استراتژی تحقیر دشمن تبدیل شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/693071" target="_blank">📅 11:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4395e833.mp4?token=obw1GOofAhtEH7FJ0y9kHlMe9FLzAf80LN6W5-5Ur6rb29mI58JHHEcgwqvmZBeS0nGNiY-gdHN0wkgJIc_-v5I6UnZ_5NhpK38PfTC6jXu2dlqZ8TFQs9CUpvdbB3tcUhqLiXhDvQz8YaG-mHge-I--2q_eHC68cOz4XkQlZMTW6KPN66pt2JuGudmOeWOOZy9Jfxf0jVS9P-sw_thZ4fgVB0ZwG9llDjNZsbP_r7E8aAq8g2DSCTxuty3SaLzCyMTgcSfKQpGeJt_Ca5V1tC3zNoYDU5HYP_RS4lP3OH5GBtW5dojq5cnURTBBUra7wkYZ_Iz1Mn1UG3Mz0d6MGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4395e833.mp4?token=obw1GOofAhtEH7FJ0y9kHlMe9FLzAf80LN6W5-5Ur6rb29mI58JHHEcgwqvmZBeS0nGNiY-gdHN0wkgJIc_-v5I6UnZ_5NhpK38PfTC6jXu2dlqZ8TFQs9CUpvdbB3tcUhqLiXhDvQz8YaG-mHge-I--2q_eHC68cOz4XkQlZMTW6KPN66pt2JuGudmOeWOOZy9Jfxf0jVS9P-sw_thZ4fgVB0ZwG9llDjNZsbP_r7E8aAq8g2DSCTxuty3SaLzCyMTgcSfKQpGeJt_Ca5V1tC3zNoYDU5HYP_RS4lP3OH5GBtW5dojq5cnURTBBUra7wkYZ_Iz1Mn1UG3Mz0d6MGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید جو بی‌اعتمادی موجود بین ایران و آمریکا شکسته شود و به آنچه نوشته‌ایم پایبند باشیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/693069" target="_blank">📅 10:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تصاویر منتسب به مشاهده مخزن سوخت یک جنگنده آمریکایی-اسرائیلی در غرب کشور منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/693067" target="_blank">📅 10:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
پزشکیان: آمریکا اگر یک ماه صبر می‌کرد تنگه هرمز باز می‌شد/ تعجیل آمریکایی‌ها کار را سخت کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/693066" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543dcdc581.mp4?token=Qr-GbGw5k4G6Orpo00jXKVfD7v2Sxzto_TbQhYON37K3T0GRwYgYL9qLJL8P35IaD-uObBJHL-LLm8-ofmVAqZmQjeh-QzSOc-A20VeBrYFQdLbR_Ma8BotzOlg9OqIfnTscYw4UObpVKQPRHx1HWkhomdNz_g4ttqY8w_Mz9dK66WOELdLdV9x8Sht5D6FZj84fbGDPzLqesPe_fNmsn9fLo7C2tXbPxrvnYCAk6SryUDmDx9vU9W6gphF3M3CUDJ9QL2mFEtc39urwuNh34FISr0hekCyF4hGp8hCyEzi3ULKIUMPubbqnjFzI-No1enxbJfTsPBcygk8pLRYbth6R9ddlqUcOtq-LmfCx72hEvcPsklQR1_GbFvi0RvDwc4Lfd-bcGYAtqbiNEI7Ra6zj5U38Z0K9kX3xJJDlN_qqEJ_kHYd8AEYvqMLYgnevTBZV-YmKLt_jnoNj-41-2MQjt92iK_rpxOCUUcIGWqwoGN80BzhBPyTz0knNUj4NqCPUMykCGvIHK3Mh6oQNP6hDhsLpcRKWA8y-ihb4DyPzLzQG-36gmzEMqGHEId7mRg1t_4AB3XwdnVCIprIG6EMGFqyOATz7EDICTnKb53ZNG68mqsPJoIY8mzRyTtRNySqoSMz2394p90Iy9ZD5qGbKh2WZ2wpLb3wAvEeqaaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543dcdc581.mp4?token=Qr-GbGw5k4G6Orpo00jXKVfD7v2Sxzto_TbQhYON37K3T0GRwYgYL9qLJL8P35IaD-uObBJHL-LLm8-ofmVAqZmQjeh-QzSOc-A20VeBrYFQdLbR_Ma8BotzOlg9OqIfnTscYw4UObpVKQPRHx1HWkhomdNz_g4ttqY8w_Mz9dK66WOELdLdV9x8Sht5D6FZj84fbGDPzLqesPe_fNmsn9fLo7C2tXbPxrvnYCAk6SryUDmDx9vU9W6gphF3M3CUDJ9QL2mFEtc39urwuNh34FISr0hekCyF4hGp8hCyEzi3ULKIUMPubbqnjFzI-No1enxbJfTsPBcygk8pLRYbth6R9ddlqUcOtq-LmfCx72hEvcPsklQR1_GbFvi0RvDwc4Lfd-bcGYAtqbiNEI7Ra6zj5U38Z0K9kX3xJJDlN_qqEJ_kHYd8AEYvqMLYgnevTBZV-YmKLt_jnoNj-41-2MQjt92iK_rpxOCUUcIGWqwoGN80BzhBPyTz0knNUj4NqCPUMykCGvIHK3Mh6oQNP6hDhsLpcRKWA8y-ihb4DyPzLzQG-36gmzEMqGHEId7mRg1t_4AB3XwdnVCIprIG6EMGFqyOATz7EDICTnKb53ZNG68mqsPJoIY8mzRyTtRNySqoSMz2394p90Iy9ZD5qGbKh2WZ2wpLb3wAvEeqaaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: آمریکا و اسرائیل مراکز هسته‌ای ما را که بیشترین نظارت روی آنها بود، بمباران کردند و آژانس بین‌المللی هسته‌ای سکوت کرد/ هر موقع آمریکا به تعهدات خود عمل کرد، می‌توانیم درباره بازرسی‌های هسته‌ای صحبت  کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693065" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693064">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
شرط ایران برای آمریکا برای بازگشت به میز مذاکره و گفتگو  پزشکیان:
🔹
آمریکاست که راه ما را بسته؛ طبیعتا ایران هم راه را بسته است. راه‌ها باید دوطرفه باز شود تا بنشینیم و در میز مذاکره با هم گفت‌وگو کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/693064" target="_blank">📅 10:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693063">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5dddbc36.mp4?token=WA6gG9cIdchESqcpiQjd0BzWNt-uQtn9JPMLWoiOn55CYMwm-0-uVjzZ_eIRuAlaSpwkLU_bwYPUQi8kplcibQsjc-p-h5G9qPBexJos69tAAkF6ZNtYlEbIVr6-CI25SNEHo3UIX7h42pS483yZMpXStIG2CM5hfcdEMdHO8-iJaQXx9LBEZLsZd42vEq1wLeivSxGF0Z2lcIIeI50YjxDVtozi5sCZt6_05iMFE4tJAURfXAvrAiFbVfjU7RVcFaOruhoQE7vbPiDuyAOReNEiUOVHZXqhIbQi6dZvdNUWxHxMmON8_fPj6b66cWQtnPkeADWW5j_u3EMYybcAOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5dddbc36.mp4?token=WA6gG9cIdchESqcpiQjd0BzWNt-uQtn9JPMLWoiOn55CYMwm-0-uVjzZ_eIRuAlaSpwkLU_bwYPUQi8kplcibQsjc-p-h5G9qPBexJos69tAAkF6ZNtYlEbIVr6-CI25SNEHo3UIX7h42pS483yZMpXStIG2CM5hfcdEMdHO8-iJaQXx9LBEZLsZd42vEq1wLeivSxGF0Z2lcIIeI50YjxDVtozi5sCZt6_05iMFE4tJAURfXAvrAiFbVfjU7RVcFaOruhoQE7vbPiDuyAOReNEiUOVHZXqhIbQi6dZvdNUWxHxMmON8_fPj6b66cWQtnPkeADWW5j_u3EMYybcAOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در مصاحبه با شبکه CBS آمریکا: به عنوان یک پزشک می‌گویم که رهبر انقلاب در سلامت کامل هستند، ایشان به راحتی ۷ ساعت روی زمین با ما جلسه داشتند
🔹
دائم پایمان را عوض می‌کردیم و جابه‌جا می‌شدیم اما ایشان کاملاً در آن مدت نشسته بود و آن‌قدر سلامت جسمی داشتند…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693063" target="_blank">📅 10:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693062">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f6b017a903.mp4?token=S06cuKDOv8xnsnPb8QeCYDDzmJRrhLztFgXNFUIPZsz0KE47uK3hQ_NHPqNmpJQxG-30YAk2ElgcCe9Ipr4_y8kX0YSsCgkDRz1p9BiMHIIx1XEYR5wZPNIC2Umm_Kg_pKllJV2JosL_nHLWlt0wCT83Kt0-_Ydl0OJTuIZS1d9b_8Fn6ETWJhe-u_Kq2CpSxktkCGbMKPhKLotelp3KE-T0t258PosW6FZuRvzHhythkaMCcUra7Iz3wszVwpNcx6f71gScTfhsP-uF1XbWE3-GN7VVPWcz974R6A7EzMZuZ6pNzlqQx8WXl1PDKqcSPziWJHpOjlKFSQf5QVCWVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f6b017a903.mp4?token=S06cuKDOv8xnsnPb8QeCYDDzmJRrhLztFgXNFUIPZsz0KE47uK3hQ_NHPqNmpJQxG-30YAk2ElgcCe9Ipr4_y8kX0YSsCgkDRz1p9BiMHIIx1XEYR5wZPNIC2Umm_Kg_pKllJV2JosL_nHLWlt0wCT83Kt0-_Ydl0OJTuIZS1d9b_8Fn6ETWJhe-u_Kq2CpSxktkCGbMKPhKLotelp3KE-T0t258PosW6FZuRvzHhythkaMCcUra7Iz3wszVwpNcx6f71gScTfhsP-uF1XbWE3-GN7VVPWcz974R6A7EzMZuZ6pNzlqQx8WXl1PDKqcSPziWJHpOjlKFSQf5QVCWVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلوگیری از حشرات مزاحم خونه از زبون خودشون
🐛
🕸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693062" target="_blank">📅 10:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693061">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-text">🔹
«روشنایی» از دل آوار و خرابی‌ها دوباره سر برآورد؛ پل‌ها و تونل‌های هرمزگان استوارتر از قبل، قد برافراشتند
🔹
در روزهایی که دشمن برای ویرانی زیرساخت‌های جاده‌ای کشورمان به خود می‌بالید و راه دسترسی مردم بندرعباس را می‌بست، مردان راهدار، در دل خطر ایستادند؛ تا هیچ بن‌بستی، پایان راه مردم نباشد.
🔹
و‌ دشمن چه غافل بود از آن‌که مردم جنوب سال‌هاست با ایستادگی مأنوس‌اند؛ و این‌گونه بود که از دلِ تاریکی و آوار، دوباره نور سر برآورد، پل‌ها قامت برافراشتند و جاده‌ها زندگی را از نو به جریان انداختند.
🔹
آنچه در ماه‌های اخیر بر هرمزگان گذشت، نشان داد که راه‌ تنها ترکیبی از آسفالت و بتن نبوده، بلکه تجلی اراده‌هایی است که می‌ایستند، می‌سازند و دوباره عبور را ممکن می‌سازند.
🔹
آنچه خواهید دید، روایت مهندسان و راهدارانی است که با عشق و غیرت، راه را به مردم بازگرداندند؛ قلب‌های تپنده جاده‌ها و مردان بی‌ادعای روزهای دشوار...
🇮🇷
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/693061" target="_blank">📅 10:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693059">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0ii4pVLOMdrm72hzUUiOD0iXgvDZ6XQKQ42Hk-MkGRUFdiZ1ztrIpkqcryKcka2dJRjuK7H_4Br1wQntsl1cN8-lUxncDHY6sR7f5hVVwGR0vWEPqzn0NdwkZM3lNk6uiFPdi08CIDODHi46-iKAKFdfOTmOsA9Enh8OqSxp1Mt84h84gMzTTC9RDteCk0y-XcS1ML7JCE0ucGj0ZfCpgFUoiGQDlfgHEctWa_30PdtLGLlCHWXXvRYOsIVRimUK_GsoCgABhWoWgaCsuh2GjfCC_o2NKI_i4V5GVw_Qk9nnrmgaYvn0lQsjmYjgw2e_8AhMrv87nMWUILRc7Swrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5aa01c77.mp4?token=ryWk_Xuu0yzh7plhQvixDxD-7V_Uqbyx-ijAUaSIKA5ncav-I1m86ZdvB2QkR79_hPir5mXAPxtDUflcUqY4ahrUOiW2P1QQNFitlVx43obRlMiRQvq3ovEbrK4bzqzNS7-ijkak_6eTN7VIg3QMgW1mWCw_T8x4_TETZeJ7Q7scz8DPadOBRn0N5jg4y2Mb0BPw9qyUKZpd7MlTP59BPuHc3cqvZ_hnBPCjN8J-oxM0UahLoqZblcHqWiQANbIGfKoLgNKVf7Xjh7AAUPKvbeXkG2yRfx2ZeEwWdo6TcGbBfSsNDqRQFcoxrMxUlZeSE94eU6RN-u7KEHE61liE3Jlef7cn7JtA2OpcBjNOLRwXlJzCoQkyt9Nmy3dXALxjisuJbWaN38edPivRCYVlKfyz16CTjw_OkShPgSR7lLAt4dfLZY421fnWdJdC6a-9UjQla5NDlD5v_OB1ePHd-00rRggNy1TnZ_Pgr9dzuyOEsoy1bnyX66398dAd4tN8pCD_96B3t3V_s1mDXxEFyc5ePAWY4TksriOnYsmjW7Y4InYaruRGNkwkFJiKtzqvW3EG9Ocg7f7CxqR3IG-8ymGmqYgb4JJ3ASbNSXFu-CSAjKDoi-Nzoyi859ka6di68hJgEvEPQ-sc0G97mLMDoWyHGhKP_64OvG9EOQpzLQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5aa01c77.mp4?token=ryWk_Xuu0yzh7plhQvixDxD-7V_Uqbyx-ijAUaSIKA5ncav-I1m86ZdvB2QkR79_hPir5mXAPxtDUflcUqY4ahrUOiW2P1QQNFitlVx43obRlMiRQvq3ovEbrK4bzqzNS7-ijkak_6eTN7VIg3QMgW1mWCw_T8x4_TETZeJ7Q7scz8DPadOBRn0N5jg4y2Mb0BPw9qyUKZpd7MlTP59BPuHc3cqvZ_hnBPCjN8J-oxM0UahLoqZblcHqWiQANbIGfKoLgNKVf7Xjh7AAUPKvbeXkG2yRfx2ZeEwWdo6TcGbBfSsNDqRQFcoxrMxUlZeSE94eU6RN-u7KEHE61liE3Jlef7cn7JtA2OpcBjNOLRwXlJzCoQkyt9Nmy3dXALxjisuJbWaN38edPivRCYVlKfyz16CTjw_OkShPgSR7lLAt4dfLZY421fnWdJdC6a-9UjQla5NDlD5v_OB1ePHd-00rRggNy1TnZ_Pgr9dzuyOEsoy1bnyX66398dAd4tN8pCD_96B3t3V_s1mDXxEFyc5ePAWY4TksriOnYsmjW7Y4InYaruRGNkwkFJiKtzqvW3EG9Ocg7f7CxqR3IG-8ymGmqYgb4JJ3ASbNSXFu-CSAjKDoi-Nzoyi859ka6di68hJgEvEPQ-sc0G97mLMDoWyHGhKP_64OvG9EOQpzLQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیژن مرتضوی، نوازنده و خواننده سرشناس ایرانی، جدیدترین آهنگ خود را برای کودکان شهید میناب خواند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/693059" target="_blank">📅 10:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693058">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2cac7c872.mp4?token=U8d1xtTUIW2S0-_trOmMUealb82fc95hH0QOnK-5AuWlA4BSu8-UYzMcAGFpChJ5NszkN2fwSrxlz_k0JDINm09J2xa8rNH8RYKOlcYSTopnUESGw2i--X1AFNG_NXAQRI6v3jQgrjN-UchKMQFeZuZBOsQuIbvTb_k8W2trDCWSJROKkpNEq4IrbRoEQ0a5NST5f-rqjo3JfGhHnZ9SdoAsNEe7XfkG7OOrgKFD1nxFs4Xaenz8L0FRQ9Se6ZUEnoTWPQb_5PeAM1jDswbdzB5SzgTa40EoPD8FHddGuHIDJHJgz1e_ehRpQ1S_C7bYu0ewKgiwS4uFBSmhEOAPvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2cac7c872.mp4?token=U8d1xtTUIW2S0-_trOmMUealb82fc95hH0QOnK-5AuWlA4BSu8-UYzMcAGFpChJ5NszkN2fwSrxlz_k0JDINm09J2xa8rNH8RYKOlcYSTopnUESGw2i--X1AFNG_NXAQRI6v3jQgrjN-UchKMQFeZuZBOsQuIbvTb_k8W2trDCWSJROKkpNEq4IrbRoEQ0a5NST5f-rqjo3JfGhHnZ9SdoAsNEe7XfkG7OOrgKFD1nxFs4Xaenz8L0FRQ9Se6ZUEnoTWPQb_5PeAM1jDswbdzB5SzgTa40EoPD8FHddGuHIDJHJgz1e_ehRpQ1S_C7bYu0ewKgiwS4uFBSmhEOAPvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این گرونی سوسیس و کالباس، خودت توی خونه کالباس لیونر خوشمزه و سالم درست کن
🥪
مواد لازم:
🔹
سینه مرغ ۵۰۰ گرم
🔹
روغن مایع ۱۰۰ گرم ( ۷ قاشق غذاخوری)
🔹
سفیده تخم مرغ ۱ عدد (۳۰ الی ۳۵ گرم)
🔹
نمک ۱۲ گرم (۱ قاشق غذاخوری)
🔹
سیر ۲ حبه
🔹
پوره یخ ۱۵۰ گرم (۳ چهارم لیوان)…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/693058" target="_blank">📅 10:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693057">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13472a3137.mp4?token=T6ZmIINZXbADos7t4t2yPgbfFruTv8qgXnIjLc89VG5VJdOAXMRN49mg-ziOReKsdewu9aRnMrYBA4VMCg1IVGJrsXQxYYdDYT-Q0cWJtw_o_KFTCgfqrxpm77z3qQW5KI_VqhcC-XCukv7lnKef6LNcdsTxUfUGp8f6uX0c9kDuhEgVkDEBuDiLpaybCcuTYQ5_P9jgB-mKlFk4hIgSYff9vwPevSxEJjWwDofUBmYv5KJ3TvxZk10qRs0oamO4S6hd7A5q76t8boGY6fUz4N-OdKWCrMad6AOhwUCwKNodZ1LCoXerWGqfuorodTuwluXmqMrPUUYA8Rp2giUrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13472a3137.mp4?token=T6ZmIINZXbADos7t4t2yPgbfFruTv8qgXnIjLc89VG5VJdOAXMRN49mg-ziOReKsdewu9aRnMrYBA4VMCg1IVGJrsXQxYYdDYT-Q0cWJtw_o_KFTCgfqrxpm77z3qQW5KI_VqhcC-XCukv7lnKef6LNcdsTxUfUGp8f6uX0c9kDuhEgVkDEBuDiLpaybCcuTYQ5_P9jgB-mKlFk4hIgSYff9vwPevSxEJjWwDofUBmYv5KJ3TvxZk10qRs0oamO4S6hd7A5q76t8boGY6fUz4N-OdKWCrMad6AOhwUCwKNodZ1LCoXerWGqfuorodTuwluXmqMrPUUYA8Rp2giUrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در مصاحبه با سی‌بی‌اس: آمریکا برای باز شدن تنگه هرمز عجله کرد و باعث شد تفاهم‌نامه از بین برود/ آمریکا به مفاد تفاهم‌نامه درباره تنگه هرمز عمل نکرد و کار به درگیری کشید
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/693057" target="_blank">📅 10:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693056">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c79738457.mp4?token=hvtArveQpuFCZ7akPuv7-nsi4254dZE2TP8qSinpgvB7QaKtlHeeuLlQSWq93QssoADjSMNMgI6xgltqCYrlqAGDvHqlqQEUR9CYkLUNw3wji1YY7AYjjlBhjJNJ7AsuX1ypXNApPQedJJ8ojsqwL2Hi5Y09kuq_jccgpI_dKt6kBhrgFD1nxMIFrRVH216PHYnts9ncQB3aq9YuneePhd_0AZF2VWYEdQ8RpabazreBDYa5pjxEvfHmaHzwQz86I4aUbwZIF9UvEYnQhYZN0fjeNeQDThMf6qNVcCfO2dQzzbOSJrEUXnnISLAEEkHCHyCfrP8mPUxaIkJ-kjplhhtx-9W_7mWPn54GP1gM9xGw5pAxnEQlL1YSHGzFyzWtgaUJUo3xrZMspe9TCXkXBjjCqCriZLP8MUwzVGXVyDAzlidRnYzAgwyn3e1EjBZ6ziZZI8gZuRJowl_TowRk4CJfPNc8eIsbn_ca-a-anpEuxmkcwn_aB5MDT754VVCSKQlbzi4ETwppwyOIoDnTTS_itDMg6I1pUw3Tf2wCEbXsqNvfptYA9z_MLTiFL-c8VAcnbD2xLYLJUsglODGadi_TpkniawO3ISmm-L4qkJWa4qWV3XbTruGv5ztQdrhW2mdiyxPVCW3Q49EzFIAsTwCX0ihc1mabE_DcPkFM9K4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c79738457.mp4?token=hvtArveQpuFCZ7akPuv7-nsi4254dZE2TP8qSinpgvB7QaKtlHeeuLlQSWq93QssoADjSMNMgI6xgltqCYrlqAGDvHqlqQEUR9CYkLUNw3wji1YY7AYjjlBhjJNJ7AsuX1ypXNApPQedJJ8ojsqwL2Hi5Y09kuq_jccgpI_dKt6kBhrgFD1nxMIFrRVH216PHYnts9ncQB3aq9YuneePhd_0AZF2VWYEdQ8RpabazreBDYa5pjxEvfHmaHzwQz86I4aUbwZIF9UvEYnQhYZN0fjeNeQDThMf6qNVcCfO2dQzzbOSJrEUXnnISLAEEkHCHyCfrP8mPUxaIkJ-kjplhhtx-9W_7mWPn54GP1gM9xGw5pAxnEQlL1YSHGzFyzWtgaUJUo3xrZMspe9TCXkXBjjCqCriZLP8MUwzVGXVyDAzlidRnYzAgwyn3e1EjBZ6ziZZI8gZuRJowl_TowRk4CJfPNc8eIsbn_ca-a-anpEuxmkcwn_aB5MDT754VVCSKQlbzi4ETwppwyOIoDnTTS_itDMg6I1pUw3Tf2wCEbXsqNvfptYA9z_MLTiFL-c8VAcnbD2xLYLJUsglODGadi_TpkniawO3ISmm-L4qkJWa4qWV3XbTruGv5ztQdrhW2mdiyxPVCW3Q49EzFIAsTwCX0ihc1mabE_DcPkFM9K4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در گفت‌وگو با شبکه خبری سی‌بی‌اس: آماده گفت‌وگو هستیم، اما قلدری و زور را نمی‌پذیریم  پزشکیان:
🔹
هر موقع آمریکا شرایط ما را بپذیرد، وارد مذاکره می‌شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/693056" target="_blank">📅 10:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693055">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
دبیرکل النجباء عراق: اگر پروازهای ایران از سر گرفته نشود، از مردم عراق، موکب‌ها و زائران می‌خواهیم برای اعتصاب در فرودگاه‌های عراق تا زمان لغو این تصمیم آماده شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/693055" target="_blank">📅 10:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693054">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
پزشکیان به سی‌بی‌اس نیوز: تیم ۶ نفره از نهادهای مختلف درباره سیاست خارجه تصمیم می گیرند/ بی‌اعتمادی میان ما و آمریکا مانع مهمی برای دیدار مستقیم با ترامپ است
🔹
اگر آمریکا جدیدترین پیشنهاد ایران برای بازگشایی تنگه هرمز را بپذیرد، تهران به تعهدات خود پایبند…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/693054" target="_blank">📅 10:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693053">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTa-B47LPFRuyo6hpT3GLm6PQPLjUFht0p5GG7C9hpH0yztuXGYOiiCAwdEhTQFhXU-qZlItkDvDn0diqZppMfplwgYPPLIqnf7CgrPfzcpwJCM4n_hGmzegkkR14xSn3VPlFiso359JsIYA2QmgnbBHkCzSTD-Ah1be_NrC1sjZiFyKVm4MetcaFVH-vxjq6nXn7YWpW1oLtdtyMOAR9NevBawxUbCk0zPKHsfHMLWFcVwiAMPnt9fz7wNHazxtHotG0CqdnYXPa2vKbzFSfekHeZNltrcZZOlLSuUTpcDr4NJU9fF1ivna1s1qNPI6xmu-T67p7NIJ72VKAPenqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این شماره‌ها و کدهای کاربردی می‌تونن خیلی از کارهاتون رو سریع‌تر راه بندازن
📱
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/693053" target="_blank">📅 09:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693052">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ایجنت‌های OpenAI خودمختار ۵۳ تصویر کاربران را در اینترنت منتشر کردند
🔹
شرکت OpenAI اعلام کرده ۵۳ تصویر متعلق به کاربران، بدون اطلاع شرکت توسط عامل‌های هوش مصنوعی در سایت‌های عمومی میزبانی تصاویر منتشر شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/693052" target="_blank">📅 09:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693051">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe8mOnvBGbOhg-G43eqWux_NlmpBEhXNFFniNMdl0vfQa--4VXp6v4YVgSuYtwDpOjI0lKKDfWLS2B6dpDjsZVt8nd7QPNWBCTFBUsfGhgPKhvOoMPOh7qJJWLrr11XTwCsYDl9KnanPRT5mdt4lmiWvEccwIl5uie3qw2RNCN5ZEVbNfy6IllURWVKMUmukaJvVZ0sAm9Lnmct5Z8VXkM7Z2nHBbQU4mG7yZpsIv3wLBwgkZ9VEax8ClxdUE_7iBhGXtbG9qlzzmkUQZtAAtjdUh0bzxDWmpJtTleK9au20Ear7KsfwVuPd4x6_lggv1PDb7vKdxVSv5wMQU99wXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ خوراکی مفید برای رشد و استحکام استخوان‌های کودکان
🦴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/693051" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693049">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
فردا یکشنبه ۵ مهر، کالابرگ سرپرستان خانوار با رقم انتهایی کد ملی ۷، ۸ و ۹ شارژ می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/693049" target="_blank">📅 09:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
جنگنده‌های سعودی در دو نوبت شهرستان قطابر در استان صعده یمن را هدف حمله هوایی قرار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/693048" target="_blank">📅 09:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693045">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVduwS0c1GFnrgJGA3OXfstFN-4VM7-izUsOiC3iN0lj1twdDmzcLH5cqrsgyIljHal4WSSsCyglZnuDMigP4Bq1gY7LB03Pv2MtcGPAF1OO7e8AMUl95G9HPctRT0XDUA0Z2TpHZ9YAHrG8QM7xBzSsIRfvSAEwUg5-_ZSFtPskBAEbWd6b7MfbVTF4hix9dXODNWNrgyqoR6z9CWfxYngpQkSCCxsHPpRaYhXi5L9BAN-wF6uKvah9y8z2KZ8MS4X1B_DNx7qANQeGJj0KuNH1t0i6JT3WBeOJBpsgwjjnwBRpYtTUuTXNoqL8JYyjzJIMMVnaHhVeNZSwVX515Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f5aab4b20.mp4?token=FWW-iSqmNZwDtZ6yuDjiGbzn_GqGmvRiF_AASQ8JMNhj4BYci6adWFqi7ExvNqa6IfSEkLamYAZjEr1KejxgT1VMyyf_Lz3ZGY-AJ_hnLndMoCtfY63weiLkDcXU5SbZoPQ68VLISPnMOdnMrQuWcM-zgmUnFQc__-aSwn1WmOK-yuo6SNK5MXyG68p7QfiFpvP92u46NmE5mLlw9sA64a-o53oVoeYeLexSfWThfXQwJ1ec1Wc-B1GR3jUkW8gGRVr_SacZFNOJhDttCQMF-8q9fQi5gz6UOG3eP-6DpVHzTYdOOu4Ul7QxujA6ogWkfuITVUmxuvIh4eCuLmmGaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f5aab4b20.mp4?token=FWW-iSqmNZwDtZ6yuDjiGbzn_GqGmvRiF_AASQ8JMNhj4BYci6adWFqi7ExvNqa6IfSEkLamYAZjEr1KejxgT1VMyyf_Lz3ZGY-AJ_hnLndMoCtfY63weiLkDcXU5SbZoPQ68VLISPnMOdnMrQuWcM-zgmUnFQc__-aSwn1WmOK-yuo6SNK5MXyG68p7QfiFpvP92u46NmE5mLlw9sA64a-o53oVoeYeLexSfWThfXQwJ1ec1Wc-B1GR3jUkW8gGRVr_SacZFNOJhDttCQMF-8q9fQi5gz6UOG3eP-6DpVHzTYdOOu4Ul7QxujA6ogWkfuITVUmxuvIh4eCuLmmGaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جالب سفارت ایران در زیمبابوه و به سخره گرفتن سخنرانی نتانیاهو برای صندلی‌های خالی:
نتانیاهو هنوز در حال شمارش کسانی است که سالن را در زمان سخنرانی‌اش ترک کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/693045" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693043">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBxMfevckiH1VCcqn7BEvafUsOw5fDnfsHRz0q53OPhla6qsXKgb_f0M284VFK0HFbvVCWIaSVt5171-m_wM18s-cql_OJowsoarkb63DVlCBjcAMrWVvi_Oge97MiO94cWCYxQ1jZDQJkQUBs0djONy7tiFwg5zzs5rheAlfZYsUKtRK0jKPrrIJhK7-seaKFqixhpEHqPT_C-JvH8bSzw8kKy02P5XAR9xvlIFDZ6v7588V6GJzN3imt3buspN3fIBd-xCI7Nq-RFMuGJjTY1A60TnYq210Qa9x8fNw7ZYEeHuiNdKCIzP1K4NTyXirJcNIt8wzr4NutasDuHtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلمبیا به طور رسمی روابط دیپلماتیک خود را با ایران قطع کرد
🔹
کلمبیا در این بیانیه ایران را به آنچه «ارتباط با گروه‌های تروریستی بین‌المللی» خوانده شده متهم کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/693043" target="_blank">📅 09:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693042">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbfQg6gFBpkbaUCGDoPi2mK2MTEpM6tWIc0TEEsQowmEP4LZrFPEMjljBP2pNJ5fLRmEDM0abn8k8G-7SWJpVZhZv1Rj-J-qmh0OfXXt3SB9RnVv8c64lyFC8dQyDlHpWZ8KI983YLc-urVzmDf6yrZWubxZOjfIUmcbLrg4UcQfZMhZYn-IYF0IRQlX-9Dbu_eNjTuDpZDKtezCtz_5XuDifEWgCenJk51DVdQNJLyz1LucRZJzEPr7qY0o2DVu5VassRBZy-yqPup21oUr40lu8yeAhgD88iK5d7pxnrV4Md9obdAsIXP-iF_XPsdP6HW1V7PDUUgvWnlyOA1_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال ۱۴ اسرائیل: عربستان سعودی تمام‌وقت مشغول درخواست کمک اطلاعاتی از اسرائیل برای مقابله با حوثی‌هاست، اما در نهایت، هیئت نمایندگی‌اش هنگام سخنرانی نتانیاهو در مجمع عمومی سازمان ملل، سالن را ترک می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/693042" target="_blank">📅 09:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693041">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raz4zeRAnaeooeNunsb8EZceVI4_ZKtJlO3mvtl4hkgt6T1QnLLD0wvGEiIeGkOmhECLoxfoB9QAHo5iZEKh-UiePCE5PtoWDyNtn32oGHh685V3yZ2-9HzqM_JKGxfLGbEVKMHpX5inaXHCIuSgxlcswZGq7u0hv2j494BxAVukemms7ZTUeuiS5s9XxsqvL_JZsSsmAKplfxd3Q7eCdJnZPh2vhuATVu7nuDv_eb83XTrpKaSP4tCS_k81JpVLt4W3vQIyMVeSWLUzQR8eiJT_DUD1wTyxwHe6Ehrd2KCxZIiPi4w1yQxdR5bug6HuAfWccA7Czubm5Ci2AI0hCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داروهای رایج برای مشکلات دهان و دندان
🦷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/693041" target="_blank">📅 09:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693040">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه ششم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693040" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه ششم؛ سرچشمه‌ قدرت
🔹
انسان‌ها از دیرباز به دلیل احساس ضعف و ترس در برابر حوادث جهان، یا به نیروهای تاریک و شیطانی پناه برده‌اند یا به ریسمان محکم الهی چنگ زده‌اند.
🔹
یادآوری مداوم نام‌های خداوند، شکرگزاری و هم‌نشینی با انسان‌های مؤمن و مثبت‌نگر، راهی مؤثر برای جلوگیری از فراموشی رحمت پروردگار و نجات از ناامیدی است.
🔹
انسان‌ها برای عبور از سختی‌ها و فتنه‌های روزگار، نیازمند تکیه بر دو نام مبارک
«الْقَوِيُّ»
و «
الْمَتِينُ»
هستند تا جسمی توانا و روانی استوار برای خدمت‌رسانی داشته باشند.
🔹
هرچه ظرف «باور و ایمان» انسان بزرگ‌تر باشد، دریافت او از قدرت و رحمت الهی بیشتر می‌شود.
🔹
متوقف کردن کار و تلاش به بهانه‌ی شرایط سخت، نشانه‌ای از ضعف روان است.
🔹
مؤمن واقعی کسی است که حتی در تاریک‌ترین روزها با دلی مطمئن می‌ایستد و جوانه امید می‌کارد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/693040" target="_blank">📅 09:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693039">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سخنگوی ائتلاف سعودی حمله موشکی و پهپادی یمنی‌ها به عربستان (به سمت خمیس مشیط) را تأیید کرد
🔹
بامداد امروز منابع غیررسمی از شنیده‌ شدن صدای انفجار در بخش‌هایی از پایتخت عربستان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/693039" target="_blank">📅 08:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693038">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Paeeiz</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/akhbarefori/693038" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎼
پاییز
🎙
محسن چاووشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/693038" target="_blank">📅 08:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693037">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9c7f0ea6.mp4?token=Bk6NBi_OghKKQFYm9sDXsZEb_NlCTfmCfyob2XHRinR_gHBmPBqJscfZDy1uFMoIY7ruUtly1RJYXjtFUJAHkmUBjtgUmdZm8xPuedaVFiTS3aqirnMorIzgsv5wIuU44GJw5sLbdyeIS-BKUxlvjqlhqQJffMFkF682hTMzs8w2nkWIDI86UBzzRxnLi1qzrk8Kmz98lCkmIo8sIgRX3qrU-xsm_UTrU8wt2SyXCQBAF4tZ4F0BQ5WQKlnT5iNXOtzXBI16UpYN2RjYMO8eAyTnD73L1W3QHRFi4nku8B7tRh_986pIDYEu9xOLUemZt5D05wwaPuKWn1wDQdKErA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9c7f0ea6.mp4?token=Bk6NBi_OghKKQFYm9sDXsZEb_NlCTfmCfyob2XHRinR_gHBmPBqJscfZDy1uFMoIY7ruUtly1RJYXjtFUJAHkmUBjtgUmdZm8xPuedaVFiTS3aqirnMorIzgsv5wIuU44GJw5sLbdyeIS-BKUxlvjqlhqQJffMFkF682hTMzs8w2nkWIDI86UBzzRxnLi1qzrk8Kmz98lCkmIo8sIgRX3qrU-xsm_UTrU8wt2SyXCQBAF4tZ4F0BQ5WQKlnT5iNXOtzXBI16UpYN2RjYMO8eAyTnD73L1W3QHRFi4nku8B7tRh_986pIDYEu9xOLUemZt5D05wwaPuKWn1wDQdKErA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک: به وفوری فراتر از مصرف انسان می‌رسیم؛ ربات‌ها آنقدر گسترده می‌شوند که حتی اگر کسی قلعه بخواهد، برایش می‌سازند و تقاضای انسانی را کاملاً برآورده می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/693037" target="_blank">📅 08:49 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
