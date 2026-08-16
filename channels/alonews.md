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
<img src="https://cdn4.telesco.pe/file/LXXJysPkfnr6ohUwwySTf_PLF1oj5fiy1NAp47WWeQrAWGddwEtwj3eNK5YwIALbs7BoLCSmD1bJmTPfxI42DsY_satgGzeZdVmBikov0lglnS2KyWOhsNScdJhTzhROVqcjuluSloIvWe_CyNrqTsxx3GL2hbA7GC3sXTZmu19eD8pP4ii5VTyLbo2FgzAaWVSCnX03CbuO607R14eWaBVCBxNy0aFFbQJ_UC097_t7zX-5tLnm_g62CqAo_J_3JtdOeDBqyQLMMIBtk167HLBHfe3BAs2jAV8oAGNLP6tDDStik_H1RtujevZxAwFCMw0kIO0ZKgeMWaJJhHnzGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 15:50:12</div>
<hr>

<div class="tg-post" id="msg-142053">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
معاون برق وزارت نیرو در پاسخ به این سوال که چرا خاموشی ها طبق زمانبندی اعمال نمی شود، گفت: خاموشی های اعلام شده در اپلیکیشن برق من احتمالی است و وقتی زمانی را می نویسند، یعنی در این زمان احتمال دارد برق برود و آماده باشید اما لزوما به این معنا نیست که در آن ساعت مشخص برق قطع می شود!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/142053" target="_blank">📅 15:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142052">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
میدل ایست آی: به دلیل «وخامت شرایط»، ناو هواپیمابر جورج واشنگتن جایگزین ناو آبراهام لینکلن در خاورمیانه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/142052" target="_blank">📅 15:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142050">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ooao2tlKJKTWOsTKDeDH5DMTLfTAIryjZdcZaFqKoA86BaiJrh2zBpS-PROKiKv8gm8Hm-G1Xxe4cCfTfkBE7nIobNolOXXeEKRgjrI6Ps5-E03EiBhpHn3bYNJsEztUC-2Szu0SY8QL2_Pjt3q0dQUODK6JoCuo7Dwl5nnm5Z2_SJdftBdeTrjQRttxcQd6aGaeYvCiZwj6twZhYgeAYHhGtfKcekLgp4n_3Df7UXscPaaB7YlFp3sSR_RcQXtsvTGIxqfM28oKfZBCnuyYmxSzaPajNaHQgqB-w0gcYWIytznC7HHGXXjW5C3OHtsoLokGnm8lB5d6myA0RxxPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfEvPVX55Y3o3PxehcD9pggw1hMJKAGF7FoL_EJQK7DPLSGO9_INOB-8BNCL68BElUVvkjFNUKE4Q6L_muLDc7CpjEkS4sBKyeFkg_SNrQtSlcgyNxAvTMffxWmE8QxbmPoqz6-snygPTLI3BzGNG_Iczjbn2YNrlhARNPoIWIs6uiOOCGm5T-4wuQzuK9jPueLUWqW7fRhXci7uJbbDvWTvbSSTIFUilAxhEQH6q0VC9rXTwJoMknRqn6vKw5ccF05qvk09UsAmTB7GD5VfogdqF8lMhzBhmkY5y43CCnsmY2a7rISohHCx3m2xkeqe1O1-pjcvMyox_ZoRhFFP8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حالا عکسایی که این خانم به رامین فرستاده هم منتشر شده که منشوریه و گذاشتیم تو بات تا ببینید
😐
👇
⚠️
مشاهده عکس‌ها
⚠️</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/142050" target="_blank">📅 15:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142047">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
متکی ، نماینده مجلس: ملت ایران منتظر صدور حکم قصاص برای ترامپ و نتانیاهو در ۱۰ روز آینده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/142047" target="_blank">📅 15:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142046">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
هم اکنون حمله پهپادی اسرائیل به چند خودرو تو خان‌یونس، جنوب غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/142046" target="_blank">📅 15:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142045">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
معاون وزیر نیرو: به دلیل سنگین شدن بهای برق در بازه‌های دوماهه، در دستور کار است تا دوره صدور قبض‌های برق به یک ماه برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/142045" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142044">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
معاون بهداشت وزارت بهداشت:
امیدبه‌زندگی کشور به ۸۰ سال رسیده درحالی‌که سال ۱۳۵۷، ۵۵ سال بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142044" target="_blank">📅 15:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142043">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWwr8Ed-Q9ZGvUl55KO-QJcXhxYMY59e57d2kl7Z0Tyn5pwQEhWG6LzgbWLJZKiYZjRJsAlX3kjfRQClebQBTRFGD1ct_TMf1rVNOcEc7sz_GPRWnzw1khm6wjSQgzg-oa6S5N-XPsuCIs16oIxbgK-VYeZjD_sReRkMyhlylE-mhTWrq_TYKSM1SFPbsDNTd7aP6sXYjl35vnM0krjxHLFwNVGcq3kad6QBVEuobM8vZB2ssTHqpEiwqmbD_3U5jYbZHXPJNafGb00KbJLfMRslol3LkKjSBOtHbJBdDmzlZ-ZE4W90lV2zKlY3SRzodHbZZlXDvVC0MJsky5BM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین ۴۳ هزار سربازش را در ماه اخیر در یکی از خونین ترین ماه ها از زمان شروع جنگ از دست داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/142043" target="_blank">📅 15:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142042">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مجلس: ۵ تا ۱۰ سال زندان برای برگزارکنندگان دوره‌ها، کلاس‌ها یا کارگاه‌های آموزشی حضوری یا مجازی که با فرهنگ ایرانی ناسازگارند؛ ۶ ماه تا ۲ سال زندان هم برای شرکت در این دوره‌ها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142042" target="_blank">📅 14:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142040">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egvh1SajPe2AZOJewufsqdtc8V4ynpl0U3MlLASY1Z4ZOkuhohpGrv80FhJIvdVterpRt5_LPkW0B3SuXyFzjB7giaKXW5MFCUwvkLYRUZVlP7HX3zJ9MKn5Kofgg3yls1fgQhRHxUMYz4Y7sMxY6hhfCUAU8QYoMcEAQHjxO9xBs-QOCcUhA6iOwRFAI2NChrufp3dHKoPVXDyKdKt4hjNMtmzVb76ibSFoe6ZI1wf4E8K-DQxU6za3JVhg1yqbD9DYCjEp97KxCnNzP5ppyxdG1404jfpd7-sM6IP12xc9rtdhFOd-kHpRAm1CJ_noEYzduC3Rqm0lre1eVRs3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMUIidycaKU3RuYYA6IfslzoqVoVhaf4lZFzsfJeU36OjajODg4t40to1gjNcMdgnZSdK96eY__Fqyz-4CJAxxZqGg7cVy3GNwJvwgjf2JMtcnY74xJUCSY_wyjDELPN8O9vMVqfxaPSKhv5ZOX6gaMuZKYes7EDXRM9ANsIffxSbemjMPnznPWm7K8_oSD8hxWV5fuBbUe0Ebm070KK1BQtvAiZNxSqpxbdFdHbIuEy4W1RO7M5tNQD_Sp8HHsGHXfaYpZheUPfhkVnuwG5xWQsltZPiZLfPiLz6H_8fQTvF-gZyWyG5CWtaKPdcnKw8aC9YpfQhyYsm8zISDnKow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک نشت جدید نفت خام در تنگه هرمز رخ داده است، و علت آن هنوز مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142040" target="_blank">📅 14:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142039">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaPbsooSe6fGXoF5CEwct3lZA2sYopY8lBIrGd_RSLdmAuQiQMD45URPExaviri8GPODA_lX5LDjYyXfVLZzm1rleOKpRfJ_C1njN9Xu9ZBM1j53arVCjEEdQw4kNirnkeE9Jd7gqF6k-TL08raK1ww_-IqfNvw4MZt2WaO8wrh1GDjSpfoydObciQANYQorS4WpC2Hw7om3fB5YpuICmJsAKuVhlE8gobwqfqQxgWtTGb5VJMi-NORgrI8ptCzxUlzzTqGUPouqpgUVnyghIkzNReirzyq6ONZgKOQSTV7edOulqt33JmDAV0vety-XBrgTekalZe4OhWFVC-vVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی جملات و عبارات “دشمن صهیونی” و “ اشغال اسرائیل” و “ مسلمانان هیچ وقت اورشلیم را تسلیم نمی کنند” را از کتب درسی مدرسه در چارچوب برنامه سعودی ویژن ۲۰۳۰  حذف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142039" target="_blank">📅 14:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142038">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b1f639be.mp4?token=gvEK1LIzA88kZZCpXy3xDU7ikSGXkgUkyMg_ihTJKwavaCmyLIB0sKavFisORqhxly38_1N3Nmmu5PGVk2UUkb1iToATHunc2rfkYaIEORgki4YJ1BTfKzsb2ZElLCtjC2CsxkicVggRQ_nP1dH0DFlILzQTUFr06X1bOa8L9muq--eR-uzga61mgy2I6MzHxv_Jx_n_t7BZZMgvtTjuh-6W_i0CvQavCfs-5KnwQbcaTR6q4hl76I7W5wsIU6ZC3yABH15TgZvz7x7tPLiyul83nXOGX-bC3p4LswDYPy6ve0iUUqwMKcndFZQKSNnkdsNZkKmQtKiJa57hGSIqkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b1f639be.mp4?token=gvEK1LIzA88kZZCpXy3xDU7ikSGXkgUkyMg_ihTJKwavaCmyLIB0sKavFisORqhxly38_1N3Nmmu5PGVk2UUkb1iToATHunc2rfkYaIEORgki4YJ1BTfKzsb2ZElLCtjC2CsxkicVggRQ_nP1dH0DFlILzQTUFr06X1bOa8L9muq--eR-uzga61mgy2I6MzHxv_Jx_n_t7BZZMgvtTjuh-6W_i0CvQavCfs-5KnwQbcaTR6q4hl76I7W5wsIU6ZC3yABH15TgZvz7x7tPLiyul83nXOGX-bC3p4LswDYPy6ve0iUUqwMKcndFZQKSNnkdsNZkKmQtKiJa57hGSIqkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سوال صداوسیما از رئیس‌جمهور: نوه‌هاتون بهتون نمیگن کاری کنید که مدارس مجازی بشن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142038" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142037">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سازمان غذا و داروی ایران اعلام کرد که در جریان جنگ، ۴۴ کارخانه داروسازی و ۷ داروخانه آسیب دیدند.
🔴
بخش داروسازی همچنین با ۵۰ کشته و مجروح در میان پرسنل خود روبرو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142037" target="_blank">📅 14:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142036">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142036" target="_blank">📅 14:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142035">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وب‌سایت اسرائیلی والا: تخمین‌ها در اسرائیل نشان می‌دهد که حزب‌الله و حماس در هماهنگی با ایران تلاش می‌کنند تا تنش‌ها را افزایش دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142035" target="_blank">📅 14:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142034">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
درخواست عضو کمیسیون عمران مجلس: حقوق کارکنان برای نیمه دوم سال افزایش پیدا کند
🔴
افزایش حقوق پرسنل با وجود اینکه در بودجه مصوب شده بود، دولت به طور کامل عمل نکرده و ۲۰ درصد افزایش داده است.
🔴
در حوزه معیشت و کنترل بازار، اقدامات عملیاتی ضروری است و دولت باید با جدیت بیشتری وارد عمل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/142034" target="_blank">📅 14:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142032">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142032" target="_blank">📅 14:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142031">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
همتی ، رئیس‌کل بانک مرکزی عازم عراق شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142031" target="_blank">📅 13:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142030">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG3wk31sAr0d4ftSxJ7BjTsGuY6n3HjZMLxc04f0MX07CC3vdVHSypsiF90-aNw0kb74kgVPtOnf26OHS2tXoS6kJ7nUewfQSnRebfnAOe53zTTk9Hhob6As1mhwx1PkmOHTaCiEfWOgrqgqubaE9TPq3YFMlsn6RCc6zVtWhejQXKNO-ejcPzecI5YfpfB7PMPAiYQa_Ayk98Gj5ctAcMJEvX84GLyni9yyod3AqM9wdD_0QHUuU04_44S8PhelkcSqXqMzbIrtxamhHAA-WvFoJeY2RWQeeF4v249jkLqHdDf94rXSLq7tZN-jf530A-_UFTBB8hAezkfZjkMb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ورود مهاجران غیرقانونی به اسپانیا از مراکش همچنان ادامه دارد.
🔴
تصویر مربوط به شب گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142030" target="_blank">📅 13:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142029">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxHbb23LEUqb5ge4pmdT0YhT94-b_lQVy0XS1Qwli3I4sq1ecBtD07JfhssXcGTvWHBvajNgdG9z6_yksO1T-JN5k1kuDhkDSXftM1R_gPGD5dp6ggTueRDzzzuZmOOE5Et4Kc24JWVigtUCblXo85Z7bPqWGT_vPFRgtK1pESXHd18kw7u-tdAC3vvvk6vhIOhsCSkYyhFtK84Px5_XlVAb6r3zLfgx9v40ukEitSLAFGD-EHEL4UUUocToOwkYA2FX_qYQhc2RBBprTFaDpJQ9oVR8St9hPTOQUzKjxV3qaV63n_cEkxS1IVWmjY80iRIO9glNBxGGXks4X9dkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای مسلح دولتی یمن: در ۲۴ ساعت گذشته، ۱۸۱ عملیات نظامی علیه حوثی ها انجام دادیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142029" target="_blank">📅 13:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر امنیت ملی دولت اسرائیل از نتانیاهو خواست که فوراً حملات به بیروت را آغاز کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142028" target="_blank">📅 13:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142027">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT9ux6klV7mqagHNk6ZM6Ci9wI5OcPL7e5S42ypyytVzqaZBVh0V45twQ16l2haUjMgzEZ5ERR3mSYQdfQyzZxWxAorDQwF4iiocWmK9GxcNPYOVtmIkGLpwPpLKit60vz9FMHH5zwzOueDVFb4uIFdMV2Ja26NLUlZe8WRya9QrBcbi5MLt9up05MErHoww03kQ0KhJZFY7MbHqG7HQY24mjJspyWe_uA4IvdujugnvLKn2dLIiCsdeYAo39CKwKZ6Eg6fgaDRNwHoWlf8cJF5Ww7tknEMhOwAWFyQyh2ZV5Zyt3tV1P-nJ21EM0CUBhRJN893Lw3bI3qdcRsk2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: با تبدیل شدن جنگ با ایران به یک نبرد اقتصادی، استراتژی جدید آمریکا یادآور استراتژی‌های قدیمی است.
🔴
استراتژی فعلی شباهت چشمگیری به تلاش‌های قبلی آمریکا دارد که سال‌ها به طول انجامید تا ایران را منزوی کند، با این امید که او را مجبور به دست کشیدن از برنامه‌های هسته‌ای‌اش کند. این سیاست نتایج متفاوتی به همراه داشت و برخی از تحلیلگران معتقدند که فشار اقتصادی شدید به تنهایی نمی‌تواند ایران را مجبور به تغییر مسیر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/142027" target="_blank">📅 13:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
اکسیوس: مقامات دولت ترامپ، مذاکره‌کنندگان ایران را دور زدند و مستقیماً با رهبری سپاه تماس گرفتند؛ کانال ارتباطی آن‌ها نچیروان بارزانی، رئیس منطقه کردستان عراق بود که اعتماد رهبران آمریکا و سپاه را توأمان داشت
🔴
بارزانی در طول جنگ ایران و عراق در ایران زندگی و در دانشگاه تهران تحصیل می‌کرد.
🔴
او به زبان فارسی مسلط است و روابط شخصی با بسیاری از اعضای ارشد ایران، از جمله اعضای ارشد سپاه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/142026" target="_blank">📅 13:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142025">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef6cee167.mp4?token=lSBAqwJMv_jzNvc53rsH_RfeCw0rN1ceEnep6yMMU4H3bmZ6R-nciso9fBCvpk5-hEV8iWFQpuUJUGFp_IfRsz39N8oI0S6eClw4kkYvq__nPSWxzCWeRxhCSMncWOML-1KVMBI3HU6CmnBizCGZkVOMe4IoPT7jqaL4AVPlB_jQnsNlX236TCwEBg82XTdOpWMIeQfmncsAnkjcE3X2VlglBZJqjTfzH1_fw45sZ7f9hoTaXWtcam-L53jB6iwaDCfX98ys4hrTHsx3elWiTF4ds3-_9wRxWKOfM1Dpk5EmWxbdzTFCc_OWbR9K7mP6yXv6HUbKEPkOk_JXV6BFxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef6cee167.mp4?token=lSBAqwJMv_jzNvc53rsH_RfeCw0rN1ceEnep6yMMU4H3bmZ6R-nciso9fBCvpk5-hEV8iWFQpuUJUGFp_IfRsz39N8oI0S6eClw4kkYvq__nPSWxzCWeRxhCSMncWOML-1KVMBI3HU6CmnBizCGZkVOMe4IoPT7jqaL4AVPlB_jQnsNlX236TCwEBg82XTdOpWMIeQfmncsAnkjcE3X2VlglBZJqjTfzH1_fw45sZ7f9hoTaXWtcam-L53jB6iwaDCfX98ys4hrTHsx3elWiTF4ds3-_9wRxWKOfM1Dpk5EmWxbdzTFCc_OWbR9K7mP6yXv6HUbKEPkOk_JXV6BFxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در اوگاندا، گردشگران سفیدپوست ثروتمند به ساکنان محلی پول می‌دهند تا آن‌ها را مثل دوران استعمار روی یک تخت آهنی حمل کنند و به گردش در جنگل ببرند.
🔴
این یکی از تفریحات پر طرفدار در جنگل های این کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142025" target="_blank">📅 13:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWp9aSaXE9UPSk8Vn-IzG2r-3hOYxb8i5ZTKTvniKkL5f7V1Ve7fEJVv4jprNzicVqS_vAbXo8Q0j9KqLkAtp5YI0dQeDzwU2in5WyMCjh9o4-GRpyaiAue4RTOmSMaiEiqn6CIwxNCQmi9D53uWIK_LE67ivaYkVHIFMliBz_pECqaaKTS87QeVOHzHUSurrofaIRchBKOQqA4vJAT2PF2USsuORgfYDGy2fMnc0vs-sOLMBUv0FSYpsI3ItWg30bz_0mBvp8I_9bndWT-YE3p8GXf5MeDYm5pi3I9dModsw90C_TQEf2Ly5Y_rOUuvteMGgwu63bdZ1W6CnV3rgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حالا که صحبت از ایران و نقشه ایرانه
ببینید نقشه ایران ( سرزمین پارس ) رو در زمان امپراتوری هخامنشی و پادشاهی خشایارشاه، نقطه اوج قدرت و امپراتوری ایران در تاریخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/142024" target="_blank">📅 13:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa-SFRkvsFDY_xK-CI9bNKaNh4HVh6T8jVWGekD8dxzDxjg5NLWZCwgFjjGu-dEKEYxyb9iSAmM5yu-cAK4yR5i4oiiIH3oT8e1BR6herq4o3eWQVHNKpk9FjZk8ZiZl-KkbUzZ3k2Z9ySzIqoOahQ9Qndz9RQQ2k-X5Pt0VL5xgsqolmBC9QbA7R2Y63Dssy-hrEhEvwndpUatyLmC2BRwAffimDf2Q5NOLdwWhLXTi8BPmu4onk56YycrQqBnehJesJ-Jp73zL5gawxc6mCPEGj_vLzkHeffW7DpdtJW55W1WhwhGdVkdKWFW00MOkqJuK7rPGM-D4J2_bi-n3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین شریعتمداری: وظیفه جمهوری اسلامی در قبال مردم، فقط حجاب هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/142023" target="_blank">📅 13:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
المیادین:بر اساس مذاکرات جاری میان ایران و عمان، مسیر جنوبی لغو خواهد شد.
🔴
تمامی نفتکش‌ها ملزم خواهند بود با نیروی دریایی سپاه هماهنگ کنند.
🔴
بیشتر کشتی‌ها هنگام عبور از تنگه هرمز، مسیر ایرانی را رعایت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/142022" target="_blank">📅 12:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فرمانده ارتش: هر ایرانی ای که یه سرباز آمریکایی رو اسیر کنه یا بکشه بهش ۳۰ هزار دلار جایزه میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/142021" target="_blank">📅 12:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142018">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lggbo-YeSSXRmQ0DNzUT8aSojRoryEj37pYG7aBMXNyeMY8wS2hJUqnf5z-9WxiixjPh5qRq1pbNce8RL0wZkbpo-2uDt7jTQghh6VD2r6jc_OLPqS4I-3wbtn6UWMtZ6UEJ89fnjw0Zi0W6DMXBNlRi3jo-CL7hzAm5GVKE-rLh3Ee5dwwLuxGh_drYDvI9bkjr6_3H9niQEE2qNQtBho4vv0Bw4hgsND8k7Ogs3xUdwnXinAl2fFNswrVeOASwjGeoc9qk5nwria3sLC1gkiM0Wjh0CJpRet9q0b8sh7YenESlE8f542K4ueA3yg1qpcZ22Ub0U4fjh-y6JsqNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIPSDanq_qOJYZseospJX_dT4fxVVBKTN4YaVeao6SumvyybLQ0VXz4wKZXXSgpTWb3OEc0RzLjDLGpjTQjuAiV9-DxwI27u0GVRFp-282lYyEVPiKUSfQotfURADAygofolX8-L3GCLbjkVTYFJD5cdAZLXpLFFAjeuNBnijaA1NyBrWJf9hEIyEes6EWKBNs4BdIziU_voGAl8mAzmKUi2toVhGsOvlu2cuxqH6-v-zX-cE3Oy9BRKvsMWTwre7i1MylRx-GRTdwTmPfb0C1G2Oy5klOkjUEHiIIr9Ed4GqHZprXTUqoxZWTZqNbsMm-tz5jkyIEKfSfYbWyjzMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKMTHLaP43Aje2tQRil6K4guN8y_3t2fUgVNxUe6y_Wv-LCoajEYQnFD-ZZwXdmSgDHSAMgvr2wpzDw4XaJouhNIu5U_s0Z0Mhm-ua0kLkTAXTQUkYGxhDgpqarB5iCNJ6Mgd3z90Ll7wAoIu-6AGZt3KIHYFGuCcOF4tvbGWI0vfvRzN2cpJBQRkpvNvx-fflxe_C0ajQopLizD5lWWECkwjw_7uPqyDyueclTtKqqSEqYoFo02Xsn_K8DlytiUsBpFHLPbPsk6RyjnmzqbrNomB4LDBbkccRhrl5GiFQTctJSkSGDcwzfvjB_zgJGaJHZ_bUzUAn6-vH8JWWaANA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
همچنان گریه زاری ملوانان ناو ابراهام لینکلن:
🔴
طرف ۳ ماهه شیر نخورده افسرده شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/142018" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142017">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
مصوبه تازه مجلس: ۶ ماه تا ۲ سال زندان برای مصاحبه، شرکت در گفت‌و‌گو یا هر گونه ارتباط با رسانه‌های آمریکایی یا رسانه‌هایی که آمریکا آن‌ها را تأمین مالی می‌کند
🔴
مصاحبه با رسانه‌های خارجی دیگر منوط به اطلاع‌رسانی به وزارت اطلاعات است
🔴
۶ ماه تا ۲ سال زندان برای ارتباط با سفارتخانه‌ها و نهاد‌های غیر ایرانی در داخل یا خارج، بدون اخذ مجوز کتبی از وزارت خارجه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142017" target="_blank">📅 12:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142016">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فرماندار مهران: صدای انفجار شنیده‌شدهٔ دقایقی قبل در مهران ناشی‌ از عملیات معدوم‌سازی مهمات باقی‌مانده از جنگ در خاک عراق بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142016" target="_blank">📅 12:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142015">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مجری صدا و سیما: مردم میگن حاضریم ده برابر این فشار رو تحمل کنیم اما راه شهدا رو ادامه بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142015" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142014">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
با بخشنامه بانک مرکزی برداشت وجه نقد از خودپرداز بانک‌ها به میزان نیم درصد مبلغ برداشت کارمزد خواهد داشت.
‏
🔴
حداقل کارمزد پرداختی برای برداشت وجه نقد ۳۰۰ تومان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/142014" target="_blank">📅 12:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142013">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
معاون وزیر بهداشت: مجردهای قطعی نسبت به دو دهه گذشته حدود هفت برابر شده‌اند؛ بنابراین رفع موانع و تسهیل ازدواج جوانان از وظایف مهم سیاست‌گذاران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142013" target="_blank">📅 12:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
شبکه سی‌ان‌بی‌سی به نقل از وزارت انرژی آمریکا: میزان ذخایر استراتژیک نفت به کمتر از ۳۰۰ میلیون بشکه کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142012" target="_blank">📅 12:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc02639fbd.mp4?token=lSg4Sl3jRQL7bH9T43F5lWfFi8cBcCTOc96IhtoZ5ep6mTqbqFTAyMl5_8DgPGQKcjRH_mJwy14covmRyHONQZZoBRV06OmzckbLRxyGfOurt9O7G-5dwUxf80HTrGfp7qcZinTaPsoeGf5M3CD-wEG0kbT72MlxvLT0RW4y5KnhJdEN_ClN3PSi1vo8X2YkAoR1j41ghsTpaT9pxExYTQB44xu671w-jBtekKx1zH-z-43Bw3tYoG_VsM1vi76iFDXruJEAW6iyQJ9KyxxMuOpjlbp2uPLRVlWSNjOPWVZxhn1zsDQwkRbVyWOGNB1K-d_XXORgIQjBFWdq8OWjKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc02639fbd.mp4?token=lSg4Sl3jRQL7bH9T43F5lWfFi8cBcCTOc96IhtoZ5ep6mTqbqFTAyMl5_8DgPGQKcjRH_mJwy14covmRyHONQZZoBRV06OmzckbLRxyGfOurt9O7G-5dwUxf80HTrGfp7qcZinTaPsoeGf5M3CD-wEG0kbT72MlxvLT0RW4y5KnhJdEN_ClN3PSi1vo8X2YkAoR1j41ghsTpaT9pxExYTQB44xu671w-jBtekKx1zH-z-43Bw3tYoG_VsM1vi76iFDXruJEAW6iyQJ9KyxxMuOpjlbp2uPLRVlWSNjOPWVZxhn1zsDQwkRbVyWOGNB1K-d_XXORgIQjBFWdq8OWjKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به دلیل حمله‌های ارتش اسرائیل، مردم جنوب لبنان رو به سمت بیروت، ترک میکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142011" target="_blank">📅 12:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142010">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzM1waey_m0wzG60lrhdTi9y60hPskZukyUc-Y7kQBhHo4JJQ4FWxByxPdLW4Od6p8xap1Aph9Qr4YORWpbqKvzED3oXhCbl524DxxBXEYtd7PKlHecdqf1snJXwFpfQYaNv52232xwPPbmSOFOzqAGkT5fuyJR_a1TAKAYWZ1y6i0OUixh6Z26ywsIvQ9gHv_ZvMmCsn23f7aLt3PGvX7-2kSnv9baYLcU77hRTDNQ28OqciqXXyynOE9BYCG25TsddQjgMqKQRa_JCo-KcB27GJ-87UDp6rblyVaM3FS5pS-yjVAsAOSy9O8hToviwfXeFIuZWEnZHtSFFAM339w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حالا عکسایی که این خانم به رامین فرستاده هم منتشر شده که منشوریه و گذاشتیم تو بات تا ببینید
😐
👇
⚠️
مشاهده عکس‌ها
⚠️</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142010" target="_blank">📅 11:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142009">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3995b6e7ed.mp4?token=GfqtpMX4ZOLVjO-9l25ZtD9nRn3oMVsCfbqjHWCeRoO48OuXIM9DG3LsMUWqUv6BY4W6t_DjVdh0hfMGfe_1hOCEDM-sjx-rrI9kHnbJzIWwcE3Nl-4470iyp5ABMMLa_fiA1xWRXj8REzGxKB2c4aDWs7Fmjr3gNHOBfLsAxQxdj4wkG2SLi11BlGprSUnAZPR5acZioZ2o0K0qmtQP3ne1-Scx_NKICM-8SpNVVd1VC6D1iwP_MgwAG06pT483vxyucXHe4UnmmLUOHIzW57vacFHvibs-b0qrh3uLg3J9VPMFkOF3pPd5rB91ofBV6wvGH8hLMrJh6YSVn-r0ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3995b6e7ed.mp4?token=GfqtpMX4ZOLVjO-9l25ZtD9nRn3oMVsCfbqjHWCeRoO48OuXIM9DG3LsMUWqUv6BY4W6t_DjVdh0hfMGfe_1hOCEDM-sjx-rrI9kHnbJzIWwcE3Nl-4470iyp5ABMMLa_fiA1xWRXj8REzGxKB2c4aDWs7Fmjr3gNHOBfLsAxQxdj4wkG2SLi11BlGprSUnAZPR5acZioZ2o0K0qmtQP3ne1-Scx_NKICM-8SpNVVd1VC6D1iwP_MgwAG06pT483vxyucXHe4UnmmLUOHIzW57vacFHvibs-b0qrh3uLg3J9VPMFkOF3pPd5rB91ofBV6wvGH8hLMrJh6YSVn-r0ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واژگونی یک کشتی مسافربری در زیمبابوه که بیش از ظرفیت مجاز مسافر داشت، ۷۲ قربانی به‌جا گذاشت که ۱۸ نفر از آن‌ها کودک بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142009" target="_blank">📅 11:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142007">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
طرح مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در صحن علنی مجلس تصویب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142007" target="_blank">📅 11:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142006">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc12aa96d6.mp4?token=WXSfu3n54fxfDqJyiKQ7vwlQs6_lSIOg-erD7PKMU331qWkLTpqYOpRyyFqJoOTLOj4FgsSvroExQXxjj4Eluprcoid5zvruOHRDzRHPIbs4R4TPPWoJoP_y1IymSZ8wuee8Ro-dDKg0D6W5tljZF2e21GVbEP0u7ODayinXB8G3Ps6bYB7kPLhNlGtkw_iQyAQ8s53ZeBLiIDV0xpDPVU1XyWTLN6iZr2AUDqL1277wAXzgaj1c2mmxieFgjnezjwVzU-qrMde75HJERpgHBe2tb6nHhE_LDsFpLYbERJWJnltvevXqGYjDcKkVuUIUsr5vtDFZ06IyRPZZTFtNvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc12aa96d6.mp4?token=WXSfu3n54fxfDqJyiKQ7vwlQs6_lSIOg-erD7PKMU331qWkLTpqYOpRyyFqJoOTLOj4FgsSvroExQXxjj4Eluprcoid5zvruOHRDzRHPIbs4R4TPPWoJoP_y1IymSZ8wuee8Ro-dDKg0D6W5tljZF2e21GVbEP0u7ODayinXB8G3Ps6bYB7kPLhNlGtkw_iQyAQ8s53ZeBLiIDV0xpDPVU1XyWTLN6iZr2AUDqL1277wAXzgaj1c2mmxieFgjnezjwVzU-qrMde75HJERpgHBe2tb6nHhE_LDsFpLYbERJWJnltvevXqGYjDcKkVuUIUsr5vtDFZ06IyRPZZTFtNvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: تصمیم نهایی درخصوص بنزین طی هفته‌های آتی اتخاذ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142006" target="_blank">📅 11:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142005">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fba31c7725.mp4?token=rNSDsHflPGMT4K2tpeA63G2FRIDEzrYn-PuanMPEhAoD3axxgkXGx2QEOC9rLlj_96x81ywRKu8SIqmZWgJ4-bVYqUp8ksYizK3FG4iBPzymQqGYp8Z8ZBBOLNnDQOJ4JQBO-klgzlMfFExzVtwD6moKeUtQybPCqILQGFbpXL0OrPryC2D3gQr_9hSXEhMbyACG2JF_Zo0TEM4p1mKxdR8urN0zuGA-rU1d-RweAiVwd3KJCzG9VWZtwuokRR7JEfKWsENbb-4mnmKscVDxm5fQYvo0VGxwQON3EAXb4P1KN9u2K2eZkR_7_hAG66RkoTS4hvaKDez4SDjLB4fioA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fba31c7725.mp4?token=rNSDsHflPGMT4K2tpeA63G2FRIDEzrYn-PuanMPEhAoD3axxgkXGx2QEOC9rLlj_96x81ywRKu8SIqmZWgJ4-bVYqUp8ksYizK3FG4iBPzymQqGYp8Z8ZBBOLNnDQOJ4JQBO-klgzlMfFExzVtwD6moKeUtQybPCqILQGFbpXL0OrPryC2D3gQr_9hSXEhMbyACG2JF_Zo0TEM4p1mKxdR8urN0zuGA-rU1d-RweAiVwd3KJCzG9VWZtwuokRR7JEfKWsENbb-4mnmKscVDxm5fQYvo0VGxwQON3EAXb4P1KN9u2K2eZkR_7_hAG66RkoTS4hvaKDez4SDjLB4fioA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آرش اعلایی، خبرنگار سابق اینترنشنال: اسرائیل به دنبال تجزیه ایران هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142005" target="_blank">📅 11:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142004">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کارمزد ساتنا و پایا هم با دلار بالا رفت
🔴
جدیدترین نرخ کارمزدهای بانکی نشان می‌دهد کف کارمزد پایا با رشد ۳۳ درصدی به ۴۰۰ تومان و سقف آن با رشد ۶۰ درصدی به ۱۲ هزار تومان رسیده است.
🔴
سقف کارمزد ساتنا نیز ۵۰ هزار تومان شده و کارت‌به‌کارت تا یک میلیون تومان ۱۱۰۰ تومان و با هر میلیون اضافه، ۳۵۰ تومان بیشتر می‌شود.
🔴
معاون فناوری اطلاعات بانک شهر می‌گوید که کارمزدهای بانکی نسبت به وضعیت قیمت دلار خیلی عقب مانده است؛ چون خرید تجهیزات دلاری است و دستمزد توسعه‌دهندگان نرم‌افزار بالاست باید متناسب با آن کارمزدها افزایش پیدا کند.
🔴
پیشتر رئیس‌مجلس گفته بود که افزایش نرخ ارز نباید بر بسیاری از کالاها و خدمات اثرگذار باشد؛ چرا که اساساً ارتباطی با ارز ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142004" target="_blank">📅 11:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
کاخ سفید : موشک کافی برای ادامه جنگ با ایران داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142003" target="_blank">📅 11:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142002">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در محدوده جنوب اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142002" target="_blank">📅 11:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مدیرکل فرودگاه‌های هرمزگان: پروازهای جدید در مسیر بندرعباس ـ اهواز برای تسهیل سفر مسافران هرمزگان و خوزستان از فرودگاه بندرعباس برقرار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142001" target="_blank">📅 11:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142000">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر: ما قاطعانه ادعاهای مربوط به بازداشت خلبانان ایرانی را تکذیب می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142000" target="_blank">📅 11:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141997">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_MvC-Y3TplpT3VTTKfSHG9oxtAJK96nOMqycKx3BKW99h0_iTT4_gQ469MjZdkORGNaji3ZpFWPbK9SbYh8dZkmA-GIUIuzPpCTqaPtxCULEAcKZvlcG2x-aBLnol0tHW5HvNNyf8HI_RWqy5Lqzc3FXe6Nq1zXV9B41VJnnqSzS22Df4mg3Mb1gKwgXkpj4oT_TCGXxWbePNIwftwdcJTMRowWj_XJtwfZE4aQfhuDxQvxz9tw0Wn3LBer2-yU2096vm7mcJL3rPvorJC_Yo256yKq--wrTdU_BFuYiAZ1TFcgwCUv-MDTpnfk-MrTXiMM8g9HqYVHo-k5qxnTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/El5ZAtEqZYGh3GYUlwVaJx8EuO_tnDUjSyG3W65y4trdl5KOoR2rNku309Zbzi9idxyxNsQV2gEBIQX26mXjVMFaMYsBONij02LmyPUJ8-Gycp6OJnucNmOVLy2_CWcn9bylllLNMr-4JGGi6yf6bEFIODgvXfLjwkDW9pgBTbRri02lFREFWp8KcSOYol7hdgiO_a2JGOT0KX6k1Y5l1LzCDTyhKq2Ok0NGuiWzeVMwpNmeI3ELF439slveaEp5SUaxainPf0RjXwdwD1wdNIDvQtBGF-ydR6y-aUMmSWJxGLC_qnn-DRdfB8wuebtaoPWbqjLGEkPH13odXBuLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0UMi-FoJ4_rTnysy4SZED7vKISpO4zAKtfGnVS91oq3KFMuS6w5rfpBVa5JtskftML3CRBCmftig8l6aNm_vuqJsdN1Z7gHDzSPxAQfjX4CRNQe0ZpqIIteET9o8kHBxodpCjJDnVxeZdC-TVLl4XJblY6zdcdeITZJ1QC-5O87Op7OLNs-B07CbtCw8n0WAx-7WZ1EhdzSyZdjtmValeG-oSP_11iDxzLpSGMOTsr-D5Phx1zSZ8DPyc3XHrIl9rUb9zgixxSrxlMUufI7uMJchs_reqAqj9lGq5JMGOs4dy2dU2PImPlLVW62dlMp04HlY9Uc5DExFGlsTUwWBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌های موشکی از یمن به سمت بندر المخا
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141997" target="_blank">📅 11:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141996">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
استانداری: حضور روزانه بیش از ۴۵۰ هزار نفر در حدود سه هزار کافه استان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141996" target="_blank">📅 10:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141995">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اردوغان: بسته بودن تنگه هرمز یک مشکل بزرگ است و ترکیه و ایران از پایان محدودیت‌های کشتیرانی حمایت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141995" target="_blank">📅 10:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141994">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
معاون رئیس جمهور: نمی‌دانیم پول فروش فیلترشکن که بین ۷ تا ۱۲ هزار میلیارد است؛ به جیب چه کسانی می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141994" target="_blank">📅 10:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141993">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFUoao7YfW_Bhdl9RpKLujzwSlMswu4b0HdIoQB22WOAwiHtTz_d2DdAqUbZuz1r-YJY0GVRZS2xWqpjWvhXyzLhQIHklNVXcl8gZITUsvVPFV_-b-4Kl_jWHirgoW9HDJeju0zc9njnMvAKz0xuR1a_CA3iI5tR5i1o3FRwa0uXf1cISKnwO6IaqqqRtINZhHNV0aXVnz9uKiTaG04R7UybbW8OZepl81J2kEo7szBYjhh54SdznR6SZoYoQm52Asr9JF5UOsEKUDWwY1caDFEd_kh2HiwnO86JwQ4SzZyE2hQzFjao1eN-hwCGFwN1wCrAwG76qZY-lbTII3tEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس روز ناسا راه شیری را بر فراز پارک ملی یلواستون (آمریکا) به نمایش گذاشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141993" target="_blank">📅 10:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ارتش اسرائیل در بیانیه‌ای اعلام کرد:
شب گذشته در حمله به روستای دیرالزهرانی،
ابو حسن علاء یکی دیگر از فرماندهان ارشد واحد بدر حزب‌الله را ترور کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141992" target="_blank">📅 10:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سخنگوی هیئت رئیسه مجلس: از تاریخ ۲۹ مرداد ماه به مدت یک و نیم ماه دولت فرصت دارد تا وزرای پیشنهادی اطلاعات و دفاع را به مجلس شورای اسلامی معرفی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141991" target="_blank">📅 10:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سنتکام: فرمانده سنتکام براد کوپر سفر خود به خاورمیانه را پس از بازدید از ۶ کشور و یک ناو هواپیمابر به پایان رساند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141990" target="_blank">📅 10:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
معاون رئیس جمهور: نمی‌دانیم پول فروش فیلترشکن که بین ۷ تا ۱۲ هزار میلیارد است؛ به جیب چه کسانی می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141989" target="_blank">📅 09:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141985">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rFKOolSfAqX45m2KK5bLnwaPp9DQsnIDk0t5EZft7LrPePFQ0ZeIUzwe6Lqeq-sKkYUNGMVvNiX4jjXmqS1R3TJmHvNf8fg2u7Um1pwVA4e8T086FdFECPN7LbBF6sroNJUNCMBvCSfYrCkxAjDSd-MWGY9KbXWR6TM49rjwdrVr65hKrluZqeBWa--l342bc79vgCQTJLmO4_EigBbzpSF6t6d0XClEVFTzqCVbRVw2Uqg-UVMfCmeDr9K_ZcfAaHRST8Pt0xrHv8zQWg-NXzKFM8sCiyGuxA8szX1MLBaHOpXkxSrSufKn2wNKhyfxciIWaWQP9ZIYNF-QPEMpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMNe_ZD7ng5NqquTRJjSUI9iK3JDt9839lZkKAznmRMq8briA8HhVzXXWrkL_DfUic41fYL_JbsuZErsQQozz_p1KNbcCbnaMr2oSGRePs_w7DWWjk2xR-IRyXWgUuBGLcxHWVD-59hNYsSrHxB9W6lmNcma56l8x2FtlOig2lZMd_flNcoBmKEXP2r5MU1DgYl7d6aCWrlO4dYq51zZAgA2xuIuz364GFPD1I3bXAjVVGaPiy54bvjuSOjqCLb9pUTaUU-gg6hRWAKJm11772G0RxFjU_FiMrMXHSIvmdl70wo6IZOqRnWKq1j9slWA6eqZ_phBor0iW55jheBIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9kssWs6aVbTaK19PKVG7xPu84aAUiNP7aKlWp2y1DHB2Sg6ffhvX5Lve9C7WUigHLvb7nIBTyHJgmyrY60BgfVK_TIBw6flirXmzPNHh6jDc_CT40FrdHgkG5pQnmca9KUe5-e-5NjtpyEP7XWxd7RpqMtBUY-L-Wm36Ay7sUnxyOsHHuGjttvkfL1m9rwpheDLn2jJuoMWPj0dc_F0S26jnd6nDjo8SjB-IG7FrLVQoJHlIAYh-_G6e8VFLursexmuLxg3RT61JtZSBDT6nhokp74PGYlhPuGb4vx9FjD0fzw7-8P32XDnSNc8Lj8l34Adi821GY2B00tsxaYScw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee38384b8.mp4?token=N9P56vlFdWLR2CMYLBJB8-iFUjVMnc2IQDlleLWtsoGPqY2IxZUFp_7gU4zdyXL8f3WK-RXvzWsVgF7YWXmWtU5AoGTozhko_Cc0bJrZ5bzQDYmg4ToFOiPkWhNgRqa08U57aqVmb_XR-q3THWshd9vBCv9tUmpAygPt50_fD4mlnwrMVZX8CrXZH4o6rd3dfPPtr0WdN1Cjo4-U9KPuhAF-R77SzmSol4nYodzfuz1OHFNEsqWiEuqd2MNHMa9cWII-pzPbJMfkTsU_qB3ZeYkBobgVbKUPV6SN0xmfke801WpQomt2I9Aw90bXHcrQ9LW5mVGGQ1pGuvHNm073Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee38384b8.mp4?token=N9P56vlFdWLR2CMYLBJB8-iFUjVMnc2IQDlleLWtsoGPqY2IxZUFp_7gU4zdyXL8f3WK-RXvzWsVgF7YWXmWtU5AoGTozhko_Cc0bJrZ5bzQDYmg4ToFOiPkWhNgRqa08U57aqVmb_XR-q3THWshd9vBCv9tUmpAygPt50_fD4mlnwrMVZX8CrXZH4o6rd3dfPPtr0WdN1Cjo4-U9KPuhAF-R77SzmSol4nYodzfuz1OHFNEsqWiEuqd2MNHMa9cWII-pzPbJMfkTsU_qB3ZeYkBobgVbKUPV6SN0xmfke801WpQomt2I9Aw90bXHcrQ9LW5mVGGQ1pGuvHNm073Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌های اضافی از آتش‌سوزی در انبار Wildberries در منطقه کولیدینو، منطقه مسکو روسیه، پس از حمله پهپاد اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141985" target="_blank">📅 09:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141982">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpydTvONKk9rvinF7rFDHlyaeTMWhPYmql6UZ6UoDHR_4ONS6RkIMHQQpWH8bYW4SL7cDA49cZoZ1-R6F_ZcmF7fz6BNsuYrx1hYJ7kqZTo5x3N6k2yMZPGd56ish7atbYOhyWN0j9Qj_wP02_0Ozw_swXeIt0TI_37afw7DzmQOWfZp9hKOujZXYYYd8_7by56UqH4m4XQaWiyugviMRwxgT9XYkj0CtS0xZo541oIgME09bwQJZXQ3v4O9o3pjvyfmzQONGkFsUl8V5ymCJ5lY3AQpokE_74VqnSkyD0c3zSWe0T-Wf_EMi0koTmwjgLQP8tofD2z8lmj1kGvCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3138a8e31.mp4?token=Rg0wB0m1fWVIRcqgbfgWp2BFf0LLh126KP2L9Wh9dZcspEpABiaFzlm2qA2M4OI96oU-l8amb3vh7MpQlXxQaD5ACqL4YOFl3w5Je-d26Gcsrb9hzvKhC9-ggiNn9NESPyKi-KVJmnzcwmHfqEG7lng-snppI-yD1lerRSdirF90_UjA-avSsPbbY90Q4CZfpbP1n5PJjxcbOzKWxTwfKFe2lh60jMhANpTPQMoWvl6T1SOtJ3UnY_qrBwTA272I8lm-FvHJ2Wds3AYbSNRLy1TOtjcS236dw4kVQykMUtDSEv35wemNkNF63C0RsioWFFzkfCkEVLW973Xvpbxokg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3138a8e31.mp4?token=Rg0wB0m1fWVIRcqgbfgWp2BFf0LLh126KP2L9Wh9dZcspEpABiaFzlm2qA2M4OI96oU-l8amb3vh7MpQlXxQaD5ACqL4YOFl3w5Je-d26Gcsrb9hzvKhC9-ggiNn9NESPyKi-KVJmnzcwmHfqEG7lng-snppI-yD1lerRSdirF90_UjA-avSsPbbY90Q4CZfpbP1n5PJjxcbOzKWxTwfKFe2lh60jMhANpTPQMoWvl6T1SOtJ3UnY_qrBwTA272I8lm-FvHJ2Wds3AYbSNRLy1TOtjcS236dw4kVQykMUtDSEv35wemNkNF63C0RsioWFFzkfCkEVLW973Xvpbxokg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی به یک مرکز لجستیک ویلدبری در کولدینو و انبار دیگری در دوموددوو حمله کردند که هر دو در منطقه مسکو روسیه واقع شده‌اند.
🔴
هر دو انبار در آتش سوخته‌اند و دود آسمان منطقه‌ای را که درست خارج از پایتخت روسیه قرار دارد، پر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141982" target="_blank">📅 09:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiQYf6ANv0FHMAfGW_y06S6VpHdc2u1SnpvFGGoCdvA2KY-tM0jTGZhCn6ArAubAo7TJ34uhmA6Xui0y0MRj_5dkL5iCp7K1n3yXBRhhvV6GOuvCe9HuiD2Rl6k2NeDIcZylXPQOC5djvF-lGZg8iClDFzqgecbmgn697bmGd4k9j1tILHP436JGIs32S5aX7sru2WkYCicpzpjKl1ai2o05WkuzOM7Jq-gXtYEmPdrnFUzEg6Mkc3us-JdURXoqLtnn4tf2YOSxBvcOW9gSwkfkz1DD4Nssy2SlsvcApV6KN8elh-vuZtOhUMAzu5VoAMR1_OJJc7d4QAjo0vdhtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری میزان وابسته به قوه قضاییه از اجرای حکم اعدام شهرام صادقی، از معترضان دی‌ماه، بامداد یکشنبه خبر داد.
🔴
صادقی از سوی دادگاه انقلاب کرج به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا » به اعدام محکوم شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141981" target="_blank">📅 09:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
آغاز پروازهای مسافربری میان روسیه و سوریه پس از ۱۸ ماه
🔴
خبرگزاری تاس بامداد یکشنبه گزارش داد که پروازهای هفتگی مسافرتی میان دمشق و مسکو پس از بیش از ۱۸ ماه از امروز ( یکشنبه ) از سرگرفته می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141980" target="_blank">📅 09:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
یسرائیل کاتس، وزیر جنگ اسرائیل: هیچ حساب باز در هیچ جبهه‌ای باز نخواهد ماند. ما با قدرت از سربازان و شهروندانمان دفاع می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141979" target="_blank">📅 09:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4zDuDgc06bBYJFwqer1vrhEks36_2B1v9rpwJZjurXZ9d8BWujzPiv0Ilr9YwwFtJ7RzgGV_0POv86CbWsKmW0oaYvBB5QvlLbTw1C8GlYwsA-7vtAsgllsKGb4D6E2m4W16fTjxVI_MTBMZhQCzrc9iY4EzZGNtPJ3LCwAooTCJV2djmcOGh8Q_NnHVHTmWZJ_sHaUNbUph6FSEQpwJRk0R2Y5bSCwF2PZpM4_GFdpYT-xjay11Desfk1jdtyew3HN0nhGvk26r8n3c8vj4AaMEkdk58h55wUXiPuBoZDNyrU4BZEz5Lt--R_Q4CyzmrGScZ4q7_kjrLp1Hf8bDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران، اسماعیل بقائی، با مقایسه انتقاد مارکو روبیو از اولویت دادن ایران به هزینه‌های نظامی به جای مردم، با اظهارات دونالد ترامپ مبنی بر اینکه ایالات متحده باید «حفاظت نظامی» را بر برنامه‌های داخلی برای مردم آمریکایی ترجیح دهد، از دولت ترامپ تمسخر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141978" target="_blank">📅 09:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d33efc20a8.mp4?token=V9mhRtxUnyDAYupRrr8Lb1ynxmyZ7mBgZ4_LM5KCFg-u61-spKocFxRnQHXIu44oNcdzZK_IQu6gBDllLnGlGk7GccAf9zHMUi6amAPpZhXsIpFYBctmI65k7K--EKcyWaMD4oddIihfFcYTdUdViKjtR5se6RMNoZhZni7LzEkJU7qJifTpwLV15nyeKfgGeERGftIY3VC9vUUZFJ1N6-7R3soJ6xUonu4z8VaTJ4YwcSpQvr_kxNvbXfbceL1pw-zH041dLQoL-GTUIqPlKx80kp3CycQ0KNtQQfbjFwXJtKyLKtpZcLur_ieDkTcPbMuOLd6sWosvDKGCeLSCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d33efc20a8.mp4?token=V9mhRtxUnyDAYupRrr8Lb1ynxmyZ7mBgZ4_LM5KCFg-u61-spKocFxRnQHXIu44oNcdzZK_IQu6gBDllLnGlGk7GccAf9zHMUi6amAPpZhXsIpFYBctmI65k7K--EKcyWaMD4oddIihfFcYTdUdViKjtR5se6RMNoZhZni7LzEkJU7qJifTpwLV15nyeKfgGeERGftIY3VC9vUUZFJ1N6-7R3soJ6xUonu4z8VaTJ4YwcSpQvr_kxNvbXfbceL1pw-zH041dLQoL-GTUIqPlKx80kp3CycQ0KNtQQfbjFwXJtKyLKtpZcLur_ieDkTcPbMuOLd6sWosvDKGCeLSCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع و شعار قربانيان مهریه درب ساختمان مجلس: ما اشتباه کردیم که ازدواج کردیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141977" target="_blank">📅 09:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت دفاع رومانی اعلام کرد که یک جت جنگنده اسپانیایی مدل F-18 که در ماموریت نظارت هوایی ناتو حضور داشت، یک پهپاد را که به طور غیرقانونی وارد فضای هوایی رومانی شده بود، سرنگون کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141976" target="_blank">📅 08:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ارتش کره‌جنوبی ادعا کرده طی روزهای گذشته خط مرزی نظامی توسط سربازان کره‌شمالی نقض شده و با شلیک هشدار، سربازان کره شمالی عقب‌نشینی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141975" target="_blank">📅 08:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4860f711f.mp4?token=D3nZ_BIvXVlbvu-3Z4lkiX31FxZvuB2uh5NPH1mpnUtztZs4BALBhZ8s6LTktwtvz-HwSYeK1X0Itdcze8vv-phYy5VHK67jutiNL5vXwsDEXNwy4SENwtuQdJLxqQXKfTNsttmOJ5omhWKpbl0NtBA4-mOwIaj48Zgkw6dXKnkK0oW_TxfiC4oir87ingZGaJkx5Y_I1mCOa_rin_Dh3bua_VIyKQOBc-zF15tZsVkt5ULiAj69qHsnqpAHFR1YhXHIzwW8gh7XtxqqZ_NTdmVmfQOkZpLb9AJj0-Pt3IfQqpntpcLk5EtIRpQHnESYOSkrUOdTDa1QzIwT9XCnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4860f711f.mp4?token=D3nZ_BIvXVlbvu-3Z4lkiX31FxZvuB2uh5NPH1mpnUtztZs4BALBhZ8s6LTktwtvz-HwSYeK1X0Itdcze8vv-phYy5VHK67jutiNL5vXwsDEXNwy4SENwtuQdJLxqQXKfTNsttmOJ5omhWKpbl0NtBA4-mOwIaj48Zgkw6dXKnkK0oW_TxfiC4oir87ingZGaJkx5Y_I1mCOa_rin_Dh3bua_VIyKQOBc-zF15tZsVkt5ULiAj69qHsnqpAHFR1YhXHIzwW8gh7XtxqqZ_NTdmVmfQOkZpLb9AJj0-Pt3IfQqpntpcLk5EtIRpQHnESYOSkrUOdTDa1QzIwT9XCnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی وقوع تیراندازی در پارک «چارلز یانگ» شهر لکزینگتون ایالت کنتاکی، دست‌کم یک نفر جان خود را از دست داد و ۵ نفر دیگر مجروح شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141974" target="_blank">📅 08:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-O--S_l9JhUERQxesM9wuOI6t-wZLRldFahrbyVlYm4DUavEmfL7x0FRGmngWG8FacWwNkhm-npCbGROFuyBVspez78Uj5gDVuKTJpHgkDkyvE-BNz9rJ61AdrblMiUU00DwC0OXFE0lOmYe6KPglPJk2Tad4S_6W89uV8qtMmyoiRoEwEgty7eHpurfL6lIqdX1ksEgzUd2DgdA1olQQpRLqBv7JbwdmQ75UplvEBBEld-g98lfk3QqUQOu9W88diGLL6WFSWXnOJsuMEfrcAfTM4WMOBJlOFFDseoLmCMxojuhjMdV-LYYe3bM5PHeRZGrifZVN5czP6E8C4kUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام نقشه‌ای منتشر کرده که در آن غزه و کرانه باختری به‌عنوان بخشی از قلمرو اسرائیل نشان داده شده‌اند و در ادامه نوشته: فرمانده سنتکام از بحرین، عراق، اسرائیل، اردن، عربستان سعودی و امارات متحده عربی بازدید کرد.
🔴
وی با مقامات ارشد غیرنظامی و نظامی دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141973" target="_blank">📅 08:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZeQ6EeoIgYbgVsneT9kCEltJMIhnP65SIOmYDhyWSvp3skvhGl1IR76vqSVeql8akRSYlp4keMHblrnLON-u-77-6eHvXMp_FHJeRCwHodaFdD2b969MDiBom1lK3hPSRIyr38zo-fiYxJFqh77N_Evgad6NOeKgNRw_cT3XOQD4qcOHLhe4G6tDuZedg1r-QdBQSYT4kT9ZyCrihHPBy4kKpdT7_wvz9aA_2-FW_xVboNOPPX2p5qf3CFNmfEhIyhLbh_eSUq2XbFm5QrksRFNUELM7Y3c9UTCy7y9uU9IXoNlmMUlrJgp0VAkdrM8nbV-9cIu7PgzN9vg87AuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی:
رئیس‌جمهور ایالات متحده باید به جای تهدیدهای بی‌پایان درباره تنگه هرمز، نگران امنیت خودش باشد.
🔴
او گفت ممکن است رئیس‌جمهور آمریکا مجبور شود «در یک کامیون حمل مواد غذایی پناه بگیرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/141972" target="_blank">📅 08:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d324cd6a04.mp4?token=vWl-5Q_mwQ_DFVZKgkQeeMc1I7KA4aknytkRiFxFTs1lPahkUdbFwSiF15UW6nHoM1W7YWEfNJ_HTIECH4f16V65UPtx26ehKHqfRI9oVjixsSC65jD8G3V9Pj4P-zXBN0iGd4mHapxnlQd72bBtY8CacKQaL-WEs3-e8Tb5MVBvbMzMby6cgLRNvvgBj3SyCC2wtEQKztf1-N7Nq7KocJfRinRHwWpJx7-eUNV2Sdrh4DxuLwonZwQrtSruWkORrgXGXgjujjIPWDir7x-H88JigUo9W8mHrTZo6wIojUgZorJdyUyAWTgty-yiMzHoIwBT-U2nRCm6YffwN5Pz7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d324cd6a04.mp4?token=vWl-5Q_mwQ_DFVZKgkQeeMc1I7KA4aknytkRiFxFTs1lPahkUdbFwSiF15UW6nHoM1W7YWEfNJ_HTIECH4f16V65UPtx26ehKHqfRI9oVjixsSC65jD8G3V9Pj4P-zXBN0iGd4mHapxnlQd72bBtY8CacKQaL-WEs3-e8Tb5MVBvbMzMby6cgLRNvvgBj3SyCC2wtEQKztf1-N7Nq7KocJfRinRHwWpJx7-eUNV2Sdrh4DxuLwonZwQrtSruWkORrgXGXgjujjIPWDir7x-H88JigUo9W8mHrTZo6wIojUgZorJdyUyAWTgty-yiMzHoIwBT-U2nRCm6YffwN5Pz7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چینی صحبت کردن ممدانی، شهردار نیویورک با شهروندان چینی این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/141971" target="_blank">📅 08:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911d977485.mp4?token=L3hMmOyUsecjsl8iFO4nCPJgbnTrJ6kTJxA5zkRT-hFQIJlAOkPtfR4UMVJ6Vyc2Ow8xStwYJoFkL9WbfEDT0aPjWB9MQckcsHrCV_9SMDPUxhIZOJdCzUt-Gv5cFhl9Y3YXQ3_uTwTWGHQFnnzQ-GNU7_3j09quRdbm-ev9Yq-GvDuW7WnWTdPlG1bwBJkWbmiF-yWo2Pngwi-3_F29KLuUWDbbAbiRiYOm-Z_s_r6DEtExaQEsPsdwJ4r67nUs3bZjolWc6iLcdPUEBLRSR_S4BMaIlPuq91WjW5rHoDR3UPex1TVAHfCGuaw2J0MDQyUExLQHsOBXK6orDKDaMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911d977485.mp4?token=L3hMmOyUsecjsl8iFO4nCPJgbnTrJ6kTJxA5zkRT-hFQIJlAOkPtfR4UMVJ6Vyc2Ow8xStwYJoFkL9WbfEDT0aPjWB9MQckcsHrCV_9SMDPUxhIZOJdCzUt-Gv5cFhl9Y3YXQ3_uTwTWGHQFnnzQ-GNU7_3j09quRdbm-ev9Yq-GvDuW7WnWTdPlG1bwBJkWbmiF-yWo2Pngwi-3_F29KLuUWDbbAbiRiYOm-Z_s_r6DEtExaQEsPsdwJ4r67nUs3bZjolWc6iLcdPUEBLRSR_S4BMaIlPuq91WjW5rHoDR3UPex1TVAHfCGuaw2J0MDQyUExLQHsOBXK6orDKDaMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل برای بار Nام تفاهم نامه اسلام آباد رو نقض و به لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/141970" target="_blank">📅 01:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494000c553.mp4?token=vYUWWiOMy2BOvQuGDvS622oEqT8TL6wS5_c4jSAWcjUGkN7me2anFZ-XcyP3PsWvmwQoI6cFsLxrE3C8_OLN3yzeVrJv1ENW91wm1wmayjW_VUYOoNOGMxVugX8xbaIzTOuK9ZnTnoc5sdoXloUhi9c7YAJb9vkdJCCP2DkzG3AZOjhEgvBsQyokdZz2lBd9apMFZ-A8y2mmZgIxrAzRfjtqRbQswil_9HumXPpgLVjf0OCxvLURs4U6dwr_A_oOCL5mwBYaZb3OfY6WPSqd9Ry6H6E70NW7JMHFMOuefV4AMXB87iM8wKkgUxF9zCOLzWG5utV2b2XNmlTnZ_6V7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494000c553.mp4?token=vYUWWiOMy2BOvQuGDvS622oEqT8TL6wS5_c4jSAWcjUGkN7me2anFZ-XcyP3PsWvmwQoI6cFsLxrE3C8_OLN3yzeVrJv1ENW91wm1wmayjW_VUYOoNOGMxVugX8xbaIzTOuK9ZnTnoc5sdoXloUhi9c7YAJb9vkdJCCP2DkzG3AZOjhEgvBsQyokdZz2lBd9apMFZ-A8y2mmZgIxrAzRfjtqRbQswil_9HumXPpgLVjf0OCxvLURs4U6dwr_A_oOCL5mwBYaZb3OfY6WPSqd9Ry6H6E70NW7JMHFMOuefV4AMXB87iM8wKkgUxF9zCOLzWG5utV2b2XNmlTnZ_6V7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: تا الان مردم فقط ۸۱میلیون تومن کمک کردن تا ترامپ رو بکشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/141969" target="_blank">📅 01:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141968">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
هم اکنون حملات به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/141968" target="_blank">📅 01:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
چند فروند موشک از سوی اسرائیل به منطقه "علی الطاهر" در جنوب لبنان شلیک شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/141967" target="_blank">📅 01:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKc5pH5i6hCRSKJtGv7_4XdtDv_w8A7SUeQukn010A6A2oB2p936RiaymWViFyYWaHUjOXfk-HUnstOYt0jZ9MFDpGVuz9wk6dC_MUgKj8zIIfNWeNxdMJmVO3W4lDZ_b5K-IDSDLmsAnN4Q2Ik6u4RAKgtqfw0hH9Ip4CTMkrCt19aWSx0xRP2n_PIdS3RZrHWU9tJT2F36iatc52_HqW5-6Mq3sPf6B2e4ydkSFbugti2GQSBKAVA_ySKALhROfQe836Qe4QuHGJoROMT6JVUx8nVQycYnObCexdOOhu9AOVQ9qCTMvO2Y8mK4iFhHohemNDRS9QhqB8uGv4UtVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساشا سبحانی، پسر سفیر سابق تو ونزوئلا: حالا که انقدر بهم هِیت میدید اصلا خوب کاری کردم پول مردم رو خوردم و نوش جونم همینه که هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/141966" target="_blank">📅 01:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
اردوغان:
ترامپ به من قول داد که جنگنده‌های اف-35 را به ترکیه بفروشد. ما منتظر هستیم تا او به قول خود عمل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/141965" target="_blank">📅 01:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141964">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIh8D5cEzt9Dvy5V_kefWO-VapMQ1xafRh20mcZctxQehwg7i-OO1PNFYzfHFrW63xJyZj_oYy7XrI_zJFStHLTH2QOWffuwFn-OGegwRb_cPQJKVVNVv9SWDO3_VKmkZJR3cZhJr0zdCNWx-d1j6I9eI1RW0iagrDmvyHTlYFHvucj4VWyInpB2iVtPXgC8h30-COfNrwR8VjBw7F2A2z5Tp4hYU-1ptEOXhaaTOPwMDtckuOjBzuTvbLmw64e_lLf5858jDwIvk3a9kyB94fMiiigJHrPztpSSymE3LsECbt5J30XlwSzn9AHClfbmkL_WjR0MNxOalLIpSiV5hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
دغدغه من از سال 64، لبنان هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/141964" target="_blank">📅 00:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141957">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNb_e7DSN1KzeX9WJMmU-cG9DvUSl2sPtMN65RYkNME9-3f07g1Hrp0YG1Rwu6BjnAmHjtCFHECsSE1pq40S2M0xRjHkL4Zp9i5aff9QsVyClpSMsyBQJoa8ZbCF-EuDQeWg8E3EtLdxaUrX-l22_CsPDY1gQdWp5btb1CgnBgkvtDO1xjrNrqUYIYkmEoX3mLtF5Uoubvw12iCbdDIBNMHuWs-oAJSI_Hso70gwz8JLQrXuex0IPQPNDwxiIqyCh9LMRH9gYH0Z0THPOYTkBdkJd7mf3PmUoIhC0VICvz2IhKdGbyAa28IgK34lmi3tgFRT8w-Sw9ne9jNHFx1-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oy5qD9bF184SBl9nLFZY6cnCJGyPcz9JHGqeHrKCT5dx7u2ZkhnK3Umhtm8azVy2Hy_uKUHtyGEBId-ZRDAn_9thG5gek6aalK2dL5J3E150BS9HW44vOxENQFZxOM-_g4yTjgVH4N3W8WABaJtbsiPqddmDmq_23Ju-bgCA50zybWCNTwS7VOmD0kcXARdQs4McPzg84II1g1CuuvnmPuwxgpPsNRQju5coulJZBQdUJJHpWCbll8BbEuomrYK77oFgiMwibx6J4X8Ojq9mCTWmEmpKrWYO5MagxvFlxQBj0l6SmOnDnZFv3D9-ksVcdclab6GYAQi3yMlfnBVieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKnkHmQ3yrtXVuvB2WDx2aCsSPqvWWGuJnaCGrMPtlOAsM2ROPs7aFppXmgDZ2kd-gmFyquhwBWaWytzkeJrcqA8MuA4Ru1uo6Sn7zQ1MrjLPsmNOzkiVwm0tvmvCm5JMmxY2ENNJS2kf7GPud0s-ORDoOVACgKdSoTLsoLDe46tjBKfGOPUdicF3jo6OapUTHpsx8JhaICSdEummfd9oJvKAy5_H9pzaAereM68TQ8dOjwvTvAXcehSEtgNcxzB5Bx7gcm3-rIQ0yyLboDZQEwyWgNZYqLJO7GuWrq_VU0re8NxXy9AR0NBD9YvU0AHFRz53kwUyalKxpjO03RYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbtP0GRekwEbOA37XFnUAM9saLu9tpRQxEQm7LeTwKHUwSuqjYZ1yD_nkD4J1RSkrNVFnJNIlUblJseH0-IZvyV3FUa93LGoAD3632E6Frkw38HEFHu6yvrgLZ4tU_r8J2LO3wWW7jkAAYHzSGjD3tkY8TEX0nKBS9_Da274uTPRxtKHe3aRP1Xvk3eJibU1UZ4i57WchIeuGANZdopkCPjfKvXVBHeQI_--BMpzl-7Nxeq3ztsZntQqsxGbKlw-wapSbnBujbD7dHm5sNglTXuVcIOr9TiCTQf0FEGzu0o5RVmtKtmyvv8_10qUxQ6FjxyQDr_Iis0HhJEqoQXBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lF1BsgK3XSczC6D9hX4idiOEhXeluakOdB1JEtvma2ReAOke2bOM3oHw6dCuQkhviuoOR3TEt3apRjH0cmVpskCYRGXnMWsabFzpK41aW6OQK_pkXYLX22Rxp-ydJ6LPLrye5JrKVt2Fj-f2z2di6xkYbkeCpT-6lfc3ATW7GXROrvqeXHl6QF9asIYMdupa-JBlC4vJorbpqwenxluOrTT0uCb6PwtxNNQHWp_rNhNwkyqNlgAwtTCujcbH0INT4Co90SjBv465viIBcNIGGVEYbnvSJhPsklfxB5aEY9F6sKtL4At9AkbicyWgIdKmnAL9orbDRUffee83SmV2rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112eded0c.mp4?token=tK7dtQ_vREnGpha30DCnHwAkFVLIbHBuqCofcSp4PsnLk52TxHYyf_4KbgPlyCmfpFMS8LkgHX-pmhZtdNhJStP7wgnRIrK215Cxw2aA1og8uliQnyvE4tzXKBgJOGnP19Fvnvm0SnZMN56LvndyW_qfnQi0EQNj0h5PLBlxlOE4VmjWvTDFAstnKo4FFU4-rbR_LxEFz7K6ZRc1HGDY3CX6tBRnBCy2Z6Ecyyhl6jAJur8VsCEXWh7EKJkyTjpEz1BOblhL1tY2n9RHIrKm6hlkLyCkKqbUxHA0QTksLUCUOJlcTreHOiAEA8jPbke4wX9AZbiqiRNIynpQBRfkRYVwZrZ0cuZq9xrMxzmUU5ZbVDd1PDVSDFiof4YrUADGqDOTVrMVAQ07lRZDkWRroZ79Drk8MiP2y1qszMamCUqRoIOzji84bAMZj3Tl7exCwU0sEDRPa5Z5RDdyK4LQODkwBoFczqxamw1gNJLWDDIdmjU8-AsvY6hokQmB2saMWy2hLnggBcQQRQv750pqKHhNeMD8b2QHHk9D5O3T_7LwCDBFqpC_YVQt70LgpR-Ed0024YsdV8ol4o2JoqhcOKC9uBLiuYE1G3ZVzdjtL97EqDHYlHlfFROsPwocB04E8TrXI7STZdprjtuct5wsrN3T4heU2xIAh3lM64WWMvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112eded0c.mp4?token=tK7dtQ_vREnGpha30DCnHwAkFVLIbHBuqCofcSp4PsnLk52TxHYyf_4KbgPlyCmfpFMS8LkgHX-pmhZtdNhJStP7wgnRIrK215Cxw2aA1og8uliQnyvE4tzXKBgJOGnP19Fvnvm0SnZMN56LvndyW_qfnQi0EQNj0h5PLBlxlOE4VmjWvTDFAstnKo4FFU4-rbR_LxEFz7K6ZRc1HGDY3CX6tBRnBCy2Z6Ecyyhl6jAJur8VsCEXWh7EKJkyTjpEz1BOblhL1tY2n9RHIrKm6hlkLyCkKqbUxHA0QTksLUCUOJlcTreHOiAEA8jPbke4wX9AZbiqiRNIynpQBRfkRYVwZrZ0cuZq9xrMxzmUU5ZbVDd1PDVSDFiof4YrUADGqDOTVrMVAQ07lRZDkWRroZ79Drk8MiP2y1qszMamCUqRoIOzji84bAMZj3Tl7exCwU0sEDRPa5Z5RDdyK4LQODkwBoFczqxamw1gNJLWDDIdmjU8-AsvY6hokQmB2saMWy2hLnggBcQQRQv750pqKHhNeMD8b2QHHk9D5O3T_7LwCDBFqpC_YVQt70LgpR-Ed0024YsdV8ol4o2JoqhcOKC9uBLiuYE1G3ZVzdjtL97EqDHYlHlfFROsPwocB04E8TrXI7STZdprjtuct5wsrN3T4heU2xIAh3lM64WWMvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض خانواده‌ها و بیماران مبتلا به سیستیک فیبروزیس(بیماری ژنتیکی
⬅️
Cf) در ایران به کمبود داروهای ضروری(حیاتی) مانند کرئون و پولموزایم و نبود تریکافتا در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/141957" target="_blank">📅 00:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141956">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
۲۴ساعت تا پایان آتش بس
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/141956" target="_blank">📅 00:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141955">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJzEtU7lXRGlx6rKe6meKVdlvCXjbNNIZAORPIQxuZiKdwvCYVAjtuOiY8KoEHa8LyeOwHzVu5ekdyeyy-YmwyAWJoBv0mnbnLBQotFXVLoYIncxeWBcWKg4Hggf01sxa6DzYLzK5b5x5g6iiyFTIRHa_rg-jVtiY-VxypZOcY8WfKZykCK-kSIblvwjND4H1mPW003cusoJJqgnGk0nu7auJ8UqKaVcB79weOrsR6FNjGp78kKSb_60KFRUJXOvPCfzN053vvqJBvwBSiHuI6JbLqWENxpoUdYfXZe90_z-ciEOMlgFMCENXTiTfD2Bg3Py5eDeLYNO7-j_X4H4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا سپاه امروز یه کلیپ منتشر کرده که آره ما پدافند داریم، 20 دقیقه بعد لوکیشنی که پدافند بود لو رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/141955" target="_blank">📅 00:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141954">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎙
‏روایت خداداد عزیزی از روزهای سخت زندگی‌اش  ‏ساندویچ نان و رب خالی می‌خوردم.. به‌همراه پدرم دم حرم دستفروشی و گچکاری کردم..  ‏برنج و مرغ تنها یک بار در سال و دم عید می‌خوردیم!  ‏چلوکباب نخورده بودم و نمی‌دانستم چیه  @AloSport</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/141954" target="_blank">📅 00:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOPS-MmWO38ZgdRKYwWd_tdI9IerGmhSktgAxA0PNHS-QcYS_t2BbipNQOKtXgeTW0RTp3GMM_bxKh5KKa9Sl4giPnzHoSiwQqXF-LF1jbjOx6FTtZfoh9nMkOH511I1gQ7ue7jQFaXL2jq495ZIH1RVD6DUg0-SYOxwNvul1SNY_AGN__liO7Gb9cFklW3WhAXgHlx506dhKOb4K1f1GiTYt3el3NiwQFZGnypmQjZUiJEeA9zJ_ZfX30jHB7LHI52LqRO5zLzLbaWPsdgsdbl24iBOo3caKBa6g_MRSLEWHPWK_caxfaRrDw3EmumcWip22xuDSVcPnB8DT8qiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
پست جدید ترامپ:
سوار بر اسب با جرج واشینگتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/141953" target="_blank">📅 00:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9111f575b2.mp4?token=BcPqFvVw6kAULOhfCuue-DAY4y9gjhij3GLupySDedqUQLcg4hEXtwnDfxY8xZnwsn03awnktaZic0EFs6y_QJ50JPhRpq3Zjt1aHgAZt3chz_wasJuNRJxhnPGfmcN0_dWiDsLSt6LzmIeT3tU7nMxbinrdvDvrxyRQKOWH78UQZkUW8axZJKbmMmRWaYJZ9jU_OZI5SkRaBdYRG8I4XOKGsA5JBpwV4khCLeTHb4GO_a1U13fAFZQa3xBRIQK2rRo-pbulV8MVxII8d9Tk4aqSJt6FqhpsLw7Kik8pw5aa0Rr6VsT9pnM8G5aDXSXqnGGqYmm7xRfMOkLLfOAPVH0eBGFIywIryoR6fRkxVdMlhSTv5RfXOk9nylDIAKiJVhydeb3W7X8HsvHfcXNth2Os0UPTGVsgJtF4Q7X2T0vCr79ZOBbpSk84VHRF7UNrRVs9m5K5-EdO-F9PunizRsimu5xSYKSChsxVGggO08fYAzwXiUbLoMnYan2WnVlPIQJSb_0mw1QrIhSVs7S0icTs0P4Mh_SSYUO-SClpvBctNdggoocG3W2Qx8Qth3TrR15r2kF3e6H15kNC8MZXskr5jHDOHdwX0SWnKXVCplUyzcFXsFPBx2cmm8LGgCF84BRTGVKyRGFah24Z04WWl-Bv1jNldvuSvh3hslXo3sM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9111f575b2.mp4?token=BcPqFvVw6kAULOhfCuue-DAY4y9gjhij3GLupySDedqUQLcg4hEXtwnDfxY8xZnwsn03awnktaZic0EFs6y_QJ50JPhRpq3Zjt1aHgAZt3chz_wasJuNRJxhnPGfmcN0_dWiDsLSt6LzmIeT3tU7nMxbinrdvDvrxyRQKOWH78UQZkUW8axZJKbmMmRWaYJZ9jU_OZI5SkRaBdYRG8I4XOKGsA5JBpwV4khCLeTHb4GO_a1U13fAFZQa3xBRIQK2rRo-pbulV8MVxII8d9Tk4aqSJt6FqhpsLw7Kik8pw5aa0Rr6VsT9pnM8G5aDXSXqnGGqYmm7xRfMOkLLfOAPVH0eBGFIywIryoR6fRkxVdMlhSTv5RfXOk9nylDIAKiJVhydeb3W7X8HsvHfcXNth2Os0UPTGVsgJtF4Q7X2T0vCr79ZOBbpSk84VHRF7UNrRVs9m5K5-EdO-F9PunizRsimu5xSYKSChsxVGggO08fYAzwXiUbLoMnYan2WnVlPIQJSb_0mw1QrIhSVs7S0icTs0P4Mh_SSYUO-SClpvBctNdggoocG3W2Qx8Qth3TrR15r2kF3e6H15kNC8MZXskr5jHDOHdwX0SWnKXVCplUyzcFXsFPBx2cmm8LGgCF84BRTGVKyRGFah24Z04WWl-Bv1jNldvuSvh3hslXo3sM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‏
روایت خداداد عزیزی از روزهای سخت زندگی‌اش
‏ساندویچ نان و رب خالی می‌خوردم.. به‌همراه پدرم دم حرم دستفروشی و گچکاری کردم..
‏برنج و مرغ تنها یک بار در سال و دم عید می‌خوردیم!
‏چلوکباب نخورده بودم و نمی‌دانستم چیه
@AloSport</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/141952" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141951">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/refjf16OHST8l77FfbdiS_7erI-JBX6IzF9Pr5-hRbhobV-v4rDOfuR1-lKgBSgns7IQRb592foSFnAMxIUUaojNiIyXbia0lwQSdeUYaJ8bvycR-LCG3_w5DopR36ZwuMREIAti92_l4dBo-qo42lyYwBfpQ6JKgFGm5A9trcHiNLuhm74OEISXNLBliDvJ1griYaanjBx6ySagt2xWowRAvmakAPgJmUVpK1ycUiJpJ_kSlFgTMr5oBr0L26Ys-r4WcjOltDFJQFFmEJFiM6pRchf3TB7-ypsreNuzGyLO7EV0pXEZfUugdzYLnp67DTaZwgW1XUzO-SAAq7oqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: بعد شهادت آقا دیگه نباید برنامه شادی رو اجرا کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/141951" target="_blank">📅 00:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141950">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f3644e74c.mp4?token=Cp8aKecpCp0YxekNdwb-Mxgev4uLbLu2qH1Ucv1x1uENVUso23_xZn29xbq-LkCMxPy-HDFdMezyj9K6KO-46Ueh1guiJ6J_Kl4XjCCAdz74GsD5oZ251iR4o40oUxKohz4HFbO5h_BixhGCv6PhoK6mXjw1cselOEX5LVOv2xtpC7m6K3OFG1900XPUx0IP9AQHu0sz3zlMC5HzElSIQjFW5iAKLOMKBj4v2OqHa6qxiURzq7jnPip7NUXXDaV4XHdlLgSE3SPJUv47nPc3AJmmefDJXI73RBt7RAmtowv-YFopc2uQWNDCXIB74z4LI31x7AYkhfz3PxTQ1AvRow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f3644e74c.mp4?token=Cp8aKecpCp0YxekNdwb-Mxgev4uLbLu2qH1Ucv1x1uENVUso23_xZn29xbq-LkCMxPy-HDFdMezyj9K6KO-46Ueh1guiJ6J_Kl4XjCCAdz74GsD5oZ251iR4o40oUxKohz4HFbO5h_BixhGCv6PhoK6mXjw1cselOEX5LVOv2xtpC7m6K3OFG1900XPUx0IP9AQHu0sz3zlMC5HzElSIQjFW5iAKLOMKBj4v2OqHa6qxiURzq7jnPip7NUXXDaV4XHdlLgSE3SPJUv47nPc3AJmmefDJXI73RBt7RAmtowv-YFopc2uQWNDCXIB74z4LI31x7AYkhfz3PxTQ1AvRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی اعتراضات به شرایط اعزام ناوهای هواپیمابر آمریکا شبکه CBS با جفرسون کلی که پسرش جکسون ۲۰ساله برای اولین مأموریت دریایی‌اش به ناو آبراهام لینکلن رفته است، مصاحبه‌ای داشته است. او در این مصاحبه اظهار داشته که «آن‌ها نباید این‌قدر طولانی در مأموریت باشند.»
🔴
او حتی نامه‌ای به سناتور برنی مورنو سناتور ایالتش نوشته و پیشنهاد داده که خودش به جای پسرش برود تا جکسون به خانه برگردد.  او تأکید کرده که این درخواست کاملاً از طرف خودش است و پسرش چیزی از او نخواسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/141950" target="_blank">📅 00:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
تو بی صاحاب ترین کشور دنیا زندگی میکنیم.
🔴
مملکتی که سرتاپاش رو فساد گرفته و فاسدترین افراد کسایی هستن که خودشون رو مذهبی تر نشون میدن.
🤔
روزی که در به در دنبال ریش تراش بگردین تو بازار سیاه خیلی نزدیکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/141949" target="_blank">📅 00:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy4eTpYYeFVahilK2JNljss5kGmsSF8660ZbrFRBMset13q6JKKU3oFeVvsDVRuTSPtzGUCnkf10-xDMLZnrMwG2YgWyMZV9y6KWH41k455B1J0CnutGb3yE-p2vAaBbmUrl8KIrZMAeRFLYceOHiedrwEGV3kfJlkSOgDrRujjf3hefipQ2tXfBbiCqt5Bouw8zastscIQM4So9CEdLR7zWzpfTiB20Bml7P9w_QiFSrQjM5DehtoNAdY0yJfPZD-xaKG-P54Am56RKW3MMGRNN92cCrBPJuCNBNJysQ-YL7v0SL7CtmsJP5Z03vWHulCkXJjAYXFTE5kyaOtNUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275828a58a.mp4?token=oXERktFq9R-mlAYvdVPH6clGR3azVcXp2RfZIW-aR_qHze2aDgzaJH2BVBcL8iya3416Z9WKBBBLLlvbJvcrQK2DS3Alvu-cK4CzTyOfsdTJersfKlgDzKsciyOyx5WNR14RWcYYAEAa7bkFNi4zbR1kC6n2cW3ukgiGcMa0WrqGvUzZI2YLBobrmq7Ueyr5jO8zMLeTWC5f3cfB8U_dRjIzoHcMLmZNSJW4nfqJDkTIZK2F39Fu8YTy0DDf8ruNDdI6BNFgxdcEbR33GmEKI21c2K6ADlKN-vjCY7uNzIoSz93a2FWWWk09Y2fyX8lvAC8SXKXloUY7urWwLqWMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275828a58a.mp4?token=oXERktFq9R-mlAYvdVPH6clGR3azVcXp2RfZIW-aR_qHze2aDgzaJH2BVBcL8iya3416Z9WKBBBLLlvbJvcrQK2DS3Alvu-cK4CzTyOfsdTJersfKlgDzKsciyOyx5WNR14RWcYYAEAa7bkFNi4zbR1kC6n2cW3ukgiGcMa0WrqGvUzZI2YLBobrmq7Ueyr5jO8zMLeTWC5f3cfB8U_dRjIzoHcMLmZNSJW4nfqJDkTIZK2F39Fu8YTy0DDf8ruNDdI6BNFgxdcEbR33GmEKI21c2K6ADlKN-vjCY7uNzIoSz93a2FWWWk09Y2fyX8lvAC8SXKXloUY7urWwLqWMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیر علی‌اکبری، فایتر سنگین‌وزن ایران، امشب تو مسابقات ACA 206 واسه کسب کمربند قهرمانی سنگین‌وزن این سازمان، به مصاف علیخان واخائفِ روس، قهرمان فعلی این وزن، رفت؛
علی‌اکبری که تو چند روز اخیر حسابی واسه حریف کُری خونده بود، تو همون راند اول ناک اوت شد!
در ادامه گفت :
بعضی وقت‌ها میگن روز، روز تو نیست؛ شب، شب تو نیست، من خیلی واسه این فایت آماده بودم اما نشد، شرمنده مردم شدم
@AloSport</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/141946" target="_blank">📅 00:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMsroLVfJzugVCCT_Qsj8Qc_iL94Cg8Jw3dNGj5piFwSdh03gUjkX4V2KkPosoECjcENSKt3GeFKdxl5BvKh0RJkg1ftXQVu58lMnEUgMnRVVm1k4C4Q50AGi-38FJ0tr_KXSGQE39vshbI7fmc9EdsHrXEATwpThAS0z8VPQpBID4YGLRxZ3KWQCA_L8XgObex-jv3_hMok6fZ1vsFI0SPMnumDSdqQQ8UtmG0WOrQbrFf1U5_K95IPv_8YO98SSxUrAvR37MnX0B62qs2l4AhRm6_vpnq5R0tDVHpjLSgEbn2qt-rGd111xqr6QRiDL0q4JJorPHfaX3hWduqYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: پیروز خواهیم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/141945" target="_blank">📅 00:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
حالا عکسایی که این خانم به رامین فرستاده هم منتشر شده که منشوریه و گذاشتیم تو بات تا ببینید
😐
👇
⚠️
مشاهده عکس‌ها
⚠️</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/141944" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141941">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UfU2tOYEggB2ZBucehMBloE0MBnOqNgajYYyC8qze-nzSlIbTwij4cvqsZcjMpcQCPTlhXWkeDxHFwd36GwgWE9Yx8IiJIVcmdNdXij78nQtDZKhckx3zIO4mMnXtwvm7FtfKuU9ecVJ6seKybXgjxMgyvD1u12lbqlNydZEHWTDPaM97N4VeZls2ck3fXE3uEYRead8IW2LP6c_57uG4ra7xcJQcwtjLiCMKzrPsWtG7R32btckvd1klUogQopYHGWWFWih_udLhN7Km52YC99z2r1RltXVsFV-V7W6OHls3iDc-hij7FZFnoB3Xxj_Di0k5CkykKb0X2xTfyD0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e0mrNBBTHUUCDkVbV5uY37sfc6C7xcT-5n6BkIcxkWlY98t9CyVVbFtrXLSLJnLxRboXz8mfzt3X6vN_C5aKdRTePwwfyoEoXbKhediN6WU5sEbxTLPXLheAoxo7JvJGi7H6FzQw2XC8PWLEg9UYMMZI4_FDioLSKP8r9atKqBsTUqo3YYZrdllSEWcK0EPSLrdL9KP4ELXV0qxUM9lUY2myVoM_KNvJtojzCrwDenTBTSETF0GAJ-zl7ZCxCZ6I5VF4FJr8qt01QuuMVbtXJz6pD9XciS3zTicbDgO1NDxxDkEr5-TwYUUUQpFBwh5hO2VovFCgnbgTWV6NujANJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رامین رضاییان رفته دایرکت یه خانم دو رگه ایرانی-امریکایی که به اسم «جول فرشاد» که بازیگر سریال ایفوریا هم هست و ازش درخواست نود و عکسای سکسی کرده!
خوده جول این موضوع رو تایید کرده و گفته همزمان با اینکه تو جام جهانی بخاطر حذف شدن اشک میریخت، از من نود میخواست و این خانمم فرستاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/141941" target="_blank">📅 23:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141940">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
استانداری خوزستان: درپی افزایش دما و ضرورت مدیریت و پایداری شبکه برق، فعالیت ادارات استان روز دوشنبه ۲۶ مرداد ۱۴۰۵ به‌صورت دورکاری خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/141940" target="_blank">📅 23:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141939">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/8921c86a41.mp4?token=TN76rwZN98ukOjJO2C33IYQxV4njgffetcDrke4hQHPpkVblRSbHgwhVHWIZPNCihdV-aj3GiIp_22Sk2-NsBaaEoJOSnH1YToMRIBtyho4xdUCFFLaUFKzcCI2z0dTC_fg0_Uc-BWuN6yprPUeiCJ3k7bpveIdEJg0BcVOtADRh5ohBOhjmMyZflHrmmnk4XjhA5-ZMapu7xHdR0RTh-S49z0SdxLyW-ANk_bqSnM5Gw1sfl3uGLsLc_Ejs-33x2DnTPs1PfBRQxLnJ3OF4r8yDkBf15r59yi_V_pR97zP5dfxXitJNmjvK1miP_r6-nLZxwA7ABxQkfVlLzBsX82SCPIO4MveZF8iTDiw7wD81XiwzlrKL7CBH3Q2iRoABXmNYDrYe8a81opwhpSXsTzKHAlPp8Tn7hK5Jd5WCRQiJbCGG_eZRX2cdA0etLK7EgNKzHJUsKNOOwLygDB5dS8ELrxLFj3VFYj0sRT_1m9m2A42DtbFapiPW8yF49TN2xjX3EVdA8efaqrKRsViWMDdmVd1yF_mr8zOrJgiDgtHjq8it69YDg8OIi8MJcqu07LFR8JNiT6eFTdcG1P1jezP1tVHIZvztOj6aU4Xfkr9DF_L0bNxid7kLqTFp_USvx0ic7Or16ih9yJkuTQzAXlTvvxuzKMxbcHqdhURhXcs" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/8921c86a41.mp4?token=TN76rwZN98ukOjJO2C33IYQxV4njgffetcDrke4hQHPpkVblRSbHgwhVHWIZPNCihdV-aj3GiIp_22Sk2-NsBaaEoJOSnH1YToMRIBtyho4xdUCFFLaUFKzcCI2z0dTC_fg0_Uc-BWuN6yprPUeiCJ3k7bpveIdEJg0BcVOtADRh5ohBOhjmMyZflHrmmnk4XjhA5-ZMapu7xHdR0RTh-S49z0SdxLyW-ANk_bqSnM5Gw1sfl3uGLsLc_Ejs-33x2DnTPs1PfBRQxLnJ3OF4r8yDkBf15r59yi_V_pR97zP5dfxXitJNmjvK1miP_r6-nLZxwA7ABxQkfVlLzBsX82SCPIO4MveZF8iTDiw7wD81XiwzlrKL7CBH3Q2iRoABXmNYDrYe8a81opwhpSXsTzKHAlPp8Tn7hK5Jd5WCRQiJbCGG_eZRX2cdA0etLK7EgNKzHJUsKNOOwLygDB5dS8ELrxLFj3VFYj0sRT_1m9m2A42DtbFapiPW8yF49TN2xjX3EVdA8efaqrKRsViWMDdmVd1yF_mr8zOrJgiDgtHjq8it69YDg8OIi8MJcqu07LFR8JNiT6eFTdcG1P1jezP1tVHIZvztOj6aU4Xfkr9DF_L0bNxid7kLqTFp_USvx0ic7Or16ih9yJkuTQzAXlTvvxuzKMxbcHqdhURhXcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رژه نیروهای طالبان با تجهیزات و خودروهای نظامی آمریکایی در خیابان های کابل، در سالروز خروج آمریکا از افغانستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/141939" target="_blank">📅 23:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141938">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pgIIRpRTQ7_rJbA3Nbr75xuvtUfS9AY9bhQUOWOLHrvzgIKqlG5BJPjMUfY1yk6HP_KN8v1zXmvoy7Ue6vJoOkypTonZMe29pvy2pb1B04Iy1pU7hn33dlgYm_QlieKAgU0Y3saZF1sH_W97q-5mLgjrRwL7bpBE76JI-67BINrHee1NIQmheJq8tkVfmxatxcGaaWjqkc1rb-VAU0dX-zj1AQEIyTVIXgPXtR9nRPsdoMYtFGmygmvtT-MsrP836wA3ZcrnXbksAsMQfzFtptJne_uJazVA7dnx0W3jZ4TvS03Pz_WBL_D8Lp189bcEHL5PglW7AWH1aKjRRdbAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده ستاد ارتش اسرائیل: آماده بازگشت فوری به جنگ تمام‌ عیار هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/141938" target="_blank">📅 23:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141937">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4yAXefOdcT6W10NbCEFirL1c7s2ExXfwme3ASeFDXdq3Kmzc-xFLLXo7ZmW8ETp0whAkkpzoec7IhGqS4zmT22wsgKvKz2lyibVcXbfkYonBo9EoJc4bf1hpmHw0W95CQDTHurYKvp82RmhmAQaQxzxRnHdkLogHMj7aRKNqxUqNwo-wCsRmoWfGFT3H0Q_xlCN_rLjcTGcjMZU5VMlJnnLr8KTGqhwbLKoXEGPFiPgii5ixY7cJVMiKLhzsJ1-Qk4B-DNB4ZenpElBKd2-aoFEp3A__8bOxTEgX0dEl6yyHwAza7d67Ct3b5Tf3JKENIuPg_PaURKSZ4me_UQjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همچنان جی دی ونس شانس اول برنده شدن در انتخابات ریاست جمهوری آمریکا در سال ۲۰۲۸ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/141937" target="_blank">📅 23:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1aa363cc6.mp4?token=sBGuQkjbB_JE9IPIOwIOFnjrCR9XfN7Jyh8nUKNdcpVbC34EXNpuqkLeOFLJBjprJYWY1CQCuv8O0k-V_LqiA95DLJo9U5YeVwrvPZDTKQjoUifzjfn2hqFLjoTtx3NoXtO694psfE4LR_b6D5SCf-7850zK_7K0Rzhw5ZwDG0EqYcMf6xCKzN8Y_68fZry5DzbQG2hT5bi1THHP-qJaedn4vqcPIy0c9Mpnojnf6lm5BlEz8r71iG1RW-JD1f4ZudffNVuTtjDX-WJlGZe3ZwpReau04LcAO3zwtVHgfgh8umOwpEyZlX_S2u82DoG5IIJXXCt6_GsufnQtCg5pWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1aa363cc6.mp4?token=sBGuQkjbB_JE9IPIOwIOFnjrCR9XfN7Jyh8nUKNdcpVbC34EXNpuqkLeOFLJBjprJYWY1CQCuv8O0k-V_LqiA95DLJo9U5YeVwrvPZDTKQjoUifzjfn2hqFLjoTtx3NoXtO694psfE4LR_b6D5SCf-7850zK_7K0Rzhw5ZwDG0EqYcMf6xCKzN8Y_68fZry5DzbQG2hT5bi1THHP-qJaedn4vqcPIy0c9Mpnojnf6lm5BlEz8r71iG1RW-JD1f4ZudffNVuTtjDX-WJlGZe3ZwpReau04LcAO3zwtVHgfgh8umOwpEyZlX_S2u82DoG5IIJXXCt6_GsufnQtCg5pWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی
:
پولی که برای خرید اتوبوس داشتیم را در جیب قاچاقچیان سوخت ریختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/141936" target="_blank">📅 23:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141935">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580f35cabe.mp4?token=e5raVNd3gnMLClbXkpDeU0O6drhEWwNInCITtrH3cuty4n0ZKeJ8oS4QWgfXpTlVzOb_WzD-JTPvSGkLTgGYxOt79jl04A_uirZQOg7j98bvZ9gsjvgNyulF_QogZIxpyoEEvb1JoCYqjO_osjV7ZbLa-vDe6GIEvDKvCkTL0-WKhCAjofI6jhSCaY0KfZ6LN7J7Bv9C1xTfT9X4p01qw9Xi8Za7Tkd5GR4rg4VvLGqbMpPTJ8KMuNgwqunM1FVEF013bzHVUtGTG4-74DO5gguDJy2C8hzxRIt7FY4I75tS6sjs9YDYk07Nsy0ncF2ZyT7nrCR6V_lWRHW3c5KrxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580f35cabe.mp4?token=e5raVNd3gnMLClbXkpDeU0O6drhEWwNInCITtrH3cuty4n0ZKeJ8oS4QWgfXpTlVzOb_WzD-JTPvSGkLTgGYxOt79jl04A_uirZQOg7j98bvZ9gsjvgNyulF_QogZIxpyoEEvb1JoCYqjO_osjV7ZbLa-vDe6GIEvDKvCkTL0-WKhCAjofI6jhSCaY0KfZ6LN7J7Bv9C1xTfT9X4p01qw9Xi8Za7Tkd5GR4rg4VvLGqbMpPTJ8KMuNgwqunM1FVEF013bzHVUtGTG4-74DO5gguDJy2C8hzxRIt7FY4I75tS6sjs9YDYk07Nsy0ncF2ZyT7nrCR6V_lWRHW3c5KrxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی:
هیچ شگفتانه ای برای مردم در بنزین ایجاد نخواهیم کرد
🔴
در صورت انتخاب سناریو، چند هفته با مردم مشورت می کنیم و اصلاحاتی در صورت لزوم انجام خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/141935" target="_blank">📅 23:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141934">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
در پی حمله‌ای موشکی از سوی حوثی‌ها به نیروهای مورد حمایت عربستان سعودی در شهر مأرب، یمن، طی کمتر از یک ساعت، ۵ انفجار رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/141934" target="_blank">📅 23:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141933">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سقاب اصفهانی: امکان ایجاد بازار صحیح برای فروش سهمیه افراد نیز می توان اجرا کرد/قیمت این بازار ها نباید توسط دولت یا رانت کنترل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141933" target="_blank">📅 23:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141932">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da4e44162a.mp4?token=lSOWqaqaryxzhZ34KwXP-pdAItrN7QMKnQvQqYpqoUBf0ZyDKqb-bGmXfngNXRJCUNDLE9dK_KveIYRor4HslzMeSn7997WgU6GlPrjGJ9lnngozSqQkhVzEN731Ou-JSkPcocDdlzvPK1n5FrhDGjoFYt17Ci_8l-y9t4azQ44WS297y0_7LRgZCcoxjKF6SVfeSM2LAFa8SgTzp4AV2PvY0tzY3a3D1zeYxIoILn7kBY3hoKy6082aRAuSky3NxrsaHRRwc-UNJL2_VQxn8WG8WEkZvzoHrey52WhQwob7E0K3lbIrqW5p1yZdxsO2JxF3niiRZOubSzpEPBU-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da4e44162a.mp4?token=lSOWqaqaryxzhZ34KwXP-pdAItrN7QMKnQvQqYpqoUBf0ZyDKqb-bGmXfngNXRJCUNDLE9dK_KveIYRor4HslzMeSn7997WgU6GlPrjGJ9lnngozSqQkhVzEN731Ou-JSkPcocDdlzvPK1n5FrhDGjoFYt17Ci_8l-y9t4azQ44WS297y0_7LRgZCcoxjKF6SVfeSM2LAFa8SgTzp4AV2PvY0tzY3a3D1zeYxIoILn7kBY3hoKy6082aRAuSky3NxrsaHRRwc-UNJL2_VQxn8WG8WEkZvzoHrey52WhQwob7E0K3lbIrqW5p1yZdxsO2JxF3niiRZOubSzpEPBU-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هدف قرار گرفتن نیروگاه برق الزاویه در لیبی با یک پهپاد و قطع برق
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/141932" target="_blank">📅 23:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141931">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f7915012.mp4?token=jR34psS6IZ0rjEXnu9YpL4chKZq92cj7Th0ow6OMJs5uIxhrfyike2mnTFuN2ba1bLIpnE3AHhd5auE829ma7iFom58ICE-2PeMZWDwBJJqKsdyee3BZEoLQOH6tZKxAusXVZxFSy_LwBWCksrOUDsb0AAGdNwYoq1n9aGyVGXmPrfcgxfKxx8Px7-i08fygRyYROMDldl_GWQC0Hay87vXp9KR94LIfmQXVzvZXn2FDh8daClAtTOJ4dJ-Mv4nBpeCaO859Lxl6UU6mh1XtBiLskZaVwxTMbTp_odRJCa_zowlm6IdM7fj_Ah6NKRKirTYEu6PI0r9pPIOwi5rRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f7915012.mp4?token=jR34psS6IZ0rjEXnu9YpL4chKZq92cj7Th0ow6OMJs5uIxhrfyike2mnTFuN2ba1bLIpnE3AHhd5auE829ma7iFom58ICE-2PeMZWDwBJJqKsdyee3BZEoLQOH6tZKxAusXVZxFSy_LwBWCksrOUDsb0AAGdNwYoq1n9aGyVGXmPrfcgxfKxx8Px7-i08fygRyYROMDldl_GWQC0Hay87vXp9KR94LIfmQXVzvZXn2FDh8daClAtTOJ4dJ-Mv4nBpeCaO859Lxl6UU6mh1XtBiLskZaVwxTMbTp_odRJCa_zowlm6IdM7fj_Ah6NKRKirTYEu6PI0r9pPIOwi5rRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی: امکان ایجاد بازار صحیح برای فروش سهمیه افراد نیز می توان اجرا کرد/قیمت این بازار ها نباید توسط دولت یا رانت کنترل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/141931" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141930">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی در گفتگو ویژه خبری: حدودا به هر عضو خانوار ماهی 30 لیتر تعلق می‌گیرد حتی اگر صاحب خودرو نباشد.
🔴
قابلیت انتقال آن به هر فردی که بخواهید وجود دارد. دولت مدیریت سهمیه را به افراد می سپارد.
🔴
قیمت دوم و سوم در این…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/141930" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141929">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f05284b9d0.mp4?token=R3oYp6INMw0REIM_dFkVXiv-s4zVhiNO_iwHLuVMU5Tmk4SsTCtcMwBe643UBU2oDBUIA5TWmPrUA7ZjwKYpPSZ4-b4O4TFPvtaw9ecRDDkggGJMkq93gXo7coKPRYiWfSdvRb4ESswM5lkoq9N4_S9BKzssbbZ_3HM7pW9OMCnbAnmrUxng9fwLuD69nL0kinML_daEoc5Bs468wZzOMrydyYXIq41rSJHIUP0N9wmhZrUocnzQk_UnmwcrY9GwwmF6YooVm4gl960hcyDG0SlKc4mMdkzKKKjgx6nA-GwE6wwJY0hMgOR1tP_TFme84ZuWdnolpfz95kgEjBF8SR3aepEzFsbsy-8ncdq2tc41kane23Tsx5XYYNIC6hlDjrPg-RWIablIWZUuMVs9AVUTVSWV0POAeLQxHJYm2iek1lmLTWORfUW6sEFA6950fLhr4ZfIvhEUzMJZ0pBZ4WzdMV4yiV1lTx4SW1IlZEIhggS5yIll4HycEQ6FucygmOUAK_lutr-mtRkgfamDVd-6PZVsp2fZf76zQiT8s-Nhisr0dUiB3HzQ1sWKQ0XCVihAGBS9MVtB5HZFLJ95EQqTeIq8BI9SHzW7pObXkiRB8uMUyz9FyuKbTRxbY7qJCpPR-wkPWPGza0rDwaPkhv16t0ov-vcvpADfTKbLP-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f05284b9d0.mp4?token=R3oYp6INMw0REIM_dFkVXiv-s4zVhiNO_iwHLuVMU5Tmk4SsTCtcMwBe643UBU2oDBUIA5TWmPrUA7ZjwKYpPSZ4-b4O4TFPvtaw9ecRDDkggGJMkq93gXo7coKPRYiWfSdvRb4ESswM5lkoq9N4_S9BKzssbbZ_3HM7pW9OMCnbAnmrUxng9fwLuD69nL0kinML_daEoc5Bs468wZzOMrydyYXIq41rSJHIUP0N9wmhZrUocnzQk_UnmwcrY9GwwmF6YooVm4gl960hcyDG0SlKc4mMdkzKKKjgx6nA-GwE6wwJY0hMgOR1tP_TFme84ZuWdnolpfz95kgEjBF8SR3aepEzFsbsy-8ncdq2tc41kane23Tsx5XYYNIC6hlDjrPg-RWIablIWZUuMVs9AVUTVSWV0POAeLQxHJYm2iek1lmLTWORfUW6sEFA6950fLhr4ZfIvhEUzMJZ0pBZ4WzdMV4yiV1lTx4SW1IlZEIhggS5yIll4HycEQ6FucygmOUAK_lutr-mtRkgfamDVd-6PZVsp2fZf76zQiT8s-Nhisr0dUiB3HzQ1sWKQ0XCVihAGBS9MVtB5HZFLJ95EQqTeIq8BI9SHzW7pObXkiRB8uMUyz9FyuKbTRxbY7qJCpPR-wkPWPGza0rDwaPkhv16t0ov-vcvpADfTKbLP-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی در گفتگو ویژه خبری: حدودا به هر عضو خانوار ماهی 30 لیتر تعلق می‌گیرد حتی اگر صاحب خودرو نباشد.
🔴
قابلیت انتقال آن به هر فردی که بخواهید وجود دارد. دولت مدیریت سهمیه را به افراد می سپارد.
🔴
قیمت دوم و سوم در این طرح وجود ندارد و سهمیه در کارت بانکی افراد شارژ می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/141929" target="_blank">📅 23:09 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
