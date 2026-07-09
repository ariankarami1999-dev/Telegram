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
<img src="https://cdn1.telesco.pe/file/iJGRUo8UodtOG0uSs40uPHuuESwi33zZducNjZtmhHsZeV7V8AqbNHaxdsQ7S4AzGN1i5qeTsNPthZr0fgRUQQ40eYDibdRyKZ119s6kwX32hI6JZf7npxNI9k6tgXwC1SbwXlvb7fpDZ3rSLW36zPQUqirKi-95sFnqvr1J8_5r7U6t93-NZPVfyJFn56rV_NVMLHyZ233LBy8hlKDiJDmlpj6oCOgZr-PBcVtORHQ9YLigrYHCrXp6e_KEyZbfhGSL3r6iE2l2hGee0V8PVh3z_xYZnFbblAXwpdKz1AOt6JiGLuq30zj10rGIy9YoAd8xZOttxHRCnno364l9jw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 02:17:25</div>
<hr>

<div class="tg-post" id="msg-4353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802171ad75.mp4?token=kJgDcwHZ94m0TqhzZZY_wtgjGO8jsw1d1D08gtyFMsYTfqSRuA5sknwE2ieQ8J3c6XpbZ1n94U7ErpxU98WU8ZPsx2lRQoTpC9GVS9cJ763m9UCzxIG8ljX6z_Fp8m9DYjEB_LbLn553hRaDQXuNllGUXPrFJrIP5XrHiEpjGHSnLeOc59WHQxHjddnuMTWGChwsbR4a9DHDQv2_a851TWvFUGq8fkjny5_oij2AbtvRxh1ZbHquAOWXILuFegE4ne2VMpTSvkj5FinEsCDCTsDR9MlY_DiHO-X8lbzE15d_BqNO_Coezw-x8m8MOxXfTOnL5ygTNGI36dAEJdyh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802171ad75.mp4?token=kJgDcwHZ94m0TqhzZZY_wtgjGO8jsw1d1D08gtyFMsYTfqSRuA5sknwE2ieQ8J3c6XpbZ1n94U7ErpxU98WU8ZPsx2lRQoTpC9GVS9cJ763m9UCzxIG8ljX6z_Fp8m9DYjEB_LbLn553hRaDQXuNllGUXPrFJrIP5XrHiEpjGHSnLeOc59WHQxHjddnuMTWGChwsbR4a9DHDQv2_a851TWvFUGq8fkjny5_oij2AbtvRxh1ZbHquAOWXILuFegE4ne2VMpTSvkj5FinEsCDCTsDR9MlY_DiHO-X8lbzE15d_BqNO_Coezw-x8m8MOxXfTOnL5ygTNGI36dAEJdyh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر کانفیگ میزنید و فرگمنت روی ip ها کار نمیکنه واستون بهتره که از دامنه برای ip تمیز استفاده کنید...
برای مثال بهترینش:
Chatgpt.com
Grok.com
با این مقدار فرگمنت:
Packets: 1-3
Interval: 1-1
Length: 1-7
اگر کلاینت Fakehost داشت:
Google.com
رفقایی که ابتدایی تر هستن داخل ویدیو کوتاه نشون دادم داخل هر مدل گوشی یا کلاینت که کانفیگ میزنید هست
✅
💡
نکته:اگر کندی در کانفیگ یا آپلود ندارید روشن کنید fragment رو عزیزان.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/MatinSenPaii/4353" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/MatinSenPaii/4352" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4351">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=iKDAvkT9xXEa3J5e2rB1Vchwz9XJroTICgrtXEP6EdTprGnouxfjftyIq9KUv6N_yFFVh8RxBrq0N1rFZ9LefGyDIuanKe-UApKGUBq3vw2Lxt1SWclbksvv6nDzRvGQGRgNUBUWxZhiNlkT1TeUIlkkaEO57imjoZKTv_o0Te6uxhLvUp9OagC5exqfmAKfrvcBxnIrwo_ivuch8KIlAyZH6_yKl6_pJnmyQ-fR-k7Fj4Cpwj_Gsnfna9m3hlkyafkGJRoR_E9fGdZYPlGY4tt8sD3DtgrxtDVnGrPWYh42n_mzV3LbB-MtuYf8CRu1zeU_HvPuJTWc22_eQIdz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=iKDAvkT9xXEa3J5e2rB1Vchwz9XJroTICgrtXEP6EdTprGnouxfjftyIq9KUv6N_yFFVh8RxBrq0N1rFZ9LefGyDIuanKe-UApKGUBq3vw2Lxt1SWclbksvv6nDzRvGQGRgNUBUWxZhiNlkT1TeUIlkkaEO57imjoZKTv_o0Te6uxhLvUp9OagC5exqfmAKfrvcBxnIrwo_ivuch8KIlAyZH6_yKl6_pJnmyQ-fR-k7Fj4Cpwj_Gsnfna9m3hlkyafkGJRoR_E9fGdZYPlGY4tt8sD3DtgrxtDVnGrPWYh42n_mzV3LbB-MtuYf8CRu1zeU_HvPuJTWc22_eQIdz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/MatinSenPaii/4351" target="_blank">📅 00:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه
به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/MatinSenPaii/4350" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون، یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1 هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/MatinSenPaii/4349" target="_blank">📅 23:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A1vPCeFKDAcn8UEXWA1YORarJC6bHEyIQLZQi3-fZzxtDvWTG5ogdQw6BDYPTqk0ADzg_lnbVcbiiqTSCDDkvnbsciIoD0OzbJnI8eoZHYs9UEIHGwJddd_jbBOqQWfxiaEOjzmk9iuwQTbbWVhsxVHgc9D20Ifdu26W1qd5hTzLfrIZ22UY20xJznrp8nLQnUmDVL2ogbc9mQXRN58nF1mrXlXuNtAKZjl-WvKO3Pj1F489m-L2pPctnVjrPbwVVqDPetrs0t8-IXZEPHS_Z18ZyuWQsbu6l8mBbSRmJlxOfqYOC4gvL2wZgyPwMxg0U3Ks9zyRUPnY8jbPkvy0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر درست باشه فوق‌العادست
بچه‌های توییتر تست کردن Grok چهار و نیم رو، همه تعریف تمجید کردن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4348" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4347">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون،
یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1
هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4347" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اتهام جاسوسی به Claude Code؛ چین درباره ابزار برنامه‌نویسی آنتروپیک هشدار داد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4346" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه کاری کردن انگار شرطی شدیم
تا نتمونو قطع نکنن باور نمی‌کنیم جنگ شده</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4345" target="_blank">📅 21:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4344">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ObVSH37nBuPLHO9gi0RM_UFC57Iunk_u4fTphuZ47WhzTx8UDlMRJRAnkh6SE3ejaFwDnJwLgywtPUfv5LcT3hrpZhwJV5ztITx_KmgVTt3K_SmK9x7EcC1E2A-0Vtl0__bzYIeRy1zDT9yuxdvKkD_GA6YkgRj8G8rQ2bPBKrqbyWcHfPNDMOlOBURsXcW-87g2Gp852rbY58L0Qr0fj23tvltBWXPuVO8n-8HtAKQv7jtxVwYxORr5iwH-B-2GJVN364jGxi03bmyYyAtZFbHSytyRlVVYf4_brXVncdwBHZXXjVV3kD_FUlBpBhWtvnebyZJNKPCYcuNRptZ7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsChatBot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/4344" target="_blank">📅 20:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4343">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4343" target="_blank">📅 16:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=QwFnzFtNfmtbwWWA3fAitUwtuM5ONu1eicfzX6Td7WN0zurXJ2jlbkROg90EwjALLRj_4XMDS3ZpCCDIzBHJBpjkDi4Vl15hdmXBjoB3alSQjITp8LscvO74gA4qzYE8DtLmHA5DsdfcYaYAYIP9VT43AT0g-NDYfwTBCYU_JIw7kwiTz4J5i9iz2AsgXv4sO720phvZjxmB0X3Oln3dU2uwTMOH-5TE96D0S4zqDnSyQZE-iLGq142sTa7fuM6b4941j-cPniKWspK8Le5t5wCrytKTflhsaaZY7lsHtqB7mTKScNG0A9MhosGx9aw8jJIBAbog6ijcgxalZDVPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=QwFnzFtNfmtbwWWA3fAitUwtuM5ONu1eicfzX6Td7WN0zurXJ2jlbkROg90EwjALLRj_4XMDS3ZpCCDIzBHJBpjkDi4Vl15hdmXBjoB3alSQjITp8LscvO74gA4qzYE8DtLmHA5DsdfcYaYAYIP9VT43AT0g-NDYfwTBCYU_JIw7kwiTz4J5i9iz2AsgXv4sO720phvZjxmB0X3Oln3dU2uwTMOH-5TE96D0S4zqDnSyQZE-iLGq142sTa7fuM6b4941j-cPniKWspK8Le5t5wCrytKTflhsaaZY7lsHtqB7mTKScNG0A9MhosGx9aw8jJIBAbog6ijcgxalZDVPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مقدار زود شروع شد</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4342" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nYMk5ADsiEdTCtsFgaC3fPQXdr_slosakQZunDBCxzzxPLx_TQxIJodngaKoAYQLIdffSAZJJk-rbVlbyjPKtSDEy0zK-nVUAXyvQuZjaeMEduB_z1tQWk1uexNX4U4Uv_aeroXjNzoGElkMteCHfuShtcV3-v95ogwEYNtrMxY1vP_qX-07eZQ8G6-b93xQ7L_nneecLgUIHE1ycf2w9Wyx_qTIL7UzvzmgIJqawCdgd9w5dnzVmveCSV5LcC6nkg67lovlHpqkMLVJcWIrOH4msKllTun1REg8rOr_U2p8l6gCbLx75u865LpGilE03G3auDIykeQO9EA3A9Njyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارادوکس عجیبیه. از یه طرف انگار جدی جدی جنگ شده باز
از یه طرف اینور دارم آموزش می‌بینم و کار می‌کنم با ai
و نمیدونم همین آب باریکه‌ی نت کی قطع میشه دوباره</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4341" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4340">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">احتمالاً من دچار "فرسودگی LLM" (LLM Burnout) شدم!
نویسنده‌ی این مقاله (الک سکولن) یه توسعه‌دهنده‌ست که می‌گه مصرفش از هوش مصنوعی در حد استانداردهای الان کاملا معمولیه، اما اخیراً یه حس خیلی عجیبی بهش دست داده:
خستگی مفرط از خوندن متن‌های تولید شده توسط هوش مصنوعی!
روند کارش این‌طوری شده که دیگه خودش از صفر کد نمی‌نویسه؛ طراحی می‌کنه، طراحیش رو به Claude یا Codex می‌ده، کدهای اونا رو می‌خونه و ریویو می‌کنه. علاوه بر این، روی پروژه‌ای کار می‌کنه که کدهای تولید شده توسط Qwen رو باید مداوم بررسی کنه. یعنی عملاً کل روزش با خوندن خروجی‌های AI می‌گذره. حتی برای سرچ‌های روزمره‌ش هم از ChatGPT و Gemini استفاده می‌کنه.
حالا مشکل کجاست؟
اعتراف می‌کنه که با این ابزارها خیلی بهره‌ورتر شده و قصد نداره کنارشون بذاره، اما تو چند ماه اخیر، یه بخش کوچیکی از وجودش از دیدن خروجیِ مدل‌ها وحشت داره! چرا؟ چون دقیقاً می‌دونه قراره چی ببینه:
فرضیات غلط، توهمات (Hallucinations)، جملات بریده‌بریده‌ی اغراق‌آمیز، و
✨
استفاده‌ی بیش‌از‌حد از ایموجی‌ها
🚀
.
نکته‌ی جالب اینجاست که می‌گه انسان‌ها هم اشتباه می‌کنن و می‌تونن رو اعصاب باشن، اما مشکلِ اصلی با هوش مصنوعی
تکراری بودنشه
. مدل‌های زبانی دقیقاً با یک لحنِ واحد می‌نویسن و دقیقاً یک‌جور اشتباه می‌کنن. سر و کله زدن با یک سبکِ کاملا یکسان و اشتباهات تکراری، اونم به صورت هر روزه، کلا فرسوده‌ش کرده.
این دقیقاً نشون می‌ده که با وجود تمام شخصی‌سازی‌ها (Personalization) و پرامپت‌ها، هنوز هم اون امضای پنهان و سبک خاصِ هوش مصنوعی از زیر دستمون در میره و وقتی تو طولانی‌مدت باهاش درگیر بشید، می‌تونه حسابی روی مختون بره!
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4340" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4338">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bqb7DCuWJRuSRdy12a050ctUykki0cb8eN68qaYABeSaD-wxGf6nPOkgObyWzFAmV_aQTPPZ__5YxzI4U0dN1cZZyIWpY5O3wC_6Iq5X6-YeyFE5Gi39g8mEZyFI7wpopnfeevuCoCOtLvbqQUMq1F1bUJ4hcebyfdd0tqrnqYMVswD3tjMtXOWiAfF0bppYNYzC62G3VkefwEOQ5IIXLP_rPoRvENZ9x3z0eWKN0KeC_wwi5RMDH00yhEakt-XuT-fJ8YL1laujG8V7bXSVAyS9dZSHo45LjA0nTfHMACwePmG3NyrkxwH3aPVqGr2n1M2noKPtxkQwQttZ_1j2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r_t-IKasbSwoDRcvW9pKQAVcLKZ3WPYT7xCWzw0OVXwnrt2POlvV3-y-Bk6ibqDoUsfjBabn8Ia8kLNopW_bSBgc6551vsKbZM-KUbRvnNPRGf4Pal9ZE8wUeEJEtioua30DiW-0_0zHknZinTiNCCi6kCFG3sVMslfvVzfoU4wWpTBUxuHhS_wknDNR1iTI7se2T1291BJoz8mxRR0Tu-FROvaAPGMwF6aecLA0Z-Yofs83d7eUApZwpVe6RBwgJI-qH3--ZKmT6TYMx7InyDPnHGp27d0lfynm9uhEO7HqOspNngGmTXXcF2vRIjl98RpPr6J4PnM-2BcYxOYbuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI  مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:  • Kimi K2.6 • MiniMax M2.7 • GLM 5.2 FP8  بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:  https://infer…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4338" target="_blank">📅 13:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4337">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=XlE9BrFKWn9Aqg6X54jd8im7bSeC-oWVHeF9fe5VpezZilAf5WSWVYWpKzKUY6Qx_IyD8Q8byzShPUNP0oIY6k4uj31onveuetPPoL8cGtwybJOnpuvmBplajGB46FbmfiizuZ48QDb1Kx3YoZIUQqEempp7_gxjGCStUgWCDzRyaycnG8mGNSi9uGME0LYEo78k3aWoCb5hbk26QCCXkVL0mmDgen9F4MfVwkV0YV76mKiDkJKgBTK5FTBnnnYeGBWn765MP1kOu2GJwVRI7vSYOm8nzQw_5Jhksry_PoAKn9yxtiB2x3WBjRcXysCHYKqQlcVzsp6xQp5kn3RaACPT4OVHaE7WtGk_eFAn9Ac4gLDXmlUAk_yCrcINjxNGV7rBx65RKhfwPxabnNYE529JI7i76Kz0CQ92dBhypeLfYeP7Rhxr9z5acDPp9HgrmI2eblkgU8pwE4qE20yrJ4fitZMipIEnmvBraP2v_K-n2uRapgrAP3SmCinC9-59swRgA0U9qHVPHemwvZJezbFCPcMGmdSkkw_sTPYPQd5qqhQh8XjeO7Qi1OyBOtkdILgUK0ljfXX_BoiCmnTOpHOq_UMYeUuogcDX8fZjQ1iVTRQPNi8EGuuFEUi06LvG7l9h4SNx72CW-PSHgB7m0RYZjZ2JW3v7BVU8AYz6AL4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=XlE9BrFKWn9Aqg6X54jd8im7bSeC-oWVHeF9fe5VpezZilAf5WSWVYWpKzKUY6Qx_IyD8Q8byzShPUNP0oIY6k4uj31onveuetPPoL8cGtwybJOnpuvmBplajGB46FbmfiizuZ48QDb1Kx3YoZIUQqEempp7_gxjGCStUgWCDzRyaycnG8mGNSi9uGME0LYEo78k3aWoCb5hbk26QCCXkVL0mmDgen9F4MfVwkV0YV76mKiDkJKgBTK5FTBnnnYeGBWn765MP1kOu2GJwVRI7vSYOm8nzQw_5Jhksry_PoAKn9yxtiB2x3WBjRcXysCHYKqQlcVzsp6xQp5kn3RaACPT4OVHaE7WtGk_eFAn9Ac4gLDXmlUAk_yCrcINjxNGV7rBx65RKhfwPxabnNYE529JI7i76Kz0CQ92dBhypeLfYeP7Rhxr9z5acDPp9HgrmI2eblkgU8pwE4qE20yrJ4fitZMipIEnmvBraP2v_K-n2uRapgrAP3SmCinC9-59swRgA0U9qHVPHemwvZJezbFCPcMGmdSkkw_sTPYPQd5qqhQh8XjeO7Qi1OyBOtkdILgUK0ljfXX_BoiCmnTOpHOq_UMYeUuogcDX8fZjQ1iVTRQPNi8EGuuFEUi06LvG7l9h4SNx72CW-PSHgB7m0RYZjZ2JW3v7BVU8AYz6AL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جالب Amir Hormati مهندس ارشد و پرینسیپال در گوگل در حوزه AI در مورد کدنویسی و Hard Skill ها، اینکه آینده از دید خودش چیه، چه اتفاقی بر سر کدنویسی میاد و به عنوان مهندس نرم افزار روی چه مسائلی تمرکز کنیم، جالب اینکه خود امیر از رول مدیریت به نرم افزار برگشته به خاطر همین!
✍️
Max Shahdoost</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4337" target="_blank">📅 13:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4336">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4336" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4335">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن
مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4335" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4334">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXNFxN6ftMD-A_4O0Y_xTosrH_HmrWyUu6_MX_5sR2sW5C9pvcM6uHcht8hADko-HenqCwLsBIArhR9zMUqCgqQUB83ZgXGwlN1dnJgC6UzEsHGy6RI7jbiKHUvmqxmkfYVUs6-tmDbneCJV4-rEhf_HQkCYxQUEiNxF0J4q6H3_VD67UU33V_W5-dseJ_VTIPRNJnAAOvH0SUMguvP9ob3GIV7788Byfv-qJ9IkUO2yP303tC4axZHCEuZf4DirndRArVVkosAAnW7thvDouHyNzgUkjuI1d-CE8Wqa-IZ51VFw41rSOSM7OKclZ-V6hsYovpMJmapZ2cEQS6UBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI
مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:
• Kimi K2.6
• MiniMax M2.7
• GLM 5.2 FP8
بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:
https://inference.dahl.global/chatKeys
💡
اگر کوکی مرورگر را پاک کنید، می‌توانید دوباره یک API Key جدید بگیرید.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4334" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4333">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sBBlsLkID0MJcRyIlIuTwvTB-OMVMszIYnvBj0FPhDtKFXKzERNCpLPDdADGZnn3fHIuiqlp3mcOzKbHRecFFX-enBrnkzkpyuKitxbYh3lPavDkV41pL1sk4u0olBZfb4ckuoj7C0CL0CKyytYCHum9kuVEbI-JCw0uOnRUHczipiMzYcOvFTsLrsVJtorCeoXg2zp6_52r5oUbjdqHuXFJDIS4e3EErao6c1Rcw-C-sYEbSGoMb5aZXem4t7_S8AvHL-a2bPN8DUQqtpQR_5DVQq9VxQVWkKG45VT_foF8gk5U7xQ_HAssHRCguxGh8YiyB-kGWP6wLR7SE4Vmug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست، کامیونیتی Rust هستن
😂
😂
زبان Rust برخلاف go و پایتون و... از Garbage collector برخوردار نیست.
نفر اول گفته انقدر سینتکس افتضاحه که دلم می‌خواد زبان rust رو بندازم توی آشغالا(garbage) و نفر دوم ریپلای زده که اگه بندازیش توی آشغالا کسی نیست جمعش کنه چون این زبان آشغال جمع‌کن(garbage collector) نداره</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4333" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4332">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگر می‌خواید اکانت Claude بخرید، بهتره بدونید علت بن کردن‌های کلاد distillation attack هایی هست که اخیرا بهش شده؛ و حتی کاربرهای خارجی هم یهو اکانتاشون بن شده. بهتون دوتا توصیه می‌کنم.
1- به هیچ وجه از سایت‌های ایرانی نخرید. و حتما بدید دوستی، آشنایی، چیزی بگیره از خارج کشور. اگر ندارید، برید سراغ توصیه‌ی دوم. احتمال بن شدن داره به هر حال و ریسکش پای خودتونه. من خودم به شخصه هنوز بن نشدم(نمیدونم شانسه، یا چون دوستم از خارج از کشور واسم گرفت)
2- اشتراک Codex بگیرید در عوض و یا نهایتا اگر کار خیلی واجب دارید و می‌خواید حتما کلاد باشه، cursor بگیرید اما کرسر خیلی زود تموم میشه طبق تجربه‌ی شخصی. به نظرم Codex سخاوتمندانه‌تره به شدت. و صبر کنید تا وقتی که بن شدناشون شدتش کمتر بشه.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4332" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4331">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نشت مخفیانه‌ی دیتا از ریپازیتوری‌های پرایوت گیت‌هاب با یه ترفند ساده‌ی هوش مصنوعی
📚
فکر کنید یه نفر بدون هیچ پسورد و دسترسی‌ای، بتونه کدهای مخفیانه‌تون رو توی گیت‌هاب بخونه. چطوری؟ با گول زدن ایجنت هوش مصنوعیِ خود گیت‌هاب!
تیم Noma Labs یه آسیب‌پذیری خیلی خطرناک (به اسم GitLost) توی سیستم جدید Agentic Workflows گیت‌هاب پیدا کرده. داستان از این قراره که این ایجنت‌ها می‌تونن issueها رو بخونن و اتوماسیون انجام بدن.
🫵
حالا هکرها چیکار می‌تونن بکنن؟
هکر کافیه بیاد تو یکی از ریپازیتوری‌های پابلیک شما یه Issue باز کنه و توش یه سری دستور مخفیانه به زبان انگلیسی (Prompt Injection) قایم کنه.
ایجنت گیت‌هاب این متن رو می‌خونه، گول می‌خوره و به جای کار اصلیش، میره فایل‌ها و دیتای ریپازیتوری‌های پرایوتِ همون سازمان رو می‌خونه و برای هکر می‌فرسته!
نکته‌ی جالب اینجاست:
گیت‌هاب کلی گاردریل امنیتی چیده بود که دقیقاً جلوی همین اتفاق رو بگیره. اما محقق‌ها فهمیدن فقط با اضافه کردن کلمه‌ی "Additionally" (به‌علاوه/همچنین) توی پرامپت هک، مدل هوش مصنوعی کلا گیج می‌شه و به جای اینکه درخواست رو رد کنه، تمام محدودیت‌ها رو دور می‌زنه و دیتا رو لو میده.
این دقیقاً نشون میده که توی سیستم‌های جدید هوش مصنوعی، همون متنی که ایجنت می‌خونه همزمان می‌تونه پاشنه آشیل و نقطه حمله باشه. حملات Prompt Injection الان دقیقاً دارن همون بلایی رو سر AI میارن که قبلاً SQL Injection سر وب‌سایت‌ها میاورد.
البته این باگ به طور مسئولانه به گیت‌هاب گزارش شده، ولی حواستون به ایجنت‌هایی که به سورس‌کدهاتون دسترسی دارن باشه!
منبع:
https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4331" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4330">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی فارسی، ویدئوی 10 کایی کم کمش 200 تا کامنت رو میگیره و خیلی از یوتوبرا هم جواب میدن و اهمیت میدن</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4330" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4329">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها: https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو: 1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم 2- با همدیگه…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4329" target="_blank">📅 16:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4328">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuN9OmUBpn7Wug5WoZySV1dj9POXEoDmWokCVp8ofIe-Qw-pD170DBb7gPB_9NemSzNHskxOsBIBwnxgFA0intyf4kLAUPomilVsZO5mODan0LOcT9oSUYYxDO7ILRUHThspN6V-4mvhnt8u0P4mjNkbfqsZqMzqO4h_t9P28tQOtQYvWFFW9ajxIIv3wUH4qjHomkjN8tP4U4eBAfY4g4yJ3MGgTDTOrvtuyXHTjm9lFMBcpHhE6qp6VwnRU1yUKN9eiGkwStHcXz2ijItD5cIdW0il0YAR0sECCShbEyAD9nzXR0G27XQcCNp2FzYs1EVjhoMFl1JZykvBHHihfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها:
https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو:
1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم
2- با همدیگه OpenCode رو به 9Router وصل میکنیم و روش دور زدن یه باگ خیلی رو اعصاب رو بهتون میگم
3- از هرمس استفاده میکنیم که با سامانه پیامکی، یه کرون جاب بنویسیم(قابل پیاده‌سازی برای هر ایده‌ای)
4- و کار با پنل‌های پیامکی رو بهتون یاد میدم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4328" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4327">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zombie</div>
  <div class="tg-doc-extra">Bad Wolves</div>
