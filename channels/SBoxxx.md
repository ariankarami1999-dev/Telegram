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
<img src="https://cdn4.telesco.pe/file/awpxB1YuXrfHQbfvuTrHGA2Oxpcicdnb0s9Tzx3wmc4-QM2H0ibOj9FrCI77eHO_TsP7pYQBGp8xCG3-uArCkoCNXTRDT41MTsIlmeTj6kq6wWVRvMPQg5XweoLJ60EhEuR8PluoZYwVsZ_JIhD817wWlKtsG6_CmUO1wGPMSIwO8AxW8CgIin5N6_BovNBjT6LNaD-xeakrp5x3BFzJ3e4HQPetC98gMayklYwW6esLDIKV5FyBdqlO047AHWnMzFmrUG6eJXwuIM1lx8_U8X9A1GL5EYUTDhFGrhZnfn7lPe0oLDyRNqSlaKLu3ALNhK28GoUSMMvfgDt8Io-LRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 00:48:50</div>
<hr>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8aLHLSoiBGVrgyTkvCRew_gph3STi6rruqlT61W911L-XKQeNcQ_jeGoeDHKYfpEmX9kuh4VhO8snQ5p9rZM34G9oNh79tw8L4YW2gWfAhrqA2fFPd2eY7oVZsHUU83V75KGia6b5QFo-idjmgpkSKFPnlJ0BZuDyoR2vchgoFoX1-QsM374O6F73SWjA77ax6p66OLbcY_scplb8TbeNmb8EgQ82jX48SgXdmNVSN78XkPplmC80KYTrfiAnFlgVah-Huy3wtfxlxybO6DE7SE9rrL8AhDngda41bTiEItDnnU3n9xZkI8VoeQ6qkDeFJxdQFxExi_vcH3pwgrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SBoxxx/20792" target="_blank">📅 00:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">علی الطاهر!</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/20791" target="_blank">📅 00:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mleMDzSiIdxec5syexpLGqKyV2seDpnLB3Fe96laCqUz2XoeG8TSCIb1va_TbD6Z1DVbxp_bmdY1XYuhizB81qGCkQDpFWn73tdWoQBDZbQxBwGBKkZhoD6nbDLbGtkobl2YJFNIDVbwpiuVyJNE6zIpRScYYqKoapH0h-0HjqCOB4ApAi_jdtNZ_5-gT-SCMvuZCTEgpWOnpHBc9FVabee3YjpIjR7AEUpJODiKlvBwy_c7c8d7pFWfSwyM68HqtZFXB8tNLmZxKQSCZkN9K3evGcj6aI6jm8NXRRPjcy1zqIyEA1rvA7z_KLnUitgaO_dDkeEN1OQnyLaR6WLeoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکستن انحصار چین.pdf</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/20790" target="_blank">📅 23:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">شکستن انحصار چین.pdf</div>
  <div class="tg-doc-extra">186.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/20789" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیا چین راه اوپک را می‌رود؟!  در دهه 1970، زمانی که کشورهای اوپک در واکنش به فشارهای ژئوپلیتیکی بر سر حمایت از اسرائیل، تولید و صادرات نفت خود را محدود کردند، کمبود عرضه نفت منجر به فشارهای تورمی شدید در اقتصادهای غربی شد. با این حال، این شوک عرضه، نوآوری…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/20789" target="_blank">📅 23:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftxoz17Xt_-qR_2q7ixx764kW6wfxGENFLFQ6p94ddKNtKmUQsEfkSn72TgjEhw86UmqpbOvcZkkyxJISHvz41l0AhMm0wciAJaoaZ5iSlQYqoxzULa6gKsWW-NLkYVQs7WRGN8nYcIqs30WtnaNsZluOHWtALbiaRiKMNNvhVu7C8VkCWCUwghdzMczY6nbfSZejP03YPbWL-b0ELZPEb5Rm9p0Wwtj_h-57ySMpLThjppnXxGEt8oy34ppwNZl5yriQq13SbqK_XnMYRp1pHGGPSNrfySRw1mkORvuY3hbreLY3lDdtLS3tPEtX4a4EsptwgViIlGW_O5YTcpGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:  با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.  این زیرساخت‌ها،…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/20788" target="_blank">📅 22:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:
