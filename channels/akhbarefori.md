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
<img src="https://cdn4.telesco.pe/file/PDgrB4vGEfeYGq1eUfOS8P1nw22r5D6RAEDR2s8FAEq9ltpQtIvnFbdb4gZ3wDVVpmMn8WUjo503Z9TxtGJPd8YIJmZbN6X66I9LydBfwHSupY1KPXsx6ElPCyvndMtseNlgAga4hxgVjxMOfY3XDrR-X4mxM0PHbTvvb-0kjq_mKalwX9OTIcOo3TSmN55d4mqdtNyEbo0ZCEVbRb_e2nchR2ojI6_Kz1bn3SlXSdnENHL7j3k8F1r40Vqu6wYKbF8b0H9CTvw_pkdNwsBSRyKj0A9p0XCiv4pFq1hgb1P1lZ2QT8f0ZOV2qI1FhVE-8pHZaL0gRsq-25VBscbgbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 04:26:11</div>
<hr>

<div class="tg-post" id="msg-671655">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در سمنان
🔹
دقایقی پیش مردم در بخش‌هایی از سمنان صدای انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/671655" target="_blank">📅 04:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671654">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شنیده شدن صدای ۲ انفجار در خرم‌آباد
🔹
دقایقی پیش مردم در خرم‌آباد ۲ صدای انفجار را در این شهرستان شنیدند.
🔹
هنوز محل دقیق و منشا این انفجارها مشخص نیست و تاکنون مسئولین استان در این خصوص اظهار نظری نداشته‌اند.
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/671654" target="_blank">📅 04:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671652">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79545378d8.mp4?token=j08VSyMXJQ4gUonBaJFhyJoacG8xN3XT7OImzeccvctyZKdZBsgHQVjfbqD8UMw4yK1w1q1bp6RvQ3NhzGwa19-I2-uCqfRp9X3qPGIsbSAjRCXMznqUktDuKhWzkDE0xY3AxhRzrbCcTXfnRBqtvHCCoklUTfgJKYKl0VF1xpPYRPZs9myN96z-LQPifcG4kmy04J5WE4yeYcddf5nWLiwcgINumgwH2t9K-WPGFyAEk36pvyCTKNvTPgcqRemB1bSUdS0MTIRshkWXDR6Fe0bSg2N82qdpNYQXTc3Wh5PD-RFe7bMvL-k0P9yRxBtYDrIj-S5e5XMpZUfRXojKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79545378d8.mp4?token=j08VSyMXJQ4gUonBaJFhyJoacG8xN3XT7OImzeccvctyZKdZBsgHQVjfbqD8UMw4yK1w1q1bp6RvQ3NhzGwa19-I2-uCqfRp9X3qPGIsbSAjRCXMznqUktDuKhWzkDE0xY3AxhRzrbCcTXfnRBqtvHCCoklUTfgJKYKl0VF1xpPYRPZs9myN96z-LQPifcG4kmy04J5WE4yeYcddf5nWLiwcgINumgwH2t9K-WPGFyAEk36pvyCTKNvTPgcqRemB1bSUdS0MTIRshkWXDR6Fe0bSg2N82qdpNYQXTc3Wh5PD-RFe7bMvL-k0P9yRxBtYDrIj-S5e5XMpZUfRXojKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار در پایگاه‌های آمریکا در اردن
🔹
منابع محلی می‌گویند که انفجارهایی در پایگاه هوایی «موفق السلطی» در منطقه «الازرق» رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/671652" target="_blank">📅 04:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671651">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
برخی منابع می‌گویند دقایقی پیش صدای انفجار در حوالی پارچین و پاکدشت شنیده شده است؛ این موضوع هنوز در دست بررسی است و تایید نهایی نشده است
🔹
گزارش تکمیل پس از ارزیابی‌ها متعاقباً اعلام خواهد شد. / تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/671651" target="_blank">📅 04:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671650">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حملۀ دشمن آمریکایی به خنداب
معاون استانداری مرکزی:
🔹
در ساعت ۳:۳۰ دقیقۀ بامداد نقطه‌ای در خارج از شهر خنداب هدف ۲ حملۀ هوایی دشمن قرار گرفته است.
🔹
اخبار تکمیلی متعاقبا اعلام خواهد شد.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/671650" target="_blank">📅 04:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671649">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
فعالیت پدافند در آسمان تهران برای مقابله با اهداف متخاصم / مهر  #اخبار_تهران در فضای مجازی
👇
@AkhbarTehran</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/671649" target="_blank">📅 04:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671648">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
یک فروند پهپاد MQ9 رهگیری و منهدم شد
روابط عمومی سپاه:
🔹
دقایقی قبل یک فروند پهپاد MQ9 دشمن در آسمان اندیمشک توسط سامانه نوین پدافند هوایی هوافضای سپاه رهگیری و منهدم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/671648" target="_blank">📅 03:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671647">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
فعالیت پدافند در آسمان تهران برای مقابله با اهداف متخاصم / مهر
#اخبار_تهران
در فضای مجازی
👇
@AkhbarTehran</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/akhbarefori/671647" target="_blank">📅 03:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671646">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
منابع اردنی از شنیده شدن صدای انفجار و آژیر هشدار در پی حملاتی از جانب ایران خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/671646" target="_blank">📅 03:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671645">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رسانه عراقی: شلیک مجدد موشک از کویت به ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/671645" target="_blank">📅 03:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671644">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
آسمان جنوب عربستان بسته شد
🔹
عربستان سعودی به‌دنبال حملات دوشنبه‌شب نیروهای مسلح یمن به فرودگاه بین‌المللی ابها، ناچار به تمدید تعطیلی سه‌روزه فرودگاه کلیدی جنوب خود شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/671644" target="_blank">📅 03:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671643">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c99c70405.mp4?token=HBRIxWR1hLLUjdN8tcbXKmCuvoI-MyPUq93NWiZ_TIGuFxsgg8YUnyTtLRQKAb45UsMl9ODbretR9etKKT7q-QK5lHowKSpXUdqf0NbtJZQ7S7gqri3mmZhYgx2YxqQYqd2E1kpbiFaVmFL17vbtt4ICHiJLIzHJUtvM4rNzRwDdobTskB61BoAXEcEXaN7mjMyOzo4VW8uSKd0G2OcffgUl6HQpF2QWFLL_lfOnXNm9eL3a4qTR-8qn1n6RcOr6GrwH3vbFWlMqSj-Uz2Ox4i7_jQvN5Jof3I57kHhSiz6vHf1qihyO2-1UNULCquMsLW1bIA_uA-y4l8i1ZidzEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c99c70405.mp4?token=HBRIxWR1hLLUjdN8tcbXKmCuvoI-MyPUq93NWiZ_TIGuFxsgg8YUnyTtLRQKAb45UsMl9ODbretR9etKKT7q-QK5lHowKSpXUdqf0NbtJZQ7S7gqri3mmZhYgx2YxqQYqd2E1kpbiFaVmFL17vbtt4ICHiJLIzHJUtvM4rNzRwDdobTskB61BoAXEcEXaN7mjMyOzo4VW8uSKd0G2OcffgUl6HQpF2QWFLL_lfOnXNm9eL3a4qTR-8qn1n6RcOr6GrwH3vbFWlMqSj-Uz2Ox4i7_jQvN5Jof3I57kHhSiz6vHf1qihyO2-1UNULCquMsLW1bIA_uA-y4l8i1ZidzEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت به مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/671643" target="_blank">📅 03:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671642">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ابراز نگرانی اسرائیل از فاصله گرفتن آمریکا از موضوع برنامه هسته‌ای ایران
المانیتور به نقل از یک منبع اسرائیلی:
🔹
همه چیز حول هرمز می‌چرخد. هیچ‌کس درباره مسئله هسته‌ای صحبت نمی‌کند. این بدترین نتیجه ممکن برای ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/671642" target="_blank">📅 03:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671641">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اصابت به مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/671641" target="_blank">📅 03:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671640">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حمله هوایی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/671640" target="_blank">📅 03:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671639">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
‌ منابع خبری از انفجارهای شدید در بحرین گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/671639" target="_blank">📅 02:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671638">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1d94e129.mp4?token=biTR6fcVDsY0SnqAD_UiBANsf0yGfuep0xSQMBKlfD50NqTUn6EvykuqDvIUT5Tb-u2KRb6BKsAplaD-3IFviA18VvTceqJr3oJR-r3wH3czOhozlV3hgrf0XmcuevqvJKhF5B5sil4mJRrahnrlbCS7MUNjbP8_bUrV6jgjtLotFD2rZFiZnmLKXAgIW3qRGOmW5MxaOr01ANcvVy8MAfVeEcTKqg0g80PKdJRptxfeRXacpQGLHmjparByYNyY0ApGkCyIUaNR35i0jLtAxnYn4_z0gHNTWwx09FE8NAPaRIJVMf4sqAdvHDb8UhAZk6T02zsQrjVJYhg-BtcoOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1d94e129.mp4?token=biTR6fcVDsY0SnqAD_UiBANsf0yGfuep0xSQMBKlfD50NqTUn6EvykuqDvIUT5Tb-u2KRb6BKsAplaD-3IFviA18VvTceqJr3oJR-r3wH3czOhozlV3hgrf0XmcuevqvJKhF5B5sil4mJRrahnrlbCS7MUNjbP8_bUrV6jgjtLotFD2rZFiZnmLKXAgIW3qRGOmW5MxaOr01ANcvVy8MAfVeEcTKqg0g80PKdJRptxfeRXacpQGLHmjparByYNyY0ApGkCyIUaNR35i0jLtAxnYn4_z0gHNTWwx09FE8NAPaRIJVMf4sqAdvHDb8UhAZk6T02zsQrjVJYhg-BtcoOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حمله هوایی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/671638" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671637">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا: تامین امنیت مسیرهای دریایی فقط با استفاده از ابزارهای نظامی بسیار دشوار است، زیرا هدف قرار دادن کشتی‌ها با استفاده از پهپادهای ارزان‌قیمت بسیار آسان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/671637" target="_blank">📅 02:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671636">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حمله هوایی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/671636" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671635">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پایگاه آمریکا در بحرین
🔹
همزمان با فعال‌شدن آژیرهای هشدار در بحرین، محل استقرار نظامیان آمریکایی هدف حمله هوایی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/671635" target="_blank">📅 02:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671634">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
استانداری هرمزگان: در ساعت ۲:۲۰ نقطه‌ای در حوالی بندرعباس مورد اصابت حملات دشمن آمریکایی قرار گرفت. / فارس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/671634" target="_blank">📅 02:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671633">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn_c3o5OQYKxdEnPyR1nclc_lTVW392u7SCAMUtfXhLjU90KSG6r0L3llROgbcGpcdRDns2XXZi9m3DBQcTOQamJAiLzkvl96cvUb6Jjt_pBuWGSHwr1e4HXLJN5zUIInmC0XovY5535wvVK7HeGS_l0rXuuOPKwfZm0O7IPDSS2LmEP_HdfbMbyTd7SnsIKD1SCNsJh51Dzf71y9kVobKjE2JayUjxuLSEf4cvkIFlFt5CWzDjC1w70FL2J-X3PTKh_XFAmzlKUyCOtUTpesDmbjAtck4rx6ngALWkPcisL5dnWDbxLIKRzkjcArB-RbIX0UdfUlLlq7M3R-fLqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به یاد سربازانی که دیگر بازنگشتند...
#بمپور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/671633" target="_blank">📅 02:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای خوک نجس در مورد آزادی شهروند آمریکایی توسط ایران
🔹
ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در زمان ریاست جمهوری جو بایدن به ناحق بازداشت شده بود، اجازه خروج از کشور را داد. او اکنون در خارج از ایران و در وضعیت خوبی به سر می‌برد.
🔹
ایالات متحده آمریکا از این حسن‌نیت ایران قدردانی می‌کند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/671632" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اصابت مستقیم حملات هوایی انتقامی ایران به منافع آمریکا در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/671631" target="_blank">📅 02:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تکذیب اصابت مجدد در قشم توسط استاتداری هرمزگان
استانداری هرمزگان:
🔹
در جزیره قشم بعد از اصابت پرتابه به کارخانه پودر ماهی سوزا برخورد جدیدی گزارش نشده است. شنیده شدن صداها احتمالا دارای منشاء دیگری بوده باشد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/671630" target="_blank">📅 02:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671629">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
مدیر بیمارستان شهید بقایی اهواز : پس از حمله تجاوزکارانه آمریکای جنایتکار به اطراف بیمارستان، موظف شدیم ۲۱۱ بیمار بستری را جابه‌جا کنیم
🔹
تمام تخت ها و بیماران بیمارستان شهید بقایی ۲ به علت وقوع شرایط اضطراری تخلیه شدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/671629" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671628">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c09abf4.mp4?token=BnqE-rOS2ggUpvAy-QHwEeo6oRn9edijje9g80qOk6KK7zKHBeqfOyaBrIJEtIsv3BERw5NpH5oe4NlkjD2sgTzs3Vme82Z_WxKzlFicGtJm9KeaCiTP7ZIx60SFOrEX4nSjTk0ubLWQrw37W_qyO_6Xm2FLQh4LKU0qfYvJ6C7oyHxMGaLy-LwWBc1v8imFsse6kHZxJj2mRxfir0xee2Cn9cMn_a59HgbKYQ6bgzkblEA_qDaiywzRNDGh726NeK9R01h4QYmpUVLHpZTI1Fcq7Xk1eKc6p1FRonDm0C9nBBCskjj84Av68PgdIeHaj6lMbBv9G4ZmrWvN9_kJRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c09abf4.mp4?token=BnqE-rOS2ggUpvAy-QHwEeo6oRn9edijje9g80qOk6KK7zKHBeqfOyaBrIJEtIsv3BERw5NpH5oe4NlkjD2sgTzs3Vme82Z_WxKzlFicGtJm9KeaCiTP7ZIx60SFOrEX4nSjTk0ubLWQrw37W_qyO_6Xm2FLQh4LKU0qfYvJ6C7oyHxMGaLy-LwWBc1v8imFsse6kHZxJj2mRxfir0xee2Cn9cMn_a59HgbKYQ6bgzkblEA_qDaiywzRNDGh726NeK9R01h4QYmpUVLHpZTI1Fcq7Xk1eKc6p1FRonDm0C9nBBCskjj84Av68PgdIeHaj6lMbBv9G4ZmrWvN9_kJRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت مستقیم حملات هوایی انتقامی ایران به منافع آمریکا در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/671628" target="_blank">📅 02:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671627">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0678b866.mp4?token=pg7Eyf1cZ29OJajhQBKPL04NFEHZCvagfiXjsUFVOyR95SArdvjmZs3DhjGsaE4AVYI__D12I_QjWMSSXGTjOHzEscEOknxoOv20HI0qabaqnfrU2lUJk9YCi58SuGD9TzY8Aq1B0fb4fsr70EDpvgNyItYIhpF3lxx5diSOEbIp_SxzYQ7oO9g_S7qehhPAr7sT4dMc9Kd1rDYy5szwMV7QzgfI9fnISQvGemNMVkOkuON6HWxDElawbb-2sMgjAN1jiDRzmdiLFtSlK7MsicVON4Jfax02PjYHL0NLqGgpCAe4zL2bY3zYFMoQH-QWWAaC-Q9C9zZCnFd6zT4Zwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0678b866.mp4?token=pg7Eyf1cZ29OJajhQBKPL04NFEHZCvagfiXjsUFVOyR95SArdvjmZs3DhjGsaE4AVYI__D12I_QjWMSSXGTjOHzEscEOknxoOv20HI0qabaqnfrU2lUJk9YCi58SuGD9TzY8Aq1B0fb4fsr70EDpvgNyItYIhpF3lxx5diSOEbIp_SxzYQ7oO9g_S7qehhPAr7sT4dMc9Kd1rDYy5szwMV7QzgfI9fnISQvGemNMVkOkuON6HWxDElawbb-2sMgjAN1jiDRzmdiLFtSlK7MsicVON4Jfax02PjYHL0NLqGgpCAe4zL2bY3zYFMoQH-QWWAaC-Q9C9zZCnFd6zT4Zwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کجایی مرد؟!
کجایی…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/671627" target="_blank">📅 02:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671626">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9iZA-aNExcKq3rz4eGX8UJX0ar8o4irVB4K7OCvxfao9w1Z56rJXCSK9Tk6e5_TI37wR0I6wEBbeDiPgTpjHvx3P07vG-Us8SRFor7u2wgu9JK9Vq_wZiKm8FU1yW45WbCy77u1D970UO59-0CjZBf_j3KQABywVJUDOb9m7Y90-8_2Ohji41qWq94TMBR4gv3oDadsdWV17YXZulXhWnDS5bK_0DbOWHZBIH2STUDBsI4ZmAWDKDwX0Olf_9OWB1bRw-aUxrmo8aYt64sXaRAc8hkZUbDaHzdqeDovA_-pA5Xm9tvlXfWxMylpSG0hjv2Ajh5PXvs1uNqt5JzUyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه انگلیسی زبان DD_Geopolitics: اطلاعات جدید تأیید می‌کند که ایالات متحده یک بیمارستان سرطان کودکان در اهواز را هدف قرار داد!!
🔹
آیا ۱۶۸ کودک در میناب و صدها کودک دیگر کافی نبود؟! چرا اسرائیل و ایالات متحده مداوماً به کودکان آسیب می‌زنند؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/671626" target="_blank">📅 02:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671625">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
وزارت خارجه آمریکا فروش تسلیحاتی به عربستان و کویت را تأیید کرد
🔹
آمریکا با فروش راکت‌های ۷۰ میلی‌متری به عربستان و فروش خدمات پشتیبانی نگهداری، تداوم عملیاتی و حفظ آمادگی ناوگان هواپیماهای ترابری C-17 به کویت  موافقت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/671625" target="_blank">📅 02:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f178abbd0.mp4?token=R4eaHyw26cCwx_j1jC7gDnCrbHSt82qVQpzxLcmy91XWvTY3eVkQfieQI18vYav9_c2uUwNhZuARUszz18_xgsD3dwlO9rUMHFlbsekYEy7sPr3CbteyDrhMWslTWFtLJ3KBqHMd8vt1BYo_yt1r_GKuoQWiE_NfWAU9NlmJqdMTMWh3iQra7uSlcc9h5CNcN9KnAjDnoyej19oa-rO3HkZmW7AXBzL2xZr2pqihZ1P3-3MinKmcHsUykNqEZBnCMPEQ4ccpFQF5olLTyTx17J_pW4BpHpIOjklzT9RrplWRWr6hNZo0ydwMhI7sZcIN6KArDH16qvdqtpy37Bt7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f178abbd0.mp4?token=R4eaHyw26cCwx_j1jC7gDnCrbHSt82qVQpzxLcmy91XWvTY3eVkQfieQI18vYav9_c2uUwNhZuARUszz18_xgsD3dwlO9rUMHFlbsekYEy7sPr3CbteyDrhMWslTWFtLJ3KBqHMd8vt1BYo_yt1r_GKuoQWiE_NfWAU9NlmJqdMTMWh3iQra7uSlcc9h5CNcN9KnAjDnoyej19oa-rO3HkZmW7AXBzL2xZr2pqihZ1P3-3MinKmcHsUykNqEZBnCMPEQ4ccpFQF5olLTyTx17J_pW4BpHpIOjklzT9RrplWRWr6hNZo0ydwMhI7sZcIN6KArDH16qvdqtpy37Bt7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک ۶ موشک از خاک کویت به ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/671623" target="_blank">📅 02:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sh8mXsOFzPjdxHhDoRYVWOre9jWkQqOofHqhV264E_OFtJjiwSES38IGDlXHKZjsmWjieNGWdgrckCcXJr07-VG80YMw-PobnOHJfQrn9mAjwKMMflUfoCSPnAV9BkAZrN_W2HymsEb2koHDq3iMnO2fDnROrE00-ECqBCCKPKtGxiPJn4ywdBHd_xqc6xyjsG8-12JXZbWfnzlNO8Y2QNAIRJ5QrfoJDDeMqr1cWDyw6C-W0_xHhjq1vacMY27H_jT1TQ_EwJfzEGKP-sPZcr8hcQxd8sci4YM9Ex5IfJu7KkuN5Xa6NnW_dsMfgCj3E-MP-CnjVGYigyt0dltlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریچارد مدهرست روزنامه‌نگار بریتانیایی : هنوز نمی‌تونم بفهمم چطور یه کشور دیگه رئیس کشورت رو ترور می‌کنه و تو هنوز باهاشون حرف می‌زنی
🔹
این یه مسئله حاکمیته. چطور این به عنوان یه خط قرمز مطلق در نظر گرفته نمی‌شه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/671622" target="_blank">📅 01:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
استاندارد هرمزگان: خسارات محدود در برخورد پرتابه دشمن به بخشی از یک کارخانه تولید پودر ماهی در قشم / مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/671621" target="_blank">📅 01:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
وقوع چندین انفجار در کویت
🔹
منابع محلی بامداد پنجشنبه از حمله به منافع اقتصادی و تأسیسات آمریکایی در کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671620" target="_blank">📅 01:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doz1VAQpp97thcH9UFPQxy9oq41zzoidCIbvMFt5YAg4siKE3KVFYaDfjTNDHhwimP0wFMHnpK-pXUrYaTYxPTg-qAvqXSlI6xBFxmUJBLc6URMW3ARpFaS2Ij6LtQiM-1EdLiLLTM1uXg2yHJJeASr6SELxZJUgm10tAFvJ94Cv2NHeGyPH3WbgT0njhL_zev_oxMJpfOeWylos9CJnBuwVKagakzaKrKN2MloUhW4AVwbvr0GCeQKHNQRVegPk6nf1anitynUimVyKeQOmGZkJy90j7kVny3d34PIXWllZBnW3Kx_pv1wup2H-D0fkns205P93-xZsdMI_IJ132w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: ایران تاکنون به تعهدات خود پایبند بوده است؛ برخلاف آنچه وزیر خزانه‌داری آمریکا انجام می‌دهد که با نقض بند ۹ تفاهم‌نامه، تعهدات خود را زیر پا گذاشته است
🔹
واقعیت این است که اجرای تعهدات تنها زمانی امکان‌پذیر است که هر دو طرف به‌طور متقابل به تعهدات خود پایبند باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/671619" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671618">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDbnOuOcmrmPVzc2pd_HS3cOmkrv9d1w0ZEjplXLZ_o72s5OncfbVy4TiSh2uoU_VwHJA9zPKFaEp8XDbamQa3GDRGm0dfeJpYFer2UN5YUv3iP1W3foob-aaHeVa1t_aez7GNHuG1VokyDw2AKVlPNZFKjwYS0S6LBEnpmWBJHCCKQUB9hZMT4b0bqfNN7bCGgvX7MvfPWfwUjnLaalzD1q5SuyLZ9irtmp8bofOsv8ywuXO1bh8VOOck2l4L_L5ombFYJLDlGTyzYaswLYqrC5_E-5kuXXSJAc27o6s-2Uck7EtArivHefEXR-jqaj6H6Bpy65IEQYEmf2PeiBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: دشمن تصور نکند که می‌تواند جنگ را فرسایشی کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/671618" target="_blank">📅 01:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671617">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
اصابت مجدد پرتابه‌های دشمن به نقاطی در سیریک و بندرعباس
🔹
دقایقی پیش پرتابه‌هایی به بندرعباس در مرکز و سیریک در شرق هرمزگان اصابت کرد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671617" target="_blank">📅 01:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671616">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhk1IKmLPQG2LcgdPeEdb0lpDjaSBVTPy0HdqH_3y80RykvuS3cMleRV4xewqn1EGYoaMF2_pHwzL5sPzOQGMYykxOrcEEQl9iPUFyKjas1orlTOjVhheGvQAYjtTYf-63oOtoKUoXWgjAwlRq0lZ3ExPiqdFI2AeJotgI0ifZvjEcYnfwoHcuT1kMqObR6z6jEaAjj_l9vOAOLingmHna0BvzQXJLV9Y_5MiHKTucLIEUxszcztrZMEi-LXfEl7Yj3BUXnU8BAuYaLeUNV0-Gpy-KHCB27G9H8jeC2D10IXOf7MjkERsHvW0DpVN1rC1-CxY_jKZ0YhHYTE13kc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی : دوباره می‌خوان تقصیرش رو بندازن گردن هوش مصنوعی؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/671616" target="_blank">📅 01:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671615">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی برای دومین بار در حوالی سیریک
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/671615" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671614">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGA0GIQrVBPfCOFj5psfRjMloaAHVBHPueU1rbaaUuIVl-pCbxe3_gr_tH8S6uixZQMHu02VBvXsDcySGmeSvvIh9lzmxKi_1zQabBV2nibZugUmn3Su_IPkkgItsaHEZyhQqxaimnHBrHhoD0cYWMILbbxY-uivYgMUq68mr7rRl6Wpf42KFueNkj1QD2UntmXKbgUSOwoC6zaYNuHW5Mbd9FkNBqr7f3uK4-gs0XiYJjGJ5q41T2rI8U3C4EzCK6RMRJCX6aFElldloAQxCyyLzE0yApLkEc_t3kVSbZhLnerOi-CEZ8H0RQkz7fewdaSTAb234SsXuG7bLva48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشدید فعالیت هواپیماهای آمریکایی در منطقه
🔹
فعالیت هوایی آمریکا هم اکنون بر فراز منطقه تشدید شده است؛ به‌طوری که ۱۰ فروند هواپیمای سوخت‌رسان از نوع KC-135R و KC-46A، به همراه یک فروند هواپیمای هشدار زودهنگام E-3G (آواکس)، در آسمان منطقه در حال پرواز هستند. / تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/671614" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671613">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
در پی حملات دشمن بیمارستان بقایی ۲ دانشگاه علوم پزشکی اهواز موقتا از چرخه خدمت خارج شد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/671613" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671612">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در بندرعباس
🔹
ساکنان محلی از شنیده شدن صدای انفجارهایی در شهر بندرعباس خبر دادند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/671612" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671611">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
فرمانداری راسک: مردم از ترددهای غیرضروری پرهیز کنند
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/671611" target="_blank">📅 01:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
صدای انفجار در قشم شنیده شد
🔹
دقایقی قبل صدای انفجار در جزیره قشم شنیده شد و موضوع در درست بررسی بیشتر است./ ایرنا
اخبار لحظه‌ای حملات امشب
👇
khabarfoori.com/fa/tiny/news-3230721</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671610" target="_blank">📅 01:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی در حوالی سیریک
🔹
۵۵ دقیقه بامداد پنجشنبه نقطه ای در حوالی سیریک مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/671609" target="_blank">📅 01:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671608">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ارتش: تنگه هرمز تا پذیرش نظام قانون‌مند ایران از سوی آمریکا بسته می‌ماند
سخنگوی ارتش:
🔹
تا زمانی که آمریکا نظام قانون‌مند ایرانی را نپذیرد، و سازوکار مبتنی بر اراده ایرانی بر تنگه هرمز حاکم نشود این تنگه بسته‌ خواهد ماند.
🔹
تمکین آمریکا به مفاد تفاهم‌نامه، دست برداشتن از شرارت‌ها و دشمن‌ستیزی، و حاکم‌شدن قوانین ایرانی راهکار بازگشایی تنگه هرمز است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/671608" target="_blank">📅 01:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671607">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cced705f5.mp4?token=Zm3DxvCVZTXaZjpGV9QBvKkvE9nMvRuUXWXvPIXUufHKWOFLG9_XGrEYEYmG10dbK5IRgPUTcZ7ZBO5t2wjku6z5hSbZsjSPEVpGmavRseQSukAD7K3lp72XOuL2sxy53su3Zi-UPrDDhRW-3A09Cwxbb_Rx8b8t4630SNMDr0CDPBO9ia7u9RSujgqZBMokvsnYawlFB-QuZkw1EE7SGU7ZinJhEaMMi5g_p8IVLMzivPXZ07uiN9WmcWWSIlhAgBMcI3hEhwuImJ5S1XseOqJB5-aEmcinugvEJpPKj3cOrCMECBgVApYukmBKwPZQXHvICtUufpU7670UGsTawQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cced705f5.mp4?token=Zm3DxvCVZTXaZjpGV9QBvKkvE9nMvRuUXWXvPIXUufHKWOFLG9_XGrEYEYmG10dbK5IRgPUTcZ7ZBO5t2wjku6z5hSbZsjSPEVpGmavRseQSukAD7K3lp72XOuL2sxy53su3Zi-UPrDDhRW-3A09Cwxbb_Rx8b8t4630SNMDr0CDPBO9ia7u9RSujgqZBMokvsnYawlFB-QuZkw1EE7SGU7ZinJhEaMMi5g_p8IVLMzivPXZ07uiN9WmcWWSIlhAgBMcI3hEhwuImJ5S1XseOqJB5-aEmcinugvEJpPKj3cOrCMECBgVApYukmBKwPZQXHvICtUufpU7670UGsTawQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا مدعی حمله به یک نفتکش در مسیر بنادر ایران شد  نهاد تروریستی ستاد فرماندهی مرکزی آمریکا (سنتکام):
🔹
ما امروز یک نفتکش خالی را که قصد داشت به سمت یک بندر ایرانی در خلیج فارس حرکت کند، از کار انداختیم.
🔹
این کشتی هشدارهای متعدد را نادیده گرفت در حالی…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/671607" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671606">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=jj2s6ehbyLS4w1yZhdjqhvNB5MnzOYJValvJUrLjCKfvGQlM79gAOydzxz6Ik_YL53jQ0MkuLCBCXIQDiHLkbWyNyWl66R-MiZUJM2zJiFo2jAaR0ff0aRTRrPs-znuqhlWdFq9LIjlzzzHesJP-gxmqZZHi_Hvn76SRj58GoqBdeWr_ndq5yticlYx8WviTwRao-K0PgGtiryeO866qiNzzbFs7XiFRsGAztDU0csXXhba6tHvoub5s5PaFXldOKSZ6sFNzrYZt-HKBmDqrdmtxZQ90p0xkg1U4pORhi3mQ9cH8LS_i24XnWxpQZKyf2DwxK7xn5miwckYJqRTTJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=jj2s6ehbyLS4w1yZhdjqhvNB5MnzOYJValvJUrLjCKfvGQlM79gAOydzxz6Ik_YL53jQ0MkuLCBCXIQDiHLkbWyNyWl66R-MiZUJM2zJiFo2jAaR0ff0aRTRrPs-znuqhlWdFq9LIjlzzzHesJP-gxmqZZHi_Hvn76SRj58GoqBdeWr_ndq5yticlYx8WviTwRao-K0PgGtiryeO866qiNzzbFs7XiFRsGAztDU0csXXhba6tHvoub5s5PaFXldOKSZ6sFNzrYZt-HKBmDqrdmtxZQ90p0xkg1U4pORhi3mQ9cH8LS_i24XnWxpQZKyf2DwxK7xn5miwckYJqRTTJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بیمارستان شهید بقایی اهواز پس از حملۀ آمریکا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/671606" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671605">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b35b61078.mp4?token=gGxNRp_b80agWkv2oloM9uL-bWU7U8i6gexRs5l3yMCqJd_su1CjcacFYnQEMy3OwPxPqhR2njjnUneH5CKERkYEmpNCuMf_uyJBMbLeXoeElc4E7a1qie59PS3ueptuvhteT97ahC8fVtcD_v2E3AxJR3-4JTWSOdhuzlLHGDyK-Vbq7Q6yCYwbPSysIqQF8sA119mB846h-2OIdVc7QUi1QKLJ6o05oWTZll_doZIn0eWws5SbU6eMDuYrX2wFVCGxXIr5eS88_OvtnO2TtO2xgxYl9r_yFBNCSjLF5Mtf4IffCNmpIWDSys25OpdKdtDqmBSf_aiI-bjuPX1NjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b35b61078.mp4?token=gGxNRp_b80agWkv2oloM9uL-bWU7U8i6gexRs5l3yMCqJd_su1CjcacFYnQEMy3OwPxPqhR2njjnUneH5CKERkYEmpNCuMf_uyJBMbLeXoeElc4E7a1qie59PS3ueptuvhteT97ahC8fVtcD_v2E3AxJR3-4JTWSOdhuzlLHGDyK-Vbq7Q6yCYwbPSysIqQF8sA119mB846h-2OIdVc7QUi1QKLJ6o05oWTZll_doZIn0eWws5SbU6eMDuYrX2wFVCGxXIr5eS88_OvtnO2TtO2xgxYl9r_yFBNCSjLF5Mtf4IffCNmpIWDSys25OpdKdtDqmBSf_aiI-bjuPX1NjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشارکت کویت در جنگ تحمیلی آمریکا علیه ایران
🔹
رسانه‌های عراقی با انتشار تصاویری،‌ گزارش دادند که کویت با پرتاب موشک از خاک خود به سمت خاک ایران، در جنگ آمریکا علیه جمهوری اسلامی مشارکت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/671605" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671604">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
امتحانات دانش‌آموزان بوشهری لغو شد  مدیرکل آموزش و پرورش استان بوشهر:
🔹
با تصمیم ستاد عالی آزمون‌های وزارت آموزش و پرورش امتحانات نهایی روزهای ۲۵ و ۲۷ تیرماه، در این استان لغو شد.  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/671604" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671603">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4886136147.mp4?token=Hds2xJ8t6LMSslMM13_NX2P48VszR2e37Xdt4w8R4IFTyAnHGtNRcuF9O3lSJEhKBXYIdpXKh6hWUkSe_QjBCPebGgRbuOJIoaFzJqudsFkrPtpdUWSuv_hLH-u9GstDWUIpXz0vbeNoDMIAJfFyG888H4A9ICT-vhY4XQ8XkXIue3OzZ2HWtRZGV-Y1JIp7UgZgSilkPAMhQmLcHcZBosNjZHnDdWYI2-brhJdkCcPTJUDLObwAfXToY8y23GrmkVs8EjlrDBwRoP7BD2-jq0EPBHj3SQ37BL_TNjhToQssxc3ngbn2J6dxigIV3Nh4Wu3vppUpwujJKk-Spbw0KjaH8alJQTSdJmWq0vNgeiaBAMeLM1RFdRYTDmAfseIGVm0_ekF7XcJyOMZcUWSfGNndaiaKAeFuLZKbanpQnXdD3yIOycuO3T18MY2ikDXb1aB9RnbwVrX9LP4LiJVLAn2OcOzbI1Ao69EENzrCS0vkCh5d5Cm0lnMvQm0XBPKBPne7ixPN4SlPqGPnVENFVYttvaqUc5oGXktC8POijvDlehjDlDNo2cf12igl4wQQqwRP-wm--hW7_oYbKeJg6SvnMf5ZZtrY-uAimnu_I2cIMZjky5nrK2_uwxqzkXL3EEmGzwSqb0z1o8dD8wZDtN-BVpwL0aEwqrAorOLUXzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4886136147.mp4?token=Hds2xJ8t6LMSslMM13_NX2P48VszR2e37Xdt4w8R4IFTyAnHGtNRcuF9O3lSJEhKBXYIdpXKh6hWUkSe_QjBCPebGgRbuOJIoaFzJqudsFkrPtpdUWSuv_hLH-u9GstDWUIpXz0vbeNoDMIAJfFyG888H4A9ICT-vhY4XQ8XkXIue3OzZ2HWtRZGV-Y1JIp7UgZgSilkPAMhQmLcHcZBosNjZHnDdWYI2-brhJdkCcPTJUDLObwAfXToY8y23GrmkVs8EjlrDBwRoP7BD2-jq0EPBHj3SQ37BL_TNjhToQssxc3ngbn2J6dxigIV3Nh4Wu3vppUpwujJKk-Spbw0KjaH8alJQTSdJmWq0vNgeiaBAMeLM1RFdRYTDmAfseIGVm0_ekF7XcJyOMZcUWSfGNndaiaKAeFuLZKbanpQnXdD3yIOycuO3T18MY2ikDXb1aB9RnbwVrX9LP4LiJVLAn2OcOzbI1Ao69EENzrCS0vkCh5d5Cm0lnMvQm0XBPKBPne7ixPN4SlPqGPnVENFVYttvaqUc5oGXktC8POijvDlehjDlDNo2cf12igl4wQQqwRP-wm--hW7_oYbKeJg6SvnMf5ZZtrY-uAimnu_I2cIMZjky5nrK2_uwxqzkXL3EEmGzwSqb0z1o8dD8wZDtN-BVpwL0aEwqrAorOLUXzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهانت سناتور آمریکایی به نخست‌وزیر عراق
🔹
در حالیکه سفر نخست وزیر عراق به آمریکا با انتقادات زیادی در محافل عراقی مواجه شده است، «تیم بورشیت»، از اعضای جمهوری‌خواه کنگره، درباره الزیدی اظهار داشت: من همین چند لحظه پیش وقتم را صرف گوش دادن به سخنان نخست‌وزیر عراق کردم، اما او درباره هیچ چیزی نگفت، وقتم را هدر کردم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/671603" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671602">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آمریکا مدعی حمله به یک نفتکش در مسیر بنادر ایران شد
نهاد تروریستی ستاد فرماندهی مرکزی آمریکا (سنتکام):
🔹
ما امروز یک نفتکش خالی را که قصد داشت به سمت یک بندر ایرانی در خلیج فارس حرکت کند، از کار انداختیم.
🔹
این کشتی هشدارهای متعدد را نادیده گرفت در حالی که تلاش می‌کرد محاصره آمریکا علیه ایران را نقض کند،  در ادامه یک هواپیمای آمریکایی با شلیک موشک به دودکش کشتی، آن را از کار انداخت و از حرکت آن به سمت ایران جلوگیری کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/671602" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlO7XpWHcMdQklQO1Du84m6rfXFd7W5-0yPLJEsmzl_IYXpSFo8z2q-JFDJvUIpUZ60Kuck_dPmYb6vvcC4Ugl3azskVuirXYx-aLaMHSvG0Zt0NCWLi7rLv-ek3DA-HAxGEhN8YHTec7Banb-Ki15QqOLDzzcT5eZB-wL2ZertIhf0cP4NUglK8a0TgOb-rmVrDj8QxjFjP39NKRHF3caA_n4yz_WxIiPS4q5yfTdqBbO1zSmJVPvD6HQnwu_m4P6uUFBBwYxIpd5xp66EY0M3UOjbZ4b_VJcH6nCjHTpJ916DOeOWAU7q3IPJxfsZTN4nTRnAqsCqc2SiWkjs0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل دوم آرژانتین به انگلیس
▪️
آرژانتین ۲_۱ انگلیس
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/671601" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UErmjY9srQjHGxRLf61zziBhjxGI63HV4IfG8Pf3dZ9PG61RUsCqO04xG-nS3-OB0xszkCBDvo6zdUNWEhGyfze741dsMdmNyPjU9NHibH4mUaxuELI8q5rAOzxiUtnoYcn2T56G_mBLcI8lsVDP1cTfqGU9uI7OE5zbtEGD1UZF3UddAVPVIYnXL5FWztctw7U2s9joNEckkpUbKRTLiiijXq0TEzOvtOWZz7saQ9TdGisyPOBSdBONuzrP4KP_ioY3yMruWrzn4qgnzndK4d-r_HvWE2zOl5x3RCuQqwshpEfvYBoEzzhYDWEragP1yqgcd_lLWuv1SBJFef47tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کشتی اماراتی دیگر از جنوب تنگۀ هرمز برگشت خورد
🔹
تصاویر ماهواره‌ای نشان می‌دهد که یک کشتی اماراتی ناگهان مسیر خود را از مسیر جنوبی تنگۀ هرمز تغییر داده و برگشته است
🔹
شب‌های گذشته دو کشتی اماراتی هدف حملۀ موشک‌های ایران قرار گرفتند که این هدف‌گیری به توقف صادرات نفت بندر فجیرۀ امارات منجر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/671600" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a1ced86b.mp4?token=jsciiv2hoWLGscddrt65eXxy01Zxw40zII-unxv5WXGgml04oo8pCnxT4Qfwe84o1qyQ1Sh-HUMHOLUPEbzOD_GNdMNXJqE_MEterHjZkdPM3OYT75_Azj_WdVeUn5qJZaWxPLAXj4Kfutn_R7Fwi5_thSifBz6v1EKOjvh3tNnDre4R2h2uwR1W1R1DVBs2QQ_tghR12o-LchX16JlWYsFC6cC82J5BXQiF5XQEhlCvFbOlgd1Y4AhpN0j1BgApceXtBTfbQk6meQkMTuD68O_woF4WI3cFhs4OI22gR5YSylZUvDbO7GgH2aRl3IP0GYrQ7g-KxLQ4OHCHXAJ3_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a1ced86b.mp4?token=jsciiv2hoWLGscddrt65eXxy01Zxw40zII-unxv5WXGgml04oo8pCnxT4Qfwe84o1qyQ1Sh-HUMHOLUPEbzOD_GNdMNXJqE_MEterHjZkdPM3OYT75_Azj_WdVeUn5qJZaWxPLAXj4Kfutn_R7Fwi5_thSifBz6v1EKOjvh3tNnDre4R2h2uwR1W1R1DVBs2QQ_tghR12o-LchX16JlWYsFC6cC82J5BXQiF5XQEhlCvFbOlgd1Y4AhpN0j1BgApceXtBTfbQk6meQkMTuD68O_woF4WI3cFhs4OI22gR5YSylZUvDbO7GgH2aRl3IP0GYrQ7g-KxLQ4OHCHXAJ3_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل دوم آرژانتین به انگلیس
▪️
آرژانتین ۲_۱ انگلیس
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/671599" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b282391b4a.mp4?token=ROZRc9aVuV2J3gNiGRNctWIr7AV4XEJ36s-jS_p_vUO-chy-4wfujRFKyYW99fAw9YNg9CVZW4XIpzi8cWHmw1YinA08hjMEQQD6AtGgWOwg3rTI2XuDj0SFWD6oQLjPYeD2fg5Bb-mwHXVGnNpg_wl4ofu833sOzEl298ASuOdWYGhuBHRCwdCppoawM55n1UNGWoJ4IYPzCHZG0MsPfRYfbiBqMebs6arF9puNEe_p44SVvDfo0v0NZ_VIPdEQQzc3EUeMQUeCUnuIDyP-tuKALxRrI-DDTjrv3ZRNKSsg1Q8FOt4vHJRJ_YwmKkRyCgcMyzutwH9G2a1wj-z3qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b282391b4a.mp4?token=ROZRc9aVuV2J3gNiGRNctWIr7AV4XEJ36s-jS_p_vUO-chy-4wfujRFKyYW99fAw9YNg9CVZW4XIpzi8cWHmw1YinA08hjMEQQD6AtGgWOwg3rTI2XuDj0SFWD6oQLjPYeD2fg5Bb-mwHXVGnNpg_wl4ofu833sOzEl298ASuOdWYGhuBHRCwdCppoawM55n1UNGWoJ4IYPzCHZG0MsPfRYfbiBqMebs6arF9puNEe_p44SVvDfo0v0NZ_VIPdEQQzc3EUeMQUeCUnuIDyP-tuKALxRrI-DDTjrv3ZRNKSsg1Q8FOt4vHJRJ_YwmKkRyCgcMyzutwH9G2a1wj-z3qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قانونگذار آمریکایی: کسی به ترامپ اعتماد ندارد
سث مولتون، نماینده کنگره آمریکا:
🔹
کسی به ترامپ اعتماد ندارد، نه فقط ایرانی‌ها، بلکه هر کس دیگری که طرف درگیری است.
🔹
منظورم این است که ترامپ می‌گوید که صحبت کردن با ایرانی‌ها اتلاف وقت است، اما به نظر من، بیشتر جهان فکر می‌کند که صحبت کردن با او اتلاف وقت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671598" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
رویترز: کشتی‌ها حاضر نیستند به کمک آمریکا از تنگه هرمز عبور کنند
🔹
هفت منبع در حوزه امنیت دریانوردی و صنعت کشتیرانی گفتند که شرکت‌های کشتیرانی پس از موج جدید درگیری‌ها که نگرانی‌های ایمنی را برانگیخته، از استفاده طرح ارتش آمریکا برای عبور از تنگه هرمز خودداری می‌کنند.
🔹
به گزارش رویترز، از زمان آغاز تجاوز نظامی علیه ایران و بسته شدن تنگه، کشتی‌ها مجبور به استفاده یکی از دو مسیر نزدیک به سواحل ایران یا عمان هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/671597" target="_blank">📅 00:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671596">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس درباره ایران: ما قرار نیست فقط بمباران کنیم، بمباران کنیم و باز هم بمباران کنیم
🔹
ما تلاش خواهیم کرد از نیروی نظامی‌مان به‌عنوان یکی از ابزارهای متعددی که در اختیار داریم برای حل این مشکل استفاده کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/671596" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812957343a.mp4?token=NpoDgtcZ7Q-RXeZJDvNKp8PFGST-yIhiCtrz2E-wnGGmAcRaF0X7P48pKOGmxl3Wf9cFAT1IfBSA2saeszuco2TzNIu73l46RojJaRD45xlbCMNlhtmFyQnacIqy2eeAyUIayLR7V0-J-wrDMJio84GnNRZZzh5Mh8OEfY_-PQ27R5H14IiOkix6gJMIXjNawm2nTElDfOeeI2nabetjelJ1SXRf59HJY3vecaahV72S4HQOCgCGoXY6kS7S5ESYRmp8wO_XrDNajIGHh8vxwWDyfnxhi4yaWHG-0wxjS_i9vNRePLVIieLxawr76JYj-qiD7FA3GawsRvbuJVDCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812957343a.mp4?token=NpoDgtcZ7Q-RXeZJDvNKp8PFGST-yIhiCtrz2E-wnGGmAcRaF0X7P48pKOGmxl3Wf9cFAT1IfBSA2saeszuco2TzNIu73l46RojJaRD45xlbCMNlhtmFyQnacIqy2eeAyUIayLR7V0-J-wrDMJio84GnNRZZzh5Mh8OEfY_-PQ27R5H14IiOkix6gJMIXjNawm2nTElDfOeeI2nabetjelJ1SXRf59HJY3vecaahV72S4HQOCgCGoXY6kS7S5ESYRmp8wO_XrDNajIGHh8vxwWDyfnxhi4yaWHG-0wxjS_i9vNRePLVIieLxawr76JYj-qiD7FA3GawsRvbuJVDCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل تساوی آرژانتین به انگلیس
▪️
آرژانتین ۱_۱ انگلیس
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/671595" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671594">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYPHROXRg77QaDlZVROa0TdZzT51_gIBQLzlWXtVssTi2xBo4aipIH5-VNwr7RLB9btWKixM4v_6-cCkyqL0swzHjzz2j_AUYh63WSCsSATQHmcmQwclImEGZ2pXv_xydQkGsoWMmUOW9C3l7aY474wKvscwCve2_b11gRr7GYzAkQrN3OTgKGUWsYgWwSBuv9vOCqnhJjK80C-dAbtZhMmkOwzmK4iR8ANSC9eOqGjVhNjvLYJDovS9cY4lLbHyONxIlk7e39mPhV9tvBJQS-xgNMoSaUlZ3zM2yHdW7Ch0ZoNjCP0bKM6yQvhX2tWxiCb3MoC7ZFZ8dX6fkwwgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/671594" target="_blank">📅 00:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تکذیب حمله هوایی به بوشهر
فرماندار بوشهر:
🔹
تا این لحظه هیچ‌گونه صدا یا حادثه انفجاری در سطح شهر بوشهر گزارش نشده و اخبار منتشرشده در شبکه‌های اجتماعی کاملاً بی‌اساس است.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/671593" target="_blank">📅 00:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671591">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
استانداری خوزستان: پس از تهاجم دشمن تروریستی آمریکا به شهر اهواز خساراتی به منازل مسکونی اطراف وارد شده و شیشه برخی منازل شکسته شده است
🔹
تاکنون این حملات تلفات جانی در پی نداشته است./مهر  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/671591" target="_blank">📅 00:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671590">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
تعلیق همه پروازهای فرودگاه اربیل تا اطلاع ثانوی
🔹
فرودگاه اربیل اعلام کرد تمامی پروازهای ورودی و خروجی این فرودگاه تا اطلاع ثانوی به حالت تعلیق درآمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/671590" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671589">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOp_PNU31hqyEgZ6ekdMEL_-K3cBOafHaGoAnSVbcltXR0aYnQMS9rCVvDf0veTYTb8wlFoN07lNdOnRDnSNapPbg9G_zshkFMgXQDjrFEKAr5c55xOy0didbDRHP23vLkBaSsZqu-qiPuWq9BnWqx6WHTC4Iu_zxyBbSJK7B0o-u5SH_m8wEVdG5Ly6QU3IQByNamUFsmCDRbOsA2Zc5lacsBtNOKE77G8c516lv1eyFt_-2UwWSIjMORbmp8Z8uLiLmFeWcxMg2r_8v53bj95lB7oBb5YfNJdxnGca4yxtRowQApgh4Ob6pgiH7QQ-xnZ3XKxhzruuNdaKBS8BFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/671589" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a7fdcdce.mp4?token=kZVAQkIR269IhkSRypU8IzNPtTgsiPMWZqlalHRVy0yGC_byLQcHhKnWm0K8doW_-UT9mroAeD75x1zfSwuNx2_EWl5Fh7Ahdxbkik5sgCshkVP2XqXnTqTQCsns8fYb3nCcQ73_Kb1QPYi24F4noP5jOHijrJzXuKZz1oXzZrn8HLJqaau8vnmGzIFqXZRpqrNGln-hkv5va3PQggNaeDGmvxidNqBrWzBUyWNt0LxkxW6XPOFdDNyJ2cJcgMjpUQJksRCekd7VoprNpE13hLXZR07q4w7ulDX7LxjDV03tdYPczCtfO11Pvs4uctIcnPnCWVPxOTnbEyw_Ny4KGkr9FjVpvzkXLWsbBKWEfYeYL7psKtDSk-bTtt6Xm6svFLUm5fEmPt2kt_VW19mIFymhghJt8ktyPef4h_Ub_HJIelqDlrzICLJ0gm6NderkkiOWljGwyNlhPEih7O3ZGlmRFEDsEzpP2f63i4I0KZxTWhjZdyYTmCi1zCRgNLADrBShiNypRhHyCbLmYFqakNqD5Nb1am7PUUAIJ9-KV9xRQ88eFfH2wF-Chp40nOl5ihSbFUcAyBfXbPt2VZfUBUtg6YK_osvv4RYKOHgnxNMYM5clf7HSYZbTSQ3kSaJHBCgxWFNQgrkAIJ2_FOXrXRUmcscedYrYD26Eb6XcKA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a7fdcdce.mp4?token=kZVAQkIR269IhkSRypU8IzNPtTgsiPMWZqlalHRVy0yGC_byLQcHhKnWm0K8doW_-UT9mroAeD75x1zfSwuNx2_EWl5Fh7Ahdxbkik5sgCshkVP2XqXnTqTQCsns8fYb3nCcQ73_Kb1QPYi24F4noP5jOHijrJzXuKZz1oXzZrn8HLJqaau8vnmGzIFqXZRpqrNGln-hkv5va3PQggNaeDGmvxidNqBrWzBUyWNt0LxkxW6XPOFdDNyJ2cJcgMjpUQJksRCekd7VoprNpE13hLXZR07q4w7ulDX7LxjDV03tdYPczCtfO11Pvs4uctIcnPnCWVPxOTnbEyw_Ny4KGkr9FjVpvzkXLWsbBKWEfYeYL7psKtDSk-bTtt6Xm6svFLUm5fEmPt2kt_VW19mIFymhghJt8ktyPef4h_Ub_HJIelqDlrzICLJ0gm6NderkkiOWljGwyNlhPEih7O3ZGlmRFEDsEzpP2f63i4I0KZxTWhjZdyYTmCi1zCRgNLADrBShiNypRhHyCbLmYFqakNqD5Nb1am7PUUAIJ9-KV9xRQ88eFfH2wF-Chp40nOl5ihSbFUcAyBfXbPt2VZfUBUtg6YK_osvv4RYKOHgnxNMYM5clf7HSYZbTSQ3kSaJHBCgxWFNQgrkAIJ2_FOXrXRUmcscedYrYD26Eb6XcKA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزادی‌خواهان جهان چطور و در چه محل‌هایی می‌توانند ترامپ را قصاص کنند؟
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/671588" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
استانداری خوزستان: پس از تهاجم دشمن تروریستی آمریکا به شهر اهواز خساراتی به منازل مسکونی اطراف وارد شده و شیشه برخی منازل شکسته شده است
🔹
تاکنون این حملات تلفات جانی در پی نداشته است./مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671587" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is7_jcs9qBlH0ygUkucuLV3maCVOqmYMi9e-xmbnEFXrc_l5WvEm8i2vrVFmvPLzd9FuMVf_h9Nzm9vEseRFCw-YFal87-zyZ9TnyyV31RJiV-TnrrSKSm5P-EQGCHtiOQ3Obc0AE64PP6xDTEv8mXU-bSJ7U0Vj5TQuFOQBSH_vO1x4I-duNzUrsruxTQUFGcs7uydPEAYrE7FhB-Q5Ez5LCkMnEYEArhG7oJxxYLOj-f8JG5JsNGzCUmGoecXFTypHhqq5K4uRjlaJllAy3PoG96poZwfVV_Pqou7v34U6Z5LcOgSPG-wEFLsp1tkmYSLeI7Mzh0uKu4MeVgX_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان خدمت
🔹
هفت سرباز نیروی زمینی ارتش، در حمله موشکی به پادگان بمپور ایرانشهر به شهادت رسیدند. این حمله که محل استقرار سربازان را هدف قرار داد، شماری از نیروها را نیز مجروح کرد و بار دیگر داغ جنگ را بر دل خانواده‌های ایرانی نشاند. نیروی زمینی ارتش ضمن محکوم کردن این اقدام، اعلام کرد پاسخ این تجاوز در زمان و مکان مناسب داده خواهد شد.
🔹
هشتصدودهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/671586" target="_blank">📅 23:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a931a74fee.mp4?token=RQZGMbDVNrA5DpIgVV6LsBNIL6iJfd0H94I19B06HHneSm9BMO5HZtc1gv27TWqpnI-XervYD3dkt71epoVmqG9suhXh_niOAFsmCBYMk8uqR14-EFnVYK3mKqlZiry3M3ch1TizQAJ7ttSSLtHiETBSgmzIIQH2Y-31PtZEuUmtd-374B0lpQHcvpwxahA3inrpcWJhkLk6SEjez_dogr4m8DoZJ0NGuczcWko7y2wY2vJbGgohOzIb6Y3bYqbJ2KdXZJP4ZcEYw9apkiHLhycxmcaaR-p7lPZtN9jmjDTtChla3A-tNW4dxSHy_aOubUNjAQ15Ec2R6QYdsW51Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a931a74fee.mp4?token=RQZGMbDVNrA5DpIgVV6LsBNIL6iJfd0H94I19B06HHneSm9BMO5HZtc1gv27TWqpnI-XervYD3dkt71epoVmqG9suhXh_niOAFsmCBYMk8uqR14-EFnVYK3mKqlZiry3M3ch1TizQAJ7ttSSLtHiETBSgmzIIQH2Y-31PtZEuUmtd-374B0lpQHcvpwxahA3inrpcWJhkLk6SEjez_dogr4m8DoZJ0NGuczcWko7y2wY2vJbGgohOzIb6Y3bYqbJ2KdXZJP4ZcEYw9apkiHLhycxmcaaR-p7lPZtN9jmjDTtChla3A-tNW4dxSHy_aOubUNjAQ15Ec2R6QYdsW51Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد آرزوهای خودش را تکرار کرد
رئیس‌جمهور آمریکا:
🔹
ایران به‌زودی شکست می‌خورد؛ آن‌ها خیلی زود شکست خواهند خورد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/671585" target="_blank">📅 23:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
مالک شریعتی، نماینده مجلس: یارانه بنزین باید به فرد تعلق بگیرد، نه به خودرو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/671584" target="_blank">📅 23:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e842e1cbcd.mp4?token=pZqrjTWzjd_D6xfsJw-rNhJw4QuaexPzQLh7htC1AlvyIjigRj5Sv70R1mwesy5ksUR4lCvtg2EwosTMvrO5R58o6BcvsykFtuoVfpBkErE-m5R8aDySgePxQMozXMVdAmU32ssYhZQCqLTfIidbmtk4BQOBQ2IH0r42ywg_5OaI6h7pXuaGaNxWBytqnfX3PdYvnC3_7l93fhGloygDUOHexkuEUWuJ3y6ehq9s_F4Q4HH7tk-CM1-QpOa5vYRvBwkse2GR9DM7-qPC4yxae_kBWCcaCcaKacAzDra6vcbLjsJuN5JnpFQrp-nZeSWqxV3hlf_QjftjvJBYhOnmjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e842e1cbcd.mp4?token=pZqrjTWzjd_D6xfsJw-rNhJw4QuaexPzQLh7htC1AlvyIjigRj5Sv70R1mwesy5ksUR4lCvtg2EwosTMvrO5R58o6BcvsykFtuoVfpBkErE-m5R8aDySgePxQMozXMVdAmU32ssYhZQCqLTfIidbmtk4BQOBQ2IH0r42ywg_5OaI6h7pXuaGaNxWBytqnfX3PdYvnC3_7l93fhGloygDUOHexkuEUWuJ3y6ehq9s_F4Q4HH7tk-CM1-QpOa5vYRvBwkse2GR9DM7-qPC4yxae_kBWCcaCcaKacAzDra6vcbLjsJuN5JnpFQrp-nZeSWqxV3hlf_QjftjvJBYhOnmjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول انگلیس به آرژانتین توسط گوردون
▪️
آرژانتین ۰ - ۱ انگلیس
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/671583" target="_blank">📅 23:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
خطوط هوایی، پروازهای خود را به غرب آسیا در پی تشدید تنش آمریکا و ایران لغو کردند
الجزیره انگلیسی:
🔹
شرکت‌های هواپیمایی یونان، کانادا، ایرفرانس و کی ال ام پروازهای برنامه‌ریزی شده خود به دبی، تل آویو و سایر مقاصد در منطقه را متوقف کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/671582" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
شدیدترین حملات به اهواز
🔹
امشب اهواز شدیدترین حملات را از زمان آغاز موج جدید حملات ارتش تروریستی آمریکا، شاهد است./ جماران
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/671581" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
امتحانات دانش‌آموزان بوشهری لغو شد
مدیرکل آموزش و پرورش استان بوشهر:
🔹
با تصمیم ستاد عالی آزمون‌های وزارت آموزش و پرورش امتحانات نهایی روزهای ۲۵ و ۲۷ تیرماه، در این استان لغو شد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/671580" target="_blank">📅 23:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=q4Vr2LE0bekR9Eqt3bf3Dh08RjXxhXcFYPyT6tyXy9sgWlhTnI56Ml-Hv4zMN8G6GZdY9tzjuJMwkrSRHWK1aF-ChqMgGTgZA2TOV54ObbczliG7a5k9AgBv5LCInTKGlcQbsUtv5-9E2I8FNMWxkYELfhhtvlQQ82K2qOsXMupW2CUkTu1MMjBJla7r5yVg6Z34C5kwHZvM1K_yrcZq3qzhS3cMMSOTPwsfDRwp600QL6BvIr3ppvQguG9DpZ6exOczrK2IotZaJlFJA06Lb406X02rzaLYnxs02hvbDmhbQ4xy7uXMZ2hMll1zA34AgaJY3GD2vlfEdy19Kx0hhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=q4Vr2LE0bekR9Eqt3bf3Dh08RjXxhXcFYPyT6tyXy9sgWlhTnI56Ml-Hv4zMN8G6GZdY9tzjuJMwkrSRHWK1aF-ChqMgGTgZA2TOV54ObbczliG7a5k9AgBv5LCInTKGlcQbsUtv5-9E2I8FNMWxkYELfhhtvlQQ82K2qOsXMupW2CUkTu1MMjBJla7r5yVg6Z34C5kwHZvM1K_yrcZq3qzhS3cMMSOTPwsfDRwp600QL6BvIr3ppvQguG9DpZ6exOczrK2IotZaJlFJA06Lb406X02rzaLYnxs02hvbDmhbQ4xy7uXMZ2hMll1zA34AgaJY3GD2vlfEdy19Kx0hhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماسی از ایرانی‌ها برای ملاقات دریافت کردم
🔹
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🔹
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/671579" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
وال استریت ژورنال به نقل از مقامات آمریکایی: گزینه‌ها شامل تشدید حملات و اعزام نیروهای زمینی برای تصرف جزایر ایرانی نزدیک تنگه هرمز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/671578" target="_blank">📅 23:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
امروز کدام شهرهای ایران هدف حملات آمریکا قرار گرفت؟
👇
khabarfoori.com/fa/tiny/news-3230586
🔹
در ترکیه چه گذشت؟ | جلسه محرمانه ای که باعث شد ترامپ به فکر "جنگ بزرگ" با ایران بیفتد
👇
khabarfoori.com/fa/tiny/news-3230677
🔹
آکسیوس فاش کرد؛ ترامپ در اتاق وضعیت برای حمله گسترده‌تر به ایران چه تصمیمی گرفت؟
👇
khabarfoori.com/fa/tiny/news-3230476
🔹
ترامپ دوباره تهدید کرد: پل‌ها و نیروگاه‌ها را می‌زنیم!
👇
khabarfoori.com/fa/tiny/news-3230437
🔹
طلا و سکه امروز چقدر گران شد؟
👇
khabarfoori.com/fa/tiny/news-3230577
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/671577" target="_blank">📅 23:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وال استریت ژورنال به نقل از مقامات آمریکایی: گزینه‌ها شامل تشدید حملات و اعزام نیروهای زمینی برای تصرف جزایر ایرانی نزدیک تنگه هرمز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/671576" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
استانداری هرمزگان:  در حملات جدید آمریکا به حوالی بندرعباس هیچ مصدوم غیر نظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری  گزارش نشده است
🔹
هم‌اکنون تیم‌های عملیاتی نیروهای مسلح در مناطق مورد حمله حضور داشته و اوضاع را تحت کنترل دارند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/671575" target="_blank">📅 23:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ-8S_1SIF7FymyzDBUhspp3vq6tjh2US48hwZ5eCk4Vn6JF9PDeJIsgUFSuPX4LLhEbJ_i-1xfbPTybZzhQVaUWcAGXd6KZAQYmpOCgfzbXVJPT10kvggVzeASrz7EfxtL5rsJmP_4PuJE9tOctsBmr854tS-D0fAPSF0Y5ULXfMMdj7O5AetHW-5pXqj28RWdDfAFlnN2nOIsPoBB89q9tRBQX2GrCckX1to7qg0VgUBbdBIg8VDaRU0nNeTR_WowYOx9Fi0UX_rT8qFJg4Hq3mpwvWvCZrdw4P2ZyY_9q3bAQy41jHRqwTmdmL5xMwBHxoWS0uK5R37JTKz-_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران در میان ۴۰ شهر جهان با بیشترین آلودگی نوری شبانه
🔹
توکیو، نیویورک و سئول در صدر شهرهای دارای بیشترین آلودگی نوری جهان قرار دارند و تهران با امتیاز ۷۵.۲، رتبه ۳۸ را به خود اختصاص داده است.
🔹
آلودگی نوری تهران از شهرهایی مانند ریاض، دوحه، زوریخ، ونکوور بیشتر است.
🔹
آلودگی نوری علاوه بر پنهان کردن آسمان شب، چرخه خواب انسان و زیست بسیاری از گونه‌های جانوری را نیز تحت تأثیر قرار می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671574" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شنیده شدن صدای دو انفجار در کنارک
🔹
از کنارک گزارش داد که دقایقی پیش صدای دو انفجار در مناطقی از این شهرستان شنیده شد.
🔹
براساس این گزارش، هنوز محل انفجارها مشخص نیست و صدای پرواز جنگنده‌های آمریکایی شنیده می‌شود.
🔹
طبق اعلام مسئولان منطقه صدای انفجارها از مناطق بیرونی شهر شنیده شده و اکنون شهر در امنیت و آرامش کامل قرار دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/671573" target="_blank">📅 23:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
موسسه اچ اف آی ریسرچ: فعالیت بندر فجیره در امارات عملا متوقف شده است
🔹
با وجود دو ناو هواپیمابر آمریکایی و پوشش هوایی سنگین آمریکا ، بندر فجیره در امارات عملا عملیات خود را متوقف کرده است.
🔹
با توقف فعالیت این بندر، حدود ۶ میلیون بشکه در روز از بازار حذف شده است.
🔹
این بندر اکنون «تقریباً مرده» است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/671572" target="_blank">📅 23:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hda3pRGPjBlwb8zekvS73PVOTqYURAPjaW-hXNN4TCRO3Z2EP1BDV21TSvixaKUmhM5bzoQ6qfQy4Colh7Ujj423yjH0btyl6iF-kGNQiRagra6QaG8RlZ4Z584VC3d6Uy2NCwF1ZVeqhsX0tjoybnYE_5NPMTkg2NOhFgrilRO56EVoTvgtCzGkgesJ3tbGHvH11c_B7QT9ie0HcSy3ho9QvONdPs1yGR3eHT8ogxYC8tfkPMgShXxxfyKJhXNHjtAQxOFzlgHKHSm9D1Ke4qEKL31TGEharjfSfOcD1zHmJXOeVmDU-iN_5EqkcZpkzIB9nhSLxhUaAYWvudnKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهاجرانی: داغ بمپور، داغ همه ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671571" target="_blank">📅 23:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4wVCMwvRNPrC-Lo9lMEgw4ciAsvwiIJ1IAqxT4OtW_hx5LYKaJQlyKLMhKSThHX2uvtVWYK2d1UBA2zCvE9-iY2_FUKnbW4fMl-Kphvc0hnYV8kLhsxI1I_Qi_gw7ak5kaSatZ21uwejTdVV3ypK6Y9DGVLqlJvImnv55u0-B16mskiLMvX3nVrI53kdnlU-8dyTUE0EqJOMdQPa-g8m4JYy48H1rpmlOjH95rELE3jNKgki-tAmAHxVoqZY6bNja-vJ4EhO9P0wYkH-zSNWvitvpxIRQ1tpROFG5n5fck7AtDvop66KH13l3waqVWFARycj03B_N_5IpwHOjInnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصول مومن بودن از منظر امام علی (ع)
🔹
امام علی (ع) در پاسخی حکیمانه، ایمان را نه فقط باوری قلبی، بلکه ساختاری شانزده‌گانه بر پایه‌ی چهار ستون اصلی (صبر، یقین، عدل و جهاد) و زیرشاخه‌های عملی آن‌ها تعریف می‌کند. این رویکردِ جامع، ایمان را از مرز اعتقاد فراتر…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/671570" target="_blank">📅 23:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
آژیرهای هشدار در بحرین به صدا درآمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/671569" target="_blank">📅 23:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671568">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار دیگری در اهواز خبر داد
🔹
منشا صدای اخیر هنوز مشخص نیست.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/671568" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671567">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYhUEtCLDMMcUK3DlScF1PPouqMAbLCIcpF0bKPheEt-H-ysLFvqwJQ4DYv5jfOqqC0WxwujNjMCrgi8WfNde1_pg-dxbRxoPGBr6loI0zGIdiciWbPCV3ls4YuySiQT1qohorkbr2MjEWoQpJ6RXwdAknDtlB3kZeLheWmLmd4s6GGgnEoliXpKGnVdxNA3TAQoEsObtVW9gXqGMXcosd6pVYuoGwSqdBJVMo6FvxIrqYPErl4vxdxrOEqkDYQefZ4um2_PUXi0XsRCcHZIZZ2DUSjpTkrHWFaI6lo0We5anv2dZVc2-ZEkcE4jpG43ewk10nrTGdGSv5o8piGhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ترکیه چه گذشت؟/ جلسه محرمانه‌ای که باعث شد ترامپ به فکر "جنگ بزرگ" با ایران بیفتد
🔹
به نظر می‌رسد یک جلسه محرمانه و مرموز باعث شد ایران و آمریکا وارد جنگ با هم شوند و درگیری ها دوباره اوج بگیرد و تفاهم نیز به سرعت از بین برود. این جلسه مرموز مربوط می شود به جلسه مخفی ترامپ با سران ناتو در ترکیه.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3230677</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/671567" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
انفجارها به بحرین رسید
🔹
منایع عربی از شنیده‌شدن صدای انفجار از حوالی پایگاه آمریکایی شیخ  عیسی در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/671566" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
انفجارها به بحرین رسید
🔹
منایع عربی از شنیده‌شدن صدای انفجار از حوالی پایگاه آمریکایی شیخ  عیسی در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671565" target="_blank">📅 23:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
صدای انفجار در راسک شنیده شد
🔹
دقایقی قبل صدای انفجار در شهرستان راسک استان سیستان و بلوچستان شنیده شد./مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/671564" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af223d3da.mp4?token=BTYgWg8or-7NHyUI7PYV8ClIlBNbCX-yDyYt5w1qiU9ZxboQ2eADJafNA1e1D2sFQXcQ1LvmJIsWwBi3woUpNAfDd1xSao1vBD1yg-yGfaCf1Yis2Ss1spEk6zQQ-g23Dzo_SszJIslvwUsPniGED9upK-nI914RuE0DYeEcBw9S9ptISDtP8xbs_81kel3q64SvqwO-K_NxhxSFeRlqhE5PhG2iMLctM9fhFzRJq0iOGKt8K0spttSHoaGRhEPvbxs5n9FkvDkY9NcYY6HDnX-tpemkVgQJFHero2nflQ_SbdJx01earqj5LotMc_gBETSukbcJ_Y9nlLtTITMkYUQbod7j_DtOe7e-diuRe5TBMtO2LY1ibMGFmjifwVvvjFgfiOER3NCCUin2_V9nglba5Hq7vaKyUJMXz3ahSflScj_nl8pULHl8D_swCrpE29KYspe_8mR-HgKS8rovL_WUI3vdGacJE7Ax8ik96RvvYQO0P3oXQSPJmqmF2-TTMhLLaB4wtcsSyv9OZDvgIrKjJdXj4b-dMJjRE23bYsJ5puqWfph9g4ATSdo_fW2Dlcq-Hzev-09ePzicSWK4krbBNilP1n-kgjtJfykVJ1fbOiuauwAYFNHrpLA1GeG309rxN3QdaaBNChgd42WJw91Aar1n94fuFIbPH93xXVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af223d3da.mp4?token=BTYgWg8or-7NHyUI7PYV8ClIlBNbCX-yDyYt5w1qiU9ZxboQ2eADJafNA1e1D2sFQXcQ1LvmJIsWwBi3woUpNAfDd1xSao1vBD1yg-yGfaCf1Yis2Ss1spEk6zQQ-g23Dzo_SszJIslvwUsPniGED9upK-nI914RuE0DYeEcBw9S9ptISDtP8xbs_81kel3q64SvqwO-K_NxhxSFeRlqhE5PhG2iMLctM9fhFzRJq0iOGKt8K0spttSHoaGRhEPvbxs5n9FkvDkY9NcYY6HDnX-tpemkVgQJFHero2nflQ_SbdJx01earqj5LotMc_gBETSukbcJ_Y9nlLtTITMkYUQbod7j_DtOe7e-diuRe5TBMtO2LY1ibMGFmjifwVvvjFgfiOER3NCCUin2_V9nglba5Hq7vaKyUJMXz3ahSflScj_nl8pULHl8D_swCrpE29KYspe_8mR-HgKS8rovL_WUI3vdGacJE7Ax8ik96RvvYQO0P3oXQSPJmqmF2-TTMhLLaB4wtcsSyv9OZDvgIrKjJdXj4b-dMJjRE23bYsJ5puqWfph9g4ATSdo_fW2Dlcq-Hzev-09ePzicSWK4krbBNilP1n-kgjtJfykVJ1fbOiuauwAYFNHrpLA1GeG309rxN3QdaaBNChgd42WJw91Aar1n94fuFIbPH93xXVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکرار و تاکید انتقام در پیام‌های رهبر معظم انقلاب
حجه‌الاسلام قمی، رئیس سازمان تبلیغات اسلامی:
🔹
رهبر انقلاب در اولین پیام، پیام شهادت دکتر لاریجانی و پیام به مناسب چهلم شهادت امام شهید، به انتقام و خونخواهی تاکید کردند/ این یعنی انتقام حتمی و قطعی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/671563" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان
🔹
هم‌اکنون صدای پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان شنیده می‌شود.
🔹
مردم منطقه صدای اصابت ۳ موشک و انفجار را مناطقی از شهر چابهار شنیدند اما هنوز محل دقیق این انفجارها مشخص نیست.
🔹
مسئولان امنیتی و انتظامی گفتند که تیم های عملیاتی به محل های انفجار اعزام شده‌اند و به زودی اطلاعات دقیق به مردم اعلام خواهد شد./تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/671562" target="_blank">📅 23:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای انفجارهایی در بندرعباس  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/671561" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
۴ نقطه در اطراف شهر اهواز مورد تهاجم دشمن آمریکایی قرار گرفت
معاون استاندار خوزستان:
🔹
دقایقی پیش ۴ نقطه در اطراف  شهر اهواز توسط دشمن آمریکایی مورد تهاجم قرار گرفت.
🔹
تاکنون این حملات تلفات جانی در پی نداشته است. /مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671560" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پاداش میلیاردی برای سرمربی تیم ملی
🔹
مهدی تاج، رئیس فدراسیون فوتبال، مبلغ ۱۴۰ میلیارد تومان از پاداش ۳۵۰ میلیاردی اهدایی از سوی رئیس‌جمهور را به امیر قلعه‌نویی اختصاص داد. همچنین تیم ملی ایران برای حضور در جام جهانی، حدود ۱۰ میلیون دلار نیز از فیفا دریافت خواهد کرد. در همین زمینه، یکی از روزنامه‌ها با تیتر پاداش برای هیچ به این اقدام واکنش نشان داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/671559" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40564f6cd.mp4?token=FW1FvLbbg6vAb66JK2HITP_ol9H4nHhVjg9ILk66ux4lMQj8rGx8yeLTPEbBMd_aFYTvO7sWL8EP-Tw8CSexH44iBfoqIZ7XCiBehqBpLBQPc5FNla32UF5OgZnhNwAl82eC44a3isVfzRPq6dvzR4bpUIc8wiftI_QiM6RAPECVDwcNFYQqAf9FEFzf_CwC7lOT-10lvvU7VtC9PhqkH3vFYt6K9cOJ3dChk-2PyTlF7rSJvf9R4MwxFWmXAQnKiGqJE8acM3d12urjYnQV8eW7Y7dFP3voHM3199Zhmfj4G2mLmhVgUNbfV54fMZdfddYk5kyoLmU2cgV2JzrEPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40564f6cd.mp4?token=FW1FvLbbg6vAb66JK2HITP_ol9H4nHhVjg9ILk66ux4lMQj8rGx8yeLTPEbBMd_aFYTvO7sWL8EP-Tw8CSexH44iBfoqIZ7XCiBehqBpLBQPc5FNla32UF5OgZnhNwAl82eC44a3isVfzRPq6dvzR4bpUIc8wiftI_QiM6RAPECVDwcNFYQqAf9FEFzf_CwC7lOT-10lvvU7VtC9PhqkH3vFYt6K9cOJ3dChk-2PyTlF7rSJvf9R4MwxFWmXAQnKiGqJE8acM3d12urjYnQV8eW7Y7dFP3voHM3199Zhmfj4G2mLmhVgUNbfV54fMZdfddYk5kyoLmU2cgV2JzrEPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به ترور شدن توسط ایران فکر نمی‌کنم
خبرنگار
:
🔹
تهدیدهایی علیه جان شما از سوی ایران وجود داشته است... آیا از ظاهر شدن در چنین موقعیت‌هایی احساس امنیت می‌کنید؟
🔹
ترامپ:
من حتی به آن فکر هم نمی‌کنم، چون اگر فکر کنم، خیلی مؤثر نخواهم بود.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/671558" target="_blank">📅 23:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای انفجارهایی در بندرعباس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/671557" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ae1b4fe0.mp4?token=dE1cI5Tzr43-bE9tzl1sxGDG_8RjDy0gK0YtBKKIItHB8PbpJCZF87-H9tmwQI7lxq4MmDNPDIRtfXhtYFtir8w2MxxautnmImoM5b93fycPVOCTQ561e_RlB2bniMxnSL0A-hIZgdvHyAWZGKrJPre4UmZOxr5FnHqo2DOW_0OjLgncNvSJf7kwGp5gVxgjhRCJ5kEDVCmqLLFDIAXz3bUlU8dQ3WJKPejkVktf9xve1rT-z8Bez3rih_6lZrSs2tUqZST_Hb4H8q8TIiyD6xN9GE9zFF67hXNkAohL0axTOpy8uXu1zXOjmaohzeIxYBd4BAG04BfYYFsH3M7hlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ae1b4fe0.mp4?token=dE1cI5Tzr43-bE9tzl1sxGDG_8RjDy0gK0YtBKKIItHB8PbpJCZF87-H9tmwQI7lxq4MmDNPDIRtfXhtYFtir8w2MxxautnmImoM5b93fycPVOCTQ561e_RlB2bniMxnSL0A-hIZgdvHyAWZGKrJPre4UmZOxr5FnHqo2DOW_0OjLgncNvSJf7kwGp5gVxgjhRCJ5kEDVCmqLLFDIAXz3bUlU8dQ3WJKPejkVktf9xve1rT-z8Bez3rih_6lZrSs2tUqZST_Hb4H8q8TIiyD6xN9GE9zFF67hXNkAohL0axTOpy8uXu1zXOjmaohzeIxYBd4BAG04BfYYFsH3M7hlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانی‌ها می‌خواهند توافق کنند
شیطان زرد:
🔹
آنها آدم‌های بدی هستند اما می‌خواهند توافق کنند
🔹
می‌توانم به شما بگویم که آنها می‌خواهند توافق کنند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/671556" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=dcLUYs4-0rVSE6j8_38x2NYq_7yE04aysTK_BKW0j0hBQjcf_Hgq9bfamxkHlwSIpumo2Ds9GW6tIZeSICqONvffQQAMXAFA7qhZv8JDReD73exCcysx2oeYwaK0v-7Cu2VMIm-dUPUaOxc6drAhXR60PXGLzxwvATH0EzuQyppkqHo460nQ47fXwLWVi9Y51s2czQhKnCLTZUfHFe8L6SKcFok65hCnJg59R4iiowWDTprwTJDJkFd15w37dS_5S8r_GrZDBH3ZXz4RBHjUoCOuNqz-iF4ucC30eUDZoPf50YaL_0Wk0u9FZJ_pGhHREqzjkuLiw4FxEl5kO-UPOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=dcLUYs4-0rVSE6j8_38x2NYq_7yE04aysTK_BKW0j0hBQjcf_Hgq9bfamxkHlwSIpumo2Ds9GW6tIZeSICqONvffQQAMXAFA7qhZv8JDReD73exCcysx2oeYwaK0v-7Cu2VMIm-dUPUaOxc6drAhXR60PXGLzxwvATH0EzuQyppkqHo460nQ47fXwLWVi9Y51s2czQhKnCLTZUfHFe8L6SKcFok65hCnJg59R4iiowWDTprwTJDJkFd15w37dS_5S8r_GrZDBH3ZXz4RBHjUoCOuNqz-iF4ucC30eUDZoPf50YaL_0Wk0u9FZJ_pGhHREqzjkuLiw4FxEl5kO-UPOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ایرانی مقیم خارج از کشور: ایرانیان مقیم خارج جنگ‌طلب نیستند، ما نمی‌خواهیم کشورمان بمب بخورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/671555" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671554">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psyIWUT8GHuZ9TD7QUJpfYX3QI0dSCH2G2XvSqIB6ACRM34s5pDm8japkslBKDtmFWdmDd-LTsKN4339VN8SlebELrjQCCvrKpLAyyDHzsO7nvTg_7FDuEn2WN3unxOQfwaDkQAI6t2ifmU6dhKJ14kQe-pQwFEucYMwuaelhzQfcRWvcNOJTpxi2TeTg_bxqVJe82XuTUwU8nLIUtBioZ098qF02YCqDFYjgCLgjmiffm0ueTQcIw7vKPXWotNsSQokLARKjtNLMZnf1dFJ436kqVbKmltymmDSvMsrbuLL1iKa_Avc9fYJRsw18wgvL8PMzLwTWyg69gEqc3wJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای بوئینگ‌های مرموزی که در مسیرهای جنگی پرواز می‌کنند
🔹
تحقیقات رویترز نشان می‌دهد شرکت‌هایی تحت کنترل یک کهنه‌سرباز نیروهای ویژه ارتش آمریکا، چند فروند هواپیمای قدیمی بوئینگ را در مسیرهایی به کار گرفته‌اند که به شبکه‌های تأمین نیروهای واکنش سریع سودان مرتبط بوده است؛ گروه شبه‌نظامی‌ای که به ارتکاب جنایات گسترده، از جمله اتهام نسل‌کشی در دارفور، متهم شده است.
در خبرفوری بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3230659</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/671554" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر اتحادیه املاک تهران: برخلاف گفته دولت، اجاره‌بها ۳۰ تا ۵۰ درصد افزایش پیدا کرده است
سعید لطفی، دبیر و عضو هیئت رئیسه اتحادیه املاک تهران در
#گفتگو
با خبرفوری:
🔹
اجاره‌بها تابعی از قیمت تمام شده مسکن است، با توجه به اینکه افزایش قیمت مسکن  داشتیم، قطعا اجاره‌بها هم نسبت به سال گذشته افزایش پیدا می‌کند.
🔹
برخلاف گفته دولت مبنی بر اینکه نسبت به پارسال فقط ۲۵ درصد افزایش اجاره‌بها مجاز است، به‌طور میانگین بین ۳۰ تا ۵۰ درصد افزایش قیمت در اجاره‌بها اتفاق افتاده که این موضوع با توافق میان مالک و مستأجر انجام می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/671553" target="_blank">📅 22:55 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
