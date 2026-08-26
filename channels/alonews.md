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
<img src="https://cdn4.telesco.pe/file/HbiJPHgh8EgU2Zts0MgY4Am5A4q2lA3Bo66oN18MP6dvk6RjduTNDr4x1JVFL6jbjjY92M5zZAzlPDhzZdjCKN4mxButPQ97NweqytTZiIH6C2Vkv-WYROn_yRjkup8zVODlJfnRtfupnD2jRxExyweSO7DqxfHxphjd5t3Crn2mlrg7hUc8a1UuEy4WgiyO0DAn6SrBtujUiBlP1zRRCdHr9Eq377-2YEpqITXeSWhhR5S-LNUbNnjglzsZ3c8TMqijdVPw-M39Rsszel7u48d1WhJdiA6q4Iv79LktDSwrvILR0F2R9khLTrR-UAEaqSmhYBg5YS0Dpdc3Yd-j5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 19:40:24</div>
<hr>

<div class="tg-post" id="msg-143940">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: تا تدوین پروتکل بازرسی از سایت‌هایی که مورد حمله قرار گرفته‌اند، آژانس نمی‌تواند از سایت‌های هسته‌ای بازرسی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/143940" target="_blank">📅 19:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143939">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhVFz0yuKMehF3op5h9GwfVmMMCECLk-VXqLUSVv8yJA1pRMgluPvbOTkNUFW6Fs6b2hXO8spe3XAU_CFIO6HejCyp4iVBUHNfbQbD6U5JLSc0ki0WxPPv-nEhwhAzht_tI4SOAHwpkolMClw1riYc87cycQ1PtuYTmj2DUbtkKsyljD4EmX8mfw8pKsb3AkmG0Psaj6I1CsE1rKs6LDpB7EOGdOgpW16gnQV5oQmna4MAif9wPGj_lQ52gxt19uivuLbQS3WU11DjqLaDx5yjyYUoWJTJQvoTYy7jFSWqMVPA_T8GMpV8DaDts4xQTSdquQ57Lv44iC7OFLJge3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدلیل گرونی سنگ قبر یه عده دزد شبونه از قطعه ۲۱۷ بهشت زهرا کلی سنگ دزدیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/143939" target="_blank">📅 19:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143938">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سی‌ان‌ان: پاکسازی مین‌های تنگه هرمز کار ساده‌ای نیست
🔴
همکاری ایران حیاتی است
🔴
صرفاً اعلام بازگشایی نمی‌تواند خطر مین‌های دریایی را از بین ببرد یا اعتماد بازار را در میان صنایع کشتیرانی و بیمه احیا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/143938" target="_blank">📅 19:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143937">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یک منبع دیپلماتیک به شبکه المیادین:
نخست‌وزیر و وزیر خارجه قطر به زودی به تهران سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/143937" target="_blank">📅 19:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143936">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یک نفتکش هندی به نام HAANA لحظاتی پیش قصد داشت از مسیر جنوبی تنگه هرمز، موسوم به کریدور عمان، عبور کند.
🔴
این نفتکش پس از دریافت هشدار، از ادامه مسیر منصرف شد
🔴
همچنین گفته شده در ۲۴ ساعت گذشته هیچ ترددی در مسیر جنوبی تنگه هرمز مشاهده نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/143936" target="_blank">📅 19:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143935">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: سفر رئیس سازمان اطلاعات مرکزی آمریکا (CIA) به روسیه ربطی به تحریم‌های ایران یا احتمال حمله مسکو به انگلستان ندارد
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، گفت سفر جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (CIA)، به روسیه «به‌نوعی یک سفر نیمه‌روتین» بوده و گمانه‌زنی‌ها درباره دلیل این سفر را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/143935" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143934">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12996542f.mp4?token=Js8IvWZiWq27KK53nGt_IcoNxG0a_LeoKRyIFyyIKRRuSzjU_XZ2r8VL5Ldppwe5jP-tIKWRQudN9BchQQicgH543lmuivLYz9PaXbivjgis8hjpRAnmGfbtZ5DPWiSZ7RWg63cQcPSLMD7xyYQ4unvL_tPn8MYUlOtw0phTUZqH60EHAdZQfonvbb7c_USy0ekmU-tjwuZ00aCkgUCU4CFHEveiWI8echLAcwghLRdojjP5qq-I2lUKu8qecdZvrdPzakfh3MpHDQhLGPjR8g01KwuH_PI7ZQZ0hfmZXEnyFiA5mTFnq5kwFicR9A0VLNsK1n54_n0WnmKz3rr7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12996542f.mp4?token=Js8IvWZiWq27KK53nGt_IcoNxG0a_LeoKRyIFyyIKRRuSzjU_XZ2r8VL5Ldppwe5jP-tIKWRQudN9BchQQicgH543lmuivLYz9PaXbivjgis8hjpRAnmGfbtZ5DPWiSZ7RWg63cQcPSLMD7xyYQ4unvL_tPn8MYUlOtw0phTUZqH60EHAdZQfonvbb7c_USy0ekmU-tjwuZ00aCkgUCU4CFHEveiWI8echLAcwghLRdojjP5qq-I2lUKu8qecdZvrdPzakfh3MpHDQhLGPjR8g01KwuH_PI7ZQZ0hfmZXEnyFiA5mTFnq5kwFicR9A0VLNsK1n54_n0WnmKz3rr7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست: گزینه حمله نظامی در هیچ نقطه‌ای از تنگه هرمز منتفی نیست
🔴
ما به هیچ‌وجه استفاده از حملات نظامی در هیچ نقطه‌ای از تنگه هرمز را منتفی نمی‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/143934" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143933">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ:
شب گذشته 22 قایق نظامی تندروی ایران را در تنگه هرمز هدف قرار دادیم و نابود شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/143933" target="_blank">📅 18:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143932">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Egopf7fjGjdS8NVWhMlUHVrqf99rf1FvJvnmbnK0BY0vrVtufKyL5JRdTbFJWGeyNb4BlWCvOXHur34hcu73ZJsMPvBA8PjPg3zeB_HcmVww3Lw9FD7wztqg8gkT6jLSezJNoqvBKlEyfIPQKxQmKp1u92KNw9KLGDbUCpkl7EtWhrH8TrRDcVFIXhzreQx9QV4CXR-OXy-JUMFHy982N4kXD4YsaV3flC1FudAskm_rEmNEhRuP4zOkt1hrw7gSJekANyCkHbs-8pGGRpJOGdIdR9kXuloOZepp9iTdi76jaCYQinLDdoQD9QV67n1xMfZwB146vLluh93w9bdyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اینترنت رو قطع کنید، یه دیقش هم ضرره
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/143932" target="_blank">📅 18:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏
👈
خبرنگار کاخ سفید:
گزارش هایی وجود دارد مبنی بر اینکه روسیه در حال آماده شدن برای حمله محدود به انگلیس است، سفر ناگهانی و غیر عادی رئیس سازمان سیا به مسکو نیز به همین دلیل بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/143931" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48fa42be5.mp4?token=SvLRHIDhne_657VaWsaH_hNtKXPQLQsqrsFnHSOXoBEuy9WMgVSVg0Q0So9jbNcoNR-2GhhzQZX6xeqM94-WvYDRe5nQaVZwnpjfznI33fx2ZzxGlCno6OOvMC_FTywORqi9K4SWwOK42oZSni5QIrqWt8XoCiXOx7HyvysCBtuem5xhxn0Htr8D5uiNq1j3qbfos3BBeSphN7OdYzZmAAt1okuN4ZlqgJAIpI6mVIp86ngK6PX_u9xEhL1HBK-8il1aU1N-xfGcKgmRK14EtpGp27KTh6cPw-Sv2eV4S_7JoEn-K1yAEHFJv9_296jWdpRBtd4YAqNL1RspAJD7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48fa42be5.mp4?token=SvLRHIDhne_657VaWsaH_hNtKXPQLQsqrsFnHSOXoBEuy9WMgVSVg0Q0So9jbNcoNR-2GhhzQZX6xeqM94-WvYDRe5nQaVZwnpjfznI33fx2ZzxGlCno6OOvMC_FTywORqi9K4SWwOK42oZSni5QIrqWt8XoCiXOx7HyvysCBtuem5xhxn0Htr8D5uiNq1j3qbfos3BBeSphN7OdYzZmAAt1okuN4ZlqgJAIpI6mVIp86ngK6PX_u9xEhL1HBK-8il1aU1N-xfGcKgmRK14EtpGp27KTh6cPw-Sv2eV4S_7JoEn-K1yAEHFJv9_296jWdpRBtd4YAqNL1RspAJD7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از مسئولان‌نظام هنگام مال مردم خوری
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/143930" target="_blank">📅 18:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143929">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMGruYeTxfjtw8CEnsa5Vxov2GcdQOK4wUC6triEzqLOkGHoKBq7TTk_rayrTmyp1ukEr7Xl0QwUstbvxHl9NGWbEij7ovinML6raQtvqe_OkDWd-6H793YedY1x3toX9Xnbi7aF--nJ8ZaN6G0xUJmTLj_TKPwcYl6KV1gWGOP4inJyNOew8f_Bq2TSAEbYlKlHRPzbIbJV9-TISKI1SzgXiEk03KeTerj71kTuiQzeN0Ib_ph9E0euAtJuADbcqOmKOBNciCg611Ywi-pIq18lqvcTtelCw9kQiPIxoacFIE_GhsOBnalBhio-KpRzKRFlaIQEBhnL1kQBtn-mAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چادی هوپان: یه عده خائن از ویزا نشدن من خوشحال شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/143929" target="_blank">📅 18:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd6b5d203.mp4?token=Ao671VICvy7nsKaX3RxTVQFpX_fMeYW3VYFYjzh6x5jaSfA1QdOn3-hX0KR0KIsfOb6znRAKIPdg9y1KYSKMtexX24s1G_92DaQvjpWQjafHeestvokpjx5YOloP_eQBNw92MXj2XbfMNV0D5_uFNdKIhS-oDuFX_pB-oqeUuBw5SbYg7N-o7FM7k07BBXH9TwtbtqJQkeGU8aCjEdenLD35VVW8iHfEBIQTf31d1lQkAuaLAEB_dLIzW5NhljnuaUooD3B7WNSn9FnrisAQQe_sbXbWmmfmsjv1wYeWp9ZzkHftuGb-NwgGslw0IADeui5s4eWPGvOVwltqPljQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd6b5d203.mp4?token=Ao671VICvy7nsKaX3RxTVQFpX_fMeYW3VYFYjzh6x5jaSfA1QdOn3-hX0KR0KIsfOb6znRAKIPdg9y1KYSKMtexX24s1G_92DaQvjpWQjafHeestvokpjx5YOloP_eQBNw92MXj2XbfMNV0D5_uFNdKIhS-oDuFX_pB-oqeUuBw5SbYg7N-o7FM7k07BBXH9TwtbtqJQkeGU8aCjEdenLD35VVW8iHfEBIQTf31d1lQkAuaLAEB_dLIzW5NhljnuaUooD3B7WNSn9FnrisAQQe_sbXbWmmfmsjv1wYeWp9ZzkHftuGb-NwgGslw0IADeui5s4eWPGvOVwltqPljQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیالوگ ماندگار مرحوم داود رشیدی که حال و روز الان ماست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/143928" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143927">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود
🔴
استفاده از فیلترشکن‌ها خسارت بزرگی زده است
🔴
افرادی هستند که اصرار دارند در بر همان پاشنه بچرخد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/143927" target="_blank">📅 17:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143926">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qor9VOqNNt0-sbqqm-6u6TPVNX7zIoDKBCMacvAGZ1PW1KzBrpSer5k1Ib4-VtkzCYogMaQHyCUBh-Esv1XyYvT3LWB5VhyWMMcG_8K6YK2Xfuhg0KzLkU1yMMwUhQH06dgxLV_JIJcjIuu-utdfGJwrGyjdI4FzPI0e873VHLLeJlfc2WKh56m5ZypdYz04yvymYaaAVq3Dtv9D7ZRqLtBhPNIEJCqLzv3eaTljfh204Nwiy795zZMkTKnp3sI9yJXqC3iwSMxKKk3U9f0yVrl_IMhR-GfiSW8X2ENIcJlQGRJY-UPVtCO0YQUBMBxKpZRqJSNTPPQFd3tlyYADZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به الجزیره گفت که حکومت ایران "با مردم خود بسیار بد رفتار می کند، آنها بسیاری از معترضان را می کشند."‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143926" target="_blank">📅 17:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143925">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrI9Np-4CHv7T4BCznkzhyPi3g0UhbkJ1IrBWn7jO9p1z8NiCwqnZOxuhF6PN-7saA7uYr2WeV7YkusZD7rCG0s4hVt8OhQhtepQwVi08EaXt1P-qrKt-DF3aho6xojUy4_kjk-Zv3XtuW0DAjmqkPx943VaqAMszoqnKL-ZABWVoTuNXgVMpFfPUFsRdVa--7l89YYcQ8pJz_o3SMgqlQ0Tvzx3RrnGpTspq9qgtGvuNhvmWlYYtxAoeSjmBxHmUTbGPsPv_MP-V8vdupghUz-zB8IgNL1nsuE-BWoodhKQOBiXu9KE2A6YvVQ-K1lfEi7_4Ycar7I-B86Wrnb8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: رهبر ایران زنده است ولی دست و پا و بدن به شدت آسیب دیده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/143925" target="_blank">📅 17:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143924">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: رویارویی آمریکا با ایران تابع هیچ جدول زمانی نیست و تا هر زمان که لازم باشد ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/143924" target="_blank">📅 17:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
دلار و طلا ریخت
‼️
بیا اینجا ببین کی باید بفروشی و بخری
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/143923" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de06f44cb7.mp4?token=up08NF56CoUsTdUdECgZCKqOhvyN0S_mK_E4CoIBRmQfb_imwh3tn-V4PkBNVh8LSxqlbjjhTxsW119ijso418OdE5yMLqohbzICBu3UlFp5PqIq96egMhd0HYvgzhcx1lD0NMkg58HN-yUWshq2gqWZKoNGP0MZoauDuzpaeNssHnXh6zTvdmDoSAUVTgYyu5apCOFtO4MXbfSewaGpk1RRBx6uiCLdxzAJa4ZAw0PfToKV4xqYVvEFDrKTbEp4eKWz0CZ4zdqRVoHO3L9DqatZJrLdRSQFDafPnoE9bZms2foFaC_qTucGl6NJidmUDwNTTUSEW1sYTqzNPGDgCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de06f44cb7.mp4?token=up08NF56CoUsTdUdECgZCKqOhvyN0S_mK_E4CoIBRmQfb_imwh3tn-V4PkBNVh8LSxqlbjjhTxsW119ijso418OdE5yMLqohbzICBu3UlFp5PqIq96egMhd0HYvgzhcx1lD0NMkg58HN-yUWshq2gqWZKoNGP0MZoauDuzpaeNssHnXh6zTvdmDoSAUVTgYyu5apCOFtO4MXbfSewaGpk1RRBx6uiCLdxzAJa4ZAw0PfToKV4xqYVvEFDrKTbEp4eKWz0CZ4zdqRVoHO3L9DqatZJrLdRSQFDafPnoE9bZms2foFaC_qTucGl6NJidmUDwNTTUSEW1sYTqzNPGDgCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر دونالد ترامپ رئیس‌جمهور نبود، اکنون اسرائیل وجود نداشت.
🔴
این یک تضمین است. اسرائیلی وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143922" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143921">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b63c7b29f.mp4?token=WhrKBBwZDIDvf4C3zQxyVFVR9xZDysJHcBlznNXKm11eUCSmUrez_HfoluN_FvOEY5CeO1cYiWrwdYxgxfy9VDSoXze1YGRcq8u6EThaX8QQS35Cwyb6Srefx31NhenpVp_cIKoXU77HzXvRH1wc5Njx4F2Iso8lrqdw8hFVV_sNYn5SgW5WhIIw5OfYodxv9-p8XN33I5YQ3KIDdOrv4OkHbHIQFXVgtWfihDENWuOeSezynK1HA8E318vLYoTIZocQKUb8r9bm1vVfNqVdvHTEaaFP57rTdmRfmtARkrTRSTONprmlHwrCaxNP_73DDKDSecTvYm7Ip2DzHRvkIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b63c7b29f.mp4?token=WhrKBBwZDIDvf4C3zQxyVFVR9xZDysJHcBlznNXKm11eUCSmUrez_HfoluN_FvOEY5CeO1cYiWrwdYxgxfy9VDSoXze1YGRcq8u6EThaX8QQS35Cwyb6Srefx31NhenpVp_cIKoXU77HzXvRH1wc5Njx4F2Iso8lrqdw8hFVV_sNYn5SgW5WhIIw5OfYodxv9-p8XN33I5YQ3KIDdOrv4OkHbHIQFXVgtWfihDENWuOeSezynK1HA8E318vLYoTIZocQKUb8r9bm1vVfNqVdvHTEaaFP57rTdmRfmtARkrTRSTONprmlHwrCaxNP_73DDKDSecTvYm7Ip2DzHRvkIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
وقتی به لندن می‌روید، وقتی به پاریس می‌روید، تقریباً انگار قانون شریعه (احکام  اسلامی) یک سبک زندگی دوم است.
🔴
این مسخره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/143921" target="_blank">📅 17:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143920">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61179d1b62.mp4?token=jSDvCjeGHKHA_eCF_ZahdIpmbOXxZ2nD02F_-vfR9fiEw_xNnE9N9ul5t0sxkI2xLPUVcrJwheqddpZfoPP61O1jpKVe1nxrEpevXd4fGHZEyWuNtrWDJtXRTmhiy2LkM4QpijDqg1JVKx4bdy_inH3tJutAWJywAZaUk4JUhFNybhJpeSJWdWJd05o40fAB2FOkWe8VWkfBl4BxCzGdgpKcqjFG7MYB4oyBThSF3q-Q2wq-xTyDTtZyorg1h_VHnK1X8uL2ggr29CMVtR-oTT0eGtUyZdkV-nnSvReHL5rETKHXSHnIm4qkULHY3lDL4TFJPnsLkETvFUZ7HszVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61179d1b62.mp4?token=jSDvCjeGHKHA_eCF_ZahdIpmbOXxZ2nD02F_-vfR9fiEw_xNnE9N9ul5t0sxkI2xLPUVcrJwheqddpZfoPP61O1jpKVe1nxrEpevXd4fGHZEyWuNtrWDJtXRTmhiy2LkM4QpijDqg1JVKx4bdy_inH3tJutAWJywAZaUk4JUhFNybhJpeSJWdWJd05o40fAB2FOkWe8VWkfBl4BxCzGdgpKcqjFG7MYB4oyBThSF3q-Q2wq-xTyDTtZyorg1h_VHnK1X8uL2ggr29CMVtR-oTT0eGtUyZdkV-nnSvReHL5rETKHXSHnIm4qkULHY3lDL4TFJPnsLkETvFUZ7HszVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تورم در ایران
:
فکر می‌کنم تورم ۳۰۰ درصدی دارند. شنیدم ۹۰ درصد است. فکر می‌کنم تورم ۳۰۰ درصد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143920" target="_blank">📅 17:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143919">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=VWXTtouvHKRpPifmXcik3WCvJn3IHNc_X4XesuaSDPaWxClCxH1TZWvMpqRqnaTrtlRzZODT3ijxVFKfn3PNyQ_6FdUQliN9gM4JPvZjYjfjHSiXD44ewU1K8g2rJicy80fzKtDijtfsd72lTLKdjZPzIQRF8eoq_zN6K-NUgoGGABrbLawhPjVZdZi2UhMoNIG_3g5UJjyj3pZsb-SNg3z6yDL1_t-m3ij4g3pa-WpZrMg7cSC8getRqMrpesQsbJxvCpBccuwlwgRqSPyDH3SrKPOB3FLysbkg0tioPIqkQD4Rs43AxDlnOG3g-YGUGWl-1DEEjcN7Ow78MZeWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=VWXTtouvHKRpPifmXcik3WCvJn3IHNc_X4XesuaSDPaWxClCxH1TZWvMpqRqnaTrtlRzZODT3ijxVFKfn3PNyQ_6FdUQliN9gM4JPvZjYjfjHSiXD44ewU1K8g2rJicy80fzKtDijtfsd72lTLKdjZPzIQRF8eoq_zN6K-NUgoGGABrbLawhPjVZdZi2UhMoNIG_3g5UJjyj3pZsb-SNg3z6yDL1_t-m3ij4g3pa-WpZrMg7cSC8getRqMrpesQsbJxvCpBccuwlwgRqSPyDH3SrKPOB3FLysbkg0tioPIqkQD4Rs43AxDlnOG3g-YGUGWl-1DEEjcN7Ow78MZeWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: وقتی افرادی حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است. به همین دلیل آن‌ها اعتراض نمی‌کنند.
🔴
و شانس وجود دارد زیرا آن‌ها بسیار تضعیف شده‌اند... بسیاری از سربازانشان حقوق دریافت نمی‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143919" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143918">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e724bf7fc2.mp4?token=KwWznANESmrxQJ1qnDOZ2rhMYJly4oWlSyO4F8StHfkTF4J-b8_-hkam1G_SdEPbWNSqh4iKA-VTQKTK0m3x3x9jle_Os6957NUw-orgJQVW7xZENtkMscig_5DtdDuml9-e4gvuI-LuI3aO2KmDIVuFxNNipUHsO-LS9kFKG8dIOkRCAa-l4z0CmWjIk1knvWweA9bQBO7F5MTh0j_cxelq9cwrRLwhnvu4LRYgoWqZ5o5sfO0qoio7N8d4sblzHkEm4cL47p2CG2KP_3eyDTnPBRZwdtl6zEinsoTiWyjahNtII78cssg8QaHdIcMWRUAleYOTCX9Dm1CfFR8tpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e724bf7fc2.mp4?token=KwWznANESmrxQJ1qnDOZ2rhMYJly4oWlSyO4F8StHfkTF4J-b8_-hkam1G_SdEPbWNSqh4iKA-VTQKTK0m3x3x9jle_Os6957NUw-orgJQVW7xZENtkMscig_5DtdDuml9-e4gvuI-LuI3aO2KmDIVuFxNNipUHsO-LS9kFKG8dIOkRCAa-l4z0CmWjIk1knvWweA9bQBO7F5MTh0j_cxelq9cwrRLwhnvu4LRYgoWqZ5o5sfO0qoio7N8d4sblzHkEm4cL47p2CG2KP_3eyDTnPBRZwdtl6zEinsoTiWyjahNtII78cssg8QaHdIcMWRUAleYOTCX9Dm1CfFR8tpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا
:
آن‌ها هیچ چیزی ندارند که ما به آن نیاز داشته باشیم. ما می‌توانیم بدون آن‌ها ادامه دهیم.
🔴
چند مورد وجود دارد که می‌تواند کمی آزاردهنده باشد، اما می‌توانیم آن‌ها را از جای دیگر تهیه کنیم.
🔴
حرفه است که به کانادا درس دهیم که دیگر نمی‌توانند این کار را انجام دهند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/143918" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143917">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: من باور ندارم که رهبر فعلی ایران فوت کرده باشد
🔴
اگر هم مرده باشد، دارند نمایش خیلی خوبی اجرا می‌کنند؛ چون مدام صحبت از این است که باید برای گرفتن تأیید نهایی‌اش با او گفتگو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/143917" target="_blank">📅 17:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143916">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ به الجزیره: ما در حال دستیابی به یک پیروزی بسیار بزرگ هستیم و ایرانی‌ها از تورم عظیم رنج می‌برند و اقتصادشان در حال فروپاشی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/143916" target="_blank">📅 17:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143915">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/ترامپ درباره ایران: بگذارید این را به شما بگوییم، من متوجه شدم گروه سوم (سران کنونی ایران) هم خوب نیستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143915" target="_blank">📅 17:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143914">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/ترامپ درباره ایران: بگذارید این را به شما بگوییم، من متوجه شدم گروه سوم (سران کنونی ایران) هم خوب نیستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/143914" target="_blank">📅 17:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143913">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ: ما مین‌ها را از آنجا خارج کردیم. اما تنگه هرمز، به کار خود ادامه می‌دهد، یک تنگه فعال است.
🔴
بله، گاهی اوقات ممکن است یک پهپاد یا موشک شلیک شود، اما این یک تنگه کاملاً فعال است.
🔴
مقدار زیادی نفت از آنجا صادر می‌شود.
🔴
دیشب ۲۰ قایق ایرانی را منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/143913" target="_blank">📅 16:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143912">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f8d4b27a.mp4?token=ScMPIImqAc3dqiLkQiLAzkQ8XypAox821pF8ZmViPCSf6vBa4BEIbDgHsMA6STsUOsrnce2e25bOZnftKWF-nkkfVT0CuzuMtcaZGdffzDZWTDSET7UdsDK7NN5Dt4WrC2KbdWgw4YCk0UyI7iRSFtwWQEHeuimpz5Ucx3Rl5yTbi553hvFi2WyRdUvo5YPOMNPEVYsOnrCXWEBepR3lMTymHxL4H5CjNye1DWm9v4vsXxe7_iREXC_saURwy-4zr1NhUfzbnVAcV6sOZZ7ODktc9cQ9JSfShNiZglOu17PRVeDU9A5mhfhDlgdgJQgPkjDwJw9Nl80a2DZ_qgbw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f8d4b27a.mp4?token=ScMPIImqAc3dqiLkQiLAzkQ8XypAox821pF8ZmViPCSf6vBa4BEIbDgHsMA6STsUOsrnce2e25bOZnftKWF-nkkfVT0CuzuMtcaZGdffzDZWTDSET7UdsDK7NN5Dt4WrC2KbdWgw4YCk0UyI7iRSFtwWQEHeuimpz5Ucx3Rl5yTbi553hvFi2WyRdUvo5YPOMNPEVYsOnrCXWEBepR3lMTymHxL4H5CjNye1DWm9v4vsXxe7_iREXC_saURwy-4zr1NhUfzbnVAcV6sOZZ7ODktc9cQ9JSfShNiZglOu17PRVeDU9A5mhfhDlgdgJQgPkjDwJw9Nl80a2DZ_qgbw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من قطعاً قانون شریعت (احکام اسلامی) را ممنوع خواهم کرد.
🔴
ما یک سیستم عالی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143912" target="_blank">📅 16:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143911">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2bb31062.mp4?token=B0JHHn03A_m3wMJJ-q0EdgKonqV7jofO48wiejLgu4304sxBW7nvgBhgwgiTxEZPGA59UbTPvnplIWFAZyr-tTnvWzYsu1xIIOHgxIksUZQmlhJaiupLxuBUj3sW8Sj5m39VE1AUzvPkyTUmWddzRo094trO5KHnsUvd7RSfTMEs6P0rRQ26dS2qm-vHIF-Sha-EWqJ4t8h0fjgk3slwbY6ceQYNZIX-ELDY9B2ZU2OzsnMSkzkYOxh6w_MyTBkkwOf3r0LXT02E4GRZ7Am8OjBP-UPnOwRbcJVi41valA_xwtfZIQPfG9pui5cdDNJ4t9hl5deCOAzkjrRGm6ITug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2bb31062.mp4?token=B0JHHn03A_m3wMJJ-q0EdgKonqV7jofO48wiejLgu4304sxBW7nvgBhgwgiTxEZPGA59UbTPvnplIWFAZyr-tTnvWzYsu1xIIOHgxIksUZQmlhJaiupLxuBUj3sW8Sj5m39VE1AUzvPkyTUmWddzRo094trO5KHnsUvd7RSfTMEs6P0rRQ26dS2qm-vHIF-Sha-EWqJ4t8h0fjgk3slwbY6ceQYNZIX-ELDY9B2ZU2OzsnMSkzkYOxh6w_MyTBkkwOf3r0LXT02E4GRZ7Am8OjBP-UPnOwRbcJVi41valA_xwtfZIQPfG9pui5cdDNJ4t9hl5deCOAzkjrRGm6ITug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما به زودی پیروزی بزرگی در ایران خواهیم داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143911" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143910">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb401a2e6.mp4?token=R0JG1tU3Q1a9o-Q-h_H8bfkxljgHYHn2dIW5iV5wSUmndMsSvTpYwcnHWRdlK-Jpa65DdU99m4LqONnviIvYJVVJ80mJM9PVhr0BhoJQkHY7bDwcI4WQRx03FXf6bWNQD3gLotYxCeWz7ltpxJzO0GlMgijzEXiRmTZMZ8vogh6doD1Eay9m4bXP_mBm8rSLPXc7hto79bBLXW3NqoSihHy4TSs_Iq6czkgXwYhYcDlKWfJhNToJMhUWM7p8pAirOs2l6vxOjNLul4VU_O_MtWOLaQ7JjIAmZaKcek0jvqGx2EcnIvFM4QKMC79vrilqDwwplBtt0m_umsP7QDJUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb401a2e6.mp4?token=R0JG1tU3Q1a9o-Q-h_H8bfkxljgHYHn2dIW5iV5wSUmndMsSvTpYwcnHWRdlK-Jpa65DdU99m4LqONnviIvYJVVJ80mJM9PVhr0BhoJQkHY7bDwcI4WQRx03FXf6bWNQD3gLotYxCeWz7ltpxJzO0GlMgijzEXiRmTZMZ8vogh6doD1Eay9m4bXP_mBm8rSLPXc7hto79bBLXW3NqoSihHy4TSs_Iq6czkgXwYhYcDlKWfJhNToJMhUWM7p8pAirOs2l6vxOjNLul4VU_O_MtWOLaQ7JjIAmZaKcek0jvqGx2EcnIvFM4QKMC79vrilqDwwplBtt0m_umsP7QDJUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما از همان ابتدا واقعاً و به‌طور کامل بر ایران مسلط شده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143910" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143909">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رایزنی وزرای خارجه عربستان، ترکیه و قطر درباره کاهش تنش در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143909" target="_blank">📅 16:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143908">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab00cbf2d.mp4?token=FBLeVKYhyHIIE-M0ZbTCScCmX_Isp9R6pRiCexxZd-gP6XSgDKLUK_dNgZJo3c1-EmYd3rOI1pQhXp3AZwjCAInGK4gwiEy_8EfXezz82kbcCn5K72j5dn_q1kqyuCmlPvD0dzxzowN3rWu3o-R1xIPvLP25Gv7Xjn-BGMvLcadQ7PDGA8nTjiPmiBYg5jaL9szHuNUqu1r4XVdY2X-fo3-PX_9LbwZRfA348k5JhMHd585K1qGulrkNcUbKajlRW77mRZaV1agI0VhYB4gSOH0lpxup6hFbd3rSjwmYmrwGwI2_er-IRQJiE3CSUWk5QZLueAHaokNEbiz81E7iAHEfr3xDgFhaUrQCqgPx8KSM2LgBf0ETwnvn7Aecrd7BcPcBjZflcqoasniA5xNeewGEYokE50rBjP4nzii10OwXp7FW48PyJw94UrQe7gMgkkXTkFRr6CWRP_0xK9wnRM8x_s2ThH518usUw1e2PWkQryc5sgHnRXHbMhgBY2ZlpQTR0ovov9xZ9lwwkXvsYyPLNqbi7VMaO1m5TSuMeYXpcN0_1uksgvwH5HQxkwq8zQFXobEsRt7hsGwnJNxR1kGHbChCIXF0wb77U_io_z0q3Yz2DqBV6klRnPHziewKsu0ESAVvV2HB2HRGn5nJnsJPhN_crT3J7xcancjBTjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab00cbf2d.mp4?token=FBLeVKYhyHIIE-M0ZbTCScCmX_Isp9R6pRiCexxZd-gP6XSgDKLUK_dNgZJo3c1-EmYd3rOI1pQhXp3AZwjCAInGK4gwiEy_8EfXezz82kbcCn5K72j5dn_q1kqyuCmlPvD0dzxzowN3rWu3o-R1xIPvLP25Gv7Xjn-BGMvLcadQ7PDGA8nTjiPmiBYg5jaL9szHuNUqu1r4XVdY2X-fo3-PX_9LbwZRfA348k5JhMHd585K1qGulrkNcUbKajlRW77mRZaV1agI0VhYB4gSOH0lpxup6hFbd3rSjwmYmrwGwI2_er-IRQJiE3CSUWk5QZLueAHaokNEbiz81E7iAHEfr3xDgFhaUrQCqgPx8KSM2LgBf0ETwnvn7Aecrd7BcPcBjZflcqoasniA5xNeewGEYokE50rBjP4nzii10OwXp7FW48PyJw94UrQe7gMgkkXTkFRr6CWRP_0xK9wnRM8x_s2ThH518usUw1e2PWkQryc5sgHnRXHbMhgBY2ZlpQTR0ovov9xZ9lwwkXvsYyPLNqbi7VMaO1m5TSuMeYXpcN0_1uksgvwH5HQxkwq8zQFXobEsRt7hsGwnJNxR1kGHbChCIXF0wb77U_io_z0q3Yz2DqBV6klRnPHziewKsu0ESAVvV2HB2HRGn5nJnsJPhN_crT3J7xcancjBTjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرتس صدراعظم آلمان: ما باید از این جوّ غم و ناامیدی خارج شویم.
🔴
ما باید از رنجش گسترده‌ای که برای مدت طولانی کشورمان را فلج کرده است، رها شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/143908" target="_blank">📅 16:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143907">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ به الجزیره: برای مذاکره با ایران «عجله‌ای ندارم»
🔴
ترامپ در گفتگو با الجزیره مدعی شد که هم اقدامات اقتصادی و هم نظامی در مواجه با ایران «موثر» هستند.
🔴
او در پاسخ به سوال خبرنگار الجزیره، افزود که «من هیچ برنامه زمانی ندارم، عجله‌ای ندارم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/143907" target="_blank">📅 16:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143906">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
یک منبع ارشد ایرانی: توافق با عمان در مورد تنگه هرمز هنوز نهایی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143906" target="_blank">📅 16:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143905">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cbeca874.mp4?token=H69cSwawonRatsxWpKb0X_2RLx62frXfiKNDq8u91j09lU2cEb8iNPGjDAAB3ZsM3SrItokZXeforOfqIW9FvIJpPzJJGunXU-2ncspXNwR9vrkGUPIhZc8gJtjqtCiOpEv7J-ILPy1455L3gvQzSh1QanbNphbx-v9ieocE0O1lVG3HbSHQ2xCT2-aM2I23vX93jqvnYtsEUpkG3TFRFadvaRC7fG66XFfRu3AaSpCeVr-gmva7EnjTjUGAuHtiVHEVT8AtCXBkOwoGVzj485KtMjkJoqVfEpBM1x9GYIfRVeJvIxmNfZcDMoBZf57WloSRTLO_PsjemGCqIsMCJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cbeca874.mp4?token=H69cSwawonRatsxWpKb0X_2RLx62frXfiKNDq8u91j09lU2cEb8iNPGjDAAB3ZsM3SrItokZXeforOfqIW9FvIJpPzJJGunXU-2ncspXNwR9vrkGUPIhZc8gJtjqtCiOpEv7J-ILPy1455L3gvQzSh1QanbNphbx-v9ieocE0O1lVG3HbSHQ2xCT2-aM2I23vX93jqvnYtsEUpkG3TFRFadvaRC7fG66XFfRu3AaSpCeVr-gmva7EnjTjUGAuHtiVHEVT8AtCXBkOwoGVzj485KtMjkJoqVfEpBM1x9GYIfRVeJvIxmNfZcDMoBZf57WloSRTLO_PsjemGCqIsMCJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به‌دنبال وقوع سیلاب‌های گسترده در نپال، نزدیک به 300 گردشگر خارجی مفقود شده‌اند.
🔴
این سیلاب‌ها تاکنون دست‌کم 17 کشته و حدود 400 زخمی برجا گذاشته‌اند.
🔴
گزارش‌ها حاکی است مناطق مرزی نپال و چین نیز تحت تأثیر این سیلاب‌ها قرار گرفته‌اند و عملیات امداد و جست‌وجو برای یافتن مفقودشدگان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/143905" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143904">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae40c1a74.mp4?token=dMw8Q_rw4l2nbVAnr7OJvgNPnTCnbIEqHBmxbyde5Meu9c0ELv5bJoUF6RGae5dHBtNVJKB_BIVCdmFW5oaCfZ59gDQx-nyIeJ7pJuovaIx-sEN02jVipEXCm8aoetnlo_u-G9XtdHB-falKQ-pWJn-3MavBSokdw9gS-bLQjRXjZPt4ZRq428kwsk2YVo3FvCKuwBV73YMaUPwFmx_IH6vOH2d8EsRZaH66IjOI2fIe2N71Gp4gFHP8ysMxDkigH8wDX-wcsXQqtnBLx24lymhIFre_i7PdoS5DugqNtr3Gs1axcwHHX594RLWu1SCLmScOWXPu5XrVtaK4LENfwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae40c1a74.mp4?token=dMw8Q_rw4l2nbVAnr7OJvgNPnTCnbIEqHBmxbyde5Meu9c0ELv5bJoUF6RGae5dHBtNVJKB_BIVCdmFW5oaCfZ59gDQx-nyIeJ7pJuovaIx-sEN02jVipEXCm8aoetnlo_u-G9XtdHB-falKQ-pWJn-3MavBSokdw9gS-bLQjRXjZPt4ZRq428kwsk2YVo3FvCKuwBV73YMaUPwFmx_IH6vOH2d8EsRZaH66IjOI2fIe2N71Gp4gFHP8ysMxDkigH8wDX-wcsXQqtnBLx24lymhIFre_i7PdoS5DugqNtr3Gs1axcwHHX594RLWu1SCLmScOWXPu5XrVtaK4LENfwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار دیشب تجمعات شبانه: دلار شده ۲۰۰ تومن همتی یه کاری کن نگن که بی غیرتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/143904" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143903">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXmvfpz553C-t-y2bk7LBfv-8GzhBt2vMJtpDE9OBqb_YJ-OZHQfuDU-luukhIUke4esGTxm0nrCbfQeSiRD0kY4Kv1rVU8jA6oqXpxQOUr954ZbNFDtQqDtjT3O4HNQ2i90Vh4RdgClN7B9kqXp9kCpCRnfZDWFXFx0fZ_PtJ2Gclp7A2Qja4vKiQhiO7wrfCRojgGzXA2Y0TmPStG_zR_3RNrqi5MUTIt16Ge6xoYT3B7yD_3b76dZKonWJJ1oMCk2_8ti3rBbnZU_b-TTIJqarsBQALGTFKPB2pWnpKChemHVSxAPS3Zure-MZ-989iyU6bfpUi8dZdVXFPUhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده، تعداد هواپیماهای تانکر سوخت‌رسان خود را در پایگاه هوایی العديد در قطر به بیش از ۹ فروند افزایش داده است
🔴
در حال حاضر، بیش از ۱۵ فروند هواپیمای تانکر سوخت‌رسان در امارات و قطر، و حدود ۲۰ فروند در عربستان سعودی مستقر هستند تا از عبور نفت‌کش‌ها از تنگه هرمز پشتیبانی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/143903" target="_blank">📅 16:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143902">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سفیر ایران در روسیه: برخی تلاش می‌کنند مناسبات تهران و مسکو را به روابط ایران و غرب نسبت دهند که رویکردی نادرست است
🔴
پزشکیان و پوتین برای ششمین بار، در حاشیه اجلاس آتی سران سازمان همکاری شانگهای دیدار می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/143902" target="_blank">📅 15:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143901">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزارت خارجه سریلانکا:
13 نفتکش تحت تحریم متعلق به ایران را که در نزدیکی سواحل جنوبی سریلانکا هستند را زیر نظر گرفتیم و آماده توقیف آنها هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/143901" target="_blank">📅 15:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143900">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWnOw0FzIB8L4ZBh7FSHQ6fkfP2gbswErzSJ_wYgqH87XQjnLzzRTcW0MWzYSPbm-xcyJ7Y46SfyzM0Vo_rbxTe3j8wZPCfwv46JJeJmSjj75ag9jWlL3pr9AT3dw9Ajz8RnMX5r-AhWRmg0jJS7fbWWJB9OW6OkoyqNji3a5aRpUEHWmRsEeUM5RLEpow2T4x9MZRU1xGFptL9bzvMM19npT6WqvGNG4CsDQ4UAn92PnoeWOrYbuZeJRUBECGRlpys8UGlJm7asqRSxpZmzVVvXOBIBgIZ1WH8HkVJ1vLI7a4DUGGIgkdM7cej1ZZMnb9P8KomwfkfDlOYadMYl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:رئیس مجلس نمایندگان، مایک جانسون، عالی است. او کارها را انجام می‌دهد!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/143900" target="_blank">📅 15:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143899">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، قرار است به‌زودی به تهران سفر کند.
🔴
بر اساس گزارش‌های منتشرشده، این سفر احتمالا فردا پنجشنبه و در چارچوب تلاش‌های میانجیگرانه قطر میان ایران و آمریکا انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143899" target="_blank">📅 15:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143898">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر نیرو: در جریان جنگ اخیر، در مجموع ۴۲۰۰ مگاوات از ظرفیت نیروگاهی کشور را از دست دادیم که بازسازی و جبران این ظرفیت در دستور کار قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143898" target="_blank">📅 15:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143897">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی سپاه: تنگه هرمز در اختیار ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143897" target="_blank">📅 15:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143896">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شبکه ام‌اس‌ناو: از مجموع سه ناوشکن همراه گروه ناو هواپیمابر آبراهام لینکلن، فقط یک ناو همراه لینکلن بازگشته؛ دو ناوشکن دیگر تاکنون هیچ دستوری مبنی بر بازگشت دریافت نکرده‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143896" target="_blank">📅 15:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143895">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-ymcjd9fD5EajsLokabjIoIkv_czCMR-m5wtum37HNBTOMYOT4VQ_X1wsw1p7RR-fOgtJAwJJ-W6i2qxp8TJmSrBht2--WElhPFTqPDNIy77Y-f4XcBrDwYqUXvHqpL6CUn0zMQRcf4ZJm2odCqlsP2Ev2lHbsI0rco_cek8M1frOOT9pA6W1f6UL7UMtJFHcqff1PmybyiI4P9bGSOTER9eHbfCfyslFAUpDBcaRDiQrg7r8C4U7VA-Ysvsuh5moBQWpL-xBsH0vYXO-3v8PC8ZF6Ccy6TDV3hv6Jrf_9YeoKnrvAcxi952Eyxg62Jj6xFXij2CHRQwg4H7PKKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
راک‌استار انتشار تصاویر لو‌رفته GTA 6 را «دلخراش» توصیف کرد؛ تاریخ عرضه ۱۹ نوامبر
🔴
به اعلام راک‌استار گیمز، انتشار تصاویر گیم‌پلی GTA 6 پیش از موعد «دلخراش» بوده و این شرکت بابت اینکه بازی به شکلی خارج از برنامه در معرض دید قرار گرفته، عذرخواهی کرده است.
🔴
راک‌استار تأیید کرد توسعه بازی «تقریباً به پایان رسیده» و فردا نمایش مفصل‌تری از GTA 6 منتشر خواهد شد.
🔴
تاریخ انتشار بازی نیز ۱۹ نوامبر اعلام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/143895" target="_blank">📅 15:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143894">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نشریه "ترایبون"، پاکستان اعلام کرده است که ایران در جریان درگیری نظامی با هند در ماه مه سال ۲۰۲۵، "حمایت قوی" از این کشور به عمل آورده است!
🔴
این ادعا توسط ایشاق دار، معاون نخست‌وزیر و وزیر امور خارجه پاکستان، در پاسخ کتبی به مجلس ملی در مورد وضعیت روابط پاکستان و ایران مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143894" target="_blank">📅 15:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143893">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYrOIpsCqmzymIt-CR96oPh99k5xiZrAKfXfs7v9yyZAHaB0n4fSlWDkZQhaDgarJhVEQjQ4SNPIiwC9Tnr66tE9HlqNk3_deDc0KExQC41PH_qJKF1Gq2YFDCa5HpLRtblPvowDWdDMqA8wA3kNDRWr60aqlMIK6-3G_IXRXOMFHr26I21wVnMGkVNxyFacsadsh2alyDHhXuTXUcy9giYYXXKRdo0ykvP8Zn-EAlpH781zh-2ONWbjlV8Z1gRLcQeXkH6gooMd5WZX2c2qfIL0ktcX1qyHHADAlR6EWgVqsgKblK6JwYp7MPOXsIevuT52aNOy7c7-ntIiYmJIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، شبکه اجتماعی Truth Social:
رئیس مجلس نمایندگان، مایک جانسون، فوق‌العاده است. او کارها را به خوبی انجام می‌دهد!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143893" target="_blank">📅 15:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143892">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پزشکیان: جنگ همیشه راه‌حل عبور از مشکلات نیست
🔴
گره‌ای که می‌توان با دست باز کرد را نباید با دندان باز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/143892" target="_blank">📅 14:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143891">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گفتگوی وزرای خارجه قطر و عربستان درباره تحولات منطقه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143891" target="_blank">📅 14:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143890">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تانکر ترکرز: در خلیج عمان دست‌کم ۱۵ مجموعه عملیات انتقال کشتی‌به‌کشتی (STS) در حال انجام است.
🔴
ما ۲۵ میلیون بشکه نفت خام را شمارش کرده‌ایم؛ به‌علاوه مقداری محصولات پالایش‌شده نفتی.
🔴
این نفت تقریباً از تمام کشورهای منطقه، به‌جز ایران، منشأ گرفته است.
🔴
اکنون پنج مجموعه دیگر نیز پیدا کرده‌ایم و یکی از آن‌ها مشخصاً مربوط به گاز مایع نفتی (LPG) ایران بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/143890" target="_blank">📅 14:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143889">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
امید دانا:
اختلاف «علی کریمی» و «رضا پهلوی» از اونجایی شروع شد که علی کریمی گفته بود به ازای هر اعـدامی؛ ما هم یه قرآن میسوزونیم که رضا پهلوی خیلی به اسلام اعتقاد داره و با اینکار مخالفت کرد.
هرکسی که اسلام ستیز باشه رضا پهلوی بایکوتش میکنه و بهش فشار میاره. چون میگه ما با اسلام نمیجنگیم.
🔴
رضا پهلوی خودش تا سال ۲۰۰۹ اصلا دنبال تغییر جمهوری اسلامی نبود و دنبال این بود از طریق رفسنجانی و خاتمی توی حکومت اصلاحات به وجود بیاره. مدارکش هم موجوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/143889" target="_blank">📅 14:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143887">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L157JAKXZgAE8LHNxpUmzyBRdYVEqtZdLiomC-C1GSQ6B8jWsnKsv7g2WniuttIBDSb48hz0gGOwkogSsK8ZzKkwmoaZB6DTf82ssYygmOPN-7YM6tI2TOyIyP-CncxqIltu6z7zN6X2foPWhdrUQQS4nzIufJqa4Z8ohn4k4LSWdloDYHQd0SErb5Ks_t90M92v6c0Ay2zmAbhayYvOpL7WsWeOTn6AgwSWcIyr__-mEAWF-zDpiPJ3JzuxMAJ-IELBm0DB-JiD4kzFVUhCTa5qO6fOOnf2AZZZZL8YRL8t4H6zkRhXe502vfxWu3oJxqeGF2cdqO0GSbfypCxdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640fdccd62.mp4?token=eA6FY_j--bqubf_WKVyqQ-n5K4tUqNgRR7rKyIje3z02REpjZi7eWTnERI1S2aWHTLAbby5G8FoYYwRBYkJQN6AK21ru1FZCMlkFNEGK-bTlu_5rQE7mBZHkCNvDJ0lLh8iz9-AZBVlNA7xZSPecjPfN4bMQADGyzARClvCH-qdQAhksJ3EWr8j8MetOrF6Pe6GJ8JLc6X49bXNwoEO0WuNQV3v2USufDRwuq9hFBSIRufoCHGE8A5cOuscfwtday0FNoGOg4-V_3DtuSvf4JOFd6Yyl18h2LFARJIuMV6F8JnDn0i61QR2_vgr0laG7wJtNZXNgB0GtOJHDqnrA5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640fdccd62.mp4?token=eA6FY_j--bqubf_WKVyqQ-n5K4tUqNgRR7rKyIje3z02REpjZi7eWTnERI1S2aWHTLAbby5G8FoYYwRBYkJQN6AK21ru1FZCMlkFNEGK-bTlu_5rQE7mBZHkCNvDJ0lLh8iz9-AZBVlNA7xZSPecjPfN4bMQADGyzARClvCH-qdQAhksJ3EWr8j8MetOrF6Pe6GJ8JLc6X49bXNwoEO0WuNQV3v2USufDRwuq9hFBSIRufoCHGE8A5cOuscfwtday0FNoGOg4-V_3DtuSvf4JOFd6Yyl18h2LFARJIuMV6F8JnDn0i61QR2_vgr0laG7wJtNZXNgB0GtOJHDqnrA5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب ایرج مصداقی، عضو دفتر رضا پهلوی گفت که
امید نادان (دانا) به پیچِ 14 میلیونیِ علی کریمی دسترسی داره چون کسایی که علیه امید نادان (دانا) حرف میزنن رو بلاک کرده.
🔴
حالا علی کریمی استوری گذاشته که
ایرج مدل 57، مشاور آقای رضا پهلوی؛ اگر ثابت نکنی که پیج من دست هر کسی غیر از خود من باشه، خیلی بی ناموس و پیشرفی!
24 ساعت به اقای رضا پهلوی زمان میدم که در این مورد اظهار نظر کنه، در غیر اینصورت هر اتفاقی بیفته، گردن خودش و مشاوراشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143887" target="_blank">📅 14:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143886">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHv_O1QFY-fAd1j1TYT23F7JZQ7OhScpnL2gHMfl9r4WIusETs6L5STK0UFrZGZxPd9njHuL4pJci05je2O5H_6Ilsh6qNA162s22n6o2-JuqtkfBqwl-Dhy4Fx39cNo1g4Df0dX7ERt0lTmk8YEsRZF1nnz0mkrwQ2fRqJKqvAeYg_cb4RXtqQ2Q3S6UrytS7VRyASIMAJtr3NTlHQVmLkQNrX9z-zeVbIC5qXJJ9GPmauctIzc1EfmU44SYvf-0FYaOiPMkwLDDIYedL_SIgEVVc8hROIca74xRc_dHXItnjX8ujx2oeBp5kAL9cMeB2JEdHuy_YLYKsJMQkv58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: به نظر می‌رسد که واشنگتن ممکن است در متقاعد کردن کشورهای همسایه برای پیوستن به تحریم‌ها علیه تهران با مشکل مواجه شود.
‏
🔴
برخی گزارش‌ها حاکی از آن است که با ۱۶ کشور هم‌مرز با ایران تماس گرفته است - ۸ کشور از این میان، دشواری قطع روابط اقتصادی خود با ایران را به دلیل منافع در هم تنیده تأیید کرده‌اند - در حالی که ۸ کشور دیگر پاسخ داده‌اند که در حال بررسی این احتمال هستند، که می‌تواند به عنوان یک امتناع مودبانه تعبیر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143886" target="_blank">📅 14:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143885">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
به گفته برخی منابع: به نظر می‌رسد که واشنگتن در متقاعد کردن کشورهای همسایه برای مشارکت در تحریم‌های اعمال‌شده علیه تهران، با مشکلاتی روبرو است. برخی اطلاعات نشان می‌دهد که این کشور با 16 کشور همسایه ایران در تماس بوده است:
🔴
8 کشور تأکید کرده‌اند که به دلیل وابستگی‌های اقتصادی متقابل، قطع روابط اقتصادی با ایران برای آن‌ها دشوار است.
🔴
8 کشور دیگر نیز اعلام کرده‌اند که در حال بررسی امکان این موضوع هستند، که این می‌تواند به عنوان یک رد غیرمستقیم دیپلماتیک تلقی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143885" target="_blank">📅 14:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143884">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHC2N7YDoB5icDYjgHRBTJeqpjcF5a0nG9RWz6za9rDq6OgD5S2F0yq8ifvYZA1mOXwDQrhKyXviRqIG7z1z5YoH5C_Rqkkjf-0PbAx244m_bvRkxTYyF3y6w1ABW7IpAK5znsV50VFwGvuagK0XtWy6W2O5VGNPaXhR9XO6ITtcq6I9ozfykhhWdFEj7k9AWA_yRho8CMnzVcv_LyOErZgnVkT8MKUsOERt9-ZL_g0XyZMFIPXZRbsxv0fjnGxZ4SgIqZjkNHOrZ42OIskb_A8lAwCcVMa-0xEcxi4oDj02PVJbb3jjJuAg0RnqBoRPD6xVBNlaAwQdJp8dTLmcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلتفرم خرید آنلاین طلا میلی‌گلد، حدود ۳۰۰ کیلوگرم کسری طلا داره، یعنی طلاها رو فروخته ولی نگه نداشته. اگر توی این پلتفرم سرمایه‌گذاری کردین حتماً سرمایتون رو از اینجا خارج کنید.
#میلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/143884" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143883">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739904d208.mp4?token=qyq0UD7N-xMOSK-H7ISJpHuO_iUPdP3NQ-iX8GPorlvSAubhP5JayBK8fhziuDofcb1BK128FR24UtVqH2mQokA2dNlrRFA8E2SxkhPzLXTgj9v9VIoU3gK_QX16RsQOCzVzbvJ7C0cDWcH5E-4TM0BZZjbK9UydwbPwQUJnVn1oN1QHt7SDeD4lcJHO30-vUMSELOzmnp7viucx9kW1VC3m0TJ1DXiXsAO0nHt9uJwJtMDoGu6YICXFk5-VZi0Ohw7ZyW9f4v_Q5rH9c4ImAej-d0WD5rnDHHEHfe3WPMLgxLNGYYPkZf_Mpk8dcbg9mhJ--zCj6jJ8FpZFGp3qRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739904d208.mp4?token=qyq0UD7N-xMOSK-H7ISJpHuO_iUPdP3NQ-iX8GPorlvSAubhP5JayBK8fhziuDofcb1BK128FR24UtVqH2mQokA2dNlrRFA8E2SxkhPzLXTgj9v9VIoU3gK_QX16RsQOCzVzbvJ7C0cDWcH5E-4TM0BZZjbK9UydwbPwQUJnVn1oN1QHt7SDeD4lcJHO30-vUMSELOzmnp7viucx9kW1VC3m0TJ1DXiXsAO0nHt9uJwJtMDoGu6YICXFk5-VZi0Ohw7ZyW9f4v_Q5rH9c4ImAej-d0WD5rnDHHEHfe3WPMLgxLNGYYPkZf_Mpk8dcbg9mhJ--zCj6jJ8FpZFGp3qRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به نظر میاد اگه حجاب داشته باشید دیگه رقص توی خیابون مشکلی نداره
🔴
البته هرشب شاهد رقص پرچم و میله هستیم و اونم مشکلی نداره
✅
@AloNews
|</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143883" target="_blank">📅 14:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143882">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP0TYmwB9oiKIpDS5asKoETmMc6DrRaPIc39x1Wjpc1R4WAz7oAAnFYGSbFzSbhxqm2wNPb4Gh8PxejqeYSVI60ZQhxL2BaG4fdAcbxp8Wb5zAoAhDGPetF0vi5AmmMzdCsUa1JQ8jlC7VWr82bSIVpiyap0U9NJIql5Z76p5yCG6gvOTIroBfTSAsDxtwbjiImJgURqq6p6MPo8jtKm1U6-8WQogZZFPjFHCwmmNd_b7gGsexUO1uaMBsh-2RiWzKnLQEdThBvJ4Z1VrI7gEJKHKkvUfwJZaQyJSnIT8RUzGUV2Ku6bZiqN5zP7acPbeZEuKQWuVbJw6B0OrSgTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قالیباف: مذاکره با قاتلان رهبر برام افتخار نیست و برعکس برام خیلی سخت و امتحانی سنگینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143882" target="_blank">📅 14:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143881">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143881" target="_blank">📅 14:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143880">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رویترز:تحقیقات آمریکایی در مورد نفوذ به داده‌های مرتبط با ایران در یک شرکت که از ابزارهای آن برای تاسیسات آب استفاده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143880" target="_blank">📅 13:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143879">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=vz9cRlwRxF0lCYB_zA4MgYhKIS1tUcIDbsnKkzWlch9jYtl7uF0_7T2xwoGpk1SXgfyvHh36QE-RJYZyTnnfMBvYnlkkpOB-C16zh322zbvFQ1auOZ3HdjwZCZFtbhQpTnY9uK6lmhYnYMsH3HiE2esAP6w_vdSH5F_wpN1kGOHZHDYxlXRmyiQ9TnhLfOnKcXznEi7j6rcXy4Vxx1Ypf8tJyArlkj9osAqnp-LxnYJzky-Vk5UMO7JNk8kJLfVXRRw0A1FoObAsnWjlZzy4YspYp8uAgrbA--RKwLFyr3iIKrQMHGRJ9YwgnoiUvHNIGx3Uzkoz5iHYfVP6tFhg1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=vz9cRlwRxF0lCYB_zA4MgYhKIS1tUcIDbsnKkzWlch9jYtl7uF0_7T2xwoGpk1SXgfyvHh36QE-RJYZyTnnfMBvYnlkkpOB-C16zh322zbvFQ1auOZ3HdjwZCZFtbhQpTnY9uK6lmhYnYMsH3HiE2esAP6w_vdSH5F_wpN1kGOHZHDYxlXRmyiQ9TnhLfOnKcXznEi7j6rcXy4Vxx1Ypf8tJyArlkj9osAqnp-LxnYJzky-Vk5UMO7JNk8kJLfVXRRw0A1FoObAsnWjlZzy4YspYp8uAgrbA--RKwLFyr3iIKrQMHGRJ9YwgnoiUvHNIGx3Uzkoz5iHYfVP6tFhg1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از حامیان حکومت: ارزش دلار هر روز داره بالاتر میره و پول ما بی ارزش میشه، اما این به نفع ماست!
🔴
اون فرد خارجی بیشتر محصولات مارو میخره، در نتیجه تولید بیشتر، بیکاری کمتر و تورم مهار میشه.
#کریه_المنظر
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/143879" target="_blank">📅 13:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143878">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=g1xkRFe69V2UjlTXW1aWBdVqGkSY9-NsWxNqbedKJENF_i_gLyw1on57Q8GrDFZfM0evG_77vRaY4_zK9SSNiqCAIrPG3Kqx1EoqUEUp0FZHkjcIk9u3s2isz56j4UztqS4BcI6bjxSh3S7XmuGiwpINK1qmfwworruKJsz9irLzljCRbuewMArJNYjrGkmsWv3ve1WZoDaFZV5oa95H72kz9rN_3LxB88Tx-mtdptwiZTgl_g2Pp1LwfdwT0TEqblZfaXhDFN99rzZ3yI39Z6EzdDdmc7ydePnONBRSdIpDWHZgOXGtnEhPKEqAoQomt4RlrfwBYVhXu8eUgepKug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=g1xkRFe69V2UjlTXW1aWBdVqGkSY9-NsWxNqbedKJENF_i_gLyw1on57Q8GrDFZfM0evG_77vRaY4_zK9SSNiqCAIrPG3Kqx1EoqUEUp0FZHkjcIk9u3s2isz56j4UztqS4BcI6bjxSh3S7XmuGiwpINK1qmfwworruKJsz9irLzljCRbuewMArJNYjrGkmsWv3ve1WZoDaFZV5oa95H72kz9rN_3LxB88Tx-mtdptwiZTgl_g2Pp1LwfdwT0TEqblZfaXhDFN99rzZ3yI39Z6EzdDdmc7ydePnONBRSdIpDWHZgOXGtnEhPKEqAoQomt4RlrfwBYVhXu8eUgepKug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فریاد «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی امروز مجلس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143878" target="_blank">📅 13:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143877">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قالیباف: مذاکره در نگاه این جانب، نه ارزش ذاتی دارد و نه تابو است؛ نه مطلقاً خیر است و نه مطلقاً شر. مذاکره هنگامی معنا می‌یابد که ابزار پیشبرد منافع ملی، احقاق حقوق ملت، رفع ظلم و تثبیت دستاوردهای مقاومت باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143877" target="_blank">📅 13:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143876">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پولیتیکو: جنگ ایران ذخایر تسلیحاتی آمریکا را تحت فشار گذاشته و استرالیا نگران شده است
🔴
به گزارش فرارو به نقل از پولیتیکو، کاهش ذخایر مهمات آمریکا در پی جنگ با ایران، نگرانی‌هایی را در استرالیا ایجاد کرده که برای دفاع از خود وابستگی زیادی به تسلیحات آمریکایی دارد.
🔴
کانبرا برای کاهش این وابستگی، برنامه ساخت صنایع موشکی داخلی را سرعت بخشیده و قرار است تولید محلی موشک‌های Naval Strike و Joint Strike از سال ۲۰۲۷ آغاز شود.
🔴
منتقدان اما می‌گویند استرالیا برای ایجاد توان تولید داخلی بسیار کند عمل کرده و همچنان به‌شدت به زنجیره تأمین تسلیحات آمریکا وابسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143876" target="_blank">📅 13:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143875">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry3mHCcVJPERGpr9pee_GCv11k_jF-ZPmR7DKbJBuU-S0KtJ-MC0uY2FQAM7bzXbK-y_9u3u2h6bYyGiGB31TzoPHPINH_ixT3UJy1CF0zk8dCg7jrD4k2cdug6V1CwE0OlJUPM96y_ggdv4kJqjR7604lk1pwLwGmrqbcElp4mea1b9DvSvvcI9rpp2SO4SlYFp930Svq77CAR5j6vU_ooZcYHrAzMrUwZ3bczCo3bAFUFNXINbYdxRRZ3esoFR2FLuxWGmIhkFauOGuuSGsVAvlBcrOKws_eVlh2nsndQlPUn4D4bETKEfk8vLCawWGi1eUaIsUJhv6EVh3P4I2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله علی کریمی به طرفداران پهلوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/143875" target="_blank">📅 13:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143874">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=gqIiKcSj-RMa22PtLi_wnFCb7vEYK3R4jnHNAh28u6A8TgVGJF223RGCqhfjPN7MqjHB1H_QMMOb4TnwzPpqxkmOQBaWqTnMvqqXnXs_AxYUeWn5eo2oW4jTEkNPkV5uQX-IxaFYkxZoANSMfOPGimIJEVkZ3lNumIeapct5pHr4hoG1Lawpmuih-fK92sRSKFyUFXD4dhjMc3wBN8CUKa2IrofZc1LBNFBdras0AwoBsPb6LEEV9LJfjRb25cu14oi0RLMPsXVD5fPXmXAgO7hXGLZvh2neJ7uE_qWNVG-qfvHUxFpq-p1VIShoXTLVPtzEK0ITlm43Q0PlKqWwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=gqIiKcSj-RMa22PtLi_wnFCb7vEYK3R4jnHNAh28u6A8TgVGJF223RGCqhfjPN7MqjHB1H_QMMOb4TnwzPpqxkmOQBaWqTnMvqqXnXs_AxYUeWn5eo2oW4jTEkNPkV5uQX-IxaFYkxZoANSMfOPGimIJEVkZ3lNumIeapct5pHr4hoG1Lawpmuih-fK92sRSKFyUFXD4dhjMc3wBN8CUKa2IrofZc1LBNFBdras0AwoBsPb6LEEV9LJfjRb25cu14oi0RLMPsXVD5fPXmXAgO7hXGLZvh2neJ7uE_qWNVG-qfvHUxFpq-p1VIShoXTLVPtzEK0ITlm43Q0PlKqWwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: تو جنگ اخیر ۱۰تا ژنرال اسرائیلی رو کشتیم اما به دلایل امنیتی خبرش رو نگفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143874" target="_blank">📅 13:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143873">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKHoBDMvLaBiTFLcuG9stGZ12BisB8T22WjccnLSkGNL21K6lbaINdLMEGKRvr732tXnGD4tVOoXYsurby3mQoLCWlInRDUm5VT4F5-bccNLHC70Udc074yzVgyTiB_zhwNCaNw3q5YvTTAwDYurLbT2fFU8UPxfms4937X39MF91OOLS5lazgxvh4H_ge8XJjjXqawSxr1-6KOcTInCJJqKpnWmYxhw4V-t8oWgd4ZK4ved26ccSUI2aENgmW_PbhkEC_U0JWrmxPMmi9jiezu3lcjMxEEzB-G7JOswyZOzwf-eF-v1mS_xl0C5qTI79lWn8OcXbUuljij8JRtnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بلومبرگ: به گزارش‌ها، آتش‌بس بین آمریکا و ایران در حال نزدیک شدن است
‏
🔴
بر اساس گزارش خبری که به منابع نظامی پاکستان و ایران استناد می‌کند، آمریکا و ایران به توافقی برای آتش‌بس دست یافته‌اند و انتظار می‌رود در روزهای آینده این موضوع اعلام شود.
‏
🔴
این توافق گزارش شده، شامل آزادی تردد در تنگه هرمز و از سرگیری مذاکرات تحت "مذکر اسلام‌آباد" است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143873" target="_blank">📅 13:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143872">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پزشکیان: بنای ما تفاهم و حل مسائل از طریق تعامل و مذاکره است
🔴
با تمهیداتی که بخش‌های اقتصادی دولت پیش‌بینی کرده، آمریکا کاری از پیش نخواهد برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143872" target="_blank">📅 13:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143871">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
قالیباف در دیدار با رئیس شورای عالی قضایی عراق: آمریکایی‌ها به وضوح شکست خوردند و همه دنیا بر این موضوع صحه گذاشتند؛ آن‌ها در اقدامات اقتصادی نیز شکست خواهند خورد
🔴
اگر اسرائیل در جنگ با ایران موفق می‌شد، به سراغ سایر کشورها می‌رفت
🔴
ایران در نظم منطقه‌ای می‌تواند نقش تعیین کننده‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143871" target="_blank">📅 13:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143870">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
بلومبرگ: فشار اقتصادی ایالات متحده بر ایران، تأمین انرژی ترکیه را تهدید می‌کند. ایران در سال گذشته حدود ۱۳ درصد از گاز طبیعی ترکیه (۷.۷ میلیارد متر مکعب) را تأمین کرد و پس از روسیه، آذربایجان و ایالات متحده، در رتبه چهارم قرار گرفت.
🔴
وزیر خزانه‌داری، بسنت، از مجازات‌های اقتصادی برای تجارت با ایران پس از یک مهلت نامشخص هشدار داد و اشاره کرد که ترامپ با رهبران، احتمالاً از جمله اردوغان، در تماس است. تحلیلگران پیش‌بینی می‌کنند که ترکیه برای تضمین معاملات F-35/F-16 پیش از سفر اردوغان به واشنگتن، با ایالات متحده همسو خواهد شد.
🔴
اگر گاز ایران قطع شود، ترکیه واردات LNG (از جمله از ایالات متحده) را افزایش می‌دهد، تولید داخلی ساکارا را تقویت می‌کند و از تأمین جدید آذربایجانی از سال ۲۰۲۹ استفاده خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143870" target="_blank">📅 13:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143869">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بر اساس گزارش Reuters، صادرات گاز طبیعی مایع (LNG) قطر به دلیل مسدود شدن تنگه هرمز به‌شدت کاهش یافته و افت آن به حدود ٩٩ درصد رسیده است.
🔴
قطر تاکنون حدود ٢۴ میلیارد دلار از درآمد حاصل از فروش گاز را از دست داده است؛ در همین حال، افزایش صادرات LNG از ایالات متحده تا حدودی این کاهش را جبران کرده است.
🔴
هم‌زمان، ذخایر گاز در تأسیسات ذخیره‌سازی اروپا در پایین‌ترین سطح خود برای این مقطع از سال قرار دارند و این وضعیت خطر افزایش ناگهانی قیمت گاز پیش از آغاز فصل زمستان را افزایش داده‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143869" target="_blank">📅 13:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143868">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">امروز ۴تا تخم مرغ و یه سوسیس گرفتم ۵۰۰تومن و کلی خوشحالم
[اگه ناراحت باشم اعدامم میکنن]
🐸
🕺
🐸
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143868" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143867">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سخنگوی دولت: از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
🔴
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143867" target="_blank">📅 12:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143866">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=YpmeysorVxQ3PdGjj7qfBZmhYFt-L17eS5Ot-rN3uUlKygP1kSBD5HEX0gOMEm9faDhJp7-FfMvDzpnaU_WLXXu_rPb7eW4ejc2PJ44hpmBZG5hAgCtaGYSNm9tG8fgwn2NH8a3E_pwTd3TWn0VyeUsOLmhcWGN1qCjk5W6VYnP8SHLS3Z47RkKdqzM9obvt6cJS_BR-p7x4T2-jroDRgx45tnEJHa8miNSMgaysFwHVLpQeDMbkjDVxPOPLuKiT-gMNu8iBQ1FwjdyT4zA_osMNGyzOM2SgxMUWYPvNDhHZHQSaa1F13u9YnwqZXg7k7YS67PuF-KCx9LooihsYbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=YpmeysorVxQ3PdGjj7qfBZmhYFt-L17eS5Ot-rN3uUlKygP1kSBD5HEX0gOMEm9faDhJp7-FfMvDzpnaU_WLXXu_rPb7eW4ejc2PJ44hpmBZG5hAgCtaGYSNm9tG8fgwn2NH8a3E_pwTd3TWn0VyeUsOLmhcWGN1qCjk5W6VYnP8SHLS3Z47RkKdqzM9obvt6cJS_BR-p7x4T2-jroDRgx45tnEJHa8miNSMgaysFwHVLpQeDMbkjDVxPOPLuKiT-gMNu8iBQ1FwjdyT4zA_osMNGyzOM2SgxMUWYPvNDhHZHQSaa1F13u9YnwqZXg7k7YS67PuF-KCx9LooihsYbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
🔴
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/143866" target="_blank">📅 12:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143865">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
همه کافه‌های پایین مجتمع ونک‌پارک امروز پلمب شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143865" target="_blank">📅 12:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143864">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/143864" target="_blank">📅 12:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iiARmOUbJJ35kHVE6kGGbJU0tbditsvIBHYHlNSdJH0VOwAXlUQLRw-ysWC__jzDIGu2jBXk4sHAD4Gl9RZr7OCANfDKK24tEsTxNDLpDPY47Wf8_r_7gAUmFWwVCBOk2z4dY_qX3HkJaNDXaM3R6eaSdT449eSwvG9lP9XZDYruC-XdzzFfe4ZEX4y6EZaWZSldiSM2FLFigjS-CG_5mNODrcIMpRqYTwD_gwQ_6Ez89tSs5OruuZ2dkbEU0KiednQvqT1POOFN9Pt_QfEg5q9dI_-2sjJJ-_AUkn5qMAh1pZJKAa3DPelIezMfiLylRty-rxHEIgxLF_kyElMsfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c46o6oc7-7SqgSjS8rOiCIqyT1uQp9R_SmqytEKcvJZLRKBv2TZ081nNkJMRpxozj7dNtaOeQTtb99IkA7tUSXYWfzdRHX-siuSe16f2CNEgkqSIID7C5N6Wqhb8RIJcn4Y2gM0IHvVupBrXYiuUqk7tMsz3FI9IqGChp_dEtV6v-FkFv4ZzZ-40eASWaGJcEEzL1YAdTJQpWnfsIR8CjKpP0jetDrNCHr0tSGN7rm2coT14BA8cBg0Ki7-aURc3HvEnlYIFImrHXX0gnoeipa1h8KGpNx1XdwEaxf_mmR3ISaine8l2E_o5Fr1RQJPzLKOsX3PTtAX9ptDy1nNtBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری/دولت ایالات متحده ویزای هادی چوپان رو به دلایل نامعلوم صادر نکرد
🔴
چادی در مسترالمپیا غایب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143862" target="_blank">📅 12:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: می‌خواهم به شما بگویم: هنوز چالش‌های پیش رو داریم.
🔴
چالش ایران به پایان نرسیده است.
🔴
ما همچنین باید چالش در غزه، در لبنان و در سایر عرصه‌ها را به اتمام برسانیم و برای انجام آن عزم راسخ داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143861" target="_blank">📅 12:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17ef710e9.mp4?token=AJ7evRMs-YF83rE2D0iXBAoQzAvHAth3KO-EU187SSgjWqiI86gQxU2RXh20PGfnXekqSQ_dNppjuq6DvD_20CfSQWJ4r4shylRfp6gl4NPOG_Bd94QG2LZHfWOeZQjtkxSdqqi1lbMW_sIsB6jDb-xn7Bl3tBSWMS090awo2_gNcF5x0gfLAe9aLngxD4tnPTqY03EZUnC4lylXqhgSfFznKH1tXWulC7dyIxWI1DMwB0oVR15ZXAvn7lmUXsevwPBgy35B6Txtmf8A3gy_NMKlI0tcyOTM2ff0jsNtC8RWkPNVVACPANAzDsTonywCMNMH-8Rv-T4wWeeDxKMd_wddJYdo_eO0Iam5gdeAPofaZrLS0Oh8TbMl1sDaubWKx92bc-H2iGaIFT8sTJhx7NfwBeNLn6_QewmekwSmjM9HEVW2CieWeTYYxO5zVGCVxCxCmqRZZX48ygowghNkNDS-WzOdWYEVrt-xdTtl1Bi2b5aVqXv8mHY1wTG_Z6ImNujZuLIbzYCBmbmbQunWcl5S5Ii6gJf5JhSNa7pqgZ9EffWwZHh7RP-osKcvGYGqJozKhK5FCLpGpt-cz18Tz5-VIDDOzvIG7MQxyQe2Yv8rY-Kf4t4dIrStDuhXFn-wpdm6usrDhVzu-pLPHg5vL7c78Fwoy-5aW9lDcXZbqMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17ef710e9.mp4?token=AJ7evRMs-YF83rE2D0iXBAoQzAvHAth3KO-EU187SSgjWqiI86gQxU2RXh20PGfnXekqSQ_dNppjuq6DvD_20CfSQWJ4r4shylRfp6gl4NPOG_Bd94QG2LZHfWOeZQjtkxSdqqi1lbMW_sIsB6jDb-xn7Bl3tBSWMS090awo2_gNcF5x0gfLAe9aLngxD4tnPTqY03EZUnC4lylXqhgSfFznKH1tXWulC7dyIxWI1DMwB0oVR15ZXAvn7lmUXsevwPBgy35B6Txtmf8A3gy_NMKlI0tcyOTM2ff0jsNtC8RWkPNVVACPANAzDsTonywCMNMH-8Rv-T4wWeeDxKMd_wddJYdo_eO0Iam5gdeAPofaZrLS0Oh8TbMl1sDaubWKx92bc-H2iGaIFT8sTJhx7NfwBeNLn6_QewmekwSmjM9HEVW2CieWeTYYxO5zVGCVxCxCmqRZZX48ygowghNkNDS-WzOdWYEVrt-xdTtl1Bi2b5aVqXv8mHY1wTG_Z6ImNujZuLIbzYCBmbmbQunWcl5S5Ii6gJf5JhSNa7pqgZ9EffWwZHh7RP-osKcvGYGqJozKhK5FCLpGpt-cz18Tz5-VIDDOzvIG7MQxyQe2Yv8rY-Kf4t4dIrStDuhXFn-wpdm6usrDhVzu-pLPHg5vL7c78Fwoy-5aW9lDcXZbqMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: و من به ترامپ گفتم که یک امکان سوم نیز وجود دارد: تشدید محاصره.
🔴
دیروز، او این تصمیم را به‌شدت، بسیار، بسیار، بسیار قوی تأیید کرد.
🔴
آنچه رئیس‌جمهور ترامپ دیروز انجام داد، تشدید محاصره علیه ایران بود — نه با تشدید محاصره خود ایران، بلکه با تشدید محاصره علیه کسانی که به این رژیم، این دیکتاتوری وحشتناک، کمک می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143860" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: به ترامپ گفتم: یکی از احتمالات، البته، این است که با ایران به توافق برسید — یک توافق خوب. ما اعتراضی به این موضوع نداریم.
🔴
فقط شک دارم که آیا می‌توانید با آن گروه آنجا، با آن وحشیان، به توافقی برسید. به شما می‌گویم، نمی‌توانید با آن‌ها به توافقی برسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143859" target="_blank">📅 12:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143858">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f0422250.mp4?token=eYAX-JHJl7UyU5DH82JawWA3LPd8CAaVu5I1tcE_UJgjeUgSVCDrM_EJOcJs5IdF86wgAdGdzy6xXcM6cS8UGhZ_KOI2a1MQJOflfg298mdT3EwXfBblcp4VfMtdhhx8zcSqFe36o3x3BOn8GbA2wgATvxghijuituyFwfT4UyzQWDgONhPZdthtFuNaNAxnVPnIfFh1GfHFJea5IBRsFunV9dKIujHznFVVAR0VufCrOFBG0BV1Q9yGpkgfsCG0N5CGhL1pesPrutoYNE9aw0FbLhYLg_HYdp9ApwbjbyEJm6LARg4jRSTYc_W5FLvNejY5PZcModjAT7YyW2Jyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f0422250.mp4?token=eYAX-JHJl7UyU5DH82JawWA3LPd8CAaVu5I1tcE_UJgjeUgSVCDrM_EJOcJs5IdF86wgAdGdzy6xXcM6cS8UGhZ_KOI2a1MQJOflfg298mdT3EwXfBblcp4VfMtdhhx8zcSqFe36o3x3BOn8GbA2wgATvxghijuituyFwfT4UyzQWDgONhPZdthtFuNaNAxnVPnIfFh1GfHFJea5IBRsFunV9dKIujHznFVVAR0VufCrOFBG0BV1Q9yGpkgfsCG0N5CGhL1pesPrutoYNE9aw0FbLhYLg_HYdp9ApwbjbyEJm6LARg4jRSTYc_W5FLvNejY5PZcModjAT7YyW2Jyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: امروز، بسیاری از برادران و خواهران ما در سراسر جهان درک می‌کنند: این سرزمین ماست و سرزمین دیگری وجود ندارد.
🔴
و وقتی می‌گویم «سرزمین ما» — هر یهودی، هر زن یهودی — درها باز است.
🔴
ما در دولت اسرائیل، در قلب سرزمین اسرائیل، منتظر شما هستیم و شما زمینه را برای موج بسیار بزرگی از آلیاه که خواهد آمد، آماده می‌کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143858" target="_blank">📅 12:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143857">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نتانیاهو درباره طرح اوگاندا: هرزل طرح اوگاندا را پیشنهاد داد زیرا، مانند یک نبی واقعی نسل ما، درک می‌کرد که قرار است در اروپا چه اتفاقی بیفتد.
🔴
در اوگاندا، هرگز نمی‌توانستیم شور مردممان، چشم‌انداز نسل‌ها و آرزوی بزرگ بازگشت به صهیون و سرزمین اسرائیل را شکل دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143857" target="_blank">📅 12:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143856">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=L44K5Kt5_nVdH_ox8t9iv18PaF_RBe_N67-HTuIOpMevyqHysu-wMDF6tMppQIAPRCr3eh8dCyW3VTlWOvAKZHaDWXVvWonAsLCSsbh9yGm-opkck95en9UUGRVx42Bu6TzWEh1kPeEtq1C-ywG1f1a9zUMgK1JeTURHE5U3BPjI9ZHsBdio1OIR3IJXOsVNkxrG0ri_cyuHFcUSzhzzQ1K4P1mCaxhHTX_0wvbybCNCvME8t6y5uasxv1nP-hKbiE0ZPokpMwvWgtAxirbymRIDEV-6N_fDq0Tx8XDPd3Pl_eoL9uoRROq-5iDmuxlPtn36LxfxDWTNl4YpZujWpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=L44K5Kt5_nVdH_ox8t9iv18PaF_RBe_N67-HTuIOpMevyqHysu-wMDF6tMppQIAPRCr3eh8dCyW3VTlWOvAKZHaDWXVvWonAsLCSsbh9yGm-opkck95en9UUGRVx42Bu6TzWEh1kPeEtq1C-ywG1f1a9zUMgK1JeTURHE5U3BPjI9ZHsBdio1OIR3IJXOsVNkxrG0ri_cyuHFcUSzhzzQ1K4P1mCaxhHTX_0wvbybCNCvME8t6y5uasxv1nP-hKbiE0ZPokpMwvWgtAxirbymRIDEV-6N_fDq0Tx8XDPd3Pl_eoL9uoRROq-5iDmuxlPtn36LxfxDWTNl4YpZujWpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: تا آخر شهریور هیچگونه تغییری در بنزین 1500 و 3000 تومانی نخواهیم داشت
‏
🔴
مهاجرانی: تولید داخل و ذخائر استراتژیک بنزین مناسبی داریم و جای نگرانی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143856" target="_blank">📅 12:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143855">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ارتش: قطر از سرنوشت خلبانان ایرانی اعلام بی‌اطلاعی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/143855" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143854">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نتانیاهو دربارهٔ شهرک‌سازی: واقعیت پیش چشم ما در حال تغییر است.
🔴
دیروز با وزیر دفاع و دبیر کابینه بودم و اولین چیزی که می‌خواستم ببینم یک نقشه بود.
🔴
وقتی نقشه را می‌بینم و نقاط، نقاط، نقاط، نقاط، نقاط را می‌بینم، می‌دانم که ما نه تنها وجود خود را در حال حاضر تضمین می‌کنیم؛ بلکه وجود ملت یهودی را در آینده تضمین می‌کنیم.
🔴
۱۶۰ ایستگاه پیشرو، ۱۰۴ جامعه که ما تأسیس و قانونی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143854" target="_blank">📅 12:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رویترز: تقریبا نیمی از نفت جهان در سال ۲۰۲۶، از کشور‌هایی جریان می‌یابد که درگیر جنگ بوده‌اند
🔴
درگیری‌ها در خلیج فارس و اوکراین ظرفیت پالایش جهانی را حدود یک دهم کاهش داده
🔴
قیمت‌های بالای سوخت، به افزایش بدهی‌های آمریکا به ۴۰ تریلیون دلار منجر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143853" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گاردین:پس از عملیات نظامی جسورانه برای ربودن رئیس جمهور ونزوئلا، نیکلاس مادورو، غرور ترامپ را فرا گرفت و او تصور کرد که پیروزی مشابه و سریعی در خاورمیانه در انتظارش است، اما این اقدام، زخم عمیقی بر حیثیت ملی آمریکا وارد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143852" target="_blank">📅 12:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
نتانیاهو:
دستیابی به توافق با ایران ممکن نیست‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143851" target="_blank">📅 12:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47002c575.mp4?token=AXQJbfIAS4BCL0Wb2aU7GO_k8ES9CB0o8s3lEpWRBJJUTaYoYx0G1lZOnrBXKb3CFg34LX1EtTARhiRdXtJ4A6iet4BGSBt5aqlJZHtGynKCYZUZairVZE99Pj94Q7VLGszFoUGZ-P8lgU0yfYRMmxupiA-SIG2cl2n-SUemLq3HPq1UVT7zPtwvfYhkjZ4y9baGQ5_o_mK107Av9eZ8VX5FNSwOzDdNzBJT_MxxZck42Y0kAICP2IaDUk0VDOdBmdTR1uWMdWyLxmlH7KX0FXvga6-1wfn_VyBpGWkrgtBwdvZjwEKKcOiyZfbTFVAZIFGz2Cdc55qdX2KCpGBoIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47002c575.mp4?token=AXQJbfIAS4BCL0Wb2aU7GO_k8ES9CB0o8s3lEpWRBJJUTaYoYx0G1lZOnrBXKb3CFg34LX1EtTARhiRdXtJ4A6iet4BGSBt5aqlJZHtGynKCYZUZairVZE99Pj94Q7VLGszFoUGZ-P8lgU0yfYRMmxupiA-SIG2cl2n-SUemLq3HPq1UVT7zPtwvfYhkjZ4y9baGQ5_o_mK107Av9eZ8VX5FNSwOzDdNzBJT_MxxZck42Y0kAICP2IaDUk0VDOdBmdTR1uWMdWyLxmlH7KX0FXvga6-1wfn_VyBpGWkrgtBwdvZjwEKKcOiyZfbTFVAZIFGz2Cdc55qdX2KCpGBoIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143849" target="_blank">📅 11:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143848">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI5leLsHi0nyTLm6EDwucFNcR8oNpWS3_UJh0w7WMtHDwQA3Pdy6ZTKPe8jj6MB4aE3K6MtjTp4gqce4zGiNe66gh9hD-OI7SJ6sP4hRcMy64Ty13eHdy4oJ7sb9-UK5isqIvfmx0lpEE2vFX4AsH16nKlbv9rDx5tXPdkiRH88K6MbJ1I_iBQmwIwOyAaY2SnGQZcULThw5q6B-w9WiBlxkS5NeMGo-JuV6z6SzDXlTzSwgkYOcAE1gTMcm9CN3wTd8bhRwXEbbyCnfWz93RaRReyHQsAsoPboAZ0m28PzNazpOZajnip-OkffLyeKouxMOHzcqk1iNRf-pynneQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی قبل زمین لرزه ای به بزرگی ۴ ریشتر در عمق ۷ کیلومتری زمین نوار مرزی کردستان را لرزاند.
🔴
کانون زمین لرزه مرز شهرستان های بانه، پینجوین و مریوان گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/143848" target="_blank">📅 11:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143847">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=mzLDMlpGECghsNyJ5P06F2s7WTbB7k-g-5M2-IdAvPO55xbPfsJYHc2sErhtgM9I1Y9WgU6uwk0XdgQ-QcITuHNAXhAsUwemrl-hregXrzkXJxEB7VhfysXfZPnpcxSiCaA8Wu-aV8ubej-RbClKN3AKcnblm2iIt35kjkIU2dvLfFgGs_GK83aRWOzRbbaLK2Cwe3ttzuwZBTrNqo6bl3GBtpSRLCoIm7MUZXwgeHFl3FJcxSAEBNwUmYr7Bk95YHMW0q85boax8H_-QGPg_Nif6Y4EBYIaeanosK2F9AulCZx-DAS9b7jOGlx8vIWwEpTD_LGFLhEQSSrnWGnz_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=mzLDMlpGECghsNyJ5P06F2s7WTbB7k-g-5M2-IdAvPO55xbPfsJYHc2sErhtgM9I1Y9WgU6uwk0XdgQ-QcITuHNAXhAsUwemrl-hregXrzkXJxEB7VhfysXfZPnpcxSiCaA8Wu-aV8ubej-RbClKN3AKcnblm2iIt35kjkIU2dvLfFgGs_GK83aRWOzRbbaLK2Cwe3ttzuwZBTrNqo6bl3GBtpSRLCoIm7MUZXwgeHFl3FJcxSAEBNwUmYr7Bk95YHMW0q85boax8H_-QGPg_Nif6Y4EBYIaeanosK2F9AulCZx-DAS9b7jOGlx8vIWwEpTD_LGFLhEQSSrnWGnz_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رکنا گزارش داده این فرد که بلاگر اینستاگرام هم بوده، عاشق ماشین‌های مدل بالا بوده و توی دیوار دنبال آگهی ماشین‌های گرون می‌گشته.
با صاحب ماشین قرار می‌ذاشته، می‌گفته یه دور تستش کنم و بعد با ماشین می‌رفته!
نکته عجیب ماجرا اینه که بعدش زنگ می‌زده و می‌گفته من دزد نیستم؛ چند روز با ماشینت دور دور می‌کنم و بعد سالم پسش میارم!
ظاهراً هدفش فقط لذت بردن از ماشین‌های مدل بالا بوده و بعد از چند روز هم ماشین رو سالم برمی‌گردونده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143847" target="_blank">📅 11:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143846">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=bZQ7QQHARTLsS1MVqY5T2vkZnIxV_ajtoy9clA48fToiz0bg2AMVixZa7M3fT3hq6gSNuRt3JcelM5ZJwtC7b4XWdrEP3nfIzxpZGo9IFUsGKAI_4qf886k8tiD7L0jF2sapxM3zExxGrsmxf9Jlm2AYffqutPyNah1VvoBMTkvjDRnITDvyaMkhG6gb9yKTA5Cna6KMWlofzEI1lVADfyXT6q3I-CQIxiAkp-LOweHo1EwVKlLPWQFmFYqWeFI1rRIVxoXJkXZecuylyMXCCDDgidjIVIbhL6alAmk1thm2nzQC141t3_37FEuwx1RdEqxXJyFLfQdWrikEW3c9Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=bZQ7QQHARTLsS1MVqY5T2vkZnIxV_ajtoy9clA48fToiz0bg2AMVixZa7M3fT3hq6gSNuRt3JcelM5ZJwtC7b4XWdrEP3nfIzxpZGo9IFUsGKAI_4qf886k8tiD7L0jF2sapxM3zExxGrsmxf9Jlm2AYffqutPyNah1VvoBMTkvjDRnITDvyaMkhG6gb9yKTA5Cna6KMWlofzEI1lVADfyXT6q3I-CQIxiAkp-LOweHo1EwVKlLPWQFmFYqWeFI1rRIVxoXJkXZecuylyMXCCDDgidjIVIbhL6alAmk1thm2nzQC141t3_37FEuwx1RdEqxXJyFLfQdWrikEW3c9Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رفسنجانی در سال ۱۳۶۰:
پهلوی همه همت و دغدغه ش این بود که مردم خونه و ماشین خوب داشته باشن؛ زندگی خوبی داشته باشن و ارتباط ایران با کشورهای جهان خوب باشه ولی الان دیگه اینا ارزش نیست و برای کسی مهم نیست و مردم دنبال معنویاتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/143846" target="_blank">📅 11:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143845">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
فلاحت‌پیشه: هیئت پاکستانی بیش از اینکه به دنبال احیای تفاهم باشد، حامل تهدیدهای جدید آمریکا بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143845" target="_blank">📅 11:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143844">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
روزنامه هند اکسپرس: تحریم‌های جدید آمریکا میتواند صادرات هند به ایران را به شدت مختل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/143844" target="_blank">📅 10:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143843">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkg1s6niUYDWivwVjUcZEMmlK-zJmA01Ml0_UR5Xf5pLfxbjouoJcwebdumq7xfDTgxZCxbLrc2SW9J_qmd_GoJ-KwRyA9UPhQMj3OxaoVISq0VFH_sx63W1gUuxYRvEm3bboh0qSp460axOFsYwxT8n3lVgTkILlKvnmZuwZJzssVsdAPW9Scs9-umazwelFywUjw5BFLykB9AXkWl4vdXm3pYNDRnOOpN4B5jpZqC6PJISShH90w9t6OW5JrfHkbAKYG1AaVWkrdNjsuhJCXn2kZmutsPmbC6PMeWpZn8AYL0sBJhtlevWtcSMmmBVC6Sm24aJsc39_WQljQzr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری خانعلی‌زاده، تحلیلگر کصخول، احمق و متوهم صدا و سیما بر مبنای یک توییت جعلی!
🔴
مارک کارنی، نخست‌وزیر کانادا در سخنرانی خود هیچ نامی از ایران نبرده.
🔴
پ.ن: البته مستمع‌های این نوع افراد هم همگی احمق هستن و استثنا نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/143843" target="_blank">📅 10:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143842">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6963f249.mp4?token=tkS719fV0koybNCjtZx0GuMozoeBzdI-sPgPizQLQMdEqLy_tu26go9TacVORdBD0Pjz9Hb5imxodqnwCxUj_sDmEBzx_fGgewT547M7kTbnDtnOPHQM8ZDYyZGvpW8bGyrTruwoElz9hz_EtCDTaqSXrEaoVm8hmnivSvGBnCPve3Xax8Ox-lGJmGutuvAqi63QcbZTal7MGfF50HdC-AcsR9tVvaf6TpadwpPkXR-IqdQIexfoczInHHUEgrJjtElpwQ9Uvlx_0DSuxOxbPMrM6JZ_0C9zbTMgwe1S8FtNny4rfVdy8-vFOCOvNy8BAoeZtPSNnwaIHj_NUfJ1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6963f249.mp4?token=tkS719fV0koybNCjtZx0GuMozoeBzdI-sPgPizQLQMdEqLy_tu26go9TacVORdBD0Pjz9Hb5imxodqnwCxUj_sDmEBzx_fGgewT547M7kTbnDtnOPHQM8ZDYyZGvpW8bGyrTruwoElz9hz_EtCDTaqSXrEaoVm8hmnivSvGBnCPve3Xax8Ox-lGJmGutuvAqi63QcbZTal7MGfF50HdC-AcsR9tVvaf6TpadwpPkXR-IqdQIexfoczInHHUEgrJjtElpwQ9Uvlx_0DSuxOxbPMrM6JZ_0C9zbTMgwe1S8FtNny4rfVdy8-vFOCOvNy8BAoeZtPSNnwaIHj_NUfJ1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز یادآور زادروز مردی است که نامش با شکوه و عظمت ایران گره خورده است؛
کوروش بزرگ
، بنیان‌گذار شاهنشاهی هخامنشی و یکی از بزرگ‌ترین فرمانروایان تاریخ.
🔴
از پاسارگاد تا گستره پهناور شاهنشاهی ایران، یادگار او روایتگر روزگاری است که ایران در اوج قدرت، تمدن و شکوه ایستاده بود.
🔴
زادروز کوروش بزرگ،پدر ایران و نماد شکوه شاهنشاهی ایران، خجسته باد.
پاینده ایران
✌️
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/143842" target="_blank">📅 10:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143841">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc01971222.mp4?token=vQLn-_NfeKkZjYwG4lDzvpuNElFy-mNcfaYLlEngWCzqMHKdoJOHqjmew_aVwGhGRNQNYIdj8GluCh6GHULP35PHXcYC86F2YSLUaNG95svTHhIWYgzcCFPwEHgGzmnP30iCDLXLbRCY4jysA6FfZtT-ewWiNbGmSpzKOTKCXMWAmqPWLN7nzUtbTQCaBsFYTmnxjGer2DrUF32-mYV-h2vRyshCEVuUYUw1SKhL-8NFDWV1jvBTNVcEoob_egFLzfNztFnOZsii8BKa1Y8Yf_B5kyO6VL4QIrY-Z2R2Xtv0gi42eU_YMGe1HgPljQWlBfrALnB55Th4OrUM_8uvYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc01971222.mp4?token=vQLn-_NfeKkZjYwG4lDzvpuNElFy-mNcfaYLlEngWCzqMHKdoJOHqjmew_aVwGhGRNQNYIdj8GluCh6GHULP35PHXcYC86F2YSLUaNG95svTHhIWYgzcCFPwEHgGzmnP30iCDLXLbRCY4jysA6FfZtT-ewWiNbGmSpzKOTKCXMWAmqPWLN7nzUtbTQCaBsFYTmnxjGer2DrUF32-mYV-h2vRyshCEVuUYUw1SKhL-8NFDWV1jvBTNVcEoob_egFLzfNztFnOZsii8BKa1Y8Yf_B5kyO6VL4QIrY-Z2R2Xtv0gi42eU_YMGe1HgPljQWlBfrALnB55Th4OrUM_8uvYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: انتشار اطلاعات میزان فقر مردم، نیاز به مجوز شورای عالی امنیت ملی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/143841" target="_blank">📅 09:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143839">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وب سایت نیوزماکس:چند ماه پیش، پسر نتانیاهو، به طور مخفیانه از میامی تخلیه شد. این اقدام پس از آن انجام شد که یک گروه اطلاعاتی ایرانی که او را تحت نظر داشت، شناسایی شد. این موضوع در لحظات پایانی کشف گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/143839" target="_blank">📅 09:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143838">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47002c575.mp4?token=HXYF0b35raXopXTHpYACUTGjqc02YKKhQWmkZpvWpTLeXDe9n_AshQHRoaD8oj5WddIJRHSfSwbO7-EHX2yAzuK405CxRqjxfFt8fBkFk7hrskh8w854KAOYMFmciEj8-QdxwVTtN9RPjl0K4yhw86onhBvaemu0eFvY6O-NXdr60o_3-RYBkz1wf1BpUQ33TCYgEclzzfhz5RcoV9k9GBKj-8HXsxEdJ1vYfL3atcLWUv1FFsZk3w12EJNH07baQ4lmnnc4ZNG4uOXs-3NOWDWdgg0WOmmcOVyuIqEKyuwmingVFSzykwtJPaMibwkcnPRTkuP_NEtfrLElEcYEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47002c575.mp4?token=HXYF0b35raXopXTHpYACUTGjqc02YKKhQWmkZpvWpTLeXDe9n_AshQHRoaD8oj5WddIJRHSfSwbO7-EHX2yAzuK405CxRqjxfFt8fBkFk7hrskh8w854KAOYMFmciEj8-QdxwVTtN9RPjl0K4yhw86onhBvaemu0eFvY6O-NXdr60o_3-RYBkz1wf1BpUQ33TCYgEclzzfhz5RcoV9k9GBKj-8HXsxEdJ1vYfL3atcLWUv1FFsZk3w12EJNH07baQ4lmnnc4ZNG4uOXs-3NOWDWdgg0WOmmcOVyuIqEKyuwmingVFSzykwtJPaMibwkcnPRTkuP_NEtfrLElEcYEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل
در تداوم حملات به جنوب لبنان ، اقدام به تخریب و انفجار در شهرک «مجدل زون» در جنوب لبنان کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/143838" target="_blank">📅 09:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143837">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اکسیوس به نقل از یک منبع مطلع:
انتظار می‌رود استیو ویتکاف و جرد کوشنر، نمایندگان کاخ سفید که هدایت مذاکرات با ایران را بر عهده داشتند، امروز چهارشنبه از فرماندهی مرکزی آمریکا (سنتکام) بازدید کنند تا درباره وضعیت میدانی منطقه توجیه شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/143837" target="_blank">📅 09:40 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
