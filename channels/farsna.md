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
<img src="https://cdn4.telesco.pe/file/GmlbRDIKhn0Ussu6ZWHH711tuSxn5XFd2GfIQma6718jGpdhPOM-nAp1soCxEWmuefnG2OFVHOpXsTc1-I3vV7sfnyFsg4QKKxDCfO4w7_E80i_STTIe71z6r4l-vFW8g0nXFMwTsaQ_uVMYkSZMAtSKZFNwgqZbfQXm_HG8Nck9oFO5wGeCnllRF96ZjMR0N-3wBIqt40QuLLVgUQCxKbFWT2W_uzR0_wbsTxmNTYaxhFFfT3jZypBfYmEGA2z_17PGM7pAbZw1JQ-euTR9iLPpUVIW7o3TiQwblORa1W9zR5-obTpO3GtoDUzWJW3GIyLVR91OYzRJG5kaxa81QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 13:52:58</div>
<hr>

<div class="tg-post" id="msg-435084">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در اصفهان
🔹
سپاه اصفهان: امروز از ساعت ۱۵ تا ۱۸ در محدودهٔ زردنجان احتمال شنیدن صدای انفجار کنترل‌شده وجود خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/farsna/435084" target="_blank">📅 13:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435083">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqL98RholiChFHRfm93G0Tf62L9Id054uCo5gwjfU00PgeUGFX4NkRi4UeKAGjTfTfXX_GX4_YVZxpO9uUd-fOND7HAh37basUOigsO4O9xMbY2-OdClZNOQPvzSlrEIj6bkGeDo0CPDQE1UkKFPKLcp9IMr51UFGzmT9PTNhM7YLkotT7XM8G7_YxZRY2807wY5v2qVrLmpbGyBL697ic28Qv6WKRWljjMdKDGbQhSJ4hioQ3E-Ezo2pgZRE2YQXp--TuQbSqe9EOzYT9EFCNusAUaZIqq3ystsWUg6VFIthNp6LhPqTqtEf_DZr4MuCdXV-B3qsp_DesPalK4qVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توری که امارات برای ۲ بانک ایرانی پهن کرد
🔹
وابستگی ارزی و تجاری ایران به امارات به نقطهٔ حساسی رسیده و به گفتهٔ خاندوزی، وزیر اسبق اقتصاد، امارات با استفاده از شرکت‌های پوششی، صرافی‌ها و حتی شعب بانک‌های ملی و صادرات به مرکز اطلاعات مالی ایران تبدیل شده است.
🔹
وزیر خزانه‌داری آمریکا نیز اعلام کرده است کشورهای خلیج فارس اطلاعات مالی ایران را در اختیار واشنگتن گذاشته‌اند.
🔹
خاندوزی به بازداشت مقام بانکی ایران و محدودسازی حساب‌های درهمی اشاره کرد که برای فشار ارزی انجام شده بود.
🔹
اکنون با وجود اینکه بیشتر کالاهای وارداتی فقط از مسیر امارات عبور می‌کنند، نیمی از تسویهٔ تجارت ایران در این کشور انجام می‌شود.
🔹
کارشناسان علت این وابستگی را عادت تجار و سود ناشی از ارز چندنرخی می‌دانند و پیشنهاد می‌کنند ایران از مسیرهای جایگزین لجستیکی و شبکه‌های مالی چین، عمان، ترکیه و تهاتر استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/farsna/435083" target="_blank">📅 13:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435082">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsPi3h-qqa8eCCHZxJ2gsXFi8UBt9QQG6c_i94s-IX3j6HRF-2iN68moxR-qWHxQVnlNqfWQ2V0xufGo8I_syVJpxvejSQTVxa5_6ibey077Uyu2T4nNHY7S4Zkk2zMA_GSwikyw4TShj4V9siesESWjNe_sf2q86OVMeuj-AOKvlbxTsu-sXL_T2BF2lpgghIHMD19d5782q4jqli5BUG9kdg8Nk8nZzodkA86p8hywGHGAB_wbsz522chrWJ5F-mrkmcuCsJKA4UJ1B-8OYpVgN7shHcI7aMfFJFixz6X4pgH0Zl1q_xIIfZiaVsNnQIGiky3fxn7gpowrxM2R9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت صمت تأمین نشدن قطعات سایپا توسط کروز را تایید کرد
🔹
مفتح، قائم‌مقام وزیر صمت: زنجیرۀ تامین قطعات وابسته به شرکت ایران‌خودرو، باید براساس قراردادی که با سایپا دارد قطعات این خودروسازی را تامین کند، اما این موضوع انجام نشده است.
🔹
از بهمن پارسال هزاران خودروی کوئیک، اطلس و شاهین به‌دلیل عدم تامین قطعه در پارکینگ‌های سایپا مانده و قابل تحویل به مشتریان نیست. تعداد این خودروها آن قدر زیاد است که خودروساز دیگر جایی برای نگهداری آنها ندارد.
🔹
بخش زیادی از این قطعات به گفتۀ مسئولان سایپا قبلا توسط شرکت قطعه‌سازی کروز که حالا مدیریت ایران‌خودرو را برعهده دارد تامین می‌شد.
🔹
وزیر صمت پیگیر ماجراست و در صورت اجرا نشدن قراردادها از طریق مراجع قضایی عمل می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/farsna/435082" target="_blank">📅 13:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435081">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b219d0099.mp4?token=VJsk2IrlAuag6S5UPzi-pvwilRVFdytQPNaZ8APWVtvDH6YlOsW5VgPsacTgKHjMwnm4Hpn-26EC9JFifA4boKmEFF8_MPJS_nfzWgi0lsu1H-BjfssPvMAMZS_XO3Fi83M2wG8Y4cE-eEAZJ-gHcWs67wyUbhpfwcNKrz87BrrqBrviVGu4DSdbB8mDd1VC-gei8e8IHdJeVtr2YIRd7p-YpC8fuZMh1jp064W_SPlaLp0Dvm_obdwBjJhEByrziBtWKKe8TqBcw3qI2LlWCORhVbLRghaLICL3RHndeyar04st7IF2qMP1Np1CDPnBbjuiheD2qlC8hOmKstaqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b219d0099.mp4?token=VJsk2IrlAuag6S5UPzi-pvwilRVFdytQPNaZ8APWVtvDH6YlOsW5VgPsacTgKHjMwnm4Hpn-26EC9JFifA4boKmEFF8_MPJS_nfzWgi0lsu1H-BjfssPvMAMZS_XO3Fi83M2wG8Y4cE-eEAZJ-gHcWs67wyUbhpfwcNKrz87BrrqBrviVGu4DSdbB8mDd1VC-gei8e8IHdJeVtr2YIRd7p-YpC8fuZMh1jp064W_SPlaLp0Dvm_obdwBjJhEByrziBtWKKe8TqBcw3qI2LlWCORhVbLRghaLICL3RHndeyar04st7IF2qMP1Np1CDPnBbjuiheD2qlC8hOmKstaqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محل تحصیل فوتبالیست‌ها بازهم سوژه شد
!
@Fars_plus</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/farsna/435081" target="_blank">📅 13:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435080">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c04d602d9.mp4?token=Pc593oOO7UHTXgJSIEtWZPwhI8974pzLI08uL4Tm-RzVXp-avDPIAQTVLbB5VWJniSTTCePFZ1h7fEbgubXGrn4gq3P89wJvoI41soBydjHcPQiKkb-GPfSpVhv2EaQaLwqsYNPbW1lHmkYKoqT-RwKYSTd0jOKWHQZr0KjKoDsfJvrIwidfsUfu0H3OzzkZO-1aL7yH53gFMYU4GwodDGqE-SViLKesL5Asly_cfd5Hxe1Qx08FKLU41P4HufVowQYtL6Vm5N_aWUwLYiXy3asKHIKbq6_609PLPWMhaI9ttsqpX5ZoqtzPh4tMsgLvhPeN6wXtfrfzPsqNxt364A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c04d602d9.mp4?token=Pc593oOO7UHTXgJSIEtWZPwhI8974pzLI08uL4Tm-RzVXp-avDPIAQTVLbB5VWJniSTTCePFZ1h7fEbgubXGrn4gq3P89wJvoI41soBydjHcPQiKkb-GPfSpVhv2EaQaLwqsYNPbW1lHmkYKoqT-RwKYSTd0jOKWHQZr0KjKoDsfJvrIwidfsUfu0H3OzzkZO-1aL7yH53gFMYU4GwodDGqE-SViLKesL5Asly_cfd5Hxe1Qx08FKLU41P4HufVowQYtL6Vm5N_aWUwLYiXy3asKHIKbq6_609PLPWMhaI9ttsqpX5ZoqtzPh4tMsgLvhPeN6wXtfrfzPsqNxt364A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای پرنده ترامپ را ترساند
🔹
رئیس‌جمهور آمریکا در سخنرانی خود، هنگامی که صدای یک پرنده را شنید، ناگهان ترسید و گفت: «فکر کردم پهپاد است.»
@Farsna</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/435080" target="_blank">📅 13:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435079">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دولت لبنان نباید با صهیونیست‌ها مذاکرات مستقیم داشته باشد
🔹
ما بر مذاکرات غیرمستقیم تاکید داریم، جایی که برگ‌های قدرت در دست مذاکره‌کننده لبنانی است، و خواستار عقب‌نشینی از مذاکرات مستقیم هستیم که تنها به سود اسرائیل و به معنای امتیازدهی…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/farsna/435079" target="_blank">📅 12:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435078">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: توافق ایران و آمریکا که شامل توقف تجاوز به لبنان است، قوی‌ترین برگ برنده برای توقف حملات صهیونیست‌ها به شمار می‌رود
🔹
ما از ایران برای توجه به لبنان و مردمش سپاسگزاریم و از هر طرفی که در توقف تجاوز سهم داشته باشد، قدردانی می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/farsna/435078" target="_blank">📅 12:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435077">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: میدان را رها نمی‌کنیم و آن را برای اسرائیل به جهنم تبدیل خواهیم کرد
🔹
به تجاوزها و نقض حریم‌ها پاسخ می‌دهیم و به شرایط پیش از ۲ مارس باز نخواهیم گشت. دشمن دیر یا زود تن به شکست خواهد داد‌. @Farsna</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/farsna/435077" target="_blank">📅 12:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435076">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889ffe9d37.mp4?token=sOhK7dTChTb_C84jTf3DPWS3nMD4NCIMDqkcxTfhqTFcwKlilZDBrprh1mT33PFvIvQy2hiym5jbtXDVIRr12-WgcAOFfnrMvMPZ4kIQXZf_FJAlqm2Mt1TFUaZK94B99SYbZXQ--JZf8LxHhAEnhR5rxIDseuCB44PXe4-1Gh5oSIPfA3JSSktBOqJMmK6hUV9S5qVIlM4hjnPMlz7oA783D-XqbGc4ME0T45alHbQlhikQkqe9ihsfiwtkjoZQpJUWNJV_8eqF4HxbuUcRi5OzISjYqmpfyhzsxa04tCT6v5a3IE_sjgyTvAbfAfPaGBU9oqz7cOX-gPLBb-tamg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889ffe9d37.mp4?token=sOhK7dTChTb_C84jTf3DPWS3nMD4NCIMDqkcxTfhqTFcwKlilZDBrprh1mT33PFvIvQy2hiym5jbtXDVIRr12-WgcAOFfnrMvMPZ4kIQXZf_FJAlqm2Mt1TFUaZK94B99SYbZXQ--JZf8LxHhAEnhR5rxIDseuCB44PXe4-1Gh5oSIPfA3JSSktBOqJMmK6hUV9S5qVIlM4hjnPMlz7oA783D-XqbGc4ME0T45alHbQlhikQkqe9ihsfiwtkjoZQpJUWNJV_8eqF4HxbuUcRi5OzISjYqmpfyhzsxa04tCT6v5a3IE_sjgyTvAbfAfPaGBU9oqz7cOX-gPLBb-tamg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویری از انهدام خودروهای نظامی ارتش صهیونیستی با ریزپرنده را منتشر کرد
@Farsna</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/farsna/435076" target="_blank">📅 12:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435075">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دفاع از لبنان و مردمش را تا هر زمان که لازم باشد ادامه می‌دهیم
🔹
هرچقدر هم که فداکاری‌ها بزرگ باشد، هزینهٔ آن از هزینهٔ تسلیم‌شدن کمتر است. @Farsna</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/farsna/435075" target="_blank">📅 12:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435074">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: هرگز تسلیم نخواهیم شد
🔹
ما با تجاوز اسرائیلی-آمریکایی روبه‌رو هستیم که می‌خواهد کشورمان لبنان را تسلیم کند تا بخشی از «اسرائیل بزرگ» باشد اما ما هرگز سر خم نخواهیم کرد و تسلیم نخواهیم شد. @Farsna</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/435074" target="_blank">📅 12:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435073">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: هرگز تسلیم نخواهیم شد
🔹
ما با تجاوز اسرائیلی-آمریکایی روبه‌رو هستیم که می‌خواهد کشورمان لبنان را تسلیم کند تا بخشی از «اسرائیل بزرگ» باشد اما ما هرگز سر خم نخواهیم کرد و تسلیم نخواهیم شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/435073" target="_blank">📅 12:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oR-Dc3aOtjVkCjKSTDkOb_tSKdZamkSNP_8s053TI9rDgTqLPJq0Wbu5rq9ha0nl6yrJVfLx2AyYvYXtHgH6HXnWIAP2sZalRw1PVxPsOAWbj6ZIvF4gEgYUltBbKiu_MkJrCdjmCsfyfxpz5TUGn6KMI0EYN-4X1u_0PSS5vPDdt1J1APEZx_GnrADZxn5Opodo8zkI2QQ8P62S4Tyh6qWTRMR6ZZVSTtPCVhvkueb8jjmWnuzwxzOmcZZik37wDqRrwdfI7dptiDYqmZfidFp9WTBKb2LK8zFq_kqwsZ97BNYORuc881f6xSodQgfrYar6L3lPHfQe-kCeqsxZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMEybxtgvT7BRWolkLrfyFe-8fqC10m12_o_lNWA15xn4_gr_gf-S3zYX8abFJpILFwPtLPY7t2OQ4vc4s62MbSLRA8S1j6O9Hrg0fOuyanlZiMa6FcJMtOGhh81JNNcQ_98v_ZjP_W7nG9WBmHVQiC4xKJn2vBiqhqIqW0qWYumoWAD3LkOgSpfhi18GmyxIwVXkYr7ORPQf_9CxXGidJ-bbI7-fdGuJmPr_YE8wysuVabxPULm3f7jCyNDlmPDgEFAq5flVXtOxfpZ1EHDjwWm0Cxp0qGQAWCTL7o-PSl2UcYcQwIX7I-WyzUn0IKe83GCADA50PM-CAWc7EYq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pnc235MAltDw2uaH-oMpYJkHEHoPwTiciPooqpMpWFqj6La6eI2PbxfrL1kkacUD04lgd2TKYi0j3NBfYn_DP9Czlyqj5eAU_JwZZ1VDvVvC3S9ykTznFuBJuFBr1yR8cmuBkHo5bBUPmnjxs8pbdskVxARtjevsgVivrMasB6aw4Wsi4Shu96d7oaA0g9wyFtbTW4-82gr0ZYtO67rp1DW997LNQ2xsvJ_oeZtu3Mlkjis1mOAI3GEtu4rdKWBjmZG0KUawYEBni8SZTqmgMoFqnBQgqy9eRpRTT5yNs3m38HlSlGV_9nGaQbF4sju79aO1pZsI6i2SGMP3okrT2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارسال پیامک‌های تهدیدآمیز منتسب به ایران به شهروندان اسرائیلی
🔹
اسرائیل هیوم از ارسال پیامک‌های تهدیدآمیز به زبان عبری به شهروندان صهیونیست خبر داد که در این پیام آمده: «به شما قول داده بودیم که به‌زودی ستاره‌هایی را در آسمان شب خواهید دید که ستاره نیستند... به زودی خورشید را در آسمان شب خواهید دید، اما...»
🔹
کاربران معتقدند که خورشید در آسمان شب اشاره به حملات موشکی و پهپادی ایران دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/435070" target="_blank">📅 12:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در بروجرد
🔹
فرمانداری بروجرد: امروز و فردا انفجارهای کنترل‌شدهٔ مهمات صورت خواهد گرفت؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/farsna/435069" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435068">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجار بمب در پاکستان جان دست‌کم ۹ نفر را گرفت
🔹
در پی وقوع انفجار در یکی از بازارهای شلوغ منطقهٔ شمال‌غرب پاکستان ۹ نفر کشته و ده‌ها نفر دیگر زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/435068" target="_blank">📅 12:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
پاسخ سخنگوی دولت به سوال مخاطبان فارس من دربارۀ خدمات درمانی برای کودکان زیر ۷ سال
🔹
مهاجرانی در پاسخ به فارس: خدمات درمانی کودکان زیر ۷ سال به سه دسته بستری، اورژانسی و سرپایی تقسیم می‌شود. بر اساس بازبینی سیاستی برای جلوگیری از افزایش خدمات غیرضروری و کاهش پیامدهای منفی احتمالی، فقط خدمات سرپایی (مانند برخی آزمایش‌ها) از ۲۲ فروردین لغو شده است.
‌
🔹
خدمات بستری و اورژانسی کودکان زیر هفت سال همچنان به قوت خود باقی است و نگاه حمایتی دولت در راستای سیاست‌های جوانی جمعیت پابرجاست.
🔹
معاون درمان وزارت بهداشت نیز در آذر ۱۴۰۳ تأیید کرده بود که مصوبه اصلی لغو نشده، اما این تغییر جزیی در فروردین اعمال شده است.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/435067" target="_blank">📅 12:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkiAxrtZUVLUMwp4tJ9nvsAP2gTdVAo_OhwlZNRxLa70-EEKAz4bXWU6OmanavQTxbzTG8a9TBoTSss3eNHRCNnRunzMTLf4gcFDDFRRQTxr67IQ78RxzhyIQ4H-vM2AySPaRpBrWQ2zKMTgl3m9j2Y_hB4VXd6jtzusQo5ZGbihSPAYyuZwQphUq-GMxdNVkoW1WkZbzc8tw8x00YWzXON6pOyHCli4Zraoei0hr_lOZ2s9aRnrIeXt3CtHFkfZKOnQgmfVuELgODJt2IWBYr7Rw4XukIj1hNUNrW8CmDMOIdRrmL7M9BdePcD7youEeeHmEbBkGuQI8P-q-8DZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۷ همت کالای قاچاق و احتکاری در کرمان
🔹
فرمانده انتظامی کرمان: درپی برخورد با مخلان امنیت اقتصادی در ایام اخیر و جنگ رمضان چندین انبار و محل نگهداری اقلام مختلف و کالاهای احتکاری شناسایی مورد بازرسی قرار گرفت.
🔹
در این عملیات‌ها بیش از ۴ هزار تن میلگرد، ۱۴۰۰ حلقه لاستیک خودرو، ۱۰ تن برنج، ۱۲۱ هزار قلم انواع لوازم آرایشی و بهداشتی احتکاری و ۷۲ هزار قلم اقلام دارویی به ارزش ۷ همت کشف و متخلفان دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/435066" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621ce4d683.mp4?token=hV9z8Xt62h30U04Sumr_ohN6hhFuTWFR4l6Svcmyi_p0DUDHRyMpJ-C_QtAFAPh0CwkbAu6ndv3ivwjnXXoxshgCM07acAdcPHXcenYc1XOOPEI0AEN1CF0VwoGhQyCUqvsn62sp3bH8hi8cr7Jr69MVB4CiygCh6RA-83HPvKSjak-LFVNcOzBfg172rFbXv1PSxCGtS9wEHhBz44WVEA7fTqZbrdxXDi2IKadgNtg2LPrVEdpItNc-d0Jb0HTNq5y8fmx5HLdO4AefdxN8Ms5whrm4StTYrLM3KL_h10h_h0o96SG5aa-__i4qmbshAEMAR-Bz0FPnEL29ZC2CGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621ce4d683.mp4?token=hV9z8Xt62h30U04Sumr_ohN6hhFuTWFR4l6Svcmyi_p0DUDHRyMpJ-C_QtAFAPh0CwkbAu6ndv3ivwjnXXoxshgCM07acAdcPHXcenYc1XOOPEI0AEN1CF0VwoGhQyCUqvsn62sp3bH8hi8cr7Jr69MVB4CiygCh6RA-83HPvKSjak-LFVNcOzBfg172rFbXv1PSxCGtS9wEHhBz44WVEA7fTqZbrdxXDi2IKadgNtg2LPrVEdpItNc-d0Jb0HTNq5y8fmx5HLdO4AefdxN8Ms5whrm4StTYrLM3KL_h10h_h0o96SG5aa-__i4qmbshAEMAR-Bz0FPnEL29ZC2CGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیروزه جابانی</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/435065" target="_blank">📅 11:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435060">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS_CfwnhJlwkxnTQ-LoMIsspQ4lyIx5HKkkD4VFgYUD8cYTbzrY4J8_2ikRJkzTXm7paPe__U8MXIFXT3R4WjA0sWVTCfORS85exvTKgJUW9wIj0_OwjnrmwpzGnR3eSrPDQDMUjbt66J_w8UEXABQj_cK2YecKkZJWjEWbZJdCZ70Z4QACp4GjFednEJyYcviIGNMhP616-pFts2IUxCaIKYLgE_XsksX_4AoGJ4nzPhXxK8UhlmiMlH8SYuHd_Ed2EQPjO8tbUooVEUjiDPOlYV7aiVgZOOYKHtywZ8OLDk8zn_gUUbPA3QpfvwELXFVWQVROBQVPMjtR4rkoigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h83xJ0rm6kYcVMyZxVjT6OtK7zq1aB9ieaYwTA6dvpDbTBCalcJYiTrlLSSYV9om_M7mymH_-UwGdsNiqNxwNHUyEPiAD9zHXwxQHy0Q1rE81cfr0t1bl0INntluESJs_DniGoEAYa_-_o02IykLtEqdVcnePELn-0rfolNZcdEPKxT2iwuM7dPNUfeCX_69cQgnZ0jX5L2hZ0ifQCWhn3LFjiwX0LtSKVaT23UVnimXLAOsvw9rGxb6D3BtTOnx3xXUYX1ADMJ1T1ZFyKA4SJWRZnUyknLWC5ZKuDaYw5VB6oVIrQgEvqKA5PuwDsBTemMmpCEvvw7dYZnHDNNAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bk7J4usr6nAiImrh5qpO8FnvqYpf09oUzboZ9xHmIpAFV_aTo83d6Y_CqTyYnBBouBEvDNmD2IH9-KKG2onA3Kxd5FFtggLD2ePwrOrU9UWP7QNoY1SY83bmkiueUsMMpoI3iWjKU_6sRHRcjv06_QKVPJJdubVdTCRgfRFvAJsHFE4wAtiPtJMjOxgXl9kyK_9F_yHA2Cu63Vz31O7gdW9yktSNU1-S580AtwODzNzjM_xP_4I5xEma3r_rZqfAb7qekal7vN0dJi7TLWr8G7xkumn1L2fAh0VZQEx60e8zZafsFozpzyfaenoE5DWu7kxFUglYnksldYxUQ2h2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftFLqmq2ZBIkr6JFRnCAHOPefb_LeKHPMwz9V9VolBKuryDxK2d2wZA6JU1VOxf0uEnG9zMcCNthI2OjWfMZZ-yH2Le7P2wmA0jvtZW5MN0Nzzl1XYT_sN2pgXXOKX5IlvesIZ-kakRwAL4Daz_mYnEUHmOatk3iMhwbRGdF5dnqmhyC508D1ooGDJuczCPX7aLyK-gZ5wpLqoS9t7TnAtNh-jfjMnMAWGuPXQPo5Ii4VPr0PWMJsbMNo-2kmJGvUhev8oAjkwKXqPbD5bI6ivKOt7xc8V8iPVEzRYZa7DcY42cwTUmHIPRwqyjDpxtdoH8FVgHIUFEB08u3a1Wcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_xtyohgexta8VRx-u1pdEPJWiuK61akj__MtrPIGs0QdZCuQtZJDERJ-dSTgRKi3WW2raCb-JryOFLCGh69X-HO1OCmrORBxmdloI-dzjL7GWdHhOg3Vp50KT5GhDwdGCWZ7jtfURGE5zFg9MM0eP0D9sJXQQZklG8MSeQP2M6Z3Xb_BI9u1IZSGVSxZ6HOz5MdCdLplKOnS4KZobh17VZqtiaXqUu_MqoHHSdU0af00xePrr0vSU6zk8inTUALGlBGGstEZys95-2wDFm057q3b3SC3HUSFqzPpOPtShJny4QEkj1RdMojjJ8iScbyBXXYWD-4wl30Dde9IyeqIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: اجازۀ سوءاستفاده از شرایط جنگی و فشار بر معیشت مردم را نخواهیم داد
🔹
رئیس‌جمهور در نشست بررسی الگوی مشارکت اصناف در تنظیم بازار: یکی از سیاست‌های اساسی دولت در شرایط فعلی «کنترل مصرف و جلوگیری از شکل‌گیری تقاضای القایی و کاذب» است.
🔹
ایجاد تقاضای غیرواقعی بدون تأمین متناسب کالا، منجر به نارضایتی عمومی خواهد شد.
🔹
دولت بنا ندارد برای فعالیت اقتصادی سالم محدودیت ایجاد کند. اجازه نخواهیم داد عده‌ای با سوءاستفاده از شرایط جنگی، معیشت مردم را هدف قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/farsna/435060" target="_blank">📅 11:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae34f29f31.mp4?token=qY9S-1eDhRIP6OiJ9dun5K9qOL7iiUbRbbqGLRVrq37JfCQ5CTDgLgVrzcUG7GTv9pZz_zSCuuPQPkzXZoRwAUfeJglkGWcdkuRqQ9BVoJWjiQAM2P_HmiRIw2IuLmKGqK9jqj_9rmc3dJvpOs_AgBEomCrtGVTjlCLrVVFKfuLnYD7BP7OfwTVB1Bvaj9qmyHoOVHKkvZF81XcFIhpfpoWHozGPMpo8d_7R2kRZeKEKfFrNT7HTDwGGRS7cYuBMpGAc9TL80TQYuzfWGF7mmRXVyBvokc4x-lOdkDdzVplHZ0yQAjeTwnuJyRKsIl_3ruVIxNFLvnuN4bJXQRKpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae34f29f31.mp4?token=qY9S-1eDhRIP6OiJ9dun5K9qOL7iiUbRbbqGLRVrq37JfCQ5CTDgLgVrzcUG7GTv9pZz_zSCuuPQPkzXZoRwAUfeJglkGWcdkuRqQ9BVoJWjiQAM2P_HmiRIw2IuLmKGqK9jqj_9rmc3dJvpOs_AgBEomCrtGVTjlCLrVVFKfuLnYD7BP7OfwTVB1Bvaj9qmyHoOVHKkvZF81XcFIhpfpoWHozGPMpo8d_7R2kRZeKEKfFrNT7HTDwGGRS7cYuBMpGAc9TL80TQYuzfWGF7mmRXVyBvokc4x-lOdkDdzVplHZ0yQAjeTwnuJyRKsIl_3ruVIxNFLvnuN4bJXQRKpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران مهمان این روزهای آذربایجان‌شرقی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farsna/435059" target="_blank">📅 11:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f588c713.mp4?token=OFl2XOiqSKO_9sPyTXAG8wtro67m3nKQEPTiI6qCuxSWrDC1VsNk_p8yTIEApZOsI6MCexB5VJFdTvF8OqzpqMfMoZhcl7xoN5BpO29aknkiG0fKJy4ruJMUhchgryPeBxJmRpT3d6vmcj_5kWAJ5G9A7C95thcgGRWYjTLmxRIwUO34E_zCABeyxwYvtquBcrAOBVvETUKNggM5QHOo5oPfOSJu7O43wQkHMqdyFR2ZumC5ymmMQensdbXCE4tn_w6gQePGK1fWg7f8cZEJZbmw4oNhxxnO_fneT82yC5lO2gowC1yrS8T7um7jDLrWlqGllgiCBw-99bBCPKwACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f588c713.mp4?token=OFl2XOiqSKO_9sPyTXAG8wtro67m3nKQEPTiI6qCuxSWrDC1VsNk_p8yTIEApZOsI6MCexB5VJFdTvF8OqzpqMfMoZhcl7xoN5BpO29aknkiG0fKJy4ruJMUhchgryPeBxJmRpT3d6vmcj_5kWAJ5G9A7C95thcgGRWYjTLmxRIwUO34E_zCABeyxwYvtquBcrAOBVvETUKNggM5QHOo5oPfOSJu7O43wQkHMqdyFR2ZumC5ymmMQensdbXCE4tn_w6gQePGK1fWg7f8cZEJZbmw4oNhxxnO_fneT82yC5lO2gowC1yrS8T7um7jDLrWlqGllgiCBw-99bBCPKwACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای در جلسه با وزیر ارتباطات: مسئله‌ٔ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند: با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/435058" target="_blank">📅 11:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3750246ce.mp4?token=ZtMnplD2p0aMGNA3_19sV3JY7n5q32bKF4Su7BBAAbgF3BfALVOtXDZYGz0vGT9cbd5ULN34OoJ-ktm94wAHx-9JCaD8kzwPnLwnG5HXrkJMoVoCpmA2qYAZlZ8tGjBWX5qv-yAe6AdEIqKwi_18IKNqDkIrk6ux69QOeCT1uAU21PvCTkoEbLNM0JBJK4SYQvoCSYvcLmdfbDD3TqJYT2o2E77m5OCSWCUnVGrdHmshWabg5UZMHcsVq1wBvhuITorL1FVoQug0gBzOleV7F_VDF0DqSIhQUHo1zoH8Wyv57ot4FFjZoFsf9TjXp1IerXAPPoDcxHEY4meKGFodXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3750246ce.mp4?token=ZtMnplD2p0aMGNA3_19sV3JY7n5q32bKF4Su7BBAAbgF3BfALVOtXDZYGz0vGT9cbd5ULN34OoJ-ktm94wAHx-9JCaD8kzwPnLwnG5HXrkJMoVoCpmA2qYAZlZ8tGjBWX5qv-yAe6AdEIqKwi_18IKNqDkIrk6ux69QOeCT1uAU21PvCTkoEbLNM0JBJK4SYQvoCSYvcLmdfbDD3TqJYT2o2E77m5OCSWCUnVGrdHmshWabg5UZMHcsVq1wBvhuITorL1FVoQug0gBzOleV7F_VDF0DqSIhQUHo1zoH8Wyv57ot4FFjZoFsf9TjXp1IerXAPPoDcxHEY4meKGFodXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: در جنگ تحمیلی سوم ما ۵۰ نفر شهید ۱ تا ۵ سال داشتیم
.
@Farsna</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/435057" target="_blank">📅 11:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b106a12408.mp4?token=cahSYKxRnnWdG9uu_qwAbJxcJmpRk1mg1v5FZGFPdwCcVItXKZlqmRVUcPzcw6dkIAbqEjdqrhQIOwAroEeAYA_xXYWO3hbk0mPTirZuSeX-l87a7NAJ8zADKbJyLaVbbaN7tJoAGlMvzvKjjo1cKAUcipN2n3f_WUBX5jXqxswuTcZ-Yvaofe4kp-FxpTqqBolPHyv14VFFm4TE2PbT6H7Ai1ruMKholW7cN3R0LQepOr6e2lUsuuf51Y8bmBVfxIRiwNdh76Mz--aw74W6cYdMdIU5oVw6jrGGa1XbrogQirGtSjy-9mJIDOaIEV98wfb3qrEoU_a-gcMae2VTPa_YTZ6r-32kQQoGj1Zx_TQzHPenJ-r9X5vQG_xBGzm_zXmmBguQ6mZZYqSXr2EpsIhA6qbmg4UwKauqDKmPDckeRaM1vIl2fiHQlm0fiJzCq5eZwrVA9oFrtv5lZeemaZVqKsUgu96vqy7IoCLHv91oI-zwnPngTt96IQakfUJg9vp9-65suXWT8E00wjGPstDgLnNbvXLwaKXYhm9NTmw1UB-FU1NYjJ099GeEhWBOwjPLLKoOorjZ3gpyTFO8ZPv3xZHmRGzl0W6F1iaZsRVH3MZLb1vg9uzKOEr1bo0_iLC-u1FGrNC8IzZrqsKBYeS6H9bpBPnfNLrBI17I4yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b106a12408.mp4?token=cahSYKxRnnWdG9uu_qwAbJxcJmpRk1mg1v5FZGFPdwCcVItXKZlqmRVUcPzcw6dkIAbqEjdqrhQIOwAroEeAYA_xXYWO3hbk0mPTirZuSeX-l87a7NAJ8zADKbJyLaVbbaN7tJoAGlMvzvKjjo1cKAUcipN2n3f_WUBX5jXqxswuTcZ-Yvaofe4kp-FxpTqqBolPHyv14VFFm4TE2PbT6H7Ai1ruMKholW7cN3R0LQepOr6e2lUsuuf51Y8bmBVfxIRiwNdh76Mz--aw74W6cYdMdIU5oVw6jrGGa1XbrogQirGtSjy-9mJIDOaIEV98wfb3qrEoU_a-gcMae2VTPa_YTZ6r-32kQQoGj1Zx_TQzHPenJ-r9X5vQG_xBGzm_zXmmBguQ6mZZYqSXr2EpsIhA6qbmg4UwKauqDKmPDckeRaM1vIl2fiHQlm0fiJzCq5eZwrVA9oFrtv5lZeemaZVqKsUgu96vqy7IoCLHv91oI-zwnPngTt96IQakfUJg9vp9-65suXWT8E00wjGPstDgLnNbvXLwaKXYhm9NTmw1UB-FU1NYjJ099GeEhWBOwjPLLKoOorjZ3gpyTFO8ZPv3xZHmRGzl0W6F1iaZsRVH3MZLb1vg9uzKOEr1bo0_iLC-u1FGrNC8IzZrqsKBYeS6H9bpBPnfNLrBI17I4yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دوربین مخفی|
استخدام وزیر شعار برای تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/435056" target="_blank">📅 10:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b3f0d347.mp4?token=ZDMvAAHGN1oxFeBsOur7WSs_4cB7LVQy7g3ncbpkyB2TuJURm0vT55DCu6wQSOGz5otE7kzD2fwVjDD0j8cx6LwTO3Wg0CkCJY7eYZ2sH0RiHUJ6MFAjspkvIArpO9Pk_r4T0Q787FSG7eGBBqAD8-nHaI4OSL5Hnq4KwIOvrNvbwrO1k7hFlEikOLX8D1J9L9uTiEBSokfwH3AcHt8XJLHhrbiwY3qIxsFLR2XuobWLvDRnwmyD4LAfaQiQa8z526Dy4BwgsALijhrPN8C2s8HcT-AzSfv0JJrL1G-g_crLez5HiubJh1B79UGYrdRsysJc9ZTyiyUsgCBpU_v-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b3f0d347.mp4?token=ZDMvAAHGN1oxFeBsOur7WSs_4cB7LVQy7g3ncbpkyB2TuJURm0vT55DCu6wQSOGz5otE7kzD2fwVjDD0j8cx6LwTO3Wg0CkCJY7eYZ2sH0RiHUJ6MFAjspkvIArpO9Pk_r4T0Q787FSG7eGBBqAD8-nHaI4OSL5Hnq4KwIOvrNvbwrO1k7hFlEikOLX8D1J9L9uTiEBSokfwH3AcHt8XJLHhrbiwY3qIxsFLR2XuobWLvDRnwmyD4LAfaQiQa8z526Dy4BwgsALijhrPN8C2s8HcT-AzSfv0JJrL1G-g_crLez5HiubJh1B79UGYrdRsysJc9ZTyiyUsgCBpU_v-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستور رئیس قوه قضائیه برای پیگیری اختصاص سیمکارت‌های سفید یا اینترنت پرو به برخی افراد
🔹
حجت‌الاسلام‌والمسلمین محسنی اژه‌ای: وفق گزارشات واصله، در قضیه موسوم به اینترنت خط‌های سفید و اینترنت‌پرو، اتفاقاتی حادث شده که ضروری است دادستانی کل و سازمان بازرسی…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/435055" target="_blank">📅 10:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO-j1gB7NTt9bCmsGrhSOIeiQ2_DtvasCt_s8RIGrGh7vC_YD7wEPGdZ3-HV6Q-0uo9AxRMDilD0BcgNer_2bXl0zlXHubLH0-HnQj5IkpJ1XGpPWactxPuE6YZxMahbnCiZWblrbCnnb6Bq_PvI-L3msHW-P8qn8FzSuwSKA4hd-eYZYiimHAC4Nw2lCL-sx5VA66K00ZUV3NS0pXzEkQez73Ekqo6nX_NlGgi2t1t8qa_oLtlwZe6nIxBQpYMZLlHJLsiwmUTz7_wApptTMOgdX2B-YY3YYrUZFuVswmGsRyeQ7BCxeNR6bBWtHf2I6NVoKxi4xL-6FY7tHrYR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار ترامپ برای محاکمه خبرنگاران «خائن» در جنگ ایران
🔹
در حالی که زیر سوال بردن ادعاهای دونالد ترامپ درباره جنگ با ایران توسط رسانه‌های آمریکایی ادامه دارد، وال استریت ژورنال از فشارهای او برای محاکمه خبرنگاران خبر داد.
🔹
طبق گزارش از این روزنامه، شکایت‌ها و گلایه‌های ترامپ در مورد افشاگری‌های رسانه‌ها درباره جنگ با ایران، «تحقیقات تهاجمی وزارت دادگستری» علیه خبرنگاران را برانگیخته است.
🔹
به روایت وال استریت ژورنال، «رئیس‌جمهور ترامپ ماه گذشته به طور خصوصی از تاد بلانش دادستان کل موقت، در مورد افشاگری‌های رسانه‌ای در پی جنگ ایران شکایت کرد.»
🔹
یکی دیگر از مقامات دولت ترامپ خبر داد، رئیس‌جمهور در یک جلسه مجموعه‌ای از گزارش‌ها و مقالات خبری را که او و دیگر مقامات ارشد فکر می‌کردند امنیت ملی را تهدید می‌کند، به بلانش داد که روی آن نوشته شده بود «خیانت».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/435054" target="_blank">📅 10:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
معاون نیروی دریایی سپاه: محدودهٔ تنگهٔ هرمز برای ما بزرگ‌تر شده است
🔹
در گذشته، تنگهٔ هرمز به‌عنوان یک محدودهٔ محدود در اطراف جزایری مانند هرمز و هنگام تعریف می‌شد، اما اکنون در چارچوب طرح جدید، محدودهٔ تنگه هرمز به‌طور قابل توجهی گسترش یافته و از سواحل…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/435053" target="_blank">📅 10:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obr88e9wypWfaHEx5_IfFE6sWhTVfDOoXobBxQCOpDgbNvKoLZqcoonVLtBCAmgMC5JeBCPPomqdEqsDLj-b-FPCB0KL9I774bMD_e3J4nkmAROcNoOVqZSC_BwyifSKMiCD1ujZWxyzVWmq9qAegbgwiiQGJ0cZ6HFTFvJi_X4G3JMvFfIxP--A5myuFZaYIjdIWTETiBBrz1Zqs1Df4wiJYlyiJTXQ5C8ESjcWuYxKKM8vcmkG0-OgUIe2OrVYeX_dtL9zbTxvTMyBIn3t9updoUMaajoDT-v5zWgiHbueuX0PiCnRAVA88q5DiRq2jYUoFyPcq9ED6skmYkwowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خادمی پردیس احمدیه در حرم امام رضا(ع)
🔹
بازیگر سینما تصویری از انجام امر خادمی خود در حرم امام رضا(ع) را منتشر کرد و در صفحۀ شخصی خود تصاویری از حضور در حرم رضوی به اشتراک گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/435052" target="_blank">📅 10:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435051">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8hVy2-tzUh40_aiOyYD70QPwXDOAjJsZ6SYh2Zc4Ja6VPH31xSRMnwIrkRpYTj2YCw-mM1AgutD8SlNFXFyn5PX1vlzFefnYcNvZI76C1CNeyyi9KHRQQsousafw0TOnw7scoCmA3T6n8sEpzxpem0rAAVtQyvv9XITgY5JJwWzlfMSNweCQXa8XBK4kbXpsudwWw67LQ7xfSj03k_D4HIOQ0DUdWinSdANb6btPVYKU4GE0Z2p1RCMWUbiRex32dGx6CmBh41foXHNzQWLhYbPvX1Jv5IvDpCI_XAO_HT_WmG-MOk87peQNq6HvG3jCltNpUhlIjXchtKjHFFB1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان گزارش شبکهٔ آمریکایی دربارهٔ حضور هواپیمای ایرانی در اسلام‌آباد را رد کرد
🔹
وزارت خارجهٔ پاکستان گزارش سی‌بی‌اس نیوز دربارهٔ «استقرار هواپیماهای نظامی ایران در پایگاه هوایی نورخان» را گمراه‌کننده و جنجالی خواند و هدف از آن را تضعیف تلاش‌های جاری برای ثبات و صلح منطقه‌ای توصیف کرد.
🔹
این وزارتخانه اعلام کرد که «هواپیماهای ایران و آمریکا در طول دورهٔ آتش‌بس و مذاکرات اولیهٔ اسلام‌آباد برای انتقال پرسنل دیپلماتیک، تیم‌های امنیتی و کارکنان اداری وارد شدند و ارتباطی با هیچ وضعیت اضطراری‌ای ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/435051" target="_blank">📅 10:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435050">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMuNDn7Tpj2qO_Sh9pEivDdcSZaCN12ITs4u_fp4HXQBr_JAyA5L3HjcsQWKavsPUMtzyq0FkTaG2P3BdxLRr8uWkns9qZrfco63yjj4vRm8DxVGcWL463AFx9mmXM4dQWqvMCHGeTM4BQ8V2cWaKwM1jGf_-7RNdqAQ9r0Ng_nwHfgbyiKrnxyjF_uMXMeDCkJyIpSPNQ2dlAKLIjyVUL_AHUyy0H2vRoazaDyJssFg-ivXdXTswh5TQLoeS6U88IJaMamB225iMoLBv5NxTAyct6wChgoxIswHOh-QS_L5CImsAQl5gVIWBAHMY3bOwpyeU83s6QH_ZpVOnGwagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی بن گویر کنار کیکی که بوی مرگ می‌دهد!
🔹
تصویری که به تازگی در شبکه‌های اجتماعی منتشر شده، چهره وحشیانه کابینه رژیم صهیونیستی را بیش از پیش نمایان کرده است.
🔹
در این تصویر، کیک تولد ایتامار بن گویر، وزیر امنیت داخلی رژیم صهیونیستی، با یک طناب دار تزئین…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/435050" target="_blank">📅 10:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435049">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
زخمی‌شدن ۸ نظامی صهیونیست در درگیری با حزب‌الله
🔹
رادیو ارتش اسرائیل خبر داد که در ۳ درگیری بین نظامیان اشغالگر با نیروهای حزب‌الله در اطراف روستای «زوطر» ۸ نظامی زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/435049" target="_blank">📅 10:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
معاون نیروی دریایی سپاه: محدودهٔ تنگهٔ هرمز برای ما بزرگ‌تر شده است
🔹
در گذشته، تنگهٔ هرمز به‌عنوان یک محدودهٔ محدود در اطراف جزایری مانند هرمز و هنگام تعریف می‌شد، اما اکنون در چارچوب طرح جدید، محدودهٔ تنگه هرمز به‌طور قابل توجهی گسترش یافته و از سواحل جاسک و سیری تا فراتر از جزایر بزرگ، به‌عنوان یک پهنه راهبردی تعریف شده است.
🔹
به‌عبارت دیگر، تنگه هرمز بزرگ‌تر شده و به یک منطقه وسیع عملیاتی تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/435048" target="_blank">📅 10:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435046">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52478a45c6.mp4?token=JCfUUtbIpF3qg_6O-t3g9EDqRVb5MlEuQp2oWqultowCQjCPBYTWFAqr3eTdsyWBODEY-r2KOei6vYhZIp9rAuxuFA99X3uqyk5L7NMU313DdVwScNeoYhQ6LZbGxEFs20sXcRLE51IptHq5Czh8ZQ9fT_hDAOjyy0ZQAnX15B53RJJneN3Wufi2jk03HQyhs1yd2Lf-3aTQZBxmmK4Yu22F-BIQOrZLiCjJsMJodvya-6z8IJSDoyD0dKszlFxebAJRxU-fPK4BJH7O-kxVZg-5MImkUR5L1v4GPibJKXWjbBqaTeMkrf7m8Nwh7eFWYvyghfN6wPACA1bKJlcZZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52478a45c6.mp4?token=JCfUUtbIpF3qg_6O-t3g9EDqRVb5MlEuQp2oWqultowCQjCPBYTWFAqr3eTdsyWBODEY-r2KOei6vYhZIp9rAuxuFA99X3uqyk5L7NMU313DdVwScNeoYhQ6LZbGxEFs20sXcRLE51IptHq5Czh8ZQ9fT_hDAOjyy0ZQAnX15B53RJJneN3Wufi2jk03HQyhs1yd2Lf-3aTQZBxmmK4Yu22F-BIQOrZLiCjJsMJodvya-6z8IJSDoyD0dKszlFxebAJRxU-fPK4BJH7O-kxVZg-5MImkUR5L1v4GPibJKXWjbBqaTeMkrf7m8Nwh7eFWYvyghfN6wPACA1bKJlcZZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار نارنجی؛ به حریم و بستر رودخانه‌ها نزدیک نشوید
!
@Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/435046" target="_blank">📅 09:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435044">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تروریست آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اعدام شد
🔹
رئیس دادگستری سیستان‌وبلوچستان: بامداد امروز حکم اعدام عبدالجلیل شه‌بخش فرزند جلال، عنصر آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اجرا شد.
🔹
در پی بازداشت عبدالجلیل شه‌بخش در جریان اقدامات ضدتروریستی در شرق کشور، پرونده‌ای علیه وی تشکیل و دادسرا او را با عناوین اتهامی بغی از طریق حمله مسلحانه به مقر‌های انتظامی و عضویت در گروه باغی انصارالفرقان به دادگاه انقلاب معرفی کرد.
🔹
نظر به بررسی دقیق پرونده در مراحل دادسرا و دادگاه و وجود مدارک و مستندات متقن استخراج شده از وسایل ارتباطی و فایل‌های صوتی متهم و همچنین اقاریر صریح وی در مراحل مختلف بازجویی و بازپرسی؛ سرانجام با ابرام حکم وی در دیوان عالی کشور، حکم اعدام این عنصر تروریست بامداد امروز اجرا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/435044" target="_blank">📅 08:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435043">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b971bed600.mp4?token=QpBjaYYvHEynAAH3vI_vTXfNT-_xdJLleTkbUSYk60iiRTglJIwcnNuvIzOdbnBzlEi94UT2rlE6crFDoYNScm8dseILZ6qujJolQTF7b3ePIxbGhJWJunxOdUeVHixQ6Ha5VXjP3pHxmAnjJqUca9pvjN8uva1qNToNULAXx_AcKvzXLNsQJpIHirXBxH3uYEe36NrS34SAaIakVcaBjEhQXcneydf_cn9RQXqveweGPXxbl5VVFoYx3OQw9lAkdtaDH9C4ThBE1KtP3Qs7cy0fT3irVluAFRh_S58Lq5hGFOSkeBJGHBLhx3kG_szbh8cTqIrc-lTh_9cbZZetzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b971bed600.mp4?token=QpBjaYYvHEynAAH3vI_vTXfNT-_xdJLleTkbUSYk60iiRTglJIwcnNuvIzOdbnBzlEi94UT2rlE6crFDoYNScm8dseILZ6qujJolQTF7b3ePIxbGhJWJunxOdUeVHixQ6Ha5VXjP3pHxmAnjJqUca9pvjN8uva1qNToNULAXx_AcKvzXLNsQJpIHirXBxH3uYEe36NrS34SAaIakVcaBjEhQXcneydf_cn9RQXqveweGPXxbl5VVFoYx3OQw9lAkdtaDH9C4ThBE1KtP3Qs7cy0fT3irVluAFRh_S58Lq5hGFOSkeBJGHBLhx3kG_szbh8cTqIrc-lTh_9cbZZetzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صادرات فلفل دلمه به روسیه آزاد شد
🔹
رئیس اتحادیه ملی محصولات کشاورزی ایران: ممنوعیت صادرات فلفل دلمه به روسیه برداشته شد و صادرات به این کشور از روز شنبه از سرگرفته می‌شود.
🔹
کسانی که می‌خواهند این محصول را به روسیه صادر کنند با سازمان حفظ نباتات هماهنگ کرده…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/435043" target="_blank">📅 08:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435042">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e57f4c1545.mp4?token=XvAr5zNY-45rs28tPyGeDFMdNvHIYTG0STuJU40UAlUtWKjWFshL2t3Yc32-OYg8310GoBOO2cb0_MGDP4msCYAjYLXMvmOPHsdMRl2bv0rZKSjTVWg-pIFcwMz86m34etQEgxT7KGyyBT4YvXLoZ6w-MLHgtkuZNC0nzDqloCFWbuqIkB7EP_RSNrjeCzqC9mpjbDgNQRpupIlNYBlPDCnwVlwtZcxiTtY3rkMUz6-M-pDSsxFIyXCx8n-qS6EjZJ2f0mxpXXqa_MhpH0RAcsXiJPaWvwqJYadH_CMlyQyB_tD_r5mEfnDAAEbWzLi-Dx52xTuB-9VETqHbyRfVgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e57f4c1545.mp4?token=XvAr5zNY-45rs28tPyGeDFMdNvHIYTG0STuJU40UAlUtWKjWFshL2t3Yc32-OYg8310GoBOO2cb0_MGDP4msCYAjYLXMvmOPHsdMRl2bv0rZKSjTVWg-pIFcwMz86m34etQEgxT7KGyyBT4YvXLoZ6w-MLHgtkuZNC0nzDqloCFWbuqIkB7EP_RSNrjeCzqC9mpjbDgNQRpupIlNYBlPDCnwVlwtZcxiTtY3rkMUz6-M-pDSsxFIyXCx8n-qS6EjZJ2f0mxpXXqa_MhpH0RAcsXiJPaWvwqJYadH_CMlyQyB_tD_r5mEfnDAAEbWzLi-Dx52xTuB-9VETqHbyRfVgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم بزرگداشت رهبر شهید انقلاب در ایالت پیشاور پاکستان
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/435042" target="_blank">📅 08:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435041">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فایننشال‌تایمز: قیمت کودهای نیتروژنه که بخش عمده‌ای از آن در خاورمیانه تولید می‌شود، از زمان آغاز جنگ با ایران بیش از ۳۰ درصد افزایش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/435041" target="_blank">📅 08:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435040">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa2fc8c8e.mp4?token=MmQHHv4e68cddvHWJQKcGWLeL25NPy7Jp7qsQ5h5515ujcS0zHT2HdjjxAUEfFhN-H_4AGiFxsgoptIXcOAWDq4dWphhvbxn3qZ1qrE0p025r1Hqqb-svtYrdBoD_73Kpe46jtfNxAhNVBYlHnN8kc1w-iyJogG3Fxu4mhJydn6f-NlKW16FThlINBhYjEv4iYAiUOMwRAW45wucO0qQgfKOlFrtG5X2L7czFffD96bdSZa8O-l1tPvOuHMJ1OQ71jLBHuxmu_61a0D06D0fnI-on_SxeNgYbjiLi4evWthq42ambgU2YJgzXpN_PFOcxxz0gGCZ70EWPmpT5fwaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa2fc8c8e.mp4?token=MmQHHv4e68cddvHWJQKcGWLeL25NPy7Jp7qsQ5h5515ujcS0zHT2HdjjxAUEfFhN-H_4AGiFxsgoptIXcOAWDq4dWphhvbxn3qZ1qrE0p025r1Hqqb-svtYrdBoD_73Kpe46jtfNxAhNVBYlHnN8kc1w-iyJogG3Fxu4mhJydn6f-NlKW16FThlINBhYjEv4iYAiUOMwRAW45wucO0qQgfKOlFrtG5X2L7czFffD96bdSZa8O-l1tPvOuHMJ1OQ71jLBHuxmu_61a0D06D0fnI-on_SxeNgYbjiLi4evWthq42ambgU2YJgzXpN_PFOcxxz0gGCZ70EWPmpT5fwaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانواده‌ای که به‌خاطر نماهنگ «باید برخاست» از آلمان برگشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/435040" target="_blank">📅 07:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435039">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیش‌بینی رگبار باران و رعدوبرق در ۱۴ استان
🔹
هواشناسی: امروز سه‌شنبه در برخی نقاط آذربایجان شرقی، آذربایجان غربی، اردبیل، گیلان، کردستان، کرمانشاه، زنجان، قزوین، همدان، مرکزی، البرز و برخی مناطق در استان کرمان و شمال خراسان رضوی، رگبار باران، رعدوبرق، وزش باد شدید موقت و در مناطق مستعد تگرگ پیش‌بینی می‌شود.
🔹
امروز آسمان تهران کمی ابری، از بعدازظهر افزایش ابر، افزایش باد و احتمال رگبار و رعدوبرق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/435039" target="_blank">📅 07:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435038">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">در نمایشگاه کتاب امسال، کتاب ۲ میلیون تومانی را ۵۰۰ هزار تومان ارزان‌تر بخرید
🔹
به گفتۀ قائم مقام نمایشگاه بین‌المللی کتاب، امسال کتاب‌های ناشران داخلی تا سقف ۲ میلیون تومان با ۲۵ درصد تخفیف پشت جلد به مخاطبان عرضه می‌شود. یعنی یک کتاب ۲ میلیون تومانی را می‌توان به مبلغ ۱ میلیون و ۵۰۰ هزار تومان خریداری کرد.
🔹
در خریدهای بالاتر، ۱۵ درصد تخفیف بر مازاد ۲ میلیون تومان اعمال می‌شود؛ به این صورت که جدای از دومیلیون تومان که شامل ۲۵ درصد تخفیف شده، الباقی مبلغ نیز با تخفیف ۱۵ درصدی محاسبه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/435038" target="_blank">📅 07:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435037">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy7Qrm5udV04iQYTCD7LnLBDVOMxBdw_4lg9ejPzxgKhTjDVrez8CBgE9yiBJftWpQ_nyRO6amnS-xrIpTsE_xp9TymJUwnbYiGN7DjqHPXi-o5jFyU6eUbGMVLok5IV9JLw8wa0Rz-dqPat4361SxP00_LOG9khanhncz74OGDO8Z8iiMBk-vtsj_zwdm98c4W-fuRBK8tCKd_Ali-RRc7zIzce9-ojE1rwyUSsALT3sts-5ApTuTxjZP4oxuJcILD0Vn5FrUZy_hQ7HZHbpjub3K7wZlLoD5RhJPQRe-JsnoCQxD_uCWeac3i9myzpSbzTZKMEF_hdfiRHRgXpgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴۰ روز هوای خوب سهم تهرانی‌ها در سال جاری
🔹
۵۲ روز از شروع سال ۱۴۰۵ گذشت و تهران از ابتدای سال جاری تاکنون ۴۰ روز هوای قابل قبول، ۱۱ روز در وضعیت پاک و یک روز در وضعیت ناسالم برای گروه‌های حساس بوده است.
🔹
در مقایسه با مدت مشابه سال گذشته، تعداد روزهای قابل‌قبول یکسان و تعداد روزهای پاک ۵ روز افزایش داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/435037" target="_blank">📅 06:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435036">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سامانۀ گزارش مردمی گران‌فروشی، احتکار و اخلال در توزیع کالای اساسی راه‌اندازی شد
🔹
دادستانی کل کشور: با هدف دریافت گزارش‌های مردمی دربارۀ تخلفات اقتصادی از جمله گران‌فروشی، احتکار عمده و هرگونه اخلال در تأمین و توزیع کالا‌های اساسی، سامانه‌ای به نشانی
dadsetani.ir/ehtekar
ایجاد شد.
🔹
شهروندان می‌توانند گزارش‌ها و مستندات خود را دربارۀ موارد تخلف از طریق این بستر ثبت کنند.
🔹
دادستان‌های سراسر کشور موظفند در چارچوب قانون و با بهره‌گیری از گزارش‌های دریافتی، با اخلال‌گران در امر تأمین و توزیع مایحتاج عمومی با قاطعیت و سرعت برخورد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/435036" target="_blank">📅 06:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435035">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHDJRynCygRVr9nfW6v7SnxpnIizZE82KJHBosD8RvpmVjzsobXSb-AiSYz_2k29xHzjYKFCJlQ9hxujPFrE6_z5Wxi_Kx6ncWPigmDhPMvawAnDo2D88A4-SHEqzG9cN-rVQK56Amu6LQnkAXS4WdAwT4nY9J_uan9Bs3q8OLSkgQOk71HUA37CPNOqAxZ0zdiZb1lNcbK1WKKssZCITx6Ee5LNP_i5J4cDlxwlbLPdaiuZbPwjOCkB5Afna4HieeT5vNgTITU-Q3DPdOJfORSPp9uBGBKtqK4PhPzS3Y7BVdSAZe5jzPpo3NLQpGzAHiUriZOGHatEB1t7Y677fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: صبر ترامپ از بسته‌بودن تنگۀ هرمز تمام شده است
🔹
شبکۀ سی‌ان‌ان به نقل از منابع مطلع در دولت آمریکا: تندروهای دولت ترامپ برای حمله به ایران فشار می‌آورند.
🔹
دونالد ترامپ در مقایسه با هفته‌های گذشته، به‌صورت جدی‌تری ازسرگیری عملیات نظامی علیه ایران را بررسی می‌کند. صبر او از ادامۀ بسته بودن تنگۀ هرمز تمام‌ شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/435035" target="_blank">📅 06:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435034">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
از برگ‌های سبز در مزارع مازندران، تا چای خوش طعم ایرانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/435034" target="_blank">📅 05:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435033">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">مقام حماس: جنایات اسرائیل در غزه هنوز ادامه دارد
🔹
«طاهر النونو» مشاور رسانه‌ای رئیس دفتر سیاسی حماس شامگاه دوشنبه گفت که اشغالگران به تاکتیک‌های کشتار و گرسنگی در نوار غزه ادامه می‌دهند که ادامه جنگ در مقیاس کوچکتر است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/435033" target="_blank">📅 05:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435031">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
سنگ‌تمام آملی‌ها در میدان دفاع از ایران
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/435031" target="_blank">📅 05:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435030">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6pqoMPQ7JTpEQZINeA3lalxk2QRMApEDocHO-JGfkiXwjpJxe3MuvSA3jLyaXKI9uNQeFa1s_qCIKNORNfumeWmameAQcnLlVDmIb2A2A83r5ycqb9B7uSjnqiBkBPE8Z_OAZpDUJ68bOTmbxPUpIrFWeCYQkc4HwKggp4Fz6EU6CKcNo4NPaj1IrvzRF0eVH5dm5FmFUkITGEvyANMkzyBcwyAo1WYvr35XyaoPnKWV9m7YIkx9VL-JGaYkTUjkXOpq_oVAcMQ8OnImW3fEUV4-2GXNm5tWhBrNa6LGtASoaF-mPVkOyEQXGIdn7WtRufcvY7-draxr4O28M-Yfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد ۶ سالۀ دریاچۀ ارومیه شکسته شد
🔹
آمار و ارقام مربوط به دریاچۀ ارومیه نشان می‌دهد این پهنۀ آبی پس از افزایش حجم آب، حال رکوردهای جدیدی را ثبت کرده است.
🔹
به گفتۀ استاندار آذربایجان‌غربی، اکنون تراز دریاچه به ۱۲۷۱ متر رسیده که طی ۶ سال گذشته بی‌سابقه بوده و امید به احیای این پهنۀ آبی را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/435030" target="_blank">📅 04:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435029">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
شما هم طرفدار استقلال هستید؟
@Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/435029" target="_blank">📅 04:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">روایت رحیم‌پور ازغدی از ۳ شگفتی که محاسبات دشمن را در جنگ بهم زد
🔹
عضو شورای‌عالی انقلاب‌فرهنگی: در جریان سفرهای اخیر مقامات کشورمان به روسیه و چین، عالی‌ترین مقامات این دو کشور گفتند تهاجم اخیر به ایران، بزرگ‌ترین لشکرکشی تاریخ پس از جنگ جهانی دوم بوده، و دشمنان مطمئن بودند که با این حجم از حمله، هر کشوری باشد ظرف یک یا دو روز سقوط کرده یا تسلیم می‌شود.
🔹
آن‌ها اذعان کردند که سه اتفاق شگفت‌انگیز در ایران رخ داد که هیچ‌کس در دنیا آن را باور نمی‌کرد و نشان داد که هیچ ملتی در جهان شبیه ملت ایران نیست.
🔸
شگفتی اول؛ هر ملت دیگری به‌جای ایرانیان بود، پیش از آغاز بمباران فرار می‌کرد و سیل مهاجرت به راه می‌افتاد. اما مردم ایران در اوج بمباران و با وجود تمام مشکلات اقتصادی، نه‌تنها خانه‌ها را ترک نکردند بلکه در خیابان‌ها حاضر شدند.
🔸
شگفتی دوم، حفظ ساختار و اقتدار نظامی کشور بود. هیچ‌کس باور نمی‌کرد پس از شهادت رهبر و فرماندهان کشور، نیروهای رزمی بدون ازهم‌پاشیدگی، باقدرت و صلابت به جنگ ادامه دهند؛ گویی که هیچ اتفاقی رخ نداده است.
🔸
اما شگفتی سوم به رهبر انقلاب در اوج تهدیدات برمی‌گردد. برخلاف رهبران جهان که در زمان جنگ به امن‌ترین مکان‌ها منتقل می‌شوند، ایشان پیشنهاد مکرر مسئولان حفاظت برای انتقال به پناهگاه را با یک جمله تاریخی رد کردند: «پس مردم چه؟ مردم کجا بروند؟»
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/435028" target="_blank">📅 03:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DosNCUDgiifJ1xMp7a7wdFJgoWKf8Y1NVMZfRFeIQ9FgkWW-vpZY_XEAw-Y48h1dRSmHcP9SkN9WbOliSDo-2axYYt8MpSJehUkwDieRPjTE3LmQD7gvp_qXM2TSCsdaOBuNj_1C7gYNJl0frFRxMX0TXVTPyVF_nZ3BmGsTB6b4AWOWxPL9cMfJUh1DEIMtMKs4wmZLehYB5qlC9V0z9NrkolkDjZB8zK-NuNFc-KI_-gUPXmnPg7y0epNkcXmGJjzgWLO8-ytEYAFDFmXxvO_Fvirb4BZarWB3ryNBmq9nXigJsR2Y0AU4ejn0vkcUFRS-VGjrvlPanEjFwArbQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف خط لولۀ ۶ کیلومتری انتقال سوخت قاچاق در بندرعباس
🔹
جانشین پایگاه دریابانی بندرعباس از شناسایی و انهدام خط لولۀ انتقال سوخت قاچاق به طول ۶ کیلومتر خبر داد.
🔹
قاچاقچیان این خطوط لوله را زیر ماسه‌ها و آب دریا جاسازی کرده بودند و از آن طریق، سوخت را از ساحل به دریا و شناورهای متخلف انتقال می‌دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/435027" target="_blank">📅 03:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435025">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای ترامپ درباره احتمال بازگشت به عملیات نظامی در تنگه هرمز
🔹
رئیس جمهور آمریکا در مصاحبه با شبکه «سی‌بی‌اس» ضمن تهدید به انجام اقدامات «بسیار شدیدتر» علیه ایران، مدعی شد که واشنگتن ممکن است به زودی عملیات نظامی در تنگه هرمز را از سر بگیرد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/435025" target="_blank">📅 03:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435024">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29818c4e2b.mp4?token=aZ9iMUJHTp2Ub6HjWGOaH0ENCMN7JoXMu-J8ep_5PZGk4Rdgl30TVc6MLRN4L1pWyAfOdGs0pPdfuhFI2FzpjvLC7vk4Jx8XJrgMgxeeg09QZSLzsoQ2oNO4J8jHBX_pS5Mb7NWdSFELYpJem2ix70dWocc50esbUEdyPxaJgFNMt7iJaxjhvcydy7yzQdWYT3SVHrBnd6Vga2L_E9iQWvfJHe5LnfNGdZs-TKWRCDQEJqTvDom802N6zVWB3nS1qwgPxBlHEFS67JPoDeXGLyw0TZ-dCY7TfQy9CMp-hAlvo9i2k0mLeV23lQuTv3_VBmkySe0znSwBqVZqKWzkoqOvvjBgsT3BZPLekQ6Qjo1YNyvwTgKVEYsG43V-cwzROkoJ7YnMDIBaBlPKkpZp2N77sRpF9v02MnzGUzqnPr0omiHBaGyuxsIe-pVSWtBT4DmmJdMiQDxbJ3M8qsurxQPViuKovbyZsN-Qj1vpZxODrf7Q2v2p9xPLMEzJeW4TcSbmT52Tx7cwHWLvXCMt_shVoKH2OFiDGlL53R9J4_bwy6yYPnifPNuPrenEroGgoUnxZvbdkVnIZO1I7IhVdE7AbdP8cxz07kA6E8FE-yRWQLeLtUL7rDI7IsW30lY5tcE9-wnr2I1pq14zytMk8Pw_mQ5Fpe5h_0fwxN8ndpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29818c4e2b.mp4?token=aZ9iMUJHTp2Ub6HjWGOaH0ENCMN7JoXMu-J8ep_5PZGk4Rdgl30TVc6MLRN4L1pWyAfOdGs0pPdfuhFI2FzpjvLC7vk4Jx8XJrgMgxeeg09QZSLzsoQ2oNO4J8jHBX_pS5Mb7NWdSFELYpJem2ix70dWocc50esbUEdyPxaJgFNMt7iJaxjhvcydy7yzQdWYT3SVHrBnd6Vga2L_E9iQWvfJHe5LnfNGdZs-TKWRCDQEJqTvDom802N6zVWB3nS1qwgPxBlHEFS67JPoDeXGLyw0TZ-dCY7TfQy9CMp-hAlvo9i2k0mLeV23lQuTv3_VBmkySe0znSwBqVZqKWzkoqOvvjBgsT3BZPLekQ6Qjo1YNyvwTgKVEYsG43V-cwzROkoJ7YnMDIBaBlPKkpZp2N77sRpF9v02MnzGUzqnPr0omiHBaGyuxsIe-pVSWtBT4DmmJdMiQDxbJ3M8qsurxQPViuKovbyZsN-Qj1vpZxODrf7Q2v2p9xPLMEzJeW4TcSbmT52Tx7cwHWLvXCMt_shVoKH2OFiDGlL53R9J4_bwy6yYPnifPNuPrenEroGgoUnxZvbdkVnIZO1I7IhVdE7AbdP8cxz07kA6E8FE-yRWQLeLtUL7rDI7IsW30lY5tcE9-wnr2I1pq14zytMk8Pw_mQ5Fpe5h_0fwxN8ndpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ساعت از ۳ بامداد گذشته، و هم‌چنان حماسه‌سازی مردم تهران ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/435024" target="_blank">📅 03:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435023">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
فایننشال‌تایمز: گرانی بنزینِ ناشی از جنگ با ایران، ۳۵ میلیارد دلار به مردم آمریکا خسارت زده است
🔸
براساس داده‌های دانشکده امور عمومی «واتسون» در دانشگاه براون، مصرف‌کنندگان آمریکایی تا روز جمعه، بالغ بر ۳۵ میلیارد دلار هزینه اضافی برای بنزین و گازوئیل…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/435023" target="_blank">📅 03:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435022">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تکلیف نحوۀ امتحانات نهایی ۲ ماه دیگر روشن می‌شود
🔹
در حالی که پیش‌تر احتمال برگزاری دومرحله‌ای امتحانات نهایی شامل داخلی مجازی و حضوری کشوری مطرح شده بود، حالا وزیر آموزش‌وپرورش اعلام کرد «تا ۱۵ تیر برای مشخص‌شدن وضعیت امتحانات نهایی صبر می‌کنیم.»
🔹
به گفتۀ کاظمی، برگزاری ۲ آزمون موجب افزایش فشارهای روحی و روانی به دانش‌آموزان می‌شود و ترجیح این است که یک مرحله آزمون بعد از اطمینان از وضعیت کشور و پس از فرصت کافی به دانش‌آموزان برگزار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/435022" target="_blank">📅 02:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435021">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgepcaQT_S0IIKdtlt3XGVQARAHUvMQEp8Wq2369LfN3eJVwLoWOtexEj96uPjkzXMwuYd0me8YgIHY3q8r209nXKCTvtE8qHNgdfEl50mWuuo7dFOF551Nrlm4lA-z3cbh-yAE-BWg3LFl7K5kJaLayzpQvrwI9iI2wojRbDig5RPJt6SIrgp5Fr6LW6eSIo7VGBBYVZHqzdO41rl7dUP4qVMM_zK6t5fJVv9KWPAO7owg1XaXqeYJPrnl4H5tfLle_8mRd2USkz3ZsoBxFUw5-oBoMWx43mCO0Uxz89tsc0i8LT6BCdp9V1INBF8K503Hvc8agLEEMpdIAS4d2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۶ درصد آمریکایی‌ها از توجیهات ترامپ برای جنگ با ایران ناراضی‌اند
🔹
نظرسنجی جدید در آمریکا نشان می‌دهد که ۶۶ درصد مردم این کشور از نحوۀ توضیح رئیس‌جمهور خود دربارۀ تحمیل جنگ بر ایران ناراضی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/435021" target="_blank">📅 02:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عراق وجود پایگاه اسرائیل در این کشور را تکذیب کرد
🔹
فرماندهی عملیات مشترک عراق در بیانیه‌ای اعلام کرد: ما تأیید و تأکید می‌کنیم که در حال حاضر هیچ نیرو یا پایگاه نظامی غیرمجاز در خاک عراق وجود ندارد.
🔹
نیروهای ما در ماه مارس با گروه‌های ناشناس و غیرمجاز که دارای پشتیبانی هوایی بودند، در صحرای کربلا درگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/435020" target="_blank">📅 02:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c457c0ab.mp4?token=aNH9KH5dicNeY6w4CFtC8CYdpkmlTG2pBwu7wnX__uDHPHoQsX5SxM7xDfBHPeFLg2yFYEcYtS3zjxNLuJk9OSkb2ufza6O3Xv7VRVuE-QmMe_2gtGJ59pCe5fXJEWE9i2kwp9d5Li2llX2BP7akv1ZJqxLQ3Miy4grzSJB-fdPKreR1BtzQ0l7TIf7AfmTZCqgdtIwKtdxoYfjnd9KcSUxL66SGNb4jSqtjXJh__GRO1XeoS3rI1_by5zJsENHQH-dq1TiC4dHRrBZwsEriDEGKXg0nmUFksS_WSgzf2tJIgQB4weuRfDY-iD3Qs49rfPQksJpchVFwFw5Xq1yO-4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c457c0ab.mp4?token=aNH9KH5dicNeY6w4CFtC8CYdpkmlTG2pBwu7wnX__uDHPHoQsX5SxM7xDfBHPeFLg2yFYEcYtS3zjxNLuJk9OSkb2ufza6O3Xv7VRVuE-QmMe_2gtGJ59pCe5fXJEWE9i2kwp9d5Li2llX2BP7akv1ZJqxLQ3Miy4grzSJB-fdPKreR1BtzQ0l7TIf7AfmTZCqgdtIwKtdxoYfjnd9KcSUxL66SGNb4jSqtjXJh__GRO1XeoS3rI1_by5zJsENHQH-dq1TiC4dHRrBZwsEriDEGKXg0nmUFksS_WSgzf2tJIgQB4weuRfDY-iD3Qs49rfPQksJpchVFwFw5Xq1yO-4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل خروشان اهوازی‌ها در شب هفتاد‌ودوم
@Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/435019" target="_blank">📅 02:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSHY5wCyJnOrfx4NgCNmvCSloQdry6q90TBxWJyqPKZTaOaW8_akWMANa3A71sqFzteP9xoUtgXQKl1lrfXlPwjqel6xw9AhA6c_G_WE176CfsEmwvnKB98sCz0J72qTiLq4A-tENitXaVEBFzibLgW9UuorBi1JzDgI7Rrsd3MDJ9TpJYRSdyWKmrAVnw5ozMpKk03KYl3Drz0uOFaFbt9rCWHKOg1ZUoWqiX3OuB62DKtOL0JMb-lWtoOGpyMA8_P4Ri0IlgKYqfwKqg12Bv-wb7azckDRArDgCQ9cL0DdsBmzRzBnf0um_J49NSF_6a9KaFr0sdoxkkLIGApeDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر دموکرات‌های سنای آمریکا: برای هفتمین‌بار، طرح محدود کردن اختیارات جنگی ترامپ و پایان دادن جنگ ایران به رأی گذاشته می‌شود.
🔹
چاک شومر: تکرار می‌کنم، ترامپ آمریکا را به یک جنگ غیرقانونی، پرهزینه و بدون هیچ هدف و هیچ پایانی کشاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/435018" target="_blank">📅 02:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435017">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bede6129.mp4?token=bg8I9NTGwdbbKi6aKoo1iRPivON3AqAyZouTdsCjFHVzEHDkJ5-7T87T852Hbmly9xOnMzdE8ES8MWG0pxNbmUjX3eYcEacvGV-6P8O0OJxD2AF3G7p6PPfLmvtnbFnt4lwZEd5jl8NvwqUZKhClUH6ovoAGbw4p6q6W3h1SevIBb5VLd0mHVODq7r_jXVn1gI-eK6wrfXJuJYGABRFpEVuAQFGQPctzdVOG0-1QN65UZeba4-Z9pbWicKkxdPKZZxFeuRWXPI9Fzuk9wAVgJMQF4JGrOiMpqE2QHyrAOZhF_OT8wmTq6h1cTJ4orrjOohicTVEbn_Z4jIDeGtxA0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bede6129.mp4?token=bg8I9NTGwdbbKi6aKoo1iRPivON3AqAyZouTdsCjFHVzEHDkJ5-7T87T852Hbmly9xOnMzdE8ES8MWG0pxNbmUjX3eYcEacvGV-6P8O0OJxD2AF3G7p6PPfLmvtnbFnt4lwZEd5jl8NvwqUZKhClUH6ovoAGbw4p6q6W3h1SevIBb5VLd0mHVODq7r_jXVn1gI-eK6wrfXJuJYGABRFpEVuAQFGQPctzdVOG0-1QN65UZeba4-Z9pbWicKkxdPKZZxFeuRWXPI9Fzuk9wAVgJMQF4JGrOiMpqE2QHyrAOZhF_OT8wmTq6h1cTJ4orrjOohicTVEbn_Z4jIDeGtxA0Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نشریهٔ آتلانتیک: واشنگتن نمی‌تواند پیامد‌های باخت در جنگ با ایران را کنترل کند
@Farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/435017" target="_blank">📅 02:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">افزایش حقوق بازنشستگان تأمین اجتماعی امروز تعیین تکلیف می‌شود
🔹
خبرنگار فارس کسب اطلاع کرد، تکلیف افزایش حقوق و زمان پرداخت ۳۰ درصد باقیماندۀ همسان‌سازی بازنشستگان تأمین اجتماعی در سال ۱۴۰۵، احتمالا در نشست مشترک سه‌شنبۀ مدیران سازمان و نمایندگان کانون‌ها نهایی می‌شود.
🔹
افزایش حقوق سال ۱۴۰۵ قرار است بر مبنای مصوبات شورای‌عالی کار، و برای حداقل‌بگیران افزایش ۶۰ درصدی و برای سایر سطوح افزایش ۴۵ درصدی در نظر گرفته شود.
🔹
بازنگری در مزایای جانبی شامل حق مسکن، حق عائله‌مندی، حق اولاد و حق معیشت نیز متناسب با نرخ تورم و رشد هزینه‌های زندگی در دستور کار قرار دارد.
🔸
بر اساس قانون مصوب مجلس، همسان‌سازی باید تا سقف ۹۰ درصد اجرا شود که ۶۰ درصد آن در دو سال گذشته اعمال شده و ۳۰ درصد باقیمانده اکنون نیازمند تصمیم‌گیری نهایی است تا این فرآیند تکمیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435016" target="_blank">📅 01:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
هشدار جی‌پی مورگان: ذخایر نفت جهان تا نیمهٔ خرداد بحرانی می‌شود
🔹
بانک جی‌پی مورگان: ذخایر نفت کشورهای توسعه‌یافته تا اوایل ژوئن (نیمهٔ خرداد) به «سطح تنش عملیاتی» می‌رسد. در این وضعیت توانایی جهان برای جبران کمبود عرضهٔ خاورمیانه از طریق برداشت از مخازن ذخیره به‌شدت محدود خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435015" target="_blank">📅 01:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435008">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBD0NtkhkcT3HHFZb6e9WUYW33VKe8nMPOzy21UiyIiVs06GbR7fhr26LBJiEL5rGR_GIHmkbNLd8CIhL3o5j4s4tRgemRwc1vn8Vuwl8loHjcW-Oa11pOtvyCm9FpXpn7YD1zGlPOdQPH_xBzpMtsWxVY_qMNDGR20wJvX3DP-bg8EhJ8QC6Qv9g_a2Y5pgtXjN3S0gKqxFOGaFIk0OnYO3SLG6ME1GXevZc5tyN4QPU9Uun7oNmfxIpMd7T30c89Y0m3aLDmGhRrgd1GAKZodQR_y_4r98IOF7a1PGvL7IjwIZsdGumnDcK8YM9OMijrCl4Ygd_7-Xpv5Rku9xbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRsBrGeJ58pu-YgD_aQ6AgMJZcA4oz0oExrk_vIuNqJohqMhiTMwSjH0kbUqJrEE1IzD0AB3k1jti0hkR_vtKPlqtw2RGn8SjVKDsdZC4FmHet66AQLoBew1YA-S-Oq_lwoJ41StvMsnkiITSfcHeJsD62fglU2i8j4xEqayaYCc_LdR1QUs8FxWqoFFV9y2ByjAJLnmxY0-hqmkW5IEueY2gkDUzcugnaBHxwCoXcHLM-Ll6qtBzEs1JyI5u5nauXH2FRkNpUcWbXU2_GpoBB2nUuLOH7nsR--jMGLhExdDlZrWjvPaC5zelYo8lhanUsHIrFbPIJ9Wbh6nCQ7UMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YhEhVVlvuWgx4CiYULyCwSJoHTnc3Sa9JevTbKaIsKyNXq5YjB4JXP1k7hJ7yUxzmSzUo_eOn_Zr830Tu6NMhUxgsV0SqpGsLNuFuPfoXzPpcCmg_Lc5aDI5bYm1Zh3GSSYTYM30vEi42C705xWRv3QksRb6FFphLwAlIkyrFciAGrjwY1WNQaGk8OLNFGZh0GPHAd85c3M9uuLZV8_p_w0O3FhRFDFEj3lmlseJHyCWmGH0yjybL4W4f-8tObW3VRwXz9Qu4K5JUwt1OFANX93mZ1Ucs-v_V2QI6we8miyZN-j4Pj6ystFJw7_vnBxOn_tsMh_M9ZPQrf1MAroe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oaNGrGxsOpIrzu3N0fdcTag__ppBPpJF7LtdNSm4FKv2z_QO-82nkU8G6OoVDEaSaWTd-X2pdiG7YbUvufzTBqPb_OhTzaLyo6vwRaD8GCbKr-hd8iJnElcYORsIbwhzYFX9PQLzVyuzvCk2yIVpaLs7ojVYpkKtVxhLf31TerhpvfSH37PRW02724AfiCiXZMiKpHy3_07n1z11FOQ_pzOkKXNfYfaukTwFeZo2IuqMV2bxo50pykBfBA4s5KgI7oE_eeae8dHCWNXEI6Kr8xVKfac_y3hFA4ryOZkn0bgMXj0XOPyoV5xdDHrEKmzSuTy0W5B-IHeaMKaY0E845g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzfgO3QcBz6JUAn4H6UF0a7i6b10gQd20aGhU24ERKgVQ3ak_ubAiIuYEtXI-sGQchJrOL2ATVpuJt5gjc-D8ZvFAAxOEIPXCMPirFvpdilqUvLBQyZye-KAZMHIn5ewGwvGvVlx4U49t6woEI4rallYdwqRvM2M-NtmSibmM1Xjin8pyAj3vbfs1FJ_5UgrFSQyM-F4ZPQFb6f-Pui8oLZw0XY8pHMiwyBGUqldfw4xF7tWeZoAGD71di7632GfQOi8YnxdKAmSc82tvhZ3QpYYJ2gjfErd-1BL2_Ag-hAlZ4cDIVYXs8Fl6mpfL-7wQRsZufTwyZKWVAW3ARP1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaTDOBkPxIi2f6BtwYaTVAWO_Cadgr9N2t9_yaezCh2iK5gK31N1KwqHUFxqFhMXCam2ZE6prOH9-D9V_URXUIIfEs6E2N4zSuAEdfu2kI3C0zPg-CAuNku_tHEpq3mwximorR2ehHbkTrReCpOrv8lgpPZz46I_2SWw-B4HorjbPYN1DxYtmLEE_-qgCpjzQRcKNNK2ulqF0E4wvAtUQ2syVbr8GyGz5TJ3VDWknmwWP-dee0IOyOTuYJ7O-p4qenrOU3AYvMfHhAjWZAva_G6Sh8vJ0JIQfZVwA54_uu1KLmmMRVslO4cwcScRUrG8ofoR7YiPZuOXlD-jskXbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILbfJ0tf3eKy3SWwJrUz2GCgP5AUW-T62LYRkLjoM5tgi8Ei1jSNbqZf7gTFdX6fWRecrwUhJo7gTLaAOBvFLUrQ1mVVtkmPZul9IPKrGGZqOVMyuxNdIqeBE8dPNcDN6mWtwF3DcJkzEVfIkoV-mM4WNSUhxtgl2QbQqYBeSbIXwg_64MImuegDGbSIQLK5_vMaExiSbWwDpJGSbec4kiGiraUDFwnWNBjDTJ61oKyK5m-kdUuEez97O09IwOoS3CJzXKPpM3BsW34-sOUPcxnDEuWB4vKDgQPKzRtvJIowClebxj--8wH1PgzGQq17hUxWBTglOXxGDI9GSgYfqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردم شهرکرد، شب هفتادودوم را به یاد ۷۲ شهید کربلا به میدان آمدند
عکاس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/435008" target="_blank">📅 01:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435007">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/On9lhyZTn_gIokf5lZra0U_aviq-Px6JjvdQtejb3EY0XMb3vfcn7450ouOkN7szeFgxizM0FkSM5Rjg9TO9OLFPDuKo_ouV7qIcbHHAAN-V4LKolQD8-ZUx5pkDGLdrs01G6rBFTGeNdrX_DGe_irU9GO7nLZiRshhRqFUQsqwkKySIv32AQgdusxDkOMeSisyB6dtMxXOe_616oGhJihXqjt00qZb9p_eFZVoKj9rB8rCbp7_RJMySdpkYVxYesOQ8MEE0UfPiJgVkcnADXYt3fH72L6EUylUxA1cloP7PPvbDZpZmgHnjB9RU_4IFvnRcsZEGtyVztAihltYHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاها دربارۀ تمایل ترامپ برای ماجراجویی دوباره علیه ایران
🔹
شبکۀ ۱۲ تلویزیون رژیم صهیونیستی به نقل از یک مقام آمریکایی مدعی شد که رئیس جمهور آمریکا در حال حرکت به سمت دستور تجاوز نظامی مجدد به ایران است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/435007" target="_blank">📅 01:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435006">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
وقتی رهبر شهید با «رمان نوتردام» پروندۀ خلع سلاح حزب‌الله را بستند
🔸
روایت سید محمد حسینی، وزیر فرهنگ دولت دهم در برنامۀ پرچمدار خبرگزاری فارس، از دیدار هیئت لبنانی با رهبر شهید انقلاب، و نحوۀ اقناع آنان با استفاده از یک رمان فرانسوی.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/435006" target="_blank">📅 01:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435001">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgmFMrPy26AylGz_mlvdd8zYV4YpY_NvIDqJWTNm-314nu2U4D8whkDtZMIvVBpsKRuhDNr5LizCY7iJrcy2F6SafOTbqmzBMk7K8tnVb2NrOsSZXkudai2OVlCkme-oW8Eysg0hqUUDE6ghCPEPIu2Qu1wz8b4NbPewSJLGmuXWdWxSwvnSatBdWFlHVWbodkPvbRxjOLgjfUOBdKcJhlioj4Col_GiuFHuopDHySW97UuU3SRDvYgidWl-aPqx1lCqFeKFzNms7VYtAyXJSpcOD0ObsEKkf56D8dsxsVytRqlIZjPTiK5-QY21C_NJIXmVO7N8D7RfE98waZcyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxweXsdN05GENsSuyltwfwp_4JfIqSUY83xBb1Kn4bG02s_dh9UV4U1wjkxn9pD0uVrPSXBFagDJ1rD4_tmOoLMwxzHqhDJfRKn0cDp9AVXH1_1Abooh_HKl0C7xjoWoF7hLIjuJfeTY0iEWCYlU-LS4Yx8KPTgJqkn7gaVS4XTliXO8M9GUPlhMEUaqShyTEs9cBJfscYl79FCW4BVooMTqgichzoW_cYY_2XIivrcZ6cl3QceGZVXMIUIyLoLG3CBE_GmXaFKW82no0cSJcyWDxP1I7bFzB6GyJF0rbqy-y6TDEXbO4e1m9vmSSNMM1TjMFEjWoYGrQ7T5dUt1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCD4XiADMSn27F-QdqgJT7yOdUbvFsabUxGzMH_6dfAQ8gl20mKmSg2Rs--xNRjXHYu1sAQaPrLYz-yG9Bzf1sT8fQTzRpuG0czRkfIWtp7MYY6HUblieXOVz7H-i4Hs6b7L8mMkSGILvh6O3heB6t4BR2o3HC7hiSEQ5Qt9dWuxfuJ0cKktLNkz3j1bh_Z70q3voRkhtjxWQEu-rPYkawa5mjxHsKbf5QABp7tv8zmNvm3KR2X-8cbISJdEj4ZSOmClqm6yeOEDBY3oDBB3VNIwTUS4BGPIX-RxgyjCpyBRKJAFCb7pa8w3kqfnmMsGxwcPLVtBSoi3iPjABwzUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mN_Akm6NzPRNYcEP7Nv99vk-0GCsdwLcaMyCV1Nuknri4ZCvsUIHGIRJo9Ni3im01XArKdHPqt6ewntFLyNZymTcWyLhaGWfPtOjs32rF8Jp6-DW9PtsAzDTTNVE5O-NLfyxQwUs2t9pr5hep4lZAjY6GcjgueHU6CSNldZoEDqJQpEJVV6Z8cNLF5d8XSBEd_t780s8cbeQ6RJiingjoyg0nmx3nXWugOQbjqICA29weC8iDsR3tXN9HFDC-6OmYEI6_FCGjXTFmMrs0Bh2Lbd0RBzjXkg4wi8NePk1zXx_4PhPKTerO7XNvdk-Fs2F7scZHyezFlxTfEUDdERXnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmnEGkRbW6mE8ipZeoOxeYTZ8V7UnmtxdXeMz7yZ2ZgoXoaCtiRO5bbwNC5mgnpXa4fhl9wublM2AtAYlq8NGa6Leyb2evCbWhZWdKadleqphbMKMfA7tlnDMqZDGSHm9uGRUBpqMl227vjgOf66nGvgefnHmqBpDNNJqRUsFi6EIRqkLC7apFfV69lcOUcivioQpuHhRwhTPqfMFp4xSZXVkeX73sXiatS-I0KAOaqrFX1ytq7SsLwP0bpwGctSEtZdJwo07mmfCR79ZB2vol2BUcUnrcmBxGKIXIBTj1hj3rijcrVgJFKBNerNq-zKDcP7LK43uedP5HRBRGCOHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/435001" target="_blank">📅 01:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SL6SKvYvH20DYtA78z2t9Z3ymXiquxwpye2xgg31VCKuazxaeGB2YuZSPGe3TYtOpEgTgtgND7Rb0tBkD1T0Zjft8MNFuIi0NIp1Z9MkShdEvW2IqyEasAx75qu8ilftO4EvJ4u7FwshjgQb1uJmWkF6GO-X_JeC4HtOtrE8AzthI1KtRLVR_-_wC7NNl6A9_nKxe8VP6cUCky2zw0jJR4jMh7ZkUmidD4ATvD7H52cj_wVuFYNk-9vQtIaKFZh1PPkcEcK2Gv6_IsCX1DTgldvcHyqVb7aadMuEterpjp4OkEfU6QjUe-9LkAT11fZHUDhFrvywjKSV6jzsPk9iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3b3eJbUAtwU85DKe4O6OvUsai8GBYs6B7xGpgAZFNjaANSTwXpyUk1dqw8F_HhOoFJdefOZ3jfZemjrazi40Yv6HUmkVdypoQssF-zP_v1p98WJp_nK0rKiqR17LVIWcnsgTJ8c3V8bYBotkaseNPzSUCrbYuF5LNP2WiSOlXYfshZNyJfDL4dBmqCqJ7Lj5QEiTxl_9UxeIZwKVzZDNVezjoyJ8TUTazQF0eBHTkXQSSGKPVXPG2CM3GTtFtbPqcgXapP-hjllZ3_SfAbFGqSFT0LzPaUUNJdfnR3egePhLnkIX0LVVpkTh1I7korIeArfRfcU-XcnbNz6Lt0CdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMCzmlX3PzsI6tC-nWtOOg_G5owyAZoj9flbKw8dq-blkU_G8_bh_Yz1JOauf47S8cMpaggut4O_zwJ4ZAybIbE4_LFc0Pw5F94bHrHA2H0OB0fvJCE5hp7aIDvXjXOjPzx9xirqnnWdyY3H_pIlFU5GGoHZ0AUqq2GOdZx4voLvvlwjmlEy-xbkOoVF9KoXI6jqiuloeESctpsoLzyJu_4J1NoQIr_tEaI9SvV4qP81M0u3r_iZUAuoKZdzFc24gFEaR5KTZHPgyF4rcP2q64gDTxej65Sdmmspm-uYb6IY-nid_jY5t6Ht4clQslCXWyfmR-JMKIVqks3KmeZwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEyA2CXoP8OoqDe3rM9VDr-loP8NVrOl1tGUcX8WlHfgQrW5YHsw8HzwLa5Zc3s9_xgHmqjqU6CWjMp7NJ72hmC_X2kYFVM-MXM0xNIH4vslxKkN3dltVeb4bK9AoVThqvr5xU8sNTHlfwJBAazsVprUjZNw8Wqu_3dN_HI5T7GMrmOC0Z2OZDISqvOCXZkl3A-QP8FvCb7Dmg6cgmcGfq4SzRvAsgWkGqMn_xRsKqXS0E_wDAcriJlh1VlVlDuibeQcfJki8fsvZpWtBM_-3LU6zGChf3BTi_qkWEljtH15pAc5-Da-AegKIYNAapjDA1VVCT8k42in3Iy-M-lrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/In9wPpBG6X_eSu3OG0Kw7xe4EybsqgnVsbOqD9z2nZt_5qiMAReVjMpuMImTKm3FVzN6b0GK6Rilg_2BFkRqXByYM6RLpc1DkeMDBefuPDjS3pNMR9xy7olDonjxObmAn9VPmFF2LILk0QjG8PETSu2XooqgCwhtj2KGAWMCC0Y071FThNFZKcdRYm9RB2WzW_TdAoJV906JzIXOs3moiPKJaXBla3iimsRHo32-xcUvrcyCek-cB0GDc38GANA-pNo1vBWaANXl_HORDb1txTjpm8rHXKgE6lLJL-YzWrchtLyQQpqxcL6sIINlcQun04IyZ6itpWaFDC8LZDxEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1ptj7yJ22uLfIeNMs60vXttnDhxFMaJE4tGRnN82Xs0PmF6eg3dPyCypFWi74bAshcoHrjlD5aVF6pEB6OZ0hAXkDw8CxwHMkcCx-dH5_3MZkYjVQl1LBIQ8p2kYCOh8eDTeO3ZIO2EemGFyYS9z2NZjmzABGDSuoOAwdywLV5eal9_W-pJzB_PTr_eWR6FE5RiQg1VFCHpILKIE0_Syll9JLkaEsFc_kpxSYoA36GLlYwLu4eQCTlY7y037GJYvQoEq8OIxVtDp-EECN-DdOsHakJwhD4IRorTF21VtI_2q8GBG1nUWGONLKRdtXWkhXYODW541mca_hReEeTOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiiVDt7__hqe-i6iGseSI8Hq-_d93IE6-l9SKK0IRmOd6kM1FA8lBBJNZ5YBqm3VPxO9zjgpN43hjB-H-Bx-yagnHjJV_H8gIS31jhzLNK91-raYMXe7hqE51ifH6YnAQOUqO1O0Zrc0wxn2MKoV9C11TuP-fXJ-HjQ-NTh0s_lhKDkObDNbp34k3uChPsPyHwCfEmV658vb4zB1QerJVJhMU4gHDZTHxp9abUo07ORv5xpWWo2RikJ7iyioyAEoSZPzLQB4EG8JdnVlyE4xZcjDBMWXWT6a6JWNnSq0W7p1Spas9ySANbLTJKmD9zkPktmhK_7TW7P9Gu9qhVxa8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tc0yUj0TnivoJyqky63jr-ZqDEy6tf_NSWRk0YrzK8GyhcUgX_IDiglg9eH-udFEjDQOAfQ0T1tFP-Y-OEr2_XICCDpvhaxlBMwE7NOgRwa9YC8nVui03GT76kINg8ViPJ_oxqFOrPfpHgNdk65OOrRcpaB5aGDvJdDD-swUTDJnCXNp3B5YLJyTS1N-EkfdsjqTK3l-ciIxmwh3wCPiFvUuB76JnqUL13TnAAL7I-WRZF6OxlvEOMCButoJZWUlmh0ql9DSUjUnHciDOiATYKXUbYn9lHL3wmhDwiIiDFR2K0_M5bjKGYuaQLPRtNRxb22mn8Me6ZMnrNlD1y0Sbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A0ZPCcXbHy0Xy174UgOLSyMFwM6wedEW4QJZsYo1eakvb-esNuMMG9PKeGpkBJ0YP0GXL9Oyrl3gAasVca1l7PVxBSjDRahLucBCsT6jjUJDwkHJY4rusIM6lZiqQLZfv3pGJxC9pKMv6qWReZ3o_h6afoMf2m6wkrGeFF4M51rG2VgB_3gTL50hTFFcy0TlIP8l3aIEqjPOUXAhR8PLlk-dtjzW0olCkndQnmPywMFbbUG4qQplU_7N1AXcryleeWPf7uYZ0hSKeCKcqllTLZzTIFGS__25DooO5_KhpmbztN2GAMhpDjvCQ2G6EbLd9XkdjcOMnYiUzXfpg-Ptfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgXmQynhBU8sWSH-lKhezteaA2BlS2w8ZGuEeNDUBTvyKx0GOzpNtuguUZTYFc0Y0LCDFlulbeI6mCNgdCx9d4bzVswmtcRKO2Ox2EYkpkWizIYVC27Aka6uzf99rdxhuXFn6zkCAaMf9lrhr2shrLXnWeD3YTfzxBqnuDi_YyjvTgCBaJUcAOnXFftvGNXUCagGuPR6_W1XVR1oPc1z-lY55qVFQuN09ocC8JHMFH40wyNcATQL05rMcfsDwHKNgIM4dsaGywV50yLvAt4PynPIds5alISNw6ssp4oi0XXn0oLKG_IwZBSpLA3wLXjGtR3d6buapPZmGiEo-JQ68g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/434991" target="_blank">📅 01:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88a97a0e6.mp4?token=CMHZ6W3_LXcigZy-_Rw6yMOvg44EDjP-2eR3ADY2Mcew39u5ZBgtzlZyEi6juwx-u6la6Ycir0c_36q0_yiwy_vjWEU6FpcPN23KEgWSMrIdEHInQAliROxu1f8Ah3noUGXRibkYDzJSg8d-3b0yNPO_fi7h2BylnWeoCDJkf-q2Orux7O8oR1SSMFoNTnG-hE0paJcAkTfhigL4s12Opjp5edIKRvjpOtXu-rK4NzAmOkjHGDg3Qbnp8W4NKXxxzuwVgHgmLEY9kDGM7KvHvU8rocFznrpGikJZ0hkIdzEesWBjUUOIziePntLpHzuN9fRE-wODKrwodPqk7XDtxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88a97a0e6.mp4?token=CMHZ6W3_LXcigZy-_Rw6yMOvg44EDjP-2eR3ADY2Mcew39u5ZBgtzlZyEi6juwx-u6la6Ycir0c_36q0_yiwy_vjWEU6FpcPN23KEgWSMrIdEHInQAliROxu1f8Ah3noUGXRibkYDzJSg8d-3b0yNPO_fi7h2BylnWeoCDJkf-q2Orux7O8oR1SSMFoNTnG-hE0paJcAkTfhigL4s12Opjp5edIKRvjpOtXu-rK4NzAmOkjHGDg3Qbnp8W4NKXxxzuwVgHgmLEY9kDGM7KvHvU8rocFznrpGikJZ0hkIdzEesWBjUUOIziePntLpHzuN9fRE-wODKrwodPqk7XDtxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دادستان تهران: اخلال کلان در توزیع، گران‌فروشی و احتکار مایحتاج و ارزاق عمومی می‌‌تواند تا ۲۰ سال حبس داشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/434990" target="_blank">📅 01:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434989">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">باز هم آتش‌سوزی در پالایشگاه آمریکایی در بحبوحۀ بحران انرژی
🔹
در حالی که ایالات متحده با بحران بی‌سابقۀ انرژی و کمبود شدید سوخت ناشی از تبعات جنگ با ایران دست‌وپنجه نرم می‌کند، رسانه‌های این کشور از وقوع یک آتش‌سوزی دیگر در یک پالایشگاه نفت در ایالت اوکلاهما در مرکز آمریکا خبر می‌دهند.
🔹
مقامات هنوز اعلام نکرده‌اند که چه چیزی باعث این آتش‌سوزی شده و آیا کسی در این حادثه آسیب دیده یا خیر.
🔸
چند روز پیش از این هم یک آتش‌سوزی در پالایشگاه شالمت در ایالت لوئیزیانا رخ داده بود.
🔸
چند روز قبل‌تر از آن نیز پالایشگاه شورون در کالیفرنیا دچار آتش‌سوزی مشابهی شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/434989" target="_blank">📅 00:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434988">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
حماسۀ مردم شهرقدس به شب ۷۲ رسید
@Farsna</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/434988" target="_blank">📅 00:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434987">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حزب‌الله: دیروز ۲۰ عملیات علیه صهیونیست‌ها انجام دادیم
مقاومت اسلامی لبنان در پاسخ به نقض آتش‌بس، روز دوشنبه، ۲۰ عملیات سنگین را به شرح زیر اجرا کرد:
🔸
انهدام یک تانک مرکاوا، دو بولدوزر زرهی D9، یک خودروی هامر و چندین خودروی مهندسی و تانکر سوخت در محورهای «رشاف»، «ناقوره» و «طیرحرفا».
🔸
هدف قرار دادن سه‌مرحله‌ای نیروهای صهیونیست در شهرک «طیبه» که منجر به انهدام محل استقرار و اعزام بالگردهای امدادی دشمن برای تخلیه تلفات شد.
🔸
درهم‌کوبیدن تجمعات نظامی و مرکز فرماندهی تازه ایجاد شدهٔ دشمن در «بیاضه» و مواضع توپخانه در «عدیسه».
🔸
مقابله با پهپاد ارتش صهیونیستی در آسمان «صور» با موشک زمین‌به‌هوا.
@Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/434987" target="_blank">📅 00:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434986">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">وال‌استریت ژورنال: امارات حمله به تأسیسات لاوان را انجام داد
🔹
منابع مطلع می‌گویند که فقط ساعاتی بعد از اعلام آتش‌بس توسط آمریکا با ایران، جنگنده‌های اماراتی به تأسیسات نفتی در جزیره لاوان حمله کردند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/434986" target="_blank">📅 00:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434984">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
بسته‌بودن تنگهٔ هرمز کرایهٔ مسیرهای دریایی آمریکا را هم گران کرد
🔹
پیتر سند، از متخصصان داده‌های کشتیرانی در مؤسسه «گزنتا» می‌گوید: «حتی در مسیر اقیانوس اطلس از شمال اروپا به سواحل شرقی آمریکا که تماسی با مراکز ترانزیتی آسیا یا بنادر خاورمیانه ندارد، نرخ کرایه حمل از پایان فوریه تاکنون ۵۶ درصد افزایش یافته است.»
@Farsna</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/434984" target="_blank">📅 00:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6jBma7NlMq_NZgbB8WQyIQUSjZ72w7itepVWjoxmzw19ceVj-3jWyDID1MwBRM-Zjj5mbhOSWPvla3zCMigVENbJgxKRHC0pvC3v5pdSPsTMl4SlxxlGw-woeKSwrqU3cgTDFS087jysJNb-Kg2wOW_V6Wu-xEESVDmai-xi-T-MtXMNhTJkOWFCCzTJYxzsaLJtfkjookXMysY57Wfh1MV1_RUgvQGLaTqjzgBXkcf2NAQbKOuK1L22WM3TsAuLSMwAHdgsGurpnT9OYfIakN1l5jbKhxQ_Eiqoh8B9MU4niSa2dwY-L_NHKD4gG9ti2qesT-brJ04q1g_R-P8BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: جز پذیرش حقوق مردم ایران که در پیشنهاد ۱۴ بندی آمده، راه دیگری وجود ندارد
🔹
هر رویکرد دیگری کاملاً بی‌نتیجه و شکست‌ پشت شکست است
@Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/434983" target="_blank">📅 00:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
هفتادودومین شب اقتدار در نیشابور
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/434982" target="_blank">📅 00:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434980">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فایننشال‌تایمز: جنگ با ایران صدها میلیارد دلار به آمریکا ضرر زده است
🔹
فایننشال‌تایمز نوشت: جنگ ترامپ با ایران با هزینه‌ای معادل صدها میلیارد دلار در بخش تولید، درحال درنوردیدن اقتصاد آمریکاست؛ چراکه اوج‌گیری قیمت سوخت، افزایش هزینه‌های استقراض و گره‌های…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/434980" target="_blank">📅 23:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434979">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QglDbrv6WeC3U-rJnr6rp8FBiPcMKrBE9TNRwab6KRWrMCORWHijUoRapuo3uO6SZdjfGYcSq1eX3f-pudzzE7asS0o13OtYK5G-KtnB-8d8z6RZT2iHCCcJBLeJ_w8l3E6j7EpjfIZF2_G2PFVI6cOGC6_vv14yrffx4DAQVwK5QDioP_flXDWT5sQePzi_JHT08qAj3woMR23F7tMgn9ZrhLQgw85vG71bwLRWn8U3ODypGCfKkYpmrngPVctFzkg1wTYB2VP6HEEVMQxfbx3wbNr36TAjFOg86osOJZngJVEEVSOQXYy6AJZJXottrVmU_pEF89oux2ibKh0f5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فایننشال‌تایمز: جنگ با ایران صدها میلیارد دلار به آمریکا ضرر زده است
🔹
فایننشال‌تایمز نوشت: جنگ ترامپ با ایران با هزینه‌ای معادل صدها میلیارد دلار در بخش تولید، درحال درنوردیدن اقتصاد آمریکاست؛ چراکه اوج‌گیری قیمت سوخت، افزایش هزینه‌های استقراض و گره‌های کور در زنجیرهٔ تأمین، رفاه و آسایش آمریکایی‌ها را به‌شدت فرسوده کرده است.
🔹
برآوردهای اولیهٔ دولت ترامپ، هزینهٔ مستقیم وارد شده بر دوش مالیات‌دهندگان آمریکایی را ۲۵ میلیارد دلار اعلام کرده اما اقتصاددانان پیش‌بینی می‌کنند که با در نظرگرفتن مخارج کامل نظامی و هزینه‌های بالای تأمین مالی، خسارات وارده بسیار سنگین‌تر خواهد بود.
🔸
لیندا بیلمز، استاد دانشگاه هاروارد و کارشناس هزینه‌های جنگ‌های آمریکا، دراین‌باره می‌گوید: «هزینه‌های بودجه‌ای که رسماً اعلام شده، در واقع تنها بخش کوچکی از کوه یخ است. شاید این هزینه‌ها بلافاصله احساس نشود و بتوان برای مدتی اوضاع را وصله‌پینه کرد؛ اما مقیاس مالی این جنگ به گونه‌ای است که نمی‌توان آن را تا ابد پنهان نگه داشت.»
@Farsna</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/434979" target="_blank">📅 23:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434978">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d07aed129.mp4?token=LkhymDau7Hrno6F5fTufVDqAQc_LN5VNnKrrhBCz_07Xlu6ChneWQzbd2M9x_XIcTGvBv19RQv_NwXHWOf91ZKHkSg_9vTKkVy6phAvHp2ty4x3JexVasMLJevTVTlyPcFWwb6LOGda5Gv8vcjXYaZUVgXcTi1aogA0piAstP8nPGlkincWUrWueMHpoq3x_MbQfRkj5jF43EOu1XHjc4xlbbUHMe9uScsO2T_mCqZP3PrYmE60rbbq5DRO51VkI2v9_INb82B8nmiZv2K-XYRm0C7iMLHy_2WjQxfda4CQ3VrFranooPTVqSry8bA5q2JlYDVLEwcO1zHEpkiWvTxMbGGdXkT4HtNSM2GjCw_AReaByb6a-1Zk3Hd0K4sgoLngpoCsFiyCnvzAvPV-p9WD_7mY8E17IyJHF3m0QYziWRNVs1-5cYUdPld4nht0nr-SKBMJ-OepMfb_PHmxbhIwQQZX5PT73cNZroYidV7KP54J3pInL2uHJfym-mz9I7L-_Ym5GEz9cCVp-0CmeCsBjieM2TRr70i22c8JYvmNm9egRjTt6ESY-zI4bRqOSps-EyKfmA63TSoosNkOxlEJbmn2oHwmeAssmrqwQ71RH_xNC9SuR7SXcWbH8PqBWwZVSCva3deFztLHM4gBlifBL-L73LeCSq9gHpaJYyeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d07aed129.mp4?token=LkhymDau7Hrno6F5fTufVDqAQc_LN5VNnKrrhBCz_07Xlu6ChneWQzbd2M9x_XIcTGvBv19RQv_NwXHWOf91ZKHkSg_9vTKkVy6phAvHp2ty4x3JexVasMLJevTVTlyPcFWwb6LOGda5Gv8vcjXYaZUVgXcTi1aogA0piAstP8nPGlkincWUrWueMHpoq3x_MbQfRkj5jF43EOu1XHjc4xlbbUHMe9uScsO2T_mCqZP3PrYmE60rbbq5DRO51VkI2v9_INb82B8nmiZv2K-XYRm0C7iMLHy_2WjQxfda4CQ3VrFranooPTVqSry8bA5q2JlYDVLEwcO1zHEpkiWvTxMbGGdXkT4HtNSM2GjCw_AReaByb6a-1Zk3Hd0K4sgoLngpoCsFiyCnvzAvPV-p9WD_7mY8E17IyJHF3m0QYziWRNVs1-5cYUdPld4nht0nr-SKBMJ-OepMfb_PHmxbhIwQQZX5PT73cNZroYidV7KP54J3pInL2uHJfym-mz9I7L-_Ym5GEz9cCVp-0CmeCsBjieM2TRr70i22c8JYvmNm9egRjTt6ESY-zI4bRqOSps-EyKfmA63TSoosNkOxlEJbmn2oHwmeAssmrqwQ71RH_xNC9SuR7SXcWbH8PqBWwZVSCva3deFztLHM4gBlifBL-L73LeCSq9gHpaJYyeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ حماسی  «دست الهی» با صدای مهدی رعنایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/434978" target="_blank">📅 23:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434977">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
فریاد هیهات منا الذله یاسوجی‌ها در موج ۷۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/434977" target="_blank">📅 23:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434976">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6437c3f20.mp4?token=C9LJkt0Ty1VV6WbXjQjM3pNEFnmh4PMLZXMaonLy6lOIRoDGUePJpr-LaUIKU_uMgJwFSPoGIepdZAKhhlch56e95DisupqstPnj1x_V6toSnJ4JQG30xjDioBH6-z989l6GBU6lwrGAdzbvWbjBqOUqBwKD_pYRVCWT1MEB_20HaQiX1C-jF1Ceyq8_V5yEPZK2osWb78izlCL11ltnHIKLx1UtcBwoZmdoQFU6c4eBNlN-jIqALMqAYXrqTzB7JkIFlsiOZvZXQTc8GGx4jFxWB0l8GRrK3aqCwDfa3L8VISD8NeeeuPjMMObQKNEztyYucsSgm3QB0wasGd8rrLCpWMe7JN5g-c3VlW1iah36iPBCese0oyQoEV2BQrLFGycEw95ju0Qh6Dno4tXNJzEOEBv7QMmVQmksF7sKr8lC_6_LNST7dbSRXSKVspyGTKJ9C-wVlrZYSWSRymoYK8EGwSL9KNhuS_5v2jnzqXX9wILhNrosDBO7_BHZUR34IOQPUa0A6B40o_WX7AF7VpIMIQatt2hQd8402miwJtblgpB_qk-QUyYsNgMjK_0xD_x8zpsj6K0USAsEfyw3i2D5chUtDVcY4y4dBGRZTpZ3doTZxkhHFJPVDh0KQax3n-Vxt0s5Pk6xidqT4Uj5PVDacx0upgGUPkMIWDcP-sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6437c3f20.mp4?token=C9LJkt0Ty1VV6WbXjQjM3pNEFnmh4PMLZXMaonLy6lOIRoDGUePJpr-LaUIKU_uMgJwFSPoGIepdZAKhhlch56e95DisupqstPnj1x_V6toSnJ4JQG30xjDioBH6-z989l6GBU6lwrGAdzbvWbjBqOUqBwKD_pYRVCWT1MEB_20HaQiX1C-jF1Ceyq8_V5yEPZK2osWb78izlCL11ltnHIKLx1UtcBwoZmdoQFU6c4eBNlN-jIqALMqAYXrqTzB7JkIFlsiOZvZXQTc8GGx4jFxWB0l8GRrK3aqCwDfa3L8VISD8NeeeuPjMMObQKNEztyYucsSgm3QB0wasGd8rrLCpWMe7JN5g-c3VlW1iah36iPBCese0oyQoEV2BQrLFGycEw95ju0Qh6Dno4tXNJzEOEBv7QMmVQmksF7sKr8lC_6_LNST7dbSRXSKVspyGTKJ9C-wVlrZYSWSRymoYK8EGwSL9KNhuS_5v2jnzqXX9wILhNrosDBO7_BHZUR34IOQPUa0A6B40o_WX7AF7VpIMIQatt2hQd8402miwJtblgpB_qk-QUyYsNgMjK_0xD_x8zpsj6K0USAsEfyw3i2D5chUtDVcY4y4dBGRZTpZ3doTZxkhHFJPVDh0KQax3n-Vxt0s5Pk6xidqT4Uj5PVDacx0upgGUPkMIWDcP-sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرم‌آبادی‌ها: ما ذوالفقار تیزیم، ما قلدر ستیزیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/434976" target="_blank">📅 23:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434975">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
طنین الله‌اکبر در خیابان گلستان اهواز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/434975" target="_blank">📅 23:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434974">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9YMrDdR0sK_jSp0tHa0snpGYXwcONw3hT6T-tQ1EmvrOoEwN3KpYhzQHtd3_xJ1ZJPeYJ83PnndLFJ27Szp_GTxR3UuWeIKexsVm0UNaseWm4h2tyweoLyTeLwzs_CZ300iT6PiluGgwn6gPg2DliOxgFcfY_G809E1Hf-FBZDJ8dy4buqafYm0TKRWGdTmOpOrFu5O5s1_CvU9_ySH8pVoyFYKrj3aWnw5X94MRZTuSfOxq2Vf7ES-TzlMiK11XEmyI5xagL38BN7ltsVxwusT7Irfj6-7xhJWSrzZtxU2g_my9ZF9oLXVprSNMwkildiJQQ7hT7LXukfl5A1EVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر انگلیس: هرگز وارد جنگ با ایران نخواهم شد
🔹
استارمر: اگر وارد جنگ ایران می‌شدیم باید با آنها روبه‌رو می‌شدیم و من اجازه نخواهم داد بریتانیا وارد جنگ با ایران شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/434974" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434973">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R04XxoOh3LSoxdBGGIyLIQYmoXS9H_Z9EdO00kUWWHHOJIGNTxc3KOL7RDxLFcE2XsVOrn4OIT3cXCEkpDERDLur4C6PrGN8yF9k4_6P8-WC3yqDhyNDWAKmhhRbaHv0S05qwQRuCobJl1vmQSSswpaNMGTuTZRiJaBdHPe_vA2c1TRgkD3CZb260Qr7ToAJdRvIzn4qCKLELBAKEaUuBxFVAguN_m41kCczTHA4yfDqQQ6N96Vntbo5aLpf0FXHAvRQJ-krdTJXkkCCJog9s8ah-xJje24IcCoWxF8xdv_A6Ea6RB98-_QKrNf4V_vA7DWAwXJBaJQVBhB87QiQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابودی ۵.۵ تریلیون روپیه در بازار سهام هند
🔹
بازار سهام هند در حال ریزش است و تاکنون ۴ سهام‌دار بزرگ هندی قربانی سخنان دیشب نخست‌وزیر هند، نارندرا مودی شده‌اند.
🔹
تا این لحظه، ۲۴.۵ درصد از ارزش سهام بانک دولتی هند، شرکت بزرگ جواهر‌فروشی تایتان، شرکت برق رسانی…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/434973" target="_blank">📅 23:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434972">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40494bdc0b.mp4?token=wA6_LBYZXZJlaITybHhMRJ63APTP2MQnFR7idbXPkW_3ovUl1FZWJEXRKkJatXPzohnR_iptJRqJbvnR_mSybXxeWRtEcTPl3VVlBC-WqumP1tCSxTS_igZaiwCZ-xcLfywg3hZGx53eTABSHGtCzrZ_SIOqievtuV62-5HVcfIIH9tuxcn0ydqrejnAT7lP8PDeCva3i7LDglAisuRHRiP0lnJ2YDU49sJ0yOj4N7LtthiABviuUjLFXs8OIJMtlwV0I3ylk1r-0E1v5PTnNMiICr7v4gt6bcrAvNRcH5MZOkxaP-dTmDCE-RbzKwdBTRJE03os5TsqeFon1UGSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40494bdc0b.mp4?token=wA6_LBYZXZJlaITybHhMRJ63APTP2MQnFR7idbXPkW_3ovUl1FZWJEXRKkJatXPzohnR_iptJRqJbvnR_mSybXxeWRtEcTPl3VVlBC-WqumP1tCSxTS_igZaiwCZ-xcLfywg3hZGx53eTABSHGtCzrZ_SIOqievtuV62-5HVcfIIH9tuxcn0ydqrejnAT7lP8PDeCva3i7LDglAisuRHRiP0lnJ2YDU49sJ0yOj4N7LtthiABviuUjLFXs8OIJMtlwV0I3ylk1r-0E1v5PTnNMiICr7v4gt6bcrAvNRcH5MZOkxaP-dTmDCE-RbzKwdBTRJE03os5TsqeFon1UGSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مورد علاقهٔ مردم: مرگ بر آمریکا، مرگ بر اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/434972" target="_blank">📅 23:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434971">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
مدیرعامل آرامکو: جنگ ایران و بسته‌ماندن تنگهٔ هرمز باعث شده که یک میلیارد بشکه نفت صادر نشود. @Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/434971" target="_blank">📅 23:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434970">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آمریکا تحریم‌های جدید علیه ایران وضع کرد
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا فهرستی متشکل از ۳ فرد و ۹ شرکت مرتبط با ایران منتشر کرده و گفته آنها را در فهرست تحریم‌های ضدایرانی قرار داده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/434970" target="_blank">📅 23:01 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434969">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11ed6ecc2.mp4?token=uUNtHPJ-5TXCfhg602dEFqTLnQ4XghWUQJJNQzAuKQtdRhhIIc7ZAbLV7cnPMcXPEpGArxJla9D0JXAXTpVAU279IZQEtZMx_q7yRvqoXDSFdEmpKJ6xBqRsDT64BMGQeuFKznZbx9j_FiOz7zpjqHl7QOLBZ3bNVNLNm-NCHvGNTib2PkcIoyRCKUnsfhhF8sdhuB77JpJPBNZDtbJ-PpR0Ir69zLtLdpiOz5wLcu_DyXRNHE-sTqtHQoUJxgySneepwbGcxB5OgtfeeK--6urCYDkIJHsVLH9E0IPgXFBSXubfLRTIN9Eup8VC1kRicXRnG05nkAnfGv5eE4YIcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11ed6ecc2.mp4?token=uUNtHPJ-5TXCfhg602dEFqTLnQ4XghWUQJJNQzAuKQtdRhhIIc7ZAbLV7cnPMcXPEpGArxJla9D0JXAXTpVAU279IZQEtZMx_q7yRvqoXDSFdEmpKJ6xBqRsDT64BMGQeuFKznZbx9j_FiOz7zpjqHl7QOLBZ3bNVNLNm-NCHvGNTib2PkcIoyRCKUnsfhhF8sdhuB77JpJPBNZDtbJ-PpR0Ir69zLtLdpiOz5wLcu_DyXRNHE-sTqtHQoUJxgySneepwbGcxB5OgtfeeK--6urCYDkIJHsVLH9E0IPgXFBSXubfLRTIN9Eup8VC1kRicXRnG05nkAnfGv5eE4YIcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون؛ بانگ الله‌اکبر در خیابان کشوردوست
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/434969" target="_blank">📅 23:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a52af043e.mp4?token=sUhRK-ltC_7CsGHcnxJiV6F7nyLXvj1IGmcnKv3KOnr3A7Q3-lxSuGVcgfmsS0lFVN8WgseBtWzQYvMcV8gaf9bwO799xJYs8THRQq5YNlyGSB3q9Hpqh-ludLEVKg25thsi-Z4N8V1-katDyxtntR1sAUgfVm7OOP-2No42f2ZNnKvJ8gQbaWSbdgnnqQPtggiNl8KQFM65Jv7I0m3WrVS_z_rFCAhZYyg4Glno-cxUp3WG-m3kjEzcheCRVWP1w3IwL829ezF846A5SF-8um1B23frrf_-vahUIKM9KWzAeKuaQQINpevOqIJxRwJ3HSca7ox2R6Vo7ZiLPrEM7q_S6b4REnSBb5uGrXESvBSgPa0BEMbwCodYgA8FDGC0Bob1XW8MObyDUx-_A1XcyVfr3Cx0L5FsbeKz6hoemCizcMpSbo0ATr3i5OV_w2j6ySlFNFdwry4s2O8n9SUrDs2MJ5RHdUZ_6SqogqSOgkLAFUmEIvf6ClWVK3Mo4q5IeBWhFj4--1pqsOv2ytmzkXPNRaK4RFNWPGnza0Y1g4hWbKY4KCYUEm24U6ANbuHXA4r0wKW9DJi0mD07ipVQJmRGZFTWkoY4IrP4ZD_J95vUO_VdfUtYcB9P9WPLE1wEhdO9Rwx8xtDsqw-lpP1vmWpdJHtaB-20Jzxvo5F1ApU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a52af043e.mp4?token=sUhRK-ltC_7CsGHcnxJiV6F7nyLXvj1IGmcnKv3KOnr3A7Q3-lxSuGVcgfmsS0lFVN8WgseBtWzQYvMcV8gaf9bwO799xJYs8THRQq5YNlyGSB3q9Hpqh-ludLEVKg25thsi-Z4N8V1-katDyxtntR1sAUgfVm7OOP-2No42f2ZNnKvJ8gQbaWSbdgnnqQPtggiNl8KQFM65Jv7I0m3WrVS_z_rFCAhZYyg4Glno-cxUp3WG-m3kjEzcheCRVWP1w3IwL829ezF846A5SF-8um1B23frrf_-vahUIKM9KWzAeKuaQQINpevOqIJxRwJ3HSca7ox2R6Vo7ZiLPrEM7q_S6b4REnSBb5uGrXESvBSgPa0BEMbwCodYgA8FDGC0Bob1XW8MObyDUx-_A1XcyVfr3Cx0L5FsbeKz6hoemCizcMpSbo0ATr3i5OV_w2j6ySlFNFdwry4s2O8n9SUrDs2MJ5RHdUZ_6SqogqSOgkLAFUmEIvf6ClWVK3Mo4q5IeBWhFj4--1pqsOv2ytmzkXPNRaK4RFNWPGnza0Y1g4hWbKY4KCYUEm24U6ANbuHXA4r0wKW9DJi0mD07ipVQJmRGZFTWkoY4IrP4ZD_J95vUO_VdfUtYcB9P9WPLE1wEhdO9Rwx8xtDsqw-lpP1vmWpdJHtaB-20Jzxvo5F1ApU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۷۲ خروش مردم در تربت حیدریه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/434968" target="_blank">📅 22:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45449344b.mp4?token=JLfYn_2BfFsYtthx9WPZCcngMi8rBSVSxQi_zuT1OOWAXN2kW_9eUp4BfPTJOQX51dXZliI38ziVFLjCBvNO7opPn2up3I-TgKuEMijzXVaacYUrc0Nvlx16YN2qTHsnt2lHmFTZO2sFQ2KcO63LtXHlvIGYp6RCEARQKSIKffQEuPUi2TPQEdZsibeDlcrHjgQBTF2b4-5Gey7bXkrVwX9HDMNhVHbfpcHLeZCM3QwQsCbReas11dVg8ayjreJAp_cxHLaKHuuzxokLi7NKPY3IKQmS0GE977_PZLIGL1fb8A8wWMm9t3f302nuHSHaZMQD_A0Iun-XP61TiF60fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45449344b.mp4?token=JLfYn_2BfFsYtthx9WPZCcngMi8rBSVSxQi_zuT1OOWAXN2kW_9eUp4BfPTJOQX51dXZliI38ziVFLjCBvNO7opPn2up3I-TgKuEMijzXVaacYUrc0Nvlx16YN2qTHsnt2lHmFTZO2sFQ2KcO63LtXHlvIGYp6RCEARQKSIKffQEuPUi2TPQEdZsibeDlcrHjgQBTF2b4-5Gey7bXkrVwX9HDMNhVHbfpcHLeZCM3QwQsCbReas11dVg8ayjreJAp_cxHLaKHuuzxokLi7NKPY3IKQmS0GE977_PZLIGL1fb8A8wWMm9t3f302nuHSHaZMQD_A0Iun-XP61TiF60fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آبی‌اناری‌ها با برتری در ال‌کلاسیکو قهرمان لالیگا شدند
⚽️
بارسلونا ۲ - ۰ رئال مادرید @Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/434965" target="_blank">📅 22:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
مدیرعامل آرامکو: اگر تنگهٔ هرمز همین امروز هم باز شود، بازگشت تعادل به بازار نفت ماه‌ها زمان خواهد برد
🔹
اما اگر بازگشایی تنگه چند هفتهٔ دیگر به تعویق بیفتد، عادی‌سازی شرایط تا سال ۲۰۲۷ طول خواهد کشید. @Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/434964" target="_blank">📅 22:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341d1791b5.mp4?token=RqsWcbFMW3ds8NUOIpUMdkQUENJMsQvPLqlPHQMOabwPSppzVNlEzFeMAmA13SXEJmfBck0Q2xlMjDszmFsjC129-AnhPI7bUYXs1c8zMY3G-XHdDKZFy5Y7OjKpsqJ4R5Jn7U6CyhcdpH7kzukrT-B2gHzmtZcmP-mZmd2Vjj3_X3GueyyH5YRxi39-Qj2LMto16uNj38EV6yFEmD6uclOCPTAP3lld7D-pGTc9WGP2FZAUJOoRyWvnzwzhuxKayntPsQp5fn5xCjd5nbu40FvfaH0guVCmLIdqT2VHW2bAUNEJY9O1maELnJL1U4GBc_j7baJh6KTNc3Ja35qSRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341d1791b5.mp4?token=RqsWcbFMW3ds8NUOIpUMdkQUENJMsQvPLqlPHQMOabwPSppzVNlEzFeMAmA13SXEJmfBck0Q2xlMjDszmFsjC129-AnhPI7bUYXs1c8zMY3G-XHdDKZFy5Y7OjKpsqJ4R5Jn7U6CyhcdpH7kzukrT-B2gHzmtZcmP-mZmd2Vjj3_X3GueyyH5YRxi39-Qj2LMto16uNj38EV6yFEmD6uclOCPTAP3lld7D-pGTc9WGP2FZAUJOoRyWvnzwzhuxKayntPsQp5fn5xCjd5nbu40FvfaH0guVCmLIdqT2VHW2bAUNEJY9O1maELnJL1U4GBc_j7baJh6KTNc3Ja35qSRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبرمون هرچی بگه همونه
🔹
شعار امشب مردم در میدان انقلاب تهران.
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/434963" target="_blank">📅 22:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434962">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa87c6a9d5.mp4?token=W_uJnGGD7hD3hrfK2WCYCCdrUoHjg690JVYoiAvYrJAqL0pAFTfqZB_uA4rV7H1eRsKX2L5JMs6dpLG4gUIfSmsWJ2m8vfM3TUogx8vNsnEcqUnnklfeUH1_RbNXquz1QNV6As_p3cLSbj8ueDsayduQmU2rj2eSbVADVlZ67vHqtifLpZFogkj3MspVLD5M1GYjPzE8lCChP1Jm9HSnoNDvEdnGz9KGiU-wz5C3O-cTBn4TA4YtmY8qlmu236O7xvFDwWtZFg1thKNIf6-EiInmyZ3c2MuYG3zg6JLVMHoe__cQd5AZD3V6Ut6idaZlHVLsx995MXirqYXWdC7zlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa87c6a9d5.mp4?token=W_uJnGGD7hD3hrfK2WCYCCdrUoHjg690JVYoiAvYrJAqL0pAFTfqZB_uA4rV7H1eRsKX2L5JMs6dpLG4gUIfSmsWJ2m8vfM3TUogx8vNsnEcqUnnklfeUH1_RbNXquz1QNV6As_p3cLSbj8ueDsayduQmU2rj2eSbVADVlZ67vHqtifLpZFogkj3MspVLD5M1GYjPzE8lCChP1Jm9HSnoNDvEdnGz9KGiU-wz5C3O-cTBn4TA4YtmY8qlmu236O7xvFDwWtZFg1thKNIf6-EiInmyZ3c2MuYG3zg6JLVMHoe__cQd5AZD3V6Ut6idaZlHVLsx995MXirqYXWdC7zlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش علیرضا دبیر هنگام بمباران خانهٔ کُشتی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/434962" target="_blank">📅 22:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434960">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5KkQuqStWETS03hQTpSHzdAtqumznJUcIkEJHGfr78MbLrKvOKhmbq6dMCw_HYjqYbyOPqgE5xdvjipgqGpK9RRa2b7DV8wINDUbq0pBkfsZ5qmw_l_cnEiaKNjHKjbkzqNz895m93E_dbI8i50Y8DjfYLd8QGNp31mC_6TqV9B5Ro84encMothxo3CLHMxlfPz7jckZWvcvY4s8fl_x655bFcM742vpno39GvgXmcRx64OgZI84yDd5Oo00-iFVeAxI7k0f96VA6ECer98zNJn2R3KkSGLRDprlrNjLk1RORJpKKW-zHFvGtfuare5L-MdpLUBBEZ6Ki5-yqb6Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قاليباف: برای تمام گزینه‌ها آماده‌ایم، شگفت‌زده خواهند شد
🔹
نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند؛ ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/434960" target="_blank">📅 22:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434959">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
مدیرعامل آرامکو: اگر تنگهٔ هرمز همین امروز هم باز شود، بازگشت تعادل به بازار نفت ماه‌ها زمان خواهد برد
🔹
اما اگر بازگشایی تنگه چند هفتهٔ دیگر به تعویق بیفتد، عادی‌سازی شرایط تا سال ۲۰۲۷ طول خواهد کشید.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/434959" target="_blank">📅 22:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434958">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">مقام ایرانی: تهران مخالف انتقال اورانیوم به خارج از خاک خود است
🔹
شبکه خبری الجزیره امروز دوشنبه به نقل از یک مقام ایرانی گزارش داد که واشنگتن در پیشنهاد خود خواستار دستیابی به اورانیوم غنی‌سازی شده با غنای ۶۰ درصد شده است.
🔹
وی با بیان اینکه ایران با انتقال اورانیوم به خارج از خاک خود مخالفت کرده، در عین حال خبر داد تهران آماده است اورانیوم مذکور را تحت نظارت آژانس بین‌المللی انرژی اتمی رقیق کند.
🔹
این مقام با تأکید بر اینکه ایران آماده است اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد رقیق کند، تصریح کرد: آمریکا خواستار توقف ۲۰ ساله غنی‌سازی اورانیوم شده، اما ایران این درخواست را رد کرده است.
🔹
وی در پایان گفت که آمریکا پیشنهاد پرداخت غرامت به ایران در ازای خسارت‌های جنگ را رد کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/434958" target="_blank">📅 22:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434957">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNDtbP7HNeWOqhkCIp-S9ewOiAXo6QbppOBFI0N9GCuBTCqbLrHV91_dULNyXgz66KU543yI_V9mKVxeSWF4za8Ez-j44A9IUXT4mKeWG46o4zQub5V8DK0s4cCyI5ZPTQ_X_Ovef0uwvv97C8AhdrMXhmWrH20_cvN05N_aGUtG9Mg9ij7GO6gifZ_lrA8w3CbEMl9ZRQj003AuER_B4kd43OFMHSdaDPUxLD82-ZOgqqaSQPdHcQPvOwuZJOVwbG8QowMFB9SOuvqTSQiFLTyQAU3DLB3avVcf5REgwjldmydB-9mJBrMLweJxxwNSgNU2ioAskoJtPR6Wfu1yEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثر پروانه‌ای خرید یک کالای ایرانی
🔹
خرید یک قلم کالای ساخت داخل، تنها یک معامله خرد نیست. این انتخاب، زنجیره‌ای از حلقه‌های پنهان را به حرکت درمی‌آورد؛ هر معامله، کوچک یا بزرگ، در کلان اقتصاد یک «تکانه» ایجاد می‌کند که در طول زنجیره تأمین منتشر می‌شود.
حلقه اول: خرده‌فروش و توزیع‌کننده
🔹
نزدیک‌ترین حلقه به مصرف‌کننده، شبکه توزیع است. وقتی تقاضا برای یک کالای داخلی افزایش می‌یابد، اولین نشانه آن در صندوق فروشنده ثبت می‌شود.
حلقه دوم: تولیدکننده و خط تولید
🔹
با رسیدن سفارش‌های بیشتر به کارخانه، دومین حلقه فعال می‌شود. تولیدکننده برای پاسخ به تقاضای اضافی، مجبور است ضریب ظرفیت خود را بالا ببرد.
حلقه سوم: زنجیره تأمین و صنایع پایین‌دستی
🔹
این حلقه معمولاً از دید مصرف‌کننده پنهان است، اما اثر آن حیاتی‌تر از حلقه‌های قبلی است؛ زیرا یک جهش کوچک در تقاضای نهایی می‌تواند به دلیل اثر اهرمی زنجیره، جهشی بزرگ در تقاضای مواد اولیه ایجاد کند.
🔹
این نیاز، مستقیماً به صنایع تأمین‌کننده منتقل می‌شود: کارخانه فولادسازی که ورق تولید می‌کند، واحد پتروشیمی که مواد پلیمری می‌سازد، یا کارخانه مقوا که بسته‌بندی تأمین می‌کند، همگی سفارش‌های بیشتری دریافت می‌کنند.
حلقه چهارم: اقتصاد کلان‌ کشور
🔸
دورترین و در عین حال مهم‌ترین حلقه، سطح کلان اقتصادی است؛ وقتی حجم قابل توجهی از تقاضای مصرف‌کنندگان از کالای خارجی به سمت داخلی تغییر مسیر می‌دهد، چند متغیر اساسی تحت تأثیر قرار می‌گیرد:
🔹
کاهش تقاضا برای ارز برای تأمین کالاهای وارداتی
🔹
افزایش ارزش افزوده داخلی و رشد تولید ناخالص داخلی
🔹
بهبود کسری بودجه دولت با افزایش درآمدهای مالیاتی و کاهش هزینه‌های حمایتی
🔹
کاهش وابستگی به واردات در کالاهای استراتژیک که امنیت اقتصادی را در مقابل تحریم‌ها یا شوک‌های خارجی افزایش می‌دهد.
🔹
یک کارشناس اقتصادی کشور می‌گوید این مسیر نشان می‌دهد هر یک ریال تقاضای نهایی برای یک کالای خاص، چه مقدار ارزش افزوده در بخش‌های مختلف ایجاد می‌کند.
🔹
مثلاً در صنعت نساجی، ضریب تکاثر اشتغال حدود ۳.۵ است؛ یعنی یک شغل مستقیم در کارخانه پوشاک، ۲.۵ شغل دیگر در زنجیره تأمین ایجاد می‌کند. پس اثر زنجیره‌ای کاملاً واقعی و مستند است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/434957" target="_blank">📅 21:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434956">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
درخواست قناری یک جنگ‌زده از سازمان مدیریت بحران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/434956" target="_blank">📅 21:51 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdeaf0d546.mp4?token=NNySjUrtNb5ldhLLaBpli0rCpIKsJxUNY0OFWFk-m-PETWT2GFnOW0kVcoe_POS5z6EAwjAZj968m__KjD6J_bSoGaJTK4L-86Zry--DxP5LVgb7bZ9DE0MZCQIzTz3vQsvoLJW3-KRgyw208dDD2Ekoe9Zg8OwmVDhZodp7eGymX2x_ea0_aU8Ff43agUWmlcLRv6J-E8KOUrjvCwTPR8blkbzhlnMgaWEiHnboKpnUMhjUIWuSaub9ezpN2MUSA0sALQewovUtQUK_EnyfQMquD1ZmEGjVqBmk9aauTstxz1T_Mhp6TpYoA0xd6sXuIMwRW4a1VLrag5TzuieynneYbIVVHkHWYgIaY9UJcT60s5KNSBwpPHtxSrDCixgWgTu46GYcoLexSzvt3QiDxHJD1G6o-68Kq-Soa-KprRYfbftXXcyco5bn0Zg0fmerpVcs_Nn_Bwnlt5wyehveX1wtNAAiQsZ3gaSm6N0XKqkteynw3cAJcMq1AQitgaoCvt8xavvjGXRPpkBx475OOQ6aFbfggJ_9MzjYYxAWcRKgWNY4F3H_NUXJ_RMu_pw3U3UQROD7Fjvwzb5-N98G_EJCvBOk0zjOmE6bfGGZyupobI6DxjF-RLTTd4CQwUr5-Mqwahi-ypXHVwXJ8rQXPuMOykYJ7o_MbdPCU6SqnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdeaf0d546.mp4?token=NNySjUrtNb5ldhLLaBpli0rCpIKsJxUNY0OFWFk-m-PETWT2GFnOW0kVcoe_POS5z6EAwjAZj968m__KjD6J_bSoGaJTK4L-86Zry--DxP5LVgb7bZ9DE0MZCQIzTz3vQsvoLJW3-KRgyw208dDD2Ekoe9Zg8OwmVDhZodp7eGymX2x_ea0_aU8Ff43agUWmlcLRv6J-E8KOUrjvCwTPR8blkbzhlnMgaWEiHnboKpnUMhjUIWuSaub9ezpN2MUSA0sALQewovUtQUK_EnyfQMquD1ZmEGjVqBmk9aauTstxz1T_Mhp6TpYoA0xd6sXuIMwRW4a1VLrag5TzuieynneYbIVVHkHWYgIaY9UJcT60s5KNSBwpPHtxSrDCixgWgTu46GYcoLexSzvt3QiDxHJD1G6o-68Kq-Soa-KprRYfbftXXcyco5bn0Zg0fmerpVcs_Nn_Bwnlt5wyehveX1wtNAAiQsZ3gaSm6N0XKqkteynw3cAJcMq1AQitgaoCvt8xavvjGXRPpkBx475OOQ6aFbfggJ_9MzjYYxAWcRKgWNY4F3H_NUXJ_RMu_pw3U3UQROD7Fjvwzb5-N98G_EJCvBOk0zjOmE6bfGGZyupobI6DxjF-RLTTd4CQwUr5-Mqwahi-ypXHVwXJ8rQXPuMOykYJ7o_MbdPCU6SqnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۷۲ نطنز با حضور گستردهٔ مردم برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/434955" target="_blank">📅 21:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1478a217d2.mp4?token=dzgHTkicFFvWmYXqWSMteZmZwWZOqe6V0CaO7Jbn0wYkXm8YRW5oBfLtA00ysDOC7-wUNIHupslLKzKrUl9WYZR3MbR7u-4BrgHD1RulAa06ugOJlmZaPjP3ksNxi_n9yFGBMKolysuihRyKiqxyizcfnWIv5EkLgDDW38gV2NZTwEiOG8vchkNLZrOM-Y_3EIMDw02nterpNY-rRJmb6bsETbWvbNPKVRWlN6tCpQ-hWC9G2OQnl1T0zzld3g51LtZb5JzWsAjz9SNnSCbNaGVnMIPucT1Ils-uejYk4CobZvO5hYyXqSFUmHztEyllyVvaYqhMb7iMGb2XzeP7Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1478a217d2.mp4?token=dzgHTkicFFvWmYXqWSMteZmZwWZOqe6V0CaO7Jbn0wYkXm8YRW5oBfLtA00ysDOC7-wUNIHupslLKzKrUl9WYZR3MbR7u-4BrgHD1RulAa06ugOJlmZaPjP3ksNxi_n9yFGBMKolysuihRyKiqxyizcfnWIv5EkLgDDW38gV2NZTwEiOG8vchkNLZrOM-Y_3EIMDw02nterpNY-rRJmb6bsETbWvbNPKVRWlN6tCpQ-hWC9G2OQnl1T0zzld3g51LtZb5JzWsAjz9SNnSCbNaGVnMIPucT1Ils-uejYk4CobZvO5hYyXqSFUmHztEyllyVvaYqhMb7iMGb2XzeP7Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاسوس مشترک سیا و موساد در ایران اعدام شد
🔹
عرفان شکورزاده، فرزند جعفر، به جرم همکاری با سرویس اطلاعاتی آمریکا و سرویس جاسوسی موساد به دار مجازات آویخته شد.
🔹
براساس محتویات پرونده، نامبرده به عنوان پروژه و با توجه به تخصصی که داشته، جذب یکی از سازمان‌های…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/434954" target="_blank">📅 21:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434953">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عضو شورای شهر: پرسنل شهرداری تهران در جنگ رمضان فداکاری کردند
🔹
محمد آخوندی: همهٔ بخش‌های‌های شهرداری تهران از دقایق اول جنگ با همهٔ وجود در خدمت مردم و حل مشکلات و اداره امور شهر تهران بودند.
🔹
شهرداری حتی در بخش‌هایی که وظیفهٔ ذاتی‌اش نبود با همه وجود قبول مسئولیت کرد و از همه امکانات برای حل مشکلات مردم آسیب دیده استفاده و رضایت مردم را جلب کرده است.
🔹
حتی در شرایط جنگی شاهد افتتاح برخی پروژه‌ها در شهر تهران هم بودیم.
🔹
آیندگان خواهند نوشت که پرسنل شهرداری تهران در جنگ بزرگترین قدرت‌های نظامی جهان با ملت ایران چگونه با ایثارگری و جان‌فشانی در همه صحنه‌ها حاضر بودند و به صورت شبانه‌روزی تلاش کردند.
@Farsna</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/434953" target="_blank">📅 21:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434952">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPymjGaiWLU7jRgyNC-aJaEx3IgVLkZsW9Gk0ijLXn_4meCAMUc1cVC3ASOQWPkCD-rqSx_5tcz8rMFygf5CxOa4VES_MZi6BULTGf0MaTBLlcwW3kqxhV-1vz_KXpsfMxqVz5zQGp8e_bQ1bMzKKdD4xM30UKE9tggkf9MLh3fBg5dh7DEUuSYCF4tVI5KgIj5PjjMg7BoUN-MUqcUg24E7YfoLh_S57jOWXSB4OE-jspeBBHYPdeAJVpVZlWVDBmrU6zplYVB_T2LuYP9MFRRyBh98tBRqp5gLaut7XtZ1i_jd-xAyy_h_c4NhLeeesLPln8Wywo6ta1nKmrVy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر اقتصاد: انتصابات اخیر در نظام بانکی و بیمه‌ قانونی و برای اصلاح بوده است
معاون وزیر اقتصاد درباره انتصابات اخیر در این وزارتخانه گفت:
🔹
این انتصابات و تغییرات مدیریتی در چارچوب قانون و مقررات موجود است و وزیر امور اقتصادی و دارایی نیز در چارچوب همین اختیارات قانونی، مسئولیت سامان‌دهی و هدایت تیم مدیریتی نهادهای مالی را بر عهده دارد.
🔹
نظام بانکی و بیمه‌ای کشور در سال‌های اخیر با مجموعه‌ای از مسائل ساختاری مواجه بوده و حرکت در مسیر اصلاحات، ارتقای کارآمدی، بهبود سلامت مالی و تقویت نقش بانک‌ها و بیمه‌ها در تأمین مالی، نیازمند انسجام و هم‌افزایی مدیریتی در سطح نهادهای مالی است.
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/434952" target="_blank">📅 21:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-434950">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMg9_YoAS5M2KR6rMWIfIBJRAh35DIFFQ8ujveAuQ7IQCdtQL__DBxEh3wbt1ZW7blDGY0k30WXKM2qXatlvYcK96l9RY8mdP1CZv8y11jdI_VKUjSYlr1mY-rXe2_25l6TVfj-WLCbpxTvEPOXqUmsDsIQI6MvcrtSXkTW-2Y0VHA_OEI_Mr4B84XJqRiGdFIax1rJf1g9ilROqr1w5MN8S5-6iOaiNwZvdwloBeObQDG47uxXL3ayH-y3yp1-ioZWAjRJBKjEqzAqR6W69LksWb78L80rBsKjr0uftLp28fWlsYlfiCNhf6oEPZCjrgxUaRilcRvZjd0kH0Ernew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلید ۵۵۰۰ واحد نهضت ملی به هم‌وطنان قمی و سمنانی تحویل شد
همزمان با سفر «فرزانه صادق» وزیر راه و شهرسازی به استان‌های قم و سمنان، آیین افتتاح پروژه‌های بزرگ نهضت ملی مسکن و راهداری این دو استان برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/434950" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