</div>
<a href="https://t.me/MatinSenPaii/4327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4327" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4326">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خب انگار فعلا خبری نیست
نت منم اوکی شدش</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4326" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4325">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4325" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4324">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=rKb3InbWINSFTbaMYzcamB8MDOeoHVrl2byb7IneRV7MsIfg-NF4xcHp1Zycw4EoYz40Ypwxp-qtiTBpzqoYcjQi289QZe2upoC8-SZhPebHljm6Uw1fXxW-5gMDNzJaVNuWPw1TU8Aj-43lQ3AELxwpefZI2K2c7R-R_IapFh_q6rPc3aj6_Eej8r5gzJDiF_GVux8rResJ5eUXRgHJeoDCUUpSELm42QUiLX8Y3dl3PikLjUa8kP5JUBj1ES3VJbU7a8mLOlHHGvowLEwUyq7nxqG3cEJ2BuvJvowSKFTKPydT_oprSSRGUxbS983TLAv9S-KLd_Q1jlOFxFapRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=rKb3InbWINSFTbaMYzcamB8MDOeoHVrl2byb7IneRV7MsIfg-NF4xcHp1Zycw4EoYz40Ypwxp-qtiTBpzqoYcjQi289QZe2upoC8-SZhPebHljm6Uw1fXxW-5gMDNzJaVNuWPw1TU8Aj-43lQ3AELxwpefZI2K2c7R-R_IapFh_q6rPc3aj6_Eej8r5gzJDiF_GVux8rResJ5eUXRgHJeoDCUUpSELm42QUiLX8Y3dl3PikLjUa8kP5JUBj1ES3VJbU7a8mLOlHHGvowLEwUyq7nxqG3cEJ2BuvJvowSKFTKPydT_oprSSRGUxbS983TLAv9S-KLd_Q1jlOFxFapRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The Return of
قدرت مذاکره</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4324" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4323">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4323" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4322">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4322" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4321">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">روی اینترنتای خود من به شدت اختلال هست
همراه اول که به زور چیزی باز میکنه
ایرانسل 4g+ اما هیچی به هیچی. آپلود 0
فیبر مخابرات هم از صبح 2 دقیقه وصله 20 دقیقه قطعه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4321" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4320">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4320" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4319">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4319" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4318">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4318" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4312">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4312" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4312" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4311">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4311" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4303" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXhB5575hXje31ZETn7JpbwPviNz5eC1YIUKfRuyRp2Ft4xFx3MBLMQ9fEgCDibmmeWM92G91xK011TnQa9u_F5JzyeK60Ej2hz7BWu2ZFqJ9GjZat3XlrriJJS54uW_qWc6di7i60i8cnAoaboOnubMBijM56rN95z-Xo94PIWjJ9ABZd_j8W25GTFUACku24BukSVHotu6l0_EcxCx8TEKTd6AZ9qmysJFjVG4khgoS68uFrAhd69Fo_mActcH8DXKgmVlBr5TgEal_oXnM8k2QtkJvBnCI1Fs33Ve2Wjl4u9jZvazcdhA7t5ghRrSo7rOycnicWVdmG3wmCh--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4302" target="_blank">📅 11:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اعصاب و روان نموند برامون. نمیدونیم درس بخونیم، کار کنیم، کارگری کنیم، لپ تاپو بفروشیم و دلال بشیم که بتونیم زندگی کنیم، چیکار کنیم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4301" target="_blank">📅 11:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">میترسم پنج دقیقه بخوابم ببینم نت قطع شده باز</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4300" target="_blank">📅 11:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4297">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OR5PJIZP55m7IgbJTIOgLpLLL_Pa48qWBfUYMZmtIpLbMYrGrIJT8U0LpId5FH5cUmiJPZ7d1MDr0dFT1jc7beIgNra_VtjPt15U2B03WVX7aeD0dvgVJ5qYkihyw2kAPq7zpgCp2IsPhf4pA4xpynWu4A3aJQNbfRURgpfHynCsMAdrRvUHUsFkyV9sakQVEs47-d0Td_LRHibB-cDRXVS1Abo4oued7xErAwX4HGfcYUxlgTkaa8rQsMZoWJobA3Q7TofEzsGj1VPIL74DnuRlUWHLbIX9EcxaJ1uTQ_tRVP7Ssp_zaDLGXw2uNzjQ5b_UdWyJCMEowa-VHWW1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZPQRvmrH7EIjsr0p3JOWzJbHN-CgEYFHNqc00Sm1u_CSlS_0QEstMZcr4VHtI69-FfgO5-kU5qtrFOxItV9kXlwhMczofy6DWLJAl_Gbhf7EpBzZYot4VEx9T9hME3rQxqDsylRalG0xG8fbvj4UtZdX-31gTPp9As18M3Lsg33DCNFhmzsEHYNDhl-_gQPbufuBABtCTou9SOIwdnngPqSenlYmkMue7ajbr1vQOrrWfxuQ37WbYGlMWmTseWw1onye-NoTKp11mo1GZYyNRv7ityestWGM6zdT6TvgRoH8jC661VEGUB_No9XYWDOTp-bi73UhIV89GNJHkwsiRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X2Igd-WSdwVIL-RQpOMQqkgDl-lmJ72XSajzrY_J7iMUd4FAUjSRd9sNnd6Mkb2NWO_mPocb3orzScJV3BcARClWh1wv4vGBx7Y5E3AERQxZVw8JT-zvDbAdyorjnQqAGAFAbDdKz4YMYC8rOWXMvY3OjFvLJo7kxbsZmyI4N70V3xoHv-n2sof1vLzkEtoK9M5cFcKZhnUsuOzhhz0_qlj6IuQCPmsLoqfCjQ3WN6oQMaxHyjNrtAWxa3BCy51alBELwJaP5xqTwDHEhx9MauOjs-Q4p4ribdvQD2PydIV1PhrIrbYMpdnULu6EOrOKshFSfoHOtAb1bcXkzpfFyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی هزینه‌ی هوش مصنوعی از حقوق مهندس هم بیشتر می‌شه
خلاصه:
شرکت «آنتروپیک» (Anthropic) حدود ۲.۳ برابرِ پولی که بابت حقوق و دستمزد می‌ده، خرج زیرساخت و پردازش (Compute) می‌کنه! یعنی با حساب حقوق سالانه ۲۲۴ هزار دلاری (با احتساب تمام مزایا)، سالی ۵۱۵ هزار دلار به ازای هر مهندس خرج پردازش می‌کنه. در حالی که ۱ درصد از برترین شرکت‌های نرم‌افزاری فقط ۸۹ هزار دلار و شرکت‌های میانه بازار (میانه آماری)، کلاً ۱۳۷ دلار خرج می‌کنن. حالا ۳ تا سناریو برای سال ۲۰۲۹ داریم که نشون می‌ده این شکاف عمیق چطوری ممکنه پر بشه.
همونطور که اشاره شد، آنتروپیک ۲.۳ برابر حقوق پرسنلش، در حال حاضر داره خرج زیرساخت و پردازش می‌کنه. با حدود ۵,۰۰۰ تا کارمند و تقریباً ۱۰ میلیارد دلار هزینه‌ای که توی سال ۲۰۲۶ برای آموزش مدل و استنتاج (Inference) می‌کنه، سهم هر کارمند سالی حدود
۲ میلیون دلار
هزینه پردازشی می‌شه؛ اونم در مقابل حقوق و مزایای کلانی که برای هر نفر احتمالاً بالای ۵۰۰ هزار دلاره!
بقیه بازار نرم‌افزار خیلی از این رقم‌ها عقب‌ترن. ۱ درصد از برترین شرکت‌ها سالی ۸۹ هزار دلار به ازای هر مهندس روی هوش مصنوعی خرج می‌کنن؛ یعنی ۴۰ درصد از یک حقوق ۲۲۴ هزار دلاری برای یک مهندس ارشد. این رقم برای شرکت‌های میانه بازار فقط ۱۳۷ دلاره! اختلاف فاحش اینجاست:
۲.۳ برابر حقوق
در لبه‌ی تکنولوژی
۰.۴ برابر حقوق
در صدر بازار
نزدیک به صفر
برای شرکت‌های معمولی بازار
حالا بقیه‌ی بازار چقدر می‌تونن خودشون رو به این سطح برسونن؟ جواب این سوال توی ۳ تا سناریو خلاصه می‌شه.
(توضیح نمودار خطی(عکس سوم): نمایش سه سناریو برای هزینه‌های هوش مصنوعی به عنوان درصدی از حقوق مهندسان تا سال ۲۰۲۹؛ در سناریوی خوش‌بینانه، این رقم به رکورد ۲۳۰ درصدی آنتروپیک می‌رسه)
سناریوی بدبینانه (کاهش قیمت توکن‌ها برنده می‌شه)، سناریوی پایه (رشد ۱ درصد برتر بازار کند می‌شه)، سناریوی خوش‌بینانه (بقیه بازار تا سال ۲۰۲۹ به نسبتِ هزینه آنتروپیک می‌رسن). هر کدوم از این سناریوها، هزینه سالانه هوش مصنوعی به ازای هر مهندس رو نشون می‌دن(عکس دوم)
توی سناریوی خوش‌بینانه، فقط هزینه هوش مصنوعی به ازای هر مهندس، با کل درآمدی که یه کارمند توی شرکت‌های معمولی SaaS تولید می‌کنه برابری می‌کنه! همین الانش هم شرکت‌های آنتروپیک و اوپن‌ای‌آی به ترتیب ۱۴ میلیون دلار و ۶.۵ میلیون دلار به ازای هر کارمند درآمد دارن، که بالاترین رقم توی لیست ۲۰۰۰ شرکت برتر فوربز (Forbes Global 2000) به حساب میاد.
ساختار هزینه‌ها، دقیقاً جا پای ساختار درآمدها می‌ذاره.
موتورهای محرک توی سناریوی خوش‌بینانه:
قیمت مدل‌های پیشرفته ثابت می‌مونه، چون هزینه‌های آموزش به ثبات می‌رسه و تقاضا از عرضه جلو می‌زنه. فرآیندهای کاری مبتنی بر ایجنت (Agentic Workflows) نسبت به چت‌های معمولی، چند سر و گردن توکن بیشتری مصرف می‌کنن؛ طوری که «گلدمن ساکس» پیش‌بینی می‌کنه مصرف توکن تا سال ۲۰۳۰ حدود ۲۴ برابر بشه. تازه، اگه شرکت رقیب قابلیت‌های جدید رو سریع‌تر عرضه کنه، دیگه پرداخت صورت‌حساب هوش مصنوعی یه انتخاب نیست، بلکه یه اجبار حیاتیه.
ترمزها در سناریوی بدبینانه
: قیمت توکن‌ها توی سه سال گذشته، هر سال ۱۰ برابر کاهش پیدا کرده. مدل‌های متن‌باز (Open-weight) دارن با کسری از هزینه‌ها، شکاف کیفی رو پر می‌کنن. از طرفی شرکت‌هایی که مصرف هوش مصنوعی رو بر اساس نقش یا حجم کاری کارمندان سهمیه‌بندی می‌کنن، می‌تونن شیب این نمودار هزینه رو خم کنن و کاهش بدن.
نظر شخصی: اصلا نمیشه پیش‌بینی کرد:) با اومدن ایجنت‌ها، سناریوی توکن داره مطرح میشه. از اون طرف، چین غوغا کرده و با رایگان عرضه کردن مدل‌هایی مثل MIMO و GLM-5.2، واقعا نمی‌تونم نظر بدم.
منبع مقاله:
https://tomtunguz.com/ai-spend-breakeven-2029/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4297" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4296">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه مقاله از نیویورک تایمز(با اینکه ازشون خوشم نمیاد) دیدم که توی هکرنیوز بحث‌برانگیز شده. داستان در مورد اینه که با پیشرفت سریع مدل‌های زبانی، مهارت‌های کسایی که فلسفه خوندن، چطور توی بحث‌های اخلاقی هوش مصنوعی و Alignment مدل‌ها داره به شدت کاربردی می‌شه. و انگار یه بازار کار جدید داره برای این رشته شکل می‌گیره =)
لینک مقاله:
https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4296" target="_blank">📅 23:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4295">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4295" target="_blank">📅 21:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4294">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4294" target="_blank">📅 20:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4293">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Js6Kbe3-_UI2Fpe7T9QDSmLsEDeRLKYL2ATCw0WTlcXrSa6WPSLSzA-pC9iVWkUBvyvJAZDFy6a3OYZXfvqDFRS3pB114BAZhG7PAXOuJsLnJt8-Q3tL0f897EbuIjlCpJUgf7K2JxqNrFcwQ7ayLMGuUhh5eE0sD0RLVEaqniDxsjnoCfhzfpjsDzPP8o0WlkkEBc7uGFfPZj3A4rvksKaFi-X0n7mqwkSCqnTIZSW_1-p4R9LOdE2qzB8hQHwdacDVu9IqMzbe8oMBzzK1lA7J5vT_pVVZcl9MSUrc219Z8F4VqXT7IEVGGSt8_d-HYB33yEqTT1wRYH9KRQvgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبان برنامه‌نویسی Cyrus(کوروش) چیست؟
سایروس یک زبان برنامه‌نویسی متن‌باز و جدید است که برای ساخت نرم‌افزارهای زیرساختی و سیستمی طراحی شده؛ یعنی همون نوع نرم‌افزارهایی که نزدیک به سخت‌افزار کار می‌کنن و به سرعت و کنترل دقیق نیاز دارن (مثل سیستم‌عامل، درایور، یا ابزارهای زیرساختی).
فلسفه اصلی سایروس این است: هیچ اتفاقی پشت پرده و بدون اطلاع برنامه‌نویس نیفتد. یعنی کد باید همیشه روشن و قابل پیش‌بینی باشد و برنامه‌نویس دقیقاً بداند هر خط کد چه کاری انجام می‌دهد، بدون رفتارهای پنهان یا پیچیدگی‌های اضافه.
چند ویژگی مهم سایروس:
بدون گاربیج کالکتور
: بر خلاف خیلی از زبان‌های مدرن (مثل پایتون یا جاوا) که حافظه رو خودکار مدیریت می‌کنن، سایروس این کار رو به خود برنامه‌نویس می‌سپارد. این یعنی کنترل کامل و دقیق‌تر روی مصرف حافظه، که برای نرم‌افزارهای سریع و حساس خیلی مهمه.
کامپایل مستقیم به کد ماشین
: سایروس از فناوری معروف و قدرتمند LLVM استفاده می‌کند تا کد رو قبل از اجرا به‌طور کامل به زبان ماشین تبدیل کند؛ نتیجه‌اش برنامه‌ای سریع و بدون واسطه است.
سازگاری استاندارد با سیستم‌عامل‌ها
: طوری طراحی شده که به‌راحتی با نحوه‌ی کار سیستم‌عامل‌های رایج هماهنگ باشد.
سینتکس ساده و مینیمال
: تلاش شده که نوشتن و خواندن کد تا حد امکان ساده و بدون ابهام باشد.
قابلیت‌های پیشرفته بدون هزینه اضافه
: مثل ژنریک‌ها (نوشتن کد قابل استفاده مجدد برای انواع مختلف داده) و چندریختی (Polymorphism)، بدون این‌که سرعت اجرای برنامه رو کند کنند.
ساخت افزایشی (Incremental Build)
: یعنی موقع تغییر کد، فقط بخش‌های تغییر‌کرده دوباره کامپایل می‌شوند، نه کل پروژه؛ این باعث سریع‌تر شدن فرآیند توسعه می‌شود.
هدف کلی سایروس این است که زبانی باشد نزدیک به سخت‌افزار و ماشین، اما بدون این‌که خوانایی و سادگی کد قربانی شود.
این پروژه هنوز در حال توسعه است و به‌تازگی نسخه بتا (Beta) آن منتشر شده. اگر دوست دارید بیشتر بدانید، امتحانش کنید، یا در توسعه‌اش مشارکت کنید:
مستندات:
https://cyrus-lang.ir/en
گیت‌هاب:
https://github.com/cyrus-lang/Cyrus
کامیونیتی:
@cyrus_lang
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4293" target="_blank">📅 18:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4292" target="_blank">📅 16:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4291">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دیروز و پریروز می‌خواستم ویدئو بذارم، اما با اینکه موضوعات زیادی دارم برای ویدئو ساختن، حس کردم که کمی عجولانه‌ست و تایم گذاشتم که هم خودم کمی بیشتر با ابزارها کار کنم، هم وقت داشته باشم برای مطالعه‌ی شخصی که محتوای باکیفیت‌تری ارائه بدم. برای همین تا وقتی حس نکنم کافیه، ویدئوی جدیدی منتشر نمی‌کنم
❤️</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4291" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4290">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wksyc5xiyh1Y9yHPedakl_ejMtTRQKP9CFjZY6N2alMTDe12jEXLpykG4IWAVmdMXsREiKYxnRvSNjQ6SVAYzsimOR1yguO3aJdO4bc54cPocym_13uAk30NnPF8GI8gGAK7yaJJoFNbph4_Z5WVvc1nFpl6sFDi1GgOAKLr2aKL9JjGap72RYcRz1Q754-VyvX5JbEDDGDgKC2S41lc7hji_vmY09z09XxmQVo2ebDb2QLmAbRh4QdtRTp_6W1B-vLXQWjK6KvE2J6xuU2wDb2K0998sGtWRv0De_7itXhD6w_3MlfJyxmn1Bkp6q7ooOTc359B_5wfOOGOY-pN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا هزاران پست سیو می‌کنیم ولی هیچ‌وقت نمی‌خونیمشون؟
🤔
اسم علمی این رفتار
Digital Hoarding
(ذخیره‌سازی وسواسی دیجیتال) یا "
پارادوکسِ بعدا می‌خونم
" هست.
این اصطلاح رو اولین بار
Van Bennekom و همکارانش توی سال ۲۰۱۵
و داخل یه مقاله توی مجله‌ی
BMJ Case Reports
مطرح کردن؛ اونجا یه مورد بالینی رو توصیف کردن که یه مرد ۴۷ ساله هر روز حدود ۱۰۰۰ عکس روی کامپیوترش ذخیره می‌کرده بدون این‌که هیچ‌وقت سراغشون بره.
از اون موقع، این پدیده به یه حوزه تحقیقاتی جدی تبدیل شده. تحقیقات جدیدتر (مثل مطالعه‌ای که سال ۲۰۲۳ توی مجله
Journal of Obsessive-Compulsive and Related Disorders
منتشر شد) نشون می‌ده Digital Hoarding با الگوهای شناختی و هیجانی شبیه به اختلال وسواسی-جبری (OCD) و وابستگی هیجانی به اشیاء مرتبطه؛ یعنی حذف‌کردن یه فایل یا پست، همون حس ناراحتی رو ایجاد می‌کنه که دور انداختن یه وسیله فیزیکی.
چرا این اتفاق می‌افته؟
👩
هر بار که پست مفیدی رو سیو می‌کنیم، مغز دوپامین آزاد می‌کنه؛ حس «پیشرفت» بدون این‌که واقعاً کاری انجام داده باشیم.
✈
ترکیبی از
FOMO
(ترس از دست دادن اطلاعات) باعث می‌شه به‌جای مصرف محتوا، فقط جمعش کنیم.
💤
نتیجه؟ انبار دیجیتالی از Save‌ها و بوکمارک‌ها که عملاً هیچ‌وقت سراغشون نمی‌ریم.
چندتا راهکار عملی:
قانون 5 دقیقه
: اگه محتوا کمتر از 5 دقیقه وقتتونو می‌گیره، همون لحظه بخونید؛ وگرنه رهاش کنید.
سقف هفتگی
: حداکثر ۵ تا ۱۰ آیتم توی یه هفته سیو کنید تا تلنبار نشن.
دسته‌بندی و پاک‌سازی دوره‌ای
: هر چند وقت یه‌بار Saved items رو مرور و پاک‌سازی کنید.
اگه واقعاً مهمه، به‌جای سیو کردن، همون لحظه یادداشت بردارید یا اجراش کنید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4290" target="_blank">📅 16:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4289">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4289" target="_blank">📅 15:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4288">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S-4ryWPeXGMIhBtxtW1f5Oth-uRtE-44myT9n2VWr8M6c-lmHA1vuAQGP3NzyLYIu3Cox9kssHDAotEw3x9TZUDQgUtgDoJC0QxGuqtH97984uJ2ohm211KUIXnA2nGDT4DfWBkHgwbYw71lABuLeH0Y89BKzLCfM1qu-zQoPVDUIYZBO0PdpWo1TfRH5mEj5XD0Jqa_NC0UBDMfNbyBxOjNCkXdtsEyuEGSxQ5msB3s-zsrO4qPalx6nrgMVZi6KeWMfezPa8xobuBreGgf1He1dI5tBTjuciAiC6GOAP-MjCOwXUW1z2f30Z1_zoLdmvKaIxnylHd1G8nYuKPU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر، خیلی راحت با قابلیت Browser که اینجا: https://youtu.be/_30_ng3Hyfs یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4288" target="_blank">📅 14:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v8oOuHadnu8uzkFXWbuTcFwn8wZhmSowiuWrj9_9tfKnrc2GI1p83M1Mro9v59bw1p1S4dz_MK6fWMwswEAScQTDMxLK3D-dLn9jxU72gNOoHLNlWEbpFbhgfTlRF85T0VeV7e63XFrLH95dVL9oeT8jl5hmyNypGr328phTi2zDJa94k0JwqdmeZt-sEfPGTr5WtYu0nmdQlG7tXLccyPIlkyHeP7xhVsZ03kP1ffCxhKfl64fcWHeYPT1Vwu6abglHTSOzfV-nV7mo4B2miiZbbDDZoXIo3arwtK0Ut0nbEeVmxEJqe1yTNW-7zFnZSwtvsshmlaY3Yj2KxkvU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nt2LnhvwvHR6xsESy8YckZpkiUrIUQlzUYQSzVU1KW4BDRq5GkQtB7Z9ZTWv9T5r2v_2HY3na5UIwEb2mVntLofe8i5FSdPdib1sBIBtWpDl1wVnL0GA96drJeqy_0lY55tLRMozCahZfNjQcV4Cf0r-KMrQQS759xzigWcfWlChhGpIP-oTGn4WkBF4N3pF0KfWt_eD9dAvXFJzXKhAStY0uJQuueXcUt6viEAXDeC_xspj4td9EGl9rsHQxZfLuMu0WYUVLIuQhvifrRKuHxFfZsyNOw-i5Za8zNKzVHHE2lgHpedT7Z49A07-JOWuTL2SkdyQjQmJXjDePrieIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر،
خیلی راحت با قابلیت Browser که اینجا:
https://youtu.be/_30_ng3Hyfs
یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4286" target="_blank">📅 14:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/okRwqzxtM0QMYmOMer4PiqcOmy6DeYujXpe4n7nxolR9Q8ZvLM4tIzcd54oGfhqAdMFwbLglR4D1OvO3me19EQVykQlP6WKqdCFnTbXjQuvsCw9cXWUyTi9TQI4nhxJhJzR_wMkfxjKeoaCWaGd3JGgInTISumYdWGHQeU4eW-5IYjc8daM1zYD83ddZQgzXdQpDg7WSwjLnOjP2YfT3ZgOR0wfQivj-AxSG3UL_rd7lwjItMWxWSp_rFNkWJPXOu5KdR_B1_FhotM-ybK_5D_JNIS3XscPfyK_CWGEPV9eb1RtkO8mc0M9a8_YDGvrd15FFHfkD90wN0-p03ESWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با docker کار می‌کنید، احتمالاً درگیر زدن پشت‌سرهمِ دستوراتی مثل
docker ps
و
docker logs --tail 50
هستید تا چندتا کانتینر رو همزمان مدیریت کنید. این کار هم خسته‌کننده‌ست و هم ترمینال رو به هم می‌ریزه.
ابزار
Lazydocker
دقیقاً برای حل همین مشکل ساخته شده؛ یه TUI برای داکر و داکر کامپوز که تمام کارها رو با شورت‌کات‌های کیبورد براتون انجام می‌ده.
-
بدون switch کردن:
همه چیز از مصرف منابع (RAMو CPU) تا لاگ کانتینرها به صورت زنده توی یه داشبورد یکپارچه نشون داده می‌شه.
-
سرعت بالا با کیبورد:
لاگ دیدن، ری‌استارت کردن یا پاک کردن کانتینرها فقط با زدن یک دکمه کیبورد انجام میشه (بدون نیاز به موس).
-
پشتیبانی کامل از Compose:
سرویس‌های داکر کامپوز رو هم به خوبی می‌شناسه و مدیریت می‌کنه.
-
بدون کانفیگ:
با زبان Go نوشته شده و فقط یه فایل اجرایی باینریه؛ نیازی به نصب سرور یا دیپندنسی اضافه نداره.
و خلاصه این ابزار سرعت کارتون رو چند برابر می‌کنه.
گیتهاب Lazydocker  + آموزش نصبش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4285" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید: https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4284" target="_blank">📅 13:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:  سلام متین خوبی داداش متین به خدا شوخی نمیکنم همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا من تو گوگل سرج…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4283" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4281">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OLuRflMvodU-UPOVHTiZXQC2NgmRRse529MPk9uFUk_cWyDJZaY91ebaKSs488SGSvQkNHj8Aip39JnkNptLMZXUFkCJQoGUIl5hH8sP1w_ZMPwqxdaWuhnbrp7Lj15uMme57BYwKiVUc4bVtQQ8V0W8LPuZ1_k4KfHHzwY4jufj8-q9o3sQKdTIwfO4pC_HoAJp5c_GV3a7VAU3id3DvJggXsCZqiGHfwUYgDE04IMWOnH8RxRuG3V8n-sV3XayoMjrnMc65COyIMbeUKBZyek_DT0MPER3mwnKTQ8ctjlWL7GtD5c5l5RcCJAuKM0ESr9gFB25YrdB7fG6jtUXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dr62kU6yAGtkuDt3mnPgyf-hXsxLAAzYjP7pPvMxAGFl_4-zB2VvRV7p0cKRR7Jaq30Xczghk3PPSxaKPlvQA-xH77PNfHT9WDdnqJusFgbCqnvHpffQXksdLxngnF7A87GXJi_mhwGoegfYKbXlc1NLK4GW0MKEJE3jGJ5VaXzq7lBAfPwNStlRK6wFWr9ZIo1dfXmRMdITjPT_y6Z4mSZdqHlRCVd8R-TSuXvX-cy_musV7IEPCde-S22SEqG2iXDwVEJGfu_UL4nTTnWxwvknfB676MrlMB-afjez0xwSSXjnWFQ8TPHaZx0tM0IKy6my8kmQTuRm8cZz6kDwyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:
سلام متین خوبی داداش
متین به خدا شوخی نمیکنم
همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا
من تو گوگل سرج کردم و هنوز هم شماره مجازی نخریده بودم
https://build.nvidia.com/settings/api-keys
ببین دقیقا ادرس هم برات گزاشتم
تو گوگل سرچ کردم Nvidia Get ApiKey
بعد سایت اومد بالا ازم ایمیل خواست
تازه atomicmail وارد کردم ایمیل گوگل هم ندادم
بعد که وارد کردم منو برد تو یک صفحه ای یک کپچا داشت تایید کردم و رمز عبور خواست اونم اوکی کردم
بعد گفت نام کاربری رو وارد کن اونم وارد کردم
منو مستقیم برد تو صفحه apikey ها و استفاده هم کردم
با تشکر از محمد عزیز. نمیدونم انویدیا وریفای رو برای ایمیل‌های شخصی برداشته یا اینکه کلا برداشته</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4281" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید:
https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4280" target="_blank">📅 11:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4279">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه پروژه‌ی خیلی عجیب روی گیت‌هاب (با اسم Pon) منتشر شده به تازگی که تونسته پایتون ۳.۱۴ رو مستقیما به کد ماشین کامپایل کنه و دیگه نیازی به Interpreter و مفسر نداره. این برای پرفورمنس پروژه‌های پایتونی می‌تونه یه انقلاب باشه
👍
https://github.com/can1357/pon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4279" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4278">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یکی از دوستان رو اون روز باهاش صحبت کردم، برای یادگیری فرانسوی داشت از Hermes استفاده میکرد در کنار منابع و ... دیگه‌اش. و به شدت راضی بود و می‌گفت حس میکنم بازدهیم چندین برابر شده
جالب بود برای خودم</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4278" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4277">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست. فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4277" target="_blank">📅 00:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4276">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست.
فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4276" target="_blank">📅 00:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4275">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=BKiGeUiIWlpq4i5UfE00JsR8ZSga9idY3Nh32RkIlMkV3bmIpXFdXR41Xuxr2-GLVHzhB9Qm11eKRpjS4o-2BqB43YEQX7xK6JsqNfRLayHiw5h01dCgeeoqzijei86JcdAQjZkGAlRlqjKezMfSGnzuVsKM-Ii4ePHRA-bczLgJznUmrHFj2QlMeYHcbWJpZDIgy-VR_M0-zDVoWp19XjZO7afvI7SsXxzRuOGW2akL3ZZLysDvQvLwLCjSAZ_7e1nHVQSJOHiihQF9y48iE1oKPbam5DSVtQSm0rn-oFkWfiAzYFoA5LrLrx6RB52evhnfIRdSTdOEbP1ORkuWM26SjDjySvIeA3ZRFBIEVfm43JYtikfxl2l8pvOC5F55eCEtwKhQPSHEcu4Ju9Uphne22UhZLATXy2ng80d-Em2PeVD5WFdv6MOAsAPA7odjdLJDaKWRfR4xFCGOjFYdZyMI2BAXmAvtI0Ketcpoo-dZclqw8lXq7nXIpa3T4K0X2RvV7LydBhm7PoQcIZ5nSN3h_ZUOb_UKLI7Wn_CSQJAQTKx50xjX_vA2kQDu6vNbU6MmKU3VelqSvEdwcnbeyww3_jeNFVgGanR1BgNJgfH-2LQ1K2R7uOhuRT-elW29Kewqr-93rUIda-VB9X_C3J_FbOmqSMK8klYKlJ_Vk5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=BKiGeUiIWlpq4i5UfE00JsR8ZSga9idY3Nh32RkIlMkV3bmIpXFdXR41Xuxr2-GLVHzhB9Qm11eKRpjS4o-2BqB43YEQX7xK6JsqNfRLayHiw5h01dCgeeoqzijei86JcdAQjZkGAlRlqjKezMfSGnzuVsKM-Ii4ePHRA-bczLgJznUmrHFj2QlMeYHcbWJpZDIgy-VR_M0-zDVoWp19XjZO7afvI7SsXxzRuOGW2akL3ZZLysDvQvLwLCjSAZ_7e1nHVQSJOHiihQF9y48iE1oKPbam5DSVtQSm0rn-oFkWfiAzYFoA5LrLrx6RB52evhnfIRdSTdOEbP1ORkuWM26SjDjySvIeA3ZRFBIEVfm43JYtikfxl2l8pvOC5F55eCEtwKhQPSHEcu4Ju9Uphne22UhZLATXy2ng80d-Em2PeVD5WFdv6MOAsAPA7odjdLJDaKWRfR4xFCGOjFYdZyMI2BAXmAvtI0Ketcpoo-dZclqw8lXq7nXIpa3T4K0X2RvV7LydBhm7PoQcIZ5nSN3h_ZUOb_UKLI7Wn_CSQJAQTKx50xjX_vA2kQDu6vNbU6MmKU3VelqSvEdwcnbeyww3_jeNFVgGanR1BgNJgfH-2LQ1K2R7uOhuRT-elW29Kewqr-93rUIda-VB9X_C3J_FbOmqSMK8klYKlJ_Vk5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش کامل Mahsang VPN | تنظیمات جدید CDN Fronting و اتصال پایدار
اگر می‌خواهید با روش جدید اتصال Mahsang آشنا شوید، این ویدیو را از دست ندهید.
✅
آموزش نصب و راه‌اندازی
✅
تنظیمات کامل CDN Fronting
✅
روش جدید اتصال
✅
بررسی تمام گزینه‌های مهم برنامه
✅
نکات افزایش پایداری اتصال و رفع مشکلات رایج
اگر قبلاً در اتصال یا تنظیمات Mahsang سؤال داشتید، احتمالاً پاسخ آن را در این آموزش پیدا خواهید کرد.
🎥
ویدیو را از کانال TakTarfand ببینید و اگر مفید بود، برای دوستانتان هم ارسال کنید.
لینک مشاهده ویدیو در یوتیوب :
https://youtu.be/35-GhIi-egg
@mobamoz_channel
⚡️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4275" target="_blank">📅 23:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4274" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4273">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">توی همین 5 دقیقه شد دو میلیون</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4273" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4272">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JT7oEz6V1ebPfNoeg-IpGOkr6cM9o9htPxxwanAjPwQODHoeJeFWSSAxGLOsQV2G-fwUfxCebl0NqoRjKBujRjOTpXkCl2ak8x-SUWDLrabeFYAzOTm42YucarovWm90umCPfIQeX8bCXpzhy6ZOQv6yXqMEUW3On78WSu4hLXbFbZE0r26-kN0ZwMpKwOLwoio6Wp0rD67_amxcUxdVvkfiiIbuR-22wEvJUp8cWXEMorQOJxpdK4Hl7bay2ytfyZMyQtejycD_WlfWz5hBvdbQJaOSnevdfRxW8Y3oiF0OGxS2kcwcqVlLHcama8VhGO6SPigE0nLU8rs6CcP7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4272" target="_blank">📅 19:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PCbUbO1MfzJbl-XIQSevtUd173MrBz3VlQl7MvA582w8670dhwdFqb2AbpjNZlN3tcJg1eZELC2oFftzwCc-SFeEnxmz6tEleEvNOL7w6v4vq0PV-rPBwynRmvljVR8tBCykA858uRopICGKwoR-AgTTQBn82mIYeEQmsAnRgZUfy48mUMfYoNt-ORTiL2rE_6dDwiUn18q2G70rLMtLPJXYOH_2E-neG4_YOrmKP-mXpCQ2kpEv--amIoqUOrLl6h5bwlebMOkcP6ge702mqdX33z1wj6nAcY6-Oy_cYrLAfXFbSSbJE5dEFqJtwXvlUGYkQqqKjG-Pq5RzMJPJLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین
درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4271" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4270">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jWU7v6eb6E4hjSnuAEjjs2czrzLmq_PVJ4vUVCpt6LTd54bMZrVF_B4Xr-pBQN4IZVzU78QT-M4_Fdt5XLu78WpvLnra9LrV_X0jsz7ImKxDPY2YwYsSk5jRR9fpTZKNFmEz5doISoMZuRfKPLHCWRzoxCj0xQZC6oKCQYEMC_39U_Q4-cadO4nx2S0AdocwZ4Yrf-B4uEYkS2xQtqjUiUYFLsPtVYMlI-H9_ciToUyEUIi2zIamUwD_I0KepxSAeUvU2N2CH9gJQncDKs38xlpBINZD5aa2dTYVmIsEWkeE9qFq47X6zuDwRcngBSm0ecSAMyijBO5iTSCtIvVfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4270" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4269">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/juetJc2GeVe5eDTlu0PIj9MrXJg99DQLVmHY8RmBUZOo50n1ZpFHO4W2kdSGxfEBoBQkLaJur3uOSlvccnHgmHq5h-pbJDTK4uCIGHHisknO8HsYVnyr-QBDXr8oDrEmOczWbbz_zHkH3p7yuGhyvl1n_-Lzwhsr1RQet1kWoT-yiMLkQbJAN81qRcJwVzLiUn-hln8oXTSHR_23mqq64YzzcMmX7YC3rWjP-50Rc7Wtrn1mY9CrokO6wNm91_67getnQaVgly-hXzbNmgrryETeh9VBmn8Z720yBgQuZ9akYeA-eEXXhQv2Zl4rAxV1Vfi0UipFj6hO9zghwSEqnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4269" target="_blank">📅 19:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4268">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GwpAkHsR5kxe-bekH7DMdwJhaxYRLFMPtbIJIaCBiII1KhhN6JPBMxinbwN62gSZHCbLOOUmuT2Mi0r_i1MwNqoV7m06EswTZupO6c_3JWINkqK0Ym0lDhsT4VuAhJvnu1UaFmBlljB6gxRKquqQsxogySxC5A50X2lRAq6M6-1WvpVupEZTNdboTES8qWFsrjfc1nMoEPDZZmeOjvyUzcLBtwRvRG6w29pCnL5zH-ZzsJDK_8o1nyUrIKgcA41mKF0jzrNTPLquB1OHuyNRllFudWFbVBdnvLnda4izxVJs9ZVWAxqoteX9OptcWhfN3xp4qMBDLktYS-Zl7skH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی احتمالا به Hermes اضافه بشه برای کارای روزمره
😁</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4268" target="_blank">📅 16:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4267">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4267" target="_blank">📅 07:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4266">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=Cc2tekn6NbIE6Eg_2BH4V3Nlh22vILQaeSh47DBeT38jaxSZKi-T-d5qxLprAjlm9y1klsB-NbIy_5lPgcuKpKif_bCXbgC4aORgQLzHG7Kzp9jjQdb0mbC6DJe844q0wEKCgtur68SlqVoDzk38sVHhconnQuT-tPvimoodjs1BFjIk0d2gqaDaO66fmcS_BmVAzmdHvZbNYsJva2Ih3lzLLZNmFN9X1xJhl_d4-59A--vIRpw1fraqxvVEqC1OlHpMmr5tNcCcEPAd3ARhWlwC9G1nW5Ky1vhiBSPo8s3NytM3gzWUNh4FutmuhN4gdI2QvGKp-lXHaM8_n8EA2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=Cc2tekn6NbIE6Eg_2BH4V3Nlh22vILQaeSh47DBeT38jaxSZKi-T-d5qxLprAjlm9y1klsB-NbIy_5lPgcuKpKif_bCXbgC4aORgQLzHG7Kzp9jjQdb0mbC6DJe844q0wEKCgtur68SlqVoDzk38sVHhconnQuT-tPvimoodjs1BFjIk0d2gqaDaO66fmcS_BmVAzmdHvZbNYsJva2Ih3lzLLZNmFN9X1xJhl_d4-59A--vIRpw1fraqxvVEqC1OlHpMmr5tNcCcEPAd3ARhWlwC9G1nW5Ky1vhiBSPo8s3NytM3gzWUNh4FutmuhN4gdI2QvGKp-lXHaM8_n8EA2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4266" target="_blank">📅 01:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4265">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رفقا
freemodel.dev
گویا api رایگان از claude opus و اینها میده، منتها به هیچ وجه سایت امنی به نظر نمیرسه. استفاده کنید اما نه برای پروژه‌های حساس و چیزی رو در اختیارش نذارید. روی هرمس شخصی و لوکالتون هم ترجیحا نزنید.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4265" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">متین واقعا باهوشه اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس. بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست. و همشو هم باید تا جلسه بعد تحویل…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4264" target="_blank">📅 00:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4263">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">متین واقعا باهوشه
اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس.
بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست.
و همشو هم باید تا جلسه بعد تحویل بدم</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4263" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">Matin SenPai
pinned «
خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4262" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4261">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4261" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RqTGp2o8KvatlWU7rM1hSWmLhd2T-Vh-7hkoF4wnT9xhz-wdHJ_gURmSCUxOG8mx7niu5Wra93-sJIdtDgw7EB5SpXkQPmbLiR_EB_QNDScDqevcA1Bvw2qmWUHiey6C6IJWLHqlTRSIq1mw3BZHLYuvYT6nyRKWubEBHTapJB3tIXoHij2KrRtD6VzJIrm861RV5nZbjFWA7-pVnXgEZX6HqwydI_qkpJI1JiLHrKb1TQU571lBokPBeCtN_aEE_9xF8Fnx8tL4BjTQhwhLWQCk0gKQAfU6IrQN23p2Rx2GiW3NoUB2mUy0hU5s1WScFPPE7Jj8Tg03GCZWwTaIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fZ4btPi9SPK_Dmgu9AjdzAsYjmnAaAYAJS_h2nlZA3AsEx2xsx3H1_GJGFDBJ1DLrkjM8RfRFWK3cTwd7gV9G3CcnadyzxuF9TYgaAbttw46sxhQTNrKa2yuyRZZ7ftG6I3C3a7bkWXIGyoht1wzAb3l91m4w2DYWIk0LC4pHkuBLxnEg9WhSUAAyalTmxY_jxUbCYcNMJun983FZqIutHh2BkTn53XZ7ClEWrk7hj78xEk9wGQxRA2yWm8Qd5kbQfrSU3O4w_vuT1KsLT-e-S9V9Xrdfik1I0VLmgfqofsrEaJ_0D4Ernv60GYvCdV13X8TJhaBRPsqMaN6xresBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4259" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4258">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4258" target="_blank">📅 22:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4257">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4257" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4256">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟
اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر شدن شرایطم، راجب خود برنامه‌نویسی هم ویدئو داریم) ولی در حدی نمی‌بینم خودمو که بخوام توصیه بکنم جدا؛ دوما در حال حاضر، فعلا خودمو نمی‌تونم هنوز متخصص هیچ حوزه‌ای بدونم. که اصلا بخوام راهنمایی‌ای بکنم توی هر حوزه‌ای. خیلی افراد بهتری از من هستن که بخواید سؤال کنید. اما یه سری نکات رو می‌تونم بهتون بگم که خودم با تجربه بهشون رسیدم و شاید مسیرتون رو کمی کوتاه‌تر کنه:
۱- دنبال پرسیدن مسیر از من و دیگری و این و اون نباشید. اگر توی این چرخه‌ی باطل بیفتید و هی دنبال ویدئوهای مصاحبه‌های آدمای معروف راجب زندگیشون برید مثلا زاکربرگ و بیل‌گیتس و... یا حتی پادکستایی مثل طبقه ۱۶ آقای علوی، هیچوقت نمی‌تونید اون چیزی که دنبالش هستید رو پیدا کنید.
صرفا برای اینکه گوش‌ـتون به یه سری اصطلاحات این حوزه عادت کنه این چنین پادکست‌ها و مصاحبه‌ها رو ببینید.
۲- شما الان AI رو دارید رفقا. می‌تونید به راحتی بپرسید، Roadmap درست کنید برای خودتون، شروع کنید به یادگیری، بعدش هم توی توییتر بیاید و وارد کامیونیتی برنامه‌نویسا/یا هر حوزه‌ای بشید، تایم‌لاینتون رو درست کنید و مشارکت کنید توی بحث‌ها، اشتباه کنید، یاد بگیرید، و...
۳- همیشه حواستون باشه که علاقه‌تون کجا ظاهریه و کجا واقعی. خیلیا هستن که دوست دارن «از اینترنت» یا «با کامپیوتر» یا «با گوشی» پول در بیارن، اما اکثر مردم وقتی واردش میشن تازه میفهمن نیم ساعت هم اعصابشون نمیکشه پشت لپ تاپ بشینن. عجولانه تصمیم نگیرید و راجب مسیری که می‌خواید برید، خوب تحقیق کنید
۴- توی یوتوب خیلیا آموزش‌های خوبی دادن؛ با ترکیبش با ai و مشورت باهاش و کاری که می‌خواید بکنید و هدفتون، می‌تونید به یه جمع‌بندی نهایی برسید و اون موقع هست که تازه می‌تونید نظر یه متخصص(مثلا بکند یا ai engineering یا حتی یوتوبر یا دیزاینر یا فرانت اند) رو بپرسید و اون هم برای صیقل دادن Roadmapـتون هست صرفا، نه اینکه بخواد صفر تا صد آموزشی رو بهتون بده. من هم خودم از خیلی از دوستان توییتر راجب بکند پرسیدم وقتی برنامه‌ام کامل شده بود، بعدش رفتم راه خودم رو ادامه دادم. وسط مسیر هم چند بار چرخید پلنم با پروژه‌های مختلف</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4256" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uV48Gn46Lo2O9WImJi-AGMpN4e-iXeXLm5idm-s_3g4AGx1cxwZ7GqCk6wiTgIN3TE_s9QdsLhFfs1dVqwJTUDIOW-2PhU1vc8gHXrGg-nqPl3TaT57IBucmeFvcALFfohCqNZBjQZSdRR4be5e7KJ1r8gWoLi4KycukBfhOtvcHKFt5DiAqHmAR249LtRGwMG5YlBl15u1SlgQ1TJXMbdT8nb2zd4ElbP4WWSUaj_3XszvfOXqTYGoZG2soBwAgY3lF9QJXAwAcoYT8XC_6v3_0gv3_aQwD-hC9Suk1zS_xfuHChvALJG9U1nN5ywvLdMel_xGb7Y5Ig6-uYeMXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tNl5yK0ybEJMEt2wQjT3H8dCcYS7_cohGwI_4jpgX4QS7cv73b0Y-WMUyQguL-X3mZvy4plk4TXWHGX-yZIW4s0-MVdc4omZCFnef4g6YScBdqPWH0y--jvx6i_0Ib5_ML2jYIKf_keviXtcShvxZuvgWHYBXGCUeXBjiUMqZvk9zTlerycttfC4fdMIPeX6UI5b_21iU6GHwkXUDdvpbZAbTPTvOsmdcBC9djaSjJsEp5QpcFhb3u8V23H_6Uu0pGeVWyojZ4awQcafWc_TsX_oGMbdWG3XbeF5qoWs84CLjKWaFJw_aQhEcMbbtQRnx0W0IIlJWnUS1liutUgCqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت
فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4254" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4250">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4250" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4250" target="_blank">📅 21:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4249">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بهم یاد داد از این وبسایت‌ها برای جزوه‌ها و تحقیقاتم درست کنم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4249" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rdj4GAmtaJyAJReCGg5mUHo9IiPPgrs8_5b5o-N4_b3UcEq0vpWPIoCL2EaRjcS7QLRQLpWk38BwVRLC9e7PQ2eR3WfVXGZn14tQkvUsWiu0veXUKDVknCsramjCI2kaFGfXgpG6kGDEi1bBLNmKkSxCLI7I5h6tKNPpSm2HvURlXStNVIS_06EiY2rKChuL3OruLII8zt6AGnhRrp_T3_nVYUW3epsTBiHLR_JejrYa_QYtgvJRS9K1R-2X_67dT9Vc724qwl5Pzze_A6x-1EnMfECOnkWRdKRhkCujd5ygohH-b1Juvat05jMG9dOs728klJR_suHDo0M2RDaoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iC4PvWDVhd9GC-cuZE4fA8Zp1seriS7N0KOsEYTcekbuGBTG1SFSX6PAIF-uwqN1V-ErF4otQ_heUAo6BySpI9qnWj4qNzcHdcvqlGgJ680S2BMrkB3NToN3kTloMAB2R1itgrC_NwkCXIwGpNGXI1ppuazSgMdT_AaariMrmdfsKOkLKtaRO9tGMZ5fMG6X3xHucSLoneuqIS-bH6zpo-L3FSkv0fCF6GgKaafa29_EH1JKiu4bPvwGNqYEJyBgtgVDKAMTj2g9jUlvCtuFlFab0cn2q0ncFlilkHF7TakAnVHrmVtuwge22yFpvA0pbea5RdR84Oud1_Wo_5Seug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jz0fbctzK3TGfE41QkS3oRU9CaYZoOJBtwqiU8ddb-XadhD6v7Au6d3ZaDGVOo4lkdHrFsB-fNMrB-A2gXfZjCH9dYRMg7I9ZFhcXDUkBMlCYop7GNRmfaF0Y82VDC6x8YgAB75wiUJ20BQ45qSqMV_Lna0chPhewA7jCAy7chNK1QLssFtrKjAHxDa4cCzpYL9S159xA9w0plCVnSjccAh5qIZrQtqihzPuF0juqHTcJMU6DTU-mQzyVs1Qh1MvWd5FPENIpmd3Yi0Wpb8K8ElldYdUoEUHgJUI0ISmlP3DCffYTX5q_2FsfsouZbmPrxxisJr6jkEWP1Y6WjXIjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z5LJ58psWtkZwky4BIIkHud0TR1iztTCD20Ck8NyMEjflEiD56XOZv4bHhAxC7hN_Fp7_MZDuKwLliF8fwqI50sfD3F9G1bEmB25zXS2b8etqMItX0GEwwzCxos4coqYYJhfTuATYKbWVf6uoT6mIWxscWph4p9tpLT_TotfQUEgnBqOIoGWW5HWJq_OG4zHzqYu5ieZlqPjx3e2AxI9il-XxSG4w2PZyR6NNvPhoxPaow4-6fOdPg47kxI6xuQCWwkUw0zItQ0UtOgJRhCFjjT-8hQpoADS7QtuJ_EbP_XSRq6edOAKSRZBaieDPQGZtKPLDJf-ko3-HaGUCbtcNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gRwkpfH_u0_Rgqcj7IgLwYccfTQhit1DgFlRA1QNi9kqpJk_07uRNGqhWizPj8hTF_ylN3iF8Svma6KBSUMyAiQhL5KGrV2XbdhZjAzkFy6OBf0QCh6fOd5J-_gx8U8L4LkaYwaR0QqrH5CnIRQna7oaqZz9ln8uKC3UzhNAO0E3Zc9jo1SyCYRO_oaGRFrB_9oaushXD0sbK4Ubr4q0SaSkBSm-6g8kQ21uJfOvEMCRwdj6gknOTqnvms1HislRCDKD0oALk-wtnJ2TNAo3nYjOgRF3LnNpn3xp0r1H0YBN2OtazFjWIXg-X9fTO18Wj4TBa9L0glovVZHAJPHkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ld7ijN6w6IrRu9Y7pJSehDnvHmX8eOCDJIRploRHx4uf6QSsixwH-eETD11v64v2XrL-eQuZwyZTpEsP1LJhUjh_jr6KYInz5Mr53m79Ro-zsHJWEpYxiUxx1QKgzUvkOrY2V9art85Rz0Jorjz8KBj-Q06b6Zg41uUiiAcAdQN6jmaVTAP06fvX2UmHF5kSBnU3hTOKEuR_d3FXDL3DhZPsJ-hXpHtkeuYCMcm10CgURm2JKcvB0rVz2xBVjNjhNggux-Yl3hW3KUFnFjALWRa-XtLTGvLzAoJFxamOUy53583QntweOZDz1ry3LmJKddprARAx41BZB2OCSFrmpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم مهسا توی آپدیت جدید، یه صفای حسابی به UI دادن
😁
اما UI کوچیکترین بخش اپ هست که عالی شده.
۱- هسته‌ی سایفون برای ایران بهینه شده و به راحتی تمام، وصل میشه(الان با همون پیام میدم)
۲- اسکنر قدرتمند اضافه شده برای اسکن آیپی cdn_fronting
۳- الان میتونید از سایفون+آیپی تمیزتون، کانفیگ بسازید. مثلا من اینو ساختم با لوکیشن آمریکا:
psiphon://?region=US&protocol=cdn_fronting&aggressive=ON&cdn_type=any&cdn_ips=
104.16.73.68
%2C104.18.180.6&cdn_sni=
pypi.org
&no_sni=false&skip_cert=true&proto_tls=true&proto_http=true&proto_quic=true&builtin=true#psiphon+2026-07-05+20%3A26%3A39
۴- یه منو کامل برای Chain کردن دوتا کانفیگ V2ray(مثلا یه کانفیگ آمریکا دارید که کار نمیکنه، یه کلودفلر دارید که کار میکنه. با کلودفلره وصل میشید به آمریکا و آمریکا VPN نهاییتون میشه)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4243" target="_blank">📅 20:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کتاب کامپایلرها و طراحی زبان - Introduction to Compilers and Language Design
اگر دوست دارید بدونید زیر پوست زبان‌های برنامه‌نویسی چی می‌گذره و کامپایلرها چطوری کار می‌کنن، این کتاب آنلاین یه منبع رایگان و عالی برای شروع طراحی زبان و درک کامپایلرهاست. خوندنش برای عمیق‌تر شدن تو مفاهیم پایه‌ای سیستم‌ها خیلی بهتون کمک می‌کنه:
https://dthain.github.io/books/compiler/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4242" target="_blank">📅 20:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تعداد پنل‌های وی پی ان بر پایه‌ی کلودفلر کم کم از تعداد کاربرا بیشتر میشه
همشونم شبیه هستن تقریبا. زیاد فرقی ندارن با همدیگه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4241" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHHMAQsv7ABU3943y2fMofzhznoEAGS7MlzQPVkDsK8gVipjRypp1GLSo7FWT4jCH6co9__3H0Jtlpy4ddWVlXWUsHtdywxCATlCyGLISjm6gxPcdlEro69-NJu2kFWmWzWrKPjcH63zGO30IcLi73jZmddsw3WgQD7dd6LzG0KeH_HWcv0aMzmg29ayMnhE3um22qoRa-tkOivN_7n_-Rw2Yq2Q_ky-lRn-M-y9QNdcCOgq9y7vQv1f0dXhjhGMTdAshadarCf5NJ3BreFcXfQ1n2i3pwAtWNd-OMGH5gVKj1WXOX2yULF5ISEtGm3RdLQpOgM9jawOuL54p9bpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OD5hDh-pBgEv8M3jH1ZIGaNVU7TNJVjPgZVlB4IzvXG-ToV1GGK182uMaBQAXG6wy_5heTVUXvKEXvZSxC9VjKQqrm_K46oDbDQ03rgzEvVDeuTEP6tUHESeO1uHJ5X6Jzeui-jqvcZ1ERZh-JmFp7uCkj0381wTH5vjjTAqlBn_p5Ctvkz5tTLFd3Hw-ybBW_Q5YoTaFhabHM6sMEm4awpb_BW3JQKw4qElcXJoxOVtkPcfh3rRsGr7HhHLFMS7k6U3mYX5L9pecX8gKTaS4Kywo0jaFgZSnY6dG2cOklRycctopeRBryfebghoRFCj2OO6XUuVG9ND5PRGW9lyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cmhol-agNv7IEOq6QCIRJQYenUjszg45g7wkgI6YPPH4ZvJArS0zQhww4NtiMBqIqWiLJngNxxL99pkA_a-Q3cFffGBZOQVU1hfWS-4tnJQDYSpU-xl86I-Puf8DTJdkhE-B-6Vm1OE2TjMG7dVjRUntfhLpuS9pwPxPhTH1LwXsL5TaguOxvSua8yPgrYLRIkislYDgZBUqBqJwwLdZppehAc0V3eafHzWqSFaRwij9CELGleIg9mizGF5PRffuy4-oHqP6v14OEYeD5rGifVactBlFnlbe93KBKg1kb9ip_yBecDEVTp5cVrCcunNTa5NxabyM_YiZ7vfkptse3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-Commands-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات استفاده شده توی ویدئو، با توضیحات کامل
سایت ConEmu برای ترمینال:
https://github.com/ConEmu/ConEmu
سایت Nara برای API رایگان:
https://router.bynara.id</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LSnD_A_re3nRNw4grLSNezJRw-htOW2w6rIeTp9COazJRZlJiItoDOfGWNNXGXMQfKDp7TVDab8M4p4qfani-pcPuDcyJugAdW6p3IU5iqmi0QKw9re7YwdXSKvJZUg6QTcz43pkKcpO53tnFMdmsOu6YXuRYr9a6crLoQ1OW98-owyrwsWBp6sgEDX-__vt1zT8hEtmOK_7L86IXKUC0AxXH1pAa0WCFBPChDjSbWdaSypCwA8bAKMud-BVIEnwqfWtii36g27a6kj6-iuSXZWT1ixeZ__uQJplxTh0ULMyybgj8VGOUxj-dA7AZUq8NEogw8cmDNAeZqMFpuUdKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
مثل یه حرفه‌ای از Hermes استفاده کن! 47 دستور مخفی هرمس که باید یاد بگیری
⚡️
فایل خلاصه‌ی دستورات:
https://t.me/MatinSenPaii/4236
⭐️
چندتا از چیزهای باحالی که تو این ویدئو می‌بینید:
دستور
/learn
: با این دستور به هرمس یه داکیومنت یا سایت رو میدی، می‌خوندش و کامل یادش می‌گیره! دفعه بعد که سوال بپرسی از همون دیتایی که یاد گرفته بهت جواب میده. همینطور ازش یه Skill شخصی هم می‌سازه!
دستور
/goal
: یه هدف بلندمدت براش تعریف می‌کنی و اون توی کل پروسه‌ی توسعه یادش می‌مونه که باید به اون هدف پایبند باشه.
دستور
/snapshot
و
/rollback
: دقیقاً مثل سیو/لود کردن تو بازی‌ها. یه جای کار رو سیو می‌کنی، اگه هوش مصنوعی گند زد، با یه دکمه برمی‌گردی به قبل!
دستور
/yolo
: خاموش کردن ترمزهای امنیتی هرمس!
دستور
/suggestions
: اگه گیر کردی و نمی‌دونی قدم بعدی برای پروژه‌ات(یا زندگیت
😂
) چیه، اینو می‌زنی و خودش کارهای هوشمندانه‌ای که میشه انجام داد رو بهت پیشنهاد می‌ده
دستور
/moa
: ترکیب قدرت چندتا هوش مصنوعی با هم (Mixture of Agents) برای حل باگ‌های غیرممکن. با چندتا مدل موازی و یه مدل تهاجمی
دستور
/browser
و
/bg
: دور زدن محدودیت سرچ تمامی مرورگرها برای ایجنت با CDP (Chrome DevTools Protocol). این یکی فوق‌العادست
دستور
/pet
: این رو دیگه باید خودتون ببینید...
😂
بتمن رو تبدیل به ترمینال پت می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=oC7EJD1qDOH59mjeTam1wAqeqTxPPfDivfZ7w3rRf85JwxoI1Pg8tw3afXOpvTg2c4xjBQ_Wqqoq9k15TZ9L4XMijdPvOskqomZMUerUWpqLr9R2bMW3gqL2OrldJxo5cq5j75ruv0FGoxA0pIOFe9NJSs6AGmG0hDy0_Ij4oJidaybA1GhXODc3Xtp2NJ-qJ8eLM0N2Ngq_TngFu5k1GzLX8rge1Cc5EMV1W6O-UxAJvlcanNKLcj5O83Nspoy51MwslOo8ONdyK3bPqNfyv_5BYgqsqPoLlgJN_kr0fnuRD_EFbkvt2jhiKSyDHmeVWioVyqUdqpGhlabA-owfWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=oC7EJD1qDOH59mjeTam1wAqeqTxPPfDivfZ7w3rRf85JwxoI1Pg8tw3afXOpvTg2c4xjBQ_Wqqoq9k15TZ9L4XMijdPvOskqomZMUerUWpqLr9R2bMW3gqL2OrldJxo5cq5j75ruv0FGoxA0pIOFe9NJSs6AGmG0hDy0_Ij4oJidaybA1GhXODc3Xtp2NJ-qJ8eLM0N2Ngq_TngFu5k1GzLX8rge1Cc5EMV1W6O-UxAJvlcanNKLcj5O83Nspoy51MwslOo8ONdyK3bPqNfyv_5BYgqsqPoLlgJN_kr0fnuRD_EFbkvt2jhiKSyDHmeVWioVyqUdqpGhlabA-owfWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ADuMHYsnGNrXgarhxnlPq4NAXISybgXnkyuEagzJyuTML-KF7z_BbMu20ZHe6Va5H2sHXRDFVSM7iHepz4coPCC84YiH_cTiRVRISh6TjmROHrcfuIpaLh_Q5eFfBRxl51YLeWyZpkty9EDfY7gjDYMSgXA7Mrggqog5E1C3rj-iUUW696u-IwtXTiql0PFESKxXCgHqOSeOppUoZB2oihpZgSj6XRCpFXqK_qGYVaX0Sd9JT82Zom9WCBFtI0YfrAe86Q9lxp7kFSqZPL_NdGa24ZvKETTDtiHLL5Ff3LaL7T_c4PljlWb0_HcLmDznnRu6E0J9zHPZJ0v3-ZWKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I_38omKV4TnVVX7w_tdHLT5W-vqBdIiant7EjRSKZonlwr2yco6RLVGhV__eCbatOAukACyw-vfTveJhmvfr8Lv-CpIwzNeCkorgeM7-K7KNMOdRZSm9mOJnCQTTrBEpYdfz1YCtFGnBsy6moFm37W8sPnd3pXtNhJPLrsd6m3sXnti-wWabv5orZ5GBBrkjAnxUsemownljDbWOAgwdi7SjW0QKpDt6mJKcg7OXNcxnN1AJhzfUsExnkL0-R6J3hxOld_QbBlVnjxmdRzuV7OvLsAzXbI7gthXitip2SyH0snXrsTo23XybIeqPXrZ058XdUWUEtUaG-WJqdF7SAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
