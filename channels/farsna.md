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
<img src="https://cdn4.telesco.pe/file/gQQqWhgyXtQWK5_9N8-q6vyUpEBsLNCyQ9iLjf49lGK7xG-CiBaauy06TaP-0AQJslSNIjaWkAb4ImXi5cXdwNNXZmBVZhGsP0UljDZnwtTJROAOpaVjq2TTYnD9X_F_nqGPow1pYVDWeNiWZZ95FRl5RPsPLJOTCm4lY0bKXNmpye3q-EYy4zqHEzXNrU1RWDH4f2ycF1N8TGoY4-5p9i4DSP3ogIvIBvznt-64ixAH6DkbmNnGjZDqWrhwdGdhHhfA8n33h1bDaZlCaRWn3L0r5QmNUMQbHsVSKz5FQKu8agIxpPuePF5u_JTuzNwsdD_N6JEyIaOH16RFloPh6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 14:17:28</div>
<hr>

<div class="tg-post" id="msg-441571">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اموال ۱۹ وطن‌فروش در کردستان توقیف شد
🔹
رئیس‌کل دادگستری کردستان: اموال ۱۹ نفر از عناصر وطن‌فروش و خائن به مردم در استان توقیف شد.
🔹
متهمان از اماکن حساس و محل اصابت برخورد پرتابه‌های دشمن فیلم و عکس تهیه کرده و برای رسانه‌های وابسته به دشمن و حساب‌های کاربری وابسته به سرویس‌های جاسوسی ارسال می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/441571" target="_blank">📅 14:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441570">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np091ywUPZMfd9vIqhXWJ49ueMmfgke7PnbnqkESW0Fkvv43LjzPjZjYNDIyLLFo9FnQKL0UodJg24m7VulydFVSki2QHyDdGn3T0QVi9xgDSiJQDdgewv_DOfdsxGDuoQGBTC1fzC-OZKDV-YR92z_UYo0Qkcf03vLdGBLaGcH609KmjVH_D9ZiXUN9VniTtLuKwM7Ibg64HNCUe0rrHITfvYj9IaHW1EHPY82jRIkL4IJnS6J46vq2riD8QKSiJt7PLgSuIdA7PK_HUy0vlhjMXJtvEu7vsFhp104ZgGTv3j97aUZ988dt39t8FpWnTiZuoP-G9rs8JZaqZ22_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه هامبورگ در پی یک حادثه امنیتی تخلیه شد
🔹
شبکۀ ان‌دی‌آر به‌نقل از پلیس هامبورگ اعلام کرد فرودگاه این شهر در پی یک «حادثه امنیتی» به‌طور کامل تخلیه و تمام پروازهای آن متوقف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/441570" target="_blank">📅 13:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441569">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فهرست چند عطر غیرمجاز و خطرناک منتشر شد
🔹
سازمان غذا و دارو با انتشار فهرستی از محصولات بدون مجوز، نسبت به خطرات احتمالی آن‌ها برای سلامت عمومی هشدار داد.
🔹
گروه ادوپرفیوم:
🔹
Dark Aoud
🔹
MAY WAY
🔹
ALLTEREI (Royal Essence Eau de Parfum)
🔹
گروه بادی‌اسپلش:
🔹
Mar Maris
🔹
The Body Shop
🔹
JANA
🔹
MATERIAL (Perfume Spray)
🔸
استفاده از این محصولات می‌تواند به‌دلیل تماس مستقیم با پوست و تنفس ذرات شیمیایی، عوارض جدی از جمله حساسیت‌های تنفسی و حتی اختلالات هورمونی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/441569" target="_blank">📅 13:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441567">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌ تکمیلی: روایت ترامپ از «پذیرش ایران» در برابر واقعیت میدانی
🔹
همزمان با عقب‌نشینی تاکتیکی آمریکا از اضافه‌بندهای جدید به پیش‌نویس توافق، دونالد ترامپ با افزایش لحن تهدیدآمیز در شبکه‌های اجتماعی، تلاش می‌کند روایت «تسلیم ایران در برابر بمباران» را بسازد؛…</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/441567" target="_blank">📅 13:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441566">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22473c5f26.mp4?token=gNUtgrTy0cATP-pP0Vmkr8ndORtI2eo3fw59q3hJsFxghyG_VzBsme_yZPxI4Dvrd9dnWExJNzoYDhVgAq75csugx5bPSn_I5U3AP9jRN5PedZzU2uqndKO7omWXFloiSjQzjx4VOd-gOGTsSFt7v_tzU-K3JTYtrDa1LC6wpceKdQSMVmwcasoR83DBJVFyA-QzL86GzT-Dg-x86gCSZdrvPQ7ZjMpv9-AEXZ-AMCsa1HcJ7SwZxzgPwH9odY78hSLJjVPTB3W8gPZ4WOv-azchRHBlVElR3CrweO9hTrkySxBZICGHbn-zNY2YJE95i0u8O9092nzwQbdSywFJrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22473c5f26.mp4?token=gNUtgrTy0cATP-pP0Vmkr8ndORtI2eo3fw59q3hJsFxghyG_VzBsme_yZPxI4Dvrd9dnWExJNzoYDhVgAq75csugx5bPSn_I5U3AP9jRN5PedZzU2uqndKO7omWXFloiSjQzjx4VOd-gOGTsSFt7v_tzU-K3JTYtrDa1LC6wpceKdQSMVmwcasoR83DBJVFyA-QzL86GzT-Dg-x86gCSZdrvPQ7ZjMpv9-AEXZ-AMCsa1HcJ7SwZxzgPwH9odY78hSLJjVPTB3W8gPZ4WOv-azchRHBlVElR3CrweO9hTrkySxBZICGHbn-zNY2YJE95i0u8O9092nzwQbdSywFJrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت آیت‌الله سیدمحمود مرعشی از مراتب علمی آیت‌الله سیدمجتبی خامنه‌ای
🔹
آیت‌الله سید محمود مرعشی، نسخه‌شناس برجسته و فرزند ارشد آیت‌الله شهاب‌الدین مرعشی نجفی(ره): روزی در تهران با آیت‌الله سیدمجتبی خامنه‌ای قرار ملاقاتی داشتیم که بیش از ۲ ساعت و نیم طول کشید. در این جلسه درباره مباحث مختلف حوزوی، اساتید، دروس و تقریرات علمی گفت‌وگو کردیم.
🔹
در جریان این گفت‌وگوها به تدریج متوجه شدم که ایشان از نظر علمی مطالعات و تحصیلات عمیق و گسترده‌ای داشته‌اند.
🔹
این موضوع برای من بسیار شگفت‌انگیز بود و همان روز تصمیم گرفتم که اگر لازم باشد از ایشان دفاع کنم.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/441566" target="_blank">📅 12:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441565">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtHmCw7VGEYNPbwX_E_LbwNaL16amkIHjc_nmolHM2KODvArZ9QXAe4Iybq1N-C1rqqFgY6nrm4JWPIhd2Q4dPVAtxM1Qm8MNgJZktA_2uYVEgB9z3fAMOtKRHYEv8ZYOm7VBVDncSu09gqNOpuat_RCnSEPjPpZEyrnVntDme5dSvV2RD1Ppswefs2pi5koiQxjvi6CkB8nbhp3Nz-udQpmQ6pNttZyhl_zZzQmmzpA4Ys4oPUYQKTCQa8VD6u4R8xCWBu0XxRUGhpv25LJrJZ9-AygFn9E-_1mCdlCy2g8DDwUA9n_oB0cKO1A8-yD-zt8BCguZJd2EmX-bBzC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انسجام و همبستگی ملی مهم‌ترین سرمایهٔ کشور در شرایط کنونی است
🔹
در وقایع اخیر بیش از ۱۰۰ شب است که ملت ایران در صحنه در دفاع از کشور و انقلاب حضور دارند و نقشه های دشمنان را نقش بر آب کردند.
🔹
بسیاری از محاسبات و برنامه‌ریزی‌های دشمنان به‌واسطهٔ همین…</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/441565" target="_blank">📅 12:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441564">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYn8xgDzwD1Ax5Ftv4-Q0OVUQsP4HRBw4OjdzixYWpmPGltOOQlDNtT01e6Wb9Y0gbn0OM5ZI1Pm0MPxO151bSyzZ6n3w4Rp98gxSiLl4-b_9d4Q9eRxPxjs_pAxARQ-tAnYyZ9vhFgBpoJB6kv9pogJHg6uWtHe4DdX5Kb3M8x8-tyF4UCznRsqe5pVyrUfY5sdbg3ppJCeV9z1QtX_rAX0CEz6sIYo5V7j9pt-DPPrhpRiRPOtnye8FfgAkYm9gfObHZWxjZy_qD2XBWl84MBQJB2ttEUJ_P-RuFuDzdPn9WCFlOWF5efH3XOzRRN7ZCX5bcaRpqmp1OsymQB4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انسجام و همبستگی ملی مهم‌ترین سرمایهٔ کشور در شرایط کنونی است
🔹
در وقایع اخیر بیش از ۱۰۰ شب است که ملت ایران در صحنه در دفاع از کشور و انقلاب حضور دارند و نقشه های دشمنان را نقش بر آب کردند.
🔹
بسیاری از محاسبات و برنامه‌ریزی‌های دشمنان به‌واسطهٔ همین همراهی و ایستادگی مردم ناکام مانده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/441564" target="_blank">📅 12:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441563">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌ پروازهای فرودگاه مشهد و روند بازگشت حجاج به روال عادی بازگشت
🔹
روابط‌عمومی فرودگاه شهید هاشمی‌نژاد: با فراهم‌شدن شرایط، محدودیت‌های پروازی رفع شده و پروازها در فرودگاه شهید هاشمی‌نژاد مشهد طبق برنامه به روال عادی بازگشته است.
🔸
پیگیری‌ها نشان می‌دهد روند…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/441563" target="_blank">📅 12:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441562">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d5295085.mp4?token=fo9Ubo1aqchutTK9ToCc8QeEU22clhXvMv0rWH7L3_SKRtj7bzNzBSDQI1Qi_rgouVMj-7wPwZCM4I_OODUCznMFtdCTcEQeAkp-35RuIVRuv8mjR8lps6w2f6vJpVy-SbKmfB_cpNgE_tPJT1DUbFP_x0NQgUAwbLjTAEJdSBArfppzuDJG7Y4bZ8xHZxMV0hfYi7XKq_AQaFfS0F3NJPqXAcbI0wOn_1mfEq956I_vDqjghjhw879AGk4HOh6XheYlsJphGRxLTkUmyc1VFUPx2F68cpj5AJKo7BdvJ_2ZNiCpkLHJcu2oIT4eLVJfFk4o2ReSA_CFzVCzG31d6HJ_X-dcZvXU5pQMze0d0Y4QNyLZHicM2hnLRu919Klm-Toak4QXpZH24Wa_UR0eiO9nrNt4X-60KY-E2PGZjZk65Mgjje9fYMmd9JvyNwRDSW8e-J3Ej82tjflEhs5p1fvPFEGhkBRX5UITr_W6cg1J0c-otZzD_PvqW1zPK_myxrx0G8M5eB5ujCw_AfSQ_BDGfvIFHgLxb_fGB9ZZPwo5Kddzd7DD6fpMfTRosNrRMeBzX5H1e2lTy8NfKWg7YG1uYms4qGdIiDHkz8AzQgWG-968NSSngmtzaNew26Hi7JQU_56iEyWKMmwL3Q-CRXrT4w4Kp2_fLmxW6ConK1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d5295085.mp4?token=fo9Ubo1aqchutTK9ToCc8QeEU22clhXvMv0rWH7L3_SKRtj7bzNzBSDQI1Qi_rgouVMj-7wPwZCM4I_OODUCznMFtdCTcEQeAkp-35RuIVRuv8mjR8lps6w2f6vJpVy-SbKmfB_cpNgE_tPJT1DUbFP_x0NQgUAwbLjTAEJdSBArfppzuDJG7Y4bZ8xHZxMV0hfYi7XKq_AQaFfS0F3NJPqXAcbI0wOn_1mfEq956I_vDqjghjhw879AGk4HOh6XheYlsJphGRxLTkUmyc1VFUPx2F68cpj5AJKo7BdvJ_2ZNiCpkLHJcu2oIT4eLVJfFk4o2ReSA_CFzVCzG31d6HJ_X-dcZvXU5pQMze0d0Y4QNyLZHicM2hnLRu919Klm-Toak4QXpZH24Wa_UR0eiO9nrNt4X-60KY-E2PGZjZk65Mgjje9fYMmd9JvyNwRDSW8e-J3Ej82tjflEhs5p1fvPFEGhkBRX5UITr_W6cg1J0c-otZzD_PvqW1zPK_myxrx0G8M5eB5ujCw_AfSQ_BDGfvIFHgLxb_fGB9ZZPwo5Kddzd7DD6fpMfTRosNrRMeBzX5H1e2lTy8NfKWg7YG1uYms4qGdIiDHkz8AzQgWG-968NSSngmtzaNew26Hi7JQU_56iEyWKMmwL3Q-CRXrT4w4Kp2_fLmxW6ConK1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاکسازی سازمان‌یافته در کرانۀ باختری فقط توسط شهرک‌نشینان انجام می‌شود؟
🔹
سازمان عفو بین‌الملل و آکسفام اقدامات اسرائیل در کرانه باختری را «پاکسازی قومی سازمان یافته علیه فلسطینی‌ها» خواندند و تاکید کردند: این اقدامات کار عوامل خودسر یا آنچه که شهرک‌نشینان افراطی خوانده می‌شود، نیست.
🔹
سازمان عفو بین‌الملل در گزارشی هشدار داد که «جامعۀ جهانی باید فوراً برای متوقف‌کردن روند الحاق کرانۀ باختری اشغالی توسط اسرائیل اقدام کند و بی‌عملی در این زمینه به‌معنای هم‌دستی است».
🔹
این گزارش با موضوع «پاک‌کردن هرچه فلسطینی است؛ پاکسازی قومی اسرائیل علیه جوامع فلسطینی و دامدار بادیه‌نشین در کرانه باختری» نشان می‌دهد که دولت اسرائیل، الحاق رسمی این منطقه را به یکی از اهداف آشکار سیاست‌های خود تبدیل کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/441562" target="_blank">📅 11:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441561">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6492bfd8ae.mp4?token=TLOuIkaRURDaqItVSiZuzWfM11pzUQsiGciLeQeFBoWTgYwBbNbEErxKs_l8WXdhgn3wSmBYymJOcplgOzJSnzBMOkW6UywqKczZOpZ577k02DoNZ1ez3T9FKzr9Gayno4q4oIhV6f9nB8YKRiYVfelfo2cJ0TJ8mxxAR7vLhe17UpgFWVEyJBZpGAV0SNAphNa4EOvhn6hintkSnuwGUZF-GF2Az_i8MtDRJA7bhP79DAzRBMOjCoaVo30sA2SfCLuP2VMYYS_9KKf6dCGYFpqOGCd6NQOKSqxFV9RhMU7Ym30Q_WUC09cHz7XYao1otZg7rGARuIcaEVDIAb7x0nVEkCQeTN1jTTZdqOTIFNVHqES_xyzpe_FyiufuLynA0QBZNm9hL4NytSTNNND2ms5HTVV6u1RYCbfvlXwr2PxR2mneEjeQFSmHxVBn9ZxIygqFgnPY85_neEqJ31YSrTh6BAJEQBTJnIN2FKauNd5iq5k1Rp-Dbm86OJzOW5c7bw0h9nZWfUoLH8qs5jxnXX5qg7m_sLreRQFGLoKH_DcAxaC9o9Tgg81BT2ZJrH9VuzIIDJ4rAVT2b_oxk9vBmWMEEU7SCrcKntu6kG8adpm4tbgK8gvzAYO9o8idSoaGpaJ1qxSwkXRo4cdUuOvePKpOHHnN95letd1dVFsbPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6492bfd8ae.mp4?token=TLOuIkaRURDaqItVSiZuzWfM11pzUQsiGciLeQeFBoWTgYwBbNbEErxKs_l8WXdhgn3wSmBYymJOcplgOzJSnzBMOkW6UywqKczZOpZ577k02DoNZ1ez3T9FKzr9Gayno4q4oIhV6f9nB8YKRiYVfelfo2cJ0TJ8mxxAR7vLhe17UpgFWVEyJBZpGAV0SNAphNa4EOvhn6hintkSnuwGUZF-GF2Az_i8MtDRJA7bhP79DAzRBMOjCoaVo30sA2SfCLuP2VMYYS_9KKf6dCGYFpqOGCd6NQOKSqxFV9RhMU7Ym30Q_WUC09cHz7XYao1otZg7rGARuIcaEVDIAb7x0nVEkCQeTN1jTTZdqOTIFNVHqES_xyzpe_FyiufuLynA0QBZNm9hL4NytSTNNND2ms5HTVV6u1RYCbfvlXwr2PxR2mneEjeQFSmHxVBn9ZxIygqFgnPY85_neEqJ31YSrTh6BAJEQBTJnIN2FKauNd5iq5k1Rp-Dbm86OJzOW5c7bw0h9nZWfUoLH8qs5jxnXX5qg7m_sLreRQFGLoKH_DcAxaC9o9Tgg81BT2ZJrH9VuzIIDJ4rAVT2b_oxk9vBmWMEEU7SCrcKntu6kG8adpm4tbgK8gvzAYO9o8idSoaGpaJ1qxSwkXRo4cdUuOvePKpOHHnN95letd1dVFsbPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قهرمان‌هایی که در روزهای سخت کنار مردم ماندند
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/441561" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441560">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌ پیام تسلیت رهبر انقلاب در پی ارتحال آیت‌الله فیاض
🔹
خبر ارتحال مرجع عالی‌قدر، آیت‌الله حاج شیخ اسحاق فیاض (طاب ثراه)، موجب تأثر و اندوه فراوان گردید و حوزه‌های علمیه به‌ویژه حوزۀ مقدسه نجف اشرف را در سوگ نشاند.
🔹
سال‌ها حضور در حوزه مقدسه نجف اشرف و کسب…</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/441560" target="_blank">📅 11:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441559">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7962256a5.mp4?token=pj6MZGxiv-JaIq9y06L8MrcugTspRxdjfXr4SkqLgjtK5UcLAXx5fhZO-qN05tMAml1g7_1608oYYjFX12Im8bYyFRhfxejmFKjPDLw-FPbneeapr2rfcgZTD9BI9FraCTvFOseE9DPWP9QfG8kbCLK99aRV3kmWI58xwhaaUwRjEEDlbZJT91nSfzqar8Q260FJc8T6ZQf2p_18HOwgNJd3cwMx5sxhq2lo9WQPBq6ColBfgdDTYjZyvTbFpMmL3-OvoHE7fPqTMRrxMaIIFqAPK596D0g-pAiX4qMTWMU1fP-8XyoK5rAqSpptIB9uH5htv6HLPvIU_Hgb2GBBAIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7962256a5.mp4?token=pj6MZGxiv-JaIq9y06L8MrcugTspRxdjfXr4SkqLgjtK5UcLAXx5fhZO-qN05tMAml1g7_1608oYYjFX12Im8bYyFRhfxejmFKjPDLw-FPbneeapr2rfcgZTD9BI9FraCTvFOseE9DPWP9QfG8kbCLK99aRV3kmWI58xwhaaUwRjEEDlbZJT91nSfzqar8Q260FJc8T6ZQf2p_18HOwgNJd3cwMx5sxhq2lo9WQPBq6ColBfgdDTYjZyvTbFpMmL3-OvoHE7fPqTMRrxMaIIFqAPK596D0g-pAiX4qMTWMU1fP-8XyoK5rAqSpptIB9uH5htv6HLPvIU_Hgb2GBBAIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی قوه قضاییه در گفتگو با تلویزیون روایت فردا خبر داد:
بیش از ۱۴۰۰ همت اثر بخشی مالی بر اثر تلاش و مبارزه مستمر دستگاه قضایی در ۵ سال گذشته
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/441559" target="_blank">📅 11:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441558">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPdmFDhgIaG2BMpmYGVP584izmpstBjd3BYoLCuciPj6Rdi-dqPWwhThoVYYOSVi4_RdBIlaPgb7nJFrwPVTRDpa1pp74kdapPz5Q10ZQ3pcaopPjCAoInGfvZSKshNKcB1YUgB9lSexMiHnaUF5PKUVdHQHFt8ZF6dTao7aKRMMdkO_02FKMfp4gsgjJ5WryN3FsJbeGCSPnfehuvzcobb6dqf6urXiqPKfQ5IoiKNr8WSUkVYIODaZOJ3y6WVsiofLbt0KcYWW4wi7YGKO3gZdu3cS-jlmzrsC6M6gulfSKEz3-Mi0dzo51GFNSGkmGqXZZZkvTXxZguDa-tBicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هنوز ۵ گیگ اینترنت رایگان نگرفتی؟
برای شروع پیش‌بینی‌ها:
1️⃣
وارد اپلیکیشن «همراه من» شو
2️⃣
گزینه زمین بازی (جام جهانی) انتخاب کن
3️⃣
مسابقه‌های جام جهانی رو پیش‌بینی کن
4️⃣
۵ گیگ اینترنت هدیه بگیر و برای جوایز میلیاردی رقابت کن
🏆
⚽️
در «همراه من» پیش‌بینی کن و برنده شو!
👇
👇
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/441558" target="_blank">📅 11:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441557">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/441557" target="_blank">📅 11:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441556">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b0718a9af.mp4?token=MHFwXZA7O8YlOo9q-30z-cG7rL2dlz5Ml0FU1FEMtW_zkT-C6fpb_bdmiqZj12Bm-88TJ4QtZzCXzCeJNQGKm8MVq2HAPhQArICqPw89ta7wOFQ2DkSFKcq_XKJTNhbsN6FlrVVmCfIEVQ6iGtutyi8AwQK-f3KMJvYAqNakxmmuKnCgwzGTftHjLfD8gWhw-4UJVJz8mWZgyCfOCYfNLpWPnEFhBRrdzqtwy0pWGCGNEl6MNphKS5uh0xwj4ZoF_IpAISwcp2WqJ2nVwe6Qf11PmRxg9eoWmFFaxSTp6SK-__9JUdQAeB26ecsYu_P8tPfn4ol8EJCQxsZCRPwd6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b0718a9af.mp4?token=MHFwXZA7O8YlOo9q-30z-cG7rL2dlz5Ml0FU1FEMtW_zkT-C6fpb_bdmiqZj12Bm-88TJ4QtZzCXzCeJNQGKm8MVq2HAPhQArICqPw89ta7wOFQ2DkSFKcq_XKJTNhbsN6FlrVVmCfIEVQ6iGtutyi8AwQK-f3KMJvYAqNakxmmuKnCgwzGTftHjLfD8gWhw-4UJVJz8mWZgyCfOCYfNLpWPnEFhBRrdzqtwy0pWGCGNEl6MNphKS5uh0xwj4ZoF_IpAISwcp2WqJ2nVwe6Qf11PmRxg9eoWmFFaxSTp6SK-__9JUdQAeB26ecsYu_P8tPfn4ol8EJCQxsZCRPwd6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسطورۀ فوتبال مصر: آمریکا با میزبانی جام جهانی می‌خواهد آبرویی که با جنایت از دست داده را برگرداند.
🔹
محمد ابوتریکه: فیفا با دادن میزبانی به آمریکا در حال سفیدشویی جنایات میزبان این رقابت‌هاست. اینفانتینو می‌خواهد جام جهانی را در کشوری متجاوز برگزار کند.
🔹
کشوری که در نسل‌کشی غزه شرکت دارد و حالا جام جهانی را میزبانی می‌کند تا آبروی خودش را برگرداند. کشوری که رئیس‌جمهور ونزوئلا را ربود و به ایران حمله کرد، حالا با جام جهانی می‌خواهد جنایاتش را سفیدشویی کند تا آبروی خودش را برگرداند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441556" target="_blank">📅 10:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441555">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38e7322b2.mp4?token=Mq9MTRg3VPoWzxiQJcxy1_ZJLfaov7lbU22VaJn4ool5hTHdHTvyC35yQIHsOE_9OPLTa0MMwA0TmylC9U3Hq2EzuHAX8QivEy16S_feTXAANN6FTn2c68XrZwCF-SLl5wM6XHLGNFsMPqP6W4L_4eLIL1o33SLMe-EchyPEeh7tc6kiDvI5ewvrD7LweRuGTHyNGsPnw8u616_xVGlJ3uWdiJOp7nuNL15xU-A9mO1bXbh_7iIu8ckMFZ7dYplUQk87lt_uBI30Aii8SVPv7xEPujtCyICAR1bdk9-2jCNk3huarR8u04GUj7CtzJkOxhRVlQMem6bCkkgG9aIaDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38e7322b2.mp4?token=Mq9MTRg3VPoWzxiQJcxy1_ZJLfaov7lbU22VaJn4ool5hTHdHTvyC35yQIHsOE_9OPLTa0MMwA0TmylC9U3Hq2EzuHAX8QivEy16S_feTXAANN6FTn2c68XrZwCF-SLl5wM6XHLGNFsMPqP6W4L_4eLIL1o33SLMe-EchyPEeh7tc6kiDvI5ewvrD7LweRuGTHyNGsPnw8u616_xVGlJ3uWdiJOp7nuNL15xU-A9mO1bXbh_7iIu8ckMFZ7dYplUQk87lt_uBI30Aii8SVPv7xEPujtCyICAR1bdk9-2jCNk3huarR8u04GUj7CtzJkOxhRVlQMem6bCkkgG9aIaDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با داشتن این خصلت خدا حتی صدایت را هم نمی‌خواهد بشنود
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441555" target="_blank">📅 10:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441554">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
المیادین: رژیم صهیونیستی به النبطیه در جنوب لبنان حملۀ پهپادی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441554" target="_blank">📅 09:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441552">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e11b63690.mp4?token=bPcpc_EaSjpVUvrEwjpAvBi4NDqhEDRLtiZz_j7l0TA2MPxcOd-TzjRQXFAZPR_8sMa9mnmH4xO5gQDICMziHEVqOdNhj_F8SDJj4dDAHiZk2aOiwhrKgcdnO-WaZsDK56K2KFnQC5voaKOFh3MpmLZOeUHEWwwsev0nR2Rw0VxweMepvPZQ_bYtadAxI3X9p9bmmPBGfrTPsvQOq4IOSZAJSpserFTgvro7xN5cd2KoePguIzm96LknuSi4XOLV2GSODxY3lDNhPnqUSh8MKkfaKja9LV5rHRhfYIOtiL9uzb7B5pa8Y-7oPKe6LKUfUgRQySliYclMg51TuVhfCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e11b63690.mp4?token=bPcpc_EaSjpVUvrEwjpAvBi4NDqhEDRLtiZz_j7l0TA2MPxcOd-TzjRQXFAZPR_8sMa9mnmH4xO5gQDICMziHEVqOdNhj_F8SDJj4dDAHiZk2aOiwhrKgcdnO-WaZsDK56K2KFnQC5voaKOFh3MpmLZOeUHEWwwsev0nR2Rw0VxweMepvPZQ_bYtadAxI3X9p9bmmPBGfrTPsvQOq4IOSZAJSpserFTgvro7xN5cd2KoePguIzm96LknuSi4XOLV2GSODxY3lDNhPnqUSh8MKkfaKja9LV5rHRhfYIOtiL9uzb7B5pa8Y-7oPKe6LKUfUgRQySliYclMg51TuVhfCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مونتاژ منتشر شده توسط شبکه سی‌ان‌ان از ۳۹ باری که ترامپ از آغاز جنگ تا به امروز ادعا کرده است توافق میان ایران و آمریکا «نزدیک است»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/441552" target="_blank">📅 09:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441551">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHhvGJo4oX6m95dLwfCek8pWgkhTSz-CmXEx02jmGCfdisq7g9OInxNvQxGGAsJg_oYXnrnKggI_5q1Unc2PEcv7sfTNDOOuV2cEeexrVXCx7xXvIMS7vOj-CR9eVofKiMndpyUfhWLWpNL1vd_Jy7KxWPdEpvKSqMpk8Bg4oEVb1W9keArmB5WMvcXBLG93DzFocaTOqf-I8oiUV246NxYnPbSoSKl2-w6ZmAVbjDc08gUzBKlpL1H3UBOs_rQGuEnfjLbF5nAOpQZoTf10iN9vRODT2JxVUE0Ky9W2oRmHzSOcUuyUY84PENeK2BCGQPLBi5IWeO-D-3bQ2zc6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حبس ابد برای رئیس‌جمهور شورشی کرۀجنوبی
🔹
دادگاهی در کره‌جنوبی امروز رئیس‌جمهور پیشین این کشور یون سوک یول را به‌خاطر رهبری شورش در پی اعلام حکومت نظامی در دسامبر ۲۰۲۴، به حبس ابد محکوم کرد.
🔹
این حکم پس از آن صادر شد که بازرس ویژۀ تحقیق درباره پرونده یون ۱۳…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441551" target="_blank">📅 08:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441550">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKSkrYLLlEwLzuT9v0N9yTqgrzV79vMJ9YDyuwv0NC-dZXjBTGex89I-vr56wI5s3MaSioUpXjPRu00hjlaKIrl00jTl5VpS4GBbg3uf-Ye9mLnMHjkANnTWsBRdfLjVt-izo4HtqrEsRbOexpbjHjMpv5MSy8T-aRegmhP4bn1XzQETtofRYbPFIi_vTZXZA7iSEngUA8Jyg5CSi0w6lSD6zkBsSFVHFA4ux67MWwAPs3i2FHJ0nlDVtowT_5yGRzb-M-90CuQsCpab1FzihfBILAKejICBcoGGUWqUeIO-Z_c2UTeYgGo2QtOreL5USTMSuD1kb0cPMJ30s8cTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین برد آسیایی در جام‌جهانی
🔸
کرۀجنوبی ۲ - ۱ جمهوری چک @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/441550" target="_blank">📅 07:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441549">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
منابع خبری از حملات هوایی رژیم صهیونیستی به حومۀ شهرک بلاط در شهرستان مرجعیون واقع در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/441549" target="_blank">📅 07:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441548">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtT4FgWiGURRanN8EYvOU8GfHpteVD0mmYoemgTYU6AP90_fee-jaaJWk62r6HpnQsDv1eF2xKgwsb8Th5kmXuJs8fIHWJbjZefMAF2ad3_dvgZ9fpsmThE0NGJOV3cz7foQyZlKnNTm3HsrgXG_falDgq6XQ7ptMf6BORH5YUmqUZ9JGJavvNJ1WEtKwb6WXzTmkqMCxYwQpb1lUOz0e0ucOfztk52Zam3nTR27O6MLbqOrFYG0vuiNQQriCUBCRxSr6dh3hM3XEQfkkFph7Mv9XwaJJfATm-lFpqX_VpPuZGVibGliD2lodt6_oiwWXW3QWPrFDiuw9YdFr_My_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول گروه A جام‌جهانی ۲۰۲۶ پس از پایان بازی اول این گروه @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441548" target="_blank">📅 07:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441547">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWAKOwQ4YX4pd26Jp-qQDbKlzLcqh_jHPVtvbIzp4pVrx6qbfqUqxS8joLij3BaAQJvdUTnTUcEcRwe5cIDkDNl6JekP__r-aFkRaIFSLmGutxtedIoBwNPJwCTCOHqLURTa60UmhvzXSvpkSqLHPpIDJsOtyqKkTS_-BVmvYeXSAPGNBLz3uGKkBnU8zNTlrGlidFWpGxcqwiLZ0vmu5iTFGl4OjIWaIMZX1QVCsMArHr2t5ID8HLbQJUwcqHlc5nt1-s3OYfIcXAO2Il59LpVLJ3a1Rv5oezwV5g3NCChtcS9VnPXktWFsYQyyLqnLbqhYYEkU5Pm-2gqOAtkcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین برد آسیایی در جام‌جهانی
🔸
کرۀجنوبی ۲ - ۱ جمهوری چک
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441547" target="_blank">📅 07:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441540">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEBWFPvIXvM2ZeNorI0Pgr3qRp-HdJfu9OI_7pc06LcBHCzVvmt0YGsUxg8gmCQ5gEdA7asJ6lAU-U6cbP4MJh00lDUHjv5tdPZYggBTSLdC-DYQDjO2z703NUXmCrpp2f9N5b3M6l_iLSJ-Hbe5wK8X9drssr0-7iki_0FIQ2WeYRB9CzdXlX3bDKgfVtcyqoOFAwJCV2sbntrWYrPRhkpy3cTL4AfkP3xIPPyptB8BvQpweJzcQE3DxSxwz6FmZeH660rmIe5WJmdDFiohEQLKFB-yylFei5GPsMP_QW2FGKTJm8wxh3fad01rLgMFjncV9VdBgDYMsns65XAcSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PopJnMZfc1yIvyrF4blojYV6R7AlxJE4wFVHSQQLUBAbhAe21wAXMpjTLq0ct20mkAJoBLWueH_26eyfklxQh8om427CaKNjInJ8meklXH8yx7K_QEY2UyEVtlUD1RXVC3m05Bi87WB2QyzN2WtGWt2735xXP-PpOp-iY6pbXfiG9Y_HVw66QrW4s82oDQ8EsYMJu2gapp3HuFl0tpfacuZdCK2cYWhfQ4eNjJRhwa9nQJGsYi77BGV2AHOiIL8hWe0ksy5aODD4O0x9Hv8SQxmSHEfxyRa6zqgEi9R4P4HgfgcBjSnKNgpc7U-TKQhWxz9u9LGDsXAN5cgjGZPwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyBBRUxoH5ZAl98cNtMY_SUSYWZGQTWmb0r_s3J1olB40W2sRqR__00imvurd7o-pxZfB6__7mL_iuUjesP4QekoVfu5ptBs4gy5r1cNJYD-bD8RmWmmEJV2s4uHeT1CmwXFIQ3gqqIFioxnvUKKPCnwvigYuzz67JVYypsxJYWKpfpUziE9LCWFfu3fk-nKoZ5iCuIwW6CJ5NzyCI9nup2vsW4ZPpBOwqHTufUVtmFKVn3RSoAw9hSD8SjvXAf-GqjeWxXHsCe18XSqO_nt2F3bVdy4xwESiHRUuq1ZOwQuAOLKGGC_n0GdGKcuj5DHkqMJUbrTV8TyWYfITD483w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZNRt6rc1gh28szftTic6q7lUYaCSyAl1n4WqdOZnKFZXgsTC4E_r8p6o8PL65CkRD8Et3DSm-xYkB4XcNzaOtAQljS3eniqCencZwLPKE5lp52NanOlU3fpucqS71Eux2gcnm5KqvOqRDIiRIBbjClkIGb-ZagjvWZQjBckvEbsnBU36X8o0tT6FieV8DZGf5aEqnVCNvDqScsHF6NXHzLS_6uUkEw4zSb6F-dO8gIDMtg1LE5rNuLStiTuBn6iTL7dQzZQP8RfQcxhMf09N1DLM9L_-lIbTugUsZnibIGbbr-8FBtTZKn6khiVjrHS4jSX9YQ0iVRDiXDbQRTpgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZSakv7xhK7gPDmi3tGT7l627xrp3fQvMiRlxcEJQA8jjhFGb3DNXv2seE1uLxXUxC0RpSj3nrKXYERb4_o_s6RxuFYDfMASRnT5F6-od9_p1X3znDSw6idlMcGVXDPKsq5kPV3vPFUbGdJZ0CyZibtah3ITiRvIcAlsIZR4QvGPFm7NTidKc-AdXuyG8lWaXDbiZ94Is8-hIgp0bIX_RxQ-rvQvMv6XcqSYd7VU658ZdtJ3zP_Z_UFN4jFSw7p7FdTypASuLOSdwrCnge7RMp03R7pCXdsS8zUrc9HgvYqE7JdJn232w2qzwtZ_RI8fh06pWzAciFdSIpWLg1gYNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqQFB4QXzb9sg0eUMYUM9nfA7iA7bdMW50BXqxdZlkH29O1S9OmHqM63pQQ52LP2ko1OlJU02hDj_E1EKd63jT7ybcjEimKgvO-CpnOQ6AJqVEoeheqTvYTDGFstmunQf3j05DaKlR49ZHr-3zjag3XPoYGv89q4qmtY6rEEcG8P800xx-Tm9kD2eU5j9IlzgiIVPV9gRu1bxhxxUoZXl5KxByEmSozELfn_qVK9Jcc8GQTgIl8FyJTu5fZi8SVgPRhzBgLk81ENU5YgE0lV3lFMaPbN8oEhXbpoaqqA7esDIXGAgxV34pQWb7j8f02LlzWU9qU-EBG_kckZFpckoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baDy1nqy6sgAKS9RSb5aR_JHBcClqTsDoMbM_1HmXRICuHx9RzKB0pWZXjLK8MS2C4A3lUt-G8qEDRK2n-3cNjqRJ-d6j_TNEhoR0U6uEN8VUP1kOFQBjtD9y4CeDx0CzVbogpH71Rs8RsB3dmX5ulKqKd63xQ_IchcwiJXpRVpM2xSYrsIk1inAxXFgrm5nZL1YIH8tj-IjPWi3bqIWExLKy8F7LdrrReAeKuqYB4qI5Jcf81kKJNaWQoelLJRc4_Wo26NIOsI4wSgndgmmykC0c9vh8CRGnUnmb8fLoDU29b_RakY1bGxEN6gzzhWW628vgd7BAYgAnlwbfI5K-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کوچ بهارۀ دامداران مازندرانی به مراتع ییلاقی
عکس: غلامرضا شمس‌ناتری
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441540" target="_blank">📅 07:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441538">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2a21254.mp4?token=OiC7e3HBJu9z9qmdpw66hB0lShLy-wlfzCFSizM28GI9lc16edlj0jYGXkU7yX6yWBJBb_l54bFXFLPhQR2tC2pwW38uN70wWyx2pRWvlte1DdoGXQqkk5xJ1e09C5yVhQVjfvukqKdDSL3mt5KTL5_qsmC4IJVfvYQM9CAa_dLSgY0guzT4DqPWUU6euFrBREwjWgqLD2RoITNTrk19TXBiO-Fvaf9tmdg5b89XJgpRzwAy8Xwff9eNN-ZTQ45VHDVeNavz5tJPUYiL5aXWxE7zUEfFl1kPNLSaA8KjnkHckc4oMoHUHhnvk4Go-9guuJ-UukOxbE5h39iR49nlYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2a21254.mp4?token=OiC7e3HBJu9z9qmdpw66hB0lShLy-wlfzCFSizM28GI9lc16edlj0jYGXkU7yX6yWBJBb_l54bFXFLPhQR2tC2pwW38uN70wWyx2pRWvlte1DdoGXQqkk5xJ1e09C5yVhQVjfvukqKdDSL3mt5KTL5_qsmC4IJVfvYQM9CAa_dLSgY0guzT4DqPWUU6euFrBREwjWgqLD2RoITNTrk19TXBiO-Fvaf9tmdg5b89XJgpRzwAy8Xwff9eNN-ZTQ45VHDVeNavz5tJPUYiL5aXWxE7zUEfFl1kPNLSaA8KjnkHckc4oMoHUHhnvk4Go-9guuJ-UukOxbE5h39iR49nlYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاره‌شدن لباس بازیکن جمهوری چک در اثر خطا
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/441538" target="_blank">📅 06:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441537">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4lNmJYWC6pxs2pxSYF9rde8uSUPGqrhG4hI9YOxg-CQsuQbNiFGJuSoST_zTW12W0Pu0ZNMMxRD752LWPz5SvHYtAy7sjgWQYTvut_bDjoOquQB7PxJz2TzcewpuQXFX4OWUffVeyR6jwErrqAkKVglRuofh6WWEq6p4GzieOEAvqYKvovFIPgQTwLXa5OavC8IRAREWM7z4wb_Ab68xhldtBrQGYZDssmgWYGHUovuBSq0Zt_1DL8o8n34AiqwLdUcO1EtHz9ITag0hL6IEFXsv7l7nZ00xEdwr56zhsbVVR7waTA9bQZyU-0aZ4FExLxM1iV9jos2FMWpajYiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نیمۀاول بازی کرۀ‌جنوبی و جمهوری چک با تساوی بدون گل به پایان رسید.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/441537" target="_blank">📅 06:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441536">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9oetCf_07KbJdCE_Z4u08p2_XY914UQzahxA86LrFQQo-G0PleTxXCR0aSQlSYwjBEcDM0oU06-qXxu7cgdYaO_88n0r79BEQIeE_uCXFx-n75a6dzOGm3bF_de6u7PJFiWxnlWzpPiyueMfZZ0y1bxB44j-sw1XER0PIiML9wnS11Hp2pzZK12RGbiW97q2s0DL59l7S32zMpzHZ4nxfKpBl7qtPzFfkg_JKgAPM7w1UqxUwxUMz7t3SAPfPTZXHor3aP7yNfoglTOAc3AeC5tW3aoaSN9jqUMvze-1tOOZOcrLPJr9KJWnftfNGsZY0h63GoL2VVuvhOeDHCgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوایپماهای آمریکا گران‌ترین سوخت یک دهۀ اخیر را می‌سوزانند
🔹
هزینۀ سوخت شرکت‌های هواپیمایی آمریکا در آوریل با کاهش مصرف، جهش ۷۸ درصدی داشته و میانگین قیمت هر گالن به بیش از ۴ دلار رسیده است.
🔸
کارشناسان علت این شوک قیمتی را مستقیماً به تجاوز نظامی آمریکا و رژیم صهیونیستی به ایران و به‌دنبال آن مختل‌شدن عرضۀ نفت در بازارهای جهانی ناشی از بسته شدن تنگۀ هرمز مرتبط می‌دانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441536" target="_blank">📅 05:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441535">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جنایت جنگی آمریکا در حمله به تأسیسات آب ایران؛ سنت‌کام وعدۀ بررسی داد
🔹
سازمان تروریستی سنت‌کام مدعی شده که درحال بررسی گزارش‌های منتشرشده دربارۀ احتمال هدف قرار گرفتن یک تأسیسات آب‌رسانی در جنوب ایران توسط حملات موشکی یا هوایی آمریکا است.
🔹
روزنامۀ نیویورک‌تایمز امروز در گزارشی با بررسی مستندات ماهواره‌ای ارزیابی کرده بود که حملۀ بامداد چهارشنبه به این تأسیسات آب آشامیدنی در نزدیکی تنگۀ هرمز احتمالاً عامدانه صورت گرفته است.
🔹
روزنامۀ نیویورک‌تایمز تأکید کرده حملۀ عمدی به زیرساخت‌های غیرنظامی «جنایت جنگی» محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/441535" target="_blank">📅 05:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441533">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JBlgLM25yKBwWL819J0uM6BY9zcvUgHx3tg9askbAl2pM6m8aqdFwXYR9oDEB2QxQBKoOwIPSfQiZ6XfGAHiHaly8DmN03wNB6pRNoh6LriyJn9B-59brIttKCi-73i6ADKvLqYMkdt8VMY8j4ya0y8D60iTVXHOpfWxkLHvk7-QmwnJZ4FCN3z5jYc4TU4fFXNCV1o2QZBtJeC71gFTPRfYT-nNxoVXGk1mFsUpUTaH1XEDPcrXQpuQfD665P4DONYD5EUvkIh5e4NnslUefiwuScVxIUSbSn7RRQiyIOgr4JBuyCdO-00mD_e2WpVijOMLQiMBYBE7-IzWTbAJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kS-Mesv2o1xDfMxQ3saz6ADabJjh1AGzRcNG8vM1KKyuEuiPgME6qEBOn8PHCTzsSXNSVt9sDSaa7QY4eqym7idT4QyL6vpBQ-LN1_PBN_ck3SCElHpbrfGrhTJrmFQkK-4BZhHvANmaLPdUn8vmqWXgDUuaGrFGFbAahThH2WUMYjZ_Hu8kTmcYeTv7LU3W42i2tdc5JZJl6XigtbzPlhrl-uOFKkl6E1wCpkj-120fZKttfHqYM3HD6MK-f5CKWuW8jSfMzMDhyFGQysM8ymOCmucg2tWFvYHUD98jG6WK9ttWLgwMVfYh7-xBA67MGfEuCC62XMVaIsxUZZgWxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حنظله: در پاسخ به حمله علیه زیرساخت‌های آبی ایران، تأسیساتی آب ایالت کالیفرنیا را هک کردیم
🔹
گروه هکری حنظله اعلام کرد که در واکنش به «حملات آمریکا به غیرنظامیان و زیرساخت‌های آبی ایران»، تأسیسات آب ایالت کالیفرنیا را هک کرده است.
🔹
حنظله اعلام کرد که باوجود دسترسی به سامانه‌های مرتبط، از ایجاد اختلال در آب‌رسانی شهرهای آمریکا خودداری کرده و این اقدام تنها «هشداری» به واشنگتن بوده است.
🔸
این گروه هکری هشدار داده که هرگونه اقدام علیه ایران با پاسخ متقابل در حوزۀ زیرساخت‌های حیاتی مواجه خواهد شد.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441533" target="_blank">📅 04:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441532">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARGtrzXo3hrftk-a7pF_4BZMtc8nXyvCmVfY0qejOsQ-14lskxRZvP6VTjz6NcctUNkG7h5P8iQ43L8K1-K1CkohwSrs1z_fCNmha2ajjph0x7KkMyAMz4Q8CApLVCqa3u7ssYgWXUYCbzAVuW43Y2g3Kj4xewtB66ed_NTI9HVdax85_7GQdERR54F26PzkWOcGuG-QvNcJ6jeTAj_E0QKNEZ9plQYEZ7QsTNE3-LLyH5KUEivPJV30eeEeFffuJBu-1Lvw84w3o9czoxt6DXya7-kIXcPeVFz_HVfSrLLaDX14Fop2WrjH2CvnjBABrTu2AO68_vU9DHgKZ3-iAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانادا چت‌جی‌پی‌تی را برای زیر ۱۶ ساله‌ها ممنوع می‌کند
🔹
دولت کانادا یک لایحۀ جدید «ایمنی دیجیتال» معرفی کرد که هدف آن محدود کردن دسترسی افراد زیر ۱۶ سال به شبکه‌های‌اجتماعی است؛ مگر اینکه پلتفرم‌ها استانداردهای ایمنی مشخصی را رعایت کنند.
🔹
این طرح با هدف ایمن‌تر کردن چت‌بات‌های هوش‌مصنوعی طراحی شده و قرار است یک نهاد تنظیم‌گر دیجیتال برای تعیین استانداردهای ایمنی این فناوری‌ها ایجاد شود.
🔹
براساس این قانون پیشنهادی، شرکت‌هایی که از مقررات تبعیت نکنند ممکن است با جریمه‌ای معادل ۳ درصد از درآمد جهانی یا حداکثر ۱۰ میلیون دلار کانادا روبه‌رو شوند.
🔹
مقامات دولت کانادا می‌گویند شبکه‌های اجتماعی و چت‌بات‌های هوش مصنوعی برای جلب توجه طراحی شده‌اند و می‌توانند باعث اضطراب، انزوا، افسردگی و سایر مشکلات سلامت روان در میان نوجوانان شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/441532" target="_blank">📅 04:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441531">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KT7SSifEWZK0fPGo6r_w7fSiPtx0NIibmJrAzYMmVIWFeRGL_JoE2LrQ5Xsf7o73Cx_28B_9GMoEW8WPNJEhjg8c-DAkTCvrRQkVfikbxklqnTxcxbPwWPgH9Udsb0gmFV54f9bEJzj8ZQmgJAUNlRXodkgrJwlaflob7k88hZnT6U9kuxd9F4BTFZJcmWBOM0e_P6bnqs2FCQV1xlj1lf4eQTyVCQ8-AepE5VmCL-T3SPFWoft0VHVu3t5eZbTzkxDAqj9WMgc7VB-S1RaqKyaYYuKlDxZS2YwhfaHEuKQ8_qlcDxA2_AKhypzmar59Bnnx9Z2Dm25U588kyjlStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزۀ خفیف پردیس تهران را لرزاند
🔹
ساعت ۳:۳۰ بامداد زمین‌لرزه‌ای به بزرگی ۳.۱ ریشتر در عمق ۱۰ کیلومتری زمین حوالی پردیس تهران را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/441531" target="_blank">📅 03:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441530">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de09e75f4.mp4?token=nDogg32020Kgg_IEXPiM9feW86mlWvjljsaJ-sH9btJbh0EJJq9um1sLkidKDmluWEerb8MeTvYYlhe7qbvT3SSADMZ7YB92kjkCAdgqhIvRS2I-IBYc3pDIuvM2p3W9rzkjtiHDsl0lB0-rMQCqJFeCIVDvR4S37aJ8pv49jKP9AGHtwkWQ0Mc5QrGoyPzy25GJ2yPB5WwjtTzX1MEI_fEmQryJBw0qsEAINZ7PfKze5wNW7GqgdUFtavSAhtHAwOAXlUVwpa3Lb7_fd34f4SAofD7No5uMNsV8H2Bx0zWAF5ioB8XuQh5DpCIR9te-Pw_UiFFz0DIMWRL8y5HI0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de09e75f4.mp4?token=nDogg32020Kgg_IEXPiM9feW86mlWvjljsaJ-sH9btJbh0EJJq9um1sLkidKDmluWEerb8MeTvYYlhe7qbvT3SSADMZ7YB92kjkCAdgqhIvRS2I-IBYc3pDIuvM2p3W9rzkjtiHDsl0lB0-rMQCqJFeCIVDvR4S37aJ8pv49jKP9AGHtwkWQ0Mc5QrGoyPzy25GJ2yPB5WwjtTzX1MEI_fEmQryJBw0qsEAINZ7PfKze5wNW7GqgdUFtavSAhtHAwOAXlUVwpa3Lb7_fd34f4SAofD7No5uMNsV8H2Bx0zWAF5ioB8XuQh5DpCIR9te-Pw_UiFFz0DIMWRL8y5HI0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ جانباز پای لانچر به سوالی دربارۀ دلتنگی برای دست‌وپایش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/441530" target="_blank">📅 03:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441529">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e016e32dc0.mp4?token=AHSPQA3D6QrOnt-jypuFosQXqh4bSSTdzvc1uS5Us9eSSSceJM24alqyUrPtS2k_f28ucShrks6UfxbAFL_UFS36lIOaMjE6qacWsl9djSqCOqsrgcDIKcSpgpNIXoJe2yXd3jPQcQOTPy2LcoWozOx0ckYh0zJtTunMDHdht1Aw5E76D5XEw-8eBKltCeTqCzckkJiCBoHkdmn3uv8RjZxu3CBVqo_iwkfad_5rc4lUG2mbmprKTXPgMC4nB6gJ2v5HAlpKOFLA5X_0lE6nCW9XYOijEoou-uxcSBI_H1jNffAQ1UDxcpJTW0gHMmvsj31WqrPfYmhZ_2beFe5OgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e016e32dc0.mp4?token=AHSPQA3D6QrOnt-jypuFosQXqh4bSSTdzvc1uS5Us9eSSSceJM24alqyUrPtS2k_f28ucShrks6UfxbAFL_UFS36lIOaMjE6qacWsl9djSqCOqsrgcDIKcSpgpNIXoJe2yXd3jPQcQOTPy2LcoWozOx0ckYh0zJtTunMDHdht1Aw5E76D5XEw-8eBKltCeTqCzckkJiCBoHkdmn3uv8RjZxu3CBVqo_iwkfad_5rc4lUG2mbmprKTXPgMC4nB6gJ2v5HAlpKOFLA5X_0lE6nCW9XYOijEoou-uxcSBI_H1jNffAQ1UDxcpJTW0gHMmvsj31WqrPfYmhZ_2beFe5OgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفوذ حنظله‌ به سامانۀ پهپادهای FBI و استخراج داده‌های محرمانه
🔹
گروه هکری حنظله اعلام کرد که به سامانه‌های امنیتی پهپادهای اف‌بی‌آی نفوذ کرده و ماه‌ها به تصاویر و داده‌های این پهپادها دسترسی کامل داشته است.
🔹
حنظله در پیام خود تاکید کرد که حتی اطلاعات مربوط به مأموران اف‌بی‌آی نیز برای این گروه هکری قابل مشاهده بوده است.
🔹
این گروه هکری با
انتشار تصاویری که به‌دست آورده‌
، گفت این تصاویر مستقیماً از پهپادهای امنیتی اف‌بی‌آی دریافت شده است.
🔹
حنظله همچنین اعلام کرد که ممکن است هم‌اکنون از طریق پهپادهای MQ-9 ارتش آمریکا، تحولات پایگاه‌های نظامی این کشور در بحرین را رصد کند.
🔹
حنظله در پایان پیام خود تأکید کرد که همواره «یک گام جلوتر از سایه‌ها» حرکت می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/441529" target="_blank">📅 03:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441528">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKe-TEAVU_J_xBQ7zK-TrecFRxaOcOrhY7pKVMnm3UBZ_m2rkqeHW5eIjhJ3KcSYyvC0cjVuf8fP--1gJEFQJZBx1NoXNmYrDZ4jU4iW9vbWN6AaIqyYF3gHu-6R_ncUPnJEWsKkvR9jW1CMMwKqgOhH_WsMk-27SuGa8mXp3b23oXWkQ3TlrrMj7ewxMwtgtAd8aEW1eM2w8e1JmqShLqWv5cPt6kWHzav2AYXMLkIIJ1DcGoP0RYngi19piqszKef2ARZCvCf64-GCwHuUbsfhG9La_1WyuInX6BgxR7xawBOCU8TRNPRBkMw7AeVryJpaTqVS1kYwn9WzOUsgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: امروز به جنگ با ایران پایان دادیم
🔹
رئیس‌جمهور آمریکا در ادعایی جدید گفت: «ما امروز به جنگ با ایران پایان دادیم و آن‌ها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند؛ این همان چیزی بود که ما بر آن اصرار داشتیم.»
🔹
وی اضافه کرد: کل هدف ما همین بود؛ این موضوع ۹۵ درصد از هدف ما را تشکیل می‌داد و آن‌ها این کار را به محکم‌ترین شکل ممکن انجام داده‌اند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/441528" target="_blank">📅 03:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441527">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">موشک‌های ایرانی دنبال انتقام از غول‌های فناوری و بورسی آمریکا
🔹
از ۹ اسفند تاکنون آمریکا، اسرائیل و شرکای منطقه‌ای دست به جنایت علیه مردم ایران زدند.
🔹
در نگاه اول ممکن است به نظر برسد که تنها ارتش این کشورها شعلۀ جنگ را روشن کرده‌اند اما بررسی اسناد مالی، قراردادهای نظامی و دفاتر منطقه‌ای ده‌ها غول فناوری و سرمایه‌گذاری نشان می‌دهد که شبکۀ پیچیده‌ای از نهادهای وال‌استریتی و سیلیکون‌ولی، نه‌تنها از برنامه‌های نظامی آمریکا و اسرائیل حمایت مالی می‌کنند، بلکه به‌عنوان مجری مستقیم، شریک اطلاعاتی و تأمین‌کنندۀ زیرساخت، در قلب این برنامه‌ها جاخوش کرده‌اند.
🔹
از اسپیس‌ایکس و استارلینک ایلان ماسک تا گوگل، از صندوق‌ها تا بانک‌های بزرگ همگی به شکلی مستند در زنجیرۀ تأمین جنگ، جاسوسی و تسلیحات هوشمند نقش دارند.
🔗
این گزارش را که با تکیه بر اسناد رسمی، تصویر روشنی از این هم‌پوشانی منافع مالی و نظامی ترسیم می‌کند،
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/441527" target="_blank">📅 02:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441526">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3_KpKWpOzympelC_-YKo7jWuwTBGn-IZX5PHl4B6LSrlB65EPhQYNAGZDQJfs2sc8E1bdKEA5dz_hrepp7K_QDSsp70pUdLrwFoEVMqTpMkTnyONu7zGGmTmJsJkJz9oDni2PYxrY-r065HjMCpTyw6PnYElpPGYxa6JDBblOxmaPVJcgiaSM7pFcUJP86z6KeFsoFevkRfBJYTmOyK15pdgPaXiVClzCaPt7h0p-vrsrEHH8qDN9jnJX9sj-E1CkWBuxpnHxdRY1rFWxxaDpJe7Jb-wNZSUqqXytm0NVOPjTX_HCCMRnagNp4CmFrug9Z-JIPk1A1WbSa9WJItYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی آفریقای‌جنوبی اولین منتقد به داوری جام‌جهانی شد
🔹
سرمربی تیم فوتبال آفریقای‌جنوبی ‌پس از شکست مقابل مکزیک در افتتاحیۀ جام‌جهانی ۲۰۲۶، به انتقاد از داوری پرداخت و گفت با کارت قرمز دوم تیمش موافق نیست.
🔹
او دربارۀ اخراج تمبا زوانه گفت: بازیکن مکزیک راه بازیکن من را سد کرده بود. این تصمیم داور بود و باید آن را بپذیریم، اما به‌نظر من آن صحنه آن‌قدر شدید نبود که کارت قرمز داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/441526" target="_blank">📅 02:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441525">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAimPLBCJn0NGzLY_og_F7AUm41axl2Ut6lNVhYyoYh6JHwmTFWZ0XUAKDdgAE7A67EVJ-xixQqRwjv5YwESyEgKx57ugX4BUyzyq4i7QmEy6p7AUHOsGoI4iDXfWdU5ziDv6A7jW6gnySAqahlS5eS4DNnzZc5NsMeDbQ7mM2tvnHSK_JtDdgHd_vj3YlmJsvSfyiwx8mfaTgrPN6xV6SymsUjHAKamDkHjRImCe44-nJkX7PTjmHWYLLH8IVGS8gIe49ir5UQV378vUFsy2cWJzTFpvtQi1ItP0qqpaPXr70JPasSQvhc8r7zwyZNwm0WTVDTc1lo01M02QzhWqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت اضطراری توسط یک جنگنده F-35 آمریکا در آسمان امارات
🔹
برخی گزارش‌های تأیید نشده حاکی است یک فروند جنگنده نسل پنجم F-35 لایتنینگ ۲ (Lightning II) متعلق به نیروی هوایی ایالات متحده در حین پرواز بر فراز آسمان امارات متحده عربی وضعیت اضطراری اعلام کرد.
🔹
ین جنگنده پیشرفته با فعال کردن کد اسکوآک ۷۷۰۰ (Code 7700) بر روی دستگاه ترنسپاندر خود، وجود یک نقص فنی یا وضعیت اضطراری عمومی را به برج‌های مراقبت و رادارهای منطقه مخابره کرده است.
🔹
کد ۷۷۰۰ در پروتکل‌های بین‌المللی هوانوردی به معنای وقوع شرایط اضطراری در هواپیما است که به کنترلرهای ترافیک هوایی هشدار می‌دهد تا مسیر را برای فرود فوری و بدون نوبت جنگنده باز کنند.
🔹
هنوز جزئیات بیشتری درباره علت دقیق این حادثه یا وضعیت فعلی جنگنده منتشر نشده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/441525" target="_blank">📅 02:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441524">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b6587e422.mp4?token=rjIiBup0hIit5r_shF8VOjTUTv7IuG1tZXj8JciW6HDxocjCAHOnqGKL6GcYS5TE7BcWofuolwAqsLbJ4CzZCOWRI0V2GFF3czAaTB9HLWbaru6X_ckLFoqibZWMFCIOxaXBo6YgShRcqPUUPW9uiFpAPSrC-VIS5srb3fT3rqAMgy3UMg4BMr1ZWJQM_WLFiTROpcErlSWb0RNBIGx597x96KOws0WvpU8n3EZ3jqqR0x57C_qrjcWdJNfJh89tvUEgmuHseoy3iOx7Z4SLDd5aE8FnsI7IevcJ9LZWe4paXkolbefE4jEpoJYu65v9pVsKWMtJoHTDZEMSDac5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b6587e422.mp4?token=rjIiBup0hIit5r_shF8VOjTUTv7IuG1tZXj8JciW6HDxocjCAHOnqGKL6GcYS5TE7BcWofuolwAqsLbJ4CzZCOWRI0V2GFF3czAaTB9HLWbaru6X_ckLFoqibZWMFCIOxaXBo6YgShRcqPUUPW9uiFpAPSrC-VIS5srb3fT3rqAMgy3UMg4BMr1ZWJQM_WLFiTROpcErlSWb0RNBIGx597x96KOws0WvpU8n3EZ3jqqR0x57C_qrjcWdJNfJh89tvUEgmuHseoy3iOx7Z4SLDd5aE8FnsI7IevcJ9LZWe4paXkolbefE4jEpoJYu65v9pVsKWMtJoHTDZEMSDac5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حق پخش جام‌جهانی ۲۰۲۶ به ایران رسید
🔹
مجری برنامۀ «جام ۲۶» شبکۀ سه، با نمایش سند مربوط به خرید حق‌پخش مسابقات اعلام کرد که صداوسیما حقوق رسانه‌ای جام‌جهانی ۲۰۲۶ را خریداری کرده است.
🔹
در ماه‌های اخیر گمانه‌زنی‌های مختلفی دربارۀ وضعیت پخش این رقابت‌ها در ایران مطرح بود، اما اعلام رسمی این خبر روی آنتن شبکۀ سه به ابهام‌ها پایان داد.
⚽️
جام‌جهانی ۲۰۲۶ برای نخستین‌بار با حضور ۴۸ تیم و به میزبانی مشترک آمریکا، کانادا و مکزیک برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/441524" target="_blank">📅 01:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441523">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
ایران اجازۀ عبور نفتکش متخلف از تنگۀ هرمز را نداد
🔹
پیگیری خبرنگار فارس در بندرعباس از منابع محلی نشان می‌دهد دقایقی قبل نیروهای ایران اجازۀ عبور یک نفتکش متخلف که بدون هماهنگی وارد محدودۀ تنگه شده بود را ندادند.
🔹
گزارش‌های مردمی نیز از شنیده شدن صدای سه انفجار در فاصله حدود دو کیلومتری ساحل از سیریک حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farsna/441523" target="_blank">📅 01:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441522">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/140d000d3f.mp4?token=aB1dynWMXx_wec7mIZ6c0OK-8cAH7SOMEOKZZ1DR0IVre9AXO9iQ4kPTuqU4Kvpf4m77sBnaz_p2tz_fUK14qZU05iG7bA9FNIPFmWX_VOZA6gtXTi0s1cX3aQ4HFPchm5IQ9A-PP1DugR_IGBgXctseRhftF5ybgHDfgg8Q5b4V7_ZKCSYGylHR04_dFnUnvn26wiMi_yMMeJrGVexN8PkVCqxWbXZFtXPbB3bQzgxRxZjOyyaEQjsQj4BV9l_iVSNsppL0onCtBJmEamP_3IJXpz7YK56m6SKWy6REzSGIzNuF3UKRXqvk794RaxmaheDYfDZt_Fc8dtFK6ptR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/140d000d3f.mp4?token=aB1dynWMXx_wec7mIZ6c0OK-8cAH7SOMEOKZZ1DR0IVre9AXO9iQ4kPTuqU4Kvpf4m77sBnaz_p2tz_fUK14qZU05iG7bA9FNIPFmWX_VOZA6gtXTi0s1cX3aQ4HFPchm5IQ9A-PP1DugR_IGBgXctseRhftF5ybgHDfgg8Q5b4V7_ZKCSYGylHR04_dFnUnvn26wiMi_yMMeJrGVexN8PkVCqxWbXZFtXPbB3bQzgxRxZjOyyaEQjsQj4BV9l_iVSNsppL0onCtBJmEamP_3IJXpz7YK56m6SKWy6REzSGIzNuF3UKRXqvk794RaxmaheDYfDZt_Fc8dtFK6ptR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سپهبد شهید حسین سلامی: آرزو دارم به شهدا و حاج‌قاسم بپیوندم
🔹
در پیکار حق و باطل سرانجام حق پیروز می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/441522" target="_blank">📅 01:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441521">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9NY74aHKxpv3CMdHOmJ2tzhWCtEWOZIrKBvIp43JqXyJibyEyAQmEO08UrZG4rGujb4CmPOBBmXUiISJlwkjuxJPdnyxxjPvTKDh6dcuQrU71ga25n25fuQYihoatGEbx_c8qebsd9jd2BXbLQ04CiVQd_uUkATlg3PPsRqWw4w_RJDdcWDWpW_NpHVJdxT5PLqSRdeJMnlkgjtXUtxIMTDq05l2cW5zv7B9cKvDSYdIGH7j8c25AEsSYJg6yZzvx7kqYxAzEs1uoS9yjRC9_ecFLpkfixgbTC9XZ9zLu9PN2jTiXzh8f9zQgJTWmkMlbqeGfCKCfrwCex1eNTCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ اخراجی و ۲ گل در افتتاحیه میزبان جام را با برد شروع کرد شروع فاجعه آفریقای جنوبی
⚽️
جام‌جهانی ۲۰۲۶ مکزیک ۲ - ۰ آفریقای جنوبی    @Sportfars</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farsna/441521" target="_blank">📅 01:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441520">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVmtSA4Wh9YSIWSj9wgK_TJtoCqFXcagWP3qyixOxJFjj1NXO99u_XMJ2VPEEL_0Rwa7rsYlGiBFCgLGDzdBT44vMZpW83ONAfPo9cgCcZ8POUcQFAvI20OK0CGKLKotgXwp81o1-Utrq6A68PfmwlSpQfYeflK7sKwMDyJGGoTN43AZD2Kmounb1jFRHZcXtYeiXeAo06P1YXifmXwaOQFaI67xsIs8BC2VqE97HPRqnoe5926EzRAw8ow193Drn15dHFgWRBSOPVhArLFCIdi3vUyNP-2-nwg4rz2JDjzp8HMuuIICBpn7eEhv_D7Whqb5DLYmXqdC3fFzM0vCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: حملات آمریکا به کشتی‌های تجاری و راهزنی دریایی، تهدیدی جدی علیه دریانوردی بین‌المللی است
🔹
سخنگوی وزارت خارجه: حملات بی‌رحمانه آمریکا به کشتی‌‌های تجاری هندی که موجب قتل حداقل سه شهروند هندی شده است، نتیجۀ سیاست سرقت مسلحانه و راهزنی دریایی دولت آمریکا است.
🔹
با خانواده‌ و دوستان ملوانان هندی کشته‌شده ابراز همدردی می‌کنیم و به مردم و دولت هند تسلیت می‌گوییم.
🔹
جامعۀ بین‌المللی باید آمریکا را به‌خاطر رفتار قانون‌شکنانه‌اش پاسخگو کند؛ رفتاری که تهدید علیه صلح و امنیت جهانی است و آزادی دریانوردی را به خطر انداخته است.
@Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/441520" target="_blank">📅 01:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441519">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-XSFP2UU9uX88u_xciQ1TvMTPgfQcTL_Lok8J9o0BtXErRtYZjfsWvk_VTZOsP7DghQhJhO68oZUkXQ6scDqDdeBCibswaynm4PVTwMEaVFqVHY4OSCIgmGT_o0u9RApU_FHkHOSPE7xCIP74-9Hiv_n7NdDBunNcFLJl9Xwa3gJAcHSPq1AOv4LFDibay72qQkn3l6ZBuP9-2MfJvXQrhvFJF_E7XDn2WP9Z4q3R9nVWcQG5PCAzhdi2q4hMOZDVjKTjyiTKZ1bxwWZXXcW9yUGLlboXlZR5lXGA-nXOwfe-sftxJNALcEyoHoEZnS2jD7n5MXnP7s9wGI3Bbt9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ اخراجی و ۲ گل در افتتاحیه میزبان جام را با برد شروع کرد شروع فاجعه آفریقای جنوبی
⚽️
جام‌جهانی ۲۰۲۶ مکزیک ۲ - ۰ آفریقای جنوبی    @Sportfars</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/441519" target="_blank">📅 00:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441518">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuVK5bFUBeebSbVszXNm2FYMm8In33JKNyrKH3O2mbkvy14thhe3MjOPQYgaT2B0Fy4Gax9djXGHi5aZ8P3U-QoIg4Ydb4VQbKIEFpiAHObSel-ZBeJ-VeW41dsAkfCYy8G_XtEngfZCz0_ILZ04xWmfPgl2fG8NTqSIjskmHhvrqy96-EA0chwJ8h7D1EDtSx5uG6PORhHMpc8f81B4APfEqaWxt1BR3gex67socGqq2skwrZ6REuiRTMIUBTT5QkDnr-ZNg4yXIoTDBWqpHn06df01rQjPefCx8y23a9GKMMdxMmmcBzzinVJKJN38TChipMbaf-xLCaEfVJXEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ اخراجی و ۲ گل در افتتاحیه
میزبان جام را با برد شروع کرد
شروع فاجعه آفریقای جنوبی
⚽️
جام‌جهانی ۲۰۲۶
مکزیک ۲ - ۰ آفریقای جنوبی
@Sportfars</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/441518" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441517">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxWJmEwesfEKFlJGupdJVWUG2ft4onNggyD0dZCftVU2tSM79E6OUHsrHX6DTmPEyoIuj13x4ARBI_cXbEA8p09p-xJT3nXIT2b1GyXqegz4Nn1y564wWLLiaN3mTIz9oNkkbkPJK7BPoGY_eoF63X5hp8GWtCEtAmWjYnUyZ3vCccdk_xgB_od7GwlqroBrvbI_5jyUZmIMrM3Qo5pE_51yMPHMHoXNMZPNCRMWE9hucMhHO1BJmGc91RP--R4Ny5tNwJe-Wq3aPt0U0Jmoy7v2eyNtZ86n1qzJWHtFdKovGmEAED0rBNbylDqBh4K-f2nuQLgpGTGsoRPpEwxQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست ایران در دومین بازی
اشتباهات فردی کار دست شاگردان پیاتزا داد
لیگ ملت‌های والیبال
🏐
ایران ۰ - ۳ بلغارستان
🇮🇷
ایران: ۲۱ | ۱۹ | ۲۳
🇧🇬
بلغارستان: ۲۵ | ۲۵ | ۲۵
@Sportfars</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/441517" target="_blank">📅 00:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441516">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9017f90840.mp4?token=YB0U__2AEbB_W63WHXuEUVUsqnceLb8z-fmudDKEsTagNVc5Xr2UBnN9P8Ur_9EaiCPUaVagbE_2P4PzDJw5wzWCWjiB8ouqokptyFDTyg8cEi-upkqAeNgpRVdQ4KL6oL_mpOrFLaA-7e4VKd1zLTlQaNC9mVamqQcJ4deZXw6IVS9vKZAvnKK0YjYn1VcMzJT182tKtgSKL90xQ-sRqPaQRcF1WFaJMKCy2QY5e5KdFQ3Z9YJ0TSrQKbrBlPz3t0i-3chHSCorl1MVAdJbnHhqK-t_S9cciyfEAI7xMT6X8f7BmEhDz_Cf6OJW4RsTmi90QkPwdLrsr4wWj0EqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9017f90840.mp4?token=YB0U__2AEbB_W63WHXuEUVUsqnceLb8z-fmudDKEsTagNVc5Xr2UBnN9P8Ur_9EaiCPUaVagbE_2P4PzDJw5wzWCWjiB8ouqokptyFDTyg8cEi-upkqAeNgpRVdQ4KL6oL_mpOrFLaA-7e4VKd1zLTlQaNC9mVamqQcJ4deZXw6IVS9vKZAvnKK0YjYn1VcMzJT182tKtgSKL90xQ-sRqPaQRcF1WFaJMKCy2QY5e5KdFQ3Z9YJ0TSrQKbrBlPz3t0i-3chHSCorl1MVAdJbnHhqK-t_S9cciyfEAI7xMT6X8f7BmEhDz_Cf6OJW4RsTmi90QkPwdLrsr4wWj0EqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تنگهٔ هرمز به‌دلیل اقدامات غیرقانونی آمریکا همچنان بسته است
🔹
کشتی‌ها باید مراقبت کنند برای اینکه امکان تردد ایمن وجود ندارد. @Farsna</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farsna/441516" target="_blank">📅 00:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441511">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🎥
سخنگوی وزارت خارجه: ابتدا باید مراجع ذی‌ربط نظام دربارهٔ جزءبه‌جزء هرگونه تفاهمی به جمع‌بندی برسند‌
🔹
به‌محض اینکه به جمع‌بندی نهایی برسیم رسماً اعلام می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farsna/441511" target="_blank">📅 00:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441510">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">واکنش طنزآمیز کاربران به تناقض گویی ترامپ درباره تنگه هرمز
🔹
تناقض‌گویی جدید دونالد ترامپ درباره تنگه هرمز و توافق با ایران، به سوژه داغ کاربران شبکه‌های اجتماعی انگلیسی و آمریکایی تبدیل شده است.
🔹
ترامپ صبح امروز مدعی شد «آمریکا کنترل تنگه هرمز را در دست گرفته است»، اما ساعتی پیش اعلام کرد که توافق با ایران «نهایی شده» و به این ترتیب تنگه هرمز باز می‌شود. کاربران با برجسته کردن این تناقض، می‌پرسند: «اگر تنگه هرمز باز می‌شود، پس چرا صبح گفتید در کنترل ماست؟»
🔹
ایران تأکید کرده که هیچ توافقی نهایی نشده و موضوع همچنان در حال بررسی است.
@Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/441510" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441509">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3137e1f2c1.mp4?token=o1JNzAkBwmUFaauSfG_ceO5UoIOuCyVAiQkOs-NTbphn4Gad1mxfP9Irah_GLE-XaiTcmMeSOrFnAMcmtb-feSo6wXpcNQTfiG9q8H5OmMiLG_Ow8lIcSd0DKhp1jEEcwcajDVYG6UI5jzVhQliinyXl3rk1fgDKVa1jkH87TS8gYy8cOiSBOOJS1T-dcLe6Htf_J-ZngcN52SYx3C27Af2AVSraIWwvml_vsa18ehC_c7tpSTOeYCo00Oa4wSGaGDmlPlFZpmrd9_swLhd4MvWXw27s2Aji_YoFTxrfJI1BEaJ9RggAmq07dWNpDw6j7dgBmhG-wo2nHcLz4K0j4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3137e1f2c1.mp4?token=o1JNzAkBwmUFaauSfG_ceO5UoIOuCyVAiQkOs-NTbphn4Gad1mxfP9Irah_GLE-XaiTcmMeSOrFnAMcmtb-feSo6wXpcNQTfiG9q8H5OmMiLG_Ow8lIcSd0DKhp1jEEcwcajDVYG6UI5jzVhQliinyXl3rk1fgDKVa1jkH87TS8gYy8cOiSBOOJS1T-dcLe6Htf_J-ZngcN52SYx3C27Af2AVSraIWwvml_vsa18ehC_c7tpSTOeYCo00Oa4wSGaGDmlPlFZpmrd9_swLhd4MvWXw27s2Aji_YoFTxrfJI1BEaJ9RggAmq07dWNpDw6j7dgBmhG-wo2nHcLz4K0j4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: اعلام تاریخ برای امضای تفاهم، گمانه‌زنی رسانه‌ای است. @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441509" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441508">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: بخش عمدهٔ متن تفاهم نهایی شده اما مشکل این است که مواضع ضدونقیض آمریکا باعث اخلال در روند می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/441508" target="_blank">📅 00:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441507">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: به‌دلیل اقدامات غیرقانونی آمریکا در تعرض به ایران، روند دیپلماتیک هم تحت تأثیر قرار گرفته است
🔹
میانجی‌ها فعال هستند و ما خیلی شفاف به آن‌ها مواضع‌مان را اعلام کرده‌ایم‌. @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441507" target="_blank">📅 00:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441506">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: اگر قرار بود ایران تحت فشار و تهدید از مواضع اصولی خود کوتاه بیاید، یک‌سال قبل این کار را انجام می‌داد. @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/441506" target="_blank">📅 00:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441505">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکایی‌ها در این چند روز تلاش کردند که مطالبات و خواسته‌های غیرمعمول تحمیل کنند اما ایران نشان داد که به‌هیچ‌‌عنوان تسلیم شرایط و خواسته‌های نامشروع طرف مقابل نمی‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441505" target="_blank">📅 00:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441504">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b0c3fae3.mp4?token=aV7IzzOddT4QFE4Ey0cZiwiGInrwvKZyUtT6hIeELagFk27x6M_dMVBMWztVWfGgaeAJRBpFmQPIQ1eviyn07og_Gyd6OYjIsjxO81n3dqHX_ckepu5t7rwmpoLupkgBKvUVan_DxQSYmozEGLgNt7wfGqGpQK7iarivLqUrSdL_KFXAdjVKfcqV9GeGa2ACNjFOXjFMcT_gd6lNp5GXUyxW5fKAXR779_ZzJV4snfbtN_v4Gj4YJLsJmTdOI95nUuID5_qFgnOPDitASjguxNZEfTxChAeXYplqejaDw7IpllsaiOCwyuWdPZuF_LAecQVY0tHislQ2JFYgrtGGOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b0c3fae3.mp4?token=aV7IzzOddT4QFE4Ey0cZiwiGInrwvKZyUtT6hIeELagFk27x6M_dMVBMWztVWfGgaeAJRBpFmQPIQ1eviyn07og_Gyd6OYjIsjxO81n3dqHX_ckepu5t7rwmpoLupkgBKvUVan_DxQSYmozEGLgNt7wfGqGpQK7iarivLqUrSdL_KFXAdjVKfcqV9GeGa2ACNjFOXjFMcT_gd6lNp5GXUyxW5fKAXR779_ZzJV4snfbtN_v4Gj4YJLsJmTdOI95nUuID5_qFgnOPDitASjguxNZEfTxChAeXYplqejaDw7IpllsaiOCwyuWdPZuF_LAecQVY0tHislQ2JFYgrtGGOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: آمریکایی‌‌ها درحال القا هستند که جمهوری اسلامی تحت فشار به توافق رضایت داده است، در حالی که ما به هیچ عنوان از خطوط قرمز خود کوتاه نخواهیم آمد. @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/441504" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441502">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمدهٔ متن نهایی شده بود اما آمریکایی‌ها مواضع خود را تغییر می‌دادند
🔹
ایران ثابت کرده که در آنچه به‌عنوان خط قرمز معین کرده، مماشاتی ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/441502" target="_blank">📅 00:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441501">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمدهٔ متن نهایی شده بود اما آمریکایی‌ها مواضع خود را تغییر می‌دادند
🔹
ایران ثابت کرده که در آنچه به‌عنوان خط قرمز معین کرده، مماشاتی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/441501" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441500">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67e82794b.mp4?token=b2BTH7gwQp3CuNHwXPk2BzGEoHP28_tkC9UetITFQo3RDDS4Xmo1gt2E2fXP1usLmlLj6oEOqyKVblqSVC5QyTFfDm-5Mw30qX3-7ZpQQMPOKUpB9_0kU8tTLjti2BRXvcVqLax36tsKX7J-YaxYsAtvQgOaq9XmAP6VOVLXc-mc7TDNgno-oit1Z0oM6CHOyFSkG-1yv-G3X7XCNM0L7Ana7aUw0-NJEOsz60kF4CgKe725vpsVNWf-xSg4itLv50PJck5KIlBz6R_Ken0hPwG2mvim8OUfDFR3X5J2IOMQWGaLpkusaYj5lqpNNKp1ECIKVaLFUlJzQLV-U82hgSq-n4Grs0B0pE4jmMpIcFdDJLV_tXSmUfxAOTktpebBAZ-v728eZnj9oKzAnxSQHa_VdcyzT1s1bwopkAqS55yGq6U4z3D3pIlWVoE_MhvqMcm1dJ_WCaHjaThCPszlpKqHYt4n308HOeXVmUczMy1P7MZ6HGCrjceGagigx2-aU6gL3mbNValnw1jLiE5GdzNX0GHxlJhyFpAVSfR0P91er8iIzCE2irzIke08G-WpUYuGq0LdH2gAe-6ZPgJrn6SKqJ7_BJ-2SHXAybgbn72U7WrzuRTjhtfG6cFqaug4QaVbsMSsa7g3DA82EPK_YGnyVl4W-wQq9SGzO6V4CJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67e82794b.mp4?token=b2BTH7gwQp3CuNHwXPk2BzGEoHP28_tkC9UetITFQo3RDDS4Xmo1gt2E2fXP1usLmlLj6oEOqyKVblqSVC5QyTFfDm-5Mw30qX3-7ZpQQMPOKUpB9_0kU8tTLjti2BRXvcVqLax36tsKX7J-YaxYsAtvQgOaq9XmAP6VOVLXc-mc7TDNgno-oit1Z0oM6CHOyFSkG-1yv-G3X7XCNM0L7Ana7aUw0-NJEOsz60kF4CgKe725vpsVNWf-xSg4itLv50PJck5KIlBz6R_Ken0hPwG2mvim8OUfDFR3X5J2IOMQWGaLpkusaYj5lqpNNKp1ECIKVaLFUlJzQLV-U82hgSq-n4Grs0B0pE4jmMpIcFdDJLV_tXSmUfxAOTktpebBAZ-v728eZnj9oKzAnxSQHa_VdcyzT1s1bwopkAqS55yGq6U4z3D3pIlWVoE_MhvqMcm1dJ_WCaHjaThCPszlpKqHYt4n308HOeXVmUczMy1P7MZ6HGCrjceGagigx2-aU6gL3mbNValnw1jLiE5GdzNX0GHxlJhyFpAVSfR0P91er8iIzCE2irzIke08G-WpUYuGq0LdH2gAe-6ZPgJrn6SKqJ7_BJ-2SHXAybgbn72U7WrzuRTjhtfG6cFqaug4QaVbsMSsa7g3DA82EPK_YGnyVl4W-wQq9SGzO6V4CJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش مردم پیشوا به تهدیدهای ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/441500" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441499">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee25fa2f5.mp4?token=i8J7u_XSevu2mzFYAdIYRLx25QJfeyyFI1BwG_kl2ak7b3tHbCSfWyx8WLh5JwJil-5BY9LSozPnDSJtrGQKidhZ16zu8kKbE6CdlZlx5KyshePP-TQ9iiLXCQ7AhhFRUx8SsKdHhMTo4cSSUFkdYJCW_uqhXfe62Zh-vq6Bd3eyDtePbnjDeiAm73rvKf4K1BaZPK7iqOzbFpYNl7RckCt6aw2NXJ5y6pDMREilE-xf4xPQqYr19hd6CXYqZ1Y0SZTSxjOPMhHiqqa1nH9w1-Hsmh5HdYs45lrDtM-IH9pCkY8ciStYPXTV8VY66Q9krB5uj9uV8OoTGTm86Ia8gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee25fa2f5.mp4?token=i8J7u_XSevu2mzFYAdIYRLx25QJfeyyFI1BwG_kl2ak7b3tHbCSfWyx8WLh5JwJil-5BY9LSozPnDSJtrGQKidhZ16zu8kKbE6CdlZlx5KyshePP-TQ9iiLXCQ7AhhFRUx8SsKdHhMTo4cSSUFkdYJCW_uqhXfe62Zh-vq6Bd3eyDtePbnjDeiAm73rvKf4K1BaZPK7iqOzbFpYNl7RckCt6aw2NXJ5y6pDMREilE-xf4xPQqYr19hd6CXYqZ1Y0SZTSxjOPMhHiqqa1nH9w1-Hsmh5HdYs45lrDtM-IH9pCkY8ciStYPXTV8VY66Q9krB5uj9uV8OoTGTm86Ia8gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مزدورران رسانه‌ای دشمن در هرمزگان به دام افتادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441499" target="_blank">📅 23:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441498">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b89f257c.mp4?token=n5dPVKwM6-IdKPYvlqX5bjpro33huofKvN4SETpi1AzUMcgt0Vd3KSyDzfwMa5hSrDSW6sdlfJ6BDQxqISoiQxNjXG5jgJbvuSGxg6wEb2_fuRy0gmzXuivFtV9QJ-kzU-MPrGpsH8yUdTQjAbe0txAr6K5gVIEgN9LEbHCtXp2DhRKXq7ZhSuUs9_Hud5OgRgGvsAxIDYZZHzI1r_FvD8su2ENsVdAN137SSsEO9GaljbtmcntpvlG9b0vxL0sG_7Eh7scMjnsH5oW25tMGnFd_WXnAayEvJQipKFtfzB7359j9mBWE1hElbOFKn7-Ytb2kOxJtnuX2w_eccFsXLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b89f257c.mp4?token=n5dPVKwM6-IdKPYvlqX5bjpro33huofKvN4SETpi1AzUMcgt0Vd3KSyDzfwMa5hSrDSW6sdlfJ6BDQxqISoiQxNjXG5jgJbvuSGxg6wEb2_fuRy0gmzXuivFtV9QJ-kzU-MPrGpsH8yUdTQjAbe0txAr6K5gVIEgN9LEbHCtXp2DhRKXq7ZhSuUs9_Hud5OgRgGvsAxIDYZZHzI1r_FvD8su2ENsVdAN137SSsEO9GaljbtmcntpvlG9b0vxL0sG_7Eh7scMjnsH5oW25tMGnFd_WXnAayEvJQipKFtfzB7359j9mBWE1hElbOFKn7-Ytb2kOxJtnuX2w_eccFsXLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلوهٔ اتحاد و همدلی مردم مشهد در تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/441498" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441497">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_AF3kQH8lDY87HtURjBuVoS9-8VwJAsS8FFFO1avm8gaxcAfNr794ygfRUInHVBm0n6L0KjVhW_Dh-Lye3RnIDvEjsnjsOht-rYpkLi-B1c6zF3BLP0f18pFfOvAix9c0BdetpdIS1gSNjT4vPSen6Lb1IJvDnBYm-j6rGI1LZmzyo2YMGjjeYk-apJaUp5uI-0wROSiXWnMAWU8sb6UEWr3cPdQs41De-4WMF0bETH9p_3NkvDX1015uNWPHdhu1y5E8OEGGGOJ9I8otOaABSkCIb7GjNN9dN6j_sK7Ajl0BwnFIGozugqYud6VeU5XJ3eK8u1ENuV4NobA-33tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین رتبه بندی شبکه های صداوسیما در میزان مخاطب؛ سه، آی‌فیلم ،خبر
🔹
جدیدترین نظرسنجی در خصوص پرمخاطب‌ترین شبکه‌های تلویزیونی  توسط مرکز افکارسنجی متا در سراسر کشور برگزار شد.
🔹
مطابق این نظرسنجی‌ شبکه سه در رتبه اول پربیننده‌ترین شبکه‌های تلویزیونی حضور دارد.
🔹
شبکه‌های آی‌فیلم و خبر نیز با فاصله کمی در جایگاه دوم و سوم قرار دارند.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441497" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441496">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8LC_dHgsmAiR0P8CBWDqAcWpBOurWDUsof46n7PeycHYv8dK0yqx0kwUbc9uu5_AkbYBWAE2q3PelxLsh57q2-MYQBcAId4LDw4eMMdnxWmrxNP06RDHPIa3Tjuf74BE_r1jK5j0JoxF-kC7iKuIaDXfS_ZukyHFZh5thzhPHdCN4g76Z7IIqz8pD54Cp9y7b2kC7rvPfR19wqMnA4d-vYmjoXeHXT5oksp7SEegvVJmaXPlWXyeVlZojLOvdJqwypWfR67qJPjjcyf8qStHXlA0I3xcEYtuP7vvVxMHbCriQwzsb97e6-ED713nQfLAddUWNxeA0WuGU1tQL6nZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
جام جهانی ۲۰۲۶ از همین حالا در «همراه من» شروع شده!
برو توی اپلیکیشن *«همراه من»*، بازی‌ها رو پیش‌بینی کن و جوایز هیجان انگیز ببر
🤩
🎁
۵ گیگ اینترنت رایگان بدون قرعه کشی
🎮
هر روز یک  PS5
💵
۱ میلیارد تومان اعتبار کیف پول در روزهای مسابقه
📱
قرعه‌کشی بزرگ S26 Ultra به همراه سیم‌کارت ۰۹۱۲ برای سه نفر برتر
✨
3 کمک هزینه سفر به عتبات عالیات در هر بازی تیم ملی
پیش‌بینی از تو، جوایز میلیاردی از همراه اول!
🔗
https://www.mci.ir/-9VEQ3HH</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441496" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441495">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/441495" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441494">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc58d63ac4.mp4?token=sYFsZHXgbHLR0nc8TR_ODjoUsM3DPYev8YMds649wlBvxYdFZyGFLUI_Xg90QmNhU1LTn-SMngdY3dWdruEdh3hCelOPPgs00kgA3JIsfEtZNQDKHgZwZxm5urYgkKofgsl4Ja_Ctj7YCrfejwFbaqYpmxgNaL9FnI_QtWmA7I9aqQb3LXnyIfGRhit9vjsRU5fQtKRArv6oJL2gqcio-idErRcCusL6hnrhrSGfVQw2OGOiL3MVtfqVIhRxji8oDG0RRTb87lkGDGUC8Jry2x6OMkWAHnOb8HxtsO975kPpLmfuJzSjFBZo1A80s2sJscDmVszhwuVNKlRmv8QsXV1nkvrUQNYKk5UJAI2ICvAjpo1w_ncuDt4zwDb8YCJZ9nFytP4p-fiLTsNKzkIax66Qg89ZjDvQiYTDZk_5i_vXanCTOE92VWSLv1jg-tkjelwnniQFD4lDvoYbVk5xVBp9uooivNNeNO5078ouysCjhfrZxiJEKunTr7-3m0dmzgK5q9vSZ2c-GkIcoGj41DBtPYPFaKbs5DK6yytZL9_sP8xkNC4aN33DtsAB_YzyRDDYYnlwB9SCpoiXtjYiE2fkYXP_PLyg34S4SJge2qs-ZFYgNt0o8ITv6epbZ9UyWRq4PZ-EMPFsStOEkWQOzmwm86zQ9rqWQUB8PI_i1YI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc58d63ac4.mp4?token=sYFsZHXgbHLR0nc8TR_ODjoUsM3DPYev8YMds649wlBvxYdFZyGFLUI_Xg90QmNhU1LTn-SMngdY3dWdruEdh3hCelOPPgs00kgA3JIsfEtZNQDKHgZwZxm5urYgkKofgsl4Ja_Ctj7YCrfejwFbaqYpmxgNaL9FnI_QtWmA7I9aqQb3LXnyIfGRhit9vjsRU5fQtKRArv6oJL2gqcio-idErRcCusL6hnrhrSGfVQw2OGOiL3MVtfqVIhRxji8oDG0RRTb87lkGDGUC8Jry2x6OMkWAHnOb8HxtsO975kPpLmfuJzSjFBZo1A80s2sJscDmVszhwuVNKlRmv8QsXV1nkvrUQNYKk5UJAI2ICvAjpo1w_ncuDt4zwDb8YCJZ9nFytP4p-fiLTsNKzkIax66Qg89ZjDvQiYTDZk_5i_vXanCTOE92VWSLv1jg-tkjelwnniQFD4lDvoYbVk5xVBp9uooivNNeNO5078ouysCjhfrZxiJEKunTr7-3m0dmzgK5q9vSZ2c-GkIcoGj41DBtPYPFaKbs5DK6yytZL9_sP8xkNC4aN33DtsAB_YzyRDDYYnlwB9SCpoiXtjYiE2fkYXP_PLyg34S4SJge2qs-ZFYgNt0o8ITv6epbZ9UyWRq4PZ-EMPFsStOEkWQOzmwm86zQ9rqWQUB8PI_i1YI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعثت مردم و هنرمندان در خیابان‌های شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441494" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441493">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سریال استعفای وزرای انگلیسی ادامه دارد
🔹
پس از وزیر دفاع، وزیر نیروهای مسلح انگلیس ال کارنز نیز از سِمت خود استعفا داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/441493" target="_blank">📅 23:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441492">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
حزب‌الله: پایگاه «نمر الجمل» اسرائیل را که به‌تازگی در جنوب لبنان ایجاد شده بود، با پهپاد هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/441492" target="_blank">📅 23:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441491">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4460115fd.mp4?token=qWMG94Qj_SjDu55053-_Gmy5AzZMCBN3Z_plL3FrLTp4GLYj5Juu5zotWlbJot552AwXeKtsSD4VfWW9uM4T8hZSsEKz8wYGyLoM_jBURnTOX4wwL6Yo7M1-08MMO9XtLeATF9VOwDBfwjJ35T3MCflDgtANuREFaRhGGjURDnQk8wrIgXJfmXuaNIxwY_uTsB-ERBPl6zc07xNOy5UPnnFWO43NT48DJ9USU5-z2ygGE0YALzaJFvixQ_mse_mZMaHtTzjguh-Ac6-jxfIla-XkeMjDPsK8BQP34YDxWDyuex5z9vGyRVlUs7Jmov7OvQbsLZXGA6KTNuygut0FLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4460115fd.mp4?token=qWMG94Qj_SjDu55053-_Gmy5AzZMCBN3Z_plL3FrLTp4GLYj5Juu5zotWlbJot552AwXeKtsSD4VfWW9uM4T8hZSsEKz8wYGyLoM_jBURnTOX4wwL6Yo7M1-08MMO9XtLeATF9VOwDBfwjJ35T3MCflDgtANuREFaRhGGjURDnQk8wrIgXJfmXuaNIxwY_uTsB-ERBPl6zc07xNOy5UPnnFWO43NT48DJ9USU5-z2ygGE0YALzaJFvixQ_mse_mZMaHtTzjguh-Ac6-jxfIla-XkeMjDPsK8BQP34YDxWDyuex5z9vGyRVlUs7Jmov7OvQbsLZXGA6KTNuygut0FLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰۳ شب از بی‌قراری گنابادی‌ها برای وطن
گذشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/441491" target="_blank">📅 23:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441489">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌ تکمیلی: روایت ترامپ از «پذیرش ایران» در برابر واقعیت میدانی
🔹
همزمان با عقب‌نشینی تاکتیکی آمریکا از اضافه‌بندهای جدید به پیش‌نویس توافق، دونالد ترامپ با افزایش لحن تهدیدآمیز در شبکه‌های اجتماعی، تلاش می‌کند روایت «تسلیم ایران در برابر بمباران» را بسازد؛…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/441489" target="_blank">📅 23:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441488">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdpm3Tm1AswYtsW3dBTjUzpcArKVpXG0sVqgerRXANsAOvg9grXZTIgrBD_TerG4MuoenzZJErCFVlV5UHMEM3Ysj5iBjDsWan6YC6kiyB9Vi97OU1j_-lp0HAVoYbOhE7Y0gXVBqJoW_Rw9f5A5at3iuVxSiCjW9dPrRxrR-YHUlclQgALyu5y-qwzd0snixX25Gbhby12c003R9vV0mLMykW5BGWTuXFQiW3Joqf999cvG-Hdiwj3uVBWC3sl23mCx4Nn28kzGtDhjoRkpnukfgHVJDadTqJTr4W832eYz59F8dCruyfrA5g4xplyllG6qo7Ys_xLkEkjz0U1zoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید جنبلاط: صلح با اسرائیل غیر ممکن است
🔹
ولید جنبلاط، از رهبران دروزی و رئیس حزب سوسیالیست ترقی‌خواه لبنان، در گفت‌وگو با الجزیره گفت: «ما امروز با نقشه‌ای جدید از مرزهای اسرائیل روبه‌رو هستیم.»
🔹
وی با ابراز نگرانی از حجم انبوه آوارگان جنگی که از جنوب لبنان به سمت مناطق شمالی فرار کرده‌اند، گفت: «باید حداقل تضمین‌های اجتماعی لازم را برای پناهجویان فراهم کنیم.»
🔹
جنبلاط با اشاره به تحولات منطقه اظهار داشت: «لبنان امروز از آنچه در کشورهای خلیج فارس رخ می‌دهد، جدا و مصون نیست. در شرایط کنونی، دور نگه داشتن لبنان از تحولات و درگیری‌های منطقه‌ای بسیار دشوار است و ما باید واقعیت‌های موجود را بپذیریم، خود را با آن‌ها تطبیق دهیم و مقاومت کنیم.»
🔹
جنبلاط سپس به آمال و آرزوهای برخی در لبنان برای عادی‌سازی روابط با رژیم اسرائیل اشاره کرد و گفت:«هیچ امکانی برای دستیابی به صلح با اسرائیل نمی‌بینم.»
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/441488" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441487">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlA2uWtgmGF2YN0LBBOsgjeqyMshzJkR21MshkdhMRcWcWzh1Sj7ijXmHrkWPcltCnDFUv9n_yWq-AppvRrA8IOvu1oQ7UVkng25m09Ra-9KcTqtEOIrbr4WmB0rntzQHzL-gHYlb4I6_Zcg7iBoshzViDgl2EZ_vKwpC6HRR6ubCs5eW4eCES1dBPRGwE5hRSocpGGrMIfToVpOaITcExL-pTGuzX02sqwuaymCfyXFDO8aWmm5iZMpWFcTkzfMwzJ8ZUJtp9FPTjSVDsbjP3KkNOigeHrP6ldSI0K6dHTslAxI-mKQSjRqrhFOsnR_64k_HtKedbQ_NRNelNsyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهسته برانید؛ «هلیا» و توله‌هایش از جاده مرگ می‌گذرند
🔹
در حالی که محیط‌بانان حیات‌وحش این روزها چشم به تحرکات هلیا و سه توله‌اش دوخته‌اند، محور عباس‌آباد-میامی بار دیگر به کانون نگرانی دوستداران محیط‌زیست تبدیل شده است.
🔹
این جاده طی سال‌های گذشته بارها…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/441487" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441486">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c897c20c51.mp4?token=XEos2oWKlif_LYbtEF5MOCpTysfpySfudonGXhlLanEaJZat87CxJNBPhack1R4smBVq2pMi6ZaamoxAyn9gNd5yOGy6pPVGlx0FCZNE5zHtcKoY_Eszdgr3tviZ5DxxC36rNnx1h-mVnblpNPe_oZoc0jVRgru8xy8GJSoMSY-ihHgjzIUR_ODsMcbuhjeBxXrGmdXD14JiqwtX0DY7wJQl-4ClNDQt7TunAxv3v139clw_L46MhHnXUhz5yMW6LiPhvxzAsoIj0On_qi3RtFH_bMxtubhPt9YEavX0vYSvlHkjjq7sI9Ae3e_80UV1uc4GuBSP8Bfj7EI8jb5iaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c897c20c51.mp4?token=XEos2oWKlif_LYbtEF5MOCpTysfpySfudonGXhlLanEaJZat87CxJNBPhack1R4smBVq2pMi6ZaamoxAyn9gNd5yOGy6pPVGlx0FCZNE5zHtcKoY_Eszdgr3tviZ5DxxC36rNnx1h-mVnblpNPe_oZoc0jVRgru8xy8GJSoMSY-ihHgjzIUR_ODsMcbuhjeBxXrGmdXD14JiqwtX0DY7wJQl-4ClNDQt7TunAxv3v139clw_L46MhHnXUhz5yMW6LiPhvxzAsoIj0On_qi3RtFH_bMxtubhPt9YEavX0vYSvlHkjjq7sI9Ae3e_80UV1uc4GuBSP8Bfj7EI8jb5iaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرثیه‌خوانی امشب محمود کریمی در رواق کشوردوست
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/441486" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441484">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
مراغه در مدار ایستادگی؛ صدوسومین قرار خونخواهی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441484" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌  منبع آگاه: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
🔹
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران به خبرنگار فارس گفت.
🔹
رئیس‌جمهور ایالات متحده ساعتی قبل در پیامی…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farsna/441483" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎥
عصبانیت وزیر جنگ آمریکا از مقاومت ایرانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/441482" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441481">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f20a7fd97a.mp4?token=ClQPh8d5VLvuqgs-VWkKaHVSV3z7Rjxzk5dIlpUM1NLDB4K16OVgcjLD21E8ozoeSfS0XzTMpiW37sdfV6H0Y3IefD2I-hwtJzzZRFYg-dCeKJYZ577k6F3YKc2PggvUlNZJN-5YLpiuj6H_R5Qpe6sLAd0VDQJpCV3FR8KMrM-Ue9x4Q4LpaBqv9_NtVDmS0q6AEs7MZ22up2CiAWh_DLpMoD6Jy0er4MntLeHhsg0rl_xQXWAUelyyvVElwXwr-JefBrsc9eMz8RvjsWwWYIR6zLECYPY-tfwoCFX7f9Koc8Wu8_gr0MEYBtU31PBO9EFDRf1KjmWchKGd6xKr1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f20a7fd97a.mp4?token=ClQPh8d5VLvuqgs-VWkKaHVSV3z7Rjxzk5dIlpUM1NLDB4K16OVgcjLD21E8ozoeSfS0XzTMpiW37sdfV6H0Y3IefD2I-hwtJzzZRFYg-dCeKJYZ577k6F3YKc2PggvUlNZJN-5YLpiuj6H_R5Qpe6sLAd0VDQJpCV3FR8KMrM-Ue9x4Q4LpaBqv9_NtVDmS0q6AEs7MZ22up2CiAWh_DLpMoD6Jy0er4MntLeHhsg0rl_xQXWAUelyyvVElwXwr-JefBrsc9eMz8RvjsWwWYIR6zLECYPY-tfwoCFX7f9Koc8Wu8_gr0MEYBtU31PBO9EFDRf1KjmWchKGd6xKr1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پرچمی که حذف‌شدنی نیست
پرچم کشورهای راه یافته به جام جهانی وسط زمین قرار گرفت
@Sportfars</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/441481" target="_blank">📅 22:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da571543ba.mp4?token=sJUyoqPUSvFtrGrF2X62vkoPJ3p8u8BgUUz_dezd1SzezaL_v76wNkCz2IHbhtToSZ1Q_YAm0vSVeoP8ngi5L3u7k757FVUh7Zm0cHhKYR4LoxmVByoOT9pN0gJFIF4PIj-IWSfd1hMw5uT1suHhZJ5Cel3V5C6NdolWbdS-aOUdO5WZhcyETBtb7ENEflBv7E1bF23r0pRzTPxpSxciRGQxbveOEpMUZt8Qs0hVvfw6yMaB7uYulL5tOJePLufcibccPkIW4gQun4JhS-WXkBmrrQg3o1XBhDR_EqcC1So7F7jiU4FLhqD4kQaY1DaJJHkG9CsjPv50MCMp76jH6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da571543ba.mp4?token=sJUyoqPUSvFtrGrF2X62vkoPJ3p8u8BgUUz_dezd1SzezaL_v76wNkCz2IHbhtToSZ1Q_YAm0vSVeoP8ngi5L3u7k757FVUh7Zm0cHhKYR4LoxmVByoOT9pN0gJFIF4PIj-IWSfd1hMw5uT1suHhZJ5Cel3V5C6NdolWbdS-aOUdO5WZhcyETBtb7ENEflBv7E1bF23r0pRzTPxpSxciRGQxbveOEpMUZt8Qs0hVvfw6yMaB7uYulL5tOJePLufcibccPkIW4gQun4JhS-WXkBmrrQg3o1XBhDR_EqcC1So7F7jiU4FLhqD4kQaY1DaJJHkG9CsjPv50MCMp76jH6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم باغ‌فیض تهران همچنان در میدان ایستاده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/441480" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441475">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHaxjdzuFBSDU3Xb9-zIJKSdUzRMZ9c37er0jjm_d5yCpmUPe395m8r0Vu8NeSNQRrRCjdXOX0hLObXpnNc-c6q3s9W6MuEOLvM23abfmqKf5JbkJZEgfpq0mXfeAlWo55UymOZ8iougGfu6jL_wAoUo4Jxruyb7wuJqx5ohIpZuc6tPQLuUw02jUYk28Ly6_EGE913mqSx8Kuxs66WEIu17_E31ZZd0rfCRiAEgWRLpcg-NWV7YiO2DY7gJJRSucrenZtsSfHWmxqWUgIMsek3y_hIkNsu3Phbrh8fzCl44S3x5SsEDm81O3Cj54I68D_Qv69FuNWJWsB0UT_QRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihWXbj04qSX9FPo-ITDUQKG7xFV7qD6cSh1vEY5BJEGN1WuhxLLyAKe9XOD_OJ4Og9dX2fuKKh6qYYaKb_df9Qya7A3dxxrmLc1eIZ14oI4GWfOoNgjch6hIrG7Ox6l6QKwG2RbAiAI9U_BbZ9s2UwRrZKNbkzMBNHKSgq7W54fKy6Q4kXaPrFMcyD6mPwyH1MNaIDPiBYPTB6vSoiNzc8-CUc9mMomb1y0zDqoWuMZhpzlX6uxaRpDk9A5ZC5NOtqQtNtqDk5DKMK5VNN5dmKe-WsWjKJoIjx2wJOAQiqnyg1A-ex6A7QQ9j4-iOGjil1_R24ZBYdhVcV81ad4ZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDCIfJxo-pj34UzTEigtK2bH9InNHnlt6q7hiNu92yZ6PAmh40b8JP7fWPfEeBqam1pQIZkYbvW_NBxV4tykADFu1N7DLrOwJ3T_pgzHTxidU-7JGxE8IQx6ypGY9HSqT7IRdW1cgX5L1oHzXsoUjozztaULg2Kd5v-Ui1xSTwKObL6vhWOUET9ZxGZ7nOLYNQKixb1t1mGGW5qJgM2Q1abrSHC86R18roefl6Mg8sYr2zUftZGnxBl9-2q9Pjc7s-emB41tbBXCh9Fixl5OA-4FyTAXM7jMo24yLs1fsnimT12Lnl7shJRCt5siyNHY-9F7pD2X7G6QLwONBXdkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOjkTGSzHrTcs7LafW-UDHmnC4kg_fARyxzd3PqEipwJ6R9DwIq5nPz9x2Oef9-0_FwCxUFUj8lbtmgbxZRRAbfmDWOtWjDEJCo-E0ltFCrYoc5--PQMf_Sg2LFRDYRc6zv4x_ktQbgplzYbyd_opek8KIdXiV3Cw2cweRtZbWxsr0roD3_Zwo0QkDGDlLG1r6uFHw4SutlQ5Yngz1F1DbCygdtiGhjAdwPAKdLDbcFtBSUlQQA72J4Ut0Nb0dTGy754yV2s_DIZGu56XgWrkCvEmjUCX-w1kjZDYqAylwkhwOT6Ht3GdL6hB46dcHBdTQxtCk5W9IhTBnB31SMB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZMtIiCO7Hnml0R9tKFd7tI6VZfq_StHJx7L3T5EEqXe4Pr-2vD9nSepaDq9JaH01P2jhvKnCqsGwjoV17wjZ7WyeIXtEjhYCb10FeKyAR_UdJAPNcrtvpO4h5iVpgzUPmkImc7F17C8ofml3J8oc_guSM08W9c01bz5EtjZ0ViTXHbC65SpvItQtfCp26fv0YLJ-MO21lhThYeq7L26zfIxBKuL4HSW8GJekbqfrDuVaQeHKN-MQsUw5zUZFRKgIe-HCqw6PCgDWwr1s7bJQFnVNewjkYnLnQ-VEkSROqcOZ0t7zyfHfA8qAJXUIZBBj8JiD8KTHpfZnyrZrCLIdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماهایی از افتتاحیۀ جام جهانی در ورزشگاه آزتک
@Sportfars</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/441475" target="_blank">📅 22:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441474">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نقص فنی دلیل قطعی برق در شهرهای جنوب غرب تهران بود
🔹
شرکت توزیع برق استان تهران: مشکل پیش‌آمده ارتباطی با طرح‌های مدیریت مصرف برق نداشته و ناشی از بروز یک نقص فنی در بخش فوق توزیع بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/441474" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441473">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88480d9614.mp4?token=G8BX4WUbjsPT-ClJYvfCLEdkS9moahZLAl_6R8ALWKQcppgWkk5mEVGrK9mDlOWmO_TvQqnC6RCD8KhA0uoElcCvDgQW28BWjJfE_ilPz0p0KdvaoUrfkH9tdYB3JZwu8bPsxIdSKqvmHlnT6qU5EpYOiVJ53RfQpeRPgcQ6noUFGlKKuDAyfAWdCO-WBcC4SefEVKTwlcZemdJIAg6yY8Gotnzr1X7LzG30DWYNwBnKvOsHW13XH9P9PNVvq39zD6hxXPnh32-Xm3O6nVfyXq16Vjl7lRLBlahM2mvcf4t2XvDaoxhF7BF8--yor8QwIRoT5juAw2k-6-8wKY9HiWL-DqTqaFoafZB9DwJJvXg2lPc4Etclzqx9ApxJogoShvSzXUHUNZ3QhTIxJOZHKm0N2xoD_72K5t5-jqR0fMEqlmYe4HI6UdvxPfz13JLmRijP0RU7K7-GsGTyla9rGwrpIZJfWtdVrgJ07dY0Je3MZ-8K590NWkaSo98K2m0WaxUNWKatPOCr33DCOAEipmj0NtBC8SDPzjbO8Wx57D7PwYx-lRJtojBK0wd7XTBmClzXiEH0M2oiAkHQdt6EpX-RyHKtJlxGJeFgVtRM1Rz-roq9s6PO6Q1fy6RVo5e_2wfc3mDhiVqJ1KqNZ5BtkvOQA9FpAp8Ig2_iwtCALOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88480d9614.mp4?token=G8BX4WUbjsPT-ClJYvfCLEdkS9moahZLAl_6R8ALWKQcppgWkk5mEVGrK9mDlOWmO_TvQqnC6RCD8KhA0uoElcCvDgQW28BWjJfE_ilPz0p0KdvaoUrfkH9tdYB3JZwu8bPsxIdSKqvmHlnT6qU5EpYOiVJ53RfQpeRPgcQ6noUFGlKKuDAyfAWdCO-WBcC4SefEVKTwlcZemdJIAg6yY8Gotnzr1X7LzG30DWYNwBnKvOsHW13XH9P9PNVvq39zD6hxXPnh32-Xm3O6nVfyXq16Vjl7lRLBlahM2mvcf4t2XvDaoxhF7BF8--yor8QwIRoT5juAw2k-6-8wKY9HiWL-DqTqaFoafZB9DwJJvXg2lPc4Etclzqx9ApxJogoShvSzXUHUNZ3QhTIxJOZHKm0N2xoD_72K5t5-jqR0fMEqlmYe4HI6UdvxPfz13JLmRijP0RU7K7-GsGTyla9rGwrpIZJfWtdVrgJ07dY0Je3MZ-8K590NWkaSo98K2m0WaxUNWKatPOCr33DCOAEipmj0NtBC8SDPzjbO8Wx57D7PwYx-lRJtojBK0wd7XTBmClzXiEH0M2oiAkHQdt6EpX-RyHKtJlxGJeFgVtRM1Rz-roq9s6PO6Q1fy6RVo5e_2wfc3mDhiVqJ1KqNZ5BtkvOQA9FpAp8Ig2_iwtCALOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر فصل جدید «حسینیه معلی» ویژه ماه محرم ۱۴۰۵ منتشر شد.
حاج سید مجید بنی‌فاطمه، حاج مهدی رسولی، حاج سیدرضا نریمانی، حجت‌الاسلام سیدحسین آقامیری و کربلایی امیر برومند در میز ذاکران این فصل حضور دارند.
🔹
نجم‌الدین شریعتی نیز همچون فصول گذشته اجرای برنامه را برعهده دارد.
📺
«حسینیه معلی» از دوشنبه ۲۵ خرداد از شبکه سه سیما روی آنتن می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441473" target="_blank">📅 22:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441472">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjwn8YJpwHN7-emuhFyLvAqJ9N8CKfwz2GmlfVdBDAS3gXUBqJzChm2wR-6_57WJVHJI5iY-zZmaJmK50QOj785LXNGqMaptV2Bv6xeLEUryvNL87dxkOsnGn5L9GOgAP4WwmWWCj6EA8wHCJg58fjxWnOaSNVHzEMFPHMR4hg-6EBlWq3euNnbciVOF2kX5YAOGnPuUxFPeNnil6DbkCVvZpqajhnc6sKgGXnSBz-c_7lMwV-6i015bO3xQIUd-_5VU-_0rCHPA0rm3U8Xmy5PALL21rlfPbHwg5W9S7rjmTg8t6-RrQ8t7TvA4OsbM5sub0mZu0TIDsu0N_0G4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور بانک سینا در جمع ۵ بانک برتر کشور برای دومین سال پیاپی
بانک سینا در ارزیابی بانک‌ها و مؤسسات اعتباری از سوی بانک مرکزی در چارچوب شاخص CAMELS، برای دومین سال پیاپی در میان ۵ بانک برتر کشور قرار گرفت.
بر اساس گزارش خبرگزاری وابسته به بانک مرکزی، در ارزیابی انجام‌شده برای شش‌ماهه نخست سال ۱۴۰۴، وضعیت بانک‌ها بر پایه پنج نسبت مالی کلیدی شامل نسبت کفایت سرمایه، نسبت بدهی به حقوق صاحبان سهام، بازده حقوق صاحبان سهام، نسبت کفایت سرمایه لایه یک و نسبت مالکانه مورد بررسی قرار گرفته که بانک سینا در این ارزیابی، برای دومین سال پیاپی در جمع ۵ بانک برتر کشور قرار گرفته است.
این شاخص‌ها از مهم‌ترین معیارهای تحلیل مالی بانک‌ها به شمار می‌روند و در سنجش توان مالی، ساختار سرمایه، سودآوری و میزان ریسک‌پذیری نقش تعیین‌کننده‌ای دارند.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441472" target="_blank">📅 22:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441471">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441471" target="_blank">📅 22:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441470">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT6UPJGS1xhYrqXvTCmrFgfHiPG_4xIdCvdqqR_fviYTqwxbPuo_iigcrlwq84u3GFp3t6iui2EFR9FHGkoii4DG9A0eKt1SZ9BGomsZnnxvO_m3OYC4XNCwBdfNo_SBilX_upTio0XqKHQI9JFZySXJXelo-svy1aLDt5hwDvz-PwUHfebe9EJG4IlPLthICJHwVK_kyq1iGM0_wlOzULWfhnems-ImLj3KEUIgI2HCvwpF6sUFnQqPIFqHpt_E5-8N9ugBinoduXJMUdSSPnxTbY2Ud-8ENn3zxVHXOAhzXBhmTcPt_v3nOjYXCi5VrvroSnRCH8IDHMg-WnmiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجاهد: رفت‌وآمدهای میهمانان عرب به تهران به‌خاطر نگرانی از تحولات آینده است
🔹
مهدی مجاهد تحلیلگر مسائل سیاسی: بر اساس اخبار منتشرشده از سوی برخی منابع غیررسمی، در هفته‌های اخیر رفت‌وآمدهایی از سوی برخی کشورهای عربی به تهران انجام شده که به نظر می‌رسد بخشی از آن با هدف انتقال پیام‌ها و ابراز نگرانی نسبت به تحولات احتمالی پیش رو صورت گرفته است.
🔹
به نظر می‌رسد این کشورها نگران آن هستند که در صورت وقوع هرگونه درگیری یا تجاوز علیه جمهوری اسلامی ایران، مبادی و مراکز آغازکننده این اقدامات در منطقه مورد پاسخ قرار گیرند.
نگرانی کشورهای عربی از تبعات هرگونه درگیری با ایران
🔹
جمهوری اسلامی ایران پیش از این نیز به‌صراحت اعلام کرده بود در صورت هرگونه تجاوز، مبادی و پایگاه‌های مبدأ این اقدامات، به‌ویژه پایگاه‌های آمریکایی در منطقه، در چارچوب دفاع مشروع مورد هدف قرار خواهند گرفت.
پایگاه‌های مبدأ تجاوز در تیررس پاسخ ایران
🔹
کشورهای حوزه خلیج فارس در بیش از دو ماه گذشته فرصت کافی برای انجام اقدامات عملی در تعامل با جمهوری اسلامی ایران را داشته‌اند و همچنان نیز این فرصت وجود دارد. اگر اراده‌ای برای اعتمادسازی، کاهش تنش یا ارائه تضمین‌های مؤثر وجود داشته باشد، باید در عمل مشاهده شود و نقدا دریافت کنیم.
وعده‌های غیرنقد مبنای محاسبات دفاعی نیست
🔹
جمهوری اسلامی ایران در ارزیابی روابط و مناسبات منطقه‌ای، بیش از هر چیز به اقدامات عملی توجه دارد. اگر قرار است اقدامی در این زمینه صورت گیرد، باید تا پیش از هرگونه تحول یا بحران احتمالی به مرحله اجرا برسد؛ چراکه در مسائل امنیتی، معیار تصمیم‌گیری اقدامات عینی و ملموس است، نه وعده‌ها و اظهارات.
شرط ایران برای بازنگری در بانک اهداف مشروع
🔹
توقع جمهوری اسلامی ایران از این کشورها کاملاً روشن است. نخست آنکه اجازه ندهند سرزمین، آسمان و ظرفیت‌های نظامی آن‌ها به مبدأ تجاوز علیه ایران تبدیل شود و دوم آنکه خسارت‌های پیشین وارد شده به جمهوری اسلامی ایران را جبران کنند.
🔹
بعد از آنکه آنها به وعده‌های خود عمل کردند، مستحق دریافت امتیاز از جانب جمهوری اسلامی ایران خواهند بود و در آن صورت، خروج این کشورها از بانک اهداف مشروع ایران توسط ما بررسی خواهد شد در غیر این صورت، محدود کردن جغرافیای دفاعی جمهوری اسلامی ایران، خطاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/441470" target="_blank">📅 22:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441469">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ بار دیگر عقب‌نشینی کرد
🔹
رئیس‌جمهور آمریکا مدعی شد: با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران رسیده و تأیید شده است، من به عنوان رئیس جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده علیه ایران را امشب…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/441469" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌ کدام شرکت‌ها در کشورهای منطقه، شریک اسپیس‌ایکس محسوب می‌شوند؟
🔸
الکام اینترنشنال: شرکت دبی‌محور در حوزه الکترونیک دریایی، از سال ۲۰۲۳ به‌عنوان توزیع‌کننده مجاز تجهیزات استارلینک فعالیت می‌کند و یک مرکز عملیات شبکه استارلینک در دبی برای پشتیبانی از مشتریان…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441466" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شرکای استارلینک در منطقه، هدف مشروع حملات ایران
🔹
هفته گذشته رویترز در گزارشی به نقل از منابع پنتاگون افشا کرد استارلینک در جریان تجاوز آمریکا به خاک ایران، با ارتش این کشور همکاری داشته و سنتکام برای هدایت پهپادهایش از ترمینال‌های استارلینک استفاده کرده است.…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441465" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441464">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شرکای استارلینک در منطقه، هدف مشروع حملات ایران
🔹
هفته گذشته رویترز در گزارشی به نقل از منابع پنتاگون افشا کرد استارلینک در جریان تجاوز آمریکا به خاک ایران، با ارتش این کشور همکاری داشته و سنتکام برای هدایت پهپادهایش از ترمینال‌های استارلینک استفاده کرده است.
🔹
پیش از این وزارت جنگ آمریکا نیز قراردادهای چند میلیارد دلاری جدیدی با اسپیس‌ایکس(مالک استارلینک) امضا کرد تا این شرکت در توسعه شبکه ارتباطی ماهواره‌ای جنگی نسل بعدی آمریکا مشارکت کند؛ شبکه‌ای که قرار است سامانه‌های تسلیحاتی، سنسورها و زیرساخت‌های جنگی آمریکا را به‌صورت لحظه‌ای به هم متصل کند.
🔹
این مشارکت گسترده اسپیس‌ایکس در تجاوز نظامی به خاک ایران، سبب شده منافع این شرکت و شرکایش در منطقه، جهت قرار گرفتن در بانک اهداف ایران مورد بررسی قرار گرفته است و نیروهای مسلح ایران می‌توانند به جهت رفع تهدید تجاوز مجدد پهپادها با استفاده از زیرساخت‌های اسپیس ایکس، این شرکت‌ها را مورد هدف قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/441464" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0245725c3.mp4?token=aAxEPTS4A9VnGFLjqO2voqHki8JWekUVfmbf-e39GgfZzaUPU0HRiSFxZkNyz60ODyz3G97-9XSNu3BoXdaEhKd6h0QI3XyF1EghUtgoVmjAJwRum_UjXz2zWvv6-7q1kKeZ_EzP_-IYYcq1zPSGqK9-zvEOr3eWsjHVSSg4c3FmGgtt3qsoS4aXsV8s_WS1LmhmciQZmbMM5DIyi36nUPMXppc4YieKv4TQwzY6hugpFNo4jdPUViOgUvyn79900ALNzRs9MCZ3_ftf9RbYYli56efNgm66sEwgo2SKzja6cUIgDutJSebR9iiXxgxVlnazDJGrmvwMxlt9n8ldDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0245725c3.mp4?token=aAxEPTS4A9VnGFLjqO2voqHki8JWekUVfmbf-e39GgfZzaUPU0HRiSFxZkNyz60ODyz3G97-9XSNu3BoXdaEhKd6h0QI3XyF1EghUtgoVmjAJwRum_UjXz2zWvv6-7q1kKeZ_EzP_-IYYcq1zPSGqK9-zvEOr3eWsjHVSSg4c3FmGgtt3qsoS4aXsV8s_WS1LmhmciQZmbMM5DIyi36nUPMXppc4YieKv4TQwzY6hugpFNo4jdPUViOgUvyn79900ALNzRs9MCZ3_ftf9RbYYli56efNgm66sEwgo2SKzja6cUIgDutJSebR9iiXxgxVlnazDJGrmvwMxlt9n8ldDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروج قطار مسافربری از ریل در ترکمنچای با ۸ مصدوم
🔹
قطار مسافربری تبریز ـ مشهد در محدوده ترکمنچای از ریل خارج شد؛ این حادثه تاکنون ۸ مصدوم داشته که ۶ نفر از آن‌ها توسط عوامل اورژانس به مراکز درمانی اعزام شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441463" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZEoPug2CoMMHXJOSGB4Xh6B8GQ19oFe03J-4hcT7_v7nZTBzN0oPiqBFPrl3iQPbEkU8S2UtOt7F00iwkEbYyT0pi2ektRPw9Ozz1JGxNgx7vp71Ofq9M1aSPhB1qXPPg3p3aDaXTU1tSUjW5E_tiBFJZena49A159D1ACO8Sqm08In0w_pF0a3FzY2AfV7B58rPzGbAZSBrgFXgdKdd3pReKF0vTG6vfS75zKwTek7fPovOZnBKWCBg9tvM7rvrDI93TwfE1hjBgRehzBKY8-q131SlkmLTE74NNeAkZO9CljeJxGlggILF_ipyVgd5PsaroYoUM1aoEMDeMtXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«صفا با خانواده»؛ بی‌مسئولیت و به دور از ارزش‌های دفاع مقدس ۱۲ روزه
🔹
«صفا با خانواده» سریالی به کارگردانی منوچهر هادی، تهیه‌کنندگی مصطفی تنابنده و نویسندگی بابک کایدان و پدرام کریمی که با محوریت یک خانواده معمولی ایرانی و در بستری از اتفاقات امنیتی و اجتماعی، می‌کوشد هم سرگرم‌کننده باشد و هم حرفی برای گفتن داشته باشد؛ اما در نهایت نه چندان سرگرم‌کننده است و نه حرف درستی برای گفتن دارد.
🔹
متن «صفا با خانواده» از یک ضعف جدی رنج می‌برد: کشدار بودن و پرحرفی بیش از حد. بابک کایدان در مقام نویسنده‌ای که سابقه طولانی در نگارش فیلمنامه‌های محبوب و جذاب دارد، این بار در «صفا با خانواده» عملکرد قابل قبولی نداشته است.
🔹
با وجود تمام ضعف‌های فیلمنامه و کاستی‌های اجرایی، بزرگ‌ترین مشکل «صفا با خانواده» نه به نحوه ساخت آن مربوط می‌شود و نه به کیفیت بازی‌ها و کارگردانی آن. مسئله اصلی به محتوای اثر بازمی‌گردد؛ جایی که سریال در مواردی مرز میان همدلی با مشکلات اقتصادی و توجیه رفتار مجرمانه را مخدوش کرده در برخی موارد زاویه اشتباهی را برای بیان اتفاقات دفاع مقدس ۱۲ روزه انتخاب می‌کند.
🔗
ادامه نقد این اثر را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441462" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441461">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ6ykwVu0RMKiiye8fmAQBLRCuPnKXilEFWvJfH1Nqyk9E_f3Qt1Nb1_6yKN3X_ku1DzvPthe2SA0PXw7XopYhFOuozX4z3PSaKyfukbRF_1k16E5ouVg0Xddo_qZ3202iGs6XN6tNwUPyosmVfcFRsRSqcB-yQfTim8WeQi7p5hWOZ44dQEwMzx4eUFQtiQtJvNCw1oWXgQMSqqoNDW4EAAPElQVb8FHjRF-T89wEHVVgklKJEAI34P-shu8UWbVDnZ7xXklIJGF1R0-Zb6vIsM9isFL-zQ4_E4S3iZrWwl7zqPLyhvqMryxx3zYPmpsmL62rg-CrMRQrs8I3BJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ فرمانده قرارگاه خاتم الانبیا(ص): اگر آمریکا بار دیگر حملاتی علیه ایران انجام دهد آتش جنگ علاوه بر منطقه، فراگیر و گسترده تر خواهد شد
🔹
آمریکا از یک سو حرف از توافق و مذاکره می زند و از سوی دیگر شرارت می کند و این تناقض آشکار در رفتار و گفتار آمریکا عامل…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441461" target="_blank">📅 21:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjFM8FaJYHiFqvs94X7SJF9W4Gy7Ga8L_Xij1KSD16tnZ_IzZTXpDMvQPAyw_3mwKd3mGgrpA2VCbeUNeesT42NeEGbG863zggftFMU6EiegC0q1_pGlnEzbVyl8hdP37fOdViC6rzRvR7pI2j5WMtnXNTDQjLFdIraXBhKps8Q9AleQUjKls9-yLwTWdnnW-bdCL7hkdKOwmZeu4NomLhcxFc7M1HkF5zLjFITYbkhouthks7EM2sZCr9M-lzFADIR1zdq5PRmI7KhGnPaVvkgeyy7XnBciLxpZbBW1ZkoRfVuls6L02L1hPD0Q--n1y9D15hPgez9kJmVr1bEntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: با اتکا به خدا و اقتدار نیروهای مسلح، هرگونه تعرض با شکستی قطعی و پشیمان‌کننده مواجه خواهد شد.
🔹
امروز بنیه دفاعی و بازدارندگی ایران، فرسنگ‌ها فراتر از دوران دفاع مقدس سوم و هر مقطع دیگری است.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441460" target="_blank">📅 21:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
کارشناس بین‌الملل فرانسوی: همزمان با تشدید تنش‌ها در منطقه، کاخ سفید با نوعی فروپاشی پنهان مواجه شده است و آن چیزی نیست جز افول جایگاه آمریکا در کشورهای کلیدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441459" target="_blank">📅 20:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441458">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_DNLHfsrmddFynQr6dXbtIgqU3nzIFNhWum7T3Q5fNSwYtvVa1AXs6VJ2R9YKN1tryXXVvxeYrUT0EJKj-wokHT9Y9hWw8gw_FgXnMtU5tx3TCKRxuOjSt7dDXQXF8u4Ao5BFc1lBLQUYkBZkWgrxevPO1FjRf0SaYqVHDMkTCkPURiecV0R96j6HR1RvRvW9QZBsJhscZHvWgKUoEVjuUp7zBtNJpOYqe0vygypVzjBSZWbF0oEIb1uAY1e8khzHRNCYEHsobnkmxDmvEVaTWOTzA9XBMNTnL0Min_wcqidJHE1_d_q6ArAM_O2o-N28B5xJ2j4gChkxw8yp62oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط بطلان آمار و ارقام بر ادعاهای ترامپ درباره تنگهٔ هرمز
🔹
رئیس‌جمهور آمریکا روز گذشته ادعا کرد که ارتش این کشور در هفته‌های اخیر موفق شده ده‌ها میلیون بشکه نفت را به‌طور مخفیانه از تنگه هرمز عبور دهد و بدین ترتیب مانع از جهش بیشتر قیمت‌های جهانی انرژی شود.
🔹
او گفت در نتیجه عملیاتی مخفیانه بیش از ۱۰۰ میلیون بشکه نفت از تنگه هرمز عبور کرده و بیش از ۲۰۰ کشتی تجاری با امنیت کامل از این گذرگاه راهبردی عبور کرده‌اند.
🔹
با این حال، بررسی داده‌های کشتیرانی، اظهارات مقامات آمریکایی، گزارش‌های رسانه‌ای و داده‌های موجود از ارقامی که ترامپ مطرح کرده از جمله عبور «۱۰۰ میلیون بشکه نفت» حمایت نمی‌کنند.
🔹
پیش از آغاز جنگ، روزانه حدود ۲۰ میلیون بشکه نفت و فرآورده‌های انرژی از تنگه هرمز عبور می‌کرد. بنابراین ۱۰۰ میلیون بشکه معادل تنها پنج روز از حجم عادی انتقال انرژی پیش از جنگ است.
🔹
شبکه الجزیره در گزارشی نوشته چنانچه حجم تردد دریایی پیش از جنگ مبنا قرار گیرد انتقال ۱۰۰ میلیون بشکه نفت به عبور حدود ۷۰۰ کشتی از تنگه هرمز نیاز دارد.
🔹
نشریه تخصصی «لویدز لیست» نیز تعداد کشتی‌های عبوری از زمان آغاز بحران را ۱۴۲ فروند برآورد کرده و شرکت «کپلر» که بالاترین رقم را ارائه داده، از عبور ۲۶۴ کشتی خبر داده است.
🔹
حتی اگر بالاترین برآور مبنا قرار بگیرد با سطح ترافیکی که بتواند انتقال ۱۰۰ میلیون بشکه نفت را توجیه کند فاصله زیادی دارد.
🔗
شرح کامل این گزارش را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441458" target="_blank">📅 20:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441456">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۲.pdf</div>
  <div class="tg-doc-extra">3.3 MB</div>
