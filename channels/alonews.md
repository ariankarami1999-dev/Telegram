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
<img src="https://cdn4.telesco.pe/file/S3IdUroGKnTseHkP9ZLAZKAWQvGTbB9RI1irxMNz9_cnkg9iA97KLB-GBZGZwSj2vT6SUuQQV8T-tybNH2Cytf_LxZ0l8jqoJfJInd_Bf_ZWENIiYgntSi0jZEJBC9LPG-9hMIbpgMWnSzaRiUY5tZY0XuBH728vLdx4mvecXYNqgajYbt6YpXz08nW0y4IC071Hx1fXnMCwHOOD2O9peum64VA8s6UpMlNUlS8sFFouElzgLba0kpH7KnRFcAW25sPbGkMKS90dHZNDUtzb6h76FrwGAd8hjZ1EmSt_PsZNRtP7RaL2WC247Udx97RDiw_Bc7fYQpDfSw1999iRiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 22:37:13</div>
<hr>

<div class="tg-post" id="msg-131802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
حوثی‌ها با انتشار ویدئو : برای همه احتمالات آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/131802" target="_blank">📅 22:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131801">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c8672f92.mp4?token=LHksyftK-hx1iTnBrTbyRcJYOo5JyVy5RdE-IEh28gH6AAxuoRCZcaaY112p-VaxMRik8xV1rN4Kcpe-3lT1zitiyxydE8zFns7ExtTc5J1V8Uwmyw7KncwiRiZJsfD5GGq5rzrU4qWONAgRMYWutv5HZk7qdBdhnLss6iYJ0d9sWlKf1alPdUI-7vKsGZm8XoSO-Lg2sDVLaqGT90DkGC84apFXF7PfVpgo-jBKKjPuvZxPffsyyHmYdJgQ7R3ajszpYtvdCMHA4WTJqK357yUwKa7A0pGXJEsa4Kr-tlHd0v69Xni2avlfLCH-w_c90C1wud_IRwKncsqyXr3UOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c8672f92.mp4?token=LHksyftK-hx1iTnBrTbyRcJYOo5JyVy5RdE-IEh28gH6AAxuoRCZcaaY112p-VaxMRik8xV1rN4Kcpe-3lT1zitiyxydE8zFns7ExtTc5J1V8Uwmyw7KncwiRiZJsfD5GGq5rzrU4qWONAgRMYWutv5HZk7qdBdhnLss6iYJ0d9sWlKf1alPdUI-7vKsGZm8XoSO-Lg2sDVLaqGT90DkGC84apFXF7PfVpgo-jBKKjPuvZxPffsyyHmYdJgQ7R3ajszpYtvdCMHA4WTJqK357yUwKa7A0pGXJEsa4Kr-tlHd0v69Xni2avlfLCH-w_c90C1wud_IRwKncsqyXr3UOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار تانکر سوخت در آمریکا
🔴
پلیس شهرستان مونتگومری در ایالت آلابامای آمریکا روز شنبه از انفجار یک تانکر سوخت و آتش‌سوزی در محل حادثه خبر داد.
🔴
این انفجار حوالی ظهر به وقت محلی رخ داده و علت آن نقض فنی اعلام شده است.
🔴
این حادثه منجر به قطع برق چندین خانه در منطقه شد. پلیس از مردم خواست تا از ورود به این منطقه خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/131801" target="_blank">📅 22:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
واشنگتن پست: ایران در موقعیت قوی‌تری در تقابل با آمریکا قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131800" target="_blank">📅 22:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131799">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/131799" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
شرکت ملی پخش فرآورده‌های نفتی:
هیچ جایگاهی بدون بنزین نمی‌ماند
🔴
سوخت هواپیماهای حامل هیات‌های خارجی تامین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/131798" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131797">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
دولت ونزوئلا : تعداد کشته‌ها به
۲۹۵۴
نفر افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/131797" target="_blank">📅 21:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131796">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
صداسیما: از صبح تاکنون بیش از ۲۰ بار مصلی پر و خالی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/131796" target="_blank">📅 21:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131795">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d5d97bd2.mp4?token=t2zqe_ONuZL_7xzKy5mlxtv2OYsP8ETMszBNFM4VbwPDO1ec1X_mxRGWdpqRC4S1Ji56ll9s8d2eakmE8_1HST9-gxpknB4n6y3htaahR1H2N-JR06NRfbDSvwi7LMk42M7l4uZ9ten6gkdVpagT5X5B8lztJ6XihJqaQiSEfp1m4qWx6NKsnoq7CGQM10LbNc5OLKxwvwjj8jvNaILQGPcVGSptYwC65KnT5H8nvANPhxVovLaGNdsJ3hcCoUmPvXLHm3VXU0vTllTI6x-AJknyZg-xEiGw-iP_SbYpm35E-glElpSSY4dw3VvtYBrTJO6zgT4n3zqY5qOpmy4cCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d5d97bd2.mp4?token=t2zqe_ONuZL_7xzKy5mlxtv2OYsP8ETMszBNFM4VbwPDO1ec1X_mxRGWdpqRC4S1Ji56ll9s8d2eakmE8_1HST9-gxpknB4n6y3htaahR1H2N-JR06NRfbDSvwi7LMk42M7l4uZ9ten6gkdVpagT5X5B8lztJ6XihJqaQiSEfp1m4qWx6NKsnoq7CGQM10LbNc5OLKxwvwjj8jvNaILQGPcVGSptYwC65KnT5H8nvANPhxVovLaGNdsJ3hcCoUmPvXLHm3VXU0vTllTI6x-AJknyZg-xEiGw-iP_SbYpm35E-glElpSSY4dw3VvtYBrTJO6zgT4n3zqY5qOpmy4cCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که امروز زودتر، یک شبه‌نظامی متهم حزب‌الله در پی تعقیب در مجدل زون، منطقه صور، لبنان توسط نیروهای زمینی ارتش اسرائیل کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/131795" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-n7JO-yg-xQajnoiv3Fka0g1XQAp2Haz4Kje9FqefzBitOLXflcsHTVotYhZVP_M93bAinzpmN6wU-LllK1qUduOsxIfjTrawlPMwDLjXhV-FzsWE_CDYfroGwUjxTTKBCThw0D-dOepuuhnmtrJqPxG8O1pozuDnPQ-8zSwf0v2lQlos4YVHimmlbSs9yFOUcxTA3_JhgfGd0ZTIY_pJLeCEy65d41YDIgxa31UREpVo3nDysYdBCJRF13nQVS2A-mN5Fhp4lKv8MGNi9qPrpv5olsZlLOb1yCiuc2Th3St8GtzO3mtKSWAOeciMtgsPtzuPyXjrpH_kr7firWJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به آکسیوس: نتانیاهو میداند رئیس کیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131794" target="_blank">📅 21:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ادعای کانال ۱۵ اسرائیل: منابع مطلع فاش کردند که ارتش اسرائیل آماده است تا یک مقر و سنگر مستحکم حزب‌الله در منطقه «علی طاهر» را مورد تهاجم قرار دهد، اما این عملیات با دستور مستقیم نتانیاهو متوقف شده است.
🔴
این تصمیم در پاسخ به درخواست رئیس‌جمهور آمریکا، دونالد ترامپ، گرفته شده است؛ کسی که «در حال حاضر نمی‌خواهد در لبنان انفجارهایی رخ دهد»، تا مذاکرات حساسی که او با ایران در جریان دارد دچار اختلال نشود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131793" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfVZG0DyavFRgltXoikjQQeIDEBifsothvsV-1-zcDdqsvKLElbWlaJQzmMt5aA4ESb_1pQ6wdwZH9krcaCZt2wuLBnd_g0WjtAYbI0fwtP5ersW8OyWQdarWjC2ZEKvingzcWJYSxFML5smKcNxo-8KIJVsnxMl5ZAY_wXH142FTxsbtlN5Qu5ubWTujKpSYnx9Lrc4H_ittoDojSvOaH7sHSdQCcGeZBccLHMQ2Y7C_-GSA77nJOjwfGmUowtOO-nLjGj_TWqV-LXySvd1cWZvvwdxXOzftFGYVQzewH_pgB5lZaFmBlB4OoeJ1I1i771Z-3f8zaMZ73apCcWDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131792" target="_blank">📅 21:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آکسیوس: بسیاری از نزدیک‌ترین مشاوران ترامپ معتقدند که «بنیامین نتانیاهو» در همه چیز اشتباه می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131791" target="_blank">📅 21:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نتانیاهو : ۲۵۰ سالگی آمریکا رو به ترامپ تبریک میگم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/131790" target="_blank">📅 21:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
انصارالله یمن : با حضور تو تهران، محاصره دشمن رو شکست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/131789" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: بنیامین نتانیاهو درخواست ملاقات در کاخ سفید را داده است که می‌تواند اوایل هفته آینده انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131788" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
العربیه: هیئت ایرانی شامل قالیباف و عراقچی بعد از مراسم برای ادامع مذاکرات به پاکستان خواهند رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131787" target="_blank">📅 20:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
اکسیوس : ترامپ می‌گوید که ایران «می‌خواهد به توافق برسد» اما گفت که هر دو طرف توافق کرده‌اند که مذاکرات هسته‌ای را به مدت یک هفته متوقف کنند تا وقایع مربوط به تشییع پیکر  رهبرشان به پایان برسد.
🔴
او افزود که هیچ یک از طرفین در طول این توقف به دیگری حمله نخواهد کرد.
🔴
ترامپ :  از دیدن گریه مردم ایران در تشییع آیت‌الله خامنه‌ای غافلگیر شدم؛ چراکه فکر می‌کردم مردم از او متنفر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131786" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY7lh2KSVcD2YAaTaIsXejiY15l1V-a80WSJdTgLr2_IBeOHMsKpuQ__lkpuEFWPLCP_rTZxZRz5XN3P0oTG-TUzuEbnaKSk1bYKJwAhC-i__8CtNqNg1Kp9KC2JgCYHJ3P4VZ_5lUKlI-loCnkHD8by5dZIMHuj4rpRwECUzG6xfWuS0EM1Lk_bxl979e0xVYoV3vxu9whJINixFzroK-5nOPBzeYTWcULrl6LhXvMwv9-lXriErQQbW2LE457745AA0x1rsbYTWscgsexyeTDakkcvdWniiKLeiyaW55O3VDZU2LfTfmFrcYfL3xeNnw7xmiDMCtnfijzPqXsMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قبلیه بنی مطر یمن علیه آمریکا و اسرائیل اعلان جنگ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131785" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HzhGzfoL_9Wtu1H89HJX2pUbSw7WqPLLAOHA-nzde6LqKMU6F8KP6Kl9fYbTBeJcSdRl1was-27akAN5EwAf2ZYS3hMkLbu9DmhxRzNyo8PI7mzo1RIA1-E6zZx_VijPWa8vlwmcpCs7tT_fiqWQaY78MMrO4JAhawm4C0xlBeI05kDjQrljj_IsP2fkYqouuZvEBTSAFvupykzUDyRoUaVAZ9ZZGdjYKu2b3QK9K4ml6eJvA_-hfyXK5_WNOy0WyZDJ9DUGk2fH2i_0NIRKpzMoxM0T9RvyD_l3kO0iaXA78_xxHCrgLubuKLnMHpnK9I6pimMULhhtHu2brgJ-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ُ
👈
ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131784" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رئیس‌جمهور عراق:عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131783" target="_blank">📅 20:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c668b6cf80.mp4?token=lZ-YbrEUE_vD-zreCp5OLB6aiyyibcs0LVgZjhoLBHljeEkcGue7A9fA7fQPZQMxtmVl7Uk2qU9ygdYxapKh9ZoTUyyp4W1V6J2ATXDDhhVrFhAgCCd59unT3cp34vHIhSfxXPCNtOibIDHNfPdWmzrxuurSIGlDyMiLLOjXB6EeaSPaDHf8qcE-3EcLEgL74sgB-xtN4zagwm3IrZQHJhoQmV2bU5FNh1W8kMGJdjCgOzG2PN4i5JOoltZPQNsXfXWsNCv_RzLphQcoDz9d0SP4ZUts4L1CFWmDA5w0qOLvCRcn6EEPH2ajiMPCvaa_-rJEOAbCizEv7ZLkgUIzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c668b6cf80.mp4?token=lZ-YbrEUE_vD-zreCp5OLB6aiyyibcs0LVgZjhoLBHljeEkcGue7A9fA7fQPZQMxtmVl7Uk2qU9ygdYxapKh9ZoTUyyp4W1V6J2ATXDDhhVrFhAgCCd59unT3cp34vHIhSfxXPCNtOibIDHNfPdWmzrxuurSIGlDyMiLLOjXB6EeaSPaDHf8qcE-3EcLEgL74sgB-xtN4zagwm3IrZQHJhoQmV2bU5FNh1W8kMGJdjCgOzG2PN4i5JOoltZPQNsXfXWsNCv_RzLphQcoDz9d0SP4ZUts4L1CFWmDA5w0qOLvCRcn6EEPH2ajiMPCvaa_-rJEOAbCizEv7ZLkgUIzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت مترو بهشتی تهران: شعار مرگ بر اسراییل
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131782" target="_blank">📅 20:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
به‌دلیل افزایش ازدحام جمعیت، از ساعاتی پیش قطارهای مترو در ایستگاه مصلی توقف نمی‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131781" target="_blank">📅 20:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پزشکیان:
اسرائیل به همه کشورهای منطقه حمله کرد و عامل بی‌ثباتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131780" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سفیر جمهوری اسلامی در چین:  پکن از تسهیلات ویژه‌ ای در تنگه هرمز برخوردار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131779" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcLdwhd1ZO2c0NO0q7QD7faXyaXwNZ1BLMyb75bCbiLSpib0KSI4GcimuVTYB5ZYU-EBZQoXuM_PguQ3ukbjB2iX2UDLSTUaZEMBkOjvz1WEvhHfzKw8Ex459KXUXXQtqt-QF4-s7ydBwRLAY169osFzLCl3M9obHtvSjqvW10Zk-3WVBqVkYOaMxrIeU5cWi7MafW6InMK0jz-ynw-b1UsaH-pZFWoU7Anx1Ju5hX3qa-NgD-0z0G2Uc8k_N6p4HbBmUuGx7fSFM0eR5IkKDOJrf4-LqAqP21XYO8Tnd83v8y-l4QKAUwZePdd1d4C-VfcBkye7-n1XLijiZjOIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا گوشی آیفون علی نعمتی در مراسم استقبال در فرودگاه توسط حامیان حکومت  دزدیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131778" target="_blank">📅 19:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNDZECTpRZWan7hPuzEM8ZiZJ-PAnI7bPgHq-2Jxh4OUDGBNH01CxdO9QC7pPGMDAEjiLutzm8vZSnJE5c648ML_HN6g4s_7uDgtTe-CfIZWTAH3RfsO93FaK7wxozkjQKOMJt_DcGQFvaDcDYPQw8t1rlWFh1iXEnDd9URVJVyf-qKgm2zyV1if3RtfEXo7Z3kBzvF22oHUGG8NZyUxs9moTssvSnRGl82c66ry-iu9N5j_yj7dorQHIEp7H4Nk5INUN-P-NXLzLLUWWXDmAMBfPVZP8vZNvy5Y9ubFw-sA7ldZmV7QELYOhiW-YTnoCE8ntxBVA4asmJ3tHeBeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
مردم برای یه لحظه هم موضوع انتقام خون رهبر شهید انقلاب رو رها نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131777" target="_blank">📅 18:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfMcuHkCA0LsvgURfrpZiIUveH34TzUZik0TQf9PTfle0z659kns7NSqOCT6PziNDr8FnFw5FQZoBzEASyjvhn9RzllW01RoydaGpavRyHsrPoQmXSFbVSkRTvmGzjfvHXSapJ25nxNvm8oErCcufR9Ccra02nenPprqB1laPPzCiSTlM541_K1OQgiDPfNYXgN-4JoqzOm9ndfbXDeQUZi8ji43qp4IwNzHshj5qZS0iZO2EbyB3j0Juql0kxY1M15vyyk9sSqZ_V6rOfid4TOTsHsWJ7B9_XiVvIKIjEe0E8uGKorHxIN_R9ZjzQLtiyruTE4Rr4w-Z4jkrNEGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌ها اعلام کردند که یک فروند بالگرد MH-60S Seahawk نیروی دریایی آمریکا که از ناو هواپیمابر USS George H.W. Bush به پرواز درآمده بود، در روز چهارشنبه در شمال اقیانوس هند سقوط کرده و یک خدمه از چهار خدمه‌ی آن مفقود شده و تا به امروز پیدا نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131776" target="_blank">📅 18:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb289f43ad.mp4?token=er2TBsep6_AsI1tZhcJNPEX5uNzRFy1Zwf2CA0I_wgIk0eviskjpYiItroZ9EcIVP69KLxrFKTzq1gqPlMGpvVQShAh1dhJ-SJezdxl5Qr-D6MXjvThm-rmcXji27xxjaQDaTQYe3yRjh6xJsord0jfBVeAqMK_kjbuVT6mkixf3obcwewH3EfayhXGKzYnjufUsuZqB8wc0URRAoG5wdX3FPcKj7GUkWFwR7rBPW4TwWal14ZXlEb9weY5T6JOEr13AANlnlwl0hvQ0igGkLsCEDAccFfpd6bQeyKNFJ8o8BsQsEwP0ojwXbdidq8BBTws70Nbo6xCEOkxcVPJVMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb289f43ad.mp4?token=er2TBsep6_AsI1tZhcJNPEX5uNzRFy1Zwf2CA0I_wgIk0eviskjpYiItroZ9EcIVP69KLxrFKTzq1gqPlMGpvVQShAh1dhJ-SJezdxl5Qr-D6MXjvThm-rmcXji27xxjaQDaTQYe3yRjh6xJsord0jfBVeAqMK_kjbuVT6mkixf3obcwewH3EfayhXGKzYnjufUsuZqB8wc0URRAoG5wdX3FPcKj7GUkWFwR7rBPW4TwWal14ZXlEb9weY5T6JOEr13AANlnlwl0hvQ0igGkLsCEDAccFfpd6bQeyKNFJ8o8BsQsEwP0ojwXbdidq8BBTws70Nbo6xCEOkxcVPJVMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهباز شریف: موفقیت ترکیه موفقیت پاکستان است.
🔴
پیشرفت پاکستان پیشرفت ترکیه است.
🔴
ما زبان‌های متفاوتی صحبت می‌کنیم و در سرزمین‌های متفاوتی زندگی می‌کنیم، اما نوری که مردم پاکستان و ترکیه را راهنمایی می‌کند، یکی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131775" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
هشت جت تهاجمی A-10C Thunderbolt II که در خدمت وینگ بیست و سوم ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131774" target="_blank">📅 18:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131773">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ارتش روسیه : ما 5 روستا رو تو شرق اوکراین تصرف کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131773" target="_blank">📅 18:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131772">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شریف :  با افتخار می‌گوییم پاکستان و ترکیه، دو قلب در یک روح هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131772" target="_blank">📅 18:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شریف :  با افتخار می‌گوییم پاکستان و ترکیه، دو قلب در یک روح هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131771" target="_blank">📅 18:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131770">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سردار رحیم صفوی:  بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131770" target="_blank">📅 18:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
اردوغان: ما از نزدیک تلاش‌ها برای برهم زدن توافق ایران و آمریکا را زیر نظر داریم/ نباید به اسرائیل اجازه داد دوباره بوی باروت و خون را در منطقه ما بپراکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131769" target="_blank">📅 17:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
اردوغان : وقتی آمریکا و ایران توی اسلام‌آباد به توافق رسیدن
🔴
دنیا نفس راحتی کشید و نگرانی‌ها کمتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131768" target="_blank">📅 17:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131767">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66ce12768.mp4?token=u1rGH4et9PkRumyEzVuKh4AHCboAZbiLqDo6K6u9BbaM2OvJqVGTh7iKjO8f8I_CjMsgsKXV5dHfAPlJ6szwHZxtN5c1gEFDGOoAko4d7aikehzIMa8o9AnOtQs8tSB9R7BUH3chooLipCGepmuLo-ZwFfhrrQzWSw1tnYfvX3Vibyl32mqsp05QuHVf5NC2Rv5bpkSYmJAO9b8lVXc3PVapZXeENseQSzkIL_GMa8vkVA02cTe-KwSEUds5qmSIECUADrbKbemMdCASA3hgvPS8J9RSxYrrS4M4RJQ2vUF2_UYP0_l-3damoAY9UrAY0OlgEpBhxAIyevtR-AwyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66ce12768.mp4?token=u1rGH4et9PkRumyEzVuKh4AHCboAZbiLqDo6K6u9BbaM2OvJqVGTh7iKjO8f8I_CjMsgsKXV5dHfAPlJ6szwHZxtN5c1gEFDGOoAko4d7aikehzIMa8o9AnOtQs8tSB9R7BUH3chooLipCGepmuLo-ZwFfhrrQzWSw1tnYfvX3Vibyl32mqsp05QuHVf5NC2Rv5bpkSYmJAO9b8lVXc3PVapZXeENseQSzkIL_GMa8vkVA02cTe-KwSEUds5qmSIECUADrbKbemMdCASA3hgvPS8J9RSxYrrS4M4RJQ2vUF2_UYP0_l-3damoAY9UrAY0OlgEpBhxAIyevtR-AwyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا کِیر استارمر می‌گوید که نمی‌تواند فاش کند از چه ژل موئی استفاده می‌کند زیرا این یک «راز دولتی بسیار سطح بالا» است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131767" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123544aa58.mp4?token=mh1wdv6TbtzMBnc9IbSwDCpynSiYIZxYEes6-YbYhIXcs87EBADcCGChPxX-wYcmmk5Hh87ohVctvXsL13OO2tyf4eeuXisN6Sud4r9VZpiuWg6tQV2SAlYTLkH3NI7bia9pRHJ-MwOrjEke9_9eOncZQPWd6ZBEYuCV4A428NVCYjj13Vq6LdhRYr_XRgFv2pF1Il0gW0VrmEky8RVxTh6spEx8i1GYviGMBi-6Bks770lvqwE935J6X1adkuDxUB_bRBP7L4LeJXWXdByStvrDZSgeJwv1V7B6XnhBEzE7nC0JSMPJ5tvJLVUW89nFdK_np_3gw09-BoQ7hbMTyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123544aa58.mp4?token=mh1wdv6TbtzMBnc9IbSwDCpynSiYIZxYEes6-YbYhIXcs87EBADcCGChPxX-wYcmmk5Hh87ohVctvXsL13OO2tyf4eeuXisN6Sud4r9VZpiuWg6tQV2SAlYTLkH3NI7bia9pRHJ-MwOrjEke9_9eOncZQPWd6ZBEYuCV4A428NVCYjj13Vq6LdhRYr_XRgFv2pF1Il0gW0VrmEky8RVxTh6spEx8i1GYviGMBi-6Bks770lvqwE935J6X1adkuDxUB_bRBP7L4LeJXWXdByStvrDZSgeJwv1V7B6XnhBEzE7nC0JSMPJ5tvJLVUW89nFdK_np_3gw09-BoQ7hbMTyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جکسون هینکل فعال رسانه‌ای امریکایی در حال توزیع شربت نذری در مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131766" target="_blank">📅 17:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
به گزارش بلومبرگ، سفیر ایران در پکن اعلام کرد چین و دیگر کشورهای دوست هنگام تعیین سطح و نوع هزینه‌های خدمات دریافتی از کشتی‌های عبوری از تنگه هرمز، از «ملاحظات ویژه» برخوردار خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131765" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131764">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ادعای الحدث به نقل از منابع آگاه:
دور جدید مذاکرات آمریکا و ایران در تاریخ ۱۱ ژوئیه [۲۰ تیر] در پاکستان برگزار خواهد شد.
🔴
دور بعدی مذاکرات بر موضوع تحریم‌ها، دارایی‌های مسدودشده ایران و پرونده هسته‌ای متمرکز خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131764" target="_blank">📅 17:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAMxTg3ljJiV4Pimu9fNAovRlAzYeUV7dHS57gyZC27kHmIwQKV1AaAmB0Dp_buU6lnQX6hSdbPtnBqQnnF2RjSf_PQwjXdgrpbhXdHKdgeMUDIR79ycA9SNsIPDM4SfJkgOuCJPuKgMZitFIc8VaipX53tfC5qRhv1zQBoDVUkpVe3HLze6htUrwcnRr8IZJ2XkHbSRbteBtzdhKE6GihcS_LTaRVtwbAs5qBCEj9aGLXef3HmVVmUIWiqbPfYwXtX-4sZ4g6wocJw59AHmF0JxVbAHqUDrghXPkdPtRrBxZ8TEN0m3lvko73x8nRmBaNALmCYpnRxQS703T26IJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز مستقیم هواپیمای باری 17-C نیروی هوایی ایالات متحده از پایگاه هوایی نواتیم به پایگاه هوایی الظفره امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131763" target="_blank">📅 17:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=t7i-gIjMtw14b0qCUWMqQkXg__dgyNj3q09cR2HC6idbMmk96kmT0PoLxQ0ZZkuZMDDkMT4cZHslz1cfl72csxVoL3ceCPuRThHkrfY9Ma3hAwpOzP60Eor8Gyzt4cS2wCIeB6aMMTWB1gA1mC-VxY-xVMGrX35LMJx8IjJzIv4W-O_vVs3vCK4WIHaRadth8x8GPfE4OXiyT4XFEVMgrN2q9rOKYDnR8sK_dwzX9E8-IuQMic9iGd0OcLEqGy5eBIKufeKS2K6sAhHwmfxB-QWR2f0ZilM51OXvzhL8HbMPY4Yc5COvdEY-SNV2xDfkuNOkZLB3aKjv-ym_2cmNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ec205bc1.mp4?token=t7i-gIjMtw14b0qCUWMqQkXg__dgyNj3q09cR2HC6idbMmk96kmT0PoLxQ0ZZkuZMDDkMT4cZHslz1cfl72csxVoL3ceCPuRThHkrfY9Ma3hAwpOzP60Eor8Gyzt4cS2wCIeB6aMMTWB1gA1mC-VxY-xVMGrX35LMJx8IjJzIv4W-O_vVs3vCK4WIHaRadth8x8GPfE4OXiyT4XFEVMgrN2q9rOKYDnR8sK_dwzX9E8-IuQMic9iGd0OcLEqGy5eBIKufeKS2K6sAhHwmfxB-QWR2f0ZilM51OXvzhL8HbMPY4Yc5COvdEY-SNV2xDfkuNOkZLB3aKjv-ym_2cmNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز : هم‌زمان با مراسم تشییع رهبر جمهوری اسلامی در ایران ، آمریکا جشن دویست‌وپنجاهمین سالگرد استقلالش را برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/131762" target="_blank">📅 17:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
به گزارش فارن‌پالیسی، هند و ایالات متحده ممکن است در برخی اولویت‌ها اختلاف‌نظر داشته باشند، اما رقابت جداگانه هر دو کشور با چین همچنان به اندازه‌ای جدی است که همکاری راهبردی بلندمدت میان دهلی‌نو و واشنگتن را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131761" target="_blank">📅 16:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
کامران غضنفری نماینده مجلس: پول دادن به مداحان که دیگر در تجمعات شبانه حاضر نشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131760" target="_blank">📅 16:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
روزنامه تلگراف گزارش می‌دهد که یک ابرقایق ۱۳۳ میلیون دلاری که گمان می‌رود به ولادیمیر پوتین، رئیس جمهور روسیه، مرتبط باشد، به سمت بندر مورمانسک در قطب شمال در حرکت است تا خطر حملات پهپادی اوکراین را کاهش دهد.
🔴
این کشتی ۸۲ متری گریسفول توسط ناوشکن روسی سورومورسک و کشتی گشتی وووودا اسکورت می‌شود، در حالی که ناتو کاروان را زیر نظر دارد.
🔴
از این قایق تفریحی در حالی که تورهای ضد پهپاد عرشه آن را پوشانده‌اند، عکس گرفته شده و پس از ورود به دریای شمال، سیستم شناسایی خودکار آن خاموش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131759" target="_blank">📅 16:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نخست‌وزیر و وزیر امور خارجه قطر، محمد بن عبدالرحمن آل ثانی، با وزیر امور خارجه سوریه، اسعد الشیبانی، در دوحه دیدار کرد تا درباره همکاری‌های دوجانبه و آخرین تحولات در سوریه گفتگو کنند.
🔴
در این دیدار، آل ثانی مجدداً بر حمایت قطر از وحدت، حاکمیت و تلاش‌های بازسازی سوریه تأکید کرد و بر حمایت دوحه از آرمان‌های مردم سوریه برای ثبات، ایجاد دولت و بهبودی بلندمدت تاکید نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131758" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نشریه نظامی «میلیتاری واچ»: کارخانه هواپیماسازی روسیه تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط ایران را به پایان رسانده
🔴
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
🔴
احتمال دارد نخستین سوخو-۳۵ها از سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131757" target="_blank">📅 16:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01db34aaaf.mp4?token=mMB6DrWj9vStZwRx6UKGgeHifAUw0aIDws3m9D9BBsCKEBVnrBT6jKLXHAyds_wyWCgojsId2-vuUMK0VII1lEV3gIEoHccKrgNYTQyRgVqcy-CmWKodZz7chCdrnX26wHbBfburcko0RSHIdvGbM0Q8hKoZM-iHWkSrmiEvlgUcC3ATWFk0y50kBrjWYlDbS-wagHRU_00qpJUb4WckVmRFyWcTcj37YnxqMhdrZIIukOZM7flGdhURlMASTXxjA5Fa9fyl4S75eQNAK25Hupu-GThX6o9eZFsq-Cangsy0_HMqL8S1b5EnaMir3B0YkLrlgtC92jlPJ2sZ6f_Emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01db34aaaf.mp4?token=mMB6DrWj9vStZwRx6UKGgeHifAUw0aIDws3m9D9BBsCKEBVnrBT6jKLXHAyds_wyWCgojsId2-vuUMK0VII1lEV3gIEoHccKrgNYTQyRgVqcy-CmWKodZz7chCdrnX26wHbBfburcko0RSHIdvGbM0Q8hKoZM-iHWkSrmiEvlgUcC3ATWFk0y50kBrjWYlDbS-wagHRU_00qpJUb4WckVmRFyWcTcj37YnxqMhdrZIIukOZM7flGdhURlMASTXxjA5Fa9fyl4S75eQNAK25Hupu-GThX6o9eZFsq-Cangsy0_HMqL8S1b5EnaMir3B0YkLrlgtC92jlPJ2sZ6f_Emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای روسی مستقر در آفریقا، امروز صبح حملات هوایی را بر علیه مواضع گروه‌های FLA-JNIM در شهرهای آنفیس، گائو و سِوارِه انجام دادند.
🔴
همچنین، یک اردوگاه کوچ‌نشینان توارگ در منطقه زارحو، واقع در استان تیمبوکتو، مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131756" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnyGjFLIrQtjO3dCqTfJ6lqyYbLL4HeTUBJJL1OwXFFRMxNejPBFotVcFdYBUYG-P6uHsGvdsoDY9YVogOt8xIlrI7HR1Cm02dorSISuGhgfYJCN6tQySimIafnsFuDHsocdajpGkssAeFnYMSeYaLVNRxjey84KY60PY10hAuiofWgg-y4AWsps3pwqCknGI5JQSRekyWMJKtcePccfjUORs994ESy0vcD2vdh9031in8jFoV17QuZh0bQj3lh7GPw-e_AfuSXyhN5TWwmoQMruZV1d5QWkfYShFjxOF6WJ73_Svtd5qGQHXE8-Y6bQJgtc92-APPpToQD_YaSeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی در ایران به اعدام محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/131755" target="_blank">📅 16:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری/فردا یکشنبه سراسر کشور تعطیل رسمی اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131754" target="_blank">📅 16:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEeYAv3jaybW74tXD31W9yPTZbg-0MYip1f_8tSH7mbIl_vbG8RtQ3RX-0s41WkCZLQC4Can5mo0_aPvRR8hnLFiKLVPLts_1lWYlWGE7yVBfzX99CuteKB-yKuc2xqptfQ_F3tANio8btiPJZ8I_ZmaLgdRuzsOFURScrIPMOUJ9MB6_VMiVS8uI974GtmLgcRYYtswv0tWe7H-iRTH1O73MGbO2AeRu2nVyWMojM88dRyT4lHaJm5aRm9Kfxe-AoN53_7FwGFia4hUkJCdGL_OGGFteWFoThF3hFVncw5KSHRnVMz1TyJYLb7IwnDzFnHQ-qqVMhayvCGxVJLF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار عظمایی به عنوان فرمانده نیروی دریایی سپاه معرفی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/131753" target="_blank">📅 16:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9286675b.mp4?token=OTYhk9wAM3xSI0cL9hbJ5NQR8GJxmMzuO2F46HVsEF_elfQIzGDBblYznMjHsNn0ZS080PiSBDsKEZMVKjsh3YG1qk9-_RnBQ0A6jeBklBkN_DYbkzgFDFE_utqIkgWUTIJJGYvAGDeUvoD_juK6175bo1SCKH0U03ARXFdggr5ve5nWOuL6mxYMzps833tD2QVLrbrz14DBqX2u4Pwx4WRIIcH7zNKzzUakMxXRgV4UH7bihy7nGImztPg2Duh_dN2THSC6VfIhKd6UYHpgfMOUsEnm1_u3jAv_LohWgAS567Ux5KcxRPszTSzeBGsBf2qS0qNF4vRES7-9EjKj9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9286675b.mp4?token=OTYhk9wAM3xSI0cL9hbJ5NQR8GJxmMzuO2F46HVsEF_elfQIzGDBblYznMjHsNn0ZS080PiSBDsKEZMVKjsh3YG1qk9-_RnBQ0A6jeBklBkN_DYbkzgFDFE_utqIkgWUTIJJGYvAGDeUvoD_juK6175bo1SCKH0U03ARXFdggr5ve5nWOuL6mxYMzps833tD2QVLrbrz14DBqX2u4Pwx4WRIIcH7zNKzzUakMxXRgV4UH7bihy7nGImztPg2Duh_dN2THSC6VfIhKd6UYHpgfMOUsEnm1_u3jAv_LohWgAS567Ux5KcxRPszTSzeBGsBf2qS0qNF4vRES7-9EjKj9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهرک‌نشینان اسرائیلی، دسترسی فلسطینی‌های محلی به زمین‌هایشان را در نزدیکی شهر سنجیل، در مرکز کرانه باختری اشغالی، با مسدود کردن یک جاده، مختل می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131752" target="_blank">📅 15:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
آگهی دبیرخانه شورای عالی مناطق آزاد تجاری: انجام هرگونه پیش‌فروش خودروهای وارداتی در مناطق آزاد ممنوع گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131751" target="_blank">📅 15:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر خارجه مصر: از تسهیل مذاکرات ایران و آمریکا حمایت می‌کنیم
🔴
باید آتش‌بس در لبنان اجرا شود و اسرائیل به طور کامل عقب‌نشینی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131750" target="_blank">📅 15:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003c393383.mp4?token=ThiCPKmUsB_bseQ4cOXWU52g_E7s-eLTkqfi0hDUK5Yz042qMkYaMZ7rxEJY-cq09NgkOjHKtUlrPXryz4LhEo0K1KJc522uEJ7Bwaq-NlMyjZOjlXMlVlLXBm1BrEbsIrIb19Awqd4QdqOl_bTvlzLEwGSqu0lWBuoPbuueFdo-7k_66zHqafbqqenD9dqHc2PeeUk_JBUO4iBSQuPUZKZoGZAbnlFoswRL5kVpS23aqIeYJjhAqpCnJnEJ5uofs6u8lmp3dhnfKHHQVhkFJeS1OacpRY4I7AHHUnQ37BG7cSA_icnBYhhnpzSSEkLvvJv94xKHGbesD0oZAycqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003c393383.mp4?token=ThiCPKmUsB_bseQ4cOXWU52g_E7s-eLTkqfi0hDUK5Yz042qMkYaMZ7rxEJY-cq09NgkOjHKtUlrPXryz4LhEo0K1KJc522uEJ7Bwaq-NlMyjZOjlXMlVlLXBm1BrEbsIrIb19Awqd4QdqOl_bTvlzLEwGSqu0lWBuoPbuueFdo-7k_66zHqafbqqenD9dqHc2PeeUk_JBUO4iBSQuPUZKZoGZAbnlFoswRL5kVpS23aqIeYJjhAqpCnJnEJ5uofs6u8lmp3dhnfKHHQVhkFJeS1OacpRY4I7AHHUnQ37BG7cSA_icnBYhhnpzSSEkLvvJv94xKHGbesD0oZAycqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه‌های بزرگ وابسته به سازمان FLA-JNIM وارد شهر آنفیس در شمال مالی شده‌اند.
🔴
تعداد زیادی از نیروهای ارتش مالی (FAMa) کشته یا اسیر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131747" target="_blank">📅 15:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b402cee7.mp4?token=aiK9IimPrRXaSbJdplw1G0OvVseKO8bgHcbR3y1zajWyZKg8u2BvYvDonDafDvTd-eBxT0b9Pl1DTzFPlsIEy5hHYdGPgEhwfDsGNhKsUHl4899dVfibAZ3giI-nogspzvTiKxPMyRuYbmnVdBBR7xybVTyRj-Ntp7B4jrnHzIvLW-ew2Us_tpQZXt9nyfoYKuhtD6b-dqZX6Ti2qYzZtpSRjEbs4U9_YlBoAxzVZ1IdIaqvEqDdmX0pm2Haxi2_CBqC-CXYrKJen8QaQURboAQf_2n7OPftdwXfdwiYAPETrMhPg9L2ktDSMcH4h00qlMizAzPPDOXzzeBm6SSnuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b402cee7.mp4?token=aiK9IimPrRXaSbJdplw1G0OvVseKO8bgHcbR3y1zajWyZKg8u2BvYvDonDafDvTd-eBxT0b9Pl1DTzFPlsIEy5hHYdGPgEhwfDsGNhKsUHl4899dVfibAZ3giI-nogspzvTiKxPMyRuYbmnVdBBR7xybVTyRj-Ntp7B4jrnHzIvLW-ew2Us_tpQZXt9nyfoYKuhtD6b-dqZX6Ti2qYzZtpSRjEbs4U9_YlBoAxzVZ1IdIaqvEqDdmX0pm2Haxi2_CBqC-CXYrKJen8QaQURboAQf_2n7OPftdwXfdwiYAPETrMhPg9L2ktDSMcH4h00qlMizAzPPDOXzzeBm6SSnuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار نمایندگان جنبش امل لبنان  با سید عباس عراقچی وزیر امور خارجه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131746" target="_blank">📅 15:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی: پزشکیان به مجتبی خامنه‌ای اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
🔴
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی خامنه‌ای با یادداشت تفاهم موافقت کند.
🔴
دکتر پزشکیان، قبل از امضای توافق، به آیت‌الله سید مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/131745" target="_blank">📅 15:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گزارش ها از پرواز گسترده و غیر عادی پهپاد های اسرائیلی بر فراز بیروت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/131744" target="_blank">📅 15:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
تصویر بسیار منشوری و زننده دیگری را همسر سپهر حیدری در اونلی فنز منتشر کرده!!! که به شدت وایرال شده
◀️
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131743" target="_blank">📅 15:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExExf5wgG1ZIKVFENfFTbU7QhMQ4Jk0TjufhtCwJg4XeJeLU9OgCLzfyRQ2RrcvAtFOOGbELcf3rr4kiSIrKW5u69VlWHmJelp92enKRMI7oMuD5bPPcZsSU4DKpV82mqCEeoL94NTOubLCROY37mjrWU5tFtQ_g1vKPBIK8enEsw3Pvsgt7JOaatKIMLWgppqcNHRtgdLAcyKpbK_-Oa73PHo9oLlyeHBJ7Bk9dF4ydHts8lmIsvVfxLKeqGxNCnpHEgBybyj9RJcsy8CHHPaLX2ldfd8c7SLTnhLhHEDxlSsZLW5Yi3JzjhXXIb8IS7ysvw1LhwXho80i-InMWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خلاصه‌ای از کیفرخواست رضا پهلوی که توسط خبرگزاری تسنیم منتشر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131742" target="_blank">📅 14:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رئیس‌جمهور عراق: عراق نه با ایران در برابر آمریکا متحد است، نه با آمریکا در برابر ایران
🔴
روابط خود را صرفاً بر اساس منافع ملی تعیین می‌کنیم
🔴
پرونده گروه‌های ضد انقلاب بر اساس توافق با تهران، حل‌ می‌شود
🔴
امنیت خلیج فارس، ما و منطقه به هم گره خورده
🔴
تلاش داریم تا بهترین روابط استراتژیک با عربستان برقرار شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131740" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131738">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L1ryTqlblK_OQqCBlndb4ygSFFZDA28oKalpeFT7CMD8GqPYoGLRwDUtvB8TznWdPwQsoZcD1rz86xTVIN4QBw1HcfmYo-a2Xnleiees68lOdd1CxLLSbm87j4OGjtYtjtIGbzpVN2hRrUzPNg46o1lC9KGQQD2ozYJu7xWbwKdZDWDl0DwGk1mtnEuvoqx3122Qnqmo8ByvzyeRgGOPu-rLSb7Ecur4WJvasaEedNhmxH34n-hFgsUvzmvTK0gwmRO7ymiHsNzmywprFKdBtxifUQPhoOCRTUSBwGS6sDQgxvebYi0ME3RDfGeMON02n1Of4VW5W4kzXEr1hj9DhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dc1Ur6ar189nIAwBWuRnN-PgJeLbcEKqznTn3nvWbNaXnasPS3NOItRy1JfhR9H-TTsRt6hHjRw6ENBhNXyBfoOJw5qFCFYc979x64aZxus2kCL86wcZsn68TyAteblTaNn02p5IWDGotShGtvKa9LL48iRBiLW5Q6QcwGA5yOl_CCVaFb0OzFQfBg8YtH245GAWjsiglUoHonoJml-ujQK57UI1ow1U-d9nRTqwf_6BjPYsy5k62t0b4qJ3dLntRfoltnxBJJGK2Ii42dN-h4DHG95n9nXrC9BXZz5vftcRfGFB5UYvEsm9dOHq9HPG24EfP7pE3Bhv-m7gUsVMXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا یک بالن نظارتی (الکترواپتیکی) یا مخابراتی در آسمان تهران مستقر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131738" target="_blank">📅 14:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131737">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
به گزارش اسکای‌نیوز، گروهی فراحزبی متشکل از ۷۱ نماینده و عضو مجلس اعیان بریتانیا از دولت این کشور خواسته‌اند بنیامین نتانیاهو و یاریو لوین را به اتهام نظارت بر سوءاستفاده و شکنجه سیستماتیک بازداشت‌شدگان فلسطینی تحریم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131737" target="_blank">📅 14:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131736">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ : کمونیسم یعنی مرگ، استبداد و دنبال کردن شرارت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131736" target="_blank">📅 14:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131735">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پیام پوتین به ترامپ: مطمئن هستم که روابط برابر بین مسکو و واشنگتن، به نفع کل جامعه جهانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131735" target="_blank">📅 14:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131734">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
به گزارش بلومبرگ، امانوئل مولین، عضو شورای حکام بانک مرکزی اروپا، اعلام کرد این بانک پس از افزایش نرخ بهره در ماه گذشته و انتشار داده‌هایی که از کاهش تورم همزمان با افت قیمت نفت حکایت دارد، در «وضعیت خوبی» قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/131734" target="_blank">📅 14:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131733">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است؟
🔴
مقام‌های ترک و اسرائیلی سال‌هاست که علیه یکدیگر تهدید و توهین نثار می‌کنند. از زمان آغاز جنگ اسرائیل در غزه در سال ۲۰۲۳، این جنگ لفظی تلخ‌تر هم شده است. اما حالا به نظر می‌رسد اوضاع دارد از کنترل خارج می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131733" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131732">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvl4Zg_KiCNbbcGtrjWyFOBtNOOUtlXYvYzI_PG1KWAE3VL6Q_opmdL-utmLmrZCTCgq6XE3326WwnpmoB0isg8IhODpPYpif8nwRALbFAXoL5uVSmaSMFFfxAcjKWNOc32rV1c2zy-lu8JgTU3solrWYvG8YioIbJTPMto9iqy9pRSMcZbz2dwuiSJOUsSRzwytUgAv9t8vRA2kzPgJ5Cqekc2eWL_8pTDSWC4Qbj5U7KdXlzy9NOBdIKYIsbCSPvKt8IdwZp5GP2L5Av2mz_LRZs_Se_kiWNf0en6_2T188F6w4QOKlnZ2ee6JQ4veR2eVnX5JfHlDY6ECzKCEnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار سی ان ان در مصلی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131732" target="_blank">📅 14:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131731">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW7igi91Yv7OjMWQ0gxWMwF5PRBt3WPhDbS284uee58ySRgVsDMmXYxW1HIaVzGKCooW7beosmetEDXEElC4zSpVriWNfijj2EKzXNmC6EoXSY08bMwrBaqigSsjP_qpU4cEkyKc-s5ps6IH8LjGBwt5zBJ6iAZzduxS5xJMmbzYVWevVoLsnEvKCfCEly7-pIeEt7A8qjLc1IEQ26RmSC_g2Wk3GFmXXlTpxdTy5zWDLHKe4i0OOc0-RGRvwXHs5DqT0HSsKF-PUTgoDxvjXIwfeoxnRSHcSfoQcABQ4KPsIFUasEL_vWnGUeYhJrOSEehgjcxM3vibvPaFBBm87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131731" target="_blank">📅 14:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131730">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر سقوط یک هواپیمای جنگی متعلق به ارتش روسیه به دلیل آتش زمین در شهر گائو در مالی منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131730" target="_blank">📅 14:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131729">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
به گزارش بلومبرگ، پاتریک پویان، مدیرعامل توتال‌انرژیز، اعلام کرد تولیدکنندگان نفت خاورمیانه به‌دنبال فروش نفت خام ذخیره‌شده در جریان درگیری‌های خلیج فارس هستند؛ با این حال نگرانی‌های حمل‌ونقل همچنان بر موجودی بنزین و گازوئیل فشار وارد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131729" target="_blank">📅 13:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131728">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مهران رجبی : حسرتی که پس از دیدار با رهبر به دلم ماند این بود که نتوانستم پایش را ببوسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131728" target="_blank">📅 13:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131727">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی : تاکنون هیچ حادثه‌ای در مراسم وداع گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131727" target="_blank">📅 13:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131726">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktDE9xb-JZ8SCeUO__KRQ7bHqKHVLMAZ9yjVr1OWiqd3YGh3uQlzHdH55qKMYrIAwGJNsxYJ_S1CrCwtrkpZiD3AXfFvhfKvUbgfFgRw6vwyJOrWb4SQ_srqsPR78hJ22N3KFOEBf5z2yR8RM0xS15Jtf7HSySQo1vZDuBw31NcYSHdBJLI_oGxs7_H0muFbxA-IU9j742jR9mYn-zUrQWagmqxw25akwqWi6n2tXJNu_DXhaZjTLn32qctyKwvl6OZy7kf8ho4Kx4MgBE-940Xy6_XQp50Gxcrj_ZpDCfJXlZk1ZsghGpLEQ2Re8_TkEJ5QnpYDZawqqrJVm7PeFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز روز استقلال کشور ایالات متحده آمریکا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/131726" target="_blank">📅 13:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131725">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaidKMsfW78AHH7LoB7D0TrORvC36vJgy98ezOb4OdkQGOLIGZd2bnFLcU2YxTIpyeFyerxz061IMsEhJYwx0mWfQCF8ycB2NhcaeKB_j8jj9t7Y6uf2hygvlvcOfZLw-M4rbePlV4ShDCv-IR9EOZot5lJQzsIqhZ2mc6MywVmc5_51LNe17FNr4dHOSedhGOy_0Xo4Wcg4hP-paNLlgDQHVr_JeS9fzoP6nPDxjS7SLBdfCR_Cr4hUJlkiVbrJY_shBu_cU9q2IJZHOBw3yw720K2j2ns9lLb-7KqRPDSzdvlX1VUJopSSH5cEeO7fqxe-uQxAMHbi7ZqfDAdoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب/برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131725" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131724">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
میشل عون در پیامی به ترامپ : از شما می‌خواهیم که همچنان در کنار آرمان‌های عادلانه لبنان و نهادهای آن بایستید تا بتوانیم فصل جدیدی از امید و صلح را آغاز کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131724" target="_blank">📅 13:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131723">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ:هیچ کشوری به اندازه ایالات متحده آمریکا، خیر بیشتری برای این دنیا انجام نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131723" target="_blank">📅 12:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131722">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
آلمان انتقاد ترامپ درباره صرف هزینه‌های نظامی کم در ناتو را رد کرد
🔴
فریدریش مرتس صدراعظم آلمان، انتقادات تند دونالد ترامپ رئیس‌جمهور آمریکا، در مورد کمک‌های ناچیز آلمان به ناتو را رد کرد.
🔴
وی پس از دیدار با سران کشورهای حوزه بالتیک در برلین گفت: آلمان در حال حاضر بودجه دفاعی خود را ظرف چهار سال دو برابر می‌کند. این بزرگترین تلاشی است که ما تاکنون برای تقویت قابلیت‌های دفاعی خود انجام داده‌ایم. بنابراین، چیزی برای پنهان کردن از کسی نداریم.
🔴
وی افزود که این موضوع را با کمال فروتنی در اجلاس آنکارا در روزهای ۷ و ۸ ژوئیه ابراز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/131722" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131718">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBhwZcfky0sjKtZI6FnbsFW-wsiOqAp95FFvAUMzGkAYEmDIaon9r9mypwG-W6H55dLn7IdYeJ4tZWPtbzqScEQYBaflBPblb0ahfwPoI11dkBwls5uSfx3h7rmb9VJmELHKI9lwTmB5NCTY2cwXfCePaQbDjlgOUH9FRgzMAOGqo1NaC2tcvQx_A_ktzqhYYrJImPl38oo4emBSHg7UB7xBS7eRZj2RCOeXTWz4GzFrBxxavGfHeplwiaKzhrximnKTIfo2w4zRvTtF2jitOAyTHknmsst24KGtm61Edx5_hhDyPnejIYQaudBr4nHivJBlcSdtdtHd2XANAyUEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atoXGr6uLVOpZhb8laFE-2q8HVdVhYlpduKNsUuFbBBTaouNHx_t-MUK8CUl9KR7MbJ80spXKhx6SN62HLUYt15Fp9EIKWIsv0M8W5qNo9DOYpqxRYz-faLjofysBm4nGk-VRFDsveEcZz1992-FC5y0cQqr_gT-M9tw0c49JLhb50Xiz8VH1V38EWLrmz3CB68UXcF23vKfpG-WwKn-zNR8G3CsDFZ5PfkbbhUOykFvdgbw2Rftwz1m9MEsZG-XMS5iOcf6UGloZ7estZHUW4jLg3DDom8DylGIVdnZYEMSleaxMsiFOwtc4Y5eOHHl0KNF472qSOYCHdAirEEkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMshWpWjNwvfhzBrGGh6RgktpwJqtTuIBM20bh2jX87ZurZuVcACgsgJ8Mnf_fSlojbAFudpXMpz9pXk7oMivavKLk8L6VA-0NjFLvik93ri_odl4bYCYGmfnGSyvlPKft3P2fK0IYCKpb5FF1aCcv81S_SHwRJrZcM6r3hT9TYnoiIB7Ldjm3cE2P-Nssilp5P5O93dvSwZmGfKJuWoGLnnNhNaF8YvN6f512-CpHUDYLgaXqngNuFw7DmGvSp6u5WF4tOmciqE_7nsVQctMy0-EMjWuztZkWBnxuaznH9yx60rm4vrpWaAU4hTGw0dt8Yh27YvVgzwKN97pnZ4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OK_FKRwEWNIurva0juGRbp41E4BR3z3U4JwseGbnDNbKbB3sC90PPOhP4JWGFosAlU_5GnuceO4WbKevKvnUQ6TanhNyaradMJsaWQkyKZZGpt3toN1m53AUf1mspDnM4M1PfT7cm4s409QAm4omRWRbxPRdNXiC_BnYODRqtpmnYp-62ozajo_N7U9yIkPQZJeKJY6miD6u8su_IBHrN77zoOByr96im4hZVpauaro5fhG8Ko9ti3V0f8Ot7odbjlX2H-6oQNuN-_v6wUCYcuGRu3ngvI7iq--HdsaYGHA6kslFm2IDOyp-dO6hAILLGMs8lbTWo3-t9xgVe-UiZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
به‌روزرسانی (تنگه هرمز): چندین کشتی به‌طور ناگهانی در حال تغییر مسیر از کریدور عمانیِ تحت کنترل آمریکا به کریدور تعیین‌شده از سوی ایران هستند، یا حتی دور زده و بازمی‌گردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131718" target="_blank">📅 12:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131717">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
منابع لبنانی از حملهٔ پهپادی اسرائیل به اطراف شهرک «صدیقین» در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131717" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131716">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی: به سایت‌های هسته‌ای ایران باید دسترسی داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131716" target="_blank">📅 12:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131715">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
زلنسکی: زیرساخت‌های نفتی روسیه در نزدیکی سن‌پترزبورگ را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131715" target="_blank">📅 12:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131714">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFgUKmyEfqvy47gJBCYJOlhdTj-YPEX9bD8CEk-pP7Bx3XUPs6ugom1VIVNAnbrLFV26_EpPBo9whYX-upUIQGYAdCXELRsWzLVTXQh8sNwDxLpp6PvdVF05DZ07WBryecy3OHa-0uXJqLxcs1V9qTqtU-AG5hSeE411QfXTwzWU0dTa_xCZKpSmIDRVOx3An9bdmyPp_O0ev5DnDM4Hx3ZhL0w8OYEG-SshLyjPF6okTTUZmwOt5Q9CtrdaMQJAh6l7LAU_tyxrhhYzGhV7yblYyJDfivyDfVOHo1kxw70QaLJyxpTnY2igiVC7AfQQlnGWOjLrOWvzeTYM8nfUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌ پهپادی گسترده اوکراینی ها به یک پایانه نفتی در سن پترزبورگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131714" target="_blank">📅 12:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131713">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
تولید نفت اوپک با بازگشایی تنگه هرمز و ازسرگیری صادرات تولیدکنندگان خلیج فارس افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/131713" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131712">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT_7sP9s7oft1tqIBoccBx_g8NajYb3CEcuh9JwXMEnKXEet6_JWHqvmjNuD2DeX9-JUlnh3DVTm9E3TPQFggmw4ilWgcr4q6YHloV6Ho5JOBjZ9wyH-0_Stf1BE8KYCzB03wW1G9RjyA6BNqPUBA409Zo2Ru003wCWM6Ernp9k9OMPuuDORkRp7dd82ZeIpf8_4XCCd-YG_4QTB0N1taJ4Z6XHQy1usycnYWkwbgIfvO6yhqR24mAUwO3hfX-dauOwf0cmmhFDEbvestf5Vq87s78N0Zrgk4cqGcmIudoF6MWaQxJmtI1qaVAaxa8xSCWT9DsCQypbVhSe57123Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: به گفته سه نفر که از موضوع مطلع هستند، مجتبی خامنه‌ای در حمله‌ای که منجر به کشته شدن پدرش در آغاز جنگ شد، جراحات شدیدی متحمل شد، از جمله سوختگی در صورت و بدن و زخم‌هایی که نیاز به چندین عمل جراحی روی یکی از پاهایش داشته است.
🔴
انتظار نمی‌رود که او در مراسم تشییع جنازه پدرش شرکت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/131712" target="_blank">📅 11:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131711">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YegtIU4SQaTTUrDWgLCwcNs1Z9fnvGGePvg0P3h4Uc6xpAqTHPlj_cwvN7aFtCDN4jXUTcbDOK83rliI8tBcoK9GXMF8aEppcsGwSLI5KsMNTDDb2Q7wKqqWCwCZ4yfF-MiskHxEMrqPknpSjLrRKIGncU9DtPtPNydvVJEgY2_DTXOIqvDsyX5zREOAqqoBFChxezXmAPlVpQw22jhBi8uc-MrnGKJdH8RDRkPWxuDiLfScLEI0ii4AYUfb6Ts7-BVZEfZDigmVO7V1Mq5HmspnLYhkOhxE6lcNpy0QbOz136xHivDw599895-9fSJxAFpnBckp4UqspRmDXR_kIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک
کاربر اسراییلی:همه کشورهایی که در طول جنگ توسط ایران مورد حمله قرار گرفتند، در مراسم شرکت کردند؟
🔴
چه آدم‌های بی‌اراده و بی عرضه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131711" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131710">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
محمدباقر قالیباف در دیدار با رئیس پارلمان عراق: درباره مدیریت تنگه هرمز موضوعات مهمی در تفاهم اخیر با آمریکا به امضا رسیده است و بر اساس قوانین بین‌المللی، اداره تنگه هرمز باید میان دو کشور ساحلی ایران و عمان انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131710" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131709">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
انفجارهای کنترل شده برای امحای مهمات عمل نکرده، امروز در جنوب اصفهان (ارتفاعات صفه و بهارستان) انجام میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131709" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131708">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcUHQRRTiBhdj2T254XP4V0kQC5UlIAt8V-1xG5Rl95tC0ZfJcQP0LMoWb8v80gldMKi8PSbXu9skqaEF3mcD_Bf6qDIwhcxNxuRqdqGDqhFbqbqKGl_HOnOhBdJb0oHhQMFqsoznsbpV8Ac6BGzy0bVZDstUgrc5JzZluI_Cb2kwrESrAIACRpDOy0rCkzwMmR2U2wEGIzoP42UfTGt8PdhaDrPrHS8vh8mfxe3Yjt3qyGizzL6iwx86IPG1kNJe_a6YGiQqLDiGmtmMdl9aT8texELI0Bo8ZoGM5PPc8AhFFjYXbcCFiTv3JYNFB6coKGUaVjp0DROfAswbvn0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده در رویترز از مراسم امروز در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/131708" target="_blank">📅 11:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131707">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مدودف: تنگه هرمز اکنون برای ایران به سلاحی تبدیل شده است که از نظر اهمیت دست‌کمی از سلاح‌های هسته‌ای ندارد؛ اما یک «سلاح هسته‌ایِ» دیگر نیز وجود دارد و آن تنگه باب‌المندب است.
🔴
روسیه، ایران، چین و دیگر کشورها می‌توانند درباره ایجاد یک پلتفرم مشترک برای کشورهای تحت تحریم به‌منظور مقابله با محدودیت‌ها و تحریم‌ها گفت‌وگو و رایزنی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131707" target="_blank">📅 11:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131706">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ارتش اوکراین کنترل شهر کوستیانتینیفکا در شرق این کشور توسط روسیه را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/131706" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131705">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131705" target="_blank">📅 10:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131704">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فرانس۲۴: عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند
🔴
از آنجا که‌ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد
🔴
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود
﻿﻿﻿﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/131704" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131703">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jibm6AKMkcBHr0FvnKFVNIDlyHiGlKOdP3FeU6h4KoK1MVQTGYixLqhdkyqwpAVBZ9NOlEX8Hsk5Tla_2kjGKdV4A4Vvm7RURRqJFwLwlZKkGnrqzo2Gh1-uYs5_XDNgB5zgFGL8SIHvAtFB5WmNF487Orrh5rW4dJSiihoEY78aQOZ4ztVTBY9NqrcdiSF2m1utKn_FT7X0voVouunqiuPUH9WyvscuFKtGN2goX099UdEeU8E0SR7vrYalFmkeP4EbU_7dX6voxUGVxS4s9_iUH9WOt9WxJCUOX8dRZg33nsiBZZVrH2VR_RVcklHgVTtREeUIfBsi32NbURpCqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت سنگین نیروی هوایی آمریکا در خلیج فارس
🔴
نیروی هوایی آمریکا در حال اسکورت کشتی‌ها در آب‌های عمان و جمع‌آوری اطلاعات درباره جنوب ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/131703" target="_blank">📅 10:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
🔴
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131702" target="_blank">📅 10:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sllrHklJm5qeiEEIQ5Bw_A-27_OkvkxiQNwKL_PfxNoVvhQMHWXU93Upq461ZkGKAmnvo6zBRZQjALo0H3pHDd2i4vJqb-3I_mcMHeFfuQ-sZxLaZ_5fSh_4Z8sGdLaQmTH0xRHQpJAj53shKTxKU2vrHOwvRXEbGYjjhz5erhNve8s6SNCcErajT_p85JfBO23xQKRnSgJHki5FaHpddeTOggGaLJrzsMRzUxl_9_As8MQV8tOM4zupuMaVLv3o8lkRLXgHFjSosm0Ilr23kVUc_yWdnBwK4hD6El1CydKVmEr_1lNkVMRThfwtlGPRAmW2wuu8U5e49EoGXKkxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار غریب آبادی نسبت به هر حرکت نظامی در تنگه هرمز
🔴
معاون وزیر امور خارجه در واکنش به بیانیه مشترک فرانسه و انگلیس: تنگه هرمز میدان نمایش نظامی قدرت‌های فرامنطقه‌ای نیست. ایران به‌عنوان قدرت مسئول و ضامن امنیت تنگه، نسبت به هر حرکت نظامی در این آبراه حساس هشدار می‌دهد.
🔴
امنیت هرمز با دولت‌های ساحلی است؛ بحران‌سازان مسئول پیامدهای ماجراجویی خود خواهند بود؛ این هشدار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/131701" target="_blank">📅 09:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
گروسی: تاکنون نتوانسته‌ایم به تأسیسات هسته‌ای ایران دسترسی پیدا کنیم؛ این موضوع به مذاکرات جاری میان ایالات متحده و ایران بر سر تفاهم‌نامه گره خورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/131700" target="_blank">📅 09:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرنگار الجزیره تأکید کرد که تاکنون هیچ اظهارنظر رسمی از سوی واشنگتن منتشر نشده است، اما رسانه‌های آمریکایی به نقل از منابع آگاه از وجود «تفاهمی موقت» میان ایالات متحده و ایران برای کاهش تنش خبر می‌دهند؛ تفاهمی که امکان ازسرگیری روند مذاکرات را پس از پایان مراسم تشییع رهبر فقید ایران، فراهم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131699" target="_blank">📅 09:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مکرون، رئیس‌جمهور فرانسه: دو شناور مین‌روب را به خاورمیانه اعزام کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131698" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzRdvDxAyWfQaa0oaIGAQDCDSgolVZnabflccI3R57mjLYiW5JyCI8nJxEuEss4O5KxDzc3CmbeQSQ7s2ts-PQE2oGvKvfpg--S02U1YL2RZhV_0A1EoRSSa-eE6VoEiETBXZT4sD36ulz6hpF4BoS6w216AWFtJEdIL8NSji-Q_P2vkGL3pkaF-749oD_Fs1okoxmKVMiZp73I7GCY1S3VG7HW5qTnf82X3N67tmV5fBTaehtePw7PZks2urHTUw5RZ9d8SEQ5t1mrtBq29Le9uuESmnnalt6qPdpMIk4Ew7TM_lSdsxgnBZhW3bujsVb3QvcU1wguH1vX8k_cWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی از پهپاد انتحاری دوربرد «SKYWASP» رونمایی کرد
🔴
این پهپاد توسط شرکت SR2Vector توسعه یافته و برد عملیاتی آن حدود ۱,۵۰۰ کیلومتر (۹۳۲ مایل) اعلام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/131697" target="_blank">📅 09:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
فرانسه و بریتانیا آمادگی خود را برای استقرار یک نیروی چندملیتی به بهانه حمایت از آزادی دریانوردی در تنگه هرمز و تضمین عبور ایمن از تنگه هرمز که یک موضوع با اهمیت جهانی است، اعلام کردند.
🔴
فرانسه و بریتانیا هر دو همچنین بر تعهد خود به ثبات منطقه‌ای و احترام به حاکمیت همه ملت‌ها تأکید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131696" target="_blank">📅 09:07 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