با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.
این زیرساخت‌ها، یک شبکه تروریستی استراتژیک است که طی دو دهه گذشته، با بودجه و برنامه‌ریزی ایران ساخته شده است. این زیرساخت‌ها و مقرها در منطقه "علی طاهر" قرار داشتند و قرار بود به عنوان پایگاهی برای اشغال جلجول و کنترل و تیراندازی به سمت شهرهای "متولا" و "کریات شمعونه" عمل کنند. نابودی آن‌ها، به معنای تکمیل کنترل عملیاتی در منطقه "علی طاهر" است، هم از سطح زمین و هم از زیر زمین.
نیروهای ارتش اسرائیل برای دفاع از منطقه و جلوگیری از بازگشت دشمن به این منطقه، آماده هستند.
ارتش اسرائیل در این منطقه امن باقی خواهد ماند، به نابودی زیرساخت‌های تروریستی ادامه خواهد داد و از هرگونه تلاش سازمان تروریستی حزب‌الله برای استقرار مجدد و بازسازی توانایی‌های خود، جلوگیری خواهد کرد.
دولت اسرائیل به حفاظت از شهرها و مناطق شمالی از داخل لبنان ادامه خواهد داد و هرگونه تلاش برای آسیب رساندن به شهروندان و نیروهای ما، با قاطعیت پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/20787" target="_blank">📅 21:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وال استریت ژورنال :
ایران در حال ازسرگیری تولید محدود موشک‌های بالستیک در زیرزمین است و پس از آنکه حملات ایالات متحده و اسرائیل به تأسیسات تولیدی آن آسیب رساند و محاصره دریایی واردات سوخت را محدود کرد، در حال مونتاژ سلاح‌ها از قطعات ذخیره‌شده است.
تولید همچنان به‌طور قابل‌توجهی پایین‌تر از سطح پیش از جنگ باقی مانده است، اما تهران هنوز یک زرادخانه قابل‌استفاده از موشک‌ها را در اختیار دارد و در حال ساخت تأسیسات جدید زیرزمینی است که برای محافظت از ظرفیت‌های تولید سلاح در برابر حملات آینده طراحی شده‌اند.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/20786" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">موج ۳ از ۵ در حال آغاز است.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20785" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتانیاهو
:
توانمندی فوری ایران برای تولید بمب هسته‌ای را دو بار نابود کردیم و آن‌ها بار دیگر در حال تلاش هستند.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/20784" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تنها دستاورد موشک پرانی های یمنی ها در دریای سرخ هم بدبخت تر شدن مصر بود و نیز برجسته شدن مسیر جایگزین ترانزیت دریایی از چین به روسیه</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20783" target="_blank">📅 19:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8Yaplv5toYH2F2HMeEUJDeoM8Xn0-MDkW4pjOKO3R5__CblRXNKVsa8NbGkT0gtJVk8eW-Cr7_ARJp0hvVNMaWAMyWcZs7F4uXKJnbpnb4CB-TDyAg3JOTctZDSe6rbmAOziCsMMf45ark4pvO9Rz98w8IZhikb57P72ttAt1o7PG1jgpjGfJPvCjXFpgXZJMuryjMVSvLlQQjKcICSTyi4e4KXBxdesAy3xzqJhgVIkH6Nn5EYTa3X9V6toK8Z_BGLsFY1nsb5LR9XgFOofOGUNgHgDTNvV-62Egh6_m1leHJgQa-H06qDfs1C-Leohfyx0Ju7QBnzRAJGpW5qNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20782" target="_blank">📅 18:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عربستان سعودی به اوپک گزارش داد که تولید نفت این کشور ماه گذشته به دلیل اختلالات ایجاد شده توسط حوثی‌ها به ۶.۲۴ میلیون بشکه در روز کاهش یافته است که پایین‌ترین سطح از سال ۱۹۹۰ است.
احتمالاً این ماه، پس از حملات به جازان و ابها، این رقم حتی کمتر هم خواهد شد.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20781" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/20780" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20779" target="_blank">📅 17:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcQsvni6tRoGVwX8U4GWnLsBPPZOJGh4vQMyE62N9oRrlvU0uhxtVSjL558AhFs7M6iGnaaLah2Abpq0OJ98qWARYv7Jmc6wZ3g7Y7haRqIzfcvhaLJI_g7az7AGWlkAPPH0SrgivS1-RsC8ha9r83O2Zt4nVq75HfjAOOsdRu0qRRb2kG455Z7r6O3Fv90Eub1--73KJiMI9JGQ7dcnQbvo_lY4b08OlYepg1GEGE-xpYBZbdgj6F7XS88EhEeCTa_RyRyHQawuKoRFuLDsTs51baT0i9Q1dTL2AkQpRlSrlJTQre4bnK6NGgMWrWFSOEn7rdupcyrDSJ-0pofCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این ترتیب باب المندب هم بسته شد و ۱۲ درصد تجارت جهان زیر ساطور حوثی ها قرار گرفته است!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20778" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20777" target="_blank">📅 16:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اخبار اولیه حاکی از آن است که نیروهای مسلح حوثی(انصارالله) جزیره میون را در قلب تنگه باب‌المندب تصرف کرده‌اند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20776" target="_blank">📅 16:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گویا طلا منتظر انتشار خوانش شاخص بود تا ۳۰۰ پیپ بریزد!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20775" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در یمن شاهد فروپاشی نیروهای مورد حمایت عربستان هستیم.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20774" target="_blank">📅 15:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b73ZnyTS_DKEG6L79UMy9p_OKtYpEsoFlacYXg1pvIEyaBHdVMAH4Ke1G_zhu3LQ8aYdx2B-b2THkm0oK7ovoj-Vz9m6f_UShMgSWS7NCxx5KO6ztcN7RolfHh7yYFjON3GtocQT3WuuV5KZJfyao8Omg-L0mXRj70xIXlsZB0z3NeiH7fjqMzrTfJm5q4VjhrpO9egpNFYBxqBqCwCcud0p64pxBfg0sNPgeRpU15wuja7Zl0F8UD1dXBUV6oKIBS1gCQKQUFvBcQ_X3ndT9MdhohNr7zgb-ucyrqT6BtpmWb5XCx2kIKqKlKX437pqEQ3wKg96ALUNaXy2gSvoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزیره زُقَر هم به دست حوثی ها تصرف شد.  این جزیره در مسیر کشتیرانی بین‌المللی در جنوب دریای سرخ قرار دارد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20773" target="_blank">📅 15:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20772" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20771" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl_2u-M33LbknjjSq-JTe9rtYTMzcBOAAT8OR1KudQNHR5oJlfLkNzNX5LZCOvoS0RDX9Gyhf2iefXXwSigyQ-YeDBy3HX_PebI10We67sfMIipmuFOqR_xVWzNlDtQK2lQ4IGazxu-BFKYlnt-btpnGU1Kmmv2F8-s0ojhSjuGVVbJaDgLTppZJYtx6OxCc-Bh2noRReHXp1Bt4SYx04N_bsfGrndNv94TMThfOxALDvpz2-2jmJm_oVlJbAKgN-yzwuRtLnbTn2txbDOMc4sFsoNLGZ0Pn3PM6xdWPCJEOvB-yBM7YhSdqXuSSTeY1WYwqgq-II3n9bYvyIBDIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 26</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20770" target="_blank">📅 13:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حوثی‌ها در یک پیشروی ساحلی سریع، حدود ۲۶۰۰ کیلومتر مربع از قلمرو در غرب یمن را به دست گرفته‌اند.  این پیشروی به سمت استان‌های غربی تعز و جنوبی الحدیده هدف داشت و گزارش‌ها حاکی از آن است که نیروهای دولتی یمن با حمایت عربستان سعودی در سراسر یک جبهه گسترده به…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20769" target="_blank">📅 13:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 26</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20768" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 25
پنجشنبه 10 سپتامبر  2026</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20768" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20767">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بلومبرگ به نقل از منبع ایرانی:
ایران تا زمانی که اطمینان پیدا نکنند آمریکا در آینده برای حمله مجدد بیش از حد محتاط خواهد بود، جنگ را ادامه می‌دهد
دولت ترامپ تنها به تهدید و تشدید تنش پاسخ می‌دهد
تهران آماده ورود به جنگی شدیدتر است و اگر واشنگتن به تجاوزات خود ادامه دهد، حملات متقابل خود را تشدید خواهد کرد</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20767" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDGHlguLW0X_CLJzmt_K2RKtJK3xZ2ri6WyRkv3sS7JLXGtVizcK62Wk4fMLPWxzE5mm_39e8Elc4lZaOtwnF7-qiGIaNiXUpB238878VeVIA5LfNbrOc_E4_xnQT3_2hySNPmjRMdL5ze9NTvmQUxTwG3qzCfl4as_L6iYw5SpW9X-ctRHLU8C8Wmvpb_4vwynOKfkivSDten0PT8Uf-4uYfvdE1s8lfKaF8tIe3K3jauRaMYkswt4CWIr5a_YGb0IVP7J6ikcB5HpBnNdjNPNPcQTMuiqIe3yH9lXJNZCMcpfzfHkRnt8i3JMsbuFSAQY7474-N8pNL0vQkNyGAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20766" target="_blank">📅 12:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">راستی فرهنگستان برای shemale هیچ برابر پارسی پیشنهاد نداده یک چند میلیاردی بدهیم شارژ بشود استاد؟</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20765" target="_blank">📅 12:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دارم حداد عادل را با شلوارک و پیراهن هاوایی و کلاه در پاتایا تصور میکنم!  اصلا آدم یک جوری می‌شود!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20764" target="_blank">📅 12:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeMepYYve6LVfi2M9BrCLzOG-o6tGEyLmCtkwlKtP6TlbBCww0Y-o8ojwkdHhJvxHYzxyxnTFBDH9g9a3CDCp1blcoug-AquiCqxS1uoixhHjTHXAT1nRercNTG3a-TxorVJ_jimK6LvPAOhdekSDH4hLjHLDbGxucfnvW1VVZ4aeWR8NeIWn0XKmw4nTmQWn5p6XfFC0U1UTw03c45N9Cs3vb6dg-0bRmm466zQDKjm5cY_Fq1tv_1-o7KVxgHKOB6g6Yl7Hq5vj2ZW85Isj3tC1E-0G8LT1MJ58O4RcQd2EDqM2OD_Dkf1ZqhLCLGITjqDDGqqFfxAEQjFF_yVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا انتظارهای تورمی واقعاً اهمیت دارند؟
انتظارهای تورمی زمانی بر اقتصاد اثر واقعی می‌گذارند که مصرف‌کنندگان، شرکت‌ها یا سرمایه‌گذاران بر اساس آن‌ها رفتار خود را تغییر دهند؛ از افزایش دستمزد و قیمت‌ها گرفته تا تغییر در سرمایه‌گذاری.
بنابراین صرفِ افزایش نگرانی درباره تورم کافی نیست و سیاست‌گذاران باید در کنار انتظارات، عوامل بنیادی مانند عرضه و تقاضا، هزینه تولید و قدرت خرید را نیز در نظر بگیرند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20763" target="_blank">📅 12:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پس مشخص است سفرهایی با اهداف خاص هم داشته اید کلک ها!</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/20762" target="_blank">📅 12:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:  وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر  با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20761" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:
وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر
با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی انتظار داریم که قانون حجاب را تعیین تکلیف کند</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20760" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhdLAezH7-vy_6i1h2RJC-SVLMNquZuyr2WwH0hUZCOmcEFX7fLRnBrpoLAxX9pRpx3HZRz79_-X4KyPKt8HZdGaVP2C1MDVSD6nE17y_RBh0Gq0PsVyL2VlTqkQStOV9P9JgBqy9h8x51yGm03qebDCQNgSLfXyirn7O5ZGvsupHjA_euhKR9tb_MmMJ0PJOqQ8Vm1fPcpCrAqRT89XkLK97BQJ4Ol1JMmaQvbZecr7a9tqs8gMRoBxWtiwSiqMXlQEs5CoBHHqgoCxDLM_nFjoCOnL-FvxXmuVAm92F6JsB15ZREMfk6sJIRyFwKwa-27_oBy5dm7ICvjJpMVoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.
نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20759" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ درباره نظارت نیروی فضایی آمریکا بر کوه کلنگ:   «به لطف نیروی فضایی آمریکا، ما می‌توانیم همه‌چیز را ببینیم. حتی می‌توانیم نوشته روی لباس آنها را ببینیم؛ محمد الفیاض، ؛ هیچ وقت محمد جونز نیست مثلا؛ محمد العزوری.  می‌توانیم آن را از فضا بخوانیم؛ باور می‌کنید؟…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20758" target="_blank">📅 11:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8qfGdbXHwYpl1yU_ZTPNPsB6_hOPauJWAStVfhtmLYr21w7s6kBQ8mmwYSg9vXpSnqsSusCreN2OxU6_YwsqPtOZStWsG7cNCcjNfZraMwvKViL4-Qg5RhnQF_IH23Rm-rAK8ekLcegGBFOPejAjPB1pgK5u4GMD1h8DnRPY-dxVzmppBYIfJ1qAz93p8IN0ITT57fzvUiYhEBjZxrq1hzVwmVBeSWvlSYyHlS0kLZ0jNNVrBUpykbCEqQ2L4OEKG0d6YGq4i3IihdpMCeKzbvyb0xOSAUqGncfWoSrGXUAYV168Ztw5HUd6uhLYsBJHCaSwEgLCtuWWSkhzMmfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهر بندری راهبردی «مخا» هم توسط انصارالله تصرف شد</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20757" target="_blank">📅 11:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20756" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20755" target="_blank">📅 10:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شبکه سی‌بی‌اس گزارش داد در پی حمله موشکی ایران به پایگاه هوایی «موافق‌السلطی» در اردن، چند فروند هواپیمای نظامی آمریکا آسیب دیدند که یک فروند A-10 یک بال خود را از دست داد و حدود ۸ فروند جنگنده F-15 نیز دچار خسارت شدند.
بر اساس ادعای سی‌بی‌اس، نیروهای آمریکایی مستقر در اردن برای مقابله با حملات موشکی ایران مجبور شده‌اند، بیش از ۳۰ فروند موشک پاتریوت شلیک کنند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20754" target="_blank">📅 10:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaEfXQ7R3Prb2gfPduxLqq1mcv73IeDxVHT4zgNL9nZrG6N7sqBLblbtzwKAlC-nOcMxT5B9R3KfzwqqnThjf4p7NZFc-rvopfvAjkviDw1McuAkxZfoEU4lF4s1MS5tbcCUUe9GlAeaQoNCWAInmbu58vqwh_ykE3BL6WNNHftpPOzLyU36XIaXuv7sEd9E2AKRqULFpSzf1Xy1F5_GoRx_OFJ9gNVq18wXvR6eyRIBepaVy9vG98NAv8VgwOHK2PQsr1rI_jmwkm8mnjD1vnlJoetl7xkFYFsTm1cZseuChs0p1PviI1Si9hLpsoimTIOyRgRWpvv6hK7SRGE-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20753" target="_blank">📅 01:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دو انفجار در طائف عربستان</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20752" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCuujc4leOnJ-xXtYiGqHfgCd8WBxf-P3vHSwq_Tz9FJ1QveUTUq-N7tfSiKEA21y2RA17LI1DxieS_S98fShoLKHEMsIDnHHSTSnfjmX5tECc_3w7fbxCb2Grsdm1OP60nOzYBVQp0knf6JnW3QF755hXA3-tZmfsIPEJtRpyvbkfCF-ZVzllokY_4azM90iC29lVe7Iz8sCasQ3nG7uKn1Y4qZGcy7B-RzJi6YIJHDepD5y4zTOTr35m52PxDl9Ke_GaYXNkWkjicCB742gXcdlu2HgVp5I4ypLwRe1vBzH4EHi1UhwjzdBBVGxUB7QFRpKpe4z5CjPj21j0D5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک؟!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20751" target="_blank">📅 01:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پست ترامپ در
تروث‌سوشال
:
این رژیم به‌زودی می‌فهمد که هیچ‌کس نباید قدرت آمریکا را به چالش بکشد.
ای مردم سربلند ایران، ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20750" target="_blank">📅 01:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">برخی منابع عربی از پرتاب موشک به سوی تنگه هرمز خبر می دهند</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20749" target="_blank">📅 01:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20748" target="_blank">📅 01:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">لینک ویدیوی ضبط شد
ه نشست امروز با نیما</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20747" target="_blank">📅 01:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja_Q1BjYBjozaSKBLkBdUwyB9QlSSkjf6ib-yqHnq0iJ1TQYZ0v2dKpHZzujRT50w9l9hZP1K5RI51EtoTWPrSvW51LBueK-iWgkvPu9sH1IkZmlXczqnaE-OvVvW2dyctWXWETi4ckyViA618A1C5xybis-PIqSuSOm4LVmsJNCWIvL0tUWyeguhq55j2yZI1FNqDpmzpQGrKlnjXrq0F-kHSwQ1HbXjGo5p7IKUkK1RlkUpO4I7BJitqLk4-ebedJpRK886fbeO4x923UuK5rZvAnbDCH7MRGYo_jQVCn7adHaJ2cbdS9sVa-ta9o3GTKvmIetC9LuTa400jEUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20746" target="_blank">📅 01:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20745" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20744" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صدای انفجار در بندرعباس و سیریک</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20741" target="_blank">📅 00:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20740" target="_blank">📅 23:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlEk0eG2DETSDCMceJ-BaTtHXZNehZiG7R8Wy0haGDYORSig4Cx5G8FExFRsPz2uB2vEMcKLTuIkpXQHueXTnbhcNYTtxKMZemZvuGP1e_em9H-lrwnsQl29eCxxD3JmodUkmDxGlQ7pReUBzPaweDPuYtUOK7C2mxDSbDBX5yjRCAmoO6QlDPBTKf2clKWpVEtLmXneJYWQag0bbVdUPUb1OM5Bys-uoTcY9BxDeLZXtyehbRb2gZhrVUP3pVmybCYbGvsK_9CPIdqdHNp501ibx6z3v-TGAM--AXahINsqOYpHnK9jZkFfYZT_D4wDJgAe9GV0Rh8hRBu8G_8PUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20739" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:
باز هم به ایران حمله خواهیم کرد؛ مذاکراتی در کار نیست و جنگ علیه ایران بعد از انتخابات پایان خواهد یافت</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20738" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigiato | دیجیاتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wxe8pZkn4gE02M94YRXhXRdVX5UufjlJ2o4PgTdfNr8Vi_ZK2_Wmfv1GCHQXk8Jj0JJ1uPklseZSeXV9lSIKcTguDj4mS6zrHQUzpvKYQeIKNx7S2Kk6m_ysFFrW0fUQVNAKoEtpLAI__2THsOIeRHSXk8ULDJT8DfUvj3U3wUr_KLvczUXkLtpjmcreYgaPW7A4x03u3aOYaCNjLalr-qAGrfSov_Sm7b2kEXI9vNpifejK5_r1VfyGUcwpwi7wZpG-bQrYQfRbQ2xQPK19GSId3YQaLHuXl99yK2l44XnBiMOzWbziakIllNNvcRjPqqYVHwZdA8-hlM0LKqazpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
مریم عظیمی، مهندس ایرانی اپل دوربین iPhone 18 Pro را معرفی کرد
یک ایرانی در قلب توسعه دوربین آیفون؛ مریم عظیمی، دانشمند الگوریتم‌های زیبایی‌شناسی دوربین (Camera Aesthetics Algorithms Scientist) در اپل، در مراسم معرفی iPhone 18 Pro درباره فناوری‌های جدید دوربین این گوشی توضیح داد.
عظیمی که در تیم دوربین اپل روی الگوریتم‌های پردازش تصویر و بهبود کیفیت عکس و ویدیو کار می‌کند، درباره قابلیت‌های جدید سیستم دوربین iPhone 18 Pro صحبت کرد؛ دوربینی که حالا با دیافراگم متغیر، کنترل بیشتری روی نور و عمق میدان در اختیار کاربران قرار می‌دهد.
حضور یک مهندس ایرانی در یکی از بزرگ‌ترین مراسم‌های معرفی فناوری دنیا، بار دیگر نشان می‌دهد پشت محصولات محبوبی مثل آیفون، تیمی از مهندسان و پژوهشگران از سراسر جهان فعالیت می‌کنند.
#AppleEvent
🔵
@Digiato</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20737" target="_blank">📅 21:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بیانیه ایران، روسیه و چین در نشست شورای حکام: ارجاع پروندۀ هسته‌ای ایران به شورای امنیت مبنای حقوقی ندارد   راه‌حل پایدار برای وضعیت کنونی تنها از طریق توقف فوری و دائمی تمامی حملات و رفع تهدید به تجاوز بیشتر حاصل می‌شود   همه پرسش‌های مشروع درباره برنامه…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20736" target="_blank">📅 21:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شورای حکام سازمان بین المللی انرژی هسته ای پرونده هسته ای ایران را به شورای امنیت سازمان ملل متحد فرستاد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20735" target="_blank">📅 21:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20734" target="_blank">📅 20:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شورای حکام سازمان بین المللی انرژی هسته ای پرونده هسته ای ایران را به شورای امنیت سازمان ملل متحد فرستاد.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20733" target="_blank">📅 20:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تغییر موازنه در یمن؟!
(این مقاله ترجمه یک یادداشت در یک سایت ترکی است و لزوماً همه موارد مطرح شده در آن مورد تایید من نیست)
جنگ یمن در سال ۲۰۲۶ وارد مرحله‌ای تعیین‌کننده شده است و ائتلاف ضدحوثی به رهبری عربستان سعودی پس از سال‌ها بن‌بست، بار دیگر ابتکار عمل را به دست گرفته است. نقطه عطف این تحول، توافق دفاعی مشترک مکه در ۷ اوت ۲۰۲۶ بود؛ پیمانی در سبک ناتو میان عربستان سعودی، ترکیه و پاکستان که همزمان با شکل‌گیری یک ائتلاف دفاع دریایی ۱۴ کشوری برای مقابله با تهدیدهای حوثی‌ها در دریای سرخ همراه شد.
این ائتلاف توانسته است نیروهای پراکنده و چندپاره ضدحوثی در یمن را تا حدی متحد کند و زمینه را برای عملیات‌های هماهنگ در تعز، الجوف و حضرموت فراهم آورد؛ مناطقی که نیروهای دولتی توانسته‌اند در آنها بخشی از سرزمین‌های تحت کنترل گروه مورد حمایت ایران را بازپس بگیرند.
نقش محوری پهپادهای ترکیه
یکی از عوامل اصلی این تغییر موازنه، توانمندی ترکیه در جنگ پهپادی است. پهپاد بیرقدار آکینجی، پیشرفته‌ترین پهپاد رزمی ترکیه، به‌صورت عملیاتی در یمن به کار گرفته شده و سرنگونی یک فروند از آن بر فراز استان الجوف در ژوئیه ۲۰۲۶ تأیید شده است. این تحول پس از انعقاد یک قرارداد دفاعی گسترده میان آنکارا و ریاض رخ داده که شامل انتقال فناوری و توافق‌های مربوط به تولید مشترک نیز می‌شود.
توافق مکه به‌طور مشخص همکاری در حوزه‌های پهپاد، جنگ الکترونیک و هوش مصنوعی را دربر می‌گیرد و به عربستان سعودی اجازه می‌دهد از سامانه‌های پیشرفته دفاعی و فناوری‌های عمیق ترکیه برای مقابله با حملات موشکی و پهپادی حوثی‌ها استفاده کند. اپراتورهای سعودی که آموزش آنها از اکتبر ۲۰۲۵ در ترکیه آغاز شده بود، اکنون از عملیات‌های تحت رهبری عربستان پشتیبانی می‌کنند. این مسئله نشان‌دهنده یک ارتقای راهبردی در توانایی ائتلاف برای انجام حملات دقیق است.
تأثیر فوری بر حوثی‌ها
تأثیر این تغییر بر حوثی‌ها فوری و شدید بوده است. پیش از این، مزیت نامتقارن این گروه ــ یعنی توانایی انجام حملات موشکی و پهپادی دوربرد ــ به حوثی‌ها اجازه می‌داد زیرساخت‌های نفتی عربستان، کشتیرانی در دریای سرخ و حتی اهدافی در خاک اسرائیل را با آزادی عمل قابل‌توجهی هدف قرار دهند. اما ورود پهپادهای آکینجی و سامانه‌های پیشرفته مقابله با پهپادها موجب کاهش آزادی عملیاتی حوثی‌ها شده است.
پدافند هوایی عربستان، که با فناوری ترکیه تقویت شده، توانسته است چندین پهپاد و موشک حوثی را در میانه مسیر رهگیری کند. همزمان، حملات هوایی ائتلاف، مواضع و سایت‌های پرتاب موشک حوثی‌ها را در صنعا و حدیده هدف قرار داده و منهدم کرده است. محاصره دریایی حوثی‌ها که در ۲۰ ژوئیه ۲۰۲۶ اعلام شد، و همچنین حملات آنها به تأسیسات آرامکوی عربستان در جیزان و ینبع، واکنش بی‌سابقه ریاض را به دنبال داشته است؛ از جمله حملات هوایی علیه مواضع نظامی حوثی‌ها و تعهد عربستان به استفاده از «نیرویی بی‌سابقه» در صورت تداوم تجاوزات.
حمایت گسترده‌تر دفاعی ترکیه از عربستان
نقش ترکیه تنها به پهپادها محدود نمی‌شود. حمایت دفاعی گسترده‌تر آنکارا نیز موقعیت عربستان را تقویت کرده است.
توافق مکه امکان اشتراک‌گذاری اطلاعات، ایجاد سامانه‌های هشدار زودهنگام و نظارت دریایی را فراهم می‌کند و در نتیجه توانایی حوثی‌ها برای گسترش قدرت خود فراتر از مرزهای یمن کاهش می‌یابد. اگرچه اعزام مستقیم نیروهای نظامی ترکیه به یمن همچنان بعید است، اما صنایع دفاعی ترکیه و شرکت‌های نظامی خصوصی مانند SADAT پشتیبانی لجستیکی و فنی در اختیار ائتلاف قرار داده‌اند که اثربخشی آن را افزایش می‌دهد. گزارش‌هایی نیز درباره انتقال تجهیزات نظامی ترکیه به یمن از طریق سومالی منتشر شده که می‌تواند نشان‌دهنده حمایت غیرمستقیم اما حیاتی آنکارا از نیروهای مورد حمایت عربستان باشد.
تضعیف موقعیت حوثی‌ها
اثر تجمعی این تحولات، تضعیف موقعیت نظامی حوثی‌ها است. این گروه اکنون با برتری هوایی، جنگ پهپادی پیشرفته‌تر و نیروهای زمینی متحدتر روبه‌روست و توانایی آن برای حفظ عملیات‌های گسترده در حال کاهش است.
شکست احتمالی حوثی‌ها می‌تواند ضربه سنگینی به «محور مقاومت» ایران وارد کند؛ زیرا تهران در این صورت مؤثرترین نیروی نیابتی خود در شبه‌جزیره عربستان را از دست خواهد داد. چنین تحولی می‌تواند توازن قدرت در خاورمیانه را به نفع بلوک سنی به رهبری عربستان سعودی تغییر دهد.
در شرایط کنونی، به نظر می‌رسد برتری فناوری و انسجام راهبردی ائتلاف ضدحوثی در حال تبدیل شدن به عوامل تعیین‌کننده‌ای هستند که می‌توانند روند جنگ طولانی یمن را تغییر دهند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20732" target="_blank">📅 19:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">میم‌کوین کریپتویی «لپ‌تاپ» متعلق به هانتِر بایدن پس از عرضه، ۹۹ درصد سقوط کرد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20731" target="_blank">📅 19:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9R6ibbdnNqYnIqX8cM5YDa67rvLW-MTZlkDVYSZ9XfntbPxXqGSuqJ4cex5xhqTFXwoX2QYuZge6g1anFrww9lZwKZhvIkz8cG5tUXHKrMJsRTS0ZpRQy1iuHMdEtzmegIak2e0f61-p5cN_dKht6BnIYoF4Ml2G6X4orw-KqeFQT3q4zQE6p-0wJwj_ZjGT2MOpqAuPFmsJfd46ce1BlQifexcaBEX-GVriVIm0dBd6VXs2Lgh35kl3kJWPzrBcK_38Z1Y3IV6s5j-IKEYeAMKJmjVC0I24jP_yrbc5gZMEC5vRjriqWoFgLON87762MD-9y3ftxPjetuasPS5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYrxOyb67g19zSkhlmdbG0QFqgb3wYKrUfnXcjqEKKl-f2_Upr9TH-HedqCjjix7f2bC1Dkt4xB4EQua-1QRdn68PSkRlLGEIQY2OVhNL-fmcWwT8o7ZPElGEBIAu3LMybtz7hkaAtvhvQfVjCp56frfRH2DjsQUEiY388LGBzkwMXBR9Cyo51A74hhU2BipeT2CKOTu72mxHChHJBq2Swk17QGHOkUFIBuRNbRnnbeLBLBW4ZTPxvdllb0aaC-cdChgNkBMfT3RncpcZ2QxqQCwye8gRR46Xn4FvxbH5GtWIQ-xRWeFLVfATqcShOrVH2VPScdC6-zkPwwJMUJO9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میم‌کوین کریپتویی «لپ‌تاپ» متعلق به هانتِر بایدن پس از عرضه، ۹۹ درصد سقوط کرد</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20729" target="_blank">📅 19:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بازدهی اوراق قرضه ۱۰ ساله خزانه‌داری ایالات متحده به بالاترین سطح از سال ۲۰۲۳ رسید</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20728" target="_blank">📅 19:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بازدهی اوراق قرضه ۱۰ ساله خزانه‌داری ایالات متحده به بالاترین سطح از سال ۲۰۲۳ رسید</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20727" target="_blank">📅 19:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20726" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک روزنامه ترکی:
عربستان سعودی از پاکستان خواسته است که در عملیات نظامی علیه انصارالله شرکت کند و مداخله نماید.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20725" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfkCIGPJUSHhAX2hlZl1RsBWJG2Pp_eAMy-I2md4yJ8k1zvCq2ujiJfhar4-0VCUTYzPEgJcw3zGNcPlvkehm-QnUUbpqTQOQYaEwt-P5q6HfhaVVKjtNVhFpcuzPBfXPEc2ETsZ2r6tob-av4pmqiEvvAq1aRQsFUJYohMkY6d6dHF-g6Pnp3tPMH5aEfhPKila3QF4epadt-_9lc8BjsBA8NN_mCDWTQWNolV0K9GgpIqLtzkVzmFKpTKtQDWXeJWV5RQUNYw2rdpxlYISmMj8inXpp0lzKrXlLiOAcWlCxChJ9uJxyIPo52PMF8R9NTL2dr_fLAnIjVcGCvz2luqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfkCIGPJUSHhAX2hlZl1RsBWJG2Pp_eAMy-I2md4yJ8k1zvCq2ujiJfhar4-0VCUTYzPEgJcw3zGNcPlvkehm-QnUUbpqTQOQYaEwt-P5q6HfhaVVKjtNVhFpcuzPBfXPEc2ETsZ2r6tob-av4pmqiEvvAq1aRQsFUJYohMkY6d6dHF-g6Pnp3tPMH5aEfhPKila3QF4epadt-_9lc8BjsBA8NN_mCDWTQWNolV0K9GgpIqLtzkVzmFKpTKtQDWXeJWV5RQUNYw2rdpxlYISmMj8inXpp0lzKrXlLiOAcWlCxChJ9uJxyIPo52PMF8R9NTL2dr_fLAnIjVcGCvz2luqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکایی ها عموما از اوضاع جهان بی اطلاع هستند و خصوصا سیاه پوست هایشان که رسما توی دیوارند!
اینجا این منگل در پاسخ به این که چرا به ایران حمله کردیم می‌گوید چون ایران داشت نفت ما را از زمین میدزدید!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20724" target="_blank">📅 17:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">منابع محلی:
بیش از ۱۵ تروریست هیئت تحریر الشام (HTS) در پی انفجار انبار مهمات در حومه شمالی ادلب کشته و زخمی شدند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20723" target="_blank">📅 17:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خر تو خر در یمن!
نیروهای ائتلاف جنوب مورد حمایت امارات امروز سعی کردند طاهر العقیلی وزیر دفاع یمن را که مورد حمایت عربستان است، گروگان بگیرند!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20722" target="_blank">📅 17:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20713">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZeHmjYuv5iO6gflVx8jEqsAxb9IzgJvN_p_7a5pSBKRFiStNXH15PLfyqno-JNeJJ_BcJanFavLIzBZVZCoZ4PMlW4Q4SrEVBU6lJztxPxjSYTnIPUbIGYopjy8e5oRiW5yrm08nvpe0u3fxCQjO7g0aWKIuCnmRu24JRVRLhx2WdOQmjWY81s69WSg0G6j0MCkwRl6929Tk33RIA7lkTSdEYOQGZ8YZnw01LxYMWXiYu7vRqfk-KRRzh2Q4TcuHtm_IHjqF_nwxQ5rB6sjqZcxMVa82yb2CWhp5qeiXlVHV1PHbdvQwza0hwp1WV2QEdngLKzWBN0E2AxvLF3AuRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdPTJdxJE9H2zS6duUj_-MVJDWDHHe9gSCNDWfcBbomnI0vDGARhBUSqbG5j2g-i4dguodPHOGTctCc7FnSUzM7ZigRFrkhfLzWnNaZQPeFaTbAbuWEXT7nSNEd95ouFfUNiIrrBcVeLpKpOTWfjW0X-Prwrx1HBZsG4eVfPyqB-zEddsvjMM8Ys8y7VUtOvptu7yQNcUlB56knmRzeu6YbI6M81MEZ9p7DU4dRHMMbagyzfU3fW84ginXVro6TYhSD9MUVuBO1iN5TdRAjA2sEm4iarII3YqlAZbeL8C-nPp6on6r-9Mrff8l7OKdvXXPhMVvP3hNd1dhU-zMEL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPnnxDxzQ7yezG8JrVosx23A5ongctrGPIYy5CANSxGvDwj23U7AKHATXxCRrvW4ZlmNhhPm19yfD3uhUektCqSAnwascdOXg5ZjvIbyrmTGbxj9NS6CdLNi5sSKtS9PLZODnhVlMa_VMflv1M-Cd2nrhLt2AA_fEi7EeMDxtndT709-FN0erf4eGYM7fKIfPtpHn8zr7-hTKO3Uo3DQErNLl7ClaB47GPDnDiL987GaY9_bOKaWexyNfavjr_51M5IV_ULsewiJfG8OeSKdvNpNql03wbexVtaDC8XOCkIHXbeYW2RfKZiv5QXmX4COISp1dTwSQPIjnvRjzCyqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTWZlxNTJYWspJBYKC8PLeg02zuPkJKqzF67Xjqn1VTjn0CHthGC1IF0O5OlHgsvNpKXxEM9KpaCv7NdyFZlN3TLpuMoRTD1onMsng_BCJ1Y_xXcYcyrkQlBiM07Qa6G-9R8ChCFYdLU7_kJwr3luiZk1qp4tKcT708f_QGsmoZmVak315GBPGYwloOLxpsblavFSiwW-xaYVsE9lrwjn3B7CnuiLd2MFsYlJT8lxuCZG5EUqJEtARJQ0etR3k8CDIKqwsBl66uSfYfreTvVcBD7ODl8MKIK18foaEf2JRXeZHGKJbJjPkSlt6lhNlp_yzMSB3Qmg6h4feB1fy0ImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORuoGAu36xe1JoEh2ZZbIJWdhYgk5QuDaZP8eorLbwhubyeACTwItnzNIkGeNf5v6JDkx3Lql8zhdH65IaJMMCJm_YBaS_CGqBR5kkFC1oW3vSKRKdy6OZ4njZcaY5-7-lNYRcCo46IhEYQdXI-AOOCAeGLX_j2D4kTLHsV84RBy3Pzw8PAAgf0dHxP8JJ78gkCBVRx25QSle0-tu_tzU91Oi-i1d74cW3xK4E4gy_p64_HO_n-fLHN8maN25yquavekfRrj2Q-2gAumTfrYFMfbeDSTL1C8nzPuiuI4nZAJt6wn9w_6mqRM9jzNmOSiHPSWY_kaVU9MVd4Xi0QMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaNtUU3F45eB3ek6i_qiZHgX8wTLBqbxZl88yCvC12lw9RxLhnZL5Zgxk0wm7KyUdMTir9CUlLSwGniip3U7xwn2xNdOkQ1ZBYgRmn9Wt66ZaBwRtvxjTFi9XK6vvMq2PD2pI1-npmerKctGp46LBJlZcxxlfsfo8xhGcPnDovkmRCMbDHH-UQvNlFoPLxLFOS2gU56b4NpEhga2yeGF0LLJMG-3bKhtuvlvyzPXWZh6Y89i2fpm2nNX6uvqglke0AIXtSkYt60JyZyQ3lqhQlNptIESUh4cuzjNbk3hLs7qYmK7gK5-EnL_IzStAuWx1uxYW7xkZZKtBgTwIG-7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jiHUhtBPww0K58FSrqbl1KHE5ujiXbIFFWViX4wbB2d7srA68qmjVHvsmnOY_dVKhmmf8g3QV7HvHuSwPpTRMoisveWmMkTxNzU0TQCWo5k4EOR5e9cHmF2CGS4BWzW3ViexE7_s3jhlnLtxniDyU3Qrgxdat0XpTdGn_fLjabmMUj8nJwfYlA7iO6EfgTQHQ-CET_NdwtYAEDKl5MDiAXjwoq0vj9HTk0Beljf6IUrafNSqXTr8SFVmyF29ieuydk_hZcaj0yG4pArNOt_CmyZ8iXTLw-G-XLwjuFynLILO0_e0ggK98Bmgw6B3LD3Od8PEoehzS3olRxZshUdaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJeJvs3anqCcCiQMF7DRSY7O96j8DLy4-Fii_rjtZtyWL7caHnSkFpPRe9uMz6d_nr525GBr784PL13qmOn5VYVBVLyf3Td6YCDMYF7RDOLF82XxekPiOpRkrlweFv6sQYi_RNNZUM2XnLJa7suufkn6SN5eZbs8fbtDJ5UcYpHc6X8kaj6BE0n88NKpit_OdokUterC7LHtXHVX3sT4jP_6_rXRAILsh3BZ6a7s93so-Lo4MCkIlh-UTXKbbcTFUR1-gkAn3tVFlyHLk8md7GvQPmwcE0SiJ1gg698_DKAWRvETx0tYGwlzWOrGvyEZ0LZLD6EyGmShPdMLbvaQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_yAIZudhw-6e_xaZflu6K_jbjF8_PY3g80LE2qJbw-tIJotEYVcIVFjqruPdMTdvFlWwRbiCLpbbFBKvRzT3VBqd1s66IOexrhdPn7CBBg1bTDUACCmLh5UXrBYMT8Mc1EQkA75l3ulV6LlzzKJDRLh1fiVTE5RU4zNMuNavdBPmLe3L1FD3aXZaD-780jn0362jlQqVbI0xDpzNXBrm_NK3dSFBXEw6VP44QpkGRvrWP7owpsLDDD90tCCbUKPAEslli1Y7wGbckVBYGMzJYx--0Sf2hGMfiyAqkiou7mPK0cQNH_TVcli8gqgbRgxy7P-4VzgHie1LAVWN7BJmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در دره پنجشیر، یک تنه در برابر ارتش سرخ شوروی ایستاد، آنگاه که کل افغانستان زیر سیطره رژیم کمونیستی کابل درآمده بود. در میانه جنگ‌های داخلی، کوشید که ثبات بر این کشور گسیخته‌از‌هم حاکم شود؛ اما نشد. تا انکه طالبان شهرهای افغانستان را یک به یک تسخیر کردند. این بار نیز در پنجشیر جانانه ایستاد، آنگاه که دست یاری‌کننده‌ای را نمی‌یافت.
در میانه سال‌های جنگ، روزی در تخار در شمال غرب افغانستان، در جمع مجاهدین و خبرنگاران نشسته بود و دیوان حافظ شیرازی را می‌خواند که خبر آوردند طالبان در منطقه‌ای حمله کرده و در حال پیشروی است. مسعود توجهی نکرد و به خواندن دیوان حافظ با عشق ادامه داد. یکی از فرماندهان از بی تفاوتی مسعود ناراحت شد و با صدای بلند گفت: آمر صاحب! طالبان حمله کرده اند. مسعود گفت: بگذار که این غزل را تمام کنم، مگر نمی دانی که جنگ با ما بر سر حافظ است؟!»
۲۵ سال پیش در چنین روزی، احمد شاه مسعود، شیر دره پنجشیر و قهرمان ملی افغانستان، ترور شد و جان خود را از دست بداد!⁩
@Iran_Simorq</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20713" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20712">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!  از این جهت خیلی شبیه احمدی نژاد است؛   منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20712" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20711">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">منابع خارجی:
بر اساس تحلیلی که از بررسی تصاویر ماهواره‌ای به دست آمده است، در سال جاری شاهد افزایشی در ساخت‌وساز در محل زیرزمینی مشکوک هسته‌ای ایران در نزدیکی نطنز بوده‌ایم.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20711" target="_blank">📅 17:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20710">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر خارجه یونان، جورج گِراپتِریس، درباره ترکیه:
«ما درک می‌کنیم که این نوع تنش‌های بالا که اغلب از سوی محافلی در ترکیه همسایه می‌بینیم، همچنین به این دلیل است که یونان به قدرت واقعی دست یافته است — صدایی که بیش از هر زمان دیگر شنیده می‌شود.
من فقط می‌خواهم اشاره کنم که هر کسی که فریاد می‌زند، همیشه قوی‌ترین نیست. در واقع، اغلب آن فرد ضعیف است.»</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20710" target="_blank">📅 15:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20709">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20709" target="_blank">📅 15:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20708">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20708" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20707">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IT47mGVdsesEybAhs14T1uHRFR2Au27VGpJmQkFzreKyk7Tpb7-fi_sQUCc3nXBYLRyAT1u7Lnsm3hvc9G7SfPwYA-oTDLkLWA_FpeQl4IV2-pFrxCZvK7ITj5-hFT6sCplfxgcdGM5_GPHCl9msc11FBidUbiWGwrlJRfYbwLeDrhI9OGUwZbUPIOMhYfWgXoYSLwYUO4UBA_gjLAdT9FZ4TqNGhVPi0I0zVl7uz6eAV-L9F3Ctn4mzJhhEebt-KaarZIPBZ9Di8_kFzNOSC_4Eb31q3LzQxLwoZsAKitLZNVyF9-pJ2cGTCVXmpWfU8-FQDKWbSO3fea4MRJKnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20707" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سخنگوی سپاه:
هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
در صورت عبور هر شناوری از محدودهٔ تحریمی تنگهٔ هرمز که مختصات دقیق آن اعلام خواهد شد، ارائهٔ هرگونه خدمات دریایی، بیمه‌ای و پشتیبانی به آن شناور متوقف می‌شود؛ به‌گونه‌ای که حتی در صورت تردد بعدی در تنگهٔ هرمز نیز از دریافت این خدمات محروم خواهد شد.
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20706" target="_blank">📅 15:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این تحلیل برای 1 اردیبهشت است. تارگت من برای قبل عید 150 هزار تومان بود و تصورم این بود که از یکی دو هفته پیش یک اصلاح موقت بزند تا حدود 120 تومان که این پارت آخر نشد.  با این شتاب، اگر 150 تومان را رد کند تارگت مرکز تحقیقات مجلس در 240 تومان را فعال خواهدکرد…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20705" target="_blank">📅 15:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شروط ایران برای پایان جنگ توسط سخنگوی سپاه اعلام شد:
۱- ضمن توقف کامل جنگ،
۲- از تهدید مجدد دست بکشد،
۳- ارتش اسرائیل از لبنان عقب‌نشینی کند،
۴- محاصرهٔ یمن پایان یابد،
۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۶- و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20704" target="_blank">📅 15:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKrN0J4i2VY0sLl6i2v4Nnk6yVZgaMlSGDgsgMu4pdInbn8kmTB-xjvTFoglwvsxr7ZXvlNjT-VTCXUJBi5SAHrATxujKHkJjduTB3QNekHYRW18rD1WIfyvU8xnZ0Od7LEd82bRWlMH_EtR-SYtEkj2qEghLUbRImTv1-jIVNFTJjPVSU0ChRpjc0yfza4y1VHoJifMw5y4GcDOhd2_kEe8qlhDr9GGJFeZzfftv79R4T5w-YzvIqBfPhkuph-D3C-LgG-axejEKuepCwHJg5p9looNUenajDbe5CFZWxW9TWdC2luKC5HGiVecqJUPDmokPp08rGNatpu2JMA1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های رهبر حزب AfD درباره برنامه های اجرایی این حزب  دقیقا کپی برنامه های خاویر میلی در آرژانتین به اضافه:  — کاهش حمایت از اوکراین  — مبارزه با مهاجرت بی رویه</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20703" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏اکانت صابرین نیوز در توئیتر:   حداقل ۴ آمریکایی در حملات دیشب به هلاکت رسیدند</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20702" target="_blank">📅 13:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏
اکانت صابرین نیوز در توئیتر:
حداقل ۴ آمریکایی در حملات دیشب به هلاکت رسیدند</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20701" target="_blank">📅 13:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20699">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شعارهای شب گذشته امت مبعوث در تجمعات شبانه
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20699" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20698">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20698" target="_blank">📅 13:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20697">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzeFWkbAN8Q_VpF1_xy3Dn9hWTof-_WSGatzxkWo5JF5OzfQlbFh6lgDlLGGakBkqKdN9vZhggOWuWMrPf5c3fD35N5MbtXQPJy6b4ZdNuTg0fml5jmHnp4UhzkEoy2djhqNSmZJzzRsyqUsDYKRPa9Nob2fpCyRMRR_K2WgevLfQdNg5-8syi06evfkcK8np7avwZGGdD-yxTtp9yDxT5yQigLUAELsOQ02_NwJ_h7yVCclsn6ExujWKXCbeVbInEOzylBLcHiEVQ0rb2kA7njBSZSrqRWdQZWkRuq_13xi20qj8RJfG9mOU7zodKI7416BVY2SEIxNYD7MFP7Vxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20697" target="_blank">📅 11:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وال استریت ژورنال:
تلاش‌های اخیر ایران برای هدف قرار دادن تجهیزات نیروی دریایی آمریکا این نگرانی را ایجاد می‌کند که ارتش این کشور از سلاح‌های پیشرفته‌تری استفاده می‌کند و ممکن است از چین یا روسیه کمک دریافت کند.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20696" target="_blank">📅 09:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جنگ اراده‌ها در تنگه هرمز؛ ایران و آمریکا چه کسی زودتر عقب‌نشینی می‌کند؟
جنگ ایران و آمریکا وارد مرحله‌ای شده است که در آن، اقتصاد به اندازه موشک و نیروی دریایی به سلاح جنگی تبدیل شده است. تهران و واشنگتن هر دو تلاش می‌کنند هزینه‌های ادامه جنگ را به طرف مقابل تحمیل کنند و در نهایت او را به این نتیجه برسانند که ادامه درگیری بیش از دستاوردهای آن هزینه دارد. به همین دلیل، آنچه اکنون در اطراف تنگه هرمز جریان دارد، صرفاً یک رویارویی نظامی نیست؛ بلکه یک جنگ اراده‌ها است که در آن هر دو طرف منتظرند دیگری زودتر تسلیم فشار شود.
از یک سو، ایالات متحده با ایجاد محاصره دریایی و هدف قرار دادن برخی زیرساخت‌ها و نفتکش‌های ایرانی تلاش می‌کند صادرات نفت ایران را محدود کرده و فشار اقتصادی بر جمهوری اسلامی را افزایش دهد. از سوی دیگر، ایران با تهدید شناورهای آمریکایی، ایجاد محدودیت برای کشتیرانی و تلاش برای افزایش هزینه عبور کشتی‌های تجاری از تنگه هرمز می‌کوشد هزینه اجرای محاصره را برای واشنگتن بالا ببرد.
ایران؛ فشار بر مهم‌ترین منبع درآمد
برای تهران، مسئله اصلی اقتصاد است. نفت همچنان مهم‌ترین منبع درآمد جمهوری اسلامی محسوب می‌شود و محاصره دریایی آمریکا مستقیماً توانایی ایران برای صادرات نفت را هدف گرفته است.
بر اساس گزارش شرکت Kpler، حجم نفت خام ایران که روی نفتکش‌های خارج از منطقه محاصره ذخیره شده بود، از حدود ۹۰ میلیون بشکه در اواسط ژوئیه به حدود ۲۹ میلیون بشکه کاهش یافته است. اگر این روند ادامه پیدا کند، فشار بر درآمدهای ارزی ایران افزایش خواهد یافت و دولت برای تأمین هزینه‌های جاری و واردات با محدودیت بیشتری مواجه خواهد شد.
اما فشار اقتصادی تنها در سطح صادرات نفت باقی نمانده است. دولت ایران هم‌زمان مجبور شده قیمت بنزین در بالاترین سطح سهمیه‌بندی را به ۱۰۰ هزار ریال در هر لیتر افزایش دهد. این تصمیم از این جهت اهمیت دارد که افزایش قیمت سوخت در سال 1398 به اعتراضات گسترده در سراسر کشور منجر شد.
بنابراین، تهران با یک معادله دشوار مواجه است: اگر در برابر فشار آمریکا عقب‌نشینی کند، بخشی از دستاورد استراتژیک خود در تنگه هرمز را از دست می‌دهد؛ اما اگر مقاومت را ادامه دهد، فشار اقتصادی و احتمال نارضایتی داخلی افزایش خواهد یافت.
آمریکا نیز هزینه جنگ را می‌پردازد
با این حال، تصور اینکه تنها ایران در حال پرداخت هزینه اقتصادی جنگ است، اشتباه خواهد بود.
بر اساس برآورد لحظه‌ای دانشگاه براون، جنگ تاکنون حدود ۱۰۰ میلیارد دلار هزینه اضافی انرژی بر مصرف‌کنندگان آمریکایی تحمیل کرده است. این رقم با سرعتی حدود یک میلیون دلار در هر دو دقیقه در حال افزایش بوده است. به‌طور متوسط، افزایش قیمت بنزین و گازوئیل از زمان آغاز جنگ بیش از ۷۶۰ دلار هزینه اضافی برای هر خانوار آمریکایی ایجاد کرده است.
فشار اصلی در هفته‌های اخیر از سوی بازار گازوئیل آمده است. قیمت گازوئیل در آمریکا به حدود ۵.۹۰ دلار در هر گالن رسیده؛ یعنی تقریباً ۶۰ درصد بیشتر از یک سال قبل. اهمیت گازوئیل بسیار فراتر از هزینه سوخت خودروهاست، زیرا بخش بزرگی از سیستم حمل‌ونقل کالا، کامیون‌ها، کشاورزی و زنجیره تأمین به آن وابسته است.
در نتیجه، تداوم قیمت بالای انرژی می‌تواند به موج دوم تورمی در اقتصاد آمریکا منجر شود؛ از افزایش هزینه حمل‌ونقل گرفته تا افزایش قیمت مواد غذایی و کالاهای مصرفی.
تنگه هرمز؛ میدان اصلی جنگ اراده‌ها
اینجاست که اهمیت تنگه هرمز دوچندان می‌شود. ایران می‌داند که نمی‌تواند الزاماً آمریکا را از نظر نظامی شکست دهد، اما می‌تواند تلاش کند هزینه پیروزی آمریکا را بالا ببرد.
حمله موشکی ایران در ۵ سپتامبر به سمت دو شناور آمریکایی، هرچند بدون اصابت و تلفات بود، دقیقاً در همین چارچوب قابل تحلیل است. تهران می‌خواهد به واشنگتن نشان دهد که اجرای محاصره هزینه نظامی دارد.
در مقابل، آمریکا تلاش می‌کند با اسکورت کشتی‌های تجاری از مسیر جنوبی تنگه، نشان دهد که ایران نمی‌تواند به‌تنهایی قواعد عبور و مرور در هرمز را تعیین کند.
اقدام ایران برای ایجاد یک «منطقه محدودشده» نیز بخشی از همین رقابت است. تهران می‌خواهد کشتی‌هایی را که از کنترل ایران عبور می‌کنند، با تهدید به قرار گرفتن در فهرست کشتی‌های غیرمطیع، جریمه، توقیف یا حتی مصادره، تحت فشار قرار دهد.
بنابراین، هر دو طرف در حال تلاش برای تغییر محاسبه هزینه ـ فایده طرف مقابل هستند. جنگی که هر دو طرف می‌خواهند دیگری آن را تمام کند. ماهیت این جنگ را می‌توان در یک جمله خلاصه کرد: ایران می‌خواهد آمریکا زودتر از محاصره عقب‌نشینی کند؛ آمریکا می‌خواهد ایران زودتر از استفاده مؤثر از تنگه هرمز دست بکشد.
واشنگتن امیدوار است فشار اقتصادی، کاهش درآمدهای نفتی و تهدید ناآرامی داخلی، تهران را مجبور به پذیرش شرایط آمریکا کند.
تهران نیز امیدوار است افزایش قیمت انرژی در آمریکا، فشار تورمی بر خانوارها، افزایش هزینه حمل‌ونقل و نزدیک شدن انتخابات میان‌دوره‌ای، در نهایت افکار عمومی و سیاستمداران آمریکایی را علیه ادامه محاصره تحریک کند.
این دقیقاً یک جنگ فرسایشی و روانی ـ اقتصادی است. پیروزی لزوماً به معنای نابودی توان نظامی طرف مقابل نیست؛ بلکه ممکن است به معنای آن باشد که یک طرف زودتر به این نتیجه برسد که ادامه جنگ دیگر ارزش هزینه‌ای را که می‌پردازد ندارد.
مسئله زمان
در چنین جنگی، زمان اهمیت تعیین‌کننده دارد.
ایران باید پیش از آنکه فشار اقتصادی به یک بحران داخلی تبدیل شود، راهی برای کاهش فشار پیدا کند. آمریکا نیز باید پیش از آنکه قیمت انرژی و تورم به یک مشکل جدی سیاسی تبدیل شود، بتواند به یک نتیجه قابل ارائه به افکار عمومی دست یابد. به همین دلیل، جنگ در تنگه هرمز بیش از آنکه صرفاً مسابقه موشک‌ها و ناوها باشد، مسابقه استقامت سیاسی، اقتصادی و روانی است.
در نهایت، پرسش اصلی این نیست که کدام طرف می‌تواند ضربه سخت‌تری وارد کند؛ پرسش این است که کدام طرف زودتر حاضر خواهد شد هزینه ادامه جنگ را نپذیرد. و تا زمانی که تهران و واشنگتن تصور کنند طرف مقابل زودتر از آنها عقب‌نشینی خواهد کرد، احتمال ادامه این رویارویی بالا خواهد ماند.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20695" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد  تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20694" target="_blank">📅 07:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد
تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20693" target="_blank">📅 07:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20692">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر دفاع پاکستان، یمن را تهدید کرد:
اگر حملات از سوی یمن ادامه یابد، ممکن است مجبور شویم توافقنامه دفاع مشترک بین پاکستان، عربستان سعودی و ترکیه را فعال کنیم.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20692" target="_blank">📅 02:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20691">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuWXzw6DTIhlydPIImWFttF2ae_rRRC3GFO04AtVBoj_TARVFYUKxmaiG6c05oYjg27PO806uGinpP2GsY5HLlj511BeRcXmUOy1YTGfeAPHp1cB139GYFZdoq5Q93NWQdSGMikBIQWDh6Fx9owHoLrh9C9xF51gSVuQ-yQkSEAMGytv_e6z0WRXC9GLR8m7z5FszdJAKk7EaXEvvM7WWyRKun_BR7hhixfKUSx3Ly5yz_4LmbjnFeB0i6nTzz8U8cE8C01VB8IQKZzRPJz-EAR8_d7fs4t0oNfhsE17YY-3oDUlV31zNEtx-yA-ZtXe_3NIz_UQ3qwK3HCp4fIIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه شلیک انبوه موشک‌های پدافندی اردن برای دفاع در برابر حملات موشکی ایران به پایگاه موفق السلطی</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20691" target="_blank">📅 02:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20690">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8172d6b5b3.mp4?token=up_144rVqWBLTQdXDNl6fYwlJQqZwNvarzdl1__2uhSuX2qezeT3MaeMe3nMc7yhvdwBI4pChj6H81oSoM_CKtSTFCCTh3ri0QYklF7_ddNydTtbOZ5UeWvvCeGSnD8Y-heuHoM20MxcWEwf6_c4W2IqmZgi51k47mjluBE9Ruy_Z1ZWe8k5YVB_d792xvzGMNtlzWzfoesfy85b2KBA9WX2oP8o0jXGqHVU1f2V6kazX27Rvzw6O4tWcd7AbNgzFAzinXoaSYOkNfDUWMpKzufmVD3gYErW1mr9MgRvEvl7H4TeX4PY5R6PBI3dHJJTTQ_IWHCtS8bAb4kbuQiHmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8172d6b5b3.mp4?token=up_144rVqWBLTQdXDNl6fYwlJQqZwNvarzdl1__2uhSuX2qezeT3MaeMe3nMc7yhvdwBI4pChj6H81oSoM_CKtSTFCCTh3ri0QYklF7_ddNydTtbOZ5UeWvvCeGSnD8Y-heuHoM20MxcWEwf6_c4W2IqmZgi51k47mjluBE9Ruy_Z1ZWe8k5YVB_d792xvzGMNtlzWzfoesfy85b2KBA9WX2oP8o0jXGqHVU1f2V6kazX27Rvzw6O4tWcd7AbNgzFAzinXoaSYOkNfDUWMpKzufmVD3gYErW1mr9MgRvEvl7H4TeX4PY5R6PBI3dHJJTTQ_IWHCtS8bAb4kbuQiHmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه شلیک انبوه موشک‌های پدافندی اردن برای دفاع در برابر حملات موشکی ایران به پایگاه موفق السلطی</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20690" target="_blank">📅 02:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20689">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH6yKR15ah4tqwdQcabK_ubK_Na48_kDSNS-GlvEp1iBIupl2FISyecOs8ULEW15i0323MZMs05GuZQbPEUVHs4pfe86YV-pPYgoEl9aoezJt4oYq4el508NnSJofIDN9t8dUJ9Y2QNn205nUgNsgwb2EayFHN2AuQ6PvygZBygngADoFzbSriuBYlS5us5itwiyVJyRl7QZm4jTZdZ8BA7gEawKDCjlk1Mhp1MJc9jyKqJExws9ohElZObI5n390nK7Kb_lKlXflaMZz26n3QxzzN844IZQJwaRekh9udLOmKoGG9UfDrcHHmsc4WHQBpURG0w21JJ1zM5Fc2Bs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20689" target="_blank">📅 02:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20688">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سنتکام:
نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، ۵ کشتی نفتکش ایرانی را منهدم کردند.
کشتی جنگی ایالات متحده با موفقیت از حملات ایران جان سالم به در برد و به گشت‌زنی در آب‌های منطقه‌ای ادامه داد. هیچ پرسنل آمریکایی آسیبی ندید.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20688" target="_blank">📅 01:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20687">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03fbb033c5.mp4?token=MAt19EIf_RE4KrnQMc0BB_TOwZU41DlLjzx7VUTO65MEJ8PDHQbpVxLEDCx1C1JieuJIImTvs1CX9juPgYeV0hebBQTyE0iq8p3SZ-S2T78f07q8YhLDSHkuuWcwo4l1DODLuqAeNGNoMFGrE3t7iEWpSOARxIqa20hzc9IGdiy8eWCsX4JQz9cG1Z8bdzlT2WH0OqcGKRFR0_4vpnPQzoyb1TNXhNhjpcM8ujnjy4sCPt66ky-m3FvYd6Z-6xrz7ex1PcgV2H3AvfL89iWXHqOIzHNekkylkZJ2qQdWYQv-dM6IrVTLYeoOR9R5tEooYHAppdArOdFVnRj4ZlNkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03fbb033c5.mp4?token=MAt19EIf_RE4KrnQMc0BB_TOwZU41DlLjzx7VUTO65MEJ8PDHQbpVxLEDCx1C1JieuJIImTvs1CX9juPgYeV0hebBQTyE0iq8p3SZ-S2T78f07q8YhLDSHkuuWcwo4l1DODLuqAeNGNoMFGrE3t7iEWpSOARxIqa20hzc9IGdiy8eWCsX4JQz9cG1Z8bdzlT2WH0OqcGKRFR0_4vpnPQzoyb1TNXhNhjpcM8ujnjy4sCPt66ky-m3FvYd6Z-6xrz7ex1PcgV2H3AvfL89iWXHqOIzHNekkylkZJ2qQdWYQv-dM6IrVTLYeoOR9R5tEooYHAppdArOdFVnRj4ZlNkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردنی ها برگ هایشان از مشاهده موشک های با کلاهک بارشی سپاه ریخته !</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20687" target="_blank">📅 01:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20686">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حمله ایران به بحرین</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20686" target="_blank">📅 01:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20685">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">من تردید ندارم مرحومه مغفوره برانیگان بخش هایی از اثر خود‌ را برای توصیف پدافند اردن، کویت، بحرین و اندکی هم خودمان خوانده بوده است.
مثلا اینجا به انفجار در پایگاه پدافند و شکسته شدن دیوارهای پایگاه اشاره دارد:
In the night, no control
Through the wall something's breaking
اینجا به تاثیر جنگال و عملیات SEAD روی رادارهای خودی اشاره دارد که کنترل را از دست نیروهای خودی خارج می‌کند:
You take my self, you take my self control
اینجا هم از قول یکی از سربازان پدافند می فرماید از این وضعیت تخمی خسته شده و دیگر اراده جنگیدن ندارد:
I, I live among the creatures of the night
I haven't got the will to try and fight</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20685" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20684">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20684" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20684" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20683">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آهنگ زیبای این شبهای خواهرمیانه:</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20683" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20682">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اصابت بیش از ۲۰ موشک به عقبه و الازرق اردن</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20682" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسراییلی ها دارند اذا رمیت میخوانند</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20681" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
