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
<img src="https://cdn4.telesco.pe/file/ve7ykfdS7NvybeltI7lv4yjtc794Gsr494m_8mcid5ktJrWZWr0aj96C02HVY6Qo62M6hVF-X_6V6Ip9bgsYI-MFdFhm24gdWIBXfW_2Tdemfv8tFJyd_EBmjP2k75rHwuT-ygIh_ohMLUNg48CdmaJW7Qnj6IrJyG5lff_ExUXnBK9pIJDO2dJzNEcyPTxNNEBO11udQ0cZOYw0MytBuFk1gx8cAgDw59U37E4CjtZaSIc4ZqLtkhlrMK1tQqd0_XJRB_qI36yfcuS-7ye3-qX-Hq6robHowKky_uj9h0OBRW0O2R5f-I_uO8o2F4sYlPQkdY3hzR_aM-UWkOvW-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 986K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 17:19:42</div>
<hr>

<div class="tg-post" id="msg-139844">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3aBfOEISWOO4CncoEDWEHEdrDzViXwD1X8ntXMUhr17JipbE3HEBcLfzb6DIlPHZdaIfT4Mtd1QQcUBq6UUST1cPzzkKc-lxfBJdMtHcVYSp4-dleo-k-HqoeRIOiP2zryggxJm2bQad20yXhpfl_xMqPJ-YklmNej9fziaW2fEjXSPvma6i2jtO3EoYSFr-7JrWnDuD_J_fEj9cO3INcefPXmBdcEhwGDzRw9jeC7Yhl3Tpo6FW13kSyJsAZuLM6sPooUMd6PW-MhOgm8x8mPHvBA2iRdDha4dC_7Nalabm7IA4zv4XkGv3wf-P6M5KBzXwoQPqyryKZjHYpaVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFxzx5MKGLaHX468am9pHm6_8Lye_RQJKis90o_sPvYahRnCh0-H7QNsHasZJnN2JJY6I7-XsCBau8lJqJ8dKU5ywj9U-DaSpk8504__cdve1D-vWy5KDRLVIM1KxOy58a7c22x9vPJm42SzkGQy9VY9uZQKyWAH9-nlbChYU3aHGcQ57by1zk9fngW3WZppei50D3oorQ2bLF2GrWZXwTnSpgsoj_3yE8eKm8jsCKjWOGY-YjCgzNdRiaEuUlrI_w3BrhoDnNtaGR3VEjaMZHh40WKVs_Nm-t5WrFDEhyZ48F3hpy4Og2LaNusZrKntIw_JzcIbUfFjHLun8O2mPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک هواپیمای آمریکایی امروز از پایگاه هوایی اوسان در کره جنوبی به سمت پایگاه هوایی عیسی در بحرین به پرواز درآمد که احتمالاً به دلیل کمبود موشک‌های پدافند هوایی در بحرین، محموله‌ای از این موشک‌ها را حمل می‌کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/139844" target="_blank">📅 17:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139843">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
الجزیره : اعلام توافق برای بازگشایی کامل تنگه، ممکنه تا چند ساعت دیگه یا نهایتاً فردا انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/alonews/139843" target="_blank">📅 17:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139842">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
یک منبع مطلع به العربیه: احتمالاً طی ساعات آینده یا فردا، جزئیات مربوط به بازگشایی کامل تنگه هرمز اعلام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/139842" target="_blank">📅 17:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139841">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شرکت تسلیحاتی «فایر پوینت» اوکراین با بیش از ۱۲ شرکت دفاعی اروپایی برای تأمین رادار، سامانه‌های هدایت و دیگر تجهیزات مورد نیاز پروژه دفاع موشکی «فریا» توافق‌نامه امضا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/139841" target="_blank">📅 17:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139840">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_exWetlnRXFBDs7HIPkWQymQsCnYXrPcuWN9idWlPUx94wfN9Xi8uT1AelS-rBUilzzFzONCQP89nq3H1AxfuyKB2WsLPFX-huwXqQcsVTm1XYUW63uRgQbeVSu57ey7PBoF7LtikOmpzmD9t-w_5I9Yslm1PUOd7OmagitrReFGfcSp-5neiE2T0Pe8ET8L5R3oOdN3146et6UaEBwyjPzTBBUy_E33OFCiUCTNDBU8BQRn6fULq7LM07IvOhHtVjuPf2bOA2V8u_uIVWw8IeFH8ug0-HvGnJOC8b5An3RWIhFlMa3m-F0GTZpSf9L6cQ-8bbQ9CC7Qgou374wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایوان: همکاری نظامی با آمریکا فراتر از تصور است!
🔴
مقام‌های تایوانی از گسترش همکاری‌های دفاعی با ایالات متحده خبر داده‌اند؛ همکاری‌هایی که علاوه بر فروش تسلیحات، آموزش‌ها و تبادلات نظامی گسترده‌ای را نیز در بر می‌گیرد و بخش زیادی از آن تاکنون به‌صورت علنی مطرح نشده بود. این موضع‌گیری در عین حال پیامی به چین تلقی می‌شود که نشان می‌دهد روابط نظامی میان واشنگتن و تایپه همچنان در حال تقویت است.
🔴
به نوشته وال‌استریت ژورنال، «ولینگتون کو» وزیر دفاع تایوان تأکید کرده است که سطح همکاری با آمریکا «بسیار نزدیک‌تر از آن چیزی است که تصور می‌کنید». به گفته او، این همکاری‌ها تنها به تأمین تجهیزات نظامی محدود نیست و نیروهای تایوانی از طریق تعامل با ارتش آمریکا، تجربیات عملیاتی و رزمی ارزشمندی نیز کسب می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/139840" target="_blank">📅 16:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139839">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUX2S9Y9qnAylkEeVcwTz9KQF5P1GeAVUYNt7dmY9lXsy_4ROCF4qiFaycf73E8wKrfIguNb3E34PsVIDv4clC6LlV7aG5aitxdi5R7W0my6jk00ymihz4bnx8Kji3udyT0kQz1OWD3EPut_kHXo5YzMyaeIbQEqNlMvRPy3zqEfPQQSytHVD3n0kppnzk24l_sdyjlGJg0RL2GvJ2ifUufyjRcIygCbem4GFKbWcld_3bOMm0qNJbvjsI9DFuB630ZVtFLXmgsMFUI0gi6iezZaOuuUplkbtaVfKIn0VDpEad9R5aY4FxEnmh_LYQPWkbi8vBOOyLusITWEQ_7KQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط نفت برنت به ۸۰ دلار پس از مصاحبه تلویزیونی وزیر خزانه‌داری آمریکا و اعلام احتمال دستیابی به توافقی جدید برای بازگشایی تنگه هرمز تا فردا
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/139839" target="_blank">📅 16:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139837">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شش نفتکش غول‌پیکر سعودی، خالی از محموله، مسیر باب‌المندب را تغییر داده و از جنوب اقیانوس هند به سمت آفریقا حرکت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/139837" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139836">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رسانه‌های انگلیس: آتش گرفتن قایق حامل ۱۶۰ مهاجر در کانال «مانش»
🔴
رسانه‌های انگلیس امروز (سه‌شنبه) اعلام کردند یک قایق حامل ۱۶۰ مهاجر هنگام تلاش برای عبور از کانال مانش دچار آتش‌سوزی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/139836" target="_blank">📅 16:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139835">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ویدئویی از عملیات جنگنده F-22 همراه سوخت‌رسان آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/139835" target="_blank">📅 16:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139834">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
روزنامه Izvestia: آمریکا داره با سردر‌گم کردن تهران زمینه رو برای یک حمله غافلگیرانه فراهم میکنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/139834" target="_blank">📅 16:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139833">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
امارات متحده عربی ورود همه شناورهای ایرانی، از جمله کشتی‌ها و لنج‌ها، را به بنادر خود ممنوع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139833" target="_blank">📅 16:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139832">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA8wYEzk3EQGA4dM0iXUqhhvd8UC67UulAqD09KAXxJUb3h-2EN1M39rWMHjRLFO5SN2XtfRli-0hz3alHqjGvpgQXcKpgxB03hCu_kyXQKJjU_lST6IPJu3bJ5FW838Yh3Mkozzr_BmoUAZBCm3JqH0PzqG-07qypmDHLBl81uGd1Ib3HyDKUjDKatB1b-_orXs_fc9nVP2Ry6lhGQdZugMq8vEEJpY8hS9UpIi9hOV-dvLa8UhqX_7FRCa2yUP7s8LTE3HhGrZDnYJl6xAzKanvujw2OFm3konuKTFyZTbUWqtNSqVkuyPIMxP_H4FsLtC5qqpXZ-d2reDSPluIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن عباسی:
سال 73 با امکانات متروی تهران، در جزایر و سواحل جنوب تونل زدیم
🔴
زیرِ جزایر و سواحل، تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139832" target="_blank">📅 16:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139831">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EguU5f4xO3oA2CR96wrFjprjK8inu5HWMTHW3vO4w0Tbs13tDqg19geZ-tElnho0S_mD5DqpBuz3jduU1HfEzYYUgTvEI5-lpdXI4D5RgWhX8PSrZE9Ue8AImHQCUWl7q04m9i_oQBuGAvqiGz4NDi90Fkepe_l8VXohEbw2z0jY4UuMrjVpDMnJc6YVGpvYzGpvDw7LBrlpJPfvUj4-K9PZ2mWtXy6fmQu7-ZjX5Kq3Gw_3XWeUm0uj99et80noH62JYLNGHkISksqyBP8nKHn-Q1DXyRwgcDfEBOJBdqn9RN_1Iz5eBFuVJbXgG1kbdgs_EXwKiAvVOE4xG47Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : وقتی با رضا پهلوی حرف میزنی، میفهمی بیشتر از سیاست به فوتبال، غذا و عکاسی علاقه داره
کاملاً مشخصه که او ویژگی‌ های لازم برای رهبری را ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/139831" target="_blank">📅 16:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139830">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7UsZ-JJj7gRlXCxtr09rt3KRMaekVE9uPkJtMDF4apY8q52HjPeSW1nULtHx_n81r8IoWJrNzdxco4CwZrBkW5ofnnL_WmXjt4ykXFoGBoDkkK5Yqbb7bkVKWPMRU9387Zv9lbaNGFpIKoEY-M5seAWW7ZqiwDpyk1_m-SjD8mEZUUVKFZEPDtbXbObnmPjma0A-qqTin0NQfOCPL5rUkIGIOyQCZwv8dXez8slQKB2Uuqt8-rQjbFLGa5OXDmhVLNVjV2hv4EIAtjsSSuNMfb3eq0Jx-2XSIqqIqUK4yxcrJn9iLPE5uy7dEU_LE8rangQaN5mV01exO6ENbHdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۸ نفر بر اثر انفجار در شهرک شمس آباد مصدوم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/139830" target="_blank">📅 16:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139828">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df5d5b7fb.mp4?token=R6mmVgszfTcz0hHzCmxGKUmNTzelwx59K2P7Tf3svMqhqkiD8CClcUTFH4PLJ22cMV11h-QgAzHPb6AuB2dQK0NDhnPC47K0Hp-eruDQtHzH7pu9h9bgkr5RNXokjAE_VSNNZ28Fdc98Ql2P1lZLVfVkuoNsBNU1LAc-h3NCVZYFqdUaVL_uuzuuCOoqeaWOjxBZ0aoJkubz3nXaKbW5QIDq8wvd_vn2xu2-DApAkZnCxylDMhUxTAHab1N-xhirEqtjWrME_aHIQC7BtX2kFW6x6k6Tzifs1lX0sQZva4Ck82uLSYEgB_iKO_uK9xWXFM2ydMb7RkccEyI46xLNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df5d5b7fb.mp4?token=R6mmVgszfTcz0hHzCmxGKUmNTzelwx59K2P7Tf3svMqhqkiD8CClcUTFH4PLJ22cMV11h-QgAzHPb6AuB2dQK0NDhnPC47K0Hp-eruDQtHzH7pu9h9bgkr5RNXokjAE_VSNNZ28Fdc98Ql2P1lZLVfVkuoNsBNU1LAc-h3NCVZYFqdUaVL_uuzuuCOoqeaWOjxBZ0aoJkubz3nXaKbW5QIDq8wvd_vn2xu2-DApAkZnCxylDMhUxTAHab1N-xhirEqtjWrME_aHIQC7BtX2kFW6x6k6Tzifs1lX0sQZva4Ck82uLSYEgB_iKO_uK9xWXFM2ydMb7RkccEyI46xLNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
توریست ایرانی پاشده رفته کوبا و زیبایی های کمونیسم رو به عینه تجربه کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139828" target="_blank">📅 15:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139827">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کاهش نفت و افزایش اونس طلا بعد از مصاحبه وزیر خزانه داری آمریکا
🔴
ریزش 5 درصدی نفت برنت به زیر 80 دلار.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139827" target="_blank">📅 15:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139826">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا، در مصاحبه با شبکه CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139826" target="_blank">📅 15:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139825">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139825" target="_blank">📅 15:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139824">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-C1o7NS2DGod1JnlyMuX2Zl2pTvIIqh0fdcVB5CornlIFSNrrPKofL7v5iHD86XZK44sZ1MVT11qw1YcoPhsPCOIC-CHG1BSC8OPvpCfSWW-WrDE7Zs0sbuZFpJ82HC6F8x3LhXRH9D7WiaL9VigKqOFaZzZ0T2s35fucrmMit7TUJEZ-1H1ZEzUbvRYRywMQk-gP6o4gnQm48e9JaTMNFzXuER3SbX9KImmHraqsHEAHNLHaw63XP5oSGr07px_N-8KcxsTyEbKkvEN2-0wlLF8vEyy2W6kfS5R11D3pfluMuHAe32P3gdudON9x-x49LGekUNNAUwQ3VTCaOhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
العربیه تصویری از کشتی هدف قرار گرفته در تنگه هرمز منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139824" target="_blank">📅 15:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139823">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi29nO7snJmg4p-r6ffXnXPNLU532RKfuMfjsGo__Ik3vCuSN-Vm6_yyS6TAYOD2m8jd6V3vW_38_5a08ryoanMoyq5dq2ymwrd_tmWnkrC3k_6fTUohAOnGpC0AWkCeHnKBdbeaUbcyTUgMAygQnKnrvhYIgW_szf06Xe2o1i_8MgBXl1V7cOB6Ii8GF5gkqeZ0WqzKFCoqbOhMapfI4BEM7WcIg7O3RXGWe8b9f4GE6cowB143NAGC5V5G5wHPEKSxxc3Ri5vVvbjAjcVgZs8nNQzL7aU070-4T1Ldk-_prbaEkNgxreEdau7mDpwgpV4EYyoBmoD3QLz_r5Oy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: ترامپ تا سه شنبه به جمهوری اسلامی فرصت مذاکره داده و باید تنگه هرمز رو باز بکنن
در صورت باز نشدن تنگه هرمز ایران با حملاتی ویرانگر مواجه خواهد شد
✅
‎
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139823" target="_blank">📅 15:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139822">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpFgpi42Y7bsdpfMrOkMfJOqSnmDYiff10Nzfi-JxAlHj-Q57UAxSoW6hAQigMqQ0yBeahpupQBD_KvCEoOK-GI08DtZjSK1vEDn6yYbBUWwWdaUXhVYnjox84ebguKSdhoXOyEA3JzVT8ACOYnNWRURG2J7agP_VCuLqofHZrFWceMAjCB8EJrpoMcdrCR3k0XjzydACVVEGOfatEtRr6IerTh2BrQwDEfO3fF10jkbNn1uoTLBl_jkzyxFpdOQd9FEaY3i7V5O5ZmCjjYIog6a3enVpDCU3cA1geK0ilQKbesbwIdn9c3wulmaHQBeVhAI5o9LIDS2qZEEdBvFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پراید در سال ۱۳۸۵: ۶ میلیون تومن.
Vs
چرخ فرغون در سال ۱۴۰۵: ۶ میلیون تومن.
همین برای توصیف اقتصاد ایران کفایت میکنه.
فقط طی ۲۰ سال.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139822" target="_blank">📅 14:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139821">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
قطر: متن اولیه برای یک توافق  آمریکا–ایران تدوین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139821" target="_blank">📅 14:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139820">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
قطر: متن اولیه برای یک توافق  آمریکا–ایران تدوین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139820" target="_blank">📅 14:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139819">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
امام جمعه ساری: بی حجابی سبک زندگی یزیده، سرباز یزید نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/139819" target="_blank">📅 14:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139818">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
جمهوری‌خواهان کنگره آمریکا برای ایجاد اجماع میان اکثریت شکننده خود بر سر «قانون SAVE»، بودجه دفاعی و چندین طرح مهم دیگر با چالش روبه‌رو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139818" target="_blank">📅 14:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139817">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
زمین‎لرزه‌ای به بزرگی ۴.۱ ریشتر در عمق ۲۶ کیلومتری زمین، کهنوج در استان کرمان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139817" target="_blank">📅 14:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zng8-TX71e0HDAMgWRxEIOkcu33IdxFJMTWGMaxlcIP4FHJ0sSNLoS-cAsyvM_yrUqiEpY2JjJnkPuEvcXBkh7L-PZXIltepXh8pVpev7-gPHOYDpaF5IFZCEq80VVICB4bPT6ekBpOP49hLog3h85Im-uc7ljDs2kVy85k4FhDv2RpUENndTvGeeIpF92_7EGLx5v5tu5k5waHUs3L_cUs0t651MJLt88aXDjNyr-wnVGe8zev-9dCkrSsOvNzDwG2L4kk65c5kcCZIJqMvP1LXR2dLY2Ggt8ISzqL0ZKXC7dAxi1UIe7QKvmkTEIb_4u9l03PlGRx3uNMQbyb9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری دیگر منتسب به انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139815" target="_blank">📅 14:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
گویا یه مخزن گاز ترکیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/139814" target="_blank">📅 13:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رویترز:ایالات متحده تقریباً تمام مهمات پرای‌اس‌ام (PrSM) و اِتِی‌سی‌اِم (ATACMS) را در طول جنگ با ایران مصرف کرد. همچنین، کمی کمتر از نیمی از ذخایر جهانی موشک‌های تام‌هاوک (Tomahawk) نیز به کار رفت. برخی از مقامات نگران هستند که کاهش ذخایر، آمادگی ایالات متحده را در صورت بروز درگیری‌های بعدی تحت تأثیر قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/139813" target="_blank">📅 13:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حوثی‌های یمن : با پهپاد، یه حمله دقیق به یک «هدف حساس» تو فرودگاه نجران عربستان انجام دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139812" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139811">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
گویا یه مخزن گاز ترکیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139811" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139810">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / صدای انفجار در شهرک صنعتی شمس آباد تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139810" target="_blank">📅 13:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139809">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
حوثی‌های یمن: یک هدف حساس از عربستان سعودی را در فرودگاه نجران با پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139809" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139807">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUiMVkmTkIT53QF5dGf7-mD8o22ddlYGkO-85o5qgtAzLkLQCOx7oekR4b7wdDGB97oTkaFJMl0OySrTcK5IK_b_ljF6IK9Akw3HE_6Ac0OSKcJ_mxyOfhJgO6hhvowQC_7zpGe7EbkJ62C2tmQo3lCmwVKqs3MXBBdAvXUx1Ik2GOQdppAJ680TertEzlWBwDMdG962-qvP5nagaG1v-QA59nKgD__sKi_zZH_EtPzpIH0s9Ezxr1ghPsMeQldOkIECkFxPKVwTIbj9_z8BM18iVs6I207Jm8vhTkZUx-S9ChSZ0FhdlUe3AoJbgKqNeAilIs-El_VpFZD6U3-tTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez7HNQu9EoFHGFy7RyDDc0ZBpZZhGIjHfzPesbaNqT5tesnBR-dkkXVcz89Ij2ZPXYNyDvNpHjtRHT4Yaqgo1NkLcxnMgIPC9kyFmQH6yyGpjQ8i3h36YQzHKVFAeh0_ddUiEdYT9b_Q9MJn_IWHqr_7Xx4dHmJyaS8bAo3LV6-J7NZNfBz_Zo2Lj-jnB-IQ19lpxhupONakzl6dwqGebp380MupZ7Z5sU1ks8PRfAH-CdGBOiUH_io2BsCB2e6E7vvswKUVdAjXZ9W8frGc7vQPPk6O6Jz-z-zUFiGfYqvpYNwUHQQJa0h0xs8_bRxDYWiKg-B5e9AjljPrWl6hoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی یونانی که مورد هدف قرار گرفت، در حال حرکت در نزدیکی عمان بود و سیستم شناسایی خودکار آن فعال نبود. این کشتی پیش از این، در تاریخ ۲۹ جولای، با خیال راحت از مسیری عبور کرده بود که توسط ایران تعیین شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139807" target="_blank">📅 13:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139806">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4tMBlQrw3-RlDC9z9K5WPjBByk-cheSsPLAuY94rg3urFU9cNbX-kUx_61P2VkS23o6uGHLVfvkBUM3RnPjWshqYjoxx8vXyg32keyX0YDEvzQuzn-UnXsdadgnTVvxajQNXFgS1Ubn7ZRrn7hq4uy8IKD67sDffnaVOgEYFsvfs7zuCvu46FGrqyvDE_G3XcokJKMdN2dlB_R5VRWZnCakFNNA5UCeFuTAyg7mT4s0sYSF0aOcNiV-3_M2RaIJaGOFuh7QtjdiqU6hpxOqoyDBvrEUMWWpWwnGrD8NzcojrVIxIdyGWdotG2deXEdTpYJDM5lrQkGOSVKCs_mEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شعار علیه اسرائیل می داد اما جاسوس بود.
🔴
این مرد ‎إیلی‌ کوهین بود. مردی ‎تندرو و مخالف اسرائیل!
🔴
اما در اصل مأمور مخفی ‎اسرائیل که تا یک قدمی نخست وزیری سوریه رفت. در مجلس ملی سوریه فریاد می‌زد و اسرائیل را به هزار کار کرده و نکرده متهم می‌کرد، اما شب‌ها، برای اسرائیل اطلاعات ارسال می‌کرد.
🔴
شباهت نداره به بعضیا؟
#الی_کوهن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139806" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139805">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dArVkYrTauud3NcgkgzHwwrWcPQJrsSxS0Z9C8iYSGqvobHVzjvrwFW6VmKqVCNFDQcWWWBvaiWCFB9qJ7dCoCQw6uql5Xxt48ozHvcNn_cgT5XRZUNAz2O7QER2-xGAalRszkRs9WyAuKf-pK2uJTdtgCbisXq2XSDS0juJbP97wHPnzPzClKUJSZ9vdsJGUQX2KGMHNU7WiOAanX0gUpDCNISf9C5VS4eiMbJASWTPKpBYhYVuOet3ytca_VCM5ioY07xGEwyAcyMZ9kS2tmDmMDDnn5o_EnBGy7jzoneSuBLUROH4bSCtvo8jtxg1q72ZtGktqmMcHG1KbtEUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اظهارات عجیب محمد باقر خرازی: تنها راه نجات ایران ساختن بمب اتم و زدن بمب اتم تو دریای اطلس و اقیانوس آرامه طوری که تو آمریکا سونامی بیاد، هرکس با ساخت بمب اتم مخالفه با اطلاع بهتون میگم اون دنیا باید جواب پس بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139805" target="_blank">📅 13:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139804">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
دونالد ترامپ از ایران خواسته است حداکثر تا روز سه‌شنبه بر سر تنگه هرمز با میانجی‌گری عمان به توافق برسد.
🔴
بر اساس گزارش بلومبرگ، ترامپ هشدار داده است که در صورت عدم دستیابی به توافق، ایران با حملات هوایی ویرانگر مواجه خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139804" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139803">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIwMUoG7cLTmb0fziypH6-wHZjmRh2iq9WBem1KtnRCpbWSYW2BJdKasQkzJ7tJGoITjvMW_38S05BbgAfX-DGpmMGzq-rCoj8TjsmuYWr9WjxK0aye1_1Tog30GAqSRcl9Om5n87szDMKbNDgcEGZRK5I2R2iw8qXu-B4ZVi5xjtmP-nvHe6M7zvir0fUXczS3SQ6GM3TooaK028VHbD3ebUmzN0zqsEHpoLJL9b93wsNOhruc84Sq-oYjTTTEc7VsvZaFW_HUgCMWB_ErnGvY7UaTbt93PkwjNqoKC2X5isfv7honLdqEWNg1AoWaY2WdvXMMTKw1RKlmz67X2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / صدای انفجار در شهرک صنعتی شمس آباد تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139803" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139802">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رویترز به نقل از منابع امنیتی دریایی:
یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت موشک قرار گرفت؛ خدمه آن کشتی را ترک کردند و یک ملوان نیز مفقود شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139802" target="_blank">📅 13:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139801">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نعیم قاسم: رهبری آقای جدید(مجتبی خامنه‌ای) یعنی پیروزی‌های بیشتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139801" target="_blank">📅 12:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139800">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نعیم قاسم، رهبر حزب الله لبنان:
دیدار بین حزب الله و دولت سوریه هیچ مانعی ندارد و این دیدار در زمان درستش بر اساس روابط دو طرفه انجام خواهد شد.
🔴
یک سوریه پایدار منبع حمایت برای لبنان است و یک لبنان پایدار هم می تواند به ستپن استراتژیک سوریه تبدیل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139800" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139799">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7yEYJm0fhlBGJVX-hnvOk3dtZWTYVoTMwFSyGEeCCkQUrPLVaKkAHo3xNODL3pvkuXb72jLbFSauX5ELn79fsABrOsvbmNXqKE9uDgmitQygWMjq0v5-p2xBZz8f-BdjDmlK3pQnZwjpo-o9eFtvjm5K0yTmbn32EbsmhS14NlInTdMKRxQmw6Ycj9UNdJgP81IEO8D9mqVlo-6xobILwNVti8HHo5Q9nIvMHmD8v-UW7fCcvHOJqD1ETAsxa80ex7CMMv1AsHYdP5JKwbK1gBC_YZKpCACOLNbmdQkRJmm32s61F0usuIdv6wp96lNzMwnch5gm312LRouNTMD2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اگه‌ توی گوگل سرچ کنید «پدر استعفای ایران»؛ با همچین شاهکاری مواجه میشید.
✅
@AloSport</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139799" target="_blank">📅 12:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139798">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a783e28.mp4?token=jKEZhGHt9pjpUtIZ9hC_WplXEr9OQfQoboNviQ55s_NYc3PXhFngqtgnsKIcdBhy1uxgpZwOfNoELRIhua0Jt5FtFwxhM0xYwZMg33BgFHJC_S110p-hUjZ4xHSkhaRAluZ6NJJw-e-tEuizByCvHFUOUlf7QfoO8yiwBjmGYKVx8jCITdc1QC3_VX3e2vAPMTzQXllcOBqE22ZgYGDx2jmLfHxDr4Gcf-x63W1RZVRddX4a0fyt9VnjtNzuAEXw-0hfJjSV0SmjFxJbOtL-rZ3PidOLpGZnH_M2Q4q70ULaOa8fCmJYxoE_knv4srmuVwsZPLobGgF3qZeoRLB6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a783e28.mp4?token=jKEZhGHt9pjpUtIZ9hC_WplXEr9OQfQoboNviQ55s_NYc3PXhFngqtgnsKIcdBhy1uxgpZwOfNoELRIhua0Jt5FtFwxhM0xYwZMg33BgFHJC_S110p-hUjZ4xHSkhaRAluZ6NJJw-e-tEuizByCvHFUOUlf7QfoO8yiwBjmGYKVx8jCITdc1QC3_VX3e2vAPMTzQXllcOBqE22ZgYGDx2jmLfHxDr4Gcf-x63W1RZVRddX4a0fyt9VnjtNzuAEXw-0hfJjSV0SmjFxJbOtL-rZ3PidOLpGZnH_M2Q4q70ULaOa8fCmJYxoE_knv4srmuVwsZPLobGgF3qZeoRLB6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش رسانه‌های ترکیه یک کشتی باری این کشور در حمله‌ای که ظاهراً با پهپادهای اوکراینی انجام شده، در نزدیکی بندر نووروسیسک روسیه در دریای سیاه هدف قرار گرفت و دچار آتش‌سوزی شد.
🔴
بر اساس اعلام اداره کل امور دریایی ترکیه، ۲۲ خدمه سرنشین کشتی بودند که ۱۳ نفر آن‌ها شهروند ترکیه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139798" target="_blank">📅 12:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139797">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
جروزالم پست به نقل از یک منبع آگاه مدعی شد امروز سپاه پاسداران ایران به یک پایگاه نظامی آمریکا در کویت حمله کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139797" target="_blank">📅 12:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139796">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دور جدید مذاکرات لبنان و اسرائیل در رم آغاز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139796" target="_blank">📅 12:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139795">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
حاجی دلیگانی، نایب رئیس کمیسیون اصل نود: هر نوع توافق با عمان درباره تنگه هرمز باید به تصویب مجلس برسد
🔴
افکار تیم وزارت امورخارجه در دوران قاجار گیر کرده و از روی ترس و وادادگی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139795" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139794">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
زلنسکی: جنگ با روسیه باید قبل از آغاز زمستان پایان یابد
🔴
رئیس‌جمهور اوکراین، در دیدار با سفرای این کشور، اعلام کرد مقامات اوکراینی تلاش خواهند کرد تا درگیری نظامی با روسیه قبل از آغاز فصل زمستان پایان یافته باشد.
🔴
او گفت: ما بسیار تلاش خواهیم کرد تا این اتفاق پیش از زمستان و در پاییز امسال رخ دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139794" target="_blank">📅 12:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139793">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
یک منبع بلندپایه به العربیه: سفر وزیر امور خارجه ایران به اسلام‌آباد به‌زودی انجام خواهد شد
🔴
درباره دستیابی به گشایشی در مذاکرات میان آمریکا و اسرائیل، خوش‌بینی محتاطانه‌ای وجود دارد.
🔴
فضای مثبتی درباره توقف عملیات نظامی و همچنین ترتیبات مربوط به بازگشایی کامل تنگه هرمز وجود دارد.
🔴
میانجی‌ها برای دستیابی به اعلام رسمی و قریب‌الوقوع آتش‌بس، به زمان بیشتری نیاز دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139793" target="_blank">📅 12:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139792">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر دفاع یونان، دندیاس : ما می‌خوایم شرکت‌های دفاعی اسرائیلی رو تشویق کنیم
🔴
تا کارخانه‌ها و واحدهای تولیدی خودشون رو در یونان راه‌اندازی کنند
🔴
این کار باعث تقویت صنایع دفاعی یونان، انتقال فناوری، تولید مشترک و افزایش توان صادراتی کشور میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139792" target="_blank">📅 12:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139791">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
‏
🔴
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139791" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139789">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
روزنامه روسی ایزوستیا: آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139789" target="_blank">📅 11:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139788">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بلومبرگ: حجم تردد کشتی‌ها در تنگه هرمز همچنان بسیار کم بوده است، زیرا حملات به کشتی‌ها و تهدیدهای ایران، نگرانی‌های امنیتی را برای صاحبان کشتی‌ها و خدمه‌های آن‌ها که قصد عبور از این آبراه را دارند، افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139788" target="_blank">📅 11:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139787">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c173297d17.mp4?token=qleKx5-hACh-Wt1mGuw9ceQTHPC9hVlVLy6sq3KzLLsact75rx5rL_270gFkvAQFRVB16-rzTuvjMntiXAs9OY2ZfeuUilkgyxRE1BvKmSbf7jQhGYOKHKrPf5MKbS9G9uE0xAj3Dl9cbiTPurqPAKUrU4CvEnNh7qjFYqTF48OymhGpl7nFUgvIMSsQpW3Z0RT34Tf9Bq5sRY7DHU6cBYlbTxRZlUUFnp0ZEgNuqnPAYNm4KfWJzHznP8DXsCxYUxwBTxifQhw1Ff1aM9YtT724CvHd3xg819tljTb6AkGHWdLCE_ZZOgMcUdmjvA_ivDxf0TcCO_Tg5XBbXEQxTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c173297d17.mp4?token=qleKx5-hACh-Wt1mGuw9ceQTHPC9hVlVLy6sq3KzLLsact75rx5rL_270gFkvAQFRVB16-rzTuvjMntiXAs9OY2ZfeuUilkgyxRE1BvKmSbf7jQhGYOKHKrPf5MKbS9G9uE0xAj3Dl9cbiTPurqPAKUrU4CvEnNh7qjFYqTF48OymhGpl7nFUgvIMSsQpW3Z0RT34Tf9Bq5sRY7DHU6cBYlbTxRZlUUFnp0ZEgNuqnPAYNm4KfWJzHznP8DXsCxYUxwBTxifQhw1Ff1aM9YtT724CvHd3xg819tljTb6AkGHWdLCE_ZZOgMcUdmjvA_ivDxf0TcCO_Tg5XBbXEQxTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی به یک انبار بزرگ شرکت ویلبریز در منطقه کراسنی بور واقع در استان لنینگراد حمله کردند که این حمله منجر به آتش‌سوزی گسترده‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139787" target="_blank">📅 11:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139786">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyaqLfT6Ru8wfGD0Mg5hGxrezDOH9z7zmw_ZPkNZjkVRySoE4Q4i-Ervj0JoovMFbEnLiQMVh5wvQ1JKVfYgPqdu3hPqeiFBeHrrLcLM_21fkJ5vXlX51wH5ijcDbH1ituD5uaoPxRD2WPopDPcN9OqmZqcmdvjV28Lei4w6K4uMueHE1UquUFIMUh2qoDiAJzVHbwAGCRePDWT_aUHCO4IduLayF1bKforAEP2Homtt7ADw-txIrqVrvX3IIxdDjmX0ur6_G6KZUXsC3fVGw3b9vdKmjwRXlawi6BaXIjO8rzT6wC4ShDETCbfWy0-g4RHlcnBmelWFy3-6AV7jMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مایک پمپئو، وزیر خارجه پیشین آمریکا: محور روسیه، ایران و چین، اکنون به واقعیتی تبدیل شده که تهدیدی برای جان آمریکایی‌ها به شمار می‌رود
‏
🔴
ان‌بی‌سی مدعی است روسیه در جریان رویارویی نظامی میان آمریکا و ایران، اطلاعات الکترونیکی پیشرفته‌ای شامل داده‌های شناسایی ماهواره‌ای و اطلاعات سیگنالی در اختیار تهران قرار می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139786" target="_blank">📅 11:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139785">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
دبیر کل حزب الله، نعیم قاسم: تفاهم ایران و آمریکا، اسرائیل را مهار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139785" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139784">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1aa3d91bc.mp4?token=OsDT2_wiOrQE3RFxqDi2rudErkU5WmRwtl0FTmba5pDkxKMytY_jrI724IAgAXhgHAVwjWLwnFqPsPCBE3jNYbnjGFmbdzWsgONAUV4dkQmQd9IShOX-JaO5HGeSyXiOjBq-sngQ-4MnCkwDfHtjmIQ1SqbIm4aWnej1dMguDmObs1vr7QAFQGlDlNX95LVuq80-3_uSElcoSIrRrNCtN0N4_8FlflMesk0vxAzbTGW18JD9fAvAYpfqA3WbyeSwdVynZBk8YNI_hLCD9TMpSGzNwLjAIch9BVtnLMDLl03xpBkqtp_fYpA9uM7krY9TI9dDh7NfuYEnvRZ9CRaP_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1aa3d91bc.mp4?token=OsDT2_wiOrQE3RFxqDi2rudErkU5WmRwtl0FTmba5pDkxKMytY_jrI724IAgAXhgHAVwjWLwnFqPsPCBE3jNYbnjGFmbdzWsgONAUV4dkQmQd9IShOX-JaO5HGeSyXiOjBq-sngQ-4MnCkwDfHtjmIQ1SqbIm4aWnej1dMguDmObs1vr7QAFQGlDlNX95LVuq80-3_uSElcoSIrRrNCtN0N4_8FlflMesk0vxAzbTGW18JD9fAvAYpfqA3WbyeSwdVynZBk8YNI_hLCD9TMpSGzNwLjAIch9BVtnLMDLl03xpBkqtp_fYpA9uM7krY9TI9dDh7NfuYEnvRZ9CRaP_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشر شده از فرودگاه رامون اسرائیل حاکی از حضور بیش از 40 هواپیمای سوخت‌رسان KC-135 و KC-46 در این فرودگاه است
‏
🔴
ده‌ها سوخت‌رسان دیگر آمریکایی در فرودگاه بن‌گوریون،حیفا و… هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139784" target="_blank">📅 11:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139783">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اسرائیل به شهر کونین در جنوب لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139783" target="_blank">📅 11:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139782">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adlxQ_pxGbtzgMgM-HkDAKPL7M2aIeVtr9-JU7I3GYKu1LunsdvEOf9Km_s3O8DvoWkr98mO-d_r46ric64iMgI95IfQ5SQqZJg5TZ9AbWDKaAyh6u4e3HdcQ0xVTmNsqs0dYv7pZ6tOVw87P5A5U6tMNUTm7Av47gqxJSg5V1Km2xaEcxZp92shCXR7nG6a_JnLOzp_h_9JA6FP8FTmKhsoTKllRs8Rtxud4fGvO2sGAmlKRKY6kz8Jn3MM30l_En15STLp28lFD6uunLkiJ2j_KUmn5zpLZrT4z5SoL73--nLaLjZEyRyA4_S8sgkhtQIKK91rwT5XDWC3cs5ipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت ۸۴.۴ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139782" target="_blank">📅 10:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139781">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPf5Mw6jZLAKJK-BDKwLQO7OAtIng9HX9lHaRUx7t9x5HSTC5_O66UlcQ1l1nT9oB3FnD5fq6CojMf0gcpRTRfZ-UKNZQS-2OGe4lKe_lBLIyHjMu_ME6v_DqvK2MDOztQ2zG_qe0YS6HQt3sMYaNPOwESTxezRbLUmQT9UPV06U3RE0hzL4MsVWIpb_d4AIzQ7NNwn4twb3_H3a_Kd0OtgPgumWfIf0bi2C1G97tnLnxKxxeC8bAoOOyrcKuJenaVPWK_qg0fBSfUo1QsjJ59DaAaupV5PtTHv0ek1CAENXZaaFs1XLupJp9vg6eJBdtmevY6QlE642pPjbhXPgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139781" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139780">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfbXCPA68jefEhFiZrWmlW0QzN00sRhnCkGJKedz2PBsLA7nhfVVml29eJPFfs5W0Ysv06ox51I4LoZ_4ARtf6HTgzgYu8h8zqElUoAGjsGrCsWjgaWR2pEbbx2Dpribu3eqpZlYE_6cnOtAd5IBnoce8HYN3ZbtiEM35ggxGWhmKxFcu4cnFVJBZbbINh4IKCDCBeVOAU7H3twlPm_0i7BN00wgmPLC2WAiQe03yeTHq2koK_CvlQD__nzKDg5xqZtj5xvNOrB1g7uGop2N_WUD2nGACkli00VxI3p81O-BzsTPI7jI0hmaWAKOlPryIrR2fMwaIw1bfKGF5KvE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرکل حفاظت محیط زیست مازندران:
یک فقره حریق جدید در محدوده پناهگاه حیات وحش و ذخیره‌گاه زیست‌کره میانکاله رخ داد.
🔴
از ۲۶ تیر تاکنون در مجموع ۱۰ فقره حریق در میانکاله رخ داده است و تداوم این وضعیت، فشار سنگینی بر نیروهای عملیاتی و ماشین‌آلات موجود وارد کرده و بخشی از تجهیزات را از چرخه عملیات خارج کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139780" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139779">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPl-nC0ApxTx6Mbhd5Dm_aHpzOQ4W4LmBNDPgehO5dtaHOd7dE0P1N7GzFfllYff8GzVlNUzW2kXGtYozPBi4gPSZmbUNCgwJdE7SJfhXx_DWm6cCQSiNp9465W9mTjFiEXlrSJKjppWfOJrzqZ9Yivcawst92YTsKlZIZtctEzFJ_Q0ZIiFKVewCKnhba8r4Y9DGJevbwSGSioDLl8d0M5jfBd8CrLaL0H9GBA3D7sPoEuhipdRdwbb-yLcCZ_GOFbAqMlNgoMZbLk6sFiBRsAq46bxzFQab2E1Icpyn2f3ccn0gNQcZmP4PvPl0xhvdn0tG0ZdpVd9a-JM4ZdsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهپادهای اوکراینی بامداد امروز به پالایشگاه نفت سیژران در روسیه حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139779" target="_blank">📅 10:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139778">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d32c2045.mp4?token=LXA0iBwwF65XyV7etwa301HLrjPtyi_lIP_cskLIGr_GeQEU_aEwOYZPpExxaK3wY0n2zaHm5HEroXpT8ulUKwMl3tgzo98UlDxsaop34Fegt-t_pVDZ9yAfIz2WVcbkL6J2spktTJ3qtBbJhJVhPFie4JF9utj1gBRUy00DDK_uo0nkeVMtpLyervi8DpDkoARcEeZeJa4SEmhA37EByVNT9kVhCkwqAljVxtM5GPb7IudkEZP38OGoQ2-uLfQZZ3kzp1zJ_AVsOkniMybmqD8o9HQ1w1rnRLipYSuhed_Mi871OUM4jCBJdsSTaBUqqYDswq6UWQz6LTWquw_Uvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d32c2045.mp4?token=LXA0iBwwF65XyV7etwa301HLrjPtyi_lIP_cskLIGr_GeQEU_aEwOYZPpExxaK3wY0n2zaHm5HEroXpT8ulUKwMl3tgzo98UlDxsaop34Fegt-t_pVDZ9yAfIz2WVcbkL6J2spktTJ3qtBbJhJVhPFie4JF9utj1gBRUy00DDK_uo0nkeVMtpLyervi8DpDkoARcEeZeJa4SEmhA37EByVNT9kVhCkwqAljVxtM5GPb7IudkEZP38OGoQ2-uLfQZZ3kzp1zJ_AVsOkniMybmqD8o9HQ1w1rnRLipYSuhed_Mi871OUM4jCBJdsSTaBUqqYDswq6UWQz6LTWquw_Uvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حجم آب پشت سد کرج در مرداد سال گذشته و امسال
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139778" target="_blank">📅 09:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139777">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oC6-ktCfsgBVZlMMUW_RhQMJ1z_xMrobGCpX7KnYUxSL14LOFOVZzGdrSnvi236lt8avZ0Icg0qQB83UcyIoDTLAZ8TaF9ebAX-I9gD6jns0WvipRHiSMIMnlTSzCgOKR2L3xF8KWiPvb7L-1dO5h9tKl5eNCI64k5esXm_mEquy9x-mxDfepA_22vphVF8muaBELc3YIyEchvD95vlDJji4Lj_BTx8I_jx_NaVeIrsEf8iYmrmIJRY8pMYDEkQyWTY_DGOLv-iBeakdaBMSimAd2bekMfPO9lnhHCfczA_sBNxgyWqETIcPEKx7xSw9YzXTTk-4bvd2lWD6EHvotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت اپل اعلام کرد پس از آنکه در یک بررسی مشخص شد محتوایی مغایر با قوانین این شرکت در رابطه با «ممنوعیت سوءاستفاده جنسی از کودکان» در تلگرام قرار گرفته، این پیام‌رسان را به‌طور موقت از «اپ‌استور»، فروشگاه نرم‌افزاری اپل حذف کرده است.
🔴
به گفته اپل، پس از آنکه تلگرام «محتوای متخلف را به‌سرعت حذف و حساب کاربری منتشرکننده را مسدود کرد»،  دوباره به اپ‌استور بازگردانده شد.
تلگرام نیز در واکنش به گزارش‌ها درباره حذف این پیام‌رسان، در شبکه‌ اجتماعی ایکس نوشت: «گزارش‌های مرگ من بسیار اغراق‌آمیز است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139777" target="_blank">📅 09:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139775">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پزشکیان: استعفا نخواهم داد و خواهم ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139775" target="_blank">📅 09:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139774">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e764948ea9.mp4?token=o99PYqQGyZ0hI1_uqevXLLh6xnE-Ok1UcbPDGyronHqXqbcTGZ_ZpwzDzL8vQMxgZkBs5bP798wFAhUdpxogCt6w3RSheTt9kKAx4gESjtSVyydOEMEJLmJxUrklZTHCZySg9nOVVYrcBTMa9Vaj_i7o0ZoeBUorNxf6B7EP4qt_71RF-hvnlUw2ed0EtVP-VH1yfjWVNoSCYM36S3stZKscZtBT_cxN-stHJqPqc2JYm48aSSQrJSdwH1SfIWenPr6N5RAR_mMsSt8Pauida-Z2d-z8_sz1_7n_RIj34Nitw0j-S2YHi9YmqTkpO70xa3jdQWxiSKxggnl00l7e4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e764948ea9.mp4?token=o99PYqQGyZ0hI1_uqevXLLh6xnE-Ok1UcbPDGyronHqXqbcTGZ_ZpwzDzL8vQMxgZkBs5bP798wFAhUdpxogCt6w3RSheTt9kKAx4gESjtSVyydOEMEJLmJxUrklZTHCZySg9nOVVYrcBTMa9Vaj_i7o0ZoeBUorNxf6B7EP4qt_71RF-hvnlUw2ed0EtVP-VH1yfjWVNoSCYM36S3stZKscZtBT_cxN-stHJqPqc2JYm48aSSQrJSdwH1SfIWenPr6N5RAR_mMsSt8Pauida-Z2d-z8_sz1_7n_RIj34Nitw0j-S2YHi9YmqTkpO70xa3jdQWxiSKxggnl00l7e4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک خودرو در غرب غزه هدف قرار گرفت که منجر به کشته شدن دو نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139774" target="_blank">📅 09:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139773">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ادعای نیویورک تایمز: ایران و عمان به توافقی در مورد تنگه هرمز نزدیک شده‌اند که بر اساس آن کشتی‌هایی که وارد تنگه هرمز می‌شوند از مسیر ایران عبور می‌کنند و کشتی‌هایی که از تنگه خارج می‌شوند از نزدیکی عمان
‏
🔴
این توافق شامل هزینه خدمات (نوعی کمیسیون) برای ایران می‌شود.
‏
🔴
طبیعتاً تا این گزارش‌ها توسط مقامات ایرانی بیان نشود، مورد تأیید نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139773" target="_blank">📅 09:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139772">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae3de193b.mp4?token=WfLVwgT4d5_nkRAHXBi3ziZ1cbNXNkEfZIbYvVLhTx7FpDG22P-z9ChZnsSm91QxBW5LxbFf7t5jpN_5neNS-cd0gNpJnIPo90aIU1R7LsuRHhtQa1-IaH-GX0hg600uuLU8JictMpbVOdrZONiEAfMmI3FE5Dmvwn1lp3XQJz4b08EnkDyIXG3nK0lNp71kZlMKtplrNSnwKWhttCGsRWiWiDUR-bBAFGb0MZuVA4A1mIqBzRbMHP-GQaRkH8ZyGu2juEXRRo2JOPgX7JLKqyOAnFayTYCAmgl3OAOOVJhOL5k-HpJHB9Ph5rkoH_a-BuC5gANfu5ctuOyhRTm5_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae3de193b.mp4?token=WfLVwgT4d5_nkRAHXBi3ziZ1cbNXNkEfZIbYvVLhTx7FpDG22P-z9ChZnsSm91QxBW5LxbFf7t5jpN_5neNS-cd0gNpJnIPo90aIU1R7LsuRHhtQa1-IaH-GX0hg600uuLU8JictMpbVOdrZONiEAfMmI3FE5Dmvwn1lp3XQJz4b08EnkDyIXG3nK0lNp71kZlMKtplrNSnwKWhttCGsRWiWiDUR-bBAFGb0MZuVA4A1mIqBzRbMHP-GQaRkH8ZyGu2juEXRRo2JOPgX7JLKqyOAnFayTYCAmgl3OAOOVJhOL5k-HpJHB9Ph5rkoH_a-BuC5gANfu5ctuOyhRTm5_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طراحی پرچم‌ های لبنان، عراق و ایران با استفاده از گوجه، خیار و... در موکب‌ های عراقی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139772" target="_blank">📅 09:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139771">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزارت دفاع روسیه: 4 کشتی باری را در بنادر نیکلایف و یوژنی و همچنین در دریای سیاه هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139771" target="_blank">📅 09:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139770">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
بر اساس گزارش تاس به نقل از استاندار مسکو نیز در پی حمله پهپادی اوکراین به منطقه مسکو، 5 نفر کشته و 6 نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139770" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139769">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5f722d89.mp4?token=n2sVEU20yRylFSzY9SSmazH9Figzr3FIKZ8NAGlVFoiTckJmR57sDfhjuueS9WuVnhtz4I0yv4WOIVY9FUxZjnFfcrgMHWDctg91Uco_J4OKny4xrj8Kb3qWH3LCwZU5A3Zj6z9sIkqnPf8uYeKuTDWO_DpjDC1y9DWGd3e2oe_V_yP5RrGhCvJ-br4h1Ni77xlI4ZlUQ7xJc_iH_AQcuWXkncfEiNZlKWvFfQje7lL4-iV827SGsTsL2Qj31Req9nhCfuuthCsOQXOwA0U0KyVva4Wwe6PiO1f2hr81ug6a_zDUAozB2R1ubros9IMyRD07rdGoHiTst19cdSYIWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5f722d89.mp4?token=n2sVEU20yRylFSzY9SSmazH9Figzr3FIKZ8NAGlVFoiTckJmR57sDfhjuueS9WuVnhtz4I0yv4WOIVY9FUxZjnFfcrgMHWDctg91Uco_J4OKny4xrj8Kb3qWH3LCwZU5A3Zj6z9sIkqnPf8uYeKuTDWO_DpjDC1y9DWGd3e2oe_V_yP5RrGhCvJ-br4h1Ni77xlI4ZlUQ7xJc_iH_AQcuWXkncfEiNZlKWvFfQje7lL4-iV827SGsTsL2Qj31Req9nhCfuuthCsOQXOwA0U0KyVva4Wwe6PiO1f2hr81ug6a_zDUAozB2R1ubros9IMyRD07rdGoHiTst19cdSYIWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از سیلاب در شهرستان راز خراسان شمالی که موجب قطع کامل دسترسی مسیر ورودی و خسارت به زیرساخت ها شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139769" target="_blank">📅 09:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139768">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رویترز گزارش داد صادرات نفت خام آمریکا پس از توافق صلح با ایران به ۳.۶۶ میلیون بشکه در روز کاهش یافته است. به نوشته این خبرگزاری، افزایش عرضه نفت خاورمیانه به بازارهای جهانی پس از این توافق، از عوامل اصلی افت صادرات نفت آمریکا بوده است.
🔴
بر اساس این گزارش، سهم صادرات نفت خام آمریکا به بازار آسیا نیز کاهش یافته و از ۵۲ درصد در خردادماه به ۴۰ درصد در تیرماه رسیده است؛ موضوعی که نشان‌دهنده افزایش رقابت نفت خاورمیانه در بازارهای آسیایی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139768" target="_blank">📅 09:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139767">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سنتکام شمالی یک سامانه موشکی هیمارس را در ۳۱ جولای به نوم، آلاسکا، در چارچوب عملیات توندرا مرلین مستقر کرد.
🔴
این استقرار که با پشتیبانی یک هواپیمای ترابری C-17 نیروی هوایی سلطنتی کانادا انجام شد، با هدف تقویت توانایی‌های حمله دقیق دوربرد و نمایش قابلیت استقرار سریع نیروهای آمریکایی و کانادایی در سراسر منطقه شمالگان صورت گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/139767" target="_blank">📅 09:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139766">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سیلاب‌های اخیر در افغانستان ۲۹ کشته و ۱۲۹ زخمی برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139766" target="_blank">📅 08:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139765">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTsCDQL-oRHzloHOCXuxGt2io_jfe6pIpPY6IGn9kJalkRLwKs1QTuTPuKIz4J-E9AiNaBTrWvSPYCEHES1aPTS_-My0smLfwI7mi-fgrtwtUK0tz6Li5lUvNGDz7fMS4JRSDjX0t_7Sz2vKqkoBQy1ixJLwuPV122eQXkAQTxiEGf9l-8FqYUjrXFYbsMdI8HRVqUwRIVBKouhdjKRpbINDLbKyzDBzf1AuFnNN-rbaUr_aNeZEXdD-I8AK_suDGAQgFs5-r2NT2pQq1RmGhcazsgVVrrgIJRYI4rcvZIU88K9jyhALK8CuEWuYug9nNYNzAdhgg6ybwIFd9rqitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیدآبادی، روزنامه‌نگار:
اسماعیل بقایی اگه سخنگوی یک نهاد نظامی بشه به نظرم براش زیبنده‌تره
🔴
اجازه نمیده آب از گلوی یه خبر معطوف به حل مشکل جنگ پایین بره؛ درجا میاد اونو تکذیب می‌کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/139765" target="_blank">📅 08:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139764">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45090a2b37.mp4?token=kosPC6sd1hqtjAsKzQeOCLonyWQwCVW-A6Yae-30oHiEwa7Yo4hnRtrPpEo0iKc8FadTVooM5N0SHq79QjBvjFwwRFuaTmInSqy7-SpgdE3fIPUuUu9YvohwCr5tjJOllKcIspTdFUVwY3DX0O5TwbsYjsKFYYrah_P5DEAlRpzJPHUE5lZUt4mZiBon04ICFTp_ujiHmu-7yGOx1vxb7cWPX1JV03vIf2zHf8OxHGWXe_Ia44Ldm6rhWfI7rEfhROSDb5B-_PMMvNuLTHTksGgwLgg3cJjG_56wFGK9OObPdGA-5T1kVngzR5tInX-0NrdJ5FPOH51nedFbElaQ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45090a2b37.mp4?token=kosPC6sd1hqtjAsKzQeOCLonyWQwCVW-A6Yae-30oHiEwa7Yo4hnRtrPpEo0iKc8FadTVooM5N0SHq79QjBvjFwwRFuaTmInSqy7-SpgdE3fIPUuUu9YvohwCr5tjJOllKcIspTdFUVwY3DX0O5TwbsYjsKFYYrah_P5DEAlRpzJPHUE5lZUt4mZiBon04ICFTp_ujiHmu-7yGOx1vxb7cWPX1JV03vIf2zHf8OxHGWXe_Ia44Ldm6rhWfI7rEfhROSDb5B-_PMMvNuLTHTksGgwLgg3cJjG_56wFGK9OObPdGA-5T1kVngzR5tInX-0NrdJ5FPOH51nedFbElaQ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: ما از حد و حدود خودمان دفاع می‌کنیم، اما به‌دنبال گسترش جنگ نیستیم
🔴
باید تلاش کنیم در این اوضاع و احوال، جامعه‌ای بسازیم که دشمن در آن طمع نکند، وارد آن نشود و نتواند این مجموعه اجتماعی را تکه‌تکه کرده و از بین ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/139764" target="_blank">📅 08:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139763">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏
👈
منابع عربی:
چندین پهپاد انتحاری به سمت شرق و شمال کویت شلیک شده است و سامانه های پدافندی درحال مقابله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/139763" target="_blank">📅 02:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139762">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
روزنامه روسی ایزوستیا:
آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/139762" target="_blank">📅 02:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139761">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل:
کانال‌های دیپلماتیک ایران عملاً از کار افتاده‌اند.
🔴
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه پاسداران، اکنون سیاست رسمی آنها است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/139761" target="_blank">📅 02:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139760">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af4929d98.mp4?token=Rgh2ksn4wBl3RA-q6D_nK5o5HphhkROS7YirgHsIVKSXZv28V22xA8LF6uX7aLOmMR-dho55FPBRJ4evziPyQaWv-uCx3sxcgWrU0PVtpXlKI9MJB15iXEOtC7WyqAdHes-qFMSMaYJtrRXGbYkFdQ_UKTbaP-MCzN3jfcpqqSnYndOpG9QEqIJulDQE3V1nfzlrM415dlBDXjYH3iryI2cl4H7aN9AljS8P8Xt2M1ai8Ss0l8-jDB0dgZjquJtlIZN_4dCASrNmLjO7WQ_x3R-Q2B1C53HssErlOyVf6n3cNL2eDUZ8vR8n_NVfn41ba_j614zhnIbINyRbGJza1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af4929d98.mp4?token=Rgh2ksn4wBl3RA-q6D_nK5o5HphhkROS7YirgHsIVKSXZv28V22xA8LF6uX7aLOmMR-dho55FPBRJ4evziPyQaWv-uCx3sxcgWrU0PVtpXlKI9MJB15iXEOtC7WyqAdHes-qFMSMaYJtrRXGbYkFdQ_UKTbaP-MCzN3jfcpqqSnYndOpG9QEqIJulDQE3V1nfzlrM415dlBDXjYH3iryI2cl4H7aN9AljS8P8Xt2M1ai8Ss0l8-jDB0dgZjquJtlIZN_4dCASrNmLjO7WQ_x3R-Q2B1C53HssErlOyVf6n3cNL2eDUZ8vR8n_NVfn41ba_j614zhnIbINyRbGJza1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از یه درگیری تو ایران، انقدر وایرال شده که حتی رسانه‌های خارجی هم منتشرش کردن!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/139760" target="_blank">📅 02:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139758">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjK6kV0JxKMuf0LRM16Xuo2kicM5iut7d9JaijlGOfmS83-GJT6XqdQ_7aBy7wzBw8r4W7ZTdVzL3krW4Q0MdQrF3mnxZDjWoAuc6EfCR-BQ9GaD1E77Fb_sxUQxXY8XGWqhXWUAcPqNmEio52MFGN-fV4MsVSrR730SazrAtm-MuM1Iif2qPsl3E8zuWcM96GzooeX2rIt2UAn-ALnjzLNsyAT389p6tzG0FEmL8GtK2tlW0k5bWyeTSeB5IuU2evmeByQo-p49ynqiPUyolD6TxMpZkidgVqSob1szPx9fmazH92KPMAsvgpEi6g7YEGxgeVeZoq8VQobFrYoAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXOr1HRQKmxxWHXl356Y25NoWNZvCXuokHWxJ07VZUUrTprqux0OOmWnfsX-hogfxIyk5KdoWjemSBXZBHO6-7jX_8HAOw7aT6NMCmyC5p8mfqlV7El7tFUFck_v5jbaeSuMWt1K-rgIJpjlPdssEC8hKSn2x2labL-EEMGL-yQpFqMNBey51Xh-XayZVee3nPBUWid1A6yOf47p6sxbncU2JEAbDrddoa5bxNmWnX-vhbnFq7e2xlUge6NQ65h6a_w6w9Nz4wNQFVTMijKt6gTMcmpLjFXF-aHUtUruIGt0aZXVdXQzUzHA_TjSi_qLzhz2H9JxmeFLoqaG05RAwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صحبت‌های فیلد مارشال، دو کشور دشمن(روسیه و اوکراین) رو در خندیدن به یک موضوع واحد نزدیک کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/139758" target="_blank">📅 02:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139757">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzznuW1TwBJyFKH_V8aIjRC2sJGAZhBvI5NVdiyacX_NK_wwkiqHJCaBX6eqbb0eMBZYENaJKlGR_H66SeTrAALw8_jkk6QttoNnCANIYyin4i6PMGmUBizh-5Kd_A9kONZRj3dFJvacg99KrEyDUHtq0__u2tkDflDfaEVFkSMay_tyBtDAehcceF-_jJz1TaLgS_W2lj81fGbJt2682QMPaifokEwZQ7KXdfZqLH22cO4Z-oH9mQO8CZ0hL1rD1nh6KD79VR7D_4eF9FZJ2LOxMSiaQwZT4J45v2Qr-vJzh86AxjUHw2z21QESyntkvoJaRSIMFtjTtbpaIhdcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نسناس:
پزشکیان باید رسماً استعفا بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/139757" target="_blank">📅 01:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139756">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfOuMzk8-UqDJvFA_uHfcyStV-XtryxxQtOQuQpHflz2RZogXDy-oUpiv64OEj_usO9KCfKV3iawmJIUd81wEX7vSJljyogFBr6zyVTIFjET8nCkphIsHP3cY6zE3uT-tMc7Sm5gRxl_UCJeywhw_z0bpzNnoAg-4eDHqZtZf0BPjqc6f2CUZWD-kIReaqXCzDaR8AlkuhgO5jI68yQ5_J9gy1nVIzu9r96ok2Wq1DqEsxgpAR_EmMN9xxvmqa2cbAtsb1X7uxx2IYbPuw6YgKsu8DqlBKbVkwfnY_EkugupLalK5pOtOjogfD7E60uJF9lguJm_LDsbWzzC0JvqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اربیل عراق هم اکنون هدف حمله پهپادی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/139756" target="_blank">📅 01:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139755">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نیویورک پست: مسیر ترامپ برای بازگشایی تنگه هرمز ممکن است از طریق عمان بگذرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/139755" target="_blank">📅 01:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139754">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/139754" target="_blank">📅 01:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مدنی‌زاده وزیر اقتصاد: دشمن آرزوی زمین زدن اقتصاد ایران را به گور خواهد برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/139753" target="_blank">📅 01:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139752">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
تعداد کُشته‌های زلزله تو ونزوئلا به ۶۱۲۵ نفر افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/139752" target="_blank">📅 01:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139751">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhNjHltKSGvN5iR_4ai9IMkCGG3GJvrM9qhelKWkRnC-_iNnw39jodUM3SMPIezLSXMCvTetmN95OaPp4hAaVvjw2tapfhBtjCLaDRlA91kx2UXb7OqCbLc_6pVAUPVWlB46Xp4agqaExY-Ua5W4Z161JAgKMEEE8fMBhdtjhLJ08XSPxyWrEiCZLs3r1wneJn8UHTS9o_B6YfvsysM9-n6WavpP7xhN5lGCoxhnISXoaewx8SiWi7cBWoeleq_jb1JWeZpjUxcXr1LS6Glg8nr641s-6Zy463KIpwU1pi-rP8kpEOWFMX-jYcYiP8O3wpVT8zO8NBJnW2a8xQb6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکایی‌ها درحال حاضر ۱۹۳ هواپیمای سوخت‌رسان را در خاورمیانه و اروپا مستقر کرده‌اند!
🔴
این هواپیماها تانکر سوخت‌رسان، شامل ۱۶۵ فروند از مدل KC-۱۳۵ و ۲۸ فروند از مدل KC-۴۶ پگاسوس هستند و در پایگاه‌های مختلف مستقر شده‌اند.
🔴
بیشترین حجم این تانکر ها در اسرائیل مستقر‌اند و تخمین ها حدود ۱۱۰ تا ۱۳۵ فروند را نشان می‌دهد، که در فرودگاه های مختلف اسرائیل مستقر‌ و به‌طور مداوم درحال انجام مأموریت و تمرینات هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/139751" target="_blank">📅 01:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139750">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=Z7x3cK7Y9fdiXNSEWG2XcZXNn4H-ofUrmyHWs63jU6RMi239BuqRAIHMjjnziwVn_H9bdBe-A_ZGgmxvo8dpln34o9OLOBokQmFqAZyJSIBuYWLNinBbJEDp-8BpWJwdc4f8KVHbyv9giJ8blQMxh-Rj6INpiGJ8bJBCzaMhIygIwW38D_DVfioJ_cdweH_Dipfw-LN7w6QOIpFzjWt_l7sHmCiNUku6rJ2ALCRRW9CIrpv2-9UsEHoXMqSs2Gx-EZSoZpSRNBIYEDSKrzttZctJVU7ai0PSfzA0BX5R5UxsfrLL1tVarA82XZkdJnfqdGYoHpjKr5rz7Opq2IQ0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=Z7x3cK7Y9fdiXNSEWG2XcZXNn4H-ofUrmyHWs63jU6RMi239BuqRAIHMjjnziwVn_H9bdBe-A_ZGgmxvo8dpln34o9OLOBokQmFqAZyJSIBuYWLNinBbJEDp-8BpWJwdc4f8KVHbyv9giJ8blQMxh-Rj6INpiGJ8bJBCzaMhIygIwW38D_DVfioJ_cdweH_Dipfw-LN7w6QOIpFzjWt_l7sHmCiNUku6rJ2ALCRRW9CIrpv2-9UsEHoXMqSs2Gx-EZSoZpSRNBIYEDSKrzttZctJVU7ai0PSfzA0BX5R5UxsfrLL1tVarA82XZkdJnfqdGYoHpjKr5rz7Opq2IQ0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز گروهی از مردم پاکستان، تجمع ضد جنگ برگزار کردن؛ اما وسط مراسم یهو یه عده، یک حمله انتحاری انجام دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/139750" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pGJ1COZKLuM0UlRXi9IBYKy0geD_wQUgujG2gxqm9nrRdlUNn_yAQgWBpiAWqzb-KwmhYp17jm0KqW-Fe_6biso0yY_2ea54J4Sx6Rf8RmfDMavVRYEdbwNCQoBk3NDaSz2okqiUIYRFpwA9hfjUGuJ-O5m_BTVl7iHfWD4P40qur8uwuMOkdMdLmwm07udtSWrL712pffC_S51x5Jta62ZtVx2vIcGOPwHnhjv3WjAYsCLp65E0P-Edd8CSpKBvPSDeNXtmWvlrKWZpeP0ylZF7-sB1Glq6J6ujpgQsXG5dmYnVjzM-RXYJbwXpzdBhK_Vl5niZhceXD8CVryrNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WXbZ-Lupy6Lqb0Y8USPvLgc-iX40b2g5G0Pcp-0dASzAq-B9dCkEOYFR9Poa1Y2R5GCTENsSd5Hn4ajgUgadfCSXN8N1Oog0Xvxlqqh8rQ7rqklwOzAwqzNXQ-el4gvmqemmBkNysY9T4H4ulUixZmoWAE4XoCugNc9ygSdvdyEzj9cuaFo9GCS__U6zXVumHcHCSFcvn9WvA1N-DUcT8UwP019NOgPPhp6A7Jtz98XxrPrtWGyLiJ2luGkX_RsuPK5TVT0mKhBoZlt6h1ebXORUDM9anUiNC5TW0GEvRFru9jOvsmX-6NG5E_gE9pFqSAI9FBZV9MBKl0yQcnR5UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مهدی روشنی، فردی که این عکس را گرفته بود به اعدام محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/139748" target="_blank">📅 00:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139747">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4W2xHL6vmMDD5g4tbdQGlh7VntmhsbYq8tCTzrgeeFmAyuq0k5CrqFev8qUO2TWsQuZ__1zH0yYT6QQ6EPrST3URI0yGLRa1cR3TTVVdNnaaXA7VPZYIoBfDx0H76laHM1RrYrjrtJ8DW6-KRkvDjLfUf5Sgl44RjsaQsM6Lw31OaceKFS1CvQ_FcyPoZbBDkOXEWINt31fo8Ddv3iFQj0Rj-UY6YmPisd-HCXf93ZssGKUEXq2cj9GIRF0DvJCtYGZwWdnZqAlEP6eZTKfYItuEglDZY1TizjLPJAyAY89tD8BAG1A9Dc88G3--e_mgKGT_3a0HhO8-x2OnSk4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: این‌ها کودکان گمشده هستند و ما هیچ کمکی از سوی شهرهای پناهگاه  (Sanctuary Cities) دریافت نمی‌کنیم
آن‌ها حتی تمام تلاششان را می‌کنند تا این کودکان همچنان گمشده باقی بمانند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/139747" target="_blank">📅 00:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139746">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/139746" target="_blank">📅 00:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139745">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سازمان ملل: از تلاش‌ها برای توقف درگیرها میان ایران و آمریکا استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/139745" target="_blank">📅 00:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139744">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بیانیه قطر، مصر و ترکیه: از جامعه بین‌المللی می‌خواهیم که اسرائیل را برای پایبندی به توافق آتش‌بس در نوار غزه تحت فشار قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/139744" target="_blank">📅 00:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139743">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
الجزیره: ایران تعیین می‌کند چه کشتی‌هایی وارد خلیج فارس یا خارج از آن شوند
🔴
تهران همچنان کشتی‌هایی را که بدون اجازه‌اش حرکت می‌کنند، هدف قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/139743" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139742">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
صمصامی، عضو کمیسیون اقتصادی: با ادامه روند فعلی تا دو ماه آینده موج جدیدی از تورم در راه است !
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/139742" target="_blank">📅 23:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139741">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مرندی:ایران هیچ قصدی برای مذاکره با ترامپ ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/139741" target="_blank">📅 23:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139740">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMr4QcwPrdny77loWvtdXSZTkp3BOVBX8yNaWiOFZJXK4LqR74QvrpKSBdoQNpOxwEW1KnmxaGbk1yBAOdP8BdG-EB17XI06bdoYYKWI5QOdNsIjT1rdsmkthLJ3mRZ4UTd3ii9X9X5YVl0U5qkNhGD5V21wE0EOlullVgZEw44fDpTnV7XkfXgI6WwOXf8tLsqirZGO1RNisOlagxGKgmgkrjoagDVu8cWpj9D2BOad0A40wUUsCLLOlJywXtQMwxzz8irh7QcRGwX9_3_pcs14cyuWsKvHS_CZ9wKIQZVNlUxgFiVWV7olXUl3kF4JgVoa6aICfKwgg6E06mIKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی: اگر محاصره ادامه یابد، کشتی‌ها و نیروهای آمریکایی با خطرات و تلفات جدی روبرو خواهند شد. ایالات متحده باید رفتار خود را تغییر دهد - در غیر این صورت ما این را تحمل نخواهیم کرد. ما هرگز اجازه افتتاح یک کریدور دوم در تنگه هرمز را نخواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/139740" target="_blank">📅 23:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139739">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
الحدث: سفر عراقچی به اسلام‌آباد در آینده نزدیک انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/139739" target="_blank">📅 23:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139738">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a02fc078e.mp4?token=jcny5qpKeuRHJMku8KSeWAAn8onBom5XYRM7SeGePyis4-vhP_VdCYiQ6dKC2CsljY5WlN-LuhsLd1Nq0YErmvxK3G8h5adtWXs_ce-wdkF-aot_PW42BBcz7O8_gnkF-O7fmtHLXAMJG7h1AgYZ-7qnTBGVU3Gnv03zjdZm_oV_ytCXco0PLMul1w5Nlkxe1yHuvlw_PtRRTWKJVOoR3r8Z8mgNe3z0J6ITPExYTke9QiXlsb3K-mtouo8I8_env4FoxGHbj6-c2GWMpelxzcWDimzyy30FZ-uMdsR9TsEfVbOt9SVn6effpvoBMISjW5h6ENfb1iWxKeilsFKH9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a02fc078e.mp4?token=jcny5qpKeuRHJMku8KSeWAAn8onBom5XYRM7SeGePyis4-vhP_VdCYiQ6dKC2CsljY5WlN-LuhsLd1Nq0YErmvxK3G8h5adtWXs_ce-wdkF-aot_PW42BBcz7O8_gnkF-O7fmtHLXAMJG7h1AgYZ-7qnTBGVU3Gnv03zjdZm_oV_ytCXco0PLMul1w5Nlkxe1yHuvlw_PtRRTWKJVOoR3r8Z8mgNe3z0J6ITPExYTke9QiXlsb3K-mtouo8I8_env4FoxGHbj6-c2GWMpelxzcWDimzyy30FZ-uMdsR9TsEfVbOt9SVn6effpvoBMISjW5h6ENfb1iWxKeilsFKH9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رابرت اف. کندی جونیور، وزیر بهداشت ایالات متحده: من واقعاً هر چیزی را می‌خورم!
🔴
من هیچ واکنشی از نظر تهوع ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/139738" target="_blank">📅 23:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139737">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0ce171f4.mp4?token=lBQbH7M9ikkAf2hegyWD7e0FNa_MNJ6HFygjIH1x64R6F1W1xDzrG2RN50k18f96yJQjus67I4ZHwQH3373HFz_t678LzaZG2gWtE_c5B05OOBM94so-vIVjnd3tONP_4s9jGGoj_-HQy3uhKaKFXCAuvVPSYVV3nbFIXWG5ISdPlQD499K0xtLsF_pjNPtt8-KT5rYrO9NNzCxBrEARnXf_WEe38RmIaUR4RciDC7To1loM2x0aazSxvAtEvG5GkCeSIX6-cdFj8geL0vs8NOR5Yb31NPHK-o18h-e04P0MT7j-Hxg6zPyfHgmSQx-xOUsRex_tJvgKbeb1cXKKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0ce171f4.mp4?token=lBQbH7M9ikkAf2hegyWD7e0FNa_MNJ6HFygjIH1x64R6F1W1xDzrG2RN50k18f96yJQjus67I4ZHwQH3373HFz_t678LzaZG2gWtE_c5B05OOBM94so-vIVjnd3tONP_4s9jGGoj_-HQy3uhKaKFXCAuvVPSYVV3nbFIXWG5ISdPlQD499K0xtLsF_pjNPtt8-KT5rYrO9NNzCxBrEARnXf_WEe38RmIaUR4RciDC7To1loM2x0aazSxvAtEvG5GkCeSIX6-cdFj8geL0vs8NOR5Yb31NPHK-o18h-e04P0MT7j-Hxg6zPyfHgmSQx-xOUsRex_tJvgKbeb1cXKKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدتی پیش، یک پهپاد متعلق به نیروهای دفاعی اسرائیل، یک خودرو را در نزدیکی ساحل در غرب شهر غزه هدف قرار داد.
🔴
بر اساس گزارش‌های محلی، دو نفر در این حادثه کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/139737" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
