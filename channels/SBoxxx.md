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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 21:39:48</div>
<hr>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQLx8iSxwDe-pxoXIKF0oohRRPcakYlkuYPLDNrttmdlJRcJP6IjsRGNbIKcLoJY6tY5NsmU17i60RhH4h8tHd-LspdPCcdhCUezH-JzKLFT51sNh1TjdjCT5w8D542fl-y1PysUOVvU0kXfAv97J9V55D-IPBQf4m6G4M7JLJik8KWrrRLEhQUtyLWlbup4_OYvwXTXAE_tsbqhHODzElOmO50U9-UBCcVi-eZ4hpHh0uS2n4_wCcA7eSvj1mrM8qqddsEIY5XU6M6NZ-PHC82yraYKelx0PB0010lMJqvwjp-kVoqCJihADkojC2Cdhnmvd2KvTUFCtc9MSJoo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uFZ4lmT5waVr_cYAdntloTldDAlUKpxV5Bu9qUN1wWmApC63OCySX-iFuAgQ9jOVar50pa49vXA1QwxeYnsDVGoBEjtobybGVAZuDBt2uO1TVd1L7NB94N-e0P9yGPW1R2ng-wTjbe3ClqMNgMzAMY7owl48u2NigVLFlprTEH79Y0ckxeBpcC69_GtIlDBDpT11QuKHJ5ZvYvathBipgObYNTG0nCh8YQXJL6wPfT9qLDPKZNR0lxPwq7zrADAAmCAD31G4tXrtrEUkOI7-vwIIsedabsfHcR0cqXy-foq1mLqtvvvB0GpjJYsTMzpNTDAvxQ1a6rOZmuMBSsAzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uFZ4lmT5waVr_cYAdntloTldDAlUKpxV5Bu9qUN1wWmApC63OCySX-iFuAgQ9jOVar50pa49vXA1QwxeYnsDVGoBEjtobybGVAZuDBt2uO1TVd1L7NB94N-e0P9yGPW1R2ng-wTjbe3ClqMNgMzAMY7owl48u2NigVLFlprTEH79Y0ckxeBpcC69_GtIlDBDpT11QuKHJ5ZvYvathBipgObYNTG0nCh8YQXJL6wPfT9qLDPKZNR0lxPwq7zrADAAmCAD31G4tXrtrEUkOI7-vwIIsedabsfHcR0cqXy-foq1mLqtvvvB0GpjJYsTMzpNTDAvxQ1a6rOZmuMBSsAzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S83jB46GDI0Fo9gsuFkDF7sgMTBBfxrbMJSsM_VK9Kg9cQIs-Eq8XBKjtr-uXxoxi6Xq1JcBQnwKTG7QsoZ2klT-XYZDKm641CayvVeUaOlj65uyLZNFoH25DDrdvFAQK9U5_5llYtM3knyrd75qaQtb7GY1SCTUJgELYOsLAGFz7DD_hMQOfvPUw1Uu1dYzerUN3LRtigbgeI0bStzOAs-5qFoKLJhGDGk5Uj0GKytYbdxrxkAzN8wPsc3qh20CJymVh-6ZNT6nM80urO7vS2rVGeEcu2iP3H7reJYR0wW3cfUAJ2Fmgk2kxIC0-B5QqCVR5XW9ObJErWkfRKnjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qwy4MwPBj0CV0ArKtWoDVrqjrE04A_VZ8dVZO-VD-ZW2lFKTu6cjJJl9He-wcXezfWQmul37ITr5KUeyxEcHaFsFXEWwKPWeX257koIFpMhYK7U8cb_oBN_h5AB-3rIt6H4YzSODJVrHQg-80xnFBB8umW4k_kGFuitM4fhi-YVrg91H4Nx9gtzJnwP_mvUuJCNi_aHGUZ32mtS5lbUkYElQL6kYIRDd6n03dMVN85DFwU8atzLfKWVsMf5F5yHRkNROAQ9EEXfskRsYnVMnDb2Ne4fchTac9BjUoA32c7UPhkt-gUczz4Rc-yrjEL5rMxZBU9Zqkoo3z5u4cq61gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNS8Gsot92uRlwDDEmaaC-aBITySaIgoI18JowbZIIns49XomhBye2iYoxdRmfJOkWw871twQHWJ--s9QS_BkxKNi9jeTa3Ys8vmaF1IrPehlF0AZUSF_EFMED38W3WU4qx60dJsKicCZzdFSSOe79pb-UeZzZgKGH9Ve4dlb_FrbVqiQoJJK5pdwn-V7JgGZI52lN4RUesp_pVKCvq74tmifDzg2T5FInT982nJjr5nEWEKcnTeYIR_P_P5ZmleUbEHBCRGScg3uSMA_O5AFEadYfcPEJcYkMFmPuRFOYy6Y3i6VRx6eitZLLooMYEj1LuHWTF7nYWMSkGQgIoVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhfACF52uauy_6kl2UAp3gbPVGqz3xiPKLnEwpV5wFf9gR9Zk9LMlRk64j4Y0GxLiaYp7KwCSdzxG8KplPeSi4ZSexAcXLDopBC9ZpQcTsIyDqdNffYlGsXIg9xbvnAWntWxvyKPgLmZAbS_yf4p8Rf2Lv9-RY64bXCiRUJ4phA_CjZrv_aftejYkMUFIbkUHgU62GJccrYKF3JinNIc7ABYfsFlAuu6wlaxpJRcfVU0HKjz6J79rysqQSKJ9SQBkQ3o3zabcUq14r5yQV8S8C1fMmby6gk2cZ5mgmw_7wiHEtJZoNfYLBMlsmZkPzAHo_LJle6jg5bPa8e8S0p3KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fperqOWlMGj9CiCNFqCHpAKcOi3D0xt5RuXnuO_lzyZ0o9lbQhLVg2l5mUwkA2JMUrigDBZ_9R0o7BUWQt2-p9lAL2yvWVCpdvlWLw1TGWGlFabpkfIvK6U_SVNgU_HExuTcLDQY8PpOvV-RuT8zV792GtgvJb06AdUlcZKY2HQZVz9-uXNFfr7XoWwSuvKzPf3u2ZYd8XOoFsfoRZtZ7xMPAM8_mpt0SiALV5fMtVX4rczQ1Uqx-6ILSvAK6Iv_Gph7jMYQL9ooQzKzpQ_kh7ZZ-j-GPH5moErI0EZM8r93T-lO3lmvI8QERQkIBHQIO36Yt1044pS3BiXADbakmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5WHSpRJgOYXflWfq1Td7gJsuCiuuqSBXWq3myQn2kY-h-eNDvJYmrAGdSofx77Gx6aJQjanOS6mPZHX7yF_ekig8bGVejf-0Zq0qIWORnejBPBnoQ8847AFsOH4VZ09DysXIlsm5UDz6aAhed4Wc8TUCeK7rHViKf45ffSJ1NBPaDNlrq6fG-tkJE-CRc6jtPTgbhZVzTFrt30HXwha-ioBh0ZfYQlURY5T6tyx0qWWr3Ihue47Nt-TS-tjiogeZ_64yFkEOaU0bmuyuIoY4tp6_LNgJ1dM4lU0WzZ9gR5INFd58TUK_CoXs-n0glWW4V2k9RmUYtECd_zKz5P1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=eQB95hxstEGBmKT6j0vIa16aob2T2-kUMi8785jp2uzc4RksN_w4m_e59azgmsahzLkXlqVYOte7-Xvzade2NeNHHZ0trBk3dBk5VK7l8hLNb7kIO8ds0YnL3IBEvJNvKU5BPbYzYEuyzHqMH-uXm0LtqAf09GCVzn5p-N0mYt9Cdnv6S35iIBOmelK2zsba35sch1xuiqOYcEfWxFY9IGUup_06PRJ-D2gQorUygCxh0H7dz2prYhq8mnFsxAjrXttE5Ax_B7UunBX_yJ2RXdsVhXKRU9QZ9loriZKUOgVEY1_z1StCFlv7QT25DoB_VcKQCsFU1DmNildG6hHa-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=eQB95hxstEGBmKT6j0vIa16aob2T2-kUMi8785jp2uzc4RksN_w4m_e59azgmsahzLkXlqVYOte7-Xvzade2NeNHHZ0trBk3dBk5VK7l8hLNb7kIO8ds0YnL3IBEvJNvKU5BPbYzYEuyzHqMH-uXm0LtqAf09GCVzn5p-N0mYt9Cdnv6S35iIBOmelK2zsba35sch1xuiqOYcEfWxFY9IGUup_06PRJ-D2gQorUygCxh0H7dz2prYhq8mnFsxAjrXttE5Ax_B7UunBX_yJ2RXdsVhXKRU9QZ9loriZKUOgVEY1_z1StCFlv7QT25DoB_VcKQCsFU1DmNildG6hHa-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=SV9JJJlrSTShUES930CJ27lTtU2gZTXkkX8w3bRQgYsTisUikOQ_a6LFiC20q57RLopPw_8e9-53rlqAn7vVkg1wmWpsSQUZiCIBtlRdfkpXyrDS3iyqgyUVeq8vSlR4NMre3OuveJo_Yu2J0FGoGpQmkZ1EXmX5Z05BLsDNwFj1qaCHsUdfb6P6tqEQZSHcrgNk3FE7PJPlK3nE3AXEHwIvL7tufl1Zr4-nvECu-KOzNZMa2n60wyYggcbr-H0widhaPU6KnJ9GP4RIzLWYS3wyhhj5TbBLWFiSxVnLeRuHxTZNd5Ct5FTQY-lMgYt5p-CqJXEzYpkPEFG6DFWXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=SV9JJJlrSTShUES930CJ27lTtU2gZTXkkX8w3bRQgYsTisUikOQ_a6LFiC20q57RLopPw_8e9-53rlqAn7vVkg1wmWpsSQUZiCIBtlRdfkpXyrDS3iyqgyUVeq8vSlR4NMre3OuveJo_Yu2J0FGoGpQmkZ1EXmX5Z05BLsDNwFj1qaCHsUdfb6P6tqEQZSHcrgNk3FE7PJPlK3nE3AXEHwIvL7tufl1Zr4-nvECu-KOzNZMa2n60wyYggcbr-H0widhaPU6KnJ9GP4RIzLWYS3wyhhj5TbBLWFiSxVnLeRuHxTZNd5Ct5FTQY-lMgYt5p-CqJXEzYpkPEFG6DFWXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw2scvlgZS0sDNibtLC-vceRgQ2zQFfKnwFdR6G70BmxFJPkOqoM5mLdxF_NVJ8CT93Ik1t4TdnjSPNud3UNbWnBE7hPg0ACGsr3Z0vBJCSFZhFeuzY1J45olqmkK3zJ8Vi4O8k4JcNp45thWUzo2d9HDtmkHsWCTxK59EUYrvkQ4p0eRrLvGAkiSrhmi5yGXjFhZqFvEAV66jcjnI74G_B_Umuh95dJYkPgQMCy7nbFoqeVCf5tfa68RHovxTKzZz-Z6Zz4pjxmJQ7Nj0GnQbuRUn77HZ-xNRIPDpesCoBkGh5hC79mE7-RqCgMDO_o9J1p3SLOUKjz-2Kyj4Kl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqIO7njdBD-LTa-Na9sY4dBW3gGcAvVHaHvBxp1oKLT-XxRBG1mmfgs1k5sa_R6H4Fb7mbexiD54pUH_JkDVGkCjtpRucDW9liJlf8A6lNfLFv5pq3HL1vfQTrlndTq_znqzC6lmrmp1NUiPTjJbDt_ISSRm-pn1oCUXK7PsOKTupfZ3PZQTbB2u6LJ5-RXOm6fLmEIp4-HIT6zbKVgNGYwqaCJLiQsrfsZkW4vl9rplM1fn8QPCwAsTO8NurA9sN80mbjBVl6ll--gpery3IxI3cq2Rve4I1Wk1OSGBDVZQbjw8FuSUuASAU7iXWQjw7YcxWHHvEQ2UDnFGaM8B8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kodH93_-kXoqzJaZzC5G1PlCDfpvBihzieYz8XERtWUJNKxRGZVXPSWTlUJtce_fkLtVZQUqi1PE4dy3fjExMFPZwK2IMa_A7_ZPNQwdzl_VbBE1yKH3OCnfpFnlnzjN_5qhbefS2kyeSadBDXF9-LgSg-IQeFXJbE2DABBf6sW7hwYiNQEWNbcjOZHoCd7IFWpzx2hyqtCAIhmspTF7xfOMV4Fc_gxG6xqoGSXEoXw2gN7j0cIDEsAJefobe2QWFvjubYcB81745_Q_Dri3W8c1LEArMApMqXmfKk_arunZdQlAxVBcYW0F_Ddu37RB4Df7o5lW4MVI3Ic0ahpwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzA6HZ5kwlBmKf8zOXtANbt07rnmbam4x0p0KExRtH63EZhfy9xLAaRb4z01hjV3mUSa0NVKHrrp3epam79crKpS0atxOVZu4S6z4Ax-KUdejjmwERWhWr7PQK7owGz1Y0AkXAPjiTnQSEe9zhuxP24Pq1keW91ERUceRsqXuOVTy9MZoZK6ZWa9en9785mSbsxSXGh9aUOrcC4skebkXZSGKw9UUv-mEiPWHjoVaskiAQxuMKU034AYiKUOhmUHp50itjeoV-cHEEDzCNa1ZFeeWi1qoSN3wdIgWJpmQCFThDhsCECfj8S4pLacmA6g3rF4HGQgDo9Zyw-vg-1uMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPWnnVQajRRo4pFAPNNSbl7G18u66d_7ReC1SHtsfstuXUxviLzFAa0MPMrGKfPRb7ZIyuieknu5LoqLvSxhFNJAv7NtnaMSrqmjPOo-Ku1MoTsaTok62s73OtoRjcUfH6yXsrLgyeWL5C1FjaiRzZ9XtUn2PfmEuSLVACiGFiHaEq5Hj8swgNo6-8PsRPkxSWPCX6UtV3NDiPLDZeL0Zc6_iKnPevUB5mF2i1SBTz5Cu7nLYgkJlRsomCKZ87u2U0XdnUkriRFPi80ODLpfng7OpqZxJCRfyW6FUP6iuC4TKrQ53mpFAPDZAbEej5uJRWMZeSqe9Y0CeWS6m5654Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPIbad0t2YNKRC88tJOfk5aI6A3Kk7f7JJMyLaALa0lnYeqZNbCBmU5Qhv1Abb7rj0Vs0QLazaJftHyHjZrxP7Y2Bd4vYKVKB2cQJ4wvydNLu1RV-Rll03iDupkR0JKN5vjlkmUv415yGfW9wOecYO0ORyZsOWiAacSg2hia2MMMYXAdTULNT0azAg5WgbSSWox9pDjWihopsNo-HRfXW8QEUN8X6FTyNyV_GBDUDXnaDry4HC8IBwzlS4tBe-2dnJOQstBYmyyCq5w4EfVmYUCg4a1utYlJayC9MfECEjAUorCH2WCMZ7rg3faNcpcEVX9SbTVd0PjaQYKOn6vTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X09gWzstQHE13HJeJT7K_UFfEL5G-aWtiKYOisRATXo47GuV8x7jQTJ5ULe7T1OC09OMYgbhr34WmWFhQCaF-yrlXVbYBPovIrKGQTSx9XbN5xzJK3Xtiz3O3bQ1TkltFdkxFP24_YS2vXq0f5srAE81S9Np3axLtzvVvJ_UqaGHudXUY-ePvvdIVyo4-jMo_Q5Fbq_FDvYNtmzfZIkH7xkUkwxuA3dHIa7EJnZPbWVhnaVYAwY5-xCZnGwCZMvWvG2pZnXzcfIOT7AlsXI2kRtdNy56g1D5JNXQAsi1sz9RYX3St6sKc-LqLOvQac3VDRzksrmqLf2UFbm1hD_8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXXqnko3m9u1tbvKWIQR7KJ326gEPIYerMWCupSGl_wl9D1Dbkj8QMRxHcZXBEt6kc1iaoqc1S_xfIKhuugnV0qjrdqlwS-BSj0xRSwznCAY17qSE1MF84ulW8Ol5NZDuevvZGkuJIosNGL2NjY0dby36qHkLb21mkBJXB4bhWK3Nlh8BLL8GfCiZg8c9lcg1PvHtl8DXMcVqsR_BFZq8J8TlfTHk-739dAMp_ibutS3KK74f2gJI3QrD1_AIMHgSTqSo454oYi8xi8zkdFdl31zjSXAVQxiNjp3lMievoLg906HI6w0SqTaZTJWYw6pPkNe5HevpjGIq0gCLhVK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckCjWNi5iGSV94JcjLJoOwy6awkdYgXPGDikj-35FaSikV96YIyGgUZfUl6knk3KZxnLREXkpU_Wo9hRX_vveIKq1K_aXwCn_0MS2M-XGgNhUNzeVPZKNkTmFpdxqqS3u-H4ECxPQ3OkAnDL24Cj84r3QUWVrkUy5nCmk3FTVymgrGp9q5NLBgdj8RUUuy-sSzURUYF9D9AhbMrtkx9TtzJwDl3DDck51RA67ayAf03u9eAJBXhqCs6G9A90aK3DCYysHwrNX4tJbU0sgEnPeo-VhkM3mdZ2bzA_we9vygNi4ctZMaOUAEpAi0TqWyXKC74-9olRY4TSFgQq_pU8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_omj6JmL72iOwsTPS_OmMmCJdER4E9bcgovGM4fntmD98p6Lr0EuA9OKsRdKRamotVVnyRiAgkIstQ9VLtp26u5FxB5M4cSxekFpT_9wDsl3F_c873hxR6MmH5kEr36eB0BWg1cIuMq6STQv5bMfG4kOgWQoDBlWO6_jympKSVQapP1TDZn1Ekhgn7MJYEBex5X-VNPtS8n0t0vZiBpFFVs-UL9SNgutIyn7O-gQBOCSwMvAZpF4VKckLoR6xwlnad-mC72433oGU4pzkh_PtaXIVzA9fktYHlgekjhblep79V9BIE0WIA4gakg4hqKmlBkVZbUPNZEqSk6WrHcyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK6ZE4FEeMkcbxDk4RwikBWpYfI0qxCQWWeXoVKlCxM9biSuL2UBaYH6E5PtqdF7G-hzI9kHuRsI5pqfojdcePYzZ3yRQLYd_9Qt3oC5xIQ9SG6-rpQduYn3JQIU7YKl1Sk49k-M2RArHne96uGBoLFrfZUfWp8UbV3SuIQ9QBT-u6z9FEfsSiuC0-EbwdkzNVGRjXFi02fXH046jmhxajU-xWlujihjcJM60Ybsq0J46ON2r9q1-xJgzmFBhYvZDF0iUQAZXmWF3-wo_BEFynQ-6Kn4qIevHYPBOphNUFJA6Da5sJhX7koH-w_2erQwfZs8rg06Qk0AyOPws0v_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/benlTJIG7UdAqF_ygVktlP48oU3UNkkjxlduyLfcInah7-OIm9woWrEL3SzctcOLuuymUQOJN0ja44nJSOhnbP73OXCF5b4iTQp9TaOmLUoQx3EusZdzldEAAXjofvCp4uNaN6cn0Rtv7IpUh2d2bD341Kz89zF2GPbbILOEQqveryafzFgOaharwfRfRUFuwmaQaQKG95vT51OEJqag2JO0CuMHDAvsbzsJygrbQ0eTvQrvNYUfNyJwl-vepXrpCP_-wl-pUuB9wvh-gNOgW6UAmysEqmqmLEKajqmB8ZeveNGGhds9BQoWWXSMQa4fTR83ffhMsFixsK7rZslGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.  دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.   ولی با این حال، پیش…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20185" target="_blank">📅 03:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فرمانده انتظامی کل کشور در ساری:  جنگ سوم هنوز تمام نشده لذا باید با آمادگی کامل در برابر دشمن، غافگیر نشویم، چرا که خیلی از غافلگیری‌ها نتیجه غفلت بوده و دشمن از ما دست برنداشته و جایی از ما دست بر می دارد که ما دست برتر داشته باشیم.   دشمن به‌دنبال ایجاد…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20184" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20183" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=UVrGqaZoHZfmRhioorNJuWhJ2mb5rcckV2kvmH9j-f88mj2ao7705T1d8ERkN1rqM_5wRjJCzHoH3LGktVEIgi_DJRBUGzBW3SwkE8acPI6Qv4J0OLmJ87ZiCC-kErVDD2uTIpqSLrlR2MBa_uZ2bsZXlz7lltt_97KHJYg_CF_gytqYI0DAeBToU_khYI01jT_SAUaTZCh_FH4exD565Jzx7oWA0nVNTu47_fX4K7hAl3zU9ovuFCDPNEXUakHBsQG70CQEg-aQDkN1cxlhuLWuLcQ8GW0XaxS1FePknHrLosWyDNEjApV46cMVxyijON5XGc-mvPWr4-TizQ6koA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=UVrGqaZoHZfmRhioorNJuWhJ2mb5rcckV2kvmH9j-f88mj2ao7705T1d8ERkN1rqM_5wRjJCzHoH3LGktVEIgi_DJRBUGzBW3SwkE8acPI6Qv4J0OLmJ87ZiCC-kErVDD2uTIpqSLrlR2MBa_uZ2bsZXlz7lltt_97KHJYg_CF_gytqYI0DAeBToU_khYI01jT_SAUaTZCh_FH4exD565Jzx7oWA0nVNTu47_fX4K7hAl3zU9ovuFCDPNEXUakHBsQG70CQEg-aQDkN1cxlhuLWuLcQ8GW0XaxS1FePknHrLosWyDNEjApV46cMVxyijON5XGc-mvPWr4-TizQ6koA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20182" target="_blank">📅 01:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کری خوانی وزیر خزانه داری آمریکا برای عبدالناصر همتی:   به زودی دلار 300 هزار تومانی تحویلت می دهم</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20181" target="_blank">📅 01:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irYIm7fSw7s5GHys_Efqz7DtYota-lWYPAKXEHvdSUJc8ZqwxcixBUtfRAO6_Q1BCYKjBkbFg6a4nY_nUd0SH9LIiKmbxfTwWjScoU9VSkCnuNbevkRop7c2x_L6fvbmL1qy0JqupEzhjd-QQeZZYhIUjQ8TEpY8O297_2vS23qLFWOy2E0hmZjaeAV4YUbTygBQZr3ElPJlOpYbfapmkGa7VGEhHKfrwGpxYk9DLPyQWXMyLcvmpYu532jppqYIZXtqkerNTp7L_m-66gN6jS9xIcdx0lsDpYDf-H80RM8JZd1RPF0gndSsgb7WM3oHjShkf_iyQy8yrvafR2BaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20180" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20179" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnlRggyTUuJ6wl3kOSlp1xvM_ty5KHrjg9GboMncGtMZx6bR3selVCVulS1zk3by0uJGSuXX3EkcdvAxeN1u9dCEdL4ZgXDN0yAuIoDmrvHALhgQzmwCGDkMw2LSFPPH4i1ljhhTUt_6k-DMoiRbFprjsknP3SjlM0QCgbj67JIpGCNz8Hg_RKvPMGgeQ93wcDhGBpYfLSCZqJ2kOowNgz16HL_5jw6wIM-Vu-E53RU4INfBTNqSKCo5ncSiI3QXguv4OjWVsj1CCz_EabU7Ff-rP8-yIwiHb4VIjreZLeBxSNicL29RgwBDy6U7zYPhGc5yaezi-Ydq2uvU1nbiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/20178" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسرهایم را به قتل برساند
کانال ۱۲ اسرائیل: سانسور نظامی ماه‌ها انتشار جزئیات تلاش ایران برای ترور یکی از پسرهای نتانیاهو را ممنوع کرده بود.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20176" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «خطاب به سربازان عادی حامی این رژیم: همچنان که حقوق‌هایتان بیشتر و بیشتر قطع می‌شود یا ظاهراً فقط به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشورتان را برای پیروزی ترک می‌کنند یا برای ویرانی، و به یاد بیاورید…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20175" target="_blank">📅 21:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «ترامپ در حال برقراری تماس‌های تلفنی با رهبران جهان است و درخواست‌های مشخصی برای توقف تعاملات آنها با رژیم ایران دارد.  اکنون زمان آن رسیده است که رهبران جهان بین آمریکا و ایران تصمیم بگیرند.  هر نهادی که از طرف…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20174" target="_blank">📅 21:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20173" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
«امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.
ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه شریان اقتصادی است که این رژیم استبدادی را حفظ می‌کند تا زمانی که تهران به تنهایی بایستد.
از امروز، ما حلقه محاصره را تنگ‌تر کرده و هر منبع درآمد بالقوه‌ای را که سپاه پاسداران و رژیم ایران را تأمین مالی می‌کند، مسدود خواهیم کرد. ما در حال اجرای رویکرد «بدون نشت» هستیم.»</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20172" target="_blank">📅 21:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20171" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7vZBnXKja3Eun2qKU9N_kjXVt1l6hCk6QKu-M_SAeKzMjrhyJIuzXGMuzACO5tFAVyQOpdx-ody1BRQAsU9YGINjuTKVFU9wCqaiBZVIfV8Nc7gb-SHUjsZgqZwi7mBG1VAXyrTDRBZZS_9pujRZAQXMi7WA4d8Zk6D1c_pSM2YInpTAay_0MfAQE-KFlulT2N4PazHkqO9D3Y4v03i7MegVzrdCm3TnVHbFhqwWgObcnpa17znz7VrRhcg7_A6X4YnBA7r9MuSxoEKK-p5Br4HEF-QMJeIJYFxDNFQxEStxo8cM3zrZMwC5sLvwP5sibGw5sDkk-Sd7Ikq6cRYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2.5 ماه پیش میداند که هدف درگیر کردن ترکیه چیست. بزودی یونان هم به اسرائیل خواهدپیوست.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20170" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20169" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20168" target="_blank">📅 18:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=CCRyFftGj2hQJy-1kI_KorG-y81hMBnTbz1ESCLHe43Z9bVhE-bFJfE1Larbg8bydTpsBaEvBaLK0D0jqmClEnmGl5F7FDdBbSQ5iq1ktzoyPeTOssAXT7GpleQr8iuwy8cTZQn4U_E7xyq7aF6OtQCX9c2QbP79V1jYP4JcuKF6mFe8qtcvorCkRc6UGpLhlLxIX14S4l_7078kmK6rpJbkL8JBf1HDFbPRTPrEPxTanrLQfPi58B9y3U1GCTD-gjnFpFTplxH99AF4qqogZ63hr7LlB2Klvo6LPNPnNn5ubvclvj6h8q2yk6YB-QiALXC21nHLC9gJlTCzwZi4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=CCRyFftGj2hQJy-1kI_KorG-y81hMBnTbz1ESCLHe43Z9bVhE-bFJfE1Larbg8bydTpsBaEvBaLK0D0jqmClEnmGl5F7FDdBbSQ5iq1ktzoyPeTOssAXT7GpleQr8iuwy8cTZQn4U_E7xyq7aF6OtQCX9c2QbP79V1jYP4JcuKF6mFe8qtcvorCkRc6UGpLhlLxIX14S4l_7078kmK6rpJbkL8JBf1HDFbPRTPrEPxTanrLQfPi58B9y3U1GCTD-gjnFpFTplxH99AF4qqogZ63hr7LlB2Klvo6LPNPnNn5ubvclvj6h8q2yk6YB-QiALXC21nHLC9gJlTCzwZi4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20167" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJL-ldMSbd6oazRLDlAXCs3Vav0Q23-pFVGQ8CWeTc-r-o5rFdvt2KgyjdLtxQYi6c5ZSi6yyNY6_jFZfl1L6Log35C7fwDNWXcHhVXwyOPLk8a8YtmILqfSN3mmWNXB73mWw3i4Q0LWL9sdildvYabGSmHpYvCa6W6euEURbzO1Mynt5GK_F53g9Lg2yhfgF3-OWoVkfGdM0r2ugU-0InFGzo2v2uATmbTku4gRDD2cJhI57ifwm9mbktnaHhMTsirX5usH6eOVcjCUsDGmrNfI86USnhYLQa0q0wUtEII55-jJW9znmN7ryJY0Om-NMAmOi5KiwbNb_mLmcIVm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20166" target="_blank">📅 16:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزیر سابق دفاع اسرائیل، یوآو گالانت، درباره ترکیه:
باید درک کنید که وقتی ایران تضعیف می‌شود، آن خلأ توسط کسی پر خواهد شد.
نامزد طبیعی، با آرزوهای امپراتوری در خاورمیانه، ترکیه است.
ترکیه یک کشور قوی با میراث امپراتوری است. آن در پل میان آسیا و اروپا قرار دارد.
آن بزرگ‌ترین ارتش ناتو را به جز آمریکایی‌ها دارد، یک صنعت دفاعی بسیار قوی، مردمی سخت‌کوش و در عمل یکی از مناطق اصلی صنعتی اروپا است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20165" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB-Zwn1A1LLN3YI2M011QnOwHUdTXViaFNqOaVzP8dceSaHJyWmx616UxNRRWkYD3M-YJ02A_pEud0ryeIiMTJletPDGr4WGWBKDhFh5CvMWWOS5Yo-ynwhil498kBhdo5ITBonQh5bK67ATeqBmic81ofm1N4b8ZgkuP6sp-3IMMAb9H_JKDzq4bhHUGLkbjMajCr8lV8D_lxv7OkD_XT4tPs0FSD-cMBdh_0i2rV0UzVfNqRdG77AKbacF56svGgxL_FT-46XEO30pdSZ9bZH-LmpwBeqMmmEArTqaIqz46hqUGgSdKAUxNmb0ctVF6Zle7swsgruJE52G9lBqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک PL-15 و تحول در نیروی هوایی مصر  همانطور که در یادداشت پیشین گفتم، محدودیتهای شدید اعمال شده روی تامین موشک های دوربرد هوا به هوا برای مصر از سوی غربی ها، مصر را به خرید جنگنده J-10 CE چینی واداشته که مجهز به موشک دوربرد PL-15 است.  اما این موشک چه ویژگی…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20164" target="_blank">📅 14:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Secret Box
pinned «
این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20163" target="_blank">📅 13:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20162" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dnspTolNUIdI7p4CLDMXRuT3XTQBPZb5-z_C1FWmPVz0pJJYVpaMgCmNcPGLb9VvU3nRabpcVeR8WBlkTEucck9XsIXo6btVYtwAEsR9-h5dw3CiAlchDV3V4rptEqvrwmqvBZRAVQQkRkSLlYVdwluYu2HechOEGRmOAFLQOSr9IxWKRcMkN7gLTzwXEZa3kZv3yN5PW50YlBZQ-S8o-jte0d4G6kZ56lk8KSbTrPalkYGBpqY4QqlKykCkNtoD3LY27u7L9gNNCvqPLpJtbMfwdufhdy2ZamZijVq9Rq7alCHNkY3gpUhggdLOvXEuwTbzJ3he5SLI0eNoeL_H0JU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dnspTolNUIdI7p4CLDMXRuT3XTQBPZb5-z_C1FWmPVz0pJJYVpaMgCmNcPGLb9VvU3nRabpcVeR8WBlkTEucck9XsIXo6btVYtwAEsR9-h5dw3CiAlchDV3V4rptEqvrwmqvBZRAVQQkRkSLlYVdwluYu2HechOEGRmOAFLQOSr9IxWKRcMkN7gLTzwXEZa3kZv3yN5PW50YlBZQ-S8o-jte0d4G6kZ56lk8KSbTrPalkYGBpqY4QqlKykCkNtoD3LY27u7L9gNNCvqPLpJtbMfwdufhdy2ZamZijVq9Rq7alCHNkY3gpUhggdLOvXEuwTbzJ3he5SLI0eNoeL_H0JU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20161" target="_blank">📅 12:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20160" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhWlYxpfD6x7LMn2TlFLSocHu44sCPrUW-xxUfvtQ-_n4FVbRBXGJT3rD1SJVD-2OrnO3wsFVx6wPW3I-RCUiuxz4tx0K3qBk81dS2DjSSCi0XLl1OEshaWJZ_V_z0g3LwWKqKHt9H2hNPP1M1T6Lukn7-uAb94a_ECz2LSpYM2AFQzY63Ir9PEdSasCs2x5b6JJHJnk69R4nG9aYazdwWxrdcpvw8ULljPsH80Gd-KxIVNPjHfAPZ6rV7JGSuBWEzylO9EmTdEs9VPf9gCEBx5GmIBawJLoFqZM7AJl5H1o0CwfF2yXZ1tCTrLkAZJfdq8s2QscZEX0npWVsnCtbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی:
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20159" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=RQ65g2ZAp_LeGoFZeBgtpv9SKCjDOX9JfoJBtV1oiNQtJd6Clw4lQtjd70AQbWcrlNZpdCt6nCCloQiIPIttUlVAtcAcKPWCtpgujL4DfXPoJbk68UzZdMUp6f8-N0mQHOaRdbWr9ZFxV_fiBBgMaKOb-ZeGpaAtwJBS3_2I5qE-8XY2xqXX6GkkylimwMuYAVtGxGRMmYK5PULiA5wA1N1yLjf9ylZp4yiOzYmzFuBRGkcY0IqPR11pN3rLddM_6nmbMOdaMI51ATWjHr-ahGKaCMLDFYDEcnmgGoggBdhMR03A9ODSvc4_DHN8cLQKLiZaefeh-eiTzdiEr8xZ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=RQ65g2ZAp_LeGoFZeBgtpv9SKCjDOX9JfoJBtV1oiNQtJd6Clw4lQtjd70AQbWcrlNZpdCt6nCCloQiIPIttUlVAtcAcKPWCtpgujL4DfXPoJbk68UzZdMUp6f8-N0mQHOaRdbWr9ZFxV_fiBBgMaKOb-ZeGpaAtwJBS3_2I5qE-8XY2xqXX6GkkylimwMuYAVtGxGRMmYK5PULiA5wA1N1yLjf9ylZp4yiOzYmzFuBRGkcY0IqPR11pN3rLddM_6nmbMOdaMI51ATWjHr-ahGKaCMLDFYDEcnmgGoggBdhMR03A9ODSvc4_DHN8cLQKLiZaefeh-eiTzdiEr8xZ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20158" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">درباره اینکه پول خرید واردات چطور پرداخت بشود نیز با توجه به اینکه ایران کشوری با بدهی پایین است، شاید چینی ها به دلیل نقشی که ایران دارد روی فشار بر مالیه و توان نظامی آمریکا وارد می کند، خطوط اعتباری درنظر بگیرند که بعداً (مثلاً بعد از رفتن ترامپ) تسویه بشود.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20157" target="_blank">📅 12:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20156" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:  امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد  روز تسویه حساب اقتصادی ایران نزدیک است  هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.  جایگزین برای کشورهایی که سرنوشت خود را به تهران…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20155" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF8TReCJLrBFQ45-sJS8lPYfFwGZEOg37ub539UjNvx7Ou-on8h2dFT6D5xjTNjHYI4TsjxCBs8Xgcv7m-0pGiDINy2pJK6MGimpcacIUehUVPhOgc9uz0mO2PvfSCFjIrddsPlVZKZkHfHK3N0Ld5E7_l1ZhA_WxmKsR0-jwDnq1MjDWMfxUzGY4-QfOKBFILXOhqzaTwGngOZzKy1e8ZvVN7PAzRSONxHkS4ryMShFScnUIMFbCnd81s3GniLJTbjKQ_MyHvSkbRqhhZ87ziDeQL2MQGE_Mt3lCccrsGl7qw4JhHEQkvhCcKHJrjzgVRXU7EUJpS-d0bygkDSlag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز گزارش داده که صادرات نفت ایران در اوت به حدود
۵۳۴ هزار بشکه در روز
کاهش یافته، در حالی که میانگین سال ۲۰۲۵ حدود
۱.۴ میلیون بشکه در روز
بوده است</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20154" target="_blank">📅 11:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ما بیشتر تیله بازان خوبی هستیم به نظرم.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20153" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فعلاً این یادداشت را بخوانید؛ توضیحاتی درباره برنامه بازخرید اوراق قرضه که هفته پیش اعلام شد و سناریوهای پیش روی طلا ارائه داده ام.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20152" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jnl3lvrTmuMG9L2IYttDQHpqL7Y8uYq3HFEP8BcMsH-rnJqc6uv4uL6nbtl3es4OyaBvswLx7cn7-h1IRabE_R9FudC3A5GmVAZEaPoqAdyKvyzYAnn0uKbWzA5PQeJSGc4th_5p2C0Ti1rGhHeJ0B3SIZTir7AL4_OT9HmvmYORtylWNQ-y13dPerYhEQKlKiUUJOVFpc1Hlm5M85JrYIOKZQ76AXFb3K1qGZkLCSxc77_H4bCGJov7q5jOJ2jyihkuLiYIwNlSLXqnfvBoiJysAUB9RvyA4jnP4lnKarG6zQMDWNL-tn60QTUvTgBIlVoXZDNymBRp5BCPt6rPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.
دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.
ولی با این حال، پیش بینی می شود که شاخص های سهام امروز زیر فشار فروش بالایی بروند و نفت هم احتمال زیاد صعودی باشد.
برای طلا، احتمالاً از مومنتوم صعودی کاسته بشود و اصلاح داشته باشیم اما به یاد داشته باشید که اقدام اخیر خزانه داری زمینه بنیادی طلا را تغییر داده است و از این پس، معیار موفقیت شاخص GRI را روی دارایی های کاملاً ریسکی مانند شاخص های سهام تعریف میکنیم.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20151" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpCa-co5KQvuWW8vS75yC-sNv-5U1cVpZPf2eX5zlOqR9xz1oujCUFdKbQh67pQPtNCQBq-P5j9z8U9jSlPwC_WLAhrWuJMObsyAfticuSMchmC13_MQGu_RRc0J-jev1kh_JNjCjm3imVOqGOsv0YarFYFglAR0O2bQCegIQtz19rRHEXxkHUEfwz4JDN8zrvXTQgQbe86JiCBRNnT6b9GKCm80BRWL3IU_Do_mdo-g7zH8SoQHGYAzUn20pAzj3BVJnSHhWJsgYItgRu6O4ntAantuIOpRgDUQWWEyor8995_puATcnj4P81eM9oihCNt-XTN3wnvr6ocvmsMCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرار گرفتن یک کشتی نفت کش در نزدیکی بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20150" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:
امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد
روز تسویه حساب اقتصادی ایران نزدیک است
هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.
جایگزین برای کشورهایی که سرنوشت خود را به تهران گره می‌زنند، بسته شدن هرگونه مسیری به سوی رفاه پایدار است.
هر کشوری که به عنوان شریان مالی برای یک نظام رو به زوال عمل کند، باید انتظار داشته باشد که انزوا را با آن تقسیم کند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20149" target="_blank">📅 10:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:  از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20148" target="_blank">📅 01:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKkJvoZrzPRFJcKOj7mUTp0KSsXtXFKaY2E_tSL0PBGGWEbfJ-EmYBytUUr0v1OKcnyWfsjkvOb47TYKodZYiKW0t07VjrSAZa1d4uBAqk-VSqeS7RzRn8s-1H6wZxxb_zBaoXrWlqH0q7YJhYGW56g1nLvoKR1hwQqgQbwEJPDiS6IYDocvRuPwVrhXNHgk85bNRj2EMd667GfMSiBG3GoyHRQqgF_LsPvhotcogUDVQsuiWoI2x1zt5B5ui8ZrTJZjGDiOsBctXH9gGWc9Pl1pfZeSjISj0yiM10U5JEdtbwmZBtkvAJrBxirppwYjrTu9lNOjbGGygPCS896a0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مرندی:
در روزهای آینده، درگیری نظامی به احتمال زیاد دوباره شعله‌ور خواهد شد.
با هر رژیمی که با ترامپ برای گرسنگی دادن به شهروندان ایرانی همکاری کرده باشد، به شدت برخورد خواهد شد. اقتصاد جهانی در آستانه سقوط است.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/20147" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=emOkVtsnGja40ciARUxjziltjRbceV-RdxpoWJYoSu30hXyiIBtZEwmIFiZlGLTzD158RK0mx-RpJe46wswUtlVFE95NlmYl6moaOM2VfXZDpa3rB-KrMgGiylIBOGp2rrJSzDjpcTXVNPuhDQoqypQqGEpDUFGE6u_Ci-LOffOAstSSsq6go1rUtUZldQDeJQmdUpsqx4Rw251k7EYKUKxHpIirnUFA69YL4-nbfCaG761tB2rQs0OGXsqjnhAVL5T6Exuv9lwoHJ4VbhQpw2LG2hbISNO_BLfi8Piv4V3-2jBqV58ppm4luySkTYPHBBcah3B8px1RapdKTFfLSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=emOkVtsnGja40ciARUxjziltjRbceV-RdxpoWJYoSu30hXyiIBtZEwmIFiZlGLTzD158RK0mx-RpJe46wswUtlVFE95NlmYl6moaOM2VfXZDpa3rB-KrMgGiylIBOGp2rrJSzDjpcTXVNPuhDQoqypQqGEpDUFGE6u_Ci-LOffOAstSSsq6go1rUtUZldQDeJQmdUpsqx4Rw251k7EYKUKxHpIirnUFA69YL4-nbfCaG761tB2rQs0OGXsqjnhAVL5T6Exuv9lwoHJ4VbhQpw2LG2hbISNO_BLfi8Piv4V3-2jBqV58ppm4luySkTYPHBBcah3B8px1RapdKTFfLSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو:   این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20146" target="_blank">📅 21:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وزیر نیرو:
این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20145" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20144" target="_blank">📅 19:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20143" target="_blank">📅 17:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez-h12yxNDGlIbyAtr_jk-jEeqw1qeafeq8Kc_vwwrvd15HGEmnvw5lfmsTJfMxZxlzMQJbfuUGwHHAKFcUgPJ8FyRyvNW2EJa4JH5L1j6i9Kh5FeMlGsGei7R-TiQDf66P6olJWLAZUIioPNjAT-cw0H96cb5JXQkiQRukidHNn2Y6esw6vJEV9CqU3YWi9RxCT06U4to4CFeiK_faaYHyg2mqPTcxiFAVWjgTiShUS_ftBX0Lc0nteyjgbYwlhjOf9fNe7X7Zk7WlqhgmY_R_o1I5EW918h_AGK0NCP7YaofC3rKZC1c7eCb8CQd2qiug3pUmtVSu4-zXn-_7jTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20142" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20141">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">برخی اخبار تاییدنشده خبر از سفر عاصم منیر به تهران می دهند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20141" target="_blank">📅 16:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20137">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">انسان‌ها_بحث_درباره_خودآگاهی_هوش_مصنوعی_را_برعکس_در_نظر_می‌گیرند.pdf</div>
  <div class="tg-doc-extra">328.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/20137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک بحثی که وجود دارد اینکه یک مدل «رایانش قهری زیستی» هم مدنظر ممکن است قرار بگیرد. (Forceful Biological Computing) که در آن مغز یک انسان بدون رضایت خودش از طریق کاشت ابزارهای خاصی (نانورباتها یا ....) در اختیار یک شرکت پردازشگر هوش مصنوعی قرار بگیرد.  در…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20137" target="_blank">📅 15:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20136">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترکیه، فاکستان، عربستان، ایران، بنگلادش!  به نظرم اسمش را پیمان «جده» بگذارند بهتر است.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20136" target="_blank">📅 15:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20135">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:   از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20135" target="_blank">📅 14:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20134">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:
