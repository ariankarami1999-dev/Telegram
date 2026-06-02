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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 08:37:57</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTKFRwykCe81o0z4NmeRxflVSlrkwvG5iWbiUGdDBPhbT92MhhfM7x0Er5dNuOYIneXXc5Ios1I6nU_rkaRwzdAVv38g74lMfYj1JvUZQvj-yogTnLbcW75yN37v9RZMwbsc-f4AaCXFqspzRNOw0qTelLmM4D4OBaQ0yo1WXfpFNYS6GaXRFY4lWfdrROYT1vDaPrRs_YnJlFtbN-nyfCEx6Dxia5cAac_zdz7eKF7aAJ9afMcNtQe_ipV3D3clXO3rNc9Y6sz3PMZ9J5htKnsCfgyWIsKcyM4GgCtG3mXRwdOZDvk3T-_LHTtOJL-Yp8FDr6mJR1MKeakFE7rCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1t3qGLXPPYSYQDKG3Ik_NSEHVIvqehPanKbmwfRFvjKms45b_cYe95iHq8zzrNfcaTyrmQkPAt3hu72Agg7rlkfA-acs8cTMZlHBf2JQHFgB8yKMeXq7xjFtC7qMMus8KuJeD9BMY8m0QrCGbXkj-aL0ANUahM0nprOWmvmUMBinywR-dSjHGXheDV9ZpOTdbCoyDf7hPoJjxvqeMIS_yv-ZYhnwM6tT7T5TkWrruCCSAaEiI6Kd2kzh_gPFFrB9nEUFo-JnGX9Z6nJbHy3fdHaAQlp6eK0jEFwRrhPjLdjD2UlJWEtrHValaJ03AzpklYAK8fHtjylOXWJOfBl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qolsH6FJvRRzcI6L-9qb0zFud1_weD0X_OVRMbq_g58h2YNPzV9nAtyEpaK05LnG9zvbXcY-vItP-MWkBnX4fAo5lvhgV-shA4egWgNM0eNg5q1u4d6h094rU_LGUu-YJQAEAfNfLcku-uS3Rb86qDBWWDiY1t9UVpZ6e_XJa3WtzdDFJSLJxREenm3U5556OF5WaW6pJuwX2eWJf6O31D8wR3U08En3USm81BzJZzpk2qf08Z1WryjJzkGjJ5tMNGpPDRgWmdf0JnIM0ezFCw7XkjLcdUocKX0bQNZqwabFfsOEQQlZUSd2zdN1qy9Ew7ut_NFErYfNExtvj3UFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRxQ3GL7Rr_iQ31_xBU6WKXq77WPnD2KVBpPWidBnZ3-_bZ0BCutmvCjfcTPcDa0sn17yredtD8LOLYs86bjnNGcnnqToFZQjQdG79tqZMzF5kblA9e9BUZPSSMnXEFruUTXI9WPOoE3-lMXmWNviSXAWIdCaa3v4MkvkIacEEohf9GcUBp7WoWUhsrkfZIwV2oeewA1IrXjloYlEnv1bDw0n-2Z9Lj1syRJSRSREomGAzukEOamqWpwbKpj2CkCoGE0YYL9wO6UGBlg0buxVYj2B7t1ko814onRaf-Ae6xeOTd4m5k6nwzwl0C_8xb3MN4tW_kmMjxXqOL28N47uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmoBdfJ3Eps7x7Up04Dk98WrE6w24RofCeMmBpfN_mLWfCSBOI2S34keQkt7jmKx85mjChOdDhSnfe-GYhaCpdOc8z1VcKBjyKEhFJjWLlEllrs7veRRMEiY-dv-a0vU4XaMpKDR0rmaPiAM1-jof2TL_IkwxdfLdZF7pd9TSzcWL3t893EZ2r6Z_JmmibfspU02tOKehoWqpeRm4i4ObLOYAzjS-0zJj05tiKmv-oLLt_wwrTb1rk2xYanTvC5jDPVTlycaUoS17QcJvuKM1x1BemauNP0h3am225WlxLUn4mJC-zlfVaCrxKnZOpC33OJ31O3sV5gLyM5ZJdiZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jdo3C-aUBNy2EQh2ybAzt69PdBhsCa3piHHPiO2kHMTTUDWT2k50xVHoksZ5Qvp51BtWDFUTgnRS_jI1sB74NHwIgpX0UVvX0_55jfHBXomi_frzujIxvW-ZUN76GVsTfbOPq5AZTt9CX2EznxiBjNY1RS0Lm5YoAPCwRaDL6Ay7GG8aRAb9HMOOAEVQLU8l33a1Zsu2t8ncONXu5PJE81RyPWYkFULnzZb7SmPhZZqK1Jo9rqYrUYbIL7pjf3l9xE-L8M11d3wEuAqo793cFyY2jKX54g1JcwyPvlv5Vj0x-cYPyKcnOkDwsigFwVMj8fEmxIlvSqYaWpJQkItAXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu828bLFPXf7z-tcJe449HY559hg0RUwyXlDRmQ-BKy45KaQaUk6EBQr_W5eW9NtALOUsWc69dnBpQe0UiYTUQQOirzA3kn6fm_il65NeldEDSViolkUc3gJgJFX3cYDbnqvJVCe1sX2Oww1JOGdktPYzxnCVwABUXmO33q9BVKMLZwMdNfl0m2gDoFL9PauExbCuUt17gFfOukqoQwBNPyZ--3mcpdvW_vx_9K5-N-OFrF985HPARJ_jXaC8Yt5Yynb31ORw4EsnXwLVMZYDA0TO4iaJCo2_xV5MGvJzv03A2x096ukvjTe-K_0UCJBjipnlkyEE0HZqr57STgkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=M1XzM0yEt8MzyYJjPjRCTuNDTVqYcUGWFZKdQfYPhb2zZuCMpLzh62-Asw7x8xzKBq6xYeqET_kg8v821uT1GI39sISRmecTPqHzFAHKiKecDqIvWALKbfjveRmbLJ_sFnkz9wojDe19ReCqFREy5KkoZ3wZfitNHi32nZ5KrtOc6oLIe0GzgDml4ULpwOri0hfa4N_ZegMOLpr23FPdRUPzVKOdLEpSLIDhB7g37OzP5bhb3ur4-n4xmsQxG_JJqfv19urWuy5FT2wSCS1chCzkE69DD7o-HkI33zxR3ZaZXTUz8_W_fDm-ts4LD7PpzXVXsDmiyVP7Bmv4DGHTBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=M1XzM0yEt8MzyYJjPjRCTuNDTVqYcUGWFZKdQfYPhb2zZuCMpLzh62-Asw7x8xzKBq6xYeqET_kg8v821uT1GI39sISRmecTPqHzFAHKiKecDqIvWALKbfjveRmbLJ_sFnkz9wojDe19ReCqFREy5KkoZ3wZfitNHi32nZ5KrtOc6oLIe0GzgDml4ULpwOri0hfa4N_ZegMOLpr23FPdRUPzVKOdLEpSLIDhB7g37OzP5bhb3ur4-n4xmsQxG_JJqfv19urWuy5FT2wSCS1chCzkE69DD7o-HkI33zxR3ZaZXTUz8_W_fDm-ts4LD7PpzXVXsDmiyVP7Bmv4DGHTBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=CxKfUE5-7dIZHBFzkraRTlH5fy6nEc7_DXzn8xTL4p3Z5FXDoWD-oAyXyvVs-U6WsP1pv1vanYiIFMSAs1DZadG206qxyPx8sFKhfXg1GWQ96iR3a_C4SaN_fLwFHg7xAG85gbtg0ZVPGlZma6R6TSQ9yZUaw1Rq-CtCUCRSlyway-Vc-BO_ibICHf3cu4fl7z08XudiXOwQIJGM6Z3vHUSbwBJtrdh7-T75x5CY2_0_wHTpYU-FOYxUAhOXU_kPpE9qda4gTtNBqGqWtfyFi9wOowLtAbS3Ye3B7nsmLde2bbJede6l198wjYyS63xE_EBaQKS4CtrFEjKMbP90aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=CxKfUE5-7dIZHBFzkraRTlH5fy6nEc7_DXzn8xTL4p3Z5FXDoWD-oAyXyvVs-U6WsP1pv1vanYiIFMSAs1DZadG206qxyPx8sFKhfXg1GWQ96iR3a_C4SaN_fLwFHg7xAG85gbtg0ZVPGlZma6R6TSQ9yZUaw1Rq-CtCUCRSlyway-Vc-BO_ibICHf3cu4fl7z08XudiXOwQIJGM6Z3vHUSbwBJtrdh7-T75x5CY2_0_wHTpYU-FOYxUAhOXU_kPpE9qda4gTtNBqGqWtfyFi9wOowLtAbS3Ye3B7nsmLde2bbJede6l198wjYyS63xE_EBaQKS4CtrFEjKMbP90aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Muce9x6ra2GDfVu4h7j8lixitnov_VRqTOgcxnUtEMldPAx1WPsXX0nWgf1ml9PY-fFS67VxOif-f6m5XfQUcni1PNnLMVWO827vF1-a_uO_VwwkrySlGnomr5h5flOVTKjL4RGxvLaLpb3LN0gsToFKl7AYqfTYlnC_d1Ux8DqiVXSq0dbD7MsrqhpK80a7oUx9VwvH0L3PgdIvz6t-l0c7j37SVueMGL4XFjCiwz_15zd0aWgJcV8q9Zs2DKFLhgKgd_TcjUdiM0ACQ5XbobpMkgwFNfVwBClCuRHGFUkNlZAvseESccDyF7Acn24v7_AMcrjYqDB2OUfsj6Wd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=gaB988QGAtwl-PBPBMuVixMpqqeb1uEnN5MC6A4VJfKKWj41AD_otIyG_Vz1ZRKudCptT3YiWLHN-Z_3nlbLz4I5mEJAXGHtlSuWa5oxxuJfBgoWE7HF9igHavHJJxkElgZCPmv-zhOXw8QtH_0xwIYA7SPPLPVo6kfoWI_Yo32bJWJgIuMKCKqRLoOW4mBMnaB3-8SDYImotVldRQpnefN6BtItgCWpK7GHocSSV-saub-xuo1xYLfneaefY9HAUatGkJDkJrYWczcrKoYbxSaGr36s9fch1hJEGnXLalp-nkaaauI0-oN7ODpywQ8v0bfWpJFt4EGG8kA85OqX7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=gaB988QGAtwl-PBPBMuVixMpqqeb1uEnN5MC6A4VJfKKWj41AD_otIyG_Vz1ZRKudCptT3YiWLHN-Z_3nlbLz4I5mEJAXGHtlSuWa5oxxuJfBgoWE7HF9igHavHJJxkElgZCPmv-zhOXw8QtH_0xwIYA7SPPLPVo6kfoWI_Yo32bJWJgIuMKCKqRLoOW4mBMnaB3-8SDYImotVldRQpnefN6BtItgCWpK7GHocSSV-saub-xuo1xYLfneaefY9HAUatGkJDkJrYWczcrKoYbxSaGr36s9fch1hJEGnXLalp-nkaaauI0-oN7ODpywQ8v0bfWpJFt4EGG8kA85OqX7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvbU32VH5NuhhkK9ieduh5wQdnnr5a1Nk3VJy862XpFzbOdyez7hGEf0EvZ331aVw1MJvzMTL0RfHjvmm18jQ3U0D7pD3AOMj2q9djT-Uf8d5tvGiCj_e9SZRmPQoOxkN-qSEu186JRBeGU6_V7fYuZT-pB7IPTC51VXrf1CWY5VpSteNyFUy5C6_LHI06cniYzGNHcHVcoY0eaK3AnNxZwjPj9LkAR3MF07z1wiWQtQGebiynkWh6HZ-RCMUWyi6I0oTc8nrkuObQmPCZggQCY3SOaO52h2l3j2j4g1UzT3pWjDUAmgHy-VuoHiSzHOTXkbr93TNFlGsT-t_B8Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEDYyS-sFG_IrQoNCL2VULirl8-HrmPzq6jrpuWYk8mawFwlOFMxP3lBEi2h3lpyqRw2AysdzqbiMkNEew4liAAh57ugcAz4iGmguutPk_9IqIYRcNhf5OMkEDGnUq5k0o8_UnOWNP81cCQAzYNT2XB1HoiI73Xyo6V1Pv-oUF95gJuOFUjnEDbFBNG4I5GN4w0l3VV4oCpFgEM6tz6pmV8EoO8s31xz98P0tuTJIzQwuP2X3nnzUQkaGTYIsYc00mPiL7vjwhqJDAI3FGYwYh2J8Ut795BHbr407LNBZiqctrAi8PC_Ve--sGN877e8N4dN3jM_6mlqXexUzJCGnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATf2gESEAD3T2TTM6WoF0K4w_EZgD41chfdd4AQ-meM8FmJ-RPfrRhPE7R7iLQQdWz0kzCnBhejAMsvbvIZslL6MwgF6yE7wfnxRT_ImVLhNxBX6b4eZY89qdRjzyAiac32JjDo3KGJWv4kX6L7ZQjvIZydsDNIb9OlXLtLzhfiylTFvvSMtqeHMjWs-HgWr491GrVnYbhjGPhbnXvSppiIe3MzmerUM_mcbrTLDFCfKEm3ZgZMfwQRm48VgBkX9bvmAKhh5tSZg4ocrapwFHN1gHPh7UhoYEY_yvpVmzwnkUGci7zytkTf5NOy3zURSjhLK80LQkrOrV7n2euWxMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IVtgp9BEYUSdmfNIRFxQ1fXWY0w7KNuVplPzt7uAstJOIeH5jN9Qn1ijkDrQ7rpCDXfNVdOVh18lznMz5PtOdZTYXPMUp7nqZfDeM9QB_ur3DNqNzGTVKkbm1-onSKVeKWEgHWGLlW4s1b8o18jPsvWwD_27LWSXsG_iOGR0vY2-nsnPIIjqKY7xnq6hj0GVvb1Mz_5Ve3YMgaIL9tlx8Q9wbLW5I4lW1I13GUuQfCe6nDC1TkOrMY5n6Clzy5KkJ3xsx18mApPZ0G3vDQRHCaSIfYVl-DJ9yy_H62lpHeqsI_2LLD4laLny8a6tZtKvfSV6epizexnZKnJkLJ-Cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEc34Zx_bFUpvdUc3bsYPkiSy-NnwOVD9ROk9NZjIsgemeswcBAYN1uCeciygn8wgN-r5Nr62ZHhf829TQDhaOI6YqLmRqnR4jPjScX9sQo5aOLRf_YohX9VB3lQHyw5OzHB_eRr9PIdj2NxpFUsZLcIsi3vaGjGnDpoDC9jMeDCCBdNNFUSmDGGNPiMNsID1JPYTxHQ_oS3PR5IsFWs7jJryD_vKY-u9YPXfy8OfXcsVsy7aN0rar4QRRe2wvsLgIYMY-Zu4CPmFxn9MwLbXyMEZs_Wh4_HKRruUcrQL_0B-07R7tSGiDYF5mGSWYJ3fkdAVvxIYg-LtCBJQSSaUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MiaXzKszV5ycsw1wbPzCvx2ovkJB_ZbAEyntbK-IHXjHkrHZMrTe-3Ymbd__qZjfuLPiZGk-Yjh5tQaLY140O5-0pePNRGCf0eJfKLVFbaQA0Vi3bScRPYot3l_oaDXtct0CulU0OCchyeKUUrnFBZ_zfwMj6EuocGghbQfoPq7mwaUypSBAqjFgMQU9VTQERvzZFpcC3tnIYsg43nV8AMl_rMn-GzxDPXCrBf84C9r4ANegwk5kKwQQVR13EEpKbMTppWt6UEAgrfeWiRjCJ1Nd2kx0RRGW8-dl_xwzMlJavdR1YXWJt2qznb9xLXLl67cIKOvWl_GvzgReNuyU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnOlB2Dn_iMjbjgU4MMVpRR9zOUb7GdrtC_D0twJnjN5AgPRJzb3YKu34G1c_KULA9WxdogwzBckPMvp-VRAMb03dPzDHf7ynwNyXU5OiBziybDWYGlJYXjKic1_PKahLWF2XGWRNcer59BYTrvHWt5sgf8GYXU9XF5jbAc05Zo_HC-wQxMPUW4Q_D2Nz8cACpI0sBLAZb0Uq0o3_VhwdczQ8iGymTaZUNskI8cR-Yhb16H35GrkUJBqsOt16AwE2mKqj0WuT3ku8yxmPWIRnA4hvs0VQtsM6ha7qntmA0OmwJAKkKL5DLHSXmErKAJGEH8zgQMJ8iR6IOK3aUmuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwHd1vKWMQMRf20ubvPG8yCXEwv2Egu415BpLHQEEn1E59IPh9dG0t8tphJwhqfrsG0OfNmr3Lh3jNGcGMh-9v5Lc3dYi1vK2ls1HFP49AVG884Cm5VQc3ST4CazxBbIYq_46VlMdYxBTTJEVv1l90y29IiceJgXxRwEYvRs_WcWVGJ2Ed1IeeUKOktJTQ7sR2GWR-Z0_TafToTsx33yTTiuXFKzKckUHw4CRgy1vlSsmJyCiGNIfeyg9e0VUcjqw65U8VdY1-wGWXiEUxmCG1ozF7AlbPAjsgqXkvPe8tS21po7mohpDTirD4JhotY8tZFuT6Y-FzX3vBiwaTu6mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=TbK-9KIdqxUg08MvvFwfChnetuLKbzmDnI4BC1UodnfQZgLLD6-5qOxX7SPwN7ZfGQjPMOif_L7fhLQ3gwcJ9Xv09ALzAW4_RYOm_dKM0CVxx5RXo01Jm30TVBokUOg0wyERMBTcoDfOOpX8AaQLQPaLgDBsfNY3Pe2nLz7YaEPVNcYzmv2E5Shmg7Hl1Qf4EHUTk7yv5ojgt8rn2Cb6J8WVCGo0SvfHifegkEGfcLkF0aMdEQ3PBUKaao9jeUr3uriEHZwSmlMqBBzt113nJoojpmXblJmmnF6cHoGRTXEVZJVu8VlCj0M2u0tgsHR5ru10828YdKO7UUtKWFkw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=TbK-9KIdqxUg08MvvFwfChnetuLKbzmDnI4BC1UodnfQZgLLD6-5qOxX7SPwN7ZfGQjPMOif_L7fhLQ3gwcJ9Xv09ALzAW4_RYOm_dKM0CVxx5RXo01Jm30TVBokUOg0wyERMBTcoDfOOpX8AaQLQPaLgDBsfNY3Pe2nLz7YaEPVNcYzmv2E5Shmg7Hl1Qf4EHUTk7yv5ojgt8rn2Cb6J8WVCGo0SvfHifegkEGfcLkF0aMdEQ3PBUKaao9jeUr3uriEHZwSmlMqBBzt113nJoojpmXblJmmnF6cHoGRTXEVZJVu8VlCj0M2u0tgsHR5ru10828YdKO7UUtKWFkw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=sspqtxBd2Cl0bXCsfbceSQSvYg7Jd7bgw0LON1xvvFv_o8xKH4Un9L8dBp4XHd_Y_c3E1PYCJbKi_nKdYQCt8mnlhaKE48Y6YKNiRcUSmtC4lEuG0mSVL5WzlQcrCXIZS2RcUCom85Xolp4S_5Rsj8rtuSuf8ypZJXuQIKZm2SQCJEOoR9Kze_nS3l6WysBCeAJvCoTSOPoHmXoav4kw3oCFACWGG0zJjrXYScLnUSKf3X8hY_iGsqqunLjUtv80rT1WJgCmg7Ps0qEl0iB_-936FC1XhUhIb8w_CxfwysGZYqdLwCbq5U0DAGQhc3SpAqWQpR_1qMAfAX0PKjHLzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=sspqtxBd2Cl0bXCsfbceSQSvYg7Jd7bgw0LON1xvvFv_o8xKH4Un9L8dBp4XHd_Y_c3E1PYCJbKi_nKdYQCt8mnlhaKE48Y6YKNiRcUSmtC4lEuG0mSVL5WzlQcrCXIZS2RcUCom85Xolp4S_5Rsj8rtuSuf8ypZJXuQIKZm2SQCJEOoR9Kze_nS3l6WysBCeAJvCoTSOPoHmXoav4kw3oCFACWGG0zJjrXYScLnUSKf3X8hY_iGsqqunLjUtv80rT1WJgCmg7Ps0qEl0iB_-936FC1XhUhIb8w_CxfwysGZYqdLwCbq5U0DAGQhc3SpAqWQpR_1qMAfAX0PKjHLzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=CbWGVC1Ors3sSRffLwzgSJEcAGF2qU0M2VpS9UlVFEEbPli803_pE_SSy8wj0EAUHJzHUiKIMzGwxL0eMnDck0Ocyiv50aKBp1K8C2r_E-iMKh1FNhDpYkGoWziR-d_AOxetmsub8dah2IJdwvjREHIrPAAcbX7hPRiIsCu-wiznqEwE2xWdEP6OWImFZbFzq85r6frP49hg2FNPvKJSXetGdPhE2GUpNHQpNo0AqcZYnt9W1tREwZU9Ar0B7v4U6aaKgBzU1FckQ880E4mLGVoCu7VM6Qv24Ho0Cb6sOleqn7007o72fdVCM4e2-rVJQOjXze6v09mMIu4JPeMZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=CbWGVC1Ors3sSRffLwzgSJEcAGF2qU0M2VpS9UlVFEEbPli803_pE_SSy8wj0EAUHJzHUiKIMzGwxL0eMnDck0Ocyiv50aKBp1K8C2r_E-iMKh1FNhDpYkGoWziR-d_AOxetmsub8dah2IJdwvjREHIrPAAcbX7hPRiIsCu-wiznqEwE2xWdEP6OWImFZbFzq85r6frP49hg2FNPvKJSXetGdPhE2GUpNHQpNo0AqcZYnt9W1tREwZU9Ar0B7v4U6aaKgBzU1FckQ880E4mLGVoCu7VM6Qv24Ho0Cb6sOleqn7007o72fdVCM4e2-rVJQOjXze6v09mMIu4JPeMZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5VOZ1_o7T6OGBSMVS-Ria-etuYNqBvtNOtPdos4TrN7OVMuLnPA5dWBDgho1qFJrcNcQmTEI98CdRYyM4Vj_IvfbjUCf9-lW8D9TZAjLDvMeZIPatAUPtiIqrss4Ki88NMC31lkDpkR-YeQ5IIqOxWrFGXB2uDkO1MbVbs-9D1mbS7YpyVO4aqisG_MdSHYcVqFCNYlstuGOGASph9STpVYI3XCkoPXyG8u_e5ycfDShVJtwPykgZv5AL47q8mbysp8Mb-9lU1D5QV1R01n184ngcB5sNjWhHRCpiyEvVlQ9y9zp-LWM65dbm_7LVM55wcwQDw14R-quvf34qEnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TezynNttCasek57FnM_s6ABr9SaPXt-oqKd-MHUYxfSeF6eU07cZS3Emy-1NihL85bmcyiYxxWP-Lqgt2uyWTIqlqzCnupzj-OK3MeuUoRSL1n9CanZIstHgBaS7KgCavkX2FYFpPQVIRICwHf-ZpXaXhqL0Ze4MQmWwzK3ti-svWZwSUjqlPWZE6_a4Q_J3bgdFs7gslvUnWpIR9J7lajBOGLD2CYDXIXxJkncwc3V5f3egjLie3C0mKJiwP9miPI4VvXwVqUMdTrDQFZd-LShiv6wFAbpaJmLUCEou8GasUAeSnCk7CjTJ40vWcCQAxgbYTTEocq7sqDX_yR9aYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzEt55OJ0HCtVueZBikSGhKSPEF3WkHY3GMUA849mJHXwzc-2RiA2p0Wpb6oB9GePF50_hMDUxV6h3YsxazCdoV1-WaaLWbX6R6dOViBRmLNx-VY1OyFz6ArNRlmL1K4c7MREqdKLuxNS66ltVdPTw6KLAmvqYIkbslXU6oBiZlwyYSlXZJfCTUC_1Gzwe0LZSd3Zyuh9Tqc1JAnOancHGNYz8lPnk9o0vbw1zVUDjWRSpnsfsNVnNbLVlt-K7-Ye744hKgz5aksW5_Mce6n4qzPB21yuZjjw5e2MK8FEP8Ze6Z1OvBrW6yD-76hgZltryHYAhc7HBMBPED_fulMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZM9PfbcACpsxrhAFgD3ohiBlOwgrdvxc5jTonq2CzCWznTkiHU0P02U7rhBgXF3bcfeHpASniVf_vTbhZMxNKdTd35d8h00S_4kcKwmevoGQrfy7dg-iV778lMBZLEdMWSUo7gasqYEBr0G7OdVzkfGKTPskUD8_mGu3Qx-om82zvH1gv-hP33j15ryrTq84CkzruMnGIvTiIs7Jdk_yjzEzlqEgzn07IIFp81yd152bUPyIsnbDkvETrmlj6WXkZqM3BpYjVv6jWhRY_s_qgS-vLQMON4YEYDv-TF9_dE8df0vf0Kgr8JejJ19bSvyJZg5gud6Fau-qC66tuWk4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=kZ5OSs5djCmc5Pg0Z-LQYRPaBzyc6gYYQ4xJLb2jL-hhhhJgtKDD1CACHBws_i4bn1TLxuYtL3gmYKtWR3BHCfQQDfd7_85Yrrn6cjUtN0y_C588q7djnMITxeV4-5JAUayV3zpT11fUS7g5lvViAJ-Z20YTsec5pt8gHQTgfc1ZENPsH4wpGPSItahQM6HAHoJ7hBPLNnfyPqnwNRPzm7nXjfS3ieTBfYfTGqLYNz5bYFYsVdV__G2rm4YRT3MwO5Uo8j1GKnwEXUtoSEDjbUHhufMycEityayui7pABS6layFpqJo--CzeOqrKIvdB7OohGBP_OWIKjQt3ZUtN4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=kZ5OSs5djCmc5Pg0Z-LQYRPaBzyc6gYYQ4xJLb2jL-hhhhJgtKDD1CACHBws_i4bn1TLxuYtL3gmYKtWR3BHCfQQDfd7_85Yrrn6cjUtN0y_C588q7djnMITxeV4-5JAUayV3zpT11fUS7g5lvViAJ-Z20YTsec5pt8gHQTgfc1ZENPsH4wpGPSItahQM6HAHoJ7hBPLNnfyPqnwNRPzm7nXjfS3ieTBfYfTGqLYNz5bYFYsVdV__G2rm4YRT3MwO5Uo8j1GKnwEXUtoSEDjbUHhufMycEityayui7pABS6layFpqJo--CzeOqrKIvdB7OohGBP_OWIKjQt3ZUtN4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=f0hNAEfFwtw25kyIWp5RLCsZxQy7OWuP5OabDZsHEZKdvCGZyyS-44vM5OVTDHpjUR9LWVawbnBby520wKlOcwYJCCIQB7813tl0P8EkIvzJmRh2KPUxzwQp5UbI9KigU645apwSMQr2HjN5wnwiGYbjErsg3cbr0YKhtGXWyHvScNqIc-2GvjMQVp4K6vpezWAxbV6uLjMszbpUmX8QFD8fmslDiAVkp4OFovpp1whcGPNFuj7r81-TKd_4fWH-OsROJyfYeForSXBnzKMdveHkqw80iFcSo82NHdpwk8VUfbGt0JMMXkP2l_hnmkYTYP3v-_rh5eFpZVYE36ub-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=f0hNAEfFwtw25kyIWp5RLCsZxQy7OWuP5OabDZsHEZKdvCGZyyS-44vM5OVTDHpjUR9LWVawbnBby520wKlOcwYJCCIQB7813tl0P8EkIvzJmRh2KPUxzwQp5UbI9KigU645apwSMQr2HjN5wnwiGYbjErsg3cbr0YKhtGXWyHvScNqIc-2GvjMQVp4K6vpezWAxbV6uLjMszbpUmX8QFD8fmslDiAVkp4OFovpp1whcGPNFuj7r81-TKd_4fWH-OsROJyfYeForSXBnzKMdveHkqw80iFcSo82NHdpwk8VUfbGt0JMMXkP2l_hnmkYTYP3v-_rh5eFpZVYE36ub-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjCZeNqhtC7fM7nqbtnDGqNxHnAEL_pad4n-7_Ekrve2BhYu6NDrdDyABlS66Srkj-hUJ7FMv_EYls1kZzlcNf8uG6eOeC9UFU5QAjZPlSxYfDnAB5ByQiXHGRARVSaRdYXANqQ6eT9SS_uEOggB9Rk2CafR31IFY7vA7LX8RjKVsqF3ZZ3oRH27D8uvw94Ewg0kJSP9W0UJ7jMTVQGeGPXUT9cyGevdEWx1-8AUq1iiGZI6RVui2wPqVMZwr7QXFYWFaFobbecsT9acTs6R1TSc3FfwGc0KA3GT3P61Q9a_batsRcXL_e0ZIu1f3amdAKzo-5g9UuK7fd-tDWZcBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTwXBeuDXz2cdAa5hZEZErvLNEv-PrzLz7eDIXYjgbPEor2fwiLY3OCsFROTyhVU2Q4WtD149ewc2NrDM8Zgh8YIezJwSnpk5d33eDDTjcnhPfVOor-YoHYok_10kjK_vECRO9cMLnXMgh7x8NaWBCL4DZxcQ2z9QfYJLBi8M1eyFsFiswcCBze0JqR1kjQcKjkor5zhnFe21IpQADN_OrIu1Sy6CztulHTmAWdKUL7K7IJQ7tgKucNu42gAkfyJZtaU_mPV63PeQtIw0i0HZhSKk9zn13RKJgfz3fyKFMdnco3zsnSMpCDNlOxDVtm2CckGkPsFpAh8ZqFrpmBWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc88CiSxfMzQ3qD4ttDmH1rF44VYoQgVkdKUfjjeOGCqJO294UcwRJfm6jN47OS5CUvzGGdl4M0HXMN5e2FBqYJWE3BHF88-n8cRRldm39uW7RlcFHhyonaWWf4tIncCEOGURY_AYCrpjkcqNJbiqLK3FkWpLCUKfPhPT1gHLJgS1bng0f7-WCjVADCgikUKNJc_YX2AF--JySXswh98GPnaQRgBsPaYToLa0NEGAxvM2io4NxRmkdsNXIFMZ7jK9NIufxhSC497vIFWZUqAlwDdKAFXOUQzwHKmR2SZUI1ncf9Os9vnx-fu6qebnbFhiodEQiQ1ayudWZjgVqmZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVWV7FRnb_kpPubFGlI4o2t35vBYuInJFo1c4bBZCpC64taiaUvQL1w-FiVI0Ukbnr5VytrqHsqP7gA1NRXpNYZHoXMKs9Q1u4gmX2VX0IkNMTx1Q3S3FTA6FU47CvTnq96bLaxPUT89nzE0GV3UDW9kcLxM9cSUulbSak1P-5Aqw0d7yI3UKCiZxol4hFznUrqwVyQ-LT25_L_Ko4tLBdoq1YPIvdriwTonvCRTjiiu6vvXJ7akShOtVIAY2uEgPnMzLTz01WI_dMiwDyKH8xiB8EZgNJzCsddJScBY8mD2aNuLuONaJahqIWPI9SHwfjAsHtDl9jyYheewNbMX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUDTXTkVQF2oobum2gmvFCS3MW1HxnXpi3KV4gFE_t2WJwuSuucrXS7lduZrgqnvfcGvnu9icF8N0P7DpMxQ5gu59oIwTU1mq0vSjN14LJ60YtSMz2ZuMRoXYg0UXxzSniPEZ7JM46h0njKGix6WM61Jelu2uDoQ9TwpARWWqzFIyHdJYqXn0qsvkOeMIpm27_AdWHvGdD4pHvII53pg8ZuxUoPFyjHoiqVUfJ-8S2FuFStQ49QV2M8LOeZoIJ_3GeUsnDjmRsfayqo3RxX89dPAJqmyPLvvAT6LemqncfkWbsuzyBAr1NaOb-HfIt3I3381lXHk9uYV2N8tkaBHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKZC94fT4W6mwoD6CzPv_5D03wC2wGCzyfYEakpd17E2nWEIX9j0Mjm9c-GC561AHRbyTHpHzmdOUXJSdBShM_hNutbOpEvsmFR3rwkQzgoqCmyEwQCbNu1fzdvUGpe9wC5WEtpATPg3JSbztXBRyOeJuv2wgHP7wbTRksILD0rmlNCdxWGMIOvK-uKMPTfcEFuOxjWqJLX3HcSjwuEy0DY2XGnXz0UDV9PIHKMXr8xcqkRj4pnTvntAO5OHyOSD1y-uVAUERS7gT_0OV-MFyhAWT-Xt8hoH8EmtylutufLKDUphBl3ZVKITcXGPgEiXZlR2_sOcSA-xDz7TvVWUuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qw0Jgzt6lm6ujz8ViWxe_U4WLAIKB4FLsVHrI-7dol2oNRhbrAOAL9LRUNoLiVhK2lgWhbwC4J7pzY3nhhYw94h35t9skI4vKv5vhPqPPcKqcKyDq0yxxCI1-LcR0RbVLwCr2DchC_moe6ipHJw_HMzff16N9sQ3doh1PghLlDq99DL3leIpSbkVjguo46SkFwB3GbzfObd2ux9oN2vDo58Sco3iBF_WtLwYQdGUYE1wVgqBfnW6y8c1LjTXZCoVH9KYLnudAhZ8zSEZwWpruDmRTsEuVV6_eKRXv3A2_Bo80ozUzDRVeMNjiB-u4KNNI-Tn2Zdd9M9WTHUZPMp4_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNRjud73sdRzODat3wIRs55tl051OwjbFRoWuWhSVQzA1Lcse_RwUGn4aUNsdJFrDKnpjMnybSro5nIe6BB9_T3DyXzbrDXLlC55FhbvPuit2lMydQh7CHNSyxMrESMFlJ0KwdJFHgvcwNVnr2AjRctAVcvWWV8dc5NGDKzBiI_rOPTQ_itx8S3hdxkSXym_dE6q4PaWyVMkdqVUALyMWDyZkl2uTu4Tk0QtgEMFbOOWtFHlXkirVTG7SCEO4l5PEJCj7vHa-nUAYm1yrj_gI1AGTDMGVrnY-N3qpENq5riuXIqP9xx3iAwrFCTZJfeSny2jF1xuxf8GaAQEgQUT2A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=IP4lzo32SLwdRfv0jrrIm7axjemhoj-AH-u1VVZ_01-G8W6iXWxRRcUsxLgvUpOZ4Ec3-1ZN5toTOAzda0nkcmGucCb6YBh4z9J8gKsrtbjIQyilDbZRYzggog7eyT9BPXY0XKeau0-Gtgj_YCrgsHirD4enRBQJS0kKqsgDciEPFBSLUJmhxLQtr-6UcRebY3jrKLehzEA6AbLvM50YSIBhQC-6-LVfvDa8pfp4AyCmk-Jwpyo44iJCZflRD6mq2hwhbwE8oxtByMPEjNl98M6cK-zs-M5EH56Ry5xzNGjj5_j21toeZJVvdSZ_E-qDa4hWoXQVZ0yzUQW2fDWosg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=IP4lzo32SLwdRfv0jrrIm7axjemhoj-AH-u1VVZ_01-G8W6iXWxRRcUsxLgvUpOZ4Ec3-1ZN5toTOAzda0nkcmGucCb6YBh4z9J8gKsrtbjIQyilDbZRYzggog7eyT9BPXY0XKeau0-Gtgj_YCrgsHirD4enRBQJS0kKqsgDciEPFBSLUJmhxLQtr-6UcRebY3jrKLehzEA6AbLvM50YSIBhQC-6-LVfvDa8pfp4AyCmk-Jwpyo44iJCZflRD6mq2hwhbwE8oxtByMPEjNl98M6cK-zs-M5EH56Ry5xzNGjj5_j21toeZJVvdSZ_E-qDa4hWoXQVZ0yzUQW2fDWosg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=ZeMKAQQjnBj0UwFK-ZgiD5h95y9c1c5YUdOEY5FY0mC-5VK7IUqACytZsrREQK0SScI66HVW6GLr25uzUvnDXUeQVrj5PLGiz0BQguxsAo3cE4--lOkzr-D0JGUSf-1flHXkv0h5Iz1kylLOnxuhk0V3Gb8myVxsGhIp5i_3GMdhxnyejAqLM0gIfys76WWT-UQE1RqSfBhOy5_jlJkYj0dFOQEStbLYLlfyoEx9G1L-JgBV_YSavjdIN32Hm9ZOsiNu233ZOgC0pH0Wdad9dcCHJfwqUHC_9_ZOAUsTmBMiDlv_7S15OWqyQl7sK5s7cU-j26EjxhJCx-5a07UJhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=ZeMKAQQjnBj0UwFK-ZgiD5h95y9c1c5YUdOEY5FY0mC-5VK7IUqACytZsrREQK0SScI66HVW6GLr25uzUvnDXUeQVrj5PLGiz0BQguxsAo3cE4--lOkzr-D0JGUSf-1flHXkv0h5Iz1kylLOnxuhk0V3Gb8myVxsGhIp5i_3GMdhxnyejAqLM0gIfys76WWT-UQE1RqSfBhOy5_jlJkYj0dFOQEStbLYLlfyoEx9G1L-JgBV_YSavjdIN32Hm9ZOsiNu233ZOgC0pH0Wdad9dcCHJfwqUHC_9_ZOAUsTmBMiDlv_7S15OWqyQl7sK5s7cU-j26EjxhJCx-5a07UJhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCzaiYKGyJIMDCebZP4lySA-V_b3uu6fyMvz3QVpN_5gotokJLJchxamaSlO2rRLYqpoIpzwSlFpQq58HPMraVG2wE0o4e7oZDfB7QuizEYFtTBcvOX52-exwTY0Ts0wZXbLmRwgmnHQj-wuISy_ZmjK_q703NCx0DPAmbwyqcy4btkD85yIwzunuvNnw8G90ESsOj3kk1FYDFDhRCNcWo7HkBQ0wjkgVhvZ1tGUE2coD2ofnAHH_XlJRHj7iLxH8GPa4ntV_vwXjsxUwAiLEpWcVLHxTY0Q2_mt-NBPObCPfsuY256O1Nxe0MTZ2PLKsR01CVbEsS5DQUmNObacjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjmbTz-Wq8UaRIeUPRrmnVtIRt033IcNZQAmckjDtxsJx-76hHaYDwBK0993Ait9r12H69GG_Tdnuwfe7itcWAcVNkNlB7U41hzIQ0qUGidAU4Qdo_tc2nMFXsSt0vijhXLGlxRFwrP0LlwAnyeDmz-w7MJ_eAvDmyLYQI1NS8XJ3R3uOd9xWjGKfI8VpM47ucv5qVRJ-xGyuBG9VcWjfrRcG5OR-qzB0V4I4Yn4-XBz3QeWUu8joq9brGWyXFpIwTqvP28wF_zEUSyvLYElfLbzo6yNFZXMepuVIwnGUInVow5LaQCiW88rXAFACJcQfowhdqiFMmKwMs6tQAJqkw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=IFh1WxzvNatJW6Wbrvl2FXr_U16tv6biQERsSeQxTIfPFEsFALIZf_OsuI0xaDgBpe4fnLwCG6f7-eftV7HqmVm7fDdZnRhydBp9A5bHoXCbL1W5gGWbTren5wMjogBcMwg54KTp-UzzDFku6LMC7cqM9zvMAsJ_emEvXD9hB-RCATNVWbf3RBSPyYi351LmoOymNFXNMHB7pGB6zeURc3ZJB2LivmiVvT0z-0dgkKrUpIVKu0_9jZrmMknMOnRtOtuyDfNJoVy_szLJRo6P0gTA5g-4NfKgTesqfEB4ZgqfFtcK3jlLZOL3SdzyTp2mCeSElEPuU5NhVeURX4yhzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=IFh1WxzvNatJW6Wbrvl2FXr_U16tv6biQERsSeQxTIfPFEsFALIZf_OsuI0xaDgBpe4fnLwCG6f7-eftV7HqmVm7fDdZnRhydBp9A5bHoXCbL1W5gGWbTren5wMjogBcMwg54KTp-UzzDFku6LMC7cqM9zvMAsJ_emEvXD9hB-RCATNVWbf3RBSPyYi351LmoOymNFXNMHB7pGB6zeURc3ZJB2LivmiVvT0z-0dgkKrUpIVKu0_9jZrmMknMOnRtOtuyDfNJoVy_szLJRo6P0gTA5g-4NfKgTesqfEB4ZgqfFtcK3jlLZOL3SdzyTp2mCeSElEPuU5NhVeURX4yhzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyqH9jJvEDYhuyzNQOJhXL7E4Pmf0PGkKnbCOiXRoOOtsLPkMhcA7shpr5V6TIaGjRjCPBAGCDTI8-LftwVOhg5YK-v_liQAov9RWZ17EonAvFZcv7Q_uw64JPQ0SzkaPXqaJOEU87EGteW42Iu12DN7ZdEE6gOAnQgY23Iyg6SZ7w17S218RSpTDTjtVLUAkckHot80lEQetb8mILODSKtnxxXOp-Mwqxl8cN9FWakEN9jn8tNpZIdgZctdx0NjXaWk0LbMlCrLdi5zDqOd5DJnJ00mVN8Kv-rOyIviWspAPDO2wx221Hr3AUCx8h8G4IgeWe6wssI7Wz8T_--HTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=JjouocEtEOAdBYZ_a-MavDS-Qnwgfl8iQiFkWesQfIcB21nlVPyEXOCh8I5Tcvnlnm0tRluYa1dMC_UyRgtKEr0xp9_5HEFMnl3pgnCJ8_91BLeTm3T5zsMpnNn8MKMovJIGjfsVAL_6BDFofCETH0xH6y73sQQHnOfHpcsd9Rkb4q6j8bzpVDmqhgtq5s7lrbU_6clz4rxOez_xdj28_WY3jkOTZtiOmMNS_NkVVXdDyl362MK-GA1fkkTQnDWLrGP3op-g95_hTW5tzIYVycaSHk2l7rdqBU3Kpu6byxpkvD2L7ZP6q4mWIf1ZShyPPU52SYM_18kcGyBreqt7uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=JjouocEtEOAdBYZ_a-MavDS-Qnwgfl8iQiFkWesQfIcB21nlVPyEXOCh8I5Tcvnlnm0tRluYa1dMC_UyRgtKEr0xp9_5HEFMnl3pgnCJ8_91BLeTm3T5zsMpnNn8MKMovJIGjfsVAL_6BDFofCETH0xH6y73sQQHnOfHpcsd9Rkb4q6j8bzpVDmqhgtq5s7lrbU_6clz4rxOez_xdj28_WY3jkOTZtiOmMNS_NkVVXdDyl362MK-GA1fkkTQnDWLrGP3op-g95_hTW5tzIYVycaSHk2l7rdqBU3Kpu6byxpkvD2L7ZP6q4mWIf1ZShyPPU52SYM_18kcGyBreqt7uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=IwF0uz1q7gjLe2_UsYORCXS8A5MD8aL5tMELWrhqGTvJ5x43fMFpUAMDLAQ7dYFJkCtpdPnLusz7Wf_h46ZB4ydzo7gDF4m5RxK6WN8grvy4gK19pETlL7CI8myaz78wR0ud3fEn9TfewArplZp3U0QTBZqwwfj2OViS_mGSO7h6gPvIdJDFiyM19Shxrtihcp67Jhr5pkUMvjW-o0zoqEUZXshy8X4Fm07rcg30bSavChtJbuFkiLbS8mkFFL4vjt7IfyR_SLyQAA-GquCLQvnakK69Dk45Lcmwz7NHZ91ChofAh4_rPNeG6sDVk6fmgOebaqDF_t1EvQVo2AjCYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=IwF0uz1q7gjLe2_UsYORCXS8A5MD8aL5tMELWrhqGTvJ5x43fMFpUAMDLAQ7dYFJkCtpdPnLusz7Wf_h46ZB4ydzo7gDF4m5RxK6WN8grvy4gK19pETlL7CI8myaz78wR0ud3fEn9TfewArplZp3U0QTBZqwwfj2OViS_mGSO7h6gPvIdJDFiyM19Shxrtihcp67Jhr5pkUMvjW-o0zoqEUZXshy8X4Fm07rcg30bSavChtJbuFkiLbS8mkFFL4vjt7IfyR_SLyQAA-GquCLQvnakK69Dk45Lcmwz7NHZ91ChofAh4_rPNeG6sDVk6fmgOebaqDF_t1EvQVo2AjCYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=DO9L1UiyYd4ZKIdCxvY9_tIjupTyJYCkSscGpYH1sPTlCW3uqOUtyjapiqDP7obR9Aiu9juLPVUrojgasaLffokmRfWjvROfuF5FfG4A8cGU0cD2w1xVqE1QaIsnUdwmIE3pqiDtgbDdua9Vw77bll8zwMyI7UD8mRa0ACANOCn4FTwxRI5Lrvs646fDnFha3OEXbAxpbQIOE-OYhtik9PesAcRXk9zupz3Q6cq1odo55mRQ6cZJc_RW0jVsNc9ejJravIaii1--42xXXn3ObhWSuf7DZ5xRua4qMyIj5eZRvVQAQ51rHQqIt0n9SD6--s4PiiMkJb-c7vj-opA1Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=DO9L1UiyYd4ZKIdCxvY9_tIjupTyJYCkSscGpYH1sPTlCW3uqOUtyjapiqDP7obR9Aiu9juLPVUrojgasaLffokmRfWjvROfuF5FfG4A8cGU0cD2w1xVqE1QaIsnUdwmIE3pqiDtgbDdua9Vw77bll8zwMyI7UD8mRa0ACANOCn4FTwxRI5Lrvs646fDnFha3OEXbAxpbQIOE-OYhtik9PesAcRXk9zupz3Q6cq1odo55mRQ6cZJc_RW0jVsNc9ejJravIaii1--42xXXn3ObhWSuf7DZ5xRua4qMyIj5eZRvVQAQ51rHQqIt0n9SD6--s4PiiMkJb-c7vj-opA1Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=A2-LTYa7z1M4Mg5OQaVgA8YapVzx7CPsaTtFIvHRItR5pvHMuzlO4XgNuFfGpE4fn0OpJWF3U9pIva5JL7slQThQfKxm-rlG50nTMCPu2hSSdGiwKhoU1ojjAbCP5gaxPV__KYWRJTuNH3layHjuJmOSeOddWzsNDWAe7Kb6qN8qjJfpjOxeOO51ZY6hPbYWGWIJEu2G-zY-9q1hkEKKSKzw0Pidd_AAxIack_ef2OtbXdbERuuVug6f57ZaNzRjVuR-Ekw_dLi45M_b02y0m9HsUyLRgXGz0XbX3Z-DAucB_8DVFOF11k_LuMnYo2Yg4Z7BicqqSsvBMdYhrnHffw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=A2-LTYa7z1M4Mg5OQaVgA8YapVzx7CPsaTtFIvHRItR5pvHMuzlO4XgNuFfGpE4fn0OpJWF3U9pIva5JL7slQThQfKxm-rlG50nTMCPu2hSSdGiwKhoU1ojjAbCP5gaxPV__KYWRJTuNH3layHjuJmOSeOddWzsNDWAe7Kb6qN8qjJfpjOxeOO51ZY6hPbYWGWIJEu2G-zY-9q1hkEKKSKzw0Pidd_AAxIack_ef2OtbXdbERuuVug6f57ZaNzRjVuR-Ekw_dLi45M_b02y0m9HsUyLRgXGz0XbX3Z-DAucB_8DVFOF11k_LuMnYo2Yg4Z7BicqqSsvBMdYhrnHffw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=P5YUHH3gMnnCBWTj8mheP6amd2YNaJlNHqy47KEvX-rtoGSuI8KhYNCmEYMMX9gXDFljsTALOatU6BGSG_d6a0GG_wkXDRKqG-kRW8MwysLPOottwGnzFJf7VsBRWF_ybqno6Ey-FJygP-7-O_CY5BmP47sEtGOor-VPN5wR4oAtE6z-wigQmVrMF_2OMtgcAtoVwLGdeiQiB9K6E--j6mn6vNxC2yyhz8MzQ6qGsMy_S-YPqHl7P8bJu_69rLAvFhFrSUn62Fbo0jdqR41CqDge1RtP7husI8KBnSpSSJuyIeVbfHXaGW3eyXct2_bbnN-6dVxbn6z_dX_F9JSPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=P5YUHH3gMnnCBWTj8mheP6amd2YNaJlNHqy47KEvX-rtoGSuI8KhYNCmEYMMX9gXDFljsTALOatU6BGSG_d6a0GG_wkXDRKqG-kRW8MwysLPOottwGnzFJf7VsBRWF_ybqno6Ey-FJygP-7-O_CY5BmP47sEtGOor-VPN5wR4oAtE6z-wigQmVrMF_2OMtgcAtoVwLGdeiQiB9K6E--j6mn6vNxC2yyhz8MzQ6qGsMy_S-YPqHl7P8bJu_69rLAvFhFrSUn62Fbo0jdqR41CqDge1RtP7husI8KBnSpSSJuyIeVbfHXaGW3eyXct2_bbnN-6dVxbn6z_dX_F9JSPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=e1wZpTWC2n682z-FlioLj-0UmX6MplxQjH7Ad1-QqPxqzJcbD7fy9aRUhUVdceyz8OClHqcYzmm6I7Qz167ypnkoaGQtt7i_gxyGxnKD3gnNaWC9k1pS9lG_5A0GO5F-9hDEOB-i2RdNQrbAEov_HbVnDQxg0pkUekhI1DqXGBpMnjUL6Y2fdoeYOfG0fjiu3-ZF25DmqOWbKcM2EankcZA98gAU5_KbXN9Y7eaVqoBt9n2ZQTxjf08AJFprA5bjBuEFxIu30IQH6SU893HRHV6V60bD8-KggVAALRxiDA-7QNPPmq486aVNvFiLrcPjz6dQFI3z812WhnG5LiAxpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=e1wZpTWC2n682z-FlioLj-0UmX6MplxQjH7Ad1-QqPxqzJcbD7fy9aRUhUVdceyz8OClHqcYzmm6I7Qz167ypnkoaGQtt7i_gxyGxnKD3gnNaWC9k1pS9lG_5A0GO5F-9hDEOB-i2RdNQrbAEov_HbVnDQxg0pkUekhI1DqXGBpMnjUL6Y2fdoeYOfG0fjiu3-ZF25DmqOWbKcM2EankcZA98gAU5_KbXN9Y7eaVqoBt9n2ZQTxjf08AJFprA5bjBuEFxIu30IQH6SU893HRHV6V60bD8-KggVAALRxiDA-7QNPPmq486aVNvFiLrcPjz6dQFI3z812WhnG5LiAxpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StFL4JW9cLAzWUXkrJrHXdLBlYLBFE7h3sYI5qUeU0eygff39TYxaUneDJd0TmU0h4S8wmmj1uFO3Dh-Mff2-oq_kw9_rPP8rL2tJpwAa1_b8GrSmXY4MVZ9rlWSQ4KJD1AmKAoV-qOqsNvtzmtLA-XBsJhp-vtGr3dFFCQeL3enS4A9WjJW1y6erdvhxpV4oo7793mWgWxaPWwguOFcIoDpX8ZIT92YD-7XNxoqwmeAlv8mB2rivkFIGvhsxskaPqYKrD1aGhM8fgJTsRtYwY-2KJ_A9Lj7Pfz7rSU-YA0lvi579yGFDZaCDXAwxy1M-j3ZZbiVsg_sV4bko2qYFw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=UYqCsInf4Ap_-f7yL-r7mmO1AEDSNKi7ca49OrLTXJcckYyft2cJxmYTkLWOtT5D7lgXSbIfJnnIDjUMg4TUo3wqv4nrityOvoFc7M5_yEAb_4gE8Gi9t-7yba3LgPW8nLNSGzN5vaMBux2NAbXl8Okzp_90c4481IXhQxr5PsEPdRRcH7RGnj4IFsMIZG5HNr8fC4aHh8S5qI57S0FUjY9hzCUZsxq1uripl1wl54qPXsIG4koGFPefOfFhvfA-UPBQtX-qgWF-JM44oE4O2dL1rMrGr5dtFa9lHEGasQ8rG9DvjgDKBnRdbFPJxvfhO3Bp-nvzGPyixWYbl3eVBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=UYqCsInf4Ap_-f7yL-r7mmO1AEDSNKi7ca49OrLTXJcckYyft2cJxmYTkLWOtT5D7lgXSbIfJnnIDjUMg4TUo3wqv4nrityOvoFc7M5_yEAb_4gE8Gi9t-7yba3LgPW8nLNSGzN5vaMBux2NAbXl8Okzp_90c4481IXhQxr5PsEPdRRcH7RGnj4IFsMIZG5HNr8fC4aHh8S5qI57S0FUjY9hzCUZsxq1uripl1wl54qPXsIG4koGFPefOfFhvfA-UPBQtX-qgWF-JM44oE4O2dL1rMrGr5dtFa9lHEGasQ8rG9DvjgDKBnRdbFPJxvfhO3Bp-nvzGPyixWYbl3eVBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY3tLNxbqwQVYKgrv0PPZTeaLfxnrRczXMu4xhQRBbfPoVq4BuKvvAsyigl3YUK5LHT3k1OYwDiw0UUwB8LteiHpKhHfeMJWMjlBVQbWCAfiuX9iqUTW0gaKk4mMmxtBpOOvwypVQzVLwWofLmHNhwAk7f2BLyhGQdraBryuZ1WfN7OiJCAFfNGs8sQIqp4XRbF7fy-v2uOpQGJBIMOfgC6ml0vJYTC8PC8rxoeDips58aPCrEzKkF1ZMRX6_eeNeFHV1Dc5YRgSdeqQefjRUrtzG48QeAQkTb3a5HsWZviT75g9LqKplvJOdLwAWFlV3W1zJiRqLXjpl6WKmED2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=F3YscI2JztTT5gwxrx2su6oF_tv6U81xASJlhyI4m4KSAQHDRR6Yt_6nT5_p25Rv6PcQ7c3-ysZnfvQwSMvNZmx8NU9-TKPUsHWDLlKBJx74yZsLGiFCYOVSOi0_spDU_QLmwQDT2-i5l91T5nrap87v9KxsHGTXgmg3_B8J1KttbehlUa-Pqn_8uJTmV3jJ0lQ6pnoEQvNYk6NLOhSimK16evOwES0G97QVbtx5ptYocFlEaXcxcSYZSOOZQPbROwfPtBXQaHttsOGzaPs8y2VcMrvrgKHrgh3CRX3zESXpfINei8D1XCMN_rJkO6oVoP-9OO-4L9jDhoLQ0bAG1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=F3YscI2JztTT5gwxrx2su6oF_tv6U81xASJlhyI4m4KSAQHDRR6Yt_6nT5_p25Rv6PcQ7c3-ysZnfvQwSMvNZmx8NU9-TKPUsHWDLlKBJx74yZsLGiFCYOVSOi0_spDU_QLmwQDT2-i5l91T5nrap87v9KxsHGTXgmg3_B8J1KttbehlUa-Pqn_8uJTmV3jJ0lQ6pnoEQvNYk6NLOhSimK16evOwES0G97QVbtx5ptYocFlEaXcxcSYZSOOZQPbROwfPtBXQaHttsOGzaPs8y2VcMrvrgKHrgh3CRX3zESXpfINei8D1XCMN_rJkO6oVoP-9OO-4L9jDhoLQ0bAG1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEgaG1btKQq7zFZVXS1t6g5Zy_nGp3KYxcp0P1yWrIMeOxvj5si4LrScKId2usfF6OPMx4CQsowbKzUo0TcHpavunrtQjGRl7hOqsdr135QVsq8gkzJwottYav4pO418yUFC4HQc7raBgCKSj-qvPg0oWZL5ZWnPQhDHZ293JL2rww87TRLxAXLuoQEt2U5_f8xiX5NCWVrA-TJFqRAfI0rB6YzAHMpVGyxA7bsIZ_jp3wP94Tzwu3QrXf_kb5pqRpQW2Q1fDH4a-9fqsT3zBoe2l0nMBSBq-7SYJwuUV9D8EchQFd-NC9Gn23XsfVNVLHEVW564o5RoPwGC6fjpfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4yjdqr_WafM-SnjM10K23FjzZsBZjWfaHmf_O5hMljcvP3Vb4egAU21jMswwZnXwQJopAClsAlCBCOQbtFu_byTABk2_kB5D2FD0hcl-D3XfwapdRbDm_JKIOOY6XmcJQgqTa4gz_4tZ81LZtkdDr4cgrs6Un4CMvuIN5Q1_mRITKypOVbiUnouu91YcHZc6-RnhhJ4a4_ozDEMvXdd-tVjjQ7wugYGp4mKteLgzzNRyfl3fbtRT-jupsGyvsoMjVgP6zSwawWv_xzrerkC4Qdf-Z1XrtQtJSOuuwA9-roYjBZNmdmEy_f-0_MU-HptaP15uJi1kv5rsoJPMpDwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJXuZiDfr--srjk9V_fCCW80s2Qs-qq31WrnLh4QrJaucUAJ5XY51te9OW9OO5s8LMY9hlD09JkXIQr4OmjUbK04fiPqStZKS2buwq2mEBfbP2tm-gJU_m0iJiCddmi1OLhJzaY1IVCF896r3rgWDdTnL6HDV4afxkE5WMVRHnHHTadJU1imgZB-s4DLOCxlkB04AOjtJes22xUBQ9m_-FABMMO5BfGephiNxr0iyb1ggz3OHocfFtlNTQRiOnqLN_y8Bt7r7GaMIH_hEg5YPv0BG0rrZXpcaxeD4WHSKyXpCBLkWQJ6g_wcEyz74t6lErNAiLL1vjJffYOaQNH88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLGOTNLHKdow6ibEdaYAPtUTLnJsk0SypiwuU3WQH1VNWs2lRWJIzN_d1lCrBD5GHXu3kgfoYIfXnQEIlH2GptkwY4AtFEnDW_K2f8IJLWdgLgu6DRssTKjBgdKk93RC4eultWPp8eH04h68E67yc8nWBA2Pt_0-4k5fidlxZaVZQEAaHcPjhsCp52tYvAaaibxU9y6ijsPBwsZQzW8LOU6ZHCt2FqS0FyZClJQxUXdu6Nq2T4pHnU1q7hiSrkLZYoukNeLmoHr1-a3qUd60IU32lUSyeX1MTcDFpoz5w7kHo3ZCsh7yPMaQZxMnxGKhdwxzsYmBdN_OqtJ27qP5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYEnepDCcd5kbKGcqale5tq1PVQ15kVxHCUdXSwI2r0rxNT3VXTelT7Ow-xjfkdA3X9mIWtci39Uwa-Oyu9Enyb0lGfAIyrPpvfgmcVghPpdzW4b4nBaqV6FYWhTJcIuSHiTyX4DU1ikdaGl4__vp2_a4I0R4NKoM5boUedQdBduQhPNatyoOTtV-RFik_0VJzR06bi8tS5QMitDDVnf1UuaqnxY1OpmtQ_UQozCmQH_s9xKJTl4ekYsBXaLbrRabQjLiX2QNxC2kNOabEBb3Lblx1NWiQii7DEeMgtG4TWKVhtK7dy55-4eZoi5oXWI6DY9eoJSw8Sjl-2hw5jUKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYEQhWHUv7WGz8wo9_tDRXz_bdemI2NLwvJUme52WAryjr_IhhLiJJqum8QfBcz6xfF1DFarVSM7qoLGcTN4gzH2Bt5VF9n73FHgdv2p48b2cNCQ_gmvbYW6wL6InEigQcXB67AB4KQrFJ3Xm_EfEBkzOeYdzLxYvXrC-94DULBnqRRdhZJ3Sso-VZfShVfK9fRYZdK-kl-jXCmrRlzhMRHu3Sq2Iig0HFbBo0NQ2G5aC8fDRQNwB_770dPK1S_GURO7LjHux-ZGyZ9LjdnJdMWc_E2kyJUGq6PwRnrydJAAd68zeD72MIpY_e_G183-ffYHiy83MXOLD4lGVlXHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3XdceapxM3APAfRhvVITrx6g9j4UPG-EIeU7StEYKJIbulOJfpOzU6gRSgdf6pALVWCr3T7LN-JbXY1EBulZqnfzH1qc_D9VUsaeXLz0z7jh7GXT9iu8ggUdPzdpYITUUlzGY5PB55cQ2PpOKb-QILF7b3wwK7YV4J_K8bvukXS4nvP4lKfnsQ_8CtZ2-IJ8FsIQa9DoUSaE_csk4Y--SmdVdhb3tgq85kcVUbiMopwMyM2J_fLiCT_ph8BAP1uMPRIzqOAoumP3KYyiMBd_RS7Dzfa7RLNlXqVuLUnk8MbzYzOzjN1YWhRG_vhbT1kIL9gzraqX4TsYeHKnalyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=jD1mLQMoTOLTzDTTxe7N8s-vZnU3THaLahwjLW81h8EUmOCKOQjayCMg32lN8b3u7BEnd4c1FMDHLhfuDTli5NBsDHWMpGMAaRkCzAU6hZKiO53wlZwtypB8eGgB7k-k3jK8xc08aKly7QiAf9s9GkCH3yDUmvgQApcpooNqoD6iVh9m0uU8VuIfGSNT9imeWsr9mQR5_WJnBccRiMGTWjYl7WbFMevZSX9rvLr2t29Uwg7EcRM8DsGvMCwWYsGRYkB4SaG-aDNbi-9-vOOKqGQpz_pKDP5o5KkAr8fOlwtxvW7jXIum5nv-LfqwnuqCaO_wDXul_eGquN3_V3Vb1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=jD1mLQMoTOLTzDTTxe7N8s-vZnU3THaLahwjLW81h8EUmOCKOQjayCMg32lN8b3u7BEnd4c1FMDHLhfuDTli5NBsDHWMpGMAaRkCzAU6hZKiO53wlZwtypB8eGgB7k-k3jK8xc08aKly7QiAf9s9GkCH3yDUmvgQApcpooNqoD6iVh9m0uU8VuIfGSNT9imeWsr9mQR5_WJnBccRiMGTWjYl7WbFMevZSX9rvLr2t29Uwg7EcRM8DsGvMCwWYsGRYkB4SaG-aDNbi-9-vOOKqGQpz_pKDP5o5KkAr8fOlwtxvW7jXIum5nv-LfqwnuqCaO_wDXul_eGquN3_V3Vb1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpJkmBmoXzEM3Wgza-F0CmLGaTQmLpBNU8tYxrWW5nCJhVm-poS5IKxPLkRpxd6p_AO0ORe244SoXVYeNvwGqJr2NEl--67WseimXTEfoaNJ0kTW4VvvWBtTefLlJ73jdnLkAVYE6eQMLk8PFMS81NXjCexvo3mA8TYXgSvspGtD1oaXdXF-PorLHDxro733QdIjZAtzaC7euHgS0ZQFwBjnVsLzx7aHLJIYTUj0Janr8bNkyk7jI-SlPxZ71_B9WTZ8hY5zrcthzgIywZ2rh9jEBuwywl_g2jGca7Xctt_B8zug-ScD1abKjNjZ_DGzCzjoDPWhdQBT5SsslUTwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3qbbqEcFxE3zzZ3MKHd7V8TxorjpOuBxq9UKS-CgIsPaDCr8-FFT8b9_5cCLXVCiR06ALTOpSE6hbFcEWvbOtEFOfWfkygEGW6MiVUN3-pgHfV505g6mgOfvaYFxlW6xi4qUKtienBepFJcRw9y2OygEWdf0OvGN3AppwOqxnAYFw5nsnZYFBMJsfSFR1hMPnVwGq4vatB-OfIL7ihu0OEIZsttPxoJOVACon6Br4dLF68IwFMUh_xM1nDUVeELqqaKVMnr_MCeAVswEVoCTFdF611w5IOTlUh3LuwzA5qRFp2fzSlw1LR75p3dSUwRobBqooF7kI-Xd0EEeaFL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4fDSP5wVzfR6CuQazeWry7kfbSgO7sCu-ynRWoC0dOaadNr7q4L8FZSwCSQGMHmB1SPwhCv3dFC-hMyBsAoH0lUDroixXslDk7MtiiaWnkED2Tupo_vDjVZGOeJZpIPjCW9pfn9DHAL9_LCtI9VR64XBvxmaY-0YINZIppldiwYNhLPxL40CkcEG8YvwBl_r5thR7BBxT-E4FgE-Z67TWwXJRvPlwUfHgwrWxrfTwb9xP9_n-tm_Q5JJuQRTmlbXy_e6rZ-CR3pkQI2ep9P4P6wcQOyyiejVqt8rHuiM-Y1p_qcoLq8r1ELaoC5pnRNMbhPKVSd0JgYII7LeSqHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTchGGc7jfGjT4wd7A5xoYRJUQt5h214supyPhX2mirhH7MexvJ9cyxfmOxKaKPC6nIhV_r4VdDToSOUbsy1FLyNimhqUPPTCICnkGhWULnGFCReZqZzuis5Cty33D5dzmi8ZRoWkMcJvC5Z3s6JVzl8goPUTwNjQHFCxsQUuklP1pj6A93bYDIG5k3WkA3kJYCIQ1gdk2qwOW6_Xbm4_nH2g_yAPaKyFSTiUwRbMoJoFdH2GuoU0pIBnASZWvrstddDO0_-9NBtXVyagLBWu1clFr5BEdrUvMlNSACoGAUFm15mIHaJlRkDT_ks0_6KkCsWh6cROHxdaIQFooENZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3bsVFsTu3-HM8aJYXyDgbSdZVG_9I4SKHVA9hXaqQ_8v_6H0NFIqo713wxC8TJ9zumOWx90X930fZAQtjlKMtqnv_4tsO_NuZtFGUB7k7utGR72yi4BbE6d9gsxXbASNAFj15JOEDYgF59YDKtGmM3IikMu96ZoLG7PnGTwjrVwBOKVaDxBc7hsJIF7dDmWlW7D-RRCxk2JhWg3RKxBahuwUh9iGT4FNXhYSUYAMio0BR69DSws99F2QTGkTaJK7wjl6AtU4sm9v5_0_3ANZ_NthDvJ2WjL43osyXjG9lKSj5EPVTOAB_Yrp_nejjm6hT96jpXXqsFejgy_h2AI2w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=B9naNl5eDaPZtcFyYCsQ8iEfKK1VPFXKcmFdB2QEKBjlQOlYVuKxqn--rArA9-otdmT26s2NwhNP9uV2N3qUTcMgGprd_0p-EXYz_ZEKVwXdRxti4BpHU9OT6VqtKpinJTG1VZcZt4M_G15OsUDPozzOb0i4Fd6mKg8JN_8Va6z8LyI9SZ0-7fluOzsFtlo0cd16HtGmAtVf6kH7Il7JGS_r4Vok4VcD4pE4y1_jwUaBAy1-Q2oK5eXd2TRN2eggp0FdSY3GRcP3k2c2FGqJc4SfblfZTtAkMBtvSZRlR3CqtW-zz8bZORqqomA-qUpiTTCkIsVjx4BOHiTYF-nbeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=B9naNl5eDaPZtcFyYCsQ8iEfKK1VPFXKcmFdB2QEKBjlQOlYVuKxqn--rArA9-otdmT26s2NwhNP9uV2N3qUTcMgGprd_0p-EXYz_ZEKVwXdRxti4BpHU9OT6VqtKpinJTG1VZcZt4M_G15OsUDPozzOb0i4Fd6mKg8JN_8Va6z8LyI9SZ0-7fluOzsFtlo0cd16HtGmAtVf6kH7Il7JGS_r4Vok4VcD4pE4y1_jwUaBAy1-Q2oK5eXd2TRN2eggp0FdSY3GRcP3k2c2FGqJc4SfblfZTtAkMBtvSZRlR3CqtW-zz8bZORqqomA-qUpiTTCkIsVjx4BOHiTYF-nbeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nf1wPBzcXAOS9CXx-5SxhcepVI-jhf0rqTXdHP4eHhaEXDCgtnkTND_LjUw4wHKZRlmWOnf3JWWTH69bAoBnyO10Oi1mKZRC07dqiuhFBRpVxTRTuzBA9bSGBb-amn8rKcBtK1bViVqxk_6uUTs-7xQl_BxWFMOYJw3HUIbCptKQX59gQgMjMuDJb3V1CEs77aA--Yqu26THhuls0VjZJNJb58oRlZPLXBu7GuFn2-wWHeN4hmhbi-jLRZGSeYaD01oM-pg5YfKqQD39i4TvTf-esbF2arEAMYfNsnStqF8RYexZuNumdIfvuEKxV6wur3ebvkDWc383GihCEz131w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=SwMvqLwqOHJrhjr-I4Cbto9b6DBhkte_Lw6A6drKPLOEbzwM_HaWXux1VF0R9fd3fl5mwMYPFVggK6oPmuqXrYX7vbAcfueGPR719MuYZTkRHOxwg9cBnIGGsRzvLoZdNPQkHHygwzF4-NuKTVcebHk-giJjZMoTQT6_ZhapXtQQ1TaQ2m0b-gOJ9OX0ke3M3PnRPRliQNEsm3pSimvhsqsDU7yeYca3XblNRJdDzcTGeuh4PWPBWCSBxTX8nLcFL3cd2Ogxfq21TbWMeCNrX8fNqQdW3eHqBBlaKvkExHzSVuS_Uknm4J5BmtN4MkWpV1fWEzYdPyEWdLyiQdVRvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=SwMvqLwqOHJrhjr-I4Cbto9b6DBhkte_Lw6A6drKPLOEbzwM_HaWXux1VF0R9fd3fl5mwMYPFVggK6oPmuqXrYX7vbAcfueGPR719MuYZTkRHOxwg9cBnIGGsRzvLoZdNPQkHHygwzF4-NuKTVcebHk-giJjZMoTQT6_ZhapXtQQ1TaQ2m0b-gOJ9OX0ke3M3PnRPRliQNEsm3pSimvhsqsDU7yeYca3XblNRJdDzcTGeuh4PWPBWCSBxTX8nLcFL3cd2Ogxfq21TbWMeCNrX8fNqQdW3eHqBBlaKvkExHzSVuS_Uknm4J5BmtN4MkWpV1fWEzYdPyEWdLyiQdVRvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=lnp4Pfo1T3ZYcyYD63y7B0koi90xp6eMZLznwcKk5o0CZ6aZ8fhl5W-nCVPOAeI7wU6E6HLASL844WBky9joQA0uVLkaJubZ0rAjHB4vdpr1FrxoNpswLeJOFRG-ocKWhXWLjLlINP60dZIkAUaRYwNXrU46f1eWazJX9YJz7v41JBU7_bM5nZt8Q94RMa3dtGAJLVCXplsnxpL9GINRb5MxNJHYLku65dMdObZwCYGtyyKHRTj212IXe42c-Naunet4oa3KZrIz4r3bp6ahOp5J51MEc-3Bo9WMCsKhuoOAVbUt6yfpLUXuGcxXmAb0qvFMPsanzafKlxN0t9cQaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=lnp4Pfo1T3ZYcyYD63y7B0koi90xp6eMZLznwcKk5o0CZ6aZ8fhl5W-nCVPOAeI7wU6E6HLASL844WBky9joQA0uVLkaJubZ0rAjHB4vdpr1FrxoNpswLeJOFRG-ocKWhXWLjLlINP60dZIkAUaRYwNXrU46f1eWazJX9YJz7v41JBU7_bM5nZt8Q94RMa3dtGAJLVCXplsnxpL9GINRb5MxNJHYLku65dMdObZwCYGtyyKHRTj212IXe42c-Naunet4oa3KZrIz4r3bp6ahOp5J51MEc-3Bo9WMCsKhuoOAVbUt6yfpLUXuGcxXmAb0qvFMPsanzafKlxN0t9cQaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
