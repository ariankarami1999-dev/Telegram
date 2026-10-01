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
<img src="https://cdn4.telesco.pe/file/aFxFR3qlLdWDmBBYc-OBJnyJ8XmbmHZkFaVxploOZASiPXN2ct1sRU8Z-i2HK54N9R2LDAfUD6ohGPuHoV956MAnemp4Qan1GJENmT7LNLm60OFDqkL5n1Db8Psn0txC58upapm5mtY8W0KDMFQ5w1EoDkUDzcRlxLJm1BD3uLPPA74TcNksIRiCDWuqlZYj_oDNQ6uU674SU-GKnSPVI7XB_732AoQUNz8rNQ_GEAiyMA39GDGu4RPvqmbQumpD1cb7PzHXCmkUY16ChNFY9zi4WhnqDn4Gia_8hdC6T2hCsWxALuBtftnGW4B0QLCvEEipOSVIhwTuhii9BsdwxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 02:47:57</div>
<hr>

<div class="tg-post" id="msg-21413">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SBoxxx/21413" target="_blank">📅 00:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21412">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/21412" target="_blank">📅 00:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21411">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51530cf576.mp4?token=Uc1zKsrfDtBhe1vJ_pRDt84-L2I3NOeXbZ40MTgXMuC-k6jgHugu7dE1z53a41yhCoHvnv9a-9xNqX2x2ciQvLy3ZDNK-e3njG82CON4LtmhdJtL86BWOqvw7tFN9T1Z1pyVzBh7o4_74VW8769_z9KCeOynXpWnWAwNBlb5luU5fOzCNOAdGSkOUgqexCGd6kgL3sv-0enBJQG56lNiGkZ5Z6XEfFiDNq9NKttiKOWBYOpugZ56dBYXGQJjACIahH00a0C39AK6bxY4PWxdMmb_yyvgU5OdFM6345Ppz4y-_X3ikl-C6Ed8xvaA40br-kbf54gkOdaQdDWaXtnvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51530cf576.mp4?token=Uc1zKsrfDtBhe1vJ_pRDt84-L2I3NOeXbZ40MTgXMuC-k6jgHugu7dE1z53a41yhCoHvnv9a-9xNqX2x2ciQvLy3ZDNK-e3njG82CON4LtmhdJtL86BWOqvw7tFN9T1Z1pyVzBh7o4_74VW8769_z9KCeOynXpWnWAwNBlb5luU5fOzCNOAdGSkOUgqexCGd6kgL3sv-0enBJQG56lNiGkZ5Z6XEfFiDNq9NKttiKOWBYOpugZ56dBYXGQJjACIahH00a0C39AK6bxY4PWxdMmb_yyvgU5OdFM6345Ppz4y-_X3ikl-C6Ed8xvaA40br-kbf54gkOdaQdDWaXtnvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/21411" target="_blank">📅 00:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21410">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارشگر:
«آیا ایران در حادثه پایگاه هوایی فرفورد دخالت داشت؟»
ترامپ:
«به نظر می‌رسد که بله.»</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/21410" target="_blank">📅 00:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21409">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ادعای وزیر خزانه‌داری آمریکا:
جمهوری اسلامی در یکماه گذشته حتی یک قطره نفت هم نفروخته است!</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/21409" target="_blank">📅 23:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21408">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هدف قرار گرفتن شرکت آرامکو در شهر ینبع عربستان</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/21408" target="_blank">📅 23:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21407">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مقام ایرانی:
ادعاهای بلومبرگ در مورد پیشنهاد هسته‌ای ارائه شده توسط ایران به طرف آمریکایی در جریان گفتگوها با میانجی‌گران نادرست است</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/21407" target="_blank">📅 23:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سوپرنفتکش ۲.۵ میلیون بشکه‌ای در تنگه هرمز هدف قرار گرفت</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/21406" target="_blank">📅 23:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21405">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
معاون وزیر ارتباطات
:
اگر استفاده از استارلینک گسترده شود ، در مواقع بحران مجبوریم تمام برق را قطع کنیم تا مودم های استارلینک هم از کار بیفتد؛ چراکه حکمرانی اینترنت را نخواهیم داشت</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/21405" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21404">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مقامات ایالات متحده به الجزیره:  ناو هواپیمابر یو‌اس‌اس تئودور روزولت به همراه گروه ضربتی خود، پایگاه سن دیگو را ترک کرده و به سمت خاورمیانه در حرکت است.  تا پایان نوامبر، ۳ ناو هواپیمابر و ۲ گروه ویژه حملات آبی-خاکی در اطراف ایران مستقر خواهند شد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/21404" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21403">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:  به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21403" target="_blank">📅 18:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21402">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:
به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21402" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21401">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به نظر می رسد محاصره شهر راهبردی تعز در یمن از سوی حوثی ها تکمیل شده و کار نیروهای مورد حمایت سعودی در این شهر به پایان خود نزدیک می‌شود</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21401" target="_blank">📅 17:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21400">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تا نزدیکی محدوده دوم ورود آمد.  پوزیشن اول را اینجا با حدود ۲۰۰ پیپ سود تسویه کنید</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21400" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21399">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">#FairValueCurve  نمایه FVC تغییر خاصی نسبت به دیروز نداشته.  محدوده های مناسب خرید:  4165 4148  تارگت ها:  4187 4213</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21399" target="_blank">📅 15:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21398">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyW3nJRXxxObM9yQ_kmPsvKyrCFt0mowTEL4ZWqK2dfae3tTI4NCwSuuRi3eAzKsyoXiAED2a0caugl6AE8Y1TNv9tAbTbRbB1rh2xhhwyII8n-bC8TO4NpNoYQ8anKK_CEtbeuuvTP8PFLxhl7bptwg3a0vjW4bGaotwcVY3nUjlHj4vI2nZEGq_2m0viysHtOuWMPsQxZvyOY4q34VACaeLCxBMeoKJUAy4_DCHafDij9hVrXLrRBkHnoEGYmQEkLkl-Eaz1XoFhPYuFki7u_sMqaFxA6LBi98gcZD7piouBoZ2FPrCwfRa384L-vy_OH5F11o-QkSB_jtmpHriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیآمدهای نظامی امپراتوری ایلان ماسک</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21398" target="_blank">📅 14:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21397">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رویترز:
مقامات دولت سوریه و نمایندگان حزب‌الله در سپتامبر به‌صورت مخفیانه در ترکیه دیدار کردند که نخستین گفت‌وگوی حضوری شناخته‌شده میان این دو طرف پس از سقوط بشار اسد محسوب می‌شود.
این مذاکرات که با تسهیل‌گری نهادهای امنیتی و اطلاعاتی ترکیه انجام شد، بر کاهش تنش‌ها میان دمشق و حزب‌الله متمرکز بود.
سوریه به حزب‌الله اطمینان داد که برای تسلیح‌زدایی از این گروه، مداخله نظامی در لبنان نخواهد داشت، در حالی‌که از حزب‌الله خواست قاچاق سلاح از مرزها را متوقف کند و سلول‌های باقی‌مانده خود را در سوریه منحل سازد.
حزب‌الله تعهد کرد که در امور سوریه دخالت نکند، اما پاسخی مستقیم به این درخواست‌ها ارائه نداد. هیچ توافق نهایی‌ای حاصل نشد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21397" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IMG_9826.PNG</div>
  <div class="tg-doc-extra">4.7 MB</div>
