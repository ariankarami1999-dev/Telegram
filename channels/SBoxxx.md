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
<img src="https://cdn4.telesco.pe/file/kUdLRRA6BX2O9K-cNlg-dmJk73Nl2ngt6TrYLOVa1ZYGwsfIuTnYY4-08r-rjFm4vv_qCNB_Zr3GUTJ5vKaQEfGIoOm4ngpHij53D696xEN6fJNNM4C4fed4ht_3W25XMHvJvh0fU11tPgAtp2daich10HVH6zbLmOBqfCZGJkKS9UyOB97Tj5tu_YhMqsWUxDE6cA6-a8LPOqeBsPLRyxDifeZf7jab8fDYiOS-g4QKK5UXxqoa-pRt4-kme8glM3tNV3ocS_ni8goYh-kuPHeH7_kXceZ8RJsOScnuHJ5Z4px41GtgBJWVfBt7SMGZ77ElykMVyyVzf8-g9vk3uA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 19:40:24</div>
<hr>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXec92vnkhy3bhoxt3tmxs5ZAhYZYNL609O4dRrHarKwyLdxXdtYvihqK06xnJP1nemJ0L4PxQ8qlb_QCTOcg6WM3uCjQMtQbcitxbBQ0myCow29g0JhOLKXkJvSPv9mtfez5LksgcNV6B1c_GOoraR1SqFHrbzqIyXrXSGjPVVtR4VgpE01iLBak_ixVZl07Bmq53DmTPX2AA3IKRifkPlaiDBI70M4zzJP5APRW4t5-AawAnbx1a62KJ7nT-hRKZ1LONNrzexcZ4pgfRe-R90UR2vRoUHduD_unI9gIbec_XxFsB9yqNHZSlHpfxbE6OarnQHSMk8tJg8e4MTViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 18 ماه پیش می داند که چین
«تا جایی که می تواند از اقتصاد و حاکمیت ایران حمایت خواهدکرد»
و البته از
خطر و ریسک این All-in کردن به اتکای چینی ها
هم آگاه است و متوجه است که به محض اینکه آمریکا یک امتیاز اساسی به چین بدهد، ر
وسیه و ایران هر دو
در موقعیت بشدت ضعیفی قرار خواهندگرفت.
اقدامات احتمالی ایران و پیآمدهای آنها را هم دقیقاً
1 سال پیش در یک نشست لایو اینستاگرامی
مطرح کرده بودیم که اغلبشان تا کنون محقق شده اند.</div>
<div class="tg-footer">👁️ 92 · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQLx8iSxwDe-pxoXIKF0oohRRPcakYlkuYPLDNrttmdlJRcJP6IjsRGNbIKcLoJY6tY5NsmU17i60RhH4h8tHd-LspdPCcdhCUezH-JzKLFT51sNh1TjdjCT5w8D542fl-y1PysUOVvU0kXfAv97J9V55D-IPBQf4m6G4M7JLJik8KWrrRLEhQUtyLWlbup4_OYvwXTXAE_tsbqhHODzElOmO50U9-UBCcVi-eZ4hpHh0uS2n4_wCcA7eSvj1mrM8qqddsEIY5XU6M6NZ-PHC82yraYKelx0PB0010lMJqvwjp-kVoqCJihADkojC2Cdhnmvd2KvTUFCtc9MSJoo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uFZ4lmT5waVr_cYAdntloTldDAlUKpxV5Bu9qUN1wWmApC63OCySX-iFuAgQ9jOVar50pa49vXA1QwxeYnsDVGoBEjtobybGVAZuDBt2uO1TVd1L7NB94N-e0P9yGPW1R2ng-wTjbe3ClqMNgMzAMY7owl48u2NigVLFlprTEH79Y0ckxeBpcC69_GtIlDBDpT11QuKHJ5ZvYvathBipgObYNTG0nCh8YQXJL6wPfT9qLDPKZNR0lxPwq7zrADAAmCAD31G4tXrtrEUkOI7-vwIIsedabsfHcR0cqXy-foq1mLqtvvvB0GpjJYsTMzpNTDAvxQ1a6rOZmuMBSsAzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uFZ4lmT5waVr_cYAdntloTldDAlUKpxV5Bu9qUN1wWmApC63OCySX-iFuAgQ9jOVar50pa49vXA1QwxeYnsDVGoBEjtobybGVAZuDBt2uO1TVd1L7NB94N-e0P9yGPW1R2ng-wTjbe3ClqMNgMzAMY7owl48u2NigVLFlprTEH79Y0ckxeBpcC69_GtIlDBDpT11QuKHJ5ZvYvathBipgObYNTG0nCh8YQXJL6wPfT9qLDPKZNR0lxPwq7zrADAAmCAD31G4tXrtrEUkOI7-vwIIsedabsfHcR0cqXy-foq1mLqtvvvB0GpjJYsTMzpNTDAvxQ1a6rOZmuMBSsAzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S83jB46GDI0Fo9gsuFkDF7sgMTBBfxrbMJSsM_VK9Kg9cQIs-Eq8XBKjtr-uXxoxi6Xq1JcBQnwKTG7QsoZ2klT-XYZDKm641CayvVeUaOlj65uyLZNFoH25DDrdvFAQK9U5_5llYtM3knyrd75qaQtb7GY1SCTUJgELYOsLAGFz7DD_hMQOfvPUw1Uu1dYzerUN3LRtigbgeI0bStzOAs-5qFoKLJhGDGk5Uj0GKytYbdxrxkAzN8wPsc3qh20CJymVh-6ZNT6nM80urO7vS2rVGeEcu2iP3H7reJYR0wW3cfUAJ2Fmgk2kxIC0-B5QqCVR5XW9ObJErWkfRKnjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qwy4MwPBj0CV0ArKtWoDVrqjrE04A_VZ8dVZO-VD-ZW2lFKTu6cjJJl9He-wcXezfWQmul37ITr5KUeyxEcHaFsFXEWwKPWeX257koIFpMhYK7U8cb_oBN_h5AB-3rIt6H4YzSODJVrHQg-80xnFBB8umW4k_kGFuitM4fhi-YVrg91H4Nx9gtzJnwP_mvUuJCNi_aHGUZ32mtS5lbUkYElQL6kYIRDd6n03dMVN85DFwU8atzLfKWVsMf5F5yHRkNROAQ9EEXfskRsYnVMnDb2Ne4fchTac9BjUoA32c7UPhkt-gUczz4Rc-yrjEL5rMxZBU9Zqkoo3z5u4cq61gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNS8Gsot92uRlwDDEmaaC-aBITySaIgoI18JowbZIIns49XomhBye2iYoxdRmfJOkWw871twQHWJ--s9QS_BkxKNi9jeTa3Ys8vmaF1IrPehlF0AZUSF_EFMED38W3WU4qx60dJsKicCZzdFSSOe79pb-UeZzZgKGH9Ve4dlb_FrbVqiQoJJK5pdwn-V7JgGZI52lN4RUesp_pVKCvq74tmifDzg2T5FInT982nJjr5nEWEKcnTeYIR_P_P5ZmleUbEHBCRGScg3uSMA_O5AFEadYfcPEJcYkMFmPuRFOYy6Y3i6VRx6eitZLLooMYEj1LuHWTF7nYWMSkGQgIoVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhfACF52uauy_6kl2UAp3gbPVGqz3xiPKLnEwpV5wFf9gR9Zk9LMlRk64j4Y0GxLiaYp7KwCSdzxG8KplPeSi4ZSexAcXLDopBC9ZpQcTsIyDqdNffYlGsXIg9xbvnAWntWxvyKPgLmZAbS_yf4p8Rf2Lv9-RY64bXCiRUJ4phA_CjZrv_aftejYkMUFIbkUHgU62GJccrYKF3JinNIc7ABYfsFlAuu6wlaxpJRcfVU0HKjz6J79rysqQSKJ9SQBkQ3o3zabcUq14r5yQV8S8C1fMmby6gk2cZ5mgmw_7wiHEtJZoNfYLBMlsmZkPzAHo_LJle6jg5bPa8e8S0p3KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fperqOWlMGj9CiCNFqCHpAKcOi3D0xt5RuXnuO_lzyZ0o9lbQhLVg2l5mUwkA2JMUrigDBZ_9R0o7BUWQt2-p9lAL2yvWVCpdvlWLw1TGWGlFabpkfIvK6U_SVNgU_HExuTcLDQY8PpOvV-RuT8zV792GtgvJb06AdUlcZKY2HQZVz9-uXNFfr7XoWwSuvKzPf3u2ZYd8XOoFsfoRZtZ7xMPAM8_mpt0SiALV5fMtVX4rczQ1Uqx-6ILSvAK6Iv_Gph7jMYQL9ooQzKzpQ_kh7ZZ-j-GPH5moErI0EZM8r93T-lO3lmvI8QERQkIBHQIO36Yt1044pS3BiXADbakmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5WHSpRJgOYXflWfq1Td7gJsuCiuuqSBXWq3myQn2kY-h-eNDvJYmrAGdSofx77Gx6aJQjanOS6mPZHX7yF_ekig8bGVejf-0Zq0qIWORnejBPBnoQ8847AFsOH4VZ09DysXIlsm5UDz6aAhed4Wc8TUCeK7rHViKf45ffSJ1NBPaDNlrq6fG-tkJE-CRc6jtPTgbhZVzTFrt30HXwha-ioBh0ZfYQlURY5T6tyx0qWWr3Ihue47Nt-TS-tjiogeZ_64yFkEOaU0bmuyuIoY4tp6_LNgJ1dM4lU0WzZ9gR5INFd58TUK_CoXs-n0glWW4V2k9RmUYtECd_zKz5P1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZk7xLJ7ZacDq6DUwkyoq36-tH3tyKZ39uuXv-MKPSGYThpLyYmobCXTiQCxIbaPeQueohJSi8m8iKutSN_6pLNbVTIMnZNVjuqCKciiE78iNrMpdsZre8gCsM4tM7idJii9zSN6wrnzK83fbD-NKQhimUcOl6otOij3mVy-6Yt0Izn-ZSgLa3EfNn54Ll5ywsWyAP5wIK3n7HQw2NDy-Sy82yv-PK6NrfjsQ_bGeI82CHdjdEmnTmoHzsLNZT62SC5OJzHB1iloctuCjvxlhPMrGuKJaNuw4uaCMOAzoStNw_pvk1ArQr7idh0KtBKF-T5irB_QCxIfqIG3LHsggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=eQB95hxstEGBmKT6j0vIa16aob2T2-kUMi8785jp2uzc4RksN_w4m_e59azgmsahzLkXlqVYOte7-Xvzade2NeNHHZ0trBk3dBk5VK7l8hLNb7kIO8ds0YnL3IBEvJNvKU5BPbYzYEuyzHqMH-uXm0LtqAf09GCVzn5p-N0mYt9Cdnv6S35iIBOmelK2zsba35sch1xuiqOYcEfWxFY9IGUup_06PRJ-D2gQorUygCxh0H7dz2prYhq8mnFsxAjrXttE5Ax_B7UunBX_yJ2RXdsVhXKRU9QZ9loriZKUOgVEY1_z1StCFlv7QT25DoB_VcKQCsFU1DmNildG6hHa-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=eQB95hxstEGBmKT6j0vIa16aob2T2-kUMi8785jp2uzc4RksN_w4m_e59azgmsahzLkXlqVYOte7-Xvzade2NeNHHZ0trBk3dBk5VK7l8hLNb7kIO8ds0YnL3IBEvJNvKU5BPbYzYEuyzHqMH-uXm0LtqAf09GCVzn5p-N0mYt9Cdnv6S35iIBOmelK2zsba35sch1xuiqOYcEfWxFY9IGUup_06PRJ-D2gQorUygCxh0H7dz2prYhq8mnFsxAjrXttE5Ax_B7UunBX_yJ2RXdsVhXKRU9QZ9loriZKUOgVEY1_z1StCFlv7QT25DoB_VcKQCsFU1DmNildG6hHa-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=Gvd75Ho5YZDS0Wa2w4Hfr9lT58PwZSFN6F5F73V-IPsTzv36RyoxR8ic_jZDmjGB_63pfSdnIg-oEleeKnF0jieWXqWIMiYW6DyEkhppXY2A5E8rmUCbuWgAckCtIcMB7vt15GDLN9l5J670T3FpR0dtiRSL1fuZ0evK2mPcWSsqOopimEOh60aYHAzWOedKStsPLmDcvFo8L6PquEhVM_lmBOp_4TE-TM9aRsZO2fuUyyj8uEWTtjp1UMNK3pnh5QlZ1Lp4zNOZlf3NRQcFNxrXHj6KqD5CDOiYKl1vkWY9E5FUU4K4LNh1iab2AVLDUjj-Dl83v0DhCYcV3BDooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=Gvd75Ho5YZDS0Wa2w4Hfr9lT58PwZSFN6F5F73V-IPsTzv36RyoxR8ic_jZDmjGB_63pfSdnIg-oEleeKnF0jieWXqWIMiYW6DyEkhppXY2A5E8rmUCbuWgAckCtIcMB7vt15GDLN9l5J670T3FpR0dtiRSL1fuZ0evK2mPcWSsqOopimEOh60aYHAzWOedKStsPLmDcvFo8L6PquEhVM_lmBOp_4TE-TM9aRsZO2fuUyyj8uEWTtjp1UMNK3pnh5QlZ1Lp4zNOZlf3NRQcFNxrXHj6KqD5CDOiYKl1vkWY9E5FUU4K4LNh1iab2AVLDUjj-Dl83v0DhCYcV3BDooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxqHojIre8Y-wuWvxpxHFpz3N00etSKqb_4M7qY9kj2kY_hcfjoIJVALosA1nKo9jKqUMJ2T19GGKZtpXgXNFgiyeBEGI-ClMomgXInMjtg1up1xUPgO3R6O1Bn1EvwQjbH03nPY5vt3FpryT93jT1JnRAj2DN_EsFmadJbrlFpl9K4kMHJ5luOLdRUbXARHBtFoHks-3Esyo6f0DyOKq0Rqpj3JK-3gKLvysAy1_vC-1d3T14C1SyTPimKQkIqgAcUyRRXQEnF17VygVAKKK-neolBSwSXsS44qRz-MfeVX_Wwp5eQG-AkrIxaIU5d3CtKXvpSGsnymAd9d_mgiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CThM0CosDaJ9mwiUCYwwhShyp9txusioEPbsmRLWF3VJJshppD_Gd7qhtqwrz1bN5KennqwcVyqp3p5hSwYf8lwNsRBjsCVpR9xXkh39D93BN1UWTrtj3xXvCdTofxjKVNIJJ-U8ukDjBOp_LdJtTMYGCyDU9enQ7qZdDUYgBTx_aW7E6fd1fiaY2-zE-XY9AJhKIk8KxuYUyxXKZcpH6AmeOYPiSVDiHVrx56FPe6LM4HsR2Xny9RQXzKEYdZWgbWhcYaWnqwh5EvCqqs7P6ubOQrsseED5auRl_YXiCERdbZkCCTscn72kRVot3XY8TENcA3K8d9DlLNGQoDpoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI6gFDpX1aYBBCpqh1WA5cDbdEE5AbPM1-vTy7MLAlHLiz-kaUfJ86CgffsRTr6xO5FaMTdZD8pYzuig3UVpR6q3QWVDmzFReNxkIdXerqsGYsmrrp_PvxgWUyjKQTWy7vnmHlQYfhZfhPB1weSCZGT12goieBATBBPCDL8SS8TIUCBYEpl0Q2XIgVrQ6dm06ida9tmh4PsA8HJpdDwswkN8KBCeiErRkEOU0ejGPLoYVXvbYNa7NIGJY2zFnKFekmM1vNHOTLMS8NWoIEbWng314RHtiP7TOV6hQR6VR55a8pct23IxLwI2-FQmLUF5YfTGH4PMWjhOOJ9OBRcW4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI7btpK-E8qulwxm6SXZ1FeA0fPC0FM1wrHjTqSRusKUzedq2Pi1pUZG3MQkX4fkI_ywh_X6w3JJTEeo66VpzdzGwwvOfo0Mb4t5rpcVgrYrninqswyKlagksuXntTVWSnzNBqo54Rf6oMeJEbbhEGK8Ju7CrQYXAVr_oC1In95sOTFkZdDXC0v7oI9H5VMfhn0KTffUJfrISGuSBZf_cF5yGXYna3uQpJngcUZqZL3QhzqzqtaIKUTOd2brfHhouC3vByMFS-VhtVqigIQtRLEzx60zDU9qYn3s5yXmTGOyQacYq0OgRdN6eGc6Yqxrm09tHo0D6oWYxy4HVxTiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrB7ZfA39ukXr-OLdOTum2B-ZNWUDT3uCDjdr2UN_VqAlClaXJv_kk-Plf1Ec-rkXQU2AZfLoLXknx5RI9tq0Dk1lq9TMyqyUhmxzK7CZ5qHZHgjYDj7KSyvHl1ccCa9cfVNk5j8g1MT3oCy0bEwuo1LjcBy5JJrZNlEeiPPDMzNBZZnSWkFp467h8TJYDdm-4izyXMpORVCANjOjEbGO-zPv2F7JCtoOwI-vAWzdn4ixQGK3ZkgnizerjY5ABClZFzODAHMF5LcpWEEwQUIUsbon1dvBfvHu_JzgTYrW8jVd6ES_tEMyfdXs8hUdwe4Tg0zB_rLK4klGTb8EUUYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2IxW4i7V-v1gq20LV5COtKAQ9t09mOgwU2Sq7wyL9MGYoTuh6x75LzLW5JwfEf5jsssywEm0QRlBNGb2mZGJgjjyPnnv965r0ZRqNpKp5MQ1jaz1MU4D_n9IwBQUZxg-5LqUS-iO5g01rK71Yg1JSzKpmSsfg75S4-HM93wPw-zVgmksWbqk5TqpYBCjz2wciFRrlJLJryJDiOV8Vx9bH8pGbNpTMcfuOWyJUCFECHQsTVu_FhI2-7maNzLkjN89zFgbepG80Xp7JIObbNjQABMM8F-g8ECy_G-1Qboa73mJvRaw59oAfj1Bb4NveH06xryWB9EkufNWPm1BD9VGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_4ljcd9a67zdMI_uYa4XZzv_BECqfVsp6buEMR4HEWUx46FjxblcsHbt1QQqoNEbkhkzDXNGTVgX_GKZCZ-YksqpIxS5m1X-zO_fwDWgYvq8JpMRnt8N7QHnseS7vav4lBsTUy6NiT8iVcNZt1ZDwo6k09v74a04snuUyqpjXzrWOS0WTjK3tw-q6If8cCi-95FBl9K-R8WUUkp2ugH1Oj6hnRKIe-4NlinGPlMQL268PAvUjyMPuqdFs_kxWCO3uLM9r8Q0KFhm5Xk8Rkq9nfrEOlOlbSp4fMJI1vNmcAo0HUvoxCb6z0dEeLG8ZdxDgRzHkJx5ED0gqsFor4MFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhTEREfjYHTfTxhaIB9Xnrdi-BRyZDVyX605H12km3DWAFn3oFRWYcsFPNQ7f1N6OyySLMxVyMY0T9nxy02C9c0PoIW7jjfcg6g4DpZaDtQrhWbTZQW5kgkBG77pvH4HqtcT85yHxFFqHhq964gPbbS00VUePMsNhegMT2WE1b77vuTntSVdYG_xB654-3K3AdLGNOLRObj9_PYg0aqA3ZepVJDOnRd-zr_9QhX-Fwv2mWJIgd1Ma09A0DXs5TgWUjPOns4skuxIfF4X_pkc7VT4uwWAqQYMbe0OrTuI5EyDHQTgAAMmjeUkSVrWEaOBIFH57cAPAw1gOn0t2HbqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJebvRgehbxDftk9_4PtHWri_T2by8x978d7N8J85Wrq5cDzqBdxMXmHd8eMaJsoEwydlWjjwpErsIHoR9KWNRvC0H3FlM6Z7fDJ-nwVgc4sbyCpQ_UyVNrqJSiAJwOrsW6ZEOlhQswUQgSGBJbCQcNim4HlLkfE6gVBQD_7ObkDhBPc5SjuUpJeXMTT3r8q4_6aVTei15sOXowvgzI0u96gQFDLxVMb6QkAVHWpduaCCaDD9lWpPBa1n3VdT5Sxmxb3b965_IDBK5k3_4_edod02q_2gPm8KsrGuDMdvfaFakTo5DOB2tsWQqzagS5YgCag4uaA3sp5tOm_cHcVGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODTHWDL3Dp8LifRoVbDBhtMkAJywutRBERD4ynYeQneIA_t7KJdPi67M-fhg798MK2h365yfgfyOynOJeril6HiKHsrLCEg4Dt8DVPTHakuCIChQXm4FCNDH23gPUoLkjO6u0Avlw5Q2C92XzAcpR-1TA-7Nmib0ECzHI3mj1IEAybyi13OvXDZ_FF6iWDOjrxqwrCo3u-CqF2rksTtI0sEBCYNckXTlyDaqnraCHBg1zhfmTm7iRWCyRJSN_debF1EeyMwczEHDauGO6O5uTj8nv6rEZygu1sGBJByk1R20ReGHON5DOjf1IhBM-o4HyG5MPPevkxri3y5eSc3xIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJ5cd-fZtFG6Ka2oJwrqAWbit2FLKgm0tugsVjlIOL-JyRdgytvBB7MwECSBXXsyE9GOa9bOH3k0AFKmMPp7py1lJsUF-JRa5OuisqKkPSHXAyAvOm5hNhPFM4BLiG5gX0XbDIrIzJDPmuLSF-7byB6aw6gg0IabdgsJz1BDk5oTVwLMyo4srX67FOMCsbGBuvoywdUHVaRMmMKOAa3W2OTntceVgUIGofASgY94krjB1YfIOz0CurpVUxZs5_jiB1xY_yVgSbZsdKDHHRBMct_hIYpdbH8GdBKxi7YQT1An3o1SYca5qmhn1VhR40gEi0Gj7fZBgdIti281gn2zFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/benlTJIG7UdAqF_ygVktlP48oU3UNkkjxlduyLfcInah7-OIm9woWrEL3SzctcOLuuymUQOJN0ja44nJSOhnbP73OXCF5b4iTQp9TaOmLUoQx3EusZdzldEAAXjofvCp4uNaN6cn0Rtv7IpUh2d2bD341Kz89zF2GPbbILOEQqveryafzFgOaharwfRfRUFuwmaQaQKG95vT51OEJqag2JO0CuMHDAvsbzsJygrbQ0eTvQrvNYUfNyJwl-vepXrpCP_-wl-pUuB9wvh-gNOgW6UAmysEqmqmLEKajqmB8ZeveNGGhds9BQoWWXSMQa4fTR83ffhMsFixsK7rZslGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.  دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.   ولی با این حال، پیش…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20185" target="_blank">📅 03:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فرمانده انتظامی کل کشور در ساری:  جنگ سوم هنوز تمام نشده لذا باید با آمادگی کامل در برابر دشمن، غافگیر نشویم، چرا که خیلی از غافلگیری‌ها نتیجه غفلت بوده و دشمن از ما دست برنداشته و جایی از ما دست بر می دارد که ما دست برتر داشته باشیم.   دشمن به‌دنبال ایجاد…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20184" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20183" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=o_o10JLpEg72SUghf2WLw7Rr9OHCTSLXksQVWGj9NzOgt2bL3YBysho7Bw5TgXZRdKxekpg2ODuSQ9AabFz-68LsjvTcrSy3KgH90Wz942tn5OUo8cBZe2mcl9BawN9nJxQgEnjYWSwBoZPR4foHyt9Z2Epn-UGKOIoSbh9Ab5z1wFbTK18jKyVBlJ8wdWJsg1v10bgtyTEeuivdPNBDSHwv588l6YYMQbMFjOzFLHdN6xq6ZBNyIaOvtwRdR6YqJRnvfWZdH4qFcs5Oe9HseYx6SYkp4YQcQvjJ-hdxDCpcShOruM-YFjytDdL_-IYmxPCVYUzNI1vvPvYJZQxInw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=o_o10JLpEg72SUghf2WLw7Rr9OHCTSLXksQVWGj9NzOgt2bL3YBysho7Bw5TgXZRdKxekpg2ODuSQ9AabFz-68LsjvTcrSy3KgH90Wz942tn5OUo8cBZe2mcl9BawN9nJxQgEnjYWSwBoZPR4foHyt9Z2Epn-UGKOIoSbh9Ab5z1wFbTK18jKyVBlJ8wdWJsg1v10bgtyTEeuivdPNBDSHwv588l6YYMQbMFjOzFLHdN6xq6ZBNyIaOvtwRdR6YqJRnvfWZdH4qFcs5Oe9HseYx6SYkp4YQcQvjJ-hdxDCpcShOruM-YFjytDdL_-IYmxPCVYUzNI1vvPvYJZQxInw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20182" target="_blank">📅 01:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کری خوانی وزیر خزانه داری آمریکا برای عبدالناصر همتی:   به زودی دلار 300 هزار تومانی تحویلت می دهم</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20181" target="_blank">📅 01:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9fjsb4RTbkqEQFjvPaDKOi6yRj8YGSr4IVu8WaZSNfDipEtOh7FJmXsrpmsfOGMzBv_t2UtShKhJoywRerF3L-y7O0i-w67xDNhUS6mrharYpsFibf0z9QwAW9dIXHAShQDee0KYUL2bx8jQiUQG52DkYeU59sqqRUAy7icownlNIUVvNHOe4sEIiCPv-mTkt4-od79VGg8TNZCrghHu3IUf5VBsk626Uuhyxlr7qMKsxqEVGL3IeMA67uwazB0EaNaARHQYnWcmw-BsyN6z4ikbsFlAkL4Ek9ZMtSOVAg3SSN4QSwHdUNFwRSBzfcIs5FkiJh4YrD7E7J_1yVj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20180" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20179" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUE0M_MB0LoYgkdE3CvBjRmyZLWnF0Mt3G_MPkej9CbgZZiMH4ak-PWMeEtBSo2ET51-4C4qM6wv7I2ghA0wGEdkIJL9VCOXVUv4Z5Cl4EMMsozAWN5ka0igSfxPvNfTle_3Te-90mOMyvORhSePcDoIAe1xjL9xNCFL7JYER7CUZY2fW6GYWRO-wUFSaO5SifV3amqoWHR11Ulumau2kcofZ3RBxuh-6ZkhR4cxZB9Rp0fmEG-HoDRD8hNx-kAHLpz8u5rgx1UgDCb_wLpwlkUhJFhxz3_inZ-1QD8_8bZb68StgZsx3trcc7v7qKGRBIX43QqfwyCP-JUuZHno3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/20178" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسرهایم را به قتل برساند
کانال ۱۲ اسرائیل: سانسور نظامی ماه‌ها انتشار جزئیات تلاش ایران برای ترور یکی از پسرهای نتانیاهو را ممنوع کرده بود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20176" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «خطاب به سربازان عادی حامی این رژیم: همچنان که حقوق‌هایتان بیشتر و بیشتر قطع می‌شود یا ظاهراً فقط به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشورتان را برای پیروزی ترک می‌کنند یا برای ویرانی، و به یاد بیاورید…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20175" target="_blank">📅 21:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «ترامپ در حال برقراری تماس‌های تلفنی با رهبران جهان است و درخواست‌های مشخصی برای توقف تعاملات آنها با رژیم ایران دارد.  اکنون زمان آن رسیده است که رهبران جهان بین آمریکا و ایران تصمیم بگیرند.  هر نهادی که از طرف…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20174" target="_blank">📅 21:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20173" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
«امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.
ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه شریان اقتصادی است که این رژیم استبدادی را حفظ می‌کند تا زمانی که تهران به تنهایی بایستد.
از امروز، ما حلقه محاصره را تنگ‌تر کرده و هر منبع درآمد بالقوه‌ای را که سپاه پاسداران و رژیم ایران را تأمین مالی می‌کند، مسدود خواهیم کرد. ما در حال اجرای رویکرد «بدون نشت» هستیم.»</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20172" target="_blank">📅 21:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20171" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR9uLdAbzzCoZBTenPO_HFeO0rEOnlLuodPH4HIocr_cU7Vy78rKYqmmi_ljdgRIN-c5btMfvzyUna5lVtkE4eVIzkdlqd8OqN3qiT4VvQDD9SO76veRMvOO9j5WE3iw8ZlECnd6_4gabt1dfVHhUK7o8LEufoP8WnEVA9UaxYJJhtWdSp_rkEGa7brt7VUn5G2pInXAKmuqs5ZiKki-pbCnfravlHN6J9tEXH4lq8qL0u_o7i0CO7x4gDmqWD_r635DWlXPzvqE0MKSJurzJVGTJ773HOuKQuQ7b7kTNDDrVsIvER30ljboV2QVWho_GQKhtiUAfW8QrW013cVcNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2.5 ماه پیش میداند که هدف درگیر کردن ترکیه چیست. بزودی یونان هم به اسرائیل خواهدپیوست.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20170" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20169" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20168" target="_blank">📅 18:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=cLr4Hh0VZSMEDga_uo-FUnDhD_OpHSXzlP67ttdpulDnCmsWcw_j4_w63AZx40tK2glpT8LoC4Dy1msDalIw0nM-8tuZg15ERESRgnFVBVgRUZ5D4PzTDPV3kr2oyZUFjs_CPV6wunoQx5Z9xZpxxqdK631A0pbIeqg-EbuFKMZDBYu1FmOLDTn8Y0neQhOokioUSl7cBPeR_XvzfTFCBPF9NodTJ7np7zTBXlrBYTCgfU6L04q94Kd8qftc8Jud8R755FRPJuo_pOdULWFuzixxi_F6Y7wxRph32p6UP-0xN6G8tNEFgucGp2tZ9ZVa8hNoq3Qs0xH3N098Js7PNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=cLr4Hh0VZSMEDga_uo-FUnDhD_OpHSXzlP67ttdpulDnCmsWcw_j4_w63AZx40tK2glpT8LoC4Dy1msDalIw0nM-8tuZg15ERESRgnFVBVgRUZ5D4PzTDPV3kr2oyZUFjs_CPV6wunoQx5Z9xZpxxqdK631A0pbIeqg-EbuFKMZDBYu1FmOLDTn8Y0neQhOokioUSl7cBPeR_XvzfTFCBPF9NodTJ7np7zTBXlrBYTCgfU6L04q94Kd8qftc8Jud8R755FRPJuo_pOdULWFuzixxi_F6Y7wxRph32p6UP-0xN6G8tNEFgucGp2tZ9ZVa8hNoq3Qs0xH3N098Js7PNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20167" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2Xs1Te7dojgG9N4hqW56-iECmbQqPUopvftmt5w9zrDe9tEaoOOEm52azW6E16x0uzxM4LmmFlJycEw17aWLJXVJYAPCTcjB2KeW7dv2ofEbm5wrAxHmWOs6mUNWvf6Jnyu-7P19J3edRBB0qFetA4ZIR5vh3KDK5UTyLhkPsElU7q6pXJwA_R6pjzX6Cvr4zCS58-WUw-akcht2z6xjMaxwloRuXrzWupBSCx9ugMNcjBSoMkkZ3JTxCfnHZtF-lzR_y0SzZVZM5PzqgXV8Cc2bnkU8fUaSUZjusI86K53o-W1i-AqE7mHY4bPbMpdZNZbF34ZYcQ-aQ9nN6YGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20166" target="_blank">📅 16:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزیر سابق دفاع اسرائیل، یوآو گالانت، درباره ترکیه:
باید درک کنید که وقتی ایران تضعیف می‌شود، آن خلأ توسط کسی پر خواهد شد.
نامزد طبیعی، با آرزوهای امپراتوری در خاورمیانه، ترکیه است.
ترکیه یک کشور قوی با میراث امپراتوری است. آن در پل میان آسیا و اروپا قرار دارد.
آن بزرگ‌ترین ارتش ناتو را به جز آمریکایی‌ها دارد، یک صنعت دفاعی بسیار قوی، مردمی سخت‌کوش و در عمل یکی از مناطق اصلی صنعتی اروپا است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20165" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCD5dbFn9FWrpJBWXoxLuz9UyKZc7ZZdnd1ieTbnZpUjw9z96Q-CF2Qk8vhCHlDSUOG2KvIZKzIHE9jhVZFr17sjPoV4yDLjMeLCV-Upk5kzW-iaHuL0kpHwVfz90b6djwezXd7UTayenwX4eEsAWmWW9ackDiy-FvH0Bj-azBBhSGDbEB59HWel8FkAeVX7RusNewGS2JoEN5BjKbAwDJz5OVkSGWFB3sqBo_OsjRfxcooVZ2Oj3bT-DgI8Kmqt4R3alZXtJCcNqVD70RNaQIExgvCKVZk_BogQOoN_Kjx4WkkfxBv2KwkIySHmtCdKFddMKWbjupfH6ej0IzBCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک PL-15 و تحول در نیروی هوایی مصر  همانطور که در یادداشت پیشین گفتم، محدودیتهای شدید اعمال شده روی تامین موشک های دوربرد هوا به هوا برای مصر از سوی غربی ها، مصر را به خرید جنگنده J-10 CE چینی واداشته که مجهز به موشک دوربرد PL-15 است.  اما این موشک چه ویژگی…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20164" target="_blank">📅 14:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Secret Box
pinned «
این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20163" target="_blank">📅 13:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20162" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=ohitIbk_GjnXbZ6dMUoabE24IwEIOMM9WrlGvtG70_5Uc3dmMR8QKfvaj_2sstTkb2ZFr0BtHWOA88D742_IKgjUTHoq02payAknn7Zv3gtDYbQ_WVfZAx8MDUHG_IyRQhDxM22sLBHdes4EP7toeQXr6c8S9b1Zi9M_pZRGWLqG9srwRoGbSjgmP7-ZwLjDmgZ1SQuMhwPXO_clCEckd8b1e7ddxr2qic1euPTdh5hEhnEd8n91f_Et4s-lRA82QCIw13ThVm0BLVvFYuJZaD6J5gu4w1dREGc9L7KKqAo5hs4cu1S069J10QWJFBMJ6OiwtLPt4YWw47Jxj4lGb0bfD55-y7YQmWvF8MUHM_Pm-_ydpG31vhXyD_MjwTtlLoK40EWuj4UzSXdKFtr5Iz56Op_o62XXdHlZI9GYMNBeyO5XoZPhgXWX-RnBQmNVaW6olBrbI-8g3GKyhMSQUu-pn2u09NSa58Ue_LtkDaFOoCvmvIdzm3hu2ScpsMLm2yoepQyTCYUKaNaEiq_cGFYZrq0dqxRzw3nnjTG0rNoylBIvb0Kdoag_ucMOzLoH9gDAXknFFcj6fsKhG4WPI5_PoblpRSLcbhBXpmtgRga3n_T8vCnBpj6ZkwSerUBckXpPy5SC229Z0w_3iloX_aHubVLJh7IGL1Pqj966PKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=ohitIbk_GjnXbZ6dMUoabE24IwEIOMM9WrlGvtG70_5Uc3dmMR8QKfvaj_2sstTkb2ZFr0BtHWOA88D742_IKgjUTHoq02payAknn7Zv3gtDYbQ_WVfZAx8MDUHG_IyRQhDxM22sLBHdes4EP7toeQXr6c8S9b1Zi9M_pZRGWLqG9srwRoGbSjgmP7-ZwLjDmgZ1SQuMhwPXO_clCEckd8b1e7ddxr2qic1euPTdh5hEhnEd8n91f_Et4s-lRA82QCIw13ThVm0BLVvFYuJZaD6J5gu4w1dREGc9L7KKqAo5hs4cu1S069J10QWJFBMJ6OiwtLPt4YWw47Jxj4lGb0bfD55-y7YQmWvF8MUHM_Pm-_ydpG31vhXyD_MjwTtlLoK40EWuj4UzSXdKFtr5Iz56Op_o62XXdHlZI9GYMNBeyO5XoZPhgXWX-RnBQmNVaW6olBrbI-8g3GKyhMSQUu-pn2u09NSa58Ue_LtkDaFOoCvmvIdzm3hu2ScpsMLm2yoepQyTCYUKaNaEiq_cGFYZrq0dqxRzw3nnjTG0rNoylBIvb0Kdoag_ucMOzLoH9gDAXknFFcj6fsKhG4WPI5_PoblpRSLcbhBXpmtgRga3n_T8vCnBpj6ZkwSerUBckXpPy5SC229Z0w_3iloX_aHubVLJh7IGL1Pqj966PKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20161" target="_blank">📅 12:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20160" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6M0EQINlWTov2pqrpkEV3K3gd-9Tb1P3VJZRTRWS-SDAqUkPo3a8vixQGeX1LY7iR9GkMknXmCyJNcjX9N-tEbBEHv7dp3RUGvifpfkiWirT_gza9kau7kY9u9-1xoo7kcJRgsRdh-mGw_7V2mCh44l2rI_J79jLp-gykk8CVwcre9rjqzldSIT40WtA1dS7Hy2mSqcGuC4mnZYdD0QujchUzbjURsf6vatGjYDAu0X7M8adwcisd8zATvBqJJTej5ggGazPqtEk8nPWrP0kR2S1FUISNSaZL6uZ8qcp-rNpJ95U1MyHER3zAn6wD9uJ9uJ8gUbmRcAzl1nUlVbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی:
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20159" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=nnhTwwZSON3E9ZtjOdLxTj1Gu9xLZKS3wHr9yQU1ISCC4CDXgO3rafRc4DMtGBrbZyOfMi2jg5IS_rygImddGwa0sjuM_Ah08n4xv9J_V22xOWTMmNHgiDcuZkWfZo2h3YMjFTY9pXzoevqbTrmIkUliq1A9aauVo1_kHqkrRT2XaT1YrziWXJ2mLyg0cLpAYQJ6DDm3JJESDsJSIMAbb-uxfhe706ugr98IbLX3M43tgpdw00EQo437InqvQHTsihpj39doGwB4E8Ge_18IgPTXmNnooWDDy9fek6LUlxZTitVYHCePkJ009QlC88SSMPk1rMOE_gAsSm107ab2WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=nnhTwwZSON3E9ZtjOdLxTj1Gu9xLZKS3wHr9yQU1ISCC4CDXgO3rafRc4DMtGBrbZyOfMi2jg5IS_rygImddGwa0sjuM_Ah08n4xv9J_V22xOWTMmNHgiDcuZkWfZo2h3YMjFTY9pXzoevqbTrmIkUliq1A9aauVo1_kHqkrRT2XaT1YrziWXJ2mLyg0cLpAYQJ6DDm3JJESDsJSIMAbb-uxfhe706ugr98IbLX3M43tgpdw00EQo437InqvQHTsihpj39doGwB4E8Ge_18IgPTXmNnooWDDy9fek6LUlxZTitVYHCePkJ009QlC88SSMPk1rMOE_gAsSm107ab2WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20158" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">درباره اینکه پول خرید واردات چطور پرداخت بشود نیز با توجه به اینکه ایران کشوری با بدهی پایین است، شاید چینی ها به دلیل نقشی که ایران دارد روی فشار بر مالیه و توان نظامی آمریکا وارد می کند، خطوط اعتباری درنظر بگیرند که بعداً (مثلاً بعد از رفتن ترامپ) تسویه بشود.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20157" target="_blank">📅 12:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20156" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:  امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد  روز تسویه حساب اقتصادی ایران نزدیک است  هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.  جایگزین برای کشورهایی که سرنوشت خود را به تهران…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20155" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGxRyubXpcdpRXUGWf-qkGHeOMJfiyOfB2ZZo_m_TqD3xH3_ZUpQmVBgSlPzCv5Y5-zkfX9sLyr2ZB-SyJnKIhQo44PbsEDsAwpmpBVKC_Km4-x49nGJxYyn_XBrxA52-78aEzw8ny0XqCJRGeb2j9KCqAmEKKmNRNn-bOcfZIywtUGlyjWNKMBBBUDVtqPVdq5KlnTp9ur4IUkFQQT5aej7QR4cfI58oaRgIDeuWF-zYeVf_hG2DE5VfrMRwTVCl_gszqp4VpLOcVkoxmLzr7L4Rzs-HyFbnXT8NnkE5uJGdZ_UMwQQwyXbAlPDDo2XiKvLmG1HoiS7QCxY3O_kAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز گزارش داده که صادرات نفت ایران در اوت به حدود
۵۳۴ هزار بشکه در روز
کاهش یافته، در حالی که میانگین سال ۲۰۲۵ حدود
۱.۴ میلیون بشکه در روز
بوده است</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20154" target="_blank">📅 11:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ما بیشتر تیله بازان خوبی هستیم به نظرم.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20153" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فعلاً این یادداشت را بخوانید؛ توضیحاتی درباره برنامه بازخرید اوراق قرضه که هفته پیش اعلام شد و سناریوهای پیش روی طلا ارائه داده ام.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20152" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH1M7cYDcEee61CCnlO4df95W5keM01ihYPmle7qZzAu3gdZbgVx2bIViQLnvVIGF4lbQzaSB7YmqVDHGT_f4Z_vSoi6ZUQoJaRwFlVhUdRl3j2FAhTEIMH2kSOw9mexyTrXalbMVU0LnYRW2GMWo8WliQF_KSBf8hLPtssR1Ac5iaF43bC1WItqzSu1TV4N5qzAGTCb_MwlDat9hfSyZwNwEABHL8NE1w4v86kzlQgOQ-t9YOw2Wmz-KJ_ajjey0lb44P77vY6s6BlCFvjJINGQkEsD48KT9CGKJP_6iSVBZnR2EAWZF7bYKgb3z_S91QyZHsRiqy8TY_4HavrkRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.
دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.
ولی با این حال، پیش بینی می شود که شاخص های سهام امروز زیر فشار فروش بالایی بروند و نفت هم احتمال زیاد صعودی باشد.
برای طلا، احتمالاً از مومنتوم صعودی کاسته بشود و اصلاح داشته باشیم اما به یاد داشته باشید که اقدام اخیر خزانه داری زمینه بنیادی طلا را تغییر داده است و از این پس، معیار موفقیت شاخص GRI را روی دارایی های کاملاً ریسکی مانند شاخص های سهام تعریف میکنیم.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20151" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRuz2OPkK5UaW_PmFV6oZvtsJUzyt7zO55O_lGEHyR1T2p5f29rrea8RHCNmWgjurt40PPR5Yz4esXDHh6EiTknFQMuIM_iDpj_eSnzcNB9dtb8gSQX3gwOuo_kR96esGqULNzmhZIABXVQQlDNDB_TxLrs4BP9me2Mp3WRHkU6TZW784kHEKl3oKBckwvzf32BCkhr9vMr6ylL-3NHsI5K0LycHTUqcQ9M_BjQ0ZxifTEkDxsrsNHKKCA7sefHaEjjxBuVqBuP-_duZqYBzoOa3R-rO7H7axGyBI011qQh9NjbedycgfCoG3L2Uohbwj3ex44QgT1krB356Zih9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرار گرفتن یک کشتی نفت کش در نزدیکی بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20150" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:
امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد
روز تسویه حساب اقتصادی ایران نزدیک است
هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.
جایگزین برای کشورهایی که سرنوشت خود را به تهران گره می‌زنند، بسته شدن هرگونه مسیری به سوی رفاه پایدار است.
هر کشوری که به عنوان شریان مالی برای یک نظام رو به زوال عمل کند، باید انتظار داشته باشد که انزوا را با آن تقسیم کند.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20149" target="_blank">📅 10:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:  از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20148" target="_blank">📅 01:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUBn_ff7I0S1npfnrx6ZptXqmHrfbEsZrPDejBBTJuzx-OEgQkbokOAyyGiGYuxPfJ0rrHFg62HgWyBQNmQqZUryYaq2xNEUd4Q5XCLvXjQdvcqMkb03R5EZeew-Ee-umF-WirP8VSAXGhcfFPbT4ti6MtxOPNac67XCURZHbb_tQIwUtdLjw92fNbYC9YJvR02fLYElmbUwS41BlV9h6BfjzoPvGcVYgtdbDVbp_UKip_f4DVXfOD4ZrRb8nvZGA9Tjsdspjg7NJO1vIaYmnfmBRyP59BOR2Is2UCiqYlc5i_VBQvXfc1b5rbhixLky1mcPLV0KIhjp_F1a3p3YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مرندی:
در روزهای آینده، درگیری نظامی به احتمال زیاد دوباره شعله‌ور خواهد شد.
با هر رژیمی که با ترامپ برای گرسنگی دادن به شهروندان ایرانی همکاری کرده باشد، به شدت برخورد خواهد شد. اقتصاد جهانی در آستانه سقوط است.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/20147" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=DZ9wRC50Cc19KkbuomDEb-JoGsffQE5Sv2qmye3SaibXejirDpzzW5A3dmVo1Yj6I5T6N8-tBOHu0HrkoJr6R3AEjYfkohFTuv6dTF1DyfskB_rDsOTybeNuquvUH4OCY98IAsLVHXVqy543nOKqb-jwjkTLRkxQz9CYjuxl120HzEVCORcHQnMQ54iJmNxIaTuYOK4WyC4mIc9aavw0qCXvAYLqTncIxunIO682ZPVod7TDwAK3Wgo0YRjmeDOu0sYn7fUeN7ivI8NC4VWSXP7upjTCkGTkjgVk1NBTpLQ6c22e_th8SWcSVpO5utsskAtHmKyO9bCiQzVLBdX9tIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=DZ9wRC50Cc19KkbuomDEb-JoGsffQE5Sv2qmye3SaibXejirDpzzW5A3dmVo1Yj6I5T6N8-tBOHu0HrkoJr6R3AEjYfkohFTuv6dTF1DyfskB_rDsOTybeNuquvUH4OCY98IAsLVHXVqy543nOKqb-jwjkTLRkxQz9CYjuxl120HzEVCORcHQnMQ54iJmNxIaTuYOK4WyC4mIc9aavw0qCXvAYLqTncIxunIO682ZPVod7TDwAK3Wgo0YRjmeDOu0sYn7fUeN7ivI8NC4VWSXP7upjTCkGTkjgVk1NBTpLQ6c22e_th8SWcSVpO5utsskAtHmKyO9bCiQzVLBdX9tIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو:   این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20146" target="_blank">📅 21:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر نیرو:
این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20145" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20144" target="_blank">📅 19:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20143" target="_blank">📅 17:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vezk6liTANE56bjuIGNFz5jFs6zj2eaqSDBQ2xnTzMuVOm8JUJ05JgVivt-XaZqDevf5kTnmklwvv2wdWpIMO5LJXyxVBAxkNp_pOppXkI36zVGdWnxiauheXazNZ0BzgGU_oHqLS5P_9rx0NuRm9jXpgREzVL-bgNtOY4flAn34NUHu2V44D1bLSGiqN2L78J5MUNB_CAFIig6Yy56kFSECAA36YhkE_YmFssrvvQJq8o3TX-UgJ6Nij8S5QZWJHtkVtwayjQG-02oaQWkJVrAI88SsQB6tbK-HOikkqXvt5IvfpHuO9I4yvGk1NDpQiB049i75TNQM35WwbDRc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین
پس از آغاز نخستین محاصره بنادر ایران در
۱۳ آوریل
، حمل‌ونقل ریلی کالا از
شی‌آن چین به تهران
افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر
سه تا چهار روز
رسیده است.
این مسیر ریلی پیش از آغاز بحران نیز فعال بود.
نخستین قطار باری مستقیم از شی‌آن در
۲۵ مه ۲۰۲۵
در بندر خشک
آپِرین (Aprin)
در نزدیکی تهران تخلیه بار کرد. بنابراین، مسیر مذکور پیش از اعمال فشارهای دریایی ایجاد شده بود.
مسیر قطار از
قزاقستان و ترکمنستان
عبور می‌کند و سپس وارد ایران می‌شود و به آپرین می‌رسد. در این مرکز، محموله‌ها ترخیص شده و برای توزیع در سراسر کشور ارسال می‌شوند. حمل بار از این مسیر ریلی حدود
۱۳ تا ۱۶ روز
زمان می‌برد، در حالی که حمل دریایی در شرایط عادی حدود
۳۰ تا ۴۵ روز
طول می‌کشد.
افزایش تقاضا برای این مسیر هزینه حمل را نیز بالا برده است. قیمت حمل یک کانتینر ۴۰ فوتی در ماه مه به حدود
۷ هزار دلار
رسید که تقریباً ۴۰ درصد بیشتر از سطح معمول بود.
هر قطار حدود
۵۰ کانتینر
حمل می‌کند. محموله‌ها عمدتاً شامل قطعات خودرو، ژنراتورها، تجهیزات الکترونیکی و سایر کالاهای صنعتی و مصرفی هستند. قطارهای برگشتی که با ظرفیت پایین حرکت می‌کنند نیز هزینه حمل در مسیر غرب را افزایش می‌دهند.
بااین‌حال، ظرفیت ریلی قابل مقایسه با تجارت دریایی نیست. یک کشتی کانتینری بزرگ می‌تواند هزاران کانتینر حمل کند و انتقال نفت خام یا سایر محموله‌های فله‌ای در مسافت حدود
۱۰٬۴۰۰ کیلومتر
از طریق راه‌آهن از نظر اقتصادی مقرون‌به‌صرفه نیست.
در نتیجه، این کریدور ریلی نمی‌تواند تجارت نفت ایران پیش از محاصره را احیا کند یا جایگزین دسترسی آزاد به بنادر شود.
پس از آنکه آمریکا نخستین محاصره را در
۱۸ ژوئن
لغو کرد، این محاصره در
۱۴ ژوئیه
دوباره برقرار شد و اهمیت مسیر ریلی به‌عنوان یک کانال جایگزین افزایش یافت.
ایران همچنین از مسیرهای زمینی و ریلی دیگری استفاده می‌کند. خطوط ریلی در شمال به سمت
روسیه
امتداد دارند و گذرگاه‌های زمینی در شرق نیز امکان ارتباط با
پاکستان
را فراهم می‌کنند.
هیچ‌یک از این مسیرها از نظر حجم قابل مقایسه با حمل‌ونقل دریایی از طریق خلیج فارس نیستند، اما امکان انتقال بخشی از کالاهای مورد نیاز ایران از طریق مسیرهای زمینی و ریلی را فراهم می‌کنند
.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20142" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20141">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">برخی اخبار تاییدنشده خبر از سفر عاصم منیر به تهران می دهند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20141" target="_blank">📅 16:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20137">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">انسان‌ها_بحث_درباره_خودآگاهی_هوش_مصنوعی_را_برعکس_در_نظر_می‌گیرند.pdf</div>
  <div class="tg-doc-extra">328.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/20137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک بحثی که وجود دارد اینکه یک مدل «رایانش قهری زیستی» هم مدنظر ممکن است قرار بگیرد. (Forceful Biological Computing) که در آن مغز یک انسان بدون رضایت خودش از طریق کاشت ابزارهای خاصی (نانورباتها یا ....) در اختیار یک شرکت پردازشگر هوش مصنوعی قرار بگیرد.  در…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20137" target="_blank">📅 15:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20136">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترکیه، فاکستان، عربستان، ایران، بنگلادش!  به نظرم اسمش را پیمان «جده» بگذارند بهتر است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20136" target="_blank">📅 15:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20135">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:   از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20135" target="_blank">📅 14:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20134">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:
