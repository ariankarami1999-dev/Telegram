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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 19:37:34</div>
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
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ_sdZL2628-noW0FD2mYU48mgldBc2IS37VcvyEac1ZcqmTLzL7-7vDbc71QfTWq2LFnva_relaLABuYiHkU6WR7fpl8rOqw0x4ff9KT2H79K56KQ4VWGBvTUsw8GzVUf1KelDFSyfN8ZN3hHla6IJVLHfddl6CvScYf5gOMHx7s_wk6Rwvk-Nc1Sjj1826qSD4rr7A-nJL9jwP0e740HPFaoZO0jfmXHL7DTY7RTiYmjPdAjy3WkR0JrefxM6MJOLZlIL6zgWtw7bX7vUytOtu8eLokyDJyCXxbFR8wfcwOWpn-WuocBBrh7q81KkElOpVOaaj94jXYwrN2PZkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0Zbkwfj_VVRNft6m2I5vtNvWV_JfD1Rp77agvSiugy4LvHYH3fat9MP4bptUCdTYZqchjvslc4vMcXUwNjbiOxfcsT63JVZAkvC5Vrk1zR4c5EW47qEL9EXOx-5Sh3m65xCUqKmgRK6co8huTimliggOo5r9FyNV9midpHdn_dHc0HXSiWy5OTwMNwFX6kBL1G71_l6QlWjil_oMRCnaLhMx7Ba0PviCcuEEIf9uB5BsLF3Do_mlFlFAApHHkaJppQ5RrZ3YSi_LCL8n72I15uM8QpXtOBA0BrGBfTzalXSWrLHPBTJ-DxAt4qw_CvEUXM_hmhVpZ9oaFIbIWV0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuTDziwN04fXK41NIBTUchPlO5gYpc2KrMTUDwD9SuObJlTcCAbiwPqHY5j5Tc37CCw4MqgfEyaPgKJ-y-bvXAG40KcadQQle6KDry1fBbtFftUj0oIPt2DCq001MsVJbbEvIY1UthJqjCuEttvmRS9uV6JlrDg-fH7PKHyz2QmqqCwuaBiNkA25ZrPgiES-DX_9wRpsHEV_m9hTCPq197GzzvLNiQ_OQxsZblzmFR7Uh6r1mjr-z7O6uY3-bLWauq8__Rkq4FnPJ5GBnbeMqrC19kX6Cb4HyRdDYLjM-Suf2zdNHGjn02XI0ZfyEHZtWGKtsD2sTWrIvE6OJq5bcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZyW9lFixriPk_TDV4HZ-GTmp3aMbzg1qi9xGYU2jaoGimsm52HU3QE_YnX6MS3kejmUMHgaBvkpy8i5-WBKuX9Q_0d5lWqMfusKPpbyPEY1r8NKvTRSL2p5EqNkEApMWC5H4Bq15q_86DzaxVar6QCIgvsOAKqM8uJxU4qRsqyGKEaB6wmybW6G27xKxMVikjNmA0riIrt1ONOgTgfyyqhWGCTmDtDOEOeXgkbC7ZWVLthWLdpJuo5I6DfwBuaAa85BPxkVZ56-wpabC_uQZGG6cCbsSv177ZP0M07Hdxpjj4gK6Da7sijDNS5GT_ibH1lpP-YvVMWfP0uLvtMzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srpUwUGEiqptFoKzQNOtT7GSBq0M8qsaPI08FNiLHCEDfHOT3udeF7LzEvE8caogyUZW_PNy7s3ZZg-ZaqKcqmDl6pWVL_Hu3UCdBugdeh4TVQ-CpVyUed-6KtmxNRX_xbLOUaFW2-Mgn7MKX6EXk1C8q-mkB8c7ukVPCwHqheE7rPBJcI08Ov5N1yk-_OFLvXozITHMnNGEJxVjHWbhV5xBVi2ML5U1JDWZKQL_INd-Z2YPVTNs6B9Dn_TsBkyp0rRwju0y-CNuecuH1Z0ZFYE0NR_6_k11ZIh_1PJtyk8zDc0cfXopUwXBdrnfvBHtuMpNsSE-7oDUl-61Veapfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWbhz3gLBdBSk1szOe344XtEiVN_JWcdljpPevjaGtZKyiDsy2uCPuG1URsnsnMFZ-hj2iacFKFs-AwmmwOy0f2PRanjzSe3B1CfW73qrIuqDPkIl4lxUJqfwePDk0mbl8nf8BEvlN7G2VI-JjX-39M6GwtSS6yD_4N9AUprKIFrISgVx-8j7YxIAdFk7eJ8s7pfFtcbEgdHCM4Zi47YzUlkbpW4wjBVYooOztbcTJxIxXRyxLBnrCkehrrvS_lg_gJn7jzExo4hw6zSVS-btsceKSck80d4ygS_3ETVrmbh-Im_mp558Le4AznpkT-sT5WVhKXPz3dl5Z8P0BaBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR4YNPhiMQRdnSAzNF9Amaai9YvEyIPDLZsDICf7vzpFkX2X57jtipUnB4a9fiqHPjjPPkBIpIMUGygn-OLCOUqyrSsQNrbj1warzucQHSzoFotZeNPJdn-eDyJvWyjRsM_QHVfsRxpLAg_iBY64HkXrsKYYekAS0p-uyAeCpjg4dUKtBdq_M052ShLAPDuGo-YXDxOYsCbQmMGNFc3kctpknmjQyKSMiR67pNNVdfIWupaMVw-RK8YGjaRd1cpZ_N0t1rAogztQ0o43FVZ34leBPcEr6Qbkr973oS8EYPmQf2E_TPSUPNE5eEqJSMkS-4oufTG8Rt6OnMozF3x1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBB_NlHTR3YNdWknY_vJ1YZWy1boBzdN723ifC0GDqpiq6Dtpf6ctwRhxDiB8dk5Is_tkHFxjfM0JZi4ng_-PF2j3Yer5GrFOvfXC_spTb9sqBe20qzGWGyJ1hc3IvP5wfQ3XWQ48Cbo97idnR1xvWYQEQJFR9STX4z0BOCoCGq6ZdjjkAnuVTynW5-qShjJWV71Yv6OcykLSLqio3kK5Xh9cjIVnWCaeC2cl9QpNhxgsTCKMJ2-oEXke0yExE771qOg8G5iFU3yhqNQY-1ybz8Ez0yv6lWr7eP7EU37ZCwXaAcKSRoK2Njneqk0oiB7qqCYRrNQYJhR-lmW8f8nnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2p1Oi7pYTDsZ4gV8VP9ReEE4774n02xuz6nXIMJg3PAQ5VtFeUAzMUVUBFcO2XB_ZeILgGRSPcv65BFwc0dEpuA3STSMJsX1DJoIoeuhh7y4T-y4vuS87ACM_iZl38GmIzC6DEVBrWto76tZQhG_Lnh0VLD9hJiXrDJV40Ozn9csOLBt2rJVxswix2R8fa9ehjUT_FxWb2jaa-JlLrSg_Adb-FH74pVR9ov11TxB-rkvlKV1gfjkG_DOJ2XKcZdv-DRi1gfBuEzzJJzmGu4CB0ms-Wg4v7uGUmIw5I1kjuYlazobnSZVEV9-t1zRssZcKA_zGkswvBsSW6frK2Iag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WviFigk2hSciDxGfS9_7T8HZRh1DwWRJciN9VYQmLR8YOBQMD2Jptx4Y5ufs1CehnOKZos8rz3lhXSmGCoX6IaveLyHB4KgIcPcvlwMpC_Osq-TXRDmJAdhMjChP9JMyGImufovgIXBlXZmwstfxFDKx0bFusWHyAuqUHluoSxIFUyeuLrP1CxrqEPDVlRwhr4466ukUeh4BbThIkTcOAWbecnIWTzsTFTNfyfZ5IKzuJkS9PWdTSrenwcYaSTmw7umTB7rLmCoNkhhlfZt4WqizKsacMVolSU6YRC0o0Zxj8UF9qOBxC-vZ4RXN5wbdEpr7aEPr8CRPiNQOkFOb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrbeMTqsyJ63zzjTPBbGDp83rJ8rWi31pZB1d0wAXvbgzywzAI1hOv5XzuGwYElFFn6LRzkENjRxyVvODsroAaAITfogZoKf8o6O7uughPwNttSSEQNR3QfG1Cqniai2p69T3danRL7U3qabb2wRGJoqPAay8M4fLsWqJS4gJYa-4LYfaCbX0S-PW79WHuT4smSLdyZB-88oWdHFsgr24WvzOIYzag_LG9R_d5yY6-9APWrO5SH7uhEtZh1EqRQuA8kyJlexrMDFL3cEJPIVRT_DhprJb2u0yE4ouuMsTzymKbWrApaJjLBg1DkXzZD0F3uHJPv_wVPvf19IutaTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olMCzcrcU-87zjUJRoesjXSNuySLfRAJ-WHCEE2fqU0Gp-f_OgvUYYxvAcv-ew8EYCL44j5-fBJVXeSOAFMLJIiYom89ipfT4CgTHO8oFxkMRFBZ4SRSdb5LDECXteohKnlTomAKQHf6ey952GND6KWE7LCfZqL44oi4VEkwdUU9YKU5tdFH1HoZdhv4uLQDYkquoR5ylZ633mDHmKCc4dyrsWJBpeHgSbinOFM3JkGsygbDaY_t4l494foHJTlfBFfsPKkhi4PnP9IRlZmZ-BSCu2b4DW-uhqPsfTX22xt5nSFSfXP4Zsd3Z6HHbBz8qXZ9-11_4CJDrVLoT4lgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpyQJrhqqPJN5kbEuhwjAUceRUS1XzxuEIqP7Sd77G3j0K3hgqIdqV6rc4M_izPpQiLmiySLjw5XjqBMUlE1VGcv2xYwnojk0vbOjv88135bKEsWmMPUR8RjHBxBf95UpGAgM3DTHQ-8ay_T5Te5m0XaVY2Yl8DIDZ7tzZSoyEZ448exo7F3ER-nPAr_FZJgp8-mN-0FMVotiSveLKkETDvdSxGk1NQ3vaBsR9uvy2XQf8q_vGlkA1hqxOZFWg5hoZXH2JgUjb-MkV7FsADJ44SCv6jHVKrJwOEIDBOM2nT7oNXQtB3-pkW19UnVqh5w-mdgiTh6Ub0NQKJdocHLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsXC34HRvpKucJw9rYnStlgz8w68oVHlRfgusbYRZ6SY8zCdFOiSg18Yf9bh3H7J07CNnf-2zuaTuCtfnF8zgBkgxFAjOALHCSb1VqU4tIzLZgLyXT4vwMcBl1s34fzF4F4GJ5EoyuaveFvnypD-zmDjHHz-p-rBKhafyDc_7FGZdhAytzXMPGjOHlbfrWjSY1EETwJVCATwQpOhAfgKd1K1-MimM-_mpncFjATWf8Fez0UdXn6GtvmTgU0jVM2PpHx2H4d1-nfsE54VpeaYalOxgTgfirjMrFF_P4MDdLn9pIBptmvCMGMvFCcihybHmucCnXv8ZJsryhrTagdZcQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=Vdf5iz9DFAHPloB3EWby1MRfR0LVEgvCxQwR7kCDVJx5uIKnKC23OBE6kzXJjm9iWUPpF7pf3TgNJODsoJn1AotDOgRBxT2elUNhpJFXVYpymuTi9kuA4n0IGgW1xbeNd6Uy2-bXjL7NsC11z69Wjf1cRBAAbDD63DhI-QyPPDKq7D7ZUD5g6SARLe2aGXqzX_F8C0plS9dIocLqQmfWZBmKcyXZ-HQlZWhDyIkgmftVxE8UTdqmKqbyZVJ0soZOUGAOyn9g6U-Rn-bnXYkHadboBIuUUtOEJLWVRuHgajOkxrA_i67C0S0RIgf0N3wd5PKg2-ee5_RcVa7SOPKa0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=Vdf5iz9DFAHPloB3EWby1MRfR0LVEgvCxQwR7kCDVJx5uIKnKC23OBE6kzXJjm9iWUPpF7pf3TgNJODsoJn1AotDOgRBxT2elUNhpJFXVYpymuTi9kuA4n0IGgW1xbeNd6Uy2-bXjL7NsC11z69Wjf1cRBAAbDD63DhI-QyPPDKq7D7ZUD5g6SARLe2aGXqzX_F8C0plS9dIocLqQmfWZBmKcyXZ-HQlZWhDyIkgmftVxE8UTdqmKqbyZVJ0soZOUGAOyn9g6U-Rn-bnXYkHadboBIuUUtOEJLWVRuHgajOkxrA_i67C0S0RIgf0N3wd5PKg2-ee5_RcVa7SOPKa0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3qzZWU138oRNiHSneqHurigHwhTgnzMZvBh_4kon7zhUvdDgGHZWrlzJNdO0FAiiQrJumN0-Pc0rUNXGfWpli1jDaGCLHJs5BBNuacWIYvvauH2Yp_Iknr3AfN15rMnd7MicoseLrZwbYFLf4dSVhgYZkanVRp32QXNbH8onLEel4FgIqA9T1rmZqxnfQAXttFbvXvqL3wv93_Jjw9T5ilxIOLQlD73StehTSrIARUE5o_xfhbxgBEubCAK2jS2976eUioBewZH2awPjEbQNSvjPpY3e5yffWdcEtzH6gL8fRepEaNDxW-HqByb7AIbAGIjGwKe3xL27o0fvnExjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTFJ71Rg0FULh5n0o-xjoir1rPYj6j6g4Y-zv1Y02x8P-DrNMJuI2dBg7lnsDnVDi223ASepoLZrsKewWUO7CZyDJqLvuOecGuiUZ-7KH4OgS3BfjeoASz8wgewZQXus1Rxy_ZPSNVIJLa0gOv-HrQMyLKpy-hXIWe1A-hYp1Q1b69lAzZQJRY8GF9EAD3CTv0bxocja_-nh1p5FOdZvUZaxk3RPHmuSnbi74gzTvoMOKLFWZsk_7olqPz0kujzsRcN_FI0MOlEWGORKnO-5ajWoLeCs7tiB1MLz76xinrzD7D2p-8yevdHpKwTrkFvQCLc-ZDjD_vY7tvDF62-4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZwUHpsAeV-E6xqFCwt9VuADr2jsC1GiZk7nm6MjsrCj94Mpc5lzbgK0RX-RUsZow2xuaNNEslKPvLBSqVRYyM19y7b8Gq5AP8QoK-HfFReR_hfxp3UhkceCfrk5a7R1Zhc-kJPqtdOmOgR9FxMQ3UAasj9Bm6ZiEhklNbIFY5Ia-CSHTE2hLQRzvofGX5oQRU2UO24MlZX0ttsXOpN4YPNKW6WiA4AjTksbmDZv7u42T8bLt_faWOkafxwzP6OS5A3wJzuoGV5g6ijXyWScGkRQdpm7H5TuaGRpMzMBP-bu5hh468n_vke5LOkDsOTdux0M-dAhNT-uPfQ8iPWv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPI5mpb3SvvslZV7oqiBYcNNNxLRJ4remaHN_9grGgbOqYZfAZTCQzprN-Q5pmD1DH-8L15LvKs7uQcVOuJVSLgPy45FRMe2T-bNPKSwcN_QRbRgrb38IjuHp6b83Qfs2Tr0LrYcJeDzcomvwZ0i3qGD0V_EmnL1sF0cR85bn6aWxQV5kqcCEW33JSo6ixQpurRg3LEH3g2UMVxIrTKr6z0AN61xYKcmYA4yN9mmOgXDb_NansrXqLGF0ehir8xSeK5Knp2-dqFCq6H4vwllpIfR8axuw1mhxOh90G04Ljmo64S06eJGEc5juxcJDUFCmnQ5YNy8eZlqdY_nU0Xubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkJbfacdqp81Gxf4mfMCfNZYyG_RUO-RGKuy_xB8B0aw0Va2cG3lvGmv9-QwZpxJfEvukQ-wWAPfZfWunc9U-45GiC3OY8HPnIYQ6bkdZ6OzlXu80Nu3uL7dRPklFcVOQdHYjgaJ0s8UXbHnYYraUg41GSsr6GkajzEAD3eI6xfpXSTZQM8Yzsgr5DEItAhFdPDR8geuZzQwOeXrM29QTxKqrQ2Ii5ZEGTmP4JFqZgdwerzTmXe6kTB_iaMNfMBj-rcKYUTccrWifhFGaWkFM0v8tPnfPPreIFosZE8tEYIido24CSLN_iS3Tdqzsmu5FHFmC4Ft_d4JTjfqeHr9Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUcy7bxw7HipJlUKgIOyhvnnnIlepNLW6vInnJVzs1Eo3rA46eekYjQGvM7vlUVxDjcoOXxksllzZZF_Nmvz3KrkSV2B2fuCayrofTygWLRhuFEvUDWLNsOMQH1-VK6q5GDSmkBuHV77U_qmGbp2KlkRNblOSUX_yikQIBUouamEeCR9p5TjI7bc_nW89S2dgfYYXTZaYKrPXyZA7kwydWGDugCslcw9Nf4ZzDuP9CCLnpVxM1iw6ARBde2L-ckrOQUIp9DSmTGkLneakWgYXZxy2AQxF4rkH9HzModQKdkw-KTTZ3lCqYfDxEFEuNJmYsfhgxmoDdrxEoNSMPpDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lykXTRtq_ORyA_H2Ly1wBzTK1iPvKR-uW0_myD0Ik-b-W9oOZHRzA9M1p0LDT-H1EVGkhhPkkILKz2TKXewQEiO1sILwabtlMFKmHFRXt_GT8KmXWcZe_uQEst4x3l0Be_AmPWIPzqheJz3ZWpNzxUA-D_g34ouMDZ_q7ZzKEkNg_0eMYjD14GYmCULWWzBctFGl_rKP09wAii6Sre4e9Xzy74_Cw0KhBvlRFN0LL5H5ch-Rozhq7DmNC0NsUhxUX4DJ1Y6X_Ydad9R8OeaUy5YHscnrfje3jtjLTfg6XC7KZ9A0NdswdIlW5p76O8DDxEDvX7OAEq_oLRG9nQeoxg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=VBKnlmj2I7HArrwqbiGsNzPJK6oAkaluZ5gKLcdrRL3UENMNQ-eYUC8lBN8dUT1c3yAmoMrbIsjTZkheommzaEBZS1ewiGI61A9QneS67BCr0SbwXBZfEAmlJAhvNhX1NmqMERQpM-JrpEK1wwjB6Ga-zy2K7wkKSjh7-q8DHkWPh0xt9_qLHWXELHogPeAL1XXjqwOFnUz_AEjHLcea677UWK4iD8QV4IAC-4eXZeW_Eq1LnQlk-lZgXCF3xEMcE7T6GgDA8gi1Jy1UevWKeAPdiLVbJLusOh-tgf9e1r3efBuc_Dxn8tnP6MmLD31qlPxKKRxpJDtFOcTOxMorDIqs_FHkJM_jmkpLSCgrBWFMcz_ILeL20a1YiBcVBXMOAs_7D7C1A9OY79qQ5EUqqhthdjZ9sT--xbcGCfbR4g45inX5yS3Fu_FcYjMrktwyzmyw2gq97D74wKXQtWj0JqMku9yftbobDRbV4hJBz1Nis-3J3nXEaPOFW7fhUXYeDWT0ZN7yCe_CLvY62C34L_EKNOXjKN3OZd-clFRpxdAd00v5acD9374Sx8zYG2iB8XEXPWiQPxRqReqi-6frxwxZvB9wRiwqjH9W3QS8ZIyx32r-tYwJ76ymSR8EQ2bqCtUA1l-DlrIyWVGR9KHo8SE3VV02uE9v18A8sPPvRE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=VBKnlmj2I7HArrwqbiGsNzPJK6oAkaluZ5gKLcdrRL3UENMNQ-eYUC8lBN8dUT1c3yAmoMrbIsjTZkheommzaEBZS1ewiGI61A9QneS67BCr0SbwXBZfEAmlJAhvNhX1NmqMERQpM-JrpEK1wwjB6Ga-zy2K7wkKSjh7-q8DHkWPh0xt9_qLHWXELHogPeAL1XXjqwOFnUz_AEjHLcea677UWK4iD8QV4IAC-4eXZeW_Eq1LnQlk-lZgXCF3xEMcE7T6GgDA8gi1Jy1UevWKeAPdiLVbJLusOh-tgf9e1r3efBuc_Dxn8tnP6MmLD31qlPxKKRxpJDtFOcTOxMorDIqs_FHkJM_jmkpLSCgrBWFMcz_ILeL20a1YiBcVBXMOAs_7D7C1A9OY79qQ5EUqqhthdjZ9sT--xbcGCfbR4g45inX5yS3Fu_FcYjMrktwyzmyw2gq97D74wKXQtWj0JqMku9yftbobDRbV4hJBz1Nis-3J3nXEaPOFW7fhUXYeDWT0ZN7yCe_CLvY62C34L_EKNOXjKN3OZd-clFRpxdAd00v5acD9374Sx8zYG2iB8XEXPWiQPxRqReqi-6frxwxZvB9wRiwqjH9W3QS8ZIyx32r-tYwJ76ymSR8EQ2bqCtUA1l-DlrIyWVGR9KHo8SE3VV02uE9v18A8sPPvRE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=PdjQze8x1eG7zU7HlvNyIJ4rGMRjZEKVCHBu0BIL8RhkeJGcnESIphaH5hE-XlRcbcmGtXq23vTxfIo4neB6Ibw2Dwa-GphAdO2FcnN11Ov4xFZ8kESzBhQz-XwReD_gcxTmA5guY7bZb9GIc9iNrh9DTHEbHxY9qCQUiXS4f7au0R-8eTZsaJ8rRcaK7kKaaai5TGO-Y48oRjVzjkcxrHs5w8dQIx4BFIc5QOfxpOanF9cDzupFLKOOE-DWi-GCw6Y8W8wa0j0A4YSMof5dieWO856IIJFpdW5-m403nkl9lm-RsRw4qVPodne3EDa1rnoXjdiRLdwxfUkYRTh9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=PdjQze8x1eG7zU7HlvNyIJ4rGMRjZEKVCHBu0BIL8RhkeJGcnESIphaH5hE-XlRcbcmGtXq23vTxfIo4neB6Ibw2Dwa-GphAdO2FcnN11Ov4xFZ8kESzBhQz-XwReD_gcxTmA5guY7bZb9GIc9iNrh9DTHEbHxY9qCQUiXS4f7au0R-8eTZsaJ8rRcaK7kKaaai5TGO-Y48oRjVzjkcxrHs5w8dQIx4BFIc5QOfxpOanF9cDzupFLKOOE-DWi-GCw6Y8W8wa0j0A4YSMof5dieWO856IIJFpdW5-m403nkl9lm-RsRw4qVPodne3EDa1rnoXjdiRLdwxfUkYRTh9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smTRXV0AnbYiRzwsT5zPyEgkMkfLCYvxd4vUH0ppsZiFD3cZLKXUieN4Djtcjt9wj7YNYQeKsY0Wai3YmXBTkn7BIeSp8yKFFavjiSZHNUGFOvQ9qLFxVpgPna2ogxiRogx3t9xnwN0URfLVTYBmsfsBqSRarqNZlh6B2HA_nsXBJig-lzPU-sAhPe8DEO8xrb53ikFvmAl27ocrGkOmNnCv_ZTg1mTCs1M8XC7fgOhjAsGRp0PafxP_RJ6KFr70-jG98YtkFyAIq-28Ll5B6MyLDrcTlnQxf6etJXZv9uB7sGFGssIENGqTOlbSbEurUMOArXhrM-IdOHk8A_aFMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnZ1U9pn9QtLC6-BJXkkffbZscMkw1-2e89W97EwkKbsdY1kVyU2_cUbgUMRR8EXPbSnS3yMdYC3VR5HKxPDDrk9962fF4GrtukXSyG9KdB-rcCzwbvGr4O9esNE89ef95u9C3iJDdz7V8tzAT1cZB6ksb0MjsDPTDoOBYQ-IcAi4rMHClu3xCmtEzVBYkJjYkFWGd_PWUbN3-FSOHmdvv9XPZBjm0JqkMCV5AkU4kSNJ_FHNufmbijGoPp29h80FZ2d8fLsjc7154Z7qCW6HpUX02kmZmAb_xxn5BeAwB9h6Bh4AOXrIVQJVcb9R_aWVu9FFw9rUGT2PaNuRg3r0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=vaRdJDJMG-fl_TDLTcLzJae3Tv-O4M1EN-VZN1z7UIqj-XcoqHrYyM1-yZjzBcYpYOZ2R5zbuPQxfhPF7K6gDzd9z6Bc7aMXu6FeHdmEIyaarFau_aiJCL6GCEqne430MB1pT8mpLl6aXp5zTjLy7lnK4Ye2eDkwNmN2XRmG9vhs509gHWMGl6S_dfSb7bfKj6QglOHId7kye4hMvVZA1vrcKC7fHQLuSjeKmDcV_dae2rumJnK2bKxPBi-3XInGiMoss13eGpdBLpGCZWAgbTtKNpzctkDQFl_Y28tS7bOIYhruHKCvUGLCDSVe9cj-GpMOs_INrvbZQiy6hT-FZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=vaRdJDJMG-fl_TDLTcLzJae3Tv-O4M1EN-VZN1z7UIqj-XcoqHrYyM1-yZjzBcYpYOZ2R5zbuPQxfhPF7K6gDzd9z6Bc7aMXu6FeHdmEIyaarFau_aiJCL6GCEqne430MB1pT8mpLl6aXp5zTjLy7lnK4Ye2eDkwNmN2XRmG9vhs509gHWMGl6S_dfSb7bfKj6QglOHId7kye4hMvVZA1vrcKC7fHQLuSjeKmDcV_dae2rumJnK2bKxPBi-3XInGiMoss13eGpdBLpGCZWAgbTtKNpzctkDQFl_Y28tS7bOIYhruHKCvUGLCDSVe9cj-GpMOs_INrvbZQiy6hT-FZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phzrdDfO8lSCMB7y-k7gLvux8QvYFVjFVGsy3YDFAjW8lYhHfP7KhpKm452on741gVFkj7WsutBFoz6OFP_ijYCpTp6vgjfcAf2aPElips8GcmlUC5sJVYlQEomk9djfcCO4vo0XYIzSYQ758m-7RhuA7IC2J3qw5xloqSE42YT3juYcqCG3EDyMGlMqRBbqGkM71l-m8ov6oq-q99eQV7KcMg6Brh7hASKn3UOR0T9H6KJfBWdYnm6grsAX0UzwDiG3nAw_dtYu0LxFyWbhYqWcTCpjN5EjVtliPstU1WDeKgcViW_nXS-vF999yt-uMHf7AjwlIATjBq4_JR3iPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw9tguTAF3va-g5fDgSR9UXtGT2QPM-d_ZNA9lkSwiQVq8I-y39KCQWV-3ByavI8E8BHelZLbKJad8WcsWdkqFJsUIM9X3AWbHPlpGCpMBHrfoR6jXVBzeqzpUCSLa_eTGET1WQ7fRWQMzg4HOGZWOBeteeKyALntBYbUBWG9gnDsz4NeAtaC-YkwY7eS0g8gjL0LkyzLp2pNUPRKq1Ou9EQqqhYVuHKMZGrDkFUaptPFSF1JIB1q1PkGvOhCie31E-muTDczvu6dY5uM3bomq5uY3Ah7cpj2ED5KdNgUWaeOO5DuXhg5ginkWVuHz1oZzLTBnwLcz99pQRLq9syLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf27W4d-5dHFrLP4y5eRLcGs6tfC9W2WwFkKme_IH_WwzOY0evMPlsGt6pONteDSJejwMbur9Sea80QLaHT23DfTGMuE7XRIloeu9UCOVMzl_86J3qakijnKI-cBXvNS8diS-3v9jQKxU5SRJd-su8kXUuBJqgCplTy6hBnjLpJn06q9k-0rqYvhjYJqenL8oOmVEmEfdWWkJhZ3mZr0IUXqnDB3knrPo56bKtxLW23peL0oerGn7BCf0Klt-ITARp0laxRpoCtRfAe2q-mcOwzxL72Br2Z8YQ9PqgiBr0j0LXkDpt2NNNFEeJ5cghRLJQY1x1fnFUK_h00ifN4Xjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg-dlCLHNQP9LgTIxc_ss-8ivsIkdHWSRIRp5VqPWjz6hrDLOeJwkp8d-vHsqnQzpFgAbjgIQa76waY-mh1Jt12ZqWe8IwkNvouMflgOIiqHL28RQBlQp9LbkREgf-Sqe_prJoOICqvrBMbMJKlLw5wYhbKxWUWA4yJXB-fTRw7mCPPSxMvWbkaqHVrnX406Drqiys0sOMT65Gg9yM_suyCouvfrgnW21lKsHgf7R50oAVLqXw3CE8ze0jC7ueTP2F653eoU2oQPeno0WMKCNtX2IniztbVfDwXwryAxtsn1JOzSWkhEpwSb_A48tEScrQ7qsu0UwxKr4dFjrwH53Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sebOGos7xLbKecClAzZC_kEbuB8W7FLugQ_C90QoITY2vqJQGBeQHO7XqX9P7jeisSrBIyutHlqpqtVrbkZKDTJFE2qgzeE-EC52Xu-RVK1AOU3eEcfujX9XMMuY2gabsGJqA1G_32QQ_iCckh35mflb767i_8mxiugDyl04s1Za_4-N5xpL8VYZor_XE3WchrTXavUn3cwM6j_ehCBMiw79il-mQ7yIx_X0ZhkSe7UJJ20hpK7xj3QnV5IO1lwaB6oo1cOZEVlt_WFrJ1Jy7cJgJkgn4MqQtd3kr2K32MpvOloWphoSbxjOtTQWSiEITCIpQDeUY9Ez-F78tpe0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5a788xLdwgLInrjd7mGE3FBYEd0IkZivGZPOynGG9RassjP2Ggy6CpETIFNRLd8qip-OXdRNJKfTd9IHiDeqMvC3yo3hu4q_skeAFi1MC8AzhHPR0KvwwHZcUNaYvun0PvtnBc2EqWlPRExWz6M1qsE-9JZD919RB-MDOCQTrEGw20NynKtrYb5M43_en51w5zR8x3EaH4Iz-7rScENHcidRz1y1hrtH75rAcR_ebt9v-TqUq4Sn0logGOdar4SFhzX7aTIaaDKFi8P-dFimoFiaIvmhUnc1tGEbRcrNdJLZqLigahzjRVXVUBy4216V80g-AsrjLYdcSd6AChYu-5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5a788xLdwgLInrjd7mGE3FBYEd0IkZivGZPOynGG9RassjP2Ggy6CpETIFNRLd8qip-OXdRNJKfTd9IHiDeqMvC3yo3hu4q_skeAFi1MC8AzhHPR0KvwwHZcUNaYvun0PvtnBc2EqWlPRExWz6M1qsE-9JZD919RB-MDOCQTrEGw20NynKtrYb5M43_en51w5zR8x3EaH4Iz-7rScENHcidRz1y1hrtH75rAcR_ebt9v-TqUq4Sn0logGOdar4SFhzX7aTIaaDKFi8P-dFimoFiaIvmhUnc1tGEbRcrNdJLZqLigahzjRVXVUBy4216V80g-AsrjLYdcSd6AChYu-5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf63ju6LfrSxy73Vaq4ggMuhd9TARA-ezWZzYfMZNXgW30VQEg1z2cRifuzgTxoxRE7i7eXEjlxo0nwZY3O3JKbOkGT1e7dcTcRAstrlgPv-0VYrb_FdX2HzGin0wmPkAv8rj4MoUXnTu5gnGlvDst3TwhoXo0KnvwqPAZMx37B1T-7aKmXUns4FO6SvpyzyJAOgVfS3BFAyqFVyWsAHlN_VWUOS9pwnNooORF3PaUMqegIrDCMdZpXhXH4Gy5GTJkmQHpdf4-ZmuVHJLDrJ5P9duY1lTRQ3lOjB42QL8RbMDAFQS9MyEZlp0p51C5BOcMOftSriJ3Fem33z9ULMqx-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf63ju6LfrSxy73Vaq4ggMuhd9TARA-ezWZzYfMZNXgW30VQEg1z2cRifuzgTxoxRE7i7eXEjlxo0nwZY3O3JKbOkGT1e7dcTcRAstrlgPv-0VYrb_FdX2HzGin0wmPkAv8rj4MoUXnTu5gnGlvDst3TwhoXo0KnvwqPAZMx37B1T-7aKmXUns4FO6SvpyzyJAOgVfS3BFAyqFVyWsAHlN_VWUOS9pwnNooORF3PaUMqegIrDCMdZpXhXH4Gy5GTJkmQHpdf4-ZmuVHJLDrJ5P9duY1lTRQ3lOjB42QL8RbMDAFQS9MyEZlp0p51C5BOcMOftSriJ3Fem33z9ULMqx-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=MGiEfqyibXH74OadrB2MVyBLI8FQuo-u_61Y4tjqxfTUOWzkx5aRRYido6H3AD-sF3UfWHFLcZQCJtkkWa5Te8mHMdiVNEgfBV-IGbEtbo66DWsQVeoLH_X0yedQVVWlzP2aLTSjXbkyY2yyd_QH53Q-rtc0nzgzpfA-KvNFuYG4qRreLSvp_LHhw78jsincytbX9iK0nH1WkOPEwko9r9tLq6Ey08uqcL06BEUpKXumWgHZGoL-RY1Zjf6AVLFaVpPtrc8sohCqmysl9KfhJqx_rtfMjGmwGmo2pNMnG6pFxj4kVaDydqYypbCcF5i0H0lA9JJWmSWHXg8TzC4VwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=MGiEfqyibXH74OadrB2MVyBLI8FQuo-u_61Y4tjqxfTUOWzkx5aRRYido6H3AD-sF3UfWHFLcZQCJtkkWa5Te8mHMdiVNEgfBV-IGbEtbo66DWsQVeoLH_X0yedQVVWlzP2aLTSjXbkyY2yyd_QH53Q-rtc0nzgzpfA-KvNFuYG4qRreLSvp_LHhw78jsincytbX9iK0nH1WkOPEwko9r9tLq6Ey08uqcL06BEUpKXumWgHZGoL-RY1Zjf6AVLFaVpPtrc8sohCqmysl9KfhJqx_rtfMjGmwGmo2pNMnG6pFxj4kVaDydqYypbCcF5i0H0lA9JJWmSWHXg8TzC4VwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8jOTDJHlcqO4Vh2kNRmh5I-aQof5hG8DIi__BavFcAyB_2k41uSUc8RYdxVLxsY4J7zbmFJ-HePQy4kQTcg_hUwmFXBBIvCpEshYH2h6ARwGWLKTysUVdK082Ek3WZ2ttgq0QLQP0qHZPqDqvyOq4DsSS5neH9jroL054jEbPlStKAYVRIj63PuTfQLX7IXO8SfFLIQjKGyvmHZKnfynMYE2MCBrYNnQYx6s_zdG1KpMjDC3A1LIQgHJv4GB6AO3-jigW3gUZV_yyhs8l-Uyp5iDp3KLuU4Zcq7cFIc1r8QgZtQJ0xMZOnpfw086l_m-l6laKacrhRKdiJdk4-LiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTZkyKmIl6EJF3LA7lOEgixV78DJ2mPRXZYGsRokOzjTGX_JCi7jaaBSADu6m5WNMnn1BjQc8xKH__DzR3hSnlt6ba9cXXPdTnIh-h9XyxDC56hmOM6LroO8KPLsDSGAytSypimoMHJSwxUwfV8rgjnpdY7QwZUXUUDyzhQNz8WiCeYW76IOdn9vrWVPMNL1EJjCvn0ADy8PjmntgML_JradVaoHw-G_dITW1HXSu8FGW86xnGFOyCTbkyZsUtsODz-7F018K3-gNcK7N3uQt4A32xFmRfUpw5-bSOzbKWbSFMsonCwkQVqNmAOYhsMBqGu9YrRPmxaBiv12ftHG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=C7WEsl2Dc4qZaQ7PNGIz79Y--Q_VCNcBb_yp7WEnj3r-dNEPU9mY6ePNiYuN8p4x2cEXErSQYrP7cEXASYtFjXUw9sdKpPXCTCXZ8hzgM-QfH9FcSWz_XLOXyzRgcGnCgvNuLPSFIDzBPuDqYqEg4M31bL2KxQ1hjkPJR_QEhssB3WpfOFWeSiEekSzjyVw3jfhzlmPx6SxduUgV500jWQWvfG0INEQyC7Hav8435IzMGhkc60soZS8csCk4R5IaX99QRTqgZ7AClGly_m0iE8eOICwkSjxexB4ns_RAHcuEAr1NCdaqsNrVDhlgOhDtd1DvX4Sbije9mcShyeq_k4MEoiGd2lM2vkTcVcMqECu2HJ9L3KLxuMLSsmU_Ub3LA5UG5GGmFQ2wEQCfCYNRxKTGZ3v-Xz7HEc9m0fIsY9bmmboV4stLzPi0A4GFQAqRLCXZD5ItALy1HfoqemqRu_pkxQx75zuxeyQrJBRxyU8uGIeDNUYU0LQhuF0vX2GhSersadd5x6LsBUp041bVobNUNM-cm3phIPXTODopQz2PFyjttYqLVzy0zjLcJ1qihQ8gKFjA1YfDKH1t2fsGf-3QAMjPXTZxPiYU0gxXylnjUi4NSoUgDU9VM3_W5GaWpA4CAgIAZORySYmaZjRicUkvIr8Jv0VIc5YZDY6l2Ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=C7WEsl2Dc4qZaQ7PNGIz79Y--Q_VCNcBb_yp7WEnj3r-dNEPU9mY6ePNiYuN8p4x2cEXErSQYrP7cEXASYtFjXUw9sdKpPXCTCXZ8hzgM-QfH9FcSWz_XLOXyzRgcGnCgvNuLPSFIDzBPuDqYqEg4M31bL2KxQ1hjkPJR_QEhssB3WpfOFWeSiEekSzjyVw3jfhzlmPx6SxduUgV500jWQWvfG0INEQyC7Hav8435IzMGhkc60soZS8csCk4R5IaX99QRTqgZ7AClGly_m0iE8eOICwkSjxexB4ns_RAHcuEAr1NCdaqsNrVDhlgOhDtd1DvX4Sbije9mcShyeq_k4MEoiGd2lM2vkTcVcMqECu2HJ9L3KLxuMLSsmU_Ub3LA5UG5GGmFQ2wEQCfCYNRxKTGZ3v-Xz7HEc9m0fIsY9bmmboV4stLzPi0A4GFQAqRLCXZD5ItALy1HfoqemqRu_pkxQx75zuxeyQrJBRxyU8uGIeDNUYU0LQhuF0vX2GhSersadd5x6LsBUp041bVobNUNM-cm3phIPXTODopQz2PFyjttYqLVzy0zjLcJ1qihQ8gKFjA1YfDKH1t2fsGf-3QAMjPXTZxPiYU0gxXylnjUi4NSoUgDU9VM3_W5GaWpA4CAgIAZORySYmaZjRicUkvIr8Jv0VIc5YZDY6l2Ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=fXagjlqAKq6H9esCLojnPCyQ2r6nipjEFW0TvDjmYno7Zfb1CaT5YsemnHKaOTA4ht02iHiuGTsLN6uyn645zW8V2kP6XqYAyLeUoA5pjwGAysw-6MDkVL635iJFOTTmQyLn0yFChcKysy1OPcg0hQ-E0NAL-Yvjq7pbESYMv-38aeWzX1gbZLBYhRcvpP7oJiK9RmWu0SNii-cnt2uuCCldoJ-6tO1_56XR2JPkYTNwzTheIEmQUosZtEiPpky4n-UU3DSCEoyBTQm-wMlRUFQ3_Vu4sYAdmKY_WKjcOCQYYzip9RnIpliNVovGVXqrF_LvNI8XWRc12sx6UzdVxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=fXagjlqAKq6H9esCLojnPCyQ2r6nipjEFW0TvDjmYno7Zfb1CaT5YsemnHKaOTA4ht02iHiuGTsLN6uyn645zW8V2kP6XqYAyLeUoA5pjwGAysw-6MDkVL635iJFOTTmQyLn0yFChcKysy1OPcg0hQ-E0NAL-Yvjq7pbESYMv-38aeWzX1gbZLBYhRcvpP7oJiK9RmWu0SNii-cnt2uuCCldoJ-6tO1_56XR2JPkYTNwzTheIEmQUosZtEiPpky4n-UU3DSCEoyBTQm-wMlRUFQ3_Vu4sYAdmKY_WKjcOCQYYzip9RnIpliNVovGVXqrF_LvNI8XWRc12sx6UzdVxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwpL9n2TK7xMPC3sj4eomEAXCRz06wCaPBjVKmtANZ1IIy-jc-tT6wXV3N74JZ51CL8Je_lTD6ZV_eRDYVQM7P96HhxJS-iwmAlQQmLjJ9R5k-zKM7niIFhPR163XOejJoKPUDIP_r5_WegIYSvf_NAwelEUa36KDEyLz0jHQGE_gqAiVvfT2yvJJUHCJ1XqkKsAh_rilAaItQE3KKuAayJwT3pghhnDhx1G6UNhUb7Z36CDFnh_7jTfxEqXmMNdvitiLEzB40AQUujE7ila8ge7BFiMCOTY6JWTA1NdxOZI_QdMleZNcM_-R81lvV2TBr-LOuwQPPLKwm3kIwdkjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKxHVDG_t4MBKsCmzAsd4VUnT_PuMNsTvHQZkMzTJ0un3mzGOkO2nflQbHBFZluzw_2zkd4THGXhuziQVi1n294NV1gn6xJRlvvOuvxaP8ohW3eeabUv0CsWIFNvcuJJtI5wdd0IwH2UIWawJjixb0RyRQId8_SP0t5pwdgQCq_8gQfmZazDr_nC3C3FSDUHmh7BnpQKz0-4A_ogQN8M-Mo1p9ZdfL_jWB8nhcYtcM4gLCvmEYAQowqZZaWLrfNb2k3rUGHhjMbFhUQYUX7kn7NTqjLgjqkpgr-oPYxpyoqqy1ppFvsQpsR65VH370DTEw-DF3-7lEXyXq5Ad0lxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVHt4qWN6TL-mwuA1DPa69jbwFyqYkYriEYJilzvuQKDYOLnNnepPcqn7v-C_fkM9J_r36M8nmaLlnrgEYAQqhmunyvqCFKHdrzHJmbAQvmX2mAQz8gCVELcgYPTHzMxxRXZQkuxI1CdY6uxvjAOIqoVFDO5qttXiEhMiEChXoD4zDPfPJ6B-KrjEJec1c8oGHKutUmkYQ5qFIQXgp39-II5vZsU3MpaYC9apwznupz20SxZmmsqmQp91jmjmYTDQBxcNhCV8oSwCmK-O1ElN3rbQdcHzOARpX9OkHsJSqw-Rcgie6FHaIIn9FxcorWz8iDybjiAwSrbvELJUtet_w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=fhfKJ_88h8RuYdt1Qr3gi3iUw4Nzosp7ICF0_snh3BbBU6MX1Ff76RxHrx6rjxgCWqHYMdhOKz_jxHIPMq8VelfNnxa43WrwZocOAtLEZXm40z7Yh9Ut_AzAhoI4skjnbaj9j6HoIkhBrZQ8igagko7P7raAevJfASd2DYIOFzRSOKOP1VbVArlLtEGKWlHsdnqtMjgDzD4mZacqlv9v6vHvKA3IxKZO9UhOWPbYhVajL2RtoN5f3lRtjw-fc7pGKvb4q8DDEKhrL9H-qaTsMD7FAf9MC10kJAevy44MzObxDJDA7o7oRYo0j6sD0yub7S-WgiUvY0fEei7IP8LYiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=fhfKJ_88h8RuYdt1Qr3gi3iUw4Nzosp7ICF0_snh3BbBU6MX1Ff76RxHrx6rjxgCWqHYMdhOKz_jxHIPMq8VelfNnxa43WrwZocOAtLEZXm40z7Yh9Ut_AzAhoI4skjnbaj9j6HoIkhBrZQ8igagko7P7raAevJfASd2DYIOFzRSOKOP1VbVArlLtEGKWlHsdnqtMjgDzD4mZacqlv9v6vHvKA3IxKZO9UhOWPbYhVajL2RtoN5f3lRtjw-fc7pGKvb4q8DDEKhrL9H-qaTsMD7FAf9MC10kJAevy44MzObxDJDA7o7oRYo0j6sD0yub7S-WgiUvY0fEei7IP8LYiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=OCfYvT2ibD7ON_1Cb4MnI5_9o0T9iA_knXeL10RtWGvkJQbcGRHcDLug_gvdHTk4KmWWjX9E1MJeelb_ELBks4qMdqrMrg7h0wRA8DaNtyZuflerPZcbknAeey4DHbqj5M-VEakeOFa9Bifp-zeCViRtgIFYVDfdETuNhwiCY-DLoIfGLDmuTphzgbeqDkWiH_a3m18aPfBx_5Voi4UvNuSGD2_8b_EipJvdr4MziKrlAw_HWOLqlt0SfjR2jjxkUS2A_Ua0d9LDntosgSC90Vg9BmNvdhK02JOyriBZRZJVjCzgbFOl4iTczHe0rpULOWDi2RTB8K4Tw8ICw6IPkoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=OCfYvT2ibD7ON_1Cb4MnI5_9o0T9iA_knXeL10RtWGvkJQbcGRHcDLug_gvdHTk4KmWWjX9E1MJeelb_ELBks4qMdqrMrg7h0wRA8DaNtyZuflerPZcbknAeey4DHbqj5M-VEakeOFa9Bifp-zeCViRtgIFYVDfdETuNhwiCY-DLoIfGLDmuTphzgbeqDkWiH_a3m18aPfBx_5Voi4UvNuSGD2_8b_EipJvdr4MziKrlAw_HWOLqlt0SfjR2jjxkUS2A_Ua0d9LDntosgSC90Vg9BmNvdhK02JOyriBZRZJVjCzgbFOl4iTczHe0rpULOWDi2RTB8K4Tw8ICw6IPkoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj1xUgD58uoql1vCYGuvftMjEkNuUsyuNGWCy4cX6TI07_t_HEyfw2WYbRzCQqh8j6Xpi5FMdtN-QVNAOPQvRf14Xsek9La1T9Umx9SHuqTLbl13k_0vQtqGtk94TwawcGHyMW33j2l0gmXiRc1w9dX2m5mhNTE3wuagU1_nY40AkjSeL9XmpHwyJi3x_W5GyjVp3Z8cyx93kGaP0GNlNKbGbh6vQA3owVFl6FDkVyBhxHC6OnYD0A4bE9NccPBL9j1CC4YYOeEqs3IiUAykIWPXJY_HJf0mcXqHq2QT68cacmffV6-8PxWBEBISZGJiqggxcvqJg25D4qbaMjJS0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr9zbmMxZVVFVpOlRBy_Z7rJ96IdEtMDEnLMoVHoeN3I3AeIgFVBy5GC1YIuxZ70XJLzZTZDYYY-5qmztqL7f_yFDjDlG5S2pCGPRyF_ZIhWxSsgaKvYMCes1ljblGZBu6BQKXyiCyUXdYo9_xAZAFvaVczcNTZQH2g_F9IGt1aGMZaf6E9z7H2drlBNLxUmPJfgGdGHRibLdXZlSr-tvVpN00Yb0c7EkkGhUrKSC7e9Ezxce2YZ8YmcRdfZvhSkowyEcvDR3YV5-pVX2N176E1LrzfWa6Q4hvVhshUHVCW28C2o_Z-VafA8xfv0RSt3N8223P0agWHkO67XX1j-Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=b8O0DvpFxZOG1TA_qmDeSCYQzHXMN9ZPLb_Yj3smmziEzoW3VsLb5QEQRosnEGAsY1tqTfmJElAhT9tOH8HbaNRrMLrlyg3smj9JjBu90wCIi1kc2x4lQCOpfE48CiX1oSqDfgRTHzy8Rwhr4uR2bHvu648wHDxPjyfo6snWm50guIdkuwSWIRah7URxRgyhfW5HDZvOL_4VWBgUOwHxZGu5HBbpsrRq-pIbt4tvDh950uPxaXpNR_UE6q5cDnqGUg603qybkQRQHlO3pBTGohQdRXAJgMYwnwJHBFacDSRD1Q4AV6hLxUgz78gVUJJnH1xUBgsw33kiBlv07ep0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=b8O0DvpFxZOG1TA_qmDeSCYQzHXMN9ZPLb_Yj3smmziEzoW3VsLb5QEQRosnEGAsY1tqTfmJElAhT9tOH8HbaNRrMLrlyg3smj9JjBu90wCIi1kc2x4lQCOpfE48CiX1oSqDfgRTHzy8Rwhr4uR2bHvu648wHDxPjyfo6snWm50guIdkuwSWIRah7URxRgyhfW5HDZvOL_4VWBgUOwHxZGu5HBbpsrRq-pIbt4tvDh950uPxaXpNR_UE6q5cDnqGUg603qybkQRQHlO3pBTGohQdRXAJgMYwnwJHBFacDSRD1Q4AV6hLxUgz78gVUJJnH1xUBgsw33kiBlv07ep0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7pEjf25gWzNfLvcSeLe1mOe4254o3mf-Ju2wxVYJNijVaMaZTROYLuwMSP9iV5R27aKPuiAGPq2-ifj55fIVAFnp3CRIKquzYRly3_Dt6HoR2sQ3v6ulszb-PjijTNB8BddTOL1VqLvJ9ly8hz7kc-j2IjdQj2hm5cL4q9kioGrEt8QAnka53-ld7b11UGfT-2pibCoJIzvas1m9J6P0OpEGVJcAp2tYkK6qFJUM-EjbN5dzpe_aZXLkngS-kg_DiUFwU-RJqpd0L5iA6_RxMGrFufV6s_p3_wG3cLBYJyLYSakMLJw8olnKSueQ2yCGeDOBgurPkcPLrta0G0GAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oed5EUfquPN4TJ9DTTuB3eQSndk9v_k0sb1LFEud9S3TQr15K24iv83IKLIn4IVE6scHhd-ZZZbaSV2bi2S39GZwWJ-6HtpUOYmVcWja-5n0Rkc3VD55VSnv5FPCmB12uMqB_Z8PunulkVc7wsCz35eUElAHxGJ-N1XB4q0oY8R0tuduOU5HXd1IC9TH8ssml-gZmB0Wt7jNJzufXefh1P6FuVl_JR_m1kyZTGZrdVmXgBt9wnv0XqV4NLj3PeC-O2lpo8F66k4T_Lzf6yCFU6-2Blx0MUVw1ALhAUhut5yzacHRzp43_YBBA7UAVnp6r7irEwd6R_u5iC-Tws7h0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz9ooZCvFD25N6q8KjTn0pcUex2ddIYPMAhS-T2rvYj0whN4PIf6Gdu_sCS48Lq9j2SXPfyR2iBOC6s73WRtOqKY52jUogIr4nHY7lNS0aE1a6LGByQH3jK9hCHqkFAwhLS43FZeTuNzgn3HwlFzR6-jK2qZeLyFtE5Mys_oQXOusnaDFgJtKs5XJtWlicvUKeQhEEOycD_2KDKXexCcf4MH3bp5OpsZqSnyvkl763f4wJgzzNaoCL9jPR1PRKKD3a5SPSq324TpfPYje4Jiq4q7oCCC5By-HnXc1m7ddSGz3fCKURS7_2Ik1ZrFx7WG5iotHgVBBQzC7lCSnodL0A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWNbmdaNM55QgdZIgdeor79xl5VCf1he-8Fan6zjVvu-DadYpd025VEG6d-ItedkBo-KrAbkFOQ4N7g39un5tF9r3vTl8PmgMF4Fpxi9perTKKchXhCLZqCc4N0XrXILsdA_bt6vd6V2rjbtXQweMBnaQ3nhW8K7Ffm4SUI6dh_UvRKhYJFiqGm9FkKoP5qGp6bQ7D21APUwcRT-BqLxHBdVen03LMJddH9KUoaqZ6SFLolKt48XQxuzI8OeAFFlY3MZp7-4mTUQrZ5G1mFB6Fxu4yVlILHBer1uFgK4B0CcAJzd7LRt0oA213c2BL9CT_oiFoaEbNVJ67Pe5VLnHh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWNbmdaNM55QgdZIgdeor79xl5VCf1he-8Fan6zjVvu-DadYpd025VEG6d-ItedkBo-KrAbkFOQ4N7g39un5tF9r3vTl8PmgMF4Fpxi9perTKKchXhCLZqCc4N0XrXILsdA_bt6vd6V2rjbtXQweMBnaQ3nhW8K7Ffm4SUI6dh_UvRKhYJFiqGm9FkKoP5qGp6bQ7D21APUwcRT-BqLxHBdVen03LMJddH9KUoaqZ6SFLolKt48XQxuzI8OeAFFlY3MZp7-4mTUQrZ5G1mFB6Fxu4yVlILHBer1uFgK4B0CcAJzd7LRt0oA213c2BL9CT_oiFoaEbNVJ67Pe5VLnHh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_U3wFN5AF0OdWJ_A7p58RR2BhiTxnPQYNnVOVycxhFK9sE3n3yE4XvrGuVfs-ydUs6herZLeQCZgUc8xuNHLFHq2xwNL8wAmQ21JkcdNmdYqG3Ha8l-aM_Y17QT0qJZHyv4bwlEVpdQBBkWRo4SYZgfJT86BK4b7y-ohMeerF9ctOD5Cx91U0j_RT7qKKYY5bJmxxJ8zP9UfP-0FGk82BjpvhzIf3FoowOSEf5V2DFlfThcBt1KFt5BjC2uyJFcE2laczuKlgnHDH6T_TOC5K1mMO9JP8JhSwNIFPRacrL0OenbY9GY_uWZHthsX5bonBmMyGOfLBpkgFVH4xHcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4Tc9SuwwJulhGGpt1u7aP9Yh2x6QMI_X8kQHD5ED4OdM-26ZQbqvV10JZd781Ueko32pv6d_I8oxZdYYz5lGBcC39GtOQUuFho98bk6dP1dE3UFsEQcaX5TqpnAB7-DC32Uc1ZPy-qjW-j5MmSkDKsLX0IJkHLIXOV3hMElF3s3KNRm9JQS8-b52NzmMamsHWgg0S26BqDlZ3rkpMcK1DsesQbYhMli7BoDDLsG2cd1YXqWrwV_5JlSrp8M-s2SD11gXDNoxq9-Jjr7-sD5v3hZiGLYm-wlaH-JqWDFeFrP_MJhIOODYF7VJ2p2GTs8LPLKsXcLXdesRSBQkkenvw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=AoPAHBdKdiSVnkCzzvsmlK5l48H7GvNL-IcFoqEpXKTcJE994nm23RXJ0dXGo_r7Jeth91pzJH3Z1MVpOyaXjpCxmNAyt_ZGluxUL0IzHXW2ZOFkDcic3qJgo3ZBkfhhYtyApIYQo7vM12K94nmGo3DChxQr-A_kErYJxiGfiTpf1J8uUj-u9G1tmESYOTRO4mVPTXLdOlJVRegOUev7xCxdrCDeQxCMxe-AX6h6ZZXS2b7rD00RBkoFNxNniwaSPnq4cO1tMmN1EhHIA-xgUXLNsj7o8oAJnekkBRhnNeCnRA_uUOGMiBYC4cxv2_wqLNBX1P4SM1zDx2yO_ZHh9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=AoPAHBdKdiSVnkCzzvsmlK5l48H7GvNL-IcFoqEpXKTcJE994nm23RXJ0dXGo_r7Jeth91pzJH3Z1MVpOyaXjpCxmNAyt_ZGluxUL0IzHXW2ZOFkDcic3qJgo3ZBkfhhYtyApIYQo7vM12K94nmGo3DChxQr-A_kErYJxiGfiTpf1J8uUj-u9G1tmESYOTRO4mVPTXLdOlJVRegOUev7xCxdrCDeQxCMxe-AX6h6ZZXS2b7rD00RBkoFNxNniwaSPnq4cO1tMmN1EhHIA-xgUXLNsj7o8oAJnekkBRhnNeCnRA_uUOGMiBYC4cxv2_wqLNBX1P4SM1zDx2yO_ZHh9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=uXB0847PowE24-uk4i2ctyI6oCJNrdV2qTbKdKxqw5Nd_jE-CzXYcksy0yZvVDF2PmAB39dUPKwtisCE4zhA65dFzctUnJ0hgzIEMDT7Ne1JDDuP6QAfnB_13A9igjPi8pQg8N8g1MUQL2rPfwMv7a3DCkv8OF3eBNxs3f_8RwUMLrP7e1vQNwVHjWJrkNT7b4cG7fQsRSXq8ef0peN5f6yaHrbIG-xta-88m84leGT05nhPNwNAMN_7dLQnbwknF0LSzuykvVVhjPRRgIzQPx5Tx661V2sJc3bRHOwBM6Qg6cLu8YcjPT7bo95jl5Q90eTOv8q3zPzu3e3NpjzMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=uXB0847PowE24-uk4i2ctyI6oCJNrdV2qTbKdKxqw5Nd_jE-CzXYcksy0yZvVDF2PmAB39dUPKwtisCE4zhA65dFzctUnJ0hgzIEMDT7Ne1JDDuP6QAfnB_13A9igjPi8pQg8N8g1MUQL2rPfwMv7a3DCkv8OF3eBNxs3f_8RwUMLrP7e1vQNwVHjWJrkNT7b4cG7fQsRSXq8ef0peN5f6yaHrbIG-xta-88m84leGT05nhPNwNAMN_7dLQnbwknF0LSzuykvVVhjPRRgIzQPx5Tx661V2sJc3bRHOwBM6Qg6cLu8YcjPT7bo95jl5Q90eTOv8q3zPzu3e3NpjzMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwSzRc_1h1vwF1ZBUopgcLjMyzjwQXadYwcjYaN67X4nzx5rsjWxQeRQoC5x3N15NXgeoaSsUPXI1ZAZlZXXsJx9HW2kRRWEnKAyi0jMudBpfyERwJ8YbqF5ri50HB8ptzdVu9chOXJ-DgKfxwzRC2SA--HgAjJ0sfkTbNFaPs3J5012DrN8ktv1dvhgincRTTYOldCAfG6FouCSDxA0UVwLpxWz3YJk9gZhW6D7IzcA2zqXthpdmECcEqpdbvO2yfgDT6T6MmaX4U7CzrEZ1C8ihIx7C5prNyqcyBPUAF9XPE-XJ6fWryHYHVW5H2PEfx-sUagvrVos6UcRR6GgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9Ukqam7OzrvdjMv-QuSHrjLQsBIf7Tbs-KQqgTmQyhZI63Ni47bPT0lwh2huh1LZbD7G6hPiFElp8dlaozYcB3rjecLcfV7wrmbhdGlicCkALS8lmUa23boHHc9IJWJcRyRdcs_cL7tOJUXNiQfB1KW-c3TJoGPyCYJeKk4lMsxoWsPlDR10p3lNqLOXacgHLo9w8hjV_hHeSvZDdz2DnzhybJww3bYQxQvEKyvvlu_Rr4-YLvPZxN8VmFe9jck9kJqbzEX1BnMfjHnoeOV7AOBmdYkd87dkRyAxvinvHKjavLuJryZUelG3uveujb69Ues3nGM5gvcTJNoBshqjw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=UhRRE_18JpRnWnq6Ynh7-WOHQIYCE9FzAoup7YjBiw1u60QtWwPCPBqr6rdUAcglLBA05iaSI6eHPARSruyEF6k5kzoRt7452dUZlLc0z7Z4PO6_nTeCEsPFWOjDRJuNLDahsDAjP9d7PBtvcbmuHAmLMOfa1ccuBuKT012N8YRfdl9CjbCsNY5tJi9TswAEOosQ7-oHgZBmzdeM0xYgDM_By2M2NeIIVK8uj3qcIe_a-lldSERBUwVtPY4Pza_T8AhyDsFOIA1LZjfbIqCcor1dY06fGZR1KQTU6PK8CQolzoprT5QPcxRYT7b99qwtUSOGweHyEj6iYMZnOtFaxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=UhRRE_18JpRnWnq6Ynh7-WOHQIYCE9FzAoup7YjBiw1u60QtWwPCPBqr6rdUAcglLBA05iaSI6eHPARSruyEF6k5kzoRt7452dUZlLc0z7Z4PO6_nTeCEsPFWOjDRJuNLDahsDAjP9d7PBtvcbmuHAmLMOfa1ccuBuKT012N8YRfdl9CjbCsNY5tJi9TswAEOosQ7-oHgZBmzdeM0xYgDM_By2M2NeIIVK8uj3qcIe_a-lldSERBUwVtPY4Pza_T8AhyDsFOIA1LZjfbIqCcor1dY06fGZR1KQTU6PK8CQolzoprT5QPcxRYT7b99qwtUSOGweHyEj6iYMZnOtFaxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=hVsA-oetFCwOhfjA9P83uNYqcONvTy1UNSqbPUiN-aRvsBToapuuS2ZlVIJ2IMrLx7knlD-ztEB5SErcvRAi8_aYZqBLsAf6Jln9NerBwIF3wMEwAP5jjgYOy0pSfq-wMz8oLV1QJYihyu_hwqLfogOqT3ifA2_TeU7oRpx-Y3uCwvjw4vJQ1khvTJPAV4bD2DjoAak1S-w9wMp_UwrKjQRuoIAHoEGPJ1nNJuh2x0wkatFw74h79sZsRDwoaWi9xsX9ABkzm8Ifo08pyIL2VaqwM35GmyQD2EznTHU2u-c1jmDDr8aRAUKqkLf1NQbr9aio-3iuZQtCY_Zu1xbPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=hVsA-oetFCwOhfjA9P83uNYqcONvTy1UNSqbPUiN-aRvsBToapuuS2ZlVIJ2IMrLx7knlD-ztEB5SErcvRAi8_aYZqBLsAf6Jln9NerBwIF3wMEwAP5jjgYOy0pSfq-wMz8oLV1QJYihyu_hwqLfogOqT3ifA2_TeU7oRpx-Y3uCwvjw4vJQ1khvTJPAV4bD2DjoAak1S-w9wMp_UwrKjQRuoIAHoEGPJ1nNJuh2x0wkatFw74h79sZsRDwoaWi9xsX9ABkzm8Ifo08pyIL2VaqwM35GmyQD2EznTHU2u-c1jmDDr8aRAUKqkLf1NQbr9aio-3iuZQtCY_Zu1xbPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIzynxhAiizO3y8BJUNvaYMCdkFDl2FkMgp2g1fQGG49j6BHM69tbpbi6mfTh36doyVS1BCFqLmpkN0atHENU2et8dK48Koxd7j0zdSuUW6f5xqYWY_71KnLHQwD_S4QZ3ubbF86d33CLZymPgzIKLbHvEMWC50qKXRQDw-VczLh3LBVzPJE7iulAniAf9tRTiFUfI9excKwUNnvjAohCRLeY-Ve7eC8QFu3Lz4GRazzqwlm0yZsqC-vMyQkO_-6WZ6_41vimy5w4TD39WauruTYlIyiwhPi_opsjVtHpI6cH9okk92ocRnDZzu41Dnzrd7m2bzdrNYOlm4LLXcdOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U88Bg-iIoSNZSbjVH_Zge3Ee7wiXwJ6DsXDPaZE6281i1NPjdz_MKCtGBwoA5Xj9ern_2ea_2Vorrlt4e3Ee-dXmgzzY6SgpRTfn0UBXo4I2SQXeumOIxpQxOIf7Nx6cp1Fj9YbXowUuUybegeFVjWxrRTKEtP4r7MNzODv6vZObicw92wSATaFd3sh0fvkCtHHeNcYKfNixFBcebkXGTNJ3n6ziZnH5-S0_MpfUyRANGhdzTqP1OYf3uAQYyOsEH2i6-R2rvBCPHNu1JxpOc-uqs_lhOARb9XMWFbPMWeMuTthNE90_WXYXvNKcytcKhKsBtF2ZMksekHaq1lCzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFNRQRvugmbvfPRSbgR1xjF2A9JIV2w5Jt_rDIE59NSL2GPHiqUJvNQTQWjmKfPR986s4-N21a8AB2gShCvSgAVF6Tnpef3zZqX1-hLa6LcNp9QoS9nx-89COy8WSB6yanPeFLWYxVOouXXwTyjjZg_UTVirDZ_WqfeLrwS_QrUvZx6vzq8uKKYSL0LZ21VSgjtAM85E5n_4M6kC9O28p8qWBASahqtvZBW1ExusqIQ_YHGhj06qvpuKjIB05pPrCdC2-tPrV6CdxpObuqbQycj1xpoOZ24pFPOx-CSL_NE4qjAa3L4deB86deuA08_DcoTpGbDJ3_2athiWiXmjfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlEVWE-TqalFMty3pQHQAirbkFJyV1xu1vlokqz2txI3QdtN9HCmtfnItLPzxebMICygTTgApzzThkmIVyzUBhiFJmZMjxzozVmravg2HN0gU2Be0kKBbuB_MYellC1ZmIkS1grhAKShibctG8FxwwP4U0SfvPwA171kjfeVIUQk13_PPwvocFpb7ZCQZkwUmpJ0q11OMGOEuzX1Z3sTcpDD6CO0mfmOp6Z_2KcBYyZ6J7TZEk3Moxam5F8USMS_utDNYCORUW_uJ1Pq7G2b-junTe923BqFTvZJo60BXZ9DVeR16JAEKZGCaESP_ecPcYpAbqs6zWmeZQ_YKxEz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umTJDMt1GMU_r46R1kh--kbepwFAY3Vofe5qdfV0ZBwD3yVOOIGeRedbD6EQaTYfKT7bd9t1_Ttl_L3H6LhaVSxzR9KmrBaL2zP5-hhSUf057y5HToZhiKA_8fIJu0Yuy-uEb3iXO5X1ogHwZS6l4GldnMcGZZNwywlRgTuqaJ2OWf6rd3vZvugFMb3-5N5Z0N9NfgRCZVh55AhvgNlgMBqjvTGmlHJ4Z2LbLK25gn5W5pV5edZkvGYpIdshJlXzdDtoP8MbopC7jbGxh3TLH-6o5uTDHiNUW1qchOirBD9RoPg1BEDAPH-Zs9lXoEgC3HJzU5KRy7LVI5CEfSweDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vs6B6xOaxGwgvgbGIbshwsU8jHvW_k2w7-wqTY3V9XqsZIBBg9GothKwccXNnHHB-IdlPArvA1Ny1Az8U4m_nnPMG6kj2zltpDr1SMwju-XfjHX9N3RVOSNaoJQqBRS92qyOWFdnwuFz4DJHQwluzArDroWzlLXJUT7thGKdHcGKr2ro9qj6n6zCYm31aX-yZ4eR9zDytEpGhYh2NV82K1rBT4VoreWr_1UeYT1ZOgdzJv97ES25xDTWZ7hbaSBIwU2PKENPj-lhaTUcoJihISFesyT6ShxWS-d0vnPRBO-0_F7zBcYW-wPDuRL1hV70DMMlpFfyHz5T7-A7qgpq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvnMYTuJsGsCi2qMdXQwXGklms-SWI0TwLezofH9H7K3SuTmFvyQlcKmpRsXcwiouDJjnTI90PHugPA5oK7G7PWE58hlYfFTV50-45dEdbgymPYfkok6ICimpbsOIQanHS4LbVqpGEuSmiK6PoN5eM-RHxTmGv-xXwuYrM--oD2ErZYixwCvsa22O8YQMnQyj9-f0U_oOV3pDZMRWX8blBPHleWcgzftvYqXyNUj0tu4zy8ViK11188vwRCMKc1AxIsjAQb8E9Tig3rwzYgT6COmNNjMBpETXCAeg_rrFKOLCB5KIQtiRRCJLuE-iZ5EERGxVMaXcDb38775eYV6cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QN6hzQOQZxW0O1_DAO54vSFlmMz6qkwh0c934kLDfswUG70RzGVwShxWg2jFvkBcilP3RwpnGx1QYOqslOIyaT6v25jJVOfUu4W0SZfMOFi0_EJB0cq8yi8Q4V9lYAvPVHxSkRJ0InwlhwP3kFrkaAicrXgvRLeaWvw_M-zS3h8nwTEqSwtXqW241IeMI5IzCxMzjIBO0X-YYdoCxGu9y_Yk5eX_2MHxC9IWALB-JB4FFKAZ08iKBx5ajIhPC2IU0xIY_xwxVP-egqTQFm5X2GIDDmD_zOxc-dPjGFlr1HMpZ05RiKxF9UcAFpKM559GmgrpYCO0QHJ8nb-ROTdNTQ.jpg" alt="photo" loading="lazy"/></div>
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
