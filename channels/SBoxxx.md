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
<img src="https://cdn4.telesco.pe/file/CNH3YUT3YvaYyJynyQ3RGCWV2F8v2CIpyUUfBzpGDbT5NqTAU5_FfQ9YgZmOlPC9anQhn521i6Uetpd5OdQnXhI8TL8KDXHvbmM89giW6ThmBkgmV9ejalaTDMEOJLe-j_2eZ_STR6TsbzimZhl_m7FFRiH8cAkrJ7DQrMcJ_w9c3EXv7i5cibQ95sNc5SZkXSt9TQoV3rFPMuop_hbFKusdFBOF64fI3cEtbkwdaJEpUltnyhXxtX2DUwj1cjFGh1d7XEQxSzACiXenl5GD5DPvpVg1exjmY433cgpaF2Y8XYKoAhSxgRUoarQ17jz73m8CEwsyiaQ46aDAEwJBAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.4K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 20:21:39</div>
<hr>

<div class="tg-post" id="msg-19027">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سازمان صدا و سیما:
یک کارخانه صنعتی در حومه شهر خمین، ایران، حدود ساعت 7 بعد از ظهر مورد حمله قرار گرفت.
هیچ گزارشی مبنی بر کشته یا زخمی شدن افراد وجود ندارد و مقامات در حال بررسی میزان خسارات وارده هستند.</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/SBoxxx/19027" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19026">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ذخایر نفت خام در ذخیره استراتژیک نفت ایالات متحده حدود 5.1 میلیون بشکه کاهش یافت و به 311.4 میلیون بشکه رسید که کمترین میزان از سال 1983 به شمار می‌رود.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SBoxxx/19026" target="_blank">📅 19:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19025">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر امور خارجه فرانسه:   امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/19025" target="_blank">📅 19:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19024">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر امور خارجه فرانسه:
امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و در ساعات آینده به فرانسه باز خواهند گشت.</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/19024" target="_blank">📅 19:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19023">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDODEQkZhUqrY-ZRJl_xwFrVzO0WfpcEg1_QMyDNQWCFv9jWFs06NuBf8yaWYqYiN40IL9lV5fDztSy7goxtxFCoId8zozZXAvKIsIkK1JJyELj4VMrx040C5s_e2aEsPtjlySF6W_1QtAtRy2x43e4ioQBmjHQLiNw_f8TXpwmX-vsvx9oYvYtfK_3ZXGY5gJNsT0FfZ1D5JCEkCixB_NHJgESMt7ofGcrPbG70CTlj4EF0M-94jf58zZ7Am66Ik2EjTwb3ye7CQFf1fZiubvgY23sF6TJZRbSLyZZS0WNo0f0mf2BQfYxiOI_9ebe4PTDjaU1z6T-psxXQePKSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح نسبتاً پایینی قرار دارد.  معمولاً در این شرایط طلا رنج می شود.</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/19023" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19022">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چهار شهروند هندی در جریان حمله به کشتی تجاری "My Golden Leo" کشته شدند، در حالی که این کشتی در حال خروج از بندر اودسا در اوکراین بود.   سفارت هند در اوکراین به دقت وضعیت را زیر نظر دارد. هند این حمله را محکوم کرده است.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/19022" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19021">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6XYPxILgSmLeu-FI4ZvbGeNfptIFoPQZnPgxdKxjIecgTG0yEIoORHOlNGyhgK5CvGgVAhX98MB2N5CY38MCWsUKm5ByHWoCBruVGSwtH1X4K4u7MCZY3EqA1kyR7FUG8e12xsGCboBMQgoo2IQWuNBhXYhw3GUMSP4kIUkLN61HDyPzNiB5RR2johDD03J7RM5g56uYNF2g3_OiJ_NSwJn7szBUusdwrTIlWiMLoyjz4T2C_yz6ELTWN-4kFG9VA0T3JIgPrSx3IHicM2PpWztgMT343uRfKZE2C3-cxr28WGgG02vPyzeY7RXkPKeXvBYkJdEk2_7UTQ99GmzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره کل کشتیرانی هند شامگاه چهارشنبه ۲۴ تیر با صدور دستوری اعلام کرد تا اطلاع ثانوی هیچ دریانورد هندی نباید به کشتی‌هایی اعزام شود که مسیر سفر آن‌ها شامل عبور از تنگه هرمز است.    در این دستور آمده است: «با توجه به تشدید وضعیت امنیتی در منطقه خلیج فارس، اداره…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/19021" target="_blank">📅 19:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19020">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حمله ایران به بحرین</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/19020" target="_blank">📅 18:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19019">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">از دیشب دیگر دامنه حملات آمریکایی ها به جنوب محدود نیست و تبریز و شیراز هم مورد هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/19019" target="_blank">📅 18:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19018">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مقامات ارشد اسرائیلی به سازمان پخش اسرائیل گفتند:  «ترکیه تهدید کرده است که در صورت عبور نیروهای کرد از خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.»</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/19018" target="_blank">📅 17:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19017">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آتش‌سوزی در یک کشتی باری یونانی رخ داده است. این کشتی در نزدیکی تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفت.
— رویترز</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/19017" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19016">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجار در شیراز</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/19016" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19015">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خب از هرمز ۲۰ میلیون بشکه نفت در روز عبور می‌کرد که برای ۷ میلیون ش جایگزین پیدا شد (خط لوله شرق به غرب عربستان)</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19015" target="_blank">📅 15:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19014">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/19014" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19013">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اگر یک بار دیگر هم فریب میخوردیم با ۲ بار قبلی می‌شد ۳ بار و این اصلا خوب نبود.</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/19013" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19012">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قالیباف :   آمریکایی‌ها تجهیزات نظامی جدیدی را به منطقه می‌آورند و ادعا می‌کنند که قصدشان متوقف کردن جنگ است. آن‌ها شرط‌بندی کرده‌اند که ضریب هوشی ما به اندازه هوش اندک خودشان است.   ما به مرحله‌ای از تسلط در تشخیص این بازی‌ها رسیده‌ایم و بر این اساس خود را…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/19012" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19011">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXSACnAehEBYOadi2v08o9qOYOjq-rRizafhasc4FBhve9A0pZfpWvBAHdLXN9pTCKA8C_cU-zTOP9TUBdnyzyeV3cH7SmXHC-d9gPQL0BQ4lBLdCB-NrF-sqWn1mnt3Fyv_WW2cLccVNf7PxlBjobpONCJnl47lRul8CfVgmgStH12-pRN_E60fqpGNNNFLjM4ltpG01ebGnkR0dPFyrJQ48gX7WbzLMp42aPfDHgC5xp32CVXqhmFCmRbqCaM8fJ-F0NWwlKxdaJoze8HBijKc7vZdK9h3alOZKwjQuRteZjPwSkSF2mL2zkOs23oPSewVgCPrf3bCbGl3OUxVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف :
آمریکایی‌ها تجهیزات نظامی جدیدی را به منطقه می‌آورند و ادعا می‌کنند که قصدشان متوقف کردن جنگ است. آن‌ها شرط‌بندی کرده‌اند که ضریب هوشی ما به اندازه هوش اندک خودشان است.
ما به مرحله‌ای از تسلط در تشخیص این بازی‌ها رسیده‌ایم و بر این اساس خود را آماده کرده‌ایم. اقدامات باید ادعاها را تأیید کنند، نه اینکه با آن‌ها در تضاد باشند.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19011" target="_blank">📅 15:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19010">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بلغارستان از پارلمان خود می‌خواهد تا استقرار ۸ هواپیمای تانکر آمریکایی در پایگاه نظامی Bezmir را برای حمایت از عملیات ایالات متحده در خاورمیانه تصویب کند.
این اقدام پس از جنجال‌های مربوط به استقرار قبلی این هواپیماها در یک فرودگاه غیرنظامی نزدیک صوفیه بدون تصویب پارلمان صورت گرفته است.
این درخواست در حالی مطرح می‌شود که تنش‌های ایالات متحده و ایران همچنان در حال تشدید است.
منبع: رویترز</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/19010" target="_blank">📅 15:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19009">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دلار فردایی تهران
⏳
188,700 فروش  بازتاب انتشار مواضع ملایم شده دو سوی نبرد روی قیمت دلار داخلی  نکته — موقت است و دوباره بالا می رود.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/19009" target="_blank">📅 15:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19008">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ببینیم آمریکا همان بلایی را که با قربانی کردن اوکراین بر سر روسیه آورد، با ژاپن بر سر چین می آورد یا نه.  در نشست با نیما (پیام ریپلای شده) مفصلاً درباره تاریخ تنشهای میان ژاپن و چین صحبت کردیم.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/19008" target="_blank">📅 14:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19007">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بوی مذاکره می آید…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19007" target="_blank">📅 13:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیروی قدس سپاه پاسداران انقلاب اسلامی ایران مدعی شد که با استفاده از اطلاعاتی که از سوی افراد مقیم اردن به دست آمده بود، به هواپیماهای آمریکایی در فرودگاه عقبه حمله کرده است و ادعا می‌کند که این حمله خسارات جدی و تلفات انسانی به همراه داشته است.
این سازمان همچنین از حامیان خود در اردن تقدیر کرد و خواستار حملات به نیروهای آمریکایی شد.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/19006" target="_blank">📅 13:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPwYCzHQ09CbvmbDUQcXzAHmwc3ehK-OcT4hdoNSlL74ZD422WZRKZbuZ771G013vcodif7WiOLKTWwZ2mT8-pb92WmwNcILLJKaDfDKTY8dPtwjjjD62w3WY1HN_1co0dz-AdU9ZWCiZxhCV2I-blnrM2OCsA17n_zmMYzgaw9hCoeVJZ0IAVB5EXsDkpn9hiWy6zhtSyFbeM858WKh4u4wscCrQGcVpOzOP_xKt6LGFgQkjkCkJQIcLR66hu-29Zey7h4KAp2OZZYbbULRbREEbPkPSt5G4t-UVsPlVviU3toE7aMEBrmlGMfKMgw7BaHJDXhTJSjXODiXfjJvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
سکوت وارش و واکنش بازار اوراق
وارش در نشست کنگره با وجود تأکید بر مهار تورم، از ارائه هرگونه راهنمایی درباره نرخ بهره یا سیاست ترازنامه خودداری کرد و بازارها را در آستانه نشست مهم فدرال رزرو در وضعیت انتظار نگه داشت.
بازار اوراق این سکوت را به معنای احتمال پایین افزایش نرخ در کوتاه‌مدت تفسیر کرد، اما رشد بازدهی اوراق بلندمدت و نرخ وام مسکن نشان داد نگرانی‌ها درباره تورم و بدهی دولت همچنان پابرجاست.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/19005" target="_blank">📅 13:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19004">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">347.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/19004" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 9  دوشنبه 20 جولای 2026</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19004" target="_blank">📅 13:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19002">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN4IDIxUvq16P_cvmwQJECCEdL-4GxwcEe66VcOKJqsx7L-SXtKkmcIJR1ntq1m6a1LfLAWhQCL5dG8dQwYtPsuW1wTchFmd7s_nyg7RZyCSKAqt9-T0ohnX3zYk9s0EuJQoK0cSk2BsXIWiSzlpMA0u8RRbYj8Qju942vMr1ox0gaFM5nwrN-_QpEhOlrcBnXhA-rikKEGZaXG6LqJbeTidV_m8WAWg1RtlT-EL7tSHocWLqrcOOFzjPcNwZ8dEAcYWHHWO5wVAV0r2MCba9A6g9HtilKGCAdVE6oyfuobrbct2NRlKIVjCRk7jIWTxepRs4f1NWG4J52WENK1Y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح نسبتاً پایینی قرار دارد.
معمولاً در این شرایط طلا رنج می شود.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19002" target="_blank">📅 12:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19001">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19001" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 9
دوشنبه 20 جولای 2026</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19001" target="_blank">📅 12:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صدای انفجار مهمات عملکرده در تبریز و مهمات عملنکرده در تهران!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19000" target="_blank">📅 11:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18999" target="_blank">📅 10:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18998">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">UKMTO:
"یک کشتی در فاصله ۸ مایل دریایی شمال غربی شهر خَمْسر در عمان، مورد اصابت یک پرتابه نامشخص قرار گرفت و خدمه کشتی به طور ایمن از آن تخلیه شدند."</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18998" target="_blank">📅 10:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18997">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سخنان شنیدنی دکتر موسی غنی نژاد درباره حرامزاده شیادی به نام علی شریعتی!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18997" target="_blank">📅 10:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18996">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15659d093.mp4?token=SwaO0U4_pXrkGv8iJG_Fj5umIgPyf5XP3t_9ONzOw4Wfdlr55yi2hLbHogSHldW--MhFHELem4tVO6ZGwtP06e5Ilx90SJGphv_jD3KDofg5fjn5riR0V6aRepYf3lmopMt3XN11XtaNVVHAFklOMkL59qzBvZm2nCzNX3nWvScETZEGPcy4lrYKfTYa6x7wqA9kZlax8UYPcWXX2pJDp65Hz1N5Cl0nfd6iyTHifuUf8VgiZcrF7tvQAW91HBftPU8QCzg0kDQ63jkqioe6GtxKYsypB45Oa0Ajk1Cz76V9gfSNmOVfL6zK_gzG9DX_zfQQNlCzO1apVh3ffacvRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15659d093.mp4?token=SwaO0U4_pXrkGv8iJG_Fj5umIgPyf5XP3t_9ONzOw4Wfdlr55yi2hLbHogSHldW--MhFHELem4tVO6ZGwtP06e5Ilx90SJGphv_jD3KDofg5fjn5riR0V6aRepYf3lmopMt3XN11XtaNVVHAFklOMkL59qzBvZm2nCzNX3nWvScETZEGPcy4lrYKfTYa6x7wqA9kZlax8UYPcWXX2pJDp65Hz1N5Cl0nfd6iyTHifuUf8VgiZcrF7tvQAW91HBftPU8QCzg0kDQ63jkqioe6GtxKYsypB45Oa0Ajk1Cz76V9gfSNmOVfL6zK_gzG9DX_zfQQNlCzO1apVh3ffacvRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان شنیدنی دکتر موسی غنی نژاد درباره حرامزاده شیادی به نام علی شریعتی!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18996" target="_blank">📅 10:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18995">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حمله به بوشهر!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18995" target="_blank">📅 09:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18994">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امروز جلسه‌ای برگزار می‌شود تا درباره وضعیت فرودگاه بن گوریون بحث و بررسی شود و به درخواست واشنگتن برای اعزام هواپیماهای بیشتر برای سوخت‌گیری پاسخ داده شود.
برآوردهایی در اسرائیل نشان می‌دهد که واشنگتن ممکن است درخواست اعزام ده‌ها فروند هواپیمای دیگر برای سوخت‌گیری به اسرائیل را مطرح کند.
— شبکه ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18994" target="_blank">📅 09:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18993">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گویا داریم به ساعت صفر حمله زمینی موج 5 نزدیک می شویم.  شاید سرانجام ترامپ توانسته با آب نبات هایی مانند اف-35 و قراردادهای تسلیحاتی و اجازه دادن به ترکیه برای حمله جولانی به لبنان و یافتن جای پا در عمق راهبردی اسرائیل، موافقت و همراهی اردوغان را برای حمله…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18993" target="_blank">📅 09:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18992">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حملات سنگین موشکی ایران به بحرین</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18992" target="_blank">📅 09:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18991">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدای انفجار در چابهار و تبریز !</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18991" target="_blank">📅 04:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18990">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ:
ایران از نظر نظامی تقریباً همه چیزش را از دست داده؛ فقط تعداد کمی موشک، پهپاد و توان تولید برایش باقی مانده، ما تنگه را کنترل می‌کنیم و ایران هیچ کنترلی روی اوضاع ندارد</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18990" target="_blank">📅 04:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18989">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کویت اعلام کرد که سامانه‌های دفاع هوایی آن پهپادهای ایرانی را رهگیری می‌کنند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18989" target="_blank">📅 02:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18988">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تا لحظاتی دیگر پخش زنده بازی تیم های  ملی New Castle و سوییس از شبکه نسیم</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18988" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18987">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO1J4nsloFlGCpNw7D-RII9DNqUogSWAZa5S6ZQFKp_6j60jPTkRn01qwpZjLnTV085fAuujnBL6f6PJ9wIcXCWR35pMprihppyeecsS4fPjP1IFVhgJd79WjQN3aWkxz51x1zEZ9zKG0RuV50fRWjON_jZtT76L4IYolJxhVSIxq_EUuYQaGllA0ZfyzgTJLnjC68M3nbIO4wbcNndrJ-YghumZz2BGOfVlyyr7b9Pr_Ku7LWGDF_c1GsLJFDQoo9bkKcJHBiRvRTWR8YboRJtsQF6kIbaP9OHH4_ey9Em6cWSlW4QPJ7aLmtKsmy8DOAw9C_5DyceMxBvDP1TRsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت پرورش غیرمجاز دام و طیور در حمام</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/18987" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18986">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پمپئو: فشار اقتصادی خفه‌کننده به ایران را ادامه دهید تا اعتراضات داخلی در آنجا رخ بدهد!
وزیر خارجه دولت اول ترامپ:
واقعیت امروز این است که به‌زودی آن محاصره‌ای که سنتکام با کارآمدی بسیار برقرار کرده و همچنین تلاش برای کاهش توانایی آن‌ها در آسیب رساندن به کشتی‌هایی که از تنگه عبور می‌کنند اهرم فشار ایران را کاهش می‌دهد و در نهایت آن‌ها دیگر قادر به پرداخت حقوق نخواهند بود.
حماس، حزب‌ الله و حوثی‌ های یمن، آن‌ها نیز دیگر قادر به پرداخت حقوق نخواهند بود و پول لازم برای خرید مهمات را از دست خواهند داد. و زمانی که این اتفاق بیفتد، مردم ایران فرصتی را به دست خواهند آورد. این مسیر پیش روست. فشار اقتصادی خفه‌کننده، قدرت نظامی و صبر دیپلماتیک، به نتیجه‌ای مطلوب برای رئیس‌جمهور ترامپ و جهان منجر خواهد شد.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18986" target="_blank">📅 01:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18985">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کشتی باری ترکیه‌ای گلدن لیو در اودسا هدف حمله قرار گرفت  کشتی باری گلدن لیو که پرچم گینه بیسائو را دارد و متعلق به یک شرکت ترکیه‌ای است، هنگام خروج از منطقه درگیری با محموله‌ای از غلات، توسط سه موشک کروز خ-۵۹/خ-۶۹ هدف قرار گرفت. این کشتی بخشی از «ناوگان سایه»…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18985" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترکیه سیستم پدافند هوایی S-400 خود را به یک کشور خلیج فارس – احتمالاً امارات متحده عربی یا قطر – فروخته است.  جزئیات نهایی شب گذشته نهایی شد و انتظار می‌رود امروز یک اطلاعیه رسمی منتشر شود.  منبع: عبدالکادیر سلوی، روزنامه‌نگار ترکیه‌ای (روزنامه حریت)</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/18984" target="_blank">📅 00:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18983">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">پناهیان:
اگه بی‌برقی و بی‌آبی رو تحمل کنید،
جهان رو آزاد می‌کنیم و آنها را هم بدون آب و برق خواهیم کرد.
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18983" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18982">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سنتکام:
یک عضو خدمه ایالات متحده در ۱۸ جولای در شمال عراق در عملیات کشته شد</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18982" target="_blank">📅 22:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18981">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gcgf-C5QZ2QmV6P6FbfxoGQxM2DM9BUlEr-GXve1zTsaBlfMgeWpCWd61mq4AmlhjdBepvzRHgbfChwc8WXT0bGnEfojXfuKFkSR5vkwNyI7tFOC4m0xbb1cVjuaAJlo3FA3DNaY-UW1MzvLVp7v3cVpmf8431ILo_UmDIoxadRgHYmKNS7oR98db-TMe64wpUp6eGqXcXi8rfdQFXoJHMm1-ANjASM31vB6UOUNMOYZlJROgK0g0tYqSuizjSgaTdx-c3tNeTOppQeEswg_A-ALRE7r2YAWhhijv7zSY8qVHdDKZtxqPQAE5Pk8bRDNj03gEh5D2sr9CzlnDnHvCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید معروف امشب موقع اجرا واسه فینال جام جهانی، رویِ لباس خودش فروهر نماد ایران باستان و آیین زرتشتی داشت.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18981" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ممکن است آمریکا از اسرائیل بخواهد به کارزار نظامی بپیوندد
برآورد اسرائیل این است که ایران طی روزهای اخیر در حال بررسی و بحث درباره این موضوع بوده که آیا به اسرائیل حمله کند یا نه، اما تاکنون هیچ تصمیمی در این‌باره گرفته نشده است.
ارزیابی دیگری نیز حاکی از آن است که ممکن است آمریکا از اسرائیل بخواهد حتی در صورت عدم حمله ایران، به کارزار نظامی بپیوندد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18980" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مقامات ارشد اسرائیلی به سازمان پخش اسرائیل گفتند:  «ترکیه تهدید کرده است که در صورت عبور نیروهای کرد از خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.»</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18979" target="_blank">📅 21:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گویا داریم به ساعت صفر حمله زمینی موج 5 نزدیک می شویم.  شاید سرانجام ترامپ توانسته با آب نبات هایی مانند اف-35 و قراردادهای تسلیحاتی و اجازه دادن به ترکیه برای حمله جولانی به لبنان و یافتن جای پا در عمق راهبردی اسرائیل، موافقت و همراهی اردوغان را برای حمله…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18978" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18977">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سایت والا:
ارزیابی‌های امنیتی اسرائیل نشان می‌دهد که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18977" target="_blank">📅 19:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18976">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک نیروگاه برق دیگر در کویت در اثر حمله ایران دچار آتش سوزی شد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18976" target="_blank">📅 18:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18975">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزیر انرژی آمریکا کریس رایت:  رئیس‌جمهور ترامپ می‌خواهد جنگ را با یک توافق مسالمت‌آمیز با ایران به پایان برساند، اما برای انجام این کار دو طرف لازم است.  اگر آنها آماده انجام این کار هستند، این راهی است که به آن پایان خواهد یافت. در غیر این صورت، ما جریان…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18975" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18974">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر انرژی آمریکا کریس رایت:
رئیس‌جمهور ترامپ می‌خواهد جنگ را با یک توافق مسالمت‌آمیز با ایران به پایان برساند، اما برای انجام این کار دو طرف لازم است.
اگر آنها آماده انجام این کار هستند، این راهی است که به آن پایان خواهد یافت. در غیر این صورت، ما جریان ترافیک از طریق تنگه را بدون همکاری ایران تضمین خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/18974" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18973">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APujbsE6mSpsDXw3qHD0lBz5mnfWCcEMp5iV0S3LNHXCpJGRoTZOQVrrO33DiEqZDW1r1vBVzPQX5hYu81-HT-cSI8EhwMhpZiqMYjx9rUF3lLgttr9EfVjZWWlAYjw_FWkPJjjvuq89-ErHFECf1cZEe8HX_SHScsxyL2bpRF2lR4QNZ28iZkbHMXraDdD9swQRBe8yZ_FyOf0rb7jmbEvdlV-oH1ZOvMdg6w-sIboU4QPI2DzZciYDmeE_L4dFNWtOxx9r5KJWtXUX5HQ3LGoVeamN2HMv9zhU3ggceidWWFo-UqHr7cVOr_AV3r3nwoF_osipvZb14NNXfGyusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات موشکی جدید ایران  ایران موشک‌های بالستیک را به سمت اردن پرتاب کرده است   برخی از موشک‌ها به سمت بندر العقبه هدف‌گذاری شده‌اند که در جنوب اردن واقع شده است.  تلاش‌های رهگیری موشک در شهر همسایه ایلات در اسرائیل ثبت شد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18973" target="_blank">📅 17:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18972">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیروهای مسلح اردن:   سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -   تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18972" target="_blank">📅 17:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18971">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیویورک تایمز:
هجوم‌های اخیر ایران به پایگاه‌های آمریکا در اردن باعث خسارات سنگینی شده است.
بیش از چهار حمله در پنج روز، موشک‌ها و پهپادها ده‌ها سرباز آمریکایی را زخمی کردند، چندین هلیکوپتر بلک هاوک را آسیب زدند و به تأسیسات نظامی کلیدی ضربه زدند.
کشنده‌ترین حمله روز جمعه در پایگاه هوایی موافق سلطی در عزره رخ داد که منجر به کشته شدن دو سرباز آمریکایی، مفقود شدن یک عضو نیروهای مسلح و زخمی شدن چهار نفر دیگر شد.
دو روز پیش، همان پایگاه مورد اصابت قرار گرفت و حدود ۲۰ سرباز زخمی شدند.
حمله دیگری تعداد قابل توجهی از هلیکوپترهای بلک هاوک را در پایگاهی در شرق اردن آسیب زد، در حالی که حمله‌ای قبلی به یک تأسیسات مسکونی ضربه زد و چندین عضو نیروهای مسلح را مجروح کرد.
مسئولان آمریکایی می‌گویند این حملات نشان‌دهنده توانایی فزاینده ایران برای غلبه بر یا فرار از دفاع هوایی ایالات متحده است.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18971" target="_blank">📅 17:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18970">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سبحان الله این چه وضعیتی است؟!
قرار بود به کمک تازیان بشتابیم تا فلسطین را از اشغال اسراییل آزاد کنند اکنون طوری شده که عربها از اسراییل کمک میگیرند تا پرتابه های ما به چاکرای پایینی شان فرو نرود!
یک جور کمدی پورن شده که انگار عطاران سناریو اش را نوشته باشد!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18970" target="_blank">📅 16:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18969">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروهای مسلح اردن:   سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -   تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18969" target="_blank">📅 16:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18968">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیروهای مسلح اردن:
سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -
تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18968" target="_blank">📅 16:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18967">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عراق، قراردادهایی به ارزش 60 میلیارد دلار در حوزه انرژی با شرکت‌های آمریکایی امضا کرد!  شرکت‌های غربی فعال در حوزه انرژی، روز جمعه، ده‌ها توافقنامه را با مقامات عراقی در زمینه‌های نفت، گاز و پروژه‌های خطوط لوله امضا کردند. این اقدام در حالی صورت می‌گیرد که…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18967" target="_blank">📅 14:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C23OdmfWcKL27YoilyeVUrgAC3og6L0ZP1nWDh4QZgUOg1oW_VYjyjVL2QNN5IyXRbin0JuAQjHSp2cCz84yu1U_SnN9VnOZDCB8o4hQoVHMQftMA2z9WmxXXplAwtr9huBNGTC3MwfFSjtmNVP_nyncbgGPCFWNnbTCRLfPC_acuBNfGLB7gCY9ZX7Bne_954b55MziEh5DQMhbw6S1nfhmrkOXkPQzshAvOUQWkLFDs7EmVX-7BX8ApOYKHU1ezthq7K4XwA62J8YYWV5ou9rf4mcHmt1c3haDE4VthRxO1Hw1PZSQmYV3mn3r3Sh0htHzIrUG7dp81g0wYeKEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپورت:
کاخ سفید به آرژانتین مجوز داده تا در صورت قهرمانی جام‌جهانی، بنر «جزایر مالویناس متعلق به آرژانتینه» را در مراسم قهرمانی به نمایش بگذارند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18966" target="_blank">📅 14:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18965">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:  ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت تروریست‌های آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه پاسداران، تلاش کردند تا تردد را مختل کرده…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18965" target="_blank">📅 13:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18964">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت تروریست‌های آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه پاسداران، تلاش کردند تا تردد را مختل کرده و از طریق یک مسیر ناامن از تنگه هرمز خارج شوند.
دو فروند از این کشتی‌ها دچار حادثه شده و متوقف شدند، در حالی که دو فروند دیگر از ادامه مسیر منصرف شدند.
نیروی دریایی سپاه پاسداران انقلاب اسلامی اعلام می‌کند که کنترل کامل تنگه هرمز در اختیار این نیرو است و تنها مسیر ایمن، مسیر مشخص و اعلام‌شده است.
همچنین تأکید می‌کند که هیچ مقداری از نفت، گاز و کود، بدون هماهنگی و مجوز قبلی از تنگه هرمز عبور نخواهد کرد.
کشتی‌هایی که تحت تأثیر اقدامات دشمنان آمریکایی قرار گرفته و وارد مسیر ناایمنی می‌شوند، قطعاً دچار حادثه خواهند شد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18964" target="_blank">📅 13:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18963">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خب جام جهانی هم امشب به پایان می رسد.
گفته می شود بازی ایران—سوییس  بعد از فینال برگزار خواهدشد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18963" target="_blank">📅 09:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/18962" target="_blank">📅 09:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18961">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چین؛ ضربه‌گیر جدید بازار نفت در بحران هرمز  در سال‌های گذشته هرگونه تهدید علیه تنگه هرمز تقریباً به‌طور خودکار با جهش شدید قیمت نفت همراه بود. دلیل آن روشن بود؛ حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه اختلال در آن، نگرانی از کمبود…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18961" target="_blank">📅 09:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18960">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6DE2ZtI9MCWVyqVox9lBXT0wmZnqe3gWJNJjYpbIkZYO6rkkde_XckgFSblLLPhyFulgNR6LwSX7Y6ujQvPAIqCse7OSyC5CnWYCOyT-qg_ndi8PTAc2_LNebYxvEjtHQnmC7FzGhTpjn_LeFPsoFXLSYlP94SGYV7Q4UcaP97vtMaB1xjxmj0AGzi8h4WsSH85xKJ_fR_NTNs0GNjdHrHjGca2Rw-fPlS3waf9_Dg3zBrErbn_JYzsD4cFmDHuAUSR7J8WiEG6Au-J3eRPGQEr2MpZxNg92GE_X1nIEry3JBXNQa6ZZNpKuc_UOP5LTQJHJ5MP2Th-3d1mcVTB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین؛ ضربه‌گیر جدید بازار نفت در بحران هرمز
در سال‌های گذشته هرگونه تهدید علیه تنگه هرمز تقریباً به‌طور خودکار با جهش شدید قیمت نفت همراه بود. دلیل آن روشن بود؛ حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه اختلال در آن، نگرانی از کمبود عرضه را افزایش می‌دهد. با این حال، ساختار بازار جهانی نفت در سال‌های اخیر تغییر کرده و اکنون یک متغیر جدید در معادله ظاهر شده است:
رفتار وارداتی چین
.
چین که بزرگ‌ترین واردکننده نفت خام جهان است، دیگر صرفاً یک مصرف‌کننده منفعل نیست، بلکه به بازیگری تبدیل شده که می‌تواند شدت نوسانات بازار را تعدیل کند.
گزارش نیکی آسیا
نشان می‌دهد که چین در دوره‌های شوک عرضه، نقش «واردکننده نوسانی» (Swing Importer) را ایفا می‌کند؛ به این معنا که با کاهش موقت خریدهای خود، بخشی از کمبود عرضه جهانی را جبران کرده و از تشدید افزایش قیمت‌ها جلوگیری می‌کند.
این توانایی از چند عامل ناشی می‌شود.:
نخست، چین طی دو دهه گذشته سرمایه‌گذاری عظیمی در ایجاد ذخایر استراتژیک و تجاری نفت انجام داده است. هنگامی که قیمت‌ها افزایش می‌یابد یا مسیرهای عرضه با تهدید مواجه می‌شوند، پکن می‌تواند برای هفته‌ها یا حتی چند ماه بخشی از نیاز پالایشگاه‌های خود را از این ذخایر تأمین کند. در چنین شرایطی، کاهش واردات به معنای کاهش مصرف داخلی نیست، بلکه صرفاً جایگزینی نفت وارداتی با نفت ذخیره‌شده است.
عامل دوم، انعطاف در مدیریت ذخایر تجاری است. چین در دوره‌های قیمت پایین، معمولاً بیش از نیاز روزانه خود نفت خریداری کرده و مخازن را پر می‌کند. اما در دوره‌های افزایش قیمت، این روند متوقف می‌شود و حتی بخشی از ذخایر مصرف می‌شود. در نتیجه، واردات کاهش می‌یابد، بدون آنکه فشار قابل‌توجهی بر فعالیت‌های اقتصادی وارد شود.
از سوی دیگر، پالایشگاه‌های چینی نیز انعطاف عملیاتی بالایی دارند. بسیاری از آنها می‌توانند برنامه تعمیرات یا کاهش موقت ظرفیت تولید را با شرایط بازار هماهنگ کنند. علاوه بر این، تنوع منابع تأمین نفت از روسیه، آسیای مرکزی و سایر تولیدکنندگان غیرخلیج فارس نیز وابستگی کامل چین به نفت عبوری از تنگه هرمز را کاهش داده است.
این تحول، پیامدهای مهمی برای بازار جهانی نفت دارد. در گذشته، کاهش عرضه از خلیج فارس تقریباً به همان میزان باعث افزایش قیمت می‌شد، زیرا تقاضا در کوتاه‌مدت انعطاف چندانی نداشت. اما اکنون، کاهش چندصد هزار بشکه‌ای واردات چین می‌تواند بخشی از این شکاف را پر کند و از شکل‌گیری موج‌های شدید سفته‌بازی جلوگیری کند. به بیان دیگر، چین علاوه بر اینکه بزرگ‌ترین خریدار نفت جهان است، به یکی از ابزارهای تثبیت بازار نیز تبدیل شده است.
البته این نقش محدودیت‌های مهمی نیز دارد. ذخایر استراتژیک چین نامحدود نیست و اگر تنگه هرمز برای چندین ماه به‌طور کامل بسته بماند یا صادرات کشورهای حوزه خلیج فارس به مدت طولانی متوقف شود، پکن نیز ناچار خواهد شد با کاهش واقعی مصرف، افزایش هزینه‌های انرژی و فشار بر صنایع خود کنار بیاید. بنابراین، توانایی چین بیشتر برای مدیریت شوک‌های کوتاه‌مدت و میان‌مدت کاربرد دارد، نه بحران‌های طولانی‌مدت.
در مجموع، یکی از مهم‌ترین تغییرات بازار نفت در دهه اخیر این است که دیگر تنها عرضه‌کنندگان بزرگ مانند عربستان سعودی یا تولیدکنندگان شیل آمریکا بر قیمت‌ها اثر تعیین‌کننده ندارند. اکنون رفتار خرید بزرگ‌ترین واردکننده جهان نیز به همان اندازه اهمیت یافته است. این تحول باعث شده تهدیدهایی مانند اختلال در تنگه هرمز، هرچند همچنان خطرناک، اما نسبت به گذشته تأثیر کمتری بر جهش پایدار قیمت نفت داشته باشند؛ موضوعی که می‌تواند بخشی از اهرم فشار کشورهای صادرکننده نفت در بحران‌های ژئوپلیتیکی را نیز تضعیف کند.
#ژئوپولیتیک
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/18960" target="_blank">📅 09:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18959">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yekyz_AD_jlD1XOYTlUKD-XfDDzTpXqDnao_bu8GNhrZUMEI6dwZ3BheUj9MpnTti_L1MCrRmQ_fKoCjAI8xhRhg9f4zbkDpfM1VxVqQT5PD0V9EK7VOuBp6hQZK9Np63O2fQjJdy2NQhmhuZ_M00uNhoUnLyJKHaMEaQ0Ir2msDnTSbng36it-VQ2Gip5Vn_zFbhF9sz8IQIIyGfWBVqOORZqeNo3_elezItXTKaqeLlX1gImtBB-3ATS1PJwBZZUXhEPvLEvDq37jow7cP59qpt70n9MacDWC9vbXwGjh_0LsZ_2q9Kpcy-oD0d0umEtcE8NvnjfR23NtPtFT-1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلی از یکی از نزدیکان محسن رضایی</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/18959" target="_blank">📅 01:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18958">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a107e63.mp4?token=b4RFeGI7QRItftVI9LHJgj6pdScfxvuc7XjSHLSX9Opt0VYDzXGqpJ89KwSOx9RxPQtNH3wSW6_Vt3kdWgUnBkxrveWp6DcbV9aTq9V5qPQRsRvT56szWSyVuSQbBzsqECMKWudUb37ruEyUGgL_46ItOBvT1whewiBalczQU1OiG8rVMXjPY4SapMG99dloLwf4IMFTwX8PRJ3ZNI7Sd0lFNvpotYc472YhCe78EjxGAQ5f_1hKdWDgx7hFwR7pr4ASkP0mbSRPzYAdbKTuIn-w3JWEGH77cSZp90xe_CUpJeBIGJepIywqRUzWppL4IpAaTyzgAleweUHiBs-4qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a107e63.mp4?token=b4RFeGI7QRItftVI9LHJgj6pdScfxvuc7XjSHLSX9Opt0VYDzXGqpJ89KwSOx9RxPQtNH3wSW6_Vt3kdWgUnBkxrveWp6DcbV9aTq9V5qPQRsRvT56szWSyVuSQbBzsqECMKWudUb37ruEyUGgL_46ItOBvT1whewiBalczQU1OiG8rVMXjPY4SapMG99dloLwf4IMFTwX8PRJ3ZNI7Sd0lFNvpotYc472YhCe78EjxGAQ5f_1hKdWDgx7hFwR7pr4ASkP0mbSRPzYAdbKTuIn-w3JWEGH77cSZp90xe_CUpJeBIGJepIywqRUzWppL4IpAaTyzgAleweUHiBs-4qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/18958" target="_blank">📅 00:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18957">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بندرعباس؛ گلوگاهی که فروپاشی‌اش فاجعه است   بندرعباس تنها یک شهر ساحلی نیست؛ گره‌گاهی است که بخش بزرگی از تنفس اقتصادی و لجستیکی ایران از آن می‌گذرد. بندر شهید رجایی، بزرگ‌ترین بندر کانتینری کشور، حدود ۸۵ درصد از کل تخلیه و بارگیری بنادر ایران را انجام می‌دهد؛…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18957" target="_blank">📅 23:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18956">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">—گزارش‌ها حاکی از آن است که جنگنده‌های F-16 نیروی هوایی ایالات متحده مستقر در پایگاه هوایی اسپانگدالم در آلمان به خاورمیانه اعزام شده‌اند. این هواپیماها قادر به هدف قرار دادن سیستم‌های راداری پدافند هوایی ایران و همچنین دارایی‌های موشکی هوا به زمین هستند.
علاوه بر این، جنگنده‌های پنهان‌کار F-35 از پایگاه هوایی لکن‌هیت در بریتانیا نیز به همراه تانکرهای اضافی سوخت‌رسانی هوایی برای پشتیبانی از عملیات گسترده‌تر هوایی ایالات متحده به این منطقه اعزام شده‌اند.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/18956" target="_blank">📅 23:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18955">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8yct9iA4tEWJdUlu2eiphCyB4cIx0KPVreeMxcTB9ln8Mlvd50TWxuRrAdTpbiCrLEOt56d5HvNhcSl4bVhTKu-oqByvyLLx8zc6fk4FetG44dBFhEmdsHEn8TbJI9Q0dMi2usmquv-zpSt3W4lFR0Lj2MasavmOeBrsvrZd0Yq4CXCvULTtfJUjCS9PGmm_FRLqTVPAnkgZCEMQbkN_SAWwf-fbs4h3GbHuz9pmc7kzsWl0B656iFayJmOmTP87VgY3l1I7KbYeFvZsDFoMMcbwquCVT7WBOctgTSQZDRai6nBEYGThEGUDZDM7kUbyhYPlshP8HShJIJFyNevvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس؛ گلوگاهی که فروپاشی‌اش فاجعه است
بندرعباس تنها یک شهر ساحلی نیست؛ گره‌گاهی است که بخش بزرگی از تنفس اقتصادی و لجستیکی ایران از آن می‌گذرد. بندر شهید رجایی، بزرگ‌ترین بندر کانتینری کشور، حدود ۸۵ درصد از کل تخلیه و بارگیری بنادر ایران را انجام می‌دهد؛ سالانه نزدیک به 6 میلیون کانتینر و تا 70 میلیون تن کالا از آن عبور می‌کند. این بندر مستقیماً به شبکه ملی راه‌آهن و بزرگراه‌های ایران متصل است و همین اتصال، آن را به مسیر اصلی جابه‌جایی تدارکات نظامی، سوخت، نیرو و کالای تجاری میان مرکز ایران و کرانه جنوبی تبدیل کرده است. موقعیت مسلط بندرعباس بر شمال تنگه هرمز نیز دروازه ایران به مهم‌ترین گلوگاه انرژی جهان است.
اما اهمیت بندرعباس به کانتینر و اسکله ختم نمی‌شود. پالایشگاه ستاره خلیج فارس در همین منطقه مستقر است؛ بزرگ‌ترین تولیدکننده بنزین ایران که به‌تنهایی حدود ۴۰ درصد بنزین کشور را تأمین می‌کند و بزرگ‌ترین پالایشگاه میعانات گازی جهان به شمار می‌رود. پالایشگاه نفت بندرعباس نیز در کنار آن قرار دارد. افزون بر این، در دوره‌های کمبود، بخشی از بنزین وارداتی ایران هم از همین بنادر جنوبی وارد و توزیع می‌شود. به بیان دیگر، تولید سوخت، واردات سوخت و ترانزیت کالا در یک نقطه جغرافیایی واحد متمرکز شده‌اند.
همین تمرکز، شکنندگی خطرناکی می‌سازد. انفجار مهیب فروردین ۱۴۰۴ (آوریل ۲۰۲۵) در بندر شهید رجایی، که ده‌ها کشته و نزدیک به هزار زخمی بر جای گذاشت، نشان داد چگونه یک حادثه واحد می‌تواند قلب تجارت دریایی کشور را از کار بیندازد و زنجیره تأمین را در سطح ملی مختل کند.
اکنون تصور کنید ایران این بندر را از دست بدهد. پیامد آن، قطع همزمان ۸۵ درصد تجارت دریایی، توقف حدود ۴۰ درصد تولید بنزین ملی و مسدود شدن یکی از اصلی‌ترین مسیرهای واردات سوخت خواهد بود؛ ترکیبی که به بحران سوخت سراسری، اختلال در زنجیره تأمین نظامی و لجستیکی، و فلج بخش عمده‌ای از اقتصاد وابسته به واردات می‌انجامد. از دست رفتن دسترسی مطمئن به تنگه هرمز نیز اهرم راهبردی ایران را به‌شدت تضعیف می‌کند.
بندرعباس دقیقاً همان نقطه‌ای است که در آن بیشترین اهمیت و بیشترین آسیب‌پذیری به هم گره خورده‌اند و بنابراین حفظ کنترل آن برای ایران نه یک انتخاب، که یک ضرورت وجودی است.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SBoxxx/18955" target="_blank">📅 23:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18954">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مقامات آمریکایی نگرانند که چین یا روسیه ممکن است به ایران در حمله به اهداف ایالات متحده کمک کنند.
به گزارش وال استریت ژورنال، ایران اکنون موشک‌های مانورپذیری را با سرعت‌های بسیار بالا شلیک می‌کند.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18954" target="_blank">📅 23:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18953">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الاغ ما سالهاست در جهنم هستیم؛ دروازه هایش را بگشایی همه فرار می کنیم!</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/18953" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18952">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انتظار تشدید بی سابقه تنش ها می رود...</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/18952" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18951">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TW7udGFGtu-AzQrN53buGQDS35EPMAJzuku66bUhMb_aA73bMj5EfMdqG9LTvaw4-e3-cfApWx9MtPdJM92n9myjar_h5QwEX_LH4cyH-mAO3AP3Cg4wy-ydQh-n_ndQ3gsV2d_vaua-uTjSKaVsXavtrHG2S6wSUsuBAdxO6buce22iBmo7yJsxX3q5-v3bdmKNTgnBAjko-GlnbPxnppQNW8p0zEvSQQp6VNmsrOD3f8qgB5E013pIM17DK-RWjYxZWtOrNmXWh2jGcdu2axYpNIIUP-L-lbv0xaBAF_kzphjKh3XG3q_uEszJs5Mhcgdi3RFXk38Jar-HqlOAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع آمریکا در واکنش به کشته شدن دو سرباز آمریکایی:
«خدا نگهدار قهرمانان. فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند.»</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18951" target="_blank">📅 22:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18950">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کریمه؛ از ویترین پیروزی پوتین تا آسیب‌پذیرترین جبهه روسیه
حملات مداوم اوکراین، کریمه را از نماد اقتدار روسیه به یکی از ناامن‌ترین مناطق تحت کنترل مسکو تبدیل کرده است. منطقه‌ای که زمانی مقصد گردشگران بود، امروز تقریباً هر شب هدف پهپادها قرار می‌گیرد؛ تا جایی که مقامات محلی برای جلوگیری از ایجاد وحشت و اختلال در فصل گردشگری، سامانه‌های هشدار هوایی را عملاً غیرفعال کرده‌اند. در بیشتر نقاط شبه‌جزیره، حملات به پایگاه‌های نظامی، زیرساخت‌های انرژی، خطوط راه‌آهن و مراکز لجستیکی به بخشی از زندگی روزمره تبدیل شده است.
تمرکز اوکراین بر قطع شریان‌های تدارکاتی، فشار بی‌سابقه‌ای بر کریمه وارد کرده است. حمله به پایانه نفتی کرچ، آسیب به کشتی‌های باری و تهدید کریدور زمینی از جنوب اوکراین، انتقال سوخت و تجهیزات را دشوار کرده است. خاموشی‌های گسترده، محدودیت فروش بنزین و اختلال در تأمین کالاها، نشانه‌هایی از فرسایش توان لجستیکی روسیه در این منطقه هستند. همزمان، پهپادهای اوکراینی پالایشگاه‌ها و تأسیسات نفتی در عمق خاک روسیه، از جمله اطراف مسکو، را نیز هدف قرار داده‌اند و بحران سوخت را تشدید کرده‌اند.
اهمیت کریمه برای کرملین تنها نظامی نیست؛ این شبه‌جزیره مهم‌ترین دستاورد سیاسی ولادیمیر پوتین پس از الحاق در سال ۲۰۱۴ محسوب می‌شود و جایگاه ویژه‌ای در روایت ملی‌گرایانه روسیه دارد. با این حال، افزایش ناامنی، کاهش اعتماد مردم به توانایی دولت در حفاظت از منطقه و مهاجرت تدریجی خانواده‌های مرفه، نشان می‌دهد که هزینه‌های جنگ به قلب این نماد سیاسی رسیده است.
با وجود این، نشانه‌ای از تغییر گسترده وفاداری ساکنان به روسیه دیده نمی‌شود. بسیاری از مردم، به‌ویژه در سایه تبلیغات گسترده امنیتی و نگرانی از برخورد احتمالی اوکراین، همچنان بازگشت حاکمیت کی‌یف را تهدیدی برای خود می‌دانند. اما آنچه بیش از هر چیز در کریمه و حتی سراسر روسیه به چشم می‌آید، خستگی عمومی از جنگی است که پس از سال‌ها نبرد، هنوز چشم‌انداز روشنی برای پایان یا پیروزی آن وجود ندارد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18950" target="_blank">📅 22:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18949">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVzeMkwXaWbR0lXpzlZAboJoNH8IK-7-l2AdfmcfX7ut1gFOOHOuOa6AAvSRUOXpEsxInLzAR_CKOhy5lFqFI_NzjUAgBskiujq7Y8Hv7Kd7qbGlZevgJSbIOX3j5M4UL1o04Q38Kjgz7GkvKOvFCuI3QMGl6UmvesSMmUIhEh7_7Za3umrJTul1Fu_esngWWJco2-Ycpx0HzusBs7Ep5sU9b8XhrIZk-Keu4A4M59cKPHniMS3dPnCqKe-KpSmuo-oEnfUe2YG9A0uQUrCfuY0Q36AqqHB8gsqenMMc1kSshzdgrWfcdaNynxaw7PEMDGCCCLk0zUqH9AN3HhQqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید گدبان سفیر اسرائیل در سازمان ملل:
موج آهنین درحال برخواستن است.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18949" target="_blank">📅 21:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18948">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLlrcrhesj3WDZHCzyuOUlwRrgCcksxAIqMbbb1EGvYmqCLfZLzY2xgBPTykXSpSVfsiGq4DwUJp1PcU2XUNBnN8MDaynE482wuWvf2oAqYv3IT1E8h_oshRsp-hIS4Fz55N2S1oRetu_JvsrowKb5pF_18U0UhjsMkNKheGCw6_gZOcA8B8_xy2WE6g1Z9x6cR43Dl3D4aIs7w-1puRmzzaMyjYYuzpaoms49a2EduB-8fyckZcQtNZ6dpP7GopeXdRNDCxD58wmgDt5MuJsS2wvk7oYS5Ioxflx9eJ0TLRZas8PvNH0xz8k-qz_fjDSnKefLLurIkoE4pCdz7gzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ممکن است سپاه پاسداران را مانند داعش نابود کنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، در اظهاراتی تازه احتمال اقدام نظامی گسترده علیه سپاه پاسداران انقلاب اسلامی را رد نکرده و گفته است که واشنگتن ممکن است این نهاد را «مانند داعش از بین ببرد». این سخنان در شرایطی مطرح می‌شود که درگیری میان آمریکا و ایران پس از فروپاشی آتش‌بس دوباره شدت گرفته و دو طرف وارد مرحله‌ای از حملات متقابل شده‌اند. (
Time
)
ترامپ در پاسخ به پرسشی درباره اینکه آیا ممکن است سپاه را همانند داعش هدف قرار دهد، گفت که «خواهیم دید چه اتفاقی می‌افتد». او همچنین مدعی شد که ایران بار دیگر خواهان مذاکره شده است، اما همزمان تأکید کرد که واشنگتن حاضر نیست بدون تغییر رفتار تهران، مسیر گفت‌وگو را ادامه دهد.
سپاه پاسداران یکی از مهم‌ترین ستون‌های ساختار قدرت جمهوری اسلامی محسوب می‌شود. این نهاد علاوه بر نقش نظامی، در حوزه‌های امنیت داخلی، برنامه موشکی، فعالیت‌های منطقه‌ای و شبکه نیروهای هم‌پیمان ایران در خاورمیانه نقش گسترده‌ای دارد. آمریکا در سال ۲۰۱۹ سپاه را در فهرست سازمان‌های تروریستی خارجی قرار داد.
مقایسه سپاه با داعش از سوی ترامپ نشان‌دهنده تغییر احتمالی در سطح اهداف جنگی آمریکا است. عملیات علیه داعش عمدتاً با هدف نابودی یک گروه شبه‌نظامی فراملی انجام شد، اما سپاه بخشی از ساختار رسمی حکومت ایران است؛ بنابراین هرگونه تلاش برای «نابودی» آن، می‌تواند به معنای رویارویی مستقیم با یکی از پایه‌های اصلی جمهوری اسلامی و افزایش شدید خطر گسترش جنگ باشد.
اظهارات ترامپ در حالی بیان شده که آمریکا حملات خود علیه اهداف نظامی ایران را افزایش داده و اعلام کرده است که مراکز فرماندهی، سامانه‌های پدافندی، توان موشکی و پهپادی و زیرساخت‌های مرتبط با تهدید علیه کشتیرانی در تنگه هرمز را هدف قرار داده است. ایران نیز در واکنش، حملاتی علیه مواضع آمریکا و متحدانش در منطقه انجام داده است.
از نگاه تحلیلگران، تهدید علیه سپاه نشان می‌دهد که اختلاف میان تهران و واشنگتن دیگر تنها حول موضوعاتی مانند برنامه هسته‌ای یا تحریم‌ها نیست، بلکه به سمت یک رویارویی ساختاری درباره نقش منطقه‌ای ایران و معماری امنیتی خاورمیانه حرکت کرده است.
در صورت عملی شدن چنین رویکردی، آمریکا با یک انتخاب بسیار پرهزینه روبه‌رو خواهد شد: تلاش برای ضربه زدن به مهم‌ترین نهاد نظامی ایران، بدون آنکه تضمینی برای فروپاشی ساختار قدرت تهران یا پایان درگیری وجود داشته باشد.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/18948" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18947">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq34HmjKBEmBTPRweUYX2PwFNTD8LJ5DncNCnVxWnmjT8yXG4TDOUhubEw5nPmSZ7Bq-qPUUMuQlN6T-tUAxHuj8h1eHgHMG1oeGDCJRfT7mtFebJ6v9wUpM6GQDtd7-OYExAAG2CAXDAhMl847aLKcSlc7g2CdXe1zQdIr_Xh4PUKN_jAs-Gi6w--4mBAMUD_vKuGCnZFzN0V9NhWQtV08n3Jts2Hm80Ovm2zGR-qjo2h6T0BQSQVrbthFVz5ewkSl9Xs-s_G5Bebh1aIWpSN8EuSWc1F2rlzgz68_VGFMQzbhNh7d2LWFJpVzaCcW6pU8HkVbQ_GBHBKytH7s3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار تشدید بی سابقه تنش ها می رود...</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/18947" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18946">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18946" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18945">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ2-RcYFnVav9hr31n2us3JCFCR9Wa3vnOroilZtLouWq93UZfP6qnfJ0jPYN-lmYlhg2oYuOSRWbyPyBVzGO6sEd8AgAycAmKyILOJPUXnWLfjgR7oTWZorI7uH6Zz1XhpGhGJLfZZnwte9c7hx9LmlyRc0JKRIuJvpF3xlu628nf-saGeuOQjHDWAIIuaD2TvOko8w6BJHqIcuBaGY6hvSRCphQcGERq0bt-bdl366J0H7UNTeNLn6g5xF64py-MdqSAuOJh7WlE7CDDSkrFYjub0aTvWN8NC7oX460qzV8q6omw_vZd7G94r4RSIhsQstXBFpI_Xk8E2owNxA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/SBoxxx/18945" target="_blank">📅 20:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18944" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18943">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.
در حال حاضر، یک نظامی دیگر مفقود الاثر است.
چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.
سایر افراد که دچار جراحات جزئی شده بودند، به وظایف خود بازگشتند.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/18943" target="_blank">📅 20:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18942">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxrtw4f_3Uz5H3hmCUsYDoEKiKaM4VhthFvK5-jq_1n8acM6mDGI10ntdacsirod4L84c6VdqKSXFED5UXDY1t0-tx-oEzuK_iUC9Et9xLhtaZzmgMaSf8VOI8-7QOWHYWcaOeSGXMaYCcuXyCm9qvnRlqOAQ-NE9Hkb5dwCnJ2YX7B4tywApoLND191N_1ZoN2L_LAnjqji6i4WI88gfC51M0SBEzPEtwF6-oGKCQX0NFEf-zugkb386UEWp-Fd-lV4Nqo0Qk1urowJCwV9bZffLw8VMjS8ja8tUpK_DGGlbTVKBdrLOWobdwGi0U3pQ9Cx6GaCdJEFCbSS_5LRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام می گوید در حمله سپاه به پایگاه آمریکایی ها در التنف سوریه هیچ تلفاتی وارد نشده است.  اساساً به نظر من حمله به سوریه پیامی تهدیدآمیز به جولانی بود که به حزب الله حمله نکند ولی اینها جدی گرفتند.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18942" target="_blank">📅 20:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18941">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4886d9a21f.mp4?token=D_i8tDS5hJjE6cK27SIa5fKuuRfxV7c65Ww-sW-ZhDKiFKlNn8ATmAIQzjrUbx0klNQJGPtLIQpw8GukQRSu9IPxggsrT7jcbAZsFTsu9ldIq3ItxQJj7UC2h6OWViXCwvznZLKYyNZpjFxlL-hdKoMHbqQKaYjCtwksY3PwYEZ2C7LXvxBGmZWC18XoVTKRtvW_SWWfZSkL8ePbX9XMLDPLcqvZ3jKk4trV8fqHPkrCbBJZMD4lioyPKMC5ov_25bJRrzmFVD0JAupZHQj0rkNAk0Gv4xIqQrH2BIQNeU29vdyP9WwrACG92Xfx2C0Gdt7wut_-Erp06kJDWH3e3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4886d9a21f.mp4?token=D_i8tDS5hJjE6cK27SIa5fKuuRfxV7c65Ww-sW-ZhDKiFKlNn8ATmAIQzjrUbx0klNQJGPtLIQpw8GukQRSu9IPxggsrT7jcbAZsFTsu9ldIq3ItxQJj7UC2h6OWViXCwvznZLKYyNZpjFxlL-hdKoMHbqQKaYjCtwksY3PwYEZ2C7LXvxBGmZWC18XoVTKRtvW_SWWfZSkL8ePbX9XMLDPLcqvZ3jKk4trV8fqHPkrCbBJZMD4lioyPKMC5ov_25bJRrzmFVD0JAupZHQj0rkNAk0Gv4xIqQrH2BIQNeU29vdyP9WwrACG92Xfx2C0Gdt7wut_-Erp06kJDWH3e3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می شود این ویدیو مربوط به اعزام صدها نیروی ویژه آمریکایی به جبهه های جنگ ایران است.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18941" target="_blank">📅 20:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18940">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarket Podcast -- 8.pdf</div>
  <div class="tg-doc-extra">210.5 KB</div>
