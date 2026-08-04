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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 21:39:20</div>
<hr>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=gBkgMzN09B9NddrsWUchv2DCOfnd-eceDTqM4N0sAomLp9sE7Qz6MUymHrFMM5dp7l9LlsdKYzVUfrtB_luSqmdIImrB05SjawA61rirNG53iUytPQjocp3mgWqjkpl-lXLayMhL90CywBAzWN74esxfFI-fFkCRzorp_DP8ruYSjFPVXdIhS-Szv3mYAgI3OljinlvwbXcliif6EeYF0IWB0mPhvIZjGTlDaLYmheQCsVLJygiJ3RuAVKenZPC6TDNOjzsUAuWdsgWNHyxA5uufjgg0lfUt_Ey8ng3ksMV40wuPhpaY1Bv0HyVfHP8_5ZylbwA84BQeBY_K28uV7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=gBkgMzN09B9NddrsWUchv2DCOfnd-eceDTqM4N0sAomLp9sE7Qz6MUymHrFMM5dp7l9LlsdKYzVUfrtB_luSqmdIImrB05SjawA61rirNG53iUytPQjocp3mgWqjkpl-lXLayMhL90CywBAzWN74esxfFI-fFkCRzorp_DP8ruYSjFPVXdIhS-Szv3mYAgI3OljinlvwbXcliif6EeYF0IWB0mPhvIZjGTlDaLYmheQCsVLJygiJ3RuAVKenZPC6TDNOjzsUAuWdsgWNHyxA5uufjgg0lfUt_Ey8ng3ksMV40wuPhpaY1Bv0HyVfHP8_5ZylbwA84BQeBY_K28uV7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ_sdZL2628-noW0FD2mYU48mgldBc2IS37VcvyEac1ZcqmTLzL7-7vDbc71QfTWq2LFnva_relaLABuYiHkU6WR7fpl8rOqw0x4ff9KT2H79K56KQ4VWGBvTUsw8GzVUf1KelDFSyfN8ZN3hHla6IJVLHfddl6CvScYf5gOMHx7s_wk6Rwvk-Nc1Sjj1826qSD4rr7A-nJL9jwP0e740HPFaoZO0jfmXHL7DTY7RTiYmjPdAjy3WkR0JrefxM6MJOLZlIL6zgWtw7bX7vUytOtu8eLokyDJyCXxbFR8wfcwOWpn-WuocBBrh7q81KkElOpVOaaj94jXYwrN2PZkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0Zbkwfj_VVRNft6m2I5vtNvWV_JfD1Rp77agvSiugy4LvHYH3fat9MP4bptUCdTYZqchjvslc4vMcXUwNjbiOxfcsT63JVZAkvC5Vrk1zR4c5EW47qEL9EXOx-5Sh3m65xCUqKmgRK6co8huTimliggOo5r9FyNV9midpHdn_dHc0HXSiWy5OTwMNwFX6kBL1G71_l6QlWjil_oMRCnaLhMx7Ba0PviCcuEEIf9uB5BsLF3Do_mlFlFAApHHkaJppQ5RrZ3YSi_LCL8n72I15uM8QpXtOBA0BrGBfTzalXSWrLHPBTJ-DxAt4qw_CvEUXM_hmhVpZ9oaFIbIWV0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_j_GRhHWokd2FQULc5nH1CzR2-LNk3NtfjVXNQZZvGLK6RRZ1Mvjfe55GB0sazqmwlL_qI8GRGiqg0GtJhuh-Z7Lc9jhorwe_15xJeo5Gg9hRzRaf-MsyCqcWt8q7DEX5BvHQFUyVNWXHdEM8hVwziJGZ8KGa2BKhFuukaYqbNH3SKMsci0WzS40fq2LlzaVc7PYQ5TK4OOppq0ly84GYqm3aGfW8gjl6zP8qYIa8PU2-pdj8oZ1RsYplw2-8-vM_1NRRVd94gvo9u_6M-4GoFjiRDwAdBLcxYQ7ZjNdzcEDSDGQF3fCS3ERhqv8WQvwgU9srXOYRe5vRS5PYKMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=GBXZ0RlZcZGQ3odp8MYklRjAYMYnleEUphkbswMpE9rPe5j4a1pZXpLtHtVjWAOZJjaMLY1Z2YGyUctG6mPscprYUxlVXYAUIqBZWRPpOFa5uc1G9gJZSOQk2PR1fVuNchfkvIsKR70wBqAvN1BOCyXRQ0NHf9pxamNQL6FiSduoIieAW9Rg-AVgBBSEKTFRhhFd7M09YpxxiB27uUvjBwJtqND7e94bKLHuMpdMTkMaaxOHqdlIvSN22HkXphHwegySRxIP42vLeuVhcUzdvPOVOoRcA5jhriXGP7v9dKO_yly44BH2U0bVo6J9eQ5QCvFTVIC3TqU9_O_siBKlOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=GBXZ0RlZcZGQ3odp8MYklRjAYMYnleEUphkbswMpE9rPe5j4a1pZXpLtHtVjWAOZJjaMLY1Z2YGyUctG6mPscprYUxlVXYAUIqBZWRPpOFa5uc1G9gJZSOQk2PR1fVuNchfkvIsKR70wBqAvN1BOCyXRQ0NHf9pxamNQL6FiSduoIieAW9Rg-AVgBBSEKTFRhhFd7M09YpxxiB27uUvjBwJtqND7e94bKLHuMpdMTkMaaxOHqdlIvSN22HkXphHwegySRxIP42vLeuVhcUzdvPOVOoRcA5jhriXGP7v9dKO_yly44BH2U0bVo6J9eQ5QCvFTVIC3TqU9_O_siBKlOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuTDziwN04fXK41NIBTUchPlO5gYpc2KrMTUDwD9SuObJlTcCAbiwPqHY5j5Tc37CCw4MqgfEyaPgKJ-y-bvXAG40KcadQQle6KDry1fBbtFftUj0oIPt2DCq001MsVJbbEvIY1UthJqjCuEttvmRS9uV6JlrDg-fH7PKHyz2QmqqCwuaBiNkA25ZrPgiES-DX_9wRpsHEV_m9hTCPq197GzzvLNiQ_OQxsZblzmFR7Uh6r1mjr-z7O6uY3-bLWauq8__Rkq4FnPJ5GBnbeMqrC19kX6Cb4HyRdDYLjM-Suf2zdNHGjn02XI0ZfyEHZtWGKtsD2sTWrIvE6OJq5bcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZyW9lFixriPk_TDV4HZ-GTmp3aMbzg1qi9xGYU2jaoGimsm52HU3QE_YnX6MS3kejmUMHgaBvkpy8i5-WBKuX9Q_0d5lWqMfusKPpbyPEY1r8NKvTRSL2p5EqNkEApMWC5H4Bq15q_86DzaxVar6QCIgvsOAKqM8uJxU4qRsqyGKEaB6wmybW6G27xKxMVikjNmA0riIrt1ONOgTgfyyqhWGCTmDtDOEOeXgkbC7ZWVLthWLdpJuo5I6DfwBuaAa85BPxkVZ56-wpabC_uQZGG6cCbsSv177ZP0M07Hdxpjj4gK6Da7sijDNS5GT_ibH1lpP-YvVMWfP0uLvtMzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uujkmZLC9Vav3wWS2sWxjNfy4_11pkVpimr5ipSSiKmQZFzT53xbunBiq4W1XcJzawaHAhceYML1EmZIrGZz1ZS_je9L1KKdOHoSCc4RkArWJhgSMQEjcAcbhi6U0t2z2ttFOPBMapATbpgpntXiNbarx_lbi8rj2sASAWi-IKXOp7gliknxj4vpYwuTeJRzTD56XSTt1-7vxiD1MU4QsPZJVfHhIr7L34HlZRSOHCRoytvKRIun0ZlINSDMw1ipERKk9hFKj0pHZHVucvI9D7TFJ-FxDasMI1m8Un6nz3EzDBxkZLFGe4J99Mg4m5z3XX-f6g33x3Q5Bm_Egu_72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBC_H0cbeAqW8pCHjMsPmKInwwQNb_u_6Z8JfFrm6oGYB3_-1srrTEtRpsbXwTf4_-vVrBg9p2d2-5Y6RoiB24-QJV-1lsXzc2bfa-hwfgBBReoy-_-_UIJHOQQg55Ux3T5XVBbmV-W-RBLQZzIyD7ze0Le95K5rjamnkGUQPglS03rXJ5peSq-J4SSVjJwt8rTVBfElCIZB9XcfdLMYbQK6RC6iBdrTrEcGxNkCS0K2DMweLt0mPn_BIJNWpPwXbuzn-Shg4014Z4cMUerjVDHrlZnOAxvWtP7z4oq3ynfYGOSwT7Wz-XAi097XhxIhN4ORMY1yXITl2dsdOAuXrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9xkz_Dl2AfXUhnBlHFK0GgGn5-5x7iqZld1Y5UYKRhQBO4ldxapU1CvTw1EhvYpibJFoYaBml0x7w_W1mXJrprEokl3ATDuV3QnYd_ZNX3dJ8CURCmizzaMH2ssUjFRY2qRTB6w7-FWb_nASBzJbGAO9lAXD64Qi7xec0WMkp8vi1QBgJDbvP051LQ8xCeWxKFDbv4syG3R-yz1OEgrq1wZ6whyHvZZ5fTJqNx2gJpMzyqyNuIaOwpjtULsqkUNkU2oi5wLG0uDAwJN0vTCk-Tnw20OkXgJiPGAxgy86KlZR9RQrGoAELDA2yTt-53ZghwGYe5x6pJnnqLkStyYzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srpUwUGEiqptFoKzQNOtT7GSBq0M8qsaPI08FNiLHCEDfHOT3udeF7LzEvE8caogyUZW_PNy7s3ZZg-ZaqKcqmDl6pWVL_Hu3UCdBugdeh4TVQ-CpVyUed-6KtmxNRX_xbLOUaFW2-Mgn7MKX6EXk1C8q-mkB8c7ukVPCwHqheE7rPBJcI08Ov5N1yk-_OFLvXozITHMnNGEJxVjHWbhV5xBVi2ML5U1JDWZKQL_INd-Z2YPVTNs6B9Dn_TsBkyp0rRwju0y-CNuecuH1Z0ZFYE0NR_6_k11ZIh_1PJtyk8zDc0cfXopUwXBdrnfvBHtuMpNsSE-7oDUl-61Veapfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWbhz3gLBdBSk1szOe344XtEiVN_JWcdljpPevjaGtZKyiDsy2uCPuG1URsnsnMFZ-hj2iacFKFs-AwmmwOy0f2PRanjzSe3B1CfW73qrIuqDPkIl4lxUJqfwePDk0mbl8nf8BEvlN7G2VI-JjX-39M6GwtSS6yD_4N9AUprKIFrISgVx-8j7YxIAdFk7eJ8s7pfFtcbEgdHCM4Zi47YzUlkbpW4wjBVYooOztbcTJxIxXRyxLBnrCkehrrvS_lg_gJn7jzExo4hw6zSVS-btsceKSck80d4ygS_3ETVrmbh-Im_mp558Le4AznpkT-sT5WVhKXPz3dl5Z8P0BaBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR4YNPhiMQRdnSAzNF9Amaai9YvEyIPDLZsDICf7vzpFkX2X57jtipUnB4a9fiqHPjjPPkBIpIMUGygn-OLCOUqyrSsQNrbj1warzucQHSzoFotZeNPJdn-eDyJvWyjRsM_QHVfsRxpLAg_iBY64HkXrsKYYekAS0p-uyAeCpjg4dUKtBdq_M052ShLAPDuGo-YXDxOYsCbQmMGNFc3kctpknmjQyKSMiR67pNNVdfIWupaMVw-RK8YGjaRd1cpZ_N0t1rAogztQ0o43FVZ34leBPcEr6Qbkr973oS8EYPmQf2E_TPSUPNE5eEqJSMkS-4oufTG8Rt6OnMozF3x1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8AXj-0xAkd-9u2KNd737fOOXz1MTm2fXsqb4teQiExAe1dLOns-3pKF3UaDSBcQ6sawEzUAGLmFY_7hl8HLgpKXTwQPaFAKU74bLxwqbzhb0gSUH29mGEtpeyluRTknm-ki78w129dEFG1Jt-Giu_SkxqgFe0QHzZ40U6ZBcy4WxOIO7abdB3Jer-GHWmKCtfuoVc4pjV5_9--IeYH1201JYRQzjFP6tNJKihqFwBfiGDDb7XNDbuk0o-_mC2LbviJ6jPGEREccViYsoAAykIi9gGlEEgbgz8Ky-LUNm6PQdLzpZWxKVwp0p2V-BM2NcyfwrhQT84iYZ16Az3P3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkK-yTcTPW6z3ds7mbrAchTTWDNltGYgoLU4MMvjMVMmrr9hyfSsR_K_h1wbDCUZJlL1AT2crIDNX-tzF6ZYKdMaUN8oFgNtDhEfCMpzkviHQYN2cmz80AbILULFiv_kQFy-hwenZadl6RvzVgAOUUilM3ZqojgWpUYtdnZz_UWUAjSnDyrphizq0OBfApe8IQSHLw1Fn6p_vVLU4WV4UpqXOdW_yZ7IWuZQOy90idvgAS92-QOy1gfGeqnm5g_smDYWJhYY6EV_SNY0uSz-WJTiSv4VJnLEdDOMDFpou99fzIXRzWahOLGkIpa3J9peaPVWYYkvsU01WwDK92kHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbtXFqpSVaqISj_Pxtz0Vnl7GkoGsuLEIs77NJOBrlVGDFk_NT9bfrMgjtdDRMnVCbUdpgJaXndy7g2j4Yrhs1PJWB3DYSVL3hIC2UVXqXRYJ82wFT9jxF0VFixIa7U_fj-YxkMVscMeRoHq-fkCTcclA0pmBVwp8ge3tJ1NALSfppUXDUlmL_KepY4zMpa7p3JyHa3CQXjesLfc6MCI_LHKjOeM8AXF4-WC-vUo08fk2XOL1GtrH1RhJ-nnDL49lPtJAaSDj6tIymP9ewFVgSWrIzcicZPmv8bOezSBmTsmWODm4b4Vryem-RBvrzv9YZsy4zNqy_6EfGMDhqFYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRkf33eVwwVVGvliWi4VT1JJOs6ZNduHxAwry4hEH63Buzk3engW2fYvNRZvYI1BcgyOgy8nc680cOXrJ1d-hyU9C-myUgIsMqIDq2Sk8aq-RmrWsTuzAdFfYTq9q-gldPthcbEes9OQpn6TkGkSNNcxYHdZYQtx4q8lzF5yscuTXXTX2Jk9VS9yJ1JX8MUMBtY2ogWHxoofRMuCv-z8knTLsg3Pczc1eJdagTqb2EUtxeuoz1S3rGACaoEfyKoVIJRv_EYg2qbfPMoDiYD8Rwbd4Eb4XQLvIh7n-IczZz9J2nqxu_ht1tLK0NhMgaJQsojvvWswcJ-gPSC8ueo_FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgX4ZAkkxUFMo0nFDddwPErXXFmJQwZX8L-OgTz4CG-7uwHzHaQYeus6Fk-NR9FwUSYOX1kd08JyXuCiD1-o-uDF6G55zsj5Y4bP6CEbChtXIr0LK_iIdew8Z_4UC-YYveNyZ-rPyTeuZzvLzxOv3KIHVa799UVeMbszXRi2WFqiDZbKRGKM00m7Ek-V3xss3bOAopQ_MX9t_KxUJ24p1oe5ag_jBuQawZmX6uiVMnn30wz54vqpvzfWPMFXPkQXLqhJacVzTxfRFfbBPal3cZey4qXGBfw_pJPBnRomnOennYBM3_6A_m3Wnd7wNytDYylRV8T8cHk6kTfyse0zkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=laOKSZVlGM4yzOfZSm4oJsXLw_28sY9B2JAGQCorRWaYozlMsiShgeuuktVbrOahTkGY4kkru1_U6u7gK3Ca3RCYLFK1q5Ki1hmn1B4g6RGmljzeEDLaLpe_iR7IbMX10bE0ZYNEgv3V52B_Pm2aELO70NFc6_6IQrd0PnNZ5--5ff9mn7bLl0WC2Tg0NRNz00wxZFcMCImlV7B5_w6rsyrZm5vobeQFOb7eWesppjhAmq06-OhsCfkV5hzOjft5NO2Pi3CktXEkO3Md0gjI3Q6KSoJD9Fo_GZ2P2xAhlrjEmtiK1uv6JhM91-VKdxTbttVQsbyUdwz8v-JPBz4Tqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=laOKSZVlGM4yzOfZSm4oJsXLw_28sY9B2JAGQCorRWaYozlMsiShgeuuktVbrOahTkGY4kkru1_U6u7gK3Ca3RCYLFK1q5Ki1hmn1B4g6RGmljzeEDLaLpe_iR7IbMX10bE0ZYNEgv3V52B_Pm2aELO70NFc6_6IQrd0PnNZ5--5ff9mn7bLl0WC2Tg0NRNz00wxZFcMCImlV7B5_w6rsyrZm5vobeQFOb7eWesppjhAmq06-OhsCfkV5hzOjft5NO2Pi3CktXEkO3Md0gjI3Q6KSoJD9Fo_GZ2P2xAhlrjEmtiK1uv6JhM91-VKdxTbttVQsbyUdwz8v-JPBz4Tqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrbeMTqsyJ63zzjTPBbGDp83rJ8rWi31pZB1d0wAXvbgzywzAI1hOv5XzuGwYElFFn6LRzkENjRxyVvODsroAaAITfogZoKf8o6O7uughPwNttSSEQNR3QfG1Cqniai2p69T3danRL7U3qabb2wRGJoqPAay8M4fLsWqJS4gJYa-4LYfaCbX0S-PW79WHuT4smSLdyZB-88oWdHFsgr24WvzOIYzag_LG9R_d5yY6-9APWrO5SH7uhEtZh1EqRQuA8kyJlexrMDFL3cEJPIVRT_DhprJb2u0yE4ouuMsTzymKbWrApaJjLBg1DkXzZD0F3uHJPv_wVPvf19IutaTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsqC6BdgCBDffNBM3BxHzOAA9BtpupNbvOBeGYKMXD7RilL6CS05zNKpbkSA4x-8mV3x50sxmoEb_ghZRVxB1HxzDAnb4GNq5MZqBgX2Not8_nyrDwgR9yKA8Rmqn2iObsUNIsGTAz1oF9QBl_zXoI1DAsUvSSyFR9YKzUrCDOryTy4uW1n9hHz-jNmokk4xgvxhenVxA3Xp5m2yih_pE1cUjWPrIAjSbsAuFhaEhQpf7y7-3xwBpgw3hOiCxvkYdRQQpTyB8LnQTAPcTlwW24DA9QulONlCGjxzQUnejQIpccbq4fHjadRQX4vOsX34BUx2r04gPgNAIS_7RuJl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxyZmZw3Lo8Ju-Jwk_L3UcMBQzivr0dFsKzkZllxpIzKyuHOkwcEpV1gqDblnfcCxraQ2zSGQahCNYcjXXGd5s_Bd_QFi3pXGbvuGqbBpPmZYfx2wGtuv8pfRJgGzLWBoqGUS6V7AH64WaSEzTGgjvd4RFhwP33yxBO3uDLLgz2XvWjLQec2fVkq2OBxZ1VhGB7bCe5Rcz2Amu3fVOw3Oxun3eAWji5wYRT-uNph7bo_e0ucgW7Xe9Hh-m9Bh3Wz7PiOnLKEh_i20ZrqVukEcoGb5I6WHJXnrUgv80SdN1S7OATiyCELQOG1hnClbnQYFcp0QF4B67AaxN_Cap3kvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0WfvwelYJ9Wd0KSb7yaPoQD4cfIuoL6oYDSDjZFyoJSNrI5nEUnX7szxsCAvWa5s0YikVhfRAkkr3fpk-l2I_cr_MhpiUSssggXU4StXXOFxajq0MJdFffhBIBY9GjapED5W69FMqgbqqTk8HI0O-h1fZITzgtISovchfFzYpWxTmFBFSOFLbsQbe81o1UbrGm2mZh9Vlh32cr_ls5P0MK6KgC14nanZ2oI0Bf5AhjJcsmryOdq-IZVFd5KDF10hC7q7kjTa23FqJtLRbaq5klqyko-UfcOy6tg0rBNCi5PrGrbznPK7VLa6S9s3e3EBj6hXKhCEwONQhbyfnCDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-rZEpz_kjwuqpTA5jQx6U-vKJ6o8hEG9uwm8tMLQbwwh5hKrRDng_fNUkLbGc2pEGTr7Xgmxypi7tCCM8ua7dnUJfkfPClbadD9r61M_o9ylu6fnbb_kU7e3bw4EETNAzXDhLmBCtrRejgeJE3F5yGFeTMQK6gyy0qXMKuWHwl9zvBw2fr2FuTUqm38ZQwiHccukV1NoLqTgW76_3wjJAMQvWTllaO6C4u8C68-Z6hA4rvpUOe-BBi2XWApCU9-T2STE0iou-PjZTLfWttO92-OSvXoAaapOT4GG5_fKSeKyEres9v3uI03De0r5IfeMspLHW_okV1y-HxWjZbJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_BiSx2xGGh6-2jGYyRqm0K8NNVhWoUnSLccOCBDFvpxyRdlG9KG6Me2UReyyur4CIWF9slf1aA5ozuzMq3qyUxvb2crKcwfMYqn9unDHj-6LHo4vYy-QWUXn5tEZ8yjjFDYpi3Tx-P8bE19T3T9WMbZhsPUmzwuJFE_tD_0ytsJziNWdrqhVLbhhrt5BcZ8czsYE8pkI_Zvevp49rbx-et2OAv43FKsbeNqS1F1064FAmF0FZiy7nBz2TQBVU4NIX1PP20wosQmBf0lUZ66ivIdUjtrYd5sFwenIC8ei0FM04fBfFlYnxdw1FAngaevZlP5zLlPL2gIMhhP7DGoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZvqdGqo8cq2IlsKFNwxvW5xqFPr88Zy_zP1DV30F9lwxvZp6HOSS_tasA-ANIX6MdYXwJpJQDluLvnqoJCVBh1JCuXAPDTjMjjO0k9o28OLRmwJovngqhsbuMAgOpktK4IYDs0ZOST5rcLF5tUMI4DivYARv095j89layh94qVxf_Ajjm9y5Uj9Hfj8-IOQdS9KU7KCOEEJ90F9OQk1BukYsBKjAisYjAqr6Mfe9vrImWcRcHBXQSOMwFZPs05fm5lkVr5YO2Z-ij7e10QnmeTtiRDG79BkUUtbOz61YWKniaXUBiYU-ZQIFP3hgF5HLUP0qmebr8R0e0oCyijiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abfUHv-XKsO6uyCOnIyIbukuRjzgdr0McQWy-bS0sbTirr404tFnj5cGEqhbOh5rwGx9dVZIiodhA0pBviDmtKOqlUnInihL2ctZKRkGisb-kDs9bkRwyTCKz1YSbwPv-_fmSc3rZKNE2Zkq6MUYuw7oGEchIvoAmGYWoxTc4I1VE4WB0nj87Vpxtq0JCXhOVItYGP3z-G1QSogC8WthbfRgu1mdLD2ZJlU66IrgJxXgnSsSBv_AvDXyGBNqZGN3WjEV9n92DC40ksvzz8KSGmwS-j0oPh5zPucTC8RJD5PBys0IoqyCCVvPwxyOECvaQqHP3h8iYTKGIQWP0jLxhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=LnO4lNaEOt-DiJyu_wYHHZKb7WTj27_Z4SDdSMbWNFfaMmKvrB7XTV5i2bLMGrkOOda8PhJM7nW5-ihx8qRL82xZ1trLW-r3cFYpz_whoamJ6GluiFpJLjSyNAsfAxj72xGAkuxTNuzo4Q-rewVFnlGrNqv2jGXpBINBusK6smYrFsHW1t2S3pTzoS2d31Phk4kvH-3HqKFYhfYXsnz7hljVzXAJQbueQ_VC7Pyf_BKGn9lJ0vCMpw9uUvt_Pihbwd7PCFRfE5wtuzABbseosqUG2ZzzgFZjBRB73gdJGOt5DD7ZstXmKCTA50V06muPj2_jGG5H9mDj5fDqQpo2Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=LnO4lNaEOt-DiJyu_wYHHZKb7WTj27_Z4SDdSMbWNFfaMmKvrB7XTV5i2bLMGrkOOda8PhJM7nW5-ihx8qRL82xZ1trLW-r3cFYpz_whoamJ6GluiFpJLjSyNAsfAxj72xGAkuxTNuzo4Q-rewVFnlGrNqv2jGXpBINBusK6smYrFsHW1t2S3pTzoS2d31Phk4kvH-3HqKFYhfYXsnz7hljVzXAJQbueQ_VC7Pyf_BKGn9lJ0vCMpw9uUvt_Pihbwd7PCFRfE5wtuzABbseosqUG2ZzzgFZjBRB73gdJGOt5DD7ZstXmKCTA50V06muPj2_jGG5H9mDj5fDqQpo2Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_kQ3UvNWaZ6gPoRh7636ZZt5KjHUhNK8YM8P3fCM67-LDXJBrV01ONgfZTBZpX8lb4AhqX2I9KGRcom8U4S240i10XqH4oXMuXZtglWWp_LWYYEdawgo_0_hkNsn-3bt5QpFOarIKA2COed4_uIflieX3yVuHh2he-lpKL5I-o3KjpS8-KHdbUY4FkZbBXBSgNOqRjLJS6rtCdaHDHtjtTQsn2mZcJCeRLsYvsDlRbnZmwRx_gnPMg4Y1lKYKQ7HuQTCiRYRyMoEIU4ykCHJCiNcgsNoOKtnrOsIqEdqdQ9KF-K0XIPWGqx3MxlPcO-XGT8BagQrBAFeWALWJ4xyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIgginxsBAPQe2sq0kVpY_6D_xxOSCF2P6rBUGlIBeGrU3JkqWORjmj0A7graW6WdL3A4vOK3af_bpdfzK8ZTdcE8_tksRfWCAbsE97wlj-I_cJyOtTsQKCwRTFheeumxiQtqJ-1d1lkZuhQAiAveEVz3-xG4xi9dXjrn1o1NxQIq4humFiZ24lfsQHez7Uwf-NxheC66LopIKxwU37GK9vm-sbZQTzlyCuhlpWYXXUW058cmhGG-llmh4waolnM9Z3XskzOIj11bBndNSNr2wj_TfcJzhVlh1XA4GPUJn6Lw7Nskv9umlDH7Au57nUQOZGkSy4FBsOgLdJKGTxKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mth_Q-5Vxl9TpSIfKI0o6Y1zQcINmV-5ZLACNrtWw2a09Pn87ooDfOWLjY_MvETQKkida3V-GzZlWqZWbsHEIdD5wTu_o7mFOPwFp3aMABk7iYr0jGHCuATZtqmeXrOpPEioRzqr6HhvpAegtW9MH7wnRcw8JWoeOj7kZ2-qvtqo46cLVVDYnEKtpM-hPXVZaIM6_tTIdlNikd7fAIpI3UIG808MvMXC_T7Sze-uggAxte2gBWnk6XNbfHObDXkIsxV_ENYqexP_kntKL6ZTLRFEic4H6KroNQGHu8MHY_Nr2MmgEz_3qKa0NZxiKQFthz5_6Qx9PADXk6OqXh4lQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sxj_OMr0Cna3YsLK-hLDQOVOpO4Q4AxMRUA08WkIJ5q7ESlpXK-bd1zXNv4jMV0vcCWWS240-_smjt-SFg4bSEBM7SKaqHylxUkHT4CRUsrpXUNstlZ18bZaSVny-sPZUjzVg3A3fNEoAiZs5GFAnr5bGO-Fm7x8nGnhv-eftFlTQj_gKJcZ_xMpbaSqsAGk0VmkAsHyixxMYhl-1smSRGrnILvehAwvw5erooKnPaBv0cTf9CigkHeNiWv257RiOMKIkU6TOT3OU2ze-jIHGEabcjgwGlf0JHcdsoqXOgbA2PjOPAVKLxnheDkmXRw7J16yVbnvg-_nYA1qSkCV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC2Dc6JG4x72C6ZpPI9xtdCFyRmwzz02fGKPpFE53NmgD4Uo4SNuiDnbSlilgOswZivFp5f8oUvY0fFUfT3s_QdJ6mZ7KbHNtMC_IZNhbbWqtLbW6T44JCRohPTxsXnbbPY4hd7aanDyulbiybSgNn4-4XU2BcgHGKjP95JC1KqeTgFc3xm5jIxfMTAaIzt9ry04DnB-JAB0oINWUD_EjQHR0FYulTPHvUkEUG2j-_CmOTjzpEvQYnFOTJ62m9sdD8p7YH3vPCzDGPdWp5GrOfeeuPA49B17Nd0Vo5dcJ32h_mS0ovmKGo_b-VLqH1G6UkqyPovh1pZPS1dAyGa83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuS2sG2xoKSu0e8XKJu2sgAbymRfhnCFG2PQRvE9alDrumpCAWS4IqbWflpFylld8tj0au-twbJMmLMk-KKmSCOxXG3PIFNVrMRaK_rd-6mzh3_6qCHPnHZtuRKI-zh_krInDG99L9seVYNjxE53yveZXTI4Ha1I9zYbm7-PjaV9zwIyQC82N9KteZdXx_ouJsO96j_oIm4_4IeJWT2y_QOyiwgBPhhpRAA4625Ro-sG-UMk70FWzSe7Kbs2Q5FmodMJHASaq2fzyUqeJD5II_ZmLF_Dek5f0zf9ju7qXfDLdgl555idrPWITOrpTrs03X8NvGK9CeWoROEEAuUg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWHmS7UjQAYSraPhzRppVxbhT2UhVCvvwApqYDDaD61m7S-8kklhiQCSfJT-1M1QhnVfwh2celZAibwRNUUl2Z7P_5LwwrL4_dsjFkkUnW59ILML9XRF807QTm0NW0DHAH9DPtGVm0XGA5IeBpAuPJdPjqQ4x9y5vHZENjqCdcKEEi77nSaHb-6n8Dml6h2Z2yzjInLpjSViPvYiYmT8ZzR9oSHsU0Mzb5N01QOgSZ87xM3VVZDB2U0wgQw_3hnIOMRb712x1NUZeybhsL8e6afF--ZwYEtWyVaWOJMLUqriMXYzrMRSCPfz0H3N3zK0K06-_ZGmP-kDRVHudUhtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=MqYs1f59fXVoVKZwR8kUDg9KagshWr3dF39ZaInQXNqykRVMm-Nyxf22FH1JxEv86BM07XOldwNQQs9yhHufdwH8fGiTLAGh9wvp8As5Lgd1R0IvVDY9euFwq_AJ59MZ4OTU4LbT3S0dM9GTH4R7w6jPyVitFenmULydDA_GfsZ2hwIOil032LRP61pISIgzqTGMmYjpW2Y8PKGZVx8cpAYhGlMi2Ao9jSvcHwKnO91tu9sE63Jc9_a1-ROdAp7saYd9rqBFyWtsenE2OVUMd-yfme60RwYW9oiauwZFJkcVG0VrF8BiC17mOXosBD37atLkzLTC_F2nRrfQKUljObwlZxP_jzWnJKA9OUbkV_lLz0mi3OJbg-gl8QeaDMxeLSzfjIy7Pqgvg_VFojaDcDbTPwWIfzwnZ9OnFvFh98DeM5ZSR70pl2oPHa6nx_W2oyIS9ZH5IHJ8La0asYhlRI-lQg-kpRHVSgTOk8cXwMzOJxxWgLR1b6tsgN6TqQ9xjFFKa0Jaqx74cWC5wOFTBk4yN5HNvBtinIZ77F7uYhS1xhDH2izOYQIzMN494ttnTx50GmDpRGfJ3pH3Z1W8NpQS4q-Wesn30AE5gpDI1KKG1vuzjKfK3lCK7TJiSW4m8J7IBnNQn3NPgXA1BZchoAZKFlrIuvoSWKv5f1iWWig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=MqYs1f59fXVoVKZwR8kUDg9KagshWr3dF39ZaInQXNqykRVMm-Nyxf22FH1JxEv86BM07XOldwNQQs9yhHufdwH8fGiTLAGh9wvp8As5Lgd1R0IvVDY9euFwq_AJ59MZ4OTU4LbT3S0dM9GTH4R7w6jPyVitFenmULydDA_GfsZ2hwIOil032LRP61pISIgzqTGMmYjpW2Y8PKGZVx8cpAYhGlMi2Ao9jSvcHwKnO91tu9sE63Jc9_a1-ROdAp7saYd9rqBFyWtsenE2OVUMd-yfme60RwYW9oiauwZFJkcVG0VrF8BiC17mOXosBD37atLkzLTC_F2nRrfQKUljObwlZxP_jzWnJKA9OUbkV_lLz0mi3OJbg-gl8QeaDMxeLSzfjIy7Pqgvg_VFojaDcDbTPwWIfzwnZ9OnFvFh98DeM5ZSR70pl2oPHa6nx_W2oyIS9ZH5IHJ8La0asYhlRI-lQg-kpRHVSgTOk8cXwMzOJxxWgLR1b6tsgN6TqQ9xjFFKa0Jaqx74cWC5wOFTBk4yN5HNvBtinIZ77F7uYhS1xhDH2izOYQIzMN494ttnTx50GmDpRGfJ3pH3Z1W8NpQS4q-Wesn30AE5gpDI1KKG1vuzjKfK3lCK7TJiSW4m8J7IBnNQn3NPgXA1BZchoAZKFlrIuvoSWKv5f1iWWig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=GHGCwGKyWObvG8cCS-oZRz7JhoSoczm7vdUHnVmNC4R3IkTLTW2aqzWoEoHgC0prWomnlMPr3WodkHxac55KpgT_DzumZH_TDV5tdstKxXd-SXv210pGSD-3ijRqwE4SmqwPVykGdhAni1zVbGxT7Y8tHcZhpVNssknK_NKia6iAd8pIjG_5f6Dnam3Vu9GYJ4-xZqXZffTLS1rgEFpEIA7Yu-reIXIPhhcqmeiuEpF3sEDkz9jEcIYTP7mfHeKCalnGDNVFTgtedE_SJW8ti19JddPEuwJcIn3p-LVVvAfobZWnV0NigXowmlcKJI-T3N3QcrwgMt9XGi2ghgTE_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=GHGCwGKyWObvG8cCS-oZRz7JhoSoczm7vdUHnVmNC4R3IkTLTW2aqzWoEoHgC0prWomnlMPr3WodkHxac55KpgT_DzumZH_TDV5tdstKxXd-SXv210pGSD-3ijRqwE4SmqwPVykGdhAni1zVbGxT7Y8tHcZhpVNssknK_NKia6iAd8pIjG_5f6Dnam3Vu9GYJ4-xZqXZffTLS1rgEFpEIA7Yu-reIXIPhhcqmeiuEpF3sEDkz9jEcIYTP7mfHeKCalnGDNVFTgtedE_SJW8ti19JddPEuwJcIn3p-LVVvAfobZWnV0NigXowmlcKJI-T3N3QcrwgMt9XGi2ghgTE_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4ZUVZvs_2kQNk9txJZETG2kYdQclXAuRE36gHOnuJbIiEsFAmoc6cizwJIkdNbuvDg0TDMqJtNFFkyzbDkp5j0TwujiLuG6Kto2GE9CvmMOVobrDfQHmxbUmFgf5OT8g4Dm4WQjTrU3qNh5HftARWCCdwb05H1boz-6HEpPz1bPBT-7CMYsOXDmCBsTu02XT6_3_-43FsUlG3Lty1oY-rOWng3Aq6K0TWKz5eQRPeb--K6F0EGGFLYBQvL_D8iyOxs3ukjn8wEU_7lWYPyqYPKYPqtNRvpO3qGlExks_7aq_wctLuIQxdJ4dnV09araxG4qm3v0FPk3YlqaA7ARcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLgfwTTlnW-R2GZ3DkXlOhVospixStnKRFjtkTKropeufGXWLkNAib7GlBgFTBzIbx4IoEjk9r9iya6EhL-HorG5dC0MdowMISALWzVcE8CfrTkxPmRVbcmp1KlrUhHfd7sUvmFv5SpDrLKirzY0uzJ0A7EvzfUbatbnWWg2KGmgP7ExkDmRDLitbbUzlX7MDESRsxaHPy3fh3pZNBpEyPDnikYntWdRp5OjT4u6da7e-RGZh7h8HVt4XNtCvdsfNNaJe9Qv2unB_cqRnCYm-z_Ix8HVH_2qtwa3EjIgdGYVzakcrRTSlhORXopCJK-7qtPWSyqJWw7qowEovSjHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=EDgmCYU5He-aGjnkTI24NZ13C3KkLFJFP_IgwkBPfAsV3hkfz7dwW3pCmb6af7g1QZ8b5NEzTyvzUyGDWgSxtKVmImASfM1j3cHMpl8KnVEMWVU2x52jM8J6paEsmTydLN2XBBYxbulqKknW3ROjGBKoS9wVH__hszNIv0ok3tmK2QQWbOQtMdBb4yzR7FF-75WXDWxyXZzAqhUnKuLdARk8v_jos1QGcU2JskjwkYZrLBOIB9qrLNAtD9OfODbljCBL00G1rPbMx4bNlFH-sQSdZnX3_xtUEV3tnKta598ThmKRCDF12JsKqWzSVeIoM6ESEsjVYlckhAJX6vQPPIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=EDgmCYU5He-aGjnkTI24NZ13C3KkLFJFP_IgwkBPfAsV3hkfz7dwW3pCmb6af7g1QZ8b5NEzTyvzUyGDWgSxtKVmImASfM1j3cHMpl8KnVEMWVU2x52jM8J6paEsmTydLN2XBBYxbulqKknW3ROjGBKoS9wVH__hszNIv0ok3tmK2QQWbOQtMdBb4yzR7FF-75WXDWxyXZzAqhUnKuLdARk8v_jos1QGcU2JskjwkYZrLBOIB9qrLNAtD9OfODbljCBL00G1rPbMx4bNlFH-sQSdZnX3_xtUEV3tnKta598ThmKRCDF12JsKqWzSVeIoM6ESEsjVYlckhAJX6vQPPIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJR-_MoWXkuhu7F8U3TdJbS-pc5PVwLUX7ntdbpPUSsvo0sGb2HC-6kxYAxBbjfyyFZkfguPzC3N5a8q8AwJN8ToWWoLSkXKdizZOxzCrE7v_GPMzogIOsATOp5GIgkT9zvnzPShLn5zrA-PitDjmR36QZz3DkaOCVK7fFV3jj22pLt3OXyIPq_S-z45i-JX8l3EPMNTdSUZMFeOJupxQB5wwMEAl5y7K9m3hY5oqSb2q4mtfQ_7nTlLobmtnMBWQR6dBVjpTwx3X_HpOqY-Zzh-cuT5BnvgOq92aVwRe-RZI1NS1PIWd5ypG7ZCCL5i66ImKiQxHQZ2WnwwsV9xnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzR3DvtGFZL3Vpp6y0O2FnbQUOC1XflaiLGBg4h1XFn26cF-hxMnNQUgVLpPtxsYOSEINzeZttx1AeEyYifDp2nUpgwHH7UeKSGmd1ROJO1VOqqEfBiXOFJzw4Zk5amhurQgN72pxr1_2mAT0MDUTPw_cZKfqsMyWtDAazZf2nSjSbNTyHyDTnKteBfjBe5s37D30GCzMtAbN0AclESvW_rUZLlOcDHZPnil4UXlca2JczIEIeTMNgY2OH21CXRuS7oenb1mHDWAfDyYZAPP6OXWTinYCVOHmjwqSE8KWNg9un8FRWRUXz08tRUq9Lnb18_oBHuf9eeMVY2zV8BJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqDxMfhvAV1_Z7etk1-IFIkTqEagSsewBdOHNtlrcxhAXXfTc1NOph6Py-GQFjxYgpkaRg3GpIQz5D5jwfezncS9MW1zxLi17gmnoMZ7HCNMMqzXUCahVMfZQtESlmzHfPX6Ed1KuV9kaEV1-ES2KK7notWOa_MV4l4N_exkMYBlp7M7k0K_iaI_taJWkV7kU3HGgckf7TiRIZsSMzMzLaosaVd3G1d1fymqydRzN-s-ZAcUY2h75j6qHbaPCeasoX023t2FuxNF1j62DMAIRWZgiykWLNyP2RRwvQKTrJUS3GMhiuEKJMCByfQymJQIzEaOq27A6xwf9Lw8574OLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp9fMmpzvxOf-8_Af00Bjx5iUaI-VT4jFSL2GjueIYX91JmoFwNaWVhFAgSZlHFpWABnwv7uxmUXLoqistHgaQdt5ZgloUEw_wek2koaTE7M-QAvlSIZEx395pINnY3Z-ig1OOrHAbtWzzeTZJbVKcNchRIiFcYGWCeDUZrPLHZ9K4juit1m1Q9UWyN-Gio2iQvXgHnDhPlpefQVHySO21GhfWnVbElC-hYhaXFsemAekzz7qUoYG_IQ8BZEKJECA1yFpLk_7_r8CiJ4kt_QGBKQ2U7X54545KX5Logt9xNsINRuXt3qR4VN6T_Ie7b_YQGOcaOzl5QGd0_sUR7-qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqDcNveQ3QzXgw105ZFguGhbfx5ClFLSyaVGOT9jhrBcqZl7jGq5qk9OueZaRdwE65n4r3ffOLvyG6clGnP_PeNLD3jGpowlJvUSh0ia86dJoXxfVWHhXpifbStaubrr9piZ0zRZMwxI9eyK362UAga1nVxMf9axwC8Vzq5hWYxdYOXeOCoSMtoJktoJEHjeseq7UzwGJk83elj-ge-NQXwQBLN1NUvvuR96l989KsNR_-0nI3XNXbdtDdTo9auomavdq_vSpn7jTnxZQzMSGRjtgHF7IOSzkxpwSlSq7pk5ampAcW5PsbyR1pD_QjFKjI9xhwfUaA0nDLbJ8bnlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5ZT6qDcawYvT9-2cMnMzhSEqGJkJpHU5OK9HO9GSPr0UHc0sOy_ET3TUvG0gR0pk5rBiL29XFMUUxeQ6ZOErEms31D6Ux49Ool7VMohnfUdkujTOg87IwcI8CZkqBDtpbYtJuW3e5JVmLGCbTEEQY46so4zcGyhxpLc1bH4l0fiNrGBMQkD7d4QAtjbM4LspnMrRfiJfKvWqg8uVnA8ZQtR5gUbnF_cnTNpq3GsywdOH6u39WARcrQmaWog96xj7RK0Nhq6i7LFexw6XcnTGUx-xnmMbaM8UM5geanpcQdSyEkOaijH0gA355WOlv5bwxDu2CeiEE4qtf14xgG_MyLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5ZT6qDcawYvT9-2cMnMzhSEqGJkJpHU5OK9HO9GSPr0UHc0sOy_ET3TUvG0gR0pk5rBiL29XFMUUxeQ6ZOErEms31D6Ux49Ool7VMohnfUdkujTOg87IwcI8CZkqBDtpbYtJuW3e5JVmLGCbTEEQY46so4zcGyhxpLc1bH4l0fiNrGBMQkD7d4QAtjbM4LspnMrRfiJfKvWqg8uVnA8ZQtR5gUbnF_cnTNpq3GsywdOH6u39WARcrQmaWog96xj7RK0Nhq6i7LFexw6XcnTGUx-xnmMbaM8UM5geanpcQdSyEkOaijH0gA355WOlv5bwxDu2CeiEE4qtf14xgG_MyLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnAtVTDuYBbHt4ioHwLEJSLWkHFsKiV-TEU7-iabYhMPY-netyZnUuRCI_ZA9cy2PN-gVYMmi1fO9vUCQxscilh1wy65Y7QcYnF3haJRrSQ8-R3pYkyPUYP1o7HZ9rUAVNFBNdKzFADcFFAPlwv5LEFTiwArUIeV3UiLtXxo2OZf6QDAr8SHSlRWyBes9HWghTBug2qxAsQGTF7Y_wjVNO5Ml3K7VuCP9Nq0UbU5YY30sjo45QBNunQSY3N9iCx7tnxzNHD8lO9fE1oMrdImGq9px0EzjXpBfP3U28AXlCqEvMvExuLMVCGDJ-b-vrRqtOn9N-QfxyNw4aMJoXJWf0qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnAtVTDuYBbHt4ioHwLEJSLWkHFsKiV-TEU7-iabYhMPY-netyZnUuRCI_ZA9cy2PN-gVYMmi1fO9vUCQxscilh1wy65Y7QcYnF3haJRrSQ8-R3pYkyPUYP1o7HZ9rUAVNFBNdKzFADcFFAPlwv5LEFTiwArUIeV3UiLtXxo2OZf6QDAr8SHSlRWyBes9HWghTBug2qxAsQGTF7Y_wjVNO5Ml3K7VuCP9Nq0UbU5YY30sjo45QBNunQSY3N9iCx7tnxzNHD8lO9fE1oMrdImGq9px0EzjXpBfP3U28AXlCqEvMvExuLMVCGDJ-b-vrRqtOn9N-QfxyNw4aMJoXJWf0qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=kWq6pN0C6iL0xCjwHUAMoccTrmsl9mTNOOdFlaJYA3SdufSWK2CT3uNpdL0qr6v8no9OoFpkt0mps0yGTDvNBJg8K4b89gn-bmaB7u5vp6wAJdwcmv_v87fdt50aGfDZ7qzfvCLD6GaOcUh3LrNRC46dszsgH7IFSRAM9gsb_croAbW1WVg28jTqIMWhsuClqBB4COyiQfXsITKS7v0Cz0KGLLTFR2UU5a7Dz-tqMM6Rd77AyjIUyo6APlOngKglV-7SJTDiUxkYhdOBBLt-ZEuJL-VwazFbqN-HKAOoKkAaZNu89GbiXGzOSKgP3MqC5Ri3jwVAf300J_3X4qEzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=kWq6pN0C6iL0xCjwHUAMoccTrmsl9mTNOOdFlaJYA3SdufSWK2CT3uNpdL0qr6v8no9OoFpkt0mps0yGTDvNBJg8K4b89gn-bmaB7u5vp6wAJdwcmv_v87fdt50aGfDZ7qzfvCLD6GaOcUh3LrNRC46dszsgH7IFSRAM9gsb_croAbW1WVg28jTqIMWhsuClqBB4COyiQfXsITKS7v0Cz0KGLLTFR2UU5a7Dz-tqMM6Rd77AyjIUyo6APlOngKglV-7SJTDiUxkYhdOBBLt-ZEuJL-VwazFbqN-HKAOoKkAaZNu89GbiXGzOSKgP3MqC5Ri3jwVAf300J_3X4qEzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRrI5A1RY6X6uep8DczEWsE4Ji8x1NQVrbh6ug87q_jDQ_WwRiS54BBgetDTNRPaWayjlOhJ-PWEEbRqamSTffhe2Xbz4uR4ghLcIx1nHkPJAuwXDwHy_d2pwYyXqZumA3VMcnj5d8KnFiCkd9-sspdROVW1LqkNflSMeJYBxBuBIA52-Tf60PvXQA1UZlf8sWEWtLFDbFgafqJjZp3kTR7AVzNwfmDflJGQ8--6BF6Ya0kX1IDkP-pLC1lWhiWilauqwqV_sV3bf8rBC0B41xSO6mbtVUj-mgWm5npCdcm6AEqfiP-p4wrHILnxP0LDeuUNxlBJ55832GL5tuRWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOXbcU_flAyM2wJjS-ADfP9LNHdU_ADFxRsjwgSPRyRVWNQvjeqigJYrfuOuGo-F8dr0M-o9RRSrn6NXEyrVCjZ5wG5abldYS8dPtU8an3B9ZkO37whPfZbkaNSMg1_3kNmcuD0f_1rtkKkP8UXLGG7EF0mvunGZ6WTIj0iBCcti92gDgtgH3O3LqaKH9kSEeS9E3I6XjZeZ9WjCMHM1hSc2zet8OBGNJC7LPosWfnb9q80Ptfk1o90r_yBEK7LdMFuClCoZKNmk4swYPQxanuueQ-PmjrHLx_TwOY5Hyrb5mSbYVkGhQ6LF9t_cFbHFtygYFx9QRY6NIMBFpm3RIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=MQiwE1Iw3KDok6MnrCIyQGf8YKG0uSv-OxeXgmTwB1NL9VjalXuYy5AMGGNQSyJ9Ez9RifiOs9pGUk4dOhSK_6oLVCMAQArB265eBQ0Wr_WcDyNlM6CXq8xZAG7IMX3PCQDaN9jUxt-2Yu66znL3c51aVJXfitpndYxTOOUQX_RXWVYVZS56_dEp_SegxdqkdpeTDKl52uWi_frEw77yrsaKJgs9jaQWhvuviNX_Urd3vOC6CINuyOOrIEuvrGOLfr09CqaH8lMGTSG9zXxly7izFTFMF2xrx4G8kVNoqPxZg73B0dXhqKo0F2sH-n5S5T9-9PYEMBFRxhbkB2D-_IH8aIcF-6xh79149M52ZNQUJQetLw-egcyWbjVsfxkPblRxSetL2odh1H7ZVFN7N4rxEd8KckKYevLHvEHzeWl6sujPz40hk9XshJToCoFeM3oi4SOu4CQerpzJDuGA586Zp6hKz-EpdfieiQ52nyp08bI8RXMNcX-pqflD4OwPd9u4x5d8x2XoEIDUN7xYBPNF1bKfut-MdQBSaG1fkBuAYKwFCIvT9ZaiHVvzR9J8zcTP9vxuHYckXgApMLisY-UufbLZNQnbdvgFsqf-B2gltGu_CZyvXeP1d7xsBxDOGnBAXS8hcWlT-Kja3JMmeL7HTSdsU0epSHJ36na3Bk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=MQiwE1Iw3KDok6MnrCIyQGf8YKG0uSv-OxeXgmTwB1NL9VjalXuYy5AMGGNQSyJ9Ez9RifiOs9pGUk4dOhSK_6oLVCMAQArB265eBQ0Wr_WcDyNlM6CXq8xZAG7IMX3PCQDaN9jUxt-2Yu66znL3c51aVJXfitpndYxTOOUQX_RXWVYVZS56_dEp_SegxdqkdpeTDKl52uWi_frEw77yrsaKJgs9jaQWhvuviNX_Urd3vOC6CINuyOOrIEuvrGOLfr09CqaH8lMGTSG9zXxly7izFTFMF2xrx4G8kVNoqPxZg73B0dXhqKo0F2sH-n5S5T9-9PYEMBFRxhbkB2D-_IH8aIcF-6xh79149M52ZNQUJQetLw-egcyWbjVsfxkPblRxSetL2odh1H7ZVFN7N4rxEd8KckKYevLHvEHzeWl6sujPz40hk9XshJToCoFeM3oi4SOu4CQerpzJDuGA586Zp6hKz-EpdfieiQ52nyp08bI8RXMNcX-pqflD4OwPd9u4x5d8x2XoEIDUN7xYBPNF1bKfut-MdQBSaG1fkBuAYKwFCIvT9ZaiHVvzR9J8zcTP9vxuHYckXgApMLisY-UufbLZNQnbdvgFsqf-B2gltGu_CZyvXeP1d7xsBxDOGnBAXS8hcWlT-Kja3JMmeL7HTSdsU0epSHJ36na3Bk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=FvGW8_79bOaP89Gjv6zKZn1uIc15ox1HEXpO0V2utSAmav36mdycbFCsaA5Fs0-d7IqbI7q7smyB7TD95SD9U4e_lwqWFVEIAUB3YbaCmldCrxyH5wnCZsMzEFpwB8128v39BR0W-gZvlvAxd58f7qKDhL7TH_pWbcYfsiMkBwD-VHGcFlguzf2P5SecHCLJkEkrOMZ6yqVEyPjm56iJKO3ZvhnmBuwg2bgnJfOgMB0-x_elkdSl4U3IdyTlEvSlNDvAv3QWJJLATv8p_qCFm9IfNym_CmSpw2UxD2QGs1UzFD4-Yx1Vt_TC4ANE1yIOSteb0vI0Sf-bgMH_iCJFeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=FvGW8_79bOaP89Gjv6zKZn1uIc15ox1HEXpO0V2utSAmav36mdycbFCsaA5Fs0-d7IqbI7q7smyB7TD95SD9U4e_lwqWFVEIAUB3YbaCmldCrxyH5wnCZsMzEFpwB8128v39BR0W-gZvlvAxd58f7qKDhL7TH_pWbcYfsiMkBwD-VHGcFlguzf2P5SecHCLJkEkrOMZ6yqVEyPjm56iJKO3ZvhnmBuwg2bgnJfOgMB0-x_elkdSl4U3IdyTlEvSlNDvAv3QWJJLATv8p_qCFm9IfNym_CmSpw2UxD2QGs1UzFD4-Yx1Vt_TC4ANE1yIOSteb0vI0Sf-bgMH_iCJFeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isZG1K2WE2xRHzgmYV709Mx8i_-1dQRu02VH_Z_W-9WiSGO8TC6z-QLzl2L3Ed6icA2QnNfjxMo5p4d5gMDZKCdCcMYvbp0ss4ylwT33qcMPe0KZ87yeGIADcqDtHiH8GHnssSKcqMDGeXN6SihdzmxQo22W_v7pLYP_tQ_ZTB3y1WetBY0XLRa_teEwacYU-isnx5-GxQsDGeS6E6rJydxrO8SEEOFKi3HUCJbNZB9jGdKP2K7NtXvgGYs-BirOUgnF3wJ6R0Uo53zzewWe03PSr2_veMjcyumVf-ceSk_eRKPerhysY82wgU2qc_pfk9lfI0rCrbE5MVtsYZzHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPGuUGJp6bIRBK0ERK06Z-nQq3UDJ5HnNIS8JAB28ycxfmuqaoISxT3PzJizlm3ddi9YeL52WI8gy8p34vJjmPjmPe5kvtF-_LYzr2nowob_Lp9mpl5-8GdHDjdgIjz9sck3RC9eF8XKflpPy1vNZQEUyCXIMTTFeJTRAvTEwHc9UKFkV0P5f0kligpoBbBfHyW_9LWxMBqD2jqfL84ofa4wIeGxYYVLNO5X4SxXklrAyP2H209V7ySyB9E0m9jkD0DO6XX2zcI1SnDA__edwIH6-o4brOAx2T0h_Y60BkWp1BpivOhcdrMGsB_uHQpz8ewmcORmStp4a9yfk87fWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ok7t6M2f-3AjVnQjv9xDmz1Sv3GVsZB9bDttwoPyz5otWOVz2RyeaYNCrxFDxFd9Fs4X5HB3B4oorY2-HW_9BMj2kc3I5fyzXzoESqK0iKVx1nzAWeInNvp2CjvUN6WgPO-5BjK503XRTubOYiebHzdurG_sa0K-YCt00KfhFBd7h6EEAvdMW-THF3yrH6PlWz2kc6lU8m4FaABGCqbpL0OKaaSrW1geXQrWyr3Ppzw0RUybfN3D0dKNm6rIsjAhxKWiaQvA2tE4yVKmpLd67JRVxkkpD7tUsTNUZkbfFm_oL8-GNWGf8u3C-_R51eH8HjWP9ZcIENQD9HBdV1tQTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=AEbUkozIL5v_dMMLpOkDFj82vAG_ycmbg_lQZn6N-qGUWv5aS4muQtlLCJ8pvtYkXhlZajtT6bnnp5IMSiBzQypRdWYMRD4ZHFuIuiPFF8mCcOf9fQTdGipl2KP8XHatQpTA3Ud91lhsZ5K4lsblch7_mOmWVfaWztCHIs6AF0v2N931UjPw6WRpSnY8OE3B4WHN5Mcq5EKI0vClDyyNfVi5g8umQtyvWrXC7LGhKwK_qrY1PHpGxGEagCl60E5qwLhTEWnutmaRPNUDTsGau2hEZqLsk_RA9-IFGmo3Am1YBhGKNU934ohj-fzgGnz6IPWiLfEAZokV64jSSX4l5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=AEbUkozIL5v_dMMLpOkDFj82vAG_ycmbg_lQZn6N-qGUWv5aS4muQtlLCJ8pvtYkXhlZajtT6bnnp5IMSiBzQypRdWYMRD4ZHFuIuiPFF8mCcOf9fQTdGipl2KP8XHatQpTA3Ud91lhsZ5K4lsblch7_mOmWVfaWztCHIs6AF0v2N931UjPw6WRpSnY8OE3B4WHN5Mcq5EKI0vClDyyNfVi5g8umQtyvWrXC7LGhKwK_qrY1PHpGxGEagCl60E5qwLhTEWnutmaRPNUDTsGau2hEZqLsk_RA9-IFGmo3Am1YBhGKNU934ohj-fzgGnz6IPWiLfEAZokV64jSSX4l5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=Zrk7Mj0OWnM8INmg4oYQucAmsufh6pMSJ49dE29UJRfotFftB9CiV-5jd4GiK6kV_NibEK22_LEjaHlzZiUMlTpfV4mZwj9IiA6aPEAQkNugHfpkBSyBjbPysIGCzH0zcLYCTS9NUZll8GZ4l07AYdSapgOotQpIJfmHX7LTs5U7PR6hdqAmBCXMqnGtAy3lf38zKv2_cKq90ur31_p3kJX60AbuxBf2K7jbY8hcQ2jHX3YjdlUEa52XgzTxMRrTk8YKt05nkieIynR8n9yk2Dkn_cwtQFg4NkPLrtrfjPiXzcWwT_AIaM3UKbNKmTTNcfyG_ph0idiE2eTITwp5hTzi9-jZJrK5lhZgizM9MAeTWAYlfZBQzcP55v8efELKiGX_HENe6NOuc_hVSfi5maRrMK8qnIJRYv7SzrkF7oPM75QJkSOGOXYeOSksBRgI01Ibom7o02w8UEGF4Ax2sITjwag6u9CHpD4FMvu3UsXRN481FKdLZyI5KYSZ7ExdzOtG_DRdBOGWLkJ5s6qYQSJ6fLujsezUfQfmlNuBoM4DdaP27pv3hiLNvOd9lmROrTG4B-HFAtOOrDsjc7DVD1ik3zKjKz7p2oXLnbazS0iwiU8ZBfCRc1mmmhL0ZJ-FeLigyYMeJhAgWn3DZ_hVhZv_YBabLs_C8RbM9xoCSys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=Zrk7Mj0OWnM8INmg4oYQucAmsufh6pMSJ49dE29UJRfotFftB9CiV-5jd4GiK6kV_NibEK22_LEjaHlzZiUMlTpfV4mZwj9IiA6aPEAQkNugHfpkBSyBjbPysIGCzH0zcLYCTS9NUZll8GZ4l07AYdSapgOotQpIJfmHX7LTs5U7PR6hdqAmBCXMqnGtAy3lf38zKv2_cKq90ur31_p3kJX60AbuxBf2K7jbY8hcQ2jHX3YjdlUEa52XgzTxMRrTk8YKt05nkieIynR8n9yk2Dkn_cwtQFg4NkPLrtrfjPiXzcWwT_AIaM3UKbNKmTTNcfyG_ph0idiE2eTITwp5hTzi9-jZJrK5lhZgizM9MAeTWAYlfZBQzcP55v8efELKiGX_HENe6NOuc_hVSfi5maRrMK8qnIJRYv7SzrkF7oPM75QJkSOGOXYeOSksBRgI01Ibom7o02w8UEGF4Ax2sITjwag6u9CHpD4FMvu3UsXRN481FKdLZyI5KYSZ7ExdzOtG_DRdBOGWLkJ5s6qYQSJ6fLujsezUfQfmlNuBoM4DdaP27pv3hiLNvOd9lmROrTG4B-HFAtOOrDsjc7DVD1ik3zKjKz7p2oXLnbazS0iwiU8ZBfCRc1mmmhL0ZJ-FeLigyYMeJhAgWn3DZ_hVhZv_YBabLs_C8RbM9xoCSys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJZDLbktTLPS5OM-F7TMR3HxdKVuXMr9pGvHtWqrDrRPX8q1hqfuV329eeSJLcmCGr_W9xYwIYIq_Z0hPwSamoBzEWAKXRyfneIuJ-X0Q7yCaGTiUuE51AyXxuI0IblPfGAyzTvkmrTpnII6DX0_BShbz_9hib93tQgXBkpjyxRNILMuDgHZkCe7tT8IwiSGz8OmTYbfOm_ukDdLul74gD32xEdLvWT-zihZBj3RX3KTucLMrYPCkL-3QhpcvNXkkfexvauOmNbTCFAiMF6RZL5k_jxh8u35B7y7FiN77s2Me6ASU9KkzPA1NNxkp3OJ6g0fg0vaUaRYZqk-egfeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvPOfVmW9PbNbh4hPXXdpDT8kqdLifqRyDR8z4yeZORJCPZTMFcYkrU4vfKq3cHZg6IiuP5kC4WrwGeUT5WCuLl8qVRFft9WMk9N4Y0pJSomF-j6sBzqIqHwFaUF1aEFHPhLxYAElI1uhHmaSTGFUP3emPGJEP0rC79RjvfmaNwNq1D5YQQWnltKnQJ1ono5z7SVNIrLLAwlEYKpqYTBwCa0YJ0hivVPBcfhbVuf3DgTj11DjvKcuuO2aPp0h00RMwv58td4vPvxTigfSoHdbJdvA071hKViKX6JzFAXv2iLl8FMidDr3HGF1FjFC-yj0TFr3-Yrt-v3WjM1JWxnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=kF6csAc7xcz0NARWbPX26vP1jFSHexRSzEM9HNJWaU5dSkYo5DsPqib2CzUpkGU6wzTsZvSJ8cpwnyWAT9788phkd6PQR8dJn8wXsA45Vxd1cZlB2OY5uAYbwd5lAMcvp8d7nmXZIo-4G5Y7lPAGOn-HVmIQ2bxujJF1ocTtAIKrLt03ITJk738b9BxtgdcVlh1nZBPmUwIGd82eP4oNqMbLbceon8IGO5GkL0EoWtY4s2mpHeFi5tWtmdOadL7LpQPnM3ZoG5pdi-DH4DGG1zvY7roe_5twpawXiV9No4zpYv3hkYrUWIKVvJX6kh8z82Py2PzumMiYGQVkFMT7-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=kF6csAc7xcz0NARWbPX26vP1jFSHexRSzEM9HNJWaU5dSkYo5DsPqib2CzUpkGU6wzTsZvSJ8cpwnyWAT9788phkd6PQR8dJn8wXsA45Vxd1cZlB2OY5uAYbwd5lAMcvp8d7nmXZIo-4G5Y7lPAGOn-HVmIQ2bxujJF1ocTtAIKrLt03ITJk738b9BxtgdcVlh1nZBPmUwIGd82eP4oNqMbLbceon8IGO5GkL0EoWtY4s2mpHeFi5tWtmdOadL7LpQPnM3ZoG5pdi-DH4DGG1zvY7roe_5twpawXiV9No4zpYv3hkYrUWIKVvJX6kh8z82Py2PzumMiYGQVkFMT7-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHv1uRXhmG1cD0jrbL_Rm5qYzUTuVvWYCy8ujMPr2ru7n9raNJbcpc2Lk159EIMQP_1w36NDWj1flqmYJWi1ZO7iTIvAEwKLcPLAgT22TlQNA7rXvKgzpdQBeT2JlLOFSs0YXjHgGIgyQJPUzTEeb72S9aQBES9Ip6_ROo5rcpIeOxs1HWH-AEJW3AtcwQo9S1FKLNcdDiGA56HoBm4tYaI-iOjK1eH3ab6x1ngm7eazlvTjAdeLw_yK0ZrnPRv9Pk8baDJr-Exsr26iIZ3F55y_fgAsLXU5ELe-X_pauTLIWhPPRU488K1PUVHrJfzzPbkSf8gHjlPmH9WPwOCOjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3HQmGvqA40FjA3rG0L0sLsbmvxyf8tXzbhHWRfbju5cfaJich6z6jQbmU3-qOqasJAWw-Yu2QzsJhUOgsqCC5WP-aa9XTET9A6dmlX-vNxNJgQkhwhf0W3zRONnMISjwC1z2sLuTqGIaVdq9SUa-AzM644ZA-XluuYeJUOXi-5EG5l7E8urnao7Wihi3XvAFG4tC3-jUpXtxCV98AMTpDyQB7C6SE16hVdQVCGRWayIkVf_UqGITKrJKb2yFWfy2yfj4EmRYRRFkIsD8dlKFUV7R_S6KTCHtkXIAC6bmSqUbAAKGNuKi-YlslB-WuDYkykR019w8oeOxs54q1ryoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxmpq_FSLfPEjvmH4Uiwn5ofTJBmFrojBPgodPWnkMVGHdDjL3UL-ILV6NVjmCYAcfsvlKvxf4mjkLEOe57omOofuzbOJiWPrsvLzirVhNaoJOg0svBZn8CUlMOtKsirwDzby1EhIj-liXsfyW7TMHjRy4sAfks8rUqLtuKprw42VR9QmEc-fkBvVdLqOl5wUeEZddhHCOTtKZq1s6CXuJYwzQIxh4qo8wmRDcSKD09Lwm3SK8IG7oxY9zXC5mXgy5yJ7rMHDvyfMInF4ZAtD8c4q24qPy8UpknW4tIFJAzMI3C43Wo53o68t0qmbwgp5WaT-5r8_W6mg4Zx6VLW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLR2N8oeDWRByU_3-0ouzjDLLS5p_7eRXJQjDdD3fJFh_f0OdKeeOSo2KyQ3i3kgp72XXDuSS2ns7kHh52l34OxCDYbAEP06P-U2wYqji1N_EefW6xcGVVqkD_PyR3ztXsX4DwqxEAvODcc2A1GQsSfZk4qvVJvHxZw5zNM5Gwim39nMqWctPI-Q7-Rvj3iA13hwKaDjJnXn9ACVZBixF2XdbwuqAU8DHPZtpHSMA7HaFXd4WX7dPZaREJfQ_IPel_-wykofdQ6swwaSoNDRJHeJjTueCDIckROSJs7upBLmf3NNjP3et_D39VF2lTOob9GpSmvZjhozsZlGpe4e5z2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLR2N8oeDWRByU_3-0ouzjDLLS5p_7eRXJQjDdD3fJFh_f0OdKeeOSo2KyQ3i3kgp72XXDuSS2ns7kHh52l34OxCDYbAEP06P-U2wYqji1N_EefW6xcGVVqkD_PyR3ztXsX4DwqxEAvODcc2A1GQsSfZk4qvVJvHxZw5zNM5Gwim39nMqWctPI-Q7-Rvj3iA13hwKaDjJnXn9ACVZBixF2XdbwuqAU8DHPZtpHSMA7HaFXd4WX7dPZaREJfQ_IPel_-wykofdQ6swwaSoNDRJHeJjTueCDIckROSJs7upBLmf3NNjP3et_D39VF2lTOob9GpSmvZjhozsZlGpe4e5z2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Osg_gF0C7yKFjY2M07v9TpqLXqAvDUspuC9_WGW8xdf0vWau2LkA9Ei-kcJWhM5PjQS_EOLj1b9rkAIqWSSCdCAUqKuZBiBf19jgdLIP86Twsi80kh1yZhzkRnR_S3CxaoumR7q4JUdQyXtI2LFnADRfPx7tisowj1VUHFvFOa3vTo8kT7bujEUKxssLJkWfaOp1zVGls8jD7fREZcedgqeL7XKDl9B--VLfxm8p4ZO8QY6UaY_MUqc7zrsvnxuIglphgRL26qYqOmMINBsIthdvYf5MyzXXQtUeUXakqeiiNl5KmlU2KRoNoSTZtvVwso9NLiH3M_5ebqDtCyxY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/drXLHQvYPWNcUSCMZ4kohEM1z7zj2bH7D39gqygBY3AMWSVVmtODDe6fugk1WFk1OtIz-MFaIiqDMder9cpLG7n8uihB-S9kqCRbHYJ8Yzv3gjrpgpgabP6TFUMpx4Wj0e2Io9SgGBHjU46w5oab0mVsZDYiEfxjydcW-rQ6BVmwT7cd3kMqVjUZPn3mORDx4WBW5An0rQGttCyTt_9bkBKz6G43-rKa1APDDw0_1B_k-Ib0dwoemT_ReG07fQOG0n9zpJicYBIeYtI2Ps9Zvo4xvlas6y9GZVzky7KyEMeFzWj7CUKSavi-i0hA28tGbGLT-eYzVEVPcmd3h9BkBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=QTfFuRSJQU5VCkmlgiC50DZb9ONUcrxXreHeqbbhTbNt1pHtyL7-3ObiB-J2UlZIpKxktuvVKsEV7M5jSw5pdqDF39p7Mo4MqHTHjJoNiO15Dm62talm7rxA9kbdDU20wIrqozmpr2UlFJMzOhlkMufZDRFpE9rxKnL5c2WAz3UL4vTPLFG4jDEI6U29579j54okK9SEQ5CSO8MxfSYY4AFYGodNQIgcqJ2ExNFGtxkDu3E2Dp66MH94DblZoGidyk-WBPz4xG-84HpqLn33a5xCBfjN5XO6BFedKsaSfIer7f9yWoJZbDorp0O4i__sNzqY1iKsc9Ac2AAZSHPa_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=QTfFuRSJQU5VCkmlgiC50DZb9ONUcrxXreHeqbbhTbNt1pHtyL7-3ObiB-J2UlZIpKxktuvVKsEV7M5jSw5pdqDF39p7Mo4MqHTHjJoNiO15Dm62talm7rxA9kbdDU20wIrqozmpr2UlFJMzOhlkMufZDRFpE9rxKnL5c2WAz3UL4vTPLFG4jDEI6U29579j54okK9SEQ5CSO8MxfSYY4AFYGodNQIgcqJ2ExNFGtxkDu3E2Dp66MH94DblZoGidyk-WBPz4xG-84HpqLn33a5xCBfjN5XO6BFedKsaSfIer7f9yWoJZbDorp0O4i__sNzqY1iKsc9Ac2AAZSHPa_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=M0vVvgpE0NPTRzhTOTFZC9FP37oaaH8HU51zCrs60PG09RpMc_miwCTjE2FXRkq0nuJHv4UlM4Id_TgccjMSY74zQWfBdhVUfMgBzv7QDuHhLMI4ol8Ufa3bPPH7ut7zJuNhXdB7OZV5WVGotvFRkQt89I-YhnQHg-NARlpRKKljR5ZOione1sykxdtQfMGuYCiMwum40GBfXgJhhnrxlLQt2JWEAjsIDlqSRhLveBC1N6GKu8NFbtFlteZbWOXqQueOtakBIBpNVIYK6sgWK37YVlLqFT4gy22AqTMGVIhCJnpAiQSUyC2xwKBA-IEiNqaClpV1endnjHDGB1RJKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=M0vVvgpE0NPTRzhTOTFZC9FP37oaaH8HU51zCrs60PG09RpMc_miwCTjE2FXRkq0nuJHv4UlM4Id_TgccjMSY74zQWfBdhVUfMgBzv7QDuHhLMI4ol8Ufa3bPPH7ut7zJuNhXdB7OZV5WVGotvFRkQt89I-YhnQHg-NARlpRKKljR5ZOione1sykxdtQfMGuYCiMwum40GBfXgJhhnrxlLQt2JWEAjsIDlqSRhLveBC1N6GKu8NFbtFlteZbWOXqQueOtakBIBpNVIYK6sgWK37YVlLqFT4gy22AqTMGVIhCJnpAiQSUyC2xwKBA-IEiNqaClpV1endnjHDGB1RJKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw2h5WiiT6jcaiDM_9DMC60XWYSujBePJECIOZg7jQsBhoADvRHiTluxrIYVvGfNaBQktPBCrPr7aCL9VZjqumbT_CTMN5cy95GtgXm7jaEWil1NrwHEwU9olSAHKv_awW04IQ23WXP8o9imGpRFf65g_LZ_TrEh0_0wgDeCEJ8iJhGeY7C0YreK3l7MYDvLcdOSPt5fgXgyexgqnvwr3-tOIJH89QNBRnCcAfDcaWvv8CqB8AJRWImFRez1BTRxIZUEDsvECC9qiRA84BjbQxp-l7IHZe_3WwrYkXpaVl_GqHA21w7jPwLarNf66Sw_OO7UpxIxGgbElvhQ16qJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt5JLU6yTUv3VmI7Efy_CSUbEUb65y_bUEDkCWr95AzRIL-K01PXzi97935lT447S596Y3qNmiNX0sbsde2Vovyq4dHtPPvDMNG_RWGjKtzv_BUfF3PLiReCU_vr-vzHAVk-opwqNWwbKkd30EIfUyem6YhGF4kGzGioPJ83yvSEi1ME4IitkS61wqaMa6PInHS6hrUPwjfpzspNRCWRut3Jah8x7jS6VxUkHynY0LJciThAnOMdiSCwzm_0yfWD4BrX7QPg8kwU4aaDyesoeSmqhW_xtInNEzJ2SuPQoh6qpX1z7g4NDdHfG5qu5txiqrbatYZ0BsEZ_n2CweydRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Dt_2hYkfo64v677C82pJQ7YLFYxoM8frBh5xGGjIdGBGj0RgZqWaOY8EjjGnLJuuaVcf_-VMYU2CiuKULprexa_4PdglLjj67fUUDaijHaDQ2MfFA5-C29Qz6fPeE-1NubHa6vwoiM6kachMqGc2HqmrWaL3a3b-bUdgeHhCEdqWj76ydqkj4H0EXOEtIAEGLsk80xY868a5CsnuMO_vF7MRcGBaSz_dd15aqKUAMawLUWAwvwQwFNQH80rzHAxrVc9sEVfeGECToHTbBMR6hXqIUHW5_KO68x-91llauPptW6q_UPxHk-vpoQ-kVjvaJa1pXfZtqgbSTAPn6DxQhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Dt_2hYkfo64v677C82pJQ7YLFYxoM8frBh5xGGjIdGBGj0RgZqWaOY8EjjGnLJuuaVcf_-VMYU2CiuKULprexa_4PdglLjj67fUUDaijHaDQ2MfFA5-C29Qz6fPeE-1NubHa6vwoiM6kachMqGc2HqmrWaL3a3b-bUdgeHhCEdqWj76ydqkj4H0EXOEtIAEGLsk80xY868a5CsnuMO_vF7MRcGBaSz_dd15aqKUAMawLUWAwvwQwFNQH80rzHAxrVc9sEVfeGECToHTbBMR6hXqIUHW5_KO68x-91llauPptW6q_UPxHk-vpoQ-kVjvaJa1pXfZtqgbSTAPn6DxQhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=dcmZ4jkU_g0M6OLgZ5kE1DokLQ90hGudnhcaEjtH3odRzbVzAeIxGVpRZ9uJiVhvKM7Bhx7pjBki0UJ1aCdP-yiY5U3T5Eb1WWgtQGQcO4jEZ1yBKArUxXD78X8_AzH3KHRAwYPRV7BXzTXD6zQsuy_KrSV_NQ4eTxVwJ7jhbAKiLgyFabMFyi6dzppOhjwuzylQn-zGN-nINnGQdnwJxL8uJHQgG8S4W6AQZl_madixWU7_hF52nH8bU_ck0OfhKDNFzMErzbwH_TkpV_Is3pcmmkh3s6wbAPKXCz8_AynemTgEkdEJt4roZJl7ofv5ty8tWS9nDUr_xhjxEb2YbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=dcmZ4jkU_g0M6OLgZ5kE1DokLQ90hGudnhcaEjtH3odRzbVzAeIxGVpRZ9uJiVhvKM7Bhx7pjBki0UJ1aCdP-yiY5U3T5Eb1WWgtQGQcO4jEZ1yBKArUxXD78X8_AzH3KHRAwYPRV7BXzTXD6zQsuy_KrSV_NQ4eTxVwJ7jhbAKiLgyFabMFyi6dzppOhjwuzylQn-zGN-nINnGQdnwJxL8uJHQgG8S4W6AQZl_madixWU7_hF52nH8bU_ck0OfhKDNFzMErzbwH_TkpV_Is3pcmmkh3s6wbAPKXCz8_AynemTgEkdEJt4roZJl7ofv5ty8tWS9nDUr_xhjxEb2YbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOl8Pnd-v1M2mSn_qQK1EFBvbFPj_JMPQ6OyuIZaVP-rR0Hp-wplu0gL8VVSpCz_75FFC5XnXxok6kkPXgti6_nj8BGp4J6G9NYEXB0CVNdogA8fNcUduemfVnAit9po9k09dqw7CaYOizC2orj8M74GjhIx59uQXY33pnCeESLJ__ZP5zYPi7rHWM2_k2RMsk1L3fOoYkLsxNnL7l1V29l9DJkVW83y9IOYG22_3EKpc7WySfxP_Q3c4luKl-euXvMYzAJVjAnyzfuGiG4K7UpdzBwmQnF2MLspfQt08cFPJvS8Oa5bFGv6pD-FvFWsMBTWqLnFqpPioyy6NrNiew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llaFcmB1aW-3Nm9xcY-PPtWE2HWc42obL2C1dNlp51Nh_FA58kxVhxn9mtFszA_hWf5CU5-bZL9Aszd0CKhnlVv6uzv8_rS9lnXgZWg1id7DQo82MzojBr2rLCaX0bfH0Qj491n0UOlOPoxJCBLKbUzDE4qJcFYCrgFO5e3URaBXncozEh0W7C_3vgIVpG4KHhayZoHcBUkBY2QM6_4tf88HX0qDT8TAq42HQ2pc-jxxLT7ZfitigfBKrJ0r99wx1fSI6EpSniZbRpILe856sv11eCLF4qZBg2LlgfxFlkBs4uaEHQ7xQFz3e40RlhT596U5nG_wXs7QpnYSavE_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6kNBWLymnIYb6wDoaKKkTHbT46UqbiM7Wtm33rcZcfMjXD-1WAElq50qyzP9X_ULC04PvoHooRtJom6L8hvi6KcZ72AipuJWQr-SjXAmezc0cIjbqeLNtfv8Mr5PZhUoUK5QF1uWu-qJr-WznFYjWRJ8Yd98GmaY4v_7vQBgHzaFaDF4shXYQk5qAr4B5mwPFOCYOBLNZVVtlDIz8faE4xrLfYF3pq_wvMt4smuYaE6bQXI8w06-XYmNYvV0ig51-uNC4uRzYyB8s_VvfwUGVm1RvctlGZB7wVJr1eqN4lYE8h-Tv0n1goTUYBXQR0p6tcyuyv_SB-OqEAOFaqwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvxWc5-SI8YTQ0q7L5vud_bIWhXVXLBmmg77jquedLTFSOIYOmhAWwqm8LbjAaP_8NpIAFapMYa2WXoKdKxHlQKeybz9gaEgfLBhIm9rMlvNzCF3YhPTqLrfTi69AlgqycffXuBbtU3B1YltK39mff85nYioLDJ4Ch7SSSnna3Kqk1PskyuMJOH17ffnEnbP_ftZ8zpWFP0KqnaCCkAkTMm0FTOoSjAhLOJCEvJ4qqPu-yrEmCGK4x79UDZu4DujBH2FMnxY5Dp8QI1U5TpcPvYFOTGyQZwA6cmlPTHQiHCp0Pxitt1w0MXq5f-VmFZysYj5PadNY812VdndFP3bjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDDS4XaGHn0712OqUcuNOwdTN-6nprC9Oa7hlEYI9DOl7yavR40aHWvSakj7hKWu1-4v8NBtkUn6moQoGL28cQGGHroOHDloZY6fOCAZFTQAWcR2mEGbi4u_Fsp5ppbgnPNDmugEorx16wlb8tH8aNFCMFWiwynqAsZ4n3JnsYzKAcElWTQkNU2elP9kV7-GtIhG37q20cJScqSTztZiFSXpjg20BktRXRQ0p9IthQNWC0SI2bkbVo_HHcAatix772S0756GhMbI-x_FOBbxNV4aIpnyiLqYYMFOY-Q0Ljf_5x66fx15Xu-1qLqdLL4c7nczNljc2CBLAkJGUt9Y7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_StiGRpJLTHUhFV6k8kvhON3200KEbQ4LbkRPWTA079SiwgeFYsbXAUXI5CYVoXLFnhrAILauJBrhhWSK1e6tMpfNSiyMLuRu0jKHXhQ3btw1OiFvAadyHpJhHPnDEI0iYRdGzZHxnX_310rID5DSf0NZpVWpn7sMys4XEY25CQ6WGaS6jpnyd-1Lt-31DnaNXehnmc6-XTvNsh3GLmFrfzeZkKvyBqfRr8ctQvmsA07YbMwT88QSFUGKr-A53nw-lfr1vnspjJek3hZYJkcQd6MhMC4I3UTHf6fBcEIKcot0CfdomOCzOAlidKncos-9qN37E_T-qLGbLAQW-vZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dA6_XtCy0O8y9dENhQwRDug5AwJ6K-Q95LZNCYgebBy0wQ7cCiRZnZZL16xGZTAkIy_CELNlXKTD91HegItdtzZIrFEpMk4lgOSV0NwdrhQSSgJvWn6Jw1oswbSwZlRiWKmATnijOmN2J4ToH4tz1GLybHHrW4bxIoJ6rg3q24cPdnJeGU7Nal5P-gty7Wo2orcUfO2yhdlI39davwZWQENsYOwe7aKgslzdBp4ghB8vJu94NP0WtQVT_Ah1SpWFMyzpVITd3l8eWvqChMsUgLU2hyb_3tgmdsPe3QhUEk4UpCkIrDkJ-R5s7DtnW-bjH4TLM1Ll1AklHo7961je9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2nnCQqpo0d2KjPyHuRgukomnHZFRxw25s861S66CaIuNqlSvOT_NN38rDbPsBkfnfgW8YF_lLF95WfKb0sEhuW4wNQSq4PBYhcbvTMVlFVBmWudcmPpKcuVpjSxrwrXKMUeXj7wDvsi8otzJLlxWRKVgHTLPDnNgI3M5r3fzOLbbOTYxhxbOgO_CSDUCR4hZCG-JXr-cz64A7In4BgGN4uyjkrkiP0xP7UWDhRLHTSUVDZmsbPmbrBqKmp0cGPtWSofNZtMRmHAzq0fM72f0HapGwy_ycaFymT9_Mwyrp6urX7Z6J2y9-30AEyj31dxZmUXhQ6PkJK7y2ldvGBZvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
