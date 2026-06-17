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
<img src="https://cdn4.telesco.pe/file/OmnSSnxanoCXCxHJckNwsPtokqW-sErO63vLTsE7iUJHcjh_x8CWZ7lqy8f-gmdUANYH0KEJsmXrM9vS2H3eIHvUruRnhVpWsbiglnCnCdlnOvOKn14kJ902aRBg_Ht3dNXuBY4hzjRlI6UAzfKGbnAMUuRk7VlcoN2rXHZv1CUBwzluD2tU4tlbp7zQFNniYy_6YCINDjH-ZTOfr2DtCvyULJ4dJfxUPHqf0PeBHyqZry3o6tCqCpUPToR1DFp-e0R6qpiUNQTwngh2nfU_i0EZVADl36EHeFOC3b_tsrw2EU58js78A1qSKgznmf-LqsemhfzobkIsRfYhdoauzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.49M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 01:23:42</div>
<hr>

<div class="tg-post" id="msg-660650">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بقایی: تعداد بند های توافق ملاک نیست مهم منافع ملی کشور که در توافق گنجانده شود، برای ما دستور عمل های شورای امنیت ملی که صادر کرده بود بعد آتش بس ملاک بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/660650" target="_blank">📅 01:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660649">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بقائی: متن تفاهم به دو زبان امضا شده؛ این اوج شفافیت ما در اطلاع‌رسانی است. اگر فقط متن انگلیسی بود دچار تفسیر سلیقه‌ای می‌شدیم. این متن کاملا منطبق بر متن انگلیسی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/660649" target="_blank">📅 01:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660648">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
بقائی: رقیق‌سازی مواد غنی شده، موضوع جدیدی نیست و برای این مطرح شده که راه بر گزین‌هایی که به هیچ عنوان برای ما قابل قبول نیست، بسته شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/660648" target="_blank">📅 01:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660647">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بقائی: ما از ابتدا گفتیم مواد غنی‌شده ایران به خارج منتقل نخواهد شد؛ در صورتی که طرف مقابل دائم مطالبات زیاده‌خواهانه‌ای داشت که درنهایت به نتیجه نرسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/660647" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660646">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بقائی درباره بند ۸ تفاهم: ما درمورد تنها بعدی از موضوعات هسته‌ای که صحبت کردیم درباره رفع تحریم‌ها در بازه ۶۰ روزه بوده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/akhbarefori/660646" target="_blank">📅 01:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660645">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سازمان ملل: از توافق ایران و آمریکا و بازگشت دیپلماسی استقبال می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/660645" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660644">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: بدون هرگونه مماشاتی، اجرای تعهدات طرف مقابل را رصد می‌کنیم. در صورتی تعهداتمان را انجام می‌دهیم که طرف مقابل به تعهدش عمل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/660644" target="_blank">📅 01:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660643">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
بقایی در پاسخ به اینکه اگر آمریکا بهانه‌تراشی کند: ان‌قلت بیاورند ما هم ان‌قلت می‌آوریم؛ تعهد در برابر تعهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/660643" target="_blank">📅 01:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660640">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
واشنگتن امضای تفاهم‌نامه با ایران را تایید کرد
🔹
دو مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفتند که واشنگتن و تهران، یادداشت تفاهم برای پایان جنگ را امضا کرده و اکنون اجرایی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/660640" target="_blank">📅 01:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660639">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بقائی درباره بند ۷ تفاهم: متن تصریح کرده همه تحریم‌های یک‌جانبه آمریکا اعم از اولیه و ثانویه برداشته شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/660639" target="_blank">📅 01:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660638">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بقائی:  از هیچ فرصتی برای مستندسازی و پیگیری و تبیین جنایاتی که علیه ملت ایران اتفاق افتاد نخواهیم گذاشت
🔹
از هر سازوکار و نهاد و فرصت بین‌المللی برای احقاق حق استفاده خواهیم کرد. اینها خارج از این یادداشت تفاهم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/660638" target="_blank">📅 01:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660637">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
بقائی: قاعدتا از هر سازوکاری استفاده خواهیم کرد که این تعهد صورت بگیرد برای ما منبع آن مهم نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/660637" target="_blank">📅 01:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
بقائی: بعضی از آسیب‌هایی که به ما زدند به عدد و رقم درنمی‌آید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/660636" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660635">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
بقائی: بازسازی خسارات ناشی از جنگ برای ما فوق‌العاده مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/660635" target="_blank">📅 01:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660634">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
بقائی در پاسخ به این سؤال که چرا برداشتن محاصره دریایی در متن نیامده: چون زودتر این اتفاق افتاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/660634" target="_blank">📅 01:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660633">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
بقایی: اگر متن را مبنا قرار می‌دادیم باید رفع محاصره از امروز انجام می‌شد اما رفع محاصره زودتر انجام شد. باید در عمل شاهد این اتفاق می‌بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/660633" target="_blank">📅 01:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660632">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: موضوع تنگه هرمز به عهده ایران و عمان است. فقط ایران و عمان ۲ دولت ساحلی تنگه هرمز هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/660632" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660631">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
بقائی: در رصدی که انجام شد مشخص شد کشتی‌های ما بدون مشکلی وارد بنادر شدند و خارج شدند و این تعهد {آمریکا به رفع محاصره} شروع شد. تعهدات ما پس از امضای این سند شروع خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/660631" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660630">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
بقایی: با عمان تا حدود زیادی به سازوکار مشخص درباره تنگه هرمز با حفظ حاکمیت ایران رسیده‌ایم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/660630" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660629">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
بقایی: تصمیم داریم برای اطمینان از تردد ایمن کشتی‌ها تدابیری اتخاذ کنیم قاعدتا خدماتی ارائه خواهیم داد و هزینه‌اش دریافت خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/660629" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660628">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
بقایی: ما برای دهه‌ها نگهبان تنگه هرمز بودیم اما سواستفاده شد و ایران طبق حقوق بین‌الملل تدابیری اتخاذ کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/660628" target="_blank">📅 01:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660627">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
موشک‌های ایران فقط برای شلیک شدن هستند نه برای مذاکره
بقایی، سخنگوی وزارت خارجه:
🔹
موشک‌های ما اصلاً دوست ندارند که کسی درباره‌شان حرف بزند.
🔹
موشک‌های ایران فقط برای شلیک شدن هستند نه برای مذاکره.
🔹
درباره توانایی دفاعی ایران در هیچ روندی و با هیچ طرفی صحبت نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660627" target="_blank">📅 01:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660626">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: قرار بود طی ۳۰ روز محاصره برداشته شود و متقابلاً ایران هم درباره تنگه هرمز این کار را انجام دهیم. اما بعد از تحولات مربوط به حمله رژیم صهیونیستی به ضاحیه و تهدیدات جدی که از سوی ایران انجام گرفت، مذاکرات فوری انجام گرفت و قرار شد آمریکا تعهداتش را فوری انجام دهد
🔹
در رصدی که انجام شد مشخص شد کشتی‌های ما بدون مشکلی وارد بنادر شدند و خارج شدند و این تعهد {آمریکا به رفع محاصره} شروع شد. تعهدات ما ‍بس از امضای این سند شروع خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660626" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660625">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
متن فارسی تفاهمنامه نیز به عنوان سند رسمی به امضای ایران و آمریکا رسیده است
🔹
با پیگیری و پافشاری ایران، متن فارسی تفاهمنامه اسلام آباد میان ایران و آمریکا نیز به عنوان یک سند رسمی به امضای دو طرف آمریکا و ایران رسیده است. /تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660625" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660624">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUIS4aPCK7HlgE1womJNvZZ6MdTOcnJfgBVf58khcYxTe0kHcQWzjE4BrreSasJFprrmbkbTSl-1wAcVXeQa8xBr-KAysR2dBnWFUp3Fp21jh_VRxiQuydrJr1kFQ2ncJexbic6i2ZVT6xqW1xfqydqEZJTfLylqlbiuV8yHiTdbA9Fh0CsY-ElRvT6_C6wXa-FRs5YrnH9XsVHBl1Uv7WFM8rPHBHwKHWv3z4_NdAYm84h6LVhYqtezkGuGKcY_504eZ_fL4sIaX_aKfOp0or3CJd7nQmgPWXWqdxRCbd8bHBGCr2MYcjoNCfXUErskplhyVb0-z-ncQcCSLFMvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن امضای تفاهم‌نامه با ایران را تایید کرد
🔹
دو مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفتند که واشنگتن و تهران، یادداشت تفاهم برای پایان جنگ را امضا کرده و اکنون اجرایی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/660624" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660623">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: تصمیم حکیمانه جمهوری اسلامی این بود که در این مرحله درباره موضوع هسته‌ای مذاکره نکنیم. قرار شد تمرکز بر خاتمه جنگ باشد و این کار را انجام دادیم
🔹
از زمان اجرای تفاهمنامه، که الان است، ظرف ۶۰ روز درباره موضوع هسته‌ای و تحریم‌ها مذاکره کنیم. اگر زودتر هم مذاکره به نتیجه برسد، بهتر است. ولی با توجه به پیچیدگی موضوع، عدد 60 روز منطقی است  و اگر لازم باشد، این زمان تمدید می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/660623" target="_blank">📅 00:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660622">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
متن کامل تفاهم نامه ایران و آمریکا منتشر شد
👇
khabarfoori.com/fa/tiny/news-3223896
🔹
فاجعه اختلال بانکی / در این بانکها پول نگه ندارید!
👇
khabarfoori.com/fa/tiny/news-3223880
🔹
پزشکیان و ترامپ، جمعه تفاهمنامه را امضا می کنند؟
👇
khabarfoori.com/fa/tiny/news-3223875
🔹
حماس با تحویل سلاح خود موافقت کرد
👇
khabarfoori.com/fa/tiny/news-3223690
🔹
تصویری از همسر زیبای نیمار
👇
khabarfoori.com/fa/tiny/news-3223828
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660622" target="_blank">📅 00:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660618">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
بقایی: تفاهمنامه ایران و آمریکا قرار شد که به صورت دیجیتال امضا شود
🔹
وقتی تفاهمنامه به امضای روسای جمهور دو کشور برسد نقض آن هزینه بیشتری خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/660618" target="_blank">📅 00:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660617">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: کار ما پایان نیافته بلکه کار تازه آغاز شده است. هم باید مراقب اجرای آن توسط طرف مقابل باشیم. و هم درباره موضوع هسته‌ای و رفع تحریم‌ها مذاکره کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/660617" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660616">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بقایی، سخنگوی وزارت خارجه: اینکه در این مرحله یک توافق خاتمه جنگ را امضا کرده‌ایم به این معنا نیست که گذشته را فراموش کرده باشیم و درسهایی که به بهای گزاف آموخته‌ایم را از یاد برده باشیم.
🔹
الان کار ما سخت‌تر از قبل است؛ چون همیشه اجرای توافقهای بین المللی…</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660616" target="_blank">📅 00:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660615">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بقایی: الان اگر متن را مرور کنیم خواهیم دید که چیز ناگفته‌ای را در این مدت نداشته‌ایم؛ همه موارد را کم و بیش بیان کرده‌ بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660615" target="_blank">📅 00:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660614">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بقایی: الان اگر متن را مرور کنیم خواهیم دید که چیز ناگفته‌ای را در این مدت نداشته‌ایم؛ همه موارد را کم و بیش بیان کرده‌ بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660614" target="_blank">📅 00:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660613">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
بقایی: تا این لحظه برنامه حضور تیم‌های مذاکره کننده در ژنو پابرجاست اما امضای تفاهمنامه به صورت دیجیتالی بوده و مراسم امضایی در سوئیس برگزار نخواهد شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660613" target="_blank">📅 00:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660611">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: جمهوری اسلامی ایران نشان داد که دوستانش را در هیچ شرایطی تنها نمی‌گذارد. برای ما آتش بس و خاتمه جنگ در لبنان به اندازه ایران اهمیت داشت و دارد. در بند اول یادداشت تفاهم، سه بار نام لبنان آمده است. احترام به تمامیت سرزمینی و حاکمیت ملی لبنان آمده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/660611" target="_blank">📅 00:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660610">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd6ca52db.mp4?token=Llqr8k4wrYKWAZl_68uPxhUNjn9vCMDtZibGJ-ZE8h-CmmTQeUpWGzccjvN-BJswk76FHb6Qe44PDhKp6gXymKq8VjyK1rOJk0fFjuYj0qRjjYhcZCKXt26q5OI45O3lav8u0En7HJ6pDOROwE6_seUBct5rA29b5bUQkNirU2BfKtrjsxphJZh40TD802gVmdRsvaf0b1mHWLQckrJwDx3vxIyaNmCU-LQnHIg_S3Ifgu6j9kR9dyd9P4MuhFzFAkpQOwUcDev8U1zdt-4ktuZ1YRujyNVKITJgy3XW0cszZ2OAl9pto9MjSoMKOVY2HfEfkCpegqlMgGOWG6LexA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd6ca52db.mp4?token=Llqr8k4wrYKWAZl_68uPxhUNjn9vCMDtZibGJ-ZE8h-CmmTQeUpWGzccjvN-BJswk76FHb6Qe44PDhKp6gXymKq8VjyK1rOJk0fFjuYj0qRjjYhcZCKXt26q5OI45O3lav8u0En7HJ6pDOROwE6_seUBct5rA29b5bUQkNirU2BfKtrjsxphJZh40TD802gVmdRsvaf0b1mHWLQckrJwDx3vxIyaNmCU-LQnHIg_S3Ifgu6j9kR9dyd9P4MuhFzFAkpQOwUcDev8U1zdt-4ktuZ1YRujyNVKITJgy3XW0cszZ2OAl9pto9MjSoMKOVY2HfEfkCpegqlMgGOWG6LexA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقایی: همین الان که در حال صحبت هستیم متن توافق رسما به امضا رئیس جمهور های دو طرف رسیده است
🔹
قرار بود که بامداد روز ۲۸ خرداد ماه رئیس جمهور دو کشور این متن و توافق رو امضا کنند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/660610" target="_blank">📅 00:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660609">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه درباره تفاهم نامه ایران و آمریکا: متن تفاهمنامه ایران و آمریکا الان رسماً نهایی شده است چرا که دو طرف آن را امضا کرده‌اند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660609" target="_blank">📅 00:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660608">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d1114b63.mp4?token=gKgX6juhCQac0eDPZ3QJ5MaOqKkf82WUMhmlFNMvOs2aOPivH9aULtt78yWMy2C5VHWcE-MehebUD-sEvcpmu2dQgURe9wLj8QSE5G1O14OFB20xCqUaCLNfgl4WLRcgvPk-u8SZLtMfKOC_CeeEonRj7Dnar6T4xqOkl2mqg-jhdM7lsijHOL1WNrLY3tK1s-x2-cKvy-PDdGqT6dSlkM6I85sZHpeTB9bu_o0vAa0ECtmDWfw7STk0NBjzcx2h0XHeAkNT38XJxSt9o910VvWnkbluirmgqCu2y5KXmvu7Tf2xkuqws97uH-Z7d6_GftzPSdBdZQOojxtuSOxNxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d1114b63.mp4?token=gKgX6juhCQac0eDPZ3QJ5MaOqKkf82WUMhmlFNMvOs2aOPivH9aULtt78yWMy2C5VHWcE-MehebUD-sEvcpmu2dQgURe9wLj8QSE5G1O14OFB20xCqUaCLNfgl4WLRcgvPk-u8SZLtMfKOC_CeeEonRj7Dnar6T4xqOkl2mqg-jhdM7lsijHOL1WNrLY3tK1s-x2-cKvy-PDdGqT6dSlkM6I85sZHpeTB9bu_o0vAa0ECtmDWfw7STk0NBjzcx2h0XHeAkNT38XJxSt9o910VvWnkbluirmgqCu2y5KXmvu7Tf2xkuqws97uH-Z7d6_GftzPSdBdZQOojxtuSOxNxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم انگلیس به کرواسی توسط بلینگام
🔹
انگلیس ۳ - ۲ کرواسی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/660608" target="_blank">📅 00:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660607">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
داسیلوا: ترامپ در انتخابات برزیل دخالت نکند
🔹
رئیس جمهور برزیل در جریان یک کنفرانس مطبوعاتی در واکنش به اظهارات ترامپ که پیش‌تر برزیل را خطرناک و از نظر سیاسی ناخوشایند خوانده بود، گفت که از ترامپ می‌خواهم که در انتخابات برزیل دخالت نکند، همانطور که برزیل به دنبال دخالت در فرآیندهای انتخاباتی آمریکا نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/660607" target="_blank">📅 00:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660606">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2vsdU1ozQ29OSqM9Zgq75xVl7Unv6LZA9e85yVkg-Z0xpWGOsHasG6OM6Z8GFEWxlQia1rd2n2osiOCifFK0kfOr0EPLXaM6FO-mzhAOLK6GKwCmBY_PHTcUmmjQcwNazsdgrffwnPDMA4_Jgv1WqzvW820oZjy9z6NA4AtM4JZ-qbg1ZFPNtne7Vpcvm1TAgga1vmOI_wP62QVPtnvJBs_By_FFjAmNmjCieiNv2Yd7vobFX4P35JxCi4MYRhnTCzdQK65GMje2a4ADjASXobP6lfX14OFNiWB6e1HCQ8M127ch-pdHF2uQmZYbUKJEnNXgPAe3PlUChtkQMxUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در
#شب_سوم
محرم، شبی که به نام نازدانه‌ی اباعبدالله، حضرت رقیه (س) گره خورده است
✨
امشب یادمان می‌آید که آسمان، جایگاه فرشته‌هایی است که زود پرواز کردند. به یاد شهیده  خردسال
«آوینا برزگر»
عزیز؛  باشیم که امروز او در میان پروانه‌ها، مهمان سفره‌ی حضرت رقیه (س) هست .
🕊️
@Heyate_gharar</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/660606" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660605">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ff0adc2d.mp4?token=d6haNlPYugQBop1ARXiXQiofyVB1bufM20uJFseiCDaO_XrdnEjCfnw0y10ppe36GeyaNUewEnSI06y42zufFSa7Y9_RXuj5N8G-bJ_eWgpqNpb3y4xFS2qPRQAgx4Tq7gL9ebUqp6cL8znPdgmP4zwcVkxM4ib_F1p-nwtiprN2UZE0Y_OBa-Tin22xwK0FxJyF4xfOeHbZOel_JAARRCSVAfjKLzHvE-kd4sSjCWSheoY_rDfVu4fj1m6OvCCciO7tigBppkBhDVP1vHIwiEPkb6ug1e__qrQotRy7_aqHAY2iXfbx7cHvyaAZd4IjXAnNTFgP3rGsIBwztep55w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ff0adc2d.mp4?token=d6haNlPYugQBop1ARXiXQiofyVB1bufM20uJFseiCDaO_XrdnEjCfnw0y10ppe36GeyaNUewEnSI06y42zufFSa7Y9_RXuj5N8G-bJ_eWgpqNpb3y4xFS2qPRQAgx4Tq7gL9ebUqp6cL8znPdgmP4zwcVkxM4ib_F1p-nwtiprN2UZE0Y_OBa-Tin22xwK0FxJyF4xfOeHbZOel_JAARRCSVAfjKLzHvE-kd4sSjCWSheoY_rDfVu4fj1m6OvCCciO7tigBppkBhDVP1vHIwiEPkb6ug1e__qrQotRy7_aqHAY2iXfbx7cHvyaAZd4IjXAnNTFgP3rGsIBwztep55w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدباقر قالیباف: خون‌خواهی رهبر شهید آزادی قدس است؛ ۱۰۰ نتانیاهو بند کفش امام شهید ما هم نمی‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660605" target="_blank">📅 00:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660604">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acmgtQlKL7J49UA3kp7IzKrH_coIdLxr2VgJ7zkhcqkKAk51N_KbUQJgJx2zHWbTAjiRMh_DVF9Ty2VfOjC6T0Jj9Ar_719YDZ5aiQqJBT786hxwX_dU8LcF63WzQoI0hnk4d7AY2Zxry_oFQXapciE6XQiEWHrLaRadcLH2F4iu6oRpz9ECFD8GFNnIoKF_dtaYkqGoURvdzZpbzN3J_oWayA7TpWKmKp57jPOVXtEZ3dIDBZZuiVCuhJEI6W2LmdTMjhCz9x_fpFpjdXvb_T81Dk0D38K_9VMvEDle_5MyLKzgznpypY10IkWlvBq0sxEx_XXAe9dNcuZBgHVpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری کمتر‌دیده‌شده از شهید سپهبد علی شادمانی در دیدار با فرمانده شهید کل قوا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660604" target="_blank">📅 00:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660603">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ed067d22.mp4?token=qxjWHvHn0pjALXU06sbaQzdqKuItuv-DxRk9O3FOxlWFNabkEaiey1Yo7yPYZyBUqvu1FnpnwSPwxVtfIu9UGAcboJH-kI-SC1uVOVXoyM4Dt63N8AXPoyPGhg_1xgoH6U38ueojo1PeAV0nftZTEg5h1I0jYyFsb6M2HEdhgoVJBkeUaim-PwHJLSKGPjhJ3Z78EEjkqg7NMYPYX53qPwjA5v3fATm_R_IyPKfiW5ZyOtbsX8THEt6Sb_2x_dRl-buCWUZ9nMPnuOdUbV6sNWOHl4ucqc1EpcVloCdYNpY-SeTIrv3LwqSJdUuouqJoT7WIROfMHX9GjOCCo5Uzsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ed067d22.mp4?token=qxjWHvHn0pjALXU06sbaQzdqKuItuv-DxRk9O3FOxlWFNabkEaiey1Yo7yPYZyBUqvu1FnpnwSPwxVtfIu9UGAcboJH-kI-SC1uVOVXoyM4Dt63N8AXPoyPGhg_1xgoH6U38ueojo1PeAV0nftZTEg5h1I0jYyFsb6M2HEdhgoVJBkeUaim-PwHJLSKGPjhJ3Z78EEjkqg7NMYPYX53qPwjA5v3fATm_R_IyPKfiW5ZyOtbsX8THEt6Sb_2x_dRl-buCWUZ9nMPnuOdUbV6sNWOHl4ucqc1EpcVloCdYNpY-SeTIrv3LwqSJdUuouqJoT7WIROfMHX9GjOCCo5Uzsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم کرواسی به انگلیس توسط موسی ۵+۴۵
🔹
انگلیس ۲ ــ ۲ کرواسی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660603" target="_blank">📅 00:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660602">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28df5a9b7c.mp4?token=M4JjW_LnJOsGEeMCFEG8ToZqOp6C3WMwZxNJIlegeGbwaFGtSO6e6ICtb2vj7rig9v5S5SvVeqy8kGUZz6pPZbfHkpZbtKttYfzdKxafIXW_2fX7zx--7vobTFyKkP_-O2MQlYA1-I6UqRiVTuSr93NAIR7ge_QZPo7zoorxfnqRuP-a5Qv2qFLsu_uICEL6Yne9fCGSJesBS63FlLPhLgucDMFVSj8_PshGI5zUrMOG6uxRqH25uQl-uE1aP8EgV--k4UX4eG0BM4CyS8SCH_tls2Aic_WCEg5AAYR7EI-ZVJtzUvd1J8sFGN06GKr0xHs9CMkf9_UIoDWWMojY0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28df5a9b7c.mp4?token=M4JjW_LnJOsGEeMCFEG8ToZqOp6C3WMwZxNJIlegeGbwaFGtSO6e6ICtb2vj7rig9v5S5SvVeqy8kGUZz6pPZbfHkpZbtKttYfzdKxafIXW_2fX7zx--7vobTFyKkP_-O2MQlYA1-I6UqRiVTuSr93NAIR7ge_QZPo7zoorxfnqRuP-a5Qv2qFLsu_uICEL6Yne9fCGSJesBS63FlLPhLgucDMFVSj8_PshGI5zUrMOG6uxRqH25uQl-uE1aP8EgV--k4UX4eG0BM4CyS8SCH_tls2Aic_WCEg5AAYR7EI-ZVJtzUvd1J8sFGN06GKr0xHs9CMkf9_UIoDWWMojY0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه سر زیبا، کین بار دیگر انگلیس را پیش انداخت
🔹
انگلیس ۲ - ۱ کرواسی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660602" target="_blank">📅 00:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660601">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
روایت خلبانان جنگنده های F۵ ایران که پایگاه های امریکا در کویت را هدف قرار دادند
🔹
این‌قدر پایین پرواز می‌کردیم که از بین دو تا کشتی عبور کردیم؛ عرشه‌شان از ما بالاتر بود؛ یعنی ملوان‌ها از عرشه ما را نگاه می‌کرد
🔹
هواپیماهای کویتی به اشتباه سه جنگنده امریکایی را که قصد حمله به ایران را داشتند به جای ما مورد هدف قرار دادند
🔹
هیچ فیلم و عکسی نگرفتیم؛ اصلاً فکر نمی‌کردیم، برگردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660601" target="_blank">📅 00:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660600">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvtjDYC1j9NRDT579odyqCgMC4FfCAxlKgzdam_JxWxvy_l2hr6rvleiOdIDk4HXCNALpgTf71MeDiYePG0Ap6dxxUgVygMdZahRecZ7zbOpDNpMGknZU4l7UO-txntPCFt5EHNhfijkOsqsU2IPn-dJfGNrkXuCtRFOdPTkR_vKuSvIRxiJugHLRs4xdauMdjgS2uP42MeXoByT8WgbXsO9A5Ycu90-q77LHOeK08bjmwg_yOiyKkZ_uW7hnvd_r47Wq8g6NXGYwQAmt--1zR0rOefQR2CHDBrFJ541M2PttKc4CgzD4K3ru0NtSifkdaNuG3yxC_GyM_TSjBacxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برتری سرمایه انسانی در ادراک عمومی
🔸
در این نظرسنجی بیش از ۴۱ هزار نفر شرکت کردند که سهم روبیکا حدود ۶۴٪، بله ۲۶٪ و تلگرام ۱۰٪ بوده است.
🔸
حدود دو سوم شرکت‌کنندگان مردم و سرمایه انسانی و حدود ۱۱٪ هم موقعیت ژئوپولیتیک را مهم‌ترین سرمایه ایران می‌دانند.
🔸
در نگاه عمومی، سرمایه انسانی و جایگاه ژئوپولیتیک مهم‌ترین دارایی‌های کشور تلقی می‌شوند و این برداشت بیشتر از تجربه زیسته مردم و ارزیابی عملی آن‌ها از ظرفیت‌های ملی شکل گرفته است.
@amarfact</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660600" target="_blank">📅 00:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660599">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe26318adc.mp4?token=D-36qnPU7ep7VDqPjjlzxUyB8nOIci8PNCjKNvH0WPnYGZa-ILbhp_Fj1p7wUDlHRNE0i3-OvVnIJ7sfTKLinrlIoqi-o8Ooqv_pG39e6sJFcz1uc-s9ll6GFj6pfYbvlly_B5YTwLX2VAK4Ukf5hLEbj9JfK98a-PqSMztrLvrm-GGr88M1UUZG3kYYm7cAhMUFJidxHz9hTU-wPruN0DqGcVcHPZ1EY5Pu7DA1FMDrMpUzVGtq0_YckAdadar2iSHzobDpQZxDDQX8EtFboKcM_8KwPIyB27izXeHJU_M--h1GpXehXxe-Ol2NpWAL6Kjhsnl4KP4V0URUXde4D2plA06ukGTl-m25TTbr_G7cRjxf76Y5Ukck25zUs1AHjfZrjyZiqm8gGSFWUfMfuwMnzsj39aDZ0hCyAp8NzDaH5zM7w-OlvjmyZe7sPtr2mGMfXH5HNt7Dx_dwKw_kDOapQNZTdsVUB3HhnB2nXS-5BsfdzQPgImtnRB3hMimHd5s3eHOISN-FP3f2v7PX0Dv0L3PJBQAMK6ZEtexv8wKQH7gW7qzI8Wz9Al9m1z09eL14Wxfzl7Nnz1OducnA8DzzP5WnsPJ6wohqC9yUoy-UhAtjGzdGtm7jk-ZMhaFg3bOKpDkdlMQDY6aaeXU_UbTZgziZQbJA0S--sM9lsPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe26318adc.mp4?token=D-36qnPU7ep7VDqPjjlzxUyB8nOIci8PNCjKNvH0WPnYGZa-ILbhp_Fj1p7wUDlHRNE0i3-OvVnIJ7sfTKLinrlIoqi-o8Ooqv_pG39e6sJFcz1uc-s9ll6GFj6pfYbvlly_B5YTwLX2VAK4Ukf5hLEbj9JfK98a-PqSMztrLvrm-GGr88M1UUZG3kYYm7cAhMUFJidxHz9hTU-wPruN0DqGcVcHPZ1EY5Pu7DA1FMDrMpUzVGtq0_YckAdadar2iSHzobDpQZxDDQX8EtFboKcM_8KwPIyB27izXeHJU_M--h1GpXehXxe-Ol2NpWAL6Kjhsnl4KP4V0URUXde4D2plA06ukGTl-m25TTbr_G7cRjxf76Y5Ukck25zUs1AHjfZrjyZiqm8gGSFWUfMfuwMnzsj39aDZ0hCyAp8NzDaH5zM7w-OlvjmyZe7sPtr2mGMfXH5HNt7Dx_dwKw_kDOapQNZTdsVUB3HhnB2nXS-5BsfdzQPgImtnRB3hMimHd5s3eHOISN-FP3f2v7PX0Dv0L3PJBQAMK6ZEtexv8wKQH7gW7qzI8Wz9Al9m1z09eL14Wxfzl7Nnz1OducnA8DzzP5WnsPJ6wohqC9yUoy-UhAtjGzdGtm7jk-ZMhaFg3bOKpDkdlMQDY6aaeXU_UbTZgziZQbJA0S--sM9lsPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: انتقادات به‌جا و حتی برخی انتقادات نابه‌جای مردم نسبت به مذاکرات را به جان می‌خریم و از ملت تشکر می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660599" target="_blank">📅 00:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660598">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
قالیباف: پرداخت هزینه خدمات عبور از تنگه هرمز در تفاهم‌نامه تثبیت شده است
🔹
کشورهای ساحلی تنگه ها در قوانین بین المللی حقوق و وظایفی دارند از جمله این که دیگران باید هزینه خدمات شان را پرداخت کنند.
🔹
دشمنان ایران را خدا از احمق ها آفریده و باعث شدند ظرفیت…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/660598" target="_blank">📅 00:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660597">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6wpKc3HADIVdhhjD13PyeNIzp0CNRocCdYr8hvDsnry_fQLXUY5SrDpdbL3y6c6WIkuqy6DXzczwHSZv5oiuKWlvIZUCSRUGtmhx4pl8juBq2JtHtP1dWtEbJFXbi6AU_66LZZ056t-M40xLeKcmZTmlGpgO2SOVjhWeQZBR3ni4obelR8KYVD0Cw9TtnkoXqrsy-oNQWWwGfdGSm1R5UWHAS_62C3oF3Ndhzx9YzMGSdYgljneIl4n-nEBmQPN8HnBJOxpwzgLOTuMfVztmGRPX9S4wlLi3prGy6_Y2bR8-A2PjAc5ENdXfUfSNcvC4KhxnQAuJ4XjaYD-PD6CpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا استفاده از مایکروویو برای سلامتی مضر است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660597" target="_blank">📅 00:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660596">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf4812f88.mp4?token=cwj0IuKEOq-BCT4g8L-UNtL7SP3tBIVEkF_Asoq1iNgEGP3fewjW0hwfUq6K1tf-liLqoEHcyPD-AesmN1M3asdxdbhNEX3XsMxCTgquehbkV4VOHE6K3vr8MmJbAWU2RVvrsMYkmqaYDxpqUddfe_vXM-wbOVZ0t_b4_RgSL_HERaI2erzYE0R7D5L0r6Q5BVvv3fXa4GT0QwCarGB_X6BvwmASAXoEn9uYwXwP7HKzGAiUGR_Z367QP_z_QeYNtqYYT9fCpHiWButM1k7H3jhlq9lhxmar0e-luDpcU_ma6ybVNUa2cK7xuKb_JGvPStqwq7G4LgV05bnP1xYBBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf4812f88.mp4?token=cwj0IuKEOq-BCT4g8L-UNtL7SP3tBIVEkF_Asoq1iNgEGP3fewjW0hwfUq6K1tf-liLqoEHcyPD-AesmN1M3asdxdbhNEX3XsMxCTgquehbkV4VOHE6K3vr8MmJbAWU2RVvrsMYkmqaYDxpqUddfe_vXM-wbOVZ0t_b4_RgSL_HERaI2erzYE0R7D5L0r6Q5BVvv3fXa4GT0QwCarGB_X6BvwmASAXoEn9uYwXwP7HKzGAiUGR_Z367QP_z_QeYNtqYYT9fCpHiWButM1k7H3jhlq9lhxmar0e-luDpcU_ma6ybVNUa2cK7xuKb_JGvPStqwq7G4LgV05bnP1xYBBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوپر گل مارتین باتورینا به انگلیس در دقیقه ۳۶
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660596" target="_blank">📅 00:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660595">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtoBBmx0nDet6jr9jHWJ3WbeCCioTR9FtbRJWEvvXlybeA2GPjX_xUbORerWa7FEtwO5FWQ2W7kdRtJ2t_K9Q3dn58Rpz-zjKshNRoGO3T2wkc5zCfH9_ikWFuiGzbevTHIpGjze8qRDClnMcWjMXrI5ffOlXdCv8thFUKtP-l4Pnp4NVEWtH3PNZsK-mERTqRKvrlx1GQOux1xc_y7Ol_OrQhLDTl6WRFQ-ixld1-Vxp4C82LZkWIMjNV4bRe5W4opjawIUzyKrLMfvbJdDyir66SZ0Sb5E3_IrMuDQKlit54h3zhwx3SJKnwFg6P0fbl-SVHkhy9DK_5FcgjMaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله صهیونیست‌ها به جنوب لبنان با بمب‌های فسفری
🔹
رسانه‌های لبنانی گزارش دادند که ارتش رژیم صهیونیستی به شدت ارتفاعات علی الطاهر مشرف به شهر النبطیه را با گلوله‌های توپخانه و بمب‌های فسفری آماج حملات وحشیانه خود قرار داده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660595" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660594">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a21e6cec.mp4?token=Sof23oDFZDnFDJ27FN1Mxehmmj6YJK7yWnFtCdOLu4S9BIB3SFCj1XSqGHhPXWmLbaFzRTk3Ty0nP0g3U3hSclncuOJkEGN0SVY8pAAUN6lVAmf0BkxkPKb5A-tlSA2Yi_p4vzsCZdz3SVEvJaW18Q7-cZvXCAR8EDopl_tI2wps8SrPdtNpkDZtQe0hPeBGb06A71mEamxO2hUlV-EuibGyM7FEsAk0rhe-RSWx3_-JTlQMk0WB4k4hBcu5Z_UuckiQFEzcTIHykyPnsbRIM_0ngW9JFvJM7fJPJxiHKKi8UGqo9ZiOp1GgtW5TAEVGtYpyxc8HX0uGXxXrU4kf4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a21e6cec.mp4?token=Sof23oDFZDnFDJ27FN1Mxehmmj6YJK7yWnFtCdOLu4S9BIB3SFCj1XSqGHhPXWmLbaFzRTk3Ty0nP0g3U3hSclncuOJkEGN0SVY8pAAUN6lVAmf0BkxkPKb5A-tlSA2Yi_p4vzsCZdz3SVEvJaW18Q7-cZvXCAR8EDopl_tI2wps8SrPdtNpkDZtQe0hPeBGb06A71mEamxO2hUlV-EuibGyM7FEsAk0rhe-RSWx3_-JTlQMk0WB4k4hBcu5Z_UuckiQFEzcTIHykyPnsbRIM_0ngW9JFvJM7fJPJxiHKKi8UGqo9ZiOp1GgtW5TAEVGtYpyxc8HX0uGXxXrU4kf4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از یه ربات انسان نما چینی که کنار خیابونا میشینه و از مردم پولِ کمک جمع میکنه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660594" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660593">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d797efbe.mp4?token=h5iAEkgDZXbsJ2diO_3Fj4MTtInhFUx8HjP2gMbxXW3AsKMTQH4qDX_gAGssUSja9ieeq3nL_oLAm2z0Lj1daREcgN8hXQKrWlLzHu1PKPETvK9bqjLpMMI2-49_Crusy2H1YEUm8xtJx6tW7lr0SEAwE0FeXMtF6209rHsVO7n8rXbLfLKETZx8db4oCaMKANyrhTcx_SggmQszRLnMHqwK_AFwYvoRbkcpPvpUcPk3TFZcxbWo4qYwIQvBbYOlCSdMqAIqqsggl5BLiqsBUuUEjUJNEg5fpmdYkXydCPaseVCvglomd-XE5R2CZlsgx-kIzJIAJ2uGfRGeSWtC9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d797efbe.mp4?token=h5iAEkgDZXbsJ2diO_3Fj4MTtInhFUx8HjP2gMbxXW3AsKMTQH4qDX_gAGssUSja9ieeq3nL_oLAm2z0Lj1daREcgN8hXQKrWlLzHu1PKPETvK9bqjLpMMI2-49_Crusy2H1YEUm8xtJx6tW7lr0SEAwE0FeXMtF6209rHsVO7n8rXbLfLKETZx8db4oCaMKANyrhTcx_SggmQszRLnMHqwK_AFwYvoRbkcpPvpUcPk3TFZcxbWo4qYwIQvBbYOlCSdMqAIqqsggl5BLiqsBUuUEjUJNEg5fpmdYkXydCPaseVCvglomd-XE5R2CZlsgx-kIzJIAJ2uGfRGeSWtC9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: هرجا دشمن به تعهداتی که داده عمل نکند شمشیر ما موجود است و با منطق قدرت به او خواهیم فهماند
🔹
من دیپلمات نیستم اما خوب بلد هستم به آمریکا تفهیم کنم که باید چه کار کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660593" target="_blank">📅 00:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660592">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
قالیباف: مدیریت تنگه هرمز را براساس قوانین بین‌المللی پیش می‌بریم
🔹
براساس این قوانین ما حق داریم هزینۀ خدمات در تنگه هرمز را دریافت کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660592" target="_blank">📅 00:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b75MqjNyKmz7_sx-qJgS1rRIuLroGy61H8yvMA8YomQwDnZ33Cqi-p9fssh5ZM3pUbgmUiUU7ZNjOq4BebaXx0PLWPoEsQ3AVDCJsbSKjmuXbbn2OTBdpVKy6F6VawFEP3e5SW-T006WSNsty9ziGW--TbvjOPmKIrGBXJb5nOd03fWX-_yUvOiY7ODTKDSbAce6CFtRCB-1iYMV5YI3LCCb9EtI8QI-JUc6Lkw5zLJjrN4wCGwKKNJFRwKZYrrI6ae5cg1FW05HB4J3LrojK7U1A72K4tDNv-Ob_OzaBOWNePMTeajmhlVAoijYK2gxeBpVGNu7Hgo9n9l2OX_L9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaoMGNB9BFuXyjkP_9XDEXD4unWTFOYcAnElkiT0s-uZBCMBjgKBlML5kyz4AwbGVBprG01vhtYsm5U2pjgfPUJpSasNZn3aLntur57Buw3a7B_z1xTaebpny2J109SG4yQfXuNZDPhyBfEG8S3yufVIMvPSqZvw8CJYRXp2JVRbl6dX0ufkNk0XJ4wY5gptZgejl7fA9ejZ8TIqj4X5IiKq4DNVGZoMNOeY_d7GtHFO5cUngX1DslTy8D45bdM4R73nM6IwmLWuADVLiSHfYsdYOrTYeEAtgmSMvWVDXXnRrIQrolmefskIYIqLC1JjtFO_A9w_4eTtQ9y68hyyYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4TxoNMIFJxNvP_rN1PWJfOA3HuIbtMyzNwRMxrDFFX_Wi01N6NybhXfT__NS1heAA0l4cf7VM2ZIC5pdDtXAUP9v47aS6BZDCsYwFbEAq1oJ4RozB5QkcFVVYr4-6zbWVt2qFRAGVUuYyVGUcIvHgVOKvPL3Vxdg8bv6O6d0_xsCLMzhLq3-fTrh01wHAQZBJtzn-1mmzdgrwJ84_ByH3idr-l44A2trHHXhzTlaNRt6bdu2g1E34lW-X4gcEQptomiid0SttUk90FmF0vsfr8dsjli3M4uLHp4lge36X3WdN3ZLuqvfscccjfWdGNv3GIWcVW0f1Li5Ls1zQ3PjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnF5RplNBGjev_EXqh55jWOl2zzh4tGNRhCVLvw4Js7_IfcZHCEw3SFDgYaNutXkiQ0QvPyECHrX7eUhhGbd87B1Df6dlScXmzXgF_bAOgjhmJoWC6aRaG4q3raLnlBYUPcf5FUVzIMEKQ-OvTjje79SG9ifuM8HKqym18qhvvCj8puq3mc775jlCcC22cyqX020Kmdx7A2CRp8PKchfMTZzM6Sga6LCfaNleLLEIEEfngt_eSSAZA_inDhcsytDpiKFcQh7AGCvxyT-6k44oNDYAuY_aVZPsUWdeYe9-lgg5YfZ3Z61irQGLvNPElsEqZy9pCgX5-VwVgvLVtDU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k45Hw89sDYYvPZJ4zFlokw1JRkfQePoYcmomJSfKfq32ouVZcOrr90rMzhp2PoGhsWv5vTUn3e5NpqVlMS2ZDuasvBkLpJlri-2wmrJEvyzlTd4Yrv-wijgKlFrKyax2pOwpXCFi4SmxDtOSiGSHuGEIuc4XVfJetH_yTzkz_DkujLDkFgZ1QKm8ozbJzSb2ct5orVDj20a5YHAoQRckOAGpzVPaXfEriigiAHc41e1uolNOhnk1TaSoH7NVstOok8Gkay54bPJ0bbjcUEe-4iz9T_fJWLcmXbBBKWjbjJnLryLVQKgleR2jgiUSZifTMvSIcGtyOB2MsREExSMcMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SudorTki_IB6JVrWffzuvKT4ztJknQhhDaDGZonFjLHVCrX3sfen2K9gTyQn-lYPXvzVFLf4VPNFuaw1L6Nd9CB2ksd0rmEB-95m7rSVbTDoVz_FKcVvXa-ob_rzcpmPPhttHOY8KnSm-EBYDBIvL4vF-MtVRtsjovPvDPTMRX_WjSqnBClbV8cATEI9lhjxVMNMrzlDIw9Afn89tRNoINuDKkZ2VwalKItAndYYlgjF2-HhDFhaaOSVKQU7oZI4pxE24nFYxAZjXsLFEt8WLJ5KiBWFanq4FqTJeTt0J9AsAGge8udAQIykG9m5_39oZuK8KNipq3yy8bPz1MH0Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwZyBF0Y88T5VSO60tOjCHVcTud6LYRP9rLcLNfYXC8WZh7O9fJgAzVcGwsDw5jbAcE7taV3NtOWRMBwB_yQiES-gj1wUE-l-SAX7iuTLkQaseqqE1QryskBY3We5p8VlZ1EVSUzVBnc9UvZG00sYoIbdnW7gPIcLEm1Wv5cho2FsnF0llCPsFA5n2NrFSn6rc0lLqeVsdGnrKa8VRiSqidDh4trjExeABGjKy3y_wtQa5NyzbbyfFcUPfwo6KaKH4ePfvaFp9TAAR4Z0zZjjVs7VCxDm5bVa9Flmmtm8uxV-6DWSZf3Kjg5MR2oBCmMldibGDRTXh0vfgdGNJKNOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ویژگی ها و احساساتی که در ابتدای عاشق شدن به وجود میاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660585" target="_blank">📅 00:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2_s0YlZei4sC920G--1hi7tPIAmhGQQFcMkGGgZlHZEpay1ce9soXHR1h3pe5FhzwP5anZJwnzAPYR44oxuBgnLRv5z7SfWx0WB33Dut0-4FV9VJpj161fRlcFn0_wiIPR5TqwSq-RFLn7Kd2skanP7HCVq5pYna1mI6VwvDFmskHSz6hvSgLGJ80rGwbd_Lko8vrmC6ZVe_jSe5cYinh40nIruuQALTgaIbizq4KCe-Z8KZ1RDRFlSSndr7990zXuUob8Fmf5c0p55EevigV3W1UZYESPTONAuaKyl8tX2MHMAXGKyHDPZia-H41jnIWCDHdW6GH-PQC5bdoDyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/660584" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تا ده‌ها ساعت تو مسیر بودند تا با اتوبوس و ماشین و شناور به محل کارشون برسند و بعضا تا سه هفته هم امکان برگشت به خونه نداشتند. بدون تعطیلی و بدون استراحت.
این فقط بخشی از جنگ و پشت صحنه‌ی تولید پایدار گاز در پارس جنوبیه...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660583" target="_blank">📅 23:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
قالیباف: بازهم تاکید می‌کنم که تنگه هرمز هرگز به شرایط قبل بازنمی‌گردد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660582" target="_blank">📅 23:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660581">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
قالیباف: ما دستمان روی ماشه است و اگر دشمن زبان منطق را نفهمد دوباره با زبان قدرت وارد می‌شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660581" target="_blank">📅 23:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660580">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
قالیباف: اکنون براساس تفاهم‌نامه، باید ابتدا بندهای ۴، ۵، ۱۰ و ۱۱ و اکنون تأکید می‌کنم بند ۱ نیز در اولویت اجرا قرار گیرد تا پس از آن وارد سایر بندهای تفاهم‌نامه شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660580" target="_blank">📅 23:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660579">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
قالیباف: قبل از مذاکرات اسلام آباد اعلام کردیم موضوع لبنان و آزادسازی پول های بلوکه شده باید محور مذاکرات باشد
🔹
ما چیزی به عنوان پیش‌شرط نداشتیم، هرچند ممکن است خواسته‌هایی داشته باشیم. البته به میانجی گفته بودیم که بحث آتش‌بس لبنان و آزادسازی پول‌های بلوکه‌شده،…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660579" target="_blank">📅 23:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
توضیحات قالیباف در مورد فرآیند مذاکرات اسلام آباد
🔹
طی ۲۴ ساعت ۳ دور مذاکرات با متن و ۳ دور مذاکرات سه جانبه با حضور میانجی برگزار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660578" target="_blank">📅 23:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e223f9d98c.mp4?token=kZzsZA3-bKLZuAhrILV0JoHMeP_aLh0zRg8pJ1zNbZkcxpSfNJWoW6HoiPSTIYeSKj1zWQ9xTyZXWoaT-ZxVIzxtDt43b0goLpInbMZUuSQHvkW9LHqeTSRCGVL1t0XObVoA7docUrtD-JZrk84DkTd5vw8ODzlwvjPrmJI6K0lR8Izg6WQau_Njbw1qzREoszgkyeNSTkkjhIj3-6X4k5QRYR9fjHgXNdA5EYGoJ8BGvVeHr5qqoC0s6_DmnE6L6AZIB7fdo_FAHHFX4NDNYEfNWsfu0noDCOSY5290uI1HKwX7qqGPntyM50-2Wqo7ee_buAKPrsryLvhmMJzO3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e223f9d98c.mp4?token=kZzsZA3-bKLZuAhrILV0JoHMeP_aLh0zRg8pJ1zNbZkcxpSfNJWoW6HoiPSTIYeSKj1zWQ9xTyZXWoaT-ZxVIzxtDt43b0goLpInbMZUuSQHvkW9LHqeTSRCGVL1t0XObVoA7docUrtD-JZrk84DkTd5vw8ODzlwvjPrmJI6K0lR8Izg6WQau_Njbw1qzREoszgkyeNSTkkjhIj3-6X4k5QRYR9fjHgXNdA5EYGoJ8BGvVeHr5qqoC0s6_DmnE6L6AZIB7fdo_FAHHFX4NDNYEfNWsfu0noDCOSY5290uI1HKwX7qqGPntyM50-2Wqo7ee_buAKPrsryLvhmMJzO3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول انگلیس به کرواسی/ هری کین با تکرار پنالتی گل زد
🤩
🤩
🤩
🤩
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660577" target="_blank">📅 23:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660576">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
قالیباف: من برای پذیرش حضور در تیم مذاکره‌کننده کراهت داشتم
🔹
من نه تنها داوطلب حضور در تیم مذاکره کننده نبودم بلکه کراهت هم داشتم و قبل از پذیرش مسئولیت مذاکرات من تمام تلاشم را کردم که این مسئولیت به من سپرده نشود.
🔹
یکی از دلایل من برای عدم پذیرش این…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660576" target="_blank">📅 23:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
قالیباف: در طول جنگ نمایندگان چند کشور اروپایی به ایران آمدند تا از ما خواهش کنند
🔹
همان کشورهای اروپایی که سپاه را در لیست تروریستی گذاشته بودند از مسیرهای زمینی به سختی به ایران آمدند تا با ما صحبت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660575" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
قالیباف: مهم‌ترین ضمانت برای تفاهم فقط قدرت ماست وگرنه دشمن قابل‌اعتماد نیست
🔹
ترامپ قطعنامه‌ رسمی سازمان ملل را جلوی چشمان همه پاره کرده پس به هیچ وجه قابل‌اعتماد نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660574" target="_blank">📅 23:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
قالیباف: من به‌عنوان خدمت‌گزار مردم به ملت عزیز می‌گویم که پس‌از پایان بحث مذاکرات و امضای تفاهم، اولویت ما میدان خدمت به مردم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660573" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTukM1FsteWwkPdKaezb6U_Kloxfa8vYPianomRpaifnuaWK9bOqCGC-9s9unJ1SuOohJ0Ktuo3D_3wmtnnOrTq3RzWESTEiAL9l0G_fde48dG77LUc-jK0AMOKjz3HN9V2gTsdorXEjUiNpzRvPac_mTXk_pikN7io-XeTUfb3aY-lA9phLvQOYB6bB1QQlt8XRqGn5v9tW1O4QDmh0MlEuuSxIto_paNaX5Fw1_a0O1zcHYuE8tli5Upe0DN5JxIiZ3_In-NkxRxnS5MHY61pHgLrpVw0GOqajsKL9y-7DcUbCgxERHzQrUmS3uEiq_SMRwqPQZRSsjSXLE9uDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1wu4fAfLYYXBzaUf6T2bmsyL64lBBgSJp4RI8I8Oy17115K19E_VamI5cJgTMAezg1NRBf_2kMLqlahMVQyT1y3D-osxoQHEiyHw26rBBXDG0ENkd0DiAZcF6-097gxeO-3_uCrU2d2-fkyfVNZqrvrqwZ4mQ63Edtc8DLu5Q9Ejf73NJ_V76VFB5ZfnUgBrBP-AabqPTJtV-r9wGohy4zMRrpBrhHrBKvdJ1O_AiifLG56urP8GIdvxzLYD6goW8RYTOuxGRT3wG5mdm_omxVbhK5ijwgx-ntXFXyNrOPUF2YaN3dzlEe47IJL4BATdKGQBCv3nxiCecmrGns_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIgrwNHrsh4s80YuUmNixeUAn-RZ95G3nplKvMwsZhecpQVbnENZf2Ywv4mS76QlEDI86Rsj32LRv0OkvxtiBZpSTPuAyNdcALADuR8-4jGUSzWMgBKtbz1hL50XR3c1PMD8J2kRa0KBTj0yLzV4cs9cYDTkPT4DiRKlv7gacTar-o7xX17Hhjobwd99mZz6_0avnaaZvFlo-E0RoVKYP_sKYHa9mqpDepRpYYOYRzyCAY0WQeA63UPWuX36nHcUtBl0052K9L57Wea-bEScR5BKUPNa2G6KHuVfB9y7NiWY2cJXB0StUqnaZPWaRmPj5c3C9Kz5JkrW4VRRKP3PBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmipZ0kEIWX10QNmG-ap_JUbUm-J7oseXit8qUzOgt2HMJ102dQBcAkV4se7XMOw5H7qadhBgGAek-nf2lQRBdVMoMCskviA-UyAiuJkbCF7la6t0aIoVlAc3ntOwAfMT5etiA54uAik-_QIPBQoRWBY3TgRB6T0amjH9fRZqoAGpACWijHYSyuagzftJlGG-bNf83iRYW9FTau2d-E0_8ruGZ9ky8Gzgk69e526IVk0EJJb8cS2BxydgRJriD7xRe8S1DyD3bUDTF_Fez7q5reqWvy5upO88iZl9R1ej578uSrjYCXj05dgBVGA4w1_SxQ8XUMoD6wZKkMmRkMwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TB01v05C2HRGtf-vHc5IriSuJYArOV_rbY7qGMlrwDrZ91VrqVaeKrdQkKlj-5ZDutKCgjns9bfZZCAo7pQVYYjIZAnFnijoZD0EHbrSHPqcD7JoPM8-DQRznEZuAqflBtJIWE7Kkpk9bgEHjUeyl7gwGzbWEvXNdrL_6sd22w51Pz3mWDDeZuTA5GQKGjyACAGqdm7Li4hmsiavDOv8pJwPhbXlJjlqgd5NYrfBH-_dVe819P-7VBTHTuD8fxl8fS3xdpEG-mKVjDKzf3n5MGmwIxMvyw3TdXbpZvVG-pD-Neb2z1jTmxieqUaCgTZ_9_49fNXHuVjAxU4JoeFo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6H3mvQKWXseJqo4Q3GGBguBq4ZYdqD4SYroA5QVTp6d4VB0Xssh_R7p6gkK6F0ZtppaoJvGXOxp2DiPZCXKP93lJN04DPAbULHGeqTKb7FUVo2mX6Jm-pUKWwh_U8k2_OaOObkskT2ILFC79mOLJziUDIEXLMuZ0wdMjzZtT4EodnxV1Kxie6nEYQDSTvpN4-REfjuBZE3jIQDYUd1E0qnWDiRWWpT2QGPTp39O6pYqy2CLhUHrkLHtZv7hzJ3lh1dJG5tuZk1BY-3Cw3yY63kE6weBEf6RTOlaXqYh3FrZie5pUt4qkJjTj37ozE32arhX6z4w0UkQ-Eb0IfBaCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماکان، پسر جاودانه ایران بر شانه‌ی قهرمانان
🔹
همزمان با آغاز رقابت‌های جام جهانی و با حضور تیم ملی فوتبال ایران، پویش «ماکان کجاست؟» بر تابلوهای تبلیغی پایتخت اجرا شده است.
🔹
پویش«ماکان کجاست؟» با شعار «بر شانه قهرمانان ماست» تلاش می‌کند مفهوم قهرمانی را فراتر از میدان نبرد و زمین مسابقه تعریف کند. قهرمان، می‌تواند کودکی باشد که فرصت رسیدن به رویای خود را پیدا نکرد، اما یاد او در خاطر همه قهرمانان ایران است.
سازمان زیباسازی شهر تهران تلاش دارد یاد و نام «ماکان نصیری» و ۱۶۸ دانش آموز مظلوم مینابی را که در پی حمله موشکی رژیم صهیونیستی و آمریکا به مدرسه شجره طیبه به شهادت رسیدند، در حافظه جمعی جامعه زنده نگه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660567" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660566">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
قالیباف: قرار بود آمریکا محاصره را ظرف ۳۰ روز بردارد اما ترامپ گفت همین امشب محاصره را برمی‌داریم
🔹
اگر مذاکره نبود این موضوع اتفاق نمی‌افتاد و اگر موشک نبود حرف‌های من پای میز مذاکره بلوف و خالی‌بندی تلقی می‌شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660566" target="_blank">📅 23:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660565">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
چرا ایران در روز آخر مذاکره حمله به اراضی اشغالی را متوقف کرد؟   قالیباف:
🔹
ما هر آنچه که می‌خواستیم با حمله بگیریم را چندین برابرش را با مذاکره گرفتیم. ساعت ۲ صبح ترامپ آتش‌بس را در کل لبنان داد و با آن ادبیات با نتانیاهو صحبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660565" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660564">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
قالیباف: فرق مذاکرات الان با دوره‌های قبل در این است که امروز علمِ پیروزیِ میدان، پشتوانه مذاکرات است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660564" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660563">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
قالیباف: وقتی خواستیم در جواب حمله به ضاحیه به اراضی اشغالی موشک بزنیم طرف مقابل گفت که نزنید، ما گفتیم حتما می‌زنیم و اگر پاسخ بدهید منطقه را می‌زنیم؛ این فرهنگ غالب بر مذاکرهٔ ما بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660563" target="_blank">📅 23:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660562">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
قالیباف: وقتی دشمن به ضاحیه حمله کرد من بلافاصله از جلسهٔ بررسی مذاکره بیرون آمدم و توییت زدم که ما پاسخ می‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660562" target="_blank">📅 23:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660561">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
قالیباف: وقتی دشمن به ضاحیه حمله کرد من بلافاصله از جلسهٔ بررسی مذاکره بیرون آمدم و توییت زدم که ما پاسخ می‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660561" target="_blank">📅 23:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660560">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
♦️
قالیباف: وقتی حرف از مذاکره می‌زنیم شمشیرمان هم آماده است
🔹
وقتی به ضاحیه حمله شد و بلافاصله عملیات نصر را انجام دادیم و اینجا نیروی نظامی این کار را انجام داد و دشمن متوجه شد وقتی حرف از مذاکره می‌زنیم شمشیرمان هم آماده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/660560" target="_blank">📅 23:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660559">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
قالیباف: در مذاکره وقتی به دشمن اولتیماتوم دادیم، ترامپ توییت زد و به صهیونیست‌ها گفت باید آتش را قطع کنید؛ ما با مذاکره دشمن را وادار کردیم که این اتفاق بیفتد
🔹
بدون شک این به‌خاطر قدرت نظامی ما بود‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/660559" target="_blank">📅 23:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660549">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9fPWQZLBBsGsd-ykGeMCE0LySyfLQDjCl3Z4gBWrmzx2iufVwDuX3RvGx7kjKmmoC2LI1Fpj-T6xRh4-aBnqgDUv4X4ZcKpIsjMa4EyVM2rCYlbx8FcFp7MayEzyvMiUXmcle7O4VaJoGw4m8CYhZVMj61bLz5UMROLaBkdFt5oszgTKGZlo2N35W2xxEpT3WO_Zk8PUDZNALJVsFB1WckWK0WcNtLc9pXiFBjmkTwZr7F1dTDorglBczW0qCZgtI46LUaKenuY73O5S6H57Hk5x0nVl1GpUy_rYXFeTZZ88QTV1OdFyJSvcIJr-bUiu8kDaxKnvW87b-XEimgoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4A6FalR1sqT-Mb_txI22d1MjAYedjumnSmzYyBdakEC1vnnGn5_RQtLA3K2pji2-Kz8hFht4kQx1KvqQUdnOc18Ln_iYO6Mp_0jt3JV-6TdbG84nQObXAGJtu1Au23LPC2arYU_0WzxuR3hUwgTLZPk0ib_uuZoidQVRLqb6p59HbhQasfXERo61cUKurmIAQQP-CGz8HON6f7hqOhGytAox6dlGMgdC3s2q4OBOW0dK6r0SVqH7fS503FMMBVR0amiTCrSJsODI_mvWZy562CaybV0-69IqWB7i2YftYBPoITUCo9ftxKnKZFUMY8atLDGlVxwzjVvYSh5-RGhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOSbdjHiOfNkPExfn_7JGL1fsHeYbyHlvCNaCBX0IL4DG01FosJTd7jOmAdUzQm8W35xwaXP7dHH9mHxXt1eLT1ecJG7T-3xk3bnWOH9exFoDVS39rhMSOYtDHH2P9RnmBjoyI9eppU4TgUS-QxLRfuxGU25EK3EWEcVn4fUkmCR4KBtWBzvNA1oJk-6nO37WgTp30jDLQSAf0pSaFL2lmYpm0ugmIb_fQXjHSO65zv3OsQbPnCvPo55agmVgdObF4rdNecObNowYAFpHWgZJa55Cn9DAXUo8-mWCZaIIm8234aCDp-nfPc9uzsWcVrG0L1FmTt3_4yUSnd3RCpUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkIfiZ4J7f-Mycpy1HT3DwsfiVxM-IXw3DrGHrjMHicklIGolboOWJRUL5ehRP5cZcBPuZqlNBsNbQaH4CBjC6NvISTZ5OoY9AUQOteVxGZPI3O_bOBXv4q0x-u892Mi7zPyKdE1nTJlLNBKCmLURGfpDcpEkejGJo5i3Wfj-cP1pcNtgR3_F8tcPZLNsWgoEeGaUvTEClXkkya6CzCWvOkROf-1NQ22rak5uy1JxCCnwuQzTV3j4akbVQOrq72UF8Cyln9mVKbNJ-TIbrrARWUFlAnv9s_VCYpiSUBGL9LhDP0ZHD5JyZHXp2l55ss0l6eHcJG7VmN69h5B6vNdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAGPHk0jbCGPOrVeFi7MiyrXLPF9_rwLOYyAkIx_zWlk4-zC0KPFma62qgMwJWxilLwNMACjw4A5gkyh7e49n0T3axC4TMZvydlUb2A8Y5XA7vBu9h8ZyEPGtS-WD3fFMeB0qp_tF82vCRzSb4lPmNBOnj9Oeq_OmAMh7JjnTxCpa64iN-NQ-v7BCZ6ZvrpsgRGx3VCJzpI82XoghYA4feP5NOgWNs_AeG3A6s6VRi9R5gVo3b8vJv01YyAyF37tGIq73bn98Dihu1MiA-SgSJ5AjJ-otAZ8Tu9DB9Ny4uK5gKo7g_IP_w1nAb0MhcPV4GL3Wr8aTJMHYbXut-_N5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4vIOPgmCj59LSClhWhqvpqwwbOX28_49emMdO1jrEz8XAfarmKM-shQCXy1qUdKAU2jsWd8vIxWFJvJ02KxCwc4G_A8b-HKpByFIloPKiqzUZNTvE1ttO5g5VZrngvt8b0OHAfI_Ldr3uQOdX8S7bQPh6W24lfTkZrP2Cp4QxXiCbY5mrnn19uEq-JL-UaUnWkBZjCJUb18sGBjYBYQtkXUtSqD029_79gi64EUJpcDvljVTHhYQV2zng9dOghju5CPpwFdPy238YIewoB31gdDzKWuJ50guI17NgMaNTNwTL4agXP2Tr4HaPjUeaSnKSVJrcMRms0mti4uaqDKGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzDZFmuDT6OCmsjGbM0Q4XY84bJ1xsTyVBz_rBNt_KPGBGFAGUpGBKd63cLtqvJyyCivREUNQ0lnjPt-ZGPaZ-2pUpuhV2aLeK78_L_9FT3RyMlRYnExb3Q4h6pZe5BFt1TOZ9W-8X57YzEcAxUS7Q3kNx6pxSgqCMJilxOZeCotLbz-e5Ti097A5E6ykQSdHpIojYRUJqOc3y_uWdJDWYBPWMBLfk-ztcd8eCdgaaefYxIAjaOV94rh6-WPkNaEGvBHJIjYCAe9HaaE1x8Z3YcEItn-zg7GIGiIFUnjeb-S7mekqOZ7k8JkaE3WLEIo18LVnTRRgZqzUh_2nb_4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaTftfF4UUT73hSd5c_9wcyHiBufYJXVnde24PoybjG33tXXTEk2BcgBS3rJ-l0SuTHbrEHaMF_Dag3OigbsLXSerTpWHRfhboHlOKSDjz_ktdwKig0xMNEQXXP5kEcl9o0cR1NzEK828G3T_4TyxLRqyWW4Q12V7IY-aD-yZJY0_kWBCiMk7F9JnFO_7Vr5M5zhN321F0KgBrm-RGhdFu1pDXxvpYreHxB4Wzi_0AvVpXdY0kuOko5eIg3o3J9M_ygHAl0pNDrMcoBr90qJGtxQQaQqDaUnxRoy-N4uNfs1Up10mjQWvRtgXutVWZ1iqu8z03y6gOYNFb3gPyjyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJdK6QPXLqkIQTGKY2Fpd7H_XJTEQx6kzD_9kkZDJdzfjYOWEifKB8T73QQ0tVr-Xjj7ccagN6LJAcXsAB6Numr8PWwRTFYQXRw8xHm9DG_wLLV0oQKldiaOTc-v30jDn24JY_ynXTR-8huyN-81VbDPNStzYxfmEQBqchagMyUpEXBBu2uvt57XZxPlbdmq1NJayWANMp4Uu3y5g3NT2y82adQgx6eNpPt9D-lBwaKDsXagxoXbyer3iTNsvYPEuRImH1J_nDISKVCIJT9tiwJLm3ZfjU2ElhWooJRGfppQAvelOiDKPvHTibaJzWx9RuZVBZ1DKqPMvwBsLp6ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aGG63_k8K6oJN_ClKwS3UJ-Vl4ECqedjnobx3autVFsqv45CU_U5KynkrKbfQAPMjVy0bcfvwfXuO0FzBzE3RLM0u1gMyswktH7GK8ymQzwH73znqDJ2mbuynO8gcvQ0s4rUCLMXLdIrkG9dMESaPIHVyB9rldjvH-ifscvBMj1VkOSZqno1mqQnPDfmIo8ytaPJ5F_5lkPXdvT4ZTSd0I3PP5aFt3QRzeDahFxteQ5ZyxQt11xPUQNnqvbDVGVuLS9DcPIQWVPbb2SSe5S7_D42Oru7pqgq6uYGVLDiF-FBIK6Bxdbb3LV-zvYloTO1sUDN2zuw1GgDgc14Buyp0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
آنچه این روزها جریان دارد، فقط یک خدمت نیست؛ جلوه‌ای از
#همدلی
مردمی‌ست که دل در گرو محبت به اهل‌بیت علیهم‌السلام دارند.
💫
به برکت همراهی شما عزیزان، مسیر خدمت در
#هیات_قرار
همچنان ادامه دارد و هر قدم، به پشتوانه دل‌های بزرگی برداشته می‌شود که بی‌نام و نشان، شریک این خیر ماندگارند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660549" target="_blank">📅 23:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660548">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4aYPq2QOJPCBJ9fDBqL3XO-QjNNH3i36Noe8GqU7KYOzvePCaCATxqNO-jLGqdMfSCXXOBh76ZfeEgIAiw7EQMCc1JAV9qMdq6lDSWBX_YIyhmOYUERDSw4DWIXWqKAD3XRFG-ry-OAWhW6CvABm81HlZV8wTjfP2bO1RgcDIZAknRDl6fKWjhawYZlEFC3TnohXsNspOXNSJIulSQLAJoilgTIOBG_9Igxguj4QchOHEcJyUF_zwB0PZSZtVy0e2QG6NCquUVZEUzkPFnPAVI3GBgFvUv_VKx_zolTDIl5hN_t1nFKo1hCwU7ENPFxiS3CgrgyhUBzGXRLte62RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میلیاردها دلار دارایی ایران در کدام کشورها مسدود شده‌اند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/660548" target="_blank">📅 23:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660547">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
♦️
قالیباف: آتش‌بس را دشمن درخواست کرد و دنبال کرد
🔹
بعد از آتش‌بس دیدید که دشمن اقداماتی انجام داد و ما فورا پاسخ دادیم. ۲ ناوچهٔ دشمن که خواستند عبور کنند مورد اصابت قرار گرفتند‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660547" target="_blank">📅 23:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
♦️
قالیباف: اجازه ندادیم آمریکا و اسرائیل به ۹ هدفی که خودشان از آغاز جنگ مطرح کردند برسند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660546" target="_blank">📅 23:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
♦️
قالیباف: امروز در هر ۴ جبهه میدان مبارزه، میدان دیپلماسی، میدان خیابان و میدان خدمت هرکس دقیقا می‌داند چه کاری باید انجام دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660545" target="_blank">📅 23:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f23ee767a.mp4?token=XCfbxisSpQj3CCXR8_1yfn31VXB6RHfCQJvPsBU_gCm1JBrGg4ip0Ien2Y2rYz892NqsCfMXAIeWPLjgNlrU2Jo3eJkydpkaqaf8oIgPJTt1BRUthsqR1v7EvypzvHqBHweleLQitLJgemjFuT2_wuFGak10xqwkb4LoEX5JH8Z6p99nsle9o2NghgV1L_LKyfGigg5-af6HBKfeGVl9nSwO4tve1VtWmLr8SNuzY7SXqXzpMKxf5zC309l-VprsT-iFD70LCkn8Dut8QkVff5WBaFWHgiM1_a2VXvUvpRGertI56LF79GVfdi1xk1SALRXCPOAEpYGAY24RsP6-5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f23ee767a.mp4?token=XCfbxisSpQj3CCXR8_1yfn31VXB6RHfCQJvPsBU_gCm1JBrGg4ip0Ien2Y2rYz892NqsCfMXAIeWPLjgNlrU2Jo3eJkydpkaqaf8oIgPJTt1BRUthsqR1v7EvypzvHqBHweleLQitLJgemjFuT2_wuFGak10xqwkb4LoEX5JH8Z6p99nsle9o2NghgV1L_LKyfGigg5-af6HBKfeGVl9nSwO4tve1VtWmLr8SNuzY7SXqXzpMKxf5zC309l-VprsT-iFD70LCkn8Dut8QkVff5WBaFWHgiM1_a2VXvUvpRGertI56LF79GVfdi1xk1SALRXCPOAEpYGAY24RsP6-5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: چه مدت نیروهای نظامی آمریکا را در خلیج فارس نگه می‌دارید؟  ترامپ:
🔹
به این موضوع فکر نکرده‌ایم. احتمالاً مدتی آنجا می مانند. جای خوبی برای ماندن است. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660544" target="_blank">📅 23:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
قالیباف: مذاکرۀ فعلی ما از موضع قدرت است
🔹
من در زمان برجام هم گفته بودم فقط با مذاکره‌ای موافقم که خودش نوعی مبارزه باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660543" target="_blank">📅 23:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
قالیباف: در مذاکره‌ای که خود یک شیوه مبارزه باشد وادادگی وجود ندارد
🔹
همچنین در این شیوه «شعارزدگی» هم وجود ندارد زیرا شعارهای توخالی دشمن را جسورتر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660542" target="_blank">📅 23:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0416604755.mp4?token=PH08gPY5cFVoHBJRD2H9YpyBcCMfjutUC-jZcvFg8vSeHqicKHI1m2UC6-PRh1NikJ4K6ACV-_z466a-GVWoHcE3n1EbGND4JaviBAekfrZtWiapIBLxfzKrbDmLoRhA6PDShdPX0HTj25ODf1ZthWDjYflyz5f9JB7KKAYOtYQO9VjaOD0EJoAFfTKko40GXuB6S61tV_to2JzXNcTaHPtNpKEOUv073oM8dcFxpCawuN63dAzgIAmBxLe6tS5eX8TNgA0n4fHOPilNDFlBEMIYCSfKOfpRf7wzK3n8lUlHKfYMPcw5VfkqhyP9q3rf3BQUWC4fXgRIJz9tPgiZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0416604755.mp4?token=PH08gPY5cFVoHBJRD2H9YpyBcCMfjutUC-jZcvFg8vSeHqicKHI1m2UC6-PRh1NikJ4K6ACV-_z466a-GVWoHcE3n1EbGND4JaviBAekfrZtWiapIBLxfzKrbDmLoRhA6PDShdPX0HTj25ODf1ZthWDjYflyz5f9JB7KKAYOtYQO9VjaOD0EJoAFfTKko40GXuB6S61tV_to2JzXNcTaHPtNpKEOUv073oM8dcFxpCawuN63dAzgIAmBxLe6tS5eX8TNgA0n4fHOPilNDFlBEMIYCSfKOfpRf7wzK3n8lUlHKfYMPcw5VfkqhyP9q3rf3BQUWC4fXgRIJz9tPgiZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: توافق با ایران طی ۴۸ ساعت آینده امضا خواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660541" target="_blank">📅 23:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
قالیباف: در مذاکره‌ای که خود یک شیوه مبارزه باشد وادادگی وجود ندارد
🔹
همچنین در این شیوه «شعارزدگی» هم وجود ندارد زیرا شعارهای توخالی دشمن را جسورتر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660540" target="_blank">📅 23:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1ce79520.mp4?token=EH0lksTjWvVZK_JM2p_DjzbYH2ttEtfDvJEFMDAqvhSsF74U75gS4bU1OLMkMLENIWhu6EmFMJy3ycdKsq237KbPMotZCRvHcWdP2Q-k8gtHjhPhO773nYtwv4ENHaqHbO9Ru3OpDkMbZ9CvpgF0diL0Bc5mqHz3rFMHupAza-h_uzEyvwpyitjldQoJvXQywA0Axsw8vUod3FWTRufSNpe8QwiV92Mi7zME37kc29J2HsQe9z4PltH5KOCMd_ERToXVSh-oHHO_lxgDnRAmFMcu8V8ojBOH6bUHc8zOI-8maBa_fujzKT6yJXEYUXGSmSh79V1U6lpNBN9gzIzwFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1ce79520.mp4?token=EH0lksTjWvVZK_JM2p_DjzbYH2ttEtfDvJEFMDAqvhSsF74U75gS4bU1OLMkMLENIWhu6EmFMJy3ycdKsq237KbPMotZCRvHcWdP2Q-k8gtHjhPhO773nYtwv4ENHaqHbO9Ru3OpDkMbZ9CvpgF0diL0Bc5mqHz3rFMHupAza-h_uzEyvwpyitjldQoJvXQywA0Axsw8vUod3FWTRufSNpe8QwiV92Mi7zME37kc29J2HsQe9z4PltH5KOCMd_ERToXVSh-oHHO_lxgDnRAmFMcu8V8ojBOH6bUHc8zOI-8maBa_fujzKT6yJXEYUXGSmSh79V1U6lpNBN9gzIzwFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: توافق با ایران طی ۴۸ ساعت آینده امضا خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660539" target="_blank">📅 23:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
فاکس نیوز: کشورهای خلیج ‌فارس از اعطای حق کنترل تنگه هرمز به ایران خودداری می‌کنند
فاکس‌نیوز، به نقل از یک مقام آمریکایی:
🔹
کشورهای حاشیه خلیج فارس از اعطای حق به ایران برای وضع عوارض بر عبور و مرور از تنگه هرمز خودداری می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/660538" target="_blank">📅 22:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ادعای اکسیوس از انتشار متن کامل توافق ایران و آمریکا
🔹
متن کامل یادداشت تفاهم ایالات متحده و ایران، توسط یک مقام ارشد دولتی در جلسه توجیهی با خبرنگاران آمریکایی ارائه شده است.
🔹
این یادداشت تفاهم پایان جنگ را اعلام می‌کند، از ایران می‌خواهد تنگه هرمز را…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660537" target="_blank">📅 22:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
رضایی، سخنگوی کمیسیون امنیت ملی مجلس: افرادی که برای مذاکره رفتند تمام تلاش خود را کردند
🔹
مسئولین حتما باید با مردم حرف بزنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/660536" target="_blank">📅 22:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660532">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نوحه</div>
  <div class="tg-doc-extra">حاج‌منصور ارضی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/660532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک هیئت قرار  ویژه شب سوم محرم
