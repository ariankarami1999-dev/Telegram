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
<img src="https://cdn4.telesco.pe/file/nWmmIbWfzOCvUSXZpld2h2pKB1Y1bN4nXJwkLgXsT2k60RJRIfPEcd70Vtpgx6cDvDnhLq_paLk3jYP-9HXIsnYEM6cm_0qqjj-si2kLhUe1iG10Y0ebltp4RKaQpc_CQjcwZX0ra63uHsp1Sl6lQIFZPkw76i4OZStWY4i78I2DumCql_KLsYTpSI6L56Pf8DwYZU_Ijic_cjEwn477RGs9ZI_pKRc7D3JKcWRAaHVHYMa905J4gEIwpyT5w08mTPzkFWpvOfu8ba8kQTrYznZ5aKMspjQTtrAhxnXciFGz2cv7zEaItqzmRz0WC08GFnFVhXfcoT4hWovI273xkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 05:20:15</div>
<hr>

<div class="tg-post" id="msg-673968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تایید حمله هوایی ساعتی قبل به نقاطی از استان ایلام
فرماندار آبدانان:
🔹
ساعتی پیش منطقه چوار و آبدانان در استان ایلام مورد تهاجم قرار گرفت، این حمله هیچ تلفات جانی نداشته است.
🔹
همچنین حمله هوایی به منطقه انارک در چوار منجر به آتش سوزی در اراضی منابع طبیعی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/akhbarefori/673968" target="_blank">📅 04:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به بانه در استان کردستان
🔹
بامداد چهارشنبه ۳۱ تیرماه یک نقطه در خارج از محدوده شهری بانه هدف حمله دشمن قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/673967" target="_blank">📅 04:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673966">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ترامپ با توافق هسته‌ای ۳۰‌ساله با عربستان موافقت کرده است
🔹
این توافق دسترسی ریاض به برنامه تاسیسات هسته‌ای غیر نظامی و احتمال ساخت تاسیسات غنی‌سازی با مشارکت شرکت های آمریکایی را فراهم می‌کند و همزمان نظارت واشنگتن بر این برنامه را افزایش می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/673966" target="_blank">📅 04:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673965">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به سیریک
🔹
استانداری هرمزگان در اطلاعی جدید که حدود ۴ بامداد چهارشنبه ۳۱ تیرماه آن را در اختیار رسانه‌ها قرار داده، از حمله دشمن آمریکایی به سیریک خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/673965" target="_blank">📅 04:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673964">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
معاون‌استاندار همدان: در ادامۀ اقدامات تجاوزکارانه، دشمن آمریکایی ساعتی قبل نقاطی در شهرستان کبودرآهنگ مورد حمله هوایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/673964" target="_blank">📅 04:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673963">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای سنتکام
:
ما یازدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/673963" target="_blank">📅 04:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به بوشهر
🔹
ساعت ۰۲:۴۵ دقیقه بامداد صدای مهیب انفجار در برخی مناطق شهر شنیده شد که بررسی‌های اولیه نشان‌دهنده تعرض هوایی متجاوز آمریکایی به دو نقطه در حومه شهر بوشهر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/673962" target="_blank">📅 04:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سپاه پاسدارن: عملیات تنبیه متجاوز ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/673961" target="_blank">📅 04:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673960">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcrY8LbQrulbdiKPOP4hMQNWqFl8bx-3_BisSWr8FkuM6E1b4RUgKrOXGannc5J_1BYHKteYhG5-jAfrDmJIal99EIvG4UnEaGPgXdWG1Zw57GW9Jdlso4bax2Ru6FRmGWHQRGLHq6F327ZfuEwcDdwQ6Y1z7-0dJbvianPG1O407yhf41FJbp3izJXFtWOEUVT6TShkCOO73b9ilT_ODHpmjP3Qa1MN9Y6mkUZE7H_491tWI8Q08n8fJC0twkuNS5Tzu-98yYS1pFejOyIdufNm4NrBPZCsgc6kqmlRYxCv5QO5dSsGe9E3yAjiFOdKLU9-3hoUwMQ4j--n3GKmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از پلاکاردهای معترضان ضد جنگ علیه ایران در جلسه استماع سنا همزمان با سخنرانی وزیر جنگ آمریکا
🔹
نه به جنگ علیه ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/673960" target="_blank">📅 04:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: دقایقی پیش صدای ۴ انفجار، و برای لحظاتی صدای پرواز جنگندۀ‌ دشمن در چابهار شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/673959" target="_blank">📅 03:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پدافند تهران دقایقی قبل بار دیگر در شرق و غرب تهران بزرگ فعال شده است و به نظر می‌رسد که پدافند مشغول مقابله با ریزگردهای احتمالی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/673958" target="_blank">📅 03:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
منابع خبری دقایقی قبل، از شنیده‌شدن فعالیت پدافند هوایی در غرب، شرق و شمال شرق تهران خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/673957" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/673956" target="_blank">📅 03:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تکذیب خبر حمله به استان هرمزگان
🔹
معاون استانداری هرمزگان: تا این لحظه (ساعت ۰۳:۱۵ بامداد چهارشنبه) هیچ گونه تجاوز دشمن یا انفجار در سیریک و سایر نقاط استان هرمزگان نداشته‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/673955" target="_blank">📅 03:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: نقاطی در اطراف شهر بهبهان و امیدیه توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/673954" target="_blank">📅 03:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به بوشهر
🔹
ساعت ۰۲:۴۵ دقیقه بامداد صدای مهیب انفجار در برخی مناطق شهر شنیده شد که بررسی‌های اولیه نشان‌دهنده تعرض هوایی متجاوز آمریکایی به دو نقطه در حومه شهر بوشهر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/673953" target="_blank">📅 03:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
دقایقی قبل دشمن آمریکایی نقطه‌ای در شهرستان کنگاور استان کرمانشاه را مورد حمله موشکی خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/673952" target="_blank">📅 03:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd130fc44.mp4?token=UodKWJ1--qy-1yEnArXa--7TqIbmP2PbWn77AYgLBHn_DxROMfaoIDoU8fcOTY4tlT0XXRH0ZNFN_gy7u6H0hLO_c44suhLvmdekQHhIapc3DusUlFY0ezbOgGwvJG3eRKVONhYwgfHDsYu5zQvCHeOShF4OTsPtIsrJgcNTXGfZtqv2WtAK9rBvPjcA6DiIfkeVTygW9zdKXM5othBNvJRM7JhS_TKQCaYk0KIPxeOnP7ioxP30-tHq5lsafJHewUMAL813ZMH272-ZvDLPH13shwkuKesMXcxyOGTkB2wGIcqb-LR_-yWOhULjpZ_lmal5hJ8dL8pyIagED-qCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd130fc44.mp4?token=UodKWJ1--qy-1yEnArXa--7TqIbmP2PbWn77AYgLBHn_DxROMfaoIDoU8fcOTY4tlT0XXRH0ZNFN_gy7u6H0hLO_c44suhLvmdekQHhIapc3DusUlFY0ezbOgGwvJG3eRKVONhYwgfHDsYu5zQvCHeOShF4OTsPtIsrJgcNTXGfZtqv2WtAK9rBvPjcA6DiIfkeVTygW9zdKXM5othBNvJRM7JhS_TKQCaYk0KIPxeOnP7ioxP30-tHq5lsafJHewUMAL813ZMH272-ZvDLPH13shwkuKesMXcxyOGTkB2wGIcqb-LR_-yWOhULjpZ_lmal5hJ8dL8pyIagED-qCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شمال شرق تهران
🔹
دقایقی پیش مردم تهران از شنیده‌شدن فعالیت پدافند هوایی در شرق تهران خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/673951" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای فرماندهی مرکزی ایالات متحده : نیروهای سنتکام از ساعت ۷ عصر به وقت شرق آمریکا امروز، برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/673950" target="_blank">📅 03:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: دقایقی پیش صدای ۴ انفجار، و برای لحظاتی صدای پرواز جنگندۀ‌ دشمن در چابهار شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/673949" target="_blank">📅 03:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجارهایی در سیریک
🔹
دقایقی پیش صدای چند انفجار در حوالی سیریک در شرق هرمزگان شنیده شده است‌.
🔹
مردم سیریک حدود ساعت ۲:۳۰ دقیقه هم از سمت دریا صدای انفجارهایی شنیده بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/673948" target="_blank">📅 03:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
انفجار در اطراف بهبهان و بندر ماهشهر
🔹
دقایقی قبل صدای چند انفجار در شهرستان‌های بهبهان و بندر ماهشهر در استان خوزستان شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/673947" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/673946" target="_blank">📅 02:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ده‌ها شخصیت سیاسی، ملی، فرهنگی و عشایری اردن با صدور بیانیه‌ای، خواستار خروج نیروهای آمریکایی و لغو یا بازنگری توافقنامه امنیتی ـ نظامی با واشنگتن شدند
🔹
آنان تأکید کردند حضور نیروهای خارجی، اردن را در معرض تهدیدات امنیتی، سیاسی و اقتصادی و خطر کشیده شدن به درگیری‌های منطقه‌ای قرار می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/673945" target="_blank">📅 02:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در ماهشهر
🔹
دقایقی پیش مردم ماهشهر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/673944" target="_blank">📅 02:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
هشدار مقام ایرانی درباره هدف گرفتن منافع انگلیس در غرب آسیا
خبرگزاری تاس:
🔹
اگر لندن به واشنگتن در جنگ تحمیلی علیه ایران کمک کند، منافع آن در منطقه هدف مشروع خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/673943" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ترامپ به دنبال دبیرکلی اینفانتینو بر سازمان ملل
نیویورک پست:
🔹
دونالد ترامپ خواهان انتخاب جانی اینفانتینو، رئیس فیفا، به‌عنوان دبیرکل بعدی سازمان ملل است؛ پیشنهادی که برای تحقق آن به حمایت شورای امنیت و تأیید مجمع عمومی نیاز دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/673942" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHBH2jOAgBaulvD3aQQTGoXh2yDXlLg7GEqaF3wj5-s_MTxJ5a3-Q9BooilB7ZXhYS4M_LF27d6hn2yuhyw1D9oWVA8gjlG6lbKAaysrQjz30FW2T6X7KTEyLzH-oxBH1kCpnFAqQyyyxmKXbRvGt0oJidD4qdoiBTKm6aTY-QHTqkNGaIvabur-HFYUI9yiNTu8aFlXQmrsVmEkhY1ih0PyFC1zEZqhGDLtYPT3msLgJZ9hF8hoCqzTTCWnuT64D5Y2YqI2SSNiewDkNeFBhoglH-JUSZOiKlj_Hkc4szyUEpPHDGMkrL624a4AcA6H_hNMmeeBy2f8L7zPw7G_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر خارجه چین به ترامپ درباره تنگه هرمز
🔹
خوک نجس: برای بازگشایی تنگه هرمز روزانه به دو میلیارد دلار نیاز داریم.
🔹
وزیر امور خارجه چین: تنگه هرمز قبل از جنگ باز بود. ریشه مشکل در اقدامات غیرقانونی شما علیه ایران نهفته است؛ شما از هیچ، یک بحران جهانی ایجاد کرده‌اید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/673941" target="_blank">📅 02:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/687a21821a.mp4?token=GdnQEVZI9LUOSaKjQ7JnpsJc5VDP7No1TZPQRljUq2gcLnbQqTTlNbE-OFW5N5MstG0yq9ncDOp1EexlhL75jSBa47bzcjg8Dby6672npkm52oMEgcizaf6Kej4woNF_KEGt6nwG0bgl0-IgZbWeQcFNQRdpdVN-oAw2vQ3hr6ZNDDJ6QjQAAH1_4t4w9k5KWTSrQ8EesYDobW7lhOLTmRZ4_MLhRQh45ma7enP20gv-s7O92jpTIIR7shZNbHuMV98WQR4oxGV3zaeESS9x4jSRXCmxuNPCM_mq9dLtU2CK4AxxCk8tullz5og1RxcJxEEwQKKfv_3Synyk9CBbFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/687a21821a.mp4?token=GdnQEVZI9LUOSaKjQ7JnpsJc5VDP7No1TZPQRljUq2gcLnbQqTTlNbE-OFW5N5MstG0yq9ncDOp1EexlhL75jSBa47bzcjg8Dby6672npkm52oMEgcizaf6Kej4woNF_KEGt6nwG0bgl0-IgZbWeQcFNQRdpdVN-oAw2vQ3hr6ZNDDJ6QjQAAH1_4t4w9k5KWTSrQ8EesYDobW7lhOLTmRZ4_MLhRQh45ma7enP20gv-s7O92jpTIIR7shZNbHuMV98WQR4oxGV3zaeESS9x4jSRXCmxuNPCM_mq9dLtU2CK4AxxCk8tullz5og1RxcJxEEwQKKfv_3Synyk9CBbFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطعی برق گسترده در منطقه کردستان عراق
🔹
منابع محلی می‌گویند که برق در بخش‌هایی از استان‌های سلیمانیه، اربیل و دهوک قطع شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/673940" target="_blank">📅 02:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: تأسیسات هسته‌ای که در عملیات "چکش نیمه‌شب" (Midnight Hammer) هدف قرار گرفتند، به‌طور کامل نابود شدند؛ اما ایرانی‌ها همچنان تلاش کردند توانمندی‌های هسته‌ای خود را دنبال کنند
/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/673939" target="_blank">📅 01:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f18f4b5b.mp4?token=PAFYvJKneqLKiWzg5BnKUFTrlprEIgEnaC7pUp0p1KIH68-AxxOyBntv8QnTMafIZns5RvbAo6b67lWmwORdUoO71lZ_X98j2QroKuEJSBVBilu9OzLJsFD4I-Nd8hR6FKhH36srqG-oHv715Ge_rnFj_jU6GbpGdrnUgVtY5Q4DEj5vFuAqjk_b5iQAdZYiD0XJ9nZbWhv7YqFFKGIRcqRt_Q7Pzii6YRu4uOcLDOcqqP00E3f9HdH5hKjqOUooYmvhNIRFyNbKnfrfXRzIGLl3K6lXy8usA3B6VDgkSO5Mplw1g97zLlT_FaxuAIEaNOBAAOGvHkO8TQ1kRqVg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f18f4b5b.mp4?token=PAFYvJKneqLKiWzg5BnKUFTrlprEIgEnaC7pUp0p1KIH68-AxxOyBntv8QnTMafIZns5RvbAo6b67lWmwORdUoO71lZ_X98j2QroKuEJSBVBilu9OzLJsFD4I-Nd8hR6FKhH36srqG-oHv715Ge_rnFj_jU6GbpGdrnUgVtY5Q4DEj5vFuAqjk_b5iQAdZYiD0XJ9nZbWhv7YqFFKGIRcqRt_Q7Pzii6YRu4uOcLDOcqqP00E3f9HdH5hKjqOUooYmvhNIRFyNbKnfrfXRzIGLl3K6lXy8usA3B6VDgkSO5Mplw1g97zLlT_FaxuAIEaNOBAAOGvHkO8TQ1kRqVg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تناقض در ادعای نابودی موشک‌های ایران؛ چرا موشک‌ها همچنان به اردن می‌رسند؟
🔹
گیلیبرند، سناتور: شما همچنین گفتید که برنامه موشکی را «نابود و از نظر رزمی غیرفعال کرده‌اید.» پس چرا موشک‌هایی باقی مانده‌اند که به اردن اصابت کنند و منجر به کشته شدن مردان و زنان شجاع ما شوند؟
🔹
هگزث، وزیر جنگ آمریکا: آنها ۴۷ سال است که تلاش می‌کنند موشک‌هایشان را در زیر کوه‌ها پنهان کنند، دقیقاً مانند توانمندی‌های هسته‌ای‌شان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/673938" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی بامداد چهارشنبه گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673937" target="_blank">📅 01:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
آژیر هشدار و انفجارهای متعدد در کویت
🔹
منابع محلی بامداد چهارشنبه گزارش دادند که منافع و تأسیسات آمریکایی در کویت، هدف موج جدیدی از حملات موشکی و پهپادی ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/673936" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
معترضان ضد جنگ علیه ایران در جریان  جلسه استماع سنا سخنان پیت هگست، وزیر جنگ آمریکا را قطع کردند
🔹
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
🔹
پلیس کنگره هر چهار معترض را از جلسه بیرون برد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/673935" target="_blank">📅 01:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تصاویر نزدیک از مکانی که در کوه ازمر، در استان سلیمانیه در شمال عراق، مورد هدف یک پهپاد قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/673934" target="_blank">📅 00:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2256ba648c.mp4?token=CtSD2axueUwf8c4poO3XSk8fSzvu-7G7M7ir-CNkS8514VCLZiPRuwOemRLtfV-V0H1HTc1SRY90WJ6BHs6JZpDvq5dNn0_qujhZ-v34olMKQIEgGHG6yu5C0GyY_1rH8HjuulnWY8vCskk2G-gQ-noHWChd3h5899G_tZy-g7u-XiVokYZ1uEsK5qksB4SVw6ZGSauSHKQT5eR2J7WEvm14Obgim3GdDkRDupka_A1FYvZ0lWVF2AyRizKM8dlmgesw5f8tbiDB1wPYqUpGg7eQhcgviGNKyIAzAX7LxXr96tycyKrUXh8h7hBFR_dK82-QeNBGUaZyb482BTvWSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2256ba648c.mp4?token=CtSD2axueUwf8c4poO3XSk8fSzvu-7G7M7ir-CNkS8514VCLZiPRuwOemRLtfV-V0H1HTc1SRY90WJ6BHs6JZpDvq5dNn0_qujhZ-v34olMKQIEgGHG6yu5C0GyY_1rH8HjuulnWY8vCskk2G-gQ-noHWChd3h5899G_tZy-g7u-XiVokYZ1uEsK5qksB4SVw6ZGSauSHKQT5eR2J7WEvm14Obgim3GdDkRDupka_A1FYvZ0lWVF2AyRizKM8dlmgesw5f8tbiDB1wPYqUpGg7eQhcgviGNKyIAzAX7LxXr96tycyKrUXh8h7hBFR_dK82-QeNBGUaZyb482BTvWSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان ضد جنگ علیه ایران در جریان  جلسه استماع سنا سخنان پیت هگست، وزیر جنگ آمریکا را قطع کردند
🔹
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
🔹
پلیس کنگره
هر چهار معترض
را از جلسه بیرون برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/673933" target="_blank">📅 00:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e3a9751d.mp4?token=RbfUhtthpqxtJv5RcCei9cdUChY-w3Nw-BP_aRtiajjHBTSQC3XicG0b9LFi8yx_gXdtgjzl0ylQt9wzoMzZ4Sh3HLaXcM4c8Ss1qO-TTTdL8KW8jclC9-1rwcoN8rSiXOhO_rz31pnnLvuyfte6jB0ZaRBQGY0kM5lPUq58FfpgeBTuaR3XuJuAKL4kyuZd3uT9Punl5-r5tEMi4-4kOva1LJlCrS4uww4WCoTHTGKOiCm1TJqBik_KyW0vcoINjK9ujfsvHq4dQFJyNIywSMvGiJtePIDLbXvCS0mwRfb88mrfO4PA1p_qjI34qmlYvgELfzk_8CiwQl3kAPXkMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e3a9751d.mp4?token=RbfUhtthpqxtJv5RcCei9cdUChY-w3Nw-BP_aRtiajjHBTSQC3XicG0b9LFi8yx_gXdtgjzl0ylQt9wzoMzZ4Sh3HLaXcM4c8Ss1qO-TTTdL8KW8jclC9-1rwcoN8rSiXOhO_rz31pnnLvuyfte6jB0ZaRBQGY0kM5lPUq58FfpgeBTuaR3XuJuAKL4kyuZd3uT9Punl5-r5tEMi4-4kOva1LJlCrS4uww4WCoTHTGKOiCm1TJqBik_KyW0vcoINjK9ujfsvHq4dQFJyNIywSMvGiJtePIDLbXvCS0mwRfb88mrfO4PA1p_qjI34qmlYvgELfzk_8CiwQl3kAPXkMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر نزدیک از مکانی که در کوه ازمر، در استان سلیمانیه در شمال عراق، مورد هدف یک پهپاد قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/673932" target="_blank">📅 00:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673931">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: من اذعان می‌کنم که ایران هنوز هم بدون شک توانایی‌هایی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/673931" target="_blank">📅 00:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f739848044.mp4?token=hAqAXB6qsk9G7Je0fMvaJjRzwK7htrDYd044AGUr-vwM_BoWWwzDXT1IWb6PbTJHEQ2aRUiRz6MDGYUGro1SeTt-4FmOL5OH_MH81aeDPVelj7yHtStUT5_PKlQsWfK9h4s_t7lXqaE9IJXhEVfcKPS-yk-dq3i_T1oHEr6f582sD8qPvydrVjFFDgqaQnNOBCIStib0IWWJ5MsYP-ipLxl3_Xr4BW9GHHlNRo2I-2G4Y4DeL6idBDe7F95FPOlqnQGIfTThXtKZ2mLwNNMKszIODdWL2X0z8xLBY9stVE8PFZOg4CJ3EQBU-07eqCzxKJD58ANYDWFRWufEk3cPlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f739848044.mp4?token=hAqAXB6qsk9G7Je0fMvaJjRzwK7htrDYd044AGUr-vwM_BoWWwzDXT1IWb6PbTJHEQ2aRUiRz6MDGYUGro1SeTt-4FmOL5OH_MH81aeDPVelj7yHtStUT5_PKlQsWfK9h4s_t7lXqaE9IJXhEVfcKPS-yk-dq3i_T1oHEr6f582sD8qPvydrVjFFDgqaQnNOBCIStib0IWWJ5MsYP-ipLxl3_Xr4BW9GHHlNRo2I-2G4Y4DeL6idBDe7F95FPOlqnQGIfTThXtKZ2mLwNNMKszIODdWL2X0z8xLBY9stVE8PFZOg4CJ3EQBU-07eqCzxKJD58ANYDWFRWufEk3cPlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف بزرگ شبکه‌های عبری به شکست ایالات متحده در برابر موشک‌ها و پهپادهای ایرانی
کانال 14 اسرائیل:
🔹
آمریکا در حال حاضر نمی‌تواند از پایگاه‌های خود در منطقه در برابر حملات ایران محافظت کند به همین دلیل این پایگاه‌ها را تخلیه و هواپیماهای سوخت‌رسان و اسکادران‌های جنگنده خود را به اسرائیل منتقل می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/673930" target="_blank">📅 00:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GybwSWiyRBfl3Ns7iNItnP6IAzZKkaTqkTzIyEidQyib28P_yhnfmZ5Mj6jbsL4waD4GhR5LMWNAwy3NleKddYN4WlizCKN__qFOuitTvZh3sbO5nTksogpWkdmR0D2zX_VXdUFFFKJf6x2snFzR1zEnzeSEJR_Bnh1Bt9A29kITFhf1e3nzVgRVBW4gFDVduvgjs7ktN4-EC_SIngM0LyyqHUAB47UYoNYZz01BgBx7N8Z4VkCFV8wl5SAAFgFaGoQof84zT4LIl6f62oTRx3ZW0zZ6X_PGeBpP1IqFgyqsh8B_eJGIxBoUzPGp0Qa1NWGCQVhHISvcqqZbEQYMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/673929" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3eFET-B9x3b5yaIpm3h2QcmnptDVYB2VrZs_8XmtVqk_OftFuQhdKe5OniluDEgNEMIguF7kaBcCQ-4DuQF6DkQ3FN9NHI7Ax6H_nsKlnp53PYeXPBybYeESWKVW8ksHzRpTUG-y8rx-dzF4uihyM36ObMJav_Ad53s1exMbRyYDUfPBEvJ5CTgRj3d_9wFvz-0ooX4r_bg65fXjgZXsOav4zI8Iqe525Gf8d2p06Hwcf3PlNzt9U_Uni4ZY7qG46uKuxVUCj_5qqOGA5SYeZqJItNZF7Kaf3us7jTkt1kPhB3IC0aj3KPWF9GO7wmiwAC5Xlz4gi7P1VKEk22fQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاتر تحصیلی شفق تولید انواع دفاتر مشق طلقی فانتزی وکلاسیک ،رحلی،و....
تماس
☎️
09129318455
دریافت لیست قیمت
@Ghamilou73</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/673928" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673927">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwAZSI6386SiQ0txqxtgDP3P-q8jceTOGhvgWqK-09i74YToJejxgxx0fcPZktMXBIWJSRJciTuRYu6Azm60eEhPROWahFconxDgA7Kzkld96tAoeJrNZuxFSs1-Z9s5q5ml1IIFUQCeIzq9oO1dzF95jf-mphnUWFvO0MxtVPanhqrQJWui_enC5LXafqKl5aGvVPCmQs2VeD2JW3RdGrRul4D3Nz1uAKCuJoa6QdEO-4zEdMXYOW0TFWbk7oZtvuIYYQMbabMC690rzViz12DwfsKNZ5G_KFl50-XwR8sAqJ6xlowUnUimtNq7PmXxlLhlIl7aP0N5QPNqoz5PiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار در مقر تروریست‌های ضدایرانی در کردستان عراق
🔹
منابع عراقی بامداد چهارشنبه از حمله هوایی به مقر مرکزی گروه‌های تروریستی جدایی‌طلب در استان سلیمانیه واقع در شمال عراق و وقوع آتش‌سوزی گسترده خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/673927" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673926">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): آمریکای جنایتکار مراکز هسته‌ای و حساس ایران اسلامی را تهدید به حمله نموده است
🔹
اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله‌ای بشود، آن را به عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم‌پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/673926" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673925">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
واکنش وزیر نیرو به خاموشی‌ها: در حال حاضر برخی کشورهای همسایه در شرق کشور با قطعی برق ۱۲ ساعته مواجه‌اند و در برخی مناطق دیگر تنها ۲ تا ۳ ساعت برق متفرقه برای تامین نیازهای ضروری وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/673925" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673924">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سخنگوی هیأت رئیسه مجلس: دولت پذیرفته است که فعلاً هیچ‌گونه اصلاح قیمتی در حوزه بنزین انجام نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/673924" target="_blank">📅 00:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673923">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=jBGQKRoJoG_6qin37v2642rDK25Z8zmM_fu_j_GTc8JjgE3F3gBikOOiCy7vcVsbYeS5YeKnErXo7ARr2K-v0Wi1gDs8A0mSDw7yVUwdPUKzSV5E3ainyhhyyZncxjGCBxrPw3RuzEIqY_vIaUlwTrYpF5tcSYLHkE5eTu5T1KdIWb3rbFENqKKIQWGW4L-tH9hpP9TAtOsUwUFY2VyoyRg04H4BUUI28LVaGw8ovFqazFXQ5ZhlPdzFL_ZvtkkAx5EOYWIQD80jSCa021bT1A77REbOrk0s1JzFGwws6ONAoUKJCkVpu2Xz8xKMSjPn_2LGC5equ1I3SqoRlwHqkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=jBGQKRoJoG_6qin37v2642rDK25Z8zmM_fu_j_GTc8JjgE3F3gBikOOiCy7vcVsbYeS5YeKnErXo7ARr2K-v0Wi1gDs8A0mSDw7yVUwdPUKzSV5E3ainyhhyyZncxjGCBxrPw3RuzEIqY_vIaUlwTrYpF5tcSYLHkE5eTu5T1KdIWb3rbFENqKKIQWGW4L-tH9hpP9TAtOsUwUFY2VyoyRg04H4BUUI28LVaGw8ovFqazFXQ5ZhlPdzFL_ZvtkkAx5EOYWIQD80jSCa021bT1A77REbOrk0s1JzFGwws6ONAoUKJCkVpu2Xz8xKMSjPn_2LGC5equ1I3SqoRlwHqkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی خطاب به وزیر جنگ ترامپ: شما چندی پیش ادعا کردید که ایران کنترلی بر تنگهٔ هرمز ندارد. اگر این حرف درست بود، ایران چطور توانست هفتهٔ گذشته دوباره رفت‌وآمد کشتیرانی در تنگه را به حداقل ممکن برساند؟
🔹
ادعای مضحک وزیر جنگ ترامپ: ما مدت‌هاست که کنترل عبور و مرور از تنگه را در دست داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/673923" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673921">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=TPJrUgv8e6MNQgnUsZQW6gN_MRQp0vcF7WIkWRtEn_9Fn1Pesq7vphXpDz8UUkaddadzkHLVhL7ake4kTOFIv5lPuIcXc69FyX_z-2fNTxyhsjU5_pdVNLfRpDgDQpsv6HdIs7WqweVoHG0NUmzxdfi07lTNHOkSeragSQTNiwBiJ5n7ibQEE736wqk_xeYxlXK6kUecwUjbUFb9LNJKYuT7VbcbeVs3_xE4am7gSyI4I_IHIbCGbYeaklrXf08osrbyUa76eDnYBbnvGFdiJfx69S-XoikjDdxldJ0SbopCJozQhh5oeIhambv2ZVZDHWGdOVrZRRZoj6Kx3wHJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=TPJrUgv8e6MNQgnUsZQW6gN_MRQp0vcF7WIkWRtEn_9Fn1Pesq7vphXpDz8UUkaddadzkHLVhL7ake4kTOFIv5lPuIcXc69FyX_z-2fNTxyhsjU5_pdVNLfRpDgDQpsv6HdIs7WqweVoHG0NUmzxdfi07lTNHOkSeragSQTNiwBiJ5n7ibQEE736wqk_xeYxlXK6kUecwUjbUFb9LNJKYuT7VbcbeVs3_xE4am7gSyI4I_IHIbCGbYeaklrXf08osrbyUa76eDnYBbnvGFdiJfx69S-XoikjDdxldJ0SbopCJozQhh5oeIhambv2ZVZDHWGdOVrZRRZoj6Kx3wHJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: آیا توانایی نابود کردن آنچه را که زیر «کوه کلنگ» ایران قرار دارد داریم؟
🔹
وزیر جنگ ترامپ: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/673921" target="_blank">📅 00:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673920">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyzemymJEu5J9j1g_fq3obVsQKiOQdd48wk_R5b3mxFoq5qF8u6bfFDnd-OcY7UDWonnFMVbkT3gtRXqAzuixuohvxs5Y3vkQ9pGbcYzwDWCALo6brC-LKgiJ6aOWqWQ9jS_z8NDHw7as2U8bIlvff1xMDCVjnCqj65FXVJMqXDypL7m47bNJa7Ijt8cnom00b1A25R2EO-cte7BB1Dmoxh45NiHwDuRijYiK5SJ0KBmhqjH7UE5jNqxK-EukWhWEz22rODVHtvGZ9L81OmFJV4LAcL9NHKj9VC_dKlAMIPpSG7nTg8Nb3fAtgwYtdByCR6z6tqfXZe3AVzJG85ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/673920" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673919">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJr10TIUEogfrtitFSxUJfrUEazEIGe8GNAotXmBfkvJEQByN8f5-0SK08sMWdt8Rg3mBLu4buwdPkaaDigj4RrDUUBKJR-eW7mtO2zNoU35wLnxUZ-LvptwZmQCVCW8FDKKnyCNUQ_FbpOi01KIbcnHZJ0eniTNSVcAEPwf_HQdDDvjhhsV5EVV7qn7YbjLGQIJjx_jAPzh0LC0KbVLiJCv8ikXQnBxny1caz4GyLGDVs1sEhs4iwdPg-zittu3X9kwxsp2ZN3gJplVdtT5IDcawExBZ9-Q-RNrIjBsIMPgW8mcdiEmeNHtipMQSD5CbQvwUeZNMkFYR5QLcKpEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه ترامپ برای حمله زمینی به جنوب/ ایران با این سلاح ها آمریکا را شکست می دهد
🔹
نزدیکی ایران به محل استقرار نیروهای آمریکایی سبب می شود که توپخانه ایران فعال شود و ثمربخشی چندبرابری آن را تضمین می کند. توپخانه به دلیل نوع پرتاب توپ و نحوه عملکردش قابلیت رهگیری توسط پدافندهای دشمن را ندارد و به دلیل نزدیکی به محل استقرار دشمن (در جنوب) ضربات سنگینی می تواند به آمریکایی ها وارد کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3232047</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/673919" target="_blank">📅 23:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673918">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای پیت هگست: انهدام تمامی قایق‌های تندروی ایران، تمامی تیربارهای نصب‌شده بر روی این قایق‌ها یا تمامی موشک‌های کروز آنها امکان‌پذیر نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/673918" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673917">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای وزیر دفاع آمریکا: ما در حال حاضر محاصره‌ای مؤثر علیه تمام کشتی‌ها و بنادر ایران اعمال می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/673917" target="_blank">📅 23:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673916">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddfd4c9329.mp4?token=gsbrYDoJvCQrMAnyy4gELd9Ci0pc9IP0IN3LHnVVnMBg5njziVz3FE95nz0zyc8JAdiTQAe96YHyyXJ9UOSxrXnCrxKcgxebCPVuaC_Dcmggjr_TB4R9xvGb3qh9TVyfw9pyT3cBmZvf9iK88CoR3Xft_nm11AWbXj-tIjjWc5vSM0p-F6sMt2sDA34paTC5PKBxQynwUF7bbNfsLVq2T38DdW8iYr2pwzhdKDjGRl0cMQVMI5S27uP914yeTy1aca0I-VsEK5EwupCRuC0nWOQYKT5sljFZc_wKRhfoQPlqe4rPsbxNsp9lEObTPM5TUtRixEkvE7WBn6a2859XEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddfd4c9329.mp4?token=gsbrYDoJvCQrMAnyy4gELd9Ci0pc9IP0IN3LHnVVnMBg5njziVz3FE95nz0zyc8JAdiTQAe96YHyyXJ9UOSxrXnCrxKcgxebCPVuaC_Dcmggjr_TB4R9xvGb3qh9TVyfw9pyT3cBmZvf9iK88CoR3Xft_nm11AWbXj-tIjjWc5vSM0p-F6sMt2sDA34paTC5PKBxQynwUF7bbNfsLVq2T38DdW8iYr2pwzhdKDjGRl0cMQVMI5S27uP914yeTy1aca0I-VsEK5EwupCRuC0nWOQYKT5sljFZc_wKRhfoQPlqe4rPsbxNsp9lEObTPM5TUtRixEkvE7WBn6a2859XEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطرۀ ایمان تاجیک، سخنگوی عملیات وعده صادق از دیدار با رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/673916" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673914">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: جنگ با ایران تا کنون ۳۷.۵ میلیارد دلار هزینه داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/673914" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673913">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=R5-trgeH_F0p5pFlCozucFODMwbkuTA9qIpnkDT7qdyf9QFGKT8aw754ykr_mpzvOuphlP7H1DNnJc7IEhMnP-oxe8Fln5cDL3bD1mS7khywsxYp9hbr0lNzXfIcjGUfEI9t9hgE9vvuR-6Y4IggkUaglXJAyvmX7NjnxNGRiQLOMHZztDxXuYZCtcBttfjYcUC7wfZI6eCKBXCB8h9c8ets3kgTa5pmJM4YkF70edb3SY_HBHUnUt0Ib89HuM1C3i99Ki4g-N_cwkpNLW1jmo5euyGYiStv0THTnQkv7LIBqmKa5ikqoVPmHv_uPck-HIb6Mer2_J4EGKUMnuPVzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=R5-trgeH_F0p5pFlCozucFODMwbkuTA9qIpnkDT7qdyf9QFGKT8aw754ykr_mpzvOuphlP7H1DNnJc7IEhMnP-oxe8Fln5cDL3bD1mS7khywsxYp9hbr0lNzXfIcjGUfEI9t9hgE9vvuR-6Y4IggkUaglXJAyvmX7NjnxNGRiQLOMHZztDxXuYZCtcBttfjYcUC7wfZI6eCKBXCB8h9c8ets3kgTa5pmJM4YkF70edb3SY_HBHUnUt0Ib89HuM1C3i99Ki4g-N_cwkpNLW1jmo5euyGYiStv0THTnQkv7LIBqmKa5ikqoVPmHv_uPck-HIb6Mer2_J4EGKUMnuPVzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌پردۀ فراخوانی که به‌ اسم انقلابی‌ها منتشر شد چه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/673913" target="_blank">📅 23:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673912">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb25034032.mp4?token=hkM75rGSxeZEcs_IBE3yGNdi2AHChgJiAUxQxBpaJ1n-AvVRBDXdGBFyIV08exIv1zVCzBINsDegGkTFaZXNuSepcAL9Qyk4XZ-o4UfZv3j-2OiupeioUDJoiQYMx7V-yW3W7lJEQutQQf5aej4ep0BIbpWo0am_FO7NNsJxpjfb2iRrKdzXNTH5GryuLF60dmQx0Oc2IoAcn-B5dZs2yLWLALMMMNM3ax4RYoeSnksk7m8n1nNeECGXiS0LrF_1zZ04W6l3TeiQYttfwxYLnVVyc4LjZ0u2qFWMIWkzTK0JAM2EQ5mJIyxyn9CR5haL8hM0NYoDeZEM8guL-FX35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb25034032.mp4?token=hkM75rGSxeZEcs_IBE3yGNdi2AHChgJiAUxQxBpaJ1n-AvVRBDXdGBFyIV08exIv1zVCzBINsDegGkTFaZXNuSepcAL9Qyk4XZ-o4UfZv3j-2OiupeioUDJoiQYMx7V-yW3W7lJEQutQQf5aej4ep0BIbpWo0am_FO7NNsJxpjfb2iRrKdzXNTH5GryuLF60dmQx0Oc2IoAcn-B5dZs2yLWLALMMMNM3ax4RYoeSnksk7m8n1nNeECGXiS0LrF_1zZ04W6l3TeiQYttfwxYLnVVyc4LjZ0u2qFWMIWkzTK0JAM2EQ5mJIyxyn9CR5haL8hM0NYoDeZEM8guL-FX35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان ضدجنگ در جلسهٔ سنا، سخنان پیت هگزت را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/673912" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673911">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlijnJ8EW09oJsobnvM7g_Z4hpLPPi4E7K5egDIZzHu104XYb0wsuoSrwf34yWFt1Bsw1gqHOJWuleakiWm8xZ3m83MpKKXvcTX06L0qhadvuh5byUMifJXW4wUUmvpxSWYKaE9uFtB9V6Pk1Cj6zkP5zBlKueU5L1v5FxM7wt4Y3a6XfuhFeAjXO0Fg5AgKB69luhpVaBbttTObaQRmwomRqDR03iIwD-Nn07DRboDNOs8AfXDw9Xfxfuck8Huaa6AxaHIVVHI9oGOqFxbLCHZ6dSiCSExAAYQFktY8_2yN2QLX6QgStLzSoRGNxMXhr37baE01a1gQ4DRXPLlVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار: ۱۸ آمریکایی در جنگ علیه ایران کشته شد
🔹
جنگ افغانستان: ۲۰ سال، ۲۰۰۰ کشته
🔹
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
🔹
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
🔹
جنگ کره: ۳ سال و یک ماه، ۳۶۵۷۴ کشته.
🔹
جنگ ونزوئلا: ۱ روز، ۰ کشته.
🔹
درگیری نظامی ایران: ۴ ماه، ۱۸ کشته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/673911" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673910">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3ahwWr2Q0pjXDsnYu-6P2qghDfRB5b16fuHeGET3mn1Zp0QDxKEVFe7e6tyZobWZ-9JliFyaHGFvpkallfOuH9EV840PYc1ax_hC2jOOG1o6WnvWh5qWg5R9Tefxcux20nZUg3exzl518Wj-EbgYp58xCHNEUklTFMzbm1cknBR4S52MPqIeQ37X4YNvrGUOB0k48rfOGzoFREQKZvkAZ6khaTEEvdMTTt67smITLHI2tViee1Vfp6Cco3fqteL5F2SHHMwXWYzsy6TuhhAQYmm47pS05MOXgJUmk_F2sGkX4zq4bo8hWHTe5hPA2UpUVa4xS2Bb_JHjB9LCm3qlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام معنادار امارات در روزهای اخیر: اقامت برخی ایرانیان در امارات دوباره فعال شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/673910" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673909">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
خوک نجس: پرواز‌های مستقیم شرکت‌های هواپیمایی آمریکا به لبنان از سر گرفته می‌شود.
🔹
وزیر جنگ آمریکا: اقرار میکنم که ایرانی‌ها هنوز هم توانایی‌هایی دارند.
🔹
الجزیره: آمریکا در حملات پی در پی به ایران دستاوردی نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/673909" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673908">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNEgdx5Xn2-CnvuyPPigT-z6RekhF0fWTZS3hzLBh-ZhM6JDmJcA-XhaWqtu_CCqVPu_DyNnbb6mm2rJwzyoquXPrD73yZ-1b9cL1DaF10BxbX1EGf6pC9NyJqjuYKF-ax2miO84SFUQyO-O_x0U64GYMljdRlvHDOqgcpxfkcwcQhMcYadVZ8MfsgTJ2ivNeaLJ5g0n2DcFLXXxorQ6eud6rsmTIX8zzHTm0XShU7XocO1UuB4nPFdPzU33JA08NfSdQOheax9BWAT_IIvNNhn9Um_rKiLJjsieSv96Q9LNyi0o9wJY3borcLM4kd5n_Fh67O-_NoASC3JU7OB7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ اپلیکیشن هوشمند؛ برای یک گوشی حرفه‌ای تر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/673908" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673907">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0add65574.mp4?token=H2-5cxk2APYmBKBbyss3zIm-gFNbsDHgke0cYd0ar1mKY0am_WOHf5TuUSLUtMUSJ-BYhewGOkg4REjWWLmnMs48KOoJGeoVGqP7NIdernr-hqrTp75BhCkLmBRR5YojtI8_tdsdvk-7Q-iqKv9UB0FbqI3S3SWrYY3bkwkSxVFMOBgwKrmKCFshrm6NH3rAG__TRliSdwWfdbobd9DwVYzPg8E8YqkK7nypALlQyXHBDLr_fUt7zf8z1pFy_MM5Ck8NklSA16ixuN9xhXyCACZ3eNVPAWIQpiQ3FHp1oq0xBTtL6sNGoUjgPAlI6g45stxQPz-aYClTSZwslkQPcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0add65574.mp4?token=H2-5cxk2APYmBKBbyss3zIm-gFNbsDHgke0cYd0ar1mKY0am_WOHf5TuUSLUtMUSJ-BYhewGOkg4REjWWLmnMs48KOoJGeoVGqP7NIdernr-hqrTp75BhCkLmBRR5YojtI8_tdsdvk-7Q-iqKv9UB0FbqI3S3SWrYY3bkwkSxVFMOBgwKrmKCFshrm6NH3rAG__TRliSdwWfdbobd9DwVYzPg8E8YqkK7nypALlQyXHBDLr_fUt7zf8z1pFy_MM5Ck8NklSA16ixuN9xhXyCACZ3eNVPAWIQpiQ3FHp1oq0xBTtL6sNGoUjgPAlI6g45stxQPz-aYClTSZwslkQPcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس مسائل استراتژیک: نقد‌هایمان را «مشفقانه» بگوییم؛ باید از شخصیت «عراقچی» و «قالیباف» حفاظت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/673907" target="_blank">📅 23:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673906">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تغییر ساعت ۱۵۰۰ مگاوات در برق صرفه‌جویی می‌کند
سیدجواد حسینی‌کیا، نایب رئیس اول کمیسیون صنایع و معادن مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از ظرفیت‌های عملیاتی برای کمک به ناترازی انرژی در شرایط فعلی، بازگشت به تغییر ساعت است. برآوردهای کارشناسی نشان می‌دهد که این اقدام حدود ۱۵۰۰ مگاوات در مدیریت بار شبکه تاثیر مثبت خواهد داشت.
🔹
طرح پیشنهادی در این زمینه تدوین شده است و امیدواریم در نوبت رسیدگی قرار گرفته و به مرحله اجرا برسد.
@TV_Fori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/673906" target="_blank">📅 23:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673905">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVIPu3P6VQyX0zq7QY88n1yCaxslyCTkt1xp3W9oigZ_ouYkg16bOXqrn6vzaLN8ERp1z4Iekzy-xsVB1xKbVuNHNObzqrFnkK_HdRK7NZwAmKcgv5sd-m6YgxAtB3QN_ceCxbizYO3x4eEjQszaNCIbRdXHBmObX4JZuWUQ_PyJrr_MZMSW5e9yX0xMDZhrIevrXrp8FR1Fn3f7dSPSwS-upTAxZhBe6HQ3EndXHzcYkf-XAX1E26qgl6E07bBpaGw4MfDC56IGD-AExzXgRV-IXG3H0GWI67KOnGbsKF5D3EGgU40bKpjeJeZqgMM5TKQgKy0uJL2gkqwe2TSzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر جدید بریتانیا استفاده ایالات متحده از خاک بریتانیا برای انجام حملات بمب افکن به ایران را تایید کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/673905" target="_blank">📅 22:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673904">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۰/ هلاکت تعدادی سرباز در هدف قرار گرفتن مجتمع محل استقرار نیروهای ارتش تروریست و کودک‌کش آمریکا در منطقه‌ی الرُکبان اردن   روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت بصیر و همیشه در صحنه ایران اسلامی،  با دعای خیر شما عملیات تنبیهی رزمندگان…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/673904" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673902">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpFZFzII_KPcGRmPesVkAlxWdqKwHlThYovMN6RVvcvIa7-VGmOcBHPMI4rxmh-NOZUEUIzIc9hGEupSsitLBJ7vJ6J4ZKXNa75-R2Cmhwvt-17njcDlFJ9x-V_ja8O0aPtPmdXTCHdedewvW75mBADuhosExrVvIbfy_HrcjTZBOegp3NZ4rIrnb5Y287UwJqiy9IsU3uizKqUv2iYLtJ76P0DzNIvM75XKZZMw-3Sr_ESjvLyYMsdXrzsW5KpCmo0RfmGjweQodiB8OkK_Zjyv5qlk5uJj3RcaTPt03kRwI9pTZBBgsVESoZF4kvG6ahCXhOQQ1ehMlL6ynljjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عدالت از منظر امام علی (ع) چیست؟
🔹
از نگاه امام علی(ع)، عدالت تنها اجرای قانون نیست؛ هنر و توانایی فهم درست موضوع، دانایی عمیق بر قوانین، داوری شفاف و بردباری است. کسی که حقیقت را درست نشناسد یا در برابر فشارها آرامش خود را از دست بدهد، هرگز نمی‌تواند…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/673902" target="_blank">📅 22:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673901">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تحلیل جنجالی مصطفی خوش‌چشم از تصویر مقاله ظریف در نشریه فارن افرز: تصویر می‌گوید موشک را بده تا بتوانی نان بخوری
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/673901" target="_blank">📅 22:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673900">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71aa646a5e.mp4?token=Vnr38bAOu-LJ0GEg8-E4nO394OULhQjleJT9ctOSHtcIYbowtV0YkPpmjpJBScBo2VqMrlkvCZuibv89yIuT31NKGVvt9zStPpktnB_OnCBpit_I5-z0_WU-nzHjTWU2yNJCqHDI3xgzpH4cX_9Mdd6TQv6qdMiUfPZbN3sLYWrJsxWrYKMnBC3TvvFND9xTAvV4O-iK0daEDsnZBLGYNmZktrMho0AraUk5ByaxyLoXkligplIZZywPSbuFDOdueBy4zZ8d2VqYrIq2FfMuGMc_rBSM69ruobJj1OdNa7E0kJrEDqadtMHxb9iU5ltkyVdgJYeK-BiYnVPc0ubrDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71aa646a5e.mp4?token=Vnr38bAOu-LJ0GEg8-E4nO394OULhQjleJT9ctOSHtcIYbowtV0YkPpmjpJBScBo2VqMrlkvCZuibv89yIuT31NKGVvt9zStPpktnB_OnCBpit_I5-z0_WU-nzHjTWU2yNJCqHDI3xgzpH4cX_9Mdd6TQv6qdMiUfPZbN3sLYWrJsxWrYKMnBC3TvvFND9xTAvV4O-iK0daEDsnZBLGYNmZktrMho0AraUk5ByaxyLoXkligplIZZywPSbuFDOdueBy4zZ8d2VqYrIq2FfMuGMc_rBSM69ruobJj1OdNa7E0kJrEDqadtMHxb9iU5ltkyVdgJYeK-BiYnVPc0ubrDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که یک ایستگاه پشتیبانی زمینی و یک مرکز تعمیر و نگهداری مربوط به یک بالن شناسایی آمریکایی در فرودگاه اربیل در شمال عراق، مورد اصابت قرار گرفته است
🔹
به نظر می‌رسد پهپاد با دقت هدف خود را مورد اصابت قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/673900" target="_blank">📅 22:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673899">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d504030f.mp4?token=JhPQA3xIIA33zWnZPXlZqB0-QX_fBGR-WSiGtOobUjQq36ZTTNEK9yq7N2ZSXl3zddgAG3WspyWQF452HcPd0jA3HJWf3E2fqWtHCjJeagpAmUYSPSGEgk95xicRiJyB7vcFLgR9Tpa1H4AN0w3bcWin-hsvo5Q_vT9qAWXQH_XfKhIi52yGUlZtixX7o2VyeBfPa-5kf49SUIgFtR7Y0fKmJmB8aHym7E5qBRJhgcl7r0ySa8siI19u2_zhVsqLMl4pBsvFLuQY1AdXf_lAMmWVn_hxzEjkxNZu_087BQVT4RDsGesPpNE7pB2xTa-8DbgdaTVsBTdOQEuK8DvW04diFmJWwddu4W62ywcy7rjzQ5XELYnUykU6dLzpxf_AWmStOcdbzp2plhsUmWOcIK-j-14DjBXv_OPn-_fjGY5LtAI4ZAl-ZMet3ol4yBHmVqLSPtxYCBAEdvvz0qstMmXYDRzsStPHvoA2eQZ5mP5UkseFKMhE_eKTGL_4FAM8SrfJ8HbN1Uh7hxohQRDcOHWhIFfzhAalZq0zvGfKUgvJpezZkjMFaUenYPZS_ZwqLoBcPVZ3dlv4BkBAXrT8QkYO0ztVEehfpbuqbq2MkDuO0gqGn5iES3pSWpVw76f1oeLurTonzjZ8AC9zVzrdT1hDEooBhJMWZQmYyC7vH84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d504030f.mp4?token=JhPQA3xIIA33zWnZPXlZqB0-QX_fBGR-WSiGtOobUjQq36ZTTNEK9yq7N2ZSXl3zddgAG3WspyWQF452HcPd0jA3HJWf3E2fqWtHCjJeagpAmUYSPSGEgk95xicRiJyB7vcFLgR9Tpa1H4AN0w3bcWin-hsvo5Q_vT9qAWXQH_XfKhIi52yGUlZtixX7o2VyeBfPa-5kf49SUIgFtR7Y0fKmJmB8aHym7E5qBRJhgcl7r0ySa8siI19u2_zhVsqLMl4pBsvFLuQY1AdXf_lAMmWVn_hxzEjkxNZu_087BQVT4RDsGesPpNE7pB2xTa-8DbgdaTVsBTdOQEuK8DvW04diFmJWwddu4W62ywcy7rjzQ5XELYnUykU6dLzpxf_AWmStOcdbzp2plhsUmWOcIK-j-14DjBXv_OPn-_fjGY5LtAI4ZAl-ZMet3ol4yBHmVqLSPtxYCBAEdvvz0qstMmXYDRzsStPHvoA2eQZ5mP5UkseFKMhE_eKTGL_4FAM8SrfJ8HbN1Uh7hxohQRDcOHWhIFfzhAalZq0zvGfKUgvJpezZkjMFaUenYPZS_ZwqLoBcPVZ3dlv4BkBAXrT8QkYO0ztVEehfpbuqbq2MkDuO0gqGn5iES3pSWpVw76f1oeLurTonzjZ8AC9zVzrdT1hDEooBhJMWZQmYyC7vH84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشورهای عربی دست از پا خطا نکنند!
🔹
کشورهای حاشیه خلیج‌فارس معضل بسیار بزرگی دارند که اگر همراهی آنها با آمریکا ادامه داشته باشد، شاید ایران ناچار به یک تصمیم مهلک برای آنها شود.
🔹
ماجرا چیست؟ در این ویدیو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/673899" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673898">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
آتش‌سوزی در ارتفاعات دراک شیراز
رئیس سازمان آتش‌نشانی و خدمات ایمنی شهرداری شیراز:
🔹
آتش‌سوزی در ارتفاعات دراک رخ داده است.
🔹
در حال حاضر ۹ ایستگاه و تیم‌های عملیاتی آتش‌نشانی به محل حادثه اعزام شده‌اند.
🔹
اخبار تکمیلی درباره ابعاد حادثه و روند عملیات متعاقباً اعلام خواهد شد.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/673898" target="_blank">📅 22:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673896">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326e59136a.mp4?token=OCl9F8eqcnpCryjCTzMxxGOtWUsbIvPTdtVc6E4vUcWvyTzpzHAMLdOmbZOrrjh9WtnhJ_KPYCohf87fWI7nbEYcV0h8OeavTcruSKkx1FSvEJxQ8zORf-9uymRY3-kFGw1M-1ZLrilK-_JYigulRh-eaaZvueYGGAcaizzONoDfLug6QjXb5bQF_bCQLf7lxwJ6__zyhRYjrSlcSiSP3aiE-OCVgyOuFaWKUaDc7TzL1sbYpj8qWILeilH4D0sdzka6vjdU7L-PWOpLNNArryCQ9f1_cGEPIMe-MDkT0UtjDCMr88zSb8J2AwPdJlAC61EtKdrNVW6j_meHaGRISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326e59136a.mp4?token=OCl9F8eqcnpCryjCTzMxxGOtWUsbIvPTdtVc6E4vUcWvyTzpzHAMLdOmbZOrrjh9WtnhJ_KPYCohf87fWI7nbEYcV0h8OeavTcruSKkx1FSvEJxQ8zORf-9uymRY3-kFGw1M-1ZLrilK-_JYigulRh-eaaZvueYGGAcaizzONoDfLug6QjXb5bQF_bCQLf7lxwJ6__zyhRYjrSlcSiSP3aiE-OCVgyOuFaWKUaDc7TzL1sbYpj8qWILeilH4D0sdzka6vjdU7L-PWOpLNNArryCQ9f1_cGEPIMe-MDkT0UtjDCMr88zSb8J2AwPdJlAC61EtKdrNVW6j_meHaGRISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسربچه دوست‌داشتنی فینال
جام جهانی فوتبال
🔹
شیطونی‌های برادر یامال در جشن شادی اسپانیا پس از برتری مقابل آرژانتین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/673896" target="_blank">📅 22:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673895">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
کویت سفیر ایران را احضار کرد
🔹
وزارت امور خارجه کویت ادعا کرد نفتکش «کیفان» عصر دوشنبه هنگام عبور از تنگه هرمز هدف قرار گرفته و در پی این حادثه چند نفر از خدمه آن زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/673895" target="_blank">📅 22:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673894">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رسانه عبری: الجولانی برای عملیات علیه حزب‌الله آماده می‌شود
شبکه صهیونیستی «کان»:
🔹
با وجود اینکه مقامات دولت انتقالی دمشق به صورت علنی از مخالفت خود با ورود به مساله لبنان سخن می‌گویند، اما در عمل دمشق در حال آماده شدن برای انجام عملیات علیه حزب‌الله است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/673894" target="_blank">📅 22:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673892">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR-KiskaLIVsA3zL5RUbKxAtrj3DiJtiQOn6VNNG1s3sJQTG2aWIDLz1-uR2XSw7_4AB4bpwyVEL6Qt_VPQdEL7PL1FEmeUHNp-YBcqj6_ILkvn87od7ZOVojo51psuOTW47TkxwucAcG9VHdkj8y19OUN7g4sOofjqCiYrtMJNS1DltdAnkJvqERBl96uUO48ZVJAWbv3hlvGO3srtCaZ8myCgxusA07GtcvkqN5dyU0gn0KLXFbI5zD2B1gslPgFP3tHCbdYtmRo4BkUbnbuOQPuzyipaOPLvVQNjBMbG0m-Z33Tf6_rCeJxUmOddCmTgH22OXp5AXVfYYXc1xmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزبانی از دشمنان ایران و همدستی با آنها، نشانه ناسپاسی و فقدان آینده‌نگری است
سخنگوی وزارت خارجه با انتشار عکسی تاریخی از سال ۱۹۹۱ یادآور شد:
🔹
ایران در سال ۱۹۹۱ با وجود حمایت کویت از صدام در جنگ تحمیلی، به درخواست این کشور، تیمی ۴۷ نفره از متخصصان خود را برای خاموش کردن ۲۸ حلقه چاه نفت در میدان برقان اعزام کرد؛ عملیاتی که به‌عنوان یکی از بزرگ‌ترین مهار آتش‌های نفتی در تاریخ ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/673892" target="_blank">📅 22:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673891">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
بازسازی زیر سایه تهدید؛ فرزانه صادق در کنار کارکنانی که خدمت را تعطیل نکردند
🔹
فرزانه صادق، وزیر راه و شهرسازی، در جریان بازدید میدانی از محل آسیب‌دیده راه‌آهن بندرعباس، در کنار کارکنانی حاضر شد که در شرایطی دشوار، هم‌زمان با تهدید حملات مجدد، حضور پهپادهای دشمن و گرمای بیش از ۵۰ درجه، مشغول بازسازی خط ریلی بودند.
🔹
این تلاش بی‌وقفه، زمینه ازسرگیری خدمات جابه‌جایی مسافران از ۲۷ تیرماه را فراهم کرد. خدمت، حتی در روزهای سخت، ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/673891" target="_blank">📅 22:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBDJH2dMtIFUwPXrGrU8NXB84O1S2PvVAJPtQH-dAK8vW-7QsJuxHsPUW4wiG4AIC9SJslM4cKQNPnl0rUtQAJHWddjvSyCiKjcQtvuNjUPUoJV_8J_Gs0J7EW4fLxvnOi1Bhb4rVTaL87r9Z8cVpKAqYnhCE_mezwp5ihcZFThsOcev0Xl6ksMiQEZ6P0db5e_BDzRv97abZKfBEYJlTAR4WYwCih4ror0AZoRZMXCnTwD91K95L4k3WjFUK0Y8ZAxcQDN8OQKr_C_Fl8wZ6I-h_l7yx0Dv5U7_B1_mND1aB5Vh61f8tNdntTRjod5ACjrbWZQ4k8VC_6VQhSaCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام چند هواگرد متخاصم در ارتفاعات شیراز با سامانه نوین پدافند هوایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/673890" target="_blank">📅 22:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
نتانیاهوی خبیث، دقایقی پیش، از عون و سلام، چاکران درگاه ترامپ در بیروت، اینطور تشکر کرد: از دولت لبنان بابت شجاعتی که نشان داد، تشکر می‌کنم #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/673889" target="_blank">📅 22:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673888">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNJsSsAgiVQpU_SCGWJGmtmBA5UxQ0Du3yN--4j0o4hl1ehFGRswl3th7yq4CEB2ZDmG1Wt243EaegfUEwOGXaoCdv2RvFcFshkLdOEtD0WPM1PJKHNllFnauLmfbb9uMlq-nIbqW4opFGRm-Z1pS0dlrklTcQobnqXMlrbwZYUVX286uvbChQ2mDq_ZoMZW6W5Xdrdq7P49JetdmWdscbzSxCDrS0cct6A1-lZx3R00K40WI4QmxoS4P2-k_TP0EVfWGGJY438Q1wzLW4qw6V0eqdAV6csnA7TBIuB-vayEZP4RyDgCryJRlf_br04UrixK2hkzv-aJ_da0x57Lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوب؛ غول درآمدزای ویدئو
🔹
درآمد جهانی یوتیوب از ۱۵.۱ میلیارد دلار در سال ۲۰۱۹ به ۴۰.۳ میلیارد دلار در سال ۲۰۲۵ رسیده و در کمتر از هفت سال حدود ۲.۷ برابر شده است.
🔹
بیشترین جهش درآمد یوتیوب در این دوره، بین ۲۰۲۳ تا ۲۰۲۴ رخ داده و درآمد این پلتفرم از ۳۱.۵ به ۳۶.۱ میلیارد دلار افزایش یافته است.
🔹
بخش عمده درآمد یوتیوب از تبلیغات تأمین می‌شود و با رشد تولید محتوا، افزایش کاربران و توسعه سرویس‌هایی مانند YouTube Premium، درآمد این پلتفرم طی سال‌های اخیر روندی صعودی داشته است.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/673888" target="_blank">📅 21:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673887">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
منابع: منطقه‌ای که در بحرین هدف قرار گرفته، محل حضور نظامیان آمریکایی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/673887" target="_blank">📅 21:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673886">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb76U0BxJsuA1NWxZw8xZnm5m3xuNpzyqBmH3jWg_gkXO8GXCvnsdopp-7WYJKQE7JLmpCODfSqPJbxJVhcGwbVaJ8W4hX652wY2Un-ky8fgMuBReSYCCHF62qvqzcU-Cn8us9HzF7eiYJFiB828FjHwtrtepaNZyNdHTNDx9lXOa9aAkMKyINYS84zTg47N63vh4Sjx73jzqYucDYxTgly30Q9u7lHLqIT0GLvBGZQoIDnTn2bQCeJcSiRKUEY3-l3vsu4FS4CLsYrxGBfTHBhHo_3rQqlSxnv_PfRi70vTTj7hORCMt00FLEJK3G7nVqwxwu67OCa_Chw2xvpubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱.۵ میلیارد دلار سوخت‌رسان آمریکایی در تیررس ایران
🔹
حملات هوایی ایران به پایگاه‌های آمریکا در منطقه باعث کوچ زیرساخت نظامی این کشور به اسرائیل شد.
🔹
تصاویر ماهواره‌ای نشان می‌دهد، حداقل ۲۴ هواپیمای سوخت‌رسان آمریکایی در فرودگاه رامون ایلات اسرائیل پارک شده‌است.
🔹
ایران در طول جنگ ۱۲ روزه و ۴۰ روزه بارها منطقه ایلات را هدف حمله قرار داده است.
🔹
هر سوخت‌رسان آمریکایی ۶۵ میلیون دلار ارش دارد و تنها یک باند فرودگاه رامون ۱.۵ میلیارد دلار تجهیزات در خود جای داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/673886" target="_blank">📅 21:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673885">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbe7bed94.mp4?token=AyvINQ_upuJBPiDxc3kEIc_gR6y11pQfPWeyDLfaHcT4x1dy_tB6VncDZRGzC4nEkl0LM5-qVYvZEL5J_AazbMsq2d-EkKZIZz1WZb9U74KOAI26IklZGwul9pRZTPatV76p0Vyl_9hjhWk7LqwDLkb11gcqoQBsswmdzVqHXe8yZCOes5OIkYQ_04qAdkT4q6xqmTA6GjTe7Cp5nT1gIYus7pNrWgP8wr8jlCqvCKDI37igTV7xImEn-B2ujo6CCOw9I-8RjwpyrURI18MUyAzBF4JDmsvFa83KUZpKI_UUfY48FEjPlb3ZPmZLE3xz_lBeaUVPQp8v6POG9pVbeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbe7bed94.mp4?token=AyvINQ_upuJBPiDxc3kEIc_gR6y11pQfPWeyDLfaHcT4x1dy_tB6VncDZRGzC4nEkl0LM5-qVYvZEL5J_AazbMsq2d-EkKZIZz1WZb9U74KOAI26IklZGwul9pRZTPatV76p0Vyl_9hjhWk7LqwDLkb11gcqoQBsswmdzVqHXe8yZCOes5OIkYQ_04qAdkT4q6xqmTA6GjTe7Cp5nT1gIYus7pNrWgP8wr8jlCqvCKDI37igTV7xImEn-B2ujo6CCOw9I-8RjwpyrURI18MUyAzBF4JDmsvFa83KUZpKI_UUfY48FEjPlb3ZPmZLE3xz_lBeaUVPQp8v6POG9pVbeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: حوض نقاشی
🔹
ژانر: درام اجتماعی، خانوادگی
🔹
خلاصه: «حوض نقاشی» به کارگردانی مازیار میری، داستان رضا و مریم، زوجی با کم‌توانی ذهنی است که با تمام وجود برای ساختن آینده‌ای بهتر برای فرزندشان تلاش می‌کنند. فیلمی سرشار از عشق، امید و انسانیت که با…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/673885" target="_blank">📅 21:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
لحظۀ اصابت موشک به مقر ترویست‌ها در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/673884" target="_blank">📅 21:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673882">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d9d5e5da.mp4?token=DPxRW2UGFb6SskMsKjgQApo2A4tu5SoC-_4ykys1jkNkG6DRY6HqeIjtooMzZjjGVLxvYxJp6CdEoYYqQ8JhZmiCxpTg6-4ISjviabW8IXbHWA2rqPH8DEi7s5GKWCvy2H3tPV-CocyetUVk1xrFchpS1hKs5-THgdcakBaRxAsWDMQJ2NmZUkewPtyfgiHDz2QuB2VpuQdEjArIgMp-3S72PdfwTH1_T-UqUeMuZ8sZ3pFs0Xv-K9QYgkAmBN1Xdm6J-NE8qjVegn5TbHhKEQdtN8ZZC3QMgpwr7MQT8LeXRrmHBGc7WUgaPa-Kksp_4l7wlTqrg8fgs9va8ndgAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d9d5e5da.mp4?token=DPxRW2UGFb6SskMsKjgQApo2A4tu5SoC-_4ykys1jkNkG6DRY6HqeIjtooMzZjjGVLxvYxJp6CdEoYYqQ8JhZmiCxpTg6-4ISjviabW8IXbHWA2rqPH8DEi7s5GKWCvy2H3tPV-CocyetUVk1xrFchpS1hKs5-THgdcakBaRxAsWDMQJ2NmZUkewPtyfgiHDz2QuB2VpuQdEjArIgMp-3S72PdfwTH1_T-UqUeMuZ8sZ3pFs0Xv-K9QYgkAmBN1Xdm6J-NE8qjVegn5TbHhKEQdtN8ZZC3QMgpwr7MQT8LeXRrmHBGc7WUgaPa-Kksp_4l7wlTqrg8fgs9va8ndgAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ اصابت موشک به مقر ترویست‌ها در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/673882" target="_blank">📅 21:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673881">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhwFJWAX4GmHVhI0clH2rE-qPxkJGNlLL_qqhskzbyerqKr46fI_i1scQLfOhjesI6hDgVXjitI-f95-7UKaJVqyJ2Ce3BzgZCIPoAc00NNCdwP1xUvYXfTiMRxbOj7ULmH25JD_vwJlqspVuR6rTXlg_FOpWyvF7M5X_YA_AJ5NAI8T4Z3vkaTE2KVkv25vmvJqVbnmR0GtkWwlIAYVTRDlMrONeXMXSFJomrW-Ak4qoHteDPywiNOaOnlvH3esCwuckK2ajwECVY9vKPuGROZJAFOM7B6aJJYKey2mSPTAZuewr8Oz33Fjr3JG_XXBmIn1J2QZil2phI1I3GMexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر آرزوی
زیارت اربعین
را داری، این فرصت را از دست نده.
🔸
به همت هیئت قرار،
۱۰۰۱
نفر به قید قرعه عازم سفر کربلا خواهند شد.
🔸
اگر می‌خواهی به نیابت از رهبر انقلاب در پیاده‌روی اربعین حضور داشته باشی، همین حالا عدد
۲ را به ۳۰۰۰۱۱۵۲
پیامک کن و در قرعه‌کشی شرکت کن.
شاید امسال، نام تو در میان زائران اباعبدالله(ع) باشد...
🏴
🤍
@Heyate_gharar</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/673881" target="_blank">📅 21:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673880">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fujFvC1hZPl8L5Ah8P-5oIWv9Afy62OHVfk6nY60yIfGdzshRLxIa6FYTZBO939pWX4P3PKiZAf9TQFCatH7KYlddODUmlpq5ChM99UWg6aGbP0qafdftEMfpjljbgYTmdad7vTiekoq30f9Agou4dMcg0FFbJTHubIvd_QmutgJxbxW-1FJf0W_FmDM9xpwukcC78VChivJBD-5v6EZ2045wtg1koe-YjKezVnhKS2107LPUBfKcTDFEulwL6a6XYjx9m45FSe1YyH604YbaPcFvfOZku2Gy8io5S7dc1Aa120xsUdzpgy34kRGr0VYrX6I3VS9xT_4S2OGLSIfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
براساس همین یک توییت می‌توان یکبار اختصاراً تاریخ تحولات سیاسی معاصر را توضیح داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/673880" target="_blank">📅 21:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673878">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCWVg2ajApHQW72ejor3bVl1PJcAN-CUZhhXp-6A6-7rwPjoF-xuwZqCUcpPGcpEm-0U8QDEoA8fZ3dFt6E-EXydGVgEJBQpxz1EyX_aRBb2F1VK0EiXeRDsmjreCnvlzrl36rbOQhmi19hmSB3wyU1zky-ZPiC6Rku6M14STPdewWZhCdcWowTVuQRxJRvyfLRMfbOY2nGUlg9XH9AJijXX7sQ53h-Uqvk5rwVSV8Arx_TikmFb9TCbtaRuiJsFQ1But6H0ZXD4oZ42W3vB8EYVgXIyLe4lmw4wIcsQXpD4zRD_vU6yd2W0G_XyzBKZWLaMFptuXcDAEmFdul2Plw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد رآکتورهای هسته‌ای فعال در کشورهای مختلف جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/673878" target="_blank">📅 21:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673877">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6af6d1f6.mp4?token=HDZX7pS_uAzT3bbjE_9ep9TNa5FBPFiFNsmp6F8SbhNnS4IbearV9BgdTv7XrRXhKHUfcAR9bHFbmfx6xY41q6NMp2BoouM3e0UOetYboWF9W31-WJgon8IeJmmWaRapA5S1zYxrjQ4nOKhrdd_qzSsioOS5s7SyOQhiguywf0UNXByVOFpz16fQEp7nSPHYrdLrLPJqi56A9CZUZwHGUU1bavuh3nrEX4C0qAg-koLKY3AjpriKTzgwWVmWX8dak3fF8JW8ufY7d8lJjfcydQnXFOxgGI5Oma_Prx4ynOOCAut5tXnTyZwr2R3W6AQZRjBgmwPURxfSxqNwclNs-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6af6d1f6.mp4?token=HDZX7pS_uAzT3bbjE_9ep9TNa5FBPFiFNsmp6F8SbhNnS4IbearV9BgdTv7XrRXhKHUfcAR9bHFbmfx6xY41q6NMp2BoouM3e0UOetYboWF9W31-WJgon8IeJmmWaRapA5S1zYxrjQ4nOKhrdd_qzSsioOS5s7SyOQhiguywf0UNXByVOFpz16fQEp7nSPHYrdLrLPJqi56A9CZUZwHGUU1bavuh3nrEX4C0qAg-koLKY3AjpriKTzgwWVmWX8dak3fF8JW8ufY7d8lJjfcydQnXFOxgGI5Oma_Prx4ynOOCAut5tXnTyZwr2R3W6AQZRjBgmwPURxfSxqNwclNs-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی منتشر شده در رسانه‌های اجتماعی پلیس نیویورک را نشان می‌دهد که بعد از قهرمانی اسپانیا به هواداران کمک می‌کند تور دروازه فینال را تکه‌تکه کرده و با خود به خانه ببرند
🔹
اسپانیا در این بازی با شکست آرژانتین، برای دومین بار قهرمان جام جهانی فوتبال شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/673877" target="_blank">📅 21:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673874">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
♦️
منابع عربی: لحظاتی پس‌از به‌صدا درآمدن آژیرها، یک موشک‌ به نقطه‌ای در پایتخت بحرین اصابت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/673874" target="_blank">📅 21:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673873">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf309493d9.mp4?token=O1SYASCXFu0RHyq4PgGOLsnHCK5LWtxRwx940FYP5XIE79ZtHA9rpr2hwWXiNiT30VtSCY3rZ_Ln3BN0kwt5KSz4NypZ-gRta5fZZ3RpQEdthz5CFZEnHs2QG6EwZ_l6uH-WpUaoBTHEPgWkTmUw0R9N6RPHko4UwNO7glcIEvNMQo6FLNuZUzsUQuBClyxmXdAAFw6KNVlKInbj4ohrQ9pTrDFfcuqwZISm-gh8ZxF-oHRa69zGpfe5gDV3V8JpQA3aN84tfkNSVPyRZ38fyDzQd5aJHF-f95zD0PxRzLF9l8syfOlkManyRWR2rh8isGtxXiOrlcVpw-yVufLeME18yvqn6HGMsCK13kUn6ZsZpkK_e9tYYbWd6pw-pDNwFJzpV_0Vct_QqbqDE5WOnUrQGvUnkroacmGS9irsiNQ-16OBdBk-JBUvhSB3hfHBs8C1_GVA9BvMKhff6pD6CzbqTdLj8J7utU5WfqRTFA4UKQnlmO8r8_kxQ4wwcT3fdFcCDgMk8PzFxmLYBP-QldAsUlNZUx5DhCRq74CsOu4sRDqXdeXLkNZFM1IuGuVYZ5mt41gUWDyVtaHrBb_4T5pKwM959pBjV8yfrZVfaTRC3PytK18-Gla7cMwYthMdUX6WzkZQcGbE-X6dw67sUh0NRHNw0Ga9ZfgjTVTrrA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf309493d9.mp4?token=O1SYASCXFu0RHyq4PgGOLsnHCK5LWtxRwx940FYP5XIE79ZtHA9rpr2hwWXiNiT30VtSCY3rZ_Ln3BN0kwt5KSz4NypZ-gRta5fZZ3RpQEdthz5CFZEnHs2QG6EwZ_l6uH-WpUaoBTHEPgWkTmUw0R9N6RPHko4UwNO7glcIEvNMQo6FLNuZUzsUQuBClyxmXdAAFw6KNVlKInbj4ohrQ9pTrDFfcuqwZISm-gh8ZxF-oHRa69zGpfe5gDV3V8JpQA3aN84tfkNSVPyRZ38fyDzQd5aJHF-f95zD0PxRzLF9l8syfOlkManyRWR2rh8isGtxXiOrlcVpw-yVufLeME18yvqn6HGMsCK13kUn6ZsZpkK_e9tYYbWd6pw-pDNwFJzpV_0Vct_QqbqDE5WOnUrQGvUnkroacmGS9irsiNQ-16OBdBk-JBUvhSB3hfHBs8C1_GVA9BvMKhff6pD6CzbqTdLj8J7utU5WfqRTFA4UKQnlmO8r8_kxQ4wwcT3fdFcCDgMk8PzFxmLYBP-QldAsUlNZUx5DhCRq74CsOu4sRDqXdeXLkNZFM1IuGuVYZ5mt41gUWDyVtaHrBb_4T5pKwM959pBjV8yfrZVfaTRC3PytK18-Gla7cMwYthMdUX6WzkZQcGbE-X6dw67sUh0NRHNw0Ga9ZfgjTVTrrA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت دوازدهم مستند احیاء و حقیقت | «جوانه می‌زنیم»
🔹
گاهی، پس از عبور آتش، نخستین نشانه زندگی نه در هیاهوی ماشین‌آلات، که در جوانه‌ای کوچک نمایان می‌شود.
🔹
در دل دیوارهای سوخته، میان قاب‌های شکسته و سکوت پس از حادثه، هنوز نشانه‌هایی از حیات نفس می‌کشند؛ گویی…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/673873" target="_blank">📅 21:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673872">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auOMfW2zlsXK7L2iObBlnrM8xVOLZeGAGvalFnkkF6CLX2MR8O7NfjvsonT-frswkif7MuDY_v1WNJ9l6KPYHksCsRwnjX_Y2prd0-TsEzndX7vWkCZeopqRboRDo8LzfQvPvEjSVk9aKkaXYxoaDrjVBRteAlOVmCqIRKqlycSNmDSnUkgkVPFfOa73kI4-XVtq6U3BO8upbHkE3Xpd1xGWYLsUWZQFEEzgoKpxV2nBlzG-PIQZGTxCgZ9vCVYpjhiQEclxOiiPbuG3kkCUHtgf4snaOPykqKrWEwkT8Qt7vpFiMHiFfo-FH-USTipfYtSnVev8y9X5s-LVT3ayYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت سیاوش اردلان، خبرنگار BBC: ابتدا همه فکر می‌کردند حملات اخیر امریکا مقدمه حمله زمینی است ولی نتیجه ضربات ایران نشان می‌دهد امریکا باز هم بدون برنامه وارد عمل شده؛ یک مقام نظامی آمریکا می‌گوید ما قابلیت دفاعیمان در برابر موشک‌های ایران مستهلک شده اما کاخ سفید به حرف ما گوش نداد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/673872" target="_blank">📅 21:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673871">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f568acff.mp4?token=UpZVSOvckPdeeASt7b3ns2tcTy9MR5ILq70X1g3-vafZSSY01xXkgt5s8hOF_JgDXoF8EM6QU8eKcaZNjUuuK2K62WARW2ZFeyqtCEKh0V59soqxy1zTH75KRLARcbV7oKKQNra6XYNJ4PCXfEUuiXYyNAxn9WKu_o-CX3ZhhwIIGfV2fkJW25NrOBdHQQ9KBXo_phQl-Spm0aIchaMbWhMTWhCcK2WfLjB6Nz2iOhJR7p9Wql9WpevDEZqB1EeMAzzgXqePm1hHTardnxXpsczke1OyrNt2cZLznGwkMAaEgrQqp-6m4Dfux9yaWqsJDxU-8z7bMvvNmPMyR_d3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f568acff.mp4?token=UpZVSOvckPdeeASt7b3ns2tcTy9MR5ILq70X1g3-vafZSSY01xXkgt5s8hOF_JgDXoF8EM6QU8eKcaZNjUuuK2K62WARW2ZFeyqtCEKh0V59soqxy1zTH75KRLARcbV7oKKQNra6XYNJ4PCXfEUuiXYyNAxn9WKu_o-CX3ZhhwIIGfV2fkJW25NrOBdHQQ9KBXo_phQl-Spm0aIchaMbWhMTWhCcK2WfLjB6Nz2iOhJR7p9Wql9WpevDEZqB1EeMAzzgXqePm1hHTardnxXpsczke1OyrNt2cZLznGwkMAaEgrQqp-6m4Dfux9yaWqsJDxU-8z7bMvvNmPMyR_d3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آدم از عشقش می‌تونه بگذره ولی از وطنش نه #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/673871" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673870">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cc59af399.mp4?token=cjoPWOqMLAMe43ETsSWz6w4KmddNQC9ut2nRHJw5_PaVN-i-4j7l8VV5vmdTrBW-8BvHRyBx6eGg8y1OYqIcJ2yEBkQEoySX8Z8yxfKWHc-_dED38vSnBWSrqxmj-0raBwH8OHIM0MVd0zdoc0Hlw5mM4vWPDWbyxmEPDvV0Uw0SoBtb4gcVznjtpdf8OUR1G8I_htaprZyNMxEsvfWGlYdCIHuX3ZF5yjeVqBZv_mtZNLo5VJAi69JgYsiEePZ-GgUQcZ1SRK3jp8uTllWgjmVzoPh8mVjnaK13Sh-yLvkQsGn_cSBgNwWMoVkg6I5L95DPV_ANU-jNXFF1MzUGFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cc59af399.mp4?token=cjoPWOqMLAMe43ETsSWz6w4KmddNQC9ut2nRHJw5_PaVN-i-4j7l8VV5vmdTrBW-8BvHRyBx6eGg8y1OYqIcJ2yEBkQEoySX8Z8yxfKWHc-_dED38vSnBWSrqxmj-0raBwH8OHIM0MVd0zdoc0Hlw5mM4vWPDWbyxmEPDvV0Uw0SoBtb4gcVznjtpdf8OUR1G8I_htaprZyNMxEsvfWGlYdCIHuX3ZF5yjeVqBZv_mtZNLo5VJAi69JgYsiEePZ-GgUQcZ1SRK3jp8uTllWgjmVzoPh8mVjnaK13Sh-yLvkQsGn_cSBgNwWMoVkg6I5L95DPV_ANU-jNXFF1MzUGFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
منابع عربی: لحظاتی پس‌از به‌صدا درآمدن آژیرها، یک موشک‌ به نقطه‌ای در پایتخت بحرین اصابت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/673870" target="_blank">📅 21:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673869">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پاسخ به یک نگرانی بزرگ؛ وضعیت ذخایر کالاهای اساسی اعلام شد
محمد جواد عسکری، رئیس کمیسیون کشاورزی مجلس در
#گفتگو
با خبرفوری:
🔹
در حال حاضر، حمل‌ونقل و ترخیص کالاهای اساسی بدون هیچ‌گونه اختلالی ادامه دارد و در روند تأمین اقلام مورد نیاز مردم مشکلی وجود ندارد.
🔹
حتی اگر حملات به زیرساخت‌ها تشدید شود، ذخایر کالاهای اساسی به میزان کافی پیش‌بینی و تأمین شده و از این بابت نیز جای نگرانی برای مردم وجود ندارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/673869" target="_blank">📅 21:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673864">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
روایت تکان‌دهنده مردی که پس از مرگ موقت، عذاب گران‌فروشان را دید
🔹
00:08:30 پرسش و پاسخ در مورد امامان دینی
🔹
00:16:40 گناه گرون‌فروشی و فریبکاری در حق مشتری مغازه
🔹
00:25:10 نظاره‌گر حادثه‌ شش‌ماهگی‌ام در حرم امام رضا (ع) شدم
🔹
00:36:10 درک عمیق از عذاب رباخواران و زنان بدکار
🔹
00:40:05 تغییر احوالات من و پیدایش نور با صدا زدن نام خداوند
🔹
00:54:50 رؤیت اتفاقات روزمره توسط روح انسان در کما، از نظر علم پزشکی
🔹
01:01:00 تغییرات رفتاری و اعتقادی بعد از تجربه
🔹
01:03:50 آثار مال حرام در زندگی دنیوی
🔹
قسمت هشتم (تاوان)، فصل پنجم
🔹
#تجربه‌گر
: سید حسین موسوی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/673864" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673862">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF37BqzujQoNdRmLlWMsa_H_04ESAP38VIxgo8E-sInsg5AfhAl_o5LkPdCvnvaXvl_wyr03sXzm6aJe-tqzpm7gb8nhOh46i2312sBrvbWUbTtFGHRkRXwAsOmRrkhjD7egp7_9vG3v_UWLmd53HilKNO4ry6dG_TzmkxptBiXLl2KxUAGvwhNSd5Rih6bP3PZkgv6wFZckfX1noKVM9wqnXoBcwMx7ZwxJJ5tjkQpN9k4Zcbaw3_Ro2jzww6e6z_CG2QWCI0LP-M8zsw7Tgv7nbKZo05bgHIIjG0OuC3CLEizJd1Nnfr9unMy22zRiJ6ykAcuDUPnDWLN2-78KIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثبت یک رکورد تازه در صنعت پتروشیمی؛ امیرکبیر یک روزه سود سهامداران را پرداخت کرد
🔹
حسام خوشبین‌فر مدیرعامل شرکت پتروشیمی امیرکبیر: واریز سود سهامداران حقیقی، صندوق‌ها و سبدهای سرمایه‌گذاری تنها یک روز پس از برگزاری مجمع عمومی عادی سالانه این شرکت انجام شد.
🔹
در این مرحله، مبلغ ۹۳۲ میلیارد و ۱۰۴ میلیون و ۹۶۶ هزار ریال بابت سود سهامداران حقیقی، ۱۴۰ میلیارد و ۲۷۴ میلیون و ۳۰ هزار ریال بابت سبدهای سرمایه‌گذاری و ۳۷۷ میلیارد و ۵۱۳ میلیون و ۵۸ هزار ریال بابت صندوق‌های سرمایه‌گذاری به حساب شرکت سپرده‌گذاری مرکزی اوراق بهادار و تسویه وجوه واریز شد.
🔹
عضو هیئت‌مدیره شرکت پتروشیمی امیرکبیر مجموع سود پرداخت‌شده در این مرحله را یک هزار و ۴۴۹ میلیارد و ۸۹۲ میلیون و ۵۴ هزار ریال اعلام کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/673862" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673861">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef8bbJRHsobXFIiniQ_ra6BZZ0K4D3TFw9NyNx-xHuhbTvBjx80_x2Z_cl-8fLX90zk9OEW6dxpIE1S8ck8BYAEjREUtj-b2gNee-KyqmUpJa_-aSfpc_fsJ1A_-MF30WJ-PXb80JFFkEoOulK3V6Em1TtAcxTvkVQ-G5GzC9KrASJK-rfg2yIfgFA3hBym1mi1dE6O5Vm5yG5RZCwCifajX0-bV6TsO5SIJpUvCFJbxAF0F2Ytdm2JdXBobxq4rGw2-xWmaBbnRMbjeoYOXV4JtKZg-8cJU3VPRlI0pCXuxGuw35JTwlpLsAByzFDREO32fVcdhVHhhAUI_JLaIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان شانس برنده شدن در لاتاری‌های ایران‌خودرو در سالی که گذشت
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/673861" target="_blank">📅 20:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673860">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5r8wCtACkMqtTm0L7bqkFfEfwRcX_YVXs1WDioSwiPXMUVcABH3w_fK9AiG-VdKSMKKQAUGOLc87tgF1RqsGY1XBb7Q_nG3dODAGi0ar0VK4g2hdgpf6I2WW33zXR7YzoyAgbckpGD6SH6eIFelzBHb7WblXy0IUqa2pZ6xFhVxVm_qq2u52qOvlYj13iqPzKr8LZlPWGqswmIDxEkpIRTMND2U3P1ok8G2eBQUeZNX4dJhryVMCNcjS5V8eL1Hr1kr9yK0Xg3DHwFxyu-BhrCldYk4tY7dDRtRfKyVFc4OPkiF_0baecqkp5RtwjqQxLgcm5oQrLb-b4DrmH3u6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد انتحاری متجاوز توسط پدافند هوایی ارتش
روابط عمومی ارتش:
🔹
ساعت ۱۸:۳۰ امروز یک فروند پهپاد انتحاری دشمن متجاوز با رهگیری و شلیک موفق سامانه‌های نیروی پدافند هوایی ارتش، در آسمان استان آذربایجان شرقی مورد اصابت قرار گرفت و منهدم شد.
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/673860" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673859">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEXYIX38_PmePH68Efr6hIvWDFZMnneHtQBA_KZrX2GFzoHXmfewDtNJOWwktZLPhYas5wXca6HAzIOL0pNtt5NBhXllH96kzedJqoMsi1lfSsSFRfnmrneNR3aR9hZyYP2Z7CfyIYxw_LeTgvzIDxgUokGP0_DBqcSquw__5wc40EXFmRkvEs6nuRkxUsr3RMunspdItXZ0AledgiiNVL7v1sX3bP--Juw6btmdv21cUDq00zpTfo-KjErFW1xe45wA9LHf4sIqFHZ-sLSpWUx0FgM-chcURrLD-eevyEdowwpQwMk5OQ2WszlDxat-a5EnjumTC4TgFL06CKCjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درجه آسیاب قهوه؛ کلید طلایی برای طعمی بی‌نقص و حرفه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/673859" target="_blank">📅 20:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673858">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtExNZl5V0l3Nn7axDtCVF-X_vJvs13AZJ_7JqoycmWBKrbiZBeLdX-TMc6PVQfNrJN54riKL8dcSXel7L3P-HGj_PyjvvE7-ChMuLDvhA1AB9FsY0Y6__wb_vOcq9XePFbmU7TIflBj7sKo8TB4_pIQKaHc44Tl9aFWKMdQFo0eBOB0NezKB22pXql_Ayv4qMDnSps0F2zQvGGjZ-ad4hYOL1YmkMjQqkqqxPCDG4kgsOUtoTivQbUIbSSNP2GxVCG8Jjx22oaAPvqU9dm__Js8B-IBUFnhRsLqYkWP2LkPanyu9tPyeh-mI3pZCFq3kkaEEt7toPL9a-5Ly9b7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار ارزیابی رگولاتوری ارتباطات از مراسم تشییع رهبر شهید؛ تمرکز ایرانسل بر مسئولیت ارتباطی جواب داد
🔹
رگولاتوری ارتباطات با انتشار گزارشی، عملکرد شبکه ارتباطی کشور در مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی را تشریح کرد. بر اساس این گزارش، ایرانسل موفق شده است در محدوده مصلی و مسیرهای تشییع تهران، رکوردهای قابل توجهی را در زمینه سرعت دسترسی کاربران به اینترنت نسل چهارم و پنجم ثبت کند.
👈
جزئیات بیشتر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/673858" target="_blank">📅 20:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673856">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfFwYIv_ifx1KrcfFg82swve19qEjZciMger5EcWchCJ-5ZX_hvA6DhCqr445yI1CcXRguj8y6JbSDP1xzdVu2KezgW7LHOZh1ld2tkDjlbdO6W4FF3758XlfmlFnTr7HIbhYQ1IrxvCkBc-17vSzg58Lr_M4rIci9Jrzew_OcnWJHvfD3JWKCWucxmrE3sd7OPIy85mYYcnVLoSMqyXExgXWsEmmnRhm7qeS7fYnjPh2zqXJ3GCZYDlzUJVAfWhA6ieA4dFT-tPRyw5K0a8ZBLyELTvefJXLtc36bVv9dvc4lWTTEKKBslD8sxjCMOdVmxiPedJErugzVbuJkfaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه با هم برای ایران
🔹
در روزهایی که کشور با حمله تجاوزکارانه آمریکا و فشار بر برخی زیرساخت‌های حیاتی روبه‌روست، مهم‌ترین سرمایه ایران، همدلی و مسئولیت‌پذیری مردم است. امروز بیش از هر زمان دیگری باید مراقب باشیم اختلاف سلیقه‌ها و نگاه‌های سیاسی، ما را از یکدیگر دور نکند، چرا که هیچ آسیبی به اندازه تفرقه، توان یک ملت را کاهش نمی‌دهد. در کنار حفظ انسجام ملی، باید هر فرد به نوبه خود پای کار ایران بیاید حتی با کارهای کمترینی چون مصرف مسئولانه آب، برق، گاز، سوخت و مواد غذایی و کمک به هم‌نوع.هر چراغی که بی‌دلیل خاموش می‌شود، هر قطره آبی که هدر نمی‌رود و هر قرص نانی که حفظ می‌شود، سهمی در پایداری کشور دارد. ایران، خانه مشترک همه ماست؛ خانه‌ای که عبور از روزهای سخت آن، نه با اختلاف و اسراف، بلکه با همدلی، احترام متقابل و احساس مسئولیت جمعی ممکن خواهد بود.
🔹
هشتصدوپانزدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/673856" target="_blank">📅 20:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673855">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLa7peH1IPLngysNp2BMDaCW2xuckMYozwauhQY0vAg7T-RB3JUsOZVO5H8LRA2uWp9ZvCFMqCrWSRxvb2ZoNgetf1vpqY6amFO_B-PTXM9b_9Hcy5IZjZp0Y5FHts08DxgLcDCB-DGZ_MAycMRpHXK7jRRcCWxvbtmfL3nN-G7IO5_Y6HpxAkgQ5lISA29xVIr7a5UTia8fsLcDwRqWWCPrM3Lf1KCAQZC9BFwKucfksVOJYRKR-ojgj-n_Om3h63qd3H04eW77sTz0ZcCecg8mAhve8bfOM_mcqnLv70CGbpfgVSIWHzQpuRcYvhj3kD14RqwhK15lbTZ9F9nhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/673855" target="_blank">📅 20:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673853">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3HIA-H4k5YONRmv4rZKdm8yjWWjv--R8UA8uoflyybA5EmWPnwjmLnuVFv2jV543KMJUWkLKdBGkVnYfcAWIApmDaUvEAzAG1aZR3g1DMPB0-F-QhZjw2w3iglXo0sZH0eLCH07YV6UhYW9DjjtHYCWNatwMDmSJlGxik0nR2YTqUll4k07ttqEuDkDuejJaLY9855XgfV-cMxkA_l2oBrrNX0ABgZ25EWFpicVDXreUko6rTX3WwysrpDKvpYt7Td6M-USQpw400uYEdgKCCe29Esw2O8FCOSTzatiKwPH9QnomGZ7-5_46qyHnQdaYN0HA8yOyb-grHNQEnx_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7tDAhAQDTXIE_FLUAa_XrbcXqn8WvvsKs8HwQ6JN7bbJ6aShLyaxX7hRifLv8DWrDF2DaJ-bF24xRj2Kn6oBPj04PKTyH6ib9DMKF-lQVzQiXBVyRMHC0Aj6PwBbDoT4-YOcWZ24ZlLwZR4O6lt5wmxPrsTO0LDoW_qAvEsC5OyJWMWhMUhIOEgoao_pF3DZQTX2Z9ISDEuGaPRy8ibPGAfdzFgUTalblyF9FnG7rdGRaiXhI7rJ_ncxfg8NgrPIhL69fbQDBDqS3e2U-Bg4-lY1A29D9Cfrm8AJtuOnNwBNy_Mv0w5zk5sXXAWuXym-9bYnReDp8LD7JUf0uHNAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جوونی و با این اوضاع اقتصادی نمی‌دونی چه‌طور باید کسب‌و‌کارت رو راه ببری؟ این کتاب رو بخون!
🔹
اگر فکر می‌کنید برای  موفق شدن به پول، استعداد خارق‌العاده یا شانس نیاز دارید، این کتاب نظرتان را عوض می‌کند. تینا سیلیگ، استاد دانشگاه استنفورد، نشان می‌دهد چگونه با تغییر زاویه دید، هر محدودیتی می‌تواند به یک فرصت بزرگ تبدیل شود. کتابی الهام‌بخش، کاربردی و پر از ایده‌هایی که می‌تواند مسیر زندگی و کسب‌وکارتان را متحول کند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/673853" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
