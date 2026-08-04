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
<img src="https://cdn4.telesco.pe/file/l3XCj1zHx-5TpoF9_7laM280Vc6kMFgBWVeioevFRmucSq9GhVQYLlM07zdyy_mTyNm__sD7Z3FnAYfAoiqKC7_tl_zTtC66OhnEjqrCBrdjznwnM8P18cdbShcQD_Oh8jMyluDA5VZ9ni42Q_L6iiX98glykT7grMi_122j0gf1091yZ7dLugp9AIij2H4QUk3lPZ7vjsjd-ZFgXM5eOFkm5kX73KNMKZa_cy2IwQ_LUqBBRgDhVCSkluraZVxgx6TDAh-n10dXWJY43XrlpyTovppLHKZ5y72aHKVMAE9yEHKPqN352nMG8b2Oznj6bHAWBIt0cnFWk2-Beb0D6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 02:23:09</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ_sdZL2628-noW0FD2mYU48mgldBc2IS37VcvyEac1ZcqmTLzL7-7vDbc71QfTWq2LFnva_relaLABuYiHkU6WR7fpl8rOqw0x4ff9KT2H79K56KQ4VWGBvTUsw8GzVUf1KelDFSyfN8ZN3hHla6IJVLHfddl6CvScYf5gOMHx7s_wk6Rwvk-Nc1Sjj1826qSD4rr7A-nJL9jwP0e740HPFaoZO0jfmXHL7DTY7RTiYmjPdAjy3WkR0JrefxM6MJOLZlIL6zgWtw7bX7vUytOtu8eLokyDJyCXxbFR8wfcwOWpn-WuocBBrh7q81KkElOpVOaaj94jXYwrN2PZkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0Zbkwfj_VVRNft6m2I5vtNvWV_JfD1Rp77agvSiugy4LvHYH3fat9MP4bptUCdTYZqchjvslc4vMcXUwNjbiOxfcsT63JVZAkvC5Vrk1zR4c5EW47qEL9EXOx-5Sh3m65xCUqKmgRK6co8huTimliggOo5r9FyNV9midpHdn_dHc0HXSiWy5OTwMNwFX6kBL1G71_l6QlWjil_oMRCnaLhMx7Ba0PviCcuEEIf9uB5BsLF3Do_mlFlFAApHHkaJppQ5RrZ3YSi_LCL8n72I15uM8QpXtOBA0BrGBfTzalXSWrLHPBTJ-DxAt4qw_CvEUXM_hmhVpZ9oaFIbIWV0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r7X-3-vboGHzU6442C7jbjplfboxRFRc_Qqdh1stWFaqGtuDoDT7yD5anUiq7US2o1CKcnQteTTyzYziZKuTSdWI3oGrORjJ13-RGGophaXcwj-p39FTSrus0n3Q7KbbJ49yC5fEIRAk_GQ5s8JfAuKush2TcPFGqNqerbKhjiXZgrCr5tEdJnpvH0dwMdSLkonyqx3AB8yQToQsFWXKb0f69CvMOO18V3ko-dN0g9w2t93I3RNTJJ6807pnVVLLx7faB08AYReVByhpyzuGcl1hBNrn_snYuTuddwYpaV4lTnXmoWn7bg1-LzfiZqPYwTIIzgTyvxsWF_o69S_lUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r7X-3-vboGHzU6442C7jbjplfboxRFRc_Qqdh1stWFaqGtuDoDT7yD5anUiq7US2o1CKcnQteTTyzYziZKuTSdWI3oGrORjJ13-RGGophaXcwj-p39FTSrus0n3Q7KbbJ49yC5fEIRAk_GQ5s8JfAuKush2TcPFGqNqerbKhjiXZgrCr5tEdJnpvH0dwMdSLkonyqx3AB8yQToQsFWXKb0f69CvMOO18V3ko-dN0g9w2t93I3RNTJJ6807pnVVLLx7faB08AYReVByhpyzuGcl1hBNrn_snYuTuddwYpaV4lTnXmoWn7bg1-LzfiZqPYwTIIzgTyvxsWF_o69S_lUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=lK6y3k7hlCU0wfaWTyVpV1jiHKCpel-FG7JDNzFW-dIimq4o3-BV4eYJnXpWTRSLgKQyf1kOypQuPGwf2m3lN-wJCi7cBR-wrH_KBin7d4CXthn_iLQxF5rt8goAPtLPSDZpgrom8r1u9OPXBvcnK6Tmr6qYR16afW0f2TREIRSOPJCDsTaQ3MUXo8W--HyOtV0GTD0EEDANlDZqgaqBZpshTrVn-v4iiliZ93z7eHE5j95k_-6jQkYqxdYp6MHd6Je0Ec40BrkxduFfz_OK66Y3BU7kcSOjIVCHhLiA_xofErl6r0yGHqpmbxrxSj12MciWQPOyQstrt7hso5OzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=lK6y3k7hlCU0wfaWTyVpV1jiHKCpel-FG7JDNzFW-dIimq4o3-BV4eYJnXpWTRSLgKQyf1kOypQuPGwf2m3lN-wJCi7cBR-wrH_KBin7d4CXthn_iLQxF5rt8goAPtLPSDZpgrom8r1u9OPXBvcnK6Tmr6qYR16afW0f2TREIRSOPJCDsTaQ3MUXo8W--HyOtV0GTD0EEDANlDZqgaqBZpshTrVn-v4iiliZ93z7eHE5j95k_-6jQkYqxdYp6MHd6Je0Ec40BrkxduFfz_OK66Y3BU7kcSOjIVCHhLiA_xofErl6r0yGHqpmbxrxSj12MciWQPOyQstrt7hso5OzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuTDziwN04fXK41NIBTUchPlO5gYpc2KrMTUDwD9SuObJlTcCAbiwPqHY5j5Tc37CCw4MqgfEyaPgKJ-y-bvXAG40KcadQQle6KDry1fBbtFftUj0oIPt2DCq001MsVJbbEvIY1UthJqjCuEttvmRS9uV6JlrDg-fH7PKHyz2QmqqCwuaBiNkA25ZrPgiES-DX_9wRpsHEV_m9hTCPq197GzzvLNiQ_OQxsZblzmFR7Uh6r1mjr-z7O6uY3-bLWauq8__Rkq4FnPJ5GBnbeMqrC19kX6Cb4HyRdDYLjM-Suf2zdNHGjn02XI0ZfyEHZtWGKtsD2sTWrIvE6OJq5bcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZyW9lFixriPk_TDV4HZ-GTmp3aMbzg1qi9xGYU2jaoGimsm52HU3QE_YnX6MS3kejmUMHgaBvkpy8i5-WBKuX9Q_0d5lWqMfusKPpbyPEY1r8NKvTRSL2p5EqNkEApMWC5H4Bq15q_86DzaxVar6QCIgvsOAKqM8uJxU4qRsqyGKEaB6wmybW6G27xKxMVikjNmA0riIrt1ONOgTgfyyqhWGCTmDtDOEOeXgkbC7ZWVLthWLdpJuo5I6DfwBuaAa85BPxkVZ56-wpabC_uQZGG6cCbsSv177ZP0M07Hdxpjj4gK6Da7sijDNS5GT_ibH1lpP-YvVMWfP0uLvtMzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uujkmZLC9Vav3wWS2sWxjNfy4_11pkVpimr5ipSSiKmQZFzT53xbunBiq4W1XcJzawaHAhceYML1EmZIrGZz1ZS_je9L1KKdOHoSCc4RkArWJhgSMQEjcAcbhi6U0t2z2ttFOPBMapATbpgpntXiNbarx_lbi8rj2sASAWi-IKXOp7gliknxj4vpYwuTeJRzTD56XSTt1-7vxiD1MU4QsPZJVfHhIr7L34HlZRSOHCRoytvKRIun0ZlINSDMw1ipERKk9hFKj0pHZHVucvI9D7TFJ-FxDasMI1m8Un6nz3EzDBxkZLFGe4J99Mg4m5z3XX-f6g33x3Q5Bm_Egu_72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBC_H0cbeAqW8pCHjMsPmKInwwQNb_u_6Z8JfFrm6oGYB3_-1srrTEtRpsbXwTf4_-vVrBg9p2d2-5Y6RoiB24-QJV-1lsXzc2bfa-hwfgBBReoy-_-_UIJHOQQg55Ux3T5XVBbmV-W-RBLQZzIyD7ze0Le95K5rjamnkGUQPglS03rXJ5peSq-J4SSVjJwt8rTVBfElCIZB9XcfdLMYbQK6RC6iBdrTrEcGxNkCS0K2DMweLt0mPn_BIJNWpPwXbuzn-Shg4014Z4cMUerjVDHrlZnOAxvWtP7z4oq3ynfYGOSwT7Wz-XAi097XhxIhN4ORMY1yXITl2dsdOAuXrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9xkz_Dl2AfXUhnBlHFK0GgGn5-5x7iqZld1Y5UYKRhQBO4ldxapU1CvTw1EhvYpibJFoYaBml0x7w_W1mXJrprEokl3ATDuV3QnYd_ZNX3dJ8CURCmizzaMH2ssUjFRY2qRTB6w7-FWb_nASBzJbGAO9lAXD64Qi7xec0WMkp8vi1QBgJDbvP051LQ8xCeWxKFDbv4syG3R-yz1OEgrq1wZ6whyHvZZ5fTJqNx2gJpMzyqyNuIaOwpjtULsqkUNkU2oi5wLG0uDAwJN0vTCk-Tnw20OkXgJiPGAxgy86KlZR9RQrGoAELDA2yTt-53ZghwGYe5x6pJnnqLkStyYzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srpUwUGEiqptFoKzQNOtT7GSBq0M8qsaPI08FNiLHCEDfHOT3udeF7LzEvE8caogyUZW_PNy7s3ZZg-ZaqKcqmDl6pWVL_Hu3UCdBugdeh4TVQ-CpVyUed-6KtmxNRX_xbLOUaFW2-Mgn7MKX6EXk1C8q-mkB8c7ukVPCwHqheE7rPBJcI08Ov5N1yk-_OFLvXozITHMnNGEJxVjHWbhV5xBVi2ML5U1JDWZKQL_INd-Z2YPVTNs6B9Dn_TsBkyp0rRwju0y-CNuecuH1Z0ZFYE0NR_6_k11ZIh_1PJtyk8zDc0cfXopUwXBdrnfvBHtuMpNsSE-7oDUl-61Veapfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWbhz3gLBdBSk1szOe344XtEiVN_JWcdljpPevjaGtZKyiDsy2uCPuG1URsnsnMFZ-hj2iacFKFs-AwmmwOy0f2PRanjzSe3B1CfW73qrIuqDPkIl4lxUJqfwePDk0mbl8nf8BEvlN7G2VI-JjX-39M6GwtSS6yD_4N9AUprKIFrISgVx-8j7YxIAdFk7eJ8s7pfFtcbEgdHCM4Zi47YzUlkbpW4wjBVYooOztbcTJxIxXRyxLBnrCkehrrvS_lg_gJn7jzExo4hw6zSVS-btsceKSck80d4ygS_3ETVrmbh-Im_mp558Le4AznpkT-sT5WVhKXPz3dl5Z8P0BaBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR4YNPhiMQRdnSAzNF9Amaai9YvEyIPDLZsDICf7vzpFkX2X57jtipUnB4a9fiqHPjjPPkBIpIMUGygn-OLCOUqyrSsQNrbj1warzucQHSzoFotZeNPJdn-eDyJvWyjRsM_QHVfsRxpLAg_iBY64HkXrsKYYekAS0p-uyAeCpjg4dUKtBdq_M052ShLAPDuGo-YXDxOYsCbQmMGNFc3kctpknmjQyKSMiR67pNNVdfIWupaMVw-RK8YGjaRd1cpZ_N0t1rAogztQ0o43FVZ34leBPcEr6Qbkr973oS8EYPmQf2E_TPSUPNE5eEqJSMkS-4oufTG8Rt6OnMozF3x1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6FhyQlu4XRctwJszA8ONvxGB1svUQq_hBEwAAZ776Dp8QT9FCP1QrG2RrfxYLezRFG-8KNCV6QczhVPVwEyMj7H1S1nYDmBiigmDLFyDr-t9CgLOo17Bv7DQY0r8LGN2rZklfY5ndYHMzw0SNU4U45URToT9y0qeTgMVlHxe9PZHAl2zh7nPyPTtasKKRm4eTCFUQEQiBLrYFYSEgKDxvjg-SyURPsKT512MMLvcChq5i7qFcV3qF59UunspbrtrW44b7BGu2T7iEazObsepqfFLyienMDERz1-ZAtCopjeB6yCMLA5z4uGb1awrOCRmUKmWxZxhh-E_EjRHRCZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk0NLh2vJtWc-NmJUIRFThKr15IsMqU4cO9V637fxhadio_dfQQNDLy_RAR_Zne4RGn14fZxDcBCTrX44Bt-cHx2g2kX375PvdlBur3JQJFgm6p_XbX7NsODS4hFTGs0RtC6bNjbm41nYpzZIXSBjYCRPIQCg1FU2RKZ88UU36Jg03OplhQhXTT0Qg05hZQUL8bC1I6ryt5wyv9SGCGD8VFv_3QQGAQrqxil-S3iy5fdrdvxWQoTriX6qTAIuuHyZ242C02aZx9DJtxpLByua7rO7iCrjhDyual4luaZk_dMqPm4XmXAvJgJkCYOLJAjFaK5HJcAHJ4cqwXQlrp8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f51_OP7f0swvsxOzeb9EmberjebhKiihqesX3myDadW6C94Up51lIo6VVvZqHJjm6-7GvcWgkycjiR5PtrZG2c_b1YFxAkzPRI87mGPEPRNEunnpD1TySYU_ZWE5eyH_Ci3VkhuwRFYcDOugWZQkGRlie52B_ddEJIj-2cClLyIxBo-ROUgQlhAZPm3aqDNpkCroJF4JQTmCSmMSJDmqSYvmEFHrUbq-6phFbz5A0hAdcZVl43MDyeQFU_jIEIFf63xqkDQfuQJ_qiZiBYdesKaSUu6Hn8meMJgIsl2B2niouZQdxhrV2Pi5ZTYNBlluXizt-e3ENUeR5kuh5NM1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbgqcZLSmjVqviDPQVzU-vCJlDRZ0d99cRimhV3pYb_pdei4H7prHP28DvN3FS0bC54fLD3-x5AoPzPS6MrgI2QFZG6p6rTRS1RM_fat1GgTNPtEV2-inh38yrNjgSvd3AgxH-iyYi2Ob4J4kCzz_EdnhjvGKSRUqgs31U_1ELaaQi-8zBbz-QlbMdRFD1V8BH0c549F9fSTuCnXfEiPiHscPPdPP46eXb-hUrrufNoCQtNFJjrvbjoHBWYzNlaa9Z_HoyGHOoY760_m4U5jmZ3pGyKnQ_lu-JdIYSYMTT7ufkyjwH_EHMLDMgKttcPGs-ylrJOEvWlixoTKVhTIaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puhZ-DpRnGzqJ-bQLiOjMo87wKasejlH0WzEs2BjZojwRGV94Npc3RSQi2KhDjWTCmZiF5HgHAheTK8cI1hTezlv5h9Mt3bkB1E0UMR5zzHgCcmdbLtvXJCD6p7PVv4-uxA962ettgH378RFhed5jssxQtcLij8CCLvWNv_3nniHr8QNDEE1c7iVCSC30KVHc04CdWFUHMMFbAWaUsswWtyPVpL0-mdcbbJclY1e_9DooSrbb4Fc0aCroehPXg3C8ghCIXGpC_747v7QAHTqBvHGvbeiSkXN0Xhx66pvebnBMp-1oCPlki3bPZCRRy5_CcRdl_UU7ZeSpn-WOelV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=sROkoSJh34uJ2rOwBt_U70WHriMOAtaKDue8ZdRGccVHyC6m4bf0aYcL131056C99wNocUIKh7kEZdqpmJ0PuoVicMgQgnC9wMR5Nf-iQEdpbAAuRm_VrA0pNNw6Vkm2zqn2EVC3675Y_8-YxdnTTtlYGWz4NblsS6lLx9DKR6D4RtRQvx3D51bjznI8qoMhNDqfT3-YRizlbei9--rPtVWVH0cb9Y9S849c5OHy3esxnB9vLq6U454HHs5xWK6g9Ypzyqjq3lLfssF5GhFDSnXmwei6uZA-5w2MRugGPifjXbLecRuPrO1QeW8e3tj_HRhCsDx0zhLjQdydCsXfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=sROkoSJh34uJ2rOwBt_U70WHriMOAtaKDue8ZdRGccVHyC6m4bf0aYcL131056C99wNocUIKh7kEZdqpmJ0PuoVicMgQgnC9wMR5Nf-iQEdpbAAuRm_VrA0pNNw6Vkm2zqn2EVC3675Y_8-YxdnTTtlYGWz4NblsS6lLx9DKR6D4RtRQvx3D51bjznI8qoMhNDqfT3-YRizlbei9--rPtVWVH0cb9Y9S849c5OHy3esxnB9vLq6U454HHs5xWK6g9Ypzyqjq3lLfssF5GhFDSnXmwei6uZA-5w2MRugGPifjXbLecRuPrO1QeW8e3tj_HRhCsDx0zhLjQdydCsXfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4vzG-qvwFW2tN7M7ghB3ElmWwHrckkolEsNYoyRNK34Ws8eC_-7wJOsJC5KhyAmXiXpjp5U0IC-AENcqa_UEkHuxUE-vVWr2VIuZ69yNfnUOnWgvHkOQjdTHwkhZJ6yh_EIWPpF2jxWSDDELRcfHnpxVxNitZjz3nr4bmNJGMw6aYaSk5jm5O0ClC0f6sK3dykPIIZJE38BvOBXXTmdFl63JamooYVHuksLlXZ0BdZVbkKFqM48cRUJv28GAVSQ8ioqGUNBQEw7c-YjlUvRtxV2vTa_ZuCg-mvfxcZ70B8jG_CGIfWJX61wdof_14UAUTEM99pQsTKu6QVgbRabyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yszg5worjWTxJH3nP15etgJ64AZ0OrdXq_e8h3xU_TEFSAhTHgWXjGsvd0Q8AkqB3gJSKNFx0SlwWl6taEs9yx3X3lkIbhjYzVQaazNUDtJ1PQsKR-xHRmGF-08QipFYnhIAFpPshRBp9yH7HgCfeH_i-OS7JKlWxarVKCPfrEzEzpq6DvzBXMZ4dpoZ9d9W-aW9R93WEM7m-n2uo2C_vQYG8Rt6vjS4nSJD3MOWbzczpcfF0FW3uaaCzqZgMO8xrRNK7DdAs49K6bCNiBO9dSmUwONEPNQIVoZbfHMpncmU8sAPkL_FPQsHaLczUobj1I6EaNvAStofDBFwETBuQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtVFvBSGmfxKwQPfpSMdcIGDl14njqUP3cVcI9G1sIUDpVOaUFPwDvmtnozLoA_jiHN4J6lTLDajfKlICsEy6xYla-IfW_I7kUavuSMaUWsD1QK_XRpfgVTXFQELX7v4xxQTniJUW_KBeEWsu4aXvd3ThjNjE7_3aKA9n_8kBrZclcGeb7DUtvO6YQX6H8qeN-ERg2VHHbX-LOnSfYTr9-mUvm9qz92NF5Q-XmSOvXSlHb-VOe5iRTNDfk3cX4txqgoE0AZSW0UkyVniQydoRR_NdDf0NYkPYYpbaLV9hcg9txOi2LLAnSCEDQejvQ1b1Nt8N2ROXowOkq_friWwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW1mzRAKNREGlFzVUm-iD4Es6lHqehbvF7ywMufFKWbBqK3hbhhdjsGSR3batdmB-bzMZcRvl9oFywTlNx3RRbBOPXkpUUkKtGf0Va9E80H9wCXKCF4lKpL057Oie4eNRVWwi7yMg5M_yYEX2Ey3uIJEZjjTa10r8Rl6CJssQtkEvFRTwkZligHfsyIEZSHRkcf09OAczBuvi9NHXgUwjWJVYDA1qq9cDitC4MOzgkBWTY4WEopelfc3OgjJXSSbKdlngv-FmeSl4FxVGe1TBv0KJuFKT5dEJpreKNhQqFFxqpFzTJvy5elWl7cmu61-57VKrBfepsnAo231TaDGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgFsu00FWHBI_6AlRcsXLs_rWYLCHjEJF1yRId93D6g7CleLHEKrgCSbKoHGbok7rd_9_tn_aEGsvABzepQFqz_-ZAocN7smH4lU5tyGoDg34k7fQARWh6iPJuFJLQuqTMcfw2OOi8Ku96Fum5_GV631SH3jhaygS0JYeXb6rgRZt09v9fmJR-jBiv3U5_7y_2qRcKh3o8EQYe1CpmF8fujUoOQqB7QRyYRrPZcoy1HElZAgzMJGGrg80TLWaaNMJ_Xp7KppbUieGlOwRgno-wW8cnw_H3Wd6LUZuGzeQZk5FzNgu0XmoZjHKyVwAItHr0hK8M9Ochv02BWK3cA6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AivZ7l7tv4uiV0PtDwXZWvC0rd_9BcR6negT7Vsnx6ZFv-wOxhdaTrcoEhgWitv06dc6PErnj0qBFCIrfng4N5P28a0GmduJpKGe3QhT8-06DTOWlAdj2eCN9h2a_wadK-KynSJL-hJCIdG-C22Rel_wC-3hNX0egyp3fYqgXWG6lEB5zeO9OZk8d7pBlybuGQCK_522KY-pMPH9QpM6F-iRVqq6INiLSo9JpHBMnuw0C-6TwO41hFuUDhxZ9hBZXvGn2Cd-FOBaloMOaEc5uKzLcWSA0840bkiruXUiGRJU5DHARM1PihxAe_Khi9mNlyIdXxlVRPXAkg2BEwre2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLz38F-ZRovw9ZsZq9qFuVsxXIDMUJz8rNc7WrLGuc85DWUFWur0Ektpk8RMlKDPazAcYTqCF0ykh1h4-h9kCzfQC-rd-H6q2StwBt9M68ELOguLx5yLMUxmBwDe6-ZWMlAwrQ1ZlRNglkn67B_hKWt_0HKPbeGNUpU62FcB38G5vFR4wiN1BmEeA1doVSANpd9aOPOhjKzdXoJnbQxdDCRgIrOy1DbQEVuFnztMJklAgO1KcQzJTBbSpcwAFxefcNFxOxyn0JtKaoWYE1UbHcS_3MmtCZmXwRCyNblZ9QJ0B_1E_wHLtk6uuQDYRlBj00G-bbhoGWnjjYDmpumIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siAWKekpQrw4jTsRGMXndqXObd2u8CJ848-pd3EOUfdVmf5ddItFsNAs0nupDpjHVLiL4S_zf1YXe7RQYQtXUb4WHVQZ7KrKi_J-csuCAXLDcGnzxLIXlLcC91lLbhoH6MaBP1vOv7pCF_V8AEfq7xY-iLVwvV2TU0uEi-L0LdmNrqN-ylWLXEwIcA0pCMWKaGKzGHQhfUxnjcOfDZRLatm_sNJn5V5wYJOfVtzEtVSZ_bT_KbPNn8vdc3zgnvj73pSdDq4RmadxFk_j_yabJe7yVSprvBdg_X0WGAJ_qGlgT4ytIBeJOXdI69PsFx99egmdlbyHS0NdALHyruP8vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=F3BcLfjklaUZvw__5hvSZd1VEu8GikkaFNjtUEjKGa2KnMKVaac70miYZGYrFQa08O11lQmUX5IIltBj2ULNx0UKj6DOe_nQT4BGvLCHT7t1BxKkimZleghPQQBER4oWP8qaVqUl7jqAIgVpl9ve4Ns1y8Mg8YBbcF3qC-17raTQuPynA2LZAxOtS1VGONChe7YDbepwDtVyr3Dk5SLhVL48n1AqcJibgdnDNuxBsLmHa7OdLfrTcntcdr-vEI9R9Mf-VwUS428MhIljhovUvZQ7qo_VRtyOn3S_V1dcT7mwDmRz180wzHefmruBcHAc-dpTRvbPHMJOYM8B9iGmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=F3BcLfjklaUZvw__5hvSZd1VEu8GikkaFNjtUEjKGa2KnMKVaac70miYZGYrFQa08O11lQmUX5IIltBj2ULNx0UKj6DOe_nQT4BGvLCHT7t1BxKkimZleghPQQBER4oWP8qaVqUl7jqAIgVpl9ve4Ns1y8Mg8YBbcF3qC-17raTQuPynA2LZAxOtS1VGONChe7YDbepwDtVyr3Dk5SLhVL48n1AqcJibgdnDNuxBsLmHa7OdLfrTcntcdr-vEI9R9Mf-VwUS428MhIljhovUvZQ7qo_VRtyOn3S_V1dcT7mwDmRz180wzHefmruBcHAc-dpTRvbPHMJOYM8B9iGmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMrhb_limjyTYrPXXrqSvFziYNDbuYRN2lWOQnQ3__I8GbZyi6D0kWNmC2tqrLljbdiM3FWXB8dQvK9lJj5VyNobqoPtOJF7NTOXwLY21Voq0L37z-Fna05NxVayAhFas-SnPYG3aUD-zU-AxqpS7vJE3Asmfvrqpbz5qSCxsu_kvJlSQzwp0Z0UVR8ou04aMnujQm8FDmVmvI5FhDRTb0AgLapPpXB-XAPOcasgHUWM1j7NwusnMDIvPY9_uhEIiuZdMRjEDate8nuzLL4Ui0o1AICYJIqVD0D7aU0AchsJUv6tR05IOdbfPiyso8pkAhTPPHv97Z_QtdkokLktmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rowCABeQRMKF4m0JaJWF2loszk_IEvtVbO0MazjpZRvWrhU7f_A7Dhu8VKFANUiPeCRzBLEsRkNUI87Z9kQ1LcCSgG2iMWNZRIS5MrxYaTxp4k_5tOXM3UN6a-bgHznEgc6UcsA9gibNymktk5D0Yukwo5MEXSzrrO7MakvTrYQIJxo8nJ2E4iDObr1aUZLozfw5ZAoH6RaMzebk-xZJ2IUKF8QU_aB6DUAzDnHVY71PaIo9d3LPDjyQFo6W1-Gc1CzMFqb76CD7t1QXYoPzOxsM-Fva2Jg-LJtTOM2zSCjOPkbB0OEq7mNAGZRH6zBg-JFfCP73u08yEnGVVv2ssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYD_YKOJVUgkxsvCEnMPibleD9vK-FCXn8Pjz1IAM836xWWg4ybYhpAwgKxXEL4Rrzgbg1s3_a8qEvY84SO-oACMVGJMqSDfkmdrduaJ84wTNHgPcQldyPfF2UcwT-GjZDEpWp05SI7saD8mbmcDuRQ4rjZdfnI5B9iWwiLDY8x-NIhA7uUD2W-hG7se7ErNyahml-vsWhuknDkTmkm2tDylV_wmZiphUicaT0StC4r7-8HzsRdjOVwDVOvf3zLpts5xVXVMb6BYpTmGhjKDgHOqGocZkkH5sv_YUiG4Uznn_6Un_hvMNbObrt4CcKEij4kdjU71VRmYy21YXMucfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tns5_7hF7ygJHFM-M4ZCB7D1SkKS7IK7h52HpkxJ2zS3QuMC1Om5O1aCyO2ZgWpAMSvXizTAzzh-40PeZxbDMoL6IXC2edw4zOMxifLB2EaHuRSKaBHQGU9sOR3ZgBOd1d-gnUJkYix2w3ZgnjYbaDamyKZ1HXMt7IFb_6GqWigaJSNI6cpEeITv6II0BDfYQmKzDKP9_eFT0t0Q7qxRQ0aHFpNQlhELZE1lLJ88pWe606tm481gE7TkVIJbsfKR8tTjS8rFchwdAoo5AtH59oTAxjy28GP6rChQoMVQ7cHwzOH1T6sM40mfS144a8Zwndfqj3e7T-_2BZZIQlTm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmP03ky7EF0lbzf6FeVvvYLFkm_ZpDn9V_yVu6M2xJDseg4yPZu8ld2Jv9lwdGIxtZcnpoCRayfLqzY-La3gq86MydZskzxRxmdjZ2XOavThlIvV7Ok4kBRbK1fWZ-zR0OXiQiEZsKpK-VCTtyo8UFurdChZAfeISMCzWBiFxy_5Rs7MFWIK0mV6kfNdFiaigeGX71OItveaVYBLS1vs-AaA3W2IGqNdaln7WNRMn2LxDvHO13st6UtacOJgbGUq7TqMFWcgJzzaqJ7umw28VNBZVkG77hxhhrA-lMXJCb_xXkxoEWTu_zOFGDZC8pMzbq-LeqWDeLOaVCDP4qmJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVlnMoesHELbN89CWGTgd_2Y4t0rYDTnnAeLE-da8iBHaN_9udIcnKregmnlQSUwm9yeOOK2KUgrG1ZRgMROWNarjHtx5Pw04l5JxrGsPrm2938WtyluPXnckwdCExrsL26p0s-Kg5Z16lETFigr5hmgGz1yQzqJeu6n3IcCBO1Tg4i8bl3VMN4nAaft2QxUKGaYNLXLf-LYafbWnY_uR_ok41fGlhrAu04ryfw5bCYuPDhXDzAPQaZcJuJpsBdt4w044oJCKnVHaoN79NcDfnBYO5PpsrVh-XsEpkZJSRad33bP7r5kaTKvcBOjRiFGN6NTwdMFqcmQNTZbRkSVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGDRSJdeUUp0mUNupvH19RpegeJUCOurWUdrr0BGNSh-3QT9vXj3uvyX9ZedD6l3c1DvMVdN_5JbyNxtWdRUFRzPlRZ5B2eqMPMGrq6oDNsZwJw1whoYL3GNPlkxCtEjeyiJ4WJwZYdPYzO2que1vntfJsND8F8BcyHv6GRkMlGYhpnlDMLpmRSFIxgL4q25nICP4En9H8CbnDMlWo8SMsNk5niqRY9RPLKvQJhOUH-fXKuMiwFfNY5Bkoh-TLZuepJf4L9brftkVvBEUX3EuTs24OvJInRCzucUD1geF-OwGCQgTfk0-FwuOV9fjn4w4h7c2AB7rRwSprBpAiNlJA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=D-Bt9VIxTKyrgV6gQ0sFy1W4mkhzFdcrQev9atB8QhqTrcAYPbh-GmuiPEtLMZQKRRrAUsMw6MZIU4wAN6mFpgfje8Y_RLQRfWDW6wYBuzhgnlGuFuOBmKkuOY9S2JRx4h3BBydVePHdau088IIYySLO6X2RWt0SApAqVL8KWxElwJQGBmhWh3M0uoawzyUlrMm544A_KgQbLPHc3CPctQykKonS_g_wDeRwfZJG-MpcWpCiEDu8sLZiUpM5PmlhVWKTcB2VGBBvJcCDMIu6LPiYC4Z2ftHTtgCn7tG6yYtJ979JkJfY6EhdxaFcrUumwkBU-_BQHrhzKi--aBuhjna3PD1NlTb3U0AkepHKtDBC3hURz1h_z5jfqz8sz847J3uam4GPrGuCFWPayQBQiKjOkMhDRXmpIDtoiaMLuPQAVb9b2ZSxtsl_IuI6xF7X1OZ84kj_XapSHTMV7sqq1AHeU1qEcc-TJ5mRP0PxqJy4hD63fhdyTSGCLE9ohnvEx1ImqPYSNNx0LQdBe7hUHJp304E_erkm_Yu5n-ZxzUfMmFOoiaoxw0_W7wDduanrX_-cEhLsK90lYCnEWD_mTxlFzDAiV3xdd2OpGNfPQXisGFoTXvlzltTBQVBoI8Sj1BVMKdVXdX3kd_L8GmB_Y-qsRui7EzWzNhNfFUWxWzs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=D-Bt9VIxTKyrgV6gQ0sFy1W4mkhzFdcrQev9atB8QhqTrcAYPbh-GmuiPEtLMZQKRRrAUsMw6MZIU4wAN6mFpgfje8Y_RLQRfWDW6wYBuzhgnlGuFuOBmKkuOY9S2JRx4h3BBydVePHdau088IIYySLO6X2RWt0SApAqVL8KWxElwJQGBmhWh3M0uoawzyUlrMm544A_KgQbLPHc3CPctQykKonS_g_wDeRwfZJG-MpcWpCiEDu8sLZiUpM5PmlhVWKTcB2VGBBvJcCDMIu6LPiYC4Z2ftHTtgCn7tG6yYtJ979JkJfY6EhdxaFcrUumwkBU-_BQHrhzKi--aBuhjna3PD1NlTb3U0AkepHKtDBC3hURz1h_z5jfqz8sz847J3uam4GPrGuCFWPayQBQiKjOkMhDRXmpIDtoiaMLuPQAVb9b2ZSxtsl_IuI6xF7X1OZ84kj_XapSHTMV7sqq1AHeU1qEcc-TJ5mRP0PxqJy4hD63fhdyTSGCLE9ohnvEx1ImqPYSNNx0LQdBe7hUHJp304E_erkm_Yu5n-ZxzUfMmFOoiaoxw0_W7wDduanrX_-cEhLsK90lYCnEWD_mTxlFzDAiV3xdd2OpGNfPQXisGFoTXvlzltTBQVBoI8Sj1BVMKdVXdX3kd_L8GmB_Y-qsRui7EzWzNhNfFUWxWzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=DNUvjtSk2PwZL7R47yjCC05t0QSM3V2Kk4o-3P0a_BgTkj7trzt0SEt4DfkaNuRM8RXmPijjK96DyIX-5C1Zs5NDDlpPgbgJka_IGaDpZ3WnVcKcb5627bywOm7z3TGeG9RTJBlSJj-YS7aJry3auKPkDs1mI6aqLxJtni3tpA6pcLWM0f65h0hfgCglc3jZfLtno7VG7k-2BrT2BkbYgzqMMa3Brye56vj9R-QmgMqe2Q5iaPhdH8HkYjkvsN0eMsbrCKQkRaM7Y9jYp10WqKHdsYUCuXLfXHE-S5piepH8rMHWXRZdBLlolxq4SWfAgOZBxulyEun566hGmS4VhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=DNUvjtSk2PwZL7R47yjCC05t0QSM3V2Kk4o-3P0a_BgTkj7trzt0SEt4DfkaNuRM8RXmPijjK96DyIX-5C1Zs5NDDlpPgbgJka_IGaDpZ3WnVcKcb5627bywOm7z3TGeG9RTJBlSJj-YS7aJry3auKPkDs1mI6aqLxJtni3tpA6pcLWM0f65h0hfgCglc3jZfLtno7VG7k-2BrT2BkbYgzqMMa3Brye56vj9R-QmgMqe2Q5iaPhdH8HkYjkvsN0eMsbrCKQkRaM7Y9jYp10WqKHdsYUCuXLfXHE-S5piepH8rMHWXRZdBLlolxq4SWfAgOZBxulyEun566hGmS4VhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQXaGF560oHOYIy1kYxQ4KL_3epmYBZ6ZNYGbJSkRtIa0FE8GXNAi6X4fghwSAK2D3RUSyVQFc7N9HjrUhOWAl1zFKD9hjljMwBu_QNfkIC5gH1zgvQISKf3lhs-MA5y5Ti1MmH-SKvpKB-FuzkNtTIBYvxi9Y-febtbQ738Tk2X2zbOpUPlpAJu6Sv4DnSTqGI6XUPAP-Voro62TMMzLn6GABQ0M8DzIAziRo3MzZJUJ7qjHa7UI6Oo3xeMXXAl1e0nmMYzRvDP7tQliH0DH6OgvWsioq1_NQk9MUaXFiDeoOPx8kL3G7GocMZxA9gVl2fO0pCPUHKsLw3jYHcWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gj7PigJPp2OOEar0DyXYfz1sBoWZ2khG4YmgcUqppUNA3kLozmgRyfOxEn-oYZwP3JDMjD668dx2sCETM-jhEofaEUCUsKArtUJyV7ODBjtpWd5f2omRyw9fDCqqJlj1mHM8GNjwRkRym8mMLmeLBJN8gKp4LrAFyYoI0-anD_bCvH0444RaL9zjCKvmCtV86JuVm6MzK4twePjlhhD8Ad2zwJevZCVnlTPgidNlHlGhnY51bKPjtPhTgFr4JmGnhZvDpkyJV-l6VuiPO7eE546s7xyk0QzAv9gDD0LEZmVURkDPyZwym1AAUIiGZdMSI8UxO90DyrvFRSjEEI7m0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=tkk7nSk5hehHzqfIzZ62GP6i5wEiAHNkBt_kKSC0xJmXjh-L01xza3qXMfSFByx6y5QHFCORLkz9ugeYn-ql5bvw7jTTXs8vZxdSmBgglTOk0PE7RaxbZawsgD-dbLntT6y43oh-ZPXqB8SoZk_risbReshB7XIIgUvNWRSKvSJHgBdbmsrG4Kij7Lv87MRkX2KpxUzdaEUmZ7yMrrU7uXjjjt2qR-Tv9-ACORITb7WMDRkEN9n-VIAsrHdK0P5ydqLIthIkLN46Zei1liOONAQdnmTvEQsyG-QuD2M4aioBwv17OKR9gopxc2K9Xu3QCuLyqps9sk02Tkno2icr8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=tkk7nSk5hehHzqfIzZ62GP6i5wEiAHNkBt_kKSC0xJmXjh-L01xza3qXMfSFByx6y5QHFCORLkz9ugeYn-ql5bvw7jTTXs8vZxdSmBgglTOk0PE7RaxbZawsgD-dbLntT6y43oh-ZPXqB8SoZk_risbReshB7XIIgUvNWRSKvSJHgBdbmsrG4Kij7Lv87MRkX2KpxUzdaEUmZ7yMrrU7uXjjjt2qR-Tv9-ACORITb7WMDRkEN9n-VIAsrHdK0P5ydqLIthIkLN46Zei1liOONAQdnmTvEQsyG-QuD2M4aioBwv17OKR9gopxc2K9Xu3QCuLyqps9sk02Tkno2icr8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho3mVmxWewSIUuuZivBzXeBKdoDy7lrC8wAwxVdJ-bgJGr1x6e0HNs8m91tbguzOZ6TE9tohIg89d6flwurcYzIXI4LzHNn6Onv4OOOIU-YtxJn54XvLRmyl_srAgpA5W4bbLefizxVymxZGNRuyMTYxX6-PwK0FZbCYuhYqDOSG-VNG9JQFQfc8TSfXf_Jc2_m1iRyK0gWN8En2dcQPpouyfP4fkGtQzmVR7WY2_gp5FBZnihk6Qsf9BAdwx4WXNH8FnspuRaeFonlucw2RSfnox7xzew40U6YWclICPDKUGaAoRo6urpHKzOulOvBbKyWzHy7KhS47OeNh6j-fEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLQ0w6Cn4O-kA6ig6X1YplCd3x7u_el631kxDrTFDYnxwCyR6HMuEKU8C4dSEMygeVzw84ByEa0ff8pi91QQWyFNE1gbrN0kNJ-SpSxiposkrGnAJIu87GEc4mM1P89vTZjwdRxeoySmSosDKgydnU8qadr69bU5Sp2GSntjEItrUfiCOPmJ6x83WCAhvHomqk0VbcefG5o4AREGJ58yWCG-xaWiuXozmGwiD7FiQwq9OVBjHP7ydwkEkyG8QKrS35gj-RN6D4b5yJuraA3rOmhisSosXRLf7YJvFeBR2OqKGXY9asYw-G4dHQ77u8gY3k6VMu-lGWSSCkLIfPbEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taKLINmzu4fH1pIrdPnlMGmm1dScqRYKUtyld2ZYJ0gjk7cgzv1nHyxc0VInmGRRAIY3133QP_NVcuSJjaQBqfM7xhBpVxqez2vs9iLULbsAa28hgf_iM4Hjn4CYNDr-5EElw69OV7mjGWWmDTnH9Q1ltmjNiDbZKIHwlUWYxtaVSwco3rbXa3InLvDwJvJt4QZlv8vv5WznWp7af99is55NNFUKPB_HX6QJtfyb2qoyUfuoF9okSTL5xTG8RcY0I48DHAcjR_m2GrgrKLWFula9yW7Az_OIpINNJT-nNVe6ZwkXMRjMJ4VImzho85pzT5JD4dunmxpdEFb8TwsoXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTuvTrpZU2e1IBCL7DcMYyPkIpZpPbxZulHiqP2KLH-HMR9dd-uo2yPHgUlGc-zoXJSfroA4eHph9nFSNtCiWIf-jxXsgv6kMvu-_GorGpB1VbuxaNZ-iM-aBy_ZVT7mhH4qDLgNsUIKwuwnD9hrm44vvCuc4Z4jLuvFKNyzQVcmGAOjoqFJOxK91VWANWbPDpxStb1IEOAmRtqepYJVNcPjmfS15DPWk8dQp1AuRaPJ5z_V0opo1juce_Go3Zr0z5WFmsZvAJbnwBnAyqiHgyBxKrw7x8_5pFMFt74-Tm29wHBfhLZFuMqNv3-aWhG7ocXPTEG3zi1Z5WPquX8PAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoG5EsM9O8zkot1cPa5J1rE2anFl3-7Uh4kKZeOr03Qy7PG70cPWS4GAk5XTkSOTreOL1SbXau8meEP1E9wcOArEQbSNjnflFc_eZUyohRtIZ0Hsd6JITfwU6H2yT31PQ1C7aOHjLQwi789Jf_6TT-iDJk7bLVxmnD-ZFMcFK9iLf_YcHq8943sFdkAJmH7Y5aOh9AVAcr6ndNdA7GCzHe3vMSzRW-ZzrsRGkS-vtqFTIx-gDuv0viUYLn8NEs_DB1br6Xuy3GQAwTgtlYbJxgtrvC9pAgCZxGK4n1BC_IOdJAZL0OKfWLGgbCOamWtv0NIhqN2QxfpXsn5YJQiohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJRw1hkRZB2hSlqkIJliXhL8XyZvF5H6tDMsIk912lqCrMKZdYWWKR7RIwis3v6SK87Ejm6emiakcxh5qRwAS2TU-a908uL0qLoBmFCeM1OP4c6wDlllKeafcRT40aCBPWSp5_UaAx6Iz8bYq6AtDgF7rnu3PoaJhqhYpZB10f6M3uPXHtFF_tvxCJd8tt04QLukf27gFQRBL1VxdhhNiNgbfRmNWtqTP5gmH6_HB32l6jzdM-XYCXxYugq72Xll196NxV6wlHbTGG8khXhcY-FswSasinESi2JIQC2-7EJRIk-m75YyldOewRjx5Y3uUqQydFf-w5FX7_QnE-dnXUoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJRw1hkRZB2hSlqkIJliXhL8XyZvF5H6tDMsIk912lqCrMKZdYWWKR7RIwis3v6SK87Ejm6emiakcxh5qRwAS2TU-a908uL0qLoBmFCeM1OP4c6wDlllKeafcRT40aCBPWSp5_UaAx6Iz8bYq6AtDgF7rnu3PoaJhqhYpZB10f6M3uPXHtFF_tvxCJd8tt04QLukf27gFQRBL1VxdhhNiNgbfRmNWtqTP5gmH6_HB32l6jzdM-XYCXxYugq72Xll196NxV6wlHbTGG8khXhcY-FswSasinESi2JIQC2-7EJRIk-m75YyldOewRjx5Y3uUqQydFf-w5FX7_QnE-dnXUoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf093K9Zz_pvRlQiUfjTzUDlwPcCs-vvbbhztT3Z5bJlwvdDEG7TWbEnRfsbIQKzvxwwQgWu28TQY02R3_7wt925NKe6RwrK40fuLPlqMsECgTWjddaRQ6v7C4Kdb3rDpjyv_fgH8_GUK4d9uzVfJBHdTaPFFaDrCVkZQ4PKLjBqvzYKe5MSYZZrM97Y7cWTGaL7v2nET1Attdz8fyG_cPSP-1WhWfXcjaUob1hWimOENJ5K05Z1nh0m50-cSVRLe71yjKIu8EJKRT0VQ3BFZHUj2ksCKDbebV6zNionqpaXVisxEiLZtERZ-vzyFgscvRcX4-VyHwpsfJh2q6e4PX4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf093K9Zz_pvRlQiUfjTzUDlwPcCs-vvbbhztT3Z5bJlwvdDEG7TWbEnRfsbIQKzvxwwQgWu28TQY02R3_7wt925NKe6RwrK40fuLPlqMsECgTWjddaRQ6v7C4Kdb3rDpjyv_fgH8_GUK4d9uzVfJBHdTaPFFaDrCVkZQ4PKLjBqvzYKe5MSYZZrM97Y7cWTGaL7v2nET1Attdz8fyG_cPSP-1WhWfXcjaUob1hWimOENJ5K05Z1nh0m50-cSVRLe71yjKIu8EJKRT0VQ3BFZHUj2ksCKDbebV6zNionqpaXVisxEiLZtERZ-vzyFgscvRcX4-VyHwpsfJh2q6e4PX4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=CmEUxnY0IHbHyoZxsgDKRc0hksQd7Dhcf9xNcD4rOKjPGghL44PMhkLhaeB0RJYMXw6Fd4LQv9vatgMOnmv_mFBYG-Yp8TowJPmkc0DQIb0rcOYz5yvFYmSbQ_3879i9d2m1qclQIkiz_qOHFygG-UC10DW4f4eWT6GtQ5IMnHbYjMdStno12MAWVfCeVJ1nVnSkTDLK5x7-h-7UADuvTXnyFEKu2G0-SO3mjrSzLNxNsO3ZAzgx2ZkzgMEkhdWajZrG7vZ97Q1peW43vhnWyklsg2G11Z4DCbOsCoSRYX22qtnoF7WECaSarEQ5eavZtcVkvvnuFZuvW05q9OXrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=CmEUxnY0IHbHyoZxsgDKRc0hksQd7Dhcf9xNcD4rOKjPGghL44PMhkLhaeB0RJYMXw6Fd4LQv9vatgMOnmv_mFBYG-Yp8TowJPmkc0DQIb0rcOYz5yvFYmSbQ_3879i9d2m1qclQIkiz_qOHFygG-UC10DW4f4eWT6GtQ5IMnHbYjMdStno12MAWVfCeVJ1nVnSkTDLK5x7-h-7UADuvTXnyFEKu2G0-SO3mjrSzLNxNsO3ZAzgx2ZkzgMEkhdWajZrG7vZ97Q1peW43vhnWyklsg2G11Z4DCbOsCoSRYX22qtnoF7WECaSarEQ5eavZtcVkvvnuFZuvW05q9OXrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWjRfiBip88exvSg02Liq2cZALX1W6gC4WULVbGQWTBE8TwV6a3ddEafcf56L0QmXuRx-Mfr8AlNxa9WhrPRJCVcme-cHJARERAuRuO0cxOUDPMkSMHsvt0Ngae6vQn3J0ttoaqOosW1uSSRqXCz2iyLypGlG97LePK2-cT-bw4xoLGBCp4kzkp8Rg-w-IawTfcvxKj2cjTLKj0cEeQjLd_reUFTP5OLoDlquw8R8AFAwP08s2sHsi7Cm-gphqdcD3gKfo3Ifp5IbGI1-8C15MesaMHLDgoZBvC07izUfdF50ZoHmDmAlcRrgnzKPiqG5ossoeOcxlTNcMus40XHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR7cOC5AUuxj9BmSYjiGa1iMGe4E2AvpKNfuHX_rK_YAUSFfq7VIl0wBNxd3KxN6FUR0kvzYT3VcsLMQnTz_70imhmgXek_Cy490srf94ajfYclk1Kh1YwaYzWYukaydJvQglgWZfl_gVt6jZexnxpNnl_S8PmMPG227iB3POcFTe5NgP86yYt2X8EETYirJschI5tcIRVOM8zoocNhwOe1r5bGBhMJqMrZcFv0NNo2wpTEEGfc2ESuAKUelQTeML3_tVq0abCWD9Cn_ox_X65dflBS-jkLAZav6DDSEdmXf4_tq-IeJj63vSZKE1RlXwO8En0awFWPYbm2QrWKKPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=ZI7ISZnlEMIKE21e8H6c45jhK93eGsZ1bdIsbJ7qJgt3Wucm1AOQxS3fOhuK_UDwT35PxRDfv_AMCG10JWTIdsm0n0gWfolC1ACG1dK4S49eVNs43uFUNfSEyamUAFmj9msoWj4k4E_Gm-xpN7VvAZ5xtQRUgNuNKcyzyufmRU09x0n95YkfOEymv9_V20ql0nzvc575K3kik0cgGF5MLhbtrYa8rPFzCmmn0KEZ6NRbVKCH0BeuH-gC2FE3MM1C1vkdw7yXomNheSVzxYANoS2_YtplFEZSwRax35zSyly_v_mtkhO-zX1gj4Z10vU2_Vj91fyldzO9TLaRbnLWkBftnMic7mHgpttQz53x1j7kaUJTtcr_ZAP395IHLRqyZhW6OvuZJ0RzzP7N0uqaYOCqk70MegBzL4BIMlMpH-HHxq4HObWh2ySgYzZ6I4oQRW69PoF8QU__q1m7X7kAGJQ-oRxfEDlVBFqKCYNod0mTf0DMwSuUc61lDgjUVhoDArJNqn_5dvG5IvL-Glns5jJonwT08oUCXftQooBXIEZRmCulOVN3PwhJp9E2dNDEWi1ZHcenS0mQZ68xA_fLihzyFES5a5y6pUq6hCorwEfNAeByrpUHWjFK59XEd_uKWW_aNsE4ptHdzM3whCIOSD0hCfNPyhEH4BW9bwVd9Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=ZI7ISZnlEMIKE21e8H6c45jhK93eGsZ1bdIsbJ7qJgt3Wucm1AOQxS3fOhuK_UDwT35PxRDfv_AMCG10JWTIdsm0n0gWfolC1ACG1dK4S49eVNs43uFUNfSEyamUAFmj9msoWj4k4E_Gm-xpN7VvAZ5xtQRUgNuNKcyzyufmRU09x0n95YkfOEymv9_V20ql0nzvc575K3kik0cgGF5MLhbtrYa8rPFzCmmn0KEZ6NRbVKCH0BeuH-gC2FE3MM1C1vkdw7yXomNheSVzxYANoS2_YtplFEZSwRax35zSyly_v_mtkhO-zX1gj4Z10vU2_Vj91fyldzO9TLaRbnLWkBftnMic7mHgpttQz53x1j7kaUJTtcr_ZAP395IHLRqyZhW6OvuZJ0RzzP7N0uqaYOCqk70MegBzL4BIMlMpH-HHxq4HObWh2ySgYzZ6I4oQRW69PoF8QU__q1m7X7kAGJQ-oRxfEDlVBFqKCYNod0mTf0DMwSuUc61lDgjUVhoDArJNqn_5dvG5IvL-Glns5jJonwT08oUCXftQooBXIEZRmCulOVN3PwhJp9E2dNDEWi1ZHcenS0mQZ68xA_fLihzyFES5a5y6pUq6hCorwEfNAeByrpUHWjFK59XEd_uKWW_aNsE4ptHdzM3whCIOSD0hCfNPyhEH4BW9bwVd9Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=QRYzKtbdZAHUGxIHe9nvobSv3Ex25F2pB_UPMqN2MPpy-LwxvsHNFR-Uf9iNK1Fol3GYXbrfRKjkcmQn-nfL-qNbMVl-4EG60nIe_jehONzHKsU5mqAoDXulIfKOvlJfmdQUy17wzRMkMwJwOEcOZDo2OiTekcclViWos0kbTMpM0-Ud9rdb0-kKorkkT88TiS68rGEWVDDCsv1Jlw47XJFtOVPMCwhopM_8RzdFAavUeKWdhG9OVzWZ9yBEDsq1krDVj0-rEgqm-BkIH8Uwoh5NqlYeZwY89GceIAdXPkxv5yTtGsGzMSITnZGfjUd_B8yf18G22r6u6-klP5ffxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=QRYzKtbdZAHUGxIHe9nvobSv3Ex25F2pB_UPMqN2MPpy-LwxvsHNFR-Uf9iNK1Fol3GYXbrfRKjkcmQn-nfL-qNbMVl-4EG60nIe_jehONzHKsU5mqAoDXulIfKOvlJfmdQUy17wzRMkMwJwOEcOZDo2OiTekcclViWos0kbTMpM0-Ud9rdb0-kKorkkT88TiS68rGEWVDDCsv1Jlw47XJFtOVPMCwhopM_8RzdFAavUeKWdhG9OVzWZ9yBEDsq1krDVj0-rEgqm-BkIH8Uwoh5NqlYeZwY89GceIAdXPkxv5yTtGsGzMSITnZGfjUd_B8yf18G22r6u6-klP5ffxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clnA-KUefRrp7TDLWW7x2VQR_J05TNJCY3NhzW1p0702I3tH3ZfdBuL2Ck5YqUdu3BMICLijyrUHU8tMG8gZF1mp3Jy-XdUv0P4iVgthC_AoMn3JZunS3tcXGGeArYMxlykqPDcOrIVxSFvQ0RygGZtliZCzs9H2mNdLsPeAqrLsv-GIuKNFqA5qqP8TjRwesGp_v3Tyfpl15YfTb7yOXVIOKKbsXg1zd-PojMGx4Y7hOFbC9Dgzh-yy2ZiiJJKgNHHWY5YuNohtoPzI8ny3Gvj_hkY7zW-oyyLs8lkoJh2uwKzK4Ml-ygsio7L1KViGt0h6TcE7ZASjW6RrbbMxEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKJuVgiQIRB_lvdYQoYinBHUXrs0JRp8eQkUcxjH1ETTlNr_QylxxAgoomF7gN5ihDx6pVadPFxaRc_Q6oJR5_oMx1QaZEQZl-vwLHxaKIdCQufKx_rqAKpNGu8QfK6tVI-zTJOU4KAc-54D_arVvpEDgwqu0uTOCxuL7CZyJvVOcuIt70a4N2NUB-vd9KTjZv6NxeqC2kFn7iyElZUXH-OHx2PvnNw_e1b1ZcdAfZyJ-DKHdisyPUfoNWOEcAyzOXVinAbir3Op_SGfqL0ySr374Pj1DC6w5jn_RRc8lNkgNTfcoJnDfFVrnM3jGd0oowOm9o8xFCfNik-Se42SkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5InG3mz30Cafb7wof5f87mYyoa7qBRdJ5I4-A-wIJaJ0JXda3mQ_Y6bGVFWiR8mV_Nv3APkN-3SuaSiHloWpl06ojj_v_k5-Ad-wQAIX8d0ZcX0C8fbre1sSe3v9fH3tGSIUV6Vms2XXmG9B1NVa899MMi8FyXEOTzXWAWlUI_7P3eN2Gi0mGxAidpD0yUrv1ymj2g5ESLs0FvA1AZHKIyn47tEMtnfYtCRC9fP3dlvqMi09TsM9kmXpCFin8ki7rNyfuu833Cw3FB1S5_QRxA5Ci_uzNUSFsma7YswRTEtFM3B7CCQDsNjddnQjRlHMr8N9tShQ1nFarHbH4pBDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=l1RzSWP0sTnbveqgLf7Li05NldjhJx4VTapqo68FjeKDIHqPIwJYBO1NrRV56DL7IUAoObo8IPLORx6OUnwY0VhqIntfFyuzZG09dAFBW1ju7aSBFoR8v74YskfCwyZM3vx8dIhhGI-HI4PgvC0OvLKigW0fZNNEXaZ_rATQlMj-EnI4RLq07zGG-mMfoljeYFmELPgOhLgJyKs1TCm9C1jfkQQPn4mUNSAPaM8CH1IMfWRVBdD2iV-RoKjpa8Sz17sm2giKmUimdC6c7ttDhb6FBwkqyeoQDOwytkjk0VkI5ftY3T2t59NUbyW_zUw07d1H-gCoiDfv6Z_ZbepxOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=l1RzSWP0sTnbveqgLf7Li05NldjhJx4VTapqo68FjeKDIHqPIwJYBO1NrRV56DL7IUAoObo8IPLORx6OUnwY0VhqIntfFyuzZG09dAFBW1ju7aSBFoR8v74YskfCwyZM3vx8dIhhGI-HI4PgvC0OvLKigW0fZNNEXaZ_rATQlMj-EnI4RLq07zGG-mMfoljeYFmELPgOhLgJyKs1TCm9C1jfkQQPn4mUNSAPaM8CH1IMfWRVBdD2iV-RoKjpa8Sz17sm2giKmUimdC6c7ttDhb6FBwkqyeoQDOwytkjk0VkI5ftY3T2t59NUbyW_zUw07d1H-gCoiDfv6Z_ZbepxOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=hYvFtqlvBD064m79Tr1nze3e73fH8IaHgvGG2OzdZJbPmsLVc9_GE1g24QKIP117TzB9vN28eKPerXDyyDCb9CDPXP5YFOKuRaosUdK945xIeySZ8M2bvbQLoi7vDQrumLXZasHFaSQpb20hWzCObO_rwOZ4TfT9TiiyVNtTC92XB_DWnShfS3mlTWr8hzmq6CAku8Khv0q669DSBmjiKVunsjJujFc5NNNqehVSxLRhwATbO4T3VibPZwUcvJSCaVwisU6iIDbSCcFN8hOw4kMKpaqDVudAA_eunt10tAUvZ_edcKBHGi6MgLy4pjz_jm6WQaD41irapcbNZeQjcwow28Wmq9ugnxmqKAAwrWgNWfkZ_UHCZsoqOkp1XWouclJZmvGsgWuMuJWh2qKperKsn_G6g1A1vFRmA4Qtuua78NpxhGswfmvJVbTfklpkuO8Gq5Zd6T9a7_u9EoaurscLmDoedx8zNlV64aIEqUj2Fq-KpV6_GYCeoiR6jINrvmHLTnzcwt0gFtQtCO2q-chsWdnUxaewLzlLeSrVjSoycccZguFwiUnNsXHMXyHI_bwSyq3POybtWw9QtAZ2eegCSw1qzLaks-8OwhVJw_MXwMNybOHhKfEEa8J-muOL7_MLUZZ8-YIuW8lFZ1X35p22R9jW94SKCxfE89uKmCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=hYvFtqlvBD064m79Tr1nze3e73fH8IaHgvGG2OzdZJbPmsLVc9_GE1g24QKIP117TzB9vN28eKPerXDyyDCb9CDPXP5YFOKuRaosUdK945xIeySZ8M2bvbQLoi7vDQrumLXZasHFaSQpb20hWzCObO_rwOZ4TfT9TiiyVNtTC92XB_DWnShfS3mlTWr8hzmq6CAku8Khv0q669DSBmjiKVunsjJujFc5NNNqehVSxLRhwATbO4T3VibPZwUcvJSCaVwisU6iIDbSCcFN8hOw4kMKpaqDVudAA_eunt10tAUvZ_edcKBHGi6MgLy4pjz_jm6WQaD41irapcbNZeQjcwow28Wmq9ugnxmqKAAwrWgNWfkZ_UHCZsoqOkp1XWouclJZmvGsgWuMuJWh2qKperKsn_G6g1A1vFRmA4Qtuua78NpxhGswfmvJVbTfklpkuO8Gq5Zd6T9a7_u9EoaurscLmDoedx8zNlV64aIEqUj2Fq-KpV6_GYCeoiR6jINrvmHLTnzcwt0gFtQtCO2q-chsWdnUxaewLzlLeSrVjSoycccZguFwiUnNsXHMXyHI_bwSyq3POybtWw9QtAZ2eegCSw1qzLaks-8OwhVJw_MXwMNybOHhKfEEa8J-muOL7_MLUZZ8-YIuW8lFZ1X35p22R9jW94SKCxfE89uKmCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpa23VRLa1mVPt5XjcEggoE13_kSvL8jqRLWWapbhRVM4K3QlOBNNius9a8ksx4EAoAiNpYzg1MzjgVqO4yB4IxJoQ_An_TqhqKtrgHD_QxFVZhT2IikrnJ_OZgoQtqXyiSGkOob0peyGwzcr4tIigwlY9KHwapG2YS_PG1bJnJk5PgYKSe06_O7-VBROrwj_dFhlK3YOqgMhBmTnFFr-LTxn4dqDkaB1AICGUbKSB2f3FTKCstZFWguySQXa2XpSyFbFttYBCpvnFKXad2yTLq4yGSe8qa65k_aWugxnAHzw-5iqF2cbnKJT7I3k5bc1SEeYjUBbmEHf2hmzvUsjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0QH5Y0nzYtYCVOAciXmytFZvwPTWdtNUEPOHeiHMKe3dLkRpxedGAhuNJHv3jBbYb8xNkvnSNwN-kqFEVd5bj0o-L8OHehYrJW2N3Xv7_547o1kcWl2pUmdrtHELOKQW8bnQqHy9aYZBuYSeeN-Ptzazrum3lbU4EFe0iwuG0S-yzFLjsusXBBrGYeVN18cHrqov9_HLgOD9L7Uwe2Tf819qdBWGtm66oBDE2chBt5JmG4jMa-LRw7i1vBbLwDbC0DwprZePgrYzcwFHtxVqf9_HKq5wyXJgiMT-qGhtLUA4K9EZit8gC_f3lsYGhLavry1G5W-zTFNKkbaBRpETg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=aBE2aPrpA1zSu-XKTmNgCbitusYoi3fSeO6lChaZ5jHUnu8XK-rInhrl3RFL45Xw8fzhUY2L-yCPUEY-tMd0Jril5JfAzzr4-H73W76i0bScY7End1xRXXCgPlr1wityh7ThBdFYpX9quuW5WHoAv3DJcqctg2pCizwzjHCtYcdxA1kIgZRq6J7_9lhuX9NLRbUD5-sWHFIRJJIqfRiLPwDTJPAGG8F2y3uxPeZNk2K1Yh9sllNjlIAvxH-hkoRRpL6Z-Tzk6eL5hueiA80bueuTVtxR6fkOpYL37tTHYv-zwXK5A5tVJRo6uAUB8wISp_88jI43LfFUTZ2JJVXQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=aBE2aPrpA1zSu-XKTmNgCbitusYoi3fSeO6lChaZ5jHUnu8XK-rInhrl3RFL45Xw8fzhUY2L-yCPUEY-tMd0Jril5JfAzzr4-H73W76i0bScY7End1xRXXCgPlr1wityh7ThBdFYpX9quuW5WHoAv3DJcqctg2pCizwzjHCtYcdxA1kIgZRq6J7_9lhuX9NLRbUD5-sWHFIRJJIqfRiLPwDTJPAGG8F2y3uxPeZNk2K1Yh9sllNjlIAvxH-hkoRRpL6Z-Tzk6eL5hueiA80bueuTVtxR6fkOpYL37tTHYv-zwXK5A5tVJRo6uAUB8wISp_88jI43LfFUTZ2JJVXQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLPhkZPi0mRYqwMykUfQ2QeAZ8aUAupC7PHYmNQxWQzEExlcjzDQpSaJ5QZctnssFlxfo2ed8ZDz1EfmOdCe77n8kZ3lE_0HgGZvUulSqunahzse-4GqWUKug7MpBbdbEyKgdsWLD29PNKZFkvn6L1r_nWnqJ_XOwO9cFs55R0MVnSOGfRnCht_TdJ9b8fEyFhsApPDvhmzzHjRQlXojhkkPu-vNfgME34XN8IrC2wYOmMxX0vq4_BTPCnCwswmcOhBtAd77WGhlyw-yEbjCyiAagykDjqEHvET-xZR0lSxExlGNrQhMIpjLxFKsdfpg7RDPfZXh8U1Chvyw19Jo9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBAR6UbiFTRmBE9m11BRddrfMAhlThor8zKvTgGxsK0ogxaIEeoiWrk23FqUm57uTMzvlAROO36PbBLcGBoiXSxq-GTRvnXIS1b8D0tnMxTIkioPXnI99X2xYy9Y7Fr8Sq2Okl_tg9F-dBe7hN24Weu_OydZwlVVGNejBouCn_ZAwrPVOyJaODEHeT0qPHZ_sZFV_an-aFgBOxhpYXQckuCy6BKE4fRTOZ44qL1X55Fxbt1ECe5hEuUdjY7ogC4Mczoo28UIA6sXsr8gZKuS4G0qkNifs82KAFQGuo3mKqbEGpMf-ZAngk5E2b1r-1CuwDaCAXYB69An166eqoP98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWy7u12EdwoMYJ3tYIQqgmdEIJ8kXLNuC2JpobuWh_ELGZVvv2H7YPTSFWn2CQI1I2pE9RqlgXE45g6Fy7PTw_FffekFzLBg5Gq03ihFkj7zZSO_vt2dqeY8nIApKPfQxB66ccMS7oOzkqES9tZ5cmwnDZlE77zrPqyFKuqFED4isgeqSu2T3hDEgPQn6Z2FRgnff2xQaXGY2AkypIsByO7AWrRTbLfpPHG5qWAziCBZybT07HzqJMtEIQG_lUoS8AVDaXvT83WIAvE8SrbPdINWSKp_hFWUZjWHFcB7Y05d53WWpdrPNTK-S5t44hpw1OGzgOi8lZ7rSPt5Jo5SwQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLbASC2NtSD60FOlxcDJVxJCwB-UN0H5ZcICnWPCE2meM1UP65dioJSpanGLbuBzv5OnRpgaORaS2nfmEOrmb3mnlIaFGx4toj1raAPzLwXTXOH6xXtmKYrCsTEpkh7lIu9C3wVJuWdf2eX1Ye8Y2bCKCIeHoCc6lxKqeeosB04DA78YwJ5OevN7d05VxP99D2Eb2joR1dRMIajETNaKeI70o87I16CEOu4wDGs4iK-LmqwShjWA2zKSgDWgB7YHpwCwIC1ChvbfrmW3j2IahAbqz4fW9EMCokmtkIl5rYmdX3BiP4LiF3BglxOl4mjtOUDcl65wsnl2CBi0Nw4tb0gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLbASC2NtSD60FOlxcDJVxJCwB-UN0H5ZcICnWPCE2meM1UP65dioJSpanGLbuBzv5OnRpgaORaS2nfmEOrmb3mnlIaFGx4toj1raAPzLwXTXOH6xXtmKYrCsTEpkh7lIu9C3wVJuWdf2eX1Ye8Y2bCKCIeHoCc6lxKqeeosB04DA78YwJ5OevN7d05VxP99D2Eb2joR1dRMIajETNaKeI70o87I16CEOu4wDGs4iK-LmqwShjWA2zKSgDWgB7YHpwCwIC1ChvbfrmW3j2IahAbqz4fW9EMCokmtkIl5rYmdX3BiP4LiF3BglxOl4mjtOUDcl65wsnl2CBi0Nw4tb0gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVr9McDfwA-tIjZWqIzg_EBIJKEW6ioiDf0JsF-vJP0rfsDoZUz2snIeAwYeJDLWvjhEZgwJe7NIZ0LAwOCIM54peLPpOAuJgXKUEY4DOX3lZfIigeu_AtXczzLSPfc3Ce-2ioCGYn9E0SeblE4q0we0q62gkBOVnDJMlMQAlFA-vdsmcMP5anrRtnmpCntnAqeMIFHyjdxnzuMeYlsBmyOl37VFdC4FF5AXsP-OvXwX2MrNyCJav_rhWUzJ_43ODzOg2ivyyA7nhpgt6WjEW56gBHZorbiI3nAu00R7q3IhADDw24kXjp7jCn2ap8DVo8uKjkf9KAUsWvSJl46JOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lg3y4M4ziUf-1Plte0QGl7UJcMTK-PXJ8iPeJ5gVA-f1sAERDiz3CNZ8jcyUf3RQGaGjJnC3rDQYIeaLekfsWGrcP1qBz11pzY-dmVSUlwspqa1IIx5LxYgKbW7CBEy_YiZxPjpMT8Nj_pJoBVhOyyr81ZqmuTOK3ZUkssbwwwSBQUMPYt210DUpyubF1ZyyZbwO_mWrZdp__IGp-HXwPC0iGAeBBLmwu5oT5uiHphz-nRZjXZOs9NSTS8fYDCHaN93p4tul5CloZdZzH_5tHhg3y1XHTNcYb6wQmgPuW5KW2zqzewzhUBDn_DaG8zhSDNfpOhsMPsFp4-PO3a_abg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=B2ZmLxq9cO1AsnL_9Dx7NOBcaD0enuP7E6N_qPsmnkGfHc__FFRVe8ioExwIDsAhXfPuN1Tq3FbrmGsNoVPbgDywHb-1KxuW3K6Qxy_ycESVTnFS8sipDSvx9QL0h9R-c9hO_zbwqeXnQuqZ7-NxLruXmGvwKm0NuhUWqC39TjGZ9sMpsZvXHd261VQc1-M2kogcl9BOvKcy6gIJb-fMQQBXYtF6vRtY9SEXF7AQm3bdi7Oidof_o9w6ewE2rNOgdyS0HP796g3KsuwGmLI4zoCScZ3Ywl8gX5Vttwu3Pxq4SsmJpOoinxIZS46U6AflZpY_iDgDfV2hrdK4mdj2aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=B2ZmLxq9cO1AsnL_9Dx7NOBcaD0enuP7E6N_qPsmnkGfHc__FFRVe8ioExwIDsAhXfPuN1Tq3FbrmGsNoVPbgDywHb-1KxuW3K6Qxy_ycESVTnFS8sipDSvx9QL0h9R-c9hO_zbwqeXnQuqZ7-NxLruXmGvwKm0NuhUWqC39TjGZ9sMpsZvXHd261VQc1-M2kogcl9BOvKcy6gIJb-fMQQBXYtF6vRtY9SEXF7AQm3bdi7Oidof_o9w6ewE2rNOgdyS0HP796g3KsuwGmLI4zoCScZ3Ywl8gX5Vttwu3Pxq4SsmJpOoinxIZS46U6AflZpY_iDgDfV2hrdK4mdj2aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=jzjyHo1tClOZwVptN0tKYKc3wPJmlQlt5rLLYJSf9qKHDklFTnVr_xWrOUAaUGzNmcgsZ3-i4QzpaOccKQaXxdRe_oAYXcyCpucEm6vDU9w4m5Pvuj6MmfEuq_9_sJ3wo6LKbl9qXdn_9sR0tHy1ebtylvb8MLk9VA78pccapSQTZjSxX9AF7frj6P_i7-vSlJyUOyekxy2aSbJOVolFwVam35HQr7TPxEgAsQosCt7GahFMaRmZeL8HdZ55ItGpoT90GDR7aaIm5AAtbYNLeHJU5Qmhxb9hTd_okKlPwO1S5lG0p1xUfXlgzD3yMX1aaWszrKDGeXi3a6veBoIjLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=jzjyHo1tClOZwVptN0tKYKc3wPJmlQlt5rLLYJSf9qKHDklFTnVr_xWrOUAaUGzNmcgsZ3-i4QzpaOccKQaXxdRe_oAYXcyCpucEm6vDU9w4m5Pvuj6MmfEuq_9_sJ3wo6LKbl9qXdn_9sR0tHy1ebtylvb8MLk9VA78pccapSQTZjSxX9AF7frj6P_i7-vSlJyUOyekxy2aSbJOVolFwVam35HQr7TPxEgAsQosCt7GahFMaRmZeL8HdZ55ItGpoT90GDR7aaIm5AAtbYNLeHJU5Qmhxb9hTd_okKlPwO1S5lG0p1xUfXlgzD3yMX1aaWszrKDGeXi3a6veBoIjLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okpZnsV5praDLA1qT8pNEo-Kulp6vSC1LgUoV4PZOHcak24YqgHY1zQd2DwmEuLZYJ0vg9AHE3CsBBYAVOCMTk8WAtk9_4MhdX2lWx3ziZqxRbZKgoswEgQ9u9BCrsQj8Gvryn0Ub7R_zWWp8YQwiGQM4AXkaH3je0OrYbPUx5JjRfIyWiOMpjFXTSFQ6uK7Z_QUh0Ruk5KZTFBdCVb0o2jmIiiPN_K72usvUiskRaXqKbtFfraE5PqXabS2FsAq7FsI9p0h81QCvSzrizkLfKGj33Z-UVUBr2loHxm-RTDsWyawvst8-cqMEC8h-b-JhIpy_CQj0eNDUvv_qOsmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFRqv3NyFFapfrid1n_s1Xi7kxJjtBQoDhzIcXsZl8NQFhJcIQuwQIwibgwbS7_C97gXSrsjKeluQv-CmhzpOH2_kyKwx3_4VrW7Etad_My9tDr4ac3FNjouW8Eg6KSK9xMHqzGf4S1oGmHUJs7ZCNRg3hvOW6lMsf_iTFReikWrDtixBGQVaYsZ4k_8G36VGnFopZAMFAbGj2JuBV8Q8vYq4RbF9oFfKGZRJ4XmCUeGrtctvKx7TTDlUqtqk_WL_CcpWoqrms59UTCKYSPLO-GxJ9UBKvgQNBs5_nZnqA8vx9ZOuUPt7nRxR-8ZFkBKRQSOG1eznNFUHmae0VJiAA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=k6RnCpS9cIAbo5RIST_7t48L4skN5aeTEIKZAeD0yYPGFDSFp47JuFTrZa4jNcq2dGtezwFkMbm_9PUnZcEHdy_57Xo2XOOgONdof7G81mrEE6y6C2I0wzWDtSph0COo52YH_sEvT1HKQVZ_xuCKQFXQlzQfmyct8PTpIJT7addxmmZ5ARHPeC0QZHKVfehKrYRe80S7CbJDsHoGVKzIl9zo-XwuU8jJ7toIlpFkf_KNIsHDtyHs02Jdnex2HrxVZXpJzzsMEJH3F0IlTnqzJ5QxUd82rfNGPkD3Ysoe_UcpzAiJSBJwfN9MB0qFSXtr3zf5-69YTFHlcsSecVq5RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=k6RnCpS9cIAbo5RIST_7t48L4skN5aeTEIKZAeD0yYPGFDSFp47JuFTrZa4jNcq2dGtezwFkMbm_9PUnZcEHdy_57Xo2XOOgONdof7G81mrEE6y6C2I0wzWDtSph0COo52YH_sEvT1HKQVZ_xuCKQFXQlzQfmyct8PTpIJT7addxmmZ5ARHPeC0QZHKVfehKrYRe80S7CbJDsHoGVKzIl9zo-XwuU8jJ7toIlpFkf_KNIsHDtyHs02Jdnex2HrxVZXpJzzsMEJH3F0IlTnqzJ5QxUd82rfNGPkD3Ysoe_UcpzAiJSBJwfN9MB0qFSXtr3zf5-69YTFHlcsSecVq5RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=eGivSoVESPnscln4T27RLpXc4MPcfLnfAbFdhPLpkWetBdt0DFyaIFSMQ_xq0GTmlz-4CjlkUHbU3LqIfZNNlhXhtRmPr8VDh3BlGlzU67IkcrlMDvScKsaZ61n3-xDfn5Dqj0wjY31R3JWHJeEo8C1yjp99nkmFGMkIHdtd_FcGvWfU5HtJqr_9qv374MwK8Y2ajSTSa0qJh69578ZohfcszskKgvhvg2rIS-iN2ewBRRnUdxzddQicAcQe1H1NXr-GL8GS5tRUT0X3owRZb7QJqVlFD5tq6her0UtjU_FvQ_0Kqy8CCHL5E1vVQWXopWEOKto_SdnA4XS-xPvfyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=eGivSoVESPnscln4T27RLpXc4MPcfLnfAbFdhPLpkWetBdt0DFyaIFSMQ_xq0GTmlz-4CjlkUHbU3LqIfZNNlhXhtRmPr8VDh3BlGlzU67IkcrlMDvScKsaZ61n3-xDfn5Dqj0wjY31R3JWHJeEo8C1yjp99nkmFGMkIHdtd_FcGvWfU5HtJqr_9qv374MwK8Y2ajSTSa0qJh69578ZohfcszskKgvhvg2rIS-iN2ewBRRnUdxzddQicAcQe1H1NXr-GL8GS5tRUT0X3owRZb7QJqVlFD5tq6her0UtjU_FvQ_0Kqy8CCHL5E1vVQWXopWEOKto_SdnA4XS-xPvfyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-Orhs9h_nbmCmG2M52g3j-I3Rkve3uAIaSHO9GwAkJO5L32itMULcbxGLdbMJKJwLx_wTDA-V2xaNSt_raE5KfXAV86jjWalD85EAWgALqhmncL0nauewNqwCwAQ7mht3Y5eKBqQ6eAPq5PnHb1i04_ajoCSIk2u-8di5I3Nm8nc0ifdKj7tPP1YWO2olLPnHFvI5pQVPrEytMc2UPvULMJdYU3n-r3bV2nJoEHEmhu4EtgHk9EgIydgfkFiFLGR-Gqbbvwo4NhiTeF8uqzoHFR-MlnkA5QXhJAqvUxoTf1juPV_lMx0U0U_T311jbB0DN3-4Uj9jy-HeZnmVwdKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTxeTkQelFM1oKyhLT4wMNcZPQALTBfeiEU4HVG2wVlIY7-pzUacvLlkAUuR-OyzVJRFx6aYQx_cVEHRrSi_2oKkDGmbjq_FJboMy3dx-4KshPa96Tu76OvrCQdUtwHo7uxX_yYk5C7rQ3zgkixHaeMHTARmIMqIYdeva8xq4Vvi740DRluOVoCKR0YEYBU-3d4XFq8kFUHkWYdHKCPKhjOURp0xPNkLT1WS4NGgiW1I96Q8fOEDU4Y3wj7x_HO3VS8NzL4cc46vI2dZofuD8hdx34UD8pzn-w3W8v51ZuCWuWmyptyWOLEVQi97dQ6UvsylS4v19f6zWzXkb1FQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvZLFHDlTXHCA98Tgic84iOcb6Gu4qJHPFRB_1QCbTdVtw1KY00rPycZ9dHx_L_pyCc41732Cj1fizG22sQyf2AEo1SXnfCqC2TIBBSThBFLo7atk6AiW3v5ua4wtl2w34ANVxreXg5dbdMERf5tMWi36zevP7Yn3HyK27BfEP5u_L9qOeCKBTrFn1u-6GEtldNDRuhnUvgK7CJ4BwiZpWkWNr8-BnruZg4GfMYgSb_x8maXLtVXjtRbZoJjUu0fUNbSnpMN7_ShbVhYxvI3n30cS-QPrTFvVKkaHBFPZVc5tZc0XGDSwviRCTZZpinQD3cY041Ym422VeXeOim15Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnP9DP2fC60rEnb2fXZ-PwUBrRjmOuGpg9_AeBbkAGUYporF_oP84RpDUQkAIm99fyMh1kOvfbyuI5pXLpJNpclSPRq9F5WFSUZrX3xfXl8YUu2KAfei9DFK7deMMdxC_jsEOa_dGmyenyPCT90g6ssCO8zu6_XWU72HJJkgtpVaTLR6moPs1bAJcaXbDycQGGcq9z2SgYbiOzMT__b_cgwplX455yLlAhaIwMlBdWkITHJjR3xz_U1resx2RerLvo51QR-n8rZhFKAXQHJP-dMn1N0FX_pHw5RZ9b3qrM-5EOrjsUM2zaQay6A23F-N4pcDZzetNZPI_aOdkPs90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FY_gPIQXTdwHpZEnqOhyDnpjfcVDGS7Zb8e-2nWSWvmJ8e2BJ61ErTpLssicXZ_uCA181x2qMld5lXAwUH3SUwlzao6wEJTE5boVhllYFdoK1HsvpaQixB_m6XNtX3Ed-Foj9suZSXakSkd_iYyR9xs3fw57fOfLLCq8xSJlvln-y0C_sYL0jXz8_Rn-r-CstcO_Q5dOe_9ZMem2rW70QduijRv4VH0RckTzAPyj4CH-0rnEosoxMkaMl0bHwpaCAfIHgvm0Af760ubDFt5KRAjnEdHBflcGk_QDghHcV4G55j0f89eJV2UW2yZ9tP6tAnLP6e-TRwxX82GS2TuPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJAEPoNESSkEaUKXieXJoAte8SrfreyyAU6NgRyST8yya46pMKHeWCreI1KwcJFHgEQTTmR9jFIJbH7wVvfmHviViA1o1rm4Rny6-t6kCzqqFI0THhWkBntqf91P-xkjmrWR_HLn5So1-ZLOEKP_W3-LzV7BuyxCehqnJML7UH4VifYLE7KZHaGUzCqjbMjsR-PzPmBbFJCCzgIaWxvPbHb8lKHPAz1mjYZeUIdLk7uPcJP_aHnZ3psE7rDYy5nBhxi4HtRJqIEwvNww8t6gjmjo39HrVhBGCxDKPMomrsOaoCipj5e3rVafmUIdxRyle_xF9LAX1_tc_r4h15KwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCNqOSxqeFsGGBBITy3iCpW5Zl4ah24h1tfC6Pm-tTg1jyro8uQoIbnBw3UAHBg2Ccw4ooVz2AzsvcSdaOg2_CIGYGKOnhjkVJiigm6L9Vtcu72CtzRWXg1C3r0iMZ46T7ETDC3Apr27PNALITHJidL1JUDOhUnhtZHNlwaXmLxf-DT2CUlZrPnE_rhUSHUvchD5pbk0B-ZsCn8BiVDCA7_vdEGu7PIn_Uk_cCu8vNQFrlC17XK6ZmxHD9X9waZal99qfrrhcTdGIkOFOn6Zr-f0gVR-LveE7dUNa81jSDCoDRZRtchrxNFCsgve0OaA7KhnmSIhj0acqEHm_I4MCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vk_t0vOyKpNYwHRKnjTEvFe5I36ZM2RXK4XeyPuJo58HJYr3omhPeFCoCkwUa8cAHCXGflL3Iv-7GaVQmAzUHNHwbnRRlI6DES7BXjG8SmQMGy8LZ89bCaI1pliNYN1hXSVzT_QrcU_to7WOCFf-RhnG4vmiuFjYkw5X7EyQ8leclwsNwULS5o-etzdItCqLp3VkyMbBR9DZrsTyI0CslzE72lki9YVF5JQAwFhlLvrLjXMiBgElTOQAb4B2ubXI8ihfe66uaal04NoLA_PflcxuzH1sb50E_6XRj4Ua-FlAYI0_6nKjb8vBRkz1RJ5COkd7c1aNn12O5NZl3S20sg.jpg" alt="photo" loading="lazy"/></div>
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
