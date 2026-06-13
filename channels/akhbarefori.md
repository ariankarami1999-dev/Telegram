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
<img src="https://cdn4.telesco.pe/file/AJCefhYXToWNNMcUTX4-BZFWYG05D-yhWIvFaNvKEjMXKqM9u6ZCnfsA6OaRiXbAQ2ehSJGT8Ebo8G2wy4zHvxufNF8OPcASXW-xSh3MJ3Qtx854btHJhMRPePueI9TXdQVjG7-EC__1lSHsZllmrwxd-QpFxAQ1zD2C1PDknKKePxhcTJtyyB1OZ5d9YLjHfYtUQac0595w6IEN5XM8f8NsXeK7MgfUdtUYzWM7vu30iENRuMgOhSAY12v3tGfzulhUVd9A2FTzWMv7ctVSHFNVR-gLWYklFRioEndxWf17WBx1XQaj7mUIxtq-519XOp2IFRoS9AWrPFvE-Q15Yg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.58M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-658888">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
الحدث به نقل از یک منبع بلندپایه: امضای «اعلامیه اسلام‌آباد» به‌ صورت غیرحضوری (از راه دور) انجام خواهد شد و دیدارهای ژنو نیز به‌طور موقت به تعویق افتاده است/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/akhbarefori/658888" target="_blank">📅 08:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658887">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
الحدث به نقل از یک منبع بلندپایه: امضای «اعلامیه اسلام‌آباد» به‌ صورت غیرحضوری (از راه دور) انجام خواهد شد و دیدارهای ژنو نیز به‌طور موقت به تعویق افتاده است
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/akhbarefori/658887" target="_blank">📅 08:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658886">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
آمریکا مدعی سرنگونی «چندین پهپاد ایران»
ادعای سنتکام:
🔹
چندین پهپاد تهاجمی ایران را که می‌خواستند به کشتی‌های تجاری در تنگه هرمز حمله کنند، هدف قرار داد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند.
🔹
ادعای سنتکام در حالی مطرح شده که ایران اعلام کرده که عبور و مرور از تنگه هرمز تنها با مجوز نیروهای مسلح جمهوری اسلامی ایران میسر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/akhbarefori/658886" target="_blank">📅 08:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658885">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16b06d3d4.mp4?token=k-ALCnHdVvl4f35EIVYVb1EdlaK_Ucc3tESz6uykY6jPmbEFk0ucgr1eo_2o8foN7ZLY4AqpUnmTc8teQHU3IzbshsQ1G7mirxYCnrPtRQLTXz5LYfeCcGNl6w3dOOXCNZQ-3_mcDYBuQ4gBkmJthaTlYryhE9nPJ1-X7aq4tcJoTcb-o5dPA6GpKlsXWZWx7Jg4w8MnjcOX6tc5u6gSTdN8-Slz_iTvjopCoCxDGbvXdTA9CvTICWBtIKIk2WyLf_jQgOE0WZl3LKCxnklSOO_IVjZmaNqYWXSKOHXztngJ2-9FZG63qSWsUUvOeDVMXR6jRnVfSLfBQKA61O8mIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16b06d3d4.mp4?token=k-ALCnHdVvl4f35EIVYVb1EdlaK_Ucc3tESz6uykY6jPmbEFk0ucgr1eo_2o8foN7ZLY4AqpUnmTc8teQHU3IzbshsQ1G7mirxYCnrPtRQLTXz5LYfeCcGNl6w3dOOXCNZQ-3_mcDYBuQ4gBkmJthaTlYryhE9nPJ1-X7aq4tcJoTcb-o5dPA6GpKlsXWZWx7Jg4w8MnjcOX6tc5u6gSTdN8-Slz_iTvjopCoCxDGbvXdTA9CvTICWBtIKIk2WyLf_jQgOE0WZl3LKCxnklSOO_IVjZmaNqYWXSKOHXztngJ2-9FZG63qSWsUUvOeDVMXR6jRnVfSLfBQKA61O8mIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تمرین زانو که برات معجزه میکنه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/akhbarefori/658885" target="_blank">📅 08:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658884">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qm9jZrrLHpxng23h4P-TkuvrtCZdIGQ6DC9B6WQZZljYzfAXNc7sTovgu4vhJnuTDgwbD6WOiv6wpraV-zOEZ4YEsNYaA89-4xP7cepYFfa7D296eKZ9RjaPVjLxP9BkwhP5yzKoIOhklrt8ODaEqHETo92EL4SJUelwuLSCyk9H_jxQA9kpMkeyQmHukTqMAgeNV7SOCAKOOo_EnVOgSVPfVVpYkMI9fsq0-sajRnXk36Ir4OkMXEHv3-8V2Ba5wgnFrWlzvL0wN0xGH7-leKTc-Ptr_U22ucZRo96z346bx1wP2zCUgS2OCUVOMUmWgmIkBEINjjb7wJwlNPWzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: توافق با ایران تا اوایل هفته آینده نهایی می‌شود
وزیر خزانه‌داری آمریکا:
🔹
با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران احتمالا تا پایان همین هفته (میلادی) یا اوایل هفته آینده نهایی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/akhbarefori/658884" target="_blank">📅 08:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658883">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رافائل گروسی برای دبیرکلی سازمان ملل اعلام آمادگی کرد
🔹
مدیرکل آژانس بین‌المللی انرژی اتمی اعلام کرده است که برای تصدی دبیرکلی سازمان ملل متحد علاقه‌مند به نامزدی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/akhbarefori/658883" target="_blank">📅 08:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658882">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/658882" target="_blank">📅 08:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658881">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3edcbbf56.mp4?token=qDF552N8E-Xj8apSvDm_tK7xDNTGKpxVJEErdFbPwTgyz-4t0NVDGx_ZRU55SBI6-zjWTwhvj02msXsgoU9Kej1Yeoq6ViL_o2PnoPsYkZ9c1ZdrNnZ0jqAB-Yu8J5q2xUym-UhjDhpva1GjgO_1tC99ZsuCvDBWfjjw3CdvEu4wAyFfzbGR7dD3AQowWV9HExXU8sgqFjfcqYRxnjpLiVUifhVaVPKkLIdim3Bm0b66yKg_sNichfTr1GC6h55W-hLukymD1oVFR2VfrePEM70YoF-KtQNhl4xUvpCo_YQ4Rkf2z7wbpGuLwQ1B5owMIx82881Qn3PGNokV7eZ5SWzwMIs4BP8rosiE3gUNoaZ-g20tSPfcqyr4QkeEDfw1gxAOnfMePJ0YntaAiskKyUUURPEy6S9ls9x0ReHRcI7QMFNslEDs_YOg3k9ccDo5MaFfK7OIp_4x5DF-p_9LP3L_DgpEotJ8HQqC2zvF2nEEndhgXIGmn-EGI8ZHUAGavw-k38AjvpE-OKYwJh2mZ8mKSI0Xi4ZZyd9ex36b-Vw5tnLatty-3jPSA1QgeE3JdCnN_vbEFAwdeM2LoYxLgCQHkVB6pplBV1pLpxtwGme8rg0--ycb8uImD2Zq6Qlm_szxSIASAjspO7RBW7tuarHI_VGp1Zo0JjbpgHg5cyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3edcbbf56.mp4?token=qDF552N8E-Xj8apSvDm_tK7xDNTGKpxVJEErdFbPwTgyz-4t0NVDGx_ZRU55SBI6-zjWTwhvj02msXsgoU9Kej1Yeoq6ViL_o2PnoPsYkZ9c1ZdrNnZ0jqAB-Yu8J5q2xUym-UhjDhpva1GjgO_1tC99ZsuCvDBWfjjw3CdvEu4wAyFfzbGR7dD3AQowWV9HExXU8sgqFjfcqYRxnjpLiVUifhVaVPKkLIdim3Bm0b66yKg_sNichfTr1GC6h55W-hLukymD1oVFR2VfrePEM70YoF-KtQNhl4xUvpCo_YQ4Rkf2z7wbpGuLwQ1B5owMIx82881Qn3PGNokV7eZ5SWzwMIs4BP8rosiE3gUNoaZ-g20tSPfcqyr4QkeEDfw1gxAOnfMePJ0YntaAiskKyUUURPEy6S9ls9x0ReHRcI7QMFNslEDs_YOg3k9ccDo5MaFfK7OIp_4x5DF-p_9LP3L_DgpEotJ8HQqC2zvF2nEEndhgXIGmn-EGI8ZHUAGavw-k38AjvpE-OKYwJh2mZ8mKSI0Xi4ZZyd9ex36b-Vw5tnLatty-3jPSA1QgeE3JdCnN_vbEFAwdeM2LoYxLgCQHkVB6pplBV1pLpxtwGme8rg0--ycb8uImD2Zq6Qlm_szxSIASAjspO7RBW7tuarHI_VGp1Zo0JjbpgHg5cyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری معروف روس از خجالت اروپایی‌ها درآمد
🔹
۱۶۸ کودک ایرانی کشته شدند، صدایی از شما درنیامد، هیچ تحریمی علیه کسی وضع نکردید....
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/akhbarefori/658881" target="_blank">📅 08:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658880">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOiR_XUrS8-f6QBSIHwmoNTvCybInaTSijUEKB5qWaHBPpyj3m5XsEfupiusMVkErude8r27gMoec9vtgNvyHIF4JfdKWcg7u415m9F0gwbg1qIR94DVS-7aukEXCOg0LqxPOvq6_GBHYPDEjC7T8vkj7aP6HcASu0ER9CyQZmiUWxL6mlz7dOgBM20JGztdRoabnjRM6BlG2rseXVDZ3JovxNH_eMmrKrZ8XB8LKRvI6ooTVdqWJ5PAalus85snSiUoQ8TNivgeLe5o_hvvewXQ9HC56VniKp_kNCiIcEpFjTjMAX3vgJcxlJ-fZDOQeFNnKU-_0r97UuknQh3kyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول گروه D جام‌جهانی ۲۰۲۶ پس از پایان اولین بازی این گروه
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/658880" target="_blank">📅 07:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658879">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: رفع تحریم در ازای اقدامات ایران در خصوص برنامه هسته‌ای صورت خواهد گرفت
وال‌استریت‌ژورنال به نقل از منابع آگاه:
🔹
واشنگتن تأکید کرده است که هیچ گونه لغو تحریم یا آزادسازی دارایی‌های ایران پیش از اقدام مشخص این کشور درباره برنامه هسته‌ای‌اش انجام نخواهد شد. هرگونه منافع اقتصادی برای ایران منوط به «راستی‌آزمایی کامل» پایبندی تهران به تعهداتش خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/658879" target="_blank">📅 07:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658878">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
رسانه عبری: آمریکا در حال احداث پایگاه بزرگی در نزدیکی نوار غزه است
ادعای یسرائیل هیوم:
🔹
ارتش آمریکا، احداث یک پایگاه بزرگ را در امتداد حصار حائل اطراف نوار غزه، در نزدیکی پایگاه «رعیم»  رژیم صهیونیستی آغاز کرده است.
🔹
قرار است از این پایگاه به عنوان مقر نظامی و غیرنظامی برای نهادها و نیروهای بین‌المللی استفاده شود که به منظور آنچه  پیشبرد «طرح ترامپ» خوانده شد وارد منطقه شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/658878" target="_blank">📅 07:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658877">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1c9a800e.mp4?token=h11K4ywxcJbTD2VPTjuffP1x0W73C3cOFlUC5aoCyn3hMHM_drjhkACLKvz5wLGCwlvjkrQO8zrfSa-u2TY8l5Zfilly7Y1WF34Tyv9eCvho7Gt54fwldbdqzo31jJmat68DVU1eWyegL5hWV_jRUdOIv3Ych3LGiFwz9NKF-2mlMVDlP_tR54UN16NMCHVVBRkfDpYwn0NCBs4joWvBSS9TTunqGcJrOu_4OXnmQpgRwr0kj2iJ3hP3Kv7H_wAFQYq1fptVAAgLQ_jmQ0j7oKdVVHFBFzyDmn5i0pOfUD8oUa6bxQ3XErJmIaWj5sR9PYA3Ymox-bGM0mMzmY47iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1c9a800e.mp4?token=h11K4ywxcJbTD2VPTjuffP1x0W73C3cOFlUC5aoCyn3hMHM_drjhkACLKvz5wLGCwlvjkrQO8zrfSa-u2TY8l5Zfilly7Y1WF34Tyv9eCvho7Gt54fwldbdqzo31jJmat68DVU1eWyegL5hWV_jRUdOIv3Ych3LGiFwz9NKF-2mlMVDlP_tR54UN16NMCHVVBRkfDpYwn0NCBs4joWvBSS9TTunqGcJrOu_4OXnmQpgRwr0kj2iJ3hP3Kv7H_wAFQYq1fptVAAgLQ_jmQ0j7oKdVVHFBFzyDmn5i0pOfUD8oUa6bxQ3XErJmIaWj5sR9PYA3Ymox-bGM0mMzmY47iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از قانون جدید VAR در جام جهانی ۲۰۲۶
🔹
دخالت در کارت زردی که در بازی آمریکا -  پاراگوئه به اشتباه داده شده بود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/658877" target="_blank">📅 07:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658875">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vu-e-OKfy_XzK3e51Up4VokZwTdD8h1NRaXChQsWMC57X301bKx7q6gYYSOtwtgwexIrJ7jHa3iOa5YbpxuNgLvZHUXh2eGemgs1jU3CzVEhbVn3AoLyFSoIqk3VEn2y-r2jyCvucpa3avfm9yxq0uo2ld4umQslfB_pi7V8GWfoCebFvQrLbBvfkqmh4E0RFHUslIj7bJTPmXFOiZHMAvmTqD8U6dYOgTLOytpohnShtjJ9C11d1JOcYTQMqpOWl-eJN3KPaZKkqaoUd87MqniSw-QUWj49OPmuvX_cOaigr6SrLcAb7i7WdQFHoY8FCmZN-BLCoxnxODLNIZMYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPKCz4nEQLo7d3jKWMBDTcnsq8q23R70RaD5X6Ql5alC-d8xmaRF40eV9JMtnVaXuiHZ-71PN5NvJKn4MxPekYhclSdOoffFriVZXqdJvk2rLop8hSBJuI_YVU4qg2yHCr6ieuskD4SmcDft0FY1nNLl7-qewtLl1xEC3zbLJPE_BXuksN-oTEmJkIRNkcDNal4e6t247-4OJtzLzjxUFuqHQf-ba2hKRS7jlogAvSGFQIEpQs-9rPrpXA06NDwf_4YWFtUdEilZSj6DeAqRYdOad3dLG72GObnBCNOKJHvp6kgBUpNGpeodjWtjnJXFVf-6q5KAAAIQyQP2LrTpmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کشف یک جسد در نزدیکی ورزشگاه تمرین تیم ملی فوتبال ایران
🔹
خبرگزاری فرانسه (AFP) گزارش داد که جسدی در حال پوسیدگی درون صندوق عقب یک خودروی پارک شده در نزدیکی استادیوم کالینته (ورزشگاه محل تمرین تیم ملی ایران) کشف شد که در حال متلاشی شدن بود! این خودرو در پارکینگ فروشگاهی نزدیک ورزشگاه «کالینته» قرار داشت.
🔹
دفتر دادستانی کل تیخوانا با انتشار اطلاعیه‌ای اعلام کرد که این جسد در جریان یک گشت نظارتی کشف شده است. در گزارش اولیه آمده بود: « مأموران گشت هنگام بازرسی خودرو، متوجه حضور فردی در صندوق عقب شدند که درون یک کیسه سیاه پیچیده شده بود و آثار ضرب و شتم روی آن دیده می‌شد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/658875" target="_blank">📅 07:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658874">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ثبت‌نام سرویس مدارس آغاز شد
🔹
والدین یک‌ماه فرصت دارند تا درخواست ثبت‌نام سرویس را در سامانۀ سپند به نشانی
irtusepand.ir
ثبت نمایند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/658874" target="_blank">📅 07:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658873">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXRH45rq1IGJlaZhcUWn8Vuctkb-ufltE-E81Qfq8tiiAo18VcIxXvDyJCjwMndAUXSF2dEtJCbnU4Arcf0srcPfaV2NgsuMa-XzZdRN9oRV41g--jPr6I4tk-7K6JeJWD_qh-imio1dFNHDgRj8HE9YEVCns9gckLbbBksFGDT8PgoAxFruEgrzmQF5GLDGl5pojGkfamSpNSvXwcKTOKBEAcycsJmdtcsb_PKL7b60agYc32pCLs1ESCjz6rL1jh6V8rK3DBXwBSonIEAIqfvPk6IkxWt5E7nRI4-By39Kk7cR6y8B5jHLO_AHFRNTH_XBudq90GpR_vTGEow6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین پیروزی سروقامتان ایران در لیگ ملت‌های والیبال
🔹
ایران ۳ - ۰ آرژانتین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/658873" target="_blank">📅 07:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658872">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG-aPnhV6vGOdsUjesCmSQNO9kJiGo1TAla0uJJmf14T6rVXNYCNWxWFSumzF7CRe6WbAj3Dfq5JD2S02kAtstW_l4isCon2Zm4HFir43eLUdb7qzaMu2N3ftcQfFej_SRPkxoJjI2sRsJb-sGmDbiSgUUb_erxBcerGQEB_OiOvsToGm2qJvr6zaZgZ072JWma-o9CZeu-2c2IKu3QNF2PEiPjNbPB_OHIsmWSs0bkj1mSK0DsVNVMqmV3eheeHD1xUXvEL0u3dshx-GZYZjNwTeCYOC_5-m6L93x4rETdkNBdbQXm7FdQ0OmgNgUkUchahOXZJO2DL-0g2gFMqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امارات ادعای رسانه‌ای در مورد انتقال وجه به ایران را قاطعانه رد کرد
🔹
امارات متحده عربی گزارش‌های برخی رسانه‌های بین‌المللی در مورد انتقال یا تحویل هرگونه وجهی از امارات به ایران از جمله ادعاهای مربوط به سه میلیارد دلار را قاطعانه رد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/658872" target="_blank">📅 07:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658871">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beyFjF6eGqNotxYlDjai-WEWGlvLWxRRLfAoTtGcaG5Gh2e3szQb2UehZQRk4kyzDXl_lca2ACeh0GS6DYJ897uW53carDQuAsKiXOCuOlWgxoQcVbnaW_WZyUMEIhSyv2pFdlNyhwRDC84Qdj_50gQq1-RDzMoJdIM8gbSUY_B0miuEJfEfMA9N9Eeb22UHzegXI2Vu6T4uNCBXSmaW7hAb4-eic_vtLMXaMG8QzLRAt3Ldqz5ugcRBQFQ8YbT9hhx9CfteLThZXhGnOx9DKVV43Z59XprP3mjgzqGvm98RtP-iIIMZEaj9AKAHQeZ8NhMYx2nvACCNGp_3OHgt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲۳ خرداد ماه
۲۷ ذی‌الحجه ‌۱۴۴۷
۱۳ ژوئن ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/658871" target="_blank">📅 07:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658870">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در حوالی جزیره قشم و سیریک؛ گمانه‌زنی از درگیری دریایی
🔹
دقایقی پیش ساکنان مناطق ساحلی و بخش‌هایی از جزیره قشم و برخی نقاط ساحلی شهرستان سیریک صدای انفجاری را شنیده‌اند.
🔹
تا این لحظه هیچ مقام رسمی یا نهادهای نظامی و انتظامی منطقه ماهیت…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/658870" target="_blank">📅 00:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658869">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در حوالی جزیره قشم و سیریک؛ گمانه‌زنی از درگیری دریایی
🔹
دقایقی پیش ساکنان مناطق ساحلی و بخش‌هایی از جزیره قشم و برخی نقاط ساحلی شهرستان سیریک صدای انفجاری را شنیده‌اند.
🔹
تا این لحظه هیچ مقام رسمی یا نهادهای نظامی و انتظامی منطقه ماهیت این صداها را تأیید یا تکذیب نکرده است. /مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/658869" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658868">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqpUJ2FeZfukwZpYk6LIgbGYnUFu58nItateLQKykukkveOAGzkWdk8oCLOY-5vF7yQ-5ZRAP6jQDs8RvkX9s5xIRMxdjLQniGvqBRlKBEbhLkVcJ2vWF948oeYUCTcy2VTS-ACQuS9ao9JK_8Aa3P0AUhwwzWwRDWMtV0O_34STmi8jhPR-2HJos_x27x4HWITejSQd8gDqTzJepRWmbgZEpDaHM33iTflSmKEv331ucLc9WO4PU2cAJvMw3hsDHukr6dK14i-S89vuPxfg2uHRWLsohEAsbK8fzoWkqZaxIeExswLDEt7exTaGi1k15qkfGksYlyAV94ozXksOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/658868" target="_blank">📅 00:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658867">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzgh_1sGcjOuOFYmJ37iYYf-fA7MGp7j9Tod-bpkNbWmJB8NA1wq17XAfcSIbC1aaXavy0qgii-8KisEV7mlp3MjLDMrDFg8LJgdlmPkO_uwGrQ1PzHUpujMNjTFs-wpTBHQq1VkIvlFiB716rxtAupYkD-k8bBuswVr4FpGvz2q2d9MAqpj0nLFTYi7GBKtNc--A1HPR7KW4tv-5U6jBqluh0AmnSZRdL7SyxBg-Lm3dhmu7uk9bGSBsmfqxuaPigUDyOiYcK8eISqNLDWi98Y___Yq2FJ3ibD_WIa2Icn5VE_cmlNWgZk9f9bdz6AYQTB6zfgHtiZUzCwfwsK1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز به صورت همزمان گروه های سرود جان فدای ایران ، سپر انسانی به دور زیرساخت ها تشکیل دادند
🔹
در بیش از ۱۲۰ نقطه از ۳۱ استان سراسر کشور
🔹
تصاویری از حضور مردم و گروه های سرود در اطراف زیرساخت های ایران به منظور ایجاد سپر انسانی نمادین دربرابر تهدیدهای دشمن آمریکایی را مشاهده می کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/658867" target="_blank">📅 00:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658864">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
منابع لبنانی از وقوع انفجار در جنوب این کشور در پی حملات هوایی رژیم صهیونیستی خبر دادند
🔹
بر اساس این گزارش‌ها، شهرهای مَرجَعیون و نَبَطیه شاهد انفجارهای شدیدی بوده‌اند که مناطق وسیعی را به لرزه درآورده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/658864" target="_blank">📅 23:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658863">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZM7m03_jrjG9z5AAQ-9g_dbVJZkYMhwbyHhI_Hxl9YyY4-ybb_u3DZgK9bLD_tg4nr9ViYwuZmQOxsQT9vMKJQXZ5-sdr1dclUnwHMePvlOTeN6Czn3hrUWAVmOJhd3rbLkBbhPnUmhtakGoeIsMQf1ast7ebpKDNuaM2PFVeBOtRYXcaLA_zixxxS-5dNi3yLcc8YlA2mcWqOdOX99GorChy_WTgJkbmRnXpSSNSJ6ew9AH7pEHGhPsSfXKU3XURDQ-PfZBAUGrCx7Ivil26DmHPqdijqpzZ6kUo5IRQFYQaLHjEdmOEI_v64_cimmtuWlY2VIXugSgMe-_WkZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجیب‌ترین رکوردها در تاریخ جام جهانی فوتبال
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/658863" target="_blank">📅 23:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658862">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ثبت‌نام حج زودتر انجام می‌شود
نماینده ولی فقیه در امور حج و زیارت:
🔹
برای حج آینده جلساتی انجام گرفت و ثبت‌نام حج سال آینده زودتر شروع می‌شود.
🔹
بنا شد زائرانی که برای حج آینده می‌خواهند مشرف شوند، هنگام ثبت‌نام اولیه، بدون اینکه نخست واریز وجه اولیه را انجام دهند، ابتدا معاینات پزشکی آنها انجام شود./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/658862" target="_blank">📅 23:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658861">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ارتش اسرائیل: پهپاد انتحاری حزب‌الله به مقر نظامی ما در مرز لبنان برخورد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/658861" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658860">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csd2lvoQpV6MnQ2MvEEufsb6i-eZOzQ8MUlx1ee6paLPpxAa0JumYtA_JAd2CLILynsL_wAgMkWoyfra3aCdsII1orbCRY0VxmjmJhAwcQayzT-KwPadBWL5A5FC2miDMl2-IiY-40PI0pZ6Vr6AH-S0N57Hq24R3bJT1EyY3B6gK7oif6X6sjV6niYpQJWpJ1ro0fARzL6c3TxinS8DSL5GvPUkPqVLwE_1We2JE_ixQ0ZyyQmCtk55YwRUBES8NARNsyQRVtlxA1eU-HP-HUPhLejyIGN8o0dxWgLSbRZx0ObMm0Y7XnopwfcMUKJVzY8M5t3ltOYN986J478DYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر بعد از اخبار جدید درباره احتمال امضای یادداشت تفاهم
🔹
۱۷۳ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/658860" target="_blank">📅 23:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658859">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عراقچی اعلام کرد: احتمال امضای تفاهم در چند روز آینده به صورت دیجیتالی
وزیر امور خارجه ایران:
🔹
به محض اینکه آخرین مراحل مذاکرات انجام شود، توافق امضا و اعلام می‌شود. امضا در مرحله اول به صورت دیجیتالی از راه دور انجام می‌شود.
🔹
ممکن است این موضوع در چند روز آینده اتفاق بیفتد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/658859" target="_blank">📅 23:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658858">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
عراقچی: موضع ما درباره مواد غنی‌سازی شده این است که اگر بخواهد تعیین تکلیف شود، تنها شیوه رقیق سازی در داخل ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/658858" target="_blank">📅 23:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658857">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
عراقچی: شورای عالی امنیت ملی تصمیم می‌گیرد که چگونه با مذاکرات برخورد شود
🔹
پیشرفت هایی که برای آتش بس بود در زمان خودش محقق شد. شورای عالی امنیت ملی اشراف کامل در مذاکرات دارد. یک‌ کمیته‌را در شورا مشخص کردند و بر روند مذاکرات نظارت می‌کنند. اشراف کامل…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/658857" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658856">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPat2k2eWfCRvSnTxgP4UfGm_zTMaKhgfIfmfixlAu9VMst1fAJyG9Eqp0vtO-nSPpJHfX03ymeolmZ4_5OG4keialtHarEmgiq_YAcBHSP_vZk8TFzdGZlEDcwG3-YpWSlga_RLJu7LtOf82kLHtPMVgUA91A4cpiaVoK1qPU1UZ2iBxLKB1Y2eFtvKP560jZXhlo4BZMYTEhZ0wcZmWG7e5avaH7jrv34lhc39k3X_OvXADxjRcjMDbvj54lgHxQ3w8YfBkbsjHFzfBiSYaz5nxnb54qBDSkhtcBdkmpGXBG3cjMEDGkAyLiFIZRaL26mWlkJF_qc5uYYsyblX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرص لاغری اوزمپیک| ozempic
💊
جایگزین آمپول های لاغری رسید
...
💚
😍
‌رسیدن به وزن ایده آل و تناسب اندام آرزو نیست
😉
👇🏻
🔻
۸ تا ۱۰ کیلو کاهش وزن اصولی در ۳۰ روز
🔻
بدون عوارض ' پشتیبانی ۲۴ ساعت
🔻
دارای کارت شناسه وارانتی
« عودت وجه و استعلام اصالت کالا »
زیر نظر متخصص تغذیه و کارشناس لاغری
👩🏽‍💻
‌
برای مشاوره رایگان و ثبت سفارش عدد « 2 » رو به آیدی زیر بفرستید
👇🏽
📩
🆔
@
Parisa_norazar
🆔
@
Parisa_norazar
💎
09963990775
آدرس کانال رضایت و نمایندگی اوزمپیک
👇🏽
📩
🆔
https://t.me/ozempic_noorazar
🆔
https://t.me/ozempic_noorazar</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/658856" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658855">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c90df03cd.mp4?token=uUZVMFHHvn_fSynqE2-cAX_BQaohCHrxR6xMuq5gTMEd-GELSeJ71QUbSZ6SWDgfPpMByWAsmnhcp4PeUPNKkE9T3lRPJhBJRnZBbn2qFc1PwcrAtvhCK81trM8S2yq3-zNF-vsgBlBxXk_bummKk3R-2Dlmoper6Y6UUqjhdh_NO9ZKc7Fe7kEllVKQX_WP0nai0AL4jToEt2ghqZxEFsmYMhldIaBh5LFnzx6AxukpX-rH1DrG1No43MqSzf-bFz08NDPKz3bYkF7OJYCF1Izq9fMoK0QfvlKXZkHGhMtapJQPYSnLNuK7olclfet_tZWzR5lUPRGJpGokaoGW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c90df03cd.mp4?token=uUZVMFHHvn_fSynqE2-cAX_BQaohCHrxR6xMuq5gTMEd-GELSeJ71QUbSZ6SWDgfPpMByWAsmnhcp4PeUPNKkE9T3lRPJhBJRnZBbn2qFc1PwcrAtvhCK81trM8S2yq3-zNF-vsgBlBxXk_bummKk3R-2Dlmoper6Y6UUqjhdh_NO9ZKc7Fe7kEllVKQX_WP0nai0AL4jToEt2ghqZxEFsmYMhldIaBh5LFnzx6AxukpX-rH1DrG1No43MqSzf-bFz08NDPKz3bYkF7OJYCF1Izq9fMoK0QfvlKXZkHGhMtapJQPYSnLNuK7olclfet_tZWzR5lUPRGJpGokaoGW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/658855" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658854">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
واکنش عراقچی به ادعای معاون ترامپ در مورد آزادنشدن پول‌های بلوکه‌شدهٔ ایران: بعد از نهایی‌شدن تفاهم، در عمل همه خواهند دید [چه خواهد شد]
🔹
به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/658854" target="_blank">📅 23:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658853">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d496fad7.mp4?token=IXAdqDdGxy7NWKzChK2kE2il4cBdW3GUxD5iVscaW3nEH7z8esPwCHz7gqRl3d2DWCwXr93YuAsXJlRO1qgrDmkk2pwDQ4nwVw_YNHNAvSBwN9PTsu-g4pflNgivxCOEXAEahyLNRUkYTCx63g6XQ6F9fNFZoML1G5ktF9d4Yw0RvI5c6Wwfsf3XnvdjG6i-rpBlDb542QnjfdGCknoteDcZ-cDfTN29D0b_LutAZ3s8FM2xZOiZNR_yMJwdZs2ZkRTFpXeflNkBrA4BYy_DmmAh5YEhinaUge-izRo0pzAJVl9dtUqPf1e3SFGg-Lumkq1qTwiwAirE8bRisfs6Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d496fad7.mp4?token=IXAdqDdGxy7NWKzChK2kE2il4cBdW3GUxD5iVscaW3nEH7z8esPwCHz7gqRl3d2DWCwXr93YuAsXJlRO1qgrDmkk2pwDQ4nwVw_YNHNAvSBwN9PTsu-g4pflNgivxCOEXAEahyLNRUkYTCx63g6XQ6F9fNFZoML1G5ktF9d4Yw0RvI5c6Wwfsf3XnvdjG6i-rpBlDb542QnjfdGCknoteDcZ-cDfTN29D0b_LutAZ3s8FM2xZOiZNR_yMJwdZs2ZkRTFpXeflNkBrA4BYy_DmmAh5YEhinaUge-izRo0pzAJVl9dtUqPf1e3SFGg-Lumkq1qTwiwAirE8bRisfs6Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول بوسنی توسط لوکیچ در دقیقه ۲۱
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/658853" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658852">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
عراقچی: تنگه هرمز الان یکی از ابزارهای مهم بازدارندگی ماست
🔹
این آبراه سال‌ها به روی کشتی‌ها باز و رایگان بوده اما تصمیم جدی ایران است که آینده تنگه هرمز مثل گذشته نخواهد بود.
🔹
اگر آنچه در یادداشت تفاهم آمده عملی نشود، مذاکرات برای توافق نهایی انجام نخواهد…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/658852" target="_blank">📅 23:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658851">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330b6d5794.mp4?token=UZo-Bk23gkxyRZJJ_McpjRb6fOJHu58-f_QJGkSa-dUanzjgCDTcRY-2iqPuOYKDfC9Agf6CYG6E7wXVNfiH6twVO46brNqIuTsV83Hg9HCtWNwLhFW8pBF_47ZkVgQqJe8UYcMFrDOXoO26xVRisrK7e9qt84t86i-YSWeDlu8n9_r13BvccwjFPAQdBmDKC90cRZE3WDO9OkGLTAM2tpKQyqjM5sjh3n6OIJhUBRz9-X30iRevuodnzmLQGgEiI5VduLhaYi0P0eDHJeF0lyYSiFMFvKOLxvFyxTE4CmHy0yhL8qo6X7X35hj6DtWL8BMbnE1aTgWlYD4MVIJjDoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330b6d5794.mp4?token=UZo-Bk23gkxyRZJJ_McpjRb6fOJHu58-f_QJGkSa-dUanzjgCDTcRY-2iqPuOYKDfC9Agf6CYG6E7wXVNfiH6twVO46brNqIuTsV83Hg9HCtWNwLhFW8pBF_47ZkVgQqJe8UYcMFrDOXoO26xVRisrK7e9qt84t86i-YSWeDlu8n9_r13BvccwjFPAQdBmDKC90cRZE3WDO9OkGLTAM2tpKQyqjM5sjh3n6OIJhUBRz9-X30iRevuodnzmLQGgEiI5VduLhaYi0P0eDHJeF0lyYSiFMFvKOLxvFyxTE4CmHy0yhL8qo6X7X35hj6DtWL8BMbnE1aTgWlYD4MVIJjDoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احیا و حقیقت | قسمت سوم: سرمایه مردم
🔹
روایت محمد جامعی از حمله ناجوانمردانه دشمنان آمریکایی‌صهیونیستی به زیرساخت‌های غیرنظامی ایران اسلامی در شرکت فولاد خوزستان
🔹
در آن یک دقیقه، فقط آهن و فولاد نسوخت. رؤیاهای هزاران نفر زیر آوار دود و آتش ماند. پشت هر…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/658851" target="_blank">📅 23:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658850">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
عراقچی: اگر دشمن بخواهد سمت جنگ برود ما آماده‌ایم
🔹
هیچ شبی نبوده که دشمن تعرضی بکند و از نیروهای مسلح ایران پاسخ نگیرد.
🔹
به‌هیچ‌وجه از منافع ملی ایران نخواهیم گذشت و تسلیم فشار و زورگویی نخواهیم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658850" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658849">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
عراقچی: بحث دربارۀ رفع محاصرۀ دریایی و تنگه هرمز در این تفاهم‌نامه مطرح می‌شود ‌
🔹
ترامپ هرچیز دلش می‌خواهد را از زبان دیگران توییت می‌کند
🔹
اگر قرار بود چیزهایی که آن‌ها می‌گویند را بپذیریم در گذشته می‌پذیرفتیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/658849" target="_blank">📅 22:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658848">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
عراقچی: رژیم صهیونیستی دشمن امضای توافق است
🔹
امروز متن‌های مختلفی در سایت‌ها منتشر شد که هیچ کدام اعتبار ندارد.
🔹
توصیه می‌کنم رسانه‌ها اجازه دهند آرامش برقرار باشد تا به بهترین توافق برسیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/658848" target="_blank">📅 22:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658847">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
عراقچی: موضوع بازسازی در قالب یک طرح بازسازی و توسعه اقتصادی مطرح شده و سازوکارهایش در مذاکرات بعدی توافق خواهد شد
🔹
برای پول‌های مسدودشده ایران سازوکاری در نظر گرفته شده است که وقتی نهایی شود، حتما جزئیات کامل را عرض خواهم کرد و بند به بند را توضیح می‌دهم.…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/658847" target="_blank">📅 22:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658846">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
عراقچی: دشمن تعهد خواهد داد که دیگر آغازگر جنگ نباشد و از تهدید و زور استفاده نکند و دوطرف به حاکمیت یکدیگر احترام بگذارند و در امور داخلی یک‌دیگر دخالت نکنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/658846" target="_blank">📅 22:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658845">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
عراقچی: توافق شامل دو مرحله است و موضوع هسته‌ای را به مرحله دوم انتقال دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/658845" target="_blank">📅 22:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658844">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmpoTMsRDZCRs-OoV78_6orDEptRz4L-ZO5kqXZk8sRKv9jyKrQvkprlK2wYWi5jdj_7EaPiVWXTnoiba6XobRiHvDEE_f10K9WSzAVd1kJMHoCvEfn-ct9W0po_WCZJTaCn5z56xq0r49vca5krRn3HAMPdzW8RX_QCaMG_BHjImyKf0V4I3rY-LgmeE_WnmRvDAmVjDyVWA3cA4HxY6ZcAoT8eJ5LM6dd8i_YkQYJoyH29Nl60crRFNuGaghg8n-3_BxDVoGU_2ZkDxRTIVe_a9mRhGljCAW4t1sc5hEa1W2fYTF8y7wyZaVYhWCk6cPDmca8MANV6_KmO4IdChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: باید به تعهداتی که داده شده عمل شود، بدون هیچ اما و اگر و بهانه‌ای. برای توافق نزدیک پیش‌رو راه دیگری نیست. هر کسی درنهایت چیزی را درو می‌کند که کاشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/658844" target="_blank">📅 22:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658843">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
عراقچی: ترجیح میدهم جزییات تفاهم احتمالی را بعد از قطعی شدن بگویم
🔹
هنوز تفاهمی امضا نشده و ممکن است برخی موضوعات بالا و‌ پایین شود
🔹
متن تفاهم تا الان در نوبتهای زیادی تغییر یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/658843" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658842">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وزیر خارجه: نمی‌خواهم شعار دهم به عنوان وزیر خارجه عرض می‌کنم در این جنگ پیروز شدیم  عراقچی:
🔹
کسی ایران را اینگونه نشناخته بودو تصور ایران ضعیف در هم شکست شما شگفتی آفریدید. اینها شعار نیست من اینها را مسئولان کشورهای خارجه شنیده‌ام.
🔹
ما پیروز راهبردی…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/658842" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658841">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
عراقچی: وظیفه دیپلماسی تثبیت دستاوردهای میدان است
🔹
مذاکره و مذاکره کننده متکی به قدرت میدانی است.
🔹
مذاکره بدون قدرت میدانی به نتیجه نمیرسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/658841" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658840">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
عراقچی: مقامات غربی میگویند باورمان نمیشد ایران سرسختانه مقاومت کند
🔹
این مقاومت در وهله اول مرهون جانفشانی نیروهای مسلح است و همه ما مدیون نیروهای مسلح و شهدا هستیم.
🔹
عامل دوم مقاومت ایران، حضور مردم مبعوث در میدان بود.
🔹
رسانه‌های ایران و صداوسیما نقش…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/658840" target="_blank">📅 22:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658839">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
عراقچی: دشمنان ایران فکر می‌کردند با به‌ راه انداختن جنگ ۴۰ روزه می‌توانند به خیال واهی خودشان کار را تمام کنند اما مقاومت تاریخی مردم و نیروهای مسلح ایران آن‌ها را ناکام گذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/658839" target="_blank">📅 22:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658838">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9QiEbkrTYIjWFoU-xhoUXc-NQ_K-7L2KvS3vIA-jkXBp4S2T9fi4IjOcQXtQoV-OLLI_LJAQFmhU7bJLml9dIaQ5Bp_rfMSP7-MiYUmdYkiHySDfKM_837gwh85FRXTkOKP5uORNf9A7NTcK1FZ8eFVs2wTVI4MyEB9rwrm28deT78JT1u2o-s4fXT2n9rb85pRfE1n_3jx6jCu51mcwDpUmMvT3tgNOd-How3Yi4RLtmvg0LnrpXpuau9dStZuSop8iXNGQ2E17rUBfWHtPp112Q8gFY0mMNizr71X0TeJQArhFurnBmSn9mSBE-96jKSMLjlxTaf71Jc7GMOvaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: دشمنان ایران فکر می‌کردند با به‌ راه انداختن جنگ ۴۰ روزه می‌توانند به خیال واهی خودشان کار را تمام کنند اما مقاومت تاریخی مردم و نیروهای مسلح ایران آن‌ها را ناکام گذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/658838" target="_blank">📅 22:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658837">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnepvhDn2H7J6MoyjpnhwiExqksKVTf_KIAFPxsEqCMbkwjpQUQCi4VwUGtxO1Y_0mON0fMjBF1aJQCn5EvWh7ap0F_A_S2MvHAKNLdru0TMfhHju1pRVc2XTbEM3RHa16DZ43bZhzn83o_EFPcOgpLx-peTX9EtJyVrtSO9XOttqQS_YyZsgbSuHXQkTG0vHtj3jb9sEvZIAsL8qvIhAuEMi0vCo6H7z_w5NQd7mg8yrLAe4PI5tQn9NkWPF4d6QJPLlgwC2iQ2EO0YRvkFQHF9rul09r2S6e-DJZ-5uUqaCisidc2eR5_eaE86iEZkYXe59_g5nrZxDeG0BNF3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پرچم ایران بعد از مکزیک، در کانادا هم بالا رفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/658837" target="_blank">📅 22:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658836">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0WI7Z2o4f6BLnxXHZfPGGMvp55Exx5kxjfUlcVqf6C0BaZeVDGHEUujMeu9Cdkl6A0KVUFxDV0g2ujF2JZpo1mu_uoapq0KWCOG4Fc5LElTKdjoPce8WQkOHZ_u3T8h7EOdi_QEvDFxv_HxZ4nnNN0y-CPNLZl6_hLevKErG3SzS58Qo7yjqYY7udUN9MZ4hKhIiUrF1nUr3_mF1PrBlDbiVT7JKHg5xVtxEf5BU1fRaZT39gWcKsfP3pBCTKcYJFMBNgi4V2TTsMk1fmbYY7Gbbq9ubLkNBe7SGoKM_JdqhJ1SNIpRSAt7FS6HOQURg45pzmVDbxr4qFYne_b5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک پس از عرضه اولیه سهام اسپیس ایکس، به اولین تریلیونر جهان تبدیل شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/658836" target="_blank">📅 22:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658835">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نیویورک تایمز: تخلیه ذخایر نفت جهان به ترامپ برای رسیدن به توافق فشار مضاعف وارد کرده است.
🔹
حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است.
🔹
مقام آمریکایی: مشکلی با نیروگاه هسته‌ای در ایران وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/658835" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658833">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اهدای تجهیزات تنفسی به بیماران سی اف، زیر سايه امام رئوف
🔹
به دستور تولیت آستان قدس رضوی ،۹۰ دستگاه نبولایزر به بیماران سی اف، در بیمارستان اکبر مشهد اهدا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/658833" target="_blank">📅 22:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای رویترز: امارات قرار است مجموعاً ۱۰ میلیارد دلار از پول‌های ایران را آزاد کند که بیش از ۳ میلیارد دلار آن قبلاً تحویل داده شده است/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/658828" target="_blank">📅 22:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای رویترز: امارات قرار است مجموعاً ۱۰ میلیارد دلار از پول‌های ایران را آزاد کند که بیش از ۳ میلیارد دلار آن قبلاً تحویل داده شده است
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/658827" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a055303acf.mp4?token=XM2ZpA8jkqXAvFJM8YPhy6rUzxv3IsN4w6TGULjiZb6i8bATI1eSAnBSN07m_QhZxSNc6AF6SXmmwwJv96vlz9ILk--CdUS21b5lJQzr21-2sJJH56ne2jHebxgahlBQ8yaVlhTlKy9IkOBRHGWZuJuHBbuxDQVFcbKrx1qDV904WbJBVX3SYHCmEES3clab5mIHbqAsIrEOeWzvehPeCgNic3bPCge-Z7E68l8HgOJcNA3x0m0N8h5Zub9ibB9OhZahDGCs9v-vGpkU0Nd6_navd3XuayQlnj-61RNNG1SZCREf00fjtssv7_eUz-P2lCtQLpbN7SlJh3R3qwQmIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a055303acf.mp4?token=XM2ZpA8jkqXAvFJM8YPhy6rUzxv3IsN4w6TGULjiZb6i8bATI1eSAnBSN07m_QhZxSNc6AF6SXmmwwJv96vlz9ILk--CdUS21b5lJQzr21-2sJJH56ne2jHebxgahlBQ8yaVlhTlKy9IkOBRHGWZuJuHBbuxDQVFcbKrx1qDV904WbJBVX3SYHCmEES3clab5mIHbqAsIrEOeWzvehPeCgNic3bPCge-Z7E68l8HgOJcNA3x0m0N8h5Zub9ibB9OhZahDGCs9v-vGpkU0Nd6_navd3XuayQlnj-61RNNG1SZCREf00fjtssv7_eUz-P2lCtQLpbN7SlJh3R3qwQmIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرایند زیبا از آیین پوش‌کشی خانه امام حسینی در شهر یزد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/658826" target="_blank">📅 21:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2887501b6e.mp4?token=kQ-i-ew3FN-GoTFhmB4GGp8-eBvRyGmGy7c41i0A5ZuMN3t0VFx4bgDKs9DRegxeqFFVukWcY1jqLUao_rA8K7qN5ep25eeUfqu0-XBik6-7CRMGSLUGNaawETIYYe2OC-z7p-pk3WugZQe7owG6EjIwK3_qUxgsW_UJRh4Tee01hVXWVMe7OZRko3h90sR8liNteyHIN0CQf0Qw7cZ6VFBdRvZ0EONndhyd9Qy0Zue7tqYum5hUpYb5nnA6GzGUf4MNS24yB3BBP4v-DGiQkY6ZmCG0X2KlhDnTDvbbQnYnzCrBJp4RJhL_N7T5WB0o3hVbWFwOBLHnwemjkHsYl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2887501b6e.mp4?token=kQ-i-ew3FN-GoTFhmB4GGp8-eBvRyGmGy7c41i0A5ZuMN3t0VFx4bgDKs9DRegxeqFFVukWcY1jqLUao_rA8K7qN5ep25eeUfqu0-XBik6-7CRMGSLUGNaawETIYYe2OC-z7p-pk3WugZQe7owG6EjIwK3_qUxgsW_UJRh4Tee01hVXWVMe7OZRko3h90sR8liNteyHIN0CQf0Qw7cZ6VFBdRvZ0EONndhyd9Qy0Zue7tqYum5hUpYb5nnA6GzGUf4MNS24yB3BBP4v-DGiQkY6ZmCG0X2KlhDnTDvbbQnYnzCrBJp4RJhL_N7T5WB0o3hVbWFwOBLHnwemjkHsYl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ عجیب بقایی به سوال مجری: من فکر می‌کنم شما حساسیت بی‌جا نشان می‌دهید به ادبیات!/ آیا می‌خواهیم به نتیجه برسیم یا نه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/658825" target="_blank">📅 21:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای شبکه ۱۲ رژیم صهیونیستی: ترامپ، در آخرین تماس خود به نتانیاهو، گفته است زمان پایان دادن به جنگ فرا رسیده است
🔹
نتانیاهو در طول تماس تلفنی با ترامپ زیاد صحبت نکرده و دریافته است که توانایی تأثیرگذاری بر این توافق را ندارد/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/658824" target="_blank">📅 21:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658823">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سخنگوی هیأت مذاکره: هیچ‌کدام از گمانه‌زنی‌ها دربارۀ متن تفاهمات را نمی‌توانم تایید کنم  بقایی، سخنگوی هیأت مذاکره:
🔹
در مورد زمان و مکان امضای تفاهم نمی‌توان نظر داد و باید اول منتظر بمانیم تصمیم نهایی در داخل گرفته شود.
🔹
هیچ‌کدام از گمانه‌زنی‌ها درباره متن…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/658823" target="_blank">📅 21:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658822">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4339de380.mp4?token=sGH6C_IhyhzYt1JerjBK4yU9Pdub0snYZqmNC_FrEeZPw3yWUeEfoy7Kz7rCHbOAiYwR20BOeJI3INWNU9Fas5svSeeMYnDy4ogpqy06z4b2Hq9XrmhcklEvU1dMwSwa32Wz6kKicgINqAPdQUU6SWNuRHj4l4lvwvKvRKn61z4sjY6RhxxA9iiOKU3UH0Ds7yEaqQMYBA7sOcCBMU_Fow2FnONbpa4mDYTn9mLwlXkXGZQvWM63nMhRn7s2HbM5slyncw9eAH7YPudYwBn1YZhdhqY3NYBpSRf97VwHyPrRxdvrHD-rLvk63lCjjqIYVjqacpEWPaqh-U39NL2PpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4339de380.mp4?token=sGH6C_IhyhzYt1JerjBK4yU9Pdub0snYZqmNC_FrEeZPw3yWUeEfoy7Kz7rCHbOAiYwR20BOeJI3INWNU9Fas5svSeeMYnDy4ogpqy06z4b2Hq9XrmhcklEvU1dMwSwa32Wz6kKicgINqAPdQUU6SWNuRHj4l4lvwvKvRKn61z4sjY6RhxxA9iiOKU3UH0Ds7yEaqQMYBA7sOcCBMU_Fow2FnONbpa4mDYTn9mLwlXkXGZQvWM63nMhRn7s2HbM5slyncw9eAH7YPudYwBn1YZhdhqY3NYBpSRf97VwHyPrRxdvrHD-rLvk63lCjjqIYVjqacpEWPaqh-U39NL2PpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواداران بوسنی بیرون ورزشگاه در حمایت از فلسطین، یک صدا شعار سر دادند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/658822" target="_blank">📅 21:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658819">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSXnez9JkLxhv4WPQnSttAGjWC0ntHbSGVtFuEQPq30iZg8bTx4QXXRlxBBaJ7GCVYkrGf1j78JX38ri4N62x-K7k1gL4UMsKcGTORisSpdG8KXzRQ1YBZp_UGOFjGH2vQA3u6_84Z2Is9p-MVJc2bxzr1XB2nuc2mqXyZUUHSkZnpLGwphDXEoGutog98FbVJ9xztLdYeqruZcodVyUJIuZbGctmJA_4Rt4LiQ16Z2GSosCfTmTNZFANzJQ3O-mqCpUL_v_Vp69d7mH1NaOeqRK4rKWzrC1YKGUcejegQmVvoigkw9lPeLOw0MHrw1VWbhMt5TWBnqZk5kfqOArjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQdpyTOtkCku0F6FAr_Fr_BLKcGgTycLjNHdK_1KwXtiTh_5IgTm5dWEtEcA2wgsYtyXuJ6WWeN-LapAO10aMRwpTpb_-6Ey1P73ayTi3smQ4OmW_KM2szbPYmUUz0smG7tVUcZU2Fm5rrWRfi8pRCZj06jdvF7K6H47O9GHfzQf5aU3GOkk7XvKZUCkh3ZhoCn6HPBhmJ_k4qlNmqDWHDqUT3z37zRy_0xb97FAwP4f0QIsGu-U7JXaMYs6ZOifjTmUAMTx-62qV5PAA4O1OWJliB4dwQ4P2BaE0sQmHtvEaCkZs5_MOFk5_r5t96jFrT3mSTqn5MGjBJlimURq7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9299515ba6.mp4?token=AjA9_eieXXizSlqYTMc4p4nwI8Ipz9rqEPC2XZ_ft6eyXTdW2F4fY6I2Bh7iUNx0UuYvVm6SPaoGgMj5Ns-LZpKLIeDdF73hz0x2xaVgBLXyg4a9lC8m-oqqqUkyBOdaDZy0qJ-FMyNTqVfavCB_w-54n-mLMCO40IKVXM_aAALFmxLVlXrGIZL5Zh2xUWQX4uI8A2kw19me02OU_bqQif9NTDdSg3NLRHGkpKT2txKcgtBNrapK7zwHf8b_-FK--DuUj59lZiidzUKuc27q2mZH5nYW9bcOtptW9JUAF8wn8fOwmBkDJp8ynoh8YPzkrYSEd8GO_MUV9T17PDG4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9299515ba6.mp4?token=AjA9_eieXXizSlqYTMc4p4nwI8Ipz9rqEPC2XZ_ft6eyXTdW2F4fY6I2Bh7iUNx0UuYvVm6SPaoGgMj5Ns-LZpKLIeDdF73hz0x2xaVgBLXyg4a9lC8m-oqqqUkyBOdaDZy0qJ-FMyNTqVfavCB_w-54n-mLMCO40IKVXM_aAALFmxLVlXrGIZL5Zh2xUWQX4uI8A2kw19me02OU_bqQif9NTDdSg3NLRHGkpKT2txKcgtBNrapK7zwHf8b_-FK--DuUj59lZiidzUKuc27q2mZH5nYW9bcOtptW9JUAF8wn8fOwmBkDJp8ynoh8YPzkrYSEd8GO_MUV9T17PDG4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از مراسم افتتاحیه در ورزشگاه تورنتو پیش از شروع دیدار کانادا و بوسنی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/658819" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658818">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
الحدث: وزیر خارجه پاکستان امشب عازم ژنو می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/658818" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658817">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
خبرگزاری رسمی اسرائیل: رهبری سیاسی از ارتش خواسته است عملیات خود را در جنوب لبنان کاهش دهد تا به توافق احتمالی آمریکا با ایران آسیبی نرسد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/658817" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658816">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
الحدث: وزیر خارجه پاکستان امشب عازم ژنو می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/658816" target="_blank">📅 21:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658814">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhKGZvsibYbUgulwfyczuR5Oq6pb7f1FSS4As3FYvLg1LmTH8IUXlBFa0q7-iwD-_gPUnHR4dp-uzT1PNcTqZnxWMGPjeBWAY5M9fNEZLIbdT3z7_QzAE0Z2LlKQjUTGNb-FprBeuZYoAAKUBkGdBpvRJIonmQdOVErgGmXniI_YWnDiCCBC-vLqtYUC1Q_0_0QITKo_XlE2l-153cQTa_QjktbUZyR-46EY-G1WCMA35WxnBc3kI_RZB6PHf-BHQswPXGLbnWDyIfceA_NRHW7NGWcftrcGD_3ZYEq5_zJIm0DeGo4L4s3qXoBTRhkEYlIN-o4jlijFJuBkH4vYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: ترس ایران از جنگ ریخته است
مجله اکونومیست:
🔹
درگیری مستقیم ایران با آمریکا و اسرائیل به «واقعیت جدید» منطقه تبدیل شده است.
🔹
جمهوری اسلامی پس از مقاومت در برابر دو رقیب قدرتمندتر، جسورتر و در استفاده از قدرت نظامی بااعتمادبه‌نفس‌تر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/658814" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658809">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K74H6gCdx7tTSvyN4WxGXurtdndwxi1xZZexOjc7EIa7g_bJs5ZyM6ywzN2-Jy-hk1e3bySZxG0K3HmfmJSHFuJrKhli7MapLk1AtI-i5EDMFKRcin_pMLsxdKH0NA40p0YTKBisKeksFR3tqXn0ocOFAArPc-FYaYs732U3OMhXYCMMFZAjR2gAM6wRWphFtTPEy4Kuw0G0bj2eJ2o9PJxWmPOyyD4I2TE3e9HpjOW3RnNnh4VfcnP3iz1cZhCbANgRXkhjI5f7-vsQuyiiqjybCSXkOxamPabuzuGh_4YSTxoqD0ylKAzpAYgXTDSpX40tBCPKtwpLy13nyWhWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8F4IbZKYudSXg1haEbynZWDIQLJbLKUM_p01jL942qsDOkQNCsa0hMBrb9TP4x8BCKlOa6N1DLh6hI82L3X9HbgCQJLTCV6lmPv_IsTqKaZOj4XVpNAW8yHL6zSdGZ-1oveBeePF2lRVeBLk54tziOR6Ky7IdBa5H9WZL5xwlcbsZ6t4idYwBkM89OL4Ifk2Va1w4Cmf06KyFtA8WRhlP4x2pT8IIlsxpc8cXTuEzRn7E9mUqPsP5SNE4n1k8wLpucSZTAK9MJfvIUWNupdtGSwOVM7JBnQlmU3b91Ms84T3XRbeAahE_F1E1dUv4U-U37OoNQypGwAahAHTXP6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNLAWmlDtz48lLESEqKlvZfgGHOr-idB1-PjfwwKUgTSoNUIiGD36JjSTiuT5JHj3b2cQbgl7_P3tpx9KS1LftQr1lxQroVkKiuJjDrN-pQiqkTWapErJNg_Mh2g9bNF61tTqGnuUkUA6H-98G1VKuMksppmsmUej5O8-w2pHYCXAIfFi9nIqldEtv9TU6A5OWtuT5a5oghbTBYCWpxog3A46tZDSJBZKGOeKufnm1A4qDAbenyzfDACBkuWxU4Pmg5I_gMqtZBCc7jrDPyDXM3kofOAFjvX23PmrH1-TNu25PNgl0mKGcSbVtGvoEFye6wwB-GrPH7c2ZK-_88mAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEaTAourWvlGQUMZgFsE37NOR6JYjDDIzONcZ-virqmite-j4CeTV88WURNOGQL9Xg1SIad_hqE7k6d65o6YNTgjk3ivZQPg1pPPaPMfWb09hKAR5QKOAo9QhDFSxcNoy-ncQdC_2miQU8Dszjj2IJBhxj8inUB7rlSkwxS02W32KW8Hbsz-wpHWTyaf39jCu9gSfYcqIqIo-A8d5AHSq__WmNK60EXshK8uIOC0j5JKlZGqNoKN0kbcXoNJVJ8vuF9zhOXLyenZW5EZhkqdSTCQxgXI_0ofD5-Zz5zaI-6HqYCrC4tc1TbUCC5xdiT8VzGQLCf0uzy_eYZnIJe5-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3KwkKyMttFzgsLtMBDfsNkwKeojZrqBvEdiEDvTJUBz_HUoO_y6KpzBs0FvL2CHwHXQCkRV9q1egY3RgphsQC5CJ4AH-vhzVGv9nOrbBPD9sD9-a__E6yHKFLD_EYX7w_mg0lmcUjvnEb0u1qYZXNXsXK-9C5pv6n5B4283OrIXNC4auUn4QsVEUBXtl0BE0xrt8l3DFIRyd9Sym2iI5rMqvd1ZVHaZSsyAPp53azHW14H-WNPLW_fbr45Y0w0579oPC1xBZ6GiXj0p5wIoh_wMnGjdyfs_LSLdRvKTygc9rVjLokSRF6eyaQ3kPIZ06hA5ruN2Z03BzDP60TxbwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زنگ خطر بحران پلاستیک در ایران و جهان
🔹
بیش از ۸۵٪ زباله‌های پلاستیکی در ایران سالانه به دل طبیعت و خیابان‌ها سرازیر می‌شوند.
🔹
همچنین، میزان مصرف سالانه پلاستیک در کشور به مرز ۲.۶ میلیون تن و سرانه‌ مصرف پلاستیک به نفری ۲۹‌ کیلوگرم در سال رسیده که زنگ خطر بزرگی را به صدا درآورده است.
🔹
این چالش در ابعاد بین‌المللی نیز دیده می‌شود، چرا که نیمی از کشورهای دنیا در بدترین وضعیت مدیریت پسماند قرار دارند.
@amarfact</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/658809" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658806">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سخنگوی هیأت مذاکره: هیچ‌کدام از گمانه‌زنی‌ها دربارۀ متن تفاهمات را نمی‌توانم تایید کنم
بقایی، سخنگوی هیأت مذاکره:
🔹
در مورد زمان و مکان امضای تفاهم نمی‌توان نظر داد و باید اول منتظر بمانیم تصمیم نهایی در داخل گرفته شود.
🔹
هیچ‌کدام از گمانه‌زنی‌ها درباره متن تفاهمات را نمی‌توانم تایید کنم.
🔹
اینکه درباره جزئیات روند دیپلماتیک نمی‌توان صحبت کرد به معنای نامحرم‌بودن مردم نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/658806" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658805">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
رئیس اداره هواشناسی دریایی مازندران: گردشگری دریایی در مازندران تا اطلاع بعدی ممنوع شد
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/658805" target="_blank">📅 20:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658804">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ترامپ دیوانه گستاخ‌تر از همیشه  ادعای ترامپ:
🔹
ایران به طور خصوصی به خاطر ارائه اطلاعات نادرست درباره توافق عذرخواهی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/658804" target="_blank">📅 20:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658803">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a93427fa.mp4?token=R6HwDQr4mlFVMWTX296K9HMSEsZIDMPcV7UpldPEvMVAYryge0mGWjYRjzH_s7r6BcXUHVYRO-L9AxTHcdEYU9MViJssl_tiUFurZTfpUxNIWM-wBWZORHw-RnSlcCAxIUdqy3HFf_ozCsehFEJAYozjv84Y8EhA2XKwt_0u19PHSaUMDBnhhbnUUwX7AnV_-1eCvJwcWLLjr9uPht-UYc9nz3CsrQMCWgyNEmHN5OgqOXhAyDet-NnRb23ocxFTPYeWZozKwjvOkaRhnotDHdIk1tz-730_XEyzMSczAZz6Owuj4gnfnlLzEsdpOp2mANqwNVe7FCUVUlfkdalMAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a93427fa.mp4?token=R6HwDQr4mlFVMWTX296K9HMSEsZIDMPcV7UpldPEvMVAYryge0mGWjYRjzH_s7r6BcXUHVYRO-L9AxTHcdEYU9MViJssl_tiUFurZTfpUxNIWM-wBWZORHw-RnSlcCAxIUdqy3HFf_ozCsehFEJAYozjv84Y8EhA2XKwt_0u19PHSaUMDBnhhbnUUwX7AnV_-1eCvJwcWLLjr9uPht-UYc9nz3CsrQMCWgyNEmHN5OgqOXhAyDet-NnRb23ocxFTPYeWZozKwjvOkaRhnotDHdIk1tz-730_XEyzMSczAZz6Owuj4gnfnlLzEsdpOp2mANqwNVe7FCUVUlfkdalMAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار شبکه CNN: احتمالا ترامپ باز هم از ایران فریب خورده است
🔹
این که تنگه هرمز بلافاصله باز شود و حجم تردد به سطح قبل از جنگ ظرف ۳۰ روز بازگردد، اینکه محاصره دریایی آمریکا و برخی تحریم‌های ایران به عنوان بخشی از این توافق لغو شود، و اینکه تمام خواسته‌های آمریکا در موضوع هسته‌ای تأمین شود. این همان چیزی بود که ما گزارش می‌کردیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/658803" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658802">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای ترامپ: من هنوز فکر می‌کنم که توافق با ایران ممکن است آخر هفته یا دوشنبه امضا شود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/658802" target="_blank">📅 20:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658801">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsYeqNEgtZwAz2wL8ijPvGAp8rWIL_KnPg6rOgVELLnZJ7DBJywIBlMlNOhw859P5gKhZqDnR8FjuqM6BpVZWwphYnjL58WEG_kGDImMnWQvc2mWpYfH5p0sj8wsUD-goCeVYinMCnvy0mI51T6ya-rLn3zVHNCvZrrbO9ffogisMjq23fcrQDpsbmr0RoYmMxKfGQdHF1858eiLIpEDnAzy3BdMspcnTqYJTxDeWs4ODzQHpITkPqvdAxhRlChzn3rHWqAHVPJDN-ysmMDhivgJfcKJHR6FCrUacaiDBraQvltJo3UQ97LK3iqi6g0_Dl8wpMwwJcEqbMuXgny9lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/658801" target="_blank">📅 20:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658800">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
جدا شدن روح از بدن نجفیان در نوجوانی و ....
🔹
00:10:00 چگونگی مبتلا شدن به بیماری ناعلاج در ۱۶ سالگی
🔹
00:15:00 پرواز ناگهانی و بی وقفه روح
🔹
00:24:10 احساس سبکی بسیار زیاد به همراه رفع درد و نگرانی
🔹
00:28:45 آگاهی داشتن نسبت به درختی که نردبان از آن ساخته شده بود
🔹
00:38:00 درک سنگین بازگشت روح به جسم
🔹
00:42:20 پیش آمد دردسری از نردبان حمامی که روح من آن را نظاره کرد
🔹
00:49:30 دریافت عمیق رفتگر از تجربه نزدیک به مرگ من
🔹
00:55:05 علت داشتن آرامش زیاد برخی افراد در این دنیا
01:07:20 بزرگ‌ترین لطف خداوند به بشریت
🔹
قسمت سیزدهم (رسم زمونه)، فصل چهارم
🔹
#تجربه‌گر
: رسول نجفیان
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/658800" target="_blank">📅 20:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658799">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا: پول نقدی به ایران نخواهیم داد
🔹
درصورت پایبندی ایران به تعهدات خود، منافع اقتصادی نصیب آن‌ها و کل منطقه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/658799" target="_blank">📅 20:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658798">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
خبرنگار آکسیوس: ترامپ در یک تماس کوتاه به من گفت که پست عراقچی، وزیر خارجه ایران، را «بسیار مثبت» ارزیابی کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/658798" target="_blank">📅 20:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658797">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvRRVdnpo2sIPMd-aeRN16kn-aebUboTmrv84V0xi6pYe5LLOBe3Z2e-pZh39ggSqsCy07DIvBbH8gpAEbj0W68TTFxG592tOHSCSQaoipwrqFdpCeONbVSXmQPA0YwKlvjcKxiqPE4QCulQrabfqRFmqQ9K7TkDG8AyVZF-P-wWgv2WxeOhmRDJS--ytgCmeubBLbhzBBEk9hBeLaHMZxVv1seDyD35z7tshVAnH9GPvh6uATtchqDndpLBnHD3onAU9gIYMYcRbkeMnVeXe00HTUf9Kdq7u77QD_dR0mF3FhBztbKEAnVxEKSVG08oQMWuflE2mTbylYkKS3kddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
ترامپ: من هنوز فکر می‌کنم که توافق با ایران ممکن است آخر هفته یا دوشنبه امضا شود
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/658797" target="_blank">📅 20:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658796">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: امتحانات نهایی از ۱۳ تیر شروع می‌شود. خوشبختانه با مصوبه شورای عالی انقلاب فرهنگی تاثیر معدل پایه یازدهم مثبت شد، ۶ درس شد و برای ترمیمی‌ها هم تک درس شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/658796" target="_blank">📅 20:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658795">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سی‌ان‌ان: ترامپ به دلیل ترس از تلفات گسترده، ماموریت زمینی علیه ایران را متوقف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/658795" target="_blank">📅 20:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658794">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای گروسی: ما راستی‌آزمایی طیف کامل توانمندی‌های هسته‌ای ایران را اولویت اصلی خود قرار خواهیم داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/658794" target="_blank">📅 20:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658793">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDdkg5B2SaYM4axbuC_znqpIoHJF77ynx2irSauQQC8yPiiNXM7bHHav81q6zN3LgvWZklQOwsSd87UKk6GhEjqnyGPHUm3ERUWd-qBnZ9g3G6GU5N3TX2-eAoqZq2P0XQNtMLAEzEZP725aA26IunZ4WnlaarHd7XY5712Zm2Hs-5d4YfWOyiUJkQrKneV30L2Vvr_d3Ejw-F_LXfzneRaX0daVb20h7aG0fGUu5BG-gaGmln1JD3MMt_dHexEslHGfj_w7Tdu6T8emaTInHYjkRyfvxS3_bZgs8pzKWg4-thJ1IIfbUIJWj0aXbaHzhcyI9A74zuixKIuq-juMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب: پایگاه‌های پوشالی آمریکا تاب و توان تأمین امنیت خود را نیز ندارد، چه‌ رسد به اینکه امیدی به تأمین امنیت وابستگان و امریکاپرستان منطقه توسط امریکا باشد ۱۰/اردیبهشت/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/658793" target="_blank">📅 20:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658792">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
یک مقام رژیم صهیونیستی به یدیعوت آحارونوت: ترامپ ما را فریب داد و توافقی که قرار است به‌زودی حاصل شود، بسیار بد به نظر می‌رسد و اصولی را که هنگام آغاز جنگ با ایران درباره آن‌ها صحبت کرده بودیم، برآورده نمی‌کند
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/658792" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658791">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
شبکه MS NOW: ترامپ تاکنون چند بار ضرب‌الاجل‌هایش به ایران را لغو کرده است؟
🔹
بررسی سخنرانی‌ها، مصاحبه‌ها و مطالب ترامپ در شبکه‌های اجتماعی نشان می‌دهد که از زمان آغاز این جنگ در ۲۸ فوریه تاکنون، ترامپ حداقل ۸ بار علناً ضرب‌الاجل‌هایی را برای اقدام نظامی علیه ایران تعیین کرده، اما در نهایت از لغو آنها خبر داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/658791" target="_blank">📅 20:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658790">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
نقص فنی در هواپیمای حامل پاپ
🔹
عزیمت پاپ لئوی چهاردهم، رهبر کاتولیک‌های جهان از اسپانیا در پایان سفر یک‌هفته‌ای، به دلیل نقص فنی در هواپیما به تأخیر افتاد. پاپ به سلامت از هواپیما خارج شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/658790" target="_blank">📅 20:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658789">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: ایران قوی‌تر از قبل ظاهر شد و هدف سرنگونی نظام و نابودی توانایی هسته‌ای محقق نشد
🔹
نتایج جنگ با ایران با مفهوم پیروزی مطلق در تضاد است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/658789" target="_blank">📅 19:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658788">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQISoORBKqDz5xQJ165MCE3gvlb3NIYEVQNHEuAg-CiwxdXLZvQnsgp_goNs2_okg3Sha6unopLgzpHw9oo9phtncBjpDvkxMUOcmfpNyJXFlnVQ6gLwUmauguFSciac4jSuCR40tT-zXdUWQWLnxXt1olCzVXSU6LebMxceVX_u9LLcYae7kV0uGrilXUJ9m4mlwUZKufYU_dO79GsloUFB7ljzQRAJ79cAgcA0zzOHiqFtF0R1ZmF6wM8hiFmUU2Aq2FIzhiVAXntVN1RdQW1GTpWgJu0fsE2K7VYIA9B4_U4NFtyGZ2gToMI5CN24bMwbtiYmKwGAql8D9xZsgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان، درباره توافق ایران و آمریکا: متن نهایی و توافق‌شده‌ای از قرارداد صلح حاصل شده است
🔹
در میان تلاش‌های فشرده و مداوم پاکستان برای میانجی‌گری، ما کاملاً از کمپین بی‌وقفه و مداوم اشاعه اطلاعات نادرست توسط کسانی که می‌خواهند توافق صلح را خراب کنند، آگاهیم
🔹
چنانچه از این هیاهوها صرفنظر کنیم می‌توانیم تأیید کنیم که به متن نهایی و توافق‌شده‌ای برای پیمان صلح دست یافته‌ایم و پاکستان اکنون به طور فشرده با هر دو طرف در حال همکاری است تا گام‌های بعدی را نهایی کند. صلح هرگز تا این حد که امروز می‌بینیم، نزدیک نبوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/658788" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658787">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460611eb6b.mp4?token=aG7mYwDApynRhMoH1rNgkFHL-q0n0o-k61JCYqxlKS8ZhCYh9MBepc-HgcDOn7Bm1iSdlCqMtHRyywYUUassi5nGnjMtXLfRCqG1SgCYPTbK8qSkLWFOulpI1w8vYrYlS4HkvnuKX8rOnc8LKvoc5DnNfQVrU0X7LB3JUZcKqyfCM5llRAJWAHo5Xj6QDrbnGYUOo1pYfZ47od9rHHSkClMVGNJiTdLSvdcSqlAYV_OTF7yzQt9mtxzI58Z49JhBTWzG6IkIN6v15Pzih-_U3lyIocPUtAv3NRqA1CeliorhUnDyNbPr7s1ly0PtuPgojzm7jE7d5-QSS2eeeZs6Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460611eb6b.mp4?token=aG7mYwDApynRhMoH1rNgkFHL-q0n0o-k61JCYqxlKS8ZhCYh9MBepc-HgcDOn7Bm1iSdlCqMtHRyywYUUassi5nGnjMtXLfRCqG1SgCYPTbK8qSkLWFOulpI1w8vYrYlS4HkvnuKX8rOnc8LKvoc5DnNfQVrU0X7LB3JUZcKqyfCM5llRAJWAHo5Xj6QDrbnGYUOo1pYfZ47od9rHHSkClMVGNJiTdLSvdcSqlAYV_OTF7yzQt9mtxzI58Z49JhBTWzG6IkIN6v15Pzih-_U3lyIocPUtAv3NRqA1CeliorhUnDyNbPr7s1ly0PtuPgojzm7jE7d5-QSS2eeeZs6Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
فوری/ "
یک کیلو طلا
"، جایزه باورنکردنی برنامه جدید ابوطالب.
استودیو "
پامپ
"، این بار ترمز بریده و با ابوطالب برنامه جیمی جام رو ساخته.
🚀
🚀
🚀
جالب اینجاست همه میتونن، با روزی چند تا کیلک ساده، بدون قرعه کشی از این یک کیلو طلا سهم ببرن.
🔸
بزن رو لینک که زمان خیلی مهمه تا بقیه سهمو نبردن. ...
👇
👇
👇
👇
-لینک شرکت در مسابقه ۱ کیلو طلا-
حتما بدون فیلترشکن وارد شوید</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/658787" target="_blank">📅 19:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658786">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
وزیر انرژی آمریکا: ممکن است به عنوان بخشی از امتیازاتی که ما ارائه می‌دهیم، بخشی از تحریم‌های ایران لغو شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/658786" target="_blank">📅 19:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658785">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: ایران می‌تواند هفته‌های طولانی به سوی اسرائیل، موشک شلیک کند؛ ایران هنوز هزاران موشک بالستیک و شاید حتی خیلی بیشتر در اختیار دارد که می‌توانند به اسرائیل برسند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/658785" target="_blank">📅 19:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658783">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKZAlr6Fv2zCfVuXrQEvn3HpV-0c6b9P4ccckrJv1HEAFm4JcJOsT4ycl3H1Bo_1YrIuL1n_ykpABwsCWKpGHTQaE7TyCpg1-f8oZB0Vbr7kNgg1xhLmy9O13657KGFb-_9qyGSjmb3Co89HT9vKnKbi6CTsE68x2sKVRkChuTnEOo4CNU6sKFjyyUJsVWhYh85_ERPFsfVoV4VG3-BTe-A_9gu3xXMr40byzKBSF1LRubyoHDJvpwXeVzUCAYOIEx8IqP2ch6Ua53gL1dc36h9BTuopLSAXclvGfg7MgyEq9eKg23uUJxSv4CbaY96u7QfmNmuPweiOKYVymZEDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e359b1457e.mp4?token=WNaHM9biNg2B2wZ1wIPBjAnNgkj745zcJwRCvFai-y3MIHFKG_f49SVwO-QEvH3GhdvAOfm2EdAD5UFwhTvi95DoiuinDIrCdLsFxEslCQuAesL9ZgVFWhKdKhauXbjV2l7-PwZ0uj2QXtIiA2VsQfIZork0iH9WN9ss31zXawVLi85lD7PfdDH-xNXOlBf-PxUoAyl2km8him4uxDpGmG6tAbeaXpUhjiRTXJiWwvj3Rqt2pCESUMezU5y_jXllceyeAIsJCqagdnPK9ueffgh1G0_2aLIbHOMuuDLdpIn0XolgZiZcDpLYqUAeOwGJ5Vr6hvSxSzNS-_3GgC9XR5SmjNh15g1K0LDSPngMhqO0LoO3BK9i0fTRB3XJ8AQ4KfnNtwaMlTmgNJY3Dq0QNTCNCDDcoj-k12ZlLt39mbg_aVLkimJlCTs5tWZiuBa65nvGTvHPrKnf93rEtC4dnYxbjtsMTjAVnw1I-m55yHM9QeSUI2TOEbVk06E9AXry-WtAtlBoZkMoq-RJgnyVDpC5QY3Ba1whs4Orp7-1oES-oCsDyQRvEQhlTcRhdLz7vjaEvMo0-nVsS8XtTm8PpgIc-o03F_x-q6rjki-Vo7nF736wO0PnmoFJipef7aakLnHOHhjuL5N1z1eMC1CI2vYrtTKItWv9Y3oPs2U1fn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e359b1457e.mp4?token=WNaHM9biNg2B2wZ1wIPBjAnNgkj745zcJwRCvFai-y3MIHFKG_f49SVwO-QEvH3GhdvAOfm2EdAD5UFwhTvi95DoiuinDIrCdLsFxEslCQuAesL9ZgVFWhKdKhauXbjV2l7-PwZ0uj2QXtIiA2VsQfIZork0iH9WN9ss31zXawVLi85lD7PfdDH-xNXOlBf-PxUoAyl2km8him4uxDpGmG6tAbeaXpUhjiRTXJiWwvj3Rqt2pCESUMezU5y_jXllceyeAIsJCqagdnPK9ueffgh1G0_2aLIbHOMuuDLdpIn0XolgZiZcDpLYqUAeOwGJ5Vr6hvSxSzNS-_3GgC9XR5SmjNh15g1K0LDSPngMhqO0LoO3BK9i0fTRB3XJ8AQ4KfnNtwaMlTmgNJY3Dq0QNTCNCDDcoj-k12ZlLt39mbg_aVLkimJlCTs5tWZiuBa65nvGTvHPrKnf93rEtC4dnYxbjtsMTjAVnw1I-m55yHM9QeSUI2TOEbVk06E9AXry-WtAtlBoZkMoq-RJgnyVDpC5QY3Ba1whs4Orp7-1oES-oCsDyQRvEQhlTcRhdLz7vjaEvMo0-nVsS8XtTm8PpgIc-o03F_x-q6rjki-Vo7nF736wO0PnmoFJipef7aakLnHOHhjuL5N1z1eMC1CI2vYrtTKItWv9Y3oPs2U1fn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عروسک‌های جام‌جهانی به شکار قاچاقچی رفتند
🔹
پلیس پرو در عملیاتی عجیب، هم‌زمان با افتتاحیۀ جام جهانی یک متهم به قاچاق مواد مخدر که هفته‌ها تحت‌تعقیب بود را با استفاده از لباس‌های عروسک‌های جام جهانی بازداشت کرد.
🔹
در این عملیات چند مأمور با پوشیدن لباس ۳ عروسک رسمی جام جهانی ۲۰۲۶، به محل حضور مظنون که از طرفداران پروپاقرص فوتبال بود، نزدیک شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/658783" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658780">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tc1mx7uPhtkEpRQQ4o_B_giV_Fz4g3hMkw27TFdt-V_5XDLyjn6UEzt8QEydTVI5tuAYW7oAmMkQNvCUrZj-vLGDPvxlpQF9Zz7aXjtCr3YxP3j2VC4FdIROlA6sl870rOrGG2sSRZatuJBXP486hY4YS35yovBZA_Pu7mwK7Ni-Yi1_R8X_TCHdGr3VINs77hGf0a2Av5PSteKup_AlUP3zeb3JvBtLk-TjiS-pQM210NVCWyQvKR-ki_4rBWlJ4zrOiVaH7qaE_v5Iw6HW7lXUxkgq9Mcj1Od-BbpMYj_Y8zeIqRgOMcjwgeFwoV13STz4Ucx-M3qYe4tY_uc0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdIOheOXxN_jes_IQ30MrK6lAIa9KiVy71NJJd7WwqUH_TbZ5HeNDfvQaHxhstWEDJ2Bw39-TatjVADqdnJF4qFikoguBBOSfDm8K0Hkgvs61qOR3FBmNo6dFNFuC0fR4res52lixWBxVDUDdb8dudl5ACb1eHLcW1KX2HLsx49F5DEXGb25Pl6aCrCy7c1o2VChemK9qJ5zrAR2AM2uQ_bCWSRQm2UhRsVEritul5rfKEalr7jo8o2205QYS99H0z82NsXPEFHmIS3zVUVjBlDketTaOQbUWikLXXGbjFXtvi6NOYPiYMwHEdrRtWHI-EH9eSEDBU1L7BCt7wV2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdGB6CrtUxq1bPwW_I-RsZjBkQpZp7Jc5EtkSfRJqAPHVGqDFiYnuCtslyEYaH4yps82oPgOq6TJJs-LZ7hrvmgnY4yA0sZ7glDWepkEi9cN6K8XAFJaXM4f_3i5CZrsCPW4Ayj5ycNL77RvxU4eb42hZtVrE7M9-j1hIsb_6v4MbHbyIXpI8TpejgL0UNUMU3f1GnusSoREEUkTAYOrrVt6Vu7K3wtLU1RQTs3tBYB3XHZUJUBtdgRKPrRHQuWJPNblRIfTORCmJLgHJL4ItaUqIFocYFQLHlTIgMNbJTXwKmEdRPoZpEBKXk1PTXY1N_qsFsqMqaMwXQkTz5cZgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ساعت ۱۰ میلیاردی امیر قلعه‌نویی در فوتوشوت‌های جام جهانی سوژه شد
🔹
این ساعت ترکیب رنگ آبی پودری (Vibrant Blue) در صفحه دارد و بزل که تداعی‌کننده شخصیت‌های کارتونی اسمورف است. در حال حاضر قیمتی بین ۴۰ تا ۵۰ هزار دلار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/658780" target="_blank">📅 19:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658779">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZaEXzd8mxbCQlsA_1p1P51e4FP-_n2apGNNzyeDPA4nZOX9l6P7MU_GQliYE5J_cTKmLnGBQZ9_IBVU8NLkVkD_ziA-CyiZTS-xvbxLAENg_na6cZM1QJxsEh1M9k-voajF94vnWMx0cqqBBLIePrBMcWNQhkn9wkiNrPsaFtD35fVj2VLRbyAHZoIBpNLrJ2a3cocNhkCBbFpLi-uSgh8O8PdiWBMyTcB12JftzVa4tF1njiCzXcsyn3YirF1kdZc5_s9nd6TNYbkLZo_IDdi7cWGbGKAH4ryT91J81eS_OnVaPCfONYvhnxg8XuQfAJ3HJqSW4RK0BdQw-J-FVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر ترامپ توسط تحلیلگر بلژیکی، الایجا مگنیر: ترامپ امروز صبح در شبکه اجتماعی خود می‌گوید ایران قابل اعتماد نیست. بیایید تا ظهر در واشنگتن و بعدتر در عصر منتظر بمانیم تا سه نسخه متفاوت از این موضوع داشته باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/658779" target="_blank">📅 19:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658778">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d528980e58.mp4?token=sluEJcxEYAc9JYqZ02p1030ne1kdeZjuRFcZIMtz6AGhXpykrhuEtxJ1K8C8yFFzyKFrTy1r2F9i3wb9q3CBJH2G4xf4SYO9ejVRkx3gHntOs61rRhakzLz24nYl1zW_Dd9c1xId-nDRHGa2qXVGBzOdFUyUlW0V66V3zVm4rDYLtN4DQtyk8bIdZAiwbhGlxWhk3VGwEl6d_JMs1cb3xUmQoWFO92GaWEP32tKITEGamMqvA0xVommaEhCjAbRxglRQqeXf-_pHhOYQ1fldKdr4WVVyEYM9gZ6mfqyurKQQwveMD9q3LcZhqHcnvDbGt5UCXz3wZwOFsYQGTHAGwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d528980e58.mp4?token=sluEJcxEYAc9JYqZ02p1030ne1kdeZjuRFcZIMtz6AGhXpykrhuEtxJ1K8C8yFFzyKFrTy1r2F9i3wb9q3CBJH2G4xf4SYO9ejVRkx3gHntOs61rRhakzLz24nYl1zW_Dd9c1xId-nDRHGa2qXVGBzOdFUyUlW0V66V3zVm4rDYLtN4DQtyk8bIdZAiwbhGlxWhk3VGwEl6d_JMs1cb3xUmQoWFO92GaWEP32tKITEGamMqvA0xVommaEhCjAbRxglRQqeXf-_pHhOYQ1fldKdr4WVVyEYM9gZ6mfqyurKQQwveMD9q3LcZhqHcnvDbGt5UCXz3wZwOFsYQGTHAGwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی، صیدا در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/658778" target="_blank">📅 19:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658777">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb34BGfbP7KcPbiBl0I0fC9IKcVj4rLLWlG_Oz6gIn4uQlTD9UEs7CaAcytHi_ibK_2aMv-ygDYVghVN1rbaakoBA1OuVPy8KVtc965Qz8dN7onu-BV8afRJqtSyGqh9IBXc5XL5hUwC47uXn610XQbZcZQye2gSXluxgtmfVAWbr5LczwHoyZ7cjIcQB9VwBw6Lvzl2yhC5MuXsYpxEuLNqAKSMkfbmgGSLZcQ7iIka9V3Ix8RjlSr2JTHqkohhpIWkwqIAm3UhCe7V5OpIam8KBF0Pj6UuYUQk8vrIvTiFbhHVgDSr_oWASGX2o-_7PH2x8kza1_4aGRutQXQsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع سکه‌های جهان را بشناسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/658777" target="_blank">📅 19:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658776">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFAsNL0nfQdb9mNu--fdNRTdo4IEdJdHUdpkCv4Iedy0nOGx-kgs-XkuxoVTJNo4ncakauLn6RezHXOzfl8f0C0aIsgEjeNU6ZkAl3LSH_9uOhpuqwmsPE_YL9sNuMXBSjIW11hZ60tzNxdRbV_69zPxyfyi_WiOPYzTOvfOO5BCH46uPpwjHBujgxidqP8Gol-v0f0hZ2zP3Ya01Nq0aW5x2teKGy_tMWiHRFrAZvj8Mcr7-9A5_KBx1kO2_uBi1di5XOgsIssQKUHPsM1madtoLCSVyACQrMdyNV108rLUPvOJnVVBBnbOVV1lgQmFWp5XcCMT1OuFq2uImQlKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترور مرد موشکی روسیه | راز ترور ژنرال موشکی روسیه چیست؟ | ژنرال دامیر داویدوف کیست؟
🔹
ژنرال «دامیر داویدوف»، یکی از مهم‌ترین چهره‌های برنامه موشکی روسیه، در عملیاتی مرموز در مسکو کشته شد؛ حادثه‌ای که بسیاری آن را به سرویس‌های اطلاعاتی اوکراین نسبت می‌دهند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3222432</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/658776" target="_blank">📅 19:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658775">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
۲ دانشجوی دانشگاه تهران به علت آتش‌زدن پرچم ایران اخراج شدند
🔹
شورای انضباطی بدوی دانشگاه تهران، ۲ دانشجوی دخیل در ناآرامی‌های دی‌ماه را به دلیل تخلفات انضباطی از جمله ایجاد آشوب و اخلال در روند آموزشی، به اخراج محکوم کرد./ فارس
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/658775" target="_blank">📅 19:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658774">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPfHl_ayu1P_GzE-RZhG4lUyVqM2HQKB1I0fGkoyVJRidaKNokryLbAyouLCBCUCcAFEzsGhvsBC0Gh-kfVseW4lvpECoiVV82xlU0IiQFh0HHp3WURTRh54pey-ajPR3gWIlwbrfynncadSg-ibqI23Bu_aZdHbiOlCx_nRaQ9tlImLPy8yYTSvhFn8KXw6WHHE3v4zkwxVoyWNgZ5AvlXDa3oisxcBWvepwLx8eyhRywIN6www5rCjYXBv5VVLlXYsFw0z76vVQ7hKaxztXKZt-Zxz_4kudf96zcmDYK0BrXhHv97RadDMDTrvJ8Q-Kx5WTzsFPYwAGByWDvJJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ توئیت عراقچی را بازنشر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/658774" target="_blank">📅 19:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658773">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50ad5cc5f.mp4?token=q7ANfWg2Mo_oqMY2imCQUKE8_UslfANJqELEcP-UF9JkYDwimNBQXkg7U5EdhxCeFmwpuydaOeoPQhB1C_Cx9s-r48nXPA-nIfoA11HMWzURNjCp1J6Fv-aEDbb1YcgtH_0ZdfKfL0vXWQqSmxTfeYdco2Jx1L13-V6HKXEzh5VKAkAYOuWg-OSWP4pgXf454xp9NjCJbfzrTSijo-kOk-zra6NbSzZvrazlgRVSYVu-N0EZEED1LgxarYT5dznE4MiWEqI3UXKxl2NfbnCQMIQaXpCeexhpysUbywGUCPPFAXUod8KdX5BHzxfQl21Rp8ej_6vt0OJu8nuv8qdE-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50ad5cc5f.mp4?token=q7ANfWg2Mo_oqMY2imCQUKE8_UslfANJqELEcP-UF9JkYDwimNBQXkg7U5EdhxCeFmwpuydaOeoPQhB1C_Cx9s-r48nXPA-nIfoA11HMWzURNjCp1J6Fv-aEDbb1YcgtH_0ZdfKfL0vXWQqSmxTfeYdco2Jx1L13-V6HKXEzh5VKAkAYOuWg-OSWP4pgXf454xp9NjCJbfzrTSijo-kOk-zra6NbSzZvrazlgRVSYVu-N0EZEED1LgxarYT5dznE4MiWEqI3UXKxl2NfbnCQMIQaXpCeexhpysUbywGUCPPFAXUod8KdX5BHzxfQl21Rp8ej_6vt0OJu8nuv8qdE-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی در شهر میدلند در آمریکا
🔹
منابع خبری از تیراندازی در شهر میدلند در غرب ایالت تگزاس در آمریکا خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/658773" target="_blank">📅 19:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658772">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/442cfd591b.mp4?token=niAthzpzk0ULCH-N1ppH3i4Dr58Szuv0FvYqS0izYZkdKqgjGyTw9abP2Uf3eNvU530oJn7PIrn_vRt18AVNSk8nN3Xt-GRM9htRhPLpJ9jhuW5mCtEs6-ajW0kDX0FexACfDsiT97pO4VB9A2LK_FKEKMaseWTbAbm3R9LwW13fFGl7xlCupT0A-jYkbK9U5nArvQDwRAM69rrnHC6cO8Dt4h7WVgjefAOsk9GM-q6jTlTSWNqMCXLNj3U9DpLJd92RmdLdDD49dCo4H0v_HpeiYxlzauWv8tinEhS6CXgqHEawnUwpBItc2JChIcapkVnXwVOFy6jyAg9uT6HqCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/442cfd591b.mp4?token=niAthzpzk0ULCH-N1ppH3i4Dr58Szuv0FvYqS0izYZkdKqgjGyTw9abP2Uf3eNvU530oJn7PIrn_vRt18AVNSk8nN3Xt-GRM9htRhPLpJ9jhuW5mCtEs6-ajW0kDX0FexACfDsiT97pO4VB9A2LK_FKEKMaseWTbAbm3R9LwW13fFGl7xlCupT0A-jYkbK9U5nArvQDwRAM69rrnHC6cO8Dt4h7WVgjefAOsk9GM-q6jTlTSWNqMCXLNj3U9DpLJd92RmdLdDD49dCo4H0v_HpeiYxlzauWv8tinEhS6CXgqHEawnUwpBItc2JChIcapkVnXwVOFy6jyAg9uT6HqCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گردباد گرد و غبار روی مریخ که با دوربین مریخ‌نورد پرسویرنس ثبت شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/658772" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658771">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
تجاوز هوایی مجدد رژیم صهیونیستی به جنوب لبنان
🔹
هواپیماهای جنگی رژیم صهیونیستی، شهرک الصرفند در شهرستان صیدا در جنوب لبنان را بمباران کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/658771" target="_blank">📅 19:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658770">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a028JhqAUrZKLPzU-l8IUvBu-v-xWzHN2Uj3FqEjipBtUj59x9qke5Z5HuU9DHFP5KeA85zT-us6sX1q6uIeZQZdPWtR7yBRFO3wBezj4Xr9mqXh2R9gV8xP_zljSpOMiL4tO3PedBSHmpKPeMY0jGhcHjtE576Plu0O80dqRPQqNdo6qo-8NYWc3278GCEUFsGgliog0YTCjX_sAZOkbAu1obRj8T0TSluYtCinp9Ad2fjqoVUGAMkgw40vvsuIoSA5GbDhhbpT-d-fkGOKrwxegUYJWTP6wUVUNiO4DFgay26xTJY61FokaoX30-rPs6_2_FWCtfJeJ9zSZhfEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/658770" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658769">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
آمریکا ویزای رئیس فدراسیون فوتبال فلسطین را هم رد کرد
🔹
جبریل رجوب، رئیس فدراسیون فوتبال فلسطین، عنوان کرد آمریکا ویزای او برای حضور در جام جهانی ۲۰۲۶ را صادر نکرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/658769" target="_blank">📅 18:46 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
