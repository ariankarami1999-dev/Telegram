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
<img src="https://cdn4.telesco.pe/file/JU1Rh3F2X2MJrCeDA7Hl2JpDAQEHNEkMQs0jYt8MhliAx952WwTGeGPPABVeNUNQG0OJKwJX6U9OMrcrA9ATOqrN-O3NjigxNtVGVxFHEiSnzw9JhR_bYaHC30hfxxl4e_X5ngPZoktHUpGm_NmmOTsHu0OGiMSDqQupQETyjgD2QbSm4SyTngD_dAA20AcOjr1CKSHUK6ShTGwQfRKqJ_Ii088em9ykN27bWe1SN-KnBjVb80gqyYlhphfJW6c1OMleRAgDkb8uY1hTq1KoB5cQJ3CTZfK5I-AGqBEj3c3Wl14zJFkyYZSnBUC9UL2P_8JeY6t6oOEWrWRxg-RtCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.95K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 07:35:57</div>
<hr>

<div class="tg-post" id="msg-16962">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خواننده Secret Box از یک سال پیش آگاه بود که دلیل زدن هوانیروز و پایگاه ها و پاسگاه های مرزی ارتش و سپاه در مرزهای غربی، گشودن فضا برای ورود نیروهای مسلح کرد به داخل کشور بود.  اما چرا این طرح آن گونه که باید و شاید عملیاتی نشد؟!  بخوانید:   موساد سلاح‌های…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16962" target="_blank">📅 00:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16961">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بشدت به همین سناریو که 2 ساعت پس از آغاز جنگ اشاره کردم، ایمان آورده ام. تقریباً تردیدی برایم نمانده که مدل «فروغ جاویدان» صدام را این بار نتانیاهو با پژاک و گروههای مشابه ش میخواهد اجرا کند.  نکته بدتر اینکه در صورت موفقیت این طرح و با ورود نیروهای شبه نظامی…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16961" target="_blank">📅 00:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16960">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">محسن رضایی:
امیر قطر و ولیعهد عربستان دارند خودشان را با واقعیات تنظیم می‌کنند اما امارات، بحرین و کویت همچنان فکر می‌کنند قدرت آمریکا مثل قبل خواهد بود. این‌ها فکر نکنند که اگر این روش را ادامه دهند ما بعد از جنگ رهایشان خواهیم کرد. اگر امارات و کویت با صهیونیست‌ها همراه هستند باید ابوظبی و بوبیان را به عربستان و عراق بدهند!</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16960" target="_blank">📅 00:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gan3VtiHGnfGM2yjyR_AvHqSXVdL-uhgV8E1NaO23doysYwEbPpofr-PCeaBD-PHywrSHWW2U--bcmKYDNpuNHlGqtq8jovCAPN5jCPuhSBfeQRLpWaVOsVrZ_6eNK36HFgkP_k6u4vs88a6e78NOY7ogrd9ansgukcHrRPDJ8FheSAdOVGt6ME3J4OzaBoPr3UMnVcI6f8MAx4M6eoGmYMNNLKLLmlbp57v2_5xXHjpLCenW-a3kmtrqtDxAJUAUqQJ-Zm9QBQRxHtQtjGnXGicFgGTJRga-5oHsu-ed42AT9l0I5lPHouRTYYI_9MBrjBtsNIlrucmgUArGw0I5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/16959" target="_blank">📅 21:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16958">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ایران و روسیه یک تفاهم‌نامه همکاری به ارزش ۲۵ میلیارد دلار در بخش هسته‌ای امضا کردند - تسنیم نیوز</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/16958" target="_blank">📅 20:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16957">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز:   روسیه برای اولین بار اذعان کرد که تولید نفت این کشور در سال جاری کاهش یافته    این اعتراف در زمانی مطرح می‌شود که اوکراین در ماه‌های اخیر حملات پهپادی و موشکی خود را به تأسیسات انرژی روسیه تشدید کرده . آژانس بین‌المللی انرژی تخمین زده که تولید نفت…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/16957" target="_blank">📅 20:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16956">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/16956" target="_blank">📅 20:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16955">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dy1RALgHzh0gyfNx5Ddk77NDl9CKNtTSjMyb2lq9Sl_dQFlZp0LawmMHpvR3aMEB3gg2UyVyGwTQOmgte7liT6-Bpt63jOgTyhzsleyRrZ7p3p_u4XT1H8Zta5pXN9l0XTIWDCYZw2l081h6oWYNGEpLb1g3DOIyhnGgCNJUfNr7OQxTyD24QkRbkrTsAg6AEkNpY_AyqSEN0oH-eEmlgarFZWSrFnAeJ6Wx4gjYVGXU_ct6FzjjmUaKZNV8pbP4gypmKL5IbqsDaL0ZEWWFaYIsa6LqeKjjOh5YSsm1J5fuSk6tqvkNKzB-BVNE7yKK4nmpy8o5Qw2iN3D4eQ-o4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:   در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/16955" target="_blank">📅 19:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16954">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حالا اینجا همه حضرات میگفتند ترامپ دست خالی از چین برگشت!</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/16954" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16953">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔥
ثمره دیدار ترامپ و شی/ سپر چینی جلوی جهش قیمت نفت را گرفت
🔹
فایننشال تایمز نوشت که کاهش ۴ الی ۶ میلیون بشکه‌ای واردات نفت چین و استفاده این کشور از ذخایر نفت خود، منجر به کاهش تقاضا در بازار نفت و کاهش قیمت شده.
🔹
خاویر بلاس خبرنگار بلومبرگ می‌نویسد که…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/16953" target="_blank">📅 18:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16952">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJEFmbAN4sya6clSGhtCkBdAq8gY7DafSzDmulnpTr2UCqfcmzdDcu8mRMEYcR6tOQochC1KBfxjw2W5AMcfKP0wGJTUGcLXFoVRt9ZGZrs48I2s59FgreKhRPWvYj8MsmDhReOtq9B8MWs_d811TEcKUdqHILSh75LOe09cJ37WSZZyNTqcp-MVEZ_xTWufyCP-4_sQuGEP8vaLxSq6rdns9VgubcnuZAWD3WQhguOLz6HWdp-LiGaHRFkOX6ApKEbzqSusi9OzUWcwMGd59fqtm-GV43PKWxZIpCX4kWrdwn6YP9myhy2viStn-EXyoDQNbd3UXkPKHaS4h61HnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ثمره دیدار ترامپ و شی/ سپر چینی جلوی جهش قیمت نفت را گرفت
🔹
فایننشال تایمز نوشت که کاهش ۴ الی ۶ میلیون بشکه‌ای واردات نفت چین و استفاده این کشور از ذخایر نفت خود، منجر به کاهش تقاضا در بازار نفت و کاهش قیمت شده.
🔹
خاویر بلاس خبرنگار بلومبرگ می‌نویسد که اگر چین واردات نفت را کاهش نمی‌داد:
۱- قیمت نفت خیلی خیلی بالای ۱۰۰ دلار می‌رفت.
۲- فدرال رزرو مجبور به افزایش نرخ بهره می‌شد و وال استریت کاملاً نابود می‌شد.
۳- رئیس‌جمهور ترامپ در مذاکرات با ایران کاملاً تحت فشار زمان قرار می‌گرفت.
🔹
به گزارش خط انرژی، برنامه دولت پزشکیان برای توسعه روابط با چین چیست؟
@khate_energy</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/16952" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JABy4_KNpXlLoolNzJdVJAX-3-R9tp8VSHLjTNjbAMLn8LuJmfFz_JlWILhVpAR0Hiu5jwA7bG1bpZ28XjLJJvvSQhXFNq8ngyw4zbXsUvhgrVh3-ex3kKjlsl6KCViTyCKAg3r36ljA6zHg8ToEveQ7r_ZRVRoXC06byI6mWdBt3ClVWKrguO2nDrmWWvEI3rJ3vQQImB9VeuYtrvn0kBXfJZqr4QGHYPcgNmwlSNJ56YFGkd9XQnJ9Y-l7XQsuda-LPTvYGL7oifg4OztrmcVIxCFUQ4cbqNqaLFuFUh6XWG6wJ3-qi1OdX1N9-hjZ7G-sGOIzWBuTtdS2Po_xTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/16951" target="_blank">📅 17:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی (IAEA) اعلام کرد که نتوانسته به تأسیسات هسته‌ای ایران (به جز بوشهر) برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی پیدا کند.
این موضوع نگرانی‌ها درباره خطرات اشاعه هسته‌ای را افزایش داده است.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/16950" target="_blank">📅 17:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سپاه پاسداران:
شرط اولیه ما برای پذیرش آتش بس در جنگ منطقه‌ای، آتش بس در تمامی جبهه‌ها از جمله لبنان بوده است.
دشمن می‌بایست با فوریت حملات خود به مردم لبنان را متوقف کند، و سریعاً با تخلیه سرزمین‌های اشغال شده لبنان به پشت مرزهای بین المللی عقب نشینی نماید و تمامیت ارضی لبنان را به رسمیت بشناسد.
هیچ آرامشی در منطقه بدون عقب‌نشینی صهیونیست‌ها از مناطق اشغالی لبنان برقرار نخواهد شد
همه ما با تمام وجود از ملت لبنان حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/16949" target="_blank">📅 17:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7xDAY6wACzzZR8LfNkozwcgiH9SFhEQc-mQe0oL9_fXD--oLBjv4Ni3YyzZxx0HxptffxpViGWw1ZJXEj-604J158PWHOHgdCzOUotAUJGYnM2xjy3oVvnzrGqWGjFBIPaTRn1Eu8by-hOzTSOcsd6k1kgen8yKwYr9fGoKZIHVZZjHVYfW4u87d8LX9jZwpu-HxKCNGHpbJAJYC-w3eLv3B8YX0z7UrWwJbQL2yBclg6bYtOxi0pKwekn8PkOEasRdq_zQCteBpttCT0U6LMhyEfOyrx-QDqRG8UU3nQ-uVbG110UGcBxP7oA2n-EnLP-yNd3npPd8zvWIfeVw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
تصویر روی جلد این هفته: «نسل جدیدی از سوسیالیست‌ها قصد دارند اقتصاد را با کنترل قیمت‌ها، مالیات‌های سنگین بر ثروت و موجی از ملی‌سازی‌ها دگرگون کنند.
این جریان که با خشم ناشی از غزه تقویت شده، با سرعتی چشمگیر در حال جذب رأی‌دهندگان است.»</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/16948" target="_blank">📅 16:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce28a3a45.mp4?token=qI1cmvzpjkeSfggs-ktxMC8wu7fcuWCGcTU49wcS4BMydqyIPl89U6fcJ8lkscSi5Rpc_5CRcTK2gLpjT9IwfeOSbpSEgqbJbe6P3FhoqWiisaosOOMOWcOAdG91iua5Ph_DxA9I9y_vDoTZvQZl-CdDFNC5F4kol8iLIztBx5NcnjsxJfpaxNkVfi1fSzIBNqFoqm3qp2rjwZHcIWBghgugMkzanXBTOOerv4EU1fs3ZrgAj0GdrwsKN-8TRWmnBgWHJJyBZI7Xiu9EMtuPkxdN0fi54sLkPZX65rk-hlldP4Go4dXksOEgfWAbe0uXvIB6ni1iNGWCA7kSdp8i1bY9wi88sYvq1C_0-MKAuBnDMII_AvTTUgjrUNXqNxwQ7ptjlcp2KIIINkdpBu2OJ1RggdYlpAGBV0bH-ViQrO2QViSoi-aOJyF-j5-MEnXBnmqCiga8H-f2Bj9g_jTITsj1BIuiHnzODa0UzqvDw56yjgsk96NsgRbDnAuV5kRAv8Acnbx3cBj6c1Kc4ig8DYxWW68YGWZCiT7S25gtjtk8jjRFGU9e6RhCUZoJpcSzHv7jO--M9INbFT1JqLN_XM6XB-PeM13imuauskJgEleSfhVj1EYjmc7lmAmjqQ_pOgu3w19i4Fp0TzdpxfLgJuB5LPSlzz9LxnWqzzFdxaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce28a3a45.mp4?token=qI1cmvzpjkeSfggs-ktxMC8wu7fcuWCGcTU49wcS4BMydqyIPl89U6fcJ8lkscSi5Rpc_5CRcTK2gLpjT9IwfeOSbpSEgqbJbe6P3FhoqWiisaosOOMOWcOAdG91iua5Ph_DxA9I9y_vDoTZvQZl-CdDFNC5F4kol8iLIztBx5NcnjsxJfpaxNkVfi1fSzIBNqFoqm3qp2rjwZHcIWBghgugMkzanXBTOOerv4EU1fs3ZrgAj0GdrwsKN-8TRWmnBgWHJJyBZI7Xiu9EMtuPkxdN0fi54sLkPZX65rk-hlldP4Go4dXksOEgfWAbe0uXvIB6ni1iNGWCA7kSdp8i1bY9wi88sYvq1C_0-MKAuBnDMII_AvTTUgjrUNXqNxwQ7ptjlcp2KIIINkdpBu2OJ1RggdYlpAGBV0bH-ViQrO2QViSoi-aOJyF-j5-MEnXBnmqCiga8H-f2Bj9g_jTITsj1BIuiHnzODa0UzqvDw56yjgsk96NsgRbDnAuV5kRAv8Acnbx3cBj6c1Kc4ig8DYxWW68YGWZCiT7S25gtjtk8jjRFGU9e6RhCUZoJpcSzHv7jO--M9INbFT1JqLN_XM6XB-PeM13imuauskJgEleSfhVj1EYjmc7lmAmjqQ_pOgu3w19i4Fp0TzdpxfLgJuB5LPSlzz9LxnWqzzFdxaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗
رهبر حزب‌الله نتیجه مذاکرات مستقیم لبنان-اسرائیل را رد کرد!</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/16947" target="_blank">📅 15:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انصافاً ترامپ خدایگان دروغ، دغل بازی، فریب و سخنوری است.
زاده خرداد است و ...
(امیررضا هم زاده خرداد است و میدانم این یعنی چه)
سبحان الله!</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/16946" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16945">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA1_ZBxmNqgqHv6x7b2wPbdSCJYqqXvjy1IjifdjzkAyj-K0YnXkOsjFlV01kuoRIuBW6Qaa47SFJNBZsuMlmF7XjM-_4HxiCmz4ZvCfWg-1MCFe4nPya6w87z5GKgZnSPBwyC9Kf_LRgJ7x9o7FTOzxPcU1hMsFMk9_lOtXeeVpKCtPBCNcLDFT_oLevtCkemOVwvAuD4tF0T5jIcccLP5KamNyiir4fx1UO4sJYj-uS56BHGnlL6OCNuQnjK1997sELGrds5ojVcItbnQbYbRIa1vO4-gu1KHsYurRQRgy_-pioaJRPwFaus852URKVGmlh99SZrwr_gWWEs_ZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/16945" target="_blank">📅 15:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗
رهبر حزب‌الله نتیجه مذاکرات مستقیم لبنان-اسرائیل را رد کرد!</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/16944" target="_blank">📅 15:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16943">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp4Ud31n7oKvydd84g5ur8xhxGsC0d12nxKMG8-17tt2Ggb-MLqbCfMujdPIuoLFuhdT4HXU0Wrl24GNuLqUPionzhUAwd3IuluudVAnwXjnwaqG0fKlC8uSgPqvGx7Bs5l0pCtQii8x8dl7zYUx52rfWWSxAE3WOi_XRPqQDYu2sAR8eQ45XPOBhJNFhetldN6u1LRp-8VVqwssx1mq6G--c65bo5sHBCNeqLxvN3hVsx9XDbXCDvsNLZS9z8OmxCQ9qJjjAITX_U97LnO0FqQoANy0S2TLLKHU0OYL867E7zyRYQi-PPwc2rSOqm6rAAvYv67UoiN-rBkr4Q-48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی حصرشکن | حصر ترامپ رو بشکن!</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/16943" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16942">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">از منظر حقوق بین‌الملل، «محاصره دریایی» یکی از شدیدترین اشکال اعمال زور میان دولت‌ها محسوب می‌شود و در صورت اجرا علیه یک کشور مستقل، به‌طور معمول در زمره اقدامات خصمانه با ماهیت نظامی قرار می‌گیرد.
بر اساس منشور ملل متحد، اصل بنیادین در روابط بین‌الملل منع توسل به زور است (ماده 2 بند 4). تنها دو استثنا برای استفاده مشروع از زور وجود دارد: دفاع مشروع در برابر حمله مسلحانه (ماده 51) و اقدام جمعی تحت مجوز شورای امنیت. بنابراین، اگر ایالات متحده یا هر دولت دیگری اقدام به محاصره دریایی بنادر ایران کند، این اقدام از منظر حقوقی صرفاً یک «اقدام اقتصادی یا فشار سیاسی» تلقی نمی‌شود، بلکه به‌طور مستقیم در چارچوب «استفاده از زور مسلحانه» قرار می‌گیرد.
در حقوق بشردوستانه بین‌المللی، به‌ویژه بر اساس قواعد عرفی و راهنمای سان‌رمـو درباره حقوق جنگ دریایی، محاصره زمانی مشروع تلقی می‌شود که در بستر یک مخاصمه مسلحانه موجود انجام شده باشد، اعلام و اطلاع‌رسانی شده باشد، و به‌صورت مؤثر اجرا گردد. به بیان دیگر، محاصره دریایی ذاتاً یک ابزار جنگی است، نه ابزار صلح.
از این رو، اگر چنین اقدامی علیه ایران در شرایط غیرمجاز حقوقی (بدون مجوز شورای امنیت یا بدون وقوع حمله مسلحانه قبلی) انجام شود، می‌تواند به‌عنوان «اقدام متخاصمانه شدید» (hostile act) تلقی شود که ظرفیت ایجاد «وضعیت مخاصمه مسلحانه بین‌المللی» را دارد. در حقوق بین‌الملل معاصر، حتی بدون اعلان رسمی جنگ، وقوع چنین سطحی از درگیری کافی است تا قواعد جنگی فعال شوند.
در نتیجه، محاصره دریایی یک کشور نه صرفاً یک ابزار فشار، بلکه از نظر حقوقی یک اقدام با ماهیت جنگی است که می‌تواند به تشدید فوری تنش و ورود طرفین به درگیری مسلحانه منجر شود، مگر آنکه تحت چارچوب‌های محدود و مشروع بین‌المللی انجام شده باشد.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/16942" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16941">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عجب فریبی و عجب تاثیری در کاهش بهای نفت!</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/16941" target="_blank">📅 15:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16940">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1PD4jtyT1xjWQmw7xFzKnhfK8HhMkpSjJ2PFuT8Zgin9tTQOnVExbHwqUk817j-ipAOBWmcJJ83AnOl3KFcxYelRYtBytRT-RJ38wLajb8HTY8Im2WrGDZWpwfzCXX2LAJI8wdZ2qEpwiV6p4j8_YQ_hV5Ec4PQfGW-c9WINf5eEKuFj10Np6D4znsi2GbWCNri0gHTn8iSO2dZpVLmuS5a3yONlvktG41K6rCNJxXiNxa_7Y-THVhPYkFDhP3axR1K4D4zjS7Nzq1DkHZ8M5Kh6wUV2wg9Ddt2cEgABLhTeTo3URFRJTjdyx-zddO9Dx7IoPCJEzCzcqpPnD0u8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا رفت برای این سناریو که عصر گفتیم…؟!</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/16940" target="_blank">📅 15:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16939">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ به دستیارانش گفته است که جنگ با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند.  — وال استریت ژورنال</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/16939" target="_blank">📅 15:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16938">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کاندولیزا رایس — وزیر امور خارجه پیشین آمریکا :
«جنگ علیه ایران جنگی محدود بوده و نتیجه آن احتمالاً قطعی نخواهد بود، اما برای ایجاد خاورمیانه‌ای بسیار بهتر کافی بوده است.»</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/16938" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
بازداشت جمشید قمی، مدیرعامل ۶۳ ساله شرکت ایران تِک ، به اتهام تأمین تجهیزات آمریکایی برای تأسیسات هسته‌ای و نظامی ایران</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/16937" target="_blank">📅 11:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ به دستیارانش گفته است که جنگ با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/16936" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گفت که فشار شدیدی به ایران وارد شده و مذاکرات با ایران به خوبی پیش می‌رود. او احتمال توافق تا پایان هفته را مطرح کرد، هرچند اشاره کرد که ممکن است دو تا سه هفته دیگر نیز طول بکشد.
به گزارش فارس به نقل از یکی از اعضای تیم مذاکره‌کننده تهران، گفتگوها بین ایران و آمریکا همچنان ادامه دارد و هنوز تصمیم نهایی گرفته نشده است.
یکی از اعضای تیم رسانه‌ای هیئت مذاکره‌کننده ایران، طرحی چهار مرحله‌ای برای توافق با آمریکا ارائه کرد: ۱) پایان جنگ، ۲) اقدامات عملی در مورد تنگه، ۳) تحریم‌ها و مسائل هسته‌ای، ۴) تشکیل کمیته نظارت</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16935" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1ZoraqiAf7aMK6f-w_1KGjygCEZw0-gK5qm11k3RnVjO5310eKdJ5t3pT1BJQj_Cl-1cAlZI13sHq1U5oc2-3Je2nnimhwbcQIIq1_xZqEgltLijdtQ7dmZ38v7EqlbggrusbHQfuIbwfwxad6Uv5GjNSonqf01ZqQNc5iYDg1OApvJoume50K_12Nnoplwwl_6FPl7v_s8ucWPgTHzBCeBxHZXEoeLYUUIzYBWvD4jSz9P7G4zMWorhwLOVQrPedNWcp6MNB9nFn1k_2zsoIUxw3EQsyChef0g-kmiKhK54FaTafDjbbXzFpeEcZC2OdQT5C3Wd1Wk6v9MW15hcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی ایران برای رساندن نفت به بازارهای جهانی به شدت کاهش یافته است.
پیش از این تحولات، ایران روزانه حدود ۲ میلیون بشکه نفت خام، میعانات و فرآورده‌های نفتی صادر می‌کرد. اما اکنون نشانه‌های روشنی از افت صادرات و تولید مشاهده می‌شود. بر اساس آمار اوپک، تولید نفت خام ایران در آوریل ۲۰۲۶ به حدود ۲.۸۵ میلیون بشکه در روز رسیده که نسبت به سطح پیش از بحران حدود ۳۵۰ هزار بشکه در روز کاهش نشان می‌دهد. برخی برآوردها حتی افتی نزدیک به ۴۰۰ هزار بشکه در روز را گزارش کرده‌اند.
در بخش صادرات، کاهش شدیدتر است. Kpler برآورد می‌کند که بارگیری نفت در پایانه‌های صادراتی ایران به حدود ۶۴۰ هزار بشکه در روز سقوط کرده است. نشریه تخصصی MEES نیز گزارش می‌دهد که این رقم از ۱.۶۴ میلیون بشکه در روز در ماه مارس به کمتر از ۵۰۰ هزار بشکه در روز در ماه مه کاهش یافته است. همچنین از ۶ مه به بعد برای مدتی هیچ محموله‌ای از پایانه اصلی صادرات نفت ایران در جزیره خارک ثبت نشد.
با این حال، صادرات نفت ایران هنوز به طور کامل متوقف نشده است. چین همچنان روزانه بیش از یک میلیون بشکه نفت ایران دریافت می‌کند، اما بخش عمده این نفت از ذخایر شناور انباشته‌شده در آب‌های آسیا تأمین می‌شود، نه از محموله‌های تازه صادرشده از ایران. این ذخایر نیز به سرعت در حال کاهش هستند. برآورد Kpler نشان می‌دهد که حجم ذخایر شناور ایران از آغاز بحران ۳۳ میلیون بشکه کاهش یافته و به حدود ۸۹ میلیون بشکه رسیده است.
در نتیجه، مسئله اصلی دیگر صرفاً کاهش صادرات روزانه نیست، بلکه سرعت تخلیه ذخایر شناور ایران است. اگر روند فعلی ادامه یابد، تحلیلگران Kpler هشدار می‌دهند که طی ۶۰ تا ۷۰ روز آینده بخش عمده نفت در دسترس برای تحویل به چین مصرف خواهد شد و ایران ممکن است ناچار شود تولید خود را تا حدود ۱.۷ میلیون بشکه در روز، نزدیک به سطح مصرف داخلی، کاهش دهد.
چنین سناریویی می‌تواند درآمدهای نفتی کشور را به پایین‌ترین سطوح سال‌های اخیر برساند و فشار اقتصادی قابل توجهی بر ایران وارد کند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/16934" target="_blank">📅 01:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:
در توافق پیش‌رو، به ایران اجازه دستیابی به سلاح هسته‌ای داده نخواهد شد و پس از امضای این توافق، تنگه هرمز به سرعت بازگشایی می‌شود.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16933" target="_blank">📅 00:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
دونالد ترامپ
:
در اون منطقه از دنیا ( خاورمیانه ) ،  آتش‌بس یعنی وقتی طرفین دارند با شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنند
﻿</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/16932" target="_blank">📅 00:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیروی دریایی ارتش، "مرکز فرماندهی و کنترل" شرارت های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
در پی شرارت ها علیه شناورهای تجاری ایرانی در دریای عمان و نقض مقررات تنگه هرمز از سوی ارتش متجاوز آمریکا، نیروی دریایی ارتش، مرکز "فرماندهی و کنترل " این شرارت…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16931" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبر کوتاه بود و دلخراش: محمدرضا شهبازی مورد تجاوز قرار گرفت
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16930" target="_blank">📅 22:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">صدای انفجار در بحرین</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16929" target="_blank">📅 22:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به نظرم دسته خوبه را داده اند به سپاه که هر وقت میزند واقعاً بازارها به هم میریزند و دسته خرابه هم به ارتش داده اند برای وقتی که نفت را Short می کنند.
(باز بپرسید شورت چیست)</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16928" target="_blank">📅 22:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16927">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نمیدانم این حمله های ما چطوری است که تا خبرش بیرون می آید نفت میریزد و طلا بالا می رود!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/16927" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16926">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیروی دریایی ارتش، "مرکز فرماندهی و کنترل" شرارت های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
در پی شرارت ها علیه شناورهای تجاری ایرانی در دریای عمان و نقض مقررات تنگه هرمز از سوی ارتش متجاوز آمریکا، نیروی دریایی ارتش، مرکز "فرماندهی و کنترل " این شرارت…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16926" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اطلاعیه نیروی دریایی ارتش: ساعاتی قبل مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا در یک ناوشکن آمریکایی در دریای عمان هدف قرار گرفت</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16925" target="_blank">📅 22:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16924">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اطلاعیه نیروی دریایی ارتش:
ساعاتی قبل مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا در یک ناوشکن آمریکایی در دریای عمان هدف قرار گرفت</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/16924" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16923">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عراقچی:   آنچه در ۲ روز گذشته حمله به بیروت را متوقف کرد، در درجه اول قدرت مقاومت لبنان و توان نیروهای مسلح ایران بود  وقتی کار به جایی رسید که نیروهای رژیم صهیونیستی می‌خواستند به ضاحیه جنوبی بیروت حمله کنند، موضع قاطعی گرفتیم و نیروهای مسلح ما آماده پاسخ…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/16923" target="_blank">📅 22:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16922">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عراقچی: من مطمئنم که مسئله سفیر ما در بیروت حل خواهد شد، ما به حکمت دوستان و مسئولان دولت لبنان اعتماد داریم</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16922" target="_blank">📅 22:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16921">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر خارجه ایران: تماس‌های ما با آمریکا قطع نشده است، اما در مذاکرات پیشرفتی حاصل نشده است - المیادین.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/16921" target="_blank">📅 22:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16920">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر خارجه ایران: تماس‌های ما با آمریکا قطع نشده است، اما در مذاکرات پیشرفتی حاصل نشده است - المیادین.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/16920" target="_blank">📅 22:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16919">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTDCeBSH2IWR_wdNL9Buo_Ex0pm1cSbNwW-aSkfSeaGyRmxPTaMYZ-z6_OBc0fRm-nivSWLGfWL-x22iGsbc84Aou2mjmdGU7xwYX37yHfFubsl4BrFKQp3Wht3n1xn2elVtY_BCxJPpTkkCPEsqyx1OrXb_heERL5NSDh5KF3Iwmjqd1SYpH3j5dJYXyCq4ell8GvdgTKYFGOGtLuaCmWQryMxgv-ii65VBxmNp-XBQJGi-5VxRWF-khp0JuA0SL6E558n9YTc-WfVgDH9t4nm09XepyHacS5T7o5y_k-x5Ea_XcbujG-EjoNRRcwxdTGJr7FUgCTMBwo48lTiVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم تخریب پایگاه «علی السالم» آمریکایی ها در کویت
تصویر سمت راست مربوط به آشیانه ها و تصویر سمت چپ مربوط به انبارهای سوخت</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/16919" target="_blank">📅 19:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16918">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روبیو:
به عنوان بخشی از سیاست خارجی ما و به دلایل متعدد، ما به صورت علنی درباره اینکه آیا اسرائیل سلاح‌های هسته‌ای در اختیار دارد یا خیر، بحث نمی‌کنیم.
ما پاسخ بهتری به کنگره درباره اینکه آیا اسرائیل سلاح‌های هسته‌ای در اختیار دارد یا خیر، ارائه خواهیم داد، مشروط بر اینکه آن‌ها درخواست پاسخ به صورت محرمانه را مطرح کنند.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/16918" target="_blank">📅 18:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16917">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/16917" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16916">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2b300c77.mp4?token=o_VYydLITQ9aMWNQ0_6qMYgKdA1vsZRYiIv_SMGUEXBX94KJUf_30R3MKW5lOyvsWGzP1YTk8FH3IZTKl8pDzAObf8bxjBgXgIAFlSFkjElmhv1dbIwzZEpQ4fpT7-v_XKYm4KGNyZ9wCp7EYWG_YCJhgsbP52BpJ2cCkagh6-7UL23ijR0v2Ec9c8o4S9YuL2BX2N1GIZwgGr8Rzh9rjT91RSXNVjSsMn9wyhos6aBnvIAjGSxlUHpHSiUKQeNx39xHQGffQneT_wxvkyB2O34wK1rKHM2pwy0g3IEsj_sZ4dz_oy1R4sYkZLwM-5YLfk3VzJOWLa8J-PlMdmNKMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2b300c77.mp4?token=o_VYydLITQ9aMWNQ0_6qMYgKdA1vsZRYiIv_SMGUEXBX94KJUf_30R3MKW5lOyvsWGzP1YTk8FH3IZTKl8pDzAObf8bxjBgXgIAFlSFkjElmhv1dbIwzZEpQ4fpT7-v_XKYm4KGNyZ9wCp7EYWG_YCJhgsbP52BpJ2cCkagh6-7UL23ijR0v2Ec9c8o4S9YuL2BX2N1GIZwgGr8Rzh9rjT91RSXNVjSsMn9wyhos6aBnvIAjGSxlUHpHSiUKQeNx39xHQGffQneT_wxvkyB2O34wK1rKHM2pwy0g3IEsj_sZ4dz_oy1R4sYkZLwM-5YLfk3VzJOWLa8J-PlMdmNKMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رومن گافمن: از زخمی ۷ اکتبر تا رئیس موساد  سرلشکر رومن گافمن، مدیر تازه منصوب شده موساد اسرائیل (که در ژوئن ۲۰۲۶ سوگند یاد کرد)، به عنوان یکی از ارشدترین افسرانی ظاهر شد که به طور فعال با نیرو‌های حماس در حملات ۷ اکتبر ۲۰۲۳ درگیر شد.   گافمن که در آن زمان…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16916" target="_blank">📅 17:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16915">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رییس جدید موساد!  رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.   گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16915" target="_blank">📅 17:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16914">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بلومبرگ :
مقامات غربی می‌گویند خطر تداوم  مخفیانه ساخت سلاح‌های هسته‌ای توسط ایران اکنون بالاتر از آن چیزی است که قبل از حملات نظامی ایالات متحده و اسرائیل در ژوئن ۲۰۲۵ بود.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/16914" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16913">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شاید باورتان نشود ولی حمله دیشب ما به کویت یک کشته داشته که آن هم ….   …یک کارگر هندی بوده!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16913" target="_blank">📅 16:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16912">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.  خب اینها می‌شود تفاوت‌های حملات ما.  اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/16912" target="_blank">📅 16:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16911">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رئیس‌جمهور لبنان حملات ایران به کویت و بحرین را محکوم کرد</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16911" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16910">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئیس‌جمهور لبنان حملات ایران به کویت و بحرین را محکوم کرد</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16910" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16909">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCfoMHZ70wmV_NSNS1MkmPJqRVjRU1lE7U4TJnaHRX3vzDbwE0I9e2ZP0qdTAt6uru-qcYpBNCQ6ONVfLQ6jS7fnto5agnIFirP5loEO5DpEYLYqQECCbtXEK2M6GkCkw8zgQb2lD4I4xTGr7UDFRyqdvTy5eOi32cpGm5Hib35jZMyom8PbpVkRaNpuIA36HnVspbIo6AorLZVLQTV3cmN3UcAzB8MDYwxFXaia_UrQROBzwYkWfnWHmgoEIMaRGu9ZIBhlYnaIFP-w44LClsDQSeFRZKMrUW614FTvMB4VNRRW5eG6YMEy6MzqQPUukf-67O2nhZmus1xXtq2EyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه «مختار-007» ولی گفت که به شرط آتش بس در لبنان حاضر است سلاح های خود را تحویل دهد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16909" target="_blank">📅 15:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16908">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/16908" target="_blank">📅 14:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16907">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایران ۶ موشک بالستیک به پایگاه آمریکایی در کویت شلیک کرد  سپاه پاسداران انقلاب اسلامی حداقل ۶ موشک به پایگاه هوایی علی السالم، محل استقرار نیروهای آمریکایی، شلیک کرد. تصاویر، صداهای انفجار و تلاش‌های رهگیری بر فراز کویت را نشان می‌دهد.  رسانه‌های ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16907" target="_blank">📅 14:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16906">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">در این پست و پستهای ریپلای شده اش گفته شد که هدف اصلی ترامپ «تحقیر» شدید جمهوری اسلامی است و این مسخره بازی امروزش هم که میخواهم رهبر ایران را ببینم و اینها هم در همان راستا است.  عجیب است که ولی عده ای مونگول کماکان تصور می‌کنند هدف ترامپ سرنگونی نیست و مثلا…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16906" target="_blank">📅 14:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16905">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fs88Lhru9RaRrsL-mRjJqfRPFkPqKliwFi6TFsa_kscWHTyVosod6zLeotPUHR8gxF4Ndx14AlknZ24JLhAixuUEOaZi4JRklFB1N7RdnfnVonp3TqMGaY7nUl-eF1EvZI1uTUgKz1g8IXV15DzT47YiXJcY660GtDZ5Tx99xteWv-BFgyvdHySn9sF8SKJpgmJV49r0iwHHI2QCwSKAsVPgymy6XXo-iCmCHK2A0Q99scRS09I_i-lny02lsAYlVCt1m7RcEjiV1TYbWT0Wn-49Bdf5SKMBVCDBXxbKJnBu0CV4pl2PjcVys_3FZjuZZtohx5MVrYVxFT1xWtuIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر کوتاه بود و دلخراش:
محمدرضا شهبازی
مورد تجاوز قرار گرفت
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/16905" target="_blank">📅 14:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16904">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اینجا گفته بودم که هدف ترامپ تنها شکست ‌‌و تسلیم ایران نیست بلکه تحقیر جمهوری اسلامی نیز هست  به عنوان حکومتی که ۴۷ سال نمادهای قدرت و غرور آمریکایی را هدف قرار داده، جمهوری اسلامی از دید ترامپ بایستی پیش از شکست، شدیدا تحقیر بشود.  — تسخیر سفارت آمریکا و…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SBoxxx/16904" target="_blank">📅 14:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16903">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ:
رهبر جمهوری اسلامی با مذاکرات موافقت کرده است.
اوضاع با ایران به سرعت در حال پیشرفت است و بسیار خوب خواهد شد.
ممکن است در مقطعی با او دیدار کنم.
ممکن است محاصره ایران تا روز کارگر برداشته شود</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SBoxxx/16903" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16902">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYPptajMArues5dg3XrcuAjwqTxJMWu9Kvv6dl0aDZZZawbyI3vLfJmYnNGpIGsu7rcC2TIZ16B3BYJlsqqUkwa5VyIBxlVHe6kUzgNXt5Z2pKn_8k0XT_Bb3lXFx_onpV-DE7i2yqrfftt4MBqo_ANg70CXG1Te_lVyiu9NgQbMVavQcm_ecJJBT8Mz4b_PaDwLfIiY_qZFrA4QuruUiK7i0-hA52jv-DdvrHtMnlYHoETyGTLU53MWAY2xEG359gjFZvgyWsm9oD2g32F_dXRUrT38KQ14jLNwPDyYXa8cPrFClhL1d0AU9wgQ2oZtItA5VoJB2XHjmD9n1yl5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تخریب ۱۱۰۰ مترمربع از آیینه کاری و گچ کاری کاخ گلستان در طی جنگ ۴۰ روزه</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16902" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16901">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اصحاب کهف با خلع سلاح گروه‌های مقاومت مخالفت کرد  گروه «اصحاب کهف» که از گروه‌های مقاومت عراقی وابسته به «مقاومت اسلامی» است، روز سه‌شنبه ۲ ژوئن با درخواست‌های سیاسی برای تحویل سلاح گروه‌های مسلح مخالفت کرد و تأکید نمود که استناد به حمایت مرجعیت از این روند،…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16901" target="_blank">📅 12:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16900">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇨🇳
پروژه نظارتی چین با هوش مصنوعی: شناسایی منتقدان دولت پیش از اقدام سیاسی
🔸
شرکت چینی Geedge Networks که در زمینه ساختن نرم‌افزارهای امنیتی فعالیت دارد، اکنون تمرکز خود را روی تحلیل رفتار شهروندان گذاشته است
🔺
طبق اسناد فاش‌شده‌، این شرکت درحال استفاده از مدل‌های هوش مصنوعی برای تحلیل داده‌های موقعیت مکانی، الگوهای استفاده از اینترنت، تماس‌های تلفنی و حتی تاریخچه تماشای فیلم و مطالعه کتاب شهروندان است
🔸
هدف نهایی این پردازش‌ها، ساخت پروفایل‌های رفتاری دقیق برای شناسایی «نیت» افراد است تا سیستم بتواند کسانی را که ممکن است در آینده به منتقدان دولت تبدیل شوند، شناسایی کند. براساس صورت‌جلسه یکی از نشست‌های این شرکت، تمرکز محققان روی «کشف اطلاعات مضر» است؛ حزب کمونیست چین معمولاً از این عبارت برای توصیف نارضایتی‌های سیاسی یا محتوای مخالف دولت استفاده می‌کند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/16900" target="_blank">📅 12:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16899">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قطعی برق خانه‌ها از اواخر حرداد شروع خواهد شد
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی، صنایع، معادن و کشاورزی ایران: پیش‌بینی می‌شود که این روند از اواخر خرداد یا اوایل تیرماه آغاز شود و مردم ایران احتمالاً به مدت سه ماه با این شرایط درگیر خواهند بود که در این مدت همراهی و همدلی همگانی ضروری است.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/16899" target="_blank">📅 12:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16898">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آمریکا چهار صرافی ایرانی (نوبیتکس، بیت‌پین، رمزینکس و والکس) را تحریم کرد.
مراقب باشید که در این شرایط، ولت هایی هم که با این صرافی ها در تعامل بوده اند ممکن است بلاک شده و موجودی شان فریز بشود.
در این وضعیت، دپو کردن دلارها به صورت اسکناس و|یا در بروکرهای معتمد منطقی تر است. (یا خرید سکه|شمش و نگهداری اش به صورت فیزیکی)</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16898" target="_blank">📅 11:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16897">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV0eEdPpU5mR1QtprY8OeDtJlqL2QJNtd1JqXT1qFI371J-nyTs5H__AG79qvSJYq1OMs9g_PJyHranTcGCdo_f1QqRQf2SiB-UNhkdqGHQT0BSXuR7nPLsafvTg8KZy3-LkTgF7X_ddNoGntZqPmDivGJes1C-1tkgrQVQTxgEjmP30w8L95g3t0ANM26pE22SCoPyjCZ2NzVT1BjnDvWGaW2hPspBGOTkPmikBMt4t3KEHTwuMPtmNmXuUAOmfTJt86HFt4hh4i8yVQse2sVUocEZnvpyQlWg61uRZiwZbboCsa8NRXjR88MF9St4TNds1Rq2eUTgXl9L_lIyzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه به قول آقای رسایی، روبیکا حتی خودش اینستا هم داشت  (منظور مبارک امکان گذاشتن استوری بوده)</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16897" target="_blank">📅 07:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16896">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qi_lEiPhZdxgD8f28hrtdJiywWm5vhtY0-u58hh0sfFtjoa_pkxLGxYyLMTVStZsfUXEfP3Q0gNqqHnEVhRiDd9H2SkDuT34L8qwcO0qxf5HhgyJeOrCKdc3s9g6gT6pBIjsLnC56dMjPRkdkt7hUz_El0xFeydXVsKubIlfiF_fnb-95b2DHGS5Hyet4ENSN_dy9G4in8khujQbcTE43xVvgl1g7tJe9WzP-xyQ3_KO_x-GLC_KW4PHPVBaz1DkThb6zisDS3NbiyB18Hz1zA3HGF3swTIELGdM-E8CK4I-HjHpUzLUmA4RCp33jIXnoc4xrrjJ7PYfwr7OjIiE2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد ایرانی فاش کرده است که تهران فناوری پیشرفته چینی را برای قطع دائمی دسترسی به اینترنت جهانی وارد کرده است.
این افشاگری در بحبوحه خاموشی بی‌سابقه اینترنت در ایران صورت گرفت، جایی که مقامات پس از شروع جنگ با ایالات متحده و اسرائیل در ۲۸ فوریه، اینترنت را قطع کردند.
محمد سرافراز، عضو شورای عالی فضای مجازی ایران و رئیس سابق صدا و سیمای جمهوری اسلامی ایران، در ۲۳ مه به روزنامه آنلاین فراز گفت که سخت‌افزار چینی از قبل در کشور وجود دارد.
به گفته وی، هدف از این فناوری، زمینه‌سازی برای محدود کردن دائمی اینترنت در حالی است که فقط دسترسی تحت نظارت شدید برای کاربران منتخب در کشوری با حدود ۹۰ میلیون نفر جمعیت فراهم می‌شود.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16896" target="_blank">📅 07:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16895">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اطلاعیه سپاه درباره وقایع شب گذشته  و بامداد امروز   روابط عمومی سپاه پاسداران انقلاب اسلامی:  بسم الله القاصم الجبارین  فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ  در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/16895" target="_blank">📅 07:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16894">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اطلاعیه سپاه درباره وقایع شب گذشته  و بامداد امروز   روابط عمومی سپاه پاسداران انقلاب اسلامی:  بسم الله القاصم الجبارین  فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ  در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16894" target="_blank">📅 06:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16893">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ایران ۶ موشک بالستیک به پایگاه آمریکایی در کویت شلیک کرد  سپاه پاسداران انقلاب اسلامی حداقل ۶ موشک به پایگاه هوایی علی السالم، محل استقرار نیروهای آمریکایی، شلیک کرد. تصاویر، صداهای انفجار و تلاش‌های رهگیری بر فراز کویت را نشان می‌دهد.  رسانه‌های ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16893" target="_blank">📅 06:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16892">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حمله موشکی سپاه به کویت!</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/16892" target="_blank">📅 06:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16891">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رییس جدید موساد!  رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.   گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16891" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16890">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwFQZln96Lw80kKRdQZEY3VnO9zMeCdmcwaFFESBYOoNHMaGTJWx44sZlbas1IChl-pgzGBzJy5bnAPykw9XRnGgYiMzsXfR4Vlx-FLUpuUcclRN_n-vtJFiO8k8NO4PSTDVQdKq3ELM2h9v6Args0FWbE4CNVrOivDaw4h_MiPeMTiNd2hWUHI39JgGiLmOnpZBygQZs9xiAjoMa0OP4Ouf1_GhE8-r1MdblnT6rmluoT4snuPC8sMr9w9FikFlZCaOEz6NC_h8q39Od4bYgnbfsnqJ-UWg1dfktbdaqGeIx68i_yEbgRzkVSHjfFeLAFtYAskTyOQhoNSxF3oXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا رفت برای این سناریو که عصر گفتیم…؟!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16890" target="_blank">📅 01:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16889">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حمله موشکی آمریکا به ابرنفتکش ایرانی!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16889" target="_blank">📅 01:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16888">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLzmU_LbHUW2xm2vpRPXLm8Ro5hBULz8Su-d1ibnAJWRcNjWBhLYijoZ-oMKFDr_FvJ4JIvCAq4yIugoAqte2hy-aHNrmE7rNU9iUdsvZGGXyqkkaFj99hJGQ5zKbcDxSIQ849vRwcY2AdFvn-SyRTD5Osy2iPoHXyaIQrl0wErAxSuE9dd1iLPuOd7bqor5_G9-BJjCMss2cAuk3Q0TAVJ0ccQ5EtCMnZFId5COz2WQgikt2cQsqyfSij1IPYXpCCLjgENqHnp3oOQYRjEwc1TJxtsHXdi6vxlPsKmQyrTU0y_gh42FDRfed3C5ESOx_k5G0SVoHuTZgRaoxOQw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس جدید موساد!
رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.
گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین سازمان اطلاعاتی اسرائیل قرار گرفته؛ انتصابی که از سوی حامیان دولت با استقبال مواجه شده، اما هم‌زمان نگرانی‌هایی را در میان برخی کارشناسان و ناظران امنیتی برانگیخته است.
منتقدان این انتصاب معتقدند که پیشینه حرفه‌ای گوفمن عمدتاً در یگان‌های زرهی و مسئولیت‌های ستادی ارتش متمرکز بوده و او برخلاف بسیاری از رؤسای پیشین موساد، سابقه قابل توجهی در حوزه عملیات مخفی، اطلاعات انسانی یا مأموریت‌های برون‌مرزی نداشته است. از این منظر، برخی تحلیلگران انتصاب وی را بیش از آنکه ناشی از تجربه تخصصی اطلاعاتی بدانند، نتیجه نزدیکی سیاسی و شخصی او به نتانیاهو ارزیابی می‌کنند.
گوفمن در جریان مباحثات داخلی پیرامون جنگ غزه و ساختار حکمرانی این منطقه پس از پایان درگیری‌ها، به‌طور مستمر از مواضع سخت‌گیرانه و قاطع نخست‌وزیر حمایت کرده است. این همراهی موجب شد که او به یکی از اعضای اصلی حلقه تصمیم‌گیری نزدیک به نتانیاهو تبدیل شود و نفوذ قابل توجهی در روند تدوین سیاست‌های امنیتی پیدا کند.
از جمله موضوعاتی که نام گوفمن را در کانون توجه قرار داد، تدوین یک سند داخلی درباره آینده غزه بود که در آن از برقراری حکومت نظامی مستقیم اسرائیل بر این منطقه حمایت شده بود. این پیشنهاد با انتقادهایی در داخل نهادهای امنیتی اسرائیل مواجه شد و برخی محافل بین‌المللی نیز آن را گامی در جهت اشغال بلندمدت غزه تلقی کردند. بنا بر گزارش‌ها، حتی شماری از مقامات ارشد اسرائیلی این طرح را  «از نظر راهبردی خطرناک» و «بیش از حد سیاسی» توصیف کرده‌اند.
گوفمن همچنین در جریان عملیات نظامی اسرائیل در غزه طی سال‌های ۲۰۲۳ و ۲۰۲۴، به‌عنوان نزدیک‌ترین مشاور نظامی نتانیاهو در تمامی تصمیمات راهبردی مهم حضور داشت. منتقدان بر این باورند که این جایگاه، او را با جنجالی‌ترین و بحث‌برانگیزترین مراحل جنگ پیوند می‌دهد. برخی منابع آگاه نیز وی را شخصیتی توصیف می‌کنند که بیش از ارائه ارزیابی‌های مستقل راهبردی، تمایل دارد دیدگاه‌ها و ترجیحات نخست‌وزیر را تأیید و تقویت کند.
در نتیجه، برخی ناظران معتقدند که اهمیت انتصاب گوفمن نه در ایجاد تحول ساختاری در موساد، بلکه در تغییر جهت‌گیری و فضای حاکم بر این سازمان نهفته است. از نگاه آنان، حضور یک چهره کاملاً وفادار به نخست‌وزیر در رأس دستگاه اطلاعاتی اسرائیل می‌تواند به کاهش موانع و فیلترهای داخلی، افزایش نفوذ ملاحظات سیاسی در تصمیم‌گیری‌های اطلاعاتی و همسوتر شدن عملیات پنهان با اهداف و اولویت‌های سیاسی دولت منجر شود. بر اساس این ارزیابی، مأموریت اصلی گوفمن نه اصلاح موساد، بلکه هماهنگ‌سازی هرچه بیشتر فعالیت‌های اطلاعاتی و مخفی اسرائیل با راهبردها و جاه‌طلبی‌های سیاسی دولت نتانیاهو خواهد بود.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16888" target="_blank">📅 01:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16887">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7w55zD_uT_3Iw9oiq83iAYMpmqukZSOu6yeJmJX4YuLOx53UHBCidmkfyPbE9yvaMFRQ42L12Z8Em0f8HFcns3LDABmzbiGiwXlhbPm1ZC1lfAsp2CO7B_ldHcED0x_TzyEaw-rtnVdnQqeKUg64Q8pkUpbeLO2unKML5bTRKwZL5iKtYq9bKiA0u9ljfVVs8MTrkChX6AFyXRrQDGFKA88IyglU734uK0ldBeSQMOfDxZZpT-Jm82o4Zp_DRu_LpDm2wMEF3LgHaF5oWj_C9tPl04R8WoRuXivEUf1VQljX_46mtgtT9NkKB5VuyYccnTvosql8UdL5dx4QbJW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلمش را هم به این سرعت بیرون دادند حرامزاده ها!  اینها ثروت ملت ایران است که دود می شود.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/16887" target="_blank">📅 00:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16886">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/864d5386d4.mp4?token=DI0A_sTxw9IdyXvZTmhPiCW4HIfajwMP4JXU5sVSGcuh1GhF4voFRafzFd09B3bcNBv_8sopDDdw5A2d3df5smvDykbLNi71SFgF96jTkc8whbmXKBWO9MUMidrVH_C_NQo9Vego4KdyNxZjL4KJ7eOosPU5GFu1_1Ii8ve8kjZ_vG1yeuAgPbhjPN6-lSjPApy6SrXP14jhLXBCvl2k1S3s3GnfApeghNQt9ZC1FNElhWOb8g7ebb2mR6IF8imA8xw8mE8aI1EFIXo9Rhef-OtVm0agnPqhsy3zQhtCrxCYZYadcErrQG6bBXkUACgTzL7ScU871wov_-_FuEATaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/864d5386d4.mp4?token=DI0A_sTxw9IdyXvZTmhPiCW4HIfajwMP4JXU5sVSGcuh1GhF4voFRafzFd09B3bcNBv_8sopDDdw5A2d3df5smvDykbLNi71SFgF96jTkc8whbmXKBWO9MUMidrVH_C_NQo9Vego4KdyNxZjL4KJ7eOosPU5GFu1_1Ii8ve8kjZ_vG1yeuAgPbhjPN6-lSjPApy6SrXP14jhLXBCvl2k1S3s3GnfApeghNQt9ZC1FNElhWOb8g7ebb2mR6IF8imA8xw8mE8aI1EFIXo9Rhef-OtVm0agnPqhsy3zQhtCrxCYZYadcErrQG6bBXkUACgTzL7ScU871wov_-_FuEATaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16886" target="_blank">📅 00:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16885">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2ASHFI0fCydHqBgChRfRuEZv5e3O3BzA2dvIJCNLIAZg-o5PHsY8NqiiTBYNeJjzQQBZxVOk_1TEptSRvg_0gBmTQvuL3apg0H5BvdiK9Qy14voI9wpoSUggrBBJWjzykFUP2fiTm4G9guSkh4e3hdlaBaKZ1p3k1XOJ1GM9-359dL_hwwrfJ554xsIRPt1lOjjy2KbGUsTo13wOzJPef7jx22kV80jHK8zZwoZnXfwsMg8HZm5tS30ft7kUUxGV614baAAOzRgwPX5IDDNOuxHvqgoJooh5LxYFFurEPYgLFcjLptYu1e7lXGz_DU-fX9pKcofU3jZ0IB8KiMKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16885" target="_blank">📅 00:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16884">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حمله موشکی آمریکا به ابرنفتکش ایرانی!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16884" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16883">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حمله موشکی آمریکا به ابرنفتکش ایرانی!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/16883" target="_blank">📅 00:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16882">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گروه «مریم مقدس» هم با خلع سلاح مخالفت کرد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16882" target="_blank">📅 00:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16881">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گروه «مریم مقدس» هم با خلع سلاح مخالفت کرد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16881" target="_blank">📅 00:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16880">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اصحاب کهف با خلع سلاح گروه‌های مقاومت مخالفت کرد  گروه «اصحاب کهف» که از گروه‌های مقاومت عراقی وابسته به «مقاومت اسلامی» است، روز سه‌شنبه ۲ ژوئن با درخواست‌های سیاسی برای تحویل سلاح گروه‌های مسلح مخالفت کرد و تأکید نمود که استناد به حمایت مرجعیت از این روند،…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/16880" target="_blank">📅 00:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16879">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">همینطور کتائب امام علی.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16879" target="_blank">📅 22:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16878">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16878" target="_blank">📅 22:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16877">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خب گویا اینها هم لازم شده یک گوشمالی اساسی بشوند...  بعد از پیروزی شان در سیندور یکم، خیلی سیس عقاب برداشته بودند و این نمایشهایشان سازندگان سلاح های غربی مورد استفاده هند (خصوصاً جنگنده رافائل) را آزار داده و بیش از حد سلاح سازان چینی را نوازش می داد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16877" target="_blank">📅 22:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16876">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♨️
سقوط چشمگیر کاربران پیامرسانهای داخلی در طی هفته اخیر با بازگشایی نسبی دسترسی به اینترنت بین المللی
🩵
منبع : مجله فناوری گجت نیوز</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16876" target="_blank">📅 20:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16875">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♨️
سقوط چشمگیر کاربران پیامرسانهای داخلی در طی هفته اخیر با بازگشایی نسبی دسترسی به اینترنت بین المللی
🩵
منبع : مجله فناوری گجت نیوز</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16875" target="_blank">📅 20:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16874">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فناوری_هوشمند،_جنگ_را_به_انتخابی_احمقانه‌تر_تبدیل_می‌کند.pdf</div>
  <div class="tg-doc-extra">476.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/16874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">توهم خطرناک جنگ مدرن.pdf</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16874" target="_blank">📅 19:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16873">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حشد الشعبی نیز به پایان خود نزدیک می شود...  بعد از گروه صدر (سرایا سلام)، امروز گروه عصائب اهل حق نیز اعلام انحلال کرد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16873" target="_blank">📅 19:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16872">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/16872" target="_blank">📅 19:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16871">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزیر امور خارجه آمریکا، روبیو: ایران فقط به خاطر بازگشایی تنگه هرمز از تحریم‌ها معاف نخواهد شد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16871" target="_blank">📅 18:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16870">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇰🇵
