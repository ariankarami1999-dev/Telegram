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
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 03:37:39</div>
<hr>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoQwPKY0GMayoDIB_z3m4ikzgkkesTNaNYW5Ai442AgqpMSkyVkUctP89CkXBa62psNw6h3J51bWkj6QkiVUCToli0flnp3F1uVyyDRImwTr7WSu5RuykDVui72yGrPLeM_B3IbOdvzFXr-o0Z8sHe_wZ62PGx4Hxwpg7bvviGnKDoFKMtARqRQPeFsqls1lafUr6-cYl4szGWmosE4eB7xeCNrGatHGDe6hD2uuG4kgW-2vP_APiWszUt2yh3Id8i-s23wTl4mn4qiUAHNk0rWNndgXtnDjTM-22eTsk93AFsemhiw33FZo3Sa-mx0a9lPxbb2NdSuHaBnbrQeOCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTKFRwykCe81o0z4NmeRxflVSlrkwvG5iWbiUGdDBPhbT92MhhfM7x0Er5dNuOYIneXXc5Ios1I6nU_rkaRwzdAVv38g74lMfYj1JvUZQvj-yogTnLbcW75yN37v9RZMwbsc-f4AaCXFqspzRNOw0qTelLmM4D4OBaQ0yo1WXfpFNYS6GaXRFY4lWfdrROYT1vDaPrRs_YnJlFtbN-nyfCEx6Dxia5cAac_zdz7eKF7aAJ9afMcNtQe_ipV3D3clXO3rNc9Y6sz3PMZ9J5htKnsCfgyWIsKcyM4GgCtG3mXRwdOZDvk3T-_LHTtOJL-Yp8FDr6mJR1MKeakFE7rCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1t3qGLXPPYSYQDKG3Ik_NSEHVIvqehPanKbmwfRFvjKms45b_cYe95iHq8zzrNfcaTyrmQkPAt3hu72Agg7rlkfA-acs8cTMZlHBf2JQHFgB8yKMeXq7xjFtC7qMMus8KuJeD9BMY8m0QrCGbXkj-aL0ANUahM0nprOWmvmUMBinywR-dSjHGXheDV9ZpOTdbCoyDf7hPoJjxvqeMIS_yv-ZYhnwM6tT7T5TkWrruCCSAaEiI6Kd2kzh_gPFFrB9nEUFo-JnGX9Z6nJbHy3fdHaAQlp6eK0jEFwRrhPjLdjD2UlJWEtrHValaJ03AzpklYAK8fHtjylOXWJOfBl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qolsH6FJvRRzcI6L-9qb0zFud1_weD0X_OVRMbq_g58h2YNPzV9nAtyEpaK05LnG9zvbXcY-vItP-MWkBnX4fAo5lvhgV-shA4egWgNM0eNg5q1u4d6h094rU_LGUu-YJQAEAfNfLcku-uS3Rb86qDBWWDiY1t9UVpZ6e_XJa3WtzdDFJSLJxREenm3U5556OF5WaW6pJuwX2eWJf6O31D8wR3U08En3USm81BzJZzpk2qf08Z1WryjJzkGjJ5tMNGpPDRgWmdf0JnIM0ezFCw7XkjLcdUocKX0bQNZqwabFfsOEQQlZUSd2zdN1qy9Ew7ut_NFErYfNExtvj3UFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lmtbipq5iTdA_OMWYYaf8NHjMIAekO2qYldJFEGacpxvUDQcg1JVl2_fYSCUpByxMhC4jFBqg2Dli-t5lNnGX_k957cfOjEqHHsWkafOHkwND-7tbvW-ANkZ_JDmThEQyc3kj17TTdDFv7R_hTR3QCGZNlExN3PSukWGULKHIYGQFlC15q61LM1uBc_iY95wQrsyK9_CYYLshItyPO-0LuZ1hLd3RYB4iWC_cdq7KmxceCqlMay36yCfBGYcyekkqbQ2WFKt937owkM-vR-dVovNRbz0yPvdrZPDZazq39LV_9DWKpg_hjEHH061RYrB6rf9aCjwqYrup4h9m3q3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRxQ3GL7Rr_iQ31_xBU6WKXq77WPnD2KVBpPWidBnZ3-_bZ0BCutmvCjfcTPcDa0sn17yredtD8LOLYs86bjnNGcnnqToFZQjQdG79tqZMzF5kblA9e9BUZPSSMnXEFruUTXI9WPOoE3-lMXmWNviSXAWIdCaa3v4MkvkIacEEohf9GcUBp7WoWUhsrkfZIwV2oeewA1IrXjloYlEnv1bDw0n-2Z9Lj1syRJSRSREomGAzukEOamqWpwbKpj2CkCoGE0YYL9wO6UGBlg0buxVYj2B7t1ko814onRaf-Ae6xeOTd4m5k6nwzwl0C_8xb3MN4tW_kmMjxXqOL28N47uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRDISfWdhFTcQ6zutISdPGBmHwvYeyOEil6XtRQL1PXdOnI_-ftnJZCCd9aZihz0TsG71O8CtTUKbr_SJQnympxndG5pmCybMQUVw8kn8GlYayJ4Rf9eeQcK1bSHDF50jUzp7L4jKYhKks86BS7TqTfi4KCUp1o0mxpKWHZT0CTvNQubVnXPUtvdWmznTwfTPXobGtF16zPsxawC4kdCRtk6bDtu3EAmk7uaSY83gXwVbbbKhbggu3y8x3FE6-dZUOrEsfWn8uZBuA7IEqXMHvgxz_b0NDIjV6lJi8HFg7JA9a13_xkfx64rGsvrY2F-w3gVRIiUS6NPgwLv09ffCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmoBdfJ3Eps7x7Up04Dk98WrE6w24RofCeMmBpfN_mLWfCSBOI2S34keQkt7jmKx85mjChOdDhSnfe-GYhaCpdOc8z1VcKBjyKEhFJjWLlEllrs7veRRMEiY-dv-a0vU4XaMpKDR0rmaPiAM1-jof2TL_IkwxdfLdZF7pd9TSzcWL3t893EZ2r6Z_JmmibfspU02tOKehoWqpeRm4i4ObLOYAzjS-0zJj05tiKmv-oLLt_wwrTb1rk2xYanTvC5jDPVTlycaUoS17QcJvuKM1x1BemauNP0h3am225WlxLUn4mJC-zlfVaCrxKnZOpC33OJ31O3sV5gLyM5ZJdiZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jdo3C-aUBNy2EQh2ybAzt69PdBhsCa3piHHPiO2kHMTTUDWT2k50xVHoksZ5Qvp51BtWDFUTgnRS_jI1sB74NHwIgpX0UVvX0_55jfHBXomi_frzujIxvW-ZUN76GVsTfbOPq5AZTt9CX2EznxiBjNY1RS0Lm5YoAPCwRaDL6Ay7GG8aRAb9HMOOAEVQLU8l33a1Zsu2t8ncONXu5PJE81RyPWYkFULnzZb7SmPhZZqK1Jo9rqYrUYbIL7pjf3l9xE-L8M11d3wEuAqo793cFyY2jKX54g1JcwyPvlv5Vj0x-cYPyKcnOkDwsigFwVMj8fEmxIlvSqYaWpJQkItAXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu828bLFPXf7z-tcJe449HY559hg0RUwyXlDRmQ-BKy45KaQaUk6EBQr_W5eW9NtALOUsWc69dnBpQe0UiYTUQQOirzA3kn6fm_il65NeldEDSViolkUc3gJgJFX3cYDbnqvJVCe1sX2Oww1JOGdktPYzxnCVwABUXmO33q9BVKMLZwMdNfl0m2gDoFL9PauExbCuUt17gFfOukqoQwBNPyZ--3mcpdvW_vx_9K5-N-OFrF985HPARJ_jXaC8Yt5Yynb31ORw4EsnXwLVMZYDA0TO4iaJCo2_xV5MGvJzv03A2x096ukvjTe-K_0UCJBjipnlkyEE0HZqr57STgkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=YgbzeGn1qQ0o1qYU-Ke_qh4EOQXvlspelG8atwPESOS8o67qvVOwmXbjivXyNWuQ8q5S6mrbKS96DBKfKaZR9xC2161GZ1T46amFISPZfCZAeDK2AzoPrC9tXWfacPZ5mqYVq1AJe0CTGTnyPZRlJbJjFo0OvmbBwR6J35BipZBwNfi-Y7-haLpmnBjLuLSXMjSocZZotJjnu4TdyHzw1xx2t_YcdcCiLybIAWYcrdvGYX04F47u6YQDB8y4gNQ08X-s2de4P_2Wr8xNe0M7V8aCvZDEZmpObPtknHhTzxWjq3goCfwURvjA-3kD10tILarM3fC2rFzBvG24cLRQQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=YgbzeGn1qQ0o1qYU-Ke_qh4EOQXvlspelG8atwPESOS8o67qvVOwmXbjivXyNWuQ8q5S6mrbKS96DBKfKaZR9xC2161GZ1T46amFISPZfCZAeDK2AzoPrC9tXWfacPZ5mqYVq1AJe0CTGTnyPZRlJbJjFo0OvmbBwR6J35BipZBwNfi-Y7-haLpmnBjLuLSXMjSocZZotJjnu4TdyHzw1xx2t_YcdcCiLybIAWYcrdvGYX04F47u6YQDB8y4gNQ08X-s2de4P_2Wr8xNe0M7V8aCvZDEZmpObPtknHhTzxWjq3goCfwURvjA-3kD10tILarM3fC2rFzBvG24cLRQQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=LBNE1BoqZfrUT4bq7nDoHO6YuzfS5HOSqkXqiXzuFoNqoQSEpy96gP8VSJ8R-_OxbQ2ghl8POA83h1KK2e_5IssyIOP3obpDYbt8qfY289ucsd81xFOD0gyv8VHshy_-_ARZGLir3yJ-6uLWPlHK1aMH-XGNO3F7MmE7pPn3adZBU52FFQPO26P2upsjQ-OcLtj43IhVFsLKghGhXgCn7Pn3B0sBa_P0pHQUTW4MpF546a59x0svhkmCbym70axKAalBAF3TITYH6UHR-_ycs_gNZKIcI7O11nmWg_oOgHstQOHJ5pk9B41zkdf8Gn7ElfwylzssLqS79QMDstRB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=LBNE1BoqZfrUT4bq7nDoHO6YuzfS5HOSqkXqiXzuFoNqoQSEpy96gP8VSJ8R-_OxbQ2ghl8POA83h1KK2e_5IssyIOP3obpDYbt8qfY289ucsd81xFOD0gyv8VHshy_-_ARZGLir3yJ-6uLWPlHK1aMH-XGNO3F7MmE7pPn3adZBU52FFQPO26P2upsjQ-OcLtj43IhVFsLKghGhXgCn7Pn3B0sBa_P0pHQUTW4MpF546a59x0svhkmCbym70axKAalBAF3TITYH6UHR-_ycs_gNZKIcI7O11nmWg_oOgHstQOHJ5pk9B41zkdf8Gn7ElfwylzssLqS79QMDstRB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDt9Xz2ojJd3VEd6382cXrw2FqZdtGCX23CDSmAWq-pyVrvQ5gc0Z9P0u6gybZ2pf3vjurC-Pd7B5Yp0VdA2Bza0JzHfrJM5H_HeFxf7Ls3KrKimQkl-v5XcQaIqtMWon9C3HiTVREL6_OsD4CNovy7Gz2ycduzHJf-RrRsLEsfn6hhAO6ULlAvsSOXpfc3IJMsFfi_kP8AN-32oXggerhaQUR0Yld1Ezq-lz_OIZKADPNfrijJP7GzIUPNNEvXm9x3s5ORGYlrR62SneUdPRC57Y8w2SElnDcNJevLjldk92qgeMNrhbFN47iYoTbnygSdYdx2iAM1hJu7Ta5LE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjSdzV-Pzcth7zjNSs0St3zxKt1IZcbltsDNh9XCsDVOXVlo7z85OhznBt73LVUQAT6aB5QuhM5LbgMmq5t7lDmE4ikw4BzTSPP0LsaVcwQQMlltts8I4L1OfzuAPAo_5oAiFPhu9QZtirqKo3_jAEMNepIXd7X3JG3tfwINTcAOaEV6Dw1OdC-L0Lzzmipj5RKHIW4jP_eNk5UncZ7wJaR0R1AnV-UCrRC8kYjYZp5w4uRm9hjmhAxgm7PCETHwPWf5mVvmCvlmEwbMxuFvldfWpB1CXH6phgHXg5cp93V45lR-0oC8fI4imxot3SkGfAYxbZZINYjjZO5AOanusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2c6dPCaU8-hcXhZIJNL2wihKzuvV5W8NosN5Jmq2GhKnQdj5YOFfXYI18W5-byPVHbl1I7Hn3Blws78bzns_EvcD0ojrd6gL9a65c9lWVj7RR0G5x4GCU-jDgPTDcCotSZq-8LrDEeivme1pzpq6C4zrUfYc7SXpbJPEychVCOcztsnzpzEoQagGo1uxD3KHwyRIHBnQ-TVwKhwirzm1wbBymmZnw1cogeN6Q4KX5o5Pu_J1IdVBVfY_vb7JKvRCFXcjxo-3-TVfCg2cXlP-c4EdrPdDFVZ_zWY5YL0gAPScf1M9xoiuSRG67Fun1ssl3p2wCUuujli5QKkl_Wtow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NS8ZLTj9H-HdyPiVlmMa59VK5FngxvJyDjikQzk92opYWaCKBnjsxg2tyuom-0ehteGcWOeUYCioZY4eNrSP4bk7pV3Yg-x4nm0zKNFTdTCl1HCn4BbraVS3-OUzuxqyKxLuvFT1WbcMFS79yrTPdmunnNbjWaJPztPw_ERlWYXmSXNYhraFlRTMOfzTj_ROvhc5rJX5r-FedXja9I6RtXGnmpcwQ1fuTptDSPpfrvTFs0FEhdusdHUAhY49yY8Pqv36ZWQ5NvAk_FO2U7prsGEnp40nDCFm74RvTfCKuGU7-_A49pnjEQJnPRkEFWpsk14SRgXK0Jmxmq1fj_dwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPOUt4LJEJ91ph9vFQX12nR-SCFDVpTPtpXd6O_roKls26Is_D0Ey7LY5nflZAAHnzJoZZ14d8PZ1kH8nXKozLA2eSP6WGKMvnt4IPu72X85CDrrpbWHBRPeqVQsllxxIwxYsp-N6CdwjChjSpNOaPGrlaopi4gOQQJlBMlMbcAAOUgzjdi1kL_2iBtEr6AlQb1bT_ECQ-1DNQn_P5wmNjDJH9A_qmwd_HvBXoWkjq4tK2JGzcrRIJfiWQl1tUXA98Hmx7uR5xEKnZ7nupcuKt0DAzjPirpgTJQtqvCOjWqDOeWO0D4ZKeYjijyUKGTvA0MSbzoa6DVyBvXLpMe60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GiVCPqO-hk0zs1d9t2r3IfjsYlOEcUThjnd9BVrWTIRprONOThs36_JQhZ4dRCfuBFBVP3YDAVO5HO27vVjXxdqBCHj34Lx-UKBS4UIh7i1JWFvRkH3KAsE33L3BkeU50qcniPtReNSu7A5u6tUFySMDxQoRU_fVJ8XukYbEJzicFkSF7-9WHpbcDLUDMKTQEBzDAXCghBtcXfqnkMSRQhqikQieBnK91zpI0FgxAinu4gapG9KgJdC8yQk8nPoRa4PReOrhfb_5vEU2cgXNUzT9N2HGFbHcBVvrRq3B0TLloEapiGTsSRMlLX83D-TKRULt4Y96OhwmcPzwR1QIrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_ZAfwIdXru8UJdBZURaVm1ZVbdz9M17Ro2wL8GBO1u0wrkDSsSCRTkULR46yRZDASpzGbXwCO2sBjjA685ZaDxoJfE8M4oRdMGhFF1A398Dln0XDifnTYgQZWWZKrl5LBFbcuBEJ-eYK_n7zzC99VzwjUZ74mftop9Vyg52sfhV20Rz8BtrXL4G8ucU0kL7G6MDaUx_cNC6v6FwauAb2Uahf03c0h31h5-aUDszcJYPWcHOdTw42fBSiwikFq2fdi452RlCOxPQ8C_DzZjP1GqqjJiPULiaba_-dO7adH2DtJExpYRIismbeRChxlQTr4uHJ9ZYfu0JRLpqNDWXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZzX5rMc2iI9vQoBYblF14-jay0eaJ8wIDsIt0AoeuzyLOpU_RCpQWKx_ggWWxh1LXEm-hgqheQ_ujTB6NBNZVN9j_0ea_8ddSWUUBWRKGHxuKss6NZA-i9lqTGygwVGlIcNr-f2oz8W_YFJW3Js5ql2OfAZL6AH1d2VzL8fyfOLEN1fzlwkAO6wQUz_THfCHXkfOtBAP69BhJJMndWo8r-OD5dBwuYt-8wHqgaOSWJ-5I8UohHmTGwRrBJZIl6CmjsTzl7ryU5XVtGt8g51FzsvlRtsiS01WD_EaKN1sFOvgnT4ANnyNyUt2wHAwjGsXxwFioPHZ_S_4ZoCPCen4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3YJyqyGK07xLmU_RYPxQFOkanKZb9ufBQTRjLEqKXjYjizxc33NkoP2HN2f3OVj0j3rvYBeqGeHe4iPY2sVkAmg8N1xio6ievyqvsJeUSuNDRhDbaMxvW8bimWj_JGKwuipVOIASFIZ5AbNnDazM9cZIIt2Oxe5N-v23XS6xadfE8T8EWuLg1aXjNvPiHQCK0jbPnOP7gguunoiVv8ASDPocVyI4z9Cy4khWZ6nC0svw1zrkZt8uUJCKRf6QxHQDZH7gP6h2pDLo3TAteOTOyLyTmeXZpdlEzqlDE-NIZe0-Znfc8y_I25vGNDI7cUeAO1RlBGPLLg5Vn47SDnXPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=kSDAbGiJjrJW4HEiVuG93HLjEWTWT9iRzPBqZwQIPnwQuk7inSVlWonOzr3ExrFGreBY2HzseJ48rzHypcV8uOsibb5I-AQY5x5zVv6pMemWCwaEh2yMbPRYRUHqx1oF3Xvu4kZF-fizMg_0aj1XLGbfB5eBxfXGSq-Syevt9LcUBENpuFlk-6HTnGAsgZGuUyTmrjsfQsu0-yvuFtIZapR8ZdxKBTaqpqZHYYoDVrTyYXJXFIyw5898_zCcjbx4Z9QwhSaN6VbErv8kRjrls7LYsLrH63R9ixWUNs0l4Uyujncink7a5WOfCJX15zg7jOY2Gw3snr-Gun9eXmtsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=kSDAbGiJjrJW4HEiVuG93HLjEWTWT9iRzPBqZwQIPnwQuk7inSVlWonOzr3ExrFGreBY2HzseJ48rzHypcV8uOsibb5I-AQY5x5zVv6pMemWCwaEh2yMbPRYRUHqx1oF3Xvu4kZF-fizMg_0aj1XLGbfB5eBxfXGSq-Syevt9LcUBENpuFlk-6HTnGAsgZGuUyTmrjsfQsu0-yvuFtIZapR8ZdxKBTaqpqZHYYoDVrTyYXJXFIyw5898_zCcjbx4Z9QwhSaN6VbErv8kRjrls7LYsLrH63R9ixWUNs0l4Uyujncink7a5WOfCJX15zg7jOY2Gw3snr-Gun9eXmtsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=fXKOarnhkLCpDAAy3ohH-2fJ8UjATW6fq9zJT_GXusQG-Dem95UAmICBNDGugdELZMkSHUymde98MhPJsKgjWiaiawdWqUugws1GKb-vht5sBaFIy1j2Ay_HJgQw7rg9-jpJDwKWXsI2sQptA-1Lz1dRYYrU354WeORqsWZ9O0W-RZFqAEMJOTjPbBwss-Q-vPOHLK9RtSAZO6F5nuhNpC6kHXQCcF_1VXnUwoAFMkBNy650gviIeo7-AKkul9zHVVk4DcmoLncU1yDvYm6P0FO3SUk8HaxictM0kni6XzbGJB9X9SaT5f3gXl7LQ5RySUWrLuObf-t8r0upy2pOyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=fXKOarnhkLCpDAAy3ohH-2fJ8UjATW6fq9zJT_GXusQG-Dem95UAmICBNDGugdELZMkSHUymde98MhPJsKgjWiaiawdWqUugws1GKb-vht5sBaFIy1j2Ay_HJgQw7rg9-jpJDwKWXsI2sQptA-1Lz1dRYYrU354WeORqsWZ9O0W-RZFqAEMJOTjPbBwss-Q-vPOHLK9RtSAZO6F5nuhNpC6kHXQCcF_1VXnUwoAFMkBNy650gviIeo7-AKkul9zHVVk4DcmoLncU1yDvYm6P0FO3SUk8HaxictM0kni6XzbGJB9X9SaT5f3gXl7LQ5RySUWrLuObf-t8r0upy2pOyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=fwZJyxom-0sK4kkrjB-REeSDnZqk3MOsj6qir4wbH3-lopOVZwDs1RuSfXRLqlltA_o6_3Rwk1JUYDwFvtekLDtvc7vwtnRDFNKsywTzWWkfUaZi9uLG1ko-WwRLv35_lTEK_29LFpZkXZ7vhOYmcft_jYtKsJxYP28WJX5yf6MdM5xJ-Dy7T3bStbkQffwDHc2QVoGQxDw1_N3J5ZvJ0YU8iQ-B4uaaZBN4E9R_aH2WYfI-AxdSfSnMS7iBO4FK_P4YkTragnOpV-gkPVpeY6aitIQLQ12wO8_p8I5U6MHwTuY_WfmwtEvXpoE-iTLs3pqdgLYFHjFnofh5X2HzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=fwZJyxom-0sK4kkrjB-REeSDnZqk3MOsj6qir4wbH3-lopOVZwDs1RuSfXRLqlltA_o6_3Rwk1JUYDwFvtekLDtvc7vwtnRDFNKsywTzWWkfUaZi9uLG1ko-WwRLv35_lTEK_29LFpZkXZ7vhOYmcft_jYtKsJxYP28WJX5yf6MdM5xJ-Dy7T3bStbkQffwDHc2QVoGQxDw1_N3J5ZvJ0YU8iQ-B4uaaZBN4E9R_aH2WYfI-AxdSfSnMS7iBO4FK_P4YkTragnOpV-gkPVpeY6aitIQLQ12wO8_p8I5U6MHwTuY_WfmwtEvXpoE-iTLs3pqdgLYFHjFnofh5X2HzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD2izezkh3SsjfFL4hMyqNshYlXqKhUbsp5TeKSslaNeV5mMwUze78g55NfAnk3-W-7kqTD77Sc6e6F5ZKNw_rt9WUjhFcxxVGRlxgdIdaAOUbbP9wbXfV-5kk3c20sHeSSqUSptc7mY6pe18S1zEoI_R1uXlp0pE3QxS0ur0zj9zSwSQkchb41zvri84EWnXcy7Hv0pnyXvCl0m1QmIGc-qeE0SOUWGm-72Mclqj8skIrAg8H87tE2QHmL6x0Bl261b_3I27JLtiSED3qt1PBytFYNxNezeoDLu6N1URGhsXj5u84DcTkb_KSWtEUwUYeSRhi1LG7zHCdXU-_r1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/towqaWb2wfBeIgu6qoBJuchpxLgIGyp2YEaKKixzqdUAqCWJ0QXY81gcPxFg3Fa-pJsbfG1dRQpHk1_1ZAugPXFNnF5GBjStiRc8opX-IiWjjAyH5SSnOhMZw1-mzXIeXcxYOBwTGDLVqej4u2UdumGQpVwVq-RElKEU9VLO8S55kmfeAKltg-tQYUEygJb0fSL9lGooqyXvuXnuECAqKga3J1kqjni8RFSBN6ICvkLyCR7_86BumJdyu2l4e6F5MGM3PUSFl-MhWvO2xxY3N4Qm8pM-uv9jRB4oQsyRCH2ekVgbmFV9Qqb2o5ycN5P158b5HEdgvANTW7wmtWtJmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu4a1iRdIyG3N3Av0Ce2IYSblCriuYLdCqJi5ke_zTNMDKS59RxkqUrJ-f0mKGXB8DvifCHKkuRaEf2khMImfl-6pDS-qNyRCNrtoTHqquoSZpYNJ4AWe6p9MzqxfxYg8OGUQSXFzAHMHbkQoolEOVbKtrF1O3n0mom3HwszBTSN3wJHbeJc0M6es4bA3_n6iWnJK27mnY2Dit2XjRM3vYc0rg9RCST7NwkFAjkgAeA5IWn6gG2-VEP738MChIOO4beMvIWmnY0kZ1bHfRllBX5BLkvuyZTAT0t_038QG6s_oalsQsDqkyWnUaUI06TcRhTCRiNcxu0zSFp0-MLp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2BMHLwXXdGlIHEk_Sjh64pnFnw0R1NEhy_DvJF7lTWtqOHGqmq18nBDJqboTKVZkq8mWudNmJXAEviKNsbH6VMfYlei_oUFKQwbkm3DFiU1aAtFw5MR606RGkN_nL-aiHF5IBjkSW_x7uPm0_mUx0LibfwFzHfLc5q1zKExhwNI4YZOpdxPaLmXmF5yHumg6aVsgj3hgd4GCl7nfnOUxgnAxWEjlwjSq5jnI6V8tveZSN23jVw7S-MGWYebd8ypn_cR1fbMCtPdclQzJIQYMS-08lt0NsDhPx8nBwTcmOHRCr3ekYfyo98Z2uIp2mQ0Ollr233VZ-485r7deKfV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=NofQVxn-dDbnAGujE5cBH_eQ7am_FazKjCzYJb34ewvTTT8ieMu22ENrejVOR7dmQ7sw4m35CLLFxTMlDOSs5ikMByF0D7R2zfQG-hWT-xu46oiynSWUJsJ-rvsoh4u31i4axSdIg3nPu9fKo5w1J3VP72hCqEwPI5EnePCGiFfJwttgtcyYpegvyA3Yl5MsvQo6zIm9U0K13xcP2-2CPGawiTxbJ4oGdn97WPSTvB_LfFCbKWZn997GhPYS-DBlVrebYlpERp-CbHZesGTFxZTO4gRkyc6hf3XubPtXhMH_iL2-sYNX5Sob7p6gwIcoXyANz_MuG1MVmxGP6ps0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=NofQVxn-dDbnAGujE5cBH_eQ7am_FazKjCzYJb34ewvTTT8ieMu22ENrejVOR7dmQ7sw4m35CLLFxTMlDOSs5ikMByF0D7R2zfQG-hWT-xu46oiynSWUJsJ-rvsoh4u31i4axSdIg3nPu9fKo5w1J3VP72hCqEwPI5EnePCGiFfJwttgtcyYpegvyA3Yl5MsvQo6zIm9U0K13xcP2-2CPGawiTxbJ4oGdn97WPSTvB_LfFCbKWZn997GhPYS-DBlVrebYlpERp-CbHZesGTFxZTO4gRkyc6hf3XubPtXhMH_iL2-sYNX5Sob7p6gwIcoXyANz_MuG1MVmxGP6ps0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=qKCSEHCP-6qqCZEhne2FaafuQjjw7ytJc6abKEOYBzXhpDIqg94gCJ7CbEuxcIvEfa4Vv-JnUyHulgmMOsPE9tCH1LY8hY0wqMOroBTzNqUaZU9FUK_quPp1HgqZDQpCmmkg-DOHHRan8i5fIrQAK8YKMQYi4uCd8lQHs3xuIrr02BudKPdrHjdVC_BKGwVfObT5N5Y3a4R6UlZIu_76STngQAcClFYPbdUYLE3cOpfQLElAr_4hcCy8_4OxCnPet_kCcYYgllm7rHJvpsCicIS6gCxZ0rmBUVw8KasQlQThJlGbgwfBV1H8_w6rzZ1l6t_XMXAt2_dkZZXY60Js2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=qKCSEHCP-6qqCZEhne2FaafuQjjw7ytJc6abKEOYBzXhpDIqg94gCJ7CbEuxcIvEfa4Vv-JnUyHulgmMOsPE9tCH1LY8hY0wqMOroBTzNqUaZU9FUK_quPp1HgqZDQpCmmkg-DOHHRan8i5fIrQAK8YKMQYi4uCd8lQHs3xuIrr02BudKPdrHjdVC_BKGwVfObT5N5Y3a4R6UlZIu_76STngQAcClFYPbdUYLE3cOpfQLElAr_4hcCy8_4OxCnPet_kCcYYgllm7rHJvpsCicIS6gCxZ0rmBUVw8KasQlQThJlGbgwfBV1H8_w6rzZ1l6t_XMXAt2_dkZZXY60Js2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeBVUk8l-2wOkksRn6dnpIJIYeEIb3Dsqhl_612BWVCQkCOzPYkFtezcjrlz-3e9phJxT7hb7hZSjQOXt9msQMk6AnRt-Ze_bad08F1hMiQK2ZhqJ6FZjqYU6NsHzgvBAuz4RRYdkfAM0yB688vbh2P5GV-rR7Anfv1C5rNzPHCR9TZvsGMYs1VtONhtMKcaSV6T_h01D8CH5Nr-NXjoatsGLaUq0WIwTNguN8kfMolpoK8uYS4t4udJ9SKHFqYZmmA9VEjRNlgBdlQAA33km4CtE84Gp8dWdHTy6KqvPGGBJheoI7JD4wR0n7II0Y6wd82EwF_QqrbWZU-X8Uo3Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve-9lbgHh_xM42b35URNVbDU_C17JdDnzkW2xtO9esKKnssSKjlIq-d_x6jzRSZ9IZtXNgVNJTBWLW8j-fHDjJO9d0TCYSKLEOKWfgHAfOMfN3kC2EbrCVtm7Aq7-BeGFNFEhLnUoQvB_d40EQdKlsj1vP5hPOKNVzMI-ChysGHGmrkoO7AsFz7VKiNA9AQrYgdn1UpWTmvdo-XmijvpOEhW7gh0TcdRaqqrFv0nWlyQmLzzRqJaHQXoT6rmxmOKwoamgkIBWu1WaxaVpal7gn2o8joDLjMiTz79xb1vMsRJZD9UMGcZ1VgWayWp6tloIq83fVw1ECMu1ot_B2sUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgF-8rMICpy242JzTJot-Nq2z8R9YBFkbuYP_M9729AlR7Fcfcf9rFUYA1phTO0IMkWRhQzEQp1XapJp-r_MZmqPR8pEtLB1WugZnikRAglqJMn01wdEqzY7YPSC2VTnhqA-kOfMpt1KW7U03tu0iVi-AeZu_YJacM5YFNITxGipJeMuTWS_L1MmwD1Ue_j7vLvvmw5GJIYzXLIRXlgPj-xEod70M_8D_2-tcJtz89GUHnBNBr75mhDi1TOwEW8aBoyrlnuOWLr89hVdoAUmNkBk2o91Q-hpSziidzv2c848VfaHDC5Z5lQdweLZu_vH_el-7TOjg-ZOsryb6hLWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnslq8xkQdGHekwwK3u_pKPW5ccU2r-qb-1IuIEm8ojQFuLrHbRvrCkkrLihfQLLUj18_eKoNEG_b60GwiUtGK2adj4ZyR01HXfV5WkFguD9ArcqgJhTCpr5SiTQ0F7efniLWwefmIayc9nu_x0oaS0aAZJ-DQuhSuab75Tvk9VimXRRGR1TWAdMZuLkg0HBv32O2Y0dMxfxcl2cm0feVqN7w6Zl7R3kU3WsMhl9vVzpz0VE6XGkSZoU2aq-hdRJHkE7PjPEOGgH53UnwCw18zzSHFuyjqjw6G8xcsBlM2FwC9IFQICmFliqO8BMJNmDtqjgzMJidtaxsotLzerGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNXgJSJxrDKSPsQFHvpRBC8CLttiAMluFVFTDGCsANgIba3bnXlyRUnx9CxWQGjugCrEBRAmz4tujpDyY2TvyWbLd7SqM6tzoOumh3eXlzRL9cnVOAbtMEQ5s5FNOWWqkqnldOfEzJhegoX6NrRYcw688szlzP39v8pGB_CgF3CjsGy7qVLLNi6WzdufvqIP6jas6PlRXEHBSR_StVKHzEQGH88X47A7hkSUuAUlR23DuQkyamu955ekdFKDpdGm7e6FGlMROYs3d9NwO7gmjtBVFAGsRfZWaptr2HX0QZAKXZXlGO5_txho8fuKM6zLmB4pTR5VtpHQ-MHKhhpumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7gjFRhT1uKHEmzLbioswFxubBk0P1bBd5YHSDZPvHQtFuF7eXfN4zT9NbQzsoWFbGLdx1dFKm-raFiPNur-cVtYFn4Z91806sUztxYl0jXhgSmfYJmbuqn_QONiheZbUnV2CcpJZfTfrf29caboo5MFD9P2jXaa2z7DwfYcLnnFf2Yu3VgAN7eQBqcFi6meqJZVxjkZUCmVCGDCFwD_cAnIgZeUaZYH-UW-r5oPplTafC9rapMOamgskbH0ZhEkLN1mUlB0GY1rTX61Ma4sy5W0wBaB0rjNUicWdjDiKC6qup6lCPqFotHZXJ4TZa31TiJzsOkIOSpketsdw35dAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzvdCV5vePmGewgqYBYUtpptDn-d1ZC61m5EtkQNrLWcPTPmw60thex-3aPc6BiIoTZOY5IP692L_0weamLTtg1li_bCeNJG4qa-sNPWmUCKS8zQ6oCMsv_aYx6H6CTiBNhIpqpP0AttNisBzH9b4vzJOrgJI-QBz9dwrpDgsIIhX-C5ftk8V0wLD8EBocLbz3IWMaJ8K0ip3g4K1r0R04FNh8Po-UMKLNu_AGwFqBRVjftTgNTu42poDmieEMR9b4KM2s5bgpzjDofalkc-MF0N3rbWbJAL8KD15tNWl4ZwI3_z2kr4BKQHSL-2LUeDGbZ0PcSy0GIOxbdwNPcjbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odNxGiGoupogjT2XkWepTZYE5kZ29oDSbc8k2rV6twvcYDTC5AfvMqSdmoykzd2NtpEe0bKnq0gR4d1VAs-eUgSAOTEmlExH65tq6_UQWzCHb0Y6XQMhd0CdH4jnv4r3XvduQQabLwALRrj-oiElJ0TxsRedJ8EXEuuAajTth2IoZ7r8Oa6l5un9UVwimMRoQX02SreGMnIzCbvWUoLDV0IffTzTGS8qBa8qFlPpUiG0uCcciQktNpYS1qRFSMhnkSFvLT_PrRty_TIHALNGdr_5Anhs1Vna1nDTk5AF7MauAutqArWMXvICoV7FHNUh5rblR8yFEb7R071C7vfjHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vOEczHe5B7oXNecsb_GpJ-rhVODYPRDAxSR7wkTz0L13JTBD3lEahHjubOy21oEDEGRAtfrOA5405TEAJpSLAxcL8btQPmKgpo1fWbBIPBirgrXXnK_f6sfnM0uhI29eEB2tU-C1EEeImXlNrf2cjv6AeO2cqr7yUDxov5-lPI1ot-aeDQ2mQFmjTH0Dr7FOUJFWK5kuEZeWEQstxVet_RbAxYwbSagHiaEVUA9cbBmxGenkzBw7zLYAPSvWqjk7j2M98PCIodgm1MzbQSTLa_ck7vGfHwsEFEtfaDIKP47OI259PUzT07yFIABypKVZUuIa4FvcKRj5CnfYuPtk4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vOEczHe5B7oXNecsb_GpJ-rhVODYPRDAxSR7wkTz0L13JTBD3lEahHjubOy21oEDEGRAtfrOA5405TEAJpSLAxcL8btQPmKgpo1fWbBIPBirgrXXnK_f6sfnM0uhI29eEB2tU-C1EEeImXlNrf2cjv6AeO2cqr7yUDxov5-lPI1ot-aeDQ2mQFmjTH0Dr7FOUJFWK5kuEZeWEQstxVet_RbAxYwbSagHiaEVUA9cbBmxGenkzBw7zLYAPSvWqjk7j2M98PCIodgm1MzbQSTLa_ck7vGfHwsEFEtfaDIKP47OI259PUzT07yFIABypKVZUuIa4FvcKRj5CnfYuPtk4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=uA8b-G3yRjUFDLv-fhiZvpy6ldSBcqS67aFAZP-HDt-LNZbvnwglI0foSBPryCxmkzGnjFwnvm6NAyZefux6YPlzi1DZ-BhlHJ_D5XMZ0bxazRPr38gqoENK8b4-y_zzxVFDGAtFc8IeTzjS-gtZKbX4QbJ3oi-fA90pTipbH6IcZT61-zgKrBLU3t5JC2bHPpUD-GiK1-174baHPj0vtcJ5VfK0fARIJYF_EhKvVmarM3izPBfQz64N3GjjlcTuVQudgDY1pVRfYDBUOYB1kJvV3Itk2pFA31pg5qY7W2A9wkp6dUxVTUJHqGqATmi0V8FGim_vRn_ufvUJiDMqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=uA8b-G3yRjUFDLv-fhiZvpy6ldSBcqS67aFAZP-HDt-LNZbvnwglI0foSBPryCxmkzGnjFwnvm6NAyZefux6YPlzi1DZ-BhlHJ_D5XMZ0bxazRPr38gqoENK8b4-y_zzxVFDGAtFc8IeTzjS-gtZKbX4QbJ3oi-fA90pTipbH6IcZT61-zgKrBLU3t5JC2bHPpUD-GiK1-174baHPj0vtcJ5VfK0fARIJYF_EhKvVmarM3izPBfQz64N3GjjlcTuVQudgDY1pVRfYDBUOYB1kJvV3Itk2pFA31pg5qY7W2A9wkp6dUxVTUJHqGqATmi0V8FGim_vRn_ufvUJiDMqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RV5JLgHppE9vHh6NgMWb8o34FEvUowuQasIb9b3oNqYrboWM0BWx1BVvA_UC_3MhXEyXMb-Od3mDmcoZOurMyOPgn8H8Xo_dlBsGeoL3IyS4CR1GkGgML1GiaZFa6dLkGo-5hJBngY2QOtBBpMJU7A587JXRMYJPkwlJyRCB7xiTr3Z37jIpmwz9yeX0OqiFVcIwtnOoaOSYnQeT5zijF4HbKSSw2CQhXcc-tcSXOyiIz5lT8HhuqOUzemAnKseZz2RMX_V7VypxnkCsojAJBg-4zTb4DWCr-LbJBLo7a8Ecq563yutJL4_leU8ezjHFKoj0_QG9LAQDL3aS6VgcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogjxXWBz01zbtAStDQ8AK699Vg7uZnPX1iQTwPlC6POYft-hHc7nRgTqKTUBq3jQcI1U0w9YnNAguJ9OUinBK-zaRVJYo0ctdFhHI9MRCYXfRHeba8aw_RtF79S-0uMJZFwjESIGuVR-e1Q38PpBZ-l52oqd-fGyiqwrYCJO6nryzmMUe5xw8pSG0u8M1erEvTaqQ90ubkTvNndZPZ9nUggnd_xRE5zdnzZbMyGp6b4yMa1Ze_zKrulyMgHDhDLGUTjjKENJTkI-LOkwqOILE3oGUUn-UhT0f-aaIgJhIXx5QqGsu5kxBREnmjypezi9Mw-RX6rQSWhL9n0sMGE4pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=sM0CQJ70w9GzFe5-yfzcu98P5tLS6J36RQqYOrO6T3IAkATQ8oTqYRXGNO1v05_rOKcMUCNe_YDkVwxsjPND2PQT4VKjf7P01lU-AdYpLGcxLuTf4M-j3iI1-SYpthRHdAX0oCAYuIjG5_eW4S-XwvIPnJn28IFE278-AFUkq0GfiPu1-Rd_ahig91n_JVvgosCgmwkRSsQA9RPicz5_-RR6c_wYAegluBiP2BZS2UAbZlqVthN1ofDWqz8vttuoXDK9y9ft9u-0_2NydOF9dPoxpHKmpbTm8PY3aJYX3QP-3fm7rNMWTRzF5HZdBcCJskLpbM2cXmagJDrapz-AMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=sM0CQJ70w9GzFe5-yfzcu98P5tLS6J36RQqYOrO6T3IAkATQ8oTqYRXGNO1v05_rOKcMUCNe_YDkVwxsjPND2PQT4VKjf7P01lU-AdYpLGcxLuTf4M-j3iI1-SYpthRHdAX0oCAYuIjG5_eW4S-XwvIPnJn28IFE278-AFUkq0GfiPu1-Rd_ahig91n_JVvgosCgmwkRSsQA9RPicz5_-RR6c_wYAegluBiP2BZS2UAbZlqVthN1ofDWqz8vttuoXDK9y9ft9u-0_2NydOF9dPoxpHKmpbTm8PY3aJYX3QP-3fm7rNMWTRzF5HZdBcCJskLpbM2cXmagJDrapz-AMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrnVUQUsOYrcUjquRCBgNioap2Gga_YP925o6-CFaybqEV2wJy2GU9v9EroNjbbhd53IhgJ-pCEOTlynV248m24BZca2NpCMiCJjT3UQrBAeIHLZJZdeumJd7cwuHqkF92q1suG0U82jcgl-0O_AD5R0GAeUusrtMhLL4V_Rc6kQW1klB5GkVc8Hs9XpS0tL0yEhLk1i2UsbrCV8eg312o8HkBeA7dGgD48dL5kv10BVThOpbQ6ruUPkyYE8NR1Y4obQhXg1HA_e0vAg8n71Ex-nSIGtMZPFpY7MIitQrRpe8rrY6NkxEnFu03YmPNMvwONdaa8PkjNpNY2K9pzUFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=pB23IIdBYlCWpht_LTYQbWUTsymuyZnx9GeBSgA3jd5fThYCcpPytzqKpKj6ayFzRljn2DOvfrFO18ZUhICj6_FcI5lynEi9KEPb-vAk_JqXluzKA5kX2-LBpldAMV2s7h0UlNltIAIYfBhot88545ttExs0S5eG9BA3C9aHR0KqK_sYFdcWVPfxhLLTyiXxK4HfKp3onKheSWbY2fNWjVIcyv7BV1oKpGy2MitR7To-mb-zNYHmF6u62zwqgPwcNbr7FOFPDCG8lSsayulPdJFNWdGOaIY4eFcR_DxqIRdG9wooxUF_AXnck4VZCeBPBMpNtdz9913C6RMflHmSzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=pB23IIdBYlCWpht_LTYQbWUTsymuyZnx9GeBSgA3jd5fThYCcpPytzqKpKj6ayFzRljn2DOvfrFO18ZUhICj6_FcI5lynEi9KEPb-vAk_JqXluzKA5kX2-LBpldAMV2s7h0UlNltIAIYfBhot88545ttExs0S5eG9BA3C9aHR0KqK_sYFdcWVPfxhLLTyiXxK4HfKp3onKheSWbY2fNWjVIcyv7BV1oKpGy2MitR7To-mb-zNYHmF6u62zwqgPwcNbr7FOFPDCG8lSsayulPdJFNWdGOaIY4eFcR_DxqIRdG9wooxUF_AXnck4VZCeBPBMpNtdz9913C6RMflHmSzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=Fn70a55XW9b8y13rtNZdlF3DQgICUUblb_AUe9DiZFERAnU4E14_gGnMqjjtbE-7PzDf18lOc6rQ3ZRF75o7AQg18dikth9-iEeRBuyisujrgN3jlnn9ioUIpc-Ti4pEdNte6OYH-Vieuqq3FHBpfS_kpyqDhX6GCxQeowJRQJF5RrJJlwhfA7WEpTEfdji4_DbXvLOaiTzc5lqneVvJbr7xv9JQ9PAv11QebPXhOOy_NFnO7tbcoq9ep-_Pmy9Q9H9sE9bP5rlozONAmxmHmpREXBQrq3AwBO_dG6GXBVMJEBRaG3XrAeVEPMlXizrTq1-PtNOPbIAQtld6ZoK9GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=Fn70a55XW9b8y13rtNZdlF3DQgICUUblb_AUe9DiZFERAnU4E14_gGnMqjjtbE-7PzDf18lOc6rQ3ZRF75o7AQg18dikth9-iEeRBuyisujrgN3jlnn9ioUIpc-Ti4pEdNte6OYH-Vieuqq3FHBpfS_kpyqDhX6GCxQeowJRQJF5RrJJlwhfA7WEpTEfdji4_DbXvLOaiTzc5lqneVvJbr7xv9JQ9PAv11QebPXhOOy_NFnO7tbcoq9ep-_Pmy9Q9H9sE9bP5rlozONAmxmHmpREXBQrq3AwBO_dG6GXBVMJEBRaG3XrAeVEPMlXizrTq1-PtNOPbIAQtld6ZoK9GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=D80s2LapGzd9PwRXywxAT19wCEF4ZAPXRA2WL3kqbTVrpG-jKWBmHicgocmKsZdClnqZgS6NNixqFGf_lSTtQhukotkU2m0PpuirnshTP4-Qq44n5nvUJDitMppnFvmzNVV0RL1-EGzE1OvzcqqAVvn1OpbzrjYsln-2frPvo5NuJlHvYgu-JjPMaR4NlFyv_bzfB2k8qsVj1QNKscVEC7U8bfTaFjg4ocOi7wnHTG4FLL1uVMHrvPMvQe2uD-8A54pmeqb_RAwNTZTDbSjSXczXxuj6QCXZSb8wu_rvLYW-1FTFhuTAyP8siUbPxeM8w-XkjFpSsqIi-i5pn7EL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=D80s2LapGzd9PwRXywxAT19wCEF4ZAPXRA2WL3kqbTVrpG-jKWBmHicgocmKsZdClnqZgS6NNixqFGf_lSTtQhukotkU2m0PpuirnshTP4-Qq44n5nvUJDitMppnFvmzNVV0RL1-EGzE1OvzcqqAVvn1OpbzrjYsln-2frPvo5NuJlHvYgu-JjPMaR4NlFyv_bzfB2k8qsVj1QNKscVEC7U8bfTaFjg4ocOi7wnHTG4FLL1uVMHrvPMvQe2uD-8A54pmeqb_RAwNTZTDbSjSXczXxuj6QCXZSb8wu_rvLYW-1FTFhuTAyP8siUbPxeM8w-XkjFpSsqIi-i5pn7EL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=o922nveyVzgavyobmaJmZfuNBM0-j8lb6BVCXsIf7zx2gRJdicwT5a7IAgpDaLmOpzcfPjdNzhHVl_QL1edvKdw7LBXcHxjGXltuG_pQZmYJVbXtDb40zfGXOgYr12glAHUPC4neeYvGP4T3bY43DuZPrksPc9oafnYruGbQuEaT_sBFPQXbE46l50VQSl4jvugb9q1331fXfHfbBLRbDJsLCAp3a0Or9IsR1Z7KZzNx95jXN7oQlZvlPS0RORM8Th5INbhCiWKOcbYH9QMLFbAYA6KfuFeg0xPNJOkfZOp9IjUOtEET_NaOZioicn3kREWjA1gURcBLccAPQzNXhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=o922nveyVzgavyobmaJmZfuNBM0-j8lb6BVCXsIf7zx2gRJdicwT5a7IAgpDaLmOpzcfPjdNzhHVl_QL1edvKdw7LBXcHxjGXltuG_pQZmYJVbXtDb40zfGXOgYr12glAHUPC4neeYvGP4T3bY43DuZPrksPc9oafnYruGbQuEaT_sBFPQXbE46l50VQSl4jvugb9q1331fXfHfbBLRbDJsLCAp3a0Or9IsR1Z7KZzNx95jXN7oQlZvlPS0RORM8Th5INbhCiWKOcbYH9QMLFbAYA6KfuFeg0xPNJOkfZOp9IjUOtEET_NaOZioicn3kREWjA1gURcBLccAPQzNXhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=vpJxYoF7F6Auo8rG2gUHOau_whYpmFmd9oo6Krwr9P3NEdw1DpO5GMLLjvHSkHaykZJO8X1RPKunU1_0sc65b1k-CJdaCSjKuTOKNC_ddIJXGEFJgRHqpzK60aim2WsognX9WW1svgbaBqPtL-vx6h9kfGgauh1SI7yrawS0oHCVgHkOxZIEG5hHErddlxdaOZFky75IF6p4THmVQrPKg6puOk4FHQkZIRLrdTK4iV2a9rSQqtJMXoKnbs3yqnL9EAuUajZFCAqkRna0MTNM0WXSD-2GJeufO6DeG35FDD3aCQfNPkrz_2A-OrXsoSjjK8Pyv7EAOhD1wJZZs6DXuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=vpJxYoF7F6Auo8rG2gUHOau_whYpmFmd9oo6Krwr9P3NEdw1DpO5GMLLjvHSkHaykZJO8X1RPKunU1_0sc65b1k-CJdaCSjKuTOKNC_ddIJXGEFJgRHqpzK60aim2WsognX9WW1svgbaBqPtL-vx6h9kfGgauh1SI7yrawS0oHCVgHkOxZIEG5hHErddlxdaOZFky75IF6p4THmVQrPKg6puOk4FHQkZIRLrdTK4iV2a9rSQqtJMXoKnbs3yqnL9EAuUajZFCAqkRna0MTNM0WXSD-2GJeufO6DeG35FDD3aCQfNPkrz_2A-OrXsoSjjK8Pyv7EAOhD1wJZZs6DXuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=qWCwx69wF8pT7YqUXgN7-YXmww2v-cpjZlDhBv-ahqMThJUZjQJxW3ui_lPETAl7dk0rcvAF1kvPPpc2pNXoscSKa9-IE5MpmJ_IE0nN-BNWgBSErrPZulOPYfTUqTts7c3V_UtEe1UVp9IEoyFNEOONRjTJX5kYFK5JHmTTXZvFEoN0ack3tHrolmAwFzH__vabGbmjQQYNL6E-h3HEn7BD0Q0zL93c93N5nUc7m0AvCb2ucs0cN95wC0hhRAqySa1xnBe1v6Yfibbp2xyWjdyprmQ7UUKyKfgxbcffuPad0H5wQbeJLlhuq1NbxJfpWNkwrpAtG5RFbvJ0wOWE3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=qWCwx69wF8pT7YqUXgN7-YXmww2v-cpjZlDhBv-ahqMThJUZjQJxW3ui_lPETAl7dk0rcvAF1kvPPpc2pNXoscSKa9-IE5MpmJ_IE0nN-BNWgBSErrPZulOPYfTUqTts7c3V_UtEe1UVp9IEoyFNEOONRjTJX5kYFK5JHmTTXZvFEoN0ack3tHrolmAwFzH__vabGbmjQQYNL6E-h3HEn7BD0Q0zL93c93N5nUc7m0AvCb2ucs0cN95wC0hhRAqySa1xnBe1v6Yfibbp2xyWjdyprmQ7UUKyKfgxbcffuPad0H5wQbeJLlhuq1NbxJfpWNkwrpAtG5RFbvJ0wOWE3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX7KVlEf3wXWD5k3uMEZK6I-4_usQZKhYs62dmSgI8R3Y-AxvDcWiPbo0-WZKiTtNDFwpbN69_BF5Esl0VLSz25I4uODXItNYXwDdgFFIPptmapkrXEiXC4BOkk6uB7fX3VulYLeYZ1WEPZh_7IJEkPAVgK6YkdcQ8gnP8axQRF5XQ5J39uXDyrgDhbJZglKwXJNlLx93J00218kfMz7KHmCyVrP-ogESTiq3JwvWsxpONCQXMBBS3KSHyMkkJsqeOP2JQD5Bqjq6dlvpZkY0lfAVDBrw4VnD01i8jLWaFnyfE9jcpuJLFBIuwuO2FDPiQ3Yp_fXkYfXZJsZb-AZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=U3zhUJSS3sUwo10ovkXctYovzK3bNjxlNV6MhJkyMq49I5_FbL_e6_z9s9mnxdPI81kErAeCi5BlrYnbBJ3SfBX06FrcgXNUJYFHm7voS6fLwEam2et5txuqSrBir6_mpw2Yw4UvxAf4meybU-VIafsMYAJxeLPKV9fO6TNiDXkE8rddGXWaAYbUYoL7EZuFHWCyL2f9F0dtJDYVr3xygvBpfMBfr8ysir_lphsTprqi3ouxiq8QpH_0OceVVU9wG3SMyNh4a2EWGdItg5b1mA93khAu_xXX45jNeKD_yA6IiWj9ridr7m70CFJgAnVj69MRG7r0cNRgkYBw6jXJPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=U3zhUJSS3sUwo10ovkXctYovzK3bNjxlNV6MhJkyMq49I5_FbL_e6_z9s9mnxdPI81kErAeCi5BlrYnbBJ3SfBX06FrcgXNUJYFHm7voS6fLwEam2et5txuqSrBir6_mpw2Yw4UvxAf4meybU-VIafsMYAJxeLPKV9fO6TNiDXkE8rddGXWaAYbUYoL7EZuFHWCyL2f9F0dtJDYVr3xygvBpfMBfr8ysir_lphsTprqi3ouxiq8QpH_0OceVVU9wG3SMyNh4a2EWGdItg5b1mA93khAu_xXX45jNeKD_yA6IiWj9ridr7m70CFJgAnVj69MRG7r0cNRgkYBw6jXJPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o39DNK5M-RUPyrlq_zorEjzZ4bRb8tIeE9xPIXPFyK97wmf7tZTeI3tA9Ll9LB3eqduLxkODMvK-RCu8socFOInyURQpKY5tatvvFWleGXyhIrz5Jl_-OkYuB2rYYv7jJwvKyZ6SXFGiR4APwwi7k8ND5Yag21rCId5QunuscA3FVyNl1S3D59eUYz9pYO2-6uclmr4Fb1MtR8Vi_Wd4XQd8dMelj7fXOd_ncKDsf75u_c4HQJ1hV78FkhXiKNjPplzVBALSGWH5PLZ26jqz-CfHx7GN1ntFFcu240l8XbKeQZXZes_mvpeCG2fAJZY6BvUHRkz2PfecHdgmtTvO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=rtru8wbvDuER77aHoHhZfP8dS3UJDStmzk2WlY-xuz9A-U-xsAAA6HxdLz0oZLuifdbv1RKYypg-k_bn1sMK5c8h-bOJwTCYbSo8VmtpshBU74-M__Rx_ELNFfPfJpNc2J49wk7Zw1QSH2SYFOy0JLBn7hH159KieLjaHaAKIEvxotPDzmAkifCrlHC3HG2q44JL7Ka1nzJk2C5ti9oQlza2AWN7SoYcR1Ee7DdRCB8Jzwp8epNJpuwKAScn5oMe7x_ZCIBQzBqaecSEQhrm0OqquNrrsQcusJ4dpKxZQ6XZUdnoG4Td__Aj6b9jeBOGIy2EmFOHP9S4hdRt7rjvkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=rtru8wbvDuER77aHoHhZfP8dS3UJDStmzk2WlY-xuz9A-U-xsAAA6HxdLz0oZLuifdbv1RKYypg-k_bn1sMK5c8h-bOJwTCYbSo8VmtpshBU74-M__Rx_ELNFfPfJpNc2J49wk7Zw1QSH2SYFOy0JLBn7hH159KieLjaHaAKIEvxotPDzmAkifCrlHC3HG2q44JL7Ka1nzJk2C5ti9oQlza2AWN7SoYcR1Ee7DdRCB8Jzwp8epNJpuwKAScn5oMe7x_ZCIBQzBqaecSEQhrm0OqquNrrsQcusJ4dpKxZQ6XZUdnoG4Td__Aj6b9jeBOGIy2EmFOHP9S4hdRt7rjvkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qihz4BOEuAO8cL8w9XNpnbqZ8-Tv2If0Q4TAi9dSJ15619XI5zECd1MDfFegYW6nbTy3Hxh7l7Ub6aXfFBtxUupK-zjrSsjGcBashzwj8duXNwVOwFssDqbudtBrojq37QeCCPNhN0wDQGs1mOZ1m2YpMdMr7smpaiERsayHSNL-W6gMWhkD41eOL0BN5tM_TPlYbZvKqJ33H3Kl2DCTiQN7xWekutfTBKfll7dYbiGGLq9hVEkh_mb0u7AfpeD_HmkFYjAZUXa3KHazJby2gPgioqUHtYTLVxtCLTUltJtWDNlILml_attddChNanxg5_piasiJv0RwryeWnOsIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARWCP4RMC4QPzgDaaJjiasiABIHafKNjZOzdRIGmrFiUXdP40eedS2BdGRkxFLpq7vpon-SCqpelWIwbvGq4ts52Di7IvUY7WxzaljEXZnBS2DwdI56QppMEgAhqZhONybe4b-WpuATIHD14a3gj49rwutYTDu0CgsBngCarx7jrr8QO_fURjZpcrHo9bqnei1jgZ-hvnqy2eJbeMKH7G5tCqdDmkyQutEqJ1mmyNR850zN70ACgjxuONXPhbG8PGwXXiCO5ieC8WXmQPyvqqTJY1xmJxts0YUMUGQ9kfwVc5LrMmSMHXMccPpyQwm7Et7f5inHIqH8_WUTM5XxQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e--9qiAb7LhK-1kFBEoETn4ly5XpVaystsSrNwcwuVwlbouDaAO0e_vm6BuTkD2pljdRFnQE_kNSXAvSQCJPQxRmEt2mveDZvKAL6ZIa8pUnj_MI5c5DJgx9KR4vPiFCHmRn-HKZX9EtXPq-Z1mkbrlpqvsfIw_3tjBaAQdx8c-wn8fDdc2LDXRJ_bYlDausjk1xIFZUiTF5JhKLOkerJeTxUSphojWbL-oVjREfu3h9e4r6b09WVZsaEaHwW3Z7EwF1Okpkg8HG6Fk7Zq2iZc_eJiEoc4zuVNqfVT0IEq7D0H6YJGuDDtJSsp5s5pDwdHAFPvBJ_dgk_XW7ExmrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II5c8qn6RH10UgY2w-PwpBGMHz9f-lEZgW6xzN8_wIhe93RM_cO8DTu2ah0vu_WUKw_YwgekgffcAJeIE5-F8w4FIUT1TlcPI5cFQ9HDr5fN3wRORV4gk5NfU1dcq7x7l8UpYur3ajtHxnppqBg2FVae4hICUvzgyQ-LrfzX-4CwaKCiMxX30JUODKwQpibRrlbmYRd5rNrDZf8V_ac-N4b4xvL5SFJcgq5zKXLRACL0eVmsSddwbpPPvFmqHpemostnsJWXMYSYPjxXaEF5KjLd0KohxqjJZF7J6hChO_9eFJxY-e-VE-Fj9p5v9lw4SNNVmBqEiNqVvK9HJ5fY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NunhNlwj-nz6tCZabfFEeSX2jatpiFfR_NqmihsGqywRUeKWPoygpIYWAJ5ejq4IGJZ6YaoY6LcjqP-ng2NowtpH19niGwQd7-tJHNnHiYTIaBsCNT5ccxr6DyIy8GTvB1125WszfJDnSfLkNocO-A0aXdUP3N_q-etWL0lpntHUtICiFw1tlt-Rzj-_AW3Xhrog7wZ15ChprpaDBlaXXfAHRHPA7DPVoZb7UV796PFLnDEh3OTPGVhXsXdLhdoq2ZfsHMw9Fj5S2L5TSS3NXj1JroZBGueCBfjszjmAbAfxrXRPXomAtOZtp5a1kyNNN23PN_PXERQzE9Ee1q-hAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoFuYgBbuBSQVgZE0Qlcfl9LWI1FKwvMDTUXdZKLOJSWnB2MF1Bl-5eoy0o2RANEkv6MuwgJSkOH_fsYtfS0jtQLw9fCq5GJTZnd4aKfVNHm0nd8Zly80n554iGDgh_15zJCqn8li318VkW7lh0XUeO86QXQTMJuTrXtlLleNcB11_RGGjBxBsIMc_5RT0Ba8LCX4i97HHhblzIOooSfvT75ygW8SD6yempqh8Npky2OB-K7JMaLLVyLkxZueXSsB5D5Y0DyynTEboruODGv5MvTR3_3TPVxhZVnGpqy7PPaCWD3YJxbUN3vZTC2b6rUOVHTNUQPk2mbY9aF5XWfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjPNp9c1RwruprchVuI_cNSYj8aKhPuw6wbJvcWE7FKbFbl5MgglhPmTIoUhS8jagY9S_9lRAaAHbYOE3LhRcMpySNch8K82oF8n7Pb7ENJgslM6yXEXMFTMNoBUx9u6oIfsitBgbrXD_pEVV7cd-LViTI9q-DS5pZPgcNWnskml75coEPyQHJqtMixpj_644dXo_Ws3WMowsXteJUmDBC9_vldBK4XDwiGe7D3sne7WYPNiD9F09p9aKbXrrjOy1q8wdvhE55X2QAeTsLQuqpPYmVtbwggMhPPEQf5MjfHGOrFxyAbjLWIAyLWOQEt311eKlLTO7LUtnH9dvbjsKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vci01dy1fjnPDyIASlHCmAshMZXSCx_huVMZiX8kzf91_l141PHg80g5oqxLpvd_PuLzQ8IV2I69fDDCrOIN1l5RwZtxm5PscFRlonpHn0tFf8_K0JiTDimY_SQDXtOTJtcTxDryKtLwL3z6kS84PcvQ6MMQPvirswQRmV9-W1kE9pAyR2OeC1lelodLfj563KAfTeKx-oJfXJwcZcGimvlfzcCaCyhtZZxF7MQgio_qdIdfEeP7GIbvG6jliTQEmwkoTS6Rr6EFXn0i5W9sjkS0a9wiXllfiFUW7Q85PVNIOr5fbFEcfTrG1GzYwkTA_keFWJLiwrVrsyeyth_3QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=exN9tbjL_AoIpJo6x_YhmYcKp1Ck2P-4X40ub7e6TJBG5sRbx-Cm_ZlhkK9jNXFzRUQBYiGCO1qhueA50-tb690NPcFDvMRO2qOH-tawEQEOm46v4QViIJxiBtGXoEUlOvx7zeYwABheqL9m_jul5Y--BNEd_CiNAOCvlgxX8Lz9YRx8B2Ijxy4LZx9xAJf7wKLHBoDAupe6MUT4uxJJVOQDj4HiAb5dOXTFoLp-zfvSoyZ1G-op6WPewAOWA3W6OAbcjNxJb9w2O1gpkGtgmgt70O_asFWvYJrBNQb8eFvlXKRILH8c5bC8RIaj9ZT8tWp8IPhzA20pHEzhaxWpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=exN9tbjL_AoIpJo6x_YhmYcKp1Ck2P-4X40ub7e6TJBG5sRbx-Cm_ZlhkK9jNXFzRUQBYiGCO1qhueA50-tb690NPcFDvMRO2qOH-tawEQEOm46v4QViIJxiBtGXoEUlOvx7zeYwABheqL9m_jul5Y--BNEd_CiNAOCvlgxX8Lz9YRx8B2Ijxy4LZx9xAJf7wKLHBoDAupe6MUT4uxJJVOQDj4HiAb5dOXTFoLp-zfvSoyZ1G-op6WPewAOWA3W6OAbcjNxJb9w2O1gpkGtgmgt70O_asFWvYJrBNQb8eFvlXKRILH8c5bC8RIaj9ZT8tWp8IPhzA20pHEzhaxWpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8vL-8HY5qw34DlauVmMNHa32styGWQ_H5xb4vqQTcE0nFKtES2rJ-yIYA0WTtsXo4VgjoT9biSZQ0SVqGEa8QJigMex4O58RE-ARzEn1PUlHfXCS0tjbCfNjBqur-eI5CJG3PfKZzSVfTUARsv66zpOho7kM1-hfI9y-8pHTlqde_p8NcRQpL18HL2KNpNik_DQ7xNeiCNkiasDlFNBq77y5IYppMjU0tT3nTwvqTXL5onqQw4PRTwSVEZJdn5fruXuV7IVd9dZjX2o86EPJQyXbrVNMf3YzZjMkOIF0NNcftbkF-gZmpUIwssZFo_HHKdkrPIrFX9VIiD16pjQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Adz3lE28tQ6S4yOYLMNYRKHwJv_XY102VOuVd5V1S8IYTMfe8gUCENNFrwzUk0xnyN7hOXOXI_lpAv_tp7zpEP1CpgDJrQo4_shwee4WgjuMCd935hdJnJLJIAzqCUQSJ76KWKfu-0MGIHsAVNCQ6Hp-_Kj0JT08FiDec-wA_wziVIlB-ncBPtDLIvU5THechnIgasUVVlaKJBrjXgRBuTreT7tDP-wFiWvcTbhRdO5LXCgKyokqEcEhBK9UCzjt4LXbgANxm_02MOll3vvYRMSwBmy9ZLTXlxFPMDFOWT83p7qoIu-Mj6Tcjg5B6dl9uo31mkYSuHKhbcPEiWG2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz7YI6ZxozjmFZsIfTf6krR796Nro6mQmBzJkez5PWhkp4__Od-_ulGPMVHI94KA4BHnE0a7PuIMdDzvLG12PStMsRmFV8VkSyjuwcm652sq0xex2nQbdkXbzVKtF0KO5RHiJVxLp3kYFnR82wb8oL4Wv7SL3_DV_57rwR52A1lSJY8auQOx-3RE994DHUMBYCMqlxYlSEZUNUgEGsqNpDOebt-DZ51RG_0ky1q-O-3J8FXol5rHRLUzmZ8cOjvGaJZLElas5H7IPdxgwToDlHyxXMaN5TmztJ1B6ZPnvg0qQScWBGY8ofSrlth91-Sk3zh-LWXYUGB9K2TBaiQh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvyul9cuUgv3JnRIpbD5DM6uGcFbPYKBUzHzgtIK-6JGM3y2QlVH_QAwybhkTaeqWcHdgoe5H_bdCYEhsY4CGqi68m8MiU2YSXtT2IrfTUHPz3_LYMkQ7W_WUDoboUTqm2uze4GJ9NaovAq5vHSdaOJeS5Ii0RAedig6axbA4SWpeh3g1VYAF2v3v2f6NqQeCuzojiuVyfN2OH42QH3ZO7KHGGg1yECJPg9VCDChPahLASF7Zzq70uXnAg5FEd9jmH4jhnsjefL81_97edtIOQ8LrursqrYJfqXPO6ty1AGUdqFzBtF-Ar61SGzomi8dS3BAfZYfJkw8L8gZ3AMFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKw5kQlMS03N42XT1jnR8JCRPYjHlK7Ogu7d6SIbr5QqSUgpEjBYGPVR1YXivByADPj7ZA6l4cZuJvC4d2TqIWIGrpNUmu-2jfK9Py50vTPgpvEagmqs4v-q21K07vsjsCqvYSD4_2vTuAFxjqGK-kUMmCbTZMlQKHeOD78aZcl0EcddzkHki2syy4HxaAM382aF6RwZGcukXS6-3BdAqpL0ibas7A8GEWSDZ1JOC-SDxOMzKFuJ_Qth3-AUAA_Q4Mg1Hrw62NUOjP0VdJt3k_vbCZkdkO4pJBHTxq4hjGodvsP3TXsM_HfRAFx_27ySQIGv-KRc6DygCWD0tPQ6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=e5bDA6Hw9DtbQPys3jOmXHT7jxM6xr3jbbZZX2RCRX1MXFUwSUs6PjHaH4uRp-w3iYnVsYzr6E28QLsYASrWFH-tFU7yjMcbC_9SX4Yu3Vtm8EertEKRzHlkoeEEDmuPTg4jjehXb6abxXZvy-f6upKxmZh5cEQGFWQfW0ggpIuqXHnm53Ui6M3SHBVBDkpny-V14WRPrC-VDDxfOQCkjQWMZXiqEStM8X2HASp0CnnG_mCkJs8fRIEJLpWZ1Ne16dQ5AZ_Iud2V8WO-81rlWG-7_4Mgic7g7SRiBCxHqiBsTSkVI2S-gV126FoF9ocnEWjikIMFCKCBYq6dUorn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=e5bDA6Hw9DtbQPys3jOmXHT7jxM6xr3jbbZZX2RCRX1MXFUwSUs6PjHaH4uRp-w3iYnVsYzr6E28QLsYASrWFH-tFU7yjMcbC_9SX4Yu3Vtm8EertEKRzHlkoeEEDmuPTg4jjehXb6abxXZvy-f6upKxmZh5cEQGFWQfW0ggpIuqXHnm53Ui6M3SHBVBDkpny-V14WRPrC-VDDxfOQCkjQWMZXiqEStM8X2HASp0CnnG_mCkJs8fRIEJLpWZ1Ne16dQ5AZ_Iud2V8WO-81rlWG-7_4Mgic7g7SRiBCxHqiBsTSkVI2S-gV126FoF9ocnEWjikIMFCKCBYq6dUorn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asNY7Qta89u_ifM37FjeZ_DB5_MleaSxk5zlMY9tprl7dHxfTCQtL9Qihh4ZGpaZtTSWeh3u01US5DeNVCVkY2YOv3HE25H5kUZUTE7hsIuJSQz8govHIKZA6N0bUTWDXD3w1ocx7qgO1cR-DpS0lxQ79rIKvfXB_2W1-aILKeDUt1ULzA1hyLZ-MRih3vsWOYLC7hN2BxiPxCFbM4Ice_D_J0zxY5Tpu_Pvcgyf-2LOHCzkrA6keaZyc-DvNEYLbXpvWTY5RsTNqN0Wd8AOSr91F_LEE8dKbNsDaOGXfYl_q8y45F7XJrveKhW4pDGt5rpYLB7kfeHrD-q8gdf2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=X9JOzRFBDQyVzSlePBkA5WIkwNrWNOPZGiat2twrmPChQOJkBty3kMluK1rmlnzt__yQdABx2IcvJolomuUIh0diiaP7Qrxo6InLG-YoZQzy5mSJKkAnRhKt07kKGegv_Hv3Xss1QOll6IaU9brSRuGEcbM8OE0ICHAvv9DNxMErSOHyLs6cEuc3hvurZyA81bWOoPQ_G6d-MPqJSCvDkz8X5-bcinx2Xju6AKBxnOXodcdF94vQVh57DKUet48GZQXZCx63UslFEG1pSWxbuySoOaEWxQL9Nzm-CW2uZvsOZ157dxy0R0Xo8032eAixuR_hEh9Hz2qX2GB-9bmy2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=X9JOzRFBDQyVzSlePBkA5WIkwNrWNOPZGiat2twrmPChQOJkBty3kMluK1rmlnzt__yQdABx2IcvJolomuUIh0diiaP7Qrxo6InLG-YoZQzy5mSJKkAnRhKt07kKGegv_Hv3Xss1QOll6IaU9brSRuGEcbM8OE0ICHAvv9DNxMErSOHyLs6cEuc3hvurZyA81bWOoPQ_G6d-MPqJSCvDkz8X5-bcinx2Xju6AKBxnOXodcdF94vQVh57DKUet48GZQXZCx63UslFEG1pSWxbuySoOaEWxQL9Nzm-CW2uZvsOZ157dxy0R0Xo8032eAixuR_hEh9Hz2qX2GB-9bmy2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=eGWxipwYZCIWeoL0roTYO5mffCw5v9EYMX-jELkPIAtz8ABDmC_9xDC-epqT3JbN3UVphY4oEl3R5Ra-fwj6bZWEjyGDromVtd5U9jgrriujWKXu3UTX2qO-ilSY8aWe8EIiF8CIPTKUhxScrJtiR34BG7Ra1qHIuQbxQdJYnXM12KvMdGFL0AB5RBwdUwMTcp8LAjjDZLE6h9X_97SAZOwRvmXo18i6MlYR1mmTUuKmXJpYgKfx890pyx5L5acE9Du-DXkugoBPcrHJWhimzKw813N6QWEC91nJncCpjvLNtdqP7l7KhfpCRZaegbRiqI5IFFkgJqTZ4Ca2ecXRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=eGWxipwYZCIWeoL0roTYO5mffCw5v9EYMX-jELkPIAtz8ABDmC_9xDC-epqT3JbN3UVphY4oEl3R5Ra-fwj6bZWEjyGDromVtd5U9jgrriujWKXu3UTX2qO-ilSY8aWe8EIiF8CIPTKUhxScrJtiR34BG7Ra1qHIuQbxQdJYnXM12KvMdGFL0AB5RBwdUwMTcp8LAjjDZLE6h9X_97SAZOwRvmXo18i6MlYR1mmTUuKmXJpYgKfx890pyx5L5acE9Du-DXkugoBPcrHJWhimzKw813N6QWEC91nJncCpjvLNtdqP7l7KhfpCRZaegbRiqI5IFFkgJqTZ4Ca2ecXRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
