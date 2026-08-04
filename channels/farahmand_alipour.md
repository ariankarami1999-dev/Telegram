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
<img src="https://cdn4.telesco.pe/file/WGeFoO7YeVjUsGWGemfJxTrPoPmqD7Nrhqp3iDYDc-mj4r9g9qPPcKgUCZLb3VOU--KoZVQfOkCP6QXqWJLXYSbLiqeSf_-AIWiujwya7v-3DIUYKvcWbYsHJpBxDUrcZw2h9H2Y1DJ9YaAwK1BvRDJFvdeSrdE-Sw6pPZOKdVFV75-YlQ7kVe3gD-_QZsQbDScja1DMj8pV3hhN9xkqgzztKYw4_e2DXU5t-a24PC-0pdNS9g7ZS-eBHKI3xeuIsj2dl4njVZ5eJ0wcpXeOMMTN4Q8ap5o5qIGXovChchnyqkSzOUe2X6Y8dLuUMn1zi1eSRYnuV00cK9nCBrBqYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 15:06:30</div>
<hr>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=p-IcIbX4iw3X-ScIZCd5sVRzBcrUl8IZCcQEpvCjXbQxIqek8ZHUKaK8hDBnjsXmcJHlMbfazvvmAYLWatSDGDEZueL6xMPaw74G3lTjOSVMRsmbSNAtTNwE3kQ2qR442KRktrJphkHVEusF33iCXNAGroqFzKFThWF-atUUX9wXLQYmMffD5ACEjDfcy9xjXPXj0F1aBv-tw1vjaACCZy3Ohi45YGS5s0JG8kcypXu5WVtkV5MrswotMWtqpD0L5JsYsp3EEi4RS8J9k9YmBhXPhZh0IyqtnYbCp2grlncNCoPkGSmXR-YMmuHSZsCz2EtaAUnUToe53Quqzj1v7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=p-IcIbX4iw3X-ScIZCd5sVRzBcrUl8IZCcQEpvCjXbQxIqek8ZHUKaK8hDBnjsXmcJHlMbfazvvmAYLWatSDGDEZueL6xMPaw74G3lTjOSVMRsmbSNAtTNwE3kQ2qR442KRktrJphkHVEusF33iCXNAGroqFzKFThWF-atUUX9wXLQYmMffD5ACEjDfcy9xjXPXj0F1aBv-tw1vjaACCZy3Ohi45YGS5s0JG8kcypXu5WVtkV5MrswotMWtqpD0L5JsYsp3EEi4RS8J9k9YmBhXPhZh0IyqtnYbCp2grlncNCoPkGSmXR-YMmuHSZsCz2EtaAUnUToe53Quqzj1v7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=RNifQ7TE77IBn5jPtQfW32O-dFl47vBo90hGnGhMzJXFUYkqeQ1et8R97BS9tuIN6VKc-bMpkyttvPX53PzXmUOOWeNec0jH3UV95TIrF6e0Z_rruJv6txkao2jgmY-pZqykk6jJBmFjl9ZmFXQqKEwiYYpWRQC1FHdiBFu-oJOLbr3Gj94JINOqUqeP41BEHqiFYGXQXgFT-Dk1QI7RBknWVPwHZGdX-hBfZAfkFUVh0sTPqcfTmp1xppKKs-JVTqXxCZHNcxrus6hPIkjKIVUILpwY104NGPxGHKPrTY1ytkRLj82hG_Haw_JQ_275uJ7ALfJZBwHD_M-jOUckBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=RNifQ7TE77IBn5jPtQfW32O-dFl47vBo90hGnGhMzJXFUYkqeQ1et8R97BS9tuIN6VKc-bMpkyttvPX53PzXmUOOWeNec0jH3UV95TIrF6e0Z_rruJv6txkao2jgmY-pZqykk6jJBmFjl9ZmFXQqKEwiYYpWRQC1FHdiBFu-oJOLbr3Gj94JINOqUqeP41BEHqiFYGXQXgFT-Dk1QI7RBknWVPwHZGdX-hBfZAfkFUVh0sTPqcfTmp1xppKKs-JVTqXxCZHNcxrus6hPIkjKIVUILpwY104NGPxGHKPrTY1ytkRLj82hG_Haw_JQ_275uJ7ALfJZBwHD_M-jOUckBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=mU75bvsSKXFTS5iNgw4RVdKiG7u5VSxWirSHUXLxh_LjSGYBPSlyT6220MHX5rv0Df1xiGSMsHIDelXXMdp4ZTqHBcjoeY-w1lzUQFGU1JDfCjiU2FgEWXUOy6ZZm6ER104i3Rrxc3jn561u8zy0-5r4ra9392Wl0hn_KaErfVYQ3pVrS3xkO4-katB3Zk4_2YJKdt_RMfELBgJjiOg07mkS44FPYxDHStGt7bXR5Fx2wVZ_QPzopgadt4Cvs5OZbEUEKV7J_MzxCZK1PybwAVA7hbfOphTHlR11NBRXOU7NnNGrYQWYqwIA1S1mc2SGJ5QBdmSTGP7MM6N0Q1q_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=mU75bvsSKXFTS5iNgw4RVdKiG7u5VSxWirSHUXLxh_LjSGYBPSlyT6220MHX5rv0Df1xiGSMsHIDelXXMdp4ZTqHBcjoeY-w1lzUQFGU1JDfCjiU2FgEWXUOy6ZZm6ER104i3Rrxc3jn561u8zy0-5r4ra9392Wl0hn_KaErfVYQ3pVrS3xkO4-katB3Zk4_2YJKdt_RMfELBgJjiOg07mkS44FPYxDHStGt7bXR5Fx2wVZ_QPzopgadt4Cvs5OZbEUEKV7J_MzxCZK1PybwAVA7hbfOphTHlR11NBRXOU7NnNGrYQWYqwIA1S1mc2SGJ5QBdmSTGP7MM6N0Q1q_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=GBXZ0RlZcZGQ3odp8MYklRjAYMYnleEUphkbswMpE9rPe5j4a1pZXpLtHtVjWAOZJjaMLY1Z2YGyUctG6mPscprYUxlVXYAUIqBZWRPpOFa5uc1G9gJZSOQk2PR1fVuNchfkvIsKR70wBqAvN1BOCyXRQ0NHf9pxamNQL6FiSduoIieAW9Rg-AVgBBSEKTFRhhFd7M09YpxxiB27uUvjBwJtqND7e94bKLHuMpdMTkMaaxOHqdlIvSN22HkXphHwegySRxIP42vLeuVhcUzdvPOVOoRcA5jhriXGP7v9dKO_yly44BH2U0bVo6J9eQ5QCvFTVIC3TqU9_O_siBKlOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=GBXZ0RlZcZGQ3odp8MYklRjAYMYnleEUphkbswMpE9rPe5j4a1pZXpLtHtVjWAOZJjaMLY1Z2YGyUctG6mPscprYUxlVXYAUIqBZWRPpOFa5uc1G9gJZSOQk2PR1fVuNchfkvIsKR70wBqAvN1BOCyXRQ0NHf9pxamNQL6FiSduoIieAW9Rg-AVgBBSEKTFRhhFd7M09YpxxiB27uUvjBwJtqND7e94bKLHuMpdMTkMaaxOHqdlIvSN22HkXphHwegySRxIP42vLeuVhcUzdvPOVOoRcA5jhriXGP7v9dKO_yly44BH2U0bVo6J9eQ5QCvFTVIC3TqU9_O_siBKlOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHAFBFcnvXuewN6H6Mr-97u3vLAllyfEvjUOEngOptXF5VjVKD77NsS_E_iJrlkMXWZ556Xek-drGE_lpy04X2e7GNm02uMBa_7gEOvaNEICvH8rNFRbbKHHy-uGxfM-zaoE7PRob_v2vIgrJoWMO0H68rVbtdriag0Kdzs092EgMtSY4V2BlB8B74OmjhzSSclgeb3xiWhWdFZ2LGFRgSdyemtnKU-n4XgxEEeyuZCi4ers_RYpaHxp5Krsxs1TKMv8gabADvUDZjnitiv8wbkMLYZfx3sS6udYvyeZmheljitgGWmBTPbWvCdTk_8vuUicl7xRFQRIBSqmO6ojOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtGw8K29MtYV8qwafr_11h5bRz6yBfjpYPnJo9K-PgOF99nRNds4_kh7tDCBMimQ2VIAYyZJ6MeKqpjKoElkijYzuL1fz8V2CYyt5ai611SjXFP5-vxBeoYPNdhEiyXYWdECQ_TqCp7nnQWACcIkH55rpVy14xSsbVca3Y5jetrnO5UIAHljd_hm5KaWctJmYDCooAtvBQvSeWzE5rw1xtg2dYy5iHDZ7clmneIfABvJop1DFKY-vzdiJ3FVTtoLD81I_pe8ZJ5MkZlLA85k1wMJkFCGHnifJCXyNvt-FxaTWAIBvRovrTyL_w1QDmogThlhwlpnDyeDz8_OrnSKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tj2twco5ejiuMHZ84JP0wcvFlzHd7OaXlxdfIpaMcczC4D1C-5J_hIgplXGFT01_etp54A7AIOM4fCeRPnaVfBSPqEwBPBJ1e2rvOZLK-VXGwSPZj_6NlvZ1RAJK3umTBccGpce9VWvbP3JPhnYnSbGfeB2T_0jmKeJkxOtQVJHEfZQ-yocsV6iKHjiYnNZ8Piu4b5l8uE4oOuBDb3rYD5HzbHrbPcGDySvu8u3HEToMVOUU7PQ2WhmnIEP2lHiDji2C3jMI31N76zt4yMb7CcYvezV0OEDT7yIQGnEUJA_wURgcOdK7pt9syCcCaQQDJH0_7hHif6NcIXh8S9PUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gikmSGLqJGCWopa-vcotBpNI08bGSoUBEUQ7JQi2Lap48K3EZyWJ4y2iF2wq75F0Pvuq2stEVFrE2pz1LGmuJbdGjkA7dTmbSmDjYfo8e3XuruGJfhlP9osPBY7u-H06augoQciQDY7Gw3Oyh98Xbf8eHhKkZZ-HzKS7TCxX3eRyFRMW5ofAU1sV862scrND3n3RxpjPo_wFT7pszW5kBJzv7PlawCTp1rRt_bhnkOLEAbVRvNvRkrACabV1swzmMEj12-HkrvZ2QqSP03Kha5fJ2R8jR0PHf3i4fcukgbC4Tpp_N7h7Tt6sA8J8cSVA1RNn4hVU9fvBrwtWRhrrqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBsRqkdqM72B8JE-ckFufxObNJaBFXBVYr6QoRBdWHWtMbKAaBKe91gju1-ecvjyNhOhCoqvRp0YhnJxfJo2sBRFIEgnfMnpBi_Pa44v8U8bs3kDIF4KzBZK6f4T7JS9cl43nH9oIwdVf2fDSaTnil1EkdpJ-aeqo7sTzJNr7TfUamvCxaKNna2ULO-Gka6-j0ZyLkDjQIVZW1xNYTNysidFK-DAJ3D6TCDI52WwKBlIgd6ozFvZgvowPb0aZfn5Ex6jdDXf-yEF5OeWiYv8JHH1o3Co4A41TtOUnpbQsn2mSAgCEVu4bl-ZKvNMrnMZxHPPaUlKc9yPyiMuIfnRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSckZ-TBIiTdoOxEDmXs5ytxzTVe6-XRoW4mCU50uoAiaUo2gcifF-ZFbYHi56cmwbaLZ-13ijgG2rxk9fWyKri--0N0sMCSDgnLVARR7D7SCtNz7JGf8i3_YZ8kdtS3datfRwgrQKff2AEgO2wzMKWuERqR5JGpxk3yQXQQpO04ymIvA8UZ0fR50b1NJ2-cUTHwfHT99nT2lATViVs0xjroOYcI8DDPycgGZ3DsGOXhRoSJLjGIVQpcCDgWkmFY8jIsfd0Rws37eJsV8qnsqZkxGl5m3E_Ekc6VjqHA3i_1OK44q4xlb7synyfzgB_2Kp_dgZ6VNgpB_bkKAlQE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ1k5UbzFqqvs0wJl01nz9jJJF2d1O8Qzw13R5o31_OAzoewIa7VEvd8833-vddTL8gBNkKFtQy1Zct7FZ-WgO5RWdXuXsT04iomza0KlfXmZUkHADAWaNanMeZlcSm4OVzihmNi8wS4IRMLT5mTEiLXgYo6mt0rfaoUJlx_-jDoCGmEXUc6Nod-7ceZtP5qRb6iB3jdijhkkZQDecQB6YEtNxLPg0ZGDmfeCL6UWPuwL67ApKIjVKWYWQ9EhVOz4e6SkQY-6mSB7TB6yRXgvMoNAMXR2FXvTNQ-KJPTFMZwUtl0qhGZz9eQsxee0Eqys1ncHXDLFWZv4PWwZG6rGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-uYIYkUxeuWcMkQ5Sk4QuOMxV6E0Mtyifht6gYLv4p0Lx0yAOKqeP2tMtK7r7I-znH_ph4PE-TR4cKtid54Q6hmIv5eGTcmAq9etpUhUeqaq7WPKO3Wtog-_t6GnFW2dln_d0JmiyGKlstkrO2MaOqrUyDcu5pQeZBlRIx_EJ0_ahzFfW55NxOUSK2D-lrDIkxxl4eTtmwXO6Qjcfb_J0m2xFW8VXCvYTvTl1NC0QqOzESHyhtXFoE8a9GpClHH0avfxcaJyTljeME8iI3DyhxTTEq5r69tDXT1i2AacTyckCnf6o1XOaf641W5vSAOmNNE7_3s4o6Sxqb-g0lI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7sH94k4tMmPxpeqIS3PsCCsS64reOf1lH59D3yf6gMmG0kCGwvlA3p4wnmPHnDOV57BIT270R57F8cZ5W-crXnCFxg-_RhzyXC3IhwGnW8MJ-ainEp8WLOqiAEn2WQyJ2xc7U-U_epNGB3jJW6QxO-h9MjD_U_Kl5wJmCihl_yA5wZJ4KSYy0U8kPBwW1SdmAyVTQAWYEAYt7u4-ktP4EVTMKImbzUK9t9QkIuweMmlFyk3-3Q19ABn0JUC3zGlG9-IZJjtofndl5zavJx7_cwA4UlLiYll8F1Inm9SyMLlt1xcLE374blQgRaQKocf2rPEVn9NaWuXwJxF6gMWDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBB_NlHTR3YNdWknY_vJ1YZWy1boBzdN723ifC0GDqpiq6Dtpf6ctwRhxDiB8dk5Is_tkHFxjfM0JZi4ng_-PF2j3Yer5GrFOvfXC_spTb9sqBe20qzGWGyJ1hc3IvP5wfQ3XWQ48Cbo97idnR1xvWYQEQJFR9STX4z0BOCoCGq6ZdjjkAnuVTynW5-qShjJWV71Yv6OcykLSLqio3kK5Xh9cjIVnWCaeC2cl9QpNhxgsTCKMJ2-oEXke0yExE771qOg8G5iFU3yhqNQY-1ybz8Ez0yv6lWr7eP7EU37ZCwXaAcKSRoK2Njneqk0oiB7qqCYRrNQYJhR-lmW8f8nnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2p1Oi7pYTDsZ4gV8VP9ReEE4774n02xuz6nXIMJg3PAQ5VtFeUAzMUVUBFcO2XB_ZeILgGRSPcv65BFwc0dEpuA3STSMJsX1DJoIoeuhh7y4T-y4vuS87ACM_iZl38GmIzC6DEVBrWto76tZQhG_Lnh0VLD9hJiXrDJV40Ozn9csOLBt2rJVxswix2R8fa9ehjUT_FxWb2jaa-JlLrSg_Adb-FH74pVR9ov11TxB-rkvlKV1gfjkG_DOJ2XKcZdv-DRi1gfBuEzzJJzmGu4CB0ms-Wg4v7uGUmIw5I1kjuYlazobnSZVEV9-t1zRssZcKA_zGkswvBsSW6frK2Iag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WviFigk2hSciDxGfS9_7T8HZRh1DwWRJciN9VYQmLR8YOBQMD2Jptx4Y5ufs1CehnOKZos8rz3lhXSmGCoX6IaveLyHB4KgIcPcvlwMpC_Osq-TXRDmJAdhMjChP9JMyGImufovgIXBlXZmwstfxFDKx0bFusWHyAuqUHluoSxIFUyeuLrP1CxrqEPDVlRwhr4466ukUeh4BbThIkTcOAWbecnIWTzsTFTNfyfZ5IKzuJkS9PWdTSrenwcYaSTmw7umTB7rLmCoNkhhlfZt4WqizKsacMVolSU6YRC0o0Zxj8UF9qOBxC-vZ4RXN5wbdEpr7aEPr8CRPiNQOkFOb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl924-BtNGljyiZgFdeoJSdS4dPNnV5Jifx7uMIV14-znfvRPvAlBBa6Tvh7jgoV7xKR8vvPVhgHOWqH4lCUOarD76aVIfn83jTVGegtf2v637Cca2XPrC3yTmkKnZIgzBFl8aVTl041T3tlrtsemya__2wc8uNIbIu5DlzPUhLe4nSQjRx6448HYgklHFWEVpV2rntAABgq7KBHmTNNCVgLVaSvRoJ5lI4gxuFyxpHRqHtt-l1j-WC6FmCVtPOO4W5X5qbLRKbq0WSVnTuapKsI2czuynbzNnLDaF8v2TfxczI7eT2hTMipkM8FVZGWAYlZzguQAEQsFkHYypMmXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzthyhjs7TNiBp1MBgm4A8R6m45llm835AZPXW2_S5rkROciQ5jHhEqthplR6xdRKCWOiD73iIBNZXYPDfpWuHWZ5HK0ZzaGhCD5vDP8QpfkkUdNEYHJ_IvFDhHwdB31M_T3-vxQabgYBIrphCog5ixhkjQRNuJPXapapVI4hXF71dK6rfvW_aeXsoXBkr2__FtTodz-k4BM0UD1rCNvLf-wYnFqIqpVUdyy0U-MuSyHbHaYxdj1qEAwDZtVHshrJJscZiYJLp94NKyf69jtVJtfP0rW2rwxG1U5jD5IZMzporIS3bbIWcXTIp6fK798Smkn_wpQ-vtiu9ElMCkl3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=V2m5xuDbeHWPFrT19-66b4qCLvH0TgckPDW84Ji6QTXlvYL_PtWCC7Yig0Un449zSCuQQRMqIDqr_hSae5aC_Q3C8OXHZpC89nl8mRIqz7g0B6D-nfv8n95VHmlS2lonHCMZtBtg6a5erYDvjd8Rs2qpMkSagO3me3_hgibD4OtS3koFr1yZMyXyuk3KiFCWoKIOpNrI9uDuzAbTkwkuV0b7PuEjlTenZARUpARp9vhiw9wKjj-gpGW1xj9fG5FsrHEFskde8KEiO-Pjqrbci0FhnSntMIqxytpB1gOw6k9B0qgbVbDCmVupqrTSbclUApYI2eB6Cexj9twLdBnx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=V2m5xuDbeHWPFrT19-66b4qCLvH0TgckPDW84Ji6QTXlvYL_PtWCC7Yig0Un449zSCuQQRMqIDqr_hSae5aC_Q3C8OXHZpC89nl8mRIqz7g0B6D-nfv8n95VHmlS2lonHCMZtBtg6a5erYDvjd8Rs2qpMkSagO3me3_hgibD4OtS3koFr1yZMyXyuk3KiFCWoKIOpNrI9uDuzAbTkwkuV0b7PuEjlTenZARUpARp9vhiw9wKjj-gpGW1xj9fG5FsrHEFskde8KEiO-Pjqrbci0FhnSntMIqxytpB1gOw6k9B0qgbVbDCmVupqrTSbclUApYI2eB6Cexj9twLdBnx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI8D95Ae7DwaNTjgGWb5ZVW-4AlSf-5lCNOn0DilX6QEOERiGICFLAY9h6b39yepN0iCB2IdWUoUta129iSxdzPiHj_BEHRrqapEMUyxJFyKUP__z-f1zRM-R12yj0PgM2-bBShPFNLE-GMJyXjVWq700KCb30TLGv9aKpK7wDIxe4CTlXSrZfoiSPAw9ymOv31aCVjcdZvPniNwW9doaJwD3dDFVu1PPgd1f3syZjx-_Au_A7r-_dhkhQEFVS67-WmGqzfYJYMUuoPr09z87cPr2jok7NM3Ysy71tk_Ebui3UoC4xYeawpNZ-5b2GXV1SsOHCI8gJpo84vvqI_-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVkfbPETrSPl9fjZhanAHk8f9XSgC6eQCF6nZmD_nA8ZH_K5aDFltPW3QRy6ddsnKb-NqkRCWl0otKgPyh_m50UvHV4GWZgxL2vN43k0kyKD3e3Vvuv8BkqJ2P-KteiAt-9v0SDbcCbE-e5BQNkD3P6WeEx42H08fVbaYWPq_7chXU9Sb8zpqOM1bOrCXUHgd5dpv_9XypAKzoRHTykCCAX5PXet1WT3fl3_PxTgyYwA_6Si-oERgSNSkJSjl51Ctc83fJRtHroi-Hv0DJNvOrsy0aUDgDlLScvnvtJfDVxIB5ktUxBg4uBZmnyA7JWT6lvnzCp9We-23TAy6wiTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPsOikQ7mAZQ1BOSEEprmRTeYzGqHGCDf8wSbmN4nJ9NFQd-RstgVy3OJDDkdcVAbcmMxsToRGVicQua3ypyuJGGLmIl1lSt-UO4v5Cnjg4umA6qWSfIHyDGR_pL82fqsbyISS5_yHD3e1WA_cwwKXU_shu2UPE51o2ajQm6ttbvC9j9ey-B2FaJ18iWZYi1z1kyvTbpZen7atCkXMwDxS3j_h0blHj0GTGpRkvxL7c4fxRyVo__dYBKSwvRbOqdr2z9K2M2nIEvotx1NlhhJw2p2SAQx6BlE8bv75peSuS8Qvu_rCwxz3fFF9JG5DVPUe2gjgpo8vrTGcnjlvEsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPoSQOSGWz2EsrgAsy3ltv2nFO10uMfv3Qvo7X-elUIUmGEJp_NBILCMTl8HwAC_ivG2lJ7e-L8L63i54AbtQ0xGrr08XF6wOYj1h1XhNShQLefIF6l79zaIgjbs7en1BZKVunQJvckW1wLu3qOoCCDhyi_wXZiTkE_v5y2bK8jDSL-spkjAuyWCXNb2fE2cC4XHo5MZr8VNK4ogiLejUADEdcbDrUwXEoFqn7a9Q0q1o6aLjo-OJI8tJjuREzw-rhlrnKFActZEwijr4q9iadbaC7emu0mzFFTNSmGPnxwFGtme7tL_dxhIuk8i-2oUHBbN77BrrZyibyOiuMZ0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taUjsqXK0WGSgOC7bf5rC43O7tkv00xvoi5zOB7z4yW-20oFnP8qDE1p3uuxM-6X7IdrzqNSlsFQM4RHJBFIJe1QyzNVn5ckEIRYzZE0cAZs9TtFnUtW282bFLjeUM0o8m9F-aws9ZxkqXcIEL6BfXpZzD3K1xbLlDl3CgDwlFJ5J0wI6T6D06Bia1ohSEhgd3KDOZWhkUSlMejW1Z_P8isS-pOGQ9YBJkkHkm6iipblrxIpMYNoicIf2kIpKPngsLzB8FiOIT_qMvtnji9m0HN_DxGMaJNI6efPDOlXM6ICLe57dm11LzOBwhwaXQCihRdt6MF_IYIk9L9rMHrB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEEnEtp0ekHK5GqfDSajPUnhTFnYDTRmeVvJIvGSqOGGOewdGmcBdnWwGHoDBE6Fw3xxcIyc_cHYk6yt0ifXWpWV9TMf_tRO6BQ2ZNR_QmU-6Knc90KsbSwgAhd9IBq-6R3Kqmt4snaEsLi9px5wJ7uX-ljjBRznCirSxo-O5RxajgTqrmChRzsPgCGGlUkqPovhHXMXmNUhTVP0PqnqG24VC7uk_4NwAO-YyDZRZwUAu7Ui12lwOUD_g0J545N0OuWDyQgZkqH3ZlXMjJ0Krm7a9-IueFEhnWZ-HTJNzgHhhkZyd7ArnYO5ak59lG6RQpXckw0Utne_8ZvQ4xDxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg7WwL93B4EDP0fjfNHkgsmoyf6K1MTLqu0ZGxvTME63I_39mWhB0Uyr_iuF8RyF1DDD2CJ8cyT4yzf2hm_QyshZRga2my2jsfRBXTX-8q4LAxjliXgrk70ZgNCLrfJLyJU-N2UfEpJqY-Q8YqwsIOwXYtnuX_GxUKC3z6IQ95dxzT6WeA1ak5U49iIg8lzEXjKP00lOMGQxbezgZ8Rx8_iVUUqewAKDIBt6S7SSciOByF0J_5_aL0BMMuMGa5dpoksyx0IRIEwOuE_1i-JfuQ6aX7a4xHm76z5_mYoxADIXoBbkpran2CJqkGhu95Vm38ogYET1qvrxnYo04XzcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgJzMVVGzaZrC2yQ0RMnOLchH8FTmMs0TTQk8w8CmOnK8OFhsFBUJK6dVeSKthWJ3lhI968Dwm_ET6-YNGJ7x2HKbMjNh7JD0Yr4GcYEhjkyI-AqyDJ-W9Z-A5uMuUoT0e0tcqqGrtQVLD5Ul_VUUHKruCdGoGZdXl6EVxgEw8B_Qy9vmgAr3-fIO1yx7TxFcrJSfxaCfeCsvj-KyOfMAGDLC__NuCgDdRZE1_x1__wqa8A-Pag9wa92IsOKpyVuY5yjdceZQDr7XEWZ67aFmXn0TLydZWmL5qgL6y_NOPgZovFnPHUf9ewSXyiz3uGnMWV68H-E27mSpA5NQDeOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=SvxgymfQ5QMmjju3qxiK2LZ7d4mURDNDxBKR9f8-9JWl87mC80dnCONHw14sDpkXxzvckF063zO6CHiMQdVI2hzmwbkaGUrMdCDb1iYwhgILOrNiUe1Gkbwpv8L-Ym2XQEzg4pHYCTzdD7G3NGo-B7vklJuId3DJGSZjb-NxMpRikbH2EITcjGgz5bEsLRa1H9VYLi5rLjpt-hleFqcN3sj5AV10ctsN7yANhMuShGskbXNz3I4JNtIei3Q3bGITf3X7KqT6GAqzmmJ8BWFBsJ7okEPlBOFRrjRguiNY46HCnWtpGv2SbaIuRoZqlnAXc2CPEcMvvQ3d9B3NsAg3YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=SvxgymfQ5QMmjju3qxiK2LZ7d4mURDNDxBKR9f8-9JWl87mC80dnCONHw14sDpkXxzvckF063zO6CHiMQdVI2hzmwbkaGUrMdCDb1iYwhgILOrNiUe1Gkbwpv8L-Ym2XQEzg4pHYCTzdD7G3NGo-B7vklJuId3DJGSZjb-NxMpRikbH2EITcjGgz5bEsLRa1H9VYLi5rLjpt-hleFqcN3sj5AV10ctsN7yANhMuShGskbXNz3I4JNtIei3Q3bGITf3X7KqT6GAqzmmJ8BWFBsJ7okEPlBOFRrjRguiNY46HCnWtpGv2SbaIuRoZqlnAXc2CPEcMvvQ3d9B3NsAg3YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWhUZdGVEeCD0Bor1grUfaIlwf_1YswtX6M9WnWH-rraQiIhidY_GrsxaPXELbXtgVbNwcXDt3J6d2avsQTJVn0DknquCYrhlaw9GkpQq8DU6pQB92V1ODzUe8jCmiQBIJgeAd2gLv-WhnQEuJ5KzoF6bust865um5CGcBKK6UDxQVC1R8ABlSeSzoKiGFI0lOQFJZCGYIlcK56rjZeam10CKsMtoWr9jDO_C5_MYFjadtxntIAfkTvTPRQiSE-nES8T-F2a3_TbU1kVO6cngJF0hL3hRhzWEEneW1vRo2En5lx43TKokThPx3hIlvgOfiVGxIeeHdeIysWvZi6few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCKtKk4jQjxRZblQwixI9Irf-y6S9N2hNhzHf1VYerrnkMfMcSgePb-oFhBuk6-EJoSsnfCM8RHEjGJ-YV01SZt5UHwbv_ah5S_6bm5d83TDpGLX3Jiawoe60pENj0NEuMCzMWMitvXJTceKYPDFeTcqoTupZJgBMRjeJFTeAB_-GYmZbMmzOl-nWWsDsvemvpaHWYb-WBMa5TG3sq0zehWzHIaRoCB4Cgl_onTT5tzrnArG-OaqQTQj-2I-MTuoo9OLdK6KIHB2IMOsRTxIP_45nMc3Q1rfNQDnqWVO-21YQpnnD-Bv0ifWgCasujQYB560nDGhmYn80B9bIJv9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kykgiMGEeDs2dYO6co86U0ZEMahSDO9zJeTgM93hvnl9i5LJUOWu5vJgawDE142CqMQH98ux3ygS_aNf2syPTi6h7V-tSihGgxdsLQiZD3qj1Wasah6giI2wZ2L6H1aV8KosiJSLUdUJzYECvdv0-6TZHsIMJ0d3Dr6sBZ8E2sj-rVsw0_PQcImWTPdmSfxo7mE6zV_wmCncy5vt1mW004E-FpfFYMjHctq974TVtBGGAzErN3B4uV_PJCSEiRnXaObTo87lb0-yYEHaO5r5QOYRpblxBeSeniZsk4TghIMoz7zx-UNTGqfoIfdwdmUK6RGm0qN1XHXraPoAN9eKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIsgdrZitGRUyx5HF2uG3IgmTE1n_O3ZN_w_DmmrDpXI5qavunriS_p5BS-zJhVmm-5SNCeBYid-mZ9KWOBEUwKbvlMNF6t7Ax3XNrp9e7qsNSi3lRVrQ9SQ-Vsbbd8iDPRY-JoLtrDGh28nbTUcS3eBJge9R7e6i80sS-e_zIQN63BfartYNkbZFYjHvOoHLCtWu5gVIGzbNiaQ9tBn9H6lorKJNgMS0O7bUbrdeqz0X_4vnZR0NQug8fvYygVBQ9VeCl3cy0h91WsDorYNhwYDDRwZZ_-dhOLjya-X3JkRIHic0eos7J7wO9RpYxEuKacTNFTN2-ZJ_S3XgA4_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHEozuc5XmRNkqoCKpMSqlSUo3nzg-t35xFhBK9BLGSEO_ZbeVGwvqPB5ZipgqYXfteNzeQflW7Q3r3_pBQ37aJkQWZ45Xy0U9JUeW8sRDoaaeB3EjGTWCmkii7YnVp-UDHQX7wTyr2vQlcnTDt5EpRkuwiqzv9JlQ8Skv_w014-iQ-d56zZPF2thZVXGkpQ9e9iQdtV0oOnEj8vrXnKdpwanqKLw5DT18uTwGWA7drnI6mamwg3LoA1PFcLQXel_-I1xe8NYplomghApOSP8cxfoMha07xF9FftTS5r7JuNSVF1bmx9k2nGX9T2PFJES8yPsaDMEH7Ci1QWiHCp0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swQC21E5aSeNCQWlxrrz2prWL5c-ten38OO4TUZVLP9gekyalwC8m5pjLGc0ImEnYbMy8jWsZnOUaVuO5mRjKuWshVs1KK4p1wdq2zkAGnZ9qBooa7jaQSAWNe2HvQcml92hKdtTOmYddkW9SpNF2iIHuOyeqJVzxmaV5yYtuzj9TtCZHh6VDzIWd-3GDjpixapkw9EhlnPS8tzPxgATHnAcwXGxSkdcG9N-JGBCGlIG5-lcBOASxhzVooWk0gcoPOonn_PbpA2L0rlTHLMmrMloLKnroH_Wz_yr_I02GFQpYza4_T6RbhgEqHdrY71Rv5-fkmFCTHsBald5XxJzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1bC0AF7jnZMctdTI-qWvn8RV2dog0u7fATOA-n5SxrhNDLMlBeppbXAggQu8ijhs_IxERv8JXE_8ZBNWK15mI8z8_Ukgciv2bI2I8vX240weN-V380pNp9RzbMzwwULIroXYuueyP_u8TEMeVH3mzWnfYNY-XuxiCRG3Ay4BatvUJwIXYD93x46KMtcR3l-Sr0GPp0juarVqO5QxRfx3WCRw9ShAYu_MTmJqhd-2x73OpjZWZUOjzseX0TV2VRPVBBgonhBxVj3Nes-lyypBZRHhuV1xRou66D8328qeVwZRa-gj_B8af4-LfAVxNstTW51tlZS4YfspRXnZ7v3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=QeaamwwWtrQqLr2mGssYa4J8HKMyr8E2IgCzm2DdI1rcozbi7ImLPEW2Ls5jzjwQo4kQi28prEZqxYja4EsgXWeWxIqqXAQsUoOgbbenKMTBcZW_yL-d5uKRjtaO0XeutM0GGGEkYvvR16_iSPllMx3EQCj1V1y7XZpArnyNp8Bsm_jvVcTVsEtfp-8QOW72J3yf344iLruipg9e_6gUQrRmI8gaw4Ihz6tc5hei35qH0S2AkArOwD1CjwQIHX_y1XczvJ619N6Cvl2BcczOIz5GZUP-nHMJNiH21jH4rzIGTFeSMdS8cphbCIvF6ZrZjyXOoGl3uhEhO6LJcmO7SjDkEuXqM3GYz68-NoSlzegCbBouVlYmA7YlFVboqZcomtyjdFIkgcLBzFZ9k7MDfuhmWy7-Ede-8GmNi287EHpTHA6JZwtamw89QSVxRjg_IQ9kMr5iPlyyZUmjtHIFx5izLdiGw5Dd-AcAd4O73wCB7hdy7kmporRdbrymKb1nuzEkyQESp6ut1NNkBgacq2kSVSHK_ubT4X0bZFfvsxeOyGFYA54EycyuuqcwytH1phmMaPBzJfbTZJupZiobtZ7MAr0Kjfo5E6zuX7K7KvWVKb6bAiK-UUt99l2FYGKtck-k-JiKbMNopTD9u21rQqAVIu6LkC_wwON7VJpbcOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=QeaamwwWtrQqLr2mGssYa4J8HKMyr8E2IgCzm2DdI1rcozbi7ImLPEW2Ls5jzjwQo4kQi28prEZqxYja4EsgXWeWxIqqXAQsUoOgbbenKMTBcZW_yL-d5uKRjtaO0XeutM0GGGEkYvvR16_iSPllMx3EQCj1V1y7XZpArnyNp8Bsm_jvVcTVsEtfp-8QOW72J3yf344iLruipg9e_6gUQrRmI8gaw4Ihz6tc5hei35qH0S2AkArOwD1CjwQIHX_y1XczvJ619N6Cvl2BcczOIz5GZUP-nHMJNiH21jH4rzIGTFeSMdS8cphbCIvF6ZrZjyXOoGl3uhEhO6LJcmO7SjDkEuXqM3GYz68-NoSlzegCbBouVlYmA7YlFVboqZcomtyjdFIkgcLBzFZ9k7MDfuhmWy7-Ede-8GmNi287EHpTHA6JZwtamw89QSVxRjg_IQ9kMr5iPlyyZUmjtHIFx5izLdiGw5Dd-AcAd4O73wCB7hdy7kmporRdbrymKb1nuzEkyQESp6ut1NNkBgacq2kSVSHK_ubT4X0bZFfvsxeOyGFYA54EycyuuqcwytH1phmMaPBzJfbTZJupZiobtZ7MAr0Kjfo5E6zuX7K7KvWVKb6bAiK-UUt99l2FYGKtck-k-JiKbMNopTD9u21rQqAVIu6LkC_wwON7VJpbcOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=iK-asbdh1GRwjAszZ2-eZmUsrRPprBCTLPiGE6a6peWNWx8ouWa08ke4t9wh4ZlyQknvWKAf6VS2Yc4YB4ICufWSCtSZhGsImSGHyItVbC4g5k_YXLARF2I8VOBqIWO43NEoJ7d6Ik9-Yz-bts2kW9q9vszWOPoBBFvXbKmraSBEQ-Gprw3ZyWcRZNOOqL6CHvK6bw2-19Q_g8sAnG4u1KI4HzBk6YttGYmBC3Fn94evu8uiWXF9Ii32c7CGfz5qzYFSurl3UKBuMnh1Eb5PWE_x800Y5lfCmhXbSsMO28cw-N1VKMlJEL0wUrH-kyLV1VQytZnzXBUjiTCW4n82rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=iK-asbdh1GRwjAszZ2-eZmUsrRPprBCTLPiGE6a6peWNWx8ouWa08ke4t9wh4ZlyQknvWKAf6VS2Yc4YB4ICufWSCtSZhGsImSGHyItVbC4g5k_YXLARF2I8VOBqIWO43NEoJ7d6Ik9-Yz-bts2kW9q9vszWOPoBBFvXbKmraSBEQ-Gprw3ZyWcRZNOOqL6CHvK6bw2-19Q_g8sAnG4u1KI4HzBk6YttGYmBC3Fn94evu8uiWXF9Ii32c7CGfz5qzYFSurl3UKBuMnh1Eb5PWE_x800Y5lfCmhXbSsMO28cw-N1VKMlJEL0wUrH-kyLV1VQytZnzXBUjiTCW4n82rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGtV41pI_9fPAWch7OuDx873MYgxAWiM5GF4ODf72u69Y_d1nsqeWSircdthCd6PY_xqwLuuL2K3PTIghCxo-N64XXA4MiJwmrFE9hKRvitZEWGvqB65GPEhiCfJIk1hGNKg1N6j6wR2geGNBpYGon0IKRAJtci-0qToRRqjXSqDdlKMUuzasYhwTZQ2wNVi2O0NY4QgCXXdRA75qXjB8e6DNyT17WJduyb4t5vjeEq_Evep9gJndbXJ3mx0-4hwh6Iph_IWm6jVHvigKCCPOVYGmhrMH0AKvutmNGpvwEpUi_rQ__I57Z48YMEQwL1b8w3DZOubhXMc8Xp-dfq8hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s04vTgk_2SiGEAG0lt7tYZdWrYxZq5hPC7zXmbZymgU3oiMC6Z6qQnw6WrYXB_Wkt4-s1KXv_YekfNTb9AFp1wX4Fx6OvGpL1b-PZ3KDYD0ubMKmpkhQbw_GplBaBT6yKQMjxhRVPCXFm8A7xrRti-OESx8j5cXgkWwoR2iGDm1YFeHBs76MxFiiday6ReidZbS4fLe3cSQdOZB4gOtbobh9opJ6qicCZ_ObJf4kM8__TNYm3JtC_z7s1AvBa6TLzs4XQp25hJomW33Y46YzIDCZwyyjYO75OZ9uadgpyYcOSKjN_pSA-IYEFJkROXXg2S_8Gc8f5H-J5oQqQer0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=P9cbKr97BxKMv__9PUQxTv-fivJqhsvlOAC4SOH1a5Lv6i7sthHNENEpWfHRXi1OKcvtflEVYcP-P7K7tQT2MtRSJVCGccUQKBD4WCrL4z_iSOIjcoX3OBnzHtuzu877wRtZvQNRNsUDLQzCpAbdfmzuF7WMLxz3k7J-dt3mJPR-WSGlgSNORCoMREtOXkgVk3Ic6VMhJmvHc1EeDpZAgvuHxeGK0AjTfS_bRHywyc0KtTkedZsjdHn42-Ju8wnXhIY4AP9qk1o4FjTcVsAGLxkLloi3STK86uNXCXTi12xU6_If2A0WvxwzECWb3phdBZnfEMNURJsVrfW3fympxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=P9cbKr97BxKMv__9PUQxTv-fivJqhsvlOAC4SOH1a5Lv6i7sthHNENEpWfHRXi1OKcvtflEVYcP-P7K7tQT2MtRSJVCGccUQKBD4WCrL4z_iSOIjcoX3OBnzHtuzu877wRtZvQNRNsUDLQzCpAbdfmzuF7WMLxz3k7J-dt3mJPR-WSGlgSNORCoMREtOXkgVk3Ic6VMhJmvHc1EeDpZAgvuHxeGK0AjTfS_bRHywyc0KtTkedZsjdHn42-Ju8wnXhIY4AP9qk1o4FjTcVsAGLxkLloi3STK86uNXCXTi12xU6_If2A0WvxwzECWb3phdBZnfEMNURJsVrfW3fympxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNy_2tp41wbjoABsU4j8OTum-4iJ1ATM-IXF_oWCxLtzROLqqIO3-KAIYnwT-z1Qr76v_F6BY-2nw_EBDMCkwiilGMRpRCjQgEoRzr_xV2HYNAMCiczplxcpSpJz_zbmfXL3LkS5sm7_1uu1goTH5Aje6wgOOoL3fawQLzjsh-cWCtH_NOWKOV5LK1cRBvXiw8BuHfbjOAwYX0AwxlcbzOWTX-gQoBB80Z-5MXViUqxTXL8mzrlgpu_mePrTxnVhITt0jZdmepVncbpPI1Eb-t0DbcQi3i2dwO1uoRoXLdB6LlAKAYK3lGJ751wNkADL1icNE8NzWdmsK1rcr7LTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfn2jA8zOfUgLBQa-J2bHdVg5PdtImt-0gz3bu_9I_GCG4VBEU0FGlyvDhLiUbwbe5sheMi6LyYMFYleDqbd5QAgtt3tbigfzvUS-piVUA6aCOP4eyV3oNOkqGHcxDlRAbMAe7Nd1Rp9jpbLTXCZzUQjUAHY7E4UOiueZeJVbkR5pRVr_kZL6Ft70n6xKmJ9yz22WVoq_0ftI1cg6ZT0lWEi70kiQ_KU34rJCTqm1Ls17hZ0irQfqTCrikkHoPymoZUBsR-KHCp9bBKK5nYzYf3tf1USbteepha0KyGcjjkdknWJCmm5vqJGM8hd1QQnx12LzXXeUkS0HLO5FqGrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AreBeQGLk_WmZU-JGExasEFLLJIte2zZODPeE9bWk0jxuyixYQcbjucdq1ay5uzFo6oF5DXtQnuJe__RqyVOS5KaoegeBzA8SbcENAB_DVk4CLnqJM-oIKnKClCIy1KO1fVMmNIKZt7qZcVTRi77_CoXeH_14AH1LcyAjWSO22BEKbVBz4rBl2h981UybUPpSNpw7DoYttP_l9Bo5ce0SAzhkK1r97IK5inoF8a9MShAwFlMcCVWUJGuZmiTi1yervX8vSF6zAg_PEQkmT8q8HGKLEwUI7J4zKFncAPILJ2gL_cZwrMj0yhu7Tg5QD_WQYU1vTqiygOx7HY_9PQLRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSWlB-R6xD8qvNfhQxmD3z2w9qyJ8Go0zXFwmGJLh0hnsnw4y68ItgWE5KsTW4SGlpIK-_KPcoAH17Fj8He2_El6OqoHT__JzqUyPqx-_ENQeiSUAd6G-44xSrgheDL3rX5weVhHPI7qhfJpDknTxm-YF0K6da_5JXkyg29GE9F0d6KFbr_uYsCfBXUYBrLhKzHj-GfVfqyV8i_emDwxVjvlw5aINexK0pfXN45sPwjsIqKn6GVvz141J_ZsfaHX3Om6WERegzSSAd8bsHA-c-G-dOCpjfRhn9XZpRiU97wU2feiiGZhhZlTzfP64nuA5S3038Ot7zWyVgUN4NU7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppR96Y_ctH20TwPDCWWVwSie9pnkZu5444qDVMljHvN2OYyjKscu6Gxk9vgtsy76kTYu42P1QqJiCNlcuUq3T1amT4qEHeqWR-x6cMFQNeMXJEJkqBsA45Z89WLo3LBEZxSksxOFkTEoUP3PVJdB6gyDMpbBbaDqA22LSEN6lIGGEJk8jZxhU129uG9XUqEkUoqUPiokwNBn2AqrGPM0VVBwoIXC9_D_fcFuD4MCi0EAcIuRTfk5MJ75w85QITi_bPGzJlfJrzAi2r1A-eUFCtnHh9Vyq0pLu-Lnq3PZkXmLa27kH80kdOtS0u0m57yTbXMphFct4GnsP-nvyX5Tig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJTS0D--PYnZPROuM8zIjd8cg_PBzwEoMVfxf9DSHTQzkxp8ZWx3Ovt3BE-wTWQ-Lg3im1QdLAdIL7Yu4lOPd1WCtjlgG7_WQo_AICoFmfc8Fu8hpM_whOYtekzcvr6J4ZB7kzngTjF959JiaHTSX-tAxzgmqHzz2QXxaiGflfpwJE_bTlpGUaIKsN9enkAqJ5ICyaehSUOcXqmP-Ab3r39cT-e6397njs0BjEcK2NFybAY0Ink2qdFShQszfGoV1FN5Qef_faFTO7ErRsfd96kYOKqMMeDkq4lTYdzLhW0AtAxn3FcTj-wiEUo84laf2EDDjOkLF-hw_RgzJu4HMnVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJTS0D--PYnZPROuM8zIjd8cg_PBzwEoMVfxf9DSHTQzkxp8ZWx3Ovt3BE-wTWQ-Lg3im1QdLAdIL7Yu4lOPd1WCtjlgG7_WQo_AICoFmfc8Fu8hpM_whOYtekzcvr6J4ZB7kzngTjF959JiaHTSX-tAxzgmqHzz2QXxaiGflfpwJE_bTlpGUaIKsN9enkAqJ5ICyaehSUOcXqmP-Ab3r39cT-e6397njs0BjEcK2NFybAY0Ink2qdFShQszfGoV1FN5Qef_faFTO7ErRsfd96kYOKqMMeDkq4lTYdzLhW0AtAxn3FcTj-wiEUo84laf2EDDjOkLF-hw_RgzJu4HMnVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRfwYndxrYrd9JLDlk5fAkGvIKCGUJImPP9Sw1S0LleKrrtR6eN9F1jPCB7H6B9lzaSLkT7NoaQ12qpqiBTwy9CkttPivZZgH0Py8Zx0iEteyBMUY4j2tEt-oA3DPKceebTMSBq4yirl1JnwFnflMQVvqq8X7k5uM45zMcVYbUcP1it1GKKvY6kQXEY090_lWAYxfDjNb0tB3FrhdnU4s0qbicqnhI4UIrml1Pi0nwJPcAnrdsurkiE7T8t4gOjaqe1uXLdZpP0ChPs2QLYXXCmWlUu3EkTblUoAaqN9LLJfjL2p2rf7CEYhgtb_Xk-mESsXQym7KP8xz8E8ao4st9fdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRfwYndxrYrd9JLDlk5fAkGvIKCGUJImPP9Sw1S0LleKrrtR6eN9F1jPCB7H6B9lzaSLkT7NoaQ12qpqiBTwy9CkttPivZZgH0Py8Zx0iEteyBMUY4j2tEt-oA3DPKceebTMSBq4yirl1JnwFnflMQVvqq8X7k5uM45zMcVYbUcP1it1GKKvY6kQXEY090_lWAYxfDjNb0tB3FrhdnU4s0qbicqnhI4UIrml1Pi0nwJPcAnrdsurkiE7T8t4gOjaqe1uXLdZpP0ChPs2QLYXXCmWlUu3EkTblUoAaqN9LLJfjL2p2rf7CEYhgtb_Xk-mESsXQym7KP8xz8E8ao4st9fdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=EZiuOFcv6zJPtJLHlXhMu9YyAVKQlmvY_DymtOmBKc_0d1aE8Vda4EUisJgjgxnYuWuipHYm_YFBkbOZCejlcO0SD64ZJpRWABSzmeH5DpwcSxc06iNqLy870bWkmCd2IoHUE-VyJ6DLoM-a7aKbyUkY2vCf5bFf7-NoUqKPnrSNTAZ1F_9yJHJKrGDAofPBGZQMZ5uG8Ex7oGHPG1ghqUK-hmjB7UZF--CP4-0PHKO3YYk_qDU2EcuIRb0ZVHntujIMONrp_VErdvlBLh17sDOj5js_-ivWSGy1dR0V5MA3Gz8_TUXHbMOQFzcD3AJmeh89-mA5YzV2sLng_lpd6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=EZiuOFcv6zJPtJLHlXhMu9YyAVKQlmvY_DymtOmBKc_0d1aE8Vda4EUisJgjgxnYuWuipHYm_YFBkbOZCejlcO0SD64ZJpRWABSzmeH5DpwcSxc06iNqLy870bWkmCd2IoHUE-VyJ6DLoM-a7aKbyUkY2vCf5bFf7-NoUqKPnrSNTAZ1F_9yJHJKrGDAofPBGZQMZ5uG8Ex7oGHPG1ghqUK-hmjB7UZF--CP4-0PHKO3YYk_qDU2EcuIRb0ZVHntujIMONrp_VErdvlBLh17sDOj5js_-ivWSGy1dR0V5MA3Gz8_TUXHbMOQFzcD3AJmeh89-mA5YzV2sLng_lpd6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9i-HGnqBECqfA3xfYcD2i9tV5mtSrBd_SVKnUaXqXtsqFppxHPYm0ASHL-49tlk3JG0LQENnWQ0V4YuiWD3hszSkN3GJ-Zc6RoZbbP4arlQv8pG7jeeG5TAMPkqQskN-xSwgPaeMrFOp1EoZzN-sGJpHHzvbeNnCWGucpppQ4sfK7yqKc0l6vqHGg4pz0IGfZdG1uSJOufovx4SulnxsFmFsE7l0gHm65xtMF4FdFoyux4oksHHntZxStghss6up2sFDFdyrMOIZd5Jq6moMTmmCvqoXQImTwuNxmOu9Q4jH-XNzCbbf1X7eCXb85w1nJqCwIHf0J7VAemIhWDi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fokGtvPHWKtLLwL0SQ0Aa-y9smhpkiINjzEhb7XQHXDn37sn97V26xQ3i31eJZnXx0RRq8NhF-OQD8gHsyVZXCH7ZhHaf9wNYNo4_AB7a4vgVDKLyHmLJgJhNIfR6OePRcICsq_1r9RWoYXuM4Njz-7hTTssrES7u8HYTpEc08wGhlWdaH14yTXJqM7_ZKpAy85vhEEXXzCfcrv6N13-XWA6r3cY2f_BcQ7S9pl07s4TLU-qdxtgMhYjDgglPIn-rcSpiGRVZ3wow-c8EXl_2X-eWu3aQcKtWqVEluEyx89ysxxH3xBQ0TRjugaky6bRGunKJIn7nSiN6naX9E56mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NiFSVB2rMgOafvcoQjN49ue4TVesPYv9Qjd839_C3ZKXyydqbacalqvylNfaLcoo-zVEw5rKRnR6gY367ddXM5yIKs7QDmzHVUYLlAN_yKKv5ggpwrNCvuIf1qcHKQWEsvNSdNhgiNs9L_RtVrFWqKbFf8BN0klIQXQUfpf6Np1-JZRNkTW3CBeGnWmTb6YnsvBt4PtZyqfhxkbOuZDRjygjalE-r_wtQ7knXJ17lThzs4r-VzwI1qL01bUuZaJu455miV5-EjI2qUgvj_GKe8f3LWbXYbHWM5dpc45LxA9b1hhKb2Ki1C2ie59jMX1LElTMr4BkEbea9MIuxMR1sT5RcQ__Er1UZF4jzQDJs10xfiaWV1hFwd1BwUpFvhpVyCT0txlgSkt2aegaUUTMeXfugR2y4HotMCXnbO1ZNeHvKDen7ApwEoksqTLcQquV3AqeOsRXD1pgt3r50lLFqj8hMpoyHemG58WqSwPuPZxNm_Lz-BiHITTiItr_HYiQaYvWdh_uHsTPvccC4JVBgPEDIflNcmJds-XhCOqgdYAIdUbLVvAZhIimWePGdQj9BfrNQMevjq9XamfQz7VHiv_pg934IhlfqiCnj92QBK4BdHlCZmAZ1U3T5jp5aEAH0VplEcuD4z8afd-i1l4KMVlEnZzRnbCes6O4RPsW96A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NiFSVB2rMgOafvcoQjN49ue4TVesPYv9Qjd839_C3ZKXyydqbacalqvylNfaLcoo-zVEw5rKRnR6gY367ddXM5yIKs7QDmzHVUYLlAN_yKKv5ggpwrNCvuIf1qcHKQWEsvNSdNhgiNs9L_RtVrFWqKbFf8BN0klIQXQUfpf6Np1-JZRNkTW3CBeGnWmTb6YnsvBt4PtZyqfhxkbOuZDRjygjalE-r_wtQ7knXJ17lThzs4r-VzwI1qL01bUuZaJu455miV5-EjI2qUgvj_GKe8f3LWbXYbHWM5dpc45LxA9b1hhKb2Ki1C2ie59jMX1LElTMr4BkEbea9MIuxMR1sT5RcQ__Er1UZF4jzQDJs10xfiaWV1hFwd1BwUpFvhpVyCT0txlgSkt2aegaUUTMeXfugR2y4HotMCXnbO1ZNeHvKDen7ApwEoksqTLcQquV3AqeOsRXD1pgt3r50lLFqj8hMpoyHemG58WqSwPuPZxNm_Lz-BiHITTiItr_HYiQaYvWdh_uHsTPvccC4JVBgPEDIflNcmJds-XhCOqgdYAIdUbLVvAZhIimWePGdQj9BfrNQMevjq9XamfQz7VHiv_pg934IhlfqiCnj92QBK4BdHlCZmAZ1U3T5jp5aEAH0VplEcuD4z8afd-i1l4KMVlEnZzRnbCes6O4RPsW96A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=rEXgnxKugfK8utHNF5r3VFdfoaCIVYQEagvJOwqvt0Zh--sgQYI2WwAWfIDQ8XvOsLsHaSbiuLNZRYBMFqgJ_bn05i_RB6cKLwa3lLvPCtmq7cs2cPAyVXgz2uR7k1DJLfGW84g1BIFD9w45PAGnJRHWkx-dyC30Zh48HoUruA0d9lTuZYvDW5UGyoe0KYh6tTV7jRueVPuXVKwapAQi9_Jq6pDCStWehb64wTYRF4TKwf8x9ny0x099y4gc8fYffLHvn5woZHDrtWqhxExaTC1sn7fSYTHWT6Lei4tewTp_6HZZEaoNAQL63kzkonWiqp5X-CyROdzIhnuyjkJpMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=rEXgnxKugfK8utHNF5r3VFdfoaCIVYQEagvJOwqvt0Zh--sgQYI2WwAWfIDQ8XvOsLsHaSbiuLNZRYBMFqgJ_bn05i_RB6cKLwa3lLvPCtmq7cs2cPAyVXgz2uR7k1DJLfGW84g1BIFD9w45PAGnJRHWkx-dyC30Zh48HoUruA0d9lTuZYvDW5UGyoe0KYh6tTV7jRueVPuXVKwapAQi9_Jq6pDCStWehb64wTYRF4TKwf8x9ny0x099y4gc8fYffLHvn5woZHDrtWqhxExaTC1sn7fSYTHWT6Lei4tewTp_6HZZEaoNAQL63kzkonWiqp5X-CyROdzIhnuyjkJpMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efDxtSLK0aw6LqSMHgaNXcmmkqy7q55erJjXr-3RySaWTMqz_VERrhA3OkksTuaAO2hpxMdT_h37pHVZhehirhOSi-kzCyL8f4-8h5jIYh71BN4_8r79tk293zZKOxobtfJLPWvGEeAsd-SoT7ZZwBV0nxEkv_j_TTIIt03LFtmZ0Vr1mi0Eh4439hS25pQk2FKmr63BuFiOR8aVUmz2qtIqSfAZ79bQnCeZZTOh9EWxcNib6a7wzWtbPLd_1q4j7OKo04xQDiAqkDgR-0jcpb8BwGU8wHhRQ1YJT-uWU3xzCJGkOjVQmj1s1e091yi-Znd84Ao7pEN7t12QJWCpfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VdFnJvGpw7cqG4VCyHjU98_64672cglPrpKpH5Hh_zPl40s_F3I1wonxx1nftvd_MaJ4D7Fe0E2aLib9-PFsHsgMcDgjqnXso7CXpk_LmbsI-oACALUHEf-eywsxP9VX3nCqj9fxH3B12yOpQobe9iJ-CJEGkNZz7acAJCqEHqAJFlLQqK0g7XT7IKBEH05lpJ1YWo1nsi4FIVABGCN0MqeKFrj-ATg6gBrVFr_iqGnMxHzs-9V9nlRdQLoz54j_LTC0Z4sAAm7KM5xpxUEbx7tIEqbm9HheEFGgRBV61o4JpqD5E0uqacsO3Sr8Gi-a0taUs5CpVpwj8hwBliuc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tt9ub9AxKHJekEcTt5HbzCcFT5VnDUE-1Mwk9vMxiW_VbFuxoGZogFPenosJ_9yMOHVdYHVxjY_h7LTn8gVkh9_s7hgBxpqZREz8kA0W4Yg3vL1r6h4WTLpnr5lpBQNuSgJvpfE5Owx3SCu4go4OdcQcPFp4dXzZMWM6vyDR5fgWCQW_RH3cQVl8TPyIeSqLzGleomGN1mQRfixwMbNAKdtAq2Qd-B_PrwxIRmQCD_-d0vrFpp2KHHh9zufeENFy2dACsPvWWqDwObanai1kMd-QVvY7f4qOOS-hUjS__Z0ZAipWIccf438jgeSMUs8WTlllHagUsR7nZciywpvkyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=bTnxOCHDYpRXrWBR3wRxtbZ2k0skz7v20dObxGy7VfnnQdn4cWMkMa9pwiViaMeC9piakUJF5EpBVcY7d1NqIxyxcowuzI6nEWDV46xJ5G3Fv_ogMKbUstEMVDqfA_4LxL7okRRHzTFbxdX6eeexN7eISbKkSMjJRPAAzx96uWv6ZiTH5qbGDsErEpINQSqYFN1nTc_bC7Qx3b58FnjZ3B0MVLwbqgwgHpGIzhM9d3mkzo5YZ8UIzS3VJg8ZD7xERefAf7D75urjV7IzODfObRJrwNWV32a4ILSyp5YZUfYHGBoIBNpn8SctxvGYyhbYQTa8i1d1iPvZkxEcRKeZhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=bTnxOCHDYpRXrWBR3wRxtbZ2k0skz7v20dObxGy7VfnnQdn4cWMkMa9pwiViaMeC9piakUJF5EpBVcY7d1NqIxyxcowuzI6nEWDV46xJ5G3Fv_ogMKbUstEMVDqfA_4LxL7okRRHzTFbxdX6eeexN7eISbKkSMjJRPAAzx96uWv6ZiTH5qbGDsErEpINQSqYFN1nTc_bC7Qx3b58FnjZ3B0MVLwbqgwgHpGIzhM9d3mkzo5YZ8UIzS3VJg8ZD7xERefAf7D75urjV7IzODfObRJrwNWV32a4ILSyp5YZUfYHGBoIBNpn8SctxvGYyhbYQTa8i1d1iPvZkxEcRKeZhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=p3hKuZkbOETftn04hz5kFFLOn-V9O6Eks9Hbih27vE_m1ML5MzfSvlMeQoiKV_Qyc1CPmuwQthoAK7Y-NCsal5gcJpMVwRt072HDa_0lDnmqKkWmgMlEg3gs4C01GI-ieKDgsRdll7EzoVeSyCegPArxVcDiicFZEYrt7MJjJRUx9UL2h1cddCd_YCJ55cFVHOKmaUxcx45aHG5_csD8jQAxAVJQvv2TSVBGh5X-h6lzWV6vQj1UZz3rGK2KxbdCjX_VnvmEjLzwhr68NwQk8nfV4uSq_1m6qvqtZzPEQK4XwUZyORQE9x8rpl9W-qt9dyaAj1Qeis0ga-nq4sTr9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=p3hKuZkbOETftn04hz5kFFLOn-V9O6Eks9Hbih27vE_m1ML5MzfSvlMeQoiKV_Qyc1CPmuwQthoAK7Y-NCsal5gcJpMVwRt072HDa_0lDnmqKkWmgMlEg3gs4C01GI-ieKDgsRdll7EzoVeSyCegPArxVcDiicFZEYrt7MJjJRUx9UL2h1cddCd_YCJ55cFVHOKmaUxcx45aHG5_csD8jQAxAVJQvv2TSVBGh5X-h6lzWV6vQj1UZz3rGK2KxbdCjX_VnvmEjLzwhr68NwQk8nfV4uSq_1m6qvqtZzPEQK4XwUZyORQE9x8rpl9W-qt9dyaAj1Qeis0ga-nq4sTr9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOgkHFdfeeZ5yo2qvEBMt3NxDdhWLuGnSF0-TJQ3uI-6wnF8MJw8JK3BS0VX58PhuKinRgzo4d_vdF6oJowF0NzZpCP5BLTPTUfTdQw5_LACdrPiLRQHh4K90DO0obvxMQKSoSIWg8RsOYKFuVft9acHNVBQ0-3zqrk-b67xWaeGp85MrBvgxxfuqocMNgx58gwuiyWLgkumy02IkKAvAZJKbK931Yen_pWPcmpkcYvMnVxh2XU6FVw3YtbI7b7DyXvRtYKttOpztAOzAeWJ8X8eJCYxdbMEJtgWIkrajsyGR8cgg9NU7txbxNFFusdDzzpa8czUizVw5sx1AlMz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyqQCqZEYF4zk_VzqyHi6AOGZ2OCLK1V_RdsLrPKxGEwdzGnnHKbkNoHGYrpnMaKWnlgc2_TdU49oEhHGiLcS9zn5UGaLuUNByC03u6NmeMOZ9kK5IF6Lc94Bqrk-55cRDL-Zs2ncqnVbzleuILp-sAGNlIHBEfQlSKjtTl9VK4MSSG8Fb2hEcHPYCyZOstje4QS1eDn4A5C11wLOXpr_rig5ulvkSvgXiL2w4vOCAtGHn_3pxDwadgHhLm8z8YkAYy6I_vKZx1W5TLj0MQ4iBvVwQGfY6ZDKdheZm9B0w5O9x99kvjAluN5e0FQHHR5dJRJBHiF7n8AVxA5gZ11RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=quF_Cfz6UGqTMUEtOdQtHgksWfjvFsbIrJuIzuyZMdpMOEdCXqrgQSJ9_UXTDAOBi_NTDvmb3-N6CVd51rt-PKPITjZ1HLZuhHWbD5miJIPyXjmol_s5kf4jUc3Uh3nfwzxmMw-rNH5HJz0GBukQU6swkymUexU4_iD6JUhZyIy9L6b5uM1gRGfQ_gb1hcZjAPmuOc5h-t1kYYEwimcC6fnRN77cuX3cJj8jXSIXIzFoX029bUw9HK7uGKDGElpw2ZZzy-V0wWz2gHqkMHSdmB6GU0IbvkJqlwu__TV3IaID6Tx8ogYV8JNsl1MTmFkW2Ym8q1F_P8i2otPr3Y27Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=quF_Cfz6UGqTMUEtOdQtHgksWfjvFsbIrJuIzuyZMdpMOEdCXqrgQSJ9_UXTDAOBi_NTDvmb3-N6CVd51rt-PKPITjZ1HLZuhHWbD5miJIPyXjmol_s5kf4jUc3Uh3nfwzxmMw-rNH5HJz0GBukQU6swkymUexU4_iD6JUhZyIy9L6b5uM1gRGfQ_gb1hcZjAPmuOc5h-t1kYYEwimcC6fnRN77cuX3cJj8jXSIXIzFoX029bUw9HK7uGKDGElpw2ZZzy-V0wWz2gHqkMHSdmB6GU0IbvkJqlwu__TV3IaID6Tx8ogYV8JNsl1MTmFkW2Ym8q1F_P8i2otPr3Y27Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqyeoQaSlsO5Sh2K-SNryu2vGB4crR8ljsVQ5oGqtpKLhpC4dj0laoqMJeBzhVOQO7USABAKErKg2BrYWoqEP9uautLn0MjIB9UYJCS2TAU0aNFjsAXkmvYHt-fG6G8jIvx2BUaHWEMwc2tF54o3IGYywCWfSiyisu7A8rtVtIzp0OE8p9zkTJV2ksVnk2krQGR0FTJEspGivzifzZQSjue082eq5inT9ERh1G2ulUhwfIWn2e_NAFrDEUSIB_ScWfQyiR8bYgr5xfPuQmnNHsvWis1L2g3ZlUChem3fFfg0s39kkNph8XSEAagHD_0mKf8VKBIGsvvKF27pN5N2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkm0vtG_k6dwZUGTrrHBvfAEpKmn0UshCDnaYrgZIyeXT6Y8I5nvErvTNnqYg4TapxzVGM_cCaxVGVhPQ_ebsVgAyxPqIstczznXtSGZ1QKd5EGx26wO7T_uUVykx6i1UkwztedCEgvUkjpxWK9fkzbFFQbA45mh73R1k8a99O6pwvrKQboa-jxYduYOP0nK0354JmKjyJv_MSGl8R22RCG3xCfQQYOVlvdWuldrZ5lKPZxKq8MlQSP3cJTxqZteZxegbB4Xw27zT_YvzLows3hWiGAgHdgGen-3xagPGlKgy4gIw09GzmEztMTn-azqlz0bwLXkPVTmsP_3ECvC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aoc4VNwWzhrsOUbxXH-vn3Arb49KQcsoRMNnppa7c0NFog164oCP7yGUM8YGBIS_ZSoRDDbNOAt4yAk04Ir3ch_YEoVoVt5Q0NMRgKwBBLzXp4X1UC_sQIndsyoErbPe53P_Ydzq9c5sPoKoWLwMXa2q0zVV8d4wexu-mxTsmeGqIJhaWaadUlcWsX7ZkK2dlLDOxlOLh3E8IsYvCmVbVlvL-T0DNJexg3bdcF-5QltL_-vQOBAUyJL7frOBVzfDxoAbhVORA12QnYVyM5pMVamiUw0hbG_Sv21PuqIRODp2ec8ZFhG-uFjYE4wnI7QWWxwPqixnfIImuqLiBC_QLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IxlsYGTq2Ea9IZ7mcbHYfX-r6tj0OWH6QmopFsECQ85Lm_AAdPSfriNEDWr4EatWogM9PDjCfwfaNOYu_z3OfhQJPvCUr7yIw7ZxDTAio3obvJjp3xtdf5KyXuyHH0-ghYGijba9QPdav-Z06cPYJHJTt-_LaeqvN0heJvwBsKL2cTAaUWrD1Qajmc0ghk2sAcW3ZILNIkJz4w053JHBsVMK5xYbvC_cwUfuIQuvOITcR7aitzm6UI5vZ0WGT_OeM6exRvA93OGoQIPnH8TDgTSaLqkBlDcFqabXtFZlDoepaS-Y1I5x7fXr8V1ZAfziu4rOjARSILT2vbypeeQF7b8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IxlsYGTq2Ea9IZ7mcbHYfX-r6tj0OWH6QmopFsECQ85Lm_AAdPSfriNEDWr4EatWogM9PDjCfwfaNOYu_z3OfhQJPvCUr7yIw7ZxDTAio3obvJjp3xtdf5KyXuyHH0-ghYGijba9QPdav-Z06cPYJHJTt-_LaeqvN0heJvwBsKL2cTAaUWrD1Qajmc0ghk2sAcW3ZILNIkJz4w053JHBsVMK5xYbvC_cwUfuIQuvOITcR7aitzm6UI5vZ0WGT_OeM6exRvA93OGoQIPnH8TDgTSaLqkBlDcFqabXtFZlDoepaS-Y1I5x7fXr8V1ZAfziu4rOjARSILT2vbypeeQF7b8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdEP2KJj0YIFXxQCLitfALjyhZkf1C6ThIJTwGMprZAH5cw37p5sseAVy9sefi5ZxgVOTisLA-4FN5PZ8yt9nNv3JDMt8VJEmhwYcS51EVU2XR-6gMzU_sFN5PCuJcwKJSXqCKA5kaDLlGGxx0Yi-JwWCsnoWYtcSIDZu-tpQE41Lax5oQNsdqsc7MypvlYazGSyRNTBAL8H1CqZgs3WhT3ivchzNKEBpU0vmRjUQiOBrFIUEC_bVA6qZvxdtRXbHTbAholtDdA8Uca4wY-oLjtopTNZnQg_wq-yp-t2LVE2fxKVjFxO42xB8X_kVniJMKUoFiGnf02WeuutuAttcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXAGew4S3KEPVx16n1zsM6UVtqYlNx4FmU0BrlWnojc7YRAFzw6xV3-dAh2x906SPRb1-c2IeD9dIP5tnoqoVVdSlUNlsih5L2qxQZ-nEos7N8DJdx7fJhWgJsRDM_3oAYDgDtsJmLiPGmkspXB0-ntudAv6oVjWK2tr2CdMJkrlPmk1FMFEgLzbL2e3Z6jB-sCuViMron0kkB84zqwJGkFtbF4yPe0bo-azQ9hlj-TZ6g8p6FvlcJvruduDSMYEMqLDZFCPQrhypA9ZJHnvw-_TPM2Zz-7wd1uZ1EeHof9FGmMkuLWj_oyrtN4bzlFr4oyr7qJsOyYRq3Tu35B1gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=bC9Wzmp6rC_ENoUphVa52Qv0HxBzdejc7CZG9f43SCcB9Jvhz8tQDNT2Hc6ah3-dM4bKYrJGCGUmelBTonUyXXQmWz4iiaP9CsGTOMaWdU_u4gXZMhZk12x322QvdRwfWODqVaAsjoLd6rk2a8z1HJgh-y8Uu_0kyJKQ3yYQ7Ispf6a9k4FUq8apo6a3sKomV_60odhiOMcU8c3Cp7Ag4J6F-mJ-NaVMQZ1pjqy2gzUY29ehgd45_nSI-XTb42nQBkqBgmvHNXlhY0SK5NTxxnG5EcXCjxrNuKKgSe-EPsmtXMpNRftDrrV16E8LNpWH4O6FFLIODvREQqEfZSFk8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=bC9Wzmp6rC_ENoUphVa52Qv0HxBzdejc7CZG9f43SCcB9Jvhz8tQDNT2Hc6ah3-dM4bKYrJGCGUmelBTonUyXXQmWz4iiaP9CsGTOMaWdU_u4gXZMhZk12x322QvdRwfWODqVaAsjoLd6rk2a8z1HJgh-y8Uu_0kyJKQ3yYQ7Ispf6a9k4FUq8apo6a3sKomV_60odhiOMcU8c3Cp7Ag4J6F-mJ-NaVMQZ1pjqy2gzUY29ehgd45_nSI-XTb42nQBkqBgmvHNXlhY0SK5NTxxnG5EcXCjxrNuKKgSe-EPsmtXMpNRftDrrV16E8LNpWH4O6FFLIODvREQqEfZSFk8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=ZAzu-ra9aWKHOZI4QOcYBr2SGsnaLHF1hPm_dPSLJMi7f0wzMP4pBnX501ux2tT9jJqMvr3FTSMQ2k2tSWMG6KskuOLyHhUhZagER1aX-frKjR7lhfklHBmq6-8p0pB0jTRL0U73y6d7n9PPW6D3e9ePw2AT_FDUJZ57KSqdO4yrVKRoUsQG7nJZxe6CPjUvKxBIL-gpSLYicbGvndbIZw7qlBT-3pcmbL2Ge9h7ud0iaowkcluK1Y_Fwo6OltyvKQVbVScYYqeQMQ5xuuJZrvvE1mWkqXF0JqaZme_H4Bu_4Wg9_R8VAVZw4hEqaUfFm9vhw-amJsBSnvIQBsfzCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=ZAzu-ra9aWKHOZI4QOcYBr2SGsnaLHF1hPm_dPSLJMi7f0wzMP4pBnX501ux2tT9jJqMvr3FTSMQ2k2tSWMG6KskuOLyHhUhZagER1aX-frKjR7lhfklHBmq6-8p0pB0jTRL0U73y6d7n9PPW6D3e9ePw2AT_FDUJZ57KSqdO4yrVKRoUsQG7nJZxe6CPjUvKxBIL-gpSLYicbGvndbIZw7qlBT-3pcmbL2Ge9h7ud0iaowkcluK1Y_Fwo6OltyvKQVbVScYYqeQMQ5xuuJZrvvE1mWkqXF0JqaZme_H4Bu_4Wg9_R8VAVZw4hEqaUfFm9vhw-amJsBSnvIQBsfzCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY1HChIfnagOKrydtUVHD8OoOPV6gEMgbjXaRQgsYiTZOtzJ_ah1Qrhd0hTTunx74IKMU7zPBTk6cMmSlVb1nFZA3YLquT_xazUbC1_7SH_tAXFrd3f80cPEg0GGUHef0AOZbwN5w0FmNGWpkQykgI2FuUrr0l1mFnTGYbxyWLPi2wErOvyhLp2SvR0HUMrAkNEPAQnPkQBpKQbrVaRFngqMpaPbEiiI6Uh1DgjREjysA56XazB0_g9j0AoKfhUg1-zOKoO00QtVyfZdSNTyqOF4_1qtelg8Pmj6ZdJtwuhwW1y3k6XBw-5J7MeDgmx8fVo2m6RIK2PIixpHWxua9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxkRlTzDKQGN3DvSZJcLjfvgvZVEUi_vpGPpZ7P1uB8ylVrznas_GmnJ4q7bdd2bbcVE9AC9pHj5kxUKTsaXltxP-INrOVbU7KyI5BRzPuTlfKdc93xnCRuIZyvsqeMJJJpTSqrSxWEg6wKghNHx7d70uXTd6b2rokE1H4sWOnQTHXZKMBeDtdf3x2yPr49pziZiwKW-JU3C3rssgTWh0QNcab3t-qF6UU6m56e8L2BGg-y3i0qlGEQnksaWzyq_ZX5xpjjUg1egsC59WupSZe4CgYH7ZKajb7s9f8r6dj7qKUEKNJkW813fl25q3L0UsrmKSMGVnFHoiCrwLniNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=vep1vWAsukcMAqg-p4bCyDCSPTUZHwobSRiZbiqGoq3joi4seOz3qkbWvI5YuP2lXnBwWy2HZLtjQ_Dj2BIBPnAEya331-cTD4pUeaWv2OmHSTJ1gHw9guolK413jQ4slGEkv0nWV04bsbh4VUwXCzH6nB0AHpnrUhve7hV1XNkQd8RSav_l_FNdGbp7VIPLMIrscFGsV82ktG8iZS2Mm9AbF6PiIsSQ01ALS5si7SGGlhJr_4T88hU2YbEcjJhs11H1ft_rCLRcwa4cOKoZc_CWLYs9DEWtd4imB--xWy0SJkZs_W5h9iVpNYNwaBT4aGVWoZEPikuZDpQqHeSo5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=vep1vWAsukcMAqg-p4bCyDCSPTUZHwobSRiZbiqGoq3joi4seOz3qkbWvI5YuP2lXnBwWy2HZLtjQ_Dj2BIBPnAEya331-cTD4pUeaWv2OmHSTJ1gHw9guolK413jQ4slGEkv0nWV04bsbh4VUwXCzH6nB0AHpnrUhve7hV1XNkQd8RSav_l_FNdGbp7VIPLMIrscFGsV82ktG8iZS2Mm9AbF6PiIsSQ01ALS5si7SGGlhJr_4T88hU2YbEcjJhs11H1ft_rCLRcwa4cOKoZc_CWLYs9DEWtd4imB--xWy0SJkZs_W5h9iVpNYNwaBT4aGVWoZEPikuZDpQqHeSo5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=CGFd9DBYdsDrkCqXQZ1IOGlfbbIr4zwEmlIS0k39A1GUSjhghCZ_m6N6emcFppnRBt0T_uf3OiJKF5oGe87XqhJANxBwyvtnmdtTSfn_5RNdhBPB4NFlWX7LQKGPIJ2-0e35oivyTfDQgO_vOQqx3xAFFZJTfa_Whs5TEEJZaxulfNqe5-GQBG7bzlImxIrzNTydeKFVY0b5BE_UHLeTvJrpUQ-Ibn68-NiITl9QrUm2V4Tzz_s1Yr4rVsJTouXHKAh4xoztOTbUIS2tfkY9W5P4aV_DgnO2uFH8MwCLg4xtWaW4l1NMNZ41zS97CGj-_E8LJTZ6rpl8OArUEG_urA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=CGFd9DBYdsDrkCqXQZ1IOGlfbbIr4zwEmlIS0k39A1GUSjhghCZ_m6N6emcFppnRBt0T_uf3OiJKF5oGe87XqhJANxBwyvtnmdtTSfn_5RNdhBPB4NFlWX7LQKGPIJ2-0e35oivyTfDQgO_vOQqx3xAFFZJTfa_Whs5TEEJZaxulfNqe5-GQBG7bzlImxIrzNTydeKFVY0b5BE_UHLeTvJrpUQ-Ibn68-NiITl9QrUm2V4Tzz_s1Yr4rVsJTouXHKAh4xoztOTbUIS2tfkY9W5P4aV_DgnO2uFH8MwCLg4xtWaW4l1NMNZ41zS97CGj-_E8LJTZ6rpl8OArUEG_urA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdL_p9m5YuGp5m5Q5wVGPfm5h_dHfmUMCgE9-wNh1n-ItkclN9CNKLRI9MfNL4QPB3PXKaA0T3ouhSZV8zxilGVYSIqXcaSUSOEZl_2defo0kT8zsy2TNT-nUqzsXVzzXayKiYhuWTDEO4VG9kTij9ibrjuA7ne-iDwCQdX3i3Mx1Q8HLL8qzHZUgzDD5t-TYdj5nN1pi-mWmxA8NBWLR6I4dxyfvGyakT3_kjLGoesTCKXYGKa7uZ2So6db3jyU87Bz7ggBw7OvbDUgJcj8LbPdroyAMQuSPBAtuScWhPv7qV7shXX6U0BnRGEPN5suk2JKkRgOrZOhNQf6u41aQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loUAeKcKpck3B7ZX2clsRmiI4YeiACErEEC6NwgY91VnNSSWNAPRP7I0K0nartQF-46vToQZSnm1geXQwEaCdwcFB4TH4nbdGL0rL5qWJNZsRnJWa8By01ehionbhcQYSNnkXTAKKS8YAV3_S8KbKxEe9kw9IIuj76zwONGDuligJ2YVXvZZylkxkOclWT8YIf92OFq9t8FgFz2xedL6MtI-31dkrF_Ks0mBJb1UFQsg54xtt9lRMVARaP544G2SCCE2yT4ISHssNnFeUn-obH6xvs58ilVbs6AbYzwpsWXrKNFn2IOdmbY5tbyas2GzL4-bhljGl7CgKx18ClL-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxCm7-CDM6btv-GbfQICsx3dO4KXyYO9tKFJOSOY2gZQ30EBXxs43NoxeKEZ3IvHXXdW4Jc8wE5ckkazMgqJD8ESQRGAWm-jTa_TJ-iMKFzFIpBwjseBvA1VuoOrqkAeZNLb2M62lsYn1OQFYSILEJmZiZI-yD5UTOdii1F1F42HpRDhNzzFTBJ-IOpmAxcz0tvYkVrtQt0DuI6NcUPBsUJlASIwfewll2vkCScv3Zu1FCJ4T71kV58zpHn_GSmVl3uDVZZDQrJ5gbFh6qwds-rC1rjBoUDdxnnc8RwaNIC1gzItzPj7L-5T5vRcC3QeunsVfCDFK3IU8zDAs9ntFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St8nIjAr-bB7OtClFIoC7GoAld9yCwuTucG5TcJEBN38kYq64bjcoC6FLY8LTVNYIcYVpSJDSFaonARfBVXKbFE0CS7REhw1HVoh-VZz76AO5QiOSYZ_9PTFmFF5lf3FZrT9xkXQ1Wu5hKQcbqS5n3BDgoclH3KEsIvVNmzTRgG5VdCFjJODvqExam2ncGVIEMWujBiRbzHO1w1wzO96fEK9tlBAO6XOjjC25E7Q54IXSTW967PGkdIz87V7w99vwdecax4PfMGStUY_MKVDMPLEruCxoCHth32SSseC7xJWZE-hgwIuAavg2LtYPdlGtP6DfSmovdc4Jx2Uu5djLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AOeRgfe4Du_7r-k2pMBgp64Ucnuqf4dRkg7LNq_-cUGXqvo9tnKGMxR_jnAu9ontB4UPiaGjXC2LKTcVnc2vAIaGDpayDPEUFEeCN6utNyA4vFpXY7n0Mj1bgb20Mn8AzGUNHsMdefnAsyA1ob5oetMhvw6ZH1LdPediqWW8AEefx05Qg44C9x6nT2okD3gA-x_ukQQDBhm_ZK7zNIl6CBhXXVnih1Sh4k-xYpR31Rvq8XeHlzifJZH1p4OvruOrO5z0PPJ1pm5OyIyRy3gTqJIaZu4ZeYQao_FgaQawxpFEPGnbVOaf8gkmTaF21QCYSu-_HH_GMFoed1fjbO2QCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/liM5vmBVjx2GUvPKdbWVhYMpYHrO4lFVhsbCNO6JjE0m6T4DwKSiXXP3Pn2A0v0InmWVd6kAJ_FSArsEnG35Ewwbg3wV9GXhpbhRvZpb_JrHz691kG5eaAH5yVn6OTXPqQGfhR_wvAL5xzaoOwXJXuee00o2JLeGIhh27wpvgYSjLQ_TNAxDL5tzec9aU81qL9e8_DcfqbErWYzYfiqcT1q75AZycmLf2bknUPAA_ysgCPKwM67jmJYhxZZk-XsAMqa5LA94WlhnRggKFrQWAuRcW4IDEUXezb_NY8J66l-Eq0Eu7jepQa5WfRgKMbl4B8xI9G0IPG8E61ZQlAZXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLshYSXaCqgZXsCLBkeedO2YBZTm68gp13U9NPvV3O10CmGVp8ZYt-iJ-g91D5XV51Te_JR0uV_levkShiycFEk8-QNVVb_sraikLKOTXWLJQl2oSQhLDN6La-_XlKvdS8Sdwdb8EKvNIqc-HzQd-MA-S6JWUzjZTzouUQvhmqvEQlqfXN7AksymgbI9xqrkduU_IArQLcBuDLK54ykZOU_af68fG4ra6KjICq78S5jd7H9ncLIMmG7nXhUQroN5wmgZd6xrFFTyIIxxbu38Fy1Vx4r9U-xyAy0tbQgIxDLQ0jwxS0k9t6VaxrlfxrARiuTWBlTbToZ7hnKgZ0YzKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dveDzQKb0rS5HzYPVBMljtpqrOSt4lqizWmGhTXasNTqSbbL0g-mLlqeGUv6IAYp0D7nkFVXZ1Q2YutZewHwxvHWiE_h6TWb2x3zKRl0K7PZ0EVHYuuwWBD5jm7RTL3QubUsqV75L9HpyEZ67xLbm-BKGutFlK6KwOeFy7F2fzf0vlBn0NkpeD6FcQDLrggSEHMwzxIOUv5Qbg120dwM1MVItLbXE4QtNhojGCCJli94e5QLi6UTmaN3yuTdQiBprESx7yg7NDrDaBz4L9Iu-pGdidS2sMSY-Dvm2ZOCQt0ihtvl2W5rUOC4iLvJJEvfwSD9rW3AaAspceKqKxvw8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9AU18qhxZz2OqbpRzi_RwBbZRjeV3cbCEXKn4chc9kLW_FWHkxEa9PhucAdBqjWG9uM4KLHlR4pIf8Q0Ax30R0C_vnXjR4nI_VnlsZ9KHvQ_87XeUIwZhxe_FjzPkPyB9SYnmx-OONjOCfnTvfWF9K85mjDI2fPN_JTcVJ2uJn5UnK6jY8dk_IXOtW72v7NqmHaSQEcfo3Oig1BKU9n7YQ6DQK-OvBOgLwiO5DMg4i9Mo53OgFoQU_5pLgBavsGRzmKEEwKMMqjquewy1lNCHuDaex0W9Lb6piaZVrDnfKb0ax5jlgj9eaeFXEpqSWkd4JN_UN7Si2bcEthdzDJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InSsUu6EEdMTSst9WlwYUdjbW74W51g5VXlzxk3eWdWx75aM5zQ6WA472yVlatTM96BwxBURyB51ESjys_8p_-zpinSCCImEJqOaJSUdf-N99SYh4XQxgbXWrNKtQotk95PEaNXL55IZyG-DiVnOhKjjUCLXolZjbFr9cP092mcDlqHgyP8E1ENPib3IQ-7xhiYr77TgaBt08gwU0uavqUdxo3A5k-ma8sFDSQnle_VwRl9amZpnxVQ26ItLY1sgZb-NgPwFHROV0DVwG0-0hBKpzAVW4B8xJ6l1cdsfzcP6Es1uW0MqzWfS2CfOOzqAOIo62r84JZE0rjuFZBlYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