</div>
<a href="https://t.me/SBoxxx/21396" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali_SharifAzadeh – Podcast</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/21396" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Podcast</div>
  <div class="tg-doc-extra">Ali_SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21395" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_445
🗓
October 1, 2026
✔️
تحلیل گزارش دیروز شاخص خرجکرد شخصی مصرف کننده
✔️
ارزیابی وضعیت تنشهای مربوط به ایران
✔️
بررسی تقویم اقتصادی روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21395" target="_blank">📅 12:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">درگیری مسلحانه نیروهای انتظامی با شبه نظامیان مسلح ناشناس که از صبح امروز در زاهدان شروع شده طبق اخبار تاکنون ادامه دارد</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/21394" target="_blank">📅 10:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21393">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21393" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ansf2uGDG-zq24rTZRAZVtShqsgE-4jn8uAAYbnXFwkeYLQ29pzmmQnkqXU6Y5C006Dgoivcjh7jcX4RQIWqkjPIkoKilpNRN8Hu68MmBETvXCIsmW46szCvPUYsU_ZJHZis7kapfllRFMAk0x5IisuQacvFIl27_f1FcrUzvVvXmF0UrZd-_IFxigwAvw0oRIhcOanvlJqRZMQE1s_hcY67i7YPIQ9JxH4zluGYeMKFD0sgjN1vRwLuKjsoVBbYuK3krEX9fUPBnZEAsjdKg_ALUU5re_sYssxzMQeG4Zm161BC04UEBLsvQ_ae-nqvcMlqkJjam9zkWHvi0luzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC تغییر خاصی نسبت به دیروز نداشته.
محدوده های مناسب خرید:
4165
4148
تارگت ها:
4187
4213</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21392" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21391">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCvBVFAS5dd1hnsLKzwiTmECiATSf_q1SZ8QeO5raaV5YSw-shRmyRvFZAVvPCjqbMzf2nkWNWwnuEJbYfPWbQTsSgTkSmzt5vH1cu286MpI4amS7ajq0u8aLGRriTI5EV8Nbe6taHN-cgkjn94F7uf4JYAgmDMCi8O0fyKPmHgD3bMMk7mVzvC8vuiUEOifw3-46u8IfLb3ROH0kRMurBAXvhzohow538FTp11DE89o42j6xopM7lr7dKUUEnMgX8Rj5OMY_UwfrG84XlCOGlVWGYvXESPu4aiOxOC_0HkgqbS6YLYwChQXwRYbkUSui7IaAr7_BS245IyOCs669g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در اصلاحی ها توصیه می شود.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21391" target="_blank">📅 10:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21390">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اکسیوس:     روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21390" target="_blank">📅 10:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21389">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اکسیوس:
روبیو روز دوشنبه پس از توقف مذاکرات، از هیئت ایرانی خواست فوراً نیویورک را ترک کند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21389" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21388">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ادعای عجیب هگست وزیر دفاع آمریکا:
امروز دستور دادم ساختار عقیدتی سیاسی در ارتش آمریکا تشکیل شود!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21388" target="_blank">📅 09:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21387">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYNU5GtBXE0BNHps8xAV-2gL5sNsl3sHNSmfYl1wwipOLjGtwz7amg9Vo4dR06MYlRNQuBTXL90m7Dqzi7VRMhwJEyiCHxTuHvvSSsOIGurcFpFAFkZRcV8nL0SU-CJi7owah1DmBOpqiNuuQxC7MyDKlvm6Cwg0SYcspuEJ-VHhu4yzTjlE5g92c84KjwulWnEplP3a9GDPWV41appw-zQN6APxpUlIWhGgt6PhuXjR05Tk8QWaT810ykGC_PEf5q1XpPpevhpQ7VrHD-a5G2pIlWLd5Qpt9Vlfs8905QU_kL6mhdMDCYEcLzoVFKfpGqmFDSmbKqc6zS03ilVh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تحلیلی بر گزارش PCE دیروز
گزارش PCE در ظاهر Dovish بود؛ Core PCE به ۳٪ رسید و احتمال افزایش نرخ بهره کاهش یافت، اما تورم خدماتی همچنان چسبنده است.
مصرف قوی و پایداری Supercore نشان می‌دهد فدرال رزرو هنوز نمی‌تواند با اطمینان از موضع انقباضی فاصله بگیرد؛ بنابراین پیام PCE برای طلا کوتاه‌مدت Dovish است.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21387" target="_blank">📅 09:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21386">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ درباره ایران:
به‌زودی شاهد اتفاقاتی خواهید بود.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21386" target="_blank">📅 21:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21385">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N58VM7XpoXj711aSGJ0pfv5TfIAB1kr_mEnkB_0ddn3imfLFwdDEvl2NuY4c2HhMKG0bVbVyGF_ZVE285QQLHP-l8dZEDK-AgPSU3qpf01dlC5YkWdnIsl6LluOl7iC-lkzjvpyjuX_qksWqhoOdocSEd3xH9UcJLl4mnFY2M5Z4D0eTXUkOnB8x6EVQSh-1jwFs3Q2Zh80GrslRk60XgYvsjeQ8eVZbZyd5VwkgiOdA4WkuM7By_J2KBuYN9Dta4GLf-jH3iI-RhRzumZDIDoTCWOzqnIfjhPimKIR0PDD9P7X_XkNNHVibnZSp7BIJ8upbXJKrBgr-yqTtaRvaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به توپوگرافی یمن دقت کنید!
آن مناطق کوهستانی در غرب این کشور، عمدتا دست حوثی ها است و از علل شکست سعودی ها و متحدینشان در ۱۰ سال کذشته بوده است</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21385" target="_blank">📅 21:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21384">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21384" target="_blank">📅 20:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21383">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
دبیرکل ناتو: اروپا باید به ایران حمله می‌کرد
دبیرکل ناتو بار دیگر از حمله نظامی علیه ایران حمایت کرد و گفت که به جای آمریکا، اروپا باید چنین حملاتی را انجام می‌داد.
روته در گفت‌وگو با یورونیوز مدعی شد: «صریح بگویم، اروپا ظرفیت آن را نداشت که توانایی هسته‌ای ایران را از بین ببرد. ما نمی‌توانستیم، ظرفیت آن را نداشتیم. در ۱۰  سال می‌توانیم و باید این کار را انجام دهیم.»
دبیرکل ناتو ادعا کرد: «این کار را نباید آمریکایی‌ها انجام دهند. ما باید آن را انجام دهیم. همچنین باید ما باشیم که به وضعیت حوثی‌ها (انصارالله) در دریای سرخ رسیدگی کنیم، نه آمریکایی‌ها.»
‎</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21383" target="_blank">📅 20:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21382">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6qaxeOo_aRg_ySArrwMZ--y8hvC8klekmLF3jqz7fX16y5mhrpMJBVKAvsqBOJFOYERwooAEpxpW8CSS44XYU_onalKIAXFkJRCAaB2GKmRWQLv115XagKaDLpMQREgeeIUMCHMRGsJlSx6rKNR1RKo-gHto5uz9UxkgkDYv1yr4GNO19rzQhzH7IPaJbzBgBemNwm9re6TkoxWZw5ArguXzDk7F_a3VofZ1UOfA4NYvZZDWd4RBTx_fyuf0gGhK-4D1T6Xofb6qwydh61EeKevys1mUSAovzAWdh5T5sZRcXJQyQ8Rbdmqd3Xly0Wfkb8c8ddKnzR-izEaDQBdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21382" target="_blank">📅 19:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21381">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21381" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21380">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:  فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.  بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21380" target="_blank">📅 19:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21379">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21379" target="_blank">📅 19:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21378">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حالا آنهایی که دلار را ریال کرده و در بورس بردند برای برگشت به دلار باید تا آخر پاییز صبر کنند!
یا ذی الجلال و الاکرام!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21378" target="_blank">📅 19:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21377">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نامه بانک مرکزی به تمام صرافی های دیجیتال :   هر کاربر فقط روزانه اجازه خرید ۲۰۰۰ تتر را دارد</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21377" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21376">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21376" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21375">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی خطاب به امارات:
میزبانی از قصاب غزه پیامد‌های مثبتی ندارد/ از جنگ اخیر درس بگیرید و از آغاز جنگ دست بردارید</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21375" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21374">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">— لحظاتی پیش پرتاب یک موشک بالستیک ضدکشتی از فارس، ایران انجام شد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21374" target="_blank">📅 19:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21373">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">معامله تتر از ساعت ۹شب تا ۹صبح روز بعد ممنوع شد</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21373" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21372">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به همراهان ما روی ۴۱۸۷ سیگنال سل داده شد و اکنون نزدیک حد سود نهایی در ۴۱۴۸ هستیم</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21372" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21371">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شکست جعلی که در سقف کانال روی داده، اتفاقاً فروشندگان قدرتمندتری را تحریک به ورود کرده است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21371" target="_blank">📅 18:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21370">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i63Ma0uTt5Yxk1Hv0l7pq8qboepqWZnYKSHmqFAc8qDKyGI0C9YTYbWhHm6eRs_SofesBbAZbZj7___NzhfyuP_V5g1QzXILky-LHimz4cy_aAjqcvd_03W4cOJ8gWw7KWfgewXtBQnENl-zSBME6egqy_7TKK7U4o1LacMALwW_vQc9gFyxBy_eMx2QXtfJIF6txaQJ4hChzBdcxJL46eAYck935rqs9NTvBe51rc-pY21yCz-gWGp3vKrqo7oV0WeHLhtlVi3VgU9XAMj7UtFYNzqW_uI3VylMNCz1Jg8lcscu7uMrAaNAQPUojcyOf-0nrnQsg0A5f7HeYLc03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21370" target="_blank">📅 18:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21369">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB6oEyXdT1tJbLwn2OQJQPvxGf5swVnyBz6WfQmmsB24zRefXbKiZ9xL9aeexSKcnVszCyLYfiavPMLtc34V2_-YUCRffn73C31OILsXUXYslosqLSP71HyoEx1e4pC04_oZxTLoBlei5Q7N3YlyUsEJ1B0Zwmcz0NlLA4kfHEFP2dXaYaZJ-tQtGyHEklMFZSoTdReTlaQUX9LtDTGEQAdF7Sp4M0Y4Pr-KPbAR1fpth9dWNCPqrBXnaTgf7kK9XOQdf-H0SVQ_d9osVxjkGQient6mcXbI83BMD9Dwsds6UsbzA5RqALzj3XDG6lDBVYBX9ogsdaDdeQfAc45SAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول سناریوهای قیمتی</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21369" target="_blank">📅 18:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21367">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sunrun_RUN_Democratic_Congress_Scenario_2026_Revised.pdf</div>
  <div class="tg-doc-extra">84.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/21367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21367" target="_blank">📅 18:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21366">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حمله دوباره یمنی ها به تاسیسات نفتی آرامکو</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21366" target="_blank">📅 18:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21365">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=A2YxDGxTxcKAPKXrDYvd-9ZmGMGHAOoUFEfK8Vo_lzktK5tnDd0FC6TfPt6QVUhg0aOdKlSEdx-mlTY2HeO7jW6QEkLty12BUw8KyWeCyR7MDiCyOlFF7p2EVs36ll6ihc4u2bcmdS5Pv6oK5lxUOBcylj-WeOV_h2cIoDMgRUdpuGU8FOuEcVfbEljYk1FKRAzJq8qXZTjth5oXeQxy2dyvAVi8YrlSvc2ectGZcQ7_lva6tEV9bIncmqOs9aXWU7FyQPyWIuEwHNQc_5UaNPBam9q65FTuAEjR4PZUvZjrlGczBeFfPHkaG_y-OWmav1QuyJdFRDh7R1A5wFODfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df6804c1e.mp4?token=A2YxDGxTxcKAPKXrDYvd-9ZmGMGHAOoUFEfK8Vo_lzktK5tnDd0FC6TfPt6QVUhg0aOdKlSEdx-mlTY2HeO7jW6QEkLty12BUw8KyWeCyR7MDiCyOlFF7p2EVs36ll6ihc4u2bcmdS5Pv6oK5lxUOBcylj-WeOV_h2cIoDMgRUdpuGU8FOuEcVfbEljYk1FKRAzJq8qXZTjth5oXeQxy2dyvAVi8YrlSvc2ectGZcQ7_lva6tEV9bIncmqOs9aXWU7FyQPyWIuEwHNQc_5UaNPBam9q65FTuAEjR4PZUvZjrlGczBeFfPHkaG_y-OWmav1QuyJdFRDh7R1A5wFODfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