🖤
#محرم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660532" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660531">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tygl7RACkK7CeU7CceJvVRlvAWIG6Mf6v3SvDDOGBMhRkF_qiLE4ixhtqwbhdoWnEPKpvrVpsc-yvtHgmIHuRodBPXMElZwZZHs2zCWKC34UXgFIfLAUefYcBQHHZXpg1dQTH6wq4ZQD4P9Fitv9F_Zv_CESrSzLLs8vUR3V6CNdQQMUVl_Uqq2aI97VG0BBlP4Mi0PVeLe9BsI0777QdLNoKuoNiJ6cfmIEH-cw-KjTmKFtFPSnS1QR752GbIUJOlFXmfM-3GT0PQCjJZfmds2LbOokVsDcfOF29YSzUDTz6ttw10qdIVDGmf3vFxN1xeCsNZszugxBujW9pYC0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبر| انتشار متن تفاهم‌نامه ایران و آمریکا تا دقایقی دیگر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/660531" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660530">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsUkhWR8h-VlP9StbB5ueJ4BwMZ6u_7LxbjGLs2KqSjBZYNwH-jFGajd1waqnPE9bsOgm-xmhSxDUM7xbzioG2DH9_2IsoUWMvYfWsnNTdLXRqk1EzerRhcuqDXDbY1u-NdcUAZps1QDU-MQofP1x4FFo335cC8e-QrXhxR0PK8PM9i0BPB6ySAr-vEKPHB0pIicpXyCcEfDZOQXKVbymqr-OB6TikxKT4qYDFNmmRb6_hakfO1hBnXzBTwar5EqRLqWP7VqCYpsJn4ByDnwgSTI7aWS2sO9AMNLmJe5cR3T8zxZH5GYYIHoQ1uzwGv8ig2HyC07oqhztgsubA_GYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل تساوی کنگو به پرتغال
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/660530" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660528">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX6hFTqBiLNpw4icbjvo-qcmE-n20mOSmZ2GyGrZ_v3eltrwVE-kqhnoa47wGH1uM762lRLweQ03JFo0JDbRhPWjQ9WPqEu-bIY8jjEOR0APhyg5W8anHG5Rk5mKxV09egCWpPAJlJvhV1lT3sLIp-dOiUfPaMiJDkMTqrEquuzlAtHjLtiB2RPmR8HpIqjUuE4Vnz_8GapsD3WHCikNifhGKl5PgQTyb4HHN67ycAD5jedvjkTsAkxaBmFlTb0ZjLPhXr20cQBFIG2X5V5CsDLNaLJUC8CjL-g-LTlLz1Pq4p1oJAC02glaLDPP_EUm0V2Y1dzD4HzUb-sebg_gJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در قتل اپستین دست داشت؟ | جفری اپستین قبل از خودکشی، وسواس زیادی برای سرنگونی ترامپ داشت
🔹
بر اساس یک گزارش جدید که به اسناد و گفت‌وگوهای منتشرشده از روزهای پایانی زندگی جفری اپستین استناد می‌کند، این سرمایه‌دار بدنام آمریکایی در هفته‌های منتهی به مرگش در زندان به‌شدت در تلاش بود اطلاعاتی علیه دونالد ترامپ پیدا کند و از آن به‌عنوان ابزاری برای کاهش فشارهای قضایی استفاده کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223625</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/660528" target="_blank">📅 22:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660527">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNQsrUIG_0gFn8mdaqVY_Tq3ABr5khjpjKVi1bpumth6DMJ_C6fpgen81RiNTT194ZGU35h7ICbAhOJ9w1iscrccvT2DohBjymlj3AEYLLhVmLZzye4A0OKM4Fo4xKxBpNpIiZjoh4axIvmuykaNioMw_6Onp4iwWe3PAvrPgcAkltmDz8qPea1XyQweJtGIfyQK0Ox4u6uR0fs00dV5IimbQkys9631ux1hH5MDiwtDoct6eXF4KF0qNDFX7hYwiCup53aLx0-0FNvbgm_pU0wMwFMKu4EGQVPbP9lP6FvvRtskoM6azYLW2V0K4pOZVtJS_5aZjpklbtx0lDHK4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از محل سقوط بمب‌افکن استراتژیک B-52 آمریکا در کالیفرنیا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/660527" target="_blank">📅 22:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660526">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
منبع آگاه: پیشنهاد امضای الکترونیکی تفاهم‌نامه ایران و آمریکا پیش از سفر به ژنو مطرح شده است ‌
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده، از مطرح شدن پیشنهاد امضای الکترونیکی متن تفاهم‌نامه میان ایران و آمریکا پیش از سفر هیئت‌ها به ژنو خبر داد.
🔹
بر اساس این…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/660526" target="_blank">📅 22:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660525">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
مدیرعامل سایپا: مجوز افزایش قیمت نگرفته‌ایم
🔹
در صورت صدور مجوز افزایش قیمت، موضوع از طریق سامانه کدال به اطلاع خواهد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/660525" target="_blank">📅 22:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660524">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8pjDoWdmOJCW-OgysdTC1NUgHcJxs_LYdnL3YfAXu1hjpVFU1sUYr0AizYGoAUbQHIpb4PXyXT6TgC7A6hZfwMTrlofKoREzJiRXLtEPwIhrf7oUHRpcgjIkpSgfxFxrsZzk3mHi0mTTX5ejCKHbf99_Uk4iDZ97qnsI0mvjEaXGz6Waag01cgCokJaFE2lIouXrFdzmVZR3VXWm6HsXfWUMrI6VEFSoulZXZ158MMYqfhm9BOHaPvDvfWpaOf3MpLMbs2MLNgAnIe6oPkSvIO2E-HGE-YkI1ce9uSsYLMJp0R-8tDr7ZTzmZ9k4dB1Q-imeUb6UtfHrK_V0Ri9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اراده خداوند بالاتر از سخت‌ترین اراده‌ها
🔹
امام می‌گوید خدا را از گشوده شدن گره‌های سخت و شکستن تصمیم‌ها شناختم؛ انسان گاهی اراده‌ای محکم یا مانعی بزرگ دارد؛ اما ناگهان تغییر می‌کند. این نشان می‌دهد بالاتر از اندیشه و ارادۀ ما، ارادۀ قدرتمندتری وجود دارد…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/660524" target="_blank">📅 22:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a644bb4b89.mp4?token=No7cLHvOhO29zth5Z4cYzcVmCFytV63mI2EmfTbynd8eCQqvUhXup_wzCOhh9bDSqdYw7ynx3fg7Soa2Jfx1REr7lj7RTZxK-98AZywCATgBLd0grXC0CrNxyM3FyvjXoySN-4q1zOB3AucgEThBGGCvacMVJpGUHJiWXlGwYTWD7xNeT6mGbratW_ick1XC03eTC2mro56CUkX2FQ7xR7ts2kq-Pm30StRIZfaNperIx-29sxV3a6-xrNq7qW6Ce9TfPnz-_9pdrxaa0RmzPNHCklRw0rqUfvTuLlNwi1kdWgGjnI6xK5ZZpY0IvsbnWAqVgNxWQWVfzy0RiWNo5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a644bb4b89.mp4?token=No7cLHvOhO29zth5Z4cYzcVmCFytV63mI2EmfTbynd8eCQqvUhXup_wzCOhh9bDSqdYw7ynx3fg7Soa2Jfx1REr7lj7RTZxK-98AZywCATgBLd0grXC0CrNxyM3FyvjXoySN-4q1zOB3AucgEThBGGCvacMVJpGUHJiWXlGwYTWD7xNeT6mGbratW_ick1XC03eTC2mro56CUkX2FQ7xR7ts2kq-Pm30StRIZfaNperIx-29sxV3a6-xrNq7qW6Ce9TfPnz-_9pdrxaa0RmzPNHCklRw0rqUfvTuLlNwi1kdWgGjnI6xK5ZZpY0IvsbnWAqVgNxWQWVfzy0RiWNo5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
ویژه شب سوم محرم به یاد حضرت رقیه سلام الله علیها
🥀
شمع ها می سوزد و زخمی ترین پروانه ام
عطر نان تازه دارد غنچه ی پیمانه ام
شانه های کوچکم از بس که می لرزد دگر
عمه زینب سر نمیذارد به روی شانه ام
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/660518" target="_blank">📅 22:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnK50JsXgyJq1CyQUA1qCOeb4wBgMZk2-5WC-Ka7pfsRleiZ_EnDqPT-QK3qH1tjB2KhPKHuv0UTRTfMZfDb687lI_zAeGCkV-QVDF1HFlIax-PiTP4ewg8nhvjC3X8vEVgZ_ditBxRrLU2JcQIfm_LapA1mbz94K2tcEL_14HhsBe_GVB9tHIF5MUK306d87NmDDc8yA-tjarpxmK-TIellTmdyO2WS5d6J-5FsV7HCI1gb27uPgfFYNTi_PKRljdiRkAvPBo1Kc7z0sR-Q-T-y_R-iI4Ayt45u3s9uXetIzvMWmevgZjZImJ-29ltjUzwz-mrbuUgOT5TkSwIexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍺
بهنوش ایران در نمایشگاه ایران آگروفود ۲۰۲۶ حاضر شد
▫️
شرکت بهنوش ایران در سی‌وسومین دوره نمایشگاه بین‌المللی ایران آگروفود ۲۰۲۶، تازه‌ترین محصولات و برنامه‌های توسعه‌ای خود را معرفی می‌کند.
▫️
همزمان با این رویداد، بهنوش از محصولات جدید خود در دو گروه «دلستر» و «آب‌گازدار طعم‌دار» رونمایی خواهد کرد. همچنین کمپین «جام اینجاست» به مناسبت جام جهانی فوتبال و حضور تیم ملی ایران، همراه با برنامه‌های ویژه و اهدای جوایز در سالن خلیج فارس برگزار می‌شود.
▫️
علاقه‌مندان می‌توانند از غرفه بهنوش در سالن خلیج فارس بازدید کنند.
▫️
مشروح خبر
khabarfoori.com/fa/tiny/news-3223870</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/660517" target="_blank">📅 22:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
مقام آمریکایی: توافق با ایران از طریق قطعنامه شورای امنیت تصویب می‌شود
یک مقام ارشد آمریکایی:
🔹
یک سازوکار اجرایی برای نظارت بر اجرای یادداشت تفاهم‌ میان ایران و آمریکا و تعهد هر دو طرف به توافق نهایی در آینده ایجاد خواهد شد.
🔹
ارتباط بین تهران و واشنگتن، شاید به‌طور ساعتی یا روزانه وجود دارد، اما اعتماد بین آنها همچنان بسیار ضعیف است.
🔹
تا زمان دستیابی به توافق نهایی، ایران وضعیت برنامه هسته‌ای خود را حفظ خواهد کرد و هیچ تحریم جدیدی اعمال نخواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/660516" target="_blank">📅 21:59 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