</div>
<a href="https://t.me/SBoxxx/18940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 8  جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18940" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18939">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 8  جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18939" target="_blank">📅 20:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18938">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بلومبرگ :   قیمت بنزین خودروها در ایالات متحده با تشدید رویارویی بین واشنگتن و تهران، بار دیگر به نزدیکی ۴ دلار در هر گالن رسیده است</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/18938" target="_blank">📅 19:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18937">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عراق، قراردادهایی به ارزش 60 میلیارد دلار در حوزه انرژی با شرکت‌های آمریکایی امضا کرد!  شرکت‌های غربی فعال در حوزه انرژی، روز جمعه، ده‌ها توافقنامه را با مقامات عراقی در زمینه‌های نفت، گاز و پروژه‌های خطوط لوله امضا کردند. این اقدام در حالی صورت می‌گیرد که…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18937" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18936">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انتقاد شدید علی‌اکبر ولایتی مشاور رهبر شهید انقلاب در امور بین الملل از نخست‌وزیر عراق  سفری تأسف بار، بی‌موقع و تخریب کننده مجاهدتهای ملت غیور و مجاهد عراق در تاریخ چند هزار ساله این کشور بزرگ، توسط نخست وزیر جوان و کم تجربه، آقای علی الزیدی.  وی تأکید کرد…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18936" target="_blank">📅 19:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18935">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟  قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.  در بحران ۲۰۲۶ نیز با وجود کاهش نسبی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18935" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18934">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزارت خارجه قطر:
«ما مجدداً تأکید می‌کنیم که هدف قرار دادن نیروگاه‌های برق و تأسیسات شیرین‌سازی آب در کویت از تمام خطوط قرمز عبور می‌کند».</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18934" target="_blank">📅 17:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18933">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18933" target="_blank">📅 17:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18932">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟  قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.  در بحران ۲۰۲۶ نیز با وجود کاهش نسبی…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18932" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18931">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWuOpLGbyAdWRNhtY1F85HkCtIyLaGTBBGAzxMc3Wg2ihJIAUvpy6v2xPXGSA6fDxjg8ShD-XAlWYWAXVxSxigopl1NL0qB1YOIGo6EtbwI8IqZH7LIztpJ6BMrOsZxNQaftYxbHIXUJjnLcDDf6OgRCEOeQdU-pNyLizQAeCD-FY92wpsSkq2NoT9o8kJK2wNynMKHG14Fq3_o1LAEec_zn9PWnniRsHg5srdRViV7A5ekBUluwifDoKyXcQSH_RC5y8uV8uQcPQFc2ya1Eum2XplVjY4R_XVK__N-EU5nR3JcU-b8Ps6YBZJAlNMfwAhmdnigO-Enus7hvGzgZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟
قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.
در بحران ۲۰۲۶ نیز با وجود کاهش نسبی قیمت نفت پس از آتش‌بس، ماندگاری قیمت بالای بنزین فشار سیاسی بر ترامپ را حفظ کرد و به عاملی مهم در کاهش نرخ تأیید او تبدیل شد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18931" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18930">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا در مواجهه با ایران کلأ دو راه برایش مانده: بمب اتم یا حمله زیرساختی نابودکننده</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18930" target="_blank">📅 16:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18929">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_W7xdMTQsvqAK4G8fCkg90Kyf04GEf3fk13AptoXF_p_Gwd3IZXY_ozoHgfUjkhn2KmdEG4iSuW1yhIwbKJEqM0c2mafWvwOodEaGb-ltXlWE98V6k6bdfu4VbKXlqs4jku2DoH1oDkbWsgNjiijVPHaKuFmBpeUVM--sRRAq5tDGEsA1AbzbHbyWr1re-p8Jb86dCvwfXU60ya-eWXDi73l-8zbo-bZWCHdvNOZW3VLfN2q0DKwdlgEZvLQWEwLFQkjuK345QE46ulIoUzFM_1Ioz3x8RSRxitlldvm1bfAc9nP3jGcrL-qBMlvUcr6FEOtfEk-Ev-vQSWlesv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف مورد اصابت گرفته در منطقه از سوی سپاه</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18929" target="_blank">📅 16:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18928">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">موشک‌های بالستیک ایرانی آکادمی امنیت کویت را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18928" target="_blank">📅 16:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18927">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18927" target="_blank">📅 11:49 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
