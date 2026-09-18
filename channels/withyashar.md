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
<img src="https://cdn4.telesco.pe/file/qtnyVtT-yZbSj8UOWWyqf0Lz7I9tsG6ykdHA0RcW0_Rf6setvcYAh-WuGxmaFvu806PtWtjDzIJpXWsNppDojqwX0njv3XcP1qdvziljo6XJdP0MQLw99_oJm3sekGxUtVtfUmEupov0iJ9pNaxoHCuOdu-M6ViGcrYPQNYEuWFcfA_0TL743xWje5V5A_G1CuGqRC9JILknkdm0NgPHRnkcRURxIPUCfYL7nb0SoVWK9cGlAvG1hZ_niOqkOXVSJvPNZBiPwhKudiKy8HPN0WPL7bU5M36eLg2eV4lSrRlbDFnp5SZi9fBhcHVAg7yBD1qYZQZXY1bxDdpJpiB29A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش فاکس‌نیوز : دونالد ترامپ، رئیس‌جمهور آمریکا، در حالی وارد
هفته‌ای سرنوشت‌ساز در سازمان ملل
می‌شود که موضوعات ایران، چین و هوش مصنوعی هم‌زمان در کانون توجه قرار گرفته‌اند. نتایج یک نظرسنجی جدید «فاکس‌نیوز» نشان می‌دهد که ۷۱ درصد از رأی‌دهندگان معتقدند دولت ترامپ فاقد راهبردی روشن برای پایان دادن به جنگ با ایران است؛ این در حالی است که ترامپ در حال بررسی احتمال انجام حملات بیشتر علیه تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/23462" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فایننشال‌تایمز: ایران برای دور زدن محاصره دریایی آمریکا، انتقال بخشی از تجارت خود از مسیر دریا به مسیرهای زمینی، به‌ویژه مرز ترکیه، را افزایش داده است؛ ترافیک واردات از این مسیر در اوایل سال ۲۰۲۶ حدود ۲۵۰ درصد رشد کرده، اما تأخیرهای گمرکی و هزینه حمل‌ونقل افزایش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/23461" target="_blank">📅 15:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آسوشیتدپرس: چندین هزار نفر روز جمعه ۱۸ سپتامبر در تهران در تجمعی حکومتی علیه آمریکا و اسرائیل شرکت کردند؛ مقام‌های جمهوری اسلامی از ثبت‌نام بیش از ۶۰۰ هزار نفر برای آموزش نظامی خبر داده‌اند، اما این آمار مستقلانه تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/23460" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شرکت آرامکو سعودی به پالایشگاه‌های نفت اروپایی اطلاع داده است که در ماه آینده نیز هیچ محموله‌ای از نفت دریافت نخواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/withyashar/23459" target="_blank">📅 14:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتانیاهو درباره ایران: اول از همه، ما باید رژیم ایران را سرنگون کنیم. این مأموریت من است و این مأموریت اصلی ماست. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/23458" target="_blank">📅 14:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز:
کره جنوبی اعلام کرد هیچ نیروی نظامی را برای ورود به درگیری خاورمیانه اعزام نخواهد کرد. سئول در عین حال در حال بررسی راه‌هایی برای حفاظت از کشتی‌های تجاری، مسیرهای انرژی و شهروندان خود در منطقه است
@WarRoom</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/23457" target="_blank">📅 14:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایلان ماسک: «یا باید ویدیوگیم بازی کنید یا احمق بمانید؛ فقط همین دو انتخاب را دارید.» این اظهارنظر در واکنش به پژوهشی روی ۹۲۳ نفر مطرح شد که نشان می‌دهد گیمرها در عملکردهای شناختی، مشابه افراد حدود ۱۳.۷ سال جوان‌تر عمل می‌کنند. این مطالعه همچنین ارتباط بازی منظم با عملکرد بهتر حافظه، استدلال و سرعت پردازش اطلاعات را نشان داده، اما ثابت نمی‌کند که بازی‌کردن مستقیماً باعث جوان‌تر شدن مغز می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/23456" target="_blank">📅 13:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E39BeoMu6ifcpcl1KY0-bqkWIii0LGM5Evrbq0xxNOT_unLaix2c8kezOPsMb0-PbGbswtJlzqgTwN65C68ekVROf5KyIMCIRMcbY02IUg7Hs-LpZUTtbNMTSWv-BPQiahd7dkHbDpXSDliVdaPOFwaStY2DDqNrQAEdA8KL2xfTSipE_91s6QujCB3FanJQPKtm0ZAlHkfprT1tVYRKH3RnN8hfjowSSISJTqMCc_S0WYrK9AVLRKr5pwq4oy1NIPo__RLkeXq1zUHIBar1y-xfj7VZFxTdR65y60RB78dSwBl6pbOzZikt2Pr4EzBFBZM3dMDoLm_zi3OMRFWo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود شرق تهران
@WarRoom</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/23455" target="_blank">📅 12:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جی‌پی مورگان: بیت‌کوین می‌تواند از طلا جلو بزند؛ تحلیلگران این بانک می‌گویند اگر سرمایه‌گذاران از مواضع دفاعی خود در
صندوق‌های قابل معامله در بورس (ETF)
بیت‌کوین خارج شوند، احتمال افزایش تقاضا برای بیت‌کوین و عملکرد بهتر آن نسبت به طلا وجود دارد. این بانک همچنین اعلام کرده صندوق‌های طلا بخش عمده خروج سرمایه‌های سال ۲۰۲۶ را جبران کرده‌اند، در حالی که صندوق‌های بیت‌کوین تنها حدود نیمی از خروجی‌های قبلی را بازیابی کرده‌اند.
بیتکین در این لحظه از 78,000$ عبور کرد
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/23454" target="_blank">📅 12:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOxWL8I5S_QJ1RovUCMqGBBI1bloW6bRJ6Z_NZisPdESPegMvTc8sr6bn-z0nJt6HbDUTGC4Hh9d_GdnRQQiowp4Rhvr3S3pMEnIpwVOuAyzRtdeYTQXQb31MxsEhSUkaJkJNZZzgEqn3oG2crn8gOd7Z9Hyx35_ZZb9Ke9mf5_m6dJb5Pe1trBDDVMiqPzhtlDhakvgBOfgg93njPTFJvUVVdSXOkKRKovQs80vRiTmbV8O6tBzTIBeXjlPMKI3xnkatoRAbg1Azd9NiJmHFr2of2OQUoMqvZFRTG-eRn3RjTVkQyvuyIxBs_eaxixl3jHkapuax4RRgg3T4Zf41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز جان فدا ریختن بیرون، رژه میرن. این وسط هم دوتاشون مزدوج شدن. قیافه داماد شبیه کندفیله(یه مار حشره خوار) نمیدونم بشناسینش یا نه
@WarRoom
😂</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/23453" target="_blank">📅 12:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmBx5veCML_XFPl-oQ9AvGs3AavfGBQyc9LjyyK-4pg6dboj1_IqSNRfp0blOlBqXneJ3_j7I8CpMGRl0aiqvV-Vn9k_Yp8N69_hV9r0b4pRcRwK0NpHJ_XlbOcFMFYAQgcOMSJGpKJtlZp-OEc05g2wIIItkjYpO23vG-oIglJto7EcanHyQtu-l5zavXwbNYK7uuMIoJwj5a1B9tG1Ql4GCcoTnLo8KNndxAjppiY9BSen_Fb28147iTDEbexiD_FfF-I_N03nPN5KQQLkXMfuhcwbZxqV5-ZiRbTxPpjIvPbRL7yaDMLyFD-xr046RP2n88W-8897pUyY0xtRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSIMcxE06CHJAv6ta2ZzYeUtMERGQt4tAj9VaPd63r8nqL0tBngDs-T4yV8KAlzt2djcikwWY4ouIgaQDTPPyOGnq8X76t-CLy97XxpmLVevbIFMLranZ3UvQDhsiy1DaW74tO6Mh4U17guk0VnmwiUEtO6zKBRMnhYD5zXIYtMIVqUO2KUxSKAI1Cn8fUGZhRnGCxKs5izWm1wNhSZKuZn_FmcksSwMh2zbvz6GgtH1QQckNBMYuyqYF5S-TWkWl0FT28WrWGiT6ppD1z68DUeWnbgIcMpIq4qB6U05G9PC0nMQCqiqfp8kkay8yfM5e64mLr45v7qTV8BtME6b5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمله به سه نفتکش در حوالی تنگه هرمز
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از دو حادثه جداگانه علیه نفتکش‌ها در منطقه تنگه هرمز خبر داد.
حادثه اول: طبق هشدار شماره ۱۳۸-۲۶، یک نفتکش در تنگه هرمز هدف پرتابه‌ای ناشناس قرار گرفت. اصابت پرتابه باعث آتش‌سوزی در کشتی شد، اما آتش بعداً مهار شد. خدمه سالم گزارش شده‌اند و میزان خسارت هنوز اعلام نشده است.
حادثه دوم: طبق هشدار شماره ۱۳۹-۲۶، یک نفتکش در هنگام حرکت به سمت خروج از تنگه هرمز، هدف پرتابه‌ای ناشناس قرار گرفت. در این گزارش، آتش‌سوزی اعلام نشده و جزئیاتی از میزان خسارت نیز منتشر نشده است. خدمه کشتی سالم هستند.
حادثه سوم : تایید نشده دیدبان های اتاق جنگ به من از حمله به کشتی سوم هم خبر میدهند
@WarRoom</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/23451" target="_blank">📅 11:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZo8_IXePw5IwmVyrYWUYV5fYiPn4UjlDQuEDJnNn-2zJgX_68cunGfzHw6flqgG6fbiwE5HQ0J1uHgukZqctm4ui6CatvjfzBpobn-CcQnORfQHAoGSJ7lwKyUsVxkPd-GPJFcbuRk9V5BQ4mPyMzYaf7w6gGLLNxgGCqwAGDjed5pG0zifFAGzFU56ZGZ3r1bCw4uRqo7W3D_58OgAal7o9iFXD-cgsYTVxqNVU2gw3d7lIiYy9Ikpkq0J9EB0YOxNlMtDaX4X1NcBut_9EmWaIZuWo00QFFQTj5Wj6R6_uTfggPOoh8gGaAkSwyex1jBw85ST6mltrc4rvC0OiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌ با بازنشر مقاله‌ای از واشنگتن‌پست درباره افشاگری‌های داخلی پیرامون جنگ ایران نوشت: «خیلی جالب است. حتماً بخوانید! به افشاگری ادامه دهید،
سگ‌های کثیف
!
وقتی شما را پیدا کنیم، بهای سنگینی خواهید پرداخت!!!
» مقاله مارک تیسن، ستون‌نویس واشنگتن‌پست، استدلال می‌کند افشاگری‌ها درباره هشدارهای تولسی گبرد، مقام‌های ارشد نظامی و جی‌دی ونس درباره خطرات حمله به ایران، به‌جای اثبات اشتباه ترامپ، نشان می‌دهد او برخلاف توصیه‌های مخالفان جنگ عمل کرده و تهدیدهای حکومت ایران را جدی گرفته است. تیسن همچنین اقدامات ترامپ علیه ایران را یکی از جسورانه‌ترین تصمیم‌های سیاست خارجی یک رئیس‌جمهور در دوران زندگی خود توصیف کرده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/23450" target="_blank">📅 11:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23449">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقامات آمریکایی:
ترامپ در حال تقویت رویکرد متفاوت برای پایان جنگ اوکراین است؛ پیشنهاد قرارداد تجاری با روسیه
کاخ سفید در حال بررسی امضای قراردادهای تجاری با روسیه، حتی پیش از توقف درگیری‌ها ست
ترامپ می‌خواهد انگیزه‌های بیشتری برای نخبگان روسیه ایجاد کند تا برای صلح فشار بیاورند
@WarRoom</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/23449" target="_blank">📅 11:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد ایالات متحده رسماً از
شورای حقوق بشر سازمان ملل متحد
خارج شده است. واشنگتن این شورا را به ترویج «ادبیات ضدآمریکایی» و اتخاذ رویکردی مماشات‌گرانه در قبال حکومت‌هایی که به سرکوب مردم متهم هستند، متهم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/23448" target="_blank">📅 10:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP9uko7PXFoXZaVaDMhr220GArqw2gtzQl-RRt_Nkcn2RdK2YBacNaK5SmGMAJ89rpmUEBULKvvWuTAWBZC6ip7R2x7P4BHx8MPv05RFJfJ2K4HZXM77oeSRGHjiO6tmI-JjOkKEv_eb1eYtMUlOIVAFBw5aYLVysbi6jLcRARV036ZuhQBM9J_0KuXMpRuet00u832YtQOlRo4ryt7n6d2k-AFHJfhIIj4AuwP9Oc9MYl4NfUgf3ioOToXNxjL7JeIByUmIgpHxl5UrPorFIhCTvTeAeixPY55QoaCRxuDces99aW8wmB11CpqmbO5DXwE8VppUThaVzi_meR9P4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoUslWiFeXUD2PjI06PR0NRPKRS8sMKT5eSwYJzOvICqniIf_daCBBErrggmhiR-S_O_gWNJbojwFqrKiZLOeZx6bltNQt8SIO5Im-oFb5dpUl8oa2uY9fhj_YaJmcREFLgKXkOJErCdsc3S6O9nd3VrWQwHqMBpRdeIh9SaBSk5Te8MWpuNP3rHKouzPUYFFqydCtGGyffxde1mr2J5uvFE29pJ8ttWTglLuui8fpnweL325vjGFSVGy3HknDETBVq5PhyjQa5_OiySjDczNmXjxz0cMqr5LnC4GOn-BwaqqPOuQIrBvwXzLGT8NbhY72kQHgZe0CXPdajlvdpAPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANvILlCG3HC0nsJe2VoJMF9RifBoYLZS2WlT412-YkU1SMKxQkeCFWXrlp8WgxmwKMAjXgtoaWHrWa98xEtqIZpLF1TVNWlRvOvne9CTQ2-Ihg9Ya5jpIf57ybbysl79zbQ18fRS0EWQtmGc_1dZrJppdQ8NQS1FYjOBhEgNtA5vRa4SdU_9f0PGoY718hiW1ouefNyK6SPtF6B654afYceKrCThPhY0e_OGLBpRsp22pDU7yG-2snodgI90FSmZiLpXkCxEarhltIEOHAG3OVLYHrD2AdvXb_qYUj01faSCG0ZbG-Fj611fh1y-kiT0cB7lYJL8z-GNMfaSN5Jfqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NO25xhoOtUkJ-5GD30v3_sOqZl4cKgkp7096RBFmK2XtiYsbbVJK6_4_pQSrFdYdKpez8p7w1YwMbt6FJtfRrIHnw_hEGOqk_MU1e47SugN45S_YQFqVSXHQfsr-TRrIbsr3B7lTqinYEwSRtn4LhAx0ae6Wtw6y86am_0Vwvq84ojp1fQw-ZbqJ7vkt29SLtgDcoW631cw0CsuF4jBHFAWGyj4-e8O6HP3oGoi11H_BoQlgfdSZGcwrljD5L6o0RsgPME9c5f8LV28PSK7wXg4PhHvslvueoU7W74XBIZChnVROqLRP1z9D1N8Eu0vh52n9RNmQv-3iIVCOdD9xkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آسوشیتدپرس: آمریکا در حال تکمیل خروج نیروهایش از عراق تا ۳۰ سپتامبر است و یک مقام نظامی آمریکایی گفته صدها نیروی باقی‌مانده در شمال عراق عمدتاً به اردن و دیگر کشورهای منطقه منتقل خواهند شد. تجهیزات نظامی، از جمله سامانه‌های پدافند هوایی نیز از عراق خارج می‌شوند. روز گذشته گزارش داد یک کاروان تجهیزات سنگین آمریکایی شامل خودروهای زرهی و کامیون‌های نظامی در غرب عراق مشاهده شده که در حال انتقال به سمت اردن بوده است. جزئیات دقیق نوع تجهیزات و مقصد نهایی آن‌ها هنوز به‌صورت مستقل تأیید نشده است.
یک مقام نظامی آمریکایی گفته خروج از شمال عراق «ریسک ما را برای عملیات‌های پیشرو کاهش می‌دهد».
@WarRoom</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/23444" target="_blank">📅 10:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مجلس نمایندگان آمریکا با رأی ۲۵۲ موافق در برابر ۱۵۴ مخالف، اصلاحات سنا در طرح «قانون تحریم روسیه و ایرانِ لیندسی اُ. گراهام در سال ۲۰۲۶» را تصویب کرد. در این رأی‌گیری، ۱۹۷ جمهوری‌خواه، ۵۴ دموکرات و یک نماینده مستقل رأی موافق دادند. در مقابل، ۶ جمهوری‌خواه…</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/23443" target="_blank">📅 10:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک مقام سعودی در قبال تحولات یمن در گفت‌وگو با شبکه ۱۲ تلویزیون اسرائیل: «از سوی پاکستان یا ترکیه چیزی جز اظهارات نرسیده و هیچ همکاری‌ای صورت نگرفته است. آنها فقط می‌خواهند سلاح بفروشند.»
@WarRoom</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/23442" target="_blank">📅 09:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a920abf92.mp4?token=N2b9PQn3oL6eBh3aKVBZJ47iOzWUFw9jCgcXQRHYHmnQvBYoZoinlvEFNT5HVhUtjMKQnjb9P5oMpxsriy5i-iF2CG21ZtKc08DULaktQ9gKznpK_QGUalAI4uWABr8d4OG0HjP9Nv5PHQz6CLVueG6aSdxZAbupv-tn1biVbThy-B8NOb8ZFiNC_wln87piY1SHxSTVY19hYgorw5IKfx7y0KWOlBsUJ9QeLBe10o9LsDwRiZmFWfvZ7X3zlyQzmeUlJV5n4ppR4_0gvTwVh5Rd3XwRXj2Q5Ezm0I7WTyjQFXdHjTg_87r6pzczEOuL_-EFWUeciDr4BFZD3hQ8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a920abf92.mp4?token=N2b9PQn3oL6eBh3aKVBZJ47iOzWUFw9jCgcXQRHYHmnQvBYoZoinlvEFNT5HVhUtjMKQnjb9P5oMpxsriy5i-iF2CG21ZtKc08DULaktQ9gKznpK_QGUalAI4uWABr8d4OG0HjP9Nv5PHQz6CLVueG6aSdxZAbupv-tn1biVbThy-B8NOb8ZFiNC_wln87piY1SHxSTVY19hYgorw5IKfx7y0KWOlBsUJ9QeLBe10o9LsDwRiZmFWfvZ7X3zlyQzmeUlJV5n4ppR4_0gvTwVh5Rd3XwRXj2Q5Ezm0I7WTyjQFXdHjTg_87r6pzczEOuL_-EFWUeciDr4BFZD3hQ8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي:
فکر می‌کنم در نهایت پیروز خواهیم شد.
نمی‌دانم آیا از طریق یک توافق‌نامه باشد یا نه، اما ما از همین حالا در حال پیروزی هستیم. اما فکر می‌کنم در نهایت پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/23441" target="_blank">📅 09:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a3d694c10.mp4?token=OKOKrRKcw_sbI5HSItOCIjHHUr2pzalchJ5ob3hy3gaebLf6NLrfKD7yt9WYifZN0osr8suVWJh2TDljP2_t0yzRRPrf2tqrWfPXTn-2AVjY4m6Tah7iRtvY_cKeoGiWLGiIhPV8k8Wz7_0xoKNhUzunj6bZnEFTG3aMz7H4WxQOvrBBAWYdJr-AkR-lmy5JgPr30OvPTB26kxNm_PJTjSpu0veo3OSScH4H-9bk_ZeGnk2pefotcDFeszgIf6Azyj_tgNizHfqwS7CQ6cAUv5dOQ3lrtgK5boB5fjzOVif4TZuvTpQXKU5Lq6Q_YKe4yVT8IIgqquWI1aQ3UKB1Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a3d694c10.mp4?token=OKOKrRKcw_sbI5HSItOCIjHHUr2pzalchJ5ob3hy3gaebLf6NLrfKD7yt9WYifZN0osr8suVWJh2TDljP2_t0yzRRPrf2tqrWfPXTn-2AVjY4m6Tah7iRtvY_cKeoGiWLGiIhPV8k8Wz7_0xoKNhUzunj6bZnEFTG3aMz7H4WxQOvrBBAWYdJr-AkR-lmy5JgPr30OvPTB26kxNm_PJTjSpu0veo3OSScH4H-9bk_ZeGnk2pefotcDFeszgIf6Azyj_tgNizHfqwS7CQ6cAUv5dOQ3lrtgK5boB5fjzOVif4TZuvTpQXKU5Lq6Q_YKe4yVT8IIgqquWI1aQ3UKB1Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي:
هر جا را در جهان نگاه کنید، ایران به عنوان بدترین کشور جهان شناخته می‌شود و مدت طولانی است که این‌گونه بوده است.
ما کار را انجام خواهیم داد. آن‌ها در وضعیت بسیار ضعیفی قرار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/23440" target="_blank">📅 08:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f45e1be2.mp4?token=lCdA-X-ZEG0fAFUzA7VH82EnN_0tpbV1RshMv8PZVzSMxi-HbWD_9BGmpeANnU9LgBoKW-HR83yN1LtJYOvH9h23tMXpsU43Tt9mftQ61g6f4DtpQTloT-o1S2OdkpilCF6svuO1EJxKJlHKwQy26iV5GC6ntz0sBPRGjEmUSki80J2uke4OFO6UCLcto2CogQocJGfOKFI2OGO6aTk4OUnGA24WrrhSeHuQPagbLY6JaCcTtKfpc7sDJn8vw9AKjDrfLDJki1nbV1_U78XgzU6i6gWGnpKILneV4LTYw6RDYU4L6tM5i1qTkw87ydHUbhOvjxJLNA3UZTQCDLwZjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f45e1be2.mp4?token=lCdA-X-ZEG0fAFUzA7VH82EnN_0tpbV1RshMv8PZVzSMxi-HbWD_9BGmpeANnU9LgBoKW-HR83yN1LtJYOvH9h23tMXpsU43Tt9mftQ61g6f4DtpQTloT-o1S2OdkpilCF6svuO1EJxKJlHKwQy26iV5GC6ntz0sBPRGjEmUSki80J2uke4OFO6UCLcto2CogQocJGfOKFI2OGO6aTk4OUnGA24WrrhSeHuQPagbLY6JaCcTtKfpc7sDJn8vw9AKjDrfLDJki1nbV1_U78XgzU6i6gWGnpKILneV4LTYw6RDYU4L6tM5i1qTkw87ydHUbhOvjxJLNA3UZTQCDLwZjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
فکر می‌کنم در حال فروپاشی هستند.
می‌دانید، اقتصادشان در حال حاضر در سطحی است که هرگز پیش از این ندیده‌اند. بدترین اقتصاد تاریخشان است.
تورم آن‌ها بیش از ۳۰۰ درصد است. به سربازانشان حقوق نمی‌دهند. به ارتششان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند.آن‌ها در آشفتگی هستند. خواهیم دید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/23439" target="_blank">📅 08:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رویترز:
قیمت نفت برای سومین روز متوالی کاهش یافت؛ برنت حدود
۱۰۴ دلار
و WTI حدود
۱۰۱.۲۰ دلار
معامله شد. کاهش نگرانی‌ها درباره اختلال طولانی‌مدت در صادرات عربستان، از جمله تلاش برای بازگرداندن بخشی از ظرفیت خط لوله شرق-غرب، عامل اصلی کاهش قیمت عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/23438" target="_blank">📅 08:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق جنگ با یاشار: اگر پرونده ایران در شورای امنیت به رأی‌گیری برسد، باید بین دو حالت فرق بگذاریم: اگر رأی‌گیری درباره یک قطعنامه معمولی و الزام‌آور باشد، روسیه یا چین می‌توانند با وتو جلوی تصویب آن را بگیرند. اما اگر رأی‌گیری از نوع رویه‌ای باشد، روسیه و…</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/23437" target="_blank">📅 07:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6a10ce6c.mp4?token=uIb5do5CBNrTD1S4hDPnq9Jz3cKWJfBO-UKTl2fI7MOBHywSkeZ4-C5dltnJM_NBAUJbWHgH2A0L4CAzMZjExZDuxR4su_sYIHyFAIyE6Zpzam2OwJIPnRk6E4Rbf_4BhnF-OrZq0euGYRQupy8zMKOJnBFYzSpA_VVe2sZ1DD0deYCQmVtENdqZwtgygmOiNC9kiS2ASI25pOsqcSGPr700hcwNrp-_GfFom2_H93dp0q4RzIzYtSfEmi2vAYp0iIUbs_MmV0NGyBdHM7HNaJMZXF1QwF53wG-Y8NAdhvTw5vn8IYoQGQ6gA9jrt_Ic0nTj43rkRcfKVvlwxI9VpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6a10ce6c.mp4?token=uIb5do5CBNrTD1S4hDPnq9Jz3cKWJfBO-UKTl2fI7MOBHywSkeZ4-C5dltnJM_NBAUJbWHgH2A0L4CAzMZjExZDuxR4su_sYIHyFAIyE6Zpzam2OwJIPnRk6E4Rbf_4BhnF-OrZq0euGYRQupy8zMKOJnBFYzSpA_VVe2sZ1DD0deYCQmVtENdqZwtgygmOiNC9kiS2ASI25pOsqcSGPr700hcwNrp-_GfFom2_H93dp0q4RzIzYtSfEmi2vAYp0iIUbs_MmV0NGyBdHM7HNaJMZXF1QwF53wG-Y8NAdhvTw5vn8IYoQGQ6gA9jrt_Ic0nTj43rkRcfKVvlwxI9VpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : سلام یاشار جان زاهدان حدود ساعت 12 نیم بامداد امشب درگیری افراد مسلح شروع شد تا همین الان درگیرن صدا تیر میاد بین خیابون دانشگاه و دانشجو خیلی کشته دادن حدود 9 تا امبولانس فقط امده بود سر صحنه
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23436" target="_blank">📅 02:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزیر دفاع ایتالیا: ما کشتی‌های جنگی خود را مستقر خواهیم کرد تا از عبور ایمن در تنگه باب‌المندب اطمینان حاصل کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23435" target="_blank">📅 01:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایلی دریایی شمال شرقی خصب در عمان دریافت شده است. بر اساس این گزارش، هیچ خسارتی به کشتی وارد نشده و هیچ‌یک از خدمه نیز زخمی نشده‌اند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23434" target="_blank">📅 01:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش حمله پهپادی رژیم به کمپ های کرد های عراق اطراف اربیل
شبکه المیادین از شنیده شدن صدای انفجار در منطقه «مصیف» واقع در حومه اربیل، مرکز اقلیم کردستان عراق خبر داد.
همزمان منابع غیر رسمی از به پرواز در آمدن هواپیماهای جنگی آمریکایی در اطراف این شهر خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23433" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23432" target="_blank">📅 01:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23431" target="_blank">📅 01:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اتاق جنگ با یاشار: آیا حلقه اطلاعاتی آمریکا درباره شبکه‌های جمهوری اسلامی در حال گسترش است؟!   یکی از احتمالاتی که می‌توان درباره بازگشت برخی چهره‌ها و افراد ایرانی به کشور مطرح کرد، گسترش دامنه دستگیری‌ها و تحقیقات آمریکا درباره افرادی است که با جمهوری اسلامی،…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23430" target="_blank">📅 01:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W432Stfs3gkDiMeVlhlwH0og6ArKsogBw5KT3sIfmgghwkYVfmlUbywpcTCsLoItgDShe51V8SMKWmPAapDRLSvnJ0WoX7BwH3yPTXvhoDb_uJpvSPa4c5fzLrOHyfyoGKpcpm9WNm_86ONbSvzUFNnYVwDkQVLUivhd8wFo7BtyKjeQboLQNoJhM0iQ8Wk5jpEebzsrG1v55ZmVuUVcPZiIzyxe3DtDlTD-XK5llRNcXtM7hb8AC0NAB01hvDieTOQjKI3KzhK1buvQ9NCZ3nhdJgBw4HdVTmqadd8oSyBrSgeXWUgY9lQFh159bkXdHIK64BZYTNLFidVKAW17Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار: آیا حلقه اطلاعاتی آمریکا درباره شبکه‌های جمهوری اسلامی در حال گسترش است؟!   یکی از احتمالاتی که می‌توان درباره بازگشت برخی چهره‌ها و افراد ایرانی به کشور مطرح کرد، گسترش دامنه دستگیری‌ها و تحقیقات آمریکا درباره افرادی است که با جمهوری اسلامی،…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23429" target="_blank">📅 01:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23428" target="_blank">📅 01:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23427" target="_blank">📅 00:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">میدل ایست آی: دونالد ترامپ «وسلی هانت»، نماینده جمهوری‌خواه تگزاس، حامی سرسخت اسرائیل و از منتقدان شریعت اسلامی را به عنوان سفیر بعدی آمریکا در عربستان سعودی معرفی کرده است. هانت، افسر سابق ارتش آمریکا، پیش‌تر دو سال به عنوان افسر رابط دیپلماتیک در عربستان خدمت کرده بود. این انتخاب در شرایطی حساس برای روابط آمریکا و کشورهای خلیج فارس و همزمان با جنگ ایران و آمریکا و تشدید درگیری‌ها در یمن انجام شده است. انتصاب هانت برای نهایی شدن به تأیید سنای آمریکا نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23426" target="_blank">📅 00:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23425" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پدافند شرق تهران درگیر شد ، اگه ادامه دار بود گزارش بدید</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23424" target="_blank">📅 00:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSina</strong></div>
<div class="tg-text">داداش فکر کنم دارن تهران و میزنن
هم صدای جنگنده اومد هم صدای انفجار شیشه‌های خونه ما لرزید مادرم از ترس رفت پایین
شرق تهرانم</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23423" target="_blank">📅 00:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSemiramis</strong></div>
<div class="tg-text">پدافند پاسداران داذه همینجور میزنه</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23422" target="_blank">📅 00:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پدافند تهران فعال شده و صدا ناله های شاش قاسم میده همه ترسیدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23421" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23420">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23420" target="_blank">📅 00:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23419" target="_blank">📅 00:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23418">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23418" target="_blank">📅 00:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23417" target="_blank">📅 00:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23416" target="_blank">📅 00:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23415" target="_blank">📅 00:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صدای ناله های تنگسیری از قشم شنیده میشه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23414" target="_blank">📅 00:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نه دیگه بهمن پنجاه و هفته
نه حرف برق مفت و پول نفته
نمی‌ذارم سر من هم بذارن
کلاهی که سر بابام رفته
شاهرخ
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23413" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23412" target="_blank">📅 23:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23411" target="_blank">📅 23:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385ac22afd.mp4?token=fSlh8i8r4zqwPkizG0_c9UbpV8STtWVaC0zi3WhLPLshItzp991TcWTFKmbWCifQ5wotd9IbUWVNAlpWrxrwRs0_3B8Y0Rf4xLKBcMwBu4_oVuEXJXebkYG6sw_nqcHY4ha_EPNAdNka86aIWVimCGvF0uID2pYBD0lY6GrCoUryfcD2DfuN8CnOV51TJvMtdi6HwtrK3RuzE6gEfLEEhET0vR3_EoLmTyMrZG5FdPr9zvzT-Vs9OIei_menGavyciBK7kItPLfabLoakRstXdKSZAtHTIDZgsyR7wjaASEIIvGAfTn97T9oBqMwufVW4tSOZT_t_f8XYy4zz97Dmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385ac22afd.mp4?token=fSlh8i8r4zqwPkizG0_c9UbpV8STtWVaC0zi3WhLPLshItzp991TcWTFKmbWCifQ5wotd9IbUWVNAlpWrxrwRs0_3B8Y0Rf4xLKBcMwBu4_oVuEXJXebkYG6sw_nqcHY4ha_EPNAdNka86aIWVimCGvF0uID2pYBD0lY6GrCoUryfcD2DfuN8CnOV51TJvMtdi6HwtrK3RuzE6gEfLEEhET0vR3_EoLmTyMrZG5FdPr9zvzT-Vs9OIei_menGavyciBK7kItPLfabLoakRstXdKSZAtHTIDZgsyR7wjaASEIIvGAfTn97T9oBqMwufVW4tSOZT_t_f8XYy4zz97Dmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نِتانیاهو درباره ایران: ما تومور را از بین بردیم و اکنون زنده هستیم. این بدان معنا نیست که تومورهای دیگری برای مقابله وجود نخواهند داشت!
@WarRoom
💥</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23410" target="_blank">📅 23:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23409" target="_blank">📅 23:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23408" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23407">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2C1ZPGxx9845azFCjbw7sXScbmwq-fzanABNC0-IJxpDfrxRL0Pz6dA5XPq2ExECdj3-PE4FZzWiVis9Ml49DD65zwVnc4K68azVYi7C0C8wszfmrinSuRxGHAAxPej2WkHH9RfN0gnUBp23rNA2XESh5RCzPPeq66acZGhKOiPbdSaYQkucU4kv4uvmpvBxrbjGQdrkLXbJUyZqfC8evZ1KS8t0ltc2igJIub4EvKyBzxM6JzBvw-vpty8Ml7GoOY3pQqlrliBYFck1PV1MpnjufEOzowCgJtXKntbzLIQ63cYuh1IUIx-hB8olBKAmavqaVw2fALMlHfyCZ75HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23407" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23405" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23404">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">page2 :
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23404" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23403">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شبکه کان اسرائیل : کویت و اسرائیل در حال انجام مذاکراتی سری به دلیل حملات ایران به کشورهای منطقه، از جمله خود کویت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23403" target="_blank">📅 23:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23402">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5129cb70.mp4?token=n-HIn0FhnwRE7CU5rcMcmTg0s4ZCWLWCV7XvhJLf4kNYpEcM-8dcoK_ESnMTyQqzpuh8XNkjAe2YAlgK953BpzE_lFRP4OtpzM6etu80O6rL50ey0l7NDD-h3XUD59cu8O3De0NlmugGEleRezkcFZ43l2C2ueNDVLAMZ8nWfBvQq41DRqBsNpeT3e2fpYEJmf1sevPCtrGWh1amwU0fkJr0qHIghAoxheOGxsVmK8cAjuezvMbNugRC_aY2d7364acGTRbhoe7s1u_7dck5OlEI0hlNgaTzlE2d7KQoODTLP9CaPJBRGwV1UDsHnF9y6wynQIddeIrUBcoDU6o4Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5129cb70.mp4?token=n-HIn0FhnwRE7CU5rcMcmTg0s4ZCWLWCV7XvhJLf4kNYpEcM-8dcoK_ESnMTyQqzpuh8XNkjAe2YAlgK953BpzE_lFRP4OtpzM6etu80O6rL50ey0l7NDD-h3XUD59cu8O3De0NlmugGEleRezkcFZ43l2C2ueNDVLAMZ8nWfBvQq41DRqBsNpeT3e2fpYEJmf1sevPCtrGWh1amwU0fkJr0qHIghAoxheOGxsVmK8cAjuezvMbNugRC_aY2d7364acGTRbhoe7s1u_7dck5OlEI0hlNgaTzlE2d7KQoODTLP9CaPJBRGwV1UDsHnF9y6wynQIddeIrUBcoDU6o4Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد بزرگ شطرنج ، نتانیاهو: من مسیح نیستم و(کینگ) پادشاه هم نیستم. پادشاه نیازی به انتخابات ندارد؛ من باید انتخاب شوم.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23402" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1019a561.mp4?token=Cl1hc1V-BGkNW1pScEd-HcZelIMgzcTSrMCjk1b4bs6sbl01O7m2E-njrLKsXOhD7h8nZNKZclplnYMEcYgoUOGJPBw9qPPT6TAd6y5785hU6nJPpDvB9bAI01_7VMi2LO_LLtPItBZEyMmMGw5gwK3mWvwLhwh6IBsv58RKj54Ti3Jv_bwnbVgtUnPL1_Deh9cisgaXEanVg2ZC3ajURUor5qSwEZrTVejBBcc29Uif4J7fCZZRPDWqFE3ZJ5BXMIIniH1kVSjxv6ZhOulDXkP1oZtYNO3JNAY7HqOtOKSYJssfhl3wLLOAJNPiyrtgE_ijIJQyoTeC2UEEsDoiFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1019a561.mp4?token=Cl1hc1V-BGkNW1pScEd-HcZelIMgzcTSrMCjk1b4bs6sbl01O7m2E-njrLKsXOhD7h8nZNKZclplnYMEcYgoUOGJPBw9qPPT6TAd6y5785hU6nJPpDvB9bAI01_7VMi2LO_LLtPItBZEyMmMGw5gwK3mWvwLhwh6IBsv58RKj54Ti3Jv_bwnbVgtUnPL1_Deh9cisgaXEanVg2ZC3ajURUor5qSwEZrTVejBBcc29Uif4J7fCZZRPDWqFE3ZJ5BXMIIniH1kVSjxv6ZhOulDXkP1oZtYNO3JNAY7HqOtOKSYJssfhl3wLLOAJNPiyrtgE_ijIJQyoTeC2UEEsDoiFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران: اول از همه، ما باید رژیم ایران را سرنگون کنیم. این مأموریت من است و این مأموریت اصلی ماست.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23401" target="_blank">📅 23:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctzkWHrLiESOM-cHwlRB2jliG1LZYf2Ux6r9bONhTgTjMLY87WN1gxTQVRBAn29vobN-eDyy1XoEQv48R7iFB8BYW6gxKgCzmmRTCVMfyrUkMI8xwL2ewV9gp2QN9Kgkn6Vt0hcXa2XL_zs6Qz9kDcibdRzdxIL-OftLkkv9Iosa0MGE9mp3a22pIfmsNZmvAehYkSGPRx_ElHfpDh5lEs4oxJ-jeTII8u8CBW7JtLzlJAZ1bV5n_PF-Z69GkS85rSg99_O9QKaivFPYoHzRBtW70LWH66ujKQ_ndL8VqdWYWHtE9Fd845y9KMRgmdNHuS5deTjT3mWOu1tIrLYp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایلی دریایی شمال شرقی خصب در عمان دریافت شده است.
بر اساس این گزارش، هیچ خسارتی به کشتی وارد نشده و هیچ‌یک از خدمه نیز زخمی نشده‌اند.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23400" target="_blank">📅 23:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش پرتاب موشک‌‌ از لارک به سمت تنگه.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23399" target="_blank">📅 23:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تنگه صدای ناله های مرحوم تنگسیری ‌میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23398" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا اعلام کرد صرافی رمزارزی «بیت‌بانک» متعلق به شبکه مالی بابک زنجانی است. بر اساس اعلام خزانه‌داری آمریکا، بیت‌بانک تحت کنترل بابک زنجانی قرار دارد و شرکت «پیشتاز سیمرغ تجارت الکترونیک» نیز به‌عنوان توسعه‌دهنده نرم‌افزار این صرافی معرفی شده است. آمریکا در همین ارتباط بیت‌بانک و افراد و شرکت‌های مرتبط با شبکه زنجانی را تحریم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23397" target="_blank">📅 22:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یک مقام آمریکایی: برای ایران ویزاهایی جهت حضور در نشست‌های سازمان ملل صادر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23396" target="_blank">📅 22:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو: ما کار این رژیم را تمام خواهیم کرد ، به‌زودی غافلگیری‌ای در انتظار ایران است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23395" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو در کنفرانس حزب لیکود، روایت ترامپ را تکرار کرد: ما اسرائیل را از نابودی نجات دادیم، و اگر این اتفاق نمی‌افتاد، احتمالاً کشور اسرائیل وجود نداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23394" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تایمز اسرائیل
: سه میلیارد دلار بمب تخریب گر در راه اسراییل برای دور جدید حملات.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23392" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تحریم‌های تازه آمریکا علیه یک صرافی رمزارز و کوبا
آمریکا پلتفرم ارز دیجیتال «بیت‌بانک» را به اتهام همکاری با ایران تحریم کرد.
واشنگتن همچنین تحریم‌های جدیدی را علیه کوبا اعمال کرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23391" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ :تصمیمات آتی را با 6 کشور عربی خلیج فارس و اعضای شورای امنیت سازمان ملل بررسی خواهیم کرد.امیدوارم ناتو از فاز بی مصرف بودن خارج شود وگرنه دیگر برای آنان هیچ هزینه‌ای نمیکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23390" target="_blank">📅 21:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">واشنگتن با فروش احتمالی ۴۸ فروند جنگنده از نوع F-35 به عربستان سعودی موافقت کرده است. ارزش این قرارداد حدود ۲۴.۳ میلیارد دلار تخمین زده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23389" target="_blank">📅 21:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سی‌بی‌اس
: سپاه پاسداران انقلاب اسلامی در روزهای اخیر، حداقل دو فروند از هواپیماهای بدون سرنشین مدل MQ-1 متعلق به آمریکا را سرنگون کرده‌اند، اگرچه هنوز مشخص نیست این حوادث در کجا رخ داده‌اند و کدام مدل خاص از این هواپیما درگیر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23388" target="_blank">📅 21:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به آکسیوس : می‌خواهم از جلسه عمومی سازمان ملل (هفته بعد) استفاده کنم تا مستقیماً از متحدان منطقه‌ای درباره گام‌های بعدی جنگ بشنوم @WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23387" target="_blank">📅 21:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed20696f0.mp4?token=Br5AYqp1DuNlA6UtPZe9elx7Dg3EfDt_czEus_JvhGct-n8n5qseCYdzANUvR9UzHyfhoU4EFJeJRlots6k7uuoamYM2HB72oKYhkV5tW_6FFfz64qHXlWsHNEQSvmj7By45fgqwFnbIVV7nqST8rcJDm_aq-Jh58KbLIqoteL_tNwAZ6CW7Zv8AoXcrXhcdAPqse1i6YPe5QLK9ak7BiOrtVJdKRk8wiNOWdVPzBALAc5GYKkZvCRqoumzyvKDRcu70L5HBQr1dpVEvwfvOZYuYDePFDrGosQt8-HcZ7a1VbbvJessRdhaH2We3AReDGLlGA43gKAOChlT0TdXkwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed20696f0.mp4?token=Br5AYqp1DuNlA6UtPZe9elx7Dg3EfDt_czEus_JvhGct-n8n5qseCYdzANUvR9UzHyfhoU4EFJeJRlots6k7uuoamYM2HB72oKYhkV5tW_6FFfz64qHXlWsHNEQSvmj7By45fgqwFnbIVV7nqST8rcJDm_aq-Jh58KbLIqoteL_tNwAZ6CW7Zv8AoXcrXhcdAPqse1i6YPe5QLK9ak7BiOrtVJdKRk8wiNOWdVPzBALAc5GYKkZvCRqoumzyvKDRcu70L5HBQr1dpVEvwfvOZYuYDePFDrGosQt8-HcZ7a1VbbvJessRdhaH2We3AReDGLlGA43gKAOChlT0TdXkwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر شبکه فاکس‌نیوز از بمب‌های سنگرشکن و ۲۰۰۰ پوندی آمریکایی داخل ناو جورج واشنگتن تا دندان مسلح برای حمله به ایران
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23386" target="_blank">📅 20:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آکسیوس به نقل از مقام آمریکایی: نیروهای آمریکایی مستقر در خاورمیانه برای احتمال یک درگیری تمام‌عیار با ایران در آماده‌باش هستند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23385" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23384">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ به آکسیوس : «آیا وارد شوم و آنها [رژیم ایران] را نابود کنم یا نه؟ این یک تصمیم بزرگ است. هر اتفاقی ممکن است از سوی من رخ دهد.»  @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23384" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ به نشریه "اکسیوس" گفت: من در آستانه اتخاذ یک تصمیم مهم در مورد ایران هستم. @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23383" target="_blank">📅 20:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ به نشریه "اکسیوس" گفت:
من در آستانه اتخاذ یک تصمیم مهم در مورد ایران هستم.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23382" target="_blank">📅 20:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نماینده ویژه سازمان ملل متحد در سوریه: اسرائیل، تقریباً به صورت روزانه، در جنوب سوریه نفوذ می‌کند، موانع مرزی ایجاد می‌کند و با توپخانه شلیک می‌کند، همچنین بازدید نتانیاهو از نیروهای اسرائیلی در کوه شیخ، یک نقض دیگر از حاکمیت سوریه است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23381" target="_blank">📅 20:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23380">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نیروی دریایی بریتانیا اعلام کرد گزارشی درباره وقوع یک حادثه در فاصله ۷۵ مایل دریایی شرق عدن در یمن دریافت کرده است.بر اساس این گزارش، یک قایق اقدام به تعقیب یک نفتکش کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/23380" target="_blank">📅 19:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23379">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی ایالات متحده اعلام کرد که ارتش آمریکا در راستای اجرای محاصره دریایی و تضمین رعایت قوانین، تا امروز در مجموع به ۱۰۴ کشتی که در تلاش برای نقض این محاصره بودند، دستور تغییر مسیر داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/23379" target="_blank">📅 19:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWTfmj9lv4d76ALVvSdWuAsErH9O2Vzm2B8qV9p9mriUFTLQ4CiF6fuiEy6tdzyzO14NUwc0jUB550sRv4NznJdGa1SU5XEGMXaGkNdhyDXH12C96FZtO_MVHgHr9mdd0sWGMu9Mv6z89K5NhoD0l7G9rACoBeNwNNyk4N-lVGi8X9c-5YLJUD3NOm75mf0SVrcCuRwyDwVCtipcRVWJfTupVoGuQHkommX1reeg29ikNWyNCq0b6_fWvmPSuW0wFp4rI5tR5hDz1ZrSIpKDtqqVb7ICf31JFwNbd01WpexgAUT4i27OAeWA2DES9D60GOCo5xAPf4EuqrMGDLkA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار :
تصاویر ماهواره‌ای جدید نشان میدهد
ایران در حال بازسازی سریع تأسیسات طالقان ۲ است:
تصاویر ماهواره‌ای شرکت وانتور از ۱۳ سپتامبر ۲۰۲۶ نشان می‌دهد ایران بازسازی تأسیسات طالقان ۲ در مجموعه نظامی پارچین حدود ۳۰ کیلومتری جنوب‌شرق تهران را با سرعت پیش می‌برد. ایران روی بخش تخریب‌شده و مدفون تأسیسات یک پوشش برزنتی نصب کرده تا فعالیت‌های بازسازی زیر آن از دید ماهواره‌ها و شناسایی هوایی پنهان بماند. در محل، کامیون‌های حمل خاک، بولدوزر، پمپ و کامیون بتن و جرثقیل‌ها فعال هستند. بازسازی از ژوئن آغاز شد و ابتدا سوراخ‌های ایجادشده بر اثر اصابت چند بمب سنگرشکن (بمب مخصوص حمله به تأسیسات زیرزمینی) با بتن ترمیم و پوشانده شد. همچنین یک سازه بتنی تقویت‌شده جدید در سمت راست تأسیسات ساخته شده و سازه مشابه در سمت چپ که در ژوئیه شناسایی شده بود، اکنون ظاهراً تکمیل شده است. این سازه‌ها حفاظت بیشتری در برابر انفجار و حملات هوایی ایجاد می‌کنند
با این تصاویر الان مشخص می‌شود که
ستون دود امروز در پارچین برای باز کردن حفره‌های مسدود شده و عملیات بازسازی در این تأسیسات
می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23378" target="_blank">📅 19:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rig0ae8Yck41qdyoypsJiW7Eh-7ms2Qu_6cmV1dL6IO-0oybA9_9vt52l5Ur--rbMLTzASjUECObfoKJHqKmeS3OKFi1L9tclSa5FHkHpv8MOjpY4t9MmSGMvuu3wW30XMuL7zWCtMQX2kxf4REVBnqkFNlz6uIj43ph7T79Jc4emnDFq20LQtDhYBdhecDzwi1Oj_yBjOPRDL67B5vlWtqiK-xz_9GnyKZMdMNepTWayo5DT2wXZs9mPlLB9hj8hIdDTudDLy8X0WmQjoNptV05_CV-_W0lAObP8oEK2Ek7OIR3TeV-_1XFXgPCVzNkEbZ-243Xh3OMmnq-3XzzeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر تبلیغاتی جان فدا در تهران، آموزش رایگان سیستم‌های دفاع هوایی دوش پرتاب (MANPAD) را به شهروندانی که مایل به داوطلب شدن هستند، ارائه می‌دهد.
@WarRoom
😟</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/23377" target="_blank">📅 19:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23376">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مسعود بهنود روزنامه‌نگار قدیمی و ریاکار که در دو جنگ دوازده روزه و ۴۰ روزه هم حامی حکومت بود، خبر داد تا پیش از نوروز به ایران باز می‌گردد وی سابقه طولانی در همکاری با رسانه‌های خارج از ایران، از جمله به عنوان سردبیر و تهیه‌کننده در بخش فارسی بی‌بی‌سی دارد…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23376" target="_blank">📅 18:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رویترز: در پی درخواست عربستان سعودی از پکن پس از حمله نظامی برق‌آسای حوثی‌ها در هفته گذشته، چین مخفیانه از تهران برای آرام کردن شورشیان حوثی در یمن درخواست همکاری کرده است. @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23375" target="_blank">📅 18:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جمهوری اسلامی عضویت آمریکا در شورای حکام را مغایر اساسنامه آژانس بین المللی انرژی اتمی دانست
هیأت جمهوری اسلامی امروز در بیانیه‌ای ذیل بند هشتم دستور کار این کنفرانس با عنوان «انتخاب اعضای شورای حکام» تأکید کرد که حضور آمریکا در این شورا، به کشور متجاوز اجازه می‌دهد درباره موضوعاتی داوری کند که مستقیماً با اقدامات غیرقانونی خودش مرتبط است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23374" target="_blank">📅 18:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به گزارش وال‌استریت ژورنال،
جنرال موتورز (مالک شورولت، کادیلاک، جی‌ام‌سی، بیوک و هامر)
برای نخستین‌بار برای
لاکهید مارتین
قطعات بدنه موشک‌های رهگیر
پاتریوت PAC-3 MSE
تولید کرده و نخستین محموله را در ماه اوت تحویل داده است. این همکاری با هدف
افزایش سریع تولید موشک‌های پدافندی آمریکا و جبران کاهش ذخایر
انجام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23373" target="_blank">📅 17:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12eec9e29.mp4?token=eZQ0L-d3mJmXZEMN8lcJoIH-0oH9Ik-hOra6Ehsu4IB6YbHtVjMCwgoQWnWoPsWiVXkm4yZtleZh7RzP17ubXpiI9nWFa0yUZdYYK-H2mYUooD0dX23z4A3e6td-plBVVdILL-yqteqIu7QQPId2nfgvB4Y9rlobYG_C5wjiGA9e8TavTkqh9r03vJttSWxxJ0LMO6b_OVWVle6OCdylv0dd7kOx5ZWYI-Riwd7QPELbrYGGD9J41V87jyQKY80c8dEspp5IxEnKY--qFp0VY_vKqg2nr2M99B6rxLa2tuJdH5eiryCOuPzrpiDuS0ADYpxx6WtnWq_38tVv2kSaQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12eec9e29.mp4?token=eZQ0L-d3mJmXZEMN8lcJoIH-0oH9Ik-hOra6Ehsu4IB6YbHtVjMCwgoQWnWoPsWiVXkm4yZtleZh7RzP17ubXpiI9nWFa0yUZdYYK-H2mYUooD0dX23z4A3e6td-plBVVdILL-yqteqIu7QQPId2nfgvB4Y9rlobYG_C5wjiGA9e8TavTkqh9r03vJttSWxxJ0LMO6b_OVWVle6OCdylv0dd7kOx5ZWYI-Riwd7QPELbrYGGD9J41V87jyQKY80c8dEspp5IxEnKY--qFp0VY_vKqg2nr2M99B6rxLa2tuJdH5eiryCOuPzrpiDuS0ADYpxx6WtnWq_38tVv2kSaQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : ستون دود عظیم و قارچی شکل ، مشهد شهرک شهید رجائی ، صدای انفجار هم  اومد ، محدوده جایگاه سوخت جت مصطفی خمینی
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23371" target="_blank">📅 16:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کاهش قیمت نفت با تغییر مسیر صادرات عربستان
قیمت نفت پس از گزارش‌هایی درباره انتقال بخشی از نفت عربستان به آسیا از مسیر
عمان
کاهش یافت. عربستان در دوره تعمیر خط لوله «شرق به غرب» قصد دارد بخشی از نفت را با
انتقال کشتی‌به‌کشتی در نزدیکی بندر صحار عمان
به پالایشگاه‌های آسیایی برساند؛ اقدامی که نگرانی‌ها درباره اختلال در عرضه جهانی را کاهش داده است. نفت برنت با ۳.۵
درصد کاهش به ۱۰۲.۲۸ دلار
در هر بشکه رسید.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23370" target="_blank">📅 16:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بنیاد دفاع از دموکراسی‌ها (FDD) می‌گوید طی شش ماه گذشته دست‌کم
۲۵ افسر و فرمانده نظامی و امنیتی سوریه
در مواردی که علت مرگشان
«حمله قلبی» یا «ایست قلبی»
اعلام شده، جان باخته‌اند. FDD تأکید می‌کند
هیچ مدرکی برای ارتباط این مرگ‌ها یا غیرطبیعی بودن آنها وجود ندارد
، اما سابقه حکومت اسد در اعلام «حمله قلبی» برای برخی زندانیان و مرگ‌های مشکوک باعث شده این موارد در سوریه حساسیت و شایعات زیادی ایجاد کند. برخی احتمال می‌دهند این مرگ‌ها با
تغییر ساختار ارتش و کنار گذاشته شدن فرماندهان سابق شورشی
مرتبط باشد، اما سوابق قربانیان چنین الگوی مشخصی را تأیید نمی‌کند. دولت سوریه نیز تاکنون توضیح جامعی درباره این روند ارائه نکرده است. FDD نتیجه می‌گیرد که مشکل اصلی،
بی‌اعتمادی تاریخی به روایت رسمی حکومت
است؛ به همین دلیل «حمله قلبی» برای برخی سوری‌ها اکنون می‌تواند معنایی فراتر از یک علت پزشکی داشته باشد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23369" target="_blank">📅 16:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23368">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xcsd5qU7mEhhoGbGB0cmDl4ETFGI7cwyxHWLJp9VNVT8GofVEquLH8EEnnCPYfxXtPS1F2BAe0j7eMuTHJiPypm6nFO9va42SIJuz8T_wNimsbbQ-L11ghT_LNmCPQxXupU8hnJnC1jlENd9SzXlBMfnJKlTUrggKQjjhfBa15vKPaqrPyCxA0ufefvAPBfw-2sUMnbBm-rJXCDlhwoEfQ06-boSwfMu8fRqtiAeGWXJ8GjuyUaNKZC-oAnMtKc2GoKtVLNCPRUZ1AiLdPgFWeFHA30G-zMamPPPkA89h4HMQDgGss2OK8_nUMvuGLsTcqrNsiQHrbptfAiSL93MXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود بهنود روزنامه‌نگار قدیمی و ریاکار که در دو جنگ دوازده روزه و ۴۰ روزه هم حامی حکومت بود، خبر داد تا پیش از نوروز به ایران باز می‌گردد
وی سابقه طولانی در همکاری با رسانه‌های خارج از ایران، از جمله به عنوان سردبیر و تهیه‌کننده در بخش فارسی بی‌بی‌سی دارد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23368" target="_blank">📅 16:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رویترز: در پی درخواست عربستان سعودی از پکن پس از حمله نظامی برق‌آسای حوثی‌ها در هفته گذشته، چین مخفیانه از تهران برای آرام کردن شورشیان حوثی در یمن درخواست همکاری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/23367" target="_blank">📅 15:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzZo-FQivemjn-XlE1ViOyvfRfZZZRjmQPhLhtEJQwvuz9y3hjbhZufuQaUU4wWxeUQ4IA6KScBjv-lm3aUYmpCzu3v5P9uH1_xBDJGWd5kJTNy7KvLHxRC7mHVipvL0t0y2oqrS8qUjxiQXteA2Nv1y_FntKXgNT8_vZQLgiTjtkkJNlWE3NONNa18dI3Opmxm6poXM_BCREgu5MKwEeTXVVnsUaK48TH4jzyyotRG2KZIi1psnZI69GCfmAscw5dsOH0lyEgfB65yq8NywjeXZJmSjaPVSgNS-scDoC6bz9-gswURVHcim_2z5JEm-KBXbYFtiulH_QEy1bijMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود تهران پارچین
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23366" target="_blank">📅 15:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7807d87071.mp4?token=T3FAvLDau0HmTsPY9Ti_CYOnz4lS0uDodrugd9jKfD02ZGW7toeMqzILvgj82XRcA3d8cTVCoqEAs04WGUfZF7bH7TAnU96mGVUnLAxEGNgZkEZpjbWvmujcH-khQpuf06nDv-o4Dl-JROZd2Ish4J_5sG6p5DB_kp2si9VWqQYxacEWC3hgmpQV5nAJajhq7xF_R3ZL12nf8tC8290PVll031dByr9O7hnAvaL1VDgdseHMxcbLXfuTOxZIWQ-Tm6jCDBU857AHHVNDUVwpAISkjrEGA_iRabbg8LiHqrEotRShEfxrS7_DcUZyoNFd6tLCroqW5kbYPU2NFf6dTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7807d87071.mp4?token=T3FAvLDau0HmTsPY9Ti_CYOnz4lS0uDodrugd9jKfD02ZGW7toeMqzILvgj82XRcA3d8cTVCoqEAs04WGUfZF7bH7TAnU96mGVUnLAxEGNgZkEZpjbWvmujcH-khQpuf06nDv-o4Dl-JROZd2Ish4J_5sG6p5DB_kp2si9VWqQYxacEWC3hgmpQV5nAJajhq7xF_R3ZL12nf8tC8290PVll031dByr9O7hnAvaL1VDgdseHMxcbLXfuTOxZIWQ-Tm6jCDBU857AHHVNDUVwpAISkjrEGA_iRabbg8LiHqrEotRShEfxrS7_DcUZyoNFd6tLCroqW5kbYPU2NFf6dTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ فقط تضعیف شده است.
توانایی آن‌ها برای عملی کردن این هدف، اساساً به‌شدت آسیب دیده است. ما وظیفه خود را انجام داده‌ایم، اما هنوز کارهای بیشتری برای تکمیل باقی مانده و آن‌ها را تکمیل خواهیم کرد. ما حماس را از بین خواهیم برد. همچنین ابتدا رژیم ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23365" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امروز، دومین سالروز بزرگداشت عملیات فرخنده «پیجر» در لبنان است؛ عملیاتی که در ۱۷ سپتامبر ۲۰۲۴ انجام شد
دو سال پیش در چنین روزی هزاران دستگاه "پیجر" در مناطق مختلف لبنان و بخش هایی از سوریه منفجر شدند ، این دستگاه ها توسط نیروهای حزب الله و سپاه استفاده می شدند
@WarRoom
🎂
🍬
💥</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/23364" target="_blank">📅 15:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-jesjqr5L5z8gOfwwC7TRHolr1bMMY1KgBgnyXL8xnwkBXpR46UVwyDWDkCAMGu59oemW5oWRn478pHXLCc_GKbZH8WcuT87GodX6_2bJA6LDz6Yk4tynQ0N6n2uVMn6cIEgqt8GIG3fo_TLsJf2XQcMaQsC4c8kdP1jtVrxEeIjQuPVZGZGGfh_SIyYv2a_aHGMx5v3o4qyEXmkk8G0rAfAOuWQDy3TLQg92c7GfQSx9GOt7-w3w3qAsmE-EJKqiFjPNYMcvfl9xSeFO4adUkYIv8gmBuumhoLq7ZkRvr4voJKpctsll_dxX3msnReQNkFksqAoOZZUQR8u1WTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار :
پرواز مشکوک
یک فروند
CMV-22B اوسپری
با کال‌ساین
MEDEVC11
از روی یکی از ناوهای آمریکایی مستقر در
دریای مکران
به پرواز درآمده و در حال حرکت به سمت یکی از کشورهای حافظ منافع آمریکا در خلیج فارس . استفاده از عبارت
MEDEVAC
در ارتش آمریکا نشان می‌دهد پرواز با مأموریت تخلیه یا انتقال پزشکی انجام می‌شود؛ بنابراین یکی از احتمالات، انتقال پرسنلی است که پیش‌تر مجروح یا دچار مشکل پزشکی شده است. با این حال، از روی کال‌ساین به‌تنهایی نمی‌توان تأیید کرد که فرد در جریان حادثه جدید آسیب دیده یا قرار است پس از درمان به مأموریت بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23363" target="_blank">📅 15:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23362">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر جنگ اسرائیل، کاتس:
به رژیم ایران یا هیچ گروه دیگری اجازه نخواهیم داد که حماس را دوباره مسلح کند. اگر اردوغان می‌خواهد به آن‌ها کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما او هرگز پایش را به غزه نخواهد گذاشت. نبرد با ایران و جبهه‌های دیگر همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23362" target="_blank">📅 14:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6TSLnE0uyvlAs5wdgRjezRCJ5LaXW_--9p4ipLJ5Ju-hoR9XxHKuipw_EkXANdpHayqVvEccSUTsUHIrrXGVd0bpLTrNXiQ10LieaOwvFKe-U5KjnhjlYNyNVQfyZiiGs78vz_E98-yCsQIwnrKCpBKclkS8X4e-ySS2tAzx35OebUKv5XgOB2un1s7Ug7B2oviL_q5pay5f6x-4nZsq2FC5O8mUSMQBt6bg2YcWD_kOx-Qai1ufLz825w_Vo07aaBJTFG0t_i77ptZt5fkvgPxylKCYzIOsXPwjGsFP7k7OqZ9kyOKvEMIEdtIPutVsi3DRJ9XoteQm7vbYDNRRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ۱۰ فروند F-16C متعلق به یگان ۱۴۸ جنگنده مینه‌سوتا (یک واحد عملیاتی نیروی هوایی آمریکا در ایالت مینه‌سوتا) صبح امروز از پایگاه لاجس پرتغال (LPLA) به سمت منطقه سنتکام حرکتکردند و با پشتیبانی سوخت‌رسان‌ها همراه هستند. این انتقال شامل دو سل(گروه پروازی) پروازی است: سل اول با F-16های TREND71 تا TREND76 و دو فروند KC-46A با کدهای BORA24 و BORA25؛ سل دوم با F-16های TREND81 تا TREND84 و دو KC-46A با کدهای BORA34 و BORA35. شماره بدنه‌های اعلام‌شده F-16ها شامل 91-0336، 91-0405، 91-0421، 91-0349، 90-0831، 91-0339، 92-0915، 91-0341، 91-0347 و 91-0406 است. شماره بدنه KC-46A با کد BORA35 هنوز تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23361" target="_blank">📅 14:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">علت گزارشهای انفجار دیشب تهران
بامداد پنجشنبه، انفجار و آتش‌سوزی در یک ساختمان پنج‌طبقه مسکونی در
محله فلاح تهران
رخ داده است. انفجار باعث آتش‌سوزی کامل یک واحد حدود ۷۰ متری و تخریب بخشی از دیوارهای سه واحد و چاهک آسانسور شده و حتی به ساختمان مجاور نیز خسارت زده است. حدود
۱۲ نفر
از ساختمان خارج شدند و یک جوان
۲۴ ساله
مصدوم شد. به گفته سخنگوی آتش‌نشانی تهران، علت حادثه
نشت گاز شهری از یکی از وسایل و ایجاد جرقه
اعلام شده است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23360" target="_blank">📅 14:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عربستان برای مقابله با حوثی‌ها به دنبال تشکیل ائتلاف منطقه‌ای و بین‌المللی است؛ ریاض از پاکستان، ترکیه، مصر و کشورهای غربی درخواست حمایت کرده است
آسوشیتدپرس به نقل از دو مقام منطقه‌ای گزارش داده عربستان سعودی که با کمبود موشک‌های رهگیر مواجه شده، از
فرانسه، بریتانیا، پاکستان و مصر
خواسته است برای مقابله با حملات موشکی و پهپادی حوثی‌ها،
سامانه‌های پدافند هوایی در منطقه مستقر کنند
. عربستان همچنین در تلاش است یک واکنش جمعی علیه حوثی‌ها شکل دهد؛ با این حال، منابع تأکید کرده‌اند که فعلاً
هیچ‌یک از این کشورها اعزام نیروی نظامی برای ورود مستقیم به جنگ را اعلام نکرده‌اند
و تلاش‌های دیپلماتیک مصر و عمان برای کاهش تنش ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23359" target="_blank">📅 13:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47dac3f1f6.mp4?token=ZRm5ZoLNz6eDgAvTay12mQ_gKVcTiLBM-NXL2KDCwD8k0YUmK-q0S4wfYgCoW5HH02pTdAejrl2f-y9kimgdf-7P5KLH1XDsIFaGRGM98meqFyVImaWqoP2gg15g0WvmHXTdchXhmV04aVq0cHYhWEOVp5YL0SL3zathITMHYHlVXgbtniBn-SmsuhpQQqjF6J5PtuR9iynziZl1dDLaSS62mUC1j-D7GB8_75ZEBhFtHARHusin3t0aTmV8Kg-Ecg6Z8PNTz5y_S4ka-E13SwTVrqOjrZpmR_GDjTNSGfGz6oK57uZ19G5s6jPa1Fd9_K4VmxlHdOhQDeVH3hvme2euSVadd7YDPeyMzZ_4PzjpH-SoTK9XtIes_BZtAa6af93CAQgvigDtl1ZV_YnZon6Ee7fATFUhsBRUb09tYHQhqy0Z8MfWqUy6hHsT-1KO_c8s_Pd3VFph5wIQcsQljC701-Sq9D5d1XP3Jag5PkzUAdK4CZasB5ekzrTPvTsIeF1GgK-5LLCU9Db5svEPbFNtrL6BMoZz4CbWzRVT2nmY_UUPtiMKFLyFJ2SUfXv3QEXz2hCo4a37e92vjzqjcDMT8wa37mWj7BZiv04o7t8JJKdUdmwKHWM6SjuDRCRAEY3KnTmGiONCZePpDs7zJVSXRi1yjaQDdoXNGov5d8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47dac3f1f6.mp4?token=ZRm5ZoLNz6eDgAvTay12mQ_gKVcTiLBM-NXL2KDCwD8k0YUmK-q0S4wfYgCoW5HH02pTdAejrl2f-y9kimgdf-7P5KLH1XDsIFaGRGM98meqFyVImaWqoP2gg15g0WvmHXTdchXhmV04aVq0cHYhWEOVp5YL0SL3zathITMHYHlVXgbtniBn-SmsuhpQQqjF6J5PtuR9iynziZl1dDLaSS62mUC1j-D7GB8_75ZEBhFtHARHusin3t0aTmV8Kg-Ecg6Z8PNTz5y_S4ka-E13SwTVrqOjrZpmR_GDjTNSGfGz6oK57uZ19G5s6jPa1Fd9_K4VmxlHdOhQDeVH3hvme2euSVadd7YDPeyMzZ_4PzjpH-SoTK9XtIes_BZtAa6af93CAQgvigDtl1ZV_YnZon6Ee7fATFUhsBRUb09tYHQhqy0Z8MfWqUy6hHsT-1KO_c8s_Pd3VFph5wIQcsQljC701-Sq9D5d1XP3Jag5PkzUAdK4CZasB5ekzrTPvTsIeF1GgK-5LLCU9Db5svEPbFNtrL6BMoZz4CbWzRVT2nmY_UUPtiMKFLyFJ2SUfXv3QEXz2hCo4a37e92vjzqjcDMT8wa37mWj7BZiv04o7t8JJKdUdmwKHWM6SjuDRCRAEY3KnTmGiONCZePpDs7zJVSXRi1yjaQDdoXNGov5d8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادثه برای یک کودک کار که میخواهد از سطل آشغال زباله بردارد. واقعا وضعیت در ایران دردناکه…
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23358" target="_blank">📅 13:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بحران در ایران‌ایر؛ ۹ هزار پرسنل برای تنها ۸ هواپیمای عملیاتی
طاهر عبدالحی، مدیرعامل ایران‌ایر، اعلام کرده این شرکت اکنون حدود
۹ هزار نیروی شاغل، نزدیک به ۱۳ هزار بازنشسته و مستمری‌بگیر و تنها ۸ هواپیمای عملیاتی
دارد. او وضعیت هما را «فلج» توصیف کرده و گفته این شرایط نتیجه چند دهه سیاست‌گذاری نادرست، هزینه‌های تحریم و مشکلات صندوق بازنشستگی است. مدیرعامل ایران‌ایر همچنین گفته
۱۰ هواپیمای عملیاتی این شرکت در جنگ اخیر آسیب دیده‌اند
و شمار هواپیماهای آسیب‌دیده ایران‌ایر در نقاط مختلف کشور ممکن است به
۲۰ تا ۳۰ فروند
برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23357" target="_blank">📅 13:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رویترز: بحران اقتصادی ایران، مهاجران افغانستانی را به بازگشت به کشورشان واداشته
افزایش شدید قیمت‌ها و کاهش ارزش ریال باعث شده پس‌انداز بسیاری از مهاجران افغانستانی در ایران از بین برود و درصدی از آن‌ها تصمیم بگیرند به کشورشان بازگردند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23355" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
