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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 17:19:42</div>
<hr>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=VkgOXo0uZkLAuw4qfxLPRvmdELrQTHzPUGgIxXBWN0WE5UtozNSrJ78M74CPtWHfCPkBV1oBTYnW_lZK6DRHqLxEl156xOnaQhMcxDPx50DTBPI0XzT5S_r2EqTii40kBZU7syiU7yhkTRD-wQMVkLPtGqEkRaN63lTN8ZWp8eWjEPDBuds6rxaDBIk2aRvYD7bL6H6DzeDcwU3BheWGKVPPYW4Pvs0ES0rmtjOVBApbqeIQfrVHxUeghFYJIwCA-wv-onBpZ_MiM_yKXA3BzfmLv3gpoDrVugTsZgivBYz1s37KOPIL0VGRAmSRk70EQSRRmnocLMM77CufeTKznw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=VkgOXo0uZkLAuw4qfxLPRvmdELrQTHzPUGgIxXBWN0WE5UtozNSrJ78M74CPtWHfCPkBV1oBTYnW_lZK6DRHqLxEl156xOnaQhMcxDPx50DTBPI0XzT5S_r2EqTii40kBZU7syiU7yhkTRD-wQMVkLPtGqEkRaN63lTN8ZWp8eWjEPDBuds6rxaDBIk2aRvYD7bL6H6DzeDcwU3BheWGKVPPYW4Pvs0ES0rmtjOVBApbqeIQfrVHxUeghFYJIwCA-wv-onBpZ_MiM_yKXA3BzfmLv3gpoDrVugTsZgivBYz1s37KOPIL0VGRAmSRk70EQSRRmnocLMM77CufeTKznw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=GBXZ0RlZcZGQ3odp8MYklRjAYMYnleEUphkbswMpE9rPe5j4a1pZXpLtHtVjWAOZJjaMLY1Z2YGyUctG6mPscprYUxlVXYAUIqBZWRPpOFa5uc1G9gJZSOQk2PR1fVuNchfkvIsKR70wBqAvN1BOCyXRQ0NHf9pxamNQL6FiSduoIieAW9Rg-AVgBBSEKTFRhhFd7M09YpxxiB27uUvjBwJtqND7e94bKLHuMpdMTkMaaxOHqdlIvSN22HkXphHwegySRxIP42vLeuVhcUzdvPOVOoRcA5jhriXGP7v9dKO_yly44BH2U0bVo6J9eQ5QCvFTVIC3TqU9_O_siBKlOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=GBXZ0RlZcZGQ3odp8MYklRjAYMYnleEUphkbswMpE9rPe5j4a1pZXpLtHtVjWAOZJjaMLY1Z2YGyUctG6mPscprYUxlVXYAUIqBZWRPpOFa5uc1G9gJZSOQk2PR1fVuNchfkvIsKR70wBqAvN1BOCyXRQ0NHf9pxamNQL6FiSduoIieAW9Rg-AVgBBSEKTFRhhFd7M09YpxxiB27uUvjBwJtqND7e94bKLHuMpdMTkMaaxOHqdlIvSN22HkXphHwegySRxIP42vLeuVhcUzdvPOVOoRcA5jhriXGP7v9dKO_yly44BH2U0bVo6J9eQ5QCvFTVIC3TqU9_O_siBKlOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuTDziwN04fXK41NIBTUchPlO5gYpc2KrMTUDwD9SuObJlTcCAbiwPqHY5j5Tc37CCw4MqgfEyaPgKJ-y-bvXAG40KcadQQle6KDry1fBbtFftUj0oIPt2DCq001MsVJbbEvIY1UthJqjCuEttvmRS9uV6JlrDg-fH7PKHyz2QmqqCwuaBiNkA25ZrPgiES-DX_9wRpsHEV_m9hTCPq197GzzvLNiQ_OQxsZblzmFR7Uh6r1mjr-z7O6uY3-bLWauq8__Rkq4FnPJ5GBnbeMqrC19kX6Cb4HyRdDYLjM-Suf2zdNHGjn02XI0ZfyEHZtWGKtsD2sTWrIvE6OJq5bcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZyW9lFixriPk_TDV4HZ-GTmp3aMbzg1qi9xGYU2jaoGimsm52HU3QE_YnX6MS3kejmUMHgaBvkpy8i5-WBKuX9Q_0d5lWqMfusKPpbyPEY1r8NKvTRSL2p5EqNkEApMWC5H4Bq15q_86DzaxVar6QCIgvsOAKqM8uJxU4qRsqyGKEaB6wmybW6G27xKxMVikjNmA0riIrt1ONOgTgfyyqhWGCTmDtDOEOeXgkbC7ZWVLthWLdpJuo5I6DfwBuaAa85BPxkVZ56-wpabC_uQZGG6cCbsSv177ZP0M07Hdxpjj4gK6Da7sijDNS5GT_ibH1lpP-YvVMWfP0uLvtMzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uujkmZLC9Vav3wWS2sWxjNfy4_11pkVpimr5ipSSiKmQZFzT53xbunBiq4W1XcJzawaHAhceYML1EmZIrGZz1ZS_je9L1KKdOHoSCc4RkArWJhgSMQEjcAcbhi6U0t2z2ttFOPBMapATbpgpntXiNbarx_lbi8rj2sASAWi-IKXOp7gliknxj4vpYwuTeJRzTD56XSTt1-7vxiD1MU4QsPZJVfHhIr7L34HlZRSOHCRoytvKRIun0ZlINSDMw1ipERKk9hFKj0pHZHVucvI9D7TFJ-FxDasMI1m8Un6nz3EzDBxkZLFGe4J99Mg4m5z3XX-f6g33x3Q5Bm_Egu_72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBC_H0cbeAqW8pCHjMsPmKInwwQNb_u_6Z8JfFrm6oGYB3_-1srrTEtRpsbXwTf4_-vVrBg9p2d2-5Y6RoiB24-QJV-1lsXzc2bfa-hwfgBBReoy-_-_UIJHOQQg55Ux3T5XVBbmV-W-RBLQZzIyD7ze0Le95K5rjamnkGUQPglS03rXJ5peSq-J4SSVjJwt8rTVBfElCIZB9XcfdLMYbQK6RC6iBdrTrEcGxNkCS0K2DMweLt0mPn_BIJNWpPwXbuzn-Shg4014Z4cMUerjVDHrlZnOAxvWtP7z4oq3ynfYGOSwT7Wz-XAi097XhxIhN4ORMY1yXITl2dsdOAuXrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9xkz_Dl2AfXUhnBlHFK0GgGn5-5x7iqZld1Y5UYKRhQBO4ldxapU1CvTw1EhvYpibJFoYaBml0x7w_W1mXJrprEokl3ATDuV3QnYd_ZNX3dJ8CURCmizzaMH2ssUjFRY2qRTB6w7-FWb_nASBzJbGAO9lAXD64Qi7xec0WMkp8vi1QBgJDbvP051LQ8xCeWxKFDbv4syG3R-yz1OEgrq1wZ6whyHvZZ5fTJqNx2gJpMzyqyNuIaOwpjtULsqkUNkU2oi5wLG0uDAwJN0vTCk-Tnw20OkXgJiPGAxgy86KlZR9RQrGoAELDA2yTt-53ZghwGYe5x6pJnnqLkStyYzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srpUwUGEiqptFoKzQNOtT7GSBq0M8qsaPI08FNiLHCEDfHOT3udeF7LzEvE8caogyUZW_PNy7s3ZZg-ZaqKcqmDl6pWVL_Hu3UCdBugdeh4TVQ-CpVyUed-6KtmxNRX_xbLOUaFW2-Mgn7MKX6EXk1C8q-mkB8c7ukVPCwHqheE7rPBJcI08Ov5N1yk-_OFLvXozITHMnNGEJxVjHWbhV5xBVi2ML5U1JDWZKQL_INd-Z2YPVTNs6B9Dn_TsBkyp0rRwju0y-CNuecuH1Z0ZFYE0NR_6_k11ZIh_1PJtyk8zDc0cfXopUwXBdrnfvBHtuMpNsSE-7oDUl-61Veapfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWbhz3gLBdBSk1szOe344XtEiVN_JWcdljpPevjaGtZKyiDsy2uCPuG1URsnsnMFZ-hj2iacFKFs-AwmmwOy0f2PRanjzSe3B1CfW73qrIuqDPkIl4lxUJqfwePDk0mbl8nf8BEvlN7G2VI-JjX-39M6GwtSS6yD_4N9AUprKIFrISgVx-8j7YxIAdFk7eJ8s7pfFtcbEgdHCM4Zi47YzUlkbpW4wjBVYooOztbcTJxIxXRyxLBnrCkehrrvS_lg_gJn7jzExo4hw6zSVS-btsceKSck80d4ygS_3ETVrmbh-Im_mp558Le4AznpkT-sT5WVhKXPz3dl5Z8P0BaBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR4YNPhiMQRdnSAzNF9Amaai9YvEyIPDLZsDICf7vzpFkX2X57jtipUnB4a9fiqHPjjPPkBIpIMUGygn-OLCOUqyrSsQNrbj1warzucQHSzoFotZeNPJdn-eDyJvWyjRsM_QHVfsRxpLAg_iBY64HkXrsKYYekAS0p-uyAeCpjg4dUKtBdq_M052ShLAPDuGo-YXDxOYsCbQmMGNFc3kctpknmjQyKSMiR67pNNVdfIWupaMVw-RK8YGjaRd1cpZ_N0t1rAogztQ0o43FVZ34leBPcEr6Qbkr973oS8EYPmQf2E_TPSUPNE5eEqJSMkS-4oufTG8Rt6OnMozF3x1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP5qlvjpmHNb2O8vr2N3h-NK77cDcN5QrW4K4pZ_AvC7-_0EpeajC0p95Quf07T5H_gCDWIyuYdFL6bvKA6C7T1fk5CkLGiSvwDlTndmO9JNVfgfjSOmb48_Xm3LmWzvT_4LXvsvPjvziZN9Gqho2jfCC6mkCjYQB70hQTAJ56ztCzxcYynbCl6cvvDWPLHCxc2pcdjUy3_mRsXuoi2h_miiZ6YQN53JZWq05JafTbyQ2FbLfr9gPjH5-qua91j52kU1s_D3-RSwav4PFkG041A1lsSITA_xG3Inp1EO6aS2f4xkm_p783tSYRRBZ8sT8Psg0Eg7VTJ0OOj9cvjo0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBB_NlHTR3YNdWknY_vJ1YZWy1boBzdN723ifC0GDqpiq6Dtpf6ctwRhxDiB8dk5Is_tkHFxjfM0JZi4ng_-PF2j3Yer5GrFOvfXC_spTb9sqBe20qzGWGyJ1hc3IvP5wfQ3XWQ48Cbo97idnR1xvWYQEQJFR9STX4z0BOCoCGq6ZdjjkAnuVTynW5-qShjJWV71Yv6OcykLSLqio3kK5Xh9cjIVnWCaeC2cl9QpNhxgsTCKMJ2-oEXke0yExE771qOg8G5iFU3yhqNQY-1ybz8Ez0yv6lWr7eP7EU37ZCwXaAcKSRoK2Njneqk0oiB7qqCYRrNQYJhR-lmW8f8nnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2p1Oi7pYTDsZ4gV8VP9ReEE4774n02xuz6nXIMJg3PAQ5VtFeUAzMUVUBFcO2XB_ZeILgGRSPcv65BFwc0dEpuA3STSMJsX1DJoIoeuhh7y4T-y4vuS87ACM_iZl38GmIzC6DEVBrWto76tZQhG_Lnh0VLD9hJiXrDJV40Ozn9csOLBt2rJVxswix2R8fa9ehjUT_FxWb2jaa-JlLrSg_Adb-FH74pVR9ov11TxB-rkvlKV1gfjkG_DOJ2XKcZdv-DRi1gfBuEzzJJzmGu4CB0ms-Wg4v7uGUmIw5I1kjuYlazobnSZVEV9-t1zRssZcKA_zGkswvBsSW6frK2Iag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WviFigk2hSciDxGfS9_7T8HZRh1DwWRJciN9VYQmLR8YOBQMD2Jptx4Y5ufs1CehnOKZos8rz3lhXSmGCoX6IaveLyHB4KgIcPcvlwMpC_Osq-TXRDmJAdhMjChP9JMyGImufovgIXBlXZmwstfxFDKx0bFusWHyAuqUHluoSxIFUyeuLrP1CxrqEPDVlRwhr4466ukUeh4BbThIkTcOAWbecnIWTzsTFTNfyfZ5IKzuJkS9PWdTSrenwcYaSTmw7umTB7rLmCoNkhhlfZt4WqizKsacMVolSU6YRC0o0Zxj8UF9qOBxC-vZ4RXN5wbdEpr7aEPr8CRPiNQOkFOb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpiLV6Un89XDFb6crizFFEN2pJZ-YVF_gt5AfPYb4hO3U93QIrMSquQab8bI2D0gwmTXSUZVFJDG7OGDYywEbFdSSpFzL2ev87jAZIoHose7B_a-TNDWjq2UqH8VoVl9spOC81oB9vqgQyMVjUtbxqVXKeCkKIy2yeg_u2PBnL0l1bLOsYVfEbI4TIzKKw2TcEZOwJhL6_4svOkTdpaxWYYAjJmE629vcCj6QaI-rERaGjlm0AoganLCSaQWijoq7iO5sxtacECCwJQzyQCGN_qA8w6PDTYXR8SInzJuxCnZ_dedTnfueVg5V-clxzLoXIN1L5BpzWkqX6v24R0Ggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=VuNSD8y1ns576aU21yl-zCMJ0suaYCOblfVgmE8W5uuWBZZce7NwkcKgD6gCmQaVfur8oTjcaLzpU1rHtiyyyekCmr7O8nrhxKxZ_Gol_3K5omJmbHKAwmEI0JcPWlZXh6QIi-TFeBRknV6E7tE-l_IIxUH3jjryOffT24B6hF8Veb7nA3uW5rG1tIvGef7ywOkoAX0uV1XF_4HHiar9hvvRGzTAKRjO-UgJVu_rwFnfzsAXfKik8pV4PdQdKsjKRB5SA11H4PMP_edWfoT6yVnlprVverIbFpgNs1aXfbfoWSjYBQjVrmEASkzAqNgp2KwsJTzvMu8Fu6U0m178jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=VuNSD8y1ns576aU21yl-zCMJ0suaYCOblfVgmE8W5uuWBZZce7NwkcKgD6gCmQaVfur8oTjcaLzpU1rHtiyyyekCmr7O8nrhxKxZ_Gol_3K5omJmbHKAwmEI0JcPWlZXh6QIi-TFeBRknV6E7tE-l_IIxUH3jjryOffT24B6hF8Veb7nA3uW5rG1tIvGef7ywOkoAX0uV1XF_4HHiar9hvvRGzTAKRjO-UgJVu_rwFnfzsAXfKik8pV4PdQdKsjKRB5SA11H4PMP_edWfoT6yVnlprVverIbFpgNs1aXfbfoWSjYBQjVrmEASkzAqNgp2KwsJTzvMu8Fu6U0m178jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrbeMTqsyJ63zzjTPBbGDp83rJ8rWi31pZB1d0wAXvbgzywzAI1hOv5XzuGwYElFFn6LRzkENjRxyVvODsroAaAITfogZoKf8o6O7uughPwNttSSEQNR3QfG1Cqniai2p69T3danRL7U3qabb2wRGJoqPAay8M4fLsWqJS4gJYa-4LYfaCbX0S-PW79WHuT4smSLdyZB-88oWdHFsgr24WvzOIYzag_LG9R_d5yY6-9APWrO5SH7uhEtZh1EqRQuA8kyJlexrMDFL3cEJPIVRT_DhprJb2u0yE4ouuMsTzymKbWrApaJjLBg1DkXzZD0F3uHJPv_wVPvf19IutaTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsqC6BdgCBDffNBM3BxHzOAA9BtpupNbvOBeGYKMXD7RilL6CS05zNKpbkSA4x-8mV3x50sxmoEb_ghZRVxB1HxzDAnb4GNq5MZqBgX2Not8_nyrDwgR9yKA8Rmqn2iObsUNIsGTAz1oF9QBl_zXoI1DAsUvSSyFR9YKzUrCDOryTy4uW1n9hHz-jNmokk4xgvxhenVxA3Xp5m2yih_pE1cUjWPrIAjSbsAuFhaEhQpf7y7-3xwBpgw3hOiCxvkYdRQQpTyB8LnQTAPcTlwW24DA9QulONlCGjxzQUnejQIpccbq4fHjadRQX4vOsX34BUx2r04gPgNAIS_7RuJl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxyZmZw3Lo8Ju-Jwk_L3UcMBQzivr0dFsKzkZllxpIzKyuHOkwcEpV1gqDblnfcCxraQ2zSGQahCNYcjXXGd5s_Bd_QFi3pXGbvuGqbBpPmZYfx2wGtuv8pfRJgGzLWBoqGUS6V7AH64WaSEzTGgjvd4RFhwP33yxBO3uDLLgz2XvWjLQec2fVkq2OBxZ1VhGB7bCe5Rcz2Amu3fVOw3Oxun3eAWji5wYRT-uNph7bo_e0ucgW7Xe9Hh-m9Bh3Wz7PiOnLKEh_i20ZrqVukEcoGb5I6WHJXnrUgv80SdN1S7OATiyCELQOG1hnClbnQYFcp0QF4B67AaxN_Cap3kvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olMCzcrcU-87zjUJRoesjXSNuySLfRAJ-WHCEE2fqU0Gp-f_OgvUYYxvAcv-ew8EYCL44j5-fBJVXeSOAFMLJIiYom89ipfT4CgTHO8oFxkMRFBZ4SRSdb5LDECXteohKnlTomAKQHf6ey952GND6KWE7LCfZqL44oi4VEkwdUU9YKU5tdFH1HoZdhv4uLQDYkquoR5ylZ633mDHmKCc4dyrsWJBpeHgSbinOFM3JkGsygbDaY_t4l494foHJTlfBFfsPKkhi4PnP9IRlZmZ-BSCu2b4DW-uhqPsfTX22xt5nSFSfXP4Zsd3Z6HHbBz8qXZ9-11_4CJDrVLoT4lgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpyQJrhqqPJN5kbEuhwjAUceRUS1XzxuEIqP7Sd77G3j0K3hgqIdqV6rc4M_izPpQiLmiySLjw5XjqBMUlE1VGcv2xYwnojk0vbOjv88135bKEsWmMPUR8RjHBxBf95UpGAgM3DTHQ-8ay_T5Te5m0XaVY2Yl8DIDZ7tzZSoyEZ448exo7F3ER-nPAr_FZJgp8-mN-0FMVotiSveLKkETDvdSxGk1NQ3vaBsR9uvy2XQf8q_vGlkA1hqxOZFWg5hoZXH2JgUjb-MkV7FsADJ44SCv6jHVKrJwOEIDBOM2nT7oNXQtB3-pkW19UnVqh5w-mdgiTh6Ub0NQKJdocHLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsXC34HRvpKucJw9rYnStlgz8w68oVHlRfgusbYRZ6SY8zCdFOiSg18Yf9bh3H7J07CNnf-2zuaTuCtfnF8zgBkgxFAjOALHCSb1VqU4tIzLZgLyXT4vwMcBl1s34fzF4F4GJ5EoyuaveFvnypD-zmDjHHz-p-rBKhafyDc_7FGZdhAytzXMPGjOHlbfrWjSY1EETwJVCATwQpOhAfgKd1K1-MimM-_mpncFjATWf8Fez0UdXn6GtvmTgU0jVM2PpHx2H4d1-nfsE54VpeaYalOxgTgfirjMrFF_P4MDdLn9pIBptmvCMGMvFCcihybHmucCnXv8ZJsryhrTagdZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZvqdGqo8cq2IlsKFNwxvW5xqFPr88Zy_zP1DV30F9lwxvZp6HOSS_tasA-ANIX6MdYXwJpJQDluLvnqoJCVBh1JCuXAPDTjMjjO0k9o28OLRmwJovngqhsbuMAgOpktK4IYDs0ZOST5rcLF5tUMI4DivYARv095j89layh94qVxf_Ajjm9y5Uj9Hfj8-IOQdS9KU7KCOEEJ90F9OQk1BukYsBKjAisYjAqr6Mfe9vrImWcRcHBXQSOMwFZPs05fm5lkVr5YO2Z-ij7e10QnmeTtiRDG79BkUUtbOz61YWKniaXUBiYU-ZQIFP3hgF5HLUP0qmebr8R0e0oCyijiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8mR2Wo5o_wHVz84FnZlWABWMhIEkNqI3qDG2MFbU7bDcLsbp1UFvZBEGwwNyRRyp2l1TFMDNbdhPzNNkDPKcDIP_yleFfATr9vl3G-EiMpsFhWa0gXAA5lrdV6cDGLn_adNYMPSxm-8IUq74HD5pt6_Gbe20K7syr5zCoK75ulwCYL_p_zmFms91mwR3V3lDR6nn7q6JM5-TAqogv4uzIPiHEO_VQ5K_IcCzNwq89n1VgnD_HjIpmJ8JGFaPc9rsbhsxXr2PlmXVj6N8qklwffhhjwuwUES4FaT3zbyxaP5RM4AwlBciRseFgH5Im2HJx09E7U6wC4GJaHl4nZP4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=eIh6gU1dYFMug9fRF5LtbwB4sfculpuQDsnPAK2aDGKDwq-0LGC56MXjanUy7o16YAiPSDGgOn_NWxhRyTCpxxJujVEJwPxgubjSFODMJ0QtqedzE4fwTsY9Tbe1ao26AGD04e_bRSsYdj_QlMSjJFMLDfiV0jxnLx-qQBQ4H7PGwTARB69IkOQ65F-TZMtAqADqMPbUOEHJXRoxEbjqTYRntASIP5Y4yPVfSTGad9g3OngMio-oKbhDG1oCU1nQujQZtTgIUrbLumgffKjj67l9PkpoTv1PO-5Cd1JDAVksz1gsq4ZE7YN3XNM4dTgJb322nlBEBedEG1Osps2ywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=eIh6gU1dYFMug9fRF5LtbwB4sfculpuQDsnPAK2aDGKDwq-0LGC56MXjanUy7o16YAiPSDGgOn_NWxhRyTCpxxJujVEJwPxgubjSFODMJ0QtqedzE4fwTsY9Tbe1ao26AGD04e_bRSsYdj_QlMSjJFMLDfiV0jxnLx-qQBQ4H7PGwTARB69IkOQ65F-TZMtAqADqMPbUOEHJXRoxEbjqTYRntASIP5Y4yPVfSTGad9g3OngMio-oKbhDG1oCU1nQujQZtTgIUrbLumgffKjj67l9PkpoTv1PO-5Cd1JDAVksz1gsq4ZE7YN3XNM4dTgJb322nlBEBedEG1Osps2ywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQ2T6zVnFDbqNQrSpB2s6lBzaoOyosmxA7l3-xkl5bi84dF5hQ_Yal6jXHHQbR-0eylaLCXF4km2QmE92-pzIkZnItr3pg-okqRf0CqRZ5wn2dlBFApdqlNWAr5GcTqi1L6ZGygZd0M87MgBX6mGYyQDiMPZd16Aexm2UF1k9PJIOS9HxQo41FcXvbFfLRUc03YHaRLTei3zouN80EuNsL7tciDocsG_M57qNo_xzcx8yWC_YuR0vB2b-tI168c-8eQqRKEagj8UAxfabCCWzML3ws_OHmtqtSqBTky7hva6lWuZTch3IN2ZGQex_jePuatBU9oa7_48qvMVTptsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClvGI5Fiw54_dsL7MVvbUpCjfadYPhLSIQm_8F7wn5pItn6xLExuH7tat3LruGeHKVEmOULms4kfngTmWfvM8wgsVTFkQqyzOXekmc8IzhCoIkMfNU2Lnajdb21oiPULwmkkLlC2WmybOaeROaxuefVyXXPcBn4oQndVimPw3BfXeZDwSy45vl1LSsMp87VQiMBnluRq0eDX3ub-TmiiFZUBGg4rw4r-T_UqZidiz8hXdG8GpJuo2bm-_uWh3tzrXqwNmCdLafMOfxpO3X1lJy_fDj5kBnCI0ztH2ZzEhoAdrNH0dO4n4yxbTo7ZB_jjuRP4tAA6JfYWMgsqSCyq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwqIHtHkeUbDNlCEW5VVTVeVHjSxR4FX_0Yt64L2yqkNxugJYU5XQsm5UDyUKAJsSJhYfejxFRZozuW7GUrgmzLdXo523QM4zebsFEubx9dZI0SSMKHwxgKXsJMLV4BA0roz0djCLqgKqentchCpA8EEz5_oWTMBf9kaYtxyWCvVzn-BTP6wGY6nmz9KfWoMbKOLLi84GAc63klqxOQM518TWoPYlVx343g_mqhxisW_Mxbh6TvN5qT45osWVnQp-nym4pB8rjcnQCZbn8VrwtYiPMWew7LepBbyAY-7zKXNhjQcSgQ8LMEUYYsW3g-LIx55JE2jLHSZxNr8a6AqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOOtQvk0dHdgpZRyijTA10rgBlo4XcXe5F0gdo_clMHgE12H9-lYnMD-8WuCgbZIMfKb_BlQwxbn0IVsZlAXzfE0bh50kVN_v4zCCwaRi0Wku5MMXVM1DzjByLH6G95AUnlJiw2ji0mL80CIrCEFyXi06U6LZy3Z_PqcsZUDq-A-NjkyKJVG4wbKoQ6rzmxR4rHzpjBJL2i6CPa0qZKXgg9lkveB-iceGym8zbQqwW2NaXWnuozVRDASn769CYan55x5n6DjbLCeQjCXoj90PqZYKyn9wayvg7gjCGf1jePRPPdg0Nnw9GJ3pqkKffPBrwoE_RPFXzBzqfBgKvaK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4Fid-Nb1GBExhpvvhahIObK1XRMewF94x_B4QHouPd99nfKIddr_Vw7gbAvFqX3A6DmpITmcc07bMLRPJddBFasub_oui5eOrhvF0f20kV1UsC3xQs9NNCv-TcdLhKdvcnHPh-3T25VwYU0bR8io4JeBCd9r4j7w9t2pmXDfYjSeD_tl8NjqjjrF06N4WJNau1e8nIvH5urOb1ncxNOHrp1oj-Qp0ydacaIIhVl4F__pFuobUZz7eJapOwaQdzHYF9w9DHlHPhQRT8OIjDql-16BUs7HkJEnrlOVNQpwj9Qafpz0EMtSzVW3-mMjX7_VRTJxa-EfagxlyuMi6iYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf0-xdz4PzAC2nPqBJroI82cW2pMmxruWer0z7xvHMsjWwY9eoSqV9_TODCGDUlxAEe7PuiSpDC4bUlz8KOtvj6QQNlfTictktwwQFNFA93UrF1wMkf_SKh3n6GsOaCySXBKzNFJ4jnVoQmAi3faqMIAARoHkJrUTGuhucQ4XGmAiH517lzym3KCelHd0bbn89RMLfiMoXr2D_CCssukkYTYmtiLdvkNaFuTbhQWGdfMmbv2ufeTskyhcu9KMXBsUmF7fESNefvKkbaI9sKcXAxd6cu72CGZb3Tm2ucTNxIpQR3EO8TknbDStujkZP-USTmHEYQ_CLN5XCZLhmtuNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEK0pd8bQAzRrFb5XSdaOHkseLMMXkyqJ-px3xP0ngkJKiK3R6kVpVIMhlDAM4n3cQZQIOnsR8BOTYLomyqm_JSo8xvqXDgdpYB5SRi90cK0y91y-8Wq-CO9LWS_LwGJJq0JUOhI1ZfOMSuGqMKwbTdyqUKrwHpyKIuy2tbrwNnaKF2rpRjRAE84R1Tn2sFrR4s56rx-6XxrVHoVfJfryQ1pjXJrnvmJLDv5__cMYJNlDtUud54sMef-tlConpHeoLXcUgUSOnRu7c2jUekrvhOLfnJmiNBSf7YQfqIpAyUTvgiaWNsmEHVuNFEY6N6wvwlepxW36Hb9YaHh6CeWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=qaep3xU7XzKibUp4Xt1PUOVoVn60Qd3JSVqxhfmC2SP3Ut9cgJi5kZFS2Pc15xS57Eb4LnunzEDcNIWCQbqdxk-5oJrrtCwQv9UiFSLOIHKo9Hx9Kwm33Ll_nMG95wexIueC_PptM3rxhmJo0X2qYFAPS9tp8Y7y4ryJFoEtmX40sfo2LDqRtrH4IE_RpIO8WUVAhAlxQ8GR2leU9lgZHTr1QzE5sXNzvo_jpzpt2NaUgzIGHcj_u1oqUAbLG_7yp3VzysZXmvQKVIXCvyZIFL7UjQWtCrADeCzs6dATsS71R2MDzjp6u-dJpjtYLwIIeQ3TkvnkzQGXoZRtwdqcuUBa26uU7melPXdy3nfSedfrytnr8EUIgEJ_JtHgGIun9Rf02rj3y8TGZuShT4f22gnVS0U7Q6nXEiCHuPpFWX3zs8XoL2Th7_yHsQ8ot63zJgkN8jVokN9QpE4dKIa502XRXTtVPMYGSF7-z_LlS5vV7muVyioojFY4c-YpGl27OegFRCyRHHx0Uv5vJB0p-UOAcyRj-yqvHpcD351WdNPyZQY9tW42fOn6zb2oafLMRg0jPEs_dvIA3AyliFAw5AxEfq3M7k3zBQRBm43zv19s3uQ2u16s49NkEEuLT9dAtNUI9PFIR-_7FWA7cHcMMYRG38CSl_nqDtDoQCqZExU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=qaep3xU7XzKibUp4Xt1PUOVoVn60Qd3JSVqxhfmC2SP3Ut9cgJi5kZFS2Pc15xS57Eb4LnunzEDcNIWCQbqdxk-5oJrrtCwQv9UiFSLOIHKo9Hx9Kwm33Ll_nMG95wexIueC_PptM3rxhmJo0X2qYFAPS9tp8Y7y4ryJFoEtmX40sfo2LDqRtrH4IE_RpIO8WUVAhAlxQ8GR2leU9lgZHTr1QzE5sXNzvo_jpzpt2NaUgzIGHcj_u1oqUAbLG_7yp3VzysZXmvQKVIXCvyZIFL7UjQWtCrADeCzs6dATsS71R2MDzjp6u-dJpjtYLwIIeQ3TkvnkzQGXoZRtwdqcuUBa26uU7melPXdy3nfSedfrytnr8EUIgEJ_JtHgGIun9Rf02rj3y8TGZuShT4f22gnVS0U7Q6nXEiCHuPpFWX3zs8XoL2Th7_yHsQ8ot63zJgkN8jVokN9QpE4dKIa502XRXTtVPMYGSF7-z_LlS5vV7muVyioojFY4c-YpGl27OegFRCyRHHx0Uv5vJB0p-UOAcyRj-yqvHpcD351WdNPyZQY9tW42fOn6zb2oafLMRg0jPEs_dvIA3AyliFAw5AxEfq3M7k3zBQRBm43zv19s3uQ2u16s49NkEEuLT9dAtNUI9PFIR-_7FWA7cHcMMYRG38CSl_nqDtDoQCqZExU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=kTSJ67WaEXwV00L1bYGSqj74gCpf9ilfEG31qnqi0u1UbeKdO-C-eYh_kbvKSbbpg2ksltRReV7rK9bdvPhGp743DBPSukAGjprPLSTItmXAy5s445LKLppQJn1RIAA6dFBTIPt65lysyDwImCDLgPhXEoNzVkU1KxHgtNwvi93ZwCHVXumTzz3_Qk5ZUvOiT610ZSs6z8nbDCIa9bzdk-1H_cGAJP7kCUXBWqA_aof0ac3i5BcIaiNrUc-Wra5un-JBUHsidOhJBI2JYvcW8n_KM4o61-Es3olY4_8aCSvG5CCVutrdS1c2n9_nEUbcNe-OJP1SSZ5CBf-s74eKsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=kTSJ67WaEXwV00L1bYGSqj74gCpf9ilfEG31qnqi0u1UbeKdO-C-eYh_kbvKSbbpg2ksltRReV7rK9bdvPhGp743DBPSukAGjprPLSTItmXAy5s445LKLppQJn1RIAA6dFBTIPt65lysyDwImCDLgPhXEoNzVkU1KxHgtNwvi93ZwCHVXumTzz3_Qk5ZUvOiT610ZSs6z8nbDCIa9bzdk-1H_cGAJP7kCUXBWqA_aof0ac3i5BcIaiNrUc-Wra5un-JBUHsidOhJBI2JYvcW8n_KM4o61-Es3olY4_8aCSvG5CCVutrdS1c2n9_nEUbcNe-OJP1SSZ5CBf-s74eKsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVMLD3g7axxkinYWJjScziMYyP9mkNNnkvMKVRuoNZDgwtNk4BLfD-PMys7g30DlcYgLEaSNWLdxMjolMGuNbg3A1Jp0byugy-IurefSUcr2wUvMgv_rN03KmrXXF66fIEOTW413LY2mrLeTXfr8SazzLJ4kuGagST8PaDRhv8frKI6Rhsu25L6hiEweKmtgWbk61BsOdqsO3ruz8Xf0higll27e9AwdYk26CaDOxQ1VFTYRcIWuhQj0RomOfWF8mTM2N3GpDKsfSXQUWQG2dZVocbk6xDEpGEFHePtmrGobUDYJEfNey1BvPHV_tFy4AO_kb3AmUADzMkPiOD_QNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBSxe9tdmIosoibCS0D3GvIuM9qE9QaEOC6lHWY4WW9FULkE9KyVGGChoV3y2hPYMNUcjL641KjJ2SO95a33XTZMrr_Ki8cBa2dB3LhxXO8bHfAnJejyFLIavL5UMsTuC0ZhFCSye_kNEBZNftVoy_MmW8Hb-ztVD19bQfdhj_ly-SJRLLoIuQRDzv2Weun5qfibE0dczfiNLwVD87NJAPb2yiiM1z17RlT6_JTVAR4IPrsKRo55ZIN6sq-70nJ9-lcEOFpRVrYXzy4iBJzbylypAKCPnmS8ETmY-V8_MUi-TFyHENBflvUjmaXdini0jIdd1uHrfAQpy-TmEThiBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=ZLXQWpDHaAxfNuJCZc0MFndixUYcnmPvRmd2NqfE2DkLxHJMJ2PxzU2w7ExXmnl70zb9vL49lxQ-m0DMMDTcT5S85OjcrdI5aZ3T71PxMqAQZ-HpULxbWLxak0UB2JpOaElGHvKbtYE6GC2FB6Ea-RUsQevAcEx0X6PbqLkBVm3KOKGvPpS7GtLtKIYqbXOQjbj4_loGGNMvn57BeFbmWUEEji0tsCNEZ5qbdmWPYewGkx4OIJuyZk5ZSgAGiWYnBDg-B9wyzG2l_HfgA5rA7QqyxrkkBQ2Gq6x44keooyE7K34vrup0oDbN7Tr-Y_HM5sGVYPFKcNTCnrir8CXHOIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=ZLXQWpDHaAxfNuJCZc0MFndixUYcnmPvRmd2NqfE2DkLxHJMJ2PxzU2w7ExXmnl70zb9vL49lxQ-m0DMMDTcT5S85OjcrdI5aZ3T71PxMqAQZ-HpULxbWLxak0UB2JpOaElGHvKbtYE6GC2FB6Ea-RUsQevAcEx0X6PbqLkBVm3KOKGvPpS7GtLtKIYqbXOQjbj4_loGGNMvn57BeFbmWUEEji0tsCNEZ5qbdmWPYewGkx4OIJuyZk5ZSgAGiWYnBDg-B9wyzG2l_HfgA5rA7QqyxrkkBQ2Gq6x44keooyE7K34vrup0oDbN7Tr-Y_HM5sGVYPFKcNTCnrir8CXHOIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONEwC1PICqf_qtEw6h6GLdwpmhVKHMvyAzkES9_Cv-ToubUaWhuRxVE_JIEG3DXqTvSyGF3rtnhZUGi4iZfpUv0GmuTs1MR9OJzj5g4sJ74S_tIgvIftYkXzgdQFATho8vwtisCCzAH6_hVgGdakvbMhnxBofxYX54czA9gYZeSqy_SdVNzGxpm-WsC9eLhfzrUmZMiV-xPWCfn_QS-ns5EqgNn3XJE9IlVmkklWLNfvx0wiXjxvLi1esZq5IJvsAgb7w3BYKMlJjDnuOUbwhyWxg0oQzKFQZXHr-PCom68pKbil7VOGSM-rVhB3lhBdndBFcGp3IAmfhe31pAuQag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvxpoG4AUX3ykMU7s2Qi_dpuFx51Yg4tLOnUQw1amRQhcSHcgUZ98M3ZJmJ-rjMa4YE9MwExFmZifM5LHfM0GMoN-OoM_EhJN4JLFE9veNCXwHEs-gixnJMkv2IrMeYKluVuyrEtwE8QBLVHCMBj71isKAptGqfT01bBKc6GMRjHpa97Edzseu-W9vts6y_saRgrThDp0posIhg7qdKqHI0RmtznyS77ykWXqK-4rNBtl7nJYdWkaI10OmKWMW2Ubh6pkNB8FOiuDAuWr_RQ_fbToMzYq7_rBd7Uh9nMVedvMLufjOyORqS6UYPNHfLdcGQzDuKZ6h92nHLFDcBQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoC-eiuNiK4pfNW_ma09TrtahzWa5WZ6Bjelzxj9SgRIG72gzrASu6BY0hRZi7q4ea2WMe5aO4iUJ2UNAizssPFAAev_yfqV5FABkXsfkBIgMDP1EGdtwsPjUizveK8EsOJzw2pdf6hCzMjR8RbiJgkXTenDLp1cORoWtc6we2jddTeUJlSYnMgPzBi3GZlwF7rQ7IkOFB1f19dd5n49sJz7fgUUkTKDCZmRrK0HcXbTpJMosPaYAQaZG-eNPlX1KMMG3DFwv_SEGOlyZ6kukZ2Lf4cKvwhx3VUGY4wa6ccll1BKEDIUdE1jVcIH63EU1xIrSHrubA-8iK2vJCmumQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NINRIbgfu4vtM8mzj1X-CajC3cQlml0fAHIkMv5xV5mlV8cmWJdov2WTAk-MlJyHVmIHss7lMFYULRiXv2AV8RMkfhnVa1_G6Z9xs2MehGmeV1zQ9x6a9W1ZdLV-yQVd77HOg7oGrcZUg5OS11fB6dJWZrkAm5SFB4OsgeglKLQQ0gtEMgzSm03eNJmqoijY-YdxzfG5aVRp1jnVD61bCWyhi_tgpwskAQl525LdFwA_gtWdDXxBX8soUp0iruuFnV2RtNMGRa5s8KndwbqwEgQaBylHD2DFAgTZTquFLWPmbdUUYsY97MTgu1gS1hmTwjV03yc9HlXQL6UTD4dZ4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ggfnmg2atwww5j20VvalLJs_vPd_tV8zxGK7LdTI0dolVJJAfx4iwSyUprDOXLyAbwXZEGH-9hcjJwoFAa3iILhfrkI1tVDVnDMzC_sx4833V_yCKAPqpMfNe_nKgKfBzEX2ITddubhDHb3VNx7XhA-n4s3YIixn_jJxX8_yGseEdKYSDr-OFwh1V3d_wDzoRzQ-26ffE4BWSqUVqMYHbu7dkzi1mpSnExz9FsHSvIEsNFwXj-SI0xK5Gdo2V0jt1I6TTKFFkbCO791r8m89oNAKyyqy3GjJ1stk0_pTkgy7pssfNJOeX16clbRbA0mzznfBIsnRhEO8-GJXlv2qhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJZd9VlvX8hO-ArlDojbvuLozBl-1ivB-M90tm-MHbEsHZmTPI33wp-LrUbTo0l3gMN1oPu5D0bP-GxroMDw0GmXDzBQiAMw_m3Fwk1AHCAHfY6rFQBDmeF0Q_QD6AATOOP73jS1niLXL_e81xwWlZZDAmVHJcO1j5rdrU35rcTiDmJwc6yJhnjEvY9yRrYVet4XpWQQNs2Mj45fKX47zvVYDl_ZX8MHubHjnZIUw-uYarnZibQbl7-DkwWkuJBDsG7a58Mj26rYfmbHS6jcn2ExY3EqLup_NX6gvriB1aux6EraMxlAsvmdgFJqFUWFFHHN7Osz4Oa6r8CK18VPiaKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJZd9VlvX8hO-ArlDojbvuLozBl-1ivB-M90tm-MHbEsHZmTPI33wp-LrUbTo0l3gMN1oPu5D0bP-GxroMDw0GmXDzBQiAMw_m3Fwk1AHCAHfY6rFQBDmeF0Q_QD6AATOOP73jS1niLXL_e81xwWlZZDAmVHJcO1j5rdrU35rcTiDmJwc6yJhnjEvY9yRrYVet4XpWQQNs2Mj45fKX47zvVYDl_ZX8MHubHjnZIUw-uYarnZibQbl7-DkwWkuJBDsG7a58Mj26rYfmbHS6jcn2ExY3EqLup_NX6gvriB1aux6EraMxlAsvmdgFJqFUWFFHHN7Osz4Oa6r8CK18VPiaKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf2HWTZcqbqRpBASpl2vdvRLtiEN71p14IrQ45DRuvgMa8fzR-jHPAWcxSQpTjGmIgXPGxJGtACpWpG7ghdY_66h4JSPiUeqMHJ98_4X1hX4A6roLborBOpaz2-JhgF9HrXuEpT7ffrq_A_voA1A9ZhSQ_5vqRb0FF3wlK8fV6GXlpVRD-mZx8HAVLIVaMcqSllfzNR-eU6VULAQesrK7MWK5RO1JhE-x2427HLLfmapqlAPdLJqPSj3FKzcGbijd-APstOhzuQTunFRnqgMuDq_3BwZhJCyiWvjuEID3v_mXmb3Ru8GsFwv0vHA0u6joeGly8yXocqTWnLGb9YzQ3G0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf2HWTZcqbqRpBASpl2vdvRLtiEN71p14IrQ45DRuvgMa8fzR-jHPAWcxSQpTjGmIgXPGxJGtACpWpG7ghdY_66h4JSPiUeqMHJ98_4X1hX4A6roLborBOpaz2-JhgF9HrXuEpT7ffrq_A_voA1A9ZhSQ_5vqRb0FF3wlK8fV6GXlpVRD-mZx8HAVLIVaMcqSllfzNR-eU6VULAQesrK7MWK5RO1JhE-x2427HLLfmapqlAPdLJqPSj3FKzcGbijd-APstOhzuQTunFRnqgMuDq_3BwZhJCyiWvjuEID3v_mXmb3Ru8GsFwv0vHA0u6joeGly8yXocqTWnLGb9YzQ3G0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=VXCg45W8cAJOcp9oykcu0NTbGlZ8nX7saN739Qijxgcw_m6IyKVsYcDOR048sT4NZMbusN7te419k1YCBXtDtZrQLqK4nydfoGqGjRfR8NE--WVpABfY2lgAVBdz99iI14EenwbCx8mCOAMlnWffttxWjbfzMVfDU7iVkzc6Z-W1MgyR-r0Ed47kFx_sP40SmkO1OGTThgyVHDfaoLPoBRT4gyCM0w6XdtgdwQ9x2MWKJVYo5x5tCSkX41ONn2MsXA9olCgGyUcQ9uUDKmGWnrgrqBUFw2ZTi4t5lRR8CkCJ47ZUz2ALLCXgcGHS5YuYVKkPe9gNSM3gPiT-CmdQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=VXCg45W8cAJOcp9oykcu0NTbGlZ8nX7saN739Qijxgcw_m6IyKVsYcDOR048sT4NZMbusN7te419k1YCBXtDtZrQLqK4nydfoGqGjRfR8NE--WVpABfY2lgAVBdz99iI14EenwbCx8mCOAMlnWffttxWjbfzMVfDU7iVkzc6Z-W1MgyR-r0Ed47kFx_sP40SmkO1OGTThgyVHDfaoLPoBRT4gyCM0w6XdtgdwQ9x2MWKJVYo5x5tCSkX41ONn2MsXA9olCgGyUcQ9uUDKmGWnrgrqBUFw2ZTi4t5lRR8CkCJ47ZUz2ALLCXgcGHS5YuYVKkPe9gNSM3gPiT-CmdQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwDTouh-l_dZtzZpCvyoAzVqpEI4JKuiql-dixagCpPXHCJugjOJnYicoBOOG_z1F2xDd-qAnCcq-6-8ptOyTToTUIaQ2kS7L0FNioy7xJwVTp9ZbjsGjTDCrLfjDTLxsUR-J6gxCzSKcHNtJ7Z7Ri7J-IbJhD5iudv4AUaipDJR6gDCYv1x2wgCF3ijKKNczrIEw3oipmvh0ORTAWHq-jmLONtSgPZb-Z40BV-eSuZ0TMrnnJnfTZFDlRgLn2cdyxan_f3F3urM9T9amhNBDVxegaDqf-zn1Ju8NHETw6cIWc_vWQB8cLg7qRkueM3NFJ6FPj5QMuOR3-QGpBdjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBbjMo-8Jrme4sNcUUZN1gn_rGyIR7cTpq3_b7VY48kGVIAQphHgQVQPsdqKq2yefzRmsTie519jaQds4oi5xa6FOEvdteVdrTQEJU6tIwUnnbq3ZesUrfNE3K-PmjuB9PN58AeZUiTfKUmILLFffQrgS2an1cONOiOEApFDlfzIFIC5aiXmNtNoQTfq--3CuorGKbdKxcwDl03enuB46WzqCaED_U8Pb-OHlVjqkky7H5fXoEwKNNj8gPvqBM1E-YqLHws9o1iBkC2zipeZDOmS4BtX5fOMcpQAM-fTH01QXanm3SA1qMD-AGNPEEC7dyrX5t7vX0Cyk8X_mTAl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=aD-zuLfVCIMAKZhaGfhtUv7GHHhxthSjRRZeICD3sYo6MgSixADzNg_oVGGcLGt3-DAJSpAVdWIzFDtgUXSqPOH7NBuF9sUOJe2coZ6tUB2U-qiEVaEm7OLQ0NCPZZ5DXvxvmHlAaFG58hGCH8wL5wPXdTwwVKT0hIRugIfE2gi9SWn0k4RimIfmvs4aXs8Ek-CdZWoYrMpGJY63sdoBzMCq_1IcAGcnKdTB7HJ5zQ5iQkivKsCaH35hzbIibZ9p5wEITaUp-ms0VD5qcO_QTV6WlgU2Ci5NS5FbDLiNA15K4XqwhJBeS06IZ5JxBmQQ4doFVHKeB19cVYf_nGEjES0FtJEHth1EgtGSDv1rPP4XuuB3IuceXKzam7U5HxHXXgAYIs0lkuXKgJ4LPII4AUe4tG3E1sgJtydPu6qMlngdulv49bELVkKInlCWZfz3yZMz5nI_HioHW5vbuNkrR7kdUqwrbVWgX-h28PY3slILYTjE7rksI3iSTmW2oNSZPPfHeZxhSQCy-uUynrc0cVmYX-sg3MvW6H-MaTO51N4QSMLJzeMsMK_ScxIoZfsw0MMYCkPDIb_oXvGeGiLqkq42p6LO7RNjaSkE0YGzu0Khak-BVyxoTtluZn68P-arRePjZLJYVQ1DCzjtBbhfk79fWHCJJHaPKtyt2DD7cXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=aD-zuLfVCIMAKZhaGfhtUv7GHHhxthSjRRZeICD3sYo6MgSixADzNg_oVGGcLGt3-DAJSpAVdWIzFDtgUXSqPOH7NBuF9sUOJe2coZ6tUB2U-qiEVaEm7OLQ0NCPZZ5DXvxvmHlAaFG58hGCH8wL5wPXdTwwVKT0hIRugIfE2gi9SWn0k4RimIfmvs4aXs8Ek-CdZWoYrMpGJY63sdoBzMCq_1IcAGcnKdTB7HJ5zQ5iQkivKsCaH35hzbIibZ9p5wEITaUp-ms0VD5qcO_QTV6WlgU2Ci5NS5FbDLiNA15K4XqwhJBeS06IZ5JxBmQQ4doFVHKeB19cVYf_nGEjES0FtJEHth1EgtGSDv1rPP4XuuB3IuceXKzam7U5HxHXXgAYIs0lkuXKgJ4LPII4AUe4tG3E1sgJtydPu6qMlngdulv49bELVkKInlCWZfz3yZMz5nI_HioHW5vbuNkrR7kdUqwrbVWgX-h28PY3slILYTjE7rksI3iSTmW2oNSZPPfHeZxhSQCy-uUynrc0cVmYX-sg3MvW6H-MaTO51N4QSMLJzeMsMK_ScxIoZfsw0MMYCkPDIb_oXvGeGiLqkq42p6LO7RNjaSkE0YGzu0Khak-BVyxoTtluZn68P-arRePjZLJYVQ1DCzjtBbhfk79fWHCJJHaPKtyt2DD7cXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=kMk9qUn9q8XV_NhbaaGxdpBimNkV8uVGotWeRd5rWvb0j1t1BKyHIKAphOnnKqHXJ-97xN-QAfyDF6FduE50xk6MOuqx2bHppHH-i8pmMoQkM2fWORfW7UUB9EBb2J1xbKgOtj0psKVyXi2YXJ-5Uakidyp3ms-ol_phX9Msh1lfIIJdeFk-lempsbtadoFCK5vE6OMV5vPEuAXcme3u0d4bDkF0NeulXeHCPHiiA2bm9a0Vhb-BUKOFAGyovzazhjGAR6L1gwUmJPZ_ah0JzcvMxQga4N6KrEGECcIW0bcBTa9AR78WlPUv9SnBg636mqBcE5cRVFUGUwTmAiT3Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=kMk9qUn9q8XV_NhbaaGxdpBimNkV8uVGotWeRd5rWvb0j1t1BKyHIKAphOnnKqHXJ-97xN-QAfyDF6FduE50xk6MOuqx2bHppHH-i8pmMoQkM2fWORfW7UUB9EBb2J1xbKgOtj0psKVyXi2YXJ-5Uakidyp3ms-ol_phX9Msh1lfIIJdeFk-lempsbtadoFCK5vE6OMV5vPEuAXcme3u0d4bDkF0NeulXeHCPHiiA2bm9a0Vhb-BUKOFAGyovzazhjGAR6L1gwUmJPZ_ah0JzcvMxQga4N6KrEGECcIW0bcBTa9AR78WlPUv9SnBg636mqBcE5cRVFUGUwTmAiT3Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuB_bV3ptTW4bLWl0tjvru2FCuN42hpKrrriy5IwRNqTrGj4w6YB0AiJNhfY7EX_wXra_UgvH3WqE0WSFFx-k_HyF6V0PQaLDWPR4b0tTalh5M3tp8mzFqb__wCJ3itKDuVG0TmgH0E-B1wFD8OO2N50OUT66LQgrwAUI_7BofXDVM-daf00GF5LQsnhvH2E8NLXpEiKp1K5jcWuWbIVXMpZyNnO4WGTr-VdSCZvnZEP-DNfOpJQznN020jicz__BDcBupxKXmS8LJ9T1lXTJRau7pPAXjArW2ylXvWjnihDBQ2lZ_pNe4bSlhKLLjnbtwZTJLyEqRGVSPUtWwD4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdKXdecNRzqtfvyj7MUfKSGr4AlyxxhKyOgPExMh4yHxcwvp6qBiI8OEJKWL2xU33kVLCg5AgEXggC6-WRhsJ3AexPet302XCL1GsV1nuFC0WtmVeTrZPkfIoT5DEXYNU45bnsImznJ61AyvZwDNQE3kShPufXWq7jWJBUG0A5BbWVVr2MzSNBEj5jzy0EsmdxEnZalsJ9Y5Sf6wUqloyW81Odq7P3o3ZJ35AzKCaYcpCXtIDgO99VW2onFBNq-J9k-A4MmKf_TV9jTGP_l5MACX6RjpdF-nQwcFfZXpA5F_D7MrqOyMeNRlopKTGmGrfzF5J0s-JC1z_9nNylE8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IoumwuvWg2kCElaKkIFKOQrWpMYn2n-xJWR64ToBV2ZstkRhNvKXUqj38ImTWC0QVK8agTkeWDUqq2S3IfJ6VglnkC8j0C9L3g5u0aSls-2FvOiFnB7LqHtE6ij7u9Wqb550f9BH6GO7zusOuaBDCTHHRfo0-RO00ua0oKzOL7a9X5nbt11hZRx8SFj-osXnkPMpMuq_dTDt2QvQ2eokZpuD7Be7AVeN0FZrxclx6Id-N3GNVkdOyP5Ppb1HlG6EejBgDb7plHDs-SU-iDGUMNG5nF0BgDqMSHnTp9ltOZIz1_kZEWFwyLADIMWozQtANmoTezyWx1LB5CCXBKAXsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=XKeMC4TbgWco0Ahx7veaIYDiFfaalNkwW93W4M9yge3vLPcwVcYFEO1fiw7YJmm-rpNy4TDW-nxaOCeYq3M7qe0ValcQFi3slSAFO-TjDFwTZfQedhCn8VJp6r0PwBIeEoyHMwEG6UHKG3_vWvEDv8fhDktSqlqMU7Reakcop1b3jnnJb5T2BgNgORSE6k_-Q4yS4nL7xJUui1dy5czIAZyJGeK2aaeCrPS7yZf2ASi3EJe4ZPIlfSd5ngN8GQsNE3lWHAUn9kNBVufLZAViiTZerfrx1crJFA7nmZwdqnbIN3MUrpS1QStWLidMZ-E_U82UlBcjpFabo0boUmuZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=XKeMC4TbgWco0Ahx7veaIYDiFfaalNkwW93W4M9yge3vLPcwVcYFEO1fiw7YJmm-rpNy4TDW-nxaOCeYq3M7qe0ValcQFi3slSAFO-TjDFwTZfQedhCn8VJp6r0PwBIeEoyHMwEG6UHKG3_vWvEDv8fhDktSqlqMU7Reakcop1b3jnnJb5T2BgNgORSE6k_-Q4yS4nL7xJUui1dy5czIAZyJGeK2aaeCrPS7yZf2ASi3EJe4ZPIlfSd5ngN8GQsNE3lWHAUn9kNBVufLZAViiTZerfrx1crJFA7nmZwdqnbIN3MUrpS1QStWLidMZ-E_U82UlBcjpFabo0boUmuZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=v8P0fi-hDLIoAiEvLMk3rY_8BbZEQ4Rj7BGxwrU9YeAjhH0E5Om44fjag2vlYy_VhDqZURYaHQ0aVaZk4f4Dv1qRVbeWkhOBwsswMgsC1UZZkZY1Z5HXSpKUBb7FZizkn_o-ba15GA2WY2G09t1J7RVvEU9edJ0106C2frz3CctX-FMAO4jDLCtDbpVPMA3byf5PnGu0cxwM5R8ZBkxRJTF8j2M9oN5DVXER3_riMvWd5EtAvp24gsFaFEWHaQWrrNxUEe_XXlpESwQXD7EGIW1n-pKKMD4jEyYLICZhLuESCu2YentV-uUCI69O1muydiYMVBoN8AXkyaXaB-xbhYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=v8P0fi-hDLIoAiEvLMk3rY_8BbZEQ4Rj7BGxwrU9YeAjhH0E5Om44fjag2vlYy_VhDqZURYaHQ0aVaZk4f4Dv1qRVbeWkhOBwsswMgsC1UZZkZY1Z5HXSpKUBb7FZizkn_o-ba15GA2WY2G09t1J7RVvEU9edJ0106C2frz3CctX-FMAO4jDLCtDbpVPMA3byf5PnGu0cxwM5R8ZBkxRJTF8j2M9oN5DVXER3_riMvWd5EtAvp24gsFaFEWHaQWrrNxUEe_XXlpESwQXD7EGIW1n-pKKMD4jEyYLICZhLuESCu2YentV-uUCI69O1muydiYMVBoN8AXkyaXaB-xbhYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSdMqThppiCXfs-c2A2dhabzySZNQ8h-mKlmEyD9JBcKOjmWwu9IyZmg32BSvBPL-JoBYiCpdDdB9jEiu-KfKgTiB7aUg5d1TAi--KUUrgMl1x64jILSjCBBVA66eH_Xd8Iz8Nv8WEMpDX02AC2Cffyl6fg-NC5s8ouwaL8TC6_01pQ9duRCp9hTms0Z34oEJ4FQjz-QPEwxTvIabW3SfwEn2gjr4E_RGZR-QYkxI3TWplhLcs_wrjs-AbeJi74OK7tFw6MtCNpjKptehbVRiDAATTeU_X_rPCwQTZvOtdfiv6NFpTipTSFGW-CIfLF-pEJSSws2vNfBr1LMpcnlpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-zedQJdUZI8U75HS8lQa-jGDthxvv4aFc0I2jDH5TIrfe999g6AY2eHAG6vTTBbt5mkcThX1Dex2Sderuk0QkJ7sETINExswRTHHTbpR5A3r_0qfk9T434eyxwHZS7wp5OPtDdJ_MeutJ6ivdeLbg-Fn1ebhFwXWNWpUu4GmbEOUFWcIPO7qMd9jhlNOHQmBHPISAM25h_5YzWONuY-Ozu2Ot9RRycYi13KkhpsfBluiaAjXeIPFwNIGxcVwyJcQTvXKbekoZGSh_It1HMcJ54pvrfW-pn8S-BRPBpRIb4u8cr-k2UULJ-wIC2rtaAzzcodEQBPSrRol3U95ttoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=hdmnPwf9PnqpyAdpmnkY2_JnUOSxJ5oVR7aCZAxuTXXt5GPeviVRZjBi9r1lwwgvBEwyDKPbbdnH29iDZHm6N4hNNCIx4QNR1qxxM8ihGsvL1CxJ__aMS3317pNNgyxugRrdBuIQ4ITMNoxBJXLF6b2sn1_D6wKd-gxAntDyaB3cPzmTr4d7jURlgwquTpb47v8pnQCjapHrbc2ph9xAjQNAgq1Zx1Wr3wwaEw9-x0Di-YnKy6b0j_4jLHywfNGUEKKv92FS8PKZmHwoiTVEA2EdkLSX0Cst0xqbwNp3t8LSTGs2akDoCFK2AYEZwvzuzaYv5hXXMzc9d0PZCMcz1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=hdmnPwf9PnqpyAdpmnkY2_JnUOSxJ5oVR7aCZAxuTXXt5GPeviVRZjBi9r1lwwgvBEwyDKPbbdnH29iDZHm6N4hNNCIx4QNR1qxxM8ihGsvL1CxJ__aMS3317pNNgyxugRrdBuIQ4ITMNoxBJXLF6b2sn1_D6wKd-gxAntDyaB3cPzmTr4d7jURlgwquTpb47v8pnQCjapHrbc2ph9xAjQNAgq1Zx1Wr3wwaEw9-x0Di-YnKy6b0j_4jLHywfNGUEKKv92FS8PKZmHwoiTVEA2EdkLSX0Cst0xqbwNp3t8LSTGs2akDoCFK2AYEZwvzuzaYv5hXXMzc9d0PZCMcz1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVpDsIGUUb6wfWoWUS2VSla0G2_RzScagkTmA0zjmqjuCLHu5CzkCca-1xtJaKqg90KfU9yDF7A4Y_3_X3Ri-5i94-Zl3I7CG56qxqnZR0ZJn0AiOVIeZKcMpbVlsFTAzhVLWObedLnXZCCRHNWNt4Zs7a_GRrc3nVcz8QdKHPFrFuJ-h1VAvbAh3OD-wHjVENGAPwuZylH0xF23aiTjP_QqQkNLHcX8NUCGHh8mBT0QvSQrktcwHb7M6WJ2Ne_HFnmGvxDfAUaWj4Zg6xTo_3Ptvl8RlC5M2c9YCoDAdA9_cxapEeWgG7WmUag4ookbarKMXnXcIUtvogQcAR3aEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5SKwFp6AC-2yI3dBwq5CP_6sPuMKZMj0abdgpmtUl8ID6YDAu1Cw_Usx8a1gFZ1cvzUgKa_d-2lWD4yTm6tA-3aFNiwL-PHrmOMDafBJOCxmW28NQWOai-4fqN9n4AXfZN0rHnn_fXHCyiLvUUYYrX-9KSkk_-Yip9zJGRKsIA95Z4LK8EO87Z0Mdl5urhAJwF1D8K2y5f1KGWMMxSljed2QCUVbVUlXFQOeRlB4s3a0pMcvx6fQKDCH7m5whJ-ACbRmcSSrKDTeas4zw32vzz4_KUefWeeE1gWCg6d3su3j3D7DBJCY8lUfuqgwPcuTJsbXG4XEimbMRnp8hxSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo2WRv6tjQlLO0588ufryZINVACH4T4m_xteCFWo0dsJlKeI_yaM9teeQpinISk7yf5M7lbtY1iq1JGwGtwA3X0Zf1FiRbtItl92h56Cn3rVpmiu--Bumyl662AKMkLoToL7ujyM3C-C4zwFY6eFMHWT-8srdZq21WKZ_ohZYAHGOqGpyb6I4rs9FxpDQ1K42NuYddxozDVrT262R3PxchtwrGWQl3aOSTDVZXEWRymE1nHGpm3WWtcYYf2qrZ309327zTPeDb_M60S0tekZRqQ72xHIqf-hk9zX7EZ4wM0zQKhooi2vcYTOrAhc97IzfM0ItukSSS9NcE7kWFoqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I7KVb4Q8RYT-dZuq3-OO40lvXEkgA6blTF5BentdWmqy4OdHgJUi5dOMfrrIfbJQpz0xLY77jTd7SuTvtm8kKMnh_dxGFDI4uSfHsFDKGvYUuxiARz1iALDfqHPfmStxPdsFoeo7kqT7Qwv0vS2LOaC3oJZ8CJ8ra-ZSM1dU760PVxwox-U05CAtqVn-WJhTbqGe_u_290esL3KGYtGZW5XXv_JNYd7-3axS0Urs0EBeH6C_VxtpuQsQFHpoKMtH4NaWJHp5JUMbhTWCeN-W5fSUzSEKocQrAG3l4YTRE8FrfEfQwpjuHLXkAPKU6lAyxNjsYGK0TRnm6Qju5f4aL04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I7KVb4Q8RYT-dZuq3-OO40lvXEkgA6blTF5BentdWmqy4OdHgJUi5dOMfrrIfbJQpz0xLY77jTd7SuTvtm8kKMnh_dxGFDI4uSfHsFDKGvYUuxiARz1iALDfqHPfmStxPdsFoeo7kqT7Qwv0vS2LOaC3oJZ8CJ8ra-ZSM1dU760PVxwox-U05CAtqVn-WJhTbqGe_u_290esL3KGYtGZW5XXv_JNYd7-3axS0Urs0EBeH6C_VxtpuQsQFHpoKMtH4NaWJHp5JUMbhTWCeN-W5fSUzSEKocQrAG3l4YTRE8FrfEfQwpjuHLXkAPKU6lAyxNjsYGK0TRnm6Qju5f4aL04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMycTHMrdfk67IHt-gDkV2f9NgOzu5JYgWWLTtgljhDRPJo-ljFCmxntVYrUh93FI7w1zq90Oi5V0CVhFIwh4MBrGFfk1pXIIEoEisg_RozHpJ-moBDGHxx22pcxP9L6VF5fqIqzYEwhxL_IuAOKkviRVikV7TjXIL65B8a1cjibq9Q1V-IUp3VUKa0705cKMnSmC5U7fjvm_UETX2xo7FYSuFGG4RlfNpZSB8V2DrKJTIYhVBDu1D_n6DRumWmpjRVQMkFZgnZHkCg3cEnPQbqcKp1AA-XXubVvE3R-AZLp8_nvDzctW-q-kqTcq30Za1RiY6ZwjAWVOVt57yzevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHNtXRZizdkqFm6ngi_EBwwCQInXnLDVARisKCKjmwHz7kNtCYzSCsUyCL8MOCG4kFQT5RmUayXKtjwylakb0vCLqHpxhsdUnFuQku1MLFk32Kphgak6MTpBuCHtx1LmUXGXpLbVGeWYvXIMcq0e_ZS6h_lyGOJUifn9WV1XwnZ21NUxt2RcCGDdiCne6Hux7OLtvf6JeaYonfe7_a8KGvnTrl082zXby4hdviXjOSWFj521qvYrUImgKoLyUDZToPjI0PreXHi4uN4V8TzlfJToUN20a99eVIUOxvbVxzmWYSvJiCIRs_MtM35LebusVK9BAu5t9sbPnVLtI-2YOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Rm9Mdf1dxxxbgC04hX-OO_9n8Nz6MMQ5PCtFY9K1oI9AvaXmVwGBoEJrsjEepoxK9xP42PDnXvBOs3eS6cYMtMmaEoTLJ9sA9leC3I3h6wD-P0mtUALcPHokT3L4WpOX5-WhERyL6kVwcTrOBWCwsTpyrWgN0z5MJnm8VAv-VTyT757RjXH5oS89yuIfv6Sh53WvzdOMILMpj8Kw1zSGn_xrgQVnaTOteVfLCKEIP_bVC8hujAyKcSuV-vQcOjXRuMeAaYMU8kBeyTMs1xpWWPwu0LZ43iasl63nUZUyER1JnYiXE1BLN4xBZ8dDpnG0yGwYXVTiT88D0pIR0RXgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Rm9Mdf1dxxxbgC04hX-OO_9n8Nz6MMQ5PCtFY9K1oI9AvaXmVwGBoEJrsjEepoxK9xP42PDnXvBOs3eS6cYMtMmaEoTLJ9sA9leC3I3h6wD-P0mtUALcPHokT3L4WpOX5-WhERyL6kVwcTrOBWCwsTpyrWgN0z5MJnm8VAv-VTyT757RjXH5oS89yuIfv6Sh53WvzdOMILMpj8Kw1zSGn_xrgQVnaTOteVfLCKEIP_bVC8hujAyKcSuV-vQcOjXRuMeAaYMU8kBeyTMs1xpWWPwu0LZ43iasl63nUZUyER1JnYiXE1BLN4xBZ8dDpnG0yGwYXVTiT88D0pIR0RXgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=LpTsTWyypOqXUQbxyS89hjaen4QWqZMpBR2JDvc9_tq8gG2P1eeW2vGYUbwz9dwbgfDlgQ88Mi4IRXbHjG9qgqwpr7MWw-jYGAnGbxNXRdYgq91UHgaF7KGZiunqekfPhhrxu2q8UC-c6eVPOan1SBugaU6YwxcgKX4oKtuUJ03Gr4eV-Nr9stxcTJycpPFSpLNpysUNHHFJ4CYa9s1Tni32Tp7GXWZi2Cb8JLR4mD4wlNfY50HsyZCctET7gLgLeSsYyOaRagtV49FOSLD3aXdEtJy5eWqqZaZhYEthVrPxTnFw6FiLRen02Ny2quLKcc372sG3Wk9RdACsBhzwfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=LpTsTWyypOqXUQbxyS89hjaen4QWqZMpBR2JDvc9_tq8gG2P1eeW2vGYUbwz9dwbgfDlgQ88Mi4IRXbHjG9qgqwpr7MWw-jYGAnGbxNXRdYgq91UHgaF7KGZiunqekfPhhrxu2q8UC-c6eVPOan1SBugaU6YwxcgKX4oKtuUJ03Gr4eV-Nr9stxcTJycpPFSpLNpysUNHHFJ4CYa9s1Tni32Tp7GXWZi2Cb8JLR4mD4wlNfY50HsyZCctET7gLgLeSsYyOaRagtV49FOSLD3aXdEtJy5eWqqZaZhYEthVrPxTnFw6FiLRen02Ny2quLKcc372sG3Wk9RdACsBhzwfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpVEviAgfjV5Jtwk9p3cbU1L6Beqx7pGNcPsco0xOqpkwfTFMkqOOagw6Z3eyuome_vOhK7cuQ0NM2fMrPhUT3fp_LrjnteKl_g4MJd6xQ1-JBj7dUfrcfzM_6e3xuV9mu3Z7Vyu2vfe3FnsmWfIs8OvUtSw8ki-xFdahHo8atFg8tyKKlF2s2vY0iXt1fp8PEqkVUiH_83DOX4NgsDXxzCPdXq5F6EzltyRUVriabWqa555r5w_C8A99sDwFeJPBYY2IsksWR4jaxiA2iqNxkTtXk1lXYbrPojKXgf_ik_-bKHr5eZ9Lms3nXASCHgZNBxZwW9U_rGKmqo-4PGF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU-mC6T6tgFckphwPyL89ojsnxLf7_R5Xgklf0vJHYkQpE9vD71Fhb5IMYgIfECS2yN7IpsFZp17qPEdC0LrptWWxgvX-SK2sv8GN2ZWotM7jlZETl3VBDOTJs3TMxltDaCbvnCkE_Pfu6YLtMCISjBQF9B5-dGGCHi9355---F3LllDeC1h5A0SYhF-x_YZ5yMvf7gTpl_zCVMP5wO3OY7sQTILezCkQ8dQjY1KTMZgry6vFUcqu8TpwwsmuyE1Ti3rDB0E-6vTOkUjRtE-8VvIH8bHmyCMXHrrdNZUbrKbhkPTY9vUrOOOBzVQ2JNkrr0aHSlVfxAppS3mP9Ip7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Ya6NwxoxZaea1hPkLcabeX3i2NTSFxwPDfj_uZP9ZkFNpDVN_8g2VbFpxA2kCEiiDspCiZWDnYviJJkEv_vspToBaUorF_1sANtKN9O64SX03TOpkue0SMXjeLDqhk0L6RhqFS2W5aSwQT5LXfvg1y6E0MStdjzM_yaETvyFS5or-ikJsUf--xXjIyznXMvF_VYjCbG1DZATdoO7Z6U7ZOOoL18aPwAJH3buvW7hS4BemTKIy51AEPKC0dyvkVQWppOnjAOKTANGfOE1Gt2PkZywbhWBJMRtvtOhiu3xJ8hCvCbyeA-y6Cws79pSeDBfvfd8qV8lXb1zvBcxGN3C_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Ya6NwxoxZaea1hPkLcabeX3i2NTSFxwPDfj_uZP9ZkFNpDVN_8g2VbFpxA2kCEiiDspCiZWDnYviJJkEv_vspToBaUorF_1sANtKN9O64SX03TOpkue0SMXjeLDqhk0L6RhqFS2W5aSwQT5LXfvg1y6E0MStdjzM_yaETvyFS5or-ikJsUf--xXjIyznXMvF_VYjCbG1DZATdoO7Z6U7ZOOoL18aPwAJH3buvW7hS4BemTKIy51AEPKC0dyvkVQWppOnjAOKTANGfOE1Gt2PkZywbhWBJMRtvtOhiu3xJ8hCvCbyeA-y6Cws79pSeDBfvfd8qV8lXb1zvBcxGN3C_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=s_AX4A5g1wDHamDYCgiiQYLsvcu68UhUc-7gJKBIk0qjM_gbUmOrIYnBvF7Udf4FHBfkyYDQIj3sUvYHt3m8FAi2LknXWwDANXXf3TPtbO_-MJpP4TB4mos1QHWMlgszyAzaxFk3u5qhAfTCIbmVHtDFbGFnXVAfWv6P_rl9KG94VeMEknkO9rGky8cDA5962rFeFyo9W209-XqxOyii2pNcObxAN-StrA3QU9f7RVqahTl4zwbJ0m-FmHZxYGsAc960zABnbthxD6SSnnZyN1JOAaIj4rd0elvDXGgcHXFRKfoC-60T8dVosnjEHi716yQ0jz3xsX87EeEJ4Jv03A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=s_AX4A5g1wDHamDYCgiiQYLsvcu68UhUc-7gJKBIk0qjM_gbUmOrIYnBvF7Udf4FHBfkyYDQIj3sUvYHt3m8FAi2LknXWwDANXXf3TPtbO_-MJpP4TB4mos1QHWMlgszyAzaxFk3u5qhAfTCIbmVHtDFbGFnXVAfWv6P_rl9KG94VeMEknkO9rGky8cDA5962rFeFyo9W209-XqxOyii2pNcObxAN-StrA3QU9f7RVqahTl4zwbJ0m-FmHZxYGsAc960zABnbthxD6SSnnZyN1JOAaIj4rd0elvDXGgcHXFRKfoC-60T8dVosnjEHi716yQ0jz3xsX87EeEJ4Jv03A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoIivE5hPXszGCUShUyIAA6llwBCrRjEXcdG6ch9DnawobDWlMpMDPKQF-cNeFC0F6nX9KMgLKZ9l4ek8SzetDDclP9lmH1EDcUbFEs93-7VeS6d_GakHAQWtgZcJKTk8n0LjTC7KJ5LSgmI6zovziBjvrxgyCMgvszwNohM4dFkfYmlFNi3XatgpcQ8XFFLDwDEbPALPHk_YloQtmPzRuWS1h9uYyepvXhPczUOp3DaMLNhPRrgom5dz8DJBr4q7SdDwvsUJnGBSbULV04263td3dGxsVISIiVcaSM9CYdyziBZzQxr9JXRmhJIgDySEeAKj05b9y83K-OyJkDpYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by9WX-p06JUIvKqIqr_fCxkNtCKbrgt1fJhgunU8Ekmih2GH3tnnsUpnQIR0uIdrVv7mWyIHt7H1GWyIbiG5SqXt94f7ZhvQ2DQGtqIKWVRTSKgjvq7qzobYlLxZ9nhcrf2qzEos8kAGEkrcLgzWSFPC_DOQkiImOAVNy_bEELqzNn05FKH3N_N8wEYmwIipCxIOcIqJ9yAiTMFwUGshZ3BGgMi8D2wOgQ7a-3F6QOk1Ln6gB_6jBFGH-ubf3Vde_8DHJt_gwsHJj1pmzjHxGgODWX8KXFDFoutm82NAiu2VWOQVWpooN4INKIxC-reFPpW5-n5gGEDpyQkKwcBoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouObjOR6vCetU-18ed883gO1mY8IWCRhOxj6PetBFg2JK_LPN7eaJ8g5H-tifTTmzoECpRqsZLQRkcFrBUx9xKCujy719aN1Xpn3IuHyLtDXn9u986bsMvFyY5m0l7Hiib63puLqKDo1u5js_Ln0_urOV74dFIyXg0MRD9pdMzkaxHoxR9BE-33CSahbTpd5r9RCjceQb1X18xLy9uWlTUjwn_h_cpdYjAS18fxG51795cjN17GD4cYamg_n8OGAnKa6MYo76Cu5l-Pewhs9CMLpLmI1s_D2t_ZvOMLYFs1Hs0n6DJMRvz6CAuPJoD-U6vhHEElZDZpUfP1nTFWZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiDezGgRz2TqI6TLtA5mIKgLNhCbyUVWKHMicwox643YACvOcHE48n_GNTcpYk2Xphr0G4PjkfbwBpesEAYLmtXDqcBk_3p8lRvS-ASFRiwcxFp3JHdwBRZ2KBoEcey6YqisnqjH_PlUVIjafpurM0Lj3czIhP9slOqV7jBOKUARXww3KWALE2zG86drA57B8CoQYqPUMcLp1mzsAJUlzkQcKI6e9DLJrGhkVU29yNRLXfXl_UVSl6BQa7z47OOs324M95rV-FhCDfLkTXzzOjROmpPvZqQ_eXcCcDCYi7qBaumwCFMW0GpMLP6ctuh88TneXvPUhqXi9riKRyiXfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8GTYT9ezRDr46Zo10iAe9ycspEhJLqVi_sVFYDUr8CMYzdjWcP4QL0i-zX8nIg49nRW1YKuNCg5YcFOWUjqr7hAhNOraIrPOd8j1ujHcj2-dBTYhG3cP8QO-jQ6EU39GuCbRfwVigqTe-_83qKfxups2sDaFvlyDdm9xTOaH13p_-SqXlOqzVaIZHilOY4p6_tHM54qU3jlV2UtMTAK0J08fjL-22OPVgVMaTataOBdXetWr_rd6ifn7wolQlELy1hf34pOkAULQw3QQ3WaEtWDFUG0CmwkoC0CIk5DEVu0AEyLYxwSWVzNlaqYMh1hbd5f8bVuRG9I3oVIAtPW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luhfiw8PuO9C02AcozRrjzUiUsSOh-c0lN7uWXXFYPoCMvNriMaozMgrWRd1wrNniN28Ub_mMv6l9eX5kdLcXfMJVYEXESZGQZ0lQUP5Vtk-CGNgQyI8Yha-tTZobzz3Dih5ZmxsjvTv_KSz9YCpAG93FZm6E0RAUWg4FEhOnV1fWQFarJ7eXwfxV2iODupLmlSVT9TU9c5OXht4xlIRfm1dHkIG0jG7QZyzXNrWD-3ToXLeR1-rJWvd5acMoJoR21g4MQjArKopVHJaWOT25xzoO0E8mq44FiF7X0hxwpMt_Oh7k7LDIc3SdLw4-1npwBhR8drtLyp89DQeYCzRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnOzVAtjsVzNrtxN8DTYAkTlxq85-0CpyIKQyvPcetCDyIxJe4TiiaqKRdHwda1Heccvlw1vg6c8fcujx4B76JHskIbGYUKtg8rACrQgoOUX1wFovXbQUSUaEH_YJ1uqykV2VZvvJxxF9Rtq1mycjSXmoDtqkAYY-b-R2UY8jzvxpqpeStmb8S890okGil9EK_w07G9p01P-XsjUvd6bkbtm2AIeMigHkj6ZHdDashiZwjSkbPbJomza0JtilOi74T5yhVEIIlZsbIiNWu6EqyONFrWCSSYARE3ECI5O1OrwVfZlCBKliU8a9xlBLC23l_aEQ7s2Ku-gImIWmfRd6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcW8d9AgpfXRR_t3mupNkZb82c0EG-dqFmjBGZfdYAZJCCrvk7puB5vfhp354XAd63rXT-h5hCcn2YPsliPW-WwUq5gUbvXrflNvI9Oq2ERa9LzA1AxgnKwegIoGmSIZNmNQO1ReltqS_X_OxCzzqf0_eEx_ouTiuLp1CyP9ukU0iFUyfet-M3344s7MCuTcSZxN5VEWwVYnz540cS8xPOTZGYMHDS2O12eHcVQnEn_r6OgzuAYIhGuzELXVRC-mKnNcjL_Eb9Am6O1_QTVxbg9uL-leQRf1cbo5b-qrLJasU3S5X-hHLO8gvDd09cuyL4fNrdZGbuBQ1R0YdrjaYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUpupz6i1zBxJi9Fr9dCtAl1FvPFzP4qmd5Q-gATKgCTl59z4TnLiF6rUG_tgZ-8DPBt6n3fAjB-HYqDrq1m0mnSnfb-n26GRsqdzBn7Gw4sOAhDj64Y5ZGh5zHNwCR9KmPvn4wFrfmUe5HbPQlYAhSBDw5kHSzYhiJc3q4lpB_UjPJ-9tlliqcsxH5khuH0iQ2KQLweZUKC3jYoQ1riPU779E-3QCaD7DabEhE67moVWYfjVqYHhyxCNUsi3cpfKtv10RHqD49YKZbvAzse3N6GZwA3uTWVKMFZZU2KOa3Ki6SM3mT5qSh8VyqpPbSf3u0lfNqehTsMGfSCT-BXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
