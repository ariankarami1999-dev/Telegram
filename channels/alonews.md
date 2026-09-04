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
<img src="https://cdn4.telesco.pe/file/SN3MWV-wzQYAq2seln4eToVb3D4kGTvU45xzt3k63VMIPqIGkhsfxSl-eUchaxrsFVeP0PlVM7nPERlEft6S6EKmTAMCUgUPCyCc6oiFvuTcFc7hIczuXMRNfhQ9Jc5_IWX6sMHXTKtHzH6e2zBG-LmurMz41VkTcEACsv-jU9LO8oZhMswM2BC-RXuPj48rRddZYydMjLWzVOn2792ABev6rbk--5PojWwx_9xYDFW2D5Ahk3t1Ddw_NP2NqjBQV9boGe02UK9cpETGBFNoqI4qbUdITPiRyQxILaKDZch6XnAkyn6f6XlVMCmjUb6L4yBBhJCCGF89FZcOBuOt4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 23:13:55</div>
<hr>

<div class="tg-post" id="msg-145640">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4plMtd9lJ8t5-w8QzvusW4-NhLhQj2tbhTZn22BmV50M6am5PRAPQlmHpyEitzEux8x1HeT6y4os_VLGDKVyAriKb-MiVi3dgDQJvr4_5Hgo31oCGDfV6zaa2E4xGciBvYBf_H2jCmPUPrsp8GwwBcjvmvFek67P3W51oy59f76zEkoRmJOjhS-QoLaNtEr02ltG190PJQLzGYoZ1DyZLbAvquH2TbtVhXvZhZR3KgaYTbuWyJ-EOQ3uHoPbG8TBVLKFjjrqm5OfJl2NtEbrv1y4NueZ8lqIvIoWQhNUz7jTX598h_2yuVi61YR4xMLOay-D5moLbUMmgysSbxHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایید حمله پیشدستانه ایران توسط رئیس کمیسیون امنیت ملی
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/alonews/145640" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nMY2I2VOA4Iv_ramIM-OmQz3zlynox_7OuYr7Z2qt2itNFRPx4XWacQdeno5AHh7Oq9aoyk9O6sHPfmmRmVq0ADYWrt7x2TaV7RDnwS_fH_ORS4GenMXTZXOxyqJe3HyQGSIMsJGB5FecHO_KpTz-vKUrzUFDdoc4cYWGPmOhLSQPJC-O3dLQfT9mRGBuIyMLmc9BRp9BqwVzwKFtLwfrXdrx56TpcthxXCe7ntGvpgIIluMV9Q7IcrgVzCDE5og5MHFjRSuGdpEncs95b9ansVwN_nzspx8njfEq175UGLs2KQ0pZGnI4IS3_FjMW52p6SlhU8gVKE4qs_PA55_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
در کمپین جدید صرافی آبان تتر با یک تراکنش 1 میلیون تومانی  200 هزار تومان دریافت کنید
.
💵
💛
احراز پایه
: کدملی و تاریخ تولد
⭕️
برای شرکت در کمپین ابتدا در آبان کلاب ماموریت  مربوطه رو شروع کنید. سپس تراکنش بزنید و هدیه رو دریافت کنید
🔍
لینک ثبت نام</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/alonews/145639" target="_blank">📅 23:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
پولتیکو: ترامپ قصد دارد به‌طور گسترده برای جمهوری‌خواهان کارزار انتخاباتی به راه بیندازد، اما نامزد‌ها نگران‌اند که حضور او شانس انتخاباتی آنها را کاهش دهد
🔴
برخی از این نامزد‌ها در گفت‌و‌گو‌های خصوصی به تیم ترامپ گفته‌اند که به حوزه‌های انتخابیه آنها نیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/145638" target="_blank">📅 23:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ درباره کانادا: اگه ما نمی‌خواستیم با کانادا تجارت کنیم... فکر نمی‌کنم کانادا اصلاً وجود داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/145637" target="_blank">📅 22:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: اگه می‌خواید به‌عنوان یک ایالت ثروتمند بشید، باید برید سراغ مرکزهای داده.
🔴
اگه می‌خواید با فقر و جرم‌وجنایت دست‌وپنجه نرم کنید، به نظرم مرکزهای داده رو تأیید نکنید.
🔴
خب، انتخاب با خودتونه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/145636" target="_blank">📅 22:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
دونالد ترامپ درباره جنگ اوکراین گفت: «در مسئله روسیه و اوکراین یک مشکل شخصیتی وجود دارد. زلنسکی و پوتین واقعاً از یکدیگر متنفرند؛ نفرت شدیدی میان آن‌ها وجود دارد.»
🔴
او افزود: «این نفرت در مسیر حل‌وفصل مسائل میان آن‌ها مانع ایجاد کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/145635" target="_blank">📅 22:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ در مورد تنگه هرمز: در حال حاضر، خطوط لوله در حال ساخت هستند. جاده‌ای از طریق سوریه در حال ساخته شدن است؛ در واقع، این جاده باز است. مردم با کامیون‌های بزرگ حامل نفت از طریق سوریه تردد می‌کنند.
🔴
تلاش‌های زیادی برای ایجاد جایگزین‌هایی برای تنگه هرمز در حال انجام است.
🔴
تنگه هرمز دیگر آن‌طور که قبلاً بود، نیست.
🔴
ایران، اگر نتواند عاقلانه عمل کند، که من نمی‌دانم آیا آن‌ها قادر به این کار هستند یا خیر، در نهایت به تنگه‌ای به نام هرمز دست پیدا خواهد کرد که دیگر آن اهمیت قبلی را نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/145634" target="_blank">📅 22:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران گفت: «به شی جین‌پینگ گفتم لطفاً در موضوع ایران دخالت نکنید.»
🔴
او افزود: «چین واقعاً درگیر این موضوع نیست و دخالت بسیار کمی دارد؛ در حالی که می‌توانست نقش و دخالت بسیار بیشتری داشته باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/145633" target="_blank">📅 22:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145632">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها رادار نصب کردند، زیرا ما قبلاً آن را از کار انداخته بودیم. حالا ما آن را برای بار دوم از کار انداخته‌ایم. اکنون ما هیچ فعالیتی را مشاهده نمی‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/145632" target="_blank">📅 22:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145630">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ درباره روسیه: ویتکاف و کوشنر پیشنهادی را برای پایان دادن به جنگ به مسکو ارائه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/145630" target="_blank">📅 22:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145629">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: هشت جنگ را پایان دادم، اما جایزه نوبل را به من ندادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/145629" target="_blank">📅 22:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145628">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: هر یک از بخش‌های مهم این کشور که ما برای آنها هزینه می‌کنیم، حدود ۶۵۰ میلیارد دلار هزینه دارد.
🔴
ما باید به سطح ۱ درصد برسیم؛ نباید به سطح ۴ درصد برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/145628" target="_blank">📅 22:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145627">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبرنگار: ۱۸ نفر در جنگ با ایران جان خود را از دست داده‌اند. ما شاهد حضور نیروهای نظامی برای مدت زمان بی‌سابقه‌ای بوده‌ایم.
🔴
ترامپ: بی سابقه؟ مگه نمیدونی ما چه مدت در ویتنام حضور داشتیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/145627" target="_blank">📅 22:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145626">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68db4c2c5.mp4?token=L3gdl4Vbkvqyv2FWfcBvVymZqE2wLxRfGuZmRbB-Q5ethmGxG20BZ5V2-QW5taQtm8XIRpnUnseWL8S4lyYGHC6VLzmzdQPl4RTn7qo0wh0xwFogEPxiVhtgqjlxFs4bCVZzFkgT_d4vL22QjNasFyYwJgd25D2hj0_XOi8R-F6gee2EiDwUOiJFnW6_e7DlsmQZCjS_-QCyjnFf5vJbPQuJLWLDjibO3KkBhrmNknuEJXDOOmgdbTdUMdvu43LUY3T0niNde426CI9zWGk6df088wzoP-cG7slYr89uMkr9GxA13SnazeKDalM-YL8oEbVxEKRKEVYiRzyDckCa5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68db4c2c5.mp4?token=L3gdl4Vbkvqyv2FWfcBvVymZqE2wLxRfGuZmRbB-Q5ethmGxG20BZ5V2-QW5taQtm8XIRpnUnseWL8S4lyYGHC6VLzmzdQPl4RTn7qo0wh0xwFogEPxiVhtgqjlxFs4bCVZzFkgT_d4vL22QjNasFyYwJgd25D2hj0_XOi8R-F6gee2EiDwUOiJFnW6_e7DlsmQZCjS_-QCyjnFf5vJbPQuJLWLDjibO3KkBhrmNknuEJXDOOmgdbTdUMdvu43LUY3T0niNde426CI9zWGk6df088wzoP-cG7slYr89uMkr9GxA13SnazeKDalM-YL8oEbVxEKRKEVYiRzyDckCa5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره پوتین: من با پوتین صحبت می‌کنم؛ من او را خیلی خوب می‌شناسم. پوتین قصد حمله به خاک کشورهای عضو ناتو را ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145626" target="_blank">📅 22:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145625">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d6d722f3.mp4?token=SqbaW6HczeYgmukkYtXLhvupFQ-98KTAHYJZbaFjo6_WQliZvYGSirtk5jbSriCB5psOqJuJIbXHzN9rDwea08jOBp1Tzq90ggSSkiOcGOI-BrXFTOsOBYGhwIe55aoUyFfsT8qcIZ2xmFnZu7ajNA-GuA2KTWwisDjYo9eM_2j511Spo1psZYcHJkUAMYGxJGy1ibRqK18ToncmO3y52ar3078QxelvF4oaiXZkYzWitt5pPf5ZeJkppSYo3fJJcqyo_ya1Lmokghs0Jv9nppLUulbZd1cs_3HLjsdgmjpVQsp8GwrYx1ulOZ9D1DoQ2a5EqhJssO0VyIRQQSBQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d6d722f3.mp4?token=SqbaW6HczeYgmukkYtXLhvupFQ-98KTAHYJZbaFjo6_WQliZvYGSirtk5jbSriCB5psOqJuJIbXHzN9rDwea08jOBp1Tzq90ggSSkiOcGOI-BrXFTOsOBYGhwIe55aoUyFfsT8qcIZ2xmFnZu7ajNA-GuA2KTWwisDjYo9eM_2j511Spo1psZYcHJkUAMYGxJGy1ibRqK18ToncmO3y52ar3078QxelvF4oaiXZkYzWitt5pPf5ZeJkppSYo3fJJcqyo_ya1Lmokghs0Jv9nppLUulbZd1cs_3HLjsdgmjpVQsp8GwrYx1ulOZ9D1DoQ2a5EqhJssO0VyIRQQSBQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما ونزوئلا را تحت کنترل خود درآوردیم و در واقع، ایران را نیز به نوعی تحت کنترل خود قرار داده‌ایم.
🔴
در این چند روز، هیچ درگیری مسلحانه‌ای رخ نداده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/145625" target="_blank">📅 22:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145624">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532c884d67.mp4?token=hR71bes4PE5kSXL1Fb2rBAK2NtbrXb13WmEOQujGuZu8VGrAkPwDz1ThS3m6QxzXMQjClQgjFsngmgDpuqjZ3XjocqFjk0tisTb62vAoBi7c9q5DIyutG-Zh05g2TniPyCRZiYFGaOwZbRpeohw_78mGMjiDgs0MZSgNGjomOvgRFwE2hQojm-pe455S0CltHabzRENFktvqN0Ji4-5C-fMFrqSApXbopVcarpTcWtc32vPS1EdcCXF6KanczhYqdEYd6DDQ-P50uK9iWGlcRTOd1Air0HqId6CR0m_HTXPVTGSuv2soMMmzFo31xZ4S-XyeFB-q5ijN-27yiWUTq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532c884d67.mp4?token=hR71bes4PE5kSXL1Fb2rBAK2NtbrXb13WmEOQujGuZu8VGrAkPwDz1ThS3m6QxzXMQjClQgjFsngmgDpuqjZ3XjocqFjk0tisTb62vAoBi7c9q5DIyutG-Zh05g2TniPyCRZiYFGaOwZbRpeohw_78mGMjiDgs0MZSgNGjomOvgRFwE2hQojm-pe455S0CltHabzRENFktvqN0Ji4-5C-fMFrqSApXbopVcarpTcWtc32vPS1EdcCXF6KanczhYqdEYd6DDQ-P50uK9iWGlcRTOd1Air0HqId6CR0m_HTXPVTGSuv2soMMmzFo31xZ4S-XyeFB-q5ijN-27yiWUTq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اگر این درگیری با ایران جنگ نیست، پس دقیقاً چه چیزی است؟
🔴
ترامپ: من آن را یک درگیری نظامی می‌نامم، زیرا برای ما مسئله‌ای جزئی است؛ یک موضوع بزرگ نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/145624" target="_blank">📅 22:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145623">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: رشد اقتصادی باعث تورم نمی‌شود؛ نادانی باعث تورم می‌شود
🔴
ما باید این امکان را داشته باشیم که به جای اینکه همیشه شاهد رشد اقتصادی در سطوح ۲، ۳، ۴ باشیم، شاهد رشد اقتصادی در سطوح ۱۲، ۱۳، ۱۴، ۱۵ باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/145623" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145622">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: اگر یک کشور با ما رفتاری نامناسب داشته باشد، ما هیچ تعهدی برای انجام هیچ‌گونه معامله تجاری با آن کشور نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145622" target="_blank">📅 22:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145621">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5G99L4NcA7BFQigV3EZEdrzh0TAdGNtd77OeGelPjyRdvKyfkJIGl0Ev9qshEXI0ACCo8W83jHHRiRueIA5RJDw_c7m_aiIqjj3DqNEgKP3Rb76NnTAbO7wiBhztXDzE0qgO6scE-Kr5nUCgLLl7LD35V0nfcRmjYIDaQNN65wWFvq9-BiJNV8_E9coofaihAntfZ0cyJCyqQuYuUb9TW09NxwLtZD7VR6VGZabt8oGESy6rV1EEP0iDcUBlO4jggWCWn9flvGkOznJmeZb5SNAbbrLDhsz7JBYFeLOOTvev4lzoiiUFfj3_9QMC16KjLv9-yFAVgepFYgZD7N-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هزینه آبدارخانه شرکت بورس انرژی: ناقابل ۱۱.۵ میلیارد تومان!
🔴
صورتحساب کدال منتشر شده از شرکت بورس انرژی نشان می‌دهد در سال ۱۴۰۴ این سازمان بالغ بر ۱۱.۵ میلیارد تومان صرفا هزینه آبدارخانه داشته است.
🔴
همچنین با استخراج صورت‌های مالی بورس انرژی مشخص شد میانگین حقوق دریافتی کارمندان این سازمان دولتی در سال گذشته بطور میانگین ماهیانه ۹۰ میلیون تومان برآورد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/145621" target="_blank">📅 21:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145620">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95b5c30eb.mp4?token=nJAqduqHAb2qTh8g-n4xj-IqvuUzAzJGp4bBoS4eC1n2o3qDinNpkuRx3WgwHdns4Osx04_DYShVEZP4ewxcyypJhmhMSu-HRxFho9luPjoC_xfGD_koY68mLOC1ntme_Imk1yf8cgtxBrT0D6d6DJF1FnhVnQR8keSg5gyFvDSVaN9hdCmSgpeo39I5ouN27VjcuF9_Qvn0V0oR9j-C_zQurHs26M_wTgTwlhECuCdglzDVxqQAGaomKDzL8wJU46fjFbyISgWvfabRwo9S7X_O52suhYY024wtjxMqtw1_9u2I2k81ShOOQO6bWNfZgxjN99crKZkjejv2NqYHug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95b5c30eb.mp4?token=nJAqduqHAb2qTh8g-n4xj-IqvuUzAzJGp4bBoS4eC1n2o3qDinNpkuRx3WgwHdns4Osx04_DYShVEZP4ewxcyypJhmhMSu-HRxFho9luPjoC_xfGD_koY68mLOC1ntme_Imk1yf8cgtxBrT0D6d6DJF1FnhVnQR8keSg5gyFvDSVaN9hdCmSgpeo39I5ouN27VjcuF9_Qvn0V0oR9j-C_zQurHs26M_wTgTwlhECuCdglzDVxqQAGaomKDzL8wJU46fjFbyISgWvfabRwo9S7X_O52suhYY024wtjxMqtw1_9u2I2k81ShOOQO6bWNfZgxjN99crKZkjejv2NqYHug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر یک کشور با ما رفتاری نامناسب داشته باشد، ما هیچ تعهدی برای انجام هیچ‌گونه معامله تجاری با آن کشور نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/145620" target="_blank">📅 21:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145619">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: با فروش احتمالی بالگردهای بل ۴۱۲ به عراق به ارزش تقریبی ۱۵۰ میلیون دلار موافقت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/145619" target="_blank">📅 21:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145618">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9abd049084.mp4?token=CSXQOY24biT-5CBOnXLICV-Q06Rw-IiRp8MdWmrU3IcYmuRthZ-_3ZY0CSiZqXHR_HAUfeWqVxoaeDoe2VnxULWQ3Wr6iH9EjLesLXubj1CSL2hCa41xA2g6waZOPKw1SyWp74FWpW0G7jW_AlD7urjUNk58zH_ZGNGrLX7ufPYnMBxjZtjd33qvi0PupcMyO2TdZJfzrkMWQZ0Sj1F7XED-_jgyxb3-a5s-9byZE1hZJTgPLzHF_zCn0qlvbN7XKBrZPYPPq04Q7QhhgW-8s4IXc4p9No52xu3PPvhETDUwjVL2rkUL-d22kk80hYVwP-KVtJvkWBzOCoRTPU9Siw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9abd049084.mp4?token=CSXQOY24biT-5CBOnXLICV-Q06Rw-IiRp8MdWmrU3IcYmuRthZ-_3ZY0CSiZqXHR_HAUfeWqVxoaeDoe2VnxULWQ3Wr6iH9EjLesLXubj1CSL2hCa41xA2g6waZOPKw1SyWp74FWpW0G7jW_AlD7urjUNk58zH_ZGNGrLX7ufPYnMBxjZtjd33qvi0PupcMyO2TdZJfzrkMWQZ0Sj1F7XED-_jgyxb3-a5s-9byZE1hZJTgPLzHF_zCn0qlvbN7XKBrZPYPPq04Q7QhhgW-8s4IXc4p9No52xu3PPvhETDUwjVL2rkUL-d22kk80hYVwP-KVtJvkWBzOCoRTPU9Siw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین پاک خبرنگار مقاومت در جنوب لبنان: منطقه علی الطاهر سقوط کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145618" target="_blank">📅 21:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145617">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWujYjioO20AjXtGgyPKXN9oH4FdEv7qk9q5V1uwPvSBTtFqUZb3qeI5dKOEjiOF-YadMQCQzWTvT0PnlRexE5yFUMFXm469MyZkZ34fZi7t34W6HpXO_cNYoxssfMKkvJWs-Tfr3NYq7Gb3mBScBWckzl4tUt3FeV2RAe3OAK_lgv3sRrUFEXcwKnxhCSEjU5uL-YMbS2WWH-B9f1vAsaOWBlkH0Ee8H8XT9k2pUAeBgggYGEstWQLsoujtXbyl2OJjGAhVM-xXHzUE9gG-3ZbjO0T61JmlbBM__oZS-m30g20zxNtRrZ3lZaRBGOB7u9cpE9dZ1bfbazNa7LH82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه NBC: سربازان آمریکایی پس از درگیری با ایران، دوره استراحت خود را در یک تفرجگاه گردشگری در تایلند سپری می‌کنند؛ در حالی که فضای متشنج ناشی از جنگ با ایران همچنان حاکم است. این صحنه، تضاد میان فضای تفریحی تفرجگاه‌ها و وضعیت آماده‌باشی را که ارتش آمریکا به دلیل جنگ در آن قرار دارد، به تصویر می‌کشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/145617" target="_blank">📅 21:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145616">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T22MUkWbqcDuIqeRCPTbzRo1B349jZCGYs6pkUxP_E6KRyPqDSvaPnA_JtyqBZXZQASekJ2jSMjq3i56phyIdw3qksptyo8ymLvH-dxutb5abFNVxmokgj42GJP4DCE7s7J8LfWSl6wZAI5sd9Gf13kMmk_r4fdtOYSHtED3utVNpujemdQngzVFUQxyTxrWWN4wWWONPbE04kN1HCzbJ3k3Pd4L9RW1X1EF5MrM0iSA46LJstO2mgSmphFTeJeGgbUb3JKUhtHkJ-XpHwS6rf9il8NMoRZSXFx6rVvux0YH1ay0ivi-L0vsWc4WhUEd3fZDfwG6ug1lDpB0H_aKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وب‌سایت رسمی کاخ سفید بازی‌های ویدیویی راه‌اندازی کرده که در آن‌ها کاربران مهاجران را دستگیر کرده و دیوار مرزی می‌سازند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145616" target="_blank">📅 21:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145615">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
به گزارش سی‌ان‌بی‌سی، آمریکا یک بانک ترکیه‌ای را به اتهام تسهیل فعالیت‌های مالی مرتبط با ایران تحت تحریم قرار داده است.
🔴
هم‌زمان، اسکات بسنت، وزیر خزانه‌داری آمریکا، تلویحاً اعلام کرده که در مقطع کنونی برنامه‌ای برای اعمال تحریم‌های بانکی بیشتر وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145615" target="_blank">📅 21:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145614">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKOOVm7TUTAJH5VaXUpZVlz-ooZw2i6dXSTX_TPyW1au4ncpb0OVY__GQzytFJslwMyCenrO-vdQcnOx9vbmEAnfXNLX9IQW-uCp3v9qWZuE8KucqwhEePabVUJXcIWYGHeO3nrNZLkuS7kuFcrRHt2mm-qwF9JH6foF9ATRXgB6szLw2hOKX4A3sotLi0wXWIkgvozt7fUMu6LVLRVdUO6IkBwy7wQaas1XgEbCFjgl74s2y5OkWVs3kBYTolJqgVMSY40lPfQw2uCiAh44oGkA_aq69DKt9xooKTJYRwXE7WECJJl7Iafc9tXQCLTQTnU4RQ_DvMHmMKbhgNJ1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرنده همای سعادت تو طالقان دیده شده:
تو روایات دیده شدن این پرنده باعث اتفاقات خوب برای مملکت میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/145614" target="_blank">📅 21:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145613">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F810VOGXaXuK_MjNJ0qNXJD6DS_ITq6pWN68cBIbScotxxVXcozqooFKNPUFfnxmVa_4rBOV7dlmvh020qNYRrtgF9WzklDT20D2zbUPohcwhRhK9QW4OVR5fVOEruPjedPIfTF4e-omEBnpKXh1tD1PgKrDLdOBFvJe0xiZmSTXsYxGedHESyb5YBLiynRXTvanQ3UlROpRA3375_Xp3BJZEoVnd1SSFmM7VEmgO6rEUkxiUYplw_2p1j67dgnXUq8EBhu4Gzp0crCQEEL902mcj1zU6-FJw1Mae47zZm7Gz3ibgEaIBOObdCLAqETUiXdmxrVPv9ks23Tp_SA0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این متن رو داری میبینی
یه نشونه‌ست برای آغاز مسیری جدید از زندگیت تا یاد بگیری که چطوری،خیلی سریع به موفقیت برسی!
💸
✅
اگه میخوای درآمدت چندبرابر بشه
💰
اگه میخوای لایف استایل زندگیت متحول شه
💡
وارد کانال شو بهت یاد میده چطور دلاری پول در بیاری
اینجا میتونی روزانه درامد داشته باشی و سرمایتو چن برابر کنی.
لینک عضویت کانال وی ای پی
✅
👇
👇
https://t.me/+nTm6gDB4A8gyYmFk
https://t.me/+nTm6gDB4A8gyYmFk</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145613" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145612">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt5TLGTVdpV0c9S5oAUukpUyE4ibfCONoNYiDIMx5TIE_85Oe_xiXkyDbpd0-ckJL0wTYC9lHFKREML97gNZmTknFrPRWa5Agbt_mnfCCXO-D3VdwMrOqttheqyz8-0OXvEbqzpj73JgzPJKx9QS_VQ4YqFD4xqvS8HjyRiJSK2AGQCHLV4J_TkzJrycH5y8FjN0dULd_KmRT7Shstwk5SYQj9fKD0HgDJB8XkiZYGMpM4E-MmIz4M1jWxUYYr-u24SMhLRYi4WrqYYX8-XgrnB4lQpBYLsSGomiSCidn8sU0LUBFNG3dnRmCFJjOYzFz-hnecmwGi4x-KBRGSb3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
نفت آمریکا (WTI): ۹۰.۹۰ دلار
🔴
نفت برنت (معیار قیمت جهانی): ۹۵.۶۵ دلار
🔴
نفت امارات: ۱۰۲.۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145612" target="_blank">📅 21:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145611">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قرارگاه خاتم الانبیا:  حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/145611" target="_blank">📅 21:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145610">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از مقامات امریکایی: ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد ایران ممکن است به‌جای مذاکره به دنبال طولانی‌کردن جنگ تا انتخابات میان‌دوره‌ای آمریکا باشد
🔴
تهران درک روشن‌تری از توانمندی‌های نظامی خود پیدا کرده و ممکن است در حال بررسی یک تشدید قابل‌توجه تنش باشد
🔴
ممکن است بار دیگر به سطح تنش‌ها در ماه ژوئیه بازگردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145610" target="_blank">📅 21:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145609">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سخنگوی ارتش: سیاست ما عوض شده و به دنبال حمله پیش دستانه‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/145609" target="_blank">📅 21:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145607">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7d1ENEltAEbvWAR_kqngNVNLWKzC5UCrYW6Gbi4XeiljvI4bDlQHD2UyfzzzhYylS9jU0_g_La1xfWq6-7meJQCku4aIQaFQ2Bv9nmSvhlZt2AP4xnNEmX0NkH8ocAsCeaWQ5yae3LwkpM5FBuOsRPeDFU6pW6pWz1J0UjjxI5ailg9ixZJmdglbpQ8VZPYd4nnpLet6po27254s8jUXKPGS8SHkFmOAXEMTVFTlvYqukjWCQua2w1bPn05pIMfrBQSlabGpk8F_Nm0NFMZiVQqzks7k0-SI1urvr8uywvx6pjqoIzdVT5dzU9PVZd677FH7WxNrlQ6M4WVqeST_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: تأکید چین بر پرورش امنیت مشترک، اصلی را منعکس می‌کند که ایران مدت‌هاست از آن دفاع کرده است.
🔴
کشورهای منطقه باید آینده خود را به دستان خود بسپارند، و ثبات واقعی تنها از طریق معماری امنیتی جدید بومی می‌تواند به دست آید. ایران آماده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/145607" target="_blank">📅 21:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145606">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کانال ۱۲ اسراییل:
امشب جمهوری اسلامی شروع کننده جنگ بود و به پایگاه امریکا در اردن موشک شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/145606" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مقامات آمریکایی به اکسیوس می‌گویند هیچ گزارشی مبنی بر شلیک موشک به سمت پایگاه‌های ما در اردن وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145605" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f8f7a2582.mp4?token=nHJcCdjDamx8uWtZOrOyEP1vwrRJQZeHyJYd9vuxRNGLj5qeyMOqHPLgNOsdMEaod1K3hry3aSNKrax8ZwNJdZFswqC1abTxFkIqXcEhagMrYZ1q2sF7hiZXok1e1MrM4EGvGzgssGdlFwk9MLlFrk-tOj9NCC41cNveHgER5r1ouP4WQLOOussDLHkL0lg5qms7v5v7-Ow7_ndYaJjzYWqF0Ng2y0u4qCvtKnISMtd2Hci_Yx_FZiZ9LawwbRVVBLMnykdv4uvgaNiTXochNKlIOzI10QO_9ReHpirTfqG83im4YYJd0ZbMQuwzm0kCPHTsVhuW3dqTeQk24pcgLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f8f7a2582.mp4?token=nHJcCdjDamx8uWtZOrOyEP1vwrRJQZeHyJYd9vuxRNGLj5qeyMOqHPLgNOsdMEaod1K3hry3aSNKrax8ZwNJdZFswqC1abTxFkIqXcEhagMrYZ1q2sF7hiZXok1e1MrM4EGvGzgssGdlFwk9MLlFrk-tOj9NCC41cNveHgER5r1ouP4WQLOOussDLHkL0lg5qms7v5v7-Ow7_ndYaJjzYWqF0Ng2y0u4qCvtKnISMtd2Hci_Yx_FZiZ9LawwbRVVBLMnykdv4uvgaNiTXochNKlIOzI10QO_9ReHpirTfqG83im4YYJd0ZbMQuwzm0kCPHTsVhuW3dqTeQk24pcgLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری که به طور ظاهری پرتابه‌های موشکی سپاه پاسداران به سمت اردن را نشان می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/145604" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
گویا سپاه استارت جنگ فراگیر رو زده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145603" target="_blank">📅 20:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/پرتاب موشک کروز ضدکشتی نیروی دریایی سپاه پاسداران از سیریک به سمت تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145602" target="_blank">📅 20:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
این حملات بعد اولتیماتوم فیلد مارشال محسن رضایی به ترامپ انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145601" target="_blank">📅 20:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
فعالیت‌های پدافند هوایی در شمال اردن، به دنبال گزارش‌هایی مبنی بر پرتاب موشک از مرکز ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145600" target="_blank">📅 20:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/هم اکنون آغاز حمله موشکی ناگهانی سپاه به پایگاه های آمریکایی در اردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145599" target="_blank">📅 20:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/هم اکنون آغاز حمله موشکی ناگهانی سپاه به پایگاه های آمریکایی در اردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/145598" target="_blank">📅 20:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دو موشک بالستیک حوثی ها مواضعی را در جنوب مستقیم‌الخواخه، در جهت حیس، در جنوب‌غربی یمن هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/145597" target="_blank">📅 20:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlLVL-_pD6-nV5sfDAQLpUL6IaP70MnA53ogIlt9yGHoqNqwVyDQbVCoGJIDgd6HgeAi9RIZAKJ0MmWUitUuEzkfPNmsHnrRaRIDuqPsArDNODAXODJbzhEbJVLGeIajh6ytVM2kuqAmnD4A_DY4YMifCOFtSXMWH-73ie_59bZCqJO7Cq-pBY94YZ82I56aMNW2pvZqiUTc8WKZ2gR5NIddXlZWb6dsd2wXz0UNBevW0earpO62FC0uF-Hn7sGocUoSn5cyZxJdjR04R2w6yhgwR9SKZceN7POZ1d6IANcTZ_Um5yAITstPu2F0kNZkpJu3DbbI0zDJa-_kea7kIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
چپ‌های افراطی و دیوانه، دموکرات‌ها و کمونیست‌ها ترجیح می‌دهند ما در جنگ با ایران شکست بخوریم، تا اینکه دونالد ترامپ جنگ را برای آمریکا ببرد.
🔴
به عبارت دیگر، آن‌ها ترجیح می‌دهند ما ببازیم تا اینکه پیروز شویم!
🔴
این‌ها آدم‌های بسیار بیماری هستند که از TDS شدید رنج می‌برند؛ همان چیزی که گاهی از آن با عنوان سندرم جنون ترامپ یاد می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145596" target="_blank">📅 19:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecaed841d6.mp4?token=kXvXcXsKYZGy48pUUNcIyuWtMOkeTyZImDjgbk7WGli-JEJkQMyfk3fDsxZi0WHeoE4VHQAc9WIVhmBLJFMcrcElbBsOK9Nl4ySvjl6ODSzkepqpvauSmHU7Qjc-M_vFuh7VsdRpUmN8bEbWONUsfCXP4XooDtiKXsBTp7vj_8CEhC8OIU8-Q105lAhA75Mp2TjY9M6dBDgIrZRw-zGOkeVk7cFbFTG_H3DIkPxsi5nXFn9mRZX0VaGyiAUUOGkndfZH8CDZ9H47S09Vt_UmMRl_LOuKbkhS7ImVjrEYsu3i9FUcCob8gyIq1q_IrH6MWWknex9w_i7s-y-mVn6FYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecaed841d6.mp4?token=kXvXcXsKYZGy48pUUNcIyuWtMOkeTyZImDjgbk7WGli-JEJkQMyfk3fDsxZi0WHeoE4VHQAc9WIVhmBLJFMcrcElbBsOK9Nl4ySvjl6ODSzkepqpvauSmHU7Qjc-M_vFuh7VsdRpUmN8bEbWONUsfCXP4XooDtiKXsBTp7vj_8CEhC8OIU8-Q105lAhA75Mp2TjY9M6dBDgIrZRw-zGOkeVk7cFbFTG_H3DIkPxsi5nXFn9mRZX0VaGyiAUUOGkndfZH8CDZ9H47S09Vt_UmMRl_LOuKbkhS7ImVjrEYsu3i9FUcCob8gyIq1q_IrH6MWWknex9w_i7s-y-mVn6FYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر پرتاب موشک از اصفهان منتشر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145595" target="_blank">📅 19:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751015f665.mp4?token=PVlz1QtOkYpFsEZiquWaFkaBSFeI61dR9mVGRm4evFgNq-AkFLmk_Zv_dd7P0pSLumSmCO3AaTFTzilNOjPW8xaGnsmCqLjx39r3LhhykKV1kgnTKSquwJ3gwfYHvO3Tvu5QTixNit8PVJCPWUkamPRqSwTlAZgA-slZDbNnZ1ymO-H6eWKu99UYm32132PHf-qb5H0PG57jj80RWHLA7fMU3leM0WrnXERVe0X9UyePYYbi2Nu7fGIS5fV6Kygl0Qh_g9jf6CYzT6kr11yBwBWBHmEnraOpDah2zdzpXJ0vxCU7TOpfksHrzOkcxLScHHRhbMlzAsPp8vV-si9gAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751015f665.mp4?token=PVlz1QtOkYpFsEZiquWaFkaBSFeI61dR9mVGRm4evFgNq-AkFLmk_Zv_dd7P0pSLumSmCO3AaTFTzilNOjPW8xaGnsmCqLjx39r3LhhykKV1kgnTKSquwJ3gwfYHvO3Tvu5QTixNit8PVJCPWUkamPRqSwTlAZgA-slZDbNnZ1ymO-H6eWKu99UYm32132PHf-qb5H0PG57jj80RWHLA7fMU3leM0WrnXERVe0X9UyePYYbi2Nu7fGIS5fV6Kygl0Qh_g9jf6CYzT6kr11yBwBWBHmEnraOpDah2zdzpXJ0vxCU7TOpfksHrzOkcxLScHHRhbMlzAsPp8vV-si9gAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: نفت ۴۰ دلار خواهد شد!
🔴
در واقع فکر می‌کنم بعد از این، در بازار نفت با مازاد عرضه زیادی روبرو خواهیم شد. احتمالاً قیمت نفت خام را در محدوده ۴۰ تا ۵۰ دلار خواهیم دید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145594" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145593">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=uNjmA7cXmoI7ZKZGfyzXy544NdC9_24AjrWWRvoikdNnq4lIgip6ktw_Y2H1Ogxtkrk_Vc20pGgY9w1jZ58m869pvJXvZ5QYqJSjByNNGO8wAihHzSfiMXJPUB-wsROSifvJEuyqxTcsbu0lqSBShtVUtfW8j7TmB24TTfaBDbVCTQHbZS2qkpE6gziPGmHzUxmSI4SP9L2UrTig4ZSolCGNJKexUaxre0IaDc7NWcPDzCo-PeNUnT-8jEOJpq4IU3EP_g-PpQVE-_dWiXAens_w0giRkMVVy9CEDNyXkDmY7DbDl7vzGLDM2blV2kog6JwlIgGyI9Z7U0-9EY4c-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=uNjmA7cXmoI7ZKZGfyzXy544NdC9_24AjrWWRvoikdNnq4lIgip6ktw_Y2H1Ogxtkrk_Vc20pGgY9w1jZ58m869pvJXvZ5QYqJSjByNNGO8wAihHzSfiMXJPUB-wsROSifvJEuyqxTcsbu0lqSBShtVUtfW8j7TmB24TTfaBDbVCTQHbZS2qkpE6gziPGmHzUxmSI4SP9L2UrTig4ZSolCGNJKexUaxre0IaDc7NWcPDzCo-PeNUnT-8jEOJpq4IU3EP_g-PpQVE-_dWiXAens_w0giRkMVVy9CEDNyXkDmY7DbDl7vzGLDM2blV2kog6JwlIgGyI9Z7U0-9EY4c-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده، بِسنت، درباره جمهوري اسلامي ایران:
ما یک بانک دیگر مرتبط با رژیم ایران را تحریم کرده‌ایم. هفته گذشته، یک بانک مصری با پنج شعبه در دبی را تحریم کردیم که ۱.۸ میلیارد دلار به رژیم داده بود.
ما امروز یک بانک دیگر را تحریم خواهیم کرد و احتمالاً هفته آینده نیز یک بانک دیگر را تحریم خواهیم کرد.
ما به سیستم مالی می‌گوییم: بازیگران بد، ما می‌دانیم شما کیستید. شما می‌دانید که کیستید. تمام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/145593" target="_blank">📅 18:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=W_49c67_mf88iyE-9USKie6YpTMvKfPNY33jkkI0Qd7lv59AG8ZbhXRRCfhgeY1YB5_UmWQwPwZsFKUg-0qjlABAufodvwVmho67I0KO4U2LuxIJ2TTjkwbOENAVJqyWitx18iLidNqZ3TZwKccUstDdEQ0NkS-plAacix0_DgUgOldLgpQKTeTfkvsFmyhtsO04zfyYXxt2Z_tBZOgQr1hAZOsrE4LEGi9p_fVej7_Czl1AzMMJ2kD4Vv2Qrb9MaX3NqiOX4gi40IvPuEiIKFWEbVji7v8yqR2TcnhZBovMN4t98lAUJV5GKdJLH9s11GGLBxdzTuECVC85ZbKm9qS_lVQ4gY__4NPr4Yjz_0mE_EkEeRRvqlZN2sjSgi3nvUnnifLoKts1XyVRaMxuLkIigzMrng9CarexUNVa07_HPbgWEVLitPQ2KSEDBGlBIvD45I1rnyz3RaoQAkzBjq3odcQ6fwMDFS7YFuxl6PHwOrMGMuucHghhbWwePzefCFCwaiFfUoUb9HimP5Z-LWh9w7iFuOKBXRzuwAoWveyI8FurQYnClHfCaOqzhcKbRMy31ygr_uwT6mMjzsGv5wFF0MrLa1pCI4Ku0P5FfOhGWPTrFW8EK2hEUOc5Z5EJ0rOEiE_QJ81bbYj--408N-qcAJ7X3ekghTcQ25QjLXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=W_49c67_mf88iyE-9USKie6YpTMvKfPNY33jkkI0Qd7lv59AG8ZbhXRRCfhgeY1YB5_UmWQwPwZsFKUg-0qjlABAufodvwVmho67I0KO4U2LuxIJ2TTjkwbOENAVJqyWitx18iLidNqZ3TZwKccUstDdEQ0NkS-plAacix0_DgUgOldLgpQKTeTfkvsFmyhtsO04zfyYXxt2Z_tBZOgQr1hAZOsrE4LEGi9p_fVej7_Czl1AzMMJ2kD4Vv2Qrb9MaX3NqiOX4gi40IvPuEiIKFWEbVji7v8yqR2TcnhZBovMN4t98lAUJV5GKdJLH9s11GGLBxdzTuECVC85ZbKm9qS_lVQ4gY__4NPr4Yjz_0mE_EkEeRRvqlZN2sjSgi3nvUnnifLoKts1XyVRaMxuLkIigzMrng9CarexUNVa07_HPbgWEVLitPQ2KSEDBGlBIvD45I1rnyz3RaoQAkzBjq3odcQ6fwMDFS7YFuxl6PHwOrMGMuucHghhbWwePzefCFCwaiFfUoUb9HimP5Z-LWh9w7iFuOKBXRzuwAoWveyI8FurQYnClHfCaOqzhcKbRMy31ygr_uwT6mMjzsGv5wFF0MrLa1pCI4Ku0P5FfOhGWPTrFW8EK2hEUOc5Z5EJ0rOEiE_QJ81bbYj--408N-qcAJ7X3ekghTcQ25QjLXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا در مورد ایران:
همه می‌خواهند این وضعیت به پایان برسد. ۴۷ سال است که با این رژیم شیطانی زندگی می‌کنیم و مردم جهان از این وضعیت خسته شده‌اند.
مردم ایران، مردمی بزرگ هستند. اما متاسفانه، یک رژیم سرکوبگر بر آن‌ها حاکم است. یا این رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، وگرنه باید ببینیم چه اتفاقی می‌افتد.
ما آن‌ها را از نظر اقتصادی به زانو درخواهیم آورد. آن‌ها در چیزی که من "چنگال مرگ اقتصادی" می‌نامم، گرفتار شده‌اند.
ارز آن‌ها در حال سقوط است و صادرات نفت آن‌ها به صفر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/145592" target="_blank">📅 18:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا یک شرکت مستقر در ترکیه را در چارچوب محدودیت‌های مرتبط با ایران تحریم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/145591" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e30b8bea.mp4?token=Rt6xd1jA3GkyAYlVqBRCm-L-oiieBlkC_mODTc5e9HC3s4jgBnYxzXHn_5hDh473v34DE_MwaI5i_qopIRX3YTPJuUtShxK6JC9tHf7O3EKhFWqQa-p9lMBP4_2T3NvWR6AUe7qRf13KJzCuLcYVm63r94DaP5iGTnnYmQUh7ukjDlfFGr_F6lRZN7dqAz6LiuHBJCWtPsrFORBJtpNegT4o9ub9TQlxG8_-e41GRCTc64CuJ7MjIWl5l7hdpN0pHUulwRUVqdbUdXAyidWlq5so7sJzqah5kZDc21JnmLb6q0fimpyouFffr1zzm1dM7qphG42t0TYTSvKf-Gx5iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e30b8bea.mp4?token=Rt6xd1jA3GkyAYlVqBRCm-L-oiieBlkC_mODTc5e9HC3s4jgBnYxzXHn_5hDh473v34DE_MwaI5i_qopIRX3YTPJuUtShxK6JC9tHf7O3EKhFWqQa-p9lMBP4_2T3NvWR6AUe7qRf13KJzCuLcYVm63r94DaP5iGTnnYmQUh7ukjDlfFGr_F6lRZN7dqAz6LiuHBJCWtPsrFORBJtpNegT4o9ub9TQlxG8_-e41GRCTc64CuJ7MjIWl5l7hdpN0pHUulwRUVqdbUdXAyidWlq5so7sJzqah5kZDc21JnmLb6q0fimpyouFffr1zzm1dM7qphG42t0TYTSvKf-Gx5iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتشر شده در ایتا
‼️
بمباران ناو جرالد فورد توسط جنگنده آذرخش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145590" target="_blank">📅 18:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4589b78c3.mp4?token=F1MjZy-ijjY9LY5LZFlsvH-J8rOMqcdiliqNNJTenP6EAad2HSWXpP1kHTtIN36MzPV3ALOTpRfSBoAdetUcSNGLSxIGibck3s6BqdYjgv9mAeQMHpkUSu3CbcqbDF9hti7ks6VRJJRRHV_hAX0NV-rOz5avPacPLzL7poSmVNZLQtv_91_iCFuy_lf-T6XrDXlreUJjzFL3NOBX7oeuZq1SmPzCCI7g3gOBXPBHRvw3-y9yZoERR9mQcqDfr71iRyjhgIMIqAaJ8xZ4KYwgqZX_DuIgS-h0eLu5_niYRauo69vVSpzNgek5dQFc6R9qFJQ7T1qGQUN5i5Y7LUSCdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4589b78c3.mp4?token=F1MjZy-ijjY9LY5LZFlsvH-J8rOMqcdiliqNNJTenP6EAad2HSWXpP1kHTtIN36MzPV3ALOTpRfSBoAdetUcSNGLSxIGibck3s6BqdYjgv9mAeQMHpkUSu3CbcqbDF9hti7ks6VRJJRRHV_hAX0NV-rOz5avPacPLzL7poSmVNZLQtv_91_iCFuy_lf-T6XrDXlreUJjzFL3NOBX7oeuZq1SmPzCCI7g3gOBXPBHRvw3-y9yZoERR9mQcqDfr71iRyjhgIMIqAaJ8xZ4KYwgqZX_DuIgS-h0eLu5_niYRauo69vVSpzNgek5dQFc6R9qFJQ7T1qGQUN5i5Y7LUSCdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از لحظه اصابت پهپاد روسی به ساختمان مرکزی سرویس امنیتی اوکراین (SBU) در قلب کی‌یف
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145589" target="_blank">📅 17:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t-LkaELWTwWbeeXEBRnp8u2OvogEOKV37s-GzuovdqlzSnByGu0cqFVTEP49HpgEFrcj7TYHI2AJWKYlc_vJsQpapFk1iDTjMgFRZvf49kAjAkXB7FhgRQQ1jyB41MxSFPYB6E7Eo_VadzdldNTdztmQ2gKVw8YRdYniFvwQhwX-9lxFv_OTwFXO5SDEtXwNmv7A_ZbZvXU4q7qcDEPVGUc2V-iqhHHR5Yam2GStUkL5GSBvmGMskw3ITtcYgxTHQHAvD5No58uuKFzgT1GbOFHL0s1V85gob9C3h12T28N8JkkNpF0XRPmEkVgp6oT7aQXTxPdu8qhPmUtc5L3HIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با کاهش قیمت طلا، ارزهای دیجیتال هم سقوط کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145588" target="_blank">📅 17:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=ABfv8l1x5WymMDhrT6mmy9MlGah4quIz_rAEwXQSxhBhtdPfx0fI6oUkMgMXPtT_SHypv-s8WfSO-uQmAnIEjcgdbbcZgUVnOPr6WrI3FT87qIGzxHDEkFNb4cA9X8tn5Y5IFYtVDH5CCih4U4djwL-vScKMN1nc4RieIR-u0QZ2AJpyBJL5ysA0XJ5Z3IV7u3RphXxdhLTRVqevuQL0OYbJMfN8nPcEPJeCr55TVcezodPTd2FuE_d5ESouWTzUI7Inkaeow39mDl_uzoexLCPMfAJ_JGBEzOJjFP8a3ozRpoZTZcOVlbPG65rGlUiIIZ3jfBA5KsCZ57iliW_fRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=ABfv8l1x5WymMDhrT6mmy9MlGah4quIz_rAEwXQSxhBhtdPfx0fI6oUkMgMXPtT_SHypv-s8WfSO-uQmAnIEjcgdbbcZgUVnOPr6WrI3FT87qIGzxHDEkFNb4cA9X8tn5Y5IFYtVDH5CCih4U4djwL-vScKMN1nc4RieIR-u0QZ2AJpyBJL5ysA0XJ5Z3IV7u3RphXxdhLTRVqevuQL0OYbJMfN8nPcEPJeCr55TVcezodPTd2FuE_d5ESouWTzUI7Inkaeow39mDl_uzoexLCPMfAJ_JGBEzOJjFP8a3ozRpoZTZcOVlbPG65rGlUiIIZ3jfBA5KsCZ57iliW_fRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145587" target="_blank">📅 17:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145586">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orIbF-5D6OsQHDN_X2u2lBsReUFJuJOOlVyUFwFi3sVEw8ELP_ETqKlMpP0iWlfBIO66c43Mg9awLjkBFdG4tnsiSwvuF5yeCqXGXE4Jc3I5A4HWciUgmfPQaWYfQjoAc214z7RKfeMl2OYKYGGNXo-imz_YAImhVt0Wn-6uyHTWJY-XSMoMOr2uogEm9MBngNtcVY6w84L88GJgvJKFA4w_Ofe-8CRm3NEVC1kGusDv5MhmUnM6TyDe8C8fEE3ZJpwjHFwcjz56JOZKewgS7XbN6vKK40mIibKlHikMD0U-NK-Y4CJxkgv7BMcS0_2c-0UDi0_ou-AoylFtxZb2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استقرار ۱۲ فروند جنگنده آمریکایی مدل F-16C در پایگاه هوایی "شاهزاده سلطان" در عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/145586" target="_blank">📅 17:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سی‌بی‌اس:  بر اساس گزارش سی‌بی‌اس، پنتاگون از نظامیان آمریکایی خواسته است هنگام صحبت درباره جنگ با ایران، از عنوان «عملیات خشم حماسی» استفاده نکنند و تأکید کرده که این عملیات رسماً در ۵ مه به پایان رسیده است.
🔴
نکته قابل توجه آن است که پنتاگون بر پایان این عملیات تأکید دارد، در حالی که پیامدهای درگیری با ایران همچنان ادامه دارد؛ موضوعی که این پرسش را مطرح می‌کند که واشنگتن دقیقاً چه اقداماتی را بخشی از جنگ می‌داند و چه اقداماتی را تحت عناوین دیگری تعریف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145585" target="_blank">📅 17:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2SlCDiaV2CiQJeT-30zSUV4-s1O0OjEm6jY42quq1Z-TxiL_LPKB5PGUiIi6O6MW1NePUhsmWjdc_rKXBZXqHR00Uj_3yryJkbURDg9MrF1JLpaww-veC4IfHUUjGgpf4iymS6pzwz7FXrnul9KNLOrh6Ys1-fmPpApEDpoYN-bup1NvGGOxt9u2IX7raJ5hXLQCwf6_qRvumKrWnmCY3aAnzw06WV2XNFlJBxG_ZLGAQBaM_2L5cZSw7Al_Tzg9yll-TfwYHOhgGA_paKGrLhWiE3JReoFJ5_XxH7-PWVQNLj2eqNeNKiGpmtI91WdISaLR98lD9m_DaUz82ViQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت سکه نسبت به ۱۰ سال قبل حدود ۲۰۰ برابر افزایش داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145584" target="_blank">📅 17:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b6764494.mp4?token=HnKvPLUGk1eM0EtZPpZAtBaf7sn2mbvP8VphmR7v7oGbk_9rSQBdpC9-MyN2Ye5kU4bV-L10OZXrWqbyA3UGU3BGNHCBevw_9VQTJ0QMETgwhBvHKzoIZRXfhDAd5bp00FzzRkbFGdTLudp_mCNF0ciGWXLJIKOp5VGvXs5V4O5aSzt_y3XnbsmdK_7EoDqhm5f7f3USzQW8ADrNzhlFO-p_f78p9RgOeS6b_LWNAuliBRUPnJPwfhoiUNIkNWfgwXxJhO5mHjo6nWKs-hYGFohD81KdnBohM-EyKrhizxBVycgc6msOmKMODNdDXTL64Cu7S-YJ5oSICYUuvVZgAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b6764494.mp4?token=HnKvPLUGk1eM0EtZPpZAtBaf7sn2mbvP8VphmR7v7oGbk_9rSQBdpC9-MyN2Ye5kU4bV-L10OZXrWqbyA3UGU3BGNHCBevw_9VQTJ0QMETgwhBvHKzoIZRXfhDAd5bp00FzzRkbFGdTLudp_mCNF0ciGWXLJIKOp5VGvXs5V4O5aSzt_y3XnbsmdK_7EoDqhm5f7f3USzQW8ADrNzhlFO-p_f78p9RgOeS6b_LWNAuliBRUPnJPwfhoiUNIkNWfgwXxJhO5mHjo6nWKs-hYGFohD81KdnBohM-EyKrhizxBVycgc6msOmKMODNdDXTL64Cu7S-YJ5oSICYUuvVZgAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله توپخانه‌ای اسرائیل  به شهرک «بنی حیان» در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/145583" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:
سفیران ویژه آمریکا، ویتکو و کوشنر، به مسکو و کی‌یف سفر می‌کنند تا در مورد پایان جنگ مذاکره کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145582" target="_blank">📅 16:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145580">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO8rZ59_dxJ9Ul0vkywIewofYSB1FfZeXK9zZJKiwQqQNtimtPVKcHHrwqiZvow2JyCja5S5P_EYKNyx_sL1nYyNAUgJohOFI4ut7e-6aGudUT_-rW1icM7TqvwSjy1I8sTWaPDnxhf_251D1PZR1h1JCIwOLaNtmr2WuWKpHtYn7JLz-zclAq5apQSlwD36m87RESF8hlA8Hwlw0t1yBwApQ5Rv3_DEL4hGUEPQ_mOJBrC6yh3-rKz97QWslvUUR-1dAGdFn0FfL439pLtzP5pkmPoiLUVzK2hyUHBqeEzvd21P1sLJz3uyiKTR_cnpdYeTnLdktsVz2LbfZWgWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل فرمانده حمله به سوفا رو ترور کرد
🔴
ارتش اسرائیل یه فرمانده رو زد که حمله به پایگاه سوفا رو هفتم اکتبر رهبری کرده بود. این فرد تو نگهداری گروگان‌های حماس هم دست داشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145580" target="_blank">📅 16:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145579">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
انجمن اتومبیل آمریکا اعلام کرد: قیمت هر گالن گازوئیل به ۵.۸۵ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145579" target="_blank">📅 16:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145578">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سپاه هفته قبل: اگه اسرائیل به تپه‌های علی الطاهر حمله کنه با خشم ما روبرو میشه
🔴
اسرائیل دیشب اونجا رو فتح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145578" target="_blank">📅 16:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145577">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
قیمت جهانی انس طلا ناگهان ۱۰۰ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145577" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145576">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7wPttF1EX4RMVIKljtaQleIMmoOI0ArGuoAuTQ370jExYcy9UwFLjgdv6yqLLszXevJ9c-3M5fOaQoswRMjlFhsGNmMs5t38QvEyJpQmEicreHnjTQmXhCZkGZljMcH_cWKFtXYAm3fjNqnjQJorqFnBi4-W-imdvGgBULnNTXCuLwUjknK0xnJDaDVWv5SncNhmHYJwIba3Hx8XoCUx3YhbXyK7QpRx6IG-FUq8WlbIoa5mp8_hS90MsX2XjfGI0cas0vfNf_64BNX2kWv__Qb8y6B-kzc-l2_lhFHDiqUDZWFO9o9mS0CGU_T-bQuK2NOMHZZ5nVNSAbVFtpEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی انس طلا ناگهان ۱۰۰ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145576" target="_blank">📅 16:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145575">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
العربیه:  عباس عراقچی، وزیر امور خارجه ایران، اخیراً با عاصم منیر، فرمانده ارتش پاکستان، گفت‌وگو کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145575" target="_blank">📅 15:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145574">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پنتاگون: ۱۲ سرباز در حملات چند روز گذشته ایران به اردن زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/145574" target="_blank">📅 15:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145573">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: اسپانیا به دلیل مهاجرت، نابود خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145573" target="_blank">📅 15:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145572">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Nw6LXDfO3wQLYtlH3YFKdjdmfxq_PVQMDvc-1gtP6tPPpJfmzv7MgzG3SIP5WQAK5r54UzYr6JgquUu0Tfs9tmKRPVv6xYMWowuD89z3f7F4F4mVWrQDUzDl9kHoWlLDFqSsaYPhoz-w1FnJE5UtEYtq_dkk9kvTL0NIz2pPLBO1xirT_8EJb6UymRNZqFDDwXG5jDA8k0I6i2xWiNj7QsQGiI3fZOvZBQOQkJLnJxAaE2gaKznSD4I5d1K_ieC_Wu_5zZPK1SPt9CsQv412jGgKLHepl5IpnGyFT9sG72hF6zxdJIG9ihd_ozRsCrxBt8ZVK-LLgCKNC6_2NHqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین و لهستان در حال بررسی امکان ارائه یک پیشنهاد مشترک برای میزبانی جام جهانی فوتبال مردان هستند. کی‌یف امیدوار است که این همکاری، تکرار موفقیت این دو کشور در میزبانی مسابقات یورو 2012 باشد، طبق گزارش نشریه POLITICO
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145572" target="_blank">📅 15:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145571">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vySZl7bi5NRLitMjI6VW8vomiveyvL7-d0EcgA5x_JR7DoDhrRbD6bR7jHyALar2IlUSukSv8sWvfX2nDRpubEzWRL6DUbZCHgMoyJJEzK4Z0OzT7disMc3pQe77Uk1OzpYTkrk0aAdbh67isE5kiGPwK2873Is0HlxBM07abM6Fh77-6Pq11Jq3W4NjGFE6m5rmAn9snTcZVMdRbP8CyjK6S8qPGIHg8A54x__Ka5-VGkM9EXzX45btxBMFmi0JlDnUoxFSsuMRz6a7a5Tt5J_Fn9ZPFiMAAojkO4w9OTU5v110-o9JHFnB18INC0Cf93OIbahpfjxauhuxElwFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اد میلیبند، وزیر امور خارجه بریتانیا:
موضع بریتانیا در مورد جزایر فالکلند، قاطع و ثابت است
🔴
این جزایر متعلق به بریتانیا هستند و همچنان به این وضعیت باقی خواهند ماند، زیرا این، نظر غالب ساکنان جزایر است.
🔴
حق تعیین سرنوشت آن‌ها، از اهمیت بالایی برخوردار است و بر اساس قوانین بین‌المللی است، و ما به طور قاطع از آن حمایت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145571" target="_blank">📅 15:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145569">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/17e7eecdbd.mp4?token=ZdrDHo1CqkEM8V2nc4S-OGfW4uLLXqLus0WrMVOLR8JTde6pUoznStvb5Og4mFLLJb9nb4FN18IaBTeEFUWYlFfgxopKzM5TEAwNngdvSq4D5cpqrqEj6U-C-gNfvadHkzVn46YjASjYlssV7xMbcpA4ILZ2esnGflWMdNzXRCfpZwWRPgDbL0DriMEU8F5NxjnNEwTTMjKm4dvyb-e83ssa2qiY9mo8ex3bBdLqCzRp9km8C9Lm1kJAT4dyx1V-4JrSVlPa30ktCGAPwKcZ_jLJgR7XfR5FfdxnkwDFLMdmhot_6fYqP5u4hBXhL93o7B3_puXdYbbnbal6GMSmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/17e7eecdbd.mp4?token=ZdrDHo1CqkEM8V2nc4S-OGfW4uLLXqLus0WrMVOLR8JTde6pUoznStvb5Og4mFLLJb9nb4FN18IaBTeEFUWYlFfgxopKzM5TEAwNngdvSq4D5cpqrqEj6U-C-gNfvadHkzVn46YjASjYlssV7xMbcpA4ILZ2esnGflWMdNzXRCfpZwWRPgDbL0DriMEU8F5NxjnNEwTTMjKm4dvyb-e83ssa2qiY9mo8ex3bBdLqCzRp9km8C9Lm1kJAT4dyx1V-4JrSVlPa30ktCGAPwKcZ_jLJgR7XfR5FfdxnkwDFLMdmhot_6fYqP5u4hBXhL93o7B3_puXdYbbnbal6GMSmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی وحشتناک از خانمی که برای مهریه به دادگاه رفته و توسط شوهرش با ماشین زیر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/145569" target="_blank">📅 15:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145567">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czEWIk9Ysa4GyyHyznU6qcbhTdfCilytdoEFBbUvqOAIKuUGz5iiR9P9Spt0f0GUtOJzxFDb33E0c50hGkCg9vgwIjV1rGMUDYb0oGH4KHLssLX78CK63FZ8UgMReISXZ9Gl5hlAtVxD8M5Z75X0TZFI_HocTFvPsQMRPZRYb1X_HIXKxn-XPcs_34FDUQsu9tXpQP4nAMKpTYBhxpqXpeLm3uvOJ-xnBXO2d27y0acVcXGyhRC5L8jlXkeUZXZyVibJQms60eYjrJ1jlyAuOyN3kMe3KLipg5YYIC9Qa-hFJOO9kUu6eEyANQQDebWPfXmPmlP6rFQikWn4ZdQ92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyPLcWsfW8A4xHaGwYlsVnZAwpjsmd-lfnX9fMW4VBJAD7mzWlg-VgJjwpvDap6_CQG0E2zWyw2yu_uEIlwk0FYrtPZZJ9sIoj5jz-slVDZEWF7FWz6KjRIJSOS8PikyMmRlK7-AhV-KcxDD_SIvsni5BhgNdBgVFqGT-aY7fZBw2Lohr8DWavcfY_DHom_YhgefcwcmYGnxs1XbnrYI8HtGx-3yCw4navGGZ-d8cl0UrfCDFjKYW6jZxG_YJzspIdD4ltxniHmniHUvCBYfWmhWNpt59hi0q05gxRLeXZUCU78gpYUSY-ndugHScHTX0eG8rQ7YZllKOJH5cH61Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هشدار سپاه به کشتی قطری
🔴
دو تانکر حامل مواد شیمیایی و گاز مایع متعلق به قطر، پس از تلاش برای عبور از تنگه هرمز از طریق مسیر جنوبی، به مسیر خود بازگشتند، زیرا از سوی نیروی دریایی وابسته به سپاه پاسداران هشدار دریافت کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/145567" target="_blank">📅 15:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏
👈
تغییر ساعت کاری ادارات و بانک‌ها از یکشنبه ۱۵ شهریور
🔴
‏ ساعت کاری جدید ادارات و بانک‌ها از روز یکشنبه ۱۵ شهریور ۱۴۰۵ اجرایی می‌شود و بخشنامه مربوط به تغییر ساعات کاری نیز در آستانه پایان اعتبار بخشنامه قبلی ابلاغ خواهد شد؛ این تغییرات با هدف مدیریت مصرف انرژی و استفاده بهینه از منابع کشور انجام می‌شود.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145566" target="_blank">📅 15:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145565">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
هشدار وزارت بهداشت : در فضای بسته ماسک بزنید کرونا برگشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145565" target="_blank">📅 15:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145564">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7970c2d53e.mp4?token=HeepMqkmkL1UZRCO305nGEwdLdItSdkzLLvrZsw0ijJb9EnY3vvFLy1ZCbwrG29SjvsslOUNrafzINCIkAofAPNlnGSquQ5CVMjhcATjD7eJCpZS0wlhkadno8TqKCAEERLjPED7LCbK-0s2LKuWav1lon9nhGCLiU_FOzvrT-Te3zE5xXn6livp-G1GgT3Zg3Y9i0yFCirZocchRvB1Y48LnB7BkbEDbpj09OXysNVBWjYSvKqekQn-ZDBDlHDWi1EdPh5UIuUTCJlcaYyP83yoLviEw5rdjnTBIxsJAdQSFkAXC8Y2GBnl3Db0ZNk4JNOCbMJYVWWtzg8YlORJ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7970c2d53e.mp4?token=HeepMqkmkL1UZRCO305nGEwdLdItSdkzLLvrZsw0ijJb9EnY3vvFLy1ZCbwrG29SjvsslOUNrafzINCIkAofAPNlnGSquQ5CVMjhcATjD7eJCpZS0wlhkadno8TqKCAEERLjPED7LCbK-0s2LKuWav1lon9nhGCLiU_FOzvrT-Te3zE5xXn6livp-G1GgT3Zg3Y9i0yFCirZocchRvB1Y48LnB7BkbEDbpj09OXysNVBWjYSvKqekQn-ZDBDlHDWi1EdPh5UIuUTCJlcaYyP83yoLviEw5rdjnTBIxsJAdQSFkAXC8Y2GBnl3Db0ZNk4JNOCbMJYVWWtzg8YlORJ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی جدید از شرایط تورنتو بعد از بارش باران و طوفان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145564" target="_blank">📅 15:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145563">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
روس‌نفت: ذخایر نفت چین و روابط مسکو به پکن کمک کرده‌اند از بحران هرمز در امان بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145563" target="_blank">📅 14:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145562">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
طائب: آمریکا باید سر تعظیم فرو آورد، راهی جز این ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/145562" target="_blank">📅 14:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145561">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9JX29fvEZVCBdLD6sdsqy64Ul0mhFLbJp-yuLVee8V8PJHKj1AWRmtGOn3SdC-VNiZ0p-O7cHRjMlCq8N-T3sGZqu76XM6wF-fB6dCwATXE_m4EUG2g_WdbfTKQ062lqSjHIRSbnGns1boySma6ViL-TCLnUVJIz0WvfPZRgTBgyKdK81w4diZK4OeNJ86zyAKiYFqWKNLVRV9T2MZ-kUIFmliBzW-m1f0Ml8XSP6p6r15VgWriq-f6MKETP1I67XJNQZv_qI-2b03Ad-obfCkqdBntWDpp_f3-VR1fHyLxQtHYlJz0rVTBnORrVil9gOVrNNS3pWBFdtXXD4-6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مردم هر کشور طبق آمار، تو فضای مجازی چطوری میخندن:
🔴
ایران: خخخخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145561" target="_blank">📅 14:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145560">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
معاون هماهنگ‌کننده پدافند هوایی ارتش: از ۹ اسفند ۳۷۰ هواگرد دشمن را زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/145560" target="_blank">📅 14:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145559">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
آسوشیتدپرس: حجم تردد کشتی‌ها در تنگه هرمز همچنان پایین است، در حالی که قیمت سوخت افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145559" target="_blank">📅 14:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145558">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
امام جمعه قم: آمریکا را با شوک‌های بزرگ مواجه خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145558" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145557">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
همتی: به وقتش با قدرت در بازار ارز و دلار مداخله و ورود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145557" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145556">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نشریه  فارن پالیسی: چین از فشار ترامپ بر ایران هراسی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145556" target="_blank">📅 14:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145555">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اتحادیه اروپا: ما با واشنگتن و شرکای خود در گروه ۷ همکاری می‌کنیم تا بر ایران فشار وارد کنیم و به کاهش تنش و ثبات کمک کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145555" target="_blank">📅 14:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145554">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
یک منبع دیپلماتیک به شبکه «الحدث»:
پاکستان، قطر و عمان همچنان به تماس‌ها و رایزنی‌های خود با تهران و واشنگتن برای توقف تنش‌ها و جلوگیری از تشدید درگیری‌ها ادامه می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145554" target="_blank">📅 13:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145553">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
حمید صفت (رپر )برای بازی در نقش «افراسیاب» در پروژه «آرش» جایگزین نوید محمدزاده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145553" target="_blank">📅 13:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145552">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95a10d48b.mp4?token=tatwETdjIkW5J5XLEVO9pdTgFz4NUzZ_39cRCyyhoLVUGLMDxj2MOTfbZBCJw2LYV2E_HzQ-vf5Gz0OszO59l5ByngxABVfA6HYe2K7sY4Pay67FAMCmmRLRbLVdIpODN3f1hJ-EVqRDfLXnfjqztir9r6O9y_4w-FzCu6GczhiiCXcl6pinwfd-4hDTMJYPDVEK2qoze6611iQo60bAtQNd4i1TQtaF7X6h2Noz33F2OHrsHxHsX0C-qWZt7f6vp5sDCgltKBvKxAmpeJ9YP-FKsiuXlNFbV_vAJleUKcOhzoTvtRLETM0NtSId7psNcRS55Z2s03jFyaUpfXg4jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95a10d48b.mp4?token=tatwETdjIkW5J5XLEVO9pdTgFz4NUzZ_39cRCyyhoLVUGLMDxj2MOTfbZBCJw2LYV2E_HzQ-vf5Gz0OszO59l5ByngxABVfA6HYe2K7sY4Pay67FAMCmmRLRbLVdIpODN3f1hJ-EVqRDfLXnfjqztir9r6O9y_4w-FzCu6GczhiiCXcl6pinwfd-4hDTMJYPDVEK2qoze6611iQo60bAtQNd4i1TQtaF7X6h2Noz33F2OHrsHxHsX0C-qWZt7f6vp5sDCgltKBvKxAmpeJ9YP-FKsiuXlNFbV_vAJleUKcOhzoTvtRLETM0NtSId7psNcRS55Z2s03jFyaUpfXg4jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبتهایی برای سال ۹۹ حسن روحانی وایرال شده است وی می گوید: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم
🔴
کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145552" target="_blank">📅 13:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145551">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
البوسعیدی: عمان از تلاش برای توافق درباره تنگه هرمز عقب‌نشینی نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/145551" target="_blank">📅 13:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145550">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
حسن روحانی: باید کاری بکنیم که جنگ، عزتمندانه پایان یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145550" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145549">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
امام جمعه تهران: فشار اقتصادی علیه ایران شکست خواهد خورد، هیچ کس در نظام حق ندارد سخنی بگوید که بوی ضعف بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/145549" target="_blank">📅 13:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145548">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پنتاگون دستوری برای تغییر نام جنگ علیه ایران را صادر کرد
🔴
طبق این دستور از این به بعد نام «عملیات خشم حماسی» به «عملیات برون‌مرزی در منطقه مسئولیت فرماندهی مرکزی آمریکا» تغییر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145548" target="_blank">📅 13:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145547">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
دستیار سیاسی قالیباف: ‏اسراییل قبل از تفاهم‌نامه تا آستانه سقوط علی‌الطاهر رفت، اما با امضای تفاهم‌نامه و فشارِ دیپلماتیک جلوی سقوط علی‌الطاهر گرفته شد
🔴
حال که پنجاه روز است تفاهم‌نامه‌ای نیست، اصحاب ناراه‌حل دوقطبی داخلی را کلید زدند تا فرار به جلو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145547" target="_blank">📅 13:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145546">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بلومبرگ:وزیر دفاع آمریکا، در بحبوحه جنگ با ایران، ارتش را تضعیف می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/145546" target="_blank">📅 13:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145545">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0CWJb-4fZgqio1pVxpLHf_GhrXtMQCTexN4CggORwIJRaOiVH0P_mkbXF7QeYU6fOoovPD3KmgzsebquGYqBe23mDPiltvlzNb6kRSfO5Gjmb9ByqKNHfroQEocINaJST7H7fhbG-WgdsZ-ejEPHo_CV4t3cjK2Vv4mOrexidC_7-IPUJ505IucpKNzUo1wijWfwO74OIDQhs1pP--yOnz2N1bnJ7QriNYT7xiBujBtZrx_vIip5k4eU5kEFgpAnpOqE8Qee_jWsCvAToOWCrITlSkCaxABppLCR4WLhB5ELd6ew3urwK6h6DNmfQL2BxMuUTNn9CGMvv9IYlXY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجتبی ملکی، رئیس فدراسیون بدنسازی: مسعود ذات پرور یه اغتشاشگر بود و نباید ورزشکارها اونو تشویق یا عکسشو تو باشگاه بزارن!
🔴
جوابتون به این شخص کچل چاق چیه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145545" target="_blank">📅 13:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145544">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر نفت:  در زمان رفع محاصره نفت را به آن طرف دریای عمان منتقل کردیم/ در تلاشیم تا محاصره را به طور کامل دور بزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145544" target="_blank">📅 13:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145543">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزیر نفت: بیش از ۵۵۰ اصابت به جزیره خارک داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/145543" target="_blank">📅 12:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145542">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
الجزیره: ایران فهرست سیاه خود را برای کشتی‌ها به بیش از ۵۰ مورد به‌روزرسانی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145542" target="_blank">📅 12:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145541">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تسنیم: تا زمانی که تحریم آمریکا لغو نشود و معافیت نفتی برقرار نشود، تنگه هرمز بازگشایی نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145541" target="_blank">📅 12:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145540">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
حاجی بابایی، نایب رئیس مجلس: در مقابل بمباران اقتصادی آمریکا، باید منافع اقتصادی این کشور در منطقه را هدف قرار دهیم و با اقدامات بازدارنده، محاصره را بشکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145540" target="_blank">📅 12:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145537">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRaqQXVIomTBJkAAfZD_32np1SpT6coXvIXFXOsidtzK7FPvhQNNMG2xa7ihAn9c3e7zIu7A3z63IJ7eiS-Vf5vn77yCpwGw6P2RmrOTYrxJMPCnzab7zeeGHTcjP-Fvh__OzQ_bwy7YS5Ah-d-KWtSm5rfCDfwVj1n_P9nSwBFKYxCq4ydY7btsogTP1i324At-JEpC8DkGJ9mBsy5Yg0iZ3P2Cd7K74G55lJ_tQYgsyz0d4huqAE9-FAszseKsiD9WRHdklJI83wnxh6DtKdfCFzUsT2EZxHSxbbxBl3OaIprFX73VW-FCCrhcbLYcm826VmRzMWA4WKhsjm4uoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eC2NLZZI5IyD11EeIZzvxb8ruE6jooghSXRKaejKS4oyBfX0Eb806R4U6B0qHy9xzV0DwEmw_hWoXaZ3H3yiF4PcJ9soe3dqg6EmJbQrZ4jbBjNDJQGsakfcQJkqeSyt9MTbb3m-LQJayi9qBZuv4o0O4yDS0UQbR09bpByGRPRz17pk58V9a2fmK3G6Oho2mdcxLToZlHIPnS7rCCFRKVj0D_VMusqdOjeglwS9sPmZi5aRzjSXMtnKB8T9A_Y8Por12VHl1TqmV_rCQJdCOrOUbbEqktc14k2vVGL8_TZuvZynY9rd7iKMT5PFua0xEk-IMmO0yjRxWNCaPje8xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48943dcb4.mp4?token=vOuhAkbsUVMrBzLGi6Y-HFHoydabFpzTmPGS3f7M0fHPNabnPRQSeBI99l3IZFx5padULNTRVEBuV0yGj1JfUgPLHjA9-zXzPjiIlkRJVQEHwMhTwePZoh5BrYbx8Vl7BpJZDONr84d_sxHRQznas1XnF1UJNeiMj6WIyyUgf06CP4pn1AmTIaH5TXV-W5nPIQRDO17MYB8Eu02-aAs4-8Co8pyDjZ2U4UCn1UiScjH-sr_IwCiUKaTUwF5mJ-BB0kmGXfzIELP-c2VbID43RlD2p1ENz5uXlUzvQMYxUgBDuuwuU1Tk6R0pedMguoT_U39NC-A2IwJ5MeLP_Y9nqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48943dcb4.mp4?token=vOuhAkbsUVMrBzLGi6Y-HFHoydabFpzTmPGS3f7M0fHPNabnPRQSeBI99l3IZFx5padULNTRVEBuV0yGj1JfUgPLHjA9-zXzPjiIlkRJVQEHwMhTwePZoh5BrYbx8Vl7BpJZDONr84d_sxHRQznas1XnF1UJNeiMj6WIyyUgf06CP4pn1AmTIaH5TXV-W5nPIQRDO17MYB8Eu02-aAs4-8Co8pyDjZ2U4UCn1UiScjH-sr_IwCiUKaTUwF5mJ-BB0kmGXfzIELP-c2VbID43RlD2p1ENz5uXlUzvQMYxUgBDuuwuU1Tk6R0pedMguoT_U39NC-A2IwJ5MeLP_Y9nqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای شرکت ایندی‌گو که از نَوی مومبای عازم سرینگر بود، صبح جمعه هنگام پارک در فرودگاه بین‌المللی سرینگر با تیرک سامانه هدایت پارک هواپیما برخورد کرد.
🔴
پرواز ۶E ۲۲۵ حدود ساعت ۹:۰۲ در حال ورود به جایگاه شماره ۶ بود که با این تیرک تماس پیدا کرد و هواپیما دچار آسیب شد. با این حال، همه مسافران و خدمه سالم ماندند و بدون آسیب از هواپیما خارج شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/145537" target="_blank">📅 12:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145536">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37707ac0d.mp4?token=Sxjv67lVca594k5qozY4ZpkgZkZRsbKOFfrNF-jklH2BbxGA_tKyPQQUN6XBxr0CeJ61cxueeLzNrQQiGAsSv8N2tFkDXShHIoxh9-5671_rwOGoFUa8qOSZV4gx0PXJxVV-2kp7eq7EbljJjhJymHY9w-DO27IKm4WDXj9i2ZCREeUOX0CYGO7kUK7aYLiixLSG8StD81xa_FmuKCiVC2MDxjf936rKoYwUTJAtakj74QgqXUs-26b9uEKyY2yIZ31fYsUhuW4spRK7cXv6kJ1UGxxzrh9sfotShXyAS25HezAQusYMnMA6AIMcts5XNjQZA8T5S_zoOaEf55cekA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37707ac0d.mp4?token=Sxjv67lVca594k5qozY4ZpkgZkZRsbKOFfrNF-jklH2BbxGA_tKyPQQUN6XBxr0CeJ61cxueeLzNrQQiGAsSv8N2tFkDXShHIoxh9-5671_rwOGoFUa8qOSZV4gx0PXJxVV-2kp7eq7EbljJjhJymHY9w-DO27IKm4WDXj9i2ZCREeUOX0CYGO7kUK7aYLiixLSG8StD81xa_FmuKCiVC2MDxjf936rKoYwUTJAtakj74QgqXUs-26b9uEKyY2yIZ31fYsUhuW4spRK7cXv6kJ1UGxxzrh9sfotShXyAS25HezAQusYMnMA6AIMcts5XNjQZA8T5S_zoOaEf55cekA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو ویدیویی با هوش مصنوعی منتشر کرده که در آن شهردار نیویورک، زوران مامدانی، رئیس‌جمهور ترکیه، اردوغان، مجتبی خامنه‌ای از ایران و رئیس‌جمهور فلسطین، محمود عباس، در یک تماس گروهی حضور دارند و درباره اینکه چقدر می‌خواهند نتانیاهو شکست بخورد صحبت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145536" target="_blank">📅 12:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145535">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سخنگوی ارتش: دشمن بازم تو دستیابی به اهداف خودش در حمله به ایران ناکام موند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/145535" target="_blank">📅 12:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145534">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت اخرونوت : اسرائیل درباره ایران آمادگی ویژه‌ای انجام نداده؛ وزیر جنگ اسرائیل با اظهارات خود قصد دارد توجه‌ها را جلب کرده و در صدر اخبار قرار بگیرد. ایران منافع واقعی در وارد کردن اسرائیل به جنگ ندارد و ترامپ نیز نمی‌خواهد اسرائیل وارد درگیری شود. برآورد ارتش اسرائیل این است که ایران قصد عملی برای اقدام ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145534" target="_blank">📅 12:25 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
