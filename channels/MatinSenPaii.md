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
<img src="https://cdn1.telesco.pe/file/TIyT00qGqQtO79bz5tx2Q2zxmRC4itlI69oh_bCZzW--VS0GxUeBR0d0-WcQblrLM0T1MrLYzWkeTFLhGvQLw2UuZIW6kS0wN8G6tQjZAdXKBuYRtPohwKuoDkm84AQj37hjqpysTEhK2KrEmN03yj-fxpUH4sTLaQDsH7lw6xPNrzvmiRK-LUtHeMnGNtKVzcXhax3XZ-BjNakx-5D6OiqVGCRVIXmhgguKDYnbUlBltVBsXu106LJ21Ta_5_M3NHo4uJ3sg0Knydf-NHqKlOfkM-Y2mxo1kWziZ46CEf4gS2G3ZaZ2n_sW4H6kayNFTbAYh_hBzrnuhXO1bIXnpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tTW5qVFVHmTPwy3lwJj5IXrsX21_iUFn0Mat8VXzORTSP4x-mKl_c3ikCFT8S1zl8fD0Acp6L_yFZnSF6WQ6SfdSZ3OuLwqBQPUYeZe17qJynUxdm532XoHJJoJuZ9MI3YRimiTWs_xNPUaJld5-MSnofsuxt3nXMWMrSccLWFQN0oRaVsJtYVprKfe7JTkK7JHw3MiJvggmzo43X-_OnKD-1YoN7n-5xO73nN90MQomlK4cTcV4QgnCOACo4zJ6CwOsrQqacGdkT8VatL-IDJnr1OHaUMtQZ38Z2ANQAd1RvR4rdGeOZV_n_5n1sLwPKz-BPEXb2hYS7O3nTuQrHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ULJ7EV49LB93fTvXFE6J3zOJH3WfBLmB5HRGeGfH_7gg-zLMCM0OWOPZTpk48ljcGbtNmeagGpu2OUa-STRWpN568csqJiqLnPJGItl9kOf8rVGRH8JmYebfZuejftLNUnJLa_OoukLJse-lL5wRtfDEGr7U391utnx3_x2kfUgQwNDII8DdRVm19IZYsGuxiRgVgN9WJzPar6D-O0HFeWdlu7qXjLTXF6Ud7CMNA_q5przfucdBUnjaYrvJTBjwHPt0I9dJHOxihldLcOUONmWVPV9p14vgRuJz5pa9HfHCpWXbgKgVR3wTEsKLKGxKk648JRhrxPmXyK5xaaDUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIqLx3xKMgFtHcuICPnNCAXZJGxMsfPn0CL-5vVs7G7ee7Z0j6xMN88oqEaYZK9J07OMRiv_SQTj6r6hwhNWgFYum_GrgoQS_cc7zLHJwRECQeEkaUegMqJhuDJi81w6x_SeS3jRd3ORjD5ZTa1TJ7eeRSJZdGKmhcpOSXTkYldinvkYwwm7sf60jgq17e0cGKEJg5-kFKyVjQ-Kty-qIBtu5xyGZNsSIIW9GYPQIcxZvDtqXpiA5CxEkuIeArHgj6UyXx6niwGRua9ZG1tbPp7gdQ79M_EeNf8eSZ_5cG3XhQI0CwHMdGHzvbBUY8OQMuyMUBsmt3LC3g13H-7Zrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aLom1K16ZLD0GaQbIyKxPOc2ZnNI_zNzeOrWiCMrsuJZA--9d4CdeRaEpFovJ3R36RQg_piMemgADnmSywNyZhiU2wLYbjwdMCVLxQFTCS7fVX0_V3_U0uFIR_TRY2_UwKqg1c8iOTn4plLSIR-fLeJuW2zPg4AjKL2Mc79wB7kO7lwh_zQav-t99ECld-ZLLCu_O0_LiWs0p9WWlcWXWgNQT4t9NKJAvxete8x8f4XDC5EJEckl_99eY4b1FOknlbqnWvzXFkT18tclVqj5ZGkGDV2_oFQOprc555Rw51lI0VmIybRhebEIBbR8_brNWDV0PJqJmQJcWkjMW998Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Hw6msOYoozgPqX08HkRR3DL3j851exZfgtZmtdETUhZ6pKXdcmrfHPMwO5oiNlBzJPVdXnw7e-IPLs-BsUi_vbRgS9umgAfs59zvN3ENyS8xviua4YJcDXG8VhVOgYZDNItr5EAx0eXuBrKaTvQRJy8wn4vFAen6YlhYV3M724eeq5YUxv9NKe2UXU9YQugvz2mVLzqlh1sb6ZxRVVSzk_4h4K9j1cYQ9BeaRE2SL4HGVt0A89Lx9RGgXWYBUl9v2pgxUIDhnSRHOO8ZEPNP64kpY_Sc_iiqjeP0uvYEXJpN6ndYnRYxq1lwKLi9-BUA5OtNMjJu0tu1MZQiSwaoeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Hw6msOYoozgPqX08HkRR3DL3j851exZfgtZmtdETUhZ6pKXdcmrfHPMwO5oiNlBzJPVdXnw7e-IPLs-BsUi_vbRgS9umgAfs59zvN3ENyS8xviua4YJcDXG8VhVOgYZDNItr5EAx0eXuBrKaTvQRJy8wn4vFAen6YlhYV3M724eeq5YUxv9NKe2UXU9YQugvz2mVLzqlh1sb6ZxRVVSzk_4h4K9j1cYQ9BeaRE2SL4HGVt0A89Lx9RGgXWYBUl9v2pgxUIDhnSRHOO8ZEPNP64kpY_Sc_iiqjeP0uvYEXJpN6ndYnRYxq1lwKLi9-BUA5OtNMjJu0tu1MZQiSwaoeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krq71bp8GnMh8HvXRa9lv8XsSRKB1s-4AUd396-axFwORJoFHEQCS9kHBzoGGKLjlbkOtzGcPl3Ls2v2UMK32LLtdtimXRC3NoJWNFYnm7042eXSIrXROmsuioCT0OV-5kq9z9jt_ZrQPE1wXATuU2gJbjFvImsu6gAIG9wn6qz7Wc6vOfE9JAk2x3y4v538tlAMiq1orH02BYnAzqsoZKfaqSaHfX3QOelZG66M8N5Eod__IgKiemBut84MIeyGxeBM0A-1sUd3JDmW9ZBbKbN2qY526Ij2fsWAb6DLk-H7gi-IFffAOawpidcwbzRhBz_pYvFck_D9Wx7Oare7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P9t5A-WKimxjRMEIyCVOHfSg4zowp4mIJwHGFuYO0AtAGVGvBqWAHB66OtDQNzpXnH8igoV4WGF3vlH9UC4u5fd2P225xEcLMfRpOAcSDIsxpNP-cjD42pmahleW6-BcETpCPgAhpPXssoxASDuAXJI_6obHNTjDFyHoPdBpg_i8-1BQ870YPi_4WKHLK1Fg_ukvTdofIrEnJaOOdsW2d0vGUdC9_3-bm74wrWAxJBRsdOm5txX7TpR0G1qiDHTSrywSNc5fivCvI6e2mZ9521IUXfRM_3N0TLp6jUIJvauvlUIdiC2xhnmD2-m1qqa8PypTTSl23k3BX5oXUaQSUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG9qBvIGbLJt7b6v866ID4KFDDtadFQ4UC8OtOm9c03aP7dwWTYeB6Bk8y6VkizMSaWJQj5FERhUix1xoFeXODOQnAQqwSewNBLoYuP-BxoA9Dk-wI_CV3lhSMODHWjLHKT_Tvw84QSTuRTkC3oFga51VRnHIkVDIhfMxCfCmxJeAl_gpSMDq_CXBu9deTn4tHuSp4570incBFy2qe_uCcO0iDnXn4MOtcpwMfDHoJGPSF8P6lk-V58Z5l-VIZAhNV2lphXf7QKMLOQ3R43x1iMz-YHwr_8t6huE01-xrzcAQ66qQIyfhShlRrBtLSRrXVauBffblwMFr6DvVif7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=f3KNbfCVDnbqQe35QPZQQlBLbkq3Mo1Umjr3c_EU9cFzj-CLVwYBpyLSVC7na7mH03TeE9fUkavfJNX5iZ-9sn8qDonLrRVwUMvmZvXZ36m2Attb9uI3NqgxhoDPhlz05Q-wMGHihd4rGHh30AzBS2xzIj_fM4nDRgBxC7kraQi0jKxv4Y9xe7zYzObQYRlrWqqcLXcKFfJuxv6Jwocf_G22ClaepVttjoZuKcYBMKKhSYtjclIyqRmiUWElmOVEAKp_dXDICiW8tAd7OrNvAlJKBV0MznsfTTL_D01pfYoJ_2F2cmYc6nZcRTFJP5TsL7nciQ6VJElaeS-ryzfbwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=f3KNbfCVDnbqQe35QPZQQlBLbkq3Mo1Umjr3c_EU9cFzj-CLVwYBpyLSVC7na7mH03TeE9fUkavfJNX5iZ-9sn8qDonLrRVwUMvmZvXZ36m2Attb9uI3NqgxhoDPhlz05Q-wMGHihd4rGHh30AzBS2xzIj_fM4nDRgBxC7kraQi0jKxv4Y9xe7zYzObQYRlrWqqcLXcKFfJuxv6Jwocf_G22ClaepVttjoZuKcYBMKKhSYtjclIyqRmiUWElmOVEAKp_dXDICiW8tAd7OrNvAlJKBV0MznsfTTL_D01pfYoJ_2F2cmYc6nZcRTFJP5TsL7nciQ6VJElaeS-ryzfbwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SA82HIawR3InAMCe4z0r2QopSiaSu5UAxJW0WSOTgAyowCUYc8g9EommiHcFQvG7YXdznjuv1pRIsTOSoRzRkGpEThPSgGbsXXoU_hy4r5Zs7DlYZw-RT0tP9Rxcq3ABVsrzV-6EGGRpteLBnHo7au9D6pMBMuQYVYQj5cmz9n2vY4NaroYM48lCrsnpnMv8l37Kg7GBP4xnNPfmZHpo0x0JpS-q5dQAjTPT57kNvdU-jvFyZ0n58HWadfeZGjMHwyib81u3ZFTJUUGSeEmJzyIKP5F9YETNmCVoGyR5j8vFnMLzH6AepElPFo2no7a8BBo-3pd6v9iHXlt8_7FPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5IAzhVGcvL50pDK8QTwyDGvH8VoQGrXHlQyrq-nlZSxVO5ZN4dN_1J8lAmzpHOVtMdlEWqPCgCpPd3r1X--MH_Pm263QlGvw9KgkJiIbM0eXnmOSQnxwNClmWmaQpdlJCdTCSQ7-vD4ufNovD7xLN_yKUp3IOdvkgU13wBSuQP_FumlzZQdZo93P4M3wqjMqiSJI3-NTA6gE_3Lc6NBMGaS-zTZC44XN8MATQqltsKMg-oge8226VaLXGAHO3WQ35iTmAZRrrVRHZskWBm5EwuRtiA3OsfzAB8KeWhgV2tSG7b9yH1698Y_bwkIYChZGMl2zxHNq1dxYgpbBoT_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c9rBLBmeUyefmpV0mz6jCGvC32_Q4-d9uz_WCn3PeC4rdddmE1IKRgAP739FXJwSdiTbwz806WIIhWH01zxN11vTBgso_mneEoQF5c_zyfUQjD1yGnqzGZkzIrt9IfYoAE3riPKJqpiQ-U0PlS2ERk3ATLBwc_gbY1W8QGd3Ly6Xy3KKHXiD2sFzH-YLH3x6y3eT282tPd3IA08PU46H-2yT5E6AJ28oVTgWc1YwBWh_aLaKJ2-48GwSZvgq6rgRQILJRjNhb-YJgUt1w4lvohZEXJFczmNJVVC2n4RZfaXGEaika0EHaTQrANot8ci2CPqf5gddxvd6mrfyzHiAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ftrNMq0vWExcE891ZplDsVNImBDy76KWJFa701iAkAy5ahmgfomMR7C3gB4bPSlTinITu082ZbQVaQFdjfE6oxfR-vpp96fEvGYlXgT4CM_6jO-xJn_IcCsZFTawtKM6xxGnsM5y7wWrnsa6savisXUhX4zUQxTvc0Zj_exA-O4m_TDJHQcLXSlHDbacx9Y3BdDsjG5ze2eoLnylxBKO5RLL4rXf9QYkD5TQFMLzcYNOneTJdpr4qY21oAHO2u1oz1KqxkpcR-nZHEGlZ8X0N6ML2EgyVYZIjAOPlR5bz4ackpJqe7aFddgGTXt3HFgPLkQxFdNUclzF4MdlAC4rGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfA3FcyyUF7pB16YJhK6ccvoWLUeVBn0vxzp4vLQ40Xjd8lnbJLh_0FIkWFY_4qpU0He4FPzdWG3-hYwH5M2UVruFGh6KF2U1zvYuRW83NBqEflQC2xO6upICkwzYVzWx0SqTwwrtG-3LMmn0YXpnMNbo9l0zV92wNCcofdhRNJvgkcQV4Lf3bovLnnFuHHj21EPzFM0roZHqa0Axp0SoDqJ6qxaFfpNd4w31OcrwiOf5Uaszecv2p2cJSmgOOWj05U9DkhZoaHYbOC_-HkX2NLHzA18HGyBXKLY3deU8EjVoCLAJYo3A8gkrCxrh6tK7edHCtMHbWjmsjMXPUT68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-lwKWwjsqkmwYtJqNEVbUXf3YeO9ACpE6WyHZnEtMScKr3jpwYzdNM7W5LYk9z9pzX_z9FSx2mpV7QcEsLL9jJMbF2wwjle9F3IK91Zvo1gN5eiF63uJ2bIQWGa2X83kPSIx0NAr3du-mDI4D3ERpCyp_IRe2UsWjCPljOygYjaNNsUqRSC4dbPAw6t-G6VQiAtXCv74vC_R5GNo76SQAVNooR2bQJR4qQrgBgHDn-OXSyWMcCDsDpAxRAXIN9T_WYsuk4Skt5OkMQV1WQZKkX7YXBpJVsLV88hDSSsyAGDfFtI5S06fGPUFKqxSS0KVMra1h_wI-HTgf_LnKB5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=G-giIuPZTRKRxW8VlaxgqVgLzFw7RPNtjn7t11qAEQaEaB-Z_iykdrJ3eoScW96wE9XbazHc-q0DFJQAs5YsL-5dBYRL4GQz4gyYJ-AazSDrxPAVdPm2vjV0hb3eW7RCV7j3rkEXo1cEVTKICEa5VY9ScG1ubWo8ZOzFpD9s2-idUD4sDKzgzUbRCcc8Gpd_CZ9CF62-zppGlw_MI5Z2RGEI1TENY5Tz6gXVNcJaLIdJAgHXtCJVysu8cgtLr5YPId0AMJDcwi26iwaldBDHnFOVWPGees2lvi-Ittg2EwBikVIUS-Y5CaJAWIfOrmBb2xDtQFTdaE9ZkECHkbRpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=G-giIuPZTRKRxW8VlaxgqVgLzFw7RPNtjn7t11qAEQaEaB-Z_iykdrJ3eoScW96wE9XbazHc-q0DFJQAs5YsL-5dBYRL4GQz4gyYJ-AazSDrxPAVdPm2vjV0hb3eW7RCV7j3rkEXo1cEVTKICEa5VY9ScG1ubWo8ZOzFpD9s2-idUD4sDKzgzUbRCcc8Gpd_CZ9CF62-zppGlw_MI5Z2RGEI1TENY5Tz6gXVNcJaLIdJAgHXtCJVysu8cgtLr5YPId0AMJDcwi26iwaldBDHnFOVWPGees2lvi-Ittg2EwBikVIUS-Y5CaJAWIfOrmBb2xDtQFTdaE9ZkECHkbRpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sTcY7kX-TyPxq0Wm9j_PUHf9btYFMI1p_s2jMQpXzdci8AtH_HkLasSfzKjRZJkJYwVxIiwKJ95vywpt-Ki1kEy40XcfDX-VZOvVjyWN65XA64Y7pcTq6Tl6cFBwxMkAI6o1zqQmJmfW9Ehm7Y_5NTcfEVvw4SMFLvExNR-RcvgSyYAJKjacJ-pHS3_AicZPEyxA9g_EOstC8q1Vk9PbdON3ZoLfRe_23xx7--BfEyKkzaauQSvSaNVSzvv7VlwHkxUR_CBjYKFKjeAlQv2dZjFBPcWkWYi6k7VgtQOH0LyxTNdNucK7FuWZNW_uM5Tz5JClt9WWA704gHPmDwoBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hMU01cfxZqYGwcxj95DcOR60DigwY5lwOLWT9ODBdBJrs6CbeZqAwuLr_MEumLFG2cOvvSu2Y4dc3svBDR1rmng6i03CoHwsTYIj6UVphqLTWICi3itMPmviWoeyTUqX4iML9e8xztDatkwyjmBmvHw25gEJanHHg20j4ZSX0JeXJAiZ_B-v7FhwytG_VQ_f2KcNdO30UwQlNSd0UMsFGhCCr38QuamG3RXBV8AaI53cxgxprg4AH_2lfvi_940zemYcVQ6UYYjf7tHXkg6CLx-LQldJy0nPn4Q7glu8rUFwSlNhHhoq5Bz9mGL5yGj9vVmOLR3idBMVcPZiFAbguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iVbKxOZ4OwwQowH2g5RI5u7LM3JY65PKtJ2JxhJ5SJJXeAUXei_VGrBa3sYM7kafF3_aatmMDZWQOkGzIEkfrAkt0ZcmO6W5kJ3zZo0lTPCBcwny2Jn6YM0dHB1E3TWav79D4EOa4Cmezt4nWPtf_4yvV4T7YD_GB8hFrcbEHGbo4y9dtXMqBlIZ7HLC3gRoouv3gmWEcYJpxrIT0kiqqaHlGx_NXLWI1dk0gOzpF7wq-rcglzD0ktRqRTi_mLl-cdGF2qECehRbNnY65LJt9SnUIbrEX8uAMiocaMsw4JhMm6IFqsXWBMvtJAQYn5uYK0I6cBD2KscAnjob6NiJ0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaHL9x5FGYDx93HoRFurgPD5uFZm1mmzRVAU_xlH_QymbEIDDs7TOGudakUtiLRHM_5ZoBa1Rz1F2-2aqgrDm9689WOQQgldOehDf0ORPFUQVfNGQPZyIQaxCKFxv2lV-QBgm5ATbzBQSmGry4ztLcv7fLmOl49QgspZrEGJrdLLcHeSQaNtpKYtS8cnDjmcBf8_cE45UfMywA1IYcWZGDrc0wETFds1opC7VloWbohwaNJw8zIbUNsUrrj-8FRSRhn6LAr_Dg_QaoBdvvaSJfGhfzKGM_gs7eST9nSv7tvqrRidVTrjUVYp8u0PwnWi3wWN8ykzwnPeg_I2mJtCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H77pOTMbpLqxTYKL-hcbAx18oouPnrq16QxQW43du1abu0VvhN8I_3dt0QXpfASKYZiVmuDbSJx38EESN0kpsm_lvSPnXb4n2PbgPsNoqP2MRNC2BBVhwPwg_ix2hJuPNEW-8P9iT4tqsDbMKFgwN82JQRrbNrm42f2AerXZ3HAk_l3r1P2DeDcJr37IatA0gtunVYx3jx41lG1_kphgXLbdXdbiKlucugaV09OP_fITLLcJwP3AdX5kjV-w35FHzMFnymCKQenI1cSOTS547lHZF8vUxvAqeF2wYXc76VBZ6ok4702obqIIN0KZwrxtrZw6xRLR2OmIWB6ZrYSU4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V82xjC13oXKQplJEiiXoOSxDkmWEDDxuYI7NrkrZjD7bfJLfrEHGJXtya4hIxNV6lY497-WUO6fdjaYNkaLq59t2YkNLvkZHIgLurnqBqhuZweKqEMUkrxqamGv8mcQ1QQ-MY7NAsrf6O7Fovy91c2TczcsTIo1HjL2BgdoleCk7JBhTkadpEMVOqrCvRn4jYF_EODQO4-WqBfPR2YHru3kiSkhmMhlFnXP3IMz6GgLemoU5sDWEM-MtyrTedylL145-3m8uLgjbBRmike96semm1EWSU-zwOS247MN452Gtra2eL_-nt36aZkQEbDuhTQ2_z8CaVNOfqkzuDYtoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AkOElaflnZ3nzEMbfJ8YUTQOBWYVlMFC-CS7k0CZGDeGkBGJJj-xfL6v13uDt9DzaQ5ZLf7InXJ3fjSCU32eyECXjGwEThWh-idarw5VYWnK5UU7jrbSHB4bTQquknUOHUV1BBQIBbkOYtdN6hEUcEJc0MHeshq1bb77j4e9S59l1-Xb8gFtZ9-bZsOUnfAqltO223IwHppNb8wEbcPkGH6u5UKkgWJK7Xe0YE8l4XZvM0Exzn-yR2aav5gkcFDMJVyfnlnMRbtl3Tw-ihAwRDL42WgqobaFrOf4rZYdvhto7fjlZIZa8_MWwyXmBdTSaXfzGdd8M4ksoubIGhnr3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S4Aa5VJCpT5HVc2bSRQk6lrhM80UozwVotWGSh0oqW4Kvfh1T315cd6GqV3davwRFoNLSIgxTINim3SguQwE8_EuaWuyUQjiNgy2P21CiPmnB_lDRyuqPJW59zIZUwxt4Hfo7_QhXFu6hpYQY8fbfACFv6dDUkkhpsuLcLiKX5N4TT-TQP-GZpdzuFKsEd7mJGMn39heNGuc26aGvcvafgNxnjSsoiB72jOgNUUq3FEXlYRs1XbU2xL1-aUKT4t5Co8-J5Ne6Xg6bUdYgNIxouXgiQWJrjEZ2uwAl-7R65WmWSme2xiF-iCty9p9vxPSJhUCC9_kCR-hS4_d0gWl7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=fA3TLby5w9sPn7DMQ_ukM_gr37VpNDS3u6KI6dAjtzecspuFcm07_451ff948JhhnZ950SJ12b7dXFosYg-et5gn2oT8lmqlkXvtr5mw5J0y2Ij7toRPyF9imLXVf8wUtHFmkRb4eFBfPFELBEP_3W5GvVNCSy3CWDioIINEQpNIZTF-gaSLqvCtCuyfA7ns9zJ4yP07Zcn99y2dYusK-vb1UVi46hSla-6yBxqOzrYndz1OP0GGJChog4AzstKdmUVQsdDew6FfuTrfjoIJHiCJXXIv-QdTPKsz1LmEEvW2HR7bGapY-9sMORULG9UCI3Vkw6af7xv2p-05xhyMqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=fA3TLby5w9sPn7DMQ_ukM_gr37VpNDS3u6KI6dAjtzecspuFcm07_451ff948JhhnZ950SJ12b7dXFosYg-et5gn2oT8lmqlkXvtr5mw5J0y2Ij7toRPyF9imLXVf8wUtHFmkRb4eFBfPFELBEP_3W5GvVNCSy3CWDioIINEQpNIZTF-gaSLqvCtCuyfA7ns9zJ4yP07Zcn99y2dYusK-vb1UVi46hSla-6yBxqOzrYndz1OP0GGJChog4AzstKdmUVQsdDew6FfuTrfjoIJHiCJXXIv-QdTPKsz1LmEEvW2HR7bGapY-9sMORULG9UCI3Vkw6af7xv2p-05xhyMqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EIaTN5Kx3fqaA6Qtmp4W8rAsw-wZMaXOJPPX3_dmo8k-OfYlpM66BK1EQOQuvK2sNDgSfPIoRfDqq7-hBOz92pS8NvkOhMXdlpydX5uwy9wirIrOoxGvSu2I0CI5MMpaew99B9xm1dMzHktTBggW5hMqeiVIurdw9Rpp5OFYjwvV994zH3-kHtLvlWBzzt6IwsVd8jbuAocW-p0jZETV_Cb4mQcI-uN2di3oQnEdOiPVCW6PotqBcvfBVWKe9jA_5RoMjVdyfiEo-LKHIlFkI8FrXDU1M2KXKfpjJMQJpZiKUwzY_7xMv8UEXxR0W6291F79ea5Ae9AcSazEf_ci0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/peAmquHbdtcAJc_jd5GGoo5sRRghzCTtowySl49PhXYxWpasMyz57xYPA8d78Yb_9yPVZ1CN4YJm-hJeD-NX30-97KU1IndHtaBdw-ww0ghBYoOh82t8TzBSvmclX52xyAuUf1FTrY4jpfTTIuRIU4Zn7vourac31dgXdiEbbbGrH7rc4SNYwfcLOGyHeYL7s7HNql7Tjxvc3XFBXQq1VcJ6XjC-uyGuJen-cMclkDRpKTvXvPIfuA-tOSuNwECOoM42qTbejCpA6UDfbCNXeoKUuLSP3npQQ_-ZDLsYXOebLmmKBaYuH4HN19jCuVvX74yNyrhIXeXog3xkiJzllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR5wWinShQJqLHWp8FPXOySlIgsZfxAXLVkY_xAZEHa_z33zn0gu4Hj-9uZFlBMt-ivag8UlO2VWZFb2mADUmzb0pAZAfs5xVO5HOCn1J3FeyujLIrU_IRP1OirWi_tGqZEsx-Xe0V1SzZrxecN5B5dEt4VSmBvvCXqx8OZ2KsAHaqOpAtEhy_s5GjhHH1vDn0lJvLkUO9JCpTFicSsmURMgNfZGJWWsOcpTC6Yn09ZhHXiP21_XezC1SfB15UQzkFKXJksbvbGH0OipbFYltmWJz6z2uTLmJoOLkTLLGuryZc7lf0qeDJyXTuIZuH8nfgimmKeR6r9kbXeB5rsoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLcI3BUvZWoGuE_D0MQgi9P2YxlQCAEiL2wV2B3xGhWx7BITIBOD6YkPWR2ZDg646bw169fCFJmv12dj-x8xvaPyBO9_OSrfvHwIJyyc97rZomJRZCuyePCDoXz0ibMVCo9Xt5lDSL0Sxd_yIdk90Hhkllrrzutq-w2lLH8tJjwFt69ojsz92jUACoQ-nRyvwfSDJw7F13lMNFKh_wjzR-bUlmPTv0Q2Ph2YBwkioU8FNrs0IR9v291JXjBQeR2esY3dHV9n_CymUV6c0HojhBZGnG769UHemUEyaTrfj8K6o9uLrNere-61VJW2ONNzbd_yaLWPQtCfILT91EdF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gCDa7wInWFQ8aio9W-BkFeLVacdU1NAh0cMnCKn8ghQQmzPy0tdUrm25SfiBocHzt0LbRAy6k1jtU5QABBgQQxg91MyDGXSsNkERFlmu2FymKq3cW3uFZq97fK4L4wbZAbsNp3jvsKZSpH5JMhqFuwK1lQ5dJh96iypQDfM7l1Iv7_YwLXqEIZuJuzBc-IS5DpIpAginMa8JYMRX5od3Y3E_kRzqBYSpJ5_ZtGbjxrZjX6AjPIU1Dd3jRTkEPOWnbn7lL5pCjzIcwVnRVzzgy7Fk4Z7of_jMJ0TZ-Qkd4KNdde1ZUFTsg4denKyNSvxzvBGPaFgYQVMg3XMczrrdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/acTQ8w5V_egirg35KkKUNduW08fQjqAy9S9jmtHTx2zPjNeCVo-88sQFUEZvszr17k9oS7qtQFyYzVX2LHOs6dyLZJNYQ5s7BOgy0bok_gp--CTXK1mPL0EQphBc7DIectpt_YD6Q2UnCcLkL5nL4K_QG98GG34Yl3hfl0W7vcLHYCFRbJZYJrVZyfp9k-EeYt2EvEnVKXBfvvGl0wjBxx032t_xj8YaKbgilTVDJIa8N80kg4LKFutumcpRvpRr-ah-064Emcfw8VukEHpPjv3065Cuoj0s3MbcbdkaoqskqSbW1yqRq_iJpRzK350di66nM6vzuwweu7xc8r-gEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LLXlk_8l_Nkg5gyYhYSTn5m43_Wy_-drFjy04OSR6tQYVhL80CVnH2kO6HIix1IW33dYJyXlz7zgu0JkWSSCkM5-07KlBGDTdDJiIOK0Dpx-lXAyVzqU1h6gKKYO0-cNWZs8wy_N3kQ4D1A6TVnNpDt_HQlap8uWBzUp88nJANTgLKfxvak5sq5RsrORw9kAHKTjueDofSujYJ0sXNQaDp4O5dEJy486N8PffLVIIx0U0SDiDDNrVo1odthQFw4hGCd5MuNLDuvNoSkfK5GGRIc1YqFP-2HH3Z_HFTTqIcXB1-5MIkcuPcbXVSwC0FudBGZFbH7zQAqUXzCoE9Zj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TWGBYQvA2UvLoGLTGD6L9L2-u8MjLUyujPwvm9Bs6isePqaDXfbdF8cWydqZuV4Ty5PcenoAyvpbGFOJtnARiZV3MdI_3BC8nqZqSqv-4gn0fGzIu5PibZ5yRtliQNiRgDZ2OMVOFXz4cH1Io6POZA_jBp9UQ_O3o0dw2InHlzgz8XpcxyTFaM-A4bD6jXw5_AiWR2bwewlnj2GAG6cFrcp_Q10AMLvPVDyRoyNRGR8Sh0lrqA2ArfS8xntnmysyHjyXurw71G3Nq2o2ePxZ1gpgSXP_vcTbAPz9F3RCh7_SUU-70obOy7WqyrbikEJ_4b-CgWK3fWETGsP_sZgrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MJmTg1GQdhr2ijUC4c6KSmEXTyI-CVjbfzXePf_gyto-4XP2Ui_DR23GObpkjuioXS1BpDIsbVlb-civ0zyvoI-40BtpXdjPuV5Ra_9lECom3Odez4-0CiLSRwqj7vlhgbj6E_uK5PvQjiJdXrrac4RXfhGaXqw3tipmDltFtTdugAwYnYJ_nPgSAB504-GxAKda4wy-v3F7w9yMgJjysTuScAPcrR4LzgJFL8RkiTrj19WFkCWPparAMLwngki-NMpnXdgZaKxCCDI8uGuXyIvkJ14wmJLPpU9SySGyPRP6BHxpCK2s9_EuJfzd0SecUlXJBVdVVDEK2LOsyxdKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QP6jjL5sfh9HkTZ6upllgd07ULlq0P3CT56YH-jVp6Fn2h56ZmfBxVy0FfN8yVt89hjpIHFIoE1KMVWxMNub5zJgI4EG2W_IvvtyZ4km4-g3UZRPfhedAWoL4kTAcBML_KyboKd9sLv4TMU7YcZiZgODKUK2BOnZXY8pY6OHHqdSzpyaA_QtkJmjkU9ggeHUYII0LEjwPLFW6iA3HHEbHd7t6GX9IC_A299jf7nGIzsdglb7Kp65OsZRiaJCQb-5lJT9AhEUjNw_fqtba3JjlCBcbAWHeos_mBsjB7Y1xOCZg6-wjIswMNrp6w_PeGJSffBJ0AOi2MOeBNO03QJLBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dFX449OE5i5ull8iCVz1zaDOOPEq9H3d-ooA6QghZo_EDrlpIoks9ap0w2ng2NkCuLyEgKhDR2GywN9vdMFMyO8J9z1dmYb_1wEq98SVQlLcFvNERLtHpB80Bdxf3S-RStFORwt3mCETHbC0iadPQ0ogbM9rgAPXbsetEwiWXFgj9e4ngG6tcV7tHTju6VZxrCvpyhS4N-hpqcYj6a9lKL4NHtlcrMVqJ1fqSSEFSuOMKMETNNEf4i6K_Lqs7sa0f1YgTb_KpeOCbxX0eSw82OATIlpmYcPoHT1u-x3FP8QOl3UYLmeLZjLOJSsRAMgOZCq2FP9hvohN7SWzKOWgbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=sHgWKtl5spzbpnghwRhGUsLRMETE0XxjXVIQzkISGxNyMz2CU2Y6Mf15gVyQ3L9G8YUWqabM46BThzMGuLeXwH6Fz6BgcTmNWjz1rgWQfSbTBJweoZJAs6b2S5btXUiHzZXldqvWemjW39utw46Jpy7eChmHNsha6p9NWkMayZwPuAR2Ep1-afRa7NHn5K4vUB9jI33I7szs6oQY97D2XPpZUzgBXas6yHrpd0gAGT0r4m9HOWCgR7Y1ikh8nhLj7fxWN_oxnYlt5alAxvtFe0SDPw6F2Z2RcL2vVTIkTUm_eqq0MKZl4sMHYOkMEQctItA0BU_PDSUHvV6AreWaqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=sHgWKtl5spzbpnghwRhGUsLRMETE0XxjXVIQzkISGxNyMz2CU2Y6Mf15gVyQ3L9G8YUWqabM46BThzMGuLeXwH6Fz6BgcTmNWjz1rgWQfSbTBJweoZJAs6b2S5btXUiHzZXldqvWemjW39utw46Jpy7eChmHNsha6p9NWkMayZwPuAR2Ep1-afRa7NHn5K4vUB9jI33I7szs6oQY97D2XPpZUzgBXas6yHrpd0gAGT0r4m9HOWCgR7Y1ikh8nhLj7fxWN_oxnYlt5alAxvtFe0SDPw6F2Z2RcL2vVTIkTUm_eqq0MKZl4sMHYOkMEQctItA0BU_PDSUHvV6AreWaqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tROdD2mRzF2ifXc-sdeRPf4jvQzYN0DQzNBzPYQNve91ff55KL8R2M-efVf3EOTWT2e7RN6D2oEA83VlN7Bug7jOqmfmEN2HCjqKlTQpP72Q5GSRFdMgpROt7g4mUsbXNPF6EV07a5tnwZUomdc9p86Em5wvfWS_cL2pNXhIdvCIucd-X8Mk1j3nbvovLy61D-WB2uM_QDcJrFWUJRNESn2rbAZF7Ls6VcAcWfrJC9NNQAEaSJrnkNYblwV0KMJOW7rcUzGWPTtl4ZphJ9DA28moj95DloOBbc58_SdGZFTXlKfgoCM31dpJYtvu0C6n78g3CKFC8WkOQTwxA1DYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c_EGq8ORp8X2nc1Q2EnnvOVvqQYFxdBvJRWP7hi46A9rRrp092Q3UotCEsjUPnNrddRjqiYVsUa0mg5guoNmIe9V5Fpj4a1UDgJc8Ut_KSzmVoQlQFBBIky62GzGiuaDfQ3tcXatPLHHLVdEUKg98MhLN5b7Cyzxn0BgW27Pf6veYYDGQHiJuf6j_e_Ms-lrrkEBPjd0ffzeIAUKKjgSyeOLg4Wl0Y48cDzEgFkeADs3tjp_BrJTH7VJ8p032uRjIogNncnqZgdtt1WMgEPSjTGE-ZgJahgnJ7jiu5W4E84owgrjLoeO5J-_5LdP18Go1H5SFI2QZMOTW1iTQnDcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WU5kljhw23NoAled_rPScwHYs5XVKMsUw0OAJ4rWZSJWtW7iWiN9Vl518bi_5BviKq2VDU9Gf1L58LnWjuozyiJTEKBI0axXoW8eGTEpodr--wjnhhP8fSvlZwkKfbOxnmBPVN2prLQD3G0ELvW1xO_sHzmEeYJyqKO68FpxWM19nYgOxuVOM_j-RD146uRUptR5Aaorn4ibe86kzz_o3ONFYaQQZHQn_9Ku_SpC3TLCeNej5b2CzENtV0zFDuNHVXcSmM5APMxoAXESp_mh8LR0a8YC8vFaB6NVscBoAERSg44uhyWyfkbOWof1QsccBi2s7Uc8xNvrrRZHOjfFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MLDmALC3ua-QmJx8-vVinAS0bk6ljp6OZJomqx_op9pQMI2wlIljP-7hMXmE8jUD9W5xlwuLrgQJY5GG4Aez9ux0mVxsjN1HO9RfbNy4oCuDMN5Mvj95IsinmpRpx2674-1MKI9svy0lcMipsKJXEMO64aVOMRKKvN1-r9XMLLkHA47x_9HFDDONcqQH-l8ax9toYKxtZfXoo6iU4ZCcdzTiz1BmmGzUyoHqyccr9lWdB4-E8M8N2d07HkrzEEUIkE-Kbhdv6_SCt4UG2fONLSCMnsIBp-1YfKkQnzy_adltS6m3Z4BNNlkkxAcfZnINbcksdz2dIyjgiYVEicmUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUgMeQBReNChKFhrw6z3KpAlsbF8komgnHzKEjYrjU7tSa0LoFEEblD_YQpkyPWIQrXQ6ujkcNZOhVuIA3XXplxEwSPrDlK1ZoWtAvWJS9stvjlOB3o_W48Yd9dS4OenMerZ9I-rraP6snJB4d3RJ_Ysl3aRqY5foww7jYhnxbjXZVWA44QNZLjRIn5zPsxoCvS32tTMKh8FLN68Ay7xeagiYogjXTnAi2mNzGT0h-TYCRer9b8xSclwTnXEVwGFudWlRFqiqbFezrC_6MxabTdNpnG0KHaJwER16nQYov_nMQMel7BW87J9oeClZ65wG4ANU9NwtQmoABkKkdWA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vqoaX06Fnp3mMOvByAfuoktiApiCMzYr3IpWpxePnyXIFM5ozMNxWTDV0YebDTnVr8kGa784mXkK_M2EQuEmZnIfJ_oiYeRO2JDIwV-mERsBIq4I8wY32FTglyYp2JgRwyxLnpUgUzdlr5h6x5AfOzA4G5FeHlr4t_nHh0AO5T21ViNF7qiBpa2bTOSoQ914b7mKvGio_hL6YGqEc-Op-5tTAxaYfOlqo8Jm8UxK_5XRuyJOPJ6zIRWwOZ9AIe0SMmCqLxn5045KlYZmL8lhO8-yAgLK7JdJLpzezPU6IlToHW6sF77ztsl7bVqmxTzclrUTNsq8YRzeVPibcy7LYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U1k-wEErfTDetgxynpopuWCRl8wWGUp8N6fBeNa31ivKwLRS7TAT3Iu8BO5-rmFssAc9kZQnQA2wxNt83www12vQ0zOv10tqUH4oIqlQcCdb0z-GENuzgok-1e5C-YW3lfKxZuX_Xg-7Iaj0yh6Rz7Tb4jsS3PU_k0r5j07YZtCNtKLpkEisH2-VpnPIoqXwTqZvSUcpbzv2HO3V8zG7naJZHDGdd8_seksWZb7KzF-sc0xLqS4QzRM8LwI8xXY3MN5wFwo4EJWiy9mfuiII-vJGP4hpCS-3soBpZckx-wbwWPbUALGbN1xjH9JK15LI08IFapjEUueztFVLSXAQgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VCU_h3qpicNx_QTbxxV9qCB5clTx3y0A8dwgcWIOilbFrz2ubFYDahY0DYEXFW5hyataFiuWwB4kmKKrBFbvUOkrdqEywGDvhRUhyPfQk1-UeWiLmjUa9zieJOsatP-xjKaMr3iW5LVRGS9xBZW9unw-rme0IQsJ9iv2WwUMuDopLnmJKpud9RAC01dSmqsY0lOdnF91i-76im2gZJJjWEudeWmOOkr-BZR-T5GZgnYsnMfO2uvPeWtcr0bpGOwYVkYcVBnaAtrbi1P7zQFvw5vb_tkzrba7oFbhndXQLrwZ6wO1ukvToihKg4Gwkl8s41X5bA4Q-yr9NbtP5VlnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZoXx9ZRfja8QDX_E1hpU2aYAgR3RuRPFzUPfHbk6aL40VHWp8g-EwLyW0TO5iXZI1YYc1nq6BlASvxaacnKSCVEKw7EuhakEq6oEZRsc7jtrxXRkmHhxTCubRtebcgfdUISQamO3_wWVsQ4vsm1C5MrI3tpWra1w1Ss-t9eICVIqWhW7ze5CZpcbTG4W19ogCrZ3wf8EG0vFgvH8mbI5IZ7sXrkVVUPCb-E2vBwoE16r29b7CTAKMa2Q1t8C_Hys6u6p0j2x395rfw7AhHZjRB06q9kpGeDQfuvk50DVAqpN4su12AsiqA6323uwdn7Im6tjayh0nu4nGuE8eC9RPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/btnaSON6OgCmjJq-9ovkFM5H6yuiUiWzSB6Xngg_MxV0-N5R5TWUM4OpVhk5Nmq1pgjpw9jdlPsDe0ShYiI4AeyKTuno-QGqHLKZy5_sQN2RowX30tSCMZPioW2k5wdZd4tiT0KcYwGJmFVFsdVHJVrVXQhNJZHYAm3m7V-U8YdjUo3ZrRBWqNxVdj3IfRUehUXsvxoJYwOTglm3j84OuI4x-WOh7V5sLvMUB-Zchmb6Ypp4I64q79LrIvHrKgPG4TpAMbwRzHtV2g_i4L5JHyEmBBuc9iX7nq4veD56pAdiveoIgUGTl2CKY3aZS-eeHbqM87etOlOxdhJvFSf9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gPVlxbpx8qMzG6mFg5yJ-oViUN-oWv4g87CKLM4jrauVIOURUuG0KZEZilgg_mxoZ-m8L9cD1t1x4G3DxOWPWk641Qo68vJYb9pacd0cjLj6pFYrqddtlaxBSDcILrNhqpDchqMpFCx5m2hJD6iLTDleLSeOhNmWZPnYzRl7cVr5eRdWXpVi7Vm0RceCK0x0Vmr-H65dfZsGeUsCfZ50ZHZipRrG_3J4qYlYZ8GvGPlbByJieqjHlp-XT29RsW7f7rQlUtrL3cZleQStcyL7_UPHx40yZ05P2wIthsouqREQgs-Tme6GU6B-GgZeXBcy7c-naDOMV6zRrIXEX6cZjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RKuStJgLz_eAf16S9kWdqiu-uZVdtxirQ4CjrnlA0LnBj1HgH7TU4gLi3ocha7fxSiEAPFFLUrG7o4_A66EG4F8X81eznqRPRQxLlfgxfDrl68QeZ43v5F8TE6DkXeAxrjSVlE_QhE-Ibk_hYJofHNQDXGnwbnD_IXwbDqSUNTa0LceftuEyLRHeSzrN9MmIG44mV-neZj3KtdxjMYZWORKN4DFN4baWIS42PgEG0wp1HnKX2b-eK9GYFp1Ua_BgY73iLF0U0sVUzOQdupEEEBT71yfKo3PEN5p6nfIyu5W8NQfvb7O0ujCnhw3NFbvWb9g6HBwzBY45Ew0bsWklOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G2hjmDRflb4ipfzqNDXofJxrM_N_jsx-e9o7Bj0-EeBr-OZNjnyTMh57YNVZuaBLzZSGfMcMqHiW3ow4ck3owd1TbIBnKxYwWDF7UuPkzv-e4FYYuGf6T8i5bGA6_T_OzFNJXTtP5jBxwd6xST2IGVnALbsM0uGPqf34orggB1Mqv8ou8YHosS6bZggC589SlhTFnk4nrmh3Iihlt9GpSVvMYS1PD4kGkpuzDIZl1HkQMzUKoEZoPFFNUmjFov0wT1zT4XTjq3Xd9CEpaoQ0G3UPrqU6RbAcMdLt132EZAozhS1gu0NWv8snydj41watZWeIlUBpEWVp5ar8BVmceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CyqF445NnI_p0tjz1ucGS6pp1gakh87kKCFiuxAjFBAI4xaHeeCDBbrIdm_2F9FtREjF5lciQ_7B4McVmWazxhq9y05BzUhGHCDvauEpDzfaGR2UMwTTwpEgKR1kMu85OWdidgS3IZlOByPrznR0XxWMympX4m_CAYj_wjc5P-WYboRLHOcCRIIqZyagT61Z9mL8GnrBd07QkQFxnHLP2wkJ-ykWrhh1y1XKX46xeoL7vJp0y09Od1tSaJ6GelCnhgR-9H3h54MTGQq_6C2r065IfA-6IPDVhBzyXSu1HSQZPhijnnffOxDbBB8zE6h6fCocDXoEwGqgyLAXZh6xHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xm2srb6p04sTDlwPzelJemwz_q2PdxLcrQz1591B8TuEn0lM3qBu0zJD6oq_UqQIbq3QcHcdYicZU-kW5kQ21cIyPXYXK7Wu1p3N91SJkw9WN9-mZRb8pHrodxRKF_If4t6AWeLJhgK0Jdou5PaDleik9OL-0NYqo6NSxCAKN-dm5zsO20umUp44kLJ7nbR4FaaWPiEbb-iN3GoxZFTs7MEmDQD_36PTLTizyjjWcEnRbq_W4RSwM5Fv7Kdz7J4xO3N4PAdm-dhNPYJXQWr34VNZa8IOAva2EDm0JzuZyrX5_P-JPg3OKlT12rIbGIEUDVEBOC3pvzNq-txEWywe6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qejp9zk1FO2RM4pPAFqNXLOkbsw56ZrlojGmjv6zjq3SzaggwB2-2r6_trcBr8GIzmr031ky3YLgua6hgLkniVLs1Gb8pqk81gLdBNF2sf8GCDhOCmrYrfS9OI2Z4bhlyDxjgcvbNjKUE3qviHPDhr63I5wjlnAqZyVeUkzxB6SsAtai8fVjLcD-lHK23i7W5gnLtak4apgsk2_NFUEPc5cr6TcgZCUMml0nerjHLYt4V8I6L3yB5o16FC2RE8sBgWqqchQRCWqFhSU9uP90-dw-Xmriv864iR4vzbF9eEDZ1TzRI_AvKMSeD_SDOwAZiztdkrnQx5uh8TTQ6N7DTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BDQMjuVrK1KO1kWUQ9OMRTC3uw6Y-yFhEasnVa_8xpqel9mscpG7bTDKL_iob7uvUTWvDKbKQTTwMYenJIS092b2p-Cy-fgEFUxe3qNr9pYg3NHWD7j15E6Vg0ZouQ9piMzBfEAywFHlnIlj8_jOdEKd06QZ10Rj5xYlreAgdl0l8l-d8bAW84cuYXsyBMBDmQmQeQFq8AtEG81o-y-RUzfG_vBqZZ_97ssm1WGu4_VsKYQ6ISF8fYVynkdJtq-4raCG5rSrkIamxhzv_rptTRrNSC4gSQ_Bh7h6XS68M2WL-OKy_CfcFHX8LUJRKOLNGM27jqx_HwyJCP3n6WisbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNoHnSXYJa67F-jTaN7ks8Eicll-gfRIpN_-hbkBflnLJtlRrqnTdzThzIj2oNtNktDkVu_ySuGLF0J9rDiRTvZ6LTcRQQDTPFkL-hlu7gZ1EenOdU3xpVcY6vvbdMRbgSzcDIsJY4icxw5SBgQpi_hjkoKbwMTd1LKsF7pi8PAg4LtiwPLWmfcHG-x7mDHpMfj9GuryGOTd6F-3WPUm4cfbl-42o-P9km50T2cYQhfAI8QGHkdDF2UiAAeVeOCQFdMM7HsGQELhFkYOjkCwYV7ZPEvn8wLGNnpWsY-aCfykiAG0s2kUcdAaMDN6qKB5GesbCgrjG7Sjs1oSugQF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/irqDBP70HIjv4ffVQgQVx_decrVDIZRpOzaVGAfnv863BYyd3e-gHK8bV7OxTHxMLkauvc0lwPArrzQ1V625-u-kFm-sMrBCpVYoFYXiL8zE-0pHJt8-OeZlvJ6TbzkPIgwZsJGUKgtqYz9kw04eHOH767ETs9YjRInzz6H-dWm5dvsF36H2_UJvLOQ3eQedMlGGc9DQZXZooWuZaBnXj_MT5QbJmx-x5nnEyhcFDlPsxfo1p8FYikadRi7B625uCVdUPzu5dxqU8_VrrkJO79_7H6N7UDyiyFd-lF4yLsKCCClAIGz3BfO25NDsx9tkNYCuTOd6xFepzt1k7Itx-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXTHhegkHJdeZRtAJaUzDTbLJkg9gBHR6JOVyE1PSCNvmeYer54ew_d_5i567jZrvFh5cEGhxq9sqJM77NmncgExLeqapswvNAQypZS6a6vdzgHjTbZS1FaaFqis137ASf4brNpszM3j5tbDL6U3MO6EdUHtbVHW3ih2M-ptq-5vnQsRjAMy-_xF71XtNkzrBnjBk9c3U7z2sTaX6KMONyexWcfzGWF5gCukxoW__a9jISY_uSg-lTiESdbHyKU1zMLhQptLxVPQakkJ2BkFVFx5CBCogr8xo1ZcH2MtZ9nnJf_h3kvlRQmC5vasQ-8WUu1iGiFUuGtXIsxqRLoCIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tHHs97i7v4VhMblXEYkMYTUfc2iEnz-xuvfhJd1Cu-Uepp1CjO7hqyb6kTsp6UjuiR6ouIxBptCSZhKKk5ie-mrPU6tuHc-O5etDTkx5g1IWSmM_F3UY-78nnytTREkzEj20cFJGHlv0C-ZFf3QWiutc7HiGul7fppWp_DE6fA0vKOlYYaGV_eZAU_E1wlh6KpPti4weVtjvu5llX3qRWD3CkzZlwzkJCDSlw_rFS3g4tOx52p88vqJB_CFPRHxMcd29tM_2rINOXK97gwFCgdW9oQOXvjJU06QhViR1YD9w-vkD_tml-mpvSZutQHCkU_gaGozm11Aivev_DxfZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LvSOZNEmc6F-NwnXDG1Qwwskv3b2Wv5R20lTKVnYMJanceXH0jslDYJQ85-fYkUyncuZYjPuwqNZnMaAX5iWSk7xRCUzG8xtUSybP9X0U2ceHd6bOXAzKT5NXjdQiwvMLWX_X-M2nZt4lGuM6LBmcS1rwnfe7_36JQf0J9OlZNt_XxE91MAgrSQaLw_CzW6blV0S3YC8o6H5XjliKM2PBA2KjM86kjGtkS6JOv1IlW6YweVYlt9ghz4NpxyaXwEqTI_gqLkw1wn0gC5lSJuIdsIFIFr6NljLfU8QCd7YRA-yk-80q6Ut3cacr-9X6gWp-plCIQr7BdBgu5s6wPYOlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B_-OloxgSq7zXhP06WO3iEgtrtP54HI-BFOx7ZO6QF3bik8mXyVnQg5-vZCkHWK_J0HAGWyBMulG1_uXKr96Ihhm2MvIpPlKEbwaoF5Zt4VhcU26f97Le3JtAvD4nvuyIEa_nG3asvfGBofyU3J8rSbPq9j0LCKnsXeOaH2Ke8JQPv8aQsE82Ck93xDgYi3q_HAlCAAt6xCydH_eRHyl_HZZw2VfdPlw-CVXHCAABThKdYlQ7yVd-l-SGOFNz-7d8EFl_qOkKYL8c7AhwR9533qSMSQlMpbG3YUrim4Axc1YLIQpfG3acqqa7YrCPBc_PS7_8FrT23fg8C9MyGRUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PR6yeJ7q56C_c47is1XoPWz4pU9aCi_Ui-M-woKpRKRs4l5VPQyZTJfQm8XzIZ4Ymaqfnvd0SZiPeA5AB59BFh7pjxoRJd-5KV5ABPNOumqaHGaGbAgcd7VOWk-RarceTxJQn1DS6a8BoXW-N-qBj6dqqeEhH8yjLlICE918jX_R8bUXZqULS9jeOGU5I0ZbL8bJelzpXWlDMXMPttRJXBD-X_ZIMPh5EYhdSVc6PN8-jLt5LYr73FUXODzsw_mMx7A5JIT3IqTb2s3UgfXQeyl8Q7uz8Vk9c45IZhjGQs-fAaqnVw5G7vKa5Puw7mpPSLn4jSViZ9p_11CpUpn3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NG3X7zCduGFs7R8-UzpzWYoEu8KC5mLmGW94yn24sr-ZABwVwWxdZ5Xw0ve2veE_hInjdMf3SMXuTxqZKh4tAwGKXCkJLAJxrFOIQvIe6sLZx8TtxgitsRYASwM3O3_Ty0ta7rDdb-H5rNqS5DHiViDbbRaVwpBH0OCz4QrtwgBrOZ-44i2-80sjxPsUq_1hDh8ZHX7LYK4U4w0hUoiB_P_i3_uWtLvU6bi9cl8SvU1Tqr16mFwf8req8_-XoQ8omdiW-fMoMcjNaItxq_MZBYkEN7Y_jbzgYwx0tm-B-r7Yl50FPjXAwHwZ6EpzFbqc2DqOzhEg06T2otBi3k_Tzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
