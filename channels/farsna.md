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
<img src="https://cdn4.telesco.pe/file/B1KCVflu8tBdr83uBTCaRRnKuQp1fHd7l2Mmv1Cwzvpw-y_1_vmj2zk6dU1Cp7EMmZxPpPi6Yr7EFnvXKNcT2PQWroMs5eOZC7JITSKmsKJDcl-ju3Ad5jrE1IW8yaE0frb1zucUyyPV4rpnnBmlPswMrphc8P0aAmAfo2ouDYHDRuSGLz3Xt-7a2teE-6H2IgfZB_MQ6_LxLhRnwkNMXHGPav61IIprmTSpQE1fnFJG3fh3v1ifsjz9Ymd2jwPJAR-Yt4RGmomcouLnoh6HUENrqW6y9B9r3VX5Td9YLK8-a7j9NDdccxHa0j6tk_SE7LTFS6C1wWTBGtkIvkRfhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-461378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6hFT8vzHFd3Fbmr149VPCzHN0rjCkSL5_f405S_SNVHzgyeNVsLrwDWX0jG-vYwaRJcIwj_bhF0Rv2yNzDULCRYNDQzwBKfssQDY2kCgYFu5nPn1NpNH3AOyYUjKstA8671Jsfp09SihSH1dsZa-btFFUcmV2Wt_XyHgwhi8lU8Qiyo_vEtdRdRUIYGrBCyYRuSaS50tFORCPUCEgrrZDrL5ouO2b_BntnoOGElnGzM8wo9RYqtk68YhfWscMjQlIRTnHyrWGdewndtz1NV16viik8sVx5xixVhP3OuFUB0fizXfJ25Aic4Lf5GsPnd0Lobtjd1xScmdQduR2L_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد جزایر آزادشده توسط انصارالله به ۴ رسید
🔹
نیروهای یمنی امروز با آزادسازی جزیرۀ میون از دست مزدوران سعودی و تثبیت تسلط بر جزایر زقر و حنیش بزرگ و کوچک به عملیات‌های خود ادامه دادند.
🔹
با تسلط نیروهای یمنی بر این جزایر در تنگۀ باب‌المندب، کنترل انصارالله بر این آبراه استراتژیک جهان که ۱۰ درصد انرژی جهان از آن عبور می‌کند تکمیل شد.
@Farsna</div>
<div class="tg-footer">👁️ 202 · <a href="https://t.me/farsna/461378" target="_blank">📅 15:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFZkqhFHFcA_PmG8jZmz29vZWBnPDHu6KqJa6JtLuZFP8fjsx8DpVE_z-rG_ecFE4cIwFNO-KNRZBT9HaKCDrHuLAbSTNlTvDhdQgwQlMOVf_2HcPuIzS_1N8qcxjfVM6VoFMZKcoKGVJ6lOICgVI-o9li0I58lhSzoJ2SybptU8Vu44vkKgjzk-RcqAsFfNyB8SX6alN8u39_lCvQPv2s50mKmhDDi5TiZvP1VfCG69N0powirvVDOeGdd6GFqzNJQ52AaN0KtINZPcyNb72bUvaEV_P-Yel9qs6v75VhOMITYn-gDa0ovAhtvXArcwNcHcpkADagbrVPOMHkHclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده‌باش در ۱۸ استان برای سیلاب و رگبار از شنبه
🔹
سامانۀ بارشی با احتنمال ایجاد سیلاب و رگبار شدید، از فردا در آذربایجان‌غربی، آذربایجان‌شرقی، اردبیل، کردستان، گیلان، مازندران، گلستان، زنجان، قزوین، البرز و تهران فعال می‌شود.
🔹
شمال استان‌های همدان و مرکزی، جنوب کرمان، شرق و شمال هرمزگان و ارتفاعات سمنان نیز در محدودۀ تأثیر این سامانه قرار می‌گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/farsna/461377" target="_blank">📅 14:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzniFJ028LPT0cn_r-Yt5vuQs7BDSOn5pmtWN5NLYyv7auxPitHjnN6tLDDwyerFtZWMSZp7TqZ3fl4qL-qmGUOSYf0tMKa0Y8OHGada7R-1O4FiTzKIjkdulI2BS-9ZZo8m0u0_2ruzPGCEFZsobao5ocgYMcbj8AMfnYj-gCUq6jAJdUrbIkZrino0MHXOPxHxg7_CCeQnjnlgFEhrY6Fj9MbpnXehW47WV_VtLu4JJ-AFca5uHqywjLUWPw_pYlIZ2NlRGg16AzsSJZLi8yYRWOMqd4d2ysfdO5U2fcMYuhEyrE9V1MR4o9ahVfYIWpavm9Gh1TeZ9tQhzNpKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: فتح مبین انصارالله ثابت کرد امنیت خریدنی نیست
🔹
آمریکا و متحدانش در استراتژی و تاکتیک به بن‌بست رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/461376" target="_blank">📅 14:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF-nNXccDhF4atI46esdbAfJ3pxhOw4x0hJMYUiJDn0-mYwkww28rybmYuDD6B5zNxLxvwjsggsssizTtMTERFWR433kUc7ey5NKtZWrchgWj9HqWyRXUTI7n6Ab_5NsYo8IVcPOldDV7J-nWPJG6GRR4sVILm1OyulCNyTvpGUQf9V_xyO5LSXs6IltdUxcHUyHrw-npwGNDljmDy_x570PaTwyNlanMwNFAzfS6gArWL1xWIdql9eWs27H6WwEMHmtASdDjOsRxrPSsqobLMK-TQl_jQR_Dzvgt0n34mQn-BsGm9dr-XF9NMQQ9AOuglwMW12tqxeS8jqXABCpFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم حملات رژیم اشغالگر به جنوب لبنان
🔹
گزارش خبرنگار المیادین در جنوب لبنان: آمار تجاوزات اسرائیل تا این لحظه شامل یک مورد انفجار در شهرک برعشیت و ۷ مورد انفجار در شهرک المنصوری بوده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/461375" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBhIMQfkrf_53IgrFSCSOs5D3IEdP9DonY0bcGCoHm3Lno8ys9gS0ZSEp0yJWed8Oin7TJh2PBdPDJV4h613l-2EzDqCmBNqoc_PjVtWbnEu5uc29SVCy5xHf_HFXmKb8Rmsy3LtWIHknEIhFeiGEvGliFx6PT7fgtuR3k7Xc0cKH1tsdthWVKnGlUSHRVFyJryIumu4l8dlqp6nAmmuHehv_-T7JQiNyCLKEB1v3pHTE2on0bESeIRu3Z6Jz8U9fU3Bflk-9GYsv0KxgateaVUdUJP5Kgx50udxvjuaeYGJuSU1Xrd-RzqDTQYF8mLx68cQNbkvg5kJQIE1vPFfnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ ماهی‌گیر ایرانی بازداشتی در امارات به میهن بازگشتند
🔹
سرکنسولگری ایران در دوبی از آزاد شدن ۱۰ ماهگیر ایرانی بازداشتی در امارات و بازگشت آن‌ها به کشور خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/461374" target="_blank">📅 13:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwUchaYL9t1ERVpTqTwDgP2B1flJo_pUmgDT4Rn__VghJtsr8TvtLSafL0methmDxnqnz7aKQ8RzyiXrvqEcbqNMfc0jD3zwsGqj6oNhALyxQov4f33puKjs67vNkhLbedqIZWUqykiNO9pxGq4AEy5k5fGldACDBz59VwTptw51pfxoLfQgSxIAUcZDT13PhkvnGYvmapWI927nPD_ErhvZOAhVbKWC_h7hujf3z9MlF3Px2WffE6KJqu9qP4adXeum3GWaTeF_WN47VTPAzC-UWxmhoXGSBX2cTDvlIMBe0Dk6aljQwegGQoC4wb_x4bGwqxO2QccL3Ls0gLi3ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عضو ارشد انصارالله یمن: هرگونه حملۀ عربستان به زیرساخت شهرهای یمنی آزادشده، با پاسخ متقابل مواجه خواهد شد
🔸
نیروی هوایی عربستان در ساعات گذشته به فرودگاه بندر المخا، شهری که روز گذشته به دست نیروهای یمنی آزاد شد حمله کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/461373" target="_blank">📅 13:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlQ-5cwx7p81jSgGAqHVEd3VMxlpa-SFq1-wsNjIVElbmI55DD1MGBtH3YIpFMXhII9OQn53pC9ECA-XbFXdyrdDauTfotdVeeywpTqzTbcK3ekI3kY-ejl2-uG65oV5KwhNgEn8gorbOtB-ECgN7e4lXRzgzVlQf4TvdFwrMut0DmjOSQpvrdz_ZHThGETa6ppZDClVdLgBLsK7JXjwOo0i4_zyhSofDLQDo65t_Nic9FGJ-P_ydYtE-NKPU7tjY0DpoO27vX0v-BqXnm_BKjBB_RlI_8lNxcrJMlIFJ36tCWwEKqva7B9BzW0k7gG3qzbeHdBGOjwNd0_iPlQUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: از پیروزی‌‎های ملت یمن خرسندیم
🔹
پیام ما همچون گذشته به حکام منطقه دعوت به عقلانیت، رهایی از وابستگی و وحدت حول پرچم اسلام است.
🔹
تشکیل بلوک مقتدر اقتصادی و سیاسی اسلامی با رعایت شئون همسایگی و انسجام منطقه‌ای، ضامن منافع امت اسلامی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/461372" target="_blank">📅 13:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRBmMi__sqtPHX3Ivzjpzi6BCg_hYAmMM8OgiXa_eVNw2EFR7_KFj1TLiVKsWDVIjlynKuk-sRhh5TlIXnx36uPSJwq4XYG2ApokfOp2GfqfiYApGOz9GVdrNsdx8Q_w5B6FaEzjC3N49Z1U4Wrez6RbuGL9TbGcMkq21CNk1m59s_Gr8vZlEtWhxDTF0yHQY7KUl-LcX3HmH64G-Y8A44Kki9ydZFk8_qfn9b9Hxa_PuIeNMHDiCpL2Wo-jGlgx7pxHo_c3ezCarKbOM8My71fEGfL-8ZHEKF58h5V82MZLQ5jf_C3IIKw85Ak-rEGGivT9EGKZJKI5rBXSLQpNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزائر با امارات قطع رابطه کرد
🔹
دولت الجزائر با اعلام تصمیم قطع روابط دیپلماتیک با امارات متحده عربی، ۴۸ ساعت به سفیر ابوظبی مهلت داد تا خاک این کشور را ترک کند.
🔹
رسانه‌های الجزائری میگویند تصمیم قطع روابط به علت رفتارهای تحریک‌آمیز یا خصمانۀ امارات اتخاذ شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/461371" target="_blank">📅 13:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TM71ST6OaY4ArLKVGRQPqOsYY8w_rUYO-YMtS-HXSkYe9eMDYoKJvfiOSGzeinCV4mk3vtL37i91gart7vzNcnKuIijN0gBiw5HQosqprR30JU3TC2BLxZAHpCny8PbQf-XjLy-5oF2QuWHDiHgVwkyKpYg21DJnq0TDqtBI2-E_PVDD8tdAnWE4kvemcS4xuDwgEU4duPDJy1xPL4GrPgs8XFkpvrVEac0du9IIR22JcUkaHWislQJz73P-cft9d2D4ynbh3tB_eGb3_iMIKDIT_rrf2i3ytRG2El6lMV6W5EL9g4uXj-AeRAhZ5ty_iSgEqPb0lIp3mzr4v2qmEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فوتی و ۱۰ مصدوم در حادثۀ برخورد خودرو با تجمع‌کنندگان در مشهد
🔹
ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد مشهد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و بیش از ۱۰ نفر زخمی شدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461370" target="_blank">📅 13:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91036a20b4.mp4?token=XskxT_h-rnNYCrOYw4wxPJMB5bh2RjyeFxzDcvguJatnvC3xhbMmP_TYnuewIEOl1TQ59zFZg5XTkDyDSLwGiZcXHBHeso4iL8acxZdkK0a-vJiB1pQLIavHi7K4ZliO5VVlCwyFydmcf_InwL7KQG1AbOoS-_IoewxCQijptrnEesvMbG714kWkVMEJ_wD0OPtKLSt8-ZWZe5bOamGbslcKcyUaz31wObdoP4u1_LydtqHOjMPnhQ7-KUOZiT0b4dfcVxrWPoFlK6kaicRMRGO5kd9zyyzaaXef3g4T3ea5FllQG-MYw0GlSwYqccX9fRMDCT1CYLX_Su54tJL7nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91036a20b4.mp4?token=XskxT_h-rnNYCrOYw4wxPJMB5bh2RjyeFxzDcvguJatnvC3xhbMmP_TYnuewIEOl1TQ59zFZg5XTkDyDSLwGiZcXHBHeso4iL8acxZdkK0a-vJiB1pQLIavHi7K4ZliO5VVlCwyFydmcf_InwL7KQG1AbOoS-_IoewxCQijptrnEesvMbG714kWkVMEJ_wD0OPtKLSt8-ZWZe5bOamGbslcKcyUaz31wObdoP4u1_LydtqHOjMPnhQ7-KUOZiT0b4dfcVxrWPoFlK6kaicRMRGO5kd9zyyzaaXef3g4T3ea5FllQG-MYw0GlSwYqccX9fRMDCT1CYLX_Su54tJL7nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: تاج بازی بدون تماشاگر در لیگ را ممنوع کرده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461369" target="_blank">📅 12:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9aQsQMvhaBRVGi5i1fiURpHiSsT05wnPVa5PHw4i_JaVqPg8rDz8KsdqfbfYJVaPd_T7NYArsMGhAZpcA9JSgMBi0zqjpa0SIkU-FNc7zisHT6gPTDvU3mCJhiRalNoC40ckiYDD98N-PM9BzLdtk61MymHQu6q5BrsaXlydp_8EMtKWRIiCvwI3fFDIrQiHlASxpX7SvCxErguJNMildcG7gMb5W5hVC46QPjDe6AcVMHjtNMnQeDoHxV4ppW42HOx_OSe5cm0buAeK-N4E5PNyAhu12QeHWzWx8AR3TOqXwI4JG9ZAhZNJb7nwaxOEKgAr-4QlPgkNFbfHBAASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه،‌ لیتوانی را به حمله اتمی تهدید کرد
🔹
پسکوف، سخنگوی دولت روسیه: در صورت استقرار تسلیحات اتمی در لیتوانی، خاک این کشور هدف مشروع ودر تیررس سلاح‌های هسته‌ای ما خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461368" target="_blank">📅 11:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c41b04fc9.mp4?token=XMtgqsaLJDrWGadcVadBwSoZxsNJETxMQCGHCBRQfbDjG7vz1QwQPkY0yjouub0Ox62h2fblDA311LUq4zwomKAAJ8esHZsm6d_akT5_8eqVCh-lcn7UBGFYEfXp2VLUxadfXBdUuNeFRne-RVA9kurfuV2Sthoshq_OAqsQEDQnhi4csOqdC21B9JYLsneRXMsI3AGckI2YKV4QMkSB8OsOGVkrNgM2RXqzt8acpV8kGIYPuF4NcoRRwARBHLiARDBMnXuf8g74RQdswgXCoI2v7BJLptoIKHBuNiHRg-6xVgFmm6526lNFRyuAuqLIGH4SIhj60C-amVX28_Z_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c41b04fc9.mp4?token=XMtgqsaLJDrWGadcVadBwSoZxsNJETxMQCGHCBRQfbDjG7vz1QwQPkY0yjouub0Ox62h2fblDA311LUq4zwomKAAJ8esHZsm6d_akT5_8eqVCh-lcn7UBGFYEfXp2VLUxadfXBdUuNeFRne-RVA9kurfuV2Sthoshq_OAqsQEDQnhi4csOqdC21B9JYLsneRXMsI3AGckI2YKV4QMkSB8OsOGVkrNgM2RXqzt8acpV8kGIYPuF4NcoRRwARBHLiARDBMnXuf8g74RQdswgXCoI2v7BJLptoIKHBuNiHRg-6xVgFmm6526lNFRyuAuqLIGH4SIhj60C-amVX28_Z_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصبانیت ترامپ از گزارش وال استریت ژورنال درباره ایران
🔹
گزارش نشریه آمریکایی درباره احتمال ادامه یافتن جنگ آمریکا علیه ایران تا پایان دوره ریاست جمهوری  ترامپ، با واکنش تند او همراه شد.
🔹
ترامپ در پاسخ به سوال خبرنگاران در فرودگاه دالاس مدعی شد که «اصلا احتمال چنین چیزی وجود ندارد».
🔹
وی افزود‌ «آنها یکی از نادرست‌ترین نشریه‌هایی هستند که تا به حال خوانده‌ام».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461367" target="_blank">📅 11:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVmzQfbkXausWy3kQctH0kCvCgu2A2E6OhTjMO73WspskdEOGjTkAJhY8o6Llg1GyY3POkiX9ILIMgCsAu27Z0WsK9CnqwcI67zLQdQUL4hCKdVfd83ocwnUB_QYxiPK27V17O7q1d3EbQ-7e4rw5wo0TNNmkzhT9eiFT9kzac2APnlFjglRr2nuIcsHPCIilPxYnZ3N9WGmlwV0MSfjZIO6osmZ5RxBz7SL4FiY5IKCRY7kk0560f4Ja0yfmQSFfMSnT1UEmqIUAiUhVm8L10oBQx5g3SHkpOh7e2mM9Gc0AZXqiTGZJd3a62UNkTaVjmoXUu_hTaVtqBMdMeECRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت گران شد، عاصم منیر دست به کار شد!
🔹
با افزایش قیمت جهانی نفت و همچنین گران‌ترشدن قیمت بنزین و گازوئیل در ایالات‌متحده، واسطه‌های ترامپ برای کاهش تنش‌ها با ایران دوباره وارد میدان شدند.
🔹
رویترز گزارش داده که عاصم منیر، فرماندۀ ارتش پاکستان به‌منظور تلاش برای کاهش تنش‌ها با عراقچی رایزنی کرده است.
🔹
رویترز گفته در این گفت‌وگو دربارۀ امکان بازگشت به مذاکرات و تحولات مرتبط با حملات انصارالله یمن به عربستان سعودی صحبت شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461366" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHh-8nF2NLDazqwt20e7A_YGZPA8ZjJ73kvhxjQ_KTTEd4v7rUpuLpDYUi3adoPNASN9r99jHQSZ_BFugV5LqCIFH4-kkzNnktBXxSFo3VhPIzyZ2-ZyC6dXhKT-xYbep-tmRO40qdRzxPUlMvwkwC5Fv0Zp9NQq1xmE1gGUF3zOS8tjH295W11awoMcyKPGiQBAufv3qDHuqBmib8KK66huYgH6Bd6bQDCrIlO-G1Xst-IsRmqk2NOnF0WGemkvLl3R5bcd2TOrlIVcSI8Gb9yLDtZEOrg8BnN9EwTv3Cr-l24fUSSCfdrQyuQ7tzbB57od9Jg8g0NpFf4ZVqW8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک نوین بریکس</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461365" target="_blank">📅 11:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PBvo2qEkHW8kJeu-bb7Ht8Qr9LtCSCihK0yrcyuzmzsljB1B-pbjYkxnAH8LRq8hLRR_0pKLt5qwdWh2noWUM70HVcpTbX9aNB_2lKR1xMxZbVBvUZNZ34fyrTu3-QYaQT2dBa3GqTjFh35JY9dK6uSJfsHiyzIirHvu_O4U6fdMTMIYDqhrCtWaF92cd6EaMqYxEjYmvigqmCTf-czkcdtWbaUpeTmFa-j0ns_sJqo0rwKJXLH-V9V4dNxaz629XEtINQv0MZ8Mp77uMM1VEH_nqPp1OhnvXK2GGclf5KYSxtfiHjOhLOQcTwBdWDPGxwxib0YJeOaMWjZtSMmkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای نخستین بار در معدن‌کاری ایران
چادرملو به عمق 300 متر می‌رود
🔹
مدیرعامل شرکت معدنی و صنعتی چادرملو با تشریح برنامه‌های این شرکت برای تأمین پایدار خوراک، از ارزیابی فنی و اقتصادی ذخایر T1 و T2 در عمق بیش از ۳۰۰ متر خبر داد و گفت: چادرملو در نیمه دوم سال ۱۴۰۵ برای انعقاد قرارداد و آغاز عملیات استخراج زیرزمینی این ذخایر اقدام خواهد کرد.
🔹
به گزارش روابط عمومی چادرملو، فرید دهقانی، سخنران اصلی کنفرانس استیل پرایس، با تشریح وضعیت تأمین خوراک این شرکت اظهار داشت: در سال‌های گذشته با دقت بسیار بالا نسبت به اکتشاف ذخایر جدید در عمق اقدام کردیم. راه‌اندازی معادن جدید در D19 و آنومالی ۱۰ هم در جبهه شمالی و جنوبی، و اکتشافات بسیار جدی در معادن A21 و A19 حال انجام است.
🔹
دهقانی ادامه داد: یکی از مهم‌ترین اقدامات چادرملو در دو سال گذشته، ارزیابی کامل و فنی و اقتصادی ذخایر T1 و T2 در عمق بالای ۳۰۰ متر بوده است و فعلاً از این عمق شروع می‌کنیم.
🔹
مدیرعامل چادرملو تصریح کرد: برای استخراج زیرزمینی این ذخایر، اقدامات لازم صورت گرفته و قرار است در نیمه دوم سال ۱۴۰۵ برای انعقاد قرارداد و شروع عملیات استخراج اقدام کنیم.
🔹
وی تصریح کرد: این عملیات با مشارکت شرکت‌های داخلی و شرکت‌های خارجی انجام می‌شود و کل مطالعات پایه‌ای را انجام می‌دهند.
🔹
دهقانی با تأکید بر اهمیت اکتشاف برای تداوم فعالیت‌های معدنی چادرملو اظهار داشت: همه ما واقفیم که اکتشاف چادرملو یک ضرورت راهبردی برای بقا است. به همین خاطر در ۱۶ محدوده در یک‌ منطقه و ۴ محدوده در منطقه دیگر نسبت به اکتشاف اقدام کرده‌ایم و در معدن زمان‎آباد به یک جمع‌بندی خوب رسیده‌ایم.
🔹
مدیرعامل شرکت معدنی و صنعتی چادرملو ابراز امیدواری کرد که در سال‌های ۱۴۰۵ و ۱۴۰۶، توسعه بالادستی بخش معدن چادرملو به‌عنوان یک راهبرد اصلی مورد نیاز و ضرورت اصلی، برای بقای تولید و سودآوری این شرکت محقق شود.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461364" target="_blank">📅 11:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxnhESTIA77vRiDGpSrdVJfe-UIIlD4N7W7pkgiVmynMGceiy3XLh1SAXlBdPUXYjhGzxlJFVfXHkZV22fLtXzA20yWzWpAJdiOzzl17IB3Z2jG0tlmZKQ8Y4OuILXc68aDBof_ciwlTs2Xn-9y5t7lbir9reERWStLIaw4E00yLDaRj1ilZeL54Ahf0cBvHJgeRi5TJHXfJvYq7LT3rUJyybBQe-Dgq3SeKXgdJW64fVxqbZu29VlCu9Tnn8_qg5LC0uWWBgJQB_VE80eQUCy_CFcijz7vRFu7XJw5akYcGqkUGqTbhTxahlmmXRdGqmFmNv_51Rn-7CK4Y7-YIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
شتاب‌دهی به تامین مالی واحدهای تولیدی با ابزارهای نوین بانکی
🔹️
مدیرعامل بانک رفاه کارگران گفت: طراحی و بهره‌برداری از ابزارهای نوین بانکی مانند اوراق گواهی سپرده خاص، کارت رفاهی متصل به اوراق گام، فکتورینگ و برات الکترونیک، حاصل تلاش و همراهی تمامی ارکان بانک رفاه است. این ابزارها، تامین مالی واحدهای تولیدی را تسهیل و تسریع می‌کند.
🔹️
دکتر اسماعیل للـه‌گانی با بیان این مطلب در اولین نشست سراسری مدیران صف و ستاد بانک رفاه در سال 1405 تأکید کرد: توسعه این ابزارها و استمرار رویکرد نوآورانه، می‌تواند ضمن تنوع‌بخشی به خدمات بانک، ظرفیت‌های جدیدی برای ایفای نقش مؤثرتر در تأمین مالی بخش‌های مختلف اقتصاد ایجاد کند.
🔹️
وی بر تداوم مسیر توسعه و نوآوری بانک رفاه کارگران تأکید کرد و گفت: آنچه امروز در این بانک به دست آمده، حاصل تلاش جمعی تمامی ارکان و کارکنان بانک است و استمرار این مسیر نیازمند هم‌افزایی، هدف‌گذاری جدید و تبدیل ظرفیت‌های موجود به مزیت‌های پایدار با هدف ارائه خدمات مناسب به مشتریان است.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/461363" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/461362" target="_blank">📅 11:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461360">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR3Cw32S_a3Cvwb2v19OHtIyJem4q083cuOc52osdRD54UBze7VY1ArqjO0eWKYSJWUpWvVo8oam--aSCf6Ulblwpxs7SaT78elsjGX_Pkc2NEmr8dzkSbPNy5Fii01eXOdTrJgq8-tmn_FgX-LGy6cBnVz5HXZZoE6fYBahBIH7xDod8hdCJ55rhgmUoviy5OWhLld8d4tkfR0UN8cKwX8QceR-hyeR9I2ZuKxp79wAC4plykD0is2rUfNnw8cs5f_y9mSevWDIK9-ReqnyUiuTiv_P5GeEdAiXdAQpj7cYETgsS8RzeHkiTZ4PiWv-OxKCZ341m1cTrgQ73wKBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست رد ترامپ به خواهش بن‌سلمان دربارۀ یمن
🔹
رسانه‌های آمریکایی می‌گویند که ولی‌عهد سعودی پس‌از حملات شدید یمن، ۲ مرتبه از ترامپ درخواست کرده تا آمریکا به این جنگ ورود کند و به یمن حمله کند اما با پاسخ منفی مواجه شده است.
🔹
آکسیوس دراین‌باره گفته مقامات آمریکا به همتایان سعودی گفته‌اند که ترامپ دستور داده نیروهای آمریکایی بر ایران و تنگه هرمز متمرکز بمانند و از گشودن جبهه دیگری خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461360" target="_blank">📅 10:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461353">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0dfIGQsxKJnHM4yT-2osgFr_ELXoIAG7utLlxMP5sVttAhQInZmuFv0TMH8L-ufmTa7is8alUFh93D75hPjEXDleZq_f_Mn78GvUUiysrvs5xUqA_UIjPa2b4WSDJBDB31CeMuy8yOEnmwKTj8Z9Udp4ooONvUduhPkaBL_EsyKPGQLSzfh2S5lRmRsL8b-kCMXftUj8nWumDf43zFiHC73Vlo6oF8mHDVe0gVM3yoTj4-I5GxLGReSA7TDFYAf7bTcUimQTC1TXrJ9966m3Y49Eu6vSBnRIo01rZHeEw0AnS-StUA-bzidt7f8WO7SjcaxtASwdqRvJ6DinUPZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMDcirRbR4vbIBnjj2Yd-jePoGrbEvdXxeVZ36tXXxXAZVxwvhOSym0UW05FxGxn-ssNl-Sh51IzfV5Che8l69ne6azrCFceQDBMzSt7yCTwnycwZCNISsmOZ_FHEytGMxDTxtpzlots9IrkhXgO4C6oBTz6EWIegGLaUHk8HsE58cIqpYl5zK3eFY5aG6DfcKloX7ylRGIJxzIEddVObcmSYfcy1rfxosZ2CtGJWW3pvUrj0SEnzO3MwXo_YB1tO-bSb1B1Pz-KHVMfqf0ZDudeeL5xO514LX1eFDyyGIPg4fsYuTyofQBW1BGqHPWFv2GrVoBL--z5qxw-6tSpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjtHi9BgpshkowcVqyze8SJXdfqmfEg6-M2AniW3EseekbOnQD45RgPrcXLVBLy7uGtZcHnEGpCHcj0VU5tgznkkzUmajZB7yjmrENzBtw3Kp4b1BxgYea_qEyGHsGtC773PAp5D0PakVqmzTN58SSZziynuuWUuLMRmBEHmwXtdgbaeXeKgXhBuRqa23MRCU-HScivbyEC06AWG1hjk8DI1jO80hDaNdhzCXgOGEYeHkLVZW_AstRnyuTLNZSEwVi13ApQkg33f2DgEd2aE20p71ZwbtEVJj2bKGtOO38bv9JG0xt3LhT5mR-2zdeIfiVEYsuTstFZUYoweDiONMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phldIq1Ucuin7jOyuyXLWxCXVQveggDf7q89LBG6BjLnMon-Bn251ueb_IrR_JFhO1JL9WdsncgyPSceERkYxt4MqHZFh7aluGbPm60H6kk2BjcpanNMgEe0AF6GN71sZSNqMdZoNe2u8KHE2tqDl9QYaCUlEL-qrFagl8KlFNZ-DbjzZFeW6QhD1LQtuegUrL-ljb857uZcWo1wHVHewoKSnBk7F_rEIvqJhVtSxPDA2u2effHW7lyx_FxCgLMSEVxnD1BfLDKbSaK1d8PczwyheBHwcwbpvhtjX3iIdnVhM10_xg8mytDJysZFwG8ar_YX7uk8xJmY13eMLso_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRjbzdVObOBd5bsr_xQXzMULAOk7fH8aa-JYrobogU6aeq_iqJEt9xgbO4MixybNlNIaP6WJ_nks0JMLhMTry7wT_sBdBN9D1hGI4hNVEUzLBwHq1ZVEmNb2iJ0GBHSWdbXFR7oHYV9gA_A82vzjXP-nYmNnfXoCTnPMHmuLv7_hPABnjupa-dM2a20vWY-oMbD1j0YOkbUOzecj-mYo18BtVEbZWcCpHHvLLFO0iYFsfPmHt163VpVHpEqDbKleEOLlrXtW_EwP1JVMYI_3eV7I2Soxv4xMhQ6RaRMTsTtqURorn-cPVK3JKDJVkNnt_7-Yl2hTexhTHz2cFJvE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8_wpUtRX8ezdb7X2cunomzlA6Om5xZGpa90mz3_7ZG_HOIIxbwbTKduFyc5x4_zDWmzrcajFOVfIAuP6dS4mN7M4ypEipyku-UNtRtfJjL7EpA7rjFyTyTTHgtPOssKbWG0F6Xe5IGfZFhVcXrzFjGUcTfSvMZWH_yJ_QFeX6g1dfwE_pzc2BvN1Mop_TYZwFvLOgv2doku9A7SiBWu8Cxc7J-Xme0o3E5XJtW9T_X8B-paHiQkEBCEeKcdTDwLZ3TnKTXXxwO2XWfPHnvnYltF_ffSR3uwQNTo3CSmml1o52rBk2a5LpiM_HxMwc-r-R4mT4Tisxy_WkfPrKd17A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5vzYChfIvq7avQSjgFAnubZChvIuPxipYmvoNJjwl8htBTTm08OzRdFyk_UAyOWhLTWsOeuySs2ypNFywwHGODiqyMPC8dt63GE5ArcLbCFwpHCW8AXYnszIyDE_OVaa1snExL9gc0jsAVVmcExkH1vZq5_XZIPoPhbXNKF36kOLEsncYYnR_Faei0oo8fggR6lgHIaeApLd9-5MZe2-JgSt6V-SYq79DT_nIzNVTE5mvYykpiB4MXc9LLeyK2H6r434ToXqzLSmHzRc64eTKkjbV2dMptZISOEH07Orqj8wTkm8R_uc2ArlIAMbwdhNQAAtyLprc2oxvAyVcTREA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استقلال با تک‌گل آسانی پیروز شد
⚽️
استقلال ۱ - ۰ پیکان @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461353" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461352">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSqclQWu1ai1slHqhK7QZHjCQqp2W-XZYf2Ihe4WAi7yN-O6MMCJiR6mwcYaB_8AWJJ7W7SPmG2RNN4U_6svNs7ciia4V7ojpeoB8rIlCBX4KM5U3ZkuEMl2oLDZtDVe2y4EsxrPfXeTi-KJCq4UecLI72pu0EwGEkZK451ryzjRNRHLOPQGtN2wKbfg0yuLSAkkne5CHLcKF_hbgVl4RJ22YbWNzmim2L71vTGTEFeU20LJysurEIXQvxDOA3dKpl2xcXekoAPPNyf7z6fLS6yIf6INr2VaRPhYKpIkXUkUWdPvYvNJejdlfZIRpvAPqt2Fch-UFRFs8xZKQRpfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461352" target="_blank">📅 09:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461351">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02784790ad.mp4?token=r6kzbVxORbizhI8Gw5hnDWi9qdIhj8IkC9E8axWD-4B0KHvWXt9ssT5wJNj1PC1bJMaaTRY-Vew1APkjjliFgLFO51Ep93DtzUs8WFEvT0o16s2uuXz7M2k8vK5KCkX32Zldsnpi6AcTn7Fs6CGf0uH78b6BTpjOApdUeyIssKdxciaii-bntTTRnEFBrH3AFd_4QN5RHVYRTJSPgByFvpBy3GRpkfoWLl1n1fXsNNNuFMf7nIHwCzp-X2u5hkb4fayCIO5FQzEs5Q-M7kE4f5RS7fYNPv4ypdFpI7OmJV3NQ7jNk-POlvK8vGIQgzrouRLWFQJ52CialQAqXJylIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02784790ad.mp4?token=r6kzbVxORbizhI8Gw5hnDWi9qdIhj8IkC9E8axWD-4B0KHvWXt9ssT5wJNj1PC1bJMaaTRY-Vew1APkjjliFgLFO51Ep93DtzUs8WFEvT0o16s2uuXz7M2k8vK5KCkX32Zldsnpi6AcTn7Fs6CGf0uH78b6BTpjOApdUeyIssKdxciaii-bntTTRnEFBrH3AFd_4QN5RHVYRTJSPgByFvpBy3GRpkfoWLl1n1fXsNNNuFMf7nIHwCzp-X2u5hkb4fayCIO5FQzEs5Q-M7kE4f5RS7fYNPv4ypdFpI7OmJV3NQ7jNk-POlvK8vGIQgzrouRLWFQJ52CialQAqXJylIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور به‌منظور شرکت در اجلاس بریکس عازم هند شد  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461351" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO7kaFMbvXFp11hKPNJ_P9P6NpdNlL0yEy2LXyThuaNpIXw_rin1e4ub6_2YPGX51tfTiv1-wawaBGSQ5XMo-wQAqDMV76WtJP25BquuyHOYlZaVDWK-utJNfSUrULbtGWNsX8dcj3v-pmf9m73YLn9DesB3rLnMrjIqbOkCifZNRDNWpSPkhRx2i15VaB3hHCIpTtyKGN9EY3ushu0qjF9zaMjVZLY-LH4S4GkLcI_7BL293CrEHg3ioYwJjo3ksvLA97O761qw5zF6ICJdHY3Gcz_n8QNveewxrg7Ki1y3aFiM2BjYeMvDalkqg4EHSE4UnRjbyi7jDlR1tgZLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش عراقچی به اعتراف مقام آمریکایی: بله ما ناوگان پنجم آمریکا در بحرین را با خاک یکسان کردیم
🔹
صراحت «هانگ کائو»، سرپرست وزارت نیروی دریایی آمریکا، جای تشکر دارد. او درست می‌گوید، نیروهای مسلح قدرتمند ما واقعاً «ستاد ناوگان پنجم آمریکا در بحرین را با خاک یکسان کردند»؛ همان‌ کاری که با دیگر پایگاه‌های پشتیبان تجاوز آمریکا هم انجام دادند. مردم آمریکا واقعا نباید هزینه جنگ‌های اسرائیل را بپردازند.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461350" target="_blank">📅 08:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461349">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBv4jsVujM_0vzfAZZjCB56zwIoYA59qzPYsEmQtcc06ROHX5yhgorw5PBOkG-e2cEDJ1g3n74noVJq0h4HXLgnv6jDRWznobgaRKOpluAD7ABQ2LSXYiQGL-5DtRHsTL-gnEIaPKJYnCsc5I40q1aPZgug4xBm5TSHJDHIGH8yVyRNXmODMTmWVjp1c2MEim92Gr9OEfsTjm5gA0eDLT5Wfde6V7Kv5nMfED_tor3q-XfGQYNvvAgBBtPLHUNruU521FFyHo20KZC_Gr9zaC4LpAWR-TZJO5SfGmPRGKbYAXX3REQ1y1TMYwGHKfEbYiqZE01qU9ewYCrJZ2uwVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور به‌منظور شرکت در اجلاس بریکس عازم هند شد
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/461349" target="_blank">📅 08:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461348">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎥
شوخی ۱۸+ «شفرونی» و کنسرت «شادمهر» در تهران!
🔸
در فصل جدید «پشت صحنه» گپ‌وگفتی دوستانه داشتیم درباره خبرهای ترند روز؛ مثل کنسرت شادمهر عقیلی در تهران، شوخی جنسی و توقیف «شفرونی»، فحاشی خداداد عزیزی، قیمت بنزین و تنگه هرمز و...
🔗
نسخهٔ باکیفیت را در
یوتیوب
و
آپارات
ببینید
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461348" target="_blank">📅 08:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مدیر جهاد کشاورزی ساری: بارش‌های سیل‌آسا حدودا ۳۷۹ میلیارد تومان به بخش کشاورزی شهرستان خسارت وارد کرده است.  عکس: مصطفی شانچی- روستای اسبوکلا ساری  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461347" target="_blank">📅 07:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هوای تهران امروز هم «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۳، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461346" target="_blank">📅 07:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461338">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7m8MeeV6UvyGr3j_l8SxlRrBAnIMGkS4I0ksBm_mwA9kg5TfBbtet5OBAKw9888FD4mpbQfqg1EqollPCSkzipEMDHYMuDBDIqWQQc6CgTY3T5lxy_bs9XMHyp2DA0PPcxJXmsL4Lg6KU5KIr6e2UtiBi_8Uddce3FmTDXdKzKKA45adiS8WxlG9ar_ER5ofUaekbgZ81u59fyit-N08WUKAkGf7rWZfVS9xafNFmut9Aub3H6g963PhcNv-Cqxk9JvcNqGnsTSP4-pLYJs8e4oGFw0YpWJw7HoUQ21WIQjLHkaOXjpO2_c9xLMdiYkg0GypMbzI1ssz5XBL0RyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBgVHkyyDwxkTCEVIKZgRzHSTf8IOMqQTEgsC1nHRz7oIRM_YJtRJQSovbPbKkRExZ7LQOeFf_kMQORXU50ne2bdX2G1BTmjjzvpNGLD4rjI2qtakLx2_vQerFCbvTrHSm3zp2WOXFceeTOYAgyyHCBQ9XpQLHoYc_gJsQASgEyASYJ9sSXXdoH3S8a4rkrg0bRlWn7zGywFzjSCmsp7vjgnLiDMTwBParl73WB1kmg9La03ipfHZoKSeJ8_kw15ldnACvaapN_KHYnCutyinY_MvX7OW25AN52qq1iMd5VYGR5BW5Cs4GO5esyKPYAQ5oU9Je2GG9BRPU31-XZ4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fthCOL7yOQ6HqU5jj7hZtg_ODU0XaJm1_hSQBCRgsfV2Y3ble4W1zW_rDDhcjxb1nLfzQLZDTBqXBvmKz4SNkcHabR9IMkLziXdi-6P2YDiIOdsZkm110NBai85UnvfT-SXLQqtHRIfk89Xs4S-iFoTmyROfDLhm2dE_s8-1qebzUCC0sBUaQ65iETDb_M5GK_VSj1UzRElgl_Rus7xKcTkJp_zJC21i917UHlkyaezbF1MBforIpYsujvF0xQF2PVWsYlm815Tt2dNLwelKs_B5H0Df_e5PmCgA2UMV2QCZ7p2I1FPycw21zkIQW6-6-A-JqWWZ_hR_qPghiQG9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAuk1iMi0jaHysqnMDdfQql1BT0A34qF8xe4Cg6Y2PFowR7iAib_p81W-oGly6uZN2i8bJDOzu9Z6ewi3jg82kCDn-rEVlv1dNBXYRZL7yC-lsJwQWxb6jSSH3K06eJccJzUidtrXnQRjizDZit7ymyVIDWRqxz6JhysnjKb-u0DMOSutd5Cc-3NdRSdKllE0Uz0xmudJh3Bo4UNHFuBKEmpGeUNx2wJRefCQQQclgl9lFnPRtIgOMTG9EMCPT0SulfNMWvBns2MjPeNuIiJ_HV26l0Bj2tnOx2baoY2gQSr1-Gdw0PFLhmGhO5enwjIEl0zbp9CwGSVHGthrLmS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWFqNmcBz0IeG_MU3RWCTwvQlnxif9bRUK8pRcmtG4qRN7MFav0px63fwlbO59knDHEMSc2Qo7Y7IMBfc2Nn0be4ET5rZpH6UHBoXGA_6lhzjw7i-IoUQdQ0SgWf48x9In6U8cArWM8jJj4l0M6O0BId6hkw7u6pK0Fzm_jIYEdBG6OEoIpiLJ03svjZ05tkSuFt3b4DIT4h1IxePr2AcMotycx5Cuj8e38nfcJ-VEjGnvrvtXwTqxp8pcVwZOAcqe15Pegel0lgIHvs1AZxILWWy8JfbuE6SGKa96lj6KREqFcYesWxu1woQPspa_PF2Vv7961nMfu5grlAF4595A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dF04f1hQSOaXLeRnxztKIupX_yImKk-NQKZqQbEYHjn8VjEjch5aj8hvaOdZv90ADrbk_VUD--3d-JgH9Bmqgs59TsrkFpJ5sx-tc7auUSwUYM9AhMOKjZxCUJSZBRTTiEdZV-T07UG_xVI2xzUcQwLcu8Q6V4L-_wMnv8sRP_lhHWi423WBBLpDJkesRUH79eRWOJ6wEZNnpu-tRQOfxTiG5j8EMAYM6dzIT4ruCEMzzRnyB_ODFf4Var6b4knQXSKYLa-QR5LSTULSj4PnqKKrD0y2nTMXacU-vvY0_ub1IMDNNxeBdQo4IlE_3oh9BM-eFYZ-eQwjwF6XGbkdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMqgJpVlND5k6J1-pu64nZX3fV-IwIdfv-dowWV-526Hbav3YEiEZH-QMO3mSf2UTWFbApdrmlgV00NWfYEPgxk9wGuqb_gUs9NbKMiNft-_55DcXOg1K88MBYtlGeqMC7Xz364B1l60cHxOFtCWaEICQ-lPQqeNiI8rjbzvFDX54uLcNkm3p8iPI6MudgZpYSmtTAKMc5GYVBo1T8QEeccXzQjSl-qItxfpeqBwYpH8RE32VvZHZuXrowyLiku4RppecqSAlZ8AnajQmitOvfmObeYU5qDSGj0vQRtHw70gDJnWTIBkgpEm1HEdb5NkdVuYHokGqzzuND9oMzR3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7CQ20SF-uLOExPyBXeFXGBfo4MQ-ph3YgE5OhxroG7zfRD6rSAz77JBob29xhK3yI-RAZXBtso-X2W8GmG__8ezAcb5F2Y5bxcCBvw2_HanT-dtNJGIllZJVdZWB66e4OQT7CXSYPNOqKHz-rqmP6_a7OpqXBpDMStgD22HTLTzneIuBbGGXSxTlWFcZ-kgYIc7FTOCSQm7aMjuBH65pz0DY5NFyXVodFrXjfJN4_SOBfACASdeWvDFhE5v6IjVQanBharrkbmetTbxDZObkSVKvLP4sN8FQbaSG0zi-Zvn6niddRzqUu51LpgCPJVrowD3kShp4EApRI5BqrbqSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
باغ‌وحش ارم؛ دریچه‌ای به حیات‌وحش در قلب پایتخت
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/461338" target="_blank">📅 07:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461337">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmaKzUjQ72JcY8xg8i2XI2xUQRUD-jecAB91goBWV_gP6QbOsQZVltVO_baF-zubn3trc1Y8RMI9xUsZla5i9o0061DLWtjb9pfFf4RY8yX7k6jxVtd9I1FdnctXKkNatXh6baKektyJK16pUV4lO7Yn19VmHHp-cJu598ZMxQo0XSk7XprjjJ8TzyJsBdeacPa9v6STtBZVY2DDeEE609tjJnrGQZPhVKKC_vpszKDN5ajRy7a8cp9INS8NkrykuQq8mRQwwg8lKcVtVv2P8l0yoxRr_lU0Bv138ojenJIHkleGmcei57Q-zsa-ebA20tU-HRmFW342P_oy-b5Ddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای آتلانتیک: خروج آمریکا از عراق، دستاورد مهمی برای ایران است
🔹
اندیشکده شورای آتلانتیک در گزارشی نوشت که حضور نظامی موسوم به «عملیات عزم راسخ» در عراق به روزهای پایانی خود رسیده است و قرار است آخرین نیروهای آمریکایی تا ۳۰ سپتامبر این کشور را ترک کنند؛ اقدامی که به بیش از دو دهه حضور نظامی آمریکا در عراق پایان خواهد داد.
🔹
در این گزارش آمده است خروج نیروهای آمریکایی از عراق یکی از خواسته‌های اصلی گروه‌های مقاومت و دولت این کشور را محقق می‌کند.
🔹
الینا ال. رومانوسکی، سفیر سابق آمریکا در عراق، نیز به این اندیشکده گفت: کاهش حضور آمریکا در منطقه طی نزدیک به پنج دهه، همواره یکی از اولویت‌های اصلی دکترین امنیتی ایران بوده است. با توجه به این پیشینه، پایان «عملیات عزم راسخ» را می‌توان دستاوردی مهم برای گروه‌های مقاومت و ایران دانست.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/461337" target="_blank">📅 06:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461336">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97223f187b.mp4?token=T1iBkJ-IrSujiYyrq3UsgZKSmdg-hC46S01MzxVjDC4NHWFvGDkASXpk40e9K8CLuNiZ_jd7MQEaUlg3iasktQAO0zyWI9V-2BdfBGGEJzQYMWoYcym7O6bR458avDCOqlbJ-PPpJ0CtU0pScmefoK8wikKth-mjTKn93A1RVvP9-P0sm15SW6otej_SO6iCX4l1w9W_KNOi0NXugTrvtazTV-JM_6FPoXISe2-ifNCjzkdmz7VMSYoBdidAkKTcI0cv_BiqNK9Js9NeGI7VN8gVNhmm0ydZLDMJSMvQWleCWGfWGKoELK6t1n2PZRvjuEm9ojnqIvqvbAaDzwHpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97223f187b.mp4?token=T1iBkJ-IrSujiYyrq3UsgZKSmdg-hC46S01MzxVjDC4NHWFvGDkASXpk40e9K8CLuNiZ_jd7MQEaUlg3iasktQAO0zyWI9V-2BdfBGGEJzQYMWoYcym7O6bR458avDCOqlbJ-PPpJ0CtU0pScmefoK8wikKth-mjTKn93A1RVvP9-P0sm15SW6otej_SO6iCX4l1w9W_KNOi0NXugTrvtazTV-JM_6FPoXISe2-ifNCjzkdmz7VMSYoBdidAkKTcI0cv_BiqNK9Js9NeGI7VN8gVNhmm0ydZLDMJSMvQWleCWGfWGKoELK6t1n2PZRvjuEm9ojnqIvqvbAaDzwHpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در خواستگاری دنبال اعتراف گناه نباشید
🎙
حجت‌الاسلام شجاعی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461336" target="_blank">📅 05:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461335">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ce2bba6b.mp4?token=sRVNzC9VktomEHQ5GPIHO1c6h0ob1qwzOJbdPxyuAPpz-bKLUXXJKIHk_P2KeOXd8MmPJb4Kco5_BfA2gJL492fMz_MQ1ii0qpJyoU5145gBKSYIiDxg3lGyE0XV_NgALAabuk2hJqjG7GV2hpT0k7PSof1DVEhZA2vGwvLdCmkNbVhkRdNIPGgAg1JLFFBlS3K0636xADiKAgMIJBksQhl32lPr4ifFMmqsQFdW69V6lKMy9ys_RbnbtI5tYv3hYPRD-VMLkTNr-Lce56yKBEt66HcMUAMtXKoW8C-r94duRgpdUeuGpcr5S-q82tjpYUqTYG18h6eLn4lW1RQY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ce2bba6b.mp4?token=sRVNzC9VktomEHQ5GPIHO1c6h0ob1qwzOJbdPxyuAPpz-bKLUXXJKIHk_P2KeOXd8MmPJb4Kco5_BfA2gJL492fMz_MQ1ii0qpJyoU5145gBKSYIiDxg3lGyE0XV_NgALAabuk2hJqjG7GV2hpT0k7PSof1DVEhZA2vGwvLdCmkNbVhkRdNIPGgAg1JLFFBlS3K0636xADiKAgMIJBksQhl32lPr4ifFMmqsQFdW69V6lKMy9ys_RbnbtI5tYv3hYPRD-VMLkTNr-Lce56yKBEt66HcMUAMtXKoW8C-r94duRgpdUeuGpcr5S-q82tjpYUqTYG18h6eLn4lW1RQY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری مزدوران سعودی و اماراتی در ورودی شهر عدن
🔹
صدها نفر از مزدوران سعودی که از مناطق درگیری با رزمندگان یمنی فرار کرده بودند، تلاش داشتند وارد شهر عدن شوند؛ اما شبه‌نظامیان استان‌های جنوبی (همسو با امارات) مانع ورود آن‌ها به شهر شدند.
🔹
در این میان منابع یمنی از درگیری شدید میان آن‌ها خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/461335" target="_blank">📅 04:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461334">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqGGhhLQ1BBLqxfCDeE56317wI9HTgrm4Cj0BUVkYtX3LkSH4xorBj1iEXAIRxstOlvz95tgPoNy0k1xEw9wHUfWDtasHNmUxH5TFYDxhCe4DfEFfV2lN0UY7XvOyJXA2_dBDD8to_ZyvjV9Ebee0UdSxABkSJHH50HqvNIxy0jQ_j7AX6NdwbRamZy4_eGM-1ADyB9V0LP4p4f8zPBAULSQzlsx6hEppWCt13fN0ifMmfVSyXP0Ifun6xiyyq5Jos876XwFWl_xUfzO4fJa3A-fFbB7Clp6JIUD4YKRLQBpxlZUOWCROuHaTilmAp5_1Qm3OCTOaenuFlxIqiHI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توهمات ادامه‌دار ترامپ؛ ایرانی‌ها توان جنگیدن ندارند
🔹
در حالی که رسانه‌های آمریکایی از
نگرانی عمیق در کاخ سفید دربارۀ مقاومت بالای ایران نوشته‌اند
، ترامپ به سبک همیشگی خود بار دیگر تلاش کرد با بلوف‌زنی، حقیقت را وارونه جلوه داده و مدعی شود که ایرانی‌ها در وضعیت بدی قرار دارند.
🔹
او در مصاحبه با شبکۀ محبوب خود یعنی فاکس‌نیوز همچون روزهای گذشته ادعا کرد که جنگ علیه ایران بلافاصله پس از انتخابات میانه‌دوره‌ای در ماه نوامبر پایان خواهد یافت.
🔹
ترامپ مدعی شد که ایرانی‌ها به سختی به جنگ ادامه می‌دهند و در تنگنای شدیدی قرار دارند.
🔸
در این میان مجری از او پرسید چگونه است که موشک‌های ایران را نابود کرده‌ایم و آن‌ها همچنان شلیک می‌کنند؟ ترامپ نیز با دستپاچگی گفت آن‌ها همیشه مقداری موشک دارند، آن‌ها موشک‌های زیادی داشتند.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/461334" target="_blank">📅 03:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461333">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9Os6uZR7KRlYjyQemffROcMlY8TH1_eBoHJxwEnq3vPZJ1z-wAtztD7iWDwPey6DhE3Juh-e_cp2x1O4ZOiyJtdQxwQ7KuohzfryRf3Y8fCbxFPgUkiRXqnYmcaaxggKFM-VN3yJeMz7pWl_UZWyhfspimtWs-FhO_niXfqwCfor9howrIulaJyFAy3w4hlAnKMaIUr_k9Cs63SD7UURgD9LZzpi6B4D7at4IdzQ9FIizdd8mi8TOcyHovC_8MvLoP_Y9b74HMwANriCFnAXI-JHuWdZkHhHHFD4SFmg85uRxciaKROH7K0k8EG508538gzhcu40obJ_a7jCzAKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور موشک بالستیک چگونه کار می‌کند؟
🔹
موتورهای پیشران در موشک‌های بالستیک، قلب تپندۀ این سلاح‌ها هستند که وظیفۀ غلبه بر جاذبه و رسیدن به سرعت‌های مافوق صوت را برعهده دارند. این موتورها عمدتاً از دو نوع سوخت جامد و مایع استفاده می‌کنند. سوخت‌های جامد به دلیل پایداری بالا و قابلیت آماده‌باش سریع، در موشک‌های میان‌برد کاربرد دارند، در حالی که سوخت‌های مایع با چگالی انرژی بالاتر، برای پیمایش‌های طولانی‌تر و دقت بیشتر در موشک‌های قاره‌پیمایی استفاده می‌شوند.
🔹
فرآیند احتراق در این موتورها با دقت بسیار بالایی کنترل می‌شود تا فشار خروجی از نازل، نیروی پیشران لازم را فراهم کند. در موتورهای سوخت مایع، پمپ‌های توربو که با سرعت‌های بسیار بالا می‌چرخند، سوخت و اکسیدکننده را به محفظه احتراق تزریق می‌کنند. این فرآیند پیچیده باعث می‌شود که موشک بتواند در مراحل مختلف پرواز، تغییر شتاب و مسیر خود را با دقت میلی‌متری تنظیم کند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461333" target="_blank">📅 03:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461331">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAINaEtby2GBlvBChyQQKSwsSeMXUdiHYali-rUhcQY-KfMD6P-mfuzuk0kfMF5xlhirg4QzIWHbVMlQLmORrkVUgnTHazwIaC8feiB3w-3I6QBZsLE8KoV_6CggddL69x3G8jZO0WbbJwSQUebHCtCO_eo_UICf7d0bFM3yB_GLp3Vo7X3rOmg7S87v3UxIbudM8I23EK4eSZ1Vs6qNLyLn3qF9EgKfBdnSHYbOi-QjtHgH4PH5OmOVwOt2gX15SSACCq2Gw9247vxLFpHtZs_jm0sXgSasyDBQtBbpKENwtcVF-ZEYrRHvEAe8mVFD7SHP0SmqPCMA4NgrYmht1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tylylhuZUcbtL9yAS8mFyZ4swV1T72ySGGa7DIgQHzEUFatng8Xl_aps3huKqrUUA0d-eN51Vq2S6IiF-Vb9dZVDAI-DqAgnJPkZdZYilkLULl_0pcHEmGVkesnZwiiyhtPAxJ2xIbbbnVuBDuLLjCjlM0pj-yarXNY_KLqd1nUen4SRsZRMtmB9I92OKi7whuJZL3O7hH51tgmVcqA73VF6PZqO7DTSlFwJ_9wt7rtMfhsDFKuaKLMcm4SNfBvn8gBqk4RnAAhppWQ_iqsUfoGZN780bK93Lp0RCgUikRHjl637GPD0CvmkNXeuuvG6cRNfkZYcoir6dhrNDbDgLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر جدید از اصابت دقیق موشک‌های ایرانی به پایگاه موفق السلطی
🔹
یک حساب کاربری اوسینت  با انتشار تصاویر تازه ماهوارۀ «سنتینل-۲» نوشت که نشانۀ دست‌کم ۴ نقطه اصابت موشک در پایگاه هوایی موفق‌السلطی اردن، پس از حملات موشکی ایران در روز سه‌شنبه، وجود دارد.
🔸
بر اساس این تصاویر، یک مسیر تاکسی‌رو و سه آشیانۀ هواپیما به‌طور مستقیم هدف اصابت قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/461331" target="_blank">📅 02:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461330">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FczKntjyMYCbk7ECx1kc2dFzHaY9kO3TXBrdw2i7iAJTjFbqPyfZcxxcfVslTFzivnLNyIF6iRTxU3os_u1Ftp8MKO26dwj6yEvSCFMdA3EC9xcnUW_yavnk3ksx65l07ocAkJTyYl3thXAzKmVhLFA8yWCZJ_4ZA2IUocx7Qh3Gzw1Jg_uk3waa5C3_ps74syJTzCn84wEg8ngo-3tspHkeorJ8j5TBMJzhJhxk_ivyaApophKk45VslQoT46UKnE6nI01HOBkHlqSVNKlUq-QXDO1AktqvIFg__iR3ivZ-SINfa5BTEp7AvH6AAOAs4UP4lFLMfeMzDjgECjejCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیۀ وزارت خارجه دربارۀ تحولات مرتبط با یمن
🔹
جمهوری اسلامی ایران بر موضع اصولی و ثابت خود مبنی بر لزوم احترام به استقلال، حاکمیت ملی و یکپارچگی سرزمینی یمن و خاتمۀ محاصرۀ غیرقانونی و غیرانسانی این کشور تاکید می‌کند.
🔹
بدون تردید امنیت و ثبات در غرب آسیا و منطقۀ دریای سرخ، بدون رعایت حقوق حقه و کرامت مردم بزرگ یمن حاصل نخواهد شد.
🔹
جمهوری اسلامی ایران ضمن تأکید بر ضرورت توجه به مصالح امت اسلامی، به‌ویژه در وضعیتی که منطقۀ غرب آسیا با شرارت ظلم و توسعه‌طلبی بی‌سابقۀ رژیم صهیونیستی با همدستی آمریکا مواجه است، یادآور می‌شود که حل مسائل مرتبط با یمن از طریق ادامۀ محاصره و یارکشی نظامی ممکن نیست.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/461330" target="_blank">📅 02:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461329">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
کنجی گزین و تا به قیامت مُقام کن...
🔸
غزلی از رهبر شهید انقلاب در نجوا با امام‌رضا علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461329" target="_blank">📅 02:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461328">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974851bf5b.mp4?token=PU5zKkvXVcE7ey_F7s6QCVbmoWIHIbUhMbNY5GJ1abF14tklBUHFobz62kJQ4yabri_KfPXuXXGRyybczy6Jr_Wt2AJCUzBHe9BAVCLqIeRLoXChfVVBceZ-CWMqYi7wwdnZsrwLrdf-wsaDahcw7IeqAwHOx-ogLHyAg_ntop-VcPOduSiB5Vpuz6rd3D5eIwhihB4p8fMI1LlKSxdQEei62Kp0aVaMzDMJw6uCrglDu-VOjNMvv-Mprwrhxj7tf7iTJpvHtGYAtTY50pjbqdkAG8mu1t2AiVfPFa6uumaMzKd1NKHolfqUIzvRHtNofVoDQhDkWK_jq0p_YhS3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974851bf5b.mp4?token=PU5zKkvXVcE7ey_F7s6QCVbmoWIHIbUhMbNY5GJ1abF14tklBUHFobz62kJQ4yabri_KfPXuXXGRyybczy6Jr_Wt2AJCUzBHe9BAVCLqIeRLoXChfVVBceZ-CWMqYi7wwdnZsrwLrdf-wsaDahcw7IeqAwHOx-ogLHyAg_ntop-VcPOduSiB5Vpuz6rd3D5eIwhihB4p8fMI1LlKSxdQEei62Kp0aVaMzDMJw6uCrglDu-VOjNMvv-Mprwrhxj7tf7iTJpvHtGYAtTY50pjbqdkAG8mu1t2AiVfPFa6uumaMzKd1NKHolfqUIzvRHtNofVoDQhDkWK_jq0p_YhS3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غم شهادت شهید خامنه‌ای، هنوز با عراقی‌هاست
🔹
دلنوشتۀ بانوی بازدیدکننده از نمایشگاه بین‌المللی کتاب بغداد برای امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/461328" target="_blank">📅 01:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461327">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9pBuW76WVHNz5dfnQjq5lLGDPWDZnPpNsHLf9HeHhF8lXHMt6eb4ukBtJIZGqHlSGLf8lQhQUmP_c34Mu5NL_Dwi-sITDMgeOzvIX8UTkyeDcoBDPeVCfvgGNMsNOdnCzmDtptumJfso9ZwKyDxBZilwmABURHbATjUcxRFM0BhReLG9nq5L6BVaKf7--iHxXhCY2pIKS0q9HmJFl1wgLG3pthvQAgA3ar4xKQY7QyOtLY0xFj6KD63aCnysRuRpiSV1zuRKW7zJUPMffQZqGYTPaYGg735bkHcKm9XHxQBzpK_CacSZ6FTCxsGFDe5tKPUjFwzFUuykLqWbi_8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی گسترده در مسیر خط لولۀ نفت عربستان
🔹
داده‌های ماهواره‌ای ستونی متراکم از دود سیاه بر فراز جنوب مدینه در عربستان سعودی را نشان می‌دهد و گزارش‌های منتشرشده با استناد به داده‌های ماهواره‌ای، از وقوع آتش‌سوزی گسترده در یکی از تأسیسات مرتبط با خط لولۀ نفت شرق-غرب عربستان حکایت دارد.
🔹
طبق گزارش‌ها، داده‌های ماهواره‌ای نشان می‌دهد شدت آتش‌سوزی در این منطقه برای چند ساعت به بیش از ۷۰ مگاوات توان تابشی رسیده است؛ سطحی که به گفتۀ تحلیلگران داده‌های ماهواره‌ای، می‌تواند با نشت قابل توجه نفت خام و آتش‌گرفتن آن تحت فشار بالا مرتبط باشد.
🔹
هرچند هنوز بیانیۀ رسمی از سوی ارتش و انصارالله یمن منتشر نشده است، اما برخی کاربران احتمال حملۀ موشکی از سمت یمن به این خط لولۀ راهبردی را بالا دانسته‌اند.
🔸
این خط لوله نفت خام را از منطقۀ بقیق در ساحل خلیج‌فارس به بندر ینبع در ساحل دریای سرخ منتقل می‌کند و یکی از مسیرهای مهم انتقال نفت عربستان برای دور زدن مسیر دریایی خلیج‌فارس و تنگۀهرمز محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/461327" target="_blank">📅 01:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461325">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ونس نظر بی‌پردۀ فرماندهان دربارۀ جنگ علیه ایران را جویا شد
🔹
روزنامۀ نیویورک‌تایمز گزارش داده جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در اقدامی غیرمعمول طی بهار و تابستان مستقیماً با فرماندهان نظامی آمریکا در خاورمیانه، اروپا و آسیا تماس گرفت و از آنها خواست ارزیابی‌های بی‌پردۀ خود را دربارۀ جنگ با ایران ارائه کنند.
🔹
به گفتۀ افرادی که با او گفت‌وگو کرده‌اند، ونس پس از برخی از این گفت‌وگوها، نگرانی‌های عمیقی دربارۀ راهبرد کلی و چشم‌انداز موفقیت در جنگ پیدا کرد.
🔹
این ارزیابی‌ها نشان داد که حکومت ایران تا چه اندازه از تاب‌آوری برای تحمل هزینه و فشار برخوردار است و همچنین مشخص کرد که ذخایر تسلیحات دفاعی آمریکا برای مقابله با حملات تلافی‌جویانۀ ایران محدود است.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/461325" target="_blank">📅 01:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461324">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برخی منابع عربی از حملۀ هوایی عربستان سعودی به بندر المخا در یمن خبر می‌دهند.
🔸
همچنین شلیک موشک توسط نیروهای یمنی به سمت تجمعات دشمن سعودی نیز گزارش شده است. @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/461324" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461323">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برخی منابع عربی از حملۀ هوایی عربستان سعودی به بندر المخا در یمن خبر می‌دهند.
🔸
همچنین شلیک موشک توسط نیروهای یمنی به سمت تجمعات دشمن سعودی نیز گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/461323" target="_blank">📅 01:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461322">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نگرانی آمریکا از مهندسی معکوس زهپاد خود توسط ایران
🔹
بعد از اقدام جمهوری اسلامی ایران در تصاحب یک فروند زیردریایی کنترل از راه دور آمریکایی، واشنگتن نگران مهندسی معکوس این فناوری پیشرفته خود شد.
🔹
خبرگزاری رویترز در این‌باره گزارش داد که ایران احتمالاً زیردریایی…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/461322" target="_blank">📅 00:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461321">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5869d8727f.mp4?token=ftqocHEun-XUae2v9l28WJzbYK5VDhxfBCiBc9bLy507VqGEshDWx1nuYgTsYpjmPeBIHcCSr-JHNKJfZS0JW7l2G53rECby6_9pSJYYwjqqySorD1BRVhKwpnaLQ9RehgefeSNZ1iC2NFRg126pFq3JwZNOpkS8vSz_1BbTSYuIvYkuzZ_opTtpiSv3khC76HcHSdrn1MPL4UWG9Xh-Ft7j-ngSsY_0aLNaibzT_keaKLV10uKcM2UQt1OjMsHuuXhlAAf3wloRJVjaUKPXr-a3w07WkG2ae3PTyNWllDD8FEZ9mL9QxBekV4TnGdqTqlpUIL21edtXkj_cYujtXkED4OtY12Zrj3v4QM6XBMHwxF640Fy9LUN83-cBjZgPWM13QlY76mc0W5n-RLIALye6nq4ihYIxe-URFRa_HHHx-xSyJeTfHi8XRzNH-PWY6ZPoMzDnvU_1x_6SBnf2U7VLecMT9lTzfvfANjhiXJLHy5uVFoQpFtZKtfMPs3KZ4dhy6f34mCuG1lbtazrRW_9gUPrUxLVEpoYoM-U-_73TWtddsR7o3d_kGkaVprHN5P1rZEdKJzPIqvZh7QLsyty09lwGaKGscnyyoKhYXAVCiT7z3gGh9qtifPY3Tje4TlZ5ALDVPVF2uytnnROmrOuQ0WYIxpMZN6al7QF7ULk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5869d8727f.mp4?token=ftqocHEun-XUae2v9l28WJzbYK5VDhxfBCiBc9bLy507VqGEshDWx1nuYgTsYpjmPeBIHcCSr-JHNKJfZS0JW7l2G53rECby6_9pSJYYwjqqySorD1BRVhKwpnaLQ9RehgefeSNZ1iC2NFRg126pFq3JwZNOpkS8vSz_1BbTSYuIvYkuzZ_opTtpiSv3khC76HcHSdrn1MPL4UWG9Xh-Ft7j-ngSsY_0aLNaibzT_keaKLV10uKcM2UQt1OjMsHuuXhlAAf3wloRJVjaUKPXr-a3w07WkG2ae3PTyNWllDD8FEZ9mL9QxBekV4TnGdqTqlpUIL21edtXkj_cYujtXkED4OtY12Zrj3v4QM6XBMHwxF640Fy9LUN83-cBjZgPWM13QlY76mc0W5n-RLIALye6nq4ihYIxe-URFRa_HHHx-xSyJeTfHi8XRzNH-PWY6ZPoMzDnvU_1x_6SBnf2U7VLecMT9lTzfvfANjhiXJLHy5uVFoQpFtZKtfMPs3KZ4dhy6f34mCuG1lbtazrRW_9gUPrUxLVEpoYoM-U-_73TWtddsR7o3d_kGkaVprHN5P1rZEdKJzPIqvZh7QLsyty09lwGaKGscnyyoKhYXAVCiT7z3gGh9qtifPY3Tje4TlZ5ALDVPVF2uytnnROmrOuQ0WYIxpMZN6al7QF7ULk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتهام بزرگ خداداد عزیزی: فدراسیون پول به‌روزرسانی VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند.
@Sportfars</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/461321" target="_blank">📅 00:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461319">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ذخایر راهبردی نفت آمریکا باز هم کم شد
🔹
درحالی‌که قیمت نفت امروز به مرز ۱۰۰ دلار  رسید، آمار جدید ذخایر راهبردی نفت آمریکا که لحظاتی پیش منتشر شد نشان می‌دهد که این ذخایر ۱.۲ میلیون بشکه دیگر کاهش یافته و به ۲۸۵ میلیون بشکه رسیده.
🔹
با بسته شدن تنگه هرمز،…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/461319" target="_blank">📅 00:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461318">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حادثه برای دو شناور در نزدیکی سواحل عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه‌ای برای دو شناور در نزدیکی سواحل عمان خبر داد.
🔹
بر اساس این گزارش، این حادثه در فاصلۀ حدود ۴ مایل دریایی غرب شهر خصب در عمان رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/461318" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9264531775.mp4?token=dluU27YPut71SXCbo_uL52jwoMqrtlgVt6stM5NAPCV9gQp15KCbLy5GW_rzoqOY8kQMnnM3KCk0_d6rTG2k5ga6kR4HXXscdtKTZdZWDu4ICXZrnaU-2fI-BRKbvVExenkVAwSqySQa8qy1tBqdyihAUox0boBf9W64tuC35NuitHW25lyd9SN014uUVM8CPF6g8-TnxbojE1CEetjCipPubSmTjSNOdQ2I5hS8XS3SDKVQI0of5dgjYbNPw0ynjrSpeoEqpE3koM7QSMhDa7WTuScEtTTrTP_iLaRMpWIStiaQMrTOAnL7wJ8Q4jNiEROrrkxTkPQHWE5pkochGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9264531775.mp4?token=dluU27YPut71SXCbo_uL52jwoMqrtlgVt6stM5NAPCV9gQp15KCbLy5GW_rzoqOY8kQMnnM3KCk0_d6rTG2k5ga6kR4HXXscdtKTZdZWDu4ICXZrnaU-2fI-BRKbvVExenkVAwSqySQa8qy1tBqdyihAUox0boBf9W64tuC35NuitHW25lyd9SN014uUVM8CPF6g8-TnxbojE1CEetjCipPubSmTjSNOdQ2I5hS8XS3SDKVQI0of5dgjYbNPw0ynjrSpeoEqpE3koM7QSMhDa7WTuScEtTTrTP_iLaRMpWIStiaQMrTOAnL7wJ8Q4jNiEROrrkxTkPQHWE5pkochGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امت مبعوث خستگی‌ناپذیر در شب ۱۹۴ هم حماسه‌آفرین شدند
@Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/461316" target="_blank">📅 23:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461311">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUP_V4wly0v6HVMO6xMm5RQ37T6mSEkVqsktaEZJZqCTKKH3pPaLLcKCoytobQMDvAkZaMEo-C4osWf0O0JR6Jr-rmubFhgobryNTXkUnwQnX_d-vx0NKXVRY2cOcIvEFB_ks4ztxlMHDbt53eVE943UXafvSFldvGkdpdydC7kW53Sba2qECV9Y1UPuQYn2sjpfu6tMIbzjJuqfNQM2vso5YBa84JWr5ngXLgEecfUVniRKy6Xihi9-my0wlh3nUAqijI9PrjU--YXbAofwLaKJ3kAUk6RaZ2VrAMJ0N1e1Jr_cq-yDP8Oibx0Vmlbg-nyZ1jAKPFmVIIj0_oD4sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AV1zPwG7O7ymqA_zO0REEF-0xVvEwsIp_1lQopZViRdJ2oZvZYsM7p6BI9L_27-Mizf5DBCuuJlsOIHVJUewzUBfc4hUninFvFjFLVg8zeDA8bUbJf3jIR4vDRTOkbaqCnOG0cKtKbLpDYSDqDl5XIU6NJDtisSLBR3tWn8jICVKnD5h2Ir7bxB4rFV8yrPfpLfbLzJ9EpaWgdF37Ka142-_mOnaAYN3Q8bSq1fEvEfmuC2F2uVSkeGjfTbMXQ0UVuTDptezgDPE2GYlNRycnJLTPe7Xq4G3BIDWj7gFixUueffznPDS5YV4N6CDKvf0ec7gRbi0Iu4ovrAzFzp06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBOHfsK3jFNG79YTVLxFysLmhH5toqqNTkiJIEnxQ1jbLjVtAemV7Zkh1Egbrpl-rox8tBvsMDlmxwDBu5HSCBkXkuYFUdoRJBU0H2RCASA9EF7wy8hgwxXwxUAeEUpLp63gOOzvt9sYTHeqQkkYSMWWUrfiBExjUh_rCzIcHAOnO9BSdnwmZEMWPgQgTUqRECOYODywyasQ8P3zbuAiZyuNf4JtIaRtXba7kFCvQgxEYFwMhrEUfAiDwMkJTfTpaGZ_V32gniksso0fBI0N2jVHT2xZnI0fRoRex74u_UE_7hHdpjZ2WrASmKNfeLex980SqAOYs182i9nvJo0ejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvxRmzx0UcrH2JHTSQ6kVDCsPYV7KL8K7l5SZgGfb5pwok99C8OI8LrRN9er5jNiGeMnQnsRtC11qX4yIJBTlyvEmhGtqM9-TPebXOb7_0E6x4wspcNUwTeSaEf74rCTsTt9eRp5ctVoc1jEvUE3raCbFuuRAsTl3x2EhETUaP0BSFLEC0QIKsHv3IlUqgAJIh-0MAPk4qnmi2SkMp4MJm-LpYjiOBuH2ErGiLzHS6_tRccugyfwLQ7Efu-rsfwPZGJh7PY6qzybo-ecCmoJldY4bmNHqHzcQaCbsZ9r1AlHy8EDfLQjPQXPOh7ziytuMILquOhMiBlU5HapgbAyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXBfFr88zCLPOZTWdVqH6X1GoJ0bndfCAoMoTZrLDbANrI5UAu2Vvw8KD34Da71bOEDwQgKKcqGrRnDWGustuOKGcn-C4Sy9KzLMNeWc9Ayh5TXrQMMIKqF9eHOQOxrzjWf9U2ieXUs4m83rFaB8EuIPJespSvo6RNrESY8symkMKJ5vlWTgRqMoKbKfAefU3JlXzG6DSkgYcBzhqZi3-Z6UcJq1lkyYdicqAnN2lvwAELsz3q4NXdoPu-O67aRDjldNCabf3fxRobgh7ln2d_hlXIjnFDtCN3Uoc60cXb5JwIthD3goG4mZujgX5aNutfm12vjpvw7LMW3uQVeXDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دریچه‌ای به حیات‌وحش در قلب پایتخت
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/461311" target="_blank">📅 23:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461310">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
ما
معلمان حق‌التدریس
با وجود اینکه خود آقای وزیر سال گذشته قول دادند
قرارداد معین
برای ما انجام شود، هنوز این وعده عملی نشده است. اکنون گفته می‌شود دیگر قرار نیست این کار انجام شود، چون نیاز آموزش‌وپرورش به‌تدریج برطرف شده است. زمانی که به ما نیاز داشتند می‌گفتند قراردادمان را درست می‌کنند اما حالا می‌گویند انجام نمی‌دهند. ما عمر و جوانی خود را پای این کار گذاشته‌ایم، اما اکنون هیچ امنیت شغلی نداریم و با حداقل حقوق مشغول به کار هستیم.
🔹
ایثارگران و فرزندان شهدا، فرزندان همین آب و خاک‌اند و شایسته نیست پس از سال‌ها خدمت، همچنان به‌عنوان راننده استیجاری بلاتکلیف باشند. متأسفانه رأی وحدت رویه مورخ ۱۴۰۳/۱۰/۱۱ موجب محرومیت جمعی از
ایثارگران
راننده از
تبدیل وضعیت
شده است. از مسئولان محترم تقاضا داریم برای رفع این بی‌عدالتی و تعیین تکلیف و تبدیل وضعیت این عزیزان اقدام کنند.
🔹
وضعیت
آسفالت ورودی اصلی شهر کرمان
، از بعد از بلوار حجاج تا کارخانه سیمان، بسیار نامناسب است و چهره خوبی به شهر نداده است. مسیر از پل شهید معافی تا پل نعل‌اسبی فرودگاه و همچنین محدوده بین دو دوربرگردان، پر از گودال و خرابی است و خودروها آسیب می‌بینند. لطفاً این موضوع را پیگیری کنید.
🔹
دو سال پیش از شرکت
فردا موتورز
یک دستگاه خودروی SX5 پیش‌خرید کردم و حدود ۶۰۰ میلیون تومان هم پرداخت کردم. قرار بود خودرو طی ۱۵۰ روز کاری و با پرداخت حدود ۱۵۰ میلیون تومان دیگر تحویل داده شود، اما اکنون دو سال گذشته و هنوز کسی پاسخ‌گو نیست. جالب‌تر اینکه وقتی پیگیری می‌کنیم طوری برخورد می‌شود که انگار
درخواست انجام تعهدات قراردادی
، توقع زیادی است! می‌گویند اگر ناراحت هستید، بعد از دو سال پولتان را پس بگیرید. سؤال اینجاست که چرا با وجود انجام نشدن تعهدات قبلی، همچنان پیش‌فروش خودرو ادامه دارد؟ لطفاً مسئولان و نهادهای مربوطه این موضوع را پیگیری و تعیین تکلیف کنند.
🔹
من یک راننده تاکسی هستم. امسال دولت در ابتدای سال
حق بیمه رانندگان
را بیش از ۹۰ درصد افزایش داد. از اول تیرماه نیز ۲۰ درصد دیگر به حق بیمه اضافه شد و طبق اطلاعات سایت تأمین اجتماعی، از ابتدای پاییز مجدداً ۲۵ درصد افزایش در نظر گرفته شده است. خواهش می‌کنم پیگیری کنید این میزان
افزایش حق بیمه
بر چه اساسی انجام می‌شود؛ آن هم در شرایطی که درآمد ما رانندگان به‌دلیل جنگ واقعاً کاهش پیدا کرده است.
🔹
لطفاً مشکلات ما کامیون‌داران را به گوش مسئولان برسانید. یک جفت لاستیک بارز به ۱۴۰ میلیون تومان و لاستیک چینی به ۱۷۰ میلیون تومان رسیده است. با این وضعیت کرایه و درآمد، چطور می‌توانیم یک جفت لاستیک بخریم؟ متأسفانه مسئولان توجهی به
مشکلات کامیون‌داران
ندارند.
🔹
ما ساکن شهر آباده هستیم. فرزندم در مدرسه هیئت‌امنایی تحصیل می‌کند. دیروز برای ثبت‌نام به مدرسه مراجعه کردیم که با درخواست شهریه ۱۰ میلیون تومانی مواجه شدیم. چرا شهریه باید نسبت به سال گذشته دو برابر شود؟ در حالی که سال گذشته هم مدارس آنلاین بود و شهریه را کامل پرداخت کردیم، اما نه برنامه خاصی داشتند و نه کلاس بیشتری نسبت به سایر مدارس برگزار شد. لطفاً
وضعیت شهریه مدارس هیئت‌امنایی
را پیگیری کنید و شرایط خانواده‌ها را در نظر بگیرید؛ مردم توان پرداخت این مبالغ را ندارند.
🔹
لطفاً از شهردار منطقه ۱۵ درباره وضعیت
وانت‌های میوه‌فروش در افسریه
پیگیری کنید. این وانت‌ها به‌صورت قارچ‌گونه در حال افزایش هستند و بیش از نیمی از خیابان‌های اصلی محل را اشغال کرده‌اند و باعث ترافیک شدید در افسریه شده‌اند.
🔹
در میان کارمندان دولت، قشر زحمتکش معلمان به‌شدت مظلوم واقع شده‌اند. بنده ۵ سال سابقه خدمت دارم و با حق مدیریت، کل فیش حقوقی‌ام ۲۸ میلیون تومان است که پس از کسر بیمه و سایر موارد، تنها ۲۲ میلیون تومان به حسابم واریز می‌شود؛ سؤال این است که معلمان با این وضعیت چگونه باید زندگی کنند؟
🔹
من از اهالی
روستای کردیان در شهرستان باخرز
، خراسان رضوی هستم. چند سال است که در فصل تابستان و پاییز با مشکل
کم‌آبی
مواجه هستیم.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/461310" target="_blank">📅 22:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461309">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آخرین وضعیت میدانی جبههٔ یمن
یک منبع اطلاعاتی آخرین وضعیت جبهه یمن را تشریح کرد:
🔸
۱. از شب گذشته تاکنون طی پیروزی‌های پیاپی انصارالله در ساحل غربی یمن، مناطق مهم حیث، خوقه، بخا و جزایر حنیش و زوقر به تصرف درآمده و آزاد شده‌اند.
🔸
۲. عصر امروز نیز مناطق ذباب، تنگهٔ باب‌المندب و جزایر استراتژیک میون تحت کنترل مقاومت قرار گرفت.
🔸
۳. هم‌اکنون کل ساحل غربی یمن تحت کنترل مقاومت است و مناطق تصرف‌شدهٔ ۲۴ ساعت گذشته به بیش از ۴۵۰۰ کیلومتر مربع رسیده است.
🔸
۴. شمار زیادی از مزدوران وابسته به عربستان به ویژه نیروهای طارق عفاش به هلاکت رسیده، اسیر شده یا متفرق شده‌اند.
🔸
۵. تنها از ظهر امروز تاکنون عربستان بيش از ۸۰ حملهٔ هوایی به مواضع انصارالله داشته است.
🔸
۶. مسیرهای کشتیرانی به‌طور کامل مسدود شده و قیمت جهانی نفت به‌شدت روندی صعودی گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/461309" target="_blank">📅 22:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461308">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی و وزیر خارجۀ عربستان
🔹
عراقچی در تماس تلفنی با وزیر خارجۀ عربستان، دربارۀ آخرین تحولات منطقه گفت‌وگو کرد.
🔹
دو طرف با اشاره به تشدید تنش‌ها و افزایش ناامنی در منطقه، بر ادامه همکاری‌های دیپلماتیک برای جلوگیری از گسترش تنش‌ها و بازگشت…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/461308" target="_blank">📅 22:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461307">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تلگراف: ایران برای نخستین بار موشک مجهز به حسگرهای اپتیکی را سمت ناوهای آمریکایی شلیک کرد
🔹
مقام‌های آمریکایی مدعی شده‌اند ایران روز چهارشنبه برای نخستین بار از موشک‌های جدید مجهز به
حسگرهای اپتیکی
در تلاش برای حمله به ناوهای جنگی آمریکا استفاده کرده است.
🔹
سپاه پاسداران در جریان حملات شبانه، موجی از حملات را علیه نیروهای آمریکایی در اردن و ۱۰ فروند شناور آمریکایی در نزدیکی تنگه هرمز انجام داد.
🔹
موشک‌های مجهز به
جستجوگرهای اپتیکی
با بهره‌گیری از دوربین‌ها و حسگرهای نوری، اهداف را با دقت بالا شناسایی و ردیابی کرده و به سمت آنها هدایت می‌شوند.
🔹
ایران اواخر سال گذشته میلادی از سامانه موشکی جدید خود رونمایی کرده و آن را
قاسم بصیر
نامیده بود؛ نوعی موشک بالستیک میان‌برد که به حسگرهای اپتیکی مجهز است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/461307" target="_blank">📅 22:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461306">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a8860a2f.mp4?token=AjjeyA4NOOWcnbjRQQCLOPtskCf3FEftenaILrsp9dHmcpMxLpvh8Za9Yphdihd1bQ-CYx0bHAad1_GTWKIUiPaFDsW-yA6XDDeCfdV1RK5FhJHDFvaLBf0QoGtxr1jJX6pNY3iHH_1iOy6gmBFicubW_OF7ryIXjnz8VyO794Qgm_Avl-Q0uAssB3xOE2XiCvG-C4cu9b3T9Ryskj_FgYhbAzaDw--PjNcOSmpOW4-JKwptHwfHwOwzhoXgNlsjU16E_Pq9oRqBu5V8jTcbYpPvg0oH9U8Bhc7g79AQdZmnAJMDC79qayfyWBZmaq78_oQyh_MOQo2mni6MRlaujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a8860a2f.mp4?token=AjjeyA4NOOWcnbjRQQCLOPtskCf3FEftenaILrsp9dHmcpMxLpvh8Za9Yphdihd1bQ-CYx0bHAad1_GTWKIUiPaFDsW-yA6XDDeCfdV1RK5FhJHDFvaLBf0QoGtxr1jJX6pNY3iHH_1iOy6gmBFicubW_OF7ryIXjnz8VyO794Qgm_Avl-Q0uAssB3xOE2XiCvG-C4cu9b3T9Ryskj_FgYhbAzaDw--PjNcOSmpOW4-JKwptHwfHwOwzhoXgNlsjU16E_Pq9oRqBu5V8jTcbYpPvg0oH9U8Bhc7g79AQdZmnAJMDC79qayfyWBZmaq78_oQyh_MOQo2mni6MRlaujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشای لغو عملیات ویژۀ آمریکا، در نتیجۀ حملات ایران به پایگاه مهمش در اردن  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/461306" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461305">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
ویدیویی دیگر از انفجار در ارتفاعات علی‌الطاهر لبنان
🔸
شبکۀ ۱۲ رژیم صهیونیستی: بیش از ۱۱۰۰ تُن مواد منفجره برای انفجار تونل‌های ارتفاعات «علی‌الطاهر» استفاده شده است. @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/461305" target="_blank">📅 22:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461304">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی و وزیر خارجۀ عربستان
🔹
عراقچی در تماس تلفنی با وزیر خارجۀ عربستان، دربارۀ آخرین تحولات منطقه گفت‌وگو کرد.
🔹
دو طرف با اشاره به تشدید تنش‌ها و افزایش ناامنی در منطقه، بر ادامه همکاری‌های دیپلماتیک برای جلوگیری از گسترش تنش‌ها و بازگشت ثبات و امنیت به منطقه تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/461304" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461303">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
حجت‌الاسلام رفیعی: تجمعات شبانه تا زمانی که رهبر انقلاب لازم بدانند، ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461303" target="_blank">📅 22:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461302">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb40d1f9c.mp4?token=MtLlihL0nS6oI0SkrzlpojQub8HklfrOJl3y1zawp6DKUdR3dB_xr8sJ8ZBJB5W-MPi8p9LyY0rH8ERzdggUnu32WF7TnM6ZRDQBw_nE-l5t4Ni9JdUCHjHqEG-m4njG9lFz28BrjSXJk7m23lA3r_MRyAiMcnSENaaf1gvECpZM2zVSGodgiLnCVSRoG5A6uBETzedxM8E8HIxShLU515-iCtw8nf4IAU5XGaky0KPU-Gz5wEnaaT92S7KC_PkY2xDgs-aHrSBu3-BfIMF_0iWabDET0sqyswkGQkY09DrO6SqtQEZ3cFL3DbuVK7MzihABSd55dLoiwaYBtzo3kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb40d1f9c.mp4?token=MtLlihL0nS6oI0SkrzlpojQub8HklfrOJl3y1zawp6DKUdR3dB_xr8sJ8ZBJB5W-MPi8p9LyY0rH8ERzdggUnu32WF7TnM6ZRDQBw_nE-l5t4Ni9JdUCHjHqEG-m4njG9lFz28BrjSXJk7m23lA3r_MRyAiMcnSENaaf1gvECpZM2zVSGodgiLnCVSRoG5A6uBETzedxM8E8HIxShLU515-iCtw8nf4IAU5XGaky0KPU-Gz5wEnaaT92S7KC_PkY2xDgs-aHrSBu3-BfIMF_0iWabDET0sqyswkGQkY09DrO6SqtQEZ3cFL3DbuVK7MzihABSd55dLoiwaYBtzo3kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارتش رژیم صهیونیستی: دقایقی پیش زیرساخت‌های زیرزمینی حزب‌الله در ارتفاعات علی‌الطاهر منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461302" target="_blank">📅 22:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461301">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrFh4WQ-rUm6lxJ47puYyUCIKoSk8Tr-YmojSqPs5TuK_rsxevc62PIX1yqjjgwJ6tsy9yTv0X0f81iJexk1mww86Ls0NepM8OXI6Y0JJu_6O7fKsYOxkWqU4cYn0kzrP-7iiqI9OTMcpU_ZsW5Rqwm2zlgHLTXFG3HBFM3UYJBx2bmHan5t1wkOvs96_GHzNlVQYfVkuOcTQJr_Zxfjl4TB2uIwopb-l71ufcpR6DTXmGAZSOm7gnm_LcSHol1XJ6n79wfJU-r6EnzkVQ3H1hllJ8DOpJA_TSYPWyTDwr-FBB16EeIt1HFzVkQbO9cbV9pL2o2ef-jMosHjQWvecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلط کامل رزمندگان یمنی بر ساحل غربی؛ پایان درگیری‌ها
🔹
دولت صنعاء از پایان درگیری‌ها در مناطق ساحلی استان تعز و تسلط کامل نیروهایش بر این مناطق خبر داد.
🔹
شورای عالی سیاسی یمن اعلام کرد درگیری‌ها پس از بیرون‌راندن نیروهای وابسته به ائتلاف سعودی متوقف شده…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/461301" target="_blank">📅 22:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49180b3a49.mp4?token=hCWR2aWrS9oNHybxClg-9XExzAz4ELDKu7u3UNWez77gxN1sBcPwufNgsrWdACpBTkuN8WOnuUVygtJSKv-X_ZssPodno8M9uug6KthsaEP-4k5TiQfbs-gD0roURyeCqf-nRqdJ1-S6EBwU__JJcHRYVLG31YNR6XOKNG_iFHHy0W2DXpYQMkWPGpjkl4I13cRD57wwPdVZcRtQ9cpKcLrddqW_G5yejwmQnSyZomGSWWKI6j3TOyNNRFPCVMnOFPY_mcl79wyLLs2NNL2hRFjUFUfRG4pV9y9v9eiq2vKHFiZ0zjc7qcVBlfAO0QcX4YlL0ZMKhV_5D63KBuOM7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49180b3a49.mp4?token=hCWR2aWrS9oNHybxClg-9XExzAz4ELDKu7u3UNWez77gxN1sBcPwufNgsrWdACpBTkuN8WOnuUVygtJSKv-X_ZssPodno8M9uug6KthsaEP-4k5TiQfbs-gD0roURyeCqf-nRqdJ1-S6EBwU__JJcHRYVLG31YNR6XOKNG_iFHHy0W2DXpYQMkWPGpjkl4I13cRD57wwPdVZcRtQ9cpKcLrddqW_G5yejwmQnSyZomGSWWKI6j3TOyNNRFPCVMnOFPY_mcl79wyLLs2NNL2hRFjUFUfRG4pV9y9v9eiq2vKHFiZ0zjc7qcVBlfAO0QcX4YlL0ZMKhV_5D63KBuOM7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار در ارتفاعات علی‌الطاهر در جنوب لبنان  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/461297" target="_blank">📅 21:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34f3671584.mp4?token=jRWXmgbUxrU4WPKtruyowwYFg5FoGRPQSljJGzCmHA1WIZk4M3Alx4izGSNngBlGChYHcWe9hGcA6vpl-nULdotQw54qN62ouUCBaON7bDJ5ilULrjKNHpkfj2b5Tzq3Q2xzlhDNsrKLDxN_vSymUHmHfvOku0JyplsoxyViszxB-RLfAqaOdERH-YNQffAACuWDYcsAUtorLg_ixdk56CDrxmkv20lhuCci7NGSwA_W2lJST1rkpqS8N5ha0NGI4CTZczqbi8oag7LPkFmsIdsr9bhthwGFPxb4LbLQBDyD-yHhrR3BE6yxp0xl6Y9H9n0VLwID-AezBCgi2OlLng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34f3671584.mp4?token=jRWXmgbUxrU4WPKtruyowwYFg5FoGRPQSljJGzCmHA1WIZk4M3Alx4izGSNngBlGChYHcWe9hGcA6vpl-nULdotQw54qN62ouUCBaON7bDJ5ilULrjKNHpkfj2b5Tzq3Q2xzlhDNsrKLDxN_vSymUHmHfvOku0JyplsoxyViszxB-RLfAqaOdERH-YNQffAACuWDYcsAUtorLg_ixdk56CDrxmkv20lhuCci7NGSwA_W2lJST1rkpqS8N5ha0NGI4CTZczqbi8oag7LPkFmsIdsr9bhthwGFPxb4LbLQBDyD-yHhrR3BE6yxp0xl6Y9H9n0VLwID-AezBCgi2OlLng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سازمان رادیو و تلویزیون رژیم صهیونیستی: ارتش اسرائیل امشب تونل‌ها و زیرساخت‌های موجود در ارتفاعات «علی‌الطاهر» در جنوب لبنان را منفجر خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461296" target="_blank">📅 21:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حملۀ هوایی صهیونیست‌ها به علی‌الطاهر با وجود ادعای تسلط بر آن
🔹
الجزیره: جنگنده‌های رژیم صهیونیستی شهرک المنصوری و ارتفاعات منطقه علی‌الطاهر در جنوب لبنان را بمباران کردند.
🔹
بمباران ارتفاعات علی الطاهر در حالی است که رژیم صهیونیستی روز پنجشنبه گذشته مدعی…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/461295" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72408cebae.mp4?token=K00hhllyr6tmIyiLNpvyLRtjQNVxQHGK5kMUzGfGMUlQF9TAUMF6nmgm_RyDaRS9erLmRubvHr-k9fCbqzq2d9Dd0QdIfz6ojVOZfo1JM-D4EeBfw70QpbSd_anpnzpp9y3UGlyDXz9Ytm3qAfv5kf5lweRYovVZIQSkZ9sSClxpw6Im9ZzQuUZj7SZ7TVv_wWjGIaZX0FR1YZrsbHuqsyv_cS7R-4SJCLMgTX6d4GEMQrdTivyvn6NWH08KCHWRH01LjPJX10Q0HBNFjs04HLhLWRCQvX671fUqmf-uMkXqR-OeqqvF4no84hLI1Rtug40f-8J6cJmGZWSrhiOFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72408cebae.mp4?token=K00hhllyr6tmIyiLNpvyLRtjQNVxQHGK5kMUzGfGMUlQF9TAUMF6nmgm_RyDaRS9erLmRubvHr-k9fCbqzq2d9Dd0QdIfz6ojVOZfo1JM-D4EeBfw70QpbSd_anpnzpp9y3UGlyDXz9Ytm3qAfv5kf5lweRYovVZIQSkZ9sSClxpw6Im9ZzQuUZj7SZ7TVv_wWjGIaZX0FR1YZrsbHuqsyv_cS7R-4SJCLMgTX6d4GEMQrdTivyvn6NWH08KCHWRH01LjPJX10Q0HBNFjs04HLhLWRCQvX671fUqmf-uMkXqR-OeqqvF4no84hLI1Rtug40f-8J6cJmGZWSrhiOFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلیپی از صحبت‌های شنیدنی رهبر انصارالله، همزمان با پیروزی‌ها و پیش‌روی نیروهای یمنی
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/461294" target="_blank">📅 21:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdd560g2TO8SdsAPM3KZvLj9syHtuWvmQdBzQRjzWi_Od0rh5iPLSugNNMCOx1Xj4whXArQbbBo0704oLxIYtGDFnPajOQr0Oa3cCWt-qFIqoKP5ooQ6h668EmoyPQo7f2MTwv2FCgvv9WNgxW2_6D7qPjZ2X7VDw9j6pn-6jz860IoczrrIcdhi8yi2dqJqez-Qmb-zNNmWw4aOn2UoE3wwGmWUkwe3q8Q-Ymc5w_TfhFA1A25HokqEuxCNVjvvEF8kHtY9SqNnjQ_q1CpVSQGIOxUVwPxrfxBt3c7eML9h9YHNyG5pFeQK6ixcwrPbwANiHHEUkLsY3KnYJOeelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان فردا به هند سفر می‌کند
🔹
رئیس‌جمهور، فردا برای شرکت در هجدهمین نشست سران کشورهای عضو بریکس به دهلی‌نو سفر می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/461293" target="_blank">📅 21:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIIpiuJOEVIwG9m6TnNPD5T4u7ZtH_kbaB5t6kb_SKYeOkPbYIsc034Th2wgxwxb7GKnxZAqSO2V9mDegQZOc6dSJOOY2IWVrdYyzd-7H4I0TwycZWgqNWzstzyytAwvS7ZazcJ7qajI314vZQC2ZJVpKMbhL5tldtOzgzSQfhnb3KRhylma0hNaGDa_uiemPPmta4eGjyVyqSK09vl6lUk4kGSaE_oQCH7vVFOOT3H9bRpDi7-wAWbJtC7_kcte4Hh0L75v0WNIOTNeOHVPgaLlI5k7gG64gbs1puUeRShje_R9nGnRih7iP-RWNMFef_QmhL_a89Mahs3kfzLyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آژانس پروندۀ هسته‌ای ایران را به شورای امنیت ارجاع داد
🔹
رویترز به‌نقل از دیپلمات‌ها خبر داد که شورای حکام آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به بهانه آن چیزی که نقض تعهدات توصیف کرده، به شورای امنیت سازمان ملل ارجاع داده است.
🔹
این قطعنامه…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/461292" target="_blank">📅 21:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b528dfc40.mp4?token=E7Jft9UoUcYhqVRBjt_kvH2DS3rGkf3Hn0xPq1ssoyAnZ0buWvWvmpTB-G-52sn6GqmB1YwN8oi8yx35L0gMIdfH-afd0tOCTBPuaPkpxWBgztkV9z9VBDMBWwkKAYl_vwdQ0HOi9yddqzL7f6uEqSgryWHzVhFgNDSA6-Tk2wu9QBoLwDQyYU6qNHOuBoXHYySeO4wvvMnxbhAwGY_F2c7ek6ghD9RoB8ZaAgpzWGu9KRqLTuLiGDWDLfw-1RL1ugbUutZ-sM-GUQNJFRpGh-lEx5T_PFX682KyE9a6QNFTTerte8t3Eb_6POebBayJwj-UswRvX7WfAMijRRCaHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b528dfc40.mp4?token=E7Jft9UoUcYhqVRBjt_kvH2DS3rGkf3Hn0xPq1ssoyAnZ0buWvWvmpTB-G-52sn6GqmB1YwN8oi8yx35L0gMIdfH-afd0tOCTBPuaPkpxWBgztkV9z9VBDMBWwkKAYl_vwdQ0HOi9yddqzL7f6uEqSgryWHzVhFgNDSA6-Tk2wu9QBoLwDQyYU6qNHOuBoXHYySeO4wvvMnxbhAwGY_F2c7ek6ghD9RoB8ZaAgpzWGu9KRqLTuLiGDWDLfw-1RL1ugbUutZ-sM-GUQNJFRpGh-lEx5T_PFX682KyE9a6QNFTTerte8t3Eb_6POebBayJwj-UswRvX7WfAMijRRCaHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فروشگاهی که قیمت برنج بسته‌بندی‌شده را دستکاری می‌کرد، جریمه شد
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461291" target="_blank">📅 21:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757a9d4ea.mp4?token=aGOci-ATxw4gSTnXnypEFWEmv8fVKbz1LifcsJOE3R9uuj-TIY2YD2htwJhKT3-zfPpqLtuhN8kiPmxuxs89DWkKLnUmbebwb0L4_MVGCxzDUibJsi0BEnLYD9dh9fJisInlt4KWRvn8Ving2P9YbNdY5PL21_Fyfitrv8_3bIaKKguOJMvvQ0vBKz0KbTZc1pwBSJSWPeSWelcVY2Yyp2DHk7ZrzczWhaenq4tQyrnN0OgO_Ux8vEVXZtAOWGoz2RlVFXE8bY7NbmEXkS0VJewilqcrfIx4oH-KOh1fCQhf2sTb4yKFX84s-1YJ5wbT_OKyUMZvl1bnzNoXAf9m4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757a9d4ea.mp4?token=aGOci-ATxw4gSTnXnypEFWEmv8fVKbz1LifcsJOE3R9uuj-TIY2YD2htwJhKT3-zfPpqLtuhN8kiPmxuxs89DWkKLnUmbebwb0L4_MVGCxzDUibJsi0BEnLYD9dh9fJisInlt4KWRvn8Ving2P9YbNdY5PL21_Fyfitrv8_3bIaKKguOJMvvQ0vBKz0KbTZc1pwBSJSWPeSWelcVY2Yyp2DHk7ZrzczWhaenq4tQyrnN0OgO_Ux8vEVXZtAOWGoz2RlVFXE8bY7NbmEXkS0VJewilqcrfIx4oH-KOh1fCQhf2sTb4yKFX84s-1YJ5wbT_OKyUMZvl1bnzNoXAf9m4IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر بقایای پهپاد «کاریال» ارتش سعودی که در استان حجهٔ یمن سرنگون شد
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461290" target="_blank">📅 21:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja7Sv9S1ksrBAWDxnOFw_S5v5kYi9cx5pDTkEaUsRq_yDOCVWQK507Sq32WCGnGY4UNcxZyfT_dx-a5pOfwwJq2YnFuiFqW4qaBa4AT0wdKifzHqVpTWR8Wt2uNSnjfqSL20GaQc6n1qRuhFOX4hToGqoGkcsuwR2CvLKEpoypbcGxUKJPoQlS25tVTC72vUGeXDeFcmq4w-40e-cDeo87aACu1sFEK7Q2Ty_WnHWuoR_qdB0GDrHUAm3XPSohonSZkheaC3VJM98JeWKxtPlyh6TFNhTGYfyAKSd_GQqLf2EO00a2hH7u8e5j_UN4q8NwqP3R-PCrnmFm-JgtjyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفت به ۱۰۵ دلار رسید  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461289" target="_blank">📅 21:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۰.pdf</div>
  <div class="tg-doc-extra">3.7 MB</div>
