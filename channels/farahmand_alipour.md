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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 12:47:33</div>
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
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHAFBFcnvXuewN6H6Mr-97u3vLAllyfEvjUOEngOptXF5VjVKD77NsS_E_iJrlkMXWZ556Xek-drGE_lpy04X2e7GNm02uMBa_7gEOvaNEICvH8rNFRbbKHHy-uGxfM-zaoE7PRob_v2vIgrJoWMO0H68rVbtdriag0Kdzs092EgMtSY4V2BlB8B74OmjhzSSclgeb3xiWhWdFZ2LGFRgSdyemtnKU-n4XgxEEeyuZCi4ers_RYpaHxp5Krsxs1TKMv8gabADvUDZjnitiv8wbkMLYZfx3sS6udYvyeZmheljitgGWmBTPbWvCdTk_8vuUicl7xRFQRIBSqmO6ojOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtGw8K29MtYV8qwafr_11h5bRz6yBfjpYPnJo9K-PgOF99nRNds4_kh7tDCBMimQ2VIAYyZJ6MeKqpjKoElkijYzuL1fz8V2CYyt5ai611SjXFP5-vxBeoYPNdhEiyXYWdECQ_TqCp7nnQWACcIkH55rpVy14xSsbVca3Y5jetrnO5UIAHljd_hm5KaWctJmYDCooAtvBQvSeWzE5rw1xtg2dYy5iHDZ7clmneIfABvJop1DFKY-vzdiJ3FVTtoLD81I_pe8ZJ5MkZlLA85k1wMJkFCGHnifJCXyNvt-FxaTWAIBvRovrTyL_w1QDmogThlhwlpnDyeDz8_OrnSKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tj2twco5ejiuMHZ84JP0wcvFlzHd7OaXlxdfIpaMcczC4D1C-5J_hIgplXGFT01_etp54A7AIOM4fCeRPnaVfBSPqEwBPBJ1e2rvOZLK-VXGwSPZj_6NlvZ1RAJK3umTBccGpce9VWvbP3JPhnYnSbGfeB2T_0jmKeJkxOtQVJHEfZQ-yocsV6iKHjiYnNZ8Piu4b5l8uE4oOuBDb3rYD5HzbHrbPcGDySvu8u3HEToMVOUU7PQ2WhmnIEP2lHiDji2C3jMI31N76zt4yMb7CcYvezV0OEDT7yIQGnEUJA_wURgcOdK7pt9syCcCaQQDJH0_7hHif6NcIXh8S9PUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gikmSGLqJGCWopa-vcotBpNI08bGSoUBEUQ7JQi2Lap48K3EZyWJ4y2iF2wq75F0Pvuq2stEVFrE2pz1LGmuJbdGjkA7dTmbSmDjYfo8e3XuruGJfhlP9osPBY7u-H06augoQciQDY7Gw3Oyh98Xbf8eHhKkZZ-HzKS7TCxX3eRyFRMW5ofAU1sV862scrND3n3RxpjPo_wFT7pszW5kBJzv7PlawCTp1rRt_bhnkOLEAbVRvNvRkrACabV1swzmMEj12-HkrvZ2QqSP03Kha5fJ2R8jR0PHf3i4fcukgbC4Tpp_N7h7Tt6sA8J8cSVA1RNn4hVU9fvBrwtWRhrrqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBsRqkdqM72B8JE-ckFufxObNJaBFXBVYr6QoRBdWHWtMbKAaBKe91gju1-ecvjyNhOhCoqvRp0YhnJxfJo2sBRFIEgnfMnpBi_Pa44v8U8bs3kDIF4KzBZK6f4T7JS9cl43nH9oIwdVf2fDSaTnil1EkdpJ-aeqo7sTzJNr7TfUamvCxaKNna2ULO-Gka6-j0ZyLkDjQIVZW1xNYTNysidFK-DAJ3D6TCDI52WwKBlIgd6ozFvZgvowPb0aZfn5Ex6jdDXf-yEF5OeWiYv8JHH1o3Co4A41TtOUnpbQsn2mSAgCEVu4bl-ZKvNMrnMZxHPPaUlKc9yPyiMuIfnRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSckZ-TBIiTdoOxEDmXs5ytxzTVe6-XRoW4mCU50uoAiaUo2gcifF-ZFbYHi56cmwbaLZ-13ijgG2rxk9fWyKri--0N0sMCSDgnLVARR7D7SCtNz7JGf8i3_YZ8kdtS3datfRwgrQKff2AEgO2wzMKWuERqR5JGpxk3yQXQQpO04ymIvA8UZ0fR50b1NJ2-cUTHwfHT99nT2lATViVs0xjroOYcI8DDPycgGZ3DsGOXhRoSJLjGIVQpcCDgWkmFY8jIsfd0Rws37eJsV8qnsqZkxGl5m3E_Ekc6VjqHA3i_1OK44q4xlb7synyfzgB_2Kp_dgZ6VNgpB_bkKAlQE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ1k5UbzFqqvs0wJl01nz9jJJF2d1O8Qzw13R5o31_OAzoewIa7VEvd8833-vddTL8gBNkKFtQy1Zct7FZ-WgO5RWdXuXsT04iomza0KlfXmZUkHADAWaNanMeZlcSm4OVzihmNi8wS4IRMLT5mTEiLXgYo6mt0rfaoUJlx_-jDoCGmEXUc6Nod-7ceZtP5qRb6iB3jdijhkkZQDecQB6YEtNxLPg0ZGDmfeCL6UWPuwL67ApKIjVKWYWQ9EhVOz4e6SkQY-6mSB7TB6yRXgvMoNAMXR2FXvTNQ-KJPTFMZwUtl0qhGZz9eQsxee0Eqys1ncHXDLFWZv4PWwZG6rGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-uYIYkUxeuWcMkQ5Sk4QuOMxV6E0Mtyifht6gYLv4p0Lx0yAOKqeP2tMtK7r7I-znH_ph4PE-TR4cKtid54Q6hmIv5eGTcmAq9etpUhUeqaq7WPKO3Wtog-_t6GnFW2dln_d0JmiyGKlstkrO2MaOqrUyDcu5pQeZBlRIx_EJ0_ahzFfW55NxOUSK2D-lrDIkxxl4eTtmwXO6Qjcfb_J0m2xFW8VXCvYTvTl1NC0QqOzESHyhtXFoE8a9GpClHH0avfxcaJyTljeME8iI3DyhxTTEq5r69tDXT1i2AacTyckCnf6o1XOaf641W5vSAOmNNE7_3s4o6Sxqb-g0lI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQegXSkgHUzyOVrtA0fNECy1Chq-PphCRQzuGM-rwjVgubTBuKwruLlNOWXqx7WUpl3gKezgRdHNLUi6Tji6Yi7RBHZYhR7ROJ22COXcZ1q0wiyyl2G3YpAWE2F46gsRfXxoUQGknD1slmCIXHno__Skjc_qkA9cZ3vhWWCdiSQI5u9r9LjNOQ1UhPJqhFEtmwI2jNpF0tSHznMPEAIkxR0bz1nrO3cKrMSxtvh8VtUAkRx9GT16UBNeOLnoyVtKjjWqWKtq8eygoSDCwVLvL32qCtJt1HMC13KnXu54JPPXIzjumA6pLev7mcqL7wHT1RKBQh6vQe5DPr05dxnBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0MWkowWQmmdyAMvkgGh1G5mVkxL23MFrlfWmxa-mAjG5h1MTm0Ex_YBAxpHAt1MzgLwLboeQaDNpQofypn1txFukyzvpHRiwb0FYtHz7kwHcrrDaFDPRPqluHN3Sq6Zk5ASwVbkcJgNSLVzhADvGjKC1XScYUNlaaXxcisj7euuiooq-nVPvcM7OxIWsdnPp8GeTmxtjCA1i56GFxlZBgAmD8Ti-kAu9WZv54MzLppT4fAYEn4fj7YrrjbCPXyn-al6z6x4mj0Jh8plSmyCYTyMLKLHCgKxOItC-KgMLYjCpmki_wEK4IuMop8HOYNvtN_ZQyW73Yia6-rqu8xU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WviFigk2hSciDxGfS9_7T8HZRh1DwWRJciN9VYQmLR8YOBQMD2Jptx4Y5ufs1CehnOKZos8rz3lhXSmGCoX6IaveLyHB4KgIcPcvlwMpC_Osq-TXRDmJAdhMjChP9JMyGImufovgIXBlXZmwstfxFDKx0bFusWHyAuqUHluoSxIFUyeuLrP1CxrqEPDVlRwhr4466ukUeh4BbThIkTcOAWbecnIWTzsTFTNfyfZ5IKzuJkS9PWdTSrenwcYaSTmw7umTB7rLmCoNkhhlfZt4WqizKsacMVolSU6YRC0o0Zxj8UF9qOBxC-vZ4RXN5wbdEpr7aEPr8CRPiNQOkFOb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEXMVBAeIdOWDOChH7emiD_kBY4ucrK-BYyPSRf0Ezcx9nQKgMot6v3DQ67FDtw5lYQBkJf81eKgtVLaCW-l0wc5BVGNMjXyXptIzxmBggmxRz_ePao86Pi9cqnXt4HvXeM0IwEE3nf-uPhqVlI8jotGbrnLfrzQLmIBet0DOFveRj14acX6a_-cI3nfVWTJzC8unMfrhtnKCneTS05TRSuhkO75L1A1NiVl3ILjEZFw3Erb5Pw1vODRkDYlj53IfZ3d_64DiD2BsdXiiBhqGI1-BwtpSeQMImeVcoY7FTpdANOT2RdM5D5IE6nwrCIIeV6Mb0PSagQO_Yv36EVS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K13-EWVk300XrJ1Fkt-iGX5-rnfHdE5dP4IGPa1Z-kiTzlysN7YV214S91LGQ61UIw7oSfy_cGFHq1jg4qsxvzCCJVrWcnJtpjBrDiMxrhKULT-_NcEyVybLvqpra15vHesFDgkfDnpjjBziAcQ03FVy-0eQtcv9WiP1HL8QAiqGJ9CkPdCRkRG5uiyYtJdCWWHiP9Zi-He51y4XmiI_R0XePJ_t6O3Z_h6mGKtzOK_bnFMdpCpjERYz0XcX3ywl7ZuY-cbARFf6ZHg6zgSP4-HfsNMwzeOwSqp-aI3YZNP7RBmhZJuD0e0WDz47DeR2jr-C0rN_F5zx5kZLolamTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzZXqyT-27IT8birnRUQO9iWEShsp4D5CAnqHG73eZJccuPWYJ4QlN7iQZsLd40PnG_6T6LwOFyF_mBZo8IqJL7tu0NvCz_Oim-9oNVELnvwId-CyaYL8-eGfcsluFhe5B_bxKFQbaavHgTVC4bRCPx-1ZbectrZc4NMsi6Peyx00GpS9Y5hmSGjJa0h9G63xP8n-tWzuOQckiXmUm7ipJEU_VTvxaBOulufY-dJM5xLZAhsdcCA2MevKrten2sfnzAGtcckwyUwKMHEsFoqmf-BXQ-uGdOx3-F4UUczyILHPhndXQHhaKEIV6JmI3O4_9bHS4jiVHlGj5N2l1cL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZPHTIoomfOqVt-REz-VFrw2K2L5O0ojbJ2pARpNE3kWJpzFSazq_gnO4R-vhQwuQTZn9oNlLVgqKU6NnrUHh--ggwJYhyIe-gSKxxieD3MFWG5EWb6OJZaHAFRzf6knyZ4lT2rIIc5CyFpjKWxvIeILBgqgcGQWMQLuug0I4SeQCByHwzPBcAmimkCypgJJyQWd0mcHZ2QwRlusk4OkhGANdpwg7CMewrs2M16KxregChaVNpCw3-ZKOyM2-4kFvy1OnoRZftySF-uPUvqz8nFaQv0_WlL5I5FkwmNDfbLPJ96onpC5De0MhvrxArH7Hkhd2QURUB9ugLt4Y4gAMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGqLX56XQCCEIWTU17jn-ET9cZtqPTriNU_wg5kZMbppX7e3HUO-gpk7shcT1-eB_Qho89eYMAu3-OcT_sZuoipKuz7U1m6PDm3BU8vQMBQZY9JV2h4O-vuoX9_8EnvuNXs4BkPQCgjMXFzr005_x7f2MzTicuZKh4ZBImglneUjmXCWt9vMLaggn4-w-J93KDA5UgrkV4ypmF4GthrsJf7IEkANbySD0a2B1wcwVefDgGZBJpEMyLUMgGhkrLFx_RR-Kz1zjBWVbC1UqN-aJrhBTFEDw0rEidorqB65qmmzfCjh4FLysCQKQw3-SnXJO6PtXnCk7hJ3c1HF2iooQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPkSS6JCdx2csVd9VidYGMalktPoR7M70epREVgtd3WnNXiBBmuQqOCCfl8nRSws817iHXrcyuLhQmxe3-Z6IxQEWkC10iRyQ8AaDFPshy8TfQM8o3g_1T4mv7pp4JQE8tQUVV0MpHrTVJVukxPpDXKzlkk5ouID0ZwIGxUkQCYwgWhljF8PzltbzTnd22pkoSB47U0IsljBitlOUhV6Vdx36SbmbaQJM0vN8YfYGJaK2U_4kjVdrpli4s-aXEvAzAcEdchwGgAphXb7Dx-8ViEH3O3wtBb1XyiIbsJoysW0pN47o3-PklDNcHpWsNzFrLjcvUFgnJjPQjfF4YxpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwbTAOxs6iZVZrYScUx8tRBYdW-RRs4FtTGq6AJN8683SCxTms9q7b3BjrOw50sQumYTvD3FMpk160mATyxYE4pWhARcd4OHydi_38UW-URQP36AlwdZVM82eMniPAlFv8ZFeAmZXHhxkFtPp9LGyOsf_TyA2Aw1_IqlDq7qXtSa14KAVDEizSwEc85SN8dQG5ioFTgDtOTiofZ2e6qsJfb47w_B_GlulyFdKe3Ez8qQyDyhrN6FBhSZQA5cG5_DRP9Q-TqPf-uEQlbK0gcLr6SGCEBMv4ca-9JgGpBadu22pgNk20xZ_dS7CFNYpmxAdHJK2X-ksAkJU5oObUljRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhwIe6kw-Xu88amxQWycz_eX0McGIAd4-8EMWSdD-bFZhnXGlvirpLGerseVmr-Zo0bn5vf7tQTee9ieEvbRJegNBdDVhAxU9Ce9_wi7RIvqseCxoDvVU8ynNHQ8RtFYlZR4WtF6F_gK4SuKfYGDBQqcnszY41jZNHC43rebvP-5MRlaylnyEbn97Sh3yqyncw4E-LxiCTPpyTgVUX-xbae4hsXVMjeXnGwxpvuGgcQjeuy741J8z96oh8NwxKWtANLU9js_a2qiulqC6iEhJK36_rxn2iU3eaWQMliDk5KrWg_DkePU7jaUSIDkbSff3Kpeh6w8COqtRHAYq8TUjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=NgVI1aAtcQl-Xh74o-9U9sn9ugXQoYBGLkfmglzZbr-9aBA9NPt0cMeKpURl4_IntCo3HWRVhl_58nvCBxNHnfnDABCPDI4hC7vEKoDh5aXOJNPoSGOkR5WIbgqILEkFbrjvGCarIpGp4uimggUBeNZB9fu6rFM7xQg_weB8pjlCRNHR73rUkktzVvnq0_RInYBYgTbuLTFm6XRgTg1ECjqtIWrFhdyHsXK_qG-EX1pOR0of3NlFyfTwdgxvKEcBQNsN0ofkTS0n4z0mzSgRKhf95aOaIl4UZH31VD8JCO2PzVhT14KJzZ_liW34k5TKK5xIAih7SoasvobtG8iJ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=NgVI1aAtcQl-Xh74o-9U9sn9ugXQoYBGLkfmglzZbr-9aBA9NPt0cMeKpURl4_IntCo3HWRVhl_58nvCBxNHnfnDABCPDI4hC7vEKoDh5aXOJNPoSGOkR5WIbgqILEkFbrjvGCarIpGp4uimggUBeNZB9fu6rFM7xQg_weB8pjlCRNHR73rUkktzVvnq0_RInYBYgTbuLTFm6XRgTg1ECjqtIWrFhdyHsXK_qG-EX1pOR0of3NlFyfTwdgxvKEcBQNsN0ofkTS0n4z0mzSgRKhf95aOaIl4UZH31VD8JCO2PzVhT14KJzZ_liW34k5TKK5xIAih7SoasvobtG8iJ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EghWwEeVScDADU0UuYaQT2QsOQjP5-594CFbzvvs6TYtP6icf4JRRh_bWo30jnVE-6Qac0I0u1ktieFr9aN3xomVuenEcuylvVg5LiYJYgK8hbIcvFYJFsRx681hFlXLqim70wWIQOXym8njLw0GlxvGpSyPa1KurdBFnhgjUlky-Jc93Bsr6SZxCGEF1erKa6N8BYgl5ufVNX1TxCnDCbUmWpuObgdN_KNROZ8ikrX9ce2zHzgZNoQhSxEuQBbWZBN9c10K2zZ41dPKNrllIoQVM98rGRy7IhZ-YAxj2gqGPUd-DsgpeSbv07NpJ4d_oUR_GLl47maIofBAnZuOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lniF3elDwE_1bEyNEcWkej-Btqwj7OkWnTADtRntAGq7P0lg096eVIjhqnTr1IEppJaPh6MwOwNM9U5UWUY1y4hardIeTGOv1IYWdZqL0jKF_0MBqEl0EXtTCFiM1YmRkHHajbpnc1qKmxAB3hyNNqbYep9-a96dXYrKcVG9tfnTw-Jq5jv96sseTi1bQb7X-pl_kR-ngDJ2zW2B7yFdaoUbz81sMJkREduC3l0T1MhIXUsBiclbOuJAEJnDhM4qcs7tYJBiRQB6zFdGUyHXAjimyswg0VEpgNErwI6dEwA_442_R7Ic3meo0cBVH6Y5b25txo9jJTRCp1-jiS2sJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGXk-Va93WCojEXYLuq-sITPdez76ruAGhwskFCXunLI9aGWyh74icecK4sG8gkvzC_fekdY8wPIPpZgpB-dcHXosAYvlo5sllIBPPy2f5fFE6oSrO1kLAGFOXmi1GuW-_hxPhFsO1wf72-aroWaw7kjVAa-leBWDaYzr80Nt7IknahHS0326whF-cBYtXYiJpqT1W5KbI6x3XsLuSq6KlIwpxibziaI-tZJ0mI8-n5SPA-GJpCPg84wMr8vUW8OVS85FioKKJdVVyjfPZW_aRVddLb7jRfmNUfT-aBLTnrHobJeGhV_ReWs6_adR_Hi6eQxVM-L828ORpHa-TtNAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe7kUO-5qr2FXREnaLh_l_46xXKhuYzlLncdqvY72PHVGtsl_vKH_zNjrZH4GwhF_AQbWtPmmO0uXDIeKbHCh5djG9tnP5w4wRgDiWmBdl9drVfcoUT8FgNJEDMT1c3nfzHT7LKhO3BtFiyh0CCuwx5p1EyjGrCpmmf9Lg9ToMTpTaOgEs75t_h7KsCDnnN-CwVLPe0l7pRqeTiog528m--Cxq1_xUjMeffs6xHuHjzo_Vp-tkG_iVIix1YkgfhSftT0Ny8sRrcy6Beh0r8lDaavyreruQwcCmLPSjE3pdaZcV1Nghj9yImtxceJMia9YiUCBNI7oRJj9_Cs2SK2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPbizi80omR2iZIUxW0KFfuyxmq6fODqs4_UQlaw5NVEKB5-E6mBE7cdoTaPEad8VC97MpJfvnq2P2vBiUMxyy8XK4Ll5tcpEefVa-ocS8DMlQbjPo_yABEchM8M0PY3LfXrE2Rj1m3DX5MUXqMeRvt5B5RdiikAwoKaUPHN-rCrOAbwBwCR9foVGJiSOjb_O6tCRzHQuJMgDaiGrzreO0Ge70-Q-2Z-JhZk8fwz6iUhXzmFplyHoOVhcwwaeqrIEgDDKbanPb3QHYDUklkJ7OPIFPVb0mOvdCdkxIN24Nn58zwaLQ4VzXTT1T-2i4Mcn6FAAUBX0z6nM25uWwligg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAnNod99t77BHPstwzzvtN5NyuI9fsehu2C2xyOdfWKM3Lyif5LTAihzma3bnspgNfhYR83vAXpf_IxmyPY--F5IehGcU-S382MNWeYvbAx6wPSmDmz2IzaL2QVk05UtgJpHKHpu76hp2plM1hggfmS5Y4ONd20yjZzeRDGFSMcNDFWqQLZ18hzE4n3CkYHiceIah4jUunSfPivIOjdx7koomjya93GgBpAWcF27lTQX664_mwtflUF8Y9Q5AJhAy0I_ipMkgplmYGNV8jz6blcmz4Mt_jTzQGHkuUbUIfGraaCGf-jGINZXEqnoEY9feTkRU0BdYa1kFH46b4v7fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxl9FjBkkT7PXSCAAahzanYZ2AT5D1huGafm4n20YkD_OwS_1U6X-H2QnGaqVaI6McevUxFw0r5hdioSYg6lzfGR9oCi_tDrEU-Ko7fYYD9ikp31kLbPdQ2tbDvcvHeegl0R_GNhPQ5pNUG_LkSeDEYE2DEbkgNlri5hV-h1Z9gLnA48WlarmLRw50oVrZWh2xAtu0Vm3NIHmPCUgGbVnwSgT04feStLYSAz3nHtmb69VyaIlpGJ95FfN5YaCXHKQsEjUFal9FKZVzLlPaPcNltW1NVgiaysINyZCh6SQxLyo-GVNJDaUOUIzl7xn3_iV7aV2we15Mc-f0m9kYqpOA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=tVW-2cO1dvMs0g9t1TYmBQkXS-gDHCl6rczOW6VTYUWbK5VEUNXnVzuCMCtPG9RJZz8ELgRiDTI9IAMVcC9oMFz4a4pPBzLhBPANxzXe5RfQ-4scfEU4_wUL7VsoQY249ophwThLV5xFAVNxchyDIJYEGvKo125Xq4cgjfh5ECudnJHjFwtFVR87ZvfvYULwEEBF2kQZ9OKOkAIqfUbWoEANbvPFw_PDrTokW5bJyFc_qLeKk1DxPLAZ8KltHTcY_IpaQrQLzdnhBAJg3QT4KkD-KpmRdjLgJTRUUeC890jGrNOaMdgnyq7mm3q_Z53KH92a0bFxCMlDOEU9KeouBRS5lQ1zuWf7giXDyQxfhwpc_Bhxwf4bF6CJAa94yXLUc6BWaLLyCuGmEAWDrBscGBVoMf7hGF1umHj6EbSgcCG7HCe_lEum8wC1SDy12yNSEA7xuNYMXfLVV6wps0DNa4dJFCTtuvKR50zJZWLS97c6L1VEYR9EptuJ0swDmXU-lO_cgDQ1ki8yWERFZFsI1aX-bKKL8iI37EhZ8buOV-CwjEH1Cy6wRh1MiLq5FySgU_InvZNopjfGF4UM3_8CGyprbyUtXHMywZ68AjQjCMtlnBVIFLM01mjQ48dq2jfKSAaKqQAuGVIck3Kr_uUcADrH_-qg5OED0GLHBGovy3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=tVW-2cO1dvMs0g9t1TYmBQkXS-gDHCl6rczOW6VTYUWbK5VEUNXnVzuCMCtPG9RJZz8ELgRiDTI9IAMVcC9oMFz4a4pPBzLhBPANxzXe5RfQ-4scfEU4_wUL7VsoQY249ophwThLV5xFAVNxchyDIJYEGvKo125Xq4cgjfh5ECudnJHjFwtFVR87ZvfvYULwEEBF2kQZ9OKOkAIqfUbWoEANbvPFw_PDrTokW5bJyFc_qLeKk1DxPLAZ8KltHTcY_IpaQrQLzdnhBAJg3QT4KkD-KpmRdjLgJTRUUeC890jGrNOaMdgnyq7mm3q_Z53KH92a0bFxCMlDOEU9KeouBRS5lQ1zuWf7giXDyQxfhwpc_Bhxwf4bF6CJAa94yXLUc6BWaLLyCuGmEAWDrBscGBVoMf7hGF1umHj6EbSgcCG7HCe_lEum8wC1SDy12yNSEA7xuNYMXfLVV6wps0DNa4dJFCTtuvKR50zJZWLS97c6L1VEYR9EptuJ0swDmXU-lO_cgDQ1ki8yWERFZFsI1aX-bKKL8iI37EhZ8buOV-CwjEH1Cy6wRh1MiLq5FySgU_InvZNopjfGF4UM3_8CGyprbyUtXHMywZ68AjQjCMtlnBVIFLM01mjQ48dq2jfKSAaKqQAuGVIck3Kr_uUcADrH_-qg5OED0GLHBGovy3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=RXBhfnx9kH_ET--j8971w1L5BXBoom93nv6Hb4BYArmr3AVTYaLMghUviLZwyaGatSWKxG5UoE8zCQ9C9TCqLXxSJbXxYindyWKANZGh7M3oODuS83kJzeRlMG6UjbfvEQ0aQ9IsYrdcXTzp9h7hxyCEh2JcR1uKJXI5x5zvwg_wVwThS_s6vtwPANFD250Yq6t46FaOlpdmIpJnYvM1E7yGx1DiCPQCV1QzwgO4D3bnqjsylGL9PpFZtMs2SKCYyrHZMLOEnPbsTWlWgjEHBSOGcdFIrJFAQ3y9CUnMPMk_ISWoToojQAHF1Msb91zDWH7gGOzGaJ0ZN-1I1v1Lsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=RXBhfnx9kH_ET--j8971w1L5BXBoom93nv6Hb4BYArmr3AVTYaLMghUviLZwyaGatSWKxG5UoE8zCQ9C9TCqLXxSJbXxYindyWKANZGh7M3oODuS83kJzeRlMG6UjbfvEQ0aQ9IsYrdcXTzp9h7hxyCEh2JcR1uKJXI5x5zvwg_wVwThS_s6vtwPANFD250Yq6t46FaOlpdmIpJnYvM1E7yGx1DiCPQCV1QzwgO4D3bnqjsylGL9PpFZtMs2SKCYyrHZMLOEnPbsTWlWgjEHBSOGcdFIrJFAQ3y9CUnMPMk_ISWoToojQAHF1Msb91zDWH7gGOzGaJ0ZN-1I1v1Lsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgeJTsBSDWmsfz-nBJDq72uXcgW3snc_Yu6gFqoytBVDt0WYrdvcvvVa5Dji_4dwKgkAe-L05Q8PTo0_Kl5SYbw7EwZN1Agw1mAC3_2XbD2yQBt7My3ExTc5-ICTU6UiVSv1QD80tapv_l1oLzVK08o9oK03A3qyDLEiWceD4SRWfhaAjiR_SCZTk0Elop1btaK4rfCRi7MMNRJKDeAu9auDQhTXqEZEIz3Qe6JhFHdmOc3UfWTHn4a2mi05qfue7bQcIwoy-jf1M-aAeSQ8dwSXqmRrUshJ7m6V8aUQsdIRvAqRK-vAPa0NSF6xh0hUxFm9kLRieMTdkDqP8wbsKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0XJ1P0TwUQyMoXLVgbtOf_aCJcyV0BCxbEWNbGasjbfDwG_QMddoi5t5LNDarZMlJ9qRpfVGMYOiD3-2P6lFVhEzG_m3xlF-fYixiL9tNn_ksCOE6cK9XBu75w35erdT0ZO2Ng05Gu4aUfZA1ObSXwZLMnK4UzPFHI4ew34e8RLUttE4McD1frV47fF_isPRhoJRc4tB03USiCSm3PTFOzHfdsvR9oBTAXmEoWY4PsUYXJMzgKs95IfkGoECKDxHuH4Yz1rGnnMMaRNTOA3mvEt8_MSSdxCPwaKM7MZkOFMkXW__kEpzREo_WAfl9vXOHl9GX8QgYETOr51VLZoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=W1SmHSsYj8c1zv2GLMTcjo3q0o4n3U09NAObqfqkdX8-zSD0OaXQTHZUwFectwQq3oIQIPaN4dtfP020DaNcEI8JxdrpCSN9n12CyqMHM7-Ss_qeI1G5hkVMnQt6Z5lie1BOzvGiJxkmjFU1F_ND4NOQLQy7AkMDzBVSE-dIGz2KFSSye_zK0dK-yE3iAvf0QEYb261dnWAVyjh04xUt_rJ0sxM2RvINAQLYdW1IGoCQgfLTZt7OU5Tg7ejt3WyZJETpEBSznsx5tI6DxG_UZLnOBwY68Gwud3xagC1tzGmK-a73cLsEA9gNKkkmypjKiBbHnPJqL96rWv7wmaGiNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=W1SmHSsYj8c1zv2GLMTcjo3q0o4n3U09NAObqfqkdX8-zSD0OaXQTHZUwFectwQq3oIQIPaN4dtfP020DaNcEI8JxdrpCSN9n12CyqMHM7-Ss_qeI1G5hkVMnQt6Z5lie1BOzvGiJxkmjFU1F_ND4NOQLQy7AkMDzBVSE-dIGz2KFSSye_zK0dK-yE3iAvf0QEYb261dnWAVyjh04xUt_rJ0sxM2RvINAQLYdW1IGoCQgfLTZt7OU5Tg7ejt3WyZJETpEBSznsx5tI6DxG_UZLnOBwY68Gwud3xagC1tzGmK-a73cLsEA9gNKkkmypjKiBbHnPJqL96rWv7wmaGiNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA_MCCeTlgKKFx3AhqLaRluyq01OAlPaicFTBoAqwbJ1FJQ_GxS7ofmkcj-zrEj-10DioXcAvk8RqG9nmOPuoflLtXUddcdPyiiRcOV-KOksN5dJHlEmmZkrmjg_afNqgdcFibFqPwfDC2p5rgo6oZ8IdtT0gz2HTQWYGOBqvmKGdRcN3wpFAvf8I8yrwwcpn8NR4UhCQkoQtrOSa0lToHudA4qLC_mtZTkL9AIouccIG3RvkP0eV0SWUX7Pk8hKdlJbBbJv60c8aDH29cumyoM46Xs-Ze6Inn9p6GKx5SqsuhaTYG3YDA6_noNmOBXWKztC90GOqTH-y34wcPbR4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmnMTQ7HFELJ0R1frz7EpWZStjcqTTpRfWrOHyjYeJen8EVIoZtcbtDB3IljGRTQ2JxJ46bCCwP4TwP0jS7bI13DCrR-AJhO1e6gby0Lwibawf8CXKJwjw_E90R_uy__03Ioy-U-7GjmrL8Pcibj0aIrs9FJvWIgsa1lZogyue4rMzfchwqNNOUM2HmBz9ssRUayDFnsdtk1gNxNbo6VK09fKySbmp2fwHorDZ9PwIqrFOb6x3fe_xceDsh1F5LEXgzb3HOWNMCqwgRmgcapU2beSonDfhmYEHk7WBVZRL8hLjVHzEWc9CxzAIVDIV_H2ts3DFiQLa71ux5ITthfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VovHVeVEAi-AbNtxYq-TfhCoW3rQY2Kp0wEx9F4ezOUrBnXRMf5bIrSeKlqvu2qOIrOQaD14e4uri9oGwht-0lWEPIPTepxIlQ1KlTtrs1v9ob-RqYGd6cWHLl3ioYsPvNcSn5flWh1FNf1r10PFdQqehKZajzRznJUXRGKIgAd02v2rJ7YpLQNEdwH1ZR5p2gBecpRqmPMVzSgm2SLGCXl5uiqpZW5ZYoedMjzW5WJVvjZDTIy8EZVGBlla7fKHj6Ao3TRN78PbtqzVesZRE79nTJuwKQISgNIlyonaMPnnM7nQPGS9TGl23cVv8tZSvtLSl4pE_hwVcSMhKptlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgTeApdTKw-OZQXXxTqiUHJh4pINNIjzaqlcye4YDSz6V8Vhm0zWtI-EQeqjswC4VeC6Pbi1pAR-BRViPPzZcFI52pyxrRznEnOsdl713J96N8AIK32yZPtpqeCXQywSXJflTCHphiLcDVh1RXFr524SuMBbIipsOYzTkgj23Dnz34kJV19nwdqES91J71J_wdZe2GlV55dvVujfJarWY_W96viRgzuTcumE4A1rRha3fu9v9mVb_H9bn5IWBkJtmGQPU_2GTSbIuU5hnPzknmLFE7unxYWXsOtynBGirB5zaAqfKKNZLEK0aF_lbNWFf5EQwffUfZRmnuG1zfM0Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqkI_181hCdo1jnnE0duBCnN0faL3q8-k70KppL4bpvDWvHXbvcm7Hl9ya3wGz3dfvVIa4f_IhJXIXXWOCeHEAUzljzTiq4qBhOtqfEpolqVZq2ysvA4y7BrIELZGiR3Dp4jI1BsEFnqwYWVIEY_UO4o8qkIoD6G5I-ocY7zGZkCkvpJ8cHQhUUNK9lK6RNogT8hpTfFrCq1PZvm5pQrv5vukn5YKcSdmWyg-X5hjQvbjuVe4j99X-DDPOMPcP9Wb5fGl3lSf2rQbwsVQ2HNOYRG2hDFQNdnUZO7gdpiT-pt7LmKLQRjdae7pgMcTvE_2od5jCLmGoR1N6NO8FFI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5S5_SCHIczNHRnrl1xd3rQlZRmyXU2Cmla15GL-KcIocYAvp431s3ElR30zlAG9Zv0KSdLxF8rZfCfwK4lwLMOwMEjGYBxSrYrZUGhVefnRb0uhQy6GwMRZDqeP0VMCQfQ1Vgl_Dz5WHu958Syda9Cq-cdnRAGm_ySPbepK0yfXOB3FakmiCGOS9aiQwaInYMpp35auNQZrM2Wccgf8oPiyFujA133yz_Mb6UgjV-4lZjW7l_oSut8kuY5zb0pBLMv4k0MIcyvEANmgoA2ZUjNZGC2lNIkGyHnJ-incxRXwbvtq-fXPbc86hf1yQqeqMLNnROEWclIIoR6yESPJiPlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5S5_SCHIczNHRnrl1xd3rQlZRmyXU2Cmla15GL-KcIocYAvp431s3ElR30zlAG9Zv0KSdLxF8rZfCfwK4lwLMOwMEjGYBxSrYrZUGhVefnRb0uhQy6GwMRZDqeP0VMCQfQ1Vgl_Dz5WHu958Syda9Cq-cdnRAGm_ySPbepK0yfXOB3FakmiCGOS9aiQwaInYMpp35auNQZrM2Wccgf8oPiyFujA133yz_Mb6UgjV-4lZjW7l_oSut8kuY5zb0pBLMv4k0MIcyvEANmgoA2ZUjNZGC2lNIkGyHnJ-incxRXwbvtq-fXPbc86hf1yQqeqMLNnROEWclIIoR6yESPJiPlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf75XBGla6dHc1osYp3iprHDIn5oL6adVgZr9PubbfU_7HYaSxv9H8_5qFQEgkrbHLMG-IEpYUKq4L8S81kOyZmFzWqLC399yrrDbnO1wD5fQ0-23K-wtGLOz7KPUyJBsRzpCTIePv_LmddSM9byWdjMzTh1itoE8DiHrc37SrCzj2RxQb0kWq-47WCHZbUX9bh9ITwpuObqYtwE3SjZ7eSgrXzbIxQnCZuJTule7MybacF6DKg_ceg9zDRm4agjE8rQDb0noZ6b2UDerYRu9fZ4Z_KnrUfxlztCSyVg_9-9Wm0BhMbKyIzrxNIHvyaVeeRuCEV-vFRN_iIgy6o1RW1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf75XBGla6dHc1osYp3iprHDIn5oL6adVgZr9PubbfU_7HYaSxv9H8_5qFQEgkrbHLMG-IEpYUKq4L8S81kOyZmFzWqLC399yrrDbnO1wD5fQ0-23K-wtGLOz7KPUyJBsRzpCTIePv_LmddSM9byWdjMzTh1itoE8DiHrc37SrCzj2RxQb0kWq-47WCHZbUX9bh9ITwpuObqYtwE3SjZ7eSgrXzbIxQnCZuJTule7MybacF6DKg_ceg9zDRm4agjE8rQDb0noZ6b2UDerYRu9fZ4Z_KnrUfxlztCSyVg_9-9Wm0BhMbKyIzrxNIHvyaVeeRuCEV-vFRN_iIgy6o1RW1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=UoiCbYIFtivnrStUdm8W145NSe9-ze0z1FT5pxiIEVFgiYGlkowGvmavLAFusOcdFMwdeOkr3uTPX1ZvMI--v-LlJCPL-6jnbDskHQ5NU2ZNYJ2YXUz6IqXa5d_4Sz-ugoSu4d43DJui-dymyPURlzlwE45ptWjiyAY7BNDSXExO4LOWcqE5busQIHuVx3d_Hjd1utrLgkY7Ez2fiPMjc9UvlxS5GSeApB4aqCmf4EoQPT81SQk0S9Ge1_7Lx8Q8Qu1xFe5tpATVeqhmiSJfi3X_3vC7C2eCp_0lyFNF_VcgydyJ6FN2ycv3-hZXCPosqg6mw9X0AMM8qXIPaAYpgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=UoiCbYIFtivnrStUdm8W145NSe9-ze0z1FT5pxiIEVFgiYGlkowGvmavLAFusOcdFMwdeOkr3uTPX1ZvMI--v-LlJCPL-6jnbDskHQ5NU2ZNYJ2YXUz6IqXa5d_4Sz-ugoSu4d43DJui-dymyPURlzlwE45ptWjiyAY7BNDSXExO4LOWcqE5busQIHuVx3d_Hjd1utrLgkY7Ez2fiPMjc9UvlxS5GSeApB4aqCmf4EoQPT81SQk0S9Ge1_7Lx8Q8Qu1xFe5tpATVeqhmiSJfi3X_3vC7C2eCp_0lyFNF_VcgydyJ6FN2ycv3-hZXCPosqg6mw9X0AMM8qXIPaAYpgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWMkl19VQL-BF6mfestFc6UKtR_PzetcRVKdnAO7MMK6M0UbvAH9QSEtDr1AyuqZtr6LU2vtgfX0yBuHElSh0V_RGUM51wQnO2sKpcdbgTp-rXGWzKIvHT3RiD7TBEnZUAj2_vuhjy8nTsWkU5Y5VOnDwr5zHjf7dqdLAo0IjHd-5KsbP-qIbwHCWmRBj6-BZrYAkX2VQDJupKa1zRplZQmBybtsu5duHIu6gLcUHabJl9MxaYicZFTg_sAIp8Jl2Zb3MhDEfQC00OaTLimpc9tAXI7YW2rg75DRKpJPqPyXqtcE4ss_eEb5NeQIJpyoi1tAsFlLkXNky8faMuBIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvwyhj_dm4he4a6Hvs3XfIP3FCttW-tW0TTebUcA4zZaEW_sBS0WPI-jtUeFo7Od885j7Gwi2xxrnUxQRKHLqST_ksbqPLQVDsTjHtnIxC-_Q3zJLLAkqePi4XKfttUPLHBk7wSFuopjBS-ZvhxCUbj4ksmHNzupENCQFPBpBoQAdeIB2VvlttcE3eSi3HJIKY9UfnYguYMbBmT2RwTTAw2nuIAk07jvXtwWDOvXeFBahryjqAZH5nnFmRTp3N0VjHg2LgI-qDMQuPsAb0FL_It1gkA7Nc9l-dE2Q2OTjAyEoeAcNi7RhNDfROZUY9m0D4HL7JGOb40JX4ir0pa5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=BFK-ra983jjTWgaMYRV-_tIBxwFeP10ZAYInJOhT-hADgfDyz57ksd--OCDmbZFIpDSVu9HpWOjoI8T5FT67ixn6r-8Rj52STL-OS4eyhEDPH5NMpkl-cfEAzCwdZN2recG1b4hOwi34AhWxHC6WPSb6Yp_Bs86C-rZfsbalzLbt7wcduJaEwTmvKYvOyjE6PZ0RsYsPntHVnWGYPpeJGV7Xsk_ss3LqUVdSS3gfO0HhlhOz-63Rv_obzwAyuftJkiCwNMi0TyY5ct6HNnd9nv56_VG4ox3BZnQ34rCRZaLKJXke-I5UVPfFf_tOnz2F8M4Xx7ex0zwvONd3XAu23k1xMDd5dDjv-klnYg2-ZXSm2fr3LMJOnTSsv697KZOf5UtK8awdVgQwUeX4CoAv9ttdyDmDoZ06z8jKK8kcueolNRgzI4dOUs4JYqkTEqAyY2cidln-5CfUCZld4mr0mwuglen1X05I5N3Q6WqOZ5rQW02Pb2RXNbrcr9QGAFxuFi3UKhIqDDxlWO5UlLQgjgof7pdpcWSnXbUQTz3Vo2uU3QpjDN9zr1coZnOWM7xlHbqB3von5MM3Ij_1rsqFYKdMrQRO9Qz1dLcvoii0ga4wytS0xGD1V6QJ5UwOkzaKWc_ycWmlawDKyrxZggQ6lpCv2r6QUWyOytoVvGjqYrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=BFK-ra983jjTWgaMYRV-_tIBxwFeP10ZAYInJOhT-hADgfDyz57ksd--OCDmbZFIpDSVu9HpWOjoI8T5FT67ixn6r-8Rj52STL-OS4eyhEDPH5NMpkl-cfEAzCwdZN2recG1b4hOwi34AhWxHC6WPSb6Yp_Bs86C-rZfsbalzLbt7wcduJaEwTmvKYvOyjE6PZ0RsYsPntHVnWGYPpeJGV7Xsk_ss3LqUVdSS3gfO0HhlhOz-63Rv_obzwAyuftJkiCwNMi0TyY5ct6HNnd9nv56_VG4ox3BZnQ34rCRZaLKJXke-I5UVPfFf_tOnz2F8M4Xx7ex0zwvONd3XAu23k1xMDd5dDjv-klnYg2-ZXSm2fr3LMJOnTSsv697KZOf5UtK8awdVgQwUeX4CoAv9ttdyDmDoZ06z8jKK8kcueolNRgzI4dOUs4JYqkTEqAyY2cidln-5CfUCZld4mr0mwuglen1X05I5N3Q6WqOZ5rQW02Pb2RXNbrcr9QGAFxuFi3UKhIqDDxlWO5UlLQgjgof7pdpcWSnXbUQTz3Vo2uU3QpjDN9zr1coZnOWM7xlHbqB3von5MM3Ij_1rsqFYKdMrQRO9Qz1dLcvoii0ga4wytS0xGD1V6QJ5UwOkzaKWc_ycWmlawDKyrxZggQ6lpCv2r6QUWyOytoVvGjqYrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=OB8iNE3-IGQ1uX78u6V6HUUPVU6faKhAA6YDBW8dKMQEWWlDIag3lzHVaikVAsu8WY3dgIBNccN-_VN3oiGZSW_dtYBxoJTSVSYHFAL9PYUEGCcC-NeoS93K2iF2bPH4kXY7MkS3XmD-VeJo_ceKk0X5jn6q6FvLDWX9sjOqkU9VVf_s3nuyVqOTh2bUhUdiLMTJEzPWJfpJ3eZpMaLqOn2FMvEsKgcYC8haoR8gTv-Lm0MyU9u4NT0z97tIr5Ve1bIvBz2uK7DXq85DNNj1GGd28CIzEmFU1BfwvsVJah8ADPFEBS1rtMIraf496amImmFGED3u2llVs3HKRsnmLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=OB8iNE3-IGQ1uX78u6V6HUUPVU6faKhAA6YDBW8dKMQEWWlDIag3lzHVaikVAsu8WY3dgIBNccN-_VN3oiGZSW_dtYBxoJTSVSYHFAL9PYUEGCcC-NeoS93K2iF2bPH4kXY7MkS3XmD-VeJo_ceKk0X5jn6q6FvLDWX9sjOqkU9VVf_s3nuyVqOTh2bUhUdiLMTJEzPWJfpJ3eZpMaLqOn2FMvEsKgcYC8haoR8gTv-Lm0MyU9u4NT0z97tIr5Ve1bIvBz2uK7DXq85DNNj1GGd28CIzEmFU1BfwvsVJah8ADPFEBS1rtMIraf496amImmFGED3u2llVs3HKRsnmLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVuYfAbxNerlAQ5N5MygkYRO2O_udCOIqyLOKGmJyU-mhCKG9yZ1Jr7NXyIzINQQ7R6mG3yVBexCs6ztes-9BIha3o3baYlXp9_6UqSC2UaG942G-c-XY92iVjmDxSQvg_vUnOORJciLSWUzmRpn1WRXN2FGoJXtiFYHlqcu05q3DyC7QXvhSuuthn1SJr3PLoThEkFVIGLz2bLkvUm3a6i0sqWdR-oxP1Te98f6QNeP5uwIc4I4HDLjfl-blobfHrfutuVNNb847aYdrnsfLnGcx-ZhGxUZ34y8hmi1iy370IOfasdaey50uSLZqrldDLrPjGIIe3hHoivcxl2EoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PavkrLHnY3CeRlP_jDfFLVzAeEIxw67iK-7uUb81uDKlySiVV-T5tnZbyrKWvulvqDg5m9dIk8szrVwG1oo6MVh9ibc7yOnKW_H017jCbclrp_WZgO1RfI3LSqiH0QzHBgE0rNFABaVeYwE9nNh8LmeeeqVWPMFXrbxAwI_Nlzj_qgDqaRtTqMgKrcF9iCUKPzh9EhEsc-TRcMu6xiI2DJiDISv_cW23jWUlASTkccY-KrXmVyJDmMLrqfBrfbvdFpg2WYy0a_JG4N4bm7RlakGPN4h1bjPqFKhNtmtuGMeo1NnH6t7sbGbOddM4t2mQahwJVE1YqpgckLNY94TY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4vXScRbaG7YJjzBA7UgHXKYvPSTu281xVd9-fMcRN136HUM_eAwIGH1v4tkPAgayVLrqjzjK6ncFCYy4PWTc-U3d5cqWNH1VDCl2Yxjmiw9vu0uhJCji7_j88Pfjb7GAPqaXqNcvKOaECJJSgybKuX9gWE2nvABKzbdvMSSDrE-5je6-qjY_OGo8IfVXMjRCbUl4M5mTRto91xesmhNNKNTjkRrdD1KYGK7DbaQEMs6N-s1jxM-R_kqawG-UBkU0fESBpFP2Aa8FQjwo5aq1JL2zxKf2H3EKooGjVCR2aoEyIeB4UFItM-jVy5f8gLxgJ_kkOwdNlyzgOogZ6WNAg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=r7A6lW-qlPM_G6AecVtaFd5R5xtzio1H0Eaegu4Ej4mAUMj3sVGQJ-17D4yzhBJuovztenU48rirPx_kHb0yEqp0ArLEJh6SM9Mk2Buo6bWYdgLQy_ZFXS--3EhqCS9ghQQaB6jgGcm1-A-vGLpDgjdQ1zFls6DnL5O_xUw1lJix4X7EbHIErxAR7jLsfaEcJuR4q5tJ5t0xQdKE_TzR_pJ1p7m_JNgHBXbc1TOFYTbwypqyTtdcONCjenu0mTV8GLMjpMZQNVQUBaNkJDohXiA31_FS4CgAJzt9RJoFVd3SaISUEkBgyvTAXktvZcY1erVXURbwLHxKrHp3dktN_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=r7A6lW-qlPM_G6AecVtaFd5R5xtzio1H0Eaegu4Ej4mAUMj3sVGQJ-17D4yzhBJuovztenU48rirPx_kHb0yEqp0ArLEJh6SM9Mk2Buo6bWYdgLQy_ZFXS--3EhqCS9ghQQaB6jgGcm1-A-vGLpDgjdQ1zFls6DnL5O_xUw1lJix4X7EbHIErxAR7jLsfaEcJuR4q5tJ5t0xQdKE_TzR_pJ1p7m_JNgHBXbc1TOFYTbwypqyTtdcONCjenu0mTV8GLMjpMZQNVQUBaNkJDohXiA31_FS4CgAJzt9RJoFVd3SaISUEkBgyvTAXktvZcY1erVXURbwLHxKrHp3dktN_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=DsPTaTe2uIdX31QFWpts49wKYRvUFYBoIdW1Krd4dWEyed1EUGIJQ3htyikLXHiIKR7GAncI10aOo_J29WwEM40xl-ucIDLemzz91KA1eQFxSvOnY1__wOGV5UAK59T4k5-cN1CWwWHIP5eAT07F1BeimjZam6jYTmdE1Vu5CHgFGq6kzo7Gz1YpQhiwyGLQ6VZpJF4bYqmzpIioqhU54UQju-gwg4K5Ov51WfjtY9B3FvocBbv7wZxkEz8iON7oFyuUvjae3EtEeDU5CxKKjTeIcsj6aJtnySRQKi0PqqQYTHiDVxi7YCAZhqinUNl4bRfzt35v7w-C86BfHaPCV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=DsPTaTe2uIdX31QFWpts49wKYRvUFYBoIdW1Krd4dWEyed1EUGIJQ3htyikLXHiIKR7GAncI10aOo_J29WwEM40xl-ucIDLemzz91KA1eQFxSvOnY1__wOGV5UAK59T4k5-cN1CWwWHIP5eAT07F1BeimjZam6jYTmdE1Vu5CHgFGq6kzo7Gz1YpQhiwyGLQ6VZpJF4bYqmzpIioqhU54UQju-gwg4K5Ov51WfjtY9B3FvocBbv7wZxkEz8iON7oFyuUvjae3EtEeDU5CxKKjTeIcsj6aJtnySRQKi0PqqQYTHiDVxi7YCAZhqinUNl4bRfzt35v7w-C86BfHaPCV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGkWockfJp7vUb8lInpdVfNtPiYusbyxrGbXsBNE25TWN7AKeMfFBkIYdQJhQC3C0jT7zLHcfYSXFaLT0zc_WYTzZxC9kYYPI57VPhaiXGHcVmFH-1YcbmDDrMWMKuz9c-Ram3IrhBD2dR2h9HkHSROP6lMA3BzjIGb9xVmTTaACsTNQi5CABBPCrIuVGUBalh-tCqw5jfrfJCE6G3qHZCaZ2aoNCOrPBCBHQHinVbp0mxswhlKhZHnexhuHvGjEYZu-FZju3ZmSr6fcu43-oZLb7U8s8cttNsJSYdqNfRTwFlf7bPFSB8KNo0ojbrU7nLY5gpE3VtW2dI3FlD66CQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ7_Gu7GYBcuePvvvw3gN1t6GCBJScf-8DxHrb5G7oqa3kYXLnTEryL7yUVRSg8OGZHmQkB8eSrXIzQevq5Kw8N1slZ1ukLMh_3fVTe5UBIjKPw7zOpjshAR7F8odYMUE8g-xpJzT6GsKYEpdbCotYrRIC1y2_hxm52vyBhsTeYOSW02AnYhmxfnk9zWQ2xoErv9Ju6ZtlD27vR46rdjAFl5RyX5VQBt2UkJV1yzhhR3JGzRib5OuagS5J8RaD9WCM3k4QsjgrgrmQL7t7g-7_r418Yj9qKRdcD0iY-HVp74l_68eHa8vlfs2HnOscjjCac07Bf9wKj4YyQc-Vavug.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=Imd-K4ytYRsrO-Gh1LCSvXXPY4BCnzDCIGVXv-Pc244smryZh1QMGYbwSjmdiC7SxJzlXni7CT3bZskqzVcQroY6rzMWERBJ25Vnmxa_YGIvtDCj3pes3JwFSOY0TC1BsWzfUrSpuyXs5GQJYJF3EXjhDQjuzLQbYa7VDPLKVT_GeRfCJ2S0jwA2IK0xbHaWaMvbvWY6CtCdTktHtfAv6x2BGXOT5qRHu9tFYC2fT5uDh9X8qyT30yQENxNKuS45hhGMGw8xHyb2X_hBhBu9Nywo6byIKoptN3JEMEYuiWg4avXK_iJDUIRLPsvhRDqHRgCRSSPi7qsLYW7RPfpzGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=Imd-K4ytYRsrO-Gh1LCSvXXPY4BCnzDCIGVXv-Pc244smryZh1QMGYbwSjmdiC7SxJzlXni7CT3bZskqzVcQroY6rzMWERBJ25Vnmxa_YGIvtDCj3pes3JwFSOY0TC1BsWzfUrSpuyXs5GQJYJF3EXjhDQjuzLQbYa7VDPLKVT_GeRfCJ2S0jwA2IK0xbHaWaMvbvWY6CtCdTktHtfAv6x2BGXOT5qRHu9tFYC2fT5uDh9X8qyT30yQENxNKuS45hhGMGw8xHyb2X_hBhBu9Nywo6byIKoptN3JEMEYuiWg4avXK_iJDUIRLPsvhRDqHRgCRSSPi7qsLYW7RPfpzGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoeUoIDesoakanRv1-Ny0Hv0J770T8PvXOHYQ_yy9ivBUoS8c0B44pZ_J3gSJPegg9YUY0kbSMSBM-qdgnQzsx83jBYKHxTTLObZ9j2zX74-POKfFfEhWhq0Yy1obVXhHBHmxhI-IyTRbsk_mdFDzqcm56NaSoQBilxDFTd6Ft6hcOk9zSpGm6AtbPJxRvs8UbMVZf-F3J__GBcMPerLDg6cR1P2XTaPSrW4xqy5lkD4bI4MnCpReCkeaaB4gst0tkRnTAZq4VOCCiRDH6l8hUjtjYV_853hCEegvlL2sIxmJNwRYjJtBRf1B5hXkslSUQCdQnP37_z35EEvJIZGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrU_s5kVG2opNH3_gcT5JHPy6gogjKGSfJyeomgBLaGfbTAw10TFQTw94aN6KtHy21incLjfH-w-lnSXID2VnzECj3UqDSiJDqnUXdZIdyKVSEJFm14PW-x_WxB3r0roT-EQhZPJsB3jco6pwgi7eGAGD0BjyYaJazy5hUsl6jKlUlNa8QZFQBr_kFotPWjYjJRUDhgIpiExrTQEny5DOS1fyLk-hcN_Y59cPJHOiGosCTtKzKMT2HCbnIdYBfvEz-JMLi_kzjKh7j7uNVUHIJEVW1l75RCA-2lizYX9g4VUgXstww06UAjZ6hNctYHZL7utKqbwYlv7sSIvMW5phw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOYNwzglpCKI-LG1DJVe8_peT2gQYt8bA_XMEnQWYzmzn_Toer0OYbecAwYA9bIAFomkMzeEwZncoTJAtV6zJXmaHY2gFIrxHNsJkBfBtMkvYQu_OptJ0l916YZ-_chtW3yeA0_XOjf9aqZc7qxLpD1DIhgF4e_8VYi8sZuszypF7DiRyXwdtjbgc4aL1PQK8U3H00vFX7zalU9YB6r_aqhQL_ROhz-twjDQuwanVoZ9Fh67pZXvnuJJ9FcWt9P4XwYaN83sPdcT1H8plJYnsX6d6r6jp7uk_AHRKTfCX8MVZ8xnfi0BLUhmx-A2kEq_j6hwagtAQXpUftUiQYqToQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLaWVGwohUTcOAMwCyrJ4DTnrSgGORhkO77jTGGWsJHyH0RQjYjhVnJr_PFgY5wZ4UPbyruj-vcZtnhJBWIxYkmq3KkjB-_BY7yBiuK5puMp6BDS6-T-tTXx0nGYhwG1RGoO89GmbIEJDVwnpZ2HktgOrA3tnnjbkl6O9PY_fPbZOBWWjjWWgWqYlDRZZ7sIjwrCQSAtcEIaPAlTKOHqyT96Auo9eu9z1bI4aHeWrZb9qmeI4y4ML1G7gihu5Z4wvgwt3oS34dZFIr0rKFkAzzo4rU2jNtpn2b-tM8Py8ro4NdCweq5z_--zke1dmy7rFldulUfEO0PVzuiXB7XsEMIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLaWVGwohUTcOAMwCyrJ4DTnrSgGORhkO77jTGGWsJHyH0RQjYjhVnJr_PFgY5wZ4UPbyruj-vcZtnhJBWIxYkmq3KkjB-_BY7yBiuK5puMp6BDS6-T-tTXx0nGYhwG1RGoO89GmbIEJDVwnpZ2HktgOrA3tnnjbkl6O9PY_fPbZOBWWjjWWgWqYlDRZZ7sIjwrCQSAtcEIaPAlTKOHqyT96Auo9eu9z1bI4aHeWrZb9qmeI4y4ML1G7gihu5Z4wvgwt3oS34dZFIr0rKFkAzzo4rU2jNtpn2b-tM8Py8ro4NdCweq5z_--zke1dmy7rFldulUfEO0PVzuiXB7XsEMIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSng5qAmEQti4v2Ux6zykNG7rDVj1ilWrLqtZIp5lqLRLLEAGVhTTsh3C6UnSiKhsTsLXqXzq8h5E5n7ZsjwKesQ7GryHgaRNy44hBGvqx2ThaeNO5M82FdEuFNIes-I2MlH8Ju5Xtt56CJhNjNFZdN4pFJn34linh9xUgLFiI_u0NSjhh3Tmb0HgIxXiUezhdzGQ43_Oc1shnOAwAZMMthCpi1e_X8g9fDjhg6-vJuRONx8VI8xIgLQRIr0DekViFxy423pXgSZ172aexRqcmDATtuIN-0clQjzkiO_9Kv82St5QXSXLTy8GG4TFUtLKk_lV3tnMV_oV8mYMZRejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/evLfCN3vF2iPQGjtDEwoQOZDm5_Citln4fuSGgiSMoREnXPHVBkUFTQACv2W_xBJNdvCL1G0Jd8-LU87y3gqM0ZrFUi-mZkeM7TL9zRdngubz0bIhls9hJ0Uj14nWmQD4F6SQn-gMRiuXU6qdUgv0qNF1rLhRJZFl5zXXWw3MaUg6BhwpXNMlpMkKhI-rXGFX6MysiG-T7t69aJZKFThSqjnPkUb-xim9EfRKkZffJ8-X0S5RqCo07MWwT15TdY47261ie2pxzcTd1CMjVyexb96CDK-WEXi5OlIDyjtxelCLVieljOgHxMk-ncFbdfCJKmBnxlZQqZIUwMqZzlOkg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=joCme2l2aiBviMuveMW7G5K1Z0r75ogJZcU_uSRtT_8qMcXYHX1hj8BN0BgSRyug3plfo7EOsizoP8omfJHooPHgPS6unl448ndA3GgDRpD-XE_aqAebBHnw8J_rwo3TRK605fkZMoV8SWES_c-4v9Ndh8KR_qDqNVMY6AUP8WwYbSPr1tA0JYvve1bUzRAigkESPJngfui7zUrRAUE4Vt_BNaXBwOMHBUJQBw9WNnWL_5JunltQPWuQ10q37XFIntgFruJ7TzSTbUY9NrC1MsjWHxtYy0_iIAxTe9B-fQUv9XFN7PQin94bqZOTqNdJZQxbH9LOmw4bLkuSp83XGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=joCme2l2aiBviMuveMW7G5K1Z0r75ogJZcU_uSRtT_8qMcXYHX1hj8BN0BgSRyug3plfo7EOsizoP8omfJHooPHgPS6unl448ndA3GgDRpD-XE_aqAebBHnw8J_rwo3TRK605fkZMoV8SWES_c-4v9Ndh8KR_qDqNVMY6AUP8WwYbSPr1tA0JYvve1bUzRAigkESPJngfui7zUrRAUE4Vt_BNaXBwOMHBUJQBw9WNnWL_5JunltQPWuQ10q37XFIntgFruJ7TzSTbUY9NrC1MsjWHxtYy0_iIAxTe9B-fQUv9XFN7PQin94bqZOTqNdJZQxbH9LOmw4bLkuSp83XGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=cnWOiE-pqdxN-FpJEa9HcbKHv7gDqLR_oxtzwqqzLgtj_-XndJ01rPqRwd1ywMcj7_4nhgqxIIZUMdXKO0NUxMe20vxfEHcXymmUfQR3vENOjzBkJJioGRuXq50PFaYSSZwXYtEbMJtsOajxlzvyctm9Pphu6KgSXCWrQIf8pbXANfUc_0mi_R-pTeleb9ogam2AcfS5Eh8F5hAGwd8UrBPjovdLBOD5uYJ6LHoklIiaAXkGVGMe6gtLwyJbEvtnI0WlDAYr9QgYtgnnGAw5W716_ZjweS_pytr4a6KsTCLtfiE1naLcqXszzgJcDnVNA8G483dl-i51bJLg1cxELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=cnWOiE-pqdxN-FpJEa9HcbKHv7gDqLR_oxtzwqqzLgtj_-XndJ01rPqRwd1ywMcj7_4nhgqxIIZUMdXKO0NUxMe20vxfEHcXymmUfQR3vENOjzBkJJioGRuXq50PFaYSSZwXYtEbMJtsOajxlzvyctm9Pphu6KgSXCWrQIf8pbXANfUc_0mi_R-pTeleb9ogam2AcfS5Eh8F5hAGwd8UrBPjovdLBOD5uYJ6LHoklIiaAXkGVGMe6gtLwyJbEvtnI0WlDAYr9QgYtgnnGAw5W716_ZjweS_pytr4a6KsTCLtfiE1naLcqXszzgJcDnVNA8G483dl-i51bJLg1cxELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejh_HHGzESWcViUmHbEwbm44b8kr1NNIWwhJyDBBo4Qmh_W9MenveRJT992BS9EsFNwW9tOGyb0-ip56qCPKERrggAXEHpiwTmYRGteMxvVh8ICO1snkCJRAXwicz5RMuMY6B2PmT7dBBLJIiTAlqzJ9PfgiPnJiOaQdqrXeXP3kFtny_BBprdXfpfTvxzW1Bf9nAWWgxK0GxVUoI7g9jKT_2HAxjX_jws65b1aT1tAqhHXm3M0jF8j81Ndq6XD16XNGSERFrAqJpkLY4m0l3fnr2ZZU5M1LkTJxXAEUVK0kxWqgc7rt2wXv1oNlDjRsYAxVN-GL391teuuQ5gkASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS2I1hEAVFw6V1rJACqL7wqrBqxZswYF1C6DRLAHEFRKcMQZDNVEJPR-tmCv3T9XIAZ5X9dPr5Bw-lyBQgdzeYMNSf5DTG0ewkruMJSMNG5ZILNDFm9rp7oLJUXjwp0X1lbG5Nsu65Qu2nYvLT00W9b1h-OlfOkNUPkB2s141mn4kNIn8JA11na-_v3yEMAPidKMufo_dbmhe-GgrcBRtc-AMcFh5cgE4c0re-Knov5l1re_xiNUVFAkV2tN1jlpK3Dk_3Lh9b4pbw_HTonO7xLGE3qjWxnr8MlqOKlHY9vD5Ls6SJg4i_gE9mZaTXQrDfEj_85WaZVJsrUP_kkYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=rdMV2zzHTm_tRKb-Fjv8xbhtaI1p3nPjCjr4WLpzpNDUHod2z2bcBoMicoRggyzc1vU9p6AIx_Hd-fziIjTRYdnf-TFMHT7bkmvp4qkBbNu05ih1fHjz8APIAMzRKI6LUl2d9lC5BDcVKtoXHWR6Tp6OIpOpyr2ZPaIytE0uMcLgVstMvcn9J1LfoaTrSUmq9KkVpnJkn6UbweRi5vIbYwMwk4dETZzttoIbnhziBjMnvm8n6uXMkCSqSpuz2GV4pbkaeoR2CkKBv7via-CiLFmIM7724VZOF3fQwTb-KDkS4H5F7CfMvVsqW4QLA4-SQGD4M9MKMqBpn_PDc7b_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=rdMV2zzHTm_tRKb-Fjv8xbhtaI1p3nPjCjr4WLpzpNDUHod2z2bcBoMicoRggyzc1vU9p6AIx_Hd-fziIjTRYdnf-TFMHT7bkmvp4qkBbNu05ih1fHjz8APIAMzRKI6LUl2d9lC5BDcVKtoXHWR6Tp6OIpOpyr2ZPaIytE0uMcLgVstMvcn9J1LfoaTrSUmq9KkVpnJkn6UbweRi5vIbYwMwk4dETZzttoIbnhziBjMnvm8n6uXMkCSqSpuz2GV4pbkaeoR2CkKBv7via-CiLFmIM7724VZOF3fQwTb-KDkS4H5F7CfMvVsqW4QLA4-SQGD4M9MKMqBpn_PDc7b_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=PGoRL5aiJ7VZdHJrk4DG4KJ09vRonyoYjI_dScrtgPkyrbUGMyEw5AflelGQ1woZoAzbmMWFJPgrAIwdOBN25_NAMMJ9G8P0xvDAFgx4gWaXe3JdFGvhx-jCXwfEppW8QUxc9J2DjXpnvqsVUCtpSsss93UEQXMN14-3DKUkusPGO8RdBd7SL2BDNaduE27vZSkTm06sYZiav-XKAtYMTL26REbHFeOozvcW8y2pWkyml2ymlD0salvAuP6I4hRLMtw0DnUWMfMYovw88AAK3c-d7w0ThfCjS2fw__kY_h1yK6xcYA4WflJvRA6W1qHJzTJR2unlc0_Y-hw1iZpuIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=PGoRL5aiJ7VZdHJrk4DG4KJ09vRonyoYjI_dScrtgPkyrbUGMyEw5AflelGQ1woZoAzbmMWFJPgrAIwdOBN25_NAMMJ9G8P0xvDAFgx4gWaXe3JdFGvhx-jCXwfEppW8QUxc9J2DjXpnvqsVUCtpSsss93UEQXMN14-3DKUkusPGO8RdBd7SL2BDNaduE27vZSkTm06sYZiav-XKAtYMTL26REbHFeOozvcW8y2pWkyml2ymlD0salvAuP6I4hRLMtw0DnUWMfMYovw88AAK3c-d7w0ThfCjS2fw__kY_h1yK6xcYA4WflJvRA6W1qHJzTJR2unlc0_Y-hw1iZpuIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncfAWajGfrfpxntnQhpiVPIcTyRC-Hwu-V9EPsJ8TIsm44j9rLo3l7_pzzw8D_SBuQyvAy5rKWxnlpOmpdideGWoKnQNDkRP1NGHpoC3W4xCsu1QuwMSQDjCKSliI6AGWr4vRrZtbPn4a29PB54DMVSpHWhNpvhPZBVh52m4kDitj26EgDQqrMIT9J_OcM57YMu7ZVLOI9t1_eKyxKWPD34HDStVNWcX_UuDFI_ACndXFAL8cpJ_9QVtOUZdjVtgSTW6TGtazA2ZofoUuzXuUQY6c9-03Xw6Svpr3ViNL19CMUSW91Z_oUeguM80HSNTDtsasm8_unxzqAP0lz0CKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l33vm-x3g24qXiVrZmmvs_bBS36aSLbUslsvHwMjmmnrBEdAtpuAJD3zDTr9M3lA2pm0piAgWF4Ut96oxUL5NEXDUn-2yIEknPkQE92QXdOmV5L4vglEY9sYSc3ups0JIvz8w2hwduneIgM2KomROhwB59VaLAtbc5kf_aE_Z8TsJkumgkkpFeCs_v1TL6n84hlKYGfCQs1p90s_oWYbwMDuu_xWA8SlHkIS-fn8h5N0hcuiLtxw1KbJnyQGDCO7SwiqV9rCptHenv0Im890fznB2flT4Ja7CpSkScviOcf024tCz-PLSiuju6znt1BVUfqvRlIbft_vL2isJDyt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENAfrmWfmI6qU4Mi7qJPoiReBjuBd7obwtrJ3ynRPyXClvzNz-DKpDlmBoVPy_HRlVDFrmwptr-wYt0iid7HMLA0F4Q27dizqBIv2cAtWmkyvSe5Gk57d47Mh49750XlqvWd0GezD3WNn589BVG6ETmR-lh3u2xshdUWFxhHF6GtrXfZpbGvHAQ2TYhDnRmYdhp-x1hp3vNhkn2wp1Oseo8oSk4_tvWxRq11QXAsW83uV8XhKe_PQWVLJoMbXd_LlJL-GrsCfwS28ReH4iNnf2WFTDma6ZT-SWzAN5m_L7vbRZnHYt46klvU9DSuQh7FBWuc2uQp7rf9Ea8Y3n31uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtZCObUYu3lp2K2sbuQvFUgZZZ8CdlRUZD1Ukq9wZhhyfN4eWSQ98pOldWQsstL0NmY48CY-jxWV9z00u4UhGTLNvdDTrcMayRIFUsjCKSdElneDta3pyX40HBmu3Kf5oANv2KDWeF0R7lsWmJtjZb_PrdUuQS6D0rBPvpKpUJBgCWn-YbXtLLVIflzQ6zKJAX2sw1fxdou0oZ45E3KQW5BGzkdGjmJBsA1WoViZw5LfD5-koToDxkJhgLfYWMUvKEaMEzcERA2dWopdKCzSRSDZ7V0MK7ZN6A4ERZButnQP57IDElPVVpU3q82ed6Ygw-F9TSVKxm0TC6aGLx0Y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-UxO7OIh-x7Sp8U3yaLwpYJsbcejgx9gj2CI0Bz2ICQsbut9PxolZjpxQPJ5vOhlEbxPIB1IWlT_PtRjDOL-QtiOZk-1OX7M3VCdImirU42S_PfwUakABSEnQtiMmbDLekTTAFGkbzFDY1IpDqlgGsX4745nGm4xPPNNC2MS64ZJNIt9S4DSVG-8FC_U9ZE-RyFuXaR84xRWZeDO1D3JSlmZktT8WgRPCHmzY6kCFkBn2PnNjBssTdw7LrgYCd-FxX0N2j8yMuoumNJizH3I6vrOIjeDcvoPlqyf-g9FYTndlgNIbpOSSDUYoUi631zyaginFjRYXxFFn3T6gJytg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujtt1D1ZtdYr56EqDWdjH6knwWOGUe8bxpE9TId3bjRC79LlTO1cR9Z7sIqXt6p3mMlwg_GBvZvbP0gs4vNyZrSiSWgAG_CLq7lF_JCv1Nnih5kDtiyPgOee4rPhItKEU0DuKrLFdRE3jACC_ttny77vPoo2G1foA9jDgIAj9C7fQi1M9AbcBw09ThA_jYtRPM1JGkATl-wKC7JspCsFXNdC9unmZ2wUj0SIBxzlywKapPwgjdnMgyNihVSk3a-lyAGPTP5ye-wtc4Peaxl-_JeqJOnmVnVSMc9gSbIxXxthHDKKUHEZbfBG68Hwt6jk4sLU5I4ux2aX_8p1BlMA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYkTQ2M078YOyCxo_b93c1bsdq4FMMeX14W9sTx0qhOn8SBWEAzsSM1m94nnUFxZ53Z1Tsi91MUzan2aLId4US8UmrMHXGqDqALcCJeNTMnwSYMHyb6xDgfGjVVJVqmGwUp61jpxeGbdgOzQ6HFdT5zdIQcrOORUbO8lJylThx4kJMxAredjbincI5g-lFDH4bhJuzS-IjtZy8h0k5IL6_BGqbgehykshTmtAMJjAiX6T2iQpPgqPvZC9Jkkppc3dSKY6NGoXPONXn5nNWEteIgKKtfw8CHsS3RKCbwUpo4XY39jrXEn1jCSbVeZe5h11JZVOivnADyb_kCLxHGE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9yzwq0gqI40VYGUBcYVK6Nn0PHC7K6Ten-9aBTma4uMzdJL2OGzXtzLz2UBoscmCmSPFamClPGtNgOod8fY_f6XhoaxU3nzCXpPqIoyBy8hWgsBjnFXi9tMHxpkRAjcJT7SQm9wKF3wZLovpVLdHVb8BoVUoUAjCgLCHPufeS-rd0yGSwZX7lUMr2CYamD6HBLfr50RBtaIk64Z3N6GzSavc5tzNdZA1hxAJCNCZHN31Y7pQeXIU4afwhyAV_PaEMcu85oTdpsIctazwVlXwLXt0nYPPRsULnZUtD3qpEehVmqVrym-Jm76bSFmcP9sg0uaXcVJinQbZ-epuHwYmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLuZAV4Ui8hH1hTUWuOqywBtDgni5QHj_1Xey1dy80A_TTxzIj7PLwq7bqLxmnNTpPbA8F0DXG0F5ckZqz2ZRKwLNg3PJaDAAoICTRPtIXK8McyZgCYtW85GqXourSxKmy3ac1HfBkqdgRz48-8oPfn0BERPjsfW2fl0OFpaYLYMCrL_C0p0V_sYt5rIUEV8nQ6TdWiwr55j67DUZNPvsRfF6mP8VnmghwCrL5fWeKJtlNikqEKUa1-3LNQXvXJH9juCVwQ4QHfhOmDu85347XxqRNUZtKFrISMhsro6nuNueB-ysHeOomiGcd0XQ_QZdTpgGR-6OGvkt0ODDIgMYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqxH0HqsKk1IzQlBCf4z2pF8tH-siWJuNKLtCuI6QQcW2zt6WMiKt3HN9U9SRb7hXi8lt8SK1HW8IyWSKlj9qtEy_KZUGUREn_zYzS81peF8azNLkcfko3BzbJci4ELGNyUxlp_NY7wuds_9RrHpWB2QRIWka7aF53uWjOocQEghiiuaW7ALO7xYJrb-MrAqIPVPuAiznYbchoiiKN89U08bXyhqlswHOXQsj6rVdWV48MHQ_CoEGEJsBZ1R3ynrBqtqCp3jDbeWyC_L40Ovn62t9tDFJx6FqkO5EexlpmVWf4ks_v2lyIzlxraGQkz1-CZU3SSD6E9x0cIaqav8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
