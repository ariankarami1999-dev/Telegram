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
<img src="https://cdn4.telesco.pe/file/uajieOeGUUNjUJaVJZb2sxNf628ksEd69WIa4YSpNsCcfs9b9TwFxkYZpQNJUIpS8eVmwJTOCQvDj-t4RkrIOGDnNkm6GMw23uK1TyxprNS6_4FOs52RiQTSGYqcosWqzCElTfufXnhdzJcteiDG08HdFMr78duF1kP0plU9-2TQIY5gndXe4uGfRCoGpxNk-XwIMJBG0CfgEZPq0fBG37qaMsntzGyesvdFBrmH3TEJjAiHE0E-MEjvBCpP5vHJUYhqet4DyEiYLLZPf2WeXhJj_Fy_CzJ8lhbFX2ylRan7tDujSpJBbcjOB6-isltdOpMzD1YC62kVg6wNXIZl1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 164K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 21:18:32</div>
<hr>

<div class="tg-post" id="msg-68477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">همونطور که پیش‌بینی می‌شد، دامنه حملات امشب گسترده تر از شب های دیگه شده و حتی حملات به یزد هم کشیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/news_hut/68477" target="_blank">📅 21:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=ag9GWAGUBSNtUqeBcV_lNZgyP65z8YobmjCBDJ-urjtWEPWwz1IGTvzfef-DhlW5VYvMZGBbp7k31xSHeBj8oFwNXfhmmF-ObQxUY9MlLb3KZsq5-X-tGYmFELlN9jX8oEFghh-y9qbAAJUvX7Gb5SOdHzvxCkGH1Z6M_ta8U5Hf1cPWXpuChENDp6lZDaB-tEBHDis_fWsp2Ypk2Rc3LqmAHfM9b-jYNO56ybn3lEgzkDcNURyO93D8D8yZ6BP9so6MSUDAob1vG9C_FVGrRBEEU1zfRpywGRANfNBqDFBbB4pnD1l0vbbEb1VllSWaYkkZKw9afpm-hbX5rTHYgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=ag9GWAGUBSNtUqeBcV_lNZgyP65z8YobmjCBDJ-urjtWEPWwz1IGTvzfef-DhlW5VYvMZGBbp7k31xSHeBj8oFwNXfhmmF-ObQxUY9MlLb3KZsq5-X-tGYmFELlN9jX8oEFghh-y9qbAAJUvX7Gb5SOdHzvxCkGH1Z6M_ta8U5Hf1cPWXpuChENDp6lZDaB-tEBHDis_fWsp2Ypk2Rc3LqmAHfM9b-jYNO56ybn3lEgzkDcNURyO93D8D8yZ6BP9so6MSUDAob1vG9C_FVGrRBEEU1zfRpywGRANfNBqDFBbB4pnD1l0vbbEb1VllSWaYkkZKw9afpm-hbX5rTHYgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
یادی کنیم از این سکانس که ترامپ چند وقت پیش در تروث‌سوشال پست کرده بود: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/news_hut/68476" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:  در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/news_hut/68475" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Csv6U6uOM6e_v6AHQs4BHv_LU_iHHpXZyhFNx8mmfjeyXMZInnO7LL3CnYIlWPWBMUdOOz-90uc8NXIobaI3Ib9VM2-mOmqs9TGy1vdLNYcPoo9IDzk9hacJDzEXB-77y2RIPxJlHEOYcxfk157aSVU67HtaL2RKZclhrOMtl7Jwuz1l4KLWyuB0aXTwxf4RD1dSa27oycg2BFyY-iSrF6Myg3bB78SamlJD9nID2yIx-w9VqrglInWqNFQQDbo9BH-Bxbi1PoallMhyqn1dqkh_VTUQb9rla6v2vfuZ-ts92-8Ac0772DS2aAK6VldIkt4z4KBqllWC4wPIIIaRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.
همچنین، یک نیروی نظامی دیگر در حال حاضر مفقود است.
چهار نیروی نظامی آمریکایی برای مداوا به بیمارستان‌های اردن منتقل شدند که همگی تاکنون مرخص شده‌اند.
سایر پرسنلی که به دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به محل خدمت خود بازگشته‌اند.
سنتکام به احترام خانواده‌ها، از انتشار اطلاعات تکمیلی — از جمله هویت نظامیان جان‌باخته — تا ۲۴ ساعت پس از اطلاع‌رسانی به بستگان درجه‌یک آن‌ها، خودداری خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/news_hut/68474" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=NSe1eJ5yZycOPEwgG42-yWUh-Jqehr2qosxyVU6GAcctt_KCatuLmvdcB-NxhQjEngJemI3VGwx7JWsFQLZ61vJEi8rUCsRy61Z9T6iPCqEYRLON4bmcDQkBdfIBQ2oLannrDiZR-EOyFlmEQsQy0PGzKHWM_pSveMYvW0fB1-Hf895MWya-vHi2xkQicWt9jF7Wx49bNtKINbpH6Ml3mwj1i5ZJtWK20Q2PuiROjX-zqNjAIYl-IGylDeQu3x0gaLj8PBFdto95wZCnwT0JBEbrpUuxNtfI5IrFGPmqrQTWflbxdh18FNX60G7j_f-l4nF7W0s8zEo28Yx9Imy9sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=NSe1eJ5yZycOPEwgG42-yWUh-Jqehr2qosxyVU6GAcctt_KCatuLmvdcB-NxhQjEngJemI3VGwx7JWsFQLZ61vJEi8rUCsRy61Z9T6iPCqEYRLON4bmcDQkBdfIBQ2oLannrDiZR-EOyFlmEQsQy0PGzKHWM_pSveMYvW0fB1-Hf895MWya-vHi2xkQicWt9jF7Wx49bNtKINbpH6Ml3mwj1i5ZJtWK20Q2PuiROjX-zqNjAIYl-IGylDeQu3x0gaLj8PBFdto95wZCnwT0JBEbrpUuxNtfI5IrFGPmqrQTWflbxdh18FNX60G7j_f-l4nF7W0s8zEo28Yx9Imy9sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
اگه حملات آمریکا تا چند روز دیگه ادامه پیدا کنه، وارد مرحله تهاجمی کامل میشیم
اون موقع دیگه فقط جواب حمله رو نمیدیم و حملاتمون گسترده‌تر میشه همه جارو میزنیم
آمریکاس که ریده به مفاد تفاهم‌ نامه و همرو یکی‌یکی زیر پا گذاشته و عملا از تفاهم نامه فقط اسمش باقی موند
آمریکا از جنوب لبنان عقب‌ نشینی نکرد، توی تنگه هرمز مسیر غیرقانونی ایجاد کرد، به حاکمیت ایران احترام نذاشت، به سواحل ایران حمله کرد و اموال ایران رو هم آزاد نکرد
دیگه نه روی کاغذ و نه توی عمل چیزی به اسم تفاهم‌نامه اسلام‌آباد وجود نداره
اگه دوباره مذاکره‌ای شروع بشه، از طرف آمریکاست و اونه که دنبال نوشتن یه تفاهم‌نامه جدید با تغییرات تازه‌ست
اجازه نمیدیم نیروهای دژمن از تنگه هرمز رد شن و وارد خلیج فارس بشن، چون امنیت کشورمون به خطر میوفته
🌅
قبول نداریم آمریکا توی تنگه هرمز، که گلوگاه انرژی جهانه، نقش یا حضور داشته باشه
آمریکایی‌ ها منتظر موج موشک‌ ها و پهپادهای ایران باشن چون ما جواب حرف‌ های ترامپ رو توی میدون میدیم
فعلا سیاست ایران اینه که هر حمله موشکی رو با همون شدت جواب بده
انتقام خون فرمانده شهید و شهدای جنگ رو میگیریم
آمریکا میخواد با محاصره دریایی، مقاومت ایران رو بشکنه
ممکنه دوباره به سایت‌های هسته‌ای حمله کنه یا بعد از اقدام نظامی، ایران رو به مذاکره با شرایط جدید مجبور کنه
@News_Hut</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/68473" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/news_hut/68472" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=o-Q7rdXRCIJZqzEMpX6hBuoUCufZjkrWl1EnChG4oixw_a4_CTydx26qDgl3tjO5SJb7QKJe4x9ZB_wbap55SX_wdaWOY90GeOi0wOFl4TVZanJyPi9CHeTqY3K5Z2cu-rWbcwg5fKfb_WUR44HOVb-FUvmqRKppkGMfroddLZRdewhrqsY2JU1Ou0bVZs8yotIs0PJ4lHz1bJ4IiinwMiDYBB9a6U1JaHG_c5KFhXanK5hJ9Z-Hzoixt2QJqvbaILk_SyJNTDh2VhH9xtHzgYvXxxyoZ9NKL5TdA8StOgN3uguUtFzaiJifG-zGiz92OkssAzX4rSLYw5yFw1YbpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=o-Q7rdXRCIJZqzEMpX6hBuoUCufZjkrWl1EnChG4oixw_a4_CTydx26qDgl3tjO5SJb7QKJe4x9ZB_wbap55SX_wdaWOY90GeOi0wOFl4TVZanJyPi9CHeTqY3K5Z2cu-rWbcwg5fKfb_WUR44HOVb-FUvmqRKppkGMfroddLZRdewhrqsY2JU1Ou0bVZs8yotIs0PJ4lHz1bJ4IiinwMiDYBB9a6U1JaHG_c5KFhXanK5hJ9Z-Hzoixt2QJqvbaILk_SyJNTDh2VhH9xtHzgYvXxxyoZ9NKL5TdA8StOgN3uguUtFzaiJifG-zGiz92OkssAzX4rSLYw5yFw1YbpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/news_hut/68471" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی مبنی بر وقوع حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی، در فاصله حدود ۱۰۰ مایل دریایی به شرق شهر الدقم در کشور عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/68470" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
تفاهم‌نامه بار دیگر ثابت کرد که امضای رئیس‌جمهور ایالات متحده هیچ ارزشی ندارد و هیچ اعتبار ندارد، و مردم ایران درس‌هایی فراموش‌نشدنی برای دشمن آمریکایی دارند.
امروز، "شیطان بزرگ" بار دیگر بدون هیچ پوششی، چهره واقعی خود را آشکار کرد. این تجربه تلخ از جنایات و نقض عهد، مدرکی جدید و قاطع بر دروغگویی، بی‌منطق بودن، عدم شایستگی اعتماد و فریبکاری ایالات متحده است.
اکنون که دشمن آمریکایی در تلاش است تا جنگ را شعله‌ور کند و هزینه‌های گزاف بیشتری را متحمل شود و اعتبار خود را بیشتر از دست بدهد، باید بداند که مردم عزیز ایران و جبهه مقاومت، درس‌هایی فراموش‌نشدنی برای او دارند. در این روزها، شجاعت رزمندگان اسلام و جوانان مناطق جنوبی، نمونه‌هایی از این درس‌ها را نشان داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68469" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای ساعت ۲۰ پیامی را منتشر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68468" target="_blank">📅 19:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
هم‌اکنون زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68466" target="_blank">📅 19:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68465">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNUiiFm4rC_wXgErGNvWYDGMQAcCgnTWoKN6NQnZDZM-yXe29_draQLBtxNrhzhigeQ3xjSJhs1ynABZSJH-gDZxVi54cCee3vN3bMs52LlDNnzAeqLkdvtRA-ILe458A5hBKEAReFEQfBIXjLGIo9feFr1LuTV7dG9k9XSgHOxh-acjWr02zOZb84Ay0rFrDreGSm-0aO1k6sweW1tZzwU7b2XqEC8uIsrVeQ2-WyMd4osrT7ATtC0jqNlMryTXcKqtw2zsC5Y7RsolzKiOLa0c-Di8UdudQKd2iDMv3pYFEiuKDDLdFakUqH2858sWcq92hSoBFcyArY79YWQy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/68465" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68464">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68464" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68463">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=nvUZWb8SioyLO_jV7-eCCbxZB45bcA9MeB63UTYkb2fjYILYG9YuGJehNM_icVizgSkFNvpHWrH4qdyjENaFR2x_AL2q-LnU-taB0TdoVy4nF-okU9ISi1oxVga4-6mEfHX6ClWwL9ZY3AUx75zpZrjfIHTLURv3320L4ydGoxME9Qdd5onyvW6E-vKCC_-d8BhApgW7u9fISnpfu2LdT6M0B6WVNpY8-eZHoFhDZGo766usl8lmfUoC7TqMCnceRdBuay25n10ZR6k0bOHsnxg9yKYGl3ZJg8x7pY42VpVe8NifUqfxU3wbgCV5qoBjj3HjGdTss6fe-wlIhtRz7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=nvUZWb8SioyLO_jV7-eCCbxZB45bcA9MeB63UTYkb2fjYILYG9YuGJehNM_icVizgSkFNvpHWrH4qdyjENaFR2x_AL2q-LnU-taB0TdoVy4nF-okU9ISi1oxVga4-6mEfHX6ClWwL9ZY3AUx75zpZrjfIHTLURv3320L4ydGoxME9Qdd5onyvW6E-vKCC_-d8BhApgW7u9fISnpfu2LdT6M0B6WVNpY8-eZHoFhDZGo766usl8lmfUoC7TqMCnceRdBuay25n10ZR6k0bOHsnxg9yKYGl3ZJg8x7pY42VpVe8NifUqfxU3wbgCV5qoBjj3HjGdTss6fe-wlIhtRz7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این ویدیو کامل نشون میده که تحرکات هواپیماها های ترابری امریکایی از سمت اروپا به خاورمیانه بشدت افزایش داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68463" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68462">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDV184eVIkPI6SNjnD2NFpflAbZyPfC7ALcq027gbTNocz6hf_CIE77haylsB7DSyAOZQ-33-TkyD1Utffg3yxQrj9tEmooadiVbEGUNiuvnzyLSa_WQbkC2KAWUDoZFvBjDx6Xk_KlbkYBmNsxtrDfPX2fqVobf6RFWBVi5Us8ffCPfGeo1MAHpgPgsIzeSNcGwpc0nPBF6g0VXIVsIgkoIG-Ud5ZcV3KBSRYSdhRg9MK47Zmn1Nq27yvnjyXwtpJxNZyW3QW3i1lsIITAztOr2SY43ESlUvOF-p70Shk5ZR4-D2N96vZWTmr_NG7X9odR_k67OlVup5x4CmHuZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/68462" target="_blank">📅 18:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68461">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdXZvt0YFoAcUTb6JfTryZTY7_iTx85LyqBTOqlb51jGRfuZ3QdPoj2p5UD_wMA3sHc3z6mPHlYUB8SlAgTtBU_3FGo0vI_MsZT9Ru7kCHc_ODVFI86mhmJYWqoh7zpUrE2CWHRXRWKCf_WRBmli4it-hTnnUL3NZlTiwQ_34g8fWVaaYOnXmbOuIXnw92NWY3a7LzkoaXFKjAq1GwIJEzefdY42A6izZP2q7cnWFcGnM2ptCBaZ2EmHSchLv2DTKbpZr2I0g9x-Vt4sStnFL4vN-mZvygRn44ZhUvY40EgBdyhHfrcSF4UT8loPDvEicWJCZbPI1q0eUy7KxAVEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نماینده مجلس:
بنزین گزان میشود؛لیتری 10 هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68461" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68460">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:  «اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68460" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68459">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:
«اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68459" target="_blank">📅 17:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=iBabVXsY9ruNnthGih5gXicyy1pGxg0oaoXAZIpij8_rNrQ3S2L9FsuTEtSwdtcUMeEwvjXdN4KoJ_XxZULDxS9RUaN9GtnYxtpweYJBPCRqAr2DHvnaO-58HJe9UdnH6Vuf-Yytg-BiOLilYLJl0o7W1Bhhy3vZAOFNt4HqF2K01nq4tORISQuJksbFHwzytGZ77JsbhGsSRf802VmP7fF0jsnAkgH-jsJpWmzh7FyIby6ae3SJpOyh6ZfORtKdwa7vaPy0qfqqh4lYsrperzsriLdp4PPtFi1kFBHTVI6xsYx6Vqr1dBBSp8l_GwK_l15V4tjqGvenBicMwUCD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=iBabVXsY9ruNnthGih5gXicyy1pGxg0oaoXAZIpij8_rNrQ3S2L9FsuTEtSwdtcUMeEwvjXdN4KoJ_XxZULDxS9RUaN9GtnYxtpweYJBPCRqAr2DHvnaO-58HJe9UdnH6Vuf-Yytg-BiOLilYLJl0o7W1Bhhy3vZAOFNt4HqF2K01nq4tORISQuJksbFHwzytGZ77JsbhGsSRf802VmP7fF0jsnAkgH-jsJpWmzh7FyIby6ae3SJpOyh6ZfORtKdwa7vaPy0qfqqh4lYsrperzsriLdp4PPtFi1kFBHTVI6xsYx6Vqr1dBBSp8l_GwK_l15V4tjqGvenBicMwUCD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی در کویت به دلیل حملات موشکی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68456" target="_blank">📅 17:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH_kZg4aJqLDV1ZOal--A7rXcC1vPUTM9T5VS8i5sR3db7ZkveBCfT1dSBJbMuXR_abNAQVqRWjJILGe-yCnSHTT0oQKgNzgmjEUqWMOYUoTsm2gZZq9Bb4RCrK15XBtWJZT8375SZJVgUFGjQOEcCPMvAuWwN79sKY2LtLI2cNhaHM4yD3T51OySH8yUpXD5sgWIcymlVp9GcuJTj21UDe5QnwNE6INNQVzZSB30Zn9AUzjaCA7RqCID0WBREVKbWqO4Je9UhD5MOJv4rXP4dyswpW7-nV66m2sE6G8-lKX4mFOX-jG2RZgBIpkAJ7y8gfqzeTb8U80pTH703w_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛معاون وزیر امور خارجه جمهوری اسلامی، کاظم غریب‌آبادی:
«از این لحظه به بعد، ایران اجرای تمامی تعهدات خود را بر اساس یادداشت تفاهم، به حالت تعلیق در می‌آورد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68455" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68452">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00f574479.mp4?token=eA-Rs6hnDLYnfdfMa9ZjuiU01bo_41aFl6iwHc2lSgGnDuV1hVMj6ZjnwswNsUYz-Gc93-Ajmjdur2PJh8AdbFcCy07cQAmRU-dPZTE7oVf8ySHOle2i_W8n-CELaDGJUrYj2DKYyH_ym_uElxqLzDYagKhxsPIsvHqBLSfCBaBjNhRRpUIMHDjC8LhdNZCvjxom3-WhF1ZA2564wBygnv-dKrVM8XKauPcPcIcrEM-yNsimvNSVyr9nIclkXe5Yx-TZMKynPwb3BqEI1yw8Rcn0WS3gmNUSs8y39AGe6JY0sTo6cQ9KOLrTh856FYyYTI3d6134TjMnwRzG5qas4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00f574479.mp4?token=eA-Rs6hnDLYnfdfMa9ZjuiU01bo_41aFl6iwHc2lSgGnDuV1hVMj6ZjnwswNsUYz-Gc93-Ajmjdur2PJh8AdbFcCy07cQAmRU-dPZTE7oVf8ySHOle2i_W8n-CELaDGJUrYj2DKYyH_ym_uElxqLzDYagKhxsPIsvHqBLSfCBaBjNhRRpUIMHDjC8LhdNZCvjxom3-WhF1ZA2564wBygnv-dKrVM8XKauPcPcIcrEM-yNsimvNSVyr9nIclkXe5Yx-TZMKynPwb3BqEI1yw8Rcn0WS3gmNUSs8y39AGe6JY0sTo6cQ9KOLrTh856FYyYTI3d6134TjMnwRzG5qas4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
چند روز پیش یه ویدئو از یه پسر نوجوون وایرال شد که از سرکار اومده بود و داشت موتورهای یه نمایشگاه رو با بغض نگاه میکرد و حسرت می‌خورد؛
⏺
این ویدیو خیلی دست به دست شد و نهایتا مردمِ نازنین ایران، تو کمتر از یک هفته پول جمع کردن و واسه آقا یاسین موتور خریدن و اینجوری سورپرایزش کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68452" target="_blank">📅 16:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68451">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون جنوبی:
همه دارن از جنوب صحبت میکنن که دمشون گرم ولی منی که خودم جنوبم نمیدونم چی بگم.
درمورد پمپ بنزینی که یکساعته داخلشم صحبت کنیم یا مثلا درمورد برقی که الان رفته و نمیتونم برم خونه صحبت کنم
درمورد ماشینی که نمیتونم خرجش کنم صحبت کنم؟
درمورد وسیله ای که میخواستم بخرم و امروز صاحابش 40 میلیون گذاشت روش صحبت کنم؟
یعنی حتی نمیدونم از کجا شروع کنم
ببین قبلا به موجودی کار نگاه میکنم میگم خب بعدا این چنین میشه اما الان تخمم نیست
الان میگم بتخمم ک میزنن نهایتش اینه منو میزنه و میمیرم
چرا برق بقیه شهر های دنیا نمیره برق ما میره ؟ ما اضافه ایم ؟
بدترین اب و هوا و اکوسیستم و بی برقی و جنگ مال ماست نمیدونم از چی باید بگم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68451" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68450">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5fxder5xo3R_LS5qV2gv2j9VoaXnmogtYgBOmgNpgl8lvcbzbvyw_4-wk0xuDsC_Pa8_SlAnKYjcLhycrO22nG2lKla2uOALLs3tz1ZP6LeUBrZdqWp2K1ws9AY5auIqGwdScr7ia-sNDfhpeLLqbd662reDgBZ5FDB-X9v-NeRS0OZmTQkf6Rn8MeYP3yVswsDfCyURhCdau1vBL_AMBZvW5VqMo_PLcCo56w147SimLVR6VCPZlNx29_NBV-1sgDih9-y382fJ_6eyByXSIYHlgQADVGJiIxqzF1Hfp0QVKlgZ79D8vlh2hxfLZr2OoDiu2qfT0KFgHdVJqRmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حکومت داره به جانفداها زنگ میزنه که بیان آموزش با اسلحه ببینن و برای جنگ آماده بشن
😂
😂
اگه کسیم بهونه بیاره که مثلاً مشکل دارم و نمیتونم بیام، میگن اشکال نداره، بیا آشپزی کن یا کارای دیگه انجام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68450" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68449">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=qR2AdzxB4UHHW_DJKgXAONvVMG_sJvsgLLa83aRa_khSSg4ltbJmqXDgNS9lJATVvjJKN6rcwKQ4mFkOnLwEW58-C9pXs814aKUtM-CdLCwJoJrhDsXiG-ssnM3BTxs34tGaf6joSU3ng1xvWr3gRcHIMN93qy7nkDQQShpUI0iqZQOBgR_WUGTs_--pkx9MY8xcm5kjyVMCGndm3gTh-Zarq9NVxH5aZbfNukdIC35ETCQeLmC-h4akF2cuBEyvNn_mCjxb3870IWxcdn7iKvOwTyRvvEFZSHPUgEHoiUc6dCHRbpFUMzCdxVxdcB3VuxNIFuryxX3hRKR7UyPEPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=qR2AdzxB4UHHW_DJKgXAONvVMG_sJvsgLLa83aRa_khSSg4ltbJmqXDgNS9lJATVvjJKN6rcwKQ4mFkOnLwEW58-C9pXs814aKUtM-CdLCwJoJrhDsXiG-ssnM3BTxs34tGaf6joSU3ng1xvWr3gRcHIMN93qy7nkDQQShpUI0iqZQOBgR_WUGTs_--pkx9MY8xcm5kjyVMCGndm3gTh-Zarq9NVxH5aZbfNukdIC35ETCQeLmC-h4akF2cuBEyvNn_mCjxb3870IWxcdn7iKvOwTyRvvEFZSHPUgEHoiUc6dCHRbpFUMzCdxVxdcB3VuxNIFuryxX3hRKR7UyPEPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واسه دومین بار طی دو روز گذشته، جمهوری اسلامی به نیروگاه برق و تأسیسات آب‌شیرین‌کن تو کویت حمله کرد و باعث آتش‌سوزی شد.
کویت حدود 90 درصد آب آشامیدنیش رو از طریق آب‌شیرین‌کن‌ها تأمین میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68449" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68448">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtavAkhN2b_CCSb3_DPpvyzdbOXvGSNZR3wuE3c9C5x7snQs0iBRNqp5-pKxdCD8d4Bn0NCLfD1O88U3LCjDPYEqzMamL-eG7YmmuoY0HgITsbxjaM1KGBV1BkGUpWCOqFHdbpsvGwmT0FIexJp1iNK2F8mWeoDc-xlk2F5AMBQR6VjaQu8w3pRb3SfewBXxQjfdSIq4jPZBxsV2McJCFE7cIx2pyMjLyOaXCrcOoJTiX2YMyR3TU2FQjMOsrk6HEyoDL9px9LmXVrgxdFDYJ4TjYj6OlJlywIEp8CWmUuR1tPS7usOjJ-CXw65Qb9PoKrf8ILgSLuoTakPbT67jqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68448" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68447">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68447" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68446">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=MODN-zNr1_v5OkM0Q_HAFdt8kQCK3a2DHitIyHfOlgIkIb3Hbo2oSzo4euNJx3rr9YG_0G6mmsNAI7RpDNsfx03XfFgnYE115pIe5LM2kns35OK-cg4Dh--WzEzQJ7K9xQ7O91CM-bv84VwtE6IeiFO6-pvwL1blffhIGuygKwS2xJH_Tuffzl_MCKExTpQEU60o9L8T540fvGBMuFnioVeHFL-5Mq8ATzshFkU2uOTCBD5jC0dUBpy6Mq9TMITKchnnG2zCgYHYD7SekClMHDY_M2vsQ4mOSsSCMy9YlaoxybUjL06r0FmRzHxef93OKdF5uOA6OxGELI2-jFXIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=MODN-zNr1_v5OkM0Q_HAFdt8kQCK3a2DHitIyHfOlgIkIb3Hbo2oSzo4euNJx3rr9YG_0G6mmsNAI7RpDNsfx03XfFgnYE115pIe5LM2kns35OK-cg4Dh--WzEzQJ7K9xQ7O91CM-bv84VwtE6IeiFO6-pvwL1blffhIGuygKwS2xJH_Tuffzl_MCKExTpQEU60o9L8T540fvGBMuFnioVeHFL-5Mq8ATzshFkU2uOTCBD5jC0dUBpy6Mq9TMITKchnnG2zCgYHYD7SekClMHDY_M2vsQ4mOSsSCMy9YlaoxybUjL06r0FmRzHxef93OKdF5uOA6OxGELI2-jFXIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68446" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68445">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⏺
وزارت نفت کویت:
خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68445" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=cvekvGmDT8lWFOC2mEvOate1vDAcAmd0NGUw1dHgizMSL7HzitlNixfybgm5ze__-IpPChAgm5ZmcFiB5PgdeZbXGTZ6mCOq7WQz4zS-wBtdjoYXW7LaRCFhTTbMf-3oDzK7iwaHqQ9dFBKnhK2DQpSV7vhcKddxEmX-_hfYLUdqBm_b-nQbA7FrgnMCTpV5oLMU5_ffSqmPExVVHwHzD-GJ50vwHOsyVzDu0TVtFeYI4PocaobpSMLxTkMX353KjtsiUPJUNzzARYxLtxQ0dGdXHMcj3UflGnDG5U3q2xNU2H0QF1ym9MOM7_XVXsYb7xvbchdPnqt0UTvFYMoOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=cvekvGmDT8lWFOC2mEvOate1vDAcAmd0NGUw1dHgizMSL7HzitlNixfybgm5ze__-IpPChAgm5ZmcFiB5PgdeZbXGTZ6mCOq7WQz4zS-wBtdjoYXW7LaRCFhTTbMf-3oDzK7iwaHqQ9dFBKnhK2DQpSV7vhcKddxEmX-_hfYLUdqBm_b-nQbA7FrgnMCTpV5oLMU5_ffSqmPExVVHwHzD-GJ50vwHOsyVzDu0TVtFeYI4PocaobpSMLxTkMX353KjtsiUPJUNzzARYxLtxQ0dGdXHMcj3UflGnDG5U3q2xNU2H0QF1ym9MOM7_XVXsYb7xvbchdPnqt0UTvFYMoOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موج جدید حملات موشکی و پهبادی سپاه پاسداران به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68443" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=R89GC-7XD5J8M5eFeaHee2W0hv9G6wtHP9QDxeRQhyc82eTNYsqwfURB-fFhdi2sj3ZicgcqLfBY-gDmAG2c1niPbe6q6Btf2mgWxCargVosh8Z9U_7_MgfgcnG9dxwVvmWJdlukpqJZZ2qrzOY6PmK8GWCwOxmXtEYEdO3YcBphuyRoAXuw48CV04cNpuf2aMIoH86-kbYtURl6LhYkGd-jduTQYu8rGiNbs6ATy5KRpYeIWbsIGQB6fWcyFICMKHBF42k2ZOwrj789AQpWkrW7LGTmvPMLVZz8buO9v9-ugRFKYCsbgVeNPQ2tj_q74axlYTV5Vkd1vrs_05tfyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=R89GC-7XD5J8M5eFeaHee2W0hv9G6wtHP9QDxeRQhyc82eTNYsqwfURB-fFhdi2sj3ZicgcqLfBY-gDmAG2c1niPbe6q6Btf2mgWxCargVosh8Z9U_7_MgfgcnG9dxwVvmWJdlukpqJZZ2qrzOY6PmK8GWCwOxmXtEYEdO3YcBphuyRoAXuw48CV04cNpuf2aMIoH86-kbYtURl6LhYkGd-jduTQYu8rGiNbs6ATy5KRpYeIWbsIGQB6fWcyFICMKHBF42k2ZOwrj789AQpWkrW7LGTmvPMLVZz8buO9v9-ugRFKYCsbgVeNPQ2tj_q74axlYTV5Vkd1vrs_05tfyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپهبد خلبان نادر جهانبانی؛ میخواهم شاهد پرواز گلوله ها باشم
🫡
نادر جهانبانی (۲۷ فروردین ۱۳۰۷ – ۲۲ اسفند ۱۳۵۷) سپهبد خلبان نیروی هوایی شاهنشاهی ایران و معاون فرماندهی معروف به ژنرال چشم‌آبی بود.
وی بنیان‌گذار و سرپرست تیم آکروجت تاج طلایی است. از او به عنوان یکی از بهترین و برجسته‌ترین خلبانان عصر خود نام می‌برند.
نادر جهانبانی دانش‌آموختهٔ دانشگاه خلبانی نیروی هوایی روسیه و آموزش‌دیدهٔ دوره‌های خلبانی جنگنده‌های جت از آلمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68442" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68438">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=NYDR5zuOTD1j9ovORlJbryCDYkqBSsQGE8YVI5qKKR4ecENzFBVG-0VD5Ow-4ysuzd_De05Udmw3GXhOtYtkN20ytPtWgk0N8BwpFuVdjiRL9AkUdodaJGw1abiwqVLcN9otZ9Gps1t5cPbQy7aGiPxNDksakK_leE3j1UNQDETOxov_Rw1WQ7E1gKTNJtyqqYjjEkb1aj1q7EgPr5zqjpH35n_vjhwzuvft6F-KZnm8y6lwizJD71cIOOlM2GWxhz3WNrgrwDWXfbt26GvBJeC0w-_CxsTtPREnFYCTXGkV5eTAJg68gcCEwrGXWdWu-j2P3yrzNey3WzjvFXrMcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=NYDR5zuOTD1j9ovORlJbryCDYkqBSsQGE8YVI5qKKR4ecENzFBVG-0VD5Ow-4ysuzd_De05Udmw3GXhOtYtkN20ytPtWgk0N8BwpFuVdjiRL9AkUdodaJGw1abiwqVLcN9otZ9Gps1t5cPbQy7aGiPxNDksakK_leE3j1UNQDETOxov_Rw1WQ7E1gKTNJtyqqYjjEkb1aj1q7EgPr5zqjpH35n_vjhwzuvft6F-KZnm8y6lwizJD71cIOOlM2GWxhz3WNrgrwDWXfbt26GvBJeC0w-_CxsTtPREnFYCTXGkV5eTAJg68gcCEwrGXWdWu-j2P3yrzNey3WzjvFXrMcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
🇷🇺
حجم آتش‌سوزی در مسکو پایتخت روسیه بعد از حملات پهبادی اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68438" target="_blank">📅 13:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68437">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=B9YNq7SYqG7HnW1UaZY73mLaG1oweqpTWCCeNdasrTE0EPnez4KGICwcB5m1ya0wBE1TpFUjD9w2vHctuDVMcdJu4DnBN_cxgbRpy1nHmKHbZdDaZ1T_Ql1a8j8RL1catVne-XTs6UGcxdb4WYys2Q5u81tXUX80nXw3dXPmmmbSLTApEpYc8eNoUKvOSEbHMH4jwDuh1IoUNTzUcZJoXLXz4j_gKt7JeWr7urOsuvdYjMLL7fpcxhqrFc7rvL3gdmLYKfSrA15zzN9yp8kvcc-z41pEBq64xer2qWsgsHtZqmfWAM1ycGUQ-L2LDoMphpfaUocxFYOBQbBvd2Yjchk1ELnAROJ4_U5Z9UT2KUadBIB1CNkH9FYgWEGuEPT8kpL5-xuCPSEYyeWt6Q9HbodapVTFTILm8e-hpe5aXJa_UznV3o8f2Hozh8QQ_xfFc_uqGD6VoT_Jy56t0ad07fyE-DhpearmL8EjutD0wDYblFKDozMGbSFa02EUQPcx-8ch2sO_wPELSVbAnK24jD91X3qPmrsSNBirERkG1YHRHqzBsUha79B7YPoVdTdzZU29c2pZebBdYdQMxsVaNMw_RssG4ySAZ6DrhHltrLWGhKZMKJa3AnOn8c2z73SzpA12-QPuUokCEGufcGTKl9xMu4OA18VGZDD_e5lmtg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=B9YNq7SYqG7HnW1UaZY73mLaG1oweqpTWCCeNdasrTE0EPnez4KGICwcB5m1ya0wBE1TpFUjD9w2vHctuDVMcdJu4DnBN_cxgbRpy1nHmKHbZdDaZ1T_Ql1a8j8RL1catVne-XTs6UGcxdb4WYys2Q5u81tXUX80nXw3dXPmmmbSLTApEpYc8eNoUKvOSEbHMH4jwDuh1IoUNTzUcZJoXLXz4j_gKt7JeWr7urOsuvdYjMLL7fpcxhqrFc7rvL3gdmLYKfSrA15zzN9yp8kvcc-z41pEBq64xer2qWsgsHtZqmfWAM1ycGUQ-L2LDoMphpfaUocxFYOBQbBvd2Yjchk1ELnAROJ4_U5Z9UT2KUadBIB1CNkH9FYgWEGuEPT8kpL5-xuCPSEYyeWt6Q9HbodapVTFTILm8e-hpe5aXJa_UznV3o8f2Hozh8QQ_xfFc_uqGD6VoT_Jy56t0ad07fyE-DhpearmL8EjutD0wDYblFKDozMGbSFa02EUQPcx-8ch2sO_wPELSVbAnK24jD91X3qPmrsSNBirERkG1YHRHqzBsUha79B7YPoVdTdzZU29c2pZebBdYdQMxsVaNMw_RssG4ySAZ6DrhHltrLWGhKZMKJa3AnOn8c2z73SzpA12-QPuUokCEGufcGTKl9xMu4OA18VGZDD_e5lmtg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حاضری به عنوان یه جان‌فدا، بخاطر مملکتت، بخاطرآب و خاکت بری بجنگی و از مملکتت دفاع کنی؟
🇮🇷
جان‌فدا : آره، من بخاطر مملکتم جان میدم.
🎙
خب الان بیاین امضا و اثر انگشت بزنیم که بریم خط مقدم جنگ.
🇮🇷
جان‌فدا : من بخاطر مملکتم جان میدم، ولی الان کار دارم، شما برید من بعداً میام.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68437" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68427">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7BVlUA8Eam1yHTSz_ICmqDPmEgeNDAuVTbcqU3xLvmMo-rAMwg15KwNGxj0j9zVAkn-D6vh5NRH0Lu84vf7pDNsQwiwcY52lTuihzV5rOfM9Izol8L1rGOSsbmQqtpuH-q9X5eo2Kim62cwNFW08Yf1-tFKSPTKEtwdCvrLB1-CoQXvx4ZEVuSZUDql7WdXiNoHTfoZLxBAXXpuNdYQPHV2ASdP7eBuRsvJLLEAzdlIZILw6BKsq-UalyEoqXd52jTFCcQHrN8QoOsaKvgNhoOgb5FuMTjHrjBZXaOcRttLUy4eAKvcbuu7RCbeW8g8CFHp2xjMm4sfpCx7tl4gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMeNRZMKmdsZb_ExCKl6Z2pgucjKdIrzC23aVd7Lg16ipJiIaZaxsHWfJpHoMiI5r1HTj71c4fddEKV46XKX4_5G8TGRHw0MKS1rbp-B9SmSyk2kvcilc8pZLJMAILJNFmfLC7Dg-p02ZWev8YZtvghFI9YTE2KE0o23DxQ-CiclCaHWpYuGyUvi3ZTMQYtMPM3lSBBkTPTGZgKm2olFKYxy22ZDjVbw0FxDkG8kZu0CNvZBPUQnQXZYVhPp-cEMsrwaDKm4qdl5PWpNX5_nViHd9PO2wDcOFEXH9cPqwNaPNiNnX-W7xEPJIpPcVRBSgsLXQD6Xb5jraEcBDr0mEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXlHzIOtycVEuzMaSyfjhTQ_k0vkOM397zePhw6u_lbEw6m_jlTRAiLMkW-D9VTW5GEG1xUnCnowrGUGD2tMzz9STfNzbX42lNPsmMi68hMJKTVIbk6NhNETndSaLzKQXjhbjf6z7ifIIoK__uSrTELnJWfK0ljB9qoIOLGfgDxIWKJcym1Zk8nSpEFTlR43HVfa2EIfmt9zYbo45PCVlqMoTit3RcaJvsG0fLU4e90Sb_vs_005FEDk9SHz9fEh6cYO-LowPT6dJQmSH3nWVmlF8bxRjbJAldcRtheadU8V56BLy0L7tKgOpSO5C5l-f0hGK_0DCIVQTGi--i5SVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAHwWZcGQk9bTEPIAfKPO3pOndfQQwHEouwbOs6WPYwahNTkINmELN1cbqQaE7BT8UbCMaAS3wMzWBhNo8rZQjVR3BVuzRNCPNKEuRb7hB0OHc4-lI5_g3NSpLcHRjQqhXnjIuyQpRGwzpQK4z7RTeoOYr0hM91kIHzhLrVH6ugo05QGxZ2mjgDH5Ahw4D1NAPiJS_mOnvHIiNFoliLQmPRBCdX5NIYG50M7LHzlFRGJSdrbV23MK27soloafsPzsgtaPQcL9NMl3nSMC7Gs6lwAova0R-1gvYuxAqyiz0Axqj2GQyWgkp8KTZgxTzO_NaiHZ2ALJCDIRZMp38aBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/el8YWblstOLTJChyvfOcg93SjeaCVsL_hZRF93qlInHSjDF0fptgLupC8aPPGy--pvq4yMMNt3TVLZajI_6yt_-wk-NSATPV6TWcYhXswi46Nme-BZADsVxVaJ5XdJmABjXGfI50wRV9gKeYt7j-u2Jb_4utMKk83udfpY1dQdtGJtlvwHNqnPSA2gWHSnWKtjErk3QV5W8ZMiINvrZOj5rv_6AUE6t-7frPqi4hNne08EXa3qIqSu9klgShUCuTGPWNpvurBVXik2LBuRJ3xzUXjbGOOyEmGh2LFyOeILZNsUw640yF2G5gX2vyEz5cXqKxTru8ZTpFDCLKl6zcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4uTcxfBc32O5E4ovfMEV48s-U0QFHiUX6aMXqb2qzTZa_mEeOhYCz_5_XIybc8hwMwHTjH2-1H0ajk6tOXt3Tec2iNxxKxpehJy5L_CZWRNNSHohzfLp8UEVFk3CdZZOOiQ9gOCfoNtRvwbuMant9GigFICOf31d73Y0dAM2yNv6-Ws2VGa5lZGhaCzNXFxXapAAHoAPuc9fQyMi6xZYGEL3IITyyZONuxrV793sFNzD0i9VKDHU8skrau22kuYM8QGFcwiMsyKauyEtiaL1Rk5fd86mekrjAu5TVQH4U_CZYUgCQIiyyTM5D4TCut0Jm-yHgGMZNEPgvUdMUEVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmkC-gVka-xUR6x6Wgw6kXoe7oncRcc8cBvQf9HkpjdhPnupuKPlZaCdblo-qMk2i_eVqeHbVNhp4cK6MXdiKZ5LGxComOQn6cGeIB5OVJR2oKWK3yqISDaupymYZTLODtjxGqqu6b0yEq7oymic5CeQmphTRiD4Ud9479AZfTWjzRPTzv5LlHCRRDcNDsVx6bwIgsYi3ymzefy1g-oQlyS2ADfEdyRl4HC21xz96ENbGHW1LrPq_BNbAN16srMFbq0UlllDxfqhJpkVzIO5_wwac2Cbqks6sTiZVkf14pY0PYTPdhOQtPAOnRg47YS0nlNJTZ9OMib_OQFwSy19QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHfd_Q6YNJP1grjpJv5GKYLKv2JcpWdEfV1g-3V7WNoatHRXzM8PF6IsVM3OYuTbgzNHVbD-eKE3FcTDZCAN-DLM1_bN0g7HCeLPraSarEtyRdiVLlCVptpqAtzV4dBamRp9T4LG2XmS7bJN6erHaxbWt2EeoZcczktfqUrqibUGoJysfYqS6tB299qXg8UpcOL53MOf71XeH_E1Qy1IZNZOrSlnJN_CW65AMCqxvq2MeBeKpWPm46CuBzSdj-uXYOCVbjs9z997NmcmPoCD1KUDhw-7rEAoiPU1ky35lCxnN_24AMn6nHj8SySwgnHeDQ8DZEkKPKgn48-dUPWewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ld_XHD-1Tx6e-hHC2j1Wn4orUZ2s2nX3uzqOkzLTu7gac-AZC1wbuhCbpMiNYgeWG2f_gKP5v9bqsx_iHg9Vb6i16L9iNEjQnr68-lAB6IlxbaNekjNdD7Zwe_kchic7zdUqKHf5k-p-JS5EBI0O25MVD9jTQneQQcEz31gZ2i8Rtm9DvKeaJsJaMe5iwWzF0_xaoN-wAD-lCMmlQ0_7O0cQ6LiTf8kUcjCsV86qZodepeXLLHy6HMJV_JPmxQ1qEmTpdWpLNBXstkto7Puyo9GbwlQsPHsLKfkF44e6vhgqugjyTdyNZaDsbsOKhqhXCeHAHr4slDXtH2YJhXeVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tM-LWNTjnmcyuKiYgL5dsoS4G-ezxUb2ZLdLJk-UR5GEP2PWjbVRMnEKk5zuvCfulzlh-3xWBhi6eRS495rLoJEUUQb8kHDOEG9fXF4l59RkpNvvI8q95Ya-tmpo8ZU2wR8RvAztmFYmglnTDZpgrpg4uy0wRI4eDSsPL1rx6w5Lw3s6wFidrT5I3iUOM0Hjmaf3X3iqI9A-tXbegRRpF5KCoASuwgZqOr4BldazmQaLDSQDPP8AU-O4pWClKgTIkjMxU_Pkg2PJlPNeRw7TLerShNKE5ziFP99Nv2IyKZjrpl_OBQYp-re-eQ1HuNZoS9gOs699yISU9uC7EWXxsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آب‌شیرین‌كن  بونجی جاسك تخریب شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68427" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68426">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=Cwlekyd4fB_4Khk2s7RxZSAr2KFbeURQO4SSTQLOSrlsBH717N7t81pt3F1J-SCDIl1MA4i_-4le8HFPyaTdk4lMjnOmDNfUNIMXj-TibW4DvyZcoJJip89XqVIzN2y0DYKpGA0_LoSrUVVL5xFbz1qPIbnezDqKxRLxRnJcV_ndvyuCxOT3W1Vkd4XnmoPgspO6qTMqcZaHAyuC-DqWCxgbhrF3zEEa6Rrt_U0VgpJlYwie7Zlb3FjjDzWl0NlLkRA_nKJSDxCUS4sZwPnESJTbqle17YD35ThC2TDJCACUoGhz4d6r-uHD83cEDI6zJpg8hObWf2-K2Tm3ohJdQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=Cwlekyd4fB_4Khk2s7RxZSAr2KFbeURQO4SSTQLOSrlsBH717N7t81pt3F1J-SCDIl1MA4i_-4le8HFPyaTdk4lMjnOmDNfUNIMXj-TibW4DvyZcoJJip89XqVIzN2y0DYKpGA0_LoSrUVVL5xFbz1qPIbnezDqKxRLxRnJcV_ndvyuCxOT3W1Vkd4XnmoPgspO6qTMqcZaHAyuC-DqWCxgbhrF3zEEa6Rrt_U0VgpJlYwie7Zlb3FjjDzWl0NlLkRA_nKJSDxCUS4sZwPnESJTbqle17YD35ThC2TDJCACUoGhz4d6r-uHD83cEDI6zJpg8hObWf2-K2Tm3ohJdQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تونل گلوگاه، در حملات شب گذشته آمریکا آسیب جدی دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68426" target="_blank">📅 11:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68425">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68425" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68424">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUYtBvOfJ6oGNNVAh6ky6lH_RiRM_H6ziwcNYvlL7pPaAShJgc--Ea033F2tgfHgyiU2DJiXFEI5MMTTFYz_tDu1305_Ykj27zXggYfC4gogCVDePovfz0WwDb_ObbJKYuq1n_MmQCO8_KHvvyZDUGlaq94o92S0JXbIyhejFtWkGtKPu_O788-LI6DcLDub5V24Cl1re45ELUhdqohs8rA5sFcWExIphWnGJu4kCURNtBKF6n5-aoawWzw4oBq8daHniOYZfZ3zSUQ7ANFyNNaOjvd_6foTulu23t21P5TFpr0o35HNp3YqD80BvQuV6QLMbbsxMKjJjqvw262M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است که دو نفت‌کش در تنگه هرمز، پس از برخورد با مین در این آبراه بین‌المللی، منفجر شده‌اند.
✔️
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران، نادرست است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68424" target="_blank">📅 10:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68423">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=pl_X6TIzcVZpwc26dxlmWKZO9fgYcQmxqwq-QyaHvw5yFDUFmKHsjgKF3qesSf6U6VxKBrr_7DeaKlr2VgYFMEcUIUGDGeqhG4dCNaXRTZyA45GVrfm55yBPejsXGaB9xCsTXXnE3151qL9qW93KN_JccUUyv2JZC9uWAlNVTA9ve-f9RF4MoCN_JyxiDQMsG8m0GT3SfLTRfHlZYaaKcuWzgXlWAXXW3RJo2GghofbQcMIxSELO0b0LPwzjnUJ4w4m-OTNOFyDrUxEVJotq--Dsi41gbkLJAmPRvrRl2VCrXZtmkE0c98uOuX89dZp8LjsDQx0OW1-uO-3fnrPAMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=pl_X6TIzcVZpwc26dxlmWKZO9fgYcQmxqwq-QyaHvw5yFDUFmKHsjgKF3qesSf6U6VxKBrr_7DeaKlr2VgYFMEcUIUGDGeqhG4dCNaXRTZyA45GVrfm55yBPejsXGaB9xCsTXXnE3151qL9qW93KN_JccUUyv2JZC9uWAlNVTA9ve-f9RF4MoCN_JyxiDQMsG8m0GT3SfLTRfHlZYaaKcuWzgXlWAXXW3RJo2GghofbQcMIxSELO0b0LPwzjnUJ4w4m-OTNOFyDrUxEVJotq--Dsi41gbkLJAmPRvrRl2VCrXZtmkE0c98uOuX89dZp8LjsDQx0OW1-uO-3fnrPAMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68423" target="_blank">📅 10:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68422">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkeqEq9Kc07YqdPLVlFg2qcah7JNnQLEzkHc39aQJsRd1TnMmztQOJhBIgnnJblIeZw17HwtagGOe4DhPWH2wSi4fO2VNtu_CgceOhrwAEevZggkdQYvROJpIEUxerytayGE784AjuBKz4D4H_4q4d17sKT_ZXWkWD5RNKEnyDbZjZx42s-FQkDWEMEP2VgAB_N_f68V3AobXE5ojUZAtS-zzvUfS-bGMmdHjJ1KGfpgfKO2O1oTfb-B_PUxWJA2bMO0slJByBV_qadokcm77u6WEd8WwMoFW8xhPh6gs6SSJdrVeq7KE6W0dOmgoidAryd9SYJh1N-EzsHKYhY7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اکسیوس:سه مقام آمریکایی و اسرائیلی اعلام کردند که دولت ترامپ به اسرائیل اطلاع داده است که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند هواپیمای سوخت‌رسان دیگر به این کشور اعزام می‌کند.
پس از آنکه روز سه‌شنبه چندین طرح نظامی جدید در جلسه «اتاق وضعیت» (Situation Room) به رئیس‌جمهور ترامپ ارائه شد، او در حال بررسی یک عملیات تهاجمی گسترده علیه ایران است؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
از جمله گزینه‌های در دست بررسی می‌توان به:
⏺
بمباران تأسیسات زیرساختی ایران مانند نیروگاه‌های برق،
⏺
انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف مدفون کردن عمیق‌تر اورانیوم غنی‌شده این کشور، و بمباران تأسیسات زیرزمینی «کوه پیک‌اکس» (Pickaxe Mountain) اشاره کرد که گمان می‌رود مرکزی در حال ساخت باشد.
ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد مایل است با تشدید درگیری و وارد کردن خساراتی سنگین، حکومت ایران را وادار به بازگشایی تنگه هرمز و پذیرش شرایط هسته‌ای ترامپ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68422" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4d15k8Mxr8fllcbazJ5zrlG19AerQ2ofugqnB8xmDq3PlZwHjxG1bfLUpepkWdjRFxzUGk4rY5h5Cr9AhEMvJr4b3OeR4EnT5n6Bj2vx_iXywb2jaGZ2hLc6mGd6QL5Vha-MxqyObHHGyYHxwKLD6pfQHnlCdFpkR7XBMCZKwd1YoZyzZYc5Bs4C6Cz0es3AA8vbJD0-h-XiULZDV8LjB_THBRu_OOWgR04ucBdRxaBhQmt3_r6KLWZXWwndPXxMjZD7-tEp_05DoiSLV_s4rqvb08wA9LTkgok7j0-aQA7YWi2eEDChX4FHQsKwYa1-o-N3dxeSitbCgm4bpYaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXMXEEVbf-OM1pbIxoFchx43DhbRVWuclZ5K6h4eKamuZDNA5e_GLyrS8rJxpLzKexK5F3r2PtscYchCZGlV1cQ8TIGyFfuZwBjjV_BurstCT-26Cb0F9C2ZLnD9sxXKKDl2fJMdYlZ66zBAuI831xTAdJUtXnUAHHwJUxoCeMe4py_6fDomlka0lgzlcHpITHpDO37tvkftlCETZxVFr2xyW77j9bASnUx3j8aJUEMmmLT0l52lDmetOUjQd9JPiFaypZ_TJDLNt32VByclL1GLIU3eU-WxSrt3hv-28pXSsHEqWXuRc1hJmYlGoXTgJdyJRX8JvT3-yP4ivywDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAoVSnlUQSZ953r30_l3MS3oTV1oBqG5PQsgA7plMuLazchyJkB-c4V6JfI4pK-YY8lkzO47Xg_47THpK8FH1zB5cE8UFYq3yNgC2mdvCAjlI5lsQ8jxewusbpavbRSYQtga4ixBk10nv4S8wtE8T3b7xeU-CnP2wCGquxOlxTawCCCSMLjhBd02r9TbJFemf8Z4vLmMAR67R_PFX1cn-MkWDWaeTBDxRSFeEa_kpYAsB10tL5IDkvSMOK3mx5ZJvgp26JxUvwgOyeYlrs0pZrdLaMTWoH8gL7fnzM_LWqaGGclEU9ZpWipx82ocOwyVwz_fIlgXGlJHEeBd9Nb0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=S3piqNxIN0GsIx0vmZtDaFfL_r02GPBiEI0rRHN7uE1TEzTS21J-kVigEU-iFas9dUefREhNuVyqbS7jmDdteXCkZg4earcDpKBk_z4Gq_jma7BavkeAqU2mimwJx7K27Tooavz7jdHs8wzWOkEpjgWGlsOfThGhwsyTfhJJPTA_T1vACgNzQTFh4-Do1wDmhwK-U5f1SZN1trGg6oS54atKVeHpk74V7DhTAfRkFEbsKmfvz3r_Bhy9mFiMMGqtY7CpKmxnSurZh4il6Y8jghVJfPa8wIJUPkpgoGfN7Rk-nDj4oItHvehi7TQWBMPbNozG1iSjuGpjZQJqVJFCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=S3piqNxIN0GsIx0vmZtDaFfL_r02GPBiEI0rRHN7uE1TEzTS21J-kVigEU-iFas9dUefREhNuVyqbS7jmDdteXCkZg4earcDpKBk_z4Gq_jma7BavkeAqU2mimwJx7K27Tooavz7jdHs8wzWOkEpjgWGlsOfThGhwsyTfhJJPTA_T1vACgNzQTFh4-Do1wDmhwK-U5f1SZN1trGg6oS54atKVeHpk74V7DhTAfRkFEbsKmfvz3r_Bhy9mFiMMGqtY7CpKmxnSurZh4il6Y8jghVJfPa8wIJUPkpgoGfN7Rk-nDj4oItHvehi7TQWBMPbNozG1iSjuGpjZQJqVJFCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm6DqqBK62HFx7O-2vs8SP43a0X1MJUswm5x06PjROvMCZl403dxqofmVcC73oDpgZnZUP_mPW3jUoARSlU-PlIXRvdnfXZ9X-2nSYddpmbIQQ7hZdUiqedzz_jrfu7-0No1GQ591OIhZCfJ5S_F5Jw-1puE7z4hrhQLfjMFX36540nm7a8GzEKDct6g3ThtUMe-eYYC4CTZ-vXQcQHpePyggxKAwSwDghJu-rzaYuZTSBgKotpCVmOpsnnPifhHuPSJhnZQSeECAM1IQIal3QdACEqtCe2A62wTVzYLxeOTT-oW1z7kpufjXu_fBB25tlXOragKdYPdLXvBW4rtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68411">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRlylymiWQSABQMrLp7Cfn9kGMCAU3o96uPPEppOVmnCWoPbDD_GOEn0-rRQD7iKo9ehzcvNGjZ-i8PQGkwSkXWaKULUwW3anbDihlSky2N9-N0ZMCDG_ZXLg4Sk79I6P9w9SeIFbq5oioPcftepTNQ7VcRfgsQR9aEUioaYWPEbkn5cfEqbugYELJK0c0psgvgx4BD8bGjGw2Iqw-LaACN5Zt4Cehn5lqxhRfz0MIjyNuRNwTdI0lGZXEHgc4qVbqXKzpgdVeCxKDoCLdhqiMg6RJDYZvlgiXsHZgk7rCGBWj4uiF1QFR6KEiyambWe74IljzzxxwwhYlisradQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پل سه‌راه‌ میناب به‌سمت رودان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68411" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68409">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_Oke44SkxVR7zhxWQ9nzYmljvHqa02w_HO32B6W0hTY6jlam0qDFY-lwMBqbHYNMA54ixgUrncxFRe1ZwRwBhaXbOBNzxkA_4WedG2VcgM3PnQhVhkqfH2msmVsXBFp2fTBLbC4-FdDtkx8VUe1aDSmaduAbgUZhz-659oRM_ucy0qp0-m7s76QSgagmPplDzXpU8SnTdA08jEeJKtVahpwr7OkdnMARnH1F3Ffk7vnC0jaBN8A2FE1785AIb-qkEDmHKmXvdmf5ctdqKyCZkPfZoZrb6ZeJwuwti3dYVrCteXo4mD5sRUIgnEdOqbpHzcr2mpI00OE2Oj9JdO5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5P-zDeJGh2JdsmUBA9Syqb4ewCTrbp-u3vyHnWAuxH2LBiQOB0dA4mk_M985Lssj6sjkIIkQTZsT4kaoRD6_14xNVlHZj7iOv8DBUgc52iOFO2B4v8kooIohdfJCStGYOEYBWpZRVNNmZ3AgTyVRY4T3BZjDWMQJsQsAD2MjbHm2SP_lF9FKEBsDQ_gXzGT2kMrObjBvLCUZVqiDqBcmgHCH3ta9tIgv63qFYuWQG8Pcp7-bJmmvqVNm6nhlADwHQlQJTVsvuV2eDhmCXwACMc_6MZP_tDvrxQgtXr5qIbaXB0hZkxo3G-zmISUNgFYXp_DMeIuzgI8X-wruMYEOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ارسالی از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68409" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68408">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=IYnT1GYkeKIZgoYvHCI8w2BYbEfAw647PHE1e0qajUhdABRf0oxjXrDct424OgPuHi3eybHkWFstNpcahHjVGYbU35DvX7bCjbbwi_kfYjHSKF3hD_Il47grMo-cJt695i_6d1qSL01OCv4QnHsWLrBjprXVfZhxB--sQTfy7JiyR5ZIS1qwtSpRSL8JPwbwGRfB4683bO7towmXu9dIOFGRJECOKCEje53GjDUBAzM7ygy8m6pDpEQ5qeB61mIqS3X9X86lxYpKPlgmVxffK4odFx6qm5G3ENEwzVq6lrNcjvmZBL_IOxBbCOJVT8HcCz3AEFutRDUbsPP5QXnldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=IYnT1GYkeKIZgoYvHCI8w2BYbEfAw647PHE1e0qajUhdABRf0oxjXrDct424OgPuHi3eybHkWFstNpcahHjVGYbU35DvX7bCjbbwi_kfYjHSKF3hD_Il47grMo-cJt695i_6d1qSL01OCv4QnHsWLrBjprXVfZhxB--sQTfy7JiyR5ZIS1qwtSpRSL8JPwbwGRfB4683bO7towmXu9dIOFGRJECOKCEje53GjDUBAzM7ygy8m6pDpEQ5qeB61mIqS3X9X86lxYpKPlgmVxffK4odFx6qm5G3ENEwzVq6lrNcjvmZBL_IOxBbCOJVT8HcCz3AEFutRDUbsPP5QXnldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68408" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68407">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
دو انفجار در خرم آباد شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68407" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68406">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از تبریز موشک شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68406" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68405">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=EDGRm9xV1w6ZVdXqc6w-W8anq8ts1IHkhZJpR8VcB2iQLfGB--PyMnU-CcUBhTqkN5oZZGbFiFd3QJ4ReNgkFn1Fmgqn8_gfAgGf-82zzsuuABKOVh_Ju_9hreO5NCvx0lrD0u83fWdGwQ_dN50-q3eV_vlaZ6pHc243w2pbHKqv1UnpdgI5G-W0WNSU07uV1YuGx6T9bARqCp4pfmMYD2qK7R0OewrkEm44iooVQX4Zf6Cr7bYQyc8cr_SDLJT7osmlHB-vmawgm2VBbe_A7JSMLwcUvK6dE7wvE94Wi6s4VFvfZN_IkR7vTMqR-Eb_RxBBzjyc5kXiRsGROoIwdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=EDGRm9xV1w6ZVdXqc6w-W8anq8ts1IHkhZJpR8VcB2iQLfGB--PyMnU-CcUBhTqkN5oZZGbFiFd3QJ4ReNgkFn1Fmgqn8_gfAgGf-82zzsuuABKOVh_Ju_9hreO5NCvx0lrD0u83fWdGwQ_dN50-q3eV_vlaZ6pHc243w2pbHKqv1UnpdgI5G-W0WNSU07uV1YuGx6T9bARqCp4pfmMYD2qK7R0OewrkEm44iooVQX4Zf6Cr7bYQyc8cr_SDLJT7osmlHB-vmawgm2VBbe_A7JSMLwcUvK6dE7wvE94Wi6s4VFvfZN_IkR7vTMqR-Eb_RxBBzjyc5kXiRsGROoIwdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند:
پل گلوگاه بعد گنو بندرعباس و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68405" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68404">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68404" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68403">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
منابع داخلی:
چند محور مواصلاتی هرمزگان در پی حملات آمریکا مسدود شد
؛
⏺
بر اساس اعلام منابع رسمی، تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت به دلیل حملات دشمن تا اطلاع ثانوی مسدود شده است.
⏺
همچنین پل «شور» هدف حمله قرار گرفته است.
⏺
بر پایه این گزارش، پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرزه، نیز مورد حمله دشمن قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68403" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68402">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBeavlZEer3Fv3n7dWc_OO4Os343Gd108xtfyDI4OVIMcfS429zWa2czBF7JMOsy-lwmBwOxy4nwshuPB6RQkCJozAL-ZbzXl2H24EplqJAQBe5TlaCBoXqTAHqc_jp7IfgGcO6ZuL_7lt8J02Z_XNLarA741xhsPhmRfCuCDqomzNiNj602npYYQ4j3eGmEIQPaAyGVI1bHpBnShOIYSovI88OxzaPPkO9iLQ9fo_n_V-Dy9wbqc1SetslqPpP911DmxgBfjTSF_e1HdCMb-GK-1lL1SoQhAGkJJBp7LFBb1ydPMkal5XhlXpjFMJtv2ClDzopzKkAzQ5nQ6Hu_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پل مسیر بندرعباس رودان هدف قرار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68402" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68401">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871564b347.mp4?token=jyhAF1DM6FDDuAo816U-lUjuOrh0iyFzEzRVf0y9DAyrok05T7LcjnwFvZJWjWjmbFF8Z4loprRUU3cVte0sdj67NQke5cxwcvOsIQbThf0kD4D7AM_fGB7tQ7ZNJDoxakRaA74Hv3dSwuBLlIFs8ylc0H_Ei_2UzKjNcwtqVbVN0I7EelJc74-p31CK6JmP8eRMkihqT5Td1A9O9YwrW_CXyMfWhZY15WNm8R5lzwJS7Wn_77KJzzd2WSuISVw9PHSsS3kNO4gyKeo3jRSqPHWNnnrmp2L4KFrhrC46Sw57IOTfVA-xZm-aLf78WeZA21Ao2bj-djptJ4hlLwzOrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871564b347.mp4?token=jyhAF1DM6FDDuAo816U-lUjuOrh0iyFzEzRVf0y9DAyrok05T7LcjnwFvZJWjWjmbFF8Z4loprRUU3cVte0sdj67NQke5cxwcvOsIQbThf0kD4D7AM_fGB7tQ7ZNJDoxakRaA74Hv3dSwuBLlIFs8ylc0H_Ei_2UzKjNcwtqVbVN0I7EelJc74-p31CK6JmP8eRMkihqT5Td1A9O9YwrW_CXyMfWhZY15WNm8R5lzwJS7Wn_77KJzzd2WSuISVw9PHSsS3kNO4gyKeo3jRSqPHWNnnrmp2L4KFrhrC46Sw57IOTfVA-xZm-aLf78WeZA21Ao2bj-djptJ4hlLwzOrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره پسرش بارون:
پسر بسیار قدبلندم، بارون. بارون عاشق فوتبال است و یک بازیکن خوب فوتبال است.
نمی‌دانم، سرعتش... من گفتم، وقتی یک بازیکن از اسپانیا، آرژانتین یا فرانسه از کنار شما رد می‌شود، بارون، چه اتفاقی می‌افتد؟""چه اتفاقی می‌افتد، بارون؟"
او گفت: "بابا، من یک توپ‌گیر خیلی خوب هستم!"
من گفتم: "اما بارون، اگر او سریع‌تر باشد، چه کار می‌کنی؟"
او گفت: "بابا، او هرگز از کنار من رد نمی‌شود!"
"من گفتم: "اما اگر این اتفاق بیفتد؟" و او نمی‌خواست به این سوال پاسخ دهد.
به نظر من، سرعت در این ورزش بسیار مهم است، شما موافقید؟"
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68401" target="_blank">📅 01:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68400">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
تسنیم:
حملات مجدد دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68400" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68399">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=coDQSEg1I4qfeo8ufWKyEOAcFgN6ShN5OBMa-ruaqooJ5NJJvTV-3AGUt0C4kQzBWmHGP09iHUfFgHmSoYPX4JXwRKd-2ezccfUaaWNllRONYBE4QV65sQg5_fhHvDpV8Fg3fOSsdnX9jNxiIFTLNRUi-8Innznbwmr6yhK3krtrnOSJxvGooS8CmbnvJ99ggxehv42JncCBXILIoSKaPiO52OPjwrqSmlcJFjaIgpO1sYQKJ4eqbP2y-NDed8JOCRS0CreFzpsyOBXyEvEhO3ONew5ojfsPxmHLNeAs111Av9JKQBz0J_5pYwef6BGtd8QYuI1kWBPjFPkCH1k-sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=coDQSEg1I4qfeo8ufWKyEOAcFgN6ShN5OBMa-ruaqooJ5NJJvTV-3AGUt0C4kQzBWmHGP09iHUfFgHmSoYPX4JXwRKd-2ezccfUaaWNllRONYBE4QV65sQg5_fhHvDpV8Fg3fOSsdnX9jNxiIFTLNRUi-8Innznbwmr6yhK3krtrnOSJxvGooS8CmbnvJ99ggxehv42JncCBXILIoSKaPiO52OPjwrqSmlcJFjaIgpO1sYQKJ4eqbP2y-NDed8JOCRS0CreFzpsyOBXyEvEhO3ONew5ojfsPxmHLNeAs111Av9JKQBz0J_5pYwef6BGtd8QYuI1kWBPjFPkCH1k-sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دموکرات ها در انتخابات تقلب کردند، و من چه چیزی نصیبم شد؟ جام جهانی نصیبم شد. المپیک نصیبم شد و آن‌ها را به اینجا آوردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68399" target="_blank">📅 01:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68398">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در لار
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68398" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68397">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
دو فروند کشتی نفت‌کش با عبور از مسیر مین‌گذاری‌شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68397" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68396">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=Dygb9wYgMuFQEm8vcSz0u-E8wyqpxXfM4k_bW3YkG28jhuwr2LeCZ0UbzI_YS87dzlxuGl9gcn7StSvyXuBpIiR4R16pVVSFzw0UaCHC7lEH-8b8v0lzdTnrzCOsm8KhQynpUYW-tqZOHDZFDn6Oszfds4rOnTJ6xDEhgzA-ZFRw3vzl9XwcK9YOFPBDSPBnHWQMKLMoP10KhOS_f1YyvAz5zYIdNyPw0KsooR6eplfNSfYd3Hbe1iVz8HGZ1F24keT4U9zna3XKXwZeI2l5FHgqNZ_om9NAMfpeZJmf7XKJZU3GaDl7pMS3eSbXWvcqG8nc3hPF3OTRj5z6kuDXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=Dygb9wYgMuFQEm8vcSz0u-E8wyqpxXfM4k_bW3YkG28jhuwr2LeCZ0UbzI_YS87dzlxuGl9gcn7StSvyXuBpIiR4R16pVVSFzw0UaCHC7lEH-8b8v0lzdTnrzCOsm8KhQynpUYW-tqZOHDZFDn6Oszfds4rOnTJ6xDEhgzA-ZFRw3vzl9XwcK9YOFPBDSPBnHWQMKLMoP10KhOS_f1YyvAz5zYIdNyPw0KsooR6eplfNSfYd3Hbe1iVz8HGZ1F24keT4U9zna3XKXwZeI2l5FHgqNZ_om9NAMfpeZJmf7XKJZU3GaDl7pMS3eSbXWvcqG8nc3hPF3OTRj5z6kuDXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به یزد صدای جنگنده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68396" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68395">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خفه شو کصکش
#hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68395" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68394">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
ترامپ: هری‌کین هم خوبه ولی ممکنه تو پست اشتباهی بازی کنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68394" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68393">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
ترامپ: مسی خیلی خفنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68393" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68392">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
ترامپ: رونالدو مرد بزرگیه
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68392" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68391">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68391" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68390">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68390" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68389">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68389" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68388">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=XJ68FFylnnuPnnxzaFS6pwwfMsM0Rw_dMPmGMxqmTf99rL9AodrrTbkxIE9e2JNDPvWOdD_kR0LYY9p2tqJCzJp9_hXZIl3AxVrKaWR3TsOKxnbMIFwvufOY1O1JOu8JIEw-UElMxroeZLVs0OsNu46TH0P9eyzPnDKuM04LhX2XtILgKEPiv4OXZzU4VqosCw9lCe2Dy23Xc4MLkUWQj0F-a4YwDHdADMYmrbb--pZPevGLoYuF6NkGhovOxFA3up00FYOx82P2BBoWpsHiLzQ4iQWWfi_BbVjnEYfUg2A25fweMnYQKFZDdiCdUv-BdrEHU5nmvT7HB5AaNIhyzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=XJ68FFylnnuPnnxzaFS6pwwfMsM0Rw_dMPmGMxqmTf99rL9AodrrTbkxIE9e2JNDPvWOdD_kR0LYY9p2tqJCzJp9_hXZIl3AxVrKaWR3TsOKxnbMIFwvufOY1O1JOu8JIEw-UElMxroeZLVs0OsNu46TH0P9eyzPnDKuM04LhX2XtILgKEPiv4OXZzU4VqosCw9lCe2Dy23Xc4MLkUWQj0F-a4YwDHdADMYmrbb--pZPevGLoYuF6NkGhovOxFA3up00FYOx82P2BBoWpsHiLzQ4iQWWfi_BbVjnEYfUg2A25fweMnYQKFZDdiCdUv-BdrEHU5nmvT7HB5AaNIhyzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما ۵ دقیقه بعد از حمله به شهر های مختلف ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68388" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68387">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
دقایقی قبل آمریکا به نقاطی در داراب حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68387" target="_blank">📅 01:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68386">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
فارس:
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68386" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68385">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=smcg5Gii4ACywYr_ggC1PeRCb6aa8cRkgD2udSBMdAK-hb9LpGGmk96XCf6lwjV9l8GCXGGCaiPsPdYvLQZKxw_1rtA9AxdV3txTeDLyrMWX5J171fDBXEWJ9QBi16LC38qPsYTfAKns7PrxriJKOvNJK2o2_RuMVB-pt76FfJfSjnl3eYhhs8sseK_UCWxlyjVyBIz4cV0PWvne49aTYWNQa_qDe1ryzrZKsaVKnLW16JvfhXKSqET3FS6C8g1S5GQ6miMlWOnYRZqa_tnQzFpSSSt2UmmMKkUoPnvW1VWEOger7ZGbErTJPVDB0xVCBE6e2EwbKCS4_hPnZ2eRVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=smcg5Gii4ACywYr_ggC1PeRCb6aa8cRkgD2udSBMdAK-hb9LpGGmk96XCf6lwjV9l8GCXGGCaiPsPdYvLQZKxw_1rtA9AxdV3txTeDLyrMWX5J171fDBXEWJ9QBi16LC38qPsYTfAKns7PrxriJKOvNJK2o2_RuMVB-pt76FfJfSjnl3eYhhs8sseK_UCWxlyjVyBIz4cV0PWvne49aTYWNQa_qDe1ryzrZKsaVKnLW16JvfhXKSqET3FS6C8g1S5GQ6miMlWOnYRZqa_tnQzFpSSSt2UmmMKkUoPnvW1VWEOger7ZGbErTJPVDB0xVCBE6e2EwbKCS4_hPnZ2eRVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به لار
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68385" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68384">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
معاون استانداری خوزستان:
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68384" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68383">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=IQ19cov5WHWmwKR8qA8WH6KPwa0qoum6EB1Gz4dRnCIntNmTicLKuYK10F8chWtddjUnQdzn-SFjCqp-gzAqxa8gGydDkjInN-rqKVEy1ACFE2pC2dlz9gYrMp3qOFUTqGkEBYaYlU6IQ-Tq8S9B7DpnjJT_gND46v0jlm_lyIE65D6CNesypObziY2OSit6GW1aUir6PERG8CXkyuulkDeEhxeGqnXR5EHgB_UwcPdkoMoym-63MkRkq5M1AbBXXBa6f5d76XToytVCyGCG8U5-wi7mnaHO7YkRgcfD02pfIymzkeYRfwgxVMHn4E_IJItbfvN-SxcMWuxwMlDH_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=IQ19cov5WHWmwKR8qA8WH6KPwa0qoum6EB1Gz4dRnCIntNmTicLKuYK10F8chWtddjUnQdzn-SFjCqp-gzAqxa8gGydDkjInN-rqKVEy1ACFE2pC2dlz9gYrMp3qOFUTqGkEBYaYlU6IQ-Tq8S9B7DpnjJT_gND46v0jlm_lyIE65D6CNesypObziY2OSit6GW1aUir6PERG8CXkyuulkDeEhxeGqnXR5EHgB_UwcPdkoMoym-63MkRkq5M1AbBXXBa6f5d76XToytVCyGCG8U5-wi7mnaHO7YkRgcfD02pfIymzkeYRfwgxVMHn4E_IJItbfvN-SxcMWuxwMlDH_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا به سایت موشکی یزد
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68383" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68382">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ممکنه امشب، سخت‌ترین شب برای جنوب باشه
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68382" target="_blank">📅 00:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68381">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از چندین انفجار در یزد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68381" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68380">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428210a926.mp4?token=ZHD9YGGexuzPTU0r4Ksb6fOLWuaTAp_V1pMcbBsVY8d9ymSA5dX7Lx1hth5RVTsYBzlmJj3JeBTn5UHQjJ9CBIIcBAfVW4JNSJ3-zgao9jPifMEqqdKZocR2aEy-8cjYYEx4KWoRVvY6JM6q10svekPCpE6ZQ_tl6kPCwvFpSqMxt2AcwKXfAqQ7hWqGVFdqP3qqkHRvrwkiHpU2aAIHxlYrc2970Yc0AMQOKNNRiXIvpmyXk_iOgZW3t9M0gt-3YCpKSyP6DXdRO4mszvyXFAPPw7kdVkS39dw6kehe38Jv3iMjUQvOTooYPtTrOPqlos3PFWarWNe3cF3xUSsPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428210a926.mp4?token=ZHD9YGGexuzPTU0r4Ksb6fOLWuaTAp_V1pMcbBsVY8d9ymSA5dX7Lx1hth5RVTsYBzlmJj3JeBTn5UHQjJ9CBIIcBAfVW4JNSJ3-zgao9jPifMEqqdKZocR2aEy-8cjYYEx4KWoRVvY6JM6q10svekPCpE6ZQ_tl6kPCwvFpSqMxt2AcwKXfAqQ7hWqGVFdqP3qqkHRvrwkiHpU2aAIHxlYrc2970Yc0AMQOKNNRiXIvpmyXk_iOgZW3t9M0gt-3YCpKSyP6DXdRO4mszvyXFAPPw7kdVkS39dw6kehe38Jv3iMjUQvOTooYPtTrOPqlos3PFWarWNe3cF3xUSsPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حمله آمریکا به لارستان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68380" target="_blank">📅 00:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68379">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
گزارش ها از انفجار در لارستان استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68379" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68378">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
انفجارر
بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68378" target="_blank">📅 23:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68377">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
سیریک و اهواز انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68377" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68376">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
قشم رو وحشتناک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68376" target="_blank">📅 23:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68375">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68375" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68374">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68374" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68373">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68373" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68372">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrhJ0I97sfuKgpSBADJNyZlFHGFJRRQGCITuh1c1aASRdljme-A8PlsS4DlnPqsqZwpZBW_JqU7w_eZ37kpjqmFjHJWpTHIVaFiNMMwdt5fl413Zy45zsm3E5ll7GOWqltU2Kk9AZsfwOlo86J-0VPPdkixhQn1GMDpR2WQml2bXJn9eU6Czg0t_LEwEBvhusPOuFJtYWfNGky4kc43eCjlK2q3o3X_hGbpcZvprbs68e1-wk_u7jFJcSwWi2it4xkQMd79a6pe4WFM5f0yTc8leVGUirnl3LKndSZKbHGbNRNNN6Ihicx3A67SOZrpIeMAeaXBeDZRgN-dT2jh62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
سنتکام امروز ساعت ۳ بعدازظهر (به وقت شرقی) و برای هفتمین شب پیاپی، دور جدیدی از حملات را علیه ایران آغاز کرد. این حملات با هدف تداوم تضعیف توانمندی‌های نظامی ایران و بنا بر دستور فرمانده کل انجام می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68372" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68371">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
با اعلام سنتکام دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68371" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68370">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68370" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68368">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyasEaMQYAvKfdC6kKY5zQTIIfeuq-mO1QEjWC4t7nVbIm6mUTejyZDZ9Oq7FCgmI8AUw1Bor-Id-ye9QCYyIAyTZbRbAWkQUX1Bj3MBMVfTf6ifrQkTqexh5-rJXF6t4gfBtK_7SE_IjedOSi6Fj9Wt8s1UbInCVL-SLDPmpVwahSsBrb49vrLj0j2XolP5_UmxaQfqHKIWA9-OffQuGTZoldUswbRTx9qPnX4-OUFiGgwcsQE2oOuiGawiAvznY1ikgR5vric8q4aQ9vOGQEudEnLC_xuwuV2VYb8RNijskYADLo3v-hzpi6Ktn_-ssvWOlNqzC1DYRTIMdY5gBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J9YGGQse2gmFNCSbvTOZEBD6F-n5ZO2JqKOZJUggBQDxCsAkhFnThOb66daFpl-bAvtqHlkZqjKaCko87iWoqHF8EBFGllk7zq6QvJeKB2kumaCA6L0G3Bt17CZVcQBt7OvX2sF4D2rouAO_nWbxdOKGhnGYHBPGR25-HwT2P8X2TbVBWv0A7ec3XVwfplPDWD1vESdDnfXeKN98byuWjOpUJU0TaZ68ZWFYwjoS0gm_fy1KY_n2eusp2-5iDgvFICYWFZbRLzVNIIFRr9anxqOuw_BMbrA_B2IyW77B6jT80yD71jFYfi64cqGUHPEg7UHPCzoYGCIF-xBj0UT5rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:
علی دایی رانتیه و آرزوی بمباران ایران رو داره
!!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68368" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68367">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=jHko2NFl77CaZPxcJmW8odRbi-swTVe6lBfr_qL7MUnYe0kTI7mGTvy_1mtlVGxNt0qE9dLB5xH_AE5V4BjP1URa8bcwDVtr3YLiiI-pLbS-wgg0m8slaOlKwLzCQG20Ilj2c4GdyCvbP3bTC7MgktrB6NLfehHu3B8s03LRVQ2zPOq_w_X8f-9FoelC6Vt_bMmFsvX8pInivyQIoNHg9i1JWlnpdGIkilYkip-eUbJTJbUNg_hhrVcrfIQnEh7WFjlACRVIHQLdpCjrNkHBComTau2TMbtWnkNSTGNa5XOfz_OSrBYNRRuD6b6vVoOws7OgUGamGiG4Q4cfq282-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=jHko2NFl77CaZPxcJmW8odRbi-swTVe6lBfr_qL7MUnYe0kTI7mGTvy_1mtlVGxNt0qE9dLB5xH_AE5V4BjP1URa8bcwDVtr3YLiiI-pLbS-wgg0m8slaOlKwLzCQG20Ilj2c4GdyCvbP3bTC7MgktrB6NLfehHu3B8s03LRVQ2zPOq_w_X8f-9FoelC6Vt_bMmFsvX8pInivyQIoNHg9i1JWlnpdGIkilYkip-eUbJTJbUNg_hhrVcrfIQnEh7WFjlACRVIHQLdpCjrNkHBComTau2TMbtWnkNSTGNa5XOfz_OSrBYNRRuD6b6vVoOws7OgUGamGiG4Q4cfq282-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آرش اعلایی به جی دی ونس گفت مادرجنده
😂
:
جی دی ونس یک مادری داشته که هروئینی بوده و مدت بسیار زیادی به مواد مخدر اعتیاد داشته
مادرش پشت سرهم مجبور بوده از یک خونه به خونه دیگه بره
جی دی ونس یک کتاب داره که توش نوشته چندتا دوست پسر مامانش داشته و چطوری دوست پسراشو میاورده خونه و چقدر کمبود داشته
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68367" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=QySszFAhFUQNh3udRtuLcmK9IejItBUinhX0Jv8QeeS89Psav_XC5qN8_UGT5qLCsR0bEMpNhxBHNt9mMpuazdtmx2SDyqUaFUxTlHB9D958rKdsoBxKEDvMzC339CgxudLvUXjTY7smh2a0GfKTlPBs89GqgSEsWj09cZly-6ZBe11JNQe6BS0Z1DKLhhcBz3MFrTisnDVsaLAQCyX_A6dI2-pfNSL4qNn2wQOLY3M3BCArsaLurFqsFUVf0bkio7eO2FOIGoXKowbe_D9dKf1WNecU1GFhpk5kqmBmkjiDfdmCJJYS0H8PCdc13KS_iLs571coNiXdtcD8VNeT56cNJ6kMUlESkc7UEt9eOhQxU5I4wHv--duXJrO_esX-CzGozyqi8P7O3ZQaK6xvnPa6KVQuzzt6SLCc8NsbzaBauojPMFdj5rlPbpwyqoieY26AZeHWXCwn9hu9XOIJMK8UrUcQu9CYsfgFMqcaSBr69kxpK6N5dJnO7RzPL9q_xQJC6XjcmylP4BnCozoA7GvDohL6W5UI7Irq5eEyFovylUTPwOZApFGxfoH509qi-C-kL-cj-Zyc3IEjMGuYxy1AF-QZTJlF2Y_IghZScKLu1aalj59XeGsk4Y8m2ny2OdMC7rSGpf4R_aGh9EI7FVlk0XZ1k7YgoSc9MVmAEIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=QySszFAhFUQNh3udRtuLcmK9IejItBUinhX0Jv8QeeS89Psav_XC5qN8_UGT5qLCsR0bEMpNhxBHNt9mMpuazdtmx2SDyqUaFUxTlHB9D958rKdsoBxKEDvMzC339CgxudLvUXjTY7smh2a0GfKTlPBs89GqgSEsWj09cZly-6ZBe11JNQe6BS0Z1DKLhhcBz3MFrTisnDVsaLAQCyX_A6dI2-pfNSL4qNn2wQOLY3M3BCArsaLurFqsFUVf0bkio7eO2FOIGoXKowbe_D9dKf1WNecU1GFhpk5kqmBmkjiDfdmCJJYS0H8PCdc13KS_iLs571coNiXdtcD8VNeT56cNJ6kMUlESkc7UEt9eOhQxU5I4wHv--duXJrO_esX-CzGozyqi8P7O3ZQaK6xvnPa6KVQuzzt6SLCc8NsbzaBauojPMFdj5rlPbpwyqoieY26AZeHWXCwn9hu9XOIJMK8UrUcQu9CYsfgFMqcaSBr69kxpK6N5dJnO7RzPL9q_xQJC6XjcmylP4BnCozoA7GvDohL6W5UI7Irq5eEyFovylUTPwOZApFGxfoH509qi-C-kL-cj-Zyc3IEjMGuYxy1AF-QZTJlF2Y_IghZScKLu1aalj59XeGsk4Y8m2ny2OdMC7rSGpf4R_aGh9EI7FVlk0XZ1k7YgoSc9MVmAEIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای که گفته میشه مربوط به کشتی تایلندی هست که مورداصابت قرار گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68366" target="_blank">📅 22:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68365" target="_blank">📅 21:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68364">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68364" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68361">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=Wklgcf1m-99gNtVueLVnGhZKTeO0WQNvc0h1xHVyt9iggqi5leCiI73ocL3Bd56B97cJC6RqZnt5V9D5eXETcLnHFJvX1A_CDGqYaBbA2PobBjrYSUXYk-NCb4GR45QSI3OPekhugM5zuw2YuELwx_p4QRMi9XLq7M-ts2Kaudwo43jlXtQUBu_slhbCLmLgR2RpPnD55o5TLes4eRmfYrcnY_Km8So-4Ash1mKKP34d3EuXnP2srqRpcqtNLdXXREOcHn30ykADM_hq6riGNIeQ3CX69SWUqDHg5PhYCxZU2sfnHQ31vabaLsLa3b_5hzGH6cqOWZaBYpmGbpp6JA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=Wklgcf1m-99gNtVueLVnGhZKTeO0WQNvc0h1xHVyt9iggqi5leCiI73ocL3Bd56B97cJC6RqZnt5V9D5eXETcLnHFJvX1A_CDGqYaBbA2PobBjrYSUXYk-NCb4GR45QSI3OPekhugM5zuw2YuELwx_p4QRMi9XLq7M-ts2Kaudwo43jlXtQUBu_slhbCLmLgR2RpPnD55o5TLes4eRmfYrcnY_Km8So-4Ash1mKKP34d3EuXnP2srqRpcqtNLdXXREOcHn30ykADM_hq6riGNIeQ3CX69SWUqDHg5PhYCxZU2sfnHQ31vabaLsLa3b_5hzGH6cqOWZaBYpmGbpp6JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت اقلیم کردستان پس از حملات جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68361" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68360">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68360" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5BBlQ9171nSbPQbd8Q73PrtlXi1JBNrlvZXvBLF88B2Fi8IUJw1iUQsYtH7zZHr70oezdsLwfS6ha3to9HyyalPnfqh-0RqoASSWfHiX70FHZzuXu9BNy25QLEYO7ac_YLjdtR3A-5Zq3VPoNLlmdpnpXbnQVqM42rWXOqxdpEtKrF11x4dQuMBcL-9wt9YTzo17fb2qEgmrGpUphcepvwcWffh6JAInOPxO2DEEYONsS1H2cjwxLXSRIf-_2qycFFQSuz_aqr6UeY6FQx87H1ek3oAMnTX_PhfH7j34hngtuUIcBpIHjME1Tq1YtNCYYxuU2h1lVy20opXcXJqCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68359" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1d9D74A8chkdGp06Srm9GFJIJSHBrMj_iHeTG-i6kk3mxaI2cygivUcP8WtaDJgMNRdo_HHR5JPzMJRrEo94kVh_o0ze76J6MCCLisi2QsOPutrO3JBekjnWXUb8sU8IvQKI37Vh6i_ip3ndxzMvu5I_w2ImE2Nd_fqX5Q4RaN-DX_KpXPqsQhycQE6kN7phxQsvaqpY16XDGnXXt_u13k1BzjmoEB6NpU_-o-4xelUvNGbmE-TWQlR6ABNLQISg06IGVQcdYDBaZNnem6P22xXeQ6QvjFfkMHwPe4g_hycuKUEHViX3L1RuQgutaxEpinO9ClmyQdQC-F9io9hsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تعداد بیشتری از جنگنده‌های آمریکایی مدل F-16 که از اروپا به این منطقه اعزام شده‌اند، با پشتیبانی هواپیماهای تانکردار KC-135، در حال استقرار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68358" target="_blank">📅 21:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=gykQqJE2PlN1cZG6iAUUoLbbVBXi89EsMueR9vtkMtK93sjtitufY8EtoENDIbVUT11sGteREkQhZJO5C8E-7EPRgzLE0VIrAri-4JddmfaQzzJ-J5bYP67rufo2CSmTwoKbvSt-b9JH3yHXu60_oJ8_pSGsajpdyecfJtXKM1nD3cbjFH_rNXud4wIxqh6IUAfuisS4JYQArQ7Bl6NKIjGkpAKQlpcivJxrJBEwXyrKIwrMYqCzEcO5wY07NjZFRrJf7-4faepMRXSjtkkz9igUZqlBRg9ThcSKPRD1e3JkDMvz3-67-UjqIRFw0OfQSmvbzg_jK5SsVgEujHEqQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=gykQqJE2PlN1cZG6iAUUoLbbVBXi89EsMueR9vtkMtK93sjtitufY8EtoENDIbVUT11sGteREkQhZJO5C8E-7EPRgzLE0VIrAri-4JddmfaQzzJ-J5bYP67rufo2CSmTwoKbvSt-b9JH3yHXu60_oJ8_pSGsajpdyecfJtXKM1nD3cbjFH_rNXud4wIxqh6IUAfuisS4JYQArQ7Bl6NKIjGkpAKQlpcivJxrJBEwXyrKIwrMYqCzEcO5wY07NjZFRrJf7-4faepMRXSjtkkz9igUZqlBRg9ThcSKPRD1e3JkDMvz3-67-UjqIRFw0OfQSmvbzg_jK5SsVgEujHEqQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترافیک تنگه هرمز در ۱۶ جولای به کمترین میزان در طول سه هفته گذشته رسید و تنها هشت کشتی از این مسیر عبور کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68357" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
