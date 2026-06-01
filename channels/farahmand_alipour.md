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
<img src="https://cdn4.telesco.pe/file/FGjqPcU8YOWPvUzC2BW673iYimNRvn0NOiupHOmJ0VpygdazpHf1X-CNjmVvhp29kZ6UhZAqNI4EGTLMYNoFg3CxRmE02N6yPWXbX7GNHUSNs5EAnd9IScbpvstDp5DMjqjGIQ6d0N0bYNSMBt5l7ShhXiTYrcK3O090dWM8Jc6mu67GT__Uzh4V81wAqMcNRiJyXp17GyChvYyzRWLkPVeneeC99Zha4hcjmUoK4N9x7bVFtO0eLozhpZR9nwfFrwethXCDjO_-Dw1P4i8ZQugeRf1iaD9DPe7pp-1kJAqzqfi7oXoMwu3sPefIMacQf4NzA3ky-2h1Gax_s_o1Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 23:41:19</div>
<hr>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTKFRwykCe81o0z4NmeRxflVSlrkwvG5iWbiUGdDBPhbT92MhhfM7x0Er5dNuOYIneXXc5Ios1I6nU_rkaRwzdAVv38g74lMfYj1JvUZQvj-yogTnLbcW75yN37v9RZMwbsc-f4AaCXFqspzRNOw0qTelLmM4D4OBaQ0yo1WXfpFNYS6GaXRFY4lWfdrROYT1vDaPrRs_YnJlFtbN-nyfCEx6Dxia5cAac_zdz7eKF7aAJ9afMcNtQe_ipV3D3clXO3rNc9Y6sz3PMZ9J5htKnsCfgyWIsKcyM4GgCtG3mXRwdOZDvk3T-_LHTtOJL-Yp8FDr6mJR1MKeakFE7rCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1t3qGLXPPYSYQDKG3Ik_NSEHVIvqehPanKbmwfRFvjKms45b_cYe95iHq8zzrNfcaTyrmQkPAt3hu72Agg7rlkfA-acs8cTMZlHBf2JQHFgB8yKMeXq7xjFtC7qMMus8KuJeD9BMY8m0QrCGbXkj-aL0ANUahM0nprOWmvmUMBinywR-dSjHGXheDV9ZpOTdbCoyDf7hPoJjxvqeMIS_yv-ZYhnwM6tT7T5TkWrruCCSAaEiI6Kd2kzh_gPFFrB9nEUFo-JnGX9Z6nJbHy3fdHaAQlp6eK0jEFwRrhPjLdjD2UlJWEtrHValaJ03AzpklYAK8fHtjylOXWJOfBl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qolsH6FJvRRzcI6L-9qb0zFud1_weD0X_OVRMbq_g58h2YNPzV9nAtyEpaK05LnG9zvbXcY-vItP-MWkBnX4fAo5lvhgV-shA4egWgNM0eNg5q1u4d6h094rU_LGUu-YJQAEAfNfLcku-uS3Rb86qDBWWDiY1t9UVpZ6e_XJa3WtzdDFJSLJxREenm3U5556OF5WaW6pJuwX2eWJf6O31D8wR3U08En3USm81BzJZzpk2qf08Z1WryjJzkGjJ5tMNGpPDRgWmdf0JnIM0ezFCw7XkjLcdUocKX0bQNZqwabFfsOEQQlZUSd2zdN1qy9Ew7ut_NFErYfNExtvj3UFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lmtbipq5iTdA_OMWYYaf8NHjMIAekO2qYldJFEGacpxvUDQcg1JVl2_fYSCUpByxMhC4jFBqg2Dli-t5lNnGX_k957cfOjEqHHsWkafOHkwND-7tbvW-ANkZ_JDmThEQyc3kj17TTdDFv7R_hTR3QCGZNlExN3PSukWGULKHIYGQFlC15q61LM1uBc_iY95wQrsyK9_CYYLshItyPO-0LuZ1hLd3RYB4iWC_cdq7KmxceCqlMay36yCfBGYcyekkqbQ2WFKt937owkM-vR-dVovNRbz0yPvdrZPDZazq39LV_9DWKpg_hjEHH061RYrB6rf9aCjwqYrup4h9m3q3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRxQ3GL7Rr_iQ31_xBU6WKXq77WPnD2KVBpPWidBnZ3-_bZ0BCutmvCjfcTPcDa0sn17yredtD8LOLYs86bjnNGcnnqToFZQjQdG79tqZMzF5kblA9e9BUZPSSMnXEFruUTXI9WPOoE3-lMXmWNviSXAWIdCaa3v4MkvkIacEEohf9GcUBp7WoWUhsrkfZIwV2oeewA1IrXjloYlEnv1bDw0n-2Z9Lj1syRJSRSREomGAzukEOamqWpwbKpj2CkCoGE0YYL9wO6UGBlg0buxVYj2B7t1ko814onRaf-Ae6xeOTd4m5k6nwzwl0C_8xb3MN4tW_kmMjxXqOL28N47uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRDISfWdhFTcQ6zutISdPGBmHwvYeyOEil6XtRQL1PXdOnI_-ftnJZCCd9aZihz0TsG71O8CtTUKbr_SJQnympxndG5pmCybMQUVw8kn8GlYayJ4Rf9eeQcK1bSHDF50jUzp7L4jKYhKks86BS7TqTfi4KCUp1o0mxpKWHZT0CTvNQubVnXPUtvdWmznTwfTPXobGtF16zPsxawC4kdCRtk6bDtu3EAmk7uaSY83gXwVbbbKhbggu3y8x3FE6-dZUOrEsfWn8uZBuA7IEqXMHvgxz_b0NDIjV6lJi8HFg7JA9a13_xkfx64rGsvrY2F-w3gVRIiUS6NPgwLv09ffCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmoBdfJ3Eps7x7Up04Dk98WrE6w24RofCeMmBpfN_mLWfCSBOI2S34keQkt7jmKx85mjChOdDhSnfe-GYhaCpdOc8z1VcKBjyKEhFJjWLlEllrs7veRRMEiY-dv-a0vU4XaMpKDR0rmaPiAM1-jof2TL_IkwxdfLdZF7pd9TSzcWL3t893EZ2r6Z_JmmibfspU02tOKehoWqpeRm4i4ObLOYAzjS-0zJj05tiKmv-oLLt_wwrTb1rk2xYanTvC5jDPVTlycaUoS17QcJvuKM1x1BemauNP0h3am225WlxLUn4mJC-zlfVaCrxKnZOpC33OJ31O3sV5gLyM5ZJdiZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jdo3C-aUBNy2EQh2ybAzt69PdBhsCa3piHHPiO2kHMTTUDWT2k50xVHoksZ5Qvp51BtWDFUTgnRS_jI1sB74NHwIgpX0UVvX0_55jfHBXomi_frzujIxvW-ZUN76GVsTfbOPq5AZTt9CX2EznxiBjNY1RS0Lm5YoAPCwRaDL6Ay7GG8aRAb9HMOOAEVQLU8l33a1Zsu2t8ncONXu5PJE81RyPWYkFULnzZb7SmPhZZqK1Jo9rqYrUYbIL7pjf3l9xE-L8M11d3wEuAqo793cFyY2jKX54g1JcwyPvlv5Vj0x-cYPyKcnOkDwsigFwVMj8fEmxIlvSqYaWpJQkItAXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ofRC9OrhP8lB_2HR-rgwYj4qpv1CD4SMoNa4SdJYCRQ7CEbqrZ0A8Gq6vn7MJzEuYATVevKd7yT-hvfsBIMtetWllF_7YNtw2Ppx7cFWQ8y2uKXR_JxCoBNda7SkV_QAHGueA1-zyZXxPvqVtULruIghOBPrMSLf9qFcLBLxfxYVrQxBGj_NKNZix2CbIpvhZisKuDkgpF2-3x9VFOUEqQNp-4ZZ4N8LWFDCGbXPbLjuCATAaPut6lDeadHjn59qrGI47UfBwSDk9DMxQoXkNx8PU3FNwkRsP3f5qx4dqCGGSirBRCvosCHjhhBx2IuxGIlN7m6yo8zCNVkC7uNv_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ofRC9OrhP8lB_2HR-rgwYj4qpv1CD4SMoNa4SdJYCRQ7CEbqrZ0A8Gq6vn7MJzEuYATVevKd7yT-hvfsBIMtetWllF_7YNtw2Ppx7cFWQ8y2uKXR_JxCoBNda7SkV_QAHGueA1-zyZXxPvqVtULruIghOBPrMSLf9qFcLBLxfxYVrQxBGj_NKNZix2CbIpvhZisKuDkgpF2-3x9VFOUEqQNp-4ZZ4N8LWFDCGbXPbLjuCATAaPut6lDeadHjn59qrGI47UfBwSDk9DMxQoXkNx8PU3FNwkRsP3f5qx4dqCGGSirBRCvosCHjhhBx2IuxGIlN7m6yo8zCNVkC7uNv_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu828bLFPXf7z-tcJe449HY559hg0RUwyXlDRmQ-BKy45KaQaUk6EBQr_W5eW9NtALOUsWc69dnBpQe0UiYTUQQOirzA3kn6fm_il65NeldEDSViolkUc3gJgJFX3cYDbnqvJVCe1sX2Oww1JOGdktPYzxnCVwABUXmO33q9BVKMLZwMdNfl0m2gDoFL9PauExbCuUt17gFfOukqoQwBNPyZ--3mcpdvW_vx_9K5-N-OFrF985HPARJ_jXaC8Yt5Yynb31ORw4EsnXwLVMZYDA0TO4iaJCo2_xV5MGvJzv03A2x096ukvjTe-K_0UCJBjipnlkyEE0HZqr57STgkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=YgbzeGn1qQ0o1qYU-Ke_qh4EOQXvlspelG8atwPESOS8o67qvVOwmXbjivXyNWuQ8q5S6mrbKS96DBKfKaZR9xC2161GZ1T46amFISPZfCZAeDK2AzoPrC9tXWfacPZ5mqYVq1AJe0CTGTnyPZRlJbJjFo0OvmbBwR6J35BipZBwNfi-Y7-haLpmnBjLuLSXMjSocZZotJjnu4TdyHzw1xx2t_YcdcCiLybIAWYcrdvGYX04F47u6YQDB8y4gNQ08X-s2de4P_2Wr8xNe0M7V8aCvZDEZmpObPtknHhTzxWjq3goCfwURvjA-3kD10tILarM3fC2rFzBvG24cLRQQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=YgbzeGn1qQ0o1qYU-Ke_qh4EOQXvlspelG8atwPESOS8o67qvVOwmXbjivXyNWuQ8q5S6mrbKS96DBKfKaZR9xC2161GZ1T46amFISPZfCZAeDK2AzoPrC9tXWfacPZ5mqYVq1AJe0CTGTnyPZRlJbJjFo0OvmbBwR6J35BipZBwNfi-Y7-haLpmnBjLuLSXMjSocZZotJjnu4TdyHzw1xx2t_YcdcCiLybIAWYcrdvGYX04F47u6YQDB8y4gNQ08X-s2de4P_2Wr8xNe0M7V8aCvZDEZmpObPtknHhTzxWjq3goCfwURvjA-3kD10tILarM3fC2rFzBvG24cLRQQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=LBNE1BoqZfrUT4bq7nDoHO6YuzfS5HOSqkXqiXzuFoNqoQSEpy96gP8VSJ8R-_OxbQ2ghl8POA83h1KK2e_5IssyIOP3obpDYbt8qfY289ucsd81xFOD0gyv8VHshy_-_ARZGLir3yJ-6uLWPlHK1aMH-XGNO3F7MmE7pPn3adZBU52FFQPO26P2upsjQ-OcLtj43IhVFsLKghGhXgCn7Pn3B0sBa_P0pHQUTW4MpF546a59x0svhkmCbym70axKAalBAF3TITYH6UHR-_ycs_gNZKIcI7O11nmWg_oOgHstQOHJ5pk9B41zkdf8Gn7ElfwylzssLqS79QMDstRB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=LBNE1BoqZfrUT4bq7nDoHO6YuzfS5HOSqkXqiXzuFoNqoQSEpy96gP8VSJ8R-_OxbQ2ghl8POA83h1KK2e_5IssyIOP3obpDYbt8qfY289ucsd81xFOD0gyv8VHshy_-_ARZGLir3yJ-6uLWPlHK1aMH-XGNO3F7MmE7pPn3adZBU52FFQPO26P2upsjQ-OcLtj43IhVFsLKghGhXgCn7Pn3B0sBa_P0pHQUTW4MpF546a59x0svhkmCbym70axKAalBAF3TITYH6UHR-_ycs_gNZKIcI7O11nmWg_oOgHstQOHJ5pk9B41zkdf8Gn7ElfwylzssLqS79QMDstRB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDt9Xz2ojJd3VEd6382cXrw2FqZdtGCX23CDSmAWq-pyVrvQ5gc0Z9P0u6gybZ2pf3vjurC-Pd7B5Yp0VdA2Bza0JzHfrJM5H_HeFxf7Ls3KrKimQkl-v5XcQaIqtMWon9C3HiTVREL6_OsD4CNovy7Gz2ycduzHJf-RrRsLEsfn6hhAO6ULlAvsSOXpfc3IJMsFfi_kP8AN-32oXggerhaQUR0Yld1Ezq-lz_OIZKADPNfrijJP7GzIUPNNEvXm9x3s5ORGYlrR62SneUdPRC57Y8w2SElnDcNJevLjldk92qgeMNrhbFN47iYoTbnygSdYdx2iAM1hJu7Ta5LE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=urkoZdd6dU0ywLypBHalpTb1juRd5oefXk50CE7pJ4JHrFvqJxoQeEwWcFc7jv0kfcUUj-mnjh0f3BC07za7ZUZSW_shegh_Zm7hHKxkCRRUxyPdZv50l6NwC1uxAZ0O3O1--NzatBL97kVeY8NRkzgS8jAPS-QLOuJ6gRpmCQCfKbEn1LdO6kpjixQ7NgT3JzuD1w6FRrxxtI7NTQZRed58emJjQQAh2pJDPz5vcVWS5BjuGD8JktFjExQCCw6UFUwFm8TbOikzvugytNiLBw0Eu7tHxVI1nmPKwe5l-h8oLS1VHS-PkgDL947zuXsrHnDEORod1H-a8I-2WKtWuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=urkoZdd6dU0ywLypBHalpTb1juRd5oefXk50CE7pJ4JHrFvqJxoQeEwWcFc7jv0kfcUUj-mnjh0f3BC07za7ZUZSW_shegh_Zm7hHKxkCRRUxyPdZv50l6NwC1uxAZ0O3O1--NzatBL97kVeY8NRkzgS8jAPS-QLOuJ6gRpmCQCfKbEn1LdO6kpjixQ7NgT3JzuD1w6FRrxxtI7NTQZRed58emJjQQAh2pJDPz5vcVWS5BjuGD8JktFjExQCCw6UFUwFm8TbOikzvugytNiLBw0Eu7tHxVI1nmPKwe5l-h8oLS1VHS-PkgDL947zuXsrHnDEORod1H-a8I-2WKtWuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C46BucGKvu1j4SGJcUhej_coZy6R2NefIq4VSITbUVfLmWusUxzoEgo8dy8lKjwT7vKv7DR31qIACQnz2IWOScyZnVVf5CbOZuwsXwrX57jqdPqBC_rcnPhSW4XVQOshPFuWwdQqDO2fQ7j0SWnxfpWgyPNAxQNsECbRErtEg3K1xcD1K_mupxnxYNMWAeuwJOudvo9A_8SXiwUy_bEZXquEVZ6b7cTRlq5YDT-t39f726yQJvZztKIQ5pzLxJONc3eAAPq5RXLrlueXQVDnHIZEbIDCT1IMa8bpc8uPsBp-_LiVyI6eR92CuGmiF_563lxvPh1eehpG-BKLiIODPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqA0YJraytWtV6rAzmAWG58GdXEVQx1-Nr8ruktgtnljgq0zzjmJiffUgb7-gwV8yUZ9FH75MEneitnhqZ7sOQWlgyl5f8981oyifM8_dk_35Ww2Mk5IvNFsuuM6RgFvIeBSkEGHxkQXXZwQy7UCaXjtUtELMTvekkSNphqZ2CzxbndOP5przQERwjLT16alrZhV4yTcJEQtcaP2NSxEgmnF8X9uTMDSIwUIFrGT7XN1TcF-Ke1R6YP9HUd2ozpus_WjwEPnfz6_lTN5j0TVnKoDWWWdrMEtcjCYMgz0OaVdxWeWU4HF0LvC7iqPVXhFNE9IvdPNtoPYbrTxwghpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vICGXuPUDPh8JQMFBtsUus_dvTluoXs8WbtUfenIIotlOWAD0vhQ7YW6b-db-J9QqKGQxd_WdTIE7nvBYq22E5c7PVXhfob19H1DicyVhVagl1d2a5fkcJuJjIwcvxD8_6JZitBfQ5ARhlzIKbYpRIaF5wBgyzoy5L07hHB2CqnKQQa3EpTBZMf5OY5-z0RWYfkPTRs7B02msp_ebDbIxzvRVT9p9QAN7_UBkyq5hRclrke0TOSq_XYCab1D32HuJ4HQf7AySgBrvzQ5amu_vZDUqnUHK44byvYZcArjZBNt6eWTCqEHCIeg0owUr3zub8-taDn620yjGn-AaWZ6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPLt6UQQgh_ONMtnveA6lz-ZobNv4L6o9Gxww1JoZW3ReqeBiWY8OWBngkNXMCAUVSPggL4q7YZ1_h-wH8cUx2zkgYE0yrvUiJ2DsDbGUVvNXdcrbOS4ym-tBzQ2lYy9UotvNAHSMcqDX2hzbSS_Mo1dLSvN4ZfCq0DmW7aip6IB9BCwE3ROW0S49lpirT0UmBIa-RnSA9alomhkMdyfXNg4NkLnfPooDuiuKVgQ_-0PFJfUArqAkm94YWPW3Mx7rXxmBA_NdPEfIuh3I7qDNbV4aRkTwFRCL4G5Usu0A9jKW1F192n1C_t2kzTukfvtdwfiPoBLgn966-vsObuPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_wzD3-T4oMKT84Y1RKZxSCHORmajjTGwOCx9eHwJSYefl8Sunzg-xEccxFOkqkv-XcuL2mkfc553JKU0AMWxgPiwhUcEfUC6vySqDaLJ5N0bkBen2i57eHOaqFkTzRYU9BK9EM7hcizaBiLEaEwosl8oCc-NbgcT59B3h_HeG3mJ54S5pczBdknVc9FziaMPUgkgCPB039fHZ6ZlRLhUcTBqd0oqS4vPwPJsrJqs8E95NrsYc7iatIvLtrP9IYtZnLvu690MUdWeLB2VzrS3GVrsoI2WuwpYoUJYQIJoZG-sAQv-Ry6JwJ9CA6qOE-0JsGCZpv7e6Jel9T6yLkkOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJdtooPVlTq7K1JjryQaoHdFhYUsioZ0Po1AWwkmU_CSjyD_ESb79Q_bC6bpvc4jaVN_pEqhYaZ_Fx1euwBwl9AgT51Cz5qn3EINcK9I4qUgdUmYuUfIyyTLmpLDWPoDOz3FsZ64ek-481RP3S942uZp7EGqbAWUva4xaCC58GK4peCvdyXBQykpD1gRHg9qpa_fSF6RAuXhpFPAjU9ueM3Vsel7Et5h-4T0M0BHg2G-UV_Eddf9xFCdVRyLAKWeoNaMHZdF2xLYVlKX9vT_gglnZafzpI9CBBS_73QZxEElDNLDjdr284JzFTGrVqNHK586XH5itbWp_oYavnxwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZzX5rMc2iI9vQoBYblF14-jay0eaJ8wIDsIt0AoeuzyLOpU_RCpQWKx_ggWWxh1LXEm-hgqheQ_ujTB6NBNZVN9j_0ea_8ddSWUUBWRKGHxuKss6NZA-i9lqTGygwVGlIcNr-f2oz8W_YFJW3Js5ql2OfAZL6AH1d2VzL8fyfOLEN1fzlwkAO6wQUz_THfCHXkfOtBAP69BhJJMndWo8r-OD5dBwuYt-8wHqgaOSWJ-5I8UohHmTGwRrBJZIl6CmjsTzl7ryU5XVtGt8g51FzsvlRtsiS01WD_EaKN1sFOvgnT4ANnyNyUt2wHAwjGsXxwFioPHZ_S_4ZoCPCen4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3YJyqyGK07xLmU_RYPxQFOkanKZb9ufBQTRjLEqKXjYjizxc33NkoP2HN2f3OVj0j3rvYBeqGeHe4iPY2sVkAmg8N1xio6ievyqvsJeUSuNDRhDbaMxvW8bimWj_JGKwuipVOIASFIZ5AbNnDazM9cZIIt2Oxe5N-v23XS6xadfE8T8EWuLg1aXjNvPiHQCK0jbPnOP7gguunoiVv8ASDPocVyI4z9Cy4khWZ6nC0svw1zrkZt8uUJCKRf6QxHQDZH7gP6h2pDLo3TAteOTOyLyTmeXZpdlEzqlDE-NIZe0-Znfc8y_I25vGNDI7cUeAO1RlBGPLLg5Vn47SDnXPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=iSjAmSOis2MYvH27IcVT8iTU9shF3C08fu_mKcQD_3Jxf6qI5xyCBUenslyrGnp2NdrQZ2FJnjp6S7xRmuVfnufVNAVt0GtKYq8EL5qVYyWi37grHrjg5TvN7FWmLa4HzMEcgNJ5I6sZpccyEwulXtf8RTBN8unGUWdjjKZMe60ZdYJCRbbsWZdD5re3JOiSSKQnjmwEnYAGV10xk6eVQmyFVUy0jjgSMy92rd1cHk9-GFAAXY-9kKkJUz2p1AWqgwxdnuelhuTgVhf_6LPx_-iyHUvGeQqa-tLTBCQbLhjZICSsu-sI6R9WktBHvaNmO_ROzGPAMTiBQDQF-HDaFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=iSjAmSOis2MYvH27IcVT8iTU9shF3C08fu_mKcQD_3Jxf6qI5xyCBUenslyrGnp2NdrQZ2FJnjp6S7xRmuVfnufVNAVt0GtKYq8EL5qVYyWi37grHrjg5TvN7FWmLa4HzMEcgNJ5I6sZpccyEwulXtf8RTBN8unGUWdjjKZMe60ZdYJCRbbsWZdD5re3JOiSSKQnjmwEnYAGV10xk6eVQmyFVUy0jjgSMy92rd1cHk9-GFAAXY-9kKkJUz2p1AWqgwxdnuelhuTgVhf_6LPx_-iyHUvGeQqa-tLTBCQbLhjZICSsu-sI6R9WktBHvaNmO_ROzGPAMTiBQDQF-HDaFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=fXKOarnhkLCpDAAy3ohH-2fJ8UjATW6fq9zJT_GXusQG-Dem95UAmICBNDGugdELZMkSHUymde98MhPJsKgjWiaiawdWqUugws1GKb-vht5sBaFIy1j2Ay_HJgQw7rg9-jpJDwKWXsI2sQptA-1Lz1dRYYrU354WeORqsWZ9O0W-RZFqAEMJOTjPbBwss-Q-vPOHLK9RtSAZO6F5nuhNpC6kHXQCcF_1VXnUwoAFMkBNy650gviIeo7-AKkul9zHVVk4DcmoLncU1yDvYm6P0FO3SUk8HaxictM0kni6XzbGJB9X9SaT5f3gXl7LQ5RySUWrLuObf-t8r0upy2pOyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=fXKOarnhkLCpDAAy3ohH-2fJ8UjATW6fq9zJT_GXusQG-Dem95UAmICBNDGugdELZMkSHUymde98MhPJsKgjWiaiawdWqUugws1GKb-vht5sBaFIy1j2Ay_HJgQw7rg9-jpJDwKWXsI2sQptA-1Lz1dRYYrU354WeORqsWZ9O0W-RZFqAEMJOTjPbBwss-Q-vPOHLK9RtSAZO6F5nuhNpC6kHXQCcF_1VXnUwoAFMkBNy650gviIeo7-AKkul9zHVVk4DcmoLncU1yDvYm6P0FO3SUk8HaxictM0kni6XzbGJB9X9SaT5f3gXl7LQ5RySUWrLuObf-t8r0upy2pOyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=EVb0MygjIoTOeJxymVAYDTp5dldH9gAEaP7JjBRlyLEw0q6Iq2wSVqSblYRKqNtlKUTmjYRjYpkTER5M1DPDA-Ww9eCI9_0Y-nEd7qz3jK1dN3srLcff951YCocFeteOSuYWuZWM2p5PZBK4WY0aHaKaXbnLHnWdn4q2OzuU46SxKB1JBZ6cx6fNsAzTzd5d6Y0IFRF0R9g-gbaFgx7A3QlAV83TEkezJuKaf_HPKgMNNoEA7EvVTU2Gd_eh_UAiP3jW8xxnsWeqBwZYseM3OPft2SdDgx5fBLQBdlBo63-EGDkqvBHX97oAo3-w-vWrPE9mod9Wl63ZVd3lA63S9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=EVb0MygjIoTOeJxymVAYDTp5dldH9gAEaP7JjBRlyLEw0q6Iq2wSVqSblYRKqNtlKUTmjYRjYpkTER5M1DPDA-Ww9eCI9_0Y-nEd7qz3jK1dN3srLcff951YCocFeteOSuYWuZWM2p5PZBK4WY0aHaKaXbnLHnWdn4q2OzuU46SxKB1JBZ6cx6fNsAzTzd5d6Y0IFRF0R9g-gbaFgx7A3QlAV83TEkezJuKaf_HPKgMNNoEA7EvVTU2Gd_eh_UAiP3jW8xxnsWeqBwZYseM3OPft2SdDgx5fBLQBdlBo63-EGDkqvBHX97oAo3-w-vWrPE9mod9Wl63ZVd3lA63S9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD2izezkh3SsjfFL4hMyqNshYlXqKhUbsp5TeKSslaNeV5mMwUze78g55NfAnk3-W-7kqTD77Sc6e6F5ZKNw_rt9WUjhFcxxVGRlxgdIdaAOUbbP9wbXfV-5kk3c20sHeSSqUSptc7mY6pe18S1zEoI_R1uXlp0pE3QxS0ur0zj9zSwSQkchb41zvri84EWnXcy7Hv0pnyXvCl0m1QmIGc-qeE0SOUWGm-72Mclqj8skIrAg8H87tE2QHmL6x0Bl261b_3I27JLtiSED3qt1PBytFYNxNezeoDLu6N1URGhsXj5u84DcTkb_KSWtEUwUYeSRhi1LG7zHCdXU-_r1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg9M5VlgJlwY-CP_UP8DwnNtnxihQ0_2aa2UeYzhRLNDtYTVPlo0hFpcG-Xum0eCn4PBU3W8Iezx-Ycd9M5HUmpxEtd5gnjFjG7edEzIcbOHZ5dbuQF1ybPopII13UpBIHEvRVOUqlg9JFoKB0bwfZkbgMEGoJ4o8ogRbJfG403BciZhh77N1u8mcaCNaDI3rDuDzSakgrrsKOFDjl-eWVHss0s9Pp4Tc76Xwhcsfp8MWbkwai7GPfByP9VR7MH9UdxGBNwcYjXOUJSdw90Z1xdzqxTBrhPFInkDMPgry28B8fm1KotNbiHNyIJYZcFl4SfJiqsQpQXL_GArV9mMgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY7QVH3sV49-ZnJfP03mJHVha_lNQbhTQ0b7tq4NeHTPKXBrAnxFrve4InKPQ447S7hczujRUyT6pXgWTCxtS6J8Ewrph0C2vyzvW8lz-m_VwZfpieRR6Oi2aFiFxpHcFFjOwbxipZZjdeFDnYID-mHpET0O7SSoe9QLI078SCVj2lsXTRamMLE79LBKSArSWaIpj-utpd9MosYKgCxLO2gAQX1mjLpqAhXyyxJZRuyPhoWdIKPsyyE2r_6WB3R7s40WYvu-TNdEthGEUBXw2zglZ-16QVo7pbvmt2R21wnPr9Rd2b_r60t1IubgoIWhqRQLJcFY4Dtrt8fY35O_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlKspgm_j52NvuYvUkJA4t9lNK0xS51mCrqggvv2qTHrOzdqmdSeGw8iwC5w2IrgKuxLTfPL9cEFRfq1WzEKCG-mZYW11s6mAinb0qJs9gZxK3g0w7IKly2tLPgOYJ40Pa7G7r9RyCeuuavqOcMxc4t8j8_YjuyU8zwy39B-aRYFJinApV0qzNyOEwrlDKDeGT724XPTsf1SnO5U033nxhAqDDeJyfTHmYSwJw-j1I1yDaeA-tPvBMJi2ZT8g0vtNupwl_BfGq3CJMQ7kxI5NS9tqMyRTLxliCHKs0VZGQJ3o_3bAfhdSMXwNUXqfQIlrEjKecFedzxuRMNpVyg8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=ndzGdHMr51x0HwTEzwjtvsWohzh-hxnTJpGj2NWGifHeGnE7dSsXg39xECvFaaKSNVobR7J3PfSf34HhyQrlIGd8Bj2AuU9XEO1e0xd_BNkB-FjfY3m4jDwQEkaHUtABYRPyL_rU0Skdh_RvJaaQbic9uh5ZDcvSILGkSfL0pSfQFqzt5gxWbOeuIG2zGAIF6ooUxFFEnfWX_z5OCJVuQ7wWqkcwEd_vAsHCvG1R0gH7fXM9gLoI2gf8GBp_LEuK5yz0GFl2Vc0QjA5EO8RFXqeLWt-kePufo8lfwBEETtQujzy1-fk5Mnmg5l8H1e6GfUPsQkVkjm6lTY9S8hBnfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=ndzGdHMr51x0HwTEzwjtvsWohzh-hxnTJpGj2NWGifHeGnE7dSsXg39xECvFaaKSNVobR7J3PfSf34HhyQrlIGd8Bj2AuU9XEO1e0xd_BNkB-FjfY3m4jDwQEkaHUtABYRPyL_rU0Skdh_RvJaaQbic9uh5ZDcvSILGkSfL0pSfQFqzt5gxWbOeuIG2zGAIF6ooUxFFEnfWX_z5OCJVuQ7wWqkcwEd_vAsHCvG1R0gH7fXM9gLoI2gf8GBp_LEuK5yz0GFl2Vc0QjA5EO8RFXqeLWt-kePufo8lfwBEETtQujzy1-fk5Mnmg5l8H1e6GfUPsQkVkjm6lTY9S8hBnfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Ugdt60nBviJsHBCf-o2BF1GwgLoH7cF2zFNTWfju4Sr1iEL1ojTjbrsA5c5G4ivAk0G3JgNujeso6Sm4YdWzP9dGjNHYEjWAPLDB44LSWF_DlVpQxMU8IDJCEfHu2Wzimep6VD_BUV3cYGKLAvyNbK9-T19ZI0bHhUpmW2CzlGleLeoBdqrnAvqrMn9XEtkZOKvTAtq6oFS2P_1t42S5ss3XH27FpyvomgiULFAxA4zhEziObvhsvXI2Jd7UxjqBj9igJkhzeHk_5mzC9lEtH288pevfnXcXp5zYh1ow0DVoefynUnEfDwnxbIFtbI76Dh4ItLZrLfXecXuTcNismg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Ugdt60nBviJsHBCf-o2BF1GwgLoH7cF2zFNTWfju4Sr1iEL1ojTjbrsA5c5G4ivAk0G3JgNujeso6Sm4YdWzP9dGjNHYEjWAPLDB44LSWF_DlVpQxMU8IDJCEfHu2Wzimep6VD_BUV3cYGKLAvyNbK9-T19ZI0bHhUpmW2CzlGleLeoBdqrnAvqrMn9XEtkZOKvTAtq6oFS2P_1t42S5ss3XH27FpyvomgiULFAxA4zhEziObvhsvXI2Jd7UxjqBj9igJkhzeHk_5mzC9lEtH288pevfnXcXp5zYh1ow0DVoefynUnEfDwnxbIFtbI76Dh4ItLZrLfXecXuTcNismg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWsg5CH57JsCO7pBHtiMQLVwWHdsWBnFvWeuJAU0KEKoj7JSiaACaGlTqFA1j5ITCAjovkFJhmlCvYsbKvbSjMlgrhT_pJZQcs8eO8j1_MHWw_atG0MLv8k_hTXhPzi3jgVAv8ChNb3j8-RDRqiA9ZRPO6HCLyI7Yugy7nOKxHLIC7vxFsuvGvQD_tMsAFtcOEurt5wUvEqEzl_YcW8yQOJ0aBIsNe17ihNf826JpDxRwFH8uw-n9gj2ZJkaTdj8w8LUsNg-qgk-sTGxW4IL-P1e10yXGLVcTJEtdgMrrYSrToIyuFG3GhCjkgXQPCrxHxgnIl2_Nwe1WjeWOaL8mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyz9LVrinpujXEWBlm_EcQNQVDFCytuHWRkOiAU_lbNxlYl5B1vtG58eIFg3PWKU4Ysj13TYJeGYnDO3Ihzcc6rLANaerB6lGQ6I7-lJdr5e9FyIL-5oi0gDK7UEB83JVXbXdHnTnXYIMuJ_lo2cV7Dne1m94x4csvfIfktsjnUo9Wq4fMNdWSxqDkBsmxcK6y870tY3t6NhLx7k9pS4KiSoOmK_xmBn2GFne5WBVWbLnZBN7GCly5sQShKN8QcTP4ord-ebcJGwwuL_sc4_Vmtxr97CovkVj2WMl4WLJZPoCJ0WQ45119n5qHZ7YOA13JHQaUOlOwBzjW-FlDe_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXntvwWB4-gbzNyrLFAHn4Jvgqk9fMMXwswpumOYNuBsGMsiz_yHFdGrVbp9Mt5OeUHI2XbEuOBoPNwm5EjbBiFrgsp_zoZOjQmrsm3fKyirQVI7HOGbo9ioKbguMyg5jAsN-4qx2FpQDLDvTsoH-umMGpxovDJwyvFk0pqO2-pca6392AB4H0ARFWOh6Zq_bAOwyNe2t7J9uPq6dYqNwTCi8SdmAiMMbiHuT-eTkFXmVXoOxiF7OPxE3Ec9HlczKrKFBVtQoNz7OHvxnNKu8kE-Ek7VqOzo9hHibWKOh2wrQPJPHcaSuUVhfNK7K7nW4QziReJlLCKSBy3S2wLihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHznKjkq9VgQbdlQG11k7qOhO43hIRhWjfoZRzjBLBcLyAXaHRqixLGsb_DVHJVKsMh-dF7-gA90ZziGjQ7S0QYQ0zlY26iwfq9Mhg0lLvAu_l8CMkcpBMgS5IGFcPcxGN6ZYE43_IKoBmNT0j-CeXnbU6OidhjsmLXkJ7O_HeTcsNmg1_w8EDQmIm3jjuSYSY_Syu35K-VVer9FKFfq0MbGtix2Z1Sc7JU_ABbdZNjgF1YAiwtvga5Xc9iP2nBqKT8NRG0kJ9vCn5R9aNUKhXYl6gex8duONtKEufnuJHXu6NpIZso0qi5bXcwKvPFTFR3RsU6dwX5pBh1swqxhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdB3hQFiisT5n9qPAbdbGfxBl-BbhHkXoYkxjH345j4xu5nsN_uVMwqjm1XIcpY5ohi7faXoa_HLI04r6UU2PW2-b8zEap7zJdxgI0aNq5bsfKGwdIw2Mu1A8L9S4LZhMItG9g5jnVCewCFFWJqvEFWyFQXSbtFbTCvByr_xoknmVQtvq3M3RK-qZQLwJhfY8-vllJ03gxi6smA-WektvarytnO-S0MtzewPYeK_0NYVhosVW4M0V-2TMcN871TqIl-AKkUUn9HxSHvtDXQOmrrRAoYhlsa5XYoVtqFzzvGLfQJlTv-FT5FooCcwZV3OMhoFO4dlVO18sw5j9Q4jZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYAdvD0pAoP5n7FFy45v0lN2p_tR5NLG7aAbC9LtvnMULwe5Ucj37lzxx0zJV7NFJ5s_8o2YG0YBKUznJCxb8QqYAeY7md-CjIfNF0LDxlzQCCANN39AHZa8Yh4iIEkCqmuB_YyhAdUtrVIEPL55TbZixR2lH2icW1baF6OzLyNeH9iVQDI9cXYEVSlE-1DJWjUNGt3LFxPUyXE1ApTEGL5ZlJJHOTkmwiRfPzAp3URDsPIhL342OpNDYXf86n6wMEn4_o91zRdEhznCc1ZywIULcIKiPmnFvLsxD5Ap88BeoSfub8ybek9HU3KU2DVGqR_pBsZo-tevisktOIIGHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTpbHQjMNYxp_QsTvJX-rxh4Z4FJ4TCr1qp6A_-y9mlI5RTgkp3qgO2L4SUNBH6-SIfm9G3EdJ2dIIj3JlJTatvU5P-8banAXse4fVQplDeRMoJvZCrrhjPrMkVA9Ls70fuux_koRTo3QF9gpEHz0nUWnZ4XhZ55BOzTJQ4rMaNlyCeLZdyn-mT7r1qEvgllfjH4Mvo9Le01Kcisp9IjPUZQyVuW5QrOSEXpu1JVo3j3DDo3oK-PMIakAfrVePU-12aPlJMLlEET4VHvEXqX0va4Ap_m_JgoDWD7YLnvFOD9beF77Juvf1l6YvL5luKPrcOlzZsvYPncGWk43ZCPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFa99dHH8pWqep6AeFVPh7vpqsVhAWw6REx3vYqNscrWPon7wgHMPzAoo3yDMf0MHT8xmNe7fsfYgFUhlEYbQCnXpgD-CuwSCeP1ghA-op-ZlmfZSw6TbkG2K4x11EAUdI3Dc4NW6hXzWXYq3HVEBxxziCwBgIbVnX8PBmaAKAl6bqlEy3FsCKvJAuKTtTP4OC4FKWVLHS21rgB9ihW3bTJeFAXB0ZtMGFAWqzSCJtrDNSebTZw_Bx8A_AtmvfUNe0opqhsHSIlkyB6eNBLf-e9Qoa6AL9XntAPYj9p3WiG8DNkxgzhJdWAngPOUWtCZ_8e_FCfR8eEUJpgyiMZCpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=D6OMXcU5LgTmzCPPyMiH2oxXWcFOHuWPPKHkqQCJAS9o8JPZBhfeKdR0TWWq4OBx_hWEku3sZm7S2WMO0LbUpGFdmzGVCuzwrYx7QM2I2_Y4jEj_WprLF9b9iTrTN7zQOKG4YMqH7CPEEm8w2GjCYurYp3YlNCrWcBPf1iKtQhaEng2aAW4nwgUrrDxAVsIYjosfVhc3ikqTVo-tB7kzNP_ODerOb8CuwzeZZ7BATqinZsUEAeJc4EI-tE_P1tTXF2Wf22oR3Vqr8Y9dSawiLwWkO8hO6ljFq0l5t07_fxZqMcKcN4JXUy25bWYeGN_Samto8O_NSJba1p67FkIBnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=D6OMXcU5LgTmzCPPyMiH2oxXWcFOHuWPPKHkqQCJAS9o8JPZBhfeKdR0TWWq4OBx_hWEku3sZm7S2WMO0LbUpGFdmzGVCuzwrYx7QM2I2_Y4jEj_WprLF9b9iTrTN7zQOKG4YMqH7CPEEm8w2GjCYurYp3YlNCrWcBPf1iKtQhaEng2aAW4nwgUrrDxAVsIYjosfVhc3ikqTVo-tB7kzNP_ODerOb8CuwzeZZ7BATqinZsUEAeJc4EI-tE_P1tTXF2Wf22oR3Vqr8Y9dSawiLwWkO8hO6ljFq0l5t07_fxZqMcKcN4JXUy25bWYeGN_Samto8O_NSJba1p67FkIBnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=BOYA0mR6HYPBXqN4UxOQvNf5y0i-fnDESI1y9V4aHfnx-EYnejcGNRHOj9opAPW_WWuP0aAu-6A_79cK3iFrBsbZ5iAhZ6wBObAVRg1yKTv87LtKYPwwvN389tPI3gSHlmBErtwt1JugmKCuyNDK3Jofw3kM0jwkpN8bgwhovMDAQf99XcNZ5Lt1HRidwYo_WDza4LEhsxCg6_TEIzuFXRMJqV_GV9YyvjTZhhxXlRZQof6MtxQXtThTm3VN0KnMlUfJDnt9BNmBp9Bj64ogsu6NbvPTQPGBRBysFObaY3TAYdpiJbW-G98B1TV8O0SXLRHjASyDwPBUOe-0pwv-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=BOYA0mR6HYPBXqN4UxOQvNf5y0i-fnDESI1y9V4aHfnx-EYnejcGNRHOj9opAPW_WWuP0aAu-6A_79cK3iFrBsbZ5iAhZ6wBObAVRg1yKTv87LtKYPwwvN389tPI3gSHlmBErtwt1JugmKCuyNDK3Jofw3kM0jwkpN8bgwhovMDAQf99XcNZ5Lt1HRidwYo_WDza4LEhsxCg6_TEIzuFXRMJqV_GV9YyvjTZhhxXlRZQof6MtxQXtThTm3VN0KnMlUfJDnt9BNmBp9Bj64ogsu6NbvPTQPGBRBysFObaY3TAYdpiJbW-G98B1TV8O0SXLRHjASyDwPBUOe-0pwv-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVRGdPi6QJmpM2p6Inzl7uqn8mIe5zBaRnN1dykBssueM3sZkc6E9y_lFxeOFfGQANBFRGoPVD6GGoCpmUoPOM0pEWI6J_DItITOXZQQ50ogOhcZcF7E7nHU-5c87lP-H583AQ_dHT1LJ1CILnyx3qgeZ_ttYE1IDz6aYT2cvuM-tLbr77Y9Pd2xfCwgFrQpHKqUHQnnlPpxvYHVop0TwyNu7JTOMLJBk-X3fcFHQoHA7ZCqHVNnlsPXh1t_mtYnE5x4JVNFv05VTUEP7a_8RHVCepE-390vaZtEqKha5z_X6ZoV4apdDF1XkfkKpe2m0XFhgOajFkGW4MMe3UH1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qz6W_uWOK0bCpid9YqLRqM3POxdtgUXiOkP0F3y8nLCpouJs38PupgGzpmZd7Z1ZCJfJavKF9kWT6QAtD1dgBdJk2IVcZmYnzmMm9GbJfZ-9FY55wgEiwpYZaxVMxnwfapYegPKRWtNIsdKhmVnyyWE6zUB2he2Gub00q0gSv9OxSr-VgddEcsPpzm98GDCOpA5UjIkN_69CvfLJPXeMASCLCKnar4rTlCG_dRwWrLHw8eAD_mvt5sr54oA0Byirw2i4aFi-q1XSUGby48UHsP7vaEqUJQxqLr2RtwpR3uzWsncI6iLWPbJBnja_RNhq2we3xT4kiGQRga0dy83TzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=ax3ERt50axQYsax6nT3YV7qLj2_xJXS4_pb6XNfottKu5wsLOMqhDoP4sMayI8TpvYCqAfZSGIFflQxGLXUnSfCo8OtLGYAPXZXmTsvGV3LjwL3wIrzaMdCyKpi1o3Fd1BYNSwBQNx81UCyHbA0xWc76M6zzYNoMT8ljhIEDsccp6jEt6QfOQWWpt0o8ngOnzTTIhebz4i7maLdCxd2nxdbB44hrh5gjnQKrZWZdz-OxTxUFrelkO52iDQIwnl6MV5j7ueOj0_PemRSVjXRjm6FFmuT8SoEX281C7l-YLvuab8KV3Q_D2o14SY7MNX4q2z4SwqEB5elqcnGF6A1ZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=ax3ERt50axQYsax6nT3YV7qLj2_xJXS4_pb6XNfottKu5wsLOMqhDoP4sMayI8TpvYCqAfZSGIFflQxGLXUnSfCo8OtLGYAPXZXmTsvGV3LjwL3wIrzaMdCyKpi1o3Fd1BYNSwBQNx81UCyHbA0xWc76M6zzYNoMT8ljhIEDsccp6jEt6QfOQWWpt0o8ngOnzTTIhebz4i7maLdCxd2nxdbB44hrh5gjnQKrZWZdz-OxTxUFrelkO52iDQIwnl6MV5j7ueOj0_PemRSVjXRjm6FFmuT8SoEX281C7l-YLvuab8KV3Q_D2o14SY7MNX4q2z4SwqEB5elqcnGF6A1ZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgjZKEjVkDOf5RXcXy5kxte_5obat4FHh-zDyUfPqieGEBOOV9POLFk7syJn1PjI5CLwym3Vqx_RbJwE3mI5OMdXIDi-TycRVTnniPl-lUo4V-YKXjL4qppvM75nptMoPEaG-xDFS3_QJok0mABmZTSbTbQQ3pDPirpar0w24WlRRLhIgWpQ_2tzQKCaki600HgRP4PIB9ziWIAB7p1PdsmBlANrpKpELMAI8evGYFhBd2IX2Ra97ml6WPgGFX8FAQ3y2e1fFPIrY-I6KWBUJwctAysG925qbZ-PKB7Lq9R7us6gZqF2oRTfupDbEZiilyHmcRWGClPndDHbiNGjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=PsIkWJj9UlFw5zmC5KxR9GAA2-C9h6xt9Onn52a-A1oMmpvmydgWhje8RKU9T5Aaug5GnAbxbyFrNxVhpbY15yJYnVNQ4mQlsuY-oacF8NfIv_Mzxqa3JdWXp9j9Sis8PjEHN3BVaDYTWxmk0H10YlaC6t3ibZc2XrhkU7S9v8eSYciL4hL3oURxKapOOzxhZWOAkqK70zhxGCKHoHMc8caIf4bUpS84LDygGkhOB2EjhAwRaObR1ThffxVusgCprgpW71FZC8-oi8OUWu0De7Mj90e5NM7iHQrkPUuGCowvqtCywix0tgGAeKdSk7SqtIbyS2MohsB9-AfSC06Adw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=PsIkWJj9UlFw5zmC5KxR9GAA2-C9h6xt9Onn52a-A1oMmpvmydgWhje8RKU9T5Aaug5GnAbxbyFrNxVhpbY15yJYnVNQ4mQlsuY-oacF8NfIv_Mzxqa3JdWXp9j9Sis8PjEHN3BVaDYTWxmk0H10YlaC6t3ibZc2XrhkU7S9v8eSYciL4hL3oURxKapOOzxhZWOAkqK70zhxGCKHoHMc8caIf4bUpS84LDygGkhOB2EjhAwRaObR1ThffxVusgCprgpW71FZC8-oi8OUWu0De7Mj90e5NM7iHQrkPUuGCowvqtCywix0tgGAeKdSk7SqtIbyS2MohsB9-AfSC06Adw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=YpGfYehAKY25Sze9brEwlRWH8XMwfe24a9RV4_0Z9Bhqr9bUjBY88z4ALVnPUtARjgIbbRUAsWOfv1AMpgWVuHvLDkQLTdONVsQDuNW4JobZONfNjNzHuLqCPuXTAtqLxE_3J1GVT_VI2SsrlagOQwrAMqIF4pIoXPByfGWhOdBS4jgnMV-mjlXb-Q23oB9G23xTuh9Min2VxCGb8tAUz9xsPsyr-hKNITFovKDPnpVSSezpPyARs3H27E-PkK8f6REKV7XLbH6MPlEgEznp21XKEnPu-YAHfrfTeh0gZR4ps2H4PqCBNR2y6P4oQKmi31sO6JNyqmHSIk7xjHWhOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=YpGfYehAKY25Sze9brEwlRWH8XMwfe24a9RV4_0Z9Bhqr9bUjBY88z4ALVnPUtARjgIbbRUAsWOfv1AMpgWVuHvLDkQLTdONVsQDuNW4JobZONfNjNzHuLqCPuXTAtqLxE_3J1GVT_VI2SsrlagOQwrAMqIF4pIoXPByfGWhOdBS4jgnMV-mjlXb-Q23oB9G23xTuh9Min2VxCGb8tAUz9xsPsyr-hKNITFovKDPnpVSSezpPyARs3H27E-PkK8f6REKV7XLbH6MPlEgEznp21XKEnPu-YAHfrfTeh0gZR4ps2H4PqCBNR2y6P4oQKmi31sO6JNyqmHSIk7xjHWhOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=W0nEAVjxkbQykaq4v7ILBs977-qv8WJJTeiEUH_myq8lPiBz8NZ0Bhg6G1l6cMEZ1wAdcMB12Dt82zQOZ_y7uNdi4ZJG7XfCyi4geDpvNLhnYjBOLyKOMl4IrKHU4Qjt8lFM20MypESaUGJRlJ39UaAf9Lbje9Nt1rmzhUO1EC61qZrJHf7PzlUAZbNd_x0YyhSqt1FPcpYwLgaBb6lJ1czGaYhrdyk_2wdQo6Yti0cxw_tUVaSQi8aFjkWPAc0IkgaVnk0KKiziPxk1FJ8JwSR3K6G1dsL09x6LTByBn7qAVlIcEZHMZKKTet6WOiEabjQnzqfJcxx_YdHqgBQpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=W0nEAVjxkbQykaq4v7ILBs977-qv8WJJTeiEUH_myq8lPiBz8NZ0Bhg6G1l6cMEZ1wAdcMB12Dt82zQOZ_y7uNdi4ZJG7XfCyi4geDpvNLhnYjBOLyKOMl4IrKHU4Qjt8lFM20MypESaUGJRlJ39UaAf9Lbje9Nt1rmzhUO1EC61qZrJHf7PzlUAZbNd_x0YyhSqt1FPcpYwLgaBb6lJ1czGaYhrdyk_2wdQo6Yti0cxw_tUVaSQi8aFjkWPAc0IkgaVnk0KKiziPxk1FJ8JwSR3K6G1dsL09x6LTByBn7qAVlIcEZHMZKKTet6WOiEabjQnzqfJcxx_YdHqgBQpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=KomlJtgXzS1gSPNIh2Pelo19zYrju2Cv1APPsmvqaOB_9iRZSEBBEBHY4IIv4KojZ11PV-51j2WWaWggh8LuiOyKI1a1mbABqcAhqm5NooRBFo0CKvCqU7gQimIG_dY-7htGUmkURXgJU0XrdH7T3v4Kb4mrdBPn2MyXgb3A7JY8X5dO5BvZstB-hHfjkqDMyK2e9VCFCU3W92z2wjeBBxlboPqM-rV0EieuwDpG3aTvzqkx7jxwUGj9GFrRC1VcUObbeKDnCXgHbnMrDw9TT5ICg408eiwAZiLF24xFsJlPU2cKiMmRN-Afa_h4Vt2SM9bStnTtOA7Q_cLkLNX12Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=KomlJtgXzS1gSPNIh2Pelo19zYrju2Cv1APPsmvqaOB_9iRZSEBBEBHY4IIv4KojZ11PV-51j2WWaWggh8LuiOyKI1a1mbABqcAhqm5NooRBFo0CKvCqU7gQimIG_dY-7htGUmkURXgJU0XrdH7T3v4Kb4mrdBPn2MyXgb3A7JY8X5dO5BvZstB-hHfjkqDMyK2e9VCFCU3W92z2wjeBBxlboPqM-rV0EieuwDpG3aTvzqkx7jxwUGj9GFrRC1VcUObbeKDnCXgHbnMrDw9TT5ICg408eiwAZiLF24xFsJlPU2cKiMmRN-Afa_h4Vt2SM9bStnTtOA7Q_cLkLNX12Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=vEsZMSnLvB-D6K8prvLBg6zhpPLYDxKkjGyty_iJLjhIEqRa681c3Fj1VmcvAk9cVos7myMoOFW2NT8dYdJz6-hHItLAOE3_3bO3MkngvG3byUW8wsUhjbJT5stwi5msQ37sBOVP1aJ7-gHTT76qhuUqEmBrxLfNOPCDQ6ydpNvAmwjHqmgGNkGx0RK41sslOj0CdgryVMvzIO-n4-0GWGY1JrVYjwegU_3JNxduUQlPiE3dR0JJE5oIc1Ce9pxKh8mk-gQBG9kc4nmmVNGlSu6TJU5G_BZWcYSkiSAuyYh4DAKFY8qrsvql0ioQ3Tm0GQYvCPcOubgLGm2x47X1TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=vEsZMSnLvB-D6K8prvLBg6zhpPLYDxKkjGyty_iJLjhIEqRa681c3Fj1VmcvAk9cVos7myMoOFW2NT8dYdJz6-hHItLAOE3_3bO3MkngvG3byUW8wsUhjbJT5stwi5msQ37sBOVP1aJ7-gHTT76qhuUqEmBrxLfNOPCDQ6ydpNvAmwjHqmgGNkGx0RK41sslOj0CdgryVMvzIO-n4-0GWGY1JrVYjwegU_3JNxduUQlPiE3dR0JJE5oIc1Ce9pxKh8mk-gQBG9kc4nmmVNGlSu6TJU5G_BZWcYSkiSAuyYh4DAKFY8qrsvql0ioQ3Tm0GQYvCPcOubgLGm2x47X1TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=uPcvfc9Yqd8ebasi0w5pYA1DymqbzQRe_Peejdju25wVT4i4Z4iBfx7Ame8cOBAkKod5W8tLlf6LgvZcpn6Lmlgtc6yiG9f5mrh7bj1tQza_L5tuj94AGv9xs_-xruh3puE09BiB-l-n604pBVf7yAnWOvaNIsDhpFEWu_a0ZxKe3if0DLc0vt5YiNutgoEH1bjS66MZtaeqcLw5DM1ANYm_TbH1oFa-8kRQWKwTNTYqx-CINjdiIPFvhB3ev0xPLCORpIl0g-wxMK3g5kOFfG0dXI6ebyC0m7FtrPE5B-J4ve2HMJy5qnYS0_uXswpHAfav1tW0L7ov4J6IQDpFdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=uPcvfc9Yqd8ebasi0w5pYA1DymqbzQRe_Peejdju25wVT4i4Z4iBfx7Ame8cOBAkKod5W8tLlf6LgvZcpn6Lmlgtc6yiG9f5mrh7bj1tQza_L5tuj94AGv9xs_-xruh3puE09BiB-l-n604pBVf7yAnWOvaNIsDhpFEWu_a0ZxKe3if0DLc0vt5YiNutgoEH1bjS66MZtaeqcLw5DM1ANYm_TbH1oFa-8kRQWKwTNTYqx-CINjdiIPFvhB3ev0xPLCORpIl0g-wxMK3g5kOFfG0dXI6ebyC0m7FtrPE5B-J4ve2HMJy5qnYS0_uXswpHAfav1tW0L7ov4J6IQDpFdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj0Se4qkxXmGjQpJkeusFMs96_3hnhAbJBtrsESWjB9EI6JC1I9iShA5W3BrNcg0JvPGzgpUWIxRSrXTp66SI9YJ5RtQEd0nUE2LJ9GrtMGEr5FS6zhCZnIu-smcs8U-n9BTPNBE_8pT-vWB5KxPk0aMzCoVDKTYd0VrpCHCPY2NZ23cQPt-ePE2otWXguxnqc_cy4xSOA9zCnuvx6v-j-upRbWYTUlS_6chQ4wyLU4bjk9rZ95Qf-1Tx3SmJCPEIU49qwmLDYdceZovx0OzYsNlQEy29qED1-qYoCOJc1hXoQa-8df-SvhzlPdSRS3ZxjFFt2uUW0zci6GE5RVH6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=F0UK7O_1WyAK-QK2t-aoeK_FCg44HnqexkKDZHZB0hKQJ2GAj-mL8UMva1-lpKtMPI8FZQ1haEXRHhDWdQb3tNo4u0h9givA2iEfI37Qn1qmTNVTA3QgQ8WdZShn3BqY560X-jaK2EXXnLeXcZE3Fsz4yVAyp_QGrD0g_7QnX60b-9fOy65c3qvxYbXRN4-TV0b6vfP-ZQKbMRwx49YWibykjmv0WLw-vMWF0zhQU240VpOwC1blnprAbKq5MGWZiWceIBW9bH-m0BOg8xLBa_JJs5PKr3BbMuX_1kcV0YKt5zB9cfDtZSUO_AC-bPZhhr2dOaqFo_9m-LTKj1IS-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=F0UK7O_1WyAK-QK2t-aoeK_FCg44HnqexkKDZHZB0hKQJ2GAj-mL8UMva1-lpKtMPI8FZQ1haEXRHhDWdQb3tNo4u0h9givA2iEfI37Qn1qmTNVTA3QgQ8WdZShn3BqY560X-jaK2EXXnLeXcZE3Fsz4yVAyp_QGrD0g_7QnX60b-9fOy65c3qvxYbXRN4-TV0b6vfP-ZQKbMRwx49YWibykjmv0WLw-vMWF0zhQU240VpOwC1blnprAbKq5MGWZiWceIBW9bH-m0BOg8xLBa_JJs5PKr3BbMuX_1kcV0YKt5zB9cfDtZSUO_AC-bPZhhr2dOaqFo_9m-LTKj1IS-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lirsy3xFlxgcwliWErs7HNNH-_00Puv0odXWxaLKzKEVfh3qnKpJwjydonf6GxKmgzPT-9mKzQ4_K37JKG-LIXsNXPIyQIHQYy3fTwutHKx-GUBlTu7sr7ZyE9wummFFHXjpx5nWdJBNk1G1zm2DPmLawD8DRoLdjJX-Z0aOQQ-nRI92G5OavJNPNwdfio1mhlKLhv9897uH-RJs76joRoFv9qYndnK2liSLIeSVWEXYoSikQ9k88O8OFcj_aha9-RIPF9w8Ft6uRnjXpmGi05uSiXOsI2emQRh-dY3bPYPCADEOpql6fHrkcDKI6ZpFN_YA6u3NOTrPZvD5lbSe-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=KbQJdnXLLuyuZ4ki3HfPD-VKmMUFZm3J4pp6rqGvybYBxsfGqLGyTRRpaEXYDnefG5cCxAgGWGeJpUzSkaq4kaffUC_7hxdKzXnGG-KFKgFhEjNROrwCPaOrSY_hlRf_1nMg6VKF5WRN3SEtOMedhYGVcs6wAHw3yKUH83ZSj0-w6CHvKm6dJMGvlWo8M1LcN0ojhuuH_EUf4RYRIl4ew6cZtXLyQZzMWgT7eT3f4O4zew20JSEKJRJVCrcWPtYKuLKzAaUJMVn_xhuULLfrVk7jztQrzj-uNTWvZWJ65pMbefvXgP66_DmfG6ffWUBeha8umxIPi7upa_Zvdj_2wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=KbQJdnXLLuyuZ4ki3HfPD-VKmMUFZm3J4pp6rqGvybYBxsfGqLGyTRRpaEXYDnefG5cCxAgGWGeJpUzSkaq4kaffUC_7hxdKzXnGG-KFKgFhEjNROrwCPaOrSY_hlRf_1nMg6VKF5WRN3SEtOMedhYGVcs6wAHw3yKUH83ZSj0-w6CHvKm6dJMGvlWo8M1LcN0ojhuuH_EUf4RYRIl4ew6cZtXLyQZzMWgT7eT3f4O4zew20JSEKJRJVCrcWPtYKuLKzAaUJMVn_xhuULLfrVk7jztQrzj-uNTWvZWJ65pMbefvXgP66_DmfG6ffWUBeha8umxIPi7upa_Zvdj_2wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpkbMzHj3wpZYnEUdBgosCPYlPap_QsaYy7n2C14HOgoU-Xu3Bow0_2tbRihEh4voSDRTRuzbFFvLeIiIuOjdA1cJq2dzbO6x9eeW1K45Y6TJ8dpmjwxuxv4o_cO6qBXYrpB9BfTvTV_RvTlWi7x9NBoV-IQRqu3cLTlmnHHqe57VNnAWY-lFYI95EkoD820jskXrU-Dyx6MCgQUvobtTZ8LgAkM2qq2dzAu4Er0k0RnlI3jB1QNsDvl2jkJaxezqv35RWsOhzXLMrxTjUmCHBiNQFSFEUBrs8ptjba9muZDj-LtluqB5DMj4G1ILLeH-BNx-CTYBzSFPxX0yr6utQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKBXB67NhfKTb2dHbRONcbnGYb-TJEYGd2AR7FOuKWjo6wVhrGu7nQDmLU5BDx09TV7rYfQYX52jxMjr0zO_Ygalau5sZd7JYK9CzM4ozvo-kjY5UAgij8OzniF1FTteM2CxiDEkquRyrv2L_wp_0xTJx_dKQCrmIbIuVA9wJocc_usYy3Tu84bZ5ZCRCpAj5b5qVp9p8TqqFAa6W8rPNS-nOFxMqjIRdcq1Ut3L-9gZEEDVXOPdezJKYZHHYP-I8Gy4HnwnPKIaIeiGx82X6NhoeOcW1KUXnUw2ZlCKmU85Dd89W4ZKktHSbCwYk5TWz_G3FQfdrixv2r29mPSS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPhg-37qlCL13BsQrJuaISkjJxy2cAFUeopF4bOsbj7h9oGMrovVkKImVF-VFzUtv2c6PP77S3kHshtV47m1f1q86pZXuaD8IzazvIM-nmip4fBUz5_kv2V3QincCn9FSUZ8hUKOFBJrK_4-_HHhGN_JKApd8YGF-t8QIIBA2ZZY_hoxvq9-s7J6k3AyQ_bZ0xRaXl5BwOA5ctywRIe9UbZDFlExlkWQD3gMZc8CUp-hw1YGdPjGExMzOZaDtzDwZYBKnTQtwRNppGN961heuM3vZ2BO3-EB6adXh867ZDad08pHuOx8Bj412SzuUr3MIddZp3LvDRfnjS-PKHjtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7cAYamXWcsvG0prckBsyxRC9sZqRFujAOJ2Ng26ZVuqusauOPe-PIyBoWCp86L5TQPWSipmv-hGdcS1sW5H2Qio-I9K2HoQsKlHYjBpKpq3fomZR4qg0zOnvhWBiYkYqY-Xux0FvV3ulU-cQSEpWv_Zbp3lo6SUU9aMzAK0ds4EudNSu7ya6Q1i4gSSFl5bj42A6TkalS6Nd9YprmyAZWroz-0MAmV34lgqK7oGxzqFoxzNOXsxTgPJB_KEZKMFTFk2akLRuSGzen6msqKyplzz0cqlmtdRtLvR3ei_rUWV6liyN5UQe1v5GLBc-7-nuu7ZMuF0JS0ZVqdbg_J-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7CBV3w0CZ4y0eqvVlJie3sEG4_rc7i-bbqDbyp5GvLyjSJr7moitmQTR3uV-Kd9uGVV2QunezvNUfl9Wv0UCMZIFsSr4V33jt5oITS9JGgOnwnafrxZPQSqNm2ixRx9yLyevX07ZVMzZGhVC2aOFJZOKflW9tVkG4GsX5gG8dcTi1h4z2IYwVk5o3TeX9eqR3FX3RSCUQnuJ2o5r5Xua9MHB22yYUlOmh33awyfao4I2TfehwYjv5odRbh81c9eg2kFdplsQ2ld5R7B4H2EwXf0y2ZTft-wj0Zmo9YZfSFpm9HDO4gJR1s6ahyoCl-OhHxoUBD0dN5wxm6R-10Pgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcJTR_WUXc_z6lFCkUwUbKdBQ4WzQobfqXJb5H_yi8Xcx85RQFY-yReQp7WICL5aIoZEHu8CGbSEIQ_tVU49CdBUEOzWB4zWM5hECMSEWVNXcApPcZqeGJAu5_nzhTrVt90_Xj0PEaJbMun1mdeoapG6KuRrcvq5lN_0Vp--pZ3CbS08vHd2SQrm2-xCAwu0FkVMUaNj7gGTLvOeoKz6Yd1Yfxljtd5RFLu22P_0YNzMlOs0ddt4ZMLfvof0sWmFl5GJr0NKwrC8KM9Z3bRyV1BzU3t1A7NhBE7WffIQuTX9XeMy74NVA16_y88W-4GlpwZDQiNORurXY5uxEj-0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxqLX356U0Okkyiz2ZtttRbROQqm3MKQtN2jD_mLpbAjs7dfRFVgFDiS_0H0I2AFIA07Ai_33DbjaMIUAI-lpX_HRWgtamt2bGa1QEhBS3BUj2llC5JLmMnZ6tBSzc6XHpwnUdDdL4afZiTkuUUAcCSiXjmpB17fSnd4FOiBsaD8vm-PU1WZIEDLxLj5BnLhWg1ekM_ZUtaO1dP1CfFKwR4fza4HGiAxJU3I9IVMufhN0BhNRFKA7tKntFpErp0Ug0EBN47eJk1H9INP88frH1Yoi6dzEHnqG1gwEVFlAOWr24mVlfJHUcOdB7YDEKTj-8u0W6nDXJ5vVM90YRcX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS2Uspt2Kh_2Uq-zxDPEYmT7eZmfbFYiu68SKEt6P7QDKHXQoFw0ik7rE1lF0YYAKDBKtk-o9D7rvoojjIwD6UeWgYlF1ryyxnDc-k0slWan4k5KVaIXJMyH_hsKvAFVewxw1F6EGcA_Fihj3pU9Pp2toWnXM-_MyxZkYL7vt7M6sHOAfAD4S6fAWSezim--vtJ2C9K7S75k27uB-5mje2KFV0aTb_JAyjDgISWEomS4uCBVJOUbNOKqHzmSiTz48mnc8b6cNQ4skutW8qqQr9PbtVDkPtwR9mSdov7hyRVslSYvPtlP54ZFD_Sq0nBHqEogREfvI6N4jyKb-sEy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=ZDRAOfL6j6F7MtanvSwgwoCVl5aM8dgc413Fqw1ov-nEhWJU6DhUkNcCX-nJzbXCFfPPggWeecgm9GH0JQEXw4zR96kroG33i5cbdHsMHyr32S109VDvDGlBlm4BkhTzLy0WKOFZzFlzIzpL0hB2FdI7it0LyVNP4UY6_RaUmXghA4D9SgJpba4coTCqaBSlYCVBu7Fco3M4l9JjgWZslNbyua0RshN8w22cR9mBAPr-t1UqmYhRFSzU6XLbx3s0JfoYWBZ-5rfx6xTyCU39VY4fmnYdINN4pLUt-IoXhPDGGAlf6J66hjQ9ezG9D3LVgl7NoLNTCYZ6nmULidobuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=ZDRAOfL6j6F7MtanvSwgwoCVl5aM8dgc413Fqw1ov-nEhWJU6DhUkNcCX-nJzbXCFfPPggWeecgm9GH0JQEXw4zR96kroG33i5cbdHsMHyr32S109VDvDGlBlm4BkhTzLy0WKOFZzFlzIzpL0hB2FdI7it0LyVNP4UY6_RaUmXghA4D9SgJpba4coTCqaBSlYCVBu7Fco3M4l9JjgWZslNbyua0RshN8w22cR9mBAPr-t1UqmYhRFSzU6XLbx3s0JfoYWBZ-5rfx6xTyCU39VY4fmnYdINN4pLUt-IoXhPDGGAlf6J66hjQ9ezG9D3LVgl7NoLNTCYZ6nmULidobuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXV2eM60UJdreDVB5j_WT70TlZ61QzNfnQUv1srcw8ss6XFHS2KNIBWrOsRSBf5pbPkq2lvX0OqCKRYyXlKXfkCFWcwUGIfdWZbe15ULR4IIh-xc63vpvFP5KWTuiU5Gy-dfsI5nxQSSxZWZQ3qNFQ9PKbo0j_zKfcLPXuEhccpoVANtJO-dV_Ca5D5ecMj5aLb3dY7Zwnd3VGT3TgRw9dX1Nl0qdYZd7DaCQkrtw2R2xLCJGp2qYcXvTBHmzKwaX8q8NLeziHGHKkih7F1FmQInhFo6_BrK0IIHMlo4VeTBe8vtzKKEL4yg3VgpBec4GsfrgOTKM2oGbGnsIT08rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmhYAbWzIeR7G8eDzpzB6WRxPpAzlPkRxNfSLxLgxAcTL8MmIQUl1p1CLK9aF01DhWF-xPxFKgg6r3UYx7wK5GiGWKPr794u4BsctMgvvX-Rn73aELguxzq7Dpdcj4b-I-J-9YgBx57Y8bkyoM3gPqVoeLBWVCvWQscrScsNozMdEdRlRdVgcIrbXwajpuRWz6wFWyuEgWlGfRRW3ebBOM_ShYR2cZ9XOTvjjf52s6RXBGxZessCoYmHU6TgmE3L2tOfmKKIFWk4dA-Zh7yXysiGARnEjRjeMJ3pAhPozngC63yqLp6UkXmt3Tui_BbpycjiBUgKZQCPVe6io-AepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvMFwAzCvKJ_2k-TB7I2u-3VOEAOa9kZK1mLxzD1xI2jLlngvj9Q7-e5xuvH6GpQy89bmI-aUZGh7wOjrD_GMbuBJ4pgtmZ9vSnU9fR58o0pbFstRXenx8NO1wVjRTuesnGmGCs6vJXP_3FUe01riqdl06Z6lXGPLOGdMGm7yGacWzvIxb1vDNd-eCeZlWyDWlHGv1JrJbKSzbxJecM3KqMj1fP9WSWUXg-tNWLRAbQzoS6NlglWukpQdeYmIw2RUTzuJVnlBJ4eO6Trne51RSOD2s6KtAy-SHl3_tyLlI7ThbuBbR7fV-6uyxva2zrJyN_FBwF1RtvEOpyrVLiP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbCkVDbhsUjc3Vxfm5r4Uu6J0NSW6FVwDowYX6bbvtPNVOw49K6QAJVxVCSdfFItbfHRuZX0gevETyYynsAYm3EunASZJt4Uc7OAXFdzbNN_A-QVTKX1pa_TkIfWPdkEowiJPJTcuwH3Wauk4EMGngl0FSZVjku4UuW_V-aZcC92X2Pl2EeSObHtn6pMNgLUhmhBcZX5sp4TLGjfDndmuQ9dDxn6TM2GFJ16vcs6rgILY-U2VxJ7dZdhHXQiHkZqZdBj5gnYXAy2ziEIdle7_A8g1LSGgFmuyifq9OBRCh_urcgeGRBFTvCHDnxzpvL48M2A6hHeXwsUSXQVTyUwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOrgD4oh4KCmlryqd2NUAldfLWBQm8rnA0APbRetTKSp73q6BfvTJgsdeVIAnYcNI5qG2_x4hrAmMwaxGRabGeSAfj85-Z1bQpUNCl_OH0Ri_5BayDXRnpbadTIpJSMZlM5UIj34EgX6uLo0GWl6rrBMQ_3r4OyP27FpM2pB-pYT_rwQeVj6Utc-KutQ3xU4cJ14I5bKJ01eauxLRwb8123Fc18HUOK0DHMXFDldtwO3ZaG7zjXHVabFbhvvPtFwJXtqBYLofZ26ddKKGErs8aAweft2C-PfVo52D1qOsKIxuS2vc0HtQQmWlawVMi_msAnHyOO5B71oLT1w5_lp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=h-9ZbE606pS-CkFha5hFmSZilUdYjroGxfuSLkPrGw8GFR-wc77dRmdGDcB5vUWYkXE6U8N_pm-md8_JlIaXlT9XNJEkhW8k4QSJuRs2Vp4aaLYK4wycE2u5IdaVB39EZ7Zt4cHYVH44RY5QO9JWviufczM3mhJT-tDKKYG61J6G7DuwUdAgeF5Ewx72JVQwDvbSoWij_7bMyuVMDBv1yh529NlFMMqJxOmH_MsbsUt41pAQTtRJGyGdStFEbNQPczhkUv4bqeiHWTREtxirWCHxBPDZbv0x9e1KBBAs6jwIcD-IX7l9rUynlrGfUBSxnMlDP0DIPDj34gRDjdEPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=h-9ZbE606pS-CkFha5hFmSZilUdYjroGxfuSLkPrGw8GFR-wc77dRmdGDcB5vUWYkXE6U8N_pm-md8_JlIaXlT9XNJEkhW8k4QSJuRs2Vp4aaLYK4wycE2u5IdaVB39EZ7Zt4cHYVH44RY5QO9JWviufczM3mhJT-tDKKYG61J6G7DuwUdAgeF5Ewx72JVQwDvbSoWij_7bMyuVMDBv1yh529NlFMMqJxOmH_MsbsUt41pAQTtRJGyGdStFEbNQPczhkUv4bqeiHWTREtxirWCHxBPDZbv0x9e1KBBAs6jwIcD-IX7l9rUynlrGfUBSxnMlDP0DIPDj34gRDjdEPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl9uvTlyWmb0Ny8ZZ-1CIJaNw35rTR8UKwkVaiGrxxxrYbHhpnk3Cas65bcdk3x_99deE9c5ycPoA2d4pQ8AUc8F2qqsoP46VIl4BLjCpAXoLMtIRL__zuWlgaifMzyqaxD5QYCp2v3Bs_buVNLD7i6rBCwpDHhyaWSCXKED10HJi5BgPfw5qwtOXuoR9VCLIWoHOZ-gBpih3_VqBdqqp1e9CbA6QdBRZkNaxt_4YUf2_pG-uCDpRfmlv95CQXKo_5vvsbXm6kHzksXJam8ytC9r-gts8K4JPWFEMkscUugKBLPQc5ZV8PvH5QQMqDKNgdAg1_JE8sQ3AH8QI59mIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=nri0yE7XcwVpoBtIu92jKo5RxO4ENCrEoUTLYKIpb8j20Id9K7xDkGsywNtvilYIDhHA1nfvmT5kIs7OKyq9WEggXVUR0spWbjpx-Rz4ixUrvHkUVhwDuu2dMVJPd-tqwIKgP58wnNMogHZpsob-Y2Aly5CO5DDmFyLo48KqO-qYs9u3SIG5nlLlG7E5V_JBrfEgbiExHDyJ7NT17p38XsunlybyI5ah3VPvNnFLl0UArhxRluSC252UGQ-LnJu5MDfLlFT3va7mmHfnnIBkKk9HH7lfAQUZgDV2rZXyjMjnIK7J0JJta5nbOweeKTzQ4baNRdQZQ9ejHtzvftENuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=nri0yE7XcwVpoBtIu92jKo5RxO4ENCrEoUTLYKIpb8j20Id9K7xDkGsywNtvilYIDhHA1nfvmT5kIs7OKyq9WEggXVUR0spWbjpx-Rz4ixUrvHkUVhwDuu2dMVJPd-tqwIKgP58wnNMogHZpsob-Y2Aly5CO5DDmFyLo48KqO-qYs9u3SIG5nlLlG7E5V_JBrfEgbiExHDyJ7NT17p38XsunlybyI5ah3VPvNnFLl0UArhxRluSC252UGQ-LnJu5MDfLlFT3va7mmHfnnIBkKk9HH7lfAQUZgDV2rZXyjMjnIK7J0JJta5nbOweeKTzQ4baNRdQZQ9ejHtzvftENuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=s98yayXAzbmTV2jFl7FJfMzBUqcTv0FmDjmugwJ_RFTwt19bxyRbZVCuRc5e20qYhFmpUgr2VpnfiJiuUKD1jbtEkH0vh9jjKzM-18-DNWnZaS-aECkqv8lrvUnYWZc-N2dQiuFrh93a0uJGr-ZHleDPhNHraZ8o53AekoIfOahGPdQWZIlMH3Xb65H8RpJ91fV4wvVHaF04xzApxzCtGJUBCN1oOluALB0a_OqjjA-QDHeYf_ujmdL_t8V4z8dA5fpsxYq_Q1TGBURmSYL8b6H4pVUU9vRlF8EbLdADmOP9KL7foVxB6BMDpz4WzaSdUs_P6Dw24vvI08usZzXCrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=s98yayXAzbmTV2jFl7FJfMzBUqcTv0FmDjmugwJ_RFTwt19bxyRbZVCuRc5e20qYhFmpUgr2VpnfiJiuUKD1jbtEkH0vh9jjKzM-18-DNWnZaS-aECkqv8lrvUnYWZc-N2dQiuFrh93a0uJGr-ZHleDPhNHraZ8o53AekoIfOahGPdQWZIlMH3Xb65H8RpJ91fV4wvVHaF04xzApxzCtGJUBCN1oOluALB0a_OqjjA-QDHeYf_ujmdL_t8V4z8dA5fpsxYq_Q1TGBURmSYL8b6H4pVUU9vRlF8EbLdADmOP9KL7foVxB6BMDpz4WzaSdUs_P6Dw24vvI08usZzXCrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FToLT9I0O4jGowKWhCC2j_BrbDcvYCMGEYSRZmUnKpXY-ypzIEq3BRGO2spZaNApI8eVphEBhSLNoXUnrt7g6txZczyZsZTnUUaqqlfQt-RA5I3cmOEkWq7clnTWtfGo3dRad08homViFIIzMMLcYklgYJySt4EB4s1AMiG4KS9K_ICr4Q--eunJU_qRGzghQyHGH-BdBHEP4VuQLxEBvu-en6Cz1dEAEUHozELDRAZKoWcH5-U3hiv_203Mh6N0LOFr5qwqQfkgRt-hZaTKzTN0VD15TeVZJrL_U1L2aumVNLXmCq9Fb_RrEc78HiQYhwDyU2IaJOzkO1y3JG2ZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