رهبر کره شمالی برای خودکشی ( درصورت زنده ماندن فرد ) مجازات اعدام را قرار داد</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/16870" target="_blank">📅 17:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16869">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc85d6917.mp4?token=BfJI5zKx4-5CTLdk49Uam0unfq7x9Sm5cT1bqLiHVWyHVsUQrxDj6VG0QHrvXQWMmptIG6bhqu6DnGw0B9j6_eycyme9ArSULGCmZHecY4oJhRJrfQGd9Ybwu14bCRrNtFijYywIXcpoHw8TtVStwzuzPDJtXv89UuvVxQ10Att01XZJTX-GbJ5bsb9JqQvSymXRBNc8Fek8vrbYq6wwZj15NJTuwd9nB2PJUH-0XnLj3CHYRaI6SeABA96LnQOALI11fxIWbV4buV_kG_D3qVY3AAxOiZ3m_Fpy8k6okNHkIxJ04Vcik-95_RYhd708BMqqnw3Jo9XNh9jkHj6HBUe8nc2WykJ6xwaxRZbBHNmrvRFgG3uhC4QQpt20K516Zx9P4oMpyD8MWdL1cIpnCzqrC4pFFRP4cHe83dDfg7X5C1OvCDkRsYuJ5QhvmqP-bA0YmDAW69s2TxyF9UD-Xa2ycjjoqA_qs9oVVcSQTKrB4hQv14evLJ9dpDo3MFjo8-EM50B7BYBnefig2nv8DSr35Qf-o5eLeJG0ds-zPTRWcf6D1LOS0YVCq4VUu7yhgAz7gIW_ppOGz6veKEV0yxXv9zbN2RSIKTsFfUCT5NZe-iANLAB48Ovnva2hgwnTLFCji18CtaC1U6Eyi9VFIQkWZBi1jcjcOW1AByJidU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc85d6917.mp4?token=BfJI5zKx4-5CTLdk49Uam0unfq7x9Sm5cT1bqLiHVWyHVsUQrxDj6VG0QHrvXQWMmptIG6bhqu6DnGw0B9j6_eycyme9ArSULGCmZHecY4oJhRJrfQGd9Ybwu14bCRrNtFijYywIXcpoHw8TtVStwzuzPDJtXv89UuvVxQ10Att01XZJTX-GbJ5bsb9JqQvSymXRBNc8Fek8vrbYq6wwZj15NJTuwd9nB2PJUH-0XnLj3CHYRaI6SeABA96LnQOALI11fxIWbV4buV_kG_D3qVY3AAxOiZ3m_Fpy8k6okNHkIxJ04Vcik-95_RYhd708BMqqnw3Jo9XNh9jkHj6HBUe8nc2WykJ6xwaxRZbBHNmrvRFgG3uhC4QQpt20K516Zx9P4oMpyD8MWdL1cIpnCzqrC4pFFRP4cHe83dDfg7X5C1OvCDkRsYuJ5QhvmqP-bA0YmDAW69s2TxyF9UD-Xa2ycjjoqA_qs9oVVcSQTKrB4hQv14evLJ9dpDo3MFjo8-EM50B7BYBnefig2nv8DSr35Qf-o5eLeJG0ds-zPTRWcf6D1LOS0YVCq4VUu7yhgAz7gIW_ppOGz6veKEV0yxXv9zbN2RSIKTsFfUCT5NZe-iANLAB48Ovnva2hgwnTLFCji18CtaC1U6Eyi9VFIQkWZBi1jcjcOW1AByJidU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۵ درصد از کل گاز تولیدی کشور در حملات آمریکا و اسرائیل از بین رفت
در صدا و سیما می‌گویند بعضی حقایق را نگویید
سردبیر خط انرژی
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16869" target="_blank">📅 15:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16868">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کرملین:  اگر زلنسکی دستور عقب‌نشینی نیروهای اوکراینی از مناطق روسیه را بدهد,جنگ «تا پایان روز» به پایان می‌رسد</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16868" target="_blank">📅 14:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16867">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کرملین:
اگر زلنسکی دستور عقب‌نشینی نیروهای اوکراینی از مناطق روسیه را بدهد,جنگ «تا پایان روز» به پایان می‌رسد</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/16867" target="_blank">📅 14:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16866">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCBNoxOlEt6P4mEXNekVtim1DZ8H0g9KW28LHm0LNfZqfku72DEySzctbBZgU6m2bKZG9hahR59x1FK_7NvtV3KywR1QXSbwUXz-EjX0mYPSNRBG1AdSeSCQomelTwmNReVuK0GqDkc0wkHdiigEEzepKIhe3boZynfzphPl1fu2CFKVs9iof_OzBiko0Wbys7cEicXB46wnYzCuvcpdIru58YNVU4jLwNcOnwH8k0sKzDcASiYm2MSRDuYXTcoj1VeetdO2L2_epGVqMclVh9HRQ7wxvhq5ckEinlyEtT-ldU1wjzSTvUWDEaZVVauC6C51R-1SxKTHnKDbK7J2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/16866" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16865">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بر اساس ارزیابی مؤسسه CTP-ISW، تعلیق مذاکرات ایران و آمریکا در ۱ ژوئن را می‌توان نشانه‌ای از ترجیح بخشی از حاکمیت ایران به تداوم وضعیت فعلی دانست؛ وضعیتی که نه به توافقی محدودکننده منجر شده و نه به رویارویی مستقیم و گسترده با آمریکا. اعلام این تصمیم از سوی…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16865" target="_blank">📅 13:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16864">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خلاصه دیدگاه موسسه مطالعات جنگ درباره اهمیت راهبردی کنترل تنگه هرمز در دکترین جدید بازدارندگی جمهوری اسلامی:  مقامات ارشد ایرانی در ماه‌های اخیر بار دیگر بر اهمیت راهبردی تنگه هرمز به‌عنوان یکی از اصلی‌ترین ابزارهای قدرت و بازدارندگی جمهوری اسلامی تأکید کرده‌اند.…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16864" target="_blank">📅 13:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16863">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرستاده آمریکا باراک:   این بخش از جهان تنها زور را میپذیرد</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16863" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
