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
<p>@farahmand_alipour • 👥 64.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 09:57:06</div>
<hr>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6gb4nImEfhkyP_S0zrKaWfs8Sya7xSIqv29BcJCKYxXSK_oPAK9290IYIM9q5oa2pOTH-r4VuzjQMGEyvqyU2ILxcavXyxY9jsduEI672eA8KjwAN5mTcL2sqnMJSXdK8zQVGBsp57r5fHwBuTxND1J6fIUcAEjFVQIO4WqmEtx5-oV71_A9GC6EPa5krmQQWu4ycndS1iKYRrx6LTGeNGe8fGZrEMydxG7p3Ujes-s517eCRUrFj0Q-4Gbrdwz4B1xDgmcRLeVlBHjFaGTDyIbBWpGdEKn6fINd7pIQaj1JVbwuTiqC4T4dBJdFM9oT6JxeqeIE_orc385N13iHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=IpbwZHCJzhDHLKjx3Nkg0fq-fzv_3gXJQf1jfJfTqV4ppZCczGbkcf3MwPltUAM7diatGi9Zp7-CeFKGcyfWZgOt2idsQmTjY3_tXW99cRlxPO7v24PL5fBpuQI-_sysywa6mGC-blVRp4QzEEdyrikFj7n8gFPjLzqgQeTTeZHQmndyuMx3OtSoXQSvK5ABO2xmtCTuVEHlDqzNLvRhryrkzmqwqC-QDy1uhUNb06qImFGVaMUMSyLMHsvvAPSwt0jMdtrxrkkzi0fuJJS3-bovFwnnIzQMBmhOIEsM3pyAJOrE848uzm6SV5m7JYL5T1eyAXdg2xJ2_vna-Fg8rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=IpbwZHCJzhDHLKjx3Nkg0fq-fzv_3gXJQf1jfJfTqV4ppZCczGbkcf3MwPltUAM7diatGi9Zp7-CeFKGcyfWZgOt2idsQmTjY3_tXW99cRlxPO7v24PL5fBpuQI-_sysywa6mGC-blVRp4QzEEdyrikFj7n8gFPjLzqgQeTTeZHQmndyuMx3OtSoXQSvK5ABO2xmtCTuVEHlDqzNLvRhryrkzmqwqC-QDy1uhUNb06qImFGVaMUMSyLMHsvvAPSwt0jMdtrxrkkzi0fuJJS3-bovFwnnIzQMBmhOIEsM3pyAJOrE848uzm6SV5m7JYL5T1eyAXdg2xJ2_vna-Fg8rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gce1NLAZC-vFMvQgHZXpiYKVnvfRJAOZTB0OkQgLUNj-qT_WnOoTvJs8oYBTfELWkbxLA_Z9Gx8gtmevb0AfhnvIek5x4wz-vcBXgnWBCxeu8ZO0WwNUC4Vl-lqJ-T60tj3bVVwU7yyTc-HQb6XNplHPap65ZQbWB_mRfSBxfUjXAueOK4BtL0Y6xGg9CggbFvu43dEVbmN1PfwZRipqU2AK4sEKgtBzcR2NHWJsh2YFrVlGkL1C4NhPrv5Z4_d_UGQOyIKj-RZlalJYQmmd1PpGKMFAjIeOSKQnx9u8kpGhG6zNL6lifvI76FY7fMhTZLwKoOP1oQN7XSk3OohgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=qSKi2hqLVJvw3L1RIGNqHWrsvrnKXpnazU-rGVkSsdG3grCdBHWx-2Eom7ot-wbI9gITmnJjr1i2BnykbEzQZmpxD3goSWE1Q29FIVK9EXn_NNj_LL70NMN2e2UM4EFToP0DT47QYOfohHniDvBMm7E3hQ-vdM9RjYulNjZPDbKCjHL2-3X-9Fc87QBYAIR-3I2N4HKlGjNq2Ip1C7nMRpNL_W-k0bgpXJ2owWbeaWK0q9HFkhp8vsHyrt1OLwCAaZCrGYhh1MS9JM9erla22ptnDOja_evBeqiAdgrGAwmbKdP-So56zXbgdUw_N1eXQ2VVTpRssd9YOs_B8gTnpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=qSKi2hqLVJvw3L1RIGNqHWrsvrnKXpnazU-rGVkSsdG3grCdBHWx-2Eom7ot-wbI9gITmnJjr1i2BnykbEzQZmpxD3goSWE1Q29FIVK9EXn_NNj_LL70NMN2e2UM4EFToP0DT47QYOfohHniDvBMm7E3hQ-vdM9RjYulNjZPDbKCjHL2-3X-9Fc87QBYAIR-3I2N4HKlGjNq2Ip1C7nMRpNL_W-k0bgpXJ2owWbeaWK0q9HFkhp8vsHyrt1OLwCAaZCrGYhh1MS9JM9erla22ptnDOja_evBeqiAdgrGAwmbKdP-So56zXbgdUw_N1eXQ2VVTpRssd9YOs_B8gTnpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpdZ4cLYQysJYwE01lpVnQZDmvQFoMK65AVTTO524XZdRvK8Pa7G_wq3Uf-K2HJjHKPKxD5yDpFbb9JRXp8CCpgu3pwY8aEu18k7p6VKJS6FokOYBzA8XlIOlBlUpKDwwsBCxguKjpX0fP8ZpC5z5j_gNkJ1yP_7LASdRik6EytDnriIi5TrspZGn0CpcEcwFGT4BZyrtOmHjjVXWDbkZ8HVKWGuT4QV7EX8A0yYmX4n83m8RYv5EMbyfJQtEuAPozy7KCS24xcqsaQ5Qlg-BOKBk_o82UopbdR6EK611PKMIFLfC86aKKTmr1m4vXGxPPsS_EOURTyJfbhLezqvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNCjjBpEhkuKQuGeP_fMcQSS6tdyT9OjhtgjkXcGEuu1aDo48IdBghwk9svfL2bMu2diCJxNFePBla6ttDsaPPOdLRUoGRNhdHFFXBF0WN-8k-mTOe3IkKvecKj2R6ROGe3-VA-0fyJBu3Pn5jARA8r1nD8Soqa8youQaHcn46ACR3x1rJ9UKG3MzzgbqEyRKD_myyBPH2By1xfcpM17WmOXkVldlUKeg0VTxmW-vsA7xcr1UecC9sBG3NQDUvvAsNwdTDTFcfttIunXpZohhw987k-IsGMBMSGaJN8rcNHNmh85UgLHU6e5uQHjMOYc6BgSsldg8_dBtxxbmxDGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=nshR2fYjzqu5NGegEgHcH3h91epV7qNKwsgUwCkioGyBFlhkc576nskLHqaNSCVgA4moXF3IoXrY7VlTE_lRI6gkLSwUf8DB_IS8wOSRIGQFqNUVarbdMlPR3lMlLdWyk50LjcykIMDKSpaJUu8NNpymooDc3fYk7vD61bk2OT7oyLsLUaklD9sHI2fQ2KYC3WUm10GT6GPzBRI90gd52Jy_2i1iHiJSInRvPm_jgQ_nezTpeEre9PI-lLUyVwTC3BPLTNVU51OJdi5u2xeShEUYnYlxSBY8njCirTveoXklIRYEqRN3gT-V6agVHWg74kJQt-ebKfzLYkrSmVNAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=nshR2fYjzqu5NGegEgHcH3h91epV7qNKwsgUwCkioGyBFlhkc576nskLHqaNSCVgA4moXF3IoXrY7VlTE_lRI6gkLSwUf8DB_IS8wOSRIGQFqNUVarbdMlPR3lMlLdWyk50LjcykIMDKSpaJUu8NNpymooDc3fYk7vD61bk2OT7oyLsLUaklD9sHI2fQ2KYC3WUm10GT6GPzBRI90gd52Jy_2i1iHiJSInRvPm_jgQ_nezTpeEre9PI-lLUyVwTC3BPLTNVU51OJdi5u2xeShEUYnYlxSBY8njCirTveoXklIRYEqRN3gT-V6agVHWg74kJQt-ebKfzLYkrSmVNAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlZFK9wY08LKvp-g_POmKnjp8d6UXtxkpC0alk3PUJh7m4h19CZW33HPde0Ot9QX6LuazYSXHVwniZ-xXEMmv6lQ7JcKB1BYX_eIEMNjQXXDk-vCxATn0DuR4vc30bsS0OnQnr0shOvLgNE-nnZGyHN73XKMzdgMYbd_K2vd5ME9TWpnXEx-TlH2sXAmNabXg64LfGks7l5arHhnHuSpbWtX8Ud7EAnqpOWEv4TykMeXBMz7dUqP-HpFwEkBndQUpBS-8Yk0BotRJJ0yV4l19y12ZrdPcuWNB6odl0aPXzo1ybIhxNa2IyemU5JoSdwDPi-XHbkcAiKhh6DKjJL7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3-cwl0e6ljJt6ZZ9i6muM5CgEvZ2mqMBsP9iIFwXl4o9G_dtrGCLCrWz6CrjvtVEKWo_xi1D5IrRikg0bV2745Hz90WBtUB8cwWMwDx5wOb3knwzAVFgywBc0DUirrcczEOZ0NWV2Di27oexxRf64LLr2iMIq0L9ujtcij_usA0o9lTOrKbwdB6Jx7pSct6W5fvXlVlMr_Pi-X4pELlWblVWW9aEZ-v5Fqg3fGpJV5c6xKHGC8OYy3tQ4d9SSKwHA_futr9k0eULd-x6HEfpbS_aYyJMOUd9WH1t09NjbUcCP3sLlUGOc86-k4fWSxpGDnV17RNJLrKnqbeYV6a2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKGEHFGsFfoVdymqKNaJCG-dIBPPQQ4Hh_c8Umg0_WEZMXNW8PRGVHwtr_YLUkmgjgkcvRF0-_AB7fsjnQuErk2U_XfLYhIpmoYLvNRmh_2JjdqGQ_b79ZNbyKbqguAcCn-Y694mBoSYA9TADt2EO5rCJSMVkDUF-69I4PffBKC1AhW8Kx53ufkZBrfGF2zIGK4a4LAVPhjHQo-e0nGMXUyyu-u5DynEvnmkTdwJtObP8nSSpczvbfZDlTMlyDLFyNZj547bWYUee_39XhLq3XZMtvONtfOunyN51g0L3d1LapnBJ7l9R6aIQQhAyv4rD2auoxLXNklNg8QpJ-W9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=iAxOxBCWExqmK-a-vsHM0ZnsutQXu_eOwUOZWijEQOXaNC-WdenlIDvbiPSq9F3lSyKA5UNXVd2p0JkDmrqpBWmVVv6h1gjrQjaKlnoVgpDJtIOM31ad-2rjR4xvxLdavlWiz39sJrm2rVQuuFgrithvvQMSqOmm3g6d2LLCG7M3Um88g2NM8J-qWyBNvtXxHZe6fMtMmReN22Sy-BhmaMuIdtA3F814Oddm_r6SXc1BawjRRSuY9bRy8jvjQKHE3TKMvHvyZSX2McrBRCAeS-7d8FHB_RRW2HV1NP149Cam_heGKSWUpRr3empWFy6O0cZ9uViCyIj-YUSkaM2TCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=iAxOxBCWExqmK-a-vsHM0ZnsutQXu_eOwUOZWijEQOXaNC-WdenlIDvbiPSq9F3lSyKA5UNXVd2p0JkDmrqpBWmVVv6h1gjrQjaKlnoVgpDJtIOM31ad-2rjR4xvxLdavlWiz39sJrm2rVQuuFgrithvvQMSqOmm3g6d2LLCG7M3Um88g2NM8J-qWyBNvtXxHZe6fMtMmReN22Sy-BhmaMuIdtA3F814Oddm_r6SXc1BawjRRSuY9bRy8jvjQKHE3TKMvHvyZSX2McrBRCAeS-7d8FHB_RRW2HV1NP149Cam_heGKSWUpRr3empWFy6O0cZ9uViCyIj-YUSkaM2TCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=QWKa-EvFsUWynlfGeIDmHiiqM4R-KHLmdltEP48EmVpwH9s74HB6aHco2ldf2VFK81RZh1T3FmJCK2WEMO7Rzt6hpW5d0QxF61rRBd59rRz3MaCG2Zbbzx91213zNssVPNTIkyoS-FXkzF1cUsdMNfjVngjYRLAV3yQG2E-lVlSJGtvAadTPe2ceOj_xe1OHy04E-4eXocUUpLQQie1PU9Xu72VPKS4En5Fw14UsFk5vl1IFF8Ps16ryvEe6DboQ4cBktbyLZmyMwA-vl-nVYQK0TcMjU6NIIy0o0tAVmUBRmA3kpRtTSE5pvHn7RL0447_jVf44BMc96oyRDfRk9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=QWKa-EvFsUWynlfGeIDmHiiqM4R-KHLmdltEP48EmVpwH9s74HB6aHco2ldf2VFK81RZh1T3FmJCK2WEMO7Rzt6hpW5d0QxF61rRBd59rRz3MaCG2Zbbzx91213zNssVPNTIkyoS-FXkzF1cUsdMNfjVngjYRLAV3yQG2E-lVlSJGtvAadTPe2ceOj_xe1OHy04E-4eXocUUpLQQie1PU9Xu72VPKS4En5Fw14UsFk5vl1IFF8Ps16ryvEe6DboQ4cBktbyLZmyMwA-vl-nVYQK0TcMjU6NIIy0o0tAVmUBRmA3kpRtTSE5pvHn7RL0447_jVf44BMc96oyRDfRk9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loxgIdBKmVvfN_sU4P8fspyYxTWCYG_ua4eRjIFTqns_n3zBjmXSgoKO-cwG4fa1Jf1oPpD3nKJ0hrhc68J1J3MOEsn_1bYKvOyk6pZeusa59G-bSEEv5hH5KDHpf3XpYHSjPjmoTHuV2LUrTwdfY6W98mWzs9PhdPYdl6kAGjsDFTbtEZHkBhq3_9PqTF3_rr9xW8x0Ok-Lnf16DDXxY2Xh7cGnPa0W57vuOVBuRGcqt7r-vu59EXDWoNaP8PMGV-oGBpniaIFYSvGLrmn8sHtvTmZPncvT5dp0S4vX2VZfzT4JS1PqlJBHjKuNRlE6bcmxayr30eoXp3tqLtig2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-jTL6RzyBtfZTubcwgEeLnsi3PoaMhMZlBM9XRumfxO05L0VsUXZHDcvah3CKGzjO36X6fHzAuuIEWPI-BHJS94W1E2RsgxvEGs8akI9SImtcA_oEJTaKrW28Nv5xYei_y4v6QGerdRu3M0XXKGGyBr2WuGTlJsU-8eRyfOql5PtKGzd4x6zRCMI4zWzU9DgPzgVZorUPyegoDjU6gnCR1DZM2Zteadwon1zCoQuJh8Xt5jsxzJgW8goszjgeMB6lec520OnnN6g_AVwBXmMV9XPzyrQSAGfbsSxyHiscXXskSnp8TnYV35dOiz3yE_JKerlPrmTr-h002II3HH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVLP9vw8EwMAOXLdYc6X_Hyb8Zm15QC7NvgGkYUZoq8WB7dtWM1nPlCfMs89RS2Ts4S6vSUtDkohY8hH5M9vtLzp7JIqDRXoMRtx_wMO09Ed1zspIQy8s0l2C6RsFUU7soeeliNiUvuQSrsCLhjq4oSAR7Wa22ruqiS0xnq6FhFvavCL2QUAWnoLiO3fLaaomOBN78ohVTWOcy1eC9DKG-kfI7ixSE5T-g2iDwOD7IPxQpca0vcSg28dsagVzs2-a7wNmHy41U3hrUL_RE9KII0BcOl3ulWZolzDNcShL-w0WsiOfhFXSBwC8uwzhk6XrzwfQLkCaVn0cC6gDRpeYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3OJ8XgxBvC9TRDbg2veZdjBJC6N3Yt8Em0mzhyOl5INqHQtFvTpHhfYhc6Y9MCQJJ3ROmb_GzKUGF8jQIg70DlQdXvM-YBJzc_af5d3rV0OlL-tk9RU3N1TFMz2g19PIKgE6RzauDO49Pl9s3bRl7TzdNDpgrjNEYxlMzAPAJQrKIBOOlL2QJaKcScGvCeDicMGfnUsWVanOv3GJw4zxIynAxJWYWM_4cmzYjqrg9WoA21BXPbvbsf9ayabIjyNdot_96Ghgtz8yok6Kvr8LFyy8teoo5--zCGu9tzUTjJjbHkprXfxJqz5jSxS4k-bH3iLNBYrmhyg0P2lWBAKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOSSvfP5drQ4eF67kZAcdTneyW9QkGmxH-UxPcbnVoFxJeWFptItrVGRcIMKHNHXC1ejWyV-VeH5sZOWTY99120vSkpfusC5b_XZR4bimdIB6YfgABuPhnFigpaojRRGQ7HRzW78ZeMhZACVFWp1srp2pHdpJNQroznGEf8F5qoLo5LmTytp93-j7gDg0FxSZUaNtY9TNsvUdpfhHpiaHFkvRkD-raWOUFKCXmzGAC7q_upOjw1pgAmGgrbmNL-aXr5eLMwpzx8paH_tNaQT0ZaX6BIsXA_R_s--eYSOFS_wkOPnT5BrIfaNaW1TOLQJlB8Uhhmd-4e98yNCp2PqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RitQuVj7GQyECAx8a0crmHYofj0RPaTnAnbIUkwZSISX7Exw5H3RoUKrxmYtBdyu4rB3BTpziu0g_i-W28gUny1DJirbzf20tbpETcxZDzcwSS40MMiWMXcaexi68DmUmda4V1VEYIBxsKrntPiRVWc8XsQIxOEjAUARj8-wI634gCnd9PxSIfcfaUYadMQuqjWEtGbQKYBps_3kUpw6l-ydrxNlxKdZNhF9n84ZqwnWxAwnjg7z00D5qR9-sZKCpCbfeIbqvxkHrqnJKbyYzqDZT1FE3Xz4CEceOR5xZQbeLrgVa1liooRbp8KY6q3ecZeHzjTnKSJk9-0CgX8Tkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=KreG3oiOgV0ZqsMITjP3HFuQYLt2ZaytNy-qsIdNXpL81oJXqgXwW9rKcyz54gSuic46gOe5vRW2e78ASzEAICzq0XN8Puk6yBwKQ3GlUWbPaa9OQNyarQYenvrLb4EcgUlc0u1QSm-N38pOgsg-3uH0QOJlp9d_f1RvWl3GIDaY3F1doaqJ3Eozxne8ld6M_4wn6mPcBGm_VgVw9VbrpLpZLGaManu-tVswELvKk90QeCPj38rSeRdnu6pkL-TK8HfyOQLT1HJKYXNJJJcz27d0SkUEl2e6fXW5dNgI5yvhGao2ZaM_90l67QrSQs1kSXv6FJduIi2KhdIlGjJ6Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=KreG3oiOgV0ZqsMITjP3HFuQYLt2ZaytNy-qsIdNXpL81oJXqgXwW9rKcyz54gSuic46gOe5vRW2e78ASzEAICzq0XN8Puk6yBwKQ3GlUWbPaa9OQNyarQYenvrLb4EcgUlc0u1QSm-N38pOgsg-3uH0QOJlp9d_f1RvWl3GIDaY3F1doaqJ3Eozxne8ld6M_4wn6mPcBGm_VgVw9VbrpLpZLGaManu-tVswELvKk90QeCPj38rSeRdnu6pkL-TK8HfyOQLT1HJKYXNJJJcz27d0SkUEl2e6fXW5dNgI5yvhGao2ZaM_90l67QrSQs1kSXv6FJduIi2KhdIlGjJ6Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=Lle8E4Z7cpYfaNPqslJ7eYVi7SE3qwBUnRCpvOY4r5r2IzFovzDHcYM11DxHS74ac-9akQaa8vTi7aC0EBDTb-1793QVRd-a8i4YI3zAsM1TTi_lerY-rubs4k_tyxLRl2Inm1VzT0cAa5eBNPE7WoByRUBS6AC1_NkzHuPc8Ky2sCokPxD16KYphHTtQ1E-U_XRAa7TI33SvT1Vp0n77IyaiVvf-1buB7AlGcCSGGbvWPTEJH7JhdD9WEfTiS8jGuYT2xFBFy8XZPpvtYMXgDCa1UVMRofO1mGbf_uAMcTg1utxVDmAuv7yE-QhOVdWfVUjcJoLlONDWWe6nKQdoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=Lle8E4Z7cpYfaNPqslJ7eYVi7SE3qwBUnRCpvOY4r5r2IzFovzDHcYM11DxHS74ac-9akQaa8vTi7aC0EBDTb-1793QVRd-a8i4YI3zAsM1TTi_lerY-rubs4k_tyxLRl2Inm1VzT0cAa5eBNPE7WoByRUBS6AC1_NkzHuPc8Ky2sCokPxD16KYphHTtQ1E-U_XRAa7TI33SvT1Vp0n77IyaiVvf-1buB7AlGcCSGGbvWPTEJH7JhdD9WEfTiS8jGuYT2xFBFy8XZPpvtYMXgDCa1UVMRofO1mGbf_uAMcTg1utxVDmAuv7yE-QhOVdWfVUjcJoLlONDWWe6nKQdoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=gwEHCZKj69Vj-bLaWFza4ZxxtXghX_ApinsDhfJemwSLxwwmg6qYuLYoV_3lTaA8rnabeDZnPQcs1Y9b-BNX6Jo7yzB_h9EK4hXrqSkle3zy5WATZ1D8Cgcv-zxQNa8f8bQYFmrhVsPTGF11II5pb2Sr3qKLhFFi1t5XQayfZRflxckMPtCEu1rLpXpW1k4KLX5Ho0vhsBefNJVW-5KvGNutBZVOxrwY2VL3-F1868NzG-oOwafCUNjatYCNqz5fZc87k9WMkYxwkBQvlnAdpvIWNTebos4PlUwcHISDE9EKqfM6vDUvY2OxWjyiQ-TKgK3hWlKG1KJHoThbXCkNhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=gwEHCZKj69Vj-bLaWFza4ZxxtXghX_ApinsDhfJemwSLxwwmg6qYuLYoV_3lTaA8rnabeDZnPQcs1Y9b-BNX6Jo7yzB_h9EK4hXrqSkle3zy5WATZ1D8Cgcv-zxQNa8f8bQYFmrhVsPTGF11II5pb2Sr3qKLhFFi1t5XQayfZRflxckMPtCEu1rLpXpW1k4KLX5Ho0vhsBefNJVW-5KvGNutBZVOxrwY2VL3-F1868NzG-oOwafCUNjatYCNqz5fZc87k9WMkYxwkBQvlnAdpvIWNTebos4PlUwcHISDE9EKqfM6vDUvY2OxWjyiQ-TKgK3hWlKG1KJHoThbXCkNhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=jZya_ILYTQAEUchVy8Mbv-1H50q8MHZ1s_Z9w0Dn0tgWRyWZxttMX9-QDZFf_JvtymihjJA6XUR0KaEdFjptoqu7TeC55PoFTam7nn38SXFyajSL93TT2v9tJ90CF93WgFzmLDdfURPY9lO7jBatr-p5bIR49qMqlV9ZThjRFgPnkx19wkqxYRW9gSmn3y6_Rghbc92ZoUFC4q_Dfr-Nxudu20gPUBbunAarEAB64CjUAs8lHUdYbro7u4uNCj-JZW0IKlO3fLRlP9B8UMGPqCvNVPhL8M3FcCwpC0h1vn2yiyMuukpfIdM8hdXNZHBub5gm4ddg8MP2icYKB2dHcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=jZya_ILYTQAEUchVy8Mbv-1H50q8MHZ1s_Z9w0Dn0tgWRyWZxttMX9-QDZFf_JvtymihjJA6XUR0KaEdFjptoqu7TeC55PoFTam7nn38SXFyajSL93TT2v9tJ90CF93WgFzmLDdfURPY9lO7jBatr-p5bIR49qMqlV9ZThjRFgPnkx19wkqxYRW9gSmn3y6_Rghbc92ZoUFC4q_Dfr-Nxudu20gPUBbunAarEAB64CjUAs8lHUdYbro7u4uNCj-JZW0IKlO3fLRlP9B8UMGPqCvNVPhL8M3FcCwpC0h1vn2yiyMuukpfIdM8hdXNZHBub5gm4ddg8MP2icYKB2dHcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=fAzxT9pI4oJmmM3jeHMbTum1PPM8vpWmp-4KigPjdNeTY42goV8nnlubwucIWl3b0idrZjwoyjChErGbe_T4JW2SNokhxLr8UgO0ZOUxlP6JcafpwXgyV3AtNt63vMZ8LAySUXfZ8JQxHwVzr4XqUGtyaFc1bgFd9v6AQwfwJQ175M2NaOZR9Ir2iGoHB1ayU97C-PojE8Nln_I4mcP1MILWcjjAV1IbCZskD4W5sfY0gDY46VeLmOyJDRvjEgVW1-UlIXUiiu4AtZCpw9WcXBNwGfIvGcNi2G82LwADTPy-kwIFKEMpPFTW9rThM2_1ZpiMnkWWEb9WuCNORN7vDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=fAzxT9pI4oJmmM3jeHMbTum1PPM8vpWmp-4KigPjdNeTY42goV8nnlubwucIWl3b0idrZjwoyjChErGbe_T4JW2SNokhxLr8UgO0ZOUxlP6JcafpwXgyV3AtNt63vMZ8LAySUXfZ8JQxHwVzr4XqUGtyaFc1bgFd9v6AQwfwJQ175M2NaOZR9Ir2iGoHB1ayU97C-PojE8Nln_I4mcP1MILWcjjAV1IbCZskD4W5sfY0gDY46VeLmOyJDRvjEgVW1-UlIXUiiu4AtZCpw9WcXBNwGfIvGcNi2G82LwADTPy-kwIFKEMpPFTW9rThM2_1ZpiMnkWWEb9WuCNORN7vDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=WSutM6FVWw_P6J3JmBrUtlyoR0uGagPv6R-LKKM7ibuN473k99VGiKbh6ul0DsKQZrQlDPQme7ZlXB9BmTRw6Afdq0zj9NQcOzMb71_UO1CFCOnKBMiS_hwPhebAo0dNexABQEGeNvOvG3kcuc8yPAhs23UxFVmfdtu4-770P__0blgP0yiRc0Tt1sUs_Ubs_-XKeVPSuCmmQ8m-D2UNorswwi7XUutCaj5fOtcKWCbAOtkHrx2aoI51EptNbIaPRPCazSaj5BQIu18uvchjyVdkCK-lY6xQsZ6prapcAHvlwD59TVHZazKP-HDWjBgO2chxdyHNBupiCRru-bgjVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=WSutM6FVWw_P6J3JmBrUtlyoR0uGagPv6R-LKKM7ibuN473k99VGiKbh6ul0DsKQZrQlDPQme7ZlXB9BmTRw6Afdq0zj9NQcOzMb71_UO1CFCOnKBMiS_hwPhebAo0dNexABQEGeNvOvG3kcuc8yPAhs23UxFVmfdtu4-770P__0blgP0yiRc0Tt1sUs_Ubs_-XKeVPSuCmmQ8m-D2UNorswwi7XUutCaj5fOtcKWCbAOtkHrx2aoI51EptNbIaPRPCazSaj5BQIu18uvchjyVdkCK-lY6xQsZ6prapcAHvlwD59TVHZazKP-HDWjBgO2chxdyHNBupiCRru-bgjVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=UwR6rHn6Coud2uh4UxaQ-Xs4XQVlByf-9e1nace2ljd3T5BBN5L7Y2DgDeq-UOz356XDxWgG2WxzKIwZo3LeGW3nz3JEY7T3l3Cmj_OhihVBRWYqe6fHpSlbx1AUUZraR7kz3Wd6jJIFbr45_BrT9zF-T07XEI1Jk2oSgu_-PgcUX-FVcqTGbeaWYGnpA5v29XpKFhXB3YOIFUlDNj0mTWk7umJ4Q_IrkKF5Tfr49L3bE1npK7LwrQrEm8WSkqXDn8o5KqrPSJ2N8B35q9AVXGnR1yMlplO_WO6XOAS-yuhO7VzqP2waKgl_u-Vp8V-WvqqM4AWz0iMBtzpfRgOAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=UwR6rHn6Coud2uh4UxaQ-Xs4XQVlByf-9e1nace2ljd3T5BBN5L7Y2DgDeq-UOz356XDxWgG2WxzKIwZo3LeGW3nz3JEY7T3l3Cmj_OhihVBRWYqe6fHpSlbx1AUUZraR7kz3Wd6jJIFbr45_BrT9zF-T07XEI1Jk2oSgu_-PgcUX-FVcqTGbeaWYGnpA5v29XpKFhXB3YOIFUlDNj0mTWk7umJ4Q_IrkKF5Tfr49L3bE1npK7LwrQrEm8WSkqXDn8o5KqrPSJ2N8B35q9AVXGnR1yMlplO_WO6XOAS-yuhO7VzqP2waKgl_u-Vp8V-WvqqM4AWz0iMBtzpfRgOAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvVLSGLvKdaEn3wsBvQj-U2Qw8g4a417ItVRWs0fPKxEjmN70y_vp1WfAQPaS8-Go4DvA8ODd5EDWVj15rBNd1FuF9-lxq4JmbQwYrz9E6MYgzeAF0cQ9U7Xy-JTVsv8VbM6g5bOKIwUcLPSzNZ3EDfm_gpDx5x1t0FdJNLuh_8XvQ7SvB-1DYR6OOyfG0CYx7xidyno0wtn1F-KOLiUoSPhQn8nzqWI0K5Ha18nPCHthXjLeli0vm-1ev2ZCIYEg8q-ad27jEv4die0uLuifJC49JYNDDhVwvz85nmqM7k2ymF7lV95egnP0H5Mx7TG_-qVZ0F0bwRp2Fa9Go8FAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=id32hgkvqQXyOYMNduHDw_IBFwa6n4KgbgyTSYcFFL4_p73rBfhcYTaRGFzJTSatyph8Cn3UJxZCOCFwyzxTkJLvozgV5wel1zqb-9-RJwpzOsWoZ7eESLxlzhMSoVMXXxKls0uoMAVDUyFLhAlKSgwD7crm60_L_3xzH8yqtfpaKtIADMgQQoHPNQ83xrVOfPXfy76Qzqfb0L8bQwmFrKA8gp8YClUJ_ZIXlaSpFKRe4Jt58_xbGxmEuvQ7SJg4MSnP_lKUfQ30qHGVmuySDjnVjjOHEfk7-xmCTdydnOj5bqsTqDfJY2p9jPH7WqE5cHco6u-IZ93OdEtyzcHvtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=id32hgkvqQXyOYMNduHDw_IBFwa6n4KgbgyTSYcFFL4_p73rBfhcYTaRGFzJTSatyph8Cn3UJxZCOCFwyzxTkJLvozgV5wel1zqb-9-RJwpzOsWoZ7eESLxlzhMSoVMXXxKls0uoMAVDUyFLhAlKSgwD7crm60_L_3xzH8yqtfpaKtIADMgQQoHPNQ83xrVOfPXfy76Qzqfb0L8bQwmFrKA8gp8YClUJ_ZIXlaSpFKRe4Jt58_xbGxmEuvQ7SJg4MSnP_lKUfQ30qHGVmuySDjnVjjOHEfk7-xmCTdydnOj5bqsTqDfJY2p9jPH7WqE5cHco6u-IZ93OdEtyzcHvtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVdf18VHZo257uk8CgfWqsfiB54YaAu0tlkczCk6Cx2NhIHw4sM9qxHP09pvhgnUF6ShZ5s5rMULL-eUXP6lXcATAjWrDKa2AyidLgqDnL_gYZZu2P67ORPAsHejAs5VW0OkNX6aYLt82J2JERExBvh8HQne7gc8VczPTtBX-j2CP_e5XGpSkCI5e-c1ZN5M554XjDJL1x9UvSYN93waNeD4-Jdnny-oXPLrisCIou41GbRgZXYio2GreBFbNddf5Ow7jR3GG6mcEcJnNPFm0ODG-5M0IoyM1PsprFOPK8DbFeNIMbnHHmQdr7OV1_0WDeR2hWsd-D7jNKTFdvIkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NofLIuA26lsdEU1j7_3N-4CTmKbwskHbLQZ0m8a8umgFex0msjLXdp2emPykaQOa8nHhY-zg9AyOZNgDrSlT3fIQuPHtZUb9baVTA2wB5ffpQheP7Y0heWHXwDHdmY4TxHT3N_Y6wZimjiKGtvw9l6e47E0Ly_HJC-CxeAI2mRRoYZ4leXRhroieGQatVZP02PWF5v1ASkBW2QBYEtCSV4uzoOO9qp3Fhiz7wlCPqby3tnvHgN57ChaliZbhPUAzHsDxsI4JqpAYoDy2gCKr9kI5E7INOl3s-a00P7zMuC0GX74HnsB8uRnm-yPmXzPBGFrZGjRcygd7aliMC4Jvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP8xXI5oO4U9Api2m4tLguuYICCuke1YW-txNG8CfOHgt2JugyJJIi4-ZiyRzYYwQYZ8cNiA_AxHFwouHdzdpXF9R1ENbwYBdRL8014eaknTfxIiK2q_GmFROy1m0qw3RM2OUueKozBlOduRN5pQvNYykGGnCDXCbrQCdp4DO2sc2M1BdLw5t_4Zy2y08wReFwIrt9djC1XDAk93Sy-rVoAGnYjHYN8LfltkrInJ7in130XmOTeYQi7xaYsWA3MpsestR4xj31JJ_OZkt4r7fQwSKKWCJiwIRuWEHO2OD6yJ0xnEFMu7JgibKqNWI59BoA4Z7O7rNkUZ0ifwbITU1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H66NBePLROv3szVBSUBJJhVuOS0Anu9rol5gINFd--cpRpduczADTWxWpSbvnEBnAUDVFa4eBlOymMp-NSUfUYDJvF-7yrbl7kBVVvU2S2VQaVYiLFk4zOOzEtYovnMS-Fe0IXS3_966peKi7I1-Da7JED3LQHOnEQdKBIj4z-Nzj0K0NsYY4UEHZ_UCfpdAAFk7iUEQlY8Q7NtoE54DbXHNjZ3JqlimQ6L-fCdLRJH1KJlv3_bD28CsK5fIpetas2qYhrXmoG7zEQijNAI8d8tC4nej8iudINktn4i3sqKCm4WCP_-M_Xw0pjqq-8-IB9sLS5MxmNJC05t1KYGtxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBQfhQhCDU7g9U8lTRinAn2MR1BrKEWMgR5dib7-RS4LdW0_iTg6cvl8Uu0cjVqYn2Lg_LP8hac6e4-t7eKHG79fqQUe3Dor1b4YbPFhnCS4ovzfJSiQA1KyqMyUYWRqmIGDi9FPkvpAASaIO5S0j_nfYPu4-B62WtOq-adzCB4uIbaj74BtUBC7dOLLLGw2r2ZzncnzJmg-gdeTFxt21TF727oTKf1nAqYZ0NNzX9STfH1M8v3JJh8ktbAR8gaWbCD-lbHdoqWkclodEhEyvf96I-2nqLcvEChud8RgQDSPxlRwHakmesFmWinFZFo8MGbKkTGHxsVXifPTuhs1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=WHG91zK3K4QlJ7xtrkMr3NGltrMD2wv3iI6UonExFwQZGcVZtngYw3k7p1I1WNbvURIdZxvfo0RL8mtcwqd3iFXxxcnBdrwFYLYp4W3WezQ4r7Ud-JeovHRkHHjHk4MV1O-C3LzPjNO4fSZjeyK3SLIVrGJrPqi_DQujoI_PjHkCnfgUn5lRqe-rCzEj6DGeRBotgZFLSqYoqVB_O0isr4RRyHXexPbAqSZubqQa7Iyq8hrocSHSXlnQhF-FqzvzXgMI01hj27r0nsGN8K-IkWok9q_3Ncn39aYaJJHNq2Giu_muf7wWGby05AO2n3GVFI_WKX8JBQ1UKcDuTkoL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=WHG91zK3K4QlJ7xtrkMr3NGltrMD2wv3iI6UonExFwQZGcVZtngYw3k7p1I1WNbvURIdZxvfo0RL8mtcwqd3iFXxxcnBdrwFYLYp4W3WezQ4r7Ud-JeovHRkHHjHk4MV1O-C3LzPjNO4fSZjeyK3SLIVrGJrPqi_DQujoI_PjHkCnfgUn5lRqe-rCzEj6DGeRBotgZFLSqYoqVB_O0isr4RRyHXexPbAqSZubqQa7Iyq8hrocSHSXlnQhF-FqzvzXgMI01hj27r0nsGN8K-IkWok9q_3Ncn39aYaJJHNq2Giu_muf7wWGby05AO2n3GVFI_WKX8JBQ1UKcDuTkoL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=KeJUV96FtrzLRCbwqtcy26ieWqzPivtahU6he48ME_hivhRlLbjrYAbN5djhgIfN6BBhFzonXsx9LsdgehA-2zuVOorMx9pA8duNOV_gdIOr6tBWly8CafidtYnsg4xgEpUlHkKwibSkUehMY4wh1ZLpRFh-E0VKiETcL7sQEIRlF4lcvKOFkixQbwIMpuhsORK4_0zw2O16nbBu-wkwwrPY_K1L5AeEb1NYJMFcNHuU-gvx5l9k_3DPFK-Rj5bDJ0G9qb_OxmZL4ayjXuHEfI27COd8tENkb6E1k9j9lEl0Cvog_VjaeGEApHeZT1TevVf3fisJFriS3ofqQpWprg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=KeJUV96FtrzLRCbwqtcy26ieWqzPivtahU6he48ME_hivhRlLbjrYAbN5djhgIfN6BBhFzonXsx9LsdgehA-2zuVOorMx9pA8duNOV_gdIOr6tBWly8CafidtYnsg4xgEpUlHkKwibSkUehMY4wh1ZLpRFh-E0VKiETcL7sQEIRlF4lcvKOFkixQbwIMpuhsORK4_0zw2O16nbBu-wkwwrPY_K1L5AeEb1NYJMFcNHuU-gvx5l9k_3DPFK-Rj5bDJ0G9qb_OxmZL4ayjXuHEfI27COd8tENkb6E1k9j9lEl0Cvog_VjaeGEApHeZT1TevVf3fisJFriS3ofqQpWprg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jid9BYVPsfg-yD51qHSKGdsB0SfzJbGUzFaxkvii7D-qXYdLkLYm6zHn1r4PN9gHmEJRYY1YD8rk-OIx52jufutSwOJRvmVjYZ6Xev-FjJhSvB9UAZPy1Nolv9LL5bFNcaRHRhw__PpWSrYzhKexlgBdkpP63c2CRELA74O8InV_UD4WR2YQ7PLbLoH-3MA09s0boq73D-RpeuMTQdFGOMZxhl3Y77_XKE5Mj4j1TGogE0FSDwUMmb6kMKTsaKUR1YPMDR3m9xFyHi9DtpxBnSnP-NlIiv_oHRZaTAbgNF3gAy59__ejRCrPX8nlrSbDBlTZF-gZB_ku1vFXsRl8mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9LOm4EQrkcEZZNnXlRUZNX3MJdjT5j1ck7JPvLaAvSALDn1jmSCvazjElIpEIe68ILyjYx06XWSdW7o-fSeSPrQ6fsq4U9AXelRjqTxjxEFFnuTlvSsc2LR6curXCXn5zhgSL1BwgMEq47GhpIUOHpZHAX0Df4ZKzMsQFBrkPl_V1BftpQW5nI6OrTA9AP0kxaI_n2VCBGSwZyfZ9Ogvsx1ZUEnidC67sRTHZGL4uuYVZmxOrqDjoHt1uoY0tmT05X5K-pPJTP6WOl-1cXyF7ocK67bWFTqgJ_XRGHmbARJ6SxhbI5aQ3vjNxb7awAPGvpcelDY3VODwiRt_O2zdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8GONHC0detXysA0bMVJftkZ7fTWXEAM5h2624CUhUxmhJ4jUdSYhKF2bhgeaE-Wly5XJ7mPd0wT2XsDpxB1CE4pUAFxmav-rliibaoJ_ceA_mkbGzciyxHO_eSsihasVsY7KORCqyEUNY_FJJ22BZyxzPpuxllC5A4WT7Ni7t850981ex5x7GNi3JijqmFmwReNwyHqOVK1XxKZZxaWeAfD-Zshn9wf70W1wP0Mk-MWuVBjH8p0fiCwCpLDBIQQtOQxXb7OxpneGVlrQkfZ--RERiu4ivbBL9T2ueFuumhQuXgHq-p2183I31of5cNVXIJ0o_3m6GoUHDej0MjnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=g_v9QAt464pgRF8slKKo99VNRSMQxXrucSW8_HavzQIyKkR5eja-O4tza6pJyWKhUpC-W1y9NsguhIkmbIzT_5RvZdiHZbxS0X8okxkZyBugpb-EHwFHexzyrust5JnbizfpRxeXGTCyAyRg0HnOge9F44bQanrD1lKV0TM6LwrAW30-GJd0-iwy0FdmJI_TuT2tORhfvajhG1Ef_VrueTzAOpW4zgC_KjM26tjzBBz5u0YiHGlCSE9FJ1LvV-fV70RXF58_Qkj5_8MQajcLyQB3JGt4SaK8XvQeJ2NpEldH_VEv5bCBfxkScen61gtP8UCkR2180VlHohxo01IHyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=g_v9QAt464pgRF8slKKo99VNRSMQxXrucSW8_HavzQIyKkR5eja-O4tza6pJyWKhUpC-W1y9NsguhIkmbIzT_5RvZdiHZbxS0X8okxkZyBugpb-EHwFHexzyrust5JnbizfpRxeXGTCyAyRg0HnOge9F44bQanrD1lKV0TM6LwrAW30-GJd0-iwy0FdmJI_TuT2tORhfvajhG1Ef_VrueTzAOpW4zgC_KjM26tjzBBz5u0YiHGlCSE9FJ1LvV-fV70RXF58_Qkj5_8MQajcLyQB3JGt4SaK8XvQeJ2NpEldH_VEv5bCBfxkScen61gtP8UCkR2180VlHohxo01IHyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=WcqWWxnjjQhKtmJwyo2BmMy8w_Cv3sekAGk8OG5ZcDfF2x-fc6nzUdie-ixUSTRCoG_LokIjmj9lpw_tnInCRRdYFeMQf0A1xf90FW8nVGGM1kRNGCLqhiQYRQtIKd9B14uGfTbemJErhTn4mSMhc-75jbq7n8dM5ZixrQe5ligK84DsFXD8ioYXN37og_xrXgEXzQYch_pUYfClFru3aUMR4R2UEvbeODMu3hFZT-LVSNjAv9hMKS2IBTBNDtrbfmfBXxvLJ_jez2ycNQ-oqMHBQeGiQEvWLi5IN1j0fmdt_DdiyI004XEOEGjQRBqVBtTpzXrgyuYQnEqygJ5V4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=WcqWWxnjjQhKtmJwyo2BmMy8w_Cv3sekAGk8OG5ZcDfF2x-fc6nzUdie-ixUSTRCoG_LokIjmj9lpw_tnInCRRdYFeMQf0A1xf90FW8nVGGM1kRNGCLqhiQYRQtIKd9B14uGfTbemJErhTn4mSMhc-75jbq7n8dM5ZixrQe5ligK84DsFXD8ioYXN37og_xrXgEXzQYch_pUYfClFru3aUMR4R2UEvbeODMu3hFZT-LVSNjAv9hMKS2IBTBNDtrbfmfBXxvLJ_jez2ycNQ-oqMHBQeGiQEvWLi5IN1j0fmdt_DdiyI004XEOEGjQRBqVBtTpzXrgyuYQnEqygJ5V4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2yrrp_XJSci6lhzdggfbEKnxfLZH2t3O-7yvW2Tjg-czkwgJ5-4-gmdcnkHY6ppqMdhFlMF4lh29NO-TbjAVJq5QxxLNmOutPX5bdt5C5Ot3DVk3wtnRtJHdFxH0Aji184UAa0Mr2vW-X3Xmx3AAPcx8jI3mr-LtqpzLDO8y2-KWBYmsvaEQjqJdvpk33Wa-6PvyDMUTPKCVWzvY2kPn7medtQGAQSeaTJHkQCKU11H7vLr08QWFEztup6e9CODo_7FU_hfDLM4scuWAjYWAfe6_by6Xhl0JEBK0Vh8_RGdp2uofET_JOKFA-ABkc4jDoEIFyl8CrgHj2E-biMFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGT56e6yLxxzVJ3fzq7PiT7AJOnnbH4HRUkDrTSNP3LvwayhC_6J_DUQgQgy5Jx5m1vUAnAxpLgRVvNpo2q3F10Hj_ajiFXYRRJ1-k0CfHAdYh6gt4ki5mQXJmNWKFVehjRfO92vtzkBhNxPY34ulEsq7KK1U5y2ia4tfXCcU8Q9MtLdrGB0KujwzKg8_QrrGdp1Gy9raN3w5kZCydOpq1Jy1W9xtpA99KAqwaXcKmWeAequCZS_pVrx4ydMh5XxCSY1xT7RS92Kn-LMLVnmagzry7Gzscjdx_nL3GKU6sK2On_gQaRaPvGBpQkIPNsxWnES1lvFb8jpDc9zWFj_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM7ynBdu-v7uo9rM_Stx2dW33Ovb2ERB6vCjVozq89jNwcl-CfIuR-2XNXcaE4eCWZ8ZwsJSggesytkv-IKW2RqiyJsN90uX08B_d5tY6kmrPgFLm3N9sGLgLVRrwvP5S93llXj_tYqytACky7mvkyi--jLWx29XBhrJeFFNqq01cGKxHjRH8upOL0kTLx7wjbKT5vOEYDHVcNOMSF-bWLdUAvzhRimaacm6Mc-25xZNX3lR2-62FIG9pIBEiZ6A7SVdjick1nKR8sgUkbuEFbEx6oYZyVXOLCDpnZ6yg8SUfcYHKpzK6f1m-DZBnU1NKYyakudf1AlYvS0frSM1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNyQBPXhYnSI3SD221wkFIQrtqUVJ5etn75wxptAQRMbdyP20mOxsqDc54GM0mG0Nod7-esvQ_MnFNMrixRmZrVXZaGd7-NwydZ81A5z4pDUbD59BPxy0buOB6XUX5iKKjyqc9HoQhGyMqVlGvPWsQ2w8mmM0bomr7YiNK-hPDkOJguWWqkO0GMciv5iKtquQWCS7K3q8JyWvkacCkXXSvRhCva7NzCDngc4nNwXCUq2J3fiQxmAqT4Ig1ljGyXvw7323HPtNYIs1aLu08W6duihZmn5mxhFAr6gMrSj-3B4lkv6OhTMBGRuFUmKMvc0kgd9pIsdnxOkTI8UnNntwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceQVe9sdYtyVKNxGmHWmCNRLEsms1kOeWfgfhWo92qZChyBdhG4VTLx_vx0Z1avKSlHav7UzEgFoRTgcGPALg62y80XASdK_lTYQKN3y-v-RrS7rNpjk1WI0NHGn3_0T9C886U_8Pz829xDEQwvPe3-QASmE9Fhh8RobsrpUYKEj4t_8OWHT4hcGpb0Re7FPWS90GPXTKBkZLQKkzkwtAgTcquui6XvKzItpyMQ4to4CRoRVKT0_xkVzAmuCUMiE3KgVohj5bhljWrmGCI7e61xyiX6WB-tykiB8GdxKokAM8RfrNvO5cESXF5JxHd5DKqtmqpiUE0dZI-VDKmCyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGNIb8_7d1RIox6NOddt0yEBugE7-5lWsJWuWD0zK6NaSioySSfJygL15XQt5MgGa3L8PN5HuuHZAtTMtnGU2X-EQcjdFS9wmQqxqKNb4_4NIVwZGuxqXQ28hms5Ip7P_lWuFEeyyTFyLAHR8SNIr4Pd1jc7ajHHdqijdG3s4ozBZb2NHL7x3HtJmiVYx-tZrPWyNZd-XsrtzZzZSfvP0PbY6Tqf9zzBhtl5SWNyNUfXq0maFY8qJy3NSpimuhk7oAALLbOmXCpZcqz7rDQ43kOmsjFfRfSyi9MUgWmSE4omnik2dhwaSMQZtgGDCJZZj-qhKDpfbQt9tWl-G71o2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d94ESS0YmzBwaw06FjrrndBEU2v4YxtrPBE9gTnvuNWFjBIWFteYktqDIFwnsaV8lJJ-NaPwvoDlFJLR6pWHql0R2sPATCUZiV_ivJO_bl5QaJxzTGoOckwELVkEN0awBl6ITg8kzY59RtlD6T0Yg6h53sGhjKfuWx5ecLbiGIsE0K9gGw_P862IEH0R2ZhE609o2fj7_3ObWYxM-wnFrbeMkIe-syyKlAnoM_2AIJjQzolM_lUvPPgv_ReQ-dJPKwkFsA5nKj4uPt2-h1lSJBaKg4S9Pgcg7Go9xqFWqBXGFKbJDEYT1H0DJzwGbcP6lZTQLSGDfERCsVR_37l9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZc_BShmZm76v7P0svWzVGu_kidaJFpohOtiaDK9xQqCeisCeDq_PP-qn8sMVqgx1ohf64vxDdcddQXsBXy4JEj5C6jCEJ4natbsDLASjASGuYRijPZc25KG04y1o1dRKm2Lw_--U0_fQoe-BGPakPiw4YmfaeXtZJhcqrTuV_ff42-UgulMqmH8H7y1P6RAauyufDoIxmsf4_W813ruK0m9qXgj6GxL5SR-gAF7h734AuQED_xdJxtL6pbquaHIvtH-5d7y39RFV09p-xpUldSqiJ7H7FIRMAw7GnAviYUbm4KzzuK_MZQ1zWqftdxPU0jVG327a1qy-FgoPGNcBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHiYe1HiKHsMMVb114IqyDeqENPGurUfoyTCRw7jvGK7uyDj2ybuWuN8jhbatEAEUyE4-z9vuEXOR2n_UZ25o1vqsAk-VYdYGTYph6nGoMPGqUgn3bucneadnRg-kNC9nJMERnPms81BSkqnR3HFy-edxMbn9Dp6bVOiWFFX_qIlz8MVe-Kp8z2dQyoOmp_t_p5t1ECELKrYqIK7qT-creUffPK-gT81WWnI1AJ5AiHLCqU5Mgg-8UwMk0AYGy2mF3rjvrKkD5b4j0K85z-P6qhXPIM0TpO5Yksl2XsjeNvFKdoAaGlhLkVMQvbrcLvlp9fb2HqRGmDT_RU_GNmzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=C4Hj1MD_E20AzB6wrZn5NIKk1qCC1PoQ4CfCcCU0hWj642RBGdPpmw0GM8HbusJyrnJTK274kZJTe94m3j_TUAPRcB_FFSPgqQpnZt77_xZ_Vg8HLYZC-2NqaCGPlt_gpm7XQfL51pPEvI_KM-JbfjkzmzEQIxLdRWyV34Jfk4QIiAoHKMuzHbQ3pB-offQdklX9ZBQJgQoR0JlNPE0ylvZu9XGJOcM0II-VESZk211BU341nqNALR5JI4TsFR-q8Ede53kuyzQ2WJkXus9PUPfwfwdodfxb6Orpr-pDtn3tcZ2eEqE0XbUg3kNEo9wwSPwr4LpB9RM76jN8GR0X_oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=C4Hj1MD_E20AzB6wrZn5NIKk1qCC1PoQ4CfCcCU0hWj642RBGdPpmw0GM8HbusJyrnJTK274kZJTe94m3j_TUAPRcB_FFSPgqQpnZt77_xZ_Vg8HLYZC-2NqaCGPlt_gpm7XQfL51pPEvI_KM-JbfjkzmzEQIxLdRWyV34Jfk4QIiAoHKMuzHbQ3pB-offQdklX9ZBQJgQoR0JlNPE0ylvZu9XGJOcM0II-VESZk211BU341nqNALR5JI4TsFR-q8Ede53kuyzQ2WJkXus9PUPfwfwdodfxb6Orpr-pDtn3tcZ2eEqE0XbUg3kNEo9wwSPwr4LpB9RM76jN8GR0X_oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVkF8QigaBnSe6ONFOflD7_dLBunUQTpf7MvTiZcegIy8hUQyYmkxyn95F5P4tQjTPG9hB_7vFev1DyySO8B0AMd15qHvC1X94H2Y_uyKR5LdTVzNtuVwa4cSWnhUibW8BE0lSQl6oIktznMybVSk_YWahurXgvDCFw_pJx_Yu8fLlqrnJEgKmZgVTRx0HzLwt2efqhkZUANNjRdtHEYM7KcPZqlaI7vQYC0tAQPpqqljN-vkA8Arag0dDvGCFYptVHj0hyBSun2BKmK_L-_kngJYpFxrifVk4N_K1jo6MEp6wQBPtyK4D_LNPyZgH7JX7kXTFT85ULvW8j0W9_-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh4fxYncMrBXRJTu4Bt4aXhaB1YQ5D_yANEBRcLt4fb9Uvnnz2XvjwWN-egWPBzn1x1aL6aG90dnPXUiLx7YjlF40ACHAjpmq33aqa39-hvemlFzZII4QUJul2dFjVAsfgapTqD-mgh0PVsuY-umOgQ2kjCL7igY7FnFCcyQsi85RhZre2r0y7UuuaCag503l6kuBDn5QfViZQf7ktwc8FNKhrf4N40WRslBQfnyeUX79NK0mVFSVSfFOl-Sk9RqkoKpQCvp-3XbpXKowTfr3zxmqGYLLd82fMasYDuUiGnrd7n-Jl9QRpjdRVf875p99Y8knjE-JlqrSmq--Xypmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9n_H9w9dgrDCe-DR_XdxkfmPjuGHIPEtVV4umpsZ-nlVV1K2ZMvUuzz34TzfcvnBo4QiHYu5tBAQLRbg7x3VGMMd-2O0-xO6w9f6UXKppWGXgbEvWBSqfclPh43ksl0OzigrVOG_zeZEPtswVOoJI1a_wusXB0V63T7QAAd05I9JFL8w6Vnbec1jBRvYy756efd8HJA0XS_xi1263PayEAnuLIA_9NZGFVwGxTBowd3xfNFdvIiipR0NHP1biCRZZ5Dr5AhYHZ1lEWhoaek3UfwnFmHBJsW1dTqfYatgBydddzMHNKlIDpiss9nQMXSQML9lCvSedZE7kKDgS7vHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RupNtz_NQWb2dcaR6nxe9eCt2Gw7P1Vmm5H9nQOj0YxmAD6TSgPM7-ssZvu6eIGEsryK1KKUeBE1JDuZbL_bmiwH_bfCM-s5ACJMKVIVNOov-lWab7JoEXiihBsqnpGpL01UXTjMl7szAz-46tyzMFJeLrIz9WiSaqiLtEhzHMAxSnz2NpwTepiBRSUp24kQIJakN9qtuKKD0KchlEqOIJTAwRBlIIG-v7sBpj6Rj7qsWRDdjhtqj_rI4GNvbQgsVUIwac5cYwbfRpungtsAh1L-kVTK5HsILvLpECOxxrC7fAFMdjeKpzDQ4HMejLbs4tJhHMKHwxvep7raiwGTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLbbVwrhqxnWnw7QJvD5X8aw8d2po_fgj-Sh96DyQrYtzc2CcIsoHLKHTTx5jQhGXRFR7qWUtBTKXslBUp4ibJ_dRd_HYYIf5ECJR7dxN3oG08JMxZph9jYG8qUg3zteU0k_7fEXmt3PYbehjJL3CiAtmsRoBeIAfm-hj4-zlRu6Fn43pB0EORBmBKVepNdyf97C55LLJIyaBUUiFHzVGTmCviVRshbTBUuR3lscJeAlZPuzD0wWJDYGpK-TmwYCqBYzFrhMhdazEcU49UtUZJTUn7-CENgX0sFRnKk1jSJg03h1AsXoMrRt7nFfOXD6yW9jLFBTlVqCbyx7CMg5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeYaxqpmh7Q5Zutpecu43tsvd-iRpFNeZCDJFAC1E6KAUH41gqn2fB0QkzZwJCKIxf8YcpxXwLEeO7bUlNy_xOyuyzA4Y0FqeDeY4vRDPFuOUllwCRG38df6AWmQJ4yCou6nYo4wttNyOW165t0gdNfWIKM5Y4hXCUMQ7_VQtNmfXva4KlVoCnKU6hEmRBVXExOsqzGz3HF_zfojJinElSH4MNvsNA9AZGAioWAGTb1fl3621puVgSRF_Aib8vBRfhr3fczR95EzBn9qZcahpoOIEtDr1BbJ76nCh8AoGi8bueyyxL25ldY06R9ZbJue68eSnVgJp-m8CQ6BMwwiQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCDjfKETdvKvqF2NW_socXIw1kteEhzrKQyJCYI_PMqIgoniLKIm3J6C_RV35JMsq71_F9F_1hhun9bPFYfywG6GllXC_bwf4SOXe0wxQA08tA61tuL9_jV8YYrH4E3qanGtnUAGrOmuxFA_TzZ70o-E90emG8an2KD1MnRoCbW27stNLoA5_FyvohmOiSvTXzEBCDuuPqYFq5glS2IjX8h894_fELzI_GlysBowaE41AZ_nH6c3SXgbXoo13s4vBGWSCrWSURhMNVed43PxXb_SjbERrRnf55LS3rZ_Qm64KRHaYqmlwdJ9aYxVcup6T9hjJ3s6N7aEmsEBG-3lJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=Rn3rHEKLpkIQAk01CGkqePdsLinm9A63h1H1YD0KWEt-q6UySLQTF3l-LUfiNIs-0_fcFIMNIwGZL_T4QnFtZUjr-OkqO4oBP0lBWszqpm5GrGUVR-Gg9mRErpS9YYD9COg-uK1h4Iux01Hi9D2DtRHZYWLZ_huIVUHYIOnBoBjkgiIdT_ex6P1XCZoLwDVYV1Ys6_NOV_UXvf9uJ_13AYdJqlb0GpUC64XQymfnHnWSJ_zFJMn8lrjjJcOomwLc3fbaQcQZ9GIFtXbSQu9AWiaodiRfAFYhXrmfcU87BHo0CDsP4GkNqHO2zaANVVpfy84P4TJQ3m6n90xR8UKGgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=Rn3rHEKLpkIQAk01CGkqePdsLinm9A63h1H1YD0KWEt-q6UySLQTF3l-LUfiNIs-0_fcFIMNIwGZL_T4QnFtZUjr-OkqO4oBP0lBWszqpm5GrGUVR-Gg9mRErpS9YYD9COg-uK1h4Iux01Hi9D2DtRHZYWLZ_huIVUHYIOnBoBjkgiIdT_ex6P1XCZoLwDVYV1Ys6_NOV_UXvf9uJ_13AYdJqlb0GpUC64XQymfnHnWSJ_zFJMn8lrjjJcOomwLc3fbaQcQZ9GIFtXbSQu9AWiaodiRfAFYhXrmfcU87BHo0CDsP4GkNqHO2zaANVVpfy84P4TJQ3m6n90xR8UKGgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh0c25M3-Radw50LYIapFWxNMpqTXXZSXwymZHbsYwasy3eRgYZF3vyyGCIfHSwELSZn8w6Q7M_LOfdVJPkuw1kC75b5C3smSC76NgFWQVpG0w1DLbsofAW-osftXoYyg5I6loGTFMMggdEs_VbsGhxDrQzCcbcclHXethxiFAjH7Q9yPbh-DIQkTIPLHzLgWd7VM19e59Z7J6jJ8eGQl_pI33ao3Z_AJ_wAz6u17iTwCVNdtPxP_SETNEveojq5ID5a02tSOwtt6jtBSB_-cP6Jeny4kGUCKCAuup5ZQ5SXxzy4hYaHR4UhJtjOq4LFJIZTMYpGcaKpRja3I_t2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDt-aZCg9jIZ4IlAMzGReWMM3ChLFbbq4U67pPpkEk0X_aOzLQIqhQFc4dvo3tL3tXvjM9VHsrsTDsZ-OwFrBFcYfOVzJUwLaWpymJUtSJGcUYtP2hy8-7ZPXFLXzFJjrPYGI9oVkGdZ4QYVFsKJyNmUO4Y1w1I4H8l4kVYjwK2vY9PcAQLhdC16epUaC5hlQQyW8WGzR44W6CRuc5v6sfZkuElW-95-dT6MVZjNzChTREI3DFTOcl4Y5AETtaFtKhSpmW8Yv1iuGVoTwTf1mE0I7ijngs3leGHH6SBejW6MyvV6R1z6YGp_MbQeOV5zMkaz1gPR2UhTbHyGsRMYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyXp3NH01ldhIrEqqBPe2a1UHlzdO_vN5nEK0irltoN5H0ztt2hnHNwFvOYDE6ezlfgrv2eFRXBbYCCnJffjc1eBWgBYv05JBF4K7m-E6P5xxePv8NhamJaZicWiPSly4c2hwj-jb_HVewOpap-3jtBHtzkvffumEaOXXbwrxi72hVtxVt6x50i4nnXpObux9-SMb9tzatb0GH0RIyG-pm5z1qQmmN5H6FZb6jm6_jMzgsopyW9uhVI0a6VwBNNqn_XvUdhlMJeN-JJ104P1KljhtBzvDsQWJ62lj4H6WpA5GynAoNTtG3JWtRMUGkckIheRLe0Q3oj9QNag3jOrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=cUNwsRE0kO2sv1VQ605ad0NjkQSa-nhvTahcmeipKk2unDmgv5EQJO_2Jk47uetDSIdndg_TlrHJBL44UlW5g3RAKizgnQEdcEtsbF-rJvtSZvfqOlcbFFVm2oGJCd3sv3udrP3Yf6r9xUVz5djAe5slVEUamJpbARDTPBxaj9NIg9H2qO4y_flUJbillNKx3f8CgCza_dJ6bcCPTbbYQ0eI_cl0Dxb8CP8tIUrg9nilreWJUmWFEV80ta_x_wyz0_cK3TV29Z_8e7ZXox-CxpnmgmD13r4tPI7PvWbTyeeXBjj2jMsGTb8W_GU5owIhw8-dItMMsPgYbzAzxAfrBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=cUNwsRE0kO2sv1VQ605ad0NjkQSa-nhvTahcmeipKk2unDmgv5EQJO_2Jk47uetDSIdndg_TlrHJBL44UlW5g3RAKizgnQEdcEtsbF-rJvtSZvfqOlcbFFVm2oGJCd3sv3udrP3Yf6r9xUVz5djAe5slVEUamJpbARDTPBxaj9NIg9H2qO4y_flUJbillNKx3f8CgCza_dJ6bcCPTbbYQ0eI_cl0Dxb8CP8tIUrg9nilreWJUmWFEV80ta_x_wyz0_cK3TV29Z_8e7ZXox-CxpnmgmD13r4tPI7PvWbTyeeXBjj2jMsGTb8W_GU5owIhw8-dItMMsPgYbzAzxAfrBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4uyJGh_lhTzQsw6hiXG-BEdWSZix3fSnkm8RyPGyQW2UAhe_J6jczVnoCYt5iTK5asKHvMCpKdmtYIMjFZ-OESpAaW5bwivoFiKjfytLS1qkm5Cy6qTH2iVigD_ScifWhepzAjocB-uciBALd7g08OuKGYOxI8KNtmtvVD1oQvEuy3ZoPS73cKTwWzAnhoWitCEUBHkreFsJb9XmjOdvrqEJaaH5XHwzf4KGTcbmmU0knI8r__zu4HXCB94ambk-L4Riv_LR3i6zz3NBCgeXIVu9AdmTfBjKGuCGBHkU3w7iVdmt5LbsZalDtZksaAmhZDsd39_BXjX9m-0g-HoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXfwLeKr8aw_R9DTSkA_0oSS1HZWv5-h6AoVVjcbf-DRMbvuNNzAzEOqXYGs4wplC4DN6_EQP5ttrJ0tRINP2T-yN6ZuWKJowuQXIxeQvDPcS8gjrSSz_mvmOe9I33_O8ZarOX4WeFuvYc2S917mtxaAyx3GcUWt6udmiht9FAcJxWMuzSYVF5SD-OB8naUFarbTgrbxPo2YY_AY9AajoOU1rGohFSUJifFzaeaNdHFphgyB5NOOutWUr1ZS7d3nQqKrtURSEUDhnpM4O4Y0oS_yiVlzvAoLKklsp7ugxJUjQ8Dl1ml7qt2m5xVG51uoQFsP2gfcb-SLK4wrlWQvtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=cET1yekwLOivKVK661HA5j_yh68ZZfxS8S349wUWMbkPA27e8acT1Br26k0Gb1224X7HhzreFHZ37Wa0-iU7J9fsTtcUn7IhMhW8OceWsdzmWglPfPTEpvJcOQH_ct-R0woLQz_rmJpZikMDfSHUPcGh_aRcV_-8ux7yZiBUNsMnV3OB7hpklkt4ozGmS-owq0DOdrMLZ59wY8e0mmGH3HSiuj1_Xftcf8HExMtiXBDTIdX-XtRcgiUGCmahz0wjr9RKoxaB1TIlZgumnpo7N-z7j9yDGctO70glBG4HFL6VqPbNXcz5OG0F4qRBmhRzsxjBsnOrE5p0_YawKvzXaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=cET1yekwLOivKVK661HA5j_yh68ZZfxS8S349wUWMbkPA27e8acT1Br26k0Gb1224X7HhzreFHZ37Wa0-iU7J9fsTtcUn7IhMhW8OceWsdzmWglPfPTEpvJcOQH_ct-R0woLQz_rmJpZikMDfSHUPcGh_aRcV_-8ux7yZiBUNsMnV3OB7hpklkt4ozGmS-owq0DOdrMLZ59wY8e0mmGH3HSiuj1_Xftcf8HExMtiXBDTIdX-XtRcgiUGCmahz0wjr9RKoxaB1TIlZgumnpo7N-z7j9yDGctO70glBG4HFL6VqPbNXcz5OG0F4qRBmhRzsxjBsnOrE5p0_YawKvzXaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=R_aA1W4roGzn7y8OJc_RotFaYzTgAYmGcs-UZ_Aghva2NXNeviMf_FHpOSEfJTz3Ml-w0ZV1wb6017VbeJ9gHSqDGC7zQhREvp204DldTcM5BkkmNrqECwkllIrZHkpA4brKhicmuu0cdUx_ZYQ6-vILsHaF4igCEnSNtym684ncw_uTu0fZW0JC69aJgDOTLJWuMYkQ-cs26Sts48d_8NBtXrHfY0Ln_K9otOFvCnxVhVj3oufQQTO9m8d-X7Eh6jTweX21I3ByK1X5aI9xJtsLZvOfiOiF5feWuDhuiBYhBwp1Bf1u8yfPWLwMdca9IylZxU4QJPUn1tg9eIALQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=R_aA1W4roGzn7y8OJc_RotFaYzTgAYmGcs-UZ_Aghva2NXNeviMf_FHpOSEfJTz3Ml-w0ZV1wb6017VbeJ9gHSqDGC7zQhREvp204DldTcM5BkkmNrqECwkllIrZHkpA4brKhicmuu0cdUx_ZYQ6-vILsHaF4igCEnSNtym684ncw_uTu0fZW0JC69aJgDOTLJWuMYkQ-cs26Sts48d_8NBtXrHfY0Ln_K9otOFvCnxVhVj3oufQQTO9m8d-X7Eh6jTweX21I3ByK1X5aI9xJtsLZvOfiOiF5feWuDhuiBYhBwp1Bf1u8yfPWLwMdca9IylZxU4QJPUn1tg9eIALQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=sWqzLgPzf1K6IETMBoV30V34__7oicTJy89ne-SHIwrvEpaTbZBSxLC2I-URPJtbGv_UVtBzkkgxfRc92DKfav_Ac3Hpk-ZBsgFtfpiH-yeAfOZYLjun-U26EnJ3uxhQAX_TsE7lqAFD49augBJDy_OJ2yZU-mnEYwgCPV7qECiyiNX9nNOD3Re4ikQWiNQRuqU5UddTtFAmsU-3-I6rJTD98NinwUbZ-EbOczspR7e6acvkA0gE4CjsIofVAI9uKPxCZRtuqURxeDcMBJwjMBb4j4nYQEKebDkQphRBqMSUUsKJubjP7XJnuVOzJWnVHXQGcg1_0gpipOvolDI_wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=sWqzLgPzf1K6IETMBoV30V34__7oicTJy89ne-SHIwrvEpaTbZBSxLC2I-URPJtbGv_UVtBzkkgxfRc92DKfav_Ac3Hpk-ZBsgFtfpiH-yeAfOZYLjun-U26EnJ3uxhQAX_TsE7lqAFD49augBJDy_OJ2yZU-mnEYwgCPV7qECiyiNX9nNOD3Re4ikQWiNQRuqU5UddTtFAmsU-3-I6rJTD98NinwUbZ-EbOczspR7e6acvkA0gE4CjsIofVAI9uKPxCZRtuqURxeDcMBJwjMBb4j4nYQEKebDkQphRBqMSUUsKJubjP7XJnuVOzJWnVHXQGcg1_0gpipOvolDI_wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip3vdjgF01XkilW2ULqXGOnUWOYugjQZAXPQ_4YdSo4MeeJAQpkLdeWactbIuCcyjQgAEnVk2bnJG0fZRjQflsueTGaSS12QxTeyLc1Z6zZygjW3N9-N9hs7WeBCpupQbYlAT6LK7G_y7CSB8n7fIaUrh6q-SYMKMepqkgLfYf0M68FOKegx7U-r2tQKoVRuPHccEDFYW8RT8bt3NEC9K9X-P6-iusmYmrUTSOPVunQHQ-wBuAW53uN8a-hCz8ZR4nIX8TCtNbqcABB7xCNgdIL317hg0lE0Gq7XHIXBHMCsdCuNfS11D04Q0qYFGwhQS4b4taJBrOlxUvLaKsxVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD_WuvMCnBOokoDqOqtTsZluTHMSijr0Y2Dbxl6A_PtHrXpuNCpkcXs6G5Pra6ybBgwDSa18lDGwonONp_9aZUL0tDZ4xKDHpxlkAiLFaVVHOVK61wwBa05J_vkZZEYgcBPH1y-AzZOgFYd1fKZ9WScrQXuxxp3Iwl0c-H-1u35OJrViVIYkDad_EsaTiRuGiyKgPXiRrwTP_yLCWUvuY1VU2v97eNlIrn5cU8rKY7BtaBhozor7vceyAL37x190nElj0bDB5TVx7ZilIZ1w1hQ7aCs_VZAAgf-IRgYhVOx4ggZRGFeEyllRrYQDBbhwTH1v0yniALQy3GcAijs-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogBiUmaYZrfdG_7tQmJEZtwpu-Fcv3wK-s5L202HagniIwlC-us_GBXDSM3BpHhL1pqR8o5C5SGtfUEXluPiC57Ri6Wc4l4U1sURn2erQe-RkjIaI62rL6nALd9kNhSa2a0nYIcvJp3MlA30zdqoBsNlZJUd_TAlXhhm0diLjV5Y8CwTstqCaieISM4Z1AYQTSOkW3bnFV-w43b42lRDvc7W6fqC1ljH9WOtDGAGjtvlm61w0U42B7A7E55vt-jqSnqC3I3PbYLk6SshMbyNJ8ONVP2YFlO0E8HCrsE0kWgi2vvBArGSpND9d9LzJx4GwVOl9wY5PMGGStpcATNnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNcVfsN0703Zn7JY1dSce388kh4Qgo46n6QHJqWP73f8UHIORdDYOFWlOQ9IOCA_wxgKbGswpBYUU8LD-JP_SG8hbL4X5JelMghXmpKKnCTGVPclLf28h1obtsUSB1xJXvYb8AnOrUY2J03kFzBF2lm5lb1rL_HaRCElFTA2Kbi-ftke_SlXBHXt53AQcMwVCqXQLYCrc7mVotMI5d7kk4dv4JhhivzURdFmnzFnnLdPjcBAE1l3aPhfX0EQEhQZtd2v2UBapdSSHXT1NEKJKfDzHhXvZuF_Xox2JsVqrcqoF244yqeN6nrVi7GdtIfJz5LVjTOGPfg8LVdmQlMdyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnvK74Orc0DJh4ZrMzwEWcffC5-xoF-vVBmmK6k4SjyqLBfgV-2cjsnVQtdlIsk5WqFJL3FomhtsbgmwwpbkmclicixTdJpamcKza2GD9fPwedxkvLk8p-orHpxsGxWAoGUoB2-O1CRwy309pT3LOurWFLZzY_CNBRHwkB-aSJKHbYq5QjQbggfbAIzEi7yKBvnLLqGxj_gZ-RK01Bv6ovypb4Mx-9fY2TLdVg-IXXGGmF4QVNyPs3tOCnPCZZF77H0OIixTPsTZ2_lk4MT8IVXtPWk_YntFn__Of7m5yiOJqds3LGzVYJA-hU3QUXQyy58QsoZOo1-Ik6ogAowVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