از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20134" target="_blank">📅 14:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20132">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6Z231HUSa5V7P0b57KUaw93PBXDtGCWwU-N5OF8Okckye65_TZ5ageRqWoFktu3O4GHC74g0CjgFUr--a2IEFoixq9diYcZ2GNM5mAaPQlsZR9A-uNFBul6JuBq1AxLFePybeb36CYKVlwYHUKeYFBmzg6GDyd3iyTj2agQiFcmOjyeBbRoV_3THUdbwriha551Ci33a3d0ifhsGzvR0-NMaOz6LLQHPd--xR1a7zcqGw2m-kYru_rmMrVfzD4fxK2Wp7_zZZYyiEIv7_WmxO6LRvF1ewxLIN279aldqcFBkDE9DjZAaELPl_nzjeCQ9711WESbPrvJcit_wgCxhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=ur19B98ibdZ7dwIOfHXGWhS-BWC9aBEXllnWk898Y-dtsv_QUVC5MeudPGuK6XEXPCC_8v1W6lx2iBWkNjnKU0GrEOiVWGae693UkNARGIkVq0Ucof9EA917cmTZcCU2bfpEtRnhJ6WWTCAsJPqo8Q88lZ2aQm7gdAPmwx1JKDmjmvNejIlNce7ff7UQn965xmWCJoZevW144S0mU-nrah9h_eRXNUC32WvhZFvvSwSSDvSeI_vh-NnoOHdm7wSdK10FNtMDrzGlACwV00WP5Wv9pvxfJhZYBGUdqrOVSDU5oj971z8rGO4-bSnlHrP2UdIOxXyff8HJwXv2iWpZcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=ur19B98ibdZ7dwIOfHXGWhS-BWC9aBEXllnWk898Y-dtsv_QUVC5MeudPGuK6XEXPCC_8v1W6lx2iBWkNjnKU0GrEOiVWGae693UkNARGIkVq0Ucof9EA917cmTZcCU2bfpEtRnhJ6WWTCAsJPqo8Q88lZ2aQm7gdAPmwx1JKDmjmvNejIlNce7ff7UQn965xmWCJoZevW144S0mU-nrah9h_eRXNUC32WvhZFvvSwSSDvSeI_vh-NnoOHdm7wSdK10FNtMDrzGlACwV00WP5Wv9pvxfJhZYBGUdqrOVSDU5oj971z8rGO4-bSnlHrP2UdIOxXyff8HJwXv2iWpZcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاریکاتور اکونومیست با عنوان «کمبود رهگیرها» تصویری طنزآمیز اما هشداردهنده از یکی از مهم‌ترین آسیب‌پذیری‌های جنگ‌های مدرن ارائه می‌کند یعنی محدود بودن ذخایر موشک‌های پدافندی در برابر حجم بالای حملات موشکی و پهپادی.
در تصویر، سربازانی که ظاهراً نماینده آمریکاییها و متحدانشان هستند، در حالی که تعداد زیادی تیر دشمن ایرانی در سپرهایشان فرو رفته، زیر بارانی از تیرهای دیگر گرفتار شده‌اند.
دیالوگ بالای تصویر نیز به‌صراحت می‌گوید که جهان به رهگیرهای بیشتری نیاز دارد، اما بخش بزرگی از ذخایر موجود برای دفاع از آسمان خاورمیانه مصرف شده است.
نکته جالب‌تر، شباهت بسیار آشکار ترکیب‌بندی تصویر به صحنه معروف فیلم
300
است؛ جایی که سربازان اسپارتی در برابر سپاه عظیم ایران هخامنشی، زیر باران تیرهای پرشمار، سپرهای خود را بالا می‌برند. این ارجاع تاریخی، پیام کاریکاتور را تقویت می‌کند: مدافعان امروزی نیز با وجود فناوری پیشرفته، در برابر «اشباع» شدن سامانه‌های دفاعی با همان مسئله‌ای روبه‌رو هستند که سربازان اسپارتی به‌صورت نمادین با آن مواجه بودند.
طنز پایانی تصویر نیز تلخ است: سرباز سمت راست می‌گوید «امیدوارم دیگر چنین اشتباهی نکنیم»؛ اشاره‌ای به این واقعیت که مصرف سریع رهگیرها می‌تواند در جنگی طولانی، خود به یک بحران راهبردی تبدیل شود.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20132" target="_blank">📅 08:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20131">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خب دیگر بس است بخوابیم.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20131" target="_blank">📅 01:30 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
