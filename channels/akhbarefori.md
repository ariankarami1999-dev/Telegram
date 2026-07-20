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
<img src="https://cdn4.telesco.pe/file/EO0nGAgN7y0ioDz39dUd0ETLm18aF0ymHcc-WZ71t5mKinEnKubP5tVyT7PcYd8JKmO3K1r7i-GimMyqfB6KgF0fX0llHfYhQ6NZP5b6q6OVkvCRtYqtYtt8HntatS85WMWU3m20-2bZhNVe_6ltm0NRtpOSsQrM7D1lV5jAokEjNkfjLUxb5O3uzHbuZtp51KFFTBjNpZcSLQk438bWS_FVcXALVyVDHC4FaTWPu_I-DpHtQsaDXnPJv3nNVZ0WbyMbEpOHo5S72a23iZnfMCY6Dq4l1AHYmHB0T3eGBwZ9hkQrfQHFlW7CBbAN_k3XwpHj0_QbrBKrl5_52LX9OQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 08:29:30</div>
<hr>

<div class="tg-post" id="msg-673280">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
فقط ۲ روز تا پایان مهلت استفاده از اعتبار کالابرگ باقی مانده است
🔹
معاون اقتصادی وزارت تعاون، کار و رفاه اجتماعی: مهلت استفاده از اعتبار یک میلیون تومانی کالابرگ خردادماه، تا پایان ۳۱ تیرماه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/673280" target="_blank">📅 08:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
کیهان: اقدامات افراطی وبدگمانی به مسئولین ، نشاط جامعه را از بین می‌برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/673279" target="_blank">📅 08:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
منابع محلی از شنیده‌شدن صدای چندین انفجار در کویت خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/673278" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
صدای انفجار در نزدیکی پایگاه پشتیبانی دریایی بحرین شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/673277" target="_blank">📅 08:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
گزارش صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن به کشورمان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/673276" target="_blank">📅 08:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد MQ9 در آسمان اسلام‌آباد غرب
🔹
یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان اسلام آباد غرب رهگیری و ساقط شد./ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/673275" target="_blank">📅 07:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673274">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
یک منطقه در خورموج شهرستان دشتی مورد تهاجم دشمن آمریکایی قرار گرفت  یک منبع آگاه:
🔹
یک منطقه در خورموج شهرستان دشتی مورد تهاجم دشمن آمریکایی قرار گرفت.
🔹
این حمله موجب قطعی برق در برخی نقاط خورموج شده است/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/673274" target="_blank">📅 07:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673273">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادارات سیستان و بلوچستان به دلیل گرمای هوا امروز، ۲ ساعت زودتر به پایان خواهند رسید
🔹
روبیو به عبور موشک ایرانی از سامانه پدافندی در اردن اذعان کرد
🔹
رگبار باران و وزش باد شدید در ۶ استان نوار شمالی کشور از امروز تا چهارشنبه
🔹
دریای خزر تا فردا مواج و تعطیل است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/673273" target="_blank">📅 07:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673272">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
زلزلۀ ۵٫۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵٫۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند.  #اخبار_کرمانشاه در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/673272" target="_blank">📅 07:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
♦️
منابع عربی از حملۀ هوایی و شنیده‌شدن صدای انفجار در پایگاه‌های آمریکایی بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/673270" target="_blank">📅 07:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
زلزلۀ ۵٫۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵٫۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/673269" target="_blank">📅 07:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K52_nm344kYUipuSjXebGe5K0iEaRSX-esjXdaKrQwNts5GChfEjwYROpSy32icQHqVR6Xe4_lSHa04JxhANsqbjw9m6rJSRBGe-RfmTDeOXo6yJ-rvszBFAdwCs_IjOf6bSEfCC_OLGJCFZ_Cm4c8aBU7qyFFnCl-wdiyntHeA-2EcnKqbv4xgMDsK6ersY6M4xnCbhB2dDMzclF-iLqPbB363fqhEFIScPf6adQ8TVyYPJOTxGaknxGKVef0RJPvQbgAFYHaOSIrBDisphAo1JAdsHcLVAEVWtmJz2v9tadJaBfvwMSul8OSSWV_xwJ8_TPxTeQVyMICoQ6zI3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۹ تیر ماه
۵ صفر ‌‌۱۴۴۸
۲۰ جولای ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/673268" target="_blank">📅 07:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۰/ دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند  روابط عمومی سپاه:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی؛ اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک کوش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/673267" target="_blank">📅 05:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: بهای نفت خام برنت از ۹۰ دلار در هر بشکه عبور کرد و به بالاترین سطح خود از ژوئن (خرداد) تاکنون رسید
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/673266" target="_blank">📅 04:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673265">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۰/ دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
روابط عمومی سپاه:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی؛ اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک کوش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگه هرمز را داشتند منفجر شده و از حرکت باز ماندند.
🔹
اینجا سرزمین ماست و دخالت ارتش تروریستی آمریکا از هزاران کیلومتر آن طرف‌تر هیچ وجاهت قانونی ندارد و با قطعیت با آن برخورد خواهد شد و تا زمانی که شرارت های آمریکا در منطقه ادامه یابد این معبر برای عبور کود شیمیایی و حتی یک قطر نفت و گاز امنیت ندارد.
🔹
ارتش متجاوز، آماده عملیات تنبیه ما به خاطر این تخلف غیرقانونی باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/673265" target="_blank">📅 04:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673264">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
مهر: صدای چند انفجار در شهرستان دشتی بوشهر شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/673264" target="_blank">📅 04:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673263">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4b0f0d21.mp4?token=FYcT9QkvDKzMl94xObl6Vkddc37r9ogKrC7GvmjpKQSnW3ELeopYUED8xbWsLqM-ZJmSKlFS6MYHXp1Bimh8dcbX8pa-pGMSed07UD3AE8s55c169Q-8ZDMsf8I1NE4Uythl5htZ2OpanHOY3Wor3f9nvgQYZVoTbKU3m_qvxNsz20z5n4LFdsPVa-5vzT0M0Ut5UgRx1GPht7Loqhz9mQwrB5wZ5yYiw9MVvpch7LEPmauOTv5xsA1r-KkXkFoeKpFijXmI61xWPkez8utWEZTt2rEAfiIY4__xYUKLuHbAomMnbi-svR4WvTD8wQgwNJ7gS8k3p3rvsswLBwFpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4b0f0d21.mp4?token=FYcT9QkvDKzMl94xObl6Vkddc37r9ogKrC7GvmjpKQSnW3ELeopYUED8xbWsLqM-ZJmSKlFS6MYHXp1Bimh8dcbX8pa-pGMSed07UD3AE8s55c169Q-8ZDMsf8I1NE4Uythl5htZ2OpanHOY3Wor3f9nvgQYZVoTbKU3m_qvxNsz20z5n4LFdsPVa-5vzT0M0Ut5UgRx1GPht7Loqhz9mQwrB5wZ5yYiw9MVvpch7LEPmauOTv5xsA1r-KkXkFoeKpFijXmI61xWPkez8utWEZTt2rEAfiIY4__xYUKLuHbAomMnbi-svR4WvTD8wQgwNJ7gS8k3p3rvsswLBwFpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرمربی آرژانتین درحالی که سعی در کنترل احساسات خود داشت گفت: تا عمق وجودم درد میکشم!
🔹
به اعتقاد من، مسی بهترین بازیکنی است که تاکنون پا به زمین فوتبال گذاشته است.
🔹
ساختن و تکرار کردن همچین گروه قدرتمندی بسیار دشوار خواهد بود و این درد دارد.
🔹
اسکالونی نتوانست اشک های خود را کنترل کند و نشست خبری را ترک کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/673263" target="_blank">📅 04:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673262">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60f4fe31b.mp4?token=ufb3L1cxb_OmM1Ct_AURC2yPJLjeTAQfT9LOXBkvelggyBBUj2Us1umRhpXGnj-7fUMRlaMS2RNZzHr3ywrIojNczeTJEghHFN4-XQ6OARZI1pSTjnxBxPeuDRMe2GvojOJvZe6c578RJFtOQ78lHnBMB2By-r2vVap81KG1qB579RmtlDJYVKjb-7BfbFK6OPsELts5_9JvFtFDm_B8hhPFT3K6FNXL_ce4msKzsl8XLcNhEGJq9oRYFdKPD7APXn9zRcM14BFkJ2U6mxAjvrVcyBoO88797yuMvSmwBhndGWnXc2OoH2faN9i-IY0kHplpIEwxIjpZ1dei8yYEGAmUsnVwrjaCeUaoOqk56n2k2ZTC5bOR-BUp-U2Jek3zKzXa3tO5FLZxucPtwpTG_lZax4XwAiHnzOZT8Kz1IkYOS5CnPzTKndVCta-f4RdJleRS7SzWt0Kog_Pzaa-vxNmffSzA3b8IJVUZ2YWgioYWu3RFf-MmQ35yQCZ8SleqnrStmT8ZNOllst5bITtaXNRSDg3Jj56fOwAd91TFB4LZggL7kZDji7gk-KnQpEf96rV4xKlFJkhrQoNbw8xWrGIMJcVoeBVY3_3Z60abcAW3ggNMb7m5kl4f4jEoe01HD3d3zo4g3nbxmD1knneseUfGsgN281fG7ZUmQ-bPK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60f4fe31b.mp4?token=ufb3L1cxb_OmM1Ct_AURC2yPJLjeTAQfT9LOXBkvelggyBBUj2Us1umRhpXGnj-7fUMRlaMS2RNZzHr3ywrIojNczeTJEghHFN4-XQ6OARZI1pSTjnxBxPeuDRMe2GvojOJvZe6c578RJFtOQ78lHnBMB2By-r2vVap81KG1qB579RmtlDJYVKjb-7BfbFK6OPsELts5_9JvFtFDm_B8hhPFT3K6FNXL_ce4msKzsl8XLcNhEGJq9oRYFdKPD7APXn9zRcM14BFkJ2U6mxAjvrVcyBoO88797yuMvSmwBhndGWnXc2OoH2faN9i-IY0kHplpIEwxIjpZ1dei8yYEGAmUsnVwrjaCeUaoOqk56n2k2ZTC5bOR-BUp-U2Jek3zKzXa3tO5FLZxucPtwpTG_lZax4XwAiHnzOZT8Kz1IkYOS5CnPzTKndVCta-f4RdJleRS7SzWt0Kog_Pzaa-vxNmffSzA3b8IJVUZ2YWgioYWu3RFf-MmQ35yQCZ8SleqnrStmT8ZNOllst5bITtaXNRSDg3Jj56fOwAd91TFB4LZggL7kZDji7gk-KnQpEf96rV4xKlFJkhrQoNbw8xWrGIMJcVoeBVY3_3Z60abcAW3ggNMb7m5kl4f4jEoe01HD3d3zo4g3nbxmD1knneseUfGsgN281fG7ZUmQ-bPK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی که نتانیاهو قبل از فینال جام جهانی منتشر کرد
🔹
نتانیاهو قبل از بازی فینال در تماس تلفنی خطاب به رئیس‌جمهور آرژانتین، خاویر میلی: ما از آرژانتین به طرق مختلف حمایت می‌کنیم، از جمله فردا (در فینال). من پنهان نمی‌کنم که طرفدار آرژانتین هستم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/673262" target="_blank">📅 04:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673261">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0381272b35.mp4?token=lhHvXUAuQpfIvfpC5x4C-6XEj-MH5wyNelyhMCPWC0qq0HL-yZpYc5MhpoUceNe1kFwPXRhdSZ1vuK_22he7uWxyVwleDYav9WquOEvflTZBsfPd0RQ9M26hzNfJ_Hnr5cG0XSDHKW4Pd7a42WiY-l7GL7FpXBO2kJY_LXZhZKwr4B-nfrl3oRBlWZQ6CJfR6OYfI12rgJxLu1koeaW_S5hJz4_bo7mWxvz49YXZBLQz6MIitSUJ6hEHhk9LA9DWtGgcdi1WK9au3uE14I2wX409GUgXOm7zo25nvieZzxkCF5imSESjk5epwtGgC2csLUdQAdAFZkNhVMY3OlnUXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0381272b35.mp4?token=lhHvXUAuQpfIvfpC5x4C-6XEj-MH5wyNelyhMCPWC0qq0HL-yZpYc5MhpoUceNe1kFwPXRhdSZ1vuK_22he7uWxyVwleDYav9WquOEvflTZBsfPd0RQ9M26hzNfJ_Hnr5cG0XSDHKW4Pd7a42WiY-l7GL7FpXBO2kJY_LXZhZKwr4B-nfrl3oRBlWZQ6CJfR6OYfI12rgJxLu1koeaW_S5hJz4_bo7mWxvz49YXZBLQz6MIitSUJ6hEHhk9LA9DWtGgcdi1WK9au3uE14I2wX409GUgXOm7zo25nvieZzxkCF5imSESjk5epwtGgC2csLUdQAdAFZkNhVMY3OlnUXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: فکر می‌کردیم دو نفر در حملات ایران کشته شدند اما احتمالا سه نفر بودند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/673261" target="_blank">📅 04:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673260">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52efb5cec6.mp4?token=TVPuQwqMsc-fuuidCBRsTtfvZKlFA6Um-fa7W-YyWkvRdPD-6Pd3zUKNQC3k0QeKMyYZ4vzsl2P86cUebKO2Enp6-EGut5cB4sr61_K9FI0ndFIn4ojGsCzdtc8QcvVRObHRr0DJsX561AvIemekXI1knPMgA4P07YgEvP9fM9Txq8SNPGw9ZtiHEh_UtJE8YjsncqlOP5Lduv8P7ixvUj3NHWj_bQd1j8on85Rm-cNZCAuARQpugNJnxBxv7E8SPVXDA-kQ9LSvVceCvK4o4Px4uzGZF8ggsZ3iBgMR5VdnUi4IEMjL6i1mBwlh3ZYNp3v5HgpmBEden9DJp2fDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52efb5cec6.mp4?token=TVPuQwqMsc-fuuidCBRsTtfvZKlFA6Um-fa7W-YyWkvRdPD-6Pd3zUKNQC3k0QeKMyYZ4vzsl2P86cUebKO2Enp6-EGut5cB4sr61_K9FI0ndFIn4ojGsCzdtc8QcvVRObHRr0DJsX561AvIemekXI1knPMgA4P07YgEvP9fM9Txq8SNPGw9ZtiHEh_UtJE8YjsncqlOP5Lduv8P7ixvUj3NHWj_bQd1j8on85Rm-cNZCAuARQpugNJnxBxv7E8SPVXDA-kQ9LSvVceCvK4o4Px4uzGZF8ggsZ3iBgMR5VdnUi4IEMjL6i1mBwlh3ZYNp3v5HgpmBEden9DJp2fDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت حملات مکرر آمریکا به سیریک اعلام شد
🔹
دشمن سعی دارد با حمله به سیریک، اشراف اطلاعاتی ایران به تنگۀ هرمز را قطع کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/673260" target="_blank">📅 04:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673259">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuVWMsOjHnvP-A3ru_dmR-QRqD841qkxTOWc7Kh1zLv7IKaT5p0LI8nt2Z_K6EcBAkzqFXLARDufx3YkwPBxKBnBJbu74oZa9ZZDFMXe1mRInvaC4VDWLtDiKwcZ8c40RR_KnnF1KnC53EGBBAMFzNGJT3FvslcA6d1CLwewQ5slBtKNVh-TqTOF5DN9pVXah67EXsEVVEGkY8q0cR1PnDEfK35-VHPaGoFlBRvPJaQui_ZcKKqUH-hgLF1ANCrKRZ2tGY8BPIrJ46RdEWlVCitgknIAPqAAbNWOuVW6_AQXjCxOWsTrgXTY5KDEIzxrc1YEO9-OqQU0vUOx__9MTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس یامال بر دیوارهای غزه
شکرا یامال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/673259" target="_blank">📅 04:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673258">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca23ce1378.mp4?token=F3Zx18zGDaJGoZnscDDm9Krx5JheWWkkCDnncb7Uq-dWnOtvlkY2zxKra3mBlPX9_eFYYYrJjrw1IN3snsbtmemFJaegmoi_coH9jZIIUDcgCJnZLJZFFnOgM1n8MbrMHQX0yCB5dYUOtZ0KTx-Q5F5_mt9_XIZAxZf12eFqoWUJYM0-QJID71gbd-MiXHn4m49xduo1z6OhmAWJX_bjiqF4GTHVberP2jevucfZfl1t4pBjCjr8S9aXNhBnYbJ8f-TqeTJVWyjyu06pYeu5mlJcpQIRrEsR4GaVkvdPie6YNZvptMIm8_L5zTwMAttUgVZMNyXKHuGvltlYwbAOmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca23ce1378.mp4?token=F3Zx18zGDaJGoZnscDDm9Krx5JheWWkkCDnncb7Uq-dWnOtvlkY2zxKra3mBlPX9_eFYYYrJjrw1IN3snsbtmemFJaegmoi_coH9jZIIUDcgCJnZLJZFFnOgM1n8MbrMHQX0yCB5dYUOtZ0KTx-Q5F5_mt9_XIZAxZf12eFqoWUJYM0-QJID71gbd-MiXHn4m49xduo1z6OhmAWJX_bjiqF4GTHVberP2jevucfZfl1t4pBjCjr8S9aXNhBnYbJ8f-TqeTJVWyjyu06pYeu5mlJcpQIRrEsR4GaVkvdPie6YNZvptMIm8_L5zTwMAttUgVZMNyXKHuGvltlYwbAOmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن به کشورمان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/673258" target="_blank">📅 04:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673257">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای خوک هار: امشب ضربات سختی به ایران وارد کردیم
🔹
ما امشب به احترام سه سرباز کشته‌شده، ایران را به‌شدت هدف قرار دادیم.
🔹
ایران احتمالاً تعدادی موشک و پهپاد در اختیار دارد، اما تعداد آن‌ها زیاد نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/673257" target="_blank">📅 04:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673256">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای
خوک هار: امشب ضربات سختی به ایران وارد کردیم
🔹
ما امشب به احترام سه سرباز کشته‌شده، ایران را به‌شدت هدف قرار دادیم.
🔹
ایران احتمالاً تعدادی موشک و پهپاد در اختیار دارد، اما تعداد آن‌ها زیاد نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673256" target="_blank">📅 03:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673255">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سفارت آمریکا برای اتباع خود در بحرین هشدار امنیتی صادر کرد
🔹
سفارت آمریکا در منامه از تمامی شهروندان این کشور خواست هوشیاری لازم را حفظ کرده و از دستورالعمل‌های مقامات محلی پیروی کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/673255" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673254">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
یک شناور در شمال‌غربی منطقه «کمزار» در نزدیکی سواحل عمان دچار آتش‌سوزی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/673254" target="_blank">📅 03:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673253">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای انفجار در امارات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/673253" target="_blank">📅 03:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673252">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
صدای دو انفجار در حوالی خورموج بوشهر شنیده شد
🔹
در استان بوشهر، صدای دو انفجار از حوالی خورموج به گوش رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673252" target="_blank">📅 03:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673251">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjFijP77yDIVyw-L9XVs3gA_VRAQs9rxoMpJXMFy0Sz8vjyJ5oqRw2LsW1FXMx0_-ERK-cZMZhJID4Dssjk97iJudlGbQ78o0UNSXScWohkBuFLFkpCHAdjEpefAq0TfeUNb9xRVN9nyySEi7hYmq_CFNMtARsTp5VbQwPJCSk7KMk3ctgdQtEMsqkE4ma9aP7lhCo6ojPCPmQWw-HM8tjRBIimeGrNNsba9jQiqPow9mORORzcMVkuvt1ViIQ7kxQIe4K46kfsfXsv9f2Yf0CaWYIP-AXwCcTD0jykoJiV4PyBQzC17JawELumIOR8mCWUTB3ckYbG8HYyq_09Y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه دریایی در نزدیکی سواحل عمان خبر داد و اعلام کرد یک شناور در شمال‌غربی منطقه «کمزار» دچار آتش‌سوزی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/673251" target="_blank">📅 03:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673250">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/673250" target="_blank">📅 03:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673249">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
شنیده شدن دست‌کم ۳ انفجار در جاسک
🔹
منابع محلی از شنیده شدن دست‌کم سه صدای انفجار در شهر جاسک واقع در استان هرمزگان خبر می‌دهند.
🔹
هنوز اطلاعات دقیقی از منشأ و علت این صداها در دست نیست و مقامات رسمی تا این لحظه واکنشی به این حادثه نشان نداده‌اند. وضعیت در منطقه تحت بررسی است.
🔹
جزئیات تکمیلی در خصوص این رویداد و خسارات احتمالی آن متعاقباً اعلام خواهد شد./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/673249" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673248">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
صدای دو انفجار در حوالی خورموج بوشهر شنیده شد
🔹
در استان بوشهر، صدای دو انفجار از حوالی خورموج به گوش رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/673248" target="_blank">📅 03:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673247">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCWqQJnk2FfHvUKXHgJE7FzSIxFSfYXmRTclDuESA8hROkh0UfMb97He7fNCpNKWcS0KTz4gA1XhyuuqdxbSNXMi6fZPkriQUWh9pVs3OiZmL9Yvp4eucGJbExHGUBfqGlJpboE_8NoG1pW79CynxO6Lospj6L7p1wiyk8IEoGne6jj_dQb5bhfE5m1iibv9h0k0kCtgtXXY3oHvvOxMS69vx1FVKd_yw1_Zdcnn9eaZ48PUwucd3DoMsYo7R7rcqOqmLLPJzDKc8Xfr3SNRpd-HcRCZiY8vNm2HBGNbRtt2KNPhZ7_LzQbb_84sN7pRVRetxLxFuqGqlwG01mQy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر معنادار از مسی و جامی که ۳.۵ سال پیش بر روی دستان او بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/673247" target="_blank">📅 03:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673246">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
برخی منابع از شلیک موشک به سمت کشتی‌های متخلف در سواحل امارات گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/673246" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673245">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ساکنان محلی از شنیده شدن صدای چند انفجار در محدوده شهرستان سیریک خبر دادند
🔹
بامداد دوشنبه برخی منابع خبری و ساکنان محلی از شنیده شدن صدای انفجارهایی در شهرستان سیریک خبر دادند.
🔹
هنوز ماهیت صداهای شنیده شده توسط مردم مشخص نیست./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673245" target="_blank">📅 03:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673244">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سفارت آمریکا برای اتباع خود در بحرین هشدار امنیتی صادر کرد
🔹
سفارت آمریکا در منامه از تمامی شهروندان این کشور خواست هوشیاری لازم را حفظ کرده و از دستورالعمل‌های مقامات محلی پیروی کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/673244" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673243">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای انفجار در امارات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/673243" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673242">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای انفجار در امارات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/673242" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673241">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
صدای چند انفجار در چابهار شنیده شد./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/673241" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673240">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندر امام خمینی
🔹
لحظاتی پیش گزارش‌های مردمی حاکی از شنیدن صدای چند انفجار در بندر ماهشهر و بندر امام خمینی در خوزستان است.
🔹
اخبار تکمیلی از زبان منابع رسمی به‌زودی ارسال می‌شود./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/673240" target="_blank">📅 03:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673239">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندر امام خمینی
🔹
لحظاتی پیش گزارش‌های مردمی حاکی از شنیدن صدای چند انفجار در بندر ماهشهر و بندر امام خمینی در خوزستان است.
🔹
اخبار تکمیلی از زبان منابع رسمی به‌زودی ارسال می‌شود./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/673239" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673238">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c661eb85.mp4?token=Kw7O-Haub2js2ydqrrvTtwqxaHbUoSUGgEeYYSlr3IwGnA9C_sIr1_m7-1mRnLNkgYEFwrDcBjPN1Y93AJxKQ3gALwLfHNhU3dCj90-3WoxhFqLHc5KJY8nqchS9UZv4VFq83lXz6yerGkNGCGieOZKZVPbiuGPosxFIvKKj0ujIY8I1dBm7uTdpJMU9DaYp9j5tNEIwPnKB61dp5W-tKZ-tpxt_2bdHuCtDQgGXh4mdTTi0ddJ4ThLb9JM2YyyWT948C6Intwct8XzeMVbiw8yS3jZS3xsmzZWioqPqvbb7gN96DTSKVE0lX3kA5-7hO4fwcG3S6QuWKL_MXmTKqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c661eb85.mp4?token=Kw7O-Haub2js2ydqrrvTtwqxaHbUoSUGgEeYYSlr3IwGnA9C_sIr1_m7-1mRnLNkgYEFwrDcBjPN1Y93AJxKQ3gALwLfHNhU3dCj90-3WoxhFqLHc5KJY8nqchS9UZv4VFq83lXz6yerGkNGCGieOZKZVPbiuGPosxFIvKKj0ujIY8I1dBm7uTdpJMU9DaYp9j5tNEIwPnKB61dp5W-tKZ-tpxt_2bdHuCtDQgGXh4mdTTi0ddJ4ThLb9JM2YyyWT948C6Intwct8XzeMVbiw8yS3jZS3xsmzZWioqPqvbb7gN96DTSKVE0lX3kA5-7hO4fwcG3S6QuWKL_MXmTKqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش حماس به قهرمانی اسپانیا  باسم نعيم عضو دفتر سیاسی جنبش حماس:
🔹
ما پیروزی شایسته اسپانیا در جام جهانی فوتبال را تبریک می‌گوییم، این شادی را به فلسطین و حامیان آن هم تبریک می‌گوییم. «حتی اگر تنها فایده این پیروزی، آزار صهیونیست‌ها و همدستانشان باشد، همین…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/673238" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673237">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
انهدام پهپاد متخاصم در جنوب کشور
🔹
یک پهپاد متخاصم در آسمان جنوب ایران، توسط سامانه پدافند نیروهای مسلح ایران مورد ساقط شد.
🔹
اخبار تکمیلی بزودی اطلاع‌رسانی خواهد شد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/673237" target="_blank">📅 02:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673235">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN2t88jGGx-q4Oz5nWs5IW-Op75v2szFXl7mfqPwe7VSSlgdsAVwgi1lQBbazoTNjnFNb4xV_usk9rDZMkZ35ENmP8g_sYwkz16xYyEYP61fHRQjKEx7vXIAYbbc4knZ0xkJFXA4jVxhFClYTJHkQjzeKbR7smn2jWG1WCCnwli2mPvUcfQ-qZ76AfYx0aCi9kUkc2i6pgXFZj9C6sBmtPRoJjAdI3qVTusthf0Si_Pffs0XHtCEH-korRukFL_wwgCdK2f6DsELjKEL3xkByJFYcSDuPem-Z_ksIYt38jleQKL2lqL7LS0yxCDoomYpBETUg5m8D0DSGd80eg775Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb6a899b6.mp4?token=LnEz2AzQEL6YS_9xMzE9sJ4D2dfAmfAeKZ70-Y2_4eIk1fuDMRuM9JsS885yoiET91IJ9_qX-Z4OmxvN8vG-6ULH_HKs58kFcu9PN74S_kj3Or93rcPOSdsDP0EAnJ7Sm3UPmCsVOT_JwMRKsTMrc0VOerZDWVX5IMKWfBNYxd5h_3-Y9ywoRMxXcGE7SEOS4GW6O-j1sbHEsPATNZ47f3cjtgO83j5V497239fU9PLt0yiNaIOsSw0jLKSsonHawRMKaem3wDjP2NqHCcHbGllnMkxhaUz0jLOZuw5t9s3ll9iNSBj96EIYryh9hVvBpbb85Ik1dPOaSucVoDH2_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb6a899b6.mp4?token=LnEz2AzQEL6YS_9xMzE9sJ4D2dfAmfAeKZ70-Y2_4eIk1fuDMRuM9JsS885yoiET91IJ9_qX-Z4OmxvN8vG-6ULH_HKs58kFcu9PN74S_kj3Or93rcPOSdsDP0EAnJ7Sm3UPmCsVOT_JwMRKsTMrc0VOerZDWVX5IMKWfBNYxd5h_3-Y9ywoRMxXcGE7SEOS4GW6O-j1sbHEsPATNZ47f3cjtgO83j5V497239fU9PLt0yiNaIOsSw0jLKSsonHawRMKaem3wDjP2NqHCcHbGllnMkxhaUz0jLOZuw5t9s3ll9iNSBj96EIYryh9hVvBpbb85Ik1dPOaSucVoDH2_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بورخا ایگلسیاس، مهاجم تیم ملی اسپانیا با بی‌میلی ودر کمال بی‌توجهی به رئیس دولت تروریستی آمریکا، دست داد
🔹
علت دست دادن ایگلسیاس: «من نمی‌خواهم به زندان بروم!»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/673235" target="_blank">📅 02:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673234">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
صدای انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار در تبریز به گوش رسید، هنوز هیچ جزییاتی مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/673234" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673233">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای سنتکام: از ساعت ۷ عصر امروز به وقت شرق آمریکا (ET)، برای نهمین شب پیاپی موج جدیدی از حملات علیه ایران را آغاز کرده است./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/673233" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673232">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f0d26c63.mp4?token=qA76QjU55SSwE1tgXgWYdsdZTn0Co-BcJN6gV3yVeFVhKSmG2APSQbarLmURXK4NbQ37lag5vVqLT6KL-050Q6tlVDSAg37LlgydkkIddXNbU-upxQlo8ZALDEXhjFpyCwF3GHAx4SOqBRmyZbdJNtI6-qNCxdDm1nPUDdZhDmVJwONilZI8JVGCeZc6aJyUqtuy8NXexjzJrVAdk0VumFosjpuSHYY1ewLHW7ZznF-grUVmNzybU7Rw_sYYQuB4m9L6OVD5Osp-GPlxBl3-hICZTHkMutapMmdWweRU9etG6aPaSfG8ExGahlGpLBR3-bFn7Ls9pp6_8WLJl51e1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f0d26c63.mp4?token=qA76QjU55SSwE1tgXgWYdsdZTn0Co-BcJN6gV3yVeFVhKSmG2APSQbarLmURXK4NbQ37lag5vVqLT6KL-050Q6tlVDSAg37LlgydkkIddXNbU-upxQlo8ZALDEXhjFpyCwF3GHAx4SOqBRmyZbdJNtI6-qNCxdDm1nPUDdZhDmVJwONilZI8JVGCeZc6aJyUqtuy8NXexjzJrVAdk0VumFosjpuSHYY1ewLHW7ZznF-grUVmNzybU7Rw_sYYQuB4m9L6OVD5Osp-GPlxBl3-hICZTHkMutapMmdWweRU9etG6aPaSfG8ExGahlGpLBR3-bFn7Ls9pp6_8WLJl51e1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون مقرهای تروریست‌ها تحت حملات شدید ایران
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/673232" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673230">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLNmTUVkfjVA5sur3frCwb9VppNZ0rDZrlhCpZ6lM6cn0N_edpto1cR2Yye7zJVwtJWultKRBMpIJ30iu6wGNTRjuwUqfpi0NIVWBV5ni6bu4mWsKnTxgpQvI1pSkK8U_dbfO0S3MxleGxMuEpgfnD5-fCVLiz5TASnYjeLwdoXf1rvDYUoK8ywE59zcUJ_BTuc0wNeY_boHGUTSYWybtadcgp_uDRoGY4_cFoLZRoMHXGgEMU1pupTfoFO1W9NfMzidu5ldgCkf2peQn_H2BwbYFwxLI1bmyg5Nb9zEIr35jzusfTF9KKgmKPRfY4injqIph9kbSIxYhQ3a5p-ptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-T0UgpED3zYEOWJ4jeF540GD8l94T1ONStQ6vY7WN3L5NO73SEdNN8GjTNA1z6A6HMdetrcSBVzxGgv0yAyrrqRgBsI8LhVmXbWxGFZiw1PW5_2YBJ0VVTFo48WZ7SzNf987GNhXG7AM4-bdLBsalFLUosy4awjXMtye2bY_5MhYeGu7DDZQmOI9D_CB5AGNPCuwa6rnbFC8Z4uoDznvYiyfhBlg0vGAyNj34Bsm9ccAUpyJNDyvvYFjaAxHOc6-IF9zZXEkLqog5ZLniCErm8QO20HPj_3zY61NC7LVd21ALnm5ch7j1n-UVyjWMmVbx4RPqZERTrNXpaCgLG6bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چشم‌های یامال احساس تنفر نسبت به ترامپ کودک‌کش را فریاد می‌زنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/673230" target="_blank">📅 02:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673229">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cdc7cef56.mp4?token=YAM_xG6gg1_O-BF4v6mvLwdooyQPk5ultOf6knKTBbQyLKnVnUieockMF-b1_c3eYaxB5E-p53GzUGwM9SvZ4_7zFmwViCjtPAWAQTGl9VhELbH7uCSH2N_Jiu1advtMPDLoqLjKzrT1609oRfgPRHCsQnWDEAeUZSoVKChZbaZv3YuZ8i-y5_PI0QTqd5bdfrGeD6IkkgLozijtAKItYm-3yS8QeN3hrVWWdXJ9Ux_rc0IEn7DHbC8me06i7akOn28TmLbQZaZSP721sv2mNNeFcmLZx79m0WKRU_DSmq937S9hCRPXleaxaP0P0sT3e-zHb1rgawnm8u5GLBNaTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cdc7cef56.mp4?token=YAM_xG6gg1_O-BF4v6mvLwdooyQPk5ultOf6knKTBbQyLKnVnUieockMF-b1_c3eYaxB5E-p53GzUGwM9SvZ4_7zFmwViCjtPAWAQTGl9VhELbH7uCSH2N_Jiu1advtMPDLoqLjKzrT1609oRfgPRHCsQnWDEAeUZSoVKChZbaZv3YuZ8i-y5_PI0QTqd5bdfrGeD6IkkgLozijtAKItYm-3yS8QeN3hrVWWdXJ9Ux_rc0IEn7DHbC8me06i7akOn28TmLbQZaZSP721sv2mNNeFcmLZx79m0WKRU_DSmq937S9hCRPXleaxaP0P0sT3e-zHb1rgawnm8u5GLBNaTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن در ضاحیه بیروت در پی قهرمانی اسپانیا و شکست آرژانتین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/673229" target="_blank">📅 02:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673228">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3bc53ff5.mp4?token=WLMCR776wHEusVC5ZAzlc0No_5j__pMkyBBAAFxBViBJ4K-Z-HWduIanqTcZYuYUgGFtrIPJOEn0dqUX_FLfYlr3L0uSrG02cb5k3Vlwc_apRhLx-Q2YgtdexgXOTxnbn7EcbNAL0J2vGV6R3s-tkZTZrcgvTOp7hEIMcM1BNIhw0Cm30hdrpatvwwB1lHe4s2qBj_Egk3LMWJl-WOH9gu3rECoowKe0hlKCfZ12kKO1DN5QufzPr_bM1Ktt2fjC26i-W3zlECYMPXiJpXRCPSbs99ciBUex2vAHLsQJdf4MBJqnFEH-ywD3uywDnfwM4lXwWZshSH4FX3uZ5Q9uzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3bc53ff5.mp4?token=WLMCR776wHEusVC5ZAzlc0No_5j__pMkyBBAAFxBViBJ4K-Z-HWduIanqTcZYuYUgGFtrIPJOEn0dqUX_FLfYlr3L0uSrG02cb5k3Vlwc_apRhLx-Q2YgtdexgXOTxnbn7EcbNAL0J2vGV6R3s-tkZTZrcgvTOp7hEIMcM1BNIhw0Cm30hdrpatvwwB1lHe4s2qBj_Egk3LMWJl-WOH9gu3rECoowKe0hlKCfZ12kKO1DN5QufzPr_bM1Ktt2fjC26i-W3zlECYMPXiJpXRCPSbs99ciBUex2vAHLsQJdf4MBJqnFEH-ywD3uywDnfwM4lXwWZshSH4FX3uZ5Q9uzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غزه درطول جام جهانی طرفدار اسپانیا بود ، همان طور که اسپانیا حامی فلسطین بود و معترض سرسخت به جنایات اسراییل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/673228" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673226">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
واکنش حماس به قهرمانی اسپانیا
باسم نعيم عضو دفتر سیاسی جنبش حماس:
🔹
ما پیروزی شایسته اسپانیا در جام جهانی فوتبال را تبریک می‌گوییم، این شادی را به فلسطین و حامیان آن هم تبریک می‌گوییم. «حتی اگر تنها فایده این پیروزی، آزار صهیونیست‌ها و همدستانشان باشد، همین کافی است.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/673226" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjDJZWxeqsqr6qTSdXAtk3MNifjIjc0nxoLEvXrUsLe4eYbQb8yUhQ0vl-BrlFKj16Q051gVUr4p4lUJuBw1ecQhedOnOi3tyixBtdnBVuHrGEcldoPbdNy81-uCs32OjKSMBtqKSbNgsAwB949UQmdV1F_aoKlPd4iaQ2xFfSYvpjO-FYiflE5ydvjVVmrmF-nBs9Q8Xy6TvboqyuaqvECQXYZTTfJWHrNrK7IlCCW_xYD-3t3wjUFEQ0sPeP6jikZhmdyB-udSjRClY3Pj9Iow9W1RgMx4gPYFTN4Rwh1SL_RFbXTEUezPUYH41gXUR_rbGeR4QDYNaQ91TpE7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
طرح علاء اللقطه هنرمند فلسطینی به مناسبت قهرمانی تیم فوتبال اسپانیا در جام جهانی
۲٠۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/673225" target="_blank">📅 02:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اخبار اولیه برخی منابع، از هدف قرار گرفتن گروهی از تروریست‌های آمریکایی با حملۀ موشکی حکایت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/673224" target="_blank">📅 02:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673223">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1QIkqWdTBgkFTr-D50BG4ykEe1ujPrJfiLWhwBuhhbP-4btHS-a782kDAOOU33yB43X5ImPPm4TKjqncUZHQaG5pDxbtXNq2biEfwpE0UVsMsRjoKpSJ12nYa3HKXc6Ba1TBYR73l6R1A1PQi1bREXdaCIxeh8tAw5GUZKbA3HmsppM-UIjXPuvwUfmTKuImK5_nqPqW2q_Hsm2cTluCu073HSc_OFuV1ie8VcPphjq3CBdkTMZ-4U8hP6Pat8XZo2G3wE1NqbXHhwxrCy0-QOjnjlGEclMH4ptjt8s4KF2uJUbD3CT7x3lrle4gKACdMsIH8-lLeH4jWB0BQVAmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کیلیان امباپه با ١٠ گل
،
کفش طلای جام جهانی ۲۰۲۶ رو به دست آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/673223" target="_blank">📅 02:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673222">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارها این بار در سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/673222" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673221">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
منابع خبری: انفجارهایی پایگاه‌های اشغالگران آمریکایی در بحرین را به لرزه درآورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/673221" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673220">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702f41e938.mp4?token=LiLnHioXbC5n8o2_UcTDznADbppioLVSzT-_Y8WSHW01AI6rPTpOlR3zi04Fais_YHYroHX395m6GskIVtyx0K8YvFH3K2waL9Nel1AVVHAPPl5fChLVfdIUy_iM2edLszEJy9PV70HfzW1pANtsd-qxEWSnfP2432Ne_63Z3xsPG8XtKPD7xhwoNJbgVeE1lHfVuVDaY7Pl9X69lofGZnyvB96I5b2fEGtzF-nFr2Wo0kw4RZylwyy0kHTaUcylvl1qw9D0-M_9pxoQ7Idg9QkPZoPGX_KqrGRPt0Pnxl2GEJqHS9F7ydNstJdHIBSogYlEtO1i0-AVbkX2hGlxmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702f41e938.mp4?token=LiLnHioXbC5n8o2_UcTDznADbppioLVSzT-_Y8WSHW01AI6rPTpOlR3zi04Fais_YHYroHX395m6GskIVtyx0K8YvFH3K2waL9Nel1AVVHAPPl5fChLVfdIUy_iM2edLszEJy9PV70HfzW1pANtsd-qxEWSnfP2432Ne_63Z3xsPG8XtKPD7xhwoNJbgVeE1lHfVuVDaY7Pl9X69lofGZnyvB96I5b2fEGtzF-nFr2Wo0kw4RZylwyy0kHTaUcylvl1qw9D0-M_9pxoQ7Idg9QkPZoPGX_KqrGRPt0Pnxl2GEJqHS9F7ydNstJdHIBSogYlEtO1i0-AVbkX2hGlxmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه بالا بردن جام قهرمانی توسط رودری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/673220" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673219">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3323f025d2.mp4?token=Zc01yGzMD4hlqplgMJRRlh6aY-zA_r8m5gIcEBhyrxoqCGOojG4Ote7y-0GsBrJ3_TkSn7HBzAMSPjd0N5U05ur2ZjeH_K-egmCk1MrQKlIO4UcJ6GkpcLZ2obj6rpLmzMHO3llqVaMKCL0CnzieOq7cvv0I-I_IY5RI-g2dac4ujNSfXrgxm0ZrW55-5a-Y3TSPIyZy5QAIhAvfNmXsKsW2vLu6K2YtDDTBPhByGfOJQPhYyxM3TyJFJ-fRDX_BMtAG1OF7p-ceLNZhRIGAvptfsRO67yLFz01FHTDFN2WcX1KeV7g6-ELeO57K0DzMzGUlaQcb8Qdj0WNvXV9S6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3323f025d2.mp4?token=Zc01yGzMD4hlqplgMJRRlh6aY-zA_r8m5gIcEBhyrxoqCGOojG4Ote7y-0GsBrJ3_TkSn7HBzAMSPjd0N5U05ur2ZjeH_K-egmCk1MrQKlIO4UcJ6GkpcLZ2obj6rpLmzMHO3llqVaMKCL0CnzieOq7cvv0I-I_IY5RI-g2dac4ujNSfXrgxm0ZrW55-5a-Y3TSPIyZy5QAIhAvfNmXsKsW2vLu6K2YtDDTBPhByGfOJQPhYyxM3TyJFJ-fRDX_BMtAG1OF7p-ceLNZhRIGAvptfsRO67yLFz01FHTDFN2WcX1KeV7g6-ELeO57K0DzMzGUlaQcb8Qdj0WNvXV9S6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اعضای تیم ملی اسپانیا مدال طلای جام جهانی را دریافت کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/673219" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673218">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe7c33843.mp4?token=amhhQ7WD-8s7Zz8L0_bB6C4Vnxc-CFttw54SnVt9RaJ5yrp4SXYbp7SHtrIimmqH2xEzkXfLDUwTsjR1Fe8VqXyqBrqblbDX9rFMENOR8REZmkNxbB1Yz5ZWpUoYDLkMCLKBJ7cADLJOz_zoN1lopSucd8lWsrlmXgpg14YnjetFG2my8R1ZuqZBDVMgFUAdbAn4XlApNFZGgIzPilhk2WIt2klF9yCxyd4gaQQzi1Y-p9H5ZG1vw_dT05booKp7rdD7JM1fXXx5TmAnkxgtI-ijhC2GSpxGdFtlMInQHMg109Ff4AjUmuWkJk0h9SMcVol9IkE5cevFAO-qD7WW6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe7c33843.mp4?token=amhhQ7WD-8s7Zz8L0_bB6C4Vnxc-CFttw54SnVt9RaJ5yrp4SXYbp7SHtrIimmqH2xEzkXfLDUwTsjR1Fe8VqXyqBrqblbDX9rFMENOR8REZmkNxbB1Yz5ZWpUoYDLkMCLKBJ7cADLJOz_zoN1lopSucd8lWsrlmXgpg14YnjetFG2my8R1ZuqZBDVMgFUAdbAn4XlApNFZGgIzPilhk2WIt2klF9yCxyd4gaQQzi1Y-p9H5ZG1vw_dT05booKp7rdD7JM1fXXx5TmAnkxgtI-ijhC2GSpxGdFtlMInQHMg109Ff4AjUmuWkJk0h9SMcVol9IkE5cevFAO-qD7WW6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رودری بهترین بازیکن جام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/673218" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673217">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc20bd9e05.mp4?token=b9rbSx-HKNzBBe1Cn4UNquG0mdEY6nXp4qcsa_Y-aitu6yTsXpDPb2yXCMxq1odBRDqO1Rm0iIDiwcPE3_qyKCYApw2MK-9ChYMfxUGG0lPJHGF-s-xJEXgDqxAeQ6wPrVPeHsvrwjDerUEX7KZZZqOGEIPgJHX7Mtohxf1dYymHQ3_vvXnMlaIePnagNgxTKGLAQUdbGSnDcWh437AKI9VqUOxljFQERlP-MYiCeaT3X8UhHX3C_PRIioNkEfw-DSNAO8xGucxWKM-V3UpI7i5CigBBCW-71RkUtSuAYQHHF1CBVHRgt440Syso55FNiQKlv5dwgxyB5KPvU4JFJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc20bd9e05.mp4?token=b9rbSx-HKNzBBe1Cn4UNquG0mdEY6nXp4qcsa_Y-aitu6yTsXpDPb2yXCMxq1odBRDqO1Rm0iIDiwcPE3_qyKCYApw2MK-9ChYMfxUGG0lPJHGF-s-xJEXgDqxAeQ6wPrVPeHsvrwjDerUEX7KZZZqOGEIPgJHX7Mtohxf1dYymHQ3_vvXnMlaIePnagNgxTKGLAQUdbGSnDcWh437AKI9VqUOxljFQERlP-MYiCeaT3X8UhHX3C_PRIioNkEfw-DSNAO8xGucxWKM-V3UpI7i5CigBBCW-71RkUtSuAYQHHF1CBVHRgt440Syso55FNiQKlv5dwgxyB5KPvU4JFJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مسی مدال نقره جام جهانی ۲٠۲۶ را گرفت و گریه کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/673217" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673215">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caeeP_BM-5sZ3ztxsYI2uGG0chWcdl9FwG9MPNQr6INF5nGtFUUAmSHIMECHmF4aWma5u8l5BpHK9cirQBGk4Dq_2UpLvOizyo_5-XyapTLA-ygelU6PHHDdHVV3YXjyRZ7vhjcSjdrUKFyIWFYkVgqF0uhsVdsQyTYp1FXmCZOp4B5ozldMIWVydH0UmW8Fuo6EGLYmWjCfU7CJp4LAPx5JBX8bT5zJFcc141vzO5lAelEMNbNvcR_0g7R269NIY4JnqlS0c4sPbtK2LpeV4WyWF-K9df6dOSSgzKIAKOB8Szhhv4wXPwL_xEHKuKIuSwLKEm7lO-WXJmYVeqEOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سیمون بهترین دروازه‌بان جام جهانی شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/673215" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmPSnDVifFKcYRNT2sMSAjkJ7bJaCEx1RcazPGKb1TaOGIrCLpv4DrIoPNVtrCFpKOp552yEj21mPNCDTkyctZPhIMS69hREyMfTSjUSn1Wlp8loJl61SfHwCfd7CWsZ2aXGhvJr9-MLLi28caG3Rf2gx32V7EYh7XMU_s4IBpglsNcibrtg4ormKtSJO5Vd38Aa7EKMBGvIO14MsC64eBBDnw0oPgMeqcHDSq1_ViE1mrn2Yjmvjv17T0xmRUSSr4jcC1bH1jaIqc8HD85UIvePBvKY-iCx54zuEW3soe8wNtVPvUQICtQh20FLwWFOyKWrlkD1ZYMSXWNEG9yong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کوبارسی بهترین بازیکن جوان جام جهانی شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/673214" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673213">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در قصاص خون سربازان شهید ایرانشهر
🔹
سپاه پاسدران انقلاب اسلامی در نوزدهمین اطلاعیه خود از حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهرخبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/673213" target="_blank">📅 02:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673212">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=Yf6MvUTUWcNUT3aYpB7wGK2D2imqCCr40OLdwCXSlsFjGbP1KVkctRy-8bLM2Lfu2uBoUtP5s4up0j3jbfxQp_gUjbVyNcbNYOYTxCmssgcil7taU50JeOjGT91E8Q-Q4ze30XCSprlF8g-WnUsI4Jq7Mr3xp2xY9YmtCm1mq1TQE8fFjQjKEyKnsFoioemqKcjEUXeKorcyXDU4TvynMZG4G8k5nhqKEJ5_JKYk8bLEso2tOBR4UWbIg-uIoSvBBEGrivrad9Do_jDZ-vsU76bYVRT6a-GURhJeM-o3UlozDnev7HF3-VeJ-aj7Bz3TcZ5fDR89l7WqAi4eR9BE3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=Yf6MvUTUWcNUT3aYpB7wGK2D2imqCCr40OLdwCXSlsFjGbP1KVkctRy-8bLM2Lfu2uBoUtP5s4up0j3jbfxQp_gUjbVyNcbNYOYTxCmssgcil7taU50JeOjGT91E8Q-Q4ze30XCSprlF8g-WnUsI4Jq7Mr3xp2xY9YmtCm1mq1TQE8fFjQjKEyKnsFoioemqKcjEUXeKorcyXDU4TvynMZG4G8k5nhqKEJ5_JKYk8bLEso2tOBR4UWbIg-uIoSvBBEGrivrad9Do_jDZ-vsU76bYVRT6a-GURhJeM-o3UlozDnev7HF3-VeJ-aj7Bz3TcZ5fDR89l7WqAi4eR9BE3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک هار به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/673212" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673211">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNecl-YMdpE6D0M_2kZ74U9M6HksQHzSEV0XxPut6BKlScG8I9yxxAkowENlMgHo-nOvFUR3PeFSCBxrbuDja5ai20JnAVEZ065Sn6Xd619R5l9I7P3ZsTZ_GsUYBw6Wc8j8yBt2d2wBE8OP9wBm4QInieT_jvr-6BNZXrwSM64Ko2XYX6UcvLP-4Gfts9lYWDUVLCnBWhD-2LADe72FZpF-61s4j2lj-akoG9SpF87ss-yG3OZdsvf9oeUpb1Ia8Vz2MV4TZ-aM1ZFQ7MyX2A6HEJqZSjXqFcR_r2UqQJqgRIIN0qJXSLrh_fe5iMVuOwqO3hnatsFed0TenF5BJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا به جمع دو ستاره‌ها پیوست
🔹
با پیروزی ۱ بر ۰ مقابل آرژانتین در فینال، اسپانیا برای دومین بار در تاریخ خود قهرمان جام جهانی شد و پس از قهرمانی سال ۲۰۱۰، دومین ستاره را بر پیراهن خود نشاند.
🔹
پس از این قهرمانی، جدول پرافتخارترین تیم‌های تاریخ جام جهانی به این شکل است:
برزیل: ۵ قهرمانی
ایتالیا: ۴ قهرمانی
آلمان: ۴ قهرمانی
آرژانتین: ۳ قهرمانی
اسپانیا: ۲ قهرمانی
اروگوئه: ۲ قهرمانی
فرانسه: ۲ قهرمانی
انگلستان: ۱ قهرمانی
🔹
این قهرمانی، اسپانیا را در کنار اروگوئه و فرانسه به جمع تیم‌های دو قهرمانی جام جهانی رساند و فاصله این تیم با آرژانتین را به یک عنوان کاهش داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/673211" target="_blank">📅 02:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673210">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
برخی منابع از شنیده‌شدن صدای انفجارهایی در کویت خبر می‌دهند
🔹
وزارت کشور بحرین: آژیرهای هشدار در سراسر کشور فعال شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/673210" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673209">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3VBEQ5IxkLsa-3GbieF5DnppMig5JKPt7-reSXcVtT4CikgoHETgiN1wi-cae9AkHkPydsJrIOwA-AFu5PFu2MsowWGSg332l4BiXfxCmQRAP67nWBqA6KkJpiM6i3ejNJu1xIyoPmtF1wa2wCf0sZkwJ6sSFuXwLnFW98z1Vj8sbZ_Z8iKwnkVwSHV1BuJbiPQxijW7-8pJr-cDMhpt_mI-ed6L-xC4duoQLWzGOfdvFYtIcXMMj2GJPSVnatYM1axX86M_XgI5VcvCTdzZ2EoRI6u440BNeG5TFI8iEMH-srW6oDvUwGXrL1SZyLpcwuqTstrwkmN6L_DbgxTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به بالای ۹۰ دلار رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/673209" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673208">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ارتش تروریست آمریکا همچنان مدعی تعرض به کشتی‌ها
سازمان تروریستی ستاد فرماندهی مرکزی ایالات متحده مدعی شد:
🔹
نیروهای ما به اجرای محاصره دریایی اعمال شده علیه ایران ادامه می‌دهند.
🔹
ما مسیر ۶ کشتی را تغییر دادیم و یک کشتی را تا ۱۹ ژوئیه غیرفعال کردیم تا از رعایت کامل محاصره اطمینان حاصل کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/673208" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcebb879a.mp4?token=B0_JDSdQwxDODUZ4Z6M4IzUjNUZMtCafiQEoMVT-hHCkug-QrKVxP_Xsmy_f4nWl2t1GXha5ORgd8_qg9YvgivDURTcvlgQGpLQb81enNkw2xeAp85DobH707JWJPOGDWqLIgDpBmgUeMbNeUq69WlUIGpBKh-r6g-WSg1VNGz4lbuHVwjTsoTDpfxGbaZvvd20nITIimobvlqB4yc17DtvZCBaaLDmjuDRi7pvdR237OI0u6FbLaViC45Jyd7LRnrezxcJchYzx9KcDJ6JvE36Uxwsle9LQdPFkwsUROkwDndcX7hLGy_VAxJkj-4nO7PNfhiUFDtrsXVfwbHTZ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcebb879a.mp4?token=B0_JDSdQwxDODUZ4Z6M4IzUjNUZMtCafiQEoMVT-hHCkug-QrKVxP_Xsmy_f4nWl2t1GXha5ORgd8_qg9YvgivDURTcvlgQGpLQb81enNkw2xeAp85DobH707JWJPOGDWqLIgDpBmgUeMbNeUq69WlUIGpBKh-r6g-WSg1VNGz4lbuHVwjTsoTDpfxGbaZvvd20nITIimobvlqB4yc17DtvZCBaaLDmjuDRi7pvdR237OI0u6FbLaViC45Jyd7LRnrezxcJchYzx9KcDJ6JvE36Uxwsle9LQdPFkwsUROkwDndcX7hLGy_VAxJkj-4nO7PNfhiUFDtrsXVfwbHTZ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دست در دست هم، با مهر، خرد و غیرت از ایران پاسداری می‌کنیم؛ ایران تنها یک سرزمین نیست، سرنوشت مشترک همه ماست #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/673206" target="_blank">📅 01:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673205">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaYdBPCrmzZ8f9TM3tvfHqmhk4edMhr1Ny5gQ_u7ItGkvGzt0umDo5U7tKdw4-qOCM5b8pxubKlvLnQWLsGlJBeP4bvukn1_4cjpLp8Yuna71QaXzPgwy9r8BQzKT51RNRFicS3eg_ssFI7D-SKv6xX1cYpD3f9QYO0JPGnbkhYbbEb9AGnOGUELLtx6leiEoKRGZCzNQyFZzjQXawrp4YDPf8U14XapJ6VH82el6Xjzw3-Yb8w_Z82zA1MHihtWSDV8K6ytU5aJDZpA4CVXzBd02J9jjVOwpeMUuOZCAS4JLFebfY9pCC5ve_WU25jnYriUhPgZaP9_gJhcdqNBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لامین یامال و نسل جدید اسپانیا نقش مهمی در قهرمانی داشتند و پس از پایان بازی، تصویری از در آغوش گرفتن مسی و یامال منتشر شد که مورد توجه رسانه‌ها قرار گرفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/673205" target="_blank">📅 01:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
برخی منابع از شنیده‌شدن صدای انفجارهایی در کویت خبر می‌دهند
🔹
وزارت کشور بحرین: آژیرهای هشدار در سراسر کشور فعال شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/673204" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_sSrmpb8MkpKwkGQoEIfpVBI3uGrD8kd8eLNhay_yg8gjWcK_aOWRfVaTEheGJgjwZfj0rA4mRoGBzzwrxKBHT9K6ySqPqivrH-BCqsGY6WWS5Roj_A5arwg_X-__4QOPHd471azSdDY7B6riO6-fKEXMuu74DktYzpbfsgM3av2GO9NIeJ62eeWaPaT1UsNuPYX1_i9GKX9dDAysHCu7keEBYvlhM7Jws9sdqJCzrfSenctWtjX7zrMJSGSGKxNm5yanNdgwZBVfB6kE3K3n1TN4loGgTusSkuGYpTjOBeTidh0IKWNJZgLGgsfr7op_1Ec0wPN9ZPSeYl5WNyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران قهرمانی در جام جهانی؛ اسپانیا به جمع فرانسه و اروگوئه ۲ ستاره ملحق شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/673203" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673202">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF6a1UvOhZKHwole1NGinpTKXF1rbKxor8dZOS9XRCNDj683VU0r8H1GUqWAVBSpDv8eo_7qqkWQpKIpq-14qNIEutZP-x8ShY9Rt8Oid8vw0P54WsVpH9JHvo1RwJYAIXO-7SskvlivKPDLK6QNHx5aO5xrW5IWwnE44Qx08zXmuEcd8CV8ZuFIiUswqHp-qmoNW7h4UlyczbROHlbvpP-FgZYFUfLV9MTJf-UNXzo1JY97cmFsv2IQI3w3xDrs8gZegad4iGcc49Ao7yM836pgqWOa7AH_I71OkG1M1PIqqPdERqcjL6_V7Wy3hpKVMD5FB08kBThCr6yEKyPQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲٠۲۶ هم با همه خنده‌ها و گریه‌ها تموم شد
🇪🇸
قهرمان: اسپانیا
🇦🇷
نایب قهرمان: آرژانتین
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقام سومی: انگلیس
🇫🇷
آقای گل: امباپه
🇫🇷
آقای پاس‌گل: اولیسه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/673202" target="_blank">📅 01:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673201">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXQudn77JdUEVpjbQZLUr64b1LCIzfAxQDe22_JDrRvQz6A8HiUJtPjqZpZ0-_73V2Kc7vLl69q6lysuzp-LWUxAi2bXJPIc4UVZw9v6xuxFYrAtTYMrwTYrItIDy4KqUtp8jHjFnL7OFnzKJhRyJppYAyesBXJY6bdo3x-LgskzxH2G7Ijt_Q_l98ZrAhL2MPT7Mek40kPlylb7_Acz8GcqgrFWfDbU1--WkE3Itk_XJ1y1cKCBJ9HPoCPrlbkVg1Vslpaqz_l0qG2kaefnsxUtL_B3_2mG8TJkjbu0aP8LQCVrYxM_GZ_jjkS3n9oy9LOsIosohIyqzIua6_MtOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا برای قهرمانی اسپانیا در جام جهانی ۲
٠۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/673201" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673200">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWSyhKc5qjDafQrBeEGsSL2droSrPX4O1Mdgy2Wwzo1bMjl7TQriOnBaRSpYrcyZxp5O_glBM61cJlM8WTPmoYHLaHHHb8a6eR2VlexQ3TW0j_-bGFV5tJp0SrVe-T_N0gWgJCAfovSYsi5kJnrHpS61eTABDlRA_12Pxxi5ibIsltafi71eLnbkDv1ma9Ksp3VPAcl6iARs11gbHWDWepummYUr1cGK8wLwUHhFYeNgdDaCpKImK-rLK0dxtJ3Tmp8TptxCPIC1fODAlJ4FW3dQDysGhWMHcu1AGi1tIZ9M2rul9nuKMzNgthbISFVlSCDEJPREFC44Dmuq4hmCPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ماتادورها قهرمان جام‌جهانی ۲۰۲۶ شدند
اسپانیا با شایستگی برای دومین‌بار قهرمان جام جهانی شد
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/673200" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5911d00df6.mp4?token=ZV46WbXrB0SqPVdGuTtjbLJ--YQkPcy1lPv3HWquden6cQpITnvHfG1I2Rz1_6G70-XUquzlaWwcc1WbC0D0gzn8f4YECvcZ1AKoa9uGx84NYf6PwLO4xDyRMxwZYHYMq09Sz3rBF0bcYkaN-nh1-OAWcf2dSf-Ui-rhNbUX1urp2peHGhpmG04rIVVgwUWHJvycZCcsDnlaUyxzywfV528NqZ-BvxOam6v4u3oQPDnp8O4HwF9ONfQZ9avjDbLBPZolzWoFbY4dTUAe7wAXBwoIvbXdtd7QBKUFQuR-BnzDUfGwYvGRRcLewcb5WT7xQIcAJWMf54TSoX0oKe3fUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5911d00df6.mp4?token=ZV46WbXrB0SqPVdGuTtjbLJ--YQkPcy1lPv3HWquden6cQpITnvHfG1I2Rz1_6G70-XUquzlaWwcc1WbC0D0gzn8f4YECvcZ1AKoa9uGx84NYf6PwLO4xDyRMxwZYHYMq09Sz3rBF0bcYkaN-nh1-OAWcf2dSf-Ui-rhNbUX1urp2peHGhpmG04rIVVgwUWHJvycZCcsDnlaUyxzywfV528NqZ-BvxOam6v4u3oQPDnp8O4HwF9ONfQZ9avjDbLBPZolzWoFbY4dTUAe7wAXBwoIvbXdtd7QBKUFQuR-BnzDUfGwYvGRRcLewcb5WT7xQIcAJWMf54TSoX0oKe3fUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسرت و افسوس مسی بعد از گل اسپانیا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/673198" target="_blank">📅 01:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab996676b.mp4?token=mQ798ShwerRbLGeUxnBRVhCR2O2Q1cAtejAA8XEWY5CNNO8LGPRWGuOp_-hiWBUTJCcUaYjGS9HmdZU5v54GiHZgI0Y8R0y0_YwzCRePmWaMzDRMTrajRVn1YDrM6WI8jQ4JdIFdA7C6tHRCTN2l05lPFZ3P1ggXDuSPH1OajxYc5Lb-ru50zatiE_PXvLhZCLthfogVG4JIDGipdcz3M_KIsU6kPBQWYgXnaQlJeZXAYCqm2ln6IPRvv96pUocQ5Y8iqBXzqz8dwmDTGXWQL529g8oeyFkHKPF-mLKWdhsmBW662UkFYYFwHWqp9sZQGq4lcikAwnpfLy-ms4IQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab996676b.mp4?token=mQ798ShwerRbLGeUxnBRVhCR2O2Q1cAtejAA8XEWY5CNNO8LGPRWGuOp_-hiWBUTJCcUaYjGS9HmdZU5v54GiHZgI0Y8R0y0_YwzCRePmWaMzDRMTrajRVn1YDrM6WI8jQ4JdIFdA7C6tHRCTN2l05lPFZ3P1ggXDuSPH1OajxYc5Lb-ru50zatiE_PXvLhZCLthfogVG4JIDGipdcz3M_KIsU6kPBQWYgXnaQlJeZXAYCqm2ln6IPRvv96pUocQ5Y8iqBXzqz8dwmDTGXWQL529g8oeyFkHKPF-mLKWdhsmBW662UkFYYFwHWqp9sZQGq4lcikAwnpfLy-ms4IQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول اسپانیا به آرژانتین توسط فران تورس
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/673197" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
منابع عراقی: آژیرهای خطر در کنسولگری آمریکا در اربیل به‌صدا درآمد
/فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/673196" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELZR3rW-QVEY5YxSjhX4Wev10xVccOUlY_2x9SqXFhB4z9V-NmpgCOoGCLNPcGc_XyKBPn6qwo3VFqelpEaNUlPBGb1dK_TihKFMiZinLP4UHmgfQutvKcOtFvbNTIMEiELyLSGMa1wh73_M0xcNFXQSBuOfK0p_TfbBjA1aN5CKvW4sYt_Kq0nwqTmTUz2q8ToONMr08KHMlzX_2XtNmgAXKd_nCxnqWZaVDwEDxrLM6D4gKmPRWCy7qXutE_D5Xw1r9t98DBnOdEQshBwwzDTV9UM_xDVrw3gqUaic3y34nDKKoQeWz8SBsASk-gSteI76Z6Cy5nmanfJeCxO1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یزیدزاده
🔹
بامداد امروز، رژیم جنایتکار آمریکا، تأسیسات آب‌شیرین‌کن بونجی در شهرستان جاسک را مورد هدف حمله قرار داد. این حمله تنها یک زیرساخت را هدف نگرفت، بلکه جریان زندگی در ده‌ها روستا را نشانه رفت. با تخریب ایستگاه پمپاژ و ترانس برق این مجموعه، آب آشامیدنی حدود ۲۰ روستا با جمعیتی نزدیک به ۱۰ هزار نفر قطع شد و ساکنان منطقه با بحران تأمین آب روبه‌رو شدند. در گرمای طاقت‌فرسای تابستان، محروم شدن هزاران نفر از ابتدایی‌ترین نیاز زندگی، ابعاد انسانی این حادثه را پررنگ‌تر کرده است؛ رخدادی که علاوه بر خسارت به زیرساخت‌ها، زندگی روزمره مردم را نیز تحت تأثیر قرار داده است.
🔹
هشتصدوسیزدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/673195" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90474a79f.mp4?token=qX_yzyc1Qbc-bDusWAWfkscVXZE3ZbDm-qI16JwP3BhDnixedSH6JB4h0vikNmBvlfXsS-Ax7zW06r3uz6xPaouEcglkwb95hMVPdYdP11-DxBfFLRVnsNPYveogkcru5EaiCuYc9h_Za9lizZYsq9qOvp3VOGC90HHvrpUxLNPnJFJn_p9_g8sS7mnXZp-9EOFmBPFE6oVFxsvFDsqkxFD5Fft1TsTAXAjGBerfAO5U5n3Xpg17GOqYbH-O1UnzwoMhOWbv6huXnCxbLfLWnFsA6FqVO9m8dhVHLo0Vri1GUdPse32hKMvaKI-Vz29lTg6WqNdxFQPUg9i4138GeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90474a79f.mp4?token=qX_yzyc1Qbc-bDusWAWfkscVXZE3ZbDm-qI16JwP3BhDnixedSH6JB4h0vikNmBvlfXsS-Ax7zW06r3uz6xPaouEcglkwb95hMVPdYdP11-DxBfFLRVnsNPYveogkcru5EaiCuYc9h_Za9lizZYsq9qOvp3VOGC90HHvrpUxLNPnJFJn_p9_g8sS7mnXZp-9EOFmBPFE6oVFxsvFDsqkxFD5Fft1TsTAXAjGBerfAO5U5n3Xpg17GOqYbH-O1UnzwoMhOWbv6huXnCxbLfLWnFsA6FqVO9m8dhVHLo0Vri1GUdPse32hKMvaKI-Vz29lTg6WqNdxFQPUg9i4138GeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول اسپانیا به آرژانتین توسط فران تورس
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/673194" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673190">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nyd9Y1XFRc4l3UGE5LfnjFp_aaSnE5xft1zZ5aETjnC_CW_FWeEcyrVJXqJkE1VFIqLo__7WW8I03qC-HEn8ZtdFMs-L5UM_je0iYPzypKE8GeXpvJaFVIb98KiQM_fKq3o13BpVW1R0bTtlSJncqa_7W8SKaMgWotREdVQm3E_c6IphRXmOwAUS9raUXaz3Qb8UbvHJ2z8JqV61dHVTAAzYF1GWvU3eu5v76-NO4hyROm3mkO-LyMDuNDwi22hO_rqaJ2NxHLxmo7qTlhAPv24EbqCQNK3jKPFVfeqVPZF6K2PCwTyvT6uj11kU0wUn_FkE2lp9rw1Eex8TwKd9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملکرد عجیب آرژانتین در ۹۰ دقیقه فینال جام جهانی ۲۰۲۶
🔹
حتی یک شوت هم به اسپانیا نزدند، حتی یک شوت در خارج چارچوب! هیچ موقعیت گلی هم ایجاد نکردند. هیچ!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/673190" target="_blank">📅 01:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673189">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802f158a8c.mp4?token=HNmk3ZOuh2mbAOzBjvjIthQD6kxDiFpOLufHKTwMEH0lJMGD2FxlduUAkNhowBC_zPP4JjUsI0KGifJ5jwDrWH8_8IMAfTeH5RGdyhfPMYFBcRaLcquQKtWzAUcesAXzxP28Z5c1LFHuwBsVmu5VQ_44XNqh8dXzwxtU8pp6FQJCIOk5qzrKW9V1xoV9WJQGfktEP5giLdVAp9lDAjOWfOyi6Vb8t-LD3evH3yXnAFOstM6VGJt81S6fNjMGevsk1GKa4rGbf1JA4W-KyN2uygi7vmlXbFu4V9bb6yzaFtBLq_1Ej8TfDig6flI8XHw0ppW3Rn-q25JpZzcCmyLjyk7lihpwGzXSCwMC937_mva6k6bY7IeFkyQP5zI2mXdTQctDY2799xKwNykI8xqMr0sAzkuZq_94UuJC_7wqoOIaGHjgoM4UUVjPN-4_aVzmdLDeYyXrXoj_ketoVNjhE-EcXl2YzvaZprHVaWna77JPLzNj4phfEQGBdx5BQIBUaxOArd7-Clafr_EaAZAjmCM__2vRw1U2Ykc_OuORb-gVpkYVzEPXfnCCb_56rlCRpInG7iIVeEyFhvQiWpaHROefUDhWRPcupqohx6Pd0JHcpDZtv_nVGZrn33PeEucJFbl5EACDSiOceLPP8-v6ek4Zmp28HaJpJTFD6PCFeu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802f158a8c.mp4?token=HNmk3ZOuh2mbAOzBjvjIthQD6kxDiFpOLufHKTwMEH0lJMGD2FxlduUAkNhowBC_zPP4JjUsI0KGifJ5jwDrWH8_8IMAfTeH5RGdyhfPMYFBcRaLcquQKtWzAUcesAXzxP28Z5c1LFHuwBsVmu5VQ_44XNqh8dXzwxtU8pp6FQJCIOk5qzrKW9V1xoV9WJQGfktEP5giLdVAp9lDAjOWfOyi6Vb8t-LD3evH3yXnAFOstM6VGJt81S6fNjMGevsk1GKa4rGbf1JA4W-KyN2uygi7vmlXbFu4V9bb6yzaFtBLq_1Ej8TfDig6flI8XHw0ppW3Rn-q25JpZzcCmyLjyk7lihpwGzXSCwMC937_mva6k6bY7IeFkyQP5zI2mXdTQctDY2799xKwNykI8xqMr0sAzkuZq_94UuJC_7wqoOIaGHjgoM4UUVjPN-4_aVzmdLDeYyXrXoj_ketoVNjhE-EcXl2YzvaZprHVaWna77JPLzNj4phfEQGBdx5BQIBUaxOArd7-Clafr_EaAZAjmCM__2vRw1U2Ykc_OuORb-gVpkYVzEPXfnCCb_56rlCRpInG7iIVeEyFhvQiWpaHROefUDhWRPcupqohx6Pd0JHcpDZtv_nVGZrn33PeEucJFbl5EACDSiOceLPP8-v6ek4Zmp28HaJpJTFD6PCFeu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به آرژانتین توسط ویلیامز که مردود شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/673189" target="_blank">📅 01:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673186">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fg9_EzhOd00HXaSpfLXMsMflhUicgPxLKeZJW-hjkUVdmyyHszBKcWZDKlOftqT9FCDjdO02Mriyl3cq1Xlu_Cc6hawSETBjEP_PH2MdDHV9ab_rYmlNl0AXY-Uj3iGHeyg9D8mx7XtHOiJTWBXJBhhJ7CvmDhyx-E8raqBHG2vqYV8sGguCV87XFbd6GgT1ZKY9zUo610t0RExe6XyVVB-taVuLrKMvlw9D1De0eShDU0xcFvrZtNZyW-_OQ-kxQQKvjhaQY-XV7cc7Sfwz0vhKzzLHW4c_kzDypmSl3Nvx8bQvNV1kZXmMscWj6g-7__s1m5m1GI-4j9e1A4qAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2oRNEymNCr60BnCy5AP_3_wa5nmJFkiI1frknjV2tbxLRhutc_9WJl96U98hqG027WOb62euJIvLQ84dU1K_ZWBkr-MHmFRv1Mi7NOg2gvOsqcwSQamSwKnkqwCtM3hAihZcq3gnRUijlX34yRcne0RKyjDhPIQQIlukrSRVY3bCk5QNtxM0xsEgBcju9dpj94gURGunNVd_GB0Dr_QGdEgZc10ZdzOsSKLAXEpjuYCTUvpsMD7yYoDHSAC7_3rpj5deI8Opp9dFrifIDa_wM4EPbxsfnezl1HICEW4ILMxCb5cYgq0Jalb_brF5sipgWenEDE9atDtbBBByz0JyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88f1b708c.mp4?token=caDvJMtcO27Kbn-cHiLcSMCDDhB9dIb41ir-yp-NeCwAKepxk55scQSg3bDfg-f1yLVjrxz3TZWjFtREWC4j5vpDQ3nnVtoxy0PcrlOMIpyJo4q-G1Wo63GeDpRXspr_HRuV6DiEZykHUSciGEx0yC5maM1bZcCDgPWGZnzDmp8woi8Y_5hDoplSRrAM_FKi711bshpgnGibR5UhHLZSfgo0UYvTPFLYxB3n7a7uxdIKsn3oemLOPhkZedUyB3j3C1_YIES4utI94NjhSCQsT3RJzVC3yIPxNnFE0XxbBmyckwWh4NTb86DhElu7173SpNPVcHfiAAYL-lHLdwGnkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88f1b708c.mp4?token=caDvJMtcO27Kbn-cHiLcSMCDDhB9dIb41ir-yp-NeCwAKepxk55scQSg3bDfg-f1yLVjrxz3TZWjFtREWC4j5vpDQ3nnVtoxy0PcrlOMIpyJo4q-G1Wo63GeDpRXspr_HRuV6DiEZykHUSciGEx0yC5maM1bZcCDgPWGZnzDmp8woi8Y_5hDoplSRrAM_FKi711bshpgnGibR5UhHLZSfgo0UYvTPFLYxB3n7a7uxdIKsn3oemLOPhkZedUyB3j3C1_YIES4utI94NjhSCQsT3RJzVC3yIPxNnFE0XxbBmyckwWh4NTb86DhElu7173SpNPVcHfiAAYL-lHLdwGnkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری دیگر از خوک زرد در قفس شیشه‌ای
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/673186" target="_blank">📅 01:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673183">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-VkHbCSQs1EdgkH_fS2kRcFLmnuogD70W1osFczHkz5YxxpSVrWV-aeeSEucc7cHhQJrZzHn4MIdUk3S51e8iEed7dclVGQfXVwpZmgh94CAr0IaB4jR7KVU-NuUpklYx691LjrDPJpzFh4ZFB_DlQF1RSddaso5TNYNmdLjwKKXaKntX9tAZUpr--Wry_UDEjxon3tei4OYQNcZ_Yb1sZO2wCrGjNn0F61FLrVy_oRg1xp5YOm7IOA2GcRTccF2NGmI2Nv4fcMlHjPdHVJLOnBxXebJRP4tbpyjSgz_mr9ClHnw9Wq2vM-nCeqRrAJpyEDzw5Z_KpdE14iRaIs3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انزو اخراج شد/ آرژانتین ده نفره شد
🤩
🤩
🤩
🤩
🤩
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/673183" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673181">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwzBD1OYm1nAkWpf_Cok-OHF7VG2-q3C4T4w-N59jEng8JbH7aXIShUFYkkEzv0xB1oh7hZEBXJ4lBwV5blT1xtpAn-BbHJAr9UN31jT-NK1D5Qz84KvhMh-vbcRxr8-8DaeT5i1gjvGdOkuZnf3e4NZVLxZOAHhUUM6y2UJomhutkQFaqe4rxk1YedtZngPyxSGq1Ik9sBO2yx2fUcTiKiId52nzghilB4rIMod0Uz4YsyH2-ePhBbDPJYrDUQx4AHYZza-_AaoZ1cQIjKC4vBGzE08mDu9DmilHEAINBy9fwr7wgKfMljiyEqE7q8Of40vWCRBhCbn6WJrqldlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انزو اخراج شد/ آرژانتین ده نفره شد
🤩
🤩
🤩
🤩
🤩
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/673181" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673179">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
شلیک موشک از نقاط مختلف کشور به سمت اهداف دشمن متخاصم آغاز شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/673179" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673175">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9b75580c.mp4?token=ZTOeT3WZxhrMNuFHofDDsRK4v7aeUTlDMg5xxXrd8fxQ5yRkUlFWuEZU3u0Rkh2g4eh5s9MEzxh-6ZjianNBTcAJrmCstx3a-TKATXXqRmnZzeuEx5nL4SS_GzV8613cWlva1KccTe272Q4rRL1JGpAJ9--4KkTuYCGjui41wCV-W7AWViEmdk77AVSadOB-l6hjUNaPzfrkF6h0A8gOSyRLG_z0X4ONwnG-xpGB6HPS9HN8YOPq3ZFh0rwG4F1MD9YDsqhW6xZyzhKy6rq-sf2i-YNj47jU8h83Mez0rduIATIvVb7p_AcuOG1Wj_ppt_LctK_tm-2N7TQl3D8u7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9b75580c.mp4?token=ZTOeT3WZxhrMNuFHofDDsRK4v7aeUTlDMg5xxXrd8fxQ5yRkUlFWuEZU3u0Rkh2g4eh5s9MEzxh-6ZjianNBTcAJrmCstx3a-TKATXXqRmnZzeuEx5nL4SS_GzV8613cWlva1KccTe272Q4rRL1JGpAJ9--4KkTuYCGjui41wCV-W7AWViEmdk77AVSadOB-l6hjUNaPzfrkF6h0A8gOSyRLG_z0X4ONwnG-xpGB6HPS9HN8YOPq3ZFh0rwG4F1MD9YDsqhW6xZyzhKy6rq-sf2i-YNj47jU8h83Mez0rduIATIvVb7p_AcuOG1Wj_ppt_LctK_tm-2N7TQl3D8u7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
وینچیچ داور مسابقه به طور تصادفی دکمه اسپری‌ خود را در حالیکه بازیکنان اسپانیا پشت او بودند؛ فشار داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/673175" target="_blank">📅 00:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673172">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fn7m8bQIiGyRTF4u1VjcZ_tqITaJjmcQTj1NI0vvqkFwncTM_nlJy2OeM1aFnDqVkf2FzCD_hxLwpDtxixVMPKRheFkwZfj27xltVUEifDmPWxJ1w1rvc2yhDR-Bn9bix38_7IsWCQG89iITlWHTlqYXPDbT4RI3RQFvESICkBieJxRw46JnDxPNghYlHGe6uAor1qtLAPi6bl3tv7pkAZrHwYb06YsW_JW1i-ruz_7aXOzoIMg_VWLg0a7Nip13dwjIxqk9wNaROBBd90v0qERa5cmcRZma0eZsVZKsxJYTpEPrLaGgcKNdpN9pZL8806n7ZZuC2egQeNw7V43eFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_PgHEpLRk_ibJULpfjaHfCZXlCvgXGBdhzQIsrN98FFdIBOdDUHQyFUnvi-4UiUq2ZhYI8gPMQ3Ink7HxhKJridNcRbhPXEULtfAyYHhSUblus47LDhM_bRzIaF4IpJVw1KdjD_CQl25acmkPD-YjyK9Ttpkev2I-gNkdDAlj_mtPFjghVcJYLNr4Dn-TsWAbY-Yqownde0wH4Tavn78pTn5LuPcgqwbRjA8_EmXDJbAWlyJKOTr6NiSd2WFcPGwrgWm33K_E7U9Lp8eBIHJzyrikH-OhD5Rf1G6OwKaZBufNXTE2Yd8ai1lEyJYBOl7boBOrl5LzK7aDYxWsvEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyowF4EMX43PSp3G-bKwS7-FyT45mbp-AHXNHCO3E8P4gw47n7z41HNTqjurYq-sDuPN9FCMaX5pukMT4PBE4n8bdd62qtBRD6TJznkH_VaGAlVsKpAqg6Aq_iYQtNRgfmT-wSXNTchkMMeCVPXMLOnWmBa2rxkeG0jnDZqIfcQ1GOFcf59zYo-QoUaNkvLvwtQt5SXEMCVu_Kuj8vtEynaG21i3OyrUU5gRCbQPe02xqLUFIJCgXB7qjU6oF14Su7IprSSBKPkif2Kj2WXs8MQGk_h8263lwEouwlJvtx5fgh72b9068FgoWVKxFk9-_2hyVtUo5ZdjwjC40AZVQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جایگاه ویژه در استادیوم با مبل و کلاه آفتابی و ویوی فوق‌العاده نزدیکه به زمین
🔹
قیمت: ۱ میلیون یورو ناقابل (تقریبا ۲۰۰ میلیارد تومن)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/673172" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673171">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
واشنگتن‌پست مدعی شد آمریکا برای جنگ گسترده‌تر با ایران آماده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/673171" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673170">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای شدید در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/673170" target="_blank">📅 00:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673169">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaFlzJxElw-5FgC6biVIIB8kdsYTUyekpzv-Z8mh6ywJbkl7mALlqGBEEEdRPNu7pjLS4h0U9HAdB0DweNBcES0CE0jhWRBNc6JjScqYaZvWnu1iiL6tHPXdMzbUvQflhx4BBMB4tIl2JmBQhXVgRFsucKoFCghgg3IbTbO0x9ma7i-CQabOBW13HYs07Yi7wKooMrFZT3rDq3Xer6fJ3twOhOo46-vkHhFwJBPhI-EvdUyNyXwKhxOT_pmjWccCKG_3ZCexmjlsh-jfAD3Wxlb_yEipFU8dlpUoNGd7CrCBPPfUfO98NuKi_Z5gvK5bqLOB1U8i-k7yGgQA0RPR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارقام نجومی برای بلیط فینال
🔹
ارزونترین بلیط فینال: ۹۵۹۶ دلار (۱ میلیارد و ۸۳۵ میلیون تومن)
🔹
گرونترین بلیط فینال: ۴۹۳۸۴ دلار (۹ میلیارد و ۴۴۷ میلیون تومن)
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/673169" target="_blank">📅 00:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673167">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
معاون استاندار مرکزی: صدای انفجار لحظات پیش در اراک مربوط به اقدامات آفندی بوده و جای هیچ نگرانی نیست
#اخبار_مرکزی‌
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/673167" target="_blank">📅 00:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673166">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ac438237.mp4?token=PwKo-MK0NW_TSf-fbqybyTVo_TmSDafEpl-Wc8Vip1HULpgPU2Dy-IN4UkfM0gb1QjcQMp_g4Od9301QC9qvZW3vV7Iv-9RXPKtOKak_9_KcJTueAaYChnI_dWHvehowOhWBxNek_hRWndynlWIerzPyf66b4BkjYm9xv6Naw0Qrs3YXoq36NogMv17EG0Rhionyccy5a-EN_F-GGZoOCYUEJ-6M63H23Lk2OkpYAshGvcFsAy_3jwlueSPaRdRv4odeIJJbT59IhVUIZFQKZhq6w0QrjMY6mP3joEEN3kvWVeVPvwYwYDlqWCaDc70kBA3wRu8KW64r_i4eFl8uJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ac438237.mp4?token=PwKo-MK0NW_TSf-fbqybyTVo_TmSDafEpl-Wc8Vip1HULpgPU2Dy-IN4UkfM0gb1QjcQMp_g4Od9301QC9qvZW3vV7Iv-9RXPKtOKak_9_KcJTueAaYChnI_dWHvehowOhWBxNek_hRWndynlWIerzPyf66b4BkjYm9xv6Naw0Qrs3YXoq36NogMv17EG0Rhionyccy5a-EN_F-GGZoOCYUEJ-6M63H23Lk2OkpYAshGvcFsAy_3jwlueSPaRdRv4odeIJJbT59IhVUIZFQKZhq6w0QrjMY6mP3joEEN3kvWVeVPvwYwYDlqWCaDc70kBA3wRu8KW64r_i4eFl8uJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری عراقچی از ماجرای تماس یکی از کشورهای منطقه و تهدید ایران: ۴ صبح زنگ زد و گفت ساعت ۸ ما شما را می‌زنیم شما هم پاسخ ندهید
🔹
گفتم بزنید ما دیگر پایگاه آمریکایی در کشور شما را نمی‌زنیم خود شما را می‌زنیم
🔹
منطقه باورش نمی‌شد که ما آنها را بزنیم و آنها نتوانند حتی یکبار جواب دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/673166" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673165">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVzizbgYW8jZ4NeJSuIYPf_0H_TKQ8JGQS983SMYe39LHuN9MedcfmMl5jpS-m17eWHB3wZKsjXwAuX0CnVz4JYBpXTTp0vLmBc9OOpX9bO_DA9yEfWZua0C75-A2sKLTpaZhoR1qVymDrPQTC5cu_61v1USyNJQbmczJb2duY49rCrJ6ILg_gaqBity2ksOTm2uQc99gXjLyIRJfJiNaWZP91AUdOBhUNuaf-a-_rElogZSTyn-k8h9QehXgUosmdxe1lXC_C-eex5xgapCi8Mf4nSraueYPyvWQVQbe0J7_dFWd0a1FHFILeqT11aBsBRp4scpZLZAlyzQ34a2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/673165" target="_blank">📅 00:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673164">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a341f37b.mp4?token=su1Oyz5tuqxge2kyqLL5aBOkss_0XupkeBxz8L2Tg-gdzMW8cEcnXAi-LUZWkVec8w_sw9YVGJ64FIe23H96ch5AE2fOF4KuAGoufktpokcWgNQwKDu13U7TMQTOd54glRu7dZYdfFvSZg97Uqu8u92SG1hqHi7YczeVQ2G-VwH2Y7qy2kastnO3LynE_1Ad_DhyW6J9Qe02HXpSHS8Euzg70GVPPgTVW3HoDHtk7oarna1uv4fz5CfvttWfvpiM5pCrl8dDsZwYEZOopfHcitUxb7EHU2eUZ4a7P62n3vK0cLcZitnlYjUFfNR25aYJjY6oOnybw2qE2HtNymV2Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a341f37b.mp4?token=su1Oyz5tuqxge2kyqLL5aBOkss_0XupkeBxz8L2Tg-gdzMW8cEcnXAi-LUZWkVec8w_sw9YVGJ64FIe23H96ch5AE2fOF4KuAGoufktpokcWgNQwKDu13U7TMQTOd54glRu7dZYdfFvSZg97Uqu8u92SG1hqHi7YczeVQ2G-VwH2Y7qy2kastnO3LynE_1Ad_DhyW6J9Qe02HXpSHS8Euzg70GVPPgTVW3HoDHtk7oarna1uv4fz5CfvttWfvpiM5pCrl8dDsZwYEZOopfHcitUxb7EHU2eUZ4a7P62n3vK0cLcZitnlYjUFfNR25aYJjY6oOnybw2qE2HtNymV2Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای بیژن مرتضوی، موسیقی‌دان مازندرانی بین دو نیمه فینال
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/673164" target="_blank">📅 23:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673163">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39ab21c56.mp4?token=ccg--tpKZADsWAdAB3AGjFp_ANT-LcNKWMk0aV9t1OA4RCCTqm0FzqkA--ZEsst9pIbCmpUolc4xpOw4hohZrc3Yr9nKT-WLmj7qKLDSE_6CllukTPfsWC7A2cXMIGaXPtQzpgL5rVXGk_fXjBtSpueeBCTKGUr2DU0SYWuROfkALR7xbQ-1rcrlyNSDQ-0ydR7eloikmTw7RIQS63Y2Z7yG6lZSFOu0FI3WYG7cQ4jWI5o8Ce4IskCFjiHLyclucyAOuxXjdHKt5n461bfNjso_nlh0C0r30OSuBfwYr9E0tre6Xkqn66T6AOsamOPt6-jzs5wK4c7mDzc2ZZSD4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39ab21c56.mp4?token=ccg--tpKZADsWAdAB3AGjFp_ANT-LcNKWMk0aV9t1OA4RCCTqm0FzqkA--ZEsst9pIbCmpUolc4xpOw4hohZrc3Yr9nKT-WLmj7qKLDSE_6CllukTPfsWC7A2cXMIGaXPtQzpgL5rVXGk_fXjBtSpueeBCTKGUr2DU0SYWuROfkALR7xbQ-1rcrlyNSDQ-0ydR7eloikmTw7RIQS63Y2Z7yG6lZSFOu0FI3WYG7cQ4jWI5o8Ce4IskCFjiHLyclucyAOuxXjdHKt5n461bfNjso_nlh0C0r30OSuBfwYr9E0tre6Xkqn66T6AOsamOPt6-jzs5wK4c7mDzc2ZZSD4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی ۲۰۲۶؛ تدلاسو و دستیارش بین دو نیمه بخشی از برنامه اختتامیه را اجرا کردند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/673163" target="_blank">📅 23:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673162">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYnQDZpEJx-EiclHOTw8PuPmLIKXtpVRpb5fHJnwZBli6e6ly_OcXYijj3R7Sw8Epa6lsnkv-VyJ7_lgo5QSLufpqXYhz4QY3vPlQa4T_t_UWO-QeiXZB71HJ58jZB56htsWzJbb91VMt0PjgCu8sYqrPVzU0_zmhJYDwPzaY0NDxKn9X01EIfZ10xISfQB3I7lHfBEcINVwjKN1sZoQFp1vlQbm5LgHNFxgYLXmmQ2Gd_ru26wqKSWR_uJa7IVSZC4Cjwd2dYHNVZA0lO_mKY-90nTF3Kbewf8KX8WVtaWopa8J_Unu0HXn1bOqwWHJkFfvNbiWxOwQcwvmviMU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی زیبا از لحظه پایان اجرای بین‌ دونیمه بازی فینال جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/673162" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673161">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgd4rBKh-qki0MXoufYE-RESKi1JpqeFrTe_ioStudUHj5Lb99T5U8Qik8sgirCN0N7X_6_MDE9nzQSjlA9i4DlFmtgYka7wRNy17lWTP_h3WxFWS9Hv-9BEnvgRoN4skLOZ8BpSynUG0GgI7HSIBAf8TLUxbUUXfV4H8uMJy9eqzYPE9e1W3PJaWHL3TnxZznMtBEI-hfbdbyAEfSG3bpnsLwDOhkinlReGUgDY_cOSIMiKd1w6coLgFwaEnfs6P4h9NinFTMvpLnekW3lKu85PTfu_C-phZd8zd2UR0YSQDjQF86TK_3mWWD8V9tCNCOTvNZK-FgXTXIQHTNNpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجرای گروه  BTS بین دو نیمه فینال جام جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/673161" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673159">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyqtBgXWsmBWwxTE9HveYYomuDrzUbgSgVVToprZsBDjFbFhtKv740uMLDauvco0QDg3jOMTxBhN3TZGZwQe-se8rQxmtkEyC8sAPWgRJbvOKClVdOKjhpe2Ygu1o3Xdq-s4Rt9vnuZH9eMzA75OBjXjkZOpNe6SNVqCJWuoeVz_GUmjxiLw0Kl5nfIToDDhH7JMyX7xb6rSIdQjcfCGmS_UCUUB2sDWGRGvVMZmvZ1YW7W2KIhoY7OJaH4FYeSnIt0e0VJEMcLLJbGSF6WasSIUdjcCumSj1mBk3FggSbldVAjBJwQoqze5uajsh2E-VHFrKk2VQJbPQFFAvilOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی، حین اجرای ویالون در بین دو نیمه فینال جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/673159" target="_blank">📅 23:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673157">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
گزارشی از هشتمین روز حمله آمریکا به ایران و تهدید دوباره ترامپ
👇
khabarfoori.com/fa/tiny/news-3231372
🔹
مصاحبه جنجالی عراقچی؛ هنوز آقا مجتبی را از نزدیک ندیده‌ام
👇
khabarfoori.com/fa/tiny/news-3231467
🔹
پاکستان هم شاید به جنگ آمریکا و ایران کشیده شود/ میانجی تهران و واشنگتن یا متحد نظامی عربستان؟
👇
khabarfoori.com/fa/tiny/news-3231570
🔹
سعید حدادیان: آنها که می‌گفتند «نه غزه نه لبنان، جانم فدای ایران» بروند جنوب/ می‌خواهند ما میدان‌های شهر را رها کنیم؟
khabarfoori.com/fa/tiny/news-3231482
🔹
آتش بس در دل آتش بس / طرح عجیب قطر برای توقف درگیری‌ها در جنوب ایران / پایان حملات در ازای گشایش ۱۰ روزه تنگه هرمز
👇
khabarfoori.com/fa/tiny/news-3231634
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/673157" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
