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
<img src="https://cdn4.telesco.pe/file/HpcoMQUr7qVHz2TdCYJYsi3WTgIoWms5MNZPCmEvcTOFpWfRRzM9KJx3_YzZ3K5EBkUWfriXSZWioiLar39BMmuuniwPWPFxAlamCyxzpbz0b1RFlicSTbLyakfOjqyp_41nn--Gztcmd4NjdNhEro0ewVZX4Kpg8bbkxVCta70yaDdFhqDuknDm5UeIxU_u12DaMwO_8ivY4cAJmJEi_bxT30QWJxi2k0MXvAuKOyAOAJvSfHcx62CdlemB9hwzKLNF4Izl4uW8mdyMi49V5wH8r93ukaXtGlVJotez3jKVfkEoUYesO8pBGiaNDAZx-rLvXiIH2b7-K3UkjgksgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 16:34:40</div>
<hr>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj3KMQXhuRBpiDvVj0oRmouWdQAk_lQXO8JIkPtinsU6xhpnpf_s4Uu-ZHW_tNs83CwEu18HGOv7R1SW4INvphLMCuEF-wg1SRTIQCM7On19umFiaHqoCaO9bJbVeAPrUi7YhrLTR1n-8_F4NulcYOnlL1OFuGT2_rEdG6DjD5cIdmsq5pN4w9RWzTdtR64x1rUFb1biPV3HWwMc_lEbkJ79T3C8IGBSdNrvG-y_KZCcPtqqla7_zZlhn6uxlJygUzkHM9UvHyJOVZBoRTrv-dy0X5Ls2-1ua4mpBWDqd7p0nRKXFwRcc-UDKEf7bZUoJM_ftHvZ8mPJrV3e2oURvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCyBwzVrjUB2LvzY1-sEF6pxTTVEaVGtqDlKmA23yZ-qfhRpvvIEPwS6C81ApQ_Gby7c8wz0XtecYEuONIWo16NABiEf9bY4QJ0WgR8YPHmQFMHlrbmr7laljEROLmFoij3_fq3KZpK7Xm2f6WDAGnSo27Rc2R1zFtvsY_B77EwAE-5zSQcttR6YjCa9iRAGVnlf1bTZNROBIROf8BiodTu3jGzDkGUbLlFOiSC8AAq67-1nchDnbGo9tNn9vPcxG_xkUPtzwdAOZZBZVMj2aQGWH6XD_ODAqMyjAA52uEnrYeJGpfc_0YWefpqDsrCnpNoHzCiMdBWZZwVb-B59_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF3wG0N6k_JF36lN7XzwCBdR4RDCTAMQJG_ogUJGCF7asqhzS1S-CAT5I_ziHjLMmSwXGk0_dX1HgfAxQu2VmdqQy_GoUzxeRLNGSBpvCHhUu0Ske20Ir8pMkCdMPgdbLYwuySPsn2eczLyZgl61ame63AOVFb744032JZxarFV-e8hf21Jiap-IqNQwFbTaExviReOcn8oSAY_2MKWw6Y3Rwr3lUtJ8IDoioesYn2m9Cbq9jLhMN8sViXq4KxRSF8VVPPypVadeJS0ALW4bkSA3E3L6_xo-uGRmOMHVacmGsLUIsLq1wKsBifRWEQ1r-RT50jq-YukS-eAKJUs_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqulMgxIz7Tec-0X5fZKvxfFuusRIXVzJwt6qEXXJLtnPTQvt7lkGh2DEQ2W1JwBnAQ-O6k6sWDMCclZ5dyeJhCFJ7WPvvByS2309uO_GOx7a3hEO09N7g7szGsTism8D_awWUpF0NMp_nmVeusKjqxXPf-T3gHdyeUVRKas1BIfMt-NL9tzRHmaLIG0B7F4EA98uFsD_xFYwxCHgNNntaJMCxOn8B3OSq3UuEtbOG_fwvmP5-AjZ_e2OroMqz_CVws59Njl83cqifW-AH4O-7c_YWaqVkdSrxIg5NoVZ4dQ6KlYac3bic5a6A_4775i4wbZK8gZkrRHMlGLsN4rmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NODy6g42jK7Aouw0EDSkv7z5g6loY-zndARer1KBAdZZ9fh-h2vahLeVJkGF6YevRqirrTpE6OPTxjG6Q9RZ8heU78zuK2G78cYwuPv5g7y6sqpOEAvBzU_FKG-noWf303CRGgmwhCVYjRoE3ipwMiEkThXENd8kLr4cs_tVTulLO6WXni2cQb-xx_CfVSKgjCnP3cuyyszOBIxJX8H-11hHd4zGvjeuYzltaq4g9pigw0_kUrHCA2qYb7JM4-PpTK2u04TzRBQwCY6lFvMgLpDRPSpQWgSBX_dCy-8eDN7b52lsFbE3uCkz8PkL3VwqmiGeFRmcNr79Xajhcm-0NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUwgL-98ls8W4FfDYdSYaR_TjhymtpJRX9uXIH6gQHdOiVF2Pl-G9ll9IASITg7qV99WJ-4KWcunvv9fdx6ckXIy8hLhEiX5M6j-dgE-Ot4yEWOCQCm9rmhoWz97mn1-xWlIV4q5t5xB_otBhHvyF4reHR0-ENpjLCi-05ECOhkfOyDoJrnJmUckkYPKM3aeElbThcaBKZjFH8-m2MUlc5gGrYyq1rnhWpO5x02Z1jE9__J8BRXrmau7nh-Ea8Jyc0vnGxIWFBGZEGFDAsDAl1wgDrlzrRefup3xgX-c2KqwsCqJLD6yDsrMxIfsVccosJdXs2Pb8YgReSqdU8IYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW-mgaeDBCVy0iK6psiMs5FL4oynpiogUK4spA3EjS2db0VYKDwXz0rDEhpY1Rb1yizumrgE7lIssuJnQfR3lbBFefBDa7nO2-Sm6394m8xBOh2PF-BMnzZXXa2uw27pUvY8PdFyvaYzjs8xhO5Hif6_WfbN14wR5vDB9rSbocuYRHWswlyVzWIH3o2S-rHHS19dXBAdrCmFavP6KbLBw2ExI6W2AzVldQhLXzxTnNqXksYVa10gRhDbnPvMNDm7t7hX8uZRsBKjDyvZbCMbpyzkz0zvr9QTf8M5dx5gAX5UJuhvdp-1YowDa7YcIsMyWkOo2R66ikXxLSQhlbhBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNJk4sEEJHlVDnxY9yrY2SWSNFQa3-b41kbSw__xroP2c62XuV65rP2Sn0rKthW8naQUCcIqz79aYe73mf_4wvUwq3xqpp7WgGRf2rs-F71C7S-WPAzy835VqzE1TlzDC03i_Q_ps21leAqLY_4p4SxumcSgFWVEg_MF4Vc3j-04ls8d2g1IR4Oda7UfFJktnu89Tak2jyWlrtQJV0a8j3lWgdPf_wyK3ANzRc5Uf0dW6ltTWmoWo5DQbZs4sqiEtNvh8ZBUl4PV2HWnLHGAB8az8fpMNicEKiz8sxFzU4jVhwFlK68MYR2AMdkwGyZZMfO-d_xHN3bXMJ0Iyn3VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=sshVym8f7_ADoe95e4da8eykzwTD6Z3MrqtHpNjiknMy89Q4e5N6Je0C17Q5TXBYufM5kAtfIn7u9RllF9-fV5_FxjfgZ4MU4hzLj-CxgPIQbmooqNrZzUYHnBuYdGHiGSoNK4iqAubgARWxlGfepJXx2YLN7fyUaz9bWRjHoqtFywFmooEUsYoHuTV2i9OXi8atEO4lUiOKYRhC9sDdZ0Vpc0ulaZ9S8Ksiu1dPK8fi1cMzXJ37h7c9LD6XaX1F78LvxzVodmD-lZHc3_p3lvfq2Qi50KVgrwmQ_aND2U-yJhoEqQjWEn84SWd86syGfL8Eg73SeT_Agngcd7AAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=sshVym8f7_ADoe95e4da8eykzwTD6Z3MrqtHpNjiknMy89Q4e5N6Je0C17Q5TXBYufM5kAtfIn7u9RllF9-fV5_FxjfgZ4MU4hzLj-CxgPIQbmooqNrZzUYHnBuYdGHiGSoNK4iqAubgARWxlGfepJXx2YLN7fyUaz9bWRjHoqtFywFmooEUsYoHuTV2i9OXi8atEO4lUiOKYRhC9sDdZ0Vpc0ulaZ9S8Ksiu1dPK8fi1cMzXJ37h7c9LD6XaX1F78LvxzVodmD-lZHc3_p3lvfq2Qi50KVgrwmQ_aND2U-yJhoEqQjWEn84SWd86syGfL8Eg73SeT_Agngcd7AAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=BKxOtK_zsX-kQh4eqCbc4r9ILoH6o-XgHP-ulylKw1P4GaD-RyUFPM_vYzl4dTKxM-QCGLJIKqwnyY8em5XfXXRgqs6irtJPbf2htWVBmY9y4g_Zy9RW0Em4ejjFJS4Ds7LqLCqEsITJtgHpph3xn7ioltBfETshW-J23akSCK16_BkGHYj9CM2siD5O387EBZoqXMk-CY4n3cpijJADztA_79DEHm-TATquyuVHVfuxxRsc4ev13i7cIh2lf-NdJKzYrGJFgE1lsWZ4Z1cjZQJza9KSzV1YiF-l6-mfOcadFh7bLOX7XHfF1lV7qIhOvQhmpHuadAubomj5PbGxng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=BKxOtK_zsX-kQh4eqCbc4r9ILoH6o-XgHP-ulylKw1P4GaD-RyUFPM_vYzl4dTKxM-QCGLJIKqwnyY8em5XfXXRgqs6irtJPbf2htWVBmY9y4g_Zy9RW0Em4ejjFJS4Ds7LqLCqEsITJtgHpph3xn7ioltBfETshW-J23akSCK16_BkGHYj9CM2siD5O387EBZoqXMk-CY4n3cpijJADztA_79DEHm-TATquyuVHVfuxxRsc4ev13i7cIh2lf-NdJKzYrGJFgE1lsWZ4Z1cjZQJza9KSzV1YiF-l6-mfOcadFh7bLOX7XHfF1lV7qIhOvQhmpHuadAubomj5PbGxng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euXzC1q5uoTSmUv5AF95LHdDfC2t8m95eFYAVVMw8uS2nBycBeG8JWBnNU2qu_my2dOwdTbXbZxcfE1EWithS--OCwoGBCRVMddfQAn31hUiKByqZA3Y6gGBHVQomeKGn7ni7Hjdn5zov1fSKK8kKw1rxhsCwNutR69gFuTdhcNWpJRTB8jI6xLC01VYhxhyDAO8LSRvPBqOwKyXMTogLnh-iRIKRvIHTx3ShgrtC9BTAQwuANNYNIhFYCaMNIhytAx6Jz446SZI_6qPqICfo8_IFmuwBQgioCuNOLgC_Ty1M9oRxOoh0Riz_xMFAfK6rA_-jAPmv0Fjv6c9HYRJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJwHDRc5wS-UoHgdu34bfPT-7n-9iS7rBT-2BHqv1nK8JF5ZRRo1XjXWR_NWfG84TGL59F9e5cZeG1FDDfs3j9_ZoFDQgFp-2IEIxVBW0i8UE7NyEe2C5CnTlwzD3Z4u9rt2ThuNQJ7edNh6xPlvr0G1fcO6VqWR6mthU3ofaiStjyteG4tbyIlqaUfV7hi9Yu2pB3ocZp42p7hOekepafg14jKMMa8xntrcqeZW63ww7gMT9Kf6x31kl0Bn4fSTYIbj1w-DdnNuqyRo1KfkUtYew1OBl8BBnML2Eq0_QxWyg5qr30rH21ZD6BAHyZtjBel9NwriktFvvctPWAVGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkWjplIIOQWo9Ztw6gMIYm4YlAjM6nOkf4Wihbl3eKEcjlkc1Xom9Iqh302IZ-cpXBqERK2RPLUJkORf3Fs7YkH5posO-LvE9TFXok3PBvOwMuFYjSdYvhjAXxR2HF13rCLjd4BVWHrYrLKy2X8JnwOq0PmLOefS9XNTAVbQNRvVwDgguC6A6nFTmQJQhQ2qu_dFQkkSa0AnKYO2RV3o0YjXhliDTT7ok0P5PDHi8z8xOvVIn1kdFT_PhA_zufx4qVpv7cepuXSbix71yIy9yu9YtLR-gGq2Df8O1go1Scp5HtyqdcHSOBn1fG9429_nh_7NKYCPZ23QFXQGlldzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=XGvZ7-23rstKvUm12V2BEsk5IOlUg_IJpxcVKq9phOvtQQJxQ2P3w91jMEUrB19FgqmCryjGc7tTpOOr2FeMcXF-3Niv1ZEubh9EOyv2XDH50V2MBzfC3ecSXLwDmpcafY1lE2VBW4XnBhS1nafVo5Lje66lL84gdT6y4bcKWukR3I4i5zGcv_UYT9knp3QKr5NMaJobd5OLHg9nj4OuwH0mY2ccDVu7E1h4OCMwPzR-_thVRqmpQRQTFrLtlUHaMKRd5fT1fj7sbvuLavZ4BTfV4R_x5gABahaXCco6ncH1Yy0Ws7tjAD2ZKv872BeJmCMOkfrqM58NAoNQ88X4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=XGvZ7-23rstKvUm12V2BEsk5IOlUg_IJpxcVKq9phOvtQQJxQ2P3w91jMEUrB19FgqmCryjGc7tTpOOr2FeMcXF-3Niv1ZEubh9EOyv2XDH50V2MBzfC3ecSXLwDmpcafY1lE2VBW4XnBhS1nafVo5Lje66lL84gdT6y4bcKWukR3I4i5zGcv_UYT9knp3QKr5NMaJobd5OLHg9nj4OuwH0mY2ccDVu7E1h4OCMwPzR-_thVRqmpQRQTFrLtlUHaMKRd5fT1fj7sbvuLavZ4BTfV4R_x5gABahaXCco6ncH1Yy0Ws7tjAD2ZKv872BeJmCMOkfrqM58NAoNQ88X4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgPrIbOIbVh5bZ4FR8YEvhUgN_8WUDhCivVOU2fuidhOIhmizI2vYFPJEDiNlEECfAZH5PeZhzXWBrFid76dJ67FrlaGSf0ynRFvTdkvTm_q8lv8x_K_uypJYKcwWJgg_d-E9OcbPmo3UQv0CEiTSG--596a39H8DMnF1NTO5Hsoj4KVqiYMbg8N3LUR8I6wvU3UzT6VEAHFjG87xoKnjY9Dq2phUbe0CsIhqepLUVRzgUtU6dOT4M3vkAvKeklTOh4UUaz-S3LO8aGC2Nb3YnzpmoN_O7U0gem59LhTgW9439-vkvlEFgvgD43PkjbQZ7bfnW1x2YXpKC7xGEV4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpdRdg8pCN4VUqYB4hICeCOrAWod3WVgqIh-Y0WP-LvkMqTcL7B3vv5n5z-eSIKY8_zTANEvZPONoUJ96TOgv_8M5uCKYYqfMAb6hBrCg3F6X727n-EhtDA-KHRuEZCk2qYeTaoDASvl4h_eI_o1-uYleE2jLYp4grnOeAsXmK3OqCtQyntnA8khjkQH3q_OTUQTinwH1NCHhhmLuF8kxEoqygyGz4DKEjyr3pg78Hp2yK-_T_QcwdIF6Ap_qRiXoiHCLZMf93yq7jovMFjmMQ-ueRrWTmY00o4W1vszGldhyOEmzbinrrq_jlVM0DGk2q9MeP6ombOHjR_AMt8Qyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9mM8KIgXngzHNCnVsKldA2Ns0AJis6Vu0dvNCdHU5AkSQ1TB0wc0H43IDWhGie0cPH5xRKJZJX3w-VgcJaBItIYf7Q1F-oHwU7JJeli1TaX4gvuH2Ry589JmNzLVtnVng6v4FAc8VMjBk6LmcMg12p9z9do_h7KnHGB_WUrGwrvoiUSEzBzRq7MOB5CXCPWqXaBA2lEPSgO7qIFoxStx9ASRhJKj69E0TEhaE_keadzPzlTJyvgAT7ApngyhGFZPkmfkWyESMxuJXdle65cX1LsWNkxeT92Ka2OR0nU70fcGJsKMKr2hqIPJpKQjz0j5rOfmpzgRD4ewJza0c5gRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhfDPGB1ejk_KP6TUfL3dv22Ks1hbeh85_NOmwelaUvDcoNZUgzdsMGnvfRg1SXV0DRwz5JzhyqWMv1S9TRGws1hZd9MTp0oFdtRM8eP9gX9-piEpOJ1QVsZ3zNGhtjDZYc9h5H8F_LoXR6fa044ufutVfDOMSwkpIjtGt3sfVSCa0HaVKyY5I69r2BJZlc7NQqL2hBm9nT4hEHczmm0eRT_jSqK04qUmXLci_1j3ieXGgVh4_65hCviTzwi8MDVjHJVFBH4FeJe0B-AMNhM-Q4QXXvR2cONtDwUce2MB_jnplza36yX6tvrueWWxBhriCOoF-JlgKiLdp1xUI6rKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW_izKLif6i0fQAaWtsBXkqHNWEWyR5-COsXYrYGM9TQgyd1AbV-h_T6OuNQprQesHQpnqGoM5Q3f3VluADdYH7gr-FNxVsT6QNMyK0EpLlheg9hHTjPflO8Kpo-Oe7YqJcHUmRRI3AVvH21ojwJnq-zauo1AWwqgktLjphDxn9lVZmtzBl43iW8_COCiGrt5lKT-yoFVjDCPpl8CclM4Kh4OpMuW3GZR651hsDNGgGJ-NanZCVzCY92Knhaotfpk8nYzGlhMmcupdKnNHqmxWQfJ00wA5jutqsa_z8Nj61jPlAeie70l4AJziJK_KMaM-kwvziPbzg2FDuX69zozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZVVewh5rjxuO8RveU7u4OF9Ak0SntnuI0JI_qy4xfH-57W-UtaoS9Vks8rNzRRr0NbdPJbkdRKoSh7HF1wc5_0g5UFDssy5bNVvbAQhejQu_GhrTJNDnI-0mEXBWmi7G2gxp2B5yL6oLiw4yIwHSqJLbAOCKpiPFT21nxTEArXfmkPPeJ3Op3H_rv7WJZE6kum4xLj2sr7p4lRYPqJ_U_nI1T8WOeymw1y-2jDni9tngWrY6lnXIiAPf9TXN6HRPkjyZdmM8kUDps30JvFIjg51K7em9rmvdXgG-tEy7U6jrqa7qYVtBcpc1GDx4YK7jWybapEv-H8aO5eEj6cGuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXADQKIIQQpJ3RG9SnUaRpNdsipvsWST2Dx3xmfxYkicYwKg-BHcA4LDhKbeK7KlRKZ085WhvCcFPBR4q5qV9VH8DASUDVHIdDy0fxFo6DhrCOrPPqFU31fZWEmPfFgXGN8xWqTNmlqaDC8gFc16kxtn1Hbe7rfdvhMmuWHZ-AbE2jWWsx2Hmc-SvFD6fLxFxKv_TIiDbiyPCkVFB53dvlAW5S2dQpDxSIKohijFlZFERelO4pXWgvQV5A4pjZeUOY0nI4rljRUOpXx_0adEvkkhGR3ozHAFBGtzCMpXkDCsOU0mx2chynGjD1kNiCi_A0j86ULA-JO1lcSnILxogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWOO23E3yNEahrd7MTWtTTqcgVC16EHBrupyObeuLpEpy_Q_cevQAbIo6IrbRIDd_G1Scy2pTxBQ8G6gThRwotULVCpmA1g4MAqt5fco4KLdupDdOg-yvYVwNJii22F-OEIzGxX6PudazRk0pHoeDwrPnX-5OD2iXbMzKqy5HtdmL10eut40PgvSoemigVHBS__TYIB5-mbfdHl2cXUh-CnrWvomHvWmx5YJNrKQZSmsZl0NgUU3Xbtuvc1aeUPUtAunv65NNzfLRHCzyux6OsN2fDy6yM9JggaYfLtDBOV1-m0aw77nggZJI-b-e1EVU6h42cM-XSKdfJ4k7hDYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XPyY_h0M6Q9UK3TsafVCkS8boPlNoVK04tdsvi8nfPuegh-7bnHAC7iwbYVYAoSpeZUk-A8pkR2_O-RgUpJIC9AdJPlucq6T-r1zCmGY0xVDLYUOAPwcviPEPojXmWhG-2BztxupFIoVSwHd7zykjwwbpppIqEH8Nd4nyTsB4obO50TV9jnGDlIzISrZP7P_UfHy5tQXDT5gQjJRunHzY3ACNe0PxKOap1Hq--s6V13Dplzixvq7AFajqa9nSjxcD54C8OrwWG9sCQQqOm-PviEttPrdzsgNc_4GTNn_uaYLChTxge-Bc3rQ9W2fkV5L1tiAlc4QwNxC9sTN_c-QAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grjWV64EX91mrBPsrzWLZQamhaXI1UnxAUbnN9TfDpcphOzloPCQNlWyroiukfA03L4_QwjPRP_D2UprnIk_sQ45qpHBbl7I7DOvi9wDArTfRN3zpXw7-J4EL_WN57vbCHy7LKPHAjnN51L6J53nIe5vLPjJhwNpHZYaUzqbVyIpdWr8nmWbmmwieBDNsuelrwYAwM0YFFPIpPTZXLb9e4iJ6CDlHyqtNW5pIz2VC9B3Mu3s3YI_QrzmkG8T8b-uSBWBz-PM4OtnQ3HLMMZkeAhCYBWSZP7EJXprxwT1MpkClt01vqCGLWeJHTJVA99kaEKj7ooEDIunferMker4fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKVKNqEdSFGjnqO1oHzFql9XI8j-ig9cVYCiha3CvswCcD2pp9mFryrnH8DEJpPW1-TMx6MEh04HOvInirfYYrJRCggyzP_MTbnLRDQNIH1ndQyYomuH8ZUK51twlPdTt54bCDkoZL2GpamTd9v_Nx0-5JMsLPbRh4tR4h2tof5mnrfMF8tJgl0eP6-PELZEfVgL4hKuzXEqqxtFas-mmpLdsVzs9GLqVVjZ7UqiHP9y5wFnIFWrdPSfaPFrhaCB3vRJiq4vzF4Q0M5pCVK-b73tvE5ffP78nIOKo2weKbfXmlA5l4UgLD6Gchzz7oqhDSN-tlS3xCi5o-GweU4wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=XfDzXCniunz-jauVaik-Hk3bO0rRNcutfK3x00_BdzgalVj8NHISlltKZxuy3jgnrTMGaKuZCS58fkvYnfxIFLiSgGS4m6ABN4jDdN2a0C0Tlak1S4QXWaUGXYHbD7Q0Mce4ecAKxIQHvEbbH4ie_zau0bfSzyj_6hlBcXLhAUYnWwKfARFm0CCsPXem8yQI1Kfl3S_Ro1e5XEhGmAESZk0kCv3myui08T6pjv6Ax2-mmJXNUoXapBvjTVY9dPJFOm1Oqx_Q9CK7h9MqY94O2_QXKjhz37965SSAM4jc3S-gfFik1l1ZI58Lus7l9XrkcDrWm6fGIbsvu-B6W_DfAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=XfDzXCniunz-jauVaik-Hk3bO0rRNcutfK3x00_BdzgalVj8NHISlltKZxuy3jgnrTMGaKuZCS58fkvYnfxIFLiSgGS4m6ABN4jDdN2a0C0Tlak1S4QXWaUGXYHbD7Q0Mce4ecAKxIQHvEbbH4ie_zau0bfSzyj_6hlBcXLhAUYnWwKfARFm0CCsPXem8yQI1Kfl3S_Ro1e5XEhGmAESZk0kCv3myui08T6pjv6Ax2-mmJXNUoXapBvjTVY9dPJFOm1Oqx_Q9CK7h9MqY94O2_QXKjhz37965SSAM4jc3S-gfFik1l1ZI58Lus7l9XrkcDrWm6fGIbsvu-B6W_DfAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=rXwBdEQWx_oeXstAIb9Jn-KPTZ_5q9QnTGv7kbfbgXLcy7tX8mMLLBFNBtHnM05Q33RVecpNn29yaItoq2jwUIAIExEkc8k1fDA4lEUMi9cCb3wzFizN5UUwmPoEefK2eUfOJvf-plLyg3xcFDMandJHce6f9plhzihXo5Al5h22D1V1K2jERue1vXvjXqI7qYVZ091wTdk_TzLlpd85BrctjHSKHoO9Vb-9ypdnwervMCq0xFhDjXgK-hjLUW6P6X46KK0d-AbyCFlxy8_uin60Jc8Fxbt-2okPXxlzG3az_0XqSuTbs2ZWTwl3FMMkPvwFaL29e8gKBzCwD9uRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=rXwBdEQWx_oeXstAIb9Jn-KPTZ_5q9QnTGv7kbfbgXLcy7tX8mMLLBFNBtHnM05Q33RVecpNn29yaItoq2jwUIAIExEkc8k1fDA4lEUMi9cCb3wzFizN5UUwmPoEefK2eUfOJvf-plLyg3xcFDMandJHce6f9plhzihXo5Al5h22D1V1K2jERue1vXvjXqI7qYVZ091wTdk_TzLlpd85BrctjHSKHoO9Vb-9ypdnwervMCq0xFhDjXgK-hjLUW6P6X46KK0d-AbyCFlxy8_uin60Jc8Fxbt-2okPXxlzG3az_0XqSuTbs2ZWTwl3FMMkPvwFaL29e8gKBzCwD9uRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=UCEEjGx_PBMaHHoQqw2i6jxdYgr1UbPNiROJZtICuh2NYpnoZ6YHuBWpB1r3BaN9_MiILulG_nYC6hl3A8QBmaSVF6VxF6eY00vsth2VHubPrUslpts2EEZI2XYKdA4CmgikYZscyaXPcTEcf3LWN_vmqPVZksGVFlZcBuI_bPTmBbhjXslz7-i5x6TUe1QAMqGXwTq51_mxCx5l6ipCyosi3SNiVFMvkuz9SLrUZLFxzzbMBxza86Q3Qyb7xPcWOXfDmK3D4pkiT1QI2kmq4J9jygH3NOCgEqGA2hIa2zmVqL4s-DaoQsnAnSZEk3QuJBK4BJASlySMUUzrwzd4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=UCEEjGx_PBMaHHoQqw2i6jxdYgr1UbPNiROJZtICuh2NYpnoZ6YHuBWpB1r3BaN9_MiILulG_nYC6hl3A8QBmaSVF6VxF6eY00vsth2VHubPrUslpts2EEZI2XYKdA4CmgikYZscyaXPcTEcf3LWN_vmqPVZksGVFlZcBuI_bPTmBbhjXslz7-i5x6TUe1QAMqGXwTq51_mxCx5l6ipCyosi3SNiVFMvkuz9SLrUZLFxzzbMBxza86Q3Qyb7xPcWOXfDmK3D4pkiT1QI2kmq4J9jygH3NOCgEqGA2hIa2zmVqL4s-DaoQsnAnSZEk3QuJBK4BJASlySMUUzrwzd4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXzHsUMZ7B4_YCvutGbuLozQph4n9oLJkuTMVI4lKtCXzC3KCO4qg7J57TrY_R6yVB_MG-MnJ5Q8sOnV0Q7HusmsPsslJx5jtdWDHG4wzr3FeJkTlY5pbzgFUoJMGJ4QEDviqtTRtYTJeQhVK-0VUyozLiiawg8cTxYKX5eaQnbC3ZyY4-_s3ER8bx6YnRmEWLVqKCpos7y30W3Ab2NKRpdbvngBdfztlhzygr3x1C63r8luxjC9eBkSemgnDxQxK7a3hU_FSM0B4JxyRyBTL3v8-xpJ8VZ-buVS7oYRYzdc_vZadiCQC0dx2NImYwrXDFxaXAXBcpe2tTqvrL-3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=APijzUMwgXJ06nxC15yMhnW4j7EpF-RkuNRZKLSV1IeZAJrg8cPKgXmSNpKpGhUWeOP4lnd1Ekl0-_fQLCZJOEWy5q9KYze2_eeZEFma6PHOA2D2Sq2EQeLp_YdKb6iDXpVn7rftfNgs2Noo4HzBC7TD0mID2mP-G9t05izUeLQ_KXG-39mBKZ28cWPMxpnyTIPEn4alNMpNL1V0Izb0OymuqwjqyzCidgCZgi4VVxaphbKvXDXkHks7Gr-to6Na7R9p2ranIrSQXrKv2UkyDza7V7smYLfVYHW5AnftPkpul9mQVLRei_FloGohg7OR7Z48SZBsoQp_i5QHZ967vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=APijzUMwgXJ06nxC15yMhnW4j7EpF-RkuNRZKLSV1IeZAJrg8cPKgXmSNpKpGhUWeOP4lnd1Ekl0-_fQLCZJOEWy5q9KYze2_eeZEFma6PHOA2D2Sq2EQeLp_YdKb6iDXpVn7rftfNgs2Noo4HzBC7TD0mID2mP-G9t05izUeLQ_KXG-39mBKZ28cWPMxpnyTIPEn4alNMpNL1V0Izb0OymuqwjqyzCidgCZgi4VVxaphbKvXDXkHks7Gr-to6Na7R9p2ranIrSQXrKv2UkyDza7V7smYLfVYHW5AnftPkpul9mQVLRei_FloGohg7OR7Z48SZBsoQp_i5QHZ967vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=bI2lCMwsv5HJDiWFIuk6R98IA6YzpMoy73_6Mw-Kyw5-TEY09I_WaK6FugaGGzdIKBgKCNdHHgdO6MYWVQYeR6_Jxa8GkZZwZnVpuPooyylET0NC-YAIEuKkYMVJwNLQd6KBltd6gCQ9a7Hb-DtrtrbXpbtRbZwj1M1lha6LkaK39ArrlhQXjawzhSmgp8l-4BmIJy4iag8lZRTus4RlxP2aa6qZQuAQttUB_yCO8c8CzTNUPrCY2_AM4pfjao12wX30ZmVkmKVw6BWYBLE-vZ4p53OeaTdbwkHTvtsMFq6-Ff7dnjPvBNv7ZbTHWHggt7lnxLIj5SlurllAzS-7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=bI2lCMwsv5HJDiWFIuk6R98IA6YzpMoy73_6Mw-Kyw5-TEY09I_WaK6FugaGGzdIKBgKCNdHHgdO6MYWVQYeR6_Jxa8GkZZwZnVpuPooyylET0NC-YAIEuKkYMVJwNLQd6KBltd6gCQ9a7Hb-DtrtrbXpbtRbZwj1M1lha6LkaK39ArrlhQXjawzhSmgp8l-4BmIJy4iag8lZRTus4RlxP2aa6qZQuAQttUB_yCO8c8CzTNUPrCY2_AM4pfjao12wX30ZmVkmKVw6BWYBLE-vZ4p53OeaTdbwkHTvtsMFq6-Ff7dnjPvBNv7ZbTHWHggt7lnxLIj5SlurllAzS-7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjfsRVco7BL7i0973rcDBMDUMdtai-qK1zLKapBbbCFiGBkdUPEXzgHz5QJB5NFR9eoTSR0e_WUjin0l3RklrYGyJyXfATEncMe-XB5XdOYebrGVKL-PDs3XRTqjHDaEvMonejHOKI5NXJXjMQrcKbrIUNIeKu5BHIKWzrzbM5B64ogKgqE55YKdIEUqjenzR_s4wa_BrRqW6hpX3hLBH-8IqY6CsWirf0KWLKrCuhSH-tx-xlLh0PLZlkKOmUb0lgVXoDEQOKEWrwcpS_XAYpPWs0X7XJhW94u961RdktvTY3ocwCw-o2-3nS6Rcez-uKEFPBn3SYMVLpBeHBh62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9B6GvAXM5QvZunEJVfD69sT1Dw-cr-VA9zleoL9Wc22qCA_oBZ49qaTjByqPfhdKiWQ9suoiK6cBet2uxTdRFQFw6xafabZAydbwO8hyqGnvCXspHwPmCiMbRgD8Ax5xsKTRlMSUX_y1PHGkk2f7rQ-5708KkooE6wr0CrnMBOwmVXqnCK4KKqHfBOrhfQtfKeCuzAaq7UZaql9pVXyxGmHJ_mQ4xxoNBYw3e_MnYqjOFNfp3gzWveNug087OO4-uoA2JCnMcsSpKBBc8INiJzifXtVtA8XUHLANCwEGm6teAllatUwuZR5ljCaSen2cdLKf3XvO6adBeSgVJXOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_0OW9T5KyYkPnwqg5n83K960CPJdH9MnIKhewFax6Xk2fDfglmSjWmy4Fn8ClCu1opftZp4CFdWg13ihaV5wHoXaSVQ2fSk1QGnz1Q802SHaF5d0m-bRZogUqXTsoAPyXtL_sWG9p5r9kh1XBiOdFmQ3g6S97zywRLMevJ37CEXK9_FLpZHiSM9h-6yNu1y3nD0v2WnI873ma2HE6K46fISOahjqM7bqTC3HZBkZ93pKXFLqDpGRPK4brfbx5JMTq3Zc8rwP7vodArCtqZKdnC6qqEmEm8ploxdwh61AicItUmgGlbRaHkDJNnnA3vQZeHFbQbjdObv0Y3vQP8GGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTaaAhl46xLSUrj-2FQZZiX0_HPNPgsS_Qhw12CEfR9G8aStI98LYEaon7qJ7Yh_H9ykfqcrNmPLbY1HUkgwkC-qXT9ljz-a0ygIuxp45hPdiW9QPFSsItr5X3KJeRGcq-XVEsC5ZAV8rdyidKlZld0PqqMjlXI2GNhGs1Bu3nT3lJthCLMY4B2dnyxy490EJ4bP_895lw0ybJMVcgTEKgpSiSgS7wj6FIc2b7RI1B7gK7x6aG5z6z_04Nk_hk8xgCf6ST_341FlAwVBOl6lAO7Sf97a-LANf6v3E1jFXfLCJ0iLdQ6TcXEVoU_W2B-3K5rx2DvCVKT98Cnw7GRRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rWmA7N_9juo_oec7272hHElqlDevTXy3umhLoZ2GlKaJRzY16jRvqdkAvbxp7TEKbQn3Aos9wjLfAx49PBnjrUL4G112eICH6YnltmVLVLGbPo00I6h9gEADKvqTYpGmlkr3-phmLAh379KGJevNxhV1HsNESQ-pTIaXaYy9dgmmXTUfYKNrzDTI_q7JCBUEfgVj77f1skUEsjhfPeHXiy1aMW4VeKmqEf0dS4xkdVxWO_wnH6LDKeNS8rcktkXVrS6qVM0JljWZHbuXL3ite-RFY03rUlXFY7Bf9fn8tT1KSpn-BQip4Xiwi2qeX1ah9N8javi7JjECkbmtdMTR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBKjlulrUMEKAMWbRWzjpKLXlETB_Xy2L7_4U-xhIVe9PZ9rmLDUoNNniotryF3TdzQlJ-_aH2uTiya9B-KQ4jxobFu5bH7h0lc1qdb6gLW46dFE0w7j2XcQ8r14G7d1VhlvnJ0UCKSv6gH3PjBLzkuzHa_nOGlgiR0mvBg619cNebZ-UFkDsRzxOzuttexh8Nz_eO14e8j7ZrGb2HyCG7r2aN4RacvWIaTUXvLjf1vUrzuRdIT5awkubRMBX-O0T4bJox_vLPDRGHt0sUGRRiyGB2_vIt5VmE22JVBlTvUiu2kOfzPYb7wRzrZv5gAZwJfCyXcQxXXjGptNTDF4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmcvbgzyiErROmeDKBVxohXqGWGy8epA3s-tjB5FWS3j9HXg04uB53pFqixy33EJGN8pl_gRbyAiNVo1MCjJzyLMUOuR2ucM_o193-pd8oIyanKN_qAt2BEz8KEGMd17xfg1rjcN20of_DRp1eYznb1OrbCHSic8jiqDPFEeyf9_ixEn9idKVMn4dsKRTbVIYnPlaDOs8Hm8MJBrHa7-nkIW7Qad8DBR2t8v1iFsNNXGFvltwHNZh2j3ous4MnCg6zX6CFcnzuyzoF2y8RDn76zImdV46YFp9tSe_fk4qHbs-R7D1tc62TPZ-xhnxJZwm_tYfDh_r3UCzzDnUKwvjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=BjPFvj8VFSFyXgmy9dWAkb5D2oVekdzGsr1q5tf8o4QopQp4csJqruKWhVQsbLML9aZCzQw3H5EGwS22hikLmXnJXzr809zYhRm9IrcGlc3uLr8PKydz_zYHdP9L6eUdfXz8afPWIN5PAzWiHzYpWAIU8zGOgECJ5mQoLCztoW80epNrEE3bmvmDcn8s1VMKOLcxglkDV1MM-xtTzBj9cnwZXSCiCujJmTX-H15bE5zKAlaeQKr1Vxm1ntbaAm_TJaKaitOZyLimPEaVE7GwPdGOtJM9p5Z0e7HgSsFHKOGSchQ2NecHfbfH39d7iUhw8FnZWbpfrQK2M0EgTgKANw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=BjPFvj8VFSFyXgmy9dWAkb5D2oVekdzGsr1q5tf8o4QopQp4csJqruKWhVQsbLML9aZCzQw3H5EGwS22hikLmXnJXzr809zYhRm9IrcGlc3uLr8PKydz_zYHdP9L6eUdfXz8afPWIN5PAzWiHzYpWAIU8zGOgECJ5mQoLCztoW80epNrEE3bmvmDcn8s1VMKOLcxglkDV1MM-xtTzBj9cnwZXSCiCujJmTX-H15bE5zKAlaeQKr1Vxm1ntbaAm_TJaKaitOZyLimPEaVE7GwPdGOtJM9p5Z0e7HgSsFHKOGSchQ2NecHfbfH39d7iUhw8FnZWbpfrQK2M0EgTgKANw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pstL_qh3mi8dmyag4gbN6ADWUQjm7hydDm7CliaT2IkNx77B5SQxG70QLqSEJmI15pZUn1bx2tkB3yMhunN8cKojCATr_jFHkLKD04lPG15hy_ch72Bm6hao51ElXxuLN-TMckINJBp91ieHtvnVdlXqCkjMJKQ5EaW6K5y4g_CTaHdPvv2hAuiMjJBFzUqXg_fSXyYDnMWIzbywyut7nEOBOJ-w9be6S96DmBhdHEmULuMlKchC83OR9wMtHeTuwa99_z1XxDjcreX8pYx4ENhZL2-_iZuO1GpnAN6p1o82yABWABj-rv81GQ2zlOh84J873BzK0Yg29mDVUFdpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pqq_-g_4bq-2zL2NeRKbISk_-jQTxKtj4q8ggsywLHdSU-F7ovxmHoOcikICUkktjpJ89s2yLhS0Xq7SQriD91D5hRPjo9IHAdLMqZpfWJNry2O2EbWh9F46Sj4NuyDXlxT6DdMOPRoFzk5QyMWbH9FU6hw_XOxlQYF4S6NfafyCN45gc7b4FAqERKDcqij7wYnCR8cx6IdYbENAprXnsrvf_etCqx-bRz8C9eQZXEt_gO9nsF_BrE-wwsCsVmSioUgr1ZCNEC6NgC9zxk0C8ojBZ0A4-_BSN3S6bZmfBYm5RXHM8cgMlWn52MhWC-COsRahMBzcZKQm_b_5d8tmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ictn0JE9DhExs1mFQaiffY9bYccse0uzUKC-fyDbTsGFevDddyb1potyRUOZutbOpKxuX5gOVmxCj8EqxfPLUDEf7PxVxav9TiK-gicqUQRiJ3mD6jPeCItt1JvEHL7Lf7hPqaTl-wvXyOWxANj0raIstP9DTfVPZUhkB9fQwTtqsZZgeTE-0oUxnzq0AYqNHvMmseQBoRB3ZfLdXh3LNc9eTtccjSV4Hjz-zeJ51-3vFuf5fKeC4D9xn4oYqac0iDjpx0EBd9-zR7nJoyc84CcBCcThAH9Kaa2UGJMIk_87LRjrr5CVHi5R1vi5DtF5N9hqyEGG_wZd0edxTJ57DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HICBEW8yZ5xoRarZgjUXRnlNh6jnwLgXwAdz4TUlVSbZOuH-C1WbP3gsO6x7ax3BmrTZGeNu8TYtFH2HYWkCgTt2C8FsxmudCb8TqdMcTt0jgC9yvtpSYxhfYg2aMyUabGcnYlHBs9BQ1_Agq8_FAyCd2sihZeWsNQKFuHTzhmeeD_-3YnEUsslS2Ht11p8UYrhQVdwOu7AiNQG2P45WuOpRLOJPf9n_IsXY63fm35TUqV2WojQ8W8rJqgdqye8Zj_VqHIWXcE4bEWAEfKBj2s45lOmCIMArnrCsgTMzwmqauqIw_WaXZYsmprpkD34m4JIUqe6-7Mm1BHxxKmWqlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=uAkw3VPDzgziTcT56_jCnEORsDnlGKRCRgNgPBXxBsEUQx9XG_QV710yWXKtPT9Zc5CQC5wPgrLqn6DINjaq2EdTOlXMXAnnw-oSbddoEJkOxR8w0gIDVO5TzknsRd0RjaGx4ud685UwXKJC50qjCZ2FrmYNm65-Wr3iUQsrxwBjUHcbG6B5Huz7F0IIFQTz_8hJrSaLJ6vbS4hMZF69XrVWplqdeo9I9qPD1THnTh6ETemeu4CAdL-MGuvAIHnzIMKjwa051o-V1vZDpAnkfzYNJAPRCKlI5-GWj4RMtC659KHS9FR91y0D8QENGBalpgvct2qT5FnWHqHUCNG_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=uAkw3VPDzgziTcT56_jCnEORsDnlGKRCRgNgPBXxBsEUQx9XG_QV710yWXKtPT9Zc5CQC5wPgrLqn6DINjaq2EdTOlXMXAnnw-oSbddoEJkOxR8w0gIDVO5TzknsRd0RjaGx4ud685UwXKJC50qjCZ2FrmYNm65-Wr3iUQsrxwBjUHcbG6B5Huz7F0IIFQTz_8hJrSaLJ6vbS4hMZF69XrVWplqdeo9I9qPD1THnTh6ETemeu4CAdL-MGuvAIHnzIMKjwa051o-V1vZDpAnkfzYNJAPRCKlI5-GWj4RMtC659KHS9FR91y0D8QENGBalpgvct2qT5FnWHqHUCNG_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pT0hv_IId4NAi09NEXFV3D-SF0BkoYQc7YZGT1WvAKD5qAJTXXzrfgWM6LAZy_jPwTTviQDmYK52BVcu4rrAVt9ALg-xGVg94FVLD3gm9nKFbfeP7YEHA8I-OzWM4OYgswyf4XQbtjh2OvfY2dxQlNPztSF0sqs-Fj9p-6JKp_2umskz3kDGI1l7yk_8IdY3Wx_SMR-IOM4owif1RMBxPP35DTCWYYgXRJs-kFjs_XJPWEI33W0d0HAgjE7aQQyxijhEt_DmYo3_1i7Jly9HXZOJMcoScjXH5txH2aFFsxlOEfAZJPg5OwjFkX6NrPbA5Ie4NJkMq1iMwiUdqcWU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj5CXhio4e-PrrYbTTZ6-mJXvI5f17ndfRfo_8ar_BteZiqQgeisCTwpyJGIzX3Kkri_FgKWeAd7NZVaG7b-ngjcOuS6s5GZFEdQqodpGKMoRQIHxcheT0MKvQRn-MBC8skP-V_XUzjF2GtANNdjiRFzCQgVVcOX1QjdwzFqC00v-6_dUA4q2W15kjTxOA3nec-KmZi2sP2_zij37fz1MioFKVOLYqQr39MPO-M_s2ytv0O1S64IN_h6QMHTqHfi42toLbfzRzD7CL4NS50tnOzmD5MkxFBG97czwNVl02kvVD2IM15ami5k2yMRdzbkdNIQenSUFuHPD6VTg6KaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYpD3rsN8SfPXRopP90AMfQWCBc5X87rHWac_VHSV7-I9s-sAzNICJbC9k6n-m370mKohwMDunq6oKW-h3MXRfbBQ6_sjj8lFI6uJWpHuVButEl8uwCgSlFF1nuy0eUENcmmHwcGdsjRaceXO3uQymsKuRxbX-bfP5PZhdpetovaIbV9XJ21xlN9sY1fRIxQYqOL7A5nN1T0Y5I7_Huwt3DC05JuPXps5F8j_2PXgTW2l4S4bout8cUWaFvdXJRzc8Dq7j2pkAwNbzdXV330IE6lVJQaAJpcNBl7pcoSNM4lT0TWF1AOS2KzTV2v3P6ehmk_iE8eeqTsys1F2ilbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUIVVL8QiC6HHe9UXb7rVoURUccztutu9fbGXb0RtLtv_OeMRI_fXroWNC4a4m5XA7TGn6Vzq9zKM0dsrxjNwQLpCMF1V0790T1qnpr2cfCsMu0NJ4ljEp5fm71F1PQIT2b_rWq3vzn_L5h6CEytStxc2FjYYzcAna_iMYlnotR5JfAvWsPwK43RbEZL4uibKPZYxrCGy0_y22-eMDwgbgSR8VcmQzUYGwVb195RVQ9sRjIXuN45ct0zx8_Syk3EYeZGZG4Xyi-jVEaXe3BpRXNSMOk-GfjWI0O7hgqniM_0fqS6CEgofiDT6iGIaUMsoClVnROXrnZJwTn-2PS-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz3z7n6N65ssFhqlW4rLU8YbIghFdW3RsA0Q91jteW5VlQh3mMBptwAzoY06jgIbtZyWfkP2080CBe763jr5ZLHArrm-ESGq2NqAqInUliUIh-sD5gDAHzdnCjIVFQ67iY4Va7ZPZz-5MTbNh6PliUh4jEsotQ_tTEz94n9z7O3ORuyWKRemstzSy_u3kIcXTTULE4hXPXXWVQc1xiZJkXNIjIx8CMhVTVXwUiTqEeUSYQFOmc2EmbtoSj10eoS9ad-ikGDd7vRnP19oIG9yqWDwWhKA69PBvaCfw2yYlG8dhu9vK3pR3Gsw6ZzdHMVCqEb0w-Zt8O4xS2JJiJiP0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OerzsISm9_7w9krVhnlrr9WUkx28MdxjuVcsDvPMbPA0236PlovxmPTHdMOuMlPXVTA47nt5m-iHnueQupI8IN7pXmk4unXpW5Nw1kPqX9LKC3kTU7RW5X_tH5UYi6QgRP4mF1FYHPtp1--DdLugwq0ydAQjkS-Z5CQQDbRNjRutSAhBZarUApgJ0rKP0eWfhcDjwCW_4Wvdx7IRT99rLGr7tQTq8lr34tNrgYgoeytvdoQnYwzxqg7JKX__B0NhV5BynK5W-QOP-TBArbQMZTqnvbiQFQB67XG1_anFiIke64Ir7VV7EQ8gjFjXrZ429pWClby4Jcp7NQQgIPU3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OerzsISm9_7w9krVhnlrr9WUkx28MdxjuVcsDvPMbPA0236PlovxmPTHdMOuMlPXVTA47nt5m-iHnueQupI8IN7pXmk4unXpW5Nw1kPqX9LKC3kTU7RW5X_tH5UYi6QgRP4mF1FYHPtp1--DdLugwq0ydAQjkS-Z5CQQDbRNjRutSAhBZarUApgJ0rKP0eWfhcDjwCW_4Wvdx7IRT99rLGr7tQTq8lr34tNrgYgoeytvdoQnYwzxqg7JKX__B0NhV5BynK5W-QOP-TBArbQMZTqnvbiQFQB67XG1_anFiIke64Ir7VV7EQ8gjFjXrZ429pWClby4Jcp7NQQgIPU3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مقامات پاکستانی هر ۱۰-۱۵ دقیقه یکبار میگن به دستیابی به توافق بین ایران و آمریکا خوش‌بین هستن.
موضوعی که نشون میده وضعیت برخلاف حرفهای مقامات پاکستانی اصلا خوب نیست.
🔺
یک : پاکستان در کنار بنگلادش یکی از متضررترین کشورها از بسته شدن تنگه هرمز بوده. اقتصادش دچار ضربه بسیار سنگینی شده و باز شدن این تنگه برای پاکستان و اقتصادش، به یک «ضرورت» تبدیل شده.
پاکستان فقط برای یک ژست در سطح جهانی در پی رسیدن ایران و آمریکا به توافق نیست!  بلکه برای نجات اقتصاد کشورش دست و پا می‌زنه.
🔺
دو : پاکستان قرارداد امنیتی دوجانبه با عربستان داره و در صورتی که جنگی بین ایران و عربستان رخ بده، وضعیت پاکستان بسیار دشوار خواهد شد چون بر اساس این قرارداد باید مشارکت پیدا کنه در دفاع از عربستان، همین امروز هم ۸ هزار سرباز و یک اسکادران جنگنده در عربستان مستقر کرد و البته سیستم‌های دفاع موشکی،
پیامی به عربستان که در کنارت هستیم و پیامی به ایران!
اما وقوع جنگ بین ایران و عربستان، برای پاکستان یک کابوسه! خصوصا اینکه جمهوری اسلامی در پاکستان نفوذ زیادی داره، اما ارتش، دولت و نهادهای امینتی همه با عربستان رابطه بسیار گرم دارند.
🔺
در روزهای اخیر خبرهایی منتشر شده بود که پاکستان مواضع ایران را به طور مثبت‌تری به آمریکا منتقل می‌کند و همین باعث سوتفاهم‌هایی شده بود.
بهرصورت اینکه پاکستان امروز دائم تاکید میکنه که همه چی خوبه، میشه حدس زد، وضعیت وخیمه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=c50WkwKZIa-zp1PRa9puuHwF-Bt8sZMwS8oYwcXjrPeXuDnHTjvNd0YW4DzHqlNwxBoPDgn51RKxZHtJkDZW-mhW7Xe6z8X29mBV60ix2Khp_yNVmXtarB5ryZXVZBT7BZgEpPm-fLyeIyofhphHp3uO1amL2CIacm1WizlxRHdrjbt58EoPjB3h5ZAYQz1Kws2hIaW_0gxsA7I6zUgkx0i6IO5B2dgoc4luTjkQ_bXuPhiSqzNKVNlKW0XT22BR2InXjCdhntr3A09AgPEHUF2viY-1IwVR_gGQhuNdqrjJmuwrQWx1wc_JzRt0PWQ1hTZ1DJNPyEtPkBGStfHleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=c50WkwKZIa-zp1PRa9puuHwF-Bt8sZMwS8oYwcXjrPeXuDnHTjvNd0YW4DzHqlNwxBoPDgn51RKxZHtJkDZW-mhW7Xe6z8X29mBV60ix2Khp_yNVmXtarB5ryZXVZBT7BZgEpPm-fLyeIyofhphHp3uO1amL2CIacm1WizlxRHdrjbt58EoPjB3h5ZAYQz1Kws2hIaW_0gxsA7I6zUgkx0i6IO5B2dgoc4luTjkQ_bXuPhiSqzNKVNlKW0XT22BR2InXjCdhntr3A09AgPEHUF2viY-1IwVR_gGQhuNdqrjJmuwrQWx1wc_JzRt0PWQ1hTZ1DJNPyEtPkBGStfHleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAGCkrj0by2VItyRapWl8OkD9_QeP6tYj2dZlkg9uTfHCM6hk3bZxjSnsfCQfdjZa-oiO5L4Wg7M71Rg2i0MuAk_qZG5JpQyp1W8D1RYEITu2B7W8yMfRn1ygYlW7xSPwHKzQ0EOSM2F1aF55U759Y2p3TkDxBQp2KYiY48Weya5oyn3C8IkSiOUSaJGCYVbJuui9BazXfFui2EmBUsrm1jZ3ELpjOUQBrH-6Bx2Fq9Im19ofrKAzqFcUoeQITKs46Z_ssGK6sPT4MVp8znvASA1kwMAlLYRkkCepC8kLiKchO6B2wAyxQ4SrHbXg_bec11S0mBlFDQmTTaHlXWS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDzu4Pkm8pxkEqUGpCLKVrSsiO-gev3YckgyzaU0Vq16QhqAccEoS6g5fi28nhARSZUa78O1MSvTceC3TMLH8o4N3VHzmN6Q_bzs9LuYigVt59LNGbgufEsOryP8XJjTiYp3FH5rc267zjyI6bAsI5ICzObqhP9RnA3EzO4ydSEBeGLiiN_5QsWnMfQLWIii4KgElnq39nmAtcnjRFb936XvuQNs1p3-IdgqGSzfWiTKLNc62dsY8OkHaDVNAsgmWoQFiOj1LzS6T9pLP8-mGGyS1IAEWZyF2lGMOu4ARIVJYNpERgYHenaTR0yd0_xEw2iXWsHzUOLxKXkbWOaHaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcPcoRbeW5X2171OIPgOHX02mQKaOiHJfRUZMDoocIo7W7qabauI3AxXEMfYpIXcICJQSVql-5y-D0x_u49_4CcUiSafu87yZDayH0yJbDf3fs_Twj30_FHEeMtfE_GOsISZpmYPzOIYdor3XU9wpj5k-m6um2d99-vstYssshTtv_l69RKq9NU1h0dXMAhQA1QCd4nffynFAgUAO9ULqFnj3qye-tfo8juFLfC2ILW7K72g7jEmIMMkN3zk7tmfYYHB_R9V6O8vxrRaj4U51IDch_t1C2SbKI7AZJ2q27tVP-XQlNbEw09tBfe55RD0tOcATkPk04Fwfds7RpAtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRXzqTuIRfI0sUhZjI1tdoF7n5AFhVq2pi7nQulkI8ZeDQVOFczxSFbqQWvuHC0zR1Dg7GBO41SbCKRLUjvBx2K58KvVKW-4l3Izao-Vh5jX3ZJq9-_NTN1sD91Tb-ZZymM7e6wpGWQFfGKj-1J1HX682u4mOm24cNXXzhK6vPYR-4_EFmIoTJBTHmUJxbqaZj0p6TDrJGMQfaqRJj0HnxVpqk_rcLHcm5re4x6o6Iwo6eUBU_DazIGwG0M9pLh_fpOhumqFMKuXfDPbq8JH5fRwHW_or98v_bn82jjoaJQZPADUTujI2TRcgQ4Nc0s362Hd3qQsQ5CWPo56R7YZIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=fsy8S1poOqEy2DzYQZ7M3gcMORSobGTbYC97QQ4CCRo4-CjSmE3LKd1Qf_FFe8Xsqdb2i0du6p_9Yzkth1mY8AxkYLod4PW4wu2Ew-J7CfDy04cYlF_j1Ks5ZPrLeTBZBWIFrl0k5mNYDTn_JSjNeprBmUMrXLzA8ui5ga6UrnUabQN1bCafP-azUXlUsfdWM_q4jq3aS0VnYUAkC9FJHg3HfpXZ5srlCR6X8DESanGidqQr9GZVxsBz5qPM5HwFuV6A5sATTX6QoSxuzhsDNA1W9mMjv2HJl2ql5jw1xKb6bz4XTpFUAmALgqCPo0I1GXBc-MC4eFS1fqu7v95fkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=fsy8S1poOqEy2DzYQZ7M3gcMORSobGTbYC97QQ4CCRo4-CjSmE3LKd1Qf_FFe8Xsqdb2i0du6p_9Yzkth1mY8AxkYLod4PW4wu2Ew-J7CfDy04cYlF_j1Ks5ZPrLeTBZBWIFrl0k5mNYDTn_JSjNeprBmUMrXLzA8ui5ga6UrnUabQN1bCafP-azUXlUsfdWM_q4jq3aS0VnYUAkC9FJHg3HfpXZ5srlCR6X8DESanGidqQr9GZVxsBz5qPM5HwFuV6A5sATTX6QoSxuzhsDNA1W9mMjv2HJl2ql5jw1xKb6bz4XTpFUAmALgqCPo0I1GXBc-MC4eFS1fqu7v95fkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=UMZyXZpSHDZGnYbye9_7Ljfs237Oi5XvHcNu2aAxEqdbKWioBdGNSG7_MUOpJ5vjVciY0UDcHzH1aSHvpums3UVMLgUF8b1dVT4WqKjZ5903k-dqMeoKMBYm-zWqvcQhaT_B9g5zObWk6fB0C1UBEs5nAc9Ju3sbnxYzSZRrQgwlQ20jhAZVopEG9edchZvQqJvzRKo-O2dsn-bK_ibAwCxBx-0ePTIOVeGPtXSIsyNQYLpSYnTzztvjK3rFSxG2-0ekCPw1LEftRRsh0-oT9rJ4e7_zs-6WhUb1cd2UfXkA7PD5VP8R-05mACc6b1uiDipsSHT44u8mSxhpikSXmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=UMZyXZpSHDZGnYbye9_7Ljfs237Oi5XvHcNu2aAxEqdbKWioBdGNSG7_MUOpJ5vjVciY0UDcHzH1aSHvpums3UVMLgUF8b1dVT4WqKjZ5903k-dqMeoKMBYm-zWqvcQhaT_B9g5zObWk6fB0C1UBEs5nAc9Ju3sbnxYzSZRrQgwlQ20jhAZVopEG9edchZvQqJvzRKo-O2dsn-bK_ibAwCxBx-0ePTIOVeGPtXSIsyNQYLpSYnTzztvjK3rFSxG2-0ekCPw1LEftRRsh0-oT9rJ4e7_zs-6WhUb1cd2UfXkA7PD5VP8R-05mACc6b1uiDipsSHT44u8mSxhpikSXmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb93v8EvRkCKtHf-AnqstUIyllnK4wo1sJ60yeCIApFW3VDfgd0Ha0Na52RIV01Q6dg-JQeiewsJNuayCS_pVcrBa7gkzhvFbgt6yR6HDv8CMHjaon1qqHQ4ifgUw6ZjLsCrcYow0bUj-Ltgg6m5HE1NrAfi-Jii0uurmCRc17YcITCvmO-p_U-3D6IeeiVCl8ZvkXdMHdFUU4ra6MzupqNKgCB1BEAnjpIVj6zKqlntav6kMv5FjTEURdOz5xkvGTjZQ5jz1Dio9fzyYI4dmZQnrOClT3cLzQC-EhKGC7YIG89P0KpD_aMgV60UcA0CciC3eI9mxvi29VeqyK-1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrWG0k6QYNl8Kdf-eTkJQlNZo1JRyboRGcAVlT0m2aHZSzbmzjtWJwFon-UbWdAujBmvtj3oIY2cBBgatW8mDfQQuOktGEUL4UTvjkXv1wrFAnt70IqpPObSkwR8e2TzWMmSfWz8vOGJD_XUZccGTfRAiCYJq6ryMVCKd586GsdCgSagSFt0f40mv1e8SKT4l-Z3UaaSmqvArUyDBNqvbMjwXOj6vzzk7n8A6P18mcI-n7rHNolSkdfB37pNV863pbDQVt3Utl7w9v8SqnOTJgyqfzrITiEWB4ZkT5GvfJrtGN1G28fEEuLV2cCuklsGisfYeaWCL-rbb6EYSWkZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKGWSTPNa3SVqRrlCyaZzF2_Nh69NOrqg1Nvj6DM8N7PJdDG34EI8n39YjNl3L5qKFWmz0r1x--uTRMWIdApN40Rj-5RSuxrgMd0BzzXYKhykoPRmawtJs9l92EVVn_MHUkRhX-XiH1ZLbghZYakGoUa-O33G3OQlGP_X28WD5aTk-YwB7EsVru-wia81Nvn93EAOA0A9Ki8_2EwVpbU5mzGAiaNiqfrqu1-lVjruEVdI0XnOd45JDHe1HIo3xqMXE3E2BSWg-NOxIefjvJhRcPu93Fj6ggj14skyW9MH1YwvPJhwAH9wfm2dyhetTv2amnoG79xi45eMggh0JcKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7lfdh1i4sLhSy1tzDGjF8QXM60D2naNAWqLI3ba84GmmNFlG-k26l37TD8US7UIesDp0Zc-DK_vqkmcun-m3WjfoK2HmF2nYGxFCxgLc1nQrv1qZ0Mee4DDWBQb-e5pKr9VAdYBvbaV-o9lJxWpaZsVxfKd7ad8u2GIOkjfR7AC9P7-gy0xlD4vSQRcS_-ZDRwq6tBb3Cix1UDK2_TcBlgZ7EiJiYn6RlwFDh8a6LnFZMraO4kKMTB4N-ZkM-JobjqvaEEHmlwRwaTN_hfcqdSLIl9anEYbAZLHhpRFxG97wIJ8iqa_KSMja9YvsRCdPgx_-YnqrovNz0ySFdnNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=VWJSnsxeMkzCyHv-B1vn7Nh7W-1ap-nAmieKhjxnPdNmMHIUgQmKihffDEA2F33F1wETSmaL_O3eo-NC2YdLo7oIhCJKuqIaudtAMy-0zNb0Dnf_ylvaaynrDbCVuUxEb3Ey_KdNigbRLUIiabg4BSqyHeF5sRfmr8ojgCH94cMms-6yK30EkXo5WMyTX3C7Qq54iOQY-FBYKbVVcJ6bpAHz0Y4MmUraSwyVY3p47EgKMXZ07TD6-h0fYL1MIcCWLGm5vXp3a1f3gQ240fnuuj12eg-lRUZEAGlTHSSSm-_jYQbbGTQEb0gN175yAxgWHU_ddRXCVp_G37cwUQzCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=VWJSnsxeMkzCyHv-B1vn7Nh7W-1ap-nAmieKhjxnPdNmMHIUgQmKihffDEA2F33F1wETSmaL_O3eo-NC2YdLo7oIhCJKuqIaudtAMy-0zNb0Dnf_ylvaaynrDbCVuUxEb3Ey_KdNigbRLUIiabg4BSqyHeF5sRfmr8ojgCH94cMms-6yK30EkXo5WMyTX3C7Qq54iOQY-FBYKbVVcJ6bpAHz0Y4MmUraSwyVY3p47EgKMXZ07TD6-h0fYL1MIcCWLGm5vXp3a1f3gQ240fnuuj12eg-lRUZEAGlTHSSSm-_jYQbbGTQEb0gN175yAxgWHU_ddRXCVp_G37cwUQzCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY9NtDpPWwv1wNObug5ezq_7AODyVt48fOfr7SuKx33Rsstqt2QyYhIk4i_0CqRdvk9XRO6PIfspfxd-SWdLYoYYqQsYymDhJ9s5r90OX25Xf3_P2pT8QoRrKINDbSzcaJWKvqYDHxfAwbwaddvBKXkhYC_Nv4Th_LggSHNGbppFEvnzmksUk5d7QPb5AlO3QCrVDR1q0GRWw829VS83wpr-5QwskGGeCiWJS8nGyrtE6liauN8aanVxMdD3iKKCxSrnXneW4ZT_IfXg_52Ycnkdz4L-aDkAYPJiNgYyUCIobpdrt38qEx_MotX60werKkSpbSnYGSniZ6R5uQLzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz2JQc2I7UOTykhK1sejgB3SCbIro5d96X2IZ2GzcyeU1yngChZiebxcbS0ugJyzTOGU-GlBt7gN6yJpx29u2NzP7GEY7RdkUhJTpkRlQyYpMth9Lbd8_m07b9Ppk6WbGX1NMb8FvtE63d2mlGwoDDeKr0gBLyBnIQW1NMyfsGCBOrsQORSzrhaKYfty2ZF3mQGmCkha01oixdnvgyJtr_N0T9Ud9j7nYFuliZV1s0drSJAd7TCF7wJs8eVFmZUEqFtdPLT1bpfj066--aH9SMQ3MSl98nLV6JzrxJS0BYNLNftBR0mmtxQ7uaqXHn6XC3cKH3yA3sxO9KdC0Gb_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=v1vKd17rJk2gHoGiFZdnMWPYUUKH3uhUgb5Uf_pwi2LwjHAouQvMvhSZth3zZM__9mE5LkCvSushu_i2PfBjWjtueHut-sHPdQFpfu9u2CM_s4-LPxS78_hvilYF-5mHmCgXLf4rATI6OUnAPB1Z5hIseHKImv8jra9vOAvzx1dsdJVqzpH2ozH4kBYyumQdJWPyydJ3o4T-ZIFQiiYLFiajJEH2I_WCMZ6KoCf5esgy13QE-z1P6dXrodca_UHc090rZwnT7s4T1d0x5V0qJFnA8KKPTBBfyTo3YhNc4rvGB7DOrwNHlK1oNz-sHqCyVX5i8zqqdWP03YTO6Ffl9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=v1vKd17rJk2gHoGiFZdnMWPYUUKH3uhUgb5Uf_pwi2LwjHAouQvMvhSZth3zZM__9mE5LkCvSushu_i2PfBjWjtueHut-sHPdQFpfu9u2CM_s4-LPxS78_hvilYF-5mHmCgXLf4rATI6OUnAPB1Z5hIseHKImv8jra9vOAvzx1dsdJVqzpH2ozH4kBYyumQdJWPyydJ3o4T-ZIFQiiYLFiajJEH2I_WCMZ6KoCf5esgy13QE-z1P6dXrodca_UHc090rZwnT7s4T1d0x5V0qJFnA8KKPTBBfyTo3YhNc4rvGB7DOrwNHlK1oNz-sHqCyVX5i8zqqdWP03YTO6Ffl9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطیب نماز جمعه دره سن‌گابریل - کالیفرنیا:
تغییرات بزرگی در آمریکا در حال رخ دادن است،
و اسلام و مسلمین نقش مهمی خواهد داشت
وقت دعوت به اسلام فرا رسیده.
مردم آمریکا «باید» به سمت ما بیایند!
باید بیایند!  باید، چرا؟  چون ما «راه حل »
را داریم! خدا راه حل‌ها را به ما داده!
قرآن و سنت داریم!  اینهاست  که
آمریکا را نجات خواهند داد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdDNGFzSvY2JmeeUJr6aknpqIxkvXe4-Bi2S96Hr3r_mKA-zaLBszUUrnvlKCuDgIPSKti91dsUcnjMHTlZU0ZXZrCBfzxcyyVWsSMODAmd_08i0BaVA_Yx-lrf953nJgaR1Q5awwcFqfkbQd4N5qdxX592RygLgUqSBJAm4x8DvXsrqEtSn6rc-Zldtuq12Ejl54wPrvZCJ3UMz6FGN_Ul5lVrJekmC_-KdHyxVjCPP4bIIjwKpCbBfKEr4KAZymnAmd6NPD38ZWxY6zELlot0D9EkaGEZ-MelEeDnwOynL0KxtWuVK_E5GZvjHlM_Ps3-eDfUDXjPfcjL79CRB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=H9erJqCG9RykqvQ4RUbGxVfDGi8wEEsAy-oq1lFhEddNtGYh9vc3OG5wMCecKFzFO2KhJcmbbqDFdkk_La2G4TVSscsUD1wqVB7zydisXsTNyfFIYC-sMF8-zRwj9eGWxkP9GNYiIVATsuooaKjlFcB-7EOgesj4cHzdqN5OAYJdnagJ-vZMZfOmtDUDr0bEdwZkS57eIUTFYr7dfxGOeTspX4ewMHGIYdtmrXVJ_ju1Dvkj_o7wHOlqW6HjZawKSc3SVuMpUaZzGHzEHMN33Y8ZLSHDCVFytl9-PeV50ikF1Hib0aY1Ff_IvpnUOT5Rz-RPdRVVvS8jJPT_9YyvnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=H9erJqCG9RykqvQ4RUbGxVfDGi8wEEsAy-oq1lFhEddNtGYh9vc3OG5wMCecKFzFO2KhJcmbbqDFdkk_La2G4TVSscsUD1wqVB7zydisXsTNyfFIYC-sMF8-zRwj9eGWxkP9GNYiIVATsuooaKjlFcB-7EOgesj4cHzdqN5OAYJdnagJ-vZMZfOmtDUDr0bEdwZkS57eIUTFYr7dfxGOeTspX4ewMHGIYdtmrXVJ_ju1Dvkj_o7wHOlqW6HjZawKSc3SVuMpUaZzGHzEHMN33Y8ZLSHDCVFytl9-PeV50ikF1Hib0aY1Ff_IvpnUOT5Rz-RPdRVVvS8jJPT_9YyvnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=DSXIzrVu41J4gg4eUVQFuhhVdpfYAv08LPM_jtKa5HMQ3tn-6f-uB5Ay4Zihnhdkv0NPaKjH45lNQjF62uDYxlODqgJMiI00hj1FmKOJCT-AwOC6hEW1FlKogllRluadXGCdf7iX4-MrP8TZ7n-dEBC78X1x_vVauUZTQmcqDAnPfkKlJByiLSlxCScln4XG9TVJAfRwvxuvB2MSUSUKSkWfib9SjCgBhcg82zKW-BScG8Cp54oAlsQ8W6kVzHJB2geLy2wpC0hgzuAICc_H1vCl6YDzRBEXoIV9nR9OiCiXRPFKn_zm6iq6fptPC9t8rpS4rUIAKLGMDwClqFlIDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=DSXIzrVu41J4gg4eUVQFuhhVdpfYAv08LPM_jtKa5HMQ3tn-6f-uB5Ay4Zihnhdkv0NPaKjH45lNQjF62uDYxlODqgJMiI00hj1FmKOJCT-AwOC6hEW1FlKogllRluadXGCdf7iX4-MrP8TZ7n-dEBC78X1x_vVauUZTQmcqDAnPfkKlJByiLSlxCScln4XG9TVJAfRwvxuvB2MSUSUKSkWfib9SjCgBhcg82zKW-BScG8Cp54oAlsQ8W6kVzHJB2geLy2wpC0hgzuAICc_H1vCl6YDzRBEXoIV9nR9OiCiXRPFKn_zm6iq6fptPC9t8rpS4rUIAKLGMDwClqFlIDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=GaeNwCDYLMTrLgTUP_-HrRCE72miDwX1X_hB6ZApQHaDLmaRC_2VWvv4WnmwUCirjS23NhwgvbYUjCJMPuOMgmKrYwZrqO5sWzOWkUtRsGO_LtkMuOySgBGpKceaIii9CRBOc-kiXE2qvVouhFRIaPNYo4wKxUoh5WzoliWTCtjkRiTVRU0mI1yq4BKQNf6zLH5LsSzNKtAK_yLIjVeLMfemJajQOrUT9RccMr7krSvsQi3zwjse4oqgUiyi6kMMp-rt6qyPaqZp92uGGDigpDelqYnpvm8BbpRe0QW2y_TMYmZ8dtpY2jY4L6lbCyvLRwzuaKgxCLTAPEtiH27Y8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=GaeNwCDYLMTrLgTUP_-HrRCE72miDwX1X_hB6ZApQHaDLmaRC_2VWvv4WnmwUCirjS23NhwgvbYUjCJMPuOMgmKrYwZrqO5sWzOWkUtRsGO_LtkMuOySgBGpKceaIii9CRBOc-kiXE2qvVouhFRIaPNYo4wKxUoh5WzoliWTCtjkRiTVRU0mI1yq4BKQNf6zLH5LsSzNKtAK_yLIjVeLMfemJajQOrUT9RccMr7krSvsQi3zwjse4oqgUiyi6kMMp-rt6qyPaqZp92uGGDigpDelqYnpvm8BbpRe0QW2y_TMYmZ8dtpY2jY4L6lbCyvLRwzuaKgxCLTAPEtiH27Y8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=MXhQ_R6Qbe4KMbB5wsEgxlC3sdCd74kzjrCjCTHKBlaHRumIHAVLv8kxyoFFUros_HAk6nAUXtiShduMSVUGj_y0IaNVPvt0mq8e1SaZGbZtNW7Yw0qx7TVIfxyZPFWiTHofgxrUVVHI24CwNjDJIWBJJahlHWPoQ2oNeukS8lMR7crY6orXlYCmjmYpyr6epjgd4VIVOz7bIo_kEp5rvZ5q1miyfimONN087zrafU9a-yXoJx9tqQYA_-k5Xro144cgjMaIWfvvad5_zjjlko4g6BI4azeuV2n25Wae5pWq5-KS67SwDhRcM5LZh-39ojc5vsMe9m1PCurd3Tvk-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=MXhQ_R6Qbe4KMbB5wsEgxlC3sdCd74kzjrCjCTHKBlaHRumIHAVLv8kxyoFFUros_HAk6nAUXtiShduMSVUGj_y0IaNVPvt0mq8e1SaZGbZtNW7Yw0qx7TVIfxyZPFWiTHofgxrUVVHI24CwNjDJIWBJJahlHWPoQ2oNeukS8lMR7crY6orXlYCmjmYpyr6epjgd4VIVOz7bIo_kEp5rvZ5q1miyfimONN087zrafU9a-yXoJx9tqQYA_-k5Xro144cgjMaIWfvvad5_zjjlko4g6BI4azeuV2n25Wae5pWq5-KS67SwDhRcM5LZh-39ojc5vsMe9m1PCurd3Tvk-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