</div>
<a href="https://t.me/farsna/461288" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۹.pdf</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461288" target="_blank">📅 21:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ_NHaKl6EmNkzdbrB-TlC7ro-t-9tIkV8fx7I8a6_ZlOgcQ3918QdNzY6-62U8IKhi1MmzFVmz5u9-VavVHVUmBOQ-Z2YBNFQbzGYtq2Ey2ftA8S8aQkw38e2slaFL8S1YZW2BHItPrJS2e89L5P7yRObnHKiTF6NxLOC608JdnF2SWM-f2kAnPun9LLrAibf7vlGHfuJI1uz3iWjgWx5gQj-YZSq3F3SyxuMsl1vzcsgXeOpKUZ_X96sD3UX_NgBXtqaPtbPEs6WwTD57DeDcBf-hWMZf4-g3EYiyT5K64FPYZ3Pa9K2sGfu4zeBUXDP6SnCP1ecBiQz0RQVqrKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آسانی از روی نقطهٔ پنالتی استقلال را پیش انداخت
⚽️
استقلال ۱ - ۰ پیکان @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/461287" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
انهدام شمپاد آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه اعلام کرد یک فروند شناور سطحی بدون‌سرنشین آمریکایی از نوع Saildrone Explorer را در ورودی تنگۀ هرمز هدف قرار داده است.
🔹
این شناور با شمارۀ بدنه ۵۸۳۸ در حال انجام مأموریت در تنگۀ هرمز بود که هدف قرار…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461286" target="_blank">📅 20:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461284">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bb18e21a.mp4?token=eHa-v3LV5uUutvFyfJDiN4C51VTeyn8qpHEY34lpxtbE5XqxdiwUGjTDsO372QtrRxE_FPmTGbPKtgAYjdzt0d711-sAyIw2FLz9XKz1kXAGd27iin8_NvB1bOBnvGhBB82qALaaqon98OfFJHnG-jJZFEc9_405JlE_14bTyw5IoLJ_k1BqznfjGbQkNrB9v2KwJI0Ss7W4vqJ4CoBp6K7yZcfy66nmMUY-FPA6JylVeAhOvUQlYIRL3t6X31t7icYiHH_G2JStVb6lx-M2j1nVO7mq6MfKtOqxLKmcydLqqI6PuKNhYEjT0kcWnpWBNXwT1G3bdZFhXHTsMPPiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bb18e21a.mp4?token=eHa-v3LV5uUutvFyfJDiN4C51VTeyn8qpHEY34lpxtbE5XqxdiwUGjTDsO372QtrRxE_FPmTGbPKtgAYjdzt0d711-sAyIw2FLz9XKz1kXAGd27iin8_NvB1bOBnvGhBB82qALaaqon98OfFJHnG-jJZFEc9_405JlE_14bTyw5IoLJ_k1BqznfjGbQkNrB9v2KwJI0Ss7W4vqJ4CoBp6K7yZcfy66nmMUY-FPA6JylVeAhOvUQlYIRL3t6X31t7icYiHH_G2JStVb6lx-M2j1nVO7mq6MfKtOqxLKmcydLqqI6PuKNhYEjT0kcWnpWBNXwT1G3bdZFhXHTsMPPiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داور در دقیقهٔ ۷۵ با کمک بازبینی تصویر برای استقلال پنالتی گرفت  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461284" target="_blank">📅 20:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461283">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875cdcd8c8.mp4?token=kuDe74L0TyoKXHTdqcI74Pzx7uqJnpgzpeCAzvWcFMBRzmd7_sFzkWVduhXTNPPdFkKishPpYtOqlE26ePzWGLY6atRHceRPZ1QbKkHn4lOSgxILmfmF17tQ7G0ioyAqiHVza8SZ8Suwg8oQ5M8ppXxwWGUE3t55YN2RJrNtZ46TC8kAF2aQ6LPnj0BE5rpESWvFP-q132nIM-AOCO0OsEDS5IXA9MfmFRx6q0TRkv89leQHvd5ItdMtc4NkVAn-3s5y8UW5_erBRkh3ZNl4Q9V51OF-UPHXl-sRfAlFiRrn5k8SGT7KR9rzmINEUnpuLkRDh1IhtJgWJTBR39cULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875cdcd8c8.mp4?token=kuDe74L0TyoKXHTdqcI74Pzx7uqJnpgzpeCAzvWcFMBRzmd7_sFzkWVduhXTNPPdFkKishPpYtOqlE26ePzWGLY6atRHceRPZ1QbKkHn4lOSgxILmfmF17tQ7G0ioyAqiHVza8SZ8Suwg8oQ5M8ppXxwWGUE3t55YN2RJrNtZ46TC8kAF2aQ6LPnj0BE5rpESWvFP-q132nIM-AOCO0OsEDS5IXA9MfmFRx6q0TRkv89leQHvd5ItdMtc4NkVAn-3s5y8UW5_erBRkh3ZNl4Q9V51OF-UPHXl-sRfAlFiRrn5k8SGT7KR9rzmINEUnpuLkRDh1IhtJgWJTBR39cULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داور در دقیقهٔ ۷۵ با کمک بازبینی تصویر برای استقلال پنالتی گرفت
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461283" target="_blank">📅 20:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461282">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4211c2eb26.mp4?token=ttW7VEEOWOU7QOXtFTA_XVxfJ2gfZP9kDcC2YEGcwlJl4a94dK10bJdDNu68JxtAu3pzg9L9aOhGDY8u_3J_LZtTSDHGsnUi5QlYShTxNpVVE4F_8ppptwa6cHC5iCNi8CMnIRD-j3vOUlVGOKyRSL8WGrw6RxeWNWphZUV6_zIlJnr6LblUw1LoNDZLPaLwZHIy_prh9mReIfmFwcBHbpCxYl0nCWFyNvF02Z0htGtOqxCqrJ13PLDfXLXpWk2pBqZ1qBhVKPdUZgdWNEwr3kvm_8D3_SlB0jwW8ZYBUyWH_f1V5Ec9XftCUQFWxR5QxY1Dtlpq4r3Pl2jLTKpksg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4211c2eb26.mp4?token=ttW7VEEOWOU7QOXtFTA_XVxfJ2gfZP9kDcC2YEGcwlJl4a94dK10bJdDNu68JxtAu3pzg9L9aOhGDY8u_3J_LZtTSDHGsnUi5QlYShTxNpVVE4F_8ppptwa6cHC5iCNi8CMnIRD-j3vOUlVGOKyRSL8WGrw6RxeWNWphZUV6_zIlJnr6LblUw1LoNDZLPaLwZHIy_prh9mReIfmFwcBHbpCxYl0nCWFyNvF02Z0htGtOqxCqrJ13PLDfXLXpWk2pBqZ1qBhVKPdUZgdWNEwr3kvm_8D3_SlB0jwW8ZYBUyWH_f1V5Ec9XftCUQFWxR5QxY1Dtlpq4r3Pl2jLTKpksg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انهدام شمپاد آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه اعلام کرد یک فروند شناور سطحی بدون‌سرنشین آمریکایی از نوع
Saildrone Explorer
را در ورودی تنگۀ هرمز هدف قرار داده است.
🔹
این شناور با شمارۀ بدنه ۵۸۳۸ در حال انجام مأموریت در تنگۀ هرمز بود که هدف قرار گرفت.
🔹
نیروی دریایی سپاه تأکید کرد تنگۀ هرمز مسدود است و تحت کنترل و اشراف اطلاعاتی این نیرو قرار دارد و هرگونه حضور خصمانه در این منطقه هدف قرار خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/461282" target="_blank">📅 20:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461281">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌ روسیه برگزاری نشست شورای امنیت با موضوع ایران را محکوم کرد
🔹
نماینده روسیه در سازمان ملل: نشست امروز شورای امنیت یک جلسهٔ توجیهی بر سر موضوعی است که به پایان رسیده و وجود ندارد.
🔹
چین، روسیه و ایران معتقدند که با فعال‌نشدن اسنپ‌بک تا تاریخ ۲۶ مهر ۱۴۰۴ شورا…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461281" target="_blank">📅 20:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461280">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🖼
واکنش معاون وزیر خارجه به تصویب قطعنامۀ ضدایرانی: در شورای امنیت هم نمی‌توانید کاری از پیش ببرید
🔹
غریب‌آبادی: به تأسیسات هسته‌ای تحت پادمان ایران حمله می‌کنند، روند عادی راستی‌آزمایی را مختل می‌کنند و بعد همان اختلال را دستاویز صدور قطعنامه در شورای حکام…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461280" target="_blank">📅 20:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUmUU4e3GXYyM0m9C19BkPjXtlOV2L3us4XValc6uQXB58lRznV9CSWtccUdLXkUUyOhswZ2mNgl-5pGt2CznsfQ0YpGttXP5gQohiHAmBhwqt9tDyVsy7j2NU6NBApaWiviu5oMd-zR4PISpJoaDHkWazy8t9ncKjYfGohaPc7YybZPcHb-v1IfANcrkx49FN31ltWMmSgxL5LVwpsMnvesuKX1U7lwU_GwJTllUeibN_3Zm9L-Lmy2_3kmArDos2mDkvS8G358wqpHe4wmmbvC2gkSowhenyJxlbH-dPtvQVcWeDc6thnnEqjZ9VCG61OGMni7Lr2qTLe0hPkQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBXKx3kdj4S5YF5A8K7IuAJ1w64klpltJ9SGLOtKDc-_BOYHHCI5SQwiuNxS6MTxe1HF5fB1f1hneAEGDX45dUTNMzwVJLi01YvYMrPd6BKLMhTfEcpiA23Hgr6F6GB4sswTZqG1CWj2azP8VCIeK1LEF7GOhE0UNSwf460GeGChnNlYAjg_cymkk3TFjGM3rz7FjaondaOFcSHBaZc1gvih3NeUKPk2yh8vnnqzhJHNpC8NpcbvCrDYXUZWONZZ-yIFHy8T-LnyK3r3A3RSiAfTAXGW7Shcywn9edx1xNSiqcjnrxSwR2B2dT2_rTs08n8UDRG-LnxgMObGpGtyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_QIj9XpWaw8kXlpVJGczDPMxR2R9v2jjWs99q2hUk-joh9RY3-BaUtUICdZs3hDxeQsTE6Ph8YGujhY723Uh1x7dVsaT8nHC3uUV_2mYQhGXUl-muX2TT381DHfPDCNhui7gc0bSrK6kJfsyIICLTYvilosu7FYexrESqKK1q5YWgAGzBH9TugSd57J5dlu0REa-MDWYhDso0W7hr7MdZZ_V850VwBuPjzM6qqkrWYTUQss1gQcoJi9bEARb1gxyceXI-Cmt9C3PzlLZ5uoZFKX3Fw9aLpQfwg15FFeYZGXxQArXg2_JenmLKLFu1UZNcvso9ESmbeJ3XUwjOz0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaCVLXbozmYv5b6XrHNobJ-_XPZ-LCPX2KtlJYsS3TbK1nkflr89rXny-6sGZC-MgDILprLIAo76fYxMai9G10EquPCVJBpQFz8hDUQoGjfqlyJ6OXfW2KC5FzeeRQHZtoTHgNNQyM1PnHi3h02KiYXyWPw9WTHzwn1sF_iOjgsS9-FLU9gVOF_5IpVcP4Zd8CcD3juJJfesVGYeCiLD7iqbUt2WCXMTpEjSh8eUHzf31bWM0WkLPmTBIfPTob4QUPnT6NaTHezlT4JpDpZsCxs-RXA07_caihbarTaLbZRPFd0KhKq2IhQTP7uQ4JlhKa5TUie01VNiesEij3tHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7foWEBEg_oH0Lz_uZ6seFWgV7ktEfAtLy21-dChBL2A94aueX7u48XXUhXdqbz4Qror9pc_mcmfIDeDZz7bPrls2XmWpUDr_OfANPbThghbCbCBDp67sLYgI51idQp0HwYeEKjOrf-bmxCr6r4igg-TDY6I8CqM3LuRWgld1TEsGL8PaZ9KnQTX7FRsZiJz0wM7ZbzYxE5xuRvTN1XCEVyDl3Z4Kp-AFnzbKpbtG421VG-LQ5TUnCkm43rjHKxwUZIaraPhDiyfJ17nyJdvxI9JxHIg7z-bCxBJ4ttJXUJS-ewjzDTRUepvrTcSi4II8_qqM78HnmVxpoYapGw4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFZ5OwrBn6EZvkWmNjyXZLZ-1eN8CIrRGD2wwu8jvu0ZY4q5HtZMW_3MOnX8uQzYgxU3AvNWNKQT1I3owqkBHGWTGmsssci_ZYhlbdGaAGkPPBwaDXUrKhrq4T0Erz7-2sa9TXo0NqrMEoi5l-2s3UcHA9kgLE_nz1301P4AOxTpPzDqz38CcckCmmfZKv_JNSoLLxP9CV7B6A3hjCNloIlg7JGmpmH2RPzxLLzFE8kDaaIdyDYCJPul2wigYWPkqg1ysMCAoJw_i77xM0PEAafVsCCbx2UI0Gg8kdx6zkHs3fHAvUrCE0RbcgVfS01hwrZM_MgLDe8XqJcL-VvV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWYYqpmIA-9qNFm-VZFgdAjZxGgYKGvfUFbBlezquLMC8M3Y6gIVCHOlaDHDsfNYsESreykulfdNjL5tK8FVJFVWElzQ19QsRh_tseXask7yqzt-BbDL5T8p29UpcRy_Z9rezLdnB4-jIO1YgD0wSVxxcfsVPpdC29xiLJNOO33vYw-l48iyFWg_xuDLU5QWq_xzc7SrLoyV8m4vy3dSxE-7RygdV-ZHKcoxjaFfFNtLcWNymqWr935fFsbkoXNJM-XuQbGgiZN7JgyHYEYDhW_f31asqOURKYleAjA5mLhLHl9xWtk65Mzll4Vie3QOLSI2hArYBBttUdIgTGU50Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خدمت‌رسانی جهادگران در روستاهای همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461273" target="_blank">📅 19:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461269">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8Qr-xkuUD9dpTrg9O8uRpcca026r2EYfQ6Hr94gIUee3I1fo4BFz-f9SEazRv97kY1xPBomJicDF89d9J0PAzRle8JuCna0YlnauWNmnHD_tskkeqJhiK8ldPXsUESfZ2Ttmybz6L9Dih-jD9xbB1Yj1g0Qr-XnaAhUnJsclTovyj8rsmMG8gt9pbbL9A_BLEp6QN-yQqP4K_A_gxCQ0fEZsjhMrtmsQXpEEi1zn0EeAFQ0wPj1rir5tmfOlXiWpQJmbh9vMRXxddLcevC5InWSAYJWwhOVLtypmHvVRnUSoLPvVoBfRToX1EG43jafpTeVs7eTFLIfwOYoNvFRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6YNZ8Klqo3xSQL94WuMaHkDwxjRRSxNEukUiZkbfYSU1SMESQyX-31tC_1_p1eBpQhSJfKx_d1ZCxv82fXq51o2SX3H1C2E06WKftJRnrPQU3JiuyhdOrVUnm6PF0Acvqb0A57cpk-I6DuJhbodMeVVhfPYXMA-UimYb6NfWACrfGNW1QSWI-MuTxyIS8jOwhbWJ-l9KLLjwcs43Ap5kizSn6LWcuXgZI2H-W7pJOwlfhS0kJYGtXBe2DoUOaSUhW-MSZG-LeJTsRvcpxyjCOzt_mrE0yENqTY5SKFsLVWrFOiXQRFd2W9n4YJ5av7J6DXMzvf0RUdKVnpGxBxSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odPmVk3N27EHeAWm2cTedvbxIubXfh2yHuqw55Bs5J7o4lH6GFYLHodiMF6zvzw4SNG4q8stkQpt5gfGbmTMylsbsANSPcIGP-FMtmT3P3vuJS7m5mcgVnClRI7tSlj6UZdUxuQNGzFfgyAu-Mo8LtaM_l7z-2YrPrWqQrLv_R3MlWxKVfUdbsg0lOaT_Zz60yc8ddxwgu9lsVnXY5JkDckNk8aDrpwY9GZGrTKROZGF_HHDjaL0_9_5jUOYGpkahYvrv6802XlhnrGWCpUtDIzLNZCkG0ZxjonTpxITjvrv6436Y0XGBizOenB7Olms7k0c_d-pAIF1DzyHc5p-sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda3959e3d.mp4?token=o6WXULQ1QoiZqUIqx6M9GXhPJJ48AAw5rKFvamZ89TN_-JqKDDeO58M1EPzMj3ab-FKGBaTGvwLIQieuUOGLrTTktu5ASAndVFZxYHV2PK8mUqg6u8yJMNSBOMo1iL91wBCcGmb7EsIrY9BpBSxjcrDtsrscqph3P7AYqBYoK_9vva7y5etZiju4xY5i-oVndRvqit9n4HDaS46Z0b7hFlH_RHwOfPx5siCatWhdpat7SWTx-93AMWbdCw-OTTdLGmsJkq0UFPYobsIJJHRvq8pI1ie25bWEQ2LEZ5uo4lqtvAk6wtLiAeZ5QD7UVTEREqtL-7MWCbY-KqckPuiVJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda3959e3d.mp4?token=o6WXULQ1QoiZqUIqx6M9GXhPJJ48AAw5rKFvamZ89TN_-JqKDDeO58M1EPzMj3ab-FKGBaTGvwLIQieuUOGLrTTktu5ASAndVFZxYHV2PK8mUqg6u8yJMNSBOMo1iL91wBCcGmb7EsIrY9BpBSxjcrDtsrscqph3P7AYqBYoK_9vva7y5etZiju4xY5i-oVndRvqit9n4HDaS46Z0b7hFlH_RHwOfPx5siCatWhdpat7SWTx-93AMWbdCw-OTTdLGmsJkq0UFPYobsIJJHRvq8pI1ie25bWEQ2LEZ5uo4lqtvAk6wtLiAeZ5QD7UVTEREqtL-7MWCbY-KqckPuiVJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عیادت نمایندگان رهبر معظم انقلاب از سیدعلی موسوی‌گرمارودی، چهرهٔ ماندگار شعر و ادبیات
🔹
غلامعلی حدادعادل و حسین محمدی به‌نمایندگی از رهبر انقلاب با حضور در محل بستری سیدعلی موسوی گرمارودی، هنرمند انقلابی و چهرهٔ ماندگار شعر و ادبیات کشور، از او عیادت کردند.
🔹
در این دیدار، نمایندگان رهبر انقلاب ضمن ابلاغ سلام حضرت آیت‌الله خامنه‌ای، در جریان آخرین وضعیت درمانی این شاعر و ادیب برجسته قرار گرفتند و برای او آرزوی سلامتی و بهبودی کردند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461269" target="_blank">📅 19:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461268">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubk2kd7HGOYrkq9Hb_gV4OZLRwX2LCcWf1p4OtWyjTOduKMHAI5vI4mLufz0gUjcfkFFd0yHX4G26Zkv_uYXimE4sidjP6rhrxVYNpYeKJxow1qPwiMXKSBCu1W2AQ68aOF-XBRnLQ3Y2iwCNpgmhJQxYXQ5YInalmSaR9_0v6IpXNgaPT3LlNKMbEqRsorJ5XQ4_fCjnzuhtjCXNkUHgqm1oxF6qgRPU81iACTUpeya5TTPUr0fcp7scViZtbPs9s9HFlFWN704ia_7uTx03ztAocbGuOc4UvE1UWms2DnIOUMMXFPP7msSonHhIjEAT9zOnGexfW1jjSQYNLzYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: تحریم ابزار فشار است نه ابزار تعیین سرنوشت ایران
🔹
رئیس بانک مرکزی: آنچه تاکنون توسط امریکا انجام شده در کنار ایجاد برخی محدودیت‌های درآمدی و تجاری، تلاش برای تشدید انتظارات و تاثیرگذاری مقطعی بر فضای بازارها بوده است.
🔹
فشار اقتصادی یک سیاست نیست بلکه یک خطای محاسباتی است و هزینۀ محاسباتی آمریکایی‌ها را افزایش می‌دهد.
🔹
قول پرداخت ۵ هزار دلار به هر آمریکایی در صورت پیروزی جمهوری‌خواهان در انتخابات کنگره بخشی از همان هزینۀ خطای محاسباتی است.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461268" target="_blank">📅 19:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461267">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPwrxa0MkARRBwtdsHpUeZxHrw4QI8yCYOr7YhhIaJbHw47j-Ffm850bTf5M-5UNXD4T6vloGnzM0AsTBqhh15inCd45cuSqFRH25J4XxHeNrci4SH_F4Ql5o2RH9uJWXVWvtZ6l0hU2hFoX0XT9zSeDAKnEEVS72C14NauVDl0wpzoTbzYrEoBJ3DpoZ5MesjjK3Ysw3X1sRvseh36enXQqIFzeCJAngrTTwVQWRNnf14YpoUdI2JWiHUtHqGZmoFTP7x7AkmK3Z88Qn5eQPw6d6KidSa_lrpjuVmMKx6Ywgs7usJuNTo68660wBVsaXUBtvTqwrco7p-1SycSjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رزمندگان یمنی ۲ جزیره دیگر را آزاد کردند
🔹
رویترز به‌نقل از منابع دولت وابسته به ریاض نوشت که ارتش و انصارالله یمن بر ۲ جزیرهٔ «حنیش الکبری» و «حنیش الصغری» در نزدیکی باب‌المندب مسلط شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461267" target="_blank">📅 19:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461266">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۲ شگفتانۀ سپاه برای آمریکا در تنگۀ هرمز
🔹
در روزهای اخیر، نیروی دریایی سپاه با دو اقدام غافلگیرکننده، توانمندی خود در مقابله با نیروهای آمریکایی در منطقه را به نمایش گذاشت.
شکار زیرسطحی آمریکایی
🔸
سپاه در ورودی تنگه هرمز یک زیرسطحی هوشمند و بدون‌سرنشین آمریکایی به نام «Dive-LD» را به دام انداخت و آن را به سمت ساحل هدایت کرد.
🔸
سعدالله زارعی، کارشناس مسائل بین‌الملل، این عملیات را اقدامی چندوجهی و پیچیده توصیف می‌کند و می‌گوید: «این عملیات در واقع یک زنگ هشدار را برای ارتش آمریکا در دریا به صدا درآورد؛ چراکه نشان داد حتی شناورهای بزرگ‌تر و ناوچه‌های آمریکایی نیز می‌توانند در معرض اقدامات مشابه قرار بگیرند.»
پرواز بر فراز ناو آمریکایی و شلیک موشک‌های بارشی
🔸
زارعی می‌گوید: «اقدام دیگری که سپاه انجام داد و از جهاتی حیرت‌انگیز بود، پرواز در ارتفاع کم بر فراز ناو هواپیمابر آمریکایی و اجرای عملیات موشکی علیه آن بود. در این عملیات، یک موشک در بالای سر ناو آمریکایی قرار گرفت و سپس نزدیک به ۳۰ موشک از آن شلیک شد.
🔸
مجموعۀ این اقدامات این سؤال را برای آمریکایی‌ها ایجاد کرده که ایران چه شگفتانه‌ها و ظرفیت‌های دیگری برای مقابله با نیروهای نظامی آمریکا در منطقه در اختیار دارد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461266" target="_blank">📅 19:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461265">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8f02653.mp4?token=SCu2khOfLkITXVSGpXSYHf9qwt88eZmyjbL-jQQu-R3oT7aX975Ct8nGSKdPfpcV6m7OAwZalV7fTINt5wNn_YPQx4xyI0N_ButKGesIMkA9qu3q0VtRqDOK4NMjaAJISftpqbg-Gg5E3dTgW9OfJDbQam7ncqZeRUViCalKcwk0g-eZ5RiVxojx8OZEz_YfJgysOMrO4EK7-1nrJwIt8pJ1rBQ_DW-Ci0UiK5A7s3V2XMRvCf-0J7ALhQHcif6kskRquN09Bg4li4PlW_huyCRgg3qU3CyAMBxpYcymrp9kV3o38wWe9lFrUi1c5kiupAD3sWlnFFuGmkGl1RjNzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8f02653.mp4?token=SCu2khOfLkITXVSGpXSYHf9qwt88eZmyjbL-jQQu-R3oT7aX975Ct8nGSKdPfpcV6m7OAwZalV7fTINt5wNn_YPQx4xyI0N_ButKGesIMkA9qu3q0VtRqDOK4NMjaAJISftpqbg-Gg5E3dTgW9OfJDbQam7ncqZeRUViCalKcwk0g-eZ5RiVxojx8OZEz_YfJgysOMrO4EK7-1nrJwIt8pJ1rBQ_DW-Ci0UiK5A7s3V2XMRvCf-0J7ALhQHcif6kskRquN09Bg4li4PlW_huyCRgg3qU3CyAMBxpYcymrp9kV3o38wWe9lFrUi1c5kiupAD3sWlnFFuGmkGl1RjNzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
هواداران استقلال نام صالح حردانی را که همچنان با دستور سهراب بختیاری‌زاده دور از دیگر آبی‌پوشان است و اخراج شده صدا زدند.
@Sportfars</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461265" target="_blank">📅 18:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461264">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOSVpHn8r6VqpzfAvbXf5v__6RDab2jv91zUo88W9lShe1xgOHjYQaFhst5RpBitpseRx0Xybi6_Wjp2AguWXPt0zeVeakKqBfW7vVf0fQx5zX2ymTtbSh8RXRYAC1I_mqnoeSIQgvr_yjyBYvmooXxW9GyatMQeHhOMGsVWPTvJ2RYTJtuch_5zXehK1k_yD75d6TDcUM03PAJI7UcQ6iKUKcQyOVStYkGBbzd1mMhYnIXIx7H6YznQ1NuCzzUmqv0Igfv7NNhXBDwq2vL4yDvowzALxdq4OG-rWIDnv9MwAYQ1V7nzEpfQNMoOlzrq9gQ3CrkECY0yJWWKPgRm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل ناتو: مین‌روبی در تنگۀ هرمز به ما مربوط نمی‌شود
🔹
موضوع مین‌روبی در تنگه به قلمروی ناتو مربوط نمی‌شود. البته ما آنچه درحال وقوع است را زیر نظر داریم و کشورهای عضو ناتو از نزدیک با یکدیگر هماهنگ هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/461264" target="_blank">📅 18:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461263">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad94fd6de4.mp4?token=qYwNId56TRCiJNg4v8VSxAGfH4zcKntoGDOhx4S2Zwut9MJXGtGDo9NmFcN9xpN98fSsGSNmF8YUB8NPv5RymDpgkEosoV-Yo9-V9mfJ1qFTP3dSinShKLMupX8gRUsis53azGfK27pM3AQmi3YtCusr77yYv8yabAg18GE2YrVOhGQBBZsZ6EAVG3WC_ONikLYKW4C_XkZvIHN0YOEZtwJB2dLfufgQU-jIhquyzFEFtUZ8cU5YONzy3Hd70DuJ9kkuEoZ55bbC02puzRhaRC-gEUCQmk2HivKxtcu3b7tHMTzMQOCqmV93KBpdluaFIK5-11OMgM_wEXa89FqUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad94fd6de4.mp4?token=qYwNId56TRCiJNg4v8VSxAGfH4zcKntoGDOhx4S2Zwut9MJXGtGDo9NmFcN9xpN98fSsGSNmF8YUB8NPv5RymDpgkEosoV-Yo9-V9mfJ1qFTP3dSinShKLMupX8gRUsis53azGfK27pM3AQmi3YtCusr77yYv8yabAg18GE2YrVOhGQBBZsZ6EAVG3WC_ONikLYKW4C_XkZvIHN0YOEZtwJB2dLfufgQU-jIhquyzFEFtUZ8cU5YONzy3Hd70DuJ9kkuEoZ55bbC02puzRhaRC-gEUCQmk2HivKxtcu3b7tHMTzMQOCqmV93KBpdluaFIK5-11OMgM_wEXa89FqUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسرای یمنی از زندان‌های مزدوران سعودی در ساحل غربی آزاد شدند
🔹
رئیس کمیتهٔ ملی امور اسرای دولت صنعاء: نیروهای مسلح تمامی اسرای ما در زندان‌های دشمن سعودی در ساحل غربی را آزاد کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461263" target="_blank">📅 18:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461262">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP2pQeMGdyD_Uhlx91JjhmYXBGSXB9aFSJ9q4WhklNaJFb7yB7wNVIWxQsLrLz4VrUaKIEeuU38Ta3Y7mw2i7tyyMxyrD_gK8EkfbSUrUupANh02cD4HnHSlP2Iozl_jfTx0NIlvGusi6K2_Cb85So2r9odzhfjlaPv6crfQNZvr0j_MdAtmnYA_wXufCJvxoYXAnHgkaIlG8Gyk0EWC07IKoZwYd7uAruOxwMMn1YjZbNVstaszUarHME6MEk1IiM9QSXDtMFpzDke3YZ99LQ6BXGRUZxDBoNaPOLMNecjtC_8buA5qiNgwR9Xp2WKL0Xqa3ugznrJY2CsC3IO3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تخریب عجیب یک کاروان‌سرای تاریخی در سبزوار
🔹
رئیس میراث فرهنگی سبزوار: کاروان‌سرای روس‌ها یک ژاندارمری و بنای تاریخی در کنار کمربندی شمالی سبزوار در دوران پهلوی بوده که در زمان اشغال اتحاد جماهیر شوروی، نیروهای نظامی در این ژاندارمری خارج از شهر مستقر می‌شدند.…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/461262" target="_blank">📅 18:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461261">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c5d25dd7.mp4?token=hknUadWLwwHTYwgRVAPPNvK-DK-n_PCcdP47lJa5lPh8wZtV6JHf63LnFBRYjZZSdPfqxL0acxUkf8A7d268b3S-K2fSc63wWKBfVdyFOY1f8bertBM-IocXQQOTWNiNKjexW9gxGT2ckaMbN83ugC7F366jb4cSjiqgbQUf4dWj2sREiOkTr-Z_M0Yzd0ftWbnu2wp3U88ZWUsyedph2S-LYWauWZFZ1jnwBr1kiZ-XTGk4rE9ipBWKcafh6ryGIX_sUNmfeOb32szw4Xe3HW_BqfZBbuUOAXgdUovroO9UTouOVjiiTQ1E_4I7bHtqPnvyOPVNRGNmGPqV7XmONzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c5d25dd7.mp4?token=hknUadWLwwHTYwgRVAPPNvK-DK-n_PCcdP47lJa5lPh8wZtV6JHf63LnFBRYjZZSdPfqxL0acxUkf8A7d268b3S-K2fSc63wWKBfVdyFOY1f8bertBM-IocXQQOTWNiNKjexW9gxGT2ckaMbN83ugC7F366jb4cSjiqgbQUf4dWj2sREiOkTr-Z_M0Yzd0ftWbnu2wp3U88ZWUsyedph2S-LYWauWZFZ1jnwBr1kiZ-XTGk4rE9ipBWKcafh6ryGIX_sUNmfeOb32szw4Xe3HW_BqfZBbuUOAXgdUovroO9UTouOVjiiTQ1E_4I7bHtqPnvyOPVNRGNmGPqV7XmONzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش زاینده‌رود در آغوش پل تاریخی زمان‌خان در چهارمحال‌وبختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/461261" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461260">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5N3No5I3I37h2I3IKNqySclZZvbXkK-4xEg9s1G99dZCcSMNkMOit6pD-gtQGbeRTJc5l6YTz1cHnALPQdWsoZ7PB5jXY7CuakdPYJlS-Wq_1YCnXxNWTe1sQRcxnLBAX1GlIlzJi3UJslOZBRikavJjSr9LmT93YdTajZT9iDKs6MjUOuwHZx9FZ6KS8_KpV0n662yZTdoG-PPFCEmD1J4Uyzy3YX2W2kUg6YbYAWG0Rvkop5H0cgt3UX4P5_JCQc-grGFLPhDL6iGVbpTy5wEm4yR9TPbkgjpy8fPO8obs0ec7V4CC2IKWAPUczP9w4aWgbGtJpDxpEv6N1biwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رزمندگان یمنی ۲ جزیره دیگر را آزاد کردند
🔹
رویترز به‌نقل از منابع دولت وابسته به ریاض نوشت که ارتش و انصارالله یمن بر ۲ جزیرهٔ «حنیش الکبری» و «حنیش الصغری» در نزدیکی باب‌المندب مسلط شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/461260" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461259">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se1gsi051OkIXG1vlyNqFatn568nc98o-NRlPPdZE61yRMhO5T_1CWrYKHNqIUlhJQ0PVxvfJAf9OGHZTHQ6EV7TpixEpDod6ke9_olyC9VwmCISI6696pyF4V_ni_EYVl9ceP0cp2gy9b6FiHXasquPx0mjap6Laxu8te8NdD7UHDr_bQhtNAfwr7QLJdLCFPrrk5gl7z8RGSSbEwric9ZXQayGFf8w46JjBRa8wk3JydpjixWphgcTC8MrLDBXZdDzQETGxQ1xdGEz_nHRuWcJeMaff_lzaC0kzyQDT5391KLBJCSS_ARCDTLLykS5KLBCfqGYM2auo2Z-m1M5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
فروپاشی جبهۀ سعودی در یمن؛ ۳ تیپ کامل تسلیم شدند
🔹
محمد البخیتی عضو دفتر سیاسی جنبش انصارالله یمن امروز با انتشار یک ویدئو در حساب کاربری‌اش در شبکه اجتماعی ایکس اعلام کرد که در بزرگ‌ترین عملیات اسارت تاریخ جنگ‌های مدرن، سه تیپ کامل از ارتش سعودی و مزدورانش…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/461259" target="_blank">📅 17:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461258">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">تاجرنیا: رامین به عقب برگردد پیشنهاد استقلال را قبول می‌کند
بند فسخ ۱۰۰ میلیونی اصلاً عجیب نبود
🙍‍♂️
تاجرنیا: به رامین رضاییان مشورت اشتباهی دادند. به او گفتند هر چه بگویی چون درخشیدی قبول می‌کنند. بعد از عدم توافق، تیمی حاضر نشد مبلغ پیشنهادی ما را به او بدهد. بختیاری‌زاده او را می‌خواست اما با تیم همراهی نکرد.
🎙
ساپینتو می‌گفت به رقبای ما از جمله فولاد او را ندهید. من خیلی رضاییان را حمایت کردم.
🎙
به عقب برگردم باز هم بند فسخ ۱۰۰ میلیون تومانی را می‌گذاشتم. اصلاً هم این عدد عجیب نیست. به نفع باشگاه عمل کردیم. این رامین است که اگر زمان برگردد با استقلال توافق می‌کند.
@Sportfars</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/461258" target="_blank">📅 16:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Auma13ohqgTG-jL8gaYmFJMeEAJl3WwvXRlbxW0pZNo3bpasVfyYz4b_UnpdA4iz-sI9vQnxBjlKZz8DZ2AWhGics7moEXyR_WLC-YH9oWYUbk9Lx9t9KU9r1l97u_qhelGgQfg_ShjE1MnFA23OZBjiLsR8n9Nc5vJyVx-inJlsE4vv-h_ZaucKFfaB0UDVQP3Ow13rYf0LmqaRwRwSBP48O0cRC1OLsVnoCQ2lofeCCt-W7AGUODkjfAGZZQqD3NE7C4LKETRrFZEK_Be9w0qA1KnsEDH9pbnAPzOZDZGkp7uqv9Bjl_NWcG5pqAzCLknSKbAnGbd7DVnUqBrFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار متمول تیم حکومتی را خرید
🔹
ولید بن طلال، شاهزادۀ سعودی و هوادار متمول الهلال، طبق گزارش نشریۀ الریاضیه، ۷۰ درصد سهام این باشگاه را خریداری کرده و به‌زودی مالکیت آن را به دست خواهد گرفت.
🔹
او در یک ماه گذشته بیش از ۲۰۰ میلیون دلار برای خرید بازیکن برای الهلال هزینه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461257" target="_blank">📅 16:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461256">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN1kBjjTNa-dJlMWatx0ecVs7f8mdh_FJxKTVIJP9vofP__DCYb_-CZ649mGY__T-XV3a4jU0ZcxXzMCKUnPnpVEjE1vANPi7X9w4yy509vlYXfTwGAdXo3Qp2sI2RA3YR6GM9uwcIqs-KAovaFlGVEt1gocyLgLN-fkSTge2_OfHfmH2bZrtkuXPjoYGv9AzHMYCHVx0-vh6EKldgJ2Q5-fdL_bsSsmZHIgmbxVxVULRX9rMk5aJuQfgYysQL1zrmCJYYKsDSvdNZU2K-5P3bi6blZQDob2BTH2KUaZjwkbyzWDQR7H1x6Mfvl4zBnWRW69wW6AhO8ealUuTRXJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفت به ۱۰۵ دلار رسید
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/461256" target="_blank">📅 16:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461255">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/986f07d0b9.mp4?token=SEvmLXEIxms5Dgmz0uBQSFGIkkb7cvhqWkiDuu9UXFGbJhLBeUut6JttCpN1QOWiqLHixKTuTXN_t3tcqnEqcCmEYR73FCJo9_-afcIh0CLp3O3rgVa8TZMX9lhbw6xDXz41xJRKyWIfbqnnnV3f5dPuBf14_ycGSGS8wKQny9plTJl9idUf_Aq89LvRBMW2P6rsWMFDV_PjuWuURCzY6okZZ_Au_S-GJQ12YstZNiia2DMa6SQHM1VnFJBiU8YHUH4oVGXSfsqyNLRyezzkGAgfp-prATwh6Ers8dsDGHLZt0pmj2XfvgTD0ofyRgct8EiPCa9A9zGSBHMfE5j7mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/986f07d0b9.mp4?token=SEvmLXEIxms5Dgmz0uBQSFGIkkb7cvhqWkiDuu9UXFGbJhLBeUut6JttCpN1QOWiqLHixKTuTXN_t3tcqnEqcCmEYR73FCJo9_-afcIh0CLp3O3rgVa8TZMX9lhbw6xDXz41xJRKyWIfbqnnnV3f5dPuBf14_ycGSGS8wKQny9plTJl9idUf_Aq89LvRBMW2P6rsWMFDV_PjuWuURCzY6okZZ_Au_S-GJQ12YstZNiia2DMa6SQHM1VnFJBiU8YHUH4oVGXSfsqyNLRyezzkGAgfp-prATwh6Ers8dsDGHLZt0pmj2XfvgTD0ofyRgct8EiPCa9A9zGSBHMfE5j7mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی صهیونیست‌ها به چندین شهرک در جنوب لبنان
🔹
رسانه‌های لبنانی از حملات جنگنده‌های رژیم صهیونیستی به شهرک‌های صربین، حداثا، حاریص، النبطیه الفوقا‌ و الخیام خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/461255" target="_blank">📅 15:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461253">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65a2defa4.mp4?token=opJ4LcsL0DFXlux3jX2LOLydCqg0QNILmhiCBE-XVs1g4R8NpxZEcSIKkhIUMOlNjNSPZx9BCbzxO0ali6feVYx8haNWpfFanFTD6X4nQRON55gHJCBcjQDqmSWPw_Hnx_U2pysQHqigJfNueXqqKbHbyoxre82R1GmxN3-kG3YcDDG5AtJghx61tUZPqE4S1sPcLiIwqd4i6UNC1gzEKoUXp50ndBLOS0XBxrQ1r8CPHJXJZvtMSiMZy6YSl_YiWxCA2qsIsh6aIpYtHME_0o64o_-6syphtA8D2mLrieFajIgHUi2Xj40vTA6Mg01AZGm4LoCWjeOc2VFkq-O0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65a2defa4.mp4?token=opJ4LcsL0DFXlux3jX2LOLydCqg0QNILmhiCBE-XVs1g4R8NpxZEcSIKkhIUMOlNjNSPZx9BCbzxO0ali6feVYx8haNWpfFanFTD6X4nQRON55gHJCBcjQDqmSWPw_Hnx_U2pysQHqigJfNueXqqKbHbyoxre82R1GmxN3-kG3YcDDG5AtJghx61tUZPqE4S1sPcLiIwqd4i6UNC1gzEKoUXp50ndBLOS0XBxrQ1r8CPHJXJZvtMSiMZy6YSl_YiWxCA2qsIsh6aIpYtHME_0o64o_-6syphtA8D2mLrieFajIgHUi2Xj40vTA6Mg01AZGm4LoCWjeOc2VFkq-O0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزد، بزرگ‌ترین تولیدکنندۀ مداد و خودکار در کشور
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461253" target="_blank">📅 15:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461252">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e333d9a21b.mp4?token=OXlcSpCpDOQVeUaZDGbw63J0m7Ug94MMaVATlwKs6O0Orpu5LO8XPPwksoRyXOTzKPcaGAJAHBIfupkYIn8iDDaUA8OZfyoLh59z-0Tzi-ex6AxRCqv18KWh4JKS2q5UoB3sPAurdhUCFwNGmIC6bFbrq7meWJjv_twZzi05qviiSEyCGeMJ13o9qxTlSXojBaYaWMiFVGippbpxk3I0ap527s8IqyD2tyycxS5G9oa_dpgW1enoudvOWvfGpjUR4aclNCdraJai9VXS11D0rxVRbQtz90R-CM6yDqnYHDccpyEXHf1SHOWcBrkrPhxHwfiPC8P84NooWIFgygvYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e333d9a21b.mp4?token=OXlcSpCpDOQVeUaZDGbw63J0m7Ug94MMaVATlwKs6O0Orpu5LO8XPPwksoRyXOTzKPcaGAJAHBIfupkYIn8iDDaUA8OZfyoLh59z-0Tzi-ex6AxRCqv18KWh4JKS2q5UoB3sPAurdhUCFwNGmIC6bFbrq7meWJjv_twZzi05qviiSEyCGeMJ13o9qxTlSXojBaYaWMiFVGippbpxk3I0ap527s8IqyD2tyycxS5G9oa_dpgW1enoudvOWvfGpjUR4aclNCdraJai9VXS11D0rxVRbQtz90R-CM6yDqnYHDccpyEXHf1SHOWcBrkrPhxHwfiPC8P84NooWIFgygvYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران رتبۀ سوم دنیا در درمان ناباروری
🔹
رئیس نظام‌پزشکی: تمام تکنیک‌های پیشرفته برای درمان ناباروری در کشور درحال اجراست که برای گردشگران سلامت هم جذابیت ایجاد کرده.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461252" target="_blank">📅 15:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461251">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsosYnXSIoxTAkF6xCBLfgXpYJnA0FplemATstm12LcivIa9iAR9_ZWFxzQ4ID3EqN8pZRFu9BugXOFdzibf3zXOanMZ0YfQaezgrwLJgGYUXjmg6FOpS7uzU_vtWuzBNkaob-2dg2yRw1kEzzndSLy3CwiYyeK1DSUTbg0FT_cuI1oDd46bFU9EWJUWNs_eYalY36VSzMUzhYn7KWrk4xhFT3XGHfBnF3Wfjt7CiGax_b-97fVnS1sLiCn5UmTlrKnYinHN_NQV14TPkxpfO2y10T-HWvJzr3lriqBz0WDcUYhDU_pclcg8jIGbuIGyCLRHQvCnED9BsKtYGmMRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرفۀ مکالمه تلفن ثابت به همراه ۴۵ درصد افزایش یافت
🔹
طبق اعلام شرکت مخابرات از ۲۰ شهریور، سقف تعرفۀ مکالمه تلفن ثابت به همراه از ۶۲۵ به ۹۰۶ ریال افزایش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461251" target="_blank">📅 15:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461250">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e0c46974.mp4?token=udAej_6r-2jHp3zCyQd8jP8FbfZW8HlCijSzipfHSpwMkdCA5EoHRtcGNo820KRQGEDsxZ1uL546DkKVjkf3HN9gldcvFDTfu56G-wLPQ6jCK2ZO4irZmQ73mXkglkHcozQcq6h6QnjsrSvmEeCh0DquWjLBiJq82sa38_rYbTkifiWFwa_xzozM2JfNzHlCpRXeOz7j3RfFEkPpM2uUyL6Rt8JPR7_yUkbDZF700Ezx1U1uLO-Sj4yj9mB7SCYIA82BFGtdVZp3yl6Q07MyMBWyLH_RklyoDu_R9oq2NYEABkPTdqSqa0Fgi3H745FHah9iWaEkHSM3zPasJOmPqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e0c46974.mp4?token=udAej_6r-2jHp3zCyQd8jP8FbfZW8HlCijSzipfHSpwMkdCA5EoHRtcGNo820KRQGEDsxZ1uL546DkKVjkf3HN9gldcvFDTfu56G-wLPQ6jCK2ZO4irZmQ73mXkglkHcozQcq6h6QnjsrSvmEeCh0DquWjLBiJq82sa38_rYbTkifiWFwa_xzozM2JfNzHlCpRXeOz7j3RfFEkPpM2uUyL6Rt8JPR7_yUkbDZF700Ezx1U1uLO-Sj4yj9mB7SCYIA82BFGtdVZp3yl6Q07MyMBWyLH_RklyoDu_R9oq2NYEABkPTdqSqa0Fgi3H745FHah9iWaEkHSM3zPasJOmPqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ضربۀ‌ کاری انصارالله؛ جزیرۀ زقر هم آزاد شد
🔹
خبرگزاری فرانسه گزارش داد نیروهای مسلح یمن امروز، پس از تسلط بر شهر راهبردی  المخا، جزیره زُقر در جنوب دریای سرخ را نیز آزاد کردند.
🔹
این خبرگزاری امروز به نقل از ۳ منبع در دولت مستعفی یمن وابسته به عربستان افزود…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/461250" target="_blank">📅 15:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461249">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0392dada5.mp4?token=SLm7JNOWc0eVMYr_ntGfDFdg07d0cL0oiS2v9VkmPRGX1YnPX8AWCzDmZuSz6XIXtHP9e82GAjd8aw3LF9GmEwiPF_cq7LDwJyKCHVpD38Hw1q3F_5N6pKLHg6fi3Py2QvXi6sICZoB66h-tXfvs3JWPEQ-sR8EPOwOBuLqAIxiCCk-IaAsFblfc1kb-qO__PD_ptt1XPL4LEEOgbPAKc5D7ygZDBLC1v7HhN_sUSSnpH_6IIDsIT6KTNvSNX2RE7QUo5GbjWGONlF1WHclRYPBKBFCRVwthM21PP1uTgfNFYdCCKa8Qc0gueshgBik_tyJjaYxzxQpSGPJ5nmHz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0392dada5.mp4?token=SLm7JNOWc0eVMYr_ntGfDFdg07d0cL0oiS2v9VkmPRGX1YnPX8AWCzDmZuSz6XIXtHP9e82GAjd8aw3LF9GmEwiPF_cq7LDwJyKCHVpD38Hw1q3F_5N6pKLHg6fi3Py2QvXi6sICZoB66h-tXfvs3JWPEQ-sR8EPOwOBuLqAIxiCCk-IaAsFblfc1kb-qO__PD_ptt1XPL4LEEOgbPAKc5D7ygZDBLC1v7HhN_sUSSnpH_6IIDsIT6KTNvSNX2RE7QUo5GbjWGONlF1WHclRYPBKBFCRVwthM21PP1uTgfNFYdCCKa8Qc0gueshgBik_tyJjaYxzxQpSGPJ5nmHz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محل مصرف مالیات‌تان را خودتان مشخص کنید!
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461249" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461248">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=IoAsfgG5b-INjVFKr209bXc_sY6jqYPbpW02tvA9vQiX9vF92I4Oa05vwigors65-zM6XLHgXbOhJVxahiteCpjBthtqnsF_Qh-aoZ-Hm9gtaHzKoiT5VUB0BI9eTH0HXN-FNvsAcLASw15wL75f0GlNqOOdpw5KMW2I9LKYY1z7r31Joicxkw7TF7slhrVB8f8xLFZGWb65g7xuGkoPNmFRbkg4w430rjyVXp43YDRrgw1REJc0M2HECPimGpWfVC-7H8Gv-E6ngTKkQjQQDa6pCz2NvSccwklXUhF-nNMDubA8zeGEK3zaEp2w2o66nhGYnlMc3-XFyuGWOrs56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=IoAsfgG5b-INjVFKr209bXc_sY6jqYPbpW02tvA9vQiX9vF92I4Oa05vwigors65-zM6XLHgXbOhJVxahiteCpjBthtqnsF_Qh-aoZ-Hm9gtaHzKoiT5VUB0BI9eTH0HXN-FNvsAcLASw15wL75f0GlNqOOdpw5KMW2I9LKYY1z7r31Joicxkw7TF7slhrVB8f8xLFZGWb65g7xuGkoPNmFRbkg4w430rjyVXp43YDRrgw1REJc0M2HECPimGpWfVC-7H8Gv-E6ngTKkQjQQDa6pCz2NvSccwklXUhF-nNMDubA8zeGEK3zaEp2w2o66nhGYnlMc3-XFyuGWOrs56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حادثۀ مرگبار برای کشتی خارجی در چین
🔹
خبرگزاری «شینهوا» خبر داد که یک کشتی باری خارجی در حین تعمیر و نگهداری در کارخانه کشتی‌سازی در شهر چینگدائو آتش گرفت.
🔹
به گفته مقامات چین، در نتیجه آتش گرفتن این کشتی در چینگدائو استان شاندونگ در شرق این کشور، ۲۰ نفر جان خود را از دست دادند و ۵ تن دیگر مفقود شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/461248" target="_blank">📅 14:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461247">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX9RbljAMMRjBtgJkaYr5WO0RNjpn-EdysGpWGm6q0hMmAqy3sxywchRfnOZ-b2vZAqT3RC0BsBmnQaUNw_gj5r94h3XnZA-PfWdZzNCA2qedhIfN__GA1XUxkjQjb6JhkJoSmQ85Ij0pNfjKKldcQLnfYJMbX8zzdxs9imjAugKvHZk1xD4wpDUZTN6FhKGu4XM_NMx8g1NbQBtd8aR30zv7x5-gTHr1L_O1m_6UV7vKZ_nwoUB7Zp_5Ds4hJruiMLkOfUbmXB6dU6VveFmzXf_Qt0bZ3T8w0spfBEDuT4r9zRx8pgEaylLCaVYaTu6V_mcUge23ircIr0Lc7BGig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیبر - پرسپولیس</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461247" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461246">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k468OWM42SA2pViPLaAxXMDo5ntuCSzkB8RjQy7PUmV9G36RcH91TRt9fPWPoSfzK_QHdyyxbWGYWr2L4bP7x_n1w1fH1ieJ7IBP6yLgSRIGeRKuV-0er4KktukJEK9hxwC_yOKuhym9m8NZx__PMep2RZG8j8vIWYW19P1EUVFDA7Z8El8DRF3T1pwuj-rBofMPoBKeIC9Sm9UAhrKlBCtFFzwVSZE2KL2UcdQHcnAPVabNgIWiBhLAaw-G_NFrg0El9uhBkpgc3BCaSdtpubM7WrIh2-eFknp2UHe28U2GiH4f7fJfSAG4Pqkcwkl2n2R0BhUWeQcrNBtc0m2usg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در سواحل یمن
🔹
سازمان تجارت دریایی بریتانیا با انتشار یک هشدار دریایی اعلام کرد که گزارشی درباره یک حادثه مشکوک در ۹۸ مایل دریایی جنوب غربی شهر «المکلا»  در یمن دریافت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461246" target="_blank">📅 14:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461245">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWTINrQAMnALgxBFxK3Y05ZcTlpOCH1c0RJvIBfOXMKDnI5nj2QMPNl8gvQG6nwLmo2o4Ndhly4MUptgejOnX4k4b2IRMtuHIWEG6NZZh1sFdind9FtZpXut7-pomdBBRG64iK4L3pJITx0Yx0UnlQ25HeEKKvsEHffEPvgxoDevi82hJ9lhXKdrv1vJaFYzT8_8iT7nsUk8b-ZweFueNfWbmXF_8vSHvWHNTXHDZDYVqFyH8ZNeOl9Vfpcu67OlWrJ2ORfFH6NaVlyytSK_6Muw5fJGXM6pq2Ev6E15owr9J9gXDHCL17Kq6n3fgKoEw5ynLsD15oDYRymq0KbYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پیشروی برق‌آسا در المخا؛ انصارالله به دروازه باب‌المندب رسید
🔹
منابع رسانه‌ای از پیشروی برق‌آسای نیروهای یمنی در المخا خبر دادند. پیشروی‌ای که از شمال به ساحل و از شرق تا فرودگاه این بندر استراتژیک رسیده است. تصاویر منتشرشده، فرار و فروپاشی شبه‌نظامیان سعودی…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461245" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461244">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef49ccbd09.mp4?token=IYCpw1lQNTHLCLcHHRohhfIoxskpVuGHGcpKur2jkLwrJYksnqwFrOQT27PLYnhc9ClannoyIyl7xDy3Uhh8j0jWEbSRzMU1kXe60pLf-pBCLZyJzoW_iQPOv7EPss48UU9hl6p17kBKOY5HF2dadp_Q_N7QwMhpm8-WZNEmOtCdsiK7CwoHThgAYBVG0uWLouhiXt8Kh7tkbWYSem4KPPZ6KFW6tfLj4VRp3vJ0OHNko4JERHRy2pes_02PkKTRNpiutPx66rqeQMAzH6Yj_GXq2J_ncYprJih7LWRawyKd-Lg4zfhjvHRPDGeHOlRA29mX7Wy4lPtE5-y6Ipsg3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef49ccbd09.mp4?token=IYCpw1lQNTHLCLcHHRohhfIoxskpVuGHGcpKur2jkLwrJYksnqwFrOQT27PLYnhc9ClannoyIyl7xDy3Uhh8j0jWEbSRzMU1kXe60pLf-pBCLZyJzoW_iQPOv7EPss48UU9hl6p17kBKOY5HF2dadp_Q_N7QwMhpm8-WZNEmOtCdsiK7CwoHThgAYBVG0uWLouhiXt8Kh7tkbWYSem4KPPZ6KFW6tfLj4VRp3vJ0OHNko4JERHRy2pes_02PkKTRNpiutPx66rqeQMAzH6Yj_GXq2J_ncYprJih7LWRawyKd-Lg4zfhjvHRPDGeHOlRA29mX7Wy4lPtE5-y6Ipsg3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اعتراف رسانۀ آمریکایی به ضربۀ موشکی ایران به جنگنده‌های آمریکا در اردن
🔹
سی‌بی‌اس نیوز: در پی حملۀ موشکی ایران به پایگاه هوایی «موفق‌السلطی» در اردن، چند فروند هواپیمای نظامی آمریکا آسیب دیدند که یک فروند A-10 یک بال خود را از دست داد و حدود ۸ فروند جنگندۀ…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461244" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461243">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHfurX4DQvuPNLuPia537CoxTZI1bldCgqI5T0du-L9pB01q6isUz2WzIoJE830oNkiI_slBjLnIDm76J77vomRBDzm5tYhrlrnUQ1vKlq68EcaSSF28uRUC9Ek5TozIfREaDT9J6jngNuMyOeWtf5D-MIr7XfUTvoVHD6AJiEVBwmaVE730909hcjswbaXP_dYh9TTdpRNTaBPDb2vuHM7hvX5deorva4QCDbqMs6bpJTo9_4aIbSGUZyEvYG3fRm6bhrwvv5LE5t4AiIZYnKPnv84B3afzDIfRYAp7ZdgjJ3YVZ6yeXi9sZ8cq4frwxP4nAu_1Ysobw8dY9h-GqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تماس‌ تلفنی
پزشکیان با استانداران استان‌های درگیر سیلاب و آب‌گرفتگی
🔹
رئیس‌جمهور: رفع مشکلات و تأمین نیازهای ضروری مردم باید در کوتاه‌ترین زمان ممکن در دستور کار قرار گیرد.
🔹
همۀ ظرفیت‌های ملی و استانی باید برای کاهش آثار ناشی از سیلاب، صیانت از جان و مال مردم و بازگرداندن شرایط به وضعیت عادی به‌کار گرفته شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461243" target="_blank">📅 14:17 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
