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
<img src="https://cdn4.telesco.pe/file/jVsoh1bFgrvecqjwEdrPWzmID6ZMXtk-B6wJ07ZVGluEX97op3sPXLSYJMi4B-0rQQ-OmwR4c0xpbk0pQWB01n5x11hr5SJApwinok1u9t0drV-MmkF56BxkIyLgIKk7qBZrquGBpgdioFX5s8dV0tYJz-4Echm6OEG_BEglJiFKutnxc7vb4dzmwbZEeg9DQ9Zfw-MBoJtXcOlKJTVF_j6xfV_Yv8uh6lGzZCPvXR0JIRDPMBWR4yrgjHKIFubGXZiPxLGuyyKg7vsGJNl_zoL8tc3M8zXngS-qipWvm6XrpA5eKXsj1dPQWaMnTybSUQUrbdY8DKRmnKIbAdFUDw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.92M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 18:15:48</div>
<hr>

<div class="tg-post" id="msg-653656">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88702db038.mp4?token=h7JO0UveaQt4zGpL61GVsPLWZQvKPiuJOGESfvibbNUv952Kljn22Lqe83m8f7rk4CewFuDIm8ECwzTq9baiFkhx5jN7GxTDZFb0EDPF4_JjbPXYKbzY95fjyUBwtENsR4vQyyCff59Ir2GycEscQUwoLZhZr_ptrUbBwkD74lfmZ19yfIKGYuO8m4QI26V-YgdZcOZ-Lhy9lFHg8VvLe1DfK5DQzuaTKN3ca6iFFxK_0Z697Dw2glhOY2_1GH7KX0ZUqRXnW_SLvw_eSoRthjU2xuAFVn5tYl3F-p_jldhe7mQMFNkatql4MdCU258pesE4Y8gSjZbbdoKzR2ZdCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88702db038.mp4?token=h7JO0UveaQt4zGpL61GVsPLWZQvKPiuJOGESfvibbNUv952Kljn22Lqe83m8f7rk4CewFuDIm8ECwzTq9baiFkhx5jN7GxTDZFb0EDPF4_JjbPXYKbzY95fjyUBwtENsR4vQyyCff59Ir2GycEscQUwoLZhZr_ptrUbBwkD74lfmZ19yfIKGYuO8m4QI26V-YgdZcOZ-Lhy9lFHg8VvLe1DfK5DQzuaTKN3ca6iFFxK_0Z697Dw2glhOY2_1GH7KX0ZUqRXnW_SLvw_eSoRthjU2xuAFVn5tYl3F-p_jldhe7mQMFNkatql4MdCU258pesE4Y8gSjZbbdoKzR2ZdCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا پایان شهریور واردات کالاهای اساسی توسط همه اشخاص کاملاً آزاد است
🔹
وزیر کشاورزی در نشست دکتر پزشکیان با استانداران: حداقل تا پایان شهریور ماه به دلیل شرایطی که در آن قرار داریم، واردات کالاهای اساسی توسط همه اشخاص حقیقی و حقوقی و بدون هیچ محدودیتی از همه مبادی کشور کاملاً آزاد است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/akhbarefori/653656" target="_blank">📅 18:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653655">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOFDBD8LgJ-CxVJy9e3EIEZ6h_GTIUivfIK-NHLM3xrvrsAj37r5x3qhRcbTDIYEjeKuVpkpUAN-8MR6hCPuIQ-p7-q9AhPxRwcd9K1QeXwyAR4jp68QENKqsO7dBublJuF78MTbY7w4i8LJXblAfA9N7kBV8h4ip8vAHgh42rzdUX-gGeXjfqjak4oBNieGRKhgXds62j8ZmdLt0oXFrAg2XI7L8esb8YcDCXi2526Cgpk7sQLFbaxBqaI2tHf4zjOotjKPQeduubIGBvDMSNz2b9U0NYzcRw0OfM9EmHDbix44KW8XnkUJeXI1VVLQhRV4VkSI1uSQc35QhtwpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فائو: تنگهٔ هرمز بسته بماند، جهان با یک بحران غذایی مواجه خواهد شد
🔹
سازمان کشاورزی ملل متحد: ادامه بسته‌ماندن تنگهٔ هرمز آغاز یک شوک ساختاری در نظام غذایی جهان است و آثار این شوک طی بازهٔ زمانی ۶ تا ۱۲ ماه آینده ظاهر خواهد شد، به‌طوری‌که یک خانواده ۴ نفره در اروپا برای خرید یک قرص نان باید پول یک وعدهٔ غذا را بدهد.
🔹
افزایش قیمت انرژی، قیمت گندم و برنج را نیز بالا برده است.
🔹
کارشناسان پیش‌بینی می‌کنند در ۱۲ ماه آینده قیمت نان در جهان ۳۵ تا ۴۵ درصد افزایش یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/akhbarefori/653655" target="_blank">📅 18:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653654">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای العربیه: تهران در ازای پرداخت غرامت از سوی آمریکا به ایران، پیشنهاد بازگشایی تنگه هرمز را ارائه کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/akhbarefori/653654" target="_blank">📅 17:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653653">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ویدئو کامل صحبت‌های بقایی، سخنگوی وزارت خارجه در مورد محتوا مذاکرات غیر مستقیم با آمریکا و وضعیت کنونی آن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/akhbarefori/653653" target="_blank">📅 17:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653652">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در شمال اراضی اشغالی
🔹
ارتش رژیم صهیونیستی اعلام کرد که در پی نفوذ پهپادی متخاصم، آژیرهای هشدار در شهرک شلومی واقع در شمال اراضی اشغالی به صدا درآمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/653652" target="_blank">📅 17:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653651">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
مصوبه جدید دولت برای حمایت از آسیب‌دیدگان بندر شهید رجایی/ رشد ۷۵ درصدی اعطای وام ازدواج
🔹
سخنگوی دولت: موضوعی که در دولت به تصویب رسید؛ تضمین‌های مالی تودیع‌شده برای فعالان اقتصادی آسیب‌دیده از حادثه بندر شهید رجایی بود که تا پایان مرداد ۱۴۰۵ با آن موافقت شد.
🔹
سال گذشته میزان اعطای تسهیلات قرض‌الحسنه ازدواج ۲۰۰ هزار میلیارد تومان بود که امسال با رشد ۷۵ درصدی به ۳۵۰ هزار میلیارد تومان رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/akhbarefori/653651" target="_blank">📅 17:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653650">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای روبیو: پیشرفت‌هایی در قبال پرونده ایران حاصل شده است
🔹
مارکو روبیو، وزیر خارجه آمریکا:
🔹
تنگه هرمز باید باز شود؛ ایران نباید سلاح هسته ای داشته باشد؛
🔹
ایران باید ذخایر اورانیوم غنی شده خود را تحویل دهد؛ معضل غنی‌سازی ایران باید در مذاکرات در نظر گرفته شود؛
🔹
خواسته‌های رئیس جمهور به هر شکلی باید محقق شود؛ اولویت ما مسیر دیپلماتیک است؛ امیدواریم که از طریق دیپلماسی حل شود؛
🔹
احتمال دارد که امروز، فردا یا طی چند روز آینده مطالب قابل‌توجهی برای گفتن داشته باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/akhbarefori/653650" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653649">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6590e81384.mp4?token=OH59cV-ijUeq-v1VQxaeIVFhujerbFmphr5ByOhmhpqy8A-OLYFDmMOC_3egKQuYw89ylLRkU8KwUhUL6TpBPJCJxobd0qlXZFiKGfEL7m-scAd0p0DtnXOiS1kC6KqMLV61qxZu1eNlf6p4QoZH-pNnO8aWACDR6NwBNoiA7ijnFJZQhAU-gocAlE6zuN_MOW8DnSKvWD8cWPY0THzk0_eJeZET1y-SZp8OfcB3rLlm_fT3BxN8cS86EABUk5C4NfJEfeBLufpmTL_tf0ckzgrn_orzZ1uENJNGuSNLJMa7UXkiS_4k7NS7dVKotvg2ePoeNpuE814c8Guf_jH5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6590e81384.mp4?token=OH59cV-ijUeq-v1VQxaeIVFhujerbFmphr5ByOhmhpqy8A-OLYFDmMOC_3egKQuYw89ylLRkU8KwUhUL6TpBPJCJxobd0qlXZFiKGfEL7m-scAd0p0DtnXOiS1kC6KqMLV61qxZu1eNlf6p4QoZH-pNnO8aWACDR6NwBNoiA7ijnFJZQhAU-gocAlE6zuN_MOW8DnSKvWD8cWPY0THzk0_eJeZET1y-SZp8OfcB3rLlm_fT3BxN8cS86EABUk5C4NfJEfeBLufpmTL_tf0ckzgrn_orzZ1uENJNGuSNLJMa7UXkiS_4k7NS7dVKotvg2ePoeNpuE814c8Guf_jH5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ موشکی رئیس کمیسیون امنیت ملی به توئیت تهدید آمیز دستیار ترامپ
🔹
موشک خرمشهر در جواب ویدئوی بمب افکن B۲
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/akhbarefori/653649" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653648">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCvybRcWcOlPup3NY1ABTyRf2bpVoQKxXC1w_PsGXyTJvxRV_WnURVpPgeCwsgJFQ4oMEsLij1z9KKcEDbejJVBG3RU9NJl20SBgVNALa3Vw8U4bsjp8-Q9I5C4Ed7HvikzBvXHhEWtfu5jk84w5eWSo42GW5NffxNAWZfVFBeCm0iKMsc2FOIz8P_fQQUKhndHvtQ1_IVxqrSdtDOrm2wuwV1fgXj8CyQ5cT2UCDo2ToIMQb_Uj8bqazJlfKbyWzaK-JVsbJ-rurcd2QRVGI7colygZFkzy7gY91CcfDNox8FRmc2ovK011NKPmPg5Y52GlGYX6mf29-noDjb-jYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ متوهم: ایالات متحده خاورمیانه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/akhbarefori/653648" target="_blank">📅 17:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653647">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بقائی: ایران بر خاتمه جنگ در تمام جبهه‌ها از جمله لبنان تاکید دارد
🔹
موضوع هسته‌ای در این مرحله در مورد جزئیاتش صحبت نمی‌کنیم.
🔹
می‌دانیم که موضوع هسته‌ای بهانه دو جنگ تجاوز علیه ایران بوده‌است.
🔹
ما این تجربه را داریم که دو بار در طول مذاکرات هسته‌ای مورد تجاوز قرار گرفتیم.
🔹
مسئولانه و خردمندانه تصمیم گرفتیم که موضوع مذاکرات را بر خاتمه جنگ در تمام جبهه‌ها از جمله لبنان قرار بدهیم.
🔹
اینکه در ۳۰ روز یا ۶۰ روز وارد موضوع هسته‌ای شویم مربوط به بعد از این مرحله است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/653647" target="_blank">📅 16:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653646">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پیام وزیر امور خارجه به دبیرکل حزب الله: ایران دست از حمایت حزب‌الله نخواهد کشید
🔹
سید عباس عراقچی، وزیر خارجه در پیامی به شیخ نعیم قاسم، دبیرکل حزب‌الله تأکید کرد که جمهوری اسلامی تا آخرین لحظه از حمایت جنبش‌های مطالبه‌گر حق و آزادی دست نخواهد کشید و حزب‌الله مقاوم و پیروز در رأس این جنبش‌هاست.
🔹
عراقچی افزود که از همان ابتدا که برخی کشورهای منطقه برای کاهش تنش میان ایران و آمریکا وارد میانجیگری شدند، ایران پیوند آتش‌بس لبنان با هر توافقی را به عنوان شرط مطرح کرد و این اصل تاکنون به عنوان یک مبدأ تردیدناپذیر باقی مانده و در زمره مطالبات حقه دولت و ملت ایران است و چنین خواهد ماند.
🔹
وزیر خارجه ایران تصریح کرد که در آخرین پیشنهاد ارائه‌شده از سوی جمهوری اسلامی از طریق میانجی پاکستانی برای توقف دائمی و پایدار جنگ، مجدداً بر گنجاندن لبنان در آتش‌بس تأکید شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/653646" target="_blank">📅 16:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653645">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkhzxVUWPszfhmu0hr2yKhE1ZwPGTNAqAhR2uBheFWVBIyRlqWYr_nChUxfzWIf72SqP_IsklxJ84X8qMvsk9FzS2oHAl2Cf1BH1eQd_IAqFdaipp9zyO8AGbbECjOS2FFjHq1c2afL_wzcpxemAxKt6hM3Ite2kUeJ_sAieXd-UilUgxTxSvhFpw2jKGII8_UqA2f2s-cy5_rZsSMefMOu1AEkfFvICF9YNqALFHgN1fAaeH0l02zxs2wNcuFoFkYIVZsWUlvPn5f332FyHJiW7jCsh7wROw28TDz3T2xTa1cAMStAgJGFc6tprVJEOP0MaUycUEBDRwQTvms5Xig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پول دولت به گندم‌کاران نرسید
🔹
رئیس بنیاد ملی گندم‌کاران:‌ دولت هنوز پول گندم‌کاران را که هفتۀ گذشته قول داده بود پرداخت نکرده. این در حالی است که آنها برای کشت بعدی نیاز به نقدینگی دارند.
🔹
سه‌شنبۀ هفتۀ گذشته جلسۀ تعیین‌تکلیف مطالبات گندم‌کاران به ریاست معاون اول رئیس‌جمهور و با حضور وزیر کشاورزی و رئیس سازمان برنامه تشکیل و ۸۳ هزار میلیارد تومان بودجه تامین اعتبار شد تا ۲ روز دیگر پرداخت شود.
🔹
در جلسۀ پنجشنبۀ هفتۀ گذشته سازمان برنامه به دستور رئیس‌جمهور مکلف شده پول گندم‌کاران را سریعتر پرداخت کند با این حال به گفتۀ کشاورزان پولی به حساب آنها واریز نشده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/akhbarefori/653645" target="_blank">📅 16:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653642">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8aK1havUQFgpU3PMO3yv_gaTUXuJVj9YNqod_WZlICd3vSlf8qOcRglr8aPhuaB1WPeGirKlMYasnK4UEyXJNdNdmsR4stYFpVC3-vjeiLeibPVa9z0XMro3pYxLpD7mRUfrBoICm-i3LeH9iA3WyKC8jj9cfoDvhtZn9n_Lgl2IZ_dPykcIIVfTnONzgUdP1MUIG9taF9dacPu2eOLnH2V7ee2BgE68rE2EzNB3jExkBk1O1NeDHvMYk3w1PnXUEjbNGYlWVj8-XyLn8nEKXhpZu-ZeTfQfX3wGvXx8Du_65D-nliI6GoxG3ePAfSzaFDemcNf13QUldTtmbFpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRr58xC8qAWaDL29QSwOnqDKUiRjJngUJ4mZD2gEJw9kjR7eOOXF7xvkbQb9D3BGuFDBughbt-brijjFro7_6l68qcZaVnEXui4S1ToWxaVXG2ZrafSGrNHYIyxzfSeYDc7XRc0Tl9df0DgcaxDHK5NponjrLWendvOutJPzYHPJ9T-Gxk940LQKYaWgxnJtVJ1Cn3vzxtE7zeVHWERT8bOthkZBwXVoWw37RLLLRlY-sR-3KaUkAn5lMJseAvyfWgdl8BaZtjTgEOx-gSmN0ABOkppgkH5lyBV8w4jvIv7OnFJli0aNIFI6d02yCOTJgmkkZL0ygI5l8tokr50kMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پزشکیان: سابقۀ مذاکره با آمریکایی‌ها حکم می‌کند نهایت دقت را به عمل آوریم
🔹
رئیس‌جمهور در دیدار فرمانده ارتش پاکستان: ما صرفا به‌دنبال احقاق حقوق حقه و قانونی ملت خود هستیم، اما سابقۀ و تجربۀ مذاکره با آمریکایی‌ها به ما حکم می‌کند که نهایت دقت را به عمل آوریم.
🔹
جنگ هیچ‌گاه برای هیچ کسی منفعتی به همراه نداشته، آمریکا در این منازعه پیروز نخواهد بود و این کشورهای منطقه و جهان هستند که متحمل خسارات جدی خواهند شد و رژیم صهیونیستی تنها طرفی است که به‌دنبال تامین منافع خود در منطقه از قبال جنگ است.
🔹
با توجه به بی‌اعتمادی مردم کشورمان به آمریکا به‌دلیل نقض عهد مکرر، حملات در حین مذاکرات و ترور مسئولان، جمهوری اسلامی با اتکا به روابط برادرانه با کشورهای دوست از جمله پاکستان، در مسیر مذاکره قرار گرفته، اما هدف اصلی ما صرفا تامین منافع ملت ایران با راهکارهای مقتضی و مناسب است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/akhbarefori/653642" target="_blank">📅 16:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653641">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNsgkIDf0oW6rTS8_NssGueBOygLnlFpLTCdVJi2GxDvvOBY8Imxyu53HR6aUpEwexAfeWXtSavV98G-9V0dyHZuTIAb88MT49YKNBpTAuBq98vWIVdiKEYXWjyxdetuICUIkiw-qYCbWemwfljaJrn2SBjPHIkTPE93cdJDtHNDygQ8SGKpWZdLV7eC5HowyER8pjxhd1GSrH767OlYfjtut8Ij8gfD7s_JOXXER8EfjdFw1Dp3ngPLMkJIUftDpoEfYWUGoeGLL7knL9k1gpnNa8dIupfyY3QxcyazB0Bni9Pc33jvKwtsEU1iIrXKwSBEhRD7JYfb-Qf7DSMLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاوروف: هم‌اکنون جنگ در سراسر اوراسیا جریان دارد
🔹
وزیر امور خارجه روسیه: در منطقه اوراسیا، این جنگ هم‌اکنون به‌ صورت گسترده در جریان است، پس از تجاوزی که کشورهای غرب با استفاده از اوکراین علیه روسیه تدارک دیدند و تلاشی دیگر برای تضعیف کشور ما و حذف آن از میان بازیگران کلیدی جهان، شاهد درگیری نظامی در خلیج فارس و تنگه هرمز هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/akhbarefori/653641" target="_blank">📅 16:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653640">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ارتش: آمادۀ مقابله قاطع با هرگونه تعدی دشمنان هستیم
🔹
بیانیۀ ارتش به‌مناسبت سالروز آزادسازی خرمشهر: فتح خرمشهر، ثمره ایمان راسخ، مجاهدت خالصانه و ایثار بی‌بدیل فرزندان این مرز و بوم بود که با تبعیت از رهبری الهی حضرت امام خمینی (ره) و با اتکا به قدرت لایزال الهی، توانستند معادلات دشمن را برهم زده و مقاومت و ایستادگی ملت ایران را به رخ جهانیان کشند.
🔹
ملت شریف و نیروهای مسلح ایران، به‌ویژه ارتش غیور و سرافراز ایران، امروز نیز در پرتو همان روحیۀ جهادی و با بهره‌گیری از تجارب گران‌سنگ دفاع مقدس و جنگ‌های تحمیلی و ناجوانمردانۀ ۱۲ و ۴۰ روزه، در راستای تدابیر رهبر انقلاب برای مقابله با دشمنان، آماده و هوشیار است.
🔹
ارتش با تمسک به آرمان‌های رهبران کبیر و شهید و تحت فرامین حکیمانه رهبر معظم انقلاب، با عزمی راسخ و اراده‌ای خلل‌ناپذیر، خود را برای مقابله قاطع و همه‌جانبه با هرگونه تهدید و تجاوز دشمنان آماده نموده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/akhbarefori/653640" target="_blank">📅 16:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653639">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
امیر سیاری: آماده خلق بیت‌المقدس‌های دیگر هستیم
🔹
معاون هماهنگ‌کننده ارتش به مناسبت سالروز فتح خرمشهر: ارتش جمهوری اسلامی ایران و سایر نیروهای مسلح گوش به فرمان رهبری و گوش به زنگ اشارات این فرمانده مقتدر هستیم.
🔹
در پاسداری از تمامیت ارضی و استقلال کشور، مهیای خلق بیت‌المقدس‌هایی دیگر در برابر هر فتنه و جنگ تحمیلی هستیم و این را دنیا بداند که هویت ما با ایثار و وطن‌پرستی گره خورده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/akhbarefori/653639" target="_blank">📅 16:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653638">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
لحظه حملات پهپادی حزب‌الله به مقر ارتش اشغالگر در بلندی «العجل»، پادگان آویویم، رامیم، راموت نفتالی و معالیم گولانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/akhbarefori/653638" target="_blank">📅 15:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653637">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
بن‌گویر از ورود به خاک فرانسه منع شد
🔹
وزیر امور خارجه فرانسه: «ایتمار بن‌گویر» وزیر امنیت داخلی اسرائیل از امروز از ورود به خاک ما منع شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/akhbarefori/653637" target="_blank">📅 15:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653636">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7WOwkT0cZC121CIq9eeSmti5r9eWUXZncoEZhEo3Prn-Xj6603fCQDf8tVr6PIKshJfOA1gsdtr6FiCEDjBymjizYPLlOFHLAG9PUWXeT9bF9m_TLKkQKB4mX0Se_J0cLytn3A0_MEcJVBCRnr1Uaywr7pX_W9W6obIb6CblR4oPcrGrYvYbPzeupc4D_cenbz0w4z1oT-Y-Uva-p3qNQvHJs_-OoDgHauEUpHc7XMXUqjH6LRb8y9HABI6yQTqnvhYKVVzbUJW6ybKfWim9WTJ4BkkF7cxTgw_nhBEfsTjrD6N48-NDqB0EhrxE8veFeK6i1bp2IdaSMNcBtkaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۴۰ کشتی در انتظار اجازهٔ ایران برای عبور از تنگهٔ هرمز
🔹
تصاویر ماهواره‌ای نشان می‌دهد که حدود ۲۴۰ کشتی در آب‌های خلیج فارس و در پشت خط مرزی که ایران آن را به‌عنوان منطقهٔ تحت کنترل خود در آب‌های خلیج فارس تعیین کرده است، جمع شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/akhbarefori/653636" target="_blank">📅 15:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653635">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWaWvEJ-SfkrFN3gnFwZ4KxV1w3dXgrX33svLsNAJ_lpb48-ePm_83OnRqbMYfPsQ2h-yN1cD8quvg66YOBgnqoYPZQCC7a1bTal0w-piT8PycVx5Hz1P0WZ9X__WkLXDfEV3fjHXKRg81xu1XFwBvykhinij_Ym1J-BIURBgIPAs0NUhd99DidPpkSXtbn149DHCd-sqF7EtnOFq8V-wItNiKEt0i7AX48ReyP87MDzJcFY3YFYJS6AalA6HwAv6SvPR_5HM9pzl9NTu2uUzzC-6poYypo4DZ-EgSj-wobKCxPnN91V7iVOXf5SadDO3-turVxyj4peaVt3aS9NKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقلیم «جبل باشان» اسم رمز اسرائیل برای تجزیه جنوب سوریه
🔹
شیخ حکمت الهجری، یکی از رهبران دروزی‌های استان السویداء (جبل الدروز)، با پخش یک قایل ویدئویی بار دیگر بر طرح جدایی از سوریه و تشکیل یک اقلیم خودمختار تأکید کرد.
🔹
او همچون چندین اطلاعیه پیشین خود نام این منطقه را «جبل باشان» گذاشت، نامی عبری بر مبنای متون توراتی که ادعا می‌شود بخشی از منطقه «کنعان» بوده است. طبق متن تورات، « جبل باشان شامل حوران، جولان و اللجاه می‌شد که همگی از صخره‌ها و خاک‌های آتشفشانی تشکیل شده‌اند و خاک آن بسیار حاصلخیز و آب آن فراوان است. در آن گندم، جو، کنجد، ذرت، عدس و خلر کشت می‌شود».
🔹
نکته قابل توجه اینکه رژیم اسرائیل پس از سقوط بشار اسد دست به بمباران بی سابقه زیرساخت‌های نظامی سوریه زد و حدود ۸۰ درصد دارایی‌های نظامی این کشور را نابود کرد؛ نام آن عملیات نیز «پیکان باشان» نام داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/akhbarefori/653635" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653634">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs98Hjv0vHioMM2UrDPJZPz94bN6Mt4VH3o-2r4_MgAve0mPDOAC4YgSwCEv6jXOCseAb8NFAXb3CCjgBkOuD61JESWY-Gb2gLTY1_jf4dY-expl5hI0Z0ytETddHD73iVZH1OYMr08DnIp52V3JmZz9FuibwxYNxL1bR_5l6YaLFyxVgAO__VwT0ItYwsCnVd9XrLupJr6ZjNftkLCgjSp5GQ80quP9Gsvk6y5lrzT7yWrUKawumZAfcVX-6iIUwQLAqlViNhmAF9QseNRTWrPR7CBTbQFYGFGzqKylPeVMW_zb8AirqAkb8Y-4KxNCCTtrdFM-PC_oceL_YxmNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وام ودیعهٔ مسکن از اجاره‌بها جاماند
🔹
با وجود افزایش چشم‌گیر اجاره‌بها در کشور از ۵۰ تا ۷۰ درصد، دولت سقف وام ودیعهٔ مسکن را حدود ۳۳ درصد افزایش داده و خبر می‌رسد که سقف تسهیلات فعلاً تغییری نمی‌یابد.
🔹
امسال سقف وام ودیعه‌‌ مسکن در تهران ۳۶۵ میلیون، مراکز استان‌ها ۲۸۰ میلیون، سایر شهرها ۱۸۵ میلیون و روستاها ۷۵ میلیون تومان می‌باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/akhbarefori/653634" target="_blank">📅 15:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653633">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIyTpl1CY3uAi5kLmOepeTmTIdcbAp_emRWqHsUJI6pLlvgqv9k_QqQfjlLHfCAs0ajRS3IxgpxLnNELb2zs_Tf2IN2bVJinj4SpT8HjQwfOitAP3qHkY3CWC84Cle5bAtHaKFaPc7blTi_sSdndiU5A_Mo6gdpMhUX87execD1m6z8A1uzie6v_kJan6fS4fsW5Q_ECRcQDwIrjs0MU6aEyc-XHXxDXWoNMrUNdLwdFk350vkh5V_eslpuY-efun1Vx0XaM_LfYZlTGtne_6EAFHtmtbFzDVhiGnjyG6be9FVMOdxqYbBAQWlAWTN-NyK_BsoGsDdRzODJq1nPv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکاپوی بیشتر پاکستان برای یک توافق؛ اختلافات پابرجاست
🔹
سفر فرمانده ارتش پاکستان عاصم منیر، گفتگوهای مربوط به توافق بین ایران و آمریکا را وارد فاز جدیدی کرده است، اما همچنان برخی اختلافات به قوت خود باقی است. تلاش‌های برخی دیگر از بازیگران منطقه‌ای از جمله مقامات قطری هم تا این لحظه، نتوانسته واشنگتن و تهران را به یک توافق برساند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/akhbarefori/653633" target="_blank">📅 15:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtHKcicpj-UEqZtJgfPcJnA40bI5bsI7xNnko5_vA6guiub8VrNa3ddJeoxUomAUqUudhXgyUBbdhY-MfrV3sC53gdtZw1K-oLtPU-KJPINtBzGP2qZYuMUjBAVo1V3JsW838ovW21aNBCHABGi3DLZteTUHaFgx87ySDTIoGnYiAZlCSFVIwc3hoFdxEKX3tNqaJtSRUzSNkfBpptBNZExsS7FldZU_hwbid0BFi4ppwNASIhEF725lmtqKgXk676c7XDxmbhtJFDHEO7w96OmwYWvtI5NOgaRi0-tEHD2qwBfgHo92iAM4zZp0bcVoZt8qTUb9MLy-QKznZhHRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترور ایوانکا ترامپ توسط ایران | بازخوانی توطئه‌های ترور؛ تلاش واشنگتن و تل‌آویو برای جبران شکست‌های میدانی؟
🔹
همزمان با تشدید فشارهای سیاسی و نظامی بر محور مقاومت، در هفته‌های اخیر دو خبر امنیتی با محوریت «کشف نقشه ترور» توسط رسانه‌های غربی منتشر شده است که بسیاری آن را تلاشی برای برساختن «مشروعیت تهاجم» به ایران ارزیابی می‌کنند.
ترجمه گزارش دیلی‌میل را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3217212</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/akhbarefori/653632" target="_blank">📅 15:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای خبرنگار الجزیره: یک شخصیت بسیار بلندپایه منطقه‌ای از ایران دیدار کرده است
🔹
یک چهره بسیار برجسته منطقه‌ای، بی‌سروصدا از تهران بازدید کرد تا آنچه را که بسیاری اکنون «شکاف‌های غیرقابل عبور» می‌نامند، پر کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/akhbarefori/653631" target="_blank">📅 14:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تماس تلفنی امیر قطر با ترامپ درباره کاهش تنش‌ها در منطقه
🔹
دیوان امیری قطر از تماس تلفنی امیر این کشور با ترامپ ،رئیس جمهور آمریکا خبر داد.
🔹
دیوان امیری قطر افزود که امیر این کشور درباره  تلاش‌ها برای تحکیم آتش‌بس و کاهش تنش‌ها در منطقه صحبت کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/akhbarefori/653630" target="_blank">📅 14:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653629">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/646a9bc335.mp4?token=OT9anw2BA8t1ii6wqJPR_LAv-Xc-2rDVMEaVefK8D7d8oTRp-GiJpGN5QTEgY55yJw6a3uLE7blD3iinv3QZy7ZW24EJ1TMastzz0Hyhqk-RWJCQD-qRuTCU_itVfGtF1V2jrjjexLJEqZRtJ7N0b2vthc_rNg5wCExEzxKOQyj72MwPeiLv3byRIlteKvDUmNpJrbAeqL5TVdmp4daOI12sr9zh09fGUx2yh5JDWVN8lPS-ZoJhYBnYkp12UjNAA0oSDzp_6Wu82NaVcK4rNtypIm7DYwPNMnNfsBOoGgJklGKSPf0VBjuAlLflSXve7dCuyTFPX0F9jBjx-isDvRB4nYIZCtHzqTBKIOK_k23O4WHmKwovINXGRe5i3hxckD-DrXD4F62rBwyN9rorHTgAq7zAglbRcP3KNKvtjGe7ziJ6jdUw698y_s4aQJaq1lRCaVzzmSI8Z_v_p7cY0LNeaIeByW0yNnp9xNCWCKrGtQ3w407a7efMvDP4x2RC4rH8xShgIwfU-4KG4jsx3Nxz47xUA0MSSWcGuE8IyKIuL8DWuWND9KSYK4K4BWsLXX-Fn6bsVDgghhX0VpBuu5Gpq_-ELBYN0rq5CYm7bSTJi602w6xISRX-KWDx4tIBFi0p2wlyExtHKBOI6A-u0OLJpsKgeDCXFT7orJI5kjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/646a9bc335.mp4?token=OT9anw2BA8t1ii6wqJPR_LAv-Xc-2rDVMEaVefK8D7d8oTRp-GiJpGN5QTEgY55yJw6a3uLE7blD3iinv3QZy7ZW24EJ1TMastzz0Hyhqk-RWJCQD-qRuTCU_itVfGtF1V2jrjjexLJEqZRtJ7N0b2vthc_rNg5wCExEzxKOQyj72MwPeiLv3byRIlteKvDUmNpJrbAeqL5TVdmp4daOI12sr9zh09fGUx2yh5JDWVN8lPS-ZoJhYBnYkp12UjNAA0oSDzp_6Wu82NaVcK4rNtypIm7DYwPNMnNfsBOoGgJklGKSPf0VBjuAlLflSXve7dCuyTFPX0F9jBjx-isDvRB4nYIZCtHzqTBKIOK_k23O4WHmKwovINXGRe5i3hxckD-DrXD4F62rBwyN9rorHTgAq7zAglbRcP3KNKvtjGe7ziJ6jdUw698y_s4aQJaq1lRCaVzzmSI8Z_v_p7cY0LNeaIeByW0yNnp9xNCWCKrGtQ3w407a7efMvDP4x2RC4rH8xShgIwfU-4KG4jsx3Nxz47xUA0MSSWcGuE8IyKIuL8DWuWND9KSYK4K4BWsLXX-Fn6bsVDgghhX0VpBuu5Gpq_-ELBYN0rq5CYm7bSTJi602w6xISRX-KWDx4tIBFi0p2wlyExtHKBOI6A-u0OLJpsKgeDCXFT7orJI5kjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واشنگتن پست در گزارشی ویدئویی به بررسی آسیب‌های وارد شده به پایگاه‌های آمریکایی در منطقه پرداخته است
🔹
در گزارش این رسانه آمده است:
🔹
۲۲۸ سازه یا تجهیزات در ۱۵ پایگاه نظامی آمریکا در خلیج [فارس] هدف قرار گرفتند.
🔹
میزان خسارت بسیار بیشتر از چیزی بود که اکثر مردم تصور می‌کردند.
🔹
برخی از این انفجارها واقعاً عظیم بودند.
🔹
این نخستین بار است که یک دشمن توانسته تقریباً در لحظه، تصاویر ماهواره‌ای از خسارتی که به ایالات متحده وارد می‌کند منتشر کند.
🔹
این موضوع از این جهت مهم است که ایرانی‌ها توانسته‌اند اطلاعات را در سطح جهانی کنترل یا تحت تأثیر قرار دهند و نشان دهند چقدر به پایگاه‌های آمریکایی ضربه می‌زنند
🔹
این جنگ احتمالاً طولانی‌تر از آنچه دولت تصور می‌کرد ادامه پیدا کرد و توانایی ایران برای حمله به پایگاه‌های آمریکا بیشتر از آن چیزی بود که قبلاً درک شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/akhbarefori/653629" target="_blank">📅 14:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653628">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlftL6WgzsrTvjJpZsxK33nhta29GWvCQBHnKltbzodbM2a321cZhUHHFnnkgGzt-PY7YXdd3zFH9VJ4HQ-d7-dFAk4oTvesUTr77V_eGVlwps8nbu8bT7ZfXDq31UJSq5mvE2l18wF3DNAg0DizeORRO-fdUVvW-3eBLUHYmr9lZCNmdljMWY5z0wVx2ktQIk2CIdPEhEwgMdqHYTFn8ozQqG8jV-xcfg9H_2ECxq5Ezvtrnof7EnHaFbstOSEOaNWkVjQY3V9VyTUvIo0DsxLAuU0iA4_9ZACNjmzu0PhktK4mUy0nr7bdHNI57ldN4ksS5CImKNNZeVCFpR9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باشگاه تحلیلگران | هرمز؛ برتری ژئوپولیتیک بر تکنولوژی
🔹
از منظر ادبیات بازدارندگی در روابط بین‌الملل، هرمز ابزار «مجازات مستقیم» به معنای کلاسیک نیست؛ ابزار تولید ریسک سیستمیک است. ایران با حفظ این اهرم، آمریکا و اسرائیل را به این نتیجه می‌رساند که جنگ علیه ایران نمی‌تواند محدود، قابل مدیریت و بی‌هزینه برای نظام جهانی باقی بماند.
🔹
آمریکا برای اثبات کارآمدی قدرت خود باید امنیت عبور از هرمز را به طور پایدار تضمین کند؛ ایران برای تضعیف این تضمین کافی است نشان دهد عبور عادی، مطمئن و کم‌هزینه بدون لحاظ کردن منافع امنیتی تهران ممکن نیست.
🔹
به بیان دیگر، هرمز به ایران امکان می‌دهد میان دو رژیم امنیتی پیوند برقرار کند: امنیت ملی ایران و امنیت انرژی جهان. آمریکا و متحدانش تمایل دارند این دو را از هم جدا نگه دارند؛ بدین معنی که ایران ناامن باشد، اما جریان انرژی امن بماند. منطق هرمز این جدایی را رد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/akhbarefori/653628" target="_blank">📅 14:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4582342fa.mp4?token=anOIB_NpYx56VAjscGRgzCL_xUBrRBxY7HCH5_Y38ivbdqMMX7p9UlrqVZ7tY8_pqqCVX_gPdsHk08phNDKzqSMTEYcgNw9dxyfpaZ__u6v7esbCwFQvIuxDPopAIkcTf0RkmCkXDrUQx4eP-7rGARih8FH5Nq5fC0JOugtUmt2xY52_sRvgterQPjooFhc5zTJTia9HVITf-e2mlqm5etZoaMsXFofJ-vuXR4GDDyr29LjPheisDLkZANshiVKOIGmZQJjfaSh8xJQ0YMUHoBq-juimFaLmsSfpEWyRuCjHRT5KSzdguQpYzwxZIUkG-QeUuPJAncSZbPO14qrSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4582342fa.mp4?token=anOIB_NpYx56VAjscGRgzCL_xUBrRBxY7HCH5_Y38ivbdqMMX7p9UlrqVZ7tY8_pqqCVX_gPdsHk08phNDKzqSMTEYcgNw9dxyfpaZ__u6v7esbCwFQvIuxDPopAIkcTf0RkmCkXDrUQx4eP-7rGARih8FH5Nq5fC0JOugtUmt2xY52_sRvgterQPjooFhc5zTJTia9HVITf-e2mlqm5etZoaMsXFofJ-vuXR4GDDyr29LjPheisDLkZANshiVKOIGmZQJjfaSh8xJQ0YMUHoBq-juimFaLmsSfpEWyRuCjHRT5KSzdguQpYzwxZIUkG-QeUuPJAncSZbPO14qrSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم نقض آتش بس/ حملات سنگین هوایی رژیم صهیونیستی به جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/akhbarefori/653626" target="_blank">📅 14:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
قالیباف: در صورت حماقت ترامپ پاسخ ما کوبنده‌تر خواهد بود
🔹
نیروهای مسلح ما در دوران آتش‌بس به نحوی خود را بازسازی کرده‌اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده‌تر و تلخ تر از روز اول جنگ خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/akhbarefori/653625" target="_blank">📅 14:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
قالیباف: ما در حال مذاکره بودیم که آمریکا جنگ به‌راه انداخت و حالا می‌گوید برای پایانش مذاکره کنیم
🔹
در آتش‌بسی بودیم که شما واسطه‌اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا به‌دنبال برداشتن آن است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/653624" target="_blank">📅 14:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
قالیباف: از حقوق ملت و کشورمان کوتاه نمی‌آییم
🔹
رئیس‌مجلس در دیدار فرمانده ارتش پاکستان: ما از حقوق ملت و کشورمان عدول نمی کنیم، مخصوصا با طرفی که اصلا صداقت نداشته و اعتمادی به او وجود ندارد.
🔹
ایران همان‌طور که با شجاعت و اقتدار در میدان نبرد از کیان ایران دفاع کرد در عرصه دیپلماسی نیز با هوشمندی و قدرت برای احقاق حقوق حقه ایران و تامین منافع ملی کشور کوشش خواهد کرد.
🔹
نظامی ها بیش از دیگران و بهتر از همه ارزش صلح را می‌دانند، اما همان نظامیان هیچگاه اجازه نمی دهند، عزت و حقوق کشورشان لگدمال شود.
🔹
ما در حال مذاکره بودیم که آمریکا جنگ براه انداخت و حالا می گوید برای پایانش مذاکره کنیم.
🔹
در آتش بسی بودیم که شما واسطه اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا بدنبال برداشتن آن است!
🔹
نیروهای مسلح ما در دوران آتش بس به نحوی خود را بازسازی کرده اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده تر و تلخ تر از روز اول جنگ خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/653623" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
حزب‌الله لبنان اعلام کرد: ما با یک پهپاد، یک سکوی پرتاب گنبد آهنین را در پادگان برانیت در جلیله هدف قرار دادیم و به هدف خوردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/akhbarefori/653622" target="_blank">📅 14:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjgOURoqikfD_auN47euU8Gy2QePsljdhiiZpIP-0Vm-Jwmvf4zEDM4BHzAZhDF21RZOHgB1yC0TjtOLMsfxmdEH63hdiDghuj9S8qEwbZZdo1irkLGzFfTgJVpAqfaa8qV_WI04ypwoqbVT2s2bSRzmPCaiYK8Lz0JpCY7B8k1CJfvxboJ82uUvqsx-0o0hhfd6GKMnR1or273BtvZ5A_wC_CF3go3e1mRteXhUwIyuKhkBcQnMT4e52I_DYTN_dNcnS7FeGTt5d-DC6YuWyys69srt2F6PtPxcCbFyo9yGVSE0krYlLx-AIkuLv1HAE0WYTfbahcZcmUFmErXLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
رضایت اولیای دم برای اهدای عضو همچنان ضروری است.
🔹
طبق آمار، ۹۸ درصد خانواده افرادی که کارت اهدای عضو دارند، با اهدای عضو موافقت می‌کنند.
🔹
این عدد برای افرادی که کارت ندارند، تنها ۴۰ درصد است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/653621" target="_blank">📅 14:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eb03297a.mp4?token=c-9E19w1l9_K_NkyjWrJEQobQN6vfLBTykdVNj0TS21IF7DA4lbv7fSmlqXXK8xql938szG2PnE219QiCRmuEfXE5NsSFqb2Y1KdItT62z3cNy0R0EdWJnWWaoUBTUbBfj1lzefD1HzO4pQDyYutBdGr8Df6hUu24kEiHGLlEscscN6OdLUNb3hYokjfDnk_tHu5RfdugnHAXR2sDKiOqgZLPYuCc1by7-Lk3JAXzSf8_wA3k8fV1UavPZe_oLcq3gq3WVDG4hBFaoHTtphDJ427IasNTM9j1qzYMtXrqv3CPbMQnos5yR5AYNoVQVsZd52Org8v83dRYfVZWHm8AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eb03297a.mp4?token=c-9E19w1l9_K_NkyjWrJEQobQN6vfLBTykdVNj0TS21IF7DA4lbv7fSmlqXXK8xql938szG2PnE219QiCRmuEfXE5NsSFqb2Y1KdItT62z3cNy0R0EdWJnWWaoUBTUbBfj1lzefD1HzO4pQDyYutBdGr8Df6hUu24kEiHGLlEscscN6OdLUNb3hYokjfDnk_tHu5RfdugnHAXR2sDKiOqgZLPYuCc1by7-Lk3JAXzSf8_wA3k8fV1UavPZe_oLcq3gq3WVDG4hBFaoHTtphDJ427IasNTM9j1qzYMtXrqv3CPbMQnos5yR5AYNoVQVsZd52Org8v83dRYfVZWHm8AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شمار قربانیان حمله اوکراین به خوابگاه دانش‌آموزان به ۱۲ نفر رسید
🔹
شمار تلفات ناشی از حمله پهپادی نیمه شب اوکراین به یک خوابگاه دانش آموزان در لوهانسک به ۱۲ نفر افزایش یافته و ۹ نفر زیر آوار مفقود هستند.
🔹
لئونید پاسچنیک، رئیس جمهوری خلق لوهانسک، همچنین گفت که روانشناسان و کادر پزشکی به کار خود در مرکز اسکان موقت ادامه می‌دهند و والدین حمایت‌های لازم را دریافت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/akhbarefori/653620" target="_blank">📅 14:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تقدیر رهبر انقلاب اسلامی از میدان‌داری مردم سیستان و بلوچستان
🔹
زاهدان- رهبر معظم انقلاب اسلامی با اعزام هیئتی ویژه به استان سیستان و بلوچستان از میدان‌داری مردم این استان تقدیر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/akhbarefori/653619" target="_blank">📅 14:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653612">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLlbsgDJV_f7fzqqx8gdNRlFtKKi7IlcTjVq_j1o_EOC1iM9-AXap7od701WxniPpj47sWbWgtr6f-5EkSQ-tUAX5McUlX_7AKPMolEdetSrULvURYGiX4a98q_txccFeYOK_6KH96r6L0jedmloAZZG1rPTzxGEAS5-Bh5xHEaeZxvSMRubI-_7FnFWYOL5lqv8dlVhiQJeMtpA6W5F3aHqw6kqeiml4aJeOhNgfNWgKLZ5gpCTHnppqC4EW1jbqKWFBwMff8LJ8WTuLIG5hgX1ix1K_wXGJkuxQW3HLYEwgZ-U7LnKMrlKvuYxJZ9411N3SPF55SmHQr3ruX3WdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vncKMXAVClrxZgUNBryD24tvLegPe9KbGXduOIkia5Me4Km4gIm0XJeXyQ7nIbl60Xm-1w2kj-FRM7BiNkL36qVEOROdSLl-hBK2kBpfiW3Aouqdvz04_LuCtxc3eFEShu8FiZKaCTcQU4mI7-z9mi31bEY9Tn8TF4MKNnD1xMPAW7b7A7_4MXrEpm1iFoSyTXGQ7QURW4n6py9hJu4xP5pe2gzz4b3hLqAdFwqdIYfZ-G6QfEqo3v9Nw7KQmFuvyQmTFDMbpjRmE5WYWsiau_5dRzac4Au_rSN2BII8cYRhpv1ly3m0AadZEyKYC7RA-vnaunKqn_NHfWi8SZun-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXeSmsS1DVty2lmBsXCiXFDftRkN6etipHJkE7gWmSGEWb8kRmrTRt_mvVqgliTglKSxHFouuY4oTP8Fe6tanN7JP9Q50WlNun3UInmppofpX1TCMgoqPIRdVdVrAoLin7eDKHr87w9p4ebU9qfojLkH1NwP2SRRyzTg6ZfXjZJn4yVOveYEScxJxZIuc5XOvlWqrXJk7DiF9eK8zG6AvC6b9Fx3Br0hiCaMi_0u10Wu8Dl2Yd16g6eip_DUWVqOzRBdRvUhS9KRlIuFPOzD5jZCtig8GSbu2M_fnEVSe6PaFyoUJdzN-oE8SaptGGHaJ3ElhBLXnOmhRnr_3diLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooh5BwT6dktOmhEcqxC45zoss-jPGhxpOCzJox7BkwPU4MyawzEX6ewxbgO56DQykMFa0cm32-0unOmFywYVrCB9wXxUN4sEcWBA1_JLQhXWFfGScKNkGi5DAk8yTcHzGXbIMpgJ9UT6fMy7ke6X3j51-sRM_0SxDgTfsge8esUIGtZxOYQ0l1zphipq6YV0p6MD_Ev1wdIZhQftMxpOG8MQEwnIxR77XICyDta0P-QtY_KBXxM4GzegDlQfSdWFy0X98iO6KBdEQ1PCwjVX5DrDMyzgfttaFyDIewE0Zxhf6hfSutDBOZl0PTyS9APbNqjLFoXPtn8BUUAxz1QNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7IXQt8qFvUjKr24ANns3ADV-6MdI0ZuFhdZwXhUGi0k3mFLawO6485Ss-ZFY-KMC8P9EgVbWtzRrG5nSEATe25bGtLLvkdLFKYzAaazlRx6L4Cm80NUHgPRWFkdc93AxFKGZ9Meudpvn7K2Ome3lAJTtCDY0NkSaCrDwtf6-ZfDgpTrN6VPAu2ZUIH15NL3JbcDtIJa1Ui2WjFzLjB_boHUL4i0jmjfj2djYwu58DyWrKOO2XPzphMwS8IbJWPddVpmDhC3i58b1NZsXsNi_JsHb4zdYum_eFeguW4RSLZ4HTUvRdgXuRdESHXDkzJ8Y2CQTw95GOatY6DKQ2Sefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iL7BoW-4d3fdAhwga--2PO6k0pLgALyB2Q8dJvV_T2i-y6m1ZrFAqeSHEHGx33fGX8E9YLpUWXQgeTAihnSxv70tWiDr5MPfk9Oz7qvM_2CfuaB127TigYXdB5K-sYdAEM_byR3mm8qvU9a8s2y4ntJ_UuNM3ho25QgNm2K2pkHAbjJwDWdttj__q11KC5pzWAHrUSQNWJ-Gk-aT-eO9KF2e8aEgkmjB1L3g-4uuaGLdaQjWA_dhfP6yFvERunklBAQ_Arx3_vKmGArSTsdpmcWXW21I-0N00ps-rUQwpfbo9C9XIfEG8KKIFuM23I1zyHMVoPfxwx9ZcGo-Z6hmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hh-bDCy8whbm4mHZBeeT30Y74XAr9Q6AjtuJDY9lEj8biEGGjsOmqVjDA-vQVP1KgMVNBXDe32286iwAi3mf4Xlma2w2rwFg901OoJ5p8YVNC5eXWIUpYci8BxENnXObm6OKIkugj6oONVuxnWuWtkn3xWa-V6koU-RUdNe_1kln4g5LpZEB6uiyxLOutPVzLsfmbsehxyhcBFSBoJh8C5OlpgwdmOxHuaviDWZirIBVGa2gS8Zcj7P-ZHc74RQibhGVwv61SBZNabMu83xCeUBLFyj3sHDZEmepnXkGcW9ULeE7Jxonr8_QuzIoYnVUrmyT58sZm2q_-d3Mfe920A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کارگاه موشک‌سازی در همدان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/akhbarefori/653612" target="_blank">📅 14:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653611">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejse1BIA5Ky_Zr-931pec02KPAeZlu9bjLGtC3tQbNWmfK03G3Lxy1Fray-kEr25gEKDSiDWKcddeHOOqcCHFI8de5vzgsHyS8GMZ6VBSnOsvBCyDuBat9qgeA92mmPsEcjbb3YAMeqOel05i0BIdZKLuXts5EkspbKdgEPPrY687ntG0o473u_HMD-FI2GfPdWXIZPNNUX4jrtUCJL5yqEAVl2U6soP0BuHgYRJSMdiadCo7ZSO9SMyGnAT1E6fqiwr-SDEq3K_6rxRtiQSN9y1h7Ek7vzTDQtc947-3Vna4DCtI0jjYoHtEoQxF_b45DCnRq5EgTQMi3IkY1OxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمار شهدای غزه به ۷۲هزار و ۷۸۳ نفر رسید
🔹
از زمان اعلام آتش بس در ۱۱ اکتبر ۲۰۲۵(۱۹ مهر ۱۴۰۴) تاکنون ۸۹۰ نفر در غزه شهید و ۲ هزار و ۶۷۷ نفر دیگر مجروح شدند.
🔹
با احتساب این شهدا، شمار کلی شهدای غزه از هفتم اکتبر ۲۰۲۳(۱۵ مهر ۱۴۰۲) تاکنون به ۷۲ هزار و ۷۸۳ نفر و شمار مجروحان به ۱۷۲ هزار و ۷۷۹ نفر رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/653611" target="_blank">📅 13:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653610">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
نورالدین الدغیر: وساطت‌ها بین تهران و واشنگتن به مرحله‌ای رسیده که یکی از سران منطقه‌ای به طور مستقیم برای پر کردن شکاف‌ها وارد عمل شده
🔹
ظهور قطر در این لحظه حساس به طور مستقیم و بر اساس اطلاعات و منابع موجود، نه صرفاً به عنوان نقش کمکی برای پاکستان، بلکه به عنوان نقش محوری است.
🔹
منبعی می‌گوید که احتمال دارد یکی از میانجی‌ها به واشنگتن سفر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/akhbarefori/653610" target="_blank">📅 13:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653609">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyIrjuSEk4LQ3vswJ6B5xtoBSJYQpYgStljrVsqz1kKCYvDwmx8Gdw0d_hF8WKc6tZLXVw3PWAZqlIvXDKG5AXIZVwsMuPaWzb1wq0f9v5OPZOzwAptfnLAT85Fg42rAgZf8IVM2192e_O2dRL10z_OsIwXmE0SsQxtkUR8fi4TVkW97TVCmU6Ow8jyz6TEJm3zjdkvmH4e4CbU0FdBdG3c55JUDIfLq2ILXAEAojYtbpLV1WE-I1oa6WaPtdvmAfZwAfW_vb8ljQJPlJhgyOGoIJznRXeZJKxkVGJa2qKFpwrrw-UDnyrRfPZULKUJ-zmYanCWq-vHRwH0BS9tMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حماس: ادامه حملات به غزه نقض آشکار توافق آتش بس است
🔹
سخنگوی حماس تشدید حملات رژیم صهیونیستی به غزه را نقض آشکار توافق آتش بس خوانده و از حاضران در شورای صلح خواست تا برای توقف فوری این جنایت ها وارد عمل شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/akhbarefori/653609" target="_blank">📅 13:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653608">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db37a199e0.mp4?token=EOAd3sst-ANlzUXKoYC7VUnBQsybEup0RygKHr8Kn3PA3wQBkzpO2oMu2TeJF5qBzBBcWup9azj-zApYtJiOzBwUGSyE-VdGbDFn6UuwkdFv-LehNUdqz7cdVNj0CEtHV5gpEsfR7ZONbJuF354KSnmn-NMYu-Xj65PFogxoAz_1emEWs3mnK5xKU9eduT8RaEppI5Nfl0gm8_cM7lIn6rChK6WiAEA5DzC0fO3-OlJJJL56VBimr0-R29NH4R2Jvk2rBqLhCpsuGhKXUbbE0y6CD51vHrG601f2GoUFoR-naHHOY291QqkvENfQZo2wKirSDwscExsRoK6GnpAU0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db37a199e0.mp4?token=EOAd3sst-ANlzUXKoYC7VUnBQsybEup0RygKHr8Kn3PA3wQBkzpO2oMu2TeJF5qBzBBcWup9azj-zApYtJiOzBwUGSyE-VdGbDFn6UuwkdFv-LehNUdqz7cdVNj0CEtHV5gpEsfR7ZONbJuF354KSnmn-NMYu-Xj65PFogxoAz_1emEWs3mnK5xKU9eduT8RaEppI5Nfl0gm8_cM7lIn6rChK6WiAEA5DzC0fO3-OlJJJL56VBimr0-R29NH4R2Jvk2rBqLhCpsuGhKXUbbE0y6CD51vHrG601f2GoUFoR-naHHOY291QqkvENfQZo2wKirSDwscExsRoK6GnpAU0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا تقی‌پور، نماینده مجلس: دنیا باید به هوش باشد که گلوگاه اقتصاد دیجیتال جهان در اختیار ایران است و اگر جمهوری اسلامی ناامن باشد، اقتصاد دیجیتال آن‌ها آسیب می‌بیند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/akhbarefori/653608" target="_blank">📅 13:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653603">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpQavGD914Qlj45tXtJpg_v1Ki_ablXxrQRtVCDND7LANigmoWs6w4oJOGwuGtSxdAPOz3EbIZDMHYgmfG-4IyBitUMucKAIB_gHYYQYYGf82rjYdGeGbLpiz9dT-NdUuhJGRwZcaHJrFaxjCKBNI8ntAWl_HcxSfUrbpc-trAlxHGD8vsKfvNzVJFVUVSyJNKZNu605Lamxj_t-j3X-kMpwGHbfRXrFYCqDWxWpsyLHAtCgLqSTye77uzcl4c50X-U0GSsLsQk2A1u9-z9AchbczGx5Xve-aIJSSFuIr2griXTsSgb-3qTxaDFqx9hD0sF0SSGp5d1z7x50Ni29TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rm4-SS8uNTwErm7VVOgsw1IEWl8SchT2gvQV_SI8y5mTZoN1cQxDVXYyPNbVAJAdStl4gxe73Gpf-EywJmID46P9Lr7AGT0EoXr4lTuWc3Fn7BoOR1q-vda-YJ0fIhC-jiylU4ZkfOborzCLMpNXImqB4Ti5lLy-TX2MgX1HDu6OPYgf4hzgRS2OPMObs3Fq8LASlukLL5LjCohLCOxhJC2oxxXdycBdjkNbzntjKl-7aPGnEoSzrGcnDLmXw6WHwYO8YJGn90e3ctC0wutSihVkJlPgg5a-0-DEL-24CXrh7nEMmwKNhOWl7bK4Mk0IzZi0SeXEExs8kzbd46rBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_c4_j1TA1SYGSdkDyI3IJTttKzO7Vxm0eVnkNL7wRwjuR2Igd4-oeJ4EkGMHxykhW1mIda26mBQWhl-aSS6Ge0Er2PR-T5OwfEq08GumAyjZfu2JP196Fwo8FRQMZrRG0C6ERAAab7bSkVmO-MqpdrW8f76-lO2aMxfT9hxzvbM-5GrUAzOjeD7yGMxbS_kk6V1Fdsf9ijnsFk-P3zxTf4QxWb53wDbmHHD_BRiC4bSWrPeIXdBBU1Ep4ul5qra-_rArv_QXlaVceDvbToVa70Ru6E05Ur4OBUBd0zObxng5Fhx6YK_vtDaoE9oxs4-eDLSHIzudiHZltj-vsicag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzCXLyW6qZJ0YTvWgLLslGju8q2G8huyROteC281_IMR-rSovp7mAShfh15PiA4Cj4D-oBLaG_s0QhPwSrPzfBwdXvKIblRRhqduWeaBs3eb4zBlAqvx0Y0NqLP1nK6XLS1tpJJIonO23dpgBpTnn4MLhgRnnLSE8RSb4n7wnGjMwLzMnXaAX2Fi3opRjhZSB393Q-yIIji2Xy1U8AYEPczf7uNA-tJfusIz87UtKmTDEBHEgXWjEa9_LMwo84pvPdNatoHGjxsmPlvn9mjEqWekZrfxlCPru2WXeQGXxLDktRI0jEfaPrFr62dz_U2143xLuDuj9-ZwVD5aRsDncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLybAnprUaG1RLkjWQkAxdR785YnS2MZCjcMpRyBkYbxRFgDByVL-YxzqY6a2Q0Uada0sbHj6ELXeXmWBFemihlwGeSvJAII6wX5baLN2TdwKtLDn_3njQk1HYX6eAzpnvxl97iU81nRGwfwiM5AbuvOVgRPMf34iqeJoaQh2TA5flP20DMANSpEEhKoWz9J4UdanXvMK7GtU76XPAEfpHvBOSMH_k9pqao1hwvB54kGM_bWMnP3wGYKb-IV3buu0MRNEvigHuC84gSjpQYZ_M1Nzz4sHvf8_BDy56wuHCNQyGGHor-9MDyAlwrozvaww-NLZoEk7YTZH2vCSijTjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
‌‌
پویش مردمی نه به پلاستیک
🔹
مشارکت و همراهی شما در این حرکت اجتماعی، می‌تواند زمینه‌ساز کاهش مصرف پلاستیک و ایجاد آینده‌ای سالم‌تر برای نسل‌های آینده باشد.
شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک
@na_be_pelastic
@Alo_fori</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/akhbarefori/653603" target="_blank">📅 13:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653602">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwfbtdNCtIm_EXt3bDtDBMK0BIvw_Tg7P6RseTOCpbyx44jCj991yvlvOWvY5kJWrtaw3buV1W_b7oDc7XC0_X3TxCaGBb0TTCrthe2K7SGBwwMiCGsYLuwqXpFoTh_7wAZlHnrWxdaMdfN69_KAHtNTeHf5pv94eMqU8qj8IY1X6Ao9fVXItiPFtvqjieeaNy5jeR0rN-Wl68g6FGEoW3gj0SaZcg8fu1EJU70o0-5cpEAqkY5WvUbLP13xyTQgchhj9_WI2N9R0gC6cZQxIJUckckRv9TSMN6_gmlrhxXn8x4huK7t0aE5o3ICfTFuXu2fHCd13-SRL-pbr0m3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت طلا و سکه
🔹
سایت رسمی اتحادیه طلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/653602" target="_blank">📅 13:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653601">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df35f5dfa.mp4?token=N5GoB83MpXb7tAGWIKIVyG2pNvR6Hg7mwUASH3VKmFG-pazz8GSYxEUFWRZnzjbVyU7wTVZZdkvyo9MPRdy4_--yXXowPdXNJ81-al26PnPMJs6JZeBoAvvi4xqX5MzGgpHz4iHu2h2a9KTY-CrU13cwNa6GXJBKidUCjKSXuxptviuqB3cTfi-522vKv8G0Ukf-AZrXak7BxjBuZZdYIe9RCmV6rpQI3hQNylH4kkQevRoVNU9ZxCYJkk_iS3yFyQZaFmIYiQOZixWYpANtaiPoSC0PWg2OmaEOq0X69qn1Hk9vULaPB5mJw9Or9xXS7Ib9AbaQzfDDqvHzhqpqbJf1HpwHbKtVaau52cr0apz9OHd7Lr1bMIqZGYRaosGEm8zu8y3ArGvG_8cG_bajSDGxuhx6DrmVdo7MmBsJ5PzIKLTlUppfqVEhWNGK_BUKgnNlVsq76VkORRuVsBYM2qsR1K0mz6X3jocwh6_pK47uvb24kveOLSYjZVj_4VMjzMn8hm6pfnVdUqYPOCt0qez1gshHJgpoS1qL8wBtn1WIy1zdv7Ke674FwNOGiDZdOGwuGtISyR-mregChM0oOHZtee9vAKH_Dds6rdpWwIoiaXSVg2RGRAhMrMu-LUnF94NfZB71yUbhxYliK72_0ZkEzO1P6VEXtu_l-JmXgkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df35f5dfa.mp4?token=N5GoB83MpXb7tAGWIKIVyG2pNvR6Hg7mwUASH3VKmFG-pazz8GSYxEUFWRZnzjbVyU7wTVZZdkvyo9MPRdy4_--yXXowPdXNJ81-al26PnPMJs6JZeBoAvvi4xqX5MzGgpHz4iHu2h2a9KTY-CrU13cwNa6GXJBKidUCjKSXuxptviuqB3cTfi-522vKv8G0Ukf-AZrXak7BxjBuZZdYIe9RCmV6rpQI3hQNylH4kkQevRoVNU9ZxCYJkk_iS3yFyQZaFmIYiQOZixWYpANtaiPoSC0PWg2OmaEOq0X69qn1Hk9vULaPB5mJw9Or9xXS7Ib9AbaQzfDDqvHzhqpqbJf1HpwHbKtVaau52cr0apz9OHd7Lr1bMIqZGYRaosGEm8zu8y3ArGvG_8cG_bajSDGxuhx6DrmVdo7MmBsJ5PzIKLTlUppfqVEhWNGK_BUKgnNlVsq76VkORRuVsBYM2qsR1K0mz6X3jocwh6_pK47uvb24kveOLSYjZVj_4VMjzMn8hm6pfnVdUqYPOCt0qez1gshHJgpoS1qL8wBtn1WIy1zdv7Ke674FwNOGiDZdOGwuGtISyR-mregChM0oOHZtee9vAKH_Dds6rdpWwIoiaXSVg2RGRAhMrMu-LUnF94NfZB71yUbhxYliK72_0ZkEzO1P6VEXtu_l-JmXgkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا تقی‌پور، نماینده مجلس: شبکه حیاتی کابل‌های فیبر نوری جهان از تنگه هرمز و باب‌المندب عبور می‌کند و ایران می‌تواند این کابل‌ها را قطع کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/653601" target="_blank">📅 12:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653600">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaN2aZd8CVWdTherKMLlsp8GoQY_RMgt9wD00xwWXV1l_2ULrizRC6TmtEMqRc_u4wOavN7CyfbiJTDApIkFA_FbbeGfMwbbEX5pIHn4_QVz4pW7kRiVdQkTh8lbyOkM5Q3Ik8LnViBRgZo5szdAQJrr6mR2IHBd5OzAZRDpnpWyEIgevfim2beZPXqbZt3k_Sl99PHbJ-RKAsMBgV7JvnAQyIhykCVQldztaqYW0u9W06-f4PTsoI3BIlIcsKFwwz9es5Tegx_NDP5UjEZdQKQ5jO1r9ORJKSVgyebFKhtg7gdyMXdtwoT7W-XyJS54cTr4z3MDWDzs-ZV8m_79xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد افسران ارتش صهیونیست از نبود استراتژی در جنوب لبنان
🔹
در حالی که حملات پهپادی نیروهای مقاومت علیه نظامیان صهیونیست در لبنان به تهدیدی دردناک تبدیل شده است؛ روزنامه عبری «هاآرتص» از ناامیدی در صفوف ارتش اسرائیل در جنوب لبنان خبر داده و اعلام کرد نگرانی‌ها پیرامون فقدان اهداف استراتژیک در لبنان بالا گرفته است.
🔹
نظامیان در اظهارات خود اذعان کردند که از «استراتژی حقیقی جنگ» بی‌اطلاع هستند و نمی‌دانند که آیا رهبری سیاسی و نظامی واقعاً به دنبال پیروزی نظامی است یا دستیابی به آتش‌بس.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/akhbarefori/653600" target="_blank">📅 12:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653599">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO5nEF_k04I-_jVXPoLMswhSJE3UWeH0HvCuFDTyXDJ2t6t8G_4S3wWRkrm5rYFK29_3DRF-5FpU7f0ZN-ipbu00dKZcAxPY0o8DRNvVj2s3tZpkA0eiINjzSAcBVQ7f9kU9rOOrO1XLbIs8qx9fOGJIdLb6DgY4n5ThyM5Q1Pp8fLG466XI9IQOKysr_Jts6Na5Na--9_ODEfD3etoxB7dovSof2KsFn1rZwD2tITrkrW9auAHYIvy-ML48j7hW-E5lyuX4tYbYa9Yb6TESf7VnkiDGRnYss3fKvaZSXTYJMaVYI-X-yl_MsL0HnrYxG6-uhqDNtzQ8pYyw3V9JAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۶۹ هزار واحدیِ بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۶۹ هزار واحدی به ۳ میلیون و ۸۳۰ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/akhbarefori/653599" target="_blank">📅 12:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653598">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67eb0237ed.mp4?token=G4tokEEc3mN0ChOftx7N37zeidkPEqClOG8lmcb3_2JJM2F-bsPCWpxQckOpOfU4gtC25-_imUxazNGgj4PqA1vBUffKfeZU97zKuYqL1ic9b60peqCmXkUHhPVp8prk_GnFMhTvyCrHuJnDfMSpDtQ9wZ5z3Hvz0VjCyBaOSNyJ6W0AzxCZtvn_gfgxgHiOAEhMfjXdmMbUZW0ddWHYOV1neY9dIIid_v-uJ8QtEniCCD8POKpgjB_apEEw_xbIVHC9estWE6nvIAzscN2C5p5LYUiWtDZZUCjr8SLspeP6Fem3UF-4oPq2RNVLDnO7gHUrxtgQtb-JqhlJV1VdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67eb0237ed.mp4?token=G4tokEEc3mN0ChOftx7N37zeidkPEqClOG8lmcb3_2JJM2F-bsPCWpxQckOpOfU4gtC25-_imUxazNGgj4PqA1vBUffKfeZU97zKuYqL1ic9b60peqCmXkUHhPVp8prk_GnFMhTvyCrHuJnDfMSpDtQ9wZ5z3Hvz0VjCyBaOSNyJ6W0AzxCZtvn_gfgxgHiOAEhMfjXdmMbUZW0ddWHYOV1neY9dIIid_v-uJ8QtEniCCD8POKpgjB_apEEw_xbIVHC9estWE6nvIAzscN2C5p5LYUiWtDZZUCjr8SLspeP6Fem3UF-4oPq2RNVLDnO7gHUrxtgQtb-JqhlJV1VdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباسی، نماینده مجلس: عده‌ای دنبال این هستند که در مقابل رفع محاصره دریایی، تنگه هرمز باز شود/ تنگه هرمز اصلا قابل مقایسه با محاصره دریایی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/653598" target="_blank">📅 12:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653597">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
هزینه دریافت گواهینامه رانندگی با ۵۶ درصد افزایش به ۱۵ میلیون تومان رسید
🔹
رئیس اتحادیه صنف آموزشگاه‌های رانندگی تهران: در حال حاضر، هزینه آموزش رانندگی با افزایش ۵۶ درصدی به ساعتی ۶۰۰ هزار تومان رسیده است.
🔹
بر این اساس، مجموع هزینه دریافت گواهینامه رانندگی در شرایط فعلی حدود ۱۵ میلیون تومان تمام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/akhbarefori/653597" target="_blank">📅 12:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653595">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuqGwLxrevmp6YxBwtfS-JvfquIkG2Fp6JdcEC7JGGVRXm643g4jAFHS53IhOtMUT2r4J9ysTrNouNl6QxEZPnFupylsGIzq9hnYjnXp0cSB8H-fN06Vukv0X2DI4GZdVlKQDO2S_XVjkjsrcr9mSnDR1lcaVv_TOW8qK4LYOSK7GX7nFD-sfVbvC2Kaw86thtNT88Jr6sv9FYDG2N1_kgcMFuhLIGzK840QwnREZwad2kFNu8xyPqwPOJnz1uFc0MecvLlZthTv4ffErz8Vj_cirSm75ZkevaisanDhDqO4_G23TQDkBF0t-2oMAZYsW_vnMDn_y8r4_Qbm7y1tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار مسکن در تله رکود تورمی؛ زمین، سوداگری و جنگ علیه خانه‌دار شدن مردم
🔹
بهزاد عمران‌زاده، کارشناس سیاستگذاری شهری و مسکن در یادداشتی اختصاصی برای گروه مسکن و شهرسازی نوشت:
🔹
بازار مسکن ایران در شرایط جنگی با فشار مضاعف روبه‌رو شده و رکود تورمی عمیق‌تر از گذشته ادامه دارد.
🔹
سهم بالای زمین در قیمت مسکن، سوداگری، کاهش قدرت خرید مردم و کند شدن اجرای قوانین حوزه مسکن از مهم‌ترین دلایل بحران فعلی عنوان شده است.
🔹
این کارشناس تاکید دارد بدون اصلاح سیاست‌های زمین، مقابله با سوداگری و مردمی‌سازی تولید مسکن، هر شوک اقتصادی یا سیاسی می‌تواند دوباره بازار را وارد چرخه التهاب و افزایش قیمت کند.
🔹
عمران‌زاده همچنین بر استفاده هدفمند از زمین‌های دولتی، حمایت از متقاضیان واقعی و کاهش بروکراسی ساخت‌وساز برای بازگرداندن تعادل به بازار مسکن تاکید کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/akhbarefori/653595" target="_blank">📅 12:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653594">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrKzn02J9Df-XX-PBSNCLEYgrRUeWfUPVzcccPXC-rXAoET_FvifK5kVwK_a5C4LOaG-s8b1zFJ-nWiiJIM_HBHT415X3xXQdb2waiQrh2gT5ffaFtogTEtBDQutE5LYAaaXENJkECUpRTaZaTFWKfI3sijahsrD_ZjtpINJ1ySgOWsqEdqdkFq_qBezpCZUEYjppDVTLAclWCaiqEOwoQWKMUBSKmFJ0nbx2fm1SbHNaGeauaoWGPrmEFbEBzBLZKZ3ztXXm5O-2b6hsbSziep9jf_P4By3V3GdNwgvyvQiry7PeRbmpgn_0EXpp26N423LkZtJRxx3HnSDzXPVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: ترامپ در باتلاق ایران گیر کرده
🔹
سه ماه پس از جنگی که قرار بود در عرض شش هفته با یک پیروزی قاطع به پایان برسد، ترامپ در باتلاق ایران گیر افتاده و قادر به یافتن راه خروج آبرومندانه یا گسترش حملات نیست.
🔹
علیرغم حملات نظامی ایالات متحده، ایران سقوط نکرده است؛ کنترل مداوم آن بر تنگه هرمز - که یک پنجم نفت جهان از آن عبور می‌کند - همچنان اهرم اصلی آن است.
🔹
رئیس جمهوری که به پیروزی‌هایش می‌بالد، اکنون با چالشی روبرو است که می‌تواند جایگاه جهانی آمریکا را بیش از هر درگیری در دهه‌های اخیر تضعیف کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/653594" target="_blank">📅 12:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ابلاغ تسهیلات قرض‌الحسنه ودیعه، خرید یا ساخت مسکن
🔹
سهمیه تسهیلات قرض‌الحسنه ودیعه یا خرید یا ساخت مسکن در سال ۱۴۰۵ به مبلغ ۲ هزار و ۷۰۰ میلیارد تومان به بانک‌های عامل تجارت، ملت، صادرات و پست بانک ابلاغ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/akhbarefori/653592" target="_blank">📅 11:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
توقیف اموال ۹۶ مزدور دشمن در قزوین
🔹
دادستان عمومی قزوین: اموال ۹۶ نفر از مزدوران خارج‌نشین و داخل کشور توقیف شد؛ برای ۳ نفر به اتهام جاسوسی و برای ۶ نفر به اتهام انجام اقدام اطلاعاتی، کیفرخواست صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/653590" target="_blank">📅 11:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuMeZ_PNzaq2tj9TpGQY7NSagDXdSEfnBLgj6ycBwAIyrnOnSC-4i7pUEwwdVJs4WHZrivviLACyvmCu8YLgRuzpuS2abbFqB0rFFOHnKMB0tW1Z0I7NcNIdJweuf9hCWXiskbKXSaHq9dYtaRWV8Lzsey-JDu8AeqFW3QJpImHXq7DXj8ttCrcfWI2ROi54e8u1LZ6tEvCtsuEY_qNvS0qlVUJBURI2q_lvpJqUr8n1FKHkeJ0lb-g7gV_jIfGEAEdgEdEyrmLS5bp3ayTxDLwEVC2-bxZJ6PvjT8EF6iQZrNxCGbUGsUM7N1wT4qTNjx1GJk2lW2a8Wc3h_9YsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: هکرهای ایرانی به شرکت‌های هوانوردی آمریکا حمله کردند!
سی‌ان‌ان:
🔹
پژوهشگران شرکت امنیت سایبری پالو آلتو ادعا کردند که هکرهای منتسب به ایران در جریان جنگ اخیر با آمریکا و اسرائیل، با انتشار آگهی‌های جعلی استخدام و نرم‌افزارهای آلوده، شرکت‌های هوانوردی، نفت و گاز در آمریکا، اسرائیل و امارات را هدف قرار داده‌اند.
🔹
مهاجمان تلاش کردند با جعل هویت شرکت‌های هواپیمایی آمریکایی و انتشار آگهی جذب مهندس ارشد نرم‌افزار، به شبکه‌های داخلی سازمان‌ها نزدیک شوند و عمدتاً کارکنان فنی و مهندسان نرم‌افزار را هدف قرار دادند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/akhbarefori/653589" target="_blank">📅 11:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIigFHWfh6Tbj4nVYLNd2rW3W09JydvWn6D83D61Gstu2SH86rb80-iH7A6Ym4dxRXSZ2o53V_CySWHzlHbCCO1efhoeiGn23JZIN-rcEi_rqyp-7TaD6QbjCIKMgRq25TZRY2eIDEvWQWVnIjwre8ALQrYSOsVVLeEGNoboly3JsYg_b18ypoLcC61zoN47t5V9J6QzGn7VgqUF39Jo4Ig7VpvT7L7pzTwLQxiRbgjZKzt4rkOZoezLHGyYK_-UTEFnBph6EPGyPT0TXpboDT7KzTEBBTbKOQ2L19-uYLKhJ81EO-slqlXQtzPpd3nfUNhPgE4So406qcz17YTNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو سابق کنگره: ترامپ ممکن است جنگ ایران را بهانه لغو انتخابات ۲۰۲۸ کند
🔹
قانونگذار سابق آمریکایی هشدار داد که ترامپ ممکن است با الگوبرداری از اوکراین، از جنگ ایران برای لغو انتخابات ۲۰۲۸ ایالات متحده و تمدید حضورش در قدرت استفاده کند.
🔹
گرین در مصاحبه‌ با الکس جونز، یکی دیگر از حامیان سابق ماگا، به اظهارات ترامپ در دیدار ۲۰۲۵ با ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، اشاره کرد که از برگزاری انتخابات ریاست‌جمهوری به دلیل جنگ جاری با روسیه امتناع کرده است.
🔹
ترامپ در این جلسه به زلنسکی گفت «پس می‌گویید در طول جنگ نمی‌توانید انتخابات داشته باشید؟» «سه سال و نیم دیگر، منظورتان این است که اگر با کسی وارد جنگ شویم، دیگر انتخاباتی در کار نخواهد بود؟ چیز خوبی است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/653588" target="_blank">📅 11:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رکوردداران عبور از تنگه هرمز معرفی شدند؛ چین، هند و پاکستان
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
صحبت‌های وزیر خارجه‌ افراطیِ آمریکا (مبنی بر اینکه هیچ کشوری حاضر به پرداخت هزینه برای عبور از تنگه هرمز نیست) فرافکنی است.
🔹
کشورهای چین، هند، پاکستان و برخی از کشورهای حاشیه خلیج فارس که با ایران همکاری داشتند تا به حال بیشترین عبور را از تنگه هرمز انجام داده‌اند.
🔹
خرده فرمایشات آمریکا به گونه‌ای است که کار را سخت‌تر می‌کند و تمایل ایران به میز مذاکره را کم می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/akhbarefori/653587" target="_blank">📅 11:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653585">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc676252b1.mp4?token=V3cd-7FzEms9rIdWB5pYqE3naHL8L2_K1x_G4XsPCBe9RFTWQk8nO_F_wzYNXyJfvDphyvRoOHiSZaB5_B4h69IewKI6X_nBNpN-0xMeBgPF3JSUIxgFBLl_-S0IW-IacF5VxrANRV7YfDDsbElOI_9H9ziRllMWfUH5QOGuCOQH3bkt4ZYodomwer3K1Vb7y9pUIXMdZvZmsivYuR3RIualsfBAh43s8JxQ7hCRJsCPw2-xhocuQmVSLxJIRmZdP_5M387y8uD2SZIEeDZpRdVPRk6gkTuZsp0N43Y_7VQFb9IdU7Bz5FWLmfFSQMYDEKdRXoze6tY_BkGhL67pfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc676252b1.mp4?token=V3cd-7FzEms9rIdWB5pYqE3naHL8L2_K1x_G4XsPCBe9RFTWQk8nO_F_wzYNXyJfvDphyvRoOHiSZaB5_B4h69IewKI6X_nBNpN-0xMeBgPF3JSUIxgFBLl_-S0IW-IacF5VxrANRV7YfDDsbElOI_9H9ziRllMWfUH5QOGuCOQH3bkt4ZYodomwer3K1Vb7y9pUIXMdZvZmsivYuR3RIualsfBAh43s8JxQ7hCRJsCPw2-xhocuQmVSLxJIRmZdP_5M387y8uD2SZIEeDZpRdVPRk6gkTuZsp0N43Y_7VQFb9IdU7Bz5FWLmfFSQMYDEKdRXoze6tY_BkGhL67pfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو حاوی تصاویر دلخراش
🔹
کشتار کودکان توسط سگ هار آمریکا در فلسطین، همچنان ادامه دارد...
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/akhbarefori/653585" target="_blank">📅 11:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653584">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAX8vtEKtLznPc5H_WtyeaUToPKMVUOOj4t0IL9sGD2Zsnuk8XMNyOpR2wPmg1OXoeA18_D8cBZhZYlcFpwRX3GH6olrKXGqTqS47jM3tUhhWivpTnAhYBdWyscWxQQIcgaMlsf1AEGBxPp4aJgKWXGOalfpxfy9HF9CtJuixS5wiDYlWpfLgnuguc1Q-rLVwE6rl2Ogxh9MqI0hHq0muQ1ecvsV4ZLTdL_K9m2U2m7r_o1pNnBxL6OGaaPef_Coi5JaYy7AjFuWKTWxP-pLnmz0MXhDaEB4JEQNTnwbyOxvKk_wNEqEqXMpeN8SHUOGuemRA1ut4g2KYgf7tEaZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده خبر توافق قریب الوقوع چیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/akhbarefori/653584" target="_blank">📅 10:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653583">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
خبرهای داغ را به انتخاب مخاطبان وبسایت خبرفوری مرور کنید
♦️
🔹
لحظه به لحظه با احتمال امضای توافق ایران و آمریکا | دیدار مهمی که امروز برگزار می‌شود
👇
khabarfoori.com/fa/tiny/news-3216870
🔹
یک تحلیل عجیب؛ حمله به ایران در میانه جام جهانی؛ از حمله پهپادی به ورزشگاه ها تا گروگان گرفتن اعضای تیم ملی | جام جهانی «خونین» می شود؟
👇
khabarfoori.com/fa/tiny/news-3217004
🔹
روایتی تازه از متن توافقی که ممکن است ایران و آمریکا امضا کنند
👇
khabarfoori.com/fa/tiny/news-3216986
🔹
حکم بازداشت شاهزاده صادر شد!
👇
khabarfoori.com/fa/tiny/news-3217011
🔹
جنجال حضور سلنا گومز در فیلم ۱۸+ | هواداران با ستاره‌شان اتمام حجت کردند
👇
khabarfoori.com/fa/tiny/news-3216860
🔻
ویدئوهای منتخب را در آپارات خبرفوری ببینید
🔻
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653583" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653582">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
۱۰ انفجار در شمال فلسطین اشغالی در یک روز
🔹
رادیو ارتش رژیم صهیونیستی گزارش داد که در ۲۴ ساعت گذشته حدود ۱۰ انفجار مشابه حملات پهپادی در شمال فلسطین اشغالی ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/akhbarefori/653582" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653581">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
استاندار خوزستان: محدودیت‌های تردد کانتینرهای تجاری ایران به مقصد عراق، با دستور معاون اول رئیس‌جمهور لغو شد
🔹
موالی‌زاده: کامیون‌های کانتینریِ ایرانی می‌توانند بدون محدودیت در نوع کالا و بندر مبدأ، از تمامی مرزهای خوزستان، به‌ویژه پایانه بین‌المللی شلمچه، وارد خاک عراق شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/akhbarefori/653581" target="_blank">📅 10:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653580">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTRLgSDPww6FgnLjRdcnvloiJBLIiG5zBZxpDwBxqEmbmJw_mX-hVx4e1ojTyLrBvbczU8VakyTIoTq0xeUwwW50WGFRPaX95lNcWdN01SAECrlRgQ54KNVvWNtZkabL1JT8kQK4N3ZYCEqGM57gs8WSjm60wPvjavy3lWgBrxkIG8E8JGE8E14GFyrk1cDkBrtAqw2JLMv6f9UDFv1oW6-fy9M6tKaggO8NJl5-D5J4tsz9IIJSojXPGfD2ZZXckTPUOlTEMbZ0vhMu9yNYpYOABi3TwJCrSP9RmxPFoiBjKRltMugM4MBaUdkWuhdhIg-fXuICkbVosMjPaUkULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون رئیس جمهور: صرفه‌جویی صرفا یک انتخاب نیست، بلکه مسئولیت ملی ما در این «جنگ اقتصادی» است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/akhbarefori/653580" target="_blank">📅 09:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653579">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1hhvix8EBf2ti2NsCbpblTyQ5Wejv47uS7UYLW6F302eKsaUqBW-dWhZjFo-g_R94JOrS9t9eepCD5kc7LVI_jh8qN7Qd926Y-OnAL8HeRGXL5W-xmtx5ovxEzy9Akzd-In05WwMbt2kTNGynigixBUhnR9934dAQK6DVPGEzgbgaytJny3XjKxjzONEssa52nrxfkaXXevr0-hjnVSNpTpIEl1nWoN_v0V5K9ZHAzl63uWgdPs295eNWCeRZDoHm_dBez_BF4FrEMmXdRNGM_FAjLEuQDZ5Hv48Dik74k1uKY5LxsDZX54YqVYPz6WkRGxaQrD1e72MC3ftDpZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالمعل فوری مدیریت بحران دارویی ابلاغ شد
🔹
دستورالعمل ۶ گانه مدیریت بحران دارویی، از سوی مدیرکل دارو و مواد تحت کنترل سازمان غذا و دارو ابلاغ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653579" target="_blank">📅 09:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653578">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4bd9f809.mp4?token=P1pW-neFMcBUzaMGDcF09TwxlCCE21buG2zHusL1dn89EUR9Aufsa9WhE0Dq1rHz8nXkoI-HwvD-TyFGH9qCXQBXZ9cD3M1Lpc0mB7oRDA9MvALkc_Jh0vFuyXyRb0Mxh-JUC5tHz9JoBe6OM12dwc-76VPFqu-cgaUn0eQRzqVgeqPeQKvPx5u0cHun5pAv4Nj-DQ2DhK03fUuZQR2g57obEprGmqSMIN9BFZySykNJJk1j5P_cQKj_aw7cpRHzC71C7RE0lQ9CuSVTASqpPQRsBIBhvreInDDTseP6255o-meM8Go8T1_6KzCc_ZtwP3VAxfAOAM7lR-PM2Kl44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4bd9f809.mp4?token=P1pW-neFMcBUzaMGDcF09TwxlCCE21buG2zHusL1dn89EUR9Aufsa9WhE0Dq1rHz8nXkoI-HwvD-TyFGH9qCXQBXZ9cD3M1Lpc0mB7oRDA9MvALkc_Jh0vFuyXyRb0Mxh-JUC5tHz9JoBe6OM12dwc-76VPFqu-cgaUn0eQRzqVgeqPeQKvPx5u0cHun5pAv4Nj-DQ2DhK03fUuZQR2g57obEprGmqSMIN9BFZySykNJJk1j5P_cQKj_aw7cpRHzC71C7RE0lQ9CuSVTASqpPQRsBIBhvreInDDTseP6255o-meM8Go8T1_6KzCc_ZtwP3VAxfAOAM7lR-PM2Kl44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف‌های شبانه برای یک قرص نان در سوریه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653578" target="_blank">📅 09:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653577">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
فعال شدن آژیرها در کریات شمونا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/653577" target="_blank">📅 09:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653576">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ایروانی: دولت‌های خلیج فارس موظف به جبران کامل خسارات علیه ایران هستند
🔹
سفیر و نماینده دائم ایران نزد سازمان ملل روز جمعه در نامه‌ای به دبیرکل سازمان ملل و رئیس شورای امنیت به برخی مکاتبات اخیر کشورهای حاشیه جنوبی خلیج فارس و ادعاهای بی‌اساس آن‌ها، به اظهارات علنی اخیر مقامات آمریکا، از جمله رئیس جمهور آمریکا و فرماندهی سنتکام پاسخ داد.
🔹
نماینده دائم ایران در این نامه، مسئولیت بین المللی دولت‌های حاشیه جنوبی خلیج فارس شامل قطر، بحرین، کویت، عربستان سعودی، امارات متحده عربی و به همراه اردن، به خاطر مشارکت و تسهیل تجاوز علیه ایران مطرح و تأکید کرده است که این دولت‌ها، به‌عنوان دولت‌های مسئول، موظف‌ هستند جبران کامل خسارات وارده به ایران را به‌عمل آورند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653576" target="_blank">📅 09:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653575">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سازمان ملل خواستار پاسخگویی درباره رفتار تحقیرآمیز با فعالان کاروان غزه شد
🔹
سخنگوی سازمان ملل متحد: کافی است ویدیویی را ببینیم که توسط یک وزیر اسرائیلی منتشر شده و رفتار تحقیرآمیز با افرادی را که در کاروان بازداشت شده‌اند نشان می‌دهد.
🔹
افرادی که همچنان در بازداشت هستند باید آزاد و به خانه‌هایشان بازگردانده شوند و همچنین افرادی که مسئول این رفتار بوده‌اند باید پاسخگو شوند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653575" target="_blank">📅 08:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653574">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
حملات گسترده رژیم صهیونیستی به نوار غزه و کرانه باختری
🔹
ارتش رژیم صهیونیستی در ساعت گذشته حملات گسترده‌ای را علیه مکان‌های مختلف غزه انجام داد و به مناطق وسیعی از کرانه باختری یورش بُرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653574" target="_blank">📅 08:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653573">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdSMMBG00QWQ9us89ALOrNzYOTDZPFUlvBN-1iRz599RHS6jRgrg4SumhrW-anuG7LOjkssvCO0JiBTK5e-xONLrW0DJ5giiJLyB75_d4LMUF3oavGB8Mjn85wQRjnZ3lenChvDmsYtWcyjohrDDUx37W4uymNgn5q6O2UVihqlKoQH6KRmjFMALOhybC6d1HTZdXoj2QaXYibz0yYp_BAKcpcEfVAaB-m2Kx069AJ4cl-B29l2VQZ4u7IzQOC__r5XjwF3grcQZFtLUA1sMfDUQT5a6WlgBh4TqdY24tDU3ydnsmA11xTUXbN53LEpvJe8Tg-pTHAIx-_NzA_tVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک یمن
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک فروند نفتکش در آب‌های نزدیک جزیره «سقطری» خبر داد.
🔹
طبق اعلام سازمان عملیات دریایی انگلیس این حادثه در فاصله ۲۰۰ مایل دریایی غرب سقطری در یمن رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653573" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653572">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKBTeLuYcmlFstYJY9Zwp4uXFR8TDgWUJEVB2YlyyyMRVwaQI8ygc9TbCdCWGNlym_9AwiZQiUmjTWB9YR71MNDDBJybXNA4aGsj9RWb1JPUlMmL6wgONqv4UBK5thbYYo7IvSS3H3ZbbCdcn6LYOkVy3Jp-jNXlKacE7kHNG47SX3G0lW7q9XlnlaL5zyB9LfaZUep84C2LSKlrvr7SoPR8mpfXn6F5PJ18s7NuijlrBdkzoJ5WBk2kpGlGg_jGkOI1Sj950MDhe9HBGw_HyIyQoDrn-xZIuIMKYJGApZoc3RtCAsDwanp4ULXuR_HyJg94Z8V8AdblogSLYGFc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌خواهی آمریکا عامل سومین شکست متوالی کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای
🔹
کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای برای سومین بار پیاپی به دلیل کارشکنی‌های آمریکا و متحدانش نتوانست به سند نهایی دست یابد و در نتیجه، رئیس کنفرانس با اعلام عدم حصول اجماع، متنی را برای تصمیم‌گیری ارائه نکرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653572" target="_blank">📅 07:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653571">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای اکسیوس: برخی منابع نزدیک به مذاکرات همچنان بر این باورند که طی ۲۴ ساعت آینده فرصتی برای نوعی پیشرفت وجود دارد
🔹
دو مقام آمریکایی به اکسیوس گفتند که ترامپ روز جمعه صبح جلسه‌ای با تیم ارشد امنیت ملی خود درباره‌ی جنگ با ایران تشکیل داد./انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653571" target="_blank">📅 07:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653570">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
یک منبع ایرانی به الحدث: طرف ایرانی خواستار تضمین‌های روشن در مورد دارایی‌های مسدودشده و تحریم‌های نفتی است و این‌ها مسائل اساسی هستند
🔹
ما از تلاش دیپلماتیک کشورهای منطقه قدردانی می‌کنیم، اما توافق به ارادهٔ صادقانهٔ آمریکا نیاز دارد./انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653570" target="_blank">📅 07:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653569">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gayTU-rAp4doRNqdyl67cLk6yaQz6RPF4YnNiLPo_VWbA0FexrniQ7X0GOsHtGs9l9kmRVJP2l1GRtgTOyTPB0Qg_z3GZ9ZC4daYTRWo_Pp4ZH3XtQkHsUIosmLiQTGEoX_mlvz5frJnRrsA6pxKNscGS7vl9v6xrheYJX90yzE2HGLVYd92rN9b091JfKerqKlfT0p8RBRTKCGrBu4JYnNEVtK9EH26gD8eS3AvUgfyUI0f6AZkX_LmkgLWwvn42xCwEtrsWhmbPsIQsQFyXihXEomM3HqLln924u78pTHD6le08R6yimZt5hf4LbWQdJceVzd-hvqfdjNyqf9nCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲ خرداد ماه
۶ ذی‌الحجه ‌۱۴۴۷
۲۳ می ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/653569" target="_blank">📅 07:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653568">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8NexX61G3-M9e3Sd2OVdFQ6z7nDIX3Nz4LuyuwMg520CXyr0klviEYjXCFZ8sSU2YZ-24sgNX0Fmn29AvJyz_QWDfuvAZ_TDfl79ykhgC87BT9K7PWu1WbpKsc_G15t0aJ1XYE6EDAxCknMMGFUl_8qtSQnMkw74yEN8hqDe8D-3YgmnmOqHd2izylcn57CHIHuKRJQhi7aAvVK3oRWvx-DRyj6OMHMnBQeAQc3AEqps-ndL6c6yql2KRx5Ru-h00UTj5TfLIoOmPntvrgCSgyxIBY-9fuR4buirPvmie1rViDieArkcW64XYcsWcLQckAY2TdvhuFybbKF17_jUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف صادرات خودروی ژاپن به خاورمیانه در سایۀ بسته شدن تنگۀهرمز
🔹
طبق داده‌های دولتی ژاپن، صادرات خودروهای ژاپنی به خاورمیانه در ماه آوریل، به دلیل اختلال در مسیرهای کشتیرانی ناشی از جنگ علیه ایران تقریباً به صفر رسیده است.
🔹
براساس گزارش رویترز، این فروپاشی در تجارت، پیامد مستقیم جنگ آمریکا و رژیم‌صهیونیستی علیه ایران و متعاقب آن، مختل شدن کامل مسیرهای دریایی در تنگۀ حساس هرمز است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/653568" target="_blank">📅 05:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653567">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXRt1Bc5l-T6iiSWjNos1ckQhUbllp8rzr8hRk0UxsfeE53LdsNE5AOEn_-9ofAqUHtvC6DVc9fDNtnoDzbXUdUZ7HKXL_voiJZhnlhDiQ12-_5gYxop_jTIkXIl41jcv1UhcW-_ueUCBqJtdqHZ8JB9FCrU6WonHxFmzu76k0B3i8TLdKt76jDEStQd2BXmo4dOhrkGQKXBBl2zNPbowceXaIYmKKPM9WM6bYgbJ8OXUTMYF7KheRJJdAYhbdWhDjTM5OponWRPP_qm_Kgwash138B18qa5-QL1TBeJwxiBa-A62XHU4ZQK_f62J1VvgQDEbEvGWGjB2YiLkDx1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنفرانس بازنگری ان.پی.تی بدون نتیجه به کار خود پایان داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653567" target="_blank">📅 04:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
گفت‌وگوی وزرای خارجه ایران و عراق درمورد مذاکرات تهران - واشنگتن و ثبات منطقه
🔹
وزیر امور خارجه عراق خطاب به همتای ایرانی خود تاکید کرد: عراق چشم‌انتظار شنیدن خبر پایان جنگ و بازگشت ثبات به منطقه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653566" target="_blank">📅 03:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
نماینده ایران در سازمان ملل در نامه‌ای به دبیر کل و رئیس شورای امنیت، اتهامات آمریکا درباره حمله پهپادی به نیروگاه باراکه امارات را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653565" target="_blank">📅 03:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653564">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
محکومیت حمله اوکراین به خوابگاه دانشجویی در روسیه
🔹
پوتین، رئیس جمهور روسیه، حمله کی‌یف به خوابگاه دانشجویی در منطقه لوهانسک را محکوم کرد و به ارتش خود دستور داد تا گزینه‌هایی را برای تلافی علیه اوکراین آماده کنند.
🔹
به گفته او، در این حمله شش نفر کشته و ده‌ها جوان زخمی شدند و ۱۵ نفر دیگر نیز هنوز مفقود هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/653564" target="_blank">📅 01:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653563">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b200640b.mov?token=JjQdbxoIgSIeua8BYLgVDMR3CnachoUzct5tVJD0Gt-0BaW8GHN9RSgQlUyjHLsksA25rIf_tcD3oaNzVXoX49FGYpi44GlK4SkGTbWjSKvMXJ3f0cCSwZeDy9jwCAlpblHSwtip9iVjPcDi2JnCIbP3IZhcd4cvvZbPYbtQ1foF9H-ApxMvOhQV1hl4WRO-5rM2lFop04i_F_U6XRKUAcO5aTLa1h131EPuzo1w1zhlZBdKwLMjX829wJSWKyjw2RGdwYSCMEaFp734BRe95awK1bf3d_25hicTSeqllVM_mYvZduAqmSkVRcbSpurmT8UFL1Fdj4QrgWWZbvKA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b200640b.mov?token=JjQdbxoIgSIeua8BYLgVDMR3CnachoUzct5tVJD0Gt-0BaW8GHN9RSgQlUyjHLsksA25rIf_tcD3oaNzVXoX49FGYpi44GlK4SkGTbWjSKvMXJ3f0cCSwZeDy9jwCAlpblHSwtip9iVjPcDi2JnCIbP3IZhcd4cvvZbPYbtQ1foF9H-ApxMvOhQV1hl4WRO-5rM2lFop04i_F_U6XRKUAcO5aTLa1h131EPuzo1w1zhlZBdKwLMjX829wJSWKyjw2RGdwYSCMEaFp734BRe95awK1bf3d_25hicTSeqllVM_mYvZduAqmSkVRcbSpurmT8UFL1Fdj4QrgWWZbvKA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار جالب امشب مردم در میدان تجریش خطاب به دشمن
🔹
رسیدی به هرمز، بزن رو ترمز
🔹
ما عاشق نبرد با یزیدیم اورانیوم به هیچکس نمیدیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/653563" target="_blank">📅 01:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653562">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgdZqEf1dYfCMkAEpDZO3yyQtnBUbwgQIDQ2kAJbtK7SlYSOVurkULTiemkaplKkvR4X_EbTxjVcb0Qpsq3ImpBxSGADz0-TZ3D3ap_Ai3tJ5o4yPM4a2Z08gXCnkkxIYlZWuqeQf41PCYEuE5ZtwfBD4weLdNmjg4QJ3lBDeGOCxYicPCUVM7qyoz4uWa8D6u2YAiZm2tnm20VGNAc-Uww_OcZk4-O7dQgJ_XVAn5sxAjrVokyKAhHL0-Qv4q5gisTJ7-s7uciUwqBvx1X5iyUCKOfWWP--xp5xqiYfnvl9NN0345PlCGrsr8jApHi0FiZjsH3GXLKHsdMCwP4Fiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آملی‌لاریجانی: دشمن در صف‌آرایی مستقیم به زانو درآمده است
🔹
رئیس مجمع تشخیص مصلحت نظام: ایستادگی ملت شریف و نستوه ایران، دشمن را در صف‌آرایی مستقیم به زانو درآورده و او را به سنگر تحریم و محاصره کشانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/653562" target="_blank">📅 01:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cec408dd.mp4?token=Q9LlAGbJPIx5GIMF0QYwm0QfSPWmlsp3onCcM7kEvmO3UcgRvyBk4Ur_EnW_0HBlXGaWPcPLuoOSyuZslakSHZAbWLDOD14-L6VPIIgco35r0rE0ndaQ802sZso7dmK7KIJ6SjArz7kf5ETRA6yMSzk7u7SKTxWHAnMQVAjmPlNv_72buqKSZe9IOKn33JVYB8jMdqmzH7yQh5-R6j40HYHdByCWrxziKoP7CtIHtH_AOolqBI880-4teN4sb8keS1WBOhIDcHy-ERAC3AahljlLOdXRRNuPeXVLxLwbuWr8KUTDY4P5F08PGbpHyGb4PY8v_zfIR2mMGXTTLKN0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cec408dd.mp4?token=Q9LlAGbJPIx5GIMF0QYwm0QfSPWmlsp3onCcM7kEvmO3UcgRvyBk4Ur_EnW_0HBlXGaWPcPLuoOSyuZslakSHZAbWLDOD14-L6VPIIgco35r0rE0ndaQ802sZso7dmK7KIJ6SjArz7kf5ETRA6yMSzk7u7SKTxWHAnMQVAjmPlNv_72buqKSZe9IOKn33JVYB8jMdqmzH7yQh5-R6j40HYHdByCWrxziKoP7CtIHtH_AOolqBI880-4teN4sb8keS1WBOhIDcHy-ERAC3AahljlLOdXRRNuPeXVLxLwbuWr8KUTDY4P5F08PGbpHyGb4PY8v_zfIR2mMGXTTLKN0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همکاری اعضای ناتو برای بازگشایی تنگه هرمز بلندپروازانه است
🔹
روبیو، وزیر خارجه آمریکا: «نه، این خیلی بلندپروازانه خواهد بود.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/653560" target="_blank">📅 00:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af58dce728.mp4?token=pnA-n6gj7LkwpV__bH85JoWKVbdfbI0yKbxHz6nFyLvwl9-AEjDSfPR1HYH3OiR-DwuvAx2bE6mXHMRxruDdIUt6AgElRz_SPcgy-M5Scx8qQiCB3Z3aRYC8TQvg5xscXZigmZG_Jn1WO4E3E-9khnvgSqtADdkFhzSUNNj6rOGnof-HaYIzOTZHtoA7BeUu9tQFyaXDS1ERhyauYMKRu0qgcgaZsBheg_QSg7SrS_hPPMtgc16OOfkiHJpbbe8BvQ63RQesPufcf_vAW3w02gJC8tsopjvvIKtI1WXkJxaTMLxfApqmPa95XowWg6aQ44mhrwEh19Lx39SH5ees7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af58dce728.mp4?token=pnA-n6gj7LkwpV__bH85JoWKVbdfbI0yKbxHz6nFyLvwl9-AEjDSfPR1HYH3OiR-DwuvAx2bE6mXHMRxruDdIUt6AgElRz_SPcgy-M5Scx8qQiCB3Z3aRYC8TQvg5xscXZigmZG_Jn1WO4E3E-9khnvgSqtADdkFhzSUNNj6rOGnof-HaYIzOTZHtoA7BeUu9tQFyaXDS1ERhyauYMKRu0qgcgaZsBheg_QSg7SrS_hPPMtgc16OOfkiHJpbbe8BvQ63RQesPufcf_vAW3w02gJC8tsopjvvIKtI1WXkJxaTMLxfApqmPa95XowWg6aQ44mhrwEh19Lx39SH5ees7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ما ایران را متوقف کرده‌ایم. آنها هرگز به سلاح هسته‌ای دست نخواهند یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/653559" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653558">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4dbfae92.mp4?token=QyFFVQtGNrYKepWRHqMLtsv6ShAJ-Kr-oZrPHTWku6PLpbDO8cKPJDsyNlYbsfZBuil7WZOEK8axQjyGmATWd6lJNx8kC0ihffZhaPPw-WxotOA4rshVsBGP7l3sLaQNqffuF9wN7QPiSvW6BS2MfTp-hJmISOSGS0hR5cxUG9j0lQ6j3ImNPf5ty2jwV90LJD0ZwbLWOwYzdOu1AMXsOLPLJ4OyWRtQ9PdCbJm6VrzjVaByTVfPm5H0dad55FUZaTngnj2kH7D36oWtgejs36Eztp-VhenkbcsvtJxiTdBZw2IoI0KGgy_CNi5jv7fNSYng33TQFJDut_MpAcICGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4dbfae92.mp4?token=QyFFVQtGNrYKepWRHqMLtsv6ShAJ-Kr-oZrPHTWku6PLpbDO8cKPJDsyNlYbsfZBuil7WZOEK8axQjyGmATWd6lJNx8kC0ihffZhaPPw-WxotOA4rshVsBGP7l3sLaQNqffuF9wN7QPiSvW6BS2MfTp-hJmISOSGS0hR5cxUG9j0lQ6j3ImNPf5ty2jwV90LJD0ZwbLWOwYzdOu1AMXsOLPLJ4OyWRtQ9PdCbJm6VrzjVaByTVfPm5H0dad55FUZaTngnj2kH7D36oWtgejs36Eztp-VhenkbcsvtJxiTdBZw2IoI0KGgy_CNi5jv7fNSYng33TQFJDut_MpAcICGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با وجود تهدید ایران به حمله اتمی توسط آمریکا، آیا چین و روسیه از تغییر دکترین هسته‌ای ایران حمایت خواهند کرد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/653558" target="_blank">📅 00:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653557">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3956427383.mp4?token=soiqMQ_Gctz1R5OJkQx9TFdUqZbsm03ZMK3nH45A72G0ZSMCexux_bHvJfaQIN8eKp19dUeuywc2vJxKQAyKvTQfG7kAj5CRfbCtEyVDFZUFQaGCve9MQiX5JtPGNkKgJqX7edplaXQo0HsrkbaARxJVx5nneS9TfKrOMJs9AN9eObf_5Zl3goWq0zxwnyDdMpRBD_ylaoURLfXGgONRAeywbz-Ll0DXZ8h8EO3ff_sfTalmZhCRPFW9OeUT5V_sOwBuMNlV70DGkov7PymUBJI7Adato-H9wUARAPK_V28mNXXfRtyfeuDTGi1roAwJg607B09QwnpUDfz5GsHAew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3956427383.mp4?token=soiqMQ_Gctz1R5OJkQx9TFdUqZbsm03ZMK3nH45A72G0ZSMCexux_bHvJfaQIN8eKp19dUeuywc2vJxKQAyKvTQfG7kAj5CRfbCtEyVDFZUFQaGCve9MQiX5JtPGNkKgJqX7edplaXQo0HsrkbaARxJVx5nneS9TfKrOMJs9AN9eObf_5Zl3goWq0zxwnyDdMpRBD_ylaoURLfXGgONRAeywbz-Ll0DXZ8h8EO3ff_sfTalmZhCRPFW9OeUT5V_sOwBuMNlV70DGkov7PymUBJI7Adato-H9wUARAPK_V28mNXXfRtyfeuDTGi1roAwJg607B09QwnpUDfz5GsHAew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بحبوحه «جنگ روایت‌ها» جواد آذری جهرمی خاطره شهید لاریجانی را دوباره زنده کرد؛ شهید تنها وزیر زن دولت را «جگردارترین عضو کابینه» می‌دانست. تأکیدی بر نقشی که زنان و خانواده‌ها در ایستادگی اجتماعی و به میدان آوردن مردان برای دفاع از کشور ایفا می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/653557" target="_blank">📅 23:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653556">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1Idi9sTWsf0yv8atgCUTQwMW6vBOYiNUACu5oQAgEqWMFq_clsrDrQ1m84am3mJWIKOc0B8OnWctXGVKwsay6rzTrHcqqfeW-d960qCoyBr7mtg3_SNux7jHrs48dJx23lAgsRVVZ3Cng1eNs8aoiJadwflkK9sVrDTx6k7QRFPFYpaHgKER15xoMEI58ZQYboz0h4Vy3jcWRIaXIfO0kY7P7GC9JTBSHrHlVOSuoJjsmyElxDkY5ep_mvjvEgMXPst3bpxAL1TW1-_TPHrEgHrJyN8Mia8uQTPGar5JBFSKcadZ0pGUbw6yHAft8ibAee2xAWZcZeY6U2IQ3_7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوی تلفنی وزیر امور خارجه با دبیر کل سازمان ملل متحد
🔹
در این گفتگوی تلفنی آخرین وضعیت منطقه‌ و روند تحولات مرتبط با دیپلماسی میان ایران و امریکا با میانجی گری پاکستان مورد گفتگو و تبادل نظر قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/653556" target="_blank">📅 23:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
یک‌ منبع مطلع: گفتگوها بر سر موارد اختلافی همچنان ادامه دارد
🔹
یک منبع نزدیک به تیم مذاکره کننده
🔹
وی خاطرنشان کرد: میانجی پاکستانی همچنان در حال رد و بدل موضوعات است.
🔹
این منبع مطلع تاکید کرد: تمرکز در حال حاضر بر سر مساله «پایان جنگ» است و تا وقتی این موضوع نهایی نشود، هیچ مساله دیگری مذاکره نخواهد شد.
🔹
وی تاکید کرد: پیشرفتهایی نسبت به قبل در برخی موضوعات حاصل شده اما تا وقتی که درباره همه موضوعات مورد اختلاف جمع‌بندی نشود، توافقی رخ نخواهد داد.
🔹
این منبع مطلع تاکید کرد: متونی که برخی منابع غربی درباره جزییات تفاهم منتشر کرده‌اند دقیق نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/653555" target="_blank">📅 23:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653552">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLx3vt5ODfRRaH7XJ23l1YY5Arw7_1ZC4pl3pmDl0I7_xh0Kj30m428D9E0MdM6R64CLLTLpnNwVlhsPK3qMNCqityiaaRJGK6Kb7nnRaSb8eddkkHxNEKMmhIZ2icY-512FPn8wKi5IQRTsJmwnYNquMpF6xqy8ceU1Ad_qLQsx2EU8emB8wFy1edESMIhY9TqGEY37W9pFdOHrQHK6AEXkG75Nk_5v4AFCqw2_crDaW4NttrvN6OZLzLEXHVwdz3rvS6jmVfgzUTNYS8lXwXR4Mn3eSUhGI-oqwf8EXqesDZdwXJNU3J9q9mwr4Pp1kBJiAtXom7u-QMS8EoSUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtzPkpI1etEhOjhYOA-MdYxnIOIwoFBKcoJ1AuL5t-By_KcxFLVd0HLet5YDyK1OmG42tAFY52kXRh6hbcGKvSepPVJA1YuKlBwrZXDAiIYlOEvyOTC_TRqRsCoz0bW2ZvXUTPUdVHp1UZ2sLCeDCxqi13CEN0GbgbjfmYxjjamiC-n77UMGS_7HTTENnBO4b59kH8ugQL1VvKWezfGYBimhq2XSvAV3gLHgoFRlMntDSaIIcHQ2zMYJ-YuwEZTcfCHqkbw8Aul-KeCK0nuQcEYvkIZCiF4Z_2MZss1DF9L7s85ASbhuAOE7qAthZdgaepugd4G4feq1TDLLMtGfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsYBY74MZnYJMxeT8KKTn5-7pCtziILEnesJn1U7DMRJIH41HSiQtxSyyEyxuvqDEfbqGGnfgAnR1RJKMtReBTK0s-b73_0PxPpvi1XVqhguOBiq8xuoz11_0Td11k-hqG9bltgz5cHNtnoX-YGgxUgaJxngwQ71BCBrpsWK442xo71jV7COdTATxKlD7tS5MTSDHNb_yPBNx67VdfEzNELu8NEp4AgcFr_dNxqH5oI-zVmT6MTirxdAQm9XwhtzA-zveqNfxNFG4felTLeVQ61ooGPLg0M1-3Yo9J0X50sQmwNLXXNGHU3kZ4o1VZTtPcJWhnFT6i3Wox0O9RG4XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کشف لاشه پهپاد متجاوز به حریم کشور در هرمزگان
🔹
لاشه پهپاد اوربیتر دشمن که توسط رزمندگان پدافند هوایی جنوب شرق کشور در شب‌های گذشته مورد اصابت قرار داده بودند، کشف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/653552" target="_blank">📅 23:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653551">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5280039e23.mp4?token=GOnEZ4BJ8YZpiAORAmgBGgnCHn9wop6vAYD55t8x0Y6XqIAY9AirSqe2cJFbPTC4S6YIh5IMeIBV4EaeM6y--AgycA4H0T4APaOut4ZlWIEcDzbz2Qm-_GHvFpmqEdedK3HbU7cwuJpQ6O8Egl9hYt9n0-IkoJ3x88JZQNXosx0QGN6ap7SHcKNEs1OFEL8i44Kx0MfA24webYCMwId308MvNCK2bZi5bjjs9MIu7xv_qNJo4odKFqoCGCKSDlvLUXsjZosGlfVnPcxSZVlPqCd9oLSF85ASoVPsOwalU9vtM1H4aVUHtqm8A8fXxDFo7IERysmI5KfWDB6P4rcQtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5280039e23.mp4?token=GOnEZ4BJ8YZpiAORAmgBGgnCHn9wop6vAYD55t8x0Y6XqIAY9AirSqe2cJFbPTC4S6YIh5IMeIBV4EaeM6y--AgycA4H0T4APaOut4ZlWIEcDzbz2Qm-_GHvFpmqEdedK3HbU7cwuJpQ6O8Egl9hYt9n0-IkoJ3x88JZQNXosx0QGN6ap7SHcKNEs1OFEL8i44Kx0MfA24webYCMwId308MvNCK2bZi5bjjs9MIu7xv_qNJo4odKFqoCGCKSDlvLUXsjZosGlfVnPcxSZVlPqCd9oLSF85ASoVPsOwalU9vtM1H4aVUHtqm8A8fXxDFo7IERysmI5KfWDB6P4rcQtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت صمت: بسته‌ی حمایتی ۷۰۰ هزار میلیارد تومانی برای ۱۲ هزار واحد تولیدی تصویب شده که پیگیر ارائه کامل آن هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/653551" target="_blank">📅 22:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653550">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1fkNilgiJjuZKaw2Hk7nMc6dyYiq8dSOJqHhzAuICBGr_b-KeS7UJh-MuketUYPkXtftIHv6XKz812ck0avQ_E7i8hYTL8dPi4xG45RBAsAf57qEjombg-HwUKdtY4f39tPK-6EP9MxGmfIOUQsls1G6UwSeqCtS5T1yafUUHlYCuT0B90NpEUEojTcb3TvNe9f_yWwh6cjVF8MZHU1urNC_h9H7Vn71F6Jt5PbMjIVwOLmuvKzUIjrRzHxa_kRCGNQg-u73fJ7L9nxDQuEM6uYKAHvZe7fAw2uN8i2QF0hZFg_xndqFpX2lgQV3rPc2R46yGCaj1MpoYCPv-NMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک تحلیل عجیب؛ حمله به ایران در میانه جام جهانی؟/ گمانه‌زنی‌های هالیوودی، از حمله پهپادی به ورزشگاه ها تا گروگان گرفتن اعضای تیم ملی/ جام جهانی «خونین» می شود؟
🔹
گروهی معتقدند مساله جام جهانی آنقدر مهم است که بعید است ترامپ بخواهد آن را فدای جنگ با ایران کند و ترجیح می دهد، بدون مشکل آن را برگزار کند تا اینکه در میانه آن، حمله ای جدید را آغاز کند چرا که برگزاری بد جام جهانی هم اعتبار جهانی آمریکا را از بین خواهد برد و هم تصویری از عدم اقتدار و ضعف واشنگتن به دنیا ارسال خواهد کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217004</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/653550" target="_blank">📅 22:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653549">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8ac81235.mp4?token=owTNkLiZ_PqTFKxhCYy6HYq-DHIUnUSNhj-sDTluLdMHn_20sZVgOkbq2XBpjzceynL_Cf4qkO4_DuK-qXZml1Q-ANZbn3d-Xft61oqcDU8vej96YBSLmKHGEUa7yKD8HvLIpLmCe5eRBglew5rkgoD_sG5p8Le9D5SC7rXU5WOX6kXDG58StEiZVdYTSUCYG79mRcVf48VWhlPqeg5s9jRr8XO2rHwzsjCbBhktf_hEbwnENRtQZ8QqxmFDVlvxj9Sx1DDv5Ruj64H9zpaU6ox0veYWHnuKrgiYXYZ1ogvqLXAYEisZ1HIXTATzQCXh-MX44WrFVQcLR4NA8sGaSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8ac81235.mp4?token=owTNkLiZ_PqTFKxhCYy6HYq-DHIUnUSNhj-sDTluLdMHn_20sZVgOkbq2XBpjzceynL_Cf4qkO4_DuK-qXZml1Q-ANZbn3d-Xft61oqcDU8vej96YBSLmKHGEUa7yKD8HvLIpLmCe5eRBglew5rkgoD_sG5p8Le9D5SC7rXU5WOX6kXDG58StEiZVdYTSUCYG79mRcVf48VWhlPqeg5s9jRr8XO2rHwzsjCbBhktf_hEbwnENRtQZ8QqxmFDVlvxj9Sx1DDv5Ruj64H9zpaU6ox0veYWHnuKrgiYXYZ1ogvqLXAYEisZ1HIXTATzQCXh-MX44WrFVQcLR4NA8sGaSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با "تیما"
توقف کسب و کارها ممنوع!
✅
تیما محصول جدید بانک ملت است که هدف آن تامین مالی یکپارچه زنجیره اقتصاد کشور برای رشد، توسعه و افزایش تاب آوری است.
بانک ملت، تجربه ای متمایز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/653549" target="_blank">📅 22:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653548">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3l2WsB5ais_z_d9GpzMc2XOrG02uofeilz5OLDolQQEd4-O1OspOkd3wBtbULvGGAyd6z552fsAFbY4cq_K2u0mUlW2MHqV9fUHJaH-jH3cipt0ojxX3dz1DK49Jx43J3g2W2hdeeQlJtMjIOPrdJX8TLpirevOEXDhQ0bjimJTt7Nz7hsZNqD5EliNeQ2bRdp7CXLh82TAGTA4EWHTqVigKsIZEoJdYFmLUBfF7eSog-a2HL5coi-Fh61w_yyEsQc40adNyHDC5zQ0-EqoQjq1_RQy0lh7uJQSFg54Pp5XxMmwmHN2s9RMLr_JZOq2Eapd9f09oVAmVHzAHzBzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک تحلیل عجیب؛ حمله به ایران در میانه جام جهانی؟/ گمانه‌زنی‌های هالیوودی، از حمله پهپادی به ورزشگاه ها تا گروگان گرفتن اعضای تیم ملی/ جام جهانی «خونین» می شود؟
🔹
گروهی معتقدند مساله جام جهانی آنقدر مهم است که بعید است ترامپ بخواهد آن را فدای جنگ با ایران کند و ترجیح می دهد، بدون مشکل آن را برگزار کند تا اینکه در میانه آن، حمله ای جدید را آغاز کند چرا که برگزاری بد جام جهانی هم اعتبار جهانی آمریکا را از بین خواهد برد و هم تصویری از عدم اقتدار و ضعف واشنگتن به دنیا ارسال خواهد کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217004</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653548" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653547">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecdf190d7.mp4?token=I6oR4V162j6ayMitvRr1vQlVxPUTgUfdkrm1iGXzdD-MMAQRsDaeViBonVQTiu-lGPjb-SfI6Z1PaNi-o-D1CChYfw-EsSbxMC9F3rWNIt7XhblqLgNLxAey-T4ngAdghT65w5r28CDkdUqrut-r-TG1gg-SlHN3Uf4_DNZStHINktGddFV8AOxlZbH7dlx81VFISdf85bZbt_7Q72jXaC61n7rR9t506AuRfd9TuO2F0ZzUjTi8frbJEuCtAIHel3Tc_ZfBnQAewOiYaoP76opdINt8JMhzbyYRN1P_YixItste7ybH13XgfMW5vdKethiltjpudnud62DpIFItXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecdf190d7.mp4?token=I6oR4V162j6ayMitvRr1vQlVxPUTgUfdkrm1iGXzdD-MMAQRsDaeViBonVQTiu-lGPjb-SfI6Z1PaNi-o-D1CChYfw-EsSbxMC9F3rWNIt7XhblqLgNLxAey-T4ngAdghT65w5r28CDkdUqrut-r-TG1gg-SlHN3Uf4_DNZStHINktGddFV8AOxlZbH7dlx81VFISdf85bZbt_7Q72jXaC61n7rR9t506AuRfd9TuO2F0ZzUjTi8frbJEuCtAIHel3Tc_ZfBnQAewOiYaoP76opdINt8JMhzbyYRN1P_YixItste7ybH13XgfMW5vdKethiltjpudnud62DpIFItXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه مهم به افرادی که کارت اهدای عضو ندارند
دکتر امید قبادی، نائب رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
حتی بدون کارت، تصمیم خود را امروز با خانواده در میان بگذارید.
🔹
آگاهی خانواده، در لحظات سخت نجات‌بخش بیماران نیازمند است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا ثبت‌نام از طریق:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653547" target="_blank">📅 22:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653546">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 54</div>
</div>
<a href="https://t.me/akhbarefori/653546" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وچهارم
رائفی‌پور:
🔹
0:06:00 رفتار آموزنده پیامبر با کودکان
🔹
0:13:15 مؤمنین با تذهیب نفس به کشف شهود عالم غیب می رسند
🔹
0:41:30 کلمات پوششی از فارسی به دیگر زبان‌ها منتقل شده است
🔹
1:15:45 منظور از سست بودن بیت عنکبوت در قرآن چیست؟
🔹
1:27:20 از سود دنیا بگذرید تا به سود بی حساب آخرت برسید
🔹
1:43:40 مؤمنین حقیقی در مقابله با مرگ
🔹
1:49:10 عکس‌العمل حضرت موسی در قبال رؤیت جلوه ای از خداوند
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653546" target="_blank">📅 22:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653545">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoNH1ASw4SOykYgBC9vssJsRKL3WEDSm4vnlgSdSh_2qacuYoAjDj0tHSV-nWrMS68PrE5244vD8wY1TB77jr-Azad9LZYY_AS4jf_KZ39ZDh48HqOirJ34vws1WXjGaN8C7aKDSfbtwSaucCI70wzn05GQ7ZwQx9KQuquaotpdu0GEd6A3Axv2lN0pREt_Hy2qqstuuLmqKtODsxTRMmkhwfnZNxG2d4su9AL56KsV48-hi4QvOth2jdYjmeYsIpzNJqhDb5lHnpvtMHzcn30cKxvpImaPkdKBoAOaczddFD3xcEJWJkzCUJcEpG5TXOGhduMRL2awsbGmbTZDQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیگارو: در لبنان، ارتش اسرائیل در جنگی گرفتار شده که نه می‌تواند در آن پیروز شود و نه می‌تواند به آن پایان دهد
🔹
روزنامه فیگارو فرانسه نوشته است:
🔹
با ادامه درگیری‌ها در جنوب لبنان ارتش اسرائیل در نبردی فرسایشی با حزب‌الله گرفتار شده؛ جنگی که هزینه‌های امنیتی، نظامی و سیاسی آن هر روز بیشتر می‌شود، بدون آنکه چشم‌انداز روشنی برای پیروزی یا پایان آن وجود داشته باشد.
🔹
حملات پراکنده، تهدید دائمی مرزهای شمالی و ناتوانی در حذف کامل توان نظامی حزب‌الله، اسرائیل را در وضعیتی پیچیده قرار داده است. وضعیتی که برخی ناظران آن را یک باتلاق استراتژیک می‌دانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653545" target="_blank">📅 22:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653544">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آسوشیتدپرس: اسرائیل از تلاش‌های ترامپ برای امضای توافق با ایران خشمگین است
🔹
یک مقام که نخواست نامش فاش شود، گفت که دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه گذشته درباره وضعیت مذاکرات با ایران، یک تماس تلفنی «دراماتیک» داشته‌اند و اسرائیل از تلاش‌های ترامپ برای امضای توافق با ایران خشمگین است.
🔹
به گفته، کاخ سفید از اظهار نظر درباره محتوا یا لحن این تماس خودداری کرده است. ترامپ پس از این مکالمه به خبرنگاران گفت که نتانیاهو «هر کاری را که من از او بخواهم، انجام خواهد داد».
🔹
این اظهارات یکی از اولین نشانه‌های علنیِ وجود فاصله میان مواضع ترامپ و نتانیاهو از زمانی است که آنها تصمیم به جنگ با ایران گرفتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653544" target="_blank">📅 22:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653543">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای الشرق الاوسط: طرح امریکا برای انحلال «الحشد الشعبی» عراق
🔹
مقامات عراقی فاش کردند، آمریکا طرحی گام‌به‌گام را برای انحلال تدریجی سازمان «الحشد الشعبی» تدوین کرده است که با خلع سلاح سنگین این گروه آغاز می‌شود و با برکناری فرماندهان شبه‌نظامی ادامه می‌یابد و در نهایت به انتصاب افسران حرفه ای ارتش برای نظارت بر ساختار زیربنایی این سازمان ختم خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653543" target="_blank">📅 21:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFp3bYyDyGO-CThRXLQIp9IABBXl_5N8EEY1byU5z-_CEmnWUGgQER6V5tWZhogd_MWG_-bYeQIGJ76D7TJTMnpqBP98rEVAZCWQ8io5WC-MJc7xjANdq1Lgs-sMji4qF24HR7b_ITX0W1IkoLmLapK4pknfc8A5IvzDFwscdlKZ3XOwsDGmul1eHeZ1KP2ix3w0ps8tjl9_Eq5LDJtJQQFJOXokXR2v8BVeVXj3gmrpXidIrDqhyb5CwiLQeSwS-fgOtvJ0rZvKQZ5sO5-I7INBVFyKkWuloqxkEGjjqKJmhmFJgd4zGBKqdCavqpWzaXfq4CW5fURfXikHZbJckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djjX5pqB7LQHVFL9in_K3-wQjoonBUA0aV5IpdZgbdRUAkF1lTTgdrf2DGEWCiTR75DeUXci9NwCoXdbEaGTIDWjxl-HBrUtZ9-42M7NBI-Umgsj0iWksFUHHEJVUinLV4PUeVihwfxyVImiSUo1PjNq6I5SA1gEhjsOMwcklSC02oABpg6ZuxvtX1o3rD6Fcu5yafQCj79BrTe8C_JikVwspgg3tEf3x8aOB6XW-yFGNY0MzvCuM8w9SZShHcCFHTtffpZbuX1HcQLLGvKmZv6ZrBBCyBaIyZ4BlCyzZSoyr-TDkhO6oKMfOuf2IKTBvgEnKIkqbBlhVdKYFZMoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feeu3e4hQ_fc4iUxugn1hedTJehd9HOU8RnRlF9yuiFx5vHnnwl0640zFsDUT3s9_5q8m7TpYaGPzM7UF5JFOdxzwGJDiqjimU7p4JxpyZGuqgvIewUC06ZjM1EvLDCvSfoO8JlljfGij7DY2PzVRFLsddss8_owYzSDoTE2CMOatRptjnkyZ9nbf8Is8FO-WFKWq0jBW0O_AcsWs8c0she6X2JW9fUUEMxwLLpOyVwZent5-1kHKIJ2pVgXBC0xgKprz3C1ZNcZZ1V1dtdJQAss8pV3OarefcFnsLmK8rPCs6wFDUYPqTL-7P-ht_epOxHdUyJFQG-7eFWionvJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BU1piTHoEc4NHPsfvemgly1zy8VKW9Qxp5zANnofso8kvV-NSJ4QXG8dZvSWGIRfnIeA_svIuozkUsCYq59B3Uvw3PF3oAtAEJ-ATbR2ql67Tp7fH8d2iFJa5JklJ_I256rSec4AKpGYib6T8k9-SHw8MSpNdzeRKn6CCrbZWyQ9rt1cxa_jq9FLJs3PkWISVzrvfNb9esPMpY_r9JgkqzGjZKeQwr7AnnQ8QXFkuo63GqgcSRlct-B5U6nIdG8HBt0yr7ljK-qnC02u62bYwt5MPfT-hd9HWXantxARc1tDK5hB1JKcL-TdDeSpHlhG0nweXYFw6-No2or8-E04Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbSu3V09fOYuWhNN8KT4COcAJjK97ttElyRJDxXNJ5H21JP9c5pTo7KVwxQ9EB_TatQCkgjP9Ls5hu04uBVQWsf4dGX28mOjeWe-CkV1J93fzweXPFVfFDSLRXr8UmvXU5LpXH66rMP0AnB8CUtVKrH8lMOiX68hkq6m15cSjFW5kko_0I30QwJJiwnRp7iFzU9WNPKxaBfNzD9FA37TlAnAXeofXjvVw15x70q9EDl1-Uib0PaXQlkXBdtAyDpcS-01f8eafyK1_P0edu3k55T0FpHWq95pP1eEYKm9Y_K3wlbg0xUvQjG-U2hd4v2TUSQ1A8khJDVLU3nZcyPPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FP5AnC918X52dgPBrs0KLE29iQB6Lu8zedMpwE9ny5Ms9HR0kVMhQXbnRxPup03MVZhptbQ_65oPG0OEIAIIOpOeDyzJ98ZdV_5fhTvyS9sTcxX-oYUK3bKH8Rr4PijeBXxo8mRg-HsCuwa8hpzMYaLVODyLerx75LcFy5YpLz_oAc0p6fFzgxuajpQ38zey8GiO5vzF1OWGpF1pfxitaxMh46pODyh75GyWHodSJB36tN0eiAQtgz1ywjSEM620HCtKH3nuFN6WNHQoUMWa9ATi9Tx1GLzRk_y8hV24Nbj3fsdjMj083zawYAsJqyuSktdBAqiG_2dT68JdFDGwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdv2psFoLdCBEAdUxU0NrBQdfPFRbgG5OKNhCuBreP2r49EPl7T47l28pUcCGoOxkxWC8oCiQG2lC7xwo7oBSaCtPOSPu5vZsvy8gWbDnaPV6YDGUc29cXNW4Ba8K_JbGG9zybsZktev3VCXWVBo6KS6e_VnelWr5e5US18clSSli681vYdtjGyD_jXa3hcMMdIqoQ97FyM_0AHOMzS7L3AXdXsROCHfEN9gKz7t7BQau4SKwUTyOiE40ld8GJAKoQ5CLuvREwhByaBogAuBNPKZQYhbt5pSthobk2zv2orcyVOtOipcjjfMYuUqPSPqXc307ZSW85ZkNyMMmdgDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPZySejw-TrzJP9YW1sBlIcL8hd6fZkGSde0712LAzvm44CHo-dfJBOGnR3RB4xEUNymYMAVHGa52NL-5WUUipRs7uaPTaPMeKk63u5oXw-jTzCl7Z8c5YB1sXWesYZEo0PU6P5K3qPwl--P9P9ik_fs4mmxj4ewhL02Ilym_8TmtTddVd_uIpvhYvVYYHJMwkujPaGzx5vlKgVMAGGVEiHkt9jTm3fFYqMBRJnAKDxgmiolrzNYDuGTp9hw0zd6SQJeOosdvfeOvjCgoTQyhm1JS3sSvemGLp4JtL_Ljsv1zlAgbsgcJAr939agdFwJPHjJF76yf9VnOGdGOe40Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/or-cOsamEH7ZskAPwfaxzaEeUz4ZixdhiY2b0a7X77FBVdM-18Uho58FmOsJASe0G6vAF_EDiBvciDDVtZBUin0IE0-UBNaUiHBiD6A0j7gM3gheYCahPFczs6nKukD_QWLZG3qHXC9Kb-KwjaC5PkwaqutWzUQMsiW7S-UL4OLiTsTeu13lwnd3QPkmLCeCR7hdIQfxHxVrSR23ebDHb8tKdTvvSKJpVIvpDMWQ5V1N8eJPoQ0IVvMYOG0h3O-o0NjssNQmyIBCfpq5pdGqobqHvlsyxzxo2R72MvSKUvh4yWCfjfZo4s7I7fnJw3p8InvA-w5zSk7QWH25pVfXaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
در مسیر
#همدلی
و حمایت از خانواده‌های ایرانی،
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، تلاش می‌کند سهمی هرچند کوچک در این مسیر خیر داشته باشد.
این خدمت، با حضور و اعتماد شما مردم ادامه پیدا کرده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/653534" target="_blank">📅 21:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
حادثه امنیتی در پایگاه نیروی هوایی آمریکا
🔹
یک حادثه امنیتی در پایگاه نیروی هوایی پنساکولا در ایالت فلوریدای آمریکا رخ داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653533" target="_blank">📅 21:24 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPgt_UY-PCIWl_41PE1OSf-fz4gIOg76_qw28UGCbjLeOL88ocvkyyCYjpy0ynhc6V2weIWIpqWgzXGpRrVe4KPFP-h0M53yC9E0GNLhsGnsz7LEfzLY84fXIymodDlR_vCuFv2S2kM1suqSQeC6FpGJiLn5oMvk-4hEc7uKCgkJFMp6Gj6-55J6zNGLnMLYRcRdkkGAJv7O5SfFnr3oQbWEWLOq3wv3H8Rl40Z2bkq3kuq82r17kYQM9QhmLggWk9m4kqJdwg6NAYk6k7NYr5v_-xq0N73A28RpcgNCkr9GVR3TuuryIFfwfurxDs0OuT_pHsQ3ebu45VCWgb9v2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه آمریکایی هیل: در صورت عدم توافق با ایران قیمت نفت احتمالاً هفته آینده جهش خواهد کرد
🔹
پاتریک دی‌هان، تحلیل‌گر بازار نفت در مؤسسه (GasBuddy) هشدار داد که در صورت عدم دسترسی به توافقی میان آمریکا و ایران برای بازگشایی تنگه هرمز، قیمت نفت در هفته آینده با جهش روبه‌رو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653532" target="_blank">📅 21:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653531">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd984e22eb.mp4?token=Smnvd1e7gH2O-nv7Kmws0j16PLev6QG5H6D2Bldy18qDC3ImRuqu70t1ql_aFnSF7yjql8ctqz4Y-l4B8V0-Va-2Q0f3QPfcdpx-3Y5fGvEaTO-faY0w47Zeh8vVCT0r8vR-sZQ61dnnwHKebv4dIdNilED6LF_YMkcGq9ewIshpFbuzoUTl9qblZ6gUUEuD1Utj3YDOTlO_XmrdHwInqb45knFhjxcQ8363Qubit6ts6jQ2p6qM1CnGeUo8Hn1XZYUra2qVv8sXbWqESccnRa1C4HvJLcMKyOQnuvGLzJ0sm1dFddW-FISF8zHMhujHaaHmi4oyFPPOfrxaQbWF9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd984e22eb.mp4?token=Smnvd1e7gH2O-nv7Kmws0j16PLev6QG5H6D2Bldy18qDC3ImRuqu70t1ql_aFnSF7yjql8ctqz4Y-l4B8V0-Va-2Q0f3QPfcdpx-3Y5fGvEaTO-faY0w47Zeh8vVCT0r8vR-sZQ61dnnwHKebv4dIdNilED6LF_YMkcGq9ewIshpFbuzoUTl9qblZ6gUUEuD1Utj3YDOTlO_XmrdHwInqb45knFhjxcQ8363Qubit6ts6jQ2p6qM1CnGeUo8Hn1XZYUra2qVv8sXbWqESccnRa1C4HvJLcMKyOQnuvGLzJ0sm1dFddW-FISF8zHMhujHaaHmi4oyFPPOfrxaQbWF9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در فرایند رضایت‌گیری برای اهدای عضو، کدام عضو خانواده دیرتر رضایت می‌دهد؟
دکتر امید قبادی، نائب‌رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
وابستگی عاطفی میان اعضای خانواده، تصمیم‌گیری برای اهدای عضو را دشوار می‌کند.
🔹
در این ویدئو ببینید سخت‌ترین رضایت‌گیری در اهدای عضو مربوط به کدام عضو خانواده است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا ثبت‌نام از طریق:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/653531" target="_blank">📅 20:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653530">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7deada65a.mp4?token=VowMLFNAjVxhBWmY66-1lRZzP4O7Cj171FHQpiqtB3IKg-xncJqyN_pHAaN3_P0-B4cNiCop4vkb-14ZpA20gOoh3E9gmP59LOnOrHvDmddZmxwFqhG931XFbHSc_juTOLzJQP_s8ASVgs4WdrMfhNbZAIVQUWS0gwuwd9-Gf51QmfEyMSoO0MnLg8dRgPaxKBYNKMpHs55tk8B4Wln7gSE5-M6iJNCny2TDZcpXYg2ujybQA7kcC6rrhXU3P16hlhqvAd00PJRdd_ZmKMWQKntpq58yaah-qelLRjLn5rvxgxhpV09toBdymsqF1yAg1Yt8fpufTuS8IJGPBBdzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7deada65a.mp4?token=VowMLFNAjVxhBWmY66-1lRZzP4O7Cj171FHQpiqtB3IKg-xncJqyN_pHAaN3_P0-B4cNiCop4vkb-14ZpA20gOoh3E9gmP59LOnOrHvDmddZmxwFqhG931XFbHSc_juTOLzJQP_s8ASVgs4WdrMfhNbZAIVQUWS0gwuwd9-Gf51QmfEyMSoO0MnLg8dRgPaxKBYNKMpHs55tk8B4Wln7gSE5-M6iJNCny2TDZcpXYg2ujybQA7kcC6rrhXU3P16hlhqvAd00PJRdd_ZmKMWQKntpq58yaah-qelLRjLn5rvxgxhpV09toBdymsqF1yAg1Yt8fpufTuS8IJGPBBdzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران؛ پیشرو در اهدای عضو
دکتر امید قبادی، نائب‌رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
ایران رتبه نخست اهدای عضو در آسیا و رتبه اول پیوند کبد در جهان را دارد.
🔹
سالانه حدود ۷۰۰ پیوند کبد در کشور انجام می‌شود.
🔹
ایران از معدود کشورهایی است که پیوند اعضا از بیماران مرگ مغزی در آن کاملاً رایگان انجام می‌شود.
🔹
مردم ایران در فرهنگ اهدای عضو، پیشرو و نوع‌دوست هستند.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا ثبت‌نام از طریق:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653530" target="_blank">📅 19:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653529">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef6033519.mp4?token=MxoJY6aRQmo-LKBbhg0g1y0Mz9t0HoL2UHmfG7dZ1GWYmOD42jzmnrlbtNh8NDifEq1P81iDpbmsxdg05vuXu1z3V-y6JqVWhxZutzdVP1ZpxN3pkRo_UVZy0PmyftZHaIK5pwaF4iX1MqWbdLiod87q2JOdF8Ldf-qrFmVh2cBznYvuwcqChXFIqV44h5yB2lRWGBaoezo3_PFFqOJv-hCfGmYfnuZlk7nFTWn1szqZauRgDwQYZGm66_NAPnkjvhEuZY0VWTobYbZI_nk7NIvSISg9wNZWfsizPmcUskUnxFtU3ilkY7IqUF_R-09APgCkLqdUodgmoTUeTDkVAQzek9nh_VigkhabfdvbqH1zlT_Jzs5Pf1O2bnSvjmUj5hmrhzygCPsKnjMa0Mzlb7JYRn4fDM8nanRK5wtGrn649jwXFFcXHptO7QaaqMFXxwur97KcERcGIZ0XPpMXHBuRWNYwQidHerq3Q2lKvQfhMvz85ND0fOKjod85eELYqHgkjaVoyzDaNFEt1jWW57QQQ-weB_ylGQKPxQikSoDiN6sZ7Sonr4WRVB4YQ39vkKnjEub2pmW48x_Lki1hVURo3By18dtcCTqitJAaRcolz6V_xGp7X8A3pItxTzOH-mYSIRVEOtc5CAk5VBkuhqOs19YJwCcq9zb49KFFxr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef6033519.mp4?token=MxoJY6aRQmo-LKBbhg0g1y0Mz9t0HoL2UHmfG7dZ1GWYmOD42jzmnrlbtNh8NDifEq1P81iDpbmsxdg05vuXu1z3V-y6JqVWhxZutzdVP1ZpxN3pkRo_UVZy0PmyftZHaIK5pwaF4iX1MqWbdLiod87q2JOdF8Ldf-qrFmVh2cBznYvuwcqChXFIqV44h5yB2lRWGBaoezo3_PFFqOJv-hCfGmYfnuZlk7nFTWn1szqZauRgDwQYZGm66_NAPnkjvhEuZY0VWTobYbZI_nk7NIvSISg9wNZWfsizPmcUskUnxFtU3ilkY7IqUF_R-09APgCkLqdUodgmoTUeTDkVAQzek9nh_VigkhabfdvbqH1zlT_Jzs5Pf1O2bnSvjmUj5hmrhzygCPsKnjMa0Mzlb7JYRn4fDM8nanRK5wtGrn649jwXFFcXHptO7QaaqMFXxwur97KcERcGIZ0XPpMXHBuRWNYwQidHerq3Q2lKvQfhMvz85ND0fOKjod85eELYqHgkjaVoyzDaNFEt1jWW57QQQ-weB_ylGQKPxQikSoDiN6sZ7Sonr4WRVB4YQ39vkKnjEub2pmW48x_Lki1hVURo3By18dtcCTqitJAaRcolz6V_xGp7X8A3pItxTzOH-mYSIRVEOtc5CAk5VBkuhqOs19YJwCcq9zb49KFFxr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس مسائل بین‌الملل: کشور عربستان به دلیل جنگ اخیر با کسری بودجه شدید مواجه شده است/ بخشی از قراردادهای مشاوره ساخت‌وساز توسعه در عربستان به خاطر جنگ متوقف شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653529" target="_blank">📅 19:06 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
