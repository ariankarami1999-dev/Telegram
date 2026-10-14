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
<img src="https://cdn1.telesco.pe/file/DAecZ6-pxT0-WQ7bE4802oYMFauBXTuXPPCt1YMcrLkhNmhfZA7fwfiAnDO2zmfnr6XEg6uQumew6uQwy1xT4CqpuwuOeI8eQSe8mOcLFoQP1Goc7ZJao_V4gJK_s6Ax-QokQ9QnXeu21Nxf2WKLLLavzAjGIhxB86jp7iGyOTdcApkr5-IKOeN1TyVY5N3PqyXwaGJraFs0R2weDszaNodPbZ7ryPBuzMuQ7gjs73a756X_9zbuKQz3qTSX-_E1tmxWw3_qHAHbhXjk58p4LfdwECv-nKYcVdEsFDN8Zv94kXKy1Nc96HywPPsYLuypw6k2SSbYAr-cORoj0X3qIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 05:31:08</div>
<hr>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی و فکر میکنم با ویدئوی بعدی یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/MatinSenPaii/5575" target="_blank">📅 20:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گویا Mpay رفته زیر maintenance. حسابای منم قطعه فعلا که گفتن اوکی میشه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/MatinSenPaii/5574" target="_blank">📅 19:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sl_nuTexvEkzhk06WPZcilx095GeU4V-jF2yc5_S5BtN_3fpIF5-OCo_v_xmqsfews4b-Z_yL9lvoeO3zmxaZ1I-aY0TmGl3M9Ep1Fo07DEXbVhfOPgJTA2OGaawFjiMD5C5Nv2o9aLK5WyedFITKlrk8utbCO3A3nckzqSuomeTeAEl-woXXk8A75KeIuaJzl64Ih7S07UIXsMcd_i387iDmny6KRK_IJaKa_6EZG-ncFykLNAjl6r6JqwtnSBJo8qAhXzkoYKuv1ULEvQypfoxGSrnroM2pu3u-oAWU1xZ4fFf4CbXKpxjxSYWqsfBLk86OcSvVUvAjyK5pJKA8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Wonder بی سر و صدا معرفی شد:
• $4 input
• $20 output
• $0.20 cached
قوی‌تر از Fable 5.1 و GPT 6 Astra، و هم قیمت Opus 5.5 اما اندکی ضعیف‌تر
(نیومدن Sonnet 5.5 توی بنچمارکشون یعنی احساس خطر کردن
😂
)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5573" target="_blank">📅 11:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsgYhyQsWdzjy6mCpk1NIt74-PGRsfvly2ThHd20G_rnTOv8I1cZw8MtidWqz1YLyCzqXtEgECCajaL-KMbB3BVR1h2IHAXQ6aKc_bGe2cTztLQNu3aZr4PswakUZjgM4FURG5L1jopXBN-svpfQHTnt9kgwu5SWyUcmiVWWigRe0gusNUhktvWUHIiBSEpcgY6jWxEBPPhbu5eTualIe2DLcUxxca526FT5bKaC89M8Abdx7Ro2MmheLqq8rwEeVMgMzatHK3mivqytlIRwp5L_m6ew4g1Mu0LtlYxJ1y3IJo55XjgPPDD84OuZJiXSn5JaO8-uGU7daBzxFdwniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنپ؛ مدل تصمیم‌گیر که ۱۰۰هزار توکن رو زیر یه ثانیه می‌بلعه!
استارتاپ Subquadratic مدل SubQ Snap رو منتشر کرد: کانتکست ۳۸۴هزار توکنی مولتی‌مودال (۱۲ برابر رقیبش Jev)، پردازش ۱۰۰هزار توکن و برگردوندن تصمیم زیر یک ثانیه، با قیمت ۵ سنت به ازای هر میلیون توکن ورودی و خروجی رایگان.
توی بنچمارک Decision Index امتیاز ۶۱٫۷ گرفته مقابل ۵۷٫۹ جِو که طبیعیه. ۱۰هزار کاربر اول ۱۰۰ میلیون توکن رایگان می‌گیرن:
subq.ai
در واقع پنج دلار میده. مثل اوایل jev
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5572" target="_blank">📅 08:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آموزش راه‌اندازی Muse؛ ایجنتی برای روزمرگی  اول بهتون بگم که Muse چیه از دیدگاه خودم(یه آدم با استفاده معمولی): هرمس ایجنت رو در نظر بگیرید. اما: سریعتر، راحتتر، بدون ارور، بدون ارور، بدون ارور، و بدون نیاز به ست کردن  API Key، یه سرور رایگان که این ایجنت…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5571" target="_blank">📅 07:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5570">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKwTxux6-u9_0Bf48TxQG4y_ClvT8aetAZhkGmqkC2In4Z4dZNAyxtQ8h22VpEDDKBu7OwziKLQnXo-KMgwe6aFM0rOgy3_3m9tKkEvu5MCbR4wpIS7p3YZ8806tSvWmhSG8iT1Fu1LK3RKiG1G7S7P8lO3h_LvQ2trZ-4dONIbf2YnM_nyW5FaYZEyWCgkmOcewrcL5jbulVWwxEjd5n5L3aVpjLT4jJji4qhC3AGBlJLgipVkxtujgQGLaBegE6-9M12lB8J308ubVcY2Vd8dlZIHtFhGarez7mPJwOHfPsQgIa0uNGTwwp_W5-sGdt-LbZOArKbeW3tc7ba2k3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش راه‌اندازی Muse؛ ایجنتی برای روزمرگی
اول بهتون بگم که Muse چیه از دیدگاه خودم(یه آدم با استفاده معمولی):
هرمس ایجنت رو در نظر بگیرید. اما:
سریعتر، راحتتر، بدون ارور، بدون ارور، بدون ارور، و بدون نیاز به ست کردن  API Key، یه سرور رایگان که این ایجنت داره روش اجرا میشه؛ با راحتیِ وصل کردن هر پلتفرمی بهش که فکرشو بکنید.
صرفا... با سطح کنترل کمتر توی مسائلی مثل محیط اجرا یا خود API. که شاید نیاز معدود افرادی باشه توی این کانال
حدودا یک هفته‌ست که دارم با این ایجنت کار می‌کنم و واقعا عالیه!
مدل پشتش Muse Spark 1.3 هست.
ایمیل‌هام رو جواب میده، واسه‌ام برنامه‌ریزی می‌کنه، چیزایی که می‌خوام رو توی Google Sheets ام وارد میکنه، جزوه‌های دانشگاه و Rustام رو خلاصه برداری میکنه و قسط‌هام رو یادآوری می‌کنه(
😂
).
یهویی مثل هرمس "سکوت" نمیکنه که وقتی بهش گفتم خب چی شد و چرا یادآوری نکردی بهم، بگه "اوه شرمنده داداش! اون لحظه api key یا سرورم قطع بود(دفعات زیادی این اتفاق افتاده توی چیزای مختلف اما هنوز، هرمس عالیه. برای کارهای مختلف. خوب بودن Muse دلیل نمیشه هرمس بد باشه)"
شما نمی‌تونید روی Muse، پنل VPN و DNS و... نصب کنید. لااقل من که نتونستم و اصلا آیپی عمومی نداره و فقط دسترسی HTTPS میده. 9Router و... هم نتونستم طبیعتا. هرچند به نظر یه کم Tricky میاد و باید باهاش کار کرد هنوز شاید قانع شد
😂
در مورد 8 گیگ رم و 2 هسته CPU هم بگم که این منابع اشتراکیه و متا هم سر گنج قارون ننشسته.
سرعتش هم یه وقتایی میاد پایین اما خوبیش اینه که شما با هیچ اروری سر و کله نمی‌زنید! و یه دوری بزنید و برگردید همه چیز اوکی شده.
و میتونه براتون تصویر و ویدئو هم درست کنه(ویدئوی فریم به فریم کوتاه و..)
که متن فارسی هم داخلش خوب میفته.
آموزش راه‌اندازی:
*نکته: اگر که هر چیزی شنیدید(ریجن ایمیل و تایم ساختن اکانت و آیپی تمیز و...) اشتباهه. میوز فقط و فقط به آیپی حساسه. و تنها آیپی‌ای که باهاش تونستم وارد شم، آیپی آمریکای گوگل بود(که صد درصد یعنی با آمازون هم میشه)
1- با این روش یه VM آمازون بسازید با لوکیشن آمریکا(200 دلار کردیت رایگان):
https://t.me/MatinSenPaii/5130
یا با این روش یه VM گوگل بسازید با لوکیشن آمریکا(300 دلار کردیت رایگان اما 10 دلار اولیه باید بدید):
https://t.me/MatinSenPaii/5149
که گوگل خوبیش اینه که سرور Always free میده و منم از همون استفاده میکنم. یعنی مهلت اعتبارش هم تموم بشه، اوکیه.
2- پنل سنایی یا پاسارگارد و هر پنل دیگه‌ای رو روش نصب کنید(توی آمازون نیازه پورت‌ها رو Allow کنید از توی پنل مدیریت سرور روی سایت(به Grok بگید راهنمایی میکنه))
3- یه کانفیگ Vless معمولی Raw بسازید(مهم نیست که مستقیم کار نکنه. گوگل که اصلا امکان نداره مستقیم کار کنه)
4- اپلیکیشن PattN و PattNG رو نصب کنید(یا هر کلاینت V2ray که از قابلیت Chain proxy پشتیبانی کنه)
5- یه کانفیگ که واستون کار می‌کنه رو اد کنید، کانفیگی که از سرورهای گوگل یا آمازون ساختید رو هم اد کنید، و بعدش این دوتا رو با همدیگه Proxy Chain کنید. و VPN رو متصل کنید و پینگ بگیرید.
6- بعدش وارد اپلیکیشن Muse روی گوشی موبایلتون بشید و با یه ایمیل که تا به حال روی سرویس‌های متا ثبتش نکردید، وارد بشید و ثبت نام کنید. به همین راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5570" target="_blank">📅 18:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h176MVe0vdblMvQb7t5-NDWWWTKO2kBa1drvSmTSxj4xBETr83KyqXtx0X8SlriB6MaIpCcJYO5xZbpu1dmSuNluuvUXo_lRPi2bRywnkEQCDsjs0lYIhA9QbvDbSbf50om28D404a5AFM9V48gTPU5NGAzImr8sNQsLM2GYosxVQWhTrNU5OBSevVkJDK_Bd18XT-l8JYaMrmweXDLvfLCkpbryF8cXRM1B3on49GQYXlxq0Jx8G1O6-7lH1_fJMRIKciYHIaO-QXE2jwU2XBFwckTMMRw5BGnWOfHEeEnkf0w5um7ClYeHfy2tAOYaGg537lNItckbq0j2k1eefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول نوشتن آموزش ورود به Muse هستم
فوق‌العادست این ایجنت. عملا برای کارهای روزمره، کمتر از هرمس استفاده می‌کنم به جز کرون‌جاب هایی که از قبل داشتم چون Muse همه چیز رو Unified و سرراست داره، و توکنی که میده توی چت برای مدل هم خیلی خیلی زیاده و کامل تمام تصمیمات و کارهام رو یادشه. به زودی از مزایاش بیشتر میگم</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5569" target="_blank">📅 15:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/edcziW-WfDyRSkfXOXcs0g-nybzhoHPMKFtG2q0UhdxEL5FWEDNHDdXUbGJSXEjr0B9UrK9U5GVmrX5tY3DrQ9XxJilhv7KINlQ6D4tgPh7uOuYcO2QP0d2eEtUF4UydfJLgy8gdX4pcJGemXUG-Ovq6imja0JosTWPFOrgDuocrIWVjRXb8LN8OJcYeP1Li2WKSgIR7-ciHK2GBHrbGVdNEpu7PeW4E0V-_VkImaE4nlV426u5vFR-YTw-QMkVoAxPBq0TJZNd19PCKv5_NKVkuKW4YiJHe9DSktJpSAfyS1wFTIApYfKjw7Ik9grhhRRdFHASuPzTsUAUbVL29HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوری؛ جایگزین اوپن‌سورس Canva
پروژه Doory
https://doory.art/
به تازگی روی گیت‌هاب منتشر شده و خودش رو جایگزین اوپن‌سورس Canva معرفی می‌کنه؛ یه ادیتور طراحی تحت وب که می‌تونید خودتون ران کنید و یا توسعه‌ش بدید
🔗
لینک ریپو
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5568" target="_blank">📅 15:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkkM6ww0gi0DCGD1SLsi7dOYTpvex_1l4UYCJxoRdRygK0SlgjUz6bb207aoCKx_tbPhq1ytY9wpEJhvjTwHPc8SKGFYAm-5CpIdFEk3kD8Fi5WLB7d6i9okG1Ml1Y0mXHBHx5U9vc7br_J2WLJpPa2GjQ_1TE5uC8YZClAeRhxhSUQreafa7SXQziJ5m6KUFqA3LvFjSn7DKxIcnqqdQ-uYdJbrS5dMN9pffqAy8qwKwVXOXqZEu0CmkessmdubXVS_YvCD70IfmpI6zZRw4kocPYS8mcFLGTsnf1UGRbxlE1Za2XnaWaObR_WvM1kHXvjy9cLtFfaNyJ36PDIeRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل زبانی‌ای که خودش کانتکستش رو مدیریت می‌کنه
محقق‌های متا، MIT و دانشگاه واشنگتن روشی به اسم CLM معرفی کردن؛ به‌جای خلاصه‌سازی و فشرده‌سازی دستی، خود مدل تصمیم می‌گیره کانتکستش رو چطور ویرایش، نگه داره یا دور بریزه. می‌گن هم عملکرد بهتر شده هم هزینه محاسباتی کمتر
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5567" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این ویدئو هم ادعا شده که با کد خالص نوشته شده. توسط مدل نامعلوم Claude</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5566" target="_blank">📅 10:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این ویدئو هم ادعا شده که با کد خالص نوشته شده. توسط
مدل نامعلوم Claude</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5565" target="_blank">📅 10:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5064aac929.mp4?token=Bwa8lJrIsTOIm34P3_QmgA8y4e5WMhJB43-WPkoskrn-z-c_g90jb9yZ2VjB6xVBwMPxnaVdWgnxqDMyFQulC0N6Nsx0QTI2H-MJIS-A0NPgD5BcVqDl0ybfd8kB0DIv8F4WCdyyokQYbVyUA1vYAzGAbTYrgWenCAt9xL9ClWpBc9RtxsiL1toRlZwsyLj444bHF8ra2CLKsD0AG3XcUkGhR6UXi2ZpcsrDH6RGtlVg4gRng_ICjzXgPPXs2V3NZeLujc-gztENxvCXT_pZvoi-etJF0VJ-p6OBJSfVxaMvKsZ-0P3boDs1gCg1EySIArB_B824luuXIZ4Y2XRMfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5064aac929.mp4?token=Bwa8lJrIsTOIm34P3_QmgA8y4e5WMhJB43-WPkoskrn-z-c_g90jb9yZ2VjB6xVBwMPxnaVdWgnxqDMyFQulC0N6Nsx0QTI2H-MJIS-A0NPgD5BcVqDl0ybfd8kB0DIv8F4WCdyyokQYbVyUA1vYAzGAbTYrgWenCAt9xL9ClWpBc9RtxsiL1toRlZwsyLj444bHF8ra2CLKsD0AG3XcUkGhR6UXi2ZpcsrDH6RGtlVg4gRng_ICjzXgPPXs2V3NZeLujc-gztENxvCXT_pZvoi-etJF0VJ-p6OBJSfVxaMvKsZ-0P3boDs1gCg1EySIArB_B824luuXIZ4Y2XRMfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل جدید Claude قراره خفن باشه(اگر لیک‌ها و شایعات درست باشن).
مخصوصا توی ساخت ویدئو با js خالص.
اکانت توییتر chetaslua شایعه کرده که روی Claude code به مدل جدید Claude Next که فعلا در دست تست هست، دسترسی پیدا کرده و هی داره باهاش چیزمیز میسازه(مدل Image/Video generation نیست)
و میگن احتمال زیاد، Fable 5.5 باشه
(R.I.P Gemini 4 Argon. we all forgot about you brother. hope google come back with Gemini 5 Xenon next time
😂
)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5564" target="_blank">📅 07:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2wMRybXmQ8OdSIU4SLoWiaaqEdjABVTdMeRta3rm5QQxLat6zwMB0Vr0bI6CQuOvpRZWU10M7GDsCYn-6CsAd7NqPtvDzGv2JaZ02vsKGr2nq_0RLStQxMzpCED653rfrcWPbDxS_1cKvPII3q1RoPOsguN8BZuaY3l3_3nUZRCBIGXR1NTliWpyTVTRLQWzwXUaB4VCDMoKXkeEX8baWoghaTyCOCRtJiF_-PDQ6ijQ1ic662XbDSmmpYpMDCSJ7xrP8c7cknsBU_fo07W3tn0igMNVGCNuZof_8wcpA9tnViranbc3Y0ZpmQuUN9MpcUhSxoI_FfpWXk4SWH4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله ClickFix با طعم Claude؛ تبلیغات گوگل آلوده شد
هکرها دارن از ریدایرکت‌های واقعی نتایج جست‌وجوی بینگ به‌عنوان لینک کلیک توی تبلیغات گوگل سوءاستفاده می‌کنن تا کاربرها رو به نصب‌کننده‌های جعلی Claude بکشونن که حمله ClickFix تحویل می‌ده. ترفندش اینه که لینک تبلیغ ظاهرا معتبره ولی به صفحه مخرب می‌رسه و با انجام دادن پروسه‌هاش، دستگاهتون آلوده می‌شه. کلاد رو فقط از سایت رسمیش دانلود کنید.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5563" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مدل‌های زبانی بایتی؛ بدون نیاز به توکنایزر
یه مقاله‌ی تازه ادعا می‌کنه ترنسفورمرهای معمولی می‌تونن مستقیم روی بایت خام کار کنن و با بزرگ‌تر شدن پارامترها حتی از مدل‌های ساب‌وُردی بهتر بشن. باور رایج این بود که دنباله‌های بایتی چون ۴ برابر طولانی‌ترن(در مقابل بیت)، ناکارآمدن؛ نویسنده‌ها‌ی مقاله می‌گن این طول اضافه با مقیاس جبران می‌شه و انتزاع‌های زبانی خودشون درون مدل شکل می‌گیرن(که به نظرم اینجا باتل‌نک قضیه‌ست و باید به شدت بره زیر تست). به نظرم مقاله‌ی جالبیه. وقت کردید بخونیدش
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5562" target="_blank">📅 21:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uTzkcYlU7zu8yVYsJK5k_J6LuEQaF1zzm6AcdM7ILRANoZatwg8uUTEWBuUCBLbwewMN4eGZDlvMI9sttwEPCa4S4919MpaOEfHVEnK-Mvkh9oYrcKCYUchrwJ9xS9prvBdM7uGECtHU-z2vFuWfSiqlw_vA6LwXErkzSgrXLbyRAHrmPa4kv0o35U6RmUh5NJr4q36aEhyzwjFaXOQwLvXstYaUXGOAVtQV0lcfFyGhHHZ32X81xHmVZp1Z-nx3aYN91v2x9KSInaJrwyGr48gqJdT72_S8GFxKfXJziLGUv_fvZaMis1CD7H0b4KtQjgMd2dhAwvQlX7MoKs3ysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل اوپن‌ویت پرپلکسی از Jev جلو زد
یه ارزیابی مستقل روی ۶۶۹ کیس پزشکی می‌گه مدل pplx-decider-v1.1-27b پرپلکسی تعداد ۶۴۳ جواب درست گرفته در برابر ۶۲۸ تای Jev، با ۴۲٪ هزینه کمتر برای هر تصمیم(که فوق‌العادست. موندم مدل مایکروسافت چند میگیره
😂
). قیمتش ۰.۰۲ دلار به‌ازای هر میلیون توکن ورودیه، و خروجی رایگانه، کانتکست ۲۵۰ هزارتایی داره و روی OpenRouter در دسترسه همین الان. صدر جدول Decision Index هاگینگ فیس هم مال خودش شده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5561" target="_blank">📅 20:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ekmJmLBMzVC_YHANJQGurLQQRRKYNZCpMGXXBi5jQQkDKhDRhfNCT3OtdKY_5nR5cZ7dBH4p2JqYgZCIrWh2np55T2YzTgedMA0ErUcu9ZSQFeAEYGVV7BqJYtRXhYbSBZIx-cFENxIR8UST44HuF5cYD4jIvF0AoBbLHNM9J-K0f2oGA7OWomC9FnLtpmrIcSBDV_YE7GaLVjxcIPwk--7NIpNCqumC9gpJsiOwVzd56IVVwp3tSs6yEBMvh2hDD_8q7RsMQKq1bGkxTOr8So9bLobx5OB8QWptv40vYfgCKEFRLlqbDC9T3k2GyUeeS7rft7-RUPu8EKL8vZQnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت Decision-1؛ مدلی که فقط تصمیم می‌گیره(نسخه تنظیم بازار Jev)
مایکروسافت یه مدل تصمیم‌گیری (decision-scoring) معرفی کرده برای کارهایی مثل روتینگ، دسته‌بندی، اولویت‌بندی و کنترل ورک‌فلو؛ یعنی به‌جای تولید متن، مستقیم خروجی ساخت‌یافته می‌ده که نرم‌افزار بتونه باهاش کار کنه. ادعاشون: بالاترین دقت بین ۳۶ بنچمارک با نزدیک ۱۵۰ هزار سؤال، و سرعت ۴.۵ برابر نزدیک‌ترین رقیب و ۳۵ برابر GPT-6 Sol(چرا باید با Sol مقایسه‌اش کنن؟
👍
). توی Foundry اومده و به‌زودی روی OpenRouter هم میاد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5560" target="_blank">📅 20:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کارزاری ایرانی با ChatGPT مقاله‌ای جعلی در رسانه‌های واقعی آمریکا به جا گذاشت
گزارش واشنگتن‌پست می‌گه یه کارزار منتسب به ایران با کمک ChatGPT مقاله‌های تولیدشده با AI رو تو رسانه‌های واقعی آمریکا جا کرده. و این نشون میده عملیات نفوذ رسانه‌ای با AI چقدر ارزون و تر تمیز شده.
اینجا هم به دلایل مشخص نمی‌تونم بازش کنم جزئیات قضیه رو
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5559" target="_blank">📅 19:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNti8pbTKwf_Pk0D_rId8QKh3Vd1Z1rUwFpcAV8LqG3hm1GKFku2l2t6c6Ou22TaAIGysCDGB-PevoVQbLQi76n6aDkU6JekWPEy01Bo2IBCQTgJ-1SIQC6wBPlVigCjUO_Ydg_r6XYu5PmYYcVfRRvtwc3-htuLgRNS8PyIc6zCCWl_YXPyGVn7dvcuIycbHG1LjcHlteo7ViBJYRxch8_Q4dVcVNMhCmCydT3MMzj2GUbQYGa66pRpGsoaUHDi92Rhe53Km0v19SUZ_ydxt2UWDh7dZBTjnRPMWuAqAcC0robe1GPNmDsdOUdiF2eI-c_ZUEUC-gPXDC7Thtw0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه‌ای که یه زمانی فورک Redis بود و الان انگار وارد رقابت جد شده: ValKey
پروژه‌ی Valkey که دو سال پیش به‌عنوان فورک Redis شروع شد حالا ۱۲ تا Maintainer اصلی و ۹ عضو کمیته از شرکت‌های مختلف داره؛ تروپوت بهتر، کلاستر قوی‌تر و برنامه برای رپلیکیشن Synchronous و ذخیره‌سازی چندسطحی. تمرکز روی امنیت و اتومیشن هم جدیه و داره از کاربرد «صرفا کش» ردیسی، فاصله می‌گیره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5558" target="_blank">📅 18:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HBVv8BDY6j45XYI3Nu09PH9VOSjmTvjR9xLrTf4LicJZhckIvynw-7_afbKIhgRGWmH53aXLOKH8pEtlV5Fx7Wt9ktH7Uq278jr0Ux_4Bo3-lVRB_fUHTsFb44b1EySxvMjENXP0frWlsbaFxxuf_jxZc7VmDAqUoQ5dP4WUX_mfNkzcnXqxmC9IcdnBHIZYrDCIv4jaH_BQSrpu5t4XdkknxaqFXa3dEUMme57Ai_LL4aH9Ei_xilmRs7Mn_LtGoVHm4hiLxPTDlpFyXg-08gN2RLAY-nARgxe1BrRqhrBuOS3_xRv25jycum_usrIn7S7u1__CHrKc5UO3klr5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من و ایده‌های استارتاپی خفنم که قرار بود باهاشون پول در بیارم توی ایران:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5557" target="_blank">📅 17:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تیکه گمشده‌ی ارور هندلینگ توی Rust
یه رایت‌آپ خوب که می‌گه درد Rust انتخاب بین تایپ دقیق پر از بایلرپولیت مبهمه؛ راه‌حلش کتابخونه eros با «مجموعه خطا» هست: به‌جای تعریف enum تازه، می‌نویسیم (io::Error, ParseIntError) و کامپایلر چک می‌کنه خطای اضافه propagate نشه. با widen هم ترکیب می‌شن و کانتکست می‌گیرن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5556" target="_blank">📅 15:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bHqCpLXEoIqeypMjGBOE4IQV0W3PVV5O_46kXxQzaF2Qtqv5YmeciIlXUSukAbYZzxWMmN9i-VOuzNc3epVv-8t17xhjhCid5cLQpbk5WpscB0Fp4SAGyvdRBi5SFEvH13aLGjsdJFwU0E0yj55aNIfMxYG-9A9OytLP1jCUsU2xv4Ybxi-K-ygFraAwtcCyVwXwGTkQueJFRObXX3l6AaJJ1msxC4eF7IPuWJhax6XNloaFRzf5CpWuwjz_p4UNcy5mNv_8nW99hQ0nrL3aMHk73RLDd9bLV70env5Ev7q3xwmAtf1M5y0uHJa5qPU4UQV7hSrqrYT0QUe6FFbO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدلی که وجود نداشت، پس خودت با ML Intern بسازش
یاوراج شارما تعریف می‌کنه دنبال نسخه کوچیک بازنویسی شده‌ی Qwen-Image 2.1 بوده (نسخه رسمی ۹ میلیارد پارامتری که ۲۰ گیگ رم می‌خواد) و با ایجنت ML Intern یه نسخه ۰.۸ میلیاردی ساخته که روی CPU اجرا می‌شه؛ خروجی معتبر ۹۹.۷٪ و کل هزینه محاسبات ۱۶ دلار. تو چند روز شش مدل دیگه هم همین‌جوری ساخته و هر هفت پرامپت رو تو گیت‌هاب گذاشته.
به نظرم جالبه ببینیم برای GLM 5.3 Flash چیکارا میشه کرد
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5555" target="_blank">📅 13:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIMfvzwf-VMAn5HUzARDMSAtFwpMPiNaEwUGiDBFysagwhn1ROLQdtcce03DsbkTZdvuaLFFQL9s1lsSyflVZu3SS4YqLaFjht8K7TDWUkMuCVcMukzr5cIzSSSevxlzYF4nsBeGg6_0sqrEyf4vN-49-YmHnLg0ExS5omQJjIDv7ATbwuuFw9jZybPMZUADOSyP8jmDJohpRpDSB6LWbyfLO2wcSbRS4cBTin00XfB7UV2Ef-Aq70ziaRry8UtRjCq_LFsqUXfW8vxMXw7xa6SLKie6x7mZKAFkxqrGGQg9ACVXGL2SHvr9MJo6KuP3Stdg9aik_uOEhMRo-UZl-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داده‌های زیستی آماده برای AI
ابتکار Virtual Biology شبکه‌ی Biohub گسترش پیدا کرده؛ تعهد جهانی ۱.۸ میلیارد دلاری برای تولید داده‌ی زیستی باز و آماده AI تا بشه مدل‌های پیش‌بینی‌کننده زیست‌شناسی ساخت. اگر کسی از شما بچه‌ها توی حوزه‌ی پزشکی یا بیوتکنولوژی کار می‌کنه، دیتاست‌های Open این پروژه ارزش دنبال کردن داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5554" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حمله به بانک‌های کره جنوبی با کمک Claude
یه هکر ۲۶ ساله‌ی چینی مظنون به سرقت داده‌های بانکی کره جنوبیه و شواهد نشون می‌ده از Claude برای پیدا کردن کانال‌های تلگرامی فروش اطلاعات سرقت‌شده استفاده کرده. یه نمونه‌ی تازه از سوءاستفاده از ایجنت‌های AI برای جرایم سایبری که زنگ خطر رو برای دولت‌ها به صدا درمیاره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5553" target="_blank">📅 10:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مدل تصمیم‌گیر خودتون رو بسازید
یه آموزش عملی و تعاملی توضیح می‌ده مدل‌های تصمیم (System One مثل Jev) چطور به‌جای تولید توکن‌به‌توکن، با یه پاس و ماسک کردن وکب فقط از بین گزینه‌های ثابت مثل A تا E انتخاب می‌کنن و احتمال کالیبره‌شده برمی‌گردونن. نویسنده با Qwen3-1.7B و transformers نشون می‌ده چطور همین رفتار رو خودتون شبیه‌سازی کنید. به نظرم خیلی بامزست و ارزش مطالعه داره این مقاله:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5552" target="_blank">📅 09:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5551">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W2IGn-VKm_prp48ow1u3eT9KBE3aRHndW6tsRMNupCxMBFNT3cLvhC6gSjC7QaHrv63GYpgVqSfSGGI91ByF2fY2kSkQVcov78sKqHOl_6oRlRfYJqjt0n5UlJEVqX2qlzjkMNaoP2p5dQSjjw5pSvpsDmOcYX9uS7uRQBpiloDKl40TUJfIbDYw-Wn9kfiFgUYG8ge-73JNPI7IJf3szAEY0g8kEKGLGa5vR-sXj4aNrN2j9Tyg3HjGXze5SqEoTGPVmMs8fbZeRfU9evGW02wwEtSAZUeerUTh886WjvhpN01USFdC5ZiDka3byx-pJDfU4aP2liH8gmzhqCjlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفیس اوپن‌سورس با Rust؛ کدنویسی با Claude
استارتاپ ArtCraft نسخه‌های مشابه Word و Excel و PowerPoint رو به لاین‌آپ اوپن‌سورسش اضافه کرده؛ یه جور بازنویسی آفیس مایکروسافت با Rust که بخش زیادی از کدنویسیش رو Claude انجام داده. هنوز برای پروداکشن آماده نیست(که نکته‌ی مهمیه و توی اون اپ‌های جایگزین فوتوشاپ هم دیدیم که به نظرم به زودی آماده‌ی پروداکشن میشن).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5551" target="_blank">📅 08:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">طی امروز سعی میکنم اخبار سه روز اخیر رو پوشش بدم واستون</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5550" target="_blank">📅 08:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سلام
من از غیبت برگشتم
👍</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5549" target="_blank">📅 08:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!  آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست،…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/5548" target="_blank">📅 13:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!
آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست، ولی ارزش امتحان کردن رو داره.
🔗
getartcraft.com/apps
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/5547" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lhmtgLmu7icVQEhTOoeQ7tilKJNRBKublXt519-NXpGv-WB03wUOxqncfWIgAVlGvtQrmyH4JLMnKfYfLPD6OpFxbDrqk9Q5c-OBV9dAeLLa7EmJQR3dIqqXHMjLLiu_cxYwoSPQZhhSuWf3cG0Nt0P5zSti08x4J46aewqqwR1l4WK6YAyebWlikDq3a5bl7tFWHrlI1fuRG3fPLczydI15Bt4DJxJbogb5AzeSYiHDgr29H_HlGyRuZjQl50nmoD7PVAOlZrVNs7T_roRhxah3DyDmtq2kHQvr9W1sKS4VC384hp3dhXKxmeleI4Mmnr_eJBM3bgKXrfnOWyWSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
ببینید چی برگشته:)) Haiku 5.5
خفن‌تر از GPT 6 Luna</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5546" target="_blank">📅 09:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یادم رفته بود بگم. من از اینجا گرفتم. تا الان مشکلی نداشت اکانتا.  توی رباتش بخش هوش مصنوعی، دوباره هوش مصنوعی یه کم دسته‌بندیاش درب و داغانه
👍
اما کار میکنه @OrcaSubBot</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5545" target="_blank">📅 08:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxniG828lliYP1mxaDI_M5_BrJwJx_SBp_BI-f5qXPDYle-QRIc-5OT3uNjkeiCGwfl4snI1QJjgvi__K_663ygR5NcpOYteG8ZiA4ATFU3ZbDdqDKpQUDo5aLHvjHzNSu-YQnRKDFScRAYuXZ1k-2JW1GErVmTtXO5D8R9u8L0UkOX6DpuKkpZ9QtPITXYdK_GW9N-oNtqTD-tBzfeGHUCOlMIHaz3_XJHTD2MlQEvYoMKSPfPnNr8k3aH_5yl9tqzIN_A-D5kYYIcEDK-q6suazXuZlXytPaCJ0lb_afSdVu77E9qroLjixSIbBlqYzu4RYOAc_JuHzpAbXHoYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابط بصری جدید ChatGPT
گویا اوپن‌ای‌آی داره یه رابط جدید برای ChatGPT میده که جواب‌ها رو خیلی بصری‌تر و تعاملی می‌کنه؛ یعنی به‌جای متن خشک، ویژوال تعاملی می‌بینیم و برای کسایی که هر روز با ChatGPT کار می‌کنن(مثل خودم برای چت روزمره یا سؤالهایی که حین یادگیری Rust می‌پرسم) تجربه‌شون حسابی قراره بهتر بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5544" target="_blank">📅 08:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5543" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCoreForge</strong></div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!
نسخهٔ مک
ForgeCore
از ریویو اپل گذشت و حالا روی
TestFlight
در دسترسه.
🚀
📥
دانلود و نصب:
https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید:
اول اپ رو کامل
پاک کنید
، بعد از لینک بالا دوباره نصبش کنید. بدون این کار ممکنه نسخهٔ جدید درست بالا نیاد.
ForgeCore چیه؟
یه کلاینت شبکه برای وصل شدن به سرورها و کانفیگ‌های پروکسی/VPN خودتون:
- افزودن کانفیگ با
لینک اشتراک
،
QR کد
یا
لینک تکی
- تست
پینگ و در دسترس بودن
همهٔ کانفیگ‌ها
- پشتیبانی از پروتکل‌های متنوع
- اشتراک‌گذاری اتصال روی
شبکهٔ محلی و Personal Hotspot
برای نصب کافیه اپ
TestFlight
رو از App Store بگیرید و لینک بالا رو باز کنید.
🐞
اگه کرش یا مشکلی تو اتصال دیدید، همین‌جا بگید تا سریع درست بشه.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5542" target="_blank">📅 22:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-7Wz4gpTjy7WrYw84YqqD5VPtUq0wSk1AHsxy8Hj_ztX0wzBvs2c5b0fsVlkoZJhAkmtUcBCc4fTddQBeAYsl7i3D5C05meC1mst8P-EQVcBC_ZSTcFCtc2Q74Ek3zAZAC5n7pvIwn9D5H-nc9LkuLvKaU4ut_lTvFCeUSn_Jr00WP4S1wtTfCBWm83dj51QVnqcGkMy4-4fOvx3PiH2OgoIRPciqd2FqQ-QLl1QUkLuWKYGcju9SQbkaz9k3JEyB7YvhzvDguLGCDQt5g_lNPhNLPrw828F2i8YZlGz2y2PuBHVgTEGgr4vLGpIK6q1d00XSJHgXFMcLTqSxetIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5541" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی
و فکر میکنم با ویدئوی بعدی
یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5540" target="_blank">📅 15:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم گفتم به یکی از بچه‌ها دوتا اکانت بهم بده توی پنج دقیقه بهم داد:) اصلا باورم نمیشه و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد هرچند خب استفاده‌ی دیگه‌ای داره کلا.  اگر که اوکی بودش و نپرید و اینها،…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5539" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5538" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Math lovers, check this out:
https://github.com/openai/math</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5537" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!  تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/5536" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135826faf3.mp4?token=USWkxgnQ4FWWCHYJ1wEsxSU3PWQJxuM09cCQEUD4ypaPSWZvd42daXLWc_d5oCkUSmb0lmEf-1ZXn3JFgKvLvdJnJB58xXvevc6plMJwUIZ9uo0S5-_sYFznv31efq0pRqHYEhS1MuW8y0JArUTlArRRFlTgiOnbXXaxC-NcUfw8YQarxNVbOZywpBP-s9-8aqmk4BV62AIGCtdRfLN00-stsgjCp35bwt6ZlsMzELr0ZHJUEL2y_nVYN7sbzOYt-I5DQMN0kcWyf46xCcQ1FIEhWqkTCa1Lyi5bjRlGAYAvY2Uea67U59kYorT3cPJPWKPtlj4KpM4oo57ZNhzumSwZcQXgedJOSIeSuXnRTHGzEk0ZQy2-vndWvrsL5-NduOP73HrjuvQjnRGa7Gx-BSKH8VCvT4DzM1ccts6nfmS2zeWihLIaXb_sFS6UoY9xDxiwxwasLRltVyrT0bCJB34h51IzP1NXKRnkJI6opsg60N4MQ1qIRklVajoVmkAkG3cH4d9xjyEGbbUhBi4X3S6ML3M5aL35Bx3Z8o8lhvtc6D-xHm__jAPldu8MBlphzmhNqp-2guUCponYsQBZbZ1ezd1EQKTlcORUDnbUjMUEwF0vjavAq1On4Ay8TW0SBjpwj3ZXyGB83m8T4guxrykRKbhylc5NJrneFwMB4Os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135826faf3.mp4?token=USWkxgnQ4FWWCHYJ1wEsxSU3PWQJxuM09cCQEUD4ypaPSWZvd42daXLWc_d5oCkUSmb0lmEf-1ZXn3JFgKvLvdJnJB58xXvevc6plMJwUIZ9uo0S5-_sYFznv31efq0pRqHYEhS1MuW8y0JArUTlArRRFlTgiOnbXXaxC-NcUfw8YQarxNVbOZywpBP-s9-8aqmk4BV62AIGCtdRfLN00-stsgjCp35bwt6ZlsMzELr0ZHJUEL2y_nVYN7sbzOYt-I5DQMN0kcWyf46xCcQ1FIEhWqkTCa1Lyi5bjRlGAYAvY2Uea67U59kYorT3cPJPWKPtlj4KpM4oo57ZNhzumSwZcQXgedJOSIeSuXnRTHGzEk0ZQy2-vndWvrsL5-NduOP73HrjuvQjnRGa7Gx-BSKH8VCvT4DzM1ccts6nfmS2zeWihLIaXb_sFS6UoY9xDxiwxwasLRltVyrT0bCJB34h51IzP1NXKRnkJI6opsg60N4MQ1qIRklVajoVmkAkG3cH4d9xjyEGbbUhBi4X3S6ML3M5aL35Bx3Z8o8lhvtc6D-xHm__jAPldu8MBlphzmhNqp-2guUCponYsQBZbZ1ezd1EQKTlcORUDnbUjMUEwF0vjavAq1On4Ay8TW0SBjpwj3ZXyGB83m8T4guxrykRKbhylc5NJrneFwMB4Os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!
تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه فارسی بهینه‌اش کردم و نتیجه این ۸ تا skill شده که اُپن سورسه و می‌تونید برای ساخت ویدیو استفاده کنید :)
https://github.com/atmirrr/persian-motion-director
✍️
AmirAnonn</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5535" target="_blank">📅 11:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کم کم دارم فکر می‌کنم یه نسخه از خودم کلون کنم بذارم هرمس جام کار کنه
🍿</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5534" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M4It01Rv5altxfzGzazNzqn1izvUfILIuYKqn8lgFqbblsBiT2_mcAJdfE0yXAMANPZ_4lDg_nFHSkLcM5mgtv33-jp3uItym-I-ZWdtpY1mKcw8L1vVqfT9yE3_3g6kijtmdSGh_39IKyVbeo1t9kKqmeezdyFyqpIIPgtcXKS_abeTJouQt27myVqTMc_bzSq6IAiEptvzco0m9DSqxh2sdzxHF9Oi-wcTrwFxaCGZs7-4hz_WhGh06b2l4kYg0nouU43mtjHw5jOvdDLvRMegk2oQeLaZGIIql-Tlug4T4kMbGoeatDAp7KU8XZ6sTIQ8L8FAEf7925Q7rn07nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن OpenChamber؛ یه اپ موبایل جمع‌وجور برای مدیریت سشن opencode
نویسنده این پست توی ردیت گفته بود اولش فکر می‌کرده پست‌های OpenChamber فیکه، بعد از تست کردنش می‌گه در عمل، به طرز عجیبی خوبه؛ جایگزین opencode نیست و همچنان opencode رو روی سرورش ران می‌کنه، فقط با OpenChamber از روی گوشی به‌صورت نیتیو به همون سرور وصل می‌شه و تسک می‌ده. برای کسی که opencode رو ریموت اجرا می‌کنه و نیاز به اپ موبایل داره، تجربه‌ی تر و تمیزی داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5533" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/emmN4AmHKMxDEWgyy91Job1ViWFtXJal2w2w2QR8oPcXPc2Du3F7kje281CG_2aRNnA_yRpeL1rE8NZQNxLbRnJYYUvgcxDNGdeQaHN3ke0Cy1JwIseeF9qPtv4bC3Sg-6M4RkIKAKUybo_UXlk014hYmVZOhTKc79VL7VCAdRk2k2zj5YffKHY-EPlM0eyEVCSFpoinbb3A2iyKWCjWU6E9ET-FLQq1F13I7-C8WcDVTZw084c-Zi5RVWGtVuwuKmHf9hYLKFEOinULhIPuLNyjSh_YI4a81CQjWa7sd-EBhXzrdS_0nC7mQm1AHhqkpVS4JDoClXue7doSr9p8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل نانو بنانا 2.1 اومد روی Google flow من، و افتضاحه. اینجا با GPT 2.5 مقایسه‌اش کردم:
https://x.com/MatinSenPai/status/2107527090019131503</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5532" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اینم کانال تلگرام یزدانه پرسیده بودید توی چت فراموش کردم بگم:
https://t.me/antimatter0x1</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5531" target="_blank">📅 18:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QZOBspbgdAmFBmHct6Wme8DRRRhEilRQZj9gI18Wlbh9ypc9dl7Xvm9l04BYaCHft0lL-8ZH1n36aIAmryt0lVr5zE4UlSdymctY-qw0xqJa-xTvQs-BHZWRkBCm8uszVbSprL2ExTZFT4I2_TT1suakGbS5VRe2GlEuOF6wrLyEiDxW5_OJ140jogElae-qV0J7TRAlJxrpmnqOiENU1BvUZd0d81cEx8PaUBE9cgfY1Eb0bc0ZR03027IHYGOpguky0P82ok3ltoxNdwTv-ZXiK9ooQ_81t8biRFL0VhEShG8krg3H-FDCaqPQklELzXcsRgGGBexhl7bNcgkCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو تموم شدش
می‌تونید از اینجا ویدئوی ضبط شده‌اش رو ببینید:
https://www.youtube.com/live/nbOls9zPckM?si=xnkhmSfdlmhENs_2
توی لایو توضیح دادم که همین overlay رو هم کلاد توی 15 دقیقه زد قبل از لایو
😂</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5530" target="_blank">📅 18:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/susTPyMFCfjMUB7RJFwMw_oHB0AtAfxlIdJFOT00zjIwepccnOvccfIyySEwJg9at3S_y_Wu-wJBwjSklcRGPcp3SBSuJpxaLPOaNBffioABgbcHDWTmY1kMvvu8JSIXhD_y5D08evItmindlFuFujXfYKDgyn0DZD61Ska14dakRkv_D3BOtem1heaT17K8tYQPS3JdVVh4Hk9-NxgLTv0DxCGuvwlipPfU2voYRUth5YOzGJR8TeK4EmDh7DDkQMfi9-ir4M3-4p93YKD8F5M2vTKIKa6M9hMaENjHn9Zze5HSQpxaAAf6x1B0IIPcNNut5CbhlnqA0bJRbIirew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Matin SenPai
pinned «
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:  1. CDN/WORKER with ECH  برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال 188.114.97.6 استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5526" target="_blank">📅 13:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EjEv-cmU8I1qd82KqNy6Rtomx6LJW1Cbx0mBBBdUH2kxRrv0M56-F70NjliWVH0e5WvJAU88NLSjWr0p34vB2G3WL0CxBCBw-gQC0i_cNMJDQi9uzx2di1K1adKKbYW62DRfvh8Llv--wkJ53TgS1OBm7e_kDcwCA5GDLeJrSmiFKkvQMkECc1ZFKVSxkQOhfhimA9Ol6_qXdYSIDuCXlA-LGVnPfQawQUonFATvG-aXh91Fx25ZJLOrgpZVou3nWJCGEUWJfMsZjLPBFcxxqOMOLmtqYpaL_6otxSY9yp273lAmu9odHRmAhGrU2dNchIQYd6ItvvLTW2-R2Q0T-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw6R-2kyb1Rvc7iWbf9xD4ccYNwT1YMHPcGrEfS95CJ_osI5KWwaitfaPOVVVv72mPCGXjOzpKJ5b2D4nCpcgD5rNOUa_rWFKwJge1Wxz8zWtPrEw_YhtNhVIji7XaNFI_T4qKECVU57GxuY3fdp-7WfYk3FeW_3fwZGYCBZ3hj0MI-I66_BWhDLRE2yDw4BhlOXzmV7JcV8UGzPQN0n87WzDVfq9beGjOIXY0X3jCKHN6qlqEblKpYxslWJb-kZcvVR-ZqzuPBhhttyJf_AKuGJFwyvb_Nkr3lR2inN56tlOugHNKwKvNGaI89RbI7J270YHgDjGGK9QOHlhAz9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:
1. CDN/WORKER with ECH
برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و در قسمت echConfigList به طور مثال مقدار:
cloudflare-ech.com
+udp://1.1.1.1
را وارد کنید.
2. CDN/WORKER with IPv6
ابتدا echConfigList و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و سپس از یک آدرس IPv6 به طور مثال 2a06:98c1:3121::7 استفاده کنید.
سپس در صورتی که دامنه‌ی شما فیلتر نیست، finalMask را خالی بزارید، در غیر این صورت finalMask را باید tlshello-0-len (همان مقدار متد f&f) قرار دهید.
3. WARP with IPv6
از قسمت add aether ابتدا پروتوکل را روی wireguard/warp-in-warp قرار دهید، نوع آیپی را IPv6 انتخاب کنید، اسکن کنید، بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال ایرانسل:
1. CDN/WORKER with F&F method
ابتدا echConfigList را پاک کنید، از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask را tlshello-0-len (همان مقدار متد F&F) قرار دهید و برای فایروال ایرانسل حتما باید cipherSuites را روی semi-python (همان مقدار متد F&F) و فینگرپرینت را روی unsafe قرار دهید، همچنین دقت کنید که مقدار ALPN را درست انتخاب کرده باشید (http/1.1 برای ws و h2,http/1.1 برای XHTTP)
2. WARP
همان مراحل فایروال همراه اول، منتها روی فایروال ایرانسل میتوانید از هر نوع IPی استفاده کنید.
3. MASQUE/H2
از قسمت add aether ابتدا پروتوکل را روی MASQUE-HTTP/2 قرار دهید، فینگرپرینت را روی semi-python و finalMask را روی tlshello-0-len قرار دهید سپس اسکن کنید، و بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
دقت کنید در برخی مناطق سیم کارتتون میتونه همراه اول باشه ولی فایروالتون ایرانسل باشه و بالعکس سیم کارتتون میتونه ایرانسل باشه ولی فایروالتون همراه اول باشه.
سایر نت ها هم معمولا از یکی از این دو فایروال استفاده میکنند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnjxWnIv9UYfhEFg_We3bK1V0voGC1Zdgk-o5ybiCmm1-xkETs5ui-rWc6Nd7YrhYKuW1jUNqzIpCEDU5C76FAvwiRikO0JAarT4nECGX53mcVnvNFrx3wLn3YOBA1xQXo51RWr_4RQJ9qZdzoWeTzrZw2pP_eS6lDFkm4jDObe7MMc5JcL83PoJ7TMIRBpQQ7Z5XVCHKBTJ1zq9Du_QzhyCjyuAOZxaqA5VLegdS-sNXiCSIyX1hgxg0AlNITmLC1H3lkBvigzF9PA5ygU66J7omlZTUjxqc5ixbqxcfPM4WP8kIAV6cgMsYQQICZ__CcOW5lvLRoKxjsh7q_eR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AhkH-BO3Pyl92R8l16ltIbjXR_2j7WKQi847oPeraeqviccYmA2huwQkkLNZPqARBv3dWfyCU0PL4BKTbamvMl89W1BJU7bgvVZvs7JajvQ-nAwRejzSU_3XvdDS3RbhQBYHXYlElKc7GrJpacA-80wHUSWFxuFMi0GrHqxJlFrk3xr5dOgfd2KGvJV8h-MbsF0y2H_rokNML6v-YThO7sakKX6OHNpsFVswq5Sk_UXEQ5o-H0Hcrqv1YZ-tA8X5t8tJUlHFBnm7Mq5FxbzkT0F9XLoVCiu2Qf3ngazhlX-VWVoeNnVZo0cemrYdk7wSgwPwk7l90qHA72sypck4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNb2rHPdzw6xADuzctBHJLYf8Ka5TMu6uI-353FOWSvsU27FJK6BlrltDOcdi6jBMVLz5mb8JlSAzR4WSTZLSBvdX9OT3ygUcwW0rOWJxZd15aQ9hvWSVh2gP_FSEaPuD0b6yGWiH4WIWSy4mw_GuBetYWq9kWKbIAyHmowWR8HavMKflZEIp9jvtCstdq485n9BKYa6nqzMdFjRtBWL5VCHDPYQfCIY4pCa-yPlqZBcDVt5o8vXwJ3rh3b2IpMntjwD8NAtgVSxgmvJzXvMJFfR5Tv4JgXzbQR7GD0zQ-28Zwv0bdLgF_taqBAq4c4DcEsCAv0BLItRz8Ao_JqLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHPdJYATP0AVXFr1RvrZAed241NZ2QyQNvn6Wa3GJVwsGtgFY0YRyLoIIc8fSWkM1h64qcz4SE-RONuoVGFaW7jttmCYqa6uomN9R4gF4PfUB2QROYoc7181P9Cv8fvoCIVo9MBiFjJpJTUuQ1Q8zdCeFhQ78X02rLGX4b-9nc-BzgbTjPYM3KwQo6RisC55CDLZq6J3uxLCzBtfLORH_egjeELQTgMDvNKITKwLd1OoRn3B0F_THUcnGRq0l5dqEMqPVfKDMaNIXkcrybp3kspz3WOwaYAhYROxI2gXBGrmEnrt7F-MmwdqtAEuViMpNTH0JQcQ48cWtftOWGZr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_yO3N8HSe5BUXP_A-z0W7-v_lHKDSmLPygAXYzALDxiQvGkdYKTv7ne7xQcOtBlzn6UC4vZoDKVpjtz3bwfC9AjRlYAQGgp0dHF9oNYXVGcKupcNhvIoF77xWDEEhXkZCOmVVVctcGyC3_RBjKXFx348exPbD91abc-XkGB-bkmKWRn_cZ-IrcunoWk6p3UtLUJ9n4Pz0-nqyPoI76sJraV5p6wj_8jsYfrD1gl63tF82FkAwnq0GPfFTerxyJBP6xgmPLtfpPTBRazhC1m7o_Z4KO8oah7yarCFdPp21DkqMlRtZKtiwCHbxAqdAWSFq7YFLyC4fbsI1pUhpl8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PWQ7gCwwHD-6TkzGZZyBiWyfOvdJ2pZJKlSeq3ogqABt1sA7QN5z2tHpZ97ABdNZBQ0tqwX3grfP6atPkvw2voMQo7iuAwR5D7kjrwbQ8XixZsnqTdGXq73a8HkmQ5VzFTkSP_HhmA22WQlhYyY_A_CKE5ZqCCPy2BnSTRmTGfYtXCRsp3gmj4Yh3XUvxAOJR110XqB5sYy5NNFs_c0eav_P2SbgVqne1oyxGGlRxxpmhcOHcODqQ08RIq_ebVcbTjAt7o1hUwot-UuwFpaOjiolNY48GUrs2qxYuDyPkfGLntfEna0V9Q8QCjGmW5XyBC9sPxO3SfXeWLFO4I6Fzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده.
توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل.
توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی وصل میشه ولی وقتی میرید جایی که پوشش شبکه وجود نداره، گوشی وصل میشه به استارلینک. یعنی همون اپراتور قبلی ولی با آنتهای فضایی. واسه همین اپراتور تلفن باید فضای فرکانسی خودش رو در اختیار استارلینک بذاره.
حالا در مورد ایران قطعا هیچ اپراتور ایرانی‌ای این کار رو نمیکنه ولی لزومی هم نداره حتما اپراتور ایرانی باشه، مثلا یه اپراتور امریکایی میتونه این کار رو به عهده بگیره. اون وقت شما وقتی دارید شبکه‌های موجود رو جستجو میکنید، اسم اون اپراتور رو میبینید در کنار ایرانسل و همراه اول و غیره.
یعنی از دید موبایل شما انگار یه اپراتور جدید داخل ایران فعال شده.
ولی مساله اصلی اینه که توان ارسال از موبایل به ماهواره خیلی محدود و ضعیفه و حکومت میتونه با ارسال پارازیت کاری کنه که ماهواره‌ها نتونن سیگنال کافی دریافت کنن. حتی توی مسیر ارسال از ماهواره به موبایل هم میشه پارازیت انداخت.
تفاوت این تکنولوژی با استارلینک اینه که توی استارلینک امواج رادیویی به صورت مستقیم ارسال و دریافت میشه واسه همین شناسایی و پارازیت انداختن روش سخته ولی امواج شبکه موبایل توی همه جهات پخش میشن و میشه راحت روش پارازیت انداخت.
من مخابرات بلد نیستم ولی اگه کسی تخصصش رو داره بهتر میتونه نظر بده که آیا روش عملی وجود داره که بشه سیگنال به نویز دریافتی و ارسالی رو بهتر کرد یا نه.
ولی میشه گفت توی مناطقی خالی از جمعیت که پوشش شبکه وجود نداره و در نتیجه پارازیت هم نیست، این روش جواب میده چون پارازیت پخش کردن توی همه نقاط ایران اقتصادی نیست.
✍️
aleskxyz</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zqc-0-BlaFgOe5FHskrDTx_QQZaaPuQpVKK_VHaFLf8kN90W_I1-Z5QELk-CoHet8YdDRyD_xdD6h5HnbW6wCsJ3K_rvbsoL5LA_uTYQOTaKisK4Z8HXHrhog9AOXQc79kjqd-zp9fF19-ojSitKwVPc3TyvDtkloIHM312pw_jE3mtlX9cLocQZpVbxdGEB4rQ4pnbTf17Clz-GMhNi2yAoRsCsuQtAgervAHLSRXGDDiHBiE-JT4nHhba7bgYMx1oE8VznAZWuN0Oi8zcIFicd1kh_uQ-oXcJwnipIuF36dE2JXVEDEWsFV6tkPwCukhAUmw5BGPMx3yCeROqN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RDdwGDIIBFEJ473V10yKiHs43JdQn5kAEg8PuRbqYZAZ6RrE8jLnYLG1l-OqIFlUtpd0uzBdMwYx_pEKAND8zmynwcn118hx4NpHdnG5m8xoCP9xdqluDyhOI2qFHCjLodszFKN6DCkNJjY7CqZrYZEQL8BiqXV-91SoiM1vzwLoakOu9TEWqD3tzQ2LVWncJ93qAlpjOJcaGSY_r9JL9nudqGnFShW8nhLnuOJJPCDyGLisrhjKowrbXlXVk-X3WUN_MWN3DnsZiXZ00Ski6KsQz58Udepzt7VdK4KGZuKz1YnoEhff5veKbtBYHfKHl2NIAacrhF2qMYexDUqKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uveGSpGBrnjvs_XbZxo3GIEY-U--KDCjrkQ66iguO_8Rn-H_OpQxTtiV-oNwVw0tCaDjENKcjLTBHyuUfH0yMlr25E32IvadnwjLf8CIZFMst2XDXFU7Tg5kI6gIf1JxjuYFNSdko44p8Nvr_2bebCseNYb7q7IHyt3lPirrOc0Pf1ADmCEJifukL3_UvwZQ8Q2U3YYHHsVS8sRGail7EsXEaUQCUAKnWDEGguPGnDuSJF12DkEW-wZkbKumejUf2MvkuWXQbB293ETQ2r5Si-d7vkgyf6szFItmdG-aufG_8L5AX2MImrKI_IOS6VTlp3eKnV5MgWBS7bYzZz-Rkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه SenPai Scanner v1.1.1 منتشر شد
"برای اندروید، ورژن قبلی رو حذف و نسخه جدید رو نصب کنید"
• حالت متنی برای صفحه‌خوان (NVDA / JAWS) و افراد نابینا(ببخشید از اون سه عزیز نابینا که درخواست داده بودن و انقدر طول کشید. این آپدیت رو به خاطر شما خیلی زودتر دادم
❤️
)
• قابلیت Anti-DPI: ClientHello تکه‌تکه می‌شه، همون کاری که توی PattNG انجام میشه. مقادیرش هم قابل ویرایشه
• حالت Gentle برای اینترنت‌هایی که وسط اسکن قطع می‌شن
• Paste کردن IP / رنج / دامنه و شروع مستقیم از فاز ۲
• ذخیره و ادامه‌ی اسکن بعد از قطعی
• اندروید حالا همه‌ی قابلیت‌های دسکتاپ رو داره(برخلاف نسخه 1.1.0 که دیشب فراموش کرده بودم. این الان 1.1.1 هست
😂
)
• نسخه‌ی ۳۲ بیتی برای Termux
🛠
رفع باگ
• تست سرعت مستقیم همیشه fail می‌شد و الان نمیشه
• و Stop بعضی وقتا روی اندروید کار نمی‌کرد
📥
دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
این نسخه‌ها تماما روی گیتهاب بیلد گرفته شدن(مشکل اکانتم به لطف یکی از دوستان برطرف شد) و دیگه شبهه‌ای توی امنیتش نداره
👋
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bU-s252xoSyyNzlD-oAGEIUkHXTiYg0lYoUux13sF_U2qv57GBJsF6QWWn5AjYz5HKu8ZSKiFZxMS0ycxs6DRX3JdzEUS7DC5EBIVhVxayQqm0TrF0FDUflk4a2ewj9jlY6IboSLo3_0OV6JQ0-9qP_MfeNjiQlwWEDUsS62YJUnhFWHIcVVHlcGEmTz-6IRRn1jd7v8Wel3q6GoPCRAWVkl2gy7A6k-qJ9bVrVcykm3N9DWwgjCnaXvsDopcRM66Pi9epUpIOPVReS7XsS3ssVtyEFoHICg7ARVE1AHsXamXLUOLKOmePjvcqZ7cjlEpjV336MxE-D_tBxXLqqfeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGj5zi6ZS1QoHKTDuDtNDlNUqpjVJb0GuFQRGoip8_2h5TNSA1Oxp_67zYKWuEOMfejmwOWFCjonuriK0vm6oBtm-Lh2iAsCkFa1DfOCsMS0CI0PUP9Pt-5wdGyzkBQbYGg91uhwmAqqL-tFVfqfr2DE6a1rm-a-Qujk43WU0pNRTxhCJ0BrRUAMp4d2d7x8jOmZ_XqrHwC22n_L2BVLI1Ph-OW2DqZgXtXLYwePm_1a9ihDCQVGZMEGbpWczL5QEw_9UEaT4DtFvvDc_1PuNhrChc8GlhmTDnLmoZGgung6ngHGwpZSp5LZr3y133MPAxLv-C6yqlWbqtKi-KWnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EjLG6DDpJWY5PmB8tN9NHAWs83Ah1ak_eg4rl0LBPFIn-CuaqlVjqIHB7R6dkUogS3vsOWrxudCRDOSqQB3ZZWdxDPeSicqaC7F7XLl8i30QDquvEudM3bTc70UGSvUfAF7e8XMONpZbdQezhHeVLOnOGb28JFUVz8bEIVINU1RHjpXa8pc_zOOPWcZfsML5C1Evr0iNCfhlbxd8oRbggWCxzuirKrm3_ouV1ebHez4ahgOrDcY593UCYyul6Cw0B6jlNEJz2LqtDGc9eGSiRXBczAOCJaEqln_Uyu3xn8BIQX1fPHe5yn7rEUbm-xPrTk_kFCt-oFMAZ9SAI2cEHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=OiyeeAdtEzXPPw5fobKXRp3--r5-3URA9ORPQKBcynnjTO4-1_9IlRPuEBj-FJCy2qUxxkXphOZxKPFiFBVN9X7txudisPqf4XYog43_FcHwOcPIgS__LmbQjcbqG6K08mDvXoTeOqrmkc4359O3ENtM1_GTPenv71Q9u9ewfkXF31JDmycVcSifCv8GZhbOtuVaYGp8iEOArjbhRlSmYUQsXZ-KycJIkLzLqSHIj1JsRn0C4hm_lL4JFWCpgWtfjAG0kY3Qnis9pV3_2gsrOhGuRzqEYZKCJVcXNntHvlaCyWGJf--URc6vUeaRzvMifuH0nupHjGbnovzicvtcJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=OiyeeAdtEzXPPw5fobKXRp3--r5-3URA9ORPQKBcynnjTO4-1_9IlRPuEBj-FJCy2qUxxkXphOZxKPFiFBVN9X7txudisPqf4XYog43_FcHwOcPIgS__LmbQjcbqG6K08mDvXoTeOqrmkc4359O3ENtM1_GTPenv71Q9u9ewfkXF31JDmycVcSifCv8GZhbOtuVaYGp8iEOArjbhRlSmYUQsXZ-KycJIkLzLqSHIj1JsRn0C4hm_lL4JFWCpgWtfjAG0kY3Qnis9pV3_2gsrOhGuRzqEYZKCJVcXNntHvlaCyWGJf--URc6vUeaRzvMifuH0nupHjGbnovzicvtcJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AuMRGmtIzstvy2n74sWziJS7VA1_D6R4dfHfVh3-wfk6FTARNLvJN3pEbqZ8w9jmY9T1mUKCNKSeXBX7NOwffaGDno635qXPrGn5oEQvMSEXHwUNY3u5WhbBfQ4aZEoKvGTOjnjoe9eaPE_Jxl8uO1joJnAzsw9SyCnNKkPkmwFFKkX39l7mD6ndvZoHcnswlCuHdgI1smQVCHoRmD8Q9hOhb7co2Ea18D_uBVki9MfClXdXcvKVYU5rTJrR5u_I57JyY3tQvi1C9WvW8IkWGpnFKNEZQaIMyr0kOuK4aTzGA9ooTAv2sft9grBsDeIFkvtmtTu5-nCvAEmwcX8Gcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rv6lmiVefcn13PJLoZDyRx9f2Os0vEOVSude58UT2LKqE8ZwCcwP636M1zeuC8SYuclHSIejobN0_3fKrl-UXHRgwWE4iSF8kb_-4R3hq8F5P91qRqf1TELUZH4OSVVrzeQ4_V8DEBgrKzyy4ZZTLGPyKwa9OjVmfplib3QdBryrO9f07JvViXKqq7tyU4hXd7oS8dpznoLUSL9Gob2iHT51hT8XvYhGSEGhTEJ6CCl4kIVHnUXLk_eU-SN7895baSkMNppeyB23Ipm3rYHmKrQZ6PZ3Ib6HQbNjLA4QaIInORGWvSi_-H7m3FAc1ybMukbeG_N7L4QLk-auohdSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pVMTLViNXjosIfVZhyH1mUbB2QxC5zNwgCxhOfQadSMZZ7AAJ3pUgkY8o5ca_d6X1lzPTkmqENsrL2UOwqNtSH2EITX-kXZ02Jv00cYO_iZgvK4wtkeeTuM6la8iw7wS-79_MzI8Ys2N9i2-La9pW8z_m1IVG44mY6a9CQ47EgBbb7PWxCwhe3T3oonhywCFZR1Wa4HM5yfRxVHIOOqcukVeweOxbP96reeHZXaiiCJiCtUdgiCqa31cOvWnfZb7ApmXmrQdAw1APwN8U5ctNw8GwwHWNfjwjrQUn0jUWC2gkLFOCntHBvaHmAtjPMlcBRcw4VRvUzhm3EhyZxD4qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aPSThji49m7OTz-lTI2K2pzDWws1-46M4OSO1_96goiSKUA64oZHaGbSIlLBlhv8shVQ1oH_ez5l9CeDfaFmdJCqiqVtvNMKPbBYQ_N3tX3zsp4KaE1IXICeh1qPLw4uzQ8N7Gt-i2UXiHPU2Zd0YW44OLb4Y4FEz8o7J1tgjXNW3pNB2gytutLkNXVX2VyLG1lzAFqf3u2hdCwuMRoASbYtH_QrWxAwYhT8qsKGLmk0TmWViaswt2b7-egVp-l4ruB6kmTaU2M435jIEkSRRWR5tMQ8wnKGccKuKG0QQV0KHAUritAsdaTXRLkRZTotIqcNYN4slOrJ_s__qt6Hmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPiry-IdZ-1K3PCahrDACOGfA4wVRxHEe4qzlijn-cyQJf-rKExM4yK-VCffo3WthspbRFDo487mJngWhMkZ4UiM5hODBKhXJn-O6Fz2Rs6Z28xTcxJoTCJ3TywY4IK4qbJtah5AaQzXKWMV4Ym3yPf6WijCtsaICcLKV4M1yxFTK2NGWIfSIiLWIY25762Acc0ZfdpgnIhpgrVeVR3MFKdIST2xtW-aAadLCe3CqZCm0LB5jME6fRtKA02GNWwOGQS0mDSFzXUCIPZIB-NTHubtBbeikQCkMtth0NPWvu6Fa-Oe2vKG2ydI9aAx0kILHHglw5lrPUSLhMkY8KT74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lVv1egZNi8unfG5Ub91Tu18BaTvT6ZhNioCq2kk8BOvKPqQlsJapocD-ZX3-RqM0NDOalXbnTu0Dcei3lE74vbvysF5P3cTws-KyQpzMlIpEBA2lHHH_FORHZl8Leu86mVU2iEZ5GX2net3MggegXOgym8AFoboS3WVjMIRFDSaqPpbCR6RdB7-_5WNGa5VdPpnpeTSoXGQbT3c6X9QNQcShKZ2ISpS3u2WNQ-MEVKRctP4li6J_sLDuQKBVa55aDW3nt5fIb3DJzAFssmt6brC7J8YSrPDTNXUdbz3YX5hWSgHpoxvy2o9SIlxE7Ef6c_EH4SXhL-Urv43TukyRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx4pfSPU5RPWSUM_9kS1tt93P9cLlB0UOVSt-Z1PS3hpCOFLj1zauwBPKZTwXgrZ1-l6fEuM6nc6-Y4qKQbj-Ec5_GUef077H_wNLGy-bSnQEsy5AZnXNv8dxttvjKr4qJdlSXoesni1lq9WiS6GHqkQeD2LwD7mAR6O_3cTLpFWSGpEaieFExT9tML9Y5D2j-EKi4btAjQM18ZPLDUOt7xk9GfHrpQk25pjndkc_xekSBwfalKF3N3efRDrFEd-VaL0iS1btWvGO0vai4dwDMXoMv6h6ii2XJoL4mboCqN8RGQG3Q8nWL3kN1g-sC5MBY-Hpm6JQ4WzKIUDce8MLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j61fVCad6xMkKXYa6KZ_JyzzN4R6xSN96QOAfSJ7m5RbfBAFz5aRB6l_QGfRzdhqf9sTdaJ3BZxmg80rEI6n9kKd4lMzYP1nsiKwgVNUYcwldMYhW0JREByLmcdNb5i5IkfD2-p7Yn1g5nR3bmYkXCBdfdbJZ7khCx2xLJcVsoacP0e3dMxWXLisMHUFX7-QEHS6n9VvrPMdkU0jX2oquu68Uf-Yak3FNf-KhWTcS-_fxPyramaLXFFgC4-XsSLdqHtCTaY-ccLltzCG4J9dHIhaZHFmP1jICTue-ZYhsgefKXxgQofumChUtCUxA_z5c5hx4lP0oKchoOEA-l2xnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WHJkVE0lRdLcaVoeTlYNDUa5omIl3s96YleMlQ8nJFiK1Ma2A6E4Ts9uehQvi12alFd2AStRWv_T9UdAIn0RhwomoaKJ3Zyj8s1XTMUENnbFsoCP0A4RvJHo67e7GVnIfMA3q2zNzqsH5jKAe-QZIwmNb_-4vSMV3nsz8ndmWIcyxZtd6zc2hyaN7ac61bQtBGWPY2KQ9_8BeWZNkNX2hWgX-kwJwizCqTZNLyil4ZlVhHjaQIjLi9PDHvvo3xEN3w-3cy_6hF37SxomZGfOTUN_ZLAPOZyBpfaz8nXe2DM_gTc1EdLkSCGplMDcKREEy5s2o7BSfm1ryvB9_86dtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pa1vGs_UFYi4kZqNAbHryrEglPwLxfjZVGa1AVhEzx7gP1mwK2trgCzvHV-REH-piTF29bnIEdv0ZkPogszUMYceWo4OLQ-xISCBvuUN6Ctmn2OXRBAuWVXx9m1yWliNn3QPQkfHBmhourrL3W_sntRQbDstAEicnZs2CM0T29tCPPLh59-8iJnroca5wqhxzRj3XktvJ8_kOXQ0SEgz04oKd0iMyaEzAWuzDvK7loaj0el40aCFnAWB0SGxIiIGQeUGSlZI-iF3n1gsBScKTDToKSeBfnFPETVEZ9v1crkrAKE29OZf16XRBBieFQQbYlJCVOGWdbF9VDhEiw2G8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rBn7oeWR1ECdEtVKg11DgT-p04JelB9XKk190LO_I2pMDedy0KjGW2yFj88JtGueBVR7b5IpStf5-zO09WBjBtm9197kOZcsqws2SZXro525q9JM2YcZvHZqv0D3gSrF40i3Wy8LMfRdj9poYEc42UjP5M5DlB45dH8SqeMp3_uYlQb1e48gH0CmDEx-FRs-0aucbUJd0iQ-7WQXrqWTGYvtXyRx_aqYE9IxPKryIT36FvSYi5aXJku2OHId5xzZqFEkPQ0T76vJy3wkRvrcjBeCWD1isoWGMTom9hldyJoFidJvxZ2Ncm39_Y8uC995rDi_9Kn8luwqt-HfGFM3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4Gdx7C_1xkKyNkYMefHkcvtammqZesr1iUrdzUKqGFYyjnLjQXfo0PkOI9j3SLLepQtuYhSDiwOBsd9m9gevwwfn8TxZ9Xl5EGHoaP1gGfvaGk28mvzeag6UqhWdFVd2OyxVFhwfz9VRPn_IO7e_U1wK8bv1j2Z699gRevR5ipDxFxUMat72tz3zpHOCKSJcaeUnflIrVattFnsuK6ecvycoYh4SXmXNNvGTN4pWzlWlP9BayH-lntNr37FrzNrXohTIX6qbJdiJgir6RsNkX0dTc6T-U6tN7IoUaPx10idjtC7sKhZuGa2Qk628mfwFfO4UzN5Dl6iezePFL4HYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
