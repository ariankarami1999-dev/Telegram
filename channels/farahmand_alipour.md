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
<img src="https://cdn4.telesco.pe/file/Gq-uFEDsolrzokdB2bQroxXPh7-wzD18jzdZTrBtO1ysHshGOIm17NZWPYxFonyeQqQQdeVOp5nY4hFGMIgVmyjpC3nXt223D7iUjoaeIyECWzSl93iVKmjXJHdfzBd6I0NUTKLKagPSYNlx7t1NKdty-r6jHMahnXF0ODEP0k2hKhIsDcgUeiClGDmhaRThHpfIm0-RN2D4e_ipvL19xEQqbVWyuGmdCQ1tSCAhmOSdz97fWJZwP4HNOwY5xd1q3zT8_n3bk0-wr-Het95Wc4wviqhx9Ae7uxKb_Ao0m_wArx4-b6zRDAGs0gAKj3U-Sx5JlO0JI4OLXj8B0Z6Qvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 15:17:21</div>
<hr>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=ijAFgYgmj6-YaEcOw2w8HD-hpqnrVQKV9BrDZnqDDSeUEWQDWzgQPMSbwewykz8BOm5a2DURsdbN3qIVoDrphRz4vLmoAe82_eKH2w4sQTqmD8ZJ1LwkPeFKlOuACkdZ9keyEwUiAJLxTnFGPuX5hczJcdVsTVYSIenNuCl6u2Ba68t7Dj0MCu3MiewgQzqq0jD3soWglZI2qMNBcXYzLriADA43kf33TsYapVO_FiNWOo8saDYoU7ucaNnQYgw3s5LMOz6ayoUIKy8jf6CznX8Ik5VimdqosOxJ4bYsBpr-a7KnTCYyXL3qaHKnQ9Qroz0nXLN1YWQCXV2-TYx0Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=ijAFgYgmj6-YaEcOw2w8HD-hpqnrVQKV9BrDZnqDDSeUEWQDWzgQPMSbwewykz8BOm5a2DURsdbN3qIVoDrphRz4vLmoAe82_eKH2w4sQTqmD8ZJ1LwkPeFKlOuACkdZ9keyEwUiAJLxTnFGPuX5hczJcdVsTVYSIenNuCl6u2Ba68t7Dj0MCu3MiewgQzqq0jD3soWglZI2qMNBcXYzLriADA43kf33TsYapVO_FiNWOo8saDYoU7ucaNnQYgw3s5LMOz6ayoUIKy8jf6CznX8Ik5VimdqosOxJ4bYsBpr-a7KnTCYyXL3qaHKnQ9Qroz0nXLN1YWQCXV2-TYx0Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwVUujG8YpvY2xw_u29lAFJHNetDrpywP40Fib80dP9GbxYO2WtUfB2FDcLzVtAUiCevqFGZDxt0RlhsY-bqZ7UooTe7NOiWFE7g0S14c_jJt2agcg7YNOrN6y73D6dzc5PyIEU2D3DTlgAcp-5tiqsStXZWUxHB5R5txK-_0gt76yaBi8E9Q-alkdxU8iQ7dFqVezqCzIaSMDL-cDiisA_whbECQxjSPZGMAYeffP0RkzCdQ6aOiMX0AUT7tmPlgCYOe1yIiJ9oER2cl2fdGrNgMYpxN3rAIgl1i4WcwNF0JKtdBUouk222CNuuwwtL5dXSS06zZX6dim6nuPs_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=qSKi2hqLVJvw3L1RIGNqHWrsvrnKXpnazU-rGVkSsdG3grCdBHWx-2Eom7ot-wbI9gITmnJjr1i2BnykbEzQZmpxD3goSWE1Q29FIVK9EXn_NNj_LL70NMN2e2UM4EFToP0DT47QYOfohHniDvBMm7E3hQ-vdM9RjYulNjZPDbKCjHL2-3X-9Fc87QBYAIR-3I2N4HKlGjNq2Ip1C7nMRpNL_W-k0bgpXJ2owWbeaWK0q9HFkhp8vsHyrt1OLwCAaZCrGYhh1MS9JM9erla22ptnDOja_evBeqiAdgrGAwmbKdP-So56zXbgdUw_N1eXQ2VVTpRssd9YOs_B8gTnpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=qSKi2hqLVJvw3L1RIGNqHWrsvrnKXpnazU-rGVkSsdG3grCdBHWx-2Eom7ot-wbI9gITmnJjr1i2BnykbEzQZmpxD3goSWE1Q29FIVK9EXn_NNj_LL70NMN2e2UM4EFToP0DT47QYOfohHniDvBMm7E3hQ-vdM9RjYulNjZPDbKCjHL2-3X-9Fc87QBYAIR-3I2N4HKlGjNq2Ip1C7nMRpNL_W-k0bgpXJ2owWbeaWK0q9HFkhp8vsHyrt1OLwCAaZCrGYhh1MS9JM9erla22ptnDOja_evBeqiAdgrGAwmbKdP-So56zXbgdUw_N1eXQ2VVTpRssd9YOs_B8gTnpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpdZ4cLYQysJYwE01lpVnQZDmvQFoMK65AVTTO524XZdRvK8Pa7G_wq3Uf-K2HJjHKPKxD5yDpFbb9JRXp8CCpgu3pwY8aEu18k7p6VKJS6FokOYBzA8XlIOlBlUpKDwwsBCxguKjpX0fP8ZpC5z5j_gNkJ1yP_7LASdRik6EytDnriIi5TrspZGn0CpcEcwFGT4BZyrtOmHjjVXWDbkZ8HVKWGuT4QV7EX8A0yYmX4n83m8RYv5EMbyfJQtEuAPozy7KCS24xcqsaQ5Qlg-BOKBk_o82UopbdR6EK611PKMIFLfC86aKKTmr1m4vXGxPPsS_EOURTyJfbhLezqvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNCjjBpEhkuKQuGeP_fMcQSS6tdyT9OjhtgjkXcGEuu1aDo48IdBghwk9svfL2bMu2diCJxNFePBla6ttDsaPPOdLRUoGRNhdHFFXBF0WN-8k-mTOe3IkKvecKj2R6ROGe3-VA-0fyJBu3Pn5jARA8r1nD8Soqa8youQaHcn46ACR3x1rJ9UKG3MzzgbqEyRKD_myyBPH2By1xfcpM17WmOXkVldlUKeg0VTxmW-vsA7xcr1UecC9sBG3NQDUvvAsNwdTDTFcfttIunXpZohhw987k-IsGMBMSGaJN8rcNHNmh85UgLHU6e5uQHjMOYc6BgSsldg8_dBtxxbmxDGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=nshR2fYjzqu5NGegEgHcH3h91epV7qNKwsgUwCkioGyBFlhkc576nskLHqaNSCVgA4moXF3IoXrY7VlTE_lRI6gkLSwUf8DB_IS8wOSRIGQFqNUVarbdMlPR3lMlLdWyk50LjcykIMDKSpaJUu8NNpymooDc3fYk7vD61bk2OT7oyLsLUaklD9sHI2fQ2KYC3WUm10GT6GPzBRI90gd52Jy_2i1iHiJSInRvPm_jgQ_nezTpeEre9PI-lLUyVwTC3BPLTNVU51OJdi5u2xeShEUYnYlxSBY8njCirTveoXklIRYEqRN3gT-V6agVHWg74kJQt-ebKfzLYkrSmVNAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=nshR2fYjzqu5NGegEgHcH3h91epV7qNKwsgUwCkioGyBFlhkc576nskLHqaNSCVgA4moXF3IoXrY7VlTE_lRI6gkLSwUf8DB_IS8wOSRIGQFqNUVarbdMlPR3lMlLdWyk50LjcykIMDKSpaJUu8NNpymooDc3fYk7vD61bk2OT7oyLsLUaklD9sHI2fQ2KYC3WUm10GT6GPzBRI90gd52Jy_2i1iHiJSInRvPm_jgQ_nezTpeEre9PI-lLUyVwTC3BPLTNVU51OJdi5u2xeShEUYnYlxSBY8njCirTveoXklIRYEqRN3gT-V6agVHWg74kJQt-ebKfzLYkrSmVNAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlZFK9wY08LKvp-g_POmKnjp8d6UXtxkpC0alk3PUJh7m4h19CZW33HPde0Ot9QX6LuazYSXHVwniZ-xXEMmv6lQ7JcKB1BYX_eIEMNjQXXDk-vCxATn0DuR4vc30bsS0OnQnr0shOvLgNE-nnZGyHN73XKMzdgMYbd_K2vd5ME9TWpnXEx-TlH2sXAmNabXg64LfGks7l5arHhnHuSpbWtX8Ud7EAnqpOWEv4TykMeXBMz7dUqP-HpFwEkBndQUpBS-8Yk0BotRJJ0yV4l19y12ZrdPcuWNB6odl0aPXzo1ybIhxNa2IyemU5JoSdwDPi-XHbkcAiKhh6DKjJL7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBPCJyzP7mHu3-_F5GDNqsYwXlNvGcQ8uQbnWw6PXY81xWz_VEiFNVuPJogJciD97p00Y-sSqch7JKHTrkMG2jCkQrYFh6s2LWsWjtQCTi3Dza9srThPLDsrtwY3cW6duz0HAodYojpexGU84gRbNdfjz6GFJq6cSG8A1a7cdYBqY_pXQb0819QYuJDd84nL4AQIMDZ_PrGkk8VTGqWZH-1rQAxsJtwHSb9T6wH4xWRmE75Hqez7WLiw1oAVt6Aw9A_KH3KHSJivU4CkfzUtSsacK-rdFy1eUJPa3cdSv_drrJm8vEBKhqo7R-CSkjHlr6oOnRMQe5w0DPdS5M4RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbw9y3kU3RDJ1s-aucELbWRFid-AsSIUpWfr7WeePiYUu5zahz9SsPAGNYOx2oURL4OoznnaWS6w5IyD2tuQ4XFbuxDNmUiTrhR4fWXCm-KoDFBD_JFdn5b1VN1O8ELLvmQj6S4GNoNnI4Eie1kDj5CPdH_yBRxQQTPjcXAl3P4Pqng7X55itMh_lF7_Oaf2KxIHuI5F7sdeHXJxDg-fio48Nc3Je0S2LZcSjrqlNZAXWd-QVInyMpgqyzgTy8u7c1h0LS7NQdgAWvvkfm9S3Zu22S_mAx8ksg5ekTV6bR8S3IuPWtvdEt71_ULcY8n12dmHDLkwA0Da9DcB_Mr6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=e-00LeboGJh0fxHgI2JO3xmmDjARPY0BBwGqtY4iBcF4kWQtSVDbRKNwUIia6ZL4B3Xzk5i8t-Su_L3p30sAaSuhnPygpemdp9zQkqYWsu0Yfg7Vf5jAZRUrzxybKL3lVncAKI-pinc0dM3JxaO60Fu7MKw56l2jTh03lY6oO_ogI6P3pYcyKbpx5jsVHVqCrc7EzWEGcBShb8_s8dJgG20RQCw7_zWoEpux81FPyO6dLCM5R56gQ8sh02d6Id0ZscPl_wchI1UawEIK_qY3nHSLYUmtCU65FdpEXmJEkh5QNVKLqJ_Rzc6pZPxLZiNsrAWh12q69M_MAKlHqIWrhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=e-00LeboGJh0fxHgI2JO3xmmDjARPY0BBwGqtY4iBcF4kWQtSVDbRKNwUIia6ZL4B3Xzk5i8t-Su_L3p30sAaSuhnPygpemdp9zQkqYWsu0Yfg7Vf5jAZRUrzxybKL3lVncAKI-pinc0dM3JxaO60Fu7MKw56l2jTh03lY6oO_ogI6P3pYcyKbpx5jsVHVqCrc7EzWEGcBShb8_s8dJgG20RQCw7_zWoEpux81FPyO6dLCM5R56gQ8sh02d6Id0ZscPl_wchI1UawEIK_qY3nHSLYUmtCU65FdpEXmJEkh5QNVKLqJ_Rzc6pZPxLZiNsrAWh12q69M_MAKlHqIWrhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=XRneI5jpVViD_K5C-t6WbXHa8nv9SrjUswZe3xTLcKKqSiBDPBKmzDM_hW_YVP6dYwQtaWL0AhZSF8XqQJinKZUQw5ECfPlGKEVRT2WZ8eBgouimhfNRC9ASTlMUBI2Vgz20erhFQnckJNsjhlfV_pP8B7y-x9P3-bJNivmwYkL0VKlQRNtEaSLa28rtWl507ZDa5OdO8S1CpIElX8aj9CbKZt7yubDr7L0Q9xrRjbuFMTDHpTfZ7TBp2k7iwYk-xEVIlN41sT-zeeyYqfKZM9_E0EJ2KChz3cy1SDCGggnFNXxESCn7GCTYFDAdFKAVaKtiUoWuMNvDwrBzT4nyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=XRneI5jpVViD_K5C-t6WbXHa8nv9SrjUswZe3xTLcKKqSiBDPBKmzDM_hW_YVP6dYwQtaWL0AhZSF8XqQJinKZUQw5ECfPlGKEVRT2WZ8eBgouimhfNRC9ASTlMUBI2Vgz20erhFQnckJNsjhlfV_pP8B7y-x9P3-bJNivmwYkL0VKlQRNtEaSLa28rtWl507ZDa5OdO8S1CpIElX8aj9CbKZt7yubDr7L0Q9xrRjbuFMTDHpTfZ7TBp2k7iwYk-xEVIlN41sT-zeeyYqfKZM9_E0EJ2KChz3cy1SDCGggnFNXxESCn7GCTYFDAdFKAVaKtiUoWuMNvDwrBzT4nyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEI1XOJGovoV5SgE3B8XuUYzoVoxGnXRx816Vy-1DXLZB_pOvRn0VNZ84-9LEtcODwmZ9mSM7nGOGeKqW9C2FUsu-eodJPgrfjTlZRh12h9Z0AKglUluJMuNI35h5DTcCY70fLm7ZuoDUd9KybMK2oHaQk08TYka1hj9iCZpH6RkiPYOIqkVCxSycmz3xCABJhYZLn65Gbvb63hn3gMyhUS1opbEX_AxYcxudQxXoz1V-iQcpw6AzzSfWDkUkA6NNcy-FPUBWXRasDMAYWilmJQReYovUECTsYyVptPOujery_fLhsnNJVEzgaB_HxkE_HdoVfDYg-Jv5UaGs4Oyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loxgIdBKmVvfN_sU4P8fspyYxTWCYG_ua4eRjIFTqns_n3zBjmXSgoKO-cwG4fa1Jf1oPpD3nKJ0hrhc68J1J3MOEsn_1bYKvOyk6pZeusa59G-bSEEv5hH5KDHpf3XpYHSjPjmoTHuV2LUrTwdfY6W98mWzs9PhdPYdl6kAGjsDFTbtEZHkBhq3_9PqTF3_rr9xW8x0Ok-Lnf16DDXxY2Xh7cGnPa0W57vuOVBuRGcqt7r-vu59EXDWoNaP8PMGV-oGBpniaIFYSvGLrmn8sHtvTmZPncvT5dp0S4vX2VZfzT4JS1PqlJBHjKuNRlE6bcmxayr30eoXp3tqLtig2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-jTL6RzyBtfZTubcwgEeLnsi3PoaMhMZlBM9XRumfxO05L0VsUXZHDcvah3CKGzjO36X6fHzAuuIEWPI-BHJS94W1E2RsgxvEGs8akI9SImtcA_oEJTaKrW28Nv5xYei_y4v6QGerdRu3M0XXKGGyBr2WuGTlJsU-8eRyfOql5PtKGzd4x6zRCMI4zWzU9DgPzgVZorUPyegoDjU6gnCR1DZM2Zteadwon1zCoQuJh8Xt5jsxzJgW8goszjgeMB6lec520OnnN6g_AVwBXmMV9XPzyrQSAGfbsSxyHiscXXskSnp8TnYV35dOiz3yE_JKerlPrmTr-h002II3HH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVLP9vw8EwMAOXLdYc6X_Hyb8Zm15QC7NvgGkYUZoq8WB7dtWM1nPlCfMs89RS2Ts4S6vSUtDkohY8hH5M9vtLzp7JIqDRXoMRtx_wMO09Ed1zspIQy8s0l2C6RsFUU7soeeliNiUvuQSrsCLhjq4oSAR7Wa22ruqiS0xnq6FhFvavCL2QUAWnoLiO3fLaaomOBN78ohVTWOcy1eC9DKG-kfI7ixSE5T-g2iDwOD7IPxQpca0vcSg28dsagVzs2-a7wNmHy41U3hrUL_RE9KII0BcOl3ulWZolzDNcShL-w0WsiOfhFXSBwC8uwzhk6XrzwfQLkCaVn0cC6gDRpeYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bl7zoALXuYXCAUc_B8fHkaZ51JMU0Cd7Oc329ssvNZ5Iy0ZUXPzwQqw0xcvUfoEWe_DbvJ0q4lq8ZjkPVnAxY-B_M9NwYakbuMFwx2KwIVufRd7oXBbgOOu-NZ35hsy62YraipcUXlWBf1s9s0LYeETJnx-EODX7oC_yra7b4hB-GEZ1JydL8TGVqE8se1QT_zU4EKy7d9HHrtqPtdwv0MiBdeT6zky5NPZzn03_JgexD4zc9cpaARc1e3sT0jWUcrguyg1ZvhPeaJOAJ6uCjwyTSqBsYOAGKeM6Qw0sCTK6kyeljl5ajQ6aTT7xg9g5JpvuSpu1yW8i0BcPTIm3QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSR09OYdJvzIvPnmj95nwloIHX2KguB7ifmIrt0p1z0Np-fe6UxCcZeDT9Vnki7xCQuQKDKg0wUYpxfRl6iTLBDsePB039ufLsD6oxuCDrOePjnsqUP2BXhWpK-UoX4VkTvjZqy6U80Dirmwb60NfTHM8Bwy6bLvzcGUszYWQp4nN01x07TbqTSTTGagimWsKorZJv88m7Sj_tpfoiYwh6pq8R-QBPmVWygSwbHb3T7DYiqNk-X9UrMMsK3C60kTa4hBWxTszwZa2OTDW7cHLqkHcjVkFtkYvzWJXboCfXFpgyyCZP8v_l_e02LXIgRBO1TwRfDuWRD2cqm8xdVDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipyZSLlTqi9GcNZYvh4t1s48qMKpwE4LQZJi3CCV1FmYOeFFdNCNHxyPZDR8E4Hfi0iBilGTSwrPFEzEGAEg0Tk94t27JrEjHZpJRYxQWz4-PXtDLRPTiSVL62MSXek1oaMNnI8y-7fePSiQMhCZTpbsuJRDF9hXSJ00QViVmoTPyZMyzqi5a0fIVSrPbVzNLc5q87p7jfmuCK7Tt5XsJ99Bgl34Ouj8zdqUY4IW8GQd-FKXSSH0Mc8qcaje6k7sFQMP6IxpRABHAS6peMi-fZR1atbb3C0mTr4KfwCTo8irnaZCLRGfZNO5yA3-cgCuI9O-mriudWojiCVGapKKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=fHnN1OuvRsySyc37jqFomipMZcQ9gVPZAlGdvdII0Ax3j2e0RPiFtON0aFueHzVrnvGlyUqOh5W41B7PJL_8ZfdyOJ6GrILEmUXhbRF2bIGnPilAdb1g9ZUW69uDyydF5cRHyPePxMAgh5HEL4UPp5UMHsVGdroKiGynKA8zA8ThVzFlNaqlOKmw-OF22iCHep66kwNIEMT-mvWBOWv6u4bCm0WAnRT6RJ9bFbNk4ABQf5eCN1OsoiKmxpsjgR_MT2m4BUa7lDk5KfnciLfeqcAHPjyysyVfTSoeZ5s4Vln0Reu_8PkqvKyHJsYOgL0El4aUNSO3sZobKaps3qdQ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=fHnN1OuvRsySyc37jqFomipMZcQ9gVPZAlGdvdII0Ax3j2e0RPiFtON0aFueHzVrnvGlyUqOh5W41B7PJL_8ZfdyOJ6GrILEmUXhbRF2bIGnPilAdb1g9ZUW69uDyydF5cRHyPePxMAgh5HEL4UPp5UMHsVGdroKiGynKA8zA8ThVzFlNaqlOKmw-OF22iCHep66kwNIEMT-mvWBOWv6u4bCm0WAnRT6RJ9bFbNk4ABQf5eCN1OsoiKmxpsjgR_MT2m4BUa7lDk5KfnciLfeqcAHPjyysyVfTSoeZ5s4Vln0Reu_8PkqvKyHJsYOgL0El4aUNSO3sZobKaps3qdQ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=B1Afc45cznePr8YYD2wb8ksOUk01vRuS3n18KUxWbN1weG561Bmh-BJ-yk4LvmhafGW0JxUauW8m9mDkpUIibuQ_bZ5_2KPQrL7LXqfY2wMxb8Vlk9PntNtozrjj1bPjw7gM0kbCPdqVHh_H7492YNvh3HaYP34ZQi_IF87u11mDKRLfTQXfjn6MAkj4B-kntfBjMJ6WPRbAx07MXDELjW6hXXH8LOlN5WD-7HRgJjgZiExLgXOsbiL_wipCyNiGwblJm2m8bYEsideAp6L8WZC8VFooghchrUyFDJAi54OvhUaZ0YulnGAaoar6GK7HdbCD2NYyjyuT1y85w8nPHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=B1Afc45cznePr8YYD2wb8ksOUk01vRuS3n18KUxWbN1weG561Bmh-BJ-yk4LvmhafGW0JxUauW8m9mDkpUIibuQ_bZ5_2KPQrL7LXqfY2wMxb8Vlk9PntNtozrjj1bPjw7gM0kbCPdqVHh_H7492YNvh3HaYP34ZQi_IF87u11mDKRLfTQXfjn6MAkj4B-kntfBjMJ6WPRbAx07MXDELjW6hXXH8LOlN5WD-7HRgJjgZiExLgXOsbiL_wipCyNiGwblJm2m8bYEsideAp6L8WZC8VFooghchrUyFDJAi54OvhUaZ0YulnGAaoar6GK7HdbCD2NYyjyuT1y85w8nPHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=T12PBI-Q003ZVMpmaHlqPIV5K9XVVpQV7yGKX-M93_VmWQIrfWjqaJhNBbFeThsfTmcp6fddmpfAgP0P3oUW8uGD-CgA9TOZTSWskomqjwowVfgKYjbS51CrpZ2Y8yx3IFOhM5nR1-d_1CpGQzA-h6NCr99lB11zvX-7mlFjiiOoXpIbPS30M3ML5UqT_ojN59RdKnOrkJxyWi5BQ3TFyRQjkAaoc_0JSp_0ZJwJO9fnT_8Hc_h5vL0Y_M2LrqaM7xfdGrJXtQkOo99vxeaRnFI-8my7DixMYGdmlfQwEZ4xbc7wZMEnP8qtcTOM0vqggodNkYvGBtD9dtM-6wb2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=T12PBI-Q003ZVMpmaHlqPIV5K9XVVpQV7yGKX-M93_VmWQIrfWjqaJhNBbFeThsfTmcp6fddmpfAgP0P3oUW8uGD-CgA9TOZTSWskomqjwowVfgKYjbS51CrpZ2Y8yx3IFOhM5nR1-d_1CpGQzA-h6NCr99lB11zvX-7mlFjiiOoXpIbPS30M3ML5UqT_ojN59RdKnOrkJxyWi5BQ3TFyRQjkAaoc_0JSp_0ZJwJO9fnT_8Hc_h5vL0Y_M2LrqaM7xfdGrJXtQkOo99vxeaRnFI-8my7DixMYGdmlfQwEZ4xbc7wZMEnP8qtcTOM0vqggodNkYvGBtD9dtM-6wb2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=jZya_ILYTQAEUchVy8Mbv-1H50q8MHZ1s_Z9w0Dn0tgWRyWZxttMX9-QDZFf_JvtymihjJA6XUR0KaEdFjptoqu7TeC55PoFTam7nn38SXFyajSL93TT2v9tJ90CF93WgFzmLDdfURPY9lO7jBatr-p5bIR49qMqlV9ZThjRFgPnkx19wkqxYRW9gSmn3y6_Rghbc92ZoUFC4q_Dfr-Nxudu20gPUBbunAarEAB64CjUAs8lHUdYbro7u4uNCj-JZW0IKlO3fLRlP9B8UMGPqCvNVPhL8M3FcCwpC0h1vn2yiyMuukpfIdM8hdXNZHBub5gm4ddg8MP2icYKB2dHcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=jZya_ILYTQAEUchVy8Mbv-1H50q8MHZ1s_Z9w0Dn0tgWRyWZxttMX9-QDZFf_JvtymihjJA6XUR0KaEdFjptoqu7TeC55PoFTam7nn38SXFyajSL93TT2v9tJ90CF93WgFzmLDdfURPY9lO7jBatr-p5bIR49qMqlV9ZThjRFgPnkx19wkqxYRW9gSmn3y6_Rghbc92ZoUFC4q_Dfr-Nxudu20gPUBbunAarEAB64CjUAs8lHUdYbro7u4uNCj-JZW0IKlO3fLRlP9B8UMGPqCvNVPhL8M3FcCwpC0h1vn2yiyMuukpfIdM8hdXNZHBub5gm4ddg8MP2icYKB2dHcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=D-dwz2CblanWYtgKBn9eqR05LjIaSx0DddXAk_rqs3MYIuNJ5RHSxOd39MSuWfYKoJNjD_NwaUFkbrr0wxBepZRH6yAZfRR7DsMCGz4QMDGdbtA8VatA2aTjoMRoKTipAf0qVtYblX7RVDvy4x2ssAeN5NWM_aF2lSymUKrxFQ6aFsRYV3ikJgyg0CTvYF4YLYNG9ZNqkJHKO51Cq5VHX4yufmpp6EXAxLv_J6kIJ-_OsJDGG8oYe9onsZow1DrjXUd-arapbI7zSijkEfrS5t1qwlICMNq6ukdpKjA3hSK7Y1UC9tN1shdjnTBgqgxv2I4P3TcLXBEZqSDfqvl-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=D-dwz2CblanWYtgKBn9eqR05LjIaSx0DddXAk_rqs3MYIuNJ5RHSxOd39MSuWfYKoJNjD_NwaUFkbrr0wxBepZRH6yAZfRR7DsMCGz4QMDGdbtA8VatA2aTjoMRoKTipAf0qVtYblX7RVDvy4x2ssAeN5NWM_aF2lSymUKrxFQ6aFsRYV3ikJgyg0CTvYF4YLYNG9ZNqkJHKO51Cq5VHX4yufmpp6EXAxLv_J6kIJ-_OsJDGG8oYe9onsZow1DrjXUd-arapbI7zSijkEfrS5t1qwlICMNq6ukdpKjA3hSK7Y1UC9tN1shdjnTBgqgxv2I4P3TcLXBEZqSDfqvl-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=fw5bcDwAC2nZi65mIvWhlcXdSRp8vd-InXctc9OPe9l2aJNzRkxStQd4mtGco_UrzgP70NeC08ZT2Mqq6o-zQYVCsEbEEhjkwTqEuwZRDkFXGemKbpjoF_R8oNnBY6euvrTShAMh6IleFo_fCunV4Gu2pBJZlKCFsWhU11MOKa7NgySJanl_hNWBGIRngOR6M7T3En4R09acH2t0KHB2xUbM9EdJmFCfaH_idOWeWnCg1BPwBl4dFsZwyCSu4vWo5Qh-4JQ6K1zUAqV4RmceMNqR8WimCBYP3NyeOo6TRY_y4S2oCvVXLnDCtwDgIKFsLCxhZH5WhiCCOEnXKamSlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=fw5bcDwAC2nZi65mIvWhlcXdSRp8vd-InXctc9OPe9l2aJNzRkxStQd4mtGco_UrzgP70NeC08ZT2Mqq6o-zQYVCsEbEEhjkwTqEuwZRDkFXGemKbpjoF_R8oNnBY6euvrTShAMh6IleFo_fCunV4Gu2pBJZlKCFsWhU11MOKa7NgySJanl_hNWBGIRngOR6M7T3En4R09acH2t0KHB2xUbM9EdJmFCfaH_idOWeWnCg1BPwBl4dFsZwyCSu4vWo5Qh-4JQ6K1zUAqV4RmceMNqR8WimCBYP3NyeOo6TRY_y4S2oCvVXLnDCtwDgIKFsLCxhZH5WhiCCOEnXKamSlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=LhA9eXKNeI-Llvb0CJv8Xzir3gQqknrJdbhV6tGWTmWhwThcxLJEqnw6bq_ZW8sV22P27vLrzPurt2Q4uKylhdFKZxOisBlSboPW9ZyiaFJOqdKMq0HibTLq8zK8ogzQkxL9Rv48CR5ELN_kR02R-EcyqFbo0HbJ0u8nhKWhD35QS6f51nJh6my42S5MlxPwuxrGzAJFpoudXdkQAarCIodB1JvK-cZmMrbeqjtkXrsl_D9qLRZxOF_ChhOgGjn4O88rE23JDvFeJ-5blCybRauOOvk_R54Ts2Su3vkzbTa-mMl0J6P5ZjBHpE0JPuvBGkIID7cuWd_HgzlVjDS6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=LhA9eXKNeI-Llvb0CJv8Xzir3gQqknrJdbhV6tGWTmWhwThcxLJEqnw6bq_ZW8sV22P27vLrzPurt2Q4uKylhdFKZxOisBlSboPW9ZyiaFJOqdKMq0HibTLq8zK8ogzQkxL9Rv48CR5ELN_kR02R-EcyqFbo0HbJ0u8nhKWhD35QS6f51nJh6my42S5MlxPwuxrGzAJFpoudXdkQAarCIodB1JvK-cZmMrbeqjtkXrsl_D9qLRZxOF_ChhOgGjn4O88rE23JDvFeJ-5blCybRauOOvk_R54Ts2Su3vkzbTa-mMl0J6P5ZjBHpE0JPuvBGkIID7cuWd_HgzlVjDS6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfWvQNp-meloivZQn-Zj20F5UWjMVq1YQB43chrGon9XWtvGBiGaqmmBUzMBKc2LDjEJHCVNb4LXmYSD7CaRYpaHchBky594xiwswp7YYmCBHs7KKH0IZEjytEOGpjcYdgPX3UoCN-5P19mm_gBiWFwCcAGYlE_L7BP8PNMKEVQwSVikiLesk6Rvt4687ckr65hIVRl77NvwH8hGP1YuflfGZwqa435Vi8ziyZYQIsoutkwd21nblBuxJjxN7qK2D1G7WNXFUofMH9TR_MXziEJaiBRVQZFM5biAIAb9mixogAVxydSSfLlvy9o2GnOa2AmewBxPwbUyueZJLLaPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=RrBZw2puf5JZ_ImhtLF8MF4yvFCZY95Pf_DYdgF-YeXZaBD7kmP8wbGe-wbfvb-okMcCqS1htt0KKQMbwEBXm62gcXmuSq2fsLfS1FRISGww0oe9IjmeITS3QPXvLl256QRPN0q5ASFi8ZiMWa7PqygghS9gQwZDe6R6OJWZUVvJivzcGBJSF2jXsAlPS_qDQaV2J7j-4PhSNolQya5a21eqsmGN9t1Tfp1hMa7pcoeSKzPLiIgQVW1b2t_jcx6GhRsMgKtUkV4Qn3F0aC26glOoOJDtbjFH2b0GdwcwuTyAMJ2edOTzKYXnwPJJzQn-Bskw8SXafdJjtdXeU1RCBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=RrBZw2puf5JZ_ImhtLF8MF4yvFCZY95Pf_DYdgF-YeXZaBD7kmP8wbGe-wbfvb-okMcCqS1htt0KKQMbwEBXm62gcXmuSq2fsLfS1FRISGww0oe9IjmeITS3QPXvLl256QRPN0q5ASFi8ZiMWa7PqygghS9gQwZDe6R6OJWZUVvJivzcGBJSF2jXsAlPS_qDQaV2J7j-4PhSNolQya5a21eqsmGN9t1Tfp1hMa7pcoeSKzPLiIgQVW1b2t_jcx6GhRsMgKtUkV4Qn3F0aC26glOoOJDtbjFH2b0GdwcwuTyAMJ2edOTzKYXnwPJJzQn-Bskw8SXafdJjtdXeU1RCBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM6KVpTGzg2ZXVvh3Ld0BxiivLHJP94NmELp1c0_WG4NVI0576JOKURJucjP1eYbfgyp69Jw8T1llH0Oqsq5FmIp9kUbAaJTtvO_nbylKJXiymMN74cp_tZsP2bkMZMjtXTkqfKQ5gWgVZgP24Ly_WZJEuNyBtaUiKHNypquiPSShbsEgk4gDpcp9ZEnsgMw9ee2NxxwvX6DRJ1Ldc-2W4Zfp6J2eq7kFi9iP1aBxR45nPQA9x1QAT4RHaSQz-Y5HKG0zTta7G2rrKNQUpyrIPjUovU86Jcdj_v-MbeRqlS1fCa56Y22K9oOTStR-WDq-BDciEjDvufr0YtFImxw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEZ52LOlG9jALDVZ4Y3HLryft_74wzDNeXRuILxBfDfGCYFN7lWLD07u4EvvMXFbLsmugEQq1Z6z878crh8z9kx5eNzVGxoH_3cbDHAnVtnJi1wEeTxg3NeOYkUZT_fZqY0QMfPtGQ7l50_vjYMZoDvDa9BAHeX7uyh-Uy_geuSEp08jqC_67EaPo6oe82m0EBjwjjyO5_zZ0Lo5IrY31wk-_RPEKdMhlAwvvdxEjeMzsQcLUoZW-fwbzmmE6Y_dAFIBbMPCRhqH1Z2bdVu03Mg-EcwqVlx2AEu-RMIaigoABRtNJZn0nWOle5lhGDb35paguN0pgDFpeTgqQfr0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0fFHPHrgSfZ5wSXOLdfWavS7CVWOcOH6oddQUlvkD9l0EkQ_7h3PdXdevn7BT13yD8kWhm7Y9a-Nr-UBZhQLl1l69W_c9wp_TZXKj9_x30gmHjsDOIbLqidUIBEpifR6HS39u46PqzCbYJNtBQLFRhbhm06P8lSqTPQgIMFQbT8FNZXcdvbo_nNiAXvJXR11uFK6GRVHFM-6KcN5o2Xc5TwHtAqn8K4x8SzPHLDZ7bpySGJCG3x_6U8B4gora_1ZY4WmbW4HEoiWpf1yKnOw-K17Wq-jK5SHVdxm4jq5UvTH8TtP4uXeSu9DuJoPtBGX5ILS9v1nDR9ay5HpYcJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H66NBePLROv3szVBSUBJJhVuOS0Anu9rol5gINFd--cpRpduczADTWxWpSbvnEBnAUDVFa4eBlOymMp-NSUfUYDJvF-7yrbl7kBVVvU2S2VQaVYiLFk4zOOzEtYovnMS-Fe0IXS3_966peKi7I1-Da7JED3LQHOnEQdKBIj4z-Nzj0K0NsYY4UEHZ_UCfpdAAFk7iUEQlY8Q7NtoE54DbXHNjZ3JqlimQ6L-fCdLRJH1KJlv3_bD28CsK5fIpetas2qYhrXmoG7zEQijNAI8d8tC4nej8iudINktn4i3sqKCm4WCP_-M_Xw0pjqq-8-IB9sLS5MxmNJC05t1KYGtxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=K6easOr4u2Mv-j72gsEzGyvwXVNHQ6ti9EUZI7RJ51PGW1kn8WJiWyuPqNnNsuoq3fV8sfRsTxOmGHPf-4jznFF4hhiQUtkcFOXDz5KSywPyvM0K1d99VwX6FT7FdhQWEslIspgvo5Vs6T2jXaosGfbT-5TixgaeFmb4V7R643LFhrE8MW5psiatCnZCWqFTsHECrrq8E0hEhr49nINr1MloETdI0_ZWVVL33kk5p-_pbnd7Is4Yu576DqFFPzoxDYJxw0s-dsNA70JDZDbDVR9pYESD7fU4mKar21xquPrs487rtwxdK-LMWzk4wGxV-0EZ8EYOzssuersSoa613w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=K6easOr4u2Mv-j72gsEzGyvwXVNHQ6ti9EUZI7RJ51PGW1kn8WJiWyuPqNnNsuoq3fV8sfRsTxOmGHPf-4jznFF4hhiQUtkcFOXDz5KSywPyvM0K1d99VwX6FT7FdhQWEslIspgvo5Vs6T2jXaosGfbT-5TixgaeFmb4V7R643LFhrE8MW5psiatCnZCWqFTsHECrrq8E0hEhr49nINr1MloETdI0_ZWVVL33kk5p-_pbnd7Is4Yu576DqFFPzoxDYJxw0s-dsNA70JDZDbDVR9pYESD7fU4mKar21xquPrs487rtwxdK-LMWzk4wGxV-0EZ8EYOzssuersSoa613w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wm2ej2iiPYCauRAR-Y39iK9HhOq-lYrgQf74a5iwTZVF-9k2Pj8vMrFa9Uc36rjCjXiZROX6q1VuFJUm8mN-UnAGs4Q_1K6bDTFzHArurnQS1bEywAHfb5u7fErIunWintNoCwsKqrhW7vJR261Mh1BUuWCFvrIEqyZnbRY_QjIuT4JlxyYWrpWt6UMrOrOem6_9alndF9XPSqNQ5rEaRHLOcNH6g5LvzMWok7bUKzdGVbuiIAzN-jyyEWNyr63UK2iAhxqOYoNK02EOU_rQAfF-5uKKTyYbedYUMMXcCW8FYlwQ49nYen2SgIlsRGT7XR7kETswnvBzwMaeih20UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Wo59bRWSkH7T6RsJFKH3_Ypop4ZbF5D2t6AmXWlyveMhoyl1HteGZIFTXxR1gEcLZZ1eTuP7Efaym77XmitH2oeFwO75_YibL_q2_9Jb3bh7vIYNIjG3Ch36ETDCF4a4NmydZ8CDcU4FaCZfTWnxLLsZWDTakcV9RhKXJ7HFeeAeMkbXWie4JCmxXryqVVnzWCBITVlykvd6yD9bS-ouMCCcR5_gn9lus1UWTz9yZ-jKqJGvjlDBQau97aIS8dNQWFyS3Sx9U2zUH15cfj26aVdCVkkH8ZuYtNRuhSCDHSsiP4X-o6wjf8H6dS8cMCkrS1FwPuRF8y8rRnS-mB-C0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Wo59bRWSkH7T6RsJFKH3_Ypop4ZbF5D2t6AmXWlyveMhoyl1HteGZIFTXxR1gEcLZZ1eTuP7Efaym77XmitH2oeFwO75_YibL_q2_9Jb3bh7vIYNIjG3Ch36ETDCF4a4NmydZ8CDcU4FaCZfTWnxLLsZWDTakcV9RhKXJ7HFeeAeMkbXWie4JCmxXryqVVnzWCBITVlykvd6yD9bS-ouMCCcR5_gn9lus1UWTz9yZ-jKqJGvjlDBQau97aIS8dNQWFyS3Sx9U2zUH15cfj26aVdCVkkH8ZuYtNRuhSCDHSsiP4X-o6wjf8H6dS8cMCkrS1FwPuRF8y8rRnS-mB-C0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=k9XFiU-e7JH3FKcVPkp3psU2Ps7_e0AD_RDS2BsEpADjNpI1D1tBnbaz59mqXCIret7smlRDvopMWQEG6d2EXz_Xs4YVIqUC_R85HaRinO25mYd24MKI4Td3RsFZ9DLm150HMZNCgoC1xJLeiAT3cwrjSdJqw8Y_lflf0baL_mgNxXO6eALVtMeirCT13EbzM8sf_Z-yo9MR0YfM0OwI1jtbQOfZEF8wvF3dINebjgyipcDVJ3ltvboLhoSFUOBVZ1WDNM4nXw1pB5dOWronlNVtP6IhLg_RrBIHSWxnpthPXJK_IfdvBoQ5KH_t0Knr1Ek7LGKQGsb0Hi6khJPDiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=k9XFiU-e7JH3FKcVPkp3psU2Ps7_e0AD_RDS2BsEpADjNpI1D1tBnbaz59mqXCIret7smlRDvopMWQEG6d2EXz_Xs4YVIqUC_R85HaRinO25mYd24MKI4Td3RsFZ9DLm150HMZNCgoC1xJLeiAT3cwrjSdJqw8Y_lflf0baL_mgNxXO6eALVtMeirCT13EbzM8sf_Z-yo9MR0YfM0OwI1jtbQOfZEF8wvF3dINebjgyipcDVJ3ltvboLhoSFUOBVZ1WDNM4nXw1pB5dOWronlNVtP6IhLg_RrBIHSWxnpthPXJK_IfdvBoQ5KH_t0Knr1Ek7LGKQGsb0Hi6khJPDiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki07y0bsr1cyKJD5LkHRz_R9IdzKhP-2vgrIqJDnDouF77joEP5DCiOJ8kujp5VnifsCFS0slnaRhhAcRUVk1ddbAM3hu_5yKN4jwhClLeMI7AmuhvBxJOCFeSSVh0eCxV_IE3tr7v1J4qrp2_TYGcEjGOENdxx1qCxu3RJZndgQn_-VTf_jvpvDmepU0wlsYSHsC4lZHYlXQlgkusWVf43Y-02HoUmfepC6VU8vbvk_mW5KIZZk5KBEFxtElBEG6Wva3vDEUjSHPZ8C3ZO1fUTQuj1yRqmDk_yrLPigopGPO0CbX2OTJ84oT0jABpEDlFxfPwiH-ue1SIfaCPnk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWiCf4Q8vsRU4u7HYcSO3Ko7kZvr0qgRdAePe9EUUztk7n9eQ-HnZB97vuS9X0gDO5SZpwjDSIbPp6ooHHoc7HutET_Vm0pGvznD9SaY2oPYSB3_M_Qh8aERc6fK1VTpM8IaxXBDg5VTIHZo9XfDfa_s0yDwkhVVMJotnqD0UKE-c-f4tot24w_lE89hzL37ygOQYXNPhsK_AcYy39x7EHOrciLXL3RbCnD6PLHPe-D80QJO3dm6MkJEelroO64VPuJiRnOHnicM_zCXSuE6DxfcI99ML-8pxfh7TKLzeQJ-e1U_KGNFrVRlOk6aT5d-GybCLmMEbuAJErbLwogKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJKCOqjcJNbm3m-J6Z4ff7YgA4C8FbYr0zuAi-cer1AR8SL4hfDu3iwszfKBCsGKVpNDeKxvUCU9RqrrP4-VcA-up_RCNqwOblAqgVIWAxb2S-tJjlK7GEyiJfS_aBlFy5qTxxYc5AVA3KR3UZHY0pJtyhBC7C-fgYMMlR-5alak-Th8q74w2FGjtsoGGaPTVEED_QkbXccqBXAKZ1OOojDM1znTDV1fZBpXR4Xe2m6wnvkm_n_aVCizCCf79lY7QDx1aMKXqKAJ-kbzbcINASr0g6_PBJNucU_17QPuAr6MlVDI2IkZ5Ldvzl8EV0wgRkzpFieuxxpmnDA7jf8T8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=KmKl_jr077m8hEkUoGfHzXsWNMHEXLl1fwZNbFoSqqy2wX5NIUDvuS2-Ip6-12vu5lq7sbmzdLFVWUkl8XcPSKGW8t2-fOs0HlfF3QXbVdAHhhSSVFpploKDZhm4Vz92y_b9EgAs96tW4cX94hRuVTUTgCY6r1Miytcgl0Jit9PbNR0nv5rq3rQj8RJjSr4iSolociu7ygAWw1t1FTsdLw0FQojE_3Xudr13cOH2-QTYYjlkjO-LZJRUn1qu2vxU7gpB7Qs_6mxr0OKRYv3gh-nifquTWBs_0Skqi3XoF2w_tMVKw_6WQsHrfM7nBrZZSqqYo-m2KXOxD5ZM7E9lMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=KmKl_jr077m8hEkUoGfHzXsWNMHEXLl1fwZNbFoSqqy2wX5NIUDvuS2-Ip6-12vu5lq7sbmzdLFVWUkl8XcPSKGW8t2-fOs0HlfF3QXbVdAHhhSSVFpploKDZhm4Vz92y_b9EgAs96tW4cX94hRuVTUTgCY6r1Miytcgl0Jit9PbNR0nv5rq3rQj8RJjSr4iSolociu7ygAWw1t1FTsdLw0FQojE_3Xudr13cOH2-QTYYjlkjO-LZJRUn1qu2vxU7gpB7Qs_6mxr0OKRYv3gh-nifquTWBs_0Skqi3XoF2w_tMVKw_6WQsHrfM7nBrZZSqqYo-m2KXOxD5ZM7E9lMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=LWmW4IzXluK-OdPvmQRpiTMn7pXk1z5UEQHur4gxtZT6cONPe84ooDBtffp1dcGuU03F0_-08hi3ZHDkbwnEiLnuUkRMo0LSNGNDWRTH6KoiTdxeMSdVPBpvw51YrZrhlseNIKb4w1JMqu2LlgJAlU3t21etWqT8fJG2iTC1iHj5ejofWdy5VORGwJ1AR4Z3WcIPIFZDbNIVQegdqsyhZcmbRZ6JGLV3QVKlWfLKrZPS1HekgiP-QjcN4lo7OvV_4mptdg1BkdbxJLiWlLOf5sWNAXZP6ao8u15qykBJs6pFedaHaVeiokbrH2i-HbDQqXq-0TGQt7uWzo55bI6TwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=LWmW4IzXluK-OdPvmQRpiTMn7pXk1z5UEQHur4gxtZT6cONPe84ooDBtffp1dcGuU03F0_-08hi3ZHDkbwnEiLnuUkRMo0LSNGNDWRTH6KoiTdxeMSdVPBpvw51YrZrhlseNIKb4w1JMqu2LlgJAlU3t21etWqT8fJG2iTC1iHj5ejofWdy5VORGwJ1AR4Z3WcIPIFZDbNIVQegdqsyhZcmbRZ6JGLV3QVKlWfLKrZPS1HekgiP-QjcN4lo7OvV_4mptdg1BkdbxJLiWlLOf5sWNAXZP6ao8u15qykBJs6pFedaHaVeiokbrH2i-HbDQqXq-0TGQt7uWzo55bI6TwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2yrrp_XJSci6lhzdggfbEKnxfLZH2t3O-7yvW2Tjg-czkwgJ5-4-gmdcnkHY6ppqMdhFlMF4lh29NO-TbjAVJq5QxxLNmOutPX5bdt5C5Ot3DVk3wtnRtJHdFxH0Aji184UAa0Mr2vW-X3Xmx3AAPcx8jI3mr-LtqpzLDO8y2-KWBYmsvaEQjqJdvpk33Wa-6PvyDMUTPKCVWzvY2kPn7medtQGAQSeaTJHkQCKU11H7vLr08QWFEztup6e9CODo_7FU_hfDLM4scuWAjYWAfe6_by6Xhl0JEBK0Vh8_RGdp2uofET_JOKFA-ABkc4jDoEIFyl8CrgHj2E-biMFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b59LvMUobveQDQen33S00lhL7eEwi63o-v82KgcnQhEkc33tdrkSKRNRvA0hvceyOkuifWde8YuxYOoKcqEAiV4U9bD8WTmQ5U3EqozBN0hq-TET9F11qwTHScMZtDxlmAsC1Ghaof9u_OAvJSeCMaLJ6DgIs5UouPCkhWol_LTlgAy83JgA6LoJf3kJEjR5PCEZSThdMazGfaotYX_RNjgSRYl3hFvN2QhzhF4-1Br4Qps_nHnVtxgimUOZAEvYwtokvvH71nS1v2vCp8Args_yeGn93M-FTJ9XXIFJfeJklBev6lh_Reo4CVxZSrRC0rCULB0GzranU7oRg_iY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV4oJg31AT3JVa0mzS2yo2-djSR66WB6mWajYymr2ElHppQIKkrE_qxzneCbQ4vmUQ5syE7DiJcISlJmNoyCoMwIn-UmVl6sNXL-4O_q1nm_s1G1pqKbC-XwEPUx_lTWl6fabZ91Pqh_HKJue95Qfji7XvS2_juvoYV4f6XLN-gBECEwqPqPbFHqRCck0r6xGSIkmWJr0IKO3--d3fiGkKXbJblxR4UewN6HUBdEL6662qvV1ctXyRnYgYdu7jJFzq1d6E5HONqSXyKu14Fv7e73zLpF-Quhq-2Xhv3safFl3RM7rqTkv6z-wcDx8fjTc2UA_YJujN70CgC74SR4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNyQBPXhYnSI3SD221wkFIQrtqUVJ5etn75wxptAQRMbdyP20mOxsqDc54GM0mG0Nod7-esvQ_MnFNMrixRmZrVXZaGd7-NwydZ81A5z4pDUbD59BPxy0buOB6XUX5iKKjyqc9HoQhGyMqVlGvPWsQ2w8mmM0bomr7YiNK-hPDkOJguWWqkO0GMciv5iKtquQWCS7K3q8JyWvkacCkXXSvRhCva7NzCDngc4nNwXCUq2J3fiQxmAqT4Ig1ljGyXvw7323HPtNYIs1aLu08W6duihZmn5mxhFAr6gMrSj-3B4lkv6OhTMBGRuFUmKMvc0kgd9pIsdnxOkTI8UnNntwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQQCy76YhXrvXxjxNKPZINqwYdMIkwwEm3jLyNjmfbIGwOH3nMWNGMIvev8ayNUU8W6-btb-dYl9bda355EpkVR7tQYV7Ot2I5v9a3UNECPieEtSZNIZA69Ysmq4bMOr05XjuXpiiQHDy_aN0uNZC7L-yrR3v_ZV9UU-BB84JZRMvAZ1OGH5_25_Z8iaek4Xd5qUvEjtn3BweLcAURb0W7_Hptmt0V3a8tfJYkujAz-rqybkHHSxptryqqndAfaVchLnuDgRwk61JQsQOccLfpRrvAAhkuTu_OMj7o6gJT2y6ErWgh5s7lS3rb6DOrDWqqosaY5xcs0DXcWio-IJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6saTOVodYFWUk4GVt_bUCy_z3ZTSyBigA1WPcMjJZ5MgwF_o1yFlXP8dT6XnqF6jHX1PYUceB8WesqJCJ1nnHBadb8SrFZ62Ghlos6AojGu5PecMAztY2uXdeztamljbqqWdiRQfdAxGEJShLG4g9xzxhJCO0XNTuocnUL3K34oUV-2oWN4qmuA0nlRwyeY-6vR7MD6dpbX2o3Rqlqvrzoc_M4s8d2ziNnu90rE1JWVCx7fj7IVTlp2MyMuJ5YUNn4Y-kBPkf7eEpsngWpQSVBtiTEmOXzFJxW4x9VBau4N879pZcg2EQmJjRp05AoU5ZdSuiKB9jP5FzFK4Hlw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krUUYngxLIXnyduaBU4OBmb1chdBk_jP6BBqaWnmwbR6sybKVXOBshYvlsWlVaK0eDRkjGQuWefGEalbaYIHkbPHxel4ltGQffiViXOR0IEB5PWNKEaUiVfgeFljOT-kj4W_8mYUj14FqufjaLkWLFob_HNIG73GSgEcDuTg3sYS0HORUN97oom1voqkkCm3n0FfNACrsyO1OLv9zC_SEAOrBd1FDB8H16K6WqZbeVPk3Ccrn1arafPmks7lN42Qt0SYsaFFdDOpQDp3AXx8TVlDPtCaxWkwaj2UB1ejm1KG-oph19g4TZVzmiMGKfd8dkeIMZKoSC3ib_-e8-4nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPLiI7Ws0ZJIB_KSi5N0P2Sfsu6d-b1kKjrAcUMchiKaHYZYwAkTOeLmABpvHqA7kkCn6e8wawj1Z7ndp-Vt_ntg0z26jn_sLGogtpTgv5tL-d268DBIPguqMNMMhpCMBQ-FlzEZE0p-p496LB8iVyc4XUZf9QxVeL1MwLlvPHQMIw3hw1ftZCu59CfoaGGgAJU_tyNHT5HCyRGaXHl_ZPhP_gyGYZ3WFVf4EvmeJuRfbt3jdeWY8iJeUBe4Q44-uoWUd1RnIx8bRfeIlPjfg2EJ3yV_bT3ah3Jnjf45n_3MJ8QHZV7fOg_MZ9d0cyGQ7Cle4dhcy8JL8PHKhO_AGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcgjctTnV4AykfjXpwINv5v9ERaRv7U7JX-qS3CoPRzbWsvDblvEfd2gUi_MWb-Ye8Ly6rEo4qjD1HRVZlfpueu-bsIQV6vaye5ttI4YRWNcQiLUzDuoWv-q5VNDEZx-kAmtqZHrjqB9UTfUrnlj57y5VIpOEaPw0umh_P4g1mV27S4_m-bp1ztjtXn_jqj4yONy1nDfxhoK_sAxusxKXbd3BiE1_nLdEjiOdiZoEQ2rpa_kd6dEKRYuP0FU9suN3XZX0vW4o6RNOOBCPdWFVM0egpLCjmIyF1KLuCYgkV9kPr3dvcJfVjAPl0Qp38ilZHnT9yde1Ykif6FzNaEfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=o7y3G_bPLSOdPoFjf87ZSCdifVcjOw5BnHEEbso1ALFszQfaLaONNJufjK4_JdjH0g-MHg4o-vPxQtf-Tz3Txj9k1h_doHWlUyRQh2TbmSLYpteDv4WXcHWF72nAEtb3lbXMGxPdPKbYoP2jGCmjABjgdpSTXIdnp_3IEXJo6A5kyWS2fNXnPmGXUziqS5h2tQVGmXi0gBNLkIcI-NmqCnwv5eY1NXaXJl-1X8ZLwibuyBYeoi0Zxb9ksh8M1ol-h1BF65UKQ7vvq_5s0n1g3Wh5kOAojf70rMYXSljoFnUXNs8g3ZshawYYrhZffeTeqjbuCSV1V2WeN5adJPBET4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=o7y3G_bPLSOdPoFjf87ZSCdifVcjOw5BnHEEbso1ALFszQfaLaONNJufjK4_JdjH0g-MHg4o-vPxQtf-Tz3Txj9k1h_doHWlUyRQh2TbmSLYpteDv4WXcHWF72nAEtb3lbXMGxPdPKbYoP2jGCmjABjgdpSTXIdnp_3IEXJo6A5kyWS2fNXnPmGXUziqS5h2tQVGmXi0gBNLkIcI-NmqCnwv5eY1NXaXJl-1X8ZLwibuyBYeoi0Zxb9ksh8M1ol-h1BF65UKQ7vvq_5s0n1g3Wh5kOAojf70rMYXSljoFnUXNs8g3ZshawYYrhZffeTeqjbuCSV1V2WeN5adJPBET4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXHjFl8zEub0yFQjFhEzWsQ4hstn5VrfIH8kBixpNVLt2PjZo4Lur-Wyzh6AUK-Bx42WAmh6C4vvjOqEhODm2tRBoVQO_iKgMe50BzW_4IvJVhGqRW9-qN5kiYYfPdgvwgV1Lt9WhpXWB-OwhPIG92z6eJ-OpnN_K9wSXX23FLQaE7LE6FzTfJamf-kmVatAKwoZ5JFVaiiVelV8CR49P3Av0Vc9L9vCWgnXqsGnI0OPJSM6Q9BPvcSy3KJ10NGp5CbjDvI41REb9k3o6_KtbiwJIN46gE2aTlqjz47LBqMH_Ac1q_4RUGCM7zw2lUvUNGX3hlGyr1bx7KkEUEEpeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxBU9lpK_hshrnYdCJpCI0ycV3wSJsYNoe-GEC9wjIM01a4KlmGKJYoovi2FwgyG-7DsPT2a1a0q-CxoJQ2vDQmyK_-9XsGKice14bfrPibb-DhrwXIu2DPeskIfpY_VBJfMvL3H63C8DJXPasqC0uwJGbq_CkXqW-SMFls9Wa_RilMLb55Oy4FZNurbusqOlbwv6n-QoEdxM7V9ITrvY_bKU0tSlMyt29WRHQxEmWCdZ6B82Uq6WcLOpOvrUWpHgGg3bQopeHP61y0SvzxqAuKPbYH7XUSQjMER97jXJgqqLHNFQt6O420u2hE508-CjXR9pthMfIgS1_rR66EOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3hxWlVrZSYrka59UFgs0FZQ17jyIk1l5JMgpsG6dyRCpA-h6UWwIx-uOOZo-A-OseiA4QxgZyxQIiL1-lBeTgd7amweCLX3EvglqNp_0gfSnUw1dbdBuWnABkc3FF5bp9Qkfq1WQ0jgAs7DKO-EhRX8KHN3Nctg0hnOpVay-WrcnU2s6fLstdj5O_PqDfB4WDRvIpaC4NIRcUAFSRgnOWpN39Rt2ttUNP-NDJ-gbunEVDhrHG01cYHCNsMdOyPcbtijSY73pbTd9TDsY4VnbXjxkGc32rPp4m2c4wIy_TONkyDSyozsnFDvVWfpy5Z4I-qPEXTGtsmDGCLzQRQ89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmReSgCzln7On_TYJo9S8Dwt4MdRg5vQEjsWL_juLZSNKSHkpQXLVwEgUtVwS7SPYiXQFe7oKdCYkLQ2Gl5tIOlXXF9XV4KG7fb-uwZRmV2IjFTMMsKpLB47kxvpIOK6m9H71hVNvJMJL5ebypnuwHRqedqXtWtPGuw72LpKaZQ8lUvFJ-QYVCb8w-UnTxQ3oETJLVFZz4nWPGJJ725yhQwSZ2lBp-NJw-J4IpEFGQST-yjuFZbRelICYo2zLoUwb2RxBTE4vPu0ZYlxOLN2gk1iKi129DDU6dSmMHjIPetwmPjFXmvgq3ZSiUr_sDGwbeUmKJjl8GA_fjIP0S8wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYtSLte9tUB85Q3-TlXk9gL-wjHu2hcbuTDagXaBsZ0kT6qHdJMuldoOcY2jafgFuzwWe6hRGnjIdYZX8rFuol7bqpo5TfXS0J8y2tVGNvDlvkpQPQYV7yM6dtSyAS2ofi3Vy83KO-BEjgqm9vYOtTZin_BNb8LpW4rWPPydcdkKDArce5w6tI2cvoM03nn3BXQ1o0iygI93gu6rhnLAMtDD2OWMw5NyvMjhZNgHin9ot-PuTEViwqEJTtKlhXjVDsrJ_k7gLNPkdo_hGHchVlRmqcAz66UOmsmKvjvzpPFJnyjO14LSEX18L0wp-QMmiXG6YuI0zV8pBxeJPyRaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvAbso5TDgN3K29AR3KWoifTcz-6NbQvKfONFgA2hMxSlqldJ-j5Iry47_AkLd1hn2nUnWjGTFxJ8ogp1fgkan6YGoAueFifxHyScaqq4nFkQ2Z-xzsTPRKfq7kJEkURZQfYWsx29TcD0JmPzcnEowv8-i58Yscffpa48Ofz1Tq30Ocfwf42E2pKpor7rolR0sy9t1ClcJ3vjoRwlfbZuBPoRveCOsuvRHrpqYRGQFjYQ7BwpdmJNwWaRdIZa2CEmaY4OyORq8ZKBdCLGH5RtNEjN_xgOKn6Y-BVJu7C43JGHe2QnL0nld6hwW7ZLwExcfGTTsm7jUPhkqElUMoIXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AAIRT1wWR9dpVVYxUs6O-wNeyM8E1wNqYLS-ZMEdrqMt2FX00OZtnxG5xPYdRNfhPHVFG5KTfYG_usViy-H7KYQdX4kP6z0VnxyFo97oHzW4OhzGpXZXLEUKrnm2U-BEGdYd1qugZkWNw-CdMUBaG0OeQOrNohS2RR9vIOGKAczmZN7kbpU-r_Mylrw5E6IO2XONsVqmsQxAwGAKJmYXab68xyRDa33ZGJPNE3J0Mb3SoqpeDRECY2R5dWctf0vUWpfgWI3SAjjsFcl7yvSiwkyMU-AvmhD581oG0zCmxkk439s4q4lt6mz8g7PqXIJ__Pvz8FuATGNtc66pukVhfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=H0w7d2mqw-1LSCL_UFK_KMhrESA-e-WpkSVsr_2rAlH1vjfiCYZvj90kZ2Dn6cQGHIhsrDSz665t34fVXBc2CjSHam3702_23nWt7IZl9026lD8HQceZrbbgHsD9eAaN05FY2c79lmcd98ElluMG_57IHQ7NQOT3AR6MT9_T5BG2NMNbfeZKw_jPsHqDgefvCTkwGolX7h1clvjf7Uyh6LYmI75k_yjZJxJM6meiKeFMUtH2F6D9YMREc_4ToSS6oTs_H4Q4sxhlAJA-LSE1eGAlo4vCmJhLN2RbQURjr4GR56wgKac9LiWjRzfROz_itzBn9KcqLsuujOdehTF9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=H0w7d2mqw-1LSCL_UFK_KMhrESA-e-WpkSVsr_2rAlH1vjfiCYZvj90kZ2Dn6cQGHIhsrDSz665t34fVXBc2CjSHam3702_23nWt7IZl9026lD8HQceZrbbgHsD9eAaN05FY2c79lmcd98ElluMG_57IHQ7NQOT3AR6MT9_T5BG2NMNbfeZKw_jPsHqDgefvCTkwGolX7h1clvjf7Uyh6LYmI75k_yjZJxJM6meiKeFMUtH2F6D9YMREc_4ToSS6oTs_H4Q4sxhlAJA-LSE1eGAlo4vCmJhLN2RbQURjr4GR56wgKac9LiWjRzfROz_itzBn9KcqLsuujOdehTF9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=qfe5JBFEGG_tbX-HIF7-QYt_5dOYGtCOqDko8tdJ3dSXalzJa8DFy7DC4q2W3nsdTB9_IAgy1ctPguVjDL90yXsn5B5yEOSQmfoIsRu1QgDles90bYh0hu3g7NNDEb75Y_HGhvYjVIznt0PxIIz6aEeY3RjAjDQ79ZVw8h1f9CGrEdI6Fd3W2JTx_98c0F6axuuO9AUmS21AwIgr_JyGKZ95Tto8tIYLsF5YY7622jtBGKbBagmDoWLjKRFhFIoJEBvt5GtF9Y9W75Z8dhnsq762sCeaCI9TU6vsETOy14hsW1jSha_wZAaieRQmHJknSFUvk_yERXdQnBBO263D1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=qfe5JBFEGG_tbX-HIF7-QYt_5dOYGtCOqDko8tdJ3dSXalzJa8DFy7DC4q2W3nsdTB9_IAgy1ctPguVjDL90yXsn5B5yEOSQmfoIsRu1QgDles90bYh0hu3g7NNDEb75Y_HGhvYjVIznt0PxIIz6aEeY3RjAjDQ79ZVw8h1f9CGrEdI6Fd3W2JTx_98c0F6axuuO9AUmS21AwIgr_JyGKZ95Tto8tIYLsF5YY7622jtBGKbBagmDoWLjKRFhFIoJEBvt5GtF9Y9W75Z8dhnsq762sCeaCI9TU6vsETOy14hsW1jSha_wZAaieRQmHJknSFUvk_yERXdQnBBO263D1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh0c25M3-Radw50LYIapFWxNMpqTXXZSXwymZHbsYwasy3eRgYZF3vyyGCIfHSwELSZn8w6Q7M_LOfdVJPkuw1kC75b5C3smSC76NgFWQVpG0w1DLbsofAW-osftXoYyg5I6loGTFMMggdEs_VbsGhxDrQzCcbcclHXethxiFAjH7Q9yPbh-DIQkTIPLHzLgWd7VM19e59Z7J6jJ8eGQl_pI33ao3Z_AJ_wAz6u17iTwCVNdtPxP_SETNEveojq5ID5a02tSOwtt6jtBSB_-cP6Jeny4kGUCKCAuup5ZQ5SXxzy4hYaHR4UhJtjOq4LFJIZTMYpGcaKpRja3I_t2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDt-aZCg9jIZ4IlAMzGReWMM3ChLFbbq4U67pPpkEk0X_aOzLQIqhQFc4dvo3tL3tXvjM9VHsrsTDsZ-OwFrBFcYfOVzJUwLaWpymJUtSJGcUYtP2hy8-7ZPXFLXzFJjrPYGI9oVkGdZ4QYVFsKJyNmUO4Y1w1I4H8l4kVYjwK2vY9PcAQLhdC16epUaC5hlQQyW8WGzR44W6CRuc5v6sfZkuElW-95-dT6MVZjNzChTREI3DFTOcl4Y5AETtaFtKhSpmW8Yv1iuGVoTwTf1mE0I7ijngs3leGHH6SBejW6MyvV6R1z6YGp_MbQeOV5zMkaz1gPR2UhTbHyGsRMYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=TBH63GLPD5lWFYVlQTTsWNUfed1pZhYZhk8WeNnrae9X6rYpFNjiqNV39Vjmz8f3gSwM4Tw3dt_SPXz_sR1WviVqmYXeVFPMP1vL9CzbG8Jc25i0ACN-JfVu57CQm7fyBir94xYy4rMjpNqImQMWquyOGN3QCGsN-kp0OdhvvDOBV_AP4oVuBelyM4XovPfbFaJOZnFwgTcWSuCIFqvIW6vReMN-itbJJiQ1xjyxDOFvwBfXpv42Y7alHDYnt5XG7PHKFe50lV2XMFBgHMmImUJclDcIUau940fP1XkLBnopXQafS3n870GHFbZ6waUL71db_bNXhW4zxWJFgQtaQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=TBH63GLPD5lWFYVlQTTsWNUfed1pZhYZhk8WeNnrae9X6rYpFNjiqNV39Vjmz8f3gSwM4Tw3dt_SPXz_sR1WviVqmYXeVFPMP1vL9CzbG8Jc25i0ACN-JfVu57CQm7fyBir94xYy4rMjpNqImQMWquyOGN3QCGsN-kp0OdhvvDOBV_AP4oVuBelyM4XovPfbFaJOZnFwgTcWSuCIFqvIW6vReMN-itbJJiQ1xjyxDOFvwBfXpv42Y7alHDYnt5XG7PHKFe50lV2XMFBgHMmImUJclDcIUau940fP1XkLBnopXQafS3n870GHFbZ6waUL71db_bNXhW4zxWJFgQtaQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyXp3NH01ldhIrEqqBPe2a1UHlzdO_vN5nEK0irltoN5H0ztt2hnHNwFvOYDE6ezlfgrv2eFRXBbYCCnJffjc1eBWgBYv05JBF4K7m-E6P5xxePv8NhamJaZicWiPSly4c2hwj-jb_HVewOpap-3jtBHtzkvffumEaOXXbwrxi72hVtxVt6x50i4nnXpObux9-SMb9tzatb0GH0RIyG-pm5z1qQmmN5H6FZb6jm6_jMzgsopyW9uhVI0a6VwBNNqn_XvUdhlMJeN-JJ104P1KljhtBzvDsQWJ62lj4H6WpA5GynAoNTtG3JWtRMUGkckIheRLe0Q3oj9QNag3jOrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0cv4bg4fM7ooJqVuRUiP5GssSfHVsUOVcip_G9Jeljb2MfAllCCrMqHYJomSnH3037uP7Y7oLDX5QeCXckBAwqcKtx83WJOXzUNmm5tA8BFBYPZz_Ki7ibCmubRvwq2yV4rfV_tRJsOK2oIGssvCeP5B_JjKcJ_-K-BrUa64DDt4h4rddlcKyEN20fJAC_CdPQ3fyO24LXS2cqtvedsjUx_M4q2DNHP32T5M2wPNpxkzUXcE_fnxFketznhJA3H8dp56vq4FP1TX3vQU8VeyhcaFlRxLlxnqibZkjqKZDKVpUz-Vw75E-3U7n9UE9GE8Xz7PpaS4Hqe-hrxxMYylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=s5WYT3hNTlR5l0_IbMv20RBzqb8iNzIwJ5uZDl51f4-34aUVpFdEHtREIJ145ZYyA74AWlTQFD8DBByRNztnGhrAXJX-cVE1YwzeS1Gv_-YzemfRm4WoTBbPlgJq7S1t3GQURysEPQdlhBs597eAa1D9l9LnJfNTdzU-oJWGDMfhryPMU3elFtpTRPBKupZKJA4Km0yEmw2I-irY_5K0q8eoAGwCm1Z6J_p5XNe5HrHHUgj7vFf9JVZHfdWAVKdVkugyIaXysd50cn7K_pKxOpXlJKhJ5mtqJRzHUR1UduDjyW9Jn5LM0omCMhZ-8eDy9N2Io7WksR7RZfXTyH51wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=s5WYT3hNTlR5l0_IbMv20RBzqb8iNzIwJ5uZDl51f4-34aUVpFdEHtREIJ145ZYyA74AWlTQFD8DBByRNztnGhrAXJX-cVE1YwzeS1Gv_-YzemfRm4WoTBbPlgJq7S1t3GQURysEPQdlhBs597eAa1D9l9LnJfNTdzU-oJWGDMfhryPMU3elFtpTRPBKupZKJA4Km0yEmw2I-irY_5K0q8eoAGwCm1Z6J_p5XNe5HrHHUgj7vFf9JVZHfdWAVKdVkugyIaXysd50cn7K_pKxOpXlJKhJ5mtqJRzHUR1UduDjyW9Jn5LM0omCMhZ-8eDy9N2Io7WksR7RZfXTyH51wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=cU6Q0rX9A3TGWEsq2Xu8ao23Kz1naOrexud_JLRr7-h4b9StSjWqA2d2qlpxaV2RISXHmHHHb4S6kfOdlO1MvQPA_nDrMikRJYShFCV2WNJSTWjBbSy9x9ZprPDmeqZHhJrs7en95OkIpt6IR_-NMBc3IfgKBrratKPGW3eY0riyYfgSjyQXOIA-EikLnzzBAJpui26A7EgA-aRcEUIFSF_0vq7Jky-iRfceF6O8AMon3zz9Sj6deUpK57KMHp1SAwqvO8fB3L19UNRTqOhLJp-nRgdf3QZAN-G-3u1Q9wBAb9YFzhmWTgaoJQ2NMIIWACPasEM1leSfadduU8DTgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=cU6Q0rX9A3TGWEsq2Xu8ao23Kz1naOrexud_JLRr7-h4b9StSjWqA2d2qlpxaV2RISXHmHHHb4S6kfOdlO1MvQPA_nDrMikRJYShFCV2WNJSTWjBbSy9x9ZprPDmeqZHhJrs7en95OkIpt6IR_-NMBc3IfgKBrratKPGW3eY0riyYfgSjyQXOIA-EikLnzzBAJpui26A7EgA-aRcEUIFSF_0vq7Jky-iRfceF6O8AMon3zz9Sj6deUpK57KMHp1SAwqvO8fB3L19UNRTqOhLJp-nRgdf3QZAN-G-3u1Q9wBAb9YFzhmWTgaoJQ2NMIIWACPasEM1leSfadduU8DTgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=pnt6RrBN0Of7PC0K0PhtEX7EWFaNSBWY2t_q5FvMw710ZwNiY8y2u7o60NB2GNMBfg_NTSpf37XmM8ij-k5gRXHvu3OhXyVor4u_9CG-6GmZd_mrUe5aTJKhh2lelDUWA2-6RUkPuDhS3OIHYacfAOG1BLqZvhpRw6UW5pDyM6SVQrfRFCnKE1BXTeS0WrxhA7I8N1UUwc0epxm5QcCACrVXAAzx1q6hOeog-n3iZYExgqJ8b0HYPvbh3wE8MwHQIV3hV6AvyqWmG__hZ8L9GI7essmpA2GJPAsPNFX9-XA7axMgxOQ_SsMKZTHGF_0hX35FFivIqF5COvz23wIohw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=pnt6RrBN0Of7PC0K0PhtEX7EWFaNSBWY2t_q5FvMw710ZwNiY8y2u7o60NB2GNMBfg_NTSpf37XmM8ij-k5gRXHvu3OhXyVor4u_9CG-6GmZd_mrUe5aTJKhh2lelDUWA2-6RUkPuDhS3OIHYacfAOG1BLqZvhpRw6UW5pDyM6SVQrfRFCnKE1BXTeS0WrxhA7I8N1UUwc0epxm5QcCACrVXAAzx1q6hOeog-n3iZYExgqJ8b0HYPvbh3wE8MwHQIV3hV6AvyqWmG__hZ8L9GI7essmpA2GJPAsPNFX9-XA7axMgxOQ_SsMKZTHGF_0hX35FFivIqF5COvz23wIohw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4uyJGh_lhTzQsw6hiXG-BEdWSZix3fSnkm8RyPGyQW2UAhe_J6jczVnoCYt5iTK5asKHvMCpKdmtYIMjFZ-OESpAaW5bwivoFiKjfytLS1qkm5Cy6qTH2iVigD_ScifWhepzAjocB-uciBALd7g08OuKGYOxI8KNtmtvVD1oQvEuy3ZoPS73cKTwWzAnhoWitCEUBHkreFsJb9XmjOdvrqEJaaH5XHwzf4KGTcbmmU0knI8r__zu4HXCB94ambk-L4Riv_LR3i6zz3NBCgeXIVu9AdmTfBjKGuCGBHkU3w7iVdmt5LbsZalDtZksaAmhZDsd39_BXjX9m-0g-HoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXfwLeKr8aw_R9DTSkA_0oSS1HZWv5-h6AoVVjcbf-DRMbvuNNzAzEOqXYGs4wplC4DN6_EQP5ttrJ0tRINP2T-yN6ZuWKJowuQXIxeQvDPcS8gjrSSz_mvmOe9I33_O8ZarOX4WeFuvYc2S917mtxaAyx3GcUWt6udmiht9FAcJxWMuzSYVF5SD-OB8naUFarbTgrbxPo2YY_AY9AajoOU1rGohFSUJifFzaeaNdHFphgyB5NOOutWUr1ZS7d3nQqKrtURSEUDhnpM4O4Y0oS_yiVlzvAoLKklsp7ugxJUjQ8Dl1ml7qt2m5xVG51uoQFsP2gfcb-SLK4wrlWQvtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcR4Z-WBF0zwfwOTLUXRT6mghHZqe6EL7ugEL48TQVEkZa9FKSXeWWUKjiOKIb07hQ62JcIj51Ku9OOegq-mJ9JA8sTYc5RKkC45tgmWhAS72R1ahUH2OCX3anas6cJedFNZdgzryT6tSTlQUJs3s2CVzuvl15Ttv4xC9MRJ9yWxK54TK4hSnyXU-sc-T3X4NHvEJAr0ng_SnLtIzVLlaHariQsTCubeLdOBzPUnb5uFXB8Ot0p05ZGextbhLf6x9xPu-hboLkL-hGPnzpVrm0VSum-wEgBC8rvYy2evb1sI18gQs6KnE982JNVNgSsxPKJz9wO0mqwnt1piBUGMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=FtSvBNJ6WpaEE68RQIahso_FAmHgb19BXURhYBD3DxCvGPt1bCv-KOJkLqpRpOfkHVDjkDLRRCg0fVy_J_GFc0Mf6kxH1nutkY8vkUw6BwfM1euXT6QL74MTb_S5b_BLLX1u8-6-1Ia-GX9XSJi3-BNr_IU_K1on7u-4jrHWkYhlgsuiKN3KRinAwQH2hTJE4QfNFYfYeDb1sE3F2hThe7nC_wxxzeD4CJT2oGceBg6sFTv9cwvTM4riZe_ttkDAm_I8bgXRROOCPTzU7IhUCsYRTWYYRXXzHGd9OeQ8FITkpvk8-uRypJYzZ1Hxx-iW8TQSQTk0Lit-iCSWO39FJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=FtSvBNJ6WpaEE68RQIahso_FAmHgb19BXURhYBD3DxCvGPt1bCv-KOJkLqpRpOfkHVDjkDLRRCg0fVy_J_GFc0Mf6kxH1nutkY8vkUw6BwfM1euXT6QL74MTb_S5b_BLLX1u8-6-1Ia-GX9XSJi3-BNr_IU_K1on7u-4jrHWkYhlgsuiKN3KRinAwQH2hTJE4QfNFYfYeDb1sE3F2hThe7nC_wxxzeD4CJT2oGceBg6sFTv9cwvTM4riZe_ttkDAm_I8bgXRROOCPTzU7IhUCsYRTWYYRXXzHGd9OeQ8FITkpvk8-uRypJYzZ1Hxx-iW8TQSQTk0Lit-iCSWO39FJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=A2X2-TNEVS1WkHZZhH4AX3eXl0nbtlEOyxPQ2G5gBXtF9EneoVElniGCV2JBukO9_E2FshKDYpJB5m3NB9ro3n_dOlrgPbl_X9EMWqTAeWov0nxmmgTiAgtBqEVpzlCbr7MFkge1xinkKGL2ALp_IrEh1YkfSccKW5v8Yf41ay6UmLSH-wc-SIas29nUPcinGwImZJNvj-ZN3SvsUFIa656Na9ObAdpBfXZYH4s6G22GfwtRZQa_vyEcjn73Ss2oze6wlHH7ntZgGNDyMfyBjTYZx2J3ZBVoSfcPF1ahPeqjvTIujLiZEgPYQ5o1aQWlVdddUy299A3goJUbFZenQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=A2X2-TNEVS1WkHZZhH4AX3eXl0nbtlEOyxPQ2G5gBXtF9EneoVElniGCV2JBukO9_E2FshKDYpJB5m3NB9ro3n_dOlrgPbl_X9EMWqTAeWov0nxmmgTiAgtBqEVpzlCbr7MFkge1xinkKGL2ALp_IrEh1YkfSccKW5v8Yf41ay6UmLSH-wc-SIas29nUPcinGwImZJNvj-ZN3SvsUFIa656Na9ObAdpBfXZYH4s6G22GfwtRZQa_vyEcjn73Ss2oze6wlHH7ntZgGNDyMfyBjTYZx2J3ZBVoSfcPF1ahPeqjvTIujLiZEgPYQ5o1aQWlVdddUy299A3goJUbFZenQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=qE5uGNakzuwJeVgikMxEVkrGnQGIhMJE32h2hzMXSKTGxDwkKjb7mcrtvwam9vcbdWXFfY3Ep5cWckXLmnykkmNTt-_37rvmcvZYxMsmOszGOcBg1MJooZEymNPcPMndYopxQuSGIQwwrEXLEgiCKLPeyjzdy8x-JInP229yJD0yFvzwkbwAOwu6p1bRWuPTFjADQfgaUFAkjRGvMDVaDR1jP7jKA4PtCLyHJNzKJaUjqY6_79K1imxChwmxV5ulI4sY3pTcthU4eEzs8PmQ91TJ6W4R2kfE_EeI-k7jGdfcWTTZxoBUhymgLD26nAjoS2Jdj0RiVWGwhCp5t_bv8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=qE5uGNakzuwJeVgikMxEVkrGnQGIhMJE32h2hzMXSKTGxDwkKjb7mcrtvwam9vcbdWXFfY3Ep5cWckXLmnykkmNTt-_37rvmcvZYxMsmOszGOcBg1MJooZEymNPcPMndYopxQuSGIQwwrEXLEgiCKLPeyjzdy8x-JInP229yJD0yFvzwkbwAOwu6p1bRWuPTFjADQfgaUFAkjRGvMDVaDR1jP7jKA4PtCLyHJNzKJaUjqY6_79K1imxChwmxV5ulI4sY3pTcthU4eEzs8PmQ91TJ6W4R2kfE_EeI-k7jGdfcWTTZxoBUhymgLD26nAjoS2Jdj0RiVWGwhCp5t_bv8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=Tir4YAP2LGYGThFszXWwFSWtuv8jk-AzKDGFbsvjMMAUUrn5PI0WkcYfIRDkhQJbfBcN-cWmWwSJ_aAC06jEybHw_eFsHFZifsTob5LQJMgcJt4pIqgT0GbG7hxdK9tljfIt4Q2aWGRk1V7tdBsKWGAOz79VB3VLjLD-wtZm2uFWavEVnMaYdBAkFxDHH_OG9HZe1h-ezhfbl3VgwhkeqTZSKq1hs4fkhIB7FeXGc1fciROljTxQVRGkWBS9oT3Ri8hNMSr4J9RGh-GrWUdRUsExAGNIi-D864gLFfPOMt-A23cQJA10R_BSjy_3rXQSUO8VebFZlb0pl-kBiysRtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=Tir4YAP2LGYGThFszXWwFSWtuv8jk-AzKDGFbsvjMMAUUrn5PI0WkcYfIRDkhQJbfBcN-cWmWwSJ_aAC06jEybHw_eFsHFZifsTob5LQJMgcJt4pIqgT0GbG7hxdK9tljfIt4Q2aWGRk1V7tdBsKWGAOz79VB3VLjLD-wtZm2uFWavEVnMaYdBAkFxDHH_OG9HZe1h-ezhfbl3VgwhkeqTZSKq1hs4fkhIB7FeXGc1fciROljTxQVRGkWBS9oT3Ri8hNMSr4J9RGh-GrWUdRUsExAGNIi-D864gLFfPOMt-A23cQJA10R_BSjy_3rXQSUO8VebFZlb0pl-kBiysRtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip3vdjgF01XkilW2ULqXGOnUWOYugjQZAXPQ_4YdSo4MeeJAQpkLdeWactbIuCcyjQgAEnVk2bnJG0fZRjQflsueTGaSS12QxTeyLc1Z6zZygjW3N9-N9hs7WeBCpupQbYlAT6LK7G_y7CSB8n7fIaUrh6q-SYMKMepqkgLfYf0M68FOKegx7U-r2tQKoVRuPHccEDFYW8RT8bt3NEC9K9X-P6-iusmYmrUTSOPVunQHQ-wBuAW53uN8a-hCz8ZR4nIX8TCtNbqcABB7xCNgdIL317hg0lE0Gq7XHIXBHMCsdCuNfS11D04Q0qYFGwhQS4b4taJBrOlxUvLaKsxVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oETnCy9ZiKzmKnHwB6l-_6-hsEU28IMXiG6NjGsmGGc2FhFY-oftdQU6-rHvqKSKFnBjVDrBuV-gx7MUY7boE306r-TdOROQcDaOoPlxjAmEFvfg_faKYX_Iolv5cojgqgu6YkilADQBOa7AJdaWGEJ7V8pFmsg66_-BhaTdhB4nbQramPjjMiksxi8aDLds8AsI4DhVzklF9QW0gGk9EdJu-x9-6QC_8bxzHiGXzFNnG-K9l_kyLXHUeKSvSoWbcTZqJhvBcu8iF97hfdgDLDWp8mBeQc7s51siy9SUmhJi7atKrhhkL9z6dNEEpj5WgVIZ9En_dIFl_CfvzgijfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogBiUmaYZrfdG_7tQmJEZtwpu-Fcv3wK-s5L202HagniIwlC-us_GBXDSM3BpHhL1pqR8o5C5SGtfUEXluPiC57Ri6Wc4l4U1sURn2erQe-RkjIaI62rL6nALd9kNhSa2a0nYIcvJp3MlA30zdqoBsNlZJUd_TAlXhhm0diLjV5Y8CwTstqCaieISM4Z1AYQTSOkW3bnFV-w43b42lRDvc7W6fqC1ljH9WOtDGAGjtvlm61w0U42B7A7E55vt-jqSnqC3I3PbYLk6SshMbyNJ8ONVP2YFlO0E8HCrsE0kWgi2vvBArGSpND9d9LzJx4GwVOl9wY5PMGGStpcATNnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IukIQNk07b3OZZTedntcycow-sTYArlOVF4t6Jyv8ocHr4jMoZEiPrGcGMUdYM9uhQX7vOU67oMm9Rw8IvM25EyE7Y2I0pYyv4ouuVxMmI9wHz6QXLV-jTZLBozil0y4LNAzlzIhZOnH_3gFk-keCxJfakMtENRgu_zmxOS9fhKsyyX3ON-WNnZQUuO_Mo7TaWbZB1_qWgVj1jb2MHG-wjBMiamn-NwC_9EYpnHqKaQph_8oDLGJ5NOn5iIPKe4ebR9fyqY93RmERBagp9x_-vB_7zQJ09Um6VlMcNANpvZtd6hxytGfG7P13wIBnbXuDsqsBjUGaG3ubQkMba3lKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi466XvFQHlCPhIiM-mP0qaNCrLdKZnFJjyhDCIVPDsqvIlC2ak4Id-mm-eqbHoOHbiafRgYxYFijkMJP3LLOf8wiwiN6Xxw_jtGWXO4rqnDDu2Xk6esie-PfMHJnkHN_cmDErVoghHDKd2OCZ_fOtJ7w7em8RkTkHl8NRYi5DCv5VC1RCaP8kOtysDnZ8Ma1G4yzuaxLc-3fiMRm4ZKVKfLPhnVW7s91I1WyGbyZNP5-SIa0A2vuzIce8N05c-M7RlrVWWuKV8umu284HFp5MPKk2SHcr9kB3fV6nk6E4Ch3ybr-guo_FvSG8aPG5z5L3BEWVCflRgktJUfREaIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsXiNYj0yyIo_5IKEHNRDTC5Iqw6xcVgMLOS42If6g5mhpdm3QnK2i5Q5pOGwr6Wcdn26yJp_GHOW3fh6oRIzcZnzy5wAF6DjCDbts5X_8MHdszhapMHa71EF0TZt8MbhB202ZF3mRHfdosWRusQgLLA3bKwULZ1LmeoAv3wl08aoNXsC5neD_Dr_PiOxDOqmsG75KdYDP9EvxUCXSOiZRb5rNtn3u6E_GPbxy4Uovw1uxL0TmoHIhm_Vw8fQoA1QH2gaGh7smgZ336Ni9alZuznYxyHqGRfTHps8RSvgF8aH2Nr_eLwKt4hU9YD1MKjL4CchWhQ1-JpyKLx_zH1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
