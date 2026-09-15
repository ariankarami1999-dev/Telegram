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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 04:34:56</div>
<hr>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/owmtahqEDCeiNaHEMUSurdLK0ustKOg9K1oTjKRV_CJEjZjV_UvcZP45xl5FOZfKl_XfozlgVRsOhINz2c9i97P8qabbd28Bcc5U1xXKDIpAh8Riv-Scnh0n_Q27An2IVf5f-P7C1-OU6NZx54ZqEqPKBrJXXOLUHFSFgtGtDT1ozIAa3QNBMz39uQ1RNLFXbgCP-WWjRjfxnp_uzv-xQ8TGHkHBVoPFLLeWwj25PjaavPHccOgVrdrG2MhR4BkSgz1e7RbaOWQrUvc60Aj0vnO9iNXWhW5NNP466-z_pQ-QoEbSSroTBXOjS2bBYgSN91p7QTnjS94cmjnShG1F3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tTW5qVFVHmTPwy3lwJj5IXrsX21_iUFn0Mat8VXzORTSP4x-mKl_c3ikCFT8S1zl8fD0Acp6L_yFZnSF6WQ6SfdSZ3OuLwqBQPUYeZe17qJynUxdm532XoHJJoJuZ9MI3YRimiTWs_xNPUaJld5-MSnofsuxt3nXMWMrSccLWFQN0oRaVsJtYVprKfe7JTkK7JHw3MiJvggmzo43X-_OnKD-1YoN7n-5xO73nN90MQomlK4cTcV4QgnCOACo4zJ6CwOsrQqacGdkT8VatL-IDJnr1OHaUMtQZ38Z2ANQAd1RvR4rdGeOZV_n_5n1sLwPKz-BPEXb2hYS7O3nTuQrHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_W4hOGi3lmF7iXF_9MGAwVUUbYrZOu_hSN0n_mPa4hmo7ZIzbIL4Bx4Qwf8-9D-BiWweSx8ifcE0Vy4V7LpN6cAuSeRlwFS3jh1sqEPNk98xd18Pc1e4_tpcNvbOJO-6dq6sJosaZJjwqwmurbzFd9tCpwOJgKgppMCB60ksf0oCFzWCQ57XVwJFUR73tHrOmKWfGT_DlX5ANI7FtY6sfuJRDXHrW076ntOkpn-A0bmEoxQ8trlDbu7dAfJf0s92KmfqeqNO0HAuAsi5SZPUYtz37cmb4UDnftV53PMxQvwkfjIiWcPTyF1thK_aWCxZJ4XiJtfN1x_VR9xGRcNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN5hAlj0zOOwQyYbQS3C0SLQk310jsw1yGyBvhXK34K91ZSY0cSdOxmo8O7ed6pBFvWXZsp-Po4sj_S5KXv2xT6aSIXICE-RLnQil_-W5T9p30d6li1ZWrr85yeaTTWFXvGhubtGZE9sSYOcFl3PQKFU7_5SlVTtq15-mxNRi8SJhysytWG7kGApKShpKuVoaxvlKXHTtIBAYTomBY6HL1k4eFsFAXr2LkD9tsnaYQ0zbxY6haY0HTVaF8CzbAALTTRKxeVzxWICe6LfnpYaexR2courZuC7c9uiBSYNqmrxdQIE-FVI_kzoJnUAmshl6WXgU4tAMvuazN-tJ0ikcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iJ6k3X9oosyyFmzALKF5dxpLe2n8K4ErL8xUAMbK6mz46EJ0u7Kg_x-vtgeupvPgnYw4UdApYrAUWFePjZPCQm6mv6_0JIbGs4Ccs7-iNyBGPzV5SdQqMY_wq2dMhhVB7HDcClc11SGARjKiLBMa976Nx5pewf8GEUlrFplHelOvbfIKoIoGkGPE0fRCWRQokUWcEl_QQjQwDFAZVg5uf4pkglr8emt3qyQgOC3rJS9F03_G_IJl0yCvqYQdLAt_he1O3z8fPR0urLOMZJdBaYk6-DhrF1oXTnPOIwifHKR7G6fSpQCOeJLgFGW9N0GEVk-SkGivs5hmT19moy9E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=QZalgbGsLGoQd2hsric45bfrqrfoQikI8l_TZ6faoPjE5WWK3lHTkRKN0MNZOW0kI_r9BUe4WCsY4ZSftmBywtgcYO0wqI1FXdgM2u89xkRxnU5xxEFt7zMl4tQRZ7H-whskT5ykWkGJKf2kad33dsn53dFmrXQksfxg_1ZFcga__AEB5EGsXew8AFAJG1L4CYGSYrUtV9uj-tA9KRksK2e_0hxHwzp5kYjqtCOqrPHwneDUZHQ6t-iSLDorHhnkAl48MnEurE-1ShW8U16yP6uwmGRt-rykO4v7JzeNadW9atqNL3GOTtSG9AxJ0q7W8lo8x6XASokCPfKBHgYfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=QZalgbGsLGoQd2hsric45bfrqrfoQikI8l_TZ6faoPjE5WWK3lHTkRKN0MNZOW0kI_r9BUe4WCsY4ZSftmBywtgcYO0wqI1FXdgM2u89xkRxnU5xxEFt7zMl4tQRZ7H-whskT5ykWkGJKf2kad33dsn53dFmrXQksfxg_1ZFcga__AEB5EGsXew8AFAJG1L4CYGSYrUtV9uj-tA9KRksK2e_0hxHwzp5kYjqtCOqrPHwneDUZHQ6t-iSLDorHhnkAl48MnEurE-1ShW8U16yP6uwmGRt-rykO4v7JzeNadW9atqNL3GOTtSG9AxJ0q7W8lo8x6XASokCPfKBHgYfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krq71bp8GnMh8HvXRa9lv8XsSRKB1s-4AUd396-axFwORJoFHEQCS9kHBzoGGKLjlbkOtzGcPl3Ls2v2UMK32LLtdtimXRC3NoJWNFYnm7042eXSIrXROmsuioCT0OV-5kq9z9jt_ZrQPE1wXATuU2gJbjFvImsu6gAIG9wn6qz7Wc6vOfE9JAk2x3y4v538tlAMiq1orH02BYnAzqsoZKfaqSaHfX3QOelZG66M8N5Eod__IgKiemBut84MIeyGxeBM0A-1sUd3JDmW9ZBbKbN2qY526Ij2fsWAb6DLk-H7gi-IFffAOawpidcwbzRhBz_pYvFck_D9Wx7Oare7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aepdKSU2yOjDVqYCB51LrZ3TUTxnNLz-IaZiwyQ7T1Ey_2EbUgeUYph68bF6jHMROUJppSfrroUNquK7yiF0FHDY6VzSiM5TN3u0Ce-Prwc-W05_poeSEo-RUxrKNx9BOQJm1Dwh_8ZQc9-Dkp1v45WYSWgtrL48F5h0i3AVHKEGTN67Zza7c3GO3XB8ouV_QmTcObBOWZQ9icIlQtcF4ikUhFE8O8KMT94EuqgiCn5w6ubx51jKlUDH95QBtHqLd-f8p1GFS54E89aPU5OCc7woBkgWh0ZW-NXLM-YaA1QNhnjet-OPf26i-K0pf5jOLKgoM9jnSwoFvlFxNCq2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc3NMgMAZaUl6kf6suEfBbyaeCTM5Oud32ytpPqMBRk6-70pMBxqfRoQIXhNliPhDMa1LEOjLhl7iVEeREBJb9kHxB88HdhO1zg-8I5XsmhY5TNLR7bUrFglVreuAjADuj-oi3hG5zHDW-N7nlvzitA0zsBvTnOmo1mv7autR7ffvluk6upjVVE6L_vrw_Vro8ar-tslkgpAWMC7mKbfILkQ1hQCgcmGiAIZMWXjLHDJi2T2MPDCf4YfweVNsru_RJ-feO5K88XQSRxKaDArHfvQ3Z5Y8sEpBg4-jQSRZw6UPklEIE_uT5Kd9ttO2d6JFSSZDpDVFyhJO3Hex7qH1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=r-5Xth_i0jgEF2Vc4GnsKqDb1ijK4B3mIO6qQcZopCpg6cWPc0GSWEzHGPifk3BZc9yQtCWxFUv34_SFGux5UqzXAxEmbwS8JWT_duX__NRS1-f91krzFFIhOm6OIWmuOjXfC5XNT1HnBIT2N60DLFutv-49y-iFxcUWcSS9TwWFhz5TVVpudbjjfIfCIQRsmecg3K-gL_cqsA-YQ-096n8EbGoAzNTWgfWarVxdV1JRN4c4UvUXig8-utmkuE6wSNMTuImdn4944Qra6akyW8Q7uHqy0ddrcqjWAvcO4e3t6-kFcW2Ue7tIcCC_uQq8fjUlVfajwHZ1XPvTzxL3kA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=r-5Xth_i0jgEF2Vc4GnsKqDb1ijK4B3mIO6qQcZopCpg6cWPc0GSWEzHGPifk3BZc9yQtCWxFUv34_SFGux5UqzXAxEmbwS8JWT_duX__NRS1-f91krzFFIhOm6OIWmuOjXfC5XNT1HnBIT2N60DLFutv-49y-iFxcUWcSS9TwWFhz5TVVpudbjjfIfCIQRsmecg3K-gL_cqsA-YQ-096n8EbGoAzNTWgfWarVxdV1JRN4c4UvUXig8-utmkuE6wSNMTuImdn4944Qra6akyW8Q7uHqy0ddrcqjWAvcO4e3t6-kFcW2Ue7tIcCC_uQq8fjUlVfajwHZ1XPvTzxL3kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUqzxDVJwvn5XGW8iLzhfIXllW2YwlcKIqIYXxIEa562A5Qo33-qpaXm8yW5MbJxJkMTmPyr3aq0jWCBj0btIV65K3TqDX3e0tfmrcUhKmgyL2v4LqK3WvTmbEczzInK-99Fv3uBkaLPAN6PwxOuBu-TnhlsvscBC-Il9QFrvu2fKDk90DiQN9j3eVoC_fhetlyFWjw8QwwtavFVzyqIW-ZgL_VIpiuhOVS3ZmEos4N6j9LFq7Rhtet10tPQ30wsikeKOts5o869m3f-cEVaU0glSgpdOYdBeYMmDGNXPkRzHrJd5BGPsu-vAvhUh02IYG-ZLMBwlbPxY38AbB1N3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5IAzhVGcvL50pDK8QTwyDGvH8VoQGrXHlQyrq-nlZSxVO5ZN4dN_1J8lAmzpHOVtMdlEWqPCgCpPd3r1X--MH_Pm263QlGvw9KgkJiIbM0eXnmOSQnxwNClmWmaQpdlJCdTCSQ7-vD4ufNovD7xLN_yKUp3IOdvkgU13wBSuQP_FumlzZQdZo93P4M3wqjMqiSJI3-NTA6gE_3Lc6NBMGaS-zTZC44XN8MATQqltsKMg-oge8226VaLXGAHO3WQ35iTmAZRrrVRHZskWBm5EwuRtiA3OsfzAB8KeWhgV2tSG7b9yH1698Y_bwkIYChZGMl2zxHNq1dxYgpbBoT_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-lwKWwjsqkmwYtJqNEVbUXf3YeO9ACpE6WyHZnEtMScKr3jpwYzdNM7W5LYk9z9pzX_z9FSx2mpV7QcEsLL9jJMbF2wwjle9F3IK91Zvo1gN5eiF63uJ2bIQWGa2X83kPSIx0NAr3du-mDI4D3ERpCyp_IRe2UsWjCPljOygYjaNNsUqRSC4dbPAw6t-G6VQiAtXCv74vC_R5GNo76SQAVNooR2bQJR4qQrgBgHDn-OXSyWMcCDsDpAxRAXIN9T_WYsuk4Skt5OkMQV1WQZKkX7YXBpJVsLV88hDSSsyAGDfFtI5S06fGPUFKqxSS0KVMra1h_wI-HTgf_LnKB5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sTcY7kX-TyPxq0Wm9j_PUHf9btYFMI1p_s2jMQpXzdci8AtH_HkLasSfzKjRZJkJYwVxIiwKJ95vywpt-Ki1kEy40XcfDX-VZOvVjyWN65XA64Y7pcTq6Tl6cFBwxMkAI6o1zqQmJmfW9Ehm7Y_5NTcfEVvw4SMFLvExNR-RcvgSyYAJKjacJ-pHS3_AicZPEyxA9g_EOstC8q1Vk9PbdON3ZoLfRe_23xx7--BfEyKkzaauQSvSaNVSzvv7VlwHkxUR_CBjYKFKjeAlQv2dZjFBPcWkWYi6k7VgtQOH0LyxTNdNucK7FuWZNW_uM5Tz5JClt9WWA704gHPmDwoBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hMU01cfxZqYGwcxj95DcOR60DigwY5lwOLWT9ODBdBJrs6CbeZqAwuLr_MEumLFG2cOvvSu2Y4dc3svBDR1rmng6i03CoHwsTYIj6UVphqLTWICi3itMPmviWoeyTUqX4iML9e8xztDatkwyjmBmvHw25gEJanHHg20j4ZSX0JeXJAiZ_B-v7FhwytG_VQ_f2KcNdO30UwQlNSd0UMsFGhCCr38QuamG3RXBV8AaI53cxgxprg4AH_2lfvi_940zemYcVQ6UYYjf7tHXkg6CLx-LQldJy0nPn4Q7glu8rUFwSlNhHhoq5Bz9mGL5yGj9vVmOLR3idBMVcPZiFAbguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iVbKxOZ4OwwQowH2g5RI5u7LM3JY65PKtJ2JxhJ5SJJXeAUXei_VGrBa3sYM7kafF3_aatmMDZWQOkGzIEkfrAkt0ZcmO6W5kJ3zZo0lTPCBcwny2Jn6YM0dHB1E3TWav79D4EOa4Cmezt4nWPtf_4yvV4T7YD_GB8hFrcbEHGbo4y9dtXMqBlIZ7HLC3gRoouv3gmWEcYJpxrIT0kiqqaHlGx_NXLWI1dk0gOzpF7wq-rcglzD0ktRqRTi_mLl-cdGF2qECehRbNnY65LJt9SnUIbrEX8uAMiocaMsw4JhMm6IFqsXWBMvtJAQYn5uYK0I6cBD2KscAnjob6NiJ0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V82xjC13oXKQplJEiiXoOSxDkmWEDDxuYI7NrkrZjD7bfJLfrEHGJXtya4hIxNV6lY497-WUO6fdjaYNkaLq59t2YkNLvkZHIgLurnqBqhuZweKqEMUkrxqamGv8mcQ1QQ-MY7NAsrf6O7Fovy91c2TczcsTIo1HjL2BgdoleCk7JBhTkadpEMVOqrCvRn4jYF_EODQO4-WqBfPR2YHru3kiSkhmMhlFnXP3IMz6GgLemoU5sDWEM-MtyrTedylL145-3m8uLgjbBRmike96semm1EWSU-zwOS247MN452Gtra2eL_-nt36aZkQEbDuhTQ2_z8CaVNOfqkzuDYtoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kjQ7EMh6WGfEcb9ST-bQ_x2f6fDk9dcyf__lGrSO9AhEbLYJzadMVrrNEePwN8vZBHgmHdfSoE1r4Qll0JJI2vBYvVRRcHntx-a1pVsSSejCk4JDalocNxqwpRKOb3FNcVEQ4ib8jw4kJSjBM6i7VmPNYddRZqzxnowA4TNyH5KP5bCFd00AmOpdUl4YQsdsvqOPgkFkzSt5PsAEBIfNTPiQKqTiiEyN0lhNHLI1OkU5tNMpY-Pe2pkPEKRT4pQYX4NKxH_EiVsmYYpuzSD-Pg6swG7Qxi6Svey8FAjd31DyX0GKfK1KaFkC84j1Upl1vRyjG1LD82S-gTQXttc7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ulFufMec_ujdtomE13HI18Q4H73h7zLseINQEedM783UJ_fwncLGWYHXwlwMKIaKHdhLllxRmOILwJOWhbTR1hyD87bGDROG-ky87mSiAGRRiR3KzmQj7l8X3GRlrejFnpwphPV-sp2574HW046MJXquvZdxn_45nKn3919A3NBVJU20A_2zOPXLyvJdH95uWEUh7psjd1VeUY_2Ou-8D0flOaRSpQ_KGy76pJtv6bGxbaaCWre5Sc5JjOi984tNI0WgPxbSQBNZ9NONQO6MYxRWX1RAv16QtB6SVlBjaGSVSEkF3Xys80s6VhJNCUroTkW2vIpG20Nu_VU7mHcOPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=fA3TLby5w9sPn7DMQ_ukM_gr37VpNDS3u6KI6dAjtzecspuFcm07_451ff948JhhnZ950SJ12b7dXFosYg-et5gn2oT8lmqlkXvtr5mw5J0y2Ij7toRPyF9imLXVf8wUtHFmkRb4eFBfPFELBEP_3W5GvVNCSy3CWDioIINEQpNIZTF-gaSLqvCtCuyfA7ns9zJ4yP07Zcn99y2dYusK-vb1UVi46hSla-6yBxqOzrYndz1OP0GGJChog4AzstKdmUVQsdDew6FfuTrfjoIJHiCJXXIv-QdTPKsz1LmEEvW2HR7bGapY-9sMORULG9UCI3Vkw6af7xv2p-05xhyMqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=fA3TLby5w9sPn7DMQ_ukM_gr37VpNDS3u6KI6dAjtzecspuFcm07_451ff948JhhnZ950SJ12b7dXFosYg-et5gn2oT8lmqlkXvtr5mw5J0y2Ij7toRPyF9imLXVf8wUtHFmkRb4eFBfPFELBEP_3W5GvVNCSy3CWDioIINEQpNIZTF-gaSLqvCtCuyfA7ns9zJ4yP07Zcn99y2dYusK-vb1UVi46hSla-6yBxqOzrYndz1OP0GGJChog4AzstKdmUVQsdDew6FfuTrfjoIJHiCJXXIv-QdTPKsz1LmEEvW2HR7bGapY-9sMORULG9UCI3Vkw6af7xv2p-05xhyMqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJxUdt5cas8VDazzQJ_W23qTUHAVG-hRjxjhfarTQnsIavSLF-vI4KinUwDHhomx-SMdUUdB-RB2sITT6_MzdRm1c9fu2SD6cHTc2Vn5Se57O_1qMYN6JgKRKWNwAPxYl4baQhrJs3LWv1X6LaaSE3AM7xewpa0pw-DfWSA7w68QmHZ8W8llS8wTuTuI0pwT9saS5lWkYFbn7KCvx0uUpahcwtElXXT7xYOxD_atSRWZoAS34-xdv9QNBjhKzZWUASLFn7JK-4OA_Jbu1Gx1O6Rf7p32zkEXmS5AcQmLESiW9BD4s8acT7cTxLwp1OEPk5K-_a2oYq8uUz15Xuqlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLcI3BUvZWoGuE_D0MQgi9P2YxlQCAEiL2wV2B3xGhWx7BITIBOD6YkPWR2ZDg646bw169fCFJmv12dj-x8xvaPyBO9_OSrfvHwIJyyc97rZomJRZCuyePCDoXz0ibMVCo9Xt5lDSL0Sxd_yIdk90Hhkllrrzutq-w2lLH8tJjwFt69ojsz92jUACoQ-nRyvwfSDJw7F13lMNFKh_wjzR-bUlmPTv0Q2Ph2YBwkioU8FNrs0IR9v291JXjBQeR2esY3dHV9n_CymUV6c0HojhBZGnG769UHemUEyaTrfj8K6o9uLrNere-61VJW2ONNzbd_yaLWPQtCfILT91EdF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xd-9NyeV1BR61KxEKy81xt-aenfXTAp4A4RYU-zfMTAoZ4qJnhf70PRfWpPsGcDSJ9LQaPygBRFROiJY2DoNe434FE2j51iQhFN-mB_u0RxqevGxyx5If9tU0rdRAGN7C_f3fsIE8a81PtrGKQVGCI2OVPioTJLtWt43ah1r6vJHBCai-_vKbRSojbD7N3iVENQjprf0HbsHOvUn6fiD6mDqUJ7b7Wp1Wfuj7gVLL6Y5h5GB2J9eOlx9xVUpS6MiiSgVy78hEbqMVAwrkmm9FidxSBKEzyEUWTvhF9Ti8SWmU-8xUsiZBZrCK3yB2ev8SB_eDH1ahvEv_DQEdaEnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rqtj1swHOYqJ1NJv5H1zcxOKVmpiaK6IUuJi83J9yuzl_SCPCbrwfao-gnHtktbe6kNCHo8Q3ufO8kBUG_j7XmSECYyHmUTzJ2X_N0kKSDSOOIUAyJgXzi8DAYxfJq34Ng6MYaZTGmR9LaLdN6NBFPY0Pr4EQaNbS56ZiFYt0smYJQbpjZBlgoZg5YQrZ7BhLbMqXKUYQUi3UNgoGYcZcaP3kSjeUKAkTHc0Goy4t9dJaGFm9oD1rx_er82ghgyWOtbCCaoyJU_Ra86kgq6bnLCLapWbw7bNkU-WRiep4aUf_jYw12AspxKvKLJpR43A9tkyHOY-jADH7G3dv_YJTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/amX9QMtBgE_OOqUFePShT8X6Ra4JOYrP6FHitC-FKmShQGaMvo-kPwaNgtfcrQSzUWXpj8MQpOtvEM2G38eVkA2BKy7gJ6qFbGxeBmONGwVyYWRR6HBbA5pp_LSZg95K4FR9rh13FuYJteDfm0kLCnfA8kTHvTT4ubdlMEAxJNfAm65uXrSB8BSjgMpGKwcS0H5JZYHFIF7r6FJQ0qjTy93MfHCO9eJs7Yd5PzufK-O7V_T9N5dbL7lpo2P9Q67qfdrSsuUQy8XHelFc7w0zUXpIlqAXslxfE7mDMqiYdSmZFy2l2bMqcY7V0zmMftfPv0Q9r3TrWU-ps0sRrzg5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LtYi9j31Muhqjn511sB2IAO40GuKBiUzWQ77EmZBk7QfKhYpbRTomLqqC6T8j9Eaoe7MbFuZBpuEjLzEFec4VJh4dEc7GbXoFZdxBdWj8wQS-XarPC-9ngv253XC_UrgP_LSd56EW26q3NETqTbehELI96tqDIN3iI7HX9fOhOi7ydpsaQbin_ek3e9sh8ormyzLm0893n2mlkESu51UESFgf5hVNChE2vbzdaCEhl5Cvt_bWRDu3oCHOPTTHRpsD4iCoUjSbTwVUCNkEf3X2YScS8Y1IQY7bCf2AqmCpUNLYn_ymRROSxz-zUP01i4OCr5D5jTuNM2q518L8tk-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QFI0zauh8zR6k5eClLHpSpH1Jd0RsveXnejFKAnHPstCrjeoTW99jL2DYVq-ZOrBbQn8QmWspt6he0CcVYedvx_ZNR3fBFB6b5xSy3bdbhTu1lr-h6XjQd-r1PBmElDRNZcw2ya_8s6KBdTuwQ39wikk4GLoRQ8hC45AesgTQSpiV4z1BPkRlrpD-yi4drajlP7BnzZq9MCr_WTtldfqOaiaeVlWvP9BodMBiyfl-5OGMf-RwJqydQPrkkUY-1KGEf9iGa7PHZ6jAhubrS6UimakBDpEXBzlZAG_5w-bmN229SRiGRvhXdMD8qfLxVj7a3jH1d57lFDvcRaSZLyg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U_b2OUKR7eshHsultBmOUrU9cXns6Dgj60rq5keu3XrBPGLn-w4VaG-JE-xaolOQC1KbbZxGtSzftdK8sgvEsjHlaA2Fw-cYTRYlCOaBv3eNYRNFcpCb5i-m5c4zWRvxms-wL_nVsG1ARMeNs2oHP5_DO-Xzd9SXyIO2XQLXVc1N8GDtR73D3ogw5c3gBmMxgUTGoQiI7OoTfhWFfNriXf5BHI-AiK21iiMWg992KM8OiqtjTujg3Il3UHt0C7kCJOHDheVkxnqY5hVt67gPlHC7qZ5xC4W3AeH99i3sWQ6h9oq51kOp5c3gHZt_9gfPL_VOATqDbc-43Z-3pdYatg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lslDUlxQIHTAy_1SdVdSiE5IcHabwiuE_wDvx1JaYVRI7-QLi_aFt7Wf2AYTtDdgBw9g4Ln52NmtNltMp2kRmUiboF0zU7TZLf63UDhhtnYZKmyxr0UKQxcnoq3693Vjo0VkCLo7SIKXIr2qYNXDLUt_XnO5lv2MshQDdRs-nGvHsIOgtmmE6k2pvJAKaMCxdqQXXQxi5Guj-sE0NkOv2FC0cAzg4x1XpRNm_b7GStsq1CdGn5B_NqffmHgQrs7P1BMP-c5X7AayBz8-Ku5bpWdfP0EVVCsT0fTHpiFcya-gD6ojtz3CcXjPRP-ik6BreboPI5U8DPzdiv0XbTTukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=egdkbRg9Bq1UuTKdALpaBEWbeRFdx5S4xNj3muzODYPVULJnG6ORRQC_BpTc3tE0JPWWDzBTxPUtxu_DDizUZGMHY_YfZEs24lHgMWah3ze7eHuerECHexh5RBNMYCbiOdOjM8nsWBGrFQNW6cxeecrfUyfjka4PCnuER-z8WgGteoZpBLrsNYf66XMQEnEFN_L5vHFWc0YA9nlbNYGMd2dhv4sEchT9cf0NutvNgZzqgaSjAfRYl0BJ4JSgBssQsRCAw5bh8HobR0dSD0XECUDC578J429-Q3q2YHUUB-Uq_jZbSq6VPTbQHP0vDtFekOshCbaLdTrvJFdlWvafQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=egdkbRg9Bq1UuTKdALpaBEWbeRFdx5S4xNj3muzODYPVULJnG6ORRQC_BpTc3tE0JPWWDzBTxPUtxu_DDizUZGMHY_YfZEs24lHgMWah3ze7eHuerECHexh5RBNMYCbiOdOjM8nsWBGrFQNW6cxeecrfUyfjka4PCnuER-z8WgGteoZpBLrsNYf66XMQEnEFN_L5vHFWc0YA9nlbNYGMd2dhv4sEchT9cf0NutvNgZzqgaSjAfRYl0BJ4JSgBssQsRCAw5bh8HobR0dSD0XECUDC578J429-Q3q2YHUUB-Uq_jZbSq6VPTbQHP0vDtFekOshCbaLdTrvJFdlWvafQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TGSapKdIoA3JPkZUqWt_NIO5nardCbjbJ1V3lo90b182paSSxZdel515Yjm38susGSyIrYCBJCXeTCrRFymcKO9BV4HN66Gn_NhQfRlh5RuyTbPS88cFpXGD1iTnfxMEjjyX8TcJCJnVdWHzjyQ5G_X1iAMDnf3mVJFEEoXr0RsdowL-i3uPovCcMcZpk9LD8ZbLBm2LTW50yEXoa3me9LayXZGJhj7vKmgc-5yHyjSDV_LWsV0q6aOfw3u1dK4LyLHYus6yD57HbGf62D53rvWK-mUujtmZlulOU6QODbeauTFGShUJ8BAhF3P49Lak53l69OcqNQLhq0HiaWdOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNhTJreDMd26RndwQubGT4OXf2sNzx6NuvqohBR4WRh_8uTi_Ibf-7RDNqPCB9mHtwrGLnvFjcAXtIpZ6SnOClkyx4WoqLx3e0MhpsjrfisZRpsBGPIp4uK2sFn9qpBfE_edcyQYZ2SqfVvniVAZJJb7vEG0w8GyP2hMRtPHs2HT735lmdib78khAAx1qtbDjDKbYFoTsapfVpD4CSnmY_XfqxKqboLu0IdoO78-i-SQNtX8ajnv38o5M_fJ4qKVbfYZOqXX6KmHg_R4H4xc0vJkICHSZZULMfQeQHz9i8UXZmlt3WJii8M_wavOKJYrM2qAZT0-H7NEl3xkQvllEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r_ImIPXOswZ3Ud6X3KOlziqBLkLPqXKBMQtydlbmnprrptVdPJ93WKuga8TM3UlbAn-9I_iTHJFww9LHv3DwHAY7umZhylBn_hW9Fq3vOrNhbhcGXokh7rbL6-4VNjkEAI1MiOGrHeneLQKWUoD7UPgwOKpK58ECi-T0RvpXAQuNANFTPK36ym7JxsqJyuZ3Bw3Bl5mn4VCEfzPFpKm9LyBpaO5u5zPN8NjE1vVbv2IhFEqEkfXL3mSmPronAWFNvVF83QOKgrn8GJOwPZIDd_qakqeblHDHs0GJJQISG9M70VmJqjBfltH0Y3XXjBTWAFytFtkOAIFUHtIbUoWS-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UWW5aobMD3zA4sTHLinA0HaVPiIFF1jdg0gvJhceENZzRiV3BiA3q7ks9qNptvFVnXSW0V6MaXuywu48Z1XBMHJmcK6AySVmP9_2efr4AZgDDZidlaLAUwsonrEVe2LYzMbfrYXEIEaNcG7Tc01P4STMicLywnVg3sXe5CwtbHVIOFF3pcJ-M3XUIQ34yxKLbYzcot_m0uwzchkVvUC4gmvQ6uSdXRfDwDEwPjKMJfeT5oYDQbQUJJkFzm-yLdsrORs_nhTWu8Bt4UCJVpre66Sde0bLVUpH2CmXN4SKnojZRyAIxp1aRDUQMEaLESeSqrcZ3gIKhTqlEZXt0WJ5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZs7MYjj058rC6BRxHHtalxC6zOiOyPvMw-v3m1YOeUx8vktld3zD26Qnuft1cOk-5ulTv_0yMuSWqoxUmnNU1cXsIm0T3f8sUHHhLXYPBqLBLrJfLEQhPazgH1Ql---If2zfRg_I9eY9qOJPmzodIkfZz3aXZi9YtqmHyAJlpLNJfFVC4mnEURUCSxdOzIy2zDfofIeL8Re5iHryODawTOoD2vJZnV5Q1auECbKlY9pSbK2Fu8NDccMnAC9YuVsUWDnBNCUF0xGpSEKw0Xn0Uf_ytfT27Pjui26vXZGe_WODeri2XzBFUehhES6O3UmnGEGDBMF-F21O689Jmk60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K_stLDeVt4nkzGGVa1t9-nK5WSyOdkQLzXmvTXVcLWNrSabYl9HkCvu3jXLpUaoE8ZH7C4sNKavv8UcsGO91d6xEkCDYRBYDIANBgu6HnHbYp9hPBRGXhf-5dmAa0Qg3KrS1WkDOWi3-tZYGEaG1NfkppGY1Q0w4yJrnrWoYLNZ9z25jfBVH7dqSmZhWJGH4hNKReQEJOybXmtkJj7tMwTH-N4290gQWBAnUp1fPz5edVGP_xO6ztjJ9l6FQuvkJ4eql7GACreqRBjt-BiF1zA_rz1KNnltrOpIqIX0_2Yax1-zoUaa3CZVt25HcH-fAJHx13poul5ZvhaO7vs79EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cHT4ipKio3eEptr_vEk2fghiGutqN7yR7bYtSAnWdIDBZrBP2hnO1DtHdjsz83vYaSqql-5B1V17O6bprlL2qIm_J-W9ohvhtlX_AHWpGbeGkkjehM2C4ZF4bj1eII7TRaqUjhICyaI1OkmFsKM9gpjFlZgEXW8B8xDfbv4SPqaCZ-dFXiHCXJdEb5QKTHa3jHfYouNiPgrPOs4n0hjmYQBvupoJgPvyaOmo0yzBqZfFM7JgCaj3yc6PMyH7V12U7sbdjonZR7WyUwHkzsslrRx-qO0mYpHj-m3KmtUokPwOoFwloSDGhCKGP2sUcAc-C9Q9LV7R5WEjggXbeMzjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CSJWdQod9I_BOcIc3_UtpbeYshjFcUlCqK_2qPrMewrR3ZmueW_inx3Hd_y6WsN_4L-ewTMa8gBkFnIudijh12Z3GByDrxNJEp1wZV2Nod1XpFAou_jQ9Gpm-yvow0BuChhz31lRGnecNaGABOow0uR7s82nHOBPIIdHBwz8N9kU-rWgitSC77jtkWhkTU3Nprfwm8MGO-NufUpYDLRdl_SUzTe9Fx5TTb1dBl6XgoBjSoMge8oQhTorkwIoN_p02IS66qKcRMoVGTDON-phfnd2lsgQjRyFWPjK-P84Mqh-px8U_FF-AbG8fehqzXtYMRML41bd7-MCkETT-d0W2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D4I7P5bBa17nONCiCOuWQbzaEbnv8Wr8iEC29Ggjzky06ppgvRUpUFN9CC9Ekw77RwnoBJcwKGxdSeHqtYumUZzdGPa_lhF-ZLkfEAo6XEIPsn8ijzR0qSH1aia-nlSAWIDwpNxRvTs2jUmlIn1Y6-M7I6vNaNl4vvJm48cUPaZLl1d6L4h_OW8f3YF_RjgKGIr3l-ZZzyCrE_SoBsM0QooHzls8F4qZHjwuTyLANOvVb3XSioVWOT_3b9S2vnzwGy4pc4TrGdfTIuGgVaX-UXs7tBNi5-7-ijc-5Y4OQ2JVIK_6O89fJq6rVerIWPSoR-PH4L2aFpGx_CatUmeJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jP-CSL-Q1jv6qcdY7gG_PqU9WCZQfsVaJR2dbUqyctwmVnHagbzMO6GP-nxmsog4zekSkUCZ8J8nB4vMKzEdhhBLTHvh7Sfu3uZAAbUmPy24X4yqvignccAuAfjAOBcK04CGgY102n1K-8x1OUFBNvfNPZMWIEjju_ZD2LoXAdg4fbMZ1sZRSn32FoU07igfUZPrNPGlENyNS3b3xm7xnr5Rnz7FmUNYeAD56qqzqEFYpPYWeBe0o1LyBR1W-qOF0SkHcQ1CRUhHL_9yyMxf7wX_32SPmbxVRcAczPA0c5_tQFbBtFhyAsBvcoJDEWbwJsGr9Ps9osgjN4KcU6HMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uzoB8JdG6BMlaQIJJ0UVerwe8nmRFRxA8ZkCCemigxwUIBGdgrC91HfZuD-wIx1ckh_syhJFjotXkSSFJAgMv27TUZJHiTInZbqt8edwolARJOrzhvSa4wwpKvbbkZUijkRHSS20uuDfRBet7q9gOtmybQ-h1dGRwZ_zW7g2JiqGZHsQnH0FkGLA6nMV4wae0RqqmD5PL5typL-eTfuMlPvRVHlZMuULoKxNjS_EYtpgqxFF7KfMkmg0wjaf6DXhJeS0Ifanfl2kS9Zg76HXWyiYcs8p6U6Hbax2vB7E_pVTmkTCKyaaZvt9H1ya9gSCKjKfF-CbnTbPTPgxywQJFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AQ3GWstT92HgM-MLcy_fAc66o0vf7A_myri2LDy0b_fHAdL5-Gm4iOczZKu1xgZT0J45OfnnACZb-Lvym2P3y64X8Gh4LnfEMAi8f_1w6CkBo8vOOGEv9dHy7WGpd1qUd_jScweVURQ8XwtaT7YyTLhjvo6KgyY8VwNLF_oyHoNQ42Gf-XowAeERDvGQeV0mjT7srOuqTrv6r3vVI_f4oR5hQMkVREBmrITNjr_RbTPybz3KH-xnb3-CYWS3FDaQrZGnEjMj1B6W26chPUfgriMx-VIry0joH2jGCZv0xJPl___h_W2VVmQRqjAVtRV2yhYfMgDL2f6MLadSBqM1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bmVnU-iPJasy_iNbm77aZ8e9Fb9pPCpNLWglVbk8qx8RfAod_D6Pm1z-MDmQSZdi26ViKAuDGHDYEYoxg0syJWujcMiewNyxo8TmZCmdAFzs-qwQ24FnYhalP1S9DgDRwBWpsufig1GRF4c3AwhC0pB1JfirajBBg01xo8ni3dOuXOc2DcM0qTrx60avz9mL7UjK1nGFDiyOBy2ghTvLbT53saloSOxiJKbvltIge_eIVxfeornDYt0ijyeS917bX-8On20IVf11WVSfEzGNfh5boJY1mn6giOSpDOK6NVcGQbMVknlgZbMQHq08zi1z3yJ1ckbpY9ZRC5DBreeGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZBnHmfwzR5muV3BXVtm9fQKgpK1cyrs11LrAbLmcPqkcbtjPgaxVwdjphWjUBbyBdXIgQQzGoOamp8ALj0GP41LN0XQ5166ZkNcwbfajNOgpkCBpyfyCZ81CTS6apUUq09RW7AJQdpv1rORp6Cjmmyq-kgqj_-48vEajlQUcvay07ch98b1fghLPqECURlsA-8gDkn050xC6qPxSeEm3MI_L1apIOQC-bAHGoL-wO1apiCTwBWFljaEE_0esciN0OiFHp2xSDuKrcW6qliVP-qZz2YQphTMbkhC_NAcdd5B2GFlCJOx3WF6070fADv0pAWJ2ZMOclgYYfU_Gm8GRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QhqmOUO8IkqqIzwl6B8g4MRglKnaariuQnIxO4sHALwypyEBibEOuTdcz-Kp59NcofKD28Y5iy4GJXBYdOzVs8ZMuS0p93ujsrpuH1peOvO5U7hqvI_kLgbSQmNqH9VAn_tZZTtwqWpzSDF9hTGVMgbwELoazWcJugmjp7ZS84qnE2w5VWEfBagLsHZDiEQu2crKzLc8E7rneocvGExIvZNMICU4ZSFMpWY5LkkLKUh0PP-XojTKOPQfuUm9Dxs6q535Ynbn_7qTgaTHBxiDQjywIrO6lgRaGFr4GoETUCDxfS7YEn9KR7CEGdMtR9zCNkHVP_4lqE1nzcX0w6Xfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DOr8BKnxHwfnpD8Cc2xYnVGL0BTJnbOA90sgk1hTO5atWZTRuwZEvfFKp8wAzeEpSkQneJ_i50ybEQL6j58TxlIamDiQ0j1eDOEfM3lHyX2Q1Hxe7qR7N87ClY2G15FwToXdp9nGbS7uSYuxT89kziD9i-oXGyuJ5JspJlIYw_J49oD69FGqVBVz0D12gZmreywetxaMGcMy9h3TsL-flffqJ7UsQF38F6a2lB6OmAAfkFK3M7PipfGj-I8o5Es8GrJ_IZ4TrZm9Vr1BxvcQIz5QJCkpOyFkdLQZRa5spaXw0uEG5KGwInDDV6cRUQC716B75_jGAxoaTrTMJDq41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WkLl_Pu4r1GM0rTesHbKVmFWdMtJZlpcyR9YqQXuY9gjQQiY-1JL_YlUVXbrvtBaeehdVNmp3A0mez0fD6vHAPIaUfbHQOutgQZkLsR_s6rRJKWPwS9-60_uQsDU00Tqc5wjeeHChrfp99lida_QfKrWBaJ2KPH654ndUGYG37_qw-k9eCO4URsL1YGt_twlHGx-xC-yoGQ4fIXvc5-IYjTDJqmdJeexVfo1FczdyV2DoSgXJgIIIGnesLrDm08g0c7ZAOYsJYbMuf5Pc2LqLfodwnpS3AtApYS7Yw_CNrgfxtv2ONhXMOea8g_QiqqVD6aNq4SMhMDx5CDaHnmhbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BNW20bFDfJk5AtuQcFEvRDV_7-MtcybNuLiJmHEqdodOi6zogkU5Kx5r5H76DIh39ybSQ0MCCeQl0kHR5jYt1Es9iqf-khBJe35KD3Vd4TjbAZoUFiZQGmcquLS6BK3fAQrT22vFZRwWCuz-U9cKpFB3lLsFcolA0CLhWkisYYer7F7yPBzHn3JaExT63nx9yY-qQ27_HH54cYuvU7Q3-lsZoHizuPYbgv8M0ESFvVsa7NQNOHAxjw1aw3Hs3S2FY37QDNQue7x1VBOxyM3chE2UEsIOMAdPREgbGqeQZIwqFOAEBYMcn-_y7STyvRX9f3W-oVLZV0Mew1Bj7pcDNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LLSlTR5coU17cokCm72vc0uAt-9HAcRljDUUE6C2-6snZFHCrvokgQOjIr5hZ-5HmbXjhdtIJpwK9vxqz3_9QnOYjcOlEE_vO7BeKEGi5pZvR-bzK5FkPOv7Knu8GUNhFTFgkTuzYVnRCTENIA0tluH4jLaugPAJvDCIfkcfIRSZ6MCytg_S6x28rqlZtqoX99tsvBj6s-aSt_SYdNeuyeUQAsWbu7Rklm3NS8vECUKkCI3JtQsCZk00NbLdnRPa4QsTYQ93NtmziUiVquWpVces5TmUFIvAM0eIet9NptCboMPLpACeF95sdj1weCZHBcRvD_pKkv-X2LHp3u2Bkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K6yvTU8Niod10ADCKa_4jaIg1ICCWPUw_L8cta7qJEL11dH5lijEEXoAdXHP-npuwCeiAj2jeoi564KCi2ho1SaDfHuLy6oQComs5qT2rYCmEXCfMhY_qtoKPZNWFUHIFaB9HibC-d7A8AoHLOgPhcwB51uNBc-816daFV_3mU7bkbnl6f-4LZKHbtj-so0BY5OnkJBlXQ-S8lzEF_l7mpu6it4gX_OyV3aMRwgAhqIv2wcex62TxCWgoaUVYOKkW0dBWPliwbVnOeB_HPuqS-JlQneif8od3NbkmJzvDs5na40_BXJAnNj3TBBFzMFJrFFQTpHliSj7jfj6-CYHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XDkyYMUm9wxXksgw6Jub9FwXP6V5TkQGNSMwGiA0_UtScloUH4-eUydnVpxBLUp827m9BVxkZgYFkkeiJKj9H-iUumLbbk1_R-li9Mk4m4HJ9I2Bnwu1gThdLuIXvRKdjqGyIp18EBZQcbUTuPx1le_GYfqa-FwpEHuGEuMuEFZMSCGwwujDMMm0w92jsX6ySgUqQzatu4PyGbKutxQPeNQt_oV5sF2Vr2GJgneGao70bk74DUDqCglg3ZGXO6kStalGKNz2YvyqDGKjORHrcFk0nQaWgF2gFn4XVDnXlbJ3wYDvb4HJGHImPlM02rAf3RYmeDqz3AKhsvDbI69l0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GvfqcyMqARin79XnxOt90U8LP9Oi0ebItjXXQaNN62HjiLj03-oV_FSH7Vk90xfVQOivuZdpqtrzqm8zDR8h5J0JccnaZRUe5sq7bm5-kf-yWGWaPlw6tur2hU-IJXQT0QVJAl_Cf0RVtIdLonGKFm_HkckfHMIikaKRZ0bGUyrnVLzWkhJVaWPerLO6zdwkpfDQlPBESoYgjSc5H_eIMcpSYdhaCCU83qQgQb-AVQiVxHA4y6Obx-bISsoyQphWqzkDJOPNbRCKt4KcreYfJBeVoFjLOUO9qrUXbPT-Kf276KDdtTV48Kp-ShIOmzszS4sXBrPOTYtRFKBkftiNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
