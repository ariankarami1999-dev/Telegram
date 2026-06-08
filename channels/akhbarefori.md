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
<img src="https://cdn4.telesco.pe/file/SnJb7UlggJViluTN9Vr-LAUnH7tKgyqnXSSsyEJxKlWbLfo4UvSxevUFfunxaIzm1_K2WpPqxk2BshIy8rQj4RH1PpPmuuUKLXR-jY8jvSPQ2Qhzov6ZJv48zxZDHvA8x-C2-m-Nuq5z3B84AyKtxM-1rBMyRtncM1RpQVTppH3YlQQb9rjCbHa5Pvm6CilDfqlSbU98FOE3i0ZNhUfVMzD6K7iBWOx2M-1EUjM-Le2YoW5JSqhpL5PFISh8oBUWLjHN_GHS7MDBQcdHFcELk8IzY9UpqT9PZqXu2Qt5czM5OFZkpG8Anv2MN45N2Yn-P-Syge9KnnADGeHTUBnw7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-657408">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
خبرنگار الجزیره: آمریکا از طریق میانجی منطقه‌ای برای جلوگیری از گسترش عملیات‌ها و حفظ شتاب مذاکرات، تلاش می‌کند
نورالدین الدغیر خبرنگار الجزیره در تهران:
🔹
قاعده می‌گوید مذاکره زیر آتش، راهی برای گرفتن امتیاز در سیاست است. آنچه ایران به دنبال آن است، تحمیل معادله توقف جنگ در لبنان با تمام جزئیات آن در هر توافقی با واشنگتن است.
🔹
و آنچه اکنون در حال رخ دادن است، تلاش آمریکایی از طریق میانجی منطقه‌ای برای جلوگیری از گسترش عملیات‌ها و حفظ شتاب مذاکرات است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/akhbarefori/657408" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657407">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp2fAkFb6YcrvKV3wwSAbknpdJ1oyLl6ppzg8hd8pnH5Jwx-5Pep9Pv11T7O9X2KVfZab7Uj49njxacjFNTbRuGZKRyyMyFZOKSYvkXo4pOJMrL2tISpVgKLMrWpB5kf7nfiro7GDhf7D_u71hNmixBfv582PAwDJGXWO5iH5q4sREJGtKBZYFZXXXfGjWp5hFeTxyh2h809pWAzjUw7oXkDdpL7LE-FCjAbVj5RzQLY1ttgHg29umaMQenf8QTzr-3nPtDTdIBt_RFjrfrfncbHBDNM-M9w2aloZUqNBzqgej8X0HyDJiQqGC-gXF1wu-tw_3D4hdtzJe2bEK-3tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف، رئیس مجلس:‏ معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را بر هم زدیم
🔹
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/657407" target="_blank">📅 18:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657406">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه در سواحل عمان
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از بروز یک حادثه امنیتی جدید در آب‌های نزدیک به عمان خبر داد.
🔹
این نهاد دریایی اعلام کرد حادثه‌ای در فاصله ۲۸ کیلومتری شمال‌شرقی «جزیره مصیره» در کشور عمان رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/akhbarefori/657406" target="_blank">📅 18:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تصاویری از حملات موشکی یمن به اهداف مهم در «یافا» اشغالی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/657405" target="_blank">📅 18:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657404">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hh2SRunJLjcdHP1g9Fe72glomLkqjxwDFl_KjicHuz1m3DbtMbEEWCw_nY0J3g-rMn-2MXWKaQPi80jis50W7dTjcJAWw59jCC3B3FaydUC2rcWspRHG_mTPIqUvMpIdCMTfgOBaSXIEc11I96-2MoZ9wkAQ6gAjJjeVWduS4ih54WdAy5CM_TJ13UzLIKJ-GcF-45uJdfBbm6ltQi97hTbhnfFdA4Q0Rn2p8lfHJEKpjC4rp9ZwaFV5XrWSTgqmBrhQLJr_OgBROIydqxLzeXRbVN2bjH9tsgtA_Gub6QWwcPhhu2Q-V4k1GvPRhn_0Cuagpe1JYLo11KQ2xN587Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: اگر ائتلاف شیطانی صهیونی آمریکایی دیگر بار دست از پا خطا کند، منطقه برایش جهنم خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/657404" target="_blank">📅 17:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657403">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
پردۀ شایعات ترور مقامات نظامی و سیاسی چیست؟
🔹
همزمان با آغاز حملات اسرائیل به برخی نقاط کشور، موجی از اخبار و شایعات درباره ترور، مجروح شدن یا هدف قرار گرفتن مقامات سیاسی و نظامی در فضای مجازی منتشر شد.
🔹
تجربۀ درگیری‌های اخیر نشان می‌دهد که این اخبار صرفاً با هدف ایجاد هیجان رسانه‌ای منتشر نمی‌شود و یکی از مهم‌ترین هدف آن‌ها تحریک جامعه به تولید داده‌های ارتباطی است/فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/657403" target="_blank">📅 17:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657402">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
گروسی:‌‌‌ هفته گذشته بازرسی معمول از نیروگاه بوشهر انجام شد
‌
مدیرکل آژانس در نشست شورای حکام:
🔹
در فوریه ۲۰۲۶، آژانس به دلیل درگیری نظامی، انجام تمام فعالیت‌های راستی‌آزمایی میدانی در ایران را متوقف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/657402" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
الجزیره: هم‌اکنون باز هم نقض آتش بس و حمله هوایی اسرائیل به شهر صور در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/657401" target="_blank">📅 17:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657400">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOLwGEjRqftAJm1gRmij11twsOzpZ9cgFaw6w7taGFSvB5A48zD-2UeNYGEKYDb2daxxDTTgt_HpFQohv0aWbkjoFiPDvbgq4HR7SQMnUbCQMdS44UzsmuyMXsP2_vc8oFZlR2Mg3HUVXEzM5R5sbxlPhU4sjAY_sflws1qvF1_9kwIgFvuSt4ZFYaqHYwPZ2HN8oUG-sirNuzGDFcx0xN0BREyIfaC4k_KW7_1icipClZtfANQvFZVH2kN_YguzVPRChMDnJGf8WbekIFdXsttCsDrt65b48dlstv6-3nZlgm8JLbFQIJGFL2QW9Hdis1hpSc6bK3CP7ozoFFgdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اختلاف واشنگتن و لندن بر سر سرنوشت جزایر دیاگو گارسیا
رویترز به نقل از تلگراف:
🔹
کاخ سفید در حال بررسی طرحی برای خرید جزایر چاگوس از موریس و کنترل پایگاه راهبردی «دیگو گارسیا» است.
🔹
این طرح در پی اختلاف نظر با دولت بریتانیا مطرح شده؛ زیرا واشنگتن با برنامه لندن برای واگذاری حاکمیت این مجمع‌الجزایر به موریس مخالف است و موقعیت این پایگاه را برای امنیت ملی آمریکا حیاتی می‌داند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/657400" target="_blank">📅 17:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657399">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نخست وزیر پاکستان دقایقی قبل در پیامی در شبکه اجتماعی ایکس در واکنش به تحولات جاری منطقه‌ای ناشی از نقض آشکار آتش‌بس توسط آمریکا و ادامه تجاوزگری رژیم صهیونیستی در لبنان نوشت: از همه طرف‌ها می‌خواهیم که خویشتن‌داری کنند و به صلح فرصت دهند زیرا این هدف نهایی در شرف دستیابی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/657399" target="_blank">📅 17:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657398">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایران از هفته پیش گفته بود پاسخ می‌دهد
ناصر ایمانی، کارشناس مسائل بین‌الملل در
#گفتگو
با خبرفوری:
🔹
ایران از هفته پیش اعلام کرده بود که اگر لبنان مورد حمله قرار بگیرد، پاسخ خواهد داد و این از نظر ایران نقض آتش‌بس است.
🔹
آتش‌بس که برقرار شد شامل لبنان هم می‌شد اما متاسفانه نه‌تنها صهیونیست‌ها اجرا نکردند بلکه آمدند بخش‌هایی از جنوب لبنان را اشغال و بخش‌هایی را تخریب و کشتار کردند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/657398" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657397">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
لهستان، فرودگاهش را به روی زلنسکی بست
🔹
لهستان که همواره از حامیان کی‌یف به شمار می‌رفته، در اقدامی خبرساز، استفاده زلنسکی، رئیس‌جمهور اوکراین و دیگر مقامات اوکراینی از فرودگاه خود در ژشوف را ممنوع کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/657397" target="_blank">📅 17:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657396">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCzERuyVCZNJKTRl1bh99L70TJ70g3Cio-xeJXbrvQ8adBMXv6fwFlCrYm5Lfb0zu61_AXwoLV9rwaUs1QDFoFZ0kO0C-SuR64n6gPqGXTl4NJhhpWK3BVBromr_hQl3Y8BkPRuu-7YlYtjQ2dbDQmEL-cTppwXv3eTmgaSYMl2gbAZHmjNAlE6Y8tirF5pIrrt6Kam8qb02QLZIdkuBRX_MhiBNdLn9L-wjIU2hVsprq-LzfT-qgjkPvEMXH70GwyZ44hbPXNHpruWVMI7B9b9o3ksvRpOwmf9mAcQBSTKz79xchQxuhuNBzFK4X6WNNRzsyHO5WnMLI5Ldjhr9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران معادلات منطقه را جابه‌جا کرد | حمله ایران به اسرائیل؛ آیا قواعد بازدارندگی در خاورمیانه تغییر کرد؟
🔹
درگیری دیروز و امروز میان ایران و اسرائیل می‌تواند یکی از مهم‌ترین تحولات ژئوپلیتیکی سال‌های اخیر در خاورمیانه باشد؛ تحولی که پیامدهای آن احتمالا به‌مرور زمان آشکارتر خواهد شد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3221488</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/657396" target="_blank">📅 17:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657395">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از یک مقام آمریکایی: ادعای اسرائیل مبنی بر اینکه آمریکا موشک‌های بالستیک ایرانی شلیک‌شده به سمت اسرائیل را رهگیری کرده، صحت ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/657395" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657394">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وزارت دفاع عربستان سعودی: آنچه درباره هدف قرار گرفتن پایگاه الأمير سلطان در الخرج منتشر شده است، «صحیح نیست»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/657394" target="_blank">📅 17:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657393">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AueKdaCqRGSJP34W-LavWxrqmWMTO50cgX0SVmVcjOC5Ax03sUgya6j2ebAb6NZKG-uxVlm6W0-M3WQDgISnbPlqxKfd58sTCDi6dAWj57RHl-QZgSTU6jN4CUhP-Yr9GNziqycKDNG_k3rxn02AErrdBDw3_7jBmrNlwTSLQh4fwGAuSnliJm-5RxpLFNG7zg_BT8XENgEKjFHjDt9fJi3XOfSdWcT6X8Cqm8W2dLhmXD80FjJK_ZjmoUGml2ewvWuE1kTJuRpZULVUKHaLyhSbKH29LgX2_rfPuq9DFjrQ4SH6GrPf803DLhhv2JIPQ2M_Dw3PLWkuQSfvTmEYYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/657393" target="_blank">📅 17:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657392">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
نتانیاهو جلسه امنیتی برگزار خواهد کرد
🔹
به گزارش تایمز اسرائیل، بنیامین نتانیاهو، نخست‌وزیر رژیم اسرائیل امشب ساعت ۹ به وقت محلی جلسه کابینه امنیتی را در بحبوحه درگیری با ایران و حزب‌الله برگزار می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/657392" target="_blank">📅 17:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657391">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ازسرگیری پروازها در فرودگاه بین‌المللی دمشق
سازمان هوانوردی غیرنظامی سوریه:
🔹
فعالیت‌ها و پروازها در فرودگاه بین‌المللی دمشق از سر گرفته شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657391" target="_blank">📅 16:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657390">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077152c1ab.mp4?token=DgyFP8qUTYfmfyi2kPjf60qZDGCeSuB3HBf500dHe2cZKuqdYuLBW-ReWMRdrguhTEMGhJTdsfgV9b733DTWvmWdj9JgpqWZSfz-e559WKx545uEU25ckPfETPAWjEqmiMpeUrZDwfmYZjowmpWwWS76NZS7XEvHo7ZYePBF9qma2XqGOWkS1OnN19pvKBiW6TXMhiIVnjsfcfLMCTXIZ4JAAMF-sj1XLgcEFJoSG0l9Q0EAxa86DphMhR6GDKxcqrL-ML7978JsFphGYNMe2ZqEucv7O3BtX60_gTUfPl-Ci5uOAPUXrE4PuJS_NeuLU2-KTcEXCaG0wQwkqxyAsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077152c1ab.mp4?token=DgyFP8qUTYfmfyi2kPjf60qZDGCeSuB3HBf500dHe2cZKuqdYuLBW-ReWMRdrguhTEMGhJTdsfgV9b733DTWvmWdj9JgpqWZSfz-e559WKx545uEU25ckPfETPAWjEqmiMpeUrZDwfmYZjowmpWwWS76NZS7XEvHo7ZYePBF9qma2XqGOWkS1OnN19pvKBiW6TXMhiIVnjsfcfLMCTXIZ4JAAMF-sj1XLgcEFJoSG0l9Q0EAxa86DphMhR6GDKxcqrL-ML7978JsFphGYNMe2ZqEucv7O3BtX60_gTUfPl-Ci5uOAPUXrE4PuJS_NeuLU2-KTcEXCaG0wQwkqxyAsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: تنگه هرمز مال ایران و کشور عمان هست، به هیچ قدرتی اجازه دخالت نمی‌دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/657390" target="_blank">📅 16:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657389">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: بند ارجاع ایران به شورای امنیت از قطعنامه آمریکا حذف شد
لارنس نورمن، خبرنگار وال‌استریت‌ژورنال:
🔹
پیش‌نویس قطعنامه آمریکا در نشست شورای حکام آژانس پس از اصلاح، به قطعنامه مشترک آمریکا و سه کشور اروپایی تبدیل شده است.
🔹
در قالب یک مصالحه، بند مربوط به ارجاع فوری پرونده ایران به شورای امنیت سازمان ملل از متن پیش‌نویس حذف شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/657389" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657388">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5a518dd2.mp4?token=Na46LzKAqCZ64qxrLEvQNSADrNEaLvs7y9s6YZSUHqWq90JMjrnapSAaIvgdWrZKb7Oa_cNIfgjR7mWnAc2_hoaM4kOLUfp6bIn1XoOiEbCcoM-weyVpPMmeCLrPq4Ma4y5y8l8PpOf-JGBAMTlxeAn0iwBB2ycpOdBJa6BRqpF3kPN4S5tiGd20YRAgPBfU0CzkxuIAUuwNBIbm6D7tcESnob5zXnRa6bcPWxgJ3gODXE6Kfp7OJH9t9QZMG0XZtGAYBa_RsmDtiApyptKzzzoakKYG06CHw3AHDnAEZvdxMRbmdyYLZFc2dcGsY6mBRx-tt1S016G0gSQbqmiveiIAFWwlb-lkuYgNR3j_AmJ0lh-8Izisph_gTnxlQAHQaJrmSxSyLWXgpfHqLcVTgQfto1tyAj9o3z96NedfPBvi011o-uPOYRlTetf_GcUmJVDJdRE9LgrwkBnh2xs4ST82zKYlNLMdtJJlEwhKsDSlTXqSWPchxWIj8GK-DpngQ9x5LLjkQiM6DLDNCFlNSdbBQu5-wXwWVm5xlti7SUF5cnzpPEm4B-9QwVc126eU4sYmyX5iJOuEuf115gEv-LRVGwDqDaUv83u6nY9vd7cvfDTMGAUUM05m_sP7G7kGsd5_wmElRGfRZUHKmpBB8dotlucHdHP8gohkYZxUs0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5a518dd2.mp4?token=Na46LzKAqCZ64qxrLEvQNSADrNEaLvs7y9s6YZSUHqWq90JMjrnapSAaIvgdWrZKb7Oa_cNIfgjR7mWnAc2_hoaM4kOLUfp6bIn1XoOiEbCcoM-weyVpPMmeCLrPq4Ma4y5y8l8PpOf-JGBAMTlxeAn0iwBB2ycpOdBJa6BRqpF3kPN4S5tiGd20YRAgPBfU0CzkxuIAUuwNBIbm6D7tcESnob5zXnRa6bcPWxgJ3gODXE6Kfp7OJH9t9QZMG0XZtGAYBa_RsmDtiApyptKzzzoakKYG06CHw3AHDnAEZvdxMRbmdyYLZFc2dcGsY6mBRx-tt1S016G0gSQbqmiveiIAFWwlb-lkuYgNR3j_AmJ0lh-8Izisph_gTnxlQAHQaJrmSxSyLWXgpfHqLcVTgQfto1tyAj9o3z96NedfPBvi011o-uPOYRlTetf_GcUmJVDJdRE9LgrwkBnh2xs4ST82zKYlNLMdtJJlEwhKsDSlTXqSWPchxWIj8GK-DpngQ9x5LLjkQiM6DLDNCFlNSdbBQu5-wXwWVm5xlti7SUF5cnzpPEm4B-9QwVc126eU4sYmyX5iJOuEuf115gEv-LRVGwDqDaUv83u6nY9vd7cvfDTMGAUUM05m_sP7G7kGsd5_wmElRGfRZUHKmpBB8dotlucHdHP8gohkYZxUs0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از صد شب شما مردم بگویید...
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/657388" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657385">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df2aa9553.mp4?token=sUW6an4XM1v5qWHoHEHEsYgLpMoPxjMqnPeTIVMVETZdG1d87oHjhOH07pU7-WnF5XYWpm7yhxe9fFTInP_XNdd2RL5r-x8KyWEa5Cg8VrOZiGn647sdxIEhGZ_wjxO9A8P65Fbdy7ImN9J9s_3X5z0jyGsEclkFj-y4pT4__oeER_w0pKOMS7rcUYTqb8BaoQ8_QjIjQtjh3A0u1E-d5lWlKORJspeSceZu88F_ODf4KJJEjBP-AeU1BoojkOMxjhRU_8u4Z6VPSGOfXbQl1rVnNTzgAQQep1VStfXb2v_X23fd2ER4fBh4Z1nLOSAEHnSQLy1On9Qr3H9_19GJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df2aa9553.mp4?token=sUW6an4XM1v5qWHoHEHEsYgLpMoPxjMqnPeTIVMVETZdG1d87oHjhOH07pU7-WnF5XYWpm7yhxe9fFTInP_XNdd2RL5r-x8KyWEa5Cg8VrOZiGn647sdxIEhGZ_wjxO9A8P65Fbdy7ImN9J9s_3X5z0jyGsEclkFj-y4pT4__oeER_w0pKOMS7rcUYTqb8BaoQ8_QjIjQtjh3A0u1E-d5lWlKORJspeSceZu88F_ODf4KJJEjBP-AeU1BoojkOMxjhRU_8u4Z6VPSGOfXbQl1rVnNTzgAQQep1VStfXb2v_X23fd2ER4fBh4Z1nLOSAEHnSQLy1On9Qr3H9_19GJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشکر شهروندان لبنانی از ایران پس از حمله شب گذشته
🔹
پس از حمله ایران در پاسخ به نقض آتش‌بس و حمله به ضاحیه جنوبی بیروت، برخی شهروندان لبنان با انتشار تصاویر موشک‌های ایرانی از ایران تشکر کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657385" target="_blank">📅 16:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657384">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اعلام جزئیات مراسم وداع و تشییع پیکر رهبر شهید انقلاب اسلامی
معاون امنیتی انتظامی استانداری خراسان رضوی:
🔹
برنامه تشییع و وداع با پیکر مطهر رهبر شهید از تهران آغاز خواهد شد. پس از ۳ روز وداع و یک روز تشییع پیکر مطهر در تهران، یک روز تشییع در قم انجام می‌شود و پس از آن نیز یک روز تشییع در مشهد انجام می‌شود.
🔹
بر اساس مصوبه ملی، هر گونه اطلاع‌رسانی درباره زمان و جزئیات دقیق مراسم تشییع توسط دفتر حفظ و نشر آثار رهبر شهید انقلاب اسلامی اعلام خواهد شد.
🔹
تدفین پیکر مطهر در مشهد صورت می‌گیرد. البته مراسم تشییع و تدفین، همزمان صورت نمی‌گیرد. پس از برگزاری مراسم تشییع، مراسم تدفین در حرم مطهررضوی در شرایط مناسب صورت خواهد گرفت./ اخبار مشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657384" target="_blank">📅 16:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657383">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
لغو تمام پروازهای کشور تا اطلاع ثانوی
شرکت فرودگاه‌ها و ناوبری هوایی ایران:‌
🔹
در پی صدور اطلاعیه رسمی هوانوردی (NOTAM) توسط سازمان هواپیمایی کشوری مبنی بر بسته‌شدن فضای پروازی غرب کشور، تمامی پروازهای فرودگاه‌های سراسر کشور تا اطلاع ثانوی لغو شده و انجام نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657383" target="_blank">📅 16:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657382">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
۱۵ نفر در پی حملات اخیر رژیم صهیونیستی مجروح شدند؛ تاکنون هیچ شهیدی گزارش نشده است
رئیس سازمان اورژانس کشور:
🔹
۱۴ نفر از آنها مربوط به شهرستان ماهشهر در استان خوزستان و یک نفر نیز از شهر تهران هستند.
🔹
یک نفر همچنان در بیمارستان بستری است و ۱۴ نفر از مجروحان پس از دریافت خدمات درمانی و اقدامات لازم، ترخیص شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/657382" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657381">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رژیم صهیونیستی مدعی توقف تجاوزات به ایران شد
یک مقام ارشد اسرائیلی مدعی شد:
🔹
عملیات تجاوزکارانه علیه ایران به دستور «دونالد ترامپ» متوقف شده است اما این رژیم همچنان به تشدید حملات در لبنان ادامه خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657381" target="_blank">📅 16:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657380">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
احتمال تأخیر در برخی پروازهای حج تا ۷۲ ساعت
رئیس سازمان حج و زیارت:
🔹
با توجه به شرایط پروازهای بازگشت حجاج احتمال تاخیر در برخی پروازها حتی تا ۷۲ ساعت وجود دارد.
🔹
برای فردا (سه‌شنبه ۱۹ خرداد) ۱۰ پرواز پیش‌بینی شده که امیدواریم بخش عمده آن‌ها انجام شود.
🔹
روند بازگشت حجاج با سرعت بیشتری ادامه یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/657380" target="_blank">📅 16:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657377">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qr3Bwyn87ipesRV7tQgW6QxBGXTiZjGC83hX_lohw_lFAumasOCcnDLElqO_ljsilrOloTRf5sqVTaTyZKPRKk5FCnjm8TqEyI0Mw7LOuf3Rwc85cxJ0h0rILT2uNZcfa_5XNXcSW4X1PTkRn0rWUlMFUQ-FWEHdsWPQwMXRXK06ou7Rvk7Bn3ro84Lugo4qWo_oLEiSMwiMz8n-hFdLA84HTu9dfNc8TN4RgKeEcEXgkJtHMkbT2iVm149-cTYcEbQpHpjLLRkbD41R_hA1JGZnOgRZ6RqaLYvRclVNa30dWsKQeXl8EJObzfgwVePBmida5MgJOaGw7fO0GZEhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzoV9losd0BwGg2ssCFBjwUJEqk3B0m-024H66zsb-zLgyrHKNp60r4kYXlHN6E4bdxrlcC8Sp6Tn2h0pDFnlL04EObF57ht0ytUfinJAqLWumPIlUHFKmteMFnLkhrtrqzhHVtqn92Tvhe2NnVXZvaEjaHmkY7XQ1iGWbehKB7qPvYdIAHLbhQDQOdum2Hbx7M7mgcwgaD6hACdcW0nC3AqCjha3OQ2IJv5clxofUgIFaLohBlVRs5iUlHNjj6NNwIY8UIVxyoZTINROoObJv_w8stteBxeqXCkprsMYWjfemZNF_TRqfXDqRebZ3sM5m_zipwVF43nodA5Fd6P1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J581VRCZoW_BQ8f3jk_OSJp6p9m0SARuK-6gC65DN-X3CiTQ2ejuEVP56U0Hw2v66AQ5ONFpTZhGC1fYuY_HPbMBpY_K7zHv6FnwhmzunkKIG9qEl75t3IUiqMm7XcQpeZiTeRL42VrGFjT5w56k4Na4HOxwCtcnRbR62PKpAC_x_nxsJNZ74UMnB2MZl1dzDcXg-RKgb9QwQeFg-DI5f-R14Dg9lH8vJLaAbylTJJiSMse6s7BAT8nqdIydw3bsKg51Z2P0ZmOW-jGW2PPCzOPsjYSqF2iq0vdgMpWtE_iM02ORNqvESd0tImX7Kbw_p4c9MY9YVeFx-TOvvjaUug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشدار درباره مارهای سمی در کمپ تیم سوئیس پیش از جام جهانی ۲۰۲۶
🔹
فدراسیون فوتبال سوئیس با نصب تابلوهای هشدار «منطقه مارهای سمی» در اطراف کمپ تمرینی خود در کالیفرنیا، به بازیکنان و اعضای تیم درباره حضور مارهای جرس هشدار داد.
🔹
این کمپ در منطقه کارمل ولی سن‌دیگو، زیستگاه طبیعی این مارها قرار دارد و از اعضای تیم خواسته شده برای جلوگیری از هرگونه حادثه از ورود به مناطق طبیعی اطراف کمپ خودداری کنند.
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657377" target="_blank">📅 15:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657376">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آتش‌نشانی تهران: هیچ حادثه مرتبط با جنگ در پایتخت گزارش نشده است
سخنگوی آتش‌نشانی تهران:
🔹
از بامداد شب گذشته تاکنون هیچ مأموریتی مرتبط با جنگ یا حملات احتمالی در استان تهران به این سازمان واگذار نشده و در سطح شهر نیز حادثه یا آسیب مرتبطی ثبت نشده است.
🔹
صداهای شنیده‌شده در برخی مناطق منشأ غیرجنگی داشته و اورژانس و سایر دستگاه‌های امدادی نیز وقوع حادثه‌ای در این زمینه را گزارش نکرده‌اند./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657376" target="_blank">📅 15:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657375">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkF4X1ocqkXs1LmvPtcldJOYu4bkzTvNzlXruYFXX76mKf0yJx2KOpPnS1GFmzpC2I7go7QFYJvawu6oUWD_f6hvFuM3228QP20uCskgcM95eHpdxipz72KGnHb4RWf3EVzZuM-ObmTUuY5DGn0HJjk_x-FrOBYj8q8Ga1EMcDzh1Kg8uxhYNEa49UxiRPHqR4ArZ20q5jbG_fEZ9a_98aFhZvy2BKb0Eg-YBeC_whZqch7_1FMXvkztOkmdqd_juQbKJdqSH1kW-sm87K0eYS_jRyKGXQfTgJl69mHseSHm7gx4qXya-5R7rKuRgdbWcT7cY62ah-v-IkJVGGCF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آژیرهای هشدار در شمال اراضی اشغالی در پی حمله موشکی حزب‌الله به صدا در آمدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657375" target="_blank">📅 15:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657374">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای کانال ۱۴ به نقل از منبع صهیونیستی: نتانیاهو تماسی با ترامپ انجام داد که آن را «خوب» توصیف کرد
🔹
نتانیاهو می‌گوید تماس با ترامپ از نظر مواضع «هماهنگ» بود؛ اسرائیل اجرای «معادله ضاحیه» را متوقف نخواهد کرد.
🔹
شلیک به سمت شهرک‌های اسرائیلی با بمباران ضاحیه مواجه خواهد شد. /انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657374" target="_blank">📅 15:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657373">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT_cDKdbCZZfa89R8S8D7Y2cZqkioBixIgtGYCXmyjTL1iGjQpJLMSVdrztg9dHiunpob4J_ZPIUR53SBmQvBnhV4G8KnScYc6sSIKTWi2B-SOVFPIcTjHk4MYLYvewbpThdYVi25105TPsI_EiEQKIstbS5xZmS7qYOpGwt536mez2LIu1WLdbfNZpds3UGqxikDf3bmZTSP73FsU2BZ09lFoc7GLasjyl07Q5bgWFPokmiLEED35BpK7Yy78RMlc1dx_9EsGhQiH4PcdgPuIFAPtFGmcA0xp4dtFtb5mzOL60GeCvx8m1cRx4lZTzkBJqOo2KWhtdYg8O0s0wlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی رژیم اسرائیل به منطقه مسکونی در صور لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/657373" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657372">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdRvC77Q-Nj8RZx2TmrXYX7rj6YutlkFx88aPJWzEmjqdMVfhGLdv480lAum589Fc47NgtzFL0Ycj8wCAHAqRqPbXZU4APPQFOyqxDGLWSB26UMOCmhWXxI_c0PtSAEAnhpgdm271FMbeQPPRry5ENrckzjpqYgg5qwKYBrpLGT8S-1IQ7O1xYfdrgpoa-uApWUlhEV7jcuKhTQDcq0TN7LdOjM6fiCNx5rTe4BLN54aVmxOppSKnDlSM-dzpjor6D9_qioHNQ-fT_eoyVfhpYr9tymVjj5OrrO6vBbI98TisN1H7f26H5Um1O9n-Fuws3_HKbzd2vRmfQRW73sq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی رژیم اسرائیل به منطقه مسکونی در صور لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657372" target="_blank">📅 15:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657371">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
فرمانده کل ارتش: در صورت تکرار تجاوز، پاسخ شدیدتری می‌دهیم
سرلشکر امیر حاتمی در پی نقض مکرر آتش‌بس از سوی دشمن و صد روز مقاومت ملت ایران:
🔹
دشمن با عهدشکنی نشان داد به توافق پایبند نیست، اما حضور و ایستادگی مردم روحیه نیروهای مسلح را برای دفاع از کشور تقویت کرده است.
🔹
فرمانده کل ارتش با تأکید بر آمادگی کامل ارتش جمهوری اسلامی ایران هشدار داد مسئولیت تجاوز رژیم صهیونیستی بر عهده آمریکا است و در صورت تکرار شرارت‌ها، پاسخ ایران شدیدتر خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657371" target="_blank">📅 15:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657370">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqMmsOjRudaViTuHN5XqN5bn6LS1uzJ-1XeTjUCjDaUqiGqZKrUmmoFqFtggwIN7uMeZ-op-Xd2lBdlhhIFy49517VI2y4xGoGuMhyOVA1jLwW3lDYZ4qbFCMbL0U14zXurwzgmUSTLaUhSj8qMbDYHqN3Qz4nnAC1Isp12fWExLxaA_hC-uqdM1_Avte6YXoM_1WLNeGp-XsLIQcF4jN76LlpZ-pwI1RQGfYRDvtva51Xtm8MWgbPwLDdWjTnQA8fFJXx6bZkh_WX5eTEE9MOD0N5rBUKnyFuN70pCNTU2_nnasNOWYwemxSQU3gI8VGmndgxAVZuTklGUwL_Y66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تعرض یک ملی‌پوش ایرانی به دختر ۱۴ ساله در ترکیه
دیلی‌میل:
🔹
یک فوتبالیست ملی‌پوش ایرانی در جریان اقامت تیم در هتلی پنج‌ستاره در ترکیه، با اتهامی جدی از سوی خانواده یک دختر ۱۴ ساله بریتانیایی روبه‌رو شده است.
🔹
پدر این دختر مدعی است بازیکن مذکور پس از گرفتن عکس، از طریق تلفن همراه دخترش برای خود پیام فرستاده و سپس پیشنهاد رفتار نامناسب داده است.
🔹
به گفته او، خانواده موضوع را از مراجع قانونی پیگیری می‌کنند و مدعی‌اند پیش‌تر نیز شکایت مشابهی درباره یک دختر ۱۵ ساله مطرح شده است؛ گفته می‌شود مسئولان هتل همکاری لازم برای ارائه تصاویر دوربین‌ها را انجام نداده‌اند./ رکنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657370" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657369">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0270d3c6ba.mp4?token=G7jHfF6kX6MjWIzE59OuMkwSaZxMuaxrIt8oEo9QhoiyGyt8tR9l0VBX2zz6A4G2VU9DjG3excXqt3oChyuv-JLbIPqqPTR4ucfeS3sMUqB3F1VrRtBFqRl4-HVWVPj5zZwHVzMU4uyZHsFHlqB2xQ747_-aQootrsXtTmybPyiYEa_Q8LOeg-YN2Dcby0sydYYfN5F-beZThv776uePjiEfF1IY7qmxzQ6dU7O_27C5JWz9Kw0ckAq4fr1OkFSh-MKA7G-oN37JPnQUWXgYM2imZr_M9YytoFYVUwBF0dHR3dsS3qvUrebPrvZXZ5qh6cPgk4lpvlMfLOZFDX21wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0270d3c6ba.mp4?token=G7jHfF6kX6MjWIzE59OuMkwSaZxMuaxrIt8oEo9QhoiyGyt8tR9l0VBX2zz6A4G2VU9DjG3excXqt3oChyuv-JLbIPqqPTR4ucfeS3sMUqB3F1VrRtBFqRl4-HVWVPj5zZwHVzMU4uyZHsFHlqB2xQ747_-aQootrsXtTmybPyiYEa_Q8LOeg-YN2Dcby0sydYYfN5F-beZThv776uePjiEfF1IY7qmxzQ6dU7O_27C5JWz9Kw0ckAq4fr1OkFSh-MKA7G-oN37JPnQUWXgYM2imZr_M9YytoFYVUwBF0dHR3dsS3qvUrebPrvZXZ5qh6cPgk4lpvlMfLOZFDX21wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی خبر از حمله پهپادی به پایگاه‌های تجزیه طلب‌ها در کردستان عراق دادند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657369" target="_blank">📅 15:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657368">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📷
ادعای شهربانو منصوریان با انتشار تصویر دست زخمی خواهرش: رئیس فدراسیون ووشو با چاقو به الهه حمله کرده!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657368" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657367">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
۱۲ اصابت از شب گذشته تا کنون؛ هیچ مصدوم و شهیدی گزارش نشده است
سخنگوی جمعیت هلال احمر:
🔹
از ساعت ۴ صبح بامداد امروز دوشنبه ۱۸ خرداد، کشور ما مورد حمله دشمن صهیونیستی قرار گرفت.
🔹
تا این لحظه ۱۲ اصابت در کشور به ثبت رسیده است؛ هیچ شهید و مصدومی به ثبت نرسیده و آماده‌باش هلال احمر ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657367" target="_blank">📅 15:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657366">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3lUChKlGg3UspVdjZVp23GNfvfcsM6vVQxMGQ2glYTMZ5aoSO_dLrkvCFqiLFl2_sHyhihpRGz6R3F4ZjEPCrwMl6H8rgiX-QzVow6K87plkhH7JsxdSE5D_bHMs-Jwpu0_fWNtcKBcuqDU2CDZFKLAp3HvfGGBQi1EoEW--avUQ3DjIAQFgvqeUiO2pKy6QmX9qa-UYSCuIutrzhkpHWs7o51tRvop08L-lk8xbguXAtsE3Nc-rGwVAz7nv1jmUlQ7Bo2rlRzm_hMqm0FLA61aTw0d6NE2YNPyU0K1esp272nc8V-noa2qBsLBRZNtB-82dX16eJTYFNVjfaZO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: دیپلماسی و دفاع دو بال قدرت ملی‌اند؛ نه میدان را ترک کرده‌ایم و نه میز مذاکره‌را
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657366" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657365">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSMwFhwhmfJV5SfUlPJqIOdXgntr-mcuqFjizr7k1iQdd1w4uXTZ13C_aqL8XK74DNyjKQVj1Abh6EWWHCdBhh97yzijpWU2YNz2uyDYbFQWRrVpkhQYshQeaOJ7oaw8SSxFEn52lfzTvWBmxDeLgzFvE7sJuSWg98rvRPZemJHQWSXHCnoDEgj0h2Uw3UepB3PoBJRIYT-TOIuScm4ShAGWEj3B_Kfk5THNQMaxz0fFI0br0OKwEUk1xpweD6rffwj5LZl5fvm5tOpl3k0cAnK4BQ8ra5ee3MkFHPdZcV0b23InxtpDoXJP2F4ncgVUMYatksSl1Z2khHoBqRQ5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای اماراتی در مهر‌آباد فرود آمد
🔹
داده‌های ناوبری پروازها، تردد یک فروند هواپیما از مبدا امارات به مقصد تهران را در آسمان ایران رصد کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657365" target="_blank">📅 15:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657364">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم: تماس تلفنی جدید بین ترامپ و نتانیاهو
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657364" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657363">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
عراق آسمان خود را به روی پروازها بازگشایی کرد
سازمان هوانوردی غیرنظامی عراق:
🔹
حریم هوایی این کشور برای پروازهای ورودی و خروجی در همه فرودگاه‌های عراق دوباره بازگشایی شده و پروازها از سر گرفته شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657363" target="_blank">📅 15:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657362">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2att15hk28xM6ppf6r8lMe5FeEvnxtYZNad3LD08n8h_Guirbu5i9mBWpHqUkGw0SYM9x2ZEzVcMNBlPMJK-_pJ124nlnrraWkBfDTX4r2pztAKmN3HOjoLGKBBxHkgI6hcaIllss0HJFrtO7Wrdfzsqc7Ie7NVZtWwtmrq-jyFBJ6LGry7f_y7_Ecv9WmNFQMzSV_kODNGHmCJ-X-Iydl-vxR2XCFjyGlLIxsQATRp7JfgOx2eo9GMjUOiElAedTm1709Pi0ZdR5cDd-hRy-E8uOTzqTSbT6yZB-B20n8wNKKensW2nCPjjtuyDbDJ4WKpksYKuDreIJnhTmH-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به ۹۴.۷۴ دلار کاهش یافت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657362" target="_blank">📅 15:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657361">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): در پی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/657361" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657359">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3jhc7uOWB2T90HTnCcev0Mb5WNU7oiX2Ghg1gFeLEgk2BJRDkz1cwwz3b_7QXna6paId_Bn4B-P3RTUMHSrcPkr9LnI56EQ2CVmslE_XK7bM4XrmO2VKUZfYjnRQJFZMipfqN_vtGU9t4300fgfmCrabzBo77pMGebk4qo-LsXhGNb7Z1Kz4tauMhoKbLwJ23SzVtdDMk5g5KG7HfzcOcrqJxNRcMG5OhhK6MjyKTXv8_vU4qCrZ1O-4sjf8tAM3bkAVvVyb0PfuLj8Vj-_nxpKbYm1CBtBz5M6b1e6ZT1Z2WKWMi6la9KGwC6oF2BsEUtmQx9ujBpXZBZg_wiG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال
🔹
۳ روز مانده تا شروع جام‌جهانی ۲۰۲۶
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657359" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657358">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
اسرائیل هیوم به نقل از منابع ادعا کرد: رژیم صهیونیستی و آمریکا پیامی را به ایران مبنی بر این امر انتقال داده‌اند که اگر ایران مجدداً حمله نکند، حملات بیشتری علیه ایران صورت نخواهد گرفت
/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657358" target="_blank">📅 14:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657357">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرفوری
pinned «
♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): در پی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/657357" target="_blank">📅 14:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657356">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص):
در پی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.
🔹
پاسخی که رژیم جعلی صهیونیستی و حامیان آن باید از آن درس عبرت گرفته باشند.
🔹
بر این اساس، توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما تاکید می‌شود که در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/657356" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657355">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=PizbC7t1tkFSNl-vI4MLXWBb5Z9oYRBdFr07UBY6628lDdHn56tPweygz7GTP6RVbI79xD9PE-sU0sHJvvlbpVujaUEj1hb21R73P6BTNJdcRkH03A-q8DVCkpkr76ICvSu6mGioBRrUb8jJFEx0tfjJpH9gGnIjqK6vlc2UgCX-Ys7QK2GIiF4k3ZmaRYoYfGbBuDnRPLQdrbFuENA3_GLmj02qSjMmobGGc4HFU11DWvftkQOXGcSvp7fMxe100IUpCrMC-kISY_TdlXlI8oHDIk6GZ0C1wNiV6gveb1FrMy6ZkDGU-k9CS5S_zOAVJuFQDBfIog21s0bavyqVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=PizbC7t1tkFSNl-vI4MLXWBb5Z9oYRBdFr07UBY6628lDdHn56tPweygz7GTP6RVbI79xD9PE-sU0sHJvvlbpVujaUEj1hb21R73P6BTNJdcRkH03A-q8DVCkpkr76ICvSu6mGioBRrUb8jJFEx0tfjJpH9gGnIjqK6vlc2UgCX-Ys7QK2GIiF4k3ZmaRYoYfGbBuDnRPLQdrbFuENA3_GLmj02qSjMmobGGc4HFU11DWvftkQOXGcSvp7fMxe100IUpCrMC-kISY_TdlXlI8oHDIk6GZ0C1wNiV6gveb1FrMy6ZkDGU-k9CS5S_zOAVJuFQDBfIog21s0bavyqVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ شناوری بدون اجازهٔ ایران حق عبور از تنگهٔ هرمز را ندارد
شناور سرفرماندهی نیروی دریایی سپاه:
🔹
به تمامی شناورها اعلام می‌شود، ورود هرگونه شناور کشورهای متخاصم به تنگهٔ هرمز ممنوع است و در صورت مشاهده بی‌درنگ مورد هدف قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657355" target="_blank">📅 14:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پلیس: انتشار و بازنشر اخبار، تصاویر و ویدئوهای کذب یا تحریف‌شده در فضای مجازی ممنوع بوده و شهروندان باید اخبار را فقط از منابع رسمی دریافت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657354" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای اسرائیل درباره بازداشت «جاسوس ایران»
پلیس و شین‌بت رژیم صهیونیستی:
🔹
فردی را که برای ایران در اسرائیل جاسوسی می‌کرده بازداشت کرده‌اند.
🔹
به گزارش تایمز اسرائیل، مظنون مردی حدود ۳۰ ساله است که گفته می‌شود حدود پنج ماه با یک مأمور ایرانی به‌صورت آنلاین در ارتباط بوده و در ازای دریافت پول، برخی مأموریت‌های امنیتی را پذیرفته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657353" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657352">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-RAIIq0oR9T6mNatuflcUtA19uph9GMZFVaSn6oeaRjxd8Q5HdM7qF0SAxDzUUed1RtvAg41_a9oQjDNFJJlwsA29nMsSKun72m48DvBOj8e3IOfX9tkc4bEV9ORcwRy8p70q93wmgSjA7yd7At25qnjsOwyfL3yqMf_tf0COfIMu1kCE4JRYvyXYVPPtkrOd3ckdcCYHCq7pjMKUMYe_NaBZAna_J-CSWxfcp-XMxV9emkrbVlZdRUNcP2cwZNTnklg3E9GY49AOHLIubg9q2sDOom9H_cNsy8Hgb5rBeeaupCYPb9Dj9BFOF8HyR6v7uvxtR8ds4Yxbhcn9AoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا اینترنت قطع می شود؟
🔹
حالا که جنگ مجددا شروع شده ممکن است اینترنت بین الملل دوباره قطع شود. ممکن است بانیان ارتباطات آنلاین و مسئولان امنیتی کشور استدلال کنند که ممکن است قطعی اینترنت به نفع کشور بوده و ارتباط جاسوس ها و ماموران امنیتی اسرائیل و آمریکا را مختل کند و جلوی ارسال فیلم و مدرک به رسانه های دشمن را بگیرد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3221470</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657352" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657351">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5954bc90.mp4?token=mO35-7hDcl61AqI8b3Vl30dBxPfXf0pp3ZbKN6KCJrWACry0vHYZm7D_QMhiTgfvjBPH4e4T8un5Vl1b9l2_seuZI0HH7I0c8yfuwyrpWS-QWGLdRkZ7L96-8JB_i9sS46NlCKq0Q8RtPy-ppHQ8nkdZNjMfkF8zhIhFO9K-N1qQUlftR8ItqlSwirACFicJTVRHiePCDz2AzXgIjE1o1NeE7j5C7THuuQFW2QtoXC6JVbRls5uWE0E9jhTs900M97sKEog7x0elgUpLCGABg6cu9bMEtncgGEgnANAW5V_vmHVoMFb5EMemtPRmHBAa0h0KRIGJL7T-E8jjAKYghoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5954bc90.mp4?token=mO35-7hDcl61AqI8b3Vl30dBxPfXf0pp3ZbKN6KCJrWACry0vHYZm7D_QMhiTgfvjBPH4e4T8un5Vl1b9l2_seuZI0HH7I0c8yfuwyrpWS-QWGLdRkZ7L96-8JB_i9sS46NlCKq0Q8RtPy-ppHQ8nkdZNjMfkF8zhIhFO9K-N1qQUlftR8ItqlSwirACFicJTVRHiePCDz2AzXgIjE1o1NeE7j5C7THuuQFW2QtoXC6JVbRls5uWE0E9jhTs900M97sKEog7x0elgUpLCGABg6cu9bMEtncgGEgnANAW5V_vmHVoMFb5EMemtPRmHBAa0h0KRIGJL7T-E8jjAKYghoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر الجزیره: ایران بی‌توجه به واکنش آمریکا پاسخ قاطعی به قمار اسرائیل در بیروت داد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657351" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657350">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای گروسی: ایران باید به تعهدات خود پایبند باشد
🔹
رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: ایران باید به تعهدات خود عمل کند و از فعالیت‌های غیرقانونی خودداری کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657350" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhkUegO5xSArJZJM09kwJWZgHY1exjRM6zVuTT_3408LTeA5Sz9byHqTPNdUC_iCV4_Kq0BXEIZ1JovINOzkUByBpA0S1JuaPZ8wuwWMAJlgG2xygnVv1QRAmHQSN52A1V8Ir_kBY0d_VBYkP5qyI9GgSYJLaEHnVfrA54iTnrLltbA0UmsiA35nv5mVBO6MXEB7KPbfyVe2mAwqG5MnHUxvfrDoDATLD5xrkw5VchdPwdSdp6cfTKrpZO440G_IteqaRzBu6n07zjfR4GK6waS-EAy2xLCPAkE_rbji_14vbK7ENM-pexI5EaJP2Ou4bxki5_8XFv-ZifVGLijxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۴ ریشتر در عمق ۱۰ کیلومتری زمین، مهرانِ ایلام را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657349" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سفیر سابق ایران در امارات: آمریکا وارد درگیری با ایران نمی‌شود
محمدرضا فیاض، سفیر سابق ایران در امارات در
#گفتگو
با خبرفوری:
🔹
شواهد نشان می‌دهد که دولت امارات در یک مجموعه‌ای قرار گرفته که شاید خودش راضی نباشد اما مجبور است که با دیگران هم‌صدایی و مشارکت کند.
🔹
آمریکایی‌ها امارات را تسخیر کردند و پایگاه‌ها متعلق به آمریکا است و باید دید آمریکایی‌ها چه شیطنتی خواهند کرد. ورود آمریکا به جنگ اسرائیل و ایران به مصلحتش نیست و این کار را نمی‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657348" target="_blank">📅 14:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657347">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWGxpquioKStFX6o-_R2i5nXJcwdIlHFdHBQotmw82jf3lXZcmPqqkSGy-oVQohdaTbHZI-tG-dAHLqHjAbD5IpIuQMpy0QKAYMk4x4CypBThUinrKHhvaJdRk922iGIhWTBvsBzX0JqeSgEUoVKMaiknyxEpjmWQZVsXDMX65J7z1LqBYGlKfDmLOw8jNqXT938qFzPgyWp0YGf6TsWjl80d9OR7lBI3RQsalNRiK8966G1Gs7Q1kSpOBcT4iiyA_3hD3_2VtFHlGrpnoRI2iunzRwDGOZjcbSdg55DBGcELrWDOoH0RCiv3IWypQQ-TYzmsPLJD2kecXSEyoBSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت سفارت ایران در ارمنستان بعد از حملات ایران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657347" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657346">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnXW140TfwX1euEOdqrrRq3qrNJeQb0dnjUdpYPQGIVIe_Y3yp6vbElH4bqMuaiERWp0WJEaF80YLT2Wcb8F5PwsB6qJrsmqPHd0PH0cLboQcPpgIQKDZ0NCYZhM1X3e-nry1gIwfZC_M2RQb4nw0BZxNUuwQqwbQrTosDUhSqRV-kEub53NNOD-pyVPNslPmgtqF7X7sukB2dtglWcz7eg8qh-8ysbfhEwFz17GBT3Z-KVud8lv07zYov2rMcRciWplUeP-3YrinwzK7YcwWHl6kz5Ry0cPwvKFOb5ePyiO72tK4fNNaZ5VkWjVKZcrNLjmKdR6TuZqkb9acppmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری که شبکه CNN از ریزش سنگین بازارهای سهام شرق آسیا (کره، ژاپن، هنگ‌کنگ) به دلیل آغاز دوباره درگیری‌ها میان ایران و اسرائیل منتشر کرده است!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/657346" target="_blank">📅 14:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657345">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cefSN9gkv8x22Rjeih07JxlXKST27BOJneeFu_4hypgSt3QklxGbVPVUh7qXcfw3jZCdHEa3vB1i8pQuJmqvyWuaN46deVg7su1tCPQIgoSQCYYQwiRfUHL-Gs47uda28RSFyVv0TET12l7QvH-SzNmRZFsgELofaG3QIc3wk318CZAa6uRbw9Azj1ol1jzF7gnKvT7kk1PhiNXHCTuZTfufLvDhru43d_HWjermtEiJPaWuQOD8aMUyybM7euA3WbxUoDATjccVjXukUDFN4IyoeoMtXLzCo41Cj5jg9l7sMxjYiS33X0lQvMO2EMuvp_ALd_YwZjjTuD95cN4dEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیل و ایران باید فوراً درگیری را متوقف کنند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657345" target="_blank">📅 14:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657343">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
جروزالم‌پست: ایران سه سلاح هسته‌ای دارد!
روزنامه صهیونیستی جروزالم‌پست ادعا کرد:
🔹
ایران در عمل از دو «سلاح هسته‌ای» غیرقابل انکار استفاده می‌کند و جنگ کنونی غرب با تهران، بر سر خلع سلاح از این دو سلاح است، نه بمب اتم.
🔹
اولی توانایی ایران در بستن تنگه هرمز (عبورگاه ۲۰ درصد نفت جهان) است که قیمت نفت را ۴۵ درصد و بنزین آمریکا را ۴ دلاری کرده است.
🔹
«سلاح دوم» نیز موقعیت جغرافیایی ایران در قلب اوراسیا و کریدورهای حیاتی چین و روسیه است که برتری دریایی آمریکا را دور می‌زند.
🔹
بمب اتم تنها «سومین سلاح» و بی‌اهمیت‌ترین آنهاست. /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657343" target="_blank">📅 14:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657340">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیل و ایران باید فوراً درگیری را متوقف کنند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657340" target="_blank">📅 13:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657339">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اروپا تحریم‌های جدیدی علیه ایران اعمال می‌کند
🔹
اتحادیه اروپا در اقدامی خصمانه علیه جمهوری اسلامی ایران، برای  نخستین بار با ادعای نقض آزادی ناوبری دریایی، تحریم‌هایی علیه ایران اعمال خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657339" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657338">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69212ac3a2.mp4?token=Zg6k94XIbObl3djF-MGZt-bUvCYpodn4w_bW8DTERGKpUAOsrQ_kaffvI9AYpic7yd2tnsDIeXyVGMWlVGIqWN2I1VV5nv_E15LqkOMKGHJxFLTUAVJV5eMQVRtD9s-zwSFcRqbMyAfpDG774kiQAuQOe_XLSL9Boe1CR6DYcp3uWv6n15SVvfESWmEsQybUA8L_E3s0-3dqEBm-NKfxknTbksAS77DIQb-kUia83ldxZ1g67Wt3EDPJFhKJsUOmMGgk63FObbClTAt1RelIAkWVfzusyjFWSjZXV4IbpsHq0Q7JslcmTlLsMMXQCpRfTE4UPUY3olU9B7XOzaelHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69212ac3a2.mp4?token=Zg6k94XIbObl3djF-MGZt-bUvCYpodn4w_bW8DTERGKpUAOsrQ_kaffvI9AYpic7yd2tnsDIeXyVGMWlVGIqWN2I1VV5nv_E15LqkOMKGHJxFLTUAVJV5eMQVRtD9s-zwSFcRqbMyAfpDG774kiQAuQOe_XLSL9Boe1CR6DYcp3uWv6n15SVvfESWmEsQybUA8L_E3s0-3dqEBm-NKfxknTbksAS77DIQb-kUia83ldxZ1g67Wt3EDPJFhKJsUOmMGgk63FObbClTAt1RelIAkWVfzusyjFWSjZXV4IbpsHq0Q7JslcmTlLsMMXQCpRfTE4UPUY3olU9B7XOzaelHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک کشتی هندی در دریای عرب دچار آتش‌سوزی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657338" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657337">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e62e35608.mp4?token=smR-j6_aCUZcc1QY8AQx03S3U6Kwu7V-b9ntfwomj_u3Ge0ALSYqnF8tdj102zJPnpUGQl1AB_Iql-dfA2pXFuwta0r5VIyWOrbS4anQ04ZDBSAkAYtLtu0hXaj_sbLaNAUIyJvbdxKWWXZKzxaAn0honBZTQIvPNd4_bje3f2WI2nN9FWb3msuHojgGHMczIVDEMXPZlNFxIXr3r0wQ-aZooK0YfJDAlgvPehvMgjVp-CyElxtqfpyoAzbblOG6WE_9IcwAqpG-P2WH5suhc6UyNvUJniNa7fsjWGSjYOWD6jHdYmAnDP9KXT9hHAEaHeUndUdookVvKnvI0c2QiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e62e35608.mp4?token=smR-j6_aCUZcc1QY8AQx03S3U6Kwu7V-b9ntfwomj_u3Ge0ALSYqnF8tdj102zJPnpUGQl1AB_Iql-dfA2pXFuwta0r5VIyWOrbS4anQ04ZDBSAkAYtLtu0hXaj_sbLaNAUIyJvbdxKWWXZKzxaAn0honBZTQIvPNd4_bje3f2WI2nN9FWb3msuHojgGHMczIVDEMXPZlNFxIXr3r0wQ-aZooK0YfJDAlgvPehvMgjVp-CyElxtqfpyoAzbblOG6WE_9IcwAqpG-P2WH5suhc6UyNvUJniNa7fsjWGSjYOWD6jHdYmAnDP9KXT9hHAEaHeUndUdookVvKnvI0c2QiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع زلزله ۷.۸ ریشتری در فیلیپین
🔹
زمین لرزه ای به بزرگی ۷.۸ ریشتر جنوب فیلیپین را لرزاند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/657337" target="_blank">📅 13:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e513ad5e.mp4?token=dOu26qHdsCB8r2i7zhsvfp1Ap5o5qXl-asl2QYWLt75GXIqu5x-jNQMhYjD6P5KOmKDpLeHz1_REnsmL3KOpsWZD_6EXTfl4xEs0aqFaJrKSFNy8GeabpLHibXugSwqxrlSoUglhAhujT6OeAbfC2Xmk3m9XjPTgiPAA1_LPtHlE0jSAGHo8O_tR0OXgChi3-5Y9c_C9faLIx8J0GVIAzF1C48YyhPlvClyCQ0gbmF4xPjOg_zXwtm3LdoV95AcJIwKnQWZNGieu-fq9Kqgz-UzL3gRjzC6eWdQtJqGjw854C0Y8bPi7I8HQ4BSKs7goD2IKfght5bOz7y9CXtEwyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e513ad5e.mp4?token=dOu26qHdsCB8r2i7zhsvfp1Ap5o5qXl-asl2QYWLt75GXIqu5x-jNQMhYjD6P5KOmKDpLeHz1_REnsmL3KOpsWZD_6EXTfl4xEs0aqFaJrKSFNy8GeabpLHibXugSwqxrlSoUglhAhujT6OeAbfC2Xmk3m9XjPTgiPAA1_LPtHlE0jSAGHo8O_tR0OXgChi3-5Y9c_C9faLIx8J0GVIAzF1C48YyhPlvClyCQ0gbmF4xPjOg_zXwtm3LdoV95AcJIwKnQWZNGieu-fq9Kqgz-UzL3gRjzC6eWdQtJqGjw854C0Y8bPi7I8HQ4BSKs7goD2IKfght5bOz7y9CXtEwyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا زور کنگره در جنگ ایران به ترامپ نمی‌رسد؟
🔹
کنگره برای ترامپ در جنگ با ایران محدودیت گذاشت اما ترامپ می‌تواند همین محدودیت را وتو کند!
🔹
نکته قابل توجه اینجاست که کنگره می‌تواند جلوی رئیس‌جمهور آمریکا را بگیرد اما با یک شرط مهم ... چه شرطی در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657336" target="_blank">📅 13:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اجرای متناسب‌سازی حقوق بازنشستگان در سه مرحله
عضو کمیسیون اجتماعی مجلس:
🔹
متناسب‌سازی حقوق بازنشستگان تأمین اجتماعی در سه مرحله و در چارچوب برنامه هفتم توسعه اجرا می‌شود و هدف آن رساندن مستمری‌ها به ۹۰ درصد حداقل دستمزد زمان برقراری است.
🔹
حقوق حداقل‌بگیران ۶۰ درصد و سایر سطوح ۴۵ درصد به‌همراه مبلغ ثابت افزایش یافته و تأمین منابع پایدار برای پرداخت‌ها نیازمند همکاری دولت و مجلس است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657335" target="_blank">📅 13:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657325">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اولین واکنش چین به آغاز درگیری دوباره ایران و اسرائیل
لین جیان، سخنگوی وزارت خارجه چین:
🔹
پکن به شدت از وضعیت فعلی نگران است. از سرگیری خصومت‌ها به نفع هیچ یک از طرفین نیست.
🔹
چین امیدوار است که طرف‌های مربوطه به تعهدات آتش‌بس خود پایبند بوده، شتاب مذاکرات را حفظ کرده، متعهد به حل و فصل اختلافات از طریق کانال‌های سیاسی و دیپلماتیک باقی بمانند.
🔹
آنها باید شرایط لازم را برای بازگرداندن صلح و آرامش به خاورمیانه و منطقه خلیج‌فارس فراهم کنند. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657325" target="_blank">📅 13:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657323">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
یک کشتی هندی در دریای عرب دچار آتش‌سوزی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657323" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657321">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d2ec5f1.mp4?token=qJ-YCYOCoI6iLF_TUg-phPl239Poi2hRr99Xe_6lGiduf278Mslde1tu1K4CUFWxJf-z6myyiJRv2j6lj_b7aHBIjV0mTTg7H5xeldCNElz1tjDdKbDJ7ICk3f034Rgtph5S41Bybe7nUBnslWkalsjsvI2s_rv1dYFaNmRib2u_vERG3uuETNxcd85c9gM7PrEJRRCOyN3N0wbheM0agxdnBadXoPbZSiVTvVrouw6oZHl9FiiR_NaF5EW6KvUxTF-euGrcyzVB8Xw-VHH-HZznkkUdODJzJ3Uaz5_ncXrpLQy6iZujJFiFERKkd-SqiEDWYJ1UE5SRC-PgsFrOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d2ec5f1.mp4?token=qJ-YCYOCoI6iLF_TUg-phPl239Poi2hRr99Xe_6lGiduf278Mslde1tu1K4CUFWxJf-z6myyiJRv2j6lj_b7aHBIjV0mTTg7H5xeldCNElz1tjDdKbDJ7ICk3f034Rgtph5S41Bybe7nUBnslWkalsjsvI2s_rv1dYFaNmRib2u_vERG3uuETNxcd85c9gM7PrEJRRCOyN3N0wbheM0agxdnBadXoPbZSiVTvVrouw6oZHl9FiiR_NaF5EW6KvUxTF-euGrcyzVB8Xw-VHH-HZznkkUdODJzJ3Uaz5_ncXrpLQy6iZujJFiFERKkd-SqiEDWYJ1UE5SRC-PgsFrOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه خاتم‌الانبیا: دشمن ضربات سنگینی دریافت کرد
سخنگوی قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
نیروهای مسلح ایران شامل سپاه و ارتش با آمادگی دفاعی و هجومی بالا، به وعده‌های خود عمل کرده و در موج جدید حملات، اهداف مهم و حساس در سرزمین‌های اشغالی را مورد هدف قرار داده‌اند.
🔹
ایران و جبهه مقاومت در برابر هر تهدیدی ایستادگی می‌کنند و در صورت ادامه تجاوز، پاسخ شدیدتری به آمریکا و رژیم صهیونیستی داده خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/657321" target="_blank">📅 13:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657320">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
نامه ویژه پاکستان به رهبر انقلاب تحویل عراقچی شد /تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/657320" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657319">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
منبع نظامی: ایران برای جنگ طولانی آماده است
یک منبع نظامی:
🔹
ایران برای جنگ طولانی‌مدت با رژیم صهیونیستی و ضربه به منافع آمریکا آماده شده و تمهیدات لازم برای این موضوع در نظر گرفته شده است.
🔹
تصور محدود کردن پاسخ ایران با «تنش کنترل‌شده» اشتباه است و تهران سطح تنبیه اسرائیل را افزایش خواهد داد؛ آمریکا نمی‌تواند از مسئولیت اقدامات اسرائیل شانه خالی کند و در این زمینه هزینه خواهد داد./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/657319" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657317">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
انهدام پهپاد دشمن در غرب تهران
🔹
پیگیری‌ها نشان می‌دهد پیش از ظهر امروز دوشنبه یک پهپاد متخاصم در غرب تهران توسط رینگ پدافندی پایتخت رهگیری و منهدم شد./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/657317" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657316">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGaMMBX-UFCVin9gBA7wLmhaPbOGRMu3eVheKC9pxryDS_Agz-vjfsU7leYqwKyWdYzNX9OBpkP8GZ82budMYA1Ipf0pOuzoNlk2sa-pKa1EAxE3aPXw7oXJQ8awfmBexgEROI-HMD4_krvl4cWJUcgzqx39WnmxCtD9lNRMRFSjwRXahQlDliTX7gd8wx0Y--1cjwUrD6gZ1CIGzUOD_Gol0MGHQwrB-ojsNuU1xRNKNJ4Eqrf_yesDj-aFP_CNiiJx1FGCMyfbtoOyulTfqqnv9UKggutm3q62dYmzzjAETP7Yo7Z2qBb0u-0QWaVl_k56OprZwNLxdrmbVQkgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ישראל תתמודד עם מכות קשות והרסניות יותר אם תרחיב את התקפותיה ויחלו התקפות הרסניות נגד המשטר הציוני ותומכיו.اسرائیل در صورت گسترش حملات خود با ضربات کوبنده تر و پشیمان کننده روبرو و حملات ویرانگر علیه رژیم صهیونیستی آغاز خواهد شد.
‎
#WillPayThePrice
‎
#هزینه_خواهید_داد
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/657316" target="_blank">📅 13:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657314">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_hj5q__wlrMrXQ4LjQ2GCycqWrLbLhFQv-4XAqX2Vbu0KNnHc1GcLICF8QGIAPgLoUWOw7TPv7Rfu8z1AtAC_hxXlXq5OVhDY69DLSLDwCDuWxDmcd6SFyz5pAu0ajRc1Or85SBmQ9xyLO1LVtJbV4SO9RHg1LttggE8jR0ZQiE8k2Wiu_In2XYp-QyjR8ZrY9kWUKM7L0LHjn7hwnR0ntOjfcCTsOc4eldCH_EO3kwk6tle81Gio2XIN3sq4LvN27M44hKHnppsYB6UCBFoacrFzB7atlBwUQRB6bELH7Sw0zjWHwRUAsVJSS7lEkWneySm2eBFY3OscG4JtMiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
ترامپ قمارباز: اسرائیل و ایران باید فوراً درگیری را متوقف کنند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/657314" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657313">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfwanIjQ9Sd89Bx-AtSqBKCrBzmJw0CH6EuynwFpyXtYGfQIhcR4ciaXNQA3w1-yBIbx21dFvRNUa7AdNYSipPpEBfhfLRnVb5MTuisr6tYsIeZMJhsqlqEx1BS76xTsEi48ZTIMOCX3CR-Thazs9ryVva2nnW0vwGCGo7rl8PQL0DhhKqRloT31qdeyx_w9ffwRE9s8brn7faO3Ov_Imvc3PLdP3427J0r0lX2zO-a7KOcTjX1qINFrdVSg-MFU8nFziFysLW0zV_AP-FQipGL4Sfxxz4EIwZYgllH0rA-5o8WDEt6aj8DmmlRtLmOtIUrdCCeNH8wq0LM4P7JA7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مجمع تشخیص مصلحت نظام: تهران فصل تازه‌ای از سیاست دفاعی خود را گشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/657313" target="_blank">📅 13:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657312">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
هشدار دادستانی کل کشور درباره انتشار تصاویر محل اصابت پرتابه‌های دشمن؛ با متخلفان برخورد قاطع قانونی صورت می‌گیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657312" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657311">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
منبع ارشد امنیتی ایران به المیادین: معادله زیرساخت در مقابل زیرساخت تنها شامل اشغالگر نمی شود و همه باید به جدیت ما پی ببرند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657311" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGeXoJkOz3XqzA_OmmL-AGjB0S6dCjWbHFMnwPVF5elO0RaTfjpzC06mcs9tL3wnF5H8vi0jwWfvPGBSNWGRt_swACBK-GlIDjdeoxC-pD737ZzJEqSkIelqZTVw54GYUOOxACueSkbV0-t2aHFDJv7-2j_9yO2TKeDKwViaURsrPJltI8BFfys_mNPugKcHg8J0HYUJovkkJPSzZNWfUHJAwumcJQqF0N7wrSt5GlPkdO_F-JcX1LB8jIDIBx21PaFpRUn8uhCLH5whtinnMV1oBMIv0Cz-S7AMsDAFp9jTRNTuKTcyp5ccjIGPBXGKLT3bahLbq7eoPmbfdxqx_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد ارزش معاملات خرد بازار سرمایه شکسته شد
🔹
در حال حاضر ارزش معاملات خرد به بیش از 35 همت رسید که بالاترین رکورد ریالی ارزش معاملات خرد در تاریخ بورس است. /خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/657310" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657309">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
یک منبع آگاه نظامی:
🔹
ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد که انهدام آن توسط سامانه‌های گران‌قیمتی همچون تاد و پیکان بسیار دشوار است./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657309" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657308">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJMsOQ0aqoYpuAPt4EwBlCCBjBI8CjnExPmnCH7wZcqkz9FVZe2BM1lmgDoWr8KLrCwBnn4jPld1TKLYlp8Y4Ai1DqPLr13frVrZc2iktFvDUIbyttBt8TPmx4WYIv9cSa71jHPZP4AhIG9xI5ZIGWe4TL1gyY83qVhlaX-2fxQlNWJkd7wSA4JHzT46MBBc9E-wlua666haUL07ESN-LmyOWS1L0tMenbvvSyJw4ovSzzLXVhplobFf5rYoIkS_XXyjJYqirsLOJFLv7w540EuMaI8yLaGfo8Dj0JRGZWBomapxJoZHBmvZH6M-6nqjAUmM5B7rUqi92Ze2wx12cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس منتشر شده در برخی کانال‌ها به عنوان انفجار در تهران مربوط به ابتدای جنگ رمضان است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/657308" target="_blank">📅 12:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657307">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYD87MD__5T_JR2aCvEjt85UKx_SPdzvrcPmY8jY-lyHfClB7FZGG31ls7QQdTsFTCmVhdD_fBkCmHy4HZkGi8L88pg4UVOtqvrYqBicFX7d79T_2RIiaeywVduM3iPR4qzezEwl0V1OIa_p7lEsmHRTZN71iwCV7vZxiXsXPdHz8ZdPHdFj8WPnhLLvOlwKHppOjjjZdZyxtmLUpyj8zZCOxN1kLnhf8A_nhN7Gqb5888zWeQl9S8nwEyz6C4T1aT-vkQT-B8IcVzGvFeSg4efcs-2VPO9G01wy2nuRq3Psro3oUYn4jBpiQzIC0_swcxOI9zVbl1EhpjYIfDFCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از لحظه حمله‌ور شدن الهه و شهربانو منصوریان به اتاق ریاست فدراسیون ووشو و شکستن دوربین مداربسته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/657307" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657306">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
هشدار دادستانی کل کشور درباره انتشار تصاویر محل اصابت پرتابه‌های دشمن؛ با متخلفان برخورد قاطع قانونی صورت می‌گیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657306" target="_blank">📅 12:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657296">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXixfP5_XVMElxYCYsQT5fUr4Bm-2CA-sRU2OUjUrd-T-nQ3rpn8HbwmKKC0szlhXXgM1EiqlkTM_vlHqu5Lo07QEh8fM82RvLPe-knkEZk74Cx5a-4VRssM9vu2C66KxYw3XaGIm1zWd2rucxxpf3MvZNq7s2L1VsQyZSQLIyOcaU8II8qeKF5-0VlmlywIODP9ERQLAvrVgqfhGKmMc_3QhBWABGEkcphV3UKLjIinFVvd0feTc7Zji6qpdXolcuAXkGrmmHafVmRo-qjsc1mh0FVI5cBIMFQEaCNejHbDypnPT-yI002EmHAoPxsY_CQXYeSbl0IOVWNmgHphEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NStMAv_OtX7CifNBV6r7zFudJq_oGeMr9gObh4tYP5FAWSPFZctGSxXECTWvYdLZTgWjP4VcjTfNmDLX8dOulFHJQ3Mkb0YzKJDw7lMKoADdaPf4TjD2cgRNeRhbOUYjm6fTDBj6bQCqJHWza9Eaxhc67WZO-1VtpXcSgnUMVbkORcIxhe5easeh6boO8ZicjDsYyIakcF8aVNQk8ytUTKBAMqZ19P7Bcpnpv0JA5wS9hKN1bmzUZyq74WMAAv-6W7JdjQxyjSm3iOLupCDj6oFIrPLBDRSL1JOLz902N5Qff3oSqHWlmqhgdXRWDBTYT7pVo-5kUWdR4pojt8SN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUFpAm08mZFhjkV1V_NrorHkJlxkS-lbWsWWQm-DBdeFH4Tucu1QO4REf2AtHQ_SnlK-9KfBn8qkIB7v6SWG33ljAhPHlY2-3VCrkIo3oXt2EWZBDdcfO3EUwPpUeAKS0TgDc-uXvzUmsntakMGNGhd0w0eC9xNWGdV55PPZ-z7Fjm81Mc4pvZ2NIj8gb4Q39yZwwr0WFRlLSz7wqoZDynpC4CoJq8CD9uwuQuMxPcmeGTNze90MHK_w7AfEme0OST1PagOVR8llugNe7gasyaNvtHwP562LzDUsZ2xaT53y8w21vg1R6HREznPi5JKdiytkiEgHkk2PEXX75xNNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPQZWDKc0AsXU2pNjzOUuBni00laJgba_Ag0_OHbc5RfwrZF3jORxKpz7dvrVP52rqxJ2Hb7P5eGCyhYshbGec3TPhY1KmQg_K8w9S_1klbyGI7Cdw1CfO0lMoTGjEy9htZJzOzwJrU6U3tXs1dzy1PUDimtLnxeW9sKRo1YxxiHkZHNaRxDb-HkrK-PfppIRX1k1o8p8G6ZwtQKTEJffYNe1s-7t0UbXknVUcEvEGw7tKE1yINlYfdNZFhfoD-LTZks1bNQ8iH4s25dJmozMW3nQWD-bNvfPuozGdaJkj6BJAEuCfDyKgOa4qOIDOnNo8bJkt6jyoXd64ZRdCM3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaLPi9MviO-jWfAf9_PFxy7SDbpVSIYGETMgSKJxDQ5TwjejbX8tdZ3D75WICGasrd_7X4a-1n2VLCaPAvyOywxCwl2yiq904r7BsFtCU7oril741E9YjhMki9NlhmhcjXmjtOeaG6-8YqoARvNliklWw2Iqw1C1O8-SfO-Z-VNdVKbMse96jMzOdJNWHCuGwUeUbwsHjPbCxopjescZTNROlQrulBBz_nE7FZXFtJ4I171NNdzfAJPkGcXA4fT1278kHSzYPBjEz4TqgKzqQ7kH5R3b8TEyJ4ptPX7iQ814c53VjJ75qwNxr3UZ_SNJdXL5UQNUWdXcxq88usSndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZaCPeIA-XM42mSTJNgWIxA2HUhXT5SwCNXBrs7kBBeYbp1RRVeV5ouf5OTxRn4YSSOpyiAYO9-hvyiDeGPNJHjT-Xqy-Dlh8VwzgnCDICOWv8ZrnHboxVDen8q9GZhhj5YsQXfjNak-zVbDI6hfE3qrobY3ZSY7XsV59HrskfTKRvSR8KOc_8u_ckCXlu8Zt2o2S7G4xnt9S-L_mWo4zR0EbODNzYKHkLuL0UCKFo8VLUmcj07A_YiEYkP7IyPtH1gquESg0vlu3soXWjf-m4Vu3ZsRPgoCqnTA4bhlbY_HwOLwBFPJCNZOIPxjmVib3Ae6q6M8p8NUTBPSwIQlYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSU4HdvrFWU-lXNtJ3-uJJDh2SiZ10JkVKE_JyaKFj29w0oOog81pDQPs_U3_DMEsVVeayD__kbCojhDJYy9Pu3SgxyhKxv43bqJsXblH138tCeUMfYb8RdqdCl6DnvcBiHu0Vd7a-_ybTkPBc5BNdpG5b6Mjze6JWcfXnW_4fKiIkTtXc7RWfo29u5YWYE8efF4c0TJUDEdZXL-mY0GKTSjSeCo8LCTgJYBBOEtiMlfJ-Ne4_vhPJzBa3A0tpIwosqLBNW5t6W7lyTsQ7HAyFhsEwdVNYzVsA4Jk-E-ruvx-BkASJrS0iuFtyb9dfbk_AbKvpnIuQlwQC9X-wHWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMUP4It2fdKo_wUTRHJXOgydxbiQ7eJdas7p4wOVIQvSdSdqElIN7xofTUnOfEEVEptqucPB8qFtCKxhk7usyBVKUkEOJyr7GGsz97aD2M-s-Vujw2yS14cjY7EyD9HddoYcqm9j5pgb6g82AIKwMmbR6hZIRRRA7pwCaG3_Qajstipqiz7SwL_kKwFZExwDHQ7eMyE4fnIr_R22N5jJMHv2Kjd0Q1nxD3j2SVpIi2hIkOUnogjFOmbp4eVWkxBcwQ-dFgNs8lLnZAeqLxDETWPk68UaDwoGzWvJAmjwePXshXGPcU_M5bFbod0r3hsV8HuKVIKpcmzYSIl48am0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkGLHsEPeryyt66K7PH_39IAVFFGpufDUoPpRPn59Tmeqg6MPsF6uE5bxMCKo6yh7UsnH1UAEvxzoRwvPsRIuD8Ydk435XbzKG0aTds1ZlP7OFcW6AK09_-zcrmR7riFFfXiSXxvB9YrGGHPQLqJHvHqMvFj5_NQxXPVg5TOVsySdUZXLRbeKif89xsmHZSTezPOzL-iO9DyHkdb7zS7QenWI7AAucGKPr0Gq1x5whJR8nSOxwPMaO0xaogdNdZ71tuGPLJUmEGZC50amZSOK3Q8rFtWyAqSTWmXBZEqIXyaYLeXrqLmxJJ1WybnfOqvP9tf-QjB3SCAWvmEjEihZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8KeLscyQYwM5tfCWHSBnK9Wb6O2w602zciqoa8KZzQ3IkwJLuFiS5tUXdUlXZuWwnKrby_W54TQCugpy4XCe-KTIx4g4Acm3nVh5t7Zj9XWx3Z2Gg-m8rL8q5UGiLfF7dBi0k1uBgJ72rFfjaTf0pLSn1E1TcdR_N98AzZMjA2f_MTY1x0gXa7_qC1fhfuiS3chjhw_2RQBu9sMlVPq671HfmdxlUgxJ6tRUfi6zcsklTnmBFmk4jNbfkL6gT4jCB0RbLUhAjbWwAIfd55zmZ6tGq8dfIiZsiDu-k-udgZL3Ol0mVJZ49F_W1w2TOJ53IMTaXIHd-I9CTQN0jjs9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیشب از مخاطبین ویراستی خواستیم یک پیام برای سید مجید موسوی و اپراتورهایی که پشت لانچر نشستند و قلب تل‌آویو را هدف قرار دادند بنویسند
🔹
خداحافظ‌تون باشه ما که تو این اتش بس لعنتی.. جون‌مون به لبمون رسید الان چشم  بچه های میناب و رهبر  و مردم شهید چشم‌شون…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/657296" target="_blank">📅 12:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657293">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHO608U3JHxSPIUVyE14g-EB11b-JjSO95xGeqTEqhqblF5CQ-uvdxeW2pg6crZG1YaZg0SRkRiIjb8frBMT4p2kq3K--6pRkGxl7vyCFjdLH-5bDvaTGXzdgUhB2lTlWHSJ2TzZqr5-foxseWTluUA2vaqGn-S1Uup5vZWhpNcUdf_ktf7j8QRidlLlcPruJaICLBF0MzjZA9Fu3wzL2NvN5HjeBHY_rlb9ZSJJ6NvOKE7gIoxW_GBvXkBV3jmP0nFsuIhep0DXx0afEeKipa3KBAlNtCqKlADnxxwpaweGrQ0Dqs2GADNQatQSLde3mmPN9PTGsvwaq-bJ7kcpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی: قوی‌تر از ۹ اسفند آماده پاسخ هستیم
🔹
سخنگوی کمیسیون امنیت ملی مجلس: قوی‌تر از ۹ اسفند آماده پاسخ هستیم و تا لحظه پشیمانی و تغییر محاسبات ذهنی و ادراکی دشمن سکوت نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657293" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657292">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c6693569.mp4?token=jfq5zm-t_CTYKqY8et0kOfW4FJniM_mGT4ZNr5kTvZipAyYtjDZT3F2DbDm90c2IPmSQOgXZpdUpyiGbIFfVUh-CDn5yx7m3BRSRbI8OqzXStwB97oCLFyxVHa_gWoybH-u4UGn0S_DtmMzjuBBE-Xzo835dPl9saDVx8HV-XaSy4zn9u0UjRqy4lf74sjwuXMfQjgjfmno0BjMLwsrDKZweT1twA8Vkmnby04cfmQ1GodJjgA8wnVBmEA9JSTBxmntqXGvbI7qf1tm4_-o1r9b5FrRadaloGmN35THp0lOvhIxOc5iVGZzsDPm3fkFNdA0oZg5DRHBGVea13XQ-EBdAD9RZcGE2YCBx0JC01qNq8gy2nBT2VxIZFr1lLLuNSSVX1zIWMALKNeBryHIWd5Cv0W_iZVcrHg7Rbx5I9yTq4TCbgY0p_CWBt12nxOwwH2ni71db4yFDMa2ncTo1Rg_JuTq78nK0IowDO9l5IqsYe-XFwqPOginociayA7glYLtLi_kH-_ryAJyOo4Rk-IHRwedD8OOfvhGaAv6OA3xqagD0i9umm7utx0cFVkzsKsDptxyiMQS3fKks3BTzjqsz2dCG1PfviFDkElHcznITeShO0p6S8CKcuaZrOrqR8tn_ENwkE8ahKyRhmkrGK6NuabRHltH42HTxkoP2_do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c6693569.mp4?token=jfq5zm-t_CTYKqY8et0kOfW4FJniM_mGT4ZNr5kTvZipAyYtjDZT3F2DbDm90c2IPmSQOgXZpdUpyiGbIFfVUh-CDn5yx7m3BRSRbI8OqzXStwB97oCLFyxVHa_gWoybH-u4UGn0S_DtmMzjuBBE-Xzo835dPl9saDVx8HV-XaSy4zn9u0UjRqy4lf74sjwuXMfQjgjfmno0BjMLwsrDKZweT1twA8Vkmnby04cfmQ1GodJjgA8wnVBmEA9JSTBxmntqXGvbI7qf1tm4_-o1r9b5FrRadaloGmN35THp0lOvhIxOc5iVGZzsDPm3fkFNdA0oZg5DRHBGVea13XQ-EBdAD9RZcGE2YCBx0JC01qNq8gy2nBT2VxIZFr1lLLuNSSVX1zIWMALKNeBryHIWd5Cv0W_iZVcrHg7Rbx5I9yTq4TCbgY0p_CWBt12nxOwwH2ni71db4yFDMa2ncTo1Rg_JuTq78nK0IowDO9l5IqsYe-XFwqPOginociayA7glYLtLi_kH-_ryAJyOo4Rk-IHRwedD8OOfvhGaAv6OA3xqagD0i9umm7utx0cFVkzsKsDptxyiMQS3fKks3BTzjqsz2dCG1PfviFDkElHcznITeShO0p6S8CKcuaZrOrqR8tn_ENwkE8ahKyRhmkrGK6NuabRHltH42HTxkoP2_do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔰
واکنش یک نماینده مجلس به ادعای ثابتی: به مردم مبعوث شده ظلم نکنیم/ در مذاکرات اسلام‌آباد حتی یک اپسیلون از خطوط قرمز عدول نشد
🔻
محسن فتحی عضو کمیسیون اجتماعی مجلس:
🔹
اگر فردی خود را ولایت‌مدار می‌داند باید به گونه‌ای رفتار کند که در ذهن مردم این تصور ایجاد نشود که میان مسئولان نظام درباره جنگ و مذاکره، دودستگی وجود دارد.
🔹
ما معتقد هستیم که رهبر معظم انقلاب آنقدر مسلط و مشرف به قضایا هستند که تصمیمات را به درستی می‌گیرند.
🔹
در اسلام‌آباد دیدیم که تیم مذاکره‌کننده ما به ریاست آقای دکتر قالیباف حتی یک اپسیلون از خطوط قرمز عدول نکردند.
🔹
کوچک‌ترین خدشه به انسجام ملی، ظلم در حق مردمی است که بیش از ۹۰ شب ایستادگی، پایمردی و تعهد خود را به نظام، انقلاب و رهبری نشان داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657292" target="_blank">📅 12:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657291">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29baaf2910.mp4?token=IUkOMNvcKncurPlC9AU-QtQSdvG-DLONl_fNiaNwc98UfA-JoC28Y8eF5KstrYGzBzci95Koz_DZHs58azmiNyal8Ze2a2GH93PnpiE7SxEH-hk_6-op0f0SaT5ED3M1O7VjGL1OP7jX8p9xE4VNI5YaI-8jNTLQNwwm0w4j9WqTzeopPfMXMAaNPC7sCAujeqx4cnhrzOb-_xt1Z4rXY9JktErziljmONyITaJVK1iOHN-IYxovP94fMZHX1qv0BueYrJfHo_LYkmTSvqEoA4CyYnDXOXsn-dnWUg79ah7ODUyIi_uJ-aRkH7XgEbALOIIpjKtkXiUC3FCKFj0C8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29baaf2910.mp4?token=IUkOMNvcKncurPlC9AU-QtQSdvG-DLONl_fNiaNwc98UfA-JoC28Y8eF5KstrYGzBzci95Koz_DZHs58azmiNyal8Ze2a2GH93PnpiE7SxEH-hk_6-op0f0SaT5ED3M1O7VjGL1OP7jX8p9xE4VNI5YaI-8jNTLQNwwm0w4j9WqTzeopPfMXMAaNPC7sCAujeqx4cnhrzOb-_xt1Z4rXY9JktErziljmONyITaJVK1iOHN-IYxovP94fMZHX1qv0BueYrJfHo_LYkmTSvqEoA4CyYnDXOXsn-dnWUg79ah7ODUyIi_uJ-aRkH7XgEbALOIIpjKtkXiUC3FCKFj0C8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر ادعایی فدراسیون وشوو از آثار حمله خواهران منصوریان به دفتر رئیس فدراسیون  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657291" target="_blank">📅 12:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657287">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDogSNYUZIxrSXzCdd8lPFDwMGmtp4SsgryIXncAODzrwPARHtdXg2mjwT8zLvzA2UrpOI4VGES83JnfdTZR6wxxEQHY2PuDW2AVLh2ZzgNEwsAZgbWQ1nF5-PWancZmDdKZvQFC9x_1QVMoP5Vnx9D9Yh-YnLk722PmceF4Q9NstDdJwhPanrSe7QtGf5LdsjQmEPiSf1rqO3zXBfCsA-FaitIpaMErL9GQldCRaIiKj79gIWpnpdef329GCQGiQVQLsZgICtNj8_kJdV1FjRjM-ISwxspO0KNJRHmOvWpR8hcB3woCgDG1tO53mhPXjQzhFI3EwkkRjGAyix3-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjXGmhDCK6jWwejOfpuZ4fHXTn4CdisK8by7CdYvoX3lCZcNcxejVIGtEFSNQs7BhHBkSDHi5bmtkoD7f18x7PnmDCyx7ZH_9AyRxnUbUGUmDg4INjj7jbzCcCKnlR8H-NbcurCcsDE0jTr_uMu868Zih-b1PVj0p2Vob43MNPueM6V0pZVyBFkO4aOMvwerKCWey5QJEpUbUsWiHZyT8mnpH_kwAO256d3GY2u8nYuK--1dh9SHagQo4qmZ27UjBLCIRkGeDYqBmqD6PhKBCDkGdH5MFEJIhAY2STAMPa8jIzwNCXOdA7XuPFLRw7SNj8FQ8EKyodUYZLPdP--j_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVOtzF91e22bv_PHzngwruARBZVNGVIIxy4IbPqPTMgfF1hpT74DhM1aa1wthiEOqvCU1RmcOhNtG4-g35Gngpc_P683P6q1rBUTSXaTNh7Gp8fUScdnDSX4XfLyqQBr5cP8e0KAHSHzDp_sb9dEuHf38rqcPbMrwNAXu-l63fpHgSfq_gkjiezFEBvSfMOkm7e0PSAfUz38_jcGrraifVIH-LZXxmoFtTN8kGmKwhqrey_SbiaJWWH5DmAYH4yhlT0FgpIjrDi-WY0btEtAfwCXD20A2TeO2T0670oPsjbjAInJbe88O7zO3Lel5UIHHjKxh4S2YztgpvXffb0hiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ld3CTuWJCoWTJHzFftLdO-TPho4b7Oz9bikIzIFmjGOexWQfT3BWpqer5uEv00Ow1YvuoOKg75ls2TTrwSJokCwOQ7xQFua-1s_QDSIBI0Ge73hso9g1r7mYNT3txfPZQhRyeJ3DsWOqwRJM8urQ0KZvnptK6A7KZ_yKugcID-TWh8W6x81p10Dnj9IJsy2VyI292MNg3qgi7x0iSPugPVJAFNUxR6HdQBlJAH0gUoAlyvCuIhP5_VY2PdqjzbKD3xy6Fc7mUY246_OUNhkJOTSGaNWqFuGrrlQSVCTAyN4P4ZtVctcOQIri56_MDB8rQoQ9QDAzj2K_hJ0zzziTiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ادعایی فدراسیون وشوو از آثار حمله خواهران منصوریان به دفتر رئیس فدراسیون
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657287" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657286">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
رکورد ارزش معاملات خرد بازار سرمایه شکسته شد
🔹
در حال حاضر ارزش معاملات خرد به بیش از 35 همت رسید که بالاترین رکورد ریالی ارزش معاملات خرد در تاریخ بورس است. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657286" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657285">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e68add6f.mov?token=XLQ6UiRlVATXUcTtwYl9VAZgjCJVQJGZZDet9wcAs5oibMGCsTvmaTAhy-BV1J38QatfOMeY_HGmMPfnXOr_A1UiK749LbwZvUPgcnfcjfPnvWbAUiI76ie53J66VIlAPhvj-TFkTo4bnD7kZEJsTUodsKdZ7CgTXHx_SAgf1UT25ouIwRPFq4jorYNKPD6MzXfe-EewRoq3D1DVQPNBwyxYru4mlB8uE8nn5U3LOPyg21vjW9itR391IILT5X1XKmLkovPLkpPFXE1_gG011czRWU3WQqcD0w_1prY9yq2mcyao46f9rzIWTlf2Uls-Sy-h22YsiR-oKxNFoUsFZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e68add6f.mov?token=XLQ6UiRlVATXUcTtwYl9VAZgjCJVQJGZZDet9wcAs5oibMGCsTvmaTAhy-BV1J38QatfOMeY_HGmMPfnXOr_A1UiK749LbwZvUPgcnfcjfPnvWbAUiI76ie53J66VIlAPhvj-TFkTo4bnD7kZEJsTUodsKdZ7CgTXHx_SAgf1UT25ouIwRPFq4jorYNKPD6MzXfe-EewRoq3D1DVQPNBwyxYru4mlB8uE8nn5U3LOPyg21vjW9itR391IILT5X1XKmLkovPLkpPFXE1_gG011czRWU3WQqcD0w_1prY9yq2mcyao46f9rzIWTlf2Uls-Sy-h22YsiR-oKxNFoUsFZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استفاده از پارکینگ‌های زیرسطحی برای پناهگاه
سخنگوی شهرداری تهران:
🔹
پارکینگ‌های زیرسطحی برای استفاده به عنوان پناهگاه آماده می‌شوند.
🔹
مجموعه اقداماتی برای ایجاد استانداردهای لازم در این زمینه در حال انجام است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657285" target="_blank">📅 12:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657284">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
فعالیت عادی شعب بانکی ادامه دارد
🔹
در صورت تغییر در ساعت کار بانک‌ها در روزهای آینده، شورای هماهنگی بانک‌ها اطلاع‌رسانی لازم را انجام خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/657284" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657283">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28106fa10c.mp4?token=hyG096VU_t3bt2wmXcXot7GvD-wCukz3HuMDjH9sTO_xYowlbiY79aXTMA45tkkfdPuyQbSuKt5gRCmiB0Mp8m4_ylAm1kAn8g2j2V7G-u4ALrMCpHoOOrNsZuBHUla0CM4GNyi56SpOa-hMLBYm2G--nDjWwsHls9Q9G5rXUMc1XFPS6183meCPqlM_7kw9GDs4TvOk07qZOF_jxAFjf7IW1hDwqNnLRaQZO7lnbHEEFoGkHgqOd2c8Z0FMaSjgx_hXQVcjMPuVkyipNv8KsTuIe9fMptFipjNXXIYeT8GzkRmuXOMh96eVhS-lHDwLsl7ewQAG1ihLiozTDXBgGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28106fa10c.mp4?token=hyG096VU_t3bt2wmXcXot7GvD-wCukz3HuMDjH9sTO_xYowlbiY79aXTMA45tkkfdPuyQbSuKt5gRCmiB0Mp8m4_ylAm1kAn8g2j2V7G-u4ALrMCpHoOOrNsZuBHUla0CM4GNyi56SpOa-hMLBYm2G--nDjWwsHls9Q9G5rXUMc1XFPS6183meCPqlM_7kw9GDs4TvOk07qZOF_jxAFjf7IW1hDwqNnLRaQZO7lnbHEEFoGkHgqOd2c8Z0FMaSjgx_hXQVcjMPuVkyipNv8KsTuIe9fMptFipjNXXIYeT8GzkRmuXOMh96eVhS-lHDwLsl7ewQAG1ihLiozTDXBgGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ زخمی براثر حمله مسلحانه در ایستگاه پن در نیویورک
🔹
براثر حمله مسلحانه یک فرد در ایستگاه راه آهن پن در نیویورک، ۶ نفر زخمی شدند.
🔹
فرد مسلح، دستگیر شده اما انگیزه او از این اقدام هنوز نامشخص است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/657283" target="_blank">📅 12:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657282">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
تهدید گروه مقاومت عراق به بازگشت به جنگ با اشغالگران
🔹
گردانهای سیدالشهداء عراق به رژیم صهیونیستی در خصوص عواقب حمله به جمهوری اسلامی ایران هشدار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/657282" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657281">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
حمله جدید یمن به سرزمین‌های اشغالی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/657281" target="_blank">📅 12:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657280">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpaTOqu8driS5N1JFKB1W_5bxDeCjU2rOzyGQ7d9DtOPZ3cREqeSqnRX3SFPF7DdCA2qPWxJAylcjmLLlIYfftJ1q5cFIsxeHYjtEOBOSUknoqGbRAr-_rOE9OLXF09C0zeXPnMEqn_LZrdykGB3u0PCZlXHY-Y2xcUyThyYm-2tQkyGg_SHjPX84peBkZJQYkvlJtoh9UyY4eYA8AKENH0NWDPi7rYNMJJVP-5hU1rDTW5YcS7jfNF-EYdUV2gWS3SqWdGOVVf8AIDKimhzqGF1NWCPZ7H8UR6p3BoIxlcDl4mPW_JWMB_w_-SEeJmFPP4uDxLFftrql9Q9vMw0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعات سپاه: اطلاعات میدانی از ضربات دیشب به سرزمین‌های اشغالی نشان دهنده موفقیت ۱۰۰ از ۱۰۰ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/657280" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657279">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
عکس‌گرفتن از محل‌های بمباران و انتشار آن، بی‌احتیاطی ساده نیست؛ کمک مستقیم به دشمن است
🔹
در چهارمین جنگ هم هنوز این رفتار خطرناک را ترک نکرده‌ایم: خودمان با دست خودمان کشورمان را بی‌دفاع، بی‌نظم و بی‌حفاظ نشان می‌دهیم.
🔹
هیچ کشور عاقلی در میانه جنگ، اطلاعات میدانی، حجم خسارت، موقعیت اصابت و نقاط ضعف خود را برای دشمن منتشر نمی‌کند.
🔹
دشمن فقط با موشک و پهپاد نمی‌جنگد؛ با عکس‌ها، ویدئوها و اطلاعاتی هم که ما بی‌محابا پخش می‌کنیم، هدف بعدی را دقیق‌تر می‌سازد.
🔹
لطفاً عکس نگیرید. منتشر نکنید. بازنشر نکنید.
🔹
در جنگ، سکوت میدانی بخشی از دفاع ملی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/657279" target="_blank">📅 12:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657278">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
کوثری: به احتمال زیاد تنگه باب المندب در مرحله بعد بسته می‌شود
اسماعیل کوثری، عضو کمیسیون امنیت مجلس در
#گفتگو
با خبرفوری:
🔹
دریای سرخ را فعلا انصار یمن اعلام رسمی کردد که به کنترل رسمی در آورده که اگر شناورهای رژیم اشغالگر بخواهد تردد داشته باشد، برخورد و کنترل می‌کند. در مرحله بعدی به احتمال زیاد بحث (بستن) باب المندب هم پیش می‌آید.
🔹
ما باید جواب باصلابتی را به رژیم اشغالگر قدس بدهیم تا بدانند که آتش بس را نمی‌توانند نقض کنند و یا خودشان تعریف  کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/657278" target="_blank">📅 12:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657277">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrEhuHDvDWMBY395x9z4-wpysy8zeTJLrPwhwJAnxUqeEpZfLgAK9XTR1Z2XFh6ywpmYWgFsItU1QZbZQ9-0Tv40fiF8MKYXUycwmYENa9pPAKjSfwxF0bovc5CmCJgrkdmNXo1D1l7C64TzsVaPuT0c3Xk2K59ONxN3JpMhxFa9K9IAdFYek7wEpkqKFxd9qN00JsVWUVn-YDa1eLeGKIVqHx70ymrogyZCMYpBBBK9d6e3jNjl7lI_8ybMlvmx0eVByuRgzSC_0bQhebydNUY22vxbTLxWoPcBkTambJ8GrD5Zr2bJ4UkH9bMD4qng1Ko644rSqMRVKWIqS21crQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاوره و تسهیل گری در فرایند اخذ وام های بانکی
نیاز به وام دارید اما در میان انبوه بخشنامه‌ها و فرآیندهای اداری سردرگم شده‌اید؟
کافی‌نت آراد با جواز کسب رسمی، اینجاست تا مسیر دریافت وام‌های معتبر بانکی را برایتان هموار کند.
✅
خدمات ما:
• انجام مراحل اداری و پرداخت وام در کمتر از ۷۲ ساعت
• مشاوره و بررسی شرایط شما برای انتخاب بهترین وام بانکی
• ثبت‌نام آنلاین دقیق و بدون نقص در طرح‌های تسهیلاتی
• آماده‌سازی و تنظیم مدارک مورد نیاز
• پیگیری روند درخواست تا دریافت پاسخ نهایی بانک
📎
برای شروع، پرسشنامه اولیه ما را از طریق لینک زیر تکمیل کنید تا کارشناسان در اسرع وقت با شما تماس بگیرند:
https://survey.porsline.ir/s/CwzLVsEN
https://survey.porsline.ir/s/CwzLVsEN
https://survey.porsline.ir/s/CwzLVsEN
کافی‌نت آراد؛ پیشگام در تسهیل امور بانکی شما
🏦</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/657277" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657276">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شهرداری تهران: با توجه به شرایط موجود در کشور، استفاده از مترو و اتوبوس در هماهنگی با شورای شهر تهران همچنان رایگان خواهد بود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/657276" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657275">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس اورژانس تهران: هیچ مصدومی تا به الان نداشتیم
محمد اسماعیل توکلی، رییس اورژانس استان تهران در
#گفتگو
با خبرفوری:
🔹
در پی حملات اخیر، الحمدلله تا به الان هیچ مصدومی در استان تهران نداشتیم.
🔹
همین الان دو حادثه انفجار داریم که درحال بررسی هستیم که اگر موردی باشد به رسانه‌ها اعلام می‌کنیم.
🔹
حجم تماس‌ها با اورژانس به نسبت روزهای عادی افزایشی نداشته و کل ظرفیت ناوگان به همراه بخش خصوصی در کنار مردم برای خدمت هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/657275" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657274">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
لغو تمامی پروازهای فرودگاه شیراز تا ساعت ۲۰ امشب
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/657274" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
