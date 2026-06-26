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
<img src="https://cdn4.telesco.pe/file/NaYTvHoa1w6nI-dbIMTPVjIzvNm5vDMpCuDMz_WRBW68T39iSlpjl2a3ayDPAHH5ORIKwvxBitZFEDa75kZkItA6fNfZmN0PFptp5s0FC36l-nlwbUf8TaWbUuazLq3k2zLeqrqQlEY4aBAV4hlq8qYwA_GTB27vcisPR4nzPTJtVPiKuZq80Mzv3q-8gLj4gCVRr6yI1UDRDRBnIs5ODs5RdKm44GKAtUgYepsCbhi1yQh_e1q6iY3MEyHlEL9oblcYApEWamZH19YQVYqP6cdtxKirnYQLNwlc63dSa_dgMjDu8lKot96VoI0tjae610L-HybiZiz_yfmpS7ZLRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 15:59:24</div>
<hr>

<div class="tg-post" id="msg-130326">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=FIVnxc69AUCo16QHIT-ubrKd1cxzmqPDN0D6iPnWn5AIIYLgLVJrkgpr_HK2R3Y8_PCRbfsi02v36JMjif-ZdwnNSLsAj2yEzQmSjVACi9OoCPS2iwaiuA5262s0rLHaYcDS2hwGOnh4yrPcermgBPyU_GFITOxXf28FcYSSYbivHs5mRt-vL4-tQHGsmRae6j0aXbnXfG2ry-5RaM-IOvmD9-WyePIsHm5J8NfRzZPxYKC3iqB1v3Uk5ej5eUz5TlwXqXlzi3_z8pkvoKov3TbSHlubCgk576sgD5eogfNTKPRXJ5yOqwRLX7jvHxW4gha_PVl52uBcVAaYMetyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=FIVnxc69AUCo16QHIT-ubrKd1cxzmqPDN0D6iPnWn5AIIYLgLVJrkgpr_HK2R3Y8_PCRbfsi02v36JMjif-ZdwnNSLsAj2yEzQmSjVACi9OoCPS2iwaiuA5262s0rLHaYcDS2hwGOnh4yrPcermgBPyU_GFITOxXf28FcYSSYbivHs5mRt-vL4-tQHGsmRae6j0aXbnXfG2ry-5RaM-IOvmD9-WyePIsHm5J8NfRzZPxYKC3iqB1v3Uk5ej5eUz5TlwXqXlzi3_z8pkvoKov3TbSHlubCgk576sgD5eogfNTKPRXJ5yOqwRLX7jvHxW4gha_PVl52uBcVAaYMetyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده تا از مزایای عدم توافق و مقاومت و بدبختی بگه
🔴
نون این جریان تو بدبختی مردمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/130326" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130325">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مهار آتش‌سوزی در پتروشیمی کارون
🔴
روابط عمومی پتروشیمی کارون از مهار آتش‌سوزی امروز در این شرکت خبر داد و گفت: این آتش سوزی تلفات جانی نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/alonews/130325" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130324">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ایتمار بن گویر وزیر امنیت داخلی اسرائیل به کانال 7 گفت: آتش‌بس در لبنان نمی‌تواند پایدار باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/130324" target="_blank">📅 15:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130323">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
هم اکنون، هشدار تخلیه ارتش اسرائیل برای شهر منصوری در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/130323" target="_blank">📅 15:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130322">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فارس: مذاکرات بر سر بحث هسته‌ای برای بعد از حاصل شدن توافق نهاییه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/130322" target="_blank">📅 15:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130321">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955a11f8e7.mp4?token=MT67oYDsz1A1Jsl7X5_4bai6SAhl51c3XsHbRmiI5ZXpOwhUHoCn22N8KwexdBb15bqCCCyNGgYR6O0JhFsmYaCpl6AOg7aRLIzsihaF5XsjVZIUtOQoo0ytp7NR_4ElHCxY78z0rn8OkAWT8nqmja8-pOK7htLY3-nViZ2hsyI1b4OpsHqZZzAPdUgHERVHvBdI0NhmzBgoD99Tceq86_WKxVqtm0Nsf-ZdG18LP3Oz_gsHyQwD02PDO3rOctOAIrHKquyhYLLEZvnrcv9XjHiBD63mGyFYdtmP9l5yTtLpfFEX1Zg1MNylpRaVtkP7ncBSoM7LlyBn5vadPqsHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955a11f8e7.mp4?token=MT67oYDsz1A1Jsl7X5_4bai6SAhl51c3XsHbRmiI5ZXpOwhUHoCn22N8KwexdBb15bqCCCyNGgYR6O0JhFsmYaCpl6AOg7aRLIzsihaF5XsjVZIUtOQoo0ytp7NR_4ElHCxY78z0rn8OkAWT8nqmja8-pOK7htLY3-nViZ2hsyI1b4OpsHqZZzAPdUgHERVHvBdI0NhmzBgoD99Tceq86_WKxVqtm0Nsf-ZdG18LP3Oz_gsHyQwD02PDO3rOctOAIrHKquyhYLLEZvnrcv9XjHiBD63mGyFYdtmP9l5yTtLpfFEX1Zg1MNylpRaVtkP7ncBSoM7LlyBn5vadPqsHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی سپاه: عبور از تنگه هرمز فقط از مسیرهای اعلامی ایران ممکن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/130321" target="_blank">📅 14:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130320">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d81ff4ef1.mp4?token=bjc4NjpMm9qYenhPQc5aLLH47bUuWpI7q35c6PrHCgLYdN9CST2mxS5k3VFmEl_M8HFCjAxzOTfb9IqACihdjJfkRlt3VYeQh6sfoPXzZu9aKwlCf1m7X0gizaZ0rVeeZi4rbM9At-r7vGCB6oUi8LBrEABxKtEr7Y0CRqLE7wxWF-J6WXXphOwANlDsDa4ZioMcVukgqcosAa7QBbtx0xvyPF571xpE80mwpwgDjgV_cDZWllilLKa_EqgzDtHxhDvW-KXCML6jEYRmjOjFPc9G_F8b1oIDcW8Cb8mTj-z_IcwBy3I7mARQV_Zaixtx5Pxcgw0Og1cJ1QGrMJZBCmbboCk0jx_Gdz9RXRwwWX_Lr4sgywbqyxdLJVIOE6Eygg8z6gSr7oJV02P5ru6Ds7BhEVWf6OEmvnPY3RSLAp7_qjmMhLzaeD0TmTVb-U3QsXCvpk3W3tAsNmMBrzXA9Ujn8uY3RuMSCBNO3dkkNeES0JMWOotWrVStJ9peyGM1GZOwfxZhQC09uJYe5yDuhZvzPpd9oX9A4S4KWyWgxe4Oi90GtJPswvBgBp_5lM3L5H-Z4omrpOAXbW2s8YAyYZ8Ja56yawpW1aYJ_LdK9XDtyIB2s4dQNu2Br766u4Idz9dBhMZj5Bv4oyi6VGaJq40dZ_jpSCLqpRPieHGZ7AE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d81ff4ef1.mp4?token=bjc4NjpMm9qYenhPQc5aLLH47bUuWpI7q35c6PrHCgLYdN9CST2mxS5k3VFmEl_M8HFCjAxzOTfb9IqACihdjJfkRlt3VYeQh6sfoPXzZu9aKwlCf1m7X0gizaZ0rVeeZi4rbM9At-r7vGCB6oUi8LBrEABxKtEr7Y0CRqLE7wxWF-J6WXXphOwANlDsDa4ZioMcVukgqcosAa7QBbtx0xvyPF571xpE80mwpwgDjgV_cDZWllilLKa_EqgzDtHxhDvW-KXCML6jEYRmjOjFPc9G_F8b1oIDcW8Cb8mTj-z_IcwBy3I7mARQV_Zaixtx5Pxcgw0Og1cJ1QGrMJZBCmbboCk0jx_Gdz9RXRwwWX_Lr4sgywbqyxdLJVIOE6Eygg8z6gSr7oJV02P5ru6Ds7BhEVWf6OEmvnPY3RSLAp7_qjmMhLzaeD0TmTVb-U3QsXCvpk3W3tAsNmMBrzXA9Ujn8uY3RuMSCBNO3dkkNeES0JMWOotWrVStJ9peyGM1GZOwfxZhQC09uJYe5yDuhZvzPpd9oX9A4S4KWyWgxe4Oi90GtJPswvBgBp_5lM3L5H-Z4omrpOAXbW2s8YAyYZ8Ja56yawpW1aYJ_LdK9XDtyIB2s4dQNu2Br766u4Idz9dBhMZj5Bv4oyi6VGaJq40dZ_jpSCLqpRPieHGZ7AE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه ۳: این تیم پیر دفاعی، ابزار بازی جسورانه با مصر را ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/alonews/130320" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130319">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V05oyUP-t3j-gStrFqT_D0RhOTzWtyI2yIRc_ZEdV-AREmVvO2jOV4OCtKuTzUS131-MQXUbdnA5XPpja8jBZ7NJJQzQaGcBmOsztLmh0CsrRf5a1XTrKxi_PGeZHes2-wT3iufUxCqG7v3Uqy7oQfp5JHwHop9NbprjSQCeCMsujDrNT0bnqyoIA-w9yHKBN39RFQNAF8coe-ulLCszSVyf2RZ8V0EeU2YTY7vbAjhXqKx2pivCxoox_Yu_LDX6S0a37qQG1RanLPetaA67os75LizaglL_y7jXRchTIplMpXj7UduTrOFOsliE6qVZlys8siLH5Lq_fShZWmUboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آغاز پروازهای فرودگاه کیش پس از ۴ ماه وقفه
🔴
پروازهای فرودگاه کیش پس از چهار ماه وقفه با ورود نخستین گروه از مسافران و گردشگران در سال ۱۴۰۵ از مسیر هوایی به این جزیره آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/alonews/130319" target="_blank">📅 14:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130318">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل:
در طول این هفته ، بیش از ۱۰ ترور در غزه؛ ۶ حمله در جنوب لبنان؛ بیش از ۱۰۰ بازداشت در کرانه باختری داشته ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/130318" target="_blank">📅 14:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130316">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSrNgRpgQl9SlJFl5H2FAhL-BXPXUqbomTK-Zr94kx3YdQWG9Dup_vipnV169mjzrHDNvJeTs2Wfv_uNhXFD0zbbRynEVAGpkcOP1JnvnFBlde-x21J6U81zquebGyneff_nSTk6SjY-DHDUGx7gddrX1P8CUZwz8fT8BsJq-cnWmhCF6oCtBxZXJJ4V3yrQgMmYJpDkaQHRfHezqoq9fEJRr0OEfiG3VUO74Oj6uIuJKl-o-1DZAV8JgQyN5oH_7Sk289XoSYevzg_C6dmbziWDeqXj6t2WchSKVmcm6_JO0YNwyQZO9tgkLAFOhdurznEmuVtWorMdti2OjP_g3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس شِلتر:
مذاکره‌کنندگان وصل به شبکه یهود هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/130316" target="_blank">📅 14:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130314">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52da7df95b.mp4?token=O83G5KsPAamuItBWM0UaVKXeLEvVXeIbiQEIWO14qNFNFYziIwFKFrMQO9OOfDVrLd-RpyavfLV3QtfNk32aSbliOgA0xACUbCFQ8IF3PIx021j9FQttH5XBeE3KViOZheEMm8GGiulFsTInzYftBC-2dmapvXYFlsh04YQVp33boezZi-1dAV9D6TSMSNPdzhBILPBRsu-7xp3V5Il4zoBAhEIz5r_1nighNOLvK0ryHgF2Fn38f3NB-uzzG9LwDm90BNMhyKZ8EMetnN6ZFpmVu8SUKNgZ4TVYGj9AH7g9XnrUzW7w_Ujlkto26FvdhW4HISiSOjurUoEAj3Kc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52da7df95b.mp4?token=O83G5KsPAamuItBWM0UaVKXeLEvVXeIbiQEIWO14qNFNFYziIwFKFrMQO9OOfDVrLd-RpyavfLV3QtfNk32aSbliOgA0xACUbCFQ8IF3PIx021j9FQttH5XBeE3KViOZheEMm8GGiulFsTInzYftBC-2dmapvXYFlsh04YQVp33boezZi-1dAV9D6TSMSNPdzhBILPBRsu-7xp3V5Il4zoBAhEIz5r_1nighNOLvK0ryHgF2Fn38f3NB-uzzG9LwDm90BNMhyKZ8EMetnN6ZFpmVu8SUKNgZ4TVYGj9AH7g9XnrUzW7w_Ujlkto26FvdhW4HISiSOjurUoEAj3Kc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم وایرال شده از صف نذری تو الهیه تهران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/130314" target="_blank">📅 14:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4fae070c.mp4?token=SkAc9JARKJ-kJuMeLOgTsp45qDufeAXe8gyMome6vqrU_WySEJ4ZgfktjBm1uR7HWAxahAUUNWnzfP2VdAenMFfEauupRzVeEBXxtETTq6O-7V2JD9cZGCrkTDId5YNgFhoI06vGA-YFMk_pcSGx30JSk4bcLx9dRionjn-1nC0NGH0qS2OLdMSqg3OWy56gGXot3BK1wjpZ9tuIhBgn9tJVnsXQceMo16RmOsgRg2OYsZtxrR9tNCcP29Qb02LY75iGqmZ3HrUaV3oC7eVduUpLCmwdqr3FiacUeleXnOio9LT6yQKOVidz8xzUPwB7toTjSCOF5NuUBOt-9eIZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4fae070c.mp4?token=SkAc9JARKJ-kJuMeLOgTsp45qDufeAXe8gyMome6vqrU_WySEJ4ZgfktjBm1uR7HWAxahAUUNWnzfP2VdAenMFfEauupRzVeEBXxtETTq6O-7V2JD9cZGCrkTDId5YNgFhoI06vGA-YFMk_pcSGx30JSk4bcLx9dRionjn-1nC0NGH0qS2OLdMSqg3OWy56gGXot3BK1wjpZ9tuIhBgn9tJVnsXQceMo16RmOsgRg2OYsZtxrR9tNCcP29Qb02LY75iGqmZ3HrUaV3oC7eVduUpLCmwdqr3FiacUeleXnOio9LT6yQKOVidz8xzUPwB7toTjSCOF5NuUBOt-9eIZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن رحیم‌پور ازغدی: تُف بر روزگاری که رهبر ما را شهید کردند و ما از صلح با آمریکا حرف بزنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/130313" target="_blank">📅 14:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فارس: درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/130312" target="_blank">📅 13:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130311">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td5w0i6mXR3I3XlY6IQZnpswh_3mH5aWdgjCtqNzsj_4lpWM684iCnek6dkcSBBALssbyaZBthWDyLsEaRHRUAMP-aR9FkwrELYE3bm5G2dCYIAlQ9bVsSu8pVZwOLoq3aL-DfFgOYH_EcBN5u3C0usOxvm999i5GQli_KvPw9PN-lYYH4qqG6mcPzFbP-6uLjtFTXgkyp93ftEwaaUVSLHcuA_nw5hFklhsImbSDwWfUZKEjh8Mm2aIcRL0kdxpt7VM3DilxwYyXBUW3sYb7z9govViCUVTIG8w00fEv2Vn8kLB64u0OsHhh2TA_uOhFwTvG7UbMjM1l4cfxOyhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :
ما یه بازار جدید داریم که داره شکل می گیره و اسمش کشور دوست داشتنی ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/130311" target="_blank">📅 13:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO7wpqCLsEte4KfuMUExYgHP62Hl1UbZagm5nfCTUVG5jopjTYmbMq36RQnz2-GUOczeFiRF30ziduo9w3DaDSypfnJPwZ4F60kqcTzYe3FUN70vSGuRs7AQAYQ5Plv-MtiP5fxUFMtETP51b-9N3ny6GUMOy_C6F7W-DbysZsW5vTa89aW6qRk-kSsa7_l4GveKFOBVPQJCW54PfFTdd4yh_DsxuGxgDV6X-mFzNNs1eQ2r7bcySQqjCqBNgeTzVZxhFQLF9CuxsVTRkB0MQKDT07k5Uf5rON6nR_rcBQWIV1d3Z18nNjXI5mzgglSgIOmdoChxe4GXHMjhCcrbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روحانی: امام حسین هم روز عاشورا رفت با عمر سعد مذاکره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/130310" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=Kg35v6ywghDE_kwNMEul_s8Y7-vubLcR6a_EHEeVB5MrwdCU44-6soYkeQX5-XEHQaycFFFXyV3g75pAZI7HJ07dP98wSx48JfI-yJ6_TIqFDulJBIRVOETGRnACSUF77p-vWiMI-9OlA0Wu2mf1D0A3MsRb1BMv7VZK-NVqVTu_hgMnJCg-WQRTKq0hMTXwptcafNaXIMlgHKOvFdqMkaqaDGsI-rsqxMkX2raG7TmWNHkPF2uXeSGPfkJWOeJL5JmYVC6XI0IdlXzykH0TjTr-_uL8gZzWs9TaIIjbrUpAOwesv_tQfVwoc03prW3ysR-tCRTTimTjgfFgWLTh8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=Kg35v6ywghDE_kwNMEul_s8Y7-vubLcR6a_EHEeVB5MrwdCU44-6soYkeQX5-XEHQaycFFFXyV3g75pAZI7HJ07dP98wSx48JfI-yJ6_TIqFDulJBIRVOETGRnACSUF77p-vWiMI-9OlA0Wu2mf1D0A3MsRb1BMv7VZK-NVqVTu_hgMnJCg-WQRTKq0hMTXwptcafNaXIMlgHKOvFdqMkaqaDGsI-rsqxMkX2raG7TmWNHkPF2uXeSGPfkJWOeJL5JmYVC6XI0IdlXzykH0TjTr-_uL8gZzWs9TaIIjbrUpAOwesv_tQfVwoc03prW3ysR-tCRTTimTjgfFgWLTh8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسم محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130309" target="_blank">📅 13:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
حزب‌الله: با تفاهم ایران و آمریکا، ما به یک پیروزی بزرگ رسیدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/130308" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh8c7Q2Js99enYX5dd93_2L235xob4WFZeovi1UVGHkpXcy_xkeZYqWhnTBCI6pfsi8dkLAk5tXXxHnBr2_czsZ_Iu3Ifgxz9j2ucGV3Y47enPkSipzxY3IgCT-enQez8mm4240dUEQ9Uwmvage5Ak_8sL42bhrDFF0Wq1AV5NK5fwXVX48maXNqu2BqwNKeg53jLbkudO068WPUhyZHDeSeY8kI2trhipkTNgg7TDXuK2ssmpLhoUWYsDDKOk664acsMVcQs-j6O03o33stBI35znWEyVSs3x7_3NXgbqnFs43zKD-HFPYICH3g2wGsALnwOqlRT1RSrQpdgKPdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۳ عبری به نقل از یک افسر ارشد اسرائیل: فروش جنگنده‌های اف-۳۵ توسط واشنگتن به ترکیه، آزادی عمل نیروی هوایی اسرائیل در خاورمیانه را تهدید خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130307" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130306" target="_blank">📅 13:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=Bi6Q6dhfCvKx-c05tJIxAZBbSzcjRPSah88e0SOg-fdC80kJtLInzMONL720yr1DU1xOfhu9baZJo7kSNlgVMFi4Noj-cZ1aXQlcqu3v0qGOYcXL7e6AtVtkxYAEqvIUIKfbRnXwJwusSvvZJW1gsXUGF9wL9WXxuIzBh2RkKwIDlOvSOrlGvtya2JlO-hjUIoV_U94wWwIpqhCwA98X7jaOhZ3oUivnBlz6fog-hcgof1zp8V95__lsA9ZrOWm9l6c8seLwvLuiz5aX-sYiv4noArQBh_uHWT9g7ZUTK49XAYQJoxOfAkJXoJERo3N-NQMYD71yOC8BCI3j5Krv-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=Bi6Q6dhfCvKx-c05tJIxAZBbSzcjRPSah88e0SOg-fdC80kJtLInzMONL720yr1DU1xOfhu9baZJo7kSNlgVMFi4Noj-cZ1aXQlcqu3v0qGOYcXL7e6AtVtkxYAEqvIUIKfbRnXwJwusSvvZJW1gsXUGF9wL9WXxuIzBh2RkKwIDlOvSOrlGvtya2JlO-hjUIoV_U94wWwIpqhCwA98X7jaOhZ3oUivnBlz6fog-hcgof1zp8V95__lsA9ZrOWm9l6c8seLwvLuiz5aX-sYiv4noArQBh_uHWT9g7ZUTK49XAYQJoxOfAkJXoJERo3N-NQMYD71yOC8BCI3j5Krv-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/130305" target="_blank">📅 13:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130300">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIFTUzq6LDictYI2iae1OyxlDffoJ79MtEyOkfwhL7aKIggo5PIMSfVANkSEnCZdhAaqNquXYUhmXA9MZ3s6Yx_7-dZulbCEEuzqZacLmCbdvconkw-oq400yH-FAg7bkpFIeviknEi5Ptkc-MDBGSNVsT6FlI7kVbkS4_7s24RxL7pRd4XwvRvzhl1muNu7ScGYRx8f9orgFa-obIZMbwYK0RP6A3pRxyuyjzvcNtLE_TqfVGJbeaUt-5-NArYZIQsm1D94I5Y18jj06WP78sHqIQ6Y9tk6XBK0UnRlNA1maD8z4UefqU9fi1T-XApezY5aFOFHCsjolAIX28IEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAYidsAlDF6XIv8vbtUj37NKpwoY8nmKE7dw20SPCllxw0mulWt71CkPLJBeh4WW3Ova8p9o0U7y-ou9es6WMJ8z-ds-9ShP7EzFC8OpfhbhJMCiXZmhysdLPKvf8ThrX3Mm63iIenA1wwnhGX8_IRCp6pHc-Csg_db_t87sOUBmNvwHzfE_SAVLRZrnDsHJSUsYLEWmicTMX1B-a4lT0mbTJmqnsO8rKUdLWWD9ywUEQadxHtwEu8WmUUTEcVWkVOVNzCKzzL6INHVHWD2ib6cqFPEeK5D2lSncAuVEODZLVsD3AT_4MWzkbsxP4wrD5dk1gbDT2v984yKmtDZweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oIPOgr-bjG1Tmwmi9QDtHkfcFIhSzK5RqfUtYa2fcwNhPFL50fKjevydCUM5hsPPNFEC6kmqFRxxCTqZw0UPff5jkNs2IkkmgMj9qWSnOJwX7bDp0YV__32DLftfzRMF9ruTY-tl4PVp216Rt0xU1K_i_UEQiq1Ohg4_E2-iuzk8AUW_grzoDgiyvEhGQ1wkJu77KkuQ53pni4d7uzrtoFcZP-UvitdfdPU96astSUcUWxEtJ8wc0Xj8N66KWzTWQK9WS60fyObyaCMAmh3iiNLyiUrF01Hwod36dndoaWGU2fOekVIxxlFDaGonM8ukbsfhQ-blWPU62c4zjAcMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a25pcOGrmew_Prsd01rHY5MD61n24LsATmrTM2k4G3Rf-hfJcoHvPHLOWhXqWnwRHGIMxM3hHvxdDWM72CsxLwtYOvoaoNmlL_fyoRIrJSzm0jRVRSflFunbIhmaxLhf-mcp_rl2RV-9ezQipfJHuQF01pjK46iYYeCV03obsY2b2An7yA0on5Yk06lCsgqyrx5L7B2gYAqTtlOMAq6jw67t5JrchKrT0ahbgksN-sHPnkw6GmBrYeSChcolMP7kVmZdvAiIREE_7fcEuLVAOcLmFhq1rr2l5aQa8h1q838s2XMW129zLZpoF2aDdi2FaX_vAY_VUjBz3YrwPBwnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqGRiRmdLNIfpwcQFUtf12GMcGyqOBvUsxjXrb9uLDmNvp1CnGyybnCHJKLxey2JG4kc3C_H19pY3ZhnQFxAJ6rNWsHbasQbJDep-PEdbShbhdnohxMc7SVP_Ap9-BHbKrW1qddf4l3BgDDjzaoUo03uKzjl1ZzlS10k7kSLLKmleRXm1DoNYZNH133BTBIWLGysD_ojug9uNaBR1RuKiF7FYlPMfCPSIeowdyGHN_S_gNsFFtsxRbKiOY0JpMncqDIEPEeZ4VgXNp_bdROJdKAgDBs1dvPktDLwqhco5-hPDHqDrzFwKb1orCa26Zzgldf2BDe7uIzCcKXLpXaE4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید ماهواره‌ای از خسارت های سنگین حملات ایران به پایگاه پشتیبانی دریایی آمریکا در بحرین
🔴
در این حملات، ساختمان فرماندهی پایگاه، دست‌کم ۱۲ ساختمان دیگر و همچنین دو پایانه ارتباطات ماهواره‌ای به‌شدت آسیب دیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/130300" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130299">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/130299" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130298">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
طبس گرم‌ترین نقطهٔ جهان شد
🔴
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130298" target="_blank">📅 12:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7xEaNQ8iF6-Iky0unY_ZJ1sk8EMv9k6aSFSCtGN6hH4wp3m3ioOd4hqbIMO-dCMRKDqiqP1h9jm4e9_LuwmXSXWYe4kzmWnRWbiKJeLs_08gFPCpoubewFWlEjYehlKufDF20WpZLieLCoh4scaV0vsKDS0nqG18jRns1bPdwaovYgOwYmoXZhp1akB9Jab9BmyNmm3S3qhfRK7_g0taGted0LXi-rpRQ0J3sY1KenT_RaTofdYnM5C7uzP_ino5fwVLrGMQCg2snzmtWdc09EGxPG-A04m27FRYxCnDoA6W9SuSAqpwdK0Z_CnWOzxapG1UiTGnOd97kqMF_lbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده مختاری، خبرنگار: سال گذشته بانک مرکزی رکورد ۱۵ ساله چاپ پول را شکست
🔴
پ.ن: چاپ پول، یکی از اصلی‌ترین دلایل تورم در حالی به اوج خود رسیده که کشور ما در ماه‌های ابتدایی سال گرفتار جنگ و محاصره دریایی هم بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/130297" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
عراق شایعه خروج احتمالی از اوپک را تکذیب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/130296" target="_blank">📅 12:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130295">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=cfYWZJkD8FbkhhYy059n54vL9tTBXer_HDygguUf2i2PmYcb7CAt9cJ9kMNr-2hNq6tzisjw7RPbVhpZtqOACYSM_2k72tgPintTpsNMIkjSBfjE1sQy7vuUSPZIqkIzlmJpIjEwCnTbGfC14E4CXB452uX3FKu6Bgq1x6gUJBXFvziw3Z2NopCDqHz9ac8CJ4jej_IAEzOjp2LbxY8SOkb4oJnWdrBgoVHbaJexqfWCAHoMVXu0-iygEXE-xkK90euR0fPx9H34bxwGLKltD46zyzHz1e-Esiv9MWWXy8SoFQKo6ovdMaqw2shdz5ZM6G8ggHezo5HzlQ5VIknnbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=cfYWZJkD8FbkhhYy059n54vL9tTBXer_HDygguUf2i2PmYcb7CAt9cJ9kMNr-2hNq6tzisjw7RPbVhpZtqOACYSM_2k72tgPintTpsNMIkjSBfjE1sQy7vuUSPZIqkIzlmJpIjEwCnTbGfC14E4CXB452uX3FKu6Bgq1x6gUJBXFvziw3Z2NopCDqHz9ac8CJ4jej_IAEzOjp2LbxY8SOkb4oJnWdrBgoVHbaJexqfWCAHoMVXu0-iygEXE-xkK90euR0fPx9H34bxwGLKltD46zyzHz1e-Esiv9MWWXy8SoFQKo6ovdMaqw2shdz5ZM6G8ggHezo5HzlQ5VIknnbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاسر ، جبرائیلی: اگه قراره با آمریکا ببندیم؛ ظریف رو ببریم
🔴
یه بچه و بساز بفروش و پاساژدار رو به مذاکرات فرستاده‌ایم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/130295" target="_blank">📅 11:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130294">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwBzEEoureiuH-6_mopzjrab1fLofRc9tTOIbPMR4Ssi6oogIRa14xbLWnhRkJCrJ9I0BlzE9juM1_LBPbg8pWKtGWRKXTafTkK4D9yeGiMdYPVctdLGCw6A0zqO5fTT7bstMajPlGN4ZWFHm0lSNKg7EtOLhVKRJjx5l75bW-UaL33Z88-qvLQfU1neIJunkLd5Exdl0BmqAnkbkAMk5jtr05iZMfrag_3ho93nbGhH9Kjkw4OUpj9H70_cAFRkuEjBaSKU-oSq4EBPZIYt9QIwFsA8MrImin8BSFQQQWpP-T0uerH2izt0d_4P__YlL0XgrP0pGFqu3jJKz2K5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: امام حسین سیدالشهدا شیعیان بود و امام خامنه‌ای سید و سالار کشته‌شدگان انقلاب اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130294" target="_blank">📅 11:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130293">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2ZuU0Xt_AvUxVv-9WP-0_fG4V5e76jjhFdB7rT-6FIWFXBurY-2yQjfNBAa-GuCzSFb8-dD2fp4alzxIvnJq-1wTX-i8ac7j3l7_bGHKGJDdJU-WmQqGWtn7S0cnOm7k8Kl0kJ_aIODWS-kj4hJh3Dbb8qNnXiE2P02ASvZpsS49ofov4psDVe42uw0PqIVG2Vb2kBIq0M1lXxX-Wk3RuCYV9o2SOh9zQn0WYMiiG2iGZCq1Ug2T-RxAPeASAB4jbn6NIWRQXfo-QUhPUIHncawM9yLGCRltmN9F7J4jM06jUx7w4gjrAtLX5i_mJF_ZXokMFTvY0toq4lPDAqDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵ زلزله بزرگ در نقاط مختلف جهان طی ۳۶ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/130293" target="_blank">📅 11:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130292">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا اعلام کرد مذاکرات غیرمستقیم میان لبنان و اسرائیل که قرار بود روز گذشته در دور پنجم خود پایان یابد، برای چهارمین روز طی روز جمعه تمدید شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130292" target="_blank">📅 11:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130291">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/130291" target="_blank">📅 11:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130290">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بلومبرگ، با استناد به داده‌های ردیابی کشتی‌ها: ترافیک کشتیرانی در تنگه هرمز روز جمعه در هر ۲ جهت ادامه یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/130290" target="_blank">📅 11:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130289">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مذاکرات لبنان و اسرائیل در واشنگتن باز هم تمدید شد
🔴
این مذاکرات که پنجمین دور گفت‌وگوهای مستقیم لبنان و اسرائیل در آمریکا است، قرار بود روز پنج‌شنبه در سومین روز خود به پایان برسد، اما اختلافات همچنان باقی است؛ به خصوص در خصوص نحوه عقب‌نشینی ارتش اشغالگر از جنوب لبنان که تل‌آویو همچنان بر ادامه اشغال این منطقه اصرار دارد.
🔴
هیئت‌های مذاکره‌کننده لبنان و اسرائیل امروز (جمعه) نیز نشست‌های خود را از سر خواهند گرفت تا به ادعای این مقام آمریکایی به توافق دست یابند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/130289" target="_blank">📅 10:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130288">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌: تحرکات و حضور هواپیماهای نظامی ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران، اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
🔴
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/130288" target="_blank">📅 10:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130287">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCnUy9mBc9JSMj6kWLHzxhQO8oatGBjOlz9qeEABchDE1qyKNOvKFgF84sdgi_1B5nU0HIIB1g9Guptfk0jc4nZdOPcKZnRg6-ZLeG5RwF_bSXqFpyy0fs9XjEmkGkzl4ApCSW-ptbiC1aIKWyKtzcrgST7-uoK-YurK2ghnN4fhyIdVLAd4SIUgBXEss3w0cL5l8p51fP4-o6wo4m_S520ljr9Fpbggh5yuynlt7LVxxs6Vi2l6_dwkYCp0R2YfpXdp5lteaGUA9Sik4l1Pe8nt-WIqr7e_WckJaI7OkQPRDThpOqnInhuNlM4M8JdmIl5lWrxrGO74-CrwxEXV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان پیداش شد: مذاکره‌کنندگان برای هفته بعد قرار مذاکره گذاشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/130287" target="_blank">📅 10:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_WvBToNU_JDRzQKtpcnnLj9SZS3VH8qyxRk9m9s5CrTel8z5Ze9L6EU9ZBl3tMRUaDb4UW1DYqZmEy1j3XawsXs_Ysp3rGH5QoGFTd4kCSsiGP-Ry-2CLX7sWlNHwarDh0IS3b6NiW5Jc-7taGJHxq0IjTIkdV418pXcxQao-NpxjuKKwWPmfglpRAfFGC2Ev0G0Du_sEBMfbtht8f9p2c89BEAW-OZsop7a2-W26Kp9T4mII46RC4Gqy6_3Qiy0JlRQXoj0IvCIExV22ZAcDeCxX-pAtJ_QI8jJKBT2Zu2PpqGVUJBpInEmGzIdKZDHv3skcr5Gzja1kvs1I96EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAGzTg_QFJGzmHVr8qdpzDlG0c6vDItGL-4UnJDxInbenwldQ5nBKPANlOOs3VTD4N_WK_uNouVjEmurrXvd6ScA2-jrwHBh0IAryk4d4Fg30n7yrlrSMnHeq5ViXI0EeldYLtoq8CjnzQmRFi1W6t8sQ-2PJ5YyhKfDEjFHYBV9RmTkIZsmetYO2qzJUHwY8aVWt58pNw82_DeG4NlBypLg1NlQQBA-dRPXET31X09sIo-PQxH7m3-d3X-RKNSiaJjKAyhpw7XqzAOuDCEObmh5HgV1m07p4LclI9RBZS1iQSxffHd5lEqx_fr8XG24oLzt5xyr-JsmDFDrANgfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIH7q7aJ6vDFz62r6AszHhWa8aQNUAlNcV-hi5ojCgDVGG1hpiOFwOlLd2qvziu6RxuhMSwmeBcCivAhlShLGLZzeE-ujNFTzKPByTrfvsho7yDY8lYYBkR9Cs-IzafXk7FjbQJVPpagrugk7L07cwvLYNjgCIhE0Y0gNR8HErsnV5hYZsQXHRBdELP3OMt2z5IIwGu2jP3XPYrPUPxDN-XVfcL3VeH-IzAby9Pw1gCKmrREFPZP3glj3bLshXz79kTToleRdoDcb_AS2D2wmtFYKoWNAnA_34i4wiLk-ln81VwhjSx3wPQzhZjCUh_FiMBFsMIbA-RnsuF5IV8JuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTd8J1TbHTgcdSBdeYR8W2i577nF2tTW572eozLM1YIQGyGX8h_Gn-t_-Ugi07I-t7lKWpqlR7uQ2n-6C9xBOU1Q7-F0oGs0oH-2XSYmlLsQE0HFVILgCPG3RmaQQ2m_87LwlEnhNbHhFHYqUxDcgXe3kSwGa2AYqIa8ihBiPUJMKt1pkCnqsqc4ouVqzoRqsZ40IzymsyyMnclCnW_orLIBVTRHdcaOtvSAxLTsk_KBrRJis_MG9ylkoGNOTCuzRFFYTrul61AxRCv5LeSJPmCMwzYUnre24EBXjwZ5sp-vUmZFIeTgiuajuMY6visKlZBORzlwyJ3YbR7jVrP3Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون، رهبر کره شمالی، بر آزمایش‌های جدید پرتابگرهای چندگانه موشک، کلاهک‌های موشک بالستیک تاکتیکی و سامانه‌های توپخانه‌ای با برد افزایش‌یافته نظارت کرد و بر لزوم تقویت قابلیت‌های تهاجمی «مرگبار و مخرب» کره شمالی علیه دشمنانش تأکید کرد.
این آزمایش‌ها شامل یک پرتابگر چندگانه ۲۴ لوله‌ای ۲۴۰ میلی‌متری ارتقا یافته با سیستم هدایت دقیق خودکار و برد تا ۹۰ کیلومتر، کلاهک‌های ویژه ماموریت برای موشک‌های بالستیک تاکتیکی طراحی شده برای وارد کردن «خسارت مهلک» به فرودگاه‌ها، بنادر و زیرساخت‌های برق و گلوله‌های با برد افزایش‌یافته ۶۵ کیلومتری برای یک هویتزر خودکششی ۱۵۵ میلی‌متری بود.
کیم گفت که این آزمایش‌ها پیشرفت در چارچوب طرح نوسازی نظامی پنج ساله کره شمالی را نشان می‌دهد و «تغییری در وضعیت آتش در مرز جنوبی» ایجاد خواهد کرد.
او افزود که سیاست دفاع از خود پیونگ یانگ نه تنها با هدف تقویت توان دفاعی، بلکه با هدف ارتقای «وضعیت تهاجمی مرگبار و مخرب» آن نیز هست، به طوری که «هیچ دشمنی جرات رویارویی» با این کشور را نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/130283" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل به نقل از سفیرش در سازمان ملل گزارش داد که طرف لبنانی اظهاراتی قاطعانه مطرح کرده
🔴
وی افزود: «هنوز به مرحله صدور بیانیه نرسیده‌ایم، اما درباره مسائل اساسی گفت‌وگوهایی در جریان است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130282" target="_blank">📅 10:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130279">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhkjUoeThrDVSfNNDyYV8aQExNq309PmHPTRpWaQUexS1Y0GAdEV9nxjJSko73_ck1JQenXW4Fzi-drEZistqrYXcSEBo9xkqVhnZT4tOEfYE9yCDm4W4bV-y-QOibpPvukcxFkINdg9mxQUCI5m6iSap76tkDd9iUy9TiIkcqibchJAdty9hw9xQyyZlPwFMGkUdS1nGSpLKhxiY0wIAKlDHFLm2pmfo1aWxjt4XaVVIvuYA227eQLDeLrd4gTEq0CI3uM3pODfdB4l_w1u4jzvkzZdgDyXiCeB3DJ0LSALfF7LMzWVEaklbxiv3VGMNXWP5t7i_SMZm2MKH6pp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joSLo7p7cDQs-nCD2r5qiDUiRM0CnPXGLXtwJf04bICLjct0R1wwq8vzRe2JgizjOxeCR9AmU1DMfShVw0evytY2y6o7MKV-SqeZ9zYE8F5MWg3tfPIzcZJrwapxTbkKQ9-NFTSV3FZvrl9EJcRNxymo43n9f2ubxo0Uy9zcE5rDEgliQjh_X6q1gFbZvjeLtadvhG7NBFCvX45HP3oIJXraW3vNorB0A4Cd6ZUL0Iio1wB-EbmKIdG4QLZTbUxMO01HGB0HesDY8MCa6rb5QICI5_QJjDXzlZ_We_mHDAiFT41L09pOUxEgn6kXY0m3kIjH5oKDgQpACnt0P6Xv1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bc2eaf0b.mp4?token=HRgt9Dpe2AgI22r8NzMC4GIQYxfTwdXwVArspbVM_uC5RYvK4lHghUjZLtpxi3J__bmYORV_bKxZw5F06nRtg9tVXMtfzoaVTayDavC65h3x6ziaONpBWdhV3oQIYKnTAdSTJ62D7BLY2aMKFFWyHp7TPBSnAmopYLaG52D_D4kT8Eapblv7JNwJfejV9JiDQ-v8tkVK-JWLrzdJmz4RkONCcI3QzYdbZ1uZO3ISgRtTomaHc4OX4mYbUQm-7peIwfl556S5dDi6TU-KoNo2tmkVb3e4Kl55Co9DiOtQDW9NPHuH2qoeSRhWxBZZ8WXFV_kzlaG-W84gAY90Sx-A2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bc2eaf0b.mp4?token=HRgt9Dpe2AgI22r8NzMC4GIQYxfTwdXwVArspbVM_uC5RYvK4lHghUjZLtpxi3J__bmYORV_bKxZw5F06nRtg9tVXMtfzoaVTayDavC65h3x6ziaONpBWdhV3oQIYKnTAdSTJ62D7BLY2aMKFFWyHp7TPBSnAmopYLaG52D_D4kT8Eapblv7JNwJfejV9JiDQ-v8tkVK-JWLrzdJmz4RkONCcI3QzYdbZ1uZO3ISgRtTomaHc4OX4mYbUQm-7peIwfl556S5dDi6TU-KoNo2tmkVb3e4Kl55Co9DiOtQDW9NPHuH2qoeSRhWxBZZ8WXFV_kzlaG-W84gAY90Sx-A2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی صبح زود امروز به ناحیه النبطیه الفوقا در جنوب لبنان هدف قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/130279" target="_blank">📅 10:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130278">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وال استریت ژورنال مدعی شد:
حمله ایران به کشتی باری در سواحل عمان، آزمایش توافق ترامپ برای بازگشایی تنگه هرمز بوده است.
🔴
به گفته دو مقام ارشد آمریکایی، سپاه پاسداران انقلاب اسلامی ایران روز پنجشنبه در تنگه هرمز به یک کشتی باری با پرچم سنگاپور حمله کرد و توافق امضا شده هفته گذشته بین ایالات متحده و ایران برای پایان دادن به درگیری و بازگشایی این خط حیاتی کشتیرانی را آزمایش کرد.
🔴
این حمله تنها ساعتی پس از هشدار ایران به کشتی‌ها مبنی بر عدم استفاده از مسیرهای تأییدنشده از سوی این کشور انجام شد.پس از حمله به کشتی سنگاپوری که از مسیر تعیین شده از سوی عمان عبور می کرد، چهار نفتکش دیگر که در این مسیر حرکت می کردند، بازگشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/130278" target="_blank">📅 09:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130277">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-h04qqz9ZlVEQuKCkmgeStwj_P8ro4MzBLIZItMoSVZ2qzN5p3Kb2vlx0NZ0gGi3xxdi6gEWI32URmPQL47I8N-_FJ0yOOvVdG0JvOt6yVPTNtP9xqGlQbekc6EaeCND21GsG-8k4HcxgTqycO7VtXb2M0V1AknEATZo7dzVFjoK5g0dEQ_EqWeWw-Tzrv4-dggR2LXwm8oigXK5CsCM8b-K1shBQ85BUrsfG0c97ocF7y5qw-R5L4hznvjmnw1lUyGWlsAr1CfBfIbaCqSmrq9e0Q-M1tBaMFmRtZUxMsAzTbEBFrG3j4GEKCrkz3EZNrrykEq4SanzVCqHvQvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز ۴ زمین لرزه مرز بین عراق و ایران رو لرزوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/130277" target="_blank">📅 09:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
بهای نفت برنت با کاهش ۱.۷۴ درصدی به ۷۴.۱۹ دلار و نفت خام وست‌تگزاس اینترمدیت (WTI) با افت ۱.۹۶ درصدی به ۷۰.۵۱ دلار در هر بشکه رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/130276" target="_blank">📅 09:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6Q_ygCcQRUGPtPxxqrPo8bNctj7kPeewdj3nqDlGcb63ajarhMBW_7nE0iG73ABXt8ziRLnzYQ1cyomfNr24ITWpy1uoVQbelGkAJPtJynSSxuDDZM_4iwAV4ppAdyK59qe6U9c1I5zb2AAE8APbq10EE164zA7tHb1P0d327BpXh7owJIVj6WdE5OYBe3CRVVt5C-RkJSG468UF6IZS-5CEQazWivDaLt3wbnjLc_eTPcB5DFnoy-VGwizD_kJyLVJrUtqke4AWTkazS2fRHARPHSS_G1lfiUWGZ4HWpd3zz0XfCffH-jRJ4HeGRyEE_OtM_Z7B5mqPNjB1xAHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر امور خارجه آمریکا در امور شرق آسیا:واشنگتن، علیرغم اعتراضات چین، مرتبا کشتی‌های جنگی خود را به آب‌های مورد مناقشه در منطقه آسیا-اقیانوسیه می‌فرستد تا «از آزادی ناوبری دفاع کند!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/130275" target="_blank">📅 09:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130274">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نخستین پرواز دیروز پنج‌شنبه ۵ تیر از مبدأ تهران در ساعت ۸:۰۵ صبح در فرودگاه بین‌المللی کیش به زمین نشست و ورود گردشگران به جزیره به‌صورت رسمی آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130274" target="_blank">📅 09:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ola-frWl6P6tXT6TunJ-XCpS5MHEBDfVnHALSZYkEYNdHi2jW3gIXdfMxVCFIES4QaVK8Ehin7bq2vv6k7eavKBb-Oi6R1vws6lybfhx8JSNbyfPs037vTrvGKE-N5wSCuz-7GwJzXTV6i3mq7xg1vDGin4hPXNuphyHHPG8oH9fRHys3cncH-gaVBMKIyTOTXESUt2D-SWpcqz8IfpX5thJbs5rMr-1tlQzS5KgfYCnZa8XS3nQt18IEwMRtPO6O5AKmjWKW4o8eViklGst0Mf1YbXgIHofEmeIiILC21jRM5Mbw9qZcaXMpzznrWgGwvgBof-FSdpCYoT4tpPLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله شدید اسرائیل به نبطیه/ در ساعات اخیر چندین حمله به جنوب لبنان ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130273" target="_blank">📅 09:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130272">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل: به هیچ وجه قصد خروج از لبنان را نداریم، حتی اگر ترامپ درخواست کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/130272" target="_blank">📅 09:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130271">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
افزایش کشته‌های زلزله ونزوئلا به ۲۳۵ نفر
🔴
سازمان زمین‌شناسی ایالات متحده:
فاجعه احتمالا گسترده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/130271" target="_blank">📅 09:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130270">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6157f55c.mp4?token=ESQFGLHm1P9oe6fTHc1dT7Ctz8IHb2H9Q9YH5Z0O-LA2To_n-c256zQrRS3qXUbmVDnnBhe04KoaewWzq2fnvP16Gd158S2Pqth6wcXQotA-2xMkYGoXfk3-T_wee8V7GXw3Wpr-aOa9H9p1IuSiRBdhFMmqgDHMBfmfTIYi7QCelgRhP3QkgTIBR5N1MWWWK4kdQZoiche8LnlAnkv1CRaYas6Q7fmwbstS5tzN-ADibLsk_6ZjzH4LoxZF6NqwUdkfYie1JQ9efOL7yqTUDMUTIVTNJR1NrcdQBi79grENN_jAsYAOxAUMLwgHq_-BmCHDukGdcDehqVK-BHqV3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6157f55c.mp4?token=ESQFGLHm1P9oe6fTHc1dT7Ctz8IHb2H9Q9YH5Z0O-LA2To_n-c256zQrRS3qXUbmVDnnBhe04KoaewWzq2fnvP16Gd158S2Pqth6wcXQotA-2xMkYGoXfk3-T_wee8V7GXw3Wpr-aOa9H9p1IuSiRBdhFMmqgDHMBfmfTIYi7QCelgRhP3QkgTIBR5N1MWWWK4kdQZoiche8LnlAnkv1CRaYas6Q7fmwbstS5tzN-ADibLsk_6ZjzH4LoxZF6NqwUdkfYie1JQ9efOL7yqTUDMUTIVTNJR1NrcdQBi79grENN_jAsYAOxAUMLwgHq_-BmCHDukGdcDehqVK-BHqV3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از زلزله ۷ ریشتری ژاپن، امروز صبح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/130270" target="_blank">📅 09:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
استیون میلر، معاون رئیس کارکنان کاخ سفید: ایالات متحده در مسیر بستن کامل پرونده پناهندگی قرار دارد و پذیرش تمامی اتباع خارجی را که به دنبال یافتن پناهگاهی در آمریکا هستند، به‌طور کامل متوقف می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/130269" target="_blank">📅 09:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bc8bdc23.mp4?token=kL7IXN2vVTbL0rnZyJ68YAt09-5mZ8FIJNdEAjlll03mowEWhZjdyDnNxbIfLqPfnlCR_8h_AnegKRJuL3lfcMaQMjY5sWuWet6MzKjDgpsgCSS6E_3kBsApwudsqyt5tjRvWMSw_vryDhX4_iu07x8GluyvhR0BoBOsR8rHbmKoLOAHQZuNyUi8ClI4MJOy6D7gXhu2l2RT0OMwMqKPHlEU8YSjA0L93r_gcBy1Dwr4WfPqaXjy6jLoTIn12MWnLXTIxnEdEkh4UZee1urh9WV4ZinCNj8wjlg1-w4guKDU4DZdHRnZR09xd1f9nWoPsIy1b6vAiGpnka0EEwbX1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bc8bdc23.mp4?token=kL7IXN2vVTbL0rnZyJ68YAt09-5mZ8FIJNdEAjlll03mowEWhZjdyDnNxbIfLqPfnlCR_8h_AnegKRJuL3lfcMaQMjY5sWuWet6MzKjDgpsgCSS6E_3kBsApwudsqyt5tjRvWMSw_vryDhX4_iu07x8GluyvhR0BoBOsR8rHbmKoLOAHQZuNyUi8ClI4MJOy6D7gXhu2l2RT0OMwMqKPHlEU8YSjA0L93r_gcBy1Dwr4WfPqaXjy6jLoTIn12MWnLXTIxnEdEkh4UZee1urh9WV4ZinCNj8wjlg1-w4guKDU4DZdHRnZR09xd1f9nWoPsIy1b6vAiGpnka0EEwbX1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ونزوئلا: ما ونزوئلا را در کمتر از یک روز تصرف کردیم و نفت در حال جریان است و ما با آن‌ها بسیار خوب کنار می‌آییم.
🔴
ما می‌خواهیم به آن‌ها کمک کنیم — آن‌ها دیشب زلزله‌ای عظیم داشتند که در مورد آن خواندید، مانند یک زلزله عظیم در کاراکاس. ما می‌خواهیم به آن‌ها کمک کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/130268" target="_blank">📅 09:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گروسی: معتقدیم که مواد هسته‌ای از زمان آخرین بازرسی که در سال ۲۰۲۵ انجام دادیم، منتقل نشده‌اند، اما لازم است این موضوع را به‌طور قطعی راستی‌آزمایی کنیم
🔴
جزئیات فعالیت‌های ما در ایران و ترکیب کمیته هماهنگی ویژه مربوط به روند بازرسی، در جریان مذاکرات مشخص خواهد شد
🔴
آماده‌ایم تا فعالیت‌های فنی خود را در ایران پیش ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/130267" target="_blank">📅 08:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130266">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: ایران کشور زیبای دوست داشتنی و بازار جدید برای آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/130266" target="_blank">📅 08:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130265">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3yj-3AEZVXgu00c376vMOIaK5zsX161TXn_6509XGswILF8cu0wGjL83STm7tJ0cISG8d1TfNyf-CY6q1mC398U5SnheXZTwdPi1vXb2DO_NteVN0Sh_VHRNlF6R_BBDGUYC4OK-yZvENujyur1Sr5A0R4YeaPqkiT67YWULC8MJHnVUGMliD9fFlxOHTm3d6Z3uanxQnrjBPfemjDaEf4IDI2Ehxb8Gh7nXYbvG-dNT9jbgLkh29jWf-xISytj6cadmKVL2UxcE_PXrr0xbVMWnX-R9jVHiabtcywkFmYtATEgAl8Fp_TIWxbL6s2OO_5Pyq1PWMlsy-fyaPQVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا اعلام کرد
تماشاگران می‌توانند در دیدار تیم‌های ملی ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶ که روز جمعه پنجم تیرماه در سیاتل برگزار می‌شود، پرچم‌های رنگین‌کمان را به ورزشگاه وارد کنند.
به گزارش رویترز، این مسابقه هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود و کمیته محلی برگزاری جام جهانی در سیاتل آن را «بازی افتخار» (Pride Match) نام‌گذاری کرده است. ایران و مصر پس از قرعه‌کشی مسابقات با این عنوان مخالفت کرده بودند همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای تاکید کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه را دارند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود در دیدار ایران و مصر که از سوی کمیته محلی جام جهانی در سیاتل با عنوان «بازی افتخار» (Pride Match) معرفی شده است، از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی جلوگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/130265" target="_blank">📅 08:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24211a974.mp4?token=qXfU5Bg_EitKAGLQB9OVVOLqPXe9mZVpwH7H-7qKFT2hw0IivTXTIZA_RyWOSIRlZkE9vpACpII1T1hAIdccYWH15iV32ydCWTwpHsZ1zxFVVKvCRXjoLlFawrpQp8nZbDqRQ0SgxHilVPT3KESs0JOF13Xkje0K_jYymXW9oC-sd-sQqDRWAd9m_OMtFRP2SQeVeXTQJxy46gOlQdbcIJZVlI0cet-7szlyIrRSunC6EQdY5vQI-FsCXyiHyUA2iLa7BKQOFu-mdDDq0phvAwBxMjMzSey54NJ81IQe6pkx8Z4HVraW-yrTm4Dg6bhYeQlGCzMtxJb_NX8TEzxH1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24211a974.mp4?token=qXfU5Bg_EitKAGLQB9OVVOLqPXe9mZVpwH7H-7qKFT2hw0IivTXTIZA_RyWOSIRlZkE9vpACpII1T1hAIdccYWH15iV32ydCWTwpHsZ1zxFVVKvCRXjoLlFawrpQp8nZbDqRQ0SgxHilVPT3KESs0JOF13Xkje0K_jYymXW9oC-sd-sQqDRWAd9m_OMtFRP2SQeVeXTQJxy46gOlQdbcIJZVlI0cet-7szlyIrRSunC6EQdY5vQI-FsCXyiHyUA2iLa7BKQOFu-mdDDq0phvAwBxMjMzSey54NJ81IQe6pkx8Z4HVraW-yrTm4Dg6bhYeQlGCzMtxJb_NX8TEzxH1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رجزخوانی وحید جلیلی برای ترامپ
#گنده_گوز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/130264" target="_blank">📅 08:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130263">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: باید علیه ایران اقدام میکردیم چون داشتن سلاح هستهای به معنای نابودی اسرائیل و خاورمیانه و به خطر انداختن جهان است‌‌
🔴
اگر ایران سلاح هستهای داشت ، ظرف یک ساعت اول از آن استفاده میکرد و ما هرگز اجازه نخواهیم داد که این اتفاق بیفتد‌‌
🔴
ایران سلاح هسته ای نخواهد داشت و به آن موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/130263" target="_blank">📅 02:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130262">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: ایران خیلی می خواهد با ما توافق کند و فکر می کنم احتمالا با آنها توافق خواهیم کرد‌‌
🔴
ضربه بسیار سنگینی به ایران زدیم و اکنون از موضع قدرت مطلق با آنها مذاکره میکنیم‌‌
🔴
قیمت نفت به شدت و به طور قابل توجهی در حال کاهش است و کاهش قیمت نفت با کاهش قیمت تمام محصولات دیگر همراه است‌‌
🔴
تنگه هرمز باز است و دیروز شاهد خروج 19 میلیون بشکه نفت بود که بالاترین رقم در تاریخ آن است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/130262" target="_blank">📅 02:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130261">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: 159 کشتی ایرانی را کاملا غرق کردیم و همه در قعر دریا هستند‌‌
🔴
تنها در یک هفته و نیم ارتش ، فرماندهی ، هواپیما و نیروی دریایی ایران را 100 درصد نابود کردیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/130261" target="_blank">📅 02:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130260">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: روند خرید محصولات کشاورزی برای ایران خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
🔴
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/130260" target="_blank">📅 02:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566bfa2ebb.mp4?token=I2BFPr0NjgIzXdFpUiJWzPAWtALtlA5jTEFVgYALW4UmkKQsaeUKSQFds8ocTbs-sg1MrZrQyeJG5lPn5N1h_DIO64t6vU09pISCQ9CszYsJejsDUX0aenkEcij14aUCbNLbMtgAc_D0bR5pxMzxYvw-umwkdBpRtMu3PxcHDBHfR5a3Ti-tbzK0uTLBKgGXHhULKdJqy26i1s3nfCbat8EspSSkX6BlnSW_qf7Y0qKxpgzhPTl_o9xFKSn3FcaBeMsCWW-hu_QGkxxNnMQjtEbBg3MPoll5L9LJZs9yY2pevoyxjI-3J7rFraRVhiYHANUiMyzlAIysQPfUY-YuDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566bfa2ebb.mp4?token=I2BFPr0NjgIzXdFpUiJWzPAWtALtlA5jTEFVgYALW4UmkKQsaeUKSQFds8ocTbs-sg1MrZrQyeJG5lPn5N1h_DIO64t6vU09pISCQ9CszYsJejsDUX0aenkEcij14aUCbNLbMtgAc_D0bR5pxMzxYvw-umwkdBpRtMu3PxcHDBHfR5a3Ti-tbzK0uTLBKgGXHhULKdJqy26i1s3nfCbat8EspSSkX6BlnSW_qf7Y0qKxpgzhPTl_o9xFKSn3FcaBeMsCWW-hu_QGkxxNnMQjtEbBg3MPoll5L9LJZs9yY2pevoyxjI-3J7rFraRVhiYHANUiMyzlAIysQPfUY-YuDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف امشب با روسری در هیئت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/130259" target="_blank">📅 02:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130258">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
جی‌دی ونس در مورد جمهوری اسلامی ایران:
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/130258" target="_blank">📅 01:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130255">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ls4nBR_bXqDfmZEM1q_K7w4lBRGdgUa7SB9XMy9yo8MLdV3xHkUX_oJhM-R0Dm2cy9s8V3fLXju8dh4qPe36LL5ADRsC7PYMZFEixVbcdcEMWZ1oGfNqR4JkYEnOi93pYFcms-yXdsXWtRO4nolXMzIOqNUUXaE06aYoq57pO5YBMGNk70uvgYPRhojrfsNf3A7zqTsUGLTGZRenM9WYlurWwuGj5DwQsVRVa1p94YhZEeWFvr5FQYCM-29ybiWjxo9mCnck1GS1xu8AsJwtg9miR6gkywaj130Py9HuID-IssQpSBYQcIAxRLHZKsd5Gp8GjLdTrlE1e4qSjrAWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7Sq-52znNjVML_x5vqVY9xdrBTteMHJJ9n3K7-8FCTfEVJjqEb_RuI61Jm_G5Klk2OOIFlE0akjYwbX9K5iqa8lMWamrpFzwaYgozctB8UxN4A-4wzYSeXnwEFs04y-JssMX8XLqmTEjbSg2fWtXFHoduNC597UylRsZ-PXu-S7HM3w6WX5zECzPnWWcLCcgBRJCaH8MeVQS-Ab9ibj7n2qbdeOxckOrLqx5mgwhYwn63IS6078BlJg1pSCrXAhLuJlDaMb0uMBlzpFTxX2dC9OcXd6ElH3ZOzsnGI6pfaOZ-5OBc4NG4G5Q4Rd47VNIIf82mWdbRoNrEagcZjbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOhZnhYRBzku122-wPBozr3Y5gZUV3GO6FZDZ6Ky_KBmMOWkBySije9RlVO25U0p5AB-Yz4KaY_H5CgTQJNbfg9NnO9lw7yzF-nqTVmhyzUWo7IXd2QbkvEB4bewSGqsA-81zU0s1HS_pA_NH_b_mVsZwq6z-uZbqC0bD_GAquMuHI8n9u9Wd3vBkmFOuZPkqLeuC2OZlisuvL1Uzd1_0QnEsIKWuJiaTVZE5kwB1Q-FBIRlWWWS5TPHKkD3SrbS60nLMW8qdh3bEhklCWCWgzkZQ7boag6s3_mhiLNLYJlNsKIU-InHZAM0I3DdjOfO5jWRFL3BWX4O4NFS2_g5-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شهباز شریف هم نتونست مانع بیل زدن پایان ناپذیر پزشکیان برای کاشتن درخت تو اسلام آباد بشه
🔴
شهباز هی میگه نمادین هست ولش کن اما مسعود ول نمیکنه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/130255" target="_blank">📅 01:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130254">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e31799d4.mp4?token=aL2OaUVhni-7cNgWe19XtjWZ2PZMcPn8SGTbg3uCTk41e1u51GAfmkKaS6rMmO8Q6OuHKPG1Q82HWxcFpvtOpRHz0E7JUfa8rThhzS2zonDwEgIliaCjOWHQN0mBPeyRDUl2f4evwOciumKQ5dfn1YmVzSH2CH2YoYiIwi94MSQSjrnOd8Q5u-AonR92bUGGeiqxy9WXdDMRUTC6gqycERpJ-j_YjVvPsiU0T-Mr4YRDxdXXAi7U7Ue2a4_zq9mybxMfVFxiit3fPOHslePTWnpu3CWVQmKBRhUVkupd8MfbVlNB-hIMlezVo4DmQ--PV6qCNj-cvRxUN-T4JLF4FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e31799d4.mp4?token=aL2OaUVhni-7cNgWe19XtjWZ2PZMcPn8SGTbg3uCTk41e1u51GAfmkKaS6rMmO8Q6OuHKPG1Q82HWxcFpvtOpRHz0E7JUfa8rThhzS2zonDwEgIliaCjOWHQN0mBPeyRDUl2f4evwOciumKQ5dfn1YmVzSH2CH2YoYiIwi94MSQSjrnOd8Q5u-AonR92bUGGeiqxy9WXdDMRUTC6gqycERpJ-j_YjVvPsiU0T-Mr4YRDxdXXAi7U7Ue2a4_zq9mybxMfVFxiit3fPOHslePTWnpu3CWVQmKBRhUVkupd8MfbVlNB-hIMlezVo4DmQ--PV6qCNj-cvRxUN-T4JLF4FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یک مداح دوزاری دیگر به پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/130254" target="_blank">📅 00:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130253">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaZOIjjCRXGVM2SsxqGnblQc2Xg51M-PrxaHwKGbbvTJGKbgEn__tG2zoTPi-LHGmLBiyEo3kzV7lavhok02S9tC6vVF3dr5l6Xd6Z0W0z8bbw_wSlgl3G5b6hapALoFZFQTD6C1f4RpaxMVRxETX6iA7OclpFTRykhAlDISYvV9hj1jBuIs0lQB0enQeQKMYbU14npOZbHPNruMR7HG0ZW_1FGRmMn4GUAeFBtzQTnY_b7NCwqqJ2BtDmc3dql9bCBj2qYa9q5RLAfsIB4gytzieqQ5psEp-PCDZqy15BhbCCv0XfB816L4EViGhLgXOgqKpbcAowfwpnzNp1nNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما برداشته یه آخوند که تنها رزرومه‌اش افتتاح شلتر(خونه صیغه یابی) هست رو هر شب میاره راجع به مذاکرات نظر کارشناسی بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/130253" target="_blank">📅 00:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130252">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b6026c629.mp4?token=KEajhxGXAQe74cAkrFt-JC91Sdh8wLnv7Zm2YiwHjtnryxq5hdI_6Cyx4I1ZJFbXXfy6Af6uQfTFURD80aAV1DBOnueIvhzhwQ2dXis5uox4cCMHzE0CCm7yMQ7GZKUCU7eV0QGSPoooSKCjIRLaLf4s54z7ULMHoA3cH699ByzzMNXvLmzC44WxcbcTKrXm-e8YyH1-WIHt7Gz_a9g6FLKp3kQPBSMRXfuSS8iJFKji6FBP9bfXyEWgJlAf_b2IdXdOH2hWdVAHYNLQ67fDGj2fk1agHKLY6ApbyGAmW7iRcuqxiStmbAvy4GYXmkrEZDXTB__aEkmvIFb-UTr3pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b6026c629.mp4?token=KEajhxGXAQe74cAkrFt-JC91Sdh8wLnv7Zm2YiwHjtnryxq5hdI_6Cyx4I1ZJFbXXfy6Af6uQfTFURD80aAV1DBOnueIvhzhwQ2dXis5uox4cCMHzE0CCm7yMQ7GZKUCU7eV0QGSPoooSKCjIRLaLf4s54z7ULMHoA3cH699ByzzMNXvLmzC44WxcbcTKrXm-e8YyH1-WIHt7Gz_a9g6FLKp3kQPBSMRXfuSS8iJFKji6FBP9bfXyEWgJlAf_b2IdXdOH2hWdVAHYNLQ67fDGj2fk1agHKLY6ApbyGAmW7iRcuqxiStmbAvy4GYXmkrEZDXTB__aEkmvIFb-UTr3pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از رهگیری موشک‌های بالستیک اسکندر روسی بر فراز کیف توسط موشک‌های پاتریوت در جریان حمله دیروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/130252" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130251">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c21bf1806.mp4?token=Y4nbVZUu8htGLBQCss56ig2Xzf_1N9IHg2EvR5XoTKhMB5DqxWF530cKQHNPrS5DZinKZJHThRCSRRBO4CI3DE5NByfqUq3WRntJezkAc0nTbnu4vBgAP1PstS_-3UEZFnPQOSvi_SnHPnm7kP9G5fIhcZ2Ea6Mw20e2kyo1FQqQZO5Nztkh4Wn817rvE2CV09HiJVpGCAykcHwkAnk0vd3E7U-unl_kKrgV6Krqwh1rgpvDE7Q98CsD9WD59LPhsyBL1JRl0Ww0CW83UuLwXvQfZDY4wx94LqhNStA5z_JRl2YJJTlUgkEjUCZsXIJeMAtG_dtGDALLl8WG2eCkMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c21bf1806.mp4?token=Y4nbVZUu8htGLBQCss56ig2Xzf_1N9IHg2EvR5XoTKhMB5DqxWF530cKQHNPrS5DZinKZJHThRCSRRBO4CI3DE5NByfqUq3WRntJezkAc0nTbnu4vBgAP1PstS_-3UEZFnPQOSvi_SnHPnm7kP9G5fIhcZ2Ea6Mw20e2kyo1FQqQZO5Nztkh4Wn817rvE2CV09HiJVpGCAykcHwkAnk0vd3E7U-unl_kKrgV6Krqwh1rgpvDE7Q98CsD9WD59LPhsyBL1JRl0Ww0CW83UuLwXvQfZDY4wx94LqhNStA5z_JRl2YJJTlUgkEjUCZsXIJeMAtG_dtGDALLl8WG2eCkMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحید اشتری: واقعیت اینه شکست خوردیم و تسلیم شدیم و توان انتقام نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/130251" target="_blank">📅 00:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPs3-Iz0sOZ-2YmAUDJtL8MIXfySadtcKwLVfYdAOY_8VfVGqoNlIo_8xe9p4ctV2IZkRG8awZ1PnKUW5rASvQdNIgVEX_9lG7-r1fw1unZUZJuMe2-Dw31s8S4qAAhKl6EQzTt2dQvGRj1CYoN0PIHq5xAzK3DusfrQ_Th5AIddTvQSkukv7_AeXHW9SjbSnZUxfGrHQrNGS5iLH2swPKg27gwDvp9EdiAmtQ1Z0jWPuxc4P1IhOyz8g2YaR3G83n9-JXzPcNdCD8A4n6H0YZZX_2xSgAcC9eFj61QFF_HDnzM8h7hH1w8LycOdcSmE-eQk2MMqinI1rqBSG5CpDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzaI_1CHZwTndz7fcFrMnOnx9G4a4Jw5cYdqMGr2kx8BjUi2bJKWoJfvBL8hpYs5CPIzVoH6n2g6AsgszfzHsT2NEix8HkvYJ-anZw9BBxkTFXBQSL3pRtCKjI815DFd8Kf6MP_Bo8naqEjh8wvuh6M4IO1o5ARvYCD0WNkG8SruNsl_rA-wdMehwXBsjGR1CsJn0zICFgIDYwj22Rm69XNUj85_8WLv7YKXwVYAZck0QocBwEhEtyTwfq7rO5uzTNdM5YxiQyr2iHtrpO-153G4LrIU-gHIq9XeTezbToQ25INI-yf0cPJmDQ-k0pcDd83zfU6iCXqYyN4DpzNn-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
محاکمه شیخ "احمد بدرالدین حسون" روحانی و مفتی سوریه در زمان دولت بشار اسد در دمشق شروع شد. او متهم به حمایت و توجیه سرکوب مخالفان بشار اسد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/130249" target="_blank">📅 23:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شبکه المنار گزارش داد که توپخانه ارتش اسرائیل مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/130248" target="_blank">📅 23:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKPy-OYBXRotHy5RNyLYgtbgahRV3PNNbT0Tjdym-NID5FZPTsvs4kcvMVjDZX1nfYp5B-eBtM5TeBmtNatME0-qTo0hY0ZSby5sgcKp3DVDf0-vr60RcNI01IQDWk9eobp1iEPKacNXe3feQslr78CDF3DqrcXz-r3C7Xpc_yMLj-GxwXDdpDPLzJnCyuXE3gqjsh2l1pDoXEhdZ7xFo_OvLrDT_9ibddSMRsF6GmWnga_6A_fN7Ml4vn6RJQROb8dNGwc_-j_rjsi-5KP-Ev6ivf7dmgdW9Yiw5NzRsteuFel7EwJvLjz8MoQYys4fpP7-ITmaiX--4ZqrPS1HWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
آقای جدید گفت برید مذاکره کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/130246" target="_blank">📅 23:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130245">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ارتش اسرائیل: ۶ عضو حزب‌الله رو در جنوب لبنان ترور کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/130245" target="_blank">📅 23:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130244">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0081f0c6.mp4?token=by2FLQzRkqCYUptEW4lDlzwX2Tnode8sb3_FFVLY4-y3bnLgwfG9VxWTQtjH1CM4QOXWk2nmvL6KMybatRVc3GfatkXzhRtjqq4gkrQHY6ED9cmF5e-c8FvDLBzQZmKSw8nWY6tm8atP0SbE4fZATZOIMpwX7GTbRMwJRgtRkyyMhhvFTXjwyOPHM7EGgQJ3dDRxgUxGQSsn-Y3FnEF2hwyQ1LGGUEv_5IkDDSFYs7Z0RxQIOf8vZyVk870lJGaIPy8rBZUFgX5WdB5zrDspjXdxCrPbdk3RuromGc1UClUIarWsizGnhHOV2YnqlJoEcDi-B31I8eMf2EztnRnykg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0081f0c6.mp4?token=by2FLQzRkqCYUptEW4lDlzwX2Tnode8sb3_FFVLY4-y3bnLgwfG9VxWTQtjH1CM4QOXWk2nmvL6KMybatRVc3GfatkXzhRtjqq4gkrQHY6ED9cmF5e-c8FvDLBzQZmKSw8nWY6tm8atP0SbE4fZATZOIMpwX7GTbRMwJRgtRkyyMhhvFTXjwyOPHM7EGgQJ3dDRxgUxGQSsn-Y3FnEF2hwyQ1LGGUEv_5IkDDSFYs7Z0RxQIOf8vZyVk870lJGaIPy8rBZUFgX5WdB5zrDspjXdxCrPbdk3RuromGc1UClUIarWsizGnhHOV2YnqlJoEcDi-B31I8eMf2EztnRnykg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روته از ناتو: این بهار، با مهندسان جوان و بااستعداد در شرکت ASELSAN، بزرگ‌ترین شرکت الکترونیک دفاعی ترکیه صحبت کردم.
🔴
آن‌ها انقلاب صنعتی دفاعی ترکیه را هدایت می‌کنند که به نفع هر عضو اتحاد ما خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/130244" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130243">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49014d9e0b.mp4?token=Scw_u9JzpTeqvN8LSzQB9u-gYrGhoOWLlQcrJJT016-hLnAQ5X9mxjl9D7Qm8KYeI7HQzyCUWgDj7M7YHZ_RhkLftIeKRIKDbdTvRWYxZiRnVj1rwWso6q0g9NGPd_LXGi5I1FQ7xDCJK6ISvHYBkox8FMdu8CTRFjEwkuFGdSoS_vCDE2uNZKtjmoRY5ni21qwhiF4tmAZQRb7kS8rmNFH77ZHr2opjioIkcPgMn2SYNhcKRAmroAUMxoLn1ys--GDd3wj9BcHJYUxF9Hc_uLR536O21y2KwW9gN3cvxc23Ed2jBjJU4FJcedfqVeBp8_htPOE66-w4rIjdeaeqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49014d9e0b.mp4?token=Scw_u9JzpTeqvN8LSzQB9u-gYrGhoOWLlQcrJJT016-hLnAQ5X9mxjl9D7Qm8KYeI7HQzyCUWgDj7M7YHZ_RhkLftIeKRIKDbdTvRWYxZiRnVj1rwWso6q0g9NGPd_LXGi5I1FQ7xDCJK6ISvHYBkox8FMdu8CTRFjEwkuFGdSoS_vCDE2uNZKtjmoRY5ni21qwhiF4tmAZQRb7kS8rmNFH77ZHr2opjioIkcPgMn2SYNhcKRAmroAUMxoLn1ys--GDd3wj9BcHJYUxF9Hc_uLR536O21y2KwW9gN3cvxc23Ed2jBjJU4FJcedfqVeBp8_htPOE66-w4rIjdeaeqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هزینه تجربه کردن GTA VI در ایران، در اقتصادی ترین حالت ممکن: پلی استیشن 5 اسلیم 1 ترا - 112.000 میلیون تومان
🔴
تلویزیون سام 32 اینچ - 26.300 میلیون تومان
🔴
اکانت آلتیمیت GTAVI ظرفیت سوم - 5.500 میلیون تومان
🔴
جمعا 143.800 میلیون تومان
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/130243" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130242">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bu2Xg6INBNIlxWZK7c12NetjugdW44GxQZWKVJVqT3CL5GOOZFs24N5PRnJE1TO5FprYf2u8JwFmuYsCvaJ9MSVpF2p2EI-WxCWzJNbSCS1tlAqqAQv5nyBrfUhxMf_WaSA1op_2v5AAo1oIdtsIsOQnFLhag2NuAOukEnXUPFwUEQXwsGnMAZAvSykmjTI45YyuT69tvBhOTbNgA7CI__9cCQTFM7PT3bXUG_z7a4lLTrPuq6RI6CZz5-cLpTRUzHGxb218iDjuBJieGL6EaYfB7AfKSGcGkARs9tT13Jf2I1L3kKQEspJ910VG_Sf0cyZ4x0WKKbIwiGeJ3hPR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/130242" target="_blank">📅 23:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130241">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q64H-7WleitqNmvvjp2m6o_nCmpyyJYpwDCSkN8PbzW4qfZ3e8VrMZK4mTAFF-3d8NiF5WdX1a3QE-nG58xB3wxfpAzgBSWux7uo8lozl5xZBbaXzdE779L77Bk-FD-21-8OtP1YVeHKLrIBX-kUty63veq0b3SJh5ZdiN4dLlYMFbKZTcCg8TtfAfS2rGM2NPPj9mysZ0ge59HhedhiI0v2hJ0MeCMIcOVoTTvTpLK0yDqmUdMlk9sR09gd0AAv6EFEBUHgGGDTsbeT9_bE-sS9KufKJlghwZKxjL3ncTobBZlK-QKzFkLYJP_bk4YMGmRfV0TlAkg29m2ZxA-5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو سالی که برای پزشکیان یک عمر گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/130241" target="_blank">📅 23:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092b312727.mp4?token=emgoAtPy9i_VxirXWHHK5OsgpigwSddEHs46eBUoTXnZz6MDxs9oyoDMPcjZ_cH6aQJGpXz3SvLBPNd0tDMRYcINAUZe77i8F6KfKB8gC5jL7ebw9v2zYbSQ7Hm4zXODmF6DFEHdI_29F6ImVOCi7q-XTLb255C9rO5G3r7MCGGgmW333ZtLsIlo5Ji_ONPKXWv91337kWjlutTIfks-vQNxvpDpshrwbmD8GOKHjGu_MX-jxtqche6SFFATejM4AfyOGtL8Cpx8O9554jNcna9goJPywEaAgkjN9h_lsdq9mIl5zkRUIqalfdUZkcr5yd1wmDe-bIQAPQo3y3TefA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092b312727.mp4?token=emgoAtPy9i_VxirXWHHK5OsgpigwSddEHs46eBUoTXnZz6MDxs9oyoDMPcjZ_cH6aQJGpXz3SvLBPNd0tDMRYcINAUZe77i8F6KfKB8gC5jL7ebw9v2zYbSQ7Hm4zXODmF6DFEHdI_29F6ImVOCi7q-XTLb255C9rO5G3r7MCGGgmW333ZtLsIlo5Ji_ONPKXWv91337kWjlutTIfks-vQNxvpDpshrwbmD8GOKHjGu_MX-jxtqche6SFFATejM4AfyOGtL8Cpx8O9554jNcna9goJPywEaAgkjN9h_lsdq9mIl5zkRUIqalfdUZkcr5yd1wmDe-bIQAPQo3y3TefA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف در سفر خارجی با هیئت مذاکره‌کننده بدون نقاب حاضر شد اما شب عاشورا در هیئت «ریحانه نبی» با نقاب حضور یافت.
🤔
کجا احساس امنیت دارد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/130240" target="_blank">📅 23:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
چین رسما اینترنت 10G رو راه‌اندازی کرده؛ فناوری جدیدی که سرعت دانلود و آپلود رو چندین برابر می‌کنه و می‌تونه یه فیلم کامل با کیفیت بالا رو تو چند ثانیه دانلود کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/130239" target="_blank">📅 23:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عراق پس از بحران مالی شدید مرتبط با اختلالات صادرات در تنگه هرمز، هشدار داده که اگر گروه صادرکنندگان نفت سهمیه تولید خود را به طور قابل توجهی افزایش ندهند، ممکن است اوپک را ترک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/130238" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
پرواز مستقیم تهران-دوبی از ۱۰ تیر ماه برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/130237" target="_blank">📅 22:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130236">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmbQbzWNtz_c-hn3G6RlaNgNhwKKwvtjFr0-9abL5bcKKDSOFvSruLzZUZChztoQowdWFEwZlG0kXEKzhPPIULSSzZlgehT7kRxOYGQO_2VcRtFAGSc1eZaGERBpkTM1Rat1NTiq4bu60pmuD7Qsu5Z0cUOLZKYro7NBEDZgLr4sP_NSJWGtFZrpF9RFFtqlnpHFqgNZHHuO9va4MO0rpVerkUYn6sB6_Gx5nxiHjfaQCCfn-JF5NxVgQFSZ3cwtomNddPrEjgmGBMzNcSSg2o_3FMgt0ZfLw2SwvvJDB_Y81ZBTLUX43lymIKjbf33NWA2ExBoOBV1LLofL7gyp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/130236" target="_blank">📅 22:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130235">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd7wRzu0S-0VLsj1ajoOVsv2fib2Fal4hLpD9oXbI7ihGsk66Jt3LUjbsSO003Kx3trQUa7dv9yJ7iMK6RWSZu9muEyCz4MkKr92r7z9jD8Bdg5UkdeisaRhOv3BfoKMGlI-INHYdKBQm9N5csY-QX84Tq2iaIwnTy7sVipwMgiG1fnY1D1rzaO35aRiYE2ohFsMDEFEvS-yBg4s-p_-_dUhD5zoiAwZwK2OajevlLWo4_jGtBNHpbjJ0sLUgOMVJy1i4VhrSPK23lnz9Onc0TZLV8zeD9L3xz-zkSg3Tj3okB8_zozb6nFZeNONuUEDlObAmfWCcefiEtkhJtoXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت تنگه هرمز: تبعات عبور از مسیرهای غیرمجاز با خودتان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130235" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130234">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ملونی در مورد ایران: ایتالیا در درگیری با ایران شرکت نکرد.
🔴
در واقع، اگر در درگیری با ایران شرکت کرده بودیم، توضیح دادن ناامیدی مکرر ابراز شده توسط رئیس‌جمهور آمریکا دشوار بود.
🔴
ما با در اختیار گذاشتن پایگاه‌های خود تنها برای فعالیت‌های لجستیکی و فنی و نه برای عملیات‌های رزمی، به تعهدات خود احترام گذاشتیم.
🔴
و زمانی که درخواست‌هایی مطرح شد که فراتر از آن چارچوب بود—و شما این را می‌دانید زیرا به طور گسترده‌ای گزارش شده است—ما مجوز استفاده از تأسیسات خود را صادر نکردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/130234" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130233">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ماریا زاخارووا سخنگوی وزارت خارجه روسیه پنجشنبه گفت، هنگامی که آمریکا و ایران به توافق نهایی برسند، مسکو آمادگی دارد که در توافق بر سر پیش‌نویش قطعنامه شورای امنیت سازمان ملل مشارکت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130233" target="_blank">📅 22:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130232">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروی هوایی یک عامل حزب‌الله را که تهدیدی برای نیروهای ما در ارتفاعات علی طاهر در جنوب لبنان بود، از بین برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/130232" target="_blank">📅 22:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130231">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / ادعای وال استریت ژورنال، به نقل از مقامات آمریکایی: ایران به کشتی باری در تنگه هرمز حمله کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/130231" target="_blank">📅 22:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130230">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
هم اکنون حمله موشکی گسترده روسیه به پایتخت اوکراین، کیف با استفاده از موشک های سنگین و بارشی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/130230" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130229">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نرخ اینترنت مخابرات دو برابر شد !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/130229" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130228">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: طرح تخلیهٔ کشتی‌ها و ملوانان از تنگهٔ هرمز به‌طور موقت، پس از حمله به یک کشتی در سواحل عمان، به‌تعلیق درآمد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/130228" target="_blank">📅 21:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130227">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: اکنون ایرانی‌ها می‌توانند نفت بفروشند و پول آن را به دلار مستقیما دریافت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/130227" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130226">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
احتمال بسته شدن مجدد تنگه هرمز!
🔴
سازمان بین‌المللی دریانوردی از تعلیق طرح عبور از تنگه هرمز تا دریافت اطلاعات بیشتر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/130226" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130225">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / ادعای وال استریت ژورنال، به نقل از مقامات آمریکایی: ایران به کشتی باری در تنگه هرمز حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/130225" target="_blank">📅 21:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130224">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=I3JwuxYybFq7hg2nNARNxgv6H20uNZUC5JHOLP3zySCMhAHmZQsgku9WaYfAnmI1HOt82vvndLYjMLA3XNTS46HVuL9mPAPVaZlDqItGGxHCZgaXEEbjJr4NAmHQOsVvfAfZ03Dpkmp4TcOYlBkdia0zFA1-dk_TL35vAQaEwCUthBAJITJEutiAmXNwD-SH_4xbXgdTSmJvE2mG4SHARsH6s1624A2ssBQrUHn6Tt_h4_yM8eTFztTDFDaBOG-KVvGdeH_CPJiY2Yh4zoBx9tfk_eCJqWbsF4tDADTFRNBPDzkbHRwUdaxvS9luUqBbBsBLKQ_r4_kfxPgmzuLsCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=I3JwuxYybFq7hg2nNARNxgv6H20uNZUC5JHOLP3zySCMhAHmZQsgku9WaYfAnmI1HOt82vvndLYjMLA3XNTS46HVuL9mPAPVaZlDqItGGxHCZgaXEEbjJr4NAmHQOsVvfAfZ03Dpkmp4TcOYlBkdia0zFA1-dk_TL35vAQaEwCUthBAJITJEutiAmXNwD-SH_4xbXgdTSmJvE2mG4SHARsH6s1624A2ssBQrUHn6Tt_h4_yM8eTFztTDFDaBOG-KVvGdeH_CPJiY2Yh4zoBx9tfk_eCJqWbsF4tDADTFRNBPDzkbHRwUdaxvS9luUqBbBsBLKQ_r4_kfxPgmzuLsCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/130224" target="_blank">📅 21:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130223">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر دفاع اسراییل: هر دلاری که وارد خزانه ایران می‌شود به موشک یا پهپاد تبدیل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/130223" target="_blank">📅 21:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130222">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
به گزارش کلش‌ریپورت، ولودیمیر زلنسکی اعلام کرد که عملیات ۴۰ روزه سرویس امنیتی را با هدف اثرگذاری بر کشور متجاوز تأیید کرده است؛ عملیاتی که به گفته او برای وادار کردن طرف مقابل به پایان دادن به جنگ طراحی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/130222" target="_blank">📅 21:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130221">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / برخی از منابع محلی در لبنان و سوریه، گزارشاتی از تجمع نیروهای جولانی در مرز جنوب لبنان را داده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/130221" target="_blank">📅 21:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130220">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وال استریت ژورنال: تهران در مذاکرات با چین و مصر، پیشنهاد خود برای وضع عوارض خدمات بر عبور از تنگه هرمز را مورد بحث قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/130220" target="_blank">📅 20:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130219">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
عراقچی: دولت ایتالیا باید به‌طور رسمی استفاده از خاکش علیه ایران را تکذیب کند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/130219" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130218">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
به گزارش نشریه NRC، هلند در قراردادی به ارزش ۲۵۰ میلیون یورو، هزینه خرید ۷۰۰ موشک کروز روتا بلاک ۲ را برای اوکراین تأمین خواهد کرد.
🔴
این موشک‌ها که توسط شرکت هلندی Destinus ساخته شده‌اند، بردی حدود ۵۰۰ کیلومتر دارند، کلاهکی به وزن ۲۵۰ کیلوگرم حمل می‌کنند و از هوش مصنوعی برای تشخیص هدف استفاده می‌کنند.
🔴
مقامات اوکراینی اظهار داشتند که این موشک‌ها از حملات به اهداف نظامی با اولویت بالا در عمق خاک روسیه پشتیبانی خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/130218" target="_blank">📅 20:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130217">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بازی جی‌تی‌ای۶ در کشورهای بحرین، چین، کویت، لبنان، عمان، قطر، روسیه، تاجیکستان و تایوان ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/130217" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130216">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejsyHCLympfBnKJ2IzWcE0wRmdQRlwASiOIbrnCQXP87mEJ1rijoI4S7ZMwInpci0GUn0srCg2m9uttYAehBN7EEKvejklMBm1I30Bl7nagpnnbrMnTIcjGsJ7NLDwYDdS4YnJa8nWcIIPoq9r-cE457tI0Lm_C2bcF27LHT5CpzM1ep0hk7_ogB-s_0zwqyu9YmUdh66Ci2H4BKbOTLKzVLLyiwAAAqDucmQZeTPkpJnxDZ12BhInE6Z1epU4xS8BF-zk-2XnYmvdaF2fYURriLONEkWQ2ujFoj4ncsUuhMmMd4j6vocIeMIvgpfYnkOuytC-yG4baXMsxcU1BWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظر سنجی فاکس نیوز رسانه طرفدار ترامپ و جمهوری خواهان؛
🔴
موفقیت ترامپ در اقتصاد :
🔴
۳۱ درصد موافق
🔴
۶۸ درصد مخالف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/130216" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/130215" target="_blank">📅 20:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/130214" target="_blank">📅 20:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دبیر کل حزب الله ، نعیم قاسم: صبر ما معادلات را تغییر می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/130213" target="_blank">📅 20:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نتانیاهو: کارهای بیشتری باید علیه ایران و حماس انجام میشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/130212" target="_blank">📅 20:01 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
