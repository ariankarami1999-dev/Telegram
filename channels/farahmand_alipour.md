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
<img src="https://cdn4.telesco.pe/file/e_HEvnAEExaXscQgJ8l8wt6qkUSEHf595rmZJe6hS6orvLYqj_ovfVxl3A_5Bebcx6IQiGTgoh3SfYlRM7YnDAEB7Tw7S-oxZ3duJLW18Alig347leUr0ehbUgwFVHK_4ttReq3fHmZIr9CGexxslHlEPJ7CdVpYdH8iO1cmYUceDbx4uxOTN72vHGe9O_C_ZwSCp2qr7EddfEakbciwmwZg08cHoVzNMyw8nRHmEmLmPf8zwRGz4bQ4HEgG_RQjY7YKUkkf84e4b85f2k7E5nptVHKbAqJGbkkwrfVaTV7Yv_aQ7uGr1d2qFdT6x09K_bnzGWFZB73wHuJNjwCD5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 23:41:30</div>
<hr>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwVUujG8YpvY2xw_u29lAFJHNetDrpywP40Fib80dP9GbxYO2WtUfB2FDcLzVtAUiCevqFGZDxt0RlhsY-bqZ7UooTe7NOiWFE7g0S14c_jJt2agcg7YNOrN6y73D6dzc5PyIEU2D3DTlgAcp-5tiqsStXZWUxHB5R5txK-_0gt76yaBi8E9Q-alkdxU8iQ7dFqVezqCzIaSMDL-cDiisA_whbECQxjSPZGMAYeffP0RkzCdQ6aOiMX0AUT7tmPlgCYOe1yIiJ9oER2cl2fdGrNgMYpxN3rAIgl1i4WcwNF0JKtdBUouk222CNuuwwtL5dXSS06zZX6dim6nuPs_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=l66MeQlTfF7Uls9s3FVLKBRQYG8Gqdhy6WaGM_4QHpUSn9bWc9Ojgb4Nth3ORy7JDd8OQT7ewxOKRAHtRaJf0iRso5tn2hLXiXd3oLhFJZHtozJs9rh3Q4OaKVLEcc77s-efyt_42acc6qB1cXIRsEUAiWDMoH5UAUlk_kHDp1xYad6QsGq78pnfUez1e-VFIDS1K0Dr5ZpGVpuyHZZSArrdWoVH6ZzBfCoNlEIldQhVD4nlPE8_ERBqGckUxg-8cqPOCCdBNpJSezTfrLFEpUr3WayVjUjkjghWDM8y30tqPe6lWpifBjQkmKHSYC0ppnNO1gApTAlCgfTAzcRsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=l66MeQlTfF7Uls9s3FVLKBRQYG8Gqdhy6WaGM_4QHpUSn9bWc9Ojgb4Nth3ORy7JDd8OQT7ewxOKRAHtRaJf0iRso5tn2hLXiXd3oLhFJZHtozJs9rh3Q4OaKVLEcc77s-efyt_42acc6qB1cXIRsEUAiWDMoH5UAUlk_kHDp1xYad6QsGq78pnfUez1e-VFIDS1K0Dr5ZpGVpuyHZZSArrdWoVH6ZzBfCoNlEIldQhVD4nlPE8_ERBqGckUxg-8cqPOCCdBNpJSezTfrLFEpUr3WayVjUjkjghWDM8y30tqPe6lWpifBjQkmKHSYC0ppnNO1gApTAlCgfTAzcRsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sdlsk60IUZsEmhETLQHpLsCnhiXMGnd5KGFXpCHZ7kCLRA0ZlitGV-mUiq58LjyjBLPY1VbhBQ9iuvbFHi5Hs2IojTRz9LNMtmbKM371a2deh1joA_BhzWYYK_BJGrDiM8o_Rw9hoxvtOWkjbPW6YbFo4DRCDbTuMvqA-AsnadpmQgD7C6fOdFx6wIsRp4TerFH2nKM-fyCCiDPH16nKy0XCNe5cCSUnXXLwfGWuWGbS26PpkwIVNi6cAF5TVKSq83phKbUlJeTXD0NwkQhYRe0r_R5ZUvwMGbuCczZP4JCEktTkbwPfIugB_FNJkclmv0j6IPlnlDwgy5L-4Z-kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHmhyM7d5LValNrniV7d5cdnvSBpEAwTk_t8Frk0zKcm63AznpuxJukUmwTckjuNvXNXRDs-vGXXpgvkoFJzMX-34K8uQGVxsuPAJFuF_fFM-6eIfX6IU98mlabZTsNg22nocfu3njXEBZHFxUnSP_TgXcGuWiSv8AmRGsIGpJALQaUCnvYgT-mIlZqdmj2IDc4voW8JhwSqQCRnT8yHxxOh5l_8Q16XP9k4pMYbmnTKJ-KVMfkT0HO1T9oXPUmIRZYcH4Qs7O2bBaN6Jy9cf-FtKUPxqXpbr6AEe-WWrZNxXaZuG5-KLVZuhSQgOOuNbMJr8bLGu2CqoghtoVY1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=uJVSEGpo9nL0aYNCV1zA3nAHOGGHphu-dnea3Ja0oDdSFAj-XdiR_F9YJCZOWFgowPeRXf60dx65j3vghFato-0PBdUBETJrAlmp18EJKOq9w9J-oMY-YibkHuMC5jmcZPALHbc-5dOHd4kgZeqT0TwR8risfvCDipOqekNPD5-fKymBHaTX7KqkxJNXML8Ju5vJ2pAeqUHm_i8btTbIjY7A3p7jYrBJwmrjT1jomWGR-CuSVzIK40X1iP9JG_V49vuUVKPzpehrveAHysQGQtk0iNdGEGsW9I-49NRuY2Ajnv773gl0_22OD7hLtyZ5AB7OqOF_T9zi_2F0R-hbRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=uJVSEGpo9nL0aYNCV1zA3nAHOGGHphu-dnea3Ja0oDdSFAj-XdiR_F9YJCZOWFgowPeRXf60dx65j3vghFato-0PBdUBETJrAlmp18EJKOq9w9J-oMY-YibkHuMC5jmcZPALHbc-5dOHd4kgZeqT0TwR8risfvCDipOqekNPD5-fKymBHaTX7KqkxJNXML8Ju5vJ2pAeqUHm_i8btTbIjY7A3p7jYrBJwmrjT1jomWGR-CuSVzIK40X1iP9JG_V49vuUVKPzpehrveAHysQGQtk0iNdGEGsW9I-49NRuY2Ajnv773gl0_22OD7hLtyZ5AB7OqOF_T9zi_2F0R-hbRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ١٢٠٢ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fn1D2zQ3bDWqN89vbi6BiN-ZTLXDlU57kXKgSDtv053_snxK2G9fHybYoTQKRGXtmCyt2vudueQjnlBn66PI2QkTOsTf3dXa9D48sJ952eEEVg-Gjan-e9k7uWXk-mUTCn-TGBnEuL3CLfGOoaiIpEBDYpvaY9-0Y_LpuNhPgzuojThQuWz-PHh5IcrB5nOMeZzyJ5OqvFRdW_Xwz4z7N0BgcbN7JZLsiCDZHxLI9N8ag6awXCpf_XWcxhG69U4JOuQ_bVq9Ehpcaj9KUpYkcswUsg6-AUD3HK9dKK4uHL1TLPFeGx_UtRSfKl1JU5cNDFwPEyyNSJSQS5sRKNQ3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ١٢٠٢ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHm6bfGuK86gye662jvLe3GJumX8elgbdfwbG9CFnjUZJXtYP8AzbOD5eshPU8Rb3i3fXR04QAuzznEi7zhpodKPgW1FKqJA0FnAFm-9zdivVbJ0EZe7qYO94z092tcy3BD5kQzo3CRzrQzIl15j3NOPRhmfArhPNFe7qgkgZxie6mB72frP0v9uL19VqepqSQETn1pz5qPSCqXMZ6F0S6x1bL8mFShHnR4SMNSZ2ndVFaJhdiRTseE93o_FMZy4HqtX0u673bJgmPpi2WzDENJtxgjb28tPVJPK5Yvj3L77P57iOavbVUTBD_8hCi0nGxLUBT7ZZqqBEOWMGyS8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHMFFHMh2vfBe1zauUgJI96dfdW_Trwayjr42VE78wd5LnUJ-eVcc04vLwR1H3YoEtInFe-KsNB-agomIb4QEcpiXmn3US0RycVwvW86LSYkMJ6rZTtW-URwnEDAbF05z0S3APEbg0zP4t5j9ctXsqQC4A6GYEgxTpF4B-7g-A05_AIsS5gN53qjsYcaLdDqFhTbUqLvy5gNypxVSuI9EDX2YpZeTe2Avg47UHlWdaE6EeZwLfIWpUJpfj6dIG0fehUF1U98t5VoCuHcx1jfSk8RJAV2_8fPC9XFgKh2mTVQYXVDlHmewaZpH8s-Sbw6Fu92XVgFIERJyuZjzxjEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=tOP_lKKY_Dc4QoHSFRtx2BKrXQt3zVyLL2keswccMQ6wfK7r-nuX2IY1pYAwavdXVMUyDD0Hu_KpM0OydintGQAw4xHPdz61ETqhbtAzCPig_h8FgFUiC_i1jtUoaqs1IJosEuGQhkNQzZeIO0LpQerhp2XS8gz7AHMYzf-2PuGeiz9u-usPIPXxo_cKeGu5nAxApVcTJFr7vymcEN96AdRzXqNnvMTIUwSl7nS64GkIRW675Tzv12azY9dJc4X32JPegr1FqJf5JXWcyWF1UkSwaICrCe22YkEBo-2o42ZWv8ML5E1fJH1IxBxuTQ5VEGPSQR78EBFT-IUxx_Q3kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=tOP_lKKY_Dc4QoHSFRtx2BKrXQt3zVyLL2keswccMQ6wfK7r-nuX2IY1pYAwavdXVMUyDD0Hu_KpM0OydintGQAw4xHPdz61ETqhbtAzCPig_h8FgFUiC_i1jtUoaqs1IJosEuGQhkNQzZeIO0LpQerhp2XS8gz7AHMYzf-2PuGeiz9u-usPIPXxo_cKeGu5nAxApVcTJFr7vymcEN96AdRzXqNnvMTIUwSl7nS64GkIRW675Tzv12azY9dJc4X32JPegr1FqJf5JXWcyWF1UkSwaICrCe22YkEBo-2o42ZWv8ML5E1fJH1IxBxuTQ5VEGPSQR78EBFT-IUxx_Q3kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYEZqP5Gcf16dplyHgzrQgHy-GsiHfiGH-voHd5Tk9_dBLxdprBYYNK3Q7_Ry6GM8jqoJSQzaI0Q_HjUyt5K0o0FPrMUsYqOJkP1eNzI8e4OZq5TJUNCCUMU4iN89DfAt2HwEeDieBQoEEl-X0Dc08-gWrOX3M_g6bz-WnJrWaRZpLin80YHKz2PR-_SlOYOWKV0wejU5ZyHeRDwyl5S-yNO1lgoso733fTzkzurdZkhlVKW7nqhxM99HUO9npbI1fhp8HG5lD0nB_Uc6ziui2tw-Wnp7h5h2G-sQGEEG92Na7YpMvbBToyV8fVxn0h8uyHKdKu2jJis48qmCVktVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voyohXhAQ0yVjg8GWJ2Pdd4PZPgk4hXI1VM1ev-kfsxjYPEZ88Njk-B4VOyjz8VrGSK7LIyS5mk3HZfJm1lOttoSqp2JIdtHZSsshW1yw0eGPJjv8lFO88bt_fy5XDcAlQlJ-L-hyhw0ewB-GignzGHCBuZv9jSxcm9ARtgEWxk3nj4PENyHIOQPS2TGuZIQZPCJO4scAHjxGQ5xxer3X9MJ82tHEmMDKubW09vHJ-LyJgQHWbm-UXLVTZOse8S2Y9a3DYk-V10gFJRysOKI-AgMakXI-zxJX3LhHcIWX0rhDUtPYgm3Vhepyef0tPUefxJEmsa7a5HWeqgHsbBN_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmRlx8CuCWhSo2gKfL4n83gOV4iAeIYCrofkmvEsm8tkPJQMRqlmZ3N5Ch2zg09MI1EPCobtGEkqk57W7PyfbfFQ593UdeNUC8y42WblZ8kPtRlgF14nR2prLY4YPwpK48R4mqPyGXg3eBP9tZuqFgcfKSim84Vw4Js-rM74doi6QkE_98rgw9YPewXbZw3tfS7jniHtC5UkH8EKFrivSo8Jh0mYzuudb-8so4sKNCjiyyZvqbqxNIOGHQadc-DKmNLeOzaxVlkNvYUMJNr-UH4COpUE0vKu-ecL9BfwsrRMeNt9px5Aoj7DLk5WUEynw7MWVPdyft0hk0xbALKHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO5VrXX7C3z5N0u_fN3enTpNASWtU9AWqxMSHw-ZmErLGxziG_Pg_MCVMAI8SalwUclh8HNxtTN8Woqhsuopf0662369iTh3c0i-aCL3jH9dSbLCmeQ6OSG84Syhc0kp4pPqHvVpZ369FFQCGlOu3o1eeT7raQ-lrNO7Nao9rw7JtEnlS_Stloq_fgEjeI_czZlalOtDfYXC3Pi42gEXaEycev1yiSPveVBLdEf3IIScOw6XtrQjCyIlse5omeJYoohUBvUrEW3gfwpnoLh0nNk23-PrZcswY1Jk8mVUHb0jEj78iMhWTwrj8mRvroGur6dFBQzvhSiS6odwZAJlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol6nTZAlnv9NFJmERzlOLmHb_pfC1kfRyA8DWvHp_HaB5Sjg48xdn4ZEocSg3oNB3QbQpzMy2R5iiLGFcobdl-CRX7c7udwZg-VklN9TSA5ZrGvr3jZurTKW1-4FPJV2pnseOt3DDGqT3BMqlsjrY8YU2iP_iQrau-x7xKBRHVE_ET4a700WYSZOqkR8Te94LjMwYNt2EsoacqVJrt8S3eT6TyUJcnUo3P83YV7NBYcbCFoiQFYaEvcxDSsuFwnqrKZnt4iusE4jUhscw9byD7dMaFmcwTp8SEfoWGChsbL-Q4yZLa80rBe64pVkwiCdS1ZinhOBO_h6hDXqTEm2qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfRtofLraX0VDXQ7OZGQkTAF5_S0V44ZGvwlkTjvEU61zp-SVVvVcEgl0wxMKsrX22RZZA_8HSyBYsF_opjvLW9gZDfM6JlbqNqaA7eKx3qTPigOVNfZsugcHJBdeKPtJScz9WWYAJF5NfRR15eqfNVEz--6bF9EQAPrmZKv1AtC0A5a-avnkL7qYD8eXLsZADMZ9KjOvSE2ojz6wKwVfOWwmh3eaoGzlu2JWYgCTCBt_K-ulIyNJSpg8uJyzxSXEC2329536yMb9YRxcBkYYxOy_yxGHH0iqWnBX7zQgMyoXXnaXYj-Zm8T0olaEgz7oKn-fdSrGeCmTIvcbRiqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZPiDNfT-LMZDMO2L2_dsGm1kB1VQlpudMlGJdA9qMd8mecVNATiw0hjAvtyxS4XJImfko-YTkBFkekpgKKM3QA5v1etFnPhl67WwcxtZHGq0UNV4kCG7N_XLg5ILQh7LBdd_umkDeZCGs8s2A8OdbXcb82iYWipFIApUqXauJJ-C_2505wRMAocFWBRKYqD-NMD0UT3uTPj0LR3M0vylkYgXoewagjANa3d-qKEQwb0paaABVJnhO8DlMp45__T4gcBTmQ3LQqf7ov-zM5nZTnOaaqTAO1V5qYGFaoqftYwNZsraMraLXGsKb2ClTDI5yYYDSTDLrcIMEx7sdoenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=eZeRA-CqRxfVmonogOFwx1Kyoys02Xw6zcLBJJ3W2RnrlvmoS6Mlf_xaCgQE1jCOcxRVGBREIg18-a_b0CIWGZyblR2EEKNkwaSBGUwr8dhjDw2XUNB8arPizJXG9UajhiIfk-neea8N9Sx1x2ibKjkPjvM4ikAjx9q3-mW7DJWWCSIr2S-yOB76JTKHo_L_WZPPfTTDNaWuaPvKo0KNk2Ago1Z0UI04l7K6m99bfN7wSjsVS1pPZc5c_Cc6dIkytVGNyJYibGsw35u4pzAPa629V2WXgz09HoWmZ08j5O1wMDdkyPTHfBHmVJX1jYe-tDlkXoPUxDPsItVDzTVMyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=eZeRA-CqRxfVmonogOFwx1Kyoys02Xw6zcLBJJ3W2RnrlvmoS6Mlf_xaCgQE1jCOcxRVGBREIg18-a_b0CIWGZyblR2EEKNkwaSBGUwr8dhjDw2XUNB8arPizJXG9UajhiIfk-neea8N9Sx1x2ibKjkPjvM4ikAjx9q3-mW7DJWWCSIr2S-yOB76JTKHo_L_WZPPfTTDNaWuaPvKo0KNk2Ago1Z0UI04l7K6m99bfN7wSjsVS1pPZc5c_Cc6dIkytVGNyJYibGsw35u4pzAPa629V2WXgz09HoWmZ08j5O1wMDdkyPTHfBHmVJX1jYe-tDlkXoPUxDPsItVDzTVMyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=tBc06JTqKsS2vOKLKCZMXh3cJgS-HeOOlPTFutOtvGICYJyD_QLBqcQQrP5V2EVmcruZ6x_5V-I8Idzcvb7qtqqkaNF9p8PIQw366exwLs5OBgNHjbOjQG1WcYM7IbEPiRBc11ndfkhSTFfTykl9OXZY0hHRDf6kOHmsaSTMCzwY42OL1L6eY9slZijx70AvAT8RutuaAuookVNGYgy5CzKyxYun9nHmVNTWqzo--0aL2KjHjEU6ECiTGohij927eQxiB9X5ya9eduHS73wyBy4rE1Y_46SesHmtzCkHqAX2l5oYcajrJ8oi2A_X1YGgQfeHhsoIrui1kHFIRleLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=tBc06JTqKsS2vOKLKCZMXh3cJgS-HeOOlPTFutOtvGICYJyD_QLBqcQQrP5V2EVmcruZ6x_5V-I8Idzcvb7qtqqkaNF9p8PIQw366exwLs5OBgNHjbOjQG1WcYM7IbEPiRBc11ndfkhSTFfTykl9OXZY0hHRDf6kOHmsaSTMCzwY42OL1L6eY9slZijx70AvAT8RutuaAuookVNGYgy5CzKyxYun9nHmVNTWqzo--0aL2KjHjEU6ECiTGohij927eQxiB9X5ya9eduHS73wyBy4rE1Y_46SesHmtzCkHqAX2l5oYcajrJ8oi2A_X1YGgQfeHhsoIrui1kHFIRleLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=o4xDG5HkKW07lU_d8AdfrzTmeOJ1rr-QErFgLuhQeg7Tg5kq1yKAVrEwAAVf8Z1Fkn-R0FXR5NPLXF16COrsxRY3qFq1vYLjg_EwmqKkjLcW0tmiMTHwKNONvK_hd_A46fjWGmxcXezGXGNHllYa1O639EP1RwlrfJphmPJ-yZ9wGo60TCakpGfIyqNcta9iNlASk8gyDxqQjCV9x0LzuYqFm0dsYSQtgaPtq0val7XSqxoM_uzrtdf21d5cfx_sBfN_z__zs28ZoBhItKeCEBuwOo45k5EOudnsujgPfH58UAxg4llvD-yjPDGOQSe8p2uPmEbCTgIcHDMSU0Hzvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=o4xDG5HkKW07lU_d8AdfrzTmeOJ1rr-QErFgLuhQeg7Tg5kq1yKAVrEwAAVf8Z1Fkn-R0FXR5NPLXF16COrsxRY3qFq1vYLjg_EwmqKkjLcW0tmiMTHwKNONvK_hd_A46fjWGmxcXezGXGNHllYa1O639EP1RwlrfJphmPJ-yZ9wGo60TCakpGfIyqNcta9iNlASk8gyDxqQjCV9x0LzuYqFm0dsYSQtgaPtq0val7XSqxoM_uzrtdf21d5cfx_sBfN_z__zs28ZoBhItKeCEBuwOo45k5EOudnsujgPfH58UAxg4llvD-yjPDGOQSe8p2uPmEbCTgIcHDMSU0Hzvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=u4yk92-6NEf3msTVny9ZoQD0hbiez9U-UmuHvYibSQuTOAU1eh2EKx_6Y6NtIlMgMjaLfSrrDxuwUBPOG-YboZR5YhgLRUPWHADi6gTMIkxim5dK8XDpc-P3vWIl3LDBViY5vTKTiepOiV-pcvnHUmFxBoDT3FtD7q0sMvsi7Bnou4sfh72V7KaGANK2XHwWFYxova6PQ6epg6bhJoXuOWdMLeFfW77W5VQC3z-pwRvTSjD22Wuy6onvde65IE1YgH7ykLb63vsEBbED5IyfQLuolfUCFHjkxxYb4SyIRtPO9Ka96eCHjdgdpBqzIOEBBFE_KsYKsyFLHmdp26D6GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=u4yk92-6NEf3msTVny9ZoQD0hbiez9U-UmuHvYibSQuTOAU1eh2EKx_6Y6NtIlMgMjaLfSrrDxuwUBPOG-YboZR5YhgLRUPWHADi6gTMIkxim5dK8XDpc-P3vWIl3LDBViY5vTKTiepOiV-pcvnHUmFxBoDT3FtD7q0sMvsi7Bnou4sfh72V7KaGANK2XHwWFYxova6PQ6epg6bhJoXuOWdMLeFfW77W5VQC3z-pwRvTSjD22Wuy6onvde65IE1YgH7ykLb63vsEBbED5IyfQLuolfUCFHjkxxYb4SyIRtPO9Ka96eCHjdgdpBqzIOEBBFE_KsYKsyFLHmdp26D6GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=JPPI8sp85pb9eBd2Pk9bLjmFcycDBhq2QdUgA4Z14KyD7RTXzijyjMUAMYfzMQGmmfzCc3j_yTHD6aIGp2pAdwM2UAisPOViKmUlz82xczzNrVd7-qTxRcFipl4pvcbmC8oA0040NLOuhfQpHdiPv4LHvIKnDuYs16WVl6z77oaQBAc-LPX2xaf8mYPGK7rIptT4zWSXJIIp_jtUu5Fd9rFUv2mOJhZmh-0JRSYYIWXq3vLNggce6EHUPJT-AaFoCkXNFc0h4hnh7XQ7TjNHnV4Mptd8AFm6Qg0V6U4LJZaiumRQUsVLEWmBnmOppo2bt5QdSLBTlDG8JIIasYlIqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=JPPI8sp85pb9eBd2Pk9bLjmFcycDBhq2QdUgA4Z14KyD7RTXzijyjMUAMYfzMQGmmfzCc3j_yTHD6aIGp2pAdwM2UAisPOViKmUlz82xczzNrVd7-qTxRcFipl4pvcbmC8oA0040NLOuhfQpHdiPv4LHvIKnDuYs16WVl6z77oaQBAc-LPX2xaf8mYPGK7rIptT4zWSXJIIp_jtUu5Fd9rFUv2mOJhZmh-0JRSYYIWXq3vLNggce6EHUPJT-AaFoCkXNFc0h4hnh7XQ7TjNHnV4Mptd8AFm6Qg0V6U4LJZaiumRQUsVLEWmBnmOppo2bt5QdSLBTlDG8JIIasYlIqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=fw5bcDwAC2nZi65mIvWhlcXdSRp8vd-InXctc9OPe9l2aJNzRkxStQd4mtGco_UrzgP70NeC08ZT2Mqq6o-zQYVCsEbEEhjkwTqEuwZRDkFXGemKbpjoF_R8oNnBY6euvrTShAMh6IleFo_fCunV4Gu2pBJZlKCFsWhU11MOKa7NgySJanl_hNWBGIRngOR6M7T3En4R09acH2t0KHB2xUbM9EdJmFCfaH_idOWeWnCg1BPwBl4dFsZwyCSu4vWo5Qh-4JQ6K1zUAqV4RmceMNqR8WimCBYP3NyeOo6TRY_y4S2oCvVXLnDCtwDgIKFsLCxhZH5WhiCCOEnXKamSlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=fw5bcDwAC2nZi65mIvWhlcXdSRp8vd-InXctc9OPe9l2aJNzRkxStQd4mtGco_UrzgP70NeC08ZT2Mqq6o-zQYVCsEbEEhjkwTqEuwZRDkFXGemKbpjoF_R8oNnBY6euvrTShAMh6IleFo_fCunV4Gu2pBJZlKCFsWhU11MOKa7NgySJanl_hNWBGIRngOR6M7T3En4R09acH2t0KHB2xUbM9EdJmFCfaH_idOWeWnCg1BPwBl4dFsZwyCSu4vWo5Qh-4JQ6K1zUAqV4RmceMNqR8WimCBYP3NyeOo6TRY_y4S2oCvVXLnDCtwDgIKFsLCxhZH5WhiCCOEnXKamSlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=LhA9eXKNeI-Llvb0CJv8Xzir3gQqknrJdbhV6tGWTmWhwThcxLJEqnw6bq_ZW8sV22P27vLrzPurt2Q4uKylhdFKZxOisBlSboPW9ZyiaFJOqdKMq0HibTLq8zK8ogzQkxL9Rv48CR5ELN_kR02R-EcyqFbo0HbJ0u8nhKWhD35QS6f51nJh6my42S5MlxPwuxrGzAJFpoudXdkQAarCIodB1JvK-cZmMrbeqjtkXrsl_D9qLRZxOF_ChhOgGjn4O88rE23JDvFeJ-5blCybRauOOvk_R54Ts2Su3vkzbTa-mMl0J6P5ZjBHpE0JPuvBGkIID7cuWd_HgzlVjDS6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=LhA9eXKNeI-Llvb0CJv8Xzir3gQqknrJdbhV6tGWTmWhwThcxLJEqnw6bq_ZW8sV22P27vLrzPurt2Q4uKylhdFKZxOisBlSboPW9ZyiaFJOqdKMq0HibTLq8zK8ogzQkxL9Rv48CR5ELN_kR02R-EcyqFbo0HbJ0u8nhKWhD35QS6f51nJh6my42S5MlxPwuxrGzAJFpoudXdkQAarCIodB1JvK-cZmMrbeqjtkXrsl_D9qLRZxOF_ChhOgGjn4O88rE23JDvFeJ-5blCybRauOOvk_R54Ts2Su3vkzbTa-mMl0J6P5ZjBHpE0JPuvBGkIID7cuWd_HgzlVjDS6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG06czN1Y82GidDMNkkiYpXdLrvGNbJIlR2fI4RvGb4x8NSFhXV7g5In56euX-fA0AghJiV8PFaRR6tcfyHmicsf6JoOk27tM41hbcECkfRYymYicICW1NOM_R3qyKY6_50rUt0GoSbCGlg6qSD7OCZ937T-DpQalMGVTXNB-bc5KbG_P3LckTc82M-hjDogGLl2TaJjjtsyy1ET37BAWjdEkw9wEG9QI0ehA_1_DQGqG-ga5SzrrCoVchVthbwELGyJD4jBQ-UaYv-892pBZMtwe_WFp6RegEtGP4PNJUoyMPSDYAbOFkA1hEDA-Lc7mAezpG-TRkXtk1kSuZJ5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rk1YgD-MwBPHNM8MHgVP7JJl2jlf-QhW03HYYzJOoXcUl3SKExkzCZM4zi8mewvJLSHlHjBSO1_4KZr9QiCY8CdMCLHmLt6qyXprFVZps3HC_GPRwZVKKvxWTRu5pnR4sBY6CwQ82lN_QM2AJ-ORTQKYzSmYCMeTOWz6N6y3xj-rF0P7R-21ezaqi6MGnCRdGVOOUWRt0Tiav9VnggalUK1jREDya-CPLiEEavoOSIN2rVe1R0zTYPKVv0R0cUxTf3ORhD8eswkP0qi8ufqCiPM8tjTCxWTDlczlQAWcshYSacb_SVW8D2lL548uFVaKrAbA_LRxBQcjSzolnislyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4fWYpG4zJQggyqms1x74430aNmk-ijejGTjYkkSAQW9B0qysZDOMoYPrGTJrtd34pbYa-dnTh6jIuJf1eUAlpyYE0jt69FljJD8tFpWiIjT3Ff79Hp2x267W7XjizWJvvtaY0fUY_SOsfHjyMnyLiDH_flShId0YMfZKPXx1gnR9zDeMu-2yXfuBC4eEufrXWtrgevxBoPSw6TTbJ7CoWco20D9UrUQWhOApJJjGh28uda-21ItTM-HVd2rlowjJYWsqUtTEqDZ9wcdD6IFp4-_cjHs3Vu59RbhoqGHLmX3AUvfeTue76-fGkQc6tbY8f3zTdUM55M0wb8AdbpD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=W1g0iorTHJ9x3N86lHrJ7HGhSYMokfQnZNR92rkfjDzNexeKYaL7IfIPV_YChEj1A9wl1ERnmcjSPiPpAhXyiKYx4hTE3f1Q5Dj8jAOeByTMXOSY7aqjYMxQR3LC8cKOTHrZbP_iDFXX_CmQUx6YuvzvnSUaiHTc93UlyK1dVms7TZXYshq3klPXPg5s8sPhE7eRi8CWpahzgLT1qXZoLNHAV8QJBht5daaFk7jEIg3R83BTbURBkr99l9NlIbGMXXkNZ12iKM2aaYvm9G2iChOgW89_KGoj6QOVzW0IF9E-r74YkQ7Wy2NbE5r8oSWouiPLIFn9TL_Yg2E01tbWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=W1g0iorTHJ9x3N86lHrJ7HGhSYMokfQnZNR92rkfjDzNexeKYaL7IfIPV_YChEj1A9wl1ERnmcjSPiPpAhXyiKYx4hTE3f1Q5Dj8jAOeByTMXOSY7aqjYMxQR3LC8cKOTHrZbP_iDFXX_CmQUx6YuvzvnSUaiHTc93UlyK1dVms7TZXYshq3klPXPg5s8sPhE7eRi8CWpahzgLT1qXZoLNHAV8QJBht5daaFk7jEIg3R83BTbURBkr99l9NlIbGMXXkNZ12iKM2aaYvm9G2iChOgW89_KGoj6QOVzW0IF9E-r74YkQ7Wy2NbE5r8oSWouiPLIFn9TL_Yg2E01tbWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxJcEd1Og-9OD_aNBfrHXFyJ7WMaVxX4SwfWjike3iEBXVOsHH5BM3qliS9-BJX8yIZMrTjtPIDUYFtvYa_bCw7rSEsvKtsIFpbcSG1C_ZbCQCujsJsJVU27-ucl1XKqlWGea6HjFNIWyL4T_3Utow1ZbIh_nEQztPD9SEdbhM0obDKzxH_-p2RlsO3TUXSe5UcFIb84Is86zbAJkcB-N1GoSnIWGolp3xLRrL538qK8uAW6O_GlwoXYnGJpioUX10phOrdAf4y-ZskQuTtrIv-O3pLkvTY-LRCmTAUcoWsr44sWdI5etpCQUxm3WckNzL0jnK-CYoRXGA6fptkJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=mFCm91wgebByF6DtYygyz6BuWM46ETZsd6MQtzLq239TdFdWl_qAC_0JyT2gd5M4EhufxjF8aShmNJP0AQBxbnSfritsAQxq7UaEv5aPbQTu6yE66bKqaAO9PPGsBWFKuOgkB0mT4rkzBLIX6GYDZhPRXZIvw7RBSpKQFqmOy6QdtBOlhPI1c3jHNnGLXBIKHJ1RBdjQZHctz2-hSKGA1FLYvQkzjH2bCM2DK0e4868yHrU_m3IPEEMG1n110TjeGgFg0eiOJWh-VW9E1XBm4BkR9G1EgR-8SpaU_tcZ0gpwKihKsHykjpdiGAkPJOVTFhQNvkfiddHF0YsqrXEX7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=mFCm91wgebByF6DtYygyz6BuWM46ETZsd6MQtzLq239TdFdWl_qAC_0JyT2gd5M4EhufxjF8aShmNJP0AQBxbnSfritsAQxq7UaEv5aPbQTu6yE66bKqaAO9PPGsBWFKuOgkB0mT4rkzBLIX6GYDZhPRXZIvw7RBSpKQFqmOy6QdtBOlhPI1c3jHNnGLXBIKHJ1RBdjQZHctz2-hSKGA1FLYvQkzjH2bCM2DK0e4868yHrU_m3IPEEMG1n110TjeGgFg0eiOJWh-VW9E1XBm4BkR9G1EgR-8SpaU_tcZ0gpwKihKsHykjpdiGAkPJOVTFhQNvkfiddHF0YsqrXEX7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=X6CJbKADDYFycxxJo56kynIBEq50Ziu7hvHNFjiQmqea-X9LPs1CfOGPpP-Mp2EC9TC9SEICWwpBRurkzBd3ygQgsnK6-JH1WBLu_gw2bifHaQI1VPWtYqXq4XIEtKBQFgP_7Ru-cT3iGDUOV5Hl2FQhHvn_sNyrgfSXxa7eMHprzouXqS41piCW4mDBhO3rcKiJtrzenUt1dU9lePWHPjGoJ-PTKYtBIjt4Cw0Fs_RhzUzuzFOs65TTdUHwtUV3LrLZunO42HROxb3q62a39CRJHuwDdUViszDQB8gskuntox1j97x5727p6lHqUxiF3Ga8cqqjoRzFhCVfBSISfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=X6CJbKADDYFycxxJo56kynIBEq50Ziu7hvHNFjiQmqea-X9LPs1CfOGPpP-Mp2EC9TC9SEICWwpBRurkzBd3ygQgsnK6-JH1WBLu_gw2bifHaQI1VPWtYqXq4XIEtKBQFgP_7Ru-cT3iGDUOV5Hl2FQhHvn_sNyrgfSXxa7eMHprzouXqS41piCW4mDBhO3rcKiJtrzenUt1dU9lePWHPjGoJ-PTKYtBIjt4Cw0Fs_RhzUzuzFOs65TTdUHwtUV3LrLZunO42HROxb3q62a39CRJHuwDdUViszDQB8gskuntox1j97x5727p6lHqUxiF3Ga8cqqjoRzFhCVfBSISfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki07y0bsr1cyKJD5LkHRz_R9IdzKhP-2vgrIqJDnDouF77joEP5DCiOJ8kujp5VnifsCFS0slnaRhhAcRUVk1ddbAM3hu_5yKN4jwhClLeMI7AmuhvBxJOCFeSSVh0eCxV_IE3tr7v1J4qrp2_TYGcEjGOENdxx1qCxu3RJZndgQn_-VTf_jvpvDmepU0wlsYSHsC4lZHYlXQlgkusWVf43Y-02HoUmfepC6VU8vbvk_mW5KIZZk5KBEFxtElBEG6Wva3vDEUjSHPZ8C3ZO1fUTQuj1yRqmDk_yrLPigopGPO0CbX2OTJ84oT0jABpEDlFxfPwiH-ue1SIfaCPnk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWiCf4Q8vsRU4u7HYcSO3Ko7kZvr0qgRdAePe9EUUztk7n9eQ-HnZB97vuS9X0gDO5SZpwjDSIbPp6ooHHoc7HutET_Vm0pGvznD9SaY2oPYSB3_M_Qh8aERc6fK1VTpM8IaxXBDg5VTIHZo9XfDfa_s0yDwkhVVMJotnqD0UKE-c-f4tot24w_lE89hzL37ygOQYXNPhsK_AcYy39x7EHOrciLXL3RbCnD6PLHPe-D80QJO3dm6MkJEelroO64VPuJiRnOHnicM_zCXSuE6DxfcI99ML-8pxfh7TKLzeQJ-e1U_KGNFrVRlOk6aT5d-GybCLmMEbuAJErbLwogKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJKCOqjcJNbm3m-J6Z4ff7YgA4C8FbYr0zuAi-cer1AR8SL4hfDu3iwszfKBCsGKVpNDeKxvUCU9RqrrP4-VcA-up_RCNqwOblAqgVIWAxb2S-tJjlK7GEyiJfS_aBlFy5qTxxYc5AVA3KR3UZHY0pJtyhBC7C-fgYMMlR-5alak-Th8q74w2FGjtsoGGaPTVEED_QkbXccqBXAKZ1OOojDM1znTDV1fZBpXR4Xe2m6wnvkm_n_aVCizCCf79lY7QDx1aMKXqKAJ-kbzbcINASr0g6_PBJNucU_17QPuAr6MlVDI2IkZ5Ldvzl8EV0wgRkzpFieuxxpmnDA7jf8T8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=LWmW4IzXluK-OdPvmQRpiTMn7pXk1z5UEQHur4gxtZT6cONPe84ooDBtffp1dcGuU03F0_-08hi3ZHDkbwnEiLnuUkRMo0LSNGNDWRTH6KoiTdxeMSdVPBpvw51YrZrhlseNIKb4w1JMqu2LlgJAlU3t21etWqT8fJG2iTC1iHj5ejofWdy5VORGwJ1AR4Z3WcIPIFZDbNIVQegdqsyhZcmbRZ6JGLV3QVKlWfLKrZPS1HekgiP-QjcN4lo7OvV_4mptdg1BkdbxJLiWlLOf5sWNAXZP6ao8u15qykBJs6pFedaHaVeiokbrH2i-HbDQqXq-0TGQt7uWzo55bI6TwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=LWmW4IzXluK-OdPvmQRpiTMn7pXk1z5UEQHur4gxtZT6cONPe84ooDBtffp1dcGuU03F0_-08hi3ZHDkbwnEiLnuUkRMo0LSNGNDWRTH6KoiTdxeMSdVPBpvw51YrZrhlseNIKb4w1JMqu2LlgJAlU3t21etWqT8fJG2iTC1iHj5ejofWdy5VORGwJ1AR4Z3WcIPIFZDbNIVQegdqsyhZcmbRZ6JGLV3QVKlWfLKrZPS1HekgiP-QjcN4lo7OvV_4mptdg1BkdbxJLiWlLOf5sWNAXZP6ao8u15qykBJs6pFedaHaVeiokbrH2i-HbDQqXq-0TGQt7uWzo55bI6TwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMcfx5uwXdEst2TZb64zJWAvhoHi-POh6siJcnBwGNK1BjqBXZm88OdKQklrtWShCsNT3eIj8GR9FkJp4SrGlYM__phtpK4CCp8qmEvkOuHNLibLlFHm2Hty4Un88vdg8y9LmXS3RpmlzB8xXjgvSLV_x0qfE5INNWF3tURtPYdIKAGxVnmj511vSyZNYxhAgEyNkoy6C7z3ittsVAYJiL1Y3P4VmONVTQx4j5BmIrKg7IqOVEx43Ef4E1XElksmoGtW1zgDF5hlvCwAKVODPJufR0z0e7gF-m1pqCzWNAGkgh7ZXXzTHNSVZWfk1Oy_kWB2GM_shgRvstL98z4aUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b59LvMUobveQDQen33S00lhL7eEwi63o-v82KgcnQhEkc33tdrkSKRNRvA0hvceyOkuifWde8YuxYOoKcqEAiV4U9bD8WTmQ5U3EqozBN0hq-TET9F11qwTHScMZtDxlmAsC1Ghaof9u_OAvJSeCMaLJ6DgIs5UouPCkhWol_LTlgAy83JgA6LoJf3kJEjR5PCEZSThdMazGfaotYX_RNjgSRYl3hFvN2QhzhF4-1Br4Qps_nHnVtxgimUOZAEvYwtokvvH71nS1v2vCp8Args_yeGn93M-FTJ9XXIFJfeJklBev6lh_Reo4CVxZSrRC0rCULB0GzranU7oRg_iY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV4oJg31AT3JVa0mzS2yo2-djSR66WB6mWajYymr2ElHppQIKkrE_qxzneCbQ4vmUQ5syE7DiJcISlJmNoyCoMwIn-UmVl6sNXL-4O_q1nm_s1G1pqKbC-XwEPUx_lTWl6fabZ91Pqh_HKJue95Qfji7XvS2_juvoYV4f6XLN-gBECEwqPqPbFHqRCck0r6xGSIkmWJr0IKO3--d3fiGkKXbJblxR4UewN6HUBdEL6662qvV1ctXyRnYgYdu7jJFzq1d6E5HONqSXyKu14Fv7e73zLpF-Quhq-2Xhv3safFl3RM7rqTkv6z-wcDx8fjTc2UA_YJujN70CgC74SR4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd7PFKgMx_dZfNvrbrTrburg1HINQWjilJMBcXevNHFmfr2KbW_VsU2sv7gs8EaLrR9TWTaDpSnAGNyqXQ3YgZhJdkviyAfqXOvscYHzyL2ChS35PZZFqwD7-nyhkdK0RHGp7ouurYwqs7iFY8Tt17yEQon5Q8L9XMN4EpPoqHiu3uAUJH_1NVNeGPsO-mCXhhIS3EPuObFL8-Gc0bqmYs8-PQe87qBvIlkr_IndABcKMCkApHroOAf7LAwMtjVcfpHZaFYCaV5z7HJy-kcYGjzUH01fCW569YD5GcY2gYjVTKv8jQn1OLOTNb9jfR2kX8FYl0Gwyn4JgIn0ciqvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQQCy76YhXrvXxjxNKPZINqwYdMIkwwEm3jLyNjmfbIGwOH3nMWNGMIvev8ayNUU8W6-btb-dYl9bda355EpkVR7tQYV7Ot2I5v9a3UNECPieEtSZNIZA69Ysmq4bMOr05XjuXpiiQHDy_aN0uNZC7L-yrR3v_ZV9UU-BB84JZRMvAZ1OGH5_25_Z8iaek4Xd5qUvEjtn3BweLcAURb0W7_Hptmt0V3a8tfJYkujAz-rqybkHHSxptryqqndAfaVchLnuDgRwk61JQsQOccLfpRrvAAhkuTu_OMj7o6gJT2y6ErWgh5s7lS3rb6DOrDWqqosaY5xcs0DXcWio-IJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6saTOVodYFWUk4GVt_bUCy_z3ZTSyBigA1WPcMjJZ5MgwF_o1yFlXP8dT6XnqF6jHX1PYUceB8WesqJCJ1nnHBadb8SrFZ62Ghlos6AojGu5PecMAztY2uXdeztamljbqqWdiRQfdAxGEJShLG4g9xzxhJCO0XNTuocnUL3K34oUV-2oWN4qmuA0nlRwyeY-6vR7MD6dpbX2o3Rqlqvrzoc_M4s8d2ziNnu90rE1JWVCx7fj7IVTlp2MyMuJ5YUNn4Y-kBPkf7eEpsngWpQSVBtiTEmOXzFJxW4x9VBau4N879pZcg2EQmJjRp05AoU5ZdSuiKB9jP5FzFK4Hlw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krUUYngxLIXnyduaBU4OBmb1chdBk_jP6BBqaWnmwbR6sybKVXOBshYvlsWlVaK0eDRkjGQuWefGEalbaYIHkbPHxel4ltGQffiViXOR0IEB5PWNKEaUiVfgeFljOT-kj4W_8mYUj14FqufjaLkWLFob_HNIG73GSgEcDuTg3sYS0HORUN97oom1voqkkCm3n0FfNACrsyO1OLv9zC_SEAOrBd1FDB8H16K6WqZbeVPk3Ccrn1arafPmks7lN42Qt0SYsaFFdDOpQDp3AXx8TVlDPtCaxWkwaj2UB1ejm1KG-oph19g4TZVzmiMGKfd8dkeIMZKoSC3ib_-e8-4nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPLiI7Ws0ZJIB_KSi5N0P2Sfsu6d-b1kKjrAcUMchiKaHYZYwAkTOeLmABpvHqA7kkCn6e8wawj1Z7ndp-Vt_ntg0z26jn_sLGogtpTgv5tL-d268DBIPguqMNMMhpCMBQ-FlzEZE0p-p496LB8iVyc4XUZf9QxVeL1MwLlvPHQMIw3hw1ftZCu59CfoaGGgAJU_tyNHT5HCyRGaXHl_ZPhP_gyGYZ3WFVf4EvmeJuRfbt3jdeWY8iJeUBe4Q44-uoWUd1RnIx8bRfeIlPjfg2EJ3yV_bT3ah3Jnjf45n_3MJ8QHZV7fOg_MZ9d0cyGQ7Cle4dhcy8JL8PHKhO_AGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcgjctTnV4AykfjXpwINv5v9ERaRv7U7JX-qS3CoPRzbWsvDblvEfd2gUi_MWb-Ye8Ly6rEo4qjD1HRVZlfpueu-bsIQV6vaye5ttI4YRWNcQiLUzDuoWv-q5VNDEZx-kAmtqZHrjqB9UTfUrnlj57y5VIpOEaPw0umh_P4g1mV27S4_m-bp1ztjtXn_jqj4yONy1nDfxhoK_sAxusxKXbd3BiE1_nLdEjiOdiZoEQ2rpa_kd6dEKRYuP0FU9suN3XZX0vW4o6RNOOBCPdWFVM0egpLCjmIyF1KLuCYgkV9kPr3dvcJfVjAPl0Qp38ilZHnT9yde1Ykif6FzNaEfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXHjFl8zEub0yFQjFhEzWsQ4hstn5VrfIH8kBixpNVLt2PjZo4Lur-Wyzh6AUK-Bx42WAmh6C4vvjOqEhODm2tRBoVQO_iKgMe50BzW_4IvJVhGqRW9-qN5kiYYfPdgvwgV1Lt9WhpXWB-OwhPIG92z6eJ-OpnN_K9wSXX23FLQaE7LE6FzTfJamf-kmVatAKwoZ5JFVaiiVelV8CR49P3Av0Vc9L9vCWgnXqsGnI0OPJSM6Q9BPvcSy3KJ10NGp5CbjDvI41REb9k3o6_KtbiwJIN46gE2aTlqjz47LBqMH_Ac1q_4RUGCM7zw2lUvUNGX3hlGyr1bx7KkEUEEpeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3hxWlVrZSYrka59UFgs0FZQ17jyIk1l5JMgpsG6dyRCpA-h6UWwIx-uOOZo-A-OseiA4QxgZyxQIiL1-lBeTgd7amweCLX3EvglqNp_0gfSnUw1dbdBuWnABkc3FF5bp9Qkfq1WQ0jgAs7DKO-EhRX8KHN3Nctg0hnOpVay-WrcnU2s6fLstdj5O_PqDfB4WDRvIpaC4NIRcUAFSRgnOWpN39Rt2ttUNP-NDJ-gbunEVDhrHG01cYHCNsMdOyPcbtijSY73pbTd9TDsY4VnbXjxkGc32rPp4m2c4wIy_TONkyDSyozsnFDvVWfpy5Z4I-qPEXTGtsmDGCLzQRQ89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmReSgCzln7On_TYJo9S8Dwt4MdRg5vQEjsWL_juLZSNKSHkpQXLVwEgUtVwS7SPYiXQFe7oKdCYkLQ2Gl5tIOlXXF9XV4KG7fb-uwZRmV2IjFTMMsKpLB47kxvpIOK6m9H71hVNvJMJL5ebypnuwHRqedqXtWtPGuw72LpKaZQ8lUvFJ-QYVCb8w-UnTxQ3oETJLVFZz4nWPGJJ725yhQwSZ2lBp-NJw-J4IpEFGQST-yjuFZbRelICYo2zLoUwb2RxBTE4vPu0ZYlxOLN2gk1iKi129DDU6dSmMHjIPetwmPjFXmvgq3ZSiUr_sDGwbeUmKJjl8GA_fjIP0S8wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYtSLte9tUB85Q3-TlXk9gL-wjHu2hcbuTDagXaBsZ0kT6qHdJMuldoOcY2jafgFuzwWe6hRGnjIdYZX8rFuol7bqpo5TfXS0J8y2tVGNvDlvkpQPQYV7yM6dtSyAS2ofi3Vy83KO-BEjgqm9vYOtTZin_BNb8LpW4rWPPydcdkKDArce5w6tI2cvoM03nn3BXQ1o0iygI93gu6rhnLAMtDD2OWMw5NyvMjhZNgHin9ot-PuTEViwqEJTtKlhXjVDsrJ_k7gLNPkdo_hGHchVlRmqcAz66UOmsmKvjvzpPFJnyjO14LSEX18L0wp-QMmiXG6YuI0zV8pBxeJPyRaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvAbso5TDgN3K29AR3KWoifTcz-6NbQvKfONFgA2hMxSlqldJ-j5Iry47_AkLd1hn2nUnWjGTFxJ8ogp1fgkan6YGoAueFifxHyScaqq4nFkQ2Z-xzsTPRKfq7kJEkURZQfYWsx29TcD0JmPzcnEowv8-i58Yscffpa48Ofz1Tq30Ocfwf42E2pKpor7rolR0sy9t1ClcJ3vjoRwlfbZuBPoRveCOsuvRHrpqYRGQFjYQ7BwpdmJNwWaRdIZa2CEmaY4OyORq8ZKBdCLGH5RtNEjN_xgOKn6Y-BVJu7C43JGHe2QnL0nld6hwW7ZLwExcfGTTsm7jUPhkqElUMoIXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AAIRT1wWR9dpVVYxUs6O-wNeyM8E1wNqYLS-ZMEdrqMt2FX00OZtnxG5xPYdRNfhPHVFG5KTfYG_usViy-H7KYQdX4kP6z0VnxyFo97oHzW4OhzGpXZXLEUKrnm2U-BEGdYd1qugZkWNw-CdMUBaG0OeQOrNohS2RR9vIOGKAczmZN7kbpU-r_Mylrw5E6IO2XONsVqmsQxAwGAKJmYXab68xyRDa33ZGJPNE3J0Mb3SoqpeDRECY2R5dWctf0vUWpfgWI3SAjjsFcl7yvSiwkyMU-AvmhD581oG0zCmxkk439s4q4lt6mz8g7PqXIJ__Pvz8FuATGNtc66pukVhfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=oqoPte7LrGG7bGxbgRUO-1C3KBsxkNmTJum2vELqV7EU8E9jpytzxIy8hKieBfEnxAtjR1kSoLzz2lHKPQ4mNprOPXstbaS9W6PmM7L029py4ENVYlXwaAlu8O90ecqFw0C1HwwDQPQ0d8qpZ3eh-4FTf5NIV0dZhVE6KDZRa1w8sDm2ft1Wawg3scHuHurQxzBywKAaspyippACPOifIx5LCGkFBzX0zLUj63QvH86q6O5MwPlBCHOOH7ZPCgxqntxMaZ6e8-dNGU6mlBySMmOU0TZ_Spws4HEXFfRr_pFPfwPXboa9SIx71V184OoUklQJB3qyX-aMoX0xqjg-HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=oqoPte7LrGG7bGxbgRUO-1C3KBsxkNmTJum2vELqV7EU8E9jpytzxIy8hKieBfEnxAtjR1kSoLzz2lHKPQ4mNprOPXstbaS9W6PmM7L029py4ENVYlXwaAlu8O90ecqFw0C1HwwDQPQ0d8qpZ3eh-4FTf5NIV0dZhVE6KDZRa1w8sDm2ft1Wawg3scHuHurQxzBywKAaspyippACPOifIx5LCGkFBzX0zLUj63QvH86q6O5MwPlBCHOOH7ZPCgxqntxMaZ6e8-dNGU6mlBySMmOU0TZ_Spws4HEXFfRr_pFPfwPXboa9SIx71V184OoUklQJB3qyX-aMoX0xqjg-HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex6FSo2epV_7c0ARvMEyLuhuj1VWc9vY24BFtdeKH1XM0p3oO-XTf550ivMq2C-OYWQ0Npe2ac8Gr3DRpz0R0UXtrwa1BECH8gd6VxxFEzozIt3JpqM8yaCNXxZoNynb6H_dG0hFV6q7LXw3ayNVC7rNRdkmUB1Ldog4qoFS80zhTERWqxCtzt4kZZ0istgevBEqQw963z3yY94M99CRnfnzTQX1GVO1ieuz3gMK3TXtv_DwYl-y0oDjQZj9VI6Ml2VH_AZDCX5YNEMOldI9WgLPW3usUZOa7PfzF0juu0iiSH1_jhDVVdgObh7hspvGtd6VQraz437tN9SG1WlzNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMoW2zKxNK3aT-dJ4HabomVWwqvkFtGgvGI65FLUNFxR3zICCyW3py8zFraF4WmSekyzj7KlfBLJZfXi_0fTDKJ8w52TO24EqN0NWhjWUfTvgTrPXcVM_V6psHvLBWhQzbhXoKCtuxIN0qSUtaNZNI1937xD7mKaNhNY0W62zFNCiddvmoNcco6-ZjfvEjpm2q40rWpzAnqb6BcoHbQvn8rOMMcG2_MJxfLNcFOE8ZzhkjiqVpN-ZKrdExSuvseoNdSxhDCizqElgNutse3A82T0sDfyd0U__ZPQjbHwjugIPrdnd1kjzeBZFEYXUpDey-pLpbLf8RXRPQ7ZeSYgfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=lALeE-X38Kvos12K25hbNYdsuwKKRiTo1BqUc_eHutCmPgjkoWAXuhNJW6lNrVGuhq-xbSxZR5QWR-mJZFKFWfx8V-KNY489uUuQh1X7qSZk_kg2ScvPdGl6YBE5JGkCKWKu3gle3F3Oo7PtqICD3NNZ-a0GKWgC12_ZJZ6cwKCtbj-ORMlMA6GMjpSE6EH8yZzKcyewSqBpQmBGVkFec19vViMAowAb2iLVK8uguIh9VQlXzvr4DMs22_2F9TGF71ii3FmlBnQIRhadgLuE5jSejGaYaF0xpqtZhzfPeeaj-m5HGZ8JvNqd6fcu1dvPb_fB_4YYWs1bczDKNEAb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=lALeE-X38Kvos12K25hbNYdsuwKKRiTo1BqUc_eHutCmPgjkoWAXuhNJW6lNrVGuhq-xbSxZR5QWR-mJZFKFWfx8V-KNY489uUuQh1X7qSZk_kg2ScvPdGl6YBE5JGkCKWKu3gle3F3Oo7PtqICD3NNZ-a0GKWgC12_ZJZ6cwKCtbj-ORMlMA6GMjpSE6EH8yZzKcyewSqBpQmBGVkFec19vViMAowAb2iLVK8uguIh9VQlXzvr4DMs22_2F9TGF71ii3FmlBnQIRhadgLuE5jSejGaYaF0xpqtZhzfPeeaj-m5HGZ8JvNqd6fcu1dvPb_fB_4YYWs1bczDKNEAb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaMIi1ksGANMIz2pPNysC5nX5VDaaexk5sB4GX_a5gvBZfajBhs8eG1xiiEAGC8ri2cwscv_GKFqh6HpUEO_dIoVsW8kUFmR-HZ4XZTL7Blk0O_akX2aWi66S6KXY2gJZQphe-coTlxde97tm-_HI_eWUE1D-yx1Fc4KjbOQfQAWFKQEC_rkywynQMsIgtdih7pvxLPveKRewBBUOdSwNvWNXBnJXhh0eU2O80Rfe9A8yTYD10S1T8NIAp5JeVYDqVqBpnF8Od5H-tZr0pKErZbyCDg-x9kkiqvvtUW-0DznMQGsWDSyXIhIVUcbgQdHgKmv1bD3DXksX2PAeUDyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8hEgd5-DKml98s3gheko8UPBqA1hSHqFQK_-pguJDjUjvT-J6KPVoBvEvVycKFdroCNTiBWadpwBBp1mYMsDDFPphIeR3o_svd6HIODaLpdCyEj2DVJDC8Jrg_IAjqjxXewOk7Bzw0vpyaWbNPOhwO0nqs_QdcJmBFZxawWIpaBBhyvf7jVQlfFq8w6sXYRzdlIGttZQD_P2i1nl-qxw1w095Pw55wdGw7QmTQikO0tWPDXcCQB-vWqvelp1FXAKy6CLzHPiuh0GYCjHOe3cVmbXrQpSn7jYFpXVOlGIIjvB0iPKdbnIGTChneMRzPFAXvGIWEgXTkR0tUeXV-3Yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=vd2BInQRUWTAnzVGMffaTfvisdVJIDnwrHjXOwHs3JpXxPm9Bst3SBGxJRu_ZzuBn1PdUFWELQseH8mj-CdDrDbe38mnVr0Dw93GhHRAlj59_YAbYBGD2KRk6KJVERENgAyS_RELhqf6GUe4f9DWqo-y0ITvxbYAqKKWrQOWErmtTVxrCs6me21eea607Saed4GzaseAm5tcNdpqFAb6kmyV4HBLEJwLGQtjhXu9xL74hwZYV6tYx5Yvr6WqI2hZh5ged37Pz_t_XPDyppsM5C-xt4RKXuGw3KEUP68I8eLpenEb8oUcLEWqiTosto6SxknOIMVb9KpCAndP6KW9_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=vd2BInQRUWTAnzVGMffaTfvisdVJIDnwrHjXOwHs3JpXxPm9Bst3SBGxJRu_ZzuBn1PdUFWELQseH8mj-CdDrDbe38mnVr0Dw93GhHRAlj59_YAbYBGD2KRk6KJVERENgAyS_RELhqf6GUe4f9DWqo-y0ITvxbYAqKKWrQOWErmtTVxrCs6me21eea607Saed4GzaseAm5tcNdpqFAb6kmyV4HBLEJwLGQtjhXu9xL74hwZYV6tYx5Yvr6WqI2hZh5ged37Pz_t_XPDyppsM5C-xt4RKXuGw3KEUP68I8eLpenEb8oUcLEWqiTosto6SxknOIMVb9KpCAndP6KW9_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=UBVGxYYQkrgyXpacfmwQx15s-E_JImrnO6SiXv2XntB3oWA77wNSsJ11R3rBD3c9xnAsJCLB55lmx_19rM8FtNezFDvEs9H7VqhTGFHlvjQ6zJm09X6BEEIb084G5SPgcQxlkbQNhHKbBG9CGeOScvkBO6_OVKLWEY2PAnYQAuyjvAz7w02VZ8CwfzkHsicg_FzH3q4B-fnwUo3DiQAwSRpRJJ5K7jBLXSmhxvKo9wDi4qMUBv8WJcvhz1V3PhtYscUVqILu2xoF-XXhtU0S8CCRmTeFsrShOG7JJdGf3yuTe2Rk5Heipm-NHCBpXUGlrDhXHRLQT8-UhGk7R0DpuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=UBVGxYYQkrgyXpacfmwQx15s-E_JImrnO6SiXv2XntB3oWA77wNSsJ11R3rBD3c9xnAsJCLB55lmx_19rM8FtNezFDvEs9H7VqhTGFHlvjQ6zJm09X6BEEIb084G5SPgcQxlkbQNhHKbBG9CGeOScvkBO6_OVKLWEY2PAnYQAuyjvAz7w02VZ8CwfzkHsicg_FzH3q4B-fnwUo3DiQAwSRpRJJ5K7jBLXSmhxvKo9wDi4qMUBv8WJcvhz1V3PhtYscUVqILu2xoF-XXhtU0S8CCRmTeFsrShOG7JJdGf3yuTe2Rk5Heipm-NHCBpXUGlrDhXHRLQT8-UhGk7R0DpuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdVSajXeBVgiQJT9MbScUWfu-kOybRotxPX4uStsUPKz9Gckr-fCMi_xuAL5Cr7Y3nmxU-KFimvAhpwfkTu1pgpt7qHxTep1BgpzXSJa0B0MIP1W06pvHm-PJ7zzKTkBEf0bMxMpk3hny-yKa2RgWB_HAPMwk_ujtrp5ggtfWAorDdFeE2n2_2wravqgnqWn2CyvqrjPwvch7FJhsbDvZbhFbJfcWxDCy8kUM-iLqgLqkfbrOOO21E6-9PI0Aph2cqbDLl4UquSvC5gyH-vFXT4gBh5_MimqZA-pSPuG83BKf7879hwlFtWfPLJibfIOY1xegypDs4ABEQIScOHbfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHCvo6TbmNyvbgL2_GTMF2kq4auAnwN8yqefmMtgywIjUGErg4Gpi1ITXOdz8uJf5EGOhtF-PDPW4cls_RGaHf8BQN1HFXqNxwWpnj7TeosovnqMAWpSVPrekUfbIR8oG1HnWV3sRkSZn-y3LRUayjRdVwCCn8dSlBvUlMy2YUhd89nzjuzOucibjixEOvMgHttWmsKleH1HlvjANATd97vHoiJ6KgkzeyAktLHGpNWURITBQq73hUStKOekoDMDloWHLK8twPlv6jicQxxS1jdW0-NoIgeBET_lYJ83pZ3kicW8WydtOIvXe1NLP6nekIZb9x1ndJMgXvrD2ltV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUgiIp1e2z7egYheSLlvl3asUhlKCBqyeUm-uJRwmbtGzjvwrsVF1XHdpPoFV6CSpv-vmr_-cRbWQApEeVhS_DiDXP1nqJ9BHgTrYIuioHpB9MEYMll8U6ovk3k8U0ZDsuHOcGopdBSd9lVc3lwU2YWnRh82UFdk12d91FIKC6t8d3vvPvlQPAbEGNPQKe6Xnefesghc3F_cxkdbZnwND9tcQjf3bx6E1CzDGBgHhoGrGAoNIeYXUAiSirE78vP8z027Ru5DLpBA5rgLQ2u47fPODrBbQhcwbQfEywJr6xwjFzDm-2_ugINE6YW9fXtIOH1nk-EcpTxmgyiC0mLljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=rnamZTBXR0-g-8vUgH8Wev4DKYaWlan2JF0ZAU_v3xJLkqE1hx6tEBXCqh4t79_2ynouJNqTrCWOPkYstKWf_koWRT66bb9GZKBccppek_FqtdE4BPexJXzkSHUsflyU1biucBjax6WgOO3BQ_lzs4cnABO9pse0y4sQ6fjr-C1gfmvbswfRJGb-KnA--joD7Gv4dFN8QVTCwU3R125kwVmWYhu2mhGNK0swsOgtEr5-liuzzEYUWO4lcbqodMGoKqcUaupULU82iAwXB9C2MwdFT-r_i-793apv4SaduUAJQIITh3TtzDffK4uUZXahiccdULCKU4Mx1CO7gwnbGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=rnamZTBXR0-g-8vUgH8Wev4DKYaWlan2JF0ZAU_v3xJLkqE1hx6tEBXCqh4t79_2ynouJNqTrCWOPkYstKWf_koWRT66bb9GZKBccppek_FqtdE4BPexJXzkSHUsflyU1biucBjax6WgOO3BQ_lzs4cnABO9pse0y4sQ6fjr-C1gfmvbswfRJGb-KnA--joD7Gv4dFN8QVTCwU3R125kwVmWYhu2mhGNK0swsOgtEr5-liuzzEYUWO4lcbqodMGoKqcUaupULU82iAwXB9C2MwdFT-r_i-793apv4SaduUAJQIITh3TtzDffK4uUZXahiccdULCKU4Mx1CO7gwnbGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhaYaBQqw-AktA5uQw3etOzVOF9JxcZ5UG5rRsPC1yqu5HC9llJVqFHBa99qzE2RnebGrPN7TkMbk2sJdFliNvrY4mU_mR4JRr4CZBcWuYZUGczRd19y0FB3tuu0C_GEligA66QlERX4CLEuhgJZ0JAqWZxYTskPHC9_8FzzxHk62tibeQgKgw5khmOXf3sSxf6VzpZSWLDljhottcHNB1-Wn6yN9nmjv1WZbsJipEENbnTNhI-7dV7TMN3tEJX6J1Zxd5eTZE_Rzum4hSQunh-kQiny9AMuAhVn6RNJuw2E9fadwsdpnlq249KFGW8itDlyX80k_peJxahC9b8GXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oETnCy9ZiKzmKnHwB6l-_6-hsEU28IMXiG6NjGsmGGc2FhFY-oftdQU6-rHvqKSKFnBjVDrBuV-gx7MUY7boE306r-TdOROQcDaOoPlxjAmEFvfg_faKYX_Iolv5cojgqgu6YkilADQBOa7AJdaWGEJ7V8pFmsg66_-BhaTdhB4nbQramPjjMiksxi8aDLds8AsI4DhVzklF9QW0gGk9EdJu-x9-6QC_8bxzHiGXzFNnG-K9l_kyLXHUeKSvSoWbcTZqJhvBcu8iF97hfdgDLDWp8mBeQc7s51siy9SUmhJi7atKrhhkL9z6dNEEpj5WgVIZ9En_dIFl_CfvzgijfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CR1NpBfHtBLnxJ5lBNB13IR-6uR1_2Zi3X2vR6B7f4yO4mJrdMgyt1PHKDv82vz84cVclTOpo3fvFY-3cXjElVzm9fZbYURSzK59Dv9rnmJiIg5OpBQtqPNxcnFpZc9D9iERKNLIF8-a1fkfywaivjfPddI2ayJumoi1sNfIr8GkrRm-T_Y6pekhvx5uqO1_odyiXdS1lA5eUqW-90nfmKeAVudwMfHPE0atosMHHBXJ5fRSTr6YzazgF_rpwziOkp4ZgmMX9MI2DBVBpoTCW8eLzZhIRbi8XT4kDzAn6SdMnUbc2idgvRdgy6hwQ06jYebkRf4sxp-T_wnB3oSVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IukIQNk07b3OZZTedntcycow-sTYArlOVF4t6Jyv8ocHr4jMoZEiPrGcGMUdYM9uhQX7vOU67oMm9Rw8IvM25EyE7Y2I0pYyv4ouuVxMmI9wHz6QXLV-jTZLBozil0y4LNAzlzIhZOnH_3gFk-keCxJfakMtENRgu_zmxOS9fhKsyyX3ON-WNnZQUuO_Mo7TaWbZB1_qWgVj1jb2MHG-wjBMiamn-NwC_9EYpnHqKaQph_8oDLGJ5NOn5iIPKe4ebR9fyqY93RmERBagp9x_-vB_7zQJ09Um6VlMcNANpvZtd6hxytGfG7P13wIBnbXuDsqsBjUGaG3ubQkMba3lKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi466XvFQHlCPhIiM-mP0qaNCrLdKZnFJjyhDCIVPDsqvIlC2ak4Id-mm-eqbHoOHbiafRgYxYFijkMJP3LLOf8wiwiN6Xxw_jtGWXO4rqnDDu2Xk6esie-PfMHJnkHN_cmDErVoghHDKd2OCZ_fOtJ7w7em8RkTkHl8NRYi5DCv5VC1RCaP8kOtysDnZ8Ma1G4yzuaxLc-3fiMRm4ZKVKfLPhnVW7s91I1WyGbyZNP5-SIa0A2vuzIce8N05c-M7RlrVWWuKV8umu284HFp5MPKk2SHcr9kB3fV6nk6E4Ch3ybr-guo_FvSG8aPG5z5L3BEWVCflRgktJUfREaIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccsJUl3fgHj1OK4Y_6AwVKhq8b-9lFP8t8tmPx4wRUVRwUd0WbYU1isE0GjApUI45ipKZmYjUDJYVycHILCM3kAl1XG0KiEG_ZcgXW8H00-BcWURKppa0sE5qzR9nFCUwOz2GBAsDKPleopgWfF0g-tfJ3K6iz-4dHyh2YuzoYMLa9TOO5QtQ9Cu4gAlMhblkITWWKW7U7mu3ru6woi2fXM-C8P6our3F2YCoMEBkotIiBsD_EDg4gbo4Wc4eCYd2bFIacxR-YZalmpm1M_nVT9BEQi7X0NWG1ZMQyMAPPqyiWeRXkntVEU-EXUlL9IJTCKmOZbCAfmg2uJdKtYyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3-_Zdb2LDgu2IoA47A9dt33Av85qZWK1QakPY5JfpHRaBgFtvKy9Ru1llWylaKMTSsU663CYrLvQNTMQwSybf2qU8BmCnklyUwk3mDaS3lBZaqZJHt-azPjHM1Bo5kPEJTogrdxmN89eQR-kPoxwaWeyaWFLl5GOT3-6Mj72z7_ueWrodqhwok1gh1vDxCOTIQAXKeBysrdvzB5Nr8SAvEcVSngSWpdTMZRa4LIRNzTMvS1ezVGwVOf-5wOgrMJ3Cxjm59Koux6vfy93knWTxXqsJzXH0MPRZ_rUmPUdf2PIcIs8IQlHYzChX-zlB_pB2hgqfbb-C5gmBAaRvLcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