آزمایش و رونمایی گسترده چین از نسل جدیدی ربات‌های انسان‌نمای پیشرفته با قابلیت‌های نظامی و امنیتی    این ربات‌ها در نمایش‌های عمومی شامل حرکات رزمی، تعادل پیشرفته، پرش، و تعامل مستقل با محیط هستند و توسط چند شرکت رباتیک چینی به‌عنوان نمونه‌های «آماده کاربردهای…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21365" target="_blank">📅 18:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21364">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این چه پاییزی است که هنوز پایانش نرسیده!  نکبت ها تخمهای خودمان هم جوجه شد از بس که در بحران زیستیم!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21364" target="_blank">📅 17:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21363">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:   جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21363" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21362">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⁨ پاسخ همتی به وزیر خزانه داری آمریکا:
جوجه رو آخر پاییز می‌شمارند!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/21362" target="_blank">📅 17:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21361">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسانه‌های اسرائیلی گزارش می‌دهند که هواپیمای شرکت FlyDubai دارای یک خلبان روسی و یک کمک‌خلبان اوکراینی بوده است، که ممکن است دلیل درگیری ایجاد شده باشد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21361" target="_blank">📅 17:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21360">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Si22neVgw26mRuzH_XS1aXBzIZV-NUlogUByX5IRfOoRCfY3P8Ixwyq6fcbIAJSJxOMITDua5Us6MLOTy9FcHvuv3j6VKgx-rsL7CfprMakFHsewSZIWHkAMjn4mZhPJUNOwAcGDpO5NKmLf78DZe7FYtszjkjAoH2ntkNccYpsBImnb1EPSalT-3XzINKcmRCnJa_Dl6CEROnCDnqdRR0sBGRIFbSaU1tkwGqusrVYXA0pX2Yfbf_KGLkahdez3PIew2c7TdKuMrtolO4ZPMZTWTbK733EWrkT3FMN-DaD7iLpypYIpyDdzAGmJxFSF6503YIixP0t22HrIlPdHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر احتمالی طلا تا آخر هفته</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21360" target="_blank">📅 14:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21359">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فلایت‌رادار از تغییر مسیر یک پرواز دیگر شرکت «فلای‌دبی» به مقصد اسرائیل خبر می‌دهد
بر اساس این گزارش، هواپیما در حال بازگشت به دبی است</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21359" target="_blank">📅 14:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21358">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در فاصله میان حباب منفی تا ارزش منصفانه قرار دارد  در این شرایط، فروش در مقاومت توصیه می شود:  یک مقاومت همین محدوده 4197 الی 4203 است  بعدی 4257 است (احتمالاً نرسد)  تارگت ها:  4182 4148 4124</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21358" target="_blank">📅 14:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21357">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فردا ساعت ۱۳:۳۰ با نیما درباره آخرین تحولات مربوط به جنگ گفتگو خواهیم کرد  لینک تماشای نشست Live</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21357" target="_blank">📅 13:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21356">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رسانه‌های اسرائیلی گزارش می‌دهند که هواپیمای شرکت FlyDubai دارای یک خلبان روسی و یک کمک‌خلبان اوکراینی بوده است، که ممکن است دلیل درگیری ایجاد شده باشد.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21356" target="_blank">📅 12:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21355">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارواح عمه تان آخر هواپیمای در حال پرواز هم جای دعواست؟!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21355" target="_blank">📅 12:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21354">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2F8-T_pXgkocSpV5kODR3mB9Xh1xjPvei_NqqpzYlMk9B7hxBf6Cq3bTfpi3ZC1T-NbwIJmIhyJQGVsDQf1uJUa7OWqlTgoSARR6fJ3dn0xIAnwzT2zzVefScKsktjgNO6Zd4yrrsGXgs_dGwU3yUDQwDWmbMcqGrHfChE9IEPOGRV9S-etS_1Hk8BGmcw7ZWNjsgXZsVfYvespcUsDZnPW4f6MjLcUD_Mp3l-oZugwMsaCkGY-oB6wTWw5qfKTEGlCf8QbUDZkZAW2wmCxi_TsdePMsBExDiFqDKhwOiGNsz-bYhsfWkmMt9Wcuo8Vms8QVBfIcBz0Bqtgyetgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در فاصله میان حباب منفی تا ارزش منصفانه قرار دارد
در این شرایط، فروش در مقاومت توصیه می شود:
یک مقاومت همین محدوده 4197 الی 4203 است
بعدی 4257 است (احتمالاً نرسد)
تارگت ها:
4182
4148
4124</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21354" target="_blank">📅 12:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21353">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwKVm5N-PBz_LyYvYAeO55AaeXw1EMzqA-L7qWXGbhmyUYNBqMDMr2jYbmomhWQCLzPiWGALPhqDF3XVU_Fb8vMLb0DKmF6ZW5rluQeBwI87RM0YnGwl4PBarBDKD5RBgUUF8S0n9zbHZKWWsLL-sdvVFUwb5jpe-Jmwd-ULtbr2_4WuOqjKyIYxaXQdS2wuZ8xDfLxBujtJGfp2jtlith_5PFUbzJfGJAFt-_9EuECRnU7ZJyBgml9vm-UhHxt2XLdDEo8iffGCPnZ9n4VKvqaHjA0E9jLi6UU1h60Fgl-spHTCkezPZEOoZB5j2y5dytLnjKeK-zfLo9W1RlICKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21353" target="_blank">📅 12:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21352">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f193b66f88.mp4?token=CxVMaIWGsmoWhm07gXXTCK9DPrQC1TTCTQh2gIqwnl5hs4Q_rDtL0TLHq2dzrSlYYMbF_5tDQ6QVi2C8UnSCvpEnEDcRyzNirqZam4Xv8xC7lI7SHxTMIg-xT5DiL3Tq5sFe6afZ1SiTKs0vNdovQ1WGCiETa0RJivEDgxC49VAZo8-NfdFC1nJl_sNVetsR5GdbXfvuuYs3KXojYgG7Dc7x4SRqNDtCEKHoABTEhKnsriaIBxODeWKT9d4FLd_N4Qbr6sfh8pi51qbIbIOpCNYJoux8NPcsVB6hOX-OOwZIzRHocmZ-NtKAVBj8TubBwpAervHExCeyB1DUOTljmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f193b66f88.mp4?token=CxVMaIWGsmoWhm07gXXTCK9DPrQC1TTCTQh2gIqwnl5hs4Q_rDtL0TLHq2dzrSlYYMbF_5tDQ6QVi2C8UnSCvpEnEDcRyzNirqZam4Xv8xC7lI7SHxTMIg-xT5DiL3Tq5sFe6afZ1SiTKs0vNdovQ1WGCiETa0RJivEDgxC49VAZo8-NfdFC1nJl_sNVetsR5GdbXfvuuYs3KXojYgG7Dc7x4SRqNDtCEKHoABTEhKnsriaIBxODeWKT9d4FLd_N4Qbr6sfh8pi51qbIbIOpCNYJoux8NPcsVB6hOX-OOwZIzRHocmZ-NtKAVBj8TubBwpAervHExCeyB1DUOTljmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین خبری بود که در ۹۳ سال گذشته از سمنان منتشر شد.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21352" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بانک مرکزی گفته از امروز به هر  کارت ملی ۱۰ هزار دلار تعلق می گیرد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21351" target="_blank">📅 10:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IMG_9815.PNG</div>
  <div class="tg-doc-extra">4.8 MB</div>
