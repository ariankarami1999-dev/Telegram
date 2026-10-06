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
<img src="https://cdn4.telesco.pe/file/WOpU48kJUupeyagb48xAeWQUlPMAhfJoWdL2Ax123CicIAlY9Jk70_rtsiusbwOxum5AdnXA3lpy09V40k9F1SP2qTdHwJtCLhW2nsjuDRttj2C3gj7IFGYvllsWVc5Xr0ptpN-EkiEip1OLSn-fsHlqYDNjj3AGFQ_VdKejzdZTBIUoZxzAxV9AvVv2ept5xYHreR7zGC2Ob9DoADmMdO0Dt0DhDFDC6E4vLJAlGDISBqFbMRmJQrLuqjNqiuC-2MM54EVR8Vmzn75npO18DY3_XrGJey8SWVgmlROuXh8ojLwIzQHPN6KybhecD9Jt7M_1x22ZLrvElEGpOrHdOg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-696145">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3d0f1fd8.mp4?token=BM7j8bLlUdkj53QO8FYvwtDQt5jP_ho7q8kJlLX5K4Xl19ksNrpn4kd27dfML_wlP-FIoUQ4WSHltxkqZm65hzc_r8XRRBUn3qtMBzDeWVYLz5nbxrfLP7npkRKhHg1fRcQObe3RbzznXdXOmaTtGTaBm6Y9JJv3wDbLfMxTtFJ2Lxk2Tgi2jtPx5oV-rqPNcYaXI2izMJo6vevfxc8Wr_qRyWLcmkflZ6bMQZKPhXoQlFtrUNEBa7_RWAGzY61m4uXrqE3_lFeCXMjg447UQkd4eRsbeRZNa3u9_1fi58Q29Xw2mfpewHsJoENTcjlTiq-2L4zP6yXk4yO_kxJhjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3d0f1fd8.mp4?token=BM7j8bLlUdkj53QO8FYvwtDQt5jP_ho7q8kJlLX5K4Xl19ksNrpn4kd27dfML_wlP-FIoUQ4WSHltxkqZm65hzc_r8XRRBUn3qtMBzDeWVYLz5nbxrfLP7npkRKhHg1fRcQObe3RbzznXdXOmaTtGTaBm6Y9JJv3wDbLfMxTtFJ2Lxk2Tgi2jtPx5oV-rqPNcYaXI2izMJo6vevfxc8Wr_qRyWLcmkflZ6bMQZKPhXoQlFtrUNEBa7_RWAGzY61m4uXrqE3_lFeCXMjg447UQkd4eRsbeRZNa3u9_1fi58Q29Xw2mfpewHsJoENTcjlTiq-2L4zP6yXk4yO_kxJhjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با مفهوم علائم درج‌شده روی برچسب لباس‌ها آشنا شوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/696145" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696144">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎂
برج‌میلاد‌تهران‌تولدش‌را‌
باشـهروندان‌جـشن‌می‌گیرد
🤩
تا۵۰٪تخفیف‌ویژه‌بازدید
وشـهربـازی‌بـرج‌مـیلادتهران
🚗
نمایشگاه‌خودروهای‌کلاسیک
🛵
نمایشگاه‌مـوتورهای‌کلاسیک‌
با‌عنوان‌‌نمایشگاه‌"پـلاک‌طهـران"
👶🏻
بـرنامه‌های‌ویژه‌هفته‌‌ملی‌کودک
همراه‌بازدید‌رایگان‌کودکان‌زیر۱۲‌سال
اجرای‌ویژه‌برنامه‌‌بچه‌های‌ایران‌قوی
🎸
همراه‌گـروه‌مـوسیقی
👬
اجرای‌جُنگ‌خانوادگی
🎭
باحــضور‌هنــرمندان
🗓️
روز‌هــای ۱۶ و ۱۷ م
ـ
هر
🕐
ساعت ۰۹:۰۰‌ الی‌ ۲۳:۰۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/696144" target="_blank">📅 17:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696143">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
عارف: از شرمندگی مردم بیرون می‌آییم؛ افزایش کالابرگ نزدیک است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/696143" target="_blank">📅 16:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696142">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO9t0ih8CHuQDG0_uMwN7e0kw5U9w7Vbtah8YT0OnZWTA47A5cg9BFP4gW5Z1DPGx0NIcKUIDf1sNXHlh6C87LfC2asXsErqPD9ePdV-RP8rMbrHjYWIWArAriTJkFjdrwnnnqmwemVT5tBBah7GmdhuhB3CaJSFkr1kdAHUGvZ-IXH9_sROZmXKGbQQp-Q6eaS3Lzt0kQL_5ZZTCF0sZgV_3FJ_G4_LhWOZNwhaGvXiff_dfkBWCw1TNaKPQvY9LuqykYAYuXDQFpazzarqJsx3a1vMmSw_-iaSOUlBw-lyMSL6dFYXi0H2z6ORNxwm9Uime2c9UnlNEhz1HcSqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت آزمایشی اینستاگرام لو رفت/ بی سروصدا و بدون تعامل به پروفایل‌ها سرک بکشید
🔹
اینستاگرام ظاهراً درحال بررسی قابلیتی به نام Read-Only Mode برای مشترکان Instagram Plus است که به آن‌ها امکان می‌دهد پروفایل‌ها را بدون امکان لایک، کامنت، ارسال پیام، فالوکردن یا مشاهده استوری‌ها ببینند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/696142" target="_blank">📅 16:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696141">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سقوط بالگرد آمریکایی در دریای سرخ
🔹
یک بالگرد MH-60R آمریکا نزدیک ینبع پیام اضطراری ارسال کرد و داده‌های راداری ارتفاع آن را صفر نشان می‌دهد؛ سقوط هنوز رسماً تأیید نشده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/696141" target="_blank">📅 16:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696140">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شایعه انفجار در فاز یک اندیشه تکذیب‌شد/ هیچ حادثه‌ای گزارش نشده‌است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/696140" target="_blank">📅 16:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696139">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c99b29251.mp4?token=IQdr7cnYsAlvuJHDodYYuebwai37fFB3UpwxjjTPy87rzAGaU2cgVgFOk1nwiYfmhqmL28vc3flFE9abB-H0L4kUAlPKyF_pWZTCz5RvKyZ1_bxq3_GkLCFs6K7964Hx9U09TLSzu53x-pHEmxB9_ruJIFSWqQlQ9rDixU0PRW4OzqEKyyuZ0Rwsg2DHmMyErCrN9PcycjPeGhB2i65xvxekB0AkwOFxBmMuKUIcSheeKsPd1-NS10Ka-hdQGnUKvzq42K_a3JKF9g18AHtlKO-AsHBiPhL8JVuPjdR68pVfQFmItKnArwdwV6bxwNC-CQLwDTgxls_96PdCjiEZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c99b29251.mp4?token=IQdr7cnYsAlvuJHDodYYuebwai37fFB3UpwxjjTPy87rzAGaU2cgVgFOk1nwiYfmhqmL28vc3flFE9abB-H0L4kUAlPKyF_pWZTCz5RvKyZ1_bxq3_GkLCFs6K7964Hx9U09TLSzu53x-pHEmxB9_ruJIFSWqQlQ9rDixU0PRW4OzqEKyyuZ0Rwsg2DHmMyErCrN9PcycjPeGhB2i65xvxekB0AkwOFxBmMuKUIcSheeKsPd1-NS10Ka-hdQGnUKvzq42K_a3JKF9g18AHtlKO-AsHBiPhL8JVuPjdR68pVfQFmItKnArwdwV6bxwNC-CQLwDTgxls_96PdCjiEZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه برخورد یک سیارک با ماه؛ انفجاری که سطح ماه را به آسمان پرتاب کرد!
🌕
☄️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/696139" target="_blank">📅 16:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696138">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
رئیس جمهور با صدور حکمی پاک‌نژاد وزیر سابق نفت را به عنوان مشاور خود منصوب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/696138" target="_blank">📅 16:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696137">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/696137" target="_blank">📅 16:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696136">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a7fe12250.mp4?token=FOhNhBOr0dtYrWrai7Oh9jYWNmRML9iUN1agRUA2FYf7vnBJ6OBJDLlxjU4_kY7nsGXqINh1pENWYSK4fRClVC62DMxsRNH7MP2kmTws1H9sSLkTGvEDjjGcoLRAI9V4xMtd9WOiRzCfzz7JUwmMGKQaOHLog2nPcOFSXMs1_uU9zzt1hHULuUD4f4KryZiSIVdmP-U77Iu8ruFusRG9Zo7hUZfogwPsP6jY-RzSB3DPzuatpWEoq23QcYZHojwgdlSm2CgpLDcujQalWx0FRdpIi4KNpuwTZ_5d_XP-2CIMRDFQHBsrrM4bBmJIB5-lbeO432k2YAbYeVp09B_rLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a7fe12250.mp4?token=FOhNhBOr0dtYrWrai7Oh9jYWNmRML9iUN1agRUA2FYf7vnBJ6OBJDLlxjU4_kY7nsGXqINh1pENWYSK4fRClVC62DMxsRNH7MP2kmTws1H9sSLkTGvEDjjGcoLRAI9V4xMtd9WOiRzCfzz7JUwmMGKQaOHLog2nPcOFSXMs1_uU9zzt1hHULuUD4f4KryZiSIVdmP-U77Iu8ruFusRG9Zo7hUZfogwPsP6jY-RzSB3DPzuatpWEoq23QcYZHojwgdlSm2CgpLDcujQalWx0FRdpIi4KNpuwTZ_5d_XP-2CIMRDFQHBsrrM4bBmJIB5-lbeO432k2YAbYeVp09B_rLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرپرست وزارت نفت: تراستی کار بانکی است، ما فقط فروش نفت را داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/696136" target="_blank">📅 16:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696135">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSDQoPIzuCRuVMJOhRlLt22nnT49fbn6bBo0Kww8_C5vOLKgDs2r7ca4kT3hvRgupt_oZ1w2gmXBebdPX68iw1pwArGMntFo2vrdYBNyJMOulfgFEfGkhW-dCfkCp-7CFvey3fH3T9VCXS2PLabqlFF9PnzcjDD5Nb4HU9QX3FzX3oZph6khfHQzpFs-Dx0-SdmBn9dGQrwGoc7ed8Ofw92ozPfipaI87baAx7cRF_eWZTdhy_dNEYS3Uk-tJYqeZD_WE2-AUR9_A1mzrScbR1fBz_id4O_Oa-9h7le1OK83q0W8m9hsgvroYHUI2mkBU2r_dB_6dJNaE1rpiCkNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس پیشین سرویس جاسوسی آلمان به اتهام جاسوسی بازداشت‌شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/696135" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696134">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
سرلشکر رضایی خطاب به دشمن آمریکایی: شما در جنگ نظامی شکست خوردید و در جنگ اقتصادی نیز شکست خواهید خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/696134" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696133">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حادثه امنیتی در نزدیکی پایگاه هوایی آمریکا در انگلیس
🔹
پلیس انگلیس از وقوع یک «حادثه بزرگ» در نزدیکی پایگاه هوایی آمریکا در فیرفورد و بازداشت چند نفر به ظن نقض قوانین مواد منفجره خبر داد.
🔹
ساکنان مناطق اطراف نیز به‌دلیل این حادثه تخلیه و به یک مرکز تفریحی…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/696133" target="_blank">📅 16:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696132">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMu0bw_xBP15Lf2Us8Gp-_hIEpe61lG_wAcZAaUjQLrdeOLpNY9_LDMZldxtlsR9s8vOnivfr-8tmJo_wCx9s_pTP5L5WO1wKE0vo79gaRlC4BbSagMH1NysEUQy93zryoR0R5vGYVfKZIoFpk8y-eRZ4WA4B5DU21dn28fO0hZ1dCCQRWMJyEdF588agaxoz1T8egIJe7T6qAwNflwzxrrAvEXuUoSvUjypyTITW-na6a9fh1EFhVLr3kc15iVjK6pdql56Yc_GzaDGU6U3TR90-gPOaheruvklpTx4uaKyE9mkBkcNyBSNgySztJXYwQ0VU5bX8ckBPTPEsk1E_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت واقعی نفت از ۱۴۰ دلار عبور کرد
🔹
قیمت نقدی نفت خام فورتیز در دریای شمال به بیش از ۱۴۰ دلار در هر بشکه رسید؛ بالاترین سطح از آغاز جنگ علیه ایران.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/696132" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696131">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqPh-x2O97tXEft2KnBMvxgWqtdObPkplHxdZP8cU-Kn0_LogZHbx3F8Pjn9YiDEI1dTf-bnvkDAVp4CZ82Xjfy3IbKOe4Nuv30zcwcTh5UrOwNOzGbc1CHj5OtasfBz4ewAOWFHvuGaQFtH0GCX18mJ0EMCssgMlZZ0w6RXJF_NgZQ47WcSIb5QbsNPj4gieQBB-aggZJd6Z96dTc8EF9Ncmn1sfQd8j3mUmzWs8w8E837AlvFSWq2sT-AAKbLSXkHBj9qgcFNvXEpb-AUlbdBO_7f8B_f6cy8jhR8p8VqZFWV_lRVDUnA3OVDSD04YwieHZ054wWSPNnP_0TPVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع بد ترامپ در نظرسنجی‌های آمریکا
🔹
نتایج نظرسنجی مشترک آسوشیتدپرس و مرکز تحقیقات افکار عمومی آمریکا (NORC) از افزایش نارضایتی عمومی از عملکرد ترامپ حکایت دارد.
🔹
۸۳ درصد آمریکایی‌ها از عملکرد ترامپ در هزینه‌های زندگی ناراضی‌اند؛ ۷۴ درصد نیز درباره عملکرد او در اقتصاد و ۷۲ درصد درباره نحوه مواجهه با ایران ابراز نارضایتی کرده‌اند.
🔹
همچنین ۶۹ درصد معتقدند جنگ ایران ارزش جنگیدن نداشته است و نیمی از آمریکایی‌ها نیز نسبت به افزایش شدید هزینه بنزین ابراز نگرانی کرده‌اند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/696131" target="_blank">📅 16:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696130">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iiigu1I5nLlmzolKVzUrZHU0trth2wo2XUcOT68LRaIOH5GfG5wPzMklrMTK4qP_oNR6kE7NtfcIhjyHIt8ihEae_d8RB8urQqkmsBzwpvbTrds6awYMvhbyt7amhyjOKaGcIsO_FHnhlgJXwvRQnymHSUA9IrlHjOI0j0LeKW5XFiM4dCTcF-yarySLvPBV8PCWygb6J1mbauCV573GVxWJM-nPTPeBVu7LgXJJm2av8ps4cUcACKSzTSEDKVSe8O5_NEYsRWOHZ2Pb9gzCTHLLrMU-3MIHPUGzZk42fH61ayly9WtGqR41XxGJXNLZseLQHL8X0q_BjEkjHPyRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رتبه دوم کنکور هنر: جنگ و قطعی اینترنت باعث شد تمرکزم روی درس خوندن بیشتر بشه. در واقع، دوران جنگ برای من تبدیل شد به نقطه اوج مسیر کنکور و تونستم پیشرفت زیادی داشته باشم!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/696130" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696129">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ed6ebddd.mp4?token=hgzsbqYYdUXPj07gVxcXstfgKj7we7c8v3ddt3XFTXSYdY9Pe_P2kLLzYNxtYsNZDul5Nht-tcQKeFKAD3RBr7yadDlyx-oW1135wYThjn268XL-egaw7J05BHgkE_qZxI7CL83Z5qPNFT_ddRcWEXiNAoRFuAyNlvtiAXeSFSqA-ay5uPOP8IF6DzpAsQmYUqTf187KqGFecmD7Fk3YUIK3-eodG7M4aPutDe6WHmO1B9CGBBEEk-fdawn2U2pPF5lRpBmcrBOIXoivaI_FJI1d3PV8dn5KTWWQsH87DbkrXXQ8ijzLxI8RNt-1j4CZQQStUUAdzJQ6hOzTX0rn0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ed6ebddd.mp4?token=hgzsbqYYdUXPj07gVxcXstfgKj7we7c8v3ddt3XFTXSYdY9Pe_P2kLLzYNxtYsNZDul5Nht-tcQKeFKAD3RBr7yadDlyx-oW1135wYThjn268XL-egaw7J05BHgkE_qZxI7CL83Z5qPNFT_ddRcWEXiNAoRFuAyNlvtiAXeSFSqA-ay5uPOP8IF6DzpAsQmYUqTf187KqGFecmD7Fk3YUIK3-eodG7M4aPutDe6WHmO1B9CGBBEEk-fdawn2U2pPF5lRpBmcrBOIXoivaI_FJI1d3PV8dn5KTWWQsH87DbkrXXQ8ijzLxI8RNt-1j4CZQQStUUAdzJQ6hOzTX0rn0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوخاری؛ یکی از خوراکی‌هایی که می‌تواند روغن زیادی وارد بدن کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/696129" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696128">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgrUiYFNM_8tQuMWlkhD2BiFBveaBqehcJQc-TDRsz54vMQcivGD21tBNOmTBB-tGMgJRjfU3KgaXSFQABV9I-jlHuPBwLXdNFn0dpAU7QOK4c74N8S2g3tTpMr69kTbNUgyT3PycvNZfenwodPjwU25TOfA9WPDOO1C8CL1_TueJBANJEacw7ZUpO7D8NM5hsYBYlgFJO2EYV5DFme-qdwXpkKCP9ZSPlWVD7TLTdwua2wShEms-ZJXjrymED_2HfjY9KftXkr-kskZWs1357Lnuow-0oeF-VTDdC6uUSPkKTOSXLbi9dhZa7GX91zo5WS_u0CfAXLJoReyDsFLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید اعضای کمیسیون اقتصادی مجلس بر نقش‌آفرینی موثر
#بيمه_البرز
در چرخه اقتصادی کشور
در نشستی به میزبانی بیمه البرز و با حضور جمعی از اعضای کمیسیون اقتصادی مجلس شورای اسلامی، نقش کلیدی این شرکت ۶۸ ساله در تقویت اقتصاد ملی، حمایت از بنگاه‌های تولیدی و مدیریت ریسک‌های کشور مورد بررسی و تقدیر قرار گرفت.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5108</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/696128" target="_blank">📅 16:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696127">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a233b1dc22.mp4?token=v0V03yTn6XUOoV2DlQ6lhid5zLH7bdLR2lVb9dh92Ghk3DUu82f3Ah6IZh4nm_TmH057EJcJvILOf5HnWYtxWBX_jbp4GoNBGvH0KUx60rI5VAJONjbXPWoWXpPhsB9Ch89Wu07EI3Epy0dLMlLTVpjZ_zK4RoNIHSntCb5dFesD2L_AD-Ah0Hjh4EL3_rU04EB8gGpl__lzOEnQLp0hVFMaGK_6fKLaFl7Gzy9Z6Ysl15ynJT-tzn1rWpGJK00GBrky_KaDYEHYlJdJeGl-vVYT0qpisXkL5m9Tc1IgSmuzGIxmaysCAsWie2I02teaGlZ48bXnKCb61FZEWtNI_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a233b1dc22.mp4?token=v0V03yTn6XUOoV2DlQ6lhid5zLH7bdLR2lVb9dh92Ghk3DUu82f3Ah6IZh4nm_TmH057EJcJvILOf5HnWYtxWBX_jbp4GoNBGvH0KUx60rI5VAJONjbXPWoWXpPhsB9Ch89Wu07EI3Epy0dLMlLTVpjZ_zK4RoNIHSntCb5dFesD2L_AD-Ah0Hjh4EL3_rU04EB8gGpl__lzOEnQLp0hVFMaGK_6fKLaFl7Gzy9Z6Ysl15ynJT-tzn1rWpGJK00GBrky_KaDYEHYlJdJeGl-vVYT0qpisXkL5m9Tc1IgSmuzGIxmaysCAsWie2I02teaGlZ48bXnKCb61FZEWtNI_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش موشک هسته‌ای فرانسه / ماکرون: بازدارندگی هسته‌ای ما، حافظ امنیت ماست
🔹
این کشور در سال های گذشته از جمله مخالفین استفاده ایران از انرژی صلح آمیز هسته ای بوده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/696127" target="_blank">📅 15:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696126">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV6Hz1gmVJIicz0Gl8vQvN7Q0hj1CqJEEb4r9mRx7ZraFgUURtNURSQtSLOZZ78xAtFEUMFgnX2hYOXPRjtToGuROe0CCgAzSBqbm9jVgbe8zqQqQwCrZDHl4jBFHQB5otyOUBr_pkZZ3wvaTT4ECJDS4W1mX3K4JOIQtcGSXoqZ_2bkm4rjV95gS8WN7JAFnN_GC8zl9xS6M5uXKjUU-3wOO2M06ru6PdovN7EwGjLzD5Tcf04udvfhWbIBZwynspu3O9f8qHZP-X53qDCOM9eF7xFxNsMh25BE9EyBVSSBf3p0YfQt_Q_Y0fMSeTcsgFNsoePxFbm0iB2dXgouGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تجارت دریایی انگلیس: یک نفتکش در تنگهٔ هرمز هدف حملهٔ یک پرتابهٔ ناشناس قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/696126" target="_blank">📅 15:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696125">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMUaQuem2reKDbTRf6h6oKTPyoAC9U2EFQosDuMxPy4b3xs7PjE88nK69rXQXDjOF5B3j7fGdRQh5BNTSoMf95k2l4gUmkPmfXqAJzeMDhWdysxkcYP1jgj5jfCw47oq7uBQPQJ1fgYg5_OJSdTJNYLx2venZ1n1DzSB98yxJafsCEaP8K_ZbkC1i21-Oxm8cvWcl-_uFFRMpSzwHUQNrx46HoMdDjEQw56wtyoZ4pONi7OV-RVVeQtboSm-wm5tP4x80RWul-Vu4jOFxk7OoCpkhqBmkkxggzEym4Kx4N56FoePPi09SLSEK_QmC1xbgBYGTy7oKx7i_HzefgXP-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/696125" target="_blank">📅 15:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696124">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
آخرین وضعیت شهر تعز، دومین شهر مهم کشور یمن
🔹
نیروهای انصار الله به رنگ سبز، نیروهای وابسته به عربستان به رنگ قرمز می باشند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/696124" target="_blank">📅 15:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696123">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2a0596e7b.mp4?token=d3klCwRXKcnA5cNMNMN7_ybpHrD8WInx72bVvLNALbatkyqRv1yyrMWn9WApJo8dqtVcyhVsEAL2Fbk0gupSjta6wj8ly8Fr-pIo668AS3KfJU_RpoT9R1JEvfgmYbjqlHpzsdIb07H5aRyJKVFFW0G5fQ0zbgF8IFD-ej3Z08hX0xHgSdnZcAEYgSpZCZPjV50JVDUVEnLsPGlVzhK9q5_cpxcp4r2uA8UCYDfoO7msysJcJkDSQohmOJNn28SSo_bi2BB4XgVbusXMXKAwrVodb24DJ-f7Y61OujjxPuLhMunmPn9DdzYCdxOj2ZUL0jd3czwnhXoIt5nGnziq-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2a0596e7b.mp4?token=d3klCwRXKcnA5cNMNMN7_ybpHrD8WInx72bVvLNALbatkyqRv1yyrMWn9WApJo8dqtVcyhVsEAL2Fbk0gupSjta6wj8ly8Fr-pIo668AS3KfJU_RpoT9R1JEvfgmYbjqlHpzsdIb07H5aRyJKVFFW0G5fQ0zbgF8IFD-ej3Z08hX0xHgSdnZcAEYgSpZCZPjV50JVDUVEnLsPGlVzhK9q5_cpxcp4r2uA8UCYDfoO7msysJcJkDSQohmOJNn28SSo_bi2BB4XgVbusXMXKAwrVodb24DJ-f7Y61OujjxPuLhMunmPn9DdzYCdxOj2ZUL0jd3czwnhXoIt5nGnziq-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند نکته آشپزی که به کارت میاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696123" target="_blank">📅 15:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696113">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trQpuvh5H2Y2pokERyAbW6Rgvo8XmM6JW_-ffQrwXARfjp6XtGCzV6WFtkLJyatwVDIKwwEdTJUqzzn6mKRDZDXEt9kovHg0FC4tWZaihn4FkGI82pZ79cnkpMHeGx9PFnpESYrZJf9VvcsiPrcjzEHjrHv0cioqTUuZq3Wtc1oMNKB6EUoEslBPDdkvKs1DRKh1E7XieK-UwLr3u9Z3rmo5pnG7trmiRYoJtlmB636FQ7h6FgCeJd2XAZ-DIoMJnx9ZAiXlFHuIJ3Aye9DlrynbhWJmaVNL4bPYm1sZtqzNdfN57Pd-9kTK6xRrzgxr7J_Ad5zoRn2vkXatV_Sk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyUSjBB5OnVj6_MLAqR0gHDu1d73JkytNerUqifFg_V-o32mApgJPvR5nGIUYFidnSswGU-u8iAJz0GZgUM7cGbVmihhqrd90bsB0_9rrFj0HtyPfGoPd_YFNsIckzR-h_BTrFTwlP2xkymoE-EQH3m_nf8ZuLEqteScHvVzedGcI7NWbf6yd4VA9NGGEmAgB4nbe7Ki9Wlpxvo0V5h3Cpow2JdlnfiFTX7kdfQGPFOT3y6JjTKTJQU6fD1PzkTrkKUyg-YMQTZByQ-ars19BRPvVrmKNDbPTZnZ4qNbdlRYqpnm44MY-AQuvx3NtZ6jSvqgX3yXCCpuxSCEs9ohGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/US0rfheh-4J86C7W-Z40hIiZpV51QhbVV8lliJtZTO7X9nZMBgjXftfBP_AYIxibOW-qa9eKgDSE8QKV2etmPEy4F_r5coEbXn5dSm6Smg_Uz7tLfs_uMUtFhPVzy9pBa33LQIZxA2XRkgQwLsp946PsjPdfgLE8IjATYaDcwgmdaA6AsJeLs-JIMUKmW8r0-Z36dEl6FOhkQhl6c0wQnrVjHrEdDDbkIxNc1Ach3HpiqbDhWHHgbdlUHJwMdCaTLy6N0-wxz5QWDa5gfk93eiVg3PQ3PWtzGak6aqtgdAmi9cDz62B5zT3j15oEkZGcKdhFPynOiAXA2wg0R_MQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raUPzLL5PkdUEO6JkQkQqGAX8nq0UD_pPAdUrP2bFiPbEO1un3xM0rH9OnTDnfJym6SUYxXRTnaJlzB3ZLC7enQRRqV3vvfyc9Hr0GnejrOeLzB07hIPuEaWyQTG_FmRXddZet1-PHltDe3gGAFB0sbl62G6u6MQ7FMqKr7coAO3gk7YGOHYh3KiKR8TkcCpFB_GD2htK-ch3LEqI3oD77KlcRNiUyB_xxnUCvMd3ClSpbHv36KXqctxoF3KSKJnemTr9LvGZqO8hwDUbtB_ccIdGvLp5ZCoNTlTCqycYHIrS5QVD10p-JrFzn2CWK4S3nJ8fvXemoc34xHmtSJOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjPYbTsvZP7Ij1EvgZrGXvRNKgcQwleqJj1TjBzA0DpPiKmiiJp-NVEM0HPt1-a78JIlXveqobEKVvbmBlZxpD8p1guLFtWzgE3P4OzCGXr9lBHXpBEoIQMTUcVWcm3lAfiN7mYRdU04rnTgbMvWsOcZ_3QAgqmVnB-YaXDnWTjgUewIFoBz2MzuEwm3RALPxSJNENAwt57estnjFjNN7lIup_-3blEvJ1hybnViJq7uLuLUcAdjHJp-brmo6V9tzZh-rL83wVmPvfm80r3T0rvtQ9NIk0TKvhSFsv2ElvkUFQzzS2xljhpKbHS0yRuF9u2fRg3wRRcqs43cG6yT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bi_LOIOIu0dmxD2Lhz3MKv3zip0B_gdDyjWlLZXTpWgD6GIcLjMi995R8oTqB7rC9IYmqLySFS2awHVUCKb0IvWQMZdICSwqG_yHPzc5m5COdckgARn7K5g0GeDdCmxSCdvTsc6i0ISk7C5T9k0_IfX3HzzbUHm2zsK1Kmgvq2A0RQcEeCRywyu1jMutkZUDLvnNTYcoDpAwFyIblcJjSBNKIdI_Xe0O5b7ND9Q9Ts-M3BUNohThDc3Dn4Y3BUtTbgYIf4pDCob1QmKiAvgLh9tW2lT6gIk0XIIhQrGKU9FdywX97uBUpXFYNd3PlHrR01CEZ_ruW4TdZPPojH1fYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgWEmOsp1y1We-kdk4tR_dabK90HxIU2DjbHxLNlKm4jReM3ZxBPz-lws6G0mPQ-PbnKyBnIR2ICWabUCw0qD5q8RcHxfkSbyUiSMBTLhl6PJuyEel24zymsBywpphYKcGBXFrdE89sUBbf6oS3RD9F87JaEFlLawjzEzDrj9wkTkC-hWbZd_q2HfFPU7WpoB10PWL1HVmyJwN4DnTqWTCOgK61x9y8MTrFMw1dLfUPbWCEtyNzzPtj38ZYCFT0-A_xGCsudV57PeQLipAl_bD8agc2pCAMJRFZNBwBuimXkby9nnMJf6dVivbKt9IGOLoTE9l_JnjTwhlWXk-A-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sip0nLsxfRY-8o1_Ry5iTPMtXRtr48TLThn6nHWOd1aPTiCPfI0HYzXy5RMI5VvLqsTo3_cjFAHug0qDdBWqeakYVJztVvmPQ7qxJZv-EhEmdDkZxM119lcDJ6e6o-PKPd2A-bG7chtuBI-nF_X3YMSW_Mons0ONtNmlS1y2I8RjVUE0D4qbpUxDknd31cav1NNP6UZHdoATyLcaFzas5qUmTi7GSiJHB8EIS05XCrTyjzr9t97TnX_R0kIuGhPw_3m8es8P6E7EyNQGSjPxnG1ifj4wTEA4G-aH7FQNcqLNC6MWsNNVzPNQ5qTJQ_HCIpaVkCOqz5A7JYszcB7GBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSD2Hl44vI1CxcnIJ2aeXTJrsWaJ9c0rcAKPwV3kwOXjTGlSveMUFnoU0bSTwD0PhAHUcDAd6JYXPYFExjTVE4BV2vCub-R_3G8DDWkhz9mm9vQXlbCS9iM4gUxiHrQye5a3Vq_hItlBXog_bQLAyqjC2WQaDzFUItYJAbTtsnXt1fRkMDjy0RYaWD-xZcsNZuWd5HxUqR5ePBGIARMHxJu6-m4IWJMsXzxpeRqFf1eWnPyQitFbZrph5MI-bB1QOcTDfaRplZOwPi9tDeOrDzHI2_B_oubpsfv7z0cdBwDjeGlFw-5rIA-J4BFV46nOHwM2fERiee4f2qC-E0aduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpnEyK1e4NoDlOUm3IwR6CKTZxYGpd12xGm_Q5RAVn1jRwh5tfLhCTi7QvijDI1aCucrVd_SPngGwBJqKG9CNlDXw9daGESNU36jk9ZzJ67FOQ1AiOIepcAgtVykPh-jS2myn9q89WGHFUj73wyvyp7rovZOOGsvHW8WsXReqTFbwVIZ6_IKwE80uFILvnQm7xboJVIAR7lcMYZ_dfK4Wkhko8d5-p1BXDCDajwl-T3M6d3Fxq-Xl8MUKuF4iH56-s8_VjEbakx7BQ0PxZEg-hepsnyaJbJzcacXDsRVs8V5x2CDcVVtA3XsEh09qZ9PFoOS4E3I5LQCS4Y33lXMRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از بزرگترین زنجیره انسانی جان فدایان مشهدی
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696113" target="_blank">📅 15:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696112">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
عارف: ما به هیچ‌وجه نگران تحریم‌ها نیستیم، زیرا کشور در برابر تحریم‌ها آب‌دیده شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696112" target="_blank">📅 15:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696111">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: اهداف ما برای ضربه‌زدن به دشمن مشخص شده است
🔹
همکاری‌های دفاعی ایران با روسیه و چین متوقف یا کاهش نیافته و در برخی زمینه‌ها تقویت شده و ادامه دارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/696111" target="_blank">📅 15:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696110">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGxhBoW8Y76o0k-Ma7U-Y3TlvtMgAXWRmKEuLCvaOBOiy7Otum6JXfeej9qEVak3Wbx_6xs1YR3ojdEPQi1i_q5uVN36oozU5U78DoEfSPXSlvv7oxMbx4FG0odhdToGXBdtLf6UShhdYccuwkLXhNo9W_BszaBrqG0AGSTGBJmnoz9Or32RQlyq_kfEksOqlR3gYWiaBNgGvhFDTyX47HDyRHXhVmdB3YWArmHuTpwsyWLoB0lHRRZ_JxNJ8iSk6DmHjTPE82UsM7RnvS6qNKbSb3JYZp3Xs_2FJcoVhKmAZHqURcvSKU-5ldykQLu_a8MsSext0xHnnxEk6qfdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برند اکتیدنت در کنار دانش‌آموزان رباط‌کریم
اکتیدنت در قالب برنامه مسئولیت اجتماعی خود و با همراهی خیریه نوید طلوع احسان، مهمان یک مدرسه درمنطقه رباط‌کریم شد.
در این برنامه، دانش‌آموزان با حضوردندان‌پزشک، با نکات مهم بهداشت دهان و دندان آشنا شدند و در کنار آموزش، ساعاتی را به بازی و فعالیت‌های شاد سپری کردند. در پایان نیز هدایایی به دانش‌آموزان اهدا شد.
📷
اما این فقط بخشی از این روز بود...
روایت کامل این برنامه را در اینستاگرام اکتیدنت ببینید:
🔗
لینک اینستاگرام</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/696110" target="_blank">📅 15:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696109">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d30c47a03b.mp4?token=HcTgLdnIfgDdpnebpxar2cZmN94lstcQtP5mn3xFy_D0uKIcn0Z4b-dU3ZI2SGhuFqnJ2xSlv6rim7dlYWfm27zZhTlvOMZJs9GcxQBSsdSXZ_jHOYJiUEbCYEPYFbz-3SBc6BkwY4zKJjZ79zeBsUGnPEFDlb8qoqhVlE_NwEJ7dkbY3nFExXTV88j_HHmId2CxIKHEgLvy_wqnXZMgz1G-wiiTJwvhlmmrXBIvs9Sfu8B7A7PgK3MzwCNiuJhuNnwYDhA8JlbjfHwGtS1U6cHy_VjJsQ9zrRIesNGKgD0zuMTCy0yZe4Usx_W6JmOL69TfYcv_irDdZZWTGpAGBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d30c47a03b.mp4?token=HcTgLdnIfgDdpnebpxar2cZmN94lstcQtP5mn3xFy_D0uKIcn0Z4b-dU3ZI2SGhuFqnJ2xSlv6rim7dlYWfm27zZhTlvOMZJs9GcxQBSsdSXZ_jHOYJiUEbCYEPYFbz-3SBc6BkwY4zKJjZ79zeBsUGnPEFDlb8qoqhVlE_NwEJ7dkbY3nFExXTV88j_HHmId2CxIKHEgLvy_wqnXZMgz1G-wiiTJwvhlmmrXBIvs9Sfu8B7A7PgK3MzwCNiuJhuNnwYDhA8JlbjfHwGtS1U6cHy_VjJsQ9zrRIesNGKgD0zuMTCy0yZe4Usx_W6JmOL69TfYcv_irDdZZWTGpAGBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی شیشه می‌ره زیر پوست، واقعا وارد جریان خون می‌شه و رگ‌ها رو پاره میکنه؟ #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/696109" target="_blank">📅 15:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696108">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6b2a493d8c.mp4?token=qS8brR-KQeeqE9rvQheF3b2rfJ_32q-IJpAjGYGkAl31ulnlpUsi0W0jonVTC6WvjI-YJGR04SCp8_iC4Cgbd13sncR3BszJKHMIWsJ7A_AXeq90nWAvaQeT2cfuOUeK3ycqPKcoyOZts2NfqxkfEkkkJ_28bSpjiUXXsa4MDdc1mysBoZEgd8PC-bZv5dCF6ToFF6TCvXo5OygM0mNZynuDaePI2zhz1uvohu1g3g_eIM8FH8thYz6JdL-GWRm-CIQ3JLdYLMwc6aqMLnKUXJU-ngQ7HvpQZqqx4hrctYi73TOwAu95njcaD6uR7YHRo5bzdCN0qvDTMcbaPeC9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6b2a493d8c.mp4?token=qS8brR-KQeeqE9rvQheF3b2rfJ_32q-IJpAjGYGkAl31ulnlpUsi0W0jonVTC6WvjI-YJGR04SCp8_iC4Cgbd13sncR3BszJKHMIWsJ7A_AXeq90nWAvaQeT2cfuOUeK3ycqPKcoyOZts2NfqxkfEkkkJ_28bSpjiUXXsa4MDdc1mysBoZEgd8PC-bZv5dCF6ToFF6TCvXo5OygM0mNZynuDaePI2zhz1uvohu1g3g_eIM8FH8thYz6JdL-GWRm-CIQ3JLdYLMwc6aqMLnKUXJU-ngQ7HvpQZqqx4hrctYi73TOwAu95njcaD6uR7YHRo5bzdCN0qvDTMcbaPeC9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس رشوه ۲ میلیاردی را رد کرد
🔹
یزدان بشیری پلیس قهرمانی که با کشف ۱۵ کیلو طلا، قاچاقچیان را دستگیر و تحویل قانون داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/696108" target="_blank">📅 14:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696107">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f593bc51c3.mp4?token=mTciq2sE67SawmfW80GO-757xtGFovxN6rW6UBIEkoA6t4Qn-HOUvrqAJnhZm82l448ytv0BJ8HCA5YBTgtBn9IL7mYPCjrEmT6_C1P--CszXzHEUrVGBk4TtMkSIoBDGNfoQhrUqTy3CH3pmqdcphlwJq-ONm6Th4iibhqg96ruKRNtc8ItxzoM0Mc6OxEQGhTe69YtLXBe7hYyebG3Nq9IBaQ-5cmqUDewdjWhmb7agV8yVEaPtVb44Xo4SUHA-cI3hij6Jv9zWlQr72zc6Pq4OnMlDkEXJXcUvPhZBsIB3Jajm70y0FA2HDggXsvbybQKWuvWFAMOV4JurTj7bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f593bc51c3.mp4?token=mTciq2sE67SawmfW80GO-757xtGFovxN6rW6UBIEkoA6t4Qn-HOUvrqAJnhZm82l448ytv0BJ8HCA5YBTgtBn9IL7mYPCjrEmT6_C1P--CszXzHEUrVGBk4TtMkSIoBDGNfoQhrUqTy3CH3pmqdcphlwJq-ONm6Th4iibhqg96ruKRNtc8ItxzoM0Mc6OxEQGhTe69YtLXBe7hYyebG3Nq9IBaQ-5cmqUDewdjWhmb7agV8yVEaPtVb44Xo4SUHA-cI3hij6Jv9zWlQr72zc6Pq4OnMlDkEXJXcUvPhZBsIB3Jajm70y0FA2HDggXsvbybQKWuvWFAMOV4JurTj7bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاسر سلیمانی، نماینده مجلس: در تاریخ ثبت خواهد شد که ۸ ماه، مجلس یک کشوری تعطیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/696107" target="_blank">📅 14:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23c356164.mp4?token=E9IM0gn09W1qUeoZXlHyyPNw7JzhCmNpyKAAeZuLesCxpxU3r5pHI_TTWkrVdGPDe05bjWlZzFvoxhysctMrtw1T3TprZGq_FK6rdpxojK7V7QwdL0eRfNOrBxvPjMKW9Pxxzh5co8Lm-TTg78msF8bNU9FoTrE-ghYWaLHo9N2lX24Sm9G1exsdDhMLCRKHD9Z1TVqE7d24e7h6XvtRV1gH7nTkF2CKfQFC-FVnNYF1V1YZ99EjtJXtFT_lZz-UUhQKrMNPNm0roAr_eig0K0DQ4DVVheqmNgEQ11kM5BrqO9Hkjg0bxCNMCFckhqsAJACWwJSU7G2I13kKi2GY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23c356164.mp4?token=E9IM0gn09W1qUeoZXlHyyPNw7JzhCmNpyKAAeZuLesCxpxU3r5pHI_TTWkrVdGPDe05bjWlZzFvoxhysctMrtw1T3TprZGq_FK6rdpxojK7V7QwdL0eRfNOrBxvPjMKW9Pxxzh5co8Lm-TTg78msF8bNU9FoTrE-ghYWaLHo9N2lX24Sm9G1exsdDhMLCRKHD9Z1TVqE7d24e7h6XvtRV1gH7nTkF2CKfQFC-FVnNYF1V1YZ99EjtJXtFT_lZz-UUhQKrMNPNm0roAr_eig0K0DQ4DVVheqmNgEQ11kM5BrqO9Hkjg0bxCNMCFckhqsAJACWwJSU7G2I13kKi2GY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تومار دانشجویان و استادان مشهدی در اعلام آمادگی برای دفاع از ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/696105" target="_blank">📅 14:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696104">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای روزنامه عبری «معاریو»: برآوردهای قطعی نظامی حاکی از آن است که رژیم صهیونیستی در آستانه انجام یک عملیات نظامی در یکی از جبهه‌های منطقه قرار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/696104" target="_blank">📅 14:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696103">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
در فرانسه به خاطر اعتراضات دانش‌آموزی اینترنت را قطع کردند، نت ملی هم ندارند، حالا سیستم بانکی هم قطع شده و مردم نمی‌توانند با کارت خرید کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/696103" target="_blank">📅 14:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696102">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: ظرفیت تولید تسلیحات کشور نسبت به پیش از جنگ تحمیلی اخیر ۲.۵ برابر شده و در برخی تسلیحات، تولید بیش از ۳ برابر افزایش داشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/696102" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696101">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311d9d7cf3.mp4?token=cCQzDmK-PeyHhQPJBLoP35JMZbJ4hipuc9oi5Qp8nwfnC2h0ZTQrWapr9CsLdUr1WzP63oSCtv0YnpmlRTXY3q9tniYVRjLtj7lAJCKaJNrnD5JdQD3kXUO3cz04rLkU4GpG-MvoDzxnAj4E-Tmx2vO-qbO9ac5AooIsUVgHm3fXQRK-_ixIkg60eg7prxrWk8Q9249-B5cCgf8ovP27Bq6nFHzW_LISMuwxj7lARgqzUNeuHfLbg7bDsgoS_E_iI7Vf0xWcFuJXj_7uzGXviYaKngbzbaZoE4vkJwARqMjt9X2WaDNjThrZHxShFXKpmE5KIFxOejGnnLepEpzWfDeATNiZGyZkawEBVoOyTigXUkl073eHBa37eanKVoXKOlVkqYhyySu_An5E5Dc2OqCkRyOaXNUotnAkSXP4xMLP3A7RDELP1o3z3Nox6R2zg08_0So8Dg-P_XGyOKsPDi3QYRFSkERcyAgzcTKN5VfgjxL1x5c6_j67E6blB2OubiyF09lflPNjC3h9mzWRMGU221u5ODq8Hw3kq953huBPAwbloyx173gSewUPTqJt9W93Ryy7rTPCJOpxV0WkbjllylKWqAh4MRh33KcYegEjdnwqBMrR768522nKeCaBvcUFT5NZyoNcPG5KBHwhEjXSr9kwsa-MNpvytgtYLCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311d9d7cf3.mp4?token=cCQzDmK-PeyHhQPJBLoP35JMZbJ4hipuc9oi5Qp8nwfnC2h0ZTQrWapr9CsLdUr1WzP63oSCtv0YnpmlRTXY3q9tniYVRjLtj7lAJCKaJNrnD5JdQD3kXUO3cz04rLkU4GpG-MvoDzxnAj4E-Tmx2vO-qbO9ac5AooIsUVgHm3fXQRK-_ixIkg60eg7prxrWk8Q9249-B5cCgf8ovP27Bq6nFHzW_LISMuwxj7lARgqzUNeuHfLbg7bDsgoS_E_iI7Vf0xWcFuJXj_7uzGXviYaKngbzbaZoE4vkJwARqMjt9X2WaDNjThrZHxShFXKpmE5KIFxOejGnnLepEpzWfDeATNiZGyZkawEBVoOyTigXUkl073eHBa37eanKVoXKOlVkqYhyySu_An5E5Dc2OqCkRyOaXNUotnAkSXP4xMLP3A7RDELP1o3z3Nox6R2zg08_0So8Dg-P_XGyOKsPDi3QYRFSkERcyAgzcTKN5VfgjxL1x5c6_j67E6blB2OubiyF09lflPNjC3h9mzWRMGU221u5ODq8Hw3kq953huBPAwbloyx173gSewUPTqJt9W93Ryy7rTPCJOpxV0WkbjllylKWqAh4MRh33KcYegEjdnwqBMrR768522nKeCaBvcUFT5NZyoNcPG5KBHwhEjXSr9kwsa-MNpvytgtYLCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدرت‌نمایی نسل جدید هوش مصنوعی
🔹
هوش مصنوعی هر روز یه قدم جلوتر می‌ره، از مدل‌هایی که  از مرزهای امنیتی عبور می‌کنن تا دستیارهایی که می‌تونن خیلی از کارها رو مستقل انجام بدن.
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/696101" target="_blank">📅 14:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696100">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667dc38fa6.mp4?token=hT5_wlTrEsuCSbhZjctSkZRWB61YFrn223snWIs1d64-YH8gmqIrRZBZbdv26KC73obf4sn3T88VE8uo2zIXpSxeCiJWNRb8hu5Au1-aEjQXuD6BSt34iYnHQWw1Y7pOxl_Zclwp1ZpUL47EcZoRUv-0MV9hsvexBhKyrbEy5jol5NopUa9NHJw685TbTsJaSwxWswnpmna1NvD2uazo2ajq_Z8nZfKGLplnHIWKLdUcGKwBd4oM7BraYikVTIz3Et6hojtzl2dE5eq-etGCwsy8GR4bT0gqjfF5bTMsvxCRDz8BP7YnNLYbAnq-X39UAuVeoEt947QpN8vVt4UEiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667dc38fa6.mp4?token=hT5_wlTrEsuCSbhZjctSkZRWB61YFrn223snWIs1d64-YH8gmqIrRZBZbdv26KC73obf4sn3T88VE8uo2zIXpSxeCiJWNRb8hu5Au1-aEjQXuD6BSt34iYnHQWw1Y7pOxl_Zclwp1ZpUL47EcZoRUv-0MV9hsvexBhKyrbEy5jol5NopUa9NHJw685TbTsJaSwxWswnpmna1NvD2uazo2ajq_Z8nZfKGLplnHIWKLdUcGKwBd4oM7BraYikVTIz3Et6hojtzl2dE5eq-etGCwsy8GR4bT0gqjfF5bTMsvxCRDz8BP7YnNLYbAnq-X39UAuVeoEt947QpN8vVt4UEiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا
عطر با ادکلن تفاوت دارد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/696100" target="_blank">📅 14:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2dbjUpNzFfE2n1PIeW7RsUnO_3Y0H9X4OyhIqaUmD9Qog_bkFRbJ7REe9ipn6RKfYNHLMn2z3ptPSalNvC22f1DPl-r11cPOKEvlJN2nADZBA0IXf1wL9Xt4nG5tIlTgGdXXFWcZokzqDL_494OUnUg-KMftlMPQt3ZVQXknLkJwB_oNDGGPkyuFEBVif10L7l_NZpFIIEJyzt9tovSe64S1uk5H4ZGQymgmg3ypzaEsDAjeBtm17Cfs5ZzS8aEHQnze0eeOS8dcDJ-C4YNXhc-p0199s45IotCS5T7-7D2p52YfeZR0eA8BER1en7DJqjYuNCBmbczxhkM0CRL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شعارنویسی‌ها به خانه ایمان صفا رسید!
🔹
بعد از رضا کیانیان و تهمینه میلانی، حالا جریان شعارنویسی به دیوار خانه‌ی ایمان صفا رسید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696099" target="_blank">📅 14:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696097">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv2n0CmptaWjjBDFSOXCjSW8Jk4nKuTMSUN7Bx1e7iEMasRcE9_sV-AeTiLlnk4jEKpJ2UBgena4uH2TVwGKuTGSX6nf1Jd3yEzcAq_yHKf2Q42oJnGe45C9kWh4Yfz6rXw_GwlNq46m3gYoAbtjXz8RxqLVYuuJcupZkEZZeMkDF9yAk8D9LiSxoXvkY8BqEooc2qLeR9fk5_uzXvGaA9mCiLtTxi5Wacz-jSQhPErirOrXLX-HbP32HnnQ440mXEJXG3t2gAaqJJklr9yGWXOEUeV8glP7PpT-AakbEDVzFbZ3qiIY4ZqmVik11FqosBDjAdZL4unxF4kzmML7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910e633a10.mp4?token=BSrojcbbf_LwralB52Dzs75UQOJkRSleGQtljMfIFg7DRKy-eXzZ4vWJ1xmEJnGgCIpUBn7fwLajzrEQ5a4HYIvRyW7fazqTcBt7ooAPudf3aSkOMvnEHkdDU7ui-HQzjvo9ByrLxVL91IA7Az4bOZ68VVSSxYIFsDZNvePaWUcAlNl_bie4m1jUGXj1g8ZBYeC4azqPC4kEwxQHrpbZMtOtp7W9YHK3nnvxlwpLfBKuvg7RMaMCxpfqbE5-WSfUAv49jh6rY8_ZY_ntt1RuweoNY2Zjz5BfJDRxyptsaZ0tkHs3RRI6b-q7ID6ehS4LMO9sdfbkoCtpwEQZlf1okA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910e633a10.mp4?token=BSrojcbbf_LwralB52Dzs75UQOJkRSleGQtljMfIFg7DRKy-eXzZ4vWJ1xmEJnGgCIpUBn7fwLajzrEQ5a4HYIvRyW7fazqTcBt7ooAPudf3aSkOMvnEHkdDU7ui-HQzjvo9ByrLxVL91IA7Az4bOZ68VVSSxYIFsDZNvePaWUcAlNl_bie4m1jUGXj1g8ZBYeC4azqPC4kEwxQHrpbZMtOtp7W9YHK3nnvxlwpLfBKuvg7RMaMCxpfqbE5-WSfUAv49jh6rY8_ZY_ntt1RuweoNY2Zjz5BfJDRxyptsaZ0tkHs3RRI6b-q7ID6ehS4LMO9sdfbkoCtpwEQZlf1okA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طعنه سفارت ایران به ترامپ در روز جهانی «فلج مغزی»
سفارت ایران در زیمبابوه در پیامی در صفحه خود در ایکس:
🔹
۶ اکتبر؛ روز جهانی فلج مغزی. برای همه بیماران مبتلا به فلج مغزی، از جمله ترامپ، آرزوی سلامتی داریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696097" target="_blank">📅 14:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696096">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7946363a9c.mp4?token=vcdpCS0vlQ6McLbkaTVtVBHe9PurnPDgVFJ5RZUrBz-UOAeu98cTq_2hdxql40tYoKI1K4bW_spegUwBO73mhUuGb9EkBf1rDBjXmzGIwVfv4ZvUGW8w9VefsSiXFcvE_RK_Xotl9C4NR6_tf1qHJfeq_cv8whnUxQFTUNrhf6GtfHtI9sAi_kVb18-Q-T2HuN4hmBO5rckBjjoVtQVOYp9Z0ixOGFKmj5XMQOZmy7zOSe5LtvaTFB72HGwd3PHxUhjcbrnkJc0QtSb5amTHoyTG8EH4qG5udm1TVrfK5YJkX7RTM-em444034i_J9xJFCnutD3o94ZaEm6u3FjkM6mBGFH_SKUZl52hm-X-NFWsq4JMRRDxHUWr1pz2Y6dX8Nt7TDquQTUBy9JwWe2nz15yjLIqPZrDIyz8BVqPcUNRA3SH2MCBWc2bb5ampmmA0EnnUQzKQRo9bMPkmIz9Nge0HFcEzZ6TtjCSWXFE4BlwUVvWDvSlnQEMrqHVXjATcYfT6NQ7IsEJGRNqESQlgazYl8fMjven9u2q0-qm_iIZFtTvIJQhCnYwwojnNnF6zhQEWKER-qwGv7SpPoHqlkX1ki2FG4yAjpvkshDm7RW0zGYzmknYopu1gPxY4JB3HAMET6xf5gaSLEJFvaA6ohVdHKozvUvZH-32WP435l8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7946363a9c.mp4?token=vcdpCS0vlQ6McLbkaTVtVBHe9PurnPDgVFJ5RZUrBz-UOAeu98cTq_2hdxql40tYoKI1K4bW_spegUwBO73mhUuGb9EkBf1rDBjXmzGIwVfv4ZvUGW8w9VefsSiXFcvE_RK_Xotl9C4NR6_tf1qHJfeq_cv8whnUxQFTUNrhf6GtfHtI9sAi_kVb18-Q-T2HuN4hmBO5rckBjjoVtQVOYp9Z0ixOGFKmj5XMQOZmy7zOSe5LtvaTFB72HGwd3PHxUhjcbrnkJc0QtSb5amTHoyTG8EH4qG5udm1TVrfK5YJkX7RTM-em444034i_J9xJFCnutD3o94ZaEm6u3FjkM6mBGFH_SKUZl52hm-X-NFWsq4JMRRDxHUWr1pz2Y6dX8Nt7TDquQTUBy9JwWe2nz15yjLIqPZrDIyz8BVqPcUNRA3SH2MCBWc2bb5ampmmA0EnnUQzKQRo9bMPkmIz9Nge0HFcEzZ6TtjCSWXFE4BlwUVvWDvSlnQEMrqHVXjATcYfT6NQ7IsEJGRNqESQlgazYl8fMjven9u2q0-qm_iIZFtTvIJQhCnYwwojnNnF6zhQEWKER-qwGv7SpPoHqlkX1ki2FG4yAjpvkshDm7RW0zGYzmknYopu1gPxY4JB3HAMET6xf5gaSLEJFvaA6ohVdHKozvUvZH-32WP435l8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری سابق صداوسیما: یک خانم تزئیناتی سفره عقد، یهویی شد سردبیر برنامه تلویزیونی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/696096" target="_blank">📅 14:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696095">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f46eebc4.mp4?token=aJpohdAMRhCN7b7o55XGo4Ma3hsbwjWDMlWCfdfoCE5_BhUZQJkbdZ-HwPne0HXt7fMk6xXC8rXdWbiiL611oDc6U-3H6biQkc_CDLCSY02Ym48trQ4i8-uUrmdrmzBTq3SbmXk89VXEV7NDfnZkq_r_vxt_7aBkvoZK8opotf7SB5kmCunZvy8hAaWFXCBqCh5tQERwhBS-EEduKVGxoBHOTzsAazopUVqZkPcIXx0ScU33TzsmFXYGmIsk-03zxH90XQG1L8p1MRCQAmrhZ6cE-XlPleI6nZKZkfGru7Avb2r50hwBiaytst6SC8V7xUdwDRsPLgz9jDHu0QxoWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f46eebc4.mp4?token=aJpohdAMRhCN7b7o55XGo4Ma3hsbwjWDMlWCfdfoCE5_BhUZQJkbdZ-HwPne0HXt7fMk6xXC8rXdWbiiL611oDc6U-3H6biQkc_CDLCSY02Ym48trQ4i8-uUrmdrmzBTq3SbmXk89VXEV7NDfnZkq_r_vxt_7aBkvoZK8opotf7SB5kmCunZvy8hAaWFXCBqCh5tQERwhBS-EEduKVGxoBHOTzsAazopUVqZkPcIXx0ScU33TzsmFXYGmIsk-03zxH90XQG1L8p1MRCQAmrhZ6cE-XlPleI6nZKZkfGru7Avb2r50hwBiaytst6SC8V7xUdwDRsPLgz9jDHu0QxoWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو پارلمان اسپانیا  به فرماندار مادرید: آیا فکر می‌کنید مادران ۱۶۰ کودک، از ترامپ برای کشتن دخترانشان تشکر می‌کنند؟
🔹
علینژاد: من خبر دارم خانواده‌های داغدار به من گفتند از این که بچه‌هاشون در بمباران کشته بشوند خوشحال‌ترند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/696095" target="_blank">📅 14:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696094">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c7bafe0d.mp4?token=AL5bKqIwpZGfJXIPr1gWk8vT3q8FSH_aI3mcaD3OudrI0ODT7UAsXNr7NgCRo-JjG-hK0WedlH9wdX7zQPCafKZ-Hpk5auVsCLMqrmVJoC6gpouaD6IyXbi45mgxW6THhO0EgQ6G-P_a6MqZWjKDFkECVOGM0atrBU5nUe-8f_pgCXATwhP6qxhJZAfUy-4Mdecw-zDgN0LHgTK77MjZeNlUSvfKtLh0cElVhkZORderbOHEARwT_XIIWBlEEZbqKQBSP4cGV69KFPIJWNrlTg67ZHojPaohTqvRh63gTWe63oijNXYL7FEtC-KAnLbcYvpbK6_-orYVQHZ4Jou1mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c7bafe0d.mp4?token=AL5bKqIwpZGfJXIPr1gWk8vT3q8FSH_aI3mcaD3OudrI0ODT7UAsXNr7NgCRo-JjG-hK0WedlH9wdX7zQPCafKZ-Hpk5auVsCLMqrmVJoC6gpouaD6IyXbi45mgxW6THhO0EgQ6G-P_a6MqZWjKDFkECVOGM0atrBU5nUe-8f_pgCXATwhP6qxhJZAfUy-4Mdecw-zDgN0LHgTK77MjZeNlUSvfKtLh0cElVhkZORderbOHEARwT_XIIWBlEEZbqKQBSP4cGV69KFPIJWNrlTg67ZHojPaohTqvRh63gTWe63oijNXYL7FEtC-KAnLbcYvpbK6_-orYVQHZ4Jou1mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعد از نشستن طولانی، زانوها درد می‌گیرند؟ علت و حرکات اصلاحی را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696094" target="_blank">📅 14:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696088">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2nD_eCDrb4DthQy_be83zVkeRlHsLa1rx1bYQI5UzQ48umugHvab4-_wmySaUhhm0pIJQDALKtszu4Pj05d72aW7QfYorVxya-6ai5-3ney0D_enbbHnBElx0SbDqDnQ3VpZesccqx-peXN54r1nJM0zTNMAYPPPCm0D_SSH1PGDxgPm8IcjGJtSkqA-G_S-3VnVylUtnFOZuxtRLqyFnQgmTY2Oj1rb5oB2TPjAvZpQMvQ-FUKRc9n0LDrqhx4FaivjafBCLDxxtyrs7Ay-O_XmYSCj2MXglSjuXl2C4DxuKAgZ7tUiRQgml6QIdhPW76SCLtHq7kXeo4kdUQr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrObYy5-XZuALnOzNhxRkttXQamMCEMD7X4j9wy69q37eiVeCh6ySx2eEtprS3pxq5lrtCsWf2e-Bc7pycuVQm7R9-rUgutvkJBGM98rx-22sfmjspy1XDBoI8pN9V5jpKhQqq5a1CYwlWzz3QAHPxdSrElfB_Fl9Fx8Au6brUDJd-_0ZXr7ObZNRxwr4Azv0JJp4S7eXRxBHSq6Z7sg8c6KiKm_vEll7mzRFjI4-TpRl7T-6vKoem-gt_Qp9a3aD2TpkKnZVbVml-pa2xBVWG8eXqFFSG-YbNYeqDU5Sqk0-hZi21bPKkhP647BDT6GoAas_h62syP0jdhlw1f05Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juE4yOp4qF-x95QIPanfvRgqnsyh4XIdrvvXRorwHmR0sQXZGpBxUDHKtDA9OqgKZeD7EeoF3_PZnvpufWknfAB7LeP9Mk7XkIufZdwvfd07tROENqR6qLEBXxLc-5oWZtckjxE7CFCU1ZAG_t5NKEGaYlU-NqdlWECQzC066Dj00P5ET_2hTgn3EiPQQle8i-feMHmjAxO1cPCmYgKqljNbyVYgir7I8DmbIqRe97WSiAtauzFlPzYOWXL4fsiSf46zldcvgXjFtd7_YUmuUAhzvlNctJV1IrWttzv7md5nQDpPpAkWmf6ASt_MXH7PnsNZ4VlQPMDxd8aHVzizKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gR08BQ32Efr8nSOp_4WXsCXdlco3Ec0AOJG8dfdI-VXicbqyQt9u8sTCNXUqx08oOOOKZfF7Te-_zrXzD_R5aJJ0Nel6JT90VHLTwTPWDq1ZoIcbKC-bHdoty3mD5BAEs5AzcIAZZN2ngf5U3BM-EdA9TZxcG5-1dkfc3Gra6T5eb8ivWNpaYxThO7RK6ABRuam7ZLQPUtMamJn6xKPWW4PLfu14aujT7H7dthCoMAhMm2fA-4PwJL3vUnqiEmk45S7WK1_U0mK5juhEhMH5GswRt32NwlzOWsoShf2iu_3H1AlJ7DdzuWtEEXNhggYCyLpGeehKII9sLC2GBn2VTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fK71oz9MZe_Ilon0SK5LSLWLDkwg2bOELP5oxsJjS9wBvxERNXx7gT1cskDspOVLSLs5_KDDpD7m7mKCgZ97CY5Narp0ooSjdQPtr3F_eelGI9JKRMVq3ZRfCos_2TRg528yfCPehL3F8v5lpH1SJByBMQw_CEVf-J81kl0YA0EtJc4h9eRF3z1TlgdeRrphM3O-5_nEGMfKFDZGrqk4_p7mVDVw6YsBhSQpc2mXOIV2cbfeY-WQgmlXF_TXwYGRfoLpwoD0I7Vyi-VrMo-NP7-RQ36EtUF3d-7SRwSZqTaTekmZWQuvXleL4EL4ffLh7TWlVQmfQu4nmNsyFnkjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyP87VeFKFw75v6PGxII7BYWwCX-OTXRS0-CB9wL5tzNwTqPtq9CJs-phIDKIJZDoM49qOrbh4HyLnK9e9rCweWnHfO1Fhr1z7fnhyqB1XBWDWyViqvLgofafm9tlYbGOT5F_PDWkKKnchcrJcMMy2D-kn2bK8fLJuRtE9859BaWGW-sqFtus3NG3eNuWMnokGtsSKjA1JswSTqHQ-aLCF71yf8U9M_7l-NepkDL89dxOsSneBYqJkt-CydBzH9re5WsML4wpsCpPHJYgnlYPvTZg2mcRTfvDA8SFzAqn_JKDr8IMPat5FuG6tB2Cfnc-D5jSpOPZRNm6rKKLa1nzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از زنجیره انسانی دانشجویان و بانوان در رزمایش جانفدا در مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696088" target="_blank">📅 14:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696087">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7zQZJos_qozHuQ-m1lAVq0KhSKfkth_5D_ftPm42NYORCo9UCada6O2O9OsTm8KYRJ154sg2n-CBM5cFwnqXXRMincrRh4NI2YZJ6CV6YZZAM6GrVy3GFbSIbrlAPIOsk3r_zEq4oGUg_uNoBdIRFkQMgylhsklmT7cXcaRIbUgAIWWWPG-5jzwuU706fqsAwd24bZcOwWr04oSXdt3n8-du7WTA3ttzwoXNaNGg1eqZcJTGmCosuLaCfLc7n8GK1opOF3OZWCNKhJGaKVoMctpHxdPiofAnfuDEJQ0zVf06L3NTHLwyE8tfPsU6SuHfZRy2Pxuwrll7GGCP6anwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو نزدیک‌تر از همیشه به سقوط/ بی بی کمتر از یک‌ ماه به انتخابات دست به جنون می‌زند؟
🔹
نظرسنجی‌های روزهای اخیر تصویری متناقض از بن‌بست سیاسی اسرائیل ارائه می‌دهند. بر اساس نظرسنجی کانال ۱۲، اردوگاه مخالفان نتانیاهو با ۵۴ کرسی در برابر ۴۹ کرسی اردوگاه او پیشتاز است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3250387</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/696087" target="_blank">📅 14:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696086">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ساعاتی پیش پهپادها «احتمالا روسی» به دو کشتی تجاری در دریای سیاه، در حدود ۱۵۰ کیلومتری شرق سواحل بلغارستان، حمله کردند
🔹
یکی از کشتی‌ها غرق و خدمه آن مفقود شده و کشتی دیگر نیز دچار آتش‌سوزی شد، در صورت تایید این اولین حمله به یکی از اعضای ناتو در جنگ روسیه و اکراین محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/696086" target="_blank">📅 14:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696085">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce928690f0.mp4?token=oPeLI1C1GKJ_a6FWAdfYVs0hLcOgMGv5Hea3NnefWRIlgaK41_7hOUdZy3ixHwEz35b033bf2mHnM3ZddPC8ctnF_vbaHuU-ybKZ5hYM6y7wV1l7CTVPlJaDxkk0Xu1bLcUgthdznHLIsm3xAxrvzN0zeiheh3K8cTjvkfxRGHe9GX41qnbBLlaplAsyCsfPAFRAR8D9Nys9QCR-0NIE14_iXALSJbX0VvDozXcDDnvyZG5Zd2jY56KFXOSOLD4bIJsql7IgrBeyvruXXaRFfS3OJ6RCJ4hlu55Beji8l6TqCQAAX7fqEgHiEq3U6rvMuyZb7COcGWDZ47I-kgocrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce928690f0.mp4?token=oPeLI1C1GKJ_a6FWAdfYVs0hLcOgMGv5Hea3NnefWRIlgaK41_7hOUdZy3ixHwEz35b033bf2mHnM3ZddPC8ctnF_vbaHuU-ybKZ5hYM6y7wV1l7CTVPlJaDxkk0Xu1bLcUgthdznHLIsm3xAxrvzN0zeiheh3K8cTjvkfxRGHe9GX41qnbBLlaplAsyCsfPAFRAR8D9Nys9QCR-0NIE14_iXALSJbX0VvDozXcDDnvyZG5Zd2jY56KFXOSOLD4bIJsql7IgrBeyvruXXaRFfS3OJ6RCJ4hlu55Beji8l6TqCQAAX7fqEgHiEq3U6rvMuyZb7COcGWDZ47I-kgocrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت اینترنشنال از گزینۀ وزیر پیشنهادیِ دفاع
اینترنشنال:
🔹
وزارت دفاع عملاً به یک وزارت موشکی تبدیل خواهد شد و به‌طور خاص موشک‌های قاره‌پیما.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/696085" target="_blank">📅 14:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696084">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
حمله به کشتی تجاری در نزدیکی عمان؛ ۱۱ هندی زخمی شدند
وزارت امور خارجه هند:
🔹
در پی حمله به یک کشتی تجاری با پرچم پاناما در نزدیکی سواحل عمان، ۱۲ نفر از اعضای خدمه کشتی زخمی شدند. ۱۱ نفر از زخمی‌شدگان شهروند هند هستند. جزئیات بیشتری درباره عامل حمله و وضعیت کشتی و خدمه آن منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/696084" target="_blank">📅 14:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696083">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تایم
لپس از بزرگترین زنجیره انسانی  جان‌فدایان مشهدی‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/696083" target="_blank">📅 14:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696082">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ad9a517a.mp4?token=A9z6QFTE8aHdfEQj5jxEUkARgXJzoEO73KmbQrae4FY-cG2Xy1HicCbN2l_7FhyOnVNneXzn3FjozTI-eUi_JW6nmI3-c7CCOdt6jOYbxbeECPIXZ1HGiWrqRRaNR8Q8kLHbYVrDku1sbARYNdcWunkuRSZeAi4p77ZFtOBq8mBzdwdpxJeMpgiLIhRc-WjI7tInFCCMKTQuxwNqQd-4Yrzcuup-roapEiQ-6fbURTTitNL78sZtvwc6Xy22rUWlgbkFLWffhbxzFDcxy6Ii6AkjBkXJp0MLYzmHCvfZGgf_dKHwLq5PiQlZ5pBROQikZ5GdWjsx7U2YVJe2ZHsR4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ad9a517a.mp4?token=A9z6QFTE8aHdfEQj5jxEUkARgXJzoEO73KmbQrae4FY-cG2Xy1HicCbN2l_7FhyOnVNneXzn3FjozTI-eUi_JW6nmI3-c7CCOdt6jOYbxbeECPIXZ1HGiWrqRRaNR8Q8kLHbYVrDku1sbARYNdcWunkuRSZeAi4p77ZFtOBq8mBzdwdpxJeMpgiLIhRc-WjI7tInFCCMKTQuxwNqQd-4Yrzcuup-roapEiQ-6fbURTTitNL78sZtvwc6Xy22rUWlgbkFLWffhbxzFDcxy6Ii6AkjBkXJp0MLYzmHCvfZGgf_dKHwLq5PiQlZ5pBROQikZ5GdWjsx7U2YVJe2ZHsR4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خبرنگار وال‌استریت‌‌ژورنال: سرویس مخفی آمریکا CIA یک لیست از ۵ الی ۱٠ نفر مسئولان ایرانی را به اسرائیل داده که این افراد را نباید ترور کرد
🔹
آن‌ها قصد دارند در آینده، حکومت را به دست بگیرند تا ایران کشوری نرمال شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/696082" target="_blank">📅 14:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696076">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iitBGCuYFQhmACtfQpoSlLZf0T3gbT4EESjvQcPJB0n0amM0E9ylA5xbQv4OSD_rcvCx0Ua31ZzHsQ0JRCCChMfXKXrRZgWCgEa79dLNaCp0nzFTmn1lsj3tDcxA6UT7jg6mRWOdAUx0SmMGk2Q5lBvi2OLavo9mxGVj4aRHvJUKnT-Lh6lla-K8SWTnLnmopVTWyZByrX8u0YR8PfEKtuSTwHva_XJta6lwiwBUVdmhLTM92vfbgXV4SgoR5STbRs77biSYnWFLZEUGjuGAEKnd2jBo0cZCSG82IJ01QM2OPJs_rh8BDdLvDBHpa1Ng6VMjyzIGr7D_OclRNk11zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOvlEHngGMO0T6pdg7o-2jdiS5L3C5tw-EzeP5jWiagkVYXw1tyG03iTI2Lao8w0RDMdIWuRcRhIE3041X4lIc5rlOsn_SmxZiAzc36g1AdlMOD4EqsEo7yWah8TJAd1cdgeN4cXKLr5zic8u0cj7mR0sCPORX3RWBAqZ6pBbymQoG_zqTzj7ga0PE3JDywtlx6rDZ5uX228kiQjp-OgUT75eyguW_IdVzVsKol7calmUa69IvwykR33UH9EO8Vx8zbKOrdPZGKR1B5bz55moLQaiTBIUucdHKRzt2upIOiLFikT3URKHfvNEXT3Xsb32ktbEwXZqhR-Dv85dez1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOCTvvk1AFgv93NwSBZ0nLSCumO6v4cpup7CXc8TWA5N1rRUXO0Q1Zy7i6CYVN0_2pl9WLStJKnbic9hA6EHNYNhsIRxFmp0kXre0_2BOTfA5wjUewlx8Mpv6oTuCbdPcLCcvuOIDy9rf3FPpW0b_3VbsugBjOnHcUWw-7QdAMk5RrXrFQ37ZGgKMTgyG1Cmg9_JpMb91ml68sIDAfaps5lVDGKWQmAZdXiV-xX3Hk5aA2sr6h1bKBYngvBUjHC7teYBVOrOgHgbs99MGvZynipR5n86fGLJoESWpIlvo8Y4vgTp3jwOi7TUA5KNxxRwJXAU6RmMScy08fH6B4jSTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gd6D6FdeXplgues4rda1gQlONpw6g0NAkdcUreCjjimW19miKG0osFpyTxzdC_MFLOa4JVFYil8kv8R0b8lKK0ZhZh9JRT6ZaXk0m2E28c9HgLhnVnrE_yaIblDlAzvku9z2ojEEAmLqzmIfiGV2fv28tRYkt8rvYGRmvm48RVjFmueBIlNIboRf4wwNTf56hW1CtG8_8oAysTEAT9xFBextc9r_t36vbnBjVQzFUgQokLFKjuzqFXpHPaAl14bjL04lOV2L8Au-7TOpKrBtGBn2zQLc2EBE--eBFMvhgqBLTY0pYaqyoBGZ8GSJ4iXStackwHRz3xsr6vPidoWHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1ythp5WefeJINSU0EjUan-2D7u-BV0c2vwS6RxTPMSp2Ae4dM2deTIktZ5DL_UEJF7ZD4gnjYOCNe2R_5pc-fU_WXkcAdyxBWZNDv0ksNTCDvvVnCUCYOuDWD2YcZzAWlbUGi2hLMWgBdYJn1xAygbmfObi8S7_t0_nWxG5IVFMoFW8_ntaBL1IE4X-lGjJanYY8o4PMpSWJD6JhW-Ysz_596X1UgQYhkIlu7Cnvt5e2Eq1CS_EnYQfxzHWTW_7Nc5p1ZEVMxsfP1o2QHN4x9MtuCHbAMyMfnakEXMx_rvajqC_MqBIvdfx3lo8AejqsygtShKSzKlNyS_YyEmo4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKGC4uX15QGRhM_VYKWPD2EfKH3CiftQ1bebGDFNjrEQDXnMuxcuQJpqYDhqYJtpp7Q04V12fdh0w9gGj8mizI6l41vasKUUlBZS_0YdHcSuV05qTq0l6sHpapd-AqiSTT_l_6IsleJSWXTll1B93M-VEJ07WO2Xwhe2i0pMBaR4eMBoj5wf4zkyF6AawEF7k01jxKi5sOu-akWw_sTJtyX6v2LysL_934uBJxGxxFqV3QXRB40IG-f7F43qpRuYAKb8Oag2I6fyOxHq29p_MMMNp5RqNfO_uC7TnTWG0d-xjUhm4Ztr7-p3Q-OEFT5tGyc2o7uGGifV-ZF0FJd6mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگه شکم داری و نمی‌دونی چی بپوشی که خوش‌استایل‌تر دیده بشی، این پست مخصوص توئه! #فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/696076" target="_blank">📅 14:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696074">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وزارت خارجه قطر: تماس‌ها و رایزنی‌هایی که از سوی میانجی‌گران میان واشنگتن و تهران در حال انجام است، همچنان ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/696074" target="_blank">📅 13:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696073">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاباما تور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap9ilouDL7mnxlRDaK2RsGrnNOiZLb9X86gX8572XyW108cCXsLFm_yBo2x_wxWmZay_EOWarWPp0dzwR4UEbOsmbWhVITcNiI5PjN8LlLWsXixd_w12JHKZ9T293reXJMuXHwKlWlgctUKAbPz2Km07Pt_Pat2QbRkSf-2jbHs7mq-GJhI91Jawv7hvdiIOjg_Opb7FVhrilsdc-65Lt5--4hRtdS0n3cIAcoyVVZEC76ELYyftfQhS4FPStEPVt5qOhHF_3IIJohr9ucSbngKyEt7AMC3j3jahaKqg4w9rfJQ-wjlq0id9FHIHv9nC1v-6ad5tG_OV1fxVJWFuzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اولین بار در ایران، تورهای کمپ هتلی رو ۴ قسطه رزرو کن!
😎
⛺️
چند روز اقامت وسط طبیعت، با امکانات یه هتل؛ تجربه‌ای متفاوت از کمپینگ که حالا می‌تونی با
جاباما تور
قسطی رزروش کنی.
🌲
❌
ظرفیت محدود
برای اطلاعت بیشتر از تورهای کمپ هتلی و برنامه‌های جدید ‌با شماره  زیر تماس بگیر
👇
021-49275111</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/696073" target="_blank">📅 13:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696072">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">🧒
هر کودک، یک چراغ برای فرداست...
💡
✨
🔸
کودکان امروز، سازندگان فردای ایران‌اند؛
با آموزش مصرف درست برق، چراغ رؤیاهایشان را همیشه روشن نگه داریم....
💡
شما هم با یک انتخاب درست، یک چراغ برای آینده روشن کنید؛
درست مصرف کنیم و آینده را برای کودکانمان روشن‌تر بسازیم.
🌱
💡
🆔️
@tehran_roshan</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/696072" target="_blank">📅 13:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696071">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
معاون رفاه و امور اقتصادی وزارت کار: مرحله هفتم طرح تغذیه رایگان کودکان مبتلا به سوءتغذیه شارژ شد و از ۱۸ مهر ماه امکان خرید سبد غذایی رایگان برای خانوارها فراهم شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/696071" target="_blank">📅 13:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696070">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c733b10dd.mp4?token=phERRqX8KkNeDF3hwXkpWolZfR6az6rkwiSbJ0kCl80gDthpbW1csoiShQ_ZmpHKJq87S1PcgadPiYm5ApUKkEKImJOAdfkBfP6roFleyVl4Ju8Next23lktGTlCCMovL5fnpPUrVFJJk0_Szjy27JjKGSjl1Jk1y8IDBPJkF72ab4dwmJ1RVrGo-uenhoqZfqnZOyZlVfvi1y0uGjpcnwgxJDPe9MnwPYGw0nXyIGAOXZBr-MIvBid5zz7RzboTjUSeGFTLBaILYcZGfJ9C7e2z4R8YxCogKY8-mOeO2WfupEF0XyMGAeFqiuDfYhY6wK6wkhmyi9NwKgjAmqHypA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c733b10dd.mp4?token=phERRqX8KkNeDF3hwXkpWolZfR6az6rkwiSbJ0kCl80gDthpbW1csoiShQ_ZmpHKJq87S1PcgadPiYm5ApUKkEKImJOAdfkBfP6roFleyVl4Ju8Next23lktGTlCCMovL5fnpPUrVFJJk0_Szjy27JjKGSjl1Jk1y8IDBPJkF72ab4dwmJ1RVrGo-uenhoqZfqnZOyZlVfvi1y0uGjpcnwgxJDPe9MnwPYGw0nXyIGAOXZBr-MIvBid5zz7RzboTjUSeGFTLBaILYcZGfJ9C7e2z4R8YxCogKY8-mOeO2WfupEF0XyMGAeFqiuDfYhY6wK6wkhmyi9NwKgjAmqHypA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت معرفی وزرای دفاع، نفت و اطلاعات
فرشاد ابراهیم‌پور، عضو هیئت رییسه مجلس شورای اسلامی:
🔹
با معرفی مهرداد اخلاقی کتابچی به عنوان وزیر پیشنهادی دفاع و نیروهای مسلح به مجلس شورای اسلامی، فرآیند بررسی صلاحیت وی وارد مرحله اجرایی شد.
🔹
انتظار می‌رود فرآیند بررسی در اولین جلسه حضوری مجلس در تاریخ ۲۶ مهرماه نهایی شود.
🔹
پیش‌بینی می‌شود پس از وزیر دفاع، نامزد وزارت اطلاعات معرفی شود، اما در خصوص وزارت نفت، باید تا پایان دوره سرپرستی منتظر ماند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/696070" target="_blank">📅 13:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696069">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سخنگوی انصارالله: فرودگاه ابها و تجمع نیروهای سعودی در جیزان را هدف حملات موشکی قرار دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/696069" target="_blank">📅 13:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696067">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de80d2c24.mp4?token=nfCXCvZZ6GG_zcAHjT7QtAUQyFYiz3rZGZ1Rdhj14PIOcV96M6sPfQP_f0oDypGKyHkO5bbwlqbtHozyHMappYPDjepXIP93OgR_Fkd_V6xyx4FHSKArvzZiPgQ-WaIf6kc_svQ__5w8QvtLOHh_AHow1wJjSd0ukWlTCSqde0zVPnt-cTqOa63QTAIkGcx2sIUnlVd76LGJa8jhB9-JmFguDJ9IMa2uaAVYtKBqN7gUZDBn_a8DPdLqzNb7M5GMsMEY1TrMv0RodESbZqS_UgyGYT7Sr2VZJPMSr3DACeLyVRpwvcIjJWNxjb7bMinpAJhHOljRsIjD9t8bMEPJMqre65Ja05xvtpQSlTpIY4Si-ruOfMF8m89PVQqyxVOYVuyuRitz7ugt569c2yUNhxzHR0z1lyHKWDYqqO96PaHdl3sMS2hcpgLLD_EDcBZzI4nkn4SNiwI48JcOm7MC3vRSvZJ7aBjxKkVRC8w6DnEVC-2ZjH60WOMQtF7fJuPGnq8JpI24_hByrT8iV9Qs3p__LNyGqulwKXspCfOgbz2kqc6wQYbiAxQJvVF-y5ux_9ISwBv7gOgmcvjA1wmtaGdCGrl8WQChafd0pjNU4O1LXwD7DSq-vDRIeq8QAw5lDGxqRyLZD4hoVQdV6hFeK00zLviNtYc8nc9yhZ3pNTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de80d2c24.mp4?token=nfCXCvZZ6GG_zcAHjT7QtAUQyFYiz3rZGZ1Rdhj14PIOcV96M6sPfQP_f0oDypGKyHkO5bbwlqbtHozyHMappYPDjepXIP93OgR_Fkd_V6xyx4FHSKArvzZiPgQ-WaIf6kc_svQ__5w8QvtLOHh_AHow1wJjSd0ukWlTCSqde0zVPnt-cTqOa63QTAIkGcx2sIUnlVd76LGJa8jhB9-JmFguDJ9IMa2uaAVYtKBqN7gUZDBn_a8DPdLqzNb7M5GMsMEY1TrMv0RodESbZqS_UgyGYT7Sr2VZJPMSr3DACeLyVRpwvcIjJWNxjb7bMinpAJhHOljRsIjD9t8bMEPJMqre65Ja05xvtpQSlTpIY4Si-ruOfMF8m89PVQqyxVOYVuyuRitz7ugt569c2yUNhxzHR0z1lyHKWDYqqO96PaHdl3sMS2hcpgLLD_EDcBZzI4nkn4SNiwI48JcOm7MC3vRSvZJ7aBjxKkVRC8w6DnEVC-2ZjH60WOMQtF7fJuPGnq8JpI24_hByrT8iV9Qs3p__LNyGqulwKXspCfOgbz2kqc6wQYbiAxQJvVF-y5ux_9ISwBv7gOgmcvjA1wmtaGdCGrl8WQChafd0pjNU4O1LXwD7DSq-vDRIeq8QAw5lDGxqRyLZD4hoVQdV6hFeK00zLviNtYc8nc9yhZ3pNTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت اطلاعات: ۳ هستۀ عملیاتی گروهک تروریستی-تکفیری در جنوب‌ شرق (شهرستان‌های ایرانشهر، سرباز، سراوان و زاهدان) منهدم شدند  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/696067" target="_blank">📅 13:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
فرانسه یک موشک با قابلیت حمل کلاهک هسته ای آزمایش کرد
ادعای خبرگزاری فرانسه:
🔹
رئیس جمهور فرانسه بر آزمایشی نظارت داشت که در آن یک موشک جدید، قادر به حمل کلاهک هسته‌ای، از یک زیردریایی شلیک شد./ الجزیره
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/696066" target="_blank">📅 13:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696064">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b12d546c0.mp4?token=Vx3TPxrvV588hqEYFR_csY66BA3hHQL2Ci9ekMHfDUIKadMBgmjvmJo2YrIUsepeqbI0ZxTRLgf_GEZcP3wmwKkOkddoNWI0klpYu44GoPhQfOPPYGdpV0Qe2jvaqEseQcJ-yCn85y-unhMD1e-ZHojYQjBFS8IeACKrZENGp-cmD-z-663bKJ9KMaIo2-6A5RCSexkoQFTQWM9jJBZTEkKDiW4c2sO3u_aWOXdyYiPmq_hd2sh7pwp7ki6Z1jjsMl5UxfE2RnJ5URgJ2NInEgIXga0ujcW3bzpJgkuENQB5qyi3IPKitz4hsmXK4kySjmwZVipKTr8bAIBzfRxsAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b12d546c0.mp4?token=Vx3TPxrvV588hqEYFR_csY66BA3hHQL2Ci9ekMHfDUIKadMBgmjvmJo2YrIUsepeqbI0ZxTRLgf_GEZcP3wmwKkOkddoNWI0klpYu44GoPhQfOPPYGdpV0Qe2jvaqEseQcJ-yCn85y-unhMD1e-ZHojYQjBFS8IeACKrZENGp-cmD-z-663bKJ9KMaIo2-6A5RCSexkoQFTQWM9jJBZTEkKDiW4c2sO3u_aWOXdyYiPmq_hd2sh7pwp7ki6Z1jjsMl5UxfE2RnJ5URgJ2NInEgIXga0ujcW3bzpJgkuENQB5qyi3IPKitz4hsmXK4kySjmwZVipKTr8bAIBzfRxsAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه رفتار بازار ارز؛ آیا الگوی سال‌های ۹۷ و ۹۹ تکرار می‌شود؟
🔹
دارابی، دستیار ارزی رئیس‌کل بانک مرکزی: در ماه‌های اخیر نرخ ارز به مراتب بالاتر از تورم رشد کرده است.
🔹
این موج رفتاری مشابه مهر ۹۷ و مهر ۹۹ دارد؛ شوک‌هایی ناشی از تقاضای خروج سرمایه و انتظارات منفی که در کوتاه‌مدت اوج می‌گیرند و با تخلیه هیجانات فروکش می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/696064" target="_blank">📅 13:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696063">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNsoOvXmh-V7JkS6azfz0Q8hUF199tSbfUMG7ya8U_JDTRwqHV1l0F-HfbfD0Ci6PWHMfIUrNQQVaxSrJJtN3465NnlcAITtY50jsjzDz9GYDcvHZ_xcecANIeYbZ5GVPnRWTbn8LhEjiwwdvvkfXtOgPnj_N8I3q-KAUR0RKdFHRsfQvjR6icU9FIAXA5Bxb34adecdygj3cq6C0_JHd_LqGS6378gCnnsIDLAtFdO_ztu7kp2qXkraDh4jW7M7UUus4GagCcWwzsYXzw_bqzoaKlC80sc1Nh7D82UUKQdWvWcudtDdv-z3NnNZ0_XV6p0GK65rQAM12wTTSUZ73A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای اولین بار در تاریخ میزان فروش خودروهای بنزینی از اکثریت خارج شد و به ۴۹ درصد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/696063" target="_blank">📅 13:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
یدیعوت آحارانوت: سفیر انگلیس‌ به اسرائیلی‌ها گفته که اگر کنسولگری انگلیس در قدس را باز نکنن، ۲۷ دیپلمات اسرائیلی اخراج می‌شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/696062" target="_blank">📅 13:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24165598a.mp4?token=H8DOVn67RhZHVyg4GfbGWiwU57J8N7D9PaBN4kPZffTHO6EPq-nqQhesYOWYNEhEaADszkNfPiebWFnAwXepx0erinzj1QSGgwxWJM9B3bE4C4AKjx_Eral4n55gJsesNE33FcpOJsd44-OrHOW5CU3D-AEmKtvfmxI3FDpev0dxPtaYKC3YKqDdFPvaq-1EQ4EaoCzM1WBiC1WlhNU9XAyL9lV9LUc9VJzUgDJxnSwpuiZcSyfcwpCHxVgxuewbQ3TlzvnW7WRkaCTe04Ep6uMMp-2q3YJRCnXAf2WCCXLU3C64AXHalzbw0KAAdJDVwHx7mo1hft3JiP6ZNae_iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24165598a.mp4?token=H8DOVn67RhZHVyg4GfbGWiwU57J8N7D9PaBN4kPZffTHO6EPq-nqQhesYOWYNEhEaADszkNfPiebWFnAwXepx0erinzj1QSGgwxWJM9B3bE4C4AKjx_Eral4n55gJsesNE33FcpOJsd44-OrHOW5CU3D-AEmKtvfmxI3FDpev0dxPtaYKC3YKqDdFPvaq-1EQ4EaoCzM1WBiC1WlhNU9XAyL9lV9LUc9VJzUgDJxnSwpuiZcSyfcwpCHxVgxuewbQ3TlzvnW7WRkaCTe04Ep6uMMp-2q3YJRCnXAf2WCCXLU3C64AXHalzbw0KAAdJDVwHx7mo1hft3JiP6ZNae_iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های یمنی تأسیسات نفتی را در ریاض، هدف قرار دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/696061" target="_blank">📅 13:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VawwIQIuSs3VB-OWisosgqqXpOj3hfNnX5Nf2kMxFjUBGBbi1SyzHqMPD1A7b3-DUx1Mo7s4lP0L9hGqyyU1hXodDAUYiY8dHwu32b3o0Y-T3OydPLmQBKwLGJgq3qoictBPxzBqKu8a52aU4kOzkmnIoS91P8fjMGGu2uXKtDxH589bH-dLvzNeki3w407pWa5MD-cToikEDg23DLBmOyyzXgCOGQ_6k7ThNYeNA8jm9yQg2lRbgrQUQqG6S91kESobfcHpNJMJXNTvYjRzFVZlUDjeZDqBBEzhV5EHd8rDSkqrpJTW9o9QVLIxxZaHrFtzCL431SVie6S9pOrHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر کابل مخصوص چه کاری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/696060" target="_blank">📅 12:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIo8wsCZOZ0MOKu1xKgaRHcRKBPgl1pIwfBxA-lqDcBzpssiDM3tF3BkkHu3d0hL5wsRQNlj9hf75Uuv5ZLeQNVcVief5UsYq5Dml3Zp3TQI3AI6A767cl1--Q4hR_toysDYjWfdCmUHnsh_k-RToIimZgS92Ez4icAc6dA4WkhA4C-3iPOJzOdiaDTsvkJo9W1sqT3cUDEw-icK9EdBpfmwYTMPo6duCIHJESO7LPcnMLeRQksCBNdKcXMdzL4q_6fKbMHeWljlCfiVJkTNt1E0hZhcjcssanyqeCZnQcwrcA0p6Emkt_n1Aq9jV9JPVCukkfWWM0LxSOhtStpdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بخشی از اقدامات اخیر امارات علیه ایران
🔹
امارات همزمان با آغاز جنگ آمریکا و اسرائیل علیه ایران، مجموعه‌ای از اقدامات سیاسی، اقتصادی و امنیتی علیه ایران انجام داد که با سیاست‌های آمریکا و اسرائیل هم راستا است.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/696059" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696058">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
انهدام تیم تروریستی تکفیری ترور علمای اهل سنت در زاهدان
قرارگاه قدس نیروی زمینی سپاه پاسداران:
🔹
تیم تروریستی تکفیری که در ترور علمای اهل سنت، شهید مولوی یوسف گرگیچ و شهید مولوی محمد انور ریگی و نیز ترور ۲ نفر از نیروهای  فراجا در قطار خنجک زاهدان دست داشت، به طور کامل منهدم شد. در مجموع ۸ نفر از این تیم تروریستی به هلاکت رسیده و  ۲ نفر دیگر نیز دستگیر شدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/696058" target="_blank">📅 12:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50c57a091.mp4?token=jbUT5KCkA53ICHRJd9oLQrH4i9GWURe85tC2F551eDsgl9d5pMnS3nopv2QP_NyD8Dzz-zpyt_tOcgcoisGFp_hu4S8ASe7PNxmgYcTjb6sOzlN9EtguANsN875m1jQgnFQB7zVxAv9ZnbOTAC9GsfFenszL7i234aq6dYfulrJBxctCCWPj1JUDuhuy45xZboXc8Fac0tuCNSMFPUZklzrLQ1bW1z_o2qZnsPJmVBB_3o6DLs2VRKjJDz44HTi0i1j4-apSf4O_GCTrDp2ry2wUC9bsYyR8Es_V9R-Dsvtb5rAC7OJb_ZrxNMQjZEo_EYiCflyLR-ALEQfsj03s5TVIOv57Gq_CIQeD2Tpn8lEuIh5rqszdTBWmLzlMTxL9MQWfOj92F_MgcHeO7kj1LV5G-36RdrFhZND_19PgbiPjPJa_tnX8OjiZtVILPrhNkaBYDVGlPDtdZGefW0C7T9duoCyEITNuO0JzDztudT8Mow0MeNLe3a5IdWLoJaDDlMmLR42y2I6ZxD4aQ1disDOm1ZkqC4v6JkBV6VHyWkA4uqPXktqhsMmdScL1Wp_dVgOETTbwwMBE3Mk9hzwis6-zP-MlPVORMOpZpaxaKxJIXTXxnD9zg7H4N4P1IspSpPyf9rScIuFKzHD6Chd6zirVOEXrltIcB3kzwHLY21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50c57a091.mp4?token=jbUT5KCkA53ICHRJd9oLQrH4i9GWURe85tC2F551eDsgl9d5pMnS3nopv2QP_NyD8Dzz-zpyt_tOcgcoisGFp_hu4S8ASe7PNxmgYcTjb6sOzlN9EtguANsN875m1jQgnFQB7zVxAv9ZnbOTAC9GsfFenszL7i234aq6dYfulrJBxctCCWPj1JUDuhuy45xZboXc8Fac0tuCNSMFPUZklzrLQ1bW1z_o2qZnsPJmVBB_3o6DLs2VRKjJDz44HTi0i1j4-apSf4O_GCTrDp2ry2wUC9bsYyR8Es_V9R-Dsvtb5rAC7OJb_ZrxNMQjZEo_EYiCflyLR-ALEQfsj03s5TVIOv57Gq_CIQeD2Tpn8lEuIh5rqszdTBWmLzlMTxL9MQWfOj92F_MgcHeO7kj1LV5G-36RdrFhZND_19PgbiPjPJa_tnX8OjiZtVILPrhNkaBYDVGlPDtdZGefW0C7T9duoCyEITNuO0JzDztudT8Mow0MeNLe3a5IdWLoJaDDlMmLR42y2I6ZxD4aQ1disDOm1ZkqC4v6JkBV6VHyWkA4uqPXktqhsMmdScL1Wp_dVgOETTbwwMBE3Mk9hzwis6-zP-MlPVORMOpZpaxaKxJIXTXxnD9zg7H4N4P1IspSpPyf9rScIuFKzHD6Chd6zirVOEXrltIcB3kzwHLY21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز ساده برای تقویت و پرپشت شدن موها؛ ترکیب پیاز و رزماری و میخک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/696057" target="_blank">📅 12:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696056">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHuWkQ-x1qFfPWKEe74KSDvRzvmQSuCOoSh1SxoFca7zzJ6Mx_yFvoEPD7spVvhy4KHj3E1neKy0HLXJJ8ql8hrglcnTi6je9K8tjc77D6DWkFTSH_77iVwJgUw8n8gGUK76h-w8RivQOpZp9-zNwHwXzMstG03mvgMAVFL6icAExCeHmBESpAfwQJ-7qKdIpsb61KitWa-BW5lSNyL4dt4N38OxdJSZYCWtlN-azlPcISskm1vmr3bVdwwO6OqNUIEwUmi3K0w0yruX1cuIpL53D3eeEG2_DR_nSYzpUCriOmQ1PqqeWPN60MRNr5LZl5FhQQagWceedQwLXUdEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«چشم‌روشنی» برای نوزادان تهرانی متولد ۱۴۰۵
شارژ اعتبار ماهانه حساب شهرزاد برای مادران تهرانی
🔹
شهرداری تهران طرح «چشم‌روشنی» را برای حمایت از مادران تهرانی با فرزندان متولد ۱۴۰۵ کلید زد.
🔹
این طرح به‌جای پرداخت نقدی، یک بسته اعتباری غیرنقدی در اپلیکیشن شهرزاد است که صرف خرید کالاهای اساسی، خدمات فرهنگی، سلامت و گردشگری برای نوزادان تا دو سالگی می‌شود.
🔹
اعتبار پایه ماهانه ۳/۵ میلیون تومان تعیین شده که شامل ۲/۵ میلیون کالا، ۵۰۰ هزار تومان خدمات فرهنگی، ۵۰۰ هزار تومان سلامت است‌.
🔹
مادران سه دهک درآمدی پایین، ۵۰۰ هزار تومان شارژ اضافه دریافت می‌کنند که مجموع اعتبار آنان را به ۴ میلیون تومان می‌رساند.
🔹
این طرح با هدف کاهش هزینه‌های اولیه و دسترسی آسان‌تر خانواده‌ها به خدمات شهری طراحی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/696056" target="_blank">📅 12:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696055">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNTudYvjAs7BFY92KM3IRtytZQCSSx9Q8cQ_wVJwS4jzR1-nkYsL-m9df6s5ad1DzXpZVX31GWkwIpuX7usqkDTay41ZlaeQYXF7gXGCHIgU_iC3C1irAbR3pGbKtglutBXN7e2o94EVB9jTgaDnV2IAgMFaXyUZmgQX3p3j2HDY_5dTsS1nOTKVf3Ebo_OZOLwivaIVHcPGdRRUlmTgi_tH4ALr0aakb0R8cC7QP55nnG4z_2mHRIEJYSdnVrCAp7--7P7ugtcVdMm8qGxmN-VMANQ9oR_8Gux1zSAVicJA1SygsD6wMF8uFIWgxRk0MbHF3rgz2DeboR8kCRc3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور آمریکایی: خسارات وارد شده در حمله ایران به سفارت آمریکا در ریاض شاهدی بر این است که ترامپ برای این جنگ آمادگی کافی نداشت
🔹
امروز شخصاً از نزدیک خسارات واردشده طی حمله ایران به سفارت آمریکا در ریاض را دیدم. اگر این حمله در طول روز اتفاق افتاده بود، می‌توانست به یک حادثه با تلفات گسترده انسانی تبدیل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/696055" target="_blank">📅 12:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696054">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96b663f829.mp4?token=gM9hqfJDudFaimVeIqRyU_iachATAzz9YVh9Abkes2h02rFVwpMVM0Jq3v40QPvsPc636ALEjKpb8VPR5p1s1m2NVHXN4PLA-uAO4Kqs-VZYvb9O9mNu33C2LCBLPaBNut3BG0Mku4Q8No5dxN86qSpVrwrNhyhAUgv_18TI7kb0O_LJHTTxLFIoHy8sCPBBKpoF7Af2QViPCVB7V7qD1WjJGVmfaDRCc_jsN7vm7JO4nzv1zy8AkI1uXazLGtkAARqanXuZSr3a_3AoQRzzH05bQnR1giRqQbGLHjTMt-hKVI_4hOYunUbWfjCDGixPSUezXRxQNGnbHdzIAWAxWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96b663f829.mp4?token=gM9hqfJDudFaimVeIqRyU_iachATAzz9YVh9Abkes2h02rFVwpMVM0Jq3v40QPvsPc636ALEjKpb8VPR5p1s1m2NVHXN4PLA-uAO4Kqs-VZYvb9O9mNu33C2LCBLPaBNut3BG0Mku4Q8No5dxN86qSpVrwrNhyhAUgv_18TI7kb0O_LJHTTxLFIoHy8sCPBBKpoF7Af2QViPCVB7V7qD1WjJGVmfaDRCc_jsN7vm7JO4nzv1zy8AkI1uXazLGtkAARqanXuZSr3a_3AoQRzzH05bQnR1giRqQbGLHjTMt-hKVI_4hOYunUbWfjCDGixPSUezXRxQNGnbHdzIAWAxWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر رنگ پلاک به چه معناست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/696054" target="_blank">📅 12:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696053">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a2f2d07a9.mp4?token=v7qVpFzz5ntcY12bL6WVJ170pdCMdyQkOi34fVIl29dJFrenuRAxeKYiM7ngNAfUav2jzkzm0Zll4rTmZ1PgymzJuKhdkyLEMg3_yffN6DrH1nfEqK9sOPWpyqTZAeGM9Vr3Gj_5VnySyNXunX7LkfS-zzptv9WGG95aD6OeOsQ9ij6IghtxJW-SH-LrPRAteIgzWIXMiLUPX0XZQbyKKejpZrBQCyV3LVogBp4dSPquXtd9BEiGfiUZ-OfG5HoxqOMZo-3LapK3oshB3mMonRspXoVp6Y8yhisp1wzdzkeZBrHZH2BJbQKDpSO-UR0Y2kXNJKSxiVwcvhBHEOVZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a2f2d07a9.mp4?token=v7qVpFzz5ntcY12bL6WVJ170pdCMdyQkOi34fVIl29dJFrenuRAxeKYiM7ngNAfUav2jzkzm0Zll4rTmZ1PgymzJuKhdkyLEMg3_yffN6DrH1nfEqK9sOPWpyqTZAeGM9Vr3Gj_5VnySyNXunX7LkfS-zzptv9WGG95aD6OeOsQ9ij6IghtxJW-SH-LrPRAteIgzWIXMiLUPX0XZQbyKKejpZrBQCyV3LVogBp4dSPquXtd9BEiGfiUZ-OfG5HoxqOMZo-3LapK3oshB3mMonRspXoVp6Y8yhisp1wzdzkeZBrHZH2BJbQKDpSO-UR0Y2kXNJKSxiVwcvhBHEOVZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر نمازتو اول وقت نخونی نمازت رو با دروغ شروع کردی
گول رئیست و مشتری و رفیقت و دنیات رو نخور</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/696053" target="_blank">📅 12:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696052">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای ترامپ: بذارید ایران، لس‌آنجلس و سن‌دیگو را با بمب اتم نابود کند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/696052" target="_blank">📅 12:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696051">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1155257fca.mp4?token=tgXq8hKlI9T_bwKe1R-a4CbLxsl60uYsQFYqMzQno2ZI5EAWtSJV6pLfBrS3INaU_Qe_pqxmFBkIlVJiXsmwwtXETFNVk54I3UK3bAOo--E0eLjSsebWhtkHGmMca5kLcBf0MUJMPp4kCC_r0PIOyE-u8KsWlxv2XN6BaIJkOsObrrNrOq7ZJLeVx_1AvBUzsVCKdEEkS9RmCSzOjrCFY1BY7Cmfl-Wb4joXqg3iRvkikdUav29582WBLwznAlTJbVbQUxhWID96IQlMWuj2tERUsrXjGl4SCVlaszDsG-cRYKAHoAmZm1UJq-jH9fTMXUcelejqg1x3BFE0ebfinw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1155257fca.mp4?token=tgXq8hKlI9T_bwKe1R-a4CbLxsl60uYsQFYqMzQno2ZI5EAWtSJV6pLfBrS3INaU_Qe_pqxmFBkIlVJiXsmwwtXETFNVk54I3UK3bAOo--E0eLjSsebWhtkHGmMca5kLcBf0MUJMPp4kCC_r0PIOyE-u8KsWlxv2XN6BaIJkOsObrrNrOq7ZJLeVx_1AvBUzsVCKdEEkS9RmCSzOjrCFY1BY7Cmfl-Wb4joXqg3iRvkikdUav29582WBLwznAlTJbVbQUxhWID96IQlMWuj2tERUsrXjGl4SCVlaszDsG-cRYKAHoAmZm1UJq-jH9fTMXUcelejqg1x3BFE0ebfinw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا شب‌ها انگیزه برای تغییر زندگی داریم اما صبح، پشیمون می‌شیم؟
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696051" target="_blank">📅 12:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696050">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
«رشیدی» عضو هیئت‌رئیسه مجلس: استیضاح آقای عراقچی، وزیر امور خارجه، توسط یکی از نمایندگان در سامانه ثبت شده، اما هنوز به هیئت‌رئیسه ارجاع نشده است
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/696050" target="_blank">📅 12:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696049">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0d330ffa.mp4?token=DoZKjqZ-ILDgNvTgqAFqCme7dE4S_IPItqhyP5X0nsPRyNDUxCEqxBTQT1WB_ebappiHIg41EiPgA5_tdHk3nQAJYKURvHZkT8dc71dFucEvqixHGIXtffWUgBLxpdvOrECUhCQGmgmcU9ZevERPc1kp5LrsyX1KIDFW8ou4rsRMBTadQPJubRxJz4q9zvmkqIE4n8_9GKhSs16y0fU0ojzvlPgEwbplLus018LAji_h0ju3bVs6UCBPnrWXTZMM0ZTUz4XrtLvQ84fhkTFfFy6KVsW7mp2GqDeVjJ6OK0SiusDg6liPjdWD5KwHR5GgT2Nz_K_cS6InAPLeZg-PQl_ZeTiH5tDMyEV0NVv4XsbazoMRdoWouUn8atc05bkDsB_1KGyfULlpoeSZ5uFKu5ZE4rqXuWMEReM4cA4gTeyCqO-tz5cMSTUhC6489NXHwySkrt94jJazPi-8jl2bJPwYxBHWwYY2GmAE_953zK4ucjReql_Z-ioGqjj0CCbHQn9pwaUkiCqSn58RhFgkWdVHQUwoAw6LgiLIYOWVU4S5GFj5ARSTNUtjebnMD_I-MEc94hADInOXcKaFObvQw2mYvVPbU8Jwh3zrJr8EYgZqULsz6dMiiTc0l1wVWmxlrfhhk5eBNzrJsxGqUGL7txnFaRpajIjN1v_7-iAWR9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0d330ffa.mp4?token=DoZKjqZ-ILDgNvTgqAFqCme7dE4S_IPItqhyP5X0nsPRyNDUxCEqxBTQT1WB_ebappiHIg41EiPgA5_tdHk3nQAJYKURvHZkT8dc71dFucEvqixHGIXtffWUgBLxpdvOrECUhCQGmgmcU9ZevERPc1kp5LrsyX1KIDFW8ou4rsRMBTadQPJubRxJz4q9zvmkqIE4n8_9GKhSs16y0fU0ojzvlPgEwbplLus018LAji_h0ju3bVs6UCBPnrWXTZMM0ZTUz4XrtLvQ84fhkTFfFy6KVsW7mp2GqDeVjJ6OK0SiusDg6liPjdWD5KwHR5GgT2Nz_K_cS6InAPLeZg-PQl_ZeTiH5tDMyEV0NVv4XsbazoMRdoWouUn8atc05bkDsB_1KGyfULlpoeSZ5uFKu5ZE4rqXuWMEReM4cA4gTeyCqO-tz5cMSTUhC6489NXHwySkrt94jJazPi-8jl2bJPwYxBHWwYY2GmAE_953zK4ucjReql_Z-ioGqjj0CCbHQn9pwaUkiCqSn58RhFgkWdVHQUwoAw6LgiLIYOWVU4S5GFj5ARSTNUtjebnMD_I-MEc94hADInOXcKaFObvQw2mYvVPbU8Jwh3zrJr8EYgZqULsz6dMiiTc0l1wVWmxlrfhhk5eBNzrJsxGqUGL7txnFaRpajIjN1v_7-iAWR9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📣
سه رویداد تخصصی، همزمان در نمایشگاه بین‌المللی مشهد
از ۱۴ تا ۱۷ مهرماه ۱۴۰۵ برگزار می‌شود:
🔹
بیست‌وششمین نمایشگاه تخصصی صنایع غذایی
🔹
هفتمین نمایشگاه صنعت شیرینی، شکلات، نان، قهوه و چای
🔹
چهاردهمین نمایشگاه تخصصی چاپ و بسته‌بندی
با حضور تولیدکنندگان، فعالان و متخصصان این صنایع
📍
نمایشگاه بین‌المللی مشهد
🏢
برگزارکننده: شرکت فراگستر تجارت بهداد
📞
05138924743
منتظر حضور گرم شما هستیم.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696049" target="_blank">📅 12:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696048">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHjdevff32uMS1NKf-aaiwpTWec6n2FTnsjDTxUP99E59ZI4qmq48togRMmm9_wIG4R39FKhThuqmE9B308QujOJ1U7sUDuA91PRGteQJI6W0raf3BlQExhW8XBmdYP04kCinqhT7eHM60BpjaOKSMHjS9b6SStyeioZFlfEM01nGhrXBmnjeXGtvVdygs9mxl7gF8AvR2TkvRQX_8OpapF5x0lgt9CdvmHqM08klKIL5eZWT5jakwla6CbiPqY890HXjtSP6alPbfY91FmTv56QMTMFyghIYwbtlNy-6tMD7Nr7QVoWv3_kLhcir1m8TVcx2zQVoylxAPGKH5kKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید طلا و نقره‌ی بدون کارمزد با پشتوانه‌ی واقعی!
🪙
✨
🤩
با اسنپ‌سرمایه، فرصت خرید طلا و نقره‌ ی بدون کارمزد رو تا ۱۷ مهر از دست نده.
😎
اگه قراره سرمایه‌گذاری کنی، این بار با دستِ پُر شروع کن
چون
اسنپ‌سرمایه، جفت دستش پره!
💛
🩶
‼️
تا ۱۷ مهر، فرصت خرید بدون کارمزد رو از دست نده.
https://l.snpy.ir/tmgfr
https://l.snpy.ir/tmgfr
https://l.snpy.ir/tmgfr</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/696048" target="_blank">📅 12:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696047">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سخنگوی قوه قضائیه: بی حجابی جرم است برخورد می کنیم
🔹
بی‌حجابی به موجب قانون جرم‌انگاری شده‌ است. قوه‌ قضائیه ضمن تأکید بر اقدام فرهنگی در این حوزه، برای برخورد با هنجارشکنی وارد عمل شده‌ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/696047" target="_blank">📅 12:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696046">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeKdDvQuZUn94b_vM9q7JPhEjGZmHb3pfoUN2w8Ls7mdcOtasNilIvHxprfCqEK2xhSszfW-7oq1q8CbJG7Q9LtRVIoTYiE8hOjOMmZBUTejuEFIX4zqiD8_mjjAkPQgJxWcjFl8Xx3U0_YqNVV2nav7whIEl45yFAC6_VLSkYcFPWywkUvq0HJeTVsmavuZestbfks5SIcv59WIeKl3Llvyd3PdFHQiyoVfOQ4GMCvFkvz6rNLuaVGo1INiqdEZDfzf2CW2LuvC4dZqT2ojjmkTkHPSAWaoCp8geyeWhx21xcSK6Ou6uzIGXRomQP4bmHUPuIx0hUrZC-cPmH5Bvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/696046" target="_blank">📅 11:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696045">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
بالاخره زنی که ۱۰ شوهر خود را کشته است، قصاص می‌شود؟
🔹
کلثوم اکبری، متهم به قتل ۱۰ مرد سالمند، در دادگاه کیفری یک مازندران به ۱۰ فقره قصاص نفس و بابت ۱۰ فقره شروع به قتل به ۱۰ سال حبس محکوم شده است.
🔹
او متهم است طی حدود دو دهه با مسموم‌ کردن یا خفه‌ کردن…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/696045" target="_blank">📅 11:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696044">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
جانشین فراجا: برای ورود به اماکن انتظامی حتما باید حجاب داشته باشید. آقایانی که شلوارک می‌پوشند و لباس‌های ناهنجار به تن دارند اجازه ورود به اماکن پلیس را ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/696044" target="_blank">📅 11:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696043">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سخنگوی
قوه قضائیه: پرونده علی ضیا به دلیل توهین به رئیس‌جمهور تشکیل نشده است
🔹
علی ضیا در دو مورد شکایت داشته یکی شاکی خصوصی دارد و در دیگری پرونده توهین به مقدسات است که جنبه عمومی دارد که قوه قضاییه ورود کرده و ارتباطی با توهین به رؤسای جمهور نیست‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/696043" target="_blank">📅 11:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696041">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه ارتش جمهوری اسلامی ایران " آجامدیا"</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1cf08488.mp4?token=TuXi7BcVJ3C_6VeO-je0BjW118i48QwsIoK4NCOWGqGa8zFmpkz6DaCk_MGjMSMRu63g1v-H26cZpaSq50QjlXcuvecMnxnsOH-QwWLUFIwcXRPU4yyUtIf5Q0ib8FQVTBFzjvWteFcUK8ZFdlLGNQJrHGvjMha3_HDnogWK2P7rItwdamXmOkqhBKpAsYhjBqB2mnK3PCnpiiaW8Gjw08uTBzy9RXMpYWSLdeyO1CnHsBeZe8B_Dc3A6MthWXPKsLRe2YybJPX1_wolGzGpHKCIqDgwiQ3ZWrZvIqRmVc9YOgvN0iVu2riraUKfA8CbDB6xdObyDrl61CZF48q4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1cf08488.mp4?token=TuXi7BcVJ3C_6VeO-je0BjW118i48QwsIoK4NCOWGqGa8zFmpkz6DaCk_MGjMSMRu63g1v-H26cZpaSq50QjlXcuvecMnxnsOH-QwWLUFIwcXRPU4yyUtIf5Q0ib8FQVTBFzjvWteFcUK8ZFdlLGNQJrHGvjMha3_HDnogWK2P7rItwdamXmOkqhBKpAsYhjBqB2mnK3PCnpiiaW8Gjw08uTBzy9RXMpYWSLdeyO1CnHsBeZe8B_Dc3A6MthWXPKsLRe2YybJPX1_wolGzGpHKCIqDgwiQ3ZWrZvIqRmVc9YOgvN0iVu2riraUKfA8CbDB6xdObyDrl61CZF48q4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دانشگاه‌های افسری ارتش دانشجو می‌پذیرد
🔹
ارتش جمهوری اسلامی ایران از طریق کنکور سراسری جهت تکمیل کادر افسری خود از بین جوانان علاقه مند و مستعد برای تحصیل در رشته‌های پزشکی، خلبانی، مهندسی برق، مکانیک، رایانه، هوافضا، فرماندهی و کنترل سامانه‌های نظامی، مدیریت و ... دانشجو می‌پذیرد.
👈
شرایط و ضوابط عمومی و اختصاصی و امتیازات داوطلبان در وبگاه زیر قابل مشاهده است:
🌐
https://GOZINESH.AJA.IR
👈
جهت آشنایی با دانشگاه‌های افسری ارتش به سایت مسیر افتخار به آدرس زیر مراجعه نمایید:
🖥
https://masire-eftekhar.ir
📱
@aja_media
zil.ink/ajamedia_ir</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/696041" target="_blank">📅 11:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696040">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وزارت اطلاعات: ۳ هستۀ عملیاتی گروهک تروریستی-تکفیری در جنوب‌ شرق (شهرستان‌های ایرانشهر، سرباز، سراوان و زاهدان) منهدم شدند
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/696040" target="_blank">📅 11:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696038">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy20kl668Qk9TUitXjIQEu6kwt7pR6BGwvvmTQqJVw6Pdx9GYH1woYsxvPpDlnbGUehJ0PYJFgBO45jyklNDmjTtWfFBP2cVzD8LuQT-p1RFQUCmxmfluP5O_WZmTpIoyhFABmMSLx6XhdYEyzkuNYwwYx9-e62SpSwUSVNbGnCYfIhWwQkinbPUC0A7H2ISvq7Kz7sXOQevbBJSfM2_aQbgY7NahWoBHmCDdUN0P7HwJTojyKwwwtdNVR205OihFPOiY9SBXD1znecpEMGSKVQEBFs9rQgeOFzpllBDbUyWlh0oS8E7_YlzHrL20fGRjpBzyclxR5AREDkTQTy6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ شماره ضروری پرکاربرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696038" target="_blank">📅 11:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696036">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
با تصویب مجلس؛ مصاحبه اتباع ایرانی با رسانه‌های معاند ممنوع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/696036" target="_blank">📅 11:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696035">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سخنگوی قوه قضاییه: ۷۱ پرونده در خصوص تراستی‌ها تشکیل شده و ۲۶ همت از وجوه دریافت شده و استرداد مجرمان با همکاری پلیس بین‌الملل در حال پیگیری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696035" target="_blank">📅 11:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696034">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ماجرای طرح هدیه ماهانه ۳.۵ تا ۴ میلیون تومان به نوزادان متولد ۱۴۰۵ تهرانی چیست؟
زاکانی، شهردار تهران:
🔹
اعتبار خرید، خدمات فرهنگی و سلامت و بهداشت به نوزادان متولد ۱۴۰۵ تهرانی تحت عنوان طرح «چشم‌روشنی» اختصاص داده‌ شده‌ است.
🔹
اعتبار پایه این طرح ماهانه ۳ میلیون و ۵۰۰ هزار تومان است که در حساب شهرزاد مادران شارژ می‌شود. از این اعتبار، ۲ میلیون و ۵۰۰ هزار تومان برای خرید کالاها و اقلام ضروری، ۵۰۰ هزار تومان برای خدمات فرهنگی و ۵۰۰ هزار تومان برای خدمات سلامت و درمان اختصاص دارد. برای مادران متعلق به سه دهک پایین درآمدی، ۵۰۰ هزار تومان اعتبار اضافه در نظر گرفته شده و مجموع اعتبار ماهانه آنان به ۴ میلیون تومان می‌رسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/696034" target="_blank">📅 11:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696032">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
قزاقستان، ازبکستان و قرقیزستان به‌دلیل احتمال شیوع طاعون در روسیه، مرزهایشان با روسیه را بستند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/696032" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696031">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
فرایند پرداخت وام یک میلیارد دلاری روسیه به ایران نهایی شده و منتظر اعلام شماره حساب از سوی ایران برای انتقال وجه است
/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/696031" target="_blank">📅 11:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696030">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9372f4c05e.mp4?token=PjGisQQLO4q13ESy3frfvLWeTW3hto6aqCLThZbLL8jMTRKduynjNNsAli4usNBzzQ-lyyEnlbTmYsngpTgCmQOX7nemX6BQ4rstra5h1VCdBOk9TVr0tdbGSWLpPwKQgAGl_nJwBi0uyCTHR6XwPrfxZ8kka6RIbYCX05_4ao6sQJ34xYZthNMhv0EBmWtjq_LYE0AsPku6Kqeknb-3y_75l0KU5_dNKQpdtdMm3FS12AKO-_ikggEFUzWiB1Uv4TZHdAiEmPQDJuFaToWZMkq2MmwuyfbfbAK9qs7m-3CcerV8H6vJDnuu0KbhEWmmIX7P1mKp_o96MBNDzsQ0pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9372f4c05e.mp4?token=PjGisQQLO4q13ESy3frfvLWeTW3hto6aqCLThZbLL8jMTRKduynjNNsAli4usNBzzQ-lyyEnlbTmYsngpTgCmQOX7nemX6BQ4rstra5h1VCdBOk9TVr0tdbGSWLpPwKQgAGl_nJwBi0uyCTHR6XwPrfxZ8kka6RIbYCX05_4ao6sQJ34xYZthNMhv0EBmWtjq_LYE0AsPku6Kqeknb-3y_75l0KU5_dNKQpdtdMm3FS12AKO-_ikggEFUzWiB1Uv4TZHdAiEmPQDJuFaToWZMkq2MmwuyfbfbAK9qs7m-3CcerV8H6vJDnuu0KbhEWmmIX7P1mKp_o96MBNDzsQ0pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طولانی‌ترین شاهکار نقاشی مینیاتوری جهان با ۲۱ متر طول، ۵۰۰۰ نماد از ۱۹۳ کشور و حاصل ۲۱ سال تلاش هنری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/696030" target="_blank">📅 11:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696028">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_7Pgp74Bo6qtCLktoZCem75CvX3U1J5Ghxmy6mVgJ2waFcuXFLBRm4aG9mNkjxhfoIlK8oYi9HIN_EnuA-r4Pas8bgW42txsjSePOWdNSf4_qmq0j3Helfq4rl2QA91r85PQGnJhmxca0cGvwCmANB6vq4j7iJcodQry3lMKjii0y43e6DZx0SzrvNx6q7Mo-jumVEJUceKMUUL3oeadEz9hBXoMRN8m923QZORXKuYXEpjJwsDW6COg-M8N12OoRSx2_d6TcHgjHmY6bh1iY6QRpt2juj_9IzRHmjdfz309pmnaSJWyqcLxhNS8BrTmfcCXkiEImdFc8nqR8xe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط ویژه تأمین اعتباری آهن‌آلات اعلام شد!
🔹
با اجرای طرح ویژه تأمین اعتباری آهن‌آلات،
سازندگان، پیمانکاران، شرکت‌های عمرانی و مجریان پروژه‌ها
می‌توانند بدون نیاز به پرداخت کامل و یکجای هزینه خرید، مقاطع فولادی موردنیاز پروژه خود را به‌صورت
اعتباری با چک (با ضمانتنامه بانکی) یا LC
تأمین کنند.
🔸
این طرح با هدف
حفظ نقدینگی پروژه‌ها و مدیریت بهتر هزینه خرید آهن‌آلات
اجرا شده و امکان تأمین اعتباری برای متقاضیان واجد شرایط فراهم شده است.
❌
ظرفیت استفاده از طرح محدود است
❌
👈🏻
برای بررسی شرایط، مدارک موردنیاز و نحوه استفاده از اعتبار، درخواست خود را ثبت کنید:
🔗
ثبت درخواست تأمین اعتباری آهن‌آلات</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/696028" target="_blank">📅 11:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696026">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f90ae5beb.mp4?token=m1H6jQ0lhz9as3EJfjYWag7D56NtErmKiAbL5rs6d0i7tYM_F3NHCYvF8wTEvnRXi7g2khKnPOK3NqedMKD8azIGLF5fLD6jg258b8Zc_BAEiLHEce9BNEmUKV6mrp96vccx-t_3x56SCqLco1oZ0F_VhIaLBtkEM-4DOl_5lYgs5JrtTN042vZoaMU0VWsVTtPvkz6dfuPOXr0eQ9d4QuEwaO9ABWFzImkFWyrln6R43Xp4r_uoW2Xd89jY_p8PDuEueG6E6AkzcWw-4jUSZRv6bnlLJHxNEecQPhKvNLa9a6Sjd957DJHp1HIq7834-KFyFeSsIaZiSSgtViwP7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f90ae5beb.mp4?token=m1H6jQ0lhz9as3EJfjYWag7D56NtErmKiAbL5rs6d0i7tYM_F3NHCYvF8wTEvnRXi7g2khKnPOK3NqedMKD8azIGLF5fLD6jg258b8Zc_BAEiLHEce9BNEmUKV6mrp96vccx-t_3x56SCqLco1oZ0F_VhIaLBtkEM-4DOl_5lYgs5JrtTN042vZoaMU0VWsVTtPvkz6dfuPOXr0eQ9d4QuEwaO9ABWFzImkFWyrln6R43Xp4r_uoW2Xd89jY_p8PDuEueG6E6AkzcWw-4jUSZRv6bnlLJHxNEecQPhKvNLa9a6Sjd957DJHp1HIq7834-KFyFeSsIaZiSSgtViwP7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آتش‌سوزی در فرودگاه ریاض در پی حمله موشکی یمنی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/696026" target="_blank">📅 10:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696025">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf49084b8.mp4?token=k-TcsxizGpeaArm3uGj3Uot11HDPkR2iwgnh04H8l6Ia6Ql1EKSjq-ltF0S9RwVdY2plp9YTm6SXjlbOgf5zzy_Bt-g3aD4rYqs3HAtQpKDgsx8LE3fdLTz6Dey_ClyprcSWWcpdYsPOBI8z0i2Bk7HLtAkhxQL2aguDAP0lt8GbQwoC1Wvpm9HUkYaGCoVOitYfbxdSIVA8E7pQlyPajZnP5VmbeOdmZ-lUz7rCWju5EZubhf1vT_wT9PFHgoEVWoXPIBf33vJTaptrUHN5Fqn4YWM6_ySIgAFFkvcpOOyQqXw2kJzNQ_t3ztH5ZU7COtA7SEDO4046fg4O69Gb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf49084b8.mp4?token=k-TcsxizGpeaArm3uGj3Uot11HDPkR2iwgnh04H8l6Ia6Ql1EKSjq-ltF0S9RwVdY2plp9YTm6SXjlbOgf5zzy_Bt-g3aD4rYqs3HAtQpKDgsx8LE3fdLTz6Dey_ClyprcSWWcpdYsPOBI8z0i2Bk7HLtAkhxQL2aguDAP0lt8GbQwoC1Wvpm9HUkYaGCoVOitYfbxdSIVA8E7pQlyPajZnP5VmbeOdmZ-lUz7rCWju5EZubhf1vT_wT9PFHgoEVWoXPIBf33vJTaptrUHN5Fqn4YWM6_ySIgAFFkvcpOOyQqXw2kJzNQ_t3ztH5ZU7COtA7SEDO4046fg4O69Gb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قوه قضاییه: جرم منتسب به رسایی مربوط به پیش از نمایندگی است؛ مصونیت شامل آن نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696025" target="_blank">📅 10:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696024">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8169d52cc4.mp4?token=JaZhvIwb7UELaMDDXbMpTeig9zhvQbdDAdZibxeJytp2Ru_CsY3Zsju97akXn6x_06uYBpvjO02b0X9hA1LY9OaMc7kTwTnHjHB911rJiJdFov1nxjNlZkyoot_CKCJml5e4mSuQsiHmKWh_vYC5L1_-j6dN_tQXM5QwYbdht_eZ9y9jMG-Z0w_5MLVgahxxXjb9yo6FffJ-i8OFYWh8nu49yhcEpPNEmeBk6ydI_2zQSFDSdPBEYrCUZuZBW1NAtPoLLBKlBzFBqrKpU_bv_MY5qlptDiG_Tt1Lj_FfnFsfqOFRODmuHdRGjqMPnudYTn5Vn9OZntruNgY1qhGwr0xPmoLFSiCSjpNym8EUocnvBwJO0qT1vXvVSFqkZWBHl855P3fSuXEle8nqcYz2KCCwbJzgaoJ8j2DKmGTW6kAx6CsVJQA9-VHj55Nl6f0MSomqOXdmTLwwGNsMmBLa3tzvRp8CiU2kmAPmib59AYCnyYuATLoQGCrSgGkVxK55UFMuv_GjKC4cMRSTrv6qbcaIirfG1JPwq0UX9DFI6vtPecIU9ZCVQUPDD8DenvAhveCnxk04DnG58bAMlV8fRf4j9b3YaBzfmwBuhwEvsWWY1PHib8y7jIGj0mJxkd-L2w85dHTtw5ck3Jh0gUs2-I7SaViyOAWLRNpA2l3hSR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8169d52cc4.mp4?token=JaZhvIwb7UELaMDDXbMpTeig9zhvQbdDAdZibxeJytp2Ru_CsY3Zsju97akXn6x_06uYBpvjO02b0X9hA1LY9OaMc7kTwTnHjHB911rJiJdFov1nxjNlZkyoot_CKCJml5e4mSuQsiHmKWh_vYC5L1_-j6dN_tQXM5QwYbdht_eZ9y9jMG-Z0w_5MLVgahxxXjb9yo6FffJ-i8OFYWh8nu49yhcEpPNEmeBk6ydI_2zQSFDSdPBEYrCUZuZBW1NAtPoLLBKlBzFBqrKpU_bv_MY5qlptDiG_Tt1Lj_FfnFsfqOFRODmuHdRGjqMPnudYTn5Vn9OZntruNgY1qhGwr0xPmoLFSiCSjpNym8EUocnvBwJO0qT1vXvVSFqkZWBHl855P3fSuXEle8nqcYz2KCCwbJzgaoJ8j2DKmGTW6kAx6CsVJQA9-VHj55Nl6f0MSomqOXdmTLwwGNsMmBLa3tzvRp8CiU2kmAPmib59AYCnyYuATLoQGCrSgGkVxK55UFMuv_GjKC4cMRSTrv6qbcaIirfG1JPwq0UX9DFI6vtPecIU9ZCVQUPDD8DenvAhveCnxk04DnG58bAMlV8fRf4j9b3YaBzfmwBuhwEvsWWY1PHib8y7jIGj0mJxkd-L2w85dHTtw5ck3Jh0gUs2-I7SaViyOAWLRNpA2l3hSR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندیشمند برجسته آمریکایی: ایرانی‌ها بیش از حد باهوش‌اند، تصور تسلیم آن‌ها با حمله نظامی، مُضحک است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/696024" target="_blank">📅 10:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696023">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
عضو کمیسیون بهداشت: داروها به لحاظ کمیت و کیفیت افت کرده‌اند
حسین عبدلی، عضو کمیسیون بهداشت مجلس:
🔹
دلیل جنگ و تحریم در مضیقه هستیم و کمبود دارو و مواد اولیه داریم و داروها به لحاظ کمیت و کیفیت افت داشته‌اند.
🔹
واکسن آنفولانزا به میزان کافی برای افراد دارای نقص ایمنی در کشور موجود است و همه افراد نیاز نیست بزنند.
🔹
حذف ارز ترجیحی برای بسیاری از اقلام دارویی، باعث افزایش قیمت‌ها در بازار شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/696023" target="_blank">📅 10:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696022">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbqEaYEYGMoL-2c9agkLjJeUP-5qSbOtYbdTtKVGaCBAsqcdBXRDmrFDuIrXTz8uauWRopd6BP1f6qvtNo18FVNrg3s-BU8WcXbaf3GYPTn-4doETvW1B_qT4URAQez8QSOw1F1KHuJUSbq2PMLSB5eteO3eR5vLm8JlE2_QYYUHz1oZVZdFuHrPgc0U9PB_VmenLoMtkyKpobvVv5EbYUZ3aVqa9N9CdCJllER_dioIvWGEZlIS1r-dDyAbyUS6kTGPsAKomuAzal7-EQ6csoWxduWvL_erNrnPT6r_QYaYc9pQV9R-ofRI-1gOMR88nHMc_dDhPZkFOwnJ83OlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی سپاه یک فروند شناور اماراتی را که قصد عبور از آبراه جنوبی تنگه هرمز داشت، وادار به بازگشت از مسیر خود کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/696022" target="_blank">📅 10:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696021">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ff18f9c9.mp4?token=u_b4jrvlKwDsF5twhSUCmQVzfd631IKCi0d0ppgd5UraQXUgdbP9lzLL2V-XOmCN8saZbGhFSoBqQX6mfkg1_wj7f8RheEw2qw5Sfl2l6dOsieAm87mCHW1DliNt8biVrO2aiYGFNpkGGcEtIA_Brc1vaJiyVnA-LgyekNC7aam39RgoFhVf9yvlBENiWJBh6iJLlxUmcHXoB2hTeW7mpUXt0_cSLXVnsmSfSP5gPlW7vIFTSMb_9T-gXu46oIWWlvKj3AIIAD7gIydhS-r3Fgw4y3XaPVbRRFbNhtRmNL6xKi8FaGDX9QSY-YFKz6Yz4BGisks26mo3HpbEGkg0ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ff18f9c9.mp4?token=u_b4jrvlKwDsF5twhSUCmQVzfd631IKCi0d0ppgd5UraQXUgdbP9lzLL2V-XOmCN8saZbGhFSoBqQX6mfkg1_wj7f8RheEw2qw5Sfl2l6dOsieAm87mCHW1DliNt8biVrO2aiYGFNpkGGcEtIA_Brc1vaJiyVnA-LgyekNC7aam39RgoFhVf9yvlBENiWJBh6iJLlxUmcHXoB2hTeW7mpUXt0_cSLXVnsmSfSP5gPlW7vIFTSMb_9T-gXu46oIWWlvKj3AIIAD7gIydhS-r3Fgw4y3XaPVbRRFbNhtRmNL6xKi8FaGDX9QSY-YFKz6Yz4BGisks26mo3HpbEGkg0ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قوه‌قضائیه قسمتی از کمک‌هایی [ترکش‌هایی] که آمریکا برای کودکان مینابی فرستاده بود را به نشست خبری آورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/696021" target="_blank">📅 10:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696020">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
محمدباقر خرازی پس از یک ماه بازداشت با صدور قرار وثیقه و پذیرش آن آزاد شد/تحقیقات مقدماتی پرونده ادامه دارد و هنوز کیفرخواستی صادر نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/696020" target="_blank">📅 10:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696019">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
مدیرکل فرودگاه مهرآباد: ممنوعیت پروازهای نیمه شب در فرودگاه مهرآباد برداشته شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/696019" target="_blank">📅 10:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696018">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658e94cd22.mp4?token=c8-IUAdjo-33tnZIweR2qGVx0HfPwRZfnMa2rrRVhfxvRxPC4ZWGRCNLMWkqV309dDFGXYsz-7xfthJQTfqc3IXhv9a8OihgEKB-oLbrxx-WHE-0i7yMJFGRcL4gmj3y5BxIBfZISIu40ZSZh2RHQfe3_K-fvzkNsHwXMBYpRsmhWNR6t_-HyOA1bAkY8fLn8VwhLXvv6QJ5oFBgYRJCgrN8IWfuEYAseG5DqewopIM005Km-9PNw7zIWNakaX6LWkOyr8nGRp4TWWjAH7z9LIeTUEyzvz3vzZgsr4qgHHf90gTONyv1X8Lm0jZ9XSDfEztOstFN8vIIbVj2WRAO0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658e94cd22.mp4?token=c8-IUAdjo-33tnZIweR2qGVx0HfPwRZfnMa2rrRVhfxvRxPC4ZWGRCNLMWkqV309dDFGXYsz-7xfthJQTfqc3IXhv9a8OihgEKB-oLbrxx-WHE-0i7yMJFGRcL4gmj3y5BxIBfZISIu40ZSZh2RHQfe3_K-fvzkNsHwXMBYpRsmhWNR6t_-HyOA1bAkY8fLn8VwhLXvv6QJ5oFBgYRJCgrN8IWfuEYAseG5DqewopIM005Km-9PNw7zIWNakaX6LWkOyr8nGRp4TWWjAH7z9LIeTUEyzvz3vzZgsr4qgHHf90gTONyv1X8Lm0jZ9XSDfEztOstFN8vIIbVj2WRAO0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درصدگیری به آسان‌ترین روش ممکن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/696018" target="_blank">📅 10:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696017">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e25a1611a.mp4?token=B-hcvZNEjJ7TJUxQQvxhJneeMxikLOXsa75142ogordISY_nizBIrLr9S8Dz7xosRhZWBiEVNQmJliaeDpsTY4c3FTyDFMMmhrJSiiaZC4aBvZEgiCch1kbzrxnHYYTXrxbuEXAQQwmKNjk-vgeU1aFE5PRAlkAUzqrTtNfmdcNN6ij40iitqTdo4CRs0f3zN0UnAEPeT_Laf2tysXAQKI9_kH3pErk-9l2yb2egPy4K5kTssqnuyiHOTSDL4ssbvEBKsqKsN0c5VxXccjfskq1eOlYhHiRtFdaQ59vkgRaYxC-LCsH3XLPXSYgFUIrb5_VoZLabvkssb26bu-TgtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e25a1611a.mp4?token=B-hcvZNEjJ7TJUxQQvxhJneeMxikLOXsa75142ogordISY_nizBIrLr9S8Dz7xosRhZWBiEVNQmJliaeDpsTY4c3FTyDFMMmhrJSiiaZC4aBvZEgiCch1kbzrxnHYYTXrxbuEXAQQwmKNjk-vgeU1aFE5PRAlkAUzqrTtNfmdcNN6ij40iitqTdo4CRs0f3zN0UnAEPeT_Laf2tysXAQKI9_kH3pErk-9l2yb2egPy4K5kTssqnuyiHOTSDL4ssbvEBKsqKsN0c5VxXccjfskq1eOlYhHiRtFdaQ59vkgRaYxC-LCsH3XLPXSYgFUIrb5_VoZLabvkssb26bu-TgtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ولاگ وایرال شده از یک پسر ایرانی که از یک روز مدرسه رفتنش در آمریکا ویدئو گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/696017" target="_blank">📅 10:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696016">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f416b2a7bc.mp4?token=g-1zr18shdg6GDnh5tqMYgse93GTqCXlAvEs1d8oUTojt0Vn5x-nxwbzksgHfI8uRCiIRTzBoYjFdDmwdJWsc4RRnhncR4yGK0Ov7KOEYxC0Mi22xTgYPGwE9wn_vn_UGH1DgwBzO3OGsGpB3nwF58L_u7LHZXReycXMq8TIy_BxCVQ8wbiY_Ao9b_Ucxo_-v7TLQWSMJq865WLJxUa4AbLK4ITyV7ff1I5RYCTDsadrF48ypjz2gB7Y3okY-BTTcpwHBig-e2kW5-pJk3AtuM275ryq1DyJA_PDVlbAeNz1U6gdVDvqzcXBzISuFPoG-6swbH1YKNBeJfHD-xQTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f416b2a7bc.mp4?token=g-1zr18shdg6GDnh5tqMYgse93GTqCXlAvEs1d8oUTojt0Vn5x-nxwbzksgHfI8uRCiIRTzBoYjFdDmwdJWsc4RRnhncR4yGK0Ov7KOEYxC0Mi22xTgYPGwE9wn_vn_UGH1DgwBzO3OGsGpB3nwF58L_u7LHZXReycXMq8TIy_BxCVQ8wbiY_Ao9b_Ucxo_-v7TLQWSMJq865WLJxUa4AbLK4ITyV7ff1I5RYCTDsadrF48ypjz2gB7Y3okY-BTTcpwHBig-e2kW5-pJk3AtuM275ryq1DyJA_PDVlbAeNz1U6gdVDvqzcXBzISuFPoG-6swbH1YKNBeJfHD-xQTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در تأسیسات آرامکو در جده در پی حملۀ نیروهای مسلح یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/696016" target="_blank">📅 10:15 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
