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
<img src="https://cdn4.telesco.pe/file/QfyUVsGZYD2g_8CMQiWPdLMqSC8O2KpH-_9xeRy6LrBKZzTlnqtGSHvf17F_bt21dv71hq_l6M1iI8_TDgRD1YxhrbdA6RXbr6pVpl5GzbbDV4MAL-3XBCiBlLS2hzBxKF_7lbFg4cdYQNmq4oxHumy7W78JLwlXYYtSy98Kk23gtm9EazFk-ssCgCRFZu0JaelYyyKPhFBiyimxRcTj6pFh-92wDe6CZjOR3M7hZWE8cMyDQoqI4YQJ7HpIsLk0RmdZeFW3F5vsVarVTAsW1D4CFac06EBTdyo5Rq-aCSo1F9zYRwoWKQrbSbL2yGbLqTbvhrmHlHz48bYLBM0A9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 52.8K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 19:44:47</div>
<hr>

<div class="tg-post" id="msg-2801">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBGlcBE1h-iTAB5g-H38K4HPcu87gyQP-1v4F1ihSG5QG469rR6r2huA8bni4KyIgcFW-Zifi9bq3QCHSswu_mY8083R1K2r69jUQZIEdaTbOqSM1UnAivwd4dbB7sZq-GeDk7S9WZ4uZG5_I2YzRLFSi_fA-719VRVZF6KG-NzAv3M7JxH7RmYx7UYFSDBeo3cmaKGJfxEbs6SQwn1IReqKYMITbhJLBdET1ai78sX7PQ7yokq94LX4uV8Vl2HuBQthzSMK8DvqLFkJXa933i8BR0MWExqJ-hURWYaeyIkGj6YCgPc-7um9ndkXssQ7iYMjVhJs-EeY8dBEETqToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل‌ها برای نمایندگی فروش کانفیگ
👌🏻
🔹
در این ویدیو به معرفی و بررسی ۲ پنل قدرتمند می‌پردازیم که دارای سیستم نمایندگی فروش و قابلیت‌ مالتی اینباند هستند. با استفاده از این پنل‌ها می‌توانید به راحتی برای مدیران خود سطح دسترسی‌های مختلفی به عنوان نماینده تعریف کنید. اگر قصد دارید سیستم فروش خود را گسترش دهید و نمایندگان جدیدی اضافه کنید، این ویدیو دقیقاً برای شماست.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پنل
#نمایندگی
#فروش
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/iaghapour/2801" target="_blank">📅 18:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2800">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSwLqfr_L93Y8dNRy8_Bs_CpTlamm2nybeJQw2gMm34qRMGXM55YtGSvvhqsMq3ETZPBNEwPbkDCaGOF1fzx2QPGVoXupUIPxlXbfm2_mfk3WZA9DCuV-0ClJ37yatNuc-6I474IWnKux8UFIQNxNKYu4-zjZ6y6eLAmeHzYykpX-b2SMmwjy3kfYLB33hq1IyHiaYeY3Osu4u_ZgH3ww1j_D-mFYA6WgXwshVIfzEGMc3QN3ikG-Dn6GOhbneP4gm1ENFAG9n9cRW1oeLFkOVzlPV5JmjpC8CMiCHo3-_fn1atUGywpR_amRm-Vs3Rd2W47jTPmKl7kYwez9eDRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت نسخه 1.0.3 نرم‌افزار UAC SNI Spoofer Windows منتشر شد!
✨
نسخه جدید این ابزار با قابلیت‌ها و بهینه‌سازی‌های جدیدی همراه شده که در زیر میتونید برخی از این ویژگی ها رو مشاهده کنید.
🌐
انتخاب کشور:
امکان انتخاب کشور دلخواه برای متصل شدن به موقعیت مکانی موردنظر.
⚡️
بهبود سرعت:
افزایش سرعت بارگذاری صفحات و برقراری سریع‌تر اتصال.
🔌
کنترل پروکسی ویندوز:
اضافه شدن گزینه فعال یا غیرفعال کردن پروکسی سیستم.
🎨
رابط کاربری بهینه‌شده:
جمع‌وجورتر شدن منوی خانه برای دسترسی راحت‌تر و یک‌جای تمامی گزینه‌ها.
🔗
لینک دریافت نسخه 1.0.3 از گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/iaghapour/2800" target="_blank">📅 17:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2799">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPremstore</strong></div>
<div class="tg-text">🛍
خرید اشتراک gemini pro تنها با 299 هزار تومان در پریم استور.
☄️
آماده امتحانات باشید
❔
چرا پریم استور؟
🕖
تحویل سریع (زیر ۲۴ ساعت)
🔒
بدون نیاز به اطلاعات و لاگین حساب شما
ضمانت کامل 30 روز
علاوه بر جمنای، اشتراک سرویس‌های زیر هم برای خرید موجود است:
(Claude • Chatgpt plus, go  • Grok • Perplexity • Cursor • Leonardo • Gemini ultra •.....)
🛒
شروع خرید از طریق ربات :
🤖
@prem_store_bot
🌐
وب سایت
|
💡
کانال تلگرام
|
💬
ارتباط با پشتیبانی</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/iaghapour/2799" target="_blank">📅 20:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2798">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1uoowlGAUrbdI_e3FoxI4ub35sut7RZLzfGJg1BMfTAgL2h5HlX6CMDduzJjK29qfx5T-d4_I58q7QSagM_zRxzPaVJ5Jw0A7fV5a0s7x2JpNcJM9F2ibtdp-M2wb1LIUwqC4ochg9Dgl1mmmmXycGl9XCbo-a2pFro4Ht3_qaSOZodxjSN9MgpG26YmZzAyVWtg-nTHnI98rAnnQxzk1rcTjcuk7-OiPQdCIM7g3OV4Z5MpIBqfPxmAogAFfVcuN8sYazQVQdZak7XT-yA0ri9Ghotb6QusBJ_hJaR05pyL-W6byP09X0fRkyW3HSwvsKjAyhfAy5QyorjSfXmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی SIMORGH VPN؛ کلاینت چند‌موتوره اندروید برای شبکه‌های محدود
برنامه
SIMORGH VPN
یک کلاینت قدرتمند برای اندروید است که اختصاصی برای اتصال در شرایط اینترنت ملی، محدودیت‌های شدید و اختلالات بین‌المللی طراحی شده است.
⚡️
نکات و قابلیت‌های مهم:
🛰
حالت MSP:
اتصال ویژه در شرایط اینترنت ملی و اختلالات شدید شبکه.
🧩
فرگمنت (Fragment) پیشرفته:
قابلیت تنظیم پارامترهای فرگمنت برای عبور از فیلترینگ و بازیابی آی‌پی‌های کلودفلر.
🟣
پشتیبانی از NipoVPN و MasterDNS:
امکان وارد کردن لینک‌های
nipovpn://
و مدیریت کامل مسیرهای DNS.
🛡
سیستم هوشمند:
استثنا کردن خود برنامه از تونل VPN (برای جلوگیری از لوپ) و پشتیبانی از پروکسی‌های محلی SOCKS5/HTTP.
🔗
لینک پروژه در گیت‌هاب
🔍
لینک اسکنر پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/iaghapour/2798" target="_blank">📅 20:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2796">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXCD-rNzUW6cdBCZAVSnDt-RiEe3r8uByFUw1qHiEWuXWdR9X_k4Wm4KWJsNFychHb5AR0PCVZBUA8TsO2fAKdb9rKXAX0V3Usmy3TZqMS8FXzjqB68T3cKLe_IOmujxee1oObupnYiVuVgxynf1LilpkB0MQCCINiMjU6fOZRqLKjBiQxf686A0sfuEXrrAJwwgpp-mf1YMkYS7qHPlZ7bnwQYFXIgkZjMOb_dlNsemWNapnYs4_QZn1IsgU48G5v2p2De56atXd8JmKpwCNOgIIvwMQXyq5SEtNtj_GdUAIyC19SwHkmS7dwBcbmTYYyT0TGwoTzLYr5YA1ydjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رخداد امنیتی در Hugging Face: سرقت دیتابیس و کلیدهای دسترسی
پلتفرم
Hugging Face
(بزرگ‌ترین میزبان مدل‌ها و دیتاست‌های هوش مصنوعی) وقوع یک رخنه‌ی امنیتی گسترده را تأیید کرد.
در این حمله، مهاجمان با بارگذاری یک دیتاست مخرب و سوءاستفاده از یک آسیب‌پذیری، موفق به اجرای کد روی سرورها، ارتقای سطح دسترسی و سرقت دیتابیس‌های داخلی و کلیدهای دسترسی شدند.
⚙️
جزئیات و اقدامات انجام‌شده:
🔐
ابطال کلیدها:
هاگینگ فیس تمامی کلیدهای دسترسی افشاشده را باطل کرده و از کاربران خواسته سریعاً کلیدهای امنیتی خود را بازنشانی کنند.
🤖
تحلیل با مدل بومی:
برای بررسی لاگ‌های حساس سرور، از مدل زبانی بومی استفاده شده تا نیازی به ارسال اطلاعات به سرورهای خارجی نباشد.
⚖️
پیگیری قانونی:
موضوع به نهادهای مجری قانون و تیم‌های جرم‌شناسی سایبری برای بررسی دقیق‌تر ارجاع داده شده است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/iaghapour/2796" target="_blank">📅 18:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2795">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCube SUPPORT</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxT7G4o8YGARxjoKkO0LMZil9c1XLoQlyvoeYwcRVpv0ys-rjNmQn-wTWVhOnjdSujAdCYNbTWKxo7DlMOxt_kKBabwfR-ujNOs8okAsSHtnOpqbPnK3VCTWjq1R--YG_VYLy3SCrv5oDyS137rf2WNymnT5iobLNJo-4-obpg82MN-KygYWtwzyUXLZVSjNol2DLrLsWXx4Qkwh_xMdn2PAcIzRI5NsMCeBX5HKHNBZevN88w4EknT_hX9xGvWcK8iPpgs6ueWM5Ce2puxnXjCrp_xVXvZoCIp_I0SCbZdZE8udwHLlgfdXJ2nG-79qLZVyREDHMQPk5TsOBtrsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
CubePay
درگاه تأیید خودکار کارت‌به‌کارت
✅
بدون نیاز به اینماد و کد مالیاتی
✅
واریز مستقیم به کارت خودتان، بدون واسطه
✅
تأیید هوشمند پرداخت از پیامک بانکی در چند ثانیه
✅
اتصال کامل به سایت، ربات تلگرام و اپلیکیشن با API ساده
✅
پشتیبانی از تمام بانک‌های ایران
🏧
🏧
🏧
🏧
🏧
🏧
🏧
🏧
🏧
قابلیت‌های جدید:
🔄
چرخش چندکارتی
🎁
بونوس پلکانی کیف پول تا ۲۰٪
📎
سیستم زیرمجموعه‌گیری
🖥
ساخت فاکتور پرداخت بدون کدنویسی
✉️
خروجی اکسل تراکنش‌ها
🏦
نمایش شماره شبا
📌
مناسب فروشگاه‌ها، ربات‌های تلگرام، فروش VPN و هر کسب‌وکاری که پرداخت کارت‌به‌کارت دارد.
🔖
مستندات:
https://github.com/cubepy/cubepay-doc
💥
ربات:
@cubepy_bot
👨‍💻
پشتیبانی:
@cube_sup
🌐
سایت:
https://cubevps.ir
〰️
CubePay | پرداخت هوشمند، سریع و بدون دردسر.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2795" target="_blank">📅 21:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2794">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXcZeQK_EaC-jf_m4kAt3jpIgpZ5S8SRZus7EKey-AFAbDJITbZ8_yo5HGCnNTYp4SlgNiEeGSrlwjODd3QZPt5MuLeF8LxeaZASHfvWbm6vXgmptNs5C0E8SjHPlciGWig54yv-bS6wYCMpzvNJNRt8oPGWvxXDsbG8DQLZs8IcYoGKgZC9Wr0iJ4YWsYJkJbvVkP016jcLC0_gdhaypNQ9qZC3MfJ75DBnixN1_UxcMG-DVCC4PUx4oVDOVc8Dos_IQ053bbDJkskSREJx6KH3-IzKrwziGNc3U-naP9ok737YXCBpSLFjOXroSRukx7uNNLAkFBgdhaeD0HRYbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت جدید پروژه iran-dev-tools؛ ابزارهای جدید برای رفع تحریم
پروژه اوپن‌سورس
iran-dev-tools
که مجموعه‌ای از اسکریپت‌های هوشمند برای حل مشکلات روزمره برنامه‌نویس‌ها توی شبکه ایرانه، آپدیت شد. برعکس لیست‌های ثابت میرور، این اسکریپت‌ها سیستم‌عامل شما رو تشخیص میدن، گزینه‌ها رو بنچمارک و تست می‌کنن و بهترین تنظیمات رو اعمال می‌کنه.
توی آپدیت اخیر، ۳ ابزار جدید به این مجموعه اضافه شده:
👇🏻
🤖
اسکریپت android-fix:
تنظیم و بازگردانی هوشمند میرورهای
Gradle
،
Maven
و
Flutter
برای ویندوز و لینوکس (حل مشکلات برطرف‌نشدنی توسعه‌دهنده‌های اندروید).
🔄
اسکریپت proxy-switch:
تست و تنظیم مجزای پروکسی برای تک‌تک ابزارهای روزمره توسعه‌دهندگان روی ویندوز و لینوکس.
📦
اسکریپت pkg-pack:
باندل کردن پکیج‌های APT، ایمیج‌های داکر یا حتی خود Docker Engine روی سیستم آنلاین و نصب کاملاً آفلاین روی سیستم‌های بدون اینترنت یا دارای دسترسی محدود.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/2794" target="_blank">📅 20:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2793">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOowxCRufvgAUCv_gpTICbm3vvwnDtxJWB50ym2FUD-aZFlL7nkS_fq7kqlLkk8zk6mfM2LyT57yFCLIf-h-LG5zwyruejiqqNIKE2Dhaq5GTPXCw2cHQgZirS6l0HCszj2bkBzHNZz9w5c65UcAOQvfU3yydu-ygCWqGDnUl6_A9LFfMfB0k0L6KFEGsc6v-XdBrQqRmM9wN2m3H_urRVtP-0tNFVKcYNDycpLIiAUO8EzR9qPCACgl0svznYS4XWyatiK0TT-Yb07KlYazCDLw6WENdA0PWg0yHt7n0WKuIABn4dTlyQciohcY4AXBnDePw4Tu6xTaTGa-PUiVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش استفاده از TOR در سرور ایران یا خارج (دسترسی به لوکیشن های مختلف در X-UI)
ما حدودا 2 سال پیش همچین ویدیویی رو ساختیم و پروژه ای که توش آموزش دادیم حذف شده به اسم torsina و البته پروژه های مختلفی بعدش ساخته شدن مشابه این پروژه که یکی از اونها رو زیر معرفی کردم.
🔗
آموزش ویدیو این روش
👈🏻
اسکریپت Tor automate
(مشابه پروژه torsina)
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2793" target="_blank">📅 18:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2792">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG5Yh-OZ09aucA5S0rufPhXp910lHi7v_EHScV37G968qO4rmNeJJyFiwBgISwi1Lrl9vt7xCvXuVUo1EulG9bDBXoqXtKi4o9C6CF0AcbRngF8hmd90b8HX4UGph6Tuv2sj1zSq-sRKODCadCuZFl9IWyh4U72Z3LiKfl0p6MLAbfpg3zWfr2lkbnaUbgRDX0oXh4xVxRmKA2qQkzfA5AJdOS7QgoQObcV8rEsr4Zsos35cIGSaL93KWa5zZzcdziVAqKuCa89Y440AFdqV8-pzisuDrALrMnC9nbLKc2k4bS-WOLg3spbC_U9_pVNmcsRC_zCCT0XKgMCK9ppU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح...</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2792" target="_blank">📅 16:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2790">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgV30Q7cR_78OkHR3FZgkglmaiRfylh97BPjSCh9n19_xbWHgnW9dq_3OZkctDGNotlFRsyyDIi1_qSagi6NCj0pQ4BCsfApW5UGjlDEtGNc8qbzNPuqNFyIGeYFKKKZ_jKg2ximSYfg-Ww0RXf6KAAKKIo_zqrURkOUCgoyVCX32WWrm_FPP-kFiBtp_2rRYWcS0jIwFRyjZizRUxGoa32JiF2mfwtU-5fDypgX_chmUtVGKGwG5w5hEtgvmpKzC6feVBXgOqE3NzSjBYQ3Hshim175-oWj5cScEPhNZWsR6QpN0VdCO44m2WXt0GIzGhc0fiaUYTGjp4_G9XfoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت کد ۲ مرحله‌ای بدون نیاز به اپلیکیشن با پروژه 2FA
اگه دنبال یه جایگزین شخصی واسه اپلیکیشن‌های Authenticator هستید، این پروژه اوپن‌سورس که روی ورکر کلودفلر (Cloudflare Workers) اجرا میشه فوق‌العاده‌ست. این ابزار بدون نیاز به سرور یا دیتابیس، کدهای ۶ رقمی TOTP رو با امنیت بالا مستقیماً داخل مرورگر جنریت می‌کنه.
⚙️
ویژگی‌های کلیدی:
⚡️
سرورلس و سریع:
دپلوی چند ثانیه‌ای روی شبکه جهانی کلودفلر بدون نیاز به VPS.
🔒
بدون ذخیره داده:
ساختار مستقل بدون نیاز به دیتابیس برای امنیت بیشتر.
⏱️
استاندارد و هوشمند:
تولید کدهای امن با آپدیت خودکار هر ۳۰ ثانیه یک‌بار.
💬
پ.ن:
با اینکه پروژه کاملاً اوپن‌سورس و امن هست، پیشنهاد می‌کنم برای اطمینان کامل خودتون، کدهای سورس رو بدید هوش مصنوعی تا براتون بررسی و آنالیز کنه.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2790" target="_blank">📅 21:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2789">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029b77ae2.mp4?token=j9aHKA38BSZXATb2aQbSm-DtX1x5FdaTddueKuomLyTgNH0BcUS0PQrNdcNScmK2U4nchJ8Dvs7RXBeYh39kdIjLmLfwYsaNrOXD7t-YwlqzDpdSBXwhnPb-NpvJl8B3zVMVk91ZR5V8YWFsHpLtokyPZTH9dggsdcpiZFP_fu_JfsEP7hKCfmoKvZdqJmAMJboUrBgCBuVYYdFkFKKDVh9J5HEB1N6CPdWeWC--FNQQMnWm9UoRIpOhVs7lkl-M8uPM8KwGw-GXPCt21Udu4Soe2bTqOmDr5_Gft0-0BiEk6SeDMo6mRiVB2-5Lsa_y1xsbRWg47xLIRsui08ziAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029b77ae2.mp4?token=j9aHKA38BSZXATb2aQbSm-DtX1x5FdaTddueKuomLyTgNH0BcUS0PQrNdcNScmK2U4nchJ8Dvs7RXBeYh39kdIjLmLfwYsaNrOXD7t-YwlqzDpdSBXwhnPb-NpvJl8B3zVMVk91ZR5V8YWFsHpLtokyPZTH9dggsdcpiZFP_fu_JfsEP7hKCfmoKvZdqJmAMJboUrBgCBuVYYdFkFKKDVh9J5HEB1N6CPdWeWC--FNQQMnWm9UoRIpOhVs7lkl-M8uPM8KwGw-GXPCt21Udu4Soe2bTqOmDr5_Gft0-0BiEk6SeDMo6mRiVB2-5Lsa_y1xsbRWg47xLIRsui08ziAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی!
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده یک اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
آقای حمزه حوتی عزیز، مبارکتون باشه!
✨
آقا حمزه لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
اصلاً فکرش رو نمی‌کردیم این‌قدر حمایت کنید. حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2789" target="_blank">📅 20:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2788">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fe7rJOeegSyOqjuohFObyckJ7iWm9EAVor44svk44TABONTBxud7cDk46jMS-rNZ5IzL9VQ1s3uBXQ4Z7W_q8KfDTKZ8yhg-pqfIIYDp7U_OZCRTG8jXGxKlK8RCKlCJtBda7qO8RXKxMPbMp07HMtaGXqAK27gnq1KuLRRedZLqYiO-K5fv_iyrQz_4wq3J2HxjUkuOd0S1dXK7fqpDAPo4nUAlWx1M3H5WOkvK2GrSQUd-HDqJhzA28kesA1M5LwVQ-XKt95oy2-JV3_gSgMjM8inMUabZf9Rig_Y33jMMa_HQSGi2YaN1HkjrmOv5002kmwZvpkd4RlXT3lEg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
حل مشکل تایپ اشتباهی با کیبورد فارسی و انگلیسی در ویندوز!
مطمئناً واسه شما هم پیش اومده که کلی متن رو تایپ کردید و بعدش تازه متوجه شدید کیبورد روی زبان اشتباه بوده و کل متنتون به زبان عجیب و غریب یا برعکس چاپ شده! نرم‌افزار رایگان و سبک
LangOver
دقیقاً واسه حل همین روی اعصاب‌ترین مشکل ساخته شده.
کافیه متن اشتباه تایپ شده رو انتخاب کنید و با کلیدهای میانبر زیر، تو کسری از ثانیه درستش کنید:
👇🏻
🔄
کلید F10 (تغییر زبان):
اگه حواست نبوده و فارسی رو انگلیسی تایپ کردی (یا برعکس)، متن رو انتخاب کن و F10 رو بزن تا سریع درست بشه.
⬅️
کلید F6 (برعکس کردن متن):
کل متن یا کلمات رو به‌صورت برعکس چیدمان می‌کنه که واسه کارای خاص یا رفع به‌هم‌ریختگی متن‌ها خیلی به کار میاد.
🌐
کلید Ctrl + T (ترجمه سریع):
متن رو انتخاب کن و با زدن این میانبر، مستقیم اون رو از طریق مترجم گوگل به زبان دلخواهت ترجمه کن.
و چند قابلیت دیگه همه به صورت رایگان.
🔗
لینک سایت و دریافت برنامه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2788" target="_blank">📅 20:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2786">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستان این همون آموزش هست که زیاد درخواست میکردین.
👇🏻
🔹
آی‌پی خارج فیلتر باشه مهم نیست.
🔸
سرور ایران تا حدود زیادی ضد اکسس شده.
🔹
تانل ریورس هست با کمترین اختلال.
🔸
سرعت بسیار بالایی داره.
🔹
مصرف منابع کمه و چندین سرور رو میتونید تانل کنید با هم.
همه این موارد در
آموزش بالا
قابل پیاده سازی هستش.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2786" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2785">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RatholeEngine Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">356 B</div>
</div>
<a href="https://t.me/iaghapour/2785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
تانل ریورس روی سرور با آی‌پی مسدود
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/iaghapour/2785" target="_blank">📅 19:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2784">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtgVltAdwzKov7X6UiRBeKgV16dYjBgFv4pDTIuKuFGBIyUeRFHsQEDiNGQFn7CH9oZ79GrWFfrX7shdzjwIR55utZC3iEyenTW8WwhCw9TwHsHo14v5vqSu-0DchQIvRYQR7Wen2ohgeTzszaiIMXVR3YRkvHBEC_qxaV24HXFaNwR58-Bcbnf1nThsgvhfEkUgEcwpMBPBFTZrxBW2n1GKQipLGyezy5GzjPMQD0rYAMFKGKewlAoGamvSFY1Kn7tT5O-jTa9eaZRgKgQzbahoSBY_qGQmeh3CduEgIXZbju9r2EE07eQzOqYAg1JsndtAQClKIPXm1GLzYLxXlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل ریورس روی سرور با آی‌پی مسدود (مقاوم در برابر اکسس)
🔹
حتماً براتون پیش اومده که آی‌پی سرور خارجتون فیلتر بشه، یا سرور ایرانتون خیلی زود اکسس بشه، یا اینکه بخواید چندین سرور رو به صورت همزمان با هم تانل کنید. حالا با استفاده از تکنیک تانل ریورس می‌تونید تمام این کارها رو به راحتی و با کمترین میزان مصرف منابع سرور انجام بدید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#ریورس
#اکسس
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/iaghapour/2784" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2783">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
تعداد 116 دکل مخابراتی هرمزگان از مدار خارج شد
🔹
اداره‌کل ارتباطات هرمزگان: در حملهٔ دیشب آمریکا به‌خطوط انتقال ترافیک و پهنای باند در بندرعباس و حاجی‌آباد، ۱۱۶ دکل مخابراتی از مدار خارج شد.
🔸
درحال‌حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که تلاش برای وصل‌کردن آنها در جریان است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/iaghapour/2783" target="_blank">📅 15:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2782">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚠️
دیتاسنتر ها دوباره اختلال خوردن متاسفانه.
حالا معلوم نیست برای یک سری دیتاسنتر محدود این اتفاق افتاده یا برای همه دیتاسنتر ها.
ولی طبق تست ما آپدیت پکیج ها و گرفتن سرتیفیکیت و کار با داکر دچار مشکل شده.
🔻
در حد توان آمادگی داشته باشید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/iaghapour/2782" target="_blank">📅 13:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2780">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6Qmf49sk-bk_RkUBnF6R4gDKK8e56Z9_XEOjVsYGdtOG0rO65u0_0Dy-fviiGYBlndPpmRzYolN2ciaItvcYQTG-LxTzRS-SXA8wjdWwOQFojkSebdQ8RgZrR4cdrKl2-J-cPwUrbqEUi6HorL5LzwlBn_BJPTbUVz0S4AROEVlt1zK-_IvJcOgeA9pDOcfwqQY4o0Kcnpw03OxgFne-lxCdfrOwBbTEud5KO_k0dgKJyaq6_A2qqfExkI9RyVVBndO5N077YtaHJf9haP0hafR8vhFAQdAmp9V6ofsCy7TRllNP05Q8q-117hHYUA_2Be8HWHZf47717ly2Cv-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
قرعه‌کشی ویژه اعضای کانال!
رفقا، برای قدردانی از همراهی شما یه قرعه‌کشی جذاب داریم!
🎁
👇
شرایط شرکت:
کافیه فقط زیر
آخرین ویدیوی کانال
یه کامنت بذارید.
🏆
جایزه:
اکانت هوش مصنوعی 1 ماهه (Gemini یا ChatGPT به انتخاب ما) برای برنده عزیز!
⏳
زمان قرعه‌کشی:
همین فردا! پس تا فرصت هست کامنتتون رو ثبت کنید.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/iaghapour/2780" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
آمریکا با تحریم‌های جدیدش، صدور گواهی امنیتی (SSL) واسه سایت خبرگزاری فارس رو مسدود کرده. این کار باعث شده دسترسی کاربرا به سایت مختل بشه و اخبارشون هم کم‌کم داره از نتایج گوگل حذف می‌شه.
پ.ن: من می‌ترسم فردا روز اینا واسه جبران بیان سایتای ارائه‌دهنده گواهی مثل Let's Encrypt و اینجور چیزا رو تحریم کنن و کلاً همه رو به فنا بدن!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/iaghapour/2779" target="_blank">📅 16:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2777">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p29dFWeSYGFt5efQSqD2JWDrbOYk5Yg-bMfkenAuCAMEKKpQCHaPwNdqLQOCm_S98X565lG5Ew2PGubecwS2BO3UPxwn_wMMRhaXXLqVbl8rER25k5uGLOQJImoUqPqBD302WPxuanDuyRsdz2aPbJDV5rt3yuwRME9ybWxVI3gFFKDKD-6N5lB27watMbf_1A_x3K29g9Jgg_0IS-AefRzh6p-ahpHCYtsdtT9MA7LVSLQTMsCd13yUv7EUEDJlPqb390fqyRoTaixDec6YQ37hpkfLyDMxBeW-C_PVFJPzmKYo2-4r-DmzibdCwB-JO_zhXkdoKGZSl0GYB0n_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره یه روز لو میره که مسی اصلاً آدمیزاد نیست!
یه فضاییه که اومده زمین تا کلاس درس فوتبال برامون بذاره و برگرده سیاره خودش :)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2777" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2776">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🟢
بچه‌ها، یه سری از دوستان پیام می‌دن و می‌گن «سرور خارج گرفتیم ولی پینگ نمی‌ده و نمی‌تونیم بهش SSH بزنیم، پس خرابه یا به کارمون نمیاد.
یه نکته‌ی رو یادتون باشه: اگه قصدتون تانل زدنه، در بسیاری از موارد مهم نیست که بتونید بهش SSH بزنید!
مهم‌ترین چیز اینه که
سرور ایران شما
بتونه سرور خارج رو ببینه، بهش دسترسی داشته باشه و پینگش رو بگیره.
👌
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/iaghapour/2776" target="_blank">📅 20:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2775">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دیگه واسه چی غصه بخوریم؟ از اینکه حتی نمی‌شه یه آینده‌ی خوب رو تو ذهنمون تصور کنیم؟ از اینکه هر روز باید با قطعی برق سر و کله بزنیم؟ از اینکه وسط جنگیم؟ یا از اینکه تهش قراره آرزوهامون رو با خودمون به گور ببریم؟
🖤
خدایی دیگه چه انرژی و انگیزه‌ای واسه آدم می‌مونه؟ اصلاً نمی‌خوام نق بزنم یا فاز ناامیدی بدم، ولی واقعاً یه جاهایی آدم کم میاره و رسماً می‌بره... کشته شدن این سربازهای بی‌گناه هم که دیگه مثل یه تیر وسط قلب همه‌مون بود. آخه چرا باید پژو پارس بشه آرزو؟ چرا باید یه ۲۰۷ مشکی بشه سقف رویای یه جوون ایرانی؟
😔
خدایا... فقط بزرگیتو شکر.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/iaghapour/2775" target="_blank">📅 19:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2773">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIpkUw9RgAHzSvZsrhW5g-4n-BscZQ5s6u7yOUZOtbZ7fswpNNzPc_fABmL7S61w54vUCTMPhNeNE-RtfKjfhqbANBpVq24ugFgRbsP_gYijOHVTHq3DO4xXPync7gZ8eXw36tHKw-zqv5u9dX6aQC6SxH4zD2ri1Wwbk65A2qWX0mTkanYQBbZPsrbIjv3JpheeLK15Jj-cq8CQMv4lNQrDXqy7v6USiKugiLfC24chWnhBJgwgKTuqZU6N7WQCFA3Fum4eGyPgAvVL1JaweEE0R9kZOO2wIwb3JHNajGOCa7GhSoDy02JY4eoirUnJVruUCRyKAbUMWOx7ETFS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دور زدن رایگان فیلترینگ در ویندوز
با
UAC SNI Spoofer
🔹
اگه دنبال یه ابزار بی‌دردسر و قوی واسه ویندوز هستید، این برنامه که با هسته Xray و متد SNI Spoofing کار می‌کنه یه گزینه فوق‌العاده‌ست. این ابزار با مدیریت هوشمند مسیرها، بهترین و پایدارترین اتصال رو براتون ردیف می‌کنه.
⚙️
قابلیت‌های کلیدی برنامه:
📱
دارای حالت‌های اختصاصی همراه اول، ایرانسل و حالت هوشمند Auto.
🔍
تست و رتبه‌بندی خودکار SNIها و Edgeها برای پیدا کردن سریع‌ترین مسیر ارتباطی.
🚀
مجهز به سیستم شروع سریع TLS برای همراه اول و قابلیت «گرم‌سازی مسیر یوتیوب» برای پخش بدون بافر ویدیوها.
🔒
تنظیم خودکار پروکسی سیستم
🌐
با قابلیت App Bypass (عبور برنامه‌های دلخواه از پروکسی) و نمایش لاگ زنده.
🔻
برای کارهای حساس استفاده نکنید.
🔗
دانلود از گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/iaghapour/2773" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2772">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt1IvNF0492KjvF0eLVxT5ux8xc5FcU1gucYUihGkAPaeG01Z5FHp6_AsFvX6Z6algl15shgBIw2SRPkpjOY9TsUS8TEGSk75Bfb_MUM_tV_H6evy5b6HKmP-lITBPKX48tyely69VZXUI0sTlLg9OGZgMeVzl9pxcPcfjAJYw4sLe0s0Tn18jeqMI18Wdq9UjdFSVUBReiAkRFAHhHXA6l_SIf4PvfgZ2nuy3elygv8HIJ3NYo0osz94xzi-4H42IZHUsS5TyutS5a_CH_k0DBm2QM0OvgIkKklOAH5qoCRS5VyV0qgaumxqRopaUrVy-bTgD5SEhkxMfY5nnV_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
انتقال بی‌دردسر پنل 3x-ui بین سرورها با پروژه 3xui-mover
اگه تا حالا مجبور شدید پنل 3x-ui رو به یه سرور جدید منتقل کنید، حتماً می‌دونید که روش‌های سنتی (مثل کپی کردن پوشه‌های x-ui و cert) همیشه جواب نمیده؛ مخصوصاً اگه دیتابیس شما روی حالت PostgreSQL باشه، پنل تو سرور جدید بالا میاد ولی کاملاً خالیه!
⚙️
ویژگی‌های اصلی این ابزار:
🔸
پشتیبانی PostgreSQL و SQLite
🔹
بکاپ دیتابیس، تنظیمات و SSL
🔹
انتقال خودکار با SSH
✅
جلوگیری از ریستور اشتباه
🔸
بررسی صحت انتقال و لاگ کامل
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/iaghapour/2772" target="_blank">📅 20:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2771">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u12TSlBkwE1DxfM4Kb8JeNmsAA_Ig8ysmdjpyAAIH8jQBIVCsOqPIwz3VuETcagNKTUY1i7D6mZNqcja_Xfx0w_iyz8oUxCjRTNFlIhxgrlnpd-WGRdss8gRt-ud_-qlKce5jZ0bas3GtwY5aTG2CmUXI3fnWjUmyUSQ4J-dJRA4HzAfDNCF_GBBPTehuKbDX7fFUxoAkgOz8nvYe6pxG5Qhp5wEsNLC31qgT0YUu80mj-nnmwsSwGTSrt8t04X47j4_DJGv_OuxE1p0VbXjBONn9Hx6J0hl4kQGRo3gtNhX7vmvYYDHDadMq6pW2d7pxKgdJBpwJhYpl3iXSGC1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
توجه! مراقب کلاهبرداریِ فروش پنل‌های رایگان باشید
دوستان عزیز، با توجه به پیام‌ها و درخواست‌های متعددی که از سمت شما دریافت کردم وظیفه خودم دونستم که یک اطلاع‌رسانی مهم در مورد سوءاستفاده‌های اخیر داشته باشم.
متاسفانه اخیراً دیده شده که عده‌ای افراد سودجو، پروژه‌های کاملاً رایگانِ دور زدن فیلترینگ که بر پایه ورکر کلودفلر ساخته شده‌ را به عنوان سرویس‌های پولی و اختصاصی به کاربران می‌فروشند!
ابزارها و پروژه‌هایی مثل:
👇🏻
پنل BPB
پنل نهان
پنل نوا و...
🔹
تمامی این روش‌ها توسط توسعه‌دهندگان به صورت
رایگان و متن‌باز
منتشر شده‌ تا همه بتوانند به سادگی به اینترنت آزاد دسترسی داشته باشند. فروش این پنل‌های رایگان نه تنها یک کار کاملاً غیراخلاقی است، بلکه سوءاستفاده مستقیم از عدم آگاهی کاربران و بی‌احترامی به زحمات سازندگان این پروژه‌هاست.
✍🏻
هدف ما از انتشار آموزش‌ها در این کانال دقیقاً همین است که یاد بگیرید خودتان به سادگی و به صورت کاملاً رایگان این ابزارها را راه‌اندازی کنید. هیچ دلیلی وجود نداره که بابت یک کد رایگانِ کلودفلر به کسی هزینه پرداخت کنید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/iaghapour/2771" target="_blank">📅 15:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2Ew8u-9Py5hjI3k1jHQ6PykvZSTeVu79Ri_DF59FxS9dBD6FboBNlCZeS5rwFtaCdy7ZMQvdZ2oPpTS2kqNb81JwNMy1T-hA_6LALLGtFxeNzaSkX2fulX1IQVGt7iuch1ULyxK21J0H0E82_Fxi2PYFVoKR3XYTAW3yU28ZCAVDKCnBuMIsiC7X7E_UvDPx864DKZTjcmeddgMSNGFLMe-mG8rYBBYRaDRDgFC5MLM2_8hEh6OBphXJVQVQjiCUaPu_D1SAqMg38YbwLoZQN27P9yJJG3La1CFlHPF-xbUDF_wxsmi0TLIYmGepL83e0gZKQSRbs3BO2Xj-Q5dLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازگشت بانک ملی به مدار اصلی؛ صادرات و تجارت هم به‌زودی
بانک ملی از امروز بالاخره به زیرساخت اصلی برگشت و سرویس‌هاش پایدار شد. بانک‌های صادرات و تجارت هم قرارِ ظرف چند روز آینده به این بستر اصلی منتقل بشن تا مشکل قطعی‌شون کلاً حل بشه.
این اختلالات طولانی‌مدت که از اواخر خرداد شروع شده بود، به خاطر حملات سایبری سنگین و پیچیده بود که تو این مدت با کُر پشتیبان مدیریت می‌شد. در ضمن بانک مرکزی اعلام کرده چک‌هایی که تو این مدت فقط به خاطر این خرابی‌های فنی پاس نشدن، هیچ تاثیر منفی روی رتبه اعتباری مشتری‌ها نمی‌ذارن.
💬
پ.ن:
البته با وجود این خبرها، هنوز یه سری از کاربرها میگن بعضی تراکنش‌ها مشکل داره. از اون طرف هم انگار کلاً بخش وام رو بستن؛ یعنی مردم این‌همه سپرده گذاشتن به امید وام، ولی حالا که می‌خوان اقدام کنن جلوی وام رو گرفتن.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/iaghapour/2769" target="_blank">📅 21:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4S885KrV4pBlq0VG0kTK50_CAYsMC_BDooEgWtMsYa6TJCvjSuDXrgb95xSwllP6iEPQJToTYc-GQxTpO9bH1rsRQ_n6GUxbBifGqGzSP70CLDlpD25iQDFVyJAeGG7NnIU8NqA8EiBoLQC6yUETO7rQV4kMCvJgDmR2Qm0Pe6-zqjWsv6N6VnKZwfqhNx_SKbvToq2GMxMNxIdK1vwLEpvcU1GExmFqtNhW_VWwyEHjL3aCfLAFCOfyq2dyZxnSMOlr9FTAIZobDcAP8P4vP4sBtQsTCXmsYxhb9UvOGYaBKHgYWOlfPPOQL7MxhLQMb3WObULcs-xkL4B3bSfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دامنه t .me تلگرام دوباره برگشت
امروز دامنه معروف
t.me
(لینک‌های کوتاه تلگرام) ناگهان از کار افتاد! این دامنه توسط رجیستری کشور مونته‌نگرو به حالت تعلیق درآمده و از کل سیستم DNS جهانی پاک شده بود؛ آن هم در حالی که دامنه تا سال ۲۰۳۵ تمدید شده بود.
گزارش‌ها نشان می‌داد که این مسدودی به دلیل تحریم‌های وزارت خزانه‌داری آمریکا رخ داده بود.
🔻
این دامنه مجدداً
فعال و رفع مسدودیت شد
و اکنون تمامی لینک‌های کوتاه تلگرام بدون مشکل کار می‌کنند.
©️
Behrad Javed
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/iaghapour/2768" target="_blank">📅 19:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2767">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbAqxMPqVFFihn_CGZi61HfQpHjTRbqSM2XBh1M_CtwU6IVmO-RomXXbjCowuwkMKXuMuS8RroxoYkwLVn3F1AL--WLQMjS7IMMEQp7fAg8JOFHGVhIeUhu2lNlQvhbpTeCe6mQL31aAg8Tw6g2ND7ilcpsrFwsgSdi9XKqXcBWrJ2CjsiavCdcFyGiDWxXxzeh-Um6k2hZwulzd1CKqWFGRc3yCrOKkz4EXXkbnKPP6iimuRnfy22NkU9Kk9FtjAabR-R01FSGZa_Rp_isWo74X5vp0oSz_lh2r6cJT5V2x0kyzKfrsN4EBzWseuYmQ1oUG4N6PmrB1WcavlBBz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بعضی از بچه‌ها خبر دادن مثل اینکه کج‌دار و مریز
IPv6
روی یه سری از اپراتورها فعال شده. البته هنوز دقیق مشخص نیست که این داستان موقتی و بخاطر اختلالات شبکه‌ست، یا اینکه واقعاً خبریه و دارن یه کارهایی انجام می‌دن.
🔻
از اون طرف هم عده‌ ای از دوستان از جنوب کشور پیام دادن و گفتن که اوضاع اینترنتشون خوب نیست و قطعی و اختلال شدیدی رو دارن تجربه می‌کنن.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2767" target="_blank">📅 13:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJJEo78NxPV57XFUWHPztz8vLRuC30sAvkG_UfqiDaFuomqU8mTRWtx0hrunnPN9jwBJhaw2vbwfkrbSo4aiBX0JFYcRPQ99oS7zWQbEe2Ez6sWa46mVT7dz61ddh49henf8rtzPOtPNbM5nQ6ZNHZVaufY48Ip7f_AjPSgazIqAEFQYU3y-N5EFLHEuY-IMOBvquU6Kkl21Hb3OvZvfVvB1_qIe0l7gCFdpCgEZnBR1uHRtkn-oGJ7gHgIuzjyefTxF6AEAO-NuI0SDZhBV575nhjR7SWB2poBzwp9EJ8vd1VUcu2a_KJNonpBM8UjXEPcZcGCrrOAkP_ZIF9Pu2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل معکوس با انواع پروتکل (BackPack)
🚀
🔹
در این ویدیو به آموزش صفر تا صد راه‌اندازی تانل معکوس (Reverse Tunnel) بین سرور ایران و خارج می‌پردازیم. اگه به دنبال روشی هستید که ترافیک شما را شبیه به وب‌گردی عادی کند و کمترین ردپا را برای سیستم‌های محدودکننده به جا بگذارد، این آموزش دقیقاً برای شماست.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#ریورس
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/iaghapour/2765" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2764">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">متاسفانه به بیشتر از ۱۰ نقطه از کشور حمله شده که بیشترینش سهم بوشهر عزیز بوده.
💔
شاید خیلیا در نگاه اول بگن خب مناطق نظامی بوده و به مردم عادی آسیبی نرسیده، ولی واقعیت اینه که پشت پرده یه اتفاقایی می‌فته که آدم تعجب میکنه از شنیدنش!
مثلاً امروز یکی از بچه‌ها می‌گفت توی شرایط جنگی، حتی اگه اینترنت هم قطع نشه، کلی از فروش‌های ما کنسل می‌شه؛ چون مشتری می‌ترسه و فکر می‌کنه مثلاً ما که از جنوب آنلاین‌شاپ داریم، دیگه نمی‌تونیم بار رو برسونیم تهران یا شهرهای دیگه...
خلاصه که فقط بحث قطعی اینترنت نیست که به کسب‌وکارها ضربه می‌زنه، خود جنگ، ترس از خرید و این ریسک‌ها هم کلی به مردم آسیب می‌رسونه.
دمتون گرم تا جایی که می‌تونید از این کسب‌وکارهای بومی حمایت کنید. قبل از اینکه نگران بشید و عقب بکشید، اول با پشتیبانیشون هماهنگ کنید؛ چون توی خیلی از همین شهرها و استان‌ها پست و تیپاکس دارن مثل قبل کارشون رو انجام می‌دن و جابه‌جایی بار بسته‌ نشده. پس با خیال راحت می‌تونید از این آنلاین‌شاپ‌ها و سایت‌هایی که توی این مناطق هستن خرید کنید.
🤝
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/iaghapour/2764" target="_blank">📅 16:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/iaghapour/2762" target="_blank">📅 21:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سلام بچه‌ها. یه مدتیه دوست دارم واسه تشکر از اینکه هم تو یوتیوب هم تلگرام کنار ما هستید، ماهی چند بار یه هدیه کوچیک بهتون بدم.
👇🏻
به نظرتون چی باشه بهتره؟
🔹
اکانت هوش مصنوعی
🔸
کانفیگ فیلترشکن
🔹
پول به صورت کریپتو؟
البته این وسط دوباره درگیری‌ها زیاد شده و فقط امیدوارم باز قطعی اینترنت شروع نشه که تمام انرژی و وقتمون رو بگیره :(</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/iaghapour/2761" target="_blank">📅 21:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/iaghapour/2760" target="_blank">📅 20:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❓
سوال یکی از کاربران:
من یه سرور دارم رو همراه اول فوق‌العاده عالی کار می‌کنه اما رو ایرانسل نه. چطوری می‌تونم بفهمم مشکلم از کجاست؟
💡
پاسخ و بررسی مشکل:
دلیل اصلی این اتفاق برمی‌گرده به تفاوت سیستم‌های فیلترینگ (DPI) اپراتورها. تجهیزات و محدودیت‌هایی که هر اپراتور اعمال می‌کنه با بقیه فرق داره؛ در نتیجه یه کانفیگ یا پروتکل خاص ممکنه روی همراه اول عالی باشه، اما روی ایرانسل اختلال داشته باشه یا اصلاً وصل نشه.
به جز این مورد، چند تا دلیل مهم دیگه هم وجود داره که باعث این مشکل می‌شه:
👇🏻
📌
وضعیت آی‌پی سرور:
خیلی وقت‌ها آی‌پی یه سرور روی یک اپراتور خاص شناسایی و محدود (کثیف) می‌شه، در حالی که همون آی‌پی روی اپراتور دیگه کاملاً تمیزه و عالی کار می‌کنه.
📌
مسیریابی شبکه (Routing):
مسیر اینترنتی که شبکه ایرانسل تا دیتاسنترِ سرور شما طی می‌کنه، ممکنه با مسیر همراه اول متفاوت باشه. گاهی شبکه یه اپراتور با یه دیتاسنتر خارجی به مشکل می‌خوره و باعث افت سرعت شدید یا پکت‌لاست می‌شه.
📌
حساسیت روی SNI و دامنه:
الگوریتم‌های تشخیص ترافیک اپراتورها با هم متفاوته. ممکنه ایرانسل روی دامنه یا SNI خاصی که برای کانفیگ استفاده می‌کنید حساس شده باشه و ارتباط رو همون اول قطع کنه.
📌
آی‌پی تمیز و شبکه توزیع محتوا (CDN):
اگه ترافیک سرورتون رو از پشت کلودفلر عبور می‌دید، احتمال خیلی زیاد اون آی‌پی تمیزی که ست کردید روی ایرانسل محدود و کند شده، ولی روی همراه اول هنوز جوابه. تو این حالت معمولاً با اسکن کردن و جایگزین کردن یه آی‌پی تمیز جدید مخصوص همون اپراتور، مشکل حل می‌شه.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/iaghapour/2758" target="_blank">📅 21:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قشنگ 2 ساعت با خودم درگیر بودم تا بالاخره حسش بیاد بشینم پای سیستم و کارای خودم رو انجام بدم. تا اومدم استارت بزنم، برقا رفت.
😁
دوباره این داستان قطعی برقا شروع شد. رسماً دهن سیستم و وسایل برقی خونه سرویس شد رفت!
🥲</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/iaghapour/2757" target="_blank">📅 21:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB0TSC90qArTY6mtRIqTjNFDQBOv58TzlrgzrnomH_OnHNh8zht785KWJtCS2qXsGPn_xzaiFi_3Seg40QSNanAgfjW4Py2hnaBej0UjmIwXknlaH8LczTSkKnL7TYXQ-PV0AjaZHoKRv-Ac4m2mCQKdPhxzAgUL04pfpfufganKQA1MZWOItQDGnSLwuUnAzfs2W1qK2RH1BdJNOmGuIVTOPJNBZ6T91V9SzWNZeT1n39jnmhsXiQhioIMop-n7PdCBCLLljhouXQ2UZIzaZ4lwiknz6YnSE5qRw9BqSwvaSh4u7EUrMxeKCdrsT-zU5kKU37LH45kCniKUUanMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
دلایل ناکارآمدی و خطرات قطع اینترنت برای امنیت سایبری
🔹
توقف به‌روزرسانی‌ها:
آپدیت‌های امنیتی سیستم‌عامل‌ها و آنتی‌ویروس‌ها قطع شده و دستگاه‌ها در برابر هکرها کاملاً بی‌دفاع می‌مانند.
🦠
رشد بدافزارها:
محدودیت‌ها باعث می‌شود کاربران به سمت نصب VPNها و پروکسی‌های ناامن و آلوده سوق پیدا کنند.
🛡
بی‌اثری روی حملات بزرگ:
حملات سایبری پیچیده (مثل استاکس‌نت) معمولاً روی شبکه‌های ایزوله انجام می‌شوند؛ بنابراین قطع اینترنت جلوی آن‌ها را نمی‌گیرد.
🔌
اختلال در اینترنت اشیا (IoT):
دستگاه‌های متصل و هوشمند به دلیل قطعی ارتباط با سرورهای اصالت‌سنجی، از کار می‌افتند یا ناامن می‌شوند.
📉
بحران اقتصادی و اجتماعی:
قطع طولانی‌مدت اینترنت، زندگی و اقتصاد مردم را فلج می‌کند که این موضوع خودش یک تهدید بزرگ برای امنیت ملی است.
⚠️
خطر اینترنت طبقاتی:
تخصیص اینترنت فقط به عده‌ای خاص، باعث ایجاد شکاف در جامعه، می‌شود.
💡
نتیجه‌گیری:
به جای قطع دسترسی مردم، باید امنیت سایبری شبکه‌ها را تقویت کرد و در سیاست‌های فعلی مدیریت اینترنت تجدیدنظر اساسی انجام داد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/iaghapour/2756" target="_blank">📅 15:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/iaghapour/2755" target="_blank">📅 01:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOFb-Mk4SLYNXRSDHijgGjaSMngZ_W6FtYw7PC1cINoitJcqnO1IvUzNV-_dsY0tDA07nUUpYTB6dSubwEMD6VbxHOQx81y8Ffetn7j9p8kcg9g9a1mV_GYk_qgE_C8rjVw7-UIJN5Sm2III3TWcZCt4nOPNZ-0rqFEddOyf0XoLAgNuUyc7HRZ2t9lMnJyBBrsEXbGos-R_BwXjTM2jaO8fwhkAipF1qvmhFVAwHtgIaaiwpgyekJNaoJw4A8UoeOXKyXGJSo6LXvphBO9ijgeyfEjmMVqBi0ufNhnwKQSRcfyM7seIDO7FKaPrEczEX4IQZFFuETXoiR6Dtg9wqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
قهرمان گمنام دنیای ویدیو؛ چرا VLC هیچ‌وقت پولی و تبلیغاتی نشد؟
🔹
بیشتر از ۲۰ ساله که پلیر محبوب VLC هر فرمت و فایلی که بهش دادیم رو بدون حتی یک ثانیه تبلیغ پخش کرده! دلیل این اتفاق شگفت‌انگیز، شخصی است به نام Jean-Baptiste Kempf که از سال ۲۰۰۳ به این پروژه پیوست.
با وجود اینکه VLC تا حالا بیشتر از 10 میلیارد بار دانلود شده، او پیشنهادهای تبلیغاتی چند میلیون یورویی رو قاطعانه رد کرد تا این برنامه برای همیشه کاملاً رایگان و بدون تبلیغ باقی بمونه.
🔸
اما شاهکار این افراد فقط به ساخت نرم‌افزار VLC ختم نمیشه! در واقع، تقریباً هر جایی از اینترنت که ما در حال تماشای ویدیو هستیم، روی پایه تکنولوژی همین تیم استوار شده است.
انکودر معروف
x264
که سال‌ها استاندارد اصلی پخش ویدیو در وب بوده و همچنین دیکودر
dav1d
برای فرمت جدید و بهینه‌ی **AV1**، دقیقاً دست‌پخت همین تیم و جامعه متن‌باز (Open-Source) است. غول‌های فناوری مثل یوتیوب، نتفلیکس و تمام مرورگرهای مدرنی که امروز استفاده می‌کنیم، همگی در حال استفاده از همین تکنولوژی‌ها هستند.
©️
behrad javed
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/iaghapour/2754" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2752">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭕️
نوا کلاینت (Nova Client) منتشر شد!
از همین حالا می‌تونید کلاینت بهینه‌شده، و قدرتمند پروکسی رو با رابط کاربری اختصاصی «نوا» روی تمام دستگاه‌هاتون نصب کنید.
✨
برخی از قابلیت‌های کلیدی:
🔸
ظاهر مدرن و Dark-first:
طراحی چشم‌نواز با زبان بصری نوا و گرادیان‌های نئونی اختصاصی.
🔹
رادار نوا (Nova Radar):
اسکنر فوق‌پیشرفته و یکپارچه برای پیدا کردن سریع آی‌پی‌های تمیز کلاودفلر.
🔸
پشتیبانی کامل از زبان‌ها:
سازگاری بی‌نقص با زبان‌های فارسی و انگلیسی به‌صورت کاملاً راست‌چین (RTL).
🔹
مدیریت هوشمند:
دسترسی به داشبورد زنده، روتینگ، مدیریت پروفایل‌ها و سابسکریپشن‌ها.
🔸
قدرت‌گرفته از Flutter:
فوق‌العاده سریع، سبک و هماهنگ روی تمام پلتفرم‌ها (Multi-platform).
📥
لینک‌های دانلود (نسخه v1.0.0-beta):
🖥
macOS (Apple Silicon)
:
Nova-macOS-arm64.dmg
🪟
Windows
:
Nova-Windows.zip
📱
Android
nova-client.apk
🍎
iOS / iPadOS
TestFlight
🌐
وبسایت رسمی
📦
گیت‌هاب پروژه
نکته مهم برای macOS:
اگر سیستم بلاک کرد، این دستور رو در ترمینال اجرا کنید:
xattr -dr com.apple.quarantine /Applications/
Nova.app
👈🏻
نکته: Nova Client در واقع یک فورک بهینه‌شده از Karing هست که کاملاً با طراحی Nova Proxy هماهنگ شده و رادار قدرتمندش هم داخلش ادغام شده.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/iaghapour/2752" target="_blank">📅 21:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2751">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaHXU8FJEZABsNwOqY1DbIEEFAzDFlqpPAQStgpFUFoXOQx-3Vyzve7JmLpUX9sAT6-gfCf9nvcIskiw_gpg8uwRV3i8VtFSy_WdiDfRN2Z2b_S6L-yZLsA-tKgLIG01SbrZD5to3A8Lo88_jTDAPO3alCYQjAMGvbW4TED4z2_Z9OvXawORWTHS5DKUiSC0Z2cYArfoFH0qmiPFXQCpiflKyCTLGwLhZ6wpSu9AKHq4mXc8EGKSNn9xvJdHL5clSueotuiQIdBXpnCxONCaP76BFzDHzFsxBgy76f4EKpfZqsO6yECj4YVPeQ_JFLZZ0E8Vt3EfSYyU4e6r7HmoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط بعضی افراد میدونن این چیه
😊</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/iaghapour/2751" target="_blank">📅 19:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2749">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/iaghapour/2749" target="_blank">📅 20:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2748">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA7GBGBAO2zsfKWwNf387X4_dq736UdT7ZbLpiPrS0_SKP7rBux7mgdXej99O66nTkT-HF321SoDVVaJoolRJUI1w9KMxIQdwduaEo2XyqO82JikBmiGjBGSHdOX4nqgqM_OPJbMlue3wvTy4eHyyoAgX6BL0VElKZrI8bTnymEApycWiiJk1sPhJlQ2kkHvwckW1j2kPBUYLyLF3F29gO33uKTSUadsNlq8mwOUibbiZJ9dppFpmcOAwsCgOgTt5Z4QF_UmzsIe2mR-5Ea7slmjleH4bNICOBT-tElRE0QSK_VF28aWHZ9gnXmiFhpILSgU7K7SlL9OO8cnb0ZzQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مسدود شدن ناگهانی پنل‌های رایگان روی کلادفلر
گزارش‌های متعددی از کاربران دریافت کرده‌ایم مبنی بر اینکه پنل‌های رایگان (مانند نووا و BPB) به‌طور ناگهانی بن شدن.
سر اینکه چرا این اتفاق افتاده دو تا بحث هست؛ یه عده میگن خیلیا از قصد رفتن این پنل‌ها رو به کلادفلر ریپورت کردن تا بسته بشن. یه عده هم میگن نه، خود سیستم هوشمند کلادفلر تشخیص داده و بن کرده. خلاصه دلیلش هر چی که هست، تو استفاده از این ابزارها همیشه ریسک بسته شدن وجود داره.
💡
یه توصیه خیلی مهم:
بچه‌ها، واسه ساخت و راه‌اندازی این پنل‌ها اصلاً و ابداً از اکانت و ایمیل اصلی خودتون استفاده نکنید! همیشه یه حساب فرعی بسازید و با اون کارتون رو راه بندازید.
🔄
آپدیت جدید پنل نووا (Nova):
توسعه‌دهنده پروژه نووا خبر داده که کدهای این پنل رو دوباره بازنویسی کرده و تو آپدیت جدید، مشکل ارورهای مختلف (مثل همون ارور رو اعصاب 1101) کلاً برطرف شده.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/iaghapour/2748" target="_blank">📅 20:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2747">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">.
⚠️
ببینید، اینکه بیایم مصرف کاربر رو چند برابر حساب کنیم (مثلاً طرف ۱ گیگ مصرف کرده ولی ۲ گیگ از حجمش کم کنیم)، اسمش زرنگی نیست، رسماً دزدی و کم‌فروشی تو روز روشنه! اینجور کارا فقط گند می‌زنه به اعتماد مردم و باعث میشه مشتری به بقیه فروشنده‌هایی که دارن…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/iaghapour/2747" target="_blank">📅 18:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2746">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یک تشکر ویژه از همراهان همیشگی
🌺
دوست داشتم از این فرصت استفاده کنم و از تمام کسانی که تو این مدت اخیر که درگیر محدودیت‌های شدید اینترنت بودیم، به هر شکلی پشت ما ایستادند و کمک کردند، از صمیم قلب تشکر کنم. حمایت‌های شما باعث شد تا تیم ما بتونه هر کاری که از دستش برمیاد رو در این رابطه انجام بده.
از دوستانی که کانفیگ‌ در اختیار ما قرار دادن، تا عزیزانی که اکانت سایت‌های مختلف از سرویس‌های هاستینگ گرفته تا ابزارهای هوش مصنوعی و... رو به دست ما رسوندن تا کارها لنگ نمونه؛ واقعاً ازتون ممنونم.
و یک تشکر ویژه از دوستانی که با کامنت‌هاشون و دفاع از کار ما در گروه‌ها، سنگ تمام گذاشتند و بزرگ‌ترین حمایت رو از ما کردند.
خیلی دلم می‌خواست اسم تک‌تک شما عزیزان رو اینجا بیارم و شخصاً قدردانی کنم، اما به دلایل مشخص و برای اینکه برای خودتون بهتر و امن‌تره، از این کار صرف‌نظر می‌کنم. ولی بدونید که تک‌تک کمک‌های شما برای ما ارزشمنده.
دقیقاً تو همین زمان‌های سخت و بحرانیه که باید کنار هم باشیم و بدون هیچ چشم‌داشتی به همدیگه کمک کنیم تا از این شرایط عبور کنیم. (البته بماند که در این میون، کانفیگ‌های میلیونی هم به پست ما خورد که خب... بگذریم!
😄
)
امیدوارم دیگه در هیچ زمانی دچار مشکلاتی شبیه به این نشیم و روزهای بدون محدودیتی رو پیش رو داشته باشیم.
دم همتون گرم!
✌️
💚</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/iaghapour/2746" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2744">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Us9_NwgrDRPo8vgp4OlZKc1v2ir_yLmnWhz_Xl2fssmtZAxz8VNFM5lAAUqpXoQeL2PE190KAHqaKI0YOsqsU2z7vGOyt5t8FjPR4-EkhE4pHCE4FnacYwuhGcGQ11QVlIxpAGFaIL8WI-v5sNEhdqT8dCnXxnGVcm3zFYXH0uQZTBwTOvXmI0qIMRP1nGfwXBbABoPM1yhOyxI6dfDq82oN_FHNw7WoiWx7wWlCd7ILm2dXe2y3ZNe_gmc8xzd3M52zgDflFb8Nce9vzDNgRU7K7n7phmB1XN1zeXRk3I2MEQkO5uagD7OvaCtjmaWsLebXt4HJgcJ3I7B413Gz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.
⚠️
ببینید، اینکه بیایم مصرف کاربر رو چند برابر حساب کنیم (مثلاً طرف ۱ گیگ مصرف کرده ولی ۲ گیگ از حجمش کم کنیم)، اسمش زرنگی نیست، رسماً دزدی و کم‌فروشی تو روز روشنه! اینجور کارا فقط گند می‌زنه به اعتماد مردم و باعث میشه مشتری به بقیه فروشنده‌هایی که دارن سالم کار می‌کنن هم به چشم دزد نگاه کنه.
اگه خرج سرور و هزینه‌ها بالا رفته، خیلی روراست قیمت‌ها رو ببرید بالا. مشتری ترجیح میده گرون‌تر بخره ولی بدونه دقیقاً داره بابت چی پول میده، تا اینکه یواشکی از حجمش دزدیده بشه.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/iaghapour/2744" target="_blank">📅 20:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2743">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oExLB60Ky7l5PH36ImCuQuWF919uRojf7ZsB5UipQwr4I9ERw1YpHfdd2LVUIESHUV9NwbBLqIe8LQH6S9mpPTq_Lb8fWWyONn-QSW6gpp0vCVCx9H-usVAmdUEVJs1Fg9Y5_QdQRve78VDrBMtfSqA2sbA44N7l-2oaPqcrCstJVeARDam99tmNIA1285unzufrbSLHjdPoO4lalSeAsvdallZNtMb2Zh39rfuD1E1Y2NNJul0V6ljRR3TNfRLxwjOyA6O3935oMqdLBMv2KHlW29r-c5uxuKnhZfFeRGIjqnXzH2yxtesrf4twYiGYY8bXQfzQl8VMxlFrJ2udiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.11.0 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر شخصی بالا بیارید و با دوستان خودتون چت کنید.
-
🛡
پنل ادمین با مدیریت کامل یوزر ها و چت ها
-
👑
رول owner برای بالاترین سطح دسترسی
-
⚔️
رول admin برای دسترسی محدود به پنل ادمین
-
⚙️
دسترسی به تنطیمات برنامه از طریق پنل ادمین
-
📋
بخش لاگ برای مانیتور از چند منبع مختلف
-
👤
ساخت یا ادیت یوزر از طریق پنل ادمین
-
💬
پاک کردن کل پیام ها یا ریست کامل دیتابیس از طریق پنل ادمین
-
📖
وبسایت ویکی سانگبرد در
docs.songbird.website
-
🕑
نشان دادن آخرین بازدید کاربران
-
📡
انتخاب Songbird به عنوان سورس Remote channel
-
💨
بهبود عملکرد قابلیت Remote channel
-
🔧
رفع باگ های گزارش شده
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/iaghapour/2743" target="_blank">📅 20:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2742">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg7c3i7yLzcH3qUaxv-tYnt9ZVsyegb5fq6RgnMXwXCGre4Jd4wv07hfziC0iczPfOladiyOF4eNnwOqcqJ0DnSYxrzfNoqWDXiVUS6c6hO_PP1nnGdjKLNvFRDHTQOnpI1ibXfpLhhf3Smumdg2oP-rIlGyd3nQoW9szq7umBfBeC-FSOiYB7OI0KgDC_I3mUU1xa0DxO7jUpuKXWbHW1Ttd-R4EzuLnSPQ40CGd_niCmtle7JKHq_X--haajruahghTzBx7xkSEzXoH_ExfwJYOvetao5s5csdHY-K5Sy8m9UFKzwYZeCLvkZcCOyijxdl_tTlLWsYPR-Hscm_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قابلیت جدید گوگل سرچ کنسول: ردیابی دقیق ترافیک شبکه‌های اجتماعی
گوگل ابزار جدیدی به نام Platform Properties را به سرچ کنسول اضافه کرده است که امکان ردیابی ترافیک ورودی به شبکه‌های اجتماعی از طریق نتایج جستجو را فراهم می‌کند. با این قابلیت کاربردی، می‌توانید دقیقاً متوجه شوید مخاطبان با جستجوی چه کلماتی به ویدیوهای یوتوب یا سایر شبکه‌های اجتماعی شما (مثل ایکس، اینستاگرام و تیک‌تاک) رسیده‌اند.
این ابزار سه گزارش جامع ارائه می‌دهد؛ گزارش عملکرد برای نمایش دقیق کلیک‌ها و میزان بازدید، گزارش اینسایت برای شناسایی پست‌های موفق و تحلیل روند ترافیک، و بخش دستاوردها برای ثبت رکوردهای جدید و پیگیری رشد کانال. برای راه‌اندازی این سیستم، کافی است در سرچ کنسول یک ویژگی جدید (Add property) ایجاد کرده و پس از انتخاب پلتفرم هدف، مراحل تأیید هویت را طی کنید. این آپدیت طی هفته‌های آینده فعال می‌شود و یک امکان فوق‌العاده برای تحلیل دقیق‌تر بازخورد ویدیوهای آموزشی و مدیریت سئوی محتوای شما خواهد بود.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/iaghapour/2742" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2740">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twX6fdwXtQYudIUNJiG0Qn3aVracL3sLA_Bp6RvEKOCOC-oE1SIlnldFu1kSxwfZbjxJTA9ALAm8MSdbmttqDeOaP8h2CW1MZa3fdVto7pIE6vSTX55Ed4ohOXVV8wDiCcjgMh7l4V4wgBM4vGxeVqR8TirgYHFvGRYyU8_wWq7vVNORP8qoFLlsm7CealcFD1_BqeAEgoLrLE9Wri1SmYwMWp0mH5r5UOGg9MbSJCByS5WKPBbK8A6oDsUNkI3z3aDLF0n73x5wYkBtcrFMqiALXoRhCg3OZvDEv0kViVnqKY228hzTUYAnowhGfAOqlGrkmdkOh7dOOJONH2zaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اعتراض ۱۱۵ هزار نفری به سونی؛ دیسک‌های فیزیکی را حذف نکنید!
یک خرده‌فروش کانادایی (PNP Games) کمپینی با نام «Don't Kill the Disc» به راه انداخته که تاکنون بیش از ۱۱۵ هزار امضا برای توقف برنامه جدید سونی جمع‌آوری کرده است. سونی قصد دارد تا سال ۲۰۲۸ درایو نوری را به طور کامل از کنسول‌های پلی‌استیشن حذف کند.
🔹
جزئیات این ماجرا:
🔸
نگرانی معترضان:
به گفته راه‌اندازان این کارزار، حذف دیسک‌های فیزیکی به معنای نابودی کامل زنجیره‌ای از مشاغل (خرده‌فروشان، توزیع‌کنندگان و تولیدکنندگان)، از بین رفتن بازار بازی‌های دست‌دوم و نادیده گرفتن جامعه کلکسیونرها است.
🔸
دلیل سونی برای این تصمیم:
همسویی با ترجیحات کاربران و رشد خیره‌کننده فروش دیجیتال. آمارها نشان می‌دهد سهم فروش دیجیتال بازی‌ها از ۱۳ درصد در سال ۲۰۱۳ به حدود ۸۰ درصد در سال ۲۰۲۵ رسیده است.
🔸
نظر تحلیلگران:
به دلیل سودآوری بسیار بالاتر فروش دیجیتال و کاهش هزینه‌های تولید سخت‌افزار برای سونی، کارشناسان اقتصادی احتمال تغییر موضع این شرکت را با وجود این اعتراضات گسترده، بسیار اندک می‌دانند.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/iaghapour/2740" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2739">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🟢
دوستان عزیز، همون‌طور که قبلاً هم اشاره کردم، کامنت‌های یوتیوب به دلیل جلوگیری از اسپم، به‌صورت دستی تایید میشن. چند ماه پیش یه عده شروع به فرستادن پیام‌های اسپم و نامربوط زیر ویدیوها کردن و برای اینکه مشکلی برای کانال پیش نیاد، مجبور شدم تایید کامنت‌ها رو دستی کنم.
تا الان پیام‌ها هر ۲۴ تا ۴۸ ساعت بررسی می‌شدن، اما از این به بعد
هر شب
کامنت‌ها رو بررسی و تایید می‌کنم. البته در تلاشیم تا راهی پیدا کنیم که این محدودیت به‌زودی کمتر بشه. از درک و همراهی همیشگی شما ممنونم.
💚</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/iaghapour/2739" target="_blank">📅 19:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2738">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9NnpE3zVDx62yUyNLYZruBU5G4n9Z6C0TU7X_7dFJEYqN_eoyKxgITa8jseE8pEXRJj3u9baqBmB0-GarwhiSRGzD8QOkVjUW_FOH88ApHD6eH4LsZMMBI9aMuCLSnlfshg5wqMVgUSJZyP7PXRy_bwF9xz4ag9-wXmhB00cYCTzm8NfKeBM2Of_uWNKMwIoTqopIC_biKt_kN2wuew0a9AZTDX4E0HESgMGyjwccgAkd2vHgIhFj3Pj_InOep_JyduaBTNms3YK7gA5KUKBJnyNqfMBFEyaQM8eG3bYQxhVAuzHeOtTuF4mvrBQA0sciF9XHg1OTrHyzYEn7DXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استفاده پنهانی گوگل از عکس‌ها و ویدیوهای شما برای آموزش هوش مصنوعی!
گوگل به‌تازگی تنظیمات حریم خصوصی خود را تغییر داده است. با این تغییر، فایل‌های صوتی، تصاویر و ویدیوهایی که در سرویس‌های مختلف گوگل (مثل جستجو، مپس، ترنسلیت و...) آپلود می‌کنید، ممکن است برای آموزش مدل‌های هوش مصنوعی این شرکت استفاده شوند.
🔹
چگونه این قابلیت را متوقف کنیم؟
خوشبختانه امکان مسدود کردن این دسترسی وجود دارد. برای جلوگیری از استفاده شدن داده‌هایتان مراحل زیر را طی کنید:
۱. در تنظیمات حساب کاربری گوگل خود به بخش
Search Services History
بروید.
۲. تیک گزینه
Save Media
را بردارید.
۳. در همین بخش می‌توانید کل سابقه جستجو را غیرفعال کنید یا یک زمان مشخص برای حذف خودکار (Auto-delete) اطلاعات تعیین کنید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/iaghapour/2738" target="_blank">📅 19:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2736">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCMr-RRvzgHESkDmiSiiBsj6Nlj_Ydb0pOYx8j3GJNmuX3d1XsDvrLxb0wgU7SX9w1ZsGZ_3vD9Inqy3viypc_ny0EXDIoa746zR0_ChGhLWpwcvJpLdmmn6M_SHTpBnYKvcedaTZIYnIUwIFfkkm-LH0UgjoE_LsB4JdsOUT9qnpt7LazCIc6WvTIIeKpkYNbPAA5N_BnQ8S5WdrFMs7sPNscYn6LFVVfIAxwzaW9u2S9qU3_ngAeoMpxYNwGvfIsmlSjOYL-N6ga-3vYh-B0J8mRJcwdETOB9vz9vNsdpx3ohytz4CqNPaKupCsZZBWmGD6YSAo4x0_CmOj1TBzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠
معرفی پروژه Iran Dev Tools؛ حل مشکلات در سروهای ایران
قطعاً به عنوان یک توسعه‌دهنده بارها با چالش تحریم‌ها، فیلترینگ و سرعت پایین دانلود پکیج‌ها و دپندرسی‌ها دست‌وپنجه نرم کرده‌اید. پروژه متن‌باز Iran Dev Tools مجموعه‌ای از اسکریپت‌های هوشمند و مستقل است که دقیقاً برای حل همین مشکلات تکراری برنامه‌نویسان روی اینترنت ایران طراحی شده است.
🔸
منوی مدیریت یکپارچه لینوکس:
شامل اسکریپت نصب Docker به همراه تنظیم خودکار میرورهای رجیستری ایرانی برای دور زدن تحریم‌های داکر.
🔸
بنچمارک و تغییر هوشمند DNS و میرور APT:
تست زنده و تنظیم سریع‌ترین DNSها و مخازن سیستمی (APT) لینوکس بر اساس کیفیت شبکه شما.
🔸
تنظیم خودکار میرورهای برنامه‌نویسی:
شناسایی و ست کردن بهترین میرورها برای پکیج‌منیجرهای محبوب از جمله
npm
،
pip
،
Go
،
Composer
و
NuGet
تا با بالاترین سرعت ممکن پروژه‌های خود را توسعه دهید.
🔗
لینک ریپازیتوری پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/iaghapour/2736" target="_blank">📅 21:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2735">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG5PgIwVbV54vEW2pmopom9MFN4T42Dsi6NGPYCDgQJEP_UNgCS3URmeYKs6Hi0e6sP2qEqYPUNO3qVEIl85QLwxmP5i-lx4WUkGvZHfmz1V0TxGfiFx-LBaUqemPg-phdCrrsu9PGLFYLlg8fzeY2oQ_aXoBAMlT7cIj9AJFDzYnYpCDxv9bKG1vxC8a5TwTchtpjgNwQ36qfEv5G72QNswblWTL3OlXKtTtzeFc5rD6LCvPMyJ0prGAVDhGl_Wni0oVf-tSoGey2jIgzCUyVx-RQ91cuPJGyHf51gtRckZhFQ2B41332svs_jKNi1w7P7zbO6bh51skr6CZ17R0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی (GRoute)؛ کلاینت سبک و مدرن اندروید برای عبور از فیلترینگ
جی‌روت یک کلاینت فوق‌العاده سبک و روان برای اندروید است که بر پایه
Xray-core
ساخته شده و با ظاهر شیک و مینیمال اتصال به اینترنت آزاد را بسیار ساده‌تر کرده است.
🔹
ویژگی‌های کلیدی کلاینت GRoute:
🔸
پشتیبانی از پروتکل‌های مدرن:
سازگاری کامل با VLESS، VMess، Trojan و Shadowsocks در کنار ترنسپورت‌های پیشرفته‌ای مثل REALITY و TLS.
🔸
ابزارهای پیشرفته عبور از فیلترینگ:
مجهز به قابلیت
فرگمنت (Fragment)
برای دور زدن مسدودسازی SNI، سیستم Sniffing و مسیریابی تفکیکی (اتصال مستقیم سایت‌های ایرانی).
🔸
مدیریت ساب‌سکریپشن و وارپ:
به‌روزرسانی خودکار لینک‌های ساب، نمایش حجم و تاریخ انقضای اکانت، به همراه امکان ساخت کانفیگ
WARP کلودفلر
تنها با یک کلیک.
🔸
اسکنر اختصاصی IP تمیز:
اسکن رنج‌های کلادفلر و پیدا کردن کم‌پینگ‌ترین آی‌پی‌ها برای شخصی‌سازی سرورها.
💡
پ.ن:
در حال حاضر فقط نسخه
اندروید
این برنامه منتشر شده است، اما نسخه
ویندوز
آن نیز به‌زودی عرضه خواهد شد.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/iaghapour/2735" target="_blank">📅 20:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2733">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euE_5HoBZeXW9bDNIHqmKEccGQfG_sKhrdzjTxfM1c8dBdkv4ubiIlaNKkLnrZeecotxQYY2tlsvygaIWTM20QOmMwivu-f0vHVpy5JLcRiPKKzj4eaqAJdRauF9CtOEoh0opXjwvZ_1LihYoEl74q-PNK-KWc8ZwUVeHsLLt_cmoz-54e2k3bZSY-RDEosWXbonmYnQJNMAXf-Q08NMNq22FhsWCxuF5WslXM71dtI-tdimomJQQ9dmrMKFoKsTgFrtWhcW25W_QiNZsOdBilZPo551Gd_YxHAJHLDqDu6mLROlC4GG1wfAFww5sIiM86bS312ymYZb60BdKaFz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون دانش فنی فیلترشکن شخصی و رایگان بساز! (با یک کلیک)
🚀
🔹
تو این ویدیو قراره یه روش فوق‌العاده راحت رو بهتون معرفی کنم که بدون نیاز به دانش شبکه و بدون سرور مجازی، بتونید فقط با یک کلیک و تو کمتر از ۵ دقیقه یه فیلترشکن شخصی، کاملاً رایگان، پرسرعت با قابلیت تعویض لوکیشن و ایجاد کاربر با محدودیت برای خودتون بسازید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#رایگان
#ورکر
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/iaghapour/2733" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚠️
آقا این همراه اول قشنگ داره عجیب‌غریب حجم می‌خوره! اول که اومدن نصف بسته‌های خوبشون رو حذف کردن که مجبور بشیم بسته‌های گرون‌تر بخریم. بعدش هم برای تست یه بسته ۶ گیگی خریدم؛ منی که بیشتر از وای‌فای استفاده میکنم و ۶ گیگ برام ۱۰ روز کار می‌کنه، چشم باز کردم دیدم بعد دو روز پیام اومده بسته‌تون تموم شد!
توییتر رو که نگاه می‌کنی همه دارن از همین دزدی و حجم‌خوری شکایت می‌کنن. ایرانسل و رایتل هم همین‌طورین یا فقط اینا این‌جوری دست‌شون تو جیب مردمه...!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/iaghapour/2731" target="_blank">📅 15:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otOaVaRIRF5oUGZVDqRkrg-mTCBAGTl8JApkm5Rpzyr3ERxkRviRcaeDEnbIpQTCfPGZMKW59I00Uixgr2tCPPV1ZRI06I4f1j-ygjfrI2g_LSo2u7MqBnBHFpsWZ_TbzOe9qHmcyr9Cy4ew9m8KVJIiId4GZLbQd_5pOngIDDkSTSh6q4yS_fIiUT1V-Kn4bszi8bHGId27WDhrsNTNY4V5tB02jfVAdsehUe_jAxLPeUZTGpkYONCfq-6F-tAoi79KKU1edtLHIdgBq3LbYrsY7irD8p6MfN47Zj0tX3jjpkmH1Gwq1d5gaG3Wmwb3RHQ11O5ImiuiIRvULeD3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ری‌برندینگ بزرگ سایفون؛ ظاهر کاملاً جدید و بهبود دور زدن فیلترینگ
سایفون (Psiphon) پس از سال‌ها دست به یک تغییر هویت بصری و ری‌برندینگ اساسی زده است. ظاهر قدیمی و سنتی این اپلیکیشن جای خود را به یک طراحی بسیار مدرن، مینیمال و شیک داده است.
🔹
مهم‌ترین تغییرات در نسخه جدید:
🔸
رابط کاربری مینیمال:
محیط برنامه از آن فضای شلوغ قدیمی فاصله گرفته و با استفاده از رنگ‌های گرادینت ملایم و پس‌زمینه روشن، تجربه کاربری (UX) روان‌تری را ارائه می‌دهد.
این تغییر ظاهر نشان می‌دهد که قدیمی‌ترین ابزارهای فیلترینگ نیز برای همگام شدن با سلیقه کاربران مدرن، در حال به‌روزرسانی زیرساخت و طراحی خود هستند.
🔻
دانلود از گوگل پلی
🔻
دانلود از اپ استور
🔻
دانلود سایر نسخه ها
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/iaghapour/2730" target="_blank">📅 20:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2728">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hedioum Tunnel Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.1 KB</div>
</div>
<a href="https://t.me/iaghapour/2728" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
Hedioum Tunnel
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/iaghapour/2728" target="_blank">📅 19:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2727">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X019GMo7Xi7iuYNJVMZz7RymPUz1Az0KJbWTSU_NPwk6PbWkYnTQA_9lYid0J-cT0sMsILnd_YutvRL4NjSgW-CphnUm04OPEhoZYyGdEsf5uSEoNz6mat8id9ldXZKTmIiGnvS5m6iIN060oo-lrNjmRx9UcLkaVMQMhny5XCyNcfSSjPfBKUA31-mqD1J0cTii5Q7gpN00EUKi5vMIFrGhQCKiMYGzVTj-eOOxPN8kbG0nyvmO4U0ujxjxW4BuV2WtPMd_8W90rEDs3A2qMI3KWJrW_dovcCiBBb6KltC3F3t1oOWDrUSN3uA0AkYvWxh3kak816XB_dt6XjDuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش راه‌اندازی Hedioum Tunnel: تانل مقاوم‌ در برابر DPI
🔥
🔹
با پیشرفته‌تر شدن سیستم‌های مانیتورینگ و DPI، خیلی از تانل‌های معمولی این روزها دچار افت سرعت یا قطعی میشن. اما تو این ویدیو رفتیم سراغ یک راهکار قدرتمند به اسم Hedioum Tunnel که به خاطر مکانیزم‌های خاصش مقاومت خوبی در برابر تشخیص و اختلال شبکه داره.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/iaghapour/2727" target="_blank">📅 19:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2725">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUnWkfn8rWkDR1P9uyGK3HJPysuMYsYvCj94VfHiQgLQ-rvuCceCRvNuGSmMLDWrZdEJKXjW3e5oKonDnV8pCxl9vM8bze8XPw-uw8MVk_3QnT27aXixnmJfro7FmD6V60GyW7L4yHXvfWU-WHhbwlGzZLrHzsavCGz11ll1C2u05QaYHEZxMIn20K6FiS74xfXyV6nsZKCuvs4rbWyoF9NAcLRXB_d23EJh3_sKa7InPlS5Abf0oGd8TJn0tBTAZ-PbCdsX2txOs0p3Pxaf2gjAaYo1geRpJrDA_rSFAb-j72aL1ykPXEuSUnrOCKX7tI36SQVyvQHxKlEvrneRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ارتقای بزرگ هوش مصنوعی پروتون؛ Lumo 2.0 با قابلیت تولید تصویر منتشر شد
شرکت پروتون (توسعه‌دهنده سرویس معروف پروتون‌میل) نسخه جدید هوش مصنوعی خود را با نام
Lumo 2.0
معرفی کرد. این نسخه با تمرکز شدید روی حریم خصوصی، قابلیت‌های جذابی مثل تولید تصویر، حافظه اختصاصی و جستجوی امن وب را به همراه دارد.
🔹
ویژگی‌های کلیدی Lumo 2.0:
🔸
عرضه در دو نسخه:
مدل
Lumo 2.0 Max
برای کارهای پیچیده (با ارتقای ۲۴۰ درصدی عملکرد نسبت به قبل) و مدل سبک‌تر
Lumo 2.0 Lite
برای کارهای روزمره.
🔸
قابلیت‌های چندوجهی:
امکان تولید، ویرایش و تحلیل تصاویر در محیط گفتگو به صورت کاملاً رمزنگاری‌شده.
🔸
شخصی‌سازی پیشرفته:
اضافه شدن قابلیت حافظه تحت کنترل کاربر، تعریف پروژه‌های رمزنگاری‌شده و امکان ساخت دستیارهای سفارشی.
پروتون که حالا بیش از ۱۰ میلیون کاربر در بخش هوش مصنوعی دارد، هدف اصلی نسخه دوم را جذب کسب‌وکارهایی قرار داده که نگران امنیت داده‌های حساس خود هستند.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/iaghapour/2725" target="_blank">📅 20:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2724">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv8w0bmS0KhxvEE7KQ8qrtgigObzMKbfcLLJKbJXCAaxHEeLrfikDrnQOYzPdh1FGug86qz2GHQQdJtxgWhWQSxUK1Vl2bGqBqEu5Y_9cxTbVnD9GyQ6aLEEH3oIsDsuuMchYWRDUytNLl3f4D9Mglp9xlJjNFiulf94_M_PWzlvZE2Mx6JcLaWGmdsx3brFnu6SKfuIM5c--8GCmZqAe_DrQe8bkWGUMJ8gmpY_9PRgKFAgF4AVqtzAo7u-VkkkQkIFSyYdb-5WzSgb9JQr7zT15S47bl-J93w5K_8mAPOQIiudr9MK_NbHWcQlSf8IEpFUsv-oje7IUjjnKacEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
افزایش بی‌سروصدا و ۱۰۰ درصدی قیمت اینترنت فیبر نوری مخابرات!
شرکت مخابرات در روزهای گذشته، در سکوت کامل خبری و بدون اطلاع‌رسانی قبلی، قیمت بسته‌های اینترنت فیبر نوری را به شدت گران کرده و تغییرات عجیبی در سرعت آن‌ها به وجود آورده است.
🔹
مهم‌ترین تغییرات اعمال‌شده:
🔸
حذف سرعت‌های نجومی:
بسته‌های جذاب با سرعت ۱۰۰۰ مگابیت (۱ گیگابیت) کاملاً حذف شده‌اند و سرعت تضمین‌شده پایه برای تمام بسته‌های تمدیدی روی ۱۰۰ مگابیت قفل شده است!
🔸
جهش دو برابری قیمت‌ها:
هزینه بسته‌ها بین ۵۰ تا ۱۰۰ درصد افزایش یافته است. به عنوان مثال، بسته یک‌ماهه ۳۰۰ گیگابایتی که قبلاً با سرعت ۱ گیگابیت ۴۰۰ هزار تومان بود، حالا با افت سرعت به قیمت ۹۰۰ هزار تومان (بدون احتساب مالیات) فروخته می‌شود.
🔸
گرانی گیگابایت‌ها:
قیمت هر گیگابایت اینترنت فیبر که پیش از این حدود هزار تومان بود، حالا به نزدیک ۳ هزار تومان (و در بسته‌های کم‌حجم به ۶ الی ۷ هزار تومان) رسیده است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/iaghapour/2724" target="_blank">📅 20:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2722">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guLnTNDXv1HfPyoHDYOy9s3TjMgFVYlmQ4W-nz6LT1cu33Sr8YPH0gmxFT3jT7mkBDIuSYEUvVRX29vFh85TbydfZ6dqk6MbrDB3lx2xeoI2jDafMVqCMjBOM4uO6XnHxGsBeQKMxYIzgzSPsjcD2cKJH4csrh5JNh4Q5OLj-C8rGmxfiSsjvLROJ_b6C_6A88Pzkf4JS0xhzgTxiJGvVenT72jB8BgE47S3rKhdaDEev8_t6XPKAk4J8D6eNg7NxHLa0fEgO2X-HC2URyl7OPnZa9RH9b2zhkJgMWyRvwcy0PrrMEFnxxGZxi6hwjMYAEWZuHqkTomGpbG5cp5PVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پلتفرم متن‌باز مدیریت DNS با دامنه دلخواه
با این سیستم می‌توانید یک سرویس ارائه ساب‌دامین رایگان روی دامنه اختصاصی خود راه‌اندازی کنید. کاربران می‌توانند رکوردهای دلخواه خود (مثل
mysite.example.com
) را بسازند و تغییرات به‌صورت آنی از طریق API روی Cloudflare اعمال می‌شود.
🔹
ویژگی‌های کلیدی:
🔸
پنل ادمین و کاربری حرفه‌ای:
ورود با اکانت گوگل یا ایمیل، مدیریت کامل زون‌های کلادفلر، تعیین پلن و محدودیت‌گذاری برای ساخت رکوردها.
🔸
ربات تلگرام یکپارچه:
امکان ثبت‌نام و مدیریت کامل رکوردها مستقیماً از طریق ربات دوزبانه تلگرام.
🔸
امکانات ویژه:
سیستم دعوت از دوستان (Referral) برای دریافت سهمیه بیشتر و قابلیت ورود/خروج دسته‌ای رکوردها (CSV).
🔸
راه‌اندازی خودکار:
نصب بسیار آسان با یک دستور لینوکسی (Bash) همراه با گواهینامه SSL رایگان و بکاپ خودکار دیتابیس.
🔗
گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/iaghapour/2722" target="_blank">📅 20:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2721">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
وعده وزیر اقتصاد: بازگشت عمده خدمات بانکی از هفته آینده / اطلاعات مشتریان امن است
علی مدنی‌زاده، وزیر اقتصاد، با اشاره به تداوم حملات سایبری به شبکه بانکی کشور اعلام کرد که بخش عمده خدمات مورد نیاز مردم از ابتدای هفته آینده مجدداً در دسترس قرار خواهد گرفت.
🔹
نکات مهم صحبت‌های وزیر اقتصاد:
🔸
امنیت داده‌ها:
تا این لحظه هیچ‌گونه اطلاعاتی از مشتریان از دست نرفته است و استفاده از سامانه‌های پشتیبان، مانع از بروز مشکلات جدی در حفظ دارایی‌ها و داده‌ها شده است.
🔸
تداوم حملات:
پس از بازگشت سامانه‌های بانک‌های ملی و صادرات به مدار، تجهیزات جدید آن‌ها مجدداً هدف حمله قرار گرفته است؛ اما به لطف سامانه‌های پشتیبان، بخش زیادی از این حملات برای کاربران محسوس نیست.
🔸
اولویت‌های شبکه بانکی:
تمرکز فعلی روی بازگرداندن سریع سرویس‌ها، شناسایی منشأ حملات و افزایش سطح حفاظت سیستم‌هاست. با این حال، راه‌اندازی برخی از خدمات خاص به زمان بیشتری نیاز خواهد داشت.
پ.ن:
الان ۲ هفته‌ست که بخش بزرگی از خدمات ۳ تا بانک اصلی کشور قطعه. تو این هیر و ویر شایعه هم زیاد شده؛ یه عده میگن هک شدن، یه عده هم میگن کار خودشونه تا جلوی بیرون کشیدن پول مردم رو برای خرید طلا و دلار بگیرن.
مثل همیشه هم هیچکس راستش رو نمیگه؛ اول میان کلاً تکذیب می‌کنن، بعد میگن آره حمله شده ولی اطلاعاتی دزدیده نشده، آخر سر هم که همه‌چی به باد میره هیچ‌کس گردن نمی‌گیره و پاسخگو نیست! تو این بلبشو، حالا بماند که بانک‌ها یواشکی جلوی وام‌ها رو هم بستن و طبق گفته بعضی خبرگزاری‌ها، سود وام‌ها رو از ۲۳ درصد کشیدن بالا و کردن ۳۵ تا ۴۰ درصد!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/iaghapour/2721" target="_blank">📅 16:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2719">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDZ0XDdT1gm7JM8rofXgIwlXvLJYWd06xGYLtc5_LRzpltw4Nq_6NvtBri9VVBFJe1P3q2xTRmF1UqJlpugQ7uRiuXRUmQBiqJElRg9SJPHiZvETbWRJ3HJl4G1rzjnb2S1DAOHvEntnBzIjaccf2Lp99zT09at35A11h9B_2Y34-rmQDF_ywyWXH25fglhH5RQToHX9f8THkSSLLHkwgwg-agTnHCRY728ZGiIB8ULH2gwWri1hLKLnexBug9axnRfDh082X9x05L1blfFuIYJQf3xuogVSYYc0-Yvpj1xYZ4niSnrSsTdXgeyJawKLdQF5zQypARPOYekZXnEuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های سرور ایران فقط با یک کلیک
😎
🔹
یکی از مشکلاتی که این روزها خیلی‌ها باهاش درگیرن، محدودیت‌های شدید و اصطلاحاً اینترانت شدن سرورهای ایرانه که باعث میشه ارتباط ما با خارج مسدود بشه تو این ویدیو قراره بهتون یاد بدم چطوری فقط با اجرای یه اسکریپت ساده، تمام این محدودیت‌های شبکه رو روی سرور ایران برطرف کنید و هرچیزی که دوست داشتید دانلود کنید یا نصب کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ایران
#ملی
#محدودیت
#سرور
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/iaghapour/2719" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2718">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYJnJihyuO28_nRpZD3e5BXDIxwX8bs6eVrzMMqScQXwhqkaq9E0DOUIlNDuokw1AHkV0meaT0ZElGKcKniWuUvQADjfzjIzVyZSeZayfIztPcilKvnycJpITqTg31gH5xpXcZnWe2tXQrR3NLHgWh9fH4Vz5tv5t-KnPsqYR5kEJN7dXWe2A1eHjWqVFLp9l6FEzpgndfyYBMF0dBpbBnfj7GxLWKGMZpQxV68Ob01e0kDNJwM-KkrjpRqGtRQL_v5sFe1ic7ySfbST3U3aYkVHn2Z0rccXLUX7jFPk870i76W_5XYh6un25QYYRNnrLjwIW9DnBVO110WQSIhQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔌
قطعی برق و سریال تکراری خاموشی اینترنت و شبکه موبایل!
🔸
با شروع فصل تابستان و آغاز خاموشی‌های برق، مشکل همیشگی از دسترس خارج شدن شبکه موبایل و اینترنت دوباره گریبان‌گیر کاربران شده است. گزارش‌ها نشان می‌دهد تنها چند دقیقه پس از رفتن برق، دکل‌های مخابراتی (BTS) خاموش شده و ارتباطات در مناطق وسیعی مختل می‌شود.
🔹
دلیل اصلی این اتفاق، فرسودگی و خرابی باتری‌های پشتیبان این دکل‌هاست که توان روشن نگه داشتن تجهیزات را حتی برای زمان کوتاهی ندارند. این قطعی‌ها نه تنها دسترسی ۸۸ درصد از کاربران به اینترنت موبایل را قطع می‌کند، بلکه باعث از کار افتادن خودپردازها، دستگاه‌های کارت‌خوان، دوربین‌های ترافیکی و سایر خدمات حیاتی و شهری می‌شود./شبکه‌چی
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/iaghapour/2718" target="_blank">📅 12:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2717">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBCjuoGY8DTj7HHL5zN0lNv5sLr2qlsuSo2OD5cIjJ_ohd_xqzzBf5lDNm6YFp6smacICE8pWF51dIfxi3DpwmvqbOWmBSQPYu6u39HIvrbSRvOO8PnJweR8_HBdHdVKTKHKBmcgGDZ3qw-d0RuWg2zfyDfscIgKURd3_cRsKclCbQSgFreECpZlkcB04_23KTRW85u0M6fl27lyWyUm50zjJjQhpbRhVGYxJRtK8t7iLccUPtGLvrKtka8nFRNDCDozqXjQq4OV3r1hknJbhDrXcIhbBTX5_Q8CDRpTw5KAauEg_KZefk-qAmyNNmaqyqri_Iagft9Gj334EZBsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی اسکریپت ساده EZxray Direct Server
یک اسکریپت کاملاً خودکار که سرور شما را به یک مرکز Xray با پشتیبانی از ۱۲ پروتکل مختلف و ۲۰ پورت متنوع تبدیل می‌کند؛ آن هم بدون نیاز به هیچ‌گونه تنظیمات دستی یا دانش فنی!
🔹
ویژگی‌های کلیدی اسکریپت EZxray:
🔸
تولید همزمان ۱۲ کانفیگ
🔸
مدیریت بکاپ
🔸
مانیتورینگ لحظه‌ای
🔸
رابط بصری جذاب
🔗
اطلاعات بیشتر در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/iaghapour/2717" target="_blank">📅 17:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2711">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7T5eoK4Tvz7d3w-bjHR6ZqJ2fHRbBTMdz83mU540L6oCwHqrwQb_NtNLUgZ_8vbhaxSVpycsvwlrbAEYtA2Ve1vOrOhAe_mT_i-OnFljoZJvTGi_vGrMScHXN8YolpSRS-PwWZcdawfm4eqcJIJykEAl0orjaJBmmV9e6Vnb9hcw59EEdx57bl_vgQ5zMmn2g2y5bVRn844yBSDejC52QQJ5OaGdjk1KMCbvsOfpQ7mnUjVsHm2MMv0oPRc81PYBjg9BA0Wld2tjY16ZtPYE8LmhkfX_ELcltBUGCsGdgMqO-OaQm_MpOmiM93eAVXKRuhhJMZ4LVRa3c5BsHu4YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPzHTsMurmLHgEbrVVmAaMrfUZ3RZNAjPTYFOIAz9wqmWUkVpoOsFi5-7r6wi4kj29OcaL6-RZBIx_RQ9gSWaxvE0t_Exja7yMvWSAqU1TcSAZLW4IaP0EVQvbN-uSZMI5Zv7PfkF7nlzu-sDy5AJSOP_0PiGbd3CF-SoG5oUAsjWR-2KfmX2TVUD7srfm4YbI5VdpMMIjx1y2n6tdoAX1oNl8naSP986hHDA4a7NjFdyuQi8ZydkAA5acW8x4RXfGQrkr92kSspuR7E9sKQH50Hbz7vr6tNiKSgTWapGB7LedsUDFf4PuRUEOZIBxfIa_sPWgZJ9QY6IbhW6Xikvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ys-e4Z6qpD4NrjwrsFf8k8tN2TxeRTEbD_nDCF0W006ma8pgiMhs3CPvS209WzrHIFDfFv2Za0QxPVPvL5tfZFIu8L4ViNZliSC4-9-L0v4E2TkayAQvqYTjjVAy2dKesNCkzhVTNobsmP20mvyu8Y7SjZ0Tz9gglM3-hNOMrIZs_vVvXvIEeyUL6sX9MPFwZksjnJL1hEcEIT8vgnjfRGDlq8536YdSRBDbCIu976YmkNTM41E5S94vvI95eQkH0IP7S1o0WKHbwQALOZkra9s3MSd-BmNlgsBfeCE6Yg1daQXbYTbPqxtUSCuD89K6PBBQ5B13y4WHvuifR22Igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCSvx7RnlsbZsf6tZU6aPmNgdS3gS5sek5fV16jEp1MiCDlTka0SVgkSxNQ-KTmPU3mIhy2EefGhswYeiFTKKk1wHu8Q-eLMRZ5MR7YLZoyBcsbI5t7eO37CBjOYo_C4NtJZZPMHWKE1M7W7hDd8p0Nz0I_ARv1yMaUVdi8xjFFL25Rci-JVbVZ_qAuSBEarOcz_D0NDB2I_8Kqw2UTPabwloWFkWGReh4KhPiSeiZ1_8nIzw-J2Eok1uVpKr_BKuAXXwr45PGT4YMZtOrZfx1V30iKqPVQZZ-WGtSTCtEhTNgv_tYNB2kntjqalNNMS-LYKuTAZZi4ZWzkUdUOeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUlx_E1g10byVtp7D3SLK5RYfcOrj8c2iB7vU_tdCEVaqTdYDjWLyQK24iPUPHn7-_pjIHJw499kL5FrE3L69ZloftkCkPDjekxn2cQIGE8Oc5FqLRnVVI-vsvjh_LtVTKTBDfad4sjCtgtwzJjpy8aPoEy9JRbB71HSbHRKYb-TxB9PwwTDe5u-6v2smzDDisjnz7cI96pWN1mZ98n0zSsgo72FcyQU9QgXvd035vlQTMifb4yqu95nPQcRd_LYJkGecFlOHi6fYm55be3r7twhkERbb8lAHuJY0OlfBsQwHSOMhxLWhlfpwnxjhyWrbZimrgS6Ko4n1vzYRjmrew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همراهان عزیز کانال
💚
همون‌طور که خودتون هم می‌دونید، پشت هر اسکریپت یا ابزاری که توی گیت‌هاب منتشر می‌شه و کار ما رو راه می‌ندازه، پشتش توسعه‌دهنده‌هایی هست که بدون چشم‌داشت، دانششون رو رایگان در اختیار همه قرار می‌دن.
من به عنوان کسی که تو یوتیوب و تلگرام فعالیت دارم، همیشه وظیفه خودم دونستم که در حد توانم از این بچه‌های متخصص حمایت مالی (Donation) کنم؛ مخصوصاً اون عزیزانی که واسه اولین بار اسکریپت و ابزارهاشون رو در اختیار تیم ما قرار دادن. این کار اصلاً لطف نیست، بلکه یه وظیفه کوچیک در برابر زحمات اون‌هاست تا انگیزه داشته باشن مسیرشون رو ادامه بدن.
دم همه‌ی توسعه‌دهنده‌های خفن و کاردرست گرم
👌🏻
اگه ابزاری کارتون رو راه می‌ندازه، دمتون گرم که با یه تشکر، ستاره دادن تو گیت‌هاب یا حتی یه دونیشن کوچیک (در حد توان)، خستگی رو از تن این بچه‌ها درمیارید.
مخلص شما...</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/iaghapour/2711" target="_blank">📅 20:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2710">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxFgJzTZeTd6QrIP7rAP48_T3pBVC65XQYGUTKHPEDdP2_x4ABIQPzABYsPxTU6qPaGwtFBK9hHc4vi-h1r_GM_ivUKKzfPUzv2HaISm9YZ3wbr5LltKKZSga-NhutmyrR-WDwAi4ceSrsUJM4mMamhfHwAyCyLUSaGr8SU3yIMBHeibqBKA7OQC5W0K49GIglsOzMORMK7K4RHSEQv3rYj8OehiZLrIbjzSCsUPHgJoA7D2bRtchsj0jmXQm8Om5ALxSCNkyUt9UBXFhIatY3X8rCEm3BkWsabkUTDRkJ59BL7q44i_aRbTLq3WSD6ZMZtgdkSrNMwydSfoFZ8gFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Defyx VPN؛ دسترسی آزاد و هوشمند به اینترنت
🔹
برنامه Defyx یک VPN مدرن، امن و متن‌باز است که با رابط کاربری بسیار ساده خود، امکان اتصال سریع (تنها با یک لمس) و حفاظت از حریم خصوصی را فراهم می‌کند. این اپلیکیشن با بهره‌گیری از هسته قدرتمند DXcore، از پروتکل‌های معروفی مثل Xray، Warp، Psiphon و Outline پشتیبانی کرده و بدون نیاز به هیچ‌گونه تنظیمات پیچیده، اتصالی هوشمند به همراه ابزار داخلی تست سرعت ارائه می‌دهد.
🔻
بر اساس اطلاعات منتشر شده، نسخه جدید این برنامه هم‌اکنون برای تمامی پلتفرم‌ها از جمله اندروید، ویندوز، iOS، مک و لینوکس در دسترس کاربران قرار گرفته است.
🔗
دانلود آخرین نسخه از گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/iaghapour/2710" target="_blank">📅 18:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2708">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2lPp4xXTwv9vR2-A2Qrwdr8Zix_swu-Rla4BolKG28zLh5AKWnR8dpDQU0gJaMzBZmDPraDcOdsyUYfubIAwcGSeUceLXS5D2lHNBXjdMRDCLwqNUFh2r5TBAowoSaDjDAWlF0i6JJh63hfYP--p9KMEGleLQuugR5zmpnJzOhuR3imREcdTh1fmaLxXf4r2rWcefTjd8ulm0Igk27WrIwbivylObhKX9Zugw-q8HJx7lqt0JH9DD976mNOtsHXr5_KYfF3xHqoTtvPYDe1XAFVMlo2VnYyAoyh-bzMc7xjVQg9PMyenidiQe5_RDdKdOuUoscJAf1XbWnlJ5r-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صرافی کوینکس ارائه خدمات به کاربران ایرانی را رسماً متوقف کرد!
🔹
صرافی بین‌المللی کوینکس (CoinEx) با انتشار بیانیه‌ای رسمی، به دلیل پایبندی به مقررات جهانی مبارزه با پولشویی و در پی گزارش وال‌استریت ژورنال، نام ایران را در کنار کشورهایی مثل آمریکا، بریتانیا، کانادا و چین در لیست مناطق تحت محدودیت کامل قرار داد. در حال حاضر تلاش برای ورود با آی‌پی ایران مسدود شده و حتی در بسیاری از موارد استفاده از VPN نیز کارساز نیست و کاربران با خطای عدم دسترسی مواجه می‌شوند.
🔻
اطلاعیه مهم برای برداشت دارایی‌ها:
کاربران ایرانی حداکثر تا
۲۵ سپتامبر (۳ مهر ۱۴۰۵)
فرصت دارند تا اقدامات لازم را انجام داده و دارایی‌های خود را خارج کنند. در این دوره انتقالی، حساب‌های احراز هویت‌شده (KYC) فقط امکان برداشت خواهند داشت. در بازار اسپات تنها امکان فروش (بدون امکان خرید) و در بخش فیوچرز تنها امکان بستن پوزیشن‌های باز وجود دارد و باز کردن پوزیشن جدید ممنوع است. همچنین اگر وام فعالی دارید، باید هرچه سریع‌تر نسبت به تسویه کامل آن اقدام کنید، چرا که پس از تاریخ ذکر شده احتمال اعمال محدودیت‌های بیشتر وجود دارد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/iaghapour/2708" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2707">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQoFwNyNu_HT2njaAyz7mPxE91NJKsPl84zk6MSswpXBoCQYvK8kIT-hSlPQCQCXnGSXqbydvFAoj4EvGVTcrqV6EEBxbvvvZgKtA__v2NQIzqITods2z3tGxrDhRzmbzE9h1iqFfxINMY4jP3AVa_dlJMUP6Rti1rlafbtYqxokXZlSDXoX8hsPmGXpoEGbUG08XmfCSTj4PF0xoyfYAYu5fy15Q-J6a41dmu2J-5H0VeDG2JDhRi22eFep7dpkx8dNTyDpMUbBKx0fqVjdUgxXcjUK3zCt-dfrIspE_T5Wro5GI3Wtqki6Cqu9HVzTY_NeQCtooQhrkcCNQ8SxDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بر اساس گمانه‌زنی‌ها، انتظار می‌رود بازی مورد انتظار
GTA 6
با قیمت پایه ۸۰ دلار (معادل تقریبی ۱۳.۵ میلیون تومان) برای نسخه استاندارد روانه بازار شود. همچنین، خریداران برای تهیه نسخه کامل‌تر یعنی «آلتیمیت ادیشن» (Ultimate Edition) احتمالاً باید مبلغی حدود ۱۰۰ دلار (تقریباً ۱۶.۵ میلیون تومان) پرداخت کنند.
خوش به حال اونایی که توانایی مالی خرید دارن. )</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/iaghapour/2707" target="_blank">📅 19:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2705">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">domains List -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.5 MB</div>
</div>
<a href="https://t.me/iaghapour/2705" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دامنه ها برای به ویدیو بالا
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/iaghapour/2705" target="_blank">📅 19:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bexqcFRBx8xUTaNI0NcZkBAIUIVuA1_kX25mjTJrLdx06hh_Bd3kRYEWW8ryVtMybvfQeSKcEpeIKKAcjUCkUAHQHBC4U3M05ZCTa2okWMhNwKIybGkaH6Cs2dhjTWTNP_u_mXq92F8bNWaSLCi1c0dASgOdB5KlknXAlL3Upi1jUqMc499FAf_ntLr2Z4mZ_tlbDRa2Gj8IpA_8e5d-PIuyEKRwp577wgSUMdAu7VwI6M1kyQDHJjqfdwWVOVxIhwpHDSFen3z3OiiVwFQuqX0NPNgSrWy1uf7P9XhJaDcU3jyhMJIBEuhbpmPCvx-TMpsFHAN9NjzqtbYj6PPLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پروتکل ریلیتی رو دوباره زنده کن!
🔥
(+ اسکنر پیشرفته)
🔹
خیلی‌ها فکر می‌کنن با محدودیت‌های اخیر، دوران پروتکل ریلیتی (Reality) دیگه تموم شده و کانفیگ‌هاش از کار افتادن؛ تو این ویدیو قراره با هم یاد بگیریم چطوری پروتکل ریلیتی رو دوباره با بالاترین سرعت ممکن زنده کنیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ریلیتی
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/iaghapour/2704" target="_blank">📅 17:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXd6QsdrQ6GPsZ9js-SKe9N_8xm8rMXji9K_8_o-wFd_eHVPG2zt3oeqqv-Lah80gxY2l415fetjOnRbQB6dDVDlfoQ9udThfIBw1CD9R7PdSygGy4T5PDWj1PiAWuRGfZ-ZFyNz0-NsUnkd_lcO5T1YGhXonlQN7DDcuR6i-xVRb8OQYkHabi_f2zfxcUBOHuf6rHSRL34pRrU3SJIlhsrP0hvvVsduT_pjxs3kK_PWByTqrLbEM_JGcC8_XBIvLHTJVAVB4vzSVHt9mH4CPnl4Q0287bWjn4cvd7f_031Ly3X4t2IHQmyoYoiNku_vXaPtNiDGW4wPk5H0C0pDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
خداحافظی با کپچا؛ کلودفلر و غول‌های فناوری به دنبال استاندارد جدید
🔸
شرکت کلودفلر با همکاری توسعه‌دهندگان کروم، اج، فایرفاکس و شاپیفای در حال ساخت سیستم جدیدی به نام PACT است تا برای همیشه به دردسرهای کپچا (CAPTCHA) و اثبات ربات نبودن پایان دهد. ایده این سیستم بسیار هوشمندانه است؛ وب‌سایت‌های معتبر پس از یک بار تایید انسان بودن شما، یک توکن کاملاً ناشناس صادر می‌کنند. از آن پس، مرورگر شما همین توکن را به عنوان «برگه عبور» به سایت‌های دیگر نشان می‌دهد تا بدون فاش شدن هویت یا تاریخچه وب‌گردی‌تان، ثابت کند که شما یک انسان واقعی هستید.
🔹
مدیرعامل کلودفلر می‌گوید در حال حاضر بیش از ۵۶ درصد از کل ترافیک اینترنت را ربات‌ها و ابزارهای هوش مصنوعی تشکیل می‌دهند و ابزارهای امنیتی قدیمی دیگر پاسخگو نیستند. با اجرای این پروتکل جدید، هم حریم خصوصی کاربران به طور کامل حفظ می‌شود و هم دیگر نیازی به حل کردن پازل‌های آزاردهنده و کلیک روی عکسِ چراغ‌راهنمایی نخواهد بود! / دیجیاتو
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/iaghapour/2703" target="_blank">📅 17:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2701">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs_twm6skEShZny_5YDYL5nQlby2DOIRjeFztwxuXWZJE0a1sxgCIy5mE3RtAbErP9P8DzGEYZQ-4Wqxo-Hl9CNA9PjhELk2KUKzcSS5Co7IUFOxpZ0l9e1BUjJW56xUXpliAo0PCMiqVfd2KXAG4D835PGlXq3DMq-487JpeqRMLnAFAxhHJoMlZRh10eiTZz-9J_B2aO2MhspwiTrM96EGbmEWfvt-gchpKjELCCyE_IHkkdTqsLD_QeJ83_RjKnezlPByBIqCcsXowzimk5GCInYRPwFTDCkUUeDGTIJC2KaFa_ggI4yrM9omVNG76oShaH-djzzuQWt3SELdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سقوط آزاد پلتفرم‌های داخلی و رکوردشکنی هشتگ تخفیف پس از وصل شدن اینترنت
🔸
با بهبود نسبی وضعیت اینترنت، کاربران به سرعت در حال ترک پلتفرم‌های بومی و بازگشت به شبکه‌های جهانی هستند. آمارها نشان می‌دهد فعالیت گروه‌ها در پیام‌رسان «بله» ۸۱ درصد سقوط کرده و ۲۷ درصد آن‌ها کاملاً تعطیل شده‌اند. رشد خیره‌کننده این پلتفرم‌ها در دوران قطعی، صرفاً از روی ناچاری بوده و حالا مردم کانال‌های داخلی را فقط به عنوان یک پایگاه پشتیبان برای قطعی‌های احتمالی بعدی نگه داشته‌اند.
🔹
در همین حال، کسب‌وکارهای آنلاینی که فروش طلایی خود را در دوران محدودیت‌ها از دست دادند، برای جبران خسارت‌های سنگین به تخفیف‌های گسترده روی آورده‌اند؛ به طوری که استفاده از هشتگ «تخفیف» ۱۲۰ درصد جهش داشته است. این آمارها ثابت می‌کند پلتفرم‌های بومی برخلاف ادعاها، هیچ جایگاهی برای جبران ضرر اقتصاد و کسب‌وکارها نداشته‌اند.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/iaghapour/2701" target="_blank">📅 20:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2698">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
حمله سایبری به شبکه بانکی
!
شرکت خدمات انفورماتیک با انتشار اطلاعیه‌ای، دلیل اختلالات گسترده در کارت‌های بانکی را تشریح کرد.
🔹
جزئیات این اختلال بانکی:
🔸
دلیل اصلی قطعی:
وقوع حملات سایبری به سامانه‌های کارت‌محور بانک‌های ملی، صادرات و تجارت.
🔸
اقدام پیشگیرانه:
این شرکت اعلام کرده برای جلوگیری از دسترسی غیرمجاز هکرها و حفظ امنیت داده‌ها و موجودی مشتریان، خدمات مبتنی بر کارت را موقتاً و به‌صورت عمدی از دسترس خارج کرده است.
🔸
گستردگی مشکل:
با وجود اینکه در اطلاعیه رسمی فقط نام ۳ بانک آمده است، اما بررسی‌ها و گزارش‌های مردمی نشان می‌دهد قطعی‌ها گسترده‌تر بوده و بانک‌های دیگری مثل «ملت» هم درگیر این اختلال شده‌اند.
🔸
وضعیت فعلی:
تیم‌های فنی و متخصصان امنیت سایبری در حال کار روی شبکه هستند تا این مشکل برطرف شده و خدمات بانکی به حالت عادی برگردد.
پ.ن: بابا ولش کنید‍! بعد 2 هفته اختلال این حرفا چیه میزنید؟ مثل قبل همون روند تکذیب رو جلو برید. بگید که ما هک نشدیم و قطعه سخت افزاری سوخته!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/iaghapour/2698" target="_blank">📅 19:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2697">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLrTbhcDfRnCkC1LZJaDCvwNX-94JfnElpTpGMoBeZIHtGCI8dOMUanVOj3kGFPJYHAnu5BZCXOZE5pYv19W_2F6KMNvOVlABrD7sr-uOGi5rjrWb_shKI0VdmImnOESc5_lSaveS04PyziJ3_XQu5jmYRi_bfO15ANlqSwoy_gULrXsuYAWUFiCFqYGJInIFEMZg0Do5SXNFsabFVLUAoM_cql0b688O8kcmY5j6zxLb2nDZLzfUHunJxJoY-AIvskwIxB5LW1m4JNnAFY8naOI99KCb35DzPaiM-yEpx5PT06cOt6jqrfxdl6qc7BITCDE7iDLg5b78DyqtAfgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
چرا فعال نبودن IPv6 در ایران یک بحران است؟
در حالی که دنیا به سمت استفاده کامل از IPv6 رفته، اتکای شبکه ما به ظرفیت محدود IPv4 چه مشکلاتی ایجاد کرده است؟
🔹
پیامدهای اصلی این عقب‌ماندگی:
🔸
کابوس CGNAT:
به دلیل کمبود IP، اپراتورها هزاران کاربر را پشت یک IP مشترک مخفی می‌کنند؛ یعنی شما عملاً هویت مستقلی در اینترنت ندارید.
🔸
دردسر همیشگی کپچا:
چون درخواست‌های هزاران نفر با یک IP ارسال می‌شود، سایت‌های خارجی شما را ربات تشخیص داده و محدود می‌کنند.
🔸
مشکلات گیمرها:
گیر افتادن در لایه‌های NAT باعث خطای Strict NAT، افت پینگ و قطعی در بازی‌های آنلاین می‌شود.
🔸
اختلال در دسترسی‌ها:
بدون IP مستقل، راه‌اندازی شبکه‌های خصوصی و دسترسی از راه دور به دوربین‌ها و تجهیزات هوشمند بسیار دشوار است.
🔸
افت کیفیت شبکه:
بار سنگین سیستم‌های تبدیل آدرس (NAT) روی سرورها، باعث تاخیر در مسیریابی و کاهش پایداری اینترنت می‌شود.
پ.ن:
دنیا با میلیاردها آدرس مستقل به دنبال سرعت و پایداری است، اما ما هنوز برای یک ارتباط ساده، درگیر پیدا کردن یک IP تمیز و عبور از لایه‌های NAT اپراتورها هستیم!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/iaghapour/2697" target="_blank">📅 22:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2696">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8UdYWcvcxWqe2LRX-o1ic4mJE_jTtVbG9YKRPGh72CI05RO1M-U1YQSxLMJiSn8_l-apyj7cvSbhBPLHYlq58ug4FUid60_XF3YL7Jfks3ev-LRHVv2ultCxnnun7LFYZ4hEShoMEEuMFDsB6p-qrtvUGa8cMvn2ZEaA12YHGgl7mbEfK45XKaH_DjRCsJmw2sz051O5e5-gZvUqhCHwjEsBTTQiwXgpaaxra4twlL1_6EP-UoAUGcsg2jZGxsHKnZt4kM0D_S1v-c37qcNMW6tOm3yHYJcHoPsTGEJmrXu0hq7qsgoF7HLa2X-fOiKHJqIST8FIIxINjPpBGfa0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بحران خاموش در دیتاسنترها؛ اینترنت برگشته، اما نه برای کسب‌وکارها!
پس از گذشت چند روز از قطعی گسترده و مسدود شدن کامل ارتباط با اینترنت بین‌الملل در سراسر کشور، اکنون در حالی که اینترنت کاربران خانگی و اپراتورهای موبایل تا حدودی به حالت عادی بازگشته، اما گزارش‌ها حاکی از آن است که دسترسی بسیاری از دیتاسنترهای داخلی به اینترنت جهانی همچنان قطع یا دچار اختلال شدید است.
این دسترسیِ قطره‌چکانی و عدم اتصال دیتاسنترها، پیامدهای مخرب و گسترده‌ای برای زیرساخت‌های شبکه و کسب‌وکارها به همراه داشته است:
🔸
فلج شدن سرویس‌های آنلاین:
بسیاری از استارتاپ‌ها، پلتفرم‌های خدماتی و توسعه‌دهندگانی که برای کارکرد صحیح نرم‌افزارهای خود به APIها، کلادها و منابع بین‌المللی وابسته‌اند، با اختلال جدی مواجه شده‌اند.
🔸
خسارت‌های پنهان و سنگین:
وصل شدن اینترنت گوشی‌ها تنها ظاهر ماجرا را عادی جلوه می‌دهد؛ در حالی که شریان حیاتی بسیاری از کسب‌وکارهای دیجیتال در دیتاسنترها مسدود مانده و خسارت‌های مالی و فنی جبران‌ناپذیری در حال رقم خوردن است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/iaghapour/2696" target="_blank">📅 19:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/iaghapour/2694" target="_blank">📅 21:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2693">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoLXhMqhkG2H7RS3yQ-VRVbkwzAsmF9BPVOKDby_W_yFDTANCawztFXD-2cl0PiGHYSaSJDdBnfsejAKzhXyHekfuZLLH88fbHf62V4gv9yO5CYO9fraOQFezILuy7JaAkxYnxQ0sDmbs2LNrrxcu4XLE8xcrpQmcWIKpRSr2x3-0QtjBDHxJxZPW-kSTWHJ1sAYFjYAAKiaNQlx7_wVgvfFKkEgPYMG-EHc-ocBVP8HIXwObzXeoquEnhoBvUpH9HyYqSP2w7ILg4HoFV5GCNubOeyeBmwbW2AumMwN1i_-zHbnRf_R-SArMj5OcHpJOfrUmGuTlnnr5pSyOZ3EXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند.
در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس /
ircf
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/iaghapour/2693" target="_blank">📅 21:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2691">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDVTf_y0jbwlsdmUOA-yJuz1qnkqeGzKYs7GGfANtzdP3fooPJY4HKN-9UV6MunmdO0Tu8pZcIcIYWgqm9sxUPt9YaemVxb-UUbfkFMdQb-ol90tPc5Nvfr0PZLgE3wGX_z2vBsmlsj0pRZDs2uTkzqLw0MgIJ19_zoN2xhgsQ3Qb2sEWp4i9bxCCewRt5ClCQUuFuSOlWLzuBLHatWELHKO1016mI_wfL7kPWmcEr3MBq58PHR9Wu8-5S5SZ0_qONbZ9_fjGMWjc8GckG1ezlKOtzRfArMB5ljPbdWBs0KYiLDG7y5BEyc7g3g7drWMjpDyzyHNVQB6zNabGShb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش 4 روش تانل پیشرفته و مقاوم در برابر فیلترینگ
🔹
تو این ویدیو قراره با هم ۴ تا از بهترین روش‌های تانل زدن رو بررسی کنیم و یاد بگیریم چطوری تانل‌هایی بسازیم که در برابر فیلترینگ پایداری خودشون رو حفظ کنن.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/iaghapour/2691" target="_blank">📅 18:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2690">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
دوستان عزیز،
ربات «تماس با ما»
چون نسخه رایگانه، به محدودیت ۵ هزار پیام در ماه رسیده و رفته رو حالت تعمیر!
اگه تنظیماتش بر اساس تایم‌زون باشه، اول ماه جدید یعنی 2 روز دیگه خودبه‌خود درست میشه؛ وگرنه به ناچار نسخه پرو رو می‌خرم تا دوباره در دسترس قرار بگیره.
🥸</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/iaghapour/2690" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2689">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭕️
آموزش تانل بین سرور ایران و خارج (۲ روش سبک و سریع)
😍
🔹
تو این ویدیو قراره با هم دو تا از ساده و سبک‌ترین روش‌های تانل زدن بین سرور ایران و خارج رو یاد بگیریم. اگه برای ساخت فیلترشکن شخصی‌تون دنبال یه راه ساده و بدون دردسر برای اتصال سرورها هستید، این آموزش…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/iaghapour/2689" target="_blank">📅 16:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌐
مدیرعامل سروش‌پلاس: فیلترینگ و قطعی اینترنت به ضرر ماست!
امین شریفی، مدیرعامل سروش‌پلاس در نشست گزارش عملکرد سال ۱۴۰۴ اعلام کرد که قطعی اینترنت و اعمال فیلترینگ نه‌تنها به رشد پلتفرم‌های داخلی کمکی نمی‌کند، بلکه نتیجه‌ای جز عصبانیت و لج کاربران ندارد.
🔹
چکیده مهم‌ترین آمارهای گزارش سالانه سروش‌پلاس:
🔸
ریزش کاربران پس از رفع محدودیت‌ها:
با آزاد شدن دسترسی به سایر پیام‌رسان‌ها، سروش‌پلاس با افت ۱۰ تا ۱۵ درصدی در تعداد کاربر و کاهش ۱۰ تا ۳۰ درصدی در شاخص‌های فعالیت مواجه شده است.
🔸
وضعیت کسب‌وکارها:
آمارها نشان می‌دهد حدود ۷۰ درصد از فعالیت کانال‌های فروشگاهی، آموزشی و تولید محتوا که در دوره محدودیت‌ها ایجاد شده بودند، همچنان در این پلتفرم ادامه دارد.
🔸
رشد آمار کاربران و پیام‌ها:
تعداد کل کاربران ثبت‌نامی این پیام‌رسان از مرز ۵۲ میلیون نفر عبور کرده است که از این تعداد حدود ۲۰ میلیون نفر کاربر فعال ماهانه هستند. همچنین در سال ۱۴۰۴ بیش از ۳۰ میلیارد پیام توسط کاربران جابه‌جا شده که ۷۶ درصد از آن‌ها مربوط به چت‌های شخصی بوده است.
🔸
امکانات و تغییرات جدید:
رونمایی از مدل اشتراکی «حساب پرو» (با قابلیت‌هایی مثل نشان ویژه و حذف تبلیغات)، توسعه تنظیمات حریم خصوصی و همچنین افزایش جایگاه‌های تبلیغاتی پلتفرم از ۳ به ۱۳ مورد، از اقدامات مهم این سال بوده است.
🔻
پ.ن: من داشتم میخوندم خندم گرفت این چطوری داشت میگفت خندش نگرفت؟
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/iaghapour/2687" target="_blank">📅 19:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN5sRo4cTZxlBkz6p4o1mejlEComa0PsHKafjmU0S08Yb4SzFhEa5mejIOUeh8VGwugkhS2LGr3qTUu1wZT4arzlG9PSnf5QsAn2pnb3QqZPSCubVUCVNHrprSVoykTTP-0gE2lGeTPWshI5fNCOmHFTAetkHn4da6J7ECNF63SjwvkpWt0AArO0F2WBxDsiln946H_lQnduTwDmYw0S2V-_dtpsSF78kWh6FGG2EkZ1N58AV0zv9THVNF-qS78Gg-VRwYAG-wZiBYP8rEYoC7sZzvVXiea_XLUeppLzkWpRY0ewa0DN7zv9spJjU9XvZAF3M04fHuQqs67zjRQMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر (NovaProxy v3)
🔹
تو این ویدیو قراره یه روش فوق‌العاده برای ساخت یه فیلترشکن کاملاً رایگان و پرسرعت رو با هم یاد بگیریم. این بار رفتیم سراغ ورکر کلودفلر و قراره از اسکریپت قدرتمند NovaProxy v3 استفاده کنیم. تو این ورژن حل مشکل تماس صوتی و تصویری رو هم آموزش دادیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ورکر
#novaproxy
#worker
#کلودفلر
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/iaghapour/2685" target="_blank">📅 19:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2684">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5uj7v58V65PEyMgaCwe-Rq_V-UZUxQQOkjbnHgOnmPG6eXA78zZLNyCif2-EpfQe_WZ9dyNgeNuEFyNskZcrIPaNlTYZOdAoEgEHGoh2rlNlDxYqI6lCdrjTJY_pjAqFD7GQxI8vk0CiVIk1fdotzibE9JfTsuvaZFB-wNrXiTCFZ70eY0ZlrnrcPCPtOUzf3W-ls3OI_W5tbWOBkd6q1r1ibc_rzGtn6t-4w96pBlwg8LwZc_my5snXOuQ6iv2GIwfXLVzCh4OGrdCgwGigZ0mm27r2efNVTP1gU2GwtX4OXWgrvzL4MVwDRByl2B56-QdMSsjd9l-jB9oL9MxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
افشای ۱۲۴ میلیون پسورد و ۵۶ میلیون ایمیل؛ آیا اطلاعات شما هم لو رفته؟
پایگاه داده سرویس معروف Have I Been Pwned به‌تازگی آپدیت شده و آمار نگران‌کننده‌ای را منتشر کرده است. این بار هکرها مستقیماً به سراغ کامپیوترها و دستگاه‌های شخصی کاربران رفته‌اند و بدون اینکه کسی متوجه شود، حجم عظیمی از داده‌های حساس را سرقت کرده‌اند!
🔹
نکات مهم این نشت اطلاعاتی:
🔸
منبع سرقت:
این اطلاعات نتیجه هک شدن یک سایت خاص نیست؛ بلکه بدافزارهای مخرب، پنهانی روی سیستم‌ها (مخصوصاً ویندوز) نشسته‌اند و پسوردهای ذخیره‌شده، کوکی‌ها و داده‌های مرورگر را دزدیده‌اند.
🔸
خطر پنهان:
از آنجا که بسیاری از کاربران اصلاً متوجه آلوده شدن دستگاه خود نمی‌شوند، این سرقت اطلاعات می‌تواند تا مدت‌ها بدون هیچ ردپایی ادامه داشته باشد.
🔸
اقدام فوری:
همین حالا به وب‌سایت
Have I Been Pwned
سر بزنید و ایمیل خود را جستجو کنید.
🔸
راه‌حل‌های امنیتی:
اگر اطلاعاتتان لو رفته بود، سریعاً رمزهای عبور خود را تغییر دهید. همچنین برای جلوگیری از نفوذ، حتماً تایید دومرحله‌ای (2FA) را برای حساب‌های مهم خود فعال کنید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/iaghapour/2684" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2682">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💰
مدیرعامل همراه اول: قیمت فعلی اینترنت با قیمت واقعی آن هیچ سنخیتی ندارد!
مهدی اخوان، مدیرعامل همراه اول، در مجمع عمومی سالانه این اپراتور با گلایه از تعرفه‌های فعلی اعلام کرد که هزینه‌های سرمایه‌گذاری ارزی آن‌ها کاملاً مشابه اپراتورهای منطقه است، اما قیمت هر گیگابایت اینترنت در ایران بسیار پایین‌تر از آن کشورهاست.
پ.ن:
جناب مدیرعامل! اتفاقاً تو این مملکت خیلی چیزها هست که هیچ سنخیتی با هم ندارن؛ از کیفیت اینترنت شما و چیزی که واقعاً به دست ما می‌رسه بگیر تا درآمد بالای مردم منطقه و حقوق‌های پایین ما! از همه مهم‌تر، بین زندگی و رفاه شما و واقعیتِ زندگی مردم هیچ سنخیتی نیست!
اگه واقعاً کار براتون نمی‌صرفه ما هم راضی به ضررتون نیستیم، کلاً درِ این اپراتورها رو تخته کنید و جرم‌انگاری استارلینک رو بردارید تا ببینیم تو یه بازار آزاد اصلاً می‌تونید باهاشون رقابت کنید یا نه! واقعیت اینه که سودهای کلان این اینترنت انحصاری (پرو) حسابی به دهنتون مزه کرده و حالا با گرون کردن‌های نجومی و پشت‌سرهم، به هر دری می‌زنید تا جیب مردم رو خالی‌تر کنید. وگرنه این چیزی که دارید به ما می‌فروشید اصلاً اسمش اینترنت نیست؛ هر وقت یه اینترنت واقعی و بدون فیلتر دست مردم دادید، اون‌وقت پولش رو هم بگیرید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/iaghapour/2682" target="_blank">📅 21:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2680">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4cLgKQmPZIH7DFV51A9xEZAOgmkh2-S-XS1MeuPXe-UuecitgW5RX02YLUM27eVQpbDlYrWxNRw9ml9lNCVrSwTuaJdgnBOAE2gaQVHMUugcEdMUNkD31ll640UqIBPD2j-YknHX9NbGyrx_AJmYL5xp144_IeUQFR0W1jTqxpFTtSJ8Lvt2GJGCCapUwTdTVE36YrmNXr5aElzl2aFeTjKoC6eGwlWkwWdITNRVm0TNoBmRliRsZWQcBHwyIAuZNJ_tqAgh0PX1bu2nm8CyR_RdsqCXZGU689mAHEXbhqiE1g6GKSZeZpBCVC8-_b6oNn2KGoZbp4dNOJFfrhaEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار خیلی مهم: خطر فریز شدن دارایی‌ها در صرافی‌های خارجی!
بچه‌ها، همونطور که تو تصویر می‌بینید، صرافی‌های خارجی یه اخطار خیلی جدی در مورد تراکنش با پلتفرم‌های تحریم‌شده توسط OFAC (دفتر کنترل دارایی‌های خارجی آمریکا) منتشر کردن.
⚠️
تو این هشدار صراحتاً اسم ۴ تا از صرافی‌های معروف ایرانی آورده شده:
🔹
نوبیتکس (Nobitex)
🔹
والکس (Wallex)
🔹
بیت‌پین (Bitpin)
🔹
رمزینکس (Ramzinex)
❌
مشکل چیه و چه خطری داره؟
این صرافی‌ها اعلام کردن که سیستم‌های ضد پولشویی (AML) به شدت تراکنش‌ها رو بررسی می‌کنن. اگه مستقیم با این پلتفرم‌های ایرانی تراکنشی داشته باشید، ممکنه حسابتون محدود بشه یا حتی کل دارایی‌هاتون رو فریز و مسدود کنن!
💡
حالا باید چیکار کنیم؟
به هیچ‌وجه انتقال مستقیم ارز بین صرافی‌های ایرانی و صرافی‌های خارجی انجام ندید. حتماً از کیف پول‌های شخصی (مثل تراست ولت، یا ولت‌های سخت‌افزاری) به عنوان واسطه استفاده کنید تا مشکلی برای سرمایه‌تون پیش نیاد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/iaghapour/2680" target="_blank">📅 16:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2678">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3Y_bbIkz_psLQb5bDoX0Es8JjqHHFkN9ot4vY0bC2uWep0BYhumZ-gb3jImLSjzAul1mETwepuv3Qofpyyv_xnLQIgSrKiHyq5X39fC8Ihx4hJG2_26sAApchEbZB6Pd3V4rnfFmTyCqyqJWhyXPFZXB7MdH5d6iPabYOBzt-kXmVnx2_esxTZE0X_evjPMaaLnKmtNLGI6ZpsptNVZIvgZgPayy1ZSp-RgtN3-W5V9re25ZDZVPJGN7MrLyvu7bq7SppTaU-SlCQktHbRtSXZ-lxEz8twMYW-tqvrMMDjFWkA5lzTE-ZHMKEmYgZI_cxip_Xt_ZAxquG3sTKdnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل بین سرور ایران و خارج (۲ روش سبک و سریع)
😍
🔹
تو این ویدیو قراره با هم دو تا از ساده و سبک‌ترین روش‌های تانل زدن بین سرور ایران و خارج رو یاد بگیریم. اگه برای ساخت فیلترشکن شخصی‌تون دنبال یه راه ساده و بدون دردسر برای اتصال سرورها هستید، این آموزش دقیقاً همون چیزیه که نیاز دارید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/iaghapour/2678" target="_blank">📅 19:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2677">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭕️
دسترسی مستقیم و بدون واسطه به اینترنت آزاد
🔹
کافی است آدرس subscription را در برنامه v2rayN/v2rayNG وارد کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
— نکات استفاده
👇🏻
۱. کانفیگ سرورلس برای اجرا نیاز به هسته Xray-core حداقل ورژن 26.6.1 دارد (حداقل v2rayNG v2.2.3)
۲. سرویسها و سایتهایی که ip آنها به طور کلی از سمت ایران بلاک شده با این روش مستقیم قابل دستیابی نیستند، همچنین از آنجایی که سرویسهای خارجی ip ایران را مشاهده میکنند، سرویسها و سایتهایی که ایران را تحریم کرده اند نیز با این روش مستقیم قابل دستیابی نیستند.
۳. در تنظیمات v2rayNG دقت کنید که Enable Hev TUN FEATURE فعال باشد و همچنین پورت پیشفرض 10808 را تغییر نداده باشید.
۴. از آپدیت بودن فایلهای جئو مطمئن شوید (قسمت Asset files در برنامه v2rayNG و قسمت Help-Check Update در برنامه v2rayN)
۵. برای تجربه بهتر پیشنهاد میشود IPv6 خود را فعال کنید (در تنظیمات v2rayNG تیک Enable IPv6 را بزنید و همچنین در صورتی که از اینترنت همراه استفاده میکنید باید IPv6 را در قسمت Access-Point گوشی خود فعال کنید)
۶. در اندروید برای عدم تداخل با (dns و sniffing) کانفیگ بهتر است Private DNS در تنظیمات اندروید و Use secure DNS در تنظیمات کروم خاموش باشد.
۷. از کانفیگها تست نگیرید، نتیجه‌ی تست ارتباطی با کار کردن یا کار نکردن این نوع کانفیگها ندارد.
🟢
به گفته یکی از بچه ها با روش زیر میتونیدمتصل بشید:
کاربر اگر فیک دی ان اس رو از تنظیمات برنامه روشن کنه سرویس هایی که آیپی ایران رو محدود و مسدود کردن مشکلش حل میشه و سایتا بالا میان.
⚠️
برای کارهای حساس از این روش استفاده نکنید!
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/iaghapour/2677" target="_blank">📅 12:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✍🏻
دوستان، در حال حاضر بیش از ۷ اسکریپت (شامل اسکریپت‌های تانل و روش‌های مستقیم و رایگان) رو در دست بررسی داریم. هر کدوم که بدون مشکل جواب بده رو توی یوتیوب معرفی می‌کنیم. اما مواردی رو که به هر دلیلی (مثل محدودیت‌های دیتاسنتر سرورهایی که استفاده میکنیم و...) نتونیم خودمون ازشون جواب بگیریم، داخل کانال تلگرام معرفی میکنیم تا شما بتونید تست کنید.
ممنون از حمایت همیشگی شما.
💚</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/iaghapour/2674" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">واقعاً باید درِ این بانک‌های مزخرف رو گل بگیرن! سالی ۳ بار یا هک می‌شید، یا اپلیکیشن بانک کار نمی‌کنه، یا اختلال دارید و هزارتا کوفت و زهر مار دیگه! آخه مگه می‌شه بانک این‌همه بی‌در و پیکر باشه؟
😒</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/iaghapour/2673" target="_blank">📅 20:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2671">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INHIH5nm82zJxRGr5zYJidQf-iJ_RcK0K8ourCAKUql1M37EWBpzCk3eM9363YYHzZ3taQsgrtJMnvgz8gn8U7Atr7mVdvWI_SRp4c_FrtoAuOMXnVI0ufYzKtMsb7FLcFGLjkAQKEb-oSTenCsxeJrbnct_QUT84s71mIZU4NANZchEsAqmHW7VmnomoobntOss5KwkMf9Hege8dOfqejBT_kCPRQtRzcMOdqvNF5e0vb_AN7teBioPoVpIqJx2jqV4NyFTRMEVOQJBjjAruMTC_zkU3l9TE1WC85VKLC2aktkszssaFa8yHpAGJCJokOEby0X-QEPNI5bfSfQjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
درخواست حمید رسایی و ۱۱۹ استاد برای انحلال «ستاد ویژه فضای مجازی»
بیش از ۱۲۰ تن از اساتید حوزه و دانشگاه، و چهره‌های سیاسی از جمله حمید رسایی در نامه‌ای به رئیس قوه قضائیه و فقهای شورای نگهبان، خواستار ابطال فوری مصوبه دولت برای تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی» شدند.
🔹
مهم‌ترین دلایل مخالفان:
🔸
تشکیل این ستاد ناقض جایگاه «شورای عالی فضای مجازی» به عنوان تنها نقطه کانونی سیاست‌گذاری است و یک ساختار موازی محسوب می‌شود.
🔸
به اعتقاد نویسندگان نامه، رئیس‌جمهور صلاحیت ایجاد نهادهای فراقوه‌ای با کارکردهای کلان حاکمیتی را ندارد.
🔸
واگذاری اختیار محدودسازی اینترنت به ستاد جدید، با صلاحیت قانونی (کمیته فیلترینگ) و دادستانی کل کشور در تعارض است.
🔸
ایجاد این ساختار جدید، مصداق تشکیلات غیرضروری بوده و تنها باعث افزایش لایه‌های تصمیم‌گیری در فضای مجازی می‌شود.
پ.ن: جالبه تو این مملکت انگار با فساد و رانتِ کسی کاری ندارن؛ اما وای به روزی که بخوان اینترنتی رو که دست مفسدها رو رو می‌کنه، یه ذره آزاد کنن!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/iaghapour/2671" target="_blank">📅 21:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbNLrt73uasNGTvtGqxBr_0eM7SBLv8DquC5qnzqe8_Er3BMq8IUJclnscVWbG7_jXyM6w8LVnpt2UOmOQMTAxuFIhFKAoAW_b6XtM1hIkws2nyo8jCuEVOh-ZRzmeD0KFxhpuH8vWCOTzIz8chW_RvqvDQUhY2zf5_SpEMJde1140hhu7nqcYGGQOwJpEBx7KCfp_URyxF8kjHC1l16e-x5uho1qtLNRiRgbGPKdNCKOw4H-d2435grvbDTZZCEJv-qVI4DQiDo-Ibij_2barkiciOc9H7F9j9Ns_XM-23R9xfcoxQgo4xqr0McpV49t5s53_5ro4hJktkXhSrNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وزیر ارتباطات: محدودیت‌های اینترنت شفاف و زمان‌دار می‌شود / خسارت روزانه ۱۵ میلیون دلاری قطعی‌ها!
ستار هاشمی، وزیر ارتباطات در نشست خبری خود با انتقاد از وضعیت فعلی گفت: «در عصر هوش مصنوعی، دردناک است که هنوز دغدغه وصل بودن اینترنت را داریم.» وی تاکید کرد که قطعی اینترنت در فضای غبارآلود شایسته مردم نیست و سازوکار اعمال محدودیت‌ها باید تغییر کند.
🔹
چکیده مهم‌ترین صحبت‌های وزیر ارتباطات:
🔸
شفافیت و زمان‌بندی:
از این پس اگر قرار است محدودیتی ایجاد شود، باید مشخص باشد کدام نهاد و کمیته آن را تصویب کرده و
دقیقاً تا چه زمانی
ادامه دارد.
🔸
خسارت نجومی:
بر اساس گزارش مجلس، کشور روزانه ۱۵ میلیون دلار از قطعی اینترنت آسیب می‌بیند.
🔸
عادی‌شدن فیلترشکن‌ها:
استفاده از VPN که در گذشته قبح داشت، به دلیل سیاست‌های اشتباه به یک رویه عادی و روزمره برای کاربران تبدیل شده است.
پ.ن: وزیر مشکلی با محدودیت و قطعی نداره بیشتر داره میگه شما که داری قطع میکنی بگو تا کی که مردم اطلاع داشته باشن :)
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/iaghapour/2670" target="_blank">📅 21:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2668">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRlqxPIfmtT73_f1AmD0RxalnJSph0QCIa6UaAgYtxKi7ydW6zDY3GCR3kM1JU2jWyub3yk-HBzG9ygy36WE-4ThvuGnEQmQ8o3RyZ51xXYA6liwn9Y6mU_BtBvd8qLH8QBlVwZBJjsbSxSgzP_9ALB5H5BgpA2Ejs5HeqOLWJeg_WwSafvD0i-TLJQwwZdB_UzjON2antR1kUM3r91EYJ7r2k1dahcgaMRmNmXbLGmEhZ3QqDzdPVoukCkHB03CPGIQNq4ekT9dq-6NT8X0OlBDgNwkBRAYPVovENEu90i7YTewp9TTS0ZUttju4oQjtyUznyTgtnQqFz3B3_1Dpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای ساخت فیلترشکن شخصی با ۲ هسته در پنل پاسارگارد
🔥
🔹
تو این ویدیو قراره با هم یاد بگیریم چطوری یه فیلترشکن شخصی فوق‌العاده با استفاده از پنل پاسارگارد بسازیم. این پنل از 2 هسته Xray و وایرگارد ساپورت میکنه و همینطور از قابلیت نود هم پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پاسارگارد
#pasarguard
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/iaghapour/2668" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=pIVR8kMFBbhz45hhtRXBUxQQRmeKCcLFVkQYoXhcVxSnShkx_yZlMOIsbL9aEQ3QEvIVDeTWcTKQjDXj9epdexBbOMZo5x9igS6IX94usN16FGfOd36LA8yvcJw7Laorl2HVm0s_LK1j0-dksdmYC1nh1iTX086UhKimldV1Rd-3zFVRPXODDn4xu5iQ5Vd1bBVbrdgbg11HtJu_DidszcxBxWoXO2IQz6CdBrC4jMnJ6HAtisERf-mNHo0VNQQa9qZWjI-K7vXZQ-ndj68bfM86k_G-aHjhf4iVxOmVQyaebZlD881YGtSOAmcUwasqq4M8va6b9V0BS3TdE5jeKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=pIVR8kMFBbhz45hhtRXBUxQQRmeKCcLFVkQYoXhcVxSnShkx_yZlMOIsbL9aEQ3QEvIVDeTWcTKQjDXj9epdexBbOMZo5x9igS6IX94usN16FGfOd36LA8yvcJw7Laorl2HVm0s_LK1j0-dksdmYC1nh1iTX086UhKimldV1Rd-3zFVRPXODDn4xu5iQ5Vd1bBVbrdgbg11HtJu_DidszcxBxWoXO2IQz6CdBrC4jMnJ6HAtisERf-mNHo0VNQQa9qZWjI-K7vXZQ-ndj68bfM86k_G-aHjhf4iVxOmVQyaebZlD881YGtSOAmcUwasqq4M8va6b9V0BS3TdE5jeKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
چرا عنوان ویدیوهای یوتیوب یا زبان ویدیو برای بعضی‌ها انگلیسی شده؟!
سلام رفقا! جدیداً خیلی‌ها پیام دادید که چرا با وجود فارسی بودن ویدیوها، عنوان و توضیحات کانال رو به انگلیسی می‌بینید. یا اینکه حتی زبان ویدیو هم انگلیسی شده.
علت چیه؟
تقصیر هوش مصنوعی یوتیوبه! اگر زبان گوشی، لپ‌تاپ یا اکانت گوگل شما روی انگلیسی تنظیم شده باشه، یوتیوب به طور خودکار عنوان‌های فارسی و حتی زبان ویدیو رو براتون به انگلیسی ترجمه می‌کنه.
🛠
راه حل سریع فارسی کردن یوتیوب:
👇🏻
در اپلیکیشن موبایل:
🔹
وارد برنامه یوتیوب بشید و روی عکس پروفایلتون بزنید.
🔹
آیکون تنظیمات رو لمس کنید.
🔹
وارد بخش General و سپس App language بشید و زبان رو روی فارسی بذارید.
👇🏻
در نسخه وب (کامپیوتر/مرورگر):
🔹
سایت
YouTube.com
رو باز کنید.
🔹
روی عکس پروفایلتون در بالا سمت راست کلیک کنید.
🔹
گزینه Language رو انتخاب کرده و اون رو روی فارسی بذارید.
🎙
حل مشکل صدای انگلیسی (دوبله خودکار):
اگر وارد ویدیو شدید و دیدید صدای من انگلیسی شده، روی علامت چرخ‌دندهِ خودِ ویدیو بزنید، وارد بخش Audio track بشید و اون رو روی Original (فارسی) بذارید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/iaghapour/2667" target="_blank">📅 16:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7_DxGGWtkDH1iN0h_369TnOKmcUCEmIE5P7uVgK3DLfRSpCWr33IbwMx1cYcyrnDtccUT1MJlespKKqMQMppAUsUTnR4wW61hNtIeIFXPLdPM5zBlcFRoES1Mpj4RyYpprXMdzTJkzN-N0OEA_0hRB6UjjudhNQdrnXclQNMvBQx4ng2rDcpRw3x20MEz0MVyN8T_YOpVd9XbDhkf_NkRLmkPn73i584QXWhz-Ul3MoeVgSZyyl07LufIbWowGSGozkh2O8AhWjqUDOEJ8qmgmODVih_KBE_Q7lqHtEJMusVyuheuRg_ljZZY1mHKkqCCZYbsqpqv7ffaaQ6pnelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پولی شدن پیامک فعال‌سازی تلگرام برای برخی پیش‌شماره‌ها!
🔹
تلگرام در جدیدترین به‌روزرسانی‌های خود، سیاست سخت‌گیرانه‌ای را برای ثبت‌نام یا ورود کاربران در برخی از کشورها و پیش‌شماره‌های خاص اعمال کرده است. طبق گزارش‌های کاربران و تصویر منتشر شده، بخش جدیدی به نام
SMS Fee
به اپلیکیشن اضافه شده است.
❓
ماجرا چیست؟
تلگرام اعلام کرده که به دلیل بالا بودن آمار ساخت
حساب‌های جعلی (Fake Accounts)
و همچنین
هزینه‌های بسیار سنگین ارسال پیامک بین‌المللی
در برخی از کشورها، کاربران این پیش‌شماره‌ها باید هزینه پیامک ثبت‌نام خود را پرداخت کنند.
💵
کاربران برای دریافت کد تأییدیه مجبور هستند مبلغ
۱ دلار
پرداخت کنند. تلگرام این پرداخت را در قالب
خرید اشتراک ۱ هفته‌ای تلگرام پرمیوم (Telegram Premium)
ارائه می‌دهد.
پی‌نوشت: این محدودیت فعلاً برای تمام شماره‌ها نیست و تنها روی اپراتورها و کشورهایی که هزینه‌ی مخابراتی بالایی دارند یا سوءاستفاده از آن‌ها زیاد است، فعال شده. خوشبختانه
#ایران
تو این لیست نیست ولی اگه از شماره های مجازی استفاده میکنید باید حواستون به این موضوع باشه.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/iaghapour/2664" target="_blank">📅 00:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه چیزی میگم شاید باورتون نشه.
مردم الان بیشتر از اینکه نگران جنگ باشن نگران قطعی دوباره
#اینترنت
هستن.
کسب و کارهای آسیب دیده تا میان دوباره سرپا بشن اینترنت رو قطع میکنن یا اختلال میندازن و....
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/iaghapour/2663" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2661">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlqjAD7NtvKl7HXkNssuvisuz-ey-RoPgwlVyIA05Krt4hk21thN2-u8H4rJ4UXIgcW8K4tKoSE-E0sBHjcjADs8pscsP0Z8e4Bz81jwcE3XbDGQxotW2f49i9q3OZtfcRK0bP_JyA9diOjKoMBpR3rBKWNJCUMtElX4r8r1-5mHJ7WHILWZ0f_obzgg0O009uYUOaRAvkNXelT8G_MKx3LiA9ZweeI96s72DQfD-Ba-i8QneQWOoknrcOU_AQKtZWDaePs6GEXtcjPRCP-byMEKeN1Ho7lzc97X2QWMQk6Gv7VkJFfCilVrWFM8I8YyzV1OQKF-yksmOrR3ucpCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مدیرعامل آسیاتک: اینترنت دیتاسنترها هنوز وصل نشده است!
محمدعلی یوسفی‌زاده اعلام کرد اینترنت کاربران وصل است اما مراکز داده دسترسی کامل ندارند و شبکه به وضعیت عادی برنگشته است.
فقدان پاسخگویی:
پیگیری‌های زیادی انجام شده، اما مسئولان هیچ دلیل یا پاسخی برای این قطع بودن ارائه نمی‌دهند.
⚠️
مشکل اصلی چیست؟
اینترنت کاربران با اینترنت دیتاسنترها مسیر متفاوتی دارد. در حال حاضر کاربران به سایت‌های داخلی دسترسی دارند، اما
سرورِ خود این سایت‌ها
در دیتاسنترها به اینترنت جهانی وصل نیستند.
—
نتیجه این اختلال:
قطع شدن اتصال سرورها به ابزارهای حیاتی خارجی مثل گوگل، کلادفلر و گیت‌هاب (APIها).
— عدم امکان آپدیت، دسترسی به ریپازیتوری‌ها و سرویس‌های ابری (CDN).
📌
نتیجه:
اینترنت دیتاسنترها قطع است؛ یعنی پلتفرم‌های ایرانی از پشت صحنه به جهان متصل نیستند و زیرساخت فنی آن‌ها عملاً فلج شده است.
پ.ن: البته از وضعیت دیتاسنترهای دیگه اطلاعات زیادی در دسترس نیست.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/iaghapour/2661" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d11crse0PZAENQjz-NK-kEBFXsuyW17_tJtEklHQ6nDYVVxPRBursrOuQXIRs_a05Pkcmxr9IuTOgpcVnxXD0_Pqql21pv8N6sjWSDU-luvLt5Sv7lyYWuf_k1NH1vxZ72HPpa2X7sUo3X6TvXnq9IkjdfM64Vp9SWukh5IFHTvV2GhoWLwjJEQ-LdglCvBuZInoU8cw_P-rfG0wyK-fD4ACidmKsByoiqxHbxPdlTK-y0ldOVJzedEd0rtGHrkkaTMdLx6fZjdF18pnWjpaFRJQuGOTDRKO8eiUSnLn3SqP3QbG4nsnoXpouOvUItlo2agHVdvZglx-Xom1InnNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرقت بی‌اجازه ترافیک کاربران؛ پشت‌پرده دسترسی ناگهانی به کلاد و اسپاتیفای چیست؟
دسترسی ناگهانی و بدون VPN به پلتفرم‌های تحریم‌شده‌ای مثل
کلاد (Claude)
و
اسپاتیفای
، حاصل لغو تحریم‌ها نیست؛ بلکه نتیجه
دستکاری پنهان و بدون اجازه ترافیک کاربران
توسط زیرساخت اینترنت کشور است.
🔍
لایه‌های فنی و عملکرد
روش کار:
دولت ترافیک کاربران را به سمت سرورهای خود هدایت کرده و از آنجا به مقصد پروکسی می‌کند. کارشناسان این کار را مشابه
حملات هکری DNS
می‌دانند که پیش از این در سرویس‌های رفع تحریم (مثل شکن و ۴۰۳) اما این‌بار به صورت اجباری و پنهانی اجرا می‌شود.
امنیت داده‌ها:
به دلیل پروتکل‌های امنیتی، دولت توانایی دیدن محتوای پیام‌ها (مثلاً چت با هوش مصنوعی) را ندارد و فقط می‌تواند ببیند کاربر از چه سرویسی استفاده می‌کند.
⚠️
پیامدها و خطرات
خطر مسدود شدن اکانت‌ها:
ارسال انبوه درخواست‌ها از چند آی‌پی مشخص، پلتفرم‌ها را حساس کرده و ریسک مسدود شدن حساب را بالا می‌برد.
اختلال فنی:
این دستکاری باعث قفل شدن مداوم اکانت‌ها در سایت‌های تخصصی و افت شدید کیفیت VPNهای اختصاصی (به دلیل پدیده تونل در تونل) می‌شود.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/iaghapour/2660" target="_blank">📅 20:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIMDVXELnzHspBglVspe_JLfHsC7yYAcax505ry94N4xKIqlCmG28I8EnYgs1oZSAvPclKOw5NlGId8M4spyT_Cd1vQaZcBMvuJCkCsQ91wHjECUVX-NHQ6WFiyvV1bH5LoDtsQxUk8LkTxPy7jPc8f4H4sWGmD8QftKNLtLIeaIyOiVTNywaF47n8cHYT8TLL-HNGqLMZmFOjIxO9pqVdwu3CSxXuwXP_WpJXt-Fx7v-_b-IVsd2hA7bUbcQyu96oVigXEQrDlVA97tsaRaR7PuqGoFjkXrh4T-Ehy_k_xjYqfo755xdC4fB54tT8mLyzMx-dlydI0CcQ3SgF3pjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نصب خودکار داکر روی سرورهای ایران
اگر روی سرورهای داخل ایران داکر نصب می‌کنید، حتماً می‌دانید که به خاطر تحریم‌ها و اختلالات شبکه، باز کردن مخازن داکر و دانلود ایمیج‌ها مکافات است. این اسکریپت متن‌باز و امن، کل فرآیند نصب داکر را خودکار کرده و در انتها به شما اجازه می‌دهد از بین ۶ میرور ایرانی (ابرآروان، داکر آی‌آر، لیارا و...) بهترین را برای رفع تحریم انتخاب کنید.
💻
روش اجرا: کد زیر رو کپی کنید و در سرور اجرا کنید:
curl -fsSL https://gist.githubusercontent.com/ShahinDadashpour/35892443c09d582e53b36d09fb5a5df6/raw/install-docker.sh | sudo bash
🔗
لینک سورس کد در گیت‌هاب جهت بررسی
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/iaghapour/2659" target="_blank">📅 01:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMt_saSNHr8mew1TmjONIKNBN_KzOFotxC49vD-TXhgoIK9haUspTQpgseO1mht3kk0EqoFomnLT907x2bq7QyYJBsPyvQP2vYOie1XilR6t9dru_rmjNaoUlNj2_yNrtkF_YpQMAkd4X6rd0aM6s-l5liM7v5RuuEmhb6S5K_DOVAp8zSE3BYoGmmkfaqt125qofZuE2uO8MFLZgHnvu-rQr5zuuPGR8KFKxwOHnDwn9ujzgY5pMil2ioOcfCMJimOww4-RmiyeFw14UOiW2OvpQbJyKPMgSRLNksVkA3FICMHF6Ln4ntkiYdJEgMItk3XwFKh3umA57fGLMnlcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن بدون تانل و بررسی روش های موجود
🔹
خیلی‌ها فکر می‌کنن برای داشتن یک فیلترشکن شخصی حتماً باید درگیر دردسرهای تانل زدن بشن، اما تو این ویدیو تمام روش‌های موجود رو بررسی کردیم و بهتون آموزش دادم چطور بدون نیاز به تانل، یک فیلترشکن پرسرعت بسازید.
👇
در این ویدیو به چه مواردی اشاره شد:
— چرا تمام روش ها منتشر نمیشه؟
— چه روش هایی در شرایط سخت کار میکنه؟
— آموزش روش مستقیم ساخت فیلترشکن.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ملی
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/iaghapour/2657" target="_blank">📅 18:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2rUp2mMJiLmkXZM620BDyU4V8fEIHyoL9qpUoGuBkOEBL92heRcxLg2pbfHSyj63DWbgowTcHNC1pEW_iFmZAfLg1mRmiEPSkmA1EOpQtscQydAd1vyFZajeCGqnXKuwzBk2s6xjMCt24_28Jm0oWQDs6o0qRQdqVjnfuc73GRBPURS3Z4ZahyVmSLCNe8RsZnrmU7l7MJ-gto0EbVgExmC6iSxu2f8tpnqzJuITJw9gEYc0xA9_OwIF5lMm6VtQnDnxB8WcMlkb-9UOFycjWa-eeLB55kf4-GM5Z7BWzCc14F9w39qqOzZzvjI6mWSrc78efJhEHkXnpUCv39wnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بلوکه شدن ارز دیجیتال در خریدهای خارجی (CoinGate)
دوستان، یکی از کاربران هنگام خرید از سایت
Hostinger
با ترون از طریق درگاه
CoinGate
، متأسفانه به دلیل تحریم‌ها پولش مسدود شده است. طبق اعلام رسمی پشتیبانی این درگاه، به دلیل قوانین بین‌المللی، وجه بلوکه‌شده
به هیچ‌وجه ریفاند (برگشت) داده نمی‌شود!
⚠️
چرا شناسایی می‌شویم؟
درگاه‌های خارجی تراکنش‌ها را رهگیری می‌کنند. اگر IP شما نشت کند یا ارز را مستقیماً از صرافی‌های ایرانی به کیف پول خود (مثل تراست ولت) منتقل کرده باشید، به راحتی به عنوان کاربر ایرانی شناسایی می‌شوید.
✅
راه‌حل و پیشگیری:
—
هرگز
مستقیماً از صرافی ایرانی به درگاه‌های خارجی واریز نکنید.
— همیشه از
کیف پول واسط
استفاده کنید (ارز را از صرافی ایرانی به ولت اول، سپس به ولت دوم بفرستید و در نهایت از ولت دوم خرید کنید).
— هنگام پرداخت، حتماً از IP ثابت و معتبر استفاده کنید تا نشت IP نداشته باشید.
لطفاً این پیام را به اشتراک بگذارید تا سرمایه سایر دوستان به خطر نیفتد.
🙏
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/iaghapour/2656" target="_blank">📅 17:00 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