از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20134" target="_blank">📅 14:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20132">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZckI3HSOWawvG2b8Tm9nr_7hIgwNrxpoHpJ7OcCsVYBwZIQv-77e5h7l-Fr_Vw5WMVD0aajJGCITPyW-qiCYLvtmvkZSdYmTMNepJ6fjCxMk59p1G6rabQAsnNjwNB3V7rUfkIpk6nXQIxVgOX6766Aa52Fix3Vym6zXVpMUDJ9Ty09uCFzx3l5a-wISBO6krhbzvC-ww8DVQr9_O-Zb7O34zf_RUJWfqimW8BTYNSTOJQB1y4Z0nikki5RRfkfAxWGLG96LgQ4OmCEaXrMp4dKjiIz60PrMR7UVcaI2uzVCnEhIjv1Fotwz9r0tggCoxIdIDMsmwT5x6iC6nd2SyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=SxqdTDnFnf8EaxU0CtCGPTOpDWEJav1jGmqvl3CilmVqNps5v72wJ3q1mt-Cl3vfzigmSzR1XTdNS8xMhL1biP65v4yq3rqbPhxCxKdIvzUonelbc7bEAOylIrwBPEeKyM5qx7ggJAj8XYPKY5uHGgU6lh6ItPqDkWY3W5rGCcGfNpAdeYdk-8_cdAEmIVXzPG0kzOLKIjKMOxazn7CquUHYMypO1UKQ4yAxgC0GiiPxe8PV4BYnv82rnCp3nSEI1wT6JM_1v2K0MYzAfKsecvEvh2fkeH_RFRmK8g82BJr0i_X784gWr1NWnahSM_o9Qx-oPXANzQ37Pni4KUx0XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=SxqdTDnFnf8EaxU0CtCGPTOpDWEJav1jGmqvl3CilmVqNps5v72wJ3q1mt-Cl3vfzigmSzR1XTdNS8xMhL1biP65v4yq3rqbPhxCxKdIvzUonelbc7bEAOylIrwBPEeKyM5qx7ggJAj8XYPKY5uHGgU6lh6ItPqDkWY3W5rGCcGfNpAdeYdk-8_cdAEmIVXzPG0kzOLKIjKMOxazn7CquUHYMypO1UKQ4yAxgC0GiiPxe8PV4BYnv82rnCp3nSEI1wT6JM_1v2K0MYzAfKsecvEvh2fkeH_RFRmK8g82BJr0i_X784gWr1NWnahSM_o9Qx-oPXANzQ37Pni4KUx0XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاریکاتور اکونومیست با عنوان «کمبود رهگیرها» تصویری طنزآمیز اما هشداردهنده از یکی از مهم‌ترین آسیب‌پذیری‌های جنگ‌های مدرن ارائه می‌کند یعنی محدود بودن ذخایر موشک‌های پدافندی در برابر حجم بالای حملات موشکی و پهپادی.
در تصویر، سربازانی که ظاهراً نماینده آمریکاییها و متحدانشان هستند، در حالی که تعداد زیادی تیر دشمن ایرانی در سپرهایشان فرو رفته، زیر بارانی از تیرهای دیگر گرفتار شده‌اند.
دیالوگ بالای تصویر نیز به‌صراحت می‌گوید که جهان به رهگیرهای بیشتری نیاز دارد، اما بخش بزرگی از ذخایر موجود برای دفاع از آسمان خاورمیانه مصرف شده است.
نکته جالب‌تر، شباهت بسیار آشکار ترکیب‌بندی تصویر به صحنه معروف فیلم
300
است؛ جایی که سربازان اسپارتی در برابر سپاه عظیم ایران هخامنشی، زیر باران تیرهای پرشمار، سپرهای خود را بالا می‌برند. این ارجاع تاریخی، پیام کاریکاتور را تقویت می‌کند: مدافعان امروزی نیز با وجود فناوری پیشرفته، در برابر «اشباع» شدن سامانه‌های دفاعی با همان مسئله‌ای روبه‌رو هستند که سربازان اسپارتی به‌صورت نمادین با آن مواجه بودند.
طنز پایانی تصویر نیز تلخ است: سرباز سمت راست می‌گوید «امیدوارم دیگر چنین اشتباهی نکنیم»؛ اشاره‌ای به این واقعیت که مصرف سریع رهگیرها می‌تواند در جنگی طولانی، خود به یک بحران راهبردی تبدیل شود.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20132" target="_blank">📅 08:20 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
