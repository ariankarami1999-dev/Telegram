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
<img src="https://cdn4.telesco.pe/file/D2gMOXsrmo1xfjw5akw12kNWHf3xaE8zWgVu_4dPfupUkIAmstyEfMLebjTyrfoAsKb73hdchgda1okfHxYCDghPMxT0WKoZtmal-SJHlqYqBVQmH75hmFw-6tcm8mvrSMcznpzt8ATSKR0tG46ZqvXhSUZU7tWqzAM2W97JPPHyp0SdANlgab3KtbMahkADgZyTdGR_0i9hZCYYD6TqBVZT05a79yCT-YYPid855lpQdvij8uhT3PkY0_P38E3wJ7mg_H-r32AkyJL040rG2mVq33JRVkLSIQicQmcictIrctjyDYK6jvX51shVpagpgdlmTj6AZxDjVN7ma4GGRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-654325">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHNS9fNH5Fq7XeJ0pjc3CRhlH6jYLlLvt8Q0X7-4Dgw6L_mnHSiB-R8X1IN7JyM4N2PjI-B1m-awC8aSjfPuYHy6fcu4IqXHDSzL6cZfxcXO3yxTO5eVVBHGpomrqFDRdY3P7jDonarwnMkRz6Hpzm5CqBepIN21b2DSZoja_Eg2AHuUVBNXnHvO2ZHLmAHYbsuyt3qqYGZvhK3YzVnqIDZvZm9zdYul1k8oCks1DNcpJmgjCHTeiJqrCefHgD7ndpaw0iAngLPP9jxvg4Y8qQpDFq6p272ShkKTna2X6KaP-7TnBLspyVJUAyfrRxrdnnpFhYomwKMWREkq0RturQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیماری‌هایی که ممکن است حین ذبح گوسفند به انسان منتقل شود
#سلامتی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/654325" target="_blank">📅 17:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654324">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای تازه کاخ سفید درباره توافق با ایران
🔹
به گزارش الجزیره، کاخ سفید مدعی شده است که ترامپ تنها توافقی را امضا خواهد کرد که به طور قطعی تضمین کند ایران هیچ سلاح هسته‌ای نخواهد داشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/akhbarefori/654324" target="_blank">📅 17:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654323">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3knYYBLWJRqpvy8Apd14YizkIvjCA0yBQvrNy6K7jP2b07TLZAsgLe32bXBC-Ft5pRaLz-7MTPznYBbSQ9uw2hF5egnt8x7d1Q26M8VxKFO_6rg2SPJtVNgH7Bjrm2FkkcgCglTNH4B0u91cWM20usFn_pbGuN0Y6iUjZwThfvj6G0DlV57S9e9db5RFMJOeboiwrMcjTEevIKt4dYFv8x3bdi4gawqvEZvUIB2sgE7LbtWa5vqB4ZS7OZBZaM9zYTG29mQewRLFhooRV2MrzDe6gA4hgQ4wkDZUrDD3TRMHl3sg2msSW4_MsEINa2MQgq0N_EI08UohQJFepoSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار به مناسب عید قربان؛ دستخط یادداشت شهید دکتر علی لاریجانی از متن مناجات امام حسین علیه‌السلام در دعای عرفه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/akhbarefori/654323" target="_blank">📅 17:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654322">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHbWVqNG5t1O1LBbvrhqvDfZL0jAN5CBh59ckLD2cutRFanxXSu6t_CeFlJMITqFnmCdJPrmobEGdX7Flr2DMqWrX4n0T4WuY3vvQGp2UF3TpjiUdalJf4JJLqAqzta2t_9eTiXjaHwJPgOB3RbX5OiuEGKLW6AyDnD0EeLH_OTa2fQ2Y2ok1CcrbbUJQnBlOkJ9HUj0oRUajKEVlct2TIdAM1xPxt0FeDEixHIb2wM1E1M1wd27pOW3l_MHOMxrRJMGJ_sdAo6v5JxOdHD70588MD_Gi4k_KNXafwfwgWy2QhkujkaMq8bnLejFyHRoZ_YWTVQTL_Uu5qWq4SN9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل دستور تخلیه بزرگترین شهر جنوب لبنان ‌را صادر کرد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/654322" target="_blank">📅 17:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
آتش‌سوزی در فرودگاه امام خمینی
🔹
دقایقی قبل یک ساختمان اداری در شهر فرودگاهی امام خمینی دچار حریق شده است. این حریق در یک ساختمان اداری گمرک شهر فرودگاهی امام خمینی به وقوع پیوسته است.
🔹
تاکنون از علت دقیق حادثه و میزان خسارت و تلفات احتمالی اطلاعاتی در دست نیست. نیروهای امدادی و آتش نشانی در محل حاضر هستند.
#اخبار_تهران
در فضای مجازی
👇
@AkhbarTehran</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/654321" target="_blank">📅 17:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654320">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRNC2QoWCdmWyffmz5fQmKnzskMqrPds26kizWFz8mMYXdkyqqc-TWwSgzYhLzvq77DeRrTc529d3dlxgph-9MapYv-1LKUkpFNxH_RmVF4An_AIwGj8X6su8VWGuqWSqz4WLK50F9IBU2ks1MRcPO2VQ0QLW76s9z2lbrE6aL7UOHn5eIOpBccNT-OJE4ZfHcGiQ536-CD_RK7y7SkdOmS0Z0pi1ReC3VfZFMDpf7h3B6CYdzVL6nHv8HvnOziCpRnBXmq5j2cG8rf-n-Ytr9ozSPl0wJKzmxhZrgt374NgGq6dfefr0-N-ija_mnkHZAs7GaLJ6d3hInS6q4gfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناسا قصد دارد تا سال ۲۰۳۲ پایگاه دائمی در ماه بسازد
🔹
امریکا قصد دارد پیش از پایان دوره ترامپ فضانوردان را به ماه بازگرداند و سپس یک پایگاه کاملاً عملیاتی بسازد.
🔹
ابتدا مأموریت‌ها توسط ربات انجام می‌شود، سپس ماژول‌های مسکونی، سیستم‌های ارتباطی و نیروگاه هسته‌ای ساخته و به عنوان سکویی برای سفر به مریخ استفاده شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/akhbarefori/654320" target="_blank">📅 17:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654319">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
الجزیره: جلسه ترامپ با کابینه برای نهایی کردن توافق پایان جنگ با ایران
🔹
در وضعیت فعلی، ترامپ این ریسک را دارد که پایان دادن به جنگی که خود انتخاب کرده، با پایانی نارضایت‌بخش همراه شود؛ زیرا توافق در حال شکل‌گیری، بسیاری از مسائل حیاتی را به آینده موکول می‌کند و این مسئله او را در معرض انتقادات شدیدی قرار داده است آرای جمهوری‌خواهان را در انتخابات میان‌دوره‌ای در خطر قرار داده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/654319" target="_blank">📅 16:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654318">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9QJ6PjefniobjyOHkwA3Rw7Qcm2up21OtZi1UtFln_JWYj1q9qrYrQE4a5JsHnge2kva8eISItN-sEEvcBSz_E3QbwKpcoLvq5OKiDJfzbkEOTLyIakn-qvaSNas8ymzLEYnvfi54Cw0CmT7H14dPBfyJqaQg0lVFo3atbTyRn_pQbm2yO1Xgr8PmWUTNrcY10IOb11HMshuFg0L_v-rEzYu9TkJvrq3RiIpFaEAzJMMVxjyyGqiiOHgpHYtIgn2zyaavZ97gWGcgZs966u3C-vAvnLWRET6SIGPdAGfoD2a_mQQ8h6sVhlZ1kDHPLVxXt0KIPUjhekdEgLtnAoxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین قیمت نفت: ۹۵.۱۰ دلار
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/654318" target="_blank">📅 16:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654317">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
اقدامی برای کاهش هزینه درمان؛ حقوق گمرکی دارو فقط یک درصد شد
🔹
دولت، حقوق گمرکی دارو، ملزومات مصرفی پزشکی، شیرخشک و مواد اولیه آنها را به تنها ۱ درصد کاهش داد.
🔹
ارز مبنای محاسبه حقوق ورودی این اقلام، دیگر نرخ‌های دستوری نیست، بلکه نرخ ارز مندرج در ثبت سفارش تعیین خواهد شد. به شرطی که وزارت بهداشت عبارت «ارز ترجیحی» را در اولویت گروه کالایی ثبت سفارش درج کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/654317" target="_blank">📅 16:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654312">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
باقری: ایران و عمان به طور مشترک در حال مذاکره درباره سازوکار مدیریت تنگه هرمز هستند
معاون دبیر شورای عالی امنیت ملی:
🔹
شرایط و رویه‌های عبور از تنگه هرمز کاملاً متفاوت از شرایط قبل از شروع درگیری بر سر ایران خواهد بود.
🔹
تا زمانی که در مورد همه مسائل به توافق نرسیم، فکر می‌کنیم که در مورد هیچ چیز به توافق نرسیده‌ایم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/654312" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654311">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
رکوردشکنی خیره‌کننده بورس کالا در اردیبهشت
🔹
آمارها حاکی از آن است که درآمد بورس کالای ایران در اردیبهشت‌ماه به ۸۶۳ میلیارد تومان رسید؛ رشدی ۱۲۶ درصدی نسبت به فروردین‌ ماه.
🔹
درآمد کارمزد معاملات نیز با ۵۷۵ میلیارد تومان، رکورد قبلی مربوط به بهمن ۱۴۰۴ را ۳۹ درصد جابجا کرد. درآمد انبارداری هم نسبت به فروردین ۳۸ درصد بالا رفت.
🔹
جمع درآمد دو ماه ابتدایی سال با رشدی ۱۶۵ درصدی نسبت به مدت مشابه سال قبل ۱۲۴۴ میلیارد تومان شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/654311" target="_blank">📅 16:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654309">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
مقتدی الصدر دستور انحلال سرایا السلام را صادر کرد
🔹
رهبر جریان صدر عراق، امروز دستور انحلال کامل سرایا السلام(گروه نظامی این جریان) و پیوستن آن به دولت و مسئول کل تشکیلات نظامی خبر داد.
🔹
بعد از انتخاب علی الزیدی بعنوان نخست وزیر عراق زمزمه‌های انحلال گروه‌های نظامی غیردولتی به گوش رسید و این اقدام صدر در راستای این گفته‌ها اجرا شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/654309" target="_blank">📅 15:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654308">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqQw_TTEm6x-ltGzSieAuN1FsSE57B7fXnVjD2zYfn0hdUEz1iiQi5ovNo7hdGGzWjBhcs_OpwDJHb5vPjiP_JYWoKDzySPj-N30yhgZotINc_oK50STHMlasrw_WM37Ge2vySzacAbIFZGznx0EHu-s_FyYuiu4gNBAv_YmJhDlgwuQLB8odeYJWR3ItZqr5JcH3gyO6xpPh91-uKlJolXQeE2Bs6NrYavyF7fKTgeO8ZtiuIaNF7aq0vdB6fLurbH02OL_Pc_ao61yxODBiCVY_-5-gSElpcwAy0Ga0U_Jda5cCfOJ3jC0uS1HWEqGNlcYPIGWHeD1hdtqJfXCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل‌گر فاکس‌نیوز: ترامپ ناچار به دادن پول به ایران شده تا آبروداری کند
بجسیکا تارلوف:
🔹
ترامپ به یک توافق با ایران نیاز دارد، اما نه برای هسته‌ای برای آبروی خودش. او در آستانه دادن «پول قابل‌توجهی» به ایران است، آن هم در شرایطی که محبوبیتش پایین‌تر از همیشه است، قیمت بنزین به ۴.۵ دلار رسیده و کشاورزان آمریکایی التماس کود شیمیایی می‌کنند.
🔹
ایران دیگر تهدیدهای ترامپ را باور ندارد. توییت‌های زیاد و وقت‌کشی‌های مکرر از سوی تهران، قدرت بازدارندگی واشنگتن را صفر کرده./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/654308" target="_blank">📅 15:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654307">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT2G-NU70c9OwTNlO2XI6xIiNO8-GpBHJqP7qkmLeCwgqa6JbpuNTc2lQCqw1VvSdVqIIwZMa24ZrJjybTir2vSh55iiX3V1C5bFKeQvAOc23aldoFT8A1qNAOtQ7iHJpHyH_jku5Ypb_xM6XLXDVgdkKdsgeHQcIMAURDFtjK_Ixx9o2AhPBS8xXCy2UhfdxY4YgzAwRHzZ0NlppX7NXYnPniWlp6d7AuRSUY3MREcOGu6zX0_7oaO3zWFXKc5amTGQJqcbSSTofxnsWNL8ztzeXUYMLrNlYEAZgo49aB3WdGbce4M0rgM-PXPqOX-GUE2VlccB6TtQ5hWcy2RmBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین مدل‌های هوش مصنوعی به تفکیک کاربری کدامند؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/654307" target="_blank">📅 15:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654306">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زارعی: ترامپ نزد مردم ایران به ۵ بار اعدام محکوم شد
مجتبی زارعی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
پیش‌نویس‌ها و هماهنگی‌های اولیه درباره طرح ترور ترامپ در کمیسیون شکل گرفته و پیرامون قصاص فعلا مبلغ ۵۰ میلیون یورو تعیین شده است.
🔹
ترامپ به خاطر کودک‌خواری در جزیره اپستین یا توسط آمریکایی‌ها کشته خواهد شد یا در دوران ریاست جمهوری توسط خونخواهان به درک واصل خواهد شد.
🔹
ترامپ مثل سلمان رشدی برای همیشه باید با تجارت و قمار خداحافظی کند زیرا اگر از دنیایش یک روز مانده باشد حتما قصاص خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/654306" target="_blank">📅 15:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654304">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ریابکوف: سرنوشت اورانیوم غنی‌شده موضوع گفت‌وگوهای آتی خواهد بود
معاون وزیر امور خارجه روسیه:
🔹
پیشنهاد روسیه برای خارج کردن ذخایر اورانیوم غنی‌شده از ایران همچنان روی میز است اما مسکو کمک‌های خود را به کسی تحمیل نمی‌کند.
🔹
روسیه بارها به آمریکا اعلام کرده است که آماده است اورانیوم غنی‌شده ایران را خارج کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/654304" target="_blank">📅 15:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654303">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
جزئیات اولیه از چارچوب تفاهم احتمالی ایران و آمریکا
صداوسیما از انتشار سندی غیررسمی پیرامون تفاهم ایران و آمریکا خبر داد که محورهای اصلی آن عبارتند از:
🔹
رفع محاصره دریایی ایران و خروج نظامیان آمریکا از محیط پیرامونی ایران.
🔹
بازگشت تردد کشتی‌های تجاری به سطح پیش از تنش‌ها توسط ایران (طی یک ماه).
🔹
مدیریت مسیر تردد کشتی‌ها با همکاری ایران و عمان.
🔹
تبدیل احتمالی توافق نهایی به قطعنامه شورای امنیت پس از ۶۰ روز.
🔹
این چارچوب هنوز نهایی نشده و ایران بر «راستی‌آزمایی ملموس» پیش از هر اقدامی تأکید دارد./ میزان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/654303" target="_blank">📅 15:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWvSyGopHVhDsuXbNE4owHPVXXonWK0VOmPxhIaIQes_LGh_4avY--qQIA4aYKaojRl-Wlhn8m0Kvpz2TybG8INM-L03DUcneBllOhMWT2kcf2TFxFkiGIrXifW8yTWb4khZ69vQOejaL8cRI9KO7nhrxDwxv7nxD4-pcp12UvmMTou20B1ywTYcC4Fw-8Iaa7xiQbcoulOBV1KT7-EKSY0JwSb4S7-Uvbf4mZMEoHx4Yruts4l_FtwtlyTRaNQIxjW7mNTdts_23_WyH_qB4B_AzpUl1E38BqjmlGGlTHO-omjTE_ZRAqiz00_9sy7oNUHpHRvwppUDcG4CSwg9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: ترامپ برای رسیدن به توافق با ایران، باید تحقیر را بپذیرد
نیویورک‌تایمز:
🔹
ترامپ برای رسیدن به توافق با ایران ناچار است «به‌ میزان قابل‌توجهی تحقیر را بپذیرد» و از سیاست «فشار حداکثری» که خود بنیان نهاده عقب‌نشینی کند.
🔹
نویسنده با اشاره به اصطلاح “eat crow” در فرهنگ سیاسی آمریکا تأکید می‌کند که شرایط کنونی ترامپ را مجبور کرده به سمت امتیازهایی برود که پیش‌تر آنها را نشانهٔ ضعف می‌دانست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/654301" target="_blank">📅 15:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: عبور شناورهای کشورهای متخاصم از تنگه هرمز همچنان ممنوع است
🔹
۲۳ شناور تا این لحظه از تنگه هرمز عبور کرده‌اند و عبور شناورهای دیگر نیز تا ساعات آینده ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/654299" target="_blank">📅 14:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654298">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNC4pVgAv2uLelXESOZeN3DVWnGtRoL2HE0SaBZFjC6aR1GklCBKqwcKydeXd-3sXA4aJvzGek6yPgkPIZ78DyYM9h59S71xMTTvbbwt7H-qgJdNY-8xS-iz4rcI7zHZsbV4d6KY8QC6qVvmpAQoPpVq_zbtvmw44IVeUQ1AAR8lZtcMT1icbzw0355KVcuNLQDIQUurUsY3durIei29wZo8bcsJ1xXAcMUKbpf-s8tSTr8DCbbtw41TnH_gEZGKnRUyhhJl2rOKwOk8v6b1qUrf8qJ-EJy40qVjrPs9X18-NuuRpbNXBMvRCZTJ1jsji_7xyz_fs6GVwP_ZT9jTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب ماندگار حضور رهبر شهید انقلاب در مراسم حج سال ۵۸
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/654298" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654297">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea96298df.mp4?token=kl9rBpmtI3hPRMfyb2fxlAL0GGqzZXIXmVSxNIgl28Pz1x-PTTlPl9IBXweH4nLZYy7gtWWyAWxzUrCobGts5ULGt2aoLjGVlw-Zyk3uAYll0urWq8eMlfNQaNoky7DjtqAvGAIqoNJj8P0RsVVKbjcAcxNoRq-QHUAyW0AZbJ9PiiGG2bvgvt5AuYwwXbilY72Xu5dk0ZtsH8Qn5YxrfAfZWQbxQje65jthvrkR90av4upVCwX0NiTk9J24vxZFQC4sHwlO_XZZFvBl7isR-fdSvha74rzS9gS2FHLH4j-cRzNLkNHK73n7OiiV0vNPyj2B8gCDw_xGJlu__9mcJnHM76xCw065zikoW-0hyNNrJKjBdz8Srs6m0GUoRbO4TA51SRTlZyv2GX_hMI2YMgxIqVS4XZH4zsWrC1DanfCmXzxnOjVEX0KFPT_1aUTTNRLFiX5YY_OLB3iyivzqJyTTrstXyURXX8QKxsTNgP341robsIpjEZxVKUsh4ZoQ21EXw1qEeAaN86kvhe6TIQB4oy92RKSOcWWBAxuIhtBK5XSIAQTFmHyGxNbjHse186EDYtbYphOsTkrVHfyaJ6eGDsuGJZkO6TMZV4y46OqQNjKrGZcV1f3WQ7awAbea8Vn_1xvbFKAWvrwa3Dw5BuHL2fuT_5DuvuJE04GbJIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea96298df.mp4?token=kl9rBpmtI3hPRMfyb2fxlAL0GGqzZXIXmVSxNIgl28Pz1x-PTTlPl9IBXweH4nLZYy7gtWWyAWxzUrCobGts5ULGt2aoLjGVlw-Zyk3uAYll0urWq8eMlfNQaNoky7DjtqAvGAIqoNJj8P0RsVVKbjcAcxNoRq-QHUAyW0AZbJ9PiiGG2bvgvt5AuYwwXbilY72Xu5dk0ZtsH8Qn5YxrfAfZWQbxQje65jthvrkR90av4upVCwX0NiTk9J24vxZFQC4sHwlO_XZZFvBl7isR-fdSvha74rzS9gS2FHLH4j-cRzNLkNHK73n7OiiV0vNPyj2B8gCDw_xGJlu__9mcJnHM76xCw065zikoW-0hyNNrJKjBdz8Srs6m0GUoRbO4TA51SRTlZyv2GX_hMI2YMgxIqVS4XZH4zsWrC1DanfCmXzxnOjVEX0KFPT_1aUTTNRLFiX5YY_OLB3iyivzqJyTTrstXyURXX8QKxsTNgP341robsIpjEZxVKUsh4ZoQ21EXw1qEeAaN86kvhe6TIQB4oy92RKSOcWWBAxuIhtBK5XSIAQTFmHyGxNbjHse186EDYtbYphOsTkrVHfyaJ6eGDsuGJZkO6TMZV4y46OqQNjKrGZcV1f3WQ7awAbea8Vn_1xvbFKAWvrwa3Dw5BuHL2fuT_5DuvuJE04GbJIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضرت موسی فیک در آفریقا ظهور کرد
🔹
یک مرد آفریقایی به همراه چند تن از پیروانش قصد داشت تا معجزه حضرت موسی را تکرار کند اما با شکست مواجه شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/654297" target="_blank">📅 14:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654295">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgAubtakouCyq73bmkj29uIJw98M6pu9Z8fl3CGDYhW0or1VSwQKaQSZh3B4nlmZnGK5lR0L8zJh8VrmuKYyuVGjWW43lBgwO-EOQMsjocxNROqDDtmE7FZG-JadrbUIrvk2QonUGnGWrJQDaFeyMGQRe3_Iu_U1jmvjuAV5tCiH1Fph3BmhjOb68AnRmqYxYob_sV81QymuD23OD_Cf8uHCfxJ-2TVnGj0Qxes9kZNl4PxFVg6g89n526pF8_XMwu3MK7fMYnsC4EoDRY2N7klswE4D2Y-ZWUK2li64OPtwx4C3YvKnOScxzTjpVWyq1d2AyrUB2oKzJ-ga2SaW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر ارتباطات: ملت ایران شایسته ارتباط آزاد، آینده روشن و اقتصادی پویا هستند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/654295" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654290">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای کره جنوبی: حمله به کشتی باری ما در تنگه هرمز با یک موشک ایرانی انجام شد
🔹
کره جنوبی مدعی شد: ترجیح ما بر این است که «حمله به یک کشتی متعلق به شرکت «اچ‌اِم‌اِم»در نزدیکی تنگه هرمز، با یک موشک ایرانی انجام شده است.» سفیر ایران را احضار خواهیم کرد تا نتایج تحقیقات درباره حمله به این کشتی به او اطلاع داده شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/654290" target="_blank">📅 13:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654289">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc51083d4c.mp4?token=TIWwMtcNdl-LK5YSK6CVZgjQ8RVlsYnJFaE-rjl0xSyiXcRikjSSvyQSPflNbZCn3irXKhSqzr-uXJvXIgDQMvqNmwsCpAcgQSbCmIpfApV8VDN9m7un5INiCXaewtsQkAl0WaLvRR2OJjkTTQiPflYDKqFSsC0nTgW1bp5FmnTz0kOdKgbAG-pxlTU9sTF4Y7YrDVS3n9Od3ePyHXGNfhA_NHNODWxfUHck4ClSs_vKh_CX8fOpDsWKkHCyPITwaNUs2D8GQDelTNTes-QjxzyGNKYWL-zAjTAiWx5oAI-AouGbsO86ixpMPflkt5ARp0i2cwV5LZII4EH7Tpegtk0NPm7OI8EoZnGZuCwIgz4dJqNcwInE45lzCSQwITnIkmQvgBGTOy9XFN0y-67tBJDVJOStldI6Y9U1Q-9rlIHlryK56ufZABVrutSgTKrD9w0wva5I4g_HmD8CLZenG3901LhdA-CpuJf3qLXgpVIwsa6tHzC3efCHtfyaYW2SSNTCKTpemAlnFI-3WZ5BHUyEccpfAM37oriqk4WdYiPFjXF0KIf9A_8CiH1594Zn3u5XhQa7bSH_EG4ekAmWLvF-O-_NwxRKM5eYMKhnWMAsdZqzLvaWvD0bliML2FpP4bdAPN9BAn7G3IMWZDAu6LzzWvPl4UG0bVxDAxsbKCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc51083d4c.mp4?token=TIWwMtcNdl-LK5YSK6CVZgjQ8RVlsYnJFaE-rjl0xSyiXcRikjSSvyQSPflNbZCn3irXKhSqzr-uXJvXIgDQMvqNmwsCpAcgQSbCmIpfApV8VDN9m7un5INiCXaewtsQkAl0WaLvRR2OJjkTTQiPflYDKqFSsC0nTgW1bp5FmnTz0kOdKgbAG-pxlTU9sTF4Y7YrDVS3n9Od3ePyHXGNfhA_NHNODWxfUHck4ClSs_vKh_CX8fOpDsWKkHCyPITwaNUs2D8GQDelTNTes-QjxzyGNKYWL-zAjTAiWx5oAI-AouGbsO86ixpMPflkt5ARp0i2cwV5LZII4EH7Tpegtk0NPm7OI8EoZnGZuCwIgz4dJqNcwInE45lzCSQwITnIkmQvgBGTOy9XFN0y-67tBJDVJOStldI6Y9U1Q-9rlIHlryK56ufZABVrutSgTKrD9w0wva5I4g_HmD8CLZenG3901LhdA-CpuJf3qLXgpVIwsa6tHzC3efCHtfyaYW2SSNTCKTpemAlnFI-3WZ5BHUyEccpfAM37oriqk4WdYiPFjXF0KIf9A_8CiH1594Zn3u5XhQa7bSH_EG4ekAmWLvF-O-_NwxRKM5eYMKhnWMAsdZqzLvaWvD0bliML2FpP4bdAPN9BAn7G3IMWZDAu6LzzWvPl4UG0bVxDAxsbKCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سکانس فتح خانه کعبه در فیلم سینمایی «محمد رسول‌الله»
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/654289" target="_blank">📅 13:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654287">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سرگئی ریابکوف، معاون وزیر امور خارجه روسیه:  مسکو واشنگتن را از آمادگی خود برای انتقال اورانیوم غنی‌شده از ایران مطلع کرده است و تأکید کرد که این پیشنهاد همچنان مطرح می‌باشد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/654287" target="_blank">📅 13:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654286">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
وزارت اطلاعات: دشمن پس از شکست در جنگ نظامی، جنگ ترکیبی را تشدید می‌کند
🔹
از ابتدای پیروزی انقلاب تاکنون، ۳ جنگ تحمیلی و چندین کودتای نافرجام به سرکردگی رژیم صهیونیستی و با همراهی آمریکا، انگلیس و برخی کشورهای عربی، علیه ایران طراحی شده که همگی ناکام مانده است.
🔹
با وجود شهادت رهبر، وزیر اطلاعات و جمعی از فرماندهان ارشد، کشور همچنان پایدار و استوار مانده و نیروهای اطلاعاتی ضربات مهلکی به رژیم صهیونیستی وارد کرده‌اند.
🔹
هرگونه اغتشاش، جاسوسی، ارتباط با رسانه‌های تروریستی و اقدامات تجزیه‌طلبانه با قاطعیت پیگرد قانونی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/654286" target="_blank">📅 13:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654285">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpmfQBGccc2Ws-SQqY9fetvTMP38jPX1j5KGT_1RUhJh_xJgINqTed29HptKuzPS1lDZtiioaZAtPDGaa2Fcxawxd4MA318PEL0by4nb8YRydKNrzp7qaIbLWET1hdpCMBLENGo56NZl3M16lL0Ot94p0QeQMaaEcmm7tyV2UNSXyYJ4hSoJm6vl6wcXKAd_eV1IlKTTPU030NTiJiwAVN-5fFyZ1F2z7tfQtUoTjeCPyGgfDHI-d6Hz1Q2zoNputDOdRgdV-Mq4Y-ux8PiQyMMoXHHZrEm4rzhKzMslvdirMKUNo2V4FSR_b0dLp6tQfpOa6f-a1v7dPci9kQ_71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت فرمانده ارشد کتائب القسام تایید شد
🔹
جنبش مقاومت اسلامی حماس رسما شهادت «محمد عوده» را تایید و لحظاتی پیش، طی بیانیه‌ای اعلام کرد: در سوگ شهید قسامی، فرمانده بزرگ مجاهد محمد عوده (ابوعمرو) که استوار و سرافراز در میدان‌های جهاد به فیض شهادت نائل آمد، نشسته‌ایم.
🔹
شهدای این حمله پنج نفر اعلام شدند. محمد عوده، معروف به ابوعمرو، همسر او، ام‌عمرو و یاسر، یحیی و جمیله فرزندان آنها.
🔹
محمد عوده از فرماندهان ارشد کتائب القسام بود که از او به عنوان مرد در سایه نام برده می‌شد و پس از شهادت عزالدین حداد، فرمانده کل کتائب القسام، از بالاترین فرماندهان این کتائب به شمار می‌رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/654285" target="_blank">📅 12:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654284">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHuo_UDa_wiyTTaPatlAElRQnyXX2IJbipVBFbV3y68cV1PxlLi-5V1XOc5r6CcnHmf4FHy5OvfwO8Jd1-wCF3EvbNlwiK7wgZKy9InMwUcTJdeGyVsFW0cYKwB1dlCrcxyyDDEXMfCNTiUNlxnAJwlzXIl4pTO10IcDrO8fA87qqNAA2kzflaPCkVHtt_gIa6zanbOj1zL7FHUJsXfLZvPwmoewYnnpYq0xw_vzWuztkiFetdAIHpGLTeq49u4gDvcY-BF_QqitVKqnCqHO9KLfK2IT729MgC03QTm5RDxc7NFo-YRrXqpJ23fDu9X1jY7WCULa7UfF7myX80Ej0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراز امیدواری ونس نسبت به توافق هسته‌ای
🔹
معاون رئیس جمهور آمریکا خود را «بسیار امیدوار» توصیف کرد که ایران به عنوان بخشی از هرگونه توافقی، با عدم توسعه سلاح‌های هسته‌ای موافقت خواهد کرد.
🔹
اظهارات جی. دی. ونس درحالیست که ایران طبق فتوای رهبر شهید انقلاب مبنی بر حرام بودن توسعه سلاحهای اتمی بارها هرگونه تلاش در این زمینه را رد کرده و آژانس بین‌المللی انرژی اتمی نیز در گزارش‌های خود چنین موضوع را تایید نکرده است.
🔹
او افزود: «فکر می‌کنم سؤال دشوارتر این است که آیا آن‌ها با آن نوع از مکانیسم‌های اجرایی و نظارتی موافقت می‌کنند که به ما این اطمینان را بدهد که در آینده توافق را نقض نخواهند کرد یا خیر.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/654284" target="_blank">📅 12:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654283">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632271636a.mp4?token=XqwHgyjAAK076LCpWjyEMU69D2QdpyPJkoVV8wZY-OvucJfICYk64W46xk66xHbvWFRjqqfPdxXcwFH8o16CXEUgwMx45Iajd7J0IcnYfswviZEztntJ4JN4YBA-pDABumnSK3hNA16XzfC6WzI5BQBhhOJaYvtR29Ar-XzrUhea7VWfQSxDTCGIFeVSEg4j3TWDe1Ay82U2UKMz9_VX8hDLRf0oQ3rHbOG8NuV18VMoCBNFdmheyqCw8cxv5hwOQ_f8uRQD8l54Yilh1XPxIq0Vn-LT6-MVXE71pUD3f4AaODOnxmIbb-5Ny1Bcv__nUENgeOqi1_Q9wpbtPDNtA0f3R90TpoS-cHJXqFLXeUiqm4db18bzPrzN2r-zqRMUgh6Qw4u3dAZYR2iCmbBDgho5_IozmkW73KfJd2L7YdPs2Pv3Brr9OCzSABZNt4U-hJyGEuVm6raxudSjB2Q6fjWWZpDPYQEbSsuzmZVJC7IHOaPiuyn0KwvLZwBKHhiyDiDG7FClRWN225VAQo_ekf71VglAlmj4or0Wo-hz3fDvDdUjDJUSYM6BXSI5MC9kTdqiHIBX5nYJNr7GPrxYO_7cTX7t5RyS-m3t-YATvBqcC4zEuUpWpeTkNdQEF9enBuNuVlT4a4M64YblatugrgBOoC4YgPYxZpBWqy4GYLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632271636a.mp4?token=XqwHgyjAAK076LCpWjyEMU69D2QdpyPJkoVV8wZY-OvucJfICYk64W46xk66xHbvWFRjqqfPdxXcwFH8o16CXEUgwMx45Iajd7J0IcnYfswviZEztntJ4JN4YBA-pDABumnSK3hNA16XzfC6WzI5BQBhhOJaYvtR29Ar-XzrUhea7VWfQSxDTCGIFeVSEg4j3TWDe1Ay82U2UKMz9_VX8hDLRf0oQ3rHbOG8NuV18VMoCBNFdmheyqCw8cxv5hwOQ_f8uRQD8l54Yilh1XPxIq0Vn-LT6-MVXE71pUD3f4AaODOnxmIbb-5Ny1Bcv__nUENgeOqi1_Q9wpbtPDNtA0f3R90TpoS-cHJXqFLXeUiqm4db18bzPrzN2r-zqRMUgh6Qw4u3dAZYR2iCmbBDgho5_IozmkW73KfJd2L7YdPs2Pv3Brr9OCzSABZNt4U-hJyGEuVm6raxudSjB2Q6fjWWZpDPYQEbSsuzmZVJC7IHOaPiuyn0KwvLZwBKHhiyDiDG7FClRWN225VAQo_ekf71VglAlmj4or0Wo-hz3fDvDdUjDJUSYM6BXSI5MC9kTdqiHIBX5nYJNr7GPrxYO_7cTX7t5RyS-m3t-YATvBqcC4zEuUpWpeTkNdQEF9enBuNuVlT4a4M64YblatugrgBOoC4YgPYxZpBWqy4GYLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر موشک ایرانی که به‌سوی مواضع دشمن پرتاب شد، داستانی منحصربه‌فرد و مقصدی معین داشت
🔹
در این ویدیو، گزارشی از اهداف مورد اصابت در جریان جنگ آمریکا و رژیم صهیونیستی علیه ایران را می‌بینید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/654283" target="_blank">📅 12:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654282">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c67e239a73.mp4?token=fBC-fIVXtVMda7yV2uxxZzwTjeNH3o1cLJYRol-6Y8OJW-QBEZtzIFJhMhmINWPNELZCDBmGlHb11gCOqliCk0qzJQTQAf2Q2gHF3xVlDF2ZveadYuqTr0nlGPhzMqNP0ooz2hLx11jpjl2bizTcSoylIDZ00yotNBZmG0ny8oKibN7MRV5N6G6a_dcWU7LfWY-N-bpzwKiQCXLpqr4wxtxlpE3G6TOiPWzNtV29uZgsdS4cz5tyRJcLxxXiKEVhOyX9x99QRJtxefvdX9d-5gTq9hLi20cUTX7fCTjjQnUFSwBtPiaPvCpVKRTJ2SJHH9hCXzHSTdii7Gw8YtUxdTv1CazxURnvrK63fj44wtmvYqgG27hYd_Oy6opKZz0gnz2S2yTuqBRKvUmMPKutwPvu0ISgqKWsaKsD-NuMd6rpld03vS1Ez07GXlQnFLzoAz-o6AKmiW2JLudY2XRSyf4SGnvqJZ5L8ju9UN1lC-LDldQtukKtXwLvl1JZ550jkjE5ZEayi4zejpSf71Kt9RRn6qG1LRW9SksAQCQbMNkl0Eh_QRPp8-EOoFdQRdHK-zpdvIBxgXPCH_2-Gj3v-N8DIy5bIY3PbacV8KhpuK0pUedMoUqv2X-HDeN4_Ghtut1egZdMbEzS7A0gnLJztqTT8RRjFMjRxnMj4IClOJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c67e239a73.mp4?token=fBC-fIVXtVMda7yV2uxxZzwTjeNH3o1cLJYRol-6Y8OJW-QBEZtzIFJhMhmINWPNELZCDBmGlHb11gCOqliCk0qzJQTQAf2Q2gHF3xVlDF2ZveadYuqTr0nlGPhzMqNP0ooz2hLx11jpjl2bizTcSoylIDZ00yotNBZmG0ny8oKibN7MRV5N6G6a_dcWU7LfWY-N-bpzwKiQCXLpqr4wxtxlpE3G6TOiPWzNtV29uZgsdS4cz5tyRJcLxxXiKEVhOyX9x99QRJtxefvdX9d-5gTq9hLi20cUTX7fCTjjQnUFSwBtPiaPvCpVKRTJ2SJHH9hCXzHSTdii7Gw8YtUxdTv1CazxURnvrK63fj44wtmvYqgG27hYd_Oy6opKZz0gnz2S2yTuqBRKvUmMPKutwPvu0ISgqKWsaKsD-NuMd6rpld03vS1Ez07GXlQnFLzoAz-o6AKmiW2JLudY2XRSyf4SGnvqJZ5L8ju9UN1lC-LDldQtukKtXwLvl1JZ550jkjE5ZEayi4zejpSf71Kt9RRn6qG1LRW9SksAQCQbMNkl0Eh_QRPp8-EOoFdQRdHK-zpdvIBxgXPCH_2-Gj3v-N8DIy5bIY3PbacV8KhpuK0pUedMoUqv2X-HDeN4_Ghtut1egZdMbEzS7A0gnLJztqTT8RRjFMjRxnMj4IClOJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مشهور از سرگذشت بابک خرمدین که با خون خودش صورتش رو سرخ کرد تا دشمن خیال به ضعف او نبره...
ویدیو کامل
👇
https://youtu.be/dHJK6Sf55ew?si=LfriCOFlro6OXI8S
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/654282" target="_blank">📅 12:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654281">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نشریه اینترسپت: پنتاگون در جنگ با ایران آمار تلفات نظامیان آمریکایی را پنهان کرده است
🔹
مدیرکل حمل‌ونقل جاده‌ای ایلام: بیش از ۲۲ هزار زائر عرفه از مرز مهران تردد کردند
🔹
یدیعوت آحارونوت: وتوی آمریکا مانع حمله ارتش اسرائیل به بیروت شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/654281" target="_blank">📅 12:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654279">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDrH8lYReAEttsLgLKoJAGwsluk6jzIFhB0rary_YvIq1u6kjfvQVMIAHPuID_P4sD79dHnWZChB2K0FL9SBFIiwRLKjxF9mJvrNdU6dTyOzmdWvzKb8lrCx1TBhc7OpBi9f7yemLtwU3VG7MoqmDEsRKfS3uUu2pWx_6vdhtFdZbSOHMSxPa77ZYy8N_CDYQc3BtxU3Xry7saIPspJogTFIlT1bzKFj2uRlGRwwrSiUggcQG5GOw7FKLGFGS11vGiwpm0BC406u1A-Ba_KxFYY0_idI9GmrufZYCMKbGqmY_yR55DHNNkePCJzf2ibkswttSgsIokBCyUYo3yJhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افول بازدارندگی آمریکا؛ پایان افسانه هالیوودی پنتاگون
🔹
جنگ ۴۰ روزه اخیر با عریان کردن نقاط ضعف نظامی واشنگتن، طلسم نیم‌قرنی بازدارندگی آمریکا را شکست؛ رویدادی سرنوشت‌ساز که علاوه بر تغییر معادلات غرب آسیا، تصویر شکست‌ناپذیری پنتاگون را در چشم رقبای راهبردی چون چین و روسیه و حتی متحدان اروپایی برای همیشه فرو ریخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/654279" target="_blank">📅 12:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654278">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e940103f02.mp4?token=r_OG8bRXbbAguxcc-LSv3uIPFZNASpdYvMRG7CCr75fM1Mp9MkZqg5YBxWg3qqxPjp23uPMUwvYrVvbP70GujTFL36-1HRAaASE9-XyL4ljqAVnOQLeYdSpMtrwmaI7woHk-1-Ie6QSS4ddTow25b7AJG7eh0LE2ElZns69iCHgY06TPx3nPYQnqP0M9pXUHFsvV0VHCRQcRpWRByGMWP0UktnkKgqszYZUwZk0NfNxRvTz-8dTKy5GnO9FjhP9w7spGFaPqzev-t_QEJvDWIj0S7hpZNiDnjVTzUBUNV-fKYXWtdvGrF6BTMLNDp0dASjEyKdRQ5m0T9lJGXB7jR6BTDtr3tYB8uxHjWZxqHCQpDvzVgqw0lYnatRWCiE4KW5DZPnxykNMzuDujOIcS2xh-Oe969zfaxq0b9zJKmIA-xYKS4LrU2S2iXmXS-hRVAjLgyj6bwHFh0BuuYPM9R5LFD9ICYzMVHF9JpaZR0suvpGdZFXptse_OfBk-HUah21cNRSFBJFlweBQvU-zON52FHLuOFlu7caGgwVrboEXx5VJpuLyKZoUWSfCuzXP4rImIwFPPDKyjrcX_YDRZl1vNu5seuG-Jsm7q0yBg-ZpLrQgEYwIYnu-hZa1ibAwSw7jvKtBpQ7jBi3PVHrDmw8LFCalIOOSwMy4-7Hw6Ztc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e940103f02.mp4?token=r_OG8bRXbbAguxcc-LSv3uIPFZNASpdYvMRG7CCr75fM1Mp9MkZqg5YBxWg3qqxPjp23uPMUwvYrVvbP70GujTFL36-1HRAaASE9-XyL4ljqAVnOQLeYdSpMtrwmaI7woHk-1-Ie6QSS4ddTow25b7AJG7eh0LE2ElZns69iCHgY06TPx3nPYQnqP0M9pXUHFsvV0VHCRQcRpWRByGMWP0UktnkKgqszYZUwZk0NfNxRvTz-8dTKy5GnO9FjhP9w7spGFaPqzev-t_QEJvDWIj0S7hpZNiDnjVTzUBUNV-fKYXWtdvGrF6BTMLNDp0dASjEyKdRQ5m0T9lJGXB7jR6BTDtr3tYB8uxHjWZxqHCQpDvzVgqw0lYnatRWCiE4KW5DZPnxykNMzuDujOIcS2xh-Oe969zfaxq0b9zJKmIA-xYKS4LrU2S2iXmXS-hRVAjLgyj6bwHFh0BuuYPM9R5LFD9ICYzMVHF9JpaZR0suvpGdZFXptse_OfBk-HUah21cNRSFBJFlweBQvU-zON52FHLuOFlu7caGgwVrboEXx5VJpuLyKZoUWSfCuzXP4rImIwFPPDKyjrcX_YDRZl1vNu5seuG-Jsm7q0yBg-ZpLrQgEYwIYnu-hZa1ibAwSw7jvKtBpQ7jBi3PVHrDmw8LFCalIOOSwMy4-7Hw6Ztc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازسازی ترانه اعتراضی باب دیلن در دنیای ماینکرفت
▶️
Reimagining Bob Dylan’s Protest Song in the World of Minecraft
#ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/654278" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654277">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiATUKLaxbLMCnwTYabgnMEpOkQfd44QfjsXLJh7gaziWSxgBFDlFmC1yntGmd2TQh6ep7Z0uICLhxdRIolz1pwxm0BZq5oUI4-_zdoAVVRpcf5IcjV3NpisiVQ0RjQbBMxPZMl9RLdRDG3-lnKIhO6AajDFY21fjEsGwgrYYPYRZdvWIdygg0Pp8mtAbpnKNF6xtnHLbsyRJYyoatF-WOYK9VxRcjP3qaN8kHpcfKe641ui5nP0fuI8bp9s0yNyZHiaPjcI6QUAF9EMwJyv1sEx96uWlz1UpZGlFLfIiGlfiUHAFz9p1lEFaRzv-vK_IlU1xcjiALeP9_GSUcyzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: خط قرمز ایران روشن است؛ این بار کاغذها و امضاها تضمین نیستند. «ضامن عینی بقای توافق، تنگه هرمز است»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/654277" target="_blank">📅 11:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654276">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fxzt_4FOGtVvfSfpZi3Uq_JXgx18UnvxnyraA0kLAm3wrgC0jrFMuYc8kbXXoWF-TV0sYnoCWRedFoFg_bVlaFHIN6Ltbo14WQ_dAs-jJWbEGLLeh4WX3LdT3QiFjhIcQ9y-P-iA0v28WDGjpEmtb0USTWTqbJ5MHVV2EZxayPNvmQUaIqFPVCVLUUlatwXJTtxIAz0R8eRf5vgNYCeTjXLyu04Y4y_Udnt4E9O9wsvWU7i8GkBSPjd6dYyAaD_jvH8nsI366THdcRt0urr4WaED6lBWZ9Xttp4zSFeZ-ur-6sMFosWuc90rr0VNTYq4GFS0mFjTvsQxdINNASDMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صلیب سرخ پیگیر آزادسازی محموله مواد اولیه دارویی بیماران دیالیزی
🔹
رئیس کمیته بین‌المللی صلیب سرخ از پیگیری آزادسازی محموله مواد اولیه دارویی بیماران دیالیزی در کشتی «توسکا» که توسط آمریکا توقیف شده است خبر داد.
🔹
رئیس صلیب سرخ قول داد برای آزادسازی این محموله حیاتی از طریق رایزنی‌های بین‌المللی اقدام کند تا بیماران از حق دسترسی به دارو محروم نشوند.
🔹
همچنین «میریانا اسپولیاریک» رئیس صلیب سرخ با قاطعیت اعلام کرد که شخصاً به موضوع بازگشایی بیمارستان دُبی ورود کرده و از ظرفیت‌های بین‌المللی برای رفع موانع و ازسرگیری خدمات این مرکز درمانی استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/654276" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db80e53c6f.mp4?token=RExwYzmyTnd3bwUJPBI9R-aJFcW1nDPNzjcMgVpzXgpeOZw8Vbhw-DSpctG_9eEge5CSxTzcpr3uNWmE7OjepIs-sOlw6cCI0vHt0aCA7pU8mWpp9lzSfv0XkQ44-ZiwnKEAiMewubEOMXc57FeSIXP9_CAgNvTvmRTXqcuXzVsVvNQLBjdu1o7sjwnK8jjixLuSTPUQloHCP0QAueDxHOrMB_PVsME0xnos9B7o8aHZj_Op6H4R-e0JUEZOTxyHz_2LXIVLpZXIeSmzl8tHB9M6feE1BLfIcnLI2bsxCeWRujZnYe7nH92C6O4UI0r2jVm8fR1eTS5tN7OVMalSeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db80e53c6f.mp4?token=RExwYzmyTnd3bwUJPBI9R-aJFcW1nDPNzjcMgVpzXgpeOZw8Vbhw-DSpctG_9eEge5CSxTzcpr3uNWmE7OjepIs-sOlw6cCI0vHt0aCA7pU8mWpp9lzSfv0XkQ44-ZiwnKEAiMewubEOMXc57FeSIXP9_CAgNvTvmRTXqcuXzVsVvNQLBjdu1o7sjwnK8jjixLuSTPUQloHCP0QAueDxHOrMB_PVsME0xnos9B7o8aHZj_Op6H4R-e0JUEZOTxyHz_2LXIVLpZXIeSmzl8tHB9M6feE1BLfIcnLI2bsxCeWRujZnYe7nH92C6O4UI0r2jVm8fR1eTS5tN7OVMalSeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک عید و دو روایت: طنین تکبیر در قدس و فریاد سکوت در غزه
🔹
همزمان با عید قربان، صبح امروز ده‌ها هزار نمازگزار برغم تمامی محدودیت‌های اسرائیل، نماز عید را در مسجدالاقصی اقامه کردند، در حالی که ساکنان غزه در میان آوار و زیر بمباران، نماز را در سکوتی غم‌زده بر خاکستر خانه‌هایشان به جای آوردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/654272" target="_blank">📅 10:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e7027b1d8.mp4?token=euNpVTfk_TXWGHkl9XSeScjTz2uxpxdm8Mo9bqZjz_daeQHbQO346GmomQeTo6zNdGWJjtm5HyqmPXHdZvS7Z-N1_JwN7JUIbilQlmxLCjbeRV-OKYNxvtV5PsBjfkyuKxEA0NqKkXKiklEZGjkI4VE-YH8wxvapMQiWQoaMzvUzD1NRbLY9zTGasR4STFOyoljvHihwBvUqpoz0oRf06gCunt1VlWFOpYszKzkM8j0xW6ZYsaGqUoOkbU1Cj1mOrgzIc2SS7EXNUVQuH7O4XgKES0uz9cpegJEVvtxuJQSF37jMknoCJt2ljAFA6zIX7DmqrHQyOPDCriZo28OsLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e7027b1d8.mp4?token=euNpVTfk_TXWGHkl9XSeScjTz2uxpxdm8Mo9bqZjz_daeQHbQO346GmomQeTo6zNdGWJjtm5HyqmPXHdZvS7Z-N1_JwN7JUIbilQlmxLCjbeRV-OKYNxvtV5PsBjfkyuKxEA0NqKkXKiklEZGjkI4VE-YH8wxvapMQiWQoaMzvUzD1NRbLY9zTGasR4STFOyoljvHihwBvUqpoz0oRf06gCunt1VlWFOpYszKzkM8j0xW6ZYsaGqUoOkbU1Cj1mOrgzIc2SS7EXNUVQuH7O4XgKES0uz9cpegJEVvtxuJQSF37jMknoCJt2ljAFA6zIX7DmqrHQyOPDCriZo28OsLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله اسرائیل به غزه هنگام جشن‌های عید قربان
🔹
حمله هوایی ارتش رژیم صهیونیستی، یک ساختمان مسکونی در غرب غزه را در بحبوحه جشن‌های عید قربان تخریب کرد.
🔹
حملات اسرائیل در آستانه عید قربان منجر به شهادت دست کم ۹ فلسطینی شده است.
🔹
این حملات یک ساختمان مسکونی حاوی مغازه‌ها، سقف یک ساختمان مسکونی دیگر در شلوغ‌ترین منطقه تجاری شهر غزه، یک وسیله نقلیه غیرنظامی و تجمع غیرنظامیان در مرکز و جنوب غزه را هدف قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/654269" target="_blank">📅 09:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPqIYHQ73perxiAdSyKuLKvjvgQBpFXfU29jxvE6HD5gUVh1ppQAw5TsORzOcGVS3fUJ9fWm22ITQkLi4my4j0NsULq_srqmhO_QgpEMTK_WgARYThwUGzeKhCrEFP-LuM138e-h4Mz9vZnP_82QzRd3xyC8C1RDVvdNwdUsF3piyEZFpXuVy57ZVcRGPC3hMw_ye1yMV5r_HBaxO3dh88DFLBow8WCcr61-QuoQd9dlRKmI1-YEziPXNlfDcdyrep-WOTWPYbKnBZoXHXs2MTirUrId-0Kk0_wGYGYCCG4S7Gen15wNLvJE8x2z0NEjdy3ueqir-2ppkqV0jxLJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاریو: از «پیروزی تاریخی» بوی شکست راهبردی بلند شده است
🔹
در حالی که ارتش رژیم صهیونیستی با تبلیغات گسترده رسانه‌ای، عملیات زمینی در لبنان را «پیروزی قریب‌الوقوع» و «تغییری راهبردی» در معادلات منطقه معرفی می‌کرد، اکنون رسانه‌های خود این رژیم به اشتباه بودن این روند، اعتراف دارند.
🔹
روزنامه عبری معاریو امروز چهارشنبه درباره تداوم حضور نظامیان اسرائیلی در باتلاق لبنان، نوشت که آنچه در ابتدا «پیروزی تاریخی بزرگ» به نظر می‌رسید، به بن‌بستی تبدیل شده است که بوی شکست راهبردی از آن به مشام می‌رسد.
🔹
این روزنامه افزود: اقدام زمینی، تغییری راهبردی در واقعیت موجود نیست و چیزی بیش از گسترش میدان «تیراندازی به اردک‌ها» در لبنان نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/654268" target="_blank">📅 08:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ابلاغ پیام ویژه رهبر معظم انقلاب به مردم سیستان و بلوچستان؛ وحدت شیعه و سنی رمز شکست دشمنان
🔹
نماینده اعزامی رهبر معظم انقلاب به سیستان و بلوچستان، ضمن ابلاغ پیام ایشان به مردم منطقه، بر نقش راهبردی وحدت، ایثار و حضور مستمر در صحنه برای ابطال طرح‌های دشمنان تأکید کرد و گفت: وحدت میان مردم شیعه و سنی و حضور آگاهانه آنان در میدان، ریشه دشمنی‌ها را خشک خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/654267" target="_blank">📅 08:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/091e72bbb6.mp4?token=bkUVW1d6QJdODmFVu739sH0GcVicG35cqUbCALaNox_CSs8LfyiBVQRl6wANiyerzba3c4E4XfRE9m5dHYvGtc9quwV2ZKTlfMBjvpMdErYfN6a-wU0UjXmOUlrHkn_My5N_4cPmaRzwk6Q8M9WrsVMoyKgBZw4d5ztbR1HzlJ8gHc1gr1jXYLoFiZB6g7GaMN4ff07741KwhK7CxaDvSudpv5mr4IEi9V2k27n9hvPqf29xZPg4LOUWuHBmQFh4yX434Y5SohWO8qgYuY2k_EoZQO2IvHPqg4umQFfa5NbQVQLUi3peNPiuIYCkP9xLfQbwQZIDpphZ6ZiFj8yWxbXstiXzXWpinGb4KLbGln19NTc6r0UGaI3rlaMh9otrRkJRUEmx9LJ_eoI2NkGREtxd80zHL2rTxd5zAt6hjMQ3Zj7BgmU0YfGeW-f5yyAS2D27mTlgHGHVkJupDcZAbGVVumcGkhCZbJZy19-mI0tmIMBg_B0fO_tlttwTwr-4cw_hqmEfmHq10la8uZ3tJ7JI9blxhhNQx1kyCf2NcCiophvJiHKSZZ_Zh28teeK62j5nvuUa0FZZim7UHWeGu3iEKld_xwyyxN9EhU_2B6mEM8weMHM4FMZJeToIAJ2VPgpc-IN-vtlyc9-FKsjDyI0-ulthDMS5GMH4LgdRrfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/091e72bbb6.mp4?token=bkUVW1d6QJdODmFVu739sH0GcVicG35cqUbCALaNox_CSs8LfyiBVQRl6wANiyerzba3c4E4XfRE9m5dHYvGtc9quwV2ZKTlfMBjvpMdErYfN6a-wU0UjXmOUlrHkn_My5N_4cPmaRzwk6Q8M9WrsVMoyKgBZw4d5ztbR1HzlJ8gHc1gr1jXYLoFiZB6g7GaMN4ff07741KwhK7CxaDvSudpv5mr4IEi9V2k27n9hvPqf29xZPg4LOUWuHBmQFh4yX434Y5SohWO8qgYuY2k_EoZQO2IvHPqg4umQFfa5NbQVQLUi3peNPiuIYCkP9xLfQbwQZIDpphZ6ZiFj8yWxbXstiXzXWpinGb4KLbGln19NTc6r0UGaI3rlaMh9otrRkJRUEmx9LJ_eoI2NkGREtxd80zHL2rTxd5zAt6hjMQ3Zj7BgmU0YfGeW-f5yyAS2D27mTlgHGHVkJupDcZAbGVVumcGkhCZbJZy19-mI0tmIMBg_B0fO_tlttwTwr-4cw_hqmEfmHq10la8uZ3tJ7JI9blxhhNQx1kyCf2NcCiophvJiHKSZZ_Zh28teeK62j5nvuUa0FZZim7UHWeGu3iEKld_xwyyxN9EhU_2B6mEM8weMHM4FMZJeToIAJ2VPgpc-IN-vtlyc9-FKsjDyI0-ulthDMS5GMH4LgdRrfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف رسمی متخصص ضد جاسوسی آمریکا به دست بالای ایران در جنگ با آمریکا!
🔹
افسر پیشین تفنگداران دریایی آمریکا در گفت‌وگو با بی‌بی‌سی: «آمریکا عملاً وارد یک بن‌بست استراتژیک شده که اتفاقاً به نفع تهران است.»
🔹
«واشنگتن با تصورِ ایرانِ شبیه چین و روسیه، دچار یک اشتباه محاسباتی بزرگ شد؛ در حالی‌که ساختار قدرت در ایران کاملا متفاوت است.»
🔹
«در وضعیت امروز تنگه هرمز، دست برتر با ایران است و ناتوانی آمریکا در بازگشایی آن با وجود تهدیدهای مداوم ترامپ، این واقعیت را تأیید می‌کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/654266" target="_blank">📅 07:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXW64aiW3uPpGuaITZTCUSQLvQs8caPKjb9BP6LZGs3b51qa5ARutfpBaYwIBXhk2UCPXC8dKMPQ4zqe6jSmWiRg9n4TqGJ-BLBMv1_kWnLEiNQoCugUYuwSeGswokSKkz_JS08gqBBYSfyVVMmhK2W9PWI4gHLmsNUTV0-Zatln6K1Mz1q9RWCCtxOTEnfZxWci6uCRtKTZ9B303G4fT3AL3uoSq2deftM62VCUj8sFt8eRKq6X9ftMZx3W2S10KS0IloGDv0VQ8kGVJly5v8Py18sJiv_udsZ-nCXEdIfp-97A-mwe_AVhz03KZ2oVOImsrrC9yKaJPtkDf32Bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۶ خرداد ماه
۱۰ ذی‌الحجه ۱۴۴۷
۲۷ می ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/654265" target="_blank">📅 07:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654264">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmYGPOyR_n2Yv6_yhFClYWqJHUH7scS6lXy2K6NbLV7dpVStz96Mvioj-vcMNdtkgWTfd6r5hld8At4J0eNaz51y4B0iM0yxKOdC7r5nvJ2Yviv87az1TKC3SLcBaqgOe3AcSo6isAOcE1nwpCwd4fIME_hdE-_o6JUe-O4ACvan6xexwnPFex9SJiKZoXD52OgnKQz-uj6T8zdqqvww0YWOpSO-0TLegDPnnX9QxGjsAKlpF_v9X2dXvUzhmNT_cn1Ne307yA5Qv1viCrqzYxQDdlgp5MGTH3xXktXfG9N6KHzyj8KV0dSKrXn4eZBSSOvchcu3sZqkA5t-S4DnQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران تنگۀ هرمز را رها کرده است؟
🔹
با پذیرش قواعد و کسب مجوز از نیروی دریایی ایران، بیش از ۲۰۰ فروند کشتی در یک‌هفتۀ گذشته از تنگۀهرمز عبور کرده‌اند.
🔹
درحالی‌که فرماندهی مرکزی آمریکا (سنتکام) اعلام کرده بود کشتی‌هایی که قواعد ایران را بپذیرند حق عبور از محاصرۀ آمریکا را ندارند اما حالا کشتی‌هایی که از تنگه عبور کرده‌اند، یک‌به‌یک به مقاصد خود می‌رسند و کسب اجازه از ایران برای عبور از این آبراه حیاتی به نودمین روز خود نزدیک می‌شود.
🔹
از نظر واقعیت ژئوپلیتیک و توازن قدرت، بسیاری از تحلیلگران غربی پذیرفته‌اند که ایران در عمل به سطحی از کنترل رسیده که بدون هماهنگی یا تحمل ایران، عبور امن از این آبراه بسیار سخت شده است.
🔹
گزارش ویژۀ رویترز تایید می‌کند که ایران با شبکه‌ای از اقدامات میدانی و حتی هزینه‌های عبوری، به‌صورت عملی کنترل تنگۀهرمز را تثبیت کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/654264" target="_blank">📅 06:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654261">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
مقام غزه: جنگ هنوز ادامه دارد
🔹
«محمود بصل» سخنگوی اداره دفاع مدنی نوار غزه شامگاه سه‌شنبه گفت که آتش‌بسی در این باریکه وجود ندارد و اشغالگران تاکنون ۲ هزار و ۸۰۰ مرتبه آن را نقض کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/654261" target="_blank">📅 02:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654260">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e4223c92.mp4?token=YayvtvMdbQ7nXkNs9OuzmZCXtveX-SuUNd9HzOIeLm283K95LT0qlTqljaLNm94JNyTViHFJKO3vmvTLMLs2-XOXklW6EMeFrulbIrPRWPTtlWKrUBOhMn7eqEV7C_Q4vyZtYUTvgVI9LalYbn5S4lHNgvFs9bpJaaLxJPvSsOmsCV04n8qkRWjTpJS1xx9TCd3eFp8hENzJaRZPIt43NCCjbh4basOuhiqYIab_glkWS1S6n7hqZvNSgj-RjTxD2iHoc2zLyH7ZLl0iMIlli8_UpZJK6f-sexPPJkpD2aHfaK6n0M7LDMcKsdi9qnhfyn9v12zkDANjl4QGjBC4tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e4223c92.mp4?token=YayvtvMdbQ7nXkNs9OuzmZCXtveX-SuUNd9HzOIeLm283K95LT0qlTqljaLNm94JNyTViHFJKO3vmvTLMLs2-XOXklW6EMeFrulbIrPRWPTtlWKrUBOhMn7eqEV7C_Q4vyZtYUTvgVI9LalYbn5S4lHNgvFs9bpJaaLxJPvSsOmsCV04n8qkRWjTpJS1xx9TCd3eFp8hENzJaRZPIt43NCCjbh4basOuhiqYIab_glkWS1S6n7hqZvNSgj-RjTxD2iHoc2zLyH7ZLl0iMIlli8_UpZJK6f-sexPPJkpD2aHfaK6n0M7LDMcKsdi9qnhfyn9v12zkDANjl4QGjBC4tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هوایی شدید رژیم صهیونسیتی به شرق لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/654260" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
وزیر دفاع یمن: نیروهای مسلح ما همچنان دست به ماشه هستند
🔹
وزیر دفاع و رئیس هیئت ستاد کل نیروهای مسلح یمن گفت که یگان‌های نظامی این کشور در بالاترین سطح آمادگی و هوشیاری قرار دارند و دست آنها روی ماشه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/654258" target="_blank">📅 01:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل به نقل از یک منبع امنیتی مدعی شد که ترور محمد عوده (فرمانده جدید شاخه نظامی حماس) با موفقیت انجام شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/654256" target="_blank">📅 00:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fef1a040e.mp4?token=L9HX-L3Tf5onUVnWHumW5YeOohWdfJtsvYgO5ZDKVHAUoTgutr1ovUgcpLlA4KF9fXPGa1I9vd-3kZqZ8uOAXvedcNRYCqYCWHEl-ojh1yl7n_yYZlvuF3HjfljXMR98law6sHSzFhQEAlr2ZsKBKrr_O6gkU_E2PUBoKzHvTluz9fGUJx_RQUz2ZW2QLX9pCtE_rs2qxxIE2TtnAARshR9Vz0Rh12HaHngKOdqywMPaIQE1eeedxmm6poM3q2W4_wC45Gv916Ftws2PO8UfhCriB19bwXP1t4IaFifoQgcmvtYUPvqdl7e-bHFHGeuyG4BLRGobEDLkXIUBIFlkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fef1a040e.mp4?token=L9HX-L3Tf5onUVnWHumW5YeOohWdfJtsvYgO5ZDKVHAUoTgutr1ovUgcpLlA4KF9fXPGa1I9vd-3kZqZ8uOAXvedcNRYCqYCWHEl-ojh1yl7n_yYZlvuF3HjfljXMR98law6sHSzFhQEAlr2ZsKBKrr_O6gkU_E2PUBoKzHvTluz9fGUJx_RQUz2ZW2QLX9pCtE_rs2qxxIE2TtnAARshR9Vz0Rh12HaHngKOdqywMPaIQE1eeedxmm6poM3q2W4_wC45Gv916Ftws2PO8UfhCriB19bwXP1t4IaFifoQgcmvtYUPvqdl7e-bHFHGeuyG4BLRGobEDLkXIUBIFlkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار روسیه به کشورهای حاشیه خلیج فارس درباره پیروی از آمریکا علیه ایران
🔹
«واسیلی نبنزیا» نماینده روسیه در سازمان ملل شامگاه سه‌شنبه خطاب به کشورهای عربی حاشیه خلیج فارس گفت:‌ «شما گروگان سیاست آمریکا در خاورمیانه هستید!»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/654255" target="_blank">📅 00:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
حجت الاسلام قمی: بحران جمعیت و تبعات آن از نبرد نظامی هم سهمگین‌تر است
🔹
حجت الاسلام محمد قمی در صفحه شخصی خود در شبکه اجتماعی ویراستی نوشت: اگر بگوییم بحران جمعیت و تبعات آن، از نبرد نظامی هم سهمگین‌تر است، اغراق نیست. تبعاتی که شاید الان نه، ولی در آینده حتما گریبان ما را می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/654254" target="_blank">📅 00:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be028be8c.mp4?token=OAdu8xjvn1jjNDtzo3-GPw6wVy_1D56W5ctEiIojPF30qyVk2GykRPP2V9rThej0XEqjuooU6sRsEyPWaA7veNnnWpBMUXb0Ca0bFIbGg7CAQRhZY-HlFtMAcpCtPLDJ9zC2aiNazgO-h-KTjaBm8nmhGzdSeNX_I5-O3E4AAcAZO1iVcC5xqgV33tm656bmkbIzWxNuB4pXEkR902ozoc5Qi8xKUi73rvoXbx9sCFo1yIaT_eAR68OCBYqmV5UkZdJwts0jxUACRTMToD5uVZBWksLmMC1Tnx3BbxEj5h85VfL-VnnVCIJ9zuxAkr8rQDPxXCOFaUqDX8lZaiFjOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be028be8c.mp4?token=OAdu8xjvn1jjNDtzo3-GPw6wVy_1D56W5ctEiIojPF30qyVk2GykRPP2V9rThej0XEqjuooU6sRsEyPWaA7veNnnWpBMUXb0Ca0bFIbGg7CAQRhZY-HlFtMAcpCtPLDJ9zC2aiNazgO-h-KTjaBm8nmhGzdSeNX_I5-O3E4AAcAZO1iVcC5xqgV33tm656bmkbIzWxNuB4pXEkR902ozoc5Qi8xKUi73rvoXbx9sCFo1yIaT_eAR68OCBYqmV5UkZdJwts0jxUACRTMToD5uVZBWksLmMC1Tnx3BbxEj5h85VfL-VnnVCIJ9zuxAkr8rQDPxXCOFaUqDX8lZaiFjOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر فرار بزدلانه نظامی اسرائیلی از ترس پهپاد حزب‌الله
🔹
کانال ۱۲ رژیم صهیونیستی تصاویر جدیدی از لحظه فرار یک نظامی صهیونیستی از ترس پهپاد حزب الله را در شهرک شومیرا در شمال فلسطین اشغالی منتشر کرد.
🔹
سکانس پربازدیدِ دیگری از فرار نظامی صهیونیست از پهپاد انتحاری حزب‌الله را از اینجا ببینید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/654253" target="_blank">📅 00:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
بروجردی، عضو کمیسیون امنیت ملی: دیروز پس از آنکه دو شناور هدف قرار گرفته شدند، نیروی دریایی بلافاصله پاسخ داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/654252" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDcuZr5U8GChdu2ssYNcvsCTC48mSfbBU6ezyZsg_uTr9JNqbGTrIcsWZkHEXWHb5DFZpm1yVp5dLYiyj5iGoRh8kpNFPIqcdmlgSbO-NEsb9Uarzk8QgOIC1xdoac_nVOaI1jlygJYCqnKuLcJGldXqP4KmgRsfLQ8Q5SxxRKNNZ4F9_wguAXoKp7W2EPZrXRFYOwg05sUk89Io3DZJmYDWfi_9oWnF4SfXD_LLY8833A90XUXNdcBaHKJsIigGK2A8UV1T-uYeDS36ahNKDjq_uA_fYTI_cJwonBXaiTpxREKj4idthqDvbgtNvRVVw9VsUJUYJ7Fv98-OB_dplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس یادبود شهدای خانوادهٔ قائد شهید و رهبر معظم انقلاب
◾️
شهید زهرا حداد عادل
◾️
شهید سیده بشری حسینی خامنه‌ای
◾️
شهید مصباح‌الهدی باقری
◾️
شهید زهرا محمدی گلپایگانی
🔹
پنجشنبه و جمعه ۷و۸ خرداد؛ از ساعت ۱۶ تا ۱۸
🔹
مصلای حرم حضرت عبدالعظیم حسنی(ع)</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/654251" target="_blank">📅 23:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14f65b188.mp4?token=Wt32Z1Yd-4NLlMwU-rahvS7XmpzoTCLkXSXFa6tZeSfjeAw_XvZOxVJ-46E0bws6_gdY5FuDMgYUgRJHhCanbTxYvsKSnEn8EKJrcOSQdFvx3rBiEMbBYOzM8alKGSmsodEssYMaQN7BE65E2-uhHtcgTUPBGBavjw2c_5gGvQsZTj2eQ5s7xbu3LVpj3JhAqmxvSVopyVVNW92tCZaRrYUdSNkwL1WTnhHQGMZ6Qk6cwXt5bFlNqwIdxRiXFa46x-NBG0n2hafK4XhMSCwpIF7RNG0U7jCrvm_YShfJ8-cCe_JMTIHVshsoxggWL9bYyclIg5dwuVcBC8lqHyaexQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14f65b188.mp4?token=Wt32Z1Yd-4NLlMwU-rahvS7XmpzoTCLkXSXFa6tZeSfjeAw_XvZOxVJ-46E0bws6_gdY5FuDMgYUgRJHhCanbTxYvsKSnEn8EKJrcOSQdFvx3rBiEMbBYOzM8alKGSmsodEssYMaQN7BE65E2-uhHtcgTUPBGBavjw2c_5gGvQsZTj2eQ5s7xbu3LVpj3JhAqmxvSVopyVVNW92tCZaRrYUdSNkwL1WTnhHQGMZ6Qk6cwXt5bFlNqwIdxRiXFa46x-NBG0n2hafK4XhMSCwpIF7RNG0U7jCrvm_YShfJ8-cCe_JMTIHVshsoxggWL9bYyclIg5dwuVcBC8lqHyaexQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیکونهاد، عضو هیئت علمی دانشگاه شهید بهشتی: بدون مصوبه شورای عالی امنیت ملی اینترنت به حالت اول باز نمی گردد، مگر مرجع بالاتر که رهبر باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/654250" target="_blank">📅 23:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKA250qiuNi2JMfPryup6RoOp96Zb6SkoisRzHmvw8Srh6itoryiHJKSEdOqbvNB5G-CK-6Kvz3QmNdvBdcQM00S7REuR6TIRRIE-w9PGo4b0GAMMV1ARrQ4SjRrOA5l_59IIhGxhaxgseKGTmvNVR0Qfv2LtghkGdSYQ52T4uUq9hnz1Vt5SxLrN4scNFAVcRSYHpOLN6dNr9uzY6i-zJzTBZUfVGjEzI4LDb3sRt47TM0z3AqQ2Lgne278Wf2SzplpFrxmXGy8c4xslK-8YdpmEwDavQV486atVNMeI2XzgmpoMIzh0gdedvBzYPMvTop1mlsd85J_FmWwuxR21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: جهان اکنون به‌شدت محتاج توافق میان آمریکا و ایران است
🔹
بدون دستیابی به توافقی پایدار میان واشینگتن و تهران، تبعات ناشی از انسداد تنگه هرمز می‌تواند بحران‌های جهانی در زمینه‌های انرژی، غذا و هزینه‌های زندگی را عمیق‌تر کند.
🔹
اگر به سرعت توافقی پایدار حاصل نشود، پیامدهای آن به سرعت در سراسر اقتصاد جهانی گسترش خواهد یافت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/654249" target="_blank">📅 23:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
چین: توافق پایان جنگ ایران و‌آمریکا برای تأیید به شورای امنیت سازمان ملل ارائه خواهد شد
🔹
وانگ یی، وزیر خارجه چین گفت که پکن معتقد است توافق پایان جنگ آمریکا و اسرائیل علیه ایران باید به شورای امنیت سازمان ملل ارائه شود.
🔹
وانگ گفت پکن امیدوار است طرف‌های مربوطه بتوانند به دنبال کردن آتش‌بس متعهد بمانند.
🔹
او گفت: معتقدیم که پس از دستیابی به توافق، برای تأیید به شورای امنیت سازمان ملل ارائه خواهد شد تا مشروعیت و اقتدار داشته باشد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/654248" target="_blank">📅 23:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcamJVttZrBV8bd2aaGgPZwQ3EdNez0_YjSi2rB8j_kBeTgpPTNiFbsZpC2cQJ0QONDDA8IoqLyW2jEzBgtVJLsoVLT7dzJBFAInYsBrOHZJxE4lMLtFGkHQyeMXPeqlEg1qssANOoIH7vH3TkV520sFVlm-5SjYVqgS4PZ70hkMKOtLXyfHjgU4aOFuCG1MR-xKZmRJEwgU1UxQ0Y-tXawGMn2BHnGltilJZSThzUrZvsIKfW7jVq0Z5mY0ldIfkejFOei-E2JPxYfeTbUPz7u-UTl5MeE_mNlSF22XYrFKTUiwMzm0nHLJ7ChQOd4tlfEvKKdN7svz9mXVuPP8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آشفتگی در آمارهای پنتاگون از تلفات نظامیان در جنگ
🔹
تحقیقات اینترسپت نشان می‌دهد که آمار و ارقام ارائه‌شده از سوی پنتاگون درباره تلفات جنگ علیه ایران بدون ارائه هیچ توضیح مشخصی کم و زیاد شده است.
🔹
اینترسپت می‌گوید مقام‌های آمریکایی تاکنون به درخواست این رسانه درباره آشفتگی‌ها در ارائه آمارها پاسخی نداده‌اند.
🔹
این رسانه نوشته که وزارت جنگ آمریکا در حال پنهان کردن آمار نظامیان کشته و زخمی‌شده در جنگ علیه ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/654247" target="_blank">📅 23:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
علی باقری: نشست مسکو بستری برای مقابله با قلدری و زیاده‌خواهی آمریکا است
🔹
معاون دبیر شورای عالی امنیت ملی: ابتکار روسیه برای جمع کردن کشورهای مستقل خارج از چارچوب یک‌جانبه‌گرایی آمریکا، گامی برای برقراری صلح و ثبات جهانی است.
🔹
عضویت هم‌زمان ایران و روسیه در سازمان شانگهای و گروه بریکس، بستر مناسبی برای تقویت همکاری‌های سیاسی، نظامی و اقتصادی ایجاد کرده است.
🔹
هدف از این رایزنی‌ها، صیانت از امنیت کشورهای مستقل و جلوگیری از تحمیل منویات و زیاده‌خواهی‌های آمریکا بر دیگر ملت‌ها است.
🔹
دیدارهای دوجانبه در حاشیه این اجلاس، نقش کلیدی در نزدیک کردن دیدگاه‌های کشورهای مستقل و حفاظت از حاکمیت ملی آن‌ها دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/654246" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482bfde588.mp4?token=T7hKxU4NCueD9IHT4aGQQTV6TltsROSXOCrK3Uq7RQVzAVGYwgqGCx5vT9tfj_AMCo8l8atrLrOJIvdcIYYY7zLb8xiHlaPX7gJgi0WAG9jM3R7FE3iftjwMT3tKpBx9o1RNAT0AEoP-i3x4XDBBlxhbBY21a6uDftqzy9CU392Flg2xMuLB92Koq6fWXP3eB4Rd7U2W3Tm1P__jd6zKHmeBGxwornIUPV4I7cjmehB4HfPtGLHnlaYyrKxpIAtZ3zkQlTLFqI6o4CbDaSjw3XEMg2P1tFB15pDoQ7yi_S01OXqRNQvkdsnFDZqQAy9twDTabxw_OUZiygxV_XKOQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482bfde588.mp4?token=T7hKxU4NCueD9IHT4aGQQTV6TltsROSXOCrK3Uq7RQVzAVGYwgqGCx5vT9tfj_AMCo8l8atrLrOJIvdcIYYY7zLb8xiHlaPX7gJgi0WAG9jM3R7FE3iftjwMT3tKpBx9o1RNAT0AEoP-i3x4XDBBlxhbBY21a6uDftqzy9CU392Flg2xMuLB92Koq6fWXP3eB4Rd7U2W3Tm1P__jd6zKHmeBGxwornIUPV4I7cjmehB4HfPtGLHnlaYyrKxpIAtZ3zkQlTLFqI6o4CbDaSjw3XEMg2P1tFB15pDoQ7yi_S01OXqRNQvkdsnFDZqQAy9twDTabxw_OUZiygxV_XKOQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : آزادسازی ۱۲ میلیارد دلار از شروط ابتدایی ایران در مذاکره است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/654245" target="_blank">📅 22:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a2ec2172.mp4?token=F90l-MrXhCdcE6ujKNM42dq_JXvi2Vv8ngcSsxGvIUd_wHsCZnB3il32iWpVABw4bMuIv9QmY8pxpht_nX1RwCTn1uiCzrkxR0zvIAd-sSgF5ebs8RdJLovnU6ZxjDs-KEDp3iHDR55IVUTHnO55WClsapZPA-9flbcIaf5zACE2xVJCa1YM1-KRfDsRlv6rRNjYS8QsdLJXJlNsaBFqC1xaeniaJHo7IVe5DosEuLphl_bOQQBszk-Xrfvo36iZct2PVdECPs2JD1pJqvGi4DWT-b5_3QBi_quvyzy9xUhiXMsx2zLspAVa8cpmK67Fp0WZNNGXBHRGUIcv_wvKoHltLlj_l-yU4fHp4MJQSL0OVx1v6kNqjfoAi__bFgcffmOxa3c50-FZwsDz5OAxoB7ZWwKQ1FsD0M0P5GIvLSrYiG7DPFTD2iSM6nRKQIBYrUadcTnrnqZcfv7rvfFgqrVofL894GTqDVpeSuWHROrU2ECgp_as4gQODuYnAytlyWl2Y89RudNuTvOOdRnT5CCbukbJVVkWm8pTx-JpSf2OtgnQqgGQ73KjKmgh6I2p2PH2efJ-L0bGRgSZTBJxbKIkWJRV4tdtmxJY3btwklwA-6Qv3QerC85kqvTshKTVSPWmqYA1iYaxLo595KLcKUOXIlkPVABHy_d5gB2F67E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a2ec2172.mp4?token=F90l-MrXhCdcE6ujKNM42dq_JXvi2Vv8ngcSsxGvIUd_wHsCZnB3il32iWpVABw4bMuIv9QmY8pxpht_nX1RwCTn1uiCzrkxR0zvIAd-sSgF5ebs8RdJLovnU6ZxjDs-KEDp3iHDR55IVUTHnO55WClsapZPA-9flbcIaf5zACE2xVJCa1YM1-KRfDsRlv6rRNjYS8QsdLJXJlNsaBFqC1xaeniaJHo7IVe5DosEuLphl_bOQQBszk-Xrfvo36iZct2PVdECPs2JD1pJqvGi4DWT-b5_3QBi_quvyzy9xUhiXMsx2zLspAVa8cpmK67Fp0WZNNGXBHRGUIcv_wvKoHltLlj_l-yU4fHp4MJQSL0OVx1v6kNqjfoAi__bFgcffmOxa3c50-FZwsDz5OAxoB7ZWwKQ1FsD0M0P5GIvLSrYiG7DPFTD2iSM6nRKQIBYrUadcTnrnqZcfv7rvfFgqrVofL894GTqDVpeSuWHROrU2ECgp_as4gQODuYnAytlyWl2Y89RudNuTvOOdRnT5CCbukbJVVkWm8pTx-JpSf2OtgnQqgGQ73KjKmgh6I2p2PH2efJ-L0bGRgSZTBJxbKIkWJRV4tdtmxJY3btwklwA-6Qv3QerC85kqvTshKTVSPWmqYA1iYaxLo595KLcKUOXIlkPVABHy_d5gB2F67E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمیسیون امنیت ملی: دیروز پس از آنکه دو شناور هدف قرار گرفته شدند، نیروی دریایی بلافاصله پاسخ داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/654244" target="_blank">📅 22:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tb5pToQyHAYpjfcOIw-4YbcOeTJUAQOI4emO5nZqhHoguBK0tw8Q98abYyobAtS-2mN0O_SIkJsrqKP3VZ4A-eBEIdOcMr-6-tafjJqln1rD8liYTvMYgoeKD0fJ3O_NG8SZqI_J973TZCXebVaInkbbU3n33fPa0_mg3qCHBMpHODSvA_NF-Hb5HfDiDPMB6zPE95AhdiLZac25wT02wG3IhamVp9MaSx-nxiUIlcgB1eG9AXb6qIGMHlIe5GxZTFIfXb8izvejwOAo0xqrpNZ2o4JzaVQYDg967k6RrscmqFLaxjOC4ky1TA5bnMbntlDWBE9QH4dmKPHWoG9t0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPgWOG1enwfM42KF-RmOMZ0W-O887X6URl4TfRffCtciB83b5QGvbci4vmu5cdZ0rtXuVRIc9PIgRQKC3iluQFNe4mCucI-xtr92X18sMbNXZxYuk2k4Zxfpv0CCt0nQkZe2_ZfDBae5SmN7nmTdBrKVH8UeMQZmAVdD8fxTOp4izSw8L01Sa8w8iIavv98ZEkvxPbdAkEC30fHRPJIssl-u9djLFmtYj9nf4wI7azojdLgDm3TElWTKeVV7_ptN5oeCcRQxTcRZQdZNL0uogIdPSqz3Er5I5lRo3b5WwU9jW7VHrt2bhaH2MOGRnbT7FzxmyTuHzDmygbUIzyA6qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXXUkkhAUnLqdMwkob1ehKO8ruAY02RfxZoH7exCLhB-QBIJ40jyOl8hGSBAxAB63fg6X5_cIYa1RqS870t_3t0-f51OMCZMxfwJsMWmNARF8e63n22ZbooCGSfyk4XkDZZHu4RXzmQjJwvOVgJeOpFrzF27YeCsyv2ngsmpQ-5CQl0rNLKucBw3FPqFkDLz5ILGU-UtN56JfvwpA7DSelwd5foFDJNdIrhMIdRgeTkjZFCW3r8V9ev7u1fFBteuURQGl7PKGnQ4jb2hcCrU7pIxJ9GtfWDv_AsFfmn9FGclySqe7bl29N69BEn2qsWIVJF-ZptGS0UMB9hvoOoleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0w28EJj0G3WYCU0Lx5LJfFtfCS4oj-7Il8xZ-KCergUtTJ_eu_IoOE_O_VIxkppZGK9TTGsENgNa6BjcK6303_-2hbEhezVDoeiL2G32JnTLMkGmMhDEYfVARcq1kHPP4thIZgv5xIW3966kfDSmuUwrPuq2O0o1mI3DZz3V3OJU4cgcWPgzWOoo5tdreSKrIFUuQsoeA1q56_GhUwisXT5gOMB69lS6XtPhZCxURCe6HCoZc1YI_SqaeTFHKFKQ3X9GIrpcDvaDYj0g78W9iTP_skPMqvtRGhAfrBlAvmI-SD4CE07sBrym0tlWZ8z6A3mRw9YR8bep53n7MHnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PY1JJfT2ZT0VVHgyTffIpxx9nRuHQEKFEs_qVedxLSvZtzDPTjbVqTUT0OpQWLmTALB8NXC4p0AIJEqq2cOvSHNRs7TTgbv460OwkM_Hvda94AHfAgQCD8D2-lr46i4-kb59rmZxaQFKltO3DvT5Qu67Qc3ePUQym1lqd4Y_rK2ssYnn90gzzVt1SKmpCqTNmZBXMhW1vsY1-3gAzYQiZgp10pLwBUQL53AZmlXMG63a0Da2-Z_wTQZDkvW3fEYeAJ7XRpMifAnrnp5U3Bx1U9IC6-3oVks2absMnBmic3udoR_Ae-9QpJoib4ZLOP04GUulwonjB4OplAQDkh95hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnR818ibDXJk4nSGNrJ_9H0UnzyJ9o6Vf_p3QReqj-V3m4WmqLklkhdVdmV9ScmYcT6ViJWxvEptN-UgQ4WEymu9ifYpedm976PCdIsP7v-0dX8pQdoqKAXZqK02ySxgEFnFc0jClKW-tXQf8asoTtsHDJ8hjg-fulXZ0NQrs6pXXv99zetwGIlPtqXxkAOc8GfFmIOH33resFQBQMcJ0dKcL6rdaFyxbXztjGMtPL8dnItLrh4VyVb5UW2P55ywdPHt_-N8JFaG7Dwmk-BLW4t3P4sUXD8dmq29q38xC-3BQxB_g0wvuc9HU06yVl6a33DpImWOl3E4nZ7IZ8DKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-h_1RlaQ6Go8zSb36JmYzkMygh7p6KSgaL4DjFYRnlkunNHEaRGgReok1rqQaVmsPsrOq6hNa0zvx9cP821-hl-S8pky5BXgHmZZteEzpz5iA9NN5hmVRpqLLmt-mCcBJw_SJtDkLC7_C4mdO6_qSPAy7lqmV-41rzdCKcO7_zxisDmJstvNYMYF8hPR42pR3mOac3sCjzWG7pH3iSyoDv2zSD7xtvf5fF0acx7wPZi6hWoxbZ503FcumVRN0fGii4QmXBy3zwJCogxbfbhFHmFZPwIjakg1IGM3X86m-rVL0fREGHpAMsoe_ypWXZkP0veUM8YGzk6BiQzK-69Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoOuYceBBYEfRhYzokkCqihBvjkzqUxN1-dc6_AZqKYzELBdm9lyukyBa_SlNZwv68NBjECpoLSH42cUyMUDJNufveHKLQRRbHw_7H3JytScTicOZxMuu5fYSdb4RuaVjYNPr9IsV6xeX9oGuRuMW2Q9OPrK1v9V9yoMElBZT3JgE1_3hASqxaO3HyhHEe-eWEPOgNMGf6DoIV6OWOqGuNN_wF10YgSmDvka3_OAzJUh5KKs5hs5k6W-zBe-oU3ColCJxdtRs77YSXhOayuT4OAsUDvo1jY9UsrsIZdl_PJdVbzrPh6HTyTeOJTQ7S_ouE_9FmfQXqpyI88I34Xz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YorCwZ2ER6RuFemKw5cz-qV4z4FOQyhcBPjGJPIWsYbVD-09Q4YvZfTN59HWZgKu79awHrlvRR3claQ4M2_Ec5irNEaK32MeHdJuWL3yoY5_PIZotAsfth0xY8qHuV4DSvXth5DUDllvUmN3UVxY6VngBrJBQlBk9kZLKmj-iFGJIaTl7Ok1wSlDKI68oLb56jwK2k3Ne7g-2gR_FAz3UQXbrthmIxpoxTLu2v5CXK8J9qmGQG22zqg2OgogrQHoWIGwV6sPF8S-vVhZ7jgZZnnKhnCAWnqo0dFL-5FHjUF0rxLfS9PzMSySqyomG7QUW-SL3NoFRK8MW5zz2QTXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-I4iXKmGoKzNW6-n5LLPGf-YlfIQ_y2e6O-p0QuEXRnjlkmSH9x6BbkCxX4UsJk1_YO0Rily_6nc8lgdXUq2sjWqzn5xcD1aRB2nNyniwYvOC9bId-hD5AkQ1x8leJCrHtxRdTsy0DGOphqeP5qosTim6_GZyUptwoucjv3LECSfvWAoVLAvP_7Agx8wogbzcccSk4OyHdVTFgB5q-68OQMyslR88de4KE4J8J7C5F5oecg6zxSe9eSQ0_EsKMGNmJrLJOXGA99uqkOFjtRQJsDlWx4mHxuReH2msyRZnxSw-OT__J9ZGMWpVNaSVGJI0IerN9-viiSOf0BVxdytA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
در مسیر
#همدلی
و حمایت از خانواده‌های ایرانی،
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، تلاش می‌کند سهمی هرچند کوچک در این مسیر خیر داشته باشد.
این خدمت، با حضور و اعتماد شما مردم ادامه پیدا کرده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/654234" target="_blank">📅 22:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654233">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62aae35680.mp4?token=MUqWxJTirFW3egS05RAVye4ITAVnhdFaHm-MTIv6NgvRwCU9Glmvooo1SduvfnYtFbsZBGYRrATg15T8f77SNTf4NhVJq2EcZZ56C19GIcFZ2sjqN3a45Fla3jQXScNCD2Tkdsk26IBK61eJ_kQZ6-BPjpQ4dJpS5p5aS8Ii6Od8agwS2dEWbU1nhFoRtTXS-Q0-y8ug130eA0ERnjCEVfDdZtlQkib0roAxZZKuJv0Ou2Og29sVLenIKNmSnG9OC3IzvnbpSs64vdKURzK2phvBhjJmaWqX7wZnAytxJRvcpSxPUaxMywyDJwACPFtnEKywdLQBpPneRLlqoIEZyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62aae35680.mp4?token=MUqWxJTirFW3egS05RAVye4ITAVnhdFaHm-MTIv6NgvRwCU9Glmvooo1SduvfnYtFbsZBGYRrATg15T8f77SNTf4NhVJq2EcZZ56C19GIcFZ2sjqN3a45Fla3jQXScNCD2Tkdsk26IBK61eJ_kQZ6-BPjpQ4dJpS5p5aS8Ii6Od8agwS2dEWbU1nhFoRtTXS-Q0-y8ug130eA0ERnjCEVfDdZtlQkib0roAxZZKuJv0Ou2Og29sVLenIKNmSnG9OC3IzvnbpSs64vdKURzK2phvBhjJmaWqX7wZnAytxJRvcpSxPUaxMywyDJwACPFtnEKywdLQBpPneRLlqoIEZyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه انهدام دوباره یک جنگنده F۳۵ توسط سپاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/654233" target="_blank">📅 22:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654232">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe615e247e.mp4?token=FO8qpZE7xh5DXi07FZW_ySqZyRjseA6GCg_0n_VIecO-fjk0e8v6wYJHCAaex9Uc5_6yGq3Sd1i9VkuJhntUvpXSfMupK9tSlXdCsr9yS3Bv5XQpVuOQjVGct43ERZ2yUBFHE2nJwQe4FxhgDv9SBSrhhg49JEEaD0Aswk8lXsyO8u9ikefphZN7-iClf-9zTRUirL8xxtbM9WRaynS_PsARcuENtPrmYpHePqT4uqBat0QTzg-wA2TUexZ0lGGv6vwCRYwgqG7I9hAesTxsmcBzXGkzwNihvFhoFErhzj9LPyLjBqWTfru5MpsSiIFuq4q5FAXvDE4fg8xn9x6jog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe615e247e.mp4?token=FO8qpZE7xh5DXi07FZW_ySqZyRjseA6GCg_0n_VIecO-fjk0e8v6wYJHCAaex9Uc5_6yGq3Sd1i9VkuJhntUvpXSfMupK9tSlXdCsr9yS3Bv5XQpVuOQjVGct43ERZ2yUBFHE2nJwQe4FxhgDv9SBSrhhg49JEEaD0Aswk8lXsyO8u9ikefphZN7-iClf-9zTRUirL8xxtbM9WRaynS_PsARcuENtPrmYpHePqT4uqBat0QTzg-wA2TUexZ0lGGv6vwCRYwgqG7I9hAesTxsmcBzXGkzwNihvFhoFErhzj9LPyLjBqWTfru5MpsSiIFuq4q5FAXvDE4fg8xn9x6jog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش موشک امریکایی با چند هزار ترکش روی مردم ایران
🔹
روایت یک مستند ساز از جنایت آمریکا در لامرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/654232" target="_blank">📅 22:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654231">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec933080a.mp4?token=qS2yvADx2t_LRztPJMPZUuMg77X-J1lVRl_H8sgG7oFwuObnzDYZekcN8tuaDgv7LfaRbR70Mh4TzEaZxS2cKhRyQZAYxip9Ha0p2nq5xbMF4YJ076jUd0Q4cnJIphY4zhNnC_6utv8pQDQ7Uq1oczBUmwyuHp_DzpyHlVNNkgS42VROe_mbDWA-k8URPJtVqezt17Pq3RaYhRVUXiZH-fVuoMUpu352GtW-MqkxTv3atGg-vN3DXQJNgCpURUlXQVSjKpOqKP04XIhFoHud7vov-qZG6H0cTULR9-_-PbQhWOGWPeFZWhIDCRRBYcSP30LBZso38QGDIfYm3f3Up1qfEiqRXKGAE4aaRxA_GVw6ZT08c_bimzPJHS-Xnq7SpPQCSb_sZRv8QtdyXEJnRa667HhysogmAstqeHfvePlDHVQflzFo8C0O0EtEsRqDtYuQNA_7QsvSGYX-xY8UsIbOqNH6WLrC0dYOy87FHcidPuUR9Ey-jrEuPFrI2J0gxjaLIbh47fnJ3JNRC5J5kOkY-mrOz5zD7jPe_RFz_brVVxlKMVYEJ9UQ6_2alWlaIuPcto33QPwlyrytkl0JMjcs5FoAUY-RqsZ7blTuEiKvstGB09veeI0r3P4w1OELFtWhfbUTFgbFYyzReOAkGCXU6OeiqcQluCVsWPmZ_MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec933080a.mp4?token=qS2yvADx2t_LRztPJMPZUuMg77X-J1lVRl_H8sgG7oFwuObnzDYZekcN8tuaDgv7LfaRbR70Mh4TzEaZxS2cKhRyQZAYxip9Ha0p2nq5xbMF4YJ076jUd0Q4cnJIphY4zhNnC_6utv8pQDQ7Uq1oczBUmwyuHp_DzpyHlVNNkgS42VROe_mbDWA-k8URPJtVqezt17Pq3RaYhRVUXiZH-fVuoMUpu352GtW-MqkxTv3atGg-vN3DXQJNgCpURUlXQVSjKpOqKP04XIhFoHud7vov-qZG6H0cTULR9-_-PbQhWOGWPeFZWhIDCRRBYcSP30LBZso38QGDIfYm3f3Up1qfEiqRXKGAE4aaRxA_GVw6ZT08c_bimzPJHS-Xnq7SpPQCSb_sZRv8QtdyXEJnRa667HhysogmAstqeHfvePlDHVQflzFo8C0O0EtEsRqDtYuQNA_7QsvSGYX-xY8UsIbOqNH6WLrC0dYOy87FHcidPuUR9Ey-jrEuPFrI2J0gxjaLIbh47fnJ3JNRC5J5kOkY-mrOz5zD7jPe_RFz_brVVxlKMVYEJ9UQ6_2alWlaIuPcto33QPwlyrytkl0JMjcs5FoAUY-RqsZ7blTuEiKvstGB09veeI0r3P4w1OELFtWhfbUTFgbFYyzReOAkGCXU6OeiqcQluCVsWPmZ_MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاحی که هیمنه دو ارتش متجاوز را در هم کوبید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/654231" target="_blank">📅 22:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654230">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm-ItYRQ-Mci_yJTdr0XryMOBbjipmek6U6XeIdb84xDa3ttyO9Gv5IjOEcHxK-5qtLc-f6V9MN6pzh-PREURf_bvZU38fasxKPO6czcgsH32zMDMnIBvsdvtAZb2FFenwr5Jy2SmVC8nE6hTU1blu1GnPwombRARrdBFX3Wfr6ysK7oVpUWXDO9SUD9hYHuL1HVapxebREB-t_3Bwx2mO17pMQVRJxWFOsL4gj-K9HYJIf1wayDJ3CKVyf0Pj_1E0UQfCLlmYr7En8R1a1RhSia_srpD8R7-uF8i9FRFMGyYhQw2F9V8B7_ROAl0o3mHtOLnSWFGEUFQZVxmrhgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم یادبود شهدای خانواده امام شهید و رهبر معظم انقلاب اسلامی
▪️
شهيد زهرا حدادعادل
▪️
شهيد سیده‌بشری حسینی خامنه‌ای
▪️
شهید مصباح‌الهدی باقری
▪️
شهيد زهرا محمدی گلپایگانی
🗓
پنجشنبه و جمعه، هفتم و هشتم خردادماه
🕓
ساعت ۱۶ الی ۱۸
📍
مصلی حرم مطهر حضرت عبدالعظیم حسنی علیه‌السلام
از طرف خانواده‌ رهبر معظم انقلاب اسلامی
@Akhbarefori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/654230" target="_blank">📅 22:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUOU7VPuorz2Odvvf_vLcoTSWDhlpkblv-GPsAijxDeZfAHqskMzU_qvNJjzldtCXk62Xvg1mlcunXPBpFD4TwEDM08vdDK2r0ginHkr-Ci7Y-f_XyRZs3A8oXVuLG8kPLD2r4-DAJJZBLJrhga7NmAutxEDKsFBfJdMEHUOiN88tn26XSIY2AX_qeH_LRZWMCLPei1ZjlLNNgZ3iLMA1kfgWOqseskZe0DPaaqyaGCbUVbPlz9Kpx-S47TTUU9yWL7e1QCsBHQLWkJ_5qARlkBgoQDBGrEndTEKRHk2ob92Zw9_RWdcOlCwVdhEiG6V7QUi5i47OxeC_IWeJxEMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا مخالفان رایگان‌شدن مترو، تهران را معطل «سلیقه شخصی» خود کرده‌اند؟
🔹
افشاگری صادقی از پشت‌پرده مخالفت‌ها با رایگان شدن مترو/ برخی اعضای شورا حتی چشم دیدن رایگان بودن دو هفته‌ای مترو را هم ندارند!
احمد صادقی با افشاگری از ناکامی طرح دوفوریتی «سروری» برای تداوم رایگان‌بودن مترو، از سلیقه‌گرایی در شورا گفت و بیان کرد:
🔹
در حالی که این طرح می‌توانست به کاهش ناترازی سوخت و آلودگی هوا کمک کند، برخی اعضا حتی حاضر نشدند با امضای خود، مسیر استمرار دو هفته ای رایگان‌بودن مترو را هموار کنند و شهر را معطل ملاحظات شخصی خود کردند.
🔹
احمد صادقی، رئیس کمیته شفافیت و عضو شورای اسلامی شهر تهران، با اشاره به پیشنهاد «دو فوریت» برای تداوم رایگان‌بودن مترو تا زمان بررسی و تصویب طرح نهایی بلیت رایگان که از سوی پرویز سروری، نایب رییس شورای شهر تهران مطرح شد، گفت: برای مطرح شدن یک طرح با قید دو فوریت در صحن شورا، امضای دو سوم اعضا لازم است. در این مورد ۱۰ نفر از اعضا طرح را امضا کرده بودند اما برای رسیدن به حد نصاب، دست‌کم به امضای ۴ عضو دیگر نیاز بود که این اتفاق نیفتاد و طرح به مرحله طرح در صحن نرسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/654229" target="_blank">📅 22:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a26889fb7.mp4?token=Gsssbxem07l7x09Q1_ni8sej3270A14A3uVhayObyDQHpSerMPVxKCEjhD18ZbspncNYrP_Ymoy4OVtvWny_WMBYxeidg5DgDeL867QM9FYrtEEPcrpDhqLKF3EvrPw06fdjsTctagyw3O-CEcoHTbBqb-aJG2yUlecR8nparKPVhbzyCPAcFMYfO3US_rlQaDzYjhZoY6tFPr-JxkIzIk3ppUv4IgH335ScshfMoo1aCHOGuJBqTDxADRo-Iv9oYWEYSYbJPFFuMDt9_hRJ9pxPUUIX_9_93saJB3v3NBH_RrizPAviqYycUH9p6YXt_UXocsS4MdW-wbRJS5n9CTug3PyZWBrS3y-QKl_TpQalIe2g2yUMgePkaqSRp36MBjo4A4WCoOqZOl8FthAZMzlW8jQcj4ukNtg-ezsIi-Ul5vwZajR5hlI0YPvMFaQEEFTIydvc6rvq6Q2RRUyLlEtwRLGV0BLzPApfCjtgSKW4HdTpHCIBshw_y_gaGG-drHvYhCTbqTxARMvTmvJmLI4bFAqoZbgs5iHdgIgIgCEn9qcU-ouQWbMxGx43LwTC_WqSpH7XcIJ2LJuN2KHatFDCNHy3foA9T2mTPLedj1WgF-K33O6sUhgdOr5-jVpwlO1TFug35O7DUpVJRaw3VUu9KwwltQZm2cK6GIdJQp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a26889fb7.mp4?token=Gsssbxem07l7x09Q1_ni8sej3270A14A3uVhayObyDQHpSerMPVxKCEjhD18ZbspncNYrP_Ymoy4OVtvWny_WMBYxeidg5DgDeL867QM9FYrtEEPcrpDhqLKF3EvrPw06fdjsTctagyw3O-CEcoHTbBqb-aJG2yUlecR8nparKPVhbzyCPAcFMYfO3US_rlQaDzYjhZoY6tFPr-JxkIzIk3ppUv4IgH335ScshfMoo1aCHOGuJBqTDxADRo-Iv9oYWEYSYbJPFFuMDt9_hRJ9pxPUUIX_9_93saJB3v3NBH_RrizPAviqYycUH9p6YXt_UXocsS4MdW-wbRJS5n9CTug3PyZWBrS3y-QKl_TpQalIe2g2yUMgePkaqSRp36MBjo4A4WCoOqZOl8FthAZMzlW8jQcj4ukNtg-ezsIi-Ul5vwZajR5hlI0YPvMFaQEEFTIydvc6rvq6Q2RRUyLlEtwRLGV0BLzPApfCjtgSKW4HdTpHCIBshw_y_gaGG-drHvYhCTbqTxARMvTmvJmLI4bFAqoZbgs5iHdgIgIgCEn9qcU-ouQWbMxGx43LwTC_WqSpH7XcIJ2LJuN2KHatFDCNHy3foA9T2mTPLedj1WgF-K33O6sUhgdOr5-jVpwlO1TFug35O7DUpVJRaw3VUu9KwwltQZm2cK6GIdJQp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوار بهداشتی شدیدا گران شده؛ چرا کسی حرفی نمی‌زند؟!
🔹
۱۵ تا ۴۹ سالگی. جمعیتی سه برابر نوزادان کشور؛ اما وقتی حرف از گرانی می‌شود، اسمی از نوار بهداشتی نیست. هر ماه حداقل ۲۶۰ هزار تومان فقط برای یک نیاز طبیعی، نه برای تفریح، نه برای تجمل، برای نوار بهداشتی.
🔹
چیزی که هیچ‌کس درباره‌اش حرف نمی‌زند، دارد جیب میلیون‌ها زن را خالی می‌کند. تورم پنهانِ قاعدگی را در ویدیو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/654228" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedf16d37d.mp4?token=l7-EH-R0ZgytlexKw8fxtLNJjorBha2dz5iJYNoYta1zzDF6u8k1EYvzXz9ZjTkVwCEE9BRLlEF6NHuQ_Mmdq_yRLFJcTnwwThRqoaLoZTKDd26I8GC-WVm6h5gcC39V9I91nwb58cY2coW9bnvcE5Elpn4V5vhI3wwkH4tl-Uuja32QNQQP8MxZdUmfmK2nKho9CzWzYPm5Y0wH8ebrl9vtjE2Hn6nbON8CWZr65LNVzu2Nq6Abl9bfF8Ja3ZNsLTWhqT95xjomKH8b5bv89mm77cSU88h3QYucCIn5MFpYfKUDqPVPQXYzViWQQpOJe-b0c8I06gJOs4JLoj0vxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedf16d37d.mp4?token=l7-EH-R0ZgytlexKw8fxtLNJjorBha2dz5iJYNoYta1zzDF6u8k1EYvzXz9ZjTkVwCEE9BRLlEF6NHuQ_Mmdq_yRLFJcTnwwThRqoaLoZTKDd26I8GC-WVm6h5gcC39V9I91nwb58cY2coW9bnvcE5Elpn4V5vhI3wwkH4tl-Uuja32QNQQP8MxZdUmfmK2nKho9CzWzYPm5Y0wH8ebrl9vtjE2Hn6nbON8CWZr65LNVzu2Nq6Abl9bfF8Ja3ZNsLTWhqT95xjomKH8b5bv89mm77cSU88h3QYucCIn5MFpYfKUDqPVPQXYzViWQQpOJe-b0c8I06gJOs4JLoj0vxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام پرنده بدون سرنشین MQ۹
🔹
انهدام پرنده بدون سرنشین MQ۹ دشمن متجاوز آمریکایی هنگام نقض حریم هوایی کشور در منطقه خلیج فارس در بامداد امروز مورخ ۴ خرداد ماه ۱۴۰۵ توسط سامانه نوین پدافندی هوایی نیروی هوافضای سپاه پاسداران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/654227" target="_blank">📅 22:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654226">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای رژیم صهیونیستی در ترور فرمانده جدید قسام
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی در بیانیه مشترکی مدعی شدند که ارتش این رژیم «محمد عوده»، فرمانده جدید گردان‌های قسام، شاخه نظامی حماس را در غزه هدف گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/654226" target="_blank">📅 22:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654225">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmRSuEmKQU2bTaIfwBlU1rXNa1EHypBFNtU0S-LZ4QFHGKTlob4xAtz0fRo_Nrw2g8fIdfUoYpswuvgwLH5ZcP6t6dkV75jbNqBONkxLO1_PjMj43fJgOB3Zf1Qk23-hRm_aZHOWfr8VI49RdNUzxOru7kjV7xf9KcKfFMfs3y71_e8HNvHBlFVYhlil8F8jBLOVNtDrzRXJPqjequD7p6TaGUGO-_K1RcOHzAtk4GFFfF_sG5REQnXC4m7WJV8rpJVTo3K3cNzKvMvLCdJszmuLD_hq4AIa2uMrt3NNJoJjFRgIy_C_ushdCHB51-PgPypcqIThxPMh-pplokjx_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هآرتص: اسرائیل از زمان آغاز «آتش‌بس» در غزه ۸۹۰ فلسطینی را کشته است
🔹
از زمان آغاز آتش‌بس در اکتبر، ۸۹۰ نفر از ساکنان غزه بر اثر شلیک نیروهای اسرائیلی کشته شده‌اند. ۴۲ نفر از این قربانیان، نیروهای پلیس محلی بودند که وظیفه‌ حفظ نظم و امنیت را بر عهده دارند.
🔹
شرایط طاقت‌فرسای کمپ‌های آوارگان، تراکم جمعیت شدید، فقر، گرسنگی و بمباران‌های مداوم هوایی، دریایی و زمینی اسرائیل، زمینه‌ساز بروز تنش‌ها و نزاع‌های خونین در غزه شده است.
🔹
با وجود این وضعیت بحرانی، حماس با نیروهای پلیس خود برای برقراری نظم و رسیدگی به جرایم تلاش می‌کند. با این حال، هر یک از این مأموران که در بازارهای محلی یا مراکز توزیع غذا گشت‌زنی می‌کنند، جان خود را به خطر می‌اندازند؛ چرا که ارتش اسرائیل مأموران پلیس را که نقشی حیاتی در کاهش رنج مردم دارند، به عنوان هدف نظامی تلقی می‌کند.
🔹
علاوه بر مأموران پلیس، غیرنظامیان از جمله چوپانان، رانندگان کامیون و کودکان نیز در حملات روزهای اخیر جان خود را از دست داده‌اند. از جمله در بمباران اردوگاه النصیرات، یک مرد ۳۸ ساله به همراه همسر و نوزاد یک‌ساله‌شان کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/654225" target="_blank">📅 22:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654224">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260f53d553.mp4?token=STh0BqYp1Nvef03w8lyjC7GO_UnMS0q1ooVg24uqFi4p82-eWopleLVcCzWpW9MT9rQER2kClbDr_Is0uTaXCxLn6FiymSRhO-gZ8e_OgsHWIfC_Mfn4X2jxiOmZB4Y0Vs9-w7PU4SoQ8KtE0yhLsmbr6DLOPYQFJmAND4Pn6p9jSS3rTJy3zOLyYpD_oQMpBkruuFhsvuHZ03fJpdj2dHryezlGm3HZoqh7PGtmbK7ny2Z_3oOLUEYJ_vTy-rr4qPwn54ncnna3VpAw-Y6jN-GWpFcFVWYc0Zs35oU7WwfQcl5b1p8LS1LgSROKdGXIZvPyWNikspmgddlxZiCpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260f53d553.mp4?token=STh0BqYp1Nvef03w8lyjC7GO_UnMS0q1ooVg24uqFi4p82-eWopleLVcCzWpW9MT9rQER2kClbDr_Is0uTaXCxLn6FiymSRhO-gZ8e_OgsHWIfC_Mfn4X2jxiOmZB4Y0Vs9-w7PU4SoQ8KtE0yhLsmbr6DLOPYQFJmAND4Pn6p9jSS3rTJy3zOLyYpD_oQMpBkruuFhsvuHZ03fJpdj2dHryezlGm3HZoqh7PGtmbK7ny2Z_3oOLUEYJ_vTy-rr4qPwn54ncnna3VpAw-Y6jN-GWpFcFVWYc0Zs35oU7WwfQcl5b1p8LS1LgSROKdGXIZvPyWNikspmgddlxZiCpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعدام خانی‌شکراب جاسوس چندجانبه و عامل ترور ناکام خاخام یهودی
🔹
غلامرضا خانی‌شکراب به جرم همکاری اطلاعاتی و جاسوسی به نفع رژیم صهیونیستی، پس از تأیید حکم در دیوان عالی کشور و طی روال قانونی، به دار مجازات آویخته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/654224" target="_blank">📅 22:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654223">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79410cb18.mp4?token=uKXRcc4bOliHpoaD1pQsg9f4pWu3D-zOZLpIyRSVF8khPv-2MDIG0EG3gPSGVQ_-xEOrmThWsdr8N7Qkc7dCLlBvEkJ4xkJUVPkhI_oGVoKnAl71G-PMZ6SXTnRHZgfKvGKVH81jS5__4tfea9p7ZfQsctgCFd8USwp6L0svccyVPsxVgYDPiWe5lzf1ih3-ooZO4fcrH7YaPc4SSt6ZpVyrDNcQzoX6dnVmu828OSoDFFUTnrXZ8P9yE7axOMCiMldXUDbJsjZS6bfisI9RmhiW_a8wxV1T_CXWhOCynnBG5DXEwvFlhkvjBoPBNJJjvAfAAMxwsmOhqlaiioCwuHqkvLEhsNQ0CSmK2LD9YePK58-JQfuEqQ7DvgsBuDbKOjVNrTrWVWl-V2YlRQv8p7qOiRQ4oWWUQoWC9ilF-iZg6KHV0rNqV1mNXQcHENkgQxsKsFD8TlN8L-jpwkKQECapfg8N5jKhldn2z24mrJ2Yrj3XFBgM8PzHRVmUa8AzfN02-mtSSbl_CCGQ4iqddEA7229RG1_WSlR8a2JH5ZHGvOEgyhatUYh19RgSXQiPL5lF3u8QfU5pSwhdawCgON7C2RXkdoFW33Cdro7AW5d6JCC3i2ENreobdH-36QRnIqBCvWgelCdbRIaCWV4vQ7KjIACyYfHiSk-J-21M3oI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79410cb18.mp4?token=uKXRcc4bOliHpoaD1pQsg9f4pWu3D-zOZLpIyRSVF8khPv-2MDIG0EG3gPSGVQ_-xEOrmThWsdr8N7Qkc7dCLlBvEkJ4xkJUVPkhI_oGVoKnAl71G-PMZ6SXTnRHZgfKvGKVH81jS5__4tfea9p7ZfQsctgCFd8USwp6L0svccyVPsxVgYDPiWe5lzf1ih3-ooZO4fcrH7YaPc4SSt6ZpVyrDNcQzoX6dnVmu828OSoDFFUTnrXZ8P9yE7axOMCiMldXUDbJsjZS6bfisI9RmhiW_a8wxV1T_CXWhOCynnBG5DXEwvFlhkvjBoPBNJJjvAfAAMxwsmOhqlaiioCwuHqkvLEhsNQ0CSmK2LD9YePK58-JQfuEqQ7DvgsBuDbKOjVNrTrWVWl-V2YlRQv8p7qOiRQ4oWWUQoWC9ilF-iZg6KHV0rNqV1mNXQcHENkgQxsKsFD8TlN8L-jpwkKQECapfg8N5jKhldn2z24mrJ2Yrj3XFBgM8PzHRVmUa8AzfN02-mtSSbl_CCGQ4iqddEA7229RG1_WSlR8a2JH5ZHGvOEgyhatUYh19RgSXQiPL5lF3u8QfU5pSwhdawCgON7C2RXkdoFW33Cdro7AW5d6JCC3i2ENreobdH-36QRnIqBCvWgelCdbRIaCWV4vQ7KjIACyYfHiSk-J-21M3oI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زمان به عقب بازنمی گردد و آمریکا دیگر نقطه امنی در منطقه نخواهد داست
🔹
اخبار تحلیلی ۵ خرداد، ۸۸ روز از آغاز جنگ تحمیلی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/654223" target="_blank">📅 21:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654221">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
عبور ۲۵ فروند کشتی از تنگه هرمز با هماهنگی نیروی دریایی سپاه
🔹
طی شبانه روز گذشته ۲۵ فروند کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🔹
کنترل هوشمند تنگه هرمز با اقتدار در حال انجام است و هرگونه تجاوز با ضربات کوبنده پاسخ داده خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/654221" target="_blank">📅 21:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654220">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e1e88e8.mp4?token=vb2lsVJoBM5BqgFc-tvb2fsFlFbld0JXqTZsQ-M7tbTBTq2xiiYXQ6JEcvK9IYuu4SpICp_ZF7r09N4EzTt9r3AGciIoqwFEpAJXn5AQr5f9i4FVJjOoOifZXmFgkjQKiatBzdVUyVa-Y2yPsZJjhFJpgDSZcWZ1tZRbC_L6Ll7aNgoZBBgvQzmz49wmmnbiEq6X7Qc0W47rxGv04ODl4U40QpQWWkW_iL5Iwfs3ZQf9N8qE2dufw59LMhtr_9z9Rb3XEwKRP40Bo4VX1tj0qwede7bDmSp5Ev8St4jh6MvtmWTN7Sp3F6iEUnyVwZ04JivWbbla3Nh-VnRxNgFDPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e1e88e8.mp4?token=vb2lsVJoBM5BqgFc-tvb2fsFlFbld0JXqTZsQ-M7tbTBTq2xiiYXQ6JEcvK9IYuu4SpICp_ZF7r09N4EzTt9r3AGciIoqwFEpAJXn5AQr5f9i4FVJjOoOifZXmFgkjQKiatBzdVUyVa-Y2yPsZJjhFJpgDSZcWZ1tZRbC_L6Ll7aNgoZBBgvQzmz49wmmnbiEq6X7Qc0W47rxGv04ODl4U40QpQWWkW_iL5Iwfs3ZQf9N8qE2dufw59LMhtr_9z9Rb3XEwKRP40Bo4VX1tj0qwede7bDmSp5Ev8St4jh6MvtmWTN7Sp3F6iEUnyVwZ04JivWbbla3Nh-VnRxNgFDPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزشمار اخراج نظامیان آمریکا از غرب آسیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/654220" target="_blank">📅 21:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654219">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
کیفرخواست ۲ مدیر شهری در خوزستان به اتهام فساد مالی صادر شد
🔹
دادستان مرکز استان خوزستان: اتهامات این دو مدیر شهری شامل ارتشاء، تحصیل مال از طریق نامشروع، پولشویی، رشوه و اختلاس بوده که این جرائم انتسابی به آنان به اثبات رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/654219" target="_blank">📅 21:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654218">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
شورای عالی مسکن، سقف تسهیلات مسکن ملی را از ۶۵۰ میلیون به ۸۵۰ میلیون تومان افزایش داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/654218" target="_blank">📅 21:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654217">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دام زنده ۱۰ درصد گران شد
مقدسی، رئیس هیئت مدیره انجمن گاوداران ایران در ‎
#گفتگو
با خبرفوری:
🔹
با تدابیر صورت گرفته، در دوران جنگ و پساجنگ در تامین نهاده‌ها، شیر و گوشت مشکل خاصی نداشتیم. مشکلاتی بوده اما نه آن‌قدر که به تولید ضربه بزند. درحال حاضر نهاده‌های دامی در ثبات است.
🔹
جنگ همزمان با تغییر قیمت‌ها در سال نو بود و افزایش قیمت داشتیم. شیرخام حدود ۲۹ درصد و در دام زنده ۱۰ درصد افزایش قیمت داشته است. جدا از مبحث جنگ، بخشی از این افزایش قیمت‌ها به دلیل تحریم‌ها است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/654217" target="_blank">📅 21:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654210">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2mSr7k_nnybTmvcedI-SDDwId4W-QYHt3SGV4sXeHWbt9KtVwY80wLTZhQa0enA_oEsGcSHTGdGDXSpRoDqca2hzCjkXYDuqhf2-wdr-1ujZom53fP440I4nZFPHJHWVZLjbQok0hIFrTOBIZubj0lPJ5YYCIgimdNBxR1Qj4fA5G9yO_Cd7KqmacuYuLxw_XcbQTU-i48OLHZOVmKMKaCIFOhJVkKLRE7AK-JpQAtU_2f27CftRs2eUkCu-iSsEBED8NIQOBnWEQQk0JqOkNpBE2lc4SEmD9sJjcDDxOvFg3jsGUTQ7rhCC42SmAEnaep-8itDGPZ1Fj40GQcWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ma0w8qSsQ3kbHOIkgJjkOANqjVAUPiIgNMtmMuTBRziNAnh7W9fk8rsH15cOyueZp_b3H8Z3OBRnZsbk95lL775INX-hJzPZq5lacPDeNWR0xJ_vlb5h7gW9tWGo3qsletYPyCkDbXdOhfRVzS_lML4FnzflzVnhTTm7dl3zs3zoVd6zMsIpHsbIpAGMRiMoD-bbeZJ8xdvClM6OJ2rt0EUe4rJmfLIU0mg4eIx4cf_GTfsm3GqU-B1pjzSTlzmHV5weMp0z2-LmBEvhiZjSsu3p1RoQYojihSX0WbooI5ndCeFF1oKJZPaoBJc_uWGDfKnoxxJ9vZIn-GwgDWuoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mA736NZ2kK1YIoy_Isq7Wp6jyHN9wct5UBfZUjoBsJlwdSsz7IuyqPgggB5ISoqmhozYXilnaZe5DoPH2Cz16lwAITezMkis6metrlTASuPsYqEtw4IJ91PRR2KkPqB-qQ1Q47Ge7oXhDTLrnNr-cxABoOi--LdSDVAUqGjhtEqlnXk98Q44emaNYuIRu5-fUcRVJ4_0tw0heW5UW_zxxe6p5i1BGFm3L412z1EvgmQRnkcw7rzJRNGOEkdK4DpF_G2Dl7vMmiG83Um0RZZhbu3RijK9yeATKbfddYyI_UmtYDbWtWDhLGY5vGIMW3zkKL7UFDdg33FHpb1lejhT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3fQiS3Q7M_M2eMEGyZUsQ_U1pnMECHVSR0fdSuw4AMIGiWw8w9eTQCp_W8ILZpGo2jqA1lYxelig8Lk_AGdQeziT7xkK34z8xFtSvbofzo_Priah0hkkl2QBThaFKYxYvlCMZYFU3023YbC5-WXKwel5KAFrpYj5rPC62YhKGQjDe04qDd_pOHW6iFrTgQ6uWDNKx8kZyyol3eLtGoqyIZD2MLI8nlU5ceorT0w9oiOKrYjuENQOalJIuX4ebrLbX2wSsvdzWGsVi8O9Jqz_n_kHyyM2x70XN3RC2TLovZlFFmsiXg29DTnaaoNDuvls3QIVloOsEilgujucjhRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvCAmeOeV5PRC0YmJfstbQD1UF9Xx4oxJsCDOiInCK4kc2eB8wkZ2-pTZnmCXQ2pYjm9CWmx2SFtDEmK8rBpnEIPPoAzkTXo1ZhBQ_nctcH6L3-FhjPM5l49L-1MuiNHBKqvnZ9ZNXI6AYkQ03mhFt2240N5J_OzTdAnSO1buWHXA8iQEf6HWvyzW5nLiRnAeuXhq1RKRHEGriQR1XQBiOZ8AfE-8XjXUTfU-LMVK1647zpvP6IBJdg8i6hE7rqoW2ZGb7gdgkU1ix0BoWoCkl8CGdbQV7WjA4uSHkjq0VAQ2H5ymS4ShYfZAWbw0kA-a9ehTTx4wmfwstjQlGvncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1XZsb-KgtLYGtSy-_nknVP965iRieWcIgEbaAT2_sPfP6Guw2ETzRfKvE8Cnvaobn7eZ-eXnt0pZ2neKBOqUo-hfoKqzypiS4l-3eH_OZiT2LehBDRPv-zQe62xVyNrxM4VN7iYIRDDfX8Q7mVoLnSh7m3Nu1umx1rtn_kHOZ_UFV0CNQGARp5lZvl1qIZDy9_roIqy-ibsBruIDx3fjoN8anCr0F2JByfN0DpwjO2NkFXnzjPCmAQnYRa9T8FZ3bx2KA2LzM52s0SeSq_RJvhMbEJg-Qf3l4yAGr46HH7Gh-54zLJG4g2IRK08Ao5p4QwDRZLlUYC8jiS758GRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xab8aNhSY2AOgGOGDg1DoJi0RkCsNT9Scor5WhCgmvh56Rl1YRL3jZyhyoekGSIN86ovriBi2HFJo38plttP8hg0t0oRHPI9iJf_aMqdCuK2iOjGCnhYkd9d7vr6GbaTSLWmwP0AWWqL2v2jbcGqXzAVbE0GZo4COyTWE5xLTK-9DPYzDgYo-F9UEOkcl8YA-sGAEKPXXQWTf8BCV3imWyrkdfAu1l4U14hsjXP3gK6CyoO_5he6kF9ZgS7dQJRglNvRHFFnYXGpJiyDgrGQkjpOX-LokVHG1VvqA2N_1TAeFjINLogHNENdDUs0R8258tD6WRE93acjuCqSR-v4wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازدید دکتر سید جواد حسینی، رئیس سازمان بهزیستی کشور از دفتر تهران مجموعه رسانه‌ای خبرفوری
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3218110</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/654210" target="_blank">📅 21:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654209">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
اسرائیل گسترش تجاوزات در لبنان را به اطلاع دولت ترامپ رساند
🔹
کانال ۱۲ تلویزیون رژیم صهیونیستی گزارش داد اسرائیل دولت دونالد ترامپ را در جریان ماهیت و اهداف حملات جدیدش در لبنان قرار داده است.
🔹
روز گذشته مقام‌های دولت دونالد ترامپ به رژیم صهیونیستی درباره گسترش تجاوزات این رژیم در لبنان علی‌رغم آتش‌بس ادعایی اعلام‌شده چراغ سبز نشان داده بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/654209" target="_blank">📅 21:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654208">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798f002d6c.mp4?token=J2J5DxbBjNSsHoi-eq2jEHaUwnem9jbadp7VlASa3b2TG3IYZLSfcQhFetzuoB6jG3jSm1qno5uTQPDAGhw8i4nXXhq5msQyXuq5SwUtgrlY87Lt-UdaHzUl7SfZlfmOuqoBlP36Vfsq_XvUNY4LPQp5DVa4L-MwPEFHymSVOLKqhQRLr7ruFVbMuqwhzhCpKtgMfLjOeXPx-nweq90vta-MHDJ-pgzI08q_Ocf0MW1R0zkZ8q8arx6tdcpbasWBxYeomdc0FrocIb8TGqCOwTaZ-08WNEk5rNqtCSsav__jIUJwERE7DqZZcDcuY5TSw7TVh-EaIEm0dm5HCEuGTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798f002d6c.mp4?token=J2J5DxbBjNSsHoi-eq2jEHaUwnem9jbadp7VlASa3b2TG3IYZLSfcQhFetzuoB6jG3jSm1qno5uTQPDAGhw8i4nXXhq5msQyXuq5SwUtgrlY87Lt-UdaHzUl7SfZlfmOuqoBlP36Vfsq_XvUNY4LPQp5DVa4L-MwPEFHymSVOLKqhQRLr7ruFVbMuqwhzhCpKtgMfLjOeXPx-nweq90vta-MHDJ-pgzI08q_Ocf0MW1R0zkZ8q8arx6tdcpbasWBxYeomdc0FrocIb8TGqCOwTaZ-08WNEk5rNqtCSsav__jIUJwERE7DqZZcDcuY5TSw7TVh-EaIEm0dm5HCEuGTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار یک خودرو در حیفا
🔹
منابع عبری از آتش‌‌گرفتن و انفجار یک خودرو در منطقهٔ «اور عقیبا» در حیفا خبر می‌دهند. یک جسد از درون خودرو کشف شده و هویت او هنوز معلوم نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/654208" target="_blank">📅 21:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654207">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6LOxVrFQQnsXcktnwJp9qOyyYqvnNN_-4zlp2yN7s653T3X8BbAUYRoI3ijZLI3w2Lj08s3kny3jOnztdkD7QMNAXf5wnSP7XSTMCYS0MSrLWtmYdXRqJj0gzAVfmEHLj7Uabg2xi8WOVhJ9cf0zH47ZC69TQ91jWRvCOWjI5SiRQ0eb2_ofu_gv7aweXOU81xSqw9OkBLBmY3rfrNa42JKrXCxvtcFuG7rb28zU2ezsLh7henyNniCoMsz8u5FrJp4EHc2PBrDjt13n-VJ1fk8pG3OZ6cMpv50drJSTkBJU-GcTceaWh4HKXRLZSGyOrs8NOgXrTngiha9r6olaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب گسترده پیام حج رهبر معظم انقلاب در رسانه های بین المللی
🔹
پیام حضرت آیت‌الله «سید مجتبی خامنه‌ای» رهبر معظم انقلاب اسلامی به مناسبت برگزاری حج بازتاب گسترده ای در رسانه های بین المللی داشت.
🔹
خبرگزاری آناتولی با تیتر «مقام معظم رهبری ایران می‌گوید کشورهای خاورمیانه دگیر سپر پایگاه‌های آمریکایی نخواهند بود»، نوشت: «مقام معظم رهبری ایران روز سه‌شنبه گفت که واشنگتن دیگر نقطه امنی در منطقه نخواهد داشت.»
🔹
خبرگزاری فرانسه نیز به بازنشر موضوعات منطقه‌ای پیام امروز ایشان پرداخته و به نقل از ایشان نوشت: «مسلم است که عقربه‌های زمان به عقب بازنخواهد گشت و ملت‌ها و سرزمین‌های منطقه دیگر سپری برای پایگاه‌های آمریکا نخواهند بود.»
🔹
الجزیره در بازتاب این پیام نوشت که رهبر انقلاب اسلامی تأکید کرده‌اند آمریکا دیگر امکان ایجاد محیط امن برای حضور نظامی و استقرار پایگاه‌های خود در منطقه را نخواهد داشت. همچنین دعوت به گسترش همکاری و دوستی میان کشورهای اسلامی و ضرورت حرکت جمعی برای پیشرفت جهان اسلام از دیگر محورهایی بود که رسانه‌های قطری به آن پرداختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/654207" target="_blank">📅 21:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654206">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
اعلام آمار رسمی؛ ایران در جنگ تبلیغاتی آنلاین از آمریکا پیشی گرفت
سی‌بی‌اس:
🔹
تحقیقات نشان می‌دهد در حالی که سه ماه از درگیری نظامی ایران و آمریکا می‌گذرد، تهران در میدان نرم‌افزارانه و پروپاگاندا آنلاین موفق عمل کرده است.
🔹
بر اساس مطالعه مؤسسه گفتگوی استراتژیک، حساب‌های ایرانی در شبکه اجتماعی ایکس در ۵۰ روز پس از شروع جنگ، افزایش ۳۰ برابری بازدید و لایک را تجربه کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/654206" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654205">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تصاویری از هدف قرار گرفتن خودروی هاموی متعلق به ارتش اسرائیل در شهر بنت جبیل با ریزپرنده انتحاری ابابیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654205" target="_blank">📅 21:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654204">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7cdda78d.mp4?token=g364YJXgMhJMd2PPwuL26W0JPONB0Pn6FetR1Vjz662znSUvpoiAimKQuA8CYefIT79568EQte-9HRYSCudbHh_F92plMpKlWG_6qRKcw9WwJZN91sHN1-Hozi0tBZ3qFvgRGtFTYYFq-lrCIOY8DqE6Ttah0IDSIyQT7mXtobOy8IopAcCNAmFcunkll_uZ19_OfSmITLENR1xITyoKfSi28MxvG7gZEXLCocMBcxzLQ3sNC2c6UwX9FvBvJA0LHvBFL3H_MhloHSCDNdaOD9ymlvJULgC--zG7zOmddFwqdjDfiWG2EDpH6PxrzaHM3XK-FwqGmbyxgBV4cYnEHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7cdda78d.mp4?token=g364YJXgMhJMd2PPwuL26W0JPONB0Pn6FetR1Vjz662znSUvpoiAimKQuA8CYefIT79568EQte-9HRYSCudbHh_F92plMpKlWG_6qRKcw9WwJZN91sHN1-Hozi0tBZ3qFvgRGtFTYYFq-lrCIOY8DqE6Ttah0IDSIyQT7mXtobOy8IopAcCNAmFcunkll_uZ19_OfSmITLENR1xITyoKfSi28MxvG7gZEXLCocMBcxzLQ3sNC2c6UwX9FvBvJA0LHvBFL3H_MhloHSCDNdaOD9ymlvJULgC--zG7zOmddFwqdjDfiWG2EDpH6PxrzaHM3XK-FwqGmbyxgBV4cYnEHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عید قربان به حقیقت ز خداوند کریم
آفتابی به شب ظلمت انسان آمد
جمله دلها چو کویری ست پر از فصل عطش
بر کویر دل ما نعمت باران آمد
🔹
عید قربان مبارک باد
🎉
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/654204" target="_blank">📅 21:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654203">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d932c9054a.mp4?token=pxl675s5vn0fBzgITfpmEueY-UafJjRUAy4odm9x-nGdtPC8phTvWjw9Q-3ZoGApHdHAYtI-dO-qx_q6sjeTryr2SrD7P1_QDCxpSK9voA6U1CuES3NQQInDh4Rc7hgGNSdJbDrYfaprCyyYlF6Jn7CwRhxOpjof2WtrYiDzkAp3oY2763XvpqMVzrrmFIu_LBOrWWcwWSDYD_bxAAyjm7cj9JoLzNVDeS9U3EmykseENldGh3isJv_66xA9H_EPvB_b1Zl1clZGRKoM75mu_DAxV3L0W871fsSLJGfwoKLEW1FvtsbknQ9mc4ZAx6Spl3b94gndfTDAzCzQaoG2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d932c9054a.mp4?token=pxl675s5vn0fBzgITfpmEueY-UafJjRUAy4odm9x-nGdtPC8phTvWjw9Q-3ZoGApHdHAYtI-dO-qx_q6sjeTryr2SrD7P1_QDCxpSK9voA6U1CuES3NQQInDh4Rc7hgGNSdJbDrYfaprCyyYlF6Jn7CwRhxOpjof2WtrYiDzkAp3oY2763XvpqMVzrrmFIu_LBOrWWcwWSDYD_bxAAyjm7cj9JoLzNVDeS9U3EmykseENldGh3isJv_66xA9H_EPvB_b1Zl1clZGRKoM75mu_DAxV3L0W871fsSLJGfwoKLEW1FvtsbknQ9mc4ZAx6Spl3b94gndfTDAzCzQaoG2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات درگیری نظامی ایران و آمریکا در دو شب گذشته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/654203" target="_blank">📅 21:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654202">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaSXGx9hajuFPjIVA3MB9GNEjLpdov7mJjAkUx-4AXAZilkK8GAFq0png6IhrWN73T3sfKLeCZPm0VPHsAjCSeVC6KNOSIcP4X316fK-ncTXTn2Hwz6Ai2DFVTq8trZuTqV5Ps2e5YH-o13Tcz9k0_a4vGOWPRjj6e5ChAbA1Q3xJp1Pizn8Qmuw3zttxbWtkUWAwpLkX0TLruwazx3Dr0x9c7oeeGJWtL5xUS90m80tscgmp49poZ73ICsukRdp4OMKdpvt46Yk367DPh-BEMynUDGu4TAMxanlGgI2oZxB56YoWYZ4mozfcVs8mZNMkxJizoAgCW5F1zXcfTUr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تخفیف‌های ویژه چرم مَنطِـ آغاز شد!
تا %70 تخفیف
➕
%10 بیشتر
و 1,000,000 تومان هدیه اسنپ‌پی
برای خرید «حضوری و آنلاین»
کد: PAYSS9R
حداقل خرید ۴ میلیون تومان
مشاهده محصولات
👉
manteofficial.com
@manteofficial</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/654202" target="_blank">📅 21:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654201">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5n0nn7ceyuefUM2GqiXnNR6a2Wt1GyX7aOpb0MoySUovcjXJ7MsPcFJ1xb92AsHFCEJbDhZg_GHhsalw-vcD568J3jwFEkt7sOPXIFYjANS0uD6aAxbY4pEP40VbU5bkR7cEaqnlK7CvrLIoKFQm6FNUW6qjommYnInNwz7xsNXJcFcSIdfdvxCNGv-xUrh_Y0lHXSGSVjYoOHZ4EKly843uZkLOOkaf5yg68TC6QOtR2ZcI0YkA-GGDSABmh06NA-KiKYgMysfgBTytDdRCmptIyC8ZCrryLS232_mPyun6N-diquZan6ka1wD-nJpAlWuNQpaZwoS2Hjl1BGWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب گفتند: «سلاح الله‌اکبر»
الله‌اکبر یعنی: همان خدایی که دریا را برای موسی شکافت، هنوز زنده است
شما در یک جمله کاملش کنید:
الله‌اکبر یعنی...
پیام‌های شما در رسانه‌های خبرفوری منتشر می‌شود
شما هم در ویراستی خبرفوری کامنت بگذارید
👇🏻
https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/654201" target="_blank">📅 21:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654200">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqRYvj0JoBTZwfFz2yQjA-ax0yEo1-rEU1RPJXJZLWkPf45J3DlvMVodUu7Zfx1n56sPbPDVNLxHbHoj5scOp-FohOTMG6e4qkVpSQXxaCaXelOnnvZiUR2WJM7UZdH_a1wXCNbs9O5KIiY6e9R-sKvAOk16bELho6gLWHqt60StQR6BeOn_owH3P3np8DR7yXnU4KoCOD6bOf5rXRY81NTMuY4RNm6qGUR7m4HUv7IYlamgoUblRLGRf8QWCHbGo9Nj8EnbEX2dNRF6HEIH5o8SeoBdvjt8JBXnGua056RqblR--7xssGnfDxuDR1uTVrv9T-L5pYpobIQxCZ8V3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا کاهش چشمگیر نیروهای خود در ناتو را کلید زد
🔹
آمریکا در اقدامی بی‌سابقه طرح کاهش گسترده نیروها و تجهیزات نظامی خود در ناتو را به متحدان اروپایی اعلام کرده و از آنها خواسته است بار اصلی دفاع متعارف را تقبل کنند؛ اما همچنان نقش بازدارندگی هسته‌ای خود را در قاره سبز حفظ خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/654200" target="_blank">📅 21:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654199">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9662fd766.mp4?token=E8zYQNW_qSUTt2XnNqZUoFoZHkOC6dbfcHbjWC87sRrBRL-B_tIx0Q4rWKsOt0pXmOPEdq9gxBrMoHdMT_uK155lAQdqAwdl6Y30yCekpLcXkF8tVeOSlRbcWPW1iBJ0_a3Gq8Ml2sBb_cvUBjgFsDjXvOjWodSd8gzVutlIRcOJOlVN3D2pKJ8mnqfcc8MhuPozfM_zcnZTUaRkAvcyTS1KOVTpxjx3V6eraWuPj_-03buEc7F_FMkHFNek5cWYEDIi7cj7RGL477K4Nv_qS2YBNV-K6afXwCKlQBpwII64h-u9FX_BsVcf9h0v3-1Ux1uOo3z8qf7Epj8UqUeKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9662fd766.mp4?token=E8zYQNW_qSUTt2XnNqZUoFoZHkOC6dbfcHbjWC87sRrBRL-B_tIx0Q4rWKsOt0pXmOPEdq9gxBrMoHdMT_uK155lAQdqAwdl6Y30yCekpLcXkF8tVeOSlRbcWPW1iBJ0_a3Gq8Ml2sBb_cvUBjgFsDjXvOjWodSd8gzVutlIRcOJOlVN3D2pKJ8mnqfcc8MhuPozfM_zcnZTUaRkAvcyTS1KOVTpxjx3V6eraWuPj_-03buEc7F_FMkHFNek5cWYEDIi7cj7RGL477K4Nv_qS2YBNV-K6afXwCKlQBpwII64h-u9FX_BsVcf9h0v3-1Ux1uOo3z8qf7Epj8UqUeKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوای الله‌اکبر در سراسر کشور طنین‌انداز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/654199" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654198">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ice8Rmiz62iOK_iYvYHinndPp6GZX-hdQrgZx0wLiRuy0PYZTNwFxu-MToZqP0-EgECee-7GSdnLHOUZmFzT9P5iSejq-r2g1610t7BprGuhmB2ZVE7KI0GdQa3f5R1aK0QTarVX8cZfLNvzlUz3_qeNjHyW7VDR3zpCw1qmymhUoNACxjTx57SC4troB6RXbEV6fXMHtN21bywGek7dLxPM_ThSABVQmZr6DGlE_chkdbpNXhZWdW7SirTT21XDyDTZ1bdkJ6xNJZ8rSJgEuPKvq6Wega-DI8oLnRYfaMFBl_vrNUA-_joBauluckLUE09TipB_D0iTGSNYZzUbyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسئول حزب‌الله: ایران مصمم است لبنان بخشی از توافق باشد
🔹
عضو شورای سیاسی حزب‌الله تصریح کرد با وجود تلاش‌های آمریکا برای جداسازی جبهه لبنان از مذاکرات اسلام‌آباد، ایران مصمم است که این جبهه بخشی از هرگونه توافق برای پایان جنگ باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654198" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654197">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce48cacc5c.mp4?token=Lkrfw1U8a45xrEHAOiSnkHSNj8aChZnj8wPs941b0WJW40Nuz5Ib78JC1aXfySH6AwuGJGqSiWSW9w057LqdloFwMqrTKY-3vzNapwekzkgAV9EFU41SEhoMu0O2NQN5D2TTG6zeyBvVWKf0L3HxvsXMd1myQ1Vpl6wLWEynf3O6mvNKU9wAMdSSnnVEV9S3jYezPQ487Aex1BGxc09Js2TdpjgM_D7pGDWllKMAd3dY-4xYtdCYocnIALPJKud10WIa6x3j-H9f8Z8ZjUKQ_1spI2zfMHFSu4JFP5zs3YTSND9cliHZC1oRS4gQa-eU6xmWcHgdq5L6lOAadtzU1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce48cacc5c.mp4?token=Lkrfw1U8a45xrEHAOiSnkHSNj8aChZnj8wPs941b0WJW40Nuz5Ib78JC1aXfySH6AwuGJGqSiWSW9w057LqdloFwMqrTKY-3vzNapwekzkgAV9EFU41SEhoMu0O2NQN5D2TTG6zeyBvVWKf0L3HxvsXMd1myQ1Vpl6wLWEynf3O6mvNKU9wAMdSSnnVEV9S3jYezPQ487Aex1BGxc09Js2TdpjgM_D7pGDWllKMAd3dY-4xYtdCYocnIALPJKud10WIa6x3j-H9f8Z8ZjUKQ_1spI2zfMHFSu4JFP5zs3YTSND9cliHZC1oRS4gQa-eU6xmWcHgdq5L6lOAadtzU1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح الله اکبر
🔹
با سلاح الله اکبر بود که ملّت مسلمان ایران در چهل و هفت سال قبل قیام کرد، رژیم طاغوت، دیکتاتور و وابسته‌ی پهلوی را ساقط کرد، دست و پای امریکای طمع‌کار و مستکبر را از کشور بُرید و نفوذ صهیونیسم را بکلّی قطع کرد.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج | ۵ خرداد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/654197" target="_blank">📅 21:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654196">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-text">این زمان برخیز تا از بام‌ها
لرزه اندازیم بر اندام‌ها
🇮🇷
الله اکبر
🇮🇷
الله اکبر
🇮🇷
الله اکبر
🇮🇷
الله اکبر
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/654196" target="_blank">📅 21:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654195">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3mT-l8MKWIkV3rNM5-BASUYIsI_O9_6FQpoeGCl3kN2F41wie1nDih7SR2goRyBlCD8gd9Accnul59C_p0bgP7Tm7vsrmcAPPf8fhbvGk1_JLPVqdEZGy2TYKvzdytfSJfsQPluE10DmI0tW7Ufz6vZqcIDmX1lT38IfE_VVgcftT71W8YAQEwhg5ifOjHm7ePsGzDgXFT3oB9g5B-T2-fOGg6AFrffTz-E0MBJ-lRgtTxUZ-Fu2dN5YNZDo_-0KlaFcklkC7c_jNOknb-qs_aMwHRT23cB97pIbv37-0EIsVaSu86woSN58t_WSsi3ZO8LzdMYokhxeyG7APj6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو دستور گسترش تجاوز در لبنان را صادر کرد
🔹
بنیامین نتانیاهو نخست‌وزیر رژیم صهیونیستی امروز سه‌شنبه در نشست کابینه سیاسی و امنیتی این رژیم گفت که دستور گسترش عملیات در لبنان را صادر کرده است.
🔹
نتانیاهو در این خصوص گفت: «با دستورات من و وزیر دفاع (جنگ) و با هماهنگی رئیس ستاد کل ارتش، در حال گسترش عملیات خود در لبنان هستیم».
🔹
وی با بیان اینکه ارتش اسرائیل با نیروهای گسترده‌ای در حال انجام عملیات زمینی است،‌ مدعی شد که نظامیان رژیم، برخی مناطق را در جنوب لبنان اشغال کرده‌اند.
🔹
نخست‌وزیر اسرائیل در توجیه این تجاوزات که نقض آشکار توافق آتش‌بس است، ادعا کرد:«ما برای تقویت منطقه امنیتی در لبنان و همچنین محافظت از مناطق شمالی تلاش می‌کنیم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/654195" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654194">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
هشدار آمریکا به اسرائیل درباره حمله به بیروت
🔹
شبکه ۱۲ تلویزیون رژیم صهیونیستی گزارش داد که دولت آمریکا در پیامی صریح، مقامات تل‌آویو را از هرگونه اقدام نظامی علیه پایتخت لبنان برحذر داشته است.
🔹
آمریکا به رژیم صهیونیستی هشدار داده است که به هیچ وجه و در هیچ قالبی نباید به شهر بیروت حمله کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/654194" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654193">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
هشدار ایران به آمریکا: حمله به بیروت و ضاحیه مسیر مذاکرات را نابود می‌کند
🔹
غالب ابوزینب، عضو شورای سیاسی حزب‌الله: ایران از طریق واسطه‌ها به واشنگتن پیام داده است که در صورت عملی شدن تهدیدات اسرائیل علیه بیروت و ضاحیه، کل مسیر مذاکرات نابود خواهد شد.
🔹
دولت آمریکا پوشش کاملی برای تجاوزات رژیم صهیونیستی به لبنان ایجاد کرده است. ایران بر حضور لبنان در هرگونه توافق نهایی و پایان جنگ اصرار دارد.
🔹
حزب‌الله حق دموکراتیک خود می‌داند که دولت را با حرکت مردمی ساقط کند، اما هنوز به این مرحله نرسیده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/654193" target="_blank">📅 20:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654192">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جزئیات حضور پرستارنماها در اتاق عمل یک بیمارستان!
احمد نجاتیان، رییس سازمان نظام پرستاری کشور در
#گفتگو
با خبرفوری:
🔹
در یکی از شهرستان‌ها به ما اطلاع دادند که تقریبا تمام نیروهایی که در اتاق عمل کار می‌کنند؛ اینها همکاران گروه پرستاری هستند یا از رشته‌های دیگری هستند.
🔹
ما این موضوع را به وزارت بهداشت ارایه دادیم. چون ما اجازه نداشتیم به داخل بیمارستان برویم، از وزارت بهداشت خواستیم این موضوع را بررسی کنند و گزارش را به ما بدهند.
🔹
پرستاری که در یک هیئت انتظامی حکمی گرفته و ممنوع‌الکار شده است به راحتی می‌تواند در بخش خصوصی مشغول به کار شود چون جایی نیست که این را استعلام کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/654192" target="_blank">📅 20:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654191">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb8LPgUvCYCjomS2y-cm5QaubpTns-J86GondC9eUhAiLjjS-P2dB1cyo6FDkFXY7j5C3w7_rmszMjZ3sdV2iVVTr9uj2ypOFE7Wa6TlFJ8rl92LZLmTGwIh0YEBywLx2w0betQ-o1Ye3ux7i_NfCsbA6FBNf59Q16TjG6habcgmm-qT9G0-UbXIPyF9l43JJqTbrQ7HBpHD_Su-vjYY4SOBsIRL7HrPg89JGAAcz_Ytr9kubbja9SEpqJpMYVVo5V-n2uTETukzZCfnA1yG28wiJHwQbUFeKwyfGhumq1xhR_WQq70eBBmchwr9bmTW2MHbYrFIJ9CpWAMGyrgopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امشب ایران سراسر فریاد «الله‌اکبر» می‌شود...
🔹
در لبیک به پیام مهم رهبر معظم انقلاب اسلامی و در حمایت از وحدت ملی، جبهه مقاومت و آرمان‌های انقلاب اسلامی، از ملت بزرگ و همیشه در صحنه ایران دعوت می‌شود امشب رأس ساعت ۲۱:۰۰ در سراسر کشور، بر بام خانه‌ها، میادین و خیابان‌ها، فریاد «الله‌اکبر» سر دهند.
🔹
این ندای واحد، نمایش اقتدار ملت ایران و تجدید پیمان با راه شهیدان و ارزش‌های انقلاب اسلامی خواهد بود.
🕘
زمان: امشب ساعت ۲۱
📍
مکان: بام منازل، میادین و خیابان‌های سراسر کشور
🎥
همراهان عزیز؛ ویدئوهای خود از این همصدایی سراسری را به آیدی زیر ارسال کنید
👇
الله‌اکبر
🇮🇷
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/654191" target="_blank">📅 20:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654190">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
نگاهی به مانيفست مديريتی سيدعلی مدنی زاده
🔹
بررسی اقدامات وزیر امور اقتصادی و دارایی نشان می‌دهد نگاه دولت به «کریدورهای ارتباطی» از سطح یک پروژه حمل‌ونقل فراتر رفته و به بخشی از راهبرد کلان اقتصاد سیاسی کشور تبدیل شده است؛ جایی که کریدورها پیشران بازآرایی اقتصاد ملی و ابزار ارتقای جایگاه ژئواکونومیک ایران تعریف می‌شوند.
🔹
در دستگاه فکری سیدعلی مدنی‌زاده، توسعه کشور دیگر صرفاً از مرکز آغاز نمی‌شود، بلکه مناطق مرزی، آزاد و پیرامونی به کانون‌های جدید رشد اقتصادی تبدیل می‌شوند و کریدورها نقش «ستون فقرات» تحول اقتصادی را ایفا می‌کنند.
🔹
وزیر اقتصاد بر این باور است مزیت اصلی کریدورها زمانی ایجاد می‌شود که مسیرهای عبور کالا به «قطب‌های صنعتی و خدماتی» تبدیل شوند؛ هدف نهایی تنها افزایش عبور کامیون‌ها نیست، بلکه شکل‌گیری زنجیره‌ای از تولید، خدمات و تجارت در امتداد این مسیرهاست.
🔹
در منظومه فکری وزیر اقتصاد، مناطق آزاد تنها دروازه تجارت نیستند، بلکه می‌توانند به الگوی حکمرانی اقتصادی نوین تبدیل شوند؛ او از همین زاویه در حال مقابله با «بخشنامه‌های مزاحم» و حذف محدودیت‌های ارزی به عنوان بخشی از پروژه «آزادسازی واقعی» است./اعتماد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/654190" target="_blank">📅 19:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654188">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM4rcuuLs5PZI2ykSuKgNSZNKe0UWba2KfGQyG7f7j9sz1ANIESdASC8qxtljJrnKyw_-fb8fh5pCX4CukEFC0Cu4U9uLEk0C8MV_KReewRE0Yzt9GhwD9_H1hmTjB-sJHDlakz3H1jCysfGWdbrGj_S6xeZGausihnwEMbBBvzon06HOVok43cnDVLFPj46xta8YhW5vBad-1trhh1If3v4PgOnFWtgM8ydKElNNUQp1BF8BuKhYlcbUkvHH6tbwDLzFtd6whEzQfs-9hYe8ev_GEz3HEcfepRSYVcDYzinTnhBRTSnOa6IY5Q_Xm33No--UomI923ekNZqNawvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a942e9380.mp4?token=SilKgYuBTZ6wR3PyQvjG2DAHuS6IHy5VkzawtbQet4wHWbwhPLBXnbyfBrFAR-s-SHg7vkW55pwtc2uixCQjjJL0guXRKJHkznvaXjOJX3sG_rB7_KEbMW7cJAf3CXYUx0HI-OVWvjfs_FhbY4npqB6ML9rMZ1KEgYNDMyOvCpXBhviPvCQtI56bVVMqI2u60JRfyGA7C-AcvuLVyTz1ZYci796ZWa2LRYdw6ilTzH2nfmse0vGMgUbh6CiwOE1nTLmsTMtvoBUwQDGFB5VeC9KEVfNUaGu0TvO625w73FxOX--AC2SIj6Wf3olOeSsd0GqDiB2cmGAIELwFHFSgkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a942e9380.mp4?token=SilKgYuBTZ6wR3PyQvjG2DAHuS6IHy5VkzawtbQet4wHWbwhPLBXnbyfBrFAR-s-SHg7vkW55pwtc2uixCQjjJL0guXRKJHkznvaXjOJX3sG_rB7_KEbMW7cJAf3CXYUx0HI-OVWvjfs_FhbY4npqB6ML9rMZ1KEgYNDMyOvCpXBhviPvCQtI56bVVMqI2u60JRfyGA7C-AcvuLVyTz1ZYci796ZWa2LRYdw6ilTzH2nfmse0vGMgUbh6CiwOE1nTLmsTMtvoBUwQDGFB5VeC9KEVfNUaGu0TvO625w73FxOX--AC2SIj6Wf3olOeSsd0GqDiB2cmGAIELwFHFSgkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت وحشیانه رژیم صهیونیستی در غزه
🔹
ویدئو حاوی تصاویر دلخراش؛ در جریان بمباران جنوب غزه، محمد، کودک یک ماهه فلسطینی مادرش را از دست داد و پزشکان مجبور شدند به‌علت کمبود تجهیزات بیمارستانی، یک پای او را نیز قطع کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/654188" target="_blank">📅 19:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654187">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU0QO_ZVRemdxkEMDpeWCcO2zZJNPdruDRmALWFLdvk5bjkcD7Ik7T_iWoAQlhyLnZGK3neGkG7UrvB55SddrzqViRH_9BAUL06DDUykZw0EuS_Fb6gjNeX-VwXpOVKv2z89BNpbip-csgEoX4K5fFj2hLLIUybKs-0gHV8Wa9IYXw0LBCD45QLnDIz6114DOKaCaH0d9Pyd1nS8997VuaRQTfDvBpH9wd3IRxSgJzT-RFHJzYEQq3g4e78Ek0KVpshSUTuo34-PKufDLlAYeBEOYb0vDTk155I411Zxl56b-W5H_2xCz3QY3syoYtBx5NW1nyzRyuQ52kPKdv2Jbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورتنیکوف، رئیس سرویس اطلاعات روسیه (FSB): کشورهای غربی در تلاشند تا از تروریست‌های سوریه در جنگ علیه ایران استفاده کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/654187" target="_blank">📅 19:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654186">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5d-umv5TEqjSbyaDfFNtDsSt-6xBve903CMeZOk4LoyxtocB637_lvyxB_xneigG3bUnY3-WCVm8WIbCvVooVt--ovmhMLRM77uFKpXZKeWjvjvrc8v2lmc1A-gPkPqJS2JXWb8m2oz7SXxPgBpkQKcX8cVD92FGX7IT-EkRSuv5p-oXHUOlaC0uvvuY_ljcmSilzKq_NOKi7Cf5x9y3iIX4YleAvY-vFq9pIHYXFjkZLKHGlyzIqPCjcg-Zq2B1Hhb5XPaSx3M309LLbnDwndGjOIFItpYS44bd3E_9X-prr0NzKCoQUcxlXLpyiLNO-nk-QaPewAHsRcGtWxaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش امارات در جذب مزدوران کلمبیایی و اعزام به سودان
🔹
«ماوسی سگون»، مدیر بخش آفریقای دیدبان حقوق بشر امروز سه‌شنبه در بیانیه‌ای اعلام کرد که جذب و بکارگیری پیمانکاران نظامی خصوصی کلمبیایی، شواهد فزاینده‌ درباره حمایت نظامی امارات از شبه‌نظامیان پشتیبانی سریع را افزایش می‌دهد؛ شبه‌نظامیانی که بارها مرتکب جنایات وحشتناکی در سودان شده‌اند.
🔹
سگون افزود که صدها مزدور کلمبیایی به دست اماراتی‌ها در یک پایگاه نظامی در منطقه الظفره حدود ۲۵۰ کیلومتری (۱۵۵ مایلی) غرب ابوظبی و در یک مرکز دیگر در همین شهر قبل از اعزام به سودان برای جنگ در کنار نیروهای پشتیبانی سریع، آموزش دیده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/654186" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654185">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7v9vFtwHzrEAtROvi7klscV28YVMcqqFWZzd5hfPLYpst897kOnrsXP7vLDZN_1_ahfgtFt1UXKxFhombS5m7POLIUMLCpDOUQO3F9UgFPE1yoCzzZCze8v0lWXZ2NWDEvthg1p3bifgxGnSChtT_I7r_aaehrRSxE7etr_wDBwVOrLrY2NAJe1BS4L4C0UNisGDcIllSZIVq1J0eFznMPLqcr_duTg1K93IYhwl_h4xCImOSbzXt9AFhDjjY9HN1QRYtdI_xAB23e5yVmf5ogsUvhwBbLoevvX7iMgVWiMhf7b_03EJsO81xsifWK0yrNopXdIknTssCxg02e5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان در گفت‌وگو با امیر قطر: ایران برای دستیابی به چارچوبی عزتمندانه برای پایان‌بخشی به جنگ و تنش‌های جاری در منطقه آمادگی دارد
🔹
ایران صداقت و پایبندی خود را به مسیر گفت‌وگو ثابت کرده است؛ اکنون زمان آن است که طرف مقابل نیز اراده خود را نشان داده و در مقام عمل و نظر، به تعهدات بین‌المللی پایبند باشد.
🔹
تلاش‌های جدی و کارشناسی برای جمع‌بندی نهایی اسناد و متون پیش‌رو درحال انجام است تا مسیری روشن برای ثبات فراهم شود.
🔹
امیر قطر: دولت قطر از هیچ‌گونه کوششی در مسیر برقراری صلح، امنیت و ثبات منطقه‌ای فروگذار نخواهد کرد و همچنان به نقش میانجی‌گرانه و سازنده خود ادامه می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/654185" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