</div>
<a href="https://t.me/farsna/441456" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-61.pdf</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/441456" target="_blank">📅 20:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441455">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
قرارگاه خاتم: پاسخ نیروهای مسلح به تجاوز و شرارت‌های آمریکا تداوم خواهد داشت
🔹
توقف حملات آمریکا به مناطقی در جنوب ایران بنابر اعلام رئیس‌جمهور آن کشور، به‌دلیل پاسخ قدرتمند و کوبندۀ نیروهای مسلح جمهوری اسلامی ایران است که در این رابطه شکست دیگری بر ارتش…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/441455" target="_blank">📅 20:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441453">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a60b1aa8a.mp4?token=uWCFeBVSNZJhKTOdUnvRSj-nNp0tzh7Kfy2mRD2wwlh8Hyol0juxue1YXHjFvYOgxtuLSHP1xMVRvTRZnqHyIoRgQU1PKYUoAh5_w0-cBnWcvS3p8Vu8bTbgdLszmClse_0onjgprXvGdwnse6NIxQDye6dZqozyvvoxjJEOJSlqmKzrndMC_EJ0nXR9W3YRDV--DYv1waOoFsItRLHx3SwxWxHiCPQOHfFWVkSngSTTSGarXWgZJUkqt8jm_Jlqqj8MOgYindj5RreoW_6xMsuYf8uuJjAu7ZoFZn1QFO7URnee8AFn1oP3lZbUBrzaj3whriHv-EZ_iuQMHPVmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a60b1aa8a.mp4?token=uWCFeBVSNZJhKTOdUnvRSj-nNp0tzh7Kfy2mRD2wwlh8Hyol0juxue1YXHjFvYOgxtuLSHP1xMVRvTRZnqHyIoRgQU1PKYUoAh5_w0-cBnWcvS3p8Vu8bTbgdLszmClse_0onjgprXvGdwnse6NIxQDye6dZqozyvvoxjJEOJSlqmKzrndMC_EJ0nXR9W3YRDV--DYv1waOoFsItRLHx3SwxWxHiCPQOHfFWVkSngSTTSGarXWgZJUkqt8jm_Jlqqj8MOgYindj5RreoW_6xMsuYf8uuJjAu7ZoFZn1QFO7URnee8AFn1oP3lZbUBrzaj3whriHv-EZ_iuQMHPVmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیفا آزادی‌خواهان هائیتی را از جام بیرون کرد
🔹
جیمی‌جامپ برنامه‌ای که هر روز به حاشیه‌های جام‌جهانی می‌پردازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441453" target="_blank">📅 20:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441452">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP5M8qiyE8wOPXdEp2MXSt_92CNrWlhBUWvKOMNG_qriPrpO6P3ijcOAeuIuwLkUluhNCZ2YC7XhL97AVtkRw8c7nK5ZjFKlvihYai_XujBWI1LPuO0S3-Jweybb0QZBM4DUIh7uT87sEO3wAMuTpg6CQ7tnigHWV-43QXDnXCNJrfF4hd5ag9uyE_T5JvQa4uLBUE_rH3aAT1Zk_nwD8nekPv4hh4_pRThjYcMp1dOvQVF8UCGW41XrtLsCUBumKu6pkREN7L1d0aY-xu3e21qLM-2Ftw-tlJFbfpV0hFdRg9Mq4oQFWkawwGyTruRFT720iTeSE38PVr1bVraaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان با سرعت ۱۱۹ کیلومتر بر ساعت زابل را درنوردید
مدیرکل هواشناسی سیستان و بلوچستان: طوفان گردوخاک امروز شهرستان زابل را با سرعت ۱۱۹ کیلومتر بر ساعت درنوردید؛ گردوخاک دید افقی را تا ۲۵۰۰ متر کاهش داد.
عکس: ابوالفضل شهرکی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/441452" target="_blank">📅 20:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441451">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd3378cff.mp4?token=B2RN2v1vCf34ABqi7jl2OnBT2oCnOVWGUZVJQwvwRwucRn-MytSoRToKZ10yrzVZZh9MHYiSlsbCeI3tXUCRYvDuZwzlhMruenG1iTJvmbyLxcG8HjjF5GndVKpSJ0ad_VZiyiubLvY9TWzCBuAltQIAlAFBwaHQVQqrJxSAVJHnkqUmghhX6YNAFWeYZDt6QdhV5Y8Ihli08j2tCtK216MjiN4fNwzhClMM16XMgp1NVY2siF49gxhln06zst1j7C8Bf-F0Y2w_zMBY7btR1vent1iINDwZGZ6FWhY7C0PrJ1D8lBzsKXiRvGe0QF_eKTuoH7y1RYp73dtzi8sjczO3PpNK00LSVwgXS9d7Amc5zlvLwrPYo4bsoByGiba3cQOv25tfTdBjJ-IbAsspGwYbFZz3TNlVN1YhzAIKNWkozoAwFlQkG7xEyLaBmJETqdNv7m7St3bxlPV_HtlwcLEFV4A2_XKCbicYJPnVQyOZ7azzAJ9fq65wdJZPU6s8ZF19rQTaFKTCkIGfVR2WxOnTm4USWj24G8b483qXUy3jtmHE9FGObI1gm6cSUx6Zx4dUTbgrlYCdB8i6yDkbAUu0RnQSz-tH022yGZocvhlHIil8DDrsoWZEibpYoNETaM2rSPu8zN_m25IlZQd8y-aYoMSeLWlrMrpRo_zcx6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd3378cff.mp4?token=B2RN2v1vCf34ABqi7jl2OnBT2oCnOVWGUZVJQwvwRwucRn-MytSoRToKZ10yrzVZZh9MHYiSlsbCeI3tXUCRYvDuZwzlhMruenG1iTJvmbyLxcG8HjjF5GndVKpSJ0ad_VZiyiubLvY9TWzCBuAltQIAlAFBwaHQVQqrJxSAVJHnkqUmghhX6YNAFWeYZDt6QdhV5Y8Ihli08j2tCtK216MjiN4fNwzhClMM16XMgp1NVY2siF49gxhln06zst1j7C8Bf-F0Y2w_zMBY7btR1vent1iINDwZGZ6FWhY7C0PrJ1D8lBzsKXiRvGe0QF_eKTuoH7y1RYp73dtzi8sjczO3PpNK00LSVwgXS9d7Amc5zlvLwrPYo4bsoByGiba3cQOv25tfTdBjJ-IbAsspGwYbFZz3TNlVN1YhzAIKNWkozoAwFlQkG7xEyLaBmJETqdNv7m7St3bxlPV_HtlwcLEFV4A2_XKCbicYJPnVQyOZ7azzAJ9fq65wdJZPU6s8ZF19rQTaFKTCkIGfVR2WxOnTm4USWj24G8b483qXUy3jtmHE9FGObI1gm6cSUx6Zx4dUTbgrlYCdB8i6yDkbAUu0RnQSz-tH022yGZocvhlHIil8DDrsoWZEibpYoNETaM2rSPu8zN_m25IlZQd8y-aYoMSeLWlrMrpRo_zcx6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ وزیر علوم: مجازات قضایی و انتظامی برای کسانی که در دانشگاه پرچم مقدس ایران را آتش زدند
🔹
کسانی که پرچم منحوس پهلوی را در دانشگاه برافراشتند و پرچم مقدس جمهوری اسلامی ایران را آتش زدند، از لحاظ قضایی و انتظامی به پرونده‌شان رسیدگی شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441451" target="_blank">📅 20:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441450">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN7JvXtqe5tf7VttI4xqwwSRrOc9owJZcuws8u-gUkyJmS5iv4gdAGfvj2590S9LyV4OxPxA2RFMAg2ScnEtHeky_MLOKmrp7rD7lxqTYI9W1l00kzEr1EijT4iXSsYS5uZwC2o9Dz12eNDa1IqUqZruU_yzhAZFbBT8h5xHAvdJkld7b3Iwh7SkMNDF35-iqQZVW3gRpKQVenT0oteEWKsKBn63JmNbnoukW3FS8EBYJJXJV911-C_MEnfpIfBZeQ5Hyx3-Aw0LszDflHtWBi23bZ68eWWa64obSgsVXhcSd00MIuuxCe2IHUOnSg9tUep7fhsZh1SF-N8bqm_wNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم تشییع رهبر شهید انقلاب در خارج از کشور برگزار نمی‌شود
🔹
دبیر ستاد تشییع و وداع با رهبر شهید انقلاب اسلامی: هیچ برنامه‌ای برای برگزاری مراسم تشییع در خارج از کشور وجود ندارد و تمامی تمهیدات در داخل کشور در حال برنامه‌ریزی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/441450" target="_blank">📅 20:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441449">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKWwsWgH_3aevHduS-U36zoMeZm20TYvS-s8whIKRrB34V5LXOTLDoRNlgV4YbjGMBG74EHWT-xMdjseKhdxqJz71ZB6folqWtPQJtG6E0RKSkm4_hsPVj97kaSpU0bBavkr49ujl-8P5OH8dIPyEFJK5Y4zyRU398cDgI5MUr3VVrKNCa3jvzIcx5BcQ4JFDYYFLY33bF5soXc2_aJILdtgZATy4iAIDy4VS5q8guzYjtf2RBJhFHdYSGZ2Xcep08CY4-C9_DOOnMw_xNmEYeweX3EBr6PmkRtOvUx0yaWer4qtIaHCpgmk45iEfpKYYKySnbrl1O0uzFCz_z4oAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: محل استقرار جنگنده‌های آمریکایی منهدم شد
🔹
در پاسخ به حملات موشکی ارتش کودک‌کش امریکا به یک مکان تفریحی، یک مجتمع تولیدی و محوطه یک پادگان از اطراف کرج و نظر آباد و یک پایگاه محلی سپاه در شهرستان پیشوا، برای تنبیه متجاوز صبح امروز با ۱۲ فروند موشک…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/441449" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_jgd7HkMbKYFAU3Q6CZHZjIN5TcZoNqBcK4nIUblcy4KppT8AQ1gEd_zD5YxWBq6zW7Fn22BgGQD8ptGGQY-D0e-g70WyBqNKcNhIgrg6UGLeiZAARqhiDUfAX6j2gRLBgibny60wX8jLKImSDVTYO84fkjvOZK8xz5CNGS_DisHSUzoZYkz0yPBjqx_R2_oG1qCWOiZF_k6kEHxGAaL4zNgsvQ_6tz4kP_805zFAGwBDYpGDIeGwfn0TaNYXb9H-mnROqyRfbtR5ZmOv4nHTFE3R4EOwMn4NMZN9iEPVZ8omtXSMzC2L9EKiKiex3L4hT6MkXElsyPfELFL16TKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: پیروزی نهایی از آن حزب‌الله است
🔹
فرمانده نیروی قدس سپاه: رژیم صهیونیستی باید بداند که اشغالگری، تجاوز و جنایات مستمر علیه مردم جنوب لبنان هرگز اراده ملت مقاوم لبنان و رزمندگان حزب‌الله را در هم نخواهد شکست.
🔹
جنوب لبنان همواره سرزمین عزت، مقاومت و ایستادگی بوده و خواهد ماند.
🔹
حزب‌الله به عنوان نماد مقاومت و عزت امت اسلامی، همچنان در خط مقدم دفاع از لبنان و مقابله با زیاده‌خواهی‌های رژیم اشغالگر باقی خواهد ماند و وعده الهی مبنی بر پیروزی حق بر باطل تحقق خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441448" target="_blank">📅 19:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441447">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkHZjgKrVK7vIZ4jlbJgCEeiuaprO4vEICGlH6LgdPrOLCnD8iVZi1JTr_XoZTrRZiRxdIi6DAC9HKdgsEMjHnmc-N7S495M7uDYECZNWkBgcd0z0e7iRXUUgBGsglEJIIiTXRWK1SuAe27CqumU_PHQwwuKLOl2ZIb0cG2uZwZUiGJOXpwnW_ib5Zt8IY03NAW521q93ik5XBNtgQ91oCAI5ilyf9DrC9agd3BmhI6Upt37SLJddjUVe3fyIIyYpNTIacPxcCgHv16XVPYTqchdU5INZtK7MdIETRJGP3GRQ07UJiVHFSA6fq-hUVpm4bXm8Brz6zzUyRvIdImKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: تصمیمات بدون فکر، زیرساخت‌های انرژی و بازارها را به انفجار می‌کشاند
🔹
این کارها مردابی بی‌پایان پدید می‌آورد که سال‌ها در آن گرفتار خواهید شد.ایرانی متفاوت خواهید دید! @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441447" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
