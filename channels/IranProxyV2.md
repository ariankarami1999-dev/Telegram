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
<img src="https://cdn4.telesco.pe/file/ejz5K_dm0F3Ao4ICtmu-G43k6tF2uoLYTcth-Ch0D-zU9yaiUc81kbXkuA86a4xmpE5iNzKUiWZE4DBaL_ZitcWKzxHOMUlFwSvsrzdbJbo6-ouECoiUK8eAeem4xLVNYvUm4vxerJBak88Baud1bI08LL09e7fuqBMWKWqg9uNLaFRWP1Kcpyli9J_0pXTHvcuKD7Gn5eoeSs1x2dp8Q-D1n-WMHC_iBhiVJNlIZ4WkQX7-R2ykrJ4tDhV5WLMZXsDmlElIfu1Fg9tJBcgPHZQ41XuOdSKke4ls2j0TmVqX3FGimV8NNbAjKL7e59mExMmDgCkAQRrqFpC7CxctwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی</h1>
<p>@IranProxyV2 • 👥 1.36K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 21:14:03</div>
<hr>

<div class="tg-post" id="msg-82">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خستم مثل کسی که خستس
پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 43 · <a href="https://t.me/IranProxyV2/82" target="_blank">📅 19:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">علیرضا فغانی داور ایرانی احتمال زیاد داورِ فینال جام جهانی میشه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 74 · <a href="https://t.me/IranProxyV2/81" target="_blank">📅 17:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">همه چی به کنار برق قطع کردن تو اوج گرما به کنار
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 100 · <a href="https://t.me/IranProxyV2/80" target="_blank">📅 13:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شب آرامی داشته باشید
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 141 · <a href="https://t.me/IranProxyV2/79" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">و سوت پایان
مسی راهی فینال شد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 126 · <a href="https://t.me/IranProxyV2/78" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBijXlx_zloUUK3GENjGj0AQ-5SYXYi7Nlx6k8uT4Vxl2QxUYUQP5zXccnKtvhXFg76gXf_6ef8vi2H4ALVcXnxcUIC6JmkEZm-oTFrNxxuT7t5J6U3WLguXOAmYZl26pVsbhryZIitFIDs-kP-FQ7kelyK1_iBbMYDXox3u12smrsbyEA4SGo6vC-ijSJrE9prrH0OMYrpEJPbkMpNl5fSApN1emcOjgPAn14wPu6AGpNiLpPXwyXFpJQyeazEDjGQmjBza-jOy0EVvrpkGhitA94Uu56eTFOWht6_D5L2tTlQqU4JKGOE_Z15ZAkHuj5MaSAcK5ZFj1UPoNNFPCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی انگلیس - آرژانتین به روایت تصویر:
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 129 · <a href="https://t.me/IranProxyV2/77" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">میدونم پیام دادن نوبتی نیست ولی خب باید مطمئن شم تو هم دلت میخواد باهام حرف بزنی یا نه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 116 · <a href="https://t.me/IranProxyV2/76" target="_blank">📅 22:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-75">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گاهی لازم نیست چیزی را نجات بدهی،
توضیح بدهی،
یا به سرانجام برسانی.
بعضی فصل‌های زندگی
فقط آمده‌اند تا به تو یاد بدهند
همه‌چیز قرار نیست مالِ تو باشد،
اما هر چیزی
می‌تواند چیزی از تو بسازد...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 135 · <a href="https://t.me/IranProxyV2/75" target="_blank">📅 19:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-74">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه ۲۵ تیر و شنبه ۲۷ تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
پروکسی
پروکسی
پروکسی
پروکسی
پروکسی
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 139 · <a href="https://t.me/IranProxyV2/74" target="_blank">📅 17:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-73">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگه هوا دو درجه دیگه گرم بشه انبه میدم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 146 · <a href="https://t.me/IranProxyV2/73" target="_blank">📅 12:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-72">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سنتکام:
محاصره‌ی دریایی ایران با بیش از 20 کشتی جنگی و صدها هواپیمای نظامی آمریکا، رسما از همین الان شروع شد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 191 · <a href="https://t.me/IranProxyV2/72" target="_blank">📅 00:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-71">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شنیده‌شدن صدای چند انفجار در اهواز
🔹
دقایقی پیش صدای چند انفجار در اهواز شنیده شد و تاکنون جزئیاتی درباره منشأ و محل دقیق این انفجارها اعلام نشده است.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 172 · <a href="https://t.me/IranProxyV2/71" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-69">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امروز روز جهانی قدردانی از گاوهاست.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 143 · <a href="https://t.me/IranProxyV2/69" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYQ_yO5innd2Fr-6ibbu7-IFxmG-FG-K1uQdNXNgyyh6-xN6c2az2XszMPIOh5hIvGlTHN-hpfiZMpUZLQNcEpgZyQt2XWyM_ouahZUoW2y_PRaOuqIixV5HKWUrduu_6jAv8-YA07JSPyW_sxcq_Z5hl5bjq7Rd6JPOjjrnCJfuJp1fqWI06qSe1lGZCVyvuYD1OX9jLJOOgN5Qe01p1L04lZGNBE0GKDvVHbUnEV7gCyqZNP87E6PeKjrqzYbcE8aMEQYQB6NOw2dbbtzJz0RtLnzPT8kiXgoOmVCBCFcjzv0BVz4TJyGfQswACaBigMk9j-7YswGcoNmi-A2rww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریوش فرضیایی به سوگ مادر نشست.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 183 · <a href="https://t.me/IranProxyV2/68" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اونارو میبینی اقای رنگو، مردم نمیدونن یک ساعت بعد نت دارن یا نه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 140 · <a href="https://t.me/IranProxyV2/67" target="_blank">📅 09:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XokZU5CrAmFhDmaM6Y26_sxag6T78zmLNe7m86RNkvxjSI6Yg8qGGPQOxubo4_J2KUnDVNr497OVMHk-EBaOyCApJ1IvNQ2dKj8n3gyTfu2rSqk0SkNww3YvfGhtUtWZervCYkvVXijMuzckK2S_WS-e9_HlBQ6KhaFezQ5d8h1adOb3ZpHpTHuum8XMr37LGz--0F_IkhReVNuoSatJeiOnAlxlmiz0BgRoTNU1UVfEkWmyrDsUVqcmEf5wFopAbXUgmLDjlQEK8_P3K4M1HhjJl5WVek19qVix4RX26ZojMtzpaX8zN2P8O8yaUIH4AyiZYe5me7kH-lJTCMGhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین:
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 170 · <a href="https://t.me/IranProxyV2/66" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-65">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">درد، یا نابودت می‌کنه یا تبدیلت می‌کنه به کسی که هیچ‌چیز دیگه اونو نمی‌شکنه
بزرگ‌ترین انتقام، موفق شدنه؛ نه توضیح دادن
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 169 · <a href="https://t.me/IranProxyV2/65" target="_blank">📅 22:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-64">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: محاصره ایران را دوباره برقرار خواهیم کرد
🔹
ترامپ مدعی شد: تنگه هرمز چه با حضور ایران و چه بدون آن، باز است. عملیات محاصره ایران بلافاصله آغاز خواهد شد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 172 · <a href="https://t.me/IranProxyV2/64" target="_blank">📅 19:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-63">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امیدوارم اون چیزی که الان خیلی نگرانشی
فردا یه "آخيش حل شدِ عمیق" باشه
گوشه‌ی قلبت.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 178 · <a href="https://t.me/IranProxyV2/63" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-62">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در پی بالا رفتن تنش‌ها در منطقه خلیج فارس، باز هم قیمت نفت به مرز ۸۰ دلار در هر بشکه رسید
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 183 · <a href="https://t.me/IranProxyV2/62" target="_blank">📅 11:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-61">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بهترین راه برایِ درکِ زندگی، نه تحلیلِ آن، که تماشایِ آن با چشمانِ یک کودک است.
کودکان، چیزی را که بزرگسالانِ “عاقل” از دست داده‌اند، درک می‌کنند:
اینکه حقیقتِ دنیا، نه در منطق، که در اعجاب و شگفتیِ لحظه‌هایِ گذراست..
👤
گابریل گارسیا مارکز
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 187 · <a href="https://t.me/IranProxyV2/61" target="_blank">📅 08:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-60">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAPQB0yOvzs0LaP8YGj33t6sjAw7q-0GzRQdL9bW97mP4hacENaqpHfHtCinW_-hJ-txx6AVJb0eokiRCwRzp_OxgRvaGnuByV7jPvnBjrw1e6zsmjM8G7zVe01WE8v8buFm7kxwfqsOrO0pmseCCJOJychA_bsVusvJdqXvEoD_K4dJgPawMJIDH7UT3_mZ4l6lj9VlmB94Z2SB8TD0dg1n-cxsZh5Xem4DLtsKzcGHWSBbIor-vuXHHF81NPUqmRbNAs5S-30Ra9ZlnSDqQpErf0oSQvXLo1v4bRi-6w9jho0jM0_5RoGzw8FPY358AcTXTlu4OSjWi8hLmATmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لباس‌های فوتبال سال ۱۹۱۴
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 195 · <a href="https://t.me/IranProxyV2/60" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-59">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">در حالى كه تو مشغول بيش از حد فكر كردن و ترديد در خودت هستى، يه نفر ديگه داره بهت نگاه مى كنه و با خودش ميگه: «چطور همه كارها رو اين قدر خوب انجام میده و از پس همه چى بر مياد؟»
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 189 · <a href="https://t.me/IranProxyV2/59" target="_blank">📅 22:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-58">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کیفیتم خیلی خوب بود اما امتحانش نکردی...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 220 · <a href="https://t.me/IranProxyV2/58" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-57">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">+ خوبی؟
- آره بابا، یه چایی بخورم اوکی میشم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 224 · <a href="https://t.me/IranProxyV2/57" target="_blank">📅 17:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-56">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واقعا قدیما بدون گوشی چیکار میکردید ؟!
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 218 · <a href="https://t.me/IranProxyV2/56" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-55">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd3ytcmn8T-YlxvdFjJSekmGbRGoIV_VFWTixZL4FLJPgCHbN0y258ZtcSGtg-UItrGFssesL4FQYWfqyuZRU7VLAYm6P28__cow_ieSlAECjZymJMQ7oAw92IJ5_wdWynq7YklwoGgFA8iyynoDx7AN5At842f2Nm4bqoD4VTYNpnjyardW9OP-f3Y3Cz28oNz5sYdDg_RJ4JuSuDqpea4qMAWVPTXLPzcOO9L8LK6NM4NkMKHckrB97_XdPsptg9IMzkxTYoZYRsQ2SfurwKPmFRY4YFUYfUVopS7t-MLaxGjBrsjMsu8vFZkO21mxHBH_r3Ln1x1kXRu0g0nu2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداقت اگه عکس بود :
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 266 · <a href="https://t.me/IranProxyV2/55" target="_blank">📅 14:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-54">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
لیندزی گراهام، سناتور جمهوری‌خواه آمریکا، درگذشت.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 192 · <a href="https://t.me/IranProxyV2/54" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-53">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlhEvVc-FneweQ4udTnxt72Slz7P4jZbVH6Oha5CPLnqc4Z0tZHBwYaR794cwQbAHAb74uWuPAq64ZZzveNSeo_5_kSXXXCG2juae0tpKZAFUDv6qJvP5H63RYoLSzcLPRcb6kov45VYHCexoRewtn7MmcyD8srW1gw2qnnC917Gy5JzfqAfkZmTKNJAKw2E25vPsBaivNkZQOJoOrtx1zZp3RpTqpJqZEZyHOhgg3l1GDYo4qaqrXRxqA9aJ3AxWCNX99tkMiocn9TKcuZFtSNQP2febbEA0zmm60PuuwF_JmhlxTNuZw_JAZkyPCxbNgS03gMbDOD9ZMMQvlEeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصی که قرار بود انگلیس رو از جام حذف کنه:
پروکسی‌
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 258 · <a href="https://t.me/IranProxyV2/53" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-52">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امیدوارم امروز مثل روزای دیگه تکراری نباشه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 205 · <a href="https://t.me/IranProxyV2/52" target="_blank">📅 08:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-51">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۲۰ دقیقه ای که بین دو تا پارت درس خوندن چرت می‌زنی، بهترین ۲ ساعت دنیاست. اون ۴ ساعت رو از خودت دریغ نکن.
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 219 · <a href="https://t.me/IranProxyV2/51" target="_blank">📅 22:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-50">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDBpRxQrEBJevjYeusVG_hPvKXZ00ztLayQ43_4xxOZnPGge9BBWVQp5CQCLPqLTcl_86HaFc-c4TECzU4_vxEAUzgqdsWHbXGmZ_Uu6FYhyM9FXPAlovthytFaQzipA4cPfOJlFRbk6Kk3ySVEJEM5hXT_3SeLZFfzRignQOlIjdFyAbct9Y9v_durKZsG1C_SoMX2qzAKjAAwx-iHVRq_CK-kmKC1Z96c90fpeQxoHRvc1rhX3tnj8WNG9vT87I9uSlNIya2spxgzBq5qwdVoEQ07HgQRUrfEyLYoKk_CWPU3yVUz-JaihL--DtR3HLrMue9KjMHsolBDDlJI8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه شترها وقتی میشینن، پاهاشون شبیه چرخ میشه.
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 215 · <a href="https://t.me/IranProxyV2/50" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-49">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhYFdS1FF0pV55T-UvvNOmuH5IV_EvqBlUA85G_ygy5EKFHPPSJIm_LTgbJIBEbLZWKgRoLjtMqBmSbNBBq_PwYJqWRFPb22u-6jyKRzcDFL-kV5tYZ3wkERKLk0ZIg6yMu6VKtIlGYLf6pnscJQFu7AEp2y_uRoAmIO8u0ZfVT8_0JemxNoajnDzbtruxJ3FlIyAflJmOOCaB0HqBylZ0ZP2IMqgUH_JsG8aC5oWiHxJfRSKibop-6VXWa4v__YL-JLF-Ov0lPhcGZtDjo8S6DnUMCAemNmLpwmyfoBvkqdGLPb62KbacI5YJJBXxsqL9HDkzGNaQ9oTqFIH8rlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی وسط درس نخوندنام به خودم
استراحت میدم :
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 195 · <a href="https://t.me/IranProxyV2/49" target="_blank">📅 20:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-48">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAK6JYtrY0lRVLfiyyP0n3ffANiohKQugc845oTXL2mhT9LdFIkjof-n2bYX30Xwm8m6u8Bidn7bAM9DpRSJRtKulGOgQsfxBG2C864e2kC_80dhuiyspSUr26uSPYieigRhh23afRpZs49J7UJwNecsWujAYXfPSxeLb4L5Ux1cd3NnEWn2YzzYaPevGypPaiwcxh6kxgXy9IXu-k3o0ssvE8nMkjMAz_GcpXv29HQfmW8gbPQw39Vcx8bNJky7bBHRsMkxCmkbm4kyH7OQVNPb0nayeSVrNkUAvWbufbrB3hFjzfkNQnYSWiMaMQYyVvP2syjH2f0FBNIHr3TDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلم واسه حس گناه بعد از با دست هُل دادن تو
تنگ شده :))
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 218 · <a href="https://t.me/IranProxyV2/48" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-47">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_tpH68R3VRN0TaSnTwWxnkkjMUDk3OPlBxG1aVYWW91J8iKQ7e35TEcOihK72OKCHNYOTI3Q_qYw6D_Zi4tLTb-0emcvZ4qWtRDNDUdliGD7qCOHmKflVScvqSq8NXYCfJvnLew4Vco6CdhEjS6fIDGkvbHr5M0Aoccmd8DICxPUszVGghmbx6l6IwRsYdxpco6gDhx5fbHtNJm4Tq_HGjvZdLd10ezrNNUlMzLusMRFpDoJ6CQU2tCf2co4zP-4dERbaQL8_c9lTXKdOm8pXJySItUSihkSN--28gHX1M1p-uP_-79UGYZ40RylrHzQH6AaPj1DN0WVWDCpPJpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♾
اتصال مطمئن، تجربه‌ای روان با Lost vpn
اگر به‌دنبال یک سرویس باکیفیت برای استفاده روزمره هستی، اینجا جای درستی است.
📣
ویژگی‌های سرویس:
🔗
اتصال پایدار
🌎
سرورهای بروز
📶
سازگار با اپراتورها و دستگاه‌های مختلف
🖱
مناسب برای وب‌گردی، استریم و استفاده روزمره
🔴
تمدید آسان
💬
پشتیبانی پاسخگو
@LOST_VPNBOT
@LOST_VPNBOT</div>
<div class="tg-footer">👁️ 241 · <a href="https://t.me/IranProxyV2/47" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-46">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نمیفهمم واقعا چجوری غذای دریایی میخورید خود باب اسفنجی زیر آب همبرگر میخورد
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 267 · <a href="https://t.me/IranProxyV2/46" target="_blank">📅 16:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-45">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">امروز گرم‌ترین روز تابستون امساله این پست رو تا پایان تابستون میتونی هر روز بخونی.
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 310 · <a href="https://t.me/IranProxyV2/45" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-44">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
زیرنویس شبکه خبر ساعت ۱۲:۵۱ امروز ظهر :
با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 361 · <a href="https://t.me/IranProxyV2/44" target="_blank">📅 14:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-43">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
طبق تحقیقات جدید، کسایی که دل خانمارو میشکونن، زودتر کچل میشن
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 432 · <a href="https://t.me/IranProxyV2/43" target="_blank">📅 12:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-42">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">يك بار برای همیشه غرورم را برای يك نفر کنار گذاشتم او هم نشان داد چرا نباید هرگز این کار را میکردم
پروکسی
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 455 · <a href="https://t.me/IranProxyV2/42" target="_blank">📅 11:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-41">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بنظرم هیچ حسی قشنگ تر از اینکه مطمئن باشی یکی دوستت داره و برات تلاش میکنه...
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 483 · <a href="https://t.me/IranProxyV2/41" target="_blank">📅 10:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-38">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Channel name was changed to «
پروکسی
»</div>
<div class="tg-footer"><a href="https://t.me/IranProxyV2/38" target="_blank">📅 11:10 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-1">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Channel created</div>
<div class="tg-footer"><a href="https://t.me/IranProxyV2/1" target="_blank">📅 03:18 · 06 Ordibehesht 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