</div>
<a href="https://t.me/SBoxxx/21350" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali_SharifAzadeh – Podcast</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21350" target="_blank">📅 10:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Podcast</div>
  <div class="tg-doc-extra">Ali_SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_444
🗓
September 30, 2026
✔️
دو گزارش نسبتا ضعیف اما کم اهمیت از اقتصاد آمریکا
✔️
تحلیل مواضع اعضای فدرال رزرو
✔️
دلایل عدم ثبت سقف جدید برای نفت
✔️
بررسی تقویم اقتصادی ‌روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21349" target="_blank">📅 10:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مادر… ها!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21348" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">— واردات خودروهای لوکس خارجی را آزاد می‌کنند — دلار برای تقاضای وارداتی رشد می‌کند — خودشان در قیمت ۲۶۰ تومان دلار را به ملت می اندازند — با پولش سهام ویران خودگوه و صایپا میخرند — مجوز را لغو می‌کنند  — سهام خودروسازها صف خرید می شود</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21347" target="_blank">📅 10:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">— واردات خودروهای لوکس خارجی را آزاد می‌کنند
— دلار برای تقاضای وارداتی رشد می‌کند
— خودشان در قیمت ۲۶۰ تومان دلار را به ملت می اندازند
— با پولش سهام ویران خودگوه و صایپا میخرند
— مجوز را لغو می‌کنند
— سهام خودروسازها صف خرید می شود</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21346" target="_blank">📅 10:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رسانه‌های اسراییلی ادعا کردند علت درخواست کمک، دعوا بین مسافران بوده</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21345" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مقامات اسراییلی منتظر نظر کارشناسی کاپیتان شهبازی هستند</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21344" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21343">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کاپیتان شهبازی:
با ۲۵ سال سابقه میگویم؛ علت این حادثه این بود که سوخت هواپیما گران شده و تصمیم گرفته شد در مقصد نزدیک تر فرود صورت بگیرد تا در مصرف سوخت صرفه جویی بشود</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21343" target="_blank">📅 10:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21342">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مقامات اسراییلی منتظر نظر کارشناسی کاپیتان شهبازی هستند</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21342" target="_blank">📅 10:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Middle East Core</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21341" target="_blank">📅 10:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هواپیمای «فلای دبی» که از دبی به مقصد اسرائیل در حرکت بود، در فرودگاه تبوک عربستان سعودی به زمین نشست.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21340" target="_blank">📅 10:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21339">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هواپیماربایی در مسیر امارات—اسراییل!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21339" target="_blank">📅 10:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هواپیماربایی در مسیر امارات—اسراییل!</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21338" target="_blank">📅 10:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21337">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آکسیوس به نقل از یک منبع آگاه:
هیچ پیشرفت ملموسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها خواستار مواردی هستند که واشنگتن نمی‌تواند آن‌ها را بپذیرد.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21337" target="_blank">📅 02:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21336">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بوئینگ مسابقه F/A-XX نیروی دریایی ایالات متحده را برنده شد و با شکست دادن نورثروپ گرومن، قراردادی با ارزش بیش از ۲۰ میلیارد دلار برای توسعه جنگنده نسل بعدی ناوهای هواپیمابر نیروی دریایی را به دست آورد.
پیش‌بینی می‌شود که این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین F/A-18E/F سوپر هورنت و EA-18G گراولر شود.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21336" target="_blank">📅 01:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21335">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فردا ساعت ۱۳:۳۰ با نیما درباره آخرین تحولات مربوط به جنگ گفتگو خواهیم کرد
لینک تماشای نشست Live</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21335" target="_blank">📅 01:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21334">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تتر = ۲۵۷ هزار تومان!</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21334" target="_blank">📅 00:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21333">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">روس‌ها همیشه موقع مذاکره ایران با آمریکا کرم میریزند</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21333" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21332">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">برخی منابع روسی از احتمال قریب الوقوع جنگ با اسراییل خبر می دهند</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21332" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21331">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">برخی منابع روسی از احتمال قریب الوقوع جنگ با اسراییل خبر می دهند</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21331" target="_blank">📅 23:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21330">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrcpQnHK-auqe6vUhZOY4y2fIyiru50_WvFDR7HX025gXYaHWZMhOtxQJTHEUDxzAXYPn9ZRPiImbW1ZENwM5INAOPfYOM_DYQ9Wb2jAUQgVGlUtcB7UgBW9IWFcBctWL5pf8SKNo97OgK8qiGX8p2trvzYks9Z45Cnc8Rdx3cpPzN3XCxYlyuRmJs04LGXY3mSoOt7nWkj_CxFCA08JVWaDmbRrV9rBm8j0YvBgAbRckXL-ENooHDko7kMWmghQo5kAHSyYAK6iOLPjOFBzd-KFCZh2EHP_pKpwtrLXPapff6XgA2cLJV1k8gRmJwHL-YNRc9XWKrhrOLOX3s7GKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SBoxxx/21330" target="_blank">📅 22:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21329">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آغاز دوباره حملات موشکی و پهپادی سپاه به سمت کشتی ها در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21329" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21328">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اظهارات جی.دی. ونس درباره رهبری ایران:
در ایران شما جناح‌های تندرو را دارید، محافظه‌کاران، میانه‌روها و روحانیون.
و همه این افراد در فرآیند تصمیم‌گیری نقش دارند.
و البته، رهبر عالی‌مقام جدید نیز حضور دارد اما بسیار منفعل است. او در امور روزمره دخالت نمی‌کند.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21328" target="_blank">📅 20:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21327">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اعزام دو اسکادران جدید جنگنده‌های F-22 ایالات متحده به اسرائیل
خبرگزاری‌های بین‌المللی و رسانه‌های عبری از جمله i24NEWS تایید کردند که ایالات متحده در یک حرکت بی‌سابقه، ۱۲ فروند جنگنده رادارگریز نسل پنجم F-22 Raptor را همراه با ده‌ها هواپیمای سوخت‌رسان پیشرفته (از جمله تانکرهای KC-46) در پایگاه‌های نظامی اسرائیل مستقر کرده است.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21327" target="_blank">📅 20:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21326">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21326" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21325">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">باز تنگه بندها ریختند تو فضای رسانه ای!  احمق های نفهم شما تنگه ترمز را ببندید اولا چین زیان سنگینی می‌دهد و شما را برای همیشه از فهرست متحدین خود حذف می‌کند و ثانیا دو هفته بعدش، جزایر سه گانه را از دست خواهیم داد.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21325" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21324">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">درگیری مسلحانه میان شبه نظامیان بلوچ  و نیروهای نظامی در ایرانشهر</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21324" target="_blank">📅 19:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21323">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">درگیری مسلحانه میان شبه نظامیان بلوچ  و نیروهای نظامی در ایرانشهر</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21323" target="_blank">📅 19:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21322">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بهترین محدوده مقاومتی = 4169 الی 4175</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21322" target="_blank">📅 19:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21321">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo8S7xwEyG39_VcTQa0GndMG41BAP3Xqwht175vlB77FGAxD6C5A6GnX1OAAsjEuNPB3zXcC0dCLFQ6OGDucM58o_m63uAAXE3e3pUTo_70iVgAw7dV3boSxIDax8LXuhXkwjN8YONALmBKIElt2Zc5AkBcTRM03rXOnsZDV4BygjsGMeViAEa4oEN7s69Dpm2dVJfCBNhW24iqqkVxQGRWTomdxD7ezxu6kyOn345dwjRdUFN5PnvAQvlCJGLMv8dgxEOv7s1CQJxVgDSC_ILDjy8QpPyaRYEm3ccmaK4KF-jOHVUB2QstpDJfecpuTyGZlDqrQ4e9bn27-aG45Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
🥹
🥹</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21321" target="_blank">📅 19:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21320">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سخنگوی ارتش ایران: اگر تشخیص دهیم که یک حمله دشمن قریب‌الوقوع است، قطعاً یک عملیات پیشگیرانه را انجام خواهیم داد. - خبرگزاری فارس.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21320" target="_blank">📅 18:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21319">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ: ایران به شدت در حال شکست است و به زودی از بین خواهد رفت. قیمت نفت به شدت کاهش خواهد یافت.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21319" target="_blank">📅 18:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21318">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیدار بن‌زاید و نتانیاهو در ابوظبی در قالبی «گسترده‌شده» برگزار شده که شامل کشورهای عربی دیگر و برخی کشورهایی که روابط رسمی با اسرائیل ندارند، بود.
بر اساس گزارش کانال ۱۴ اسرائیل، نمایندگان عربستان سعودی، مراکش، کویت، بحرین، لیبی (حفتر)، عمان و مصر نیز در این نشست که در روز یکشنبه برگزار شد، حضور داشتند.
نتانیاهو و بن‌زاید ابتدا به صورت خصوصی با یکدیگر دیدار کردند و سپس مقامات سایر کشورها به جلسه گسترده پیوستند.
بحث‌ها بر روی ایران، همکاری نزدیک‌تر بین اسرائیل و کشورهای خلیج فارس، مسائل اقتصادی و سیستم‌های دفاعی اسرائیل متمرکز بود.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21318" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21317">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
اطلاع داریم که کشور های عربی حاشیه خلیج فارس با تأمین مالی آمریکا و اسرائیل برای جنگی تمام عیار علیه ایران موافقت کردند و در حال فشار به روی ترامپ برای آغاز هر چه سریعتر جنگ‌ می‌باشند.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21317" target="_blank">📅 17:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21316">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نامه سپاه پاسداران انقلاب اسلامی به مردم آمریکا
این دولت خودکامه، کودک‌کش، هوس‌باز و نادان را کنار بگذارید؛ امور خود را به اندیشمندان بسپارید، نه به زورگویان، و به آنها یادآوری کنید که جهان تغییر کرده است.
مردم جهان بیدار شده‌اند و دوران غارت ثروت ملت‌ها با زور و شمشیر به پایان رسیده است؛ این، قرن پیروزی اراده ملت‌ها است. ادامه دادن این مسیر غیرانسانی، سرنوشتی دردناک را برای آمریکا رقم خواهد زد، زیرا روزی که مستضعفان علیه ستمگر قیام کنند، بسیار وخیم‌تر از روزی خواهد بود که ستمگر علیه مستضعف عمل کرد.
هفت ماه پیش، ارتش متجاوز آمریکا —با نقض قوانین بین‌المللی و ارتکاب جنایت جنگی— جنگی علیه ایران آغاز کرد و با حمله به یک مدرسه ابتدایی در میناب، 168 دانش‌آموز را به قتل رساند، در حالی که همزمان به دفتر آیت‌الله سید علی خامنه‌ای، رهبر انقلاب اسلامی، نیز حمله کرد و ایشان و خانواده‌شان، از جمله نوه 14 ماهه ایشان، را به شهادت رساند. از آن زمان تاکنون، بیش از 3600 نفر —که بیشتر آنها غیرنظامی، از جمله 400 کودک— به شهادت رسیده‌اند، و هشت دانشگاه، سه بیمارستان و هشت مدرسه بمباران شده‌اند.
اگر در صحت گفته‌های ما تردید دارید، می‌توانید سفری کوتاه به هر نقطه از ایران که مایل هستید —حتی تنگه هرمز— داشته باشید تا از نزدیک صحت اظهارات ما را بررسی کنید.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21316" target="_blank">📅 15:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21315">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">علت تاخیر در ارسال GRI و FVC این بود که در نشست لایوی با نیما و امین و پیام بودم.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21315" target="_blank">📅 15:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21314">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">#FairValueCurve  نمایه FVC اندکی از محدوده بیش—فروش فاصله گرفته اما حباب ندارد و کماکان زیر ارزش منصفانه است.  در این شرایط بهترین راهبرد، فروش در مقاومت ها است.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21314" target="_blank">📅 15:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21313">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKHHJj2c8oMZjYJtXEUMiD0VZ0PpK-hc7kOvi0SRZVFq1iC0vq2banN9YxF3q1xA68Y0Y4WNiDctNh8jyWNqcVjGPYHPK-SwcqEyKWCfdatZIuNwlXHe1-ClWdIr9NRQc7sJggMVxZeg40rxZFcrMfDG7b-aty9Yfc0540Vw5p4fDucACZxyVEqCn661zxrTiURSCgFMRnk2OsGbky-hs1aMH6ZYU5tTXUNGl-nESUMm3Zd4v26Z4r0GoVIVmLAEWc9o6wxhRHObIYw-J2LTTTy5vYy5O8pvx6TNumPlOC9tLG-HUk8ChFTkwjO7M9Aydy3f5hNN8P_T-fjrXL4wyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC اندکی از محدوده بیش—فروش فاصله گرفته اما حباب ندارد و کماکان زیر ارزش منصفانه است.
در این شرایط بهترین راهبرد، فروش در مقاومت ها است.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21313" target="_blank">📅 15:16 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
