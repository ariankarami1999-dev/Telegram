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
<img src="https://cdn4.telesco.pe/file/HmsxHDhPuocH5cLFOPCvFIc55pEw_CRRkdzsNxfnSnEqjy7OpHOSuwlEsUBkh67PqGqU5hDTkl4rB5Q9vxXvKMKLv6LqdcxscMulP84h2KNLgXkBhII4fIHBEoz1bHjLxN3jKjFok8KYAgJ6DswJpwAQGuE3X456q8qNPTr0fEp0qPuZfRDvp5K1fvhL7yCj8ht_EGzmLjZWHAXstADl1wzS8KH97mDIk2QsXWZsT0CW8vECZLYrFntijYp8NVViu7BZlklop2DsL_fMfifldgiuXCH8VacErZ9jHEUREpL9LIwK6Ynzkau5UXtsHtGw8p86lEidJ4WEpuw6G_WKZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.61M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 01:54:22</div>
<hr>

<div class="tg-post" id="msg-658236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
صدای انفجار در بندرعباس
🔹
دقایقی پیش صدای انفجارهایی مجدد در محدوده شهر  بندرعباس از سوی منابع محلی و ساکنان شهر  گزارش شده است. این حمله مربوط به نیمه شرقی شهر بندرعباس بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/658236" target="_blank">📅 01:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای کانال کان: به گفته منابع امنیتی، اسرائیل در این مرحله در حملات مشارکت ندارد/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/658235" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: چشم‌انداز پیشرفت دیپلماتیک در مذاکرات آمریکا و ایران زمانی تیره‌تر شد که یک هیئت میانجی‌گر قطری عصر چهارشنبه بدون هیچ پیشرفتی در مذاکرات، تهران را ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/658234" target="_blank">📅 01:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
گزارش‌های اولیه از حمله به کشتی‌های آمریکایی در تنگه هرمز
🔹
کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/658233" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
خبرنگار المیادین: منطقه تنگه هرمز شاهد درگیری و تبادل آتش است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/658232" target="_blank">📅 01:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
وضعیت اینترنت ایران پایدار است؛ نشانه‌ای از اختلال سراسری جدید مشاهده نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/658230" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای فاکس نیوز به نقل از یک مقام ارشد آمریکایی: امشب چندین موج حمله دیگر نیز وجود دارد/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/658229" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
هم اکنون؛ چند انفجار در قشم شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/658228" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658227">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فرماندار عسلوبه هر گونه انفجاری در این منطقه را تکذیب کرد/
ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/658227" target="_blank">📅 01:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658226">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
گزارش‌های اولیه از حمله به کشتی‌های آمریکایی در تنگه هرمز
🔹
کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/658226" target="_blank">📅 01:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تسنیم: تاکنون خبر هدف قرار گرفتن منطقه پالایشگاهی عسلویه صحت ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/658225" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658224">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
فرماندار کنگان حمله به بندر کنگان را تکذیب کرد و گفت صدا شنیده شده اما هنوز مشخص نیست منشا ان کجا هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/658224" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
گروه هکری حنظله: ما هر حرکت و هر جلسه مخفی دشمن را دیده و شنیده‌ایم. به‌زودی دشمن خواهد فهمید یک سال جمع‌آوری حساس‌ترین اطلاعات چه معنایی دارد
🔹
ما منتظر حماقت شما هستیم، زمانی که نتایج یک سال جمع‌آوری اطلاعات فاش خواهد شد. به جهنم خوش آمدید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/658223" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658222">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
هدف قرار گرفتن رادار آمریکا در اربیل توسط سپاه پاسداران
خبرنگار اسپوتنیک:
🔹
سپاه پاسداران ایران یک رادار امریکایی را در اربیل هدف حملات توپخانه‌ای یا موشکی قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/658222" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658221">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ایرنا: صدای چند انفجار از شهر بندرعباس در حوالی فرودگاه و پایگاه هوایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/658221" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658220">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mus9hIA_VyssZxxrRDbrCh2Y0rpzbWHeIBPhK951Tb3u28L7tC-tqChRKHTaaZ8ztd3KkRxfg4KvparJ239TdM26PTJcSud7qJTvHV5m4vVySyVnyoTuKsq1gNtc8r4fodeh21TxX7vCXv3WjPKlC7v22bxqd1d2SZUQk73udOg9E4Cong6B4mR6HIgNfWEnpM7FaBiKA3AWWxRAiEhdmk6FwXCtf60vBsKXf8tgHrC-lCHS2mOWr2FBP9J_QvCwnHh-BZEaK-0aNpP8ldAttYtaiyQNiBOyoBXfK_iCLKptgEmwdLVaS0aQh-OYVLMUest0_ojYLMizPd2uTr7IDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صداوسیما: برخی منابع از رهگیری یک پرتابه کروز دشمن در عسلویه خبر می دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/658220" target="_blank">📅 01:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658219">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام سخنگوی قرارگاه مرکزی خاتم الانبیاء(ص) در پی جنایت آمریکا و نقص آتش‌بس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/658219" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658218">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
حمله به اهدافی آمریکایی در شمال عراق
منابع عراقی:
🔹
پایگاه آمریکایی الحریر در اربیل (شمال عراق) هدف موشکی از ایران قرار گرفت
🔹
وبگاه المعلومه عراق نیز خبر داد، ایران یک رادار آمریکایی در اربیل (مرکز کردستان عراق) را منهدم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/658218" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658217">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال، به نقل از پنتاگون: این حملات اقدامی از دیپلماسی قهری با هدف وادارکردن ایران به دادن امتیاز در میز مذاکره است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/658217" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658216">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دقایقی پیش نقاطی در عسلویه هدف حمله دشمن قرار گرفت/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/658216" target="_blank">📅 01:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658215">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم: یک مقام ارشد آمریکایی گفت که تمام اهداف مورد حمله در جنوب ایران قرار دارند
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/658215" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658214">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تسنیم: هم اکنون یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه بمباران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658214" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658213">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
خبر فعالیت پدافند در شیراز مورد تایید نیست
🔹
دقایقی قبل برخی رسانه‌ها و خبرنگاران اعلام کردند؛ پدافند شیراز فعال شده است. در شیراز این خبر تاکنون از سوی مسئولان مربوطه تایید نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658213" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658212">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم به نقل از مقامات آمریکایی: منتظر واکنش ایران هستیم که احتمالاً پایگاه‌های آمریکایی را هدف قرار دهد، همانطور که در شب سه‌شنبه رخ داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658212" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658211">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
بیانیه سنتکام درباره نقض آتش‌بس با ایران
🔹
نیروهای فرماندهی مرکزی آمریکا امروز ساعت ۵:۱۵ بعد از ظهر به وقت شرق آمریکا، به دستور فرمانده کل قوا، حملات دفاعی بیشتری را علیه چندین هدف در ایران آغاز کردند. این حملات در پاسخ به تجاوز بی‌اساس و مداوم ایران انجام…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658211" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658210">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سنتکام اعلام کرد حملات خود علیه ایران را آغاز کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658210" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658209">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
یک منبع موثق در استانداری هرمزگان: انفجارهایی ناشی از اصابت پرتابه در قشم و هنگام اتفاق افتاده که همگی ماهیت نظامی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658209" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658208">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea7833987.mp4?token=GLRQwSB21s4nc_0UeR25Jsj-dwhFacaHa8wvwtsfpC8wAKOntsheuweVXehiX3xlgPX0f4ilybkx8XxbB8XajegPCbYVvzZKSWj4GBzujjmGc_W2_K-T1pLKMPCcNUF-mrwjoTNBrh3-G-AtBETIZKVCl3fpols6djspHkrdmfCijgH-yLyBKoQwped04X_tW3zE4lAdfUgT5prweyeoYrfBNxhEYKdkiLNll9cE2YwVJjnsJ9K7vLAwA9o-Zkwj0-pipNpGXulyy-91nWsvBGcioIJvJD9T9r-Yr5Rw5TyA6qzsOJ7Ix-dr-_BIvmNMFMoXgNtFbNd_xbxDjGlUDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea7833987.mp4?token=GLRQwSB21s4nc_0UeR25Jsj-dwhFacaHa8wvwtsfpC8wAKOntsheuweVXehiX3xlgPX0f4ilybkx8XxbB8XajegPCbYVvzZKSWj4GBzujjmGc_W2_K-T1pLKMPCcNUF-mrwjoTNBrh3-G-AtBETIZKVCl3fpols6djspHkrdmfCijgH-yLyBKoQwped04X_tW3zE4lAdfUgT5prweyeoYrfBNxhEYKdkiLNll9cE2YwVJjnsJ9K7vLAwA9o-Zkwj0-pipNpGXulyy-91nWsvBGcioIJvJD9T9r-Yr5Rw5TyA6qzsOJ7Ix-dr-_BIvmNMFMoXgNtFbNd_xbxDjGlUDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون ـ پرواز جنگنده ارتش جمهوری اسلامی ایران بر آسمان تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/658208" target="_blank">📅 01:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658207">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
صدای چند انفجار در بندر کرگان نیز شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658207" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658206">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
یک منبع موثق در استانداری هرمزگان: انفجارهایی ناشی از اصابت پرتابه در قشم و هنگام اتفاق افتاده که همگی ماهیت نظامی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/658206" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658205">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
‌
کانال ۱۲ اسرائیل: ارتش اسرائیل آماده پیوستن به ایالات متحده در کارزار جدید علیه ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658205" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658204">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
صداوسیما: شنیده شدن صدای انفجار در بندرعباس هم اکنون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/658204" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
خبرگزاری صدا و سیمای مرکز فارس: سپاه شهرستان مهر: بر خلاف برخی اخبار منتشره، حمله دشمن به این شهرستان یا اطراف آن تایید نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658203" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
صداوسیما: شنیده شدن صدای انفجار در بندرعباس هم اکنون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/658202" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
افزایش قیمت نفت به سمت ۹۵ دلار
🔹
همزمان با آغاز دور جدیدی از جنگ افروزی آمریکا علیه ایران، قیمت نفت آمریکا از مرز ۹۰ دلار گذشت.
🔹
قیمت نفت برنت هم به سمت ۹۵ دلار در حال افزایش است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/658201" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZZL3cmo-NxNtjhSXx-0PkwyxOoBlIH2EkbHKvGswOSw8_SgnIcR-ntngcNMCI7OLuWejqBjPAI5RF6XJRN5Qa5QLHmH3tHTlG2mWOoR0qZoK_39tWIsev74VtGr_hKlAO6MQt8d5orWTDJhzFYW0kry6IO8P4D11K6MIlxvP-Upw7TTih-Pu59ntYzFxEfXSph5LFCCJ-Uhb4Ir9UXDk0z5ll-o8NbOD3gzZqZPfyA6DKx9B_yjUsD0NkYw1ARIqlAmv982Co_TMfUr1YzbokEbcZ_5hIpsEnzxV_X7kzsekGMTBAT_umtSyG-zLDdhdlO4fITGdjw6U5i5tnzqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
או שנשלח לכם את המוות
או שתמותו מפחד המוות
یا مرگ را به سراغتان می‌فرستیم
یا از ترس مرگ، خواهید مرد
#WillPayThePrice
‎
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/658200" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
آمریکا نقض دوباره آتش‌بس و حمله به ایران را تایید کرد
🔹
یک مقام ارشد آمریکایی بامداد پنجشنبه به رسانه‌های صهیونیستی گفت که حملات تجاوزکارانه‌ای به چند نقطه در ایران در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658199" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7mLe4L4XuaNmfrqyNofcr2QX4Q7--OsdVFSjNtCoRcQA5w7Wn95UrrNP5SeQIR7mR9ZTOudrO73kwXLpxpEqHy8fpZZSPYsuKTu3A9z4HBDS6FeTSlNNsbwNjBD5OSGdhizGLCc6L09j5gyCJOUgJgZItgZ4_aNvO3tMMOkY9c7z5wdtvbg796DJRMoNMQ63bEQkLAapmDqUfa54yUH38S5Ta_FrLyNvIlIYUschPERb9dXWXzaW9JfZzXqEicQfw09Dl13pje-It1wcjjqJ4MuMUjfabXXrUNG9c9CkLEdTUys5uRuGm-NXe2cnAfdzkjhgThp4SfKcn69DvBzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام اعلام کرد حملات خود علیه ایران را آغاز کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658198" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تسنیم: تاکنون صدای ۴ انفجار در سیریک شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658197" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
گروه هکری حنظله: ما هر حرکت و هر جلسه مخفی دشمن را دیده و شنیده‌ایم. به‌زودی دشمن خواهد فهمید یک سال جمع‌آوری حساس‌ترین اطلاعات چه معنایی دارد
🔹
ما منتظر حماقت شما هستیم، زمانی که نتایج یک سال جمع‌آوری اطلاعات فاش خواهد شد. به جهنم خوش آمدید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658196" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
صداوسیما: پدافند عسلویه فعال شده است
🔹
در جنوب استان فارس تا الان حمله دشمن صورت نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/658195" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تکذیب انفجار در جزیره کیش و قشم؛ صدای انفجار در میناب و سیریک
🔹
بررسی‌ها نشان می‌دهد که تا این لحظه اخبار مربوط به صدای انفجار در جزایر کیش و قشم صحت نداشته و صداهای شنیده شده مرتبط با درگیری در خلیج‌فارس است.
🔹
براساس گزارش منابع محلی، دقایقی پیش صدای انفجار در اطراف میناب و سیریک شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/658194" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
هشدار مقام سیاسی امنیتی ایرانی به کشورهای عربی
🔹
یک منبع بلندپایه امنیتی-سیاسی ایرانی به شبکه المیادین: «همان‌طور که پیش‌تر هشدار داده شده بود، هرگونه اقدام نظامی علیه ایران توسط هر کشوری، چه در خاک خود آن کشور و چه در حریم هوایی آن، به منزله مشروعیت‌بخشی برای تبدیل شدن به هدفی برای جمهوری اسلامی ایران تلقی خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/658193" target="_blank">📅 01:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده شهر میناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/658192" target="_blank">📅 00:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658191">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در سیریک /مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/658191" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658190">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
گزارش منابع عراقی: از فعالیت شدید جنگنده های آمریکایی در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/658190" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658189">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شنیده شدن صدای پدافند در غرب تهران/مهر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/658189" target="_blank">📅 00:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658188">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6976eb7c.mp4?token=NoDA_WbTd6PMlvTXDZA3S6enqe6767Fo-CuR-47B1T88Dv7P036oDrGrJY-7VgMBNNU4RfEeCZZjLIim4VgR1VsiWOe67n8qKSZOwCRxOX9gpiTsCmiqKtgtwT4fq4zJ1VqMstkWDW_qwEIMF9PI702yL0BP-CXRNnnAPyqaqMZcephDmfRG_a_ILGONSYDEypdeQ3BfO6cyg9T3xCAMXttK5a-IgnvsrZE7lIOpq7eMVOlvdBsEFlEZbtHluAjeYuPLTBSSFpo0h-4kUaG7jx3NkWWINYkIFMFHHlGN0daOuTQfjQXPF7WnkAcZdRnnTB99g8JiGYy-joIMK6DbPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6976eb7c.mp4?token=NoDA_WbTd6PMlvTXDZA3S6enqe6767Fo-CuR-47B1T88Dv7P036oDrGrJY-7VgMBNNU4RfEeCZZjLIim4VgR1VsiWOe67n8qKSZOwCRxOX9gpiTsCmiqKtgtwT4fq4zJ1VqMstkWDW_qwEIMF9PI702yL0BP-CXRNnnAPyqaqMZcephDmfRG_a_ILGONSYDEypdeQ3BfO6cyg9T3xCAMXttK5a-IgnvsrZE7lIOpq7eMVOlvdBsEFlEZbtHluAjeYuPLTBSSFpo0h-4kUaG7jx3NkWWINYkIFMFHHlGN0daOuTQfjQXPF7WnkAcZdRnnTB99g8JiGYy-joIMK6DbPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: لازم باشد با بمباران مذاکره می‌کنیم
«پیت هگزث» حین بازدید از مقر فرماندهی مرکزی ارتش آمریکا (سازمان تروریستی سنتکام) مدعی شد:
🔹
اگر لازم باشد با بمب مذاکره می‌کنیم... ما در این کار خیلی خوب هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/658188" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658187">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4897c1e3a.mp4?token=OwaEQka_3hTly2RjghbWFqwRoS6iWaHvVKC6DpHB5okv8mlcCqeJiUSJDAjzWQRmD8EjWrkgINesPo8TtdxAoycz18PG71ch_1ZZK0XsBZ893HBxl1a1abMQOls_fuNf1j14Oh1oOGyXJmR6J2m5E3pfUeFNOXtfsvgxP0FTUY0fc7XchKmkSXxDo98VRYfoaI6OzqUehulVpRH_V0UeVtIKAo0lzlmjdJlc2Tsoi6FePRXJ3hMcyvQC3n1JiLkware50aWNYNVB-qCg0RnbV8jIq3imtjPHUxbVQm7n7P6i5lEp3jiKLQBJCRV1kmV8zGLnOIha-gK6gk4EJRQJWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4897c1e3a.mp4?token=OwaEQka_3hTly2RjghbWFqwRoS6iWaHvVKC6DpHB5okv8mlcCqeJiUSJDAjzWQRmD8EjWrkgINesPo8TtdxAoycz18PG71ch_1ZZK0XsBZ893HBxl1a1abMQOls_fuNf1j14Oh1oOGyXJmR6J2m5E3pfUeFNOXtfsvgxP0FTUY0fc7XchKmkSXxDo98VRYfoaI6OzqUehulVpRH_V0UeVtIKAo0lzlmjdJlc2Tsoi6FePRXJ3hMcyvQC3n1JiLkware50aWNYNVB-qCg0RnbV8jIq3imtjPHUxbVQm7n7P6i5lEp3jiKLQBJCRV1kmV8zGLnOIha-gK6gk4EJRQJWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمسیون امنیت ملی مجلس: به کشورهای منطقه گفته‌ایم اگر آمریکا دست از پا خطا کند، اهدافش در منطقه مورد حمله قرار خواهد گرفت/ زدیم، می‌زنیم، دست از پا خطا بکنند باز هم خواهیم زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/658187" target="_blank">📅 00:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658186">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
صدای جنگنده‌ در برخی نقاط لرستان مربوط به پروازهای خودی است/ایرنا
گزارش لحظه‌ای تحولات امشب به روز می‌شود
👇
khabarfoori.com/fa/tiny/news-3222172</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/658186" target="_blank">📅 00:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658185">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
هم اینک صداهایی از دور در کیش شنیده می شود که منشا آن مشخص نیست
🔹
به نظر می رسد تحرکاتی با فاصله زیاد از کیش صورت گرفته است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/658185" target="_blank">📅 00:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658184">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: سنتکام امشب کار زیادی خواهد داشت، چون ترامپ گفته است ما به ایران حمله سنگینی خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/658184" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658183">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اسرائیل هیوم: شرکت هواپیمایی ایر کانادا تمدید لغو پروازها به اسرائیل را تا ۲۴ اکتبر اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/658183" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658182">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3669cf2f0.mp4?token=gMZ4QoifOg_elDF06cFsr04rGpZMKdSFiorpx2KPHQSrShwdv_bR7pSs9DXEibaDuSILoKp91Pc3qXi6elUp1YiA4uSpcMQeUwo8x5jHzkPkYN-kXOdTXTZIsHJqQvb40jdJyhhc3oz1_DZ8_FU5X5E2LCbYb_L3WKuXevXe66WSMh3zcpyaVyfgn4e_cwvE72RKRuQARLnwYdRcK_gp87HCxLdSkJjLnLjjnDSH5a2po9xePxoZkjLQYVir6RvA-9KfFpdGkn4AeArZ7yTz865aiUtlDYPokYQDs5ICli30ftgj7vXPYGDGgWDpAg_YCYdt1BLtVsDLlZOjsD_Xjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3669cf2f0.mp4?token=gMZ4QoifOg_elDF06cFsr04rGpZMKdSFiorpx2KPHQSrShwdv_bR7pSs9DXEibaDuSILoKp91Pc3qXi6elUp1YiA4uSpcMQeUwo8x5jHzkPkYN-kXOdTXTZIsHJqQvb40jdJyhhc3oz1_DZ8_FU5X5E2LCbYb_L3WKuXevXe66WSMh3zcpyaVyfgn4e_cwvE72RKRuQARLnwYdRcK_gp87HCxLdSkJjLnLjjnDSH5a2po9xePxoZkjLQYVir6RvA-9KfFpdGkn4AeArZ7yTz865aiUtlDYPokYQDs5ICli30ftgj7vXPYGDGgWDpAg_YCYdt1BLtVsDLlZOjsD_Xjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمسیون امنیت ملی مجلس: برای آمریکا قبول این حقیقت سخت است که امروز در دنیا چهار قدرت وجود دارد؛ ایران، آمریکا، چین و روسیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/658182" target="_blank">📅 00:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658181">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: ما از آتش‌بس برای توسعه اطلاعات و به‌روزرسانی بانک اهداف خود در ایران استفاده کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658181" target="_blank">📅 00:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658180">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شهر مُهر استان فارس
🔹
دقایقی پیش مردم در شهر مُهر استان فارس صدایی شبیه انفجار شنیدند.
🔹
پیگیری‌ها حاکی است صدای شنیده شده مربوط به فعالیت سامانه پدافندی در بیرون از شهر است و تا این لحظه هیچ انفجاری در محدوده شهرستان مهر رخ نداده است/ مهر
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658180" target="_blank">📅 00:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658179">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3618b4bb8e.mp4?token=MqRTDdYtJlh5KgXtuGjDmLT4MUxBoPDKqlBFL5WqWFUcgIIrow1VywZ8rLAJJColYPQjWJDTFOlsfDqau9ktHNQ81_lxjMPMUvaBiTxYpGEUWwUahJUoW98prU4TXu7q1XhKHJb6A_oNM0B2jBWZyT9PmWi02GKk44iGXRPnXPAW3fl5Y3xlE6je53Z7UDvXvZlqlOp-55JoMy6J3jN1tNnmNlpYIyeI-zQo-LxNcL_AVpDcfBwHhEuO85tCp2D_vUTXK2HJ5G0JuGXgWLaTLWBCb886oUEHfYGKEVhgzRefv5mbDKPxHG5sS3N1mn4MRBR0aeOsROaF18yvPYixnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3618b4bb8e.mp4?token=MqRTDdYtJlh5KgXtuGjDmLT4MUxBoPDKqlBFL5WqWFUcgIIrow1VywZ8rLAJJColYPQjWJDTFOlsfDqau9ktHNQ81_lxjMPMUvaBiTxYpGEUWwUahJUoW98prU4TXu7q1XhKHJb6A_oNM0B2jBWZyT9PmWi02GKk44iGXRPnXPAW3fl5Y3xlE6je53Z7UDvXvZlqlOp-55JoMy6J3jN1tNnmNlpYIyeI-zQo-LxNcL_AVpDcfBwHhEuO85tCp2D_vUTXK2HJ5G0JuGXgWLaTLWBCb886oUEHfYGKEVhgzRefv5mbDKPxHG5sS3N1mn4MRBR0aeOsROaF18yvPYixnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمسیون امنیت ملی مجلس: اگر آمریکا در یک تفاهم محاصره دریایی را برندارد، ما باید محاصره را به جهت حفظ منافع ملی بشکنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/658179" target="_blank">📅 00:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658178">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سفارت آمریکا در عراق برای اتباع خود اطلاعیه هشدار صادر کرد
‌
سفارت آمریکا در عراق با صدور هشداری برای اتباع این کشور اعلام کرد:
🔹
با توجه به تحولات اخیر منطقه، به شهروندان آمریکایی در عراق توصیه می‌شود که بالاترین سطح هوشیاری و دقت را حفظ کرده و به‌طور مستمر منابع خبری محلی را دنبال کنند.
‌
🔹
احتمال وقوع اختلال در سفرها یا بسته شدن حریم هوایی به‌صورت ناگهانی و بدون اطلاع قبلی وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/658178" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658177">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
نماینده مجلس: افزایش هزینه‌های درمان علت عدم پرداخت بیمه‌های تکمیلی است
جعفری‌آذر، عضو کمیسیون اجتماعی مجلس:
🔹
مشکل اصلی بیمه‌های تکمیلی بازنشستگان و شاغلین، توقف خدمات یا عدم پرداخت نیست، بلکه افزایش شدید هزینه‌های درمان و محدود بودن سقف تعهدات بیمه‌هاست.
🔹
در حال حاضر بخش قابل توجهی از هزینه‌های درمان همچنان بر عهده بازنشستگان و شاغلین است و این مسئله در دوران سالمندی به یکی از دغدغه‌های اصلی خانواده‌ها تبدیل شده است./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/658177" target="_blank">📅 00:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd097d280d.mp4?token=HgupxIgrqQp1kPvz90icbOIa7moC2Z6BCx0lkMm-HBavu5d4u262J-_tNwjbyx8rE7NAFcLvoPOMwHD1USLz22VkSIPwQblIx0rKFlpahiaABVUJOoUv_8_9M-iKG02C2Q45q9iXmyov2op4YJuVg5Yap8KPxM_QO6yiBsv4nEiZ-tnl4z5aDdTkcsewxSZz8cPma-uXwFZFkniLw8I7qbcBGiwrVcycrVZ_x54Dwu-XYg3xJOx6QgxuxldXs9sfGla8JxJGJVUemHml_ELzOyxoUTZDhAhz-Jl8gYhXi4ZIs1e5KCrd5mQuSfS9MMfw3g5luInKqf0aLovP76O39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd097d280d.mp4?token=HgupxIgrqQp1kPvz90icbOIa7moC2Z6BCx0lkMm-HBavu5d4u262J-_tNwjbyx8rE7NAFcLvoPOMwHD1USLz22VkSIPwQblIx0rKFlpahiaABVUJOoUv_8_9M-iKG02C2Q45q9iXmyov2op4YJuVg5Yap8KPxM_QO6yiBsv4nEiZ-tnl4z5aDdTkcsewxSZz8cPma-uXwFZFkniLw8I7qbcBGiwrVcycrVZ_x54Dwu-XYg3xJOx6QgxuxldXs9sfGla8JxJGJVUemHml_ELzOyxoUTZDhAhz-Jl8gYhXi4ZIs1e5KCrd5mQuSfS9MMfw3g5luInKqf0aLovP76O39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمسیون امنیت ملی مجلس: ایران گزینه خروج از NPT را در اختیار دارد/توجیهیص ندارد که ایران با شرایط امروز در این پیمان بماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/658176" target="_blank">📅 00:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658175">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb67fb959f.mp4?token=Cpll34fFeqcEtIr64OP7kDSQiQ2uzl0zxnmPjIQA_cJbnH1gcqx9FIwcf5npQijO8yBl3AGeea4lcuVS_nWNpXgF5ilSKpgSGLtravI79Lbl6KS9VANUffYvQ27S-YA0bSG9mz4AnNWd33RtzwC0oi7Xqr4fbNT5wbfhGdGP0y5nF8Mw3lhC-UQM2dikPw8pDkM-ikM-1ri-SAX79dCRZwhZ54jfYjHldgk0b2aOGJXkRjMEr6ZdrJ7ewJhJJLh31chtu-lkp4oCi-do0y9C4afQ-9XowPTb2fxubC8vQcukZigR7sDWCXTq0K1vdJKmI8CGX48HFkMmHMloBCLTLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb67fb959f.mp4?token=Cpll34fFeqcEtIr64OP7kDSQiQ2uzl0zxnmPjIQA_cJbnH1gcqx9FIwcf5npQijO8yBl3AGeea4lcuVS_nWNpXgF5ilSKpgSGLtravI79Lbl6KS9VANUffYvQ27S-YA0bSG9mz4AnNWd33RtzwC0oi7Xqr4fbNT5wbfhGdGP0y5nF8Mw3lhC-UQM2dikPw8pDkM-ikM-1ri-SAX79dCRZwhZ54jfYjHldgk0b2aOGJXkRjMEr6ZdrJ7ewJhJJLh31chtu-lkp4oCi-do0y9C4afQ-9XowPTb2fxubC8vQcukZigR7sDWCXTq0K1vdJKmI8CGX48HFkMmHMloBCLTLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمسیون امنیت ملی مجلس: دست نیروهای مسلح ما روی ماشه است/ احتمال وجود جنگ چهارم در محاسبات ما است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/658175" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658174">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
هگست مدعی شد حملاتی که امشب علیه ایران انجام می‌شود، آشکار و قدرتمند خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658174" target="_blank">📅 00:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
یک منبع اطلاعاتی اعلام کرد: ایران کلیه تحرکات ارتش آمریکا در منطقه را چه در زمین و چه در آسمان، با دقت کامل رصد می‌کند
🔹
این منبع اطلاعاتی تأکید کرد ، همانطور که قبلاً نیز هشدار داده شده بود، هرگونه تحرک نظامی علیه ایران از سوی هر کشوری - چه در خاک خود آن کشور و چه در حریم هوایی‌اش - به معنای مشروع شدن آن کشور به عنوان هدفی برای جمهوری اسلامی ایران تلقی خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/658172" target="_blank">📅 00:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5M6-i7WF1Yquh_OKddXx9uQkBd8u-d_q3O2yYgZC5LY1PxwNayzb-pLohYSj6ByDFF6kWlIkFTa-DN1OqGNbmIvblIVlQjyUyUgn3mWoAyqPvQRjbPvyT33tVV5UlX201wIlxnuxVgxraB_pg5A_5BkX_lremKZlWtJcVuD4du4wWK0yFt8C3rWR_UNx8yBycGXpzwFUO2d_SOlyVKB6NE91uMDzcSsDTfZttb0gVhLSh8TEspR-n6HjA7Ib8fSO07nfwzxXJgdg8CicR9iW_LBOTYJPE7ucjuowYNlPMTpwrUQL86hqIJdW80BHJNskGA6siksEU-G2KfmopKrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/658171" target="_blank">📅 00:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658170">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای منبع پاکستانی به الحدث: ما امروز از امضای توافقنامه صلح، دور شده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/658170" target="_blank">📅 23:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658164">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_x5tPA7MzLwV4XCkjoVj1zAtwWmpTYBI-6iZ20WoT-Gj-0ksw3boG9CodstOsVH34iM66TvQJq4VB00TVil0bn2z7WlrzIf8uQr48isEoiDthsE-lI8aeMvkqUvfxtfbZrMztqvElAlptfAu5JkYaNF4vTw3X70e3Ud3TtdbTc6qJTVeCNi4x3cEnzrs1grBZGCCTZvTiY2LOXHfng8udYoYRV-80XDqdzxuzurT4rV4yyPNHxJTf9z3gElJFFHs_gmodHPmfuOVyM_unyzhqyN-bofZFitBnlnnKQWFvuScCvuMrcTuTbBgiqfcSQZnhkQcYY7HiFJRzyCvqjmLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fv1TX6Algq_RdG4O9b7umcnLbWQoLvg29P60eRDIGF5SnYuOK1HgpkqGDRZngEoTueQcBhboWeLTliExScfcgLsfy2FQXPYUuuYhxerLvtZXIA_iHlmq5vZfbq3DPM3P6o6gsZnSImyDl3Sj6sgFgvi9FoSwO2BKbLBEyxrkxlc5bdorl1y1Ksudebrk2x7hQReHEEP3lyv-MbsivW3o2Jf5z5lkFOqw5a-u1PeU0z-g9vuc6TBtj03q-CpD_7waNHKXgHOg_9OFtOV7kpaaua4BFzU3ahwtr2TgC3J1KH7rIb5vbqteP7nx9z_OG3N1kXYy9lp6auXd3EIosBqLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBbyjXHgLDcO6EGqPp9qC1bOPpzVdGiPnX9ZwoBpAuStelYnhyowcRlBZiUj2YJ_Ov9CovXVy1NSK8-x6FnLp_DW7V_Da0H0LVFis14akZNrrGe7L64lN3zT14ooYpLlj3yqQZCUCK-ILwMRVntP87ZHMJw-nuRfrSRM5LDKH3ytppphpK2UumTD71RyxIwRYUv7i6yHMyPLtuSElrXLCBsPSTifUJR2Y_lJowpaQRjYWh7xR2aWZMOCoMmESs5IGzTkSwGyQyuhaAVG5OlRrxZX8ceniSlFVerADMdW7bCNtwc2fT_YoV5MPbp2Kixt3NqXAwZzDvgsxKUTvQkTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4yjyX7jmcuorLoSZXiaGtfkewCkMBf2zGnNbhjZ6O74DClHR8ccO3ROdsk4Bs13sVTq37G6_l4LKoikapYgKaNbY0nAVPO-ODRx-TpsvlW6a4lRglThmvqZMM-N8ywz9Rwtz4Y7lSqv1ZvadGBwRGBnBV82MiMmk_-oAFMwMrukK6TVjr_F_p5wQnnIJajdlY1K5lK2OidbJCav0ESKMiamZyt8Tk2fqdkc1H86iUmr4FNR1DjhNV0iw7hVm770sdnvxKY3fBl03qjJGOOBICcuRJHTDRRCYdM4W_qjp4FnLErMnLy4_FikOYKxjcVDJ9YD4MDGE4uKzGL94_5trQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P76LiUcrN46uAbAeHSMhnfbJ0mDheNEbZgPIgFdSAzIpx44BvefoQsHpjf1ICIw1Ks7dVdxr06oF6oewRVira5T2E6e-kQx8VBvRMe1mSKbAbs_KaTBJAearHRsRwFtk0G_TjCTC6krPOcHzlEbUjbSV8nm1ejss7rwV5VpYUUUhXgM3tjEMbLViXVvlWeWIsMq4B2zuPqhnTY9nFRZwjJaW8kN5LRL3eUPNzAopv5unOvzqUhAyQdBYW4GxriSBsGX_IeRR7roalxLgLJ90nZwaDMuYOs5yfaA2ajUuxkCTJU0BMM-GX9eb7NVjgDVBuAeO23A6snKzpfCO3y9sLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ot2OKdD43ghxGhLgE4z5IoITDJlpD2JCVhyWF3uz-xncjWazxGQUi8Lc18TrFU3n6dbjL2CrmaU56hXHPK51gQmBQl1Y1BaH0fd3tNTmZ6wVaw-A-gJ30kCagHO8la1_98YZp5Gk-znV7sSSaC-ttPP-OU1UYWB9oUN72VbVBKzVvBmz3KnUaYqp-o29kGmpf7FY6q57CdqEpSBKb0KLvBe3FRWwXO86XfBX2oImm4xEsuMcyOlfny3_To7AtmMdobRtaHqapj1V1JeSdYKlIr-zOWMMFo99dzEd_DUlhiM3c6SRM4CRt1MZf27GlpJluaYspfxKAXk3oh70q921Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جام‌جهانی در اعداد؛ رکوردها و داده‌های جذابی که همه را غافلگیر می‌کنند
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/658164" target="_blank">📅 23:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658163">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای اکسیوس: دو منبع آمریکایی گفتند: ترامپ بعدازظهر چهارشنبه جلسه‌ای در اتاق وضعیت (Situation Room) برگزار کرد تا درباره حملات احتمالی جدید علیه ایران بحث کند، این جلسه ساعاتی پس از آن برگزار شد که ترامپ به خبرنگاران گفته بود آمریکا «امروز دوباره به سختی به آنها حمله خواهد کرد»
🔹
منابع گفتند یکی از گزینه‌هایی که ترامپ در نظر دارد، انجام عملیاتی با مقیاس بزرگ ولی کوتاه‌مدت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/658163" target="_blank">📅 23:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658160">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
ترامپ لحنش را تند کرد؛ به ایران حمله می کنیم/ آنها ما را به عنوان یک احمق بازی می‌دهند
👇
khabarfoori.com/fa/tiny/news-3222119
🔹
تصویب قطعنامه علیه ایران در شورای حکام؛ تهران: پاسخ می‌دهیم
👇
khabarfoori.com/fa/tiny/news-3222091
🔹
انتشار آهنگ جدید امیر تتلو از داخل زندان/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3221986
🔹
ستون دود در جنوب تهران
👇
khabarfoori.com/fa/tiny/news-3222124
🔹
حمله موشکی سپاه به 4 هدف مهم آمریکایی در اردن و انهدام آشیانه F35ها
👇
khabarfoori.com/fa/tiny/news-3221871
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/658160" target="_blank">📅 23:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658159">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn4LZSgO5IX0XojvrKKeywD5GeMa_yo3vbshtsaFEqZW-7-CWON_b6snAKMgMYIuTw_RvQcMiPTWD9gkrUt95529A1oj5dGeYSgYetptKAROtqOjHmr_yEEiXAskfFH-wxQoJa1QnJnmeg8rIZcM2vTe0HVkaD-L1iNVToxagV3pxOUeIXvBo9ELaPxDf_pz_0lzedWRDuOBSVldcERLTERbNeOUtuFUNsVWGZFWeH5BZWwNNWk97JIfXsYfs3NIKDHlVHf4WH-a6PSj9XZnytJAQoa6tveA8iw-ZnCRbXBGZsugY0QNqrO4_YUpbmoGWJyYnIIKs-bdCzhGQMBnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرفوری|گروه های سرود،سپر انسانی به دور زیرساخت ها تشکیل می دهند
!
اجرای همزمان گروه های سرود جان فدای ایران در ۱۲۰ نقطه از زیرساخت های سراسر کشور
✊
به صورت همزمان روز جمعه ساعت ۱۷ در ۳۱ استان
🇮🇷</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/658159" target="_blank">📅 23:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658158">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جی‌دی‌ ونس: نتانیاهو در موضوع ایران کارهایی را اشتباه انجام داد
🔹
جی‌دی‌ونس در پاسخ به این سوال CBS که آیا نتانیاهو در نحوه برخورد با رابطه با آمریکا در موضوع ایران، مرتکب اشتباهاتی شده است یا خیر، او پاسخ داد: «او قطعاً کارهایی را اشتباه انجام داده است.»
ونس از ذکر مثال‌های مشخص خودداری کرد و گفت که بهتر است آن بحث‌ها «خصوصی باقی بمانند». /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/658158" target="_blank">📅 23:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658157">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
مقامات آگاه: ترامپ به شدت از کاهش ذخایر موشکی آمریکا خشمگین است
ان‌بی‌سی‌ نیوز:
🔹
به گفته منابع آگاه، سران صنایعی تسلیحاتی آمریکا خود را برای دیدار با دونالد ترامپ، رئیس‌جمهور دولت تروریستی آمریکا در کاخ سفید در روزهای آینده آماده می‌کنند.
🔹
انتظار می‌رود این گفت‌وگو با توجه به نگرانی‌های فزاینده درباره ذخایر موشکی آمریکا باشد
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/658157" target="_blank">📅 23:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658156">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انسیه خزعلی: توافق با طرف آمریکایی ممکن نیست اما چاره‌ای جز مذاکره نداریم
انسیه خزعلی، معاون شهید رییسی در
#گفتگو
با خبرفوری:
🔹
حقیقتا سلطه‌طلبی آمریکا توافق واقعی را غیرممکن کرده است، با وجود این بدعهدی‌ها، حضور در میز مذاکره برای رساندن صدای ملت ایران و اثبات عهدشکنی دشمن ضروری است
🔹
مذاکره‌کنندگان باید با اقتدار کامل حاضر شوند و آزادسازی دارایی‌های ایران را به عنوان تضمینی عملی و غیرقابل‌چشم‌پوشی مطالبه کنند. توافق‌های مبتنی بر وعده،، «خسارت محض» محسوب می‌شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/658156" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658155">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
نماینده مجلس: افزایش هزینه‌های درمان علت عدم پرداخت بیمه‌های تکمیلی است
جعفری‌آذر، عضو کمیسیون اجتماعی مجلس:
🔹
مشکل اصلی بیمه‌های تکمیلی بازنشستگان و شاغلین، توقف خدمات یا عدم پرداخت نیست، بلکه افزایش شدید هزینه‌های درمان و محدود بودن سقف تعهدات بیمه‌هاست.
🔹
در حال حاضر بخش قابل توجهی از هزینه‌های درمان همچنان بر عهده بازنشستگان و شاغلین است و این مسئله در دوران سالمندی به یکی از دغدغه‌های اصلی خانواده‌ها تبدیل شده است./جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658155" target="_blank">📅 23:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658154">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
منبع بلندپایه ایرانی به المیادین: اگر ترامپ این بار در محاسبات خود اشتباه کند، قیمت‌های نفت با صدایی بلندتر با جهان سخن خواهند گفت
🔹
ایران آماده اجرای نسخه‌ای جدید از جنگ است و غافلگیری‌هایی در انتظار دشمنان خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/658154" target="_blank">📅 23:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658153">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای نورالدین الدغیر خبرنگار الجزیره در تهران: واسطه قطری تهران را ترک کرد
🔹
به گفته ایران، سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.
🔹
منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای آتش‌بس است.
🔹
واسطه‌ها در حال حرکت برای جلوگیری از هر درگیری جدیدی هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/658153" target="_blank">📅 23:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658152">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCHaE_i-DNE4c1GIhGmqlO8xWvcTLwObJ7zDo6_bdKiirOaN0A_APAounXkbsECmahdJoWL-HBEDRCr-sTtTxU4R_3GhSLfqfcDCAeav6kaCKf2c_mmdH6K15l_y9WW6ZXBU6ZNoSa1dQDYMgqvXuF_mL1cB7YbE7NQX3tnW4TB2rca0B2Lj7lcqDxoR6N-bHxwjJCghht4a-NKWr8OwbsDxw3oOo8Z9AsPajjdtZIlw3GB_TyWeOR5Uik3IMzWzuBGOktY3MlSC9LULHeIPMVWsGqomRJFLjOUB-LxZHsHXI735YnqmbmDM2sgClG2zszdA-5xayjVoPiTy19KAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جواد خیابانی پس از ۳۵ سال فعالیت مستمر در سازمان صداوسیما بازنشسته شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/658152" target="_blank">📅 23:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yowk5AVsJtNvNiwOAykqqt_ixYGUkZild8idNtdy4oDra60pH_HUhcsIBa3X-GpoWDItvQb4X433iiGgjZAfaFI3s8wz-BG2IUKb4s5IX_0eM6orDFSpOg-QpMwzaPNlYKAUQ-JGcdkgK5wYdalEqZ1QIeg5g6Mo4PifN_m-N1_qDXVuHNhdGWWvIySLpCOLbP9wxgu10yUyqsXNXKrZHObFT31-ARFgxRfOkjwbOxueFwDiRTXxJlV92MRjXdpXBRCBBpGmIMjPH_UBwEo9iFTwKKdOTpxc9MbzWpZugjLcrHg4dS5H4ws0i-sU-T6cu8XZ8lI-Yk2eo7JmwVmE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: ما از جنگ با بازنده‌ها نمی‌ترسیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/658151" target="_blank">📅 23:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658150">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قاضی‌زاده‌ هاشمی: وحدت فقط حول رهبری معنا دارد نه چیز دیگری
امیرحسین قاضی‌زاده هاشمی در
#گفتگو
با خبرفوری:
🔹
هر آدم دیگری نمی‌تواند محور وحدت باشد؛ سابقه ما نشان داده همه مسئولان نیاز به مراقبت دارند، نیاز به کنترل دارند.
🔹
این جمهوری، جمهوری اسلامی ایران است. به بهانه‌های واهی نباید به مفهوم جمهوریت صدمه بزنیم. جمهوریتی که به پا خواسته تا هم اسلامیت را حفظ کند و هم ایران را.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/658150" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658149">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
هیچ‌گونه فعالیت پدافندی در قم انجام نشده است
‌
معاون سیاسی امنیتی استاندار قم:
🔹
در ساعات گذشته هیچ‌گونه فعالیت مرتبط با پدافند در استان قم انجام نشده و اخبار منتشرشده در این زمینه صحت ندارد./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/658149" target="_blank">📅 23:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658148">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc724dfe0e.mp4?token=fS9p8QWb_KjuIAKefwW03dfU-jAL3dgpwQNVDanUmbsT2OQi_I9CNwYHmLju9YSMF8oA9kPjx9FXaaa6cP5erD018MN6MpGlVFEOD5bW95yDZ0uX-QD_RZE409Ik_axtrsEK_QxSRTsg7JpHwuDn9Xso72OfNLMsrdvfjNDhlCCZ1yuofp8e5pc-VKt8x86iYj8467P4DhN6-Y1n8V70dA0GRHhSwOfaUt7QhKDbD9_azxfwQpf4PWaOZRR1V44KjH9TCuDOm5wmgtPKhkV8THg-ao7rwbgoNMHtRNfvdH7WJSkU6l94ugOhZfUmGwfVxksJVk9ymFmGnSZVfAYXuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc724dfe0e.mp4?token=fS9p8QWb_KjuIAKefwW03dfU-jAL3dgpwQNVDanUmbsT2OQi_I9CNwYHmLju9YSMF8oA9kPjx9FXaaa6cP5erD018MN6MpGlVFEOD5bW95yDZ0uX-QD_RZE409Ik_axtrsEK_QxSRTsg7JpHwuDn9Xso72OfNLMsrdvfjNDhlCCZ1yuofp8e5pc-VKt8x86iYj8467P4DhN6-Y1n8V70dA0GRHhSwOfaUt7QhKDbD9_azxfwQpf4PWaOZRR1V44KjH9TCuDOm5wmgtPKhkV8THg-ao7rwbgoNMHtRNfvdH7WJSkU6l94ugOhZfUmGwfVxksJVk9ymFmGnSZVfAYXuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینفانتینو، رئیس فیفا: قولم برای حضور ایران در جام جهانی؟ اگر مجبورم می‌شدم، با اتوبوس به ایران می‌رفتم و تیم ملی را به جام جهانی می‌آوردم؛ البته که کار آسانی نبود
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/658148" target="_blank">📅 23:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658147">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhjO096ZcIau3fs1-b5pQzwDG5VOsFsVmmwDUKDzwAWNSaNKmOPDocSYxQRKZwf2MSW4Bs1-pNcOtpdvKWM295V47CSJn2ThZI0BH8PZyBsUIxTDtUhSaoT9PVxpKxyjDJkkckoVV0jJmtoCbTQ_SDDg7OHwF2mLoy3lhn2k99ozf9_0WpGqElJfduuSXn_Vmj-iPNLiFWbxJ46bxBQe-rDhNFgkOLkm4Pvtzo0NkzvvvtG8ChxNJYI4ihvu-8Mu70R4M4ydvrPfWHrJbwXHz5hnqB87s0_ICFKZJxxcB8QuYf00GqKaHh98J3xtpYMRBxnqOag9er1Kub0-Gxidhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تورم مواد غذایی به ۱۲۹/۸ رسید!
‌
🔹
براساس داده‌های مرکز آمار تورم مواد غذایی در ایران در اردیبهشت ماه به رکورد ۱۲۹.۸ درصدی رسیده و قیمت اقلام خوراکی نسبت به ماه مشابه سال قبل بیش از دو برابر شده.
‌
🔹
در جهان، ونزوئلا با تورم اقلام خوراکی ۵۲۴ درصدی رکورددار است و ایران با تورم ۱۲۹ درصدی دوم است./ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/658147" target="_blank">📅 22:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658146">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
معاون رئیس جمهور آمریکا: به توافق بسیار نزدیکیم
‌
جی‌دی‌ ونس، معاون رئیس جمهور آمریکا در مصاحبه با شبکه خبری سی‌بی‌اس نیوز:
🔹
ما به دستیابی به توافقی که در درازمدت به برنامه هسته‌ای ایران بپردازد، بسیار نزدیک هستیم.
🔹
هدف سیاست ما اطمینان از این است که ایران در آینده به سلاح هسته‌ای دست نیابد.
🔹
هنوز کارهایی برای انجام دادن وجود دارد اما ما همچنان به پیشرفت در جهت دستیابی به توافق ادامه می‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/658146" target="_blank">📅 22:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658145">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای باراک راوید خبرنگار اکسیوس: ممکن است مذاکرات ظرف دو تا سه ساعت آینده دچار فروپاشی شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/658145" target="_blank">📅 22:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658144">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
توئیت
یک مقام اماراتی: ابوظبی به دنبال کاهش تنش با ایران است
‌
ادعای مشاور پیشین محمد بن زاید رئیس امارات:
🔹
امارات زمینه کاهش تنش با ایران را پس از آن فراهم می کند که بازدارندگی این کشور کارآمدی خود را نشان داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/658144" target="_blank">📅 22:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658143">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فلاحت‌پیشه: ترامپ می‌خواهد ایران را عراق ۱۹۹۱ کند
فلاحت‌پیشه، استاد دانشگاه و نماینده پیشین مجلس در
#گفتگو
با خبرفوری:
🔹
در مورد جنگ، علیرغم ادعای ترامپ مبنی بر مخالفت با حملات اسرائیل، نتانیاهو و ترامپ کاملا با هم هماهنگ عمل می‌کنند.
🔹
در واقع ترامپ تلاش دارد جنگ اسرائیل و آمریکا با ایران با شدت تمامی که در جنگ ۴۰ روزه شکل گرفت، توسط اسرائیل ادامه پیدا کند و آمریکا در میز مذاکره امتیازات لازم را از ایران بگیرد. آنچه که در دستور کار ترامپ و نتانیاهو قرار دارد؛ تبدیل ایران به عراق ۱۹۹۱ میلادی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/658143" target="_blank">📅 22:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658142">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWCpvJJ0paJ0i92lOOH_tuQIfxFkOVSivm6J-F2zdmtFSHgEO6rEq_2UJnbdFVDOE_Q4OFKCEMCgvyZmyixeD88aQvy5rKjjbTmjgfbJzyinnh6dbyzX7VcGONm5FXeFBy1HVTOqHL0bYdqgjefHd-mSR0JbyZcQdJp-YsSdWk30uXFPIVml0UyhFIjOLEe7YaWLIJRMocPF4Y0pRG-ZNQgIo7wHE-SGvKvVIlFSaTNWJ1aFAcHYtO2x_hV2JUhbydirpHYh9pgurvR6eOCIO0Am2Gl98-luzzAxkJw6YgEejbw0Uo8pGt20vZ6JzhwacI5jGqWKwuqZK3Z2stvjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگه در این روزها دچار استرس می‌شید و تمرکزتون ضعیف شده این اینفوگرافی مخصوص شماست
🔹
تکنیک‌های فوری برای آرام کردن ذهن در لحظات بحرانی/ اخباراصفهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/658142" target="_blank">📅 22:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d884dfa50.mp4?token=EacmWKLBhjt1gapj3A_cVMNCMquP7mcPhIymnCPnZjBe7jwj_e0Dl0OyvLtBy7J43o1l3upiG3iCM74VkYv8y1CVPdHx8SlGeT4dnLUqmzHqdvN1WUUQfNDwxmyyXcAa6sbngUbuIQK151zYT2owPwMJdOoCKI_6K_AMiHiUJd3ckkXpzr_pKQYCmJWIy0s-65ZS3u4kIKrW-FxUKKdr9jjW0HUVJL7y6rPNqhBb12WjQZ-qqpOnk_fz3LVcrD3RQwGfjy24mSXDMuM2M9cjwm0iInw2zfEWvW-NaiCPd6OMyg59lAzBZjGrleGkxLKp9b0vCTGpNpGpyuWi_Cse7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d884dfa50.mp4?token=EacmWKLBhjt1gapj3A_cVMNCMquP7mcPhIymnCPnZjBe7jwj_e0Dl0OyvLtBy7J43o1l3upiG3iCM74VkYv8y1CVPdHx8SlGeT4dnLUqmzHqdvN1WUUQfNDwxmyyXcAa6sbngUbuIQK151zYT2owPwMJdOoCKI_6K_AMiHiUJd3ckkXpzr_pKQYCmJWIy0s-65ZS3u4kIKrW-FxUKKdr9jjW0HUVJL7y6rPNqhBb12WjQZ-qqpOnk_fz3LVcrD3RQwGfjy24mSXDMuM2M9cjwm0iInw2zfEWvW-NaiCPd6OMyg59lAzBZjGrleGkxLKp9b0vCTGpNpGpyuWi_Cse7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی آتش‌نشانی: ساعت ۱۹:۴۴ امشب، گزارش حریق گسترده در یک انبار فرش واقع در محدوده خیابان ری به مرکز فرماندهی اعلام شد
🔹
محل آتش‌سوزی، یک فضای حدوداً ۲۰۰۰ متر مربعی است که عمدتاً برای انبار کردن فرش استفاده می‌شود.
🔹
عملیات مهار این حریق با مشارکت ۸ ایستگاه…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/658141" target="_blank">📅 22:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658138">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk1DL4Iw9u8DHhbjQ7xbTxFUxomwTsRwXLAL2RRJNWwGdXlkitMrc9XYJPLDoQnnUIwmYEdNUDLjc5nH7xNuYM6B0X5bfFALQY98rbkagz0bpeYoDN4ThJyoXnf39yVXiwtAR4Rm_H5Hb-Lqxl7a1FZg5sywgeKJP15zBR2by5hl3BnwH_E_sYmok0kIe87purhS6MB5dTKe6SesS53O4bzXrsuPxfNi42eARVBUEfEH_9OpSfgYTCzGbxInou9UUeUfdW-rRezDIETFKXkAowaWQB2Cx8f3KaAOiduyIzRDee2j90fvmcJn6vmxOLg6ZAU6aT-Srisld5IY7FJU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی آمریکا و حضور رژیم اسرائیل در فهرست پرهزینه‌ترین برنامه‌های اتمی جهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/658138" target="_blank">📅 22:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658137">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGNZpRj7EfPYGzAXtQzm6Mk6JtFf6h2mx7jpkiUoHv8kFfKMX89Ul8nIdpEqHhlpV_nX5xF3giWrpage2ypJf-sx2o9qSTcBTKguC3j7OGH2mU958sLAvJ1ZF8nT8sojuoErdhA5fcqF42k4WCrPynTnExUxEr_B8NocN9ZbcWWGoBjUo2FNrNmuH5zTAciALsnDsEXyGTR-ToggSG7vgrl4h5FKJrs7S5mk-WZ5zZnk_yJ3wwkBNOqctQ8HBoNak7n2djeqk2Rbj5AVcXBQ6fKDtcimMIhHhqcJCIFYKzWVaq3RCxdN2_OPWumxW_IQxPiG-YRUbZkzJU32_VA6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر سابق CIA: آمریکا و اسرائیل به دنبال «خرابکاری» در مذاکرات با ایران هستند. احتمالاً شاهد درگیری‌های جدیدی خواهیم بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/658137" target="_blank">📅 22:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658136">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتاپ تورز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0SEBFAF1SrugQslolDlwURs6dQ02LA64XqXFQ8zy71n4CuWEqfn1_xDtO7kFS4V7K-8K5M8qRbQOy_fKnKbTqX871p-PgSKqu9pus3vrsJeVBviK5h3cfK_AFC9H3mdtx3xs843Om0zNFM8Dmk4O_87PogtLjF2LXPuFNhJQncp0xLSYTk_9Q9YY00Juh0Rt2vwFw5JMoJYfpVln8uGpj9rnTYnb-1WyyBVN03DMdmusI-vskykNbCceDe6SepD7SlDm2v56Ba7Rd8UB25klDcFw4fk5ZtFM1lt5-O3sK-83oqr9gX19g42dL7tmNScfRr20cTk_C7P1zsF7o_aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
شروع پروازهای هواپیمایی سروش
📍
در مسیر تهران - استانبول - تهران
✈️
ایرباس مدرن310
💺
صندلی بیزینس
⏳
بهترین ساعت پروازی
خرید آنلاین از :
www.Booking.ir
📞
+98 21 8586</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658136" target="_blank">📅 22:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658135">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d7dff107a.mp4?token=TAtf6Lsdogy72T12zAR1SBKsbc1K6-oUGmbw-h39pFbQ5M6y5FoRsi7HxGZY3E9IkB2ub9Zc4_5z0xCCq8CfuN5Evr1_aS8cMpH4U2psq20DwsBdt0xYh5E2fjott_euWky2xz37DR6CgxY55mCDD1Hv1et_NoG724Fr1Tj_d3pPscVVyCffpVhZcmAf2qfqvS-pw1YVdqb9ogA-trh9ZYlmkGB-4jamA01CzxmvzW9QY8ZUFa3jHs3qwLT8OcRJxDKITYMpbY7nsiuE4KB6M0AX_3GPToPtFqFKIUzNo61bq74NRhBqcL3pAy8sbbf_Cj9OE81lzgI-gGIjttY2c0TKv0papgZM9LHH2h9vJmS_f-gmg2RHrcYo9ww1zE4nnvz1LnEKj63xJjs3u7PfXdPWX6BMylCUwOG7S9mK9rJY6Quh7OrKkHzTy_DpE7WRgX7A4gLkYQoLFTjirFimgoYOmRFUALCCLDNIwjO10aZnOcy7lJw3cSP15AKzFAQ2pUDC5g6L1t6WrdXVbKoDS1EfW1qkMJRahaSl3hbg6FrK3TbTig5Vq1ZIjdYf_YRQGa-DGPaijDVXNh2HE2VM3nx9iTMBLrPrk9vsGT_ENx8MKi3_JANUpe9zVymxEoc2NAe0zLs_1dvtSgOkNc2BOtlB8P8ELkWifQ9pI0acuv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d7dff107a.mp4?token=TAtf6Lsdogy72T12zAR1SBKsbc1K6-oUGmbw-h39pFbQ5M6y5FoRsi7HxGZY3E9IkB2ub9Zc4_5z0xCCq8CfuN5Evr1_aS8cMpH4U2psq20DwsBdt0xYh5E2fjott_euWky2xz37DR6CgxY55mCDD1Hv1et_NoG724Fr1Tj_d3pPscVVyCffpVhZcmAf2qfqvS-pw1YVdqb9ogA-trh9ZYlmkGB-4jamA01CzxmvzW9QY8ZUFa3jHs3qwLT8OcRJxDKITYMpbY7nsiuE4KB6M0AX_3GPToPtFqFKIUzNo61bq74NRhBqcL3pAy8sbbf_Cj9OE81lzgI-gGIjttY2c0TKv0papgZM9LHH2h9vJmS_f-gmg2RHrcYo9ww1zE4nnvz1LnEKj63xJjs3u7PfXdPWX6BMylCUwOG7S9mK9rJY6Quh7OrKkHzTy_DpE7WRgX7A4gLkYQoLFTjirFimgoYOmRFUALCCLDNIwjO10aZnOcy7lJw3cSP15AKzFAQ2pUDC5g6L1t6WrdXVbKoDS1EfW1qkMJRahaSl3hbg6FrK3TbTig5Vq1ZIjdYf_YRQGa-DGPaijDVXNh2HE2VM3nx9iTMBLrPrk9vsGT_ENx8MKi3_JANUpe9zVymxEoc2NAe0zLs_1dvtSgOkNc2BOtlB8P8ELkWifQ9pI0acuv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ساقط‌کردن آپاچی به آمریکا برخورد؟
🔹
جزئیات جالب توجهی را در این ویدئو خواهد دید که به شما نشان می‌دهد چرا آمریکا از سرنگونی آپاچی عصبانی شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/658135" target="_blank">📅 21:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658133">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC6WlEd0eLgxnbJ1tdsjviDnSj9Q5rxPvS0-iRccj4pYeVP4hdCyCmPBT_UVHCCWON5Z3IDjBBf6LlAqCMN9FyczFyec96lqkMntxzEUkodfH2dkgRWQ07Mg0tOwyb0EDjFoXlKP8vdua4ysUDALVPh68A2BF4O8TR6d1e7JbALOtO6dTxsyXF_aWmjbhvpJdWWvg9juH6CZkqCuU1mdq9qEXUbzA0RBBCP_gANtDRuCgvrP79Np_aJQFcAnbHRl8-oVfDYPjBCgS0EYZ0HgjQRXWf6OGeOeTd8vJPBQgNBYyhjCJUuyXWt35rc86ibLPVpVQcLlY8vy5EfGeTvV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرش ایرانی همچنان محبوب‌ترین صنعت‌دستی
🔸
در این نظرسنجی بیش از ۲۳ هزار نفر شرکت کردند که سهم روبیکا ۶۶، بله حدود ۳۰ و تلگرام حدود ۴ درصد بوده است.
🔸
بیش از نیمی از شرکت‌کنندگان فرش، قالیچه و گلیم و ۱۸٪ هم صنایع چوبی و چرمی را از میان صنایع دستی ایرانی می‌پسندند.
🔸
سلیقه مخاطبان بیشتر به سمت صنایع دستی با هویت فرهنگی قوی و کاربرد روزمره است و شاخه‌هایی مانند چوب و چرم نقش مکمل دارند.
@amarfact</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/658133" target="_blank">📅 21:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658132">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی آتش‌نشانی: ساعت ۱۹:۴۴ امشب، گزارش حریق گسترده در یک انبار فرش واقع در محدوده خیابان ری به مرکز فرماندهی اعلام شد
🔹
محل آتش‌سوزی، یک فضای حدوداً ۲۰۰۰ متر مربعی است که عمدتاً برای انبار کردن فرش استفاده می‌شود.
🔹
عملیات مهار این حریق با مشارکت ۸ ایستگاه آتش‌نشانی همچنان با شدت بالا در جریان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/658132" target="_blank">📅 21:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658131">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
برنامه بازگشت حجاج به کشور؛ امروز ۱۰ پرواز از جده انجام می‌شود
‌
هواپیمایی جمهوری اسلامی ایران اعلام کرد:
🔹
عملیات بازگشت حجاج بیت‌الله‌الحرام به کشور در روز چهارشنبه، ۲۰ خرداد با انجام ۱۰ سورتی پرواز از فرودگاه جده به چهار ایستگاه پروازی کشور ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/658131" target="_blank">📅 21:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658129">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای ترامپ: ماه گذشته، به نیروی نظامی آمریکا دستور دادم یک مأموریت مخفی برای پشتیبانی از نفتکش‌ها و دیگر کشتی‌های تجاری از طریق تنگه هرمز اجرا کند
🔹
امروز با خرسندی اعلام می‌کنم که این تلاش منجر به عبور بیش از ۱۰۰ میلیون بشکه نفت از طریق تنگه و ورود آن به بازار آزاد شده است.
🔹
بیش از ۲۰۰ کشتی تجاری با سلامت از این تنگه عبور کرده‌اند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/658129" target="_blank">📅 21:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658128">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای اکسیوس: به گفته یک منبع منطقه‌ای درگیر در میانجی‌گری و یک مقام آمریکایی، عباس عراقچی، وزیر خارجه ایران، به میانجی‌ها و آمریکا گفت برای گرفتن پاسخ به چهار یا پنج روز زمان نیاز دارد
🔹
این زمان به یک بازی انتظار دیپلماتیک تقریباً دو هفته‌ای تبدیل شد،…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/658128" target="_blank">📅 21:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658127">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ احتمالاً اواخر ماه گذشته می‌توانست یک توافق اولیه با ایران به دست آورد، اگر شرایطی را که فرستادگانش مذاکره کرده بودند می‌پذیرفت ‌
🔹
در عوض، او پس از جلسه‌ اتاق وضعیت در ۲۹ مه تصمیم گرفت درخواست دو اصلاحیه در پیش‌نویس تفاهم‌نامه را به ایرانی‌ها…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/658127" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658126">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ احتمالاً اواخر ماه گذشته می‌توانست یک توافق اولیه با ایران به دست آورد، اگر شرایطی را که فرستادگانش مذاکره کرده بودند می‌پذیرفت
‌
🔹
در عوض، او پس از جلسه‌ اتاق وضعیت در ۲۹ مه تصمیم گرفت درخواست دو اصلاحیه در پیش‌نویس تفاهم‌نامه را به ایرانی‌ها ارسال کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/658126" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658125">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5d-zZP3fEQ09rnqNLH2_hATky0Qc2DqwRRRk_NnXg46M96L2PIrHvqd9RyBkLlLt4zqKVj_-j6BgET0iefcfg2ShCwXG23Fj9gvg4n1g-58HZU8YlyK1J4j_4t08DqgwlKGgJqWa7q3w5XazZ5Xacx6vxN21snkHSbt9pEgwCTH1OLNvsUUuPp0wZgPw7pW7dqdpIUqDuTyJvs4YDNnHHNQ-P0UEgudWHzkdKDkVpIV9qx6ih7_ALF4pclfKC5ZlxfEHgQ_fRt-t4S_NA_4joAVQDkjrGsrmP-tGO72wlIUtHGRbdyTDs-c32WPBkCu7K6BFEwTxaebNaLdtRn1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در مسیر جیمی کارتر
فایننشال‌تایمز:
🔹
آمریکا امروز بیش‌از همیشه در مهار نتانیاهو ناتوان به‌نظر می‌رسد، این اتفاق موجب شده تا ایران نیز تمایلی به مذاکره نداشته باشد و آمریکا تعیین‌کننده پایان جنگ نباشد.
🔹
ترامپ برای خروج از این وضعیت، سه راه دارد: تهدید اسرائیل به قطع کمک، جدیت در مذاکرات و ثابت‌قدمی؛ که با توجه به سیاست‌ها و شخصیت ترامپ، محتمل به‌نظر نمی‌رسند و حالا، او که از تکرار تجربه کارتر و افتادن در چرخه تلفات نظامی می‌ترسید، بیش از همیشه گرفتار آن شده است./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/658125" target="_blank">📅 21:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNNg_DaPXt3fwfozbEPcc7F-2MFLqrgjY-MMMedgOoMQNPQxprSGr5N7pZpC5rh-dFpcFuBpmZlOCs0Nwz3mb9qlYqIzKRN0rlN3_F419p-iaj5lchq1ED353JHIFxpBHfedW_6e6D2RGyOE98uQDvLV4izT2VofnpiAz7Gu5_RORU4VtIWBENnd9uSI5bAPZyY139t0z5D_Atje5EqLrM5Ob05sqvDF_-DIWF23zybxR2wGV5kup7yW3q7LjDhQfKbATG1NrE-FPD6v25ok8OXvmOrlZwfxsHDhCo4SMMQDrTRFUroSsk_hVNQD_CrGB_BhFYfepDbSxRr2Te_D6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFN--TRcIb4sxFCn5eNbv04tzeAfnt_42n2PFo5_rCKTFMl9v6-eP0nuqA52deGETpocZBoX6UGaXX2Y8Gf0w0Q6kCYnsd5itMqn1plougva6yQwIYWcsmxJVe3ieCQJDs61xSgBY_GoTWU272BMF437QlulH0uvqqW50dpD5XAj24kTZ92LyNWUDb7OuhKKYHgFLOcCXN6iYnkn1StsMoE961q6nfA8cvyJK2LvZkVHh5WpgQEHzh8J1zhBDAtVfODW9Zft9nuYFRmeabPSWjwR9hG0Su0UZiCLpa169ABWT5y1KtHJlLY7tVanCBlrfM5eGBskMPbIde_UOLUKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UA9tIkx3swi05VTfAOCemW7K3agS2mNdagus7ej9kFVEwrknq0ZYWTLOwbrN_5wIwQgE2YECaKahIswr1VtNg8qfQfW2r-7D3EowvVVsfAdguYOKqn1egikL2UC2QljhiW1YWUHszabaaWYYpRfqhqKGrLNOfl7wzD4wxuqeAgmRJh88Y7LhLSe4M2kbjMa53DXNRrHUNexBwv5La-P7HiFdcJPYG0wdpIp6K2h3DdeA54jt1Ui63rOhmOUnUuMNZYd8eku566LUgX8LefaxRn9qUdmlI19HTCdib4osBaFk3KbQIN_XA5cOegAaboJ6t47aExz3jGKkssKRiDgUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAp3YBVNgNMX6Oq8U3quYA6C9ussugWSdWhuhh5vPtae7zz2TLquGYhEOwTJ6lVKw0tIrLePjObL-iQhm3z3dFHV2LUwN_YtfLJmInuqlq_OsTu7VzlrETJb6rQTabiMlLLTYueDEYGVurrvrrR-x-XDjv8d8VR80PBzJs_Q8WULDAbrMq3oUoe3DWfdO-VKptV-jmWvebg8U85mzNCaPWLoETQ2TxJ7555tmXnhFNs3FhQ_gJiHXAUPlRQMyonSpU4VG9_TKKiIeOOz-560p6ErFyJCWSX848wAF2mPWApw4YZ8F5FqmELw9h2cqbb9yM4iEKMKRXM0raI-co5UXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a7594099.mp4?token=eVPtOI_Li0uMysKTrLSXxkqnqluUClsdgvckCD_4DUyii95KF4Gx-Ned-N-2YgNw-5n0aENKDgsPPmLLEOuBfVmDVEclTXPBSDQN_NohvO34UD9u5NPtJrHQVGlKnnV4wqhYlwMMM8Xs6mk4udCvnLD8-Azfu5F9xkGD_K2xs-w2dR8Oo_BppDBuSMgkyIAjNCwr1dIAH44IIhEJ3f5O9ONjZrQ965IduzAFkz3N5UVdL7vXG69ktcsVgLIlu2T2h0VH0l5e9TWadENXgy4Xl42BlQ0LXeBjYLVmwpMaTha2ucObRMYYuhHERN31zwFNIXqArwpHt1Z4_rQ1CEpM-iEE6guOOfJ--3vm_Lt2OYIJFKB42HMKyppMwE7Yt-8V48rCx_ka3b8BAfa6MjPsWy3MFSzxA2IKjxL7bgVzdsmrulVlpdS0e_Cm9P1EFP7S_ZlJ9RpRUPgd8jFKx74mH465UnBchlUupX8sVjKVJ9WOjIWrkUb0qxXvhlBmQYg6P5LFCuwu7DSBexnNAVl2lpRIURgtAsCCk69OXLNbYsu56Hl44nxY3y6EaV0UDk24hHnq9soD3O5J11j8nyu8Jp_cEPM1GAy4MYUECOmY_Bu-VKgjQmcddS0eyvatllrW5XA5aeHvnTz5iFFflitBxj_Pkf_B_vmdRI8rIYwTlU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a7594099.mp4?token=eVPtOI_Li0uMysKTrLSXxkqnqluUClsdgvckCD_4DUyii95KF4Gx-Ned-N-2YgNw-5n0aENKDgsPPmLLEOuBfVmDVEclTXPBSDQN_NohvO34UD9u5NPtJrHQVGlKnnV4wqhYlwMMM8Xs6mk4udCvnLD8-Azfu5F9xkGD_K2xs-w2dR8Oo_BppDBuSMgkyIAjNCwr1dIAH44IIhEJ3f5O9ONjZrQ965IduzAFkz3N5UVdL7vXG69ktcsVgLIlu2T2h0VH0l5e9TWadENXgy4Xl42BlQ0LXeBjYLVmwpMaTha2ucObRMYYuhHERN31zwFNIXqArwpHt1Z4_rQ1CEpM-iEE6guOOfJ--3vm_Lt2OYIJFKB42HMKyppMwE7Yt-8V48rCx_ka3b8BAfa6MjPsWy3MFSzxA2IKjxL7bgVzdsmrulVlpdS0e_Cm9P1EFP7S_ZlJ9RpRUPgd8jFKx74mH465UnBchlUupX8sVjKVJ9WOjIWrkUb0qxXvhlBmQYg6P5LFCuwu7DSBexnNAVl2lpRIURgtAsCCk69OXLNbYsu56Hl44nxY3y6EaV0UDk24hHnq9soD3O5J11j8nyu8Jp_cEPM1GAy4MYUECOmY_Bu-VKgjQmcddS0eyvatllrW5XA5aeHvnTz5iFFflitBxj_Pkf_B_vmdRI8rIYwTlU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش اولیه از حریق یک انبار در میدان قیام از زبان سخنگوی آتش نشانی تهران  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/658120" target="_blank">📅 21:10 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
